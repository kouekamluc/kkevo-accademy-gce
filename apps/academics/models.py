from django.core.exceptions import ValidationError
from django.db import models

from apps.core.models import OrderedModel, PublicationStatus, TimeStampedModel


class ExamLevel(models.TextChoices):
    ORDINARY = "O", "GCE Ordinary Level"
    ADVANCED = "A", "GCE Advanced Level"


class AcademicLevel(OrderedModel):
    """A class a student is in: Form 5, Lower Sixth, Upper Sixth."""

    code = models.CharField(max_length=10, unique=True, help_text="Short code, e.g. F5, L6, U6.")
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    exam_level = models.CharField(max_length=1, choices=ExamLevel.choices)
    tagline = models.CharField(
        max_length=60, blank=True, help_text="Badge on the level card, e.g. 'A Level foundation'."
    )
    description = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name


class AcademicPathway(OrderedModel):
    """A stream of study, e.g. Arts or Science. Configurable in the admin."""

    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    description = models.CharField(max_length=200, blank=True)
    icon_text = models.CharField(max_length=4, blank=True, help_text="Glyph for the onboarding card, e.g. λ or Aa.")
    accent = models.CharField(max_length=10, default="blue", choices=[
        ("blue", "Blue"), ("emerald", "Emerald"), ("amber", "Amber"), ("slate", "Slate")])
    is_active = models.BooleanField(default=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name


class SubjectAccent(models.TextChoices):
    BLUE = "blue", "Blue"
    EMERALD = "emerald", "Emerald"
    AMBER = "amber", "Amber"
    SLATE = "slate", "Slate"


class SubjectIcon(models.TextChoices):
    TEXT = "", "Use icon text"
    DNA = "dna", "DNA (biology)"
    MAP = "map", "Map (geography)"
    CHART = "chart", "Chart (economics)"
    BOOK = "book", "Book"


class SubjectCategory(models.TextChoices):
    SCIENCES = "sciences", "Sciences"
    LANGUAGES = "languages", "Languages"
    HUMANITIES = "humanities", "Humanities"
    TECHNICAL = "technical", "Technical"
    BUSINESS = "business", "Business"
    OTHER = "other", "Other"


class Subject(OrderedModel):
    """A subject independent of level, e.g. Mathematics."""

    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    summary = models.CharField(max_length=160, blank=True, help_text="One line shown on subject cards.")
    category = models.CharField(max_length=12, choices=SubjectCategory.choices, default=SubjectCategory.OTHER)
    icon_text = models.CharField(
        max_length=8, blank=True, help_text="Short glyph shown in the icon tile, e.g. x², F, H₂O, Aa."
    )
    icon = models.CharField(max_length=10, choices=SubjectIcon.choices, blank=True, default=SubjectIcon.TEXT)
    accent = models.CharField(max_length=10, choices=SubjectAccent.choices, default=SubjectAccent.BLUE)
    is_featured = models.BooleanField(default=False, help_text="Show on the landing page.")
    is_active = models.BooleanField(default=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name

    def card_meta(self):
        """'Science · 3 levels' — needs `active_offerings` prefetched (see core.views)."""
        offerings = getattr(self, "active_offerings", None)
        if offerings is None:
            offerings = list(SubjectOffering.objects.active().filter(subject=self).select_related("level"))
        pathways = sorted({p for o in offerings for p in o.pathways.all()}, key=lambda p: (p.order, p.pk))
        parts = []
        if pathways:
            parts.append(" & ".join(p.name for p in pathways))
        if len(offerings) == 1:
            parts.append(offerings[0].level.name)
        elif offerings:
            parts.append(f"{len(offerings)} levels")
        return " · ".join(parts)

    def clean(self):
        if not self.icon and not self.icon_text:
            raise ValidationError({"icon_text": "Provide icon text or choose an icon."})


class SubjectOfferingQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True, subject__is_active=True, level__is_active=True)


class SubjectOffering(TimeStampedModel):
    """A subject as taught at one academic level, e.g. Form 5 Mathematics."""

    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="offerings")
    level = models.ForeignKey(AcademicLevel, on_delete=models.PROTECT, related_name="offerings")
    pathways = models.ManyToManyField(
        AcademicPathway, related_name="offerings", help_text="Pathways in which this subject is offered."
    )
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    objects = SubjectOfferingQuerySet.as_manager()

    class Meta:
        ordering = ["level__order", "subject__order", "subject__name"]
        constraints = [
            models.UniqueConstraint(fields=["subject", "level"], name="unique_subject_per_level"),
        ]

    def __str__(self):
        return f"{self.level.name} {self.subject.name}"


class Syllabus(TimeStampedModel):
    """A versioned syllabus for one subject offering.

    Content is entered by staff from official documents; nothing is seeded.
    """

    offering = models.ForeignKey(SubjectOffering, on_delete=models.CASCADE, related_name="syllabi")
    title = models.CharField(max_length=200)
    version = models.CharField(max_length=40, help_text="e.g. '2024 revision'.")
    exam_board = models.CharField(max_length=120, blank=True, default="Cameroon GCE Board")
    is_official = models.BooleanField(
        default=False, help_text="Tick only when entered verbatim from an official syllabus document."
    )
    source_url = models.URLField(blank=True)
    effective_from = models.DateField(null=True, blank=True)
    effective_to = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=PublicationStatus.choices, default=PublicationStatus.DRAFT)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "syllabi"
        ordering = ["offering", "-effective_from", "version"]
        constraints = [
            models.UniqueConstraint(fields=["offering", "version"], name="unique_syllabus_version"),
        ]

    def __str__(self):
        return f"{self.offering} — {self.version}"

    def clean(self):
        if self.effective_from and self.effective_to and self.effective_to < self.effective_from:
            raise ValidationError({"effective_to": "End date must be after the start date."})


class CurriculumReference(OrderedModel):
    """One item of a syllabus (section, objective…), possibly nested."""

    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name="references")
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    code = models.CharField(max_length=30, help_text="Reference code as written in the syllabus.")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta(OrderedModel.Meta):
        constraints = [
            models.UniqueConstraint(fields=["syllabus", "code"], name="unique_reference_code_per_syllabus"),
        ]

    def __str__(self):
        return f"{self.code} {self.title}"

    def clean(self):
        if self.parent_id and self.parent.syllabus_id != self.syllabus_id:
            raise ValidationError({"parent": "Parent must belong to the same syllabus."})
        if self.parent_id and self.pk and self.parent_id == self.pk:
            raise ValidationError({"parent": "A reference cannot be its own parent."})
