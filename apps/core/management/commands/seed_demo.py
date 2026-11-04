"""Load the sample content shown in the approved mockups, for demos and visual checks.

This is NOT official GCE syllabus content. Course structures, lesson text and questions
come from the design mockups (labelled "sample data" in the design README) and exist
so every screen can be reviewed with realistic data. Remove it with --remove.

    python manage.py seed_demo                  # subjects, courses, lessons, practice
    python manage.py seed_demo --with-student   # + a demo student with progress
    python manage.py seed_demo --remove         # delete everything this command created
"""

import secrets
from datetime import datetime, time, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from apps.academics.models import AcademicLevel, AcademicPathway, Subject, SubjectOffering
from apps.courses.models import Course, CourseResource, Lesson, LessonBlock, Module, Topic

DEMO_EMAIL = "demo.student@example.test"
DEMO_TAG = "[sample]"  # stored in Course.description so --remove can find demo courses

# name, slug, icon_text, icon, accent, category, summary, pathways, featured
SUBJECTS = [
    ("Mathematics", "mathematics", "x²", "", "blue", "sciences", "Algebra, geometry, trigonometry and statistics, from the basics up.", ["science", "arts"], True),
    ("Physics", "physics", "F", "", "blue", "sciences", "Motion, forces, energy, waves, electricity and simple simulations.", ["science"], True),
    ("Chemistry", "chemistry", "H₂O", "", "blue", "sciences", "Atomic structure, bonding, the mole, acids and organic chemistry.", ["science"], True),
    ("Biology", "biology", "", "dna", "emerald", "sciences", "Cells, nutrition, genetics, ecology and human health.", ["science"], True),
    ("Additional Mathematics", "additional-mathematics", "Σ", "", "blue", "sciences", "Functions, calculus basics, vectors and logarithms for A Level prep.", ["science"], False),
    ("Computer Science", "computer-science", "</>", "", "blue", "sciences", "Hardware, algorithms, programming logic and data.", ["science"], False),
    ("English Language", "english-language", "Aa", "", "slate", "languages", "Comprehension, summary, grammar and composition writing.", ["science", "arts"], True),
    ("Literature in English", "literature-in-english", "¶", "", "slate", "languages", "Prose, poetry and drama: themes, character and style.", ["arts"], False),
    ("French", "french", "Fr", "", "slate", "languages", "Grammar, vocabulary, reading and writing in French.", ["science", "arts"], False),
    ("History", "history", "1884", "", "amber", "humanities", "Cameroon and Africa from colonial rule to independence.", ["arts"], True),
    ("Geography", "geography", "", "map", "amber", "humanities", "Rivers, weather and climate, population and map reading.", ["science", "arts"], True),
    ("Economics", "economics", "", "chart", "amber", "humanities", "Demand and supply, money, markets and national income.", ["arts"], True),
]

