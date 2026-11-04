from django.db.models import Count, Prefetch, Q
from django.shortcuts import render

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


def planned(request, page, **kwargs):
    """Placeholder for pages delivered in a later milestone."""
    return render(request, "core/planned.html", {"page": page})
