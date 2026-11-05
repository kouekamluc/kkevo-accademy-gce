"""Measure the weight of the student pages (roadmap Feature 17).

    python manage.py measure_pages                       # print a table
    python manage.py measure_pages --write docs/benchmarks/page-weight.md

For each page it renders the HTML as the demo student (run `seed_demo --with-student` first),
then adds up every stylesheet, script and image the HTML asks for, as the browser would
download them on a first visit (empty cache), compressed the way WhiteNoise serves them.

The load time is an estimate for a slow 3G connection (400 kbit/s, 400 ms round trip):
one round trip for the HTML, one for the static files (fetched in parallel), three more per
third-party host (DNS, TCP, TLS), plus the download time of all the bytes. Fonts that CSS loads on demand
(KaTeX's maths fonts) are listed separately because the browser only fetches the ones a page uses.
"""

import gzip
import re
import time
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand, CommandError
from django.db import connection
from django.test import Client
from django.test.utils import CaptureQueriesContext, override_settings

DEMO_EMAIL = "demo.student@example.test"
BYTES_PER_SECOND = 400_000 / 8  # slow 3G: 400 kbit/s
RTT = 0.4  # seconds


class AssetParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.assets = []  # (kind, url)
        self.inline_bytes = 0
        self.lazy_katex = []
        self.has_latex = False
        self.main_text = []
        self._in_inline = False
        self._main_depth = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "data-latex" in a:
            self.has_latex = True
        if tag == "main":
            self._main_depth += 1
        if tag == "script":
            if a.get("src"):
                self.assets.append(("js", a["src"]))
                if a.get("data-katex-js"):  # lesson.js loads KaTeX itself when the page has maths
                    self.lazy_katex = [("js", a["data-katex-js"]), ("js", a["data-katex-auto"]),
                                       ("css", a["data-katex-css"])]
            else:
                self._in_inline = True
        elif tag == "link" and "stylesheet" in (a.get("rel") or "") and a.get("href"):
            self.assets.append(("css", a["href"]))
        elif tag == "link" and a.get("rel") == "preload" and a.get("href"):
            self.assets.append(("font" if a.get("as") == "font" else "other", a["href"]))
        elif tag == "img" and a.get("src") and not a["src"].startswith("data:"):
            self.assets.append(("img", a["src"]))
        elif tag == "iframe" and a.get("src"):
            self.assets.append(("iframe", a["src"]))

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_inline = False
        elif tag == "main":
            self._main_depth -= 1

    def handle_data(self, data):
        if self._in_inline:
            self.inline_bytes += len(data.encode())
        elif self._main_depth:
            self.main_text.append(data)

    def has_maths(self):
        """Same test as lesson.js: a [data-latex] element, or $, \\( or \\[ in the main text."""
        return self.has_latex or bool(re.search(r"\$|\\\(|\\\[", "".join(self.main_text)))


def gz(data: bytes) -> int:
    return len(gzip.compress(data, compresslevel=9))


def static_file(url):
    """Local path for a /static/ URL, or None."""
    path = urlparse(url).path
    prefix = settings.STATIC_URL if settings.STATIC_URL.startswith("/") else "/" + settings.STATIC_URL
    if not path.startswith(prefix):
        return None
    found = finders.find(path[len(prefix):])
    return Path(found) if found else None


def css_fonts(css_path: Path):
    """Fonts a stylesheet can load on demand: list of (name, bytes)."""
    text = css_path.read_text(encoding="utf-8", errors="ignore")
    fonts = []
    for ref in sorted(set(re.findall(r"url\(([^)]+\.woff2)\)", text))):
        font = (css_path.parent / ref.strip("'\"")).resolve()
        if font.exists():
            fonts.append((font.name, font.stat().st_size))
    return fonts


