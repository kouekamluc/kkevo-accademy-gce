import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.academics.models import AcademicLevel, AcademicPathway
from apps.accounts.models import StudentProfile

pytestmark = pytest.mark.django_db
User = get_user_model()
PASSWORD = "Learn-GCE-2026!"


@pytest.fixture
def student(db):
    return User.objects.create_user(email="ama@example.com", password=PASSWORD, first_name="Ama", last_name="Tabi")


@pytest.fixture
def onboarded(student, form5, science):
    profile = student.profile
    profile.level, profile.pathway = form5, science
    from django.utils import timezone

    profile.onboarded_at = timezone.now()
    profile.save()
    return student


# ---------- registration ----------

def register(client, **overrides):
    data = {
        "first_name": "Alex",
        "last_name": "Nfor",
        "email": "Alex@Example.com",
        "password1": PASSWORD,
        "password2": PASSWORD,
        **overrides,
    }
    return client.post(reverse("accounts:register"), data)


def test_registration_creates_user_profile_logs_in_and_starts_onboarding(client):
    response = register(client)
    assert response.status_code == 302
    assert response.url == reverse("accounts:onboarding")
    user = User.objects.get(email="alex@example.com")
    assert user.check_password(PASSWORD) and user.password.startswith("pbkdf2_")
    assert not user.is_staff
    assert StudentProfile.objects.filter(user=user, onboarded_at__isnull=True).exists()
    assert client.session["_auth_user_id"] == str(user.pk)


@pytest.mark.parametrize(
    "overrides, field",
    [
        ({"password2": "different-pass-1"}, "password2"),
        ({"password1": "12345678", "password2": "12345678"}, "password2"),
        ({"email": "not-an-email"}, "email"),
        ({"first_name": ""}, "first_name"),
    ],
)
def test_registration_validation(client, overrides, field):
    response = register(client, **overrides)
    assert response.status_code == 200
    assert field in response.context["form"].errors
    assert not User.objects.exists()


def test_registration_rejects_duplicate_email_case_insensitively(client, student):
    response = register(client, email="AMA@example.com")
    assert "email" in response.context["form"].errors
    assert User.objects.count() == 1


def test_registration_page_redirects_signed_in_user(client, onboarded):
    client.force_login(onboarded)
    assert client.get(reverse("accounts:register")).status_code == 302


# ---------- login / logout ----------

def test_login_with_email_any_case_redirects_to_dashboard(client, onboarded):
    response = client.post(reverse("accounts:login"), {"username": "AMA@example.com", "password": PASSWORD})
    assert response.status_code == 302
    assert response.url == reverse("dashboard:home")


def test_login_wrong_password_shows_error(client, student):
    response = client.post(reverse("accounts:login"), {"username": student.email, "password": "wrong"})
    assert response.status_code == 200
    assert "don’t match" in response.content.decode()


def test_login_ignores_external_next(client, onboarded):
    response = client.post(
        reverse("accounts:login"), {"username": onboarded.email, "password": PASSWORD, "next": "https://evil.example/"}
    )
    assert response.url == reverse("dashboard:home")


def test_logout_requires_post(client, onboarded):
    client.force_login(onboarded)
    assert client.get(reverse("accounts:logout")).status_code == 405
    response = client.post(reverse("accounts:logout"))
    assert response.url == reverse("core:landing")
    assert "_auth_user_id" not in client.session


# ---------- onboarding ----------

def test_dashboard_requires_login(client):
    response = client.get(reverse("dashboard:home"))
    assert response.status_code == 302 and reverse("accounts:login") in response.url


def test_dashboard_redirects_to_onboarding_until_class_chosen(client, student):
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    assert response.status_code == 302
    assert response.url.startswith(reverse("accounts:onboarding"))


def test_onboarding_lists_levels_and_pathways(client, student):
    client.force_login(student)
    html = client.get(reverse("accounts:onboarding")).content.decode()
    for name in ("Form 5", "Lower Sixth", "Upper Sixth", "Arts", "Science"):
        assert name in html


