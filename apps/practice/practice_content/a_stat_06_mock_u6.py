"""Pure Mathematics with Statistics (A Level), Upper Sixth: two mock papers.

KKEVO draft content. Timings are KKEVO practice settings, not official examination times. All data are invented
for practice; no question is taken from a past paper.
Paper 3 practice paper A: about 24 auto-markable parts (multiple choice and numeric) in 8 numbered questions on further distributions, sampling and hypothesis testing, and correlation and regression.
Paper 1 mock exam B: 50 four-option multiple-choice questions, 35 on pure mathematics (Section A) and 15 on the
option topics of this year (Section B). Every concept is the exact topic title of the course outline.
"""

from .dsl import *  # noqa: F403

COURSE = ("pure-mathematics-with-statistics", "upper-sixth")

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

# ---- Section B, Upper Sixth option topics (15 questions). Concept = the outline topic title.
# ---- Further Distributions (5)
_q(r"The number of customers arriving at a kiosk in one hour has a Poisson distribution with mean $3$. Find the probability that exactly $2$ customers arrive in an hour, to 3 decimal places.",
   "$0.224$",
   [("$0.423$", "This is $P(X \\leq 2)$. The question asks for exactly $2$."),
    ("$0.801$", "This is $P(X \\geq 2)$, not $P(X = 2)$."),
    ("$0.050$", r"This is $e^{-3}$ only. Multiply by $\frac{3^2}{2!}$.")],
   [S("Poisson probability", math=r"P(X = 2) = \frac{e^{-3}\,3^2}{2!} = 0.04979 \times 4.5 = 0.2240")],
   "The Poisson distribution", "Calculation", "Use e to the minus lambda, times lambda to the r, over r factorial.")
_q(r"A continuous random variable $X$ has probability density function $f(x) = kx^2$ for $0 \leq x \leq 3$, and $f(x) = 0$ otherwise. Find $k$.",
   r"$\dfrac{1}{9}$",
   [(r"$\dfrac{1}{27}$", r"You forgot to divide by $3$ when integrating $kx^2$: $\int_0^3 kx^2\,dx = 9k$."),
    (r"$\dfrac{1}{3}$", "$3$ is the upper limit, not the value of the integral. The total area under $f$ must be $1$."),
    ("$9$", "The integral $\\int_0^3 kx^2\\,dx$ equals $9k$ and must be $1$, so $k = \\frac{1}{9}$.")],
   [S("Total probability is 1", math=r"\int_0^3 kx^2\,dx = 1"), S("Integrate", math=r"\left[\frac{kx^3}{3}\right]_0^3 = 9k = 1 \Rightarrow k = \frac{1}{9}")],
   "Continuous random variables", "Calculation", "The area under the density function is 1.")
_q(r"A continuous random variable $X$ has probability density function $f(x) = \dfrac{x^2}{9}$ for $0 \leq x \leq 3$. Find the median of $X$, to 2 decimal places.",
   "$2.38$",
   [("$1.50$", "This is the midpoint of the range, which is the median only for a uniform distribution."),
    ("$2.25$", r"This is the mean, $\int_0^3 \frac{x^3}{9}\,dx = \frac{81}{36}$."),
    ("$3.67$", r"This is $\sqrt{13.5}$: the equation is $\frac{m^3}{27} = \frac{1}{2}$, so take the cube root, not the square root.")],
   [S("Median $m$", math=r"\int_0^m \frac{x^2}{9}\,dx = \frac{1}{2}"), S("Integrate", math=r"\frac{m^3}{27} = \frac{1}{2} \Rightarrow m^3 = 13.5"), S("Solve", math=r"m = 2.38")],
   "Continuous random variables", "Calculation", "The median splits the area into two halves of 0.5.")
_q(r"$X \sim N(50, 16)$. Find $P(46 < X < 58)$, to 3 decimal places.",
   "$0.819$",
   [("$0.977$", "This is $P(X < 58)$ only; remove the lower tail $P(X < 46)$."),
    ("$0.683$", "This is $P(46 < X < 54)$, the range within one standard deviation each side."),
    ("$0.136$", "This is $P(54 < X < 58)$, the part from $1$ to $2$ standard deviations above the mean.")],
   [S("Standardise ($\\sigma = 4$)", math=r"z_1 = \frac{46 - 50}{4} = -1, \qquad z_2 = \frac{58 - 50}{4} = 2"), S("Probability", math=r"\Phi(2) - \Phi(-1) = 0.9772 - 0.1587 = 0.8186")],
   "The normal distribution", "Calculation", "The second parameter 16 is the variance: find sigma first.")
