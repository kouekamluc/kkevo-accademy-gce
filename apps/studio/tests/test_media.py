"""Media library: validated uploads, search, inserting into image blocks."""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from apps.courses.models import LessonBlock
from apps.studio.models import LessonDraft, MediaAsset

pytestmark = pytest.mark.django_db
User = get_user_model()
PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 64
JPEG = b"\xff\xd8\xff\xe0" + b"\x00" * 64


@pytest.fixture(autouse=True)
def media_root(settings, tmp_path):
    settings.MEDIA_ROOT = tmp_path
    return tmp_path


@pytest.fixture
def editor(db):
    user = User.objects.create_user(email="editor@example.com", password="pw-Strong-123", is_staff=True)
    user.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return user


def upload(client, name="Diagram.png", content=PNG, alt="A labelled parabola", title=""):
    return client.post(reverse("studio:media"), {"file": SimpleUploadedFile(name, content), "alt_text": alt, "title": title})


def test_media_requires_staff(client, db):
    assert client.get(reverse("studio:media")).status_code == 302
    client.force_login(User.objects.create_user(email="s@example.com", password="pw-Strong-123"))
    assert client.get(reverse("studio:media")).status_code == 403


def test_upload_valid_image(client, editor, media_root):
    client.force_login(editor)
    response = upload(client)
    assert response.status_code == 302
    asset = MediaAsset.objects.get()
    assert asset.title == "Diagram" and asset.alt_text == "A labelled parabola"
    assert asset.content_type == "image/png" and asset.size == len(PNG) and asset.uploaded_by == editor
    assert asset.file.name.startswith("studio/media/diagram-") and asset.file.name.endswith(".png")
    assert (media_root / asset.file.name).exists()


@pytest.mark.parametrize("name,content,alt,error", [
    ("notes.pdf", b"%PDF-1.4", "x", "Upload a PNG, JPEG, GIF or WebP image."),
    ("evil.svg", b"<svg onload=alert(1)>", "x", "Upload a PNG, JPEG, GIF or WebP image."),
    ("fake.png", b"GIF89a" + b"\x00" * 20, "x", "This file is not a valid image of that type."),
    ("photo.jpg", JPEG, "   ", "Alt text is required."),
])
def test_upload_rejects_bad_files(client, editor, name, content, alt, error):
    client.force_login(editor)
    response = upload(client, name=name, content=content, alt=alt)
    assert response.status_code == 200
    assert error in response.content.decode()
    assert not MediaAsset.objects.exists()


def test_upload_size_limit(client, editor, settings):
    settings.STUDIO_MEDIA_MAX_BYTES = 50
    client.force_login(editor)
    response = upload(client)
    assert "The limit is" in response.content.decode() and not MediaAsset.objects.exists()


def test_library_search(client, editor):
    client.force_login(editor)
    upload(client, name="cell.png", alt="Plant cell with labelled nucleus", title="Plant cell")
    upload(client, name="graph.jpg", content=JPEG, alt="Parabola y = x squared", title="Parabola")
    response = client.get(reverse("studio:media"), {"q": "nucleus"})
    assert [a.title for a in response.context["page"]] == ["Plant cell"]
    assert len(client.get(reverse("studio:media")).context["page"]) == 2


def test_insert_library_image_into_block(client, editor, lesson):
    client.force_login(editor)
    upload(client)
    asset = MediaAsset.objects.get()
    block = LessonBlock.objects.create(lesson=lesson, order=1, block_type="image", media_url="https://example.com/old.png", alt_text="Old")
    picker = client.get(reverse("studio:media_picker", args=[lesson.pk, block.pk]), {"q": "parabola"})
    assert asset.title in picker.content.decode()
    client.post(reverse("studio:block_media", args=[lesson.pk, block.pk]), {"asset": asset.pk})
    block.refresh_from_db()
    assert block.media_url == "http://testserver" + asset.file.url and block.alt_text == "A labelled parabola"

    text = LessonBlock.objects.create(lesson=lesson, order=2, block_type="text", body="Hi")
    client.post(reverse("studio:block_media", args=[lesson.pk, text.pk]), {"asset": asset.pk})
    text.refresh_from_db()
    assert text.media_url == ""
    assert client.post(reverse("studio:block_media", args=[lesson.pk, block.pk]), {"asset": "nope"}).status_code == 404


def test_insert_into_published_lesson_goes_to_draft(client, editor, lesson):
    lesson.status = "published"
    lesson.save()
    block = LessonBlock.objects.create(lesson=lesson, order=1, block_type="image", media_url="https://example.com/old.png", alt_text="Old")
    client.force_login(editor)
    upload(client)
    client.post(reverse("studio:block_media", args=[lesson.pk, block.pk]), {"asset": MediaAsset.objects.get().pk})
    block.refresh_from_db()
    assert block.media_url == "https://example.com/old.png"
    assert LessonDraft.objects.get(lesson=lesson).blocks[0]["alt_text"] == "A labelled parabola"
