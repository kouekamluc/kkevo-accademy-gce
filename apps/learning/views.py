from collections import defaultdict
from datetime import date, datetime, time, timedelta

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.academics.models import Subject
from apps.accounts.decorators import onboarding_required
from apps.accounts.utils import get_profile
from apps.courses.models import Course, Lesson

from . import analytics, services
from .models import Enrollment, LessonProgress, SavedLesson, SessionKind, StudySession

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def _safe_next(request, fallback):
    next_url = request.POST.get("next", "")
    return next_url if next_url.startswith("/") and not next_url.startswith("//") else fallback


def _plan(user):
    enrollments = list(
        Enrollment.objects.filter(user=user).select_related("offering__subject")
        .prefetch_related(Prefetch("offering__courses", queryset=Course.objects.published().order_by("order", "pk")))
    )
    plan = []
    for e in enrollments:
        course = services.primary_course(e.offering.courses.all())
        plan.append({"subject": e.offering.subject, "course": course})
    return plan


def fmt_minutes(minutes):
    hours, mins = divmod(int(round(minutes)), 60)
    return f"{hours}h {mins:02d}m" if hours else f"{mins}m"


# --------------------------------------------------------------------------- progress (10)
@onboarding_required
def progress(request):
    user = request.user
    today = timezone.localdate()
    range_key = request.GET.get("range") if request.GET.get("range") in analytics.RANGES else "30d"
    start, length = analytics.period(range_key, today)
    prev_start, prev_end = start - timedelta(days=length), start - timedelta(days=1)

    plan = _plan(user)
    courses = [p["course"] for p in plan if p["course"]]
    stats = services.course_stats(user, courses)
    lesson_ids = list(services.published_lessons().filter(topic__module__course__in=courses).values_list("pk", flat=True))
    done = sum(s.done for s in stats.values())
    total = sum(s.total for s in stats.values())
    overall = round(100 * done / total) if total else 0
    gained = round(100 * analytics.completions_between(user, start, today, lesson_ids) / total) if total else 0

    attempts_now = list(analytics.completed_attempts(user, start, today))
    attempts_prev = list(analytics.completed_attempts(user, prev_start, prev_end))
    avg_now, avg_prev = analytics.average_score(attempts_now), analytics.average_score(attempts_prev)
    seconds = sum(r.seconds for r in user.daily_activity.filter(date__gte=start, date__lte=today))

    all_attempts = list(analytics.completed_attempts(user).order_by("completed_at"))
    by_course = defaultdict(list)
    for a in all_attempts:
        by_course[a.practice_set.topic.module.course_id].append(a.score)
    topics = analytics.topic_scores(user)
    mastered_by_subject = defaultdict(int)
    for entry in topics.values():
        if entry["mastered"]:
            mastered_by_subject[entry["subject"].pk] += 1

    subject_rows = []
    for p in plan:
        if not p["course"]:
            continue
        scores = by_course.get(p["course"].pk, [])
        quiz = round(sum(scores) / len(scores)) if scores else None
        subject_rows.append({"subject": p["subject"], "course": p["course"], "stat": stats[p["course"].pk], "quiz": quiz,
                             "mastered": mastered_by_subject.get(p["subject"].pk, 0)})
    subject_rows.sort(key=lambda r: -r["stat"].percent)
    strongest = sorted([r for r in subject_rows if r["quiz"] is not None], key=lambda r: -r["quiz"])[:2]

    recent_scores = [a.score for a in all_attempts[-10:]]
    correct, to_review = analytics.answer_totals(user)
    needs = sorted([e for e in topics.values() if e["needs_revision"]], key=lambda e: e["latest"])[:4]
    for e in needs:
        e["days_ago"] = (today - timezone.localtime(e["last_at"]).date()).days
        e["revise_url"] = (e["practice_set"].lesson.get_absolute_url() if e["practice_set"].lesson
                           else e["practice_set"].get_absolute_url())

    suggestions = _suggestions(user, needs, courses)
    recent = list(
        LessonProgress.objects.filter(user=user, completed_at__isnull=False)
        .select_related("lesson__topic__module__course__offering__subject").order_by("-completed_at")[:6]
    )
    scores_by_lesson = {a.practice_set.lesson_id: a.score for a in all_attempts if a.practice_set.lesson_id}
    for r in recent:
        r.score = scores_by_lesson.get(r.lesson_id)
        day = timezone.localtime(r.completed_at).date()
        r.day_label = "Today" if day == today else "Yesterday" if day == today - timedelta(days=1) else f"{day.day} {day.strftime('%b')}"

    return render(request, "learning/progress.html", {
        "range_key": range_key, "ranges": analytics.RANGES, "overall": overall, "gained": gained,
        "done": done, "total": total, "avg_now": avg_now,
        "avg_delta": (avg_now - avg_prev) if avg_now is not None and avg_prev is not None else None,
        "learning_time": fmt_minutes(seconds / 60), "per_day": round(seconds / 60 / length),
        "subject_rows": subject_rows, "strongest": strongest, "weeks": analytics.weekly_hours(user, today),
        "quiz_avg": analytics.average_score(all_attempts), "quiz_count": len(all_attempts),
        "quiz_line": _sparkline(recent_scores), "latest_score": recent_scores[-1] if recent_scores else None,
        "correct": correct, "to_review": to_review, "needs": needs, "suggestions": suggestions,
        "recent": recent, "nav_active": "progress",
    })


