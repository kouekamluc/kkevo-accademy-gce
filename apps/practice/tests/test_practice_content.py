import pytest
from django.core.management import call_command

from apps.courses import lesson_content
from apps.courses.lesson_content.dsl import EX, H, PQ, QUIZ, S as LS, SUM, T, lesson
from apps.practice import practice_content
from apps.practice.models import Attempt, PracticeSet
from apps.practice.practice_content.dsl import MC, NUM, C, S, practice_set

KEY = ("computer-science", "form-5")
LESSON = lesson(
    module="Web Design & Publishing", topic="HTML5 structure", title="What is HTML?", slug="what-is-html",
    minutes=10, summary="Tags.", objectives=["Name tags"], key_concepts=["tag"],
    blocks=[H("Intro"), T("Hi."), EX("Ex", [LS("One")], intro="Do."), PQ("Q?", "A."),
            QUIZ("Pick", ["a", "b"], 0, "Because."), SUM("One", "Two")])


def make_set(**overrides):
    q = MC("Which tag starts a paragraph?", [C("p", correct=True), C("br", why="That is a line break.")],
           [S("Paragraphs use p")], concept="Tags", skill="Recall", hint="Think 'paragraph'.")
    base = practice_set("Web Design & Publishing", "HTML5 structure", "HTML basics", "what-is-html",
                        [q, q | {"prompt": "Second?"}, NUM("How many heading levels?", 6, [S("h1 to h6")])])
    base.update(overrides)
    return base


def test_all_practice_files_are_valid():
    assert practice_content.validate() == []


def test_validate_reports_problems(monkeypatch):
    monkeypatch.setattr(lesson_content, "collect", lambda names=None: [(KEY, LESSON, "t")])
    bad = make_set(lesson="nope", questions=[MC("Q", [C("a"), C("b")], [])])
    errors = " ".join(practice_content.validate([(KEY, bad, "t")]))
    assert "not a lesson of this topic" in errors and "at least 3" in errors
    assert "exactly one correct" in errors and "no explanation" in errors and "no worked solution" in errors


@pytest.mark.django_db
def test_load_practice_publishes_by_default_and_keeps_attempted_ones(monkeypatch, django_user_model):
    call_command("load_gce_curriculum")
    monkeypatch.setattr(lesson_content, "collect", lambda names=None: [(KEY, LESSON, "t")])
    call_command("load_lessons")
    monkeypatch.setattr(practice_content, "collect", lambda names=None: [(KEY, make_set(), "t")])
    call_command("load_practice")
    ps = PracticeSet.objects.get(title="HTML basics")
    assert ps.status == "published" and ps.lesson.slug == "what-is-html"
    assert ps.questions.count() == 3
    q = ps.questions.order_by("order").first()
    assert q.choices.filter(is_correct=True).count() == 1 and q.solution_steps[-1]["final"]
    assert ps.questions.get(kind="numeric").numeric_answer == 6

    call_command("load_practice")  # safe to re-run
    assert PracticeSet.objects.filter(title="HTML basics").count() == 1
    ps.status = "draft"  # an admin switches the set off: a refresh must not switch it back on
    ps.save()
    call_command("load_practice", "--refresh")
    ps.refresh_from_db()
    assert ps.status == "draft"

    user = django_user_model.objects.create_user(email="s@example.com", password="pw-Strong-123")
    Attempt.objects.create(user=user, practice_set=ps)
    call_command("load_practice", "--remove")  # attempted sets are never removed
    assert PracticeSet.objects.filter(title="HTML basics").exists()


@pytest.mark.django_db
def test_load_lessons_fills_course_page(monkeypatch):
    call_command("load_gce_curriculum")
    monkeypatch.setattr(lesson_content, "collect", lambda names=None: [(KEY, LESSON, "t")])
    call_command("load_lessons")
    course = lesson_content_course()
    assert course.outcomes_list and not course.summary.startswith("Outline from")


def lesson_content_course():
    from apps.courses.models import Course
    return Course.objects.get(offering__subject__slug=KEY[0], offering__level__slug=KEY[1], description="[gce-guide]")


@pytest.mark.django_db
def test_staff_can_preview_draft_sets_but_students_cannot(monkeypatch, client, django_user_model):
    call_command("load_gce_curriculum")
    monkeypatch.setattr(lesson_content, "collect", lambda names=None: [(KEY, LESSON, "t")])
    call_command("load_lessons")
    monkeypatch.setattr(practice_content, "collect", lambda names=None: [(KEY, make_set(), "t")])
    call_command("load_practice", "--draft")
    ps = PracticeSet.objects.get(title="HTML basics")
    assert ps.status == "draft"
    student = django_user_model.objects.create_user(email="st@example.com", password="pw-Strong-123")
    client.force_login(student)
    assert client.get(ps.get_absolute_url()).status_code == 404
    staff = django_user_model.objects.create_user(email="sf@example.com", password="pw-Strong-123", is_staff=True)
    client.force_login(staff)
    page = client.get(ps.get_absolute_url())
    assert page.status_code == 200 and b"Staff preview" in page.content
    assert client.post(f"/practice/sets/{ps.pk}/start/").status_code == 302
    call_command("load_practice", "--refresh")  # a staff preview attempt does not block a refresh
    assert not Attempt.objects.filter(practice_set__title="HTML basics").exists()
