import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.learning.models import Enrollment
from apps.practice.models import Answer, Attempt, Choice, PracticeSet, Question

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db):
    return User.objects.create_user(email="p@example.com", password="pw-Strong-123", first_name="Paul")


@pytest.fixture
def practice_set(lesson):
    s = PracticeSet.objects.create(topic=lesson.topic, lesson=lesson, title="Set A", status="published")
    for i in range(3):
        q = Question.objects.create(practice_set=s, prompt=f"Question {i}?", order=i, feedback="Well reasoned.",
                                    solution_steps=[{"title": "Step", "math": "x = 1", "final": True}])
        Choice.objects.create(question=q, text="Right", is_correct=True, order=0)
        Choice.objects.create(question=q, text="Wrong", is_correct=False, order=1, why_wrong="Because sign error.")
    return s


def answer(client, attempt, number, correct=True):
    q = attempt.practice_set.questions.order_by("order")[number - 1]
    choice = q.choices.get(is_correct=correct)
    return client.post(reverse("practice:question", args=[attempt.pk, number]), {"choice": choice.pk})


def test_full_quiz_flow(client, student, practice_set):
    client.force_login(student)
    response = client.post(reverse("practice:start", args=[practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    assert response.url == reverse("practice:question", args=[attempt.pk, 1])
    assert "Check answer" in client.get(response.url).content.decode()

    answer(client, attempt, 1, True)
    page = client.get(reverse("practice:question", args=[attempt.pk, 1])).content.decode()
    assert "Correct — nicely done." in page and "Well reasoned." in page and "Why not" in page

    answer(client, attempt, 2, False)
    page = client.get(reverse("practice:question", args=[attempt.pk, 2])).content.decode()
    assert "Not quite" in page and "Because sign error." in page and "Correct answer" in page

    # Answers cannot be changed once given
    answer(client, attempt, 2, True)
    assert Answer.objects.get(attempt=attempt, question__order=1).is_correct is False

    # Finishing early sends the student back to the first unanswered question
    assert client.get(reverse("practice:finish", args=[attempt.pk])).url == reverse("practice:question", args=[attempt.pk, 3])
    answer(client, attempt, 3, True)
    results = client.get(reverse("practice:finish", args=[attempt.pk]))
    attempt.refresh_from_db()
    assert (attempt.correct_count, attempt.total, attempt.score) == (2, 3, 67)
    assert "2 of 3" in results.content.decode()


def test_resume_and_restart(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    answer(client, attempt, 1)
    assert client.post(reverse("practice:start", args=[practice_set.pk])).url == reverse("practice:question", args=[attempt.pk, 2])
    client.post(reverse("practice:start", args=[practice_set.pk]), {"restart": "1"})
    assert Attempt.objects.filter(user=student).count() == 1
    assert Attempt.objects.get(user=student).answers.count() == 0


def test_attempts_are_private(client, student, practice_set):
    other = User.objects.create_user(email="x@example.com", password="pw-Strong-123")
    attempt = Attempt.objects.create(user=other, practice_set=practice_set, total=3)
    client.force_login(student)
    assert client.get(reverse("practice:question", args=[attempt.pk, 1])).status_code == 404
    assert client.get(reverse("practice:finish", args=[attempt.pk])).status_code == 404


def test_choice_must_belong_to_question(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    other_choice = practice_set.questions.order_by("order")[1].choices.first()
    response = client.post(reverse("practice:question", args=[attempt.pk, 1]), {"choice": other_choice.pk})
    assert response.status_code == 404 and not Answer.objects.exists()


def test_draft_sets_hidden_and_index_lists_plan(client, student, practice_set, offering):
    client.force_login(student)
    assert "No practice sets yet" in client.get(reverse("practice:index")).content.decode()
    Enrollment.objects.create(user=student, offering=offering)
    assert "Set A" in client.get(reverse("practice:index")).content.decode()
    practice_set.status = "draft"
    practice_set.save()
    assert client.get(reverse("practice:set", args=[practice_set.pk])).status_code == 404
