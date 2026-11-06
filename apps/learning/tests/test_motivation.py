from datetime import date, datetime, time, timedelta

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

from apps.courses.models import Lesson
from apps.learning import motivation
from apps.learning.models import (DailyActivity, Enrollment, LessonProgress, LinkPurpose, PrivateLink, RestDay,
                                  StudySession)

pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def student(db, form5, science):
    user = User.objects.create_user(email="m@example.com", password="pw-Strong-123", first_name="Mia")
    p = user.profile
    p.level, p.pathway, p.onboarded_at = form5, science, timezone.now()
    p.save()
    return user


@pytest.fixture
def plan(student, offering, lesson):
    """Student enrolled in a course with 4 published lessons, 1 completed."""
    lesson.status = "published"
    lesson.save()
    others = [Lesson.objects.create(topic=lesson.topic, title=f"L{i}", slug=f"l{i}", order=i + 1, status="published")
              for i in range(3)]
    Enrollment.objects.create(user=student, offering=offering)
    LessonProgress.objects.create(user=student, lesson=lesson, percent=100, completed_at=timezone.now())
    return [lesson] + others


def at(day, hour=17, minute=0):
    return timezone.make_aware(datetime.combine(day, time(hour, minute)), timezone.get_current_timezone())


# --------------------------------------------------------------------------- streaks & rest days
def test_rest_days_keep_but_do_not_extend_streak(student):
    today = timezone.localdate()
    for d in (0, 2, 3):
        DailyActivity.objects.create(user=student, date=today - timedelta(days=d), seconds=600)
    assert motivation.learning_streak(student, today) == 1  # gap yesterday breaks it
    RestDay.objects.create(user=student, date=today - timedelta(days=1))
    assert motivation.learning_streak(student, today) == 3  # rest day bridges, not counted


def test_resting_today_keeps_yesterdays_streak(student):
    today = timezone.localdate()
    DailyActivity.objects.create(user=student, date=today - timedelta(days=1), seconds=600)
    RestDay.objects.create(user=student, date=today)
    assert motivation.learning_streak(student, today) == 1


def test_dashboard_streak_wrapper_uses_rest_days(student):
    from apps.dashboard.views import learning_streak

    today = timezone.localdate()
    DailyActivity.objects.create(user=student, date=today, seconds=600)
    DailyActivity.objects.create(user=student, date=today - timedelta(days=2), seconds=600)
    RestDay.objects.create(user=student, date=today - timedelta(days=1))
    assert learning_streak(student, today) == 2


def test_can_rest_rules(student):
    today = timezone.localdate()
    assert motivation.can_rest(student, today - timedelta(days=1))[0] is False
    assert motivation.can_rest(student, today + timedelta(days=90))[0] is False
    assert motivation.can_rest(student, today)[0] is True
    RestDay.objects.create(user=student, date=today)
    same_week = today + timedelta(days=1) if today.weekday() < 6 else today - timedelta(days=1)
    if same_week >= today:
        allowed, reason = motivation.can_rest(student, same_week)
        assert not allowed and "already" in reason
    assert motivation.can_rest(student, today + timedelta(days=7))[0] is True


def test_rest_day_view_toggles(client, student):
    client.force_login(student)
    today = timezone.localdate()
    client.post(reverse("learning:rest_day"), {"date": today.isoformat()})
    assert RestDay.objects.filter(user=student, date=today).exists()
    html = client.get(reverse("learning:planner")).content.decode()
    assert "Today is a rest day" in html
    client.post(reverse("learning:rest_day"), {"date": today.isoformat()})
    assert not RestDay.objects.exists()
    client.post(reverse("learning:rest_day"), {"date": (today - timedelta(days=3)).isoformat()})
    assert not RestDay.objects.exists()


