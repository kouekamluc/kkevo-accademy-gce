"""Mastery levels, hints, review my mistakes (spaced), numeric answers, timed exam mode, confidence."""

from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils import timezone

from apps.learning.models import Enrollment
from apps.practice.mastery import level_for
from apps.practice.models import (
    Answer, Attempt, Choice, MistakeCard, PracticeSet, Question, ReviewAnswer, ReviewSession, parse_number,
)

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db):
    return User.objects.create_user(email="m@example.com", password="pw-Strong-123", first_name="Mia")


@pytest.fixture
def practice_set(lesson):
    s = PracticeSet.objects.create(topic=lesson.topic, lesson=lesson, title="Set A", status="published")
    for i in range(5):
        q = Question.objects.create(practice_set=s, prompt=f"Question {i}?", order=i, hint=f"Think about step {i}.",
                                    solution_steps=[{"title": "Step", "math": "x = 1", "final": True}])
        Choice.objects.create(question=q, text="Right", is_correct=True, order=0)
        Choice.objects.create(question=q, text="Wrong", is_correct=False, order=1, why_wrong="Sign error.")
    return s


@pytest.fixture
def numeric_set(lesson):
    s = PracticeSet.objects.create(topic=lesson.topic, title="Numbers", status="published", order=2)
    Question.objects.create(practice_set=s, kind="numeric", prompt="Force?", numeric_answer=3600, tolerance=5, unit="N", order=0)
    Question.objects.create(practice_set=s, kind="numeric", prompt="Acceleration?", numeric_answer=1.5, tolerance=0.05,
                            unit="m/s²", order=1)
    return s


def q_url(attempt, n):
    return reverse("practice:question", args=[attempt.pk, n])


def pick(practice_set, number, correct=True):
    q = practice_set.questions.order_by("order")[number - 1]
    return q.choices.get(is_correct=correct).pk


def run_set(client, user, practice_set, right):
    """Complete a set with the first `right` questions correct."""
    client.post(reverse("practice:start", args=[practice_set.pk]), {"restart": "1"})
    attempt = Attempt.objects.filter(user=user, completed_at__isnull=True).get()
    for n in range(1, practice_set.questions.count() + 1):
        client.post(q_url(attempt, n), {"choice": pick(practice_set, n, n <= right)})
    client.get(reverse("practice:finish", args=[attempt.pk]))
    return attempt


# ---------------------------------------------------------------- mastery

@pytest.mark.parametrize("entry, key", [
    (None, "not_started"),
    ({"latest": 40, "mastered_runs": 0}, "attempted"),
    ({"latest": 60, "mastered_runs": 0}, "familiar"),
    ({"latest": 80, "mastered_runs": 1}, "proficient"),
    ({"latest": 100, "mastered_runs": 2}, "mastered"),
    ({"latest": 60, "mastered_runs": 2}, "familiar"),  # slipped back: level follows the latest score
])
def test_mastery_levels(entry, key):
    assert level_for(entry).key == key


def test_mastery_on_index_start_and_results(client, student, practice_set, offering):
    Enrollment.objects.create(user=student, offering=offering)
    client.force_login(student)
    assert "Not started" in client.get(reverse("practice:index")).content.decode()

    attempt = run_set(client, student, practice_set, right=3)  # 60%
    results = client.get(reverse("practice:finish", args=[attempt.pk])).content.decode()
    assert "Familiar" in results and "Score 80% or more to reach Proficient." in results

    run_set(client, student, practice_set, right=4)  # 80% once
    assert "Proficient" in client.get(reverse("practice:set", args=[practice_set.pk])).content.decode()
    run_set(client, student, practice_set, right=5)  # 80%+ twice
    page = client.get(reverse("practice:index")).content.decode()
    assert "Mastered" in page and "<strong class=\"text-ink-heading\">1</strong> mastered" in page


# ---------------------------------------------------------------- hints

