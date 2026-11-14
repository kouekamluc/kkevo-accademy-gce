"""Student feedback on lessons: what students report, so mistakes get fixed first where most people hit them."""

from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.learning.models import LessonFeedback

from ._common import _context, staff_required

PER_PAGE = 25


@staff_required
def feedback(request):
    status = request.GET.get("status", "new")
    qs = LessonFeedback.objects.select_related("lesson__topic__module__course", "question__practice_set__topic__module__course", "user")
    if status in LessonFeedback.Status.values:
        qs = qs.filter(status=status)
    else:
        status = ""
    counts = dict(LessonFeedback.objects.values_list("status").annotate(n=Count("pk")))
    # Lessons with the most open reports first: the places that most need a fix.
    hot = (LessonFeedback.objects.filter(status=LessonFeedback.Status.NEW, lesson__isnull=False)
           .values("lesson_id", "lesson__title").annotate(n=Count("pk")).order_by("-n")[:5])
    hot_questions = (LessonFeedback.objects.filter(status=LessonFeedback.Status.NEW, question__isnull=False)
                     .values("question__practice_set_id", "question__practice_set__title")
                     .annotate(n=Count("pk")).order_by("-n")[:5])
    page = Paginator(qs, PER_PAGE).get_page(request.GET.get("page"))
    tabs = [("", "All", sum(counts.values()))] + [(v, label, counts.get(v, 0)) for v, label in LessonFeedback.Status.choices]
    return render(request, "studio/feedback.html", _context(
        request, page=page, status=status, tabs=tabs, hot=hot, hot_questions=hot_questions, studio_active="feedback",
        next_statuses=[(v, l) for v, l in LessonFeedback.Status.choices if v != LessonFeedback.Status.NEW]))


@staff_required
@require_POST
def feedback_status(request, pk):
    item = get_object_or_404(LessonFeedback, pk=pk)
    new = request.POST.get("status")
    if new in LessonFeedback.Status.values:
        item.status = new
        item.handled_at = timezone.now() if new != LessonFeedback.Status.NEW else None
        item.save(update_fields=["status", "handled_at"])
    return redirect(request.POST.get("next") or "studio:feedback")
