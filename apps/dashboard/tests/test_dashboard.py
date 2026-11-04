from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson, Module, Topic
from apps.dashboard.views import learning_streak, weekly_activity
from apps.learning.models import DailyActivity, Enrollment, LessonProgress, StudySession

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="d@example.com", password="pw-Strong-123", first_name="Dina")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


@pytest.fixture
def lessons(course):
    module = Module.objects.create(course=course, title="Algebra", order=1)
    topic = Topic.objects.create(module=module, title="Expressions", order=1)
    return [Lesson.objects.create(topic=topic, title=f"Lesson {i}", slug=f"lesson-{i}", order=i, status="published",
                                  estimated_minutes=20) for i in (1, 2, 3)]


def test_empty_dashboard_shows_helpful_states(client, student):
    client.force_login(student)
    html = client.get(reverse("dashboard:home")).content.decode()
    assert "You haven’t started a lesson yet" in html
    assert "Nothing planned for the next 7 days" in html
    assert "Lessons you complete will appear here" in html
    assert "Dina!" in html


def test_dashboard_uses_real_progress(client, student, offering, lessons):
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=lessons[0], percent=100, completed_at=timezone.now() - timedelta(days=1))
    LessonProgress.objects.create(user=student, lesson=lessons[1], percent=50, position_label="Worked example 2")
    StudySession.objects.create(user=student, title="Revise expressions", starts_at=timezone.now() + timedelta(hours=1))
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    ctx, html = response.context, response.content.decode()
    assert ctx["continue_card"]["lesson"] == lessons[1]
    assert ctx["continue_card"]["minutes_left"] == 10
    assert (ctx["overall"].done, ctx["overall"].total) == (1, 3)
    assert "Worked example 2" in html and "Revise expressions" in html and "Lesson 1" in html
    assert ctx["recent"][0].day_label == "Yesterday"


def test_streak_counts_consecutive_days():
    user = User.objects.create_user(email="streak@example.com", password="pw-Strong-123")
    today = timezone.localdate()
    for d in (1, 2, 3, 5):
        DailyActivity.objects.create(user=user, date=today - timedelta(days=d), seconds=600)
    assert learning_streak(user, today) == 3  # yesterday back to 3 days ago
    DailyActivity.objects.create(user=user, date=today, seconds=30)  # under a minute doesn't count
    assert learning_streak(user, today) == 3


def test_weekly_activity_marks_goal():
    user = User.objects.create_user(email="week@example.com", password="pw-Strong-123")
    today = timezone.localdate()
    DailyActivity.objects.create(user=user, date=today, seconds=50 * 60)
    DailyActivity.objects.create(user=user, date=today - timedelta(days=1), seconds=10 * 60)
    week = weekly_activity(user, today, 45)
    assert [d["minutes"] for d in week["days"]][-2:] == [10, 50]
    assert week["days"][-1]["reached"] and not week["days"][-2]["reached"]
    assert week["days"][-1]["label"] == "Today" and week["total_minutes"] == 60


def test_session_toggle_only_for_owner(client, student):
    other = User.objects.create_user(email="o@example.com", password="pw-Strong-123")
    session = StudySession.objects.create(user=other, title="Theirs", starts_at=timezone.now())
    client.force_login(student)
    assert client.post(reverse("learning:session_toggle", args=[session.pk])).status_code == 404
    mine = StudySession.objects.create(user=student, title="Mine", starts_at=timezone.now())
    response = client.post(reverse("learning:session_toggle", args=[mine.pk]), HTTP_HX_REQUEST="true")
    assert 'aria-checked="true"' in response.content.decode()
    mine.refresh_from_db()
    assert mine.is_completed
