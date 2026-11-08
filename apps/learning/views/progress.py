"""My Progress (mockup 10) and the 'add suggestions to the planner' action."""

from collections import defaultdict
from datetime import datetime, time, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .. import achievements, analytics, services
from ..models import LessonProgress, SessionKind, StudySession
from apps.accounts.decorators import onboarding_required

from ._common import _plan, fmt_minutes


# --------------------------------------------------------------------------- progress (10)
@onboarding_required
def progress(request):
    user = request.user
    today = timezone.localdate()
    range_key = request.GET.get("range") if request.GET.get("range") in analytics.RANGES else "30d"
    start, length = analytics.period(range_key, today)
    prev_start, prev_end = start - timedelta(days=length), start - timedelta(days=1)

    plan = _plan(user)
    courses = [p["course"] for p in plan if p["course"]]
    stats = services.course_stats(user, courses)
    lesson_ids = list(services.published_lessons().filter(topic__module__course__in=courses).values_list("pk", flat=True))
    done = sum(s.done for s in stats.values())
    total = sum(s.total for s in stats.values())
    overall = round(100 * done / total) if total else 0
    gained = round(100 * analytics.completions_between(user, start, today, lesson_ids) / total) if total else 0

    attempts_now = list(analytics.completed_attempts(user, start, today))
    attempts_prev = list(analytics.completed_attempts(user, prev_start, prev_end))
    avg_now, avg_prev = analytics.average_score(attempts_now), analytics.average_score(attempts_prev)
    seconds = sum(r.seconds for r in user.daily_activity.filter(date__gte=start, date__lte=today))

    all_attempts = list(analytics.completed_attempts(user).order_by("completed_at"))
    by_course = defaultdict(list)
    for a in all_attempts:
        by_course[a.practice_set.topic.module.course_id].append(a.score)
    topics = analytics.topic_scores(user)
    mastered_by_subject = defaultdict(int)
    for entry in topics.values():
        if entry["mastered"]:
            mastered_by_subject[entry["subject"].pk] += 1

    subject_rows = []
    for p in plan:
        if not p["course"]:
            continue
        scores = by_course.get(p["course"].pk, [])
        quiz = round(sum(scores) / len(scores)) if scores else None
        subject_rows.append({"subject": p["subject"], "course": p["course"], "stat": stats[p["course"].pk], "quiz": quiz,
                             "mastered": mastered_by_subject.get(p["subject"].pk, 0)})
    subject_rows.sort(key=lambda r: -r["stat"].percent)
    strongest = sorted([r for r in subject_rows if r["quiz"] is not None], key=lambda r: -r["quiz"])[:2]

    recent_scores = [a.score for a in all_attempts[-10:]]
    correct, to_review = analytics.answer_totals(user)
    needs = sorted([e for e in topics.values() if e["needs_revision"]], key=lambda e: e["latest"])[:4]
    for e in needs:
        e["days_ago"] = (today - timezone.localtime(e["last_at"]).date()).days
        e["revise_url"] = (e["practice_set"].lesson.get_absolute_url() if e["practice_set"].lesson
                           else e["practice_set"].get_absolute_url())

    suggestions = _suggestions(user, needs, courses)
    recent = list(
        LessonProgress.objects.filter(user=user, completed_at__isnull=False)
        .select_related("lesson__topic__module__course__offering__subject").order_by("-completed_at")[:6]
    )
    scores_by_lesson = {a.practice_set.lesson_id: a.score for a in all_attempts if a.practice_set.lesson_id}
    for r in recent:
        r.score = scores_by_lesson.get(r.lesson_id)
        day = timezone.localtime(r.completed_at).date()
        r.day_label = "Today" if day == today else "Yesterday" if day == today - timedelta(days=1) else f"{day.day} {day.strftime('%b')}"

    return render(request, "learning/progress.html", {
        **achievements.journey(user),
        "range_key": range_key, "ranges": analytics.RANGES, "overall": overall, "gained": gained,
        "done": done, "total": total, "avg_now": avg_now,
        "avg_delta": (avg_now - avg_prev) if avg_now is not None and avg_prev is not None else None,
        "learning_time": fmt_minutes(seconds / 60), "per_day": round(seconds / 60 / length),
        "subject_rows": subject_rows, "strongest": strongest, "weeks": analytics.weekly_hours(user, today),
        "quiz_avg": analytics.average_score(all_attempts), "quiz_count": len(all_attempts),
        "quiz_line": _sparkline(recent_scores), "latest_score": recent_scores[-1] if recent_scores else None,
        "correct": correct, "to_review": to_review, "needs": needs, "suggestions": suggestions,
        "recent": recent, "nav_active": "progress",
    })