def _sparkline(scores, width=340, height=90):
    if len(scores) < 2:
        return None
    step = width / (len(scores) - 1)
    points = [(round(i * step, 1), round(height - (s / 100) * (height - 10) - 5, 1)) for i, s in enumerate(scores)]
    return {"points": " ".join(f"{x},{y}" for x, y in points), "last": points[-1], "width": width, "height": height}


def _suggestions(user, needs, courses):
    out = []
    if needs:
        weakest = needs[0]
        target = weakest["practice_set"].lesson
        out.append({"html_title": weakest["topic"].title, "text_before": "Re-read", "text_after": ", then retry its practice set",
                    "title": f"Revise {weakest['topic'].title}", "subject": weakest["subject"], "lesson": target,
                    "topic": weakest["topic"], "kind": SessionKind.REVISION, "minutes": 30})
    current = (LessonProgress.objects.filter(user=user, completed_at__isnull=True, lesson__topic__module__course__in=courses)
               .select_related("lesson__topic__module__course__offering__subject").order_by("-last_viewed_at").first())
    if current:
        module = current.lesson.topic.module
        left = services.module_stats(user, module.course).get(module.pk)
        remaining = (left.total - left.done) if left else 0
        out.append({"html_title": current.lesson.title, "text_before": "Finish", "text_after": f" — {remaining} lesson{'s' if remaining != 1 else ''} left in {module.title}",
                    "title": current.lesson.title, "subject": current.lesson.course.offering.subject,
                    "lesson": current.lesson, "kind": SessionKind.STUDY, "minutes": current.lesson.estimated_minutes})
    for course in courses:
        if len(out) >= 3:
            break
        nxt, prog = services.next_lesson(user, course)
        if nxt and not any(s.get("lesson") == nxt for s in out) and not prog:
            out.append({"html_title": nxt.title, "text_before": "Start", "text_after": f" in {course.offering.subject.name}",
                        "title": nxt.title, "subject": course.offering.subject, "lesson": nxt,
                        "kind": SessionKind.STUDY, "minutes": nxt.estimated_minutes})
    return out[:3]


@login_required
@require_POST
def add_suggestions(request):
    """'Add these to my planner': schedule each suggestion on the next free evenings at 17:00."""
    courses = [p["course"] for p in _plan(request.user) if p["course"]]
    needs = sorted([e for e in analytics.topic_scores(request.user).values() if e["needs_revision"]], key=lambda e: e["latest"])
    tz = timezone.get_current_timezone()
    day = timezone.localdate() + timedelta(days=1)
    created = 0
    for s in _suggestions(request.user, needs, courses):
        starts = timezone.make_aware(datetime.combine(day, time(17, 0)), tz)
        StudySession.objects.create(user=request.user, title=s["title"][:120], subject=s["subject"], lesson=s.get("lesson"),
                                    topic=s.get("topic"), kind=s["kind"], starts_at=starts,
                                    duration_minutes=max(15, min(int(s["minutes"] or 30), 120)))
        day += timedelta(days=1)
        created += 1
    messages.success(request, f"Added {created} session{'s' if created != 1 else ''} to your planner." if created
                     else "Nothing to add right now.")
    return redirect("learning:planner")


