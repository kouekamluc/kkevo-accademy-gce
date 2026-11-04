"""Seed the class levels and pathways the platform is launched with.

These are structural records named in the product brief, not curriculum
content. Staff can rename, deactivate or add records in the admin.
"""

from django.db import migrations

LEVELS = [
    ("F5", "Form 5", "form-5", "O", "GCE Ordinary Level", "Master Ordinary Level subjects.", 10),
    ("L6", "Lower Sixth", "lower-sixth", "A", "A Level foundation", "Build strong Advanced Level foundations.", 20),
    ("U6", "Upper Sixth", "upper-sixth", "A", "GCE Advanced Level", "Understand advanced concepts with confidence.", 30),
]
PATHWAYS = [("Arts", "arts", 10), ("Science", "science", 20)]


def seed(apps, schema_editor):
    AcademicLevel = apps.get_model("academics", "AcademicLevel")
    AcademicPathway = apps.get_model("academics", "AcademicPathway")
    for code, name, slug, exam_level, tagline, description, order in LEVELS:
        AcademicLevel.objects.get_or_create(
            code=code,
            defaults=dict(
                name=name, slug=slug, exam_level=exam_level, tagline=tagline, description=description, order=order
            ),
        )
    for name, slug, order in PATHWAYS:
        AcademicPathway.objects.get_or_create(slug=slug, defaults=dict(name=name, order=order))


def unseed(apps, schema_editor):
    apps.get_model("academics", "AcademicLevel").objects.filter(code__in=[lvl[0] for lvl in LEVELS]).delete()
    apps.get_model("academics", "AcademicPathway").objects.filter(slug__in=[p[1] for p in PATHWAYS]).delete()


class Migration(migrations.Migration):
    dependencies = [("academics", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