# --------------------------------------------------------------------------- exam countdown
def test_exam_countdown_pace_and_buffer():
    today = date(2026, 11, 4)
    info = motivation.exam_countdown(today + timedelta(days=84), done=10, total=80, recent_completed=14, today=today)
    assert info["days_left"] == 84 and info["buffer_days"] == 14
    assert info["target_date"] == today + timedelta(days=70)
    assert info["remaining"] == 70 and info["per_day"] == 1.0 and info["per_week"] == 7
    assert info["on_track"] is True  # 1 lesson/day recently
    behind = motivation.exam_countdown(today + timedelta(days=84), 10, 80, recent_completed=2, today=today)
    assert behind["on_track"] is False
    short = motivation.exam_countdown(today + timedelta(days=10), 0, 5, 0, today)
    assert short["buffer_days"] == 0 and short["per_day"] == 0.5
    assert motivation.exam_countdown(today - timedelta(days=1), 0, 5, 0, today)["past"] is True
    assert motivation.exam_countdown(today, 0, 5, 0, today)["is_today"] is True
    assert motivation.exam_countdown(None, 0, 5, 0, today) is None
    done = motivation.exam_countdown(today + timedelta(days=60), 5, 5, 0, today)
    assert done["finished"] and done["on_track"] and done["per_week"] == 0


def test_set_exam_date_and_see_countdown(client, student, plan):
    client.force_login(student)
    html = client.get(reverse("dashboard:home")).content.decode()
    assert "Add your GCE exam date" not in html  # a new student is not nagged yet (see dashboard.modes)
    exam = timezone.localdate() + timedelta(days=100)
    client.post(reverse("learning:exam_date"), {"exam_date": exam.isoformat()})
    student.profile.refresh_from_db()
    assert student.profile.exam_date == exam
    planner = client.get(reverse("learning:planner"))
    assert planner.context["countdown"]["days_left"] == 100
    assert planner.context["countdown"]["remaining"] == 3
    assert "100</span>" in planner.content.decode()
    dash = client.get(reverse("dashboard:home"))
    assert dash.context["countdown"]["remaining"] == 3
    assert "days to your GCE exams" in dash.content.decode()


def test_exam_date_validation_and_removal(client, student):
    client.force_login(student)
    client.post(reverse("learning:exam_date"), {"exam_date": (timezone.localdate() - timedelta(days=1)).isoformat()})
    student.profile.refresh_from_db()
    assert student.profile.exam_date is None
    client.post(reverse("learning:exam_date"), {"exam_date": (timezone.localdate() + timedelta(days=5000)).isoformat()})
    student.profile.refresh_from_db()
    assert student.profile.exam_date is None
    student.profile.exam_date = timezone.localdate() + timedelta(days=30)
    student.profile.save()
    client.post(reverse("learning:exam_date"), {"exam_date": ""})
    student.profile.refresh_from_db()
    assert student.profile.exam_date is None


# --------------------------------------------------------------------------- recurring sessions & editing
def test_recurrence_dates():
    wed = date(2026, 11, 4)  # a Wednesday
    dates = motivation.recurrence_dates(wed, [0, 2, 4], weeks=2)
    assert dates == [date(2026, 11, 4), date(2026, 11, 6), date(2026, 11, 9), date(2026, 11, 11), date(2026, 11, 13)]
    assert len(motivation.recurrence_dates(wed, range(7), 20)) <= motivation.MAX_SERIES


def test_create_recurring_series(client, student):
    client.force_login(student)
    start = timezone.localdate() + timedelta(days=1)
    start = start + timedelta(days=(7 - start.weekday()) % 7)  # next Monday
    client.post(reverse("learning:session_create"), {
        "title": "Maths practice", "kind": "practice", "date": start.isoformat(), "start_time": "17:00",
        "duration_minutes": 45, "repeat_days": ["0", "2", "4"], "repeat_weeks": 3})
    sessions = list(StudySession.objects.filter(user=student))
    assert len(sessions) == 9
    assert len({s.series for s in sessions}) == 1 and sessions[0].series is not None
    assert {timezone.localtime(s.starts_at).weekday() for s in sessions} == {0, 2, 4}
    assert all(timezone.localtime(s.starts_at).strftime("%H:%M") == "17:00" for s in sessions)


