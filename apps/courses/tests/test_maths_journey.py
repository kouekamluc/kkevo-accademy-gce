"""End-to-end student journey through Form 5 General Mathematics, on the real course content.

Loads the GCE outline and KKEVO's maths lessons and practice sets, publishes them (as a reviewer
would), then walks one student from the dashboard to a mock exam:
dashboard → course page → lesson → its practice set → results → next lesson → mastery → mock
exam → score by topic → progress page.
"""

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import AcademicLevel, SubjectOffering
from apps.courses.models import Course, Lesson
from apps.learning.models import Enrollment
from apps.practice.mastery import mastery_for_topic
from apps.practice.models import Attempt, PracticeSet

pytestmark = pytest.mark.django_db
MATHS = "mathematics:form-5"


@pytest.fixture
def maths(db):
    call_command("load_gce_curriculum")
    offering = SubjectOffering.objects.get(subject__slug="mathematics", level__slug="form-5")
    # An older published course on the same offering (like the demo course) must not hide the new one.
    old = offering.courses.get()
    old.description, old.title, old.slug, old.status = "[sample]", "Form 5 Mathematics", "form-5-mathematics", "published"
    old.save()
    call_command("load_lessons", "--only", MATHS)
    call_command("load_practice", "--only", MATHS)
    # Everything loads published by default; nothing is switched on by hand here.
    return Course.objects.get(offering=offering, description="[gce-guide]")


@pytest.fixture
def student(maths):
    user = get_user_model().objects.create_user(email="ama@example.com", password="pw-Strong-123", first_name="Ama")
    profile = user.profile
    profile.level = AcademicLevel.objects.get(slug="form-5")
    profile.onboarded_at = timezone.now()
    profile.save()
    Enrollment.objects.create(user=user, offering=maths.offering)
    return user


def answer_all(client, attempt, correct):
    """Answer every question of an attempt; `correct(index)` says whether to answer question index right."""
    questions = list(attempt.practice_set.questions.order_by("order", "pk").prefetch_related("choices"))
    for n, q in enumerate(questions, 1):
        url = reverse("practice:question", args=[attempt.pk, n])
        right = correct(n - 1)
        if q.is_numeric:
            data = {"value": str(q.numeric_answer if right else q.numeric_answer + 1000)}
        else:
            data = {"choice": next(c.pk for c in q.choices.all() if c.is_correct == right)}
        client.post(url, data)
    finish = reverse("practice:finish", args=[attempt.pk])
    return client.post(finish, follow=True) if attempt.is_exam else client.get(finish)


def start(client, practice_set, mode="practice"):
    client.post(reverse("practice:start", args=[practice_set.pk]), {"mode": mode} if mode == "exam" else {})
    return Attempt.objects.filter(practice_set=practice_set).latest("started_at")


@pytest.mark.parametrize("subject, min_topics, min_mocks", [
    ("mathematics", 15, 2), ("additional-mathematics", 8, 2), ("computer-science", 5, 2), ("ict", 7, 2),
    ("history", 7, 1),  # History essays cannot be auto-marked, so it has a Paper 1 mock only
    ("geography", 35, 2), ("logic", 50, 2),
    ("pure-mathematics-with-mechanics", 10, 2), ("pure-mathematics-with-statistics", 10, 2)])
def test_o_level_courses_have_lessons_practice_and_mocks_for_every_topic(db, subject, min_topics, min_mocks):
    level = "lower-sixth" if subject.startswith("pure-mathematics") else "form-5"
    call_command("load_gce_curriculum")
    call_command("load_lessons", "--only", f"{subject}:{level}")
    call_command("load_practice", "--only", f"{subject}:{level}")
    course = Course.objects.get(offering__subject__slug=subject, offering__level__slug=level,
                                description="[gce-guide]")
    topics = [t for m in course.modules.all() for t in m.topics.all()]
    assert len(topics) >= min_topics + 2  # syllabus topics plus the Examination papers
    for topic in topics:
        lessons = list(topic.lessons.all())
        assert lessons, f"{topic.title} has no lessons"
        for lesson in lessons:
            assert PracticeSet.objects.filter(lesson=lesson).exists(), f"{lesson.slug} has no practice set"
    mocks = PracticeSet.objects.filter(topic__module__course=course, is_mock=True)
    assert mocks.count() >= min_mocks and all(m.time_limit_minutes for m in mocks)


