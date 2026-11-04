"""Safe editing of published lessons: draft changes, review comments, revisions, audit log."""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse

from apps.courses.models import LessonBlock
from apps.studio.models import LessonDraft, LessonEvent, LessonRevision

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def editor(db):
    user = User.objects.create_user(email="editor@example.com", password="pw-Strong-123", is_staff=True, first_name="Ed")
    user.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return user


@pytest.fixture
def reviewer(db):
    user = User.objects.create_user(email="rev@example.com", password="pw-Strong-123", is_staff=True, first_name="Rita")
    user.user_permissions.add(*Permission.objects.filter(codename__in=["change_lesson", "publish_lesson"]))
    return user


@pytest.fixture
def student(db):
    return User.objects.create_user(email="student@example.com", password="pw-Strong-123", first_name="Sam")


@pytest.fixture
def published(lesson):
    lesson.status = "published"
    lesson.save()
    LessonBlock.objects.bulk_create([
        LessonBlock(lesson=lesson, order=1, block_type="heading", title="Original heading"),
        LessonBlock(lesson=lesson, order=2, block_type="text", body="Original paragraph"),
    ])
    return lesson


def student_html(client, student, lesson):
    client.force_login(student)
    response = client.get(reverse("courses:lesson", args=[lesson.course.slug, lesson.pk]))
    assert response.status_code == 200
    return response.content.decode()


def edit(lesson):
    return reverse("studio:edit", args=[lesson.pk])


def test_editing_published_lesson_creates_draft_students_do_not_see(client, editor, student, published):
    heading, text = published.blocks.all()
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Edited paragraph"})
    client.post(reverse("studio:block_add", args=[published.pk]), {"block_type": "tip"})
    client.post(reverse("studio:block_delete", args=[published.pk, heading.pk]))

    text.refresh_from_db()
    assert text.body == "Original paragraph"  # live row untouched
    assert published.blocks.count() == 2
    draft = LessonDraft.objects.get(lesson=published)
    assert [i["block_type"] for i in draft.blocks] == ["text", "tip"]
    assert draft.blocks[0]["body"] == "Edited paragraph"

    html = student_html(client, student, published)
    assert "Original paragraph" in html and "Original heading" in html and "Edited paragraph" not in html

    client.force_login(editor)
    response = client.get(edit(published))
    assert response.context["draft"] == draft
    marks = {b.block_type: b.change for b in response.context["blocks"]}
    assert marks == {"text": "changed", "tip": "new"} and response.context["removed"] == 1
    assert "Edited paragraph" in response.content.decode()
    assert LessonEvent.objects.filter(lesson=published, action="changes_started").count() == 1


def test_draft_changes_review_cycle_with_comments(client, editor, reviewer, student, published):
    heading, text = published.blocks.all()
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Second version"})
    client.post(reverse("studio:block_move", args=[published.pk, text.pk]), {"direction": "up"})
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "submit", "comment": "Fixed a typo"})
    draft = LessonDraft.objects.get(lesson=published)
    assert draft.status == "review"
    # Editors cannot approve their own changes.
    assert client.post(reverse("studio:changes", args=[published.pk]), {"action": "publish"}).status_code == 403

    client.force_login(reviewer)
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "send_back", "comment": "Please add a worked example."})
    draft.refresh_from_db()
    assert draft.status == "draft"
    client.force_login(editor)
    page = client.get(edit(published)).content.decode()
    assert "Please add a worked example." in page  # review note shown in the editor

    client.force_login(reviewer)
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "publish", "comment": "Looks good"})
    assert not LessonDraft.objects.filter(lesson=published).exists()
    blocks = list(published.blocks.all())
    assert [b.pk for b in blocks] == [text.pk, heading.pk]  # rows updated in place, new order
    assert blocks[0].body == "Second version"
    assert "Second version" in student_html(client, student, published)

    actions = list(LessonEvent.objects.filter(lesson=published).order_by("pk").values_list("action", "comment"))
    assert actions == [("changes_started", ""), ("changes_submitted", "Fixed a typo"),
                       ("changes_sent_back", "Please add a worked example."), ("changes_published", "Looks good")]
    kinds = list(LessonRevision.objects.filter(lesson=published).order_by("number").values_list("kind", flat=True))
    assert kinds == ["submitted", "published"]


def test_discard_changes_keeps_published_version(client, editor, published):
    text = published.blocks.get(block_type="text")
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Throwaway"})
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "discard"})
    assert not LessonDraft.objects.filter(lesson=published).exists()
    text.refresh_from_db()
    assert text.body == "Original paragraph"
    assert client.get(edit(published)).context["draft"] is None


def test_invalid_draft_block_is_rejected(client, editor, published):
    client.force_login(editor)
    client.post(reverse("studio:block_add", args=[published.pk]), {"block_type": "image"})
    draft = LessonDraft.objects.get(lesson=published)
    image_id = draft.blocks[-1]["id"]
    client.post(reverse("studio:block_save", args=[published.pk, image_id]),
                {"media_url": "https://example.com/a.png", "alt_text": ""})
    draft.refresh_from_db()
    assert draft.blocks[-1]["media_url"] == ""  # not saved without alt text
    assert client.post(reverse("studio:block_save", args=[published.pk, 99999]), {"body": "x"}).status_code == 404


