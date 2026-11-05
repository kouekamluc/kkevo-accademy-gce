"""Streaks, rest days, exam countdown, weekly summaries and goal suggestions.

Everything here is derived from the student's own records. Kept free of dark
patterns on purpose: no loss-framing, no paid streak repairs, rest is allowed and
the numbers shown to parents are the same ones the student sees.
"""

import math
from datetime import date, datetime, time, timedelta
from datetime import timezone as dt_timezone

from django.utils import timezone

from apps.practice.models import Attempt

from .models import DailyActivity, LessonProgress, RestDay, StudySession

ACTIVE_SECONDS = 60  # a day counts towards the streak after one minute of learning
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def fmt_minutes(minutes):
    hours, mins = divmod(int(minutes), 60)
    return f"{hours}h {mins:02d}m" if hours else f"{mins} min"


def week_start(day):
    return day - timedelta(days=day.weekday())


# --------------------------------------------------------------------------- streaks & rest days
def active_days(user, since):
    return set(DailyActivity.objects.filter(user=user, seconds__gte=ACTIVE_SECONDS, date__gte=since)
               .values_list("date", flat=True))


def rest_days(user, since, until=None):
    qs = RestDay.objects.filter(user=user, date__gte=since)
    if until:
        qs = qs.filter(date__lte=until)
    return set(qs.values_list("date", flat=True))


def learning_streak(user, today):
    """Consecutive learning days up to today. Planned rest days are skipped, not broken.

    Today only counts once the student has learned (or rests); an empty today does not
    break a streak that ran until yesterday.
    """
    since = today - timedelta(days=400)
    active, rest = active_days(user, since), rest_days(user, since, today)
    day = today if (today in active or today in rest) else today - timedelta(days=1)
    streak = 0
    while day >= since:
        if day in active:
            streak += 1
        elif day not in rest:
            break
        day -= timedelta(days=1)
    return streak


def can_rest(user, day):
    """(allowed, reason). One rest day per Monday–Sunday week, today or later."""
    today = timezone.localdate()
    if day < today:
        return False, "Rest days are planned ahead — you can’t add one for a day that has passed."
    if day > today + timedelta(days=60):
        return False, "Plan rest days up to two months ahead."
    start = week_start(day)
    taken = RestDay.objects.filter(user=user, date__gte=start, date__lte=start + timedelta(days=6)).exclude(date=day)
    if taken.count() >= RestDay.PER_WEEK:
        return False, "You already have a rest day that week."
    return True, ""


# --------------------------------------------------------------------------- exam countdown
def exam_countdown(exam_date, done, total, recent_completed, today, recent_days=14):
    """Days left and the lesson pace needed to finish the plan before the exam.

    The target leaves two weeks of revision before the exam when there is time for it.
    `recent_completed` is the number of lessons finished in the last `recent_days` days.
    """
    if not exam_date:
        return None
    days_left = (exam_date - today).days
    info = {"date": exam_date, "days_left": days_left, "past": days_left < 0, "is_today": days_left == 0,
            "remaining": max(0, total - done), "total": total, "done": done}
    if days_left <= 0:
        return info
    buffer_days = 14 if days_left > 28 else 0
    study_days = days_left - buffer_days
    remaining = info["remaining"]
    per_day = remaining / study_days if study_days else 0
    recent_pace = recent_completed / recent_days
    info.update({
        "weeks_left": days_left // 7,
        "buffer_days": buffer_days,
        "target_date": exam_date - timedelta(days=buffer_days),
        "per_day": round(per_day, 1),
        "per_week": math.ceil(per_day * 7) if remaining else 0,
        "recent_per_week": round(recent_pace * 7, 1),
        "finished": remaining == 0 and total > 0,
        # On track when the last two weeks' pace would finish in time (or nothing is left).
        "on_track": remaining == 0 or recent_pace >= per_day,
    })
    return info


def recent_completions(user, today, days=14, lesson_ids=None):
    qs = LessonProgress.objects.filter(user=user, completed_at__isnull=False,
                                       completed_at__date__gt=today - timedelta(days=days))
    if lesson_ids is not None:
        qs = qs.filter(lesson_id__in=lesson_ids)
    return qs.count()


