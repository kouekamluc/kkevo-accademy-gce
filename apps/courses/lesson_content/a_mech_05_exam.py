"""A Level Pure Mathematics with Mechanics: the Examination lesson for Paper 3 (mechanics and probability).

KKEVO draft content for both the Lower Sixth and the Upper Sixth course. Exam facts follow the GCE Board's
2023 Advanced Level report; practice-paper timings are KKEVO practice settings, not official times.
Slug starts with mex-.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-mechanics", "lower-sixth"),
          ("pure-mathematics-with-mechanics", "upper-sixth")]

LESSONS = []

LESSONS.append(lesson(
    module="Examination", topic="Paper 3",
    title="Paper 3 strategy: the mechanics and probability paper",
    slug="mex-paper-3-strategy-mechanics-and-probability",
    minutes=22,
    summary="Read the question, state the model, set out working with a diagram and a named law, give answers with units and sensible accuracy, and check them, using the Board's comments on what candidates found hard.",
    objectives=[
        "Describe the format of Paper 3 as the Board's 2023 report gives it",
        "Read a mechanics question, draw the diagram and state the modelling assumptions",
        "Set out working that a marker can follow, with units and sensible accuracy",
        "Avoid the errors the Board's 2023 report records in mechanics and probability",
    ],
    key_concepts=["Paper 3", "Modelling assumptions", "Force diagram", "Units and accuracy", "Checking an answer"],
    blocks=[
        H("Introduction"),
        T("On exam day, many students know the mechanics and still lose marks. They start writing before they understand the question, they leave out a unit, or they skip the diagram. A paper on mechanics and probability rewards a calm routine as much as it rewards knowledge."),
        T("This lesson gives you that routine. It uses the Board's 2023 report to show what candidates found hard, so that you can avoid the same errors. It applies to both Lower and Upper Sixth: Paper 3 can draw on any of the mechanics and probability topics you have met."),
        H("What Paper 3 looks like"),
        KEY("From the Board's 2023 report", "The report describes the papers of Pure Mathematics with Mechanics as follows. Check the exact format of your own paper with your teacher.", cards=[
            ["Paper 3", "Eight essay-type questions on mechanics and probability. A candidate is expected to answer all of them, in three hours."],
            ["Paper 1, Section B", "Fifteen multiple-choice questions on mechanics and probability, after 35 questions of pure mathematics in Section A. All are compulsory."],
            ["KKEVO practice papers", "KKEVO's Paper 3 practice papers have eight numbered questions with about 20 auto-marked parts and a time limit of 150 minutes. These are KKEVO practice settings, not official times: they give about 7 minutes a part."],
            ["Topics named", "Differentiation of a displacement vector, connected particles, collisions and loss of kinetic energy, work, energy and power, projectiles, relative velocity, variable motion, centre of mass of a plane lamina, and elementary conditional probability."],
        ]),
        TIP("Exam link: Paper 3 is the mechanics-and-probability paper, and its topics are the ones in the Kinematics, Forces, Probability, Momentum, Energy and Statics modules of this course. Paper 1 Section B tests the same topics with multiple choice, so the habits below help in both papers."),
        H("The four-step routine"),
        D(r"Use the same four steps on every mechanics question: **Read**, **Model**, **Set out**, **Check**.",
          title="Read, model, set out, check", formula=r"\text{Read} \to \text{Model} \to \text{Set out} \to \text{Check}"),
        KEY("What to do at each step", "Spend a minute on the first two steps. It saves more time than it costs.", cards=[
            ["Read", "Underline the quantity asked for and the units. Note what is given and what is not. Read the last part first if the question is long: it tells you where the question is going."],
            ["Model", "Say what the words mean: a particle has no size; a light string has no mass; a smooth surface has no friction; an inextensible string does not stretch. Draw a large diagram and mark every force and distance."],
            ["Set out", "Name the law you are using (Newton's second law, conservation of momentum, the principle of moments). Write the equation, then substitute, then solve."],
            ["Check", "Does the answer have the right units and size? Does the sign make sense? Can you test it a second way?"],
        ]),
        D("**Particle**: a body treated as a point. **Light**: has negligible mass, so the tension is the same all along a string. **Smooth**: no friction. **Inextensible**: the length of the string does not change, so connected particles have the same speed. **Uniform**: the mass is evenly spread, so the weight acts at the centre. **Rigid**: does not bend.",
          title="Words that tell you the model", note="Use $g = 9.8\\ \\text{m/s}^2$ unless the question tells you to use another value, and say so in your answer."),
        H("Setting out a solution"),
        CODE("""Question: 4 kg particle A on a smooth table, joined over a