def test_unpublished_lesson_is_edited_directly(client, editor, lesson):
    block = LessonBlock.objects.create(lesson=lesson, order=1, block_type="text", body="Draft text")
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[lesson.pk, block.pk]), {"body": "Changed"})
    block.refresh_from_db()
    assert block.body == "Changed" and not LessonDraft.objects.exists()


def test_publishing_lesson_snapshots_and_logs_with_comment(client, editor, reviewer, lesson):
    LessonBlock.objects.create(lesson=lesson, order=1, block_type="text", body="v1")
    client.force_login(editor)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "review", "comment": "Ready"})
    client.force_login(reviewer)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "draft", "comment": "Objectives missing"})
    client.force_login(editor)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "review"})
    client.force_login(reviewer)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "published", "comment": "Approved"})
    events = list(LessonEvent.objects.filter(lesson=lesson).order_by("pk").values_list("action", "from_status", "to_status", "comment"))
    assert events == [("submitted", "draft", "review", "Ready"), ("sent_back", "review", "draft", "Objectives missing"),
                      ("submitted", "draft", "review", ""), ("published", "review", "published", "Approved")]
    published = LessonRevision.objects.get(lesson=lesson, kind="published")
    assert published.blocks[0]["body"] == "v1" and published.created_by == reviewer and published.number == 3


def test_unpublishing_folds_draft_into_hidden_blocks(client, editor, reviewer, published):
    text = published.blocks.get(block_type="text")
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Pending edit"})
    client.post(reverse("studio:status", args=[published.pk]), {"status": "draft"})
    published.refresh_from_db()
    text.refresh_from_db()
    assert published.status == "draft" and text.body == "Pending edit"
    assert not LessonDraft.objects.exists()


def test_revision_history_and_restore(client, editor, reviewer, student, published):
    text = published.blocks.get(block_type="text")
    client.force_login(reviewer)
    # Make revision 1 = original, then publish a change as revision 2.
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Original paragraph"})
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "publish"})
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Newer paragraph"})
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "publish"})
    assert published.studio_revisions.count() == 2

    history = client.get(reverse("studio:history", args=[published.pk]))
    assert history.status_code == 200 and len(history.context["revisions"]) == 2
    detail = client.get(reverse("studio:revision", args=[published.pk, 1]))
    assert "Original paragraph" in detail.content.decode()

    client.force_login(editor)
    client.post(reverse("studio:restore", args=[published.pk, 1]))
    draft = LessonDraft.objects.get(lesson=published)
    assert [i["body"] for i in draft.blocks if i["block_type"] == "text"] == ["Original paragraph"]
    assert "Newer paragraph" in student_html(client, student, published)  # restore goes through review
    assert LessonEvent.objects.filter(lesson=published, action="restored").exists()


def test_restore_on_unpublished_lesson_keeps_backup(client, editor, lesson):
    block = LessonBlock.objects.create(lesson=lesson, order=1, block_type="text", body="First")
    client.force_login(editor)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "review"})  # revision 1
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "draft"})
    client.post(reverse("studio:block_save", args=[lesson.pk, block.pk]), {"body": "Second"})
    LessonBlock.objects.create(lesson=lesson, order=2, block_type="text", body="Extra")
    client.post(reverse("studio:restore", args=[lesson.pk, 1]))
    assert list(lesson.blocks.values_list("body", flat=True)) == ["First"]
    backup = LessonRevision.objects.get(lesson=lesson, kind="backup")
    assert [i["body"] for i in backup.blocks] == ["Second", "Extra"]


def test_bulk_actions_are_logged(client, reviewer, lesson):
    client.force_login(reviewer)
    client.post(reverse("studio:bulk"), {"lessons": [lesson.pk], "action": "review"})
    client.post(reverse("studio:bulk"), {"lessons": [lesson.pk], "action": "archive"})
    assert list(LessonEvent.objects.filter(lesson=lesson).order_by("pk").values_list("action", flat=True)) == ["submitted", "archived"]


def test_overview_and_pending_changes_filter(client, editor, reviewer, published, lesson):
    text = published.blocks.get(block_type="text")
    client.force_login(editor)
    client.post(reverse("studio:block_save", args=[published.pk, text.pk]), {"body": "Edit"})
    client.post(reverse("studio:changes", args=[published.pk]), {"action": "submit"})
    response = client.get(reverse("studio:overview"))
    assert response.status_code == 200
    assert [d.lesson for d in response.context["review_changes"]] == [published]
    assert response.context["review_count"] == 1 and response.context["counts"]["published"] == 1
    listing = client.get(reverse("studio:lessons"), {"status": "changes"})
    assert [l.pk for l in listing.context["page"]] == [published.pk]


def test_admin_locks_blocks_of_published_lessons_for_non_superusers(rf, editor, published):
    from django.contrib.admin.sites import site

    from apps.courses.admin import LessonBlockInline
    from apps.courses.models import Lesson

    editor.user_permissions.add(Permission.objects.get(codename="change_lessonblock"))
    request = rf.get("/")
    request.user = User.objects.get(pk=editor.pk)  # fresh permission cache
    inline = LessonBlockInline(Lesson, site)
    assert not inline.has_change_permission(request, published)
    published.status = "draft"
    assert inline.has_change_permission(request, published)