# --------------------------------------------------------------------------- planner (11)
class SessionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}), label="Start time")

    class Meta:
        model = StudySession
        fields = ("title", "subject", "lesson", "kind", "duration_minutes")
        labels = {"duration_minutes": "Duration (minutes)", "kind": "Type"}

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        offering_ids = Enrollment.objects.filter(user=user).values_list("offering_id", flat=True)
        self.fields["subject"].queryset = Subject.objects.filter(offerings__in=offering_ids).distinct()
        self.fields["subject"].required = False
        self.fields["lesson"].queryset = Lesson.objects.published().filter(
            topic__module__course__offering__in=offering_ids).select_related("topic__module__course")
        self.fields["lesson"].required = False
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "form-input")
        if self.instance.pk:
            local = timezone.localtime(self.instance.starts_at)
            self.initial.setdefault("date", local.date())
            self.initial.setdefault("start_time", local.time().replace(second=0, microsecond=0))

    def clean(self):
        data = super().clean()
        lesson, subject = data.get("lesson"), data.get("subject")
        if lesson and not subject:
            data["subject"] = lesson.course.offering.subject
        elif lesson and subject and lesson.course.offering.subject_id != subject.pk:
            self.add_error("lesson", "Choose a lesson from the selected subject.")
        return data

    def save(self, commit=True):
        session = super().save(commit=False)
        session.subject = self.cleaned_data.get("subject")
        session.starts_at = timezone.make_aware(
            datetime.combine(self.cleaned_data["date"], self.cleaned_data["start_time"]), timezone.get_current_timezone())
        if commit:
            session.save()
        return session


SUBJECT_COLOURS = ["blue", "emerald", "slate", "violet", "rose", "cyan"]


