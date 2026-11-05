"""Form 5 General Mathematics (O Level 570): Examination module (Paper 1 and Paper 2).

Draft content. The only exam facts stated here come from the syllabus outline in
apps/academics/gce_curriculum.py; students are told to check the current GCE Board
instructions for everything else.
"""

from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

LESSONS = [
    # ------------------------------------------------------------------ Paper 1
    lesson(
        module="Examination", topic="Paper 1",
        title="Paper 1: how it works and how to tackle it",
        slug="paper-1-multiple-choice-strategies",
        minutes=25,
        summary="How Paper 1 is organised (50 multiple-choice questions in 1.5 hours, 30% of the mark) and five "
                "strategies to answer quickly and accurately: answer everything, eliminate, estimate, check units, work on paper.",
        objectives=[
            "Describe the format of Paper 1 and plan about 1.8 minutes per question",
            "Eliminate wrong options and estimate an answer before calculating",
            "Use units, substitution and quick sketches to check a choice",
            "Recognise the common traps built into multiple-choice options",
        ],
        key_concepts=["Paper 1 format", "Time per question", "Elimination", "Estimation", "Checking units", "Distractor"],
        blocks=[
            H("Introduction"),
            T("Paper 1 tests the **whole course** in one sitting: sets, commercial arithmetic, quadratics, sequences, "
              "matrices, vectors, trigonometry, circles, statistics and probability. Each question is short, but there "
              "are many of them, so speed and accuracy both matter."),
            D("Paper 1 counts for **30%** of the General Mathematics mark. It has **50 multiple-choice questions** and "
              "lasts **1.5 hours** (90 minutes). In each question you choose one answer from the options given.",
              title="Paper 1 at a glance",
              note="For the exact instructions (how to record answers, what you may bring into the room), check the "
                   "current GCE Board instructions and listen to your invigilator."),
            KEY("Your time budget",
                r"$90 \text{ minutes} \div 50 \text{ questions} = 1.8$ minutes per question, about 1 minute 48 seconds.",
                cards=[["First pass", "Answer every question you can do quickly. Mark the hard ones and move on."],
                       ["Second pass", "Return to the marked questions with the time you saved. 1.8 minutes is an average: if a question has taken about 3 minutes, mark it and move on."],
                       ["Last minutes", "Make sure every question has an answer and that each answer is on the right line."]]),
            H("Strategy 1: answer every question"),
            T("A blank answer can never earn a mark. Unless the instructions on your paper say otherwise, put an answer "
              "for every question before time runs out. If you are unsure, first remove the options you know are wrong, "
              "then choose from what is left: your chance of being right goes up each time you remove an option."),
            H("Strategy 2: eliminate wrong options"),
            EX("Worked example 1: eliminate by substituting", intro=(
                r"Solve $x^2 - x - 12 = 0$. A: $x = 4$ or $x = -3$. B: $x = -4$ or $x = 3$. C: $x = 4$ or $x = 3$. "
                r"D: $x = -4$ or $x = -3$."), steps=[
                S("Test the easiest value", text=r"Try $x = 3$, which appears in B and C.",
                  math=r"3^2 - 3 - 12 = -6 \neq 0"),
                S("Eliminate", text="$x = 3$ is not a root, so B and C are wrong."),
                S("Test a value from A", math=r"4^2 - 4 - 12 = 0 \;\checkmark"),
                S("Choose", text="$x = 4$ is a root, so D is also wrong. The answer is **A**. (Check: $(-3)^2 + 3 - 12 = 0$.)"),
            ], check=r"(x - 4)(x + 3) = x^2 - x - 12"),
            H("Strategy 3: estimate first"),
            EX("Worked example 2: estimate before you calculate", intro=(
                "A trader in Bafoussam saves 250 000 FCFA at 6% compound interest per year. How much is in the account "
                "after 3 years? A: 280 900 FCFA. B: 295 000 FCFA. C: 297 754 FCFA. D: 345 000 FCFA."), steps=[
                S("Estimate with simple interest", math=r"250\,000 + 3 \times 15\,000 = 295\,000",
                  text="Compound interest gives a little **more** than simple interest after more than one year."),
                S("Eliminate", text="A is below the estimate (it is the amount after 2 years). B is exactly simple "
                                    "interest. D is far too large. Only C is just above 295 000."),
                S("Confirm if time allows", math=r"250\,000 \times 1.06^3 = 297\,754"),
                S("Answer", text="**C**: 297 754 FCFA."),
            ]),
            H("Strategy 4: check the units and the size"),
            EX("Worked example 3: units and size", intro=(
                r"Two sides of a triangle are 8 cm and 5 cm, and the angle between them is $30^\circ$. Find the area. "
                r"A: 10 cm. B: 10 cm². C: 20 cm². D: 34.6 cm²."), steps=[
                S("Check the units", text="Area is measured in square units, so A (cm) is wrong straight away."),
                S("Use the area formula", math=r"\tfrac{1}{2}ab\sin C = \tfrac{1}{2} \times 8 \times 5 \times \sin 30^\circ"),
                S("Calculate", math=r"= 20 \times 0.5 = 10 \text{ cm}^2"),
                S("Answer", text=r"**B**. C forgets the $\tfrac{1}{2}$; D uses $8 \times 5 \times \cos 30^\circ$."),
            ]),
            H("Strategy 5: work in the question booklet"),
            EX("Worked example 4: a quick sketch", intro=(
                r"The bearing of Q from P is $072^\circ$. Find the bearing of P from Q. A: $108^\circ$. B: $162^\circ$. "
                r"C: $252^\circ$. D: $288^\circ$."), steps=[
                S("Sketch", text="Draw a north line at P, then Q to the north-east. Draw a north line at Q too."),
                S("See the back bearing", text="From Q you look back towards the south-west, so the answer is more than "
                                              r"$180^\circ$. A and B are eliminated."),
                S("Calculate", math=r"072^\circ + 180^\circ = 252^\circ"),
                S("Answer", text=r"**C**. D is $360^\circ - 72^\circ$, a common slip."),
            ]),
            TIP("Use the space in the question booklet for sketches and short working. A small diagram often answers a "
                "bearings, Venn diagram or circle question in seconds. (Check the current GCE Board instructions for "
                "where rough work may be written.)"),
            H("Common traps"),
            MISTAKE("Choosing the first number that looks familiar",
                    "Wrong options are usually the results of common mistakes: forgetting the ½, using simple instead of "
                    "compound interest, or a sign error. Finding your number among the options does not prove it is "
                    "right. Check the method once."),
            MISTAKE("Spending five minutes on one question",
                    "Every question carries the same weight in a multiple-choice paper. Mark a hard question, move on, "
                    "and come back on the second pass."),
            MISTAKE("Rounding too early",
                    "Keep full calculator values until the end. Rounding in the middle can make your answer fall between "
                    "two options."),
            QUIZ("Paper 1 lasts 1.5 hours and has 50 questions. About how long should you spend on each question on average?",
                 ["About 1 minute", "About 1.8 minutes", "About 3 minutes", "About 30 seconds"], 1,
                 r"$90 \div 50 = 1.8$ minutes, about 1 minute 48 seconds.",
                 hint="Change 1.5 hours into minutes first.",
                 feedback=["That would use only 50 of the 90 minutes. You can afford a little more time.", "",
                           r"$50 \times 3 = 150$ minutes, far more than the 90 minutes allowed.",
                           r"$50 \times 0.5 = 25$ minutes. That is too rushed and leaves most of the time unused."]),
            QUIZ("A bag has 3 red and 5 blue beads. Two are taken out one after the other **without replacement**. "
                 "What is the probability that both are red?",
                 [r"$\frac{9}{64}$", r"$\frac{3}{8}$", r"$\frac{6}{8}$", r"$\frac{3}{28}$"], 3,
                 r"$\frac{3}{8} \times \frac{2}{7} = \frac{6}{56} = \frac{3}{28}$.",
                 hint="After the first red bead is taken, how many beads, and how many red beads, are left?",
                 feedback=[r"This is $\frac{3}{8} \times \frac{3}{8}$, which assumes the bead is put back.",
                           "This is only the probability that the first bead is red.",
                           "You added the two fractions. For 'first and second' you multiply.", ""]),
            H("Practice questions"),
            IMG("f5-venn-two-sets.svg",
                alt="Venn diagram in a rectangle labelled xi = 40, with two overlapping circles: Maths Club (M) and "
                    "French Club (F). M only is 18, the overlap is 7, F only is 11 and 4 are outside both circles.",
                caption="Figure 1. Practice question 1: a class of 40 students."),
            PQ("Use Figure 1. How many students are in the French Club but not in the Maths Club? "
               "A: 7. B: 11. C: 18. D: 22.",
               "**B**. 'French but not Maths' is the F-only region: 11. A is the overlap, C is Maths only, and D is "
               r"$11 + 7 + 4$, which wrongly adds the overlap and the outside region."),
            PQ(r"$y$ varies directly as $x^2$, and $y = 12$ when $x = 2$. Find $y$ when $x = 5$. "
               r"A: 30. B: 75. C: 150. D: 1.92.",
               r"**B**. $y = kx^2$, so $12 = 4k$ and $k = 3$. Then $y = 3 \times 25 = 75$. "
               r"A treats the variation as $y \propto x$; D uses inverse variation."),
            PQ(r"Find the magnitude of the vector $\begin{pmatrix} 5 \\ -12 \end{pmatrix}$. A: 7. B: 13. C: 17. D: $\sqrt{119}$.",
               r"**B**. $\sqrt{5^2 + (-12)^2} = \sqrt{169} = 13$. Estimate first: the answer must be a little more "
               r"than 12, which removes A and D at once; 17 is $5 + 12$, which ignores Pythagoras."),
            PQ(r"ABCD is a cyclic quadrilateral with $\angle A = 74^\circ$. Find $\angle C$. "
               r"A: $16^\circ$. B: $74^\circ$. C: $106^\circ$. D: $286^\circ$.",
               r"**C**. Opposite angles of a cyclic quadrilateral add up to $180^\circ$: $180^\circ - 74^\circ = 106^\circ$. "
               r"D is impossible inside a quadrilateral, so it can be eliminated without any work."),
            SUM("Paper 1: 30% of the mark, 50 multiple-choice questions, 1.5 hours, so about 1.8 minutes per question.",
                "Work in two passes and make sure every question has an answer at the end.",
                "Eliminate options by substituting, by size and by units.",
                "Estimate before calculating, so you can spot an answer that is too big or too small.",
                "Sketch bearings, Venn diagrams and circles in the question booklet.",
                "Wrong options come from common mistakes: check your method, not just whether your number appears."),
        ],
    ),
    # ------------------------------------------------------------------ Paper 2
    lesson(
        module="Examination", topic="Paper 2",
        title="Paper 2: structured questions and setting out answers",
        slug="paper-2-structured-answers",
        minutes=25,
        summary="How Paper 2 works (structured core questions and optional multi-part problems, 2.5 hours, 70% of the "
                "mark) and how to set out answers: working, accuracy, units, geometric reasons and neat graphs.",
        objectives=[
            "Describe the format of Paper 2 and plan your 2.5 hours",
            "Set out multi-part answers with clear working and the stated accuracy and units",
            "Give a reason for every step in a geometry answer",
            "Draw a quadratic graph neatly and read values from it",
        ],
        key_concepts=["Paper 2 format", "Showing working", "Marks as a guide to length", "Accuracy and rounding",
                      "Units", "Geometric reasons", "Drawing graphs"],
        blocks=[
            H("Introduction"),
            T("Paper 2 is where most of your mark is earned. Questions come in parts (a), (b), (c) ... and the parts "
              "usually build on each other, like steps up to a house on a hill in Bamenda: each one gets you closer to the top."),
            D("Paper 2 counts for **70%** of the General Mathematics mark and lasts **2.5 hours** (150 minutes). It has "
              "**structured core questions** and **optional multi-part problems**.",
              title="Paper 2 at a glance",
              note="How many optional problems to answer, which instruments and calculators are allowed, and how to "
                   "present your script: check the current GCE Board instructions on the paper and from your teacher."),
            KEY("Using your 150 minutes", "Read the paper calmly before writing, then let the marks guide your time.",
                cards=[["Read and choose", "Read every question, then choose your optional problems before you start them."],
                       ["Marks guide length", "A part worth 1 mark needs a short answer. A part worth 4 or 5 marks needs several steps."],
                       ["Leave time to check", "Keep the last minutes to check units, accuracy and unanswered parts."]]),
            H("Show your working"),
            T("In a structured question the examiner reads your method, not only your final answer. Clear working lets "
              "them follow your reasoning, and a correct method with a slip at the end may still earn some credit. "
              "A bare answer that is wrong earns nothing. Write one step per line, with an equals sign that really means equal. Write the formula first, then "
              "substitute, then calculate. If a later part uses an earlier answer, use the unrounded value."),
            H("Accuracy and units"),
            D("Give the answer to the accuracy the question asks for (for example 3 significant figures, 1 decimal "
              "place, or the nearest degree). Keep more figures in your working and round **only at the end**. "
              "Always write the unit: FCFA, cm, cm², km, kg, degrees.",
              title="Rule for final answers"),
            EX("Worked example 1: a commercial arithmetic question with a model layout", intro=(
                "A moto-taxi costs 900 000 FCFA. Its value depreciates by 15% each year. (a) Find its value after 1 year. "
                "(b) Find its value after 3 years, to the nearest 100 FCFA. (c) Find the total loss in value over the 3 "
                "years as a percentage of the cost, to 1 decimal place."), steps=[
                S("(a) Multiplier for one year", math=r"100\% - 15\% = 85\% \;\Rightarrow\; \times 0.85"),
                S("(a) Value after 1 year", math=r"900\,000 \times 0.85 = 765\,000 \text{ FCFA}"),
                S("(b) Formula, then substitute", math=r"V = 900\,000 \times 0.85^3 = 552\,712.5"),
                S("(b) Round only now", math=r"V \approx 552\,700 \text{ FCFA}"),
                S("(c) Loss in value (use the unrounded value)", math=r"900\,000 - 552\,712.5 = 347\,287.5 \text{ FCFA}"),
                S("(c) Percentage of the cost", math=r"\frac{347\,287.5}{900\,000} \times 100\% = 38.6\%"),
            ], check=r"1 - 0.85^3 = 0.385875 \approx 38.6\%"),
            H("Reasons in geometry"),
            T("In geometry, every angle you find needs a **reason**: the name of the theorem or fact you used. Write "
              "the reason in words beside the calculation, for example 'angle at the centre is twice the angle at the circumference'."),
            IMG("f5-centre-angle-cyclic.svg",
                alt="Circle with centre O and points A, B, C, D on it, with B at the bottom on the minor arc AC and D at "
                    "the top. Radii OA and OC make an angle of 140 degrees at O. Angles ADC and ABC are marked with question marks.",
                caption="Figure 1. Worked example 2: angle AOC = 140°, with B on the minor arc AC."),
            EX("Worked example 2: circle theorems with reasons", intro=(
                r"In Figure 1, O is the centre of the circle and $\angle AOC = 140^\circ$. (a) Find $\angle ADC$, giving "
                r"a reason. (b) Find $\angle ABC$, giving a reason. (c) Find $\angle OAC$, giving a reason."), steps=[
                S("(a) Calculation", math=r"\angle ADC = \tfrac{1}{2} \times 140^\circ = 70^\circ"),
                S("(a) Reason", text="The angle at the centre is twice the angle at the circumference standing on the same arc AC."),
                S("(b) Calculation", math=r"\angle ABC = 180^\circ - 70^\circ = 110^\circ"),
                S("(b) Reason", text="Opposite angles of a cyclic quadrilateral add up to 180°."),
                S("(c) Calculation", math=r"\angle OAC = \frac{180^\circ - 140^\circ}{2} = 20^\circ"),
                S("(c) Reason", text="OA = OC (radii), so triangle OAC is isosceles and its base angles are equal; "
                                     "angles in a triangle add up to 180°."),
            ]),
            H("Drawing graphs neatly"),
            T("For a graph question: complete the table of values carefully, choose the scale the question gives (or a "
              "simple one that uses most of the grid), plot each point with a small cross, and join the points with a "
              "**smooth curve** drawn freehand, not with straight ruled lines. Label the curve with its equation."),
            EX("Worked example 3: a quadratic graph", intro=(
                r"(a) Complete a table of values for $y = x^2 - 2x - 3$ for $-2 \le x \le 4$. (b) Draw the graph. "
                r"(c) Use your graph to solve $x^2 - 2x - 3 = 0$. (d) State the minimum value of $y$."), steps=[
                S("(a) Table of values", text=r"$x$: −2, −1, 0, 1, 2, 3, 4. $y$: 5, 0, −3, −4, −3, 0, 5."),
                S("(a) Check one value by hand", math=r"x = -2: \; 4 + 4 - 3 = 5"),
                S("(b) Plot and join", text="Plot the seven points and join them with one smooth U-shaped curve. "
                                           "The curve is symmetrical about the line $x = 1$."),
                S("(c) Read where the curve meets the x-axis", math=r"x = -1 \text{ or } x = 3"),
                S("(d) Read the lowest point", text="The turning point is $(1, -4)$, so the minimum value of $y$ is $-4$."),
            ], check=r"(x + 1)(x - 3) = x^2 - 2x - 3"),
            GRAPH([1, -2, -3], alt="U-shaped parabola y = x squared minus 2x minus 3, crossing the x-axis at x = -1 and "
                                  "x = 3, with its lowest point at (1, -4).",
                  caption="Figure 2. Worked example 3: the curve cuts the x-axis at −1 and 3; the minimum point is (1, −4).",
                  xmin=-2.5, xmax=4.5, ymin=-5, ymax=6, roots=[-1, 3], label="y = x² − 2x − 3"),
            H("Common mistakes"),
            MISTAKE("Rounding in the middle of a question",
                    "Rounding 0.85³ to 0.61 gives 549 000 FCFA in worked example 1, which is not 552 700 FCFA. Keep the full value until the final line."),
            MISTAKE("Missing units or the wrong accuracy",
                    "An answer of '552 712.5' when the question asks for the nearest 100 FCFA, or a length with no unit, "
                    "is not a finished answer. Read the last words of each part again before moving on."),
            MISTAKE("Joining graph points with a ruler",
                    "A quadratic graph is a smooth curve. Straight segments give a pointed bottom and wrong readings near the turning point."),
            QUIZ("A part asks for a length 'correct to 3 significant figures'. Your calculator shows 12.3456. What should you write?",
                 ["12.3 cm", "12.35 cm", "12 cm", "12.346 cm"], 0,
                 "12.3456 to 3 significant figures is 12.3, and the answer needs its unit.",
                 hint="Count the figures from the first non-zero digit: 1, 2, 3 ...",
                 feedback=["", "That is 4 significant figures (or 2 decimal places).",
                           "That is only 2 significant figures.", "That is 5 significant figures."]),
            QUIZ(r"You found $\angle ABC = 110^\circ$ in a cyclic quadrilateral ABCD. Which reason should you write?",
                 ["Angles on a straight line add up to 180°",
                  "Opposite angles of a cyclic quadrilateral add up to 180°",
                  "Angles in the same segment are equal",
                  "The angle in a semicircle is 90°"], 1,
                 "B and D are opposite corners of the cyclic quadrilateral, so the angles there add up to 180°.",
                 hint="Where are B and D in the quadrilateral ABCD: next to each other or opposite?",
                 feedback=["There is no straight line through B in this question.", "",
                           "Angles in the same segment are equal to each other; here the two angles are supplementary, not equal.",
                           "No diameter is involved, so this theorem does not apply."]),
            H("Practice questions"),
            PQ("A farmer in Foumbot borrows 600 000 FCFA at 10% compound interest per year. (a) Find the amount owed "
               "after 2 years. (b) Find the interest after 2 years. (c) How much more is this than simple interest at 10% for 2 years?",
               r"(a) $600\,000 \times 1.1^2 = 726\,000$ FCFA. (b) $726\,000 - 600\,000 = 126\,000$ FCFA. "
               r"(c) Simple interest: $600\,000 \times 0.10 \times 2 = 120\,000$ FCFA, so the difference is $6\,000$ FCFA."),
            PQ(r"In triangle PQR, $PQ = 6$ cm, $PR = 9$ cm and $\angle QPR = 50^\circ$. (a) Find QR to 3 significant "
               r"figures. (b) Find the area of the triangle to 3 significant figures.",
               r"(a) Cosine rule: $QR^2 = 6^2 + 9^2 - 2(6)(9)\cos 50^\circ = 117 - 69.42 = 47.58$, so $QR = 6.90$ cm. "
               r"(b) Area $= \tfrac{1}{2}(6)(9)\sin 50^\circ = 20.7$ cm². Units are cm for a length and cm² for an area."),
            PQ("An arithmetic progression has first term 4 and common difference 3. (a) Find the 20th term. "
               "(b) Find the sum of the first 20 terms. (c) Which term is equal to 100?",
               r"(a) $u_{20} = 4 + 19 \times 3 = 61$. (b) $S_{20} = \frac{20}{2}(4 + 61) = 650$. "
               r"(c) $4 + (n - 1) \times 3 = 100 \Rightarrow n - 1 = 32 \Rightarrow n = 33$, so the 33rd term."),
            SUM("Paper 2: 70% of the mark, 2.5 hours, structured core questions and optional multi-part problems.",
                "Check the current GCE Board instructions for how many optional problems to answer and what equipment is allowed.",
                "Show working line by line: formula, substitution, answer.",
                "Use the marks of each part to judge how much to write.",
                "Round only at the end, to the stated accuracy, and always give units.",
                "Give a reason for every angle in geometry, and draw graphs as smooth, labelled curves."),
        ],
    ),
]