_q(r"$X \sim \text{Po}(36)$. Use a normal approximation with a continuity correction to estimate $P(X \geq 40)$, to 3 decimal places.",
   "$0.280$",
   [("$0.252$", "This uses $P(Y > 40)$. A continuity correction for $X \\geq 40$ uses $Y > 39.5$."),
    ("$0.227$", "This uses $P(Y > 40.5)$, the correction in the wrong direction."),
    ("$0.720$", "This is the complement, $P(Y < 39.5)$.")],
   [S("Approximating normal", math=r"Y \sim N(36, 36), \quad \sigma = 6"), S("Continuity correction", math=r"P(X \geq 40) \approx P(Y > 39.5) = P\!\left(Z > \frac{3.5}{6}\right) = P(Z > 0.583)"), S("Table", math=r"= 0.280")],
   "Normal approximations", "Calculation", "For X at least 40, the boundary is 39.5.")

# ---- Sampling & Hypothesis Testing (5)
_q(r"A random sample of $25$ observations is taken from a population with mean $80$ and variance $100$. State the distribution of the sample mean $\bar{X}$ (the population is normal).",
   r"$N(80, 4)$",
   [(r"$N(80, 100)$", "This is the distribution of a single observation, not of the mean of $25$."),
    (r"$N(80, 2)$", r"$2 = 10/5$ is the standard error. The variance is $\frac{100}{25} = 4$."),
    (r"$N(80, 20)$", r"You divided the variance by $\sqrt{25}$. It is divided by $n = 25$.")],
   [S("Mean", math=r"E(\bar{X}) = 80"), S("Variance", math=r"\frac{\sigma^2}{n} = \frac{100}{25} = 4")],
   "The distribution of the sample mean", "Recall", "The variance of the sample mean is sigma squared over n.")
_q(r"A random sample of $49$ observations has mean $36$. The population standard deviation is $7$. Find a $95\%$ confidence interval for the population mean.",
   r"$(34.04,\ 37.96)$",
   [(r"$(22.28,\ 49.72)$", r"You used $\sigma = 7$ instead of the standard error $7/\sqrt{49} = 1$."),
    (r"$(34.36,\ 37.64)$", "You used $z = 1.645$, which is for a $90\\%$ interval."),
    (r"$(35.02,\ 36.98)$", r"You used a standard error of $0.5$. It is $\frac{7}{\sqrt{49}} = 1$.")],
   [S("Standard error", math=r"\frac{7}{\sqrt{49}} = 1"), S("Interval", math=r"36 \pm 1.96 \times 1 = (34.04,\ 37.96)")],
   "Estimation and confidence intervals", "Calculation", "Find the standard error first, then multiply by 1.96.")
_q(r"A test of $H_0: \mu = 30$ against $H_1: \mu > 30$ uses a random sample of $64$ observations with mean $31.2$. The population standard deviation is $4$. Find the value of the test statistic $z$.",
   "$2.4$",
   [("$0.3$", "You divided the difference by $\\sigma = 4$. Divide by the standard error $4/\\sqrt{64} = 0.5$."),
    ("$1.2$", "This is the difference $\\bar{x} - \\mu_0$ itself."),
    ("$9.6$", r"You multiplied the difference by $\sqrt{64} = 8$ but did not divide by $\sigma$: $1.2 \times 8 = 9.6$.")],
   [S("Standard error", math=r"\frac{4}{\sqrt{64}} = 0.5"), S("Test statistic", math=r"z = \frac{31.2 - 30}{0.5} = 2.4")],
   "Hypothesis tests for a mean", "Calculation", "Divide the difference by sigma over root n.")