MATHS_OUTLINE = [
    ("Algebra", "Expressions, factorization, quadratic and simultaneous equations", [
        ("Expressions and Factorization", [
            ("Algebraic Expressions and Terms", "reading", 10), ("Expanding Brackets", "reading", 12),
            ("Factorizing by Common Factors", "video", 9), ("Factorizing Quadratic Expressions", "reading", 16)]),
        ("Quadratic Equations", [
            ("Introduction to Quadratic Equations", "reading", 12), ("Solving Quadratic Equations by Factorization", "reading", 18),
            ("Completing the Square", "reading", 16), ("The Quadratic Formula", "interactive", 15),
            ("Word Problems with Quadratics", "practice", 20)]),
        ("Simultaneous Equations", [
            ("Elimination Method", "reading", 14), ("Substitution Method", "reading", 14), ("Graphical Solutions", "interactive", 15)]),
    ]),
    ("Geometry", "Angles, circle theorems, constructions", [
        ("Angles and Polygons", [("Angles on Parallel Lines", "reading", 10), ("Interior and Exterior Angles", "reading", 12), ("Regular Polygons", "reading", 10)]),
        ("Circle Theorems", [("Angles in a Semicircle", "reading", 12), ("Cyclic Quadrilaterals", "reading", 14), ("Tangent Properties", "video", 9), ("Proofs with Circle Theorems", "practice", 15)]),
        ("Constructions", [("Bisectors", "interactive", 12), ("Constructing Triangles", "reading", 12), ("Loci", "reading", 14)]),
    ]),
    ("Trigonometry", "Ratios, bearings, angles of elevation", [
        ("Trigonometric Ratios", [("Sine, Cosine and Tangent", "reading", 14), ("Finding Missing Sides", "reading", 12), ("Finding Missing Angles", "reading", 12)]),
        ("Bearings", [("Three-figure Bearings", "reading", 10), ("Bearings with Trigonometry", "practice", 15)]),
        ("Elevation and Depression", [("Angles of Elevation", "video", 8), ("Angles of Depression", "reading", 10), ("Problem Solving", "practice", 20)]),
    ]),
    ("Statistics", "Data, averages, probability", [
        ("Collecting and Presenting Data", [("Frequency Tables", "reading", 10), ("Bar Charts and Pie Charts", "reading", 12), ("Histograms", "interactive", 14)]),
        ("Averages", [("Mean, Median and Mode", "reading", 12), ("Averages from Frequency Tables", "reading", 14)]),
        ("Probability", [("Simple Probability", "reading", 10), ("Combined Events", "reading", 14), ("Tree Diagrams", "interactive", 15)]),
    ]),
]
MATHS_OUTCOMES = """Factorize and solve quadratic equations
Apply circle theorems in proofs
Use sine, cosine and tangent with bearings
Calculate averages and simple probabilities"""


def block(lesson, order, block_type, title="", body="", **extra):
    return LessonBlock(lesson=lesson, order=order, block_type=block_type, title=title, body=body,
                       media_url=extra.pop("media_url", ""), alt_text=extra.pop("alt_text", ""), data=extra)


