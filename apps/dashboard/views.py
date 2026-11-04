from django.shortcuts import render

from apps.accounts.decorators import onboarding_required
from apps.accounts.utils import get_profile


@onboarding_required
def home(request):
    # Full dashboard (enrolments, continue learning) arrives in milestone 4.
    return render(request, "dashboard/home.html", {"student": get_profile(request.user), "nav_active": "dashboard"})
