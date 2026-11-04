import math
from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.core.models import OrderedModel, PublicationStatus, PublishedQuerySet, TimeStampedModel
from apps.courses.models import Lesson, Topic

PASS_MARK = 60  # below this a topic "needs revision" (mockup 10)
MASTERY_MARK = 80  # "Mastered" = 80%+ on a topic's practice set twice

REVIEW_INTERVALS = (1, 3, 7)  # days before a missed question comes back, one per successful review step
REVIEW_SESSION_SIZE = 10
EXAM_SECONDS_PER_QUESTION = 90  # pacing for timed exam mode (about 1½ minutes a question)
EXAM_MIN_SECONDS = 5 * 60
EXAM_GRACE_SECONDS = 15  # slow connections: accept answers posted just after the clock runs out


class PracticeSet(OrderedModel, TimeStampedModel):
    """A set of questions for a topic (optionally tied to one lesson)."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="practice_sets")
    lesson = models.ForeignKey(
        Lesson, on_delete=models.SET_NULL, null=True, blank=True, related_name="practice_sets",
        help_text="Optional: the lesson this set follows.",
    )
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=PublicationStatus.choices, default=PublicationStatus.DRAFT)

    objects = PublishedQuerySet.as_manager()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("practice:set", kwargs={"pk": self.pk})

    @property
    def subject(self):
        return self.topic.module.course.offering.subject

    def clean(self):
        if self.lesson_id and self.lesson.topic_id != self.topic_id:
            raise ValidationError({"lesson": "The lesson must belong to the same topic."})

    @staticmethod
    def exam_seconds(question_count):
        return max(EXAM_MIN_SECONDS, question_count * EXAM_SECONDS_PER_QUESTION)


def parse_number(text):
    """Read a typed number: accepts "3600", "3 600", "3,6" (decimal comma), "−2" and "1.2e3"."""
    cleaned = (text or "").strip().replace(" ", "").replace(" ", "").replace("−", "-")
    if cleaned.count(",") == 1 and "." not in cleaned:
        cleaned = cleaned.replace(",", ".")
    try:
        value = float(cleaned)
    except ValueError:
        return None
    return value if math.isfinite(value) else None


class Question(OrderedModel):
    class Kind(models.TextChoices):
        CHOICE = "choice", "Multiple choice"
        NUMERIC = "numeric", "Numeric answer"

    practice_set = models.ForeignKey(PracticeSet, on_delete=models.CASCADE, related_name="questions")
    kind = models.CharField(max_length=10, choices=Kind.choices, default=Kind.CHOICE)
    prompt = models.TextField(help_text="Question text. Use $...$ for maths.")
    concept = models.CharField(max_length=80, blank=True, help_text="Tag, e.g. 'Newton’s second law'.")
    skill = models.CharField(max_length=40, blank=True, help_text="Tag, e.g. 'Calculation'.")
    diagram_url = models.URLField(blank=True)
    diagram_alt = models.CharField(max_length=300, blank=True)
    hint = models.TextField(
        blank=True, help_text="Optional nudge the student can open before answering. Point to the idea or the "
        "first step; don't give the answer away. Use $...$ for maths.")
    numeric_answer = models.FloatField(null=True, blank=True, help_text="Numeric questions: the correct value.")
    tolerance = models.FloatField(
        default=0, help_text="Numeric questions: accepted distance from the answer, e.g. 0.05 accepts 3.55 to 3.65.")
    unit = models.CharField(max_length=30, blank=True, help_text="Numeric questions: unit shown after the box, e.g. N.")
    feedback = models.CharField(max_length=300, blank=True, help_text="Shown when correct, e.g. 'You found a first…'.")
    solution_steps = models.JSONField(
        default=list, blank=True, help_text='Worked solution: [{"title": "...", "math": "..."}].'
    )

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.prompt[:60]

    @property
    def is_numeric(self):
        return self.kind == self.Kind.NUMERIC

    @property
    def correct_choice(self):
        return next((c for c in self.choices.all() if c.is_correct), None)

    @property
    def correct_display(self):
        if self.is_numeric:
            return f"{self.numeric_answer:g} {self.unit}".strip() if self.numeric_answer is not None else ""
        choice = self.correct_choice
        return choice.text if choice else ""

    def clean(self):
        if self.is_numeric and self.numeric_answer is None:
            raise ValidationError({"numeric_answer": "A numeric question needs a correct value."})
        if self.tolerance is not None and self.tolerance < 0:
            raise ValidationError({"tolerance": "Tolerance cannot be negative."})

    def check_number(self, value):
        # A tiny epsilon so float noise (0.1 + 0.2) never marks a right answer wrong.
        return value is not None and abs(value - self.numeric_answer) <= (self.tolerance or 0) + 1e-9

    def grade(self, data):
        """Read an answer from POST data: the answer's fields, or None if nothing valid was sent."""
        if self.is_numeric:
            value = parse_number(data.get("value"))
            if value is None:
                return None
            return {"choice": None, "numeric_value": value, "is_correct": self.check_number(value)}
        pk = str(data.get("choice") or "")
        choice = self.choices.filter(pk=pk).first() if pk.isdigit() else None
        if choice is None:
            return None
        return {"choice": choice, "numeric_value": None, "is_correct": choice.is_correct}


class Choice(OrderedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=300, help_text="Use $...$ for maths.")
    is_correct = models.BooleanField(default=False)
    why_wrong = models.CharField(max_length=300, blank=True, help_text="Explains this wrong answer.")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.text


