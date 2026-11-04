from django.urls import NoReverseMatch, reverse
from django.utils.functional import SimpleLazyObject

from apps.academics.models import AcademicLevel

# Sidebar items from the dashboard mockup (02). Items whose route is not installed are skipped.
SIDEBAR = [
    ("dashboard", "Dashboard", "home", "dashboard:home"),
    ("subjects", "My Subjects", "book", "courses:my_subjects"),
    ("explore", "Explore Courses", "compass", "courses:catalog"),
    ("continue", "Continue Learning", "play", "courses:continue"),
    ("practice", "Practice", "target", "practice:index"),
    ("planner", "Study Planner", "calendar", "learning:planner"),
    ("progress", "My Progress", "progress", "learning:progress"),
    ("saved", "Saved Lessons", "bookmark", "learning:saved"),
    ("settings", "Settings", "settings", "accounts:profile"),
]
# Phone bottom bar: Home · Subjects · Learn · Progress · Profile. Extra keys also light the item up.
BOTTOM_BAR = [
    ("dashboard", "Home", "home", "dashboard:home", ()),
    ("subjects", "Subjects", "book", "courses:my_subjects", ("explore",)),
    ("continue", "Learn", "play", "courses:continue", ("practice", "saved")),
    ("progress", "Progress", "progress", "learning:progress", ("planner",)),
    ("settings", "Profile", "user", "accounts:profile", ()),
]


def _resolve(items):
    out = []
    for item in items:
        try:
            url = reverse(item[3])
        except NoReverseMatch:
            continue
        out.append({"key": item[0], "label": item[1], "icon": item[2], "url": url,
                    "also": item[4] if len(item) > 4 else ()})
    return out


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
        "sidebar_items": SimpleLazyObject(lambda: _resolve(SIDEBAR)),
        "staff_nav": SimpleLazyObject(lambda: _staff_nav(request)),
        "bottom_items": SimpleLazyObject(lambda: _resolve(BOTTOM_BAR)),
    }


def _staff_nav(request):
    user = getattr(request, "user", None)
    if user is None or not user.is_authenticated or not user.is_staff:
        return []
    from .staff_nav import staff_navigation

    return staff_navigation(request)