def quadratics_blocks(lesson):
    """Lesson content from mockup 04."""
    b = []
    n = iter(range(1, 100))
    b.append(block(lesson, next(n), "heading", "Introduction"))
    b.append(block(lesson, next(n), "text", body=(
        "In the last lesson you met equations like $x^2 - 5x + 6 = 0$. Unlike a linear equation, a quadratic can have "
        "**two** solutions, so the usual \u201cget $x$ on its own\u201d approach doesn\u2019t work.\n\n"
        "Factorization gives us a different strategy: rewrite the left-hand side as a product of two brackets, "
        "then use one simple fact about multiplying by zero.")))
    b.append(block(lesson, next(n), "definition", "Definition", body=(
        "A **quadratic equation** is any equation that can be written in the form"), formula=r"ax^2 + bx + c = 0,\quad \text{where } a \neq 0.",
        note="The values of $x$ that make it true are called its **roots** or **solutions**."))
    b.append(block(lesson, next(n), "heading", "The key idea: the zero product property"))
    b.append(block(lesson, next(n), "text", body="If two numbers multiply to give zero, at least one of them must be zero. There is no other way to get zero from a multiplication."))
    b.append(block(lesson, next(n), "formula", body=r"\text{If } A \times B = 0,\ \text{then } A = 0 \text{ or } B = 0"))
    b.append(block(lesson, next(n), "text", body="So if we can write a quadratic as $(x - p)(x - q) = 0$, its roots are simply $x = p$ and $x = q$."))
    b.append(block(lesson, next(n), "graph", body="Figure 1. The roots are where the curve crosses the $x$-axis, because that is where $y = 0$.",
                   alt_text="Graph of y = x squared minus 5x plus 6 crossing the x-axis at 2 and 3",
                   coeffs=[1, -5, 6], xmin=0, xmax=5.5, ymin=-1, ymax=6.5, roots=[2, 3], label="y = x² − 5x + 6"))
    b.append(block(lesson, next(n), "worked_example", "Worked example 1", body=r"x^2 - 5x + 6 = 0", badge="a = 1", steps=[
        {"title": "Check it equals zero and identify $b$ and $c$", "text": "The right-hand side is already 0. Here $b = -5$ and $c = 6$."},
        {"title": "Find two numbers that multiply to $c$ and add to $b$", "chips": ["1 × 6 → 7", "2 × 3 → 5", "−1 × −6 → −7", "−2 × −3 → −5 ✓"]},
        {"title": "Write the factorized form", "math": r"(x - 2)(x - 3) = 0"},
        {"title": "Apply the zero product property", "math": r"x - 2 = 0 \quad\text{or}\quad x - 3 = 0"},
        {"title": "Solve each linear equation", "math": r"x = 2 \quad\text{or}\quad x = 3", "final": True},
    ], check=r"2^2 - 5(2) + 6 = 4 - 10 + 6 = 0"))
    b.append(block(lesson, next(n), "tip", "Tip", body="If $c$ is positive and $b$ is negative, both numbers in your pair must be **negative**. This cuts your search in half."))
    b.append(block(lesson, next(n), "heading", "Worked example 2: when $a \u2260 1$"))
    b.append(block(lesson, next(n), "text", body="When the $x^2$ term has a coefficient, we look for two numbers that multiply to $a \\times c$ instead, then split the middle term."))
    b.append(block(lesson, next(n), "worked_example", "Worked example 2", body=r"2x^2 + 7x + 3 = 0", steps=[
        {"title": "Multiply $a$ by $c$", "math": r"ac = 2 \times 3 = 6"},
        {"title": "Find two numbers that multiply to 6 and add to 7", "text": "They are 6 and 1. Use them to split $7x$ into $6x + x$."},
        {"title": "Factorize in pairs", "math": "2x^2 + 6x + x + 3 = 0\\\\2x(x + 3) + 1(x + 3) = 0\\\\(2x + 1)(x + 3) = 0"},
        {"title": "Solve each bracket", "math": r"x = -\tfrac{1}{2} \quad\text{or}\quad x = -3", "final": True},
    ]))
    b.append(block(lesson, next(n), "heading", "Common mistakes"))
    b.append(block(lesson, next(n), "mistake", "Not setting the equation to zero first", body="$x(x - 5) = 6$ does **not** mean $x = 6$ or $x - 5 = 6$. Move everything to one side first: $x^2 - 5x - 6 = 0$."))
    b.append(block(lesson, next(n), "mistake", "Dividing both sides by $x$", body="From $x^2 = 3x$, dividing by $x$ gives only $x = 3$ and loses $x = 0$. Factorize instead: $x(x - 3) = 0$."))
    b.append(block(lesson, next(n), "mistake", "Getting the sign of the root wrong", body="The bracket $(x + 3)$ gives the root $x = -3$, not $+3$."))
    b.append(block(lesson, next(n), "heading", "Practice questions"))
    b.append(block(lesson, next(n), "text", body="Try each one on paper first, then reveal the answer."))
    b.append(block(lesson, next(n), "practice", body="Solve $x^2 + 7x + 12 = 0$", answer="$(x + 3)(x + 4) = 0$, so $x = -3$ or $x = -4$."))
    b.append(block(lesson, next(n), "practice", body="Solve $x^2 - 9 = 0$", answer="Difference of two squares: $(x - 3)(x + 3) = 0$, so $x = 3$ or $x = -3$."))
    b.append(block(lesson, next(n), "practice", body="Solve $3x^2 - 12x = 0$", answer="$3x(x - 4) = 0$, so $x = 0$ or $x = 4$."))
    b.append(block(lesson, next(n), "heading", "Summary"))
    b.append(block(lesson, next(n), "summary", body=(
        "Rearrange so the equation equals zero.\nFactorize the quadratic into two brackets (use $ac$ when $a \u2260 1$).\n"
        "Set each bracket equal to zero and solve.\nCheck both answers by substituting them back.")))
    return b


