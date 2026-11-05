"""Core pure mathematics (A Level): practice sets for the 3D Vectors lessons, the Examination lessons and two mock papers.

KKEVO draft content. Mock paper timings are KKEVO practice settings, not official examination times.
Paper 1 mock A: 40 four-option multiple-choice questions across all Core Pure topics (concept = topic title).
Paper 2 practice paper A: auto-markable parts (multiple choice and numeric) in numbered questions of mixed topics.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-mechanics", "lower-sixth"),
          ("pure-mathematics-with-statistics", "lower-sixth")]

MOD = "3D Vectors"
TOP = "Vectors in space"


def _v(*c):
    """Column vector in LaTeX (no dollar signs)."""
    return r"\begin{pmatrix} " + r" \\ ".join(str(x) for x in c) + r" \end{pmatrix}"

# ---------------------------------------------------------------- Set 1: vectors in three dimensions
VEC_1 = [
    MC(r"Find the magnitude of the vector $4\mathbf{i} - 4\mathbf{j} + 2\mathbf{k}$.", [
        C("$6$", correct=True),
        C("$36$", why=r"This is $a^2 + b^2 + c^2$. The magnitude needs the square root: $\sqrt{36} = 6$."),
        C("$10$", why="You added the sizes of the components. The magnitude uses squares and a square root."),
        C("$2$", why=r"You added the components with their signs: $4 - 4 + 2$. Square them first."),
    ], steps=[S("Square and add", math=r"16 + 16 + 4 = 36"), S("Square root", math=r"\sqrt{36} = 6")],
       concept="Magnitude of a 3D vector", skill="Calculation", hint="Square each component, add, then take the square root.",
       feedback="The magnitude is the square root of the sum of the squares of the components."),
    MC(r"$A$ is $(2, -1, 5)$ and $B$ is $(-1, 3, 4)$. Find $\overrightarrow{AB}$.", [
        C(r"$" + _v(3, -4, 1) + "$", why=r"This is $\overrightarrow{BA}$. Use end minus start: $B - A$."),
        C(r"$" + _v(-3, 4, -1) + "$", correct=True),
        C(r"$" + _v(1, 2, 9) + "$", why="You added the coordinates. A displacement needs a subtraction."),
        C(r"$" + _v(-3, 4, 1) + "$", why=r"The $z$ component is $4 - 5 = -1$, not $+1$."),
    ], steps=[S("End minus start", math=r"\overrightarrow{AB} = " + _v(-1, 3, 4) + " - " + _v(2, -1, 5)), S("Subtract", math=r"= " + _v(-3, 4, -1))],
       concept="Vector between two points", skill="Calculation", hint="Subtract the coordinates of the start point A from those of B.",
       feedback="AB = b - a: end minus start."),
    NUM(r"$A$ is $(1, 2, 3)$ and $B$ is $(5, 4, 7)$. Find the distance $AB$.", 6,
        steps=[S("Find the vector", math=r"\overrightarrow{AB} = (4, 2, 4)"), S("Its magnitude", math=r"\sqrt{16 + 4 + 16} = \sqrt{36} = 6")],
        concept="Distance between two points", skill="Calculation", hint="Find AB first, then its magnitude.",
        feedback="Distance is the magnitude of the displacement vector."),
    MC(r"Find the midpoint of $A(2, -4, 6)$ and $B(8, 2, -2)$.", [
        C("$(10, -2, 4)$", why="This is the sum of the coordinates. Divide by 2 to get the midpoint."),
        C("$(6, 6, -8)$", why="You subtracted. The midpoint is the **average** of the coordinates."),
        C("$(5, -1, 2)$", correct=True),
        C("$(3, 3, -4)$", why="This is half of $\\overrightarrow{AB}$, not the midpoint. Add it to $A$."),
    ], steps=[S("Average each coordinate", math=r"\left(\tfrac{2 + 8}{2},\ \tfrac{-4 + 2}{2},\ \tfrac{6 - 2}{2}\right)"), S("Evaluate", math=r"(5, -1, 2)")],
       concept="Midpoint", skill="Calculation", hint="Add the coordinates of A and B and halve.",
       feedback="The midpoint is half the sum of the position vectors."),
    MC(r"Which is a unit vector in the direction of $2\mathbf{i} + 3\mathbf{j} + 6\mathbf{k}$?", [
        C(r"$\frac{1}{49}(2, 3, 6)$", why=r"You divided by $|\mathbf{v}|^2 = 49$. Divide by the magnitude, $7$."),
        C(r"$\frac{1}{11}(2, 3, 6)$", why="$11$ is the sum of the components, not the magnitude."),
        C(r"$\frac{1}{\sqrt{7}}(2, 3, 6)$", why=r"The magnitude is $\sqrt{49} = 7$, not $\sqrt{7}$."),
        C(r"$\frac{1}{7}(2, 3, 6)$", correct=True),
    ], steps=[S("Magnitude", math=r"\sqrt{4 + 9 + 36} = 7"), S("Divide", math=r"\hat{\mathbf{v}} = \tfrac{1}{7}(2, 3, 6)")],
       concept="Unit vectors", skill="Calculation", hint="Find the magnitude of the vector first.",
       feedback="A unit vector is v divided by |v|."),
    MC(r"$A(0, 3, -1)$ and $B(6, 0, 8)$. The point $P$ lies on $AB$ with $AP : PB = 1 : 2$. Find $P$.", [
        C("$(2, 2, 2)$", correct=True),
        C("$(4, 1, 5)$", why=r"This is the point with $AP : PB = 2 : 1$. Here $P$ is closer to $A$."),
        C(r"$\left(3, \tfrac{3}{2}, \tfrac{7}{2}\right)$", why="This is the midpoint, which has ratio $1 : 1$."),
        C("$(6, -3, 9)$", why=r"This is $\overrightarrow{AB}$ itself, not a point."),
    ], steps=[S("$P$ is one third of the way from $A$", math=r"\mathbf{p} = (0, 3, -1) + \tfrac{1}{3}(6, -3, 9)"), S("Calculate", math=r"= (2, 2, 2)")],
       concept="Dividing a line in a ratio", skill="Application", hint="What fraction of the way from A to B is a 1 : 2 division?",
       feedback="For AP : PB = m : n, P is m/(m+n) of the way from A to B."),
    NUM(r"$A(1, 2, 3)$, $B(3, 5, 7)$ and $C(5, k, 11)$ are collinear. Find $k$.", 8,
        steps=[S("Compare vectors", math=r"\overrightarrow{AB} = (2, 3, 4), \qquad \overrightarrow{AC} = (4, k - 2, 8)"),
               S("$\\overrightarrow{AC} = 2\\overrightarrow{AB}$", math=r"k - 2 = 6 \;\Rightarrow\; k = 8")],
        concept="Collinear points", skill="Reasoning", hint="For collinear points, AC must be a multiple of AB. What is the multiple?",
        feedback="Compare two components to find the multiple, then use it for the unknown."),
    MC(r"$ABCD$ is a parallelogram with $A(1, 0, 2)$, $B(4, 1, 0)$ and $C(6, 5, 1)$. Find $D$.", [
        C("$(9, 6, -1)$", why=r"This is $B + C - A$, the fourth vertex of a different parallelogram."),
        C("$(3, 4, 3)$", correct=True),
        C("$(-1, -4, 1)$", why=r"This is $A + B - C$. In $ABCD$ the diagonal $AC$ is opposite to $BD$."),
        C("$(11, 6, 3)$", why=r"This is $A + B + C$. Only $A + C - B$ gives $D$."),
    ], steps=[S("In a parallelogram $\\overrightarrow{AD} = \\overrightarrow{BC}$", math=r"\mathbf{d} = \mathbf{a} + \mathbf{c} - \mathbf{b}"), S("Calculate", math=r"(1 + 6 - 4,\ 0 + 5 - 1,\ 2 + 1 - 0) = (3, 4, 3)")],
       concept="Parallelogram vectors", skill="Reasoning", hint="In a parallelogram ABCD, AD is equal to BC.",
       feedback="Opposite sides of a parallelogram are equal vectors."),
]

# ---------------------------------------------------------------- Set 2: scalar product and angles
VEC_2 = [
    MC(r"Calculate $(\mathbf{i} + 2\mathbf{j} - 3\mathbf{k})\cdot(4\mathbf{i} - \mathbf{j} + 2\mathbf{k})$.", [
        C("$8$", why=r"The $z$ term is $(-3)(2) = -6$, not $+6$."),
        C("$0$", why=r"The $y$ term is $(2)(-1) = -2$, not $+2$."),
        C("$-4$", correct=True),
        C("$12$", why="You ignored the signs of the terms. Add them with their signs: $4 - 2 - 6$."),
    ], steps=[S("Multiply matching components", math=r"(1)(4) + (2)(-1) + (-3)(2)"), S("Add", math=r"4 - 2 - 6 = -4")],
       concept="Calculating a scalar product", skill="Calculation", hint="Multiply the i, j and k components in pairs, then add.",
       feedback="a.b = a1 b1 + a2 b2 + a3 b3: watch every sign."),
    MC(r"For two non-zero vectors, $\mathbf{a}\cdot\mathbf{b} = 7$. What does this tell you about the angle between them?", [
        C("It is a right angle", why=r"A right angle gives $\mathbf{a}\cdot\mathbf{b} = 0$."),
        C("It is obtuse", why=r"An obtuse angle has a negative cosine and so a negative scalar product."),
        C(r"It is $0^\circ$", why=r"$0^\circ$ would need $\mathbf{a}\cdot\mathbf{b} = |\mathbf{a}||\mathbf{b}|$. We do not know that."),
        C("It is acute", correct=True),
    ], steps=[S("Use the formula", math=r"\cos\theta = \frac{\mathbf{a}\cdot\mathbf{b}}{|\mathbf{a}||\mathbf{b}|} > 0"), S("Conclude", text=r"$\cos\theta > 0$ means $0^\circ \leq \theta < 90^\circ$, and it is acute.")],
       concept="Sign of the scalar product", skill="Concept", hint="Magnitudes are positive, so the sign of cos θ is the sign of a.b.",
       feedback="Positive: acute. Zero: right angle. Negative: obtuse."),
    NUM(r"Find $k$ so that $k\mathbf{i} + 3\mathbf{j} - 2\mathbf{k}$ is perpendicular to $2\mathbf{i} + k\mathbf{j} + \mathbf{k}$.", 0.4, tolerance=0.001,
        steps=[S("Scalar product equals 0", math=r"2k + 3k - 2 = 0"), S("Solve", math=r"5k = 2 \;\Rightarrow\; k = 0.4")],
        concept="Perpendicular vectors", skill="Calculation", hint="Write the scalar product and set it equal to 0.",
        feedback="Perpendicular vectors have a zero scalar product."),
    MC(r"Find the angle between $\mathbf{a} = (1, 2, 2)$ and $\mathbf{b} = (2, 3, 6)$ (degrees mode).", [
        C(r"$17.8^\circ$", correct=True),
        C(r"$72.2^\circ$", why=r"This is $90^\circ - 17.8^\circ$: it comes from using $\sin$ instead of $\cos$."),
        C(r"$20^\circ$", why=r"$20$ is the scalar product, not the angle. Divide by $|\mathbf{a}||\mathbf{b}| = 21$ and take $\cos^{-1}$."),
        C(r"$0.310^\circ$", why=r"$0.310$ is the angle in **radians**. The calculator was in radian mode."),
    ], steps=[S("Scalar product", math=r"\mathbf{a}\cdot\mathbf{b} = 2 + 6 + 12 = 20"), S("Magnitudes", math=r"|\mathbf{a}| = 3, \quad |\mathbf{b}| = 7"), S("Angle", math=r"\cos\theta = \frac{20}{21} \;\Rightarrow\; \theta = 17.8^\circ")],
       concept="Angle between vectors", skill="Calculation", hint="Use cos θ = a.b divided by the product of the magnitudes.",
       feedback="cos θ = a.b / (|a||b|), then use the inverse cosine."),
    MC(r"$|\mathbf{a}| = 3$, $|\mathbf{b}| = 4$ and the angle between $\mathbf{a}$ and $\mathbf{b}$ is $60^\circ$. Find $|\mathbf{a} + \mathbf{b}|$.", [
        C(r"$\sqrt{13}$", why=r"This is $|\mathbf{a} - \mathbf{b}|$. The sign of $2\mathbf{a}\cdot\mathbf{b}$ must be $+$ for a sum."),
        C(r"$\sqrt{37}$", correct=True),
        C("$7$", why="You added the magnitudes. That is only true when the vectors point the same way."),
        C("$5$", why=r"This ignores the angle: $\sqrt{9 + 16}$ is true only when the vectors are perpendicular."),
    ], steps=[S("Expand", math=r"|\mathbf{a} + \mathbf{b}|^2 = |\mathbf{a}|^2 + 2\,\mathbf{a}\cdot\mathbf{b} + |\mathbf{b}|^2"),
              S("Scalar product", math=r"\mathbf{a}\cdot\mathbf{b} = 3 \times 4 \times \cos 60^\circ = 6"), S("Add", math=r"9 + 12 + 16 = 37, \qquad |\mathbf{a} + \mathbf{b}| = \sqrt{37}")],
       concept="Scalar product algebra", skill="Reasoning", hint="Start from |a+b|² = (a+b).(a+b) and expand.",
       feedback="Expanding (a+b).(a+b) brings in the angle through a.b."),
    NUM(r"$A(2, 0, 1)$, $B(1, 2, 3)$ and $C(4, 1, 5)$. Find angle $ABC$ in degrees, to 1 decimal place.", 84.9, tolerance=0.1, unit="degrees",
        steps=[S("Vectors from $B$", math=r"\overrightarrow{BA} = (1, -2, -2), \qquad \overrightarrow{BC} = (3, -1, 2)"),
               S("Scalar product and magnitudes", math=r"\overrightarrow{BA}\cdot\overrightarrow{BC} = 3 + 2 - 4 = 1, \quad |\overrightarrow{BA}| = 3, \quad |\overrightarrow{BC}| = \sqrt{14}"),
               S("Angle", math=r"\cos(ABC) = \frac{1}{3\sqrt{14}} \;\Rightarrow\; ABC = 84.9^\circ")],
        concept="Angle in a triangle", skill="Application", hint="Both vectors must start at B.",
        feedback="For the angle at B use BA and BC."),
    MC(r"What is the scalar projection of $\mathbf{a} = (5, 2, -1)$ on $\mathbf{b} = (1, 2, 2)$?", [
        C("$7$", why=r"This is $\mathbf{a}\cdot\mathbf{b}$. Divide by $|\mathbf{b}| = 3$."),
        C(r"$\frac{7}{9}$", why=r"You divided by $|\mathbf{b}|^2$. That formula gives the vector projection's multiplier, not the scalar projection."),
        C(r"$\frac{7}{3}$", correct=True),
        C(r"$\frac{7}{\sqrt{30}}$", why=r"You divided by $|\mathbf{a}|$. The projection **on b** divides by $|\mathbf{b}|$."),
    ], steps=[S("Scalar product", math=r"\mathbf{a}\cdot\mathbf{b} = 5 + 4 - 2 = 7"), S("Divide by $|\\mathbf{b}| = 3$", math=r"\frac{7}{3}")],
       concept="Scalar projection", skill="Calculation", hint="The scalar projection of a on b is a.b divided by |b|.",
       feedback="Projection on b: a.b / |b|."),
    MC(r"For non-zero vectors $\mathbf{a}$ and $\mathbf{b}$, $\mathbf{a} + \mathbf{b}$ is perpendicular to $\mathbf{a} - \mathbf{b}$ exactly when:", [
        C(r"$\mathbf{a}$ is perpendicular to $\mathbf{b}$", why=r"That gives $|\mathbf{a} + \mathbf{b}| = |\mathbf{a} - \mathbf{b}|$: the diagonals are equal, not perpendicular."),
        C(r"$\mathbf{a}$ is parallel to $\mathbf{b}$", why=r"Then $\mathbf{a} + \mathbf{b}$ and $\mathbf{a} - \mathbf{b}$ are also parallel to them, not perpendicular."),
        C(r"$\mathbf{a} = \mathbf{b}$", why=r"This is a special case only (and $\mathbf{a} - \mathbf{b}$ would be the zero vector). The condition is more general."),
        C(r"$|\mathbf{a}| = |\mathbf{b}|$", correct=True),
    ], steps=[S("Expand the scalar product", math=r"(\mathbf{a} + \mathbf{b})\cdot(\mathbf{a} - \mathbf{b}) = |\mathbf{a}|^2 - |\mathbf{b}|^2"), S("Set it equal to 0", math=r"|\mathbf{a}| = |\mathbf{b}|", text="The diagonals of a rhombus are perpendicular.")],
       concept="Scalar product reasoning", skill="Reasoning", hint="Expand (a + b).(a - b) like a difference of two squares.",
       feedback="The scalar product behaves like ordinary algebra: (a+b).(a-b) = |a|² - |b|²."),
]

# ---------------------------------------------------------------- Set 3: vector equations of lines
VEC_3 = [
    MC(r"A line has equation $\mathbf{r} = (1, 2, 3) + \lambda(4, -1, 2)$. Which is a direction vector of the line?", [
        C("$(1, 2, 3)$", why="This is the position vector of a point on the line, not the direction."),
        C("$(4, -1, 2)$", correct=True),
        C("$(5, 1, 5)$", why="This is the sum of the point and the direction. It is not the direction."),
        C("$(3, 3, 1)$", why=r"This is not related to the line: check which vector is multiplied by $\lambda$."),
    ], steps=[S("Read the equation", text=r"The vector multiplied by $\lambda$ is the direction vector."), S("Answer", math=r"(4, -1, 2)")],
       concept="Direction vector", skill="Recall", hint="Which vector is multiplied by the parameter?",
       feedback="r = a + λd: a is a point, d is the direction."),
    MC(r"Which is a vector equation of the line through $A(1, 0, 2)$ and $B(3, 4, -2)$?", [
        C(r"$\mathbf{r} = (1, 0, 2) + \lambda(2, 4, -4)$", correct=True),
        C(r"$\mathbf{r} = (1, 0, 2) + \lambda(3, 4, -2)$", why=r"You used the position vector of $B$ as the direction. Use $\overrightarrow{AB} = B - A$."),
        C(r"$\mathbf{r} = (1, 0, 2) + \lambda(4, 4, 0)$", why="You added the coordinates of A and B. The direction is a difference."),
        C(r"$\mathbf{r} = (2, 4, -4) + \lambda(1, 0, 2)$", why="You swapped the point and the direction."),
    ], steps=[S("Direction", math=r"\overrightarrow{AB} = (3 - 1,\ 4 - 0,\ -2 - 2) = (2, 4, -4)"), S("Use $A$ as the point", math=r"\mathbf{r} = (1, 0, 2) + \lambda(2, 4, -4)")],
       concept="Line through two points", skill="Calculation", hint="Find the vector AB first.",
       feedback="Point plus a multiple of AB."),
    NUM(r"A line is $\mathbf{r} = (2, -1, 3) + \lambda(1, 2, -2)$. Find the $z$ coordinate of the point on the line with $x = 5$.", -3,
        steps=[S("Find $\\lambda$ from $x$", math=r"2 + \lambda = 5 \;\Rightarrow\; \lambda = 3"), S("Find $z$", math=r"z = 3 - 2(3) = -3")],
        concept="Points on a line", skill="Calculation", hint="Use the x component to find lambda first.",
        feedback="Find the parameter from the known coordinate, then substitute."),
    MC(r"Write $\mathbf{r} = (1, -2, 3) + \lambda(2, 5, -1)$ in cartesian form.", [
        C(r"$\dfrac{x + 1}{2} = \dfrac{y - 2}{5} = \dfrac{z + 3}{-1}$", why="You changed the signs of the point. The numerators are $x - 1$, $y + 2$, $z - 3$."),
        C(r"$\dfrac{x - 1}{2} = \dfrac{y + 2}{5} = \dfrac{z - 3}{1}$", why="The $z$ denominator is $-1$, the sign of the direction component."),
        C(r"$\dfrac{x - 1}{2} = \dfrac{y + 2}{5} = \dfrac{z - 3}{-1}$", correct=True),
        C(r"$2(x - 1) = 5(y + 2) = -(z - 3)$", why="This puts the direction components on the wrong side. They belong in the denominators."),
    ], steps=[S("Eliminate $\\lambda$", math=r"\lambda = \frac{x - 1}{2} = \frac{y + 2}{5} = \frac{z - 3}{-1}")],
       concept="Cartesian form of a line", skill="Calculation", hint="Solve each coordinate equation for lambda.",
       feedback="(x - a1)/d1 = (y - a2)/d2 = (z - a3)/d3."),
    MC(r"Which point lies on the line $\mathbf{r} = (1, -2, 3) + \lambda(2, 5, -1)$?", [
        C("$(3, 3, 4)$", why=r"$\lambda = 1$ gives $(3, 3, 2)$, so $z = 4$ fails."),
        C("$(5, 8, 2)$", why=r"$\lambda = 2$ gives $(5, 8, 1)$, so $z = 2$ fails."),
        C("$(-1, -7, 5)$", why=r"$\lambda = -1$ gives $(-1, -7, 4)$, so $z = 5$ fails."),
        C("$(7, 13, 0)$", correct=True),
    ], steps=[S("Find $\\lambda$ from $x$ in the correct option", math=r"1 + 2\lambda = 7 \;\Rightarrow\; \lambda = 3"), S("Check $y$ and $z$", math=r"-2 + 15 = 13, \qquad 3 - 3 = 0")],
       concept="Testing a point on a line", skill="Calculation", hint="Find lambda from one coordinate, then check the other two.",
       feedback="A point is on the line only if one value of lambda fits all three coordinates."),
    NUM(r"Find the acute angle between the lines with direction vectors $(2, 1, -2)$ and $(1, -4, 8)$, in degrees to 1 decimal place.", 48.2, tolerance=0.1, unit="degrees",
        steps=[S("Scalar product", math=r"2 - 4 - 16 = -18"), S("Magnitudes", math=r"|(2, 1, -2)| = 3, \quad |(1, -4, 8)| = 9"),
               S("Use the modulus for the acute angle", math=r"\cos\theta = \frac{18}{27} = \frac{2}{3} \;\Rightarrow\; \theta = 48.2^\circ")],
        concept="Angle between lines", skill="Calculation", hint="The scalar product is negative: take its modulus for the acute angle.",
        feedback="The acute angle between lines uses |d1.d2|."),
    MC(r"Which line is parallel to $\mathbf{r} = (0, 1, 2) + \lambda(2, -4, 6)$?", [
        C(r"$\mathbf{r} = (1, 1, 1) + \mu(1, -2, 3)$", correct=True),
        C(r"$\mathbf{r} = (0, 1, 2) + \mu(1, 2, 3)$", why="The direction $(1, 2, 3)$ is not a multiple of $(2, -4, 6)$: the sign of the middle component differs."),
        C(r"$\mathbf{r} = (2, -4, 6) + \mu(0, 1, 2)$", why="You used the direction vector as a point. Parallel lines have parallel **directions**."),
        C(r"$\mathbf{r} = (0, 1, 2) + \mu(-1, 2, -2)$", why=r"$(-1, 2, -2)$ is not a multiple of $(2, -4, 6)$ in the last component."),
    ], steps=[S("Simplify the direction", math=r"(2, -4, 6) = 2(1, -2, 3)"), S("Find the line with a multiple of $(1, -2, 3)$", text="Only the first option has a direction parallel to the given one.")],
       concept="Parallel lines", skill="Concept", hint="Write the direction in its simplest form first.",
       feedback="Parallel lines have directions that are multiples of each other."),
    MC(r"On the line $\mathbf{r} = (1, 2, -3) + \lambda(2, -1, 2)$, which point is 6 units from $A(1, 2, -3)$?", [
        C("$(3, 1, -1)$", why=r"This is $\lambda = 1$: its distance from $A$ is $|\mathbf{d}| = 3$, not 6."),
        C("$(5, 0, 1)$", correct=True),
        C("$(7, -1, 3)$", why=r"This is $\lambda = 3$: its distance from $A$ is 9."),
        C("$(13, -4, 9)$", why=r"This is $\lambda = 6$. The distance is $|\lambda| \times 3 = 18$, not $6$. The number 6 is the distance, not the parameter."),
    ], steps=[S("Magnitude of the direction", math=r"|(2, -1, 2)| = 3"), S("Distance condition", math=r"3|\lambda| = 6 \;\Rightarrow\; \lambda = \pm 2"), S("Take $\\lambda = 2$", math=r"(1 + 4,\ 2 - 2,\ -3 + 4) = (5, 0, 1)")],
       concept="Distance along a line", skill="Application", hint="Distance from A is the size of lambda times the magnitude of d.",
       feedback="Distance from A equals |λ||d|."),
]

# ---------------------------------------------------------------- Set 4: vector and cartesian equations of planes
VEC_4 = [
    MC(r"Which vector is normal to the plane $3x - 2y + 5z = 7$?", [
        C(r"$(3, -2, 5)$", correct=True),
        C(r"$(3, 2, 5)$", why="Check the sign of the $y$ coefficient: it is $-2$."),
        C(r"$(3, -2, 7)$", why="The 7 is the constant $d$ on the right-hand side, not the coefficient of $z$."),
        C(r"$(5, -2, 3)$", why="The components are in the wrong order: $x$, $y$, $z$ give $3$, $-2$, $5$."),
    ], steps=[S("The coefficients of $x$, $y$, $z$ form the normal", math=r"\mathbf{n} = (3, -2, 5)")],
       concept="Normal vector of a plane", skill="Recall", hint="Read the coefficients of x, y and z.",
       feedback="In n1 x + n2 y + n3 z = d the vector (n1, n2, n3) is the normal."),
    MC(r"A plane passes through $(1, 2, 3)$ and has normal $(2, 1, -1)$. What is its equation?", [
        C(r"$2x + y - z = 7$", why=r"You forgot the sign of the $z$ coefficient when finding $d$: $2 + 2 - 3 = 1$, not $2 + 2 + 3$."),
        C(r"$2x + y - z = 1$", correct=True),
        C(r"$2x + y - z = -1$", why=r"$2 + 2 - 3 = +1$. Check the sign of $d$."),
        C(r"$x + 2y + 3z = 1$", why="You used the point as the normal. The coefficients come from the normal vector."),
    ], steps=[S("Coefficients from the normal", math=r"2x + y - z = d"), S("Substitute the point", math=r"d = 2(1) + 2 - 3 = 1")],
       concept="Plane from a point and a normal", skill="Calculation", hint="Write the normal's components as coefficients, then substitute the point to find d.",
       feedback="d = a.n for any point a on the plane."),
    NUM(r"A plane through $(2, -1, 4)$ has normal $(3, 2, 1)$ and equation $3x + 2y + z = d$. Find $d$.", 8,
        steps=[S("Substitute the point", math=r"d = 3(2) + 2(-1) + 1(4) = 6 - 2 + 4 = 8")],
        concept="Finding d for a plane", skill="Calculation", hint="Put the coordinates of the point into the left-hand side.",
        feedback="d is the value of the left-hand side at a point on the plane."),
    MC(r"Which point lies on the plane $2x - y + 3z = 10$?", [
        C("$(1, 2, 3)$", why=r"$2 - 2 + 9 = 9$, not $10$."),
        C("$(2, -1, 2)$", why=r"$4 + 1 + 6 = 11$, not $10$."),
        C("$(3, 2, 2)$", correct=True),
        C("$(4, -1, 1)$", why=r"$8 + 1 + 3 = 12$, not $10$."),
    ], steps=[S("Substitute each point", math=r"(3, 2, 2):\ 6 - 2 + 6 = 10 \ \checkmark")],
       concept="Testing a point on a plane", skill="Calculation", hint="Substitute each point into the left-hand side.",
       feedback="A point is on the plane if its coordinates satisfy the equation."),
    MC(r"Find the equation of the plane through $A(1, 0, 0)$, $B(0, 2, 0)$ and $C(0, 0, 3)$.", [
        C(r"$x + 2y + 3z = 6$", why="You used the intercepts as coefficients. The coefficients form the normal, found from the vectors in the plane."),
        C(r"$3x + 2y + z = 6$", why=r"Check $A$: $3 \neq 6$. This plane does not pass through $A$."),
        C(r"$6x + 3y + 2z = 11$", why=r"Check $A$: $6 \neq 11$. $d$ must come from substituting a point."),
        C(r"$6x + 3y + 2z = 6$", correct=True),
    ], steps=[S("Vectors in the plane", math=r"\overrightarrow{AB} = (-1, 2, 0), \quad \overrightarrow{AC} = (-1, 0, 3)"),
              S("Normal $(a, b, c)$ perpendicular to both", math=r"-a + 2b = 0, \quad -a + 3c = 0 \;\Rightarrow\; \mathbf{n} = (6, 3, 2)"),
              S("Find $d$ using $A$", math=r"d = 6")],
       concept="Plane through three points", skill="Calculation", hint="Find AB and AC, then a vector perpendicular to both.",
       feedback="Check all three points in the final equation."),
    NUM(r"Find the acute angle between the planes $2x + y + 2z = 5$ and $x - 4y + 8z = 3$, in degrees to 1 decimal place.", 58.8, tolerance=0.1, unit="degrees",
        steps=[S("Normals", math=r"\mathbf{n}_1 = (2, 1, 2), \quad \mathbf{n}_2 = (1, -4, 8)"),
               S("Scalar product and magnitudes", math=r"2 - 4 + 16 = 14, \quad |\mathbf{n}_1| = 3, \quad |\mathbf{n}_2| = 9"),
               S("Angle", math=r"\cos\theta = \frac{14}{27} \;\Rightarrow\; \theta = 58.8^\circ")],
        concept="Angle between planes", skill="Calculation", hint="The angle between planes is the angle between their normals.",
        feedback="Use the normals and the cosine formula."),
    MC(r"Convert $\mathbf{r} = (1, 0, 1) + s(1, 2, 0) + t(0, 1, 1)$ to cartesian form.", [
        C(r"$2x - y + z = 3$", correct=True),
        C(r"$x + 3y + z = 2$", why=r"You added the two directions to get a normal. The normal is perpendicular to **both** directions: $(1, 3, 1)\cdot(1, 2, 0) = 7 \neq 0$."),
        C(r"$2x - y + z = -3$", why=r"Check the sign of $d$: $2(1) - 0 + 1 = +3$."),
        C(r"$x - y + 2z = 3$", why=r"This normal fails $\mathbf{n}\cdot(1, 2, 0) = 0$: $1 - 2 = -1$."),
    ], steps=[S("Normal perpendicular to both directions", math=r"a + 2b = 0, \quad b + c = 0 \;\Rightarrow\; \mathbf{n} = (2, -1, 1)"), S("Find $d$ with $(1, 0, 1)$", math=r"d = 2 + 1 = 3")],
       concept="Parametric to cartesian form of a plane", skill="Calculation", hint="Find a vector perpendicular to both direction vectors.",
       feedback="n.b = 0 and n.c = 0 for the two directions b and c."),
    MC(r"Which plane is parallel to $2x - 4y + 6z = 5$?", [
        C(r"$2x + 4y + 6z = 5$", why="The sign of the $y$ coefficient changed, so the normal is not parallel."),
        C(r"$3x - 4y + 6z = 5$", why="The normal $(3, -4, 6)$ is not a multiple of $(2, -4, 6)$."),
        C(r"$x - 2y + 3z = 9$", correct=True),
        C(r"$x - 2y + 6z = 5$", why="The normal $(1, -2, 6)$ is not a multiple of $(2, -4, 6)$."),
    ], steps=[S("Halve the normal", math=r"(2, -4, 6) = 2(1, -2, 3)"), S("Parallel planes have parallel normals", text=r"$x - 2y + 3z = 9$ has normal $(1, -2, 3)$.")],
       concept="Parallel planes", skill="Concept", hint="Parallel planes have normals that are multiples of each other.",
       feedback="The constant d can be anything for a parallel plane."),
]

# ---------------------------------------------------------------- Set 5: intersections of lines and planes
VEC_5 = [
    MC(r"$l_1: \mathbf{r} = (1, 0, 2) + \lambda(3, -1, 2)$ and $l_2: \mathbf{r} = (0, 5, 1) + \mu(-6, 2, -4)$. What is the relationship between the lines?", [
        C("Skew", why=r"Skew lines have directions that are **not** parallel. Here $(-6, 2, -4) = -2(3, -1, 2)$."),
        C("They intersect at one point", why=r"Parallel lines never meet, unless they are the same line."),
        C("Parallel and distinct", correct=True),
        C("The same line", why=r"$(0, 5, 1) - (1, 0, 2) = (-1, 5, -1)$ is not a multiple of $(3, -1, 2)$, so $l_2$ does not pass through the point of $l_1$."),
    ], steps=[S("Compare directions", math=r"(-6, 2, -4) = -2(3, -1, 2)", text="Parallel directions."),
              S("Is a point of $l_2$ on $l_1$?", math=r"(-1, 5, -1) \text{ is not a multiple of } (3, -1, 2)", text="So the lines are distinct.")],
       concept="Parallel lines in 3D", skill="Reasoning", hint="Compare the direction vectors first.",
       feedback="Parallel directions: parallel lines, then check whether they coincide."),
    NUM(r"The line $\mathbf{r} = (1, 2, -1) + \lambda(2, 1, 3)$ meets the plane $2x - y + z = 11$. Find the value of $\lambda$ at the point of intersection.", 2,
        steps=[S("Substitute the line into the plane", math=r"2(1 + 2\lambda) - (2 + \lambda) + (-1 + 3\lambda) = 11"),
               S("Simplify", math=r"-1 + 6\lambda = 11"), S("Solve", math=r"\lambda = 2")],
        concept="Line meets plane", skill="Calculation", hint="Write x, y, z in terms of lambda and substitute into the plane's equation.",
        feedback="Substitution gives one equation in lambda."),
    MC(r"$l_1: \mathbf{r} = (1, 2, 3) + \lambda(1, -1, 2)$ and $l_2: \mathbf{r} = (4, 0, 2) + \mu(-1, 0, 5)$ intersect. Find the point of intersection.", [
        C("$(1, 2, 3)$", why=r"This is the point of $l_1$ with $\lambda = 0$. It is not on $l_2$."),
        C("$(4, 0, 2)$", why=r"This is the point of $l_2$ with $\mu = 0$. It is not on $l_1$."),
        C("$(2, 1, 5)$", why=r"This is on $l_1$ ($\lambda = 1$) but not on $l_2$."),
        C("$(3, 0, 7)$", correct=True),
    ], steps=[S("Equate components", math=r"1 + \lambda = 4 - \mu, \quad 2 - \lambda = 0, \quad 3 + 2\lambda = 2 + 5\mu"),
              S("Solve", math=r"\lambda = 2, \quad \mu = 1"), S("Point", math=r"(1 + 2,\ 2 - 2,\ 3 + 4) = (3, 0, 7)")],
       concept="Intersection of two lines", skill="Calculation", hint="Equate the x, y and z components and solve two of the equations.",
       feedback="Solve two equations, test the third, then substitute."),
    MC(r"The line $\mathbf{r} = (0, 1, 1) + \lambda(1, 1, -1)$ lies in the plane $x + y + 2z = k$. Find $k$.", [
        C("$3$", correct=True),
        C("$2$", why=r"The point $(0, 1, 1)$ gives $0 + 1 + 2 = 3$: the $z$ coefficient is 2."),
        C("$0$", why="The plane does not pass through the origin: substitute a point of the line."),
        C("$1$", why=r"You used $y = 1$ only. All three terms must be included."),
    ], steps=[S("Check the direction is parallel to the plane", math=r"(1, 1, -1)\cdot(1, 1, 2) = 1 + 1 - 2 = 0"), S("Use the point of the line", math=r"k = 0 + 1 + 2(1) = 3")],
       concept="Line lying in a plane", skill="Reasoning", hint="A line in a plane has every point on the plane: use the point (0, 1, 1).",
       feedback="Direction perpendicular to the normal, and one point on the plane."),
    MC(r"$l_1: \mathbf{r} = (1, 1, 0) + \lambda(1, 0, 1)$ and $l_2: \mathbf{r} = (0, 0, 1) + \mu(0, 1, 1)$. Which statement is true?", [
        C("They intersect at one point", why=r"The $x$ equation gives $\lambda = -1$ and the $y$ equation $\mu = 1$, but then $z$: $-1 \neq 2$. No common point."),
        C("They are skew", correct=True),
        C("They are parallel", why="The directions $(1, 0, 1)$ and $(0, 1, 1)$ are not multiples of each other."),
        C("They are the same line", why="The lines have different directions, so they cannot be the same line."),
    ], steps=[S("Equate", math=r"1 + \lambda = 0, \quad 1 = \mu, \quad \lambda = 1 + \mu"),
              S("Solve the first two", math=r"\lambda = -1, \quad \mu = 1"), S("Test the third", math=r"-1 \neq 2", text="No solution, and the directions are not parallel: skew.")],
       concept="Skew lines", skill="Reasoning", hint="Solve two equations then test the third.",
       feedback="Not parallel and no common point means skew."),
    NUM(r"Find the acute angle between the line $\mathbf{r} = \mathbf{a} + \lambda(1, 2, 2)$ and the plane $2x - y + 2z = 7$, in degrees to 1 decimal place.", 26.4, tolerance=0.1, unit="degrees",
        steps=[S("Scalar product of direction and normal", math=r"(1, 2, 2)\cdot(2, -1, 2) = 2 - 2 + 4 = 4"), S("Magnitudes", math=r"3 \text{ and } 3"),
               S("Use sine", math=r"\sin\theta = \frac{4}{9} \;\Rightarrow\; \theta = 26.4^\circ")],
        concept="Angle between a line and a plane", skill="Calculation", hint="For a line and a plane use sine, with the normal.",
        feedback="sin θ = |d.n| / (|d||n|)."),
    MC(r"Which vector is the direction of the line of intersection of the planes $x + y + z = 3$ and $x - y + 2z = 1$?", [
        C(r"$(1, 1, 1)$", why="This is the normal of the first plane. The direction must be perpendicular to both normals."),
        C(r"$(1, -1, 2)$", why="This is the normal of the second plane. The direction must be perpendicular to both normals."),
        C(r"$(3, -1, -2)$", correct=True),
        C(r"$(2, 0, 3)$", why=r"This is the sum of the two normals. It is not perpendicular to both: $(2, 0, 3)\cdot(1, 1, 1) = 5 \neq 0$."),
    ], steps=[S("Perpendicular to both normals", math=r"a + b + c = 0, \quad a - b + 2c = 0"), S("Add, then solve", math=r"2a + 3c = 0 \;\Rightarrow\; (a, b, c) = (3, -1, -2)")],
       concept="Line of intersection of planes", skill="Reasoning", hint="The direction is perpendicular to both normal vectors.",
       feedback="Check: the scalar product with each normal is 0."),
    MC(r"Find where the line $\mathbf{r} = (1, 1, 1) + \lambda(1, 2, 3)$ meets the plane $x - y + z = 7$.", [
        C("$(4, 7, 10)$", correct=True),
        C("$(3, 5, 7)$", why=r"This is $\lambda = 2$. Check the plane: $3 - 5 + 7 = 5 \neq 7$."),
        C("$(2, 3, 4)$", why=r"This is $\lambda = 1$. Check the plane: $2 - 3 + 4 = 3 \neq 7$."),
        C("$(7, 13, 19)$", why=r"This is $\lambda = 6$. You found $7 - 1 = 6$ but forgot to divide by 2."),
    ], steps=[S("Substitute", math=r"(1 + \lambda) - (1 + 2\lambda) + (1 + 3\lambda) = 7"), S("Simplify and solve", math=r"1 + 2\lambda = 7 \;\Rightarrow\; \lambda = 3"), S("Point", math=r"(4, 7, 10)")],
       concept="Line meets plane", skill="Application", hint="Substitute x, y and z in terms of lambda into the plane.",
       feedback="One equation in lambda; then substitute back."),
]

# ---------------------------------------------------------------- Set 6: distances
VEC_6 = [
    MC(r"Find the distance from the origin to the plane $2x - 2y + z = 9$.", [
        C("$9$", why=r"You forgot to divide by $|\mathbf{n}| = 3$."),
        C("$3$", correct=True),
        C("$1$", why=r"You divided by $|\mathbf{n}|^2 = 9$ instead of $|\mathbf{n}| = 3$."),
        C(r"$\sqrt{3}$", why=r"You took the square root of the numerator, $\sqrt{9} = 3$, instead of dividing 9 by $|\mathbf{n}| = 3$."),
    ], steps=[S("Numerator", math=r"|0 - 0 + 0 - 9| = 9"), S("Magnitude of the normal", math=r"\sqrt{4 + 4 + 1} = 3"), S("Divide", math=r"\frac{9}{3} = 3")],
       concept="Distance from origin to a plane", skill="Calculation", hint="The distance is |d| divided by the magnitude of the normal.",
       feedback="Distance from the origin to n.r = d is |d| / |n|."),
    NUM(r"Find the distance from $P(1, 2, 3)$ to the plane $x + 2y + 2z = 2$.", 3,
        steps=[S("Value at $P$", math=r"1 + 4 + 6 - 2 = 9"), S("Divide by $|\\mathbf{n}| = 3$", math=r"\frac{9}{3} = 3")],
        concept="Distance from a point to a plane", skill="Calculation", hint="Substitute P into x + 2y + 2z - 2, then divide by the magnitude of the normal.",
        feedback="Distance = |n.p - d| / |n|."),
    MC(r"Find the foot of the perpendicular from $P(1, 1, 2)$ to the plane $2x - 3y + 6z = 4$.", [
        C(r"$\left(\tfrac{9}{7}, \tfrac{4}{7}, \tfrac{20}{7}\right)$", why=r"This moves $P$ **away** from the plane. The value $2 - 3 + 12 - 4 = 7$ is positive, so move in the direction of $-\mathbf{n}$."),
        C("$(-1, 4, -4)$", why=r"This is $P - \mathbf{n}$: the move is $\frac{7}{49}\mathbf{n} = \frac{1}{7}\mathbf{n}$, not $\mathbf{n}$."),
        C(r"$\left(\tfrac{5}{7}, \tfrac{10}{7}, \tfrac{8}{7}\right)$", correct=True),
        C("$(1, 1, 2)$", why=r"This is $P$ itself, which is not on the plane: $2 - 3 + 12 = 11 \neq 4$."),
    ], steps=[S("Value and normal magnitude", math=r"2 - 3 + 12 - 4 = 7, \quad |\mathbf{n}|^2 = 49"), S("Move back along the normal", math=r"F = P - \tfrac{7}{49}(2, -3, 6) = \left(\tfrac{5}{7}, \tfrac{10}{7}, \tfrac{8}{7}\right)")],
       concept="Foot of a perpendicular to a plane", skill="Application", hint="The foot is P moved along the normal direction. How far?",
       feedback="F = P - ((n.p - d)/|n|²) n."),
    MC(r"Find the distance between the parallel planes $3x - 4y + 12z = 5$ and $3x - 4y + 12z = 31$.", [
        C("$26$", why=r"You forgot to divide by $|\mathbf{n}| = 13$."),
        C(r"$\frac{2}{13}$", why=r"You divided by $|\mathbf{n}|^2 = 169$: $26 \div 169 = \frac{2}{13}$."),
        C(r"$\frac{36}{13}$", why="You added the constants instead of subtracting them."),
        C("$2$", correct=True),
    ], steps=[S("Difference of the constants", math=r"31 - 5 = 26"), S("Magnitude of the normal", math=r"\sqrt{9 + 16 + 144} = 13"), S("Divide", math=r"\frac{26}{13} = 2")],
       concept="Distance between parallel planes", skill="Calculation", hint="Subtract the constants and divide by the magnitude of the normal.",
       feedback="Parallel planes with the same normal: |d2 - d1| / |n|."),
    NUM(r"Find the shortest distance from $P(6, -1, 4)$ to the line $\mathbf{r} = (1, 1, 0) + \lambda(1, 2, 2)$.", 6,
        steps=[S("General point on the line", math=r"F = (1 + \lambda,\ 1 + 2\lambda,\ 2\lambda)"), S("$\\overrightarrow{PF}$", math=r"(\lambda - 5,\ 2\lambda + 2,\ 2\lambda - 4)"),
               S("Perpendicular to $(1, 2, 2)$", math=r"(\lambda - 5) + 2(2\lambda + 2) + 2(2\lambda - 4) = 9\lambda - 9 = 0 \;\Rightarrow\; \lambda = 1"),
               S("Distance", math=r"\overrightarrow{PF} = (-4, 4, -2), \quad |\overrightarrow{PF}| = \sqrt{16 + 16 + 4} = 6")],
        concept="Distance from a point to a line", skill="Application", hint="Write PF for a general point F on the line and use PF.d = 0.",
        feedback="Perpendicular condition PF.d = 0 gives lambda."),
    MC(r"Find the reflection of $P(2, 2, 2)$ in the plane $x + y + z = 3$.", [
        C("$(0, 0, 0)$", correct=True),
        C("$(1, 1, 1)$", why=r"This is the **foot** of the perpendicular, the midpoint of $P$ and its reflection."),
        C("$(-2, -2, -2)$", why="This is the reflection in the origin, not in the plane."),
        C("$(3, 3, 3)$", why=r"This moves $P$ **away** from the plane."),
    ], steps=[S("Foot", math=r"\text{value at } P = 6 - 3 = 3,\ |\mathbf{n}|^2 = 3 \;\Rightarrow\; F = (2, 2, 2) - 1\cdot(1, 1, 1) = (1, 1, 1)"), S("Reflection $= 2\\mathbf{f} - \\mathbf{p}$", math=r"(2, 2, 2) - (2, 2, 2) = (0, 0, 0)")],
       concept="Reflection in a plane", skill="Application", hint="Find the foot of the perpendicular first: it is the midpoint of P and its image.",
       feedback="Image = 2 × foot - P."),
    MC(r"$F$ is the point on the line $\mathbf{r} = \mathbf{a} + \lambda\mathbf{d}$ closest to a point $P$. Which equation lets you find $\lambda$?", [
        C(r"$\overrightarrow{PF} = \mathbf{d}$", why="This would fix the length and direction of PF to equal d, which is not the condition for the closest point."),
        C(r"$\overrightarrow{PF}\cdot\mathbf{d} = 0$", correct=True),
        C(r"$\overrightarrow{PF} \times \mathbf{d} = \mathbf{0}$", why="This says PF is parallel to the line, which is the opposite of perpendicular."),
        C(r"$|\overrightarrow{PF}| = |\mathbf{d}|$", why="The size of d has nothing to do with the distance."),
    ], steps=[S("The shortest distance is perpendicular to the line", math=r"\overrightarrow{PF}\cdot\mathbf{d} = 0")],
       concept="Perpendicular condition", skill="Concept", hint="What is true about the scalar product of perpendicular vectors?",
       feedback="Perpendicular means zero scalar product."),
    NUM(r"Find the distance from the line $\mathbf{r} = (1, 0, 2) + \lambda(1, 2, 0)$, which is parallel to the plane $2x - y + 3z = 5$, to the plane. Give your answer to 2 decimal places.", 0.8, tolerance=0.01,
        steps=[S("A point on the line is $(1, 0, 2)$", math=r"2(1) - 0 + 3(2) - 5 = 3"), S("Divide by $|\\mathbf{n}| = \\sqrt{14}$", math=r"\frac{3}{\sqrt{14}} = 0.80")],
        concept="Distance from a line to a parallel plane", skill="Application", hint="Every point of the line has the same distance. Take one of them.",
        feedback="Use a point on the line in the point-to-plane formula."),
]

# ---------------------------------------------------------------- Exam practice set 1: Paper 1 strategy
EXAM_1 = [
    NUM("In KKEVO's Paper 1 practice setting there are 40 questions and 90 minutes. What is the average time per question, in minutes?", 2.25, tolerance=0.01, unit="minutes",
        steps=[S("Divide the time by the number of questions", math=r"\frac{90}{40} = 2.25")],
        concept="Time management", skill="Calculation", hint="Divide the total time by the number of questions.",
        feedback="About 2 minutes a question: move on when a question is taking much longer."),
    MC(r"$y = (3x + 2)^4$. Using $x = 0$ as a test value, which is $\dfrac{dy}{dx}$?", [
        C(r"$4(3x + 2)^3$", why=r"At $x = 0$ this gives $32$, but the true gradient at $x = 0$ is $96$. The derivative of the bracket, $3$, is missing."),
        C(r"$12(3x + 2)^3$", correct=True),
        C(r"$12(3x + 2)^4$", why="The power must fall from 4 to 3."),
        C(r"$3(3x + 2)^3$", why=r"Only the factor 3 from the bracket was used. The power $4$ must also come down: $4 \times 3 = 12$."),
    ], steps=[S("Chain rule", math=r"\frac{dy}{dx} = 4(3x + 2)^3 \times 3 = 12(3x + 2)^3"), S("Test at $x = 0$", math=r"12 \times 2^3 = 96", text="The other options give 32, 192 and 24.")],
       concept="Test values and the chain rule", skill="Reasoning", hint="Find the true gradient at x = 0 first, then test each option at x = 0.",
       feedback="A test value can quickly eliminate options."),
    MC(r"$\alpha$ and $\beta$ are the roots of $x^2 - 5x + 2 = 0$. Find $\alpha^2 + \beta^2$.", [
        C("$25$", why=r"This is $(\alpha + \beta)^2$. You must subtract $2\alpha\beta$."),
        C("$23$", why=r"You subtracted $\alpha\beta = 2$. The identity uses $2\alpha\beta = 4$."),
        C("$21$", correct=True),
        C("$29$", why=r"You added $2\alpha\beta$. The identity is $(\alpha + \beta)^2 - 2\alpha\beta$."),
    ], steps=[S("Sum and product", math=r"\alpha + \beta = 5, \quad \alpha\beta = 2"), S("Identity", math=r"\alpha^2 + \beta^2 = 25 - 4 = 21")],
       concept="Symmetric functions of roots", skill="Calculation", hint="Write alpha² + beta² using (alpha + beta)².",
       feedback="The wrong options are the common slips: forgetting the 2, or using the wrong sign."),
    MC("Your calculator is in degree mode. You calculate $\\sin 1$ in a calculus question, where angles are in radians. Which value should you get?", [
        C("$0.0175$", why=r"This is $\sin 1^\circ$. The calculator was in degree mode."),
        C("$0.540$", why=r"This is $\cos 1$ (radians): the wrong function was used."),
        C("$1.557$", why=r"This is $\tan 1$ (radians): the wrong function was used."),
        C("$0.841$", correct=True),
    ], steps=[S("Switch to radian mode", math=r"\sin 1 = 0.841")],
       concept="Calculator mode", skill="Application", hint="Calculus uses radians. Which mode is that?",
       feedback="In calculus, always check the calculator is in radian mode."),
    NUM(r"The curve $y = \dfrac{x^2 + 1}{x - 1}$ has an oblique asymptote $y = x + c$. Find $c$.", 1,
        steps=[S("Divide", math=r"x^2 + 1 = (x - 1)(x + 1) + 2"), S("Rewrite", math=r"y = x + 1 + \frac{2}{x - 1}"), S("As $x \\to \\infty$", math=r"y \to x + 1, \quad c = 1")],
        concept="Oblique asymptotes", skill="Calculation", hint="Divide x² + 1 by x - 1.",
        feedback="The quotient from the division gives the oblique asymptote."),
    MC(r"At $x = 2$, which expression equals $\dfrac{1}{(x - 1)(x + 1)}$? (Test the value $x = 2$.)", [
        C(r"$\dfrac{1}{2(x - 1)} - \dfrac{1}{2(x + 1)}$", correct=True),
        C(r"$\dfrac{1}{x - 1} - \dfrac{1}{x + 1}$", why=r"At $x = 2$ this is $1 - \tfrac{1}{3} = \tfrac{2}{3}$, but $\dfrac{1}{(1)(3)} = \dfrac{1}{3}$. The $\tfrac{1}{2}$ is missing."),
        C(r"$\dfrac{1}{x - 1} + \dfrac{1}{x + 1}$", why=r"At $x = 2$ this is $1 + \tfrac{1}{3} = \tfrac{4}{3}$, not $\tfrac{1}{3}$."),
        C(r"$\dfrac{1}{2(x - 1)} + \dfrac{1}{2(x + 1)}$", why=r"At $x = 2$ this is $\tfrac{1}{2} + \tfrac{1}{6} = \tfrac{2}{3}$, not $\tfrac{1}{3}$."),
    ], steps=[S("Value of the target at $x = 2$", math=r"\frac{1}{(1)(3)} = \frac{1}{3}"), S("Test the options", math=r"\tfrac{1}{2} - \tfrac{1}{6} = \tfrac{1}{3} \ \checkmark")],
       concept="Partial fractions by testing a value", skill="Reasoning", hint="Work out the value of the given fraction at x = 2, then test each option.",
       feedback="Substituting a value is a fast check on partial fractions."),
    MC(r"Without doing the full integral, which is closest to $\displaystyle\int_0^1 x e^x\,dx$? (The integrand rises from $0$ to $e$.)", [
        C("$0.5$", why=r"At $x = 0.5$ the integrand is $0.5e^{0.5} = 0.82$, so the area is much larger than 0.5."),
        C("$1$", correct=True),
        C("$1.7$", why=r"This would need the average height to be $1.7$, but the integrand only reaches $2.7$ at $x = 1$ and is small for most of the interval."),
        C("$2.7$", why=r"This is $e$, the value of the integrand at $x = 1$. The area cannot exceed $e \times 1$ and is much smaller."),
    ], steps=[S("Estimate with a midpoint", math=r"0.5e^{0.5} \approx 0.82"), S("Exact value by parts", math=r"[xe^x - e^x]_0^1 = 0 - (-1) = 1")],
       concept="Estimating an integral", skill="Reasoning", hint="Estimate the height of the curve in the middle of the interval.",
       feedback="A quick estimate rules out options that are far too small or too large."),
    MC(r"A candidate differentiates $y = x^2\ln x$ and gets $2x\ln x$. Which test value shows the error?", [
        C(r"$x = 2$: both give the same value", why=r"They do not: the true gradient is $4\ln 2 + 2$, but $2x\ln x = 4\ln 2$."),
        C(r"$x = 0$: the function is not defined", why=r"$\ln 0$ is undefined, so $x = 0$ cannot be tested at all."),
        C(r"$x = 1$: the true gradient is $1$, but $2x\ln x = 0$", correct=True),
        C(r"$x = -1$: both give $0$", why=r"$\ln(-1)$ is not defined, so $x = -1$ cannot be tested."),
    ], steps=[S("True derivative (product rule)", math=r"\frac{dy}{dx} = 2x\ln x + x"), S("At $x = 1$", math=r"2(1)(0) + 1 = 1 \neq 0")],
       concept="Checking a derivative with a test value", skill="Reasoning", hint="Choose a value where ln x is easy to evaluate, such as x = 1.",
       feedback="Pick a test value that separates the right answer from the wrong one."),
]

# ---------------------------------------------------------------- Exam practice set 2: Paper 2 structured questions
EXAM_2 = [
    MC("In a question, the instruction is: Show that the equation has a root between 1 and 2. What must you do?", [
        C("Give the value of the root", why="A root is not asked for; you must show that one exists in the interval."),
        C("Draw a sketch only", why="A sketch alone does not show the sign change with values."),
        C("Show the function changes sign between 1 and 2 (and is continuous)", correct=True),
        C("State the result is true", why="A show-that question needs working, not a statement."),
    ], steps=[S("Evaluate at the ends", text=r"For $f(x) = x^3 + x - 5$: $f(1) = -3$ and $f(2) = 5$."), S("Conclude", text="The function changes sign and is continuous, so there is a root between 1 and 2.")],
       concept="Show that questions", skill="Concept", hint="What evidence proves a root lies in an interval?",
       feedback="Show that means the working is the answer."),
    MC("A question says: Hence solve ... What does hence mean?", [
        C("Use any method you like", why="Hence means use the previous result: another method may not earn credit."),
        C("Use the result of the previous part", correct=True),
        C("Give a decimal answer", why="Hence is about the method, not the form of the answer."),
        C("Ignore the previous part", why="The opposite: hence points to the previous part."),
    ], steps=[S("Command word", text="Hence: use what you have just shown to answer the next part.")],
       concept="Command words", skill="Recall", hint="Look back at the previous part of the question.",
       feedback="Hence: build on the previous result."),
    NUM(r"You have shown that $\cos 3\theta = 4\cos^3\theta - 3\cos\theta$. Hence find the smallest positive solution, in degrees, of $4\cos^3\theta - 3\cos\theta = \tfrac{1}{2}$.", 20, unit="degrees",
        steps=[S("Use the identity", math=r"\cos 3\theta = \tfrac{1}{2}"), S("Smallest positive $3\\theta$", math=r"3\theta = 60^\circ"), S("Divide by 3", math=r"\theta = 20^\circ")],
        concept="Using a previous result", skill="Application", hint="The left-hand side equals cos 3θ.",
        feedback="Hence uses the result you have just proved."),
    NUM(r"Solve $\dfrac{dy}{dx} = 2xy$ with $y = 3$ when $x = 0$. Then $y = Ae^{x^2}$ when $x = 1$ is $Ae$. Find $A$.", 3,
        steps=[S("Separate and integrate", math=r"\ln y = x^2 + c"), S("Initial condition", math=r"c = \ln 3"), S("Solve", math=r"y = 3e^{x^2}, \quad A = 3")],
        concept="Differential equation with a condition", skill="Calculation", hint="Separate the variables, integrate, then use y = 3 at x = 0.",
        feedback="Use the initial condition to find the constant."),
    MC(r"For the curve $y = xe^{-x}$, $\dfrac{d^2y}{dx^2} = e^{-x}(x - 2)$. At the stationary point $x = 1$, what is the nature of the point?", [
        C("A minimum", why=r"At $x = 1$, $\frac{d^2y}{dx^2} = -e^{-1} < 0$. A minimum needs a positive second derivative."),
        C("It cannot be determined", why="The second derivative is non-zero, so the nature is determined."),
        C("A point of inflection", why="A point of inflection needs a second derivative of 0; here it is negative."),
        C("A maximum", correct=True),
    ], steps=[S("Evaluate", math=r"e^{-1}(1 - 2) = -\frac{1}{e} < 0"), S("Conclude", text="Negative second derivative: a maximum.")],
       concept="Nature of a stationary point", skill="Reasoning", hint="Substitute x = 1 into the second derivative and look at the sign.",
       feedback="Negative second derivative: maximum. Positive: minimum."),
    NUM(r"Part (a) gives $x = 2.4567\ldots$ on your calculator. In part (b) find $x^2$ to 3 significant figures, using the full calculator value.", 6.04, tolerance=0.005,
        steps=[S("Square the full value", math=r"2.4567^2 = 6.0354 \approx 6.04")],
        concept="Accuracy", skill="Calculation", hint="Use the stored value, not a rounded one.",
        feedback="Rounding $x$ to 2.46 first would give 6.05."),
    MC(r"The Maclaurin series of $(1 + x)e^{-x}$ begins $1 - \tfrac{1}{2}x^2 + kx^3 + \ldots$. Find $k$.", [
        C(r"$\tfrac{1}{3}$", correct=True),
        C(r"$-\tfrac{1}{6}$", why=r"This is only the $x^3$ term of $e^{-x}$. You must also include $x \times \frac{x^2}{2}$ from the bracket."),
        C(r"$\tfrac{1}{2}$", why=r"This is only the product $x \times \frac{x^2}{2}$. Add the $-\frac{1}{6}$ from $e^{-x}$."),
        C(r"$-\tfrac{1}{3}$", why=r"The sign is positive: $-\tfrac{1}{6} + \tfrac{1}{2} = +\tfrac{1}{3}$."),
    ], steps=[S("Expand", math=r"e^{-x} = 1 - x + \tfrac{x^2}{2} - \tfrac{x^3}{6} + \ldots"), S("Collect $x^3$ in $(1 + x)e^{-x}$", math=r"-\tfrac{1}{6} + \tfrac{1}{2} = \tfrac{1}{3}")],
       concept="Series multiplication", skill="Calculation", hint="Collect every way of getting x³: 1 times the x³ term, and x times the x² term.",
       feedback="Collect all products that give the required power."),
    MC(r"Which working shows that $f(x) = x^3 + x - 5$ has a root between $1$ and $2$?", [
        C(r"$f(1) = -3$, $f(2) = 5$: a change of sign, so a root", correct=True),
        C(r"$f(1) = -5$, $f(2) = 5$: a change of sign, so a root", why=r"$f(1) = 1 + 1 - 5 = -3$, not $-5$: you left out the term $x^3$."),
        C(r"$f(1) = -3$, $f(2) = -3$: no change", why=r"$f(2) = 8 + 2 - 5 = 5$: check the arithmetic."),
        C(r"$f(1) = 3$, $f(2) = 5$: both positive, so a root", why="Both positive would mean no sign change. Also $f(1) = -3$, not 3."),
    ], steps=[S("Evaluate", math=r"f(1) = 1 + 1 - 5 = -3, \quad f(2) = 8 + 2 - 5 = 5"), S("Sign change", text="A continuous function changes sign, so there is a root in the interval.")],
       concept="Locating a root", skill="Application", hint="Evaluate f at 1 and at 2 carefully.",
       feedback="Correct values and a sign change, with continuity."),
]

# ---------------------------------------------------------------- Paper 1 mock A: 40 multiple-choice questions
# The position of the correct option cycles through permutations so A, B, C and D are each correct 10 times.
_POS = [0, 1, 2, 3, 2, 3, 0, 1, 1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 1, 3, 0, 2, 2, 0, 3, 1, 3, 1, 2, 0, 0, 3, 2, 1, 2, 1, 0, 3]

P1_QUESTIONS = []


def _q(prompt, right, wrongs, steps, concept, skill, hint):
    """Add one four-option question; `wrongs` is a list of three (text, why) pairs."""
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(_POS[len(P1_QUESTIONS)], C(right, correct=True))
    P1_QUESTIONS.append(MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint))


# ---- Proof (3)
_q(r"A proof by induction shows that $f(n) = 5^n - 1$ is divisible by 4. Which expression gives $f(k+1)$ in terms of $f(k)$?",
   r"$5f(k) + 4$",
   [(r"$5f(k) - 4$", r"$5(5^k - 1) - 4 = 5^{k+1} - 9$, not $f(k+1)$."),
    (r"$4f(k) + 5$", r"$4(5^k - 1) + 5 = 4\cdot 5^k + 1$, not $5^{k+1} - 1$."),
    (r"$f(k) + 4$", r"$5^k - 1 + 4 = 5^k + 3$, not $5^{k+1} - 1$.")],
   [S("Write $f(k+1)$", math=r"5^{k+1} - 1 = 5\cdot 5^k - 1"), S("Make $f(k)$ appear", math=r"= 5(5^k - 1) + 4 = 5f(k) + 4")],
   "Proof", "Reasoning", "Write 5^(k+1) as 5 times 5^k, then bring in the bracket 5^k - 1.")
_q(r"To prove by contradiction that $\sqrt{3}$ is irrational, we assume $\sqrt{3} = \dfrac{a}{b}$ in lowest terms. The contradiction is reached when we show that:",
   r"$a$ and $b$ are both divisible by 3",
   [(r"$a$ and $b$ are both even", r"This is the argument for $\sqrt{2}$. For $\sqrt{3}$ the factor is 3."),
    (r"$\sqrt{3}$ is an integer", "Nothing in the argument shows this: the assumption is a fraction in lowest terms."),
    (r"$a = b$", r"If $a = b$ then $\sqrt{3} = 1$, which is false, but this is not how the contradiction arises.")],
   [S("Square", math=r"a^2 = 3b^2, \text{ so } 3 \mid a^2 \text{ and } 3 \mid a"), S("Write $a = 3m$", math=r"9m^2 = 3b^2 \Rightarrow b^2 = 3m^2, \text{ so } 3 \mid b"),
    S("Contradiction", text="$a$ and $b$ share the factor 3, but the fraction was in lowest terms.")],
   "Proof", "Concept", "What does lowest terms say about common factors of a and b?")
_q(r"Given that $\displaystyle\sum_{r=1}^{n} r(r + 1) = \frac{n(n+1)(n+2)}{3}$, find $\displaystyle\sum_{r=1}^{10} r(r + 1)$.",
   "$440$",
   [("$220$", r"You divided by 6. The formula has a denominator of 3."),
    ("$385$", r"This is $\sum r^2$, not $\sum r(r+1)$."),
    ("$1320$", "You forgot to divide by 3: $10 \\times 11 \\times 12 = 1320$.")],
   [S("Substitute $n = 10$", math=r"\frac{10 \times 11 \times 12}{3} = \frac{1320}{3} = 440")],
   "Proof", "Application", "Put n = 10 into the formula.")

# ---- Algebra (4)
_q(r"Express $\dfrac{5x + 1}{(x - 1)(x + 2)}$ in partial fractions.",
   r"$\dfrac{2}{x - 1} + \dfrac{3}{x + 2}$",
   [(r"$\dfrac{3}{x - 1} + \dfrac{2}{x + 2}$", "The constants are the wrong way round: at $x = 1$ the numerator gives $6 = 3A$, so $A = 2$."),
    (r"$\dfrac{2}{x - 1} - \dfrac{3}{x + 2}$", r"At $x = -2$: $-9 = -3B$, so $B = +3$."),
    (r"$\dfrac{5}{x - 1} + \dfrac{1}{x + 2}$", "These are the coefficients of the numerator, not the partial fraction constants.")],
   [S("Write", math=r"5x + 1 = A(x + 2) + B(x - 1)"), S("$x = 1$", math=r"6 = 3A \Rightarrow A = 2"), S("$x = -2$", math=r"-9 = -3B \Rightarrow B = 3")],
   "Algebra", "Calculation", "Use the cover-up method or substitute x = 1 and x = -2.")
_q(r"Find the coefficient of $x^2$ in the expansion of $(1 - 3x)^{-2}$.",
   "$27$",
   [("$9$", r"This is $(-3)^2$ only. Include the factor $\frac{(-2)(-3)}{2!} = 3$."),
    ("$-27$", r"$(-3x)^2$ is positive, and $(-2)(-3) = +6$."),
    ("$54$", r"You forgot to divide by $2!$: $\frac{(-2)(-3)}{2!} = 3$, not 6.")],
   [S("Binomial coefficient", math=r"\frac{(-2)(-3)}{2!} = 3"), S("Multiply by $(-3)^2$", math=r"3 \times 9 = 27")],
   "Algebra", "Calculation", "Use the binomial expansion with the index -2 and the term (-3x).")
_q(r"$\alpha$ and $\beta$ are the roots of $x^2 - 5x + 3 = 0$. Find the equation whose roots are $2\alpha$ and $2\beta$.",
   r"$x^2 - 10x + 12 = 0$",
   [(r"$x^2 - 10x + 3 = 0$", r"The product is $4\alpha\beta = 12$, not $3$."),
    (r"$x^2 - 5x + 12 = 0$", r"The sum is $2(\alpha + \beta) = 10$, not $5$."),
    (r"$x^2 - 10x + 6 = 0$", r"The product of $2\alpha$ and $2\beta$ is $4\alpha\beta$, not $2\alpha\beta$.")],
   [S("Sum and product", math=r"\alpha + \beta = 5, \quad \alpha\beta = 3"), S("New sum and product", math=r"2\alpha + 2\beta = 10, \quad (2\alpha)(2\beta) = 12"), S("Equation", math=r"x^2 - 10x + 12 = 0")],
   "Algebra", "Reasoning", "Find the sum and product of the new roots.")
_q(r"For which values of $x$ is the expansion of $(1 - 2x)^{-3}$ valid?",
   r"$|x| < \dfrac{1}{2}$",
   [(r"$|x| < 2$", r"You inverted the condition: $|2x| < 1$ gives $|x| < \frac{1}{2}$."),
    (r"$|x| < 1$", "The condition is on $2x$, not on $x$."),
    (r"$x < \dfrac{1}{2}$", r"Both signs matter: $-\frac{1}{2} < x < \frac{1}{2}$.")],
   [S("Condition", math=r"|-2x| < 1"), S("Solve", math=r"|x| < \tfrac{1}{2}")],
   "Algebra", "Concept", "The expansion of (1 + u)^n is valid when |u| < 1.")

# ---- Functions and graphs (4)
_q(r"$f(x) = 2x + 1$ and $g(x) = x^2$. Find $gf(3)$.",
   "$49$",
   [("$19$", "This is $fg(3)$. $gf$ means apply $f$ first, then $g$."),
    ("$7$", "This is $f(3)$ only. Now apply $g$."),
    ("$16$", r"This is $(3 + 1)^2$: you replaced $f(3)$ by $x + 1$.")],
   [S("$f(3)$", math=r"2(3) + 1 = 7"), S("$g(7)$", math=r"7^2 = 49")],
   "Functions and graphs", "Calculation", "gf(3) means g(f(3)): do f first.")
_q(r"$f(x) = \dfrac{2x + 1}{x - 3}$, $x \neq 3$. Find $f^{-1}(x)$.",
   r"$\dfrac{3x + 1}{x - 2}$",
   [(r"$\dfrac{x - 3}{2x + 1}$", r"This is $\frac{1}{f(x)}$, not the inverse function."),
    (r"$\dfrac{3x - 1}{x - 2}$", r"Check the sign: $y(x - 3) = 2x + 1$ gives $x(y - 2) = 3y + 1$."),
    (r"$\dfrac{3x + 1}{x + 2}$", "The denominator is $y - 2$: collect the $x$ terms carefully.")],
   [S("Let $y = f(x)$", math=r"y(x - 3) = 2x + 1"), S("Collect the $x$ terms", math=r"xy - 2x = 3y + 1 \Rightarrow x(y - 2) = 3y + 1"), S("Swap $x$ and $y$", math=r"f^{-1}(x) = \frac{3x + 1}{x - 2}")],
   "Functions and graphs", "Calculation", "Rearrange y = f(x) to make x the subject.")
_q(r"Which is an oblique asymptote of $y = \dfrac{2x^2 + 3x - 1}{x + 1}$?",
   "$y = 2x + 1$",
   [("$y = 2x$", "Divide fully: the quotient is $2x + 1$, not $2x$."),
    ("$y = 2x + 3$", "The $3$ is the coefficient in the numerator. Divide to find the quotient."),
    ("$x = -1$", "This is the vertical asymptote, not an oblique one.")],
   [S("Divide", math=r"2x^2 + 3x - 1 = (x + 1)(2x + 1) - 2"), S("Rewrite", math=r"y = 2x + 1 - \frac{2}{x + 1}"), S("Asymptote", math=r"y = 2x + 1")],
   "Functions and graphs", "Application", "Divide the numerator by x + 1.")
_q(r"Find the range of $f(x) = x^2 - 4x + 7$ for $x \in \mathbb{R}$.",
   r"$f(x) \geq 3$",
   [(r"$f(x) \geq 7$", r"$7$ is $f(0)$, not the minimum value."),
    (r"$f(x) \geq -3$", r"Completing the square gives $(x - 2)^2 + 3$: the constant is $7 - 4 = +3$."),
    (r"$f(x) \in \mathbb{R}$", "The graph is a parabola with a minimum, so the range is bounded below.")],
   [S("Complete the square", math=r"f(x) = (x - 2)^2 + 3"), S("Minimum", text=r"$(x - 2)^2 \geq 0$, so $f(x) \geq 3$.")],
   "Functions and graphs", "Calculation", "Complete the square to find the minimum value.")

# ---- Identities (5)
_q(r"Find the exact value of $\sin 75^\circ$.",
   r"$\dfrac{\sqrt{6} + \sqrt{2}}{4}$",
   [(r"$\dfrac{\sqrt{6} - \sqrt{2}}{4}$", r"This is $\sin 15^\circ$. For $\sin(45^\circ + 30^\circ)$ both terms are added."),
    (r"$\dfrac{\sqrt{3} + 1}{4}$", r"This is about $0.68$, but $\sin 75^\circ = 0.966$. The factor $\sqrt{2}$ is missing."),
    (r"$\dfrac{\sqrt{3} + 1}{2}$", r"This is greater than 1, so it cannot be a sine value.")],
   [S("Compound angle", math=r"\sin(45^\circ + 30^\circ) = \sin 45^\circ\cos 30^\circ + \cos 45^\circ\sin 30^\circ"), S("Evaluate", math=r"= \frac{\sqrt{2}}{2}\cdot\frac{\sqrt{3}}{2} + \frac{\sqrt{2}}{2}\cdot\frac{1}{2} = \frac{\sqrt{6} + \sqrt{2}}{4}")],
   "Identities", "Calculation", "Write 75° as 45° + 30° and use sin(A + B).")
_q(r"Given that $\sin\theta = \dfrac{3}{5}$, find $\cos 2\theta$.",
   r"$\dfrac{7}{25}$",
   [(r"$-\dfrac{7}{25}$", r"$\cos 2\theta = 1 - 2\sin^2\theta$, not $2\sin^2\theta - 1$."),
    (r"$\dfrac{18}{25}$", r"This is $2\sin^2\theta$ only. $\cos 2\theta = 1 - 2\sin^2\theta$."),
    (r"$\dfrac{24}{25}$", r"This is $\sin 2\theta = 2\sin\theta\cos\theta$, not $\cos 2\theta$.")],
   [S("Use $\\cos 2\\theta = 1 - 2\\sin^2\\theta$", math=r"1 - 2\left(\tfrac{9}{25}\right) = \tfrac{25 - 18}{25} = \tfrac{7}{25}")],
   "Identities", "Calculation", "Choose the double-angle formula that uses sin θ only.")
_q(r"Write $3\cos\theta + 4\sin\theta$ in the form $R\cos(\theta - \alpha)$ with $R > 0$ and $0^\circ < \alpha < 90^\circ$.",
   r"$R = 5$, $\alpha = 53.1^\circ$",
   [(r"$R = 7$, $\alpha = 53.1^\circ$", r"$R = \sqrt{3^2 + 4^2}$, not $3 + 4$."),
    (r"$R = 5$, $\alpha = 36.9^\circ$", r"$\tan\alpha = \frac{4}{3}$ (the $\sin$ coefficient over the $\cos$ coefficient), not $\frac{3}{4}$."),
    (r"$R = 12$, $\alpha = 53.1^\circ$", r"$R^2 = 3^2 + 4^2 = 25$. $12$ is the product of the coefficients.")],
   [S("Expand", math=r"R\cos\theta\cos\alpha + R\sin\theta\sin\alpha"), S("Match coefficients", math=r"R\cos\alpha = 3, \quad R\sin\alpha = 4"), S("Solve", math=r"R = 5, \quad \tan\alpha = \tfrac{4}{3} \Rightarrow \alpha = 53.1^\circ")],
   "Identities", "Calculation", "Expand R cos(θ − α) and compare the coefficients of cos θ and sin θ.")
_q(r"How many solutions has $2\cos^2\theta + \sin\theta = 1$ for $0 \leq \theta < 2\pi$?",
   "$3$",
   [("$2$", r"You found $\sin\theta = -\frac{1}{2}$ (two solutions) but missed $\sin\theta = 1$."),
    ("$4$", r"$\sin\theta = 1$ gives one solution ($\theta = \frac{\pi}{2}$), not two."),
    ("$6$", "There are only two possible values of $\\sin\\theta$.")],
   [S("Replace $\\cos^2\\theta$", math=r"2(1 - \sin^2\theta) + \sin\theta = 1 \Rightarrow 2\sin^2\theta - \sin\theta - 1 = 0"), S("Factorise", math=r"(2\sin\theta + 1)(\sin\theta - 1) = 0"),
    S("Count", text=r"$\sin\theta = 1$: one solution. $\sin\theta = -\frac{1}{2}$: two solutions ($\frac{7\pi}{6}$, $\frac{11\pi}{6}$). Total 3.")],
   "Identities", "Reasoning", "Change cos² into sin² and solve the quadratic in sin θ.")
_q(r"Express $\sin 2\theta$ in terms of $t = \tan\theta$.",
   r"$\dfrac{2t}{1 + t^2}$",
   [(r"$\dfrac{2t}{1 - t^2}$", r"This is $\tan 2\theta$. The denominator for $\sin 2\theta$ is $1 + t^2$."),
    (r"$\dfrac{2t}{1 + t}$", "The denominator is $1 + t^2$, not $1 + t$."),
    (r"$\dfrac{1 - t^2}{1 + t^2}$", r"This is $\cos 2\theta$.")],
   [S("Write $\\sin 2\\theta$", math=r"2\sin\theta\cos\theta = \frac{2\sin\theta\cos\theta}{\sin^2\theta + \cos^2\theta}"), S("Divide top and bottom by $\\cos^2\\theta$", math=r"\frac{2t}{t^2 + 1}")],
   "Identities", "Reasoning", "Write sin²θ + cos²θ = 1 in the denominator, then divide by cos²θ.")

# ---- Conic sections (4)
_q(r"The circle $x^2 + y^2 - 6x + 4y - 12 = 0$ has centre $C$ and radius $r$. Find them.",
   r"$C = (3, -2)$, $r = 5$",
   [(r"$C = (-3, 2)$, $r = 5$", "The centre has the **opposite** signs to the coefficients of $x$ and $y$ divided by 2: $(3, -2)$."),
    (r"$C = (3, -2)$, $r = 25$", r"$25$ is $r^2$. Take the square root."),
    (r"$C = (3, -2)$, $r = 1$", r"$r^2 = 9 + 4 - (-12) = 25$: subtract the constant, which is negative.")],
   [S("Complete the square", math=r"(x - 3)^2 + (y + 2)^2 = 12 + 9 + 4 = 25"), S("Read off", math=r"C = (3, -2), \quad r = 5")],
   "Conic sections", "Calculation", "Complete the square in x and in y.")
_q(r"Find the focus of the parabola $y^2 = 12x$.",
   "$(3, 0)$",
   [("$(12, 0)$", r"$y^2 = 4ax$ gives $4a = 12$, so $a = 3$. The focus is $(a, 0)$."),
    ("$(6, 0)$", r"$a = 3$, not $\frac{12}{2} = 6$."),
    ("$(0, 3)$", r"The parabola opens along the $x$-axis, so the focus is on the $x$-axis.")],
   [S("Compare with $y^2 = 4ax$", math=r"4a = 12 \Rightarrow a = 3"), S("Focus", math=r"(a, 0) = (3, 0)")],
   "Conic sections", "Recall", "Compare with y² = 4ax.")
_q(r"The ellipse $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$ has foci at:",
   r"$(\pm 4, 0)$",
   [(r"$(\pm\sqrt{34}, 0)$", r"$\sqrt{25 + 9}$ is for a hyperbola. For an ellipse $c^2 = a^2 - b^2$."),
    (r"$(\pm 5, 0)$", "$5$ is the semi-major axis $a$, where the ellipse meets the axis."),
    (r"$(0, \pm 4)$", "The major axis is along the $x$-axis ($25 > 9$), so the foci are on the $x$-axis.")],
   [S("Use $c^2 = a^2 - b^2$", math=r"c^2 = 25 - 9 = 16 \Rightarrow c = 4"), S("Foci on the major axis", math=r"(\pm 4, 0)")],
   "Conic sections", "Calculation", "For an ellipse c² = a² − b².")
_q(r"Find the equations of the asymptotes of $\dfrac{x^2}{9} - \dfrac{y^2}{16} = 1$.",
   r"$y = \pm\dfrac{4}{3}x$",
   [(r"$y = \pm\dfrac{3}{4}x$", r"The slope is $\frac{b}{a} = \frac{4}{3}$, not $\frac{a}{b}$."),
    (r"$y = \pm\dfrac{16}{9}x$", "You used $b^2$ and $a^2$. The slopes use $a$ and $b$, not their squares."),
    (r"$y = \pm\dfrac{9}{16}x$", "You used $a^2$ over $b^2$. Take square roots and invert: $\\frac{b}{a}$.")],
   [S("For large $x$, $y$", math=r"\frac{x^2}{9} - \frac{y^2}{16} = 0"), S("Solve", math=r"y = \pm\frac{4}{3}x")],
   "Conic sections", "Calculation", "Set the right-hand side to 0 to find the asymptotes.")

# ---- Differentiation (5)
_q(r"Differentiate $y = x^2 e^{3x}$.",
   r"$xe^{3x}(2 + 3x)$",
   [(r"$2xe^{3x}$", "You differentiated $x^2$ only. A product needs the product rule."),
    (r"$3x^2e^{3x}$", r"You differentiated $e^{3x}$ only. Add the term from $x^2$."),
    (r"$e^{3x}(2x + 3)$", r"The second term is $x^2 \times 3e^{3x} = 3x^2e^{3x}$, not $3e^{3x}$.")],
   [S("Product rule", math=r"\frac{dy}{dx} = 2xe^{3x} + x^2\cdot 3e^{3x}"), S("Factorise", math=r"= xe^{3x}(2 + 3x)")],
   "Differentiation", "Calculation", "Use the product rule with u = x² and v = e^(3x).")
_q(r"Differentiate $y = \dfrac{x^2 + 1}{x - 1}$.",
   r"$\dfrac{x^2 - 2x - 1}{(x - 1)^2}$",
   [(r"$\dfrac{1 + 2x - x^2}{(x - 1)^2}$", r"The numerator is $u'v - uv'$, not $uv' - u'v$: the signs are reversed."),
    (r"$\dfrac{3x^2 - 2x + 1}{(x - 1)^2}$", r"The quotient rule subtracts: $u'v - uv'$."),
    (r"$\dfrac{x^2 - 2x - 1}{x - 1}$", "The denominator is squared: $(x - 1)^2$.")],
   [S("Quotient rule", math=r"\frac{u'v - uv'}{v^2} = \frac{2x(x - 1) - (x^2 + 1)}{(x - 1)^2}"), S("Simplify", math=r"= \frac{x^2 - 2x - 1}{(x - 1)^2}")],
   "Differentiation", "Calculation", "Use the quotient rule: derivative of top times bottom, minus top times derivative of bottom.")
_q(r"A curve has equation $x^2 + xy + y^2 = 7$. Find $\dfrac{dy}{dx}$ at the point $(1, 2)$.",
   r"$-\dfrac{4}{5}$",
   [(r"$\dfrac{4}{5}$", "Check the sign: $\\frac{dy}{dx} = -\\frac{2x + y}{x + 2y}$."),
    (r"$-\dfrac{5}{4}$", "You inverted the fraction."),
    ("$-1$", r"You forgot the product rule on $xy$, which gives $y + x\frac{dy}{dx}$.")],
   [S("Differentiate implicitly", math=r"2x + y + x\frac{dy}{dx} + 2y\frac{dy}{dx} = 0"), S("Solve for the gradient", math=r"\frac{dy}{dx} = -\frac{2x + y}{x + 2y}"), S("At $(1, 2)$", math=r"-\frac{4}{5}")],
   "Differentiation", "Calculation", "Differentiate each term with respect to x; remember the product rule for xy.")
_q(r"A curve has parametric equations $x = t^2 + 1$, $y = t^3$. Find $\dfrac{dy}{dx}$ when $t = 2$.",
   "$3$",
   [("$12$", r"This is $\frac{dy}{dt}$ only. Divide by $\frac{dx}{dt} = 4$."),
    (r"$\dfrac{1}{3}$", r"You inverted: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$."),
    ("$6$", r"$\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2}$. At $t = 2$ this is $3$, not $3t$.")],
   [S("Derivatives", math=r"\frac{dx}{dt} = 2t, \quad \frac{dy}{dt} = 3t^2"), S("Divide", math=r"\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2} = 3 \text{ at } t = 2")],
   "Differentiation", "Calculation", "Use dy/dx = (dy/dt) divided by (dx/dt).")
_q(r"Find the gradient of $y = 2^x$ at $x = 3$.",
   r"$8\ln 2$",
   [("$8$", r"The derivative of $2^x$ is $2^x\ln 2$: the factor $\ln 2$ is missing."),
    ("$12$", r"This is $x\cdot 2^{x-1}$, the rule for $x^n$, not for $a^x$."),
    ("$24$", r"This is $3 \times 2^3$. The derivative of $2^x$ is not found with the power rule.")],
   [S("Differentiate", math=r"\frac{d}{dx}(2^x) = 2^x\ln 2"), S("At $x = 3$", math=r"8\ln 2")],
   "Differentiation", "Recall", "What is the derivative of a^x?")

# ---- Series (3)
_q(r"Find the coefficient of $x^3$ in the Maclaurin series of $\ln(1 + 2x)$.",
   r"$\dfrac{8}{3}$",
   [(r"$\dfrac{1}{3}$", r"The series is $\ln(1 + u) = u - \frac{u^2}{2} + \frac{u^3}{3} - \ldots$ with $u = 2x$: include $2^3$."),
    ("$8$", r"You forgot to divide by 3: $\frac{u^3}{3}$."),
    (r"$\dfrac{2}{3}$", r"$u^3 = (2x)^3 = 8x^3$, not $2x^3$.")],
   [S("Use the series for $\\ln(1 + u)$", math=r"\ln(1 + u) = u - \tfrac{u^2}{2} + \tfrac{u^3}{3} - \ldots"), S("Put $u = 2x$", math=r"\tfrac{(2x)^3}{3} = \tfrac{8}{3}x^3")],
   "Series", "Calculation", "Replace u by 2x in the series for ln(1 + u).")
_q(r"Find the coefficient of $x^3$ in the Maclaurin series of $e^x\sin x$.",
   r"$\dfrac{1}{3}$",
   [(r"$-\dfrac{1}{6}$", r"This is only the $x^3$ term of $\sin x$. Add the contribution $\frac{x^2}{2}\cdot x$ from $e^x$."),
    (r"$\dfrac{1}{2}$", r"This is only $\frac{x^2}{2}\cdot x$. Add $-\frac{1}{6}$ from $\sin x$."),
    (r"$\dfrac{2}{3}$", r"$-\frac{1}{6} + \frac{1}{2} = \frac{1}{3}$, not $\frac{2}{3}$.")],
   [S("Multiply the series", math=r"(1 + x + \tfrac{x^2}{2} + \ldots)(x - \tfrac{x^3}{6} + \ldots)"), S("Collect $x^3$", math=r"\tfrac{1}{2} - \tfrac{1}{6} = \tfrac{1}{3}")],
   "Series", "Calculation", "Which pairs of terms multiply to give x³?")
_q(r"Find the coefficient of $x^4$ in the Maclaurin series of $\cos 2x$.",
   r"$\dfrac{2}{3}$",
   [(r"$\dfrac{1}{24}$", r"This is the coefficient for $\cos x$. For $\cos 2x$ replace $x$ by $2x$."),
    (r"$\dfrac{1}{6}$", r"$2^4 = 16$, not $4$: $\frac{16}{24} = \frac{2}{3}$."),
    (r"$\dfrac{4}{3}$", r"$\frac{16}{24} = \frac{2}{3}$, not $\frac{16}{12}$.")],
   [S("Series for $\\cos u$", math=r"\cos u = 1 - \tfrac{u^2}{2} + \tfrac{u^4}{24} - \ldots"), S("Put $u = 2x$", math=r"\tfrac{16x^4}{24} = \tfrac{2}{3}x^4")],
   "Series", "Calculation", "Use the series for cos u with u = 2x.")

# ---- Integration (5)
_q(r"Find $\displaystyle\int x\cos x\,dx$.",
   r"$x\sin x + \cos x + c$",
   [(r"$x\sin x - \cos x + c$", r"$\int\sin x\,dx = -\cos x$, so subtracting it gives $+\cos x$."),
    (r"$\dfrac{x^2}{2}\sin x + c$", "You integrated each factor separately. Use integration by parts."),
    (r"$\sin x + x\cos x + c$", "This is almost the derivative of $x\\sin x$. Differentiating it does not give $x\\cos x$.")],
   [S("Parts with $u = x$, $v' = \\cos x$", math=r"\int x\cos x\,dx = x\sin x - \int\sin x\,dx"), S("Integrate", math=r"= x\sin x + \cos x + c")],
   "Integration", "Calculation", "Use integration by parts with u = x.")
_q(r"Evaluate $\displaystyle\int_0^1 2x(x^2 + 1)^3\,dx$.",
   r"$\dfrac{15}{4}$",
   [("$4$", "You forgot to subtract the value at the lower limit: $\\frac{16}{4} - \\frac{1}{4}$."),
    ("$15$", r"You forgot the $\frac{1}{4}$ from integrating $u^3$."),
    (r"$\dfrac{15}{2}$", r"$\int u^3\,du = \frac{u^4}{4}$, not $\frac{u^4}{2}$.")],
   [S("Substitute $u = x^2 + 1$, $du = 2x\\,dx$", math=r"\int_1^2 u^3\,du"), S("Integrate", math=r"\left[\tfrac{u^4}{4}\right]_1^2 = \tfrac{16 - 1}{4} = \tfrac{15}{4}")],
   "Integration", "Calculation", "Let u = x² + 1. Remember to change the limits.")
_q(r"Evaluate $\displaystyle\int_2^3 \frac{1}{(x - 1)(x + 1)}\,dx$.",
   r"$\dfrac{1}{2}\ln\dfrac{3}{2}$",
   [(r"$\ln\dfrac{3}{2}$", r"The partial fractions are $\frac{1}{2}\left(\frac{1}{x-1} - \frac{1}{x+1}\right)$: the factor $\frac{1}{2}$ is missing."),
    (r"$\dfrac{1}{2}\ln\dfrac{2}{3}$", "The order is reversed: the result must be positive because the integrand is positive."),
    (r"$\dfrac{1}{2}\ln 3$", r"This is $-\frac{1}{2}\ln\frac{1}{3}$, the lower-limit term alone. Both limits are needed: upper minus lower.")],
   [S("Partial fractions", math=r"\frac{1}{(x - 1)(x + 1)} = \frac{1}{2}\left(\frac{1}{x - 1} - \frac{1}{x + 1}\right)"),
    S("Integrate", math=r"\tfrac{1}{2}\left[\ln\frac{x - 1}{x + 1}\right]_2^3 = \tfrac{1}{2}\left(\ln\tfrac{1}{2} - \ln\tfrac{1}{3}\right) = \tfrac{1}{2}\ln\tfrac{3}{2}")],
   "Integration", "Calculation", "Split into partial fractions first.")
_q(r"The curve $y = \sqrt{x}$, $0 \leq x \leq 4$, is rotated through $2\pi$ about the $x$-axis. Find the volume.",
   r"$8\pi$",
   [(r"$\dfrac{16\pi}{3}$", r"You used $\pi\int y\,dx$. The volume needs $\pi\int y^2\,dx$."),
    ("$8$", "You left out the factor $\\pi$."),
    (r"$16\pi$", r"$\int_0^4 x\,dx = \frac{16}{2} = 8$, not 16.")],
   [S("Volume formula", math=r"V = \pi\int_0^4 y^2\,dx = \pi\int_0^4 x\,dx"), S("Integrate", math=r"\pi\left[\tfrac{x^2}{2}\right]_0^4 = 8\pi")],
   "Integration", "Application", "Volume of revolution: pi times the integral of y squared.")
_q(r"Evaluate $\displaystyle\int_0^{\ln 2} e^{2x}\,dx$.",
   r"$\dfrac{3}{2}$",
   [("$3$", r"You forgot the $\frac{1}{2}$ from $\int e^{2x}\,dx = \frac{1}{2}e^{2x}$."),
    (r"$\dfrac{1}{2}$", r"$e^{2\ln 2} = 4$, not $2$."),
    (r"$\dfrac{5}{2}$", "You added the value at the lower limit instead of subtracting.")],
   [S("Integrate", math=r"\left[\tfrac{1}{2}e^{2x}\right]_0^{\ln 2}"), S("Evaluate", math=r"\tfrac{1}{2}(e^{2\ln 2} - 1) = \tfrac{1}{2}(4 - 1) = \tfrac{3}{2}")],
   "Integration", "Calculation", "Integrate e^(2x), then use e^(2 ln 2) = 4.")

# ---- Differential equations (3)
_q(r"Given $\dfrac{dy}{dx} = 3y$ and $y = 2$ when $x = 0$, find $y$ when $x = 1$.",
   r"$2e^3$",
   [(r"$e^3$", "You ignored the initial condition: $y = Ae^{3x}$ with $A = 2$."),
    (r"$2e$", "The exponent is $3x$, so at $x = 1$ it is $e^3$."),
    (r"$3e^2$", r"The solution is $y = 2e^{3x}$: the constants are in the wrong places.")],
   [S("Separate and integrate", math=r"\ln y = 3x + c"), S("Initial condition", math=r"y = 2e^{3x}"), S("At $x = 1$", math=r"y = 2e^3")],
   "Differential equations", "Calculation", "Separate the variables and use y = 2 at x = 0.")
_q(r"$\dfrac{dy}{dx} + 2y = 4$ with $y = 0$ when $x = 0$. What happens to $y$ as $x \to \infty$?",
   r"$y \to 2$",
   [(r"$y \to 4$", r"The steady value is where $\frac{dy}{dx} = 0$: $2y = 4$, so $y = 2$."),
    (r"$y \to 0$", r"The solution is $y = 2 - 2e^{-2x}$. The exponential term tends to 0, leaving $2$."),
    (r"$y \to \infty$", "The exponential $e^{-2x}$ decays, so $y$ approaches a limit.")],
   [S("Solve", math=r"y = 2 + Ae^{-2x}, \quad y(0) = 0 \Rightarrow A = -2"), S("Limit", math=r"y = 2 - 2e^{-2x} \to 2")],
   "Differential equations", "Reasoning", "Where does dy/dx = 0?")
_q(r"Given $\dfrac{dy}{dx} = \dfrac{x}{y}$ and $y = 2$ when $x = 0$, find $y$ when $x = 3$ ($y > 0$).",
   r"$\sqrt{13}$",
   [(r"$13$", "You forgot the square root: $y^2 = 13$."),
    (r"$\sqrt{11}$", r"The constant is $4$ (from $y^2 = x^2 + c$ with $y = 2$), not $2$."),
    (r"$\sqrt{5}$", r"$y^2 = x^2 + 4$: the sign of the constant is $+$.")],
   [S("Separate", math=r"\int y\,dy = \int x\,dx \Rightarrow \tfrac{y^2}{2} = \tfrac{x^2}{2} + c"), S("Initial condition", math=r"y^2 = x^2 + 4"), S("At $x = 3$", math=r"y = \sqrt{13}")],
   "Differential equations", "Calculation", "Separate the variables: y dy = x dx.")

# ---- Vectors in space (4)
_q(r"$A$ is $(1, -1, 2)$ and $B$ is $(3, -4, 8)$. Find the distance $AB$.",
   "$7$",
   [("$49$", "You forgot the square root."),
    ("$5$", r"You added the components of $\overrightarrow{AB} = (2, -3, 6)$ with their signs."),
    ("$11$", r"You added the sizes of the components, $2 + 3 + 6$.")],
   [S("Vector", math=r"\overrightarrow{AB} = (2, -3, 6)"), S("Magnitude", math=r"\sqrt{4 + 9 + 36} = 7")],
   "Vectors in space", "Calculation", "Find AB, then its magnitude.")
_q(r"Find the angle between $\mathbf{a} = (2, 1, -2)$ and $\mathbf{b} = (1, -4, 8)$.",
   r"$131.8^\circ$",
   [(r"$48.2^\circ$", r"$\cos\theta = -\frac{2}{3}$ is negative, so the angle is **obtuse**: $180^\circ - 48.2^\circ$."),
    (r"$41.8^\circ$", r"This is $90^\circ - 48.2^\circ$. Use cosine, not sine, and keep the sign."),
    (r"$138.2^\circ$", "Check the arithmetic: $\\cos^{-1}(-\\frac{2}{3}) = 131.8^\\circ$.")],
   [S("Scalar product", math=r"2 - 4 - 16 = -18"), S("Magnitudes", math=r"|\mathbf{a}| = 3, \quad |\mathbf{b}| = 9"), S("Angle", math=r"\cos\theta = \frac{-18}{27} = -\frac{2}{3} \Rightarrow \theta = 131.8^\circ")],
   "Vectors in space", "Calculation", "Do not take the modulus: the angle between two vectors can be obtuse.")
_q(r"Find the cartesian equation of the plane through $(1, 2, 3)$ with normal vector $2\mathbf{i} - \mathbf{j} + 2\mathbf{k}$.",
   r"$2x - y + 2z = 6$",
   [(r"$2x - y + 2z = 10$", r"$d = 2(1) - (2) + 2(3) = 6$: the $y$ term is $-2$, not $+2$."),
    (r"$2x - y + 2z = -6$", "Check the sign of $d$: it is positive."),
    (r"$x + 2y + 3z = 6$", "You used the point as the normal. The coefficients come from the normal vector.")],
   [S("Coefficients from the normal", math=r"2x - y + 2z = d"), S("Substitute the point", math=r"d = 2 - 2 + 6 = 6")],
   "Vectors in space", "Calculation", "The coefficients are the components of the normal.")
_q(r"Find the distance from $(1, 0, 0)$ to the plane $4x - 4y + 7z = -8$.",
   r"$\dfrac{4}{3}$",
   [("$12$", r"You forgot to divide by $|\mathbf{n}| = 9$."),
    (r"$\dfrac{4}{9}$", "You used $d = 8$: the constant is $-8$, so the numerator is $|4 + 8| = 12$."),
    (r"$\dfrac{4}{27}$", r"You divided by $|\mathbf{n}|^2 = 81$. Divide by $|\mathbf{n}| = 9$.")],
   [S("Value at the point", math=r"|4(1) - 0 + 0 + 8| = 12"), S("Magnitude of normal", math=r"\sqrt{16 + 16 + 49} = 9"), S("Distance", math=r"\frac{12}{9} = \frac{4}{3}")],
   "Vectors in space", "Calculation", "Use |n.p - d| divided by |n|; watch the sign of d.")

# ---------------------------------------------------------------- Paper 2 practice paper A: 27 auto-markable parts in 6 questions
# Each part repeats the shared context so that it stands alone.
_PQ2_POS = [3, 0, 2, 1, 3, 1, 0]
P2_QUESTIONS = []
_mc_count = [0]


def _p2mc(prompt, right, wrongs, steps, concept, skill, hint):
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(_PQ2_POS[_mc_count[0]], C(right, correct=True))
    _mc_count[0] += 1
    P2_QUESTIONS.append(MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint))


Q1 = r"$f(x) = \dfrac{3x + 5}{(x + 1)(x + 2)}$ and $f(x) = \dfrac{A}{x + 1} + \dfrac{B}{x + 2}$. "
Q2 = r"$g(\theta) = 3\sin\theta + 4\cos\theta$. "
Q3 = r"A curve has parametric equations $x = t^2$, $y = t^3 - 3t$. "
Q4 = r"The region $R$ is bounded by the curve $y = 2x - x^2$ and the $x$-axis. "
Q5 = r"$\dfrac{dy}{dx} = y\sin x$, with $y = 1$ when $x = 0$. "
Q6 = r"The line $l_1$ has equation $\mathbf{r} = (1, 2, 3) + \lambda(1, -1, 2)$ and the line $l_2$ has equation $\mathbf{r} = (4, 0, 2) + \mu(-1, 0, 5)$. They intersect. "

# ---- Question 1: partial fractions, series and integration
P2_QUESTIONS.append(NUM("Question 1(a). " + Q1 + "Find $A$.", 2,
    steps=[S("Clear the fractions", math=r"3x + 5 = A(x + 2) + B(x + 1)"), S("Put $x = -1$", math=r"2 = A")],
    concept="Algebra", skill="Calculation", hint="Substitute x = -1 into 3x + 5 = A(x + 2) + B(x + 1)."))
P2_QUESTIONS.append(NUM("Question 1(b). " + Q1 + "Find $B$.", 1,
    steps=[S("Put $x = -2$", math=r"-1 = -B \;\Rightarrow\; B = 1")],
    concept="Algebra", skill="Calculation", hint="Substitute x = -2 into 3x + 5 = A(x + 2) + B(x + 1)."))
P2_QUESTIONS.append(NUM("Question 1(c). " + Q1 + r"Find the coefficient of $x$ in the expansion of $f(x)$ in ascending powers of $x$, for $|x| < 1$.", -2.25, tolerance=0.001,
    steps=[S("Write $f$ with $A = 2$, $B = 1$", math=r"f(x) = 2(1 + x)^{-1} + \tfrac{1}{2}\left(1 + \tfrac{x}{2}\right)^{-1}"),
           S("Expand each", math=r"2(1 - x + x^2 - \ldots) + \tfrac{1}{2}\left(1 - \tfrac{x}{2} + \tfrac{x^2}{4} - \ldots\right)"),
           S("Coefficient of $x$", math=r"-2 - \tfrac{1}{4} = -\tfrac{9}{4} = -2.25")],
    concept="Algebra", skill="Calculation", hint="Write each partial fraction as (1 + something)^(-1) and use the binomial expansion."))
P2_QUESTIONS.append(NUM("Question 1(d). " + Q1 + r"Find the coefficient of $x^2$ in the expansion of $f(x)$ in ascending powers of $x$, for $|x| < 1$.", 2.125, tolerance=0.001,
    steps=[S("From the same expansion", math=r"2(1) + \tfrac{1}{2}\left(\tfrac{1}{4}\right) = 2 + \tfrac{1}{8} = \tfrac{17}{8} = 2.125")],
    concept="Series", skill="Calculation", hint="Use the x² terms of both expansions: 2 × 1 and (1/2) × (1/4)."))
_p2mc("Question 1(e). " + Q1 + r"Find $\displaystyle\int_0^1 f(x)\,dx$ (exact value).", r"$\ln 6$",
    [(r"$\ln 12$", r"This is the value at the upper limit only, $2\ln 2 + \ln 3$. Subtract the lower-limit value $\ln 2$."),
     (r"$\ln\dfrac{9}{2}$", "The constants $A$ and $B$ are the wrong way round."),
     (r"$\ln\dfrac{8}{3}$", r"A sign slip: $2\ln 2 - \ln\frac{3}{2}$. Both terms are added.")],
    [S("Integrate", math=r"\int_0^1 f\,dx = \left[2\ln(x + 1) + \ln(x + 2)\right]_0^1"), S("Evaluate", math=r"(2\ln 2 + \ln 3) - (0 + \ln 2) = \ln 2 + \ln 3 = \ln 6")],
    "Integration", "Calculation", "Integrate each partial fraction to a logarithm.")

# ---- Question 2: harmonic form
_p2mc("Question 2(a). " + Q2 + r"Write $g(\theta)$ in the form $R\sin(\theta + \alpha)$, with $R > 0$ and $0^\circ < \alpha < 90^\circ$.", r"$R = 5$, $\alpha = 53.1^\circ$",
    [(r"$R = 7$, $\alpha = 53.1^\circ$", r"$R = \sqrt{3^2 + 4^2} = 5$, not $3 + 4$."),
     (r"$R = 5$, $\alpha = 36.9^\circ$", r"For $R\sin(\theta + \alpha)$, $R\cos\alpha = 3$ and $R\sin\alpha = 4$, so $\tan\alpha = \frac{4}{3}$, not $\frac{3}{4}$."),
     (r"$R = 12$, $\alpha = 53.1^\circ$", r"$12$ is the product $3 \times 4$. $R^2 = 3^2 + 4^2$.")],
    [S("Expand", math=r"R\sin\theta\cos\alpha + R\cos\theta\sin\alpha"), S("Match", math=r"R\cos\alpha = 3, \quad R\sin\alpha = 4"), S("Solve", math=r"R = 5, \quad \alpha = 53.1^\circ")],
    "Identities", "Calculation", "Expand R sin(θ + α) and compare coefficients of sin θ and cos θ.")
P2_QUESTIONS.append(NUM("Question 2(b). " + Q2 + "Find the maximum value of $g(\\theta)$.", 5,
    steps=[S("Maximum of $R\\sin(\\theta + \\alpha)$ is $R$", math=r"R = 5")],
    concept="Identities", skill="Application", hint="The maximum of R sin(...) is R. What is R?"))
P2_QUESTIONS.append(NUM("Question 2(c). " + Q2 + r"Given $g(\theta) = 5\sin(\theta + 53.13^\circ)$, find the smallest positive $\theta$, in degrees to 1 decimal place, for which $g(\theta) = 5$.", 36.9, tolerance=0.1, unit="degrees",
    steps=[S("Set the sine to its maximum", math=r"\sin(\theta + 53.13^\circ) = 1"), S("Smallest solution", math=r"\theta + 53.13^\circ = 90^\circ \Rightarrow \theta = 36.9^\circ")],
    concept="Identities", skill="Application", hint="For which angle is the sine equal to 1?"))
P2_QUESTIONS.append(NUM("Question 2(d). " + Q2 + r"Given $g(\theta) = 5\sin(\theta + 53.13^\circ)$, solve $g(\theta) = 2$ for $0^\circ < \theta < 360^\circ$. Find the larger solution, in degrees to 1 decimal place.", 330.4, tolerance=0.1, unit="degrees",
    steps=[S("Solve", math=r"\sin(\theta + 53.13^\circ) = 0.4 \Rightarrow \theta + 53.13^\circ = 23.58^\circ, 156.42^\circ, 383.58^\circ, \ldots"),
           S("Keep $53.13^\\circ < \\theta + 53.13^\\circ < 413.13^\\circ$", math=r"156.42^\circ \text{ and } 383.58^\circ"), S("Subtract $53.13^\\circ$", math=r"\theta = 103.3^\circ \text{ or } 330.4^\circ")],
    concept="Identities", skill="Reasoning", hint="Find all angles with sine 0.4 in the correct range for θ + 53.13°, then subtract 53.13°."))

# ---- Question 3: parametric differentiation
P2_QUESTIONS.append(NUM("Question 3(a). " + Q3 + r"Find the $y$-coordinate of the point where $t = 2$.", 2,
    steps=[S("Substitute", math=r"y = 8 - 6 = 2")],
    concept="Differentiation", skill="Calculation", hint="Put t = 2 into y = t³ − 3t."))
P2_QUESTIONS.append(NUM("Question 3(b). " + Q3 + r"Find $\dfrac{dy}{dx}$ when $t = 2$.", 2.25, tolerance=0.001,
    steps=[S("Differentiate", math=r"\frac{dy}{dt} = 3t^2 - 3, \quad \frac{dx}{dt} = 2t"), S("Divide at $t = 2$", math=r"\frac{9}{4} = 2.25")],
    concept="Differentiation", skill="Calculation", hint="Use dy/dx = (dy/dt) / (dx/dt)."))
_p2mc("Question 3(c). " + Q3 + r"Find the equation of the tangent at the point where $t = 2$, which is $(4, 2)$.", r"$9x - 4y = 28$",
    [(r"$4x + 9y = 34$", r"This is the **normal** (gradient $-\frac{4}{9}$), not the tangent."),
     (r"$9x - 4y = 2$", "The point $(4, 2)$ was used as $(2, 4)$: check the coordinates."),
     (r"$9x - y = 34$", r"You used $\frac{dy}{dt} = 9$ as the gradient. The gradient is $\frac{dy/dt}{dx/dt} = \frac{9}{4}$.")],
    [S("Gradient and point", math=r"m = \tfrac{9}{4}, \quad (4, 2)"), S("Equation", math=r"y - 2 = \tfrac{9}{4}(x - 4) \Rightarrow 9x - 4y = 28")],
    "Differentiation", "Application", "Use y - y1 = m(x - x1) with m = dy/dx at t = 2.")
P2_QUESTIONS.append(NUM("Question 3(d). " + Q3 + r"Find the positive value of $t$ at which the curve has a stationary point (where $\frac{dy}{dx} = 0$).", 1,
    steps=[S("Set the numerator to 0", math=r"3t^2 - 3 = 0"), S("Solve", math=r"t = 1 \ (t > 0)")],
    concept="Differentiation", skill="Calculation", hint="dy/dx = 0 when dy/dt = 0 (and dx/dt is not 0)."))
P2_QUESTIONS.append(NUM("Question 3(e). " + Q3 + r"Find the $y$-coordinate of the stationary point at $t = 1$.", -2,
    steps=[S("Substitute $t = 1$", math=r"y = 1 - 3 = -2")],
    concept="Differentiation", skill="Calculation", hint="Put t = 1 into y = t³ − 3t."))

# ---- Question 4: integration and volume
P2_QUESTIONS.append(NUM("Question 4(a). " + Q4 + "Find the area of $R$, to 2 decimal places.", 1.33, tolerance=0.01,
    steps=[S("Limits: $2x - x^2 = 0$", math=r"x = 0 \text{ and } x = 2"), S("Integrate", math=r"\int_0^2 (2x - x^2)\,dx = \left[x^2 - \tfrac{x^3}{3}\right]_0^2 = 4 - \tfrac{8}{3} = \tfrac{4}{3}")],
    concept="Integration", skill="Calculation", hint="Find where the curve meets the x-axis, then integrate between those points."))
P2_QUESTIONS.append(NUM("Question 4(b). " + Q4 + r"$R$ is rotated through $2\pi$ about the $x$-axis. The volume is $k\pi$. Find $k$ to 2 decimal places.", 1.07, tolerance=0.01,
    steps=[S("Volume formula", math=r"V = \pi\int_0^2 (2x - x^2)^2\,dx = \pi\int_0^2 (4x^2 - 4x^3 + x^4)\,dx"),
           S("Integrate", math=r"\pi\left[\tfrac{4x^3}{3} - x^4 + \tfrac{x^5}{5}\right]_0^2 = \pi\left(\tfrac{32}{3} - 16 + \tfrac{32}{5}\right)"), S("Simplify", math=r"k = \tfrac{16}{15} = 1.07")],
    concept="Integration", skill="Application", hint="Expand (2x − x²)² and integrate between 0 and 2."))
_p2mc("Question 4(c). " + r"Find the exact value of $\displaystyle\int_0^1 xe^{2x}\,dx$.", r"$\dfrac{e^2 + 1}{4}$",
    [(r"$\dfrac{e^2 - 1}{4}$", r"The first term is $\frac{xe^{2x}}{2} = \frac{e^2}{2}$ at the upper limit. Do not leave it out."),
     (r"$\dfrac{e^2}{2}$", r"This is the first term only. Subtract $\int\frac{e^{2x}}{2}\,dx = \frac{e^2 - 1}{4}$."),
     (r"$\dfrac{3e^2 - 1}{4}$", "You added the second part instead of subtracting it.")],
    [S("Parts with $u = x$, $v' = e^{2x}$", math=r"\left[\tfrac{xe^{2x}}{2}\right]_0^1 - \int_0^1 \tfrac{e^{2x}}{2}\,dx"), S("Evaluate", math=r"\tfrac{e^2}{2} - \tfrac{e^2 - 1}{4} = \tfrac{e^2 + 1}{4}")],
    "Integration", "Calculation", "Use integration by parts with u = x.")
P2_QUESTIONS.append(NUM("Question 4(d). " + r"Evaluate $\displaystyle\int_0^{\pi/2} x\cos x\,dx$, to 3 decimal places.", 0.571, tolerance=0.001,
    steps=[S("Parts", math=r"\left[x\sin x\right]_0^{\pi/2} - \int_0^{\pi/2}\sin x\,dx"), S("Evaluate", math=r"\tfrac{\pi}{2} - 1 = 0.571")],
    concept="Integration", skill="Calculation", hint="Integration by parts with u = x; radians."))

# ---- Question 5: differential equation and series
_p2mc("Question 5(a). " + Q5 + "Find $y$ in terms of $x$.", r"$y = e^{1 - \cos x}$",
    [(r"$y = e^{\cos x}$", r"$\int\sin x\,dx = -\cos x$, so $\ln y = -\cos x + c$."),
     (r"$y = e^{-\cos x}$", "You did not use the condition: at $x = 0$ this gives $y = e^{-1}$, not $1$."),
     (r"$y = e^{1 + \cos x}$", r"The constant is $c = 1$ from $\ln 1 = -1 + c$, and the term is $-\cos x$.")],
    [S("Separate", math=r"\int\frac{1}{y}\,dy = \int\sin x\,dx"), S("Integrate", math=r"\ln y = -\cos x + c"), S("Use $y = 1$ at $x = 0$", math=r"0 = -1 + c \Rightarrow c = 1, \quad y = e^{1 - \cos x}")],
    "Differential equations", "Calculation", "Separate the variables, integrate both sides, then use the condition.")
P2_QUESTIONS.append(NUM("Question 5(b). " + r"The solution of $\dfrac{dy}{dx} = y\sin x$ with $y = 1$ when $x = 0$ is $y = e^{1 - \cos x}$. Find $y$ when $x = \pi$, to 2 decimal places.", 7.39, tolerance=0.01,
    steps=[S("Substitute $x = \\pi$", math=r"y = e^{1 - (-1)} = e^2 = 7.39")],
    concept="Differential equations", skill="Calculation", hint="cos π = −1."))
P2_QUESTIONS.append(NUM("Question 5(c). " + r"Given $y = e^{1 - \cos x}$, find the coefficient of $x^2$ in the Maclaurin series of $y$.", 0.5, tolerance=0.001,
    steps=[S("Series for $1 - \\cos x$", math=r"1 - \cos x = \tfrac{x^2}{2} - \tfrac{x^4}{24} + \ldots"), S("Use $e^u = 1 + u + \\ldots$", math=r"y = 1 + \tfrac{x^2}{2} + \ldots, \quad \text{coefficient } \tfrac{1}{2}")],
    concept="Series", skill="Calculation", hint="Write 1 − cos x as a series, then use the series for e^u."))
P2_QUESTIONS.append(NUM("Question 5(d). " + r"Given $y = e^{1 - \cos x}$, find the coefficient of $x^4$ in the Maclaurin series of $y$, to 3 decimal places.", 0.083, tolerance=0.001,
    steps=[S("Let $u = \\frac{x^2}{2} - \\frac{x^4}{24}$", math=r"e^u = 1 + u + \tfrac{u^2}{2} + \ldots"), S("Collect $x^4$", math=r"-\tfrac{1}{24} + \tfrac{1}{2}\cdot\tfrac{1}{4} = -\tfrac{1}{24} + \tfrac{1}{8} = \tfrac{1}{12} = 0.083")],
    concept="Series", skill="Reasoning", hint="Two terms give x⁴: the x⁴ term of u, and (u²)/2 with u ≈ x²/2."))

# ---- Question 6: vectors
P2_QUESTIONS.append(NUM("Question 6(a). " + Q6 + r"Find the value of $\lambda$ at the point of intersection.", 2,
    steps=[S("Equate components", math=r"1 + \lambda = 4 - \mu, \quad 2 - \lambda = 0, \quad 3 + 2\lambda = 2 + 5\mu"), S("Solve", math=r"\lambda = 2, \ \mu = 1")],
    concept="Vectors in space", skill="Calculation", hint="The y components give 2 − λ = 0."))
_p2mc("Question 6(b). " + Q6 + "Find the point of intersection.", "$(3, 0, 7)$",
    [("$(4, 0, 2)$", r"This is the point of $l_2$ with $\mu = 0$: not on $l_1$."),
     ("$(1, 2, 3)$", r"This is the point of $l_1$ with $\lambda = 0$: not on $l_2$."),
     ("$(2, 1, 5)$", r"This is on $l_1$ ($\lambda = 1$) but not on $l_2$.")],
    [S("Substitute $\\lambda = 2$", math=r"(1 + 2,\ 2 - 2,\ 3 + 4) = (3, 0, 7)")],
    "Vectors in space", "Calculation", "Use the value of lambda from part (a).")
P2_QUESTIONS.append(NUM("Question 6(c). " + Q6 + r"Find the acute angle between $l_1$ and $l_2$, in degrees to 1 decimal place.", 43.9, tolerance=0.1, unit="degrees",
    steps=[S("Scalar product of the directions", math=r"(1, -1, 2)\cdot(-1, 0, 5) = -1 + 0 + 10 = 9"), S("Magnitudes", math=r"\sqrt{6}, \quad \sqrt{26}"),
           S("Angle", math=r"\cos\theta = \frac{9}{\sqrt{156}} \Rightarrow \theta = 43.9^\circ")],
    concept="Vectors in space", skill="Calculation", hint="Use the direction vectors and the scalar product."))
_p2mc("Question 6(d). " + Q6 + r"The plane $\Pi$ contains the point of intersection $(3, 0, 7)$ and is perpendicular to $l_1$. Find its equation.", r"$x - y + 2z = 17$",
    [(r"$x - y + 2z = 5$", r"You used the point $(1, 2, 3)$ of $l_1$. $\Pi$ must contain $(3, 0, 7)$."),
     (r"$-x + 5z = 32$", r"You used the direction of $l_2$ as the normal. The plane is perpendicular to $l_1$."),
     (r"$x + y + 2z = 17$", r"The normal is the direction of $l_1$, $(1, -1, 2)$: the sign of the $y$ coefficient is $-1$.")],
    [S("The normal is the direction of $l_1$", math=r"x - y + 2z = d"), S("Substitute $(3, 0, 7)$", math=r"d = 3 - 0 + 14 = 17")],
    "Vectors in space", "Application", "A plane perpendicular to a line has the line's direction as its normal.")
P2_QUESTIONS.append(NUM("Question 6(e). " + r"The plane $\Pi$ has equation $x - y + 2z = 17$. Find the distance from the origin to $\Pi$, to 2 decimal places.", 6.94, tolerance=0.01,
    steps=[S("Distance formula", math=r"\frac{|0 - 0 + 0 - 17|}{\sqrt{1 + 1 + 4}} = \frac{17}{\sqrt{6}} = 6.94")],
    concept="Vectors in space", skill="Calculation", hint="Distance from the origin is |d| divided by the magnitude of the normal."))

# ---------------------------------------------------------------- Sets
SETS = [
    practice_set(module=MOD, topic=TOP, title="Position vectors, magnitude and ratio in 3D",
                 lesson="pv-vectors-in-three-dimensions", questions=VEC_1),
    practice_set(module=MOD, topic=TOP, title="Scalar product, angles and projections",
                 lesson="pv-scalar-product-and-angles", questions=VEC_2),
    practice_set(module=MOD, topic=TOP, title="Vector equations of lines",
                 lesson="pv-vector-equations-of-lines", questions=VEC_3),
    practice_set(module=MOD, topic=TOP, title="Equations of planes",
                 lesson="pv-vector-equations-of-planes", questions=VEC_4),
    practice_set(module=MOD, topic=TOP, title="Intersections of lines and planes",
                 lesson="pv-intersections-of-lines-and-planes", questions=VEC_5),
    practice_set(module=MOD, topic=TOP, title="Distances from a point to a line and a plane",
                 lesson="pv-distances-point-to-line-and-plane", questions=VEC_6),
    practice_set(module="Examination", topic="Paper 1", title="Paper 1 technique: multiple-choice strategy",
                 lesson="pv-exam-paper-1-multiple-choice-strategy", questions=EXAM_1),
    practice_set(module="Examination", topic="Paper 2", title="Paper 2 technique: structured questions",
                 lesson="pv-exam-paper-2-structured-pure-questions", questions=EXAM_2),
    practice_set(module="Examination", topic="Paper 1", title="Paper 1 mock A",
                 lesson="pv-exam-paper-1-multiple-choice-strategy", mock=True, time_limit_minutes=90,
                 questions=P1_QUESTIONS),
    practice_set(module="Examination", topic="Paper 2", title="Paper 2 practice paper A",
                 lesson="pv-exam-paper-2-structured-pure-questions", mock=True, time_limit_minutes=150,
                 questions=P2_QUESTIONS),
]
