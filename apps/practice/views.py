"""Practice sets, quiz flow (mockup 09), timed exam mode and "Review my mistakes".

Each question is answered with a normal POST and redirected back (POST/redirect/GET), so
the quiz works without JavaScript and survives page reloads on slow connections. Opening a
hint is a POST too, so hint use is recorded even without JavaScript (HTMX only avoids the reload).
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Prefetch
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.learning.models import Enrollment

from .mastery import LEVELS, NOT_STARTED, mastery_for_topic, topic_mastery
from .models import (
    EXAM_GRACE_SECONDS, REVIEW_INTERVALS, REVIEW_SESSION_SIZE, Answer, Attempt, Choice, Confidence, MistakeCard,
    PracticeSet, Question, ReviewAnswer, ReviewSession,
)
from .reviews import live_cards, review_summary, sync_mistake_cards


def _published_set(pk):
    return get_object_or_404(
        PracticeSet.objects.select_related("topic__module__course__offering__subject", "lesson"),
        pk=pk, status="published", topic__module__course__status="published",
    )


def _with_choices(qs):
    return qs.prefetch_related(Prefetch("choices", queryset=Choice.objects.order_by("order", "pk")))


def _note_miss(user, question, fields):
    """Wrong answers, and right answers the student marked as a guess, come back for review."""
    if not fields["is_correct"] or fields["confidence"] == Confidence.GUESS:
        MistakeCard.record_miss(user, question)


# ---------------------------------------------------------------- shared question rendering

def _read_answer(request, question, hinted):
    """Grade the POSTed answer. Returns the answer's fields, or None (with a message) if it can't be read."""
    fields = question.grade(request.POST)
    if fields is None:
        if not question.is_numeric:
            raise Http404  # no choice, or a choice that isn't one of this question's choices
        messages.error(request, "Type your answer as a number, for example 3600 or 3,6.")
        return None
    confidence = request.POST.get("confidence", "")
    fields["confidence"] = confidence if confidence in Confidence.values else ""
    fields["used_hint"] = hinted
    return fields


def _feedback_context(question, answer):
    why_not = None
    if answer and not question.is_numeric:
        if not answer.is_correct and answer.choice and answer.choice.why_wrong:
            why_not = answer.choice
        else:
            why_not = next((c for c in reversed(question.choices.all()) if not c.is_correct and c.why_wrong), None)
    return {"correct": question.correct_choice, "why_not": why_not}


def _dots(questions, answers, number, url_for, show_feedback):
    dots = []
    for i, item in enumerate(questions, 1):
        a = answers.get(item.pk)
        if i == number:
            state = "current"
        elif a and not show_feedback:
            state = "answered"
        else:
            state = "right" if a and a.is_correct else "wrong" if a else "todo"
        # In a timed exam students may skip around, so every dot is a link.
        dots.append({"n": i, "state": state, "url": url_for(i) if a or i == number or not show_feedback else ""})
    return dots


def _hint_requested(request, question, owner):
    """Record that the hint was opened (owner: Attempt or ReviewSession). True if this POST was a hint request."""
    if not (request.POST.get("hint") and question.hint):
        return False
    if question.pk not in owner.hints_used:
        owner.hints_used = [*owner.hints_used, question.pk]
        owner.save(update_fields=["hints_used"])
    return True


# ---------------------------------------------------------------- practice index and sets

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
    mastery = topic_mastery(request.user)
    groups = {}
    tally = dict.fromkeys(LEVELS, 0)
    seen_topics = set()
    for s in sets:
        s.last_attempt = last.get(s.pk)
        s.mastery = mastery.get(s.topic_id, NOT_STARTED)
        if s.topic_id not in seen_topics:
            seen_topics.add(s.topic_id)
            tally[s.mastery.label] += 1
        groups.setdefault(s.subject, []).append(s)
    return render(request, "practice/index.html", {
        "groups": groups.items(), "nav_active": "practice", "review": review_summary(request.user),
        "mastery_tally": list(tally.items()) if sets else [],
    })


@login_required
@require_POST
def start(request, pk):
    practice_set = _published_set(pk)
    count = practice_set.questions.count()
    if not count:
        raise Http404
    mode = Attempt.Mode.EXAM if request.POST.get("mode") == "exam" else Attempt.Mode.PRACTICE
    open_attempts = Attempt.objects.filter(user=request.user, practice_set=practice_set, mode=mode,
                                           completed_at__isnull=True)
    attempt = open_attempts.first()
    if attempt is not None and attempt.is_expired():
        attempt.finish()  # an exam left to run out is handed in as it stands
        attempt = None
    if attempt is None or request.POST.get("restart"):
        open_attempts.filter(completed_at__isnull=True).delete()
        attempt = Attempt.objects.create(
            user=request.user, practice_set=practice_set, total=count, mode=mode,
            time_limit_seconds=PracticeSet.exam_seconds(count) if mode == Attempt.Mode.EXAM else None)
    answered = attempt.answers.count()
    return redirect("practice:question", attempt=attempt.pk, number=min(answered + 1, attempt.total))


@login_required
def start_page(request, pk):
    """GET landing for a practice set: summary, mastery level, Start and Timed exam buttons."""
    practice_set = _published_set(pk)
    questions = practice_set.questions.count()
    attempts = Attempt.objects.filter(user=request.user, practice_set=practice_set)
    ongoing = attempts.filter(completed_at__isnull=True, mode=Attempt.Mode.PRACTICE).first()
    ongoing_exam = attempts.filter(completed_at__isnull=True, mode=Attempt.Mode.EXAM).first()
    if ongoing_exam and ongoing_exam.is_expired():
        ongoing_exam = None
    best = max((a.score for a in attempts.filter(completed_at__isnull=False)), default=None)
    return render(request, "practice/start.html", {
        "practice_set": practice_set, "question_count": questions, "ongoing": ongoing, "ongoing_exam": ongoing_exam,
        "best": best, "nav_active": "practice", "mastery": mastery_for_topic(request.user, practice_set.topic_id),
        "exam_minutes": round(PracticeSet.exam_seconds(questions) / 60),
    })


def _attempt_for(request, attempt_pk):
    return get_object_or_404(Attempt.objects.select_related("practice_set__topic__module__course__offering__subject"),
                             pk=attempt_pk, user=request.user)


@login_required
def question(request, attempt, number):
    attempt = _attempt_for(request, attempt)
    questions = list(_with_choices(attempt.practice_set.questions.all()))
    if not 1 <= number <= len(questions):
        raise Http404
    q = questions[number - 1]
    answers = {a.question_id: a for a in attempt.answers.select_related("choice")}
    answer = answers.get(q.pk)
    is_open = attempt.completed_at is None
    here = reverse("practice:question", args=[attempt.pk, number])

    if request.method == "POST":
        if answer is None and is_open:
            if attempt.is_exam and attempt.is_expired(grace=EXAM_GRACE_SECONDS):
                messages.info(request, "Time’s up. Here’s how you did.")
                return redirect("practice:finish", attempt=attempt.pk)
            if not attempt.is_exam and _hint_requested(request, q, attempt):
                return redirect(here + "#hint")
            fields = _read_answer(request, q, hinted=q.pk in attempt.hints_used)
            if fields is not None:
                _, created = Answer.objects.get_or_create(attempt=attempt, question=q, defaults=fields)
                if created:
                    _note_miss(request.user, q, fields)
                if created and attempt.is_exam:  # no feedback during an exam: straight on to the next question
                    if number < len(questions):
                        return redirect("practice:question", attempt=attempt.pk, number=number + 1)
                    return redirect(here)
        return redirect(here)

    if attempt.is_exam and is_open and attempt.is_expired():
        messages.info(request, "Time’s up. Here’s how you did.")
        return redirect("practice:finish", attempt=attempt.pk)

    show_feedback = attempt.shows_feedback
    is_last = number == len(questions)
    exam_open = attempt.is_exam and is_open
    if exam_open:
        next_url = "" if is_last else reverse("practice:question", args=[attempt.pk, number + 1])
    else:
        next_url = (reverse("practice:finish", args=[attempt.pk]) if is_last
                    else reverse("practice:question", args=[attempt.pk, number + 1]))
    return render(request, "practice/question.html", {
        "attempt": attempt, "practice_set": attempt.practice_set, "question": q, "number": number,
        "total": len(questions), "answer": answer, "is_last": is_last, "next_url": next_url,
        "dots": _dots(questions, answers, number,
                      lambda i: reverse("practice:question", args=[attempt.pk, i]), show_feedback),
        "progress_percent": round(100 * len(answers) / len(questions)),
        "show_feedback": show_feedback, "hint_open": q.pk in attempt.hints_used,
        "exam_open": exam_open, "seconds_left": attempt.seconds_left() if exam_open else None,
        "unanswered_count": len(questions) - len(answers),
        "review_note": "This one comes back in Review my mistakes tomorrow."
        if answer and (not answer.is_correct or answer.lucky_guess) else "",
        **_feedback_context(q, answer),
    })


@login_required
def finish(request, attempt):
    attempt = _attempt_for(request, attempt)
    if attempt.completed_at is None:
        # Practice: every question must be answered first. Timed exam: the student may hand in
        # early (POST from "Finish exam"), and running out of time hands in automatically.
        hand_in = attempt.is_exam and (request.method == "POST" or attempt.is_expired())
        ordered = attempt.practice_set.questions.order_by("order", "pk")
        unanswered = ordered.exclude(answers__attempt=attempt).first()
        if unanswered is not None and not hand_in:
            number = list(ordered.values_list("pk", flat=True)).index(unanswered.pk) + 1
            return redirect("practice:question", attempt=attempt.pk, number=number)
        attempt.finish()
    if request.method == "POST":
        return redirect("practice:finish", attempt=attempt.pk)
    by_question = {a.question_id: a for a in attempt.answers.select_related("choice", "question")}
    rows = [{"question": q, "answer": by_question.get(q.pk)} for q in attempt.practice_set.questions.all()]
    return render(request, "practice/results.html", {
        "attempt": attempt, "practice_set": attempt.practice_set, "rows": rows, "nav_active": "practice",
        "mastery": mastery_for_topic(request.user, attempt.practice_set.topic_id),
        "hint_count": sum(a.used_hint for a in by_question.values()),
        "guess_count": sum(a.lucky_guess for a in by_question.values()),
        "unanswered_count": sum(r["answer"] is None for r in rows),
        "review_count": sum(1 for a in by_question.values() if not a.is_correct or a.lucky_guess),
    })


# ---------------------------------------------------------------- review my mistakes

@login_required
def review(request):
    summary = review_summary(request.user)
    due_cards = (live_cards(request.user).filter(due_on__lte=timezone.localdate())
                 .select_related("question__practice_set__topic__module__course__offering__subject")
                 [:REVIEW_SESSION_SIZE])
    return render(request, "practice/review.html", {
        "review": summary, "due_cards": due_cards, "session_size": REVIEW_SESSION_SIZE,
        "intervals": REVIEW_INTERVALS, "nav_active": "practice"})


@login_required
@require_POST
def review_start(request):
    open_sessions = ReviewSession.objects.filter(user=request.user, completed_at__isnull=True)
    session = open_sessions.first()
    if session is not None and not request.POST.get("restart"):
        answered = session.answers.count()
        return redirect("practice:review_question", session=session.pk, number=min(answered + 1, max(session.total, 1)))
    sync_mistake_cards(request.user)
    ids = list(live_cards(request.user).filter(due_on__lte=timezone.localdate())
               .values_list("question_id", flat=True)[:REVIEW_SESSION_SIZE])
    if not ids:
        messages.info(request, "Nothing to review right now. Questions you miss come back here after a day.")
        return redirect("practice:review")
    open_sessions.delete()
    session = ReviewSession.objects.create(user=request.user, question_ids=ids)
    return redirect("practice:review_question", session=session.pk, number=1)


def _session_for(request, pk):
    session = get_object_or_404(ReviewSession, pk=pk, user=request.user)
    by_id = {q.pk: q for q in _with_choices(
        Question.objects.filter(pk__in=session.question_ids).select_related("practice_set__topic"))}
    return session, [by_id[i] for i in session.question_ids if i in by_id]


@login_required
def review_question(request, session, number):
    session, questions = _session_for(request, session)
    if not 1 <= number <= len(questions):
        raise Http404
    q = questions[number - 1]
    answers = {a.question_id: a for a in session.answers.select_related("choice")}
    answer = answers.get(q.pk)
    here = reverse("practice:review_question", args=[session.pk, number])

    if request.method == "POST":
        if answer is None and session.completed_at is None:
            if _hint_requested(request, q, session):
                return redirect(here + "#hint")
            fields = _read_answer(request, q, hinted=q.pk in session.hints_used)
            if fields is not None:
                _, created = ReviewAnswer.objects.get_or_create(session=session, question=q, defaults=fields)
                card = MistakeCard.objects.filter(user=request.user, question=q).first()
                if created and card is not None:
                    card.record_review(fields["is_correct"] and fields["confidence"] != Confidence.GUESS,
                                       hinted=fields["used_hint"])
        return redirect(here)

    is_last = number == len(questions)
    return render(request, "practice/review_question.html", {
        "session": session, "question": q, "number": number, "total": len(questions), "answer": answer,
        "dots": _dots(questions, answers, number,
                      lambda i: reverse("practice:review_question", args=[session.pk, i]), True),
        "is_last": is_last, "progress_percent": round(100 * len(answers) / len(questions)),
        "next_url": reverse("practice:review_finish", args=[session.pk]) if is_last
        else reverse("practice:review_question", args=[session.pk, number + 1]),
        "show_feedback": True, "hint_open": q.pk in session.hints_used, "from_set": q.practice_set,
        "review_note": _review_note(request.user, q) if answer else "",
        **_feedback_context(q, answer),
    })


def _review_note(user, question):
    card = MistakeCard.objects.filter(user=user, question=question).first()
    if card is None:
        return ""
    if card.retired_at:
        return "Cleared — this one is off your review list."
    days = (card.due_on - timezone.localdate()).days
    return "Comes back tomorrow." if days <= 1 else f"Comes back in {days} days."


@login_required
def review_finish(request, session):
    session, questions = _session_for(request, session)
    answers = {a.question_id: a for a in session.answers.select_related("choice", "question")}
    if session.completed_at is None:
        unanswered = next((i for i, q in enumerate(questions, 1) if q.pk not in answers), None)
        if unanswered is not None:
            return redirect("practice:review_question", session=session.pk, number=unanswered)
        session.completed_at = timezone.now()
        session.save(update_fields=["completed_at"])
    cards = {c.question_id: c for c in MistakeCard.objects.filter(user=request.user, question__in=questions)}
    rows = [{"question": q, "answer": answers.get(q.pk), "card": cards.get(q.pk)} for q in questions]
    return render(request, "practice/review_results.html", {
        "session": session, "rows": rows, "total": len(questions), "nav_active": "practice",
        "correct": sum(1 for a in answers.values() if a.is_correct),
        "cleared": sum(1 for r in rows if r["card"] and r["card"].retired_at),
        "review": review_summary(request.user),
    })
