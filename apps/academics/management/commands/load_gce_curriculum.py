"""Load the GCE subjects and syllabus outlines from docs/curriculum/GCE_CURRICULUM_GUIDE.md.

    python manage.py load_gce_curriculum            # subjects, offerings, draft syllabi + course outlines
    python manage.py load_gce_curriculum --dry-run  # check the data and report what would change
    python manage.py load_gce_curriculum --remove   # delete the syllabi and empty draft courses it made

Safe to run again: existing subjects, offerings and courses are never overwritten.
The data in gce_curriculum.py is validated first (duplicates, unknown levels or pathways,
values too long for the database, names already used by another subject); if anything is
wrong, every problem is listed and nothing is written.
Syllabi are saved as unofficial drafts; course outlines are drafts with no lessons,
so students keep seeing "Coming soon" until staff write and publish lessons.
"""

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.text import slugify

from apps.academics import gce_curriculum as data
from apps.academics.models import AcademicLevel, AcademicPathway, CurriculumReference, Subject, SubjectOffering, Syllabus
from apps.courses.models import Course, Lesson, Module, Topic

COURSE_TAG = "[gce-guide]"  # stored in Course.description so --remove can find these outlines
SKIP_IN_COURSE = {"Examination"}  # syllabus sections that are not teaching modules


def _field(model, name):
    return model._meta.get_field(name)


def _check_len(errors, where, model, field, value):
    limit = _field(model, field).max_length
    if limit and len(value) > limit:
        errors.append(f"{where}: {field} is {len(value)} characters, the limit is {limit}.")


def _check_choice(errors, where, model, field, value):
    allowed = {c for c, _ in _field(model, field).choices}
    if value not in allowed:
        errors.append(f"{where}: {field} '{value}' is not one of {', '.join(sorted(allowed))}.")


def validate(subjects, syllabi, level_slugs, pathway_slugs):
    """Return a list of readable problems with the curriculum data (empty when it is fine).

    Also checks the database for an existing subject that already uses one of the names
    under a different slug, which would otherwise fail on the unique name constraint.
    """
    errors, slugs, names, offered = [], set(), set(), set()
    taken = dict(Subject.objects.values_list("name", "slug"))
    for n, row in enumerate(subjects, 1):
        if len(row) != 9:
            errors.append(f"Subject row {n}: expected 9 values, found {len(row)}.")
            continue
        slug, name, glyph, icon, accent, category, summary, row_levels, row_paths = row
        where = f"Subject '{slug}'"
        if slug != slugify(slug) or not slug:
            errors.append(f"{where}: slug must be lowercase letters, digits and hyphens.")
        if slug in slugs:
            errors.append(f"{where}: slug appears more than once.")
        if name in names:
            errors.append(f"{where}: name '{name}' appears more than once.")
        if name in taken and taken[name] != slug:
            errors.append(f"{where}: name '{name}' is already used by subject '{taken[name]}' in the database.")
        slugs.add(slug)
        names.add(name)
        for field, value in (("slug", slug), ("name", name), ("icon_text", glyph), ("summary", summary)):
            _check_len(errors, where, Subject, field, value)
        _check_choice(errors, where, Subject, "accent", accent)
        _check_choice(errors, where, Subject, "category", category)
        if icon:
            _check_choice(errors, where, Subject, "icon", icon)
        if not row_levels:
            errors.append(f"{where}: no academic level given.")
        for lvl in row_levels:
            if lvl not in level_slugs:
                errors.append(f"{where}: unknown academic level '{lvl}'.")
            offered.add((slug, lvl))
        for p in row_paths:
            if p not in pathway_slugs:
                errors.append(f"{where}: unknown pathway '{p}'.")

    for key, value in syllabi.items():
        where = f"Syllabus {key[0]} / {key[1]}"
        if key not in offered:
            errors.append(f"{where}: that subject is not offered at that level in SUBJECTS.")
        if len(value) != 3:
            errors.append(f"{where}: expected (title, notes, sections), found {len(value)} values.")
            continue
        title, _notes, sections = value
        _check_len(errors, where, Syllabus, "title", title)
        if not sections:
            errors.append(f"{where}: has no sections.")
        seen_sections = set()
        for section in sections:
            if len(section) != 2:
                errors.append(f"{where}: a section is not (title, items).")
                continue
            s_title, items = section
            if s_title in seen_sections:
                errors.append(f"{where}: section '{s_title}' appears more than once.")
            seen_sections.add(s_title)
            _check_len(errors, f"{where}, section '{s_title}'", Module, "title", s_title)
            seen_items = set()
            for item in items:
                if len(item) != 2:
                    errors.append(f"{where}, section '{s_title}': an item is not (title, description).")
                    continue
                i_title = item[0]
                if i_title in seen_items:
                    errors.append(f"{where}, section '{s_title}': item '{i_title}' appears more than once.")
                seen_items.add(i_title)
                _check_len(errors, f"{where}, item '{i_title}'", Topic, "title", i_title)
                _check_len(errors, f"{where}, item '{i_title}'", CurriculumReference, "title", i_title)
    return errors


