import pytest
from django.contrib.auth import get_user_model
from django.db import connection
from django.test.utils import CaptureQueriesContext
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import AcademicLevel, AcademicPathway, Subject, SubjectOffering
from apps.courses.models import Course, Lesson, Module, Topic
from apps.learning.models import Enrollment, LessonProgress
from apps.practice.models import Attempt, PracticeSet, Question

pytestmark = pytest.mark.django_db
User = get_user_model()


def make_student(form5, science, email="path@example.com"):
    user = User.objects.create_user(email=email, password="pw-Strong-123", first_name="Pat")
    profile = user.profile
    profile.level, profile.pathway, profile.onboarded_at = form5, science, timezone.now()
    profile.save()
    return user


@pytest.fixture
def student(form5, science):
    return make_student(form5, science)


def add_module(course, title, order, topics):
    """topics: [(title, [(lesson title, status)])]. Returns the lessons in creation order."""
    module = Module.objects.create(course=course, title=title, order=order)
    made = []
    for t_i, (topic_title, lessons) in enumerate(topics, 1):
        topic = Topic.objects.create(module=module, title=topic_title, order=t_i)
        for l_i, (lesson_title, status) in enumerate(lessons, 1):
            slug = f"{title}-{topic_title}-{lesson_title}".lower().replace(" ", "-")
            made.append(Lesson.objects.create(topic=topic, title=lesson_title, slug=slug, order=l_i, status=status))
    return made


@pytest.fixture
def outline(course):
    """Module order is deliberately not creation order: Geometry (order 2) is created first."""
    geo = add_module(course, "Geometry", 2, [("Angles", [("Angle rules", "published")])])
    alg = add_module(course, "Algebra", 1, [
        ("Expressions", [("Expand", "published"), ("Factorise", "published"), ("Hidden draft", "draft")]),
        ("Equations", [("Solve", "published")]),
    ])
    return {"alg": alg, "geo": geo}


def finish(user, lesson):
    LessonProgress.objects.create(user=user, lesson=lesson, percent=100, completed_at=timezone.now())


def open_path(client, user, course):
    client.force_login(user)
    return client.get(reverse("courses:path", args=[course.slug]))


def steps(response):
    return [s for m in response.context["modules"] for s in m["steps"]]


def test_modules_and_steps_follow_course_order(client, student, course, outline):
    response = open_path(client, student, course)
    assert response.status_code == 200
    assert [m["module"].title for m in response.context["modules"]] == ["Algebra", "Geometry"]
    assert [(s["number"], s["topic"].title) for s in steps(response)] == [
        ("1.1", "Expressions"), ("1.2", "Equations"), ("2.1", "Angles")]
    assert [r["lesson"].title for r in steps(response)[0]["lessons"]] == ["Expand", "Factorise"]


def test_unpublished_lessons_are_hidden_and_empty_topics_dropped(client, student, course, outline):
    drafts = add_module(course, "Drafts only", 3, [("Secret topic", [("Not ready", "draft")])])
    html = open_path(client, student, course).content.decode()
    assert "Hidden draft" not in html and "Secret topic" not in html and "Drafts only" not in html
    assert drafts and "Expressions" in html


def test_unpublished_course_is_not_found(client, student, course, outline):
    course.status = "draft"
    course.save()
    assert open_path(client, student, course).status_code == 404


def test_states_and_counts(client, student, course, outline):
    expand, factorise = outline["alg"][0], outline["alg"][1]
    finish(student, expand)
    LessonProgress.objects.create(user=student, lesson=factorise, percent=40)
    response = open_path(client, student, course)
    expressions, equations, angles = steps(response)
    assert (expressions["state"], expressions["state_label"]) == ("progress", "In progress")
    assert (expressions["stat"].done, expressions["stat"].total) == (1, 2)
    assert (equations["state"], angles["state"]) == ("todo", "todo")
    assert equations["state_label"] == "Not started"
    algebra = response.context["modules"][0]
    assert (algebra["stat"].done, algebra["stat"].total, algebra["stat"].percent) == (1, 3, 33)
    assert algebra["state"] == "progress" and response.context["modules"][1]["state"] == "todo"
    assert response.context["stat"].total == 4  # the draft lesson is not counted


def test_step_and_module_done_when_all_lessons_done(client, student, course, outline):
    for lesson in outline["alg"][:2]:
        finish(student, lesson)
    response = open_path(client, student, course)
    assert steps(response)[0]["state"] == "done" and steps(response)[0]["state_label"] == "Done"
    assert response.context["modules"][0]["state"] == "progress"  # Equations is still to do


def test_continue_here_is_first_lesson_for_new_student(client, student, course, outline):
    response = open_path(client, student, course)
    assert response.context["next_lesson"] == outline["alg"][0]
    assert response.context["current_step"]["topic"].title == "Expressions"
    assert response.context["started"] is False
    html = response.content.decode()
    assert "Start here" in html and "You are here" in html


def test_continue_here_follows_the_most_recent_unfinished_lesson(client, student, course, outline):
    finish(student, outline["alg"][0])
    LessonProgress.objects.create(user=student, lesson=outline["geo"][0], percent=30)
    response = open_path(client, student, course)
    assert response.context["next_lesson"] == outline["geo"][0]
    assert response.context["current_step"]["topic"].title == "Angles"
    assert response.context["modules"][1]["is_open"] and not response.context["modules"][0]["is_open"]
    assert "Continue here" in response.content.decode()


