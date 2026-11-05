"""Feature 9: the video library. An approved video appears in its lesson; anything else stays hidden."""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.exceptions import ValidationError
from django.urls import reverse

from apps.courses.models import LessonBlock, VideoResource, youtube_id

pytestmark = pytest.mark.django_db
User = get_user_model()
YT = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


@pytest.fixture
def student(db):
    return User.objects.create_user(email="stu@example.com", password="pw-Strong-123")


@pytest.fixture
def editor(db):
    user = User.objects.create_user(email="ed@example.com", password="pw-Strong-123", is_staff=True)
    user.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return user


@pytest.fixture
def reviewer(db):
    user = User.objects.create_user(email="rev@example.com", password="pw-Strong-123", is_staff=True)
    user.user_permissions.add(*Permission.objects.filter(codename__in=["change_lesson", "publish_lesson"]))
    return user


@pytest.fixture
def published(lesson):
    lesson.status = "published"
    lesson.save()
    return lesson


def make_video(**kw):
    defaults = dict(title="Factorising quadratics", kind="original", url="https://cdn.example.com/factor.mp4",
                    creator="KKEVO", rights_status="owned", review_status="approved", duration_seconds=465)
    return VideoResource.objects.create(**{**defaults, **kw})


def video_block(lesson, video, **kw):
    return LessonBlock.objects.create(lesson=lesson, order=1, block_type="video", data={"resource": video.pk}, **kw)


def lesson_url(lesson):
    return reverse("courses:lesson", args=[lesson.course.slug, lesson.pk])


