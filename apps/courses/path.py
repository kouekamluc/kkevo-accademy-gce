"""Path view of a course: modules as sections, topics as steps, one clear "continue here".

All figures reuse apps.learning.services (published lessons only, same Stat maths and the same
"next lesson" rule as the course page) and apps.practice.mastery (topic levels). The number of
queries is fixed: it does not grow with the number of modules, topics or lessons.
"""

from django.db.models import Count

from apps.learning import services
from apps.practice.mastery import NOT_STARTED, topic_mastery
from apps.practice.models import PracticeSet

DONE, PROGRESS, TODO = "done", "progress", "todo"
STATE_LABELS = {DONE: "Done", PROGRESS: "In progress", TODO: "Not started"}


def _practice_by_topic(course):
    """{topic_id: first published, non-mock practice set that has questions}."""
    sets = (
        PracticeSet.objects.published()
        .filter(topic__module__course=course, is_mock=False)
        .annotate(question_count=Count("questions"))
        .filter(question_count__gt=0)
        .order_by("order", "pk")
    )
    found = {}
    for practice_set in sets:
        found.setdefault(practice_set.topic_id, practice_set)
    return found


def _state(done, total, touched):
    if total and done >= total:
        return DONE
    return PROGRESS if done or touched else TODO


def build_path(user, course):
    """Context for the path page. Topics or modules without a published lesson are left out."""
    lessons = list(
        services.published_lessons()
        .filter(topic__module__course=course)
        .select_related("topic__module__course")
        .order_by("topic__module__order", "topic__module__pk", "topic__order", "topic__pk", "order", "pk")
    )
    progress = services.progress_by_lesson(user, lessons)
    next_lesson, _ = services.next_lesson(user, course)
    if next_lesson is not None:  # next_lesson() falls back to the first lesson when all are done
        record = progress.get(next_lesson.pk)
        if record is not None and record.is_completed:
            next_lesson = None
    practice = _practice_by_topic(course)
    mastery = topic_mastery(user)

    modules, module_by_pk, step_by_pk = [], {}, {}
    for lesson in lessons:
        topic, module = lesson.topic, lesson.topic.module
        if module.pk not in module_by_pk:
            module_by_pk[module.pk] = {"module": module, "steps": [], "number": len(modules) + 1}
            modules.append(module_by_pk[module.pk])
        if topic.pk not in step_by_pk:
            owner = module_by_pk[module.pk]
            step_by_pk[topic.pk] = {
                "topic": topic, "number": f"{owner['number']}.{len(owner['steps']) + 1}", "lessons": [],
                "practice_set": practice.get(topic.pk), "mastery": mastery.get(topic.pk, NOT_STARTED),
            }
            owner["steps"].append(step_by_pk[topic.pk])
        record = progress.get(lesson.pk)
        lesson_state = DONE if record and record.is_completed else PROGRESS if record else TODO
        step_by_pk[topic.pk]["lessons"].append({
            "lesson": lesson, "progress": record, "state": lesson_state,
            "is_next": next_lesson is not None and lesson.pk == next_lesson.pk,
        })

    current_step = None
    course_stat = services.Stat()
    for entry in modules:
        stat = services.Stat()
        for step in entry["steps"]:
            rows = step["lessons"]
            step["stat"] = services.Stat(done=sum(r["state"] == DONE for r in rows), total=len(rows))
            step["state"] = _state(step["stat"].done, step["stat"].total, any(r["state"] == PROGRESS for r in rows))
            step["is_current"] = any(r["is_next"] for r in rows)
            step["state_label"] = STATE_LABELS[step["state"]]
            # Tapping a step opens the lesson to continue, else the first one still to do, else the first.
            target = next((r for r in rows if r["is_next"]), None) or next((r for r in rows if r["state"] != DONE), rows[0])
            step["target"] = target["lesson"]
            step["show_mastery"] = step["practice_set"] is not None or step["mastery"].rank > 0
            if step["is_current"]:
                current_step = step
            stat.done += step["stat"].done
            stat.total += step["stat"].total
        entry["stat"] = stat
        entry["state"] = _state(stat.done, stat.total, any(s["state"] != TODO for s in entry["steps"]))
        entry["is_current"] = any(s["is_current"] for s in entry["steps"])
        entry["is_open"] = entry["is_current"]
        course_stat.done += stat.done
        course_stat.total += stat.total

    if current_step is None and modules and not course_stat.is_complete:
        modules[0]["is_open"] = True
    started = bool(course_stat.done or any(r["state"] == PROGRESS for s in step_by_pk.values() for r in s["lessons"]))
    return {
        "modules": modules, "stat": course_stat, "current_step": current_step, "next_lesson": next_lesson,
        "started": started, "is_complete": course_stat.is_complete,
    }