def test_hint_is_revealed_and_recorded(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    page = client.get(q_url(attempt, 1)).content.decode()
    assert "Show a hint" in page and "Think about step 0." not in page

    response = client.post(q_url(attempt, 1), {"hint": "1"})
    assert response.url == q_url(attempt, 1) + "#hint"
    assert not Answer.objects.exists()
    page = client.get(q_url(attempt, 1)).content.decode()
    assert "Think about step 0." in page and "Show a hint" not in page

    client.post(q_url(attempt, 1), {"choice": pick(practice_set, 1)})
    client.post(q_url(attempt, 2), {"choice": pick(practice_set, 2)})
    assert Answer.objects.get(question__order=0).used_hint is True
    assert Answer.objects.get(question__order=1).used_hint is False
    assert "Hint used" in client.get(q_url(attempt, 1)).content.decode()


def test_hint_after_answering_is_ignored(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    client.post(q_url(attempt, 1), {"choice": pick(practice_set, 1)})
    client.post(q_url(attempt, 1), {"hint": "1"})
    attempt.refresh_from_db()
    assert attempt.hints_used == []


# ---------------------------------------------------------------- review my mistakes

def test_wrong_answers_and_lucky_guesses_become_cards(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]))
    attempt = Attempt.objects.get(user=student)
    client.post(q_url(attempt, 1), {"choice": pick(practice_set, 1, False)})
    client.post(q_url(attempt, 2), {"choice": pick(practice_set, 2, True), "confidence": "guess"})
    client.post(q_url(attempt, 3), {"choice": pick(practice_set, 3, True), "confidence": "sure"})
    assert Answer.objects.get(question__order=1).confidence == "guess"
    tomorrow = timezone.localdate() + timedelta(days=1)
    assert set(MistakeCard.objects.values_list("question__order", "due_on")) == {(0, tomorrow), (1, tomorrow)}
    assert "comes back in Review my mistakes tomorrow" in client.get(q_url(attempt, 1)).content.decode()
    assert "good instinct" in client.get(q_url(attempt, 2)).content.decode()

    # Not due yet: nothing to start
    assert "Nothing due today" in client.get(reverse("practice:review")).content.decode()
    response = client.post(reverse("practice:review_start"))
    assert response.url == reverse("practice:review") and not ReviewSession.objects.exists()


def make_due(user, practice_set, orders):
    for order in orders:
        MistakeCard.record_miss(user, practice_set.questions.get(order=order))
    MistakeCard.objects.update(due_on=timezone.localdate())


def test_review_session_spaces_cards(client, student, practice_set, offering):
    Enrollment.objects.create(user=student, offering=offering)
    make_due(student, practice_set, [0, 1, 2])
    client.force_login(student)
    index = client.get(reverse("practice:index")).content.decode()
    assert "Review my mistakes" in index and "3 questions you missed are due today" in index

    response = client.post(reverse("practice:review_start"))
    session = ReviewSession.objects.get(user=student)
    assert response.url == reverse("practice:review_question", args=[session.pk, 1])
    assert len(session.question_ids) == 3

    url = lambda n: reverse("practice:review_question", args=[session.pk, n])  # noqa: E731
    first, second, third = (Question.objects.get(pk=i) for i in session.question_ids)
    client.post(url(1), {"choice": first.choices.get(is_correct=True).pk})
    client.post(url(2), {"choice": second.choices.get(is_correct=False).pk})
    client.post(url(3), {"hint": "1"})
    client.post(url(3), {"choice": third.choices.get(is_correct=True).pk})
    assert "Comes back in 3 days." in client.get(url(1)).content.decode()

    today = timezone.localdate()
    cards = {c.question_id: c for c in MistakeCard.objects.all()}
    assert (cards[first.pk].step, cards[first.pk].due_on) == (1, today + timedelta(days=3))
    assert (cards[second.pk].step, cards[second.pk].due_on) == (0, today + timedelta(days=1))
    assert (cards[third.pk].step, cards[third.pk].due_on) == (0, today + timedelta(days=1))  # hinted: same gap again
    assert ReviewAnswer.objects.get(question=third).used_hint is True
    # Practice-attempt analytics are untouched by reviews
    assert not Answer.objects.exists()

    results = client.get(reverse("practice:review_finish", args=[session.pk])).content.decode()
    assert "2 of 3" in results
    session.refresh_from_db()
    assert session.completed_at is not None


def test_card_retires_after_three_spaced_successes(student, practice_set):
    card = MistakeCard.record_miss(student, practice_set.questions.first())
    today = timezone.localdate()
    card.record_review(True)
    assert card.due_on == today + timedelta(days=3)
    card.record_review(True)
    assert card.due_on == today + timedelta(days=7)
    card.record_review(True)
    assert card.retired_at is not None
    MistakeCard.record_miss(student, practice_set.questions.first())  # missed again later: back in rotation
    card.refresh_from_db()
    assert card.retired_at is None and card.step == 0


def test_old_wrong_answers_are_picked_up(client, student, practice_set):
    attempt = Attempt.objects.create(user=student, practice_set=practice_set, total=5)
    q = practice_set.questions.first()
    Answer.objects.create(attempt=attempt, question=q, choice=q.choices.get(is_correct=False), is_correct=False)
    Answer.objects.filter(attempt=attempt).update(answered_at=timezone.now() - timedelta(days=5))
    client.force_login(student)
    assert "1 question" in client.get(reverse("practice:review")).content.decode()
    assert MistakeCard.objects.get().due_on <= timezone.localdate()


