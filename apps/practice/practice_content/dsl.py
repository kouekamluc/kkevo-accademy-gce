"""Helpers for writing practice-set files in apps/practice/practice_content/.

Text accepts **bold**, *italic* and $inline LaTeX$ (use raw strings r"..." for backslashes).
"""


def S(title, math="", text=""):
    """One step of a worked solution. `math` is LaTeX without $, `text` an explanation."""
    return {k: v for k, v in {"title": title, "math": math, "text": text}.items() if v}


def C(text, correct=False, why=""):
    """One multiple-choice option. Every wrong option needs `why`: what mistake leads to it."""
    return {"text": text, "correct": correct, "why": why}


def _steps(steps):
    steps = [dict(s) for s in steps]
    if steps:
        steps[-1]["final"] = True
    return steps


def MC(prompt, choices, steps, concept="", skill="", hint="", feedback=""):
    """Multiple-choice question: 4 options (C(...)), exactly one correct."""
    return {"kind": "choice", "prompt": prompt, "choices": list(choices), "steps": _steps(steps),
            "concept": concept, "skill": skill, "hint": hint, "feedback": feedback}


def NUM(prompt, answer, steps, tolerance=0, unit="", concept="", skill="", hint="", feedback=""):
    """Typed numeric answer. `tolerance` is the accepted distance from `answer` (e.g. 0.05)."""
    return {"kind": "numeric", "prompt": prompt, "answer": answer, "tolerance": tolerance, "unit": unit,
            "steps": _steps(steps), "concept": concept, "skill": skill, "hint": hint, "feedback": feedback}


def practice_set(module, topic, title, lesson, questions, mock=False, time_limit_minutes=None):
    """A practice set for one syllabus topic. `lesson` is the slug of the lesson it follows.

    `mock=True` marks a full mock exam paper (listed under "Mock exams", kept out of topic mastery);
    `time_limit_minutes` sets its timed-exam length (e.g. 90 for Paper 1) instead of 1½ minutes a question.
    """
    return {"module": module, "topic": topic, "title": title, "lesson": lesson, "questions": list(questions),
            "mock": bool(mock), "time_limit_minutes": time_limit_minutes}