def test_single_session_has_no_series(client, student):
    client.force_login(student)
    client.post(reverse("learning:session_create"), {
        "title": "One-off", "kind": "study", "date": timezone.localdate().isoformat(), "start_time": "18:00",
        "duration_minutes": 30, "repeat_weeks": 4})
    assert StudySession.objects.get(user=student).series is None


def test_repeat_needs_weeks(client, student):
    client.force_login(student)
    client.post(reverse("learning:session_create"), {
        "title": "X", "kind": "study", "date": timezone.localdate().isoformat(), "start_time": "18:00",
        "duration_minutes": 30, "repeat_days": ["1"]})
    assert not StudySession.objects.exists()


def _series(student, n=4):
    import uuid

    series = uuid.uuid4()
    first = timezone.localdate() + timedelta(days=1)
    return [StudySession.objects.create(user=student, title="Physics", series=series, duration_minutes=30,
                                        starts_at=at(first + timedelta(weeks=i))) for i in range(n)]


def test_edit_single_session(client, student):
    s = StudySession.objects.create(user=student, title="Old", starts_at=at(timezone.localdate() + timedelta(days=2)))
    client.force_login(student)
    page = client.get(reverse("learning:session_edit", args=[s.pk]))
    assert page.status_code == 200 and "Apply changes to" not in page.content.decode()
    new_day = timezone.localdate() + timedelta(days=3)
    client.post(reverse("learning:session_edit", args=[s.pk]), {
        "title": "New", "kind": "revision", "date": new_day.isoformat(), "start_time": "19:15", "duration_minutes": 60})
    s.refresh_from_db()
    assert s.title == "New" and s.kind == "revision" and s.duration_minutes == 60
    assert timezone.localtime(s.starts_at) == timezone.localtime(at(new_day, 19, 15))


def test_edit_this_and_future_in_series(client, student):
    sessions = _series(student)
    client.force_login(student)
    assert "Apply changes to" in client.get(reverse("learning:session_edit", args=[sessions[1].pk])).content.decode()
    day = timezone.localtime(sessions[1].starts_at).date()
    client.post(reverse("learning:session_edit", args=[sessions[1].pk]), {
        "title": "Physics past papers", "kind": "practice", "date": day.isoformat(), "start_time": "16:30",
        "duration_minutes": 50, "scope": "future"})
    for s in sessions:
        s.refresh_from_db()
    assert sessions[0].title == "Physics" and timezone.localtime(sessions[0].starts_at).hour == 17
    for s, i in zip(sessions[1:], range(1, 4)):
        local = timezone.localtime(s.starts_at)
        assert s.title == "Physics past papers" and s.duration_minutes == 50
        assert local.strftime("%H:%M") == "16:30"
        assert local.date() == timezone.localdate() + timedelta(days=1, weeks=i)  # dates kept


def test_edit_only_this_in_series(client, student):
    sessions = _series(student, 3)
    client.force_login(student)
    day = timezone.localtime(sessions[0].starts_at).date()
    client.post(reverse("learning:session_edit", args=[sessions[0].pk]), {
        "title": "Changed", "kind": "study", "date": day.isoformat(), "start_time": "17:00",
        "duration_minutes": 30, "scope": "one"})
    titles = list(StudySession.objects.order_by("starts_at").values_list("title", flat=True))
    assert titles == ["Changed", "Physics", "Physics"]


def test_edit_and_delete_series_only_own(client, student):
    other = User.objects.create_user(email="o@example.com", password="pw-Strong-123")
    theirs = StudySession.objects.create(user=other, title="T", starts_at=timezone.now())
    client.force_login(student)
    assert client.get(reverse("learning:session_edit", args=[theirs.pk])).status_code == 404
    sessions = _series(student)
    client.post(reverse("learning:session_delete", args=[sessions[2].pk]), {"scope": "future"})
    assert list(StudySession.objects.filter(user=student).order_by("starts_at")) == sessions[:2]
    assert StudySession.objects.filter(pk=theirs.pk).exists()


def test_planner_shows_edit_and_series_controls(client, student):
    sessions = _series(student, 2)
    client.force_login(student)
    day = timezone.localtime(sessions[0].starts_at).date()
    html = client.get(reverse("learning:planner"), {"date": day.isoformat()}).content.decode()
    assert reverse("learning:session_edit", args=[sessions[0].pk]) in html
    assert "Delete this and later sessions" in html
    assert "Repeat every week" in html


