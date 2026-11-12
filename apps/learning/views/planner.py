"""Study planner (mockup 11): sessions, the exam countdown, rest days and ticking a session off."""

from collections import defaultdict
from datetime import date, datetime, time, timedelta
import uuid

from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_POST

from .. import analytics, autoplan, motivation, services
from ..models import Enrollment, LinkPurpose, PrivateLink, RestDay, SessionKind, StudySession
from apps.academics.models import Subject
from apps.accounts.decorators import onboarding_required
from apps.accounts.models import StudentProfile
from apps.accounts.utils import get_profile
from apps.courses.models import Lesson

from ._common import WEEKDAYS, _plan, _safe_next, fmt_minutes
from .links import _link_url


# --------------------------------------------------------------------------- planner (11)
class SessionForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time"}), label="Start time")

    class Meta:
        model = StudySession
        fields = ("title", "subject", "lesson", "kind", "duration_minutes")
        labels = {"duration_minutes": "Duration (minutes)", "kind": "Type"}

    repeat_days = forms.TypedMultipleChoiceField(
        choices=list(enumerate(WEEKDAYS)), coerce=int, required=False, label="Repeat on",
        widget=forms.CheckboxSelectMultiple(attrs={"class": "h-5 w-5 rounded border-slate-300 text-primary"}))
    repeat_weeks = forms.IntegerField(min_value=1, max_value=20, required=False, initial=4, label="For how many weeks")
    scope = forms.ChoiceField(choices=[("one", "Only this session"), ("future", "This and later sessions in the series")],
                              required=False, initial="one", widget=forms.RadioSelect(attrs={"class": "h-5 w-5 text-primary"}),
                              label="Apply changes to")

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_starts_at = self.instance.starts_at if self.instance.pk else None
        if self.instance.pk:
            del self.fields["repeat_days"], self.fields["repeat_weeks"]
            if not self.instance.series:
                del self.fields["scope"]
        else:
            del self.fields["scope"]
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
        if data.get("repeat_days") and not data.get("repeat_weeks"):
            self.add_error("repeat_weeks", "Say for how many weeks the session repeats.")
        return data

    def save_series(self, user):
        """Create one session, or one per chosen weekday for N weeks (shared `series`)."""
        first = self.cleaned_data["date"]
        days = self.cleaned_data.get("repeat_days") or []
        dates = motivation.recurrence_dates(first, days, self.cleaned_data["repeat_weeks"]) if days else [first]
        series = uuid.uuid4() if len(dates) > 1 else None
        tz = timezone.get_current_timezone()
        template = super().save(commit=False)
        created = []
        with transaction.atomic():
            for d in dates:
                created.append(StudySession.objects.create(
                    user=user, title=template.title, subject=self.cleaned_data.get("subject"), lesson=template.lesson,
                    kind=template.kind, duration_minutes=template.duration_minutes, series=series,
                    starts_at=timezone.make_aware(datetime.combine(d, self.cleaned_data["start_time"]), tz)))
        return created

    def save_edit(self):
        """Save this session; with scope 'future' also update later sessions of its series (keeping their dates)."""
        session = self.save()
        if self.cleaned_data.get("scope") == "future" and session.series:
            tz = timezone.get_current_timezone()
            later = StudySession.objects.filter(user=session.user, series=session.series,
                                                starts_at__gt=self.original_starts_at).exclude(pk=session.pk)
            for other in later:
                local_day = timezone.localtime(other.starts_at).date()
                other.starts_at = timezone.make_aware(datetime.combine(local_day, self.cleaned_data["start_time"]), tz)
                other.title, other.subject, other.lesson = session.title, session.subject, session.lesson
                other.kind, other.duration_minutes = session.kind, session.duration_minutes
                other.save(update_fields=["starts_at", "title", "subject", "lesson", "kind", "duration_minutes"])
        return session

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
    full_day = request.GET.get("hours") == "all"
    first_hour, last_hour = (max(0, min(first_hour, 6)), min(24, max(last_hour, 23))) if full_day else         (max(0, min(first_hour, 15)), min(24, max(last_hour, 21)))
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
    week_has_sessions = any(c["items"] for c in columns)
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

    missed = [s for s in StudySession.objects.filter(user=user, completed_at__isnull=True, starts_at__gte=now - timedelta(days=14),
                                                     starts_at__lt=now).select_related("subject").order_by("-starts_at")
              if s.ends_at < now][:5]
    has_plan = any(p["course"] for p in _plan(user))
    form = SessionForm(user=user, initial={"date": anchor if anchor >= today else today, "start_time": time(17, 0),
                                           "duration_minutes": 30, "repeat_weeks": 4})
    rest_this_week = RestDay.objects.filter(user=user, date__gte=week_start, date__lte=week_start + timedelta(days=6)).first()
    links = {link.purpose: link for link in PrivateLink.objects.filter(user=user)}
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
        "revision": revision, "form": form, "missed": missed, "full_day": full_day, "first_hour": first_hour,
        "week_has_sessions": week_has_sessions, "has_plan": has_plan, "week_monday": monday, "daily_goal": profile.daily_goal_minutes,
        "plan_weekdays": [{"n": i, "label": WEEKDAYS[i], "on": i < 6} for i in range(7)],
        "can_plan": monday + timedelta(days=6) >= today, "nav_active": "planner", "now": now,
        "countdown": _countdown(user, profile, today), "exam_form": ExamDateForm(instance=profile),
        "rest_this_week": rest_this_week, "rest_today": bool(rest_this_week and rest_this_week.date == today),
        "calendar_link": links.get(LinkPurpose.CALENDAR),
        "calendar_url": _link_url(request, links.get(LinkPurpose.CALENDAR)),
        "calendar_webcal": _link_url(request, links.get(LinkPurpose.CALENDAR)).replace("https://", "webcal://", 1)
            .replace("http://", "webcal://", 1),
    })


