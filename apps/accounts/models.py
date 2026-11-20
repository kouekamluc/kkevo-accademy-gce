from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserManager(BaseUserManager):
    """Manager for a user model that logs in with an email address."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("An email address is required.")
        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if not extra_fields["is_staff"] or not extra_fields["is_superuser"]:
            raise ValueError("Superuser must have is_staff=True and is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


PHONE_EMAIL_DOMAIN = "phone.kkevo.invalid"  # students who sign up with a phone number get a placeholder address that never receives mail


def normalize_phone(raw):
    """'677 12 34 56', '+237677123456', '00237 6 77...' -> '+237677123456'. Returns None when it is not a Cameroon mobile number."""
    digits = "".join(ch for ch in (raw or "") if ch.isdigit())
    if digits.startswith("00"):
        digits = digits[2:]
    if digits.startswith("237"):
        digits = digits[3:]
    if len(digits) == 9 and digits[0] == "6":
        return "+237" + digits
    return None


class User(AbstractUser):
    """Platform user. Students and staff share this model; staff use `is_staff`."""

    username = None
    email = models.EmailField("email address", unique=True)
    phone = models.CharField(max_length=16, unique=True, null=True, blank=True, help_text="Cameroon mobile number, +2376XXXXXXXX.")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.contact

    @property
    def has_real_email(self):
        return not self.email.endswith("@" + PHONE_EMAIL_DOMAIN)

    @property
    def contact(self):
        """What to show for this person: their email, or their phone number when they signed up without one."""
        return self.email if self.has_real_email else (self.phone or self.email)

    @property
    def display_name(self):
        return self.get_full_name() or self.contact.split("@")[0]

    @property
    def initials(self):
        parts = [p for p in (self.first_name, self.last_name) if p]
        if parts:
            return "".join(p[0] for p in parts).upper()[:2]
        return self.contact.lstrip("+")[:2].upper()


# Avatars: Cameroonian wildlife, shown instead of initials in the header and on the profile.
AVATARS = [
    ("lion", "🦁", "Lion"), ("elephant", "🐘", "Elephant"), ("giraffe", "🦒", "Giraffe"), ("leopard", "🐆", "Leopard"),
    ("eagle", "🦅", "Eagle"), ("tortoise", "🐢", "Tortoise"), ("parrot", "🦜", "Parrot"), ("chimp", "🐒", "Chimpanzee"),
    ("zebra", "🦓", "Zebra"), ("croc", "🐊", "Crocodile"), ("butterfly", "🦋", "Butterfly"), ("star", "🌟", "Star"),
]
AVATAR_CHOICES = [(key, label) for key, _emoji, label in AVATARS]
AVATAR_EMOJI = {key: emoji for key, emoji, _label in AVATARS}


class StudentProfile(models.Model):
    """Learning preferences for a user. Created automatically with every user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    level = models.ForeignKey(
        "academics.AcademicLevel", on_delete=models.SET_NULL, null=True, blank=True, related_name="students"
    )
    pathway = models.ForeignKey(
        "academics.AcademicPathway", on_delete=models.SET_NULL, null=True, blank=True, related_name="students"
    )
    low_data_mode = models.BooleanField(
        default=False, help_text="Load lighter images and lower-quality video."
    )
    daily_goal_minutes = models.PositiveSmallIntegerField(
        default=45, validators=[MinValueValidator(5), MaxValueValidator(480)],
        help_text="Daily learning goal shown on the dashboard chart.",
    )
    exam_date = models.DateField(
        null=True, blank=True,
        help_text="Date of the student's first GCE paper (from their official timetable). Drives the countdown.",
    )
    avatar = models.CharField(max_length=12, blank=True, default="", choices=AVATAR_CHOICES)
    reminders_enabled = models.BooleanField(
        default=True, help_text="Send one short study reminder a day (only on days the student has not studied yet)."
    )
    reminder_hour = models.PositiveSmallIntegerField(
        default=17, validators=[MaxValueValidator(23)], help_text="Hour of the day (Cameroon time) for the reminder."
    )
    last_reminder_on = models.DateField(null=True, blank=True, editable=False)
    onboarded_at = models.DateTimeField(null=True, blank=True)
    terms_accepted_at = models.DateTimeField(
        null=True, blank=True, help_text="When the student accepted the terms and privacy policy at sign-up."
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user}"

    @property
    def avatar_emoji(self):
        return AVATAR_EMOJI.get(self.avatar, "")

    @property
    def is_onboarded(self):
        return self.onboarded_at is not None and self.level_id is not None

    @property
    def class_label(self):
        """'Form 5 · Science' — shown under the student's name."""
        if not self.level_id:
            return ""
        return f"{self.level} · {self.pathway or 'Mixed'}"

    @property
    def stream_label(self):
        return self.pathway.name if self.pathway_id else "A mix"
