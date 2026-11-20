import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse

from apps.courses.models import Lesson, LessonBlock
from apps.courses.review import lesson_flags
from apps.studio.models import LessonEvent, LessonReview

pytestmark = pytest.mark.django_db
User = get_user_model()
FLAGGED = "The VAT rate is 19.25 %. Check the current Finance Law before the exam."


@pytest.fixture
def editor(db):
    user = User.objects.create_user(email="editor@example.com", password="pw-Strong-123", is_staff=True, first_name="Ed")
    user.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return user


@pytest.fixture
def reviewer(db):
    user = User.objects.create_user(email="rev@example.com", password="pw-Strong-123", is_staff=True, first_name="Mbah")
    user.user_permissions.add(*Permission.objects.filter(codename__in=["change_lesson", "publish_lesson"]))
    return user


@pytest.fixture
def flagged_lesson(lesson):
    lesson.status = "published"
    lesson.save()
    LessonBlock.objects.create(lesson=lesson, block_type="text", order=1, body="Taxes pay for public services.")
    LessonBlock.objects.create(lesson=lesson, block_type="text", order=2, body=FLAGGED)
    return lesson


def test_flags_point_at_their_block(flagged_lesson):
    flags = lesson_flags(list(flagged_lesson.blocks.order_by("order")))
    assert [(f["sentence"], f["block"]) for f in flags] == [("Check the current Finance Law before the exam.", 2)]


def test_queue_and_page_are_staff_only(client, flagged_lesson):
    assert client.get(reverse("studio:review")).status_code == 302
    client.force_login(User.objects.create_user(email="s@example.com", password="pw-Strong-123"))
    assert client.get(reverse("studio:review")).status_code == 403
    assert client.get(reverse("studio:review_lesson", args=[flagged_lesson.pk])).status_code == 403


def test_queue_lists_lessons_to_check_with_progress(client, editor, flagged_lesson):
    client.force_login(editor)
    response = client.get(reverse("studio:review"))
    assert response.status_code == 200
    assert response.context["totals"]["total"] == 1 and response.context["totals"]["checked"] == 0
    lesson = response.context["page"][0]
    assert lesson.pk == flagged_lesson.pk and lesson.flag_count == 1
    assert response.context["first_todo"] == flagged_lesson.pk


def test_review_page_shows_the_lesson_and_its_flags(client, editor, flagged_lesson):
    client.force_login(editor)
    page = client.get(reverse("studio:review_lesson", args=[flagged_lesson.pk])).content.decode()
    assert "Taxes pay for public services." in page
    assert "Check the current Finance Law before the exam." in page
    assert 'href="#b2"' in page and 'id="b2"' in page
    assert "Only reviewers with the publish permission" in page  # an editor can tick but not decide


def test_approving_needs_every_flag_ticked_then_records_the_reviewer(client, reviewer, flagged_lesson):
    client.force_login(reviewer)
    decide = reverse("studio:review_decide", args=[flagged_lesson.pk])
    client.post(decide, {"action": "approve"})
    flagged_lesson.refresh_from_db()
    assert flagged_lesson.reviewer is None  # one flag is not ticked yet

    key = lesson_flags(list(flagged_lesson.blocks.order_by("order")))[0]["key"]
    assert client.post(reverse("studio:review_tick", args=[flagged_lesson.pk]), {"key": key, "ticked": "1"}).status_code == 204
    assert client.post(reverse("studio:review_tick", args=[flagged_lesson.pk]), {"key": "nonsense", "ticked": "1"}).status_code == 400
    client.post(decide, {"action": "approve", "note": "Rate confirmed with the 2026 Finance Law."})

    flagged_lesson.refresh_from_db()
    review = LessonReview.objects.get(lesson=flagged_lesson)
    assert flagged_lesson.reviewer == reviewer
    assert review.status == "checked" and review.fingerprint and review.checked_at
    assert LessonEvent.objects.filter(lesson=flagged_lesson, action="checked").exists()  # also protects it from --refresh
    assert flagged_lesson.status == "published"  # the check never changes what students can open

    client.force_login(User.objects.create_user(email="kid@example.com", password="pw-Strong-123"))
    lesson_url = reverse("courses:lesson", args=[flagged_lesson.topic.module.course.slug, flagged_lesson.pk])
    assert "Checked by Mbah" in client.get(lesson_url).content.decode()


def test_editing_after_approval_shows_as_changed(client, reviewer, flagged_lesson):
    LessonBlock.objects.filter(lesson=flagged_lesson, order=2).update(body="Taxes are collected by the state.")
    client.force_login(reviewer)
    client.post(reverse("studio:review_decide", args=[flagged_lesson.pk]), {"action": "approve"})
    assert client.get(reverse("studio:review") + "?state=checked").context["page"][0].changed is False
    LessonBlock.objects.filter(lesson=flagged_lesson, order=2).update(body="Taxes are collected by the government.")
    assert client.get(reverse("studio:review") + "?state=checked").context["page"][0].changed is True


def test_needs_a_fix_requires_a_note_and_clears_the_reviewer(client, reviewer, flagged_lesson):
    Lesson.objects.filter(pk=flagged_lesson.pk).update(reviewer=reviewer)
    client.force_login(reviewer)
    decide = reverse("studio:review_decide", args=[flagged_lesson.pk])
    client.post(decide, {"action": "needs_fix", "note": ""})
    assert not LessonReview.objects.filter(lesson=flagged_lesson, status="needs_fix").exists()
    client.post(decide, {"action": "needs_fix", "note": "Example 2 uses the old VAT rate."})
    flagged_lesson.refresh_from_db()
    assert flagged_lesson.reviewer is None
    assert LessonReview.objects.get(lesson=flagged_lesson).note == "Example 2 uses the old VAT rate."
    queue = client.get(reverse("studio:review") + "?state=needs_fix")
    assert [lesson.pk for lesson in queue.context["page"]] == [flagged_lesson.pk]


def test_only_publishers_can_decide(client, editor, flagged_lesson):
    client.force_login(editor)
    assert client.post(reverse("studio:review_decide", args=[flagged_lesson.pk]), {"action": "approve"}).status_code == 403
