"""Usage for the pilot: are students signing up, coming back, finishing lessons and practising?

Counts students only (staff accounts are left out). Everything is computed from the records the app
already keeps: lesson progress, practice attempts, daily learning time and reports. The page answers
a few questions at a glance; it is not a full analytics tool.
"""

from datetime import datetime, time, timedelta

from django.contrib.auth import get_user_model
from django.db.models import Avg, Count, Exists, F, OuterRef, Sum
from django.db.models.functions import TruncDate
from django.shortcuts import render
from django.utils import timezone

from apps.academics.models import AcademicLevel
from apps.learning.models import DailyActivity, LessonFeedback, LessonProgress
from apps.practice.models import Attempt

from ._common import _context, staff_required

User = get_user_model()
PERIODS = (7, 30)
SUBJECT = "lesson__topic__module__course__offering__subject__name"


def _active_by_day(since_date, today):
    """Student ids active on each day: learning time, a practice set started, a lesson started or finished."""
    days = {since_date + timedelta(days=i): set() for i in range((today - since_date).days + 1)}
    sources = [
        DailyActivity.objects.filter(date__gte=since_date, seconds__gt=0, user__is_staff=False)
        .values_list("date", "user_id"),
        Attempt.objects.filter(started_at__date__gte=since_date, user__is_staff=False)
        .annotate(day=TruncDate("started_at")).values_list("day", "user_id"),
        LessonProgress.objects.filter(started_at__date__gte=since_date, user__is_staff=False)
        .annotate(day=TruncDate("started_at")).values_list("day", "user_id"),
        LessonProgress.objects.filter(last_viewed_at__date__gte=since_date, user__is_staff=False)
        .annotate(day=TruncDate("last_viewed_at")).values_list("day", "user_id"),
        LessonProgress.objects.filter(completed_at__date__gte=since_date, user__is_staff=False)
        .annotate(day=TruncDate("completed_at")).values_list("day", "user_id"),
    ]
    for qs in sources:
        for day, user_id in qs.distinct():
            if day in days:
                days[day].add(user_id)
    return days


def _bars(rows, key="n"):
    """Add a 0-100 width to each row, relative to the largest value, for CSS bars."""
    top = max((r[key] for r in rows), default=0) or 1
    for r in rows:
        r["pct"] = round(r[key] * 100 / top)
    return rows


@staff_required
def usage(request):
    try:
        days = int(request.GET.get("days", 7))
    except ValueError:
        days = 7
    if days not in PERIODS:
        days = 7
    now = timezone.now()
    today = timezone.localdate()
    since_date = today - timedelta(days=days - 1)
    since = timezone.make_aware(datetime.combine(since_date, time.min))  # midnight, local time

    students = User.objects.filter(is_staff=False, is_active=True)
    progress = LessonProgress.objects.filter(user__is_staff=False)
    attempts = Attempt.objects.filter(user__is_staff=False, completed_at__gte=since)

    by_day = _active_by_day(since_date, today)
    active_ids = set().union(*by_day.values())
    day_counts = {}
    for ids in by_day.values():
        for user_id in ids:
            day_counts[user_id] = day_counts.get(user_id, 0) + 1
    returning = sum(1 for n in day_counts.values() if n >= 2)
    daily = _bars([{"day": d, "n": len(ids)} for d, ids in by_day.items()])

    seconds = DailyActivity.objects.filter(date__gte=since_date, user__is_staff=False).aggregate(s=Sum("seconds"))["s"] or 0
    headline = {
        "students": students.count(),
        "new_students": students.filter(date_joined__gte=since).count(),
        "active": len(active_ids),
        "lessons_completed": progress.filter(completed_at__gte=since).count(),
        "practice_finished": attempts.filter(practice_set__is_mock=False).count(),
        "mocks_finished": attempts.filter(practice_set__is_mock=True).count(),
        "minutes": seconds // 60,
        "reports": LessonFeedback.objects.filter(created_at__gte=since).count(),
    }
    headline["avg_minutes"] = round(headline["minutes"] / headline["active"]) if headline["active"] else 0

    # Funnel: of the students who joined in the period, how far did they get?
    joined = students.filter(date_joined__gte=since)
    signed = joined.count()
    funnel = [
        {"label": "Signed up", "n": signed},
        {"label": "Chose their class and subjects", "n": joined.filter(profile__onboarded_at__isnull=False).count()},
        {"label": "Opened a lesson",
         "n": joined.filter(Exists(LessonProgress.objects.filter(user=OuterRef("pk")))).count()},
        {"label": "Finished a lesson", "n": joined.filter(Exists(
            LessonProgress.objects.filter(user=OuterRef("pk"), completed_at__isnull=False))).count()},
        {"label": "Finished a practice set", "n": joined.filter(Exists(
            Attempt.objects.filter(user=OuterRef("pk"), completed_at__isnull=False))).count()},
    ]
    for step in funnel:
        step["pct"] = round(step["n"] * 100 / signed) if signed else 0

    # By class: how many students in each class, and how many of them were active.
    level_counts = dict(students.values_list("profile__level_id").annotate(n=Count("pk")))
    level_active = dict(students.filter(pk__in=active_ids).values_list("profile__level_id").annotate(n=Count("pk")))
    classes = [{"name": lvl.name, "n": level_counts.get(lvl.pk, 0), "active": level_active.get(lvl.pk, 0)}
               for lvl in AcademicLevel.objects.filter(is_active=True).order_by("order")]
    if level_counts.get(None):
        classes.append({"name": "No class chosen yet", "n": level_counts[None], "active": level_active.get(None, 0)})
    _bars(classes)

    subjects = _bars(list(progress.filter(completed_at__gte=since).values(name=F(SUBJECT))
                          .annotate(n=Count("pk")).order_by("-n", "name")[:8]))
    lesson_fields = dict(title=F("lesson__title"), course=F("lesson__topic__module__course__title"))
    opened = list(progress.filter(last_viewed_at__gte=since).values("lesson_id", **lesson_fields)
                  .annotate(n=Count("user", distinct=True)).order_by("-n", "title")[:8])
    # Started in the period, still not finished an hour later: where students give up.
    dropoff = list(progress.filter(started_at__gte=since, started_at__lte=now - timedelta(hours=1),
                                   completed_at__isnull=True)
                   .values("lesson_id", **lesson_fields)
                   .annotate(n=Count("user", distinct=True), avg_percent=Avg("percent"))
                   .order_by("-n", "title")[:8])

    return render(request, "studio/usage.html", _context(
        request, studio_active="usage", days=days, periods=PERIODS, since_date=since_date, today=today,
        headline=headline, returning=returning, daily=daily, funnel=funnel, classes=classes, subjects=subjects,
        opened=_bars(opened), dropoff=dropoff))
