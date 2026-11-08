from django.db import migrations, models


def archive_extra_published_courses(apps, schema_editor):
    """Keep the published course with the most published lessons; archive the other published ones.

    Leftover demo or stub courses had stayed published next to the real course of the same subject.
    Archiving (not deleting) keeps every lesson and every student's progress.
    """
    Course = apps.get_model("courses", "Course")
    Lesson = apps.get_model("courses", "Lesson")
    seen = {}
    for course in Course.objects.filter(status="published").order_by("offering_id", "pk"):
        seen.setdefault(course.offering_id, []).append(course)
    for courses in seen.values():
        if len(courses) < 2:
            continue
        counts = {c.pk: Lesson.objects.filter(topic__module__course=c, status="published").count() for c in courses}
        keep = max(courses, key=lambda c: (counts[c.pk], -c.pk))
        for course in courses:
            if course.pk != keep.pk:
                course.status = "archived"
                course.save(update_fields=["status"])


class Migration(migrations.Migration):
    dependencies = [("courses", "0006_code_block")]

    operations = [
        migrations.RunPython(archive_extra_published_courses, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name="course",
            constraint=models.UniqueConstraint(
                condition=models.Q(("status", "published")), fields=("offering",), name="one_published_course_per_offering"),
        ),
    ]
