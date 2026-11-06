import io

import pytest
from django.core.management import call_command
from django.test import Client

pytestmark = pytest.mark.django_db


def test_pages_use_no_third_party_hosts_or_unused_flowbite():
    html = Client().get("/").content.decode()
    assert "fonts.googleapis.com" not in html
    assert "flowbite" not in html
    assert "vendor/fonts/nunito-latin-wght-normal.woff2" in html


def test_measure_pages_reports_every_student_page(tmp_path):
    call_command("seed_demo", "--with-student", stdout=io.StringIO())
    out = io.StringIO()
    report = tmp_path / "weight.md"
    call_command("measure_pages", "--write", str(report), stdout=out, stderr=io.StringIO())
    text = report.read_text(encoding="utf-8")
    for page in ("Landing", "Dashboard", "Course overview", "Lesson, reading", "Lesson, video", "Practice", "Study planner"):
        assert page in text
    assert "googleapis" not in text


def test_lessons_without_maths_do_not_count_katex(tmp_path):
    call_command("seed_demo", "--with-student", stdout=io.StringIO())
    out = io.StringIO()
    call_command("measure_pages", stdout=out, stderr=io.StringIO())
    rows = {line.split("|")[1].strip(): line for line in out.getvalue().splitlines() if line.startswith("| Lesson")}
    video = next(v for k, v in rows.items() if k.startswith("Lesson, video"))
    reading = next(v for k, v in rows.items() if k.startswith("Lesson, reading"))
    total = lambda row: float(row.split("|")[5].strip(" *KB"))
    assert total(reading) - total(video) > 60  # KaTeX (~79 KB gzip) only where there is maths
