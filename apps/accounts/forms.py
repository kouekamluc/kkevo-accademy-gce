from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from apps.academics.models import AcademicLevel, AcademicPathway

from .models import StudentProfile, User

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
    password = forms.CharField(
        label="Password", strip=False, help_text=PASSWORD_HELP,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    class Meta:
        model = User
        fields = ("email",)
        widgets = {"email": forms.EmailInput(attrs={"autocomplete": "email"})}
        labels = {"email": "Email"}

    field_order = ["full_name", "email", "password"]

    def clean_full_name(self):
        name = " ".join(self.cleaned_data["full_name"].split())
        if not name:
            raise forms.ValidationError("Enter your name.")
        return name

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
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
        if commit:
            user.save()
        return user


class EmailAuthenticationForm(StyledFormMixin, AuthenticationForm):
    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "That email and password don’t match. Check them and try again.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Email"
        self.fields["username"].widget = forms.EmailInput(
            attrs={"autocomplete": "email", "autofocus": True, "class": "form-input"}
        )

    def clean(self):
        if self.cleaned_data.get("username"):
            self.cleaned_data["username"] = self.cleaned_data["username"].strip().lower()
        return super().clean()


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
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Another account already uses this email.")
        return email


class StudyPreferencesForm(forms.ModelForm):
    level = LevelForm.base_fields["level"]
    pathway = forms.ModelChoiceField(
        queryset=AcademicPathway.objects.filter(is_active=True), required=False, empty_label="A mix of both"
    )

    class Meta:
        model = StudentProfile
        fields = ("level", "pathway", "daily_goal_minutes", "low_data_mode")
        labels = {"daily_goal_minutes": "Daily learning goal (minutes)"}


class StyledPasswordChangeForm(StyledFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = PASSWORD_HELP
