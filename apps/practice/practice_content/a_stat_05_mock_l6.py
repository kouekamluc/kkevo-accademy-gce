"""Pure Mathematics with Statistics (A Level), Lower Sixth: two mock papers.

KKEVO draft content. Timings are KKEVO practice settings, not official examination times. All data are invented
for practice; no question is taken from a past paper.
Paper 3 practice paper A: about 24 auto-markable parts (multiple choice and numeric) in 8 numbered questions on descriptive statistics, probability and discrete random variables.
Paper 1 mock exam B: 50 four-option multiple-choice questions, 35 on pure mathematics (Section A) and 15 on the
option topics of this year (Section B). Every concept is the exact topic title of the course outline.
"""

from .dsl import *  # noqa: F403

COURSE = ("pure-mathematics-with-statistics", "lower-sixth")

LESSON = "sex-paper-3-statistics-strategy"
LESSON_P1 = "pv-exam-paper-1-multiple-choice-strategy"  # the shared Paper 1 lesson; the Paper 3 lesson is in topic Paper 3

# The position of the correct option cycles through permutations so that A, B, C and D are each correct 12 or 13 times.
_POS = [0, 1, 2, 3, 2, 3, 0, 1, 1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 1, 3, 0, 2, 2, 0, 3, 1, 3, 1, 2, 0, 0, 3, 2, 1, 2, 1, 0, 3, 1, 3, 0, 2, 2, 0, 3, 1, 0, 2]

B_QUESTIONS = []


def _q(prompt, right, wrongs, steps, concept, skill, hint):
    """Add one four-option question; `wrongs` is a list of three (text, why) pairs."""
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(_POS[len(B_QUESTIONS)], C(right, correct=True))
    B_QUESTIONS.append(MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint))


# ---- Section A, pure mathematics (35 questions). Concept = the core topic title.
# ---- Proof (3)
_q(r"In a proof by induction that $\displaystyle\sum_{r=1}^{n}(3r - 2) = \frac{n(3n - 1)}{2}$, the inductive step assumes the result for $n = k$ and adds the next term. Which term is added?",
   r"$3k + 1$",
   [(r"$3k - 2$", "This is the $k$th term, already included in the sum for $n = k$."),
    (r"$3k + 3$", "The $(k+1)$th term is $3(k + 1) - 2 = 3k + 1$: you forgot to subtract $2$."),
    (r"$3k - 1$", "Substituting $k + 1$ into $3r - 2$ gives $3k + 1$, not $3k - 1$.")],
   [S("The $r$th term is $3r - 2$", text=r"The next term has $r = k + 1$."), S("Substitute", math=r"3(k + 1) - 2 = 3k + 1")],
   "Proof", "Calculation", "Which value of r gives the new term?")
_q(r"To prove by contradiction that the sum of a rational number $r$ and an irrational number $s$ is irrational, which assumption should be made first?",
   r"$r + s$ is rational",
   [(r"$r + s$ is irrational", "That is what we want to prove. A contradiction proof assumes the opposite."),
    (r"$r$ and $s$ are both rational", "$s$ is given as irrational; the assumption must be about the sum $r + s$."),
    (r"$s = \dfrac{a}{b}$ in lowest terms", "This describes a rational number, but $s$ is irrational by hypothesis.")],
   [S("Negate the conclusion", text="The claim is '$r + s$ is irrational'. Assume it is rational."), S("Then", math=r"s = (r + s) - r \text{ would be rational}", text="This contradicts the fact that $s$ is irrational.")],
   "Proof", "Concept", "What is the opposite of the statement you want to prove?")
_q(r"A proof by induction shows that $f(n) = 7^n - 1$ is divisible by $6$. Which of these equals $f(k+1) - 7f(k)$?",
   "$6$",
   [("$0$", "Expand: $7^{k+1} - 1 - 7(7^k - 1) = 7^{k+1} - 1 - 7^{k+1} + 7$, which is $6$, not $0$."),
    (r"$7^k - 1$", "This is just $f(k)$. The $7^{k+1}$ terms cancel."),
    (r"$-8$", "Check the signs: $-1 - (-7) = +6$.")],
   [S("Expand", math=r"f(k+1) - 7f(k) = (7^{k+1} - 1) - 7(7^k - 1)"), S("Simplify", math=r"= -1 + 7 = 6")],
   "Proof", "Calculation", "Write f(k+1) and 7f(k) in full and subtract.")

# ---- Algebra (3)
_q(r"Express $\dfrac{3x + 5}{(x + 1)(x + 3)}$ in partial fractions.",
   r"$\dfrac{1}{x + 1} + \dfrac{2}{x + 3}$",
   [(r"$\dfrac{2}{x + 1} + \dfrac{1}{x + 3}$", "The constants are swapped: at $x = -1$ the numerator is $2 = 2A$, so $A = 1$."),
    (r"$\dfrac{1}{x + 1} - \dfrac{2}{x + 3}$", "At $x = -3$: $-4 = -2B$, so $B = +2$."),
    (r"$\dfrac{3}{x + 1} + \dfrac{5}{x + 3}$", "These are the coefficients of the numerator, not the constants found from the identity.")],
   [S("Identity", math=r"3x + 5 = A(x + 3) + B(x + 1)"), S("$x = -1$", math=r"2 = 2A \Rightarrow A = 1"), S("$x = -3$", math=r"-4 = -2B \Rightarrow B = 2")],
   "Algebra", "Calculation", "Put x = -1 and x = -3 in the identity.")
_q(r"Find the coefficient of $x^2$ in the expansion of $(1 + 2x)^{-1/2}$.",
   r"$\dfrac{3}{2}$",
   [(r"$\dfrac{3}{8}$", "You omitted the factor $2^2 = 4$ from $(2x)^2$."),
    (r"$-\dfrac{3}{2}$", r"$(-\tfrac{1}{2})(-\tfrac{3}{2}) = +\tfrac{3}{4}$ is positive."),
    (r"$\dfrac{3}{4}$", r"You omitted the $\frac{1}{2!}$: the term is $\frac{(-\frac12)(-\frac32)}{2!}(2x)^2$.")],
   [S("Binomial series", math=r"\frac{(-\frac12)(-\frac32)}{2!}(2x)^2 = \frac{3}{8} \times 4x^2"), S("Coefficient", math=r"\frac{3}{2}")],
   "Algebra", "Calculation", "Use the binomial series for a rational index, with (2x) in place of x.")
_q(r"$\alpha$ and $\beta$ are the roots of $x^2 - 4x + 2 = 0$. Find $\alpha^3 + \beta^3$.",
   "$40$",
   [("$58$", r"This is $(\alpha + \beta)^3 - 3\alpha\beta = 64 - 6$. The correct identity has $3\alpha\beta(\alpha + \beta)$."),
    ("$12$", r"This is $\alpha^2 + \beta^2$, not $\alpha^3 + \beta^3$."),
    ("$48$", r"You used $2\alpha\beta(\alpha + \beta) = 16$ instead of $3\alpha\beta(\alpha + \beta) = 24$.")],
   [S("Sum and product", math=r"\alpha + \beta = 4, \quad \alpha\beta = 2"), S("Identity", math=r"\alpha^3 + \beta^3 = (\alpha + \beta)^3 - 3\alpha\beta(\alpha + \beta)"), S("Substitute", math=r"64 - 24 = 40")],
   "Algebra", "Calculation", "Use the cube of the sum and expand.")

# ---- Functions and graphs (3)
_q(r"$f(x) = x^2 + 1$ and $g(x) = 2x - 3$. Find $fg(2)$.",
   "$2$",
   [("$7$", "This is $gf(2)$. $fg(2)$ means apply $g$ first, then $f$."),
    ("$5$", "This is $f(2)$ alone."),
    ("$1$", "This is $g(2)$ alone, before applying $f$.")],
   [S("Apply $g$ first", math=r"g(2) = 1"), S("Then $f$", math=r"f(1) = 1^2 + 1 = 2")],
   "Functions and graphs", "Calculation", "Work from the inside: g first.")
