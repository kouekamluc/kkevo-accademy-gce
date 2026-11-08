"""Lesson revision history and restore."""

from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .. import revisions
from ..models import LessonEvent, LessonRevision
from apps.courses.models import Lesson

from ._common import _context, staff_required


# ------------------------------------------------------------------ history
@staff_required
def lesson_history(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, "studio/history.html", _context(
        request, lesson=lesson, revisions=lesson.studio_revisions.select_related("created_by"),
        events=LessonEvent.objects.filter(lesson=lesson).select_related("actor", "revision"), studio_active="lessons"))


@staff_required
def revision_detail(request, pk, number):
    lesson = get_object_or_404(Lesson, pk=pk)
    revision = get_object_or_404(LessonRevision, lesson=lesson, number=number)
    blocks = [revisions.to_block(lesson, item, i) for i, item in enumerate(revision.blocks, 1)]
    return render(request, "studio/revision.html", _context(
        request, lesson=lesson, revision=revision, blocks=blocks, studio_active="lessons"))


@staff_required
@require_POST
def revision_restore(request, pk, number):
    lesson = get_object_or_404(Lesson, pk=pk)
    revision = get_object_or_404(LessonRevision, lesson=lesson, number=number)
    with transaction.atomic():
        revisions.restore(lesson, revision, request.user)
    if lesson.status == "published":
        messages.success(request, f"Revision {number} restored as draft changes. Publish them to make them live.")
    else:
        messages.success(request, f"Revision {number} restored.")
    return redirect("studio:edit", pk=pk)
