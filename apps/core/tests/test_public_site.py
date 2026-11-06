"""The public site is one connected place: every nav destination is a real page with the same header and a sign-up prompt."""

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

pytestmark = pytest.mark.django_db

PUBLIC_PAGES = ["core:landing", "core:how_it_works", "core:about", "courses:catalog"]


@pytest.mark.parametrize("name", PUBLIC_PAGES)
def test_public_pages_share_the_nav_and_point_to_sign_up(client, name):
    response = client.get(reverse(name))
    body = response.content.decode()
    assert response.status_code == 200
    for target in ("core:landing", "courses:catalog", "core:how_it_works", "core:about"):
        assert f'href="{reverse(target)}"' in body
    assert reverse("accounts:register") in body and reverse("accounts:login") in body
    assert 'aria-current="page"' in body  # the current page is highlighted in the nav


def test_visitors_browse_subjects_inside_the_public_shell_not_the_app_sidebar(client):
    body = client.get(reverse("courses:catalog")).content.decode()
    assert 'aria-label="Sidebar"' not in body
    assert reverse("core:about") in body  # public header and footer are present
    assert "Create a free account" in body  # the phone sign-up bar


def test_signed_in_students_keep_the_app_shell(client):
    user = get_user_model().objects.create_user(email="ama@example.com", password="pw-Strong-123")
    client.force_login(user)
    body = client.get(reverse("courses:catalog")).content.decode()
    assert 'aria-label="Sidebar"' in body
    assert "Create a free account" not in body


def test_how_it_works_and_about_are_honest_about_the_board(client):
    assert "not affiliated" in client.get(reverse("core:about")).content.decode()
    assert "Do I need to pay" in client.get(reverse("core:how_it_works")).content.decode()
