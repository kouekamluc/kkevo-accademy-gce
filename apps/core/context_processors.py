from django.urls import NoReverseMatch, reverse
from django.utils.functional import SimpleLazyObject

from apps.academics.models import AcademicLevel

# Sidebar items from the dashboard mockup (02). Items whose route is not installed are skipped.
SIDEBAR = [
    ("dashboard", "Today", "home", "dashboard:home"),
    # One page for everything about the student's own subjects: where they left off, every course, adding more.
    # (Its older pages, My Subjects and Continue, keep working and light up the same item.)
    ("courses", "My Courses", "book", "courses:continue", ("subjects", "continue")),
    ("explore", "Explore Subjects", "compass", "courses:catalog"),
    ("practice", "Practice", "target", "practice:index"),
    ("planner", "Study Planner", "calendar", "learning:planner"),
    ("progress", "My Progress", "progress", "learning:progress"),
    ("report", "Report Card", "file", "learning:report_card"),
    ("saved", "Saved Lessons", "bookmark", "learning:saved"),
    ("settings", "Settings", "settings", "accounts:profile"),
]
# Phone bottom bar: Home · Subjects · Learn · Progress · Profile. Extra keys also light the item up.
BOTTOM_BAR = [
    ("dashboard", "Today", "home", "dashboard:home", ()),
    ("courses", "Learn", "book", "courses:continue", ("subjects", "continue", "explore", "saved")),
    ("practice", "Practice", "target", "practice:index", ()),
    ("progress", "Progress", "progress", "learning:progress", ("planner", "report")),
    ("settings", "Me", "user", "accounts:profile", ()),
]


# Hidden until the student has started a lesson: they have nothing to show yet, so they only add clutter.
HIDDEN_UNTIL_STARTED = {"progress", "saved", "report"}


def _resolve(items, started=True):
    out = []
    for item in items:
        if not started and item[0] in HIDDEN_UNTIL_STARTED:
            continue
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

    cache = {}

    def has_started():
        """True once the student has opened a lesson (or if the visitor is not signed in)."""
        if "started" not in cache:
            user = getattr(request, "user", None)
            if user is None or not user.is_authenticated:
                cache["started"] = True
            else:
                from apps.learning.models import LessonProgress

                cache["started"] = LessonProgress.objects.filter(user=user).exists()
        return cache["started"]

    return {
        "nav_levels": SimpleLazyObject(lambda: list(AcademicLevel.objects.filter(is_active=True))),
        "current_profile": SimpleLazyObject(current_profile),
        "sidebar_items": SimpleLazyObject(lambda: _resolve(SIDEBAR, has_started())),
        "staff_nav": SimpleLazyObject(lambda: _staff_nav(request)),
        "bottom_items": SimpleLazyObject(lambda: _resolve(BOTTOM_BAR, has_started())),
    }


def _staff_nav(request):
    user = getattr(request, "user", None)
    if user is None or not user.is_authenticated or not user.is_staff:
        return []
    from .staff_nav import staff_navigation

    return staff_navigation(request)


def site(request):
    """Values every page can use: the public contact email and the page's canonical address."""
    from django.conf import settings

    return {"contact_email": settings.CONTACT_EMAIL,
            "canonical_url": request.build_absolute_uri(request.path)}
