from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from apps.academics.models import CurriculumReference, SubjectOffering
from apps.core.models import OrderedModel, PublicationStatus, PublishedQuerySet, TimeStampedModel


class CourseQuerySet(PublishedQuerySet):
    def for_level(self, level):
        return self.filter(offering__level=level)


class Course(TimeStampedModel):
    """A complete course for one subject offering, e.g. 'Form 5 Mathematics'."""

    offering = models.ForeignKey(SubjectOffering, on_delete=models.PROTECT, related_name="courses")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    learning_outcomes = models.TextField(blank=True, help_text="One outcome per line.")
    status = models.CharField(max_length=10, choices=PublicationStatus.choices, default=PublicationStatus.DRAFT)
    order = models.PositiveIntegerField(default=0, help_text="Order among courses of the same offering.")

    objects = CourseQuerySet.as_manager()

    class Meta:
        ordering = ["offering__level__order", "offering__subject__order", "order", "title"]
        constraints = [
            models.UniqueConstraint(fields=["offering", "title"], name="unique_course_title_per_offering"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={"slug": self.slug})

    @property
    def subject(self):
        return self.offering.subject

    @property
    def level(self):
        return self.offering.level

    @property
    def outcomes_list(self):
        return [line.strip() for line in self.learning_outcomes.splitlines() if line.strip()]


class Module(OrderedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300, blank=True)

    class Meta(OrderedModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=["course", "title"], name="unique_module_title_per_course"),
        ]

    def __str__(self):
        return self.title


class Topic(OrderedModel):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300, blank=True)
    curriculum_references = models.ManyToManyField(CurriculumReference, blank=True, related_name="topics")

    class Meta(OrderedModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=["module", "title"], name="unique_topic_title_per_module"),
        ]

    def __str__(self):
        return self.title


class LessonType(models.TextChoices):
    READING = "reading", "Reading"
    VIDEO = "video", "Video"
    INTERACTIVE = "interactive", "Interactive"
    PRACTICE = "practice", "Practice"


def _lines(text):
    return [line.strip() for line in (text or "").splitlines() if line.strip()]


class Lesson(OrderedModel, TimeStampedModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    summary = models.CharField(max_length=300, blank=True)
    lesson_type = models.CharField(max_length=12, choices=LessonType.choices, default=LessonType.READING)
    estimated_minutes = models.PositiveSmallIntegerField(default=10)
    status = models.CharField(max_length=10, choices=PublicationStatus.choices, default=PublicationStatus.DRAFT)
    objectives = models.TextField(blank=True, help_text="Learning objectives, one per line.")
    key_concepts = models.TextField(blank=True, help_text="Key terms, one per line.")
    prerequisites = models.ManyToManyField("self", symmetrical=False, blank=True, related_name="unlocks")
    curriculum_references = models.ManyToManyField(CurriculumReference, blank=True, related_name="lessons")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="authored_lessons"
    )
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="reviewed_lessons"
    )

    objects = PublishedQuerySet.as_manager()

    class Meta(OrderedModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=["topic", "slug"], name="unique_lesson_slug_per_topic"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson", kwargs={"course_slug": self.course.slug, "pk": self.pk})

    @property
    def course(self):
        return self.topic.module.course

    @property
    def objectives_list(self):
        return _lines(self.objectives)

    @property
    def key_concepts_list(self):
        return _lines(self.key_concepts)

    @property
    def type_label(self):
        """'Reading · 10 min' as in the course outline."""
        return f"{self.get_lesson_type_display()} · {self.estimated_minutes} min"


class BlockType(models.TextChoices):
    HEADING = "heading", "Heading"
    TEXT = "text", "Text"
    FORMULA = "formula", "Formula (LaTeX)"
    DEFINITION = "definition", "Information box / definition"
    CALLOUT = "callout", "Key idea / callout"
    TIP = "tip", "Tip"
    MISTAKE = "mistake", "Common mistake"
    WORKED_EXAMPLE = "worked_example", "Worked example"
    PRACTICE = "practice", "Practice question (show answer)"
    QUIZ = "quiz", "Quick check (multiple choice)"
    SUMMARY = "summary", "Summary list"
    IMAGE = "image", "Image / diagram"
    GRAPH = "graph", "Function graph (polynomial)"
    VIDEO = "video", "Video"
    SIMULATION = "simulation", "Interactive simulation"
    EMBED = "embed", "External embed"


MEDIA_BLOCK_TYPES = {BlockType.IMAGE, BlockType.VIDEO, BlockType.EMBED}
DATA_REQUIREMENTS = {
    BlockType.WORKED_EXAMPLE: ("steps", "a list of steps"),
    BlockType.QUIZ: ("choices", "a list of choices"),
    BlockType.SIMULATION: ("key", "the simulation key"),
    BlockType.GRAPH: ("coeffs", "polynomial coefficients, highest power first"),
}


class LessonBlock(OrderedModel):
    """One typed piece of lesson content, rendered by `templates/lessons/blocks/<block_type>.html`.

    `body` holds text (with **bold**, *italic* and $inline maths$) or LaTeX for formulas.
    `data` holds structured extras, e.g. worked-example steps, quiz choices, video chapters.
    """

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="blocks")
    block_type = models.CharField(max_length=20, choices=BlockType.choices, default=BlockType.TEXT)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    media_url = models.URLField(blank=True, help_text="Image, video or embed URL for media blocks.")
    alt_text = models.CharField(max_length=300, blank=True, help_text="Describe images for screen readers.")
    data = models.JSONField(default=dict, blank=True, help_text="Extra structured settings for this block type.")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return f"{self.get_block_type_display()} #{self.order}"

    @property
    def template_name(self):
        return f"lessons/blocks/{self.block_type}.html"

    @property
    def anchor(self):
        return f"block-{self.pk}"

    def clean(self):
        if self.block_type in MEDIA_BLOCK_TYPES and not self.media_url:
            raise ValidationError({"media_url": "This block type needs a media URL."})
        if self.block_type == BlockType.IMAGE and not self.alt_text:
            raise ValidationError({"alt_text": "Describe the image for students using screen readers."})
        requirement = DATA_REQUIREMENTS.get(self.block_type)
        if requirement and not (self.data or {}).get(requirement[0]):
            raise ValidationError({"data": f"This block needs {requirement[1]} in data['{requirement[0]}']."})
        if (
            self.block_type not in MEDIA_BLOCK_TYPES
            and self.block_type not in DATA_REQUIREMENTS
            and not (self.body or self.title)
        ):
            raise ValidationError({"body": "This block needs some content."})


class ResourceKind(models.TextChoices):
    PDF = "pdf", "PDF"
    GLOSSARY = "glossary", "Glossary"
    LINK = "link", "Link"


class CourseResource(OrderedModel):
    """Downloads and references shown beside a course (formula sheet, glossary…)."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="resources")
    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=10, choices=ResourceKind.choices, default=ResourceKind.PDF)
    url = models.URLField(blank=True)
    file = models.FileField(upload_to="course-resources/", blank=True)
    detail = models.CharField(max_length=60, blank=True, help_text="Short note, e.g. 'PDF · 140 KB' or '86 terms'.")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.title

    @property
    def href(self):
        return self.file.url if self.file else self.url

    def clean(self):
        if not self.url and not self.file:
            raise ValidationError("Upload a file or give a link.")
