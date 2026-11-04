"""Lesson player: reading (04), interactive (05) and video (06) lessons."""

import re

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Prefetch
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.learning import services
from apps.learning.models import DailyActivity, LessonNote, LessonProgress, SavedLesson
from apps.practice.models import PracticeSet

from .models import BlockType, Lesson, LessonType, Topic

MAX_HEARTBEAT_SECONDS = 120  # ignore larger gaps (tab left open)
ANCHOR_RE = re.compile(r"^[A-Za-z0-9_-]{1,60}$")


def _clean_anchor(value):
    value = (value or "").strip()
    return value if ANCHOR_RE.match(value) else ""


def _is_low_data(user):
    profile = getattr(user, "profile", None)
    return bool(profile and profile.low_data_mode)


def _resume_point(progress, blocks, toc, created):
    """Where 'Continue from …' should take the student, or None.

    Uses the saved anchor when it still exists on the page; falls back to matching the saved
    label against section titles (older progress rows only had a label). Nothing to offer on a
    first visit, after completion, or when the student stopped at the first section.
    """
    if created or progress.is_completed:
        return None
    sections = [(item["anchor"], item["title"]) for item in toc]
    sections += [(b.anchor, b.title) for b in blocks if b.title]
    valid = {anchor for anchor, _ in sections}
    anchor = progress.position_anchor if progress.position_anchor in valid else ""
    if not anchor and progress.position_label:
        anchor = next((a for a, title in sections if title == progress.position_label), "")
    if not anchor or (toc and anchor == toc[0]["anchor"] and progress.percent < 10):
        return None
    label = progress.position_label or next((title for a, title in sections if a == anchor), "where you stopped")
    return {"anchor": anchor, "label": label}


def _get_lesson(request, course_slug, pk):
    lesson = get_object_or_404(
        Lesson.objects.select_related("topic__module__course__offering__subject", "topic__module__course__offering__level"),
        pk=pk, topic__module__course__slug=course_slug,
    )
    course = lesson.course
    published = lesson.status == "published" and course.status == "published"
    if not published and not request.user.is_staff:
        raise Http404
    return lesson


def _ordered_lessons(request, course):
    qs = Lesson.objects.filter(topic__module__course=course)
    qs = qs.exclude(status="archived") if request.user.is_staff else qs.filter(status="published")
    return list(qs.select_related("topic__module").order_by("topic__module__order", "topic__order", "order", "pk"))


@login_required
def lesson_detail(request, course_slug, pk):
    lesson = _get_lesson(request, course_slug, pk)
    course = lesson.course
    lessons = _ordered_lessons(request, course)
    index = next((i for i, item in enumerate(lessons) if item.pk == lesson.pk), 0)
    prev_lesson = lessons[index - 1] if index > 0 else None
    next_lesson = lessons[index + 1] if index + 1 < len(lessons) else None

    progress, created = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    LessonProgress.objects.filter(pk=progress.pk).update(last_viewed_at=timezone.now())
    all_progress = services.progress_by_lesson(request.user, lessons)

    module = lesson.topic.module
    module_lessons = [item for item in lessons if item.topic.module_id == module.pk]
    blocks = list(lesson.blocks.all())
    toc = [{"anchor": "objectives", "title": "Learning objectives"}] if lesson.objectives_list else []
    toc += [{"anchor": b.anchor, "title": b.title} for b in blocks
            if b.title and b.block_type in (BlockType.HEADING, BlockType.WORKED_EXAMPLE, BlockType.VIDEO)]
    video = next((b for b in blocks if b.block_type == BlockType.VIDEO), None)

    # Course outline for the left sidebar (current module expanded)
    modules = list(course.modules.prefetch_related(
        Prefetch("topics", queryset=Topic.objects.order_by("order", "pk"))))
    stats = services.module_stats(request.user, course)
    outline = []
    for m in modules:
        topics = []
        for t in m.topics.all():
            rows = [{"lesson": item, "done": all_progress.get(item.pk) and all_progress[item.pk].is_completed}
                    for item in lessons if item.topic_id == t.pk]
            topics.append({"topic": t, "rows": rows})
        stat = stats.get(m.pk)
        outline.append({"module": m, "topics": topics, "stat": stat, "current": m.pk == module.pk})
    course_stat = services.course_stats(request.user, [course])[course.pk]

    related = [item for item in module_lessons if item.pk != lesson.pk and item.lesson_type in ("video", "interactive")][:3]
    practice_set = (
        PracticeSet.objects.published().filter(topic=lesson.topic).annotate(question_count=Count("questions")).first()
    )
    context = {
        "lesson": lesson, "course": course, "module": module, "subject": course.offering.subject,
        "level": course.offering.level, "blocks": blocks, "toc": toc, "video": video,
        "progress": progress, "prev_lesson": prev_lesson, "next_lesson": next_lesson,
        "module_index": modules.index(module) + 1 if module in modules else 1,
        "lesson_index": module_lessons.index(lesson) + 1 if lesson in module_lessons else 1,
        "module_lesson_count": len(module_lessons), "outline": outline, "course_stat": course_stat,
        "is_saved": SavedLesson.objects.filter(user=request.user, lesson=lesson).exists(),
        "related": related, "practice_set": practice_set,
        "has_simulation": any(b.block_type == BlockType.SIMULATION for b in blocks),
        "notes": LessonNote.objects.filter(user=request.user, lesson=lesson),
        "resume": _resume_point(progress, blocks, toc, created),
        "auto_resume": request.GET.get("resume") == "1",
        "low_data": _is_low_data(request.user),
        "up_next": [item for item in module_lessons[module_lessons.index(lesson) + 1:]][:3] if lesson in module_lessons else [],
        "media_note": "low" if _is_low_data(request.user) else "normal",
        "chapters": _chapters(video),
        "related_reading": [item for item in module_lessons if item.pk != lesson.pk
                            and item.lesson_type in ("reading", "interactive")][:2],
    }
    if lesson.lesson_type == LessonType.VIDEO and video:
        template = "lessons/video.html"
    elif lesson.lesson_type == LessonType.INTERACTIVE and context["has_simulation"]:
        template = "lessons/interactive.html"
    else:
        template = "lessons/reading.html"
    context["notes_panel"] = template != "lessons/video.html"  # video lessons keep notes in their tab
    return render(request, template, context)


