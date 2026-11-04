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


class Lesson(OrderedModel, TimeStampedModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    summary = models.CharField(max_length=300, blank=True)
    lesson_type = models.CharField(max_length=12, choices=LessonType.choices, default=LessonType.READING)
    estimated_minutes = models.PositiveSmallIntegerField(default=10)
    status = models.CharField(max_length=10, choices=PublicationStatus.choices, default=PublicationStatus.DRAFT)
    curriculum_references = models.ManyToManyField(CurriculumReference, blank=True, related_name="lessons")

    objects = PublishedQuerySet.as_manager()

    class Meta(OrderedModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=["topic", "slug"], name="unique_lesson_slug_per_topic"),
        ]

    def __str__(self):
        return self.title


class BlockType(models.TextChoices):
    HEADING = "heading", "Heading"
    TEXT = "text", "Text"
    FORMULA = "formula", "Formula"
    CALLOUT = "callout", "Key idea / callout"
    WORKED_EXAMPLE = "worked_example", "Worked example"
    IMAGE = "image", "Image"
    VIDEO = "video", "Video"
    EMBED = "embed", "Interactive embed"


MEDIA_BLOCK_TYPES = {BlockType.IMAGE, BlockType.VIDEO, BlockType.EMBED}


class LessonBlock(OrderedModel):
    """One typed piece of lesson content. Rendered by block_type in the lesson player."""

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="blocks")
    block_type = models.CharField(max_length=20, choices=BlockType.choices, default=BlockType.TEXT)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    media_url = models.URLField(blank=True, help_text="Image, video or embed URL for media blocks.")
    data = models.JSONField(default=dict, blank=True, help_text="Extra structured settings for this block type.")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return f"{self.get_block_type_display()} #{self.order}"

    def clean(self):
        if self.block_type in MEDIA_BLOCK_TYPES and not self.media_url:
            raise ValidationError({"media_url": "This block type needs a media URL."})
        if self.block_type not in MEDIA_BLOCK_TYPES and not (self.body or self.title):
            raise ValidationError({"body": "This block needs some content."})
