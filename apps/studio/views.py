"""Staff content studio (mockup 12): lesson list with review workflow and a block editor.

Access requires staff status plus the `courses.change_lesson` permission. Publishing
and archiving additionally require `courses.publish_lesson` (reviewers / superusers).

Published lessons are never edited in place: block edits go to a working copy
(`LessonDraft`, see `apps.studio.revisions`) that students don't see until a reviewer
publishes it.
"""

from functools import wraps

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Count, Max, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from apps.academics.models import AcademicLevel, CurriculumReference, Subject
from apps.courses.models import BlockType, CODE_LANGUAGES, Lesson, LessonBlock, LessonType, Topic, VideoResource, attach_videos
from apps.practice.models import Question

from . import revisions
from .models import LessonDraft, LessonEvent, LessonRevision, MediaAsset

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


# ------------------------------------------------------------------ overview
@staff_required
def overview(request):
    counts = dict(Lesson.objects.values_list("status").annotate(n=Count("pk")))
    related = ("topic__module__course__offering__subject", "author")
    review_lessons = Lesson.objects.filter(status="review").select_related(*related).order_by("updated_at")[:10]
    drafts = LessonDraft.objects.select_related("lesson__topic__module__course__offering__subject", "created_by")
    my_drafts = Lesson.objects.filter(author=request.user, status="draft").select_related(*related).order_by("-updated_at")[:8]
    events = LessonEvent.objects.select_related("lesson", "actor")[:12]
    return render(request, "studio/overview.html", _context(
        request, counts=counts, total=sum(counts.values()), review_lessons=review_lessons,
        review_changes=drafts.filter(status="review").order_by("updated_at")[:10],
        draft_changes=drafts.filter(status="draft").order_by("-updated_at")[:10],
        pending_changes=drafts.count(), my_drafts=my_drafts, events=events,
        media_count=MediaAsset.objects.count(), studio_active="overview"))


# ------------------------------------------------------------------ list
@staff_required
def lessons(request):
    qs = Lesson.objects.select_related("topic__module__course__offering__subject", "topic__module__course__offering__level",
                                       "author", "studio_draft")
    counts = dict(qs.values_list("status").annotate(n=Count("pk")))
    status = request.GET.get("status", "")
    q = request.GET.get("q", "").strip()
    subject = request.GET.get("subject", "")
    level = request.GET.get("level", "")
    author = request.GET.get("author", "")
    if status in ("draft", "review", "published", "archived"):
        qs = qs.filter(status=status)
    elif status == "changes":
        qs = qs.filter(studio_draft__isnull=False)
    else:
        qs = qs.exclude(status="archived")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(topic__title__icontains=q))
    if subject.isdigit():
        qs = qs.filter(topic__module__course__offering__subject_id=subject)
    if level.isdigit():
        qs = qs.filter(topic__module__course__offering__level_id=level)
    if author == "me":
        qs = qs.filter(author=request.user)
    elif author.isdigit():
        qs = qs.filter(author_id=author)
    page = Paginator(qs.order_by("-updated_at"), PER_PAGE).get_page(request.GET.get("page"))
    total = sum(n for s, n in counts.items() if s != "archived")
    User = get_user_model()
    return render(request, "studio/lessons.html", _context(
        request, page=page, counts=counts, total=total, status=status, q=q, subject=subject, level=level, author=author,
        changes_count=LessonDraft.objects.count(),
        subjects=Subject.objects.filter(is_active=True), levels=AcademicLevel.objects.filter(is_active=True),
        authors=User.objects.filter(authored_lessons__isnull=False).distinct(),
        subject_count=Subject.objects.filter(offerings__courses__isnull=False).distinct().count(),
        level_count=AcademicLevel.objects.filter(is_active=True).count(),
        query_string=request.GET.urlencode(), studio_active="lessons",
    ))


