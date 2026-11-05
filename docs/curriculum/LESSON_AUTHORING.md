# Writing lessons for the GCE course outlines

Lesson content lives in Python files in `apps/courses/lesson_content/`, one or more files per
course. `python manage.py load_lessons` turns them into **draft** lessons inside the
"[gce-guide]" outline courses created by `load_gce_curriculum`. Nothing is published
automatically: a reviewer opens each draft in the studio (`/studio/`), checks it against the
official GCE Board syllabus, edits it, and publishes it there.

```bash
.venv/Scripts/python manage.py check_lessons f5_mathematics_a   # validate one file, no database
.venv/Scripts/python manage.py load_lessons --dry-run           # validate everything, save nothing
.venv/Scripts/python manage.py load_lessons                     # create the missing drafts
.venv/Scripts/python manage.py load_lessons --refresh           # rewrite drafts nobody has touched in the studio
```

## File format

```python
from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")   # (subject slug, level slug) from apps/academics/gce_curriculum.py
# Shared content: COURSE = [("pure-mathematics-with-mechanics", "lower-sixth"),
#                           ("pure-mathematics-with-statistics", "lower-sixth")]

LESSONS = [
    lesson(
        module="Quadratic Functions & Equations",   # syllabus section title, exactly
        topic="Solving quadratics",                 # syllabus item title, exactly
        title="Solving quadratic equations by factorization",
        slug="solving-quadratics-by-factorization", # lowercase-hyphenated, unique within the course
        minutes=20,
        summary="One sentence shown in the course outline (max 300 characters).",
        objectives=["Solve ... by ...", "..."],
        key_concepts=["Quadratic equation", "Root"],
        blocks=[
            H("Introduction"),
            T("Paragraph text with **bold**, *italic* and $x^2$ maths."),
            D("A **root** is ...", title="Definition", formula=r"ax^2 + bx + c = 0"),
            EX("Worked example 1", solve=r"x^2 - 5x + 6 = 0", steps=[
                S("Find two numbers that multiply to 6 and add to -5", text="They are -2 and -3."),
                S("Factorize", math=r"(x - 2)(x - 3) = 0"),
                S("Solve", math=r"x = 2 \text{ or } x = 3"),
            ], check=r"2^2 - 5(2) + 6 = 0"),
            EX("Worked example 2", intro="A trader in Bamenda ...", steps=[...]),   # word problem: intro, no solve
            TIP("..."), MISTAKE("Name of the mistake", "How to avoid it."),
            QUIZ("Question?", ["A", "B", "C", "D"], 1, "Why B is right.", hint="...",
                 feedback=["Why A is wrong.", "", "Why C is wrong.", "Why D is wrong."]),
            PQ("Practice question", "Worked answer."),
            CODE("print('hi')", "python", title="Listing 1"),
            GRAPH([1, -5, 6], alt="Parabola crossing the x-axis at 2 and 3", caption="Figure 1 ...",
                  xmin=0, xmax=5.5, ymin=-1, ymax=6.5, roots=[2, 3], label="y = x² − 5x + 6"),
            KEY("Key idea", "Text", cards=[["Heading", "Text"], ["Heading", "Text"]]),
            SUM("First point", "Second point", "Third point"),
        ],
    ),
]
```

## What a good lesson contains

Use `seed_demo.py`'s quadratics lesson (`quadratics_blocks`) as the quality bar.

1. **Introduction** (heading + short text): why the topic matters, ideally with a Cameroonian
   context (markets, FCFA prices, towns, local institutions).
2. **Definitions and key ideas** (`D`, `KEY`, `F`): every key concept named in `key_concepts`.
3. **At least two worked examples** (`EX`), each step small enough to follow on a phone.
   For history and other essay subjects, a worked example is a model answer plan:
   question in `intro`, one step per paragraph point.
4. **Common mistakes** (`MISTAKE`) that GCE examiners actually see.
5. **One or two quick checks** (`QUIZ`) with feedback for each wrong choice.
6. **At least three practice questions** (`PQ`) with full answers, in GCE style
   (Paper 1 multiple choice and Paper 2 structured questions).
7. **Summary** (`SUM`) of 3–6 points.

Length: 15–30 blocks, 15–30 minutes. Plain, clear English for students whose first language
may be French or a home language: short sentences, one idea per paragraph.

## Rules

- Stay within what the syllabus item describes. Do not invent syllabus requirements, exam
  questions "from past papers", statistics or quotations.
- History: use only well-established facts (dates, names, events). Where historians disagree,
  say so. Never invent quotations.
- Maths: LaTeX in raw strings (`r"..."`); check every answer by substituting back.
- No markdown tables, headings (`#`) or bullet lists inside text: use `H`, `SUM`, `KEY` cards
  and separate `T` blocks instead. `CODE` blocks show text exactly as written (no maths).
- `GRAPH` only draws polynomials.
- Images and videos are added later by staff from the media and video libraries.
