"""Build a study plan automatically: spread the student's next lessons and due revisions over the coming days.

Pure scheduling lives here (no request handling) so it can be tested on its own.
"""

from datetime import datetime, time, timedelta
from itertools import zip_longest

from django.utils import timezone

from . import analytics, services
from .models import RestDay, SessionKind, StudySession

GAP_MINUTES = 10
LATEST_END = time(23, 30)
MIN_SESSION, MAX_SESSION = 15, 60
MAX_SESSIONS = 40
LESSONS_PER_COURSE = 14
REVISIONS = 3


def _minutes(lesson):
    """A lesson's length as a session length: rounded up to 5 minutes, kept between 15 and 60."""
    raw = int(lesson.estimated_minutes or 20)
    return max(MIN_SESSION, min(MAX_SESSION, 5 * -(-raw // 5)))


def candidates(user, courses, today):
    """Things worth planning, in the order they should be studied (revision first, then subjects taking turns)."""
    pending = set(StudySession.objects.filter(user=user, completed_at__isnull=True, lesson__isnull=False,
                                              starts_at__date__gte=today).values_list("lesson_id", flat=True))
    pending_topics = set(StudySession.objects.filter(user=user, completed_at__isnull=True, topic__isnull=False,
                                                     starts_at__date__gte=today).values_list("topic_id", flat=True))
    out = []
    due = sorted((e for e in analytics.topic_scores(user).values() if e["needs_revision"]),
                 key=lambda e: analytics.revision_due(e, today))
    for e in due[:REVISIONS]:
        if e["topic"].pk in pending_topics:
            continue
        target = e["practice_set"].lesson
        if target and target.pk in pending:
            continue
        out.append({"title": f"Revise {e['topic'].title}"[:120], "subject": e["subject"], "lesson": target,
                    "topic": e["topic"], "kind": SessionKind.REVISION, "minutes": 30})
    queues = []
    for course in courses:
        queue = [lesson for lesson in services.upcoming_lessons(user, course, LESSONS_PER_COURSE) if lesson.pk not in pending]
        queues.append(queue)
    for round_ in zip_longest(*queues):
        for lesson in round_:
            if lesson is not None:
                out.append({"title": lesson.title[:120], "subject": lesson.course.offering.subject, "lesson": lesson,
                            "topic": None, "kind": SessionKind.STUDY, "minutes": _minutes(lesson)})
    return out


def _ceil5(moment):
    """Round up to the next 5 minutes."""
    moment = moment.replace(second=0, microsecond=0)
    return moment + timedelta(minutes=(-moment.minute) % 5)


def _busy(user, first_day, last_day, tz):
    """Existing sessions as (start, end) pairs per local date, so new ones never overlap them."""
    start = timezone.make_aware(datetime.combine(first_day, time.min), tz)
    end = timezone.make_aware(datetime.combine(last_day, time.max), tz)
    busy = {}
    for s in StudySession.objects.filter(user=user, starts_at__range=(start, end)):
        busy.setdefault(timezone.localtime(s.starts_at).date(), []).append((s.starts_at, s.ends_at))
    return busy


def build_plan(user, profile, courses, first_day, day_count, weekdays, start_time, now=None):
    """Return a list of session dicts (title, subject, lesson, topic, kind, starts_at, minutes).

    Each chosen weekday gets sessions from `start_time` until the daily goal is reached (at least one),
    skipping rest days and times already taken. Today only counts if there is still time left.
    """
    now = now or timezone.now()
    tz = timezone.get_current_timezone()
    today = timezone.localtime(now).date()
    first_day = max(first_day, today)
    days = [first_day + timedelta(days=i) for i in range(day_count)]
    days = [d for d in days if d.weekday() in weekdays]
    pool = candidates(user, courses, today)
    if not days or not pool:
        return []
    rest = set(RestDay.objects.filter(user=user, date__gte=days[0], date__lte=days[-1]).values_list("date", flat=True))
    busy = _busy(user, days[0], days[-1], tz)
    goal = max(MIN_SESSION, profile.daily_goal_minutes)
    plan = []
    for day in days:
        if day in rest or not pool or len(plan) >= MAX_SESSIONS:
            continue
        cursor = timezone.make_aware(datetime.combine(day, start_time), tz)
        if day == today and cursor <= now + timedelta(minutes=10):
            cursor = _ceil5(now + timedelta(minutes=15))
        used = 0
        while pool and used < goal and len(plan) < MAX_SESSIONS:
            item = pool[0]
            end = cursor + timedelta(minutes=item["minutes"])
            clash = next((b for b in busy.get(day, []) if cursor < b[1] and end > b[0]), None)
            if clash:
                cursor = clash[1] + timedelta(minutes=GAP_MINUTES)
                continue
            if timezone.localtime(end).date() != day or timezone.localtime(end).time() > LATEST_END:
                break
            pool.pop(0)
            plan.append({**item, "starts_at": cursor})
            busy.setdefault(day, []).append((cursor, end))
            used += item["minutes"]
            cursor = end + timedelta(minutes=GAP_MINUTES)
    return plan


def save_plan(user, plan):
    return StudySession.objects.bulk_create([
        StudySession(user=user, title=p["title"], subject=p["subject"], lesson=p["lesson"], topic=p["topic"],
                     kind=p["kind"], starts_at=p["starts_at"], duration_minutes=p["minutes"])
        for p in plan])


def complete_for_lesson(user, lesson):
    """A finished lesson ticks off the planner sessions that were set aside for it."""
    return StudySession.objects.filter(user=user, lesson=lesson, completed_at__isnull=True,
                                       kind=SessionKind.STUDY).update(completed_at=timezone.now())
