"""Stage 1 of the retention plan: no dead ends, readable buttons, a correct tab map, subject colours."""

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.academics.colours import BY_CATEGORY, VIOLET, subject_colour
from apps.academics.models import Subject, SubjectOffering
from apps.courses.models import Course, Lesson, Module, Topic
from apps.learning.models import Enrollment

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(form5, science):
    user = User.objects.create_user(email="r@example.com", password="pw-Strong-123", first_name="Rita")
    profile = user.profile
    profile.level, profile.pathway, profile.onboarded_at = form5, science, timezone.now()
    profile.save()
    return user


def _offering(name, level, pathway, *, lessons=0, order=0):
    subject = Subject.objects.create(name=name, slug=name.lower().replace(" ", "-"), icon_text=name[:2], order=order)
    offering = SubjectOffering.objects.create(subject=subject, level=level)
    offering.pathways.add(pathway)
    if lessons:
        course = Course.objects.create(offering=offering, title=f"{name} course", slug=f"{subject.slug}-course",
                                       status="published")
        topic = Topic.objects.create(module=Module.objects.create(course=course, title="M", order=1), title="T", order=1)
        for i in range(lessons):
            Lesson.objects.create(topic=topic, title=f"{name} {i}", slug=f"{subject.slug}-{i}", order=i, status="published")
    return offering




def test_catalog_puts_subjects_with_lessons_before_coming_soon(client, student, form5, science):
    # "Empty" sorts first by subject order and is in the plan, but it has no lessons.
    empty = _offering("Empty", form5, science, order=0)
    _offering("Ready", form5, science, lessons=3, order=1)
    Enrollment.objects.create(user=student, offering=empty)
    client.force_login(student)
    response = client.get(reverse("courses:catalog"))
    cards = response.context["cards"]
    assert [c["subject"].name for c in cards] == ["Ready", "Empty"]
    assert [c["ready"] for c in cards] == [True, False]
    assert response.context["ready_count"] == 1
    html = response.content.decode()
    assert html.index("Ready") < html.index("Coming soon") < html.index("Empty")


def test_catalog_has_no_coming_soon_heading_when_everything_is_ready(client, student, form5, science):
    _offering("Ready", form5, science, lessons=1)
    client.force_login(student)
    assert "Coming soon" not in client.get(reverse("courses:catalog")).content.decode()








def test_green_buttons_use_dark_text(client, student, lesson):
    lesson.status = "published"
    lesson.save()
    client.force_login(student)
    course = lesson.topic.module.course
    html = client.get(reverse("courses:lesson", args=[course.slug, lesson.pk])).content.decode()
    assert "bg-success text-white" not in html
    assert "bg-success text-[#052E1C]" in html


def test_subject_colours_by_slug_category_and_fallback():
    assert subject_colour(Subject(slug="physics", category="sciences")) == "#2563EB"
    assert subject_colour(Subject(slug="chemistry", category="sciences")) != subject_colour(Subject(slug="physics"))
    assert subject_colour(Subject(slug="new-language", category="languages")) == BY_CATEGORY["languages"]
    assert subject_colour(Subject(slug="mystery", category="")) == VIOLET


def test_catalog_lists_plan_subjects_first_within_each_group(client, student, form5, science):
    _offering("Alpha", form5, science, lessons=1, order=0)
    beta = _offering("Beta", form5, science, lessons=1, order=1)
    Enrollment.objects.create(user=student, offering=beta)
    client.force_login(student)
    names = [c["subject"].name for c in client.get(reverse("courses:catalog")).context["cards"]]
    assert names == ["Beta", "Alpha"]


def test_subject_tile_uses_the_subject_colour(client, student, form5, science):
    offering = _offering("Physics", form5, science, lessons=1)
    client.force_login(student)
    html = client.get(reverse("courses:catalog")).content.decode()
    assert f"background-color: {offering.subject.colour}" in html