_q(r"$f(x) = \dfrac{3x - 2}{x + 1}$, $x \neq -1$. Find $f^{-1}(x)$.",
   r"$\dfrac{x + 2}{3 - x}$",
   [(r"$\dfrac{x + 2}{x - 3}$", r"Sign error: $y(x + 1) = 3x - 2$ gives $x(y - 3) = -(y + 2)$, so $x = \dfrac{y + 2}{3 - y}$."),
    (r"$\dfrac{x + 1}{3x - 2}$", "This is the reciprocal of $f(x)$, which is not the inverse."),
    (r"$\dfrac{3x + 2}{x - 1}$", "You swapped the signs in $f$ but did not solve for $x$.")],
   [S("Write $y$ and solve for $x$", math=r"y(x + 1) = 3x - 2 \Rightarrow yx + y = 3x - 2"), S("Collect $x$", math=r"x(y - 3) = -2 - y \Rightarrow x = \frac{y + 2}{3 - y}"), S("Swap the letters", math=r"f^{-1}(x) = \frac{x + 2}{3 - x}")],
   "Functions and graphs", "Calculation", "Put y = f(x), make x the subject, then rename.")
_q(r"The curve $y = \dfrac{x^2 + 2x}{x - 1}$ has an oblique asymptote. Which is it?",
   r"$y = x + 3$",
   [(r"$y = x + 2$", "Divide properly: $x^2 + 2x = (x - 1)(x + 3) + 3$. The quotient is $x + 3$."),
    (r"$y = x - 1$", "$x - 1$ is the denominator, not the quotient."),
    (r"$y = x + 1$", "Check by dividing again: $(x - 1)(x + 1) = x^2 - 1$ leaves $2x + 1$, not a constant.")],
   [S("Divide", math=r"x^2 + 2x = (x - 1)(x + 3) + 3"), S("Rewrite", math=r"y = x + 3 + \frac{3}{x - 1}"), S("The fraction tends to 0", text="So the oblique asymptote is $y = x + 3$.")],
   "Functions and graphs", "Calculation", "Divide the numerator by x - 1.")

# ---- Identities (4)
_q(r"Find the exact value of $\cos 105^\circ$.",
   r"$\dfrac{\sqrt{2} - \sqrt{6}}{4}$",
   [(r"$\dfrac{\sqrt{6} - \sqrt{2}}{4}$", r"This is $\cos 75^\circ$. $105^\circ$ is in the second quadrant, so the cosine is negative."),
    (r"$\dfrac{\sqrt{6} + \sqrt{2}}{4}$", r"This is $\cos 15^\circ$, from using a plus sign in the compound formula: $\cos(A + B)$ has a minus sign between the products."),
    (r"$-\dfrac{\sqrt{6} + \sqrt{2}}{4}$", r"This is $\cos 165^\circ$. Since $105^\circ$ is only $15^\circ$ past $90^\circ$, its cosine is small.")],
   [S("Compound angle", math=r"\cos(60^\circ + 45^\circ) = \cos 60^\circ\cos 45^\circ - \sin 60^\circ\sin 45^\circ"),
    S("Substitute", math=r"= \frac{1}{2}\cdot\frac{\sqrt{2}}{2} - \frac{\sqrt{3}}{2}\cdot\frac{\sqrt{2}}{2} = \frac{\sqrt{2} - \sqrt{6}}{4}")],
   "Identities", "Calculation", "Write 105 degrees as 60 degrees plus 45 degrees.")
_q(r"$\tan\theta = \dfrac{3}{4}$ and $\theta$ is acute. Find $\sin 2\theta$.",
   r"$\dfrac{24}{25}$",
   [(r"$\dfrac{12}{25}$", r"You omitted the factor $2$ in $\sin 2\theta = 2\sin\theta\cos\theta$."),
    (r"$\dfrac{7}{25}$", r"This is $\cos 2\theta = \cos^2\theta - \sin^2\theta$."),
    (r"$\dfrac{24}{7}$", r"This is $\tan 2\theta$, not $\sin 2\theta$.")],
   [S("Right-angled triangle $3, 4, 5$", math=r"\sin\theta = \frac{3}{5}, \quad \cos\theta = \frac{4}{5}"), S("Double angle", math=r"\sin 2\theta = 2 \times \frac{3}{5} \times \frac{4}{5} = \frac{24}{25}")],
   "Identities", "Calculation", "Draw the triangle to find sin and cos, then use the double-angle formula.")
_q(r"Find the maximum value of $5\cos\theta + 12\sin\theta + 4$.",
   "$17$",
   [("$13$", r"The maximum of $5\cos\theta + 12\sin\theta$ is $R = 13$, but the constant $4$ must be added."),
    ("$21$", "You added the coefficients, $5 + 12 + 4$. The maximum uses $R = \\sqrt{5^2 + 12^2}$."),
    ("$9$", "This is the least value $-13 + 4$, not the greatest.")],
   [S("Harmonic form", math=r"5\cos\theta + 12\sin\theta = R\cos(\theta - \alpha), \quad R = \sqrt{25 + 144} = 13"), S("Greatest value of the cosine is 1", math=r"13 + 4 = 17")],
   "Identities", "Application", "Write the first two terms as R cos(theta - alpha).")
_q(r"Solve $\sin 2\theta = \sin\theta$ for $0^\circ \leq \theta \leq 180^\circ$.",
   r"$\theta = 0^\circ,\ 60^\circ,\ 180^\circ$",
   [(r"$\theta = 60^\circ$ only", "You cancelled $\\sin\\theta$ from both sides, which loses the solutions where $\\sin\\theta = 0$."),
    (r"$\theta = 0^\circ,\ 60^\circ$", "$\\theta = 180^\\circ$ also gives $\\sin\\theta = 0$ and $\\sin 360^\\circ = 0$."),
    (r"$\theta = 60^\circ,\ 120^\circ$", "$\\sin 240^\\circ \\neq \\sin 120^\\circ$. Factorise instead: $\\sin\\theta(2\\cos\\theta - 1) = 0$.")],
   [S("Double angle", math=r"2\sin\theta\cos\theta - \sin\theta = 0"), S("Factorise", math=r"\sin\theta(2\cos\theta - 1) = 0"), S("Solve each factor", math=r"\sin\theta = 0 \Rightarrow \theta = 0^\circ, 180^\circ; \quad \cos\theta = \tfrac{1}{2} \Rightarrow \theta = 60^\circ")],
   "Identities", "Reasoning", "Do not divide by sin theta: factorise.")

# ---- Conic sections (3)
_q(r"The circle $x^2 + y^2 + 2x - 10y + 10 = 0$ has centre $C$ and radius $r$. Find them.",
   r"$C = (-1, 5)$, $r = 4$",
   [(r"$C = (1, -5)$, $r = 4$", "The centre has the opposite signs to the coefficients: $(-\\tfrac{2}{2}, \\tfrac{10}{2})$."),
    (r"$C = (-1, 5)$, $r = 16$", "$16$ is $r^2$. Take the square root."),
    (r"$C = (-1, 5)$, $r = 6$", "$r^2 = 1 + 25 - 10 = 16$. You added $+10$ instead of subtracting the constant.")],
   [S("Complete the square", math=r"(x + 1)^2 + (y - 5)^2 = 1 + 25 - 10 = 16"), S("Read off", text="Centre $(-1, 5)$ and radius $\\sqrt{16} = 4$.")],
   "Conic sections", "Calculation", "Complete the square in x and in y.")
