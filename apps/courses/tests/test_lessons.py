import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson, LessonBlock
from apps.courses.templatetags.lesson_tags import polynomial_plot, rich
from apps.learning.models import DailyActivity, LessonNote, LessonProgress, SavedLesson

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db):
    return User.objects.create_user(email="l@example.com", password="pw-Strong-123", first_name="Lea")


@pytest.fixture
def lessons(lesson):
    second = Lesson.objects.create(topic=lesson.topic, title="Lesson B", slug="lesson-b", order=2, status="published")
    lesson.status = "published"
    lesson.objectives = "First objective\nSecond objective"
    lesson.save()
    LessonBlock.objects.bulk_create([
        LessonBlock(lesson=lesson, order=1, block_type="heading", title="Introduction"),
        LessonBlock(lesson=lesson, order=2, block_type="text", body="Hello **world** with $x^2$ <b>raw</b>"),
        LessonBlock(lesson=lesson, order=3, block_type="worked_example", title="Example", body="x=1",
                    data={"steps": [{"title": "Step one", "math": "x = 1", "final": True}]}),
        LessonBlock(lesson=lesson, order=4, block_type="graph", alt_text="Parabola", data={"coeffs": [1, 0, 0], "roots": [0]}),
        LessonBlock(lesson=lesson, order=5, block_type="quiz", body="Pick", data={"choices": ["a", "b"], "correct": 1}),
    ])
    return lesson, second


def url(lesson, name="courses:lesson"):
    return reverse(name, args=[lesson.course.slug, lesson.pk])


def test_lesson_requires_login(client, lessons):
    assert client.get(url(lessons[0])).status_code == 302


def test_reading_lesson_renders_blocks_safely_and_tracks_view(client, student, lessons):
    first, second = lessons
    client.force_login(student)
    response = client.get(url(first))
    html = response.content.decode()
    assert response.status_code == 200
    assert "<strong>world</strong>" in html and "&lt;b&gt;raw&lt;/b&gt;" in html and "$x^2$" in html
    assert 'data-toc="Introduction"' in html and "First objective" in html and "<polyline" in html
    assert response.context["next_lesson"] == second and response.context["prev_lesson"] is None
    assert [t["title"] for t in response.context["toc"]] == ["Learning objectives", "Introduction", "Example"]
    assert LessonProgress.objects.filter(user=student, lesson=first).exists()


def test_unpublished_lesson_hidden_from_students(client, student, lessons):
    first, _ = lessons
    first.status = "draft"
    first.save()
    client.force_login(student)
    assert client.get(url(first)).status_code == 404
    staff = User.objects.create_user(email="staff@example.com", password="pw-Strong-123", is_staff=True)
    client.force_login(staff)
    assert client.get(url(first)).status_code == 200


def test_lesson_url_must_match_course(client, student, lessons):
    client.force_login(student)
    assert client.get(reverse("courses:lesson", args=["other-course", lessons[0].pk])).status_code == 404


def test_mark_complete_htmx_and_redirect(client, student, lessons):
    first, second = lessons
    client.force_login(student)
    response = client.post(url(first, "courses:lesson_complete"), HTTP_HX_REQUEST="true")
    assert "Lesson complete" in response.content.decode() and "Lesson B" in response.content.decode()
    progress = LessonProgress.objects.get(user=student, lesson=first)
    assert progress.is_completed and progress.percent == 100
    assert client.post(url(second, "courses:lesson_complete")).url == second.course.get_absolute_url()


def test_heartbeat_records_time_and_caps_values(client, student, lessons):
    first, _ = lessons
    client.force_login(student)
    client.post(url(first, "courses:lesson_heartbeat"), {"seconds": 30, "percent": 40, "position": "Example"})
    client.post(url(first, "courses:lesson_heartbeat"), {"seconds": 99999, "percent": 100})
    p = LessonProgress.objects.get(user=student, lesson=first)
    assert p.time_spent_seconds == 150 and p.percent == 99 and p.position_label == "Example"
    assert not p.is_completed  # only the explicit button completes a lesson
    assert DailyActivity.objects.get(user=student, date=timezone.localdate()).seconds == 150
    assert client.post(url(first, "courses:lesson_heartbeat"), {"seconds": "x"}).status_code == 400


