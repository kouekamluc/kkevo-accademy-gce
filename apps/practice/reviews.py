"""Review my mistakes: helpers shared by the practice views (and usable by dashboard/planner)."""

from datetime import timedelta

from django.db.models import Max
from django.utils import timezone

from .models import REVIEW_INTERVALS, Answer, MistakeCard, ReviewSession


def sync_mistake_cards(user):
    """Create cards for wrong answers that predate the review feature (or came from imports/seed data)."""
    missed = (Answer.objects.filter(attempt__user=user, is_correct=False)
              .exclude(question__mistake_cards__user=user)
              .values("question_id").annotate(last=Max("answered_at")).order_by())
    cards = [MistakeCard(user=user, question_id=row["question_id"], last_missed_at=row["last"],
                         due_on=timezone.localtime(row["last"]).date() + timedelta(days=REVIEW_INTERVALS[0]))
             for row in missed]
    if cards:
        MistakeCard.objects.bulk_create(cards, ignore_conflicts=True)


def live_cards(user):
    """Cards still in rotation whose question is in a published set."""
    return MistakeCard.objects.filter(user=user, retired_at__isnull=True,
                                      question__practice_set__status="published",
                                      question__practice_set__topic__module__course__status="published")


def review_summary(user):
    """Counts for the "Review my mistakes" card: due today, scheduled later, next due date."""
    sync_mistake_cards(user)
    today = timezone.localdate()
    cards = live_cards(user)
    upcoming = cards.filter(due_on__gt=today)
    return {"due": cards.filter(due_on__lte=today).count(), "upcoming": upcoming.count(),
            "next_due": upcoming.order_by("due_on").values_list("due_on", flat=True).first(),
            "open_session": ReviewSession.objects.filter(user=user, completed_at__isnull=True).first()}