_q(r"In a two-tailed test of a population mean at the $5\%$ level, the test statistic is $z = -2.1$. What is the correct conclusion?",
   r"Reject $H_0$, because $|-2.1| > 1.96$: there is evidence that the population mean differs from the value in $H_0$",
   [(r"Do not reject $H_0$, because $z$ is negative", "The sign does not matter in a two-tailed test: compare $|z|$ with $1.96$."),
    (r"Do not reject $H_0$, because $2.1 < 2.576$", "$2.576$ is the critical value at the $1\\%$ level. At $5\\%$ it is $1.96$."),
    (r"Reject $H_0$, and conclude that the sample mean differs from the population mean", "Hypotheses and conclusions are about the **population** mean $\\mu$, not the sample mean.")],
   [S("Rule at 5%, two-tailed", text=r"Reject $H_0$ if $|z| > 1.96$."), S("Compare", text=r"$2.1 > 1.96$, so reject $H_0$.")],
   "Hypothesis tests for a mean", "Interpretation", "Which critical value applies for a two-tailed test at 5%?")
_q(r"Under $H_0: p = 0.4$, $X \sim B(10, 0.4)$. A test of $H_1: p > 0.4$ is made and the observed value is $x = 8$. Find the p-value, to 4 decimal places.",
   "$0.0123$",
   [("$0.0106$", "This is $P(X = 8)$. The p-value is $P(X \\geq 8)$."),
    ("$0.0017$", "This is $P(X \\geq 9)$: the observed value $8$ must be included."),
    ("$0.9983$", "This is $P(X \\leq 8)$, the wrong tail for $H_1: p > 0.4$.")],
   [S("Upper tail", math=r"P(X \geq 8) = P(8) + P(9) + P(10) = 0.01062 + 0.00157 + 0.00010 = 0.0123")],
   "Hypothesis tests for binomial and Poisson", "Calculation", "H1 says p is bigger: which tail?")

# ---- Correlation & Regression (5)
_q(r"For data with $S_{xx} = 50$, $S_{yy} = 60$ and $S_{xy} = -45$, find the product-moment correlation coefficient, to 3 decimal places.",
   r"$-0.822$",
   [(r"$0.822$", "The sign of $r$ is the sign of $S_{xy}$: it is negative here."),
    (r"$-0.900$", r"This is $\frac{S_{xy}}{S_{xx}} = -0.9$, the gradient of the regression line of $y$ on $x$, not $r$."),
    (r"$-0.750$", r"This is $\frac{S_{xy}}{S_{yy}}$, the gradient of the line of $x$ on $y$.")],
   [S("Formula", math=r"r = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} = \frac{-45}{\sqrt{50 \times 60}}"), S("Calculate", math=r"= \frac{-45}{54.77} = -0.822")],
   "Correlation", "Calculation", "r is S xy over the square root of S xx times S yy.")
_q(r"A scatter diagram of the heights and masses of $30$ students shows points close to a straight line sloping upwards, and $r = 0.95$. Which statement is correct?",
   "There is strong positive linear correlation, but this does not by itself show that one variable causes the other",
   [("Greater height causes greater mass, because $r$ is close to $1$", "Correlation does not prove cause and effect."),
    ("$95\\%$ of the students lie on the line", "The value of $r$ measures the strength of the linear relationship, not a percentage of points on the line."),
    ("There is strong negative correlation, because the points slope upwards", "Points sloping upwards give a positive $r$.")],
   [S("Interpret $r$", text="$r$ is close to $1$ and positive: strong positive linear correlation. A correlation does not prove causation.")],
   "Correlation", "Interpretation", "What does r measure, and what can it not show?")
_q(r"For $n$ pairs of data, $\bar{x} = 10$, $\bar{y} = 30$, $S_{xx} = 50$ and $S_{xy} = -45$. Find the equation of the regression line of $y$ on $x$.",
   r"$y = 39 - 0.9x$",
   [(r"$y = 30 - 0.9x$", "The line passes through $(\\bar{x}, \\bar{y})$: $a = \\bar{y} - b\\bar{x} = 30 + 9 = 39$."),
    (r"$y = 39 + 0.9x$", r"The gradient is $\frac{S_{xy}}{S_{xx}} = -0.9$, which is negative."),
    (r"$y = 21 - 0.9x$", "$a = \\bar{y} - b\\bar{x} = 30 - (-0.9)(10) = 39$: you subtracted $9$ instead of adding it.")],
   [S("Gradient", math=r"b = \frac{S_{xy}}{S_{xx}} = \frac{-45}{50} = -0.9"), S("Intercept", math=r"a = \bar{y} - b\bar{x} = 30 + 9 = 39"), S("Line", math=r"y = 39 - 0.9x")],
   "Regression lines", "Calculation", "The line passes through the mean point.")
