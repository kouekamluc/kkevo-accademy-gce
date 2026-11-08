"""Moving a student up a year (Form 5 to Lower Sixth, Lower Sixth to Upper Sixth).

Changing the class in settings used to leave last year's subjects in the plan and add nothing new, so the
dashboard mixed two years. Moving up now does it properly, and keeps everything the student has done:

* the class switches to the next active level, keeping the stream;
* every subject that continues (the same subject, with content, at the next level) is added to the plan;
* lessons already completed are carried over wherever the next course has the same lesson (same module,
  topic and lesson slug). This is how the shared Pure Mathematics "Core Pure" lessons keep their progress;
  subjects whose next-year course is different (Physics, History...) simply start fresh;
* last year's subjects leave the plan. No progress or practice result is ever deleted, so a student can
  still reopen any old course from Explore.
"""

from dataclasses import dataclass, field

from django.db import transaction
from django.utils import timezone

from apps.academics.models import AcademicLevel, SubjectOffering
from apps.accounts.utils import get_profile
from apps.courses.models import Lesson

from . import services
from .models import Enrollment, LessonProgress


def next_level(level):
    """The next active class after this one, or None in the final year."""
    if level is None:
        return None
    return AcademicLevel.objects.filter(is_active=True, order__gt=level.order).order_by("order").first()


def lesson_key(lesson):
    return (lesson.topic.module.title, lesson.topic.title, lesson.slug)


@dataclass
class Move:
    old: SubjectOffering
    new: SubjectOffering | None  # None: the subject does not continue at the next level
    carried: list = field(default_factory=list)  # [(old LessonProgress, new Lesson)]


@dataclass
class Plan:
    target: AcademicLevel
    moves: list

    @property
    def continuing(self):
        return [m for m in self.moves if m.new]

    @property
    def ending(self):
        return [m for m in self.moves if not m.new]

    @property
    def carried_count(self):
        return sum(len(m.carried) for m in self.moves)


def _carried(user, old, new):
    old_course, new_course = (services.primary_course(list(o.courses.all())) for o in (old, new))
    if not old_course or not new_course:
        return []
    wanted = {lesson_key(l): l for l in services.published_lessons().filter(topic__module__course=new_course)
              .select_related("topic__module")}
    done = (LessonProgress.objects.filter(user=user, completed_at__isnull=False, lesson__topic__module__course=old_course)
            .select_related("lesson__topic__module"))
    return [(p, wanted[lesson_key(p.lesson)]) for p in done if lesson_key(p.lesson) in wanted]


def plan_move_up(user):
    """What moving up would do, or None when the student is already in the final year."""
    profile = get_profile(user)
    target = next_level(profile.level)
    if target is None:
        return None
    enrollments = (Enrollment.objects.filter(user=user, offering__level=profile.level)
                   .select_related("offering__subject", "offering__level").order_by("offering__subject__order"))
    available = {o.subject_id: o for o in SubjectOffering.objects.for_class(target, profile.pathway).with_content()
                 .prefetch_related("courses")}
    moves = []
    for e in enrollments:
        new = available.get(e.offering.subject_id)
        old = SubjectOffering.objects.prefetch_related("courses").get(pk=e.offering_id)
        moves.append(Move(old=e.offering, new=new, carried=_carried(user, old, new) if new else []))
    return Plan(target=target, moves=moves)


@transaction.atomic
def move_up(user):
    """Carry out the move. Returns the Plan that was applied, or None if there is no next year."""
    plan = plan_move_up(user)
    if plan is None:
        return None
    profile = get_profile(user)
    old_level = profile.level
    for move in plan.continuing:
        Enrollment.objects.get_or_create(user=user, offering=move.new)
        have = set(LessonProgress.objects.filter(user=user, lesson__in=[l for _p, l in move.carried]).values_list("lesson_id", flat=True))
        LessonProgress.objects.bulk_create([
            LessonProgress(user=user, lesson=lesson, percent=100, completed_at=old.completed_at or timezone.now())
            for old, lesson in move.carried if lesson.pk not in have
        ])
    Enrollment.objects.filter(user=user, offering__level=old_level).delete()
    profile.level = plan.target
    profile.save(update_fields=["level", "updated_at"])
    return plan
