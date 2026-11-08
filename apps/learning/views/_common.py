"""Small helpers shared by the learning views."""

from django.db.models import Prefetch

from .. import services
from ..models import Enrollment
from apps.courses.models import Course


WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def _safe_next(request, fallback):
    next_url = request.POST.get("next", "")
    return next_url if next_url.startswith("/") and not next_url.startswith("//") else fallback


def _plan(user):
    enrollments = list(
        Enrollment.objects.filter(user=user).select_related("offering__subject")
        .prefetch_related(Prefetch("offering__courses", queryset=Course.objects.published().order_by("order", "pk")))
    )
    plan = []
    for e in enrollments:
        course = services.primary_course(e.offering.courses.all())
        plan.append({"subject": e.offering.subject, "course": course})
    return plan


def fmt_minutes(minutes):
    hours, mins = divmod(int(round(minutes)), 60)
    return f"{hours}h {mins:02d}m" if hours else f"{mins}m"