@pytest.mark.parametrize("url,expected", [
    (YT, "dQw4w9WgXcQ"),
    ("https://youtu.be/dQw4w9WgXcQ?t=10", "dQw4w9WgXcQ"),
    ("https://m.youtube.com/shorts/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
    ("https://www.youtube.com/watch?v=short", ""),
    ("https://notyoutube.com/watch?v=dQw4w9WgXcQ", ""),
    ("", ""),
])
def test_youtube_id(url, expected):
    assert youtube_id(url) == expected


def test_validation_rules():
    with pytest.raises(ValidationError, match="not a YouTube"):
        VideoResource(title="x", kind="youtube", url="https://cdn.example.com/a.mp4").full_clean()
    with pytest.raises(ValidationError, match="choose YouTube"):
        VideoResource(title="x", kind="other", url=YT).full_clean()
    with pytest.raises(ValidationError, match="Check the rights"):
        VideoResource(title="x", kind="youtube", url=YT, review_status="approved").full_clean()
    with pytest.raises(ValidationError, match="only applies to YouTube"):
        VideoResource(title="x", kind="original", url="https://cdn.example.com/a.mp4", rights_status="embed").full_clean()
    VideoResource(title="x", kind="youtube", url=YT, rights_status="embed", review_status="approved").full_clean()


def test_approved_video_appears_in_its_lesson(client, student, published):
    video_block(published, make_video(transcript="We factorise **x² + 5x + 6**."))
    client.force_login(student)
    html = client.get(lesson_url(published)).content.decode()
    assert 'src="https://cdn.example.com/factor.mp4"' in html
    assert "Factorising quadratics · 07:45" in html  # block title and duration come from the library
    assert "Video by KKEVO" in html


def test_youtube_video_uses_privacy_enhanced_embed(client, student, published):
    video_block(published, make_video(kind="youtube", url=YT, rights_status="embed"))
    client.force_login(student)
    html = client.get(lesson_url(published)).content.decode()
    assert "https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ" in html
    assert "<iframe" in html


@pytest.mark.parametrize("review,rights", [("pending", "owned"), ("rejected", "owned"), ("approved", "unknown")])
def test_unapproved_or_unchecked_video_is_hidden_from_students(client, student, published, review, rights):
    video = make_video(review_status=review, rights_status=rights)
    video_block(published, video)
    client.force_login(student)
    html = client.get(lesson_url(published)).content.decode()
    assert "factor.mp4" not in html
    assert video.title not in html


def test_staff_preview_shows_hidden_video_with_notice(client, editor, published):
    video_block(published, make_video(review_status="pending"))
    client.force_login(editor)
    html = client.get(lesson_url(published)).content.decode()
    assert "factor.mp4" in html
    assert "Hidden from students" in html


def test_missing_library_video_is_dropped(client, student, published):
    video = make_video()
    video_block(published, video)
    video.delete()
    client.force_login(student)
    assert client.get(lesson_url(published)).status_code == 200


def test_editor_can_add_but_not_approve(client, editor, lesson):
    client.force_login(editor)
    assert client.get(reverse("studio:videos")).status_code == 200
    response = client.post(reverse("studio:video_new"), {
        "title": "NotebookLM overview", "kind": "notebooklm", "url": "https://cdn.example.com/nb.mp4",
        "rights_status": "owned", "duration": "7:45", "topics": [lesson.topic.pk]})
    video = VideoResource.objects.get()
    assert response.status_code == 302
    assert (video.review_status, video.duration_seconds, video.added_by) == ("pending", 465, editor)
    assert list(video.topics.all()) == [lesson.topic]
    assert client.post(reverse("studio:video_review", args=[video.pk]), {"status": "approved"}).status_code == 403
    video.refresh_from_db()
    assert video.review_status == "pending"


def test_bad_duration_is_rejected(client, editor):
    client.force_login(editor)
    response = client.post(reverse("studio:video_new"), {
        "title": "x", "kind": "original", "url": "https://cdn.example.com/x.mp4", "rights_status": "owned",
        "duration": "seven minutes"})
    assert response.status_code == 200
    assert "minutes:seconds" in response.content.decode()
    assert not VideoResource.objects.exists()


def test_reviewer_approves_only_when_rights_are_checked(client, reviewer):
    video = make_video(review_status="pending", rights_status="unknown")
    client.force_login(reviewer)
    client.post(reverse("studio:video_review", args=[video.pk]), {"status": "approved"})
    video.refresh_from_db()
    assert video.review_status == "pending"
    video.rights_status = "owned"
    video.save()
    client.post(reverse("studio:video_review", args=[video.pk]), {"status": "approved", "note": "Checked."})
    video.refresh_from_db()
    assert (video.review_status, video.reviewed_by, video.review_note) == ("approved", reviewer, "Checked.")


def test_editing_the_link_of_an_approved_video_sends_it_back_to_review(client, editor):
    video = make_video()
    client.force_login(editor)
    client.post(reverse("studio:video_edit", args=[video.pk]), {
        "title": video.title, "kind": "original", "url": "https://cdn.example.com/other.mp4", "rights_status": "owned"})
    video.refresh_from_db()
    assert video.review_status == "pending"
    # A change that does not touch link, type or rights keeps the approval
    approved = make_video(title="Second")
    client.post(reverse("studio:video_edit", args=[approved.pk]), {
        "title": "Second (renamed)", "kind": "original", "url": approved.url, "rights_status": "owned"})
    approved.refresh_from_db()
    assert approved.review_status == "approved"


def test_video_block_picks_a_library_video_and_checklist_flags_unapproved(client, editor, lesson):
    pending = make_video(review_status="pending")
    block = LessonBlock.objects.create(lesson=lesson, order=1, block_type="video", media_url="https://cdn.example.com/old.mp4")
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[lesson.pk, block.pk]), {"title": "", "resource": str(pending.pk)})
    block.refresh_from_db()
    assert (block.data["resource"], block.media_url) == (pending.pk, "")
    html = client.get(reverse("studio:edit", args=[lesson.pk])).content.decode()
    assert "1 library video(s) not approved" in html
    assert "Hidden from students" in html
    # Switch back to a plain link
    client.post(reverse("studio:block_save", args=[lesson.pk, block.pk]),
                {"resource": "", "media_url": "https://cdn.example.com/new.mp4"})
    block.refresh_from_db()
    assert "resource" not in block.data and block.media_url == "https://cdn.example.com/new.mp4"


def test_only_video_blocks_may_use_library_videos(lesson):
    block = LessonBlock(lesson=lesson, block_type="image", media_url="https://x.example/a.png", alt_text="a",
                        data={"resource": make_video().pk})
    with pytest.raises(ValidationError, match="Only video blocks"):
        block.full_clean()


def test_video_used_in_list(client, editor, lesson):
    video = make_video()
    video_block(lesson, video)
    client.force_login(editor)
    assert lesson.title in client.get(reverse("studio:video_edit", args=[video.pk])).content.decode()


def test_editor_renders_a_youtube_library_video(client, editor, lesson):
    video_block(lesson, make_video(kind="youtube", url=YT, rights_status="embed", review_status="pending"))
    client.force_login(editor)
    response = client.get(reverse("studio:edit", args=[lesson.pk]))
    assert response.status_code == 200
    assert "youtube-nocookie.com/embed/dQw4w9WgXcQ" in response.content.decode()