class Command(BaseCommand):
    help = "Load GCE subjects and draft syllabus outlines from the KKEVO curriculum guide."

    def add_arguments(self, parser):
        parser.add_argument("--remove", action="store_true", help="Delete what this command created.")
        parser.add_argument("--no-courses", action="store_true", help="Load syllabi only, no draft course outlines.")
        parser.add_argument("--dry-run", action="store_true", help="Validate and report counts, then roll back.")

    @transaction.atomic
    def handle(self, *args, **options):
        if options["remove"]:
            return self.remove()
        levels = {lvl.slug: lvl for lvl in AcademicLevel.objects.all()}
        pathways = {p.slug: p for p in AcademicPathway.objects.all()}
        errors = validate(data.SUBJECTS, data.SYLLABI, levels.keys(), pathways.keys())
        if errors:
            raise CommandError("The curriculum data has problems; nothing was loaded:\n  - " + "\n  - ".join(errors))

        counts = dict.fromkeys(["subjects", "offerings", "syllabi", "references", "courses"], 0)
        offerings = {}
        for i, (slug, name, glyph, icon, accent, category, summary, level_slugs, path_slugs) in enumerate(data.SUBJECTS):
            subject, created = Subject.objects.get_or_create(slug=slug, defaults=dict(
                name=name, icon_text=glyph, icon=icon, accent=accent, category=category, summary=summary,
                order=(i + 1) * 10))
            counts["subjects"] += created
            for level_slug in level_slugs:
                offering, created = SubjectOffering.objects.get_or_create(subject=subject, level=levels[level_slug])
                if created:
                    offering.pathways.set({pathways[p] for p in path_slugs if p in pathways})
                    counts["offerings"] += 1
                offerings[(slug, level_slug)] = offering

        for key, (title, notes, sections) in data.SYLLABI.items():
            offering = offerings[key]
            syllabus, created = Syllabus.objects.get_or_create(offering=offering, version=data.VERSION, defaults=dict(
                title=title, is_official=False, status="draft",
                notes="\n".join(filter(None, [f"Loaded from {data.SOURCE}. Not the official GCE Board text: "
                                              "check against the official syllabus before publishing.", notes]))))
            if not created:
                continue
            counts["syllabi"] += 1
            refs = self.load_references(syllabus, sections)
            counts["references"] += len(refs)
            if not options["no_courses"] and not offering.courses.exists():
                self.make_course(offering, title, sections, refs)
                counts["courses"] += 1

        self.stdout.write(self.style.SUCCESS(
            ("Dry run, would load: " if options["dry_run"] else "GCE curriculum loaded: ") + ", ".join(f"{n} new {k}" for k, n in counts.items()) + "."))
        self.stdout.write("Syllabi are unofficial drafts; course outlines are drafts with no lessons yet.")
        if options["dry_run"]:
            transaction.set_rollback(True)
            self.stdout.write(self.style.WARNING("Dry run: nothing was saved."))

    def load_references(self, syllabus, sections):
        """Sections become top-level references (1, 2…), items their children (1.1, 1.2…)."""
        refs = {}
        for s_i, (s_title, items) in enumerate(sections, 1):
            parent = CurriculumReference.objects.create(syllabus=syllabus, code=str(s_i), title=s_title, order=s_i)
            refs[s_title] = parent
            for i_i, (i_title, description) in enumerate(items, 1):
                refs[(s_title, i_title)] = CurriculumReference.objects.create(
                    syllabus=syllabus, parent=parent, code=f"{s_i}.{i_i}", title=i_title,
                    description=description, order=i_i)
        return refs

    def make_course(self, offering, title, sections, refs):
        name = f"{offering.level.name} {offering.subject.name}"
        if offering.courses.filter(title=name).exists():  # e.g. the demo course already uses the name
            name = f"{name} (GCE outline)"
        slug = base = slugify(name)
        n = 2
        while Course.objects.filter(slug=slug).exists():
            slug, n = f"{base}-{n}", n + 1
        course = Course.objects.create(
            offering=offering, title=name, slug=slug, status="draft", description=COURSE_TAG,
            summary=f"Outline from the GCE curriculum guide: {title}.")
        m_order = 0
        for s_title, items in sections:
            if s_title in SKIP_IN_COURSE:
                continue
            m_order += 1
            module = Module.objects.create(course=course, title=s_title, order=m_order)
            for t_i, (i_title, description) in enumerate(items, 1):
                topic = Topic.objects.create(module=module, title=i_title, summary=description[:300], order=t_i)
                topic.curriculum_references.add(refs[(s_title, i_title)])
        return course

    def remove(self):
        syllabi = Syllabus.objects.filter(version=data.VERSION)
        courses = Course.objects.filter(description=COURSE_TAG, status="draft")
        with_lessons = set(Lesson.objects.filter(topic__module__course__in=courses).values_list(
            "topic__module__course", flat=True))
        kept = courses.filter(pk__in=with_lessons).count()
        n_courses, _ = courses.exclude(pk__in=with_lessons).delete()
        n_syllabi = syllabi.count()
        syllabi.delete()
        self.stdout.write(self.style.SUCCESS(f"Removed {n_syllabi} syllabi and empty draft course outlines."))
        if kept:
            self.stdout.write(self.style.WARNING(f"Kept {kept} outline course(s) that now have lessons."))
        self.stdout.write("Subjects and offerings were left in place (they may be in use).")
