import json

import pytest
from django.contrib.auth import get_user_model

from apps.core.pwa import USER_HEADER, user_key

pytestmark = pytest.mark.django_db


def test_manifest_is_valid_and_installable(client):
    response = client.get("/manifest.webmanifest")
    assert response.status_code == 200
    assert response["Content-Type"].startswith("application/manifest+json")
    data = json.loads(response.content)
    assert data["name"] == "KKEVO Academy" and data["display"] == "standalone"
    assert data["start_url"].startswith("/dashboard/") and data["scope"] == "/"
    assert data["theme_color"] == "#5B3FE4"
    sizes = {(i["sizes"], i["purpose"]) for i in data["icons"]}
    assert ("192x192", "any") in sizes and ("512x512", "any") in sizes and ("512x512", "maskable") in sizes
    assert all(i["src"].endswith(".png") for i in data["icons"])


def test_icon_files_exist():
    from pathlib import Path

    img = Path(__file__).resolve().parents[3] / "static" / "img"
    for name in ("icon-192.png", "icon-512.png", "icon-maskable-512.png", "apple-touch-icon.png"):
        assert (img / name).read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_service_worker_headers_and_content(client):
    response = client.get("/sw.js")
    assert response.status_code == 200
    assert response["Content-Type"].startswith("text/javascript")
    assert response["Service-Worker-Allowed"] == "/"
    assert "no-cache" in response["Cache-Control"]
    body = response.content.decode()
    assert 'const OFFLINE_URL = "/offline/"' in body and "kkevo-shell-" in body
    assert "css/app.css" in body and "/studio/" in body and "/accounts/" in body and "/practice/" in body
    assert "{{" not in body and "{%" not in body  # fully rendered


def test_service_worker_version_is_stable_and_never_caches_posts(client):
    first = client.get("/sw.js").content.decode()
    assert first == client.get("/sw.js").content.decode()
    assert 'request.method !== "GET"' in first  # mutations are passed through untouched
    assert "caches.delete(LESSONS)" in first  # cleared on logout / user change


def test_offline_page_renders(client):
    response = client.get("/offline/")
    assert response.status_code == 200
    html = response.content.decode()
    assert "No connection right now" in html and "Try again" in html


def test_base_template_links_manifest_and_icons(client):
    html = client.get("/").content.decode()
    assert 'rel="manifest" href="/manifest.webmanifest"' in html
    assert 'name="theme-color" content="#5B3FE4"' in html
    assert "apple-touch-icon" in html and "apple-mobile-web-app-capable" in html
    assert "js/pwa.js" in html


def test_user_key_header_only_for_signed_in_users(client):
    assert USER_HEADER not in client.get("/").headers
    user = get_user_model().objects.create_user(email="pwa@example.com", password="pw-12345-xyz")
    client.force_login(user)
    response = client.get("/")
    assert response[USER_HEADER] == user_key(user)
    other = get_user_model().objects.create_user(email="pwa2@example.com", password="pw-12345-xyz")
    assert user_key(other) != user_key(user)
    assert user_key(user) not in client.get("/manifest.webmanifest").content.decode()