_q(r"A parabola has parametric equations $x = 2t^2$, $y = 4t$. Find its cartesian equation.",
   r"$y^2 = 8x$",
   [(r"$y^2 = 4x$", "$y^2 = 16t^2 = 8 \\times 2t^2$, so the constant is $8$."),
    (r"$y^2 = 16x$", "$y^2 = 16t^2$, but $x = 2t^2$, so $y^2 = 8x$."),
    (r"$x^2 = 8y$", r"This has $x$ and $y$ swapped: $y = 4t$ is the linear one, so the parabola opens along the $x$-axis.")],
   [S("Eliminate $t$", math=r"t = \frac{y}{4}"), S("Substitute", math=r"x = 2\cdot\frac{y^2}{16} = \frac{y^2}{8}"), S("Rearrange", math=r"y^2 = 8x")],
   "Conic sections", "Calculation", "Make t the subject of y = 4t and substitute into x.")
_q(r"The hyperbola $\dfrac{x^2}{16} - \dfrac{y^2}{9} = 1$ has foci at:",
   r"$(\pm 5, 0)$",
   [(r"$(\pm\sqrt{7}, 0)$", r"$a^2 - b^2$ is for an ellipse. For a hyperbola $c^2 = a^2 + b^2$."),
    (r"$(\pm 25, 0)$", "$25$ is $c^2$. Take the square root."),
    (r"$(\pm 4, 0)$", "These are the vertices at $x = \\pm a$, not the foci.")],
   [S("Hyperbola: $c^2 = a^2 + b^2$", math=r"c^2 = 16 + 9 = 25 \Rightarrow c = 5"), S("Foci", math=r"(\pm 5, 0)")],
   "Conic sections", "Recall", "For a hyperbola c squared is a squared plus b squared.")

# ---- Differentiation (4)
_q(r"The curve $y = x e^{-2x}$ has a stationary point. At which value of $x$?",
   r"$x = \dfrac{1}{2}$",
   [(r"$x = 2$", "Check: $\\frac{dy}{dx} = e^{-2x}(1 - 2x)$, which is zero when $1 - 2x = 0$."),
    (r"$x = 1$", "At $x = 1$: $\\frac{dy}{dx} = -e^{-2} \\neq 0$."),
    (r"$x = -\dfrac{1}{2}$", "The sign of the bracket: $1 - 2x = 0$ gives $x = +\\frac{1}{2}$.")],
   [S("Product rule", math=r"\frac{dy}{dx} = e^{-2x} + x(-2e^{-2x}) = e^{-2x}(1 - 2x)"), S("Set to zero", math=r"1 - 2x = 0 \Rightarrow x = \frac{1}{2}", text="$e^{-2x}$ is never zero.")],
   "Differentiation", "Calculation", "Use the product rule, then factorise.")
_q(r"A curve has equation $x^2 + 3xy = 10$. Find $\dfrac{dy}{dx}$ at the point $(1, 3)$.",
   r"$-\dfrac{11}{3}$",
   [(r"$-\dfrac{2}{3}$", "You differentiated $3xy$ as $3y'$ and lost the term $3y$: use the product rule on $xy$."),
    (r"$\dfrac{11}{3}$", "Sign error: $11 + 3y' = 0$ gives $y' = -\\frac{11}{3}$."),
    (r"$-\dfrac{11}{9}$", r"You divided by $3y = 9$ instead of $3x = 3$: the term in $\frac{dy}{dx}$ is $3x\frac{dy}{dx}$.")],
   [S("Differentiate implicitly", math=r"2x + 3y + 3x\frac{dy}{dx} = 0"), S("At $(1, 3)$", math=r"2 + 9 + 3\frac{dy}{dx} = 0"), S("Solve", math=r"\frac{dy}{dx} = -\frac{11}{3}")],
   "Differentiation", "Calculation", "Use the product rule on the term 3xy.")
_q(r"A curve has parametric equations $x = t^2$, $y = t^3 - 3t$. Find $\dfrac{dy}{dx}$ when $t = 2$.",
   r"$\dfrac{9}{4}$",
   [(r"$\dfrac{4}{9}$", r"You inverted: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$, with $\frac{dy}{dt}$ on top."),
    (r"$3$", "You forgot the $-3$ in $\\frac{dy}{dt} = 3t^2 - 3$."),
    (r"$\dfrac{9}{2}$", "$\\frac{dx}{dt} = 2t = 4$, not $2$.")],
   [S("Differentiate each", math=r"\frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2 - 3"), S("Divide", math=r"\frac{dy}{dx} = \frac{3t^2 - 3}{2t}"), S("At $t = 2$", math=r"\frac{12 - 3}{4} = \frac{9}{4}")],
   "Differentiation", "Calculation", "Divide dy/dt by dx/dt.")
_q(r"Differentiate $y = \dfrac{e^x}{x + 1}$ and evaluate at $x = 1$.",
   r"$\dfrac{e}{4}$",
   [(r"$\dfrac{e}{2}$", "You divided by $(x + 1)$ instead of $(x + 1)^2$ (the quotient rule squares the denominator)."),
    (r"$e$", "At $x = 1$, $x e^x/(x + 1)^2 = e/4$. You did not divide by the square of the denominator."),
    (r"$\dfrac{3e}{4}$", "The numerator is $e^x(x + 1) - e^x = xe^x$. You added instead of subtracting.")],
   [S("Quotient rule", math=r"\frac{dy}{dx} = \frac{e^x(x + 1) - e^x\cdot 1}{(x + 1)^2} = \frac{xe^x}{(x + 1)^2}"), S("At $x = 1$", math=r"\frac{e}{4}")],
   "Differentiation", "Calculation", "Use the quotient rule: (vu' - uv') over v squared.")

# ---- Series (3)
_q(r"Find the coefficient of $x^3$ in the Maclaurin series of $\sin 3x$.",
   r"$-\dfrac{9}{2}$",
   [(r"$\dfrac{9}{2}$", r"The series of $\sin u$ is $u - \frac{u^3}{3!} + \dots$: the $u^3$ term is negative."),
    (r"$-\dfrac{3}{2}$", "Replace $u$ by $3x$: $(3x)^3 = 27x^3$, not $3x^3$."),
    (r"$-27$", "You forgot the $3! = 6$: $-\\frac{27}{6} = -\\frac{9}{2}$.")],
   [S("Series of $\\sin u$", math=r"\sin u = u - \frac{u^3}{3!} + \dots"), S("Put $u = 3x$", math=r"\sin 3x = 3x - \frac{27x^3}{6} + \dots"), S("Coefficient", math=r"-\frac{27}{6} = -\frac{9}{2}")],
   "Series", "Calculation", "Replace u by 3x in the series of sin u.")
_q(r"Use the first three non-zero terms of the Maclaurin series $\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \dots$ to estimate $\ln 1.2$. Give your answer to 4 decimal places.",
   "$0.1827$",
   [("$0.1800$", "This uses only two terms. Add the term $\\frac{x^3}{3} = 0.00267$."),
    ("$0.2227$", "The signs alternate: the $x^2$ term is subtracted, not added."),
    ("$0.2000$", "This is just the first term.")],
   [S("Put $x = 0.2$", math=r"0.2 - \frac{0.04}{2} + \frac{0.008}{3}"), S("Calculate", math=r"0.2 - 0.02 + 0.00267 = 0.18267 \approx 0.1827")],
   "Series", "Application", "Substitute x = 0.2 into the three terms.")
_q(r"What is the coefficient of $(x - 2)^2$ in the Taylor series of $e^x$ about $x = 2$?",
   r"$\dfrac{e^2}{2}$",
   [(r"$e^2$", "You omitted the factor $\\frac{1}{2!}$ in $\\frac{f''(2)}{2!}$."),
    (r"$\dfrac{e^2}{4}$", "$f''(2) = e^2$ and $2! = 2$, not $4$."),
    (r"$\dfrac{1}{2}$", "Every derivative of $e^x$ at $x = 2$ is $e^2$, not $1$.")],
   [S("Taylor series", math=r"f(x) = f(2) + f'(2)(x - 2) + \frac{f''(2)}{2!}(x - 2)^2 + \dots"), S("All derivatives are $e^2$", math=r"\frac{e^2}{2!} = \frac{e^2}{2}")],
   "Series", "Calculation", "Find f''(2) and divide by 2 factorial.")

