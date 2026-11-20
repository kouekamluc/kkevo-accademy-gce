from django.db import migrations

OLD, NEW = "History, geography, literature, economics", "History, literature, economics, commerce, accounting"


def forwards(apps, schema_editor):
    # Commercial subjects belong to the Arts stream here, so say so on the stream card students pick from.
    apps.get_model("academics", "AcademicPathway").objects.filter(slug="arts", description=OLD).update(description=NEW)


def backwards(apps, schema_editor):
    apps.get_model("academics", "AcademicPathway").objects.filter(slug="arts", description=NEW).update(description=OLD)


class Migration(migrations.Migration):
    dependencies = [("academics", "0005_alter_syllabus_status")]
    operations = [migrations.RunPython(forwards, backwards)]
