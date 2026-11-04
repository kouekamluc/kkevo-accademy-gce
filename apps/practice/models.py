from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.core.models import OrderedModel, PublicationStatus, PublishedQuerySet, TimeStampedModel
from apps.courses.models import Lesson, Topic

PASS_MARK = 60  # below this a topic "needs revision" (mockup 10)
MASTERY_MARK = 80  # "Mastered" = 80%+ on a topic's practice set twice


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


class Question(OrderedModel):
    practice_set = models.ForeignKey(PracticeSet, on_delete=models.CASCADE, related_name="questions")
    prompt = models.TextField(help_text="Question text. Use $...$ for maths.")
    concept = models.CharField(max_length=80, blank=True, help_text="Tag, e.g. 'Newton’s second law'.")
    skill = models.CharField(max_length=40, blank=True, help_text="Tag, e.g. 'Calculation'.")
    diagram_url = models.URLField(blank=True)
    diagram_alt = models.CharField(max_length=300, blank=True)
    feedback = models.CharField(max_length=300, blank=True, help_text="Shown when correct, e.g. 'You found a first…'.")
    solution_steps = models.JSONField(
        default=list, blank=True, help_text='Worked solution: [{"title": "...", "math": "..."}].'
    )

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.prompt[:60]

    @property
    def correct_choice(self):
        return next((c for c in self.choices.all() if c.is_correct), None)


class Choice(OrderedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=300, help_text="Use $...$ for maths.")
    is_correct = models.BooleanField(default=False)
    why_wrong = models.CharField(max_length=300, blank=True, help_text="Explains this wrong answer.")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.text



class Attempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="practice_attempts")
    practice_set = models.ForeignKey(PracticeSet, on_delete=models.CASCADE, related_name="attempts")
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

    def finish(self):
        answers = list(self.answers.all())
        self.correct_count = sum(a.is_correct for a in answers)
        self.total = self.practice_set.questions.count()
        self.completed_at = timezone.now()
        self.save(update_fields=["correct_count", "total", "completed_at"])


class Answer(models.Model):
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="+")
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["question__order", "question__pk"]
        constraints = [models.UniqueConstraint(fields=["attempt", "question"], name="one_answer_per_question")]
