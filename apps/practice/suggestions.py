"""Practice today: one suggested practice set for each of the student's subjects.

The Practice page lists every set, which is a wall of cards for a student with eight subjects, and the
dashboard only ever surfaced one or two subjects. This picks the best next set per subject, so every
subject gets a nudge:

1. a topic scored below the pass mark ("Attempted"): try again;
2. a topic that is "Familiar": almost at 80%;
3. a topic not started whose lesson the student has finished: practise what you just learned;
4. any topic not started;
5. "Proficient", then "Mastered" topics last, to keep them fresh.

Subjects the student has not practised for longest come first, and never-practised subjects before those.
"""

from dataclasses import dataclass

from django.db.models import Count
from django.utils import timezone

from apps.learning.analytics import topic_scores
from apps.learning.models import Enrollment, LessonProgress

from .mastery import level_for
from .models import MASTERY_MARK, PASS_MARK, PracticeSet

# Lower is more urgent. A not-started topic whose lesson is done sits between Familiar and plain not-started.
PRIORITY = {"attempted": 0, "familiar": 1, "proficient": 3, "mastered": 4}
NOT_STARTED_AFTER_LESSON = 1.5
NOT_STARTED = 2.5


@dataclass
class Suggestion:
    subject: object
    practice_set: object
    mastery: object
    reason: str
    days_since: int | None  # days since the student last practised this subject; None = never

    @property
    def last_label(self):
        if self.days_since is None:
            return "Not practised yet"
        if self.days_since == 0:
            return "Practised today"
        return f"Last practised {self.days_since} day{'s' if self.days_since != 1 else ''} ago"


def _reason(mastery, lesson_done):
    key = mastery.key
    if key == "attempted":
        return f"You scored {mastery.latest}% last time. Try again to pass {PASS_MARK}%."
    if key == "familiar":
        return f"Almost there. Score {MASTERY_MARK}% or more to level up."
    if key == "not_started":
        return "Practise what you just learned." if lesson_done else "New topic. Start here."
    if key == "proficient":
        return f"Score {MASTERY_MARK}% again to reach Mastered."
    return "Mastered. A quick run keeps it fresh."


def practice_today(user, today=None):
    """One Suggestion per enrolled subject that has a published, non-mock practice set."""
    today = today or timezone.localdate()
    offering_ids = Enrollment.objects.filter(user=user).values_list("offering_id", flat=True)
    sets = (
        PracticeSet.objects.published()
        .filter(topic__module__course__offering_id__in=offering_ids, topic__module__course__status="published", is_mock=False)
        .annotate(question_count=Count("questions"))
        .filter(question_count__gt=0)
        .select_related("topic__module__course__offering__subject")
        .order_by("topic__module__course__offering__subject__order", "topic__module__order", "topic__order", "order")
    )
    scores = topic_scores(user)
    done_lessons = set(LessonProgress.objects.filter(user=user, completed_at__isnull=False).values_list("lesson_id", flat=True))

    last_practised = {}
    for entry in scores.values():
        subject_id = entry["subject"].pk
        if entry["last_at"] and (subject_id not in last_practised or entry["last_at"] > last_practised[subject_id]):
            last_practised[subject_id] = entry["last_at"]

    best = {}  # subject_id -> (sort key, set, mastery, lesson_done)
    for position, s in enumerate(sets):
        mastery = level_for(scores.get(s.topic_id))
        lesson_done = bool(s.lesson_id and s.lesson_id in done_lessons)
        if mastery.key == "not_started":
            priority = NOT_STARTED_AFTER_LESSON if lesson_done else NOT_STARTED
        else:
            priority = PRIORITY[mastery.key]
        key = (priority, position)
        subject_id = s.subject.pk
        if subject_id not in best or key < best[subject_id][0]:
            best[subject_id] = (key, s, mastery, lesson_done)

    suggestions = []
    for subject_id, (key, s, mastery, lesson_done) in best.items():
        when = last_practised.get(subject_id)
        days = (today - timezone.localtime(when).date()).days if when else None
        suggestions.append(Suggestion(subject=s.subject, practice_set=s, mastery=mastery,
                                      reason=_reason(mastery, lesson_done), days_since=days))
    # Mastered-only subjects last; then never practised; then the longest neglected.
    suggestions.sort(key=lambda x: (x.mastery.key == "mastered", x.days_since is not None, -(x.days_since or 0), x.subject.order))
    return suggestions
