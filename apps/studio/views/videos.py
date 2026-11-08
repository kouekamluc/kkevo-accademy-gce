"""The video library (feature 9): rights, review and approval."""

from django import forms
from django.contrib import messages
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from apps.courses.models import Lesson, Topic, VideoResource

from ._common import _context, can_publish, staff_required


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
