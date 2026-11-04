"""Password reset, login rate limiting, "keep me signed in", data download and account deletion."""

import json
import re

import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.cache import cache
from django.test import override_settings
from django.urls import reverse
from django.utils import timezone

from apps.accounts.privacy import export_user_data
from apps.accounts.ratelimit import RateLimit, client_ip

pytestmark = pytest.mark.django_db
User = get_user_model()
PASSWORD = "Learn-GCE-2026!"
NEW_PASSWORD = "Fresh-Start-2026?"


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="ama@example.com", password=PASSWORD, first_name="Ama", last_name="Tabi")
    profile = user.profile
    profile.level, profile.pathway, profile.onboarded_at = form5, science, timezone.now()
    profile.save()
    return user


def login(client, email="ama@example.com", password=PASSWORD, **extra):
    return client.post(reverse("accounts:login"), {"username": email, "password": password, **extra})


# ---------- login page ----------

def test_login_page_has_reset_link_remember_box_and_show_password(client):
    html = client.get(reverse("accounts:login")).content.decode()
    assert reverse("accounts:password_reset") in html and "Forgot password?" in html
    assert re.search(r'name="remember_me"[^>]*checked', html)  # ticked by default
    assert "Show" in html and 'autocomplete="current-password"' in html


# ---------- keep me signed in ----------

def test_remember_me_keeps_persistent_session(client, student):
    login(client, remember_me="on")
    assert client.session.get_expire_at_browser_close() is False
    assert client.session.get_expiry_age() == 60 * 60 * 24 * 30
    assert client.cookies["sessionid"]["expires"]


def test_unticked_remember_me_ends_session_at_browser_close(client, student):
    response = login(client)  # an unticked checkbox is simply not sent
    assert response.status_code == 302
    assert client.session.get_expire_at_browser_close() is True
    assert client.cookies["sessionid"]["expires"] == ""  # browser-session cookie


# ---------- brute-force protection ----------

@override_settings(LOGIN_RATE_LIMIT_ATTEMPTS=3)
def test_login_locks_after_repeated_failures_even_with_right_password(client, student):
    assert "attempt(s) left" in login(client, password="wrong").content.decode()
    login(client, password="wrong")
    third = login(client, password="wrong")
    assert third.status_code == 429
    html = third.content.decode()
    assert "Too many wrong attempts" in html and reverse("accounts:password_reset") in html

    blocked = login(client)  # the right password is refused while locked
    assert blocked.status_code == 429
    assert "_auth_user_id" not in client.session


@override_settings(LOGIN_RATE_LIMIT_ATTEMPTS=3)
def test_lock_is_per_email_and_per_ip(client, student):
    User.objects.create_user(email="ben@example.com", password=PASSWORD)
    for _ in range(3):
        login(client, password="wrong")
    assert login(client).status_code == 429
    # Another account from the same IP is not affected
    assert login(client, email="ben@example.com").status_code == 302
    client.logout()
    # The same account from another IP is not affected
    response = client.post(
        reverse("accounts:login"), {"username": "ama@example.com", "password": PASSWORD}, REMOTE_ADDR="10.0.0.9"
    )
    assert response.status_code == 302


@override_settings(LOGIN_RATE_LIMIT_ATTEMPTS=3)
def test_email_case_does_not_bypass_lock(client, student):
    for email in ("ama@example.com", "AMA@example.com", " Ama@Example.com "):
        login(client, email=email, password="wrong")
    assert login(client).status_code == 429


@override_settings(LOGIN_RATE_LIMIT_ATTEMPTS=3)
def test_successful_login_resets_failure_count(client, student):
    login(client, password="wrong")
    login(client, password="wrong")
    assert login(client).status_code == 302
    client.logout()
    login(client, password="wrong")
    login(client, password="wrong")
    assert login(client).status_code == 302


