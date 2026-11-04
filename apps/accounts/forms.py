from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

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


class RegistrationForm(StyledFormMixin, UserCreationForm):
    usable_password = None  # Django 5.1+ admin-only option; students always set a password

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"autocomplete": "given-name", "autofocus": True}),
            "last_name": forms.TextInput(attrs={"autocomplete": "family-name"}),
            "email": forms.EmailInput(attrs={"autocomplete": "email"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["password1"].help_text = PASSWORD_HELP
        self.fields["password2"].label = "Confirm password"

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists. Try logging in instead.")
        return email


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


class LevelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class AcademicSelectionForm(forms.ModelForm):
    """Onboarding / settings: which class and pathway the student is in."""

    level = LevelChoiceField(
        queryset=AcademicLevel.objects.filter(is_active=True),
        widget=forms.RadioSelect,
        empty_label=None,
        error_messages={"required": "Choose your class."},
    )
    pathway = forms.ModelChoiceField(
        queryset=AcademicPathway.objects.filter(is_active=True),
        widget=forms.RadioSelect,
        empty_label=None,
        error_messages={"required": "Choose Arts or Science."},
    )

    class Meta:
        model = StudentProfile
        fields = ("level", "pathway")


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
    level = AcademicSelectionForm.base_fields["level"]
    pathway = AcademicSelectionForm.base_fields["pathway"]

    class Meta:
        model = StudentProfile
        fields = ("level", "pathway", "low_data_mode")


class StyledPasswordChangeForm(StyledFormMixin, PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].help_text = PASSWORD_HELP
