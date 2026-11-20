from datetime import timedelta

from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils import timezone

from apps.academics.models import AcademicLevel, AcademicPathway

from .models import PHONE_EMAIL_DOMAIN, StudentProfile, User, normalize_phone
from .ratelimit import login_limiter, password_reset_limiter

PHONE_HELP = "Cameroon mobile number, for example 677 12 34 56."


def clean_phone_value(value, instance=None):
    """Normalised, unique phone number, or '' when the field was left empty."""
    if not (value or "").strip():
        return ""
    phone = normalize_phone(value)
    if phone is None:
        raise forms.ValidationError("Enter a Cameroon mobile number, for example 677 12 34 56.")
    clash = User.objects.filter(phone=phone)
    if instance is not None and instance.pk:
        clash = clash.exclude(pk=instance.pk)
    if clash.exists():
        raise forms.ValidationError("An account with this phone number already exists. Try logging in instead.")
    return phone


def placeholder_email(phone):
    return f"{phone.lstrip('+')}@{PHONE_EMAIL_DOMAIN}"


PASSWORD_HELP = "At least 8 characters. Avoid common words, your name, or only numbers."


class StyledFormMixin:
    """Applies the design-system input classes to every widget."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, (forms.CheckboxInput, forms.RadioSelect)):
                continue
            widget.attrs.setdefault("class", "form-input")

    def full_clean(self):
        super().full_clean()
        for name in self.errors:
            if name in self.fields and "form-input" in self.fields[name].widget.attrs.get("class", ""):
                self.fields[name].widget.attrs["class"] = "form-input form-input-error"


class RegistrationForm(StyledFormMixin, forms.ModelForm):
    """Onboarding step 1 (07): full name, email, one password with a strength meter."""

    full_name = forms.CharField(
        label="Full name", max_length=300,
        widget=forms.TextInput(attrs={"autocomplete": "name", "autofocus": True}),
    )
    phone = forms.CharField(
        label="Phone number", required=False, help_text="Fill in your email, your phone number, or both.",
        widget=forms.TextInput(attrs={"autocomplete": "tel", "inputmode": "tel", "placeholder": "6XX XX XX XX"}),
    )
    password = forms.CharField(
        label="Password", strip=False, help_text=PASSWORD_HELP,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    accept_terms = forms.BooleanField(
        required=True, label="I accept the Terms of use and the Privacy policy",
        error_messages={"required": "Please accept the Terms of use and the Privacy policy to create your account."},
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].required = False

    class Meta:
        model = User
        fields = ("email",)
        widgets = {"email": forms.EmailInput(attrs={"autocomplete": "email"})}
        labels = {"email": "Email"}

    field_order = ["full_name", "email", "phone", "password", "accept_terms"]

    def clean_phone(self):
        return clean_phone_value(self.cleaned_data.get("phone"))

    def clean(self):
        cleaned = super().clean()
        if not self.errors.get("email") and not self.errors.get("phone"):
            if not cleaned.get("email") and not cleaned.get("phone"):
                self.add_error("email", "Enter your email, or your phone number if you have no email.")
            elif not cleaned.get("email"):
                cleaned["email"] = placeholder_email(cleaned["phone"])
                self.instance.email = cleaned["email"]
        return cleaned

    def clean_full_name(self):
        name = " ".join(self.cleaned_data["full_name"].split())
        if not name:
            raise forms.ValidationError("Enter your name.")
        return name

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip().lower()
        if email and User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists. Try logging in instead.")
        return email

    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get("password")
        if password:
            first, _, last = self.cleaned_data.get("full_name", "").partition(" ")
            self.instance.first_name, self.instance.last_name = first, last
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password", error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.phone = self.cleaned_data.get("phone") or None
        if commit:
            user.save()
            # Keep the date of consent with the account (the profile is created by a signal on save).
            StudentProfile.objects.filter(user=user).update(terms_accepted_at=timezone.now())
        return user


class EmailAuthenticationForm(StyledFormMixin, AuthenticationForm):
    """Email + password login with per email+IP brute-force protection and "keep me signed in"."""

    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "That email and password don’t match. Check them and try again.",
        "rate_limited": (
            "Too many wrong attempts. For your safety, wait %(minutes)s minute(s) and try again, "
            "or reset your password."
        ),
    }

    remember_me = forms.BooleanField(
        label="Keep me signed in", required=False, initial=True,
        help_text="Untick this on a shared phone or a cyber café computer.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Email or phone number"
        self.fields["username"].widget = forms.TextInput(
            attrs={"autocomplete": "username", "autofocus": True, "class": "form-input"}
        )
        self.fields["password"].widget.attrs["autocomplete"] = "current-password"
        self.rate_limited = False

    def _rate_limit_error(self, limiter):
        self.rate_limited = True
        return forms.ValidationError(
            self.error_messages["rate_limited"], code="rate_limited",
            params={"minutes": limiter.retry_after_minutes()},
        )

    def clean(self):
        email = (self.cleaned_data.get("username") or "").strip().lower()
        if email and "@" not in email:  # a phone number: log in as the account that owns it
            phone = normalize_phone(email)
            owner = User.objects.filter(phone=phone).first() if phone else None
            email = owner.email if owner else (phone or email)
        if email:
            self.cleaned_data["username"] = email
        limiter = login_limiter(self.request, email) if email and self.request is not None else None
        if limiter and limiter.is_blocked():
            raise self._rate_limit_error(limiter)
        try:
            cleaned = super().clean()
        except forms.ValidationError as error:
            if limiter and error.code == "invalid_login":
                limiter.hit()
                if limiter.is_blocked():
                    raise self._rate_limit_error(limiter) from error
                if limiter.remaining <= 2:
                    raise forms.ValidationError(
                        f"{self.error_messages['invalid_login']} "
                        f"{limiter.remaining} attempt(s) left before a short pause.",
                        code="invalid_login",
                    ) from error
            raise
        if limiter:
            limiter.reset()
        return cleaned


class StyledPasswordResetForm(StyledFormMixin, PasswordResetForm):
    """Asks for the account email. Limited per IP so it can't be used to flood inboxes."""

    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.fields["email"].widget.attrs.update({"autofocus": True})

    def get_users(self, email):
        return (user for user in super().get_users(email) if user.has_real_email)

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if self.request is not None:
            limiter = password_reset_limiter(self.request)
            if limiter.is_blocked():
                raise forms.ValidationError(
                    "You’ve asked for several reset links already. Check your inbox and spam folder, "
                    f"or try again in {limiter.retry_after_minutes()} minute(s).",
                    code="rate_limited",
                )
            limiter.hit()
        return email


