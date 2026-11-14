"""Students report problems from a lesson; staff see them in the studio."""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson, Module, Topic
from apps.learning.models import LessonFeedback

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="f@example.com", password="pw-Strong-123", first_name="Fay")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


@pytest.fixture
def published(course, lesson):
    lesson.status = "published"
    lesson.save()
    return lesson


def url(course, lesson):
    return reverse("courses:lesson_feedback", args=[course.slug, lesson.pk])


def test_lesson_page_offers_the_form(client, student, course, published):
    client.force_login(student)
    response = client.get(published.get_absolute_url())
    assert b"Found a mistake or something confusing" in response.content
    assert url(course, published).encode() in response.content


def test_student_can_report_a_problem(client, student, course, published):
    client.force_login(student)
    response = client.post(url(course, published), {"kind": "wrong", "message": "  The answer to part b is 12,\n not 10. "})
    assert b"Thank you" in response.content
    item = LessonFeedback.objects.get()
    assert (item.user, item.lesson, item.kind, item.status) == (student, published, "wrong", "new")
    assert item.message == "The answer to part b is 12, not 10."


def test_other_needs_a_message_and_kind_must_be_valid(client, student, course, published):
    client.force_login(student)
    assert b"few words" in client.post(url(course, published), {"kind": "other"}).content
    assert b"Choose what" in client.post(url(course, published), {"kind": "bogus"}).content
    assert LessonFeedback.objects.count() == 0


def test_reports_per_day_are_limited(client, student, course, published):
    client.force_login(student)
    for _ in range(10):
        client.post(url(course, published), {"kind": "unclear"})
    assert b"a lot of reports" in client.post(url(course, published), {"kind": "unclear"}).content
    assert LessonFeedback.objects.count() == 10


def test_must_be_signed_in(client, course, published):
    response = client.post(url(course, published), {"kind": "wrong"})
    assert response.status_code == 302 and LessonFeedback.objects.count() == 0


def make_staff():
    staff = User.objects.create_user(email="s@example.com", password="pw-Strong-123", is_staff=True)
    staff.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return staff


def test_staff_see_reports_and_can_close_them(client, student, course, published):
    item = LessonFeedback.objects.create(user=student, lesson=published, kind="display", message="Broken table")
    client.force_login(make_staff())
    page = client.get(reverse("studio:feedback"))
    assert b"Broken table" in page.content and b"Most reported" in page.content
    client.post(reverse("studio:feedback_status", args=[item.pk]), {"status": "fixed"})
    item.refresh_from_db()
    assert item.status == "fixed" and item.handled_at is not None
    assert b"Broken table" not in client.get(reverse("studio:feedback")).content  # default tab is "New"
    assert b"Broken table" in client.get(reverse("studio:feedback") + "?status=fixed").content


def test_students_cannot_open_the_studio_list(client, student):
    client.force_login(student)
    assert client.get(reverse("studio:feedback")).status_code in (302, 403)