def test_rate_limit_reports_minutes_left_and_sets_cache_timeout(monkeypatch):
    import apps.accounts.ratelimit as rl

    now = [1000.0]
    monkeypatch.setattr(rl.time, "time", lambda: now[0])
    limiter = RateLimit("test", "x", limit=2, window=600)
    limiter.hit()
    now[0] += 240
    limiter.hit()
    assert limiter.is_blocked() and limiter.retry_after_minutes() == 6
    cache.delete(limiter.key)  # what the cache does when the window's timeout passes
    assert not limiter.is_blocked() and limiter.remaining == 2


def test_client_ip_ignores_forwarded_header_unless_proxies_trusted(rf, settings):
    request = rf.get("/", REMOTE_ADDR="10.0.0.1", HTTP_X_FORWARDED_FOR="6.6.6.6, 41.202.1.2")
    settings.TRUSTED_PROXY_COUNT = 0
    assert client_ip(request) == "10.0.0.1"
    settings.TRUSTED_PROXY_COUNT = 1
    assert client_ip(request) == "41.202.1.2"


def test_rate_limit_keys_do_not_store_emails():
    limiter = RateLimit("login", "ama@example.com", "1.2.3.4", limit=1, window=60)
    assert "ama" not in limiter.key and "1.2.3.4" not in limiter.key


# ---------- password reset ----------

def request_reset(client, email="ama@example.com"):
    return client.post(reverse("accounts:password_reset"), {"email": email})


def reset_link():
    return re.search(r"https?://[^/\s]+(/accounts/reset/\S+/)", mail.outbox[-1].body).group(1)


def follow_reset_link(client):
    page = client.get(reset_link(), follow=True)  # Django swaps the token for a session marker
    return page, page.redirect_chain[-1][0]


def test_reset_request_sends_email_with_link(client, student):
    response = request_reset(client, "AMA@Example.com")
    assert response.url == reverse("accounts:password_reset_done")
    assert len(mail.outbox) == 1
    message = mail.outbox[0]
    assert message.to == ["ama@example.com"]
    assert message.subject == "Reset your GCE Learning Academy password"
    assert "Hello Ama" in message.body and "/accounts/reset/" in message.body
    assert "Spam" in client.get(response.url).content.decode()


def test_reset_request_for_unknown_email_looks_the_same(client, student):
    response = request_reset(client, "nobody@example.com")
    assert response.url == reverse("accounts:password_reset_done")
    assert mail.outbox == []


def test_reset_page_is_styled_with_auth_layout(client):
    html = client.get(reverse("accounts:password_reset")).content.decode()
    assert "Forgot your password?" in html and "GCE Learning Academy" in html and 'class="form-input' in html


def test_reset_link_sets_new_password_and_logs_in(client, student):
    request_reset(client)
    link = reset_link()
    page, set_url = follow_reset_link(client)
    assert page.context["validlink"] is True

    weak = client.post(set_url, {"new_password1": "12345678", "new_password2": "12345678"})
    assert weak.context["form"].errors

    done = client.post(set_url, {"new_password1": NEW_PASSWORD, "new_password2": NEW_PASSWORD})
    assert done.url == reverse("accounts:password_reset_complete")
    student.refresh_from_db()
    assert student.check_password(NEW_PASSWORD)
    assert client.session["_auth_user_id"] == str(student.pk)
    assert "Continue learning" in client.get(done.url).content.decode()

    client.logout()
    assert client.get(link, follow=True).context["validlink"] is False  # single use


def test_invalid_reset_link_shows_expired_page(client, student):
    html = client.get(reverse("accounts:password_reset_confirm", args=["MQ", "bad-token"])).content.decode()
    assert "This link has expired" in html


@override_settings(LOGIN_RATE_LIMIT_ATTEMPTS=2)
def test_password_reset_lifts_login_lock(client, student):
    login(client, password="wrong")
    login(client, password="wrong")
    assert login(client).status_code == 429
    request_reset(client)
    _, set_url = follow_reset_link(client)
    client.post(set_url, {"new_password1": NEW_PASSWORD, "new_password2": NEW_PASSWORD})
    client.logout()
    assert login(client, password=NEW_PASSWORD).status_code == 302


