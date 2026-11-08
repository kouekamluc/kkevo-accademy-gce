"""Report subjects whose courses at different levels share the same lessons.

A two-year A Level subject should split its syllabus between Lower and Upper Sixth. When two levels hold the
same lessons (same module, topic and lesson slug), a student sees the same content twice, with separate progress.
This is read-only: it only lists the overlap, so the content team can replace the copy with the real year-2 content
once the official syllabus split is confirmed. (Moving up a year already carries finished lessons across.)
"""

from itertools import combinations

from django.core.management.base import BaseCommand

from apps.academics.models import Subject
from apps.courses.models import Course, Lesson


def lesson_keys(course):
    return {(l.topic.module.title, l.topic.title, l.slug)
            for l in Lesson.objects.filter(topic__module__course=course, status="published").select_related("topic__module")}


def find_overlaps(threshold=0.5):
    """[(subject, course_a, course_b, shared, smaller)] for same-subject courses sharing at least `threshold` of the smaller one."""
    found = []
    for subject in Subject.objects.all():
        courses = list(Course.objects.filter(offering__subject=subject, status="published").select_related("offering__level")
                       .order_by("offering__level__order"))
        for a, b in combinations(courses, 2):
            keys_a, keys_b = lesson_keys(a), lesson_keys(b)
            smaller = min(len(keys_a), len(keys_b))
            shared = len(keys_a & keys_b)
            if smaller and shared / smaller >= threshold:
                found.append((subject, a, b, shared, smaller))
    return found


class Command(BaseCommand):
    help = "List subjects whose courses at different levels contain the same lessons."

    def handle(self, *args, **options):
        overlaps = find_overlaps()
        if not overlaps:
            self.stdout.write(self.style.SUCCESS("No subject repeats the same lessons across levels."))
            return
        for subject, a, b, shared, smaller in overlaps:
            self.stdout.write(f"{subject.name}: {a.offering.level.code} and {b.offering.level.code} share {shared} of {smaller} lessons")
        self.stdout.write(self.style.WARNING(f"{len(overlaps)} overlapping pair(s). Replace the copies with the real year-2 content."))
