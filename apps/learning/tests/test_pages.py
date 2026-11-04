from datetime import date, timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.learning import analytics
from apps.learning.models import Enrollment, SavedLesson, StudySession
from apps.practice.models import Answer, Attempt, Choice, PracticeSet, Question

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="g@example.com", password="pw-Strong-123", first_name="Gina")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


@pytest.fixture
def weak_topic(student, lesson, offering):
    lesson.status = "published"
    lesson.save()
    Enrollment.objects.create(user=student, offering=offering)
    s = PracticeSet.objects.create(topic=lesson.topic, lesson=lesson, title="Set", status="published")
    q = Question.objects.create(practice_set=s, prompt="Q?")
    right = Choice.objects.create(question=q, text="R", is_correct=True)
    wrong = Choice.objects.create(question=q, text="W", is_correct=False)
    q2 = Question.objects.create(practice_set=s, prompt="Q2?", order=1)
    Choice.objects.create(question=q2, text="R", is_correct=True)
    wrong2 = Choice.objects.create(question=q2, text="W", is_correct=False)
    attempt = Attempt.objects.create(user=student, practice_set=s)
    Answer.objects.create(attempt=attempt, question=q, choice=right, is_correct=True)
    Answer.objects.create(attempt=attempt, question=q2, choice=wrong2, is_correct=False)
    attempt.finish()
    return lesson.topic


def test_term_start():
    assert analytics.term_start(date(2026, 11, 4)) == date(2026, 9, 1)
    assert analytics.term_start(date(2027, 2, 10)) == date(2027, 1, 1)
    assert analytics.term_start(date(2027, 5, 10)) == date(2027, 4, 1)


def test_progress_page_empty_and_with_data(client, student, weak_topic):
    client.force_login(student)
    response = client.get(reverse("learning:progress"), {"range": "7d"})
    ctx, html = response.context, response.content.decode()
    assert ctx["range_key"] == "7d" and ctx["quiz_avg"] == 50
    assert [e["topic"] for e in ctx["needs"]] == [weak_topic]
    assert "Topics needing revision" in html and weak_topic.title in html
    assert ctx["suggestions"][0]["text_before"] == "Re-read"
    assert client.get(reverse("learning:progress"), {"range": "bogus"}).context["range_key"] == "30d"


def test_add_suggestions_creates_sessions(client, student, weak_topic):
    client.force_login(student)
    response = client.post(reverse("learning:add_suggestions"))
    assert response.url == reverse("learning:planner")
    session = StudySession.objects.get(user=student)
    assert session.kind == "revision" and session.topic == weak_topic
    assert timezone.localtime(session.starts_at).date() == timezone.localdate() + timedelta(days=1)


def test_planner_week_and_create_session(client, student, offering, lesson):
    Enrollment.objects.create(user=student, offering=offering)
    lesson.status = "published"
    lesson.save()
    client.force_login(student)
    assert client.get(reverse("learning:planner")).status_code == 200
    tomorrow = timezone.localdate() + timedelta(days=1)
    response = client.post(reverse("learning:session_create"), {
        "title": "Revise algebra", "subject": offering.subject.pk, "lesson": lesson.pk, "kind": "revision",
        "date": tomorrow.isoformat(), "start_time": "17:30", "duration_minutes": 45})
    assert response.status_code == 302
    session = StudySession.objects.get(user=student)
    assert timezone.localtime(session.starts_at).strftime("%H:%M") == "17:30"
    page = client.get(reverse("learning:planner"), {"date": tomorrow.isoformat()}).content.decode()
    assert "Revise algebra" in page
    day = client.get(reverse("learning:planner"), {"view": "day", "date": tomorrow.isoformat()})
    assert len(day.context["columns"]) == 1


def test_planner_rejects_bad_session_and_foreign_lesson(client, student, lesson):
    client.force_login(student)
    client.post(reverse("learning:session_create"), {"title": "", "kind": "study", "date": "2026-01-01",
                                                     "start_time": "10:00", "duration_minutes": 2})
    assert not StudySession.objects.exists()
    # Lesson from a subject the student does not study
    lesson.status = "published"
    lesson.save()
    client.post(reverse("learning:session_create"), {"title": "X", "kind": "study", "lesson": lesson.pk,
                                                     "date": "2026-01-01", "start_time": "10:00", "duration_minutes": 30})
    assert not StudySession.objects.exists()


def test_session_delete_only_own(client, student):
    other = User.objects.create_user(email="z@example.com", password="pw-Strong-123")
    theirs = StudySession.objects.create(user=other, title="T", starts_at=timezone.now())
    client.force_login(student)
    assert client.post(reverse("learning:session_delete", args=[theirs.pk])).status_code == 404
    mine = StudySession.objects.create(user=student, title="M", starts_at=timezone.now())
    client.post(reverse("learning:session_delete", args=[mine.pk]))
    assert not StudySession.objects.filter(pk=mine.pk).exists()


def test_saved_lessons_page(client, student, lesson):
    client.force_login(student)
    assert "No saved lessons yet" in client.get(reverse("learning:saved")).content.decode()
    lesson.status = "published"
    lesson.save()
    SavedLesson.objects.create(user=student, lesson=lesson)
    assert lesson.title in client.get(reverse("learning:saved")).content.decode()


def test_revision_due_spacing():
    today = timezone.localdate()
    entry = {"latest": 30, "last_at": timezone.now() - timedelta(days=3)}
    assert analytics.revision_due(entry, today) == today
    entry = {"latest": 55, "last_at": timezone.now()}
    assert analytics.revision_due(entry, today) == today + timedelta(days=3)
    assert analytics.due_label(today, today) == "Tonight"


def test_progress_requires_onboarding(client):
    user = User.objects.create_user(email="new@example.com", password="pw-Strong-123")
    client.force_login(user)
    assert client.get(reverse("learning:progress")).url.startswith(reverse("accounts:onboarding"))

