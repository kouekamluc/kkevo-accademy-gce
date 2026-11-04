"""Topic mastery levels (Khan Academy style), computed from completed practice attempts.

Not started → Attempted (<60%) → Familiar (60–79%) → Proficient (80%+ once) → Mastered (80%+ twice,
latest included). Levels follow the latest score, so a topic that slips drops back a level until
the student scores 80% again. "Mastered" uses the same "80% twice" rule as the progress page.
"""

from dataclasses import dataclass

from apps.learning.analytics import topic_scores

from .models import MASTERY_MARK, PASS_MARK


@dataclass(frozen=True)
class Mastery:
    key: str
    label: str
    rank: int  # 0–4, for the segmented meter
    next_step: str
    latest: int | None = None

    @property
    def segments(self):
        return [i < self.rank for i in range(4)]


NOT_STARTED = Mastery("not_started", "Not started", 0, "Finish the set once to get your first level.")


def level_for(entry):
    """Mastery for one topic_scores() entry (or None when the topic has no completed attempt)."""
    if not entry or entry.get("latest") is None:
        return NOT_STARTED
    latest = entry["latest"]
    if latest >= MASTERY_MARK and entry.get("mastered_runs", 0) >= 2:
        return Mastery("mastered", "Mastered", 4, "Keep it fresh: clear your mistakes when they come due.", latest)
    if latest >= MASTERY_MARK:
        return Mastery("proficient", "Proficient", 3, f"Score {MASTERY_MARK}% or more again to reach Mastered.", latest)
    if latest >= PASS_MARK:
        return Mastery("familiar", "Familiar", 2, f"Score {MASTERY_MARK}% or more to reach Proficient.", latest)
    return Mastery("attempted", "Attempted", 1, f"Score {PASS_MARK}% or more to reach Familiar.", latest)


def topic_mastery(user):
    """{topic_id: Mastery} for every topic the user has completed a set in."""
    return {topic_id: level_for(entry) for topic_id, entry in topic_scores(user).items()}


def mastery_for_topic(user, topic_id):
    return topic_mastery(user).get(topic_id, NOT_STARTED)


LEVELS = [NOT_STARTED.label, "Attempted", "Familiar", "Proficient", "Mastered"]
