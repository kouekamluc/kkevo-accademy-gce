from apps.dashboard import modes


def test_kind_follows_what_the_student_has_done():
    assert modes.student_mode(started=False, days_to_exam=30) == modes.NEW  # exam date alone is not enough
    assert modes.student_mode(started=True) == modes.ACTIVE
    assert modes.student_mode(started=True, days_to_exam=200) == modes.ACTIVE
    assert modes.student_mode(started=True, days_to_exam=90) == modes.EXAM
    assert modes.student_mode(started=True, days_to_exam=-1) == modes.ACTIVE  # exam already past


def test_new_student_sees_no_empty_blocks():
    show = modes.dashboard_blocks(modes.NEW)
    assert not any(show[k] for k in ("streak", "recommended", "overall", "activity", "revision", "recent"))


def test_blocks_without_content_are_left_out():
    show = modes.dashboard_blocks(modes.ACTIVE, completed=5, week_minutes=0, has_recent=False)
    assert not show["activity"] and not show["recent"] and not show["revision"]
    assert show["overall"] and show["recommended"]
    assert modes.dashboard_blocks(modes.ACTIVE, reviews_due=2)["revision"]


def test_exam_prompt_waits_until_the_student_has_a_few_lessons_behind_them():
    assert not modes.dashboard_blocks(modes.ACTIVE, completed=1)["exam_prompt"]
    assert modes.dashboard_blocks(modes.ACTIVE, completed=3)["exam_prompt"]
    assert not modes.dashboard_blocks(modes.ACTIVE, completed=9, has_exam_date=True)["exam_prompt"]


def test_away_hides_streak_after_a_week():
    assert modes.dashboard_blocks(modes.ACTIVE, away_days=6)["streak"]
    assert not modes.dashboard_blocks(modes.ACTIVE, away_days=7)["streak"]


def test_lower_sixth_is_not_pushed_towards_an_exam_that_is_a_year_away():
    assert modes.student_mode(started=True, days_to_exam=30, exam_year=False) == modes.ACTIVE
    assert not modes.dashboard_blocks(modes.ACTIVE, completed=9, exam_year=False)["exam_prompt"]
    assert "next year" in modes.subtitle(modes.ACTIVE, away=False, exam_level="A", exam_year=False)


def test_subtitle_speaks_to_o_level_and_a_level_differently():
    o = modes.subtitle(modes.ACTIVE, away=False, exam_level="O")
    a = modes.subtitle(modes.ACTIVE, away=False, exam_level="A")
    assert o != a and "base" in o and "deep" in a
