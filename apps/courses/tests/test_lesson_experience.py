"""Resume position, low-data media, reading notes, quick-check hints, print and shortcuts."""

import re

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from apps.courses.models import Lesson, LessonBlock
from apps.courses.templatetags.lesson_tags import at, choice_letter
from apps.learning.models import LessonNote, LessonProgress

pytestmark = pytest.mark.django_db
User = get_user_model()

IMG = "https://cdn.example.com/diagram.png"
CLIP = "https://cdn.example.com/clip.mp4"
LIGHT_CLIP = "https://cdn.example.com/clip-240p.mp4"
EMBED = "https://embed.example.com/widget"


@pytest.fixture
def student(db):
    return User.objects.create_user(email="r@example.com", password="pw-Strong-123", first_name="Rita")


@pytest.fixture
def reading(lesson):
    lesson.status = "published"
    lesson.objectives = "One objective"
    lesson.save()
    second = Lesson.objects.create(topic=lesson.topic, title="Lesson B", slug="lesson-b", order=2, status="published")
    blocks = {
        "intro": LessonBlock.objects.create(lesson=lesson, order=1, block_type="heading", title="Introduction"),
        "image": LessonBlock.objects.create(lesson=lesson, order=2, block_type="image", media_url=IMG, alt_text="A labelled diagram"),
        "example": LessonBlock.objects.create(lesson=lesson, order=3, block_type="worked_example", title="Worked example 2",
                                              data={"steps": [{"title": "Step", "math": "x=1"}]}),
        "video": LessonBlock.objects.create(lesson=lesson, order=4, block_type="video", title="Watch: roots", media_url=CLIP,
                                            data={"low_data_url": LIGHT_CLIP, "poster": "https://cdn.example.com/poster.jpg"}),
        "embed": LessonBlock.objects.create(lesson=lesson, order=5, block_type="embed", title="Graph explorer", media_url=EMBED),
        "quiz": LessonBlock.objects.create(lesson=lesson, order=6, block_type="quiz", body="What is 2 + 2?",
                                           data={"choices": ["3", "4", "5"], "correct": 1, "explanation": "Two pairs.",
                                                 "hint": "Count on your fingers.", "feedback": ["One short.", "", "One too many."]}),
        "practice": LessonBlock.objects.create(lesson=lesson, order=7, block_type="practice", body="Solve x+1=2",
                                               data={"answer": "x = 1"}),
    }
    return lesson, second, blocks


def url(lesson, name="courses:lesson", *extra):
    return reverse(name, args=[lesson.course.slug, lesson.pk, *extra])


def outside_templates(html):
    """The page minus <template> contents (which the browser does not fetch until used)."""
    return re.sub(r"<template\b.*?</template>", "", html, flags=re.S)


# --------------------------------------------------------------------------- resume
def test_heartbeat_saves_anchor_and_ignores_unsafe_values(client, student, reading):
    lesson, _, blocks = reading
    client.force_login(student)
    client.post(url(lesson, "courses:lesson_heartbeat"), {"seconds": 5, "percent": 40, "position": "Worked example 2",
                                                          "anchor": blocks["example"].anchor})
    progress = LessonProgress.objects.get(user=student, lesson=lesson)
    assert progress.position_anchor == blocks["example"].anchor
    client.post(url(lesson, "courses:lesson_heartbeat"), {"seconds": 5, "anchor": '"><script>'})
    client.post(url(lesson, "courses:lesson_heartbeat"), {"seconds": 5, "anchor": ""})
    progress.refresh_from_db()
    assert progress.position_anchor == blocks["example"].anchor


def test_reopening_offers_continue_from_saved_section(client, student, reading):
    lesson, _, blocks = reading
    client.force_login(student)
    first = client.get(url(lesson))
    assert first.context["resume"] is None and "Continue from" not in first.content.decode()

    client.post(url(lesson, "courses:lesson_heartbeat"), {"seconds": 5, "percent": 40, "position": "Worked example 2",
                                                          "anchor": blocks["example"].anchor})
    response = client.get(url(lesson))
    html = response.content.decode()
    assert response.context["resume"] == {"anchor": blocks["example"].anchor, "label": "Worked example 2"}
    assert "Continue from Worked example 2" in html and f'href="#{blocks["example"].anchor}"' in html
    assert response.context["auto_resume"] is False and "autoResume: false" in html


