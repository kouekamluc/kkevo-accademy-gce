from django.utils.functional import SimpleLazyObject

from apps.academics.models import AcademicLevel


def navigation(request):
    """Active academic levels for header/footer links (queried only if a template uses them)."""
    return {"nav_levels": SimpleLazyObject(lambda: list(AcademicLevel.objects.filter(is_active=True)))}
