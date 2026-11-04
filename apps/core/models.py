from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class OrderedModel(models.Model):
    """Gives a model a manual display order.

    `order` is intentionally not unique: admins reorder by editing numbers and a
    temporary collision must not raise an IntegrityError. Ties fall back to pk.
    """

    order = models.PositiveIntegerField(default=0, db_index=True, help_text="Lower numbers are shown first.")

    class Meta:
        abstract = True
        ordering = ["order", "pk"]


class PublicationStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PUBLISHED = "published", "Published"
    ARCHIVED = "archived", "Archived"


class PublishedQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=PublicationStatus.PUBLISHED)
