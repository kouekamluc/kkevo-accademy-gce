from django.db.models import Count, Prefetch, Q
from datetime import date

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from apps.academics.models import AcademicLevel, AcademicPathway, Subject, SubjectOffering


def landing(request):
    levels = AcademicLevel.objects.filter(is_active=True).annotate(
        subject_count=Count(
            "offerings",
            filter=Q(offerings__is_active=True, offerings__subject__is_active=True),
            distinct=True,
        )
    )
    featured_subjects = Subject.objects.filter(is_active=True, is_featured=True).prefetch_related(
        Prefetch(
            "offerings",
            queryset=SubjectOffering.objects.active().select_related("level").prefetch_related("pathways"),
            to_attr="active_offerings",
        )
    )[:8]
    pathways = AcademicPathway.objects.filter(is_active=True)
    return render(
        request,
        "core/landing.html",
        {
            "levels": levels,
            "featured_subjects": featured_subjects,
            "pathway_label": " & ".join(p.name for p in pathways),
        },
    )


def _public_stats():
    """Real totals for the public pages: published subjects, lessons and practice questions."""
    from apps.courses.models import Lesson
    from apps.practice.models import Question

    published = {"topic__module__course__status": "published"}
    return {
        "lessons": Lesson.objects.published().filter(**published).count(),
        "questions": Question.objects.filter(
            practice_set__status="published", practice_set__topic__module__course__status="published").count(),
        "subjects": SubjectOffering.objects.active().filter(subject__is_active=True).count(),
    }


def _public_levels():
    return AcademicLevel.objects.filter(is_active=True).annotate(
        subject_count=Count("offerings", filter=Q(offerings__is_active=True, offerings__subject__is_active=True),
                            distinct=True))


def how_it_works(request):
    """The student journey from sign-up to exam day, with a sign-up prompt."""
    return render(request, "core/how_it_works.html", {"levels": _public_levels(), "stats": _public_stats()})


def about(request):
    """Who KKEVO Academy is for and what it is (and is not)."""
    return render(request, "core/about.html", {"levels": _public_levels(), "stats": _public_stats()})


def planned(request, page, **kwargs):
    """Placeholder for pages delivered in a later milestone."""
    return render(request, "core/planned.html", {"page": page})


def staff_login(request):
    """The admin's login page redirects to the app's single login page (rate-limited, styled)."""
    from urllib.parse import urlencode

    from django.core.exceptions import PermissionDenied
    from django.shortcuts import redirect
    from django.urls import reverse

    next_url = request.GET.get("next") or reverse("studio:overview")
    if not next_url.startswith("/") or next_url.startswith("//"):
        next_url = reverse("studio:overview")
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect(next_url)
        raise PermissionDenied("This area is for staff only.")
    return redirect(f"{reverse('accounts:login')}?{urlencode({'next': next_url})}")


# --------------------------------------------------------------------------- legal pages and crawler files
LEGAL_UPDATED = date(2026, 11, 12)  # bump when the privacy policy or terms change in a way that matters


def privacy(request):
    return render(request, "core/privacy.html", {"legal_updated": LEGAL_UPDATED})


def terms(request):
    return render(request, "core/terms.html", {"legal_updated": LEGAL_UPDATED})


def contact(request):
    return render(request, "core/contact.html", {})


# Pages that belong to a logged-in student, or that nobody needs to find through a search engine.
ROBOTS_DISALLOW = ["/admin/", "/studio/", "/accounts/", "/dashboard/", "/learn/", "/practice/", "/my-subjects/",
                   "/continue/", "/offline/", "/courses/*/lessons/"]


@require_GET
def robots_txt(request):
    lines = ["User-agent: *", *[f"Disallow: {path}" for path in ROBOTS_DISALLOW], "",
             f"Sitemap: {request.build_absolute_uri(reverse('sitemap'))}", ""]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")