# --------------------------------------------------------------------------- daily goal suggestions
GOAL_STEP = 10
GOAL_MIN, GOAL_SUGGEST_MAX = 10, 120  # never nudge above two hours a day


def goal_suggestion(user, goal_minutes, today):
    """Suggest a small goal change from the last 14 days, or None.

    Raise only when the goal was met on almost every day; lower when it was rarely met,
    because a goal you keep beats an ambitious one you miss.
    """
    start = today - timedelta(days=13)
    minutes = [round(s / 60) for s in DailyActivity.objects.filter(user=user, date__gte=start, date__lte=today)
               .values_list("seconds", flat=True)]
    met = sum(m >= goal_minutes for m in minutes)
    active = sum(m >= 1 for m in minutes)
    if met >= 12 and goal_minutes + GOAL_STEP <= GOAL_SUGGEST_MAX:
        return {"direction": "up", "minutes": goal_minutes + GOAL_STEP, "met": met,
                "reason": f"You reached your goal on {met} of the last 14 days."}
    if active >= 4 and met <= 3 and goal_minutes - GOAL_STEP >= GOAL_MIN:
        return {"direction": "down", "minutes": goal_minutes - GOAL_STEP, "met": met,
                "reason": f"You studied on {active} of the last 14 days but reached your goal on {met}. "
                          "A goal you can keep builds the habit."}
    return None


# --------------------------------------------------------------------------- weekly summary
def weekly_summary(user, profile, start, today):
    """Monday–Sunday summary used by the student's weekly page and the parent report."""
    end = start + timedelta(days=6)
    goal = profile.daily_goal_minutes
    seconds = dict(DailyActivity.objects.filter(user=user, date__gte=start, date__lte=end).values_list("date", "seconds"))
    rests = rest_days(user, start, end)
    days = []
    for i in range(7):
        d = start + timedelta(days=i)
        m = round(seconds.get(d, 0) / 60)
        days.append({"date": d, "label": WEEKDAYS[i], "minutes": m, "reached": m >= goal, "rest": d in rests,
                     "future": d > today, "is_today": d == today})
    top = max([d["minutes"] for d in days] + [goal]) * 1.15 or 1
    for d in days:
        d["height"] = round(d["minutes"] / top * 100)

    tz = timezone.get_current_timezone()
    start_dt = timezone.make_aware(datetime.combine(start, time.min), tz)
    end_dt = timezone.make_aware(datetime.combine(end, time.max), tz)
    lessons = list(LessonProgress.objects.filter(user=user, completed_at__range=(start_dt, end_dt))
                   .select_related("lesson__topic__module__course__offering__subject").order_by("completed_at"))
    attempts = list(Attempt.objects.filter(user=user, completed_at__range=(start_dt, end_dt), total__gt=0)
                    .select_related("practice_set"))
    sessions = list(StudySession.objects.filter(user=user, starts_at__range=(start_dt, end_dt)))
    past_sessions = [s for s in sessions if timezone.localtime(s.starts_at).date() <= today]
    total_minutes = sum(d["minutes"] for d in days)
    prev = sum(round(s / 60) for s in DailyActivity.objects.filter(
        user=user, date__gte=start - timedelta(days=7), date__lt=start).values_list("seconds", flat=True))
    return {
        "start": start, "end": end, "days": days, "goal": goal, "goal_line": round(goal / top * 100),
        "total_minutes": total_minutes, "total_label": fmt_minutes(total_minutes), "prev_minutes": prev, "delta_minutes": total_minutes - prev,
        "active_days": sum(d["minutes"] >= 1 for d in days),
        "goal_days": sum(d["reached"] for d in days),
        "rest_count": len(rests),
        "lessons": lessons,
        "practice_count": len(attempts),
        "practice_avg": round(sum(a.score for a in attempts) / len(attempts)) if attempts else None,
        "sessions_planned": len(past_sessions),
        "sessions_done": sum(s.is_completed for s in past_sessions),
        "sessions_upcoming": len(sessions) - len(past_sessions),
        "is_current": start <= today <= end,
    }


