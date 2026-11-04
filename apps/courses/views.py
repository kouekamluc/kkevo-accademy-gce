from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Prefetch, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.academics.models import AcademicLevel, AcademicPathway, SubjectCategory, SubjectOffering
from apps.accounts.utils import get_profile
from apps.learning import services
from apps.learning.models import Enrollment, LessonProgress
from apps.practice.models import Question

from .models import Course, Lesson, Module, Topic

SORTS = {"popular": "Most popular", "name": "Name (A–Z)"}


def _student_level(request):
    if request.user.is_authenticated:
        profile = get_profile(request.user)
        return profile.level, profile.pathway
    return None, None


def catalog(request):
    """Explore Your Subjects (mockup 08). Filters work with or without JavaScript; HTMX swaps the results."""
    levels = list(AcademicLevel.objects.filter(is_active=True))
    pathways = list(AcademicPathway.objects.filter(is_active=True))
    student_level, _ = _student_level(request)

    level_slug = request.GET.get("level")
    level = next((lvl for lvl in levels if lvl.slug == level_slug), None) or student_level or (levels[0] if levels else None)
    stream = request.GET.get("stream", "all")
    category = request.GET.get("category", "")
    q = request.GET.get("q", "").strip()[:80]
    sort = request.GET.get("sort") if request.GET.get("sort") in SORTS else "popular"
    subject_slug = request.GET.get("subject", "")

    offerings = (
        SubjectOffering.objects.active()
        .filter(level=level)
        .select_related("subject", "level")
        .prefetch_related("pathways", Prefetch("courses", queryset=Course.objects.published().order_by("order", "pk")))
        .annotate(learners=Count("enrollments", distinct=True))
    )
    if stream != "all" and any(p.slug == stream for p in pathways):
        offerings = offerings.filter(pathways__slug=stream)
    if category in SubjectCategory.values:
        offerings = offerings.filter(subject__category=category)
    if subject_slug:
        offerings = offerings.filter(subject__slug=subject_slug)
    if q:
        offerings = offerings.filter(
            Q(subject__name__icontains=q)
            | Q(subject__summary__icontains=q)
            | Q(courses__modules__topics__title__icontains=q, courses__status="published")
            | Q(courses__modules__topics__lessons__title__icontains=q, courses__status="published")
        )
    offerings = offerings.distinct().order_by(
        *(["-learners"] if sort == "popular" else []), "subject__order", "subject__name"
    )
    offerings = list(offerings)

    enrolled = services.enrolled_offering_ids(request.user)
    courses = [c for c in (services.primary_course(o.courses.all()) for o in offerings) if c]
    stats = services.course_stats(request.user, courses)
    counts = dict(
        Module.objects.filter(course__in=courses).values("course").annotate(n=Count("pk")).values_list("course", "n")
    )
    cards = []
    for offering in offerings:
        course = services.primary_course(offering.courses.all())
        cards.append({
            "offering": offering,
            "subject": offering.subject,
            "course": course,
            "in_plan": offering.pk in enrolled,
            "stat": stats.get(course.pk) if course else None,
            "module_count": counts.get(course.pk, 0) if course else 0,
            "pathway_badge": _pathway_badge(offering, pathways),
        })
    if request.user.is_authenticated:  # "In your plan" first, as in the mockup
        cards.sort(key=lambda c: not c["in_plan"])

    context = {
        "levels": levels, "pathways": pathways, "categories": SubjectCategory.choices, "sorts": SORTS,
        "level": level, "stream": stream, "category": category, "q": q, "sort": sort,
        "cards": cards, "plan_count": sum(c["in_plan"] for c in cards), "nav_active": "explore",
    }
    template = "courses/_catalog_results.html" if request.htmx and request.htmx.target == "catalog-results" else "courses/catalog.html"
    return render(request, template, context)


def _pathway_badge(offering, all_pathways):
    names = [p.name for p in offering.pathways.all()]
    if not names:
        return ""
    if len(names) >= len(all_pathways) and len(all_pathways) > 1:
        return "Both"
    return " & ".join(names)


@login_required
def my_subjects(request):
    profile = get_profile(request.user)
    enrollments = list(
        Enrollment.objects.filter(user=request.user)
        .select_related("offering__subject", "offering__level")
        .prefetch_related(Prefetch("offering__courses", queryset=Course.objects.published().order_by("order", "pk")))
    )
    courses = [c for c in (services.primary_course(e.offering.courses.all()) for e in enrollments) if c]
    stats = services.course_stats(request.user, courses)
    rows = []
    for e in enrollments:
        course = services.primary_course(e.offering.courses.all())
        rows.append({"enrollment": e, "subject": e.offering.subject, "course": course, "stat": stats.get(course.pk) if course else None})
    return render(request, "courses/my_subjects.html", {"rows": rows, "profile": profile, "nav_active": "subjects"})


