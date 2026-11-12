"""Navigation: one "My Courses" entry, a phone tab bar with Practice, a "Today" dashboard, one place for the exam date."""

from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import SubjectOffering
from apps.learning.models import Enrollment, LessonProgress
from apps.learning.tests.test_course_organisation import build, levels, student, subject  # noqa: F401  (fixtures and helpers)

pytestmark = pytest.mark.django_db


def started(student, offering):
    """Make the student 'started': one open lesson in this offering, and enrol them."""
    Enrollment.objects.get_or_create(user=student, offering=offering)
    lesson = offering.courses.get().modules.first().topics.first().lessons.first()
    LessonProgress.objects.create(user=student, lesson=lesson, percent=30)
    return lesson


def labels(items):
    return [i["label"] for i in items]


def test_sidebar_has_one_my_courses_entry_instead_of_three(client, student, levels, science):
    started(student, build(subject("Maths"), levels["F5"], science))
    client.force_login(student)
    items = client.get(reverse("dashboard:home")).context["sidebar_items"]
    assert labels(items) == ["Today", "My Courses", "Explore Subjects", "Practice", "Study Planner", "My Progress", "Report Card", "Saved Lessons", "Settings"]
    assert "My Subjects" not in labels(items) and "Continue Learning" not in labels(items)


def test_phone_tab_bar_has_practice(client, student, levels, science):
    started(student, build(subject("Maths"), levels["F5"], science))
    client.force_login(student)
    tabs = client.get(reverse("dashboard:home")).context["bottom_items"]
    assert labels(tabs) == ["Today", "Learn", "Practice", "Progress", "Me"]


def test_new_student_phone_tabs_hide_progress_until_they_start(client, student):
    client.force_login(student)
    assert labels(client.get(reverse("dashboard:home")).context["bottom_items"]) == ["Today", "Learn", "Practice", "Me"]


def test_old_pages_light_up_the_same_my_courses_item(client, student, levels, science):
    started(student, build(subject("Maths"), levels["F5"], science))
    client.force_login(student)
    for name in ("courses:continue", "courses:my_subjects"):
        html = client.get(reverse(name)).content.decode()
        assert html.count('aria-current="page"') >= 1
        assert "My Courses" in html


def test_my_courses_lets_you_add_more_subjects_and_returns_to_the_page(client, student, levels, science):
    maths = build(subject("Maths"), levels["F5"], science)
    english = build(subject("English"), levels["F5"], science)
    started(student, maths)
    client.force_login(student)
    page = client.get(reverse("courses:continue"))
    assert [o.pk for o in page.context["suggestions"]] == [english.pk]
    assert "Add more subjects" in page.content.decode() and "+ English" in page.content.decode()
    response = client.post(reverse("courses:toggle_plan", args=[english.pk]), {"next": reverse("courses:continue")})
    assert response.url == reverse("courses:continue")  # back where they were, not on another page
    assert Enrollment.objects.filter(user=student, offering=english).exists()
    assert client.post(reverse("courses:add_class_subjects"), {"next": "https://evil.example/"}).url == reverse("courses:my_subjects")


def test_dashboard_is_today_and_keeps_charts_on_my_progress(client, student, levels, science):
    started(student, build(subject("Maths"), levels["F5"], science))
    client.force_login(student)
    html = client.get(reverse("dashboard:home")).content.decode()
    assert "Your week" in html and "See my progress" in html and "All my courses" in html
    for moved in ("Weekly learning activity", "Recently completed", "Overall progress"):
        assert moved not in html
    assert "Weekly learning activity" in client.get(reverse("learning:progress")).content.decode()


def test_exam_date_is_set_in_settings_not_in_the_planner(client, student, levels, science):
    for i in range(3):  # enough finished lessons for the dashboard to suggest an exam date
        offering = build(subject(f"S{i}"), levels["F5"], science, lessons=(("M", "T", f"l{i}"),))
        lesson = started(student, offering)
        LessonProgress.objects.filter(user=student, lesson=lesson).update(completed_at=timezone.now(), percent=100)
    client.force_login(student)
    settings_link = reverse("accounts:profile") + "#exam-date"
    assert settings_link in client.get(reverse("dashboard:home")).content.decode()
    planner = client.get(reverse("learning:planner")).content.decode()
    assert settings_link in planner and 'action="' + reverse("learning:exam_date") + '"' not in planner
    assert 'id="exam-date"' in client.get(reverse("accounts:profile")).content.decode()
    student.profile.exam_date = timezone.localdate() + timedelta(days=50)
    student.profile.save()
    assert "Change your exam date in settings" in client.get(reverse("learning:planner")).content.decode()
