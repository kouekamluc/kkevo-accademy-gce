"""Small helpers for writing lesson content files in apps/courses/lesson_content/.

Every helper returns a plain dict that becomes one LessonBlock:
{"block_type", "title", "body", "data", "alt_text"}.

Text bodies accept **bold**, *italic*, $inline LaTeX$ and blank lines between paragraphs.
Use raw strings (r"...") whenever the text contains LaTeX backslashes.
"""


def _block(block_type, title="", body="", alt_text="", **data):
    return {"block_type": block_type, "title": title, "body": body, "alt_text": alt_text,
            "data": {k: v for k, v in data.items() if v not in (None, "", [], {})}}


def H(title):
    """Section heading (also an entry in the lesson's table of contents)."""
    return _block("heading", title)


def T(body, title=""):
    """Paragraphs of text."""
    return _block("text", title, body)


def F(latex, title=""):
    """A displayed formula, written in LaTeX without $ signs."""
    return _block("formula", title, latex)


def D(body, title="Definition", formula="", note=""):
    """Blue information box: a definition, a rule, a key fact."""
    return _block("definition", title, body, formula=formula, note=note)


def KEY(title, body, cards=None, note=""):
    """Key idea callout. `cards` is a list of [heading, text] pairs shown side by side."""
    return _block("callout", title, body, cards=[list(c) for c in (cards or [])], note=note)


def TIP(body, title="Tip"):
    return _block("tip", title, body)


def MISTAKE(title, body):
    """Common mistake: `title` names the mistake, `body` explains how to avoid it."""
    return _block("mistake", title, body)


def S(title, math="", text=""):
    """One step of a worked example. `math` is LaTeX (no $), `text` is an explanation."""
    return {k: v for k, v in {"title": title, "math": math, "text": text}.items() if v}


def EX(title, steps, solve="", intro="", check="", badge=""):
    """Worked example.

    `solve`: LaTeX equation shown as "Solve <equation>" in the header (leave empty otherwise).
    `intro`: the question in words (used when `solve` is empty).
    `steps`: list of S(...) steps; the last one is marked as the final answer.
    `check`: optional LaTeX shown in a green "Check:" bar.
    """
    steps = [dict(s) for s in steps]
    if steps:
        steps[-1]["final"] = True
    return _block("worked_example", title, solve, steps=steps, intro=intro, check=check, badge=badge)


def PQ(question, answer):
    """Practice question with a "Show answer" button."""
    return _block("practice", "", question, answer=answer)


def QUIZ(question, choices, correct, explanation, hint="", feedback=None, title="Quick check"):
    """Multiple-choice check. `correct` is the 0-based index of the right choice.

    `feedback`: optional list, one line per choice, explaining why each wrong choice is wrong
    (use "" for the correct one).
    """
    return _block("quiz", title, question, choices=list(choices), correct=correct, explanation=explanation,
                  hint=hint, feedback=list(feedback or []))


def SUM(*points):
    """Numbered summary list, one point per argument."""
    return _block("summary", "", "\n".join(points))


def CODE(code, language, title="", caption=""):
    """Code listing shown in monospace (no maths or formatting inside)."""
    return _block("code", title, code.strip("\n"), language=language, caption=caption)


def GRAPH(coeffs, alt, caption="", xmin=-5, xmax=5, ymin=-5, ymax=5, roots=None, label=""):
    """Graph of a polynomial: `coeffs` from the highest power down, e.g. [1, -5, 6] for x² − 5x + 6."""
    return _block("graph", "", caption, alt_text=alt, coeffs=list(coeffs), xmin=xmin, xmax=xmax,
                  ymin=ymin, ymax=ymax, roots=list(roots or []), label=label)


def lesson(module, topic, title, slug, minutes, summary, objectives, key_concepts, blocks):
    """One lesson. `module` and `topic` must match the syllabus outline titles exactly."""
    return {"module": module, "topic": topic, "title": title, "slug": slug, "minutes": minutes,
            "summary": summary, "objectives": list(objectives), "key_concepts": list(key_concepts),
            "blocks": list(blocks)}
