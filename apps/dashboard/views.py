"""Student dashboard (mockup 02). Every figure comes from the student's own records."""

from datetime import timedelta

from django.db.models import Count, Prefetch
from django.shortcuts import render
from django.utils import timezone

from apps.accounts.decorators import onboarding_required
from apps.accounts.utils import get_profile
from apps.courses.models import Course
from apps.learning import motivation, services
from apps.learning.models import DailyActivity, Enrollment, LessonProgress, RestDay, StudySession
from apps.practice.reviews import review_summary
from apps.practice.models import Attempt, PracticeSet

WEEKDAY_SHORT = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def greeting(now):
    hour = now.hour
    return "Good morning" if hour < 12 else "Good afternoon" if hour < 17 else "Good evening"


def relative_day(when, today):
    day = timezone.localtime(when).date() if hasattr(when, "hour") else when
    delta = (today - day).days
    if delta == 0:
        return "Today"
    if delta == 1:
        return "Yesterday"
    if 1 < delta < 7:
        return day.strftime("%A")
    return f"{day.day} {day.strftime('%b')}"


def learning_streak(user, today):
    """Consecutive learning days; planned rest days keep the streak (see apps.learning.motivation)."""
    return motivation.learning_streak(user, today)


def weekly_activity(user, today, goal_minutes):
    start = today - timedelta(days=6)
    rows = dict(DailyActivity.objects.filter(user=user, date__gte=start).values_list("date", "seconds"))
    days = []
    for i in range(7):
        day = start + timedelta(days=i)
        minutes = round(rows.get(day, 0) / 60)
        days.append({"date": day, "minutes": minutes, "label": "Today" if day == today else WEEKDAY_SHORT[day.weekday()],
                     "short": WEEKDAY_SHORT[day.weekday()][0], "is_today": day == today, "reached": minutes >= goal_minutes})
    top = max([d["minutes"] for d in days] + [goal_minutes]) * 1.15 or 1
    for d in days:
        d["height"] = round(d["minutes"] / top * 100)
    total = sum(d["minutes"] for d in days)
    return {"days": days, "total_minutes": total, "goal_line": round(goal_minutes / top * 100),
            "weekly_goal_minutes": goal_minutes * 7}


def fmt_minutes(minutes):
    hours, mins = divmod(int(minutes), 60)
    return f"{hours}h {mins:02d}m" if hours else f"{mins}m"


