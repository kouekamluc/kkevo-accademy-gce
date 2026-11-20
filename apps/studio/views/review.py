"""Content review: teachers check each lesson against the syllabus, one lesson at a time.

The queue shows what is left by class and subject. The review page shows a lesson as students see it, with the
sentences the writers flagged ("check your textbook") as a tick-list. Approving needs every flagged sentence
ticked and the publish permission; it records the reviewer, which students see as "Checked by …", and logs an
event, which also stops `load_lessons --refresh` from overwriting the checked lesson.
"""

from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Count, F, Prefetch, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.academics.models import AcademicLevel, Subject
from apps.courses.models import BlockType, Lesson, LessonBlock, attach_videos
from apps.courses.review import fingerprint, lesson_flags
from apps.learning.models import LessonFeedback
from apps.practice.models import PracticeSet

from .. import revisions
from ..models import LessonEvent, LessonReview
from ._common import _context, can_publish, staff_required

PER_PAGE = 30
COURSE = "topic__module__course"
LEVEL = f"{COURSE}__offering__level"
SUBJECT = f"{COURSE}__offering__subject"
ORDER = [f"{LEVEL}__order", f"{SUBJECT}__order", f"{COURSE}__order", f"{COURSE}__title", "topic__module__order",
         "topic__order", "order", "pk"]
STATES = [("todo", "To check"), ("needs_fix", "Needs a fix"), ("checked", "Checked"), ("all", "All")]
TODO = Q(review__isnull=True) | Q(review__status=LessonReview.Status.IN_PROGRESS)


def _lessons():
    """Every lesson a teacher should check: all of them except archived ones."""
    return Lesson.objects.exclude(status="archived")


def _filtered(state, level, subject):
    qs = _lessons()
    if level:
        qs = qs.filter(**{f"{LEVEL}__slug": level})
    if subject:
        qs = qs.filter(**{f"{SUBJECT}__slug": subject})
    if state == "todo":
        qs = qs.filter(TODO)
    elif state in ("needs_fix", "checked"):
        qs = qs.filter(review__status=state)
    return qs


@staff_required
def review_queue(request):
    state = request.GET.get("state", "todo")
    if state not in dict(STATES):
        state = "todo"
    level = request.GET.get("level", "")
    subject = request.GET.get("subject", "")

    qs = (_filtered(state, level, subject)
          .select_related(f"{COURSE}__offering__level", f"{COURSE}__offering__subject", "topic__module",
                          "review__reviewer")
          .prefetch_related(Prefetch("blocks", queryset=LessonBlock.objects.order_by("order", "pk")))
          .order_by(*ORDER))
    page = Paginator(qs, PER_PAGE).get_page(request.GET.get("page"))
    for lesson in page:
        blocks = list(lesson.blocks.all())
        lesson.flag_count = len(lesson_flags(blocks))
        review = getattr(lesson, "review", None)
        lesson.changed = bool(review and review.status == LessonReview.Status.CHECKED
                              and review.fingerprint and review.fingerprint != fingerprint(blocks))

    scope = _lessons()
    if level:
        scope = scope.filter(**{f"{LEVEL}__slug": level})
    totals = scope.aggregate(
        total=Count("pk"), checked=Count("pk", filter=Q(review__status=LessonReview.Status.CHECKED)),
        needs_fix=Count("pk", filter=Q(review__status=LessonReview.Status.NEEDS_FIX)))
    totals["pct"] = round(totals["checked"] * 100 / totals["total"]) if totals["total"] else 0
    subjects = list(scope.values(name=F(f"{SUBJECT}__name"), subject_slug=F(f"{SUBJECT}__slug"))
                    .annotate(total=Count("pk"),
                              checked=Count("pk", filter=Q(review__status=LessonReview.Status.CHECKED)),
                              needs_fix=Count("pk", filter=Q(review__status=LessonReview.Status.NEEDS_FIX)))
                    .order_by(f"{SUBJECT}__order", "name"))
    for s in subjects:
        s["pct"] = round(s["checked"] * 100 / s["total"]) if s["total"] else 0

    first_todo = _filtered("todo", level, subject).order_by(*ORDER).values_list("pk", flat=True).first()
    state_counts = {key: _filtered(key, level, subject).count() for key, _label in STATES if key != "all"}
    query = {k: v for k, v in (("level", level), ("subject", subject)) if v}
    return render(request, "studio/review_queue.html", _context(
        request, studio_active="review", page=page, state=state, level=level, subject=subject,
        states=[(key, label, state_counts.get(key)) for key, label in STATES],
        levels=AcademicLevel.objects.filter(is_active=True).order_by("order"),
        subject_choices=Subject.objects.filter(offerings__courses__modules__topics__lessons__isnull=False)
        .distinct().order_by("order", "name"),
        totals=totals, subjects=subjects, first_todo=first_todo,
        querystring="&".join(f"{k}={v}" for k, v in query.items())))


