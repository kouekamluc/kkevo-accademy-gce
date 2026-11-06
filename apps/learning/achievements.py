"""Milestones that reward steady learning, and the "today" strip shown after a lesson or quiz.

Everything here is worked out from records the platform already keeps (completed lessons, daily
activity, practice attempts), so a milestone can never be earned by clicking around. Awarding is
idempotent: calling `award` again returns nothing new.
"""

from dataclasses import dataclass
from urllib.parse import quote

from django.utils import timezone

from . import motivation
from .models import Achievement, DailyActivity, LessonProgress


@dataclass(frozen=True)
class Milestone:
    code: str
    title: str
    description: str
    # Stat that must reach `target`: lessons, streak, best_score, perfect, mocks.
    stat: str
    target: int


CATALOGUE = [
    Milestone("first_lesson", "First step", "Completed your first lesson.", "lessons", 1),
    Milestone("lessons_10", "Ten lessons", "Completed 10 lessons.", "lessons", 10),
    Milestone("lessons_50", "Fifty lessons", "Completed 50 lessons.", "lessons", 50),
    Milestone("streak_3", "Three days running", "Learned 3 days in a row.", "streak", 3),
    Milestone("streak_7", "A full week", "Learned 7 days in a row.", "streak", 7),
    Milestone("streak_30", "A month of learning", "Learned 30 days in a row.", "streak", 30),
    Milestone("score_80", "Sharp", "Scored 80% or more on a practice set.", "best_score", 80),
    Milestone("perfect", "Full marks", "Got every question right on a practice set of 5 or more.", "perfect", 1),
    Milestone("first_mock", "Exam ready", "Finished your first mock exam paper.", "mocks", 1),
]
BY_CODE = {m.code: m for m in CATALOGUE}


def stats(user, today=None):
    from apps.practice.models import Attempt

    today = today or timezone.localdate()
    attempts = list(Attempt.objects.filter(user=user, completed_at__isnull=False, total__gt=0)
                    .select_related("practice_set").order_by("-completed_at")[:300])
    return {
        "lessons": LessonProgress.objects.filter(user=user, completed_at__isnull=False).count(),
        "streak": motivation.learning_streak(user, today),
        "best_score": max((a.score for a in attempts), default=0),
        "perfect": int(any(a.score == 100 and a.total >= 5 for a in attempts)),
        "mocks": sum(1 for a in attempts if a.practice_set.is_mock),
    }


def award(user, today=None):
    """Record any milestones now reached and return the newly earned ones (oldest first)."""
    have = set(Achievement.objects.filter(user=user).values_list("code", flat=True))
    pending = [m for m in CATALOGUE if m.code not in have]
    if not pending:
        return []
    current = stats(user, today)
    new = [m for m in pending if current[m.stat] >= m.target]
    for m in new:
        Achievement.objects.get_or_create(user=user, code=m.code)
    return new


def describe(request, milestones):
    """Template-ready dicts including a WhatsApp share link (students share there far more than anywhere else)."""
    site = request.build_absolute_uri("/")
    out = []
    for m in milestones:
        text = f"I just earned “{m.title}” on KKEVO Academy: {m.description} {site}"
        out.append({"code": m.code, "title": m.title, "description": m.description,
                    "share_url": f"https://wa.me/?text={quote(text)}"})
    return out


def earned_and_next(user):
    """For the progress page: milestones earned, and how far the student is from the rest."""
    earned = {a.code: a.earned_at for a in Achievement.objects.filter(user=user)}
    current = stats(user)
    rows = []
    for m in CATALOGUE:
        have = min(current[m.stat], m.target)
        rows.append({"milestone": m, "earned_at": earned.get(m.code), "have": have, "target": m.target,
                     "percent": round(100 * have / m.target)})
    return rows


def today_strip(user, today=None):
    """Minutes learned today against the daily goal, plus the streak, for the moment after a lesson."""
    from apps.accounts.utils import get_profile

    today = today or timezone.localdate()
    seconds = DailyActivity.objects.filter(user=user, date=today).values_list("seconds", flat=True).first() or 0
    goal = get_profile(user).daily_goal_minutes
    minutes = round(seconds / 60)
    return {"minutes": minutes, "goal": goal, "percent": min(100, round(100 * minutes / goal)) if goal else 0,
            "reached": minutes >= goal, "streak": motivation.learning_streak(user, today)}


# ---------------------------------------------------------------- points and levels

POINTS_PER_LESSON = 10
POINTS_PER_CORRECT_ANSWER = 2


def points(user):
    """Points are earned by learning only: 10 per completed lesson and 2 per correct practice answer."""
    from apps.practice.models import Answer

    lessons = LessonProgress.objects.filter(user=user, completed_at__isnull=False).count()
    correct = Answer.objects.filter(attempt__user=user, is_correct=True).count()
    return lessons * POINTS_PER_LESSON + correct * POINTS_PER_CORRECT_ANSWER


def level_for(total):
    """Level n needs 50*n*(n-1) points (100, 300, 600, ...), so early levels come quickly."""
    level = 1
    while total >= 50 * (level + 1) * level:
        level += 1
    start, nxt = 50 * level * (level - 1), 50 * (level + 1) * level
    return {"level": level, "points": total, "into": total - start, "needed": nxt - start,
            "to_next": nxt - total, "percent": round(100 * (total - start) / (nxt - start))}


def journey(user, today=None):
    """Everything the progress page's hero needs: level, streak and milestone rows."""
    rows = earned_and_next(user)
    return {"milestones": rows, "milestones_earned": sum(1 for r in rows if r["earned_at"]),
            "rank": level_for(points(user)), "streak": motivation.learning_streak(user, today or timezone.localdate())}