_q(r"A regression line $y = 39 - 0.9x$ was found from data with $x$ between $4$ and $16$. A student uses it to estimate $y$ when $x = 40$. What is the correct comment?",
   "The estimate is an extrapolation, so it may be unreliable",
   [("The estimate is reliable, because $r$ is close to $-1$", "A strong correlation within the data range does not guarantee that the line continues outside it."),
    ("The estimate is an interpolation, so it is reliable", "$x = 40$ is outside the data range $4$ to $16$, so this is extrapolation."),
    ("The estimate cannot be made, because the line is only for $x$ on $y$", "The line of $y$ on $x$ is correct for estimating $y$. The issue is that $x = 40$ is far outside the data.")],
   [S("Compare with the data range", text="$40$ is far outside $4 \\le x \\le 16$."), S("Conclude", text="Extrapolation: the relationship may not continue, so the estimate may be unreliable.")],
   "Regression lines", "Reasoning", "Is the value inside or outside the range of the data?")
_q(r"A Spearman rank correlation coefficient is calculated for $8$ pairs of ranks with $\sum d^2 = 14$. Find $r_s$, to 3 decimal places.",
   "$0.833$",
   [("$0.167$", "This is $\\frac{6\\sum d^2}{n(n^2 - 1)}$. Subtract it from $1$."),
    ("$-0.313$", r"You divided by $n^2 = 64$ instead of $n(n^2 - 1) = 504$."),
    ("$0.838$", r"You used $n(n^2 + 1) = 520$ in the denominator. It is $n(n^2 - 1) = 8 \times 63 = 504$.")],
   [S("Formula", math=r"r_s = 1 - \frac{6\sum d^2}{n(n^2 - 1)}"), S("Substitute", math=r"1 - \frac{6 \times 14}{8 \times 63} = 1 - \frac{84}{504} = 0.833")],
   "Rank correlation", "Calculation", "Use 1 minus 6 sum d squared over n(n squared minus 1).")

# ---------------------------------------------------------------- Paper 3 practice paper A (Upper Sixth): 23 auto-markable parts in 8 questions
# Correct options of the multiple-choice parts are spread over A, B, C and D. All data are invented for practice.
PA_QUESTIONS = []


def _pm(prompt, right, wrongs, pos, steps, concept, skill, hint):
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(pos, C(right, correct=True))
    PA_QUESTIONS.append(MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint))


def _pn(prompt, answer, steps, concept, skill, hint, tolerance=0, unit=""):
    PA_QUESTIONS.append(NUM(prompt, answer, steps=steps, tolerance=tolerance, unit=unit, concept=concept, skill=skill, hint=hint))


# ---- Question 1: the Poisson distribution
_pn(r"Question 1(a). Flaws in a roll of cloth occur at random at a mean rate of $0.8$ per metre. Let $X$ be the number of flaws in a $5$ m length. Find $P(X = 3)$, to 3 decimal places.", 0.195,
    [S("Model", text=r"$X \sim \text{Po}(5 \times 0.8) = \text{Po}(4)$."), S("Probability", math=r"P(X = 3) = \frac{e^{-4}\,4^3}{3!} = 0.1954")],
    "The Poisson distribution", "Calculation", "Find the mean for 5 m first.", tolerance=0.001)
_pn(r"Question 1(b). Find the probability that there are more than $5$ flaws in a $5$ m length, to 3 decimal places.", 0.215,
    [S("Complement", math=r"P(X > 5) = 1 - P(X \leq 5) = 1 - 0.7851 = 0.2149")],
    "The Poisson distribution", "Calculation", "More than 5 means 6 or more: use one minus P(X <= 5).", tolerance=0.001)
