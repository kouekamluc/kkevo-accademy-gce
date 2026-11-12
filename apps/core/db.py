"""Database helpers shared by the content loaders."""

from django.db import connection


def refresh_planner_statistics():
    """Update PostgreSQL's table statistics (ANALYZE) after a bulk content load.

    A freshly loaded library holds tens of thousands of questions. Until PostgreSQL has statistics for those
    tables it plans joins from default guesses, and a plain count over the review-card tables can then take
    many minutes (it did, in a test database, where autovacuum cannot see rows loaded inside a test's
    transaction). Running ANALYZE once after the load keeps those plans sane, in tests and on a real
    deployment. It is allowed inside a transaction and does nothing on other databases.
    """
    if connection.vendor != "postgresql":
        return
    with connection.cursor() as cursor:
        cursor.execute("ANALYZE")
