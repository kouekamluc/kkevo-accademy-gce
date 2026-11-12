"""Small template filters shared across the site."""

from django import template
from django.utils import timezone
from django.utils.timesince import timesince

register = template.Library()


@register.filter
def ago(value):
    """"just now", "5 minutes ago", "2 hours ago": the biggest unit only, never "0 minutes ago"."""
    if not value:
        return ""
    if (timezone.now() - value).total_seconds() < 60:
        return "just now"
    return timesince(value).split(",")[0].replace("\xa0", " ") + " ago"