class Command(BaseCommand):
    help = "Measure page weight, request count and an estimated slow-3G load time of the student pages."

    def add_arguments(self, parser):
        parser.add_argument("--write", help="Also write the results as Markdown to this file.")

    def pages(self):
        from apps.courses.models import Course, Lesson
        from apps.practice.models import PracticeSet

        pages = [("Landing", "/", False), ("Explore subjects", "/subjects/", True), ("Dashboard", "/dashboard/", True)]
        course = Course.objects.published().filter(modules__isnull=False).order_by("pk").first()
        if course:
            pages.append((f"Course overview ({course.title})", course.get_absolute_url(), True))
        for lesson_type in ("reading", "interactive", "video"):
            lesson = (Lesson.objects.published().filter(lesson_type=lesson_type, blocks__isnull=False)
                      .order_by("pk").first())
            if lesson:
                pages.append((f"Lesson, {lesson_type} ({lesson.title})", lesson.get_absolute_url(), True))
        pages.append(("Practice", "/practice/", True))
        practice_set = PracticeSet.objects.filter(status="published").order_by("pk").first()
        if practice_set:
            pages.append(("Practice set start", f"/practice/sets/{practice_set.pk}/", True))
        pages += [("My progress", "/learn/progress/", True), ("Study planner", "/learn/planner/", True)]
        return pages

    @override_settings(ALLOWED_HOSTS=["testserver", "localhost", "127.0.0.1"], DEBUG=False)
    def handle(self, *args, **options):
        from django.contrib.auth import get_user_model

        student = get_user_model().objects.filter(email=DEMO_EMAIL).first()
        if not student:
            raise CommandError("No demo student. Run: python manage.py seed_demo --with-student")
        guest, client = Client(), Client()
        client.force_login(student)

        rows, on_demand = [], {}
        for name, url, needs_login in self.pages():
            c = client if needs_login else guest
            with CaptureQueriesContext(connection) as queries:
                start = time.perf_counter()
                response = c.get(url, follow=True)
                server_ms = (time.perf_counter() - start) * 1000
            if response.status_code != 200:
                self.stderr.write(f"{name}: HTTP {response.status_code}, skipped")
                continue
            html = response.content
            parser = AssetParser()
            parser.feed(html.decode("utf-8", errors="ignore"))

            asset_gz, asset_raw, external, missing, seen = 0, 0, set(), [], set()
            assets = parser.assets + (parser.lazy_katex if parser.has_maths() else [])
            for kind, asset_url in assets:
                if asset_url in seen:
                    continue
                seen.add(asset_url)
                host = urlparse(asset_url).netloc
                if host and host not in ("testserver", "localhost", "127.0.0.1"):
                    external.add(host)
                    continue
                path = static_file(asset_url)
                if not path:
                    missing.append(asset_url)
                    continue
                data = path.read_bytes()
                asset_raw += len(data)
                asset_gz += gz(data) if kind in ("js", "css") else len(data)
                if kind == "css":
                    for font, size in css_fonts(path):
                        on_demand[font] = size

            html_gz = gz(html)
            total = html_gz + asset_gz
            requests = 1 + len(seen)
            # each third-party host costs a DNS lookup, TCP and TLS handshake (~3 round trips)
            est = RTT * (2 + 3 * len(external)) + total / BYTES_PER_SECOND
            rows.append(dict(
                name=name, url=url, html_kb=len(html) / 1024, html_gz_kb=html_gz / 1024,
                inline_kb=parser.inline_bytes / 1024, assets_gz_kb=asset_gz / 1024, total_kb=total / 1024,
                requests=requests, external=", ".join(sorted(external)) or "none", queries=len(queries),
                server_ms=server_ms, est_s=est, missing=missing))

        lines = [
            "| Page | HTML (gzip) | Inline JS | Static files (gzip) | **Total (gzip)** | Requests | Third-party hosts | DB queries | Server ms | **Est. slow 3G** |",
            "|---|---:|---:|---:|---:|---:|---|---:|---:|---:|",
        ]
        for r in rows:
            lines.append(
                f"| {r['name']} | {r['html_gz_kb']:.1f} KB | {r['inline_kb']:.1f} KB | {r['assets_gz_kb']:.1f} KB | "
                f"**{r['total_kb']:.0f} KB** | {r['requests']} | {r['external']} | {r['queries']} | "
                f"{r['server_ms']:.0f} | **{r['est_s']:.1f} s** |")
        table = "\n".join(lines)
        self.stdout.write(table)
        for r in rows:
            for m in r["missing"]:
                self.stderr.write(f"{r['name']}: asset not found: {m}")
        if on_demand:
            fonts = ", ".join(f"{n} {s / 1024:.0f} KB" for n, s in sorted(on_demand.items()))
            self.stdout.write(f"\nFonts loaded on demand by stylesheets (only the ones a page uses): {fonts}")

        if options["write"]:
            Path(options["write"]).write_text(
                "# Student page weight\n\n"
                "Measured with `python manage.py measure_pages` as the demo student, first visit (empty cache), "
                "static files gzip-compressed as WhiteNoise serves them. Third-party files (e.g. Google Fonts) are not "
                "in the byte totals but cost an extra connection each. Estimated load time assumes slow 3G "
                "(400 kbit/s, 400 ms round trip).\n\n" + table + "\n", encoding="utf-8")
            self.stdout.write(self.style.SUCCESS(f"Written to {options['write']}"))
