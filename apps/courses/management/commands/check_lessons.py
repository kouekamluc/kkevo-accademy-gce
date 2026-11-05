"""Validate lesson content files without touching the database.

    python manage.py check_lessons                         # every file
    python manage.py check_lessons f5_mathematics_a        # one or more files (module names)
"""

from django.core.management.base import BaseCommand, CommandError

from apps.courses import lesson_content


class Command(BaseCommand):
    help = "Validate the lesson content files in apps/courses/lesson_content/."

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="*", help="Content module names, e.g. f5_mathematics_a.")

    def handle(self, *args, **options):
        rows = lesson_content.collect(options["files"] or None)
        errors = lesson_content.validate(rows)
        if errors:
            raise CommandError(f"{len(errors)} problem(s):\n  - " + "\n  - ".join(errors))
        by_topic = {}
        for key, spec, _ in rows:
            by_topic.setdefault(key, set()).add((spec["module"], spec["topic"]))
        for key, done in by_topic.items():
            missing = [f"{m} / {t}" for m, ts in lesson_content.outline(key).items() for t in ts if (m, t) not in done]
            lessons = sum(1 for k, _, _ in rows if k == key)
            self.stdout.write(f"{key[0]} / {key[1]}: {lessons} lessons" + (f"; topics without a lesson: {', '.join(missing)}" if missing else "; every topic covered"))
        self.stdout.write(self.style.SUCCESS(f"{len(rows)} lesson(s) OK."))
