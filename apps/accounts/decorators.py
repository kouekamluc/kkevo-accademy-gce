from functools import wraps
from urllib.parse import urlencode

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

from .utils import get_profile


def onboarding_required(view_func):
    """Login required, and the student must have chosen a class and pathway."""

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not get_profile(request.user).is_onboarded:
            url = reverse("accounts:onboarding")
            return redirect(f"{url}?{urlencode({'next': request.get_full_path()})}")
        return view_func(request, *args, **kwargs)

    return wrapper
