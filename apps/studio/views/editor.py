"""The lesson editor: settings, blocks, status and the draft-changes workspace."""

from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction
from django.db.models import Max, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from .. import revisions
from ..models import LessonDraft, LessonEvent, LessonRevision
from apps.academics.models import CurriculumReference
from apps.courses.models import BlockType, CODE_LANGUAGES, Lesson, LessonBlock, VideoResource, attach_videos

from ._common import NEW_BLOCK_DEFAULTS, PALETTE, _context, apply_status, can_publish, checklist, staff_required


# ------------------------------------------------------------------ editing workspace
class Workspace:
    """The blocks the studio edits: the working copy if there is one, else the live rows.

    Any write to a published lesson first creates the working copy, so students never see it.
    Draft item ids equal the live block pks they were copied from, so editor URLs stay valid.
    """

    def __init__(self, lesson, user):
        self.lesson, self.user = lesson, user
        self.draft = revisions.get_draft(lesson)

    def blocks(self):
        if self.draft:
            return [revisions.to_block(self.lesson, item, i) for i, item in enumerate(self.draft.blocks, 1)]
        return list(LessonBlock.objects.filter(lesson=self.lesson).order_by("order", "pk"))

    def _prepare_write(self):
        if self.draft is None and self.lesson.status == "published":
            self.draft = revisions.start_draft(self.lesson, self.user)

    def _index(self, block_pk):
        index = next((i for i, item in enumerate(self.draft.blocks) if item["id"] == block_pk), None)
        if index is None:
            raise Http404("No such block in the draft.")
        return index

    def get(self, block_pk):
        self._prepare_write()
        if self.draft:
            index = self._index(block_pk)
            return revisions.to_block(self.lesson, self.draft.blocks[index], index + 1)
        return get_object_or_404(LessonBlock, pk=block_pk, lesson=self.lesson)

    def _touch(self):
        if self.draft:
            self.draft.save()
        self.lesson.save(update_fields=["updated_at"])

    def add(self, block_type):
        self._prepare_write()
        d = NEW_BLOCK_DEFAULTS.get(block_type, {})
        values = {"block_type": block_type, "title": d.get("title", ""), "body": d.get("body", ""), "media_url": "",
                  "alt_text": d.get("alt_text", ""), "data": dict(d.get("data", {}))}
        if self.draft:
            pk = self.draft.next_id
            self.draft.next_id += 1
            self.draft.blocks.append({**values, "id": pk, "source": None})
        else:
            order = (self.lesson.blocks.aggregate(m=Max("order"))["m"] or 0) + 1
            pk = LessonBlock.objects.create(lesson=self.lesson, order=order, **values).pk
        self._touch()
        return pk

    def save(self, block):
        if self.draft:
            item = self.draft.blocks[self._index(block.pk)]
            item.update({f: getattr(block, f) for f in revisions.BLOCK_FIELDS})
        else:
            block.save()
        self._touch()

    def move(self, block_pk, direction):
        self._prepare_write()
        items = self.draft.blocks if self.draft else list(self.lesson.blocks.all())
        index = next((i for i, b in enumerate(items) if (b["id"] if self.draft else b.pk) == block_pk), None)
        if index is None:
            raise PermissionDenied
        target = index - 1 if direction == "up" else index + 1
        if not 0 <= target < len(items):
            return
        items[index], items[target] = items[target], items[index]
        if not self.draft:
            with transaction.atomic():
                for i, b in enumerate(items, 1):
                    if b.order != i:
                        LessonBlock.objects.filter(pk=b.pk).update(order=i)
        self._touch()

    def delete(self, block_pk):
        self._prepare_write()
        if self.draft:
            del self.draft.blocks[self._index(block_pk)]
        else:
            get_object_or_404(LessonBlock, pk=block_pk, lesson=self.lesson).delete()
        self._touch()


def _block_url(pk, block_pk):
    return f"{reverse('studio:edit', args=[pk])}?block={block_pk}#block-{block_pk}"


