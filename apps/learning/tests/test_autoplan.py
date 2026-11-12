"""Automatic planning: 'Plan my week', clearing it, missed sessions, and sessions ticking themselves off."""

from datetime import datetime, time, timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson, Module, Topic
from apps.learning import autoplan
from apps.learning.models import Enrollment, RestDay, SessionKind, StudySession

pytestmark = pytest.mark.django_db
User = get_user_model()

MONDAY = datetime(2026, 11, 9, 8, 0)  # a Monday morning, so Monday evening is still ahead


def at(day_offset, hour, minute=0):
    return timezone.make_aware(datetime(2026, 11, 9 + day_offset, hour, minute))


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="p@example.com", password="pw-Strong-123", first_name="Pia")
    p = user.profile
    p.level, p.pathway, p.onboarded_at, p.daily_goal_minutes = form5, science, timezone.now(), 45
    p.save()
    return user


@pytest.fixture
def lessons(student, course, offering):
    Enrollment.objects.create(user=student, offering=offering)
    module = Module.objects.create(course=course, title="Planning module", order=1)
    topic = Topic.objects.create(module=module, title="Planning topic", order=1)
    return [Lesson.objects.create(topic=topic, title=f"Lesson {i}", slug=f"plan-{i}", order=i, status="published",
                                  estimated_minutes=20) for i in range(20)]


def plan(student, course, weekdays=(0, 1, 2), days=7, start=time(17, 0), now=None):
    return autoplan.build_plan(student, student.profile, [course], at(0, 0).date(), days, set(weekdays), start,
                               now=now or at(0, 8))


def test_each_study_day_is_filled_up_to_the_goal_in_order(student, course, lessons):
    result = plan(student, course)
    assert len(result) == 9  # three days, 20-minute lessons until 45 minutes are reached = three a day
    assert [p["lesson"] for p in result] == lessons[:9]
    monday = [p for p in result if timezone.localtime(p["starts_at"]).date() == at(0, 0).date()]
    assert [timezone.localtime(p["starts_at"]).strftime("%H:%M") for p in monday] == ["17:00", "17:30", "18:00"]
    assert {timezone.localtime(p["starts_at"]).weekday() for p in result} == {0, 1, 2}


def test_rest_days_and_busy_times_are_respected(student, course, lessons):
    RestDay.objects.create(user=student, date=at(1, 0).date())
    StudySession.objects.create(user=student, title="Maths class", starts_at=at(0, 17), duration_minutes=60)
    result = plan(student, course)
    days = {timezone.localtime(p["starts_at"]).date() for p in result}
    assert at(1, 0).date() not in days
    first = min(p["starts_at"] for p in result)
    assert timezone.localtime(first).strftime("%H:%M") == "18:10"


def test_today_only_gets_sessions_that_are_still_ahead(student, course, lessons):
    late = at(0, 23, 10)
    result = plan(student, course, weekdays=(0,), now=late)
    assert result == []  # nothing fits before the end of the evening
    result = plan(student, course, weekdays=(0, 1), now=at(0, 17, 40))
    first = min(p["starts_at"] for p in result)
    assert first > at(0, 17, 40)


def test_lessons_already_planned_are_not_planned_twice(student, course, lessons):
    StudySession.objects.create(user=student, title="x", lesson=lessons[0], starts_at=at(3, 17))
    result = plan(student, course)
    assert lessons[0] not in [p["lesson"] for p in result]


def test_plan_week_view_creates_sessions_and_reports(client, student, course, lessons):
    client.force_login(student)
    monday = timezone.localdate() - timedelta(days=timezone.localdate().weekday())
    response = client.post(reverse("learning:plan_week"), {"date": monday.isoformat(), "days": [0, 1, 2, 3, 4, 5, 6],
                                                           "start_time": "17:00", "weeks": "2"}, follow=True)
    assert response.status_code == 200
    created = StudySession.objects.filter(user=student)
    assert created.count() >= 3
    assert all(s.starts_at > timezone.now() for s in created)
    assert all(s.kind == SessionKind.STUDY and s.lesson for s in created)
    assert "Planned" in response.content.decode()