# ---- Integration (4)
_q(r"Find $\displaystyle\int x\ln x\,dx$.",
   r"$\dfrac{x^2}{2}\ln x - \dfrac{x^2}{4} + c$",
   [(r"$\dfrac{x^2}{2}\ln x - \dfrac{x^2}{2} + c$", r"After parts you must integrate $\frac{x}{2}$, which gives $\frac{x^2}{4}$."),
    (r"$\dfrac{x^2}{2}\ln x + \dfrac{x^2}{4} + c$", "The second term is subtracted in the integration by parts formula."),
    (r"$x\ln x - x + c$", "This is $\\int \\ln x\\,dx$, a different integral.")],
   [S("By parts: $u = \\ln x$, $dv = x\\,dx$", math=r"\int x\ln x\,dx = \frac{x^2}{2}\ln x - \int \frac{x^2}{2}\cdot\frac{1}{x}\,dx"), S("Integrate", math=r"= \frac{x^2}{2}\ln x - \frac{x^2}{4} + c")],
   "Integration", "Calculation", "Take u = ln x, so that it disappears after differentiating.")
_q(r"Evaluate $\displaystyle\int_0^1 \frac{x}{x^2 + 1}\,dx$.",
   r"$\dfrac{1}{2}\ln 2$",
   [(r"$\ln 2$", "The numerator $x$ is half the derivative of $x^2 + 1$, so a factor $\\frac{1}{2}$ is needed."),
    (r"$\dfrac{1}{2}$", "You integrated as if the denominator were constant."),
    (r"$\dfrac{\pi}{4}$", "That is $\\int_0^1 \\frac{1}{x^2 + 1}\\,dx$. Here the numerator is $x$.")],
   [S("Reverse chain rule", math=r"\int \frac{x}{x^2 + 1}\,dx = \frac{1}{2}\ln(x^2 + 1)"), S("Limits", math=r"\frac{1}{2}(\ln 2 - \ln 1) = \frac{1}{2}\ln 2")],
   "Integration", "Calculation", "The numerator is half the derivative of the denominator.")
_q(r"Evaluate $\displaystyle\int_0^{\pi/2} \sin x\cos^2 x\,dx$.",
   r"$\dfrac{1}{3}$",
   [(r"$\dfrac{1}{2}$", "You forgot to divide by the new power: $\\int u^2\\,du = \\frac{u^3}{3}$."),
    (r"$-\dfrac{1}{3}$", "With $u = \\cos x$, $du = -\\sin x\\,dx$, and the limits swap from $1$ to $0$, so the signs cancel."),
    (r"$\dfrac{2}{3}$", "$\\left[-\\frac{\\cos^3 x}{3}\\right]_0^{\\pi/2} = 0 + \\frac{1}{3}$, not $\\frac{2}{3}$.")],
   [S("Substitute $u = \\cos x$", math=r"du = -\sin x\,dx"), S("Limits", text=r"$x = 0$ gives $u = 1$; $x = \frac{\pi}{2}$ gives $u = 0$."), S("Integrate", math=r"\int_1^0 -u^2\,du = \left[-\frac{u^3}{3}\right]_1^0 = \frac{1}{3}")],
   "Integration", "Calculation", "Let u = cos x.")
_q(r"The region under $y = x^2$ between $x = 0$ and $x = 2$ is rotated through $2\pi$ about the $x$-axis. Find the volume.",
   r"$\dfrac{32\pi}{5}$",
   [(r"$\dfrac{32}{5}$", r"The volume formula is $\pi\int y^2\,dx$: do not forget $\pi$."),
    (r"$\dfrac{8\pi}{3}$", "You integrated $y = x^2$ instead of $y^2 = x^4$."),
    (r"$\dfrac{32\pi}{3}$", r"You integrated $x^4$ as $\frac{x^5}{3}$: the power rises to $5$ and you divide by $5$.")],
   [S("Formula", math=r"V = \pi\int_0^2 y^2\,dx = \pi\int_0^2 x^4\,dx"), S("Integrate", math=r"\pi\left[\frac{x^5}{5}\right]_0^2 = \frac{32\pi}{5}")],
   "Integration", "Application", "Square y first: y squared is x to the fourth.")

# ---- Differential equations (3)
_q(r"Given $\dfrac{dy}{dx} = 2xy$ and $y = 1$ when $x = 0$, find $y$ when $x = 1$.",
   "$e$",
   [("$2e$", "Check the constant: $\\ln y = x^2 + c$ with $y(0) = 1$ gives $c = 0$, so $y = e^{x^2}$."),
    ("$e^2$", "$y = e^{x^2}$; at $x = 1$ the exponent is $1^2 = 1$."),
    (r"$1 + e$", "The constant of integration is found by substituting $x = 0$, $y = 1$: it gives $c = 0$.")],
   [S("Separate", math=r"\int \frac{dy}{y} = \int 2x\,dx"), S("Integrate", math=r"\ln y = x^2 + c, \quad y(0) = 1 \Rightarrow c = 0"), S("So", math=r"y = e^{x^2}, \qquad y(1) = e")],
   "Differential equations", "Calculation", "Separate the variables.")
_q(r"Given $\dfrac{dy}{dx} + y = e^{-x}$ and $y = 2$ when $x = 0$, find $y$ when $x = 1$.",
   r"$\dfrac{3}{e}$",
   [(r"$\dfrac{2}{e}$", "The constant is $2$ in $y = (x + 2)e^{-x}$: do not drop the $x$ term."),
    (r"$3e$", "The factor is $e^{-x}$, so at $x = 1$ it is $e^{-1}$."),
    (r"$\dfrac{1}{e}$", "You used $y = (x + c)e^{-x}$ with $c = 0$; the condition $y(0) = 2$ gives $c = 2$.")],
   [S("Integrating factor $e^{x}$", math=r"\frac{d}{dx}(ye^x) = 1"), S("Integrate", math=r"ye^x = x + c, \quad y(0) = 2 \Rightarrow c = 2"), S("So", math=r"y = (x + 2)e^{-x}, \qquad y(1) = \frac{3}{e}")],
   "Differential equations", "Calculation", "Multiply by the integrating factor e to the x.")
_q(r"Given $\dfrac{dy}{dx} = e^{x - y}$ and $y = \ln 2$ when $x = 0$, find $y$ when $x = 1$, to 3 decimal places.",
   "$1.313$",
   [("$1.693$", "This is $1 + \\ln 2$, from adding the initial value instead of finding the constant. The solution is $e^y = e^x + 1$."),
    ("$1.718$", "This is $e - 1$, not $\\ln(e + 1)$."),
    ("$0.541$", "This is $\\ln(e - 1)$. The constant makes $e^y = e^x + 1$, not $e^x - 1$.")],
   [S("Separate", math=r"e^y\,dy = e^x\,dx"), S("Integrate", math=r"e^y = e^x + c, \quad 2 = 1 + c \Rightarrow c = 1"), S("At $x = 1$", math=r"e^y = e + 1 \Rightarrow y = \ln(e + 1) = 1.313")],
   "Differential equations", "Application", "Write e to the (x - y) as e^x times e^(-y), then separate.")

