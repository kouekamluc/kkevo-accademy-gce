"""My report card: marks out of 20 per subject, from the student's own practice."""

from urllib.parse import quote

from django.shortcuts import render
from django.utils import timezone

from .. import reportcard
from apps.accounts.decorators import onboarding_required

from ._common import _plan


@onboarding_required
def report_card(request):
    user = request.user
    card = reportcard.build(user, [p["subject"] for p in _plan(user)])
    name = user.first_name or user.display_name
    lines = [f"{name}'s report card, KKEVO Academy"]
    for row in card["rows"]:
        if row["mark"] is not None:
            lines.append(f"{row['subject'].name}: {row['mark']}/20 ({row['remark']})")
    if card["average"] is not None:
        lines.append(f"Average: {card['average']}/20")
    card.update({
        "today": timezone.localdate(), "nav_active": "report", "student_name": name,
        "share_text": quote("\n".join(lines)) if card["marked"] else "",
        "scale": reportcard.BANDS,
    })
    return render(request, "learning/report_card.html", card)