def _next_to_check(lesson):
    """The next lesson still to check after this one, in the same course; else the first in the whole queue."""
    course = lesson.topic.module.course
    ordered = list(_lessons().filter(**{COURSE: course}).filter(TODO | Q(pk=lesson.pk)).order_by(*ORDER)
                   .values_list("pk", flat=True))
    after = ordered[ordered.index(lesson.pk) + 1:] if lesson.pk in ordered else ordered
    after = [pk for pk in after if pk != lesson.pk]
    if after:
        return after[0]
    return _lessons().filter(TODO).exclude(pk=lesson.pk).order_by(*ORDER).values_list("pk", flat=True).first()


def _get_lesson(pk):
    return get_object_or_404(
        _lessons().select_related(f"{COURSE}__offering__level", f"{COURSE}__offering__subject", "topic__module",
                                  "reviewer"), pk=pk)


@staff_required
def review_lesson(request, pk):
    lesson = _get_lesson(pk)
    blocks = attach_videos(list(lesson.blocks.order_by("order", "pk")), show_hidden=True)
    for number, block in enumerate(blocks, start=1):
        block.number = number
        block.review_anchor = f"b{number}"
    flags = lesson_flags(blocks)
    review = LessonReview.objects.filter(lesson=lesson).select_related("reviewer").first()
    ticked = set(review.ticked) if review else set()
    for flag in flags:
        flag["ticked"] = flag["key"] in ticked
    flagged_blocks = {flag["block"] for flag in flags}
    changed = bool(review and review.status == LessonReview.Status.CHECKED and review.fingerprint
                   and review.fingerprint != fingerprint(blocks))
    practice_sets = list(PracticeSet.objects.filter(lesson=lesson).annotate(n=Count("questions")).order_by("pk"))
    open_reports = LessonFeedback.objects.filter(lesson=lesson, status=LessonFeedback.Status.NEW).count()
    return render(request, "studio/review_lesson.html", _context(
        request, studio_active="review", lesson=lesson, course=lesson.topic.module.course, blocks=blocks,
        flags=flags, flagged_blocks=flagged_blocks, review=review, changed=changed, practice_sets=practice_sets,
        open_reports=open_reports, simulation=BlockType.SIMULATION,
        next_pk=_next_to_check(lesson)))


@staff_required
@require_POST
def review_tick(request, pk):
    """Remember that one flagged sentence was verified (or un-tick it). Called by HTMX on each checkbox."""
    lesson = _get_lesson(pk)
    key = request.POST.get("key", "")
    keys = {flag["key"] for flag in lesson_flags(list(lesson.blocks.order_by("order", "pk")))}
    if key not in keys:
        return HttpResponse(status=400)
    review, _created = LessonReview.objects.get_or_create(lesson=lesson)
    ticked = [k for k in review.ticked if k in keys and k != key]
    if request.POST.get("ticked") == "1":
        ticked.append(key)
    review.ticked = ticked
    review.save(update_fields=["ticked", "updated_at"])
    return HttpResponse(status=204)


@staff_required
@require_POST
def review_decide(request, pk):
    """Approve the lesson (needs the publish permission and every flagged sentence ticked) or send it for a fix."""
    if not can_publish(request.user):
        raise PermissionDenied
    lesson = _get_lesson(pk)
    blocks = list(lesson.blocks.order_by("order", "pk"))
    flags = lesson_flags(blocks)
    action = request.POST.get("action")
    note = request.POST.get("note", "").strip()[:2000]
    review_url = reverse("studio:review_lesson", args=[lesson.pk])
    with transaction.atomic():
        review, _created = LessonReview.objects.select_for_update().get_or_create(lesson=lesson)
        if action == "approve":
            missing = {f["key"] for f in flags} - set(review.ticked)
            if missing:
                messages.error(request, f"Tick the {len(missing)} flagged sentence{'s' if len(missing) != 1 else ''} "
                                        "you have not verified yet, then approve.")
                return redirect(review_url)
            review.status = LessonReview.Status.CHECKED
            review.reviewer = request.user
            review.fingerprint = fingerprint(blocks)
            review.checked_at = timezone.now()
            review.note = note
            review.save()
            Lesson.objects.filter(pk=lesson.pk).update(reviewer=request.user)
            revisions.log(lesson, request.user, LessonEvent.Action.CHECKED, note, lesson.status, lesson.status)
            messages.success(request, f"“{lesson.title}” is checked. Students now see who checked it.")
        elif action == "needs_fix":
            if not note:
                messages.error(request, "Say what needs fixing, so the editor knows what to change.")
                return redirect(review_url)
            review.status = LessonReview.Status.NEEDS_FIX
            review.reviewer = request.user
            review.note = note
            review.checked_at = None
            review.save()
            Lesson.objects.filter(pk=lesson.pk).update(reviewer=None)
            revisions.log(lesson, request.user, LessonEvent.Action.NEEDS_FIX, note, lesson.status, lesson.status)
            messages.success(request, f"“{lesson.title}” is marked as needing a fix.")
        else:
            return HttpResponse(status=400)
    next_pk = _next_to_check(lesson)
    return redirect(reverse("studio:review_lesson", args=[next_pk]) if next_pk else reverse("studio:review"))