# ---- Vectors in space (5)
_q(r"Find a unit vector in the direction of $6\mathbf{i} - 2\mathbf{j} + 3\mathbf{k}$.",
   r"$\dfrac{1}{7}(6\mathbf{i} - 2\mathbf{j} + 3\mathbf{k})$",
   [(r"$\dfrac{1}{11}(6\mathbf{i} - 2\mathbf{j} + 3\mathbf{k})$", "$6 - 2 + 3 = 7$ and $6 + 2 + 3 = 11$ are sums of components. The magnitude is $\\sqrt{36 + 4 + 9} = 7$."),
    (r"$\dfrac{1}{49}(6\mathbf{i} - 2\mathbf{j} + 3\mathbf{k})$", "$49$ is the square of the magnitude. Divide by $7$."),
    (r"$\dfrac{1}{7}(6\mathbf{i} + 2\mathbf{j} + 3\mathbf{k})$", "The sign of the $\\mathbf{j}$ component must stay negative.")],
   [S("Magnitude", math=r"\sqrt{36 + 4 + 9} = 7"), S("Divide", math=r"\hat{\mathbf{u}} = \frac{1}{7}(6\mathbf{i} - 2\mathbf{j} + 3\mathbf{k})")],
   "Vectors in space", "Calculation", "Find the magnitude first.")
_q(r"The vectors $k\mathbf{i} + 2\mathbf{j} - \mathbf{k}$ and $3\mathbf{i} - \mathbf{j} + 4\mathbf{k}$ are perpendicular. Find $k$.",
   "$2$",
   [("$-2$", r"Substituting $k = -2$ gives $3(-2) - 6 = -12 \neq 0$. Solve $3k - 6 = 0$."),
    (r"$\dfrac{2}{3}$", "You omitted the term $(-1)(4) = -4$: that gives $3k - 2 = 0$."),
    (r"$-\dfrac{2}{3}$", "You took $(-1)(4)$ as $+4$, which gives $3k + 2 = 0$.")],
   [S("Scalar product is zero", math=r"3k + (2)(-1) + (-1)(4) = 0"), S("Solve", math=r"3k - 6 = 0 \Rightarrow k = 2")],
   "Vectors in space", "Calculation", "Set the scalar product equal to zero.")
_q(r"Find the acute angle between the lines with direction vectors $(1, 2, 2)$ and $(2, -1, 2)$, to 1 decimal place.",
   r"$63.6^\circ$",
   [(r"$26.4^\circ$", "This is $90^\\circ - 63.6^\\circ$, from using $\\sin$ instead of $\\cos$."),
    (r"$116.4^\circ$", "This is the obtuse angle. The question asks for the acute angle between the lines."),
    (r"$48.2^\circ$", "You divided by $3 + 3$ instead of $3 \\times 3$.")],
   [S("Scalar product", math=r"(1)(2) + (2)(-1) + (2)(2) = 4"), S("Magnitudes", math=r"\sqrt{1 + 4 + 4} = 3, \quad \sqrt{4 + 1 + 4} = 3"), S("Angle", math=r"\cos\theta = \frac{4}{9} \Rightarrow \theta = 63.6^\circ")],
   "Vectors in space", "Calculation", "Use the formula with the scalar product over the product of the magnitudes.")
_q(r"Find the cartesian equation of the plane through $A(1, 0, -1)$ with normal vector $3\mathbf{i} + 2\mathbf{j} - \mathbf{k}$.",
   r"$3x + 2y - z = 4$",
   [(r"$3x + 2y - z = 2$", "The constant is $\\mathbf{n}\\cdot\\mathbf{a} = 3 + 0 - (-1) = 4$: watch the sign of the $z$ term."),
    (r"$3x + 2y + z = 4$", "The coefficient of $z$ is the $\\mathbf{k}$-component of the normal, $-1$."),
    (r"$x - 2y + 3z = 4$", "The coefficients are the components of the normal in order: $3, 2, -1$.")],
   [S("Plane $\\mathbf{r}\\cdot\\mathbf{n} = \\mathbf{a}\\cdot\\mathbf{n}$", math=r"3x + 2y - z = 3(1) + 2(0) - (-1) = 4")],
   "Vectors in space", "Calculation", "Find n.a using the point on the plane.")
_q(r"The line $\mathbf{r} = (1, 2, 3) + t(1, 1, 2)$ meets the plane $x + 2y - z = 5$. Find the point of intersection.",
   r"$(4, 5, 9)$",
   [(r"$(3, 4, 7)$", "This is the point for $t = 2$. Substituting the line into the plane gives $t + 2 = 5$, so $t = 3$."),
    (r"$(-2, -1, -3)$", "This is the point for $t = -3$. The sign error comes from $2 + t = 5$."),
    (r"$(4, 5, 3)$", "The $z$ coordinate is $3 + 2t = 9$ for $t = 3$.")],
   [S("Substitute $x = 1 + t$, $y = 2 + t$, $z = 3 + 2t$", math=r"(1 + t) + 2(2 + t) - (3 + 2t) = 5"), S("Simplify", math=r"2 + t = 5 \Rightarrow t = 3"), S("Point", math=r"(4, 5, 9)")],
   "Vectors in space", "Application", "Write x, y and z in terms of t and put them in the plane.")

# ---- Section B, Lower Sixth option topics (15 questions). Concept = the outline topic title.
# ---- Descriptive Statistics (5)
_q(r"The values $4, 7, 7, 9, 13$ (invented for practice) have mean $8$. Find their variance, using the divisor $n$.",
   "$8.8$",
   [("$11$", r"This divides by $n - 1 = 4$ (the unbiased estimate). The variance of the data themselves divides by $n = 5$: $44 \div 5 = 8.8$."),
    (r"$2.97$", "This is the standard deviation, the square root of the variance."),
    ("$72.8$", r"This is the mean of the squares, $\frac{\sum x^2}{n} = \frac{364}{5}$. Subtract the square of the mean: $72.8 - 64 = 8.8$.")],
   [S("Sum of squares of deviations", math=r"16 + 1 + 1 + 1 + 25 = 44"), S("Divide by $n = 5$", math=r"\frac{44}{5} = 8.8")],
   "Measures of location and spread", "Calculation", "Subtract the mean from each value, square, add, divide by n.")
_q(r"The number of goals scored in $20$ football matches (invented for practice) is: $0$ goals in $5$ matches, $1$ goal in $8$ matches, $2$ goals in $4$ matches and $3$ goals in $3$ matches. Find the median number of goals.",
   "$1$",
   [("$1.5$", "This is the middle of the values $0, 1, 2, 3$. The median is the middle of the $20$ observations."),
    ("$1.25$", "This is the mean, $\\frac{25}{20}$."),
    ("$10.5$", "This is the position of the median among the observations, not its value.")],
   [S("Position of the median", text="Between the $10$th and $11$th values."), S("Cumulative frequencies", text="$5$ zeros, then $8$ ones (positions $6$ to $13$)."), S("Both the $10$th and $11$th values are $1$", math=r"\text{median} = 1")],
   "Measures of location and spread", "Calculation", "Build cumulative frequencies and find the 10th and 11th values.")
_q(r"The ordered data $3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 20, 31$ (invented for practice) have $Q_1 = 7$ and $Q_3 = 16$. Find the quartile deviation.",
   "$4.5$",
   [("$9$", "This is the interquartile range $Q_3 - Q_1$. The quartile deviation is **half** of it."),
    ("$11.5$", "This is $\\frac{Q_1 + Q_3}{2}$, the mid-quartile (here it also equals the median). The quartile deviation uses the **difference**."),
    ("$23$", "This is $Q_1 + Q_3$. The quartile deviation uses the difference, divided by $2$.")],
   [S("Quartile deviation (semi-interquartile range)", math=r"\frac{Q_3 - Q_1}{2} = \frac{16 - 7}{2} = 4.5")],
   "Quartiles and box plots", "Recall", "Is the quartile deviation the whole interquartile range?")