def newton_blocks(lesson):
    """Interactive lesson from mockup 05."""
    return [
        block(lesson, 1, "simulation", key="newton-cart", law="F = ma", definitions=[
            ["F", "net force, in newtons (N)"], ["m", "mass, in kilograms (kg)"], ["a", "acceleration, in m/s²"]]),
        block(lesson, 2, "callout", "What the simulation shows", body=(
            "A resultant force makes an object **accelerate**, meaning its velocity changes every second. "
            "Two things decide how big that acceleration is:"),
            cards=[["More force → more acceleration", "$a$ is directly proportional to $F$. Double $F$, double $a$."],
                   ["More mass → less acceleration", "$a$ is inversely proportional to $m$. Double $m$, halve $a$."]],
            note="One newton is the force that gives a 1 kg mass an acceleration of 1 m/s²."),
        block(lesson, 3, "worked_example", "Worked example", body="", intro=(
            "A pushcart of mass $60\\ \\text{kg}$ at Mokolo market is pushed with a resultant force of $150\\ \\text{N}$. Find its acceleration."),
            steps=[{"title": "Write the law: $F = ma$, so $a = F \\div m$"}, {"title": "Substitute: $a = 150 \\div 60$"},
                   {"title": "Answer with units: $a = 2.5\\ \\text{m/s}^2$", "final": True}]),
        block(lesson, 4, "quiz", "Quick check", body="A $4\\ \\text{kg}$ box is pushed with a net force of $12\\ \\text{N}$. What is its acceleration?",
              choices=["$48\\ \\text{m/s}^2$", "$3\\ \\text{m/s}^2$", "$0.33\\ \\text{m/s}^2$", "$16\\ \\text{m/s}^2$"], correct=1,
              explanation="$a = F \\div m = 12 \\div 4 = 3\\ \\text{m/s}^2$."),
    ]


def erosion_blocks(lesson):
    """Video lesson from mockup 06."""
    return [
        block(lesson, 1, "video", "Understanding River Erosion", media_url="", duration=680, size_mb=18, chapters=[
            [0, "What is river erosion?"], [95, "Hydraulic action"], [190, "Abrasion (corrasion)"], [302, "Attrition"],
            [400, "Solution (corrosion)"], [495, "Vertical vs lateral erosion"], [605, "Summary"]],
            transcript="Transcript will appear here once the video is uploaded.",
            concepts=[["Hydraulic action", "The force of moving water pushes into cracks in the banks and breaks rock apart."],
                      ["Abrasion", "Rocks carried by the river scrape and grind the bed and banks."],
                      ["Attrition", "Rocks in the load hit each other, becoming smaller and rounder."],
                      ["Solution", "Slightly acidic water dissolves rocks such as limestone."]]),
    ]