_pm(r"Question 1(c). For the number of flaws $X$ in a $5$ m length, which statement is correct?",
    r"$E(X) = 4$ and $\text{Var}(X) = 4$",
    [(r"$E(X) = 4$ and $\text{Var}(X) = 2$", r"For a Poisson distribution the variance equals the mean: $\text{Var}(X) = \lambda = 4$, not $\sqrt{4}$."),
     (r"$E(X) = 0.8$ and $\text{Var}(X) = 0.8$", "$0.8$ is the rate per metre. For $5$ m the mean is $5 \\times 0.8 = 4$."),
     (r"$E(X) = 4$ and $\text{Var}(X) = 16$", r"You squared the mean. For a Poisson distribution $\text{Var}(X) = \lambda$.")], 3,
    [S("Poisson", text=r"The mean and the variance both equal $\lambda = 4$.")],
    "The Poisson distribution", "Concept", "What is special about the mean and variance of a Poisson distribution?")

# ---- Question 2: continuous random variable
_pn(r"Question 2(a). A continuous random variable $X$ has probability density function $f(x) = kx(4 - x)$ for $0 \leq x \leq 4$ and $0$ otherwise. Find $k$, to 3 decimal places.", 0.094,
    [S("Total probability", math=r"\int_0^4 k(4x - x^2)\,dx = k\left[2x^2 - \frac{x^3}{3}\right]_0^4 = k\left(32 - \frac{64}{3}\right) = \frac{32k}{3} = 1"), S("Solve", math=r"k = \frac{3}{32} = 0.09375 \approx 0.094")],
    "Continuous random variables", "Calculation", "The integral of f over its range must equal 1.", tolerance=0.001)
_pn(r"Question 2(b). Find $P(X < 1)$, to 3 decimal places.", 0.156,
    [S("Integrate", math=r"\frac{3}{32}\left[2x^2 - \frac{x^3}{3}\right]_0^1 = \frac{3}{32}\left(2 - \frac{1}{3}\right) = \frac{5}{32} = 0.15625")],
    "Continuous random variables", "Calculation", "Integrate f from 0 to 1.", tolerance=0.001)
_pn(r"Question 2(c). Find $\text{Var}(X)$. (You may use the fact that $E(X) = 2$, by symmetry.)", 0.8,
    [S("$E(X^2)$", math=r"\frac{3}{32}\int_0^4 (4x^3 - x^4)\,dx = \frac{3}{32}\left(256 - \frac{1024}{5}\right) = 4.8"), S("Variance", math=r"4.8 - 2^2 = 0.8")],
    "Continuous random variables", "Calculation", "Var(X) = E(X squared) minus the square of E(X).", tolerance=0.005)

# ---- Question 3: normal distribution
_pn(r"Question 3(a). The mass of a mango is normally distributed with mean $250$ g and standard deviation $20$ g. Find the probability that a mango weighs more than $270$ g, to 3 decimal places.", 0.159,
    [S("Standardise", math=r"P(X > 270) = P\!\left(Z > \frac{270 - 250}{20}\right) = P(Z > 1) = 0.1587")],
    "The normal distribution", "Calculation", "Standardise with sigma = 20.", tolerance=0.001)
_pn(r"Question 3(b). Find the probability that a mango weighs between $230$ g and $275$ g, to 3 decimal places.", 0.736,
    [S("Standardise", math=r"z_1 = -1, \quad z_2 = 1.25"), S("Probability", math=r"\Phi(1.25) - \Phi(-1) = 0.8944 - 0.1587 = 0.7357")],
    "The normal distribution", "Calculation", "Find the two z values, then subtract the probabilities.", tolerance=0.001)
_pn(r"Question 3(c). The heaviest $10\%$ of mangoes weigh more than $m$ grams. Find $m$, to 1 decimal place.", 275.6,
    [S("Inverse normal", math=r"P(Z < z) = 0.9 \Rightarrow z = 1.2816"), S("Convert", math=r"m = 250 + 1.2816 \times 20 = 275.6")],
    "The normal distribution", "Application", "Find the z value with 0.9 below it, then convert back.", tolerance=0.1, unit="g")

# ---- Question 4: normal approximation
_pn(r"Question 4(a). $X \sim B(100, 0.3)$. Use a normal approximation with a continuity correction to estimate $P(X \leq 25)$, to 3 decimal places.", 0.163,
    [S("Approximating normal", math=r"Y \sim N(30, 21), \quad \sigma = 4.583"), S("Continuity correction", math=r"P(X \leq 25) \approx P(Y < 25.5) = P\!\left(Z < \frac{25.5 - 30}{4.583}\right) = P(Z < -0.982)"), S("Table", math=r"= 0.163")],
    "Normal approximations", "Calculation", "The boundary for X at most 25 is 25.5.", tolerance=0.002)
