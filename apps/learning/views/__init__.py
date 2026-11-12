"""Student learning pages: progress, planner, weekly summary, saved lessons.

Split by topic into modules; every name is re-exported here so `from . import views` keeps working.
"""

from ._common import (  # noqa: F401
    WEEKDAYS,
    _plan,
    _safe_next,
    fmt_minutes,
)
from .reportcard import report_card  # noqa: F401
from .progress import (  # noqa: F401
    _sparkline,
    _suggestions,
    add_suggestions,
    progress,
)
from .planner import (  # noqa: F401
    ExamDateForm,
    SUBJECT_COLOURS,
    SessionForm,
    _countdown,
    _form_errors,
    _planner_at,
    exam_date,
    plan_week,
    planner,
    rest_day,
    session_create,
    session_delete,
    session_edit,
    session_reschedule,
    session_toggle,
    week_clear,
)
from .links import (  # noqa: F401
    _link_url,
    _private_headers,
    calendar_feed,
    private_link,
)
from .reports import (  # noqa: F401
    REPORT_WEEKS,
    _weekly_context,
    goal_adjust,
    report,
    weekly,
)
from .saved import (  # noqa: F401
    saved,
)