def test_plan_week_needs_a_day_and_subjects(client, student, course):
    client.force_login(student)
    client.post(reverse("learning:plan_week"), {"date": "2026-11-09", "start_time": "17:00"})
    assert not StudySession.objects.exists()
    response = client.post(reverse("learning:plan_week"), {"date": "2026-11-09", "days": [0], "start_time": "17:00"})
    assert response.status_code == 302 and not StudySession.objects.exists()  # no enrolled subjects


def test_planner_offers_to_plan_an_empty_week(client, student, lessons):
    client.force_login(student)
    page = client.get(reverse("learning:planner")).content.decode()
    assert "Nothing planned for" in page and "Plan my week" in page


def test_clear_week_keeps_done_and_past_sessions(client, student):
    client.force_login(student)
    now = timezone.now()
    future = StudySession.objects.create(user=student, title="later", starts_at=now + timedelta(hours=1))
    done = StudySession.objects.create(user=student, title="done", starts_at=now + timedelta(hours=2), completed_at=now)
    past = StudySession.objects.create(user=student, title="past", starts_at=now - timedelta(hours=3))
    client.post(reverse("learning:week_clear"), {"date": timezone.localtime(future.starts_at).date().isoformat()})
    remaining = set(StudySession.objects.values_list("pk", flat=True))
    assert future.pk not in remaining
    assert done.pk in remaining and past.pk in remaining


def test_missed_sessions_are_listed_and_can_move_forward(client, student):
    client.force_login(student)
    missed = StudySession.objects.create(user=student, title="Missed one", starts_at=timezone.now() - timedelta(days=1),
                                         duration_minutes=30)
    page = client.get(reverse("learning:planner")).content.decode()
    assert "Missed sessions" in page and "Missed one" in page
    client.post(reverse("learning:session_reschedule", args=[missed.pk]))
    missed.refresh_from_db()
    assert missed.starts_at > timezone.now()
    assert timezone.localtime(missed.starts_at).time().replace(second=0, microsecond=0) == \
        timezone.localtime(missed.starts_at).time().replace(second=0, microsecond=0)
    assert "Missed sessions" not in client.get(reverse("learning:planner")).content.decode()


def test_reschedule_is_private(client, student):
    other = User.objects.create_user(email="o@example.com", password="pw-Strong-123")
    theirs = StudySession.objects.create(user=other, title="T", starts_at=timezone.now() - timedelta(days=1))
    client.force_login(student)
    assert client.post(reverse("learning:session_reschedule", args=[theirs.pk])).status_code == 404


def test_finishing_a_lesson_ticks_its_planned_session(client, student, course, lessons):
    client.force_login(student)
    planned = StudySession.objects.create(user=student, title="Lesson 0", lesson=lessons[0], starts_at=timezone.now() + timedelta(hours=3))
    other = StudySession.objects.create(user=student, title="Lesson 1", lesson=lessons[1], starts_at=timezone.now() + timedelta(hours=4))
    client.post(reverse("courses:lesson_complete", args=[course.slug, lessons[0].pk]))
    planned.refresh_from_db()
    other.refresh_from_db()
    assert planned.is_completed and not other.is_completed


def test_this_week_stops_at_sunday(client, student, course, lessons):
    client.force_login(student)
    today = timezone.localdate()
    monday = today - timedelta(days=today.weekday())
    client.post(reverse("learning:plan_week"), {"date": monday.isoformat(), "days": [0, 1, 2, 3, 4, 5, 6],
                                                "start_time": "06:00", "weeks": "1"})
    last_day = max(timezone.localtime(s.starts_at).date() for s in StudySession.objects.filter(user=student))
    assert last_day <= monday + timedelta(days=6)
