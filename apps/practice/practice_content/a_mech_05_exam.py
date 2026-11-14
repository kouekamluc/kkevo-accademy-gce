"""A Level Pure Mathematics with Mechanics: practice set for the Paper 3 strategy lesson (both years).

KKEVO draft content. g = 9.8 m/s^2 unless a question says otherwise.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-mechanics", "lower-sixth"),
          ("pure-mathematics-with-mechanics", "upper-sixth")]

SLUG = "mex-paper-3-strategy-mechanics-and-probability"

P3_TECHNIQUE = [
    MC(r"According to the Board's 2023 report, what is the format of the mechanics-and-probability paper (Paper 3)?", [
        C(r"Eight essay-type questions, all compulsory", correct=True),
        C(r"Fifty multiple-choice questions", why=r"That is Paper 1. Paper 3 is essay type."),
        C(r"Ten essay-type questions on pure mathematics", why=r"Pure mathematics only is Paper 2, which has ten essay-type questions."),
        C(r"Eight questions, of which you choose five", why=r"The report says candidates are expected to answer all the questions."),
    ], steps=[S(r"Paper 3", text=r"The report describes eight essay-type questions on mechanics and probability, all to be answered.")],
       concept=r"Paper 3 format", skill=r"Recall", hint=r"Think about which paper has which format."),
    NUM(r"A particle A of mass 4 kg is on a smooth horizontal table, joined by a light string over a smooth pulley at the table edge to a particle B of mass 2 kg hanging freely. Find the magnitude of the force of the string on the pulley, in N to 2 decimal places. Use $g = 9.8$.", 18.48, steps=[S(r"Acceleration", text=r"$2g = (4 + 2)a \Rightarrow a = 3.267$ m/s$^2$"), S(r"Tension", text=r"$T = 4a = 13.07$ N"), S(r"The two parts of the string are at $90^\circ$", text=r"$\sqrt{T^2 + T^2} = T\sqrt{2} = 18.48$ N")],
        tolerance=0.05, unit=r"N", concept=r"Force on a pulley", skill=r"Reasoning", hint=r"The force on the pulley is the vector sum of two equal tensions at 90 degrees to each other."),
    NUM(r"A ball of mass 0.5 kg hits a smooth wall at right angles at 8 m/s and rebounds at 4.8 m/s. Find the kinetic energy lost, in joules to 2 decimal places.", 10.24, steps=[S(r"Before", text=r"$\frac12(0.5)(8)^2 = 16$ J"), S(r"After", text=r"$\frac12(0.5)(4.8)^2 = 5.76$ J"), S(r"Loss", text=r"$16 - 5.76 = 10.24$ J")],
        tolerance=0.01, unit=r"J", concept=r"Kinetic energy lost", skill=r"Calculation", hint=r"Use the definition of kinetic energy before and after."),
    MC(r"$P(A) = 0.3$, $P(B) = 0.5$ and $A$ and $B$ are independent. Find $P(A \cup B)$.", [
        C(r"$0.8$", why=r"This adds the probabilities, which is only right for mutually exclusive events."),
        C(r"$0.65$", correct=True),
        C(r"$0.15$", why=r"This is $P(A \cap B) = P(A)P(B)$, not the union."),
        C(r"$0.35$", why=r"You subtracted the intersection from one of the probabilities."),
    ], steps=[S(r"Independent", math=r"P(A \cap B) = 0.3 \times 0.5 = 0.15"), S(r"Addition law", math=r"P(A \cup B) = 0.3 + 0.5 - 0.15 = 0.65")],
       concept=r"Independent events", skill=r"Application", hint=r"Work out the intersection for independent events before using the addition law."),
    MC(r"Two events $A$ and $B$ both have non-zero probabilities and are independent. Which statement is correct?", [
        C(r"They must be mutually exclusive", why=r"Independence gives $P(A \cap B) = P(A)P(B) > 0$, so the events can both occur."),
        C(r"They are mutually exclusive if $P(A) + P(B) < 1$", why=r"Mutual exclusivity depends on the intersection being zero, not on the sum of the probabilities."),
        C(r"They cannot be mutually exclusive", correct=True),
        C(r"They can be mutually exclusive if $P(A \mid B) = P(A)$", why=r"If $P(A \mid B) = P(A)$ and the probabilities are positive, then $P(A \cap B) > 0$, so they are not mutually exclusive."),
    ], steps=[S(r"Independent", text=r"$P(A \cap B) = P(A)P(B)$, which is positive if both are positive"), S(r"Mutually exclusive", text=r"needs $P(A \cap B) = 0$, a contradiction")],
       concept=r"Independent or exclusive", skill=r"Concept", hint=r"What is P(A and B) in each case?"),
    NUM(r"A force of 30 N acts at the end P of a rod OP of length 0.8 m, at $35^\circ$ to the rod. Find the moment of the force about O, in N m to 2 decimal places.", 13.77, steps=[S(r"Perpendicular distance", text=r"$0.8\sin 35^\circ = 0.4588$ m"), S(r"Moment", text=r"$30 \times 0.4588 = 13.77$ N m")],
        tolerance=0.02, unit=r"N m", concept=r"Moment of a force", skill=r"Calculation", hint=r"The distance in a moment is perpendicular to the line of the force."),
    MC(r"A candidate finds $v = \sqrt{50}$ m/s on a calculator. Which is the best way to give the final answer?", [
        C(r"$v = 7.0710678$", why=r"This has no unit and far more figures than the data support."),
        C(r"$v = 7$", why=r"This has no unit and is rounded too early to show the accuracy of the working."),
        C(r"$v = 7.07$ m", why=r"The unit is wrong: speed is in metres per second."),
        C(r"$v = 7.07$ m/s (to 3 significant figures)", correct=True),
    ], steps=[S(r"Give a unit and a sensible accuracy", text=r"3 significant figures with the SI unit: 7.07 m/s")],
       concept=r"Units and accuracy", skill=r"Concept", hint=r"A final answer needs a unit and a stated accuracy."),
    NUM(r"Ship A moves at 10 m/s due east and ship B at 6 m/s due north. Find the speed of A relative to B, in m/s to 1 decimal place.", 11.7, steps=[S(r"Relative velocity", math=r"\mathbf{v}_{A/B} = \mathbf{v}_A - \mathbf{v}_B = 10\mathbf{i} - 6\mathbf{j}"), S(r"Speed", text=r"$\sqrt{100 + 36} = \sqrt{136} = 11.7$ m/s")],
        tolerance=0.05, unit=r"m/s", concept=r"Relative velocity", skill=r"Application", hint=r"Subtract the velocity of B, then find the magnitude."),
]

SETS = [
    practice_set(module="Examination", topic="Paper 3", title="Paper 3 technique: reading, modelling and checking",
                 lesson=SLUG, questions=P3_TECHNIQUE),
]
