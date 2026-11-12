from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import Subject, SubjectOffering
from apps.courses.models import Course, Lesson, Module, Topic
from apps.learning.models import Enrollment, LessonProgress
from apps.practice.models import Answer, Attempt, Choice, PracticeSet, Question
from apps.practice.suggestions import practice_today

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="pt@example.com", password="pw-Strong-123", first_name="Pat")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


def make_subject(student, form5, science, name, order, topics=2):
    """A published course with `topics` topics, each with a one-lesson, two-question practice set."""
    subject = Subject.objects.create(name=name, slug=name.lower(), icon_text=name[:2], order=order)
    offering = SubjectOffering.objects.create(subject=subject, level=form5)
    offering.pathways.add(science)
    Enrollment.objects.create(user=student, offering=offering)
    course = Course.objects.create(offering=offering, title=f"{name} course", slug=f"{name.lower()}-course", status="published")
    module = Module.objects.create(course=course, title="Module", order=1)
    sets = []
    for t in range(topics):
        topic = Topic.objects.create(module=module, title=f"{name} topic {t + 1}", order=t + 1)
        lesson = Lesson.objects.create(topic=topic, title=f"{name} lesson {t + 1}", slug=f"{name.lower()}-l{t + 1}", order=1, status="published")
        pset = PracticeSet.objects.create(topic=topic, lesson=lesson, title=f"{name} set {t + 1}", status="published", order=t + 1)
        for q in range(2):
            question = Question.objects.create(practice_set=pset, prompt=f"Q{q}?", order=q)
            Choice.objects.create(question=question, text="Right", is_correct=True, order=0)
            Choice.objects.create(question=question, text="Wrong", is_correct=False, order=1)
        sets.append(pset)
    return subject, sets


def take(student, pset, right, when=None):
    """Finish an attempt with `right` of its two questions correct."""
    attempt = Attempt.objects.create(user=student, practice_set=pset)
    for i, question in enumerate(pset.questions.order_by("order")):
        choice = question.choices.get(is_correct=i < right)
        Answer.objects.create(attempt=attempt, question=question, choice=choice, is_correct=choice.is_correct)
    attempt.finish()
    if when:
        Attempt.objects.filter(pk=attempt.pk).update(completed_at=when)
    return attempt


def test_one_suggestion_per_subject(student, form5, science):
    make_subject(student, form5, science, "Maths", 1)
    make_subject(student, form5, science, "Physics", 2)
    items = practice_today(student)
    assert sorted(i.subject.name for i in items) == ["Maths", "Physics"]
    assert all(i.days_since is None and i.last_label == "Not practised yet" for i in items)


def test_weakest_topic_is_suggested_first_within_a_subject(student, form5, science):
    _, (first, second) = make_subject(student, form5, science, "Maths", 1)
    take(student, first, right=2)   # 100%: proficient
    take(student, second, right=0)  # 0%: attempted, needs another go
    (item,) = practice_today(student)
    assert item.practice_set == second
    assert "0% last time" in item.reason


def test_finished_lesson_beats_a_plain_new_topic(student, form5, science):
    _, (first, second) = make_subject(student, form5, science, "Maths", 1)
    LessonProgress.objects.create(user=student, lesson=second.lesson, percent=100, completed_at=timezone.now())
    (item,) = practice_today(student)
    assert item.practice_set == second and "just learned" in item.reason


def test_most_neglected_subject_comes_first_and_mastered_goes_last(student, form5, science):
    _, (maths_set,) = make_subject(student, form5, science, "Maths", 1, topics=1)
    _, (phys_set,) = make_subject(student, form5, science, "Physics", 2, topics=1)
    _, (chem_set,) = make_subject(student, form5, science, "Chemistry", 3, topics=1)
    now = timezone.now()
    take(student, maths_set, right=1, when=now - timedelta(days=2))   # 50%: attempted, practised 2 days ago
    take(student, phys_set, right=1, when=now - timedelta(days=9))    # practised 9 days ago
    for days in (6, 5):                                               # chemistry mastered (80%+ twice)
        take(student, chem_set, right=2, when=now - timedelta(days=days))
    items = practice_today(student)
    assert [i.subject.name for i in items] == ["Physics", "Maths", "Chemistry"]
    assert items[0].days_since == 9 and items[0].last_label == "Last practised 9 days ago"


def test_other_students_subjects_and_drafts_are_ignored(student, form5, science, django_user_model):
    _, (pset,) = make_subject(student, form5, science, "Maths", 1, topics=1)
    other = django_user_model.objects.create_user(email="o@example.com", password="pw-Strong-123")
    assert practice_today(other) == []
    PracticeSet.objects.filter(pk=pset.pk).update(status="draft")
    assert practice_today(student) == []


def test_dashboard_and_practice_page_show_practice_today(client, student, form5, science):
    _, (maths_set,) = make_subject(student, form5, science, "Maths", 1, topics=1)
    _, (phys_set,) = make_subject(student, form5, science, "Physics", 2, topics=1)
    client.force_login(student)
    # A new student has started nothing: the dashboard stays quiet, the Practice page already suggests sets.
    assert "Practice today" not in client.get(reverse("dashboard:home")).content.decode()
    page = client.get(reverse("practice:index")).content.decode()
    assert "Practice today" in page and "Maths set 1" in page and "Physics set 1" in page and "Practice by subject" in page
    # Once they have started a lesson, the dashboard shows the strip too.
    LessonProgress.objects.create(user=student, lesson=maths_set.lesson, percent=40)
    home = client.get(reverse("dashboard:home"))
    assert "Practice today" in home.content.decode() and len(home.context["practice_shown"]) == 2
