from django.utils.functional import SimpleLazyObject

from apps.academics.models import AcademicLevel


def navigation(request):
    """Shared layout data. Lazy, so pages that don't use it run no queries."""

    def current_profile():
        user = getattr(request, "user", None)
        if user is None or not user.is_authenticated:
            return None
        from apps.accounts.utils import get_profile

        return get_profile(user)

    return {
        "nav_levels": SimpleLazyObject(lambda: list(AcademicLevel.objects.filter(is_active=True))),
        "current_profile": SimpleLazyObject(current_profile),
    }
