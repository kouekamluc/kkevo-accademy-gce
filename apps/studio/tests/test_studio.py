import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse

from apps.courses.models import Lesson, LessonBlock

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def editor(db):
    user = User.objects.create_user(email="editor@example.com", password="pw-Strong-123", is_staff=True, first_name="Ed")
    user.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return user


@pytest.fixture
def reviewer(editor):
    user = User.objects.create_user(email="rev@example.com", password="pw-Strong-123", is_staff=True)
    user.user_permissions.add(*Permission.objects.filter(codename__in=["change_lesson", "publish_lesson"]))
    return user


def test_studio_access_control(client, lesson, editor):
    assert client.get(reverse("studio:lessons")).status_code == 302  # anonymous → login
    student = User.objects.create_user(email="s@example.com", password="pw-Strong-123")
    client.force_login(student)
    assert client.get(reverse("studio:lessons")).status_code == 403
    staff_no_perm = User.objects.create_user(email="n@example.com", password="pw-Strong-123", is_staff=True)
    client.force_login(staff_no_perm)
    assert client.get(reverse("studio:lessons")).status_code == 403
    client.force_login(editor)
    assert lesson.title in client.get(reverse("studio:lessons")).content.decode()


def test_lesson_list_filters_and_counts(client, editor, lesson):
    Lesson.objects.create(topic=lesson.topic, title="Under review one", slug="r1", status="review")
    client.force_login(editor)
    response = client.get(reverse("studio:lessons"), {"status": "review"})
    titles = [item.title for item in response.context["page"]]
    assert titles == ["Under review one"]
    assert response.context["counts"]["review"] == 1
    assert [item.title for item in client.get(reverse("studio:lessons"), {"q": "Lesson A"}).context["page"]] == ["Lesson A"]


def test_create_lesson_then_add_edit_reorder_delete_blocks(client, editor, lesson):
    client.force_login(editor)
    response = client.post(reverse("studio:new"), {"topic": lesson.topic.pk, "title": "Lesson A", "lesson_type": "reading"})
    new = Lesson.objects.get(title="Lesson A", slug="lesson-a-2")
    assert response.url == reverse("studio:edit", args=[new.pk])
    assert new.status == "draft" and new.author == editor

    for kind in ("heading", "formula", "quiz"):
        client.post(reverse("studio:block_add", args=[new.pk]), {"block_type": kind})
    heading, formula, quiz = new.blocks.all()
    client.post(reverse("studio:block_save", args=[new.pk, formula.pk]), {"body": r"(x+3)^2 = 11"})
    client.post(reverse("studio:block_save", args=[new.pk, quiz.pk]),
                {"title": "Quick check", "body": "Pick", "choices": "25\n10\n5", "correct": "1", "explanation": "Half of 10, squared."})
    formula.refresh_from_db()
    quiz.refresh_from_db()
    assert formula.body == "(x+3)^2 = 11"
    assert quiz.data["choices"] == ["25", "10", "5"] and quiz.data["correct"] == 0

    client.post(reverse("studio:block_move", args=[new.pk, quiz.pk]), {"direction": "up"})
    assert [b.block_type for b in new.blocks.all()] == ["heading", "quiz", "formula"]
    client.post(reverse("studio:block_delete", args=[new.pk, heading.pk]))
    assert new.blocks.count() == 2
    assert client.post(reverse("studio:block_add", args=[new.pk]), {"block_type": "nonsense"}).status_code == 302
    assert new.blocks.count() == 2


def test_invalid_block_is_not_saved(client, editor, lesson):
    client.force_login(editor)
    block = LessonBlock.objects.create(lesson=lesson, block_type="image", media_url="https://example.com/a.png", alt_text="A")
    client.post(reverse("studio:block_save", args=[lesson.pk, block.pk]), {"media_url": "https://example.com/a.png", "alt_text": ""})
    block.refresh_from_db()
    assert block.alt_text == "A"


def test_review_workflow_permissions(client, editor, reviewer, lesson):
    client.force_login(editor)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "review"})
    lesson.refresh_from_db()
    assert lesson.status == "review"
    assert client.post(reverse("studio:status", args=[lesson.pk]), {"status": "published"}).status_code == 403
    client.force_login(reviewer)
    client.post(reverse("studio:status", args=[lesson.pk]), {"status": "published"})
    lesson.refresh_from_db()
    assert lesson.status == "published" and lesson.reviewer == reviewer


def test_bulk_actions(client, editor, reviewer, lesson):
    other = Lesson.objects.create(topic=lesson.topic, title="B", slug="b")
    client.force_login(editor)
    client.post(reverse("studio:bulk"), {"lessons": [lesson.pk, other.pk], "action": "review"})
    assert set(Lesson.objects.values_list("status", flat=True)) == {"review"}
    assert client.post(reverse("studio:bulk"), {"lessons": [lesson.pk], "action": "archive"}).status_code == 403
    client.force_login(reviewer)
    response = client.post(reverse("studio:bulk"), {"lessons": [lesson.pk], "action": "archive", "return_to": "https://evil.example/"})
    assert response.url == reverse("studio:lessons")
    lesson.refresh_from_db()
    assert lesson.status == "archived"


def test_checklist_reports_missing_items(client, editor, lesson):
    client.force_login(editor)
    labels = [i["label"] for i in client.get(reverse("studio:edit", args=[lesson.pk])).context["checklist"] if not i["ok"]]
    assert "Learning objectives added" in labels and "At least one worked example" in labels