_q(r"In a histogram the class $0$ to $10$ has frequency $20$ and a bar of height $2$. The class $10$ to $30$ has frequency $60$. What is the height of its bar?",
   "$3$",
   [("$6$", "You divided $60$ by the width $10$ of the first class. The class $10$ to $30$ has width $20$."),
    ("$60$", "The height is the frequency **density**, frequency divided by class width."),
    (r"$1.5$", "You divided by $40$, the upper limit, instead of the width $20$.")],
   [S("Frequency density = frequency / width", math=r"\frac{20}{10} = 2 \ \checkmark"), S("Class $10$ to $30$", math=r"\frac{60}{20} = 3")],
   "Grouped data and histograms", "Calculation", "Height = frequency divided by class width.")
_q(r"$10$ values $x$ have mean $40$ and standard deviation $6$. They are coded as $y = 3x - 10$. Find the variance of $y$.",
   "$324$",
   [("$108$", "The variance is multiplied by $3^2 = 9$, not by $3$."),
    ("$18$", "This is the standard deviation of $y$, $3 \\times 6$."),
    ("$314$", "Subtracting $10$ does not change spread, and the variance is multiplied by $9$ ($36 \\times 9 = 324$).")],
   [S("Variance of $x$", math=r"6^2 = 36"), S("Variance of $ax + b$ is $a^2$ times the variance of $x$", math=r"3^2 \times 36 = 324")],
   "Coding and combining data sets", "Application", "Which part of the coding changes the spread?")

# ---- Probability (5)
_q(r"$P(A) = 0.45$, $P(B) = 0.3$ and $P(A \cup B) = 0.6$. Find $P(A \cap B)$.",
   "$0.15$",
   [("$0.75$", "This is $P(A) + P(B)$. The addition law subtracts $P(A \\cap B)$ when the events overlap."),
    ("$0.135$", "This is $P(A) \\times P(B)$, which assumes independence: it is not given."),
    ("$0.3$", "This is $P(B)$ itself.")],
   [S("Addition law", math=r"P(A \cup B) = P(A) + P(B) - P(A \cap B)"), S("Rearrange", math=r"P(A \cap B) = 0.45 + 0.3 - 0.6 = 0.15")],
   "Events and the addition law", "Calculation", "Make the intersection the subject of the addition law.")
_q(r"In a class of $40$ students, $25$ play football, $18$ play volleyball and $6$ play neither. A student is chosen at random. Find the probability that the student plays **exactly one** of the two sports.",
   "$0.625$",
   [("$0.85$", "This is the probability of playing at least one sport, $\\frac{34}{40}$."),
    ("$0.225$", "This is the probability of playing both, $\\frac{9}{40}$."),
    ("$0.4$", "This is football only, $\\frac{16}{40}$. Add volleyball only, $\\frac{9}{40}$.")],
   [S("At least one sport", math=r"40 - 6 = 34"), S("Both sports", math=r"25 + 18 - 34 = 9"), S("Exactly one", math=r"(25 - 9) + (18 - 9) = 25, \quad \text{probability } \frac{25}{40} = 0.625")],
   "Events and the addition law", "Application", "Find the number who play both first.")
_q(r"Machine $A$ makes $60\%$ of the items in a factory and machine $B$ makes the rest. $2\%$ of $A$'s items are defective and $5\%$ of $B$'s. An item is chosen at random and is defective. Find the probability that it came from $A$.",
   "$0.375$",
   [("$0.6$", "This is the probability that an item comes from $A$, before knowing it is defective."),
    ("$0.012$", "This is $P(A \\cap \\text{defective})$. Divide it by $P(\\text{defective})$."),
    ("$0.171$", "You divided by $0.02 + 0.05$ instead of by $0.6(0.02) + 0.4(0.05) = 0.032$.")],
   [S("Probability of a defective item", math=r"0.6 \times 0.02 + 0.4 \times 0.05 = 0.012 + 0.02 = 0.032"), S("Conditional probability", math=r"P(A \mid D) = \frac{0.012}{0.032} = 0.375")],
   "Conditional probability and independence", "Application", "Use a tree: find P(defective) first.")
_q(r"$A$ and $B$ are independent events with $P(A) = 0.4$ and $P(B) = 0.5$. Find $P(A \cup B)$.",
   "$0.7$",
   [("$0.9$", "This adds the probabilities, which is only correct for mutually exclusive events."),
    ("$0.2$", "This is $P(A \\cap B)$, not $P(A \\cup B)$."),
    ("$0.45$", "This is the mean of the two probabilities.")],
   [S("Independent events", math=r"P(A \cap B) = 0.4 \times 0.5 = 0.2"), S("Addition law", math=r"P(A \cup B) = 0.4 + 0.5 - 0.2 = 0.7")],
   "Conditional probability and independence", "Calculation", "Find the intersection using independence, then use the addition law.")
_q(r"A committee of $4$ is chosen from $6$ men and $4$ women. How many committees contain **at least two** women?",
   "$115$",
   [("$90$", "This counts committees with exactly two women, $\\binom{4}{2}\\binom{6}{2}$. Add those with three and four women."),
    ("$195$", "This only removes committees with no women, $210 - 15$. Also remove those with exactly one woman."),
    ("$168$", r"$\binom{4}{2}\binom{8}{2}$ counts some committees more than once: it chooses two women first and then any two others.")],
   [S("All committees", math=r"\binom{10}{4} = 210"), S("Fewer than two women", math=r"\binom{6}{4} + 4\binom{6}{3} = 15 + 80 = 95"), S("At least two women", math=r"210 - 95 = 115")],
   "Permutations and combinations", "Application", "Use the complement: count the committees with 0 or 1 women.")

# ---- Discrete Random Variables (5)
_q(r"$X$ takes the values $1, 2, 3, 4$ with $P(X = x) = kx$. Find $E(X)$.",
   "$3$",
   [("$2.5$", "This is the mean of the values $1, 2, 3, 4$, which ignores the probabilities."),
    ("$0.3$", "This is $k \\times 3$. $E(X) = \\sum x\\,P(X = x)$ with $P(X = x) = 0.1x$."),
    ("$30$", "This is $\\sum x^2 = 30$; you forgot to multiply by $k = 0.1$.")],
   [S("Find $k$", math=r"k(1 + 2 + 3 + 4) = 1 \Rightarrow k = 0.1"), S("Expectation", math=r"E(X) = \sum x \cdot 0.1x = 0.1(1 + 4 + 9 + 16) = 3")],
   "Probability distributions, expectation and variance", "Calculation", "The probabilities sum to 1: find k first.")
_q(r"$X$ takes the values $1, 2, 3, 4$ with $P(X = x) = 0.1x$, so $E(X) = 3$ and $E(X^2) = 10$. Find $\text{Var}(3X - 2)$.",
   "$9$",
   [("$3$", "The variance is multiplied by $3^2 = 9$. You multiplied $\\text{Var}(X) = 1$ by $3$."),
    ("$1$", "This is $\\text{Var}(X)$, not $\\text{Var}(3X - 2)$."),
    ("$7$", "Subtracting $2$ does not change the variance, and the coefficient is squared: $9 \\times 1 = 9$.")],
   [S("Variance of $X$", math=r"\text{Var}(X) = E(X^2) - [E(X)]^2 = 10 - 9 = 1"), S("Linear change", math=r"\text{Var}(aX + b) = a^2\text{Var}(X) = 9 \times 1 = 9")],
   "Probability distributions, expectation and variance", "Calculation", "First find Var(X), then use Var(aX + b).")
