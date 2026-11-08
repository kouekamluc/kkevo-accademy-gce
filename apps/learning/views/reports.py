"""Weekly summary, the parent report and the daily-goal suggestion."""

from datetime import timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from .. import motivation
from ..models import LinkPurpose, PrivateLink
from apps.accounts.decorators import onboarding_required
from apps.accounts.utils import get_profile

from ._common import _safe_next
from .links import _link_url, _private_headers
from .planner import _countdown


# --------------------------------------------------------------------------- weekly summary & parent report
REPORT_WEEKS = 8


def _weekly_context(user, request):
    profile = get_profile(user)
    today = timezone.localdate()
    start = motivation.parse_week(request.GET.get("week"), today, earliest_weeks=REPORT_WEEKS)
    summary = motivation.weekly_summary(user, profile, start, today)
    this_week = motivation.week_start(today)
    return {
        "summary": summary, "profile": profile, "today": today,
        "prev_week": (start - timedelta(weeks=1)).isoformat() if start > this_week - timedelta(weeks=REPORT_WEEKS) else None,
        "next_week": (start + timedelta(weeks=1)).isoformat() if start < this_week else None,
        "streak": motivation.learning_streak(user, today), "countdown": _countdown(user, profile, today),
    }


@onboarding_required
def weekly(request):
    ctx = _weekly_context(request.user, request)
    link = PrivateLink.objects.filter(user=request.user, purpose=LinkPurpose.REPORT).first()
    ctx.update({"report_link": link, "report_url": _link_url(request, link), "nav_active": "progress",
                "goal_suggestion": motivation.goal_suggestion(request.user, ctx["profile"].daily_goal_minutes, ctx["today"])})
    return render(request, "learning/weekly.html", ctx)


@require_GET
def report(request, token):
    link = PrivateLink.resolve(token, LinkPurpose.REPORT)
    if link is None:
        raise Http404
    ctx = _weekly_context(link.user, request)
    ctx.update({"student_name": link.user.first_name or "Your student", "token": token})
    return _private_headers(render(request, "learning/report.html", ctx))


@login_required
@require_POST
def goal_adjust(request):
    """Apply the suggested daily goal (recomputed here, never taken from the form)."""
    profile = get_profile(request.user)
    suggestion = motivation.goal_suggestion(request.user, profile.daily_goal_minutes, timezone.localdate())
    if suggestion:
        profile.daily_goal_minutes = suggestion["minutes"]
        profile.save(update_fields=["daily_goal_minutes", "updated_at"])
        messages.success(request, f"Daily goal set to {suggestion['minutes']} minutes.")
    else:
        messages.info(request, "Your daily goal looks right for now.")
    return redirect(_safe_next(request, reverse("learning:weekly")))
