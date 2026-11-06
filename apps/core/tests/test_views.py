import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_landing_renders_seeded_levels_and_empty_subject_state(client):
    response = client.get(reverse("core:landing"))
    assert response.status_code == 200
    html = response.content.decode()
    assert "Pass your GCE," in html
    for name in ("Form 5", "Lower Sixth", "Upper Sixth"):
        assert name in html
    assert "Subjects are being prepared" in html
    assert reverse("accounts:register") in html
    assert reverse("accounts:login") in html
    assert reverse("courses:catalog") in html


def test_landing_shows_featured_subjects_from_database(client, offering):
    html = client.get(reverse("core:landing")).content.decode()
    assert "Test Subject" in html
    assert "Science · Form 5" in html
    assert "1 subject<" in html  # Form 5 card count
    assert "Subjects are being prepared" not in html


def test_landing_query_count_is_bounded(client, offering, django_assert_max_num_queries):
    with django_assert_max_num_queries(8):
        client.get(reverse("core:landing"))


def test_authenticated_user_sees_dashboard_link(client):
    user = get_user_model().objects.create_user(email="s@example.com", password="pw-123456!")
    client.force_login(user)
    html = client.get(reverse("core:landing")).content.decode()
    assert "Go to dashboard" in html


@pytest.mark.parametrize("name", ["accounts:login", "accounts:register", "courses:catalog"])
def test_public_routes_resolve(client, name):
    assert client.get(reverse(name)).status_code == 200


def test_landing_speaks_to_teenagers_on_phones(client):
    html = client.get(reverse("core:landing")).content.decode()
    assert "Daily streaks" in html and "Points and levels" in html and "Light on data" in html
    assert "Preview of a quiz question" in html and "Kiki" in html


def test_onboarding_is_guided_by_kiki(client, django_user_model):
    user = django_user_model.objects.create_user(email="k@example.com", password="pw-Strong-123")
    client.force_login(user)
    html = client.get(reverse("accounts:onboarding_level")).content.decode()
    assert "I’m Kiki" in html and "Which class are you in?" in html
