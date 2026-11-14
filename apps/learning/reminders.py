"""Daily study reminder emails.

One short, friendly email a day, only to students who have not studied yet today and are not resting.
No loss-framing ("you will lose your streak"): see motivation.py. Run `manage.py send_reminders` every hour
(cron or the host's scheduler); it sends each student at most one email a day, at their chosen hour.
"""

from django.conf import settings
from django.core import signing
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

from . import motivation, services
from .models import DailyActivity, Enrollment, RestDay, StudySession

SALT = "kkevo.reminders.unsubscribe"


def unsubscribe_token(user):
    return signing.dumps(user.pk, salt=SALT)


def user_from_token(token):
    from django.contrib.auth import get_user_model

    try:
        pk = signing.loads(token, salt=SALT)
    except signing.BadSignature:
        return None
    return get_user_model().objects.filter(pk=pk).first()


def studied_today(user, today):
    return DailyActivity.objects.filter(user=user, date=today, seconds__gte=motivation.ACTIVE_SECONDS).exists()


def build(user, today=None):
    """What to tell this student today, or None when no reminder is due (already studied, resting, nothing to study)."""
    today = today or timezone.localdate()
    if studied_today(user, today) or RestDay.objects.filter(user=user, date=today).exists():
        return None
    sessions = list(StudySession.objects.filter(user=user, starts_at__date=today, completed_at__isnull=True)
                    .order_by("starts_at"))
    next_up = None
    if not sessions:
        for enrollment in Enrollment.objects.filter(user=user).select_related("offering"):
            course = services.course_for_offering(enrollment.offering)
            if course is None:
                continue
            lesson, progress = services.next_lesson(user, course)
            if lesson is not None and (progress is None or not progress.is_completed):
                next_up = lesson
                break
    if not sessions and next_up is None:
        return None
    return {"sessions": sessions, "next_up": next_up, "streak": motivation.learning_streak(user, today)}


def send_for(user, today=None):
    """Send the reminder if one is due. Returns True when an email was sent."""
    today = today or timezone.localdate()
    if not user.has_real_email:
        return False
    plan = build(user, today)
    if plan is None:
        return False
    base = settings.SITE_BASE_URL
    context = {**plan, "user": user, "today_url": base + reverse("dashboard:home"),
               "unsubscribe_url": base + reverse("accounts:reminders_off", args=[unsubscribe_token(user)])}
    if plan["sessions"]:
        count = len(plan["sessions"])
        subject = "Your study plan today: " + (plan["sessions"][0].title if count == 1 else f"{count} sessions planned")
    else:
        subject = "A quick lesson today?"
    send_mail(subject, render_to_string("learning/email/reminder.txt", context), None, [user.email])
    return True
