from django.db import migrations

# Card copy from the approved onboarding mockup (07). Editable in the admin.
COPY = {
    "science": ("Maths, physics, chemistry, biology", "λ", "blue"),
    "arts": ("History, geography, literature, economics", "Aa", "amber"),
}


def forwards(apps, schema_editor):
    Pathway = apps.get_model("academics", "AcademicPathway")
    for slug, (description, glyph, accent) in COPY.items():
        Pathway.objects.filter(slug=slug, description="").update(description=description)
        Pathway.objects.filter(slug=slug, icon_text="").update(icon_text=glyph, accent=accent)
    # Mockup 07 lists Science before Arts (only reorder the untouched seed values).
    Pathway.objects.filter(slug="science", order=20).update(order=10)
    Pathway.objects.filter(slug="arts", order=10).update(order=20)


class Migration(migrations.Migration):
    dependencies = [("academics", "0003_academicpathway_accent_academicpathway_icon_text_and_more")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
