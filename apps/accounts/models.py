from django.contrib.auth.models import AbstractUser, BaseUserManager
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


class User(AbstractUser):
    """Platform user. Students and staff share this model; staff use `is_staff`."""

    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class Meta:
        ordering = ["email"]

    def __str__(self):
        return self.email

    @property
    def display_name(self):
        return self.get_full_name() or self.email.split("@")[0]

    @property
    def initials(self):
        parts = [p for p in (self.first_name, self.last_name) if p]
        if parts:
            return "".join(p[0] for p in parts).upper()[:2]
        return self.email[:2].upper()


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
    onboarded_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user}"

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