def test_continue_here_matches_the_course_page(client, student, course, outline):
    finish(student, outline["alg"][0])
    path = open_path(client, student, course)
    detail = client.get(reverse("courses:detail", args=[course.slug]))
    assert path.context["next_lesson"] == detail.context["next_lesson"]


def test_completed_course_has_no_continue_step(client, student, course, outline):
    for lesson in [*outline["alg"][:2], outline["alg"][3], outline["geo"][0]]:
        finish(student, lesson)
    response = open_path(client, student, course)
    assert response.context["is_complete"] and response.context["next_lesson"] is None
    assert response.context["current_step"] is None
    assert all(s["state"] == "done" for s in steps(response))
    assert "Course complete" in response.content.decode()


def test_practice_mastery_shown_per_step(client, student, course, outline):
    expressions = outline["alg"][0].topic
    practice = PracticeSet.objects.create(topic=expressions, title="Set", status="published")
    Question.objects.create(practice_set=practice, prompt="Q?")
    for _ in range(2):
        Attempt.objects.create(user=student, practice_set=practice, correct_count=9, total=10, completed_at=timezone.now())
    response = open_path(client, student, course)
    first, second, _ = steps(response)
    assert first["mastery"].key == "mastered" and first["show_mastery"]
    assert first["practice_set"] == practice
    assert second["mastery"].key == "not_started" and not second["show_mastery"]
    assert "Practice: Mastered" in response.content.decode()


def test_draft_practice_set_is_not_offered(client, student, course, outline):
    practice = PracticeSet.objects.create(topic=outline["alg"][0].topic, title="Draft set", status="draft")
    Question.objects.create(practice_set=practice, prompt="Q?")
    assert steps(open_path(client, student, course))[0]["practice_set"] is None


def test_progress_of_other_students_is_ignored(client, student, form5, science, course, outline):
    other = make_student(form5, science, email="other@example.com")
    finish(other, outline["alg"][0])
    assert steps(open_path(client, student, course))[0]["state"] == "todo"


# ---- access ----

def test_anonymous_is_sent_to_login(client, course, outline):
    response = client.get(reverse("courses:path", args=[course.slug]))
    assert response.status_code == 302 and "/login" in response.url


def test_other_class_subject_redirects_to_public_course_page(client, student, course, outline):
    upper = AcademicLevel.objects.exclude(pk=student.profile.level_id).first()
    subject = Subject.objects.create(name="Elsewhere", slug="elsewhere", icon_text="E")
    other_course = Course.objects.create(offering=SubjectOffering.objects.create(subject=subject, level=upper),
                                         title="Elsewhere", slug="elsewhere-course", status="published")
    add_module(other_course, "M", 1, [("T", [("L", "published")])])
    response = open_path(client, student, other_course)
    assert response.status_code == 302 and response.url == other_course.get_absolute_url()


def test_other_stream_subject_redirects_but_enrolment_allows_it(client, student, course, outline):
    arts = AcademicPathway.objects.get(slug="arts")
    subject = Subject.objects.create(name="History", slug="history", icon_text="H")
    offering = SubjectOffering.objects.create(subject=subject, level=student.profile.level)
    offering.pathways.add(arts)
    arts_course = Course.objects.create(offering=offering, title="History", slug="history-course", status="published")
    add_module(arts_course, "M", 1, [("T", [("L", "published")])])
    assert open_path(client, student, arts_course).status_code == 302
    Enrollment.objects.create(user=student, offering=offering)
    assert open_path(client, student, arts_course).status_code == 200


def test_common_to_all_streams_subject_is_allowed(client, student, form5):
    subject = Subject.objects.create(name="English", slug="english", icon_text="En")
    offering = SubjectOffering.objects.create(subject=subject, level=form5)  # no stream set
    english = Course.objects.create(offering=offering, title="English", slug="english-course", status="published")
    add_module(english, "M", 1, [("T", [("L", "published")])])
    assert open_path(client, student, english).status_code == 200


# ---- links ----

def test_course_page_and_dashboard_link_to_the_path(client, student, course, outline):
    client.force_login(student)
    path_url = reverse("courses:path", args=[course.slug])
    assert path_url in client.get(reverse("courses:detail", args=[course.slug])).content.decode()
    LessonProgress.objects.create(user=student, lesson=outline["alg"][0], percent=20)
    Enrollment.objects.create(user=student, offering=course.offering)
    assert path_url in client.get(reverse("dashboard:home")).content.decode()


# ---- performance ----

def count_queries(client, student, course):
    client.force_login(student)
    with CaptureQueriesContext(connection) as ctx:
        assert client.get(reverse("courses:path", args=[course.slug])).status_code == 200
    return len(ctx)


def test_query_count_is_small_and_does_not_grow_with_course_size(client, student, course, outline):
    finish(student, outline["alg"][0])
    small = count_queries(client, student, course)
    for n in range(6):
        made = add_module(course, f"Extra {n}", 10 + n, [(f"Topic {n}a", [("A", "published"), ("B", "published")]),
                                                         (f"Topic {n}b", [("C", "published")])])
        practice = PracticeSet.objects.create(topic=made[0].topic, title=f"Set {n}", status="published")
        Question.objects.create(practice_set=practice, prompt="Q?")
        LessonProgress.objects.create(user=student, lesson=made[0], percent=50)
        Attempt.objects.create(user=student, practice_set=practice, correct_count=5, total=10, completed_at=timezone.now())
    large = count_queries(client, student, course)
    assert large == small
    assert large <= 22  # session, user, layout, access check and the page's own few queries
