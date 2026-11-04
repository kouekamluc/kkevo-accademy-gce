from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import F
from django.utils import timezone

from apps.academics.models import Subject, SubjectOffering
from apps.courses.models import Lesson, Topic

USER = settings.AUTH_USER_MODEL


class Enrollment(models.Model):
    """A subject in a student's plan ("In your plan")."""

    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="enrollments")
    offering = models.ForeignKey(SubjectOffering, on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["offering__subject__order", "offering__subject__name"]
        constraints = [models.UniqueConstraint(fields=["user", "offering"], name="unique_enrollment")]

    def __str__(self):
        return f"{self.user} → {self.offering}"


class LessonProgress(models.Model):
    """How far a student is through one lesson."""

    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="lesson_progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="progress_records")
    percent = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    position_label = models.CharField(
        max_length=120, blank=True, help_text="Where the student stopped, e.g. 'Worked example 2'."
    )
    video_position = models.PositiveIntegerField(default=0, help_text="Seconds into the lesson video.")
    position_anchor = models.CharField(
        max_length=60, blank=True, help_text="HTML id of the section in view when the student stopped, e.g. 'block-12'."
    )
    time_spent_seconds = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    last_viewed_at = models.DateTimeField(default=timezone.now, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        verbose_name_plural = "lesson progress"
        ordering = ["-last_viewed_at"]
        constraints = [models.UniqueConstraint(fields=["user", "lesson"], name="unique_lesson_progress")]

    def __str__(self):
        return f"{self.user} · {self.lesson} · {self.percent}%"

    @property
    def is_completed(self):
        return self.completed_at is not None

    def mark_complete(self):
        self.percent = 100
        if self.completed_at is None:
            self.completed_at = timezone.now()


class DailyActivity(models.Model):
    """Seconds of learning per student per day (weekly charts, streaks)."""

    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="daily_activity")
    date = models.DateField(default=timezone.localdate)
    seconds = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "daily activity"
        ordering = ["-date"]
        constraints = [models.UniqueConstraint(fields=["user", "date"], name="unique_daily_activity")]

    @classmethod
    def add(cls, user, seconds, date=None):
        date = date or timezone.localdate()
        row, _ = cls.objects.get_or_create(user=user, date=date)
        cls.objects.filter(pk=row.pk).update(seconds=F("seconds") + max(0, int(seconds)))

    @property
    def minutes(self):
        return round(self.seconds / 60)


class SavedLesson(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="saved_lessons")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="saved_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [models.UniqueConstraint(fields=["user", "lesson"], name="unique_saved_lesson")]


class LessonNote(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="lesson_notes")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="notes")
    video_time = models.PositiveIntegerField(null=True, blank=True, help_text="Seconds into the video, if any.")
    body = models.TextField(max_length=2000)
    section_label = models.CharField(max_length=120, blank=True, help_text="Section being read when the note was taken.")
    section_anchor = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["video_time", "created_at"]


class SessionKind(models.TextChoices):
    STUDY = "study", "Study"
    PRACTICE = "practice", "Practice"
    REVISION = "revision", "Revision"
    PLANNING = "planning", "Planning"


class StudySession(models.Model):
    """A block in the study planner (mockup 11)."""

    user = models.ForeignKey(USER, on_delete=models.CASCADE, related_name="study_sessions")
    title = models.CharField(max_length=120)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    kind = models.CharField(max_length=10, choices=SessionKind.choices, default=SessionKind.STUDY)
    starts_at = models.DateTimeField(db_index=True)
    duration_minutes = models.PositiveSmallIntegerField(
        default=30, validators=[MinValueValidator(5), MaxValueValidator(480)]
    )
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["starts_at"]

    def __str__(self):
        return self.title

    @property
    def ends_at(self):
        return self.starts_at + timedelta(minutes=self.duration_minutes)

    @property
    def is_completed(self):
        return self.completed_at is not None

    def clean(self):
        if self.lesson_id and self.subject_id and self.lesson.course.offering.subject_id != self.subject_id:
            raise ValidationError({"lesson": "This lesson belongs to a different subject."})