def test_save_toggle_and_notes(client, student, lessons):
    first, _ = lessons
    client.force_login(student)
    client.post(url(first, "courses:lesson_save"))
    assert SavedLesson.objects.filter(user=student, lesson=first).exists()
    response = client.post(url(first, "courses:lesson_save"), HTTP_HX_REQUEST="true")
    assert 'aria-pressed="false"' in response.content.decode()
    client.post(url(first, "courses:lesson_note"), {"body": "Remember the sign", "video_time": "95"})
    client.post(url(first, "courses:lesson_note"), {"body": "   "})
    assert list(LessonNote.objects.filter(user=student).values_list("body", "video_time")) == [("Remember the sign", 95)]


def test_video_and_interactive_lessons_use_their_layouts(client, student, lessons):
    first, second = lessons
    second.lesson_type = "video"
    second.save()
    LessonBlock.objects.create(lesson=second, block_type="video", title="Clip", data={"duration": 300, "chapters": [[0, "Start"], [60, "Middle"]]})
    first.lesson_type = "interactive"
    first.save()
    LessonBlock.objects.create(lesson=first, block_type="simulation", order=0, data={"key": "newton-cart"})
    client.force_login(student)
    assert "lessons/video.html" in [t.name for t in client.get(url(second)).templates]
    response = client.get(url(first))
    assert "lessons/interactive.html" in [t.name for t in response.templates]
    assert "newtonCart()" in response.content.decode()


def test_rich_filter_escapes_html():
    assert rich("<script>alert(1)</script>") == "<p>&lt;script&gt;alert(1)&lt;/script&gt;</p>"


def test_polynomial_plot_geometry():
    g = polynomial_plot({"coeffs": [1, -5, 6], "xmin": 0, "xmax": 5, "ymin": -1, "ymax": 6, "roots": [2, 3]})
    assert len(g["roots"]) == 2 and g["points"]
    assert polynomial_plot({"coeffs": []}) is None


def test_polynomial_plot_keeps_a_small_number_of_ticks():
    small = polynomial_plot({"coeffs": [1, -5, 6], "xmin": -5, "xmax": 5, "ymin": -5, "ymax": 5})
    assert [t["label"] for t in small["xticks"]] == [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    assert [t["label"] for t in small["yticks"]] == [-4, -2, 2, 4]
    big = polynomial_plot({"coeffs": [2000, 50000], "xmin": 0, "xmax": 120, "ymin": 0, "ymax": 300000})
    assert len(big["xticks"]) <= 12 and len(big["yticks"]) <= 8
    assert big["yticks"][0]["label"] == "50\u202f000"


def test_curve_label_moves_to_the_corner_the_curve_avoids():
    rising = polynomial_plot({"coeffs": [1, -6, 9, 0], "xmin": -0.5, "xmax": 4.5, "ymin": -1, "ymax": 6})
    assert rising["label_anchor"] == "start"  # the cubic climbs into the top right, so the name goes top left
    falling = polynomial_plot({"coeffs": [-1, 6, -9, 0], "xmin": -0.5, "xmax": 4.5, "ymin": -6, "ymax": 1})
    assert falling["label_anchor"] == "end"
    parabola = polynomial_plot({"coeffs": [1, -5, 6], "xmin": 0, "xmax": 5.5, "ymin": -1, "ymax": 6.5})
    assert parabola["label_anchor"] in ("start", "end")


def test_reading_lesson_offers_cards_mode_and_keeps_full_page_content(client, django_user_model, course, lesson):
    """Cards mode is progressive enhancement: the whole lesson is still in the HTML, plus the card controls."""
    lesson.status = "published"
    lesson.save()
    user = django_user_model.objects.create_user(email="cards@example.com", password="pw-Strong-123")
    client.force_login(user)
    html = client.get(lesson.get_absolute_url()).content.decode()
    assert 'id="lesson-body" data-cards' in html
    assert 'id="card-progress"' in html and "primaryLabel" in html
    assert html.count("data-cards-end") == 2 or html.count("data-cards-end") == 3  # complete card, nav (+ practice link)


def test_course_page_is_encouraging_and_subject_tiles_are_solid(client, django_user_model, course, lesson):
    lesson.status = "published"
    lesson.save()
    user = django_user_model.objects.create_user(email="tiles@example.com", password="pw-Strong-123")
    client.force_login(user)
    html = client.get(course.get_absolute_url()).content.decode()
    assert "Ready when you are!" in html and course.offering.subject.colour in html and "+10" in html
