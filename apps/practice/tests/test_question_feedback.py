"""Students report a problem with a practice question; the report lands in the studio inbox."""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse

from apps.learning.models import LessonFeedback
from apps.practice.models import Attempt, Choice, PracticeSet, Question

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db):
    return User.objects.create_user(email="q@example.com", password="pw-Strong-123", first_name="Quinn")


@pytest.fixture
def question(lesson):
    s = PracticeSet.objects.create(topic=lesson.topic, lesson=lesson, title="Set Q", status="published")
    q = Question.objects.create(practice_set=s, prompt="What is 2 + 2?", order=0)
    Choice.objects.create(question=q, text="4", is_correct=True, order=0)
    Choice.objects.create(question=q, text="5", is_correct=False, order=1, why_wrong="Off by one.")
    return q


def url(q):
    return reverse("practice:question_feedback", args=[q.pk])


def answered(client, student, question):
    client.force_login(student)
    client.post(reverse("practice:start", args=[question.practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    client.post(reverse("practice:question", args=[attempt.pk, 1]), {"choice": question.choices.get(is_correct=False).pk})
    return attempt


def test_report_link_appears_only_after_answering(client, student, question):
    client.force_login(student)
    client.post(reverse("practice:start", args=[question.practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    page = reverse("practice:question", args=[attempt.pk, 1])
    assert b"Think this question or answer is wrong" not in client.get(page).content
    client.post(page, {"choice": question.choices.first().pk})
    assert url(question).encode() in client.get(page).content


def test_student_can_report_a_question(client, student, question):
    answered(client, student, question)
    response = client.post(url(question), {"kind": "wrong", "message": "I think 4 is not right"})
    assert b"Thank you" in response.content
    item = LessonFeedback.objects.get()
    assert (item.user, item.question, item.lesson, item.kind) == (student, question, None, "wrong")


def test_cannot_report_a_question_never_seen(client, student, question):
    client.force_login(student)
    assert client.post(url(question), {"kind": "wrong"}).status_code == 404
    assert LessonFeedback.objects.count() == 0


def test_validation_messages(client, student, question):
    answered(client, student, question)
    assert b"few words" in client.post(url(question), {"kind": "other"}).content
    assert b"Choose what" in client.post(url(question), {"kind": "zzz"}).content
    assert LessonFeedback.objects.count() == 0


def test_staff_inbox_lists_question_reports(client, student, question):
    answered(client, student, question)
    client.post(url(question), {"kind": "unclear", "message": "What does 2 + 2 mean here?"})
    staff = User.objects.create_user(email="st@example.com", password="pw-Strong-123", is_staff=True)
    staff.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    client.force_login(staff)
    page = client.get(reverse("studio:feedback")).content.decode()
    assert "What is 2 + 2?" in page and "What does 2 + 2 mean here?" in page and "Practice set: Set Q" in page


def test_report_must_be_about_exactly_one_thing(question, lesson, student):
    from django.db import IntegrityError, transaction

    with pytest.raises(IntegrityError), transaction.atomic():
        LessonFeedback.objects.create(user=student, kind="wrong")
    with pytest.raises(IntegrityError), transaction.atomic():
        LessonFeedback.objects.create(user=student, kind="wrong", lesson=lesson, question=question)
