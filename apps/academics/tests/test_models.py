import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from apps.academics.models import (
    AcademicLevel,
    AcademicPathway,
    CurriculumReference,
    Subject,
    SubjectOffering,
    Syllabus,
)

pytestmark = pytest.mark.django_db


def test_levels_and_pathways_are_seeded_in_order():
    assert list(AcademicLevel.objects.values_list("code", flat=True)) == ["F5", "L6", "U6"]
    assert list(AcademicPathway.objects.values_list("name", flat=True)) == ["Science", "Arts"]


def test_subject_offered_once_per_level(subject, form5):
    SubjectOffering.objects.create(subject=subject, level=form5)
    with pytest.raises(IntegrityError), transaction.atomic():
        SubjectOffering.objects.create(subject=subject, level=form5)


def test_subject_requires_icon_text_or_icon():
    with pytest.raises(ValidationError):
        Subject(name="Blank", slug="blank").full_clean()
    Subject(name="Bio", slug="bio", icon="dna").full_clean()


def test_offering_queryset_active_excludes_inactive_subject(offering, subject):
    assert SubjectOffering.objects.active().count() == 1
    subject.is_active = False
    subject.save()
    assert SubjectOffering.objects.active().count() == 0


def test_card_meta_summarises_pathways_and_levels(offering, subject):
    assert subject.card_meta() == "Science · Form 5"
    lower_sixth = AcademicLevel.objects.get(code="L6")
    other = SubjectOffering.objects.create(subject=subject, level=lower_sixth)
    other.pathways.add(AcademicPathway.objects.get(slug="arts"))
    assert subject.card_meta() == "Science & Arts · 2 levels"


def test_syllabus_versions_unique_and_dates_validated(offering):
    Syllabus.objects.create(offering=offering, title="Syllabus", version="v1")
    with pytest.raises(IntegrityError), transaction.atomic():
        Syllabus.objects.create(offering=offering, title="Syllabus", version="v1")
    import datetime

    bad = Syllabus(
        offering=offering,
        title="S",
        version="v2",
        effective_from=datetime.date(2025, 1, 1),
        effective_to=datetime.date(2024, 1, 1),
    )
    with pytest.raises(ValidationError):
        bad.full_clean()


def test_curriculum_reference_parent_must_share_syllabus(offering):
    s1 = Syllabus.objects.create(offering=offering, title="S", version="v1")
    s2 = Syllabus.objects.create(offering=offering, title="S", version="v2")
    parent = CurriculumReference.objects.create(syllabus=s1, code="1", title="Section")
    child = CurriculumReference(syllabus=s2, parent=parent, code="1.1", title="Item")
    with pytest.raises(ValidationError):
        child.full_clean()