def test_review_sessions_are_private(client, student, practice_set):
    other = User.objects.create_user(email="o@example.com", password="pw-Strong-123")
    session = ReviewSession.objects.create(user=other, question_ids=[practice_set.questions.first().pk])
    client.force_login(student)
    assert client.get(reverse("practice:review_question", args=[session.pk, 1])).status_code == 404
    assert client.get(reverse("practice:review_finish", args=[session.pk])).status_code == 404


# ---------------------------------------------------------------- numeric answers

@pytest.mark.parametrize("text, value", [
    ("3600", 3600), ("3 600", 3600), ("3,6", 3.6), ("1.5", 1.5), ("−2", -2), ("1e3", 1000), ("abc", None), ("", None),
    ("inf", None),
])
def test_parse_number(text, value):
    assert parse_number(text) == value


def test_numeric_question_flow(client, student, numeric_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[numeric_set.pk]))
    attempt = Attempt.objects.get(user=student)
    assert 'inputmode="decimal"' in client.get(q_url(attempt, 1)).content.decode()

    response = client.post(q_url(attempt, 1), {"value": "lots"}, follow=True)
    assert "Type your answer as a number" in response.content.decode() and not Answer.objects.exists()

    client.post(q_url(attempt, 1), {"value": "3 597"})  # within tolerance of 5
    client.post(q_url(attempt, 2), {"value": "1,6"})  # outside tolerance of 0.05
    a1, a2 = Answer.objects.order_by("question__order")
    assert (a1.is_correct, a1.numeric_value, a1.choice) == (True, 3597, None)
    assert a2.is_correct is False
    page = client.get(q_url(attempt, 2)).content.decode()
    assert "Correct answer" in page and "1.5 m/s²" in page
    results = client.get(reverse("practice:finish", args=[attempt.pk])).content.decode()
    assert "1 of 2" in results and "3597 N" in results


def test_numeric_question_needs_an_answer(numeric_set):
    q = Question(practice_set=numeric_set, kind="numeric", prompt="?")
    with pytest.raises(ValidationError):
        q.clean()


# ---------------------------------------------------------------- timed exam mode

def test_exam_hides_feedback_until_finished(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]), {"mode": "exam"})
    attempt = Attempt.objects.get(user=student)
    assert attempt.is_exam and attempt.time_limit_seconds == 5 * 90  # 90 s a question

    page = client.get(q_url(attempt, 1)).content.decode()
    assert "Show a hint" not in page and "Save answer" in page and 'role="timer"' in page
    response = client.post(q_url(attempt, 1), {"choice": pick(practice_set, 1, False)})
    assert response.url == q_url(attempt, 2)  # straight on, no feedback
    page = client.get(q_url(attempt, 1)).content.decode()
    assert "Not quite" not in page and "Sign error." not in page and "Your answer" in page
    assert "4 questions not answered yet" in page

    # Hand in early: unanswered questions count as wrong
    response = client.post(reverse("practice:finish", args=[attempt.pk]))
    assert response.url == reverse("practice:finish", args=[attempt.pk])
    attempt.refresh_from_db()
    assert attempt.completed_at and (attempt.correct_count, attempt.total) == (0, 5)
    results = client.get(response.url).content.decode()
    assert "Not answered" in results and "0 of 5" in results
    assert "Not quite" in client.get(q_url(attempt, 1)).content.decode()  # feedback now visible


def test_exam_time_runs_out(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]), {"mode": "exam"})
    attempt = Attempt.objects.get(user=student)
    client.post(q_url(attempt, 1), {"choice": pick(practice_set, 1)})
    Attempt.objects.filter(pk=attempt.pk).update(started_at=timezone.now() - timedelta(minutes=10))

    response = client.post(q_url(attempt, 2), {"choice": pick(practice_set, 2)})
    assert response.url == reverse("practice:finish", args=[attempt.pk])
    assert Answer.objects.count() == 1  # late answer not accepted
    assert client.get(q_url(attempt, 3)).url == reverse("practice:finish", args=[attempt.pk])
    client.get(reverse("practice:finish", args=[attempt.pk]))
    attempt.refresh_from_db()
    assert attempt.completed_at and attempt.correct_count == 1


def test_practice_and_exam_attempts_are_separate(client, student, practice_set):
    client.force_login(student)
    client.post(reverse("practice:start", args=[practice_set.pk]))
    client.post(reverse("practice:start", args=[practice_set.pk]), {"mode": "exam"})
    assert set(Attempt.objects.values_list("mode", flat=True)) == {"practice", "exam"}
    page = client.get(reverse("practice:set", args=[practice_set.pk])).content.decode()
    assert "Resume practice" in page and "Resume exam" in page
