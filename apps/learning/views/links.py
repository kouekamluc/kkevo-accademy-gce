"""Private links: the calendar feed and the parent report link."""

from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from .. import motivation
from ..models import LinkPurpose, PrivateLink, StudySession
from apps.accounts.utils import get_profile

from ._common import _safe_next


# --------------------------------------------------------------------------- private links (calendar, parent report)
def _link_url(request, link):
    if not link:
        return ""
    name = "learning:calendar_feed" if link.purpose == LinkPurpose.CALENDAR else "learning:report"
    return request.build_absolute_uri(reverse(name, args=[link.token]))


@login_required
@require_POST
def private_link(request, purpose):
    if purpose not in LinkPurpose.values:
        raise Http404
    label = LinkPurpose(purpose).label.lower()
    if request.POST.get("action") == "revoke":
        PrivateLink.objects.filter(user=request.user, purpose=purpose).delete()
        messages.success(request, f"Your {label} link is switched off. Anyone using the old link can no longer open it.")
    else:
        replaced = PrivateLink.objects.filter(user=request.user, purpose=purpose).exists()
        PrivateLink.issue(request.user, purpose)
        messages.success(request, f"New {label} link created. The old one no longer works." if replaced
                         else f"Your private {label} link is ready.")
    fallback = reverse("learning:planner") if purpose == LinkPurpose.CALENDAR else reverse("learning:weekly")
    return redirect(_safe_next(request, fallback))


def _private_headers(response):
    response["Cache-Control"] = "private, no-store"
    response["X-Robots-Tag"] = "noindex, nofollow"
    response["Referrer-Policy"] = "no-referrer"
    return response


@require_GET
def calendar_feed(request, token):
    link = PrivateLink.resolve(token, LinkPurpose.CALENDAR)
    if link is None:
        raise Http404
    now = timezone.now()
    sessions = (StudySession.objects.filter(user=link.user, starts_at__gte=now - timedelta(days=30),
                                            starts_at__lte=now + timedelta(days=200))
                .select_related("subject", "lesson__topic__module__course").order_by("starts_at"))
    body = motivation.build_ics(sessions, host=request.get_host().split(":")[0],
                                exam_date=get_profile(link.user).exam_date,
                                base_url=f"{request.scheme}://{request.get_host()}")
    response = HttpResponse(body, content_type="text/calendar; charset=utf-8")
    response["Content-Disposition"] = 'inline; filename="gce-study-planner.ics"'
    return _private_headers(response)
