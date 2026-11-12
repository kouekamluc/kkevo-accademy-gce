"""Search: what a student types should land on the right lesson, even half-typed or misspelt."""

import pytest
from django.core.management import call_command
from django.urls import reverse

from apps.courses import search


@pytest.fixture
def library(db):
    call_command("load_gce_curriculum")
    for course in ("biology:form-5", "chemistry:form-5", "chemistry:lower-sixth"):
        call_command("load_lessons", "--only", course)
        call_command("load_practice", "--only", course)
    search.reset_index()
    yield
    search.reset_index()


def titles(result, kind=None, n=5):
    return [h.doc.title for h in result["hits"] if kind in (None, h.doc.kind)][:n]


def test_parse_understands_classes_shortcuts_and_mock():
    query = search.parse("O-Level maths mock on the fractions")
    assert query.levels == {"form-5"} and query.kind == search.MOCK
    assert query.terms == ["mathematic", "fraction"]  # stop words dropped, plurals folded, "maths" expanded
    assert search.parse("upper sixth").levels == {"upper-sixth"}
    assert search.parse("the").terms == ["the"]  # never an empty query just because every word is common


def test_search_ranks_title_matches_first_and_groups_kinds(library):
    result = search.search("photosynthesis")
    assert result["hits"] and all("hotosynthesis" in t for t in titles(result, n=3))
    assert result["counts"][search.LESSON] >= 2 and result["counts"][search.PRACTICE] >= 1
    assert result["counts"][search.SUBJECT] == 0  # a subject card answers its name, not any word in a lesson
    assert "<mark>Photosynthesis</mark>" in result["hits"][0].title_html

    subject = search.search("chem")  # half a word is enough, and the subject itself comes first
    assert subject["hits"][0].doc.kind == search.SUBJECT and subject["hits"][0].doc.title == "Chemistry"


def test_search_forgives_spelling_and_says_so(library):
    result = search.search("fotosynthesis")
    assert result["corrected"] == "photosynthesis" and "Photosynthesis" in titles(result)[0]
    assert search.search("zzzqqq")["hits"] == []


def test_search_uses_the_class_in_the_query_and_the_students_class(library):
    a_level = search.search("a level mole")
    assert a_level["hits"] and {h.doc.level_slug for h in a_level["hits"]} == {"lower-sixth"}
    assert search.search("mole", user_level="lower-sixth")["hits"][0].doc.level_slug == "lower-sixth"
    assert search.search("mole", user_level="form-5")["hits"][0].doc.level_slug == "form-5"

    mocks = search.search("chemistry mock")
    assert mocks["hits"] and all(h.doc.kind == search.MOCK for h in mocks["hits"])
    assert mocks["counts"][search.LESSON] > 0  # the other tabs still know what they would show


def test_index_rebuilds_when_content_changes(library):
    from apps.courses.models import Lesson

    assert search.search("zymurgy")["hits"] == []
    lesson = Lesson.objects.filter(status="published").first()
    lesson.title = "Zymurgy for beginners"
    lesson.save()
    assert titles(search.search("zymurgy")) == ["Zymurgy for beginners"]


def test_search_page_and_suggestions(client, library):
    page = client.get(reverse("courses:search"), {"q": "osmosis"})
    body = page.content.decode()
    assert page.status_code == 200 and "Lessons" in body and "Practice" in body and "<mark>Osmosis</mark>" in body
    assert 'id="search-q"' in body

    partial = client.get(reverse("courses:search"), {"q": "osmosis", "type": "lesson"}, headers={"HX-Request": "true"})
    assert partial.status_code == 200 and b'id="search-q"' not in partial.content and b"search-results" in partial.content

    assert "What do you want to learn?" in client.get(reverse("courses:search")).content.decode()
    assert "Nothing found" in client.get(reverse("courses:search"), {"q": "zzzqqq"}).content.decode()

    suggest = client.get(reverse("courses:search_suggest"), {"q": "osmo"})
    assert suggest.status_code == 200 and b"See all" in suggest.content and suggest.content.count(b"<a ") <= 7
    assert client.get(reverse("courses:search_suggest"), {"q": "o"}).content.strip() == b""
