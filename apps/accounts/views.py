import json

from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import (
    AccountDetailsForm,
    DeleteAccountForm,
    EmailAuthenticationForm,
    RegistrationForm,
    StudyPreferencesForm,
    StyledPasswordChangeForm,
    StyledPasswordResetForm,
    StyledSetPasswordForm,
)
from .privacy import export_user_data
from .ratelimit import login_limiter
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
        return redirect("accounts:onboarding_level")
    from .onboarding import STEPS

    return render(
        request, "onboarding/account.html", {"form": form, "step": 1, "steps": STEPS, "total_steps": len(STEPS)}
    )


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    authentication_form = EmailAuthenticationForm
    redirect_authenticated_user = True

    def get_default_redirect_url(self):
        """Staff go to the content studio; students to their dashboard (an explicit ?next= still wins)."""
        if self.request.user.is_staff:
            return reverse("studio:lessons")
        return super().get_default_redirect_url()

    def form_valid(self, form):
        response = super().form_valid(form)
        if not form.cleaned_data.get("remember_me"):
            self.request.session.set_expiry(0)  # ends when the browser closes
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if form.rate_limited:
            response.status_code = 429
        return response


# ---------- password reset by email ----------

class PasswordResetView(auth_views.PasswordResetView):
    template_name = "accounts/password_reset_form.html"
    email_template_name = "accounts/email/password_reset_email.txt"
    subject_template_name = "accounts/email/password_reset_subject.txt"
    form_class = StyledPasswordResetForm
    success_url = reverse_lazy("accounts:password_reset_done")

    def get_form_kwargs(self):
        return {**super().get_form_kwargs(), "request": self.request}

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if any(e.code == "rate_limited" for e in form.errors.as_data().get("email", [])):
            response.status_code = 429
        return response


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "accounts/password_reset_done.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "accounts/password_reset_confirm.html"
    form_class = StyledSetPasswordForm
    post_reset_login = True
    post_reset_login_backend = "django.contrib.auth.backends.ModelBackend"
    success_url = reverse_lazy("accounts:password_reset_complete")

    def form_valid(self, form):
        login_limiter(self.request, form.user.email).reset()
        return super().form_valid(form)


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "accounts/password_reset_complete.html"


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



# ---------- privacy: download and delete ----------

@login_required
def data_export(request):
    """Everything we store about the student, as a JSON file they can keep."""
    payload = json.dumps(export_user_data(request.user), indent=2, ensure_ascii=False, default=str)
    response = HttpResponse(payload, content_type="application/json; charset=utf-8")
    stamp = timezone.localdate().isoformat()
    response["Content-Disposition"] = f'attachment; filename="gce-academy-my-data-{stamp}.json"'
    response["Cache-Control"] = "no-store"
    return response


@login_required
def delete_account(request):
    user = request.user
    if user.is_staff:
        messages.error(request, "Staff accounts can only be removed by an administrator.")
        return redirect("accounts:profile")
    form = DeleteAccountForm(user, _post_data(request))
    if request.method == "POST" and form.is_valid():
        logout(request)
        user.delete()  # cascades to profile, enrolments, progress, notes, plans and attempts
        return redirect("accounts:account_deleted")
    return render(request, "accounts/delete_account.html", {"form": form, "nav_active": "settings"})
