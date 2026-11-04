import pytest
from django.core.management import CommandError, call_command

from apps.academics import gce_curriculum as data
from apps.academics.models import CurriculumReference, Subject, SubjectOffering, Syllabus
from apps.courses.models import Course, Topic

pytestmark = pytest.mark.django_db


def test_loads_subjects_offerings_and_draft_syllabi():
    call_command("load_gce_curriculum")
    assert Subject.objects.count() == len(data.SUBJECTS)
    assert SubjectOffering.objects.count() == sum(len(row[7]) for row in data.SUBJECTS)
    assert Syllabus.objects.count() == len(data.SYLLABI)
    assert not Syllabus.objects.filter(is_official=True).exists()
    assert not Syllabus.objects.exclude(status="draft").exists()

    cs = Syllabus.objects.get(offering__subject__slug="computer-science", offering__level__slug="upper-sixth")
    assert cs.references.get(code="3").title == "Object-Oriented Programming"
    assert cs.references.get(code="3.1").parent.code == "3"


def test_creates_draft_outlines_mapped_to_the_syllabus():
    call_command("load_gce_curriculum")
    course = Course.objects.get(slug="form-5-general-mathematics")
    assert course.status == "draft"
    assert not course.modules.filter(title="Examination").exists()
    topic = Topic.objects.get(module__course=course, title="Bearings")
    assert topic.curriculum_references.get().code == "6.2"


def test_running_twice_changes_nothing_and_keeps_existing_subjects():
    Subject.objects.create(slug="history", name="History (ours)", icon_text="H")
    call_command("load_gce_curriculum")
    counts = (Subject.objects.count(), SubjectOffering.objects.count(), CurriculumReference.objects.count(), Course.objects.count())
    call_command("load_gce_curriculum")
    assert (Subject.objects.count(), SubjectOffering.objects.count(), CurriculumReference.objects.count(), Course.objects.count()) == counts
    assert Subject.objects.get(slug="history").name == "History (ours)"


def test_remove_deletes_syllabi_and_empty_outlines():
    call_command("load_gce_curriculum")
    call_command("load_gce_curriculum", "--remove")
    assert not Syllabus.objects.exists()
    assert not Course.objects.exists()
    assert Subject.objects.exists()


def test_dry_run_saves_nothing():
    call_command("load_gce_curriculum", "--dry-run")
    assert not Syllabus.objects.exists()
    assert not Course.objects.exists()


def test_bad_data_lists_every_problem_and_writes_nothing(monkeypatch):
    subjects = list(data.SUBJECTS) + [
        ("physics", "Physics again", "P", "", "blue", "sciences", "Duplicate slug.", ["form-5"], ["science"]),
        ("astronomy", "Astronomy", "toolongglyph", "", "purple", "space", "x" * 200, ["form-6"], ["engineering"]),
    ]
    syllabi = dict(data.SYLLABI)
    syllabi[("astronomy", "upper-sixth")] = ("Astronomy", "", [("Stars", [("Sun", ""), ("Sun", "")])])
    monkeypatch.setattr(data, "SUBJECTS", subjects)
    monkeypatch.setattr(data, "SYLLABI", syllabi)

    with pytest.raises(CommandError) as exc:
        call_command("load_gce_curriculum")
    message = str(exc.value)
    for expected in ("'physics': slug appears more than once", "icon_text is 12 characters",
                     "accent 'purple'", "category 'space'", "summary is 200 characters",
                     "unknown academic level 'form-6'", "unknown pathway 'engineering'",
                     "not offered at that level", "item 'Sun' appears more than once"):
        assert expected in message
    assert not Subject.objects.exists()


def test_name_used_by_another_subject_is_reported():
    Subject.objects.create(slug="maths", name="General Mathematics", icon_text="x")
    with pytest.raises(CommandError, match="already used by subject 'maths'"):
        call_command("load_gce_curriculum")


def test_loads_on_top_of_the_demo_content():
    call_command("seed_demo")
    call_command("load_gce_curriculum")
    assert Syllabus.objects.filter(version=data.VERSION).count() == len(data.SYLLABI)