def _form_errors(form):
    return "; ".join(f"{form.fields[f].label if f in form.fields else ''} {' '.join(e)}".strip()
                     for f, e in form.errors.items())


def _planner_at(day):
    return redirect(f"{reverse('learning:planner')}?date={day.isoformat()}")


@login_required
@require_POST
def session_create(request):
    form = SessionForm(request.POST, user=request.user)
    if form.is_valid():
        created = form.save_series(request.user)
        if not created:
            messages.error(request, "None of the chosen days fall on or after the start date.")
            return redirect("learning:planner")
        first = created[0]
        if len(created) > 1:
            messages.success(request, f"“{first.title}” added {len(created)} times to your planner.")
        else:
            messages.success(request, f"“{first.title}” added to your planner.")
        return _planner_at(timezone.localtime(first.starts_at).date())
    messages.error(request, "Please fix the session details: " + _form_errors(form))
    return redirect("learning:planner")


@onboarding_required
def session_edit(request, pk):
    session = get_object_or_404(StudySession, pk=pk, user=request.user)
    if request.method == "POST":
        form = SessionForm(request.POST, instance=session, user=request.user)
        if form.is_valid():
            session = form.save_edit()
            messages.success(request, f"“{session.title}” updated.")
            return _planner_at(timezone.localtime(session.starts_at).date())
    else:
        form = SessionForm(instance=session, user=request.user)
    later = (StudySession.objects.filter(user=request.user, series=session.series, starts_at__gt=session.starts_at).count()
             if session.series else 0)
    return render(request, "learning/session_edit.html", {"form": form, "session": session, "later": later,
                                                          "nav_active": "planner"})


@login_required
@require_POST
def session_delete(request, pk):
    session = get_object_or_404(StudySession, pk=pk, user=request.user)
    day = timezone.localtime(session.starts_at).date()
    if request.POST.get("scope") == "future" and session.series:
        removed, _ = StudySession.objects.filter(user=request.user, series=session.series,
                                                 starts_at__gte=session.starts_at).delete()
        messages.success(request, f"Removed {removed} session{'s' if removed != 1 else ''} from the series.")
    else:
        session.delete()
        messages.success(request, "Session removed.")
    return _planner_at(day)


# --------------------------------------------------------------------------- exam countdown
class ExamDateForm(forms.ModelForm):
    exam_date = forms.DateField(required=False, label="Date of your first GCE paper",
                                widget=forms.DateInput(attrs={"type": "date", "class": "form-input"}),
                                help_text="Copy it from the official GCE timetable your school gives you.")

    class Meta:
        model = StudentProfile
        fields = ("exam_date",)

    def clean_exam_date(self):
        value = self.cleaned_data.get("exam_date")
        today = timezone.localdate()
        if value and value < today:
            raise forms.ValidationError("Choose a date that is still ahead.")
        if value and value > today + timedelta(days=3 * 366):
            raise forms.ValidationError("Choose a date within the next three years.")
        return value


def _countdown(user, profile, today):
    if not profile.exam_date:
        return None
    courses = [p["course"] for p in _plan(user) if p["course"]]
    stats = services.course_stats(user, courses)
    lesson_ids = services.published_lessons().filter(topic__module__course__in=courses).values_list("pk", flat=True)
    return motivation.exam_countdown(profile.exam_date, sum(s.done for s in stats.values()),
                                     sum(s.total for s in stats.values()),
                                     motivation.recent_completions(user, today, lesson_ids=lesson_ids), today)


