"""Signing up and logging in with a phone number instead of an email."""

import pytest
from django.contrib.auth import get_user_model
from django.core import mail
from django.urls import reverse

from apps.accounts.models import normalize_phone

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.mark.parametrize("raw", ["677123456", "677 12 34 56", "+237 677 12 34 56", "00237677123456", "237-677-123-456"])
def test_phone_numbers_are_normalised(raw):
    assert normalize_phone(raw) == "+237677123456"


@pytest.mark.parametrize("raw", ["", "12345", "577123456", "+33612345678", "abc"])
def test_bad_phone_numbers_are_rejected(raw):
    assert normalize_phone(raw) is None


def register(client, **extra):
    data = {"full_name": "Ngu Brice", "password": "Strong-pass-7531", "accept_terms": "on", **extra}
    return client.post(reverse("accounts:register"), data)


def test_can_register_with_a_phone_number_only(client):
    response = register(client, phone="677 12 34 56")
    assert response.status_code == 302
    user = User.objects.get(phone="+237677123456")
    assert not user.has_real_email and user.contact == "+237677123456"
    assert user.display_name == "Ngu Brice"


def test_needs_an_email_or_a_phone(client):
    response = register(client)
    assert response.status_code == 200 and not User.objects.exists()
    assert b"phone number if you have no email" in response.content


def test_invalid_and_duplicate_phone_numbers_are_refused(client):
    assert register(client, phone="12345").status_code == 200
    register(client, phone="677123456")
    client.logout()
    assert register(client, phone="+237 677 123 456").status_code == 200
    assert User.objects.count() == 1


def test_log_in_with_phone_number_in_any_format(client):
    register(client, phone="677123456")
    client.logout()
    response = client.post(reverse("accounts:login"), {"username": "+237 677 12 34 56", "password": "Strong-pass-7531"})
    assert response.status_code == 302
    assert "_auth_user_id" in client.session


def test_wrong_phone_or_password_does_not_log_in(client):
    register(client, phone="677123456")
    client.logout()
    assert client.post(reverse("accounts:login"), {"username": "677123456", "password": "nope"}).status_code == 200
    assert client.post(reverse("accounts:login"), {"username": "688000111", "password": "Strong-pass-7531"}).status_code == 200


def test_email_login_still_works(client):
    User.objects.create_user(email="a@example.com", password="Strong-pass-7531")
    response = client.post(reverse("accounts:login"), {"username": "A@Example.com", "password": "Strong-pass-7531"})
    assert response.status_code == 302


def test_phone_only_account_gets_no_reset_or_reminder_mail(client):
    register(client, phone="677123456")
    client.logout()
    client.post(reverse("accounts:password_reset"), {"email": "237677123456@phone.kkevo.invalid"})
    assert mail.outbox == []
    from apps.learning import reminders

    assert reminders.send_for(User.objects.get(phone="+237677123456")) is False


def test_can_add_an_email_later_in_settings(client):
    register(client, phone="677123456")
    response = client.post(reverse("accounts:profile"), {
        "section": "details", "details-first_name": "Ngu", "details-last_name": "Brice", "details-email": "brice@example.com", "details-phone": "677123456"})
    assert response.status_code == 302
    user = User.objects.get(phone="+237677123456")
    assert user.email == "brice@example.com" and user.has_real_email


def test_cannot_remove_both_email_and_phone(client):
    register(client, phone="677123456")
    response = client.post(reverse("accounts:profile"), {
        "section": "details", "details-first_name": "Ngu", "details-last_name": "Brice", "details-email": "", "details-phone": ""})
    assert response.status_code == 200
    assert User.objects.get().phone == "+237677123456"