# ------------------------------------------------------------------ editor
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "summary", "estimated_minutes", "lesson_type", "objectives", "key_concepts", "reviewer",
                  "curriculum_references")
        widgets = {"objectives": forms.Textarea(attrs={"rows": 3}), "key_concepts": forms.Textarea(attrs={"rows": 3}),
                   "curriculum_references": forms.CheckboxSelectMultiple(attrs={"class": "h-4 w-4 rounded border-slate-300 text-primary"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reviewer"].queryset = get_user_model().objects.filter(is_staff=True)
        refs = self.fields["curriculum_references"]
        # Only the syllabus items of this lesson's own subject offering (plus any already attached).
        refs.queryset = CurriculumReference.objects.filter(
            Q(syllabus__offering_id=self.instance.topic.module.course.offering_id) | Q(lessons=self.instance)
        ).select_related("syllabus").distinct().order_by("syllabus__version", "order", "code")
        refs.label = "Curriculum references"
        refs.help_text = ""
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "form-input")


@staff_required
def lesson_edit(request, pk):
    lesson = get_object_or_404(Lesson.objects.select_related("topic__module__course__offering__subject",
                                                             "topic__module__course__offering__level"), pk=pk)
    form = SettingsForm(request.POST if request.method == "POST" else None, instance=lesson, prefix="settings")
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Lesson settings saved.")
        return redirect("studio:edit", pk=lesson.pk)
    workspace = Workspace(lesson, request.user)
    blocks = workspace.blocks()
    draft, removed, reordered = workspace.draft, 0, False
    if draft:
        marks, removed, reordered = revisions.changes(draft, lesson)
        for block in blocks:
            block.change = marks.get(block.pk)
    lesson_checklist = checklist(lesson, blocks)
    for block in blocks:  # keep the stored link for the edit form before library videos fill media_url
        block.stored_media_url = block.media_url
    blocks = attach_videos(blocks, show_hidden=True)
    return render(request, "studio/editor.html", _context(
        request, lesson=lesson, blocks=blocks, form=form, palette=PALETTE, code_languages=CODE_LANGUAGES, checklist=lesson_checklist,
        library_videos=VideoResource.objects.only("pk", "title", "review_status", "rights_status"),
        draft=draft, removed=removed, reordered=reordered,
        changed_count=sum(1 for b in blocks if getattr(b, "change", None)),
        events=LessonEvent.objects.filter(lesson=lesson).select_related("actor")[:6],
        revision_count=lesson.studio_revisions.count(),
        studio_active="lessons", selected=request.GET.get("block")))


@staff_required
@require_POST
def block_add(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    block_type = request.POST.get("block_type")
    if block_type not in BlockType.values:
        messages.error(request, "Unknown block type.")
        return redirect("studio:edit", pk=pk)
    return redirect(_block_url(pk, Workspace(lesson, request.user).add(block_type)))


def _apply_post(block, post):
    block.title = post.get("title", block.title)[:200]
    block.body = post.get("body", block.body)
    block.media_url = post.get("media_url", block.media_url)[:200]
    block.alt_text = post.get("alt_text", block.alt_text)[:300]
    data = dict(block.data or {})
    if block.block_type == BlockType.QUIZ:
        data["choices"] = [c.strip() for c in post.get("choices", "").splitlines() if c.strip()]
        try:
            data["correct"] = max(0, min(int(post.get("correct", 1)) - 1, len(data["choices"]) - 1))
        except ValueError:
            data["correct"] = 0
        data["explanation"] = post.get("explanation", "")
        if "hint" in post:
            data["hint"] = post.get("hint", "").strip()
        if "feedback" in post:  # one line per choice, explaining why it is wrong (blank line = none)
            data["feedback"] = [line.strip() for line in post.get("feedback", "").splitlines()][: len(data["choices"])]
    elif block.block_type == BlockType.WORKED_EXAMPLE:
        steps = []
        for line in post.get("steps", "").splitlines():
            if line.strip():
                title, _, math = line.partition("|")
                steps.append({"title": title.strip(), **({"math": math.strip()} if math.strip() else {})})
        if steps:
            steps[-1]["final"] = True
        data["steps"] = steps
    elif block.block_type in (BlockType.PRACTICE,):
        data["answer"] = post.get("answer", "")
    elif block.block_type == BlockType.DEFINITION:
        data["formula"] = post.get("formula", "")
    elif block.block_type == BlockType.CODE:
        data["language"] = post.get("language", data.get("language", "text")).strip().lower()
        data["caption"] = post.get("caption", data.get("caption", "")).strip()
    elif block.block_type == BlockType.VIDEO and "resource" in post:
        choice = post.get("resource", "")
        if choice.isdigit():
            data["resource"] = int(choice)
            block.media_url = ""  # the library video supplies the link
        else:
            data.pop("resource", None)
    block.data = data


def _validate(block, exclude=None):
    try:
        block.full_clean(exclude=exclude, validate_unique=False, validate_constraints=False)
    except ValidationError as error:
        return "; ".join(m for msgs in error.message_dict.values() for m in msgs)
    return ""


@staff_required
@require_POST
def block_save(request, pk, block_pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    workspace = Workspace(lesson, request.user)
    block = workspace.get(block_pk)
    _apply_post(block, request.POST)
    error = _validate(block)
    if error:
        messages.error(request, "Block not saved: " + error)
        return redirect(_block_url(pk, block.pk))
    workspace.save(block)
    if request.htmx:
        return render(request, "studio/_saved.html", {"block": block})
    return redirect(_block_url(pk, block.pk))


@staff_required
@require_POST
def block_move(request, pk, block_pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    Workspace(lesson, request.user).move(block_pk, request.POST.get("direction"))
    return redirect(f"{reverse('studio:edit', args=[pk])}#block-{block_pk}")


@staff_required
@require_POST
def block_delete(request, pk, block_pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    Workspace(lesson, request.user).delete(block_pk)
    messages.success(request, "Block removed.")
    return redirect("studio:edit", pk=pk)


@staff_required
@require_POST
def lesson_status(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    target = request.POST.get("status")
    allowed = {"review": ("draft",), "draft": ("review", "published", "archived")}
    if target in ("published", "archived"):
        if not can_publish(request.user):
            raise PermissionDenied
    elif not (target in allowed and lesson.status in allowed[target]):
        messages.error(request, "That status change is not allowed.")
        return redirect("studio:edit", pk=pk)
    apply_status(lesson, target, request.user, request.POST.get("comment", ""))
    messages.success(request, f"Lesson is now “{lesson.get_status_display()}”.")
    return redirect("studio:edit", pk=pk)


@staff_required
@require_POST
def lesson_changes(request, pk):
    """Workflow for draft changes to a published lesson: submit, publish, send back, discard."""
    lesson = get_object_or_404(Lesson, pk=pk)
    draft = revisions.get_draft(lesson)
    action = request.POST.get("action")
    comment = request.POST.get("comment", "")
    if draft is None:
        messages.error(request, "This lesson has no draft changes.")
        return redirect("studio:edit", pk=pk)
    if action in ("publish", "send_back") and not can_publish(request.user):
        raise PermissionDenied
    Action = LessonEvent.Action
    with transaction.atomic():
        if action == "submit":
            draft.status = LessonDraft.Status.REVIEW
            draft.save()
            revision = revisions.snapshot(lesson, LessonRevision.Kind.SUBMITTED, request.user, items=draft.blocks, note=comment)
            revisions.log(lesson, request.user, Action.CHANGES_SUBMITTED, comment, revision=revision)
            messages.success(request, "Changes submitted for review. Students still see the published version.")
        elif action == "publish":
            revisions.fold_draft(lesson)
            if lesson.reviewer is None:
                lesson.reviewer = request.user
            lesson.save()
            revision = revisions.snapshot(lesson, LessonRevision.Kind.PUBLISHED, request.user, note=comment)
            revisions.log(lesson, request.user, Action.CHANGES_PUBLISHED, comment, revision=revision)
            messages.success(request, "Changes published. Students now see the new version.")
        elif action == "send_back":
            draft.status = LessonDraft.Status.DRAFT
            draft.save()
            revisions.log(lesson, request.user, Action.CHANGES_SENT_BACK, comment)
            messages.success(request, "Changes sent back to the author.")
        elif action == "discard":
            draft.delete()
            revisions.log(lesson, request.user, Action.CHANGES_DISCARDED, comment)
            messages.success(request, "Draft changes discarded. The published version is unchanged.")
        else:
            messages.error(request, "Unknown action.")
    return redirect("studio:edit", pk=pk)
