"""Shared staff-only helpers: access checks, the publish checklist and status changes."""

from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import transaction

from .. import revisions
from ..models import LessonDraft, LessonEvent, LessonRevision
from apps.courses.models import BlockType, Lesson, VideoResource
from apps.practice.models import Question


PER_PAGE = 20


MEDIA_PER_PAGE = 24


PALETTE = [  # (block_type, label, icon)
    ("text", "Text", "menu"), ("heading", "Heading", "type"), ("formula", "Formula", "sigma"),
    ("image", "Diagram", "diagram"), ("video", "Video", "video"), ("quiz", "Quiz", "target"),
    ("definition", "Information Box", "info"), ("worked_example", "Worked example", "list"),
    ("tip", "Tip", "lightbulb"), ("mistake", "Common mistake", "warning"),
    ("practice", "Practice question", "message"), ("summary", "Summary", "check"),
    ("code", "Code", "code"),
]


NEW_BLOCK_DEFAULTS = {
    "text": {"body": "New paragraph."}, "heading": {"title": "New section"},
    "formula": {"body": "x^2 + 2x + 1 = 0"}, "definition": {"title": "Definition", "body": "Explain the term here."},
    "tip": {"title": "Tip", "body": "Write a helpful tip."}, "mistake": {"title": "Common mistake", "body": "Describe the mistake."},
    "practice": {"body": "Write the question.", "data": {"answer": "Write the answer."}},
    "summary": {"body": "First key point\nSecond key point"},
    "worked_example": {"title": "Worked example", "body": "", "data": {"steps": [{"title": "First step"}]}},
    "quiz": {"title": "Quick check", "body": "Write the question.", "data": {"choices": ["Option A", "Option B"], "correct": 0}},
    "image": {"alt_text": ""}, "video": {"title": "Video", "data": {}},
}


def staff_required(view):
    @login_required
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_staff and request.user.has_perm("courses.change_lesson")):
            raise PermissionDenied
        return view(request, *args, **kwargs)
    return wrapper


def can_publish(user):
    return user.has_perm("courses.publish_lesson")


def checklist(lesson, blocks=None):
    blocks = list(lesson.blocks.all()) if blocks is None else blocks
    questions = Question.objects.filter(practice_set__topic=lesson.topic).count()
    images = [b for b in blocks if b.block_type == BlockType.IMAGE]
    video_ids = {b.data.get("resource") for b in blocks if isinstance(b.data, dict) and b.data.get("resource")}
    hidden_videos = len(video_ids) - VideoResource.objects.visible().filter(pk__in=video_ids).count()
    items = [
        {"ok": bool(lesson.objectives_list), "label": "Learning objectives added"},
        {"ok": any(b.block_type == BlockType.WORKED_EXAMPLE for b in blocks), "label": "At least one worked example"},
        {"ok": questions >= 3, "label": "Practice set has 3+ questions" if questions >= 3 else f"Add a practice set (3+ questions, {questions} so far)"},
        {"ok": all(b.alt_text for b in images), "label": "All diagrams have alt text" if all(b.alt_text for b in images)
         else f"Add alt text to {sum(1 for b in images if not b.alt_text)} diagram(s)"},
    ]
    if video_ids:
        items.append({"ok": not hidden_videos, "label": "All library videos approved" if not hidden_videos
                      else f"{hidden_videos} library video(s) not approved: students will not see them"})
    return items


def _review_count():
    return Lesson.objects.filter(status="review").count() + LessonDraft.objects.filter(status="review").count()


def _context(request, **extra):
    return {"review_count": _review_count(), "can_publish": can_publish(request.user), **extra}


def _plural(n, word):
    return f"{n} {word}{'s' if n != 1 else ''}"


# ------------------------------------------------------------------ workflow
EVENT_FOR_STATUS = {
    "review": LessonEvent.Action.SUBMITTED, "published": LessonEvent.Action.PUBLISHED,
    "draft": LessonEvent.Action.SENT_BACK, "archived": LessonEvent.Action.ARCHIVED,
}


def apply_status(lesson, target, user, comment=""):
    """Change a lesson's status, keeping drafts, snapshots and the audit log consistent."""
    previous = lesson.status
    with transaction.atomic():
        if target == "published" or previous == "published":
            # Publishing applies pending changes; leaving "published" folds them into the hidden live blocks.
            revisions.fold_draft(lesson)
        lesson.status = target
        if target == "published" and lesson.reviewer is None:
            lesson.reviewer = user
        lesson.save()
        revision = None
        if target in ("review", "published"):
            kind = LessonRevision.Kind.PUBLISHED if target == "published" else LessonRevision.Kind.SUBMITTED
            revision = revisions.snapshot(lesson, kind, user, note=comment)
        revisions.log(lesson, user, EVENT_FOR_STATUS[target], comment, previous, target, revision)
