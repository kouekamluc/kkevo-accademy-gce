import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import AcademicLevel, Subject, SubjectOffering
from apps.courses.models import Course, Lesson, Module, Topic
from apps.learning import services
from apps.learning.models import Enrollment, LessonProgress

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="s@example.com", password="pw-Strong-123", first_name="Sam")
    profile = user.profile
    profile.level, profile.pathway, profile.onboarded_at = form5, science, timezone.now()
    profile.save()
    return user


@pytest.fixture
def outline(course):
    """2 modules: A (topic with 3 lessons), B (topic with 1 lesson + 1 draft)."""
    a = Module.objects.create(course=course, title="Algebra", order=1)
    b = Module.objects.create(course=course, title="Geometry", order=2)
    ta = Topic.objects.create(module=a, title="Expressions", order=1)
    tb = Topic.objects.create(module=b, title="Angles", order=1)
    lessons = [Lesson.objects.create(topic=ta, title=f"L{i}", slug=f"l{i}", order=i, status="published") for i in (1, 2, 3)]
    lessons.append(Lesson.objects.create(topic=tb, title="L4", slug="l4", order=1, status="published"))
    Lesson.objects.create(topic=tb, title="Draft lesson", slug="draft", order=2, status="draft")
    return lessons


def test_catalog_lists_offerings_for_level_and_marks_plan(client, student, offering, course, outline):
    other = Subject.objects.create(name="Other Subject", slug="other", icon_text="O", category="humanities")
    SubjectOffering.objects.create(subject=other, level=offering.level)
    Enrollment.objects.create(user=student, offering=offering)
    client.force_login(student)
    html = client.get(reverse("courses:catalog")).content.decode()
    assert "Test Subject" in html and "Other Subject" in html
    assert "In your plan" in html and "1 is in your plan" in html
    assert "Continue · 0%" not in html and "Start course" in html
    assert "Lessons coming soon" in html  # Other Subject has no course


def test_catalog_filters_by_stream_category_search_and_level(client, offering, course, outline):
    arts_only = Subject.objects.create(name="History", slug="history", icon_text="H", category="humanities")
    o = SubjectOffering.objects.create(subject=arts_only, level=offering.level)
    o.pathways.add(*__import__("apps.academics.models", fromlist=["AcademicPathway"]).AcademicPathway.objects.filter(slug="arts"))
    url = reverse("courses:catalog")
    names = lambda r: [c["subject"].name for c in r.context["cards"]]  # noqa: E731
    assert names(client.get(url, {"stream": "arts"})) == ["History"]
    assert names(client.get(url, {"stream": "science"})) == ["Test Subject"]
    assert names(client.get(url, {"category": "humanities"})) == ["History"]
    assert names(client.get(url, {"q": "L2"})) == ["Test Subject"]  # matches a lesson title
    assert names(client.get(url, {"level": "upper-sixth"})) == []
    assert "No subjects match" in client.get(url, {"level": "upper-sixth"}).content.decode()


def test_catalog_htmx_returns_only_results(client, offering, course):
    response = client.get(reverse("courses:catalog"), HTTP_HX_REQUEST="true", HTTP_HX_TARGET="catalog-results")
    html = response.content.decode()
    assert html.lstrip().startswith('<section id="catalog-results"')
    assert "<html" not in html


def test_course_detail_public_and_ordered(client, course, outline):
    html = client.get(course.get_absolute_url()).content.decode()
    assert html.index("Algebra") < html.index("Geometry")
    assert html.index(">L1<") < html.index(">L2<") < html.index(">L3<")
    assert "Draft lesson" not in html
    assert "Learn this course for free" in html
    assert "not yet mapped to the official GCE syllabus" in html


def test_course_detail_progress_and_continue(client, student, course, outline, offering):
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=outline[0], percent=100, completed_at=timezone.now())
    LessonProgress.objects.create(user=student, lesson=outline[1], percent=40)
    client.force_login(student)
    response = client.get(course.get_absolute_url())
    ctx = response.context
    assert (ctx["done"], ctx["total"], ctx["percent"]) == (1, 4, 25)
    assert ctx["next_lesson"] == outline[1]
    algebra = ctx["modules"][0]
    assert (algebra["done"], algebra["total"], algebra["status"]) == (1, 3, "progress")
    assert [r["state"] for r in algebra["topics"][0]["rows"]] == ["done", "current", "todo"]
    assert "Continue Learning" in response.content.decode()


def test_draft_course_hidden_from_students(client, student, offering):
    draft = Course.objects.create(offering=offering, title="Draft", slug="draft-course")
    client.force_login(student)
    assert client.get(draft.get_absolute_url()).status_code == 404


def test_toggle_plan_adds_and_removes(client, student, offering, course):
    client.force_login(student)
    url = reverse("courses:toggle_plan", args=[offering.pk])
    assert client.get(url).status_code == 405
    client.post(url, {"next": course.get_absolute_url()})
    assert Enrollment.objects.filter(user=student, offering=offering).exists()
    response = client.post(url, {"next": "https://evil.example/"})
    assert response.url == reverse("courses:my_subjects")
    assert not Enrollment.objects.filter(user=student).exists()


def test_my_subjects_lists_plan_with_progress(client, student, offering, course, outline):
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=outline[0], percent=100, completed_at=timezone.now())
    client.force_login(student)
    html = client.get(reverse("courses:my_subjects")).content.decode()
    assert "Test Subject" in html and "1 / 4 lessons" in html and "25%" in html


def test_continue_learning_redirects_to_latest_lesson(client, student, outline):
    client.force_login(student)
    assert client.get(reverse("courses:continue")).url == reverse("courses:my_subjects")
    LessonProgress.objects.create(user=student, lesson=outline[2], percent=10)
    assert client.get(reverse("courses:continue")).url == outline[2].get_absolute_url()


def test_course_stats_query_count_is_constant(student, course, outline, django_assert_num_queries):
    with django_assert_num_queries(2):
        stats = services.course_stats(student, [course])
    assert (stats[course.pk].done, stats[course.pk].total) == (0, 4)


def test_level_none_catalog_does_not_crash(client):
    AcademicLevel.objects.update(is_active=False)
    assert client.get(reverse("courses:catalog")).status_code == 200
