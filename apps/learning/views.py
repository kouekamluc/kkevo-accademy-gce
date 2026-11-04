from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import StudySession


@login_required
@require_POST
def session_toggle(request, pk):
    """Tick a planner session done / not done (dashboard 'Upcoming revision', planner tasks)."""
    session = get_object_or_404(StudySession, pk=pk, user=request.user)
    session.completed_at = None if session.completed_at else timezone.now()
    session.save(update_fields=["completed_at"])
    if request.htmx:
        return render(request, "learning/_session_check.html", {"session": session, "variant": request.POST.get("variant", "")})
    next_url = request.POST.get("next", "")
    return redirect(next_url if next_url.startswith("/") and not next_url.startswith("//") else "dashboard:home")
