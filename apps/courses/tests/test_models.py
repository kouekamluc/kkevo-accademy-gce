import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction

from apps.courses.models import Course, Lesson, LessonBlock, Module, Topic

pytestmark = pytest.mark.django_db


def test_modules_and_lessons_follow_order_field(course):
    Module.objects.create(course=course, title="Third", order=3)
    Module.objects.create(course=course, title="First", order=1)
    Module.objects.create(course=course, title="Second", order=2)
    assert [m.title for m in course.modules.all()] == ["First", "Second", "Third"]

    topic = Topic.objects.create(module=course.modules.first(), title="T")
    Lesson.objects.create(topic=topic, title="B", slug="b", order=2)
    Lesson.objects.create(topic=topic, title="A", slug="a", order=1)
    assert [lesson.slug for lesson in topic.lessons.all()] == ["a", "b"]


def test_equal_order_values_are_allowed_and_tie_break_on_pk(course):
    first = Module.objects.create(course=course, title="X", order=1)
    second = Module.objects.create(course=course, title="Y", order=1)
    assert list(course.modules.all()) == [first, second]


def test_lesson_slug_unique_within_topic(lesson):
    with pytest.raises(IntegrityError), transaction.atomic():
        Lesson.objects.create(topic=lesson.topic, title="Dup", slug=lesson.slug)


def test_course_published_queryset_and_url(course, offering):
    Course.objects.create(offering=offering, title="Draft course", slug="draft-course")
    assert list(Course.objects.published()) == [course]
    assert course.get_absolute_url() == "/courses/test-course/"
    assert course.subject == offering.subject and course.level == offering.level


def test_learning_outcomes_split_into_lines(course):
    course.learning_outcomes = "One\n\n  Two  \n"
    assert course.outcomes_list == ["One", "Two"]


def test_media_blocks_need_url_and_text_blocks_need_content(lesson):
    with pytest.raises(ValidationError):
        LessonBlock(lesson=lesson, block_type="video").full_clean()
    with pytest.raises(ValidationError):
        LessonBlock(lesson=lesson, block_type="text").full_clean()
    LessonBlock(lesson=lesson, block_type="text", body="Hello").full_clean()
    LessonBlock(lesson=lesson, block_type="image", media_url="https://example.com/a.png").full_clean()