_pm(r"Question 4(b). Which of these gives the conditions under which a normal approximation to $B(n, p)$ is appropriate?",
    r"$n$ is large and $p$ is not close to $0$ or $1$ (for example $np$ and $n(1 - p)$ both greater than $5$)",
    [(r"$n$ is small and $p$ is small", "A normal approximation needs a large number of trials. Small $n$ with small $p$ gives a very skewed binomial."),
     (r"$n$ is large and $p$ is small", "A small $p$ with large $n$ gives a skewed distribution; the Poisson approximation is used instead. The normal approximation also needs $p$ away from $0$ and $1$."),
     (r"$p = 0.5$ only", "The normal approximation works for other values of $p$ too, as long as $np$ and $n(1 - p)$ are large enough.")], 0,
    [S("Conditions", text="$n$ large and $p$ not close to $0$ or $1$. Check your textbook for the exact rule (for example $np > 5$ and $n(1 - p) > 5$).")],
    "Normal approximations", "Recall", "Both np and n(1 - p) need to be large enough.")

# ---- Question 5: sample mean and confidence intervals
_pn(r"Question 5(a). The mass of a bag of cement has standard deviation $1.5$ kg. A random sample of $36$ bags has mean mass $24.3$ kg. Find the standard error of the sample mean.", 0.25,
    [S("Standard error", math=r"\frac{1.5}{\sqrt{36}} = 0.25")],
    "The distribution of the sample mean", "Calculation", "Divide sigma by the square root of n.", tolerance=0.001, unit="kg")
_pn(r"Question 5(b). Find the lower limit of a $95\%$ confidence interval for the population mean, to 2 decimal places.", 23.81,
    [S("Lower limit", math=r"24.3 - 1.96 \times 0.25 = 24.3 - 0.49 = 23.81")],
    "Estimation and confidence intervals", "Calculation", "Subtract 1.96 standard errors from the sample mean.", tolerance=0.01, unit="kg")
_pn(r"Question 5(c). What is the smallest sample size for which a $95\%$ confidence interval has a margin of error of at most $0.25$ kg?", 139,
    [S("Inequality", math=r"1.96 \times \frac{1.5}{\sqrt{n}} \leq 0.25"), S("Solve", math=r"\sqrt{n} \geq \frac{1.96 \times 1.5}{0.25} = 11.76, \quad n \geq 138.3"), S("Round up", math=r"n = 139")],
    "Estimation and confidence intervals", "Application", "Round up to a whole number.")

# ---- Question 6: hypothesis tests
_pn(r"Question 6(a). A supplier claims that the mean mass of a bag of cement is $24.0$ kg. Using the data in Question 5 ($n = 36$, $\bar{x} = 24.3$, $\sigma = 1.5$), test $H_0: \mu = 24.0$ against $H_1: \mu \neq 24.0$. Find the value of the test statistic $z$.", 1.2,
    [S("Test statistic", math=r"z = \frac{24.3 - 24.0}{1.5/6} = \frac{0.3}{0.25} = 1.2")],
    "Hypothesis tests for a mean", "Calculation", "Divide the difference by the standard error.", tolerance=0.01)
_pm(r"Question 6(b). What is the correct conclusion at the $5\%$ significance level?",
    r"Do not reject $H_0$: $|z| = 1.2 < 1.96$, so there is not enough evidence that the mean differs from $24.0$ kg",
    [(r"Reject $H_0$: $1.2 > 1$, so the mean differs from $24.0$ kg", "There is no critical value of $1$. The two-tailed $5\\%$ critical value is $1.96$."),
     (r"Reject $H_0$: the sample mean $24.3$ differs from $24.0$", "Sample means always differ from the claimed mean a little. The test asks whether the difference is too large to be chance."),
     (r"Do not reject $H_0$, so the mean has been proved to be $24.0$ kg", "A test never proves $H_0$. It only finds that the evidence is not strong enough against it.")], 1,
    [S("Rule", text=r"Reject $H_0$ if $|z| > 1.96$."), S("Compare", text=r"$1.2 < 1.96$: do not reject $H_0$.")],
    "Hypothesis tests for a mean", "Interpretation", "Compare |z| with the two-tailed 5% critical value.")