def _sparkline(scores, width=340, height=90):
    if len(scores) < 2:
        return None
    step = width / (len(scores) - 1)
    points = [(round(i * step, 1), round(height - (s / 100) * (height - 10) - 5, 1)) for i, s in enumerate(scores)]
    return {"points": " ".join(f"{x},{y}" for x, y in points), "last": points[-1], "width": width, "height": height}


def _suggestions(user, needs, courses):
    out = []
    if needs:
        weakest = needs[0]
        target = weakest["practice_set"].lesson
        out.append({"html_title": weakest["topic"].title, "text_before": "Re-read", "text_after": ", then retry its practice set",
                    "title": f"Revise {weakest['topic'].title}", "subject": weakest["subject"], "lesson": target,
                    "topic": weakest["topic"], "kind": SessionKind.REVISION, "minutes": 30})
    current = (LessonProgress.objects.filter(user=user, completed_at__isnull=True, lesson__topic__module__course__in=courses)
               .select_related("lesson__topic__module__course__offering__subject").order_by("-last_viewed_at").first())
    if current:
        module = current.lesson.topic.module
        left = services.module_stats(user, module.course).get(module.pk)
        remaining = (left.total - left.done) if left else 0
        out.append({"html_title": current.lesson.title, "text_before": "Finish", "text_after": f" — {remaining} lesson{'s' if remaining != 1 else ''} left in {module.title}",
                    "title": current.lesson.title, "subject": current.lesson.course.offering.subject,
                    "lesson": current.lesson, "kind": SessionKind.STUDY, "minutes": current.lesson.estimated_minutes})
    for course in courses:
        if len(out) >= 3:
            break
        nxt, prog = services.next_lesson(user, course)
        if nxt and not any(s.get("lesson") == nxt for s in out) and not prog:
            out.append({"html_title": nxt.title, "text_before": "Start", "text_after": f" in {course.offering.subject.name}",
                        "title": nxt.title, "subject": course.offering.subject, "lesson": nxt,
                        "kind": SessionKind.STUDY, "minutes": nxt.estimated_minutes})
    return out[:3]


@login_required
@require_POST
def add_suggestions(request):
    """'Add these to my planner': schedule each suggestion on the next free evenings at 17:00."""
    courses = [p["course"] for p in _plan(request.user) if p["course"]]
    needs = sorted([e for e in analytics.topic_scores(request.user).values() if e["needs_revision"]], key=lambda e: e["latest"])
    tz = timezone.get_current_timezone()
    day = timezone.localdate() + timedelta(days=1)
    created = 0
    for s in _suggestions(request.user, needs, courses):
        starts = timezone.make_aware(datetime.combine(day, time(17, 0)), tz)
        StudySession.objects.create(user=request.user, title=s["title"][:120], subject=s["subject"], lesson=s.get("lesson"),
                                    topic=s.get("topic"), kind=s["kind"], starts_at=starts,
                                    duration_minutes=max(15, min(int(s["minutes"] or 30), 120)))
        day += timedelta(days=1)
        created += 1
    messages.success(request, f"Added {created} session{'s' if created != 1 else ''} to your planner." if created
                     else "Nothing to add right now.")
    return redirect("learning:planner")