@login_required
@require_POST
def exam_date(request):
    form = ExamDateForm(request.POST, instance=get_profile(request.user))
    if form.is_valid():
        form.save()
        messages.success(request, "Exam date saved." if form.cleaned_data["exam_date"] else "Exam date removed.")
    else:
        messages.error(request, " ".join(form.errors.get("exam_date", ["Enter a valid date."])))
    return redirect(_safe_next(request, reverse("learning:planner")))


# --------------------------------------------------------------------------- rest days
@login_required
@require_POST
def rest_day(request):
    """Plan (or cancel) a rest day: it keeps the streak without asking for study that day."""
    try:
        day = date.fromisoformat(request.POST.get("date", ""))
    except ValueError:
        day = timezone.localdate()
    existing = RestDay.objects.filter(user=request.user, date=day).first()
    if existing:
        existing.delete()
        messages.success(request, "Rest day cancelled.")
    else:
        allowed, reason = motivation.can_rest(request.user, day)
        if allowed:
            RestDay.objects.create(user=request.user, date=day)
            messages.success(request, "Rest day planned. Your streak is safe — enjoy the break."
                             if day == timezone.localdate() else f"Rest day planned for {day:%A %d %B}.")
        else:
            messages.error(request, reason)
    return redirect(_safe_next(request, reverse("learning:planner")))


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


# --------------------------------------------------------------------------- automatic planning
@login_required
@require_POST
def plan_week(request):
    """'Plan my week': fill the chosen days with the student's next lessons and due revisions."""
    user = request.user
    profile = get_profile(user)
    today = timezone.localdate()
    try:
        first_day = date.fromisoformat(request.POST.get("date", ""))
    except ValueError:
        first_day = today
    first_day = first_day - timedelta(days=first_day.weekday())
    weekdays = {int(d) for d in request.POST.getlist("days") if d.isdigit() and 0 <= int(d) <= 6}
    try:
        start_time = time.fromisoformat(request.POST.get("start_time") or "17:00")
    except ValueError:
        start_time = None
    if not weekdays or start_time is None:
        messages.error(request, "Choose at least one study day and a start time.")
        return _planner_at(first_day)
    weeks = 2 if request.POST.get("weeks") == "2" else 1
    courses = [p["course"] for p in _plan(user) if p["course"]]
    if not courses:
        messages.error(request, "Choose your subjects first, then the planner can fill your week.")
        return redirect("learning:planner")
    start = max(first_day, today)
    plan = autoplan.build_plan(user, profile, courses, start, (first_day + timedelta(days=7 * weeks) - start).days, weekdays, start_time)
    if not plan:
        messages.info(request, "Nothing to add: those days are full, resting, already behind you, or you have no lessons left to plan.")
        return _planner_at(first_day)
    created = autoplan.save_plan(user, plan)
    minutes = sum(s.duration_minutes for s in created)
    messages.success(request, f"Planned {len(created)} session{'s' if len(created) != 1 else ''} "
                              f"({fmt_minutes(minutes)} of study). Move or delete any you don't want.")
    return _planner_at(timezone.localtime(created[0].starts_at).date())


@login_required
@require_POST
def week_clear(request):
    """Remove this week's sessions that are still to come and not done (undo for 'Plan my week')."""
    try:
        day = date.fromisoformat(request.POST.get("date", ""))
    except ValueError:
        day = timezone.localdate()
    monday = day - timedelta(days=day.weekday())
    tz = timezone.get_current_timezone()
    start = max(timezone.now(), timezone.make_aware(datetime.combine(monday, time.min), tz))
    end = timezone.make_aware(datetime.combine(monday + timedelta(days=6), time.max), tz)
    removed, _ = StudySession.objects.filter(user=request.user, completed_at__isnull=True, starts_at__range=(start, end)).delete()
    messages.success(request, f"Cleared {removed} upcoming session{'s' if removed != 1 else ''} this week."
                     if removed else "Nothing to clear: no upcoming sessions this week.")
    return _planner_at(day)


@login_required
@require_POST
def session_reschedule(request, pk):
    """Move a missed (or any) session to the next time its clock time comes round."""
    session = get_object_or_404(StudySession, pk=pk, user=request.user)
    tz = timezone.get_current_timezone()
    clock = timezone.localtime(session.starts_at).time()
    now = timezone.now()
    day = timezone.localdate()
    while timezone.make_aware(datetime.combine(day, clock), tz) <= now:
        day += timedelta(days=1)
    session.starts_at = timezone.make_aware(datetime.combine(day, clock), tz)
    session.save(update_fields=["starts_at"])
    messages.success(request, f"“{session.title}” moved to {day:%A %d %B}, {clock:%H:%M}.")
    return _planner_at(day)