@override_settings(PASSWORD_RESET_RATE_LIMIT=2)
def test_reset_requests_are_rate_limited_per_ip(client, student):
    request_reset(client)
    request_reset(client, "other@example.com")
    blocked = request_reset(client)
    assert blocked.status_code == 429
    assert "several reset links" in blocked.content.decode()
    assert len(mail.outbox) == 1


# ---------- data download ----------

def test_data_export_downloads_own_data_only(client, student, offering, lesson):
    from apps.learning.models import Enrollment, LessonNote, LessonProgress

    other = User.objects.create_user(email="ben@example.com", password=PASSWORD)
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=lesson, percent=40)
    LessonNote.objects.create(user=student, lesson=lesson, body="Remember the formula")
    LessonNote.objects.create(user=other, lesson=lesson, body="Ben's private note")
    client.force_login(student)

    response = client.get(reverse("accounts:data_export"))
    assert response.status_code == 200
    assert response["Content-Disposition"].startswith("attachment;")
    assert response["Cache-Control"] == "no-store"
    data = json.loads(response.content)
    assert data["account"]["email"] == "ama@example.com"
    assert "password" not in json.dumps(data) and "pbkdf2" not in response.content.decode()
    assert data["study_profile"]["level"]["name"] == "Form 5"
    assert data["enrollments"][0]["offering"]["id"] == offering.pk
    assert data["lesson_progress"][0]["percent"] == 40
    assert [n["body"] for n in data["lesson_notes"]] == ["Remember the formula"]


def test_data_export_includes_nested_practice_answers(student, lesson):
    from apps.practice.models import Answer, Attempt, Choice, PracticeSet, Question

    practice_set = PracticeSet.objects.create(topic=lesson.topic, title="Quick check")
    question = Question.objects.create(practice_set=practice_set, prompt="2 + 2?")
    choice = Choice.objects.create(question=question, text="4", is_correct=True)
    attempt = Attempt.objects.create(user=student, practice_set=practice_set)
    Answer.objects.create(attempt=attempt, question=question, choice=choice, is_correct=True)
    data = export_user_data(student)
    assert data["practice_attempts"][0]["answers"][0]["is_correct"] is True


def test_data_export_requires_login(client):
    assert client.get(reverse("accounts:data_export")).status_code == 302


# ---------- account deletion ----------

def test_profile_shows_privacy_section(client, student):
    client.force_login(student)
    html = client.get(reverse("accounts:profile")).content.decode()
    assert "Download my data" in html and reverse("accounts:delete_account") in html


def test_delete_account_needs_correct_password(client, student):
    client.force_login(student)
    assert client.get(reverse("accounts:delete_account")).status_code == 200
    response = client.post(reverse("accounts:delete_account"), {"password": "wrong"})
    assert response.status_code == 200 and "password" in response.context["form"].errors
    assert User.objects.filter(pk=student.pk).exists()


def test_delete_account_removes_user_and_data_and_logs_out(client, student, offering):
    from apps.accounts.models import StudentProfile
    from apps.learning.models import Enrollment

    Enrollment.objects.create(user=student, offering=offering)
    client.force_login(student)
    response = client.post(reverse("accounts:delete_account"), {"password": PASSWORD}, follow=True)
    assert response.redirect_chain[-1][0] == reverse("accounts:account_deleted")
    assert "has been deleted" in response.content.decode()
    assert not User.objects.filter(pk=student.pk).exists()
    assert not StudentProfile.objects.filter(user_id=student.pk).exists()
    assert not Enrollment.objects.exists()
    assert "_auth_user_id" not in client.session


def test_staff_cannot_self_delete(client):
    staff = User.objects.create_user(email="editor@example.com", password=PASSWORD, is_staff=True)
    client.force_login(staff)
    response = client.post(reverse("accounts:delete_account"), {"password": PASSWORD})
    assert response.url == reverse("accounts:profile")
    assert User.objects.filter(pk=staff.pk).exists()
