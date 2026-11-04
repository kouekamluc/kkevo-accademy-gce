import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import RequestFactory
from django.urls import reverse

from apps.core.staff_nav import STAFF_NAV, staff_navigation

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def superuser(db):
    return User.objects.create_superuser(email="root@example.com", password="pw-Strong-123")


def nav_for(user, path, query=""):
    request = RequestFactory().get(path + (f"?{query}" if query else ""))
    request.user = user
    return staff_navigation(request)


def active_titles(groups):
    return [i["title"] for g in groups for i in g["items"] if i["active"]]


def test_every_staff_nav_link_resolves_for_superuser(superuser):
    groups = nav_for(superuser, "/studio/")
    assert sum(len(items) for _, items in STAFF_NAV) == sum(len(g["items"]) for g in groups)


def test_exactly_one_active_item(superuser, lesson):
    assert active_titles(nav_for(superuser, "/studio/overview/")) == ["Overview"]
    assert active_titles(nav_for(superuser, "/studio/")) == ["Lessons"]
    assert active_titles(nav_for(superuser, "/studio/", "status=review")) == ["Content reviews"]
    assert active_titles(nav_for(superuser, "/studio/lessons/1/")) == ["Lessons"]
    assert active_titles(nav_for(superuser, reverse("admin:courses_course_changelist"))) == ["Courses"]


def test_items_follow_permissions():
    editor = User.objects.create_user(email="ed@example.com", password="pw-Strong-123", is_staff=True)
    editor.user_permissions.add(Permission.objects.get(codename="change_lesson"))
    titles = [i["title"] for g in nav_for(editor, "/studio/") for i in g["items"]]
    assert "Lessons" in titles and "Users" not in titles and "Staff roles" not in titles


def test_admin_and_studio_render_the_same_sidebar(client, superuser):
    client.force_login(superuser)
    admin_html = client.get(reverse("admin:courses_course_changelist")).content.decode()
    studio_html = client.get(reverse("studio:overview")).content.decode()
    for html in (admin_html, studio_html):
        assert 'class="staff-sidebar"' in html and "Staff workspace" in html and "css/staff.css" in html


def test_admin_home_and_login_point_to_the_app(client, superuser):
    assert client.get("/admin/").url == reverse("studio:overview")
    response = client.get("/admin/login/?next=/admin/courses/course/")
    assert response.url == reverse("accounts:login") + "?next=%2Fadmin%2Fcourses%2Fcourse%2F"
    assert "evil" not in client.get("/admin/login/?next=https://evil.example/").url
    client.force_login(superuser)
    assert client.get("/admin/login/?next=/admin/courses/course/").url == "/admin/courses/course/"


def test_student_gets_403_not_a_login_loop(client):
    student = User.objects.create_user(email="st@example.com", password="pw-Strong-123")
    client.force_login(student)
    assert client.get("/admin/login/?next=/admin/").status_code == 403


def test_lesson_admin_has_edit_in_studio(client, superuser, lesson):
    client.force_login(superuser)
    html = client.get(reverse("admin:courses_lesson_change", args=[lesson.pk])).content.decode()
    assert "Edit in studio" in html
    response = client.get(reverse("admin:courses_lesson_edit_in_studio", args=[lesson.pk]))
    assert response.url == reverse("studio:edit", args=[lesson.pk])
