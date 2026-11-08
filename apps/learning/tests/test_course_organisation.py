"""Course organisation rules: which subjects students are offered, one live course per subject, and moving up a year."""

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.urls import reverse
from django.utils import timezone

from apps.academics.models import AcademicLevel, Subject, SubjectOffering
from apps.accounts.models import StudentProfile
from apps.courses.models import Course, Lesson, Module, Topic
from apps.learning import promotion
from apps.learning.models import Enrollment, LessonProgress

pytestmark = pytest.mark.django_db
User = get_user_model()


def build(subject, level, science, lessons=(("Module A", "Topic A", "lesson-a"),), status="published", lesson_status="published"):
    """An offering of `subject` at `level` with one course holding the given (module, topic, slug) lessons."""
    offering = SubjectOffering.objects.create(subject=subject, level=level)
    offering.pathways.add(science)
    course = Course.objects.create(offering=offering, title=f"{subject.name} {level.code}", slug=f"{subject.slug}-{level.code.lower()}", status=status)
    modules, topics = {}, {}
    for order, (module_title, topic_title, slug) in enumerate(lessons, 1):
        if module_title not in modules:
            modules[module_title] = Module.objects.create(course=course, title=module_title, order=len(modules) + 1)
        module = modules[module_title]
        if (module_title, topic_title) not in topics:
            topics[(module_title, topic_title)] = Topic.objects.create(module=module, title=topic_title, order=len(topics) + 1)
        topic = topics[(module_title, topic_title)]
        Lesson.objects.create(topic=topic, title=slug.replace("-", " ").title(), slug=slug, order=order, status=lesson_status)
    return offering


def subject(name):
    return Subject.objects.create(name=name, slug=name.lower().replace(" ", "-"), icon_text=name[:2])


@pytest.fixture
def levels(db):
    return {code: AcademicLevel.objects.get(code=code) for code in ("F5", "L6", "U6")}


@pytest.fixture
def student(db, levels, science):
    user = User.objects.create_user(email="org@example.com", password="pw-Strong-123", first_name="Ola")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = levels["F5"], science, timezone.now()
    p.save()
    return user


# ------------------------------------------------------------------ Fix 1: only offer subjects with content

def test_with_content_needs_a_published_course_with_a_published_lesson(levels, science):
    ready = build(subject("Maths"), levels["F5"], science)
    build(subject("Draft course"), levels["F5"], science, status="draft")
    build(subject("Draft lesson"), levels["F5"], science, lesson_status="draft")
    no_course = SubjectOffering.objects.create(subject=subject("Empty"), level=levels["F5"])
    no_course.pathways.add(science)
    assert list(SubjectOffering.objects.with_content()) == [ready]


def test_onboarding_lists_only_subjects_with_lessons_and_names_the_rest(client, student, levels, science):
    build(subject("Maths"), levels["F5"], science)
    soon = SubjectOffering.objects.create(subject=subject("Geology"), level=levels["F5"])
    soon.pathways.add(science)
    client.force_login(student)
    html = client.get(reverse("accounts:onboarding_subjects")).content.decode()
    assert 'name="offerings"' in html and "Maths" in html
    assert "Coming soon:" in html and "Geology" in html
    assert html.count('name="offerings"') == 1  # Geology is not selectable


def test_add_all_and_suggestions_skip_empty_subjects(client, student, levels, science):
    ready = build(subject("Maths"), levels["F5"], science)
    soon = SubjectOffering.objects.create(subject=subject("Geology"), level=levels["F5"])
    soon.pathways.add(science)
    client.force_login(student)
    page = client.get(reverse("courses:my_subjects"))
    assert [o.pk for o in page.context["suggestions"]] == [ready.pk] and page.context["coming_soon"] == ["Geology"]
    client.post(reverse("courses:add_class_subjects"))
    assert set(Enrollment.objects.filter(user=student).values_list("offering_id", flat=True)) == {ready.pk}


def test_catalog_lists_subjects_with_lessons_before_coming_soon(client, student, levels, science):
    soon = SubjectOffering.objects.create(subject=subject("Aardvark studies"), level=levels["F5"])  # sorts first by name
    soon.pathways.add(science)
    build(subject("Zoology"), levels["F5"], science)
    client.force_login(student)
    cards = client.get(reverse("courses:catalog"), {"sort": "name"}).context["cards"]
    assert [c["subject"].name for c in cards] == ["Zoology", "Aardvark studies"]


# ------------------------------------------------------------------ Fix 2: one published course per subject

def test_only_one_course_of_a_subject_can_be_published(levels, science):
    offering = build(subject("Physics"), levels["F5"], science)
    with pytest.raises(IntegrityError), transaction.atomic():
        Course.objects.create(offering=offering, title="Physics stub", slug="physics-stub", status="published")
    Course.objects.create(offering=offering, title="Physics draft", slug="physics-draft", status="draft")
    Course.objects.create(offering=offering, title="Physics old", slug="physics-old", status="archived")


def test_publishing_a_second_course_shows_a_friendly_error(levels, science):
    offering = build(subject("Physics"), levels["F5"], science)
    second = Course(offering=offering, title="Physics 2", slug="physics-2", status="published")
    with pytest.raises(ValidationError) as error:
        second.full_clean()
    assert "already published" in str(error.value)