PHYSICS_QUESTIONS = [
    ("A car of mass $1200\\ \\text{kg}$ accelerates uniformly from rest to $15\\ \\text{m/s}$ in $5\\ \\text{s}$. What is the resultant force acting on it?",
     "Newton’s second law", "Calculation", "You found the acceleration first, then used $F = ma$.",
     [{"title": "Find the acceleration", "math": r"a = (v - u) \div t = (15 - 0) \div 5 = 3\ \text{m/s}^2"},
      {"title": "Apply Newton’s second law", "math": r"F = ma = 1200 \times 3 = 3600\ \text{N}", "final": True}],
     [("$1800\\ \\text{N}$", False, "That halves the correct answer. Check the acceleration: $15 \\div 5 = 3$, not $1.5$."),
      ("$3600\\ \\text{N}$", True, ""),
      ("$6000\\ \\text{N}$", False, "That uses $1200 \\times 5$, multiplying by the time instead of the acceleration."),
      ("$18\\,000\\ \\text{N}$", False, "That multiplies mass by the final speed, which skips the time. Force depends on acceleration, not speed.")]),
    ("A resultant force of $20\\ \\text{N}$ acts on a $5\\ \\text{kg}$ trolley. What is its acceleration?",
     "Newton’s second law", "Calculation", "Rearranged $F = ma$ to $a = F \\div m$.",
     [{"title": "Rearrange the law", "math": r"a = F \div m"}, {"title": "Substitute", "math": r"a = 20 \div 5 = 4\ \text{m/s}^2", "final": True}],
     [("$100\\ \\text{m/s}^2$", False, "That multiplies force by mass instead of dividing."), ("$4\\ \\text{m/s}^2$", True, ""),
      ("$0.25\\ \\text{m/s}^2$", False, "That divides mass by force. Acceleration is force ÷ mass."), ("$15\\ \\text{m/s}^2$", False, "Subtracting the values has no physical meaning here.")]),
    ("A book rests on a table. Which statement about the forces on the book is true?",
     "Newton’s first law", "Concept", "Balanced forces mean no change in motion.",
     [{"title": "The book is not accelerating", "text": "Its velocity stays zero, so the resultant force must be zero."},
      {"title": "So the forces balance", "text": "The upward push of the table equals the book’s weight.", "final": True}],
     [("There are no forces acting on it.", False, "Gravity still pulls the book down; the table pushes up."),
      ("The forces on it are balanced.", True, ""),
      ("The weight is bigger than the push of the table.", False, "Then the book would accelerate downwards through the table."),
      ("It needs a force to stay still.", False, "No resultant force is needed to stay at rest.")]),
    ("The same force acts on two carts. Cart B has twice the mass of cart A. How does the acceleration of B compare with A?",
     "Newton’s second law", "Reasoning", "Acceleration is inversely proportional to mass.",
     [{"title": "Use $a = F \\div m$", "text": "With $F$ fixed, doubling $m$ halves $a$.", "final": True}],
     [("Twice as large", False, "More mass gives less acceleration, not more."), ("The same", False, "Mass does change the acceleration."),
      ("Half as large", True, ""), ("Four times smaller", False, "Doubling the mass halves the acceleration; it does not quarter it.")]),
    ("What is the unit of force?",
     "Units", "Recall", "1 N is the force that gives 1 kg an acceleration of 1 m/s².",
     [{"title": "Force is measured in newtons", "math": r"1\ \text{N} = 1\ \text{kg}\,\text{m/s}^2", "final": True}],
     [("Joule (J)", False, "The joule is the unit of energy."), ("Newton (N)", True, ""),
      ("Watt (W)", False, "The watt is the unit of power."), ("Kilogram (kg)", False, "The kilogram is the unit of mass.")]),
]


