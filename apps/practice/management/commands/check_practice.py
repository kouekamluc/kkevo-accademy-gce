"""Validate practice-set files without touching the database.

    python manage.py check_practice                    # every file
    python manage.py check_practice f5_mathematics_a   # one or more files
"""

from django.core.management.base import BaseCommand, CommandError

from apps.courses import lesson_content
from apps.practice import practice_content


class Command(BaseCommand):
    help = "Validate the practice-set files in apps/practice/practice_content/."

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="*")

    def handle(self, *args, **options):
        rows = practice_content.collect(options["files"] or None)
        errors = practice_content.validate(rows)
        if errors:
            raise CommandError(f"{len(errors)} problem(s):\n  - " + "\n  - ".join(errors))
        done = {}
        for key, spec, _ in rows:
            done.setdefault(key, set()).add((spec["module"], spec["topic"]))
        for key, topics in done.items():
            missing = [f"{m} / {t}" for m, ts in lesson_content.outline(key).items() for t in ts if (m, t) not in topics]
            n_sets = sum(1 for k, _, _ in rows if k == key)
            n_q = sum(len(s["questions"]) for k, s, _ in rows if k == key)
            self.stdout.write(f"{key[0]} / {key[1]}: {n_sets} sets, {n_q} questions" + (
                f"; topics without a set: {', '.join(missing)}" if missing else "; every topic covered"))
        self.stdout.write(self.style.SUCCESS(f"{len(rows)} set(s) OK."))