# ------------------------------------------------------------------ Fix 3 and 4: moving up a year

SAME = (("Core", "Algebra", "algebra-basics"), ("Core", "Algebra", "quadratics"), ("Core", "Calculus", "limits"))


def test_next_level_follows_the_order_and_ends_at_upper_sixth(levels):
    assert promotion.next_level(levels["F5"]) == levels["L6"]
    assert promotion.next_level(levels["L6"]) == levels["U6"]
    assert promotion.next_level(levels["U6"]) is None and promotion.next_level(None) is None


def test_move_up_switches_class_keeps_continuing_subjects_and_carries_progress(student, levels, science):
    maths_l6 = build(subject("Pure Maths"), levels["L6"], science, lessons=SAME)
    maths_u6 = build(Subject.objects.get(name="Pure Maths"), levels["U6"], science, lessons=SAME)  # same lessons: shared "Core Pure"
    physics_l6 = build(subject("Physics"), levels["L6"], science, lessons=(("Mechanics", "Forces", "forces"),))
    build(Subject.objects.get(name="Physics"), levels["U6"], science, lessons=(("Fields", "Gravity", "gravity"),))  # different year-2 content
    history_l6 = build(subject("History"), levels["L6"], science)  # no Upper Sixth course: the subject ends
    student.profile.level = levels["L6"]
    student.profile.save()
    for offering in (maths_l6, physics_l6, history_l6):
        Enrollment.objects.create(user=student, offering=offering)
    done = Lesson.objects.get(topic__module__course__offering=maths_l6, slug="quadratics")
    LessonProgress.objects.create(user=student, lesson=done, percent=100, completed_at=timezone.now())
    forces = Lesson.objects.get(topic__module__course__offering=physics_l6, slug="forces")
    LessonProgress.objects.create(user=student, lesson=forces, percent=100, completed_at=timezone.now())

    plan = promotion.plan_move_up(student)
    assert plan.target == levels["U6"]
    assert {m.old.subject.name for m in plan.continuing} == {"Pure Maths", "Physics"}
    assert [m.old.subject.name for m in plan.ending] == ["History"]
    assert plan.carried_count == 1  # only the identical Pure Maths lesson carries over

    promotion.move_up(student)
    student.profile.refresh_from_db()
    assert student.profile.level == levels["U6"]
    assert set(Enrollment.objects.filter(user=student).values_list("offering__level__code", "offering__subject__name")) == {
        ("U6", "Pure Maths"), ("U6", "Physics")}
    carried = LessonProgress.objects.get(user=student, lesson__topic__module__course__offering=maths_u6, lesson__slug="quadratics")
    assert carried.completed_at is not None and carried.percent == 100
    assert not LessonProgress.objects.filter(user=student, lesson__slug="gravity").exists()  # Physics year 2 starts fresh
    assert LessonProgress.objects.filter(user=student, lesson=done).exists()  # nothing from last year is deleted


def test_the_final_year_has_nothing_to_move_up_to(student, levels):
    student.profile.level = levels["U6"]
    student.profile.save()
    assert promotion.plan_move_up(student) is None and promotion.move_up(student) is None


def test_move_up_page_confirms_first_then_moves(client, student, levels, science):
    maths_f5 = build(subject("English"), levels["F5"], science)
    build(Subject.objects.get(name="English"), levels["L6"], science)
    Enrollment.objects.create(user=student, offering=maths_f5)
    client.force_login(student)
    page = client.get(reverse("accounts:move_up"))
    assert "Move up to Lower Sixth?" in page.content.decode() and "English" in page.content.decode()
    assert StudentProfile.objects.get(user=student).level == levels["F5"]  # a GET changes nothing
    response = client.post(reverse("accounts:move_up"))
    assert response.url == reverse("courses:my_subjects")
    assert StudentProfile.objects.get(user=student).level == levels["L6"]


def test_profile_offers_the_move_up_link_except_in_the_final_year(client, student, levels):
    client.force_login(student)
    assert "Move up to Lower Sixth" in client.get(reverse("accounts:profile")).content.decode()
    student.profile.level = levels["U6"]
    student.profile.save()
    assert "Move up to" not in client.get(reverse("accounts:profile")).content.decode()
    assert client.get(reverse("accounts:move_up")).url == reverse("accounts:profile")


def test_course_overlap_report_finds_copied_lessons_but_not_a_real_year_split(levels, science):
    from apps.courses.management.commands.check_course_overlap import find_overlaps

    maths = subject("Pure Maths")
    build(maths, levels["L6"], science, lessons=SAME)
    build(maths, levels["U6"], science, lessons=SAME)  # a copy
    physics = subject("Physics")
    build(physics, levels["L6"], science, lessons=(("Mechanics", "Forces", "forces"),))
    build(physics, levels["U6"], science, lessons=(("Fields", "Gravity", "gravity"),))  # a real second year
    overlaps = find_overlaps()
    assert [(o[0].name, o[3], o[4]) for o in overlaps] == [("Pure Maths", 3, 3)]
