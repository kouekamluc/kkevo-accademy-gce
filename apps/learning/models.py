from django.conf import settings
from django.db import models

from apps.academics.models import SubjectOffering


class Enrollment(models.Model):
    """A subject in a student's plan ("In your plan")."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrollments")
    offering = models.ForeignKey(SubjectOffering, on_delete=models.CASCADE, related_name="enrollments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["offering__subject__order", "offering__subject__name"]
        constraints = [models.UniqueConstraint(fields=["user", "offering"], name="unique_enrollment")]

    def __str__(self):
        return f"{self.user} → {self.offering}"
