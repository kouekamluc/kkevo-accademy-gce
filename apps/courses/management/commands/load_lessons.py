"""Load KKEVO's draft lessons from apps/courses/lesson_content/ into the GCE course outlines.

    python manage.py load_lessons              # create missing lessons (as drafts)
    python manage.py load_lessons --dry-run    # validate and report, save nothing
    python manage.py load_lessons --refresh    # also rewrite untouched drafts from the files
    python manage.py load_lessons --remove     # delete untouched drafts that came from the files
    python manage.py load_lessons --only mathematics:form-5

Run `load_gce_curriculum` first. Lessons go into the "[gce-guide]" outline course of each
offering; if an offering has another course instead (e.g. the demo Form 5 Mathematics), its
outline course is created from the syllabus.

Lessons are always created as drafts with no author or reviewer: staff check each one against
the official GCE syllabus in the studio and publish it there. A lesson counts as "untouched"
while it is a draft and has no studio draft, revision or event; --refresh and --remove never
change any other lesson.
"""

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.academics import gce_curriculum
from apps.academics.management.commands.load_gce_curriculum import COURSE_TAG
from apps.academics.management.commands.load_gce_curriculum import Command as CurriculumCommand
from apps.academics.models import SubjectOffering, Syllabus
from apps.courses import lesson_content
from apps.courses.models import Course, Lesson, LessonBlock


def untouched(lesson):
    """A draft nobody has worked on in the studio yet."""
    from apps.studio.models import LessonDraft, LessonEvent, LessonRevision

    return lesson.status == "draft" and not any(
        model.objects.filter(lesson=lesson).exists() for model in (LessonDraft, LessonRevision, LessonEvent))


class Command(BaseCommand):
    help = "Load KKEVO's draft lessons into the GCE course outlines."

    def add_arguments(self, parser):
        parser.add_argument("--dry-run", action="store_true", help="Validate and report, then roll back.")
        parser.add_argument("--refresh", action="store_true", help="Rewrite untouched draft lessons from the files.")
        parser.add_argument("--remove", action="store_true", help="Delete untouched draft lessons from the files.")
        parser.add_argument("--only", action="append", default=[], metavar="SUBJECT:LEVEL",
                            help="Limit to one course, e.g. mathematics:form-5 (repeatable).")

    @transaction.atomic
    def handle(self, *args, **options):
        rows = lesson_content.collect()
        if options["only"]:
            wanted = {tuple(o.split(":", 1)) for o in options["only"]}
            rows = [r for r in rows if r[0] in wanted]
            if not rows:
                raise CommandError(f"No lesson content for {', '.join(options['only'])}.")
        errors = lesson_content.validate(rows)
        if errors:
            raise CommandError("The lesson content has problems; nothing was loaded:\n  - " + "\n  - ".join(errors))

        counts = dict.fromkeys(["created", "refreshed", "removed", "kept"], 0)
        courses, orders = {}, {}
        for key, spec, _source in rows:
            if key not in courses:
                courses[key] = self.outline_course(key, create=not options["remove"])
            course = courses[key]
            if course is None:
                continue
            topic = course.modules.get(title=spec["module"]).topics.get(title=spec["topic"])
            orders[topic.pk] = orders.get(topic.pk, 0) + 1
            existing = Lesson.objects.filter(topic=topic, slug=spec["slug"]).first()
            if options["remove"]:
                if existing and untouched(existing):
                    existing.delete()
                    counts["removed"] += 1
                elif existing:
                    counts["kept"] += 1
                continue
            if existing is None:
                self.write_lesson(Lesson(topic=topic, slug=spec["slug"], status="draft"), spec, orders[topic.pk])
                counts["created"] += 1
            elif options["refresh"] and untouched(existing):
                self.write_lesson(existing, spec, orders[topic.pk])
                counts["refreshed"] += 1
            else:
                counts["kept"] += 1

        summary = ", ".join(f"{n} {k}" for k, n in counts.items() if n or k == "created")
        self.stdout.write(self.style.SUCCESS(("Dry run: " if options["dry_run"] else "Lessons: ") + summary + "."))
        if counts["kept"] and not options["remove"]:
            self.stdout.write("Existing lessons were kept as they are" + (
                " (only untouched drafts are refreshed)." if options["refresh"] else "; use --refresh to update untouched drafts."))
        if options["dry_run"]:
            transaction.set_rollback(True)
            self.stdout.write(self.style.WARNING("Dry run: nothing was saved."))

    def outline_course(self, key, create=True):
        subject_slug, level_slug = key
        offering = SubjectOffering.objects.filter(subject__slug=subject_slug, level__slug=level_slug).first()
        if offering is None:
            if not create:
                return None
            raise CommandError(f"No {subject_slug} offering at {level_slug}: run load_gce_curriculum first.")
        course = offering.courses.filter(description=COURSE_TAG).first()
        if course or not create:
            return course
        syllabus = Syllabus.objects.filter(offering=offering, version=gce_curriculum.VERSION).first()
        if syllabus is None:
            raise CommandError(f"No GCE guide syllabus for {subject_slug} / {level_slug}: run load_gce_curriculum first.")
        title, _notes, sections = gce_curriculum.SYLLABI[key]
        refs = {}
        for ref in syllabus.references.select_related("parent"):
            refs[(ref.parent.title, ref.title) if ref.parent else ref.title] = ref
        course = CurriculumCommand().make_course(offering, title, sections, refs)
        self.stdout.write(f"Created outline course '{course.title}' ({course.slug}).")
        return course

    def write_lesson(self, lesson, spec, order):
        lesson.title = spec["title"]
        lesson.summary = spec["summary"]
        lesson.lesson_type = "reading"
        lesson.estimated_minutes = spec["minutes"]
        lesson.objectives = "\n".join(spec["objectives"])
        lesson.key_concepts = "\n".join(spec["key_concepts"])
        lesson.order = order
        lesson.save()
        lesson.curriculum_references.set(lesson.topic.curriculum_references.all())
        lesson.blocks.all().delete()
        LessonBlock.objects.bulk_create([
            LessonBlock(lesson=lesson, order=n, block_type=b["block_type"], title=b.get("title", ""),
                        body=b.get("body", ""), alt_text=b.get("alt_text", ""), data=b.get("data") or {})
            for n, b in enumerate(spec["blocks"], 1)])
