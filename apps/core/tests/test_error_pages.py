import pytest
from django.template.loader import render_to_string

pytestmark = pytest.mark.django_db


def test_unknown_page_shows_the_branded_404(client):
    response = client.get("/this-page-does-not-exist/")
    html = response.content.decode()
    assert response.status_code == 404
    assert "can’t find that page" in html and "Kiki" in html and "KKEVO Academy" in html


def test_server_error_page_renders_without_a_request():
    html = render_to_string("500.html")  # Django renders the 500 page with no request or context processors
    assert "went wrong on our side" in html and "Kiki" in html and "#5B3FE4" in html


def test_other_error_pages_are_branded():
    for name, text in (("403.html", "can’t open this page"), ("400.html", "didn’t look right"), ("403_csrf.html", "session timed out")):
        html = render_to_string(name)
        assert text in html and "Kiki" in html


def test_admin_and_staff_use_the_brand_palette():
    from django.conf import settings

    colours = settings.UNFOLD["COLORS"]
    assert colours["primary"]["600"] == "#5B3FE4"
    assert "#2563EB" not in str(colours) and "#102A43" not in pathlib_read("static/css/staff.css")


def pathlib_read(rel):
    import pathlib

    return (pathlib.Path(__file__).resolve().parents[3] / rel).read_text(encoding="utf-8")