@onboarding_required
def planner(request):
    user = request.user
    profile = get_profile(user)
    today = timezone.localdate()
    try:
        anchor = date.fromisoformat(request.GET.get("date", ""))
    except ValueError:
        anchor = today
    view = "day" if request.GET.get("view") == "day" else "week"
    monday = anchor - timedelta(days=anchor.weekday())
    days = [anchor] if view == "day" else [monday + timedelta(days=i) for i in range(7)]
    tz = timezone.get_current_timezone()
    start_dt = timezone.make_aware(datetime.combine(days[0], time.min), tz)
    end_dt = timezone.make_aware(datetime.combine(days[-1], time.max), tz)
    sessions = list(StudySession.objects.filter(user=user, starts_at__range=(start_dt, end_dt))
                    .select_related("subject", "lesson__topic__module__course").order_by("starts_at"))

    # Colour by subject (stable order), revision sessions use amber, planning dashed
    subject_ids = sorted({s.subject_id for s in sessions if s.subject_id})
    colour_for = {sid: SUBJECT_COLOURS[i % len(SUBJECT_COLOURS)] for i, sid in enumerate(subject_ids)}
    hours = [timezone.localtime(s.starts_at).hour for s in sessions] + [timezone.localtime(s.ends_at).hour + 1 for s in sessions]
    first_hour = min([15] + hours) if hours else 15
    last_hour = max([21] + hours) if hours else 21
    first_hour, last_hour = max(0, min(first_hour, 15)), min(24, max(last_hour, 21))
    hour_px = 112
    now = timezone.localtime()
    columns = []
    for d in days:
        items = []
        for s in sessions:
            local = timezone.localtime(s.starts_at)
            if local.date() != d:
                continue
            top = (local.hour - first_hour + local.minute / 60) * hour_px
            is_now = s.starts_at <= now < s.ends_at and not s.is_completed
            items.append({"session": s, "top": round(top), "height": max(36, round(s.duration_minutes / 60 * hour_px) - 6),
                          "colour": "amber" if is_now else ("plan" if s.kind == SessionKind.PLANNING else colour_for.get(s.subject_id, "slate")),
                          "is_now": is_now, "time": local.strftime("%H:%M")})
        columns.append({"date": d, "label": WEEKDAYS[d.weekday()], "is_today": d == today, "items": items})
    now_top = round((now.hour - first_hour + now.minute / 60) * hour_px) if first_hour <= now.hour < last_hour else None
    legend = [{"subject": Subject.objects.get(pk=sid), "colour": colour_for[sid]} for sid in subject_ids]

    todays = [s for s in StudySession.objects.filter(user=user, starts_at__date=today).select_related("subject", "lesson__topic__module__course")]
    week_start = today - timedelta(days=today.weekday())
    week_sessions = StudySession.objects.filter(
        user=user, starts_at__range=(timezone.make_aware(datetime.combine(week_start, time.min), tz),
                                     timezone.make_aware(datetime.combine(week_start + timedelta(days=6), time.max), tz))
    ).select_related("subject")
    per_subject = defaultdict(lambda: {"count": 0, "minutes": 0})
    done_minutes = 0
    for s in week_sessions:
        key = s.subject.name if s.subject else "Other"
        per_subject[key]["count"] += 1
        per_subject[key]["minutes"] += s.duration_minutes
        if s.is_completed:
            done_minutes += s.duration_minutes
    goal = profile.daily_goal_minutes * 7

    topics = analytics.topic_scores(user)
    revision = sorted(({"entry": e, "due": analytics.revision_due(e, today)} for e in topics.values() if e["needs_revision"]),
                      key=lambda r: r["due"])[:3]
    for r in revision:
        r["label"] = analytics.due_label(r["due"], today)

    form = SessionForm(user=user, initial={"date": anchor if anchor >= today else today, "start_time": time(17, 0),
                                           "duration_minutes": 30})
    return render(request, "learning/planner.html", {
        "view": view, "anchor": anchor, "days": days, "columns": columns, "today": today,
        "hours": list(range(first_hour, last_hour)), "hour_px": hour_px, "grid_height": (last_hour - first_hour) * hour_px,
        "now_top": now_top, "legend": legend,
        "prev": (anchor - timedelta(days=1 if view == "day" else 7)).isoformat(),
        "next": (anchor + timedelta(days=1 if view == "day" else 7)).isoformat(),
        "todays": todays, "todays_done": sum(s.is_completed for s in todays),
        "week_minutes": fmt_minutes(done_minutes), "week_goal": fmt_minutes(goal),
        "week_percent": min(100, round(100 * done_minutes / goal)) if goal else 0,
        "per_subject": sorted(per_subject.items(), key=lambda kv: -kv[1]["minutes"]),
        "revision": revision, "form": form, "nav_active": "planner", "now": now,
    })


@login_required
@require_POST
def session_create(request):
    form = SessionForm(request.POST, user=request.user)
    if form.is_valid():
        session = form.save(commit=False)
        session.user = request.user
        session.save()
        messages.success(request, f"“{session.title}” added to your planner.")
        return redirect(f"{reverse('learning:planner')}?date={timezone.localtime(session.starts_at).date().isoformat()}")
    messages.error(request, "Please fix the session details: " + "; ".join(
        f"{form.fields[f].label if f in form.fields else ''} {' '.join(e)}".strip() for f, e in form.errors.items()))
    return redirect("learning:planner")


@login_required
@require_POST
def session_delete(request, pk):
    session = get_object_or_404(StudySession, pk=pk, user=request.user)
    day = timezone.localtime(session.starts_at).date().isoformat()
    session.delete()
    messages.success(request, "Session removed.")
    return redirect(f"{reverse('learning:planner')}?date={day}")


@login_required
@require_POST
def session_toggle(request, pk):
    """Tick a planner session done / not done (dashboard 'Upcoming revision', planner tasks)."""
    session = get_object_or_404(StudySession, pk=pk, user=request.user)
    session.completed_at = None if session.completed_at else timezone.now()
    session.save(update_fields=["completed_at"])
    if request.htmx:
        return render(request, "learning/_session_check.html", {"session": session, "variant": request.POST.get("variant", "")})
    return redirect(_safe_next(request, "dashboard:home"))


# --------------------------------------------------------------------------- saved lessons
@login_required
def saved(request):
    items = (SavedLesson.objects.filter(user=request.user, lesson__status="published")
             .select_related("lesson__topic__module__course__offering__subject"))
    return render(request, "learning/saved.html", {"items": items, "nav_active": "saved"})