def _chapters(video):
    """[[start, title], ...] → [{'start', 'end', 'title'}] for highlighting the playing chapter."""
    raw = (video.data or {}).get("chapters", []) if video else []
    out = []
    for i, (start, title) in enumerate(raw):
        end = raw[i + 1][0] if i + 1 < len(raw) else 10**9
        out.append({"start": start, "end": end, "title": title})
    return out


@login_required
@require_POST
def lesson_complete(request, course_slug, pk):
    lesson = _get_lesson(request, course_slug, pk)
    progress, _ = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    progress.mark_complete()
    progress.save()
    lessons = _ordered_lessons(request, lesson.course)
    index = next((i for i, item in enumerate(lessons) if item.pk == lesson.pk), 0)
    next_lesson = lessons[index + 1] if index + 1 < len(lessons) else None
    if request.htmx:
        return render(request, "lessons/_complete_card.html", {"lesson": lesson, "progress": progress,
                                                                "next_lesson": next_lesson, "course": lesson.course})
    return redirect(next_lesson.get_absolute_url() if next_lesson else lesson.course.get_absolute_url())


@login_required
@require_POST
def lesson_heartbeat(request, course_slug, pk):
    """Called by the player every ~30 s and on leave: time spent, scroll %, position."""
    lesson = _get_lesson(request, course_slug, pk)
    try:
        seconds = max(0, min(int(request.POST.get("seconds", 0)), MAX_HEARTBEAT_SECONDS))
        percent = max(0, min(int(request.POST.get("percent", 0)), 100))
        video_position = max(0, int(request.POST.get("video_position", 0)))
    except ValueError:
        return HttpResponse(status=400)
    label = request.POST.get("position", "")[:120]
    anchor = _clean_anchor(request.POST.get("anchor"))
    progress, _ = LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    progress.time_spent_seconds += seconds
    progress.last_viewed_at = timezone.now()
    if not progress.is_completed:
        progress.percent = max(progress.percent, min(percent, 99))
        if label:
            progress.position_label = label
        if anchor:
            progress.position_anchor = anchor
    if video_position:
        progress.video_position = video_position
    progress.save()
    if seconds:
        DailyActivity.add(request.user, seconds)
    return JsonResponse({"percent": progress.percent, "completed": progress.is_completed})


@login_required
@require_POST
def lesson_save(request, course_slug, pk):
    lesson = _get_lesson(request, course_slug, pk)
    saved = SavedLesson.objects.filter(user=request.user, lesson=lesson)
    if saved.exists():
        saved.delete()
        is_saved = False
    else:
        SavedLesson.objects.create(user=request.user, lesson=lesson)
        is_saved = True
    if request.htmx:
        return render(request, "lessons/_save_button.html", {"lesson": lesson, "is_saved": is_saved,
                                                             "variant": request.POST.get("variant", "")})
    return redirect(lesson.get_absolute_url())


@login_required
@require_POST
def lesson_note(request, course_slug, pk):
    lesson = _get_lesson(request, course_slug, pk)
    body = request.POST.get("body", "").strip()[:2000]
    if body:
        try:
            raw_time = request.POST.get("video_time")  # only video lessons send a time
            video_time = max(0, int(raw_time)) if raw_time not in (None, "") else None
        except ValueError:
            video_time = None
        LessonNote.objects.create(
            user=request.user, lesson=lesson, body=body, video_time=video_time,
            section_label=request.POST.get("section_label", "").strip()[:120],
            section_anchor=_clean_anchor(request.POST.get("section_anchor")),
        )
    return _notes_response(request, lesson)


@login_required
@require_POST
def lesson_note_delete(request, course_slug, pk, note_pk):
    lesson = _get_lesson(request, course_slug, pk)
    get_object_or_404(LessonNote, pk=note_pk, lesson=lesson, user=request.user).delete()
    return _notes_response(request, lesson)


def _notes_response(request, lesson):
    notes = LessonNote.objects.filter(user=request.user, lesson=lesson)
    if request.htmx:
        return render(request, "lessons/_notes.html", {"lesson": lesson, "course": lesson.course, "notes": notes, "oob": True})
    return redirect(lesson.get_absolute_url() + "#notes")
