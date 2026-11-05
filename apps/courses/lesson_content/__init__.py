"""Draft lesson content for the GCE course outlines, loaded by `python manage.py load_lessons`.

Each module in this package (except `dsl`) is one content file:

    from .dsl import *
    COURSE = ("mathematics", "form-5")        # (subject slug, level slug) from gce_curriculum.py
    # or COURSE = [("pure-mathematics-with-mechanics", "lower-sixth"), (...)] for shared content
    LESSONS = [lesson(module=..., topic=..., ...), ...]

A course may be split across several files. `module` and `topic` must match a section and item
of the syllabus outline in apps/academics/gce_curriculum.py exactly.

This is KKEVO draft teaching material written against KKEVO's curriculum summary, not the
official GCE Board text. Lessons load as drafts: a reviewer checks each one against the
official syllabus in the studio before publishing.
"""

import importlib
import pkgutil
import re

from django.core.exceptions import ValidationError

from apps.academics import gce_curriculum

SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LIMITS = {"title": 200, "slug": 200, "summary": 300}
SKIP_MODULES = {"dsl"}


def content_modules(names=None):
    """Import the content files in this package (all of them by default), sorted by name."""
    names = sorted(names or (m.name for m in pkgutil.iter_modules(__path__) if m.name not in SKIP_MODULES))
    return [(name, importlib.import_module(f"{__name__}.{name}")) for name in names]


def course_keys(module):
    course = getattr(module, "COURSE", None)
    if isinstance(course, tuple):
        return [course]
    return list(course or [])


def collect(names=None):
    """[(course key, lesson spec, source file name)] for every lesson in the content files."""
    rows = []
    for name, module in content_modules(names):
        for key in course_keys(module):
            for spec in getattr(module, "LESSONS", []):
                rows.append((key, spec, name))
    return rows


def outline(key):
    """{module title: [topic titles]} for a course key, skipping the Examination section."""
    sections = gce_curriculum.SYLLABI[key][2]
    return {s: [i[0] for i in items] for s, items in sections if s != "Examination"}


def _block_problems(block):
    from apps.courses.models import LessonBlock

    problems = []
    data = block.get("data") or {}
    obj = LessonBlock(block_type=block.get("block_type", ""), title=block.get("title", ""),
                      body=block.get("body", ""), alt_text=block.get("alt_text", ""), data=data)
    try:
        obj.clean_fields(exclude=["lesson", "order", "media_url"])
        obj.clean()
    except ValidationError as error:
        problems += [m for msgs in error.message_dict.values() for m in msgs]
    kind = obj.block_type
    if kind == "heading" and not obj.title:
        problems.append("heading has no title")
    if kind == "quiz":
        choices, correct = data.get("choices", []), data.get("correct")
        if len(choices) < 2:
            problems.append("quiz needs at least 2 choices")
        if not isinstance(correct, int) or not 0 <= correct < len(choices):
            problems.append("quiz 'correct' is not a valid choice index")
        if data.get("feedback") and len(data["feedback"]) != len(choices):
            problems.append("quiz feedback must have one line per choice")
        if not data.get("explanation"):
            problems.append("quiz has no explanation")
    if kind == "practice" and not data.get("answer"):
        problems.append("practice question has no answer")
    if kind == "worked_example" and not obj.body and not data.get("intro"):
        problems.append("worked example has neither an equation (solve) nor an intro")
    if len(obj.title) > 200:
        problems.append("block title is longer than 200 characters")
    return problems


def validate(rows=None):
    """Readable problems with the content files (empty list when everything is fine)."""
    rows = collect() if rows is None else rows
    errors, seen = [], set()
    for key, spec, source in rows:
        where = f"{source}: lesson '{spec.get('slug', '?')}'"
        if key not in gce_curriculum.SYLLABI:
            errors.append(f"{where}: no syllabus outline for {key}.")
            continue
        topics = outline(key)
        module, topic = spec.get("module"), spec.get("topic")
        if module not in topics:
            errors.append(f"{where}: module '{module}' is not in the {key} outline ({', '.join(topics)}).")
        elif topic not in topics[module]:
            errors.append(f"{where}: topic '{topic}' is not in module '{module}' ({', '.join(topics[module])}).")
        slug = spec.get("slug", "")
        if not SLUG.match(slug):
            errors.append(f"{where}: slug must be lowercase words joined by hyphens.")
        if (key, slug) in seen:
            errors.append(f"{where}: slug used twice in {key}.")
        seen.add((key, slug))
        for field, limit in LIMITS.items():
            if len(spec.get(field) or "") > limit:
                errors.append(f"{where}: {field} is longer than {limit} characters.")
        if not spec.get("title"):
            errors.append(f"{where}: no title.")
        if not isinstance(spec.get("minutes"), int) or not 1 <= spec["minutes"] <= 120:
            errors.append(f"{where}: minutes must be a whole number from 1 to 120.")
        if not spec.get("objectives"):
            errors.append(f"{where}: no learning objectives.")
        blocks = spec.get("blocks") or []
        if not blocks:
            errors.append(f"{where}: no blocks.")
        for n, block in enumerate(blocks, 1):
            for problem in _block_problems(block):
                errors.append(f"{where}, block {n} ({block.get('block_type')}): {problem}")
    return errors
