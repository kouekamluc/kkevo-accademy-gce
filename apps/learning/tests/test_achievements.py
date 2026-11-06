from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.learning import achievements
from apps.learning.models import Achievement, DailyActivity, Enrollment, LessonProgress

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="m@example.com", password="pw-Strong-123", first_name="Mia")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


def test_nothing_is_earned_before_any_learning(student):
    assert achievements.award(student) == []
    assert not Achievement.objects.filter(user=student).exists()


def test_first_lesson_earns_first_step_once(student, lesson):
    LessonProgress.objects.create(user=student, lesson=lesson, percent=100, completed_at=timezone.now())
    assert [m.code for m in achievements.award(student)] == ["first_lesson"]
    assert achievements.award(student) == []  # idempotent: never announced twice


def test_streak_milestone_needs_real_consecutive_days(student):
    today = timezone.localdate()
    for back in (0, 1):
        DailyActivity.objects.create(user=student, date=today - timedelta(days=back), seconds=600)
    assert "streak_3" not in [m.code for m in achievements.award(student)]
    DailyActivity.objects.create(user=student, date=today - timedelta(days=2), seconds=600)
    assert "streak_3" in [m.code for m in achievements.award(student)]


def test_today_strip_reports_goal_progress(student):
    student.profile.daily_goal_minutes = 20
    student.profile.save()
    DailyActivity.objects.create(user=student, date=timezone.localdate(), seconds=600)
    strip = achievements.today_strip(student)
    assert (strip["minutes"], strip["goal"], strip["percent"], strip["reached"]) == (10, 20, 50, False)


def test_completing_a_lesson_shows_milestone_and_whatsapp_share(client, student, course, lesson):
    lesson.status = "published"
    lesson.save()
    Enrollment.objects.create(user=student, offering=course.offering)
    client.force_login(student)
    url = reverse("courses:lesson_complete", args=[course.slug, lesson.pk])
    html = client.post(url, HTTP_HX_REQUEST="true").content.decode()
    assert "New milestone: First step" in html
    assert "https://wa.me/?text=" in html and "daily goal" not in html.lower().replace("daily goal reached", "")


def test_progress_page_lists_milestones(client, student):
    client.force_login(student)
    html = client.get(reverse("learning:progress")).content.decode()
    assert "Milestones" in html and "First step" in html


def test_progress_page_opens_with_level_hero(client, student):
    client.force_login(student)
    html = client.get(reverse("learning:progress")).content.decode()
    assert "Level 1" in html and "more points to reach level 2" in html and "0 of 9 milestones" in html


def test_level_thresholds_and_distance_to_next_level():
    assert achievements.level_for(0)["level"] == 1
    assert achievements.level_for(99)["to_next"] == 1
    assert achievements.level_for(100)["level"] == 2
    assert achievements.level_for(300)["level"] == 3
