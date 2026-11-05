"""Draft practice sets for the GCE course outlines, loaded by `python manage.py load_practice`.

Each module here (except `dsl`) is one file:

    from .dsl import *
    COURSE = ("mathematics", "form-5")        # same keys as apps/courses/lesson_content
    SETS = [practice_set(module=..., topic=..., title=..., lesson="<lesson slug>", questions=[...]), ...]

Sets load as drafts: staff check and publish them. See docs/curriculum/LESSON_AUTHORING.md.
"""

import importlib
import pkgutil

from apps.courses import lesson_content
from apps.practice.models import Choice, PracticeSet, Question

SKIP_MODULES = {"dsl"}
MIN_QUESTIONS = 3


def content_modules(names=None):
    names = sorted(names or (m.name for m in pkgutil.iter_modules(__path__) if m.name not in SKIP_MODULES))
    return [(name, importlib.import_module(f"{__name__}.{name}")) for name in names]


def collect(names=None):
    """[(course key, set spec, source file name)]."""
    rows = []
    for name, module in content_modules(names):
        for key in lesson_content.course_keys(module):
            for spec in getattr(module, "SETS", []):
                rows.append((key, spec, name))
    return rows


def _limit(model, field):
    return model._meta.get_field(field).max_length


def _question_problems(q):
    problems = []
    if lesson_content.control_characters(q):
        problems.append('contains a control character: LaTeX such as \\text or \\frac needs a raw string r"..."')
    for field in ("concept", "skill", "feedback"):
        if len(q.get(field) or "") > _limit(Question, field):
            problems.append(f"{field} is longer than {_limit(Question, field)} characters")
    if not (q.get("prompt") or "").strip():
        problems.append("no prompt")
    if not q.get("steps"):
        problems.append("no worked solution steps")
    if q.get("prompt", "").count("$") % 2:
        problems.append("odd number of $ in the prompt")
    if q.get("kind") == "choice":
        choices = q.get("choices") or []
        if not 2 <= len(choices) <= 6:
            problems.append("needs 2 to 6 choices")
        if sum(1 for c in choices if c.get("correct")) != 1:
            problems.append("needs exactly one correct choice")
        for c in choices:
            if len(c.get("text") or "") > _limit(Choice, "text") or len(c.get("why") or "") > _limit(Choice, "why_wrong"):
                problems.append("a choice or its explanation is longer than 300 characters")
            if not c.get("correct") and not c.get("why"):
                problems.append(f"wrong choice '{c.get('text', '')[:30]}' has no explanation")
        if len({c.get("text") for c in choices}) != len(choices):
            problems.append("two choices have the same text")
    elif q.get("kind") == "numeric":
        if not isinstance(q.get("answer"), (int, float)):
            problems.append("numeric question needs a number as its answer")
        if not isinstance(q.get("tolerance"), (int, float)) or q["tolerance"] < 0:
            problems.append("tolerance must be a number of 0 or more")
        if len(q.get("unit") or "") > _limit(Question, "unit"):
            problems.append("unit is too long")
    else:
        problems.append(f"unknown question kind '{q.get('kind')}'")
    return problems


def validate(rows=None):
    rows = collect() if rows is None else rows
    lessons = {(k, s["slug"]): (s["module"], s["topic"]) for k, s, _ in lesson_content.collect()}
    errors, seen = [], set()
    for key, spec, source in rows:
        where = f"{source}: set '{spec.get('title', '?')}'"
        if key not in lesson_content.gce_curriculum.SYLLABI:
            errors.append(f"{where}: no syllabus outline for {key}.")
            continue
        topics = lesson_content.outline(key, include_exam=True)
        module, topic = spec.get("module"), spec.get("topic")
        if module not in topics or topic not in topics.get(module, []):
            errors.append(f"{where}: '{module}' / '{topic}' is not a topic of the {key} outline.")
        if not spec.get("title") or len(spec["title"]) > _limit(PracticeSet, "title"):
            errors.append(f"{where}: title missing or longer than 200 characters.")
        if (key, module, topic, spec.get("title")) in seen:
            errors.append(f"{where}: the same title is used twice for this topic.")
        seen.add((key, module, topic, spec.get("title")))
        if spec.get("lesson") and lessons.get((key, spec["lesson"])) != (module, topic):
            errors.append(f"{where}: lesson '{spec['lesson']}' is not a lesson of this topic.")
        limit = spec.get("time_limit_minutes")
        if limit is not None and (not isinstance(limit, int) or not 5 <= limit <= 300):
            errors.append(f"{where}: time_limit_minutes must be a whole number from 5 to 300.")
        questions = spec.get("questions") or []
        if len(questions) < MIN_QUESTIONS:
            errors.append(f"{where}: needs at least {MIN_QUESTIONS} questions.")
        for n, q in enumerate(questions, 1):
            errors += [f"{where}, question {n}: {p}" for p in _question_problems(q)]
    return errors
