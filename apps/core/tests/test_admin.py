import pytest
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse

pytestmark = pytest.mark.django_db

User = get_user_model()

CONTENT_MODELS = [
    "academics.academiclevel",
    "academics.academicpathway",
    "academics.subject",
    "academics.subjectoffering",
    "academics.syllabus",
    "academics.curriculumreference",
    "courses.course",
    "courses.module",
    "courses.topic",
    "courses.lesson",
]


def test_all_content_models_registered():
    registered = {f"{m._meta.app_label}.{m._meta.model_name}" for m in admin.site._registry}
    assert set(CONTENT_MODELS) <= registered


def test_anonymous_redirected_to_admin_login(client):
    response = client.get(reverse("admin:courses_course_changelist"))
    assert response.status_code == 302
    assert reverse("admin:login") in response.url


def test_student_cannot_access_admin(client):
    student = User.objects.create_user(email="student@example.com", password="pw-123456!")
    client.force_login(student)
    response = client.get(reverse("admin:courses_course_changelist"))
    assert response.status_code == 302


def test_staff_without_permission_is_forbidden(client):
    staff = User.objects.create_user(email="staff@example.com", password="pw-123456!", is_staff=True)
    client.force_login(staff)
    assert client.get(reverse("admin:courses_course_changelist")).status_code == 403


@pytest.mark.parametrize("model", CONTENT_MODELS)
def test_superuser_can_open_changelist_and_add_form(admin_client, model, lesson):
    app_label, model_name = model.split(".")
    assert admin_client.get(reverse(f"admin:{app_label}_{model_name}_changelist")).status_code == 200
    assert admin_client.get(reverse(f"admin:{app_label}_{model_name}_changelist"), {"q": "a"}).status_code == 200
    assert admin_client.get(reverse(f"admin:{app_label}_{model_name}_add")).status_code == 200


def test_admin_can_create_subject_through_form(admin_client, form5, science):
    response = admin_client.post(
        reverse("admin:academics_subject_add"),
        {
            "name": "Created Subject",
            "slug": "created-subject",
            "summary": "",
            "icon_text": "Cs",
            "icon": "",
            "accent": "blue",
            "category": "sciences",
            "order": 0,
            "is_active": "on",
            "offerings-TOTAL_FORMS": "1",
            "offerings-INITIAL_FORMS": "0",
            "offerings-MIN_NUM_FORMS": "0",
            "offerings-MAX_NUM_FORMS": "1000",
            "offerings-0-level": form5.pk,
            "offerings-0-pathways": [science.pk],
            "offerings-0-is_active": "on",
        },
    )
    assert response.status_code == 302, response.content.decode()[:2000]
    from apps.academics.models import Subject

    subject = Subject.objects.get(slug="created-subject")
    assert subject.offerings.get().pathways.get() == science