def test_resume_falls_back_to_label_and_skips_stale_or_trivial_positions(client, student, reading):
    lesson, _, blocks = reading
    client.force_login(student)
    progress = LessonProgress.objects.create(user=student, lesson=lesson, percent=50,
                                             position_label="Worked example 2", position_anchor="block-99999")
    assert client.get(url(lesson)).context["resume"]["anchor"] == blocks["example"].anchor  # stale anchor → label match

    progress.position_label, progress.position_anchor = "Deleted section", "block-99999"
    progress.save()
    assert client.get(url(lesson)).context["resume"] is None

    progress.position_label, progress.position_anchor, progress.percent = "Learning objectives", "objectives", 3
    progress.save()
    assert client.get(url(lesson)).context["resume"] is None  # still at the very top

    progress.position_label, progress.position_anchor = "Worked example 2", blocks["example"].anchor
    progress.mark_complete()
    progress.save()
    assert client.get(url(lesson)).context["resume"] is None  # finished lessons start at the top


def test_continue_learning_scrolls_automatically(client, student, reading):
    lesson, _, blocks = reading
    client.force_login(student)
    LessonProgress.objects.create(user=student, lesson=lesson, percent=50, position_label="Worked example 2",
                                  position_anchor=blocks["example"].anchor)
    target = client.get(reverse("courses:continue")).url
    assert target.endswith("?resume=1")
    response = client.get(target)
    assert response.context["auto_resume"] is True and "autoResume: true" in response.content.decode()


def test_video_lesson_says_where_playback_resumes(client, student, reading):
    _, second, _ = reading
    second.lesson_type = "video"
    second.save()
    LessonBlock.objects.create(lesson=second, block_type="video", title="Clip", media_url=CLIP, data={"duration": 300})
    LessonProgress.objects.create(user=student, lesson=second, video_position=125)
    client.force_login(student)
    html = client.get(url(second)).content.decode()
    assert "continues from <strong" in html and "02:05" in html and "Start over" in html


# --------------------------------------------------------------------------- low-data mode
def test_low_data_mode_downloads_no_lesson_media_until_asked(client, student, reading):
    lesson, _, _ = reading
    student.profile.low_data_mode = True
    student.profile.save()
    client.force_login(student)
    html = client.get(url(lesson)).content.decode()
    visible = outside_templates(html)
    for media in (IMG, CLIP, LIGHT_CLIP, EMBED, "poster.jpg"):
        assert f'src="{media}' not in visible and "poster=" not in visible
    assert 'data-low-data-placeholder="image"' in html and "A labelled diagram" in visible
    assert 'data-low-data-placeholder="video"' in html and 'data-low-data-placeholder="embed"' in html
    assert "Load image" in html and "Load video" in html and "Load interactive content" in html
    # Once tapped, the lighter video file is used
    assert f'src="{LIGHT_CLIP}"' in html and f'src="{IMG}"' in html


def test_normal_mode_renders_media_directly(client, student, reading):
    lesson, _, _ = reading
    client.force_login(student)
    html = client.get(url(lesson)).content.decode()
    assert "data-low-data-placeholder" not in html
    assert f'src="{IMG}"' in html and f'src="{CLIP}"' in html and f'src="{EMBED}"' in html and "poster=" in html


def test_low_data_video_lesson_player_is_click_to_load(client, student, reading):
    _, second, _ = reading
    second.lesson_type = "video"
    second.save()
    LessonBlock.objects.create(lesson=second, block_type="video", title="Clip", media_url=CLIP,
                               data={"duration": 300, "low_data_url": LIGHT_CLIP, "size_mb": 9})
    student.profile.low_data_mode = True
    student.profile.save()
    client.force_login(student)
    html = client.get(url(second)).content.decode()
    assert CLIP not in outside_templates(html) and LIGHT_CLIP not in outside_templates(html)
    assert "Load lighter video" in html and "about 9 MB" in html and "loaded: false" in html


