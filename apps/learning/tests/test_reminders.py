"""Daily study reminder emails."""

from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.management import call_command
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson, Module, Topic
from apps.learning import reminders
from apps.learning.models import DailyActivity, Enrollment, RestDay, StudySession

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="r@example.com", password="pw-Strong-123", first_name="Rita")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.reminder_hour = 0  # due at any hour of the day
    p.save()
    return user


@pytest.fixture
def lessons(student, course, offering):
    Enrollment.objects.create(user=student, offering=offering)
    module = Module.objects.create(course=course, title="M", order=1)
    topic = Topic.objects.create(module=module, title="T", order=1)
    return [Lesson.objects.create(topic=topic, title=f"Lesson {i}", slug=f"rem-{i}", order=i, status="published")
            for i in range(3)]


def test_reminder_suggests_the_next_lesson_when_nothing_is_planned(student, lessons):
    assert reminders.send_for(student) is True
    assert len(mail.outbox) == 1
    assert "Lesson 0" in mail.outbox[0].body and mail.outbox[0].to == ["r@example.com"]
    assert "/accounts/reminders/off/" in mail.outbox[0].body


def test_reminder_lists_todays_planned_sessions(student, lessons):
    StudySession.objects.create(user=student, title="Revise algebra", starts_at=timezone.now() + timedelta(minutes=1),
                                duration_minutes=30)
    plan = reminders.build(student, timezone.localtime(timezone.now() + timedelta(minutes=1)).date())
    assert [s.title for s in plan["sessions"]] == ["Revise algebra"]


def test_no_reminder_after_studying_or_on_a_rest_day(student, lessons):
    DailyActivity.add(student, 300)
    assert reminders.build(student) is None
    DailyActivity.objects.all().delete()
    RestDay.objects.create(user=student, date=timezone.localdate())
    assert reminders.build(student) is None


def test_no_reminder_when_there_is_nothing_to_study(student):
    assert reminders.build(student) is None


def test_command_sends_once_a_day_and_respects_the_switch(student, lessons):
    call_command("send_reminders")
    call_command("send_reminders")  # second run the same day sends nothing
    assert len(mail.outbox) == 1
    student.profile.refresh_from_db()
    assert student.profile.last_reminder_on == timezone.localdate()

    other = User.objects.create_user(email="o@example.com", password="pw-Strong-123")
    other.profile.reminders_enabled = False
    other.profile.reminder_hour = 0
    other.profile.save()
    call_command("send_reminders")
    assert len(mail.outbox) == 1


def test_command_waits_for_the_chosen_hour(student, lessons):
    now = timezone.localtime()
    if now.hour == 23:
        pytest.skip("no later hour left today")
    student.profile.reminder_hour = now.hour + 1
    student.profile.save()
    call_command("send_reminders")
    assert mail.outbox == []


def test_unsubscribe_link_switches_reminders_off(client, student):
    url = reverse("accounts:reminders_off", args=[reminders.unsubscribe_token(student)])
    assert client.get(url).status_code == 200
    student.profile.refresh_from_db()
    assert student.profile.reminders_enabled is False


def test_bad_unsubscribe_token_changes_nothing(client, student):
    response = client.get(reverse("accounts:reminders_off", args=["nonsense"]))
    assert b"not valid" in response.content
    student.profile.refresh_from_db()
    assert student.profile.reminders_enabled is True


def test_settings_page_saves_reminder_choices(client, student, form5, science):
    client.force_login(student)
    response = client.post(reverse("accounts:profile"), {
        "section": "study", "study-level": form5.pk, "study-pathway": science.pk, "study-daily_goal_minutes": 45,
        "study-reminder_hour": 19})  # reminders box left unticked
    assert response.status_code == 302
    student.profile.refresh_from_db()
    assert (student.profile.reminders_enabled, student.profile.reminder_hour) == (False, 19)
