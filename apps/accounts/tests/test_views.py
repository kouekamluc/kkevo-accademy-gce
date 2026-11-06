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
    data = {"full_name": "  Alex   Nfor ", "email": "Alex@Example.com", "password": PASSWORD, **overrides}
    return client.post(reverse("accounts:register"), data)


def test_registration_creates_user_profile_logs_in_and_starts_onboarding(client):
    response = register(client)
    assert response.status_code == 302
    assert response.url == reverse("accounts:onboarding_level")
    user = User.objects.get(email="alex@example.com")
    assert (user.first_name, user.last_name) == ("Alex", "Nfor")
    assert user.check_password(PASSWORD) and user.password.startswith("pbkdf2_")
    assert not user.is_staff
    assert StudentProfile.objects.filter(user=user, onboarded_at__isnull=True).exists()
    assert client.session["_auth_user_id"] == str(user.pk)


@pytest.mark.parametrize(
    "overrides, field",
    [
        ({"password": "short"}, "password"),
        ({"password": "12345678"}, "password"),
        ({"password": "alex@example.com"}, "password"),
        ({"email": "not-an-email"}, "email"),
        ({"full_name": "   "}, "full_name"),
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


def test_dashboard_redirects_to_onboarding_until_finished(client, student):
    client.force_login(student)
    response = client.get(reverse("dashboard:home"))
    assert response.status_code == 302
    assert response.url.startswith(reverse("accounts:onboarding"))
    assert client.get(reverse("accounts:onboarding")).url == reverse("accounts:onboarding_level")


def test_level_step_lists_levels_and_saves(client, student):
    client.force_login(student)
    html = client.get(reverse("accounts:onboarding_level")).content.decode()
    for name in ("Form 5", "Lower Sixth", "Upper Sixth", "Step 2 of 5"):
        assert name in html
    level = AcademicLevel.objects.get(code="U6")
    response = client.post(reverse("accounts:onboarding_level"), {"level": level.pk})
    assert response.url == reverse("accounts:onboarding_stream")
    assert StudentProfile.objects.get(user=student).level == level


def test_level_step_requires_choice_and_rejects_inactive(client, student):
    client.force_login(student)
    assert "level" in client.post(reverse("accounts:onboarding_level"), {}).context["form"].errors
    level = AcademicLevel.objects.get(code="L6")
    level.is_active = False
    level.save()
    response = client.post(reverse("accounts:onboarding_level"), {"level": level.pk})
    assert "level" in response.context["form"].errors


def test_stream_step_requires_level_first(client, student):
    client.force_login(student)
    assert client.get(reverse("accounts:onboarding_stream")).url == reverse("accounts:onboarding_level")


def test_stream_step_accepts_pathway_or_mix(client, student, form5):
    student.profile.level = form5
    student.profile.save()
    client.force_login(student)
    html = client.get(reverse("accounts:onboarding_stream")).content.decode()
    assert "Arts" in html and "Science" in html and "A mix" in html
    client.post(reverse("accounts:onboarding_stream"), {"stream": "arts"})
    assert StudentProfile.objects.get(user=student).pathway.slug == "arts"
    response = client.post(reverse("accounts:onboarding_stream"), {"stream": "mix"})
    assert response.url == reverse("accounts:onboarding_subjects")
    assert StudentProfile.objects.get(user=student).pathway is None
    assert "stream" in client.post(reverse("accounts:onboarding_stream"), {"stream": "bogus"}).context["form"].errors


@pytest.fixture
def form5_offerings(form5, science):
    from apps.academics.models import Subject, SubjectOffering

    offerings = []
    for i, name in enumerate(["Alpha", "Beta", "Gamma", "Delta"]):
        subject = Subject.objects.create(name=name, slug=name.lower(), icon_text=name[0], order=i)
        offering = SubjectOffering.objects.create(subject=subject, level=form5)
        offering.pathways.add(science)
        offerings.append(offering)
    return offerings


def test_subjects_step_needs_three_then_enrols_and_finishes(client, student, form5, science, form5_offerings):
    from apps.learning.models import Enrollment

    profile = student.profile
    profile.level, profile.pathway = form5, science
    profile.save()
    client.force_login(student)
    html = client.get(reverse("accounts:onboarding_subjects")).content.decode()
    assert "Pick at least 3" in html and "Alpha" in html
    # First visit: every subject of the class and stream is already ticked
    assert client.get(reverse("accounts:onboarding_subjects")).context["selected"] == {str(o.pk) for o in form5_offerings}

    too_few = client.post(reverse("accounts:onboarding_subjects"), {"offerings": [form5_offerings[0].pk]})
    assert "offerings" in too_few.context["form"].errors
    assert not Enrollment.objects.exists()

    chosen = [o.pk for o in form5_offerings[:3]]
    response = client.post(reverse("accounts:onboarding_subjects"), {"offerings": chosen})
    assert response.url == reverse("accounts:onboarding_done")
    assert set(Enrollment.objects.filter(user=student).values_list("offering_id", flat=True)) == set(chosen)
    assert StudentProfile.objects.get(user=student).is_onboarded

    # Going back and changing the selection replaces it
    client.post(reverse("accounts:onboarding_subjects"), {"offerings": [o.pk for o in form5_offerings[1:]]})
    assert set(Enrollment.objects.filter(user=student).values_list("offering_id", flat=True)) == {
        o.pk for o in form5_offerings[1:]
    }

    done = client.get(reverse("accounts:onboarding_done")).content.decode()
    assert "You’re all set, Ama!" in done and "Form 5" in done and "Beta, Gamma, Delta" in done
    assert client.get(reverse("dashboard:home")).status_code == 200


def test_subjects_step_with_no_content_still_lets_student_finish(client, student, form5):
    student.profile.level = form5
    student.profile.save()
    client.force_login(student)
    html = client.get(reverse("accounts:onboarding_subjects")).content.decode()
    assert "No subjects are available" in html
    assert client.post(reverse("accounts:onboarding_subjects"), {}).url == reverse("accounts:onboarding_done")


def test_subjects_cannot_include_other_levels(client, student, form5, form5_offerings):
    from apps.academics.models import AcademicLevel, SubjectOffering

    other = SubjectOffering.objects.create(subject=form5_offerings[0].subject, level=AcademicLevel.objects.get(code="U6"))
    student.profile.level = form5
    student.profile.save()
    client.force_login(student)
    response = client.post(reverse("accounts:onboarding_subjects"), {"offerings": [other.pk]})
    assert "offerings" in response.context["form"].errors


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


def test_profile_study_settings_allow_mix(client, onboarded):
    client.force_login(onboarded)
    l6 = AcademicLevel.objects.get(code="L6")
    client.post(reverse("accounts:profile"), {"section": "study", "study-level": l6.pk, "study-pathway": "", "study-daily_goal_minutes": 45})
    profile = StudentProfile.objects.get(user=onboarded)
    assert profile.pathway is None and profile.class_label == "Lower Sixth · Mixed"


def test_profile_updates_study_settings(client, onboarded):
    client.force_login(onboarded)
    l6 = AcademicLevel.objects.get(code="L6")
    arts = AcademicPathway.objects.get(slug="arts")
    client.post(
        reverse("accounts:profile"),
        {"section": "study", "study-level": l6.pk, "study-pathway": arts.pk, "study-low_data_mode": "on", "study-daily_goal_minutes": 60},
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


# ---------- staff accounts are not students ----------

def test_staff_login_goes_to_studio_and_skips_onboarding(client):
    staff = User.objects.create_user(email="staff.login@example.com", password=PASSWORD, is_staff=True)
    response = client.post(reverse("accounts:login"), {"username": staff.email, "password": PASSWORD})
    assert response.url == reverse("studio:lessons")
    # Student pages that need onboarding send staff to their workspace, not to student setup
    assert client.get(reverse("dashboard:home")).url == reverse("studio:lessons")


def test_staff_login_still_honours_next(client):
    staff = User.objects.create_user(email="staff.next@example.com", password=PASSWORD, is_staff=True)
    response = client.post(reverse("accounts:login") + "?next=/subjects/",
                           {"username": staff.email, "password": PASSWORD, "next": "/subjects/"})
    assert response.url == "/subjects/"


def test_student_login_still_goes_to_dashboard(client, onboarded):
    response = client.post(reverse("accounts:login"), {"username": onboarded.email, "password": PASSWORD})
    assert response.url == reverse("dashboard:home")
