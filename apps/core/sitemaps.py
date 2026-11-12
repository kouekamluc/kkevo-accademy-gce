"""sitemap.xml: the public pages a search engine may list (everything else needs a login)."""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.courses.models import Course


class StaticPages(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ["core:landing", "core:about", "core:how_it_works", "courses:catalog",
                "core:privacy", "core:terms", "core:contact"]

    def location(self, name):
        return reverse(name)

    def priority(self, name):
        return 1.0 if name == "core:landing" else 0.6


class CoursePages(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Course.objects.published().order_by("slug")


SITEMAPS = {"pages": StaticPages, "courses": CoursePages}
