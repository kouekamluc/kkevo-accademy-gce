"""Which kind of student is looking at the dashboard, and so which blocks to show.

A dashboard that shows everything to everyone buries a new student under empty charts and
gives an exam candidate the same layout as someone browsing. The kind is worked out from
what the student has actually done, never asked for:

* ``new``    — has not started a lesson yet. One job: start the first lesson.
* ``exam``   — has an exam date within ``EXAM_WINDOW_DAYS``. Countdown, practice and
               mistake review come first.
* ``active`` — everyone else who is learning.

The exam level matters too. O Level students (Form 5) take many subjects and need a solid
base in each; A Level students take few and go deep, and a Lower Sixth student does not sit
the exam until next year, so exam countdowns and prompts are for the exam year only
(Form 5 and Upper Sixth).

On top of the kind, a block with nothing to show is simply left out (an empty weekly chart,
an empty "recently completed" list), and a student who has been away for ``AWAY_DAYS`` or
more gets a welcome back instead of a broken streak and a row of empty bars.

This module has no database access, so the rules are easy to read and to test.
"""

NEW = "new"
EXAM = "exam"
ACTIVE = "active"

EXAM_WINDOW_DAYS = 90
AWAY_DAYS = 7
# Subjects listed on the dashboard; the rest are one tap away on "My subjects".
SUBJECTS_SHOWN = 6
# Lessons finished before the dashboard starts asking for an exam date.
EXAM_PROMPT_AFTER = 3


def student_mode(*, started, days_to_exam=None, exam_year=True):
    """``started``: has any lesson progress. ``days_to_exam``: days until the first paper, if set.
    ``exam_year``: the student sits the exam this school year (not Lower Sixth)."""
    if not started:
        return NEW
    if exam_year and days_to_exam is not None and 0 <= days_to_exam <= EXAM_WINDOW_DAYS:
        return EXAM
    return ACTIVE


def dashboard_blocks(mode, *, completed=0, week_minutes=0, has_upcoming=False, reviews_due=0,
                     has_recent=False, away_days=None, has_exam_date=False, exam_year=True):
    """Which dashboard blocks to show, as a dict of booleans for the template."""
    away = away_days is not None and away_days >= AWAY_DAYS
    new = mode == NEW
    return {
        "mode": mode,
        "is_new": new,
        "mood": "cheer" if mode == EXAM else "sleepy" if away else "happy",
        "away": away,
        "streak": not new and not away,
        "exam_prompt": exam_year and not has_exam_date and completed >= EXAM_PROMPT_AFTER,
        "recommended": not new,
        "overall": not new,
        "activity": not new and week_minutes > 0,
        # Revision is the heart of exam preparation, so it stays visible there even when empty.
        "revision": mode == EXAM or bool(has_upcoming or reviews_due),
        "recent": not new and has_recent,
    }


def subtitle(mode, *, away, exam_level="", exam_year=True):
    if mode == NEW:
        return "Pick a lesson and start. Everything else appears as you go."
    if away:
        return "Welcome back. Pick up where you left off."
    if mode == EXAM:
        return "Your exam is getting closer. Keep a steady pace."
    if exam_level == "A":
        return ("Go deep on each topic, then test yourself with practice questions." if exam_year
                else "Your exam is next year. Build a thorough understanding now.")
    if exam_level == "O":
        return "A strong base in every subject makes exam year easier."
    return "Every lesson you complete brings you closer to your goals."