# --------------------------------------------------------------------------- calendar feed
def test_calendar_feed_lifecycle(client, student):
    s = StudySession.objects.create(user=student, title="Chemistry, moles; revision", kind="revision",
                                    starts_at=timezone.now() + timedelta(days=1), duration_minutes=45)
    other = User.objects.create_user(email="x@example.com", password="pw-Strong-123")
    StudySession.objects.create(user=other, title="Someone else", starts_at=timezone.now() + timedelta(days=1))
    student.profile.exam_date = timezone.localdate() + timedelta(days=90)
    student.profile.save()
    client.force_login(student)
    assert "Create my calendar link" in client.get(reverse("learning:planner")).content.decode()
    client.post(reverse("learning:private_link", args=["calendar"]))
    link = PrivateLink.objects.get(user=student, purpose=LinkPurpose.CALENDAR)
    assert len(link.token) >= 40
    planner = client.get(reverse("learning:planner")).content.decode()
    assert link.token in planner and "webcal://" in planner

    client.logout()  # calendar apps fetch without a session
    url = reverse("learning:calendar_feed", args=[link.token])
    response = client.get(url)
    body = response.content.decode()
    assert response.status_code == 200 and response["Content-Type"].startswith("text/calendar")
    assert response["Cache-Control"] == "private, no-store"
    assert body.startswith("BEGIN:VCALENDAR\r\n") and body.endswith("END:VCALENDAR\r\n")
    assert f"UID:session-{s.pk}@" in body and "SUMMARY:Chemistry\\, moles\\; revision" in body
    assert "BEGIN:VALARM" in body and "TRIGGER:-PT15M" in body
    assert "SUMMARY:GCE exams begin" in body
    assert "Someone else" not in body
    link.refresh_from_db()
    assert link.last_used_at is not None

    client.force_login(student)
    client.post(reverse("learning:private_link", args=["calendar"]))  # rotate
    new = PrivateLink.objects.get(user=student, purpose=LinkPurpose.CALENDAR)
    assert new.token != link.token
    assert client.get(url).status_code == 404
    client.post(reverse("learning:private_link", args=["calendar"]), {"action": "revoke"})
    assert client.get(reverse("learning:calendar_feed", args=[new.token])).status_code == 404
    assert client.get(reverse("learning:calendar_feed", args=["nope"])).status_code == 404


def test_private_link_rejects_unknown_purpose_and_get(client, student):
    client.force_login(student)
    assert client.post(reverse("learning:private_link", args=["bogus"])).status_code == 404
    assert client.get(reverse("learning:private_link", args=["calendar"])).status_code == 405


def test_ics_folding_and_escaping():
    assert motivation._ics_escape("a,b;c\\d\ne") == "a\\,b\\;c\\\\d\\ne"
    folded = motivation._fold("SUMMARY:" + "é" * 80)
    lines = folded.split("\r\n")
    assert len(lines) > 1 and all(len(line.encode()) <= 75 for line in lines)
    assert all(line.startswith(" ") for line in lines[1:])
    assert "".join(line[1:] if i else line for i, line in enumerate(lines)) == "SUMMARY:" + "é" * 80


def test_completed_sessions_have_no_alarm(student):
    s = StudySession.objects.create(user=student, title="Done", starts_at=timezone.now() + timedelta(hours=2),
                                    completed_at=timezone.now())
    body = motivation.build_ics([s], host="example.com")
    assert "VALARM" not in body and "X-GCE-COMPLETED:TRUE" in body


