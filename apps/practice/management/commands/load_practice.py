"""Load KKEVO's practice sets from apps/practice/practice_content/ into the GCE outline courses.

    python manage.py load_practice              # create missing sets, published
    python manage.py load_practice --draft      # ... as drafts instead (staff review first)
    python manage.py load_practice --dry-run    # validate and report, save nothing
    python manage.py load_practice --refresh    # also rewrite sets no student has attempted
    python manage.py load_practice --remove     # delete sets from the files that no student has attempted
    python manage.py load_practice --prune      # also delete such sets that are no longer in the files
    python manage.py load_practice --only mathematics:form-5

Run `load_lessons` first: sets go into the same "[gce-guide]" outline courses and link to their lesson.
New sets are published so students can use them straight away; an admin disables what is not
relevant and a refresh never changes a set's status. Sets a student has attempted are never
rewritten or deleted.
"""

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.templatetags.static import static

from apps.academics.management.commands.load_gce_curriculum import COURSE_TAG
from apps.core.db import refresh_planner_statistics
from apps.courses.management.commands.load_lessons import Command as LessonsCommand
from apps.courses.models import Course, Lesson
from apps.practice import practice_content
from apps.practice.models import Choice, PracticeSet, Question


def untouched(practice_set):
    """A set no student has attempted (staff previews do not count)."""
    return not practice_set.attempts.filter(user__is_staff=False).exists()


class Command(BaseCommand):
    help = "Load KKEVO's draft practice sets into the GCE course outlines."

    def add_arguments(self, parser):
        parser.add_argument("--draft", action="store_true", help="Create new sets as drafts.")
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--refresh", action="store_true", help="Rewrite draft sets nobody has attempted.")
        parser.add_argument("--remove", action="store_true", help="Delete draft sets nobody has attempted.")
        parser.add_argument("--prune", action="store_true",
                            help="Delete draft sets nobody has attempted that are no longer in the files.")
        parser.add_argument("--only", action="append", default=[], metavar="SUBJECT:LEVEL")

    @transaction.atomic
    def handle(self, *args, **options):
        rows = practice_content.collect()
        if options["only"]:
            wanted = {tuple(o.split(":", 1)) for o in options["only"]}
            rows = [r for r in rows if r[0] in wanted]
        errors = practice_content.validate(rows)
        if errors:
            raise CommandError("The practice content has problems; nothing was loaded:\n  - " + "\n  - ".join(errors))

        counts = dict.fromkeys(["created", "refreshed", "removed", "pruned", "kept", "questions"], 0)
        orders, courses = {}, {}
        for key, spec, _source in rows:
            course = Course.objects.filter(offering__subject__slug=key[0], offering__level__slug=key[1],
                                           description=COURSE_TAG).first()
            if course is None:
                if options["remove"]:
                    continue
                raise CommandError(f"No GCE outline course for {key[0]} / {key[1]}: run load_lessons first.")
            courses[key] = course
            topic = LessonsCommand().topic_for(course, key, spec["module"], spec["topic"])
            orders[topic.pk] = orders.get(topic.pk, 0) + 1
            existing = PracticeSet.objects.filter(topic=topic, title=spec["title"]).first()
            if options["remove"]:
                if existing and untouched(existing):
                    existing.delete()
                    counts["removed"] += 1
                elif existing:
                    counts["kept"] += 1
                continue
            if existing is None:
                counts["questions"] += self.write_set(
                    PracticeSet(topic=topic, title=spec["title"], status="draft" if options["draft"] else "published"),
                    spec, orders[topic.pk])
                counts["created"] += 1
            elif options["refresh"] and untouched(existing):
                counts["questions"] += self.write_set(existing, spec, orders[topic.pk])
                counts["refreshed"] += 1
            else:
                counts["kept"] += 1

        if options["prune"] and not options["remove"]:
            wanted = {(key, spec["module"], spec["topic"], spec["title"]) for key, spec, _ in rows}
            for key, course in courses.items():
                for stale in PracticeSet.objects.filter(topic__module__course=course).select_related("topic__module"):
                    if (key, stale.topic.module.title, stale.topic.title, stale.title) not in wanted and untouched(stale):
                        stale.delete()
                        counts["pruned"] += 1
        summary = ", ".join(f"{n} {k}" for k, n in counts.items() if n or k == "created")
        self.stdout.write(self.style.SUCCESS(("Dry run: " if options["dry_run"] else "Practice sets: ") + summary + "."))
        if not options["dry_run"]:
            refresh_planner_statistics()
        if options["dry_run"]:
            transaction.set_rollback(True)
            self.stdout.write(self.style.WARNING("Dry run: nothing was saved."))

    def write_set(self, practice_set, spec, order):
        practice_set.order = order - 1
        practice_set.lesson = Lesson.objects.filter(topic=practice_set.topic, slug=spec.get("lesson") or "").first()
        practice_set.is_mock = bool(spec.get("mock"))
        practice_set.time_limit_minutes = spec.get("time_limit_minutes") or None
        practice_set.save()
        practice_set.attempts.filter(user__is_staff=True).delete()  # staff previews of the old questions
        practice_set.questions.all().delete()
        for q_i, q in enumerate(spec["questions"]):
            numeric = q["kind"] == "numeric"
            question = Question.objects.create(
                practice_set=practice_set, order=q_i, kind=q["kind"], prompt=q["prompt"], concept=q.get("concept", ""),
                skill=q.get("skill", ""), hint=q.get("hint", ""), feedback=q.get("feedback", ""),
                diagram_url=static(f"lessons/diagrams/{q['diagram']}") if q.get("diagram") else "",
                diagram_alt=q.get("diagram_alt", "") if q.get("diagram") else "",
                solution_steps=q["steps"], numeric_answer=q["answer"] if numeric else None,
                tolerance=q.get("tolerance", 0) if numeric else 0, unit=q.get("unit", "") if numeric else "")
            if not numeric:
                Choice.objects.bulk_create([
                    Choice(question=question, order=c_i, text=c["text"], is_correct=bool(c.get("correct")),
                           why_wrong="" if c.get("correct") else c.get("why", ""))
                    for c_i, c in enumerate(q["choices"])])
        return len(spec["questions"])
