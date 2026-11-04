import pytest
from django.contrib.auth import get_user_model

User = get_user_model()
pytestmark = pytest.mark.django_db


def test_create_user_uses_email_and_hashes_password():
    user = User.objects.create_user(email="Student@Example.COM", password="s3cure-pass!", first_name="Ama")
    assert user.email == "student@example.com"
    assert user.password != "s3cure-pass!"
    assert user.check_password("s3cure-pass!")
    assert not user.is_staff and not user.is_superuser


def test_email_is_required():
    with pytest.raises(ValueError):
        User.objects.create_user(email="", password="x")


def test_email_is_unique():
    User.objects.create_user(email="a@example.com", password="pw-123456")
    with pytest.raises(Exception):
        User.objects.create_user(email="a@example.com", password="pw-123456")


def test_create_superuser_flags():
    admin = User.objects.create_superuser(email="admin@example.com", password="pw-123456")
    assert admin.is_staff and admin.is_superuser


def test_initials_and_display_name():
    user = User(email="ngwa@example.com", first_name="Alex", last_name="Nfor")
    assert user.initials == "AN"
    assert user.display_name == "Alex Nfor"
    assert User(email="ngwa@example.com").display_name == "ngwa"