class Confidence(models.TextChoices):
    SURE = "sure", "I’m sure"
    GUESS = "guess", "I’m guessing"


class BaseAnswer(models.Model):
    """What a student answered for one question, in a practice attempt or a mistakes review."""

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="+", null=True, blank=True)
    numeric_value = models.FloatField(null=True, blank=True)
    is_correct = models.BooleanField()
    used_hint = models.BooleanField(default=False)
    confidence = models.CharField(max_length=5, choices=Confidence.choices, blank=True)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def lucky_guess(self):
        return self.is_correct and self.confidence == Confidence.GUESS

    @property
    def display(self):
        """The student's answer as text (may contain $...$ maths)."""
        if self.choice_id:
            return self.choice.text
        if self.numeric_value is not None:
            return f"{self.numeric_value:g} {self.question.unit}".strip()
        return ""


class Attempt(models.Model):
    class Mode(models.TextChoices):
        PRACTICE = "practice", "Practice"
        EXAM = "exam", "Timed exam"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="practice_attempts")
    practice_set = models.ForeignKey(PracticeSet, on_delete=models.CASCADE, related_name="attempts")
    mode = models.CharField(max_length=10, choices=Mode.choices, default=Mode.PRACTICE)
    time_limit_seconds = models.PositiveIntegerField(null=True, blank=True, help_text="Timed exam mode only.")
    hints_used = models.JSONField(default=list, blank=True, help_text="IDs of questions whose hint was opened.")
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True, db_index=True)
    correct_count = models.PositiveSmallIntegerField(default=0)
    total = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.user} · {self.practice_set} · {self.score}%"

    @property
    def score(self):
        return round(100 * self.correct_count / self.total) if self.total else 0

    @property
    def is_exam(self):
        return self.mode == self.Mode.EXAM

    @property
    def deadline(self):
        if not self.time_limit_seconds or not self.started_at:
            return None
        return self.started_at + timedelta(seconds=self.time_limit_seconds)

    def seconds_left(self):
        if self.deadline is None:
            return None
        return max(0, int((self.deadline - timezone.now()).total_seconds()))

    def is_expired(self, grace=0):
        return self.deadline is not None and timezone.now() > self.deadline + timedelta(seconds=grace)

    @property
    def shows_feedback(self):
        """Timed exam mode keeps right/wrong hidden until the attempt is finished."""
        return not self.is_exam or self.completed_at is not None

    def finish(self):
        answers = list(self.answers.all())
        self.correct_count = sum(a.is_correct for a in answers)
        self.total = self.practice_set.questions.count()
        self.completed_at = timezone.now()
        self.save(update_fields=["correct_count", "total", "completed_at"])


class Answer(BaseAnswer):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    class Meta:
        ordering = ["question__order", "question__pk"]
        constraints = [models.UniqueConstraint(fields=["attempt", "question"], name="one_answer_per_question")]


class MistakeCard(models.Model):
    """Spaced review of one question a student got wrong (or got right only by guessing).

    It comes back 1 day after the miss; each correct review pushes it out (3, then 7 days) and
    the correct review after the 7-day gap retires it. A wrong review starts it over at 1 day.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mistake_cards")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="mistake_cards")
    step = models.PositiveSmallIntegerField(default=0, help_text="Index into REVIEW_INTERVALS.")
    due_on = models.DateField(db_index=True)
    last_missed_at = models.DateTimeField()
    reviews = models.PositiveSmallIntegerField(default=0)
    retired_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["due_on", "pk"]
        constraints = [models.UniqueConstraint(fields=["user", "question"], name="one_card_per_question")]

    def __str__(self):
        return f"{self.user} · {self.question} · due {self.due_on}"

    @classmethod
    def record_miss(cls, user, question, when=None):
        when = when or timezone.now()
        due = timezone.localtime(when).date() + timedelta(days=REVIEW_INTERVALS[0])
        card, created = cls.objects.get_or_create(user=user, question=question,
                                                  defaults={"due_on": due, "last_missed_at": when})
        if not created:
            card.step, card.due_on, card.last_missed_at, card.retired_at = 0, due, when, None
            card.save(update_fields=["step", "due_on", "last_missed_at", "retired_at"])
        return card

    def record_review(self, correct, hinted=False, when=None):
        """Move the card along after a review. Right with a hint = same gap again, not a step forward."""
        when = when or timezone.now()
        today = timezone.localtime(when).date()
        self.reviews += 1
        if not correct:
            self.step, self.last_missed_at, self.retired_at = 0, when, None
            self.due_on = today + timedelta(days=REVIEW_INTERVALS[0])
        elif hinted:
            self.due_on = today + timedelta(days=REVIEW_INTERVALS[self.step])
        elif self.step + 1 >= len(REVIEW_INTERVALS):
            self.retired_at = when
        else:
            self.step += 1
            self.due_on = today + timedelta(days=REVIEW_INTERVALS[self.step])
        self.save()


class ReviewSession(models.Model):
    """A generated "Review my mistakes" run over questions whose MistakeCard is due."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review_sessions")
    question_ids = models.JSONField(default=list)
    hints_used = models.JSONField(default=list, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.user} · review · {len(self.question_ids)} questions"

    @property
    def total(self):
        return len(self.question_ids)


class ReviewAnswer(BaseAnswer):
    session = models.ForeignKey(ReviewSession, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="review_answers")

    class Meta:
        constraints = [models.UniqueConstraint(fields=["session", "question"], name="one_review_answer_per_question")]