_q(r"$X \sim B(10, 0.3)$. Find $P(X = 3)$, to 3 decimal places.",
   "$0.267$",
   [("$0.650$", "This is $P(X \\leq 3)$. The question asks for exactly $3$."),
    ("$0.617$", "This is $P(X \\geq 3)$, not $P(X = 3)$."),
    ("$0.027$", r"This is $0.3^3$ only. Multiply by $\binom{10}{3}$ and $0.7^7$.")],
   [S("Binomial probability", math=r"P(X = 3) = \binom{10}{3}(0.3)^3(0.7)^7 = 120 \times 0.027 \times 0.08235 = 0.2668")],
   "The binomial distribution", "Calculation", "Use C(10,3) p cubed q to the seventh.")
_q(r"$X \sim B(40, 0.25)$. Find the standard deviation of $X$, to 3 significant figures.",
   "$2.74$",
   [("$7.50$", "This is the variance $np(1 - p)$. Take the square root."),
    ("$3.16$", "You used the mean $np = 10$ as the variance. The variance is $np(1 - p) = 7.5$."),
    ("$10.0$", "This is the mean $np$, not the standard deviation.")],
   [S("Variance", math=r"np(1 - p) = 40 \times 0.25 \times 0.75 = 7.5"), S("Standard deviation", math=r"\sqrt{7.5} = 2.74")],
   "The binomial distribution", "Calculation", "Find the variance np(1 - p) first.")
_q(r"A seed germinates with probability $0.2$. Five seeds are sown. Find the probability that **at least one** germinates.",
   "$0.672$",
   [("$0.2$", "This is the probability for one seed. For five seeds, use the complement of none germinating."),
    ("$0.328$", "This is $P(\\text{none germinates}) = 0.8^5$. 'At least one' is the complement."),
    ("$0.9997$", "$1 - 0.2^5$ is the probability that not all five germinate. 'At least one' is $1 - 0.8^5$.")],
   [S("Complement", math=r"P(X \geq 1) = 1 - P(X = 0)"), S("Calculate", math=r"1 - 0.8^5 = 1 - 0.32768 = 0.672")],
   "The binomial distribution", "Application", "Use 1 minus the probability that none germinates.")

# ---------------------------------------------------------------- Paper 3 practice paper A (Lower Sixth): 24 auto-markable parts in 8 questions
# Correct options of the multiple-choice parts are spread over A, B, C and D. All data are invented for practice.
PA_QUESTIONS = []


def _pm(prompt, right, wrongs, pos, steps, concept, skill, hint):
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(pos, C(right, correct=True))
    PA_QUESTIONS.append(MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint))


def _pn(prompt, answer, steps, concept, skill, hint, tolerance=0, unit=""):
    PA_QUESTIONS.append(NUM(prompt, answer, steps=steps, tolerance=tolerance, unit=unit, concept=concept, skill=skill, hint=hint))


# ---- Question 1: measures of location and spread
_pn(r"Question 1(a). The takings of a market stall, in thousands of FCFA, on $8$ days were $12, 15, 9, 14, 18, 11, 16, 13$. Find the mean takings.", 13.5,
    [S("Sum and divide", math=r"\frac{12 + 15 + 9 + 14 + 18 + 11 + 16 + 13}{8} = \frac{108}{8} = 13.5")],
    "Measures of location and spread", "Calculation", "Add all eight values and divide by 8.", tolerance=0.01, unit="thousand FCFA")
_pn(r"Question 1(b). For the same data, find the standard deviation, using the divisor $n$. Give your answer to 2 decimal places.", 2.69,
    [S("Sum of squares", math=r"\sum x^2 = 1516"), S("Variance", math=r"\frac{1516}{8} - 13.5^2 = 189.5 - 182.25 = 7.25"), S("Standard deviation", math=r"\sqrt{7.25} = 2.69")],
    "Measures of location and spread", "Calculation", "Variance = mean of squares minus square of the mean.", tolerance=0.01, unit="thousand FCFA")
_pm(r"Question 1(c). A ninth day is added with takings of $13.5$ thousand FCFA, equal to the mean of the first eight days. What happens to the mean and the variance of the nine values?",
    "The mean is unchanged and the variance decreases",
    [("The mean and the variance are both unchanged", r"The sum of squared deviations stays $58$, but it is now divided by $9$ instead of $8$, so the variance falls from $7.25$ to $6.44$."),
     ("The mean is unchanged and the variance increases", "The new value is at the mean, so it adds nothing to the sum of squared deviations but raises the count."),
     ("The mean increases and the variance decreases", "A value equal to the mean cannot change the mean.")], 2,
    [S("Mean", text="Adding a value equal to the mean leaves the mean at $13.5$."), S("Variance", math=r"\frac{58}{9} = 6.44 < 7.25", text="The sum of squared deviations is unchanged but is divided by a larger $n$.")],
    "Measures of location and spread", "Reasoning", "How does the new value deviate from the mean?")

# ---- Question 2: quartiles
_pn(r"Question 2(a). The ordered marks of $12$ students are $3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 20, 31$. Find the lower quartile $Q_1$ (use the median of the lower half; check your textbook if your method differs).", 7,
    [S("Lower half", text="$3, 5, 6, 8, 9, 11$"), S("Its median", math=r"Q_1 = \frac{6 + 8}{2} = 7")],
    "Quartiles and box plots", "Calculation", "Take the median of the lowest six values.")
_pn(r"Question 2(b). For the same data find the upper quartile $Q_3$.", 16,
    [S("Upper half", text="$12, 14, 15, 17, 20, 31$"), S("Its median", math=r"Q_3 = \frac{15 + 17}{2} = 16")],
    "Quartiles and box plots", "Calculation", "Take the median of the highest six values.")
_pm(r"Question 2(c). Find the quartile deviation of the same data.",
    "$4.5$",
    [("$9$", "This is the interquartile range $Q_3 - Q_1$. The quartile deviation is half of it."),
     ("$11.5$", r"This is $\frac{Q_1 + Q_3}{2}$, the mid-quartile. The quartile deviation uses the difference."),
     ("$23$", "This is $Q_1 + Q_3$.")], 1,
    [S("Semi-interquartile range", math=r"\frac{Q_3 - Q_1}{2} = \frac{16 - 7}{2} = 4.5")],
    "Quartiles and box plots", "Recall", "Is it the whole interquartile range?")

# ---- Question 3: grouped data
_pn(r"Question 3(a). The masses of $50$ yams (kg, invented for practice) are grouped: $0$ to under $10$: $6$; $10$ to under $20$: $14$; $20$ to under $40$: $20$; $40$ to under $60$: $10$. Estimate the mean mass, using mid-class values. Give your answer to 1 decimal place.", 26.8,
    [S("Mid-values", text="$5, 15, 30, 50$"), S("Sum $fx$", math=r"6(5) + 14(15) + 20(30) + 10(50) = 30 + 210 + 600 + 500 = 1340"), S("Mean", math=r"\frac{1340}{50} = 26.8")],
    "Grouped data and histograms", "Calculation", "Multiply each mid-value by its frequency.", tolerance=0.05, unit="kg")
_pn(r"Question 3(b). Estimate the median mass by linear interpolation.", 25,
    [S("The $25$th value", text="Cumulative frequencies are $6, 20, 40, 50$, so the median is in the class $20$ to $40$."), S("Interpolate", math=r"20 + \frac{25 - 20}{20} \times 20 = 25")],
    "Grouped data and histograms", "Calculation", "Which class contains the 25th observation?", tolerance=0.05, unit="kg")
_pn(r"Question 3(c). A histogram is drawn for these data. Find the height (frequency density) of the bar for the class $40$ to under $60$.", 0.5,
    [S("Frequency density", math=r"\frac{10}{20} = 0.5")],
    "Grouped data and histograms", "Calculation", "Divide the frequency by the class width.", tolerance=0.01)

