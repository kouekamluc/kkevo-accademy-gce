"""The media library: validated image uploads and the picker used by image blocks."""

from django import forms
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from ..models import MediaAsset
from apps.courses.models import BlockType, Lesson

from ._common import MEDIA_PER_PAGE, _context, staff_required
from .editor import Workspace, _block_url, _validate


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
