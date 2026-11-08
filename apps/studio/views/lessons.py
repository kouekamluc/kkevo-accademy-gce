"""Studio overview, the lesson list and bulk actions, and creating a lesson."""

from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Count, Max, Q
from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from .. import revisions
from ..models import LessonDraft, LessonEvent, MediaAsset
from apps.academics.models import AcademicLevel, Subject
from apps.courses.models import Lesson, LessonType, Topic

from ._common import PER_PAGE, _context, _plural, apply_status, can_publish, staff_required


# ------------------------------------------------------------------ overview
@staff_required
def overview(request):
    counts = dict(Lesson.objects.values_list("status").annotate(n=Count("pk")))
    related = ("topic__module__course__offering__subject", "author")
    review_lessons = Lesson.objects.filter(status="review").select_related(*related).order_by("updated_at")[:10]
    drafts = LessonDraft.objects.select_related("lesson__topic__module__course__offering__subject", "created_by")
    my_drafts = Lesson.objects.filter(author=request.user, status="draft").select_related(*related).order_by("-updated_at")[:8]
    events = LessonEvent.objects.select_related("lesson", "actor")[:12]
    return render(request, "studio/overview.html", _context(
        request, counts=counts, total=sum(counts.values()), review_lessons=review_lessons,
        review_changes=drafts.filter(status="review").order_by("updated_at")[:10],
        draft_changes=drafts.filter(status="draft").order_by("-updated_at")[:10],
        pending_changes=drafts.count(), my_drafts=my_drafts, events=events,
        media_count=MediaAsset.objects.count(), studio_active="overview"))


# ------------------------------------------------------------------ list
@staff_required
def lessons(request):
    qs = Lesson.objects.select_related("topic__module__course__offering__subject", "topic__module__course__offering__level",
                                       "author", "studio_draft")
    counts = dict(qs.values_list("status").annotate(n=Count("pk")))
    status = request.GET.get("status", "")
    q = request.GET.get("q", "").strip()
    subject = request.GET.get("subject", "")
    level = request.GET.get("level", "")
    author = request.GET.get("author", "")
    if status in ("draft", "review", "published", "archived"):
        qs = qs.filter(status=status)
    elif status == "changes":
        qs = qs.filter(studio_draft__isnull=False)
    else:
        qs = qs.exclude(status="archived")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(topic__title__icontains=q))
    if subject.isdigit():
        qs = qs.filter(topic__module__course__offering__subject_id=subject)
    if level.isdigit():
        qs = qs.filter(topic__module__course__offering__level_id=level)
    if author == "me":
        qs = qs.filter(author=request.user)
    elif author.isdigit():
        qs = qs.filter(author_id=author)
    page = Paginator(qs.order_by("-updated_at"), PER_PAGE).get_page(request.GET.get("page"))
    total = sum(n for s, n in counts.items() if s != "archived")
    User = get_user_model()
    return render(request, "studio/lessons.html", _context(
        request, page=page, counts=counts, total=total, status=status, q=q, subject=subject, level=level, author=author,
        changes_count=LessonDraft.objects.count(),
        subjects=Subject.objects.filter(is_active=True), levels=AcademicLevel.objects.filter(is_active=True),
        authors=User.objects.filter(authored_lessons__isnull=False).distinct(),
        subject_count=Subject.objects.filter(offerings__courses__isnull=False).distinct().count(),
        level_count=AcademicLevel.objects.filter(is_active=True).count(),
        query_string=request.GET.urlencode(), studio_active="lessons",
    ))


@staff_required
@require_POST
def bulk(request):
    ids = [int(i) for i in request.POST.getlist("lessons") if i.isdigit()]
    action = request.POST.get("action")
    lessons_qs = Lesson.objects.filter(pk__in=ids)
    if not ids:
        messages.error(request, "Select at least one lesson.")
    elif action == "review":
        selected = list(lessons_qs.filter(status="draft"))
        for lesson in selected:
            apply_status(lesson, "review", request.user)
        messages.success(request, f"{_plural(len(selected), 'lesson')} submitted for review.")
    elif action == "archive":
        if not can_publish(request.user):
            raise PermissionDenied
        selected = list(lessons_qs.exclude(status="archived"))
        for lesson in selected:
            apply_status(lesson, "archived", request.user)
        messages.success(request, f"{_plural(len(selected), 'lesson')} archived.")
    else:
        messages.error(request, "Unknown action.")
    return_to = request.POST.get("return_to", "")
    return redirect(return_to if return_to.startswith("/studio/") else "studio:lessons")


# ------------------------------------------------------------------ create
class NewLessonForm(forms.Form):
    topic = forms.ModelChoiceField(queryset=Topic.objects.select_related("module__course").order_by(
        "module__course__title", "module__order", "order"), widget=forms.Select(attrs={"class": "form-input"}))
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-input"}))
    lesson_type = forms.ChoiceField(choices=LessonType.choices, widget=forms.Select(attrs={"class": "form-input"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topic"].label_from_instance = lambda t: f"{t.module.course.title} › {t.module.title} › {t.title}"


@staff_required
def lesson_new(request):
    form = NewLessonForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        topic = form.cleaned_data["topic"]
        base = slugify(form.cleaned_data["title"])[:180] or "lesson"
        slug, n = base, 2
        while Lesson.objects.filter(topic=topic, slug=slug).exists():
            slug, n = f"{base}-{n}", n + 1
        order = (topic.lessons.aggregate(m=Max("order"))["m"] or 0) + 1
        lesson = Lesson.objects.create(topic=topic, title=form.cleaned_data["title"], slug=slug, order=order,
                                       lesson_type=form.cleaned_data["lesson_type"], author=request.user)
        revisions.log(lesson, request.user, LessonEvent.Action.CREATED, to_status=lesson.status)
        messages.success(request, "Draft lesson created. Add blocks to build it.")
        return redirect("studio:edit", pk=lesson.pk)
    return render(request, "studio/new.html", _context(request, form=form, studio_active="lessons"))
