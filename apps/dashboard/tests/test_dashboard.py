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


def test_new_student_sees_only_what_they_need(client, student):
    """Before the first lesson there is one job: start. Empty charts and lists stay out of the way."""
    client.force_login(student)
    html = client.get(reverse("dashboard:home")).content.decode()
    assert "You haven’t started a lesson yet" in html
    assert "Dina!" in html
    for clutter in ("Nothing planned for the next 7 days", "Lessons you complete will appear here",
                    "Weekly learning activity", "Overall progress", "Recommended next", "Add your GCE exam date"):
        assert clutter not in html
    nav = client.get(reverse("dashboard:home")).context
    assert [i["key"] for i in nav["sidebar_items"] if i["key"] in ("progress", "saved")] == []


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
    assert "Worked example 2" in html and "Revise expressions" in html
    assert "Your week" in html and "Weekly learning activity" not in html  # the dashboard is "Today"; charts live on My Progress


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


def test_continue_card_skips_courses_that_are_no_longer_published(client, django_user_model, lesson):
    from django.utils import timezone
    from apps.learning.models import LessonProgress

    lesson.status = "published"
    lesson.save()
    user = django_user_model.objects.create_user(email="old@example.com", password="pw-Strong-123")
    profile = user.profile
    profile.level, profile.onboarded_at = lesson.course.offering.level, timezone.now()
    profile.save()
    LessonProgress.objects.create(user=user, lesson=lesson, percent=30)  # started, not finished
    client.force_login(user)
    assert lesson.get_absolute_url() in client.get("/dashboard/").content.decode()
    course = lesson.course
    course.status = "draft"  # e.g. a retired demo course
    course.save()
    assert lesson.get_absolute_url() not in client.get("/dashboard/").content.decode()


def test_started_student_gets_progress_and_saved_in_navigation(client, student, offering, lessons):
    LessonProgress.objects.create(user=student, lesson=lessons[0], percent=30)
    client.force_login(student)
    keys = [i["key"] for i in client.get(reverse("dashboard:home")).context["sidebar_items"]]
    assert "progress" in keys and "saved" in keys


def test_exam_student_keeps_revision_visible_even_when_empty(client, student, offering, lessons):
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=lessons[0], percent=100, completed_at=timezone.now())
    student.profile.exam_date = timezone.localdate() + timedelta(days=40)
    student.profile.save()
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    assert response.context["show"]["mode"] == "exam"
    assert "Upcoming revision" in response.content.decode()


def test_student_away_for_a_week_gets_welcome_back_not_a_streak(client, student, offering, lessons):
    LessonProgress.objects.create(user=student, lesson=lessons[0], percent=40)
    DailyActivity.objects.create(user=student, date=timezone.localdate() - timedelta(days=10), seconds=600)
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    assert response.context["show"]["away"] and not response.context["show"]["streak"]
    assert "Welcome back" in response.content.decode()


def test_lower_sixth_student_is_not_treated_as_exam_year(client, student, offering, lessons):
    from apps.academics.models import AcademicLevel

    lower = AcademicLevel.objects.get(code="L6")  # seeded by migration; Upper Sixth follows it
    student.profile.level, student.profile.exam_date = lower, timezone.localdate() + timedelta(days=30)
    student.profile.save()
    LessonProgress.objects.create(user=student, lesson=lessons[0], percent=100, completed_at=timezone.now())
    client.force_login(student)
    ctx = client.get(reverse("dashboard:home")).context
    assert ctx["show"]["mode"] == "active"


def test_many_subjects_are_capped_on_the_dashboard(client, student):
    from apps.academics.models import Subject, SubjectOffering

    for i in range(8):
        subject = Subject.objects.create(name=f"Subject {i}", slug=f"s{i}", icon_text="S")
        o = SubjectOffering.objects.create(subject=subject, level=student.profile.level)
        o.pathways.add(student.profile.pathway)
        Enrollment.objects.create(user=student, offering=o)
    client.force_login(student)
    ctx = client.get(reverse("dashboard:home")).context
    assert len(ctx["plan_shown"]) == 6 and ctx["plan_more"] == 2


def test_new_student_is_pointed_at_their_first_lesson(client, student, offering, lessons):
    Enrollment.objects.create(user=student, offering=offering)
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    html = response.content.decode()
    assert response.context["start_here"] == lessons[0]
    assert "Start your first lesson" in html and lessons[0].get_absolute_url() in html


def test_finishing_every_started_lesson_does_not_say_nothing_was_started(client, student, offering, lessons):
    """Regression: after completing a lesson the card used to claim 'You haven't started a lesson yet'."""
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=lessons[0], percent=100, completed_at=timezone.now())
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    html = response.content.decode()
    assert response.context["continue_card"] is None
    assert "You haven’t started a lesson yet" not in html
    assert "You’re up to date" in html
    assert response.context["recommended"] is not None or lessons[1].title in html
