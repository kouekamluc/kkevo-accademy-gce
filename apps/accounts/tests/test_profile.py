from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import AcademicLevel
from apps.accounts.models import AVATAR_EMOJI, StudentProfile

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="pf@example.com", password="pw-Strong-123", first_name="Pam", last_name="Nji")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


def study_post(student, **extra):
    data = {"section": "study", "study-level": student.profile.level_id, "study-pathway": "", "study-daily_goal_minutes": 45}
    data.update(extra)
    return data


def test_profile_opens_with_hero_goal_chips_and_logout(client, student):
    client.force_login(student)
    html = client.get(reverse("accounts:profile")).content.decode()
    assert "Pam Nji" in html and "Level 1" in html and "Pick your avatar" in html
    assert "15 min" in html and "90 min" in html and "Log out" in html and "Delete my account" in html


def test_unusual_goal_still_appears_as_a_chip(client, student):
    student.profile.daily_goal_minutes = 50
    student.profile.save()
    client.force_login(student)
    assert "50 min" in client.get(reverse("accounts:profile")).content.decode()


def test_avatar_is_saved_and_shown_in_the_header(client, student):
    client.force_login(student)
    client.post(reverse("accounts:profile"), {"section": "avatar", "avatar": "lion"})
    assert StudentProfile.objects.get(user=student).avatar == "lion"
    assert AVATAR_EMOJI["lion"] in client.get(reverse("dashboard:home")).content.decode()


def test_unknown_avatar_is_rejected(client, student):
    client.force_login(student)
    client.post(reverse("accounts:profile"), {"section": "avatar", "avatar": "dragon"})
    assert StudentProfile.objects.get(user=student).avatar == ""


def test_exam_date_can_be_set_from_settings(client, student):
    client.force_login(student)
    when = timezone.localdate() + timedelta(days=60)
    client.post(reverse("accounts:profile"), study_post(student, **{"study-exam_date": when.isoformat()}))
    assert StudentProfile.objects.get(user=student).exam_date == when


def test_past_exam_date_is_rejected_but_an_old_saved_one_does_not_block_saving(client, student):
    client.force_login(student)
    past = timezone.localdate() - timedelta(days=3)
    response = client.post(reverse("accounts:profile"), study_post(student, **{"study-exam_date": past.isoformat()}))
    assert response.status_code == 200 and "still ahead" in response.content.decode()
    StudentProfile.objects.filter(user=student).update(exam_date=past)  # the date has since passed
    client.post(reverse("accounts:profile"), study_post(student, **{"study-exam_date": past.isoformat(), "study-daily_goal_minutes": 30}))
    profile = StudentProfile.objects.get(user=student)
    assert profile.daily_goal_minutes == 30 and profile.exam_date == past
