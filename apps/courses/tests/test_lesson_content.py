import pytest
from django.core.management import call_command

from apps.courses import lesson_content
from apps.courses.lesson_content.dsl import EX, H, PQ, QUIZ, S, SUM, T, lesson
from apps.courses.models import Course, Lesson

KEY = ("computer-science", "form-5")


def spec(**overrides):
    base = lesson(
        module="Web Design & Publishing", topic="HTML5 structure", title="What is HTML?", slug="what-is-html",
        minutes=10, summary="Tags and elements.", objectives=["Name the parts of an element"], key_concepts=["tag"],
        blocks=[H("Intro"), T("Hello."), EX("Example", [S("One"), S("Two")], intro="Do it."), PQ("Q?", "A."),
                QUIZ("Pick", ["a", "b"], 1, "Because b."), SUM("Point one", "Point two")])
    base.update(overrides)
    return base


def test_all_content_files_are_valid():
    """Every lesson file must match the syllabus outline and produce valid blocks."""
    assert lesson_content.validate() == []


def test_validate_reports_problems():
    bad = spec(topic="Nope", slug="Bad Slug", objectives=[],
               blocks=[QUIZ("Pick", ["a", "b"], 5, ""), PQ("Q?", "")])
    errors = " ".join(lesson_content.validate([(KEY, bad, "test")]))
    assert "topic 'Nope'" in errors and "slug must be" in errors and "no learning objectives" in errors
    assert "valid choice index" in errors and "no explanation" in errors and "no answer" in errors


@pytest.mark.django_db
def test_load_lessons_creates_drafts_and_is_safe_to_rerun(monkeypatch):
    call_command("load_gce_curriculum")
    monkeypatch.setattr(lesson_content, "collect", lambda: [(KEY, spec(), "test")])
    call_command("load_lessons")
    lesson_obj = Lesson.objects.get(slug="what-is-html")
    assert lesson_obj.status == "draft" and lesson_obj.author is None
    assert lesson_obj.blocks.count() == 6
    assert lesson_obj.curriculum_references.exists()
    assert lesson_obj.course.description == "[gce-guide]"

    call_command("load_lessons")  # second run keeps the lesson
    assert Lesson.objects.filter(slug="what-is-html").count() == 1

    monkeypatch.setattr(lesson_content, "collect", lambda: [(KEY, spec(title="Changed"), "test")])
    call_command("load_lessons", "--refresh")
    assert Lesson.objects.get(slug="what-is-html").title == "Changed"

    lesson_obj = Lesson.objects.get(slug="what-is-html")
    lesson_obj.status = "published"
    lesson_obj.save()
    call_command("load_lessons", "--remove")  # published lessons are never removed
    assert Lesson.objects.filter(slug="what-is-html").exists()


@pytest.mark.django_db
def test_load_lessons_creates_outline_when_offering_has_another_course(monkeypatch, offering):
    call_command("load_gce_curriculum")
    maths = ("mathematics", "form-5")
    from apps.academics.models import SubjectOffering
    off = SubjectOffering.objects.get(subject__slug="mathematics", level__slug="form-5")
    course = off.courses.get()
    course.description = "[sample]"  # pretend the demo course got there first
    course.save()
    monkeypatch.setattr(lesson_content, "collect", lambda: [(maths, spec(
        module="Set Theory & Logic", topic="Venn diagrams", slug="venn"), "test")])
    call_command("load_lessons")
    assert Course.objects.filter(offering=off, description="[gce-guide]").exists()
    assert Lesson.objects.get(slug="venn").course.description == "[gce-guide]"
