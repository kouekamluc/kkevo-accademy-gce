"""Practice sets and quiz flow (mockup 09).

Each question is answered with a normal POST and redirected back (POST/redirect/GET), so
the quiz works without JavaScript and survives page reloads on slow connections.
"""

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Prefetch
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.learning.models import Enrollment

from .models import Answer, Attempt, Choice, PracticeSet


def _published_set(pk):
    return get_object_or_404(
        PracticeSet.objects.select_related("topic__module__course__offering__subject", "lesson"),
        pk=pk, status="published", topic__module__course__status="published",
    )


@login_required
def index(request):
    offering_ids = Enrollment.objects.filter(user=request.user).values_list("offering_id", flat=True)
    sets = list(
        PracticeSet.objects.published()
        .filter(topic__module__course__offering_id__in=offering_ids, topic__module__course__status="published")
        .select_related("topic__module__course__offering__subject")
        .annotate(question_count=Count("questions"))
        .order_by("topic__module__course__offering__subject__order", "topic__module__order", "topic__order", "order")
    )
    last = {}
    for attempt in Attempt.objects.filter(user=request.user, completed_at__isnull=False, practice_set__in=sets).order_by("completed_at"):
        last[attempt.practice_set_id] = attempt
    groups = {}
    for s in sets:
        s.last_attempt = last.get(s.pk)
        groups.setdefault(s.subject, []).append(s)
    return render(request, "practice/index.html", {"groups": groups.items(), "nav_active": "practice"})


@login_required
@require_POST
def start(request, pk):
    practice_set = _published_set(pk)
    if not practice_set.questions.exists():
        raise Http404
    attempt = Attempt.objects.filter(user=request.user, practice_set=practice_set, completed_at__isnull=True).first()
    if attempt is None or request.POST.get("restart"):
        Attempt.objects.filter(user=request.user, practice_set=practice_set, completed_at__isnull=True).delete()
        attempt = Attempt.objects.create(user=request.user, practice_set=practice_set,
                                         total=practice_set.questions.count())
    answered = attempt.answers.count()
    return redirect("practice:question", attempt=attempt.pk, number=min(answered + 1, attempt.total))


@login_required
def start_page(request, pk):
    """GET landing for a practice set: summary and a Start button."""
    practice_set = _published_set(pk)
    questions = practice_set.questions.count()
    ongoing = Attempt.objects.filter(user=request.user, practice_set=practice_set, completed_at__isnull=True).first()
    best = max((a.score for a in Attempt.objects.filter(user=request.user, practice_set=practice_set,
                                                        completed_at__isnull=False)), default=None)
    return render(request, "practice/start.html", {"practice_set": practice_set, "question_count": questions,
                                                   "ongoing": ongoing, "best": best, "nav_active": "practice"})


def _attempt_for(request, attempt_pk):
    return get_object_or_404(Attempt.objects.select_related("practice_set__topic__module__course__offering__subject"),
                             pk=attempt_pk, user=request.user)


@login_required
def question(request, attempt, number):
    attempt = _attempt_for(request, attempt)
    questions = list(attempt.practice_set.questions.prefetch_related(
        Prefetch("choices", queryset=Choice.objects.order_by("order", "pk"))))
    if not 1 <= number <= len(questions):
        raise Http404
    q = questions[number - 1]
    answers = {a.question_id: a for a in attempt.answers.all()}
    answer = answers.get(q.pk)

    if request.method == "POST" and answer is None and attempt.completed_at is None:
        choice = get_object_or_404(Choice, pk=request.POST.get("choice") or 0, question=q)
        Answer.objects.get_or_create(attempt=attempt, question=q,
                                     defaults={"choice": choice, "is_correct": choice.is_correct})
        return redirect("practice:question", attempt=attempt.pk, number=number)
    if request.method == "POST":
        return redirect("practice:question", attempt=attempt.pk, number=number)

    correct = q.correct_choice
    why_not = None
    if answer:
        if not answer.is_correct and answer.choice.why_wrong:
            why_not = answer.choice
        else:
            why_not = next((c for c in reversed(q.choices.all()) if not c.is_correct and c.why_wrong), None)
    dots = []
    for i, item in enumerate(questions, 1):
        a = answers.get(item.pk)
        dots.append({"n": i, "state": "current" if i == number else ("right" if a and a.is_correct else "wrong" if a else "todo"),
                     "url": reverse("practice:question", args=[attempt.pk, i]) if a or i == number else ""})
    is_last = number == len(questions)
    return render(request, "practice/question.html", {
        "attempt": attempt, "practice_set": attempt.practice_set, "question": q, "number": number,
        "total": len(questions), "answer": answer, "correct": correct, "why_not": why_not, "dots": dots,
        "is_last": is_last, "progress_percent": round(100 * (len(answers)) / len(questions)),
        "next_url": reverse("practice:finish", args=[attempt.pk]) if is_last
        else reverse("practice:question", args=[attempt.pk, number + 1]),
    })


@login_required
def finish(request, attempt):
    attempt = _attempt_for(request, attempt)
    if attempt.completed_at is None:
        unanswered = attempt.practice_set.questions.exclude(answers__attempt=attempt).order_by("order", "pk").first()
        if unanswered is not None:
            number = list(attempt.practice_set.questions.order_by("order", "pk").values_list("pk", flat=True)).index(unanswered.pk) + 1
            return redirect("practice:question", attempt=attempt.pk, number=number)
        attempt.finish()
    answers = attempt.answers.select_related("question", "choice")
    return render(request, "practice/results.html", {"attempt": attempt, "practice_set": attempt.practice_set,
                                                     "answers": answers, "nav_active": "practice"})

