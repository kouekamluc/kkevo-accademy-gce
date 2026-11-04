from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import (
    AcademicSelectionForm,
    AccountDetailsForm,
    EmailAuthenticationForm,
    RegistrationForm,
    StudyPreferencesForm,
    StyledPasswordChangeForm,
)
from .utils import get_profile


def _post_data(request):
    """Bound data for POST requests (even if empty), None otherwise."""
    return request.POST if request.method == "POST" else None


def _safe_next(request, fallback):
    candidate = request.POST.get("next") or request.GET.get("next")
    if candidate and url_has_allowed_host_and_scheme(
        candidate, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return candidate
    return fallback


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard:home")
    form = RegistrationForm(_post_data(request))
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user, backend="django.contrib.auth.backends.ModelBackend")
        messages.success(request, f"Welcome, {user.first_name}! Tell us which class you are in.")
        return redirect("accounts:onboarding")
    return render(request, "accounts/register.html", {"form": form})


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    authentication_form = EmailAuthenticationForm
    redirect_authenticated_user = True


@login_required
def onboarding(request):
    profile = get_profile(request.user)
    form = AcademicSelectionForm(_post_data(request), instance=profile)
    if request.method == "POST" and form.is_valid():
        profile = form.save(commit=False)
        if profile.onboarded_at is None:
            profile.onboarded_at = timezone.now()
        profile.save()
        messages.success(request, f"You’re all set for {profile.class_label}.")
        return redirect(_safe_next(request, reverse("dashboard:home")))
    return render(
        request,
        "accounts/onboarding.html",
        {"form": form, "next": _safe_next(request, ""), "is_first_time": not profile.is_onboarded},
    )


@login_required
def profile(request):
    user = request.user
    student = get_profile(user)
    details_form = AccountDetailsForm(instance=user, prefix="details")
    study_form = StudyPreferencesForm(instance=student, prefix="study")
    if request.method == "POST":
        section = request.POST.get("section")
        if section == "details":
            details_form = AccountDetailsForm(request.POST, instance=user, prefix="details")
            if details_form.is_valid():
                details_form.save()
                messages.success(request, "Your details have been updated.")
                return redirect("accounts:profile")
        elif section == "study":
            study_form = StudyPreferencesForm(request.POST, instance=student, prefix="study")
            if study_form.is_valid():
                student = study_form.save(commit=False)
                if student.onboarded_at is None:
                    student.onboarded_at = timezone.now()
                student.save()
                messages.success(request, "Your study settings have been updated.")
                return redirect("accounts:profile")
    return render(
        request,
        "accounts/profile.html",
        {"details_form": details_form, "study_form": study_form, "student": student, "nav_active": "settings"},
    )


@login_required
def password_change(request):
    form = StyledPasswordChangeForm(request.user, _post_data(request))
    if request.method == "POST" and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        messages.success(request, "Your password has been changed.")
        return redirect("accounts:profile")
    return render(request, "accounts/password_change.html", {"form": form, "nav_active": "settings"})


@login_required
@require_POST
def toggle_low_data(request):
    student = get_profile(request.user)
    student.low_data_mode = not student.low_data_mode
    student.save(update_fields=["low_data_mode", "updated_at"])
    if request.htmx:
        next_url = _safe_next(request, reverse("dashboard:home"))
        return render(request, "components/low_data_toggle.html", {"student": student, "next_url": next_url})
    return redirect(_safe_next(request, reverse("dashboard:home")))

