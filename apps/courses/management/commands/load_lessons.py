"""Load KKEVO's lessons from apps/courses/lesson_content/ into the GCE course outlines.

    python manage.py load_lessons              # create missing lessons, published
    python manage.py load_lessons --draft      # ... as drafts instead (staff review first)
    python manage.py load_lessons --dry-run    # validate and report, save nothing
    python manage.py load_lessons --refresh    # also rewrite untouched lessons from the files
    python manage.py load_lessons --remove     # delete untouched lessons that came from the files
    python manage.py load_lessons --prune      # also delete untouched lessons no longer in the files
    python manage.py load_lessons --only mathematics:form-5

Run `load_gce_curriculum` first. Lessons go into the "[gce-guide]" outline course of each
offering; if an offering has another course instead (e.g. the demo Form 5 Mathematics), its
outline course is created from the syllabus.

New lessons are published, and so is an outline course the first time it receives lessons, so
students can use everything straight away. An admin disables what is not relevant (course or
lesson status in the admin or studio); the loader never republishes it. The content is KKEVO's
own draft material, not the official GCE text, so staff still check it against the official
syllabus and fix it in the studio. A lesson counts as "untouched" while it has no studio draft,
revision or event and no student has opened it; --refresh, --remove and --prune never change any
other lesson, and --refresh never changes a lesson's status.
"""

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.academics import gce_curriculum
from apps.academics.management.commands.load_gce_curriculum import COURSE_TAG
from apps.academics.management.commands.load_gce_curriculum import Command as CurriculumCommand
from apps.academics.models import CurriculumReference, SubjectOffering, Syllabus
from apps.core.db import refresh_planner_statistics
from apps.courses import course_pages, lesson_content
from apps.courses.models import Course, Lesson, LessonBlock, Module, Topic


def untouched(lesson):
    """A lesson nobody has worked on in the studio and no student has opened (staff previews do not count)."""
    from apps.learning.models import LessonProgress
    from apps.studio.models import LessonDraft, LessonEvent, LessonRevision

    return not any(model.objects.filter(lesson=lesson).exists() for model in (LessonDraft, LessonRevision, LessonEvent)) \
        and not LessonProgress.objects.filter(lesson=lesson, user__is_staff=False).exists()


class Command(BaseCommand):
    help = "Load KKEVO's lessons into the GCE course outlines (published unless --draft)."

    def add_arguments(self, parser):
        parser.add_argument("--draft", action="store_true", help="Create new lessons and courses as drafts.")
        parser.add_argument("--dry-run", action="store_true", help="Validate and report, then roll back.")
        parser.add_argument("--refresh", action="store_true", help="Rewrite untouched lessons from the files.")
        parser.add_argument("--remove", action="store_true", help="Delete untouched lessons from the files.")
        parser.add_argument("--prune", action="store_true",
                            help="Delete untouched lessons in the loaded courses that are no longer in the files.")
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

        counts = dict.fromkeys(["created", "refreshed", "removed", "pruned", "kept", "course pages", "courses published", "courses archived"], 0)
        status = "draft" if options["draft"] else "published"
        was_empty = {}
        courses, orders = {}, {}
        for key, spec, _source in rows:
            if key not in courses:
                courses[key] = self.outline_course(key, create=not options["remove"])
                if courses[key] and not options["remove"]:
                    counts["course pages"] += self.apply_page(courses[key], key, options["refresh"])
                    was_empty[key] = not Lesson.objects.filter(topic__module__course=courses[key]).exists()
            course = courses[key]
            if course is None:
                continue
            topic = self.topic_for(course, key, spec["module"], spec["topic"])
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
                self.write_lesson(Lesson(topic=topic, slug=spec["slug"], status=status), spec, orders[topic.pk])
                counts["created"] += 1
            elif options["refresh"] and untouched(existing):
                self.write_lesson(existing, spec, orders[topic.pk])
                counts["refreshed"] += 1
            else:
                counts["kept"] += 1

        if status == "published" and not options["remove"]:
            for key, course in courses.items():
                # Only a course that had no lessons before this run: an admin-disabled course stays disabled.
                if (course and was_empty.get(key) and course.status != "published"
                        and Lesson.objects.filter(topic__module__course=course).exists()):
                    # A subject has one published course (database rule): the new course supersedes any older
                    # published one (a demo or stub course), which is archived, never deleted.
                    counts["courses archived"] += Course.objects.filter(offering=course.offering, status="published")                         .exclude(pk=course.pk).update(status="archived")
                    course.status = "published"
                    course.save(update_fields=["status"])
                    counts["courses published"] += 1
        if options["prune"] and not options["remove"]:
            wanted = {(key, spec["module"], spec["topic"], spec["slug"]) for key, spec, _ in rows}
            for key, course in courses.items():
                for stale in Lesson.objects.filter(topic__module__course=course).select_related("topic__module"):
                    if (key, stale.topic.module.title, stale.topic.title, stale.slug) not in wanted and untouched(stale):
                        stale.delete()
                        counts["pruned"] += 1
        summary = ", ".join(f"{n} {k}" for k, n in counts.items() if n or k == "created")
        self.stdout.write(self.style.SUCCESS(("Dry run: " if options["dry_run"] else "Lessons: ") + summary + "."))
        if counts["kept"] and not options["remove"]:
            self.stdout.write("Existing lessons were kept as they are" + (
                " (only untouched drafts are refreshed)." if options["refresh"] else "; use --refresh to update untouched drafts."))
        if not options["dry_run"]:
            refresh_planner_statistics()
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

    def topic_for(self, course, key, module_title, topic_title):
        """The outline topic for a lesson. Optional syllabus sections (e.g. Examination) are added on first use."""
        module = course.modules.filter(title=module_title).first()
        if module is None:
            last = course.modules.order_by("-order").first()
            module = Module.objects.create(course=course, title=module_title, order=(last.order + 1) if last else 1)
        topic = module.topics.filter(title=topic_title).first()
        if topic is None:
            items = dict(dict(gce_curriculum.SYLLABI[key][2]).get(module_title, []))
            last = module.topics.order_by("-order").first()
            topic = Topic.objects.create(module=module, title=topic_title, summary=items.get(topic_title, "")[:300],
                                         order=(last.order + 1) if last else 1)
            ref = CurriculumReference.objects.filter(
                syllabus__offering=course.offering, syllabus__version=gce_curriculum.VERSION,
                parent__title=module_title, title=topic_title).first()
            if ref:
                topic.curriculum_references.add(ref)
        return topic

    def apply_page(self, course, key, refresh):
        """Fill in an outline course's page text from course_pages.PAGES: once when the course is new, or again
        with --refresh (which overwrites the summary and outcomes, so admin edits to them are replaced)."""
        page = course_pages.PAGES.get(key)
        fresh = not course.summary or course.summary.startswith("Outline from the GCE curriculum guide")
        if page is None or not (fresh or refresh):
            return 0
        course.summary = page["summary"]
        course.learning_outcomes = "\n".join(page["outcomes"])
        if page.get("title") and not course.offering.courses.exclude(pk=course.pk).filter(title=page["title"]).exists():
            course.title = page["title"]
        if page.get("slug") and not Course.objects.exclude(pk=course.pk).filter(slug=page["slug"]).exists():
            course.slug = page["slug"]
        course.save()
        if page.get("primary"):
            # Once published, this course is the one students see for the subject (services.primary_course).
            course.offering.courses.exclude(pk=course.pk).filter(order__lte=course.order).update(order=course.order + 10)
        return 1

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
