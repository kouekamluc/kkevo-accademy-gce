"""One navigation for the whole staff workspace.

Both the content studio (custom pages) and the Django admin (themed with Unfold) render
their sidebar from STAFF_NAV, so staff move between them without feeling they changed app.
Each item: (title, Material Symbols icon, url name, optional query string, permission).
Items the user has no permission for are hidden.
"""

from django.urls import NoReverseMatch, reverse

STAFF_NAV = [
    ("Workspace", [
        ("Overview", "space_dashboard", "studio:overview", "", "courses.change_lesson"),
        ("Lessons", "description", "studio:lessons", "", "courses.change_lesson"),
        ("Content reviews", "rate_review", "studio:lessons", "status=review", "courses.change_lesson"),
        ("Pending changes", "difference", "studio:lessons", "status=changes", "courses.change_lesson"),
        ("Media library", "photo_library", "studio:media", "", "courses.change_lesson"),
        ("Video library", "video_library", "studio:videos", "", "courses.change_lesson"),
    ]),
    ("Curriculum", [
        ("Academic levels", "school", "admin:academics_academiclevel_changelist", "", "academics.view_academiclevel"),
        ("Pathways", "alt_route", "admin:academics_academicpathway_changelist", "", "academics.view_academicpathway"),
        ("Subjects", "category", "admin:academics_subject_changelist", "", "academics.view_subject"),
        ("Subject offerings", "view_list", "admin:academics_subjectoffering_changelist", "", "academics.view_subjectoffering"),
        ("Courses", "menu_book", "admin:courses_course_changelist", "", "courses.view_course"),
        ("Modules", "stacks", "admin:courses_module_changelist", "", "courses.view_module"),
        ("Topics", "topic", "admin:courses_topic_changelist", "", "courses.view_topic"),
        ("Syllabi", "gavel", "admin:academics_syllabus_changelist", "", "academics.view_syllabus"),
        ("Curriculum references", "format_list_numbered", "admin:academics_curriculumreference_changelist", "",
         "academics.view_curriculumreference"),
    ]),
    ("Practice", [
        ("Practice sets", "quiz", "admin:practice_practiceset_changelist", "", "practice.view_practiceset"),
        ("Questions", "help", "admin:practice_question_changelist", "", "practice.view_question"),
    ]),
    ("Students", [
        ("Users", "group", "admin:accounts_user_changelist", "", "accounts.view_user"),
        ("Student profiles", "badge", "admin:accounts_studentprofile_changelist", "", "accounts.view_studentprofile"),
        ("Enrolments", "how_to_reg", "admin:learning_enrollment_changelist", "", "learning.view_enrollment"),
        ("Lesson progress", "trending_up", "admin:learning_lessonprogress_changelist", "", "learning.view_lessonprogress"),
        ("Practice attempts", "fact_check", "admin:practice_attempt_changelist", "", "practice.view_attempt"),
    ]),
    ("System", [
        ("Staff roles", "admin_panel_settings", "admin:auth_group_changelist", "", "auth.view_group"),
        ("Activity log", "history", "admin:studio_lessonevent_changelist", "", "studio.view_lessonevent"),
    ]),
]


def _resolve(url_name, query):
    try:
        url = reverse(url_name)
    except NoReverseMatch:
        return None
    return f"{url}?{query}" if query else url


def staff_navigation(request):
    """Groups of visible items for this staff user, with the current page marked active."""
    user = request.user
    path = request.path
    query = request.GET.urlencode()
    groups, candidates = [], []
    for title, items in STAFF_NAV:
        visible = []
        for label, icon, url_name, item_query, perm in items:
            if perm and not user.has_perm(perm):
                continue
            url = _resolve(url_name, item_query)
            if url is None:
                continue
            item = {"title": label, "icon": icon, "url": url, "active": False, "badge": None}
            base = url.split("?")[0]
            if path.startswith(base) and (not item_query or item_query in query):
                # Longest URL wins; an item with a matching query beats the same URL without one
                candidates.append((len(base) + (1000 if item_query else 0), item))
            visible.append(item)
        if visible:
            groups.append({"title": title, "items": visible})
    if candidates:
        max(candidates, key=lambda c: c[0])[1]["active"] = True
    _add_badges(groups)
    return groups


def _add_badges(groups):
    from apps.courses.models import Lesson

    review = Lesson.objects.filter(status="review").count()
    for group in groups:
        for item in group["items"]:
            if item["title"] == "Content reviews" and review:
                item["badge"] = review
