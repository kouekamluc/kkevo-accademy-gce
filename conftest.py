import pytest

from apps.academics.models import AcademicLevel, AcademicPathway, Subject, SubjectOffering
from apps.courses.models import Course, Lesson, Module, Topic


@pytest.fixture
def form5(db):
    return AcademicLevel.objects.get(code="F5")  # seeded by migration


@pytest.fixture
def science(db):
    return AcademicPathway.objects.get(slug="science")  # seeded by migration


@pytest.fixture
def subject(db):
    return Subject.objects.create(name="Test Subject", slug="test-subject", icon_text="Ts", is_featured=True)


@pytest.fixture
def offering(subject, form5, science):
    offering = SubjectOffering.objects.create(subject=subject, level=form5)
    offering.pathways.add(science)
    return offering


@pytest.fixture
def course(offering):
    return Course.objects.create(offering=offering, title="Test Course", slug="test-course", status="published")


@pytest.fixture
def lesson(course):
    module = Module.objects.create(course=course, title="Module A", order=1)
    topic = Topic.objects.create(module=module, title="Topic A", order=1)
    return Lesson.objects.create(topic=topic, title="Lesson A", slug="lesson-a", order=1)
