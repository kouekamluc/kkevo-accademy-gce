"""Saved lessons."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ..models import SavedLesson


# --------------------------------------------------------------------------- saved lessons
@login_required
def saved(request):
    items = (SavedLesson.objects.filter(user=request.user, lesson__status="published")
             .select_related("lesson__topic__module__course__offering__subject"))
    return render(request, "learning/saved.html", {"items": items, "nav_active": "saved"})