def test_onboarding_saves_selection_and_opens_dashboard(client, student):
    client.force_login(student)
    level = AcademicLevel.objects.get(code="U6")
    pathway = AcademicPathway.objects.get(slug="arts")
    response = client.post(reverse("accounts:onboarding"), {"level": level.pk, "pathway": pathway.pk})
    assert response.url == reverse("dashboard:home")
    student.profile.refresh_from_db()
    assert student.profile.is_onboarded
    assert student.profile.class_label == "Upper Sixth · Arts"
    html = client.get(reverse("dashboard:home")).content.decode()
    assert "Upper Sixth · Arts" in html


def test_onboarding_requires_both_choices(client, student):
    client.force_login(student)
    response = client.post(reverse("accounts:onboarding"), {})
    assert response.status_code == 200
    assert set(response.context["form"].errors) == {"level", "pathway"}


def test_onboarding_rejects_inactive_level(client, student):
    level = AcademicLevel.objects.get(code="L6")
    level.is_active = False
    level.save()
    client.force_login(student)
    response = client.post(
        reverse("accounts:onboarding"), {"level": level.pk, "pathway": AcademicPathway.objects.first().pk}
    )
    assert "level" in response.context["form"].errors


def test_onboarding_returns_to_safe_next(client, student, form5, science):
    client.force_login(student)
    response = client.post(
        reverse("accounts:onboarding") + "?next=/accounts/profile/", {"level": form5.pk, "pathway": science.pk}
    )
    assert response.url == "/accounts/profile/"


# ---------- profile ----------

def test_profile_requires_login(client):
    assert client.get(reverse("accounts:profile")).status_code == 302


def test_profile_updates_details(client, onboarded):
    client.force_login(onboarded)
    response = client.post(
        reverse("accounts:profile"),
        {"section": "details", "details-first_name": "Amara", "details-last_name": "Tabi", "details-email": "New@Example.com"},
    )
    assert response.status_code == 302
    onboarded.refresh_from_db()
    assert onboarded.first_name == "Amara" and onboarded.email == "new@example.com"


def test_profile_rejects_email_used_by_someone_else(client, onboarded):
    User.objects.create_user(email="taken@example.com", password=PASSWORD)
    client.force_login(onboarded)
    response = client.post(
        reverse("accounts:profile"),
        {"section": "details", "details-first_name": "A", "details-last_name": "T", "details-email": "taken@example.com"},
    )
    assert response.status_code == 200
    assert "email" in response.context["details_form"].errors


def test_profile_updates_study_settings(client, onboarded):
    client.force_login(onboarded)
    l6 = AcademicLevel.objects.get(code="L6")
    arts = AcademicPathway.objects.get(slug="arts")
    client.post(
        reverse("accounts:profile"),
        {"section": "study", "study-level": l6.pk, "study-pathway": arts.pk, "study-low_data_mode": "on"},
    )
    profile = StudentProfile.objects.get(user=onboarded)
    assert (profile.level, profile.pathway, profile.low_data_mode) == (l6, arts, True)


def test_password_change_keeps_session(client, onboarded):
    client.force_login(onboarded)
    response = client.post(
        reverse("accounts:password_change"),
        {"old_password": PASSWORD, "new_password1": "Another-Pass-77", "new_password2": "Another-Pass-77"},
    )
    assert response.url == reverse("accounts:profile")
    onboarded.refresh_from_db()
    assert onboarded.check_password("Another-Pass-77")
    assert client.get(reverse("accounts:profile")).status_code == 200


def test_low_data_toggle_with_htmx_returns_partial(client, onboarded):
    client.force_login(onboarded)
    response = client.post(reverse("accounts:toggle_low_data"), HTTP_HX_REQUEST="true")
    assert response.status_code == 200
    assert 'aria-checked="true"' in response.content.decode()
    assert StudentProfile.objects.get(user=onboarded).low_data_mode is True
    assert client.get(reverse("accounts:toggle_low_data")).status_code == 405


def test_csrf_enforced_on_login():
    from django.test import Client

    strict = Client(enforce_csrf_checks=True)
    assert strict.post(reverse("accounts:login"), {"username": "a@b.c", "password": "x"}).status_code == 403