smooth pulley to a 2 kg particle B hanging.

1. Diagram: forces on A (T, weight, normal reaction)
            forces on B (T, weight)
2. Model:   smooth, light inextensible string, g = 9.8
3. Equations:
   B (Newton's 2nd law):  2g - T = 2a
   A (Newton's 2nd law):  T = 4a
4. Solve:   2g = 6a, so a = 3.27 m/s^2, T = 13.1 N
5. Check:   a < g, as it must be, and T < weight of B.""", "text", title="A model layout (not a real exam answer)"),
        EX("Worked example 1: the force on a pulley", intro="A particle A of mass 4 kg rests on a smooth horizontal table. A light inextensible string attached to A passes over a smooth pulley at the edge of the table and carries a particle B of mass 2 kg hanging freely. The system is released from rest. Find the force exerted by the string on the pulley. Use $g = 9.8$.", steps=[
            S("Acceleration of the system", math=r"2g = (4 + 2)a \ \Rightarrow\ a = \frac{19.6}{6} = 3.267\ \text{m/s}^2"),
            S("Tension, from particle A alone", math=r"T = 4a = 13.07\ \text{N}"),
            S("Think about the pulley", text="Two parts of the same string meet at the pulley, each pulling with tension $T$. One part is horizontal (towards A) and the other is vertical (towards B), so they are at $90^\\circ$."),
            S("Add the two tensions as vectors", math=r"\sqrt{T^2 + T^2} = T\sqrt{2} = 13.07 \times 1.4142 = 18.5\ \text{N}", text="The force on the pulley is **18.5 N**, at $45^\\circ$ below the horizontal, pointing back over the table and downwards."),
        ], check=r"\text{It is less than } 2T = 26.1\ \text{N, the value for parallel strings, as it must be: } \checkmark"),
        MISTAKE("Using Newton's second law on the pulley", "The Board's 2023 report records that many candidates did not use the angle between the two parts of the string. They used the masses and the acceleration, as if the pulley were a moving particle. The pulley is fixed. The force on it is the **vector sum** of the two tensions, so the angle between the strings decides its size."),
        EX("Worked example 2: a ball and a wall", intro="A ball of mass 0.5 kg hits a smooth fixed wall at right angles at 8 m/s. The coefficient of restitution is 0.6. Find the speed after the impact and the kinetic energy lost.", steps=[
            S("The wall does not move", text="So the ball rebounds with speed $e \\times 8$. Newton's law of restitution applies to the speed of approach and separation."),
            S("Speed after impact", math=r"v = 0.6 \times 8 = 4.8\ \text{m/s}"),
            S("Kinetic energy from the definition", math=r"\tfrac12(0.5)(8)^2 - \tfrac12(0.5)(4.8)^2 = 16 - 5.76"),
            S("Loss", math=r"10.24\ \text{J}", text="The kinetic energy lost is **10.2 J** (3 s.f.)."),
        ]),
        MISTAKE("Not seeing the wall as a collision", "The Board's 2023 report notes that some candidates could not use the idea of a collision with a wall, and that some used a wrong kinetic-energy formula instead of working from the definition. Treat the wall as a very heavy particle that does not move, and always use $\\frac12 mv^2$ before and after."),
        EX("Worked example 3: independent or mutually exclusive?", intro=r"Events $A$ and $B$ have $P(A) = 0.3$ and $P(B) = 0.5$. Find $P(A \cup B)$ (a) if $A$ and $B$ are independent, (b) if they are mutually exclusive. (c) In case (a), find $P(A \mid B)$.", steps=[
            S("(a) Independent", math=r"P(A \cap B) = 0.3 \times 0.5 = 0.15 \Rightarrow P(A \cup B) = 0.3 + 0.5 - 0.15 = 0.65"),
            S("(b) Mutually exclusive", math=r"P(A \cap B) = 0 \Rightarrow P(A \cup B) = 0.3 + 0.5 = 0.8"),
            S("(c) Conditional probability, using independence", math=r"P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.15}{0.5} = 0.3 = P(A)", text="For independent events, knowing that $B$ has happened does not change the probability of $A$."),
        ]),
        MISTAKE("Confusing the two ideas", r"The Board's 2023 report records that many candidates could not use independent and mutually exclusive events correctly. **Independent** means $P(A \cap B) = P(A)P(B)$. **Mutually exclusive** means $P(A \cap B) = 0$. If both events have non-zero probability, they cannot be both."),
        MISTAKE("Using the wrong quantity in a moment", "The report notes that some candidates used the wrong quantity to find a moment. The moment of a force is the force times its **perpendicular** distance from the point. Resolve the force or draw the perpendicular before you multiply."),
        H("Units, accuracy and the last line"),
        D("Give every answer with its SI unit. Give 3 significant figures unless the question asks for something else (angles to 1 decimal place of a degree are usual). Keep full calculator values in the middle of the working and round only the final answer. If the question says to use $g = 10$, say that you used it.",
          title="Units and precision"),
        KEY("Last-minute checks", "Spend the last minutes of each question on these.", cards=[
            ["Units", "N for force, J for energy, W for power, m/s for speed, N s for impulse, N m for a moment."],
            ["Size", "Is the answer sensible? A car does not have an acceleration of 50 m/s$^2$ on a normal road."],
            ["Sign and direction", "Say which way a velocity or an impulse points. A negative sign is a direction."],
            ["Second method", "Test a result by energy if you used forces, or by moments about a second point."],
        ]),
        H("Quick checks"),
        QUIZ(r"Two events $A$ and $B$ have non-zero probabilities and are independent. Which statement is true?",
             ["They must be mutually exclusive", "They cannot be mutually exclusive", "They are mutually exclusive if $P(A) + P(B) < 1$", "They are mutually exclusive if $P(A \\cup B) = 1$"], 1,
             r"Independence gives $P(A \cap B) = P(A)P(B) > 0$, but mutually exclusive events have $P(A \cap B) = 0$.",
             hint="Compare the two values of P(A and B).",
             feedback=["Independent events can occur together, so they are not exclusive.", "", "Mutual exclusivity depends on the intersection, not on the sum of the probabilities.", "The union being 1 says nothing about the intersection being 0."]),
        H("Practice questions"),
        PQ("A particle A of mass 3 kg rests on a smooth horizontal table and is joined by a light inextensible string over a smooth pulley at the edge to a particle B of mass 5 kg hanging freely. Find the magnitude of the force of the string on the pulley, in N to 3 significant figures. Use $g = 9.8$.",
           r"$5g = (3 + 5)a$, so $a = 6.125$ m/s$^2$. For A: $T = 3a = 18.375$ N. The two parts of the string are at $90^\circ$, so the force on the pulley is $T\sqrt{2} = 18.375 \times 1.4142 = 26.0$ N."),
        PQ(r"Ship P has velocity $12\mathbf{i}$ m/s and ship Q has velocity $5\mathbf{j}$ m/s ($\mathbf{i}$ east, $\mathbf{j}$ north). Find the speed of P relative to Q.",
           r"$\mathbf{v}_{P/Q} = \mathbf{v}_P - \mathbf{v}_Q = 12\mathbf{i} - 5\mathbf{j}$, with magnitude $\sqrt{144 + 25} = 13$ m/s. The velocity of P relative to Q points south of east."),
        PQ(r"$P(A) = 0.4$ and $P(B) = 0.25$. Find $P(A \cup B)$ if the events are (a) independent, (b) mutually exclusive.",
           r"(a) $P(A \cap B) = 0.4 \times 0.25 = 0.1$, so $P(A \cup B) = 0.4 + 0.25 - 0.1 = 0.55$. (b) $P(A \cap B) = 0$, so $P(A \cup B) = 0.65$."),
        H("Summary"),
        SUM("Paper 3, per the Board's 2023 report, is eight essay-type questions on mechanics and probability, all to be answered. Check the exact format with your teacher.",
            "Use four steps: read, model, set out, check. Draw a diagram and state the model before you write equations.",
            "Name the law you use, write the equation, then substitute. Give every answer with a unit and about 3 significant figures.",
            "Avoid the errors the Board records: forgetting the angle at a pulley, wrong kinetic energy, wrong distance in a moment, mixing up independent and mutually exclusive.",
            "Check each answer for units, size and direction, and by a second method if you have time."),
    ],
))