class Command(BaseCommand):
    help = "Load (or remove) the sample content from the design mockups. Not official syllabus content."

    def add_arguments(self, parser):
        parser.add_argument("--with-student", action="store_true", help="Also create a demo student with progress.")
        parser.add_argument("--remove", action="store_true", help="Delete everything this command created.")

    def handle(self, *args, **options):
        if options["remove"]:
            return self.remove()
        with transaction.atomic():
            self.seed_content()
            if options["with_student"]:
                self.seed_student()

    # ------------------------------------------------------------------ content
    def seed_content(self):
        levels = {lvl.code: lvl for lvl in AcademicLevel.objects.all()}
        pathways = {p.slug: p for p in AcademicPathway.objects.all()}
        self.offerings = {}
        for i, (name, slug, glyph, icon, accent, category, summary, paths, featured) in enumerate(SUBJECTS):
            subject, _ = Subject.objects.get_or_create(slug=slug, defaults=dict(
                name=name, icon_text=glyph, icon=icon, accent=accent, category=category, summary=summary,
                is_featured=featured, order=i * 10))
            for code in ("F5", "L6", "U6"):
                if code != "F5" and slug in ("english-language", "computer-science", "french"):
                    continue
                offering, created = SubjectOffering.objects.get_or_create(subject=subject, level=levels[code])
                if created:
                    offering.pathways.set([pathways[p] for p in paths if p in pathways])
                self.offerings[(slug, code)] = offering

        self.maths = self.make_course("mathematics", "Form 5 Mathematics", "form-5-mathematics",
                                      "Build confidence in algebra, geometry, trigonometry and statistics, one idea at a time. "
                                      "Every lesson explains the method, works through examples, then lets you practise.",
                                      MATHS_OUTLINE, MATHS_OUTCOMES)
        CourseResource.objects.get_or_create(course=self.maths, title="Formula sheet", defaults=dict(
            kind="pdf", url="https://example.invalid/formula-sheet.pdf", detail="PDF · 140 KB", order=1))
        CourseResource.objects.get_or_create(course=self.maths, title="Glossary of terms", defaults=dict(
            kind="glossary", url="https://example.invalid/glossary", detail="86 terms", order=2))

        target = Lesson.objects.get(topic__module__course=self.maths, slug="solving-quadratic-equations-by-factorization")
        if not target.blocks.exists():
            target.summary = "Learn how to turn a quadratic equation into two simple linear equations, and find both of its solutions."
            target.objectives = ("Recognise a quadratic equation in standard form\nExplain why the zero product property lets us split an equation\n"
                                 "Solve quadratics where a = 1 and where a ≠ 1\nCheck your solutions by substitution")
            target.key_concepts = "Quadratic equation\nRoot\nFactorization\nZero product property\nDifference of squares"
            target.save()
            target.prerequisites.add(Lesson.objects.get(topic__module__course=self.maths, slug="factorizing-quadratic-expressions"))
            LessonBlock.objects.bulk_create(quadratics_blocks(target))

        physics = self.make_course("physics", "Form 5 Physics", "form-5-physics",
                                   "Understand motion, forces and energy through simulations and worked examples.", [
            ("Measurement", "Units, scalars and vectors", [("Scalars and Vectors", [("Scalars and Vectors", "reading", 12)])]),
            ("Forces and Motion", "Newton’s laws, momentum, circular motion", [
                ("Newton’s Laws", [("Newton’s First Law of Motion", "reading", 12), ("Newton’s Second Law of Motion", "interactive", 20),
                                   ("Newton’s Third Law of Motion", "reading", 12), ("Circular Motion and Centripetal Force", "reading", 15)])]),
        ], "Describe motion with vectors\nApply Newton’s laws to everyday situations")
        newton = Lesson.objects.get(topic__module__course=physics, slug="newtons-second-law-of-motion")
        if not newton.blocks.exists():
            newton.summary = "Change the force and the mass, run the cart, and watch how acceleration responds."
            newton.save()
            LessonBlock.objects.bulk_create(newton_blocks(newton))
        self.newton = newton

        geography = self.make_course("geography", "Form 5 Geography", "form-5-geography",
                                     "Physical and human geography with map work.", [
            ("Weather and Climate", "Elements of weather", [("Weather", [("Elements of Weather", "reading", 12)])]),
            ("Rivers and Drainage", "How rivers shape the land", [("River Processes", [
                ("The Work of Rivers: Erosion, Transport, Deposition", "reading", 14), ("Understanding River Erosion", "video", 11),
                ("How Rivers Transport Their Load", "video", 9), ("Waterfalls and Gorges", "video", 8),
                ("Meanders and Ox-bow Lakes", "video", 9), ("Map skills: drainage patterns", "interactive", 10)])]),
        ], "Explain how rivers erode, transport and deposit material")
        erosion = Lesson.objects.get(topic__module__course=geography, slug="understanding-river-erosion")
        if not erosion.blocks.exists():
            erosion.summary = ("How a river wears away its bed and banks through four processes, and why rivers cut downwards "
                               "in their upper course but sideways further downstream.")
            erosion.key_concepts = "Hydraulic action\nAbrasion\nAttrition\nSolution"
            erosion.save()
            LessonBlock.objects.bulk_create(erosion_blocks(erosion))

        for slug, title in [("chemistry", "Form 5 Chemistry"), ("biology", "Form 5 Biology"), ("english-language", "Form 5 English Language")]:
            self.make_course(slug, title, title.lower().replace(" ", "-"), f"Sample {title} course.", [
                ("Foundations", "Core ideas", [("Getting started", [("Introduction", "reading", 10)])])], "")

        self.seed_practice(newton)
        self.stdout.write(self.style.SUCCESS("Sample content loaded (not official syllabus content)."))

    def make_course(self, subject_slug, title, slug, summary, outline, outcomes):
        course, _ = Course.objects.get_or_create(slug=slug, defaults=dict(
            offering=self.offerings[(subject_slug, "F5")], title=title, summary=summary,
            description=DEMO_TAG, learning_outcomes=outcomes, status="published"))
        if course.modules.exists():
            return course
        for m_i, (m_title, m_summary, topics) in enumerate(outline, 1):
            module = Module.objects.create(course=course, title=m_title, summary=m_summary, order=m_i)
            for t_i, (t_title, lessons) in enumerate(topics, 1):
                topic = Topic.objects.create(module=module, title=t_title, order=t_i)
                for l_i, (l_title, l_type, minutes) in enumerate(lessons, 1):
                    from django.utils.text import slugify

                    Lesson.objects.create(topic=topic, title=l_title, slug=slugify(l_title.replace("’", "")),
                                          lesson_type=l_type, estimated_minutes=minutes, order=l_i, status="published")
        return course

    def seed_practice(self, newton):
        from apps.practice.models import Choice, PracticeSet, Question

        practice_set, created = PracticeSet.objects.get_or_create(
            topic=newton.topic, title="Physics: Newton’s Laws", defaults=dict(lesson=newton, status="published"))
        if not created:
            return
        for q_i, (prompt, concept, skill, feedback, steps, choices) in enumerate(PHYSICS_QUESTIONS):
            q = Question.objects.create(practice_set=practice_set, prompt=prompt, concept=concept, skill=skill,
                                        feedback=feedback, solution_steps=steps, order=q_i)
            Choice.objects.bulk_create([Choice(question=q, text=t, is_correct=ok, why_wrong=why, order=c_i)
                                        for c_i, (t, ok, why) in enumerate(choices)])

    # ------------------------------------------------------------------ student
    def seed_student(self):
        from apps.learning.models import DailyActivity, Enrollment, LessonProgress, StudySession
        from apps.practice.models import Answer, Attempt, PracticeSet

        User = get_user_model()
        user = User.objects.filter(email=DEMO_EMAIL).first()
        password = None
        if user is None:
            password = secrets.token_urlsafe(9)
            user = User.objects.create_user(email=DEMO_EMAIL, password=password, first_name="Alex", last_name="Nfor")
        profile = user.profile
        profile.level = AcademicLevel.objects.get(code="F5")
        profile.pathway = AcademicPathway.objects.get(slug="science")
        profile.onboarded_at = profile.onboarded_at or timezone.now()
        profile.save()
        for slug in ("mathematics", "physics", "chemistry", "biology", "english-language"):
            Enrollment.objects.get_or_create(user=user, offering=self.offerings[(slug, "F5")])

        now = timezone.now()
        lessons = list(Lesson.objects.filter(topic__module__course=self.maths)
                       .order_by("topic__module__order", "topic__order", "order"))
        done_titles = {"Algebraic Expressions and Terms", "Expanding Brackets", "Factorizing by Common Factors",
                       "Factorizing Quadratic Expressions", "Introduction to Quadratic Equations"}
        for i, lesson in enumerate(lessons):
            module = lesson.topic.module.title
            completed = (lesson.title in done_titles or module == "Geometry"
                         or (module == "Trigonometry" and i % 8 != 0) or (module == "Statistics" and i % 2 == 0))
            if completed:
                LessonProgress.objects.update_or_create(user=user, lesson=lesson, defaults=dict(
                    percent=100, completed_at=now - timedelta(days=30 - i % 25), last_viewed_at=now - timedelta(days=30 - i % 25),
                    time_spent_seconds=lesson.estimated_minutes * 60))
        current = next(l for l in lessons if l.slug == "solving-quadratic-equations-by-factorization")
        LessonProgress.objects.update_or_create(user=user, lesson=current, defaults=dict(
            percent=58, position_label="Worked example 2", last_viewed_at=now - timedelta(hours=20), completed_at=None))
        LessonProgress.objects.update_or_create(user=user, lesson=Lesson.objects.get(slug="scalars-and-vectors"), defaults=dict(
            percent=100, completed_at=now - timedelta(days=2), time_spent_seconds=19 * 60))

        today = timezone.localdate()
        minutes = [40, 55, 70, 30, 45, 60, 25] * 8
        for d in range(56):
            DailyActivity.objects.update_or_create(user=user, date=today - timedelta(days=55 - d),
                                                   defaults=dict(seconds=minutes[d] * 60))

        practice_set = PracticeSet.objects.get(title="Physics: Newton’s Laws")
        if not Attempt.objects.filter(user=user).exists():
            for k, right in enumerate([3, 4, 3, 4, 5]):
                attempt = Attempt.objects.create(user=user, practice_set=practice_set)
                Attempt.objects.filter(pk=attempt.pk).update(started_at=now - timedelta(days=20 - 4 * k))
                for q_i, question in enumerate(practice_set.questions.all()):
                    good = q_i < right
                    choice = question.choices.filter(is_correct=good).first()
                    Answer.objects.create(attempt=attempt, question=question, choice=choice, is_correct=good)
                attempt.finish()
                Attempt.objects.filter(pk=attempt.pk).update(completed_at=now - timedelta(days=20 - 4 * k))

        if not StudySession.objects.filter(user=user).exists():
            monday = today - timedelta(days=today.weekday())
            maths = Subject.objects.get(slug="mathematics")
            phys = Subject.objects.get(slug="physics")
            chem = Subject.objects.get(slug="chemistry")
            eng = Subject.objects.get(slug="english-language")
            bio = Subject.objects.get(slug="biology")
            plan = [  # day offset, hour, minute, minutes, subject, title, kind
                (0, 16, 0, 60, maths, "Quadratic equations", "study"), (0, 19, 0, 45, eng, "Summary writing", "study"),
                (1, 16, 30, 60, phys, "Vectors review", "revision"), (1, 18, 0, 60, chem, "Bonding practice", "practice"),
                (2, 16, 0, 45, maths, "Factorization", "study"), (2, 17, 30, 30, phys, "Newton’s 1st law", "revision"),
                (2, 19, 0, 60, chem, "The mole concept", "study"), (3, 16, 0, 60, maths, "Indices & logs practice", "practice"),
                (3, 18, 30, 60, bio, "Photosynthesis", "study"), (4, 17, 0, 60, chem, "Review: the mole", "revision"),
                (4, 19, 0, 30, eng, "Comprehension", "study"), (5, 15, 0, 90, maths, "Weekly revision: Maths & Physics", "revision"),
                (6, 16, 0, 15, None, "Plan next week", "planning"),
            ]
            tz = timezone.get_current_timezone()
            for day, hour, minute, mins, subject, title, kind in plan:
                starts = timezone.make_aware(datetime.combine(monday + timedelta(days=day), time(hour, minute)), tz)
                StudySession.objects.create(user=user, subject=subject, title=title, kind=kind, starts_at=starts,
                                            duration_minutes=mins, completed_at=starts + timedelta(minutes=mins) if starts + timedelta(minutes=mins) < now else None)

        msg = f"Demo student ready: {DEMO_EMAIL}"
        if password:
            msg += f" (password: {password} — shown once, change it in Profile)"
        self.stdout.write(self.style.SUCCESS(msg))

    # ------------------------------------------------------------------ remove
    def remove(self):
        User = get_user_model()
        with transaction.atomic():
            User.objects.filter(email=DEMO_EMAIL).delete()
            from apps.practice.models import PracticeSet

            PracticeSet.objects.filter(title="Physics: Newton’s Laws", topic__module__course__description=DEMO_TAG).delete()
            Course.objects.filter(description=DEMO_TAG).delete()
            slugs = [s[1] for s in SUBJECTS]
            SubjectOffering.objects.filter(subject__slug__in=slugs, courses__isnull=True).delete()
            Subject.objects.filter(slug__in=slugs, offerings__isnull=True).delete()
        self.stdout.write(self.style.SUCCESS("Sample content removed."))