# --------------------------------------------------------------------------- weekly summary & parent report
def test_weekly_summary_numbers(student, plan):
    today = timezone.localdate()
    monday = motivation.week_start(today)
    DailyActivity.objects.create(user=student, date=monday, seconds=50 * 60)
    DailyActivity.objects.create(user=student, date=monday - timedelta(days=7), seconds=20 * 60)
    StudySession.objects.create(user=student, title="Done", starts_at=at(monday), completed_at=timezone.now())
    StudySession.objects.create(user=student, title="Missed", starts_at=at(monday, 18))
    summary = motivation.weekly_summary(student, student.profile, monday, today)
    assert summary["total_minutes"] == 50 and summary["delta_minutes"] == 30
    assert summary["active_days"] == 1 and summary["goal_days"] == 1  # default goal 45
    assert summary["sessions_planned"] == 2 and summary["sessions_done"] == 1
    assert len(summary["lessons"]) == 1 and summary["is_current"]


def test_parse_week_clamps():
    today = date(2026, 11, 4)
    assert motivation.parse_week("", today) == date(2026, 11, 2)
    assert motivation.parse_week("2030-01-01", today) == date(2026, 11, 2)
    assert motivation.parse_week("2020-01-01", today, earliest_weeks=8) == date(2026, 9, 7)
    assert motivation.parse_week("2026-10-28", today) == date(2026, 10, 26)


def test_weekly_page_and_parent_report(client, student, plan):
    DailyActivity.objects.create(user=student, date=timezone.localdate(), seconds=30 * 60)
    client.force_login(student)
    page = client.get(reverse("learning:weekly"))
    assert page.status_code == 200 and "Create a report link" in page.content.decode()
    assert "Weekly summary" in client.get(reverse("learning:progress")).content.decode()
    client.post(reverse("learning:private_link", args=["report"]))
    link = PrivateLink.objects.get(user=student, purpose=LinkPurpose.REPORT)
    assert link.token in client.get(reverse("learning:weekly")).content.decode()

    client.logout()
    report = client.get(reverse("learning:report", args=[link.token]))
    html = report.content.decode()
    assert report.status_code == 200 and "Mia’s week" in html
    assert report["X-Robots-Tag"] == "noindex, nofollow" and report["Referrer-Policy"] == "no-referrer"
    assert "m@example.com" not in html  # no email on the shared page
    assert plan[0].title in html and "30 min" in html
    last_week = (motivation.week_start(timezone.localdate()) - timedelta(weeks=1)).isoformat()
    assert client.get(reverse("learning:report", args=[link.token]), {"week": last_week}).status_code == 200

    client.force_login(student)
    client.post(reverse("learning:private_link", args=["report"]), {"action": "revoke"})
    client.logout()
    assert client.get(reverse("learning:report", args=[link.token])).status_code == 404


def test_report_hidden_for_inactive_user(client, student):
    link = PrivateLink.issue(student, LinkPurpose.REPORT)
    student.is_active = False
    student.save()
    assert client.get(reverse("learning:report", args=[link.token])).status_code == 404


# --------------------------------------------------------------------------- goal suggestions
def _days(student, minutes_list):
    today = timezone.localdate()
    for i, m in enumerate(minutes_list):
        DailyActivity.objects.create(user=student, date=today - timedelta(days=i), seconds=m * 60)


def test_goal_suggestion_up(student):
    _days(student, [120] * 13)
    s = motivation.goal_suggestion(student, 45, timezone.localdate())
    assert s["direction"] == "up" and s["minutes"] == 55
    assert motivation.goal_suggestion(student, 115, timezone.localdate()) is None  # never nudged above 2h


def test_goal_suggestion_down_and_none(student):
    _days(student, [10, 12, 8, 50, 9])
    s = motivation.goal_suggestion(student, 45, timezone.localdate())
    assert s["direction"] == "down" and s["minutes"] == 35
    assert motivation.goal_suggestion(student, 10, timezone.localdate()) is None


def test_no_suggestion_for_new_student(student):
    assert motivation.goal_suggestion(student, 45, timezone.localdate()) is None


def test_goal_adjust_view(client, student):
    _days(student, [50] * 14)
    client.force_login(student)
    assert "Set goal to 55 min" in client.get(reverse("learning:weekly")).content.decode()
    client.post(reverse("learning:goal_adjust"), {"minutes": 400})  # client value ignored
    student.profile.refresh_from_db()
    assert student.profile.daily_goal_minutes == 55