# --------------------------------------------------------------------------- notes
def test_reading_lesson_has_notes_panel_with_section_notes(client, student, reading):
    lesson, _, blocks = reading
    client.force_login(student)
    html = client.get(url(lesson)).content.decode()
    assert 'id="notes-toggle"' in html and 'aria-labelledby="notes-title"' in html and 'name="section_anchor"' in html

    response = client.post(url(lesson, "courses:lesson_note"), {
        "body": "Check the sign of b", "section_label": "Worked example 2", "section_anchor": blocks["example"].anchor,
    }, HTTP_HX_REQUEST="true")
    body = response.content.decode()
    note = LessonNote.objects.get(user=student, lesson=lesson)
    assert (note.section_label, note.section_anchor, note.video_time) == ("Worked example 2", blocks["example"].anchor, None)
    assert f'href="#{blocks["example"].anchor}"' in body and 'hx-swap-oob="innerHTML:#note-count">1<' in body

    html = client.get(url(lesson)).content.decode()
    assert "Check the sign of b" in html and "hx-swap-oob" not in html  # count only swapped on HTMX responses


def test_note_section_anchor_is_sanitised(client, student, reading):
    lesson, _, _ = reading
    client.force_login(student)
    client.post(url(lesson, "courses:lesson_note"), {"body": "x", "section_anchor": "a b<script>"})
    assert LessonNote.objects.get(user=student).section_anchor == ""


def test_students_delete_only_their_own_notes(client, student, reading):
    lesson, _, _ = reading
    other = User.objects.create_user(email="o@example.com", password="pw-Strong-123")
    mine = LessonNote.objects.create(user=student, lesson=lesson, body="mine")
    theirs = LessonNote.objects.create(user=other, lesson=lesson, body="theirs")
    client.force_login(student)
    assert client.post(url(lesson, "courses:lesson_note_delete", theirs.pk)).status_code == 404
    assert client.get(url(lesson, "courses:lesson_note_delete", mine.pk)).status_code == 405
    response = client.post(url(lesson, "courses:lesson_note_delete", mine.pk), HTTP_HX_REQUEST="true")
    assert "No notes yet" in response.content.decode() and ">0<" in response.content.decode()
    assert list(LessonNote.objects.values_list("body", flat=True)) == ["theirs"]


def test_interactive_lesson_also_has_notes_and_video_keeps_its_tab(client, student, reading):
    lesson, second, _ = reading
    lesson.lesson_type = "interactive"
    lesson.save()
    LessonBlock.objects.create(lesson=lesson, order=0, block_type="simulation", data={"key": "newton-cart"})
    second.lesson_type = "video"
    second.save()
    LessonBlock.objects.create(lesson=second, block_type="video", title="Clip", data={"duration": 60})
    client.force_login(student)
    assert 'id="notes-toggle"' in client.get(url(lesson)).content.decode()
    video_html = client.get(url(second)).content.decode()
    assert 'id="notes-toggle"' not in video_html and "My notes" in video_html


# --------------------------------------------------------------------------- quick checks, print, shortcuts
def test_quick_check_hint_and_per_choice_feedback(client, student, reading):
    lesson, _, _ = reading
    client.force_login(student)
    html = client.get(url(lesson)).content.decode()
    assert "Get a hint" in html and "Count on your fingers." in html
    assert "One short." in html and "One too many." in html and "Show answer" in html
    assert "Answer: B." in html  # printed answer and revealed-answer text


def test_quiz_filters():
    assert [choice_letter(i) for i in (0, 1, "2")] == ["A", "B", "C"] and choice_letter("x") == ""
    assert at(["a", "b"], 1) == "b" and at(["a"], 5) == "" and at(None, 0) == ""


def test_print_view_and_shortcuts_markup(client, student, reading):
    lesson, second, _ = reading
    client.force_login(student)
    html = client.get(url(lesson)).content.decode()
    assert "Print or save as PDF" in html and "print:hidden" in html and "print:!block" in html
    assert "Keyboard shortcuts" in html and f"nextUrl: '{second.get_absolute_url()}'" in html
