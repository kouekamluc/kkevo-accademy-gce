"""Read-only analytics for the progress page (10) and planner (11)."""

from collections import defaultdict
from datetime import date, timedelta

from django.utils import timezone

from apps.practice.models import MASTERY_MARK, PASS_MARK, Answer, Attempt

from .models import DailyActivity, LessonProgress


def term_start(today):
    """Cameroon school terms: Sept–Dec, Jan–Mar, Apr–Jun (Jul–Aug counts with the third term)."""
    if today.month >= 9:
        return date(today.year, 9, 1)
    if today.month <= 3:
        return date(today.year, 1, 1)
    return date(today.year, 4, 1)


RANGES = {"7d": ("7 days", 7), "30d": ("30 days", 30), "term": ("This term", None)}


def period(range_key, today):
    label, days = RANGES.get(range_key, RANGES["30d"])
    start = term_start(today) if days is None else today - timedelta(days=days - 1)
    length = (today - start).days + 1
    return start, length


def completed_attempts(user, start=None, end=None):
    qs = Attempt.objects.filter(user=user, completed_at__isnull=False, total__gt=0)
    if start:
        qs = qs.filter(completed_at__date__gte=start)
    if end:
        qs = qs.filter(completed_at__date__lte=end)
    return qs.select_related("practice_set__topic__module__course__offering__subject")


def average_score(attempts):
    scores = [a.score for a in attempts]
    return round(sum(scores) / len(scores)) if scores else None


def weekly_hours(user, today, weeks=8):
    monday = today - timedelta(days=today.weekday())
    start = monday - timedelta(weeks=weeks - 1)
    totals = defaultdict(int)
    for day, seconds in DailyActivity.objects.filter(user=user, date__gte=start).values_list("date", "seconds"):
        totals[(day - start).days // 7] += seconds
    rows = []
    for i in range(weeks):
        week_start = start + timedelta(weeks=i)
        rows.append({"start": week_start, "hours": round(totals[i] / 3600, 1), "is_current": i == weeks - 1,
                     "label": "This week" if i == weeks - 1 else f"{week_start.day} {week_start.strftime('%b')}"})
    top = max([r["hours"] for r in rows] + [1]) * 1.15
    for r in rows:
        r["height"] = round(r["hours"] / top * 100)
    return rows


def topic_scores(user):
    """Latest score per topic and mastery counts: {topic_id: {...}}."""
    by_topic = {}
    for attempt in completed_attempts(user).filter(practice_set__is_mock=False).order_by("completed_at"):
        topic = attempt.practice_set.topic
        entry = by_topic.setdefault(topic.pk, {"topic": topic, "subject": attempt.practice_set.subject,
                                               "latest": None, "last_at": None, "mastered_runs": 0})
        entry["practice_set"] = attempt.practice_set  # the set attempted most recently (revise links use it)
        entry["latest"] = attempt.score
        entry["last_at"] = attempt.completed_at
        if attempt.score >= MASTERY_MARK:
            entry["mastered_runs"] += 1
    for entry in by_topic.values():
        # Same rule as practice/mastery.py: 80%+ twice, and still 80%+ on the latest attempt
        entry["mastered"] = entry["mastered_runs"] >= 2 and (entry["latest"] or 0) >= MASTERY_MARK
        entry["needs_revision"] = entry["latest"] is not None and entry["latest"] < PASS_MARK
    return by_topic


def revision_due(entry, today):
    """Spaced review: weaker scores come back sooner."""
    score = entry["latest"] or 0
    interval = 1 if score < 40 else 3 if score < PASS_MARK else 7
    last = timezone.localtime(entry["last_at"]).date()
    due = max(today, last + timedelta(days=interval))
    return due


def due_label(due, today):
    if due == today:
        return "Tonight"
    if (due - today).days < 7:
        return due.strftime("%a")
    return f"{due.strftime('%a')} {due.day}"


def answer_totals(user):
    answers = Answer.objects.filter(attempt__user=user, attempt__completed_at__isnull=False)
    correct = answers.filter(is_correct=True).count()
    return correct, answers.count() - correct


def completions_between(user, start, end, lesson_ids):
    return LessonProgress.objects.filter(user=user, completed_at__date__gte=start, completed_at__date__lte=end,
                                         lesson_id__in=lesson_ids).count()