_pn(r"Question 6(c). A seed seller claims that the probability that a seed germinates is $0.2$ or less. Of $15$ seeds, $7$ germinate. Under $H_0: p = 0.2$, $X \sim B(15, 0.2)$. For $H_1: p > 0.2$, find the p-value, to 4 decimal places.", 0.0181,
    [S("Upper tail", math=r"P(X \geq 7) = 1 - P(X \leq 6) = 1 - 0.9819 = 0.0181")],
    "Hypothesis tests for binomial and Poisson", "Calculation", "H1 is an upper-tail alternative: which probability is needed?", tolerance=0.0005)

# ---- Question 7: correlation and regression lines
_pn(r"Question 7(a). For $8$ pairs of values, $\bar{x} = 8$, $\bar{y} = 15$, $S_{xx} = 56$, $S_{yy} = 130$ and $S_{xy} = 70$. Find the product-moment correlation coefficient, to 3 decimal places.", 0.820,
    [S("Formula", math=r"r = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} = \frac{70}{\sqrt{56 \times 130}} = \frac{70}{85.32} = 0.8204")],
    "Correlation", "Calculation", "Use S xy over the square root of S xx times S yy.", tolerance=0.002)
_pn(r"Question 7(b). The regression line of $y$ on $x$ is $y = a + bx$. Find $b$.", 1.25,
    [S("Gradient", math=r"b = \frac{S_{xy}}{S_{xx}} = \frac{70}{56} = 1.25")],
    "Regression lines", "Calculation", "The gradient is S xy over S xx.", tolerance=0.005)
_pn(r"Question 7(c). Using the regression line (with $a = \bar{y} - b\bar{x} = 5$), estimate $y$ when $x = 10$.", 17.5,
    [S("Line", math=r"y = 5 + 1.25x"), S("Estimate", math=r"y = 5 + 1.25 \times 10 = 17.5")],
    "Regression lines", "Application", "Substitute x = 10 into the line.", tolerance=0.05)

# ---- Question 8: rank correlation
_pn(r"Question 8(a). Two judges rank six contestants. Judge A ranks them $1, 2, 3, 4, 5, 6$ and judge B ranks the same contestants $2, 1, 4, 3, 6, 5$. Find $\sum d^2$, where $d$ is the difference in ranks.", 6,
    [S("Differences", text="Each difference is $1$ or $-1$, so each $d^2 = 1$."), S("Sum", math=r"\sum d^2 = 6 \times 1 = 6")],
    "Rank correlation", "Calculation", "Subtract the ranks, square, add.")
_pn(r"Question 8(b). Find Spearman's rank correlation coefficient $r_s$, to 3 decimal places.", 0.829,
    [S("Formula", math=r"r_s = 1 - \frac{6\sum d^2}{n(n^2 - 1)} = 1 - \frac{36}{6 \times 35} = 1 - 0.1714 = 0.829")],
    "Rank correlation", "Calculation", "Use n = 6 in 1 - 6 sum d squared over n(n squared - 1).", tolerance=0.001)
_pm(r"Question 8(c). What does $r_s = 0.829$ say about the two judges?",
    "They largely agree: there is strong positive agreement between their rankings",
    [("They largely disagree: there is strong negative agreement", "A positive $r_s$ close to $1$ means that high ranks from one judge go with high ranks from the other."),
     ("There is no relationship between the rankings", "No relationship would give $r_s$ near $0$."),
     ("The judges agree $82.9\\%$ of the time", "$r_s$ measures how closely the rankings move together; it is not a percentage of agreements.")], 2,
    [S("Interpret", text="$r_s$ is close to $1$: the rankings are strongly positively related.")],
    "Rank correlation", "Interpretation", "What does a value of r_s near 1 mean?")


# ---------------------------------------------------------------- Sets
assert len(B_QUESTIONS) == 50, len(B_QUESTIONS)

SETS = [
    practice_set(module="Examination", topic="Paper 3", title="Paper 3 practice paper A",
                 lesson=LESSON, mock=True, time_limit_minutes=150, questions=PA_QUESTIONS),
    practice_set(module="Examination", topic="Paper 1", title="Paper 1 mock exam B",
                 lesson=LESSON_P1, mock=True, time_limit_minutes=90, questions=B_QUESTIONS),
]