@staff_required
@require_POST
def bulk(request):
    ids = [int(i) for i in request.POST.getlist("lessons") if i.isdigit()]
    action = request.POST.get("action")
    lessons_qs = Lesson.objects.filter(pk__in=ids)
    if not ids:
        messages.error(request, "Select at least one lesson.")
    elif action == "review":
        selected = list(lessons_qs.filter(status="draft"))
        for lesson in selected:
            apply_status(lesson, "review", request.user)
        messages.success(request, f"{_plural(len(selected), 'lesson')} submitted for review.")
    elif action == "archive":
        if not can_publish(request.user):
            raise PermissionDenied
        selected = list(lessons_qs.exclude(status="archived"))
        for lesson in selected:
            apply_status(lesson, "archived", request.user)
        messages.success(request, f"{_plural(len(selected), 'lesson')} archived.")
    else:
        messages.error(request, "Unknown action.")
    return_to = request.POST.get("return_to", "")
    return redirect(return_to if return_to.startswith("/studio/") else "studio:lessons")


# ------------------------------------------------------------------ create
class NewLessonForm(forms.Form):
    topic = forms.ModelChoiceField(queryset=Topic.objects.select_related("module__course").order_by(
        "module__course__title", "module__order", "order"), widget=forms.Select(attrs={"class": "form-input"}))
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-input"}))
    lesson_type = forms.ChoiceField(choices=LessonType.choices, widget=forms.Select(attrs={"class": "form-input"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topic"].label_from_instance = lambda t: f"{t.module.course.title} › {t.module.title} › {t.title}"


@staff_required
def lesson_new(request):
    form = NewLessonForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        topic = form.cleaned_data["topic"]
        base = slugify(form.cleaned_data["title"])[:180] or "lesson"
        slug, n = base, 2
        while Lesson.objects.filter(topic=topic, slug=slug).exists():
            slug, n = f"{base}-{n}", n + 1
        order = (topic.lessons.aggregate(m=Max("order"))["m"] or 0) + 1
        lesson = Lesson.objects.create(topic=topic, title=form.cleaned_data["title"], slug=slug, order=order,
                                       lesson_type=form.cleaned_data["lesson_type"], author=request.user)
        revisions.log(lesson, request.user, LessonEvent.Action.CREATED, to_status=lesson.status)
        messages.success(request, "Draft lesson created. Add blocks to build it.")
        return redirect("studio:edit", pk=lesson.pk)
    return render(request, "studio/new.html", _context(request, form=form, studio_active="lessons"))


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


# ------------------------------------------------------------------ media library
IMAGE_TYPES = {  # extension → (content type, magic-byte check)
    ".png": ("image/png", lambda h: h.startswith(b"\x89PNG\r\n\x1a\n")),
    ".jpg": ("image/jpeg", lambda h: h.startswith(b"\xff\xd8\xff")),
    ".jpeg": ("image/jpeg", lambda h: h.startswith(b"\xff\xd8\xff")),
    ".gif": ("image/gif", lambda h: h[:6] in (b"GIF87a", b"GIF89a")),
    ".webp": ("image/webp", lambda h: h[:4] == b"RIFF" and h[8:12] == b"WEBP"),
}


def media_max_bytes():
    return getattr(settings, "STUDIO_MEDIA_MAX_BYTES", 2 * 1024 * 1024)


class MediaUploadForm(forms.Form):
    file = forms.FileField(label="Image", help_text="PNG, JPEG, GIF or WebP. Keep it small: students may be on mobile data.",
                           widget=forms.ClearableFileInput(attrs={"accept": ",".join(IMAGE_TYPES)}))
    title = forms.CharField(max_length=200, required=False, help_text="Defaults to the file name.")
    alt_text = forms.CharField(max_length=300, label="Alt text", error_messages={"required": "Alt text is required."},
                               help_text="Describe what the image shows, for students using screen readers.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "form-input")

    def clean_file(self):
        upload = self.cleaned_data["file"]
        ext = ("." + upload.name.rsplit(".", 1)[-1].lower()) if "." in upload.name else ""
        if ext not in IMAGE_TYPES:
            raise ValidationError("Upload a PNG, JPEG, GIF or WebP image.")
        limit = media_max_bytes()
        if upload.size > limit:
            raise ValidationError(f"This image is {upload.size / 1024 / 1024:.1f} MB. The limit is "
                                  f"{limit / 1024 / 1024:.0f} MB: compress or resize it first.")
        upload.seek(0)
        head = upload.read(16)
        upload.seek(0)
        content_type, check = IMAGE_TYPES[ext]
        if not check(head):
            raise ValidationError("This file is not a valid image of that type.")
        upload.studio_content_type = content_type
        return upload

    def clean_alt_text(self):
        alt = self.cleaned_data["alt_text"].strip()
        if not alt:
            raise ValidationError("Alt text is required.")
        return alt


def _media_search(request):
    q = request.GET.get("q", "").strip()
    qs = MediaAsset.objects.select_related("uploaded_by")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(alt_text__icontains=q))
    return q, qs


@staff_required
def media_library(request):
    form = MediaUploadForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        upload = form.cleaned_data["file"]
        title = form.cleaned_data["title"].strip() or upload.name.rsplit(".", 1)[0][:200]
        MediaAsset.objects.create(file=upload, title=title, alt_text=form.cleaned_data["alt_text"],
                                  content_type=upload.studio_content_type, size=upload.size, uploaded_by=request.user)
        messages.success(request, f"“{title}” added to the media library.")
        return redirect("studio:media")
    q, qs = _media_search(request)
    page = Paginator(qs, MEDIA_PER_PAGE).get_page(request.GET.get("page"))
    return render(request, "studio/media.html", _context(
        request, form=form, page=page, q=q, max_mb=media_max_bytes() // (1024 * 1024), studio_active="media"))


@staff_required
def media_picker(request, pk, block_pk):
    """HTMX partial: searchable grid of images to insert into one image block."""
    lesson = get_object_or_404(Lesson, pk=pk)
    q, qs = _media_search(request)
    return render(request, "studio/_media_picker.html", {"lesson": lesson, "block_pk": block_pk, "q": q, "assets": qs[:12]})


@staff_required
@require_POST
def block_media(request, pk, block_pk):
    """Put a library image into an image block (URL + alt text)."""
    lesson = get_object_or_404(Lesson, pk=pk)
    asset_id = request.POST.get("asset", "")
    asset = get_object_or_404(MediaAsset, pk=int(asset_id) if asset_id.isdigit() else 0)
    workspace = Workspace(lesson, request.user)
    block = workspace.get(block_pk)
    if block.block_type != BlockType.IMAGE:
        messages.error(request, "Library images can only go into image blocks.")
        return redirect(_block_url(pk, block.pk))
    block.media_url = request.build_absolute_uri(asset.file.url)[:200]
    block.alt_text = asset.alt_text
    error = _validate(block, exclude=["media_url"])  # URL built by the server from the request host
    if error:
        messages.error(request, "Image not inserted: " + error)
    else:
        workspace.save(block)
        messages.success(request, f"Inserted “{asset.title}”.")
    return redirect(_block_url(pk, block.pk))


# ------------------------------------------------------------------ video library (feature 9)
VIDEOS_PER_PAGE = 20
REVIEW_FIELDS = ("kind", "url", "rights_status")  # editing these sends an approved video back to review


def _parse_duration(value):
    """'7:45', '1:02:03' or '465' -> seconds; '' -> None."""
    value = (value or "").strip()
    if not value:
        return None
    parts = value.split(":")
    if len(parts) > 3 or not all(p.isdigit() for p in parts):
        raise ValidationError("Write the duration as minutes:seconds, e.g. 7:45.")
    seconds = 0
    for part in parts:
        seconds = seconds * 60 + int(part)
    return seconds


class VideoForm(forms.ModelForm):
    duration = forms.CharField(required=False, label="Duration", help_text="minutes:seconds, e.g. 7:45")

    class Meta:
        model = VideoResource
        fields = ["title", "kind", "url", "source", "creator", "rights_status", "licence_note", "topics",
                  "captions_url", "low_data_url", "size_mb", "transcript"]
        widgets = {"transcript": forms.Textarea(attrs={"rows": 5}), "topics": forms.SelectMultiple(attrs={"size": 8})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topics"].queryset = Topic.objects.select_related("module__course").order_by(
            "module__course__title", "module__order", "order")
        self.fields["topics"].label_from_instance = lambda t: f"{t.module.course.title} › {t.module.title} › {t.title}"
        self.fields["topics"].help_text = "Topics this video explains (hold Ctrl to pick several)."
        if self.instance.duration_seconds:
            m, s = divmod(self.instance.duration_seconds, 60)
            self.fields["duration"].initial = f"{m}:{s:02d}"
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "form-input")
        self.fields["transcript"].widget.attrs["class"] = "form-input py-2"

    def clean_duration(self):
        return _parse_duration(self.cleaned_data.get("duration"))

    def save(self, commit=True):
        self.instance.duration_seconds = self.cleaned_data.get("duration")
        return super().save(commit)


def _videos_using(video):
    return (Lesson.objects.filter(blocks__data__resource=video.pk).select_related("topic__module__course")
            .distinct().order_by("title"))


@staff_required
def video_library(request):
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")
    qs = VideoResource.objects.select_related("added_by", "reviewed_by")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(source__icontains=q) | Q(creator__icontains=q))
    if status in VideoResource.Review.values:
        qs = qs.filter(review_status=status)
    counts = dict(VideoResource.objects.values_list("review_status").annotate(n=Count("pk")))
    page = Paginator(qs, VIDEOS_PER_PAGE).get_page(request.GET.get("page"))
    return render(request, "studio/videos.html", _context(
        request, page=page, q=q, status=status, studio_active="videos",
        tabs=[("", "All", sum(counts.values()))] + [(v, label, counts.get(v, 0)) for v, label in VideoResource.Review.choices]))


@staff_required
def video_edit(request, pk=None):
    video = get_object_or_404(VideoResource, pk=pk) if pk else VideoResource(added_by=request.user)
    before = {f: getattr(video, f) for f in REVIEW_FIELDS}
    form = VideoForm(request.POST or None, instance=video)
    if request.method == "POST" and form.is_valid():
        changed = [f for f in REVIEW_FIELDS if getattr(form.instance, f) != before[f]]
        if pk and video.review_status == VideoResource.Review.APPROVED and changed and not can_publish(request.user):
            form.instance.review_status = VideoResource.Review.PENDING
            form.instance.review_note = "Link, type or rights changed: needs a new review."
            messages.warning(request, "The link, type or rights changed, so the video is back in review.")
        form.save()
        messages.success(request, f"“{form.instance.title}” saved.")
        return redirect("studio:video_edit", pk=form.instance.pk)
    return render(request, "studio/video_form.html", _context(
        request, form=form, video=video, studio_active="videos",
        lessons=_videos_using(video) if video.pk else []))


@staff_required
@require_POST
def video_review(request, pk):
    if not can_publish(request.user):
        raise PermissionDenied
    video = get_object_or_404(VideoResource, pk=pk)
    target = request.POST.get("status", "")
    if target not in VideoResource.Review.values:
        messages.error(request, "Unknown review decision.")
        return redirect("studio:video_edit", pk=pk)
    video.set_review(target, request.user, request.POST.get("note", "").strip())
    try:
        video.full_clean()
    except ValidationError as error:
        messages.error(request, "Not changed: " + "; ".join(m for msgs in error.message_dict.values() for m in msgs))
        return redirect("studio:video_edit", pk=pk)
    video.save()
    messages.success(request, f"“{video.title}”: {video.get_review_status_display().lower()}.")
    return redirect("studio:video_edit", pk=pk)
