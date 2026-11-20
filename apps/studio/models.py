"""Content-studio records: working copies, revision snapshots, audit events and media.

Blocks are stored as JSON lists of dicts with the keys in `apps.studio.revisions.BLOCK_FIELDS`
plus `id` (stable within a draft) and `source` (pk of the live `LessonBlock` it replaces, or None).
"""

import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify

from apps.courses.models import Lesson


class LessonDraft(models.Model):
    """Unpublished working copy of a *published* lesson's blocks.

    Students keep seeing the live `LessonBlock` rows until a reviewer publishes the draft.
    """

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft changes"
        REVIEW = "review", "Changes under review"

    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="studio_draft")
    blocks = models.JSONField(default=list, blank=True)
    next_id = models.PositiveIntegerField(default=1, help_text="Next id for a block added to this draft.")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Draft changes to {self.lesson}"


class LessonRevision(models.Model):
    """Snapshot of all blocks of a lesson at one moment (history + restore)."""

    class Kind(models.TextChoices):
        SUBMITTED = "submitted", "Submitted for review"
        PUBLISHED = "published", "Published"
        BACKUP = "backup", "Saved before restore"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="studio_revisions")
    number = models.PositiveIntegerField()
    kind = models.CharField(max_length=10, choices=Kind.choices)
    blocks = models.JSONField(default=list, blank=True)
    note = models.CharField(max_length=300, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-number"]
        constraints = [models.UniqueConstraint(fields=["lesson", "number"], name="unique_revision_number_per_lesson")]

    def __str__(self):
        return f"{self.lesson} · revision {self.number}"


class LessonEvent(models.Model):
    """Audit log of workflow actions, with the reviewer's comment when given."""

    class Action(models.TextChoices):
        CREATED = "created", "Created the lesson"
        SUBMITTED = "submitted", "Submitted for review"
        PUBLISHED = "published", "Published"
        SENT_BACK = "sent_back", "Sent back to draft"
        ARCHIVED = "archived", "Archived"
        CHANGES_STARTED = "changes_started", "Started draft changes"
        CHANGES_SUBMITTED = "changes_submitted", "Submitted changes for review"
        CHANGES_PUBLISHED = "changes_published", "Published changes"
        CHANGES_SENT_BACK = "changes_sent_back", "Sent changes back"
        CHANGES_DISCARDED = "changes_discarded", "Discarded draft changes"
        RESTORED = "restored", "Restored a revision"
        CHECKED = "checked", "Checked against the syllabus"
        NEEDS_FIX = "needs_fix", "Marked as needing a fix"

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="studio_events")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name="+")
    action = models.CharField(max_length=20, choices=Action.choices)
    from_status = models.CharField(max_length=10, blank=True)
    to_status = models.CharField(max_length=10, blank=True)
    comment = models.TextField(blank=True)
    revision = models.ForeignKey(LessonRevision, on_delete=models.SET_NULL, null=True, blank=True, related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return f"{self.get_action_display()} · {self.lesson}"


class LessonReview(models.Model):
    """A teacher's check of a lesson against the syllabus: which flagged sentences they verified, and the outcome.

    A lesson without a review row has not been looked at. Approving sets `Lesson.reviewer`, which students see
    as "Checked by …". `fingerprint` is the content hash at approval, so later edits show as "changed since checked".
    """

    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress", "Being checked"
        NEEDS_FIX = "needs_fix", "Needs a fix"
        CHECKED = "checked", "Checked"

    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, related_name="review")
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.IN_PROGRESS, db_index=True)
    ticked = models.JSONField(default=list, blank=True, help_text="Keys of the flagged sentences already verified.")
    note = models.TextField(blank=True, help_text="What needs fixing, or anything the next reader should know.")
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="+")
    fingerprint = models.CharField(max_length=40, blank=True)
    checked_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_status_display()} · {self.lesson}"


def media_upload_to(instance, filename):
    stem, ext = os.path.splitext(filename)
    name = (slugify(stem) or "image")[:60]
    return f"studio/media/{name}-{uuid.uuid4().hex[:8]}{ext.lower()}"


class MediaAsset(models.Model):
    """An image uploaded once by staff and reused in lesson image blocks."""

    file = models.FileField(upload_to=media_upload_to)
    title = models.CharField(max_length=200)
    alt_text = models.CharField(max_length=300, help_text="Describe the image for students using screen readers.")
    content_type = models.CharField(max_length=40)
    size = models.PositiveIntegerField(help_text="Bytes.")
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="+")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return self.title

    @property
    def size_label(self):
        return f"{self.size / 1024:.0f} KB" if self.size < 1024 * 1024 else f"{self.size / 1024 / 1024:.1f} MB"
