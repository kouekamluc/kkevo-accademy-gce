import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.learning import reportcard
from apps.learning.models import Enrollment
from apps.practice.models import Attempt, PracticeSet

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="r@example.com", password="pw-Strong-123", first_name="Rita")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


def test_marks_and_bands():
    assert reportcard.mark_out_of_20(75) == 15.0
    assert reportcard.mark_out_of_20(48) == 9.6  # 48% of 20
    assert reportcard.band_for(80) == ("A", "Excellent")
    assert reportcard.band_for(79) == ("B", "Very good")
    assert reportcard.band_for(40) == ("E", "Must work harder")
    assert reportcard.band_for(0) == ("U", "Needs help")


def test_report_card_needs_a_login(client):
    assert client.get(reverse("learning:report_card")).status_code == 302


def test_empty_report_card_points_to_practice(client, student, lesson, offering):
    Enrollment.objects.create(user=student, offering=offering)
    client.force_login(student)
    html = client.get(reverse("learning:report_card")).content.decode()
    assert "starts with your first practice set" in html
    assert "wa.me" not in html


def test_report_card_marks_a_practised_subject(client, student, lesson, offering):
    lesson.status = "published"
    lesson.save()
    Enrollment.objects.create(user=student, offering=offering)
    practice = PracticeSet.objects.create(topic=lesson.topic, lesson=lesson, title="Set", status="published")
    Attempt.objects.create(user=student, practice_set=practice, correct_count=15, total=20, completed_at=timezone.now())
    client.force_login(student)
    response = client.get(reverse("learning:report_card"))
    html = response.content.decode()
    row = response.context["rows"][0]
    assert (row["mark"], row["grade"], row["remark"]) == (15.0, "B", "Very good")
    assert response.context["average"] == 15.0
    assert "15.0" in html and "Average: 15.0 / 20" in html
    assert "https://wa.me/?text=" in html and "not your GCE result" in html
    assert offering.subject.colour in html
