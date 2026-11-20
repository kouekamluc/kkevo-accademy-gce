from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.urls import reverse
from django.utils import timezone

from apps.accounts.models import StudentProfile
from apps.learning.models import DailyActivity, LessonFeedback, LessonProgress
from apps.practice.models import Attempt, PracticeSet

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def editor(db):
    user = User.objects.create_user(email="editor@example.com", password="pw-Strong-123", is_staff=True)
    user.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    return user


@pytest.fixture
def pilot(lesson, form5):
    """Three students: one who did everything, one who only opened a lesson, one who signed up and left."""
    now = timezone.now()
    keen, curious, gone = (User.objects.create_user(email=f"{n}@example.com", password="pw-Strong-123")
                           for n in ("keen", "curious", "gone"))
    for user in (keen, curious):
        profile, _ = StudentProfile.objects.get_or_create(user=user)
        profile.level = form5
        profile.onboarded_at = now
        profile.save()
    LessonProgress.objects.create(user=keen, lesson=lesson, percent=100, completed_at=now)
    progress = LessonProgress.objects.create(user=curious, lesson=lesson, percent=40)
    LessonProgress.objects.filter(pk=progress.pk).update(started_at=now - timedelta(hours=3))
    practice = PracticeSet.objects.create(topic=lesson.topic, title="Set A", status="published")
    mock = PracticeSet.objects.create(topic=lesson.topic, title="Mock A", status="published", is_mock=True)
    Attempt.objects.create(user=keen, practice_set=practice, completed_at=now)
    Attempt.objects.create(user=keen, practice_set=mock, completed_at=now)
    DailyActivity.objects.create(user=keen, date=timezone.localdate(), seconds=1500)
    DailyActivity.objects.create(user=keen, date=timezone.localdate() - timedelta(days=1), seconds=600)
    LessonFeedback.objects.create(user=curious, lesson=lesson, kind=LessonFeedback.Kind.values[0], message="Typo")
    # staff activity is never counted
    staff = User.objects.create_user(email="staff@example.com", password="pw-Strong-123", is_staff=True)
    LessonProgress.objects.create(user=staff, lesson=lesson, percent=100, completed_at=now)
    return keen, curious, gone


def test_usage_is_staff_only(client):
    url = reverse("studio:usage")
    assert client.get(url).status_code == 302
    client.force_login(User.objects.create_user(email="s@example.com", password="pw-Strong-123"))
    assert client.get(url).status_code == 403


def test_usage_counts_students_only(client, editor, pilot):
    client.force_login(editor)
    response = client.get(reverse("studio:usage"))
    assert response.status_code == 200
    h = response.context["headline"]
    assert h["students"] == 3
    assert h["new_students"] == 3
    assert h["active"] == 2  # keen and curious; the staff account and "gone" are not counted
    assert h["lessons_completed"] == 1
    assert h["practice_finished"] == 1
    assert h["mocks_finished"] == 1
    assert h["minutes"] == 35
    assert h["reports"] == 1
    assert response.context["returning"] == 1  # keen was active yesterday and today

    funnel = {s["label"]: s["n"] for s in response.context["funnel"]}
    assert list(funnel.values()) == [3, 2, 2, 1, 1]

    classes = {c["name"]: (c["n"], c["active"]) for c in response.context["classes"]}
    assert classes["Form 5"] == (2, 2)
    assert classes["No class chosen yet"] == (1, 0)

    assert response.context["subjects"][0]["n"] == 1
    assert response.context["opened"][0]["n"] == 2
    drop = response.context["dropoff"]
    assert len(drop) == 1 and drop[0]["n"] == 1 and drop[0]["avg_percent"] == 40
    assert len(response.context["daily"]) == 7
    assert response.context["daily"][-1]["n"] == 2


def test_usage_period_and_bad_input(client, editor, pilot):
    client.force_login(editor)
    assert len(client.get(reverse("studio:usage") + "?days=30").context["daily"]) == 30
    assert client.get(reverse("studio:usage") + "?days=abc").context["days"] == 7
    assert client.get(reverse("studio:usage") + "?days=9999").context["days"] == 7


def test_usage_empty(client, editor):
    client.force_login(editor)
    page = client.get(reverse("studio:usage")).content.decode()
    assert "Nobody signed up in this period." in page
    assert "Usage" in page
