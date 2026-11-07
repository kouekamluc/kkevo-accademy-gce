"""Further Mathematics (A Level, Upper Sixth): practice sets for Vector Spaces & Linear Transformations,
Numerical Methods, Advanced Mechanics & Probability, and the Examination module (two lesson sets, a Paper 1
mock and a Paper 2 practice paper).

KKEVO draft content. Mock paper timings are KKEVO practice settings, not official examination times.
Paper 1 mock A: 50 four-option multiple-choice questions across all six modules of the year in proportion to
their topic counts (concept = topic title). Paper 2 practice paper A: auto-markable parts (multiple choice and
numeric) in numbered questions across the six modules.
"""

import math
import random

from .dsl import *  # noqa: F403

COURSE = ("further-mathematics", "upper-sixth")

VS = "Vector Spaces & Linear Transformations"
NM = "Numerical Methods"
MP = "Advanced Mechanics & Probability"
CA = "Advanced Differential & Integral Calculus"
OD = "Ordinary Differential Equations"
GR = "Abstract Algebra: Group Theory"

_rng = random.Random(7750)
_slots = []


def _slot(group=None):
    """Position of the correct option (0-3). Shuffled in blocks of four so A-D are used evenly."""
    if not _slots:
        block = [0, 1, 2, 3]
        _rng.shuffle(block)
        _slots.extend(block)
    return _slots.pop()


def mc(prompt, right, wrongs, steps, concept, skill, hint, feedback="", diagram="", diagram_alt=""):
    """Four-option question: `right` is the correct text, `wrongs` three (text, why) pairs."""
    assert len(wrongs) == 3, prompt[:50]
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(_slot(), C(right, correct=True))
    return MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint, feedback=feedback,
              diagram=diagram, diagram_alt=diagram_alt)


def _v(*c):
    return r"\begin{pmatrix} " + r" \\ ".join(str(x) for x in c) + r" \end{pmatrix}"


def _m(*rows):
    return r"\begin{pmatrix} " + r" \\ ".join(" & ".join(str(x) for x in r) for r in rows) + r" \end{pmatrix}"


SETS = []


