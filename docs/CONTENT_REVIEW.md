# Reviewing a module before students rely on it

All 2,447 lessons and 2,529 practice sets were drafted with AI help. None has been checked against the
official GCE syllabus by a teacher. Nothing here replaces that. This page is the routine for doing it
one module at a time, and for using what students tell us.

## What a machine can check (run these first)

```
python manage.py check_lessons      # structure, quiz answers, links between lessons
python manage.py check_practice     # every wrong option explains its mistake, one correct answer, topics covered
```

Both pass on all current content. They catch broken structure, not wrong facts.

Spot-check of equation answers: 8 "Solve ..." questions in Form 5 Mathematics and Additional
Mathematics practice sets were solved independently with sympy and all matched the marked answer. Only the
simplest wording is recognised, so this covers a small part of the maths. It is not a review.

## What a person must check (per module)

The reviewer should be a subject teacher. For each lesson in the module, open it in the studio and tick:

1. **Syllabus match.** Every objective appears in the official syllabus for that level; nothing the
   syllabus requires is missing. Use the Syllabus and Curriculum references pages in the admin.
2. **Facts and working.** Definitions, formulas, dates and worked examples are correct.
3. **Cameroon context.** Examples, names, places, currency and spelling fit a Cameroon classroom.
4. **Practice.** Each practice question has exactly one right answer, and each wrong option's explanation
   names the real mistake.
5. **Level.** Wording and difficulty suit the class (Form 5, Lower Sixth, Upper Sixth).

Then submit the lesson for review in the studio. A person with the publish permission approves it. Keep a
short note of who reviewed which module and when (the studio's activity log records approvals).

## Where to start

Form 5 General Mathematics, module "Quadratic Functions & Equations": 7 lessons, each with a practice set
and function graphs. It is the most developed module, so review it first and use it as the model for the
others.

## Using student feedback

Students can report a problem from the bottom of every lesson, and from any practice question once they have
answered it. Staff see both in the studio under "Student feedback", with the most reported lessons and
practice sets listed first. Fix those lessons before anything else:
students found the mistake by actually using the lesson.