def test_student_journey_from_dashboard_to_mock_exam(client, student, maths):
    client.force_login(student)

    # 1. The dashboard and My Subjects lead to the new course, not the older one.
    assert maths.get_absolute_url() in client.get(reverse("dashboard:home")).content.decode()
    assert maths.get_absolute_url() in client.get(reverse("courses:my_subjects")).content.decode()

    # 2. The course page lists lessons, a practice set under each topic, and the mock exams.
    page = client.get(maths.get_absolute_url()).content.decode()
    first = Lesson.objects.filter(topic__module__course=maths).order_by(
        "topic__module__order", "topic__order", "order", "pk").first()
    own_set = PracticeSet.objects.get(lesson=first)
    assert first.get_absolute_url() in page and own_set.get_absolute_url() in page
    assert "Mock exams" in page

    # 3. The lesson links to its own practice set, and completing it moves on to the next lesson.
    lesson_page = client.get(first.get_absolute_url()).content.decode()
    assert own_set.get_absolute_url() in lesson_page
    done = client.post(reverse("courses:lesson_complete", args=[maths.slug, first.pk]))
    assert done.status_code == 302

    # 4. Practice: all right → results offer the next lesson; twice at 80%+ → topic mastered.
    attempt = start(client, own_set)
    results = answer_all(client, attempt, correct=lambda i: True).content.decode()
    second = Lesson.objects.filter(topic__module__course=maths).order_by(
        "topic__module__order", "topic__order", "order", "pk")[1]
    assert "Next lesson" in results and second.get_absolute_url() in results
    answer_all(client, start(client, own_set), correct=lambda i: True)
    assert mastery_for_topic(student, own_set.topic_id).label == "Mastered"

    # 5. Paper 1 mock: timed by its own limit, results broken down by topic with revise links.
    paper1 = PracticeSet.objects.get(topic__module__course=maths, is_mock=True, time_limit_minutes=90)
    assert "90 minutes" in client.get(paper1.get_absolute_url()).content.decode()
    exam = start(client, paper1, mode="exam")
    assert exam.is_exam and exam.time_limit_seconds == 90 * 60
    results = answer_all(client, exam, correct=lambda i: i % 3 != 0)
    body = results.content.decode()
    assert results.status_code == 200 and "Your score by topic" in body and "Revise" in body

    # 6. Mock papers do not count as topic mastery, and the progress page still works.
    assert mastery_for_topic(student, paper1.topic_id).label == "Not started"
    assert client.get(reverse("learning:progress")).status_code == 200
    assert client.get(reverse("practice:index")).status_code == 200


@pytest.mark.parametrize("subject, level, min_topics", [
    ("computer-science", "lower-sixth", 13), ("computer-science", "upper-sixth", 9),
    ("ict", "lower-sixth", 7), ("ict", "upper-sixth", 6),
    ("history", "lower-sixth", 9), ("history", "upper-sixth", 9)])
def test_a_level_courses_have_depth_practice_and_a_practice_paper(db, subject, level, min_topics):
    call_command("load_gce_curriculum")
    call_command("load_lessons", "--only", f"{subject}:{level}")
    call_command("load_practice", "--only", f"{subject}:{level}")
    course = Course.objects.get(offering__subject__slug=subject, offering__level__slug=level,
                                description="[gce-guide]")
    topics = [t for m in course.modules.all() for t in m.topics.all()]
    assert len(topics) >= min_topics + 1  # syllabus topics plus the practice paper
    for topic in topics:
        lessons = list(topic.lessons.all())
        assert lessons, f"{topic.title} has no lessons"
        for lesson in lessons:
            assert PracticeSet.objects.filter(lesson=lesson).exists(), f"{lesson.slug} has no practice set"
    mocks = PracticeSet.objects.filter(topic__module__course=course, is_mock=True)
    assert mocks.count() >= 1 and all(m.time_limit_minutes for m in mocks)