class StyledSetPasswordForm(StyledFormMixin, SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = PASSWORD_HELP
        self.fields["new_password1"].widget.attrs["autofocus"] = True


class DeleteAccountForm(StyledFormMixin, forms.Form):
    """Asks for the password before permanently deleting an account."""

    password = forms.CharField(
        label="Your password", strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not self.user.check_password(password):
            raise forms.ValidationError("That password isn’t right.")
        return password


MIX = "mix"


class LevelForm(forms.ModelForm):
    """Onboarding step 2."""

    level = forms.ModelChoiceField(
        queryset=AcademicLevel.objects.filter(is_active=True),
        empty_label=None,
        error_messages={"required": "Choose your class.", "invalid_choice": "Choose one of the classes shown."},
    )

    class Meta:
        model = StudentProfile
        fields = ("level",)


class StreamForm(forms.Form):
    """Onboarding step 3: a pathway, or "A mix" (no single pathway)."""

    stream = forms.ChoiceField(error_messages={"required": "Choose Arts, Science or a mix."})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pathways = list(AcademicPathway.objects.filter(is_active=True))
        self.fields["stream"].choices = [(p.slug, p.name) for p in self.pathways] + [(MIX, "A mix")]

    @property
    def selected_pathway(self):
        slug = self.cleaned_data["stream"]
        return next((p for p in self.pathways if p.slug == slug), None)


class SubjectsForm(forms.Form):
    """Onboarding step 4: pick subjects offered for the student's class."""

    MIN_SUBJECTS = 3

    offerings = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def __init__(self, *args, offerings, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["offerings"].queryset = offerings
        self.minimum = min(self.MIN_SUBJECTS, offerings.count())

    def clean_offerings(self):
        chosen = self.cleaned_data["offerings"]
        if len(chosen) < self.minimum:
            raise forms.ValidationError(f"Pick at least {self.minimum} subjects.")
        return chosen


class AccountDetailsForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "phone")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = False
        self.fields["phone"].label = "Phone number"
        self.fields["phone"].help_text = PHONE_HELP
        self.fields["phone"].widget.attrs.update({"autocomplete": "tel", "inputmode": "tel"})
        if not self.instance.has_real_email:
            self.initial["email"] = ""  # do not show the placeholder address

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip().lower()
        if email and User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Another account already uses this email.")
        return email

    def clean_phone(self):
        return clean_phone_value(self.cleaned_data.get("phone"), self.instance)

    def clean(self):
        cleaned = super().clean()
        if not self.errors.get("email") and not self.errors.get("phone") and not cleaned.get("email"):
            if not cleaned.get("phone"):
                self.add_error("email", "Keep at least an email or a phone number so you can sign in.")
            else:
                cleaned["email"] = placeholder_email(cleaned["phone"])
                self.instance.email = cleaned["email"]
        return cleaned

    def save(self, commit=True):
        self.instance.phone = self.cleaned_data.get("phone") or None
        return super().save(commit=commit)


class StudyPreferencesForm(forms.ModelForm):
    level = LevelForm.base_fields["level"]
    pathway = forms.ModelChoiceField(
        queryset=AcademicPathway.objects.filter(is_active=True), required=False, empty_label="A mix of both"
    )
    exam_date = forms.DateField(
        required=False, label="Date of your first GCE paper",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-input"}, format="%Y-%m-%d"),
        help_text="Copy it from the official GCE timetable your school gives you. It powers your countdown.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reminder_hour"].required = False

    class Meta:
        model = StudentProfile
        fields = ("level", "pathway", "daily_goal_minutes", "exam_date", "low_data_mode", "reminders_enabled", "reminder_hour")
        labels = {"daily_goal_minutes": "Daily learning goal (minutes)", "reminders_enabled": "Daily study reminder",
                  "reminder_hour": "Send it at"}
        widgets = {"reminder_hour": forms.Select(choices=[(h, f"{h:02d}:00") for h in range(5, 24)], attrs={"class": "form-input"})}

    def clean_reminder_hour(self):
        value = self.cleaned_data.get("reminder_hour")
        return self.instance.reminder_hour if value is None else value

    def clean_exam_date(self):
        """Same rules as the planner's exam-date box, but an unchanged date is never re-checked
        (an exam date that has passed must not block saving other settings)."""
        value = self.cleaned_data.get("exam_date")
        if value == self.instance.exam_date:
            return value
        today = timezone.localdate()
        if value and value < today:
            raise forms.ValidationError("Choose a date that is still ahead.")
        if value and value > today + timedelta(days=3 * 366):
            raise forms.ValidationError("Choose a date within the next three years.")
        return value


class AvatarForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ("avatar",)


class StyledPasswordChangeForm(StyledFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = PASSWORD_HELP