# ================================================================ Vector spaces
_slots.clear()
SETS.append(practice_set(
    module=VS, topic="Subspaces, independence, basis and dimension",
    title="Subspaces, independence, basis and dimension",
    lesson="fmu2-subspaces-independence-basis-dimension",
    questions=[
        mc(r"Which of these is a subspace of $\mathbb{R}^3$?",
           r"$\{(x, y, z) : x + y + z = 0\}$",
           [(r"$\{(x, y, z) : x + y + z = 1\}$", r"It does not contain $(0, 0, 0)$, so it fails the first test."),
            (r"$\{(x, y, z) : x \ge 0\}$", r"It is not closed under multiplication by a negative scalar: $-1(1, 0, 0) = (-1, 0, 0)$ is outside."),
            (r"$\{(x, y, z) : xy = 0\}$", r"$(1, 0, 0) + (0, 1, 0) = (1, 1, 0)$ has $xy = 1 \neq 0$: not closed under addition.")],
           [S("Zero vector", math=r"0 + 0 + 0 = 0 \ \checkmark"), S("Closure", text="Adding two vectors with coordinate sum 0 gives coordinate sum 0, and so does scaling.")],
           "Subspace test", "Concept", "Check the zero vector first, then closure under addition and scaling."),
        mc(r"Find the dimension of $W = \{(x, y, z, w) \in \mathbb{R}^4 : x + y = 0 \text{ and } z = w\}$.",
           r"$2$",
           [(r"$4$", "That is the dimension of the whole space; the two conditions each remove one dimension."),
            (r"$3$", "You used only one of the two independent conditions."),
            (r"$1$", "Two parameters remain free ($x$ and $z$), not one.")],
           [S("Solve the conditions", math=r"y = -x,\ w = z"), S("General vector", math=r"(x, -x, z, z) = x(1, -1, 0, 0) + z(0, 0, 1, 1)"), S("Two independent vectors", text="Dimension $= 2$.")],
           "Dimension of a subspace", "Calculation", "Count the free variables after solving the conditions."),
        NUM(r"The vectors $(1, 1, 0)$, $(1, 2, 1)$ and $(2, 3, k)$ are linearly dependent for exactly one value of $k$. Find $k$.", 1,
            steps=[S("Determinant of the three vectors as rows", math=r"\begin{vmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 2 & 3 & k \end{vmatrix} = (2k - 3) - (k - 2) = k - 1"),
                   S("Dependent when the determinant is zero", math=r"k - 1 = 0 \Rightarrow k = 1")],
            concept="Linear independence and determinants", skill="Calculation", hint="Three vectors in R3 are dependent exactly when the determinant is 0."),
        mc(r"Which set is a basis of the space of polynomials of degree at most 2?",
           r"$\{1 + x,\ x + x^2,\ 1 + x^2\}$",
           [(r"$\{1,\ x,\ 1 + x\}$", r"Dependent: $1 + x$ is the sum of the first two."),
            (r"$\{1,\ x^2\}$", "Independent, but only two vectors: the space has dimension 3, so they do not span."),
            (r"$\{1,\ x,\ x^2,\ x^2 + 1\}$", "Four vectors in a 3-dimensional space are dependent.")],
           [S("The space has dimension 3", text="So a basis has exactly 3 independent polynomials."),
            S("Check independence", text=r"$a(1 + x) + b(x + x^2) + c(1 + x^2) = 0$ forces $a = b = c = 0$.")],
           "Basis of polynomials", "Concept", "A basis of a 3-dimensional space needs exactly three independent vectors."),
        NUM(r"Write $(2, 3, 5)$ in the form $a(1, 1, 0) + b(0, 1, 1) + c(1, 0, 1)$. Find $c$.", 2,
            steps=[S("Equations", math=r"a + c = 2,\quad a + b = 3,\quad b + c = 5"), S("Add them", math=r"a + b + c = 5"), S("Subtract the second", math=r"c = 5 - 3 = 2")],
            concept="Coordinates relative to a basis", skill="Calculation", hint="Write three component equations and add them to find a + b + c."),
        mc(r"What is the span of $\{(1, 2, 3), (2, 4, 6)\}$?",
           "A line through the origin, of dimension 1",
           [("A plane through the origin, of dimension 2", "The second vector is twice the first: they are dependent, so they give only one direction."),
            (r"All of $\mathbb{R}^3$", "Two vectors can never span a 3-dimensional space."),
            ("A line not through the origin", "A span always contains the zero vector, so it passes through the origin.")],
           [S("Dependent", math=r"(2, 4, 6) = 2(1, 2, 3)"), S("Span", text="All multiples of $(1, 2, 3)$: a line through the origin.")],
           "Span", "Concept", "Is one vector a multiple of the other?"),
        mc(r"The space of $2 \times 2$ real symmetric matrices $\begin{pmatrix} a & b \\ b & d \end{pmatrix}$ has dimension:",
           r"$3$",
           [(r"$4$", r"Symmetry forces the off-diagonal entries to be equal, so there are only three free entries."),
            (r"$2$", "The diagonal entries are two parameters, but $b$ is a third."),
            (r"$1$", "There are three independent parameters.")],
           [S("Free parameters", text="$a$, $b$, $d$."),
            S("Basis", math=r"\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}")],
           "Dimension of a matrix space", "Application", "Count the free entries."),
        mc(r"Which statement is true?",
           r"Any four vectors in $\mathbb{R}^3$ are linearly dependent.",
           [(r"Any three vectors in $\mathbb{R}^3$ form a basis.", "Not if they are dependent, e.g. three vectors in one plane."),
            (r"A subspace of $\mathbb{R}^3$ need not contain the zero vector.", "Every subspace contains the zero vector."),
            (r"Every basis of $\mathbb{R}^3$ is the standard basis.", "There are infinitely many bases; only the number of vectors is fixed.")],
           [S("Dimension", text=r"$\dim\mathbb{R}^3 = 3$. More than $3$ vectors cannot be independent.")],
           "Dimension and independence", "Reasoning", "Think about the largest independent set in a 3-dimensional space."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=VS, topic="Linear transformations",
    title="Linear transformations and their matrices",
    lesson="fmu2-linear-transformations-matrices",
    questions=[
        mc(r"Which of these maps $\mathbb{R}^2 \to \mathbb{R}^2$ is linear?",
           r"$T(x, y) = (2x - y,\ x + 3y)$",
           [(r"$T(x, y) = (x + 1,\ y)$", r"$T(0, 0) = (1, 0) \neq (0, 0)$: a linear map sends zero to zero."),
            (r"$T(x, y) = (x^2,\ y)$", r"$T(2\mathbf{u}) \neq 2T(\mathbf{u})$ because of the square."),
            (r"$T(x, y) = (xy,\ x)$", "A product of variables is not allowed in a linear map.")],
           [S("Test", text="Each component is a sum of terms of degree 1 with no constant, so both conditions hold.")],
           "Recognising a linear map", "Concept", "A linear map sends zero to zero and has only first-degree terms."),
        NUM(r"$T(x, y) = (3x - y,\ x + 2y)$. Find the first component of $T(2, -1)$.", 7,
            steps=[S("Substitute", math=r"3(2) - (-1) = 6 + 1 = 7")], concept="Evaluating a linear map", skill="Calculation", hint="Substitute x = 2, y = -1 into the first formula."),
        mc(r"$T(1, 0) = (2, 3)$ and $T(0, 1) = (-1, 4)$ for a linear map $T$. Its matrix is:",
           r"$" + _m([2, -1], [3, 4]) + "$",
           [(r"$" + _m([2, 3], [-1, 4]) + "$", "The images of the basis vectors must be the **columns**, not the rows."),
            (r"$" + _m([2, -1], [4, 3]) + "$", "The second column is $(-1, 4)$, not $(4, 3)$."),
            (r"$" + _m([-1, 2], [4, 3]) + "$", "The columns are in the wrong order and the wrong sign.")],
           [S("Columns are the images of $e_1$, $e_2$", math=r"A = " + _m([2, -1], [3, 4]))],
           "Matrix from images of the basis", "Calculation", "Which vectors become the columns of the matrix?"),
        NUM(r"A linear map has $T(1, 0) = (2, 3)$ and $T(0, 1) = (-1, 4)$. Find the second component of $T(2, 5)$.", 26,
            steps=[S("Linearity", math=r"T(2, 5) = 2(2, 3) + 5(-1, 4) = (4 - 5,\ 6 + 20) = (-1, 26)")], concept="Using linearity", skill="Calculation", hint="Write (2, 5) = 2 e1 + 5 e2."),
        mc(r"The matrix of the reflection in the line $y = x$ is $M = " + _m([0, 1], [1, 0]) + r"$ and of the rotation through $90^\circ$ anticlockwise $R = " + _m([0, -1], [1, 0]) + r"$. Reflect **first**, then rotate. The matrix of the combination is:",
           r"$RM = " + _m([-1, 0], [0, 1]) + "$",
           [(r"$MR = " + _m([1, 0], [0, -1]) + "$", "That is rotate first and then reflect: the matrix of the first transformation goes on the right."),
            (r"$R + M = " + _m([0, 0], [2, 0]) + "$", "Combining transformations is matrix multiplication, not addition."),
            (r"$" + _m([1, 0], [0, 1]) + "$", "The product of these two matrices is not the identity.")],
           [S("First $M$, then $R$", math=r"RM = " + _m([0, -1], [1, 0]) + _m([0, 1], [1, 0]) + " = " + _m([-1, 0], [0, 1])), S("Meaning", text="A reflection in the $y$-axis.")],
           "Composition of transformations", "Calculation", "Which matrix is next to the vector in R(Mx)?"),
        mc(r"Differentiation $D$ maps polynomials of degree $\le 2$ (basis $1, x, x^2$) to polynomials of degree $\le 1$ (basis $1, x$). Its matrix is:",
           r"$" + _m([0, 1, 0], [0, 0, 2]) + "$",
           [(r"$" + _m([0, 0], [1, 0], [0, 2]) + "$", "That is the transpose: $D$ goes from a 3-dimensional space to a 2-dimensional one, so the matrix is $2 \\times 3$."),
            (r"$" + _m([1, 0, 0], [0, 2, 0]) + "$", "$D(1) = 0$, so the first column must be zero."),
            (r"$" + _m([0, 1, 0], [0, 0, 1]) + "$", "$D(x^2) = 2x$, so the last entry is $2$, not $1$.")],
           [S("Images", math=r"D(1) = 0,\ D(x) = 1,\ D(x^2) = 2x"), S("Columns", math=r"" + _m([0, 1, 0], [0, 0, 2]))],
           "Matrix of differentiation", "Application", "Write each image in coordinates; they are the columns."),
        NUM(r"A linear map has matrix $" + _m([2, 0], [0, 3]) + r"$. By what factor does it multiply the area of the unit square?", 6,
            steps=[S("Area factor is the determinant", math=r"\det = 2 \times 3 = 6")], concept="Determinant as area factor", skill="Application", hint="The image of the unit square is a 2 by 3 rectangle."),
        mc(r"$T$ and $S$ are linear maps of the plane with matrices $A$ and $B$. The matrix of 'first $T$, then $S$' is:",
           r"$BA$",
           [(r"$AB$", "That is 'first $S$, then $T$'."), (r"$A + B$", "Sums of matrices do not represent composition."), (r"$A^{-1}B$", "Inverses are not involved.")],
           [S("Apply to a vector", math=r"S(T(\mathbf{x})) = B(A\mathbf{x}) = (BA)\mathbf{x}")],
           "Order of composition", "Concept", "Write S(T(x)) and put the matrices next to x."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=VS, topic="Kernel, range and the rank-nullity theorem",
    title="Kernel, range and the rank-nullity theorem",
    lesson="fmu2-kernel-range-rank-nullity",
    questions=[
        mc(r"The map $T(x, y, z) = (x + y,\ y + z,\ x - z)$ has matrix $" + _m([1, 1, 0], [0, 1, 1], [1, 0, -1]) + r"$ with determinant $0$. A basis of its kernel is:",
           r"$\{(1, -1, 1)\}$",
           [(r"$\{(1, 1, 1)\}$", r"$T(1, 1, 1) = (2, 2, 0) \neq \mathbf{0}$."),
            (r"$\{(1, 0, 0), (0, 0, 1)\}$", r"$T(1, 0, 0) = (1, 0, 1) \neq \mathbf{0}$; the kernel is 1-dimensional."),
            (r"$\{\mathbf{0}\}$", "The determinant is zero, so the kernel contains non-zero vectors.")],
           [S("Solve $T = 0$", math=r"x + y = 0,\ y + z = 0 \Rightarrow y = -x,\ z = x"), S("Check the third", math=r"x - z = 0 \ \checkmark"), S("Basis", math=r"\{(1, -1, 1)\}")],
           "Kernel from a matrix", "Calculation", "Solve the three component equations equal to zero."),
        NUM(r"A linear map $T : \mathbb{R}^5 \to \mathbb{R}^3$ has rank $2$. Find its nullity.", 3,
            steps=[S("Rank-nullity", math=r"\text{rank} + \text{nullity} = 5 \Rightarrow \text{nullity} = 3")], concept="Rank-nullity theorem", skill="Calculation", hint="Rank plus nullity equals the dimension of the domain."),
        mc(r"What is the rank of $" + _m([1, 2, 3], [2, 4, 6], [1, 0, 1]) + r"$?",
           r"$2$",
           [(r"$3$", "Row 2 is twice row 1, so the rows are dependent."), (r"$1$", "Rows 1 and 3 are not multiples of each other."), (r"$0$", "The matrix is not the zero matrix.")],
           [S("Dependent rows", text="Row 2 $= 2\\times$ row 1."), S("Independent rows", text="Rows 1 and 3 are independent, so the rank is $2$.")],
           "Rank of a matrix", "Calculation", "Look for rows that are multiples or sums of others."),
        NUM(r"Find the nullity of $A = " + _m([1, 2, 0, 1], [2, 4, 1, 5], [3, 6, 1, 6]) + r"$.", 2,
            steps=[S("Row reduce", math=r"\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}"), S("Rank 2; four columns", math=r"\text{nullity} = 4 - 2 = 2")],
            concept="Nullity from row reduction", skill="Calculation", hint="Row reduce, count the leading 1s, then use rank-nullity."),
        mc(r"For $A = " + _m([1, 2, 1], [2, 4, 3], [1, 2, 2]) + r"$ (rank 2), a basis of the range (column space) is:",
           r"$\{(1, 2, 1),\ (1, 3, 2)\}$",
           [(r"$\{(1, 2, 1),\ (2, 4, 2)\}$", "The second is twice the first, so they are dependent; column 2 is twice column 1."),
            (r"$\{(1, 2, 1),\ (0, 1, 1)\}$", "These are columns of the reduced matrix, not of $A$. Use the **original** pivot columns."),
            (r"$\{(1, 2, 1),\ (2, 4, 2),\ (1, 3, 2)\}$", "The range has dimension 2, so a basis has two vectors.")],
           [S("Column 2 = 2 x column 1", text="So column 2 adds nothing."), S("Pivot columns 1 and 3 of $A$", math=r"\{(1, 2, 1),\ (1, 3, 2)\}")],
           "Basis of the range", "Application", "The range basis uses the original columns that carry the leading 1s."),
        mc(r"$D : P_3 \to P_2$ takes a polynomial of degree at most 3 to its derivative. The kernel of $D$ is:",
           "the constant polynomials, of dimension 1",
           [("the zero polynomial only", "Every constant has derivative $0$."), ("the polynomials of degree at most 2, of dimension 3", "That is the range, not the kernel."), ("the polynomials with no constant term", "Those have non-zero derivatives, such as $x \\mapsto 1$.")],
           [S("Condition", math=r"p' = 0 \Rightarrow p \text{ is constant}"), S("Check", text=r"Rank $3$ + nullity $1 = 4 = \dim P_3$.")],
           "Kernel of differentiation", "Application", "Which polynomials have zero derivative?"),
        mc(r"$T : \mathbb{R}^3 \to \mathbb{R}^2$ is a linear map. Which statement is always true?",
           r"$T$ is not one-to-one",
           [(r"$T$ is onto", "Not always: the zero map is not onto."), (r"$\ker T = \{\mathbf{0}\}$", "Rank $\\le 2$, so nullity $\\ge 1$: the kernel contains non-zero vectors."), (r"$\operatorname{rank} T = 3$", "The range lies in $\\mathbb{R}^2$ so the rank is at most 2.")],
           [S("Rank-nullity", math=r"\text{nullity} = 3 - \text{rank} \ge 3 - 2 = 1")],
           "Injectivity and dimension", "Reasoning", "How large can the rank be when the target is R2?"),
        mc(r"$T : \mathbb{R}^3 \to \mathbb{R}^3$ has $\ker T = \{\mathbf{0}\}$. Then:",
           r"the range is all of $\mathbb{R}^3$",
           [(r"the range is a plane", "Nullity $0$ gives rank $3$, not $2$."), (r"the range is a line", "Rank is $3 - 0 = 3$."), ("$T$ is the zero map", "The zero map has kernel $\\mathbb{R}^3$.")],
           [S("Rank-nullity", math=r"\text{rank} = 3 - 0 = 3 = \dim \mathbb{R}^3")],
           "Isomorphism", "Reasoning", "Apply rank + nullity = 3."),
    ]))

# ================================================================ Numerical methods
_slots.clear()
SETS.append(practice_set(
    module=NM, topic="Root finding",
    title="Locating roots: bisection and linear interpolation",
    lesson="fmu2-root-finding-bisection-interpolation",
    questions=[
        mc(r"Which interval is guaranteed to contain a root of $f(x) = x^3 - x - 1$?",
           r"$(1, 2)$",
           [(r"$(-1, 0)$", r"$f(-1) = -1$ and $f(0) = -1$: no sign change."), (r"$(2, 3)$", r"$f(2) = 5$ and $f(3) = 23$: both positive."), (r"$(0, 1)$", r"$f(0) = -1$ and $f(1) = -1$: both negative.")],
           [S("Evaluate", math=r"f(1) = -1 < 0, \quad f(2) = 5 > 0")],
           "Change of sign", "Calculation", "Look for an interval whose ends give opposite signs."),
        mc(r"$f(x) = x^3 + x - 3$ has a root in $[1, 2]$. After one step of bisection the root is in:",
           r"$[1,\ 1.5]$",
           [(r"$[1.5,\ 2]$", r"$f(1.5) = 1.875 > 0$ has the same sign as $f(2)$, so the root is to the left."), (r"$[1.25,\ 1.75]$", "Bisection keeps one of the two halves, not a new interval."), (r"$[1,\ 1.25]$", "That would be the second step, and one step only halves the interval.")],
           [S("Midpoint", math=r"f(1.5) = 3.375 + 1.5 - 3 = 1.875 > 0"), S("Sign change", text=r"$f(1) < 0$ and $f(1.5) > 0$: the root is in $[1, 1.5]$.")],
           "One bisection step", "Calculation", "Find the sign of f at the midpoint."),
        NUM(r"Bisection starts with an interval of width $2$. What is the least number of steps that reduces the width below $0.01$?", 8,
            steps=[S("Width after $n$ steps", math=r"\frac{2}{2^n} < 0.01 \Rightarrow 2^n > 200"), S("Powers of 2", math=r"2^7 = 128 < 200 < 256 = 2^8 \Rightarrow n = 8")],
            concept="Bisection error bound", skill="Calculation", hint="The width after n steps is 2 divided by 2 to the power n."),
        mc(r"Linear interpolation is applied to $f(x) = x^2 - 2$ on $[1, 2]$. The first estimate is:",
           r"$\dfrac{4}{3}$",
           [(r"$\dfrac{3}{2}$", "That is the bisection midpoint; interpolation uses the function values."), (r"$\dfrac{5}{3}$", r"The weights are swapped: the root is closer to $1$, where $|f|$ is smaller."), (r"$\sqrt2$", "That is the exact root, not the first interpolation estimate.")],
           [S("Values", math=r"f(1) = -1, \quad f(2) = 2"), S("Formula", math=r"x = \frac{1\cdot 2 - 2\cdot(-1)}{2 - (-1)} = \frac{4}{3}")],
           "Linear interpolation", "Calculation", "x = (a f(b) - b f(a)) / (f(b) - f(a))."),
        NUM(r"Linear interpolation is used for $f(x) = \cos x - x$ on $[0, 1]$ (radians). Find the first estimate, to 3 decimal places.", 0.685, tolerance=0.001,
            steps=[S("Values", math=r"f(0) = 1, \quad f(1) = \cos 1 - 1 = -0.4597"), S("Formula", math=r"x = \frac{0 \cdot f(1) - 1 \cdot f(0)}{f(1) - f(0)} = \frac{-1}{-1.4597} = 0.685")],
            concept="Linear interpolation", skill="Calculation", hint="Substitute a = 0, b = 1 and use radians."),
        mc(r"Why can bisection not be used on $f(x) = \dfrac{1}{x}$ on $[-1, 1]$ even though $f(-1)f(1) < 0$?",
           r"$f$ is not continuous on the interval (it is undefined at $0$)",
           [("$f(0)$ is zero", "$f(0)$ does not exist; $1/x$ is never zero."), ("The interval is symmetric", "Symmetry does not matter."), ("$f$ has two roots", "$1/x$ has no roots.")],
           [S("Condition", text="The sign-change rule needs continuity on the closed interval. The sign change here comes from the asymptote at $x = 0$.")],
           "Continuity condition", "Reasoning", "What must be true of f for a sign change to imply a root?"),
        mc(r"A root is claimed to be $1.32$ to 2 decimal places for a continuous function $f$. To prove it, show a sign change between:",
           r"$1.315$ and $1.325$",
           [(r"$1.31$ and $1.33$", "That interval is wider than the rounding interval, so it does not prove the rounding."), (r"$1.32$ and $1.33$", "The lower rounding bound is $1.315$, not $1.32$."), (r"$1.3$ and $1.4$", "That is far too wide.")],
           [S("Rounding interval", text="Numbers that round to $1.32$ lie in $[1.315, 1.325)$.")],
           "Justifying decimal places", "Reasoning", "Which numbers round to 1.32?"),
        mc(r"Compared with bisection, linear interpolation on a curve that bends the same way over the whole interval often:",
           "keeps one end of the interval fixed and approaches from one side",
           [("halves the interval each time exactly", "That is bisection."), ("converges in one step", "It only does for a straight line."), ("fails because the sign changes disappear", "The sign change is preserved at every step.")],
           [S("From Table 2 of the lesson", text="One endpoint never moves, so the estimates creep towards the root from one side.")],
           "Interpolation behaviour", "Interpretation", "Recall what happened to the end b = 3 in the lesson."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=NM, topic="Root finding",
    title="The Newton-Raphson method",
    lesson="fmu2-newton-raphson-iteration",
    questions=[
        mc(r"The Newton-Raphson iteration for $f(x) = x^2 - 10$ is:",
           r"$x_{n+1} = \dfrac{1}{2}\left(x_n + \dfrac{10}{x_n}\right)$",
           [(r"$x_{n+1} = x_n - \dfrac{x_n^2 - 10}{x_n}$", "The derivative is $2x_n$, not $x_n$."), (r"$x_{n+1} = x_n + \dfrac{x_n^2 - 10}{2x_n}$", "The sign is wrong: subtract $f/f'$."), (r"$x_{n+1} = \dfrac{10}{x_n}$", "That is only part of the average.")],
           [S("Formula", math=r"x_{n+1} = x_n - \frac{x_n^2 - 10}{2x_n} = \frac{x_n}{2} + \frac{5}{x_n}")],
           "Newton-Raphson formula", "Calculation", "Use f'(x) = 2x and simplify."),
        NUM(r"Use one Newton-Raphson step for $x^2 - 10 = 0$ from $x_0 = 3$. Give $x_1$ to 4 decimal places.", 3.1667, tolerance=0.0002,
            steps=[S("Formula", math=r"x_1 = \tfrac12\left(3 + \tfrac{10}{3}\right) = 3.1667")], concept="One Newton-Raphson step", skill="Calculation", hint="Use the averaging form (x + 10/x) / 2."),
        mc(r"$f(x) = x^3 - 2x - 5$ and $x_0 = 2$. The next iterate is:",
           r"$2.1$",
           [(r"$1.9$", "The sign is wrong: $f(2) = -1$ and $f'(2) = 10$, so $x_1 = 2 - (-1/10)$."), (r"$2.5$", "That is the bisection midpoint of $[2, 3]$."), (r"$3$", "You divided by $f$ instead of $f'$.")],
           [S("Values", math=r"f(2) = -1, \quad f'(2) = 3(4) - 2 = 10"), S("Formula", math=r"x_1 = 2 - \frac{-1}{10} = 2.1")],
           "Newton-Raphson iteration", "Calculation", "Compute f(2) and f'(2)."),
        NUM(r"Use one Newton-Raphson step for $e^x - 5x = 0$ from $x_0 = 0.5$. Find $x_1$ to 3 decimal places.", 0.246, tolerance=0.001,
            steps=[S("Values", math=r"f(0.5) = 1.6487 - 2.5 = -0.8513, \quad f'(0.5) = 1.6487 - 5 = -3.3513"), S("Formula", math=r"x_1 = 0.5 - \frac{-0.8513}{-3.3513} = 0.246")],
            concept="Newton-Raphson on a transcendental equation", skill="Calculation", hint="The derivative of e^x - 5x is e^x - 5."),
        mc(r"For which starting values may Newton-Raphson on $f(x) = x^3 - 2x - 5$ fail badly?",
           r"values close to $x = \sqrt{2/3} \approx 0.816$, where $f'(x) = 0$",
           [(r"values close to the root $2.09$", "Near the root the method converges very quickly."), (r"all values greater than $2$", "Starting above the root, it converges."), ("values for which $f(x)$ is positive", "The sign of $f$ is not the problem; a flat tangent is.")],
           [S("Condition", math=r"f'(x) = 3x^2 - 2 = 0 \Rightarrow x = \sqrt{2/3}")],
           "Failure of Newton-Raphson", "Reasoning", "When does the tangent fail to meet the x-axis?"),
        mc(r"$f(x) = x^3 - 2x + 2$ and $x_0 = 0$. Newton-Raphson gives $x_1 = 1$ and then $x_2 = 0$. The iteration:",
           "is trapped in a cycle between 0 and 1 and never converges",
           [("converges to the root at 0", r"$f(0) = 2 \neq 0$."), ("converges to the root at 1", r"$f(1) = 1 \neq 0$."), ("diverges to infinity", "The values stay bounded: 0, 1, 0, 1, ...")],
           [S("Check", math=r"x_1 = 0 - \frac{2}{-2} = 1, \quad x_2 = 1 - \frac{1}{1} = 0")],
           "Cycles in Newton-Raphson", "Interpretation", "Compute two steps and look at the pattern."),
        mc(r"Newton-Raphson gives successive errors $0.03$ and $0.0009$. The next error is approximately:",
           r"$8 \times 10^{-7}$",
           [(r"$0.00003$", "That divides by $30$ each time, as in linear convergence; Newton-Raphson squares the error."), (r"$0.0002$", "A constant ratio is not expected here."), (r"$0.0006$", "The errors fall much faster than this.")],
           [S("Quadratic convergence", math=r"e_{n+1} \approx e_n^2 \Rightarrow (0.0009)^2 = 8.1 \times 10^{-7}")],
           "Quadratic convergence", "Interpretation", "Compare the second error with the square of the first."),
        NUM(r"Use one Newton-Raphson step for $x^2 - 2 = 0$ from $x_0 = 1.5$. Find $x_1$ to 4 decimal places.", 1.4167, tolerance=0.0002,
            steps=[S("Averaging form", math=r"x_1 = \tfrac12\left(1.5 + \tfrac{2}{1.5}\right) = \tfrac12(1.5 + 1.3333) = 1.4167")],
            concept="Newton-Raphson for a square root", skill="Calculation", hint="For x^2 - a, x1 = (x0 + a/x0)/2."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=NM, topic="Numerical integration",
    title="The trapezium rule and Simpson's rule",
    lesson="fmu2-trapezium-simpson-rules",
    questions=[
        mc(r"$\displaystyle\int_1^3 f(x)\,dx$ is estimated with $5$ ordinates. The step length is:",
           r"$0.5$",
           [(r"$0.4$", "That uses $5$ strips; there are only $4$ strips with $5$ ordinates."), (r"$0.25$", "That would need $8$ strips."), (r"$2$", "That is the interval length, not the strip width.")],
           [S("Strips", text="$5$ ordinates give $4$ strips."), S("Step", math=r"h = \frac{3 - 1}{4} = 0.5")],
           "Step length and ordinates", "Calculation", "Number of strips = number of ordinates minus 1."),
        NUM(r"Use the trapezium rule with $2$ strips to estimate $\displaystyle\int_0^1 x^2\,dx$.", 0.375,
            steps=[S("Ordinates", math=r"y_0 = 0,\ y_1 = 0.25,\ y_2 = 1"), S("Rule", math=r"\frac{0.5}{2}\left[0 + 1 + 2(0.25)\right] = 0.25 \times 1.5 = 0.375")],
            concept="Trapezium rule", skill="Calculation", hint="h = 0.5; end ordinates once, middle ordinate twice."),
        NUM(r"Use Simpson's rule with $2$ strips to estimate $\displaystyle\int_0^2 x^3\,dx$.", 4,
            steps=[S("Ordinates ($h = 1$)", math=r"y_0 = 0,\ y_1 = 1,\ y_2 = 8"), S("Rule", math=r"\frac{1}{3}\left[0 + 8 + 4(1)\right] = 4")],
            concept="Simpson's rule", skill="Calculation", hint="Weights 1, 4, 1 with a factor h/3."),
        mc(r"The weights in Simpson's rule for five ordinates $y_0, \dots, y_4$ are:",
           r"$1,\ 4,\ 2,\ 4,\ 1$ with a factor $\dfrac{h}{3}$",
           [(r"$1,\ 2,\ 2,\ 2,\ 1$ with a factor $\dfrac{h}{2}$", "That is the trapezium rule."), (r"$1,\ 4,\ 4,\ 4,\ 1$ with a factor $\dfrac{h}{3}$", "The inner even-numbered ordinate has weight $2$, not $4$."), (r"$1,\ 2,\ 4,\ 2,\ 1$ with a factor $\dfrac{h}{3}$", "The odd-numbered ordinates carry the weight $4$.")],
           [S("Pattern", text="Odd-numbered inner ordinates $\\times 4$, even-numbered inner ordinates $\\times 2$, ends once.")],
           "Simpson weights", "Recall", "Remember the pattern 1, 4, 2, 4, 1 and the factor h/3."),
        NUM(r"Use the trapezium rule with four strips to estimate $\displaystyle\int_0^1 \dfrac{4}{1 + x^2}\,dx$. Give your answer to 4 decimal places.", 3.1312, tolerance=0.0005,
            steps=[S("Ordinates", math=r"4,\ 3.76471,\ 3.2,\ 2.56,\ 2"), S("Rule", math=r"\frac{0.25}{2}\left[4 + 2 + 2(3.76471 + 3.2 + 2.56)\right] = 0.125(25.04941) = 3.1312")],
            concept="Trapezium rule with four strips", skill="Calculation", hint="h = 0.25; compute five ordinates first."),
        NUM(r"A river is $12$ m wide. Its depth in metres at $2$ m intervals is $0,\ 1.2,\ 2.1,\ 2.6,\ 2.2,\ 1.4,\ 0$ (invented data). Use Simpson's rule to find the cross-section area in m$^2$.", 19.6, tolerance=0.05, unit="m^2",
            steps=[S("Strips and step", math=r"n = 6, \quad h = 2"), S("Simpson", math=r"\frac{2}{3}\left[0 + 0 + 4(1.2 + 2.6 + 1.4) + 2(2.1 + 2.2)\right] = \frac{2}{3}(29.4) = 19.6")],
            concept="Simpson's rule with data", skill="Application", hint="Odd-numbered ordinates are the 1st, 3rd and 5th depth."),
        mc(r"The trapezium rule is applied to $\displaystyle\int_1^3 \ln x\,dx$. Because $\ln x$ is concave, the estimate is:",
           "an under-estimate",
           [("an over-estimate", "That happens for convex curves, where the chords lie above the curve."), ("exactly right", "The trapezium rule is exact only for straight lines."), ("sometimes over and sometimes under", "A concave curve always lies above its chords.")],
           [S("Chords lie below a concave curve", text="So each trapezium has less area than the strip under the curve.")],
           "Direction of error", "Interpretation", "Sketch a concave curve and a chord."),
        mc(r"Which number of ordinates allows Simpson's rule to be used?",
           r"$7$",
           [(r"$6$", "Six ordinates give five strips, an odd number."), (r"$4$", "Four ordinates give three strips, an odd number."), (r"$10$", "Ten ordinates give nine strips, an odd number.")],
           [S("Condition", text="Simpson needs an even number of strips, so an odd number of ordinates: $7$ ordinates give $6$ strips.")],
           "Condition for Simpson's rule", "Concept", "Strips = ordinates - 1, and strips must be even."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=NM, topic="Numerical solution of differential equations",
    title="Euler, improved Euler and Runge-Kutta methods",
    lesson="fmu2-euler-improved-euler-runge-kutta",
    questions=[
        NUM(r"Euler's method with $h = 0.2$ is applied to $\dfrac{dy}{dx} = 2y$, $y(0) = 3$. Find $y_1$.", 4.2, tolerance=0.01,
            steps=[S("Gradient at the start", math=r"f(0, 3) = 6"), S("Step", math=r"y_1 = 3 + 0.2(6) = 4.2")], concept="Euler's method", skill="Calculation", hint="y1 = y0 + h f(x0, y0)."),
        NUM(r"Euler's method with $h = 0.2$ is applied to $\dfrac{dy}{dx} = x^2 + y$, $y(0) = 1$. Find $y_2$ (the estimate at $x = 0.4$).", 1.448, tolerance=0.001,
            steps=[S("Step 1", math=r"y_1 = 1 + 0.2(0 + 1) = 1.2"), S("Step 2", math=r"y_2 = 1.2 + 0.2(0.04 + 1.2) = 1.448")], concept="Euler's method, two steps", skill="Calculation", hint="Update x as well as y in the second step."),
        mc(r"One step of the improved Euler method with $h = 0.2$ for $\dfrac{dy}{dx} = x^2 + y$, $y(0) = 1$ gives $y_1 =$",
           r"$1.224$",
           [(r"$1.2$", "That is the plain Euler value (the predictor)."), (r"$1.24$", "That is the gradient at the predicted point, not the new $y$."), (r"$1.448$", "That is the value of plain Euler after two steps.")],
           [S("Predictor", math=r"y^* = 1.2"), S("Gradient there", math=r"f(0.2, 1.2) = 0.04 + 1.2 = 1.24"), S("Corrector", math=r"y_1 = 1 + 0.1(1 + 1.24) = 1.224")],
           "Improved Euler method", "Calculation", "Average the gradient at the start and at the predicted point."),
        mc(r"In the fourth-order Runge-Kutta method the new value is $y_{n+1} = y_n + \dfrac{h}{6}(\ldots)$. The bracket is:",
           r"$k_1 + 2k_2 + 2k_3 + k_4$",
           [(r"$k_1 + k_2 + k_3 + k_4$", "The two middle slopes carry weight 2."), (r"$k_1 + 4k_2 + k_3$", "That is Simpson's pattern, a three-slope rule."), (r"$2k_1 + k_2 + k_3 + 2k_4$", "The end slopes have weight 1, the middle slopes weight 2.")],
           [S("Weights", text="The mid-step estimates $k_2$ and $k_3$ count twice; $k_1$ and $k_4$ once. The weights sum to $6$.")],
           "RK4 formula", "Recall", "The weights sum to 6, the divisor."),
        NUM(r"One step of fourth-order Runge-Kutta is applied to $\dfrac{dy}{dx} = y$, $y(0) = 1$, with $h = 0.5$. Find $y_1$ to 4 decimal places.", 1.6484, tolerance=0.0005,
            steps=[S("Slopes", math=r"k_1 = 1,\ k_2 = 1.25,\ k_3 = 1.3125,\ k_4 = 1.65625"), S("Combine", math=r"y_1 = 1 + \tfrac{0.5}{6}(1 + 2.5 + 2.625 + 1.65625) = 1.6484")],
            concept="Runge-Kutta step", skill="Calculation", hint="k2 and k3 use y + (h/2) k; k4 uses y + h k3."),
        mc(r"Euler's method is used with $h = 0.1$ and then $h = 0.05$. At a fixed $x$ the error roughly:",
           "halves",
           [("quarters", "That is the behaviour of the improved Euler method (second order)."), ("stays the same", "A smaller step reduces the error."), ("doubles", "A smaller step gives a smaller error.")],
           [S("Euler is first order", text="Global error is proportional to $h$.")],
           "Order of Euler's method", "Concept", "Think about the order of the global error."),
        mc(r"Euler's method with $h = 0.1$ is applied to $\dfrac{dy}{dx} = x + y$, $y(0) = 1$. $y(0.2)$ is estimated as:",
           r"$1.22$",
           [(r"$1.21$", "You used $x = 0$ in the second step. The second gradient is $f(0.1, 1.1) = 1.2$, not $1.1$."), (r"$1.2$", "That uses the constant gradient $1$ for both steps: $1 + 2(0.1)(1)$."), (r"$1.1$", "That is the estimate at $x = 0.1$, after only one step.")],
           [S("Step 1", math=r"y_1 = 1 + 0.1(1) = 1.1"), S("Step 2", math=r"y_2 = 1.1 + 0.1(0.1 + 1.1) = 1.22")],
           "Euler's method with x updated", "Calculation", "The second gradient uses x = 0.1 and y = 1.1."),
        mc(r"The exact solution of $\dfrac{dy}{dx} = x + y$, $y(0) = 1$, is convex (it bends upwards). Euler's estimates are therefore:",
           "too low",
           [("too high", "The tangent lies below a convex curve, so each step falls short."), ("exact", "Only a straight-line solution would be exact."), ("alternately high and low", "The tangent is always below a convex curve.")],
           [S("Tangent below a convex curve", text="Each step stays under the true curve and the errors accumulate downwards.")],
           "Direction of Euler error", "Interpretation", "Where does a tangent lie compared with a convex curve?"),
    ]))


# ================================================================ Advanced mechanics
_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Kinematics in polar coordinates",
    title="Polar components of velocity and acceleration",
    lesson="fmu2-polar-kinematics",
    questions=[
        mc(r"For the radial unit vector $\hat{\mathbf{r}}$ at angle $\theta$, $\dfrac{d\hat{\mathbf{r}}}{dt}$ equals:",
           r"$\dot\theta\,\hat{\boldsymbol{\theta}}$",
           [(r"$-\dot\theta\,\hat{\boldsymbol{\theta}}$", "That is a sign error. The radial vector turns towards the transverse direction."), (r"$\dot\theta\,\hat{\mathbf{r}}$", "A unit vector's derivative is perpendicular to it, never along it."), (r"$\dot r\,\hat{\boldsymbol{\theta}}$", r"The rate of change of direction depends on $\dot\theta$, not on $\dot r$.")],
           [S("Differentiate", math=r"\frac{d}{dt}(\cos\theta, \sin\theta) = \dot\theta(-\sin\theta, \cos\theta) = \dot\theta\,\hat{\boldsymbol{\theta}}")],
           "Derivative of the radial unit vector", "Recall", "Differentiate (cos t, sin t) with the chain rule."),
        NUM(r"A particle moves in a circle of radius $0.5$ m with constant $\dot\theta = 4$ rad/s. Find its radial acceleration component $a_r$ (negative means towards the centre).", -8, unit="m/s^2",
            steps=[S("Formula", math=r"a_r = \ddot r - r\dot\theta^2 = 0 - 0.5(16) = -8")], concept="Centripetal acceleration", skill="Calculation", hint="With r constant, a_r = - r times theta-dot squared."),
        mc(r"The transverse component of acceleration in polar coordinates is:",
           r"$r\ddot\theta + 2\dot r\dot\theta$",
           [(r"$r\ddot\theta$", "This misses the Coriolis term $2\\dot r\\dot\\theta$, which appears when $r$ changes."), (r"$\ddot r - r\dot\theta^2$", "That is the radial component."), (r"$r\dot\theta$", "That is the transverse component of the velocity.")],
           [S("Result", text="Differentiating $v_\\theta\\hat{\\boldsymbol{\\theta}}$ and $\\dot r\\hat{\\mathbf{r}}$ gives two transverse contributions.")],
           "Transverse acceleration", "Recall", "Two terms contribute; one involves both rates."),
        NUM(r"A particle moves with $r = 3 + 2t$ and $\theta = t^2$ (metres, radians, seconds). Find the transverse acceleration $a_\theta$ at $t = 1$ in m/s$^2$.", 18, unit="m/s^2",
            steps=[S("Values at $t = 1$", math=r"r = 5,\ \dot r = 2,\ \dot\theta = 2t = 2,\ \ddot\theta = 2"), S("Formula", math=r"a_\theta = r\ddot\theta + 2\dot r\dot\theta = 5(2) + 2(2)(2) = 18")],
            concept="Transverse acceleration of a spiral", skill="Calculation", hint="Find r, r-dot, theta-dot and theta-double-dot at t = 1."),
        mc(r"A particle moves with $r = 2t$ and $\theta = t$. Its speed at $t = 1$ is:",
           r"$2\sqrt{2} \approx 2.83$ m/s",
           [(r"$2$ m/s", "That is only the radial component $\\dot r$."), (r"$4$ m/s", "You added the components, $2 + 2$, instead of using Pythagoras."), (r"$8$ m/s", "That is $v^2 = 8$, the square of the speed.")],
           [S("Components", math=r"v_r = \dot r = 2,\quad v_\theta = r\dot\theta = 2(1) = 2"), S("Speed", math=r"v = \sqrt{4 + 4} = 2\sqrt2")],
           "Speed from polar components", "Calculation", "The components are perpendicular: combine them with Pythagoras."),
        NUM(r"A beetle crawls outward on a turntable turning at a constant $2$ rad/s. At the instant when $r = 0.3$ m its radial speed is $0.5$ m/s. Find the transverse acceleration in m/s$^2$.", 2, unit="m/s^2",
            steps=[S("Formula with $\\ddot\\theta = 0$", math=r"a_\theta = 2\dot r\dot\theta = 2(0.5)(2) = 2")], concept="Coriolis term", skill="Application", hint="With theta-double-dot = 0 only one term survives."),
        mc(r"A particle moves under a force always directed towards $O$. At $r = 4$ m, $\dot\theta = 0.5$ rad/s. At $r = 2$ m, $\dot\theta$ equals:",
           r"$2$ rad/s",
           [(r"$1$ rad/s", "That doubles $\\dot\\theta$ as $r$ halves; the correct law is $r^2\\dot\\theta$ constant, so it quadruples."), (r"$0.25$ rad/s", "$\\dot\\theta$ increases as the particle comes closer."), (r"$0.5$ rad/s", "$\\dot\\theta$ is not constant when $r$ changes.")],
           [S("No transverse force", math=r"r^2\dot\theta = 16(0.5) = 8"), S("At $r = 2$", math=r"\dot\theta = \frac{8}{4} = 2")],
           "Angular momentum per unit mass", "Reasoning", "Find the constant r squared times theta-dot."),
        mc(r"In the radial acceleration $\ddot r - r\dot\theta^2$ for motion along a rotating rod, the term $-r\dot\theta^2$ is:",
           "the centripetal acceleration, directed towards the origin",
           [("the Coriolis acceleration", "That is $2\\dot r\\dot\\theta$ in the transverse direction."), ("zero if the speed is constant", "It is zero only if $\\dot\\theta = 0$."), ("directed away from the origin", "The negative sign shows it points inwards.")],
           [S("Interpretation", text="For circular motion it is the whole acceleration, $a\\omega^2$ towards the centre.")],
           "Meaning of the terms", "Interpretation", "What is this term in uniform circular motion?"),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Variable mass systems",
    title="Rockets: thrust, acceleration and speed",
    lesson="fmu2-variable-mass-rockets",
    questions=[
        NUM(r"A rocket burns fuel at $5$ kg/s and ejects it at $2000$ m/s relative to the rocket. Find the thrust in N.", 10000, unit="N",
            steps=[S("Thrust", math=r"uk = 2000 \times 5 = 10\,000")], concept="Thrust of a rocket", skill="Calculation", hint="Thrust = exhaust speed times burn rate."),
        NUM(r"A rocket of total mass $500$ kg at lift-off burns fuel at $5$ kg/s and ejects it at $2000$ m/s relative to the rocket ($g = 10$ m/s$^2$). Find its initial acceleration in m/s$^2$.", 10, unit="m/s^2",
            steps=[S("Net force", math=r"10\,000 - 500(10) = 5000"), S("Acceleration", math=r"a = \frac{5000}{500} = 10")], concept="Initial acceleration", skill="Calculation", hint="Net force = thrust - weight; divide by the current mass."),
        mc(r"A rocket of mass $2000$ kg burns fuel at $10$ kg/s with exhaust speed $1500$ m/s ($g = 10$ m/s$^2$). At lift-off it:",
           "stays on the ground, because the thrust (15 000 N) is less than the weight (20 000 N)",
           [("lifts off with acceleration $0.5$ m/s$^2$ upwards", "The thrust is less than the weight, so the net force is not upwards."), ("lifts off, because the thrust 150 000 N is larger than the weight", "The thrust is $1500 \\times 10 = 15\\,000$ N, not $150\\,000$ N."), ("cannot be decided without the burn time", "Lift-off depends on thrust against weight at the start.")],
           [S("Thrust", math=r"uk = 1500 \times 10 = 15\,000\ \text{N}"), S("Weight", math=r"2000 \times 10 = 20\,000\ \text{N}")],
           "Lift-off condition", "Application", "Compare uk with mg."),
        NUM(r"A rocket of mass $800$ kg burns fuel at $4$ kg/s with exhaust speed $2500$ m/s. Find its speed after $50$ s from rest, in m/s ($g = 10$ m/s$^2$).", 219.2, tolerance=0.5, unit="m/s",
            steps=[S("Mass after 50 s", math=r"800 - 4(50) = 600\ \text{kg}"), S("Rocket equation", math=r"v = 2500\ln\frac{800}{600} - 10(50) = 719.2 - 500 = 219.2")],
            concept="Rocket equation with gravity", skill="Calculation", hint="v = u ln(m0/m) - g t."),
        NUM(r"A space probe in free space has initial mass $400$ kg and final mass $100$ kg after ejecting fuel at $3000$ m/s relative to it. Find its final speed from rest, in m/s.", 4159, tolerance=5, unit="m/s",
            steps=[S("Rocket equation, $g = 0$", math=r"v = 3000\ln\frac{400}{100} = 3000\ln4 = 4159")], concept="Rocket equation in free space", skill="Calculation", hint="v = u ln(m0/m)."),
        mc(r"As a rocket burns fuel at a constant rate its acceleration $\dfrac{uk - mg}{m}$:",
           "increases, because the mass falls while the thrust stays the same",
           [("stays constant, because the thrust is constant", "The mass in the denominator is decreasing."), ("decreases, because fuel is used up", "The thrust is unchanged and the mass falls, so $a$ rises."), ("is zero after the first second", "There is no reason for the acceleration to vanish while $uk > mg$.")],
           [S("Look at the formula", text="Numerator constant (if gravity is constant), denominator $m$ decreasing.")],
           "Variable acceleration", "Concept", "What changes in the formula as fuel burns?"),
        mc(r"In free space the final speed of a rocket from rest depends on:",
           "the exhaust speed and the ratio of initial to final mass only",
           [("the burn rate as well as the masses", "The time cancels out of $m\\,dv = -u\\,dm$."), ("the total time of burning only", "The time does not appear in $v = u\\ln(m_0/m)$."), ("the initial mass only", "The final mass also matters.")],
           [S("Integrate", math=r"dv = -u\frac{dm}{m} \Rightarrow v = u\ln\frac{m_0}{m}")],
           "Rocket equation", "Reasoning", "Separate the variables in m dv = - u dm."),
        NUM(r"For the first rocket (mass $500$ kg at lift-off, $k = 5$ kg/s, $u = 2000$ m/s), find the acceleration after $60$ s in m/s$^2$ ($g = 10$ m/s$^2$).", 40, unit="m/s^2",
            steps=[S("Mass after 60 s", math=r"500 - 300 = 200\ \text{kg}"), S("Acceleration", math=r"a = \frac{10\,000 - 2000}{200} = 40")], concept="Acceleration of a rocket later in its burn", skill="Calculation", hint="Use the mass at that time, not the initial mass."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Oblique collisions",
    title="Oblique impacts with walls and between spheres",
    lesson="fmu2-oblique-collisions",
    questions=[
        mc(r"A smooth sphere hits a smooth fixed wall obliquely. Which component of its velocity is unchanged?",
           "the component parallel to the wall",
           [("the component perpendicular to the wall", "That component reverses and is multiplied by $e$."), ("the speed", "The speed decreases unless $e = 1$ and the impact is head-on."), ("none of them", "A smooth wall exerts no force along its surface.")],
           [S("Reason", text="The wall's impulse is perpendicular to the wall, so the parallel velocity does not change.")],
           "Impact with a wall", "Concept", "In which direction does a smooth wall push?"),
        NUM(r"A ball hits a smooth wall at $12$ m/s, making $30^\circ$ with the wall. $e = 0.6$. Find its speed after the impact, in m/s, to 3 significant figures.", 11.0, tolerance=0.05, unit="m/s",
            steps=[S("Components", math=r"\text{parallel } 12\cos30^\circ = 10.392; \quad \text{perpendicular } 12\sin30^\circ = 6 \to 0.6(6) = 3.6"), S("Speed", math=r"\sqrt{10.392^2 + 3.6^2} = \sqrt{120.96} = 11.0")],
            concept="Speed after an oblique wall impact", skill="Calculation", hint="Parallel component stays; perpendicular is multiplied by e."),
        mc(r"A ball with velocity components $9$ m/s parallel to a smooth wall and $4$ m/s towards it rebounds with $e = 0.5$. After the impact:",
           "parallel 9 m/s, perpendicular 2 m/s away from the wall",
           [("parallel 4.5 m/s, perpendicular 2 m/s away", "The parallel component is not changed."), ("parallel 9 m/s, perpendicular 4 m/s away", "That would need $e = 1$."), ("parallel 9 m/s, perpendicular 8 m/s away", "That multiplies by $2$; $e = 0.5$.")],
           [S("Perpendicular", math=r"v' = 0.5 \times 4 = 2 \text{ (reversed)}")],
           "Restitution at a wall", "Calculation", "Which component does e multiply?"),
        NUM(r"A smooth sphere $A$ (mass $2$ kg, speed $8$ m/s) hits a stationary smooth sphere $B$ (mass $1$ kg). $A$'s velocity makes $30^\circ$ with the line of centres and $e = 0.5$. Find the speed of $B$ after the impact, in m/s.", 6.93, tolerance=0.02, unit="m/s",
            steps=[S("Component along the line", math=r"8\cos30^\circ = 6.928"), S("Momentum", math=r"2(6.928) = 2v_A + v_B"), S("Restitution", math=r"v_B - v_A = 0.5(6.928)"), S("Solve", math=r"v_B = 6.93")],
            concept="Oblique collision of two spheres", skill="Calculation", hint="Use only the components along the line of centres for momentum and restitution."),
        NUM(r"A sphere of mass $3$ kg moving at $10$ m/s hits a stationary sphere of mass $2$ kg. Its velocity makes $60^\circ$ with the line of centres; $e = 0.8$. Find the speed of the $2$ kg sphere after the impact in m/s.", 5.4, tolerance=0.02, unit="m/s",
            steps=[S("Along the line", math=r"u = 10\cos60^\circ = 5"), S("Momentum and restitution", math=r"15 = 3v_1 + 2v_2, \quad v_2 - v_1 = 4"), S("Solve", math=r"5v_1 = 7 \Rightarrow v_1 = 1.4,\ v_2 = 5.4")],
            concept="Oblique collision with restitution", skill="Calculation", hint="Write the two equations along the line of centres and eliminate one speed."),
        mc(r"A smooth sphere hits an identical stationary smooth sphere with $e = 1$, not head-on. After the impact the two spheres move:",
           "at right angles to each other",
           [("in the same direction", "They separate along different directions."), ("in opposite directions", "Only a head-on collision with the right masses does that."), ("along the same line as before", "The struck sphere moves along the line of centres, the other perpendicular to it.")],
           [S("Equal masses, e = 1", math=r"v_A = 0,\ v_B = u\cos\alpha \text{ along the line}"), S("$A$ keeps only the perpendicular component", text="So the paths are perpendicular.")],
           "Equal elastic spheres", "Reasoning", "Along the line, equal masses with e = 1 exchange the components."),
        NUM(r"A smooth sphere $A$ (2 kg, 8 m/s) hits a stationary smooth sphere $B$ (1 kg) with $A$'s velocity at $30^\circ$ to the line of centres and $e = 0.5$. Find the kinetic energy lost in the collision, in joules.", 12, tolerance=0.1, unit="J",
            steps=[S("Before", math=r"\tfrac12(2)(64) = 64"), S("After", math=r"A: \tfrac12(2)(3.464^2 + 4^2) = 28;\quad B: \tfrac12(1)(6.928^2) = 24"), S("Lost", math=r"64 - 52 = 12")],
            concept="Kinetic energy lost in an oblique collision", skill="Calculation", hint="Add the kinetic energy of both components of each sphere before and after."),
        NUM(r"A ball hits a smooth wall at $12$ m/s, making $30^\circ$ with the wall; $e = 0.6$. Find the angle the rebound path makes with the wall, in degrees.", 19.1, tolerance=0.2, unit="degrees",
            steps=[S("Components after", math=r"\text{parallel } 10.392, \quad \text{perpendicular } 3.6"), S("Angle", math=r"\tan\alpha = \frac{3.6}{10.392} \Rightarrow \alpha = 19.1^\circ")],
            concept="Direction after an impact", skill="Calculation", hint="tan of the angle = perpendicular component over parallel component after."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Damped and forced oscillations",
    title="Damped and forced simple harmonic motion",
    lesson="fmu2-damped-forced-oscillations",
    questions=[
        mc(r"A damped system obeys $\ddot x + 6\dot x + 5x = 0$. The motion is:",
           "heavily damped: no oscillation",
           [("lightly damped: oscillation with decreasing amplitude", "That needs complex roots; here $\\lambda = -1, -5$ are real."), ("critically damped", "Critical damping needs $b^2 = 4c$, i.e. $36 = 20$."), ("undamped", "There is a $6\\dot x$ term, so there is damping.")],
           [S("Auxiliary equation", math=r"\lambda^2 + 6\lambda + 5 = (\lambda + 1)(\lambda + 5) = 0"), S("Two real roots", text="Heavy damping.")],
           "Classifying damping", "Concept", "Solve the auxiliary equation."),
        NUM(r"A mass of $1$ kg on a spring of stiffness $16$ N/m has a resistance $c\dot x$. Find $c$ (in N s/m) for critical damping.", 8, unit="N s/m",
            steps=[S("Equation", math=r"\ddot x + c\dot x + 16x = 0"), S("Critical", math=r"c^2 = 4 \times 16 = 64 \Rightarrow c = 8")], concept="Critical damping condition", skill="Calculation", hint="b squared equals 4c for a repeated root."),
        NUM(r"The equation $\ddot x + 4\dot x + 13x = 0$ has solutions $e^{-2t}(A\cos\omega t + B\sin\omega t)$. Find $\omega$.", 3, unit="rad/s",
            steps=[S("Roots", math=r"\lambda = -2 \pm \sqrt{4 - 13} = -2 \pm 3i"), S("Frequency", math=r"\omega = 3")], concept="Frequency of damped oscillation", skill="Calculation", hint="Solve the auxiliary equation and read off the imaginary part."),
        mc(r"For critical damping, the general solution of $\ddot x + 6\dot x + 9x = 0$ is:",
           r"$x = (A + Bt)e^{-3t}$",
           [(r"$x = Ae^{-3t} + Be^{3t}$", "The repeated root is $-3$; there is no $+3$ root."), (r"$x = e^{-3t}(A\cos3t + B\sin3t)$", "That needs complex roots."), (r"$x = Ae^{-3t}$", "A second-order equation needs two arbitrary constants.")],
           [S("Repeated root", math=r"(\lambda + 3)^2 = 0 \Rightarrow x = (A + Bt)e^{-3t}")],
           "Critical damping solution", "Recall", "What is the form of the solution for a repeated root?"),
        NUM(r"In $\ddot x + 4\dot x + 13x = 0$ the oscillation has period $T = \dfrac{2\pi}{3}$ s and $k = 2$. Find the ratio of successive maximum displacements $e^{kT}$.", 65.9, tolerance=0.3,
            steps=[S("Exponent", math=r"kT = 2 \cdot \tfrac{2\pi}{3} = \tfrac{4\pi}{3} = 4.189"), S("Ratio", math=r"e^{4.189} = 65.9")], concept="Decay of amplitude", skill="Application", hint="Each period multiplies the amplitude by e to the power minus k T."),
        NUM(r"Find the amplitude of the steady-state response of $\ddot x + 2\dot x + 5x = 10\cos2t$, to 3 significant figures.", 2.43, tolerance=0.01,
            steps=[S("Formula", math=r"a = \frac{10}{\sqrt{(5 - 4)^2 + 4(1)(4)}} = \frac{10}{\sqrt{17}} = 2.43")], concept="Steady-state amplitude", skill="Calculation", hint="a = F / sqrt((w0^2 - W^2)^2 + 4k^2 W^2)."),
        mc(r"A particular integral of $\ddot x + 4x = 8\cos t$ is:",
           r"$x_p = \dfrac{8}{3}\cos t$",
           [(r"$x_p = 2\cos t$", "Substituting gives $3A = 8$, so $A = 8/3$; you divided by 4."), (r"$x_p = 8\cos t$", "Then $\\ddot x_p + 4x_p = 24\\cos t$, not $8\\cos t$."), (r"$x_p = 2t\sin t$", "That form is used at resonance, when the forcing frequency equals $\\omega_0 = 2$.")],
           [S("Try $A\\cos t$", math=r"-A + 4A = 8 \Rightarrow A = \tfrac83")],
           "Particular integral", "Calculation", "Substitute x = A cos t into the equation."),
        mc(r"An undamped oscillator with natural frequency $\omega_0$ is driven by a force at exactly $\omega_0$. The amplitude:",
           "grows without limit",
           [("becomes constant and large", "That needs damping to limit the growth."), ("decays to zero", "There is no damping to remove energy."), ("oscillates at twice the frequency", "The growth is linear in $t$ at the same frequency.")],
           [S("Resonance", text="The particular integral has the form $Ct\\sin\\omega_0 t$, whose amplitude $Ct$ increases without bound.")],
           "Resonance without damping", "Interpretation", "What happens to the energy supplied each cycle?"),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Moment of inertia of rigid bodies",
    title="Moments of inertia and the two axes theorems",
    lesson="fmu2-moment-of-inertia",
    questions=[
        NUM(r"Masses $2$ kg, $3$ kg and $5$ kg are fixed at perpendicular distances $0.5$ m, $1$ m and $0.4$ m from an axis. Find the moment of inertia about the axis in kg m$^2$.", 4.3, tolerance=0.01, unit="kg m^2",
            steps=[S("Sum", math=r"2(0.25) + 3(1) + 5(0.16) = 0.5 + 3 + 0.8 = 4.3")], concept="Moment of inertia of particles", skill="Calculation", hint="I = sum of m r squared."),
        mc(r"A uniform rod of mass $M$ and length $L$ has moment of inertia about an axis through one end, perpendicular to the rod, of:",
           r"$\dfrac{1}{3}ML^2$",
           [(r"$\dfrac{1}{12}ML^2$", "That is the value about the centre."), (r"$\dfrac{1}{2}ML^2$", "That is too large; it would put all the mass at $L/\\sqrt{2}$."), (r"$ML^2$", "That would put all the mass at distance $L$.")],
           [S("Integrate", math=r"\int_0^L x^2\frac{M}{L}dx = \frac{M}{L}\cdot\frac{L^3}{3} = \frac{ML^2}{3}")],
           "Rod about an end", "Recall", "Integrate x squared times the mass per unit length."),
        NUM(r"A uniform rod has mass $3$ kg and length $1.2$ m. Find its moment of inertia about a perpendicular axis through one end, in kg m$^2$.", 1.44, tolerance=0.01, unit="kg m^2",
            steps=[S("Standard result", math=r"\tfrac13(3)(1.2)^2 = 1.44")], concept="Rod about an end", skill="Calculation", hint="Use ML^2/3 for an end axis."),
        mc(r"A uniform disc of mass $M$ and radius $a$ has $I = \tfrac12 Ma^2$ about the perpendicular axis through its centre. About a diameter it is:",
           r"$\dfrac{1}{4}Ma^2$",
           [(r"$\dfrac{1}{2}Ma^2$", "That is the value about the perpendicular axis."), (r"$Ma^2$", "That is the value for a ring."), (r"$\dfrac{3}{2}Ma^2$", "That is the value about the perpendicular axis through the rim.")],
           [S("Perpendicular axes", math=r"I_x + I_y = I_z, \quad I_x = I_y \Rightarrow I_x = \tfrac14 Ma^2")],
           "Disc about a diameter", "Concept", "Use the perpendicular axes theorem."),
        NUM(r"A uniform disc has mass $4$ kg and radius $0.5$ m. Find its moment of inertia about a perpendicular axis through a point on the rim, in kg m$^2$.", 1.5, tolerance=0.01, unit="kg m^2",
            steps=[S("Centre", math=r"\tfrac12(4)(0.25) = 0.5"), S("Parallel axis, $d = 0.5$", math=r"0.5 + 4(0.25) = 1.5")], concept="Parallel axis theorem for a disc", skill="Calculation", hint="Add M d^2 to the value through the centre."),
        NUM(r"A uniform solid sphere has mass $4$ kg and radius $0.5$ m ($I = \tfrac25 Ma^2$ about a diameter). Find $I$ about a tangent, in kg m$^2$.", 1.4, tolerance=0.01, unit="kg m^2",
            steps=[S("Diameter", math=r"\tfrac25(4)(0.25) = 0.4"), S("Parallel axis, $d = 0.5$", math=r"0.4 + 4(0.25) = 1.4")], concept="Parallel axis theorem for a sphere", skill="Calculation", hint="The distance between a diameter and a tangent is the radius."),
        mc(r"The perpendicular axes theorem $I_z = I_x + I_y$ applies to:",
           "plane laminas (flat, thin bodies) only",
           [("any solid body", "For a solid body the theorem is false."), ("rods only", "A rod is one-dimensional; the theorem needs a flat body."), ("bodies rotating about the centre of mass only", "It is about three mutually perpendicular axes through a point, not about the centre of mass.")],
           [S("Condition", text="The body must lie in a plane (the $xy$ plane), with $z$ perpendicular to it.")],
           "Conditions for the perpendicular axes theorem", "Concept", "Where does the proof use the fact that z = 0 for every particle?"),
        mc(r"A thin square plate of mass $M$ and side $a$ has $I = \dfrac{1}{12}Ma^2$ about each of two perpendicular axes through its centre in its plane. About the perpendicular axis through the centre it is:",
           r"$\dfrac{1}{6}Ma^2$",
           [(r"$\dfrac{1}{12}Ma^2$", "That is the in-plane value; the perpendicular axes theorem adds the two."), (r"$\dfrac{1}{3}Ma^2$", "That is the value about a side."), (r"$\dfrac{1}{24}Ma^2$", "You halved instead of adding.")],
           [S("Add", math=r"I_z = \tfrac{1}{12}Ma^2 + \tfrac{1}{12}Ma^2 = \tfrac16 Ma^2")],
           "Perpendicular axes for a square plate", "Calculation", "I_z is the sum of the two in-plane values."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Rotation about a fixed axis",
    title="Torque, rotational energy and angular momentum",
    lesson="fmu2-rotation-fixed-axis",
    questions=[
        NUM(r"A flywheel with $I = 3$ kg m$^2$ is slowed by a constant braking torque of $6$ N m. Find the angular deceleration in rad/s$^2$.", 2, unit="rad/s^2",
            steps=[S("Law", math=r"\alpha = \frac{\Gamma}{I} = \frac63 = 2")], concept="Torque and angular acceleration", skill="Calculation", hint="Torque = I times alpha."),
        NUM(r"A uniform disc of mass $6$ kg and radius $0.4$ m has a tangential force of $15$ N at its rim. Find its angular acceleration in rad/s$^2$.", 12.5, tolerance=0.05, unit="rad/s^2",
            steps=[S("Moment of inertia", math=r"I = \tfrac12(6)(0.16) = 0.48"), S("Torque", math=r"15 \times 0.4 = 6"), S("Angular acceleration", math=r"\alpha = \frac{6}{0.48} = 12.5")], concept="Disc with a tangential force", skill="Calculation", hint="Find I for a disc, then the torque of the force."),
        NUM(r"A string is wound round a cylinder of radius $0.2$ m with $I = 0.5$ kg m$^2$. A $4$ kg mass hangs from it and is released. Find its acceleration in m/s$^2$ ($g = 10$ m/s$^2$).", 2.42, tolerance=0.02, unit="m/s^2",
            steps=[S("Mass", math=r"4g - T = 4a"), S("Cylinder", math=r"0.2T = 0.5\alpha, \ \alpha = \tfrac{a}{0.2} \Rightarrow T = 12.5a"), S("Solve", math=r"40 = 16.5a \Rightarrow a = 2.42")],
            concept="Mass falling from a pulley", skill="Application", hint="Write one equation for the mass and one for the cylinder; link a = r alpha."),
        mc(r"A $4$ kg mass hangs from a string wound round a cylinder and accelerates downwards at $2.42$ m/s$^2$ ($g = 10$ m/s$^2$). The tension in the string is:",
           "less than the weight of the mass, $T = m(g - a)$",
           [("equal to the weight $40$ N", "Then the mass would not accelerate."), ("greater than the weight", "The mass accelerates downwards, so the net force is downwards."), ("zero", "The string must turn the cylinder, so it is taut.")],
           [S("Newton's second law for the mass", math=r"T = 4(10 - 2.42) = 30.3\ \text{N}")],
           "Tension in the string", "Reasoning", "Apply Newton's second law to the falling mass."),
        NUM(r"A uniform rod of length $1.2$ m is hinged at one end and released from the horizontal. Find its angular speed at the lowest position in rad/s ($g = 10$ m/s$^2$).", 5, tolerance=0.02, unit="rad/s",
            steps=[S("Energy", math=r"\tfrac12\left(\tfrac13 ML^2\right)\omega^2 = Mg\tfrac{L}{2} \Rightarrow \omega^2 = \frac{3g}{L} = 25"), S("Speed", math=r"\omega = 5")],
            concept="Energy for a swinging rod", skill="Calculation", hint="The centre of mass falls L/2; use I = ML^2/3."),
        NUM(r"A uniform rod of length $1.2$ m swings about a horizontal axis through one end. Find the period of small oscillations in seconds ($g = 10$ m/s$^2$).", 1.78, tolerance=0.02, unit="s",
            steps=[S("Small angles", math=r"\ddot\theta = -\frac{3g}{2L}\theta"), S("Period", math=r"T = 2\pi\sqrt{\frac{2L}{3g}} = 2\pi\sqrt{0.08} = 1.78")], concept="Compound pendulum", skill="Application", hint="Equate I times theta-double-dot to the weight's torque and use sin theta ~ theta."),
        NUM(r"A turntable with $I = 2$ kg m$^2$ spins at $3$ rad/s. A ring with $I = 0.5$ kg m$^2$ is dropped on it and they rotate together. Find the final angular speed in rad/s.", 2.4, tolerance=0.01, unit="rad/s",
            steps=[S("Conservation of angular momentum", math=r"2(3) = (2 + 0.5)\omega \Rightarrow \omega = 2.4")], concept="Conservation of angular momentum", skill="Application", hint="No external torque: I omega is conserved."),
        mc(r"A skater spinning freely pulls in her arms so that $I$ halves. Her angular speed:",
           "doubles",
           [("halves", "A smaller $I$ means a larger $\\omega$."), ("stays the same", "$I\\omega$ is constant, not $\\omega$."), ("quadruples", "The factor is $I_1/I_2 = 2$, not squared.")],
           [S("Conservation", math=r"I\omega = \tfrac12 I\,\omega' \Rightarrow \omega' = 2\omega")],
           "Angular momentum conservation", "Concept", "Write I1 w1 = I2 w2."),
    ]))

_slots.clear()
SETS.append(practice_set(
    module=MP, topic="Probability generating functions",
    title="Probability generating functions",
    lesson="fmu2-probability-generating-functions",
    questions=[
        mc(r"For any probability generating function $G_X(t)$:",
           r"$G_X(1) = 1$",
           [(r"$G_X(0) = 1$", r"$G_X(0) = P(X = 0)$, which is usually less than $1$."), (r"$G_X(1) = E(X)$", r"$G_X'(1) = E(X)$; $G_X(1)$ is the total probability."), (r"$G_X'(0) = 1$", r"$G_X'(0) = P(X = 1)$.")],
           [S("Reason", math=r"G(1) = \sum p_r = 1")], "Property G(1) = 1", "Recall", "What is the sum of all the probabilities?"),
        NUM(r"$X$ has $P(X = 0) = 0.1$, $P(X = 1) = 0.3$, $P(X = 2) = 0.4$, $P(X = 3) = 0.2$. Find $E(X)$ using the generating function.", 1.7, tolerance=0.001,
            steps=[S("Pgf", math=r"G(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3"), S("Derivative at 1", math=r"G'(1) = 0.3 + 0.8 + 0.6 = 1.7")], concept="Mean from G'(1)", skill="Calculation", hint="Differentiate G and put t = 1."),
        NUM(r"$X$ has $P(X = 0) = 0.1$, $P(X = 1) = 0.3$, $P(X = 2) = 0.4$, $P(X = 3) = 0.2$. Find $\operatorname{Var}(X)$ using the generating function.", 0.81, tolerance=0.001,
            steps=[S("Second derivative", math=r"G''(1) = 0.8 + 1.2 = 2.0"), S("Variance", math=r"2.0 + 1.7 - 1.7^2 = 0.81")], concept="Variance from G", skill="Calculation", hint="Var = G''(1) + G'(1) - G'(1)^2."),
        mc(r"The generating function of $B(n, p)$ with $q = 1 - p$ is:",
           r"$(q + pt)^n$",
           [(r"$(p + qt)^n$", "The probability of success $p$ goes with the power of $t$."), (r"$q + pt^n$", "The binomial theorem raises the whole bracket to the power $n$."), (r"$e^{np(t - 1)}$", "That is the Poisson generating function with mean $np$.")],
           [S("Binomial theorem", math=r"\sum \binom nr p^r q^{n - r}t^r = (q + pt)^n")], "Binomial pgf", "Recall", "Each trial contributes (q + p t)."),
        mc(r"$X$ has $G(t) = \tfrac14(1 + t)^2$. $P(X = 1)$ equals:",
           r"$\dfrac12$",
           [(r"$\dfrac14$", "That is $P(X = 0)$ or $P(X = 2)$, the constant and the $t^2$ coefficients."), (r"$\dfrac34$", "That is $1 - P(X = 0)$."), (r"$1$", "That is $G(1)$.")],
           [S("Expand", math=r"G(t) = \tfrac14 + \tfrac12 t + \tfrac14 t^2")], "Reading probabilities from G", "Calculation", "Expand G(t) and read the coefficient of t."),
        NUM(r"A die is rolled until a $6$ appears. $X$ is the number of rolls. Find $\operatorname{Var}(X)$.", 30, tolerance=0.01,
            steps=[S("Geometric with $p = 1/6$", math=r"\operatorname{Var} = \frac{q}{p^2} = \frac{5/6}{1/36} = 30")], concept="Variance of the geometric distribution", skill="Calculation", hint="Var = q / p^2."),
        mc(r"$X$ and $Y$ are independent with generating functions $G_X$ and $G_Y$. The generating function of $X + Y$ is:",
           r"$G_X(t)\,G_Y(t)$",
           [(r"$G_X(t) + G_Y(t)$", "Adding the functions gives a total probability of $2$, not $1$."), (r"$G_X(G_Y(t))$", "That is the generating function of a random sum, not of $X + Y$."), (r"$G_X(t)^{Y}$", "$Y$ is a random variable, not an exponent here.")],
           [S("Independence", math=r"E(t^{X + Y}) = E(t^X)E(t^Y)")], "Sum of independent variables", "Concept", "t to the power X+Y splits into a product."),
        NUM(r"$X$ and $Y$ are the scores on two fair dice. Using generating functions, find $P(X + Y = 7)$ to 3 decimal places.", 0.167, tolerance=0.001,
            steps=[S("Pgf of the total", math=r"\tfrac1{36}(t + t^2 + \cdots + t^6)^2"), S("Coefficient of $t^7$", math=r"\tfrac{6}{36} = 0.167")], concept="Sum of two dice by pgf", skill="Application", hint="Count the ways to make 7 in the square of the polynomial."),
    ]))


# ================================================================ Examination: lesson sets
_slots.clear()
EXAM_1 = [
    NUM(r"A paper has $50$ multiple-choice questions and a time limit of $90$ minutes (KKEVO practice setting). How many minutes per question is that, on average?", 1.8, tolerance=0.01, unit="minutes",
        steps=[S("Divide", math=r"90 \div 50 = 1.8")], concept="Paper 1 time planning", skill="Calculation", hint="Total time divided by the number of questions."),
    mc(r"Find $\displaystyle\lim_{x \to 0}\frac{e^x - 1 - x}{x^2}$.",
       r"$\dfrac{1}{2}$",
       [(r"$0$", "Both numerator and denominator tend to $0$: the limit is not simply $0$."), (r"$1$", "The first surviving term is $\\frac{x^2}{2}$, not $x^2$."), (r"$\infty$", "The numerator behaves like $x^2/2$, so the ratio stays finite.")],
       [S("Series", math=r"e^x - 1 - x = \frac{x^2}{2} + \frac{x^3}{6} + \cdots"), S("Divide", math=r"\to \frac12"), S("Check", text="At $x = 0.01$ the value is $0.5017$.")],
       "Using a test value and a series", "Application", "Use the Maclaurin series of e^x, or test x = 0.01 on the calculator."),
    mc(r"$G$ is a group of order $15$. Which cannot be the order of an element of $G$?",
       r"$4$",
       [(r"$3$", "$3$ divides $15$, so it is allowed by Lagrange's theorem."), (r"$5$", "$5$ divides $15$."), (r"$15$", "A cyclic group of order 15 has an element of order 15.")],
       [S("Lagrange", text="The order of an element divides the order of the group. Divisors of $15$: $1, 3, 5, 15$.")],
       "Quick structural check with Lagrange", "Reasoning", "Which numbers divide 15?"),
    NUM(r"A linear map $T : \mathbb{R}^5 \to \mathbb{R}^3$ has rank $2$. Find the dimension of its kernel.", 3,
        steps=[S("Rank-nullity", math=r"\text{nullity} = 5 - 2 = 3")], concept="Rank-nullity as a quick check", skill="Calculation", hint="Use the dimension of the domain."),
    mc(r"A question asks for the first three non-zero terms of the expansion of $\ln x$ in powers of $(x - 1)$. This needs:",
       "a Taylor series about $x = 1$",
       [("a Maclaurin series about $x = 0$", "$\\ln x$ is undefined at $0$, and the question asks for powers of $(x - 1)$."), ("a binomial series in $x$", "There is no integer or fractional power of $x$ to expand."), ("L'Hopital's rule", "L'Hopital's rule is for limits, not for series.")],
       [S("Expansion point", text="Powers of $(x - a)$ with $a = 1$: the Taylor series, $f(a) + f'(a)(x - a) + \\cdots$.")],
       "Taylor versus Maclaurin", "Concept", "About which point is the series required?"),
    mc(r"Simpson's rule with $4$ strips for $\int_a^b y\,dx$ uses the weights (on $y_0, y_1, y_2, y_3, y_4$):",
       r"$\dfrac{h}{3}\,(1, 4, 2, 4, 1)$",
       [(r"$\dfrac{h}{2}\,(1, 2, 2, 2, 1)$", "These are the trapezium rule weights."), (r"$\dfrac{h}{3}\,(1, 2, 4, 2, 1)$", "The odd-numbered ordinates have weight $4$."), (r"$\dfrac{h}{3}\,(1, 4, 4, 4, 1)$", "The even-numbered inner ordinate has weight $2$.")],
       [S("Pattern", text="Ends once, odd inner ordinates four times, even inner ordinates twice, all multiplied by $h/3$.")],
       "Simpson's rule against the trapezium rule", "Recall", "Remember the pattern 1, 4, 2, 4, 1."),
    mc(r"A particle has acceleration $a = 4 - 2t$ m/s$^2$ and velocity $1$ m/s at $t = 0$. To find its velocity at $t = 3$:",
       r"integrate: $v = 1 + 4t - t^2 = 4$ m/s",
       [(r"use $v = u + at$ with $a = 4$", "The acceleration is not constant, so $v = u + at$ does not apply."), (r"use $v = u + at$ with $a = 4 - 6 = -2$", "That evaluates $a$ at $t = 3$ and treats it as constant."), (r"differentiate $a$", "Velocity is the integral, not the derivative, of acceleration.")],
       [S("Integrate", math=r"v = \int (4 - 2t)\,dt = 4t - t^2 + 1 \Rightarrow v(3) = 4")],
       "Variable acceleration", "Concept", "Is the acceleration constant?"),
    mc(r"After $45$ minutes of a $90$-minute multiple-choice paper you have answered $20$ of $50$ questions. The best next step is to:",
       "skip any question not done in about 2 minutes and return to flagged questions later",
       [("spend 5 minutes on each remaining question", "That leaves time for only 9 more questions."), ("stop and leave the rest blank", "A blank scores nothing; unless your paper says otherwise, answer every question."), ("go back and re-check the first 20 questions", "That uses the time you need for the unanswered ones.")],
       [S("Two-pass method", text="Do the quick questions first, flag the long ones, and use the time saved.")],
       "Two-pass time management", "Application", "Which approach gives the most answered questions?"),
]
SETS.append(practice_set(module="Examination", topic="Paper 1", title="Paper 1 technique: multiple-choice strategy",
                         lesson="fmxu-exam-paper-1-multiple-choice-strategy", questions=EXAM_1))

_slots.clear()
EXAM_2 = [
    mc(r"A question says 'Show that $\displaystyle\int_0^1 xe^x\,dx = 1$'. The best answer is to:",
       r"use integration by parts, show $[xe^x - e^x]_0^1$ and evaluate each limit",
       [("write $1 = 1$", "That assumes the result instead of proving it."), ("use the trapezium rule with four strips", "A numerical estimate cannot prove an exact value."), ("copy the given result", "Recopying earns no marks in a show-that question.")],
       [S("Integrate by parts", math=r"[xe^x - e^x]_0^1 = (e - e) - (0 - 1) = 1")],
       "Show-that questions", "Concept", "A show-that question needs every step of working."),
    NUM(r"A table has $9$ ordinates for $\displaystyle\int_1^5 y\,dx$. Find the step length $h$.", 0.5, tolerance=0.001,
        steps=[S("Strips", text="$9$ ordinates give $8$ strips."), S("Step", math=r"h = \frac{5 - 1}{8} = 0.5")], concept="Step length in a numerical table", skill="Calculation", hint="Number of strips = ordinates - 1."),
    NUM(r"In the Taylor series of $\ln x$ about $x = 1$, find the coefficient of $(x - 1)^3$ (as a decimal to 3 places).", 0.333, tolerance=0.001,
        steps=[S("Derivatives at 1", math=r"f''' = \frac{2}{x^3} \Rightarrow f'''(1) = 2"), S("Coefficient", math=r"\frac{f'''(1)}{3!} = \frac{2}{6} = 0.333")], concept="Taylor series coefficient", skill="Calculation", hint="f''' (1) divided by 3 factorial."),
    NUM(r"A particle starts at the origin with velocity $1$ m/s and has acceleration $a = 4 - 2t$ m/s$^2$. Find its displacement at $t = 3$ s, in metres.", 12, unit="m",
        steps=[S("Velocity", math=r"v = 1 + 4t - t^2"), S("Displacement", math=r"x = t + 2t^2 - \frac{t^3}{3} = 3 + 18 - 9 = 12")], concept="Displacement with variable acceleration", skill="Calculation", hint="Integrate the acceleration twice, with the initial conditions."),
    mc(r"A fair coin is tossed $20$ times and $X$ is the number of heads. The correct model for $X$ is:",
       r"binomial $B(20, 0.5)$",
       [(r"geometric", "A geometric variable counts trials up to the first success; here the number of trials is fixed."), (r"Poisson with mean $10$", "A Poisson approximation needs large $n$ and small $p$; $n = 20$, $p = 0.5$ is not suitable, and the exact binomial is available."), (r"normal $N(10, 5)$ without any correction", "$X$ is discrete: a normal approximation needs a continuity correction.")],
       [S("Conditions", text="Fixed number of independent trials, two outcomes, constant probability: binomial.")],
       "Choosing the distribution", "Application", "Is the number of trials fixed?"),
    NUM(r"$X \sim B(40, 0.5)$. In a normal approximation to $P(X \ge 24)$ (with continuity correction), find the $z$-value to 3 decimal places.", 1.107, tolerance=0.002,
        steps=[S("Parameters", math=r"\mu = 20, \quad \sigma = \sqrt{10}"), S("Correction", math=r"P(X \ge 24) \to P(Y \ge 23.5)"), S("Standardise", math=r"z = \frac{23.5 - 20}{\sqrt{10}} = 1.107")], concept="Continuity correction", skill="Calculation", hint="X >= 24 becomes Y >= 23.5."),
    mc(r"A normal approximation is used for a discrete variable $X$. $P(X \ge 24)$ should be approximated by:",
       r"$P(Y > 23.5)$",
       [(r"$P(Y > 24)$", "This ignores the continuity correction and under-counts the value $24$."), (r"$P(Y > 24.5)$", "That would be $P(X \\ge 25)$."), (r"$P(Y > 23)$", "The correction is half a unit, not a whole unit.")],
       [S("Continuity correction", text="The value $24$ occupies the interval $[23.5, 24.5)$, so $X \\ge 24$ starts at $23.5$.")],
       "Continuity correction", "Concept", "The value 24 is the interval from 23.5 to 24.5."),
    mc(r"Part (a) of a question gives the value $x = 2.4567\ldots$ on your calculator and part (b) asks for $x^2$ to 3 significant figures. You should:",
       r"use the stored full value, giving $6.04$",
       [(r"use the rounded value $2.46$, giving $6.05$", "Using a rounded value changes the final digit."), (r"use $2$, giving $4$", "That is far too crude."), (r"write the answer $2.46$", "That is the answer to part (a), not part (b).")],
       [S("Full value", math=r"2.4567^2 = 6.04")],
       "Carrying values forward", "Application", "Which value keeps the full accuracy?"),
]
SETS.append(practice_set(module="Examination", topic="Paper 2", title="Paper 2 technique: structured questions",
                         lesson="fmxu-exam-paper-2-structured-questions", questions=EXAM_2))

# ================================================================ Paper 1 mock A (50 questions)
_slots.clear()
P1 = []


def q(topic_module, topic, prompt, right, wrongs, steps, hint, skill="Calculation"):
    P1.append(mc(prompt, right, wrongs, steps, topic, skill, hint))


# --- Advanced Differential & Integral Calculus (10)
q(CA, "Inverse trigonometric functions in calculus", r"Differentiate $\arcsin(2x)$ with respect to $x$.",
  r"$\dfrac{2}{\sqrt{1 - 4x^2}}$",
  [(r"$\dfrac{1}{\sqrt{1 - 4x^2}}$", "You forgot the chain-rule factor $2$."), (r"$\dfrac{2}{1 + 4x^2}$", r"That is the derivative of $\arctan(2x)$."), (r"$\dfrac{-2}{\sqrt{1 - 4x^2}}$", r"That is the derivative of $\arccos(2x)$.")],
  [S("Chain rule", math=r"\frac{d}{dx}\arcsin u = \frac{u'}{\sqrt{1 - u^2}}, \ u = 2x")], "Use d/dx arcsin u = u' / sqrt(1 - u^2).")
q(CA, "Inverse trigonometric functions in calculus", r"Evaluate $\displaystyle\int_0^3 \frac{dx}{9 + x^2}$.",
  r"$\dfrac{\pi}{12}$",
  [(r"$\dfrac{\pi}{4}$", "You forgot the factor $\\frac13$: $\\int \\frac{dx}{a^2 + x^2} = \\frac1a\\arctan\\frac xa$."), (r"$\dfrac{\pi}{36}$", "The factor is $\\frac13$, not $\\frac19$."), (r"$\dfrac{3\pi}{4}$", "The factor is $\\frac13$, not $3$.")],
  [S("Standard integral", math=r"\frac13\left[\arctan\frac{x}{3}\right]_0^3 = \frac13\cdot\frac{\pi}{4}")], "Use the standard form with a = 3.")
q(CA, "Leibniz's theorem", r"The fifth derivative of $x^2e^x$ at $x = 0$ is:",
  r"$20$",
  [(r"$0$", "Only the term with the second derivative of $x^2$ survives at $x = 0$; it is not zero."), (r"$10$", r"You used $\binom52 = 10$ but forgot the factor $(x^2)'' = 2$."), (r"$40$", "You doubled the correct value.")],
  [S("Leibniz", math=r"\sum \binom5k (x^2)^{(k)}(e^x)^{(5-k)}"), S("At $x = 0$ only $k = 2$ survives", math=r"\binom52\cdot 2\cdot 1 = 20")], "Which terms of the Leibniz sum are non-zero at x = 0?")
q(CA, "Leibniz's theorem", r"The third derivative of $x^2e^{2x}$ at $x = 0$ is:",
  r"$12$",
  [(r"$6$", r"You forgot that $(e^{2x})' = 2e^{2x}$."), (r"$4$", r"You omitted the binomial coefficient $\binom32 = 3$."), (r"$0$", "The term with $(x^2)''$ does not vanish at $0$.")],
  [S("Only $k = 2$ survives", math=r"\binom32\cdot 2\cdot(e^{2x})'\big|_{0} = 3 \cdot 2 \cdot 2 = 12")], "Use the Leibniz sum and evaluate at x = 0.")
q(CA, "Taylor series and L'Hopital's rule", r"Find $\displaystyle\lim_{x \to 0}\frac{e^x - 1 - x}{x^2}$.",
  r"$\dfrac12$",
  [(r"$0$", "Both functions tend to $0$; the limit is not $0$."), (r"$1$", r"The first term of the numerator is $\frac{x^2}{2}$."), (r"$\infty$", "The numerator is of order $x^2$, so the ratio is finite.")],
  [S("Series", math=r"\frac{x^2/2 + x^3/6 + \cdots}{x^2} \to \frac12")], "Expand e^x or apply L'Hopital twice.")
q(CA, "Taylor series and L'Hopital's rule", r"In the Taylor series of $\sin x$ about $x = \dfrac{\pi}{2}$, the coefficient of $\left(x - \dfrac{\pi}{2}\right)^2$ is:",
  r"$-\dfrac12$",
  [(r"$\dfrac12$", "The sign is negative: $f''(\\frac\\pi2) = -\\sin\\frac\\pi2 = -1$."), (r"$0$", "That is the Maclaurin series of $\\sin x$, which has no $x^2$ term."), (r"$-1$", "You forgot to divide by $2!$.")],
  [S("Derivative", math=r"f''(x) = -\sin x \Rightarrow f''\left(\tfrac\pi2\right) = -1"), S("Coefficient", math=r"\frac{f''}{2!} = -\frac12")], "Find f'' at the expansion point, then divide by 2 factorial.")
q(CA, "Reduction formulae", r"Let $I_n = \displaystyle\int_0^{\pi/2}\sin^n x\,dx$, with $I_n = \dfrac{n-1}{n}I_{n-2}$. Then $I_4$ is:",
  r"$\dfrac{3\pi}{16}$",
  [(r"$\dfrac{3}{8}$", r"You started from $I_0 = 1$; in fact $I_0 = \frac\pi2$."), (r"$\dfrac{\pi}{4}$", "That is $I_2$."), (r"$\dfrac{3\pi}{8}$", r"You used $\frac{n-1}{n}$ once with $I_0$ instead of twice.")],
  [S("Apply twice", math=r"I_4 = \tfrac34 I_2 = \tfrac34\cdot\tfrac12 I_0 = \tfrac38\cdot\tfrac\pi2 = \tfrac{3\pi}{16}")], "I_0 = pi/2. Apply the formula for n = 2 and n = 4.")
q(CA, "Reduction formulae", r"Let $I_n = \displaystyle\int_0^1 x^ne^x\,dx$, with $I_n = e - nI_{n-1}$ and $I_1 = 1$. Then $I_3$ is:",
  r"$6 - 2e$",
  [(r"$2e - 6$", "The sign is reversed."), (r"$e - 3$", r"You forgot to substitute $I_2 = e - 2$; the formula gives $e - 3I_2$."), (r"$e - 6$", "That uses $I_2 = 2$ instead of $e - 2$.")],
  [S("$I_2$", math=r"I_2 = e - 2I_1 = e - 2"), S("$I_3$", math=r"I_3 = e - 3(e - 2) = 6 - 2e")], "Find I_2 first.")
q(CA, "Arc length and surface area of revolution", r"The length of the curve $y = x^{3/2}$ from $x = 0$ to $x = 4$ is:",
  r"$9.07$",
  [(r"$12.00$", "You omitted the square root: $\\int(1 + y')\\,dx$ is not the arc length."), (r"$20.42$", r"You forgot the factor $\frac49$ from integrating $\sqrt{1 + \frac94x}$."), (r"$30.62$", "You forgot the factor $\\frac{8}{27}$.")],
  [S("Formula", math=r"L = \int_0^4\sqrt{1 + \tfrac94 x}\,dx = \tfrac{8}{27}\left[\left(1 + \tfrac94x\right)^{3/2}\right]_0^4 = \tfrac{8}{27}(10\sqrt{10} - 1)")], "Use L = integral of sqrt(1 + (dy/dx)^2).")
q(CA, "Arc length and surface area of revolution", r"The line $y = x$ for $0 \le x \le 1$ is rotated about the $x$-axis. The curved surface area is:",
  r"$\pi\sqrt2 \approx 4.44$",
  [(r"$2\pi \approx 6.28$", r"You forgot the factor $\sqrt{1 + y'^2} = \sqrt2$."), (r"$\pi \approx 3.14$", "You forgot both the $\\sqrt2$ and one factor of $2$."), (r"$2\pi\sqrt2 \approx 8.89$", r"$\int_0^1 x\,dx = \frac12$: you omitted the $\frac12$.")],
  [S("Formula", math=r"S = 2\pi\int_0^1 y\sqrt{1 + y'^2}\,dx = 2\pi\sqrt2\int_0^1 x\,dx = \pi\sqrt2")], "S = 2 pi integral of y sqrt(1 + y'^2) dx.")
# --- Ordinary Differential Equations (8)
q(OD, "First-order separable and linear equations", r"Solve $\dfrac{dy}{dx} = 2xy$ with $y(0) = 3$. The value of $y(1)$ is:",
  r"$3e$",
  [(r"$3e^2$", r"You wrote $y = 3e^{2x}$; the integral of $2x$ is $x^2$."), (r"$e^3$", "That is not the solution."), (r"$3 + e$", "The solution is a product, not a sum.")],
  [S("Separate", math=r"\int\frac{dy}{y} = \int 2x\,dx \Rightarrow \ln y = x^2 + c"), S("Initial condition", math=r"y = 3e^{x^2},\ y(1) = 3e")], "Separate the variables and integrate each side.")
q(OD, "First-order separable and linear equations", r"Solve $\dfrac{dy}{dx} + 2y = e^{-x}$ with $y(0) = 0$. Then $y(1) =$",
  r"$e^{-1} - e^{-2} \approx 0.2325$",
  [(r"$e^{-1} + e^{-2} \approx 0.5032$", "The constant is $-1$, because $y(0) = 1 + C = 0$."), (r"$e^{-1} \approx 0.3679$", "You left out the complementary function $Ce^{-2x}$."), (r"$\tfrac12\left(e^{-1} - e^{-2}\right) \approx 0.1163$", "You divided by $2$ by mistake.")],
  [S("Integrating factor", math=r"e^{2x}:\ (ye^{2x})' = e^{x} \Rightarrow y = e^{-x} + Ce^{-2x}"), S("Initial condition", math=r"C = -1")], "Multiply through by the integrating factor e^{2x}.")
q(OD, "Bernoulli equations", r"Solve $\dfrac{dy}{dx} + y = y^2$ with $y(0) = \tfrac12$. Then $y(1) =$",
  r"$\dfrac{1}{1 + e} \approx 0.269$",
  [(r"$\dfrac{1}{1 + e^{-1}} \approx 0.731$", "The exponent has the wrong sign."), (r"$\dfrac{1}{2e} \approx 0.184$", "That treats the equation as linear and ignores $y^2$."), (r"$\dfrac{1}{e - 1} \approx 0.582$", "That uses $C = -1$ instead of $C = 1$.")],
  [S("Let $v = 1/y$", math=r"v' - v = -1 \Rightarrow v = 1 + Ce^x"), S("$y(0) = \\tfrac12$ gives $v(0) = 2$", math=r"C = 1,\ y = \frac{1}{1 + e^x}")], "Substitute v = y^(-1).")
q(OD, "Bernoulli equations", r"The equation $\dfrac{dy}{dx} + \dfrac{y}{x} = xy^3$ is reduced to a linear equation by the substitution:",
  r"$v = y^{-2}$",
  [(r"$v = y^{-3}$", "The substitution is $v = y^{1 - n}$ with $n = 3$, giving $y^{-2}$."), (r"$v = y^{2}$", "The exponent is $1 - n = -2$, negative."), (r"$v = y^{-1}$", "That is for $n = 2$.")],
  [S("Bernoulli", text=r"$y' + Py = Qy^n$ uses $v = y^{1-n}$; here $n = 3$.")], "Identify n in y' + P y = Q y^n.")
q(OD, "Second-order linear equations", r"Solve $y'' - 3y' + 2y = 0$ with $y(0) = 0$, $y'(0) = 1$. Then $y(1) =$",
  r"$e^2 - e \approx 4.67$",
  [(r"$e^2 + e \approx 10.11$", "The coefficients are $1$ and $-1$: $A + B = 0$ and $2A + B = 1$."), (r"$e^2 \approx 7.39$", "You dropped the $-e^x$ term."), (r"$e - 1 \approx 1.72$", "That is not the solution.")],
  [S("Roots", math=r"\lambda^2 - 3\lambda + 2 = 0 \Rightarrow \lambda = 1, 2"), S("Conditions", math=r"y = Ae^{x} + Be^{2x}: A + B = 0,\ A + 2B = 1 \Rightarrow y = e^{2x} - e^{x}")], "Solve the auxiliary equation first.")
q(OD, "Second-order linear equations", r"The general solution of $y'' + 2y' + 5y = 0$ is:",
  r"$y = e^{-x}(A\cos2x + B\sin2x)$",
  [(r"$y = e^{x}(A\cos2x + B\sin2x)$", "The real part of the roots $-1 \\pm 2i$ is $-1$."), (r"$y = e^{-2x}(A\cos x + B\sin x)$", "The real and imaginary parts are swapped."), (r"$y = Ae^{-x} + Be^{-5x}$", "The auxiliary equation has complex roots, not $-1$ and $-5$.")],
  [S("Auxiliary equation", math=r"\lambda = -1 \pm 2i")], "Use the quadratic formula on the auxiliary equation.")
q(OD, "Reducible differential equations", r"Solve $y'' = 2y'$ (let $p = y'$).",
  r"$y = Ae^{2x} + B$",
  [(r"$y = Ae^{2x}$", "A second-order equation needs two arbitrary constants."), (r"$y = Ae^{x^2} + B$", "$p' = 2p$ gives $e^{2x}$, not $e^{x^2}$."), (r"$y = Ax + B$", "That solves $y'' = 0$ only.")],
  [S("Substitute", math=r"p' = 2p \Rightarrow p = Ae^{2x}"), S("Integrate", math=r"y = \tfrac{A}{2}e^{2x} + B")], "Let p = y' and solve the first-order equation for p.")
q(OD, "Reducible differential equations", r"The general solution of $xy'' = y'$ is:",
  r"$y = ax^2 + b$",
  [(r"$y = ax + b$", "That has $y'' = 0$ and $xy'' = 0 \\neq y' = a$."), (r"$y = a\ln x + b$", "That gives $y' = a/x$ and $xy'' = -a/x \\neq y'$."), (r"$y = ae^x + b$", "Then $xy'' = xae^x \\neq ae^x$.")],
  [S("Let $p = y'$", math=r"xp' = p \Rightarrow p = cx"), S("Integrate", math=r"y = \tfrac{c}{2}x^2 + b")], "Let p = y' and separate the variables.")
# --- Group theory (8)
q(GR, "Binary operations and group axioms", r"On $\mathbb{R}$ define $a * b = a + b + 2$. The identity element is:",
  r"$-2$",
  [(r"$0$", r"$a * 0 = a + 2 \neq a$."), (r"$2$", r"$a * 2 = a + 4 \neq a$."), (r"$1$", r"$a * 1 = a + 3 \neq a$.")],
  [S("Solve $a * e = a$", math=r"a + e + 2 = a \Rightarrow e = -2")], "Find e with a * e = a for every a.")
q(GR, "Binary operations and group axioms", r"Which is a group under the stated operation?",
  r"$\{1, 2, 3, 4\}$ under multiplication modulo $5$",
  [(r"$\mathbb{Z}$ under subtraction", "Subtraction is not associative: $(5 - 3) - 1 \\neq 5 - (3 - 1)$."), (r"$\{1, 2, 3, \dots\}$ under addition", "There is no identity element in the set."), (r"$\{1, 2, 3, 4, 5\}$ under multiplication modulo $6$", "The set is not closed: $2 \\times 3 \\equiv 0$, which is not in it.")],
  [S("Check the axioms", text="Closed, associative, identity $1$; inverses $1 \\to 1$, $2 \\to 3$, $3 \\to 2$, $4 \\to 4$.")], "Test closure, identity and inverses.")
q(GR, "Cyclic and permutation groups", r"The order of the element $8$ in the group $(\mathbb{Z}_{12}, +)$ is:",
  r"$3$",
  [(r"$4$", "$4 = \\gcd(8, 12)$, not the order."), (r"$8$", "The order divides $12$."), (r"$12$", "That is the order of the generator $1$; $8$ has a smaller order.")],
  [S("Order of $a$ in $\\mathbb{Z}_n$", math=r"\frac{n}{\gcd(a, n)} = \frac{12}{4} = 3")], "Order = n / gcd(a, n).")
q(GR, "Cyclic and permutation groups", r"The order of the permutation $(1\ 2\ 3)(4\ 5)$ is:",
  r"$6$",
  [(r"$5$", "That is the number of points moved."), (r"$3$", "That is the order of one cycle only."), (r"$2$", "That is the order of the other cycle only.")],
  [S("Order of disjoint cycles", math=r"\operatorname{lcm}(3, 2) = 6")], "Take the lcm of the cycle lengths.")
q(GR, "Subgroups and Lagrange's theorem", r"A group $G$ has order $12$. Which cannot be the order of a subgroup of $G$?",
  r"$5$",
  [(r"$4$", "$4$ divides $12$."), (r"$6$", "$6$ divides $12$."), (r"$3$", "$3$ divides $12$.")],
  [S("Lagrange", text="The order of a subgroup divides $12$. $5$ does not.")], "Which numbers divide 12?")
q(GR, "Subgroups and Lagrange's theorem", r"$H$ is a subgroup of order $6$ in a group of order $24$. The number of left cosets of $H$ is:",
  r"$4$",
  [(r"$6$", "That is the order of $H$."), (r"$18$", "That subtracts instead of dividing."), (r"$144$", "That multiplies instead of dividing.")],
  [S("Index", math=r"[G : H] = \frac{|G|}{|H|} = \frac{24}{6} = 4")], "Divide the orders.")
q(GR, "Group isomorphisms", r"Which group of order $4$ is isomorphic to the cyclic group $\mathbb{Z}_4$?",
  r"$\{1, 2, 3, 4\}$ under multiplication modulo $5$",
  [(r"$\{1, 3, 5, 7\}$ under multiplication modulo $8$", "Every element has order $2$: this is the Klein four-group, not cyclic."), (r"$\mathbb{Z}_2 \times \mathbb{Z}_2$ under addition", "Every non-identity element has order $2$: not cyclic."), (r"The symmetries (rotation by $180^\circ$ and two reflections) of a non-square rectangle", "All non-identity elements have order $2$: Klein four-group.")],
  [S("Find an element of order 4", text="$2$ has powers $2, 4, 3, 1$ modulo $5$: it generates the group.")], "Which group has an element of order 4?")
q(GR, "Group isomorphisms", r"Why are $\mathbb{Z}_6$ and $S_3$ (both of order $6$) not isomorphic?",
  r"$\mathbb{Z}_6$ is abelian but $S_3$ is not",
  [(r"They have different numbers of elements", "Both have $6$ elements."), (r"$S_3$ has no identity element", "Every group has an identity."), (r"$\mathbb{Z}_6$ has no element of order $3$", "$2$ has order $3$ in $\\mathbb{Z}_6$.")],
  [S("An isomorphism preserves commutativity", text="In $S_3$, $(1\\ 2)(1\\ 3) \\neq (1\\ 3)(1\\ 2)$.")], "What structural property can differ?")
# --- Vector Spaces (6)
q(VS, "Subspaces, independence, basis and dimension", r"The dimension of the subspace $\{(x, y, z) : x = 2z\}$ of $\mathbb{R}^3$ is:",
  r"$2$",
  [(r"$1$", "Two parameters ($y$ and $z$) remain free."), (r"$3$", "That is the dimension of the whole space; there is one condition."), (r"$0$", "The subspace contains non-zero vectors.")],
  [S("General vector", math=r"(2z, y, z) = y(0, 1, 0) + z(2, 0, 1)")], "Count the free variables.")
q(VS, "Subspaces, independence, basis and dimension", r"The dimension of the span of $(1, 2, 1)$, $(2, 4, 2)$, $(0, 1, 1)$ is:",
  r"$2$",
  [(r"$3$", "The second vector is twice the first, so the set is dependent."), (r"$1$", "$(0, 1, 1)$ is not a multiple of $(1, 2, 1)$."), (r"$0$", "The span contains non-zero vectors.")],
  [S("Dependent pair", math=r"(2, 4, 2) = 2(1, 2, 1)"), S("Independent pair", text="$(1,2,1)$ and $(0,1,1)$ are independent: dimension $2$.")], "Look for multiples.")
q(VS, "Linear transformations", r"A linear map has $T(1, 1) = (3, 1)$ and $T(1, -1) = (1, -1)$. Its matrix is:",
  r"$" + _m([2, 1], [0, 1]) + "$",
  [(r"$" + _m([3, 1], [1, -1]) + "$", "The given vectors are images of $(1, 1)$ and $(1, -1)$, not of the standard basis vectors."), (r"$" + _m([2, 0], [1, 1]) + "$", "That is the transpose; columns must be the images."), (r"$" + _m([1, 2], [1, 0]) + "$", "The columns are in the wrong order.")],
  [S("Standard basis", math=r"T(\mathbf{e}_1) = \tfrac12[(3,1) + (1,-1)] = (2, 0),\ T(\mathbf{e}_2) = \tfrac12[(3,1) - (1,-1)] = (1, 1)")], "Express e1 and e2 using the two given vectors.")
q(VS, "Linear transformations", r"Which map is linear?",
  r"$T(x, y, z) = (x + y,\ 2z)$",
  [(r"$T(x, y) = (x + 1,\ y)$", "It does not send $\\mathbf{0}$ to $\\mathbf{0}$."), (r"$T(x, y, z) = (xz,\ y)$", "A product of variables is not linear."), (r"$T(x, y) = (x^2,\ y)$", "A square is not linear.")],
  [S("Test", text="Every term is of the first degree with no constant.")], "Which map has only first-degree terms?")
q(VS, "Kernel, range and the rank-nullity theorem", r"The rank of $" + _m([1, 2, 3], [4, 5, 6], [7, 8, 9]) + r"$ is:",
  r"$2$",
  [(r"$3$", "The determinant is $0$ (row 3 $= 2\\times$ row 2 $-$ row 1)."), (r"$1$", "Rows 1 and 2 are not multiples of each other."), (r"$0$", "The matrix is not the zero matrix.")],
  [S("Dependency", math=r"R_3 = 2R_2 - R_1"), S("Independent rows", text="$R_1$ and $R_2$ are independent: rank $2$.")], "Look for a relation between the rows.")
q(VS, "Kernel, range and the rank-nullity theorem", r"A linear map $T : \mathbb{R}^4 \to \mathbb{R}^3$ is onto. The dimension of its kernel is:",
  r"$1$",
  [(r"$0$", "A map from $\\mathbb{R}^4$ to $\\mathbb{R}^3$ cannot be one-to-one."), (r"$2$", "That would give rank $2$, not $3$."), (r"$3$", "That is the rank.")],
  [S("Onto means rank 3", math=r"\text{nullity} = 4 - 3 = 1")], "Onto means the rank equals the dimension of the codomain.")
# --- Numerical Methods (6)
q(NM, "Root finding", r"$f(x) = x^3 - 3x + 1$ has $f(1) = -1$ and $f(2) = 3$. After one step of bisection the root lies in:",
  r"$[1.5,\ 2]$",
  [(r"$[1,\ 1.5]$", r"$f(1.5) = -0.125 < 0$ has the same sign as $f(1)$, so the root is in the upper half."), (r"$[1.5,\ 1.75]$", "That would be the second step."), (r"$[1,\ 2]$", "Bisection halves the interval.")],
  [S("Midpoint", math=r"f(1.5) = 3.375 - 4.5 + 1 = -0.125")], "Find the sign of f(1.5).")
q(NM, "Root finding", r"Newton-Raphson is applied to $f(x) = x^2 - 5$ with $x_0 = 2$. Then $x_1 =$",
  r"$2.25$",
  [(r"$2.5$", "You used $f'(x) = x$ instead of $2x$."), (r"$1.75$", "You added $f/f'$ instead of subtracting."), (r"$2.236$", "That is $\\sqrt5$, the exact root.")],
  [S("Formula", math=r"x_1 = 2 - \frac{4 - 5}{4} = 2.25")], "x1 = x0 - f(x0)/f'(x0) with f' = 2x.")
q(NM, "Numerical integration", r"The trapezium rule with $4$ strips is used for $\displaystyle\int_0^2 x^2\,dx$. The estimate is:",
  r"$2.75$",
  [(r"$2.67$", "That is the Simpson value; the trapezium rule over-estimates a convex curve."), (r"$5.5$", r"You forgot the factor $\frac12$ in $\frac h2$."), (r"$2.2$", "You used $h = 0.4$; with $4$ strips $h = 0.5$.")],
  [S("Ordinates ($h = 0.5$)", math=r"0,\ 0.25,\ 1,\ 2.25,\ 4"), S("Rule", math=r"0.25\left[0 + 4 + 2(3.5)\right] = 2.75")], "h = 0.5 and the weights 1, 2, 2, 2, 1.")
q(NM, "Numerical integration", r"Simpson's rule with $4$ strips for $\displaystyle\int_0^1\frac{dx}{1 + x}$ gives:",
  r"$0.6933$",
  [(r"$0.6970$", "That is the trapezium estimate."), (r"$0.5758$", "The weights are in the wrong order ($1, 2, 4, 2, 1$)."), (r"$0.4647$", r"You used $\frac h3$ with the trapezium weights.")],
  [S("Ordinates", math=r"1,\ 0.8,\ 0.66667,\ 0.57143,\ 0.5"), S("Simpson", math=r"\frac{0.25}{3}\left[1.5 + 4(1.37143) + 2(0.66667)\right] = 0.6933")], "Weights 1, 4, 2, 4, 1 and the factor h/3.")
q(NM, "Numerical solution of differential equations", r"Euler's method with $h = 0.5$ is used for $\dfrac{dy}{dx} = y - x$, $y(0) = 2$. The estimate of $y(1)$ is:",
  r"$4.25$",
  [(r"$3$", "That is $y(0.5)$, after only one step."), (r"$4.5$", "That ignores the $-x$ term."), (r"$3.625$", "You used $x_{n+1}$ instead of $x_n$ in the gradient.")],
  [S("Step 1", math=r"y_1 = 2 + 0.5(2 - 0) = 3"), S("Step 2", math=r"y_2 = 3 + 0.5(3 - 0.5) = 4.25")], "Use the old x and old y in the gradient.")
q(NM, "Numerical solution of differential equations", r"One step of the improved Euler method with $h = 0.2$ for $\dfrac{dy}{dx} = x + y$, $y(0) = 1$ gives $y_1 =$",
  r"$1.24$",
  [(r"$1.2$", "That is the predictor (a plain Euler step)."), (r"$1.28$", "That uses the gradient at the predicted point alone: $1 + 0.2(1.4)$."), (r"$1.4$", "That is the gradient at the predicted point.")],
  [S("Predictor", math=r"y^* = 1 + 0.2(1) = 1.2"), S("Corrector", math=r"y_1 = 1 + 0.1(1 + 1.4) = 1.24")], "Average the two gradients.")
# --- Advanced Mechanics & Probability (12)
q(MP, "Kinematics in polar coordinates", r"A particle moves in a circle of radius $2$ m with constant angular speed $3$ rad/s. Its radial acceleration component is:",
  r"$-18$ m/s$^2$",
  [(r"$+18$ m/s$^2$", "The radial component is negative: the acceleration is towards the centre."), (r"$-6$ m/s$^2$", "That is $r\\omega$, the speed, not the acceleration."), (r"$-36$ m/s$^2$", "You used $r^2\\omega^2$.")],
  [S("Formula", math=r"a_r = -r\dot\theta^2 = -2(9) = -18")], "a_r = r-double-dot - r theta-dot squared.")
q(MP, "Kinematics in polar coordinates", r"A particle moves with $r = e^t$ and $\theta = t$. Its speed at $t = 0$ is:",
  r"$\sqrt2$ m/s",
  [(r"$1$ m/s", "That is only the radial component."), (r"$2$ m/s", "You added the components instead of using Pythagoras."), (r"$\dfrac{1}{\sqrt2}$ m/s", "That is the reciprocal.")],
  [S("Components", math=r"v_r = \dot r = 1,\quad v_\theta = r\dot\theta = 1"), S("Speed", math=r"\sqrt{1 + 1} = \sqrt2")], "Combine the perpendicular components.")
q(MP, "Variable mass systems", r"A rocket ejects fuel at $4$ kg/s with speed $1500$ m/s relative to the rocket. The thrust is:",
  r"$6000$ N",
  [(r"$375$ N", "You divided $u$ by $k$."), (r"$1500$ N", "You used $u$ alone, without the burn rate."), (r"$1496$ N", "You subtracted instead of multiplying.")],
  [S("Thrust", math=r"uk = 1500 \times 4 = 6000")], "Thrust = exhaust speed times burn rate.")
q(MP, "Variable mass systems", r"A rocket in free space (no gravity) has initial mass $m_0$ and final mass $\frac{m_0}{3}$, with exhaust speed $1000$ m/s. Its final speed from rest is:",
  r"$1000\ln3 \approx 1099$ m/s",
  [(r"$2000$ m/s", "That is $u(3 - 1)$, not a logarithm."), (r"$333$ m/s", "You divided $u$ by $3$."), (r"$3000$ m/s", "You multiplied $u$ by the mass ratio.")],
  [S("Rocket equation", math=r"v = u\ln\frac{m_0}{m} = 1000\ln3 = 1099")], "v = u ln(m0/m).")
q(MP, "Oblique collisions", r"A smooth ball hits a smooth wall with velocity components $8$ m/s parallel to the wall and $6$ m/s towards it. $e = 0.5$. Its speed after the impact is:",
  r"$8.54$ m/s",
  [(r"$10$ m/s", "That would be $e = 1$."), (r"$5$ m/s", "You applied $e$ to the whole speed."), (r"$8$ m/s", "You ignored the perpendicular component after the impact.")],
  [S("After", math=r"\text{parallel } 8,\ \text{perpendicular } 0.5 \times 6 = 3"), S("Speed", math=r"\sqrt{64 + 9} = 8.54")], "e multiplies only the perpendicular component.")
q(MP, "Oblique collisions", r"A sphere of mass $m$ moving at $10$ m/s along the line of centres hits an identical stationary sphere with $e = 0.5$. The speed of the second sphere afterwards is:",
  r"$7.5$ m/s",
  [(r"$5$ m/s", "That would be the case $e = 0$, where both move together."), (r"$10$ m/s", "That would be $e = 1$."), (r"$2.5$ m/s", "That is the speed of the first sphere.")],
  [S("Momentum and restitution", math=r"v_1 + v_2 = 10, \quad v_2 - v_1 = 5 \Rightarrow v_2 = 7.5")], "Use momentum and restitution along the line.")
q(MP, "Damped and forced oscillations", r"The general solution of $\ddot x + 2\dot x + x = 0$ is:",
  r"$x = (A + Bt)e^{-t}$",
  [(r"$x = e^{-t}(A\cos t + B\sin t)$", "That needs complex roots; here the root $-1$ is repeated."), (r"$x = Ae^{-t} + Be^{t}$", "There is no root $+1$."), (r"$x = Ae^{-t} + Be^{-2t}$", "The roots are $-1, -1$, not $-1, -2$.")],
  [S("Repeated root", math=r"(\lambda + 1)^2 = 0")], "Solve the auxiliary equation.")
q(MP, "Damped and forced oscillations", r"The steady-state amplitude of $\ddot x + 4x = 6\cos t$ is:",
  r"$2$",
  [(r"$3$", r"You divided by $\omega_0 = 2$ instead of $\omega_0^2 - \Omega^2 = 3$."), (r"$1.5$", r"You divided by $\omega_0^2 = 4$."), (r"$6$", "You took the forcing amplitude as the response.")],
  [S("Try $A\\cos t$", math=r"-A + 4A = 6 \Rightarrow A = 2")], "Substitute x = A cos t into the equation.")
q(MP, "Moment of inertia of rigid bodies", r"A uniform ring of mass $2$ kg and radius $0.5$ m has moment of inertia about a diameter of:",
  r"$0.25$ kg m$^2$",
  [(r"$0.5$ kg m$^2$", "That is the value about the perpendicular axis through the centre, $Ma^2$."), (r"$0.125$ kg m$^2$", r"That is $\frac14Ma^2$, the value for a disc."), (r"$0.75$ kg m$^2$", "That is the value about a tangent in the plane, $\\frac32Ma^2$.")],
  [S("Perpendicular axes", math=r"2I_d = Ma^2 \Rightarrow I_d = \tfrac12(2)(0.25) = 0.25")], "Use the perpendicular axes theorem for the ring.")
q(MP, "Rotation about a fixed axis", r"A wheel with $I = 4$ kg m$^2$ is acted on by a constant torque of $10$ N m from rest. Its angular speed after $3$ s is:",
  r"$7.5$ rad/s",
  [(r"$2.5$ rad/s", "That is the angular acceleration, not the speed after $3$ s."), (r"$30$ rad/s", "You multiplied torque by time, ignoring $I$."), (r"$12$ rad/s", "You multiplied $I$ by time.")],
  [S("Angular acceleration", math=r"\alpha = \frac{10}{4} = 2.5"), S("Speed", math=r"\omega = 2.5 \times 3 = 7.5")], "Find alpha first.")
q(MP, "Probability generating functions", r"A random variable has pgf $G(t) = (0.3 + 0.7t)^5$. Its mean is:",
  r"$3.5$",
  [(r"$1.5$", "That is $np$ with $p = 0.3$; the probability of success goes with $t$, so $p = 0.7$."), (r"$1.05$", "That is the variance $npq$."), (r"$0.7$", "That is $p$, not the mean.")],
  [S("Binomial", math=r"G'(1) = 5(0.7)(1)^4 = 3.5")], "This is the pgf of B(5, 0.7).")
q(MP, "Probability generating functions", r"$X$ has pgf $G(t) = \dfrac{t}{2 - t}$. Then $E(X)$ is:",
  r"$2$",
  [(r"$1$", "That is $G(1)$."), (r"$\dfrac12$", "That is $p$; the mean is $1/p$."), (r"$4$", "That is $1/p^2$ with $p = \\frac12$. The variance would be $q/p^2 = 2$, and the mean is $1/p$.")],
  [S("Differentiate", math=r"G'(t) = \frac{(2 - t) + t}{(2 - t)^2} = \frac{2}{(2 - t)^2}"), S("At $t = 1$", math=r"G'(1) = 2")], "Differentiate with the quotient rule.")

assert len(P1) == 50, len(P1)
SETS.append(practice_set(module="Examination", topic="Paper 1", title="Paper 1 mock A",
                         lesson="fmxu-exam-paper-1-multiple-choice-strategy", mock=True, time_limit_minutes=90, questions=P1))

# ================================================================ Paper 2 practice paper A
_slots.clear()
P2 = []


def p2m(prompt, right, wrongs, steps, concept, skill, hint):
    P2.append(mc(prompt, right, wrongs, steps, concept, skill, hint))


def p2n(prompt, answer, steps, concept, skill, hint, tolerance=0, unit=""):
    P2.append(NUM(prompt, answer, steps=steps, tolerance=tolerance, unit=unit, concept=concept, skill=skill, hint=hint))


Q1 = r"$f(x) = e^x\sin x$. "
p2n("Question 1(a). " + Q1 + r"Find the coefficient of $x^3$ in the Maclaurin series of $f(x)$ (as a decimal to 3 places).", 0.333, [S("Multiply the series", math=r"\left(1 + x + \tfrac{x^2}{2}\right)\left(x - \tfrac{x^3}{6}\right): \ x^3: \tfrac12 - \tfrac16 = \tfrac13")],
    "Taylor series and L'Hopital's rule", "Calculation", "Multiply the series of e^x and sin x and collect the x^3 terms.", tolerance=0.001)
p2n("Question 1(b). " + Q1 + r"Use the series to find $\displaystyle\lim_{x \to 0}\frac{e^x\sin x - x}{x^2}$.", 1, [S("Series", math=r"\frac{x^2 + \tfrac13x^3 + \cdots}{x^2} \to 1")],
    "Taylor series and L'Hopital's rule", "Application", "Divide the series of f(x) - x by x^2.")
p2n(r"Question 1(c). Let $I_n = \displaystyle\int_0^1 x^ne^x\,dx$ with $I_n = e - nI_{n-1}$ and $I_1 = 1$. Find $I_3$ to 3 decimal places.", 0.563, [S("$I_2$", math=r"e - 2"), S("$I_3$", math=r"e - 3(e - 2) = 6 - 2e = 0.563")],
    "Reduction formulae", "Calculation", "Use the formula twice: first I_2.", tolerance=0.001)
p2n(r"Question 1(d). Find the length of the curve $y = x^{3/2}$ from $x = 0$ to $x = 4$, to 2 decimal places.", 9.07, [S("Integral", math=r"\int_0^4\sqrt{1 + \tfrac94x}\,dx = \tfrac{8}{27}(10\sqrt{10} - 1) = 9.07")],
    "Arc length and surface area of revolution", "Calculation", "Arc length = integral of sqrt(1 + (dy/dx)^2).", tolerance=0.01)
Q2 = r"$\dfrac{dy}{dx} + 2y = e^{-x}$ with $y(0) = 0$. "
p2m("Question 2(a). " + Q2 + "An integrating factor is:", r"$e^{2x}$",
    [(r"$e^{-2x}$", "The integrating factor is $e^{\\int P\\,dx}$ with $P = 2$, giving $e^{+2x}$."), (r"$2e^{x}$", "The exponent is the integral of $2$, which is $2x$."), (r"$e^{x}$", "That uses $\\int 1\\,dx$; here $P = 2$.")],
    [S("Integrating factor", math=r"e^{\int 2\,dx} = e^{2x}")], "First-order separable and linear equations", "Recall", "e to the power of the integral of the coefficient of y.")
p2n("Question 2(b). " + Q2 + r"Find $y(1)$ to 4 decimal places.", 0.2325, [S("Multiply", math=r"(ye^{2x})' = e^x \Rightarrow y = e^{-x} + Ce^{-2x}"), S("Condition", math=r"C = -1 \Rightarrow y(1) = e^{-1} - e^{-2} = 0.2325")],
    "First-order separable and linear equations", "Calculation", "Integrate (y e^(2x))' = e^x and use y(0) = 0.", tolerance=0.0005)
p2n(r"Question 2(c). The Bernoulli equation $\dfrac{dy}{dx} + y = y^2$ has $y(0) = \tfrac12$. Find $y(1)$ to 3 decimal places.", 0.269, [S("Substitute $v = 1/y$", math=r"v' - v = -1 \Rightarrow v = 1 + Ce^x,\ C = 1"), S("Evaluate", math=r"y(1) = \frac{1}{1 + e} = 0.269")],
    "Bernoulli equations", "Calculation", "Let v = 1/y and solve the linear equation for v.", tolerance=0.001)
p2n(r"Question 2(d). Solve $y'' - 3y' + 2y = 0$ with $y(0) = 0$ and $y'(0) = 1$. Find $y(1)$ to 2 decimal places.", 4.67, [S("Roots", math=r"\lambda = 1, 2 \Rightarrow y = e^{2x} - e^{x}"), S("Evaluate", math=r"y(1) = e^2 - e = 4.67")],
    "Second-order linear equations", "Calculation", "Solve the auxiliary equation; use both conditions.", tolerance=0.01)
Q3 = r"$(\mathbb{Z}_{12}, +)$ is the group of integers modulo $12$ under addition. "
p2n("Question 3(a). " + Q3 + "Find the order of the element $8$.", 3, [S("Order", math=r"\frac{12}{\gcd(8, 12)} = 3")], "Cyclic and permutation groups", "Calculation", "Order = n / gcd(a, n).")
p2n("Question 3(b). " + Q3 + "How many elements of the group have order $12$ (generators)?", 4, [S("Generators", text="Those $a$ with $\\gcd(a, 12) = 1$: $1, 5, 7, 11$.")], "Cyclic and permutation groups", "Calculation", "Which elements are coprime to 12?")
p2m("Question 3(c). " + Q3 + "Which could be the order of a subgroup of this group?", r"$6$",
    [(r"$5$", "Subgroup orders divide $12$, and $5$ does not."), (r"$8$", "$8$ does not divide $12$."), (r"$9$", "$9$ does not divide $12$.")],
    [S("Lagrange", text="Divisors of $12$: $1, 2, 3, 4, 6, 12$.")], "Subgroups and Lagrange's theorem", "Concept", "Which numbers divide 12?")
Q4 = r"$T : \mathbb{R}^4 \to \mathbb{R}^3$ has matrix $A = " + _m([1, 2, 0, 1], [2, 4, 1, 5], [3, 6, 1, 6]) + r"$. "
p2n("Question 4(a). " + Q4 + "Find the rank of $T$.", 2, [S("Reduce", math=r"\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}"), S("Count leading 1s", text="The rank is $2$.")], "Kernel, range and the rank-nullity theorem", "Calculation", "Row reduce and count the leading 1s.")
p2n("Question 4(b). " + Q4 + "Find the nullity of $T$.", 2, [S("Rank-nullity", math=r"4 - 2 = 2")], "Kernel, range and the rank-nullity theorem", "Calculation", "Rank plus nullity equals the number of columns.")
p2m("Question 4(c). " + Q4 + "Which vector is in the kernel of $T$?", r"$(-2, 1, 0, 0)$",
    [(r"$(1, 2, 0, 0)$", r"$A(1, 2, 0, 0)^T = (5, 10, 15)^T \neq \mathbf{0}$."), (r"$(1, 0, 3, 1)$", r"The first row gives $1 + 0 + 0 + 1 = 2 \neq 0$."), (r"$(0, 0, 1, 1)$", r"The first row gives $0 + 0 + 0 + 1 = 1 \neq 0$.")],
    [S("Check", math=r"A" + _v(-2, 1, 0, 0) + " = " + _v(0, 0, 0))], "Kernel, range and the rank-nullity theorem", "Application", "Multiply each candidate by A and test for zero.")
Q5 = r"$f(x) = x^3 - 2x - 5$. "
p2n("Question 5(a). " + Q5 + r"One Newton-Raphson step from $x_0 = 2$ gives $x_1$. Find $x_1$.", 2.1, [S("Values", math=r"f(2) = -1, \ f'(2) = 10"), S("Step", math=r"x_1 = 2 + 0.1 = 2.1")], "Root finding", "Calculation", "x1 = x0 - f(x0)/f'(x0).", tolerance=0.0005)
p2n("Question 5(b). " + Q5 + r"Find $x_2$ to 4 decimal places.", 2.0946, [S("Step", math=r"f(2.1) = 0.061,\ f'(2.1) = 11.23 \Rightarrow x_2 = 2.1 - 0.00543 = 2.0946")], "Root finding", "Calculation", "Use the value 2.1 from part (a).", tolerance=0.0002)
p2n(r"Question 5(c). Use Simpson's rule with $4$ strips to estimate $\displaystyle\int_0^1\frac{4}{1 + x^2}\,dx$ to 4 decimal places.", 3.1416, [S("Ordinates", math=r"4, 3.76471, 3.2, 2.56, 2"), S("Simpson", math=r"\tfrac{0.25}{3}(37.69882) = 3.1416")], "Numerical integration", "Calculation", "h = 0.25; weights 1, 4, 2, 4, 1.", tolerance=0.0005)
p2n(r"Question 5(d). Euler's method with $h = 0.1$ is applied to $\dfrac{dy}{dx} = x + y$, $y(0) = 1$. Find the estimate of $y(0.3)$.", 1.362, [S("Steps", math=r"y_1 = 1.1,\ y_2 = 1.22,\ y_3 = 1.22 + 0.1(0.2 + 1.22) = 1.362")], "Numerical solution of differential equations", "Calculation", "Update x and y at each step.", tolerance=0.001)
Q6 = r"A rocket of mass $500$ kg at lift-off ejects fuel at $5$ kg/s with speed $2000$ m/s relative to the rocket ($g = 10$ m/s$^2$). "
p2n("Question 6(a). " + Q6 + "Find the thrust in N.", 10000, [S("Thrust", math=r"uk = 2000 \times 5 = 10\,000")], "Variable mass systems", "Calculation", "Thrust = u k.", unit="N")
p2n("Question 6(b). " + Q6 + "Find the speed after $60$ s in m/s.", 1232.6, [S("Rocket equation", math=r"v = 2000\ln\frac{500}{200} - 10(60) = 1232.6")], "Variable mass systems", "Calculation", "The mass after 60 s is 500 - 5(60).", tolerance=1, unit="m/s")
p2n(r"Question 6(c). A smooth ball hits a smooth wall at $12$ m/s making $30^\circ$ with the wall; $e = 0.6$. Find the speed after the impact in m/s to 3 significant figures.", 11.0, [S("Components", math=r"10.392 \text{ and } 0.6(6) = 3.6"), S("Speed", math=r"\sqrt{120.96} = 11.0")], "Oblique collisions", "Calculation", "Parallel unchanged; perpendicular times e.", tolerance=0.05, unit="m/s")
p2n(r"Question 6(d). A particle moves with $r = 3 + 2t$ and $\theta = t^2$. Find the transverse acceleration $a_\theta$ at $t = 1$.", 18, [S("Formula", math=r"r\ddot\theta + 2\dot r\dot\theta = 5(2) + 2(2)(2) = 18")], "Kinematics in polar coordinates", "Calculation", "Find r, r-dot, theta-dot and theta-double-dot at t = 1.", unit="m/s^2")
p2n(r"Question 7(a). A uniform rod of mass $3$ kg and length $1.2$ m. Find its moment of inertia about a perpendicular axis through one end in kg m$^2$.", 1.44, [S("Standard result", math=r"\tfrac13(3)(1.2)^2 = 1.44")], "Moment of inertia of rigid bodies", "Calculation", "Use ML^2/3.", tolerance=0.01, unit="kg m^2")
p2n(r"Question 7(b). The same rod swings freely about a horizontal axis through one end. Find the period of small oscillations in seconds ($g = 10$ m/s$^2$).", 1.78, [S("Period", math=r"T = 2\pi\sqrt{\frac{2L}{3g}} = 2\pi\sqrt{0.08} = 1.78")], "Rotation about a fixed axis", "Application", "Equate I times theta-double-dot to the torque of the weight and use sin theta ~ theta.", tolerance=0.02, unit="s")
p2n(r"Question 7(c). The damped oscillation $\ddot x + 4\dot x + 13x = 0$ has period $\frac{2\pi}{3}$ s. Find the ratio of successive maximum displacements.", 65.9, [S("Ratio", math=r"e^{kT} = e^{2 \cdot 2\pi/3} = 65.9")], "Damped and forced oscillations", "Application", "The amplitude decays by e^(-kT) each period; here k = 2.", tolerance=0.3)
p2n(r"Question 7(d). $X$ has $P(X = 0) = 0.1$, $P(X = 1) = 0.3$, $P(X = 2) = 0.4$, $P(X = 3) = 0.2$. Find $\operatorname{Var}(X)$ using the generating function.", 0.81, [S("Derivatives at 1", math=r"G'(1) = 1.7,\ G''(1) = 2.0"), S("Variance", math=r"2.0 + 1.7 - 1.7^2 = 0.81")], "Probability generating functions", "Calculation", "Var = G''(1) + G'(1) - G'(1)^2.", tolerance=0.001)

SETS.append(practice_set(module="Examination", topic="Paper 2", title="Paper 2 practice paper A",
                         lesson="fmxu-exam-paper-2-structured-questions", mock=True, time_limit_minutes=150, questions=P2))