# ---- Question 4: coding and combining
_pn(r"Question 4(a). For $40$ values of $x$ (invented for practice), $\sum(x - 50) = -120$ and $\sum(x - 50)^2 = 1500$. Find the mean of $x$.", 47,
    [S("Mean of the coded values $y = x - 50$", math=r"\bar{y} = \frac{-120}{40} = -3"), S("Decode", math=r"\bar{x} = 50 + (-3) = 47")],
    "Coding and combining data sets", "Calculation", "Find the mean of x - 50 first.", tolerance=0.01)
_pn(r"Question 4(b). Find the variance of $x$.", 28.5,
    [S("Variance of $y$", math=r"\frac{1500}{40} - (-3)^2 = 37.5 - 9 = 28.5"), S("Subtracting $50$ does not change the variance", math=r"\text{Var}(x) = 28.5")],
    "Coding and combining data sets", "Calculation", "Variance of x equals variance of x - 50.", tolerance=0.01)
_pm(r"Question 4(c). A second class of $20$ students has mean mark $12$ and a third class of $30$ students has mean mark $17$. Find the mean mark of all $50$ students.",
    "$15$",
    [("$14.5$", "This is the mean of the two means. The classes have different sizes, so weight each mean by its class size."),
     ("$14$", r"You swapped the weights: $\frac{30 \times 12 + 20 \times 17}{50}$."),
     ("$750$", "This is the total of all the marks. Divide by $50$ students.")], 3,
    [S("Total of the marks", math=r"20 \times 12 + 30 \times 17 = 240 + 510 = 750"), S("Divide by $50$", math=r"\frac{750}{50} = 15")],
    "Coding and combining data sets", "Application", "Combine the totals, not the means.")

# ---- Question 5: events, conditional probability and independence
_pn(r"Question 5(a). $P(A) = 0.55$, $P(B) = 0.35$ and $P(A' \cap B') = 0.2$. Find $P(A \cap B)$.", 0.1,
    [S("Probability of neither", text=r"$P(A \cup B) = 1 - 0.2 = 0.8$."), S("Addition law", math=r"P(A \cap B) = 0.55 + 0.35 - 0.8 = 0.1")],
    "Events and the addition law", "Calculation", "First find P(A union B) from the probability of neither.", tolerance=0.005)
_pm(r"Question 5(b). For the events in part (a), which statement is correct?",
    r"$A$ and $B$ are not independent, because $0.55 \times 0.35 = 0.1925 \neq 0.1$",
    [(r"$A$ and $B$ are independent, because $P(A \cap B) \neq 0$", "Independence needs $P(A \\cap B) = P(A)P(B)$. A non-zero intersection only shows that the events are not mutually exclusive."),
     (r"$A$ and $B$ are mutually exclusive, because $P(A \cap B)$ is small", "Mutually exclusive means $P(A \\cap B) = 0$ exactly."),
     (r"$A$ and $B$ are independent, because $0.1 < 0.35$", "The comparison for independence is with the product $P(A)P(B) = 0.1925$.")], 0,
    [S("Product", math=r"P(A)P(B) = 0.55 \times 0.35 = 0.1925"), S("Compare", math=r"0.1925 \neq 0.1", text="So the events are not independent. They are not mutually exclusive either.")],
    "Events and the addition law", "Reasoning", "Compare P(A and B) with P(A) times P(B).")
_pn(r"Question 5(c). In a school, $55\%$ of the students are girls. $30\%$ of the girls and $20\%$ of the boys walk to school. A student is chosen at random. Find the probability that the student walks to school. Give your answer to 3 decimal places.", 0.255,
    [S("Tree: girl walks or boy walks", math=r"0.55 \times 0.3 + 0.45 \times 0.2 = 0.165 + 0.09 = 0.255")],
    "Conditional probability and independence", "Application", "Add the two branches of the tree that end in 'walks'.", tolerance=0.001)
_pn(r"Question 5(d). Given that a student walks to school, find the probability that the student is a girl. Give your answer to 3 decimal places.", 0.647,
    [S("Conditional probability", math=r"P(\text{girl} \mid \text{walks}) = \frac{0.165}{0.255} = 0.647")],
    "Conditional probability and independence", "Calculation", "Divide the girl-and-walks branch by the probability of walking.", tolerance=0.001)

# ---- Question 6: permutations and combinations
_pn(r"Question 6(a). Find the number of different arrangements of all the letters of the word BAFANG (there are two letters A).", 360,
    [S("Arrangements with a repeated letter", math=r"\frac{6!}{2!} = \frac{720}{2} = 360")],
    "Permutations and combinations", "Calculation", "Divide by the factorial of the number of repeated letters.")
_pn(r"Question 6(b). A team of $3$ students is chosen from $9$. In how many ways can this be done?", 84,
    [S("Selection", math=r"\binom{9}{3} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84")],
    "Permutations and combinations", "Calculation", "Order does not matter: use a combination.")

# ---- Question 7: discrete random variable
_pn(r"Question 7(a). A random variable $X$ has $P(X = 1) = 0.1$, $P(X = 2) = 0.3$, $P(X = 3) = k$ and $P(X = 4) = 0.2$. Find $k$.", 0.4,
    [S("Probabilities sum to 1", math=r"0.1 + 0.3 + k + 0.2 = 1 \Rightarrow k = 0.4")],
    "Probability distributions, expectation and variance", "Calculation", "The probabilities add up to 1.", tolerance=0.001)
_pn(r"Question 7(b). Find $E(X)$.", 2.7,
    [S("Expectation", math=r"E(X) = 1(0.1) + 2(0.3) + 3(0.4) + 4(0.2) = 0.1 + 0.6 + 1.2 + 0.8 = 2.7")],
    "Probability distributions, expectation and variance", "Calculation", "Sum each value times its probability.", tolerance=0.001)
_pn(r"Question 7(c). Find $\text{Var}(X)$.", 0.81,
    [S("$E(X^2)$", math=r"1(0.1) + 4(0.3) + 9(0.4) + 16(0.2) = 0.1 + 1.2 + 3.6 + 3.2 = 8.1"), S("Variance", math=r"8.1 - 2.7^2 = 8.1 - 7.29 = 0.81")],
    "Probability distributions, expectation and variance", "Calculation", "Var(X) = E(X squared) minus the square of E(X).", tolerance=0.005)

# ---- Question 8: binomial distribution
_pn(r"Question 8(a). Each bus on a route arrives late with probability $0.35$, independently. Of $12$ buses, let $X$ be the number that are late. Find $P(X = 4)$, to 3 decimal places.", 0.237,
    [S("Model", text=r"$X \sim B(12, 0.35)$."), S("Probability", math=r"\binom{12}{4}(0.35)^4(0.65)^8 = 495 \times 0.01501 \times 0.03186 = 0.2367")],
    "The binomial distribution", "Calculation", "State B(12, 0.35) and use the binomial formula.", tolerance=0.001)
_pn(r"Question 8(b). Find $P(X \geq 2)$, to 3 decimal places.", 0.958,
    [S("Complement", math=r"P(X \geq 2) = 1 - P(X \leq 1) = 1 - 0.0424 = 0.9576")],
    "The binomial distribution", "Calculation", "Use one minus P(X <= 1).", tolerance=0.001)
_pn(r"Question 8(c). Find the variance of $X$.", 2.73,
    [S("Variance of a binomial", math=r"np(1 - p) = 12 \times 0.35 \times 0.65 = 2.73")],
    "The binomial distribution", "Recall", "Use n p (1 - p).", tolerance=0.01)


# ---------------------------------------------------------------- Sets
assert len(B_QUESTIONS) == 50, len(B_QUESTIONS)

SETS = [
    practice_set(module="Examination", topic="Paper 3", title="Paper 3 practice paper A",
                 lesson=LESSON, mock=True, time_limit_minutes=150, questions=PA_QUESTIONS),
    practice_set(module="Examination", topic="Paper 1", title="Paper 1 mock exam B",
                 lesson=LESSON_P1, mock=True, time_limit_minutes=90, questions=B_QUESTIONS),
]
