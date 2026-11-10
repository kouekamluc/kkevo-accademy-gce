"""Five-step onboarding wizard from mockup 07.

1 Create account (accounts.views.register) · 2 Academic level · 3 Arts or Science
4 Choose subjects · 5 Enter dashboard. Each step is its own URL and saves as it goes,
so a student can leave and resume.
"""

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils import timezone

from apps.academics.models import SubjectOffering
from apps.courses.models import Lesson
from apps.learning import services
from apps.learning.models import Enrollment

from .forms import MIX, LevelForm, StreamForm, SubjectsForm
from .utils import get_profile

STEPS = ["Create account", "Academic level", "Arts or Science", "Choose subjects", "Enter dashboard"]
STREAM_DONE_KEY = "onboarding_stream_chosen"


def _context(step, **extra):
    return {"step": step, "steps": STEPS, "total_steps": len(STEPS), **extra}


def _offerings_for(profile):
    """Subjects of the student's class and stream that already have lessons."""
    return (SubjectOffering.objects.for_class(profile.level, profile.pathway).with_content()
            .select_related("subject").order_by("subject__order", "subject__name"))


# On a first visit we tick a manageable starter set, not every subject: a long plan buries the dashboard.
DEFAULT_SUBJECTS = 6
CORE_SUBJECTS = ("Mathematics", "English Language")


def _default_selection(offerings):
    """Primary keys to pre-tick: the core subjects first, then the class's others in their usual order."""
    rows = list(offerings.values_list("pk", "subject__name"))
    rows.sort(key=lambda row: row[1] not in CORE_SUBJECTS)  # stable: core first, order kept otherwise
    return [pk for pk, _ in rows[:DEFAULT_SUBJECTS]]


def _coming_soon(profile):
    """Names of the class's subjects whose lessons are not ready yet (shown, but not selectable)."""
    ready = SubjectOffering.objects.for_class(profile.level, profile.pathway).with_content().values("pk")
    return list(SubjectOffering.objects.for_class(profile.level, profile.pathway).exclude(pk__in=ready)
                .order_by("subject__order", "subject__name").values_list("subject__name", flat=True))


@login_required
def start(request):
    """Send the student to the first unfinished step."""
    profile = get_profile(request.user)
    if not profile.level_id:
        return redirect("accounts:onboarding_level")
    if not profile.is_onboarded and not request.session.get(STREAM_DONE_KEY):
        return redirect("accounts:onboarding_stream")
    if not profile.is_onboarded:
        return redirect("accounts:onboarding_subjects")
    return redirect("accounts:onboarding_done")


@login_required
def level(request):
    profile = get_profile(request.user)
    form = LevelForm(request.POST if request.method == "POST" else None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("accounts:onboarding_stream")
    return render(request, "onboarding/level.html", _context(2, form=form, levels=form.fields["level"].queryset,
                                                             selected=form["level"].value()))


@login_required
def stream(request):
    profile = get_profile(request.user)
    if not profile.level_id:
        return redirect("accounts:onboarding_level")
    initial = {"stream": profile.pathway.slug if profile.pathway_id else (MIX if profile.is_onboarded else None)}
    form = StreamForm(request.POST if request.method == "POST" else None, initial=initial)
    if request.method == "POST" and form.is_valid():
        profile.pathway = form.selected_pathway
        profile.save(update_fields=["pathway", "updated_at"])
        request.session[STREAM_DONE_KEY] = True
        return redirect("accounts:onboarding_subjects")
    return render(request, "onboarding/stream.html", _context(3, form=form, pathways=form.pathways, mix=MIX,
                                                              selected=form["stream"].value()))


@login_required
def subjects(request):
    profile = get_profile(request.user)
    if not profile.level_id:
        return redirect("accounts:onboarding_level")
    offerings = _offerings_for(profile)
    current = set(Enrollment.objects.filter(user=request.user, offering__in=offerings).values_list("offering_id", flat=True))
    form = SubjectsForm(request.POST if request.method == "POST" else None, offerings=offerings)
    if request.method == "POST" and form.is_valid():
        chosen = {o.pk for o in form.cleaned_data["offerings"]}
        with transaction.atomic():
            Enrollment.objects.filter(user=request.user, offering__in=offerings).exclude(offering_id__in=chosen).delete()
            Enrollment.objects.bulk_create(
                [Enrollment(user=request.user, offering_id=pk) for pk in chosen - current], ignore_conflicts=True
            )
            if profile.onboarded_at is None:
                profile.onboarded_at = timezone.now()
                profile.save(update_fields=["onboarded_at", "updated_at"])
        request.session.pop(STREAM_DONE_KEY, None)
        return redirect("accounts:onboarding_done")
    if form.is_bound:
        selected = {str(v) for v in request.POST.getlist("offerings")}
    else:
        # First visit: tick a starter set (core subjects first) so most students just press Continue;
        # the rest stay one tap away. Students who already chose keep their own selection.
        selected = {str(pk) for pk in (current or _default_selection(offerings))}
    return render(request, "onboarding/subjects.html",
                  _context(4, form=form, offerings=offerings, selected=selected, minimum=form.minimum,
                           coming_soon=_coming_soon(profile)))


@login_required
def done(request):
    profile = get_profile(request.user)
    if not profile.is_onboarded:
        return redirect("accounts:onboarding")
    enrollments = list(
        Enrollment.objects.filter(user=request.user, offering__level=profile.level).select_related("offering__subject")
    )
    # Start in each subject's main course (an offering can have more than one, e.g. a retired demo course).
    main_courses = [services.primary_course(list(e.offering.courses.all())) for e in enrollments]
    first_lesson = (
        Lesson.objects.published()
        .filter(topic__module__course__in=[c for c in main_courses if c])
        .select_related("topic__module__course__offering__subject")
        .order_by("topic__module__course__offering__subject__order", "topic__module__order", "topic__order", "order")
        .first()
    )
    return render(request, "onboarding/done.html",
                  _context(5, profile=profile, enrollments=enrollments, first_lesson=first_lesson))
