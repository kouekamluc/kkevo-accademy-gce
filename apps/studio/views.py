"""Staff content studio (mockup 12): lesson list with review workflow and a block editor.

Access requires staff status plus the `courses.change_lesson` permission. Publishing
and archiving additionally require `courses.publish_lesson` (reviewers / superusers).
"""

from functools import wraps

from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Count, Max, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_POST

from apps.academics.models import AcademicLevel, Subject
from apps.courses.models import BlockType, Lesson, LessonBlock, LessonType, Topic
from apps.practice.models import Question

PER_PAGE = 20
PALETTE = [  # (block_type, label, icon)
    ("text", "Text", "menu"), ("heading", "Heading", "type"), ("formula", "Formula", "sigma"),
    ("image", "Diagram", "diagram"), ("video", "Video", "video"), ("quiz", "Quiz", "target"),
    ("definition", "Information Box", "info"), ("worked_example", "Worked example", "list"),
    ("tip", "Tip", "lightbulb"), ("mistake", "Common mistake", "warning"),
    ("practice", "Practice question", "message"), ("summary", "Summary", "check"),
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
    return [
        {"ok": bool(lesson.objectives_list), "label": "Learning objectives added"},
        {"ok": any(b.block_type == BlockType.WORKED_EXAMPLE for b in blocks), "label": "At least one worked example"},
        {"ok": questions >= 3, "label": "Practice set has 3+ questions" if questions >= 3 else f"Add a practice set (3+ questions, {questions} so far)"},
        {"ok": all(b.alt_text for b in images), "label": "All diagrams have alt text" if all(b.alt_text for b in images)
         else f"Add alt text to {sum(1 for b in images if not b.alt_text)} diagram(s)"},
    ]


def _context(request, **extra):
    return {"review_count": Lesson.objects.filter(status="review").count(), "can_publish": can_publish(request.user), **extra}


# ------------------------------------------------------------------ list
@staff_required
def lessons(request):
    qs = Lesson.objects.select_related("topic__module__course__offering__subject", "topic__module__course__offering__level", "author")
    counts = dict(qs.values_list("status").annotate(n=Count("pk")))
    status = request.GET.get("status", "")
    q = request.GET.get("q", "").strip()
    subject = request.GET.get("subject", "")
    level = request.GET.get("level", "")
    author = request.GET.get("author", "")
    if status in ("draft", "review", "published", "archived"):
        qs = qs.filter(status=status)
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
        n = lessons_qs.filter(status="draft").update(status="review")
        messages.success(request, f"{n} lesson{'s' if n != 1 else ''} submitted for review.")
    elif action == "archive":
        if not can_publish(request.user):
            raise PermissionDenied
        n = lessons_qs.update(status="archived")
        messages.success(request, f"{n} lesson{'s' if n != 1 else ''} archived.")
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
        messages.success(request, "Draft lesson created. Add blocks to build it.")
        return redirect("studio:edit", pk=lesson.pk)
    return render(request, "studio/new.html", _context(request, form=form, studio_active="lessons"))


# ------------------------------------------------------------------ editor
class SettingsForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ("title", "summary", "estimated_minutes", "lesson_type", "objectives", "key_concepts", "reviewer")
        widgets = {"objectives": forms.Textarea(attrs={"rows": 3}), "key_concepts": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["reviewer"].queryset = get_user_model().objects.filter(is_staff=True)
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
    blocks = list(lesson.blocks.all())
    return render(request, "studio/editor.html", _context(
        request, lesson=lesson, blocks=blocks, form=form, palette=PALETTE, checklist=checklist(lesson, blocks),
        studio_active="lessons", selected=request.GET.get("block")))


@staff_required
@require_POST
def block_add(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    block_type = request.POST.get("block_type")
    if block_type not in BlockType.values:
        messages.error(request, "Unknown block type.")
        return redirect("studio:edit", pk=pk)
    defaults = dict(NEW_BLOCK_DEFAULTS.get(block_type, {}))
    order = (lesson.blocks.aggregate(m=Max("order"))["m"] or 0) + 1
    block = LessonBlock.objects.create(lesson=lesson, block_type=block_type, order=order, title=defaults.get("title", ""),
                                       body=defaults.get("body", ""), alt_text=defaults.get("alt_text", ""),
                                       data=defaults.get("data", {}))
    lesson.save(update_fields=["updated_at"])
    return redirect(f"{reverse('studio:edit', args=[pk])}?block={block.pk}#block-{block.pk}")


@staff_required
@require_POST
def block_save(request, pk, block_pk):
    block = get_object_or_404(LessonBlock, pk=block_pk, lesson_id=pk)
    block.title = request.POST.get("title", block.title)[:200]
    block.body = request.POST.get("body", block.body)
    block.media_url = request.POST.get("media_url", block.media_url)[:200]
    block.alt_text = request.POST.get("alt_text", block.alt_text)[:300]
    data = dict(block.data or {})
    if block.block_type == BlockType.QUIZ:
        data["choices"] = [c.strip() for c in request.POST.get("choices", "").splitlines() if c.strip()]
        try:
            data["correct"] = max(0, min(int(request.POST.get("correct", 1)) - 1, len(data["choices"]) - 1))
        except ValueError:
            data["correct"] = 0
        data["explanation"] = request.POST.get("explanation", "")
    elif block.block_type == BlockType.WORKED_EXAMPLE:
        steps = []
        for line in request.POST.get("steps", "").splitlines():
            if line.strip():
                title, _, math = line.partition("|")
                steps.append({"title": title.strip(), **({"math": math.strip()} if math.strip() else {})})
        if steps:
            steps[-1]["final"] = True
        data["steps"] = steps
    elif block.block_type in (BlockType.PRACTICE,):
        data["answer"] = request.POST.get("answer", "")
    elif block.block_type == BlockType.DEFINITION:
        data["formula"] = request.POST.get("formula", "")
    block.data = data
    try:
        block.full_clean()
    except ValidationError as error:
        messages.error(request, "Block not saved: " + "; ".join(m for msgs in error.message_dict.values() for m in msgs))
        return redirect(f"{reverse('studio:edit', args=[pk])}?block={block.pk}#block-{block.pk}")
    block.save()
    block.lesson.save(update_fields=["updated_at"])
    if request.htmx:
        return render(request, "studio/_saved.html", {"block": block})
    return redirect(f"{reverse('studio:edit', args=[pk])}?block={block.pk}#block-{block.pk}")


@staff_required
@require_POST
def block_move(request, pk, block_pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    blocks = list(lesson.blocks.all())
    index = next((i for i, b in enumerate(blocks) if b.pk == block_pk), None)
    if index is None:
        raise PermissionDenied
    target = index - 1 if request.POST.get("direction") == "up" else index + 1
    if 0 <= target < len(blocks):
        blocks[index], blocks[target] = blocks[target], blocks[index]
        with transaction.atomic():
            for i, b in enumerate(blocks, 1):
                if b.order != i:
                    LessonBlock.objects.filter(pk=b.pk).update(order=i)
    return redirect(f"{reverse('studio:edit', args=[pk])}#block-{block_pk}")


@staff_required
@require_POST
def block_delete(request, pk, block_pk):
    get_object_or_404(LessonBlock, pk=block_pk, lesson_id=pk).delete()
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
        lesson.status = target
        if target == "published" and lesson.reviewer is None:
            lesson.reviewer = request.user
    elif target in allowed and lesson.status in allowed[target]:
        lesson.status = target
    else:
        messages.error(request, "That status change is not allowed.")
        return redirect("studio:edit", pk=pk)
    lesson.save()
    messages.success(request, f"Lesson is now “{lesson.get_status_display()}”.")
    return redirect("studio:edit", pk=pk)
