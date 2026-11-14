"""Write the content review checklist: every sentence in the lessons that tells students to check a fact.

    python manage.py review_checklist                      # writes docs/curriculum/REVIEW_CHECKLIST.md
    python manage.py review_checklist --out some/file.md

The writers marked facts that textbooks differ on, or that they could not confirm, with phrases such as
"check your textbook", "check your copy" or "check the current rules". This gathers those sentences by
subject, class and lesson so a teacher can verify them against the Board's syllabus and the school's books.
"""

import re
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from apps.academics import gce_curriculum
from apps.courses import lesson_content

NOTE = re.compile(
    r"check (?:your (?:textbook|copy|tables|text)|the current (?:rules|position|figures|Finance Law)|current (?:rules|figures)"
    r"|with your teacher|the Finance Law|your school)", re.I)
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z(“\"'])")
LEVEL_NAMES = {"form-5": "Form 5 (O Level)", "lower-sixth": "Lower Sixth", "upper-sixth": "Upper Sixth"}

PRIORITY = """\
## Start here: facts that need an authority, not just a second reader

These are the claims most likely to be wrong or out of date. A subject teacher or an official source should settle them first.

1. **Cameroon taxes and payroll** (Accounting, Principles of Accounts, Business Studies, Commerce): VAT 19.25 % (17.5 % plus 10 % council tax), company tax 30 % plus 10 % additional council tax, minimum tax on turnover, IRCM 16.5 %, CNPS, CFC and FNE rates, the IRPP scale and the small-business turnover limits. They are labelled teaching values; check them against the current Finance Law.
2. **SYSCOHADA and OHADA** (Accounting, Principles of Accounts, Business Studies): account numbers (packaging deposits, bills of exchange, VAT, provisions, shares, reserves), the simplified Bilan, income-statement and cash-flow layouts, SA and SARL capital and reserve rules, the SAS added in 2014.
3. **BEAC, CEMAC and the economy** (Economics): member states, the 655.957 peg, COBAC, instrument names, the HIPC completion point (2006), the 1994 devaluation, NDS30 pillar names, CEMAC treaty and AfCFTA dates.
4. **Cameroon geography and geology** (Geography, Geology): census totals (1976, 1987, 2005), Mount Cameroon eruptions (1999 and 2000), Lake Nyos (1986) and its death toll, the Cameroon Volcanic Line (length, members, origin), basin names and ages, ore and bauxite localities, dam, port and mining project status.
5. **Cameroon and church history** (History, Religious Studies, Citizenship): mission dates and names (Merrick 1843, Basel 1886, Pallottines 1890), constitutional and administrative details, institutions and laws.
6. **Set texts, from memory** (Literature, French): plot and character details for Hamlet, Coriolanus, Hard Times, Death of a Salesman, A Raisin in the Sun, Nervous Conditions, Anthills of the Savannah, the Chaucer tales, Les Fausses Confidences, Le Dernier Jour d'un condamné, La Tragédie du Roi Christophe, Le Fils d'Agatha Moudio, Rotimi's play, and the poet-and-country pairs for Poems of Black Africa. Check each against the school's own copy and the Board's current list of prescribed texts.
7. **Philosophy and Religious Studies attributions**: dates and titles of African philosophers' works (Hountondji, Njoh-Mouelle, Eboussi Boulaga, Towa), the scholars named in the Pentateuch and Synoptic lessons, approximate dates in the prophets and Pauline lessons.
8. **Food Science and Nutrition numbers**: microbial growth limits (temperature, water activity, pH), clinical cut-offs (protein for kidney disease, ORS composition, Codex gluten limit, MUAC bands), ATP yields, BMR equations, irradiation doses.
9. **Maths and statistics conventions**: the quartile method (the n/4 rule is used), n versus n minus 1 in variance, normal-approximation thresholds and the continuity correction, restitution notation, the sign of a moment, the accuracy expected from normal-table answers.
10. **Mocks written before the lessons they test**: some Paper 1 mocks were written before the sibling lessons existed. Read their questions against the lessons: Geology Upper Sixth (sediments, structure), Accounting Upper Sixth (partnership, company), Economics Lower Sixth (price theory, costs), Geography Upper Sixth (statistics against map work), Food Science Upper Sixth (preservation, commodities), French Lower and Upper Sixth, Religious Studies Upper Sixth, Philosophy Lower Sixth, and the Pure Maths option mocks.
11. **Known small points**: the Economics Upper Sixth Paper 2 practice paper has 22 parts (about 25 intended); the Economics Lower Sixth lesson on Giffen goods makes a claim about recent studies that needs a source; two diagrams are cosmetically imperfect (alecu2 forex label crossing a line, algyl1 silicates-q chain touching its box edge).

Exam formats are stated from the Board's 2023 subject reports where they gave them, and otherwise say "check the exact format with your teacher". The outlines are built from KKEVO's master blueprint, which is not a Board syllabus booklet.

---

## Every flagged sentence, by subject
"""


class Command(BaseCommand):
    help = "Write the content review checklist (every 'check your textbook' style note in the lessons)."

    def add_arguments(self, parser):
        parser.add_argument("--out", default=str(Path(settings.BASE_DIR) / "docs" / "curriculum" / "REVIEW_CHECKLIST.md"))

    def handle(self, *args, **options):
        found = {}
        total = 0
        for key, spec, source in lesson_content.collect():
            sentences = []
            for block in spec["blocks"]:
                data = block.get("data") or {}
                pieces = [block.get("body", ""), block.get("title", "")]
                for value in data.values():
                    if isinstance(value, str):
                        pieces.append(value)
                    elif isinstance(value, list):
                        pieces += [v for v in value if isinstance(v, str)]
                for piece in pieces:
                    for sentence in SENTENCE.split(" ".join(piece.split())):
                        if NOTE.search(sentence) and sentence not in sentences:
                            sentences.append(sentence[:320])
            if sentences:
                total += len(sentences)
                found.setdefault(key, []).append((spec, source, sentences))
        lines = ["# Content review checklist", "",
                 f"{total} flagged sentences in {sum(len(v) for v in found.values())} lessons. "
                 "Generated by `python manage.py review_checklist`; regenerate after content changes.", "", PRIORITY]
        by_subject = {}
        for (subject, level), lessons in found.items():
            by_subject.setdefault(subject, {})[level] = lessons
        order = {slug: i for i, (slug, *_rest) in enumerate(gce_curriculum.SUBJECTS)}
        for subject in sorted(by_subject, key=lambda s: order.get(s, 999)):
            count = sum(len(sents) for lv in by_subject[subject].values() for _s, _f, sents in lv)
            lines += [f"### {subject.replace('-', ' ').title()} ({count})", ""]
            for level in ("form-5", "lower-sixth", "upper-sixth"):
                lessons = by_subject[subject].get(level)
                if not lessons:
                    continue
                lines += [f"**{LEVEL_NAMES[level]}**", ""]
                for spec, source, sentences in lessons:
                    lines.append(f"- *{spec['title']}* (`{spec['slug']}`, {source})")
                    lines += [f"  - [ ] {sentence}" for sentence in sentences]
                lines.append("")
        out = Path(options["out"])
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Wrote {out} ({total} flagged sentences)."))
