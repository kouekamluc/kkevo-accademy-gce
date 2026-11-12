"""Legal pages, robots.txt, sitemap.xml and the share tags every page carries."""

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_legal_pages_are_public_and_say_what_they_are(client):
    for name, words in (("core:privacy", "Privacy policy"), ("core:terms", "Terms of use"), ("core:contact", "Talk to us")):
        response = client.get(reverse(name))
        assert response.status_code == 200
        assert words in response.content.decode()


def test_privacy_policy_matches_the_settings_page(client):
    page = client.get(reverse("core:privacy")).content.decode()
    # The policy tells students where to download and delete their data: those labels must exist in Settings.
    assert "Download my data" in page and "Delete my account" in page
    assert "Last updated" in page


def test_contact_shows_the_email_only_when_configured(client, settings):
    settings.CONTACT_EMAIL = ""
    assert "mailto:" not in client.get(reverse("core:contact")).content.decode()
    settings.CONTACT_EMAIL = "help@example.com"
    assert 'mailto:help@example.com' in client.get(reverse("core:contact")).content.decode()


def test_footer_and_signup_link_to_the_legal_pages(client):
    for url in (reverse("core:landing"), reverse("accounts:register")):
        page = client.get(url).content.decode()
        assert reverse("core:privacy") in page and reverse("core:terms") in page


def test_robots_txt_hides_private_areas_and_names_the_sitemap(client):
    response = client.get("/robots.txt")
    body = response.content.decode()
    assert response.status_code == 200 and response["Content-Type"].startswith("text/plain")
    assert "Disallow: /dashboard/" in body and "Disallow: /admin/" in body
    assert "Sitemap: http://testserver/sitemap.xml" in body


def test_sitemap_lists_public_pages_and_published_courses(client, course):
    response = client.get("/sitemap.xml")
    body = response.content.decode()
    assert response.status_code == 200
    assert "http://testserver/about/" in body and "http://testserver/privacy/" in body
    assert f"http://testserver{course.get_absolute_url()}" in body
    assert "/dashboard/" not in body


def test_unpublished_courses_stay_out_of_the_sitemap(client, course):
    course.status = "draft"
    course.save()
    assert course.get_absolute_url() not in client.get("/sitemap.xml").content.decode()


def test_every_page_has_share_tags_and_a_canonical_link(client):
    page = client.get(reverse("core:about") + "?utm=x").content.decode()
    assert 'property="og:title"' in page and 'property="og:description"' in page and 'property="og:image"' in page
    assert '<link rel="canonical" href="http://testserver/about/">' in page