@login_required
@require_POST
def toggle_plan(request, offering_pk):
    offering = get_object_or_404(SubjectOffering.objects.active(), pk=offering_pk)
    enrollment = Enrollment.objects.filter(user=request.user, offering=offering).first()
    if enrollment:
        enrollment.delete()
        messages.success(request, f"{offering.subject.name} removed from your plan.")
    else:
        Enrollment.objects.create(user=request.user, offering=offering)
        messages.success(request, f"{offering.subject.name} added to your plan.")
    next_url = request.POST.get("next", "")
    if next_url.startswith("/") and not next_url.startswith("//"):
        return redirect(next_url)
    return redirect("courses:my_subjects")


def course_detail(request, slug):
    """Course overview (mockup 03)."""
    course = get_object_or_404(
        Course.objects.select_related("offering__subject", "offering__level").prefetch_related("offering__pathways"),
        slug=slug,
    )
    if course.status != "published" and not request.user.is_staff:
        raise Http404
    lessons_qs = Lesson.objects.published() if not request.user.is_staff else Lesson.objects.exclude(status="archived")
    modules = list(
        course.modules.prefetch_related(
            Prefetch("topics", queryset=Topic.objects.order_by("order", "pk").prefetch_related(
                Prefetch("lessons", queryset=lessons_qs.order_by("order", "pk"))))
        )
    )
    all_lessons = [lesson for m in modules for t in m.topics.all() for lesson in t.lessons.all()]
    progress = services.progress_by_lesson(request.user, all_lessons)
    next_lesson, next_progress = services.next_lesson(request.user, course)

    module_rows, done_total = [], 0
    for m_i, module in enumerate(modules, 1):
        topics, m_done, m_total = [], 0, 0
        for t_i, topic in enumerate(module.topics.all(), 1):
            rows, t_done = [], 0
            for lesson in topic.lessons.all():
                p = progress.get(lesson.pk)
                state = "done" if p and p.is_completed else "current" if next_lesson and lesson.pk == next_lesson.pk and p else "todo"
                t_done += state == "done"
                rows.append({"lesson": lesson, "progress": p, "state": state})
            topics.append({"topic": topic, "number": f"{m_i}.{t_i}", "rows": rows, "done": t_done, "total": len(rows)})
            m_done += t_done
            m_total += len(rows)
        done_total += m_done
        pct = round(100 * m_done / m_total) if m_total else 0
        status = "complete" if m_total and m_done == m_total else "progress" if m_done or any(
            r["state"] == "current" for t in topics for r in t["rows"]) else "todo"
        module_rows.append({"module": module, "number": m_i, "topics": topics, "done": m_done, "total": m_total,
                            "percent": pct, "status": status})

    total = len(all_lessons)
    minutes = sum(lesson.estimated_minutes for lesson in all_lessons)
    question_count = Question.objects.filter(practice_set__topic__module__course=course,
                                             practice_set__status="published").count()
    has_syllabus_mapping = Topic.objects.filter(module__course=course, curriculum_references__isnull=False).exists()
    profile = get_profile(request.user) if request.user.is_authenticated else None
    in_plan = request.user.is_authenticated and Enrollment.objects.filter(user=request.user, offering=course.offering).exists()
    pathway_label = (
        profile.pathway.name if profile and profile.pathway_id and profile.pathway in course.offering.pathways.all()
        else _pathway_badge(course.offering, list(AcademicPathway.objects.filter(is_active=True)))
    )
    return render(request, "courses/detail.html", {
        "course": course, "subject": course.offering.subject, "level": course.offering.level,
        "modules": module_rows, "total": total, "done": done_total,
        "percent": round(100 * done_total / total) if total else 0,
        "topic_count": sum(len(m["topics"]) for m in module_rows), "hours": round(minutes / 60) if minutes >= 60 else None,
        "minutes": minutes, "question_count": question_count, "next_lesson": next_lesson, "next_progress": next_progress,
        "has_syllabus_mapping": has_syllabus_mapping, "in_plan": in_plan, "pathway_label": pathway_label,
        "nav_active": "subjects" if in_plan else "explore",
        "open_module": next(
            (m["number"] for m in module_rows if m["status"] == "progress"),
            module_rows[0]["number"] if module_rows else None,
        ),
    })


@login_required
def continue_learning(request):
    """Sidebar 'Continue Learning': reopen the most recent unfinished lesson."""
    latest = (
        LessonProgress.objects.filter(user=request.user, completed_at__isnull=True, lesson__status="published")
        .select_related("lesson__topic__module__course").order_by("-last_viewed_at").first()
    )
    if latest:
        return redirect(latest.lesson.get_absolute_url())
    messages.info(request, "You haven’t started a lesson yet. Pick a subject to begin.")
    return redirect("courses:my_subjects")
