"""The student's report card: one mark out of 20 per subject, from their own practice scores.

A subject's mark is the average of the latest score on each topic they have practised (mock papers are
left out, as in topic mastery). The grade is an estimate on a fixed scale and the page says so: it is a
guide for the student, never the exam board's result.
"""

from . import analytics

# (minimum percent, estimated GCE grade, remark)
BANDS = [
    (80, "A", "Excellent"),
    (70, "B", "Very good"),
    (60, "C", "Good"),
    (50, "D", "Fair"),
    (40, "E", "Must work harder"),
    (0, "U", "Needs help"),
]


def mark_out_of_20(percent):
    return round(percent / 5, 1)


def band_for(percent):
    for minimum, grade, remark in BANDS:
        if percent >= minimum:
            return grade, remark
    return BANDS[-1][1], BANDS[-1][2]


def build(user, subjects):
    """Rows for `subjects` (the student's own), plus the totals. A subject with no completed practice has no mark."""
    scores = {}
    for entry in analytics.topic_scores(user).values():
        scores.setdefault(entry["subject"].pk, []).append(entry["latest"])
    rows = []
    for subject in subjects:
        latest = scores.get(subject.pk)
        if not latest:
            rows.append({"subject": subject, "percent": None, "mark": None, "grade": "", "remark": "", "topics": 0})
            continue
        percent = round(sum(latest) / len(latest))
        grade, remark = band_for(percent)
        rows.append({"subject": subject, "percent": percent, "mark": mark_out_of_20(percent),
                     "grade": grade, "remark": remark, "topics": len(latest)})
    marked = [r for r in rows if r["percent"] is not None]
    average = round(sum(r["mark"] for r in marked) / len(marked), 1) if marked else None
    strongest = max(marked, key=lambda r: r["percent"]) if len(marked) > 1 else None
    weakest = min(marked, key=lambda r: r["percent"]) if len(marked) > 1 else None
    return {"rows": rows, "average": average, "marked": len(marked), "strongest": strongest, "weakest": weakest}
