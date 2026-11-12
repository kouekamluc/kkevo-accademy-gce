"""Continue Learning shows every course to choose from, and prerequisites steer what comes next."""

from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson
from apps.learning import services
from apps.learning.models import Enrollment, LessonProgress
from apps.learning.tests.test_course_organisation import build, levels, student, subject  # noqa: F401  (fixtures and helpers)

pytestmark = pytest.mark.django_db

TWO = (("Module", "Topic", "first"), ("Module", "Topic", "second"))


def lesson_of(offering, slug):
    return Lesson.objects.get(topic__module__course__offering=offering, slug=slug)


def touch(student, lesson, *, done=False, when=None):
    when = when or timezone.now()
    return LessonProgress.objects.create(
        user=student, lesson=lesson, percent=100 if done else 40, last_viewed_at=when, completed_at=when if done else None)


def test_continue_page_lists_every_course_with_the_last_opened_first(client, student, levels, science):
    alpha = build(subject("Alpha"), levels["F5"], science, lessons=TWO)
    beta = build(subject("Beta"), levels["F5"], science, lessons=TWO)
    gamma = build(subject("Gamma"), levels["F5"], science, lessons=TWO)
    delta = build(subject("Delta"), levels["F5"], science, lessons=TWO)
    for offering in (alpha, beta, gamma, delta):
        Enrollment.objects.create(user=student, offering=offering)
    now = timezone.now()
    touch(student, lesson_of(alpha, "first"), done=True, when=now - timedelta(days=5))
    touch(student, lesson_of(beta, "first"), when=now - timedelta(hours=1))  # opened most recently, unfinished
    for slug in ("first", "second"):
        touch(student, lesson_of(delta, slug), done=True, when=now - timedelta(days=9))
    client.force_login(student)
    response = client.get(reverse("courses:continue"))
    assert response.status_code == 200  # a page to choose from, not a redirect to the last lesson
    ctx = response.context
    assert [r["subject"].name for r in ctx["started"]] == ["Beta", "Alpha"]
    assert [r["subject"].name for r in ctx["fresh"]] == ["Gamma"]
    assert [r["subject"].name for r in ctx["finished"]] == ["Delta"]
    assert ctx["last"]["subject"].name == "Beta"
    assert ctx["last"]["resume_url"].endswith("?resume=1")  # an unfinished lesson reopens where they stopped
    alpha_row = ctx["started"][1]
    assert alpha_row["lesson"].slug == "second" and not alpha_row["resume_url"].endswith("?resume=1")
    html = response.content.decode()
    assert "Where you left off" in html and "Pick the course you want" in html
    for name in ("Alpha", "Beta", "Gamma", "Delta"):
        assert name in html


def test_continue_page_without_courses_points_to_explore(client, student):
    client.force_login(student)
    response = client.get(reverse("courses:continue"))
    assert response.status_code == 200 and "no courses in your plan yet" in response.content.decode()


def test_subjects_without_lessons_are_listed_as_coming_soon(client, student, levels, science):
    from apps.academics.models import SubjectOffering

    empty = SubjectOffering.objects.create(subject=subject("Geology"), level=levels["F5"])
    empty.pathways.add(science)
    Enrollment.objects.create(user=student, offering=empty)
    client.force_login(student)
    assert "Coming soon in your plan:" in client.get(reverse("courses:continue")).content.decode()


# ------------------------------------------------------------------ prerequisites

THREE = (("Module", "Topic", "a-first"), ("Module", "Topic", "b-second"), ("Module", "Topic", "c-third"))


@pytest.fixture
def chain(student, levels, science):
    offering = build(subject("Algebra"), levels["F5"], science, lessons=THREE)
    Enrollment.objects.create(user=student, offering=offering)
    return offering, lesson_of(offering, "a-first"), lesson_of(offering, "b-second"), lesson_of(offering, "c-third")


def test_next_lesson_skips_a_lesson_whose_prerequisite_is_not_done(student, chain):
    offering, a, b, c = chain
    b.prerequisites.add(c)  # B needs C first
    touch(student, a, done=True)
    course = offering.courses.get()
    assert services.next_lesson(student, course)[0] == c  # B is waiting on C
    touch(student, c, done=True)
    assert services.next_lesson(student, course)[0] == b  # now B is ready


def test_when_everything_left_is_blocked_the_first_one_is_still_suggested(student, chain):
    offering, a, b, c = chain
    b.prerequisites.add(c)
    c.prerequisites.add(b)  # a loop in the content must never strand a student
    touch(student, a, done=True)
    assert services.next_lesson(student, offering.courses.get())[0] == b


def test_missing_prerequisites_ignore_unpublished_lessons(student, chain):
    _offering, a, b, c = chain
    b.prerequisites.add(a, c)
    assert services.missing_prerequisites(student, b) == [a, c]
    touch(student, a, done=True)
    assert services.missing_prerequisites(student, b) == [c]
    Lesson.objects.filter(pk=c.pk).update(status="draft")  # a student can never finish an unpublished lesson
    assert services.missing_prerequisites(student, b) == []


def test_lesson_page_recommends_prerequisites_without_locking_the_lesson(client, student, chain):
    _offering, a, b, _c = chain
    b.prerequisites.add(a)
    client.force_login(student)
    page = client.get(b.get_absolute_url())
    html = page.content.decode()
    assert page.status_code == 200  # advice only: the lesson is open
    assert "Recommended before this lesson" in html and a.title in html
    touch(student, a, done=True)
    assert "Recommended before this lesson" not in client.get(b.get_absolute_url()).content.decode()


# ------------------------------------------------------------------ grouped by class


def test_my_courses_groups_courses_by_class_with_their_own_class_first(client, student, levels, science):
    chemistry = subject("Chemistry")
    chem_f5 = build(chemistry, levels["F5"], science, lessons=TWO)
    chem_u6 = build(chemistry, levels["U6"], science, lessons=TWO)
    chem_l6 = build(chemistry, levels["L6"], science, lessons=TWO)
    build(subject("Biology"), levels["F5"], science, lessons=TWO)  # in the class, not added yet
    for offering in (chem_f5, chem_u6, chem_l6):
        Enrollment.objects.create(user=student, offering=offering)
    touch(student, lesson_of(chem_u6, "first"))
    touch(student, lesson_of(chem_f5, "first"), done=True)
    touch(student, lesson_of(chem_f5, "second"), done=True)
    client.force_login(student)
    response = client.get(reverse("courses:continue"))
    sections = response.context["sections"]
    assert [s["level"].slug for s in sections][0] == student.profile.level.slug  # their own class leads
    by_level = {s["level"].code: s for s in sections}
    assert set(by_level) == {"F5", "L6", "U6"}
    # one Chemistry card per class, never mixed into one grid
    assert all([r["subject"].name for r in by_level[code]["rows"]] == ["Chemistry"] for code in ("F5", "L6", "U6"))
    assert by_level["U6"]["in_progress"] == 1 and by_level["F5"]["finished"] == 1 and by_level["L6"]["n"] == 1
    # what else the class offers is one tap away
    assert [o.subject.name for o in by_level["F5"]["add"]] == ["Biology"]
    html = response.content.decode()
    assert "Upper Sixth" in html and "Lower Sixth" in html and "Add more subjects in Form 5" in html
