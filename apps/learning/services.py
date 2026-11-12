"""Progress calculations shared by explore, course overview, dashboard and progress pages.

Everything is computed from published lessons in published courses, with a fixed
number of queries regardless of how many courses or modules are shown.
"""

from dataclasses import dataclass

from django.db.models import Count

from apps.core.models import PublicationStatus
from apps.courses.models import Course, Lesson

from .models import Enrollment, LessonProgress


@dataclass
class Stat:
    done: int = 0
    total: int = 0

    @property
    def percent(self):
        return round(100 * self.done / self.total) if self.total else 0

    @property
    def is_complete(self):
        return self.total > 0 and self.done >= self.total


def published_lessons():
    return Lesson.objects.filter(status=PublicationStatus.PUBLISHED, topic__module__course__status=PublicationStatus.PUBLISHED)


def _stats(user, group_field, filter_kwargs):
    totals = (
        published_lessons().filter(**filter_kwargs).values(group_field).annotate(n=Count("pk")).values_list(group_field, "n")
    )
    stats = {key: Stat(total=n) for key, n in totals}
    if user is not None and user.is_authenticated and stats:
        done = (
            LessonProgress.objects.filter(user=user, completed_at__isnull=False, lesson__in=published_lessons().filter(**filter_kwargs))
            .values(f"lesson__{group_field}")
            .annotate(n=Count("pk"))
            .values_list(f"lesson__{group_field}", "n")
        )
        for key, n in done:
            stats.setdefault(key, Stat()).done = n
    return stats


def course_stats(user, courses):
    """{course_id: Stat} for the given courses."""
    ids = [c.pk for c in courses]
    stats = _stats(user, "topic__module__course", {"topic__module__course__in": ids})
    return {pk: stats.get(pk, Stat()) for pk in ids}


def module_stats(user, course):
    return _stats(user, "topic__module", {"topic__module__course": course})


def topic_stats(user, course):
    return _stats(user, "topic", {"topic__module__course": course})


def progress_by_lesson(user, lessons):
    if user is None or not user.is_authenticated:
        return {}
    return {p.lesson_id: p for p in LessonProgress.objects.filter(user=user, lesson__in=lessons)}


def enrolled_offering_ids(user):
    if user is None or not user.is_authenticated:
        return set()
    return set(Enrollment.objects.filter(user=user).values_list("offering_id", flat=True))


def primary_course(offering_courses):
    """The first published course of an offering (offerings normally have one)."""
    published = [c for c in offering_courses if c.status == PublicationStatus.PUBLISHED]
    return published[0] if published else None


def _published_prerequisite_links(lesson_ids):
    """[(lesson_id, prerequisite_id)] for prerequisites students can actually open (published, in a published course)."""
    return list(Lesson.prerequisites.through.objects.filter(
        from_lesson_id__in=lesson_ids, to_lesson__status=PublicationStatus.PUBLISHED,
        to_lesson__topic__module__course__status=PublicationStatus.PUBLISHED).values_list("from_lesson_id", "to_lesson_id"))


def _blocked_from(user, links):
    if not links:
        return set()
    done = set(LessonProgress.objects.filter(user=user, lesson_id__in={to for _f, to in links},
                                             completed_at__isnull=False).values_list("lesson_id", flat=True))
    return {frm for frm, to in links if to not in done}


def blocked_by_prerequisites(user, lessons):
    """Ids of those lessons with at least one prerequisite the student has not completed yet.

    Prerequisites are advice, never a lock: a blocked lesson can always be opened. They only decide what we
    suggest next and what the lesson page recommends doing first.
    """
    return _blocked_from(user, _published_prerequisite_links([l.pk for l in lessons]))


def missing_prerequisites(user, lesson):
    """The prerequisite lessons (published) this student has not completed, in course order."""
    links = _published_prerequisite_links([lesson.pk])
    if not links:
        return []
    done = set(LessonProgress.objects.filter(user=user, lesson_id__in={to for _f, to in links},
                                             completed_at__isnull=False).values_list("lesson_id", flat=True))
    return list(Lesson.objects.filter(pk__in={to for _f, to in links} - done)
                .select_related("topic__module__course__offering__subject", "topic__module__course__offering__level")
                .order_by("topic__module__course__offering__level__order", "topic__module__order", "topic__order", "order", "pk"))


def next_lesson(user, course):
    """The lesson to continue: the most recently opened unfinished one, else the first not completed."""
    lessons = list(
        published_lessons().filter(topic__module__course=course).order_by("topic__module__order", "topic__order", "order", "pk")
    )
    if not lessons:
        return None, None
    progress = progress_by_lesson(user, lessons)
    links = _published_prerequisite_links([l.pk for l in lessons])  # always one lookup, so query counts do not depend on state
    in_progress = [progress[lesson.pk] for lesson in lessons if lesson.pk in progress and not progress[lesson.pk].is_completed]
    if in_progress:
        latest = max(in_progress, key=lambda p: p.last_viewed_at)
        return next(lesson for lesson in lessons if lesson.pk == latest.lesson_id), latest
    todo = [lesson for lesson in lessons if lesson.pk not in progress or not progress[lesson.pk].is_completed]
    if todo:
        # Prefer a lesson whose prerequisites are done; if every remaining one is waiting on something, take the first.
        blocked = _blocked_from(user, links)
        lesson = next((l for l in todo if l.pk not in blocked), todo[0])
        return lesson, progress.get(lesson.pk)
    return lessons[0], progress.get(lessons[0].pk)


def upcoming_lessons(user, course, limit):
    """The next `limit` lessons to study in a course: unfinished ones first (latest opened first), then the rest in order.

    Lessons still waiting on a prerequisite come last.
    """
    lessons = list(
        published_lessons().filter(topic__module__course=course).select_related("topic__module__course__offering__subject")
        .order_by("topic__module__order", "topic__order", "order", "pk")
    )
    progress = progress_by_lesson(user, lessons)
    todo = [l for l in lessons if l.pk not in progress or not progress[l.pk].is_completed]
    started = sorted((l for l in todo if l.pk in progress), key=lambda l: progress[l.pk].last_viewed_at, reverse=True)
    fresh = [l for l in todo if l.pk not in progress]
    blocked = _blocked_from(user, _published_prerequisite_links([l.pk for l in todo]))
    ordered = started + [l for l in fresh if l.pk not in blocked] + [l for l in fresh if l.pk in blocked]
    return ordered[:limit]


def course_for_offering(offering):
    return Course.objects.published().filter(offering=offering).order_by("order", "pk").first()