@onboarding_required
def home(request):
    user = request.user
    profile = get_profile(user)
    now = timezone.localtime()
    today = now.date()

    enrollments = list(
        Enrollment.objects.filter(user=user).select_related("offering__subject", "offering__level")
        .prefetch_related(Prefetch("offering__courses", queryset=Course.objects.published().order_by("order", "pk")))
    )
    plan = []
    for e in enrollments:
        course = services.primary_course(e.offering.courses.all())
        plan.append({"subject": e.offering.subject, "course": course, "offering": e.offering})
    courses = [p["course"] for p in plan if p["course"]]
    stats = services.course_stats(user, courses)
    for p in plan:
        p["stat"] = stats.get(p["course"].pk) if p["course"] else None
    overall = services.Stat(done=sum(s.done for s in stats.values()), total=sum(s.total for s in stats.values()))

    # Continue learning: most recent unfinished lesson
    current = (
        LessonProgress.objects.filter(user=user, completed_at__isnull=True, lesson__status="published",
                                      lesson__topic__module__course__status="published")
        .select_related("lesson__topic__module__course__offering__subject").order_by("-last_viewed_at").first()
    )
    continue_card = None
    if current:
        lesson = current.lesson
        module = lesson.topic.module
        module_lessons = list(services.published_lessons().filter(topic__module=module)
                              .order_by("topic__order", "order", "pk").values_list("pk", flat=True))
        module_stats = services.module_stats(user, lesson.course).get(module.pk, services.Stat())
        continue_card = {
            "progress": current, "lesson": lesson, "module": module, "course": lesson.course,
            "subject": lesson.course.offering.subject,
            "index": module_lessons.index(lesson.pk) + 1 if lesson.pk in module_lessons else 1,
            "count": len(module_lessons),
            "minutes_left": max(1, round(lesson.estimated_minutes * (100 - current.percent) / 100)),
            "last_opened": current.last_viewed_at,
            "module_left": module_stats.total - module_stats.done,
        }

    # Recommended next: continue another subject from where the student last finished
    recommended = None
    recent_done = (
        LessonProgress.objects.filter(user=user, completed_at__isnull=False,
                                      lesson__topic__module__course__in=courses)
        .select_related("lesson__topic__module__course__offering__subject").order_by("-completed_at")
    )
    exclude_course = continue_card["course"].pk if continue_card else None
    for done in recent_done[:20]:
        course = done.lesson.course
        if course.pk == exclude_course:
            continue
        nxt, _ = services.next_lesson(user, course)
        if nxt and not LessonProgress.objects.filter(user=user, lesson=nxt, completed_at__isnull=False).exists():
            day = relative_day(done.completed_at, today)
            recommended = {"lesson": nxt, "builds_on": done.lesson,
                           "finished_label": day.lower() if day in ("Today", "Yesterday") else f"on {day}",
                           "subject": course.offering.subject,
                           "questions": PracticeSet.objects.published().filter(topic=nxt.topic)
                           .aggregate(n=Count("questions"))["n"] or 0}
            break
    if recommended is None:
        for p in plan:
            if p["course"] and (not continue_card or p["course"].pk != exclude_course):
                nxt, _ = services.next_lesson(user, p["course"])
                if nxt:
                    recommended = {"lesson": nxt, "subject": p["subject"], "questions": 0}
                    break

    attempts = Attempt.objects.filter(user=user, completed_at__isnull=False, total__gt=0)
    avg_score = None
    if attempts.exists():
        scores = [a.score for a in attempts.only("correct_count", "total")]
        avg_score = round(sum(scores) / len(scores))

    week = weekly_activity(user, today, profile.daily_goal_minutes)
    upcoming = (
        StudySession.objects.filter(user=user, completed_at__isnull=True, starts_at__date__gte=today,
                                    starts_at__date__lte=today + timedelta(days=6))
        .select_related("subject").order_by("starts_at")[:4]
    )
    recent = list(
        LessonProgress.objects.filter(user=user, completed_at__isnull=False)
        .select_related("lesson__topic__module__course__offering__subject").order_by("-completed_at")[:4]
    )
    last_scores = {}
    for attempt in (Attempt.objects.filter(user=user, completed_at__isnull=False,
                                           practice_set__lesson__in=[r.lesson for r in recent])
                    .select_related("practice_set").order_by("completed_at")):
        last_scores[attempt.practice_set.lesson_id] = attempt
    for r in recent:
        r.day_label = relative_day(r.completed_at, today)
        r.attempt = last_scores.get(r.lesson_id)

    countdown = None
    if profile.exam_date:
        lesson_ids = services.published_lessons().filter(topic__module__course__in=courses).values_list("pk", flat=True)
        countdown = motivation.exam_countdown(profile.exam_date, overall.done, overall.total,
                                              motivation.recent_completions(user, today, lesson_ids=lesson_ids), today)

    return render(request, "dashboard/home.html", {
        "countdown": countdown, "rest_today": RestDay.objects.filter(user=user, date=today).exists(),
        "student": profile, "greeting": greeting(now), "plan": plan, "overall": overall,
        "continue_card": continue_card, "recommended": recommended, "avg_score": avg_score,
        "week": week, "week_total": fmt_minutes(week["total_minutes"]),
        "week_goal": fmt_minutes(week["weekly_goal_minutes"]),
        "streak": learning_streak(user, today), "upcoming": [
            {"session": s, "day": "Today" if timezone.localtime(s.starts_at).date() == today
             else WEEKDAY_SHORT[timezone.localtime(s.starts_at).weekday()]} for s in upcoming],
        "recent": recent, "today": today, "nav_active": "dashboard",
        "reviews_due": review_summary(user)["due"],
    })