def parse_week(value, today, earliest_weeks=None):
    """Monday of the week given as ?week=YYYY-MM-DD, clamped to [earliest, this week]."""
    try:
        day = date.fromisoformat(value or "")
    except ValueError:
        day = today
    start = min(week_start(day), week_start(today))
    if earliest_weeks is not None:
        start = max(start, week_start(today) - timedelta(weeks=earliest_weeks))
    return start


# --------------------------------------------------------------------------- recurring sessions
MAX_SERIES = 120


def recurrence_dates(first_day, weekdays, weeks):
    """Dates on the chosen weekdays (0=Mon) from `first_day` for `weeks` weeks (first week included)."""
    weekdays = sorted({int(w) for w in weekdays})
    start = week_start(first_day)
    out = []
    for w in range(weeks):
        for wd in weekdays:
            d = start + timedelta(weeks=w, days=wd)
            if d >= first_day:
                out.append(d)
    return out[:MAX_SERIES]


# --------------------------------------------------------------------------- iCalendar
def _ics_escape(text):
    return (str(text).replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,")
            .replace("\r\n", "\\n").replace("\n", "\\n"))


def _fold(line):
    """Fold lines longer than 75 octets (RFC 5545 §3.1)."""
    raw = line.encode("utf-8")
    if len(raw) <= 75:
        return line
    parts, chunk = [], b""
    for ch in line:
        b = ch.encode("utf-8")
        if len(chunk) + len(b) > (75 if not parts else 74):
            parts.append(chunk.decode("utf-8"))
            chunk = b""
        chunk += b
    parts.append(chunk.decode("utf-8"))
    return "\r\n ".join(parts)


def _utc(dt):
    return dt.astimezone(dt_timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def build_ics(sessions, host, exam_date=None, base_url="", reminder_minutes=15):
    """An iCalendar document for planner sessions (with a reminder before each)."""
    now = _utc(timezone.now())
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//KKEVO Academy//Study planner//EN",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:GCE study planner",
             "X-PUBLISHED-TTL:PT6H", "REFRESH-INTERVAL;VALUE=DURATION:PT6H"]
    for s in sessions:
        desc = [s.get_kind_display() + " session"]
        if s.subject_id:
            desc.append(f"Subject: {s.subject.name}")
        if s.lesson_id:
            desc.append(f"Lesson: {s.lesson.title}")
            if base_url:
                desc.append(base_url + s.lesson.get_absolute_url())
        lines += ["BEGIN:VEVENT", f"UID:session-{s.pk}@{host}", f"DTSTAMP:{now}",
                  f"DTSTART:{_utc(s.starts_at)}", f"DTEND:{_utc(s.ends_at)}",
                  f"SUMMARY:{_ics_escape(s.title)}", f"DESCRIPTION:{_ics_escape(chr(10).join(desc))}",
                  f"CATEGORIES:{_ics_escape(s.get_kind_display())}",
                  "STATUS:CONFIRMED"]
        if s.is_completed:
            lines.append("X-GCE-COMPLETED:TRUE")
        elif s.starts_at > timezone.now() and reminder_minutes:
            lines += ["BEGIN:VALARM", "ACTION:DISPLAY", f"DESCRIPTION:{_ics_escape(s.title)}",
                      f"TRIGGER:-PT{int(reminder_minutes)}M", "END:VALARM"]
        lines.append("END:VEVENT")
    if exam_date:
        lines += ["BEGIN:VEVENT", f"UID:exam-{exam_date.isoformat()}@{host}", f"DTSTAMP:{now}",
                  f"DTSTART;VALUE=DATE:{exam_date.strftime('%Y%m%d')}",
                  f"DTEND;VALUE=DATE:{(exam_date + timedelta(days=1)).strftime('%Y%m%d')}",
                  "SUMMARY:GCE exams begin", "TRANSP:TRANSPARENT", "END:VEVENT"]
    lines.append("END:VCALENDAR")
    return "\r\n".join(_fold(line) for line in lines) + "\r\n"
