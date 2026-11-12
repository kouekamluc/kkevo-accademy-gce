"""The content loaders refresh PostgreSQL's planner statistics so big loads do not plan joins from guesses."""

from django.core.management import call_command
from django.db import connection

from apps.core.db import refresh_planner_statistics


def _estimated_rows(table):
    with connection.cursor() as cursor:
        cursor.execute("SELECT reltuples FROM pg_class WHERE relname = %s", [table])
        return cursor.fetchone()[0]


def test_loading_content_leaves_planner_statistics_in_place(db):
    call_command("load_gce_curriculum")
    call_command("load_lessons", "--only", "history:lower-sixth")
    call_command("load_practice", "--only", "history:lower-sixth")
    # reltuples is -1 (or 0) until a table has been analysed
    assert _estimated_rows("practice_question") > 0
    assert _estimated_rows("practice_practiceset") > 0


def test_refreshing_statistics_is_harmless_to_call_twice(db):
    refresh_planner_statistics()
    refresh_planner_statistics()
