"""Further Mathematics (A Level, Upper Sixth): Vector Spaces & Linear Transformations, Numerical Methods,
Advanced Mechanics & Probability, and the Examination module (Paper 1 and Paper 2).

KKEVO draft content written against KKEVO's master curriculum blueprint (not a Board syllabus booklet).
A reviewer checks each lesson against the official GCE Board syllabus before publishing. Tables of
numerical-method iterations are computed by the helper functions below, so they are real outputs.
Practice paper timings are KKEVO practice settings, not official examination times.
"""

import math

from .dsl import *  # noqa: F403

COURSE = ("further-mathematics", "upper-sixth")

LESSONS = []


def _v(*c):
    """Column vector in LaTeX (no dollar signs)."""
    return r"\begin{pmatrix} " + r" \ ".join(str(x) for x in c) + r" \end{pmatrix}"


def _m(*rows):
    """Matrix in LaTeX (no dollar signs); each row is a list."""
    return r"\begin{pmatrix} " + r" \ ".join(" & ".join(str(x) for x in r) for r in rows) + r" \end{pmatrix}"


VS = "Vector Spaces & Linear Transformations"
NM = "Numerical Methods"
MP = "Advanced Mechanics & Probability"


# ================================================================ Vector spaces
LESSONS.append(lesson(
    module=VS, topic="Subspaces, independence, basis and dimension",
    title="Subspaces, linear independence, basis and dimension",
    slug="fmu2-subspaces-independence-basis-dimension",
    minutes=24,
    summary="Test whether a set is a subspace, decide whether vectors are linearly independent, and find a basis and the dimension of a space or subspace.",
    objectives=[
        "Use the subspace test (zero vector, closed under addition, closed under scalar multiples)",
        "Decide whether a set of vectors is linearly independent, and find the span of a set",
        "Find a basis for a subspace and state its dimension",
        "Write a vector in coordinates relative to a given basis",
    ],
    key_concepts=["Vector space", "Subspace", "Span", "Linear independence", "Basis", "Dimension", "Coordinates"],
    blocks=[
        H("Introduction"),
        T(r"In Lower Sixth you met vectors as arrows in two and three dimensions. A mobile-money agent in Douala who records three numbers each day (deposits, withdrawals, transfers) is also working with vectors: a list of three numbers that can be added and scaled. The ideas of a **vector space** let us treat arrows, lists of numbers, polynomials and matrices with one set of rules."),
        T("In this lesson you learn which sets behave like vector spaces, how to measure their size with **dimension**, and how to choose a **basis**, the smallest set of building blocks."),
        H("Vector spaces and subspaces"),
        D(r"A **vector space** over the real numbers is a set $V$ in which any two elements can be added and any element multiplied by a real number (a **scalar**), with the result always staying in $V$, and with the usual rules of arithmetic (commutative and associative addition, a zero vector $\mathbf{0}$, a negative $-\mathbf{v}$ for each $\mathbf{v}$, and the distributive laws). Examples: $\mathbb{R}^n$, the polynomials of degree at most $n$, and the $2 \times 2$ matrices.",
          title="Vector space"),
        D(r"A **subspace** $W$ of a vector space $V$ is a non-empty subset that is itself a vector space under the same addition and scalar multiplication. To test it you need only check three things:",
          title="The subspace test",
          formula=r"\text{(1) } \mathbf{0} \in W \qquad \text{(2) } \mathbf{u}, \mathbf{v} \in W \Rightarrow \mathbf{u} + \mathbf{v} \in W \qquad \text{(3) } \mathbf{u} \in W,\ \lambda \in \mathbb{R} \Rightarrow \lambda\mathbf{u} \in W",
          note="Checks (2) and (3) can be combined into one: for all u, v in W and all scalars a, b, the combination au + bv is in W."),
        EX("Worked example 1: two subsets of R cubed", intro=r"Which of these is a subspace of $\mathbb{R}^3$?  $P = \{(x, y, z) : x + 2y - z = 0\}$ and $Q = \{(x, y, z) : x + y + z = 1\}$.", steps=[
            S("Test $Q$ first: is the zero vector in it?", math=r"0 + 0 + 0 = 0 \neq 1", text="The zero vector is not in $Q$, so $Q$ is **not** a subspace. (A plane that misses the origin is never a subspace.)"),
            S(r"Test $P$: zero vector", math=r"0 + 2(0) - 0 = 0 \ \checkmark"),
            S(r"Test $P$: addition", text=r"If $\mathbf{u} = (x_1, y_1, z_1)$ and $\mathbf{v} = (x_2, y_2, z_2)$ are in $P$, then adding the two equations gives $(x_1 + x_2) + 2(y_1 + y_2) - (z_1 + z_2) = 0$, so $\mathbf{u} + \mathbf{v} \in P$."),
            S(r"Test $P$: scalar multiples", text=r"Multiplying $x_1 + 2y_1 - z_1 = 0$ by $\lambda$ gives $\lambda x_1 + 2\lambda y_1 - \lambda z_1 = 0$, so $\lambda\mathbf{u} \in P$. So $P$ is a subspace: a plane through the origin."),
        ]),
        MISTAKE("Skipping the zero vector", r"Every subspace contains $\mathbf{0}$. This is the quickest way to reject a set: a line or plane that does not pass through the origin, and any set defined by an equation such as $x + y = 1$, fails at once. But passing this test alone is not enough: the set $\{(x, y) : xy = 0\}$ contains $\mathbf{0}$ and still fails closure, because $(1, 0) + (0, 1) = (1, 1)$ is not in it."),
        H("Span and linear independence"),
        D(r"A **linear combination** of vectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ is any vector $a_1\mathbf{v}_1 + \dots + a_k\mathbf{v}_k$. Their **span** is the set of all linear combinations; it is always a subspace.", title="Span"),
        D(r"Vectors $\mathbf{v}_1, \dots, \mathbf{v}_k$ are **linearly independent** if the only solution of $a_1\mathbf{v}_1 + \dots + a_k\mathbf{v}_k = \mathbf{0}$ is $a_1 = \dots = a_k = 0$. If another solution exists they are **linearly dependent**: at least one vector is a combination of the others.",
          title="Linear independence"),
        EX("Worked example 2: testing independence", intro=r"Are $\mathbf{v}_1 = (1, 2, 3)$, $\mathbf{v}_2 = (2, 1, 0)$, $\mathbf{v}_3 = (4, 5, 6)$ linearly independent?", steps=[
            S("Write the equation", math=r"a(1, 2, 3) + b(2, 1, 0) + c(4, 5, 6) = (0, 0, 0)"),
            S("Component equations", math=r"a + 2b + 4c = 0, \quad 2a + b + 5c = 0, \quad 3a + 6c = 0"),
            S("From the third, $a = -2c$; put into the first", math=r"-2c + 2b + 4c = 0 \Rightarrow b = -c", text="The second equation then reads $-4c - c + 5c = 0$, which is true for every $c$."),
            S("A non-zero solution exists", math=r"c = 1: \ a = -2,\ b = -1", text=r"So $-2\mathbf{v}_1 - \mathbf{v}_2 + \mathbf{v}_3 = \mathbf{0}$, that is $\mathbf{v}_3 = 2\mathbf{v}_1 + \mathbf{v}_2$. The vectors are **dependent**."),
        ], check=r"2(1, 2, 3) + (2, 1, 0) = (4, 5, 6)"),
        TIP(r"For $n$ vectors in $\mathbb{R}^n$ put them as the columns of a square matrix: they are independent exactly when the determinant is non-zero. Here the determinant is $0$. Any set of **more than $n$ vectors in $\mathbb{R}^n$** is always dependent."),
        H("Basis and dimension"),
        D(r"A **basis** of a vector space $V$ is a set of vectors that is linearly independent **and** spans $V$. Every vector of $V$ is then a combination of the basis vectors in exactly one way. All bases of $V$ have the same number of vectors; this number is the **dimension** of $V$, written $\dim V$.",
          title="Basis and dimension"),
        KEY("Standard dimensions", "Memorise these; they appear in many questions.", cards=[
            [r"$\mathbb{R}^n$", r"Dimension $n$. Standard basis $\mathbf{e}_1, \dots, \mathbf{e}_n$."],
            [r"Polynomials of degree $\le n$", r"Dimension $n + 1$. Basis $1, x, x^2, \dots, x^n$."],
            [r"$2 \times 2$ matrices", r"Dimension $4$. Basis: four matrices, each with a single 1."],
            ["Zero space", r"$\{\mathbf{0}\}$ has dimension $0$ (its basis is the empty set)."],
        ]),
        EX("Worked example 3: a basis for a subspace", intro=r"Find a basis and the dimension of $P = \{(x, y, z) : x + 2y - z = 0\}$, and write $(3, -2, -1)$ in terms of your basis.", steps=[
            S("Solve for one variable in terms of the others", math=r"z = x + 2y", text="So $x$ and $y$ are free."),
            S("Write a general vector", math=r"(x, y, x + 2y) = x(1, 0, 1) + y(0, 1, 2)"),
            S("The two vectors span $P$ and are independent", text=r"Neither is a multiple of the other, so $\{(1, 0, 1), (0, 1, 2)\}$ is a basis and $\dim P = 2$."),
            S("Coordinates of $(3, -2, -1)$", math=r"(3, -2, -1) = 3(1, 0, 1) - 2(0, 1, 2)", text=r"Check it is in $P$: $3 + 2(-2) - (-1) = 0$. Its coordinates relative to this basis are $(3, -2)$."),
        ], check=r"3(1, 0, 1) - 2(0, 1, 2) = (3, -2, 3 - 4) = (3, -2, -1)"),
        T(r"**Why the count matters.** In an $n$-dimensional space, any $n$ independent vectors form a basis, and any set of $n$ vectors that spans is a basis. So you only need to check one of the two conditions once you know the dimension. In the example, $\mathbb{R}^3$ has dimension 3 and the subspace $P$ has dimension 2, so it is a proper plane inside the space."),
        MISTAKE("Thinking the basis is unique", r"A space has many bases; only the **number** of vectors is fixed. $\{(1, 0, 1), (0, 1, 2)\}$ and $\{(1, 1, 3), (1, -1, -1)\}$ are both bases of the plane $x + 2y - z = 0$."),
        MISTAKE("Confusing dimension with the size of the vectors", r"A plane in $\mathbb{R}^3$ is made of vectors with three components, but its dimension is $2$. Dimension counts the independent directions, not the number of components."),
        QUIZ(r"Which set is a subspace of $\mathbb{R}^2$?",
             [r"$\{(x, y) : x + y = 1\}$", r"$\{(x, y) : y = 3x\}$", r"$\{(x, y) : x^2 = y\}$", r"$\{(x, y) : x \ge 0\}$"], 1,
             r"$y = 3x$ is a line through the origin: it contains $\mathbf{0}$ and is closed under addition and scalar multiples.", hint="Check the zero vector first, then closure.",
             feedback=[r"The zero vector $(0, 0)$ does not satisfy $x + y = 1$.", "", r"The parabola contains $(1, 1)$ and $(2, 4)$ but not their sum $(3, 5)$.", r"$(1, 0)$ is in the set but $-1 \cdot (1, 0) = (-1, 0)$ is not: not closed under scalar multiples."]),
        QUIZ(r"The vectors $(1, 0, 1)$, $(0, 1, 1)$, $(1, 1, 2)$ in $\mathbb{R}^3$ are:",
             ["a basis of $\\mathbb{R}^3$", "linearly dependent, because the third is the sum of the first two", "linearly independent, because none is a multiple of another", "a basis of a 3-dimensional subspace"], 1,
             r"$(1, 0, 1) + (0, 1, 1) = (1, 1, 2)$, so the set is dependent and spans only a plane.", hint="Try adding two of the vectors.",
             feedback=["A basis needs independence.", "", r"Not being multiples pairwise is not enough: dependence can involve all three vectors.", r"A dependent set spans only a 2-dimensional subspace."]),
        H("Practice questions"),
        PQ(r"Show that $W = \{(x, y, z) : x = y = z\}$ is a subspace of $\mathbb{R}^3$ and state a basis and its dimension.",
           r"$W = \{t(1, 1, 1)\}$. It contains $\mathbf{0}$ ($t = 0$); $t(1,1,1) + s(1,1,1) = (t+s)(1,1,1) \in W$; $\lambda t(1,1,1) \in W$. So it is a subspace with basis $\{(1, 1, 1)\}$ and dimension $1$ (a line through the origin)."),
        PQ(r"Decide whether $(1, 1, 0)$, $(0, 1, 1)$, $(1, 0, 1)$ form a basis of $\mathbb{R}^3$, and write $(2, 3, 5)$ in terms of them.",
           r"The determinant of the matrix with these columns is $2 \neq 0$, so the three vectors are independent and form a basis of $\mathbb{R}^3$. Solve $a(1,1,0) + b(0,1,1) + c(1,0,1) = (2,3,5)$: $a + c = 2$, $a + b = 3$, $b + c = 5$. Adding: $a + b + c = 5$, so $b = 3$, $c = 2$, $a = 0$. Coordinates: $(0, 3, 2)$. Check: $3(0,1,1) + 2(1,0,1) = (2, 3, 5)$."),
        PQ(r"The polynomials $p_1 = 1 + x$, $p_2 = x + x^2$, $p_3 = 1 + x^2$ lie in the space of polynomials of degree at most 2. Show that they form a basis of it.",
           r"That space has dimension 3, so three independent polynomials form a basis. Suppose $a(1 + x) + b(x + x^2) + c(1 + x^2) = 0$. Coefficients: constant $a + c = 0$; $x$: $a + b = 0$; $x^2$: $b + c = 0$. Then $c = -a$, $b = -a$, and $b + c = -2a = 0$ gives $a = b = c = 0$. They are independent, hence a basis."),
        PQ(r"Find the dimension of the subspace of $2 \times 2$ matrices $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $a + d = 0$ and give a basis.",
           r"The condition gives $d = -a$, so the matrix is $a\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$. These three matrices are independent and span, so the dimension is $3$ (4 free entries minus 1 condition)."),
        H("Summary"),
        SUM(r"A subspace contains $\mathbf{0}$ and is closed under addition and scalar multiplication; a set defined by $x + y = 1$ is not a subspace.",
            r"Vectors are independent when $\sum a_i\mathbf{v}_i = \mathbf{0}$ forces every $a_i = 0$; more than $n$ vectors in $\mathbb{R}^n$ are always dependent.",
            "A basis is independent and spans; every basis of a space has the same number of vectors, the dimension.",
            r"Standard dimensions: $\mathbb{R}^n$ has $n$, polynomials of degree $\le n$ have $n+1$, $2\times2$ matrices have $4$.",
            "Coordinates of a vector relative to a basis are the unique coefficients of the basis vectors."),
    ],
))

LESSONS.append(lesson(
    module=VS, topic="Linear transformations",
    title="Linear transformations and their matrices",
    slug="fmu2-linear-transformations-matrices",
    minutes=23,
    summary="Recognise a linear transformation, build its matrix from the images of the basis vectors, combine transformations and interpret rotations, reflections and differentiation.",
    objectives=[
        "State and use the two conditions for a linear map, T(u+v)=T(u)+T(v) and T(ku)=kT(u)",
        "Build the matrix of a linear transformation from the images of the basis vectors",
        "Find the matrix of a composite transformation, taking care with the order",
        "Represent transformations of polynomials, such as differentiation, by matrices",
    ],
    key_concepts=["Linear transformation", "Matrix representation", "Images of basis vectors", "Composition", "Standard matrices"],
    blocks=[
        H("Introduction"),
        T("A photo editor on a phone rotates, stretches or reflects a picture. Each action moves every point by a fixed rule, and the rule has a special property: it respects addition and scaling. Such rules are called **linear transformations**, and every one of them can be written as a matrix."),
        T("In this lesson you learn how to test whether a rule is linear, how to write its matrix, and how to combine transformations."),
        H("Linear maps"),
        D(r"A function $T : V \to W$ between vector spaces is a **linear transformation** (or linear map) if, for all $\mathbf{u}, \mathbf{v}$ in $V$ and every scalar $\lambda$,",
          title="Linear transformation",
          formula=r"T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \qquad\text{and}\qquad T(\lambda\mathbf{u}) = \lambda\,T(\mathbf{u})",
          note=r"Two quick consequences: $T(\mathbf{0}) = \mathbf{0}$, and $T$ is fixed once you know $T$ of each basis vector."),
        EX("Worked example 1: linear or not?", intro=r"Decide whether (a) $T(x, y) = (x + y,\ 2x)$ and (b) $S(x, y) = (x + 1,\ y)$ are linear.", steps=[
            S("(a) Addition", math=r"T(x_1 + x_2, y_1 + y_2) = (x_1 + x_2 + y_1 + y_2,\ 2x_1 + 2x_2) = T(x_1, y_1) + T(x_2, y_2)"),
            S("(a) Scalar multiple", math=r"T(\lambda x, \lambda y) = (\lambda x + \lambda y,\ 2\lambda x) = \lambda\,T(x, y)", text="Both conditions hold: $T$ is linear."),
            S("(b) A quick test: where does zero go?", math=r"S(0, 0) = (1, 0) \neq (0, 0)", text="A linear map must send $\\mathbf{0}$ to $\\mathbf{0}$. So $S$ is **not** linear (it is a translation, not a linear map)."),
        ]),
        MISTAKE("Calling a map linear because it looks simple", r"Maps containing a constant, a square or a product of variables are not linear: $(x, y) \mapsto (x + 1, y)$, $(x, y) \mapsto (x^2, y)$ and $(x, y) \mapsto (xy, y)$ all fail. A linear map has only terms of the first degree with no constant."),
        H("The matrix of a transformation"),
        D(r"Let $T : \mathbb{R}^n \to \mathbb{R}^m$ be linear. Its **matrix** $A$ (with respect to the standard bases) is the $m \times n$ matrix whose columns are the images of the standard basis vectors, and $T(\mathbf{x}) = A\mathbf{x}$:",
          title="Matrix of a linear map", formula=r"A = \big[\, T(\mathbf{e}_1)\ \ T(\mathbf{e}_2)\ \cdots\ T(\mathbf{e}_n) \,\big]",
          note="Reason: any x = x1 e1 + ... + xn en, so T(x) = x1 T(e1) + ... + xn T(en), which is the matrix times the column x."),
        EX("Worked example 2: matrix from a formula", intro=r"$T : \mathbb{R}^3 \to \mathbb{R}^3$ is given by $T(x, y, z) = (x + y,\ y - z,\ 2x + z)$. Find its matrix and $T(1, 2, 3)$.", steps=[
            S("Images of the basis vectors", math=r"T(1,0,0) = (1, 0, 2), \quad T(0,1,0) = (1, 1, 0), \quad T(0,0,1) = (0, -1, 1)"),
            S("Place them as columns", math=r"A = " + _m([1, 1, 0], [0, 1, -1], [2, 0, 1])),
            S("Apply to $(1, 2, 3)$", math=r"A" + _v(1, 2, 3) + " = " + _v(3, -1, 5), text="Check from the formula: $(1+2,\\ 2-3,\\ 2+3) = (3, -1, 5)$."),
        ], check=r"\det A = 1(1 - 0) - 1(0 + 2) + 0 = -1"),
        EX("Worked example 3: matrix from images of other vectors", intro=r"A linear map $T$ on $\mathbb{R}^2$ satisfies $T(1, 1) = (3, 1)$ and $T(1, -1) = (1, -1)$. Find its matrix.", steps=[
            S("Write the basis vectors using the given ones", math=r"\mathbf{e}_1 = \tfrac{1}{2}\big[(1,1) + (1,-1)\big], \quad \mathbf{e}_2 = \tfrac{1}{2}\big[(1,1) - (1,-1)\big]"),
            S("Use linearity", math=r"T(\mathbf{e}_1) = \tfrac{1}{2}\big[(3,1) + (1,-1)\big] = (2, 0), \quad T(\mathbf{e}_2) = \tfrac{1}{2}\big[(3,1) - (1,-1)\big] = (1, 1)"),
            S("Columns", math=r"A = " + _m([2, 1], [0, 1])),
        ], check=r"A" + _v(1, 1) + " = " + _v(3, 1) + r", \quad A" + _v(1, -1) + " = " + _v(1, -1)),
        H("Standard transformations in the plane"),
        KEY("Matrices to know", "Each column is the image of e1 = (1,0) and e2 = (0,1).", cards=[
            ["Rotation about O, anticlockwise by angle t", r"$\begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix}$. For $t = 90^\circ$: $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$."],
            ["Reflection in the line y = x", r"$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$"],
            ["Stretch, factor a in x and b in y", r"$\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$"],
            ["Shear parallel to the x-axis", r"$\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$"],
        ]),
        H("Composition"),
        D(r"If $S$ has matrix $B$ and $T$ has matrix $A$, then doing $S$ first and $T$ second is $T \circ S$, with matrix $AB$:", title="Composite transformation", formula=r"(T \circ S)(\mathbf{x}) = A(B\mathbf{x}) = (AB)\mathbf{x}",
          note="The matrix of the transformation done FIRST is on the RIGHT."),
        T(r"Example: let $R$ be the rotation by $90^\circ$ anticlockwise, $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and $M$ the reflection in $y = x$, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. Reflect then rotate: $RM = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$, a reflection in the $y$-axis. Rotate then reflect: $MR = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, a reflection in the $x$-axis. The order matters."),
        H("Beyond arrows: differentiation as a matrix"),
        T(r"Linear maps are not only about arrows. Differentiation $D(p) = p'$ is linear: $(p + q)' = p' + q'$ and $(\lambda p)' = \lambda p'$. Take $D$ from polynomials of degree at most 3, with basis $\{1, x, x^2, x^3\}$, to degree at most 2, with basis $\{1, x, x^2\}$. The images of the basis are $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$, $D(x^3) = 3x^2$. Writing each image in coordinates gives the columns:"),
        F(r"[D] = " + _m([0, 1, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]), title="A 3 by 4 matrix"),
        T(r"Check with $p = 5 + 2x - x^2 + 4x^3$, coordinates $(5, 2, -1, 4)$: $[D]\,(5,2,-1,4)^T = (2,\ -2,\ 12)^T$, which is $2 - 2x + 12x^2 = p'$."),
        QUIZ(r"$T$ is linear with $T(1, 0) = (2, 3)$ and $T(0, 1) = (-1, 4)$. Find $T(2, 5)$.",
             ["$(-1, 26)$", "$(-1, 23)$", "$(1, 7)$", "$(4, 20)$"], 0,
             r"$T(2,5) = 2(2,3) + 5(-1,4) = (4 - 5,\ 6 + 20) = (-1, 26)$.", hint="Write (2,5) as 2e1 + 5e2 and use linearity.",
             feedback=["", r"The second component is $6 + 20 = 26$, not $23$.", r"You added $(2,3) + (-1,4)$ without scaling by $2$ and $5$.", r"You multiplied the components $2 \times 2$ and $5 \times 4$, which is not a linear combination of the images."]),
        QUIZ(r"$A$ and $B$ are the matrices of $T$ and $S$. The matrix of 'first $S$, then $T$' is:",
             [r"$BA$", r"$AB$", r"$A + B$", r"$A^{-1}B$"], 1,
             r"The first transformation acts on the vector first, so its matrix is next to the vector: $A(B\mathbf{x})$.", hint="Write T(S(x)) in matrix form.",
             feedback=["That is 'first T, then S'.", "", "Addition of matrices is not composition.", "Inverses have nothing to do with composition here."]),
        H("Practice questions"),
        PQ(r"Show that $T(x, y) = (3x - y,\ x + 2y)$ is linear and write down its matrix. Find the image of $(2, -1)$.",
           r"$T(\mathbf{u} + \mathbf{v})$ has components $3(x_1 + x_2) - (y_1 + y_2)$ and $(x_1 + x_2) + 2(y_1 + y_2)$, which is $T(\mathbf{u}) + T(\mathbf{v})$; likewise $T(\lambda\mathbf{u}) = \lambda T(\mathbf{u})$. Matrix: $\begin{pmatrix} 3 & -1 \\ 1 & 2 \end{pmatrix}$. $T(2, -1) = (6 + 1,\ 2 - 2) = (7, 0)$."),
        PQ(r"Find the matrix of the rotation through $90^\circ$ anticlockwise followed by a stretch of factor 3 in the $x$-direction (only).",
           r"Rotation $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, stretch $S = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$. Rotation first, so the matrix is $SR = \begin{pmatrix} 0 & -3 \\ 1 & 0 \end{pmatrix}$."),
        PQ(r"A linear map has $T(1, 2) = (4, 5)$ and $T(0, 1) = (1, 3)$. Find its matrix.",
           r"$T(0,1) = (1, 3)$ is the second column. $T(1, 0) = T(1,2) - 2T(0,1) = (4,5) - (2,6) = (2, -1)$. So $A = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$. Check: $A(1,2)^T = (2 + 2,\ -1 + 6) = (4, 5)$."),
        PQ(r"The map $I(p) = \int_0^x p(t)\,dt$ sends polynomials of degree at most 2 (basis $1, x, x^2$) to polynomials of degree at most 3 (basis $1, x, x^2, x^3$). Find its matrix.",
           r"$I(1) = x$, $I(x) = \frac{x^2}{2}$, $I(x^2) = \frac{x^3}{3}$. In coordinates relative to $(1, x, x^2, x^3)$ these are $(0, 1, 0, 0)$, $(0, 0, \frac12, 0)$, $(0, 0, 0, \frac13)$. The $4 \times 3$ matrix has these as columns."),
        H("Summary"),
        SUM(r"$T$ is linear when $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ and $T(\lambda\mathbf{u}) = \lambda T(\mathbf{u})$; in particular $T(\mathbf{0}) = \mathbf{0}$.",
            "The matrix of T has the images of the basis vectors as its columns.",
            "The matrix of 'first S, then T' is AB: the first transformation is on the right.",
            "Rotation, reflection, stretch and shear have standard matrices; order of composition changes the result.",
            "Differentiation and integration of polynomials are linear maps and have matrices once bases are chosen."),
    ],
))

LESSONS.append(lesson(
    module=VS, topic="Kernel, range and the rank-nullity theorem",
    title="Kernel, range and the rank-nullity theorem",
    slug="fmu2-kernel-range-rank-nullity",
    minutes=25,
    summary="Find the kernel and range of a linear map, their dimensions, and use rank plus nullity equals dimension of the domain to check results and decide injectivity and surjectivity.",
    objectives=[
        "Define the kernel (null space) and range (image) of a linear map and show that each is a subspace",
        "Find a basis for the kernel and for the range from a matrix by row reduction",
        "State and use rank(T) + nullity(T) = dim of the domain",
        "Link the kernel to one-to-one maps and the range to onto maps",
    ],
    key_concepts=["Kernel (null space)", "Range (image)", "Rank", "Nullity", "Rank-nullity theorem", "One-to-one", "Onto"],
    blocks=[
        H("Introduction"),
        T("A satellite dish in Bafoussam collapses a whole 3D scene of signals onto a flat 2D screen. Many different points land on the same spot, and the screen can only show some of the possible images. Two questions arise for any linear map: **which inputs are destroyed** (sent to zero), and **which outputs can occur**? The kernel and the range answer them, and the rank-nullity theorem says that together they use up the dimension of the input space exactly."),
        H("Kernel and range"),
        D(r"For a linear map $T : V \to W$, the **kernel** (or null space) is the set of inputs sent to zero, and the **range** (or image) is the set of all outputs:",
          title="Kernel and range", formula=r"\ker T = \{\mathbf{v} \in V : T(\mathbf{v}) = \mathbf{0}\}, \qquad \operatorname{range} T = \{T(\mathbf{v}) : \mathbf{v} \in V\}",
          note="The kernel is a subspace of V; the range is a subspace of W. (If T(u) = 0 and T(v) = 0 then T(u+v) = 0 and T(ku) = 0.)"),
        D(r"The **rank** of $T$ is $\dim(\operatorname{range} T)$ and the **nullity** is $\dim(\ker T)$. For a matrix $A$, the kernel is the set of solutions of $A\mathbf{x} = \mathbf{0}$ and the range is the **column space**, the span of the columns of $A$; the rank is the number of leading 1s after row reduction.",
          title="Rank and nullity"),
        T("To find them from a matrix: reduce $A$ by row operations to its row echelon form. The kernel comes from solving $A\\mathbf{x} = \\mathbf{0}$ with free variables for the columns without a leading 1. A basis for the range is given by the **original** columns of $A$ that contain the leading 1s."),
        EX("Worked example 1: kernel and range of a 3 by 4 matrix", intro=r"$T : \mathbb{R}^4 \to \mathbb{R}^3$ has matrix $A = " + _m([1, 2, 0, 1], [2, 4, 1, 5], [3, 6, 1, 6]) + r"$. Find a basis for $\ker T$ and for the range, and verify the rank-nullity theorem.", steps=[
            S("Row reduce ($R_2 - 2R_1$, $R_3 - 3R_1$, then $R_3 - R_2$)", math=r"\begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}", text="Leading 1s are in columns 1 and 3. Columns 2 and 4 are free."),
            S("Kernel: let $x_2 = s$ and $x_4 = t$", math=r"x_3 = -3t, \qquad x_1 = -2s - t", text=r"So $\mathbf{x} = s(-2, 1, 0, 0) + t(-1, 0, -3, 1)$."),
            S("Basis of the kernel", math=r"\{(-2, 1, 0, 0),\ (-1, 0, -3, 1)\}", text="Nullity = 2."),
            S("Range: the original columns 1 and 3", math=r"\{(1, 2, 3),\ (0, 1, 1)\}", text="Rank = 2. (Columns 2 and 4 are combinations of these.)"),
            S("Rank-nullity", math=r"\text{rank} + \text{nullity} = 2 + 2 = 4 = \dim \mathbb{R}^4"),
        ], check=r"A" + _v(-2, 1, 0, 0) + " = " + _v(0, 0, 0) + r", \quad A" + _v(-1, 0, -3, 1) + " = " + _v(0, 0, 0)),
        KEY("The Rank-Nullity Theorem", r"For a linear map $T : V \to W$ with $V$ of finite dimension,", cards=[
            ["The theorem", r"$\operatorname{rank}(T) + \operatorname{nullity}(T) = \dim V$"],
            ["Where it comes from", "Take a basis of the kernel and extend it to a basis of V. The extra vectors map to a basis of the range, so the dimensions add up."],
            ["Use it", "Find one of the two numbers; the other follows. Also a quick check on a row reduction."],
        ]),
        H("One-to-one and onto"),
        D(r"$T$ is **one-to-one** (injective) when different inputs give different outputs. For a linear map this holds exactly when $\ker T = \{\mathbf{0}\}$, that is, nullity $= 0$. $T$ is **onto** (surjective) when its range is the whole of $W$, that is, rank $= \dim W$.",
          title="Injective and surjective"),
        T(r"Why the kernel decides injectivity: if $T(\mathbf{u}) = T(\mathbf{v})$ then $T(\mathbf{u} - \mathbf{v}) = \mathbf{0}$, so $\mathbf{u} - \mathbf{v}$ is in the kernel. If the kernel is only $\mathbf{0}$, then $\mathbf{u} = \mathbf{v}$."),
        EX("Worked example 2: a map from R3 to R3", intro=r"$T(x, y, z) = (x + y,\ y - z,\ 2x + z)$ has matrix $A$ with $\det A = -1$ (from the previous lesson). Describe its kernel and range.", steps=[
            S("Determinant non-zero", text=r"$A$ is invertible, so $A\mathbf{x} = \mathbf{0}$ has only the solution $\mathbf{x} = \mathbf{0}$."),
            S("Kernel", math=r"\ker T = \{\mathbf{0}\}, \quad \text{nullity} = 0", text="So $T$ is one-to-one."),
            S("Rank-nullity", math=r"\text{rank} = 3 - 0 = 3", text=r"The range is all of $\mathbb{R}^3$: $T$ is onto as well. A map that is both is called an **isomorphism**."),
        ]),
        EX("Worked example 3: differentiation", intro=r"$D : P_3 \to P_2$ takes a polynomial of degree at most 3 to its derivative. Find the kernel, range, rank and nullity.", steps=[
            S("Kernel: polynomials with $p' = 0$", text="These are the constants, so $\\ker D = \\{c\\}$ with basis $\\{1\\}$ and nullity $1$."),
            S("Range", text=r"Every polynomial of degree at most 2 is the derivative of some polynomial of degree at most 3 (integrate it), so the range is $P_2$, of dimension $3$: rank $= 3$."),
            S("Check", math=r"\text{rank} + \text{nullity} = 3 + 1 = 4 = \dim P_3 \quad (1, x, x^2, x^3)"),
        ]),
        MISTAKE("Taking the range basis from the reduced matrix", r"The pivot columns of the **reduced** matrix are not in the range. Take the **original** columns of $A$ in the pivot positions. In Example 1 the reduced column 3 is $(0, 1, 0)$, but the range contains $(0, 1, 1)$, the original column 3."),
        MISTAKE("Using the wrong dimension in rank-nullity", r"rank + nullity equals the dimension of the **domain** (the number of columns of the matrix), not of the codomain. For a $3 \times 4$ matrix the sum is $4$, even though outputs live in $\mathbb{R}^3$."),
        QUIZ(r"A linear map $T : \mathbb{R}^5 \to \mathbb{R}^3$ is onto. What is the nullity?",
             ["$0$", "$2$", "$3$", "$5$"], 1,
             r"Onto means rank $= 3$, so nullity $= 5 - 3 = 2$.", hint="Use rank + nullity = 5 and say what onto means for the rank.",
             feedback=["A map from a bigger space to a smaller one cannot be one-to-one, so the nullity is at least 2.", "", "That is the rank.", "That is the dimension of the domain, not the nullity."]),
        QUIZ(r"A $4 \times 4$ matrix has rank 3. How many independent solutions does $A\mathbf{x} = \mathbf{0}$ have?",
             ["$0$", "$1$", "$3$", "$4$"], 1,
             r"Nullity $= 4 - 3 = 1$: the solutions form a line through the origin.", hint="Rank plus nullity equals 4.",
             feedback=["That would mean rank 4.", "", "Three is the rank, not the nullity.", "That would mean the zero matrix."]),
        H("Practice questions"),
        PQ(r"$T : \mathbb{R}^3 \to \mathbb{R}^3$ has matrix $\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{pmatrix}$. Find a basis for the kernel and the range.",
           r"Row 2 $= 2\times$ row 1, and rows 1 and 3 are not multiples of each other, so the rank is $2$. Kernel: $x_1 + x_3 = 0$ (row 3) and $x_1 + 2x_2 + 3x_3 = 0$ (row 1) give $x_1 = -x_3$ and $x_2 = -x_3$. Taking $x_3 = 1$, the kernel has basis $\{(-1, -1, 1)\}$ and the nullity is $1$. Range: the pivots are in columns 1 and 2, so a basis is the original columns $\{(1, 2, 1), (2, 4, 0)\}$. Check: rank $+$ nullity $= 2 + 1 = 3$."),
        PQ(r"The map $T : \mathbb{R}^2 \to \mathbb{R}^3$ has $T(x, y) = (x + y,\ x - y,\ 2x)$. Find its rank, show it is one-to-one and say whether it is onto.",
           r"If $T(x, y) = \mathbf{0}$ then $x + y = 0$, $x - y = 0$ gives $x = y = 0$: the kernel is $\{\mathbf{0}\}$, nullity $0$, so $T$ is one-to-one. Rank $= 2 - 0 = 2 < 3 = \dim \mathbb{R}^3$, so it is **not onto**: the range is a plane in $\mathbb{R}^3$."),
        PQ(r"A linear map $T : \mathbb{R}^4 \to \mathbb{R}^4$ has a kernel spanned by two independent vectors. State its rank, and say whether $T\mathbf{x} = \mathbf{b}$ always has a solution.",
           r"Nullity $= 2$, so rank $= 4 - 2 = 2$. The range is a 2-dimensional subspace of $\mathbb{R}^4$, so $T\mathbf{x} = \mathbf{b}$ has a solution only for $\mathbf{b}$ in that subspace, not for every $\mathbf{b}$. When there is a solution there are infinitely many (add any kernel vector)."),
        PQ(r"Show that if $T : V \to V$ is linear and $T^2 = 0$ (the zero map) then $\operatorname{range} T \subseteq \ker T$. Deduce that for $V = \mathbb{R}^3$ the rank of $T$ is at most 1.",
           r"If $\mathbf{w}$ is in the range, then $\mathbf{w} = T(\mathbf{v})$ and $T(\mathbf{w}) = T^2(\mathbf{v}) = \mathbf{0}$, so $\mathbf{w} \in \ker T$. Hence rank $\le$ nullity. Let the rank be $r$. Then $r \le$ nullity $= 3 - r$, so $2r \le 3$ and, since $r$ is a whole number, $r \le 1$."),
        H("Summary"),
        SUM(r"The kernel is the set of inputs sent to $\mathbf{0}$; the range is the set of outputs; both are subspaces.",
            "For a matrix: the kernel is the solution set of Ax = 0; a basis for the range is the original pivot columns.",
            r"Rank-nullity: rank $+$ nullity $= \dim V$, the number of columns for a matrix.",
            r"One-to-one $\Leftrightarrow$ kernel is $\{\mathbf{0}\}$; onto $\Leftrightarrow$ rank $= \dim W$.",
            "Always check your row reduction with rank + nullity."),
    ],
))



# ================================================================ Numerical methods: helpers that compute the tables
def _bisect_table(f, a, b, n):
    lines = ["step     a        b       mid     f(mid)"]
    for i in range(1, n + 1):
        m = (a + b) / 2
        fm = f(m)
        lines.append(f"{i:>3}  {a:8.5f} {b:8.5f} {m:8.5f} {fm:+9.5f}")
        if f(a) * fm < 0:
            b = m
        else:
            a = m
    return "\n".join(lines), (a, b)


def _interp_table(f, a, b, n):
    lines = ["step     a        b         x1       f(x1)"]
    for i in range(1, n + 1):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        lines.append(f"{i:>3}  {a:8.5f} {b:8.5f} {x:10.6f} {f(x):+10.6f}")
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
    return "\n".join(lines), x


def _newton_table(f, df, x, n):
    lines = ["  n       x_n            f(x_n)         f'(x_n)       x_(n+1)"]
    for i in range(n):
        xn = x - f(x) / df(x)
        lines.append(f"{i:>3} {x:14.9f} {f(x):14.3e} {df(x):12.6f} {xn:14.9f}")
        x = xn
    return "\n".join(lines), x


def _trap(f, a, b, n):
    h = (b - a) / n
    return h / 2 * (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n)))


def _simp(f, a, b, n):
    h = (b - a) / n
    return h / 3 * (f(a) + f(b) + 4 * sum(f(a + i * h) for i in range(1, n, 2)) + 2 * sum(f(a + i * h) for i in range(2, n, 2)))


def _ode_table(f, x0, y0, h, n, method):
    """Rows: x, y for Euler ('e'), improved Euler ('h') or fourth-order Runge-Kutta ('r')."""
    x, y = x0, y0
    rows = [(x, y)]
    for _ in range(n):
        if method == "e":
            y = y + h * f(x, y)
        elif method == "h":
            k1 = f(x, y)
            k2 = f(x + h, y + h * k1)
            y = y + h / 2 * (k1 + k2)
        else:
            k1 = f(x, y)
            k2 = f(x + h / 2, y + h / 2 * k1)
            k3 = f(x + h / 2, y + h / 2 * k2)
            k4 = f(x + h, y + h * k3)
            y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
        rows.append((x, y))
    return rows


_cosx = lambda x: math.cos(x) - x  # noqa: E731
_cubic = lambda x: x ** 3 - 2 * x - 5  # noqa: E731
_dcubic = lambda x: 3 * x * x - 2  # noqa: E731
_BIS_TAB, _BIS_END = _bisect_table(_cosx, 0, 1, 8)
_INT_TAB, _INT_X = _interp_table(_cubic, 2, 3, 5)
_NEW_TAB, _NEW_X = _newton_table(_cubic, _dcubic, 2.0, 4)
_SQ_TAB, _SQ_X = _newton_table(lambda x: x * x - 7, lambda x: 2 * x, 2.0, 4)
_EXP_TAB, _EXP_X = _newton_table(lambda x: math.exp(x) - 5 * x, lambda x: math.exp(x) - 5, 0.5, 4)
assert abs(_BIS_END[0] - 0.73828) < 1e-4 and abs(_BIS_END[1] - 0.74219) < 1e-4
assert abs(_INT_X - 2.093884) < 1e-6
assert abs(_NEW_X - 2.0945514815) < 1e-9
assert abs(_SQ_X - 7 ** 0.5) < 1e-9
assert abs(_EXP_X - 0.2591711018) < 1e-9

# ---------------------------------------------------------------- Root finding 1: bisection and interpolation
LESSONS.append(lesson(
    module=NM, topic="Root finding",
    title="Locating roots: change of sign, bisection and linear interpolation",
    slug="fmu2-root-finding-bisection-interpolation",
    minutes=22,
    summary="Show that a root lies in an interval by a sign change, then home in on it by bisection and by linear interpolation, with the iterations tabulated and the accuracy controlled.",
    objectives=[
        "Show that f(x) = 0 has a root in an interval using a change of sign, and explain when the argument fails",
        "Apply the bisection method and say how many steps give a required accuracy",
        "Apply linear interpolation (false position) and explain why it can be slow",
        "Report a root to a stated number of decimal places with a justified sign-change check",
    ],
    key_concepts=["Change of sign", "Continuity", "Bisection", "Linear interpolation", "Error bound", "Iteration table"],
    blocks=[
        H("Introduction"),
        T(r"Some equations cannot be solved by algebra. For example $\cos x = x$ has one solution, but no formula gives it. A calculator finds it by **numerical methods**: start with a rough location, then improve it step by step until the answer is accurate enough."),
        T("In this lesson you learn two safe methods that work from an interval where the root is trapped. They never fail once they have started, but one is slower than you might hope."),
        H("Trapping a root: change of sign"),
        D(r"If $f$ is **continuous** on $[a, b]$ and $f(a)$ and $f(b)$ have opposite signs, then $f(x) = 0$ has at least one root in $(a, b)$.", title="Change of sign rule",
          formula=r"f(a)\,f(b) < 0 \ \Longrightarrow\ \text{a root in } (a, b)",
          note=r"Always say that $f$ is continuous. Be careful with $1/x$ or $\tan x$: the sign changes across a break and there is no root."),
        EX("Worked example 1: showing a root exists", intro=r"Show that $\cos x = x$ has a root between $0$ and $1$ (angles in radians).", steps=[
            S("Define $f$", math=r"f(x) = \cos x - x", text="This is continuous for all $x$."),
            S("Evaluate at the ends", math=r"f(0) = 1 > 0, \qquad f(1) = \cos 1 - 1 = -0.4597 < 0"),
            S("Conclude", text="$f$ is continuous and changes sign, so there is a root in $(0, 1)$."),
        ]),
        H("The bisection method"),
        D(r"Take an interval $[a, b]$ with a sign change. Halve it at $m = \dfrac{a + b}{2}$. Evaluate $f(m)$: the root is in whichever half still shows a sign change, so replace $a$ or $b$ by $m$. Repeat. After $n$ steps the interval has width $(b - a)/2^n$.", title="Bisection"),
        T(r"Accuracy: if you stop when the interval has width $w$, any point in it (such as the midpoint) is within $w$ of the root, and the midpoint is within $\frac{w}{2}$. To reach an error below $\varepsilon$ you need $\dfrac{b - a}{2^n} \le \varepsilon$, so $n \ge \log_2\dfrac{b - a}{\varepsilon}$."),
        CODE(_BIS_TAB, "text", title="Table 1. Bisection for cos x - x = 0 on [0, 1] (values computed by program)"),
        EX("Worked example 2: how accurate after 8 steps?", intro=r"Use Table 1 to state the root of $\cos x = x$ to 2 decimal places, and find how many steps give an error below $0.0005$.", steps=[
            S("Read the interval after step 8", text=r"Step 8 has $f(0.73828) > 0$ and $f(0.74219) < 0$, so the root lies in $(0.73828,\ 0.74219)$, an interval of width $1/2^8 = 0.0039$."),
            S("Two decimal places", text="Every number in this interval rounds to $0.74$, so the root is $0.74$ to 2 d.p. The midpoint $0.7402$ is within $0.002$ of the root."),
            S("Steps needed for error below 0.0005", math=r"\frac{1}{2^n} \le 0.001 \ \Rightarrow\ n \ge \log_2 1000 = 9.97", text="The midpoint is within half the interval width; the interval must be below $0.001$, so $n = 10$ steps."),
        ], check=r"\text{True root } 0.73909 \in (0.73828,\ 0.74219)"),
        H("Linear interpolation (false position)"),
        T(r"Bisection ignores how big $f(a)$ and $f(b)$ are. If $f(a)$ is very small and $f(b)$ very large, the root is probably near $a$. **Linear interpolation** replaces the curve between $(a, f(a))$ and $(b, f(b))$ by a straight line and takes where the line crosses the $x$-axis."),
        D(r"The chord through $(a, f(a))$ and $(b, f(b))$ crosses the axis at", title="Linear interpolation formula",
          formula=r"x = \frac{a\,f(b) - b\,f(a)}{f(b) - f(a)} = a - f(a)\,\frac{b - a}{f(b) - f(a)}",
          note="From similar triangles. Then keep the sub-interval that still has a sign change, as in bisection. With signs opposite, the denominator f(b) - f(a) is never zero."),
        CODE(_INT_TAB, "text", title="Table 2. Linear interpolation for x^3 - 2x - 5 = 0 on [2, 3] (computed by program)"),
        EX("Worked example 3: the first interpolation step", intro=r"$f(x) = x^3 - 2x - 5$ has $f(2) = -1$ and $f(3) = 16$. Find the first estimate by linear interpolation and state the next interval.", steps=[
            S("Substitute", math=r"x_1 = \frac{2(16) - 3(-1)}{16 - (-1)} = \frac{35}{17} = 2.0588"),
            S("Sign of $f(x_1)$", math=r"f(2.0588) = -0.3908 < 0", text="Same sign as $f(2)$, so replace $a$ by $x_1$: the new interval is $[2.0588,\\ 3]$."),
            S("What Table 2 shows", text=r"Every step has $f(x_1) < 0$, so $b = 3$ never moves. The estimates creep up from one side (2.0588, 2.0813, 2.0896, 2.0927, 2.0939) towards the root $2.0946$. The method works but is slow when the curve bends the same way over the whole interval."),
        ], check=r"2.0588^3 - 2(2.0588) - 5 = 8.7265 - 4.1176 - 5 = -0.3911"),
        TIP(r"For a final answer such as '$2.09$ to 2 d.p.' you must justify it: show a sign change of $f$ at $2.085$ and $2.095$ (both bounds of the rounding interval), with $f$ continuous. The tables alone are not enough."),
        MISTAKE("Using a calculator in degrees", r"In $\cos x - x$ the $x$ is a number, so the angle is in **radians**. In degree mode the table would be wrong and the sign change would not appear where it should."),
        MISTAKE("Bisecting without a sign change", r"If $f(a)$ and $f(b)$ have the same sign there may be no root, or two roots. Check $f(a)f(b) < 0$ first. And $\tan x$ changes sign across $x = \frac{\pi}{2}$ with no root there."),
        MISTAKE("Stopping because f is small", r"A small $|f(x)|$ does not guarantee a small error in $x$ when the curve is flat. State the interval in which the root is trapped."),
        QUIZ(r"Bisection starts on an interval of width $4$. How many steps guarantee an interval of width below $0.01$?",
             ["$7$", "$8$", "$9$", "$400$"], 2,
             r"$4/2^n < 0.01$ needs $2^n > 400$. Since $2^8 = 256$ gives $4/256 = 0.0156$ (too wide) and $2^9 = 512$ gives $0.0078$, $n = 9$.", hint="Compute 4/2^n for n = 7, 8, 9.",
             feedback=[r"$4/128 = 0.031$ is still above $0.01$.", r"$4/256 = 0.0156$ is still above $0.01$.", "", "The interval shrinks by half each step, so a few steps are enough."]),
        QUIZ(r"$f(x) = \dfrac{1}{x - 2}$ has $f(1) = -1$ and $f(3) = 1$. Which statement is correct?",
             ["There is a root between 1 and 3 because the sign changes", "There is no root: $f$ is not continuous on $[1, 3]$", "There are two roots", "$x = 2$ is a root"], 1,
             r"$f$ is undefined at $x = 2$, so the sign change comes from a break in the graph, not from crossing the axis.", hint="Is f continuous on the whole interval?",
             feedback=["The rule needs continuity.", "", "The curve never reaches zero.", "$f(2)$ does not exist; it is an asymptote."]),
        H("Practice questions"),
        PQ(r"Show that $x^3 + x - 3 = 0$ has a root between $1$ and $2$. Use two steps of bisection to find an interval of width $0.25$ containing the root.",
           r"$f(1) = -1 < 0$ and $f(2) = 7 > 0$, $f$ continuous, so a root lies in $(1, 2)$. Step 1: $f(1.5) = 3.375 + 1.5 - 3 = 1.875 > 0$, so the root is in $(1, 1.5)$. Step 2: $f(1.25) = 1.953 + 1.25 - 3 = 0.203 > 0$, so the root is in $(1, 1.25)$, an interval of width $0.25$: the sign change is between $f(1) < 0$ and $f(1.25) > 0$."),
        PQ(r"Use linear interpolation once on $f(x) = x^3 + x - 3$ with $a = 1$, $b = 2$ and give the next interval.",
           r"$x_1 = \dfrac{1(7) - 2(-1)}{7 - (-1)} = \dfrac{9}{8} = 1.125$. $f(1.125) = 1.4238 + 1.125 - 3 = -0.4512 < 0$, same sign as $f(1)$, so the new interval is $[1.125, 2]$."),
        PQ(r"The equation $e^{-x} = x$ has a root near $0.57$. Show that the root lies between $0.565$ and $0.575$, and so is $0.57$ to 2 d.p.",
           r"Let $f(x) = e^{-x} - x$ (continuous). $f(0.565) = 0.5684 - 0.565 = 0.0034 > 0$ and $f(0.575) = 0.5627 - 0.575 = -0.0123 < 0$. A sign change in a continuous function: the root is in $(0.565, 0.575)$, so it is $0.57$ to 2 d.p."),
        PQ(r"How many bisection steps, starting from $[2, 3]$, guarantee a root correct to 3 decimal places (error below $0.0005$)?",
           r"The interval width after $n$ steps is $1/2^n$; the midpoint is within half of this. Require $\frac{1}{2^{n+1}} \le 0.0005$, so $2^{n+1} \ge 2000$, $n + 1 \ge 11$ (since $2^{11} = 2048$), $n = 10$. (If you instead require the interval width itself to be below $0.0005$, you would need $n = 11$: state your criterion.)"),
        H("Summary"),
        SUM(r"A continuous function with $f(a)f(b) < 0$ has a root in $(a, b)$; always mention continuity.",
            r"Bisection halves the interval each time; after $n$ steps the width is $(b - a)/2^n$, so the number of steps needed is $\log_2$ of the ratio.",
            r"Linear interpolation: $x = \dfrac{a f(b) - b f(a)}{f(b) - f(a)}$; keep the sub-interval with the sign change.",
            "Interpolation is often faster at first but can stay on one side and creep; bisection is slower but steady.",
            "Prove an accuracy claim by a sign change at both rounding bounds, and use radians for trigonometric functions."),
    ],
))


# ---------------------------------------------------------------- Root finding 2: Newton-Raphson
LESSONS.append(lesson(
    module=NM, topic="Root finding",
    title="The Newton-Raphson method: fast convergence and when it fails",
    slug="fmu2-newton-raphson-iteration",
    minutes=24,
    summary="Derive and apply the Newton-Raphson formula, see why the number of correct digits roughly doubles each step, and recognise starting values for which the method fails.",
    objectives=[
        "Derive x_(n+1) = x_n - f(x_n)/f'(x_n) from the tangent to the curve",
        "Carry out Newton-Raphson iterations and present them in a table",
        "Use the method to find square roots and to solve equations such as e^x = 5x",
        "Explain how a poor starting value can fail: a flat tangent, a cycle or divergence",
    ],
    key_concepts=["Newton-Raphson formula", "Tangent", "Iteration", "Quadratic convergence", "Starting value", "Failure cases"],
    blocks=[
        H("Introduction"),
        T(r"When your calculator finds $\sqrt{7}$ it does not look up a table. It runs a short loop: guess, improve, improve again. The loop that works best for most equations was described by Isaac Newton and Joseph Raphson, and is called the **Newton-Raphson method**. Instead of trapping the root between two points as bisection does, it follows the **tangent** to the curve down to the axis."),
        H("Where the formula comes from"),
        T(r"Let $x_n$ be a guess for a root of $f(x) = 0$. The tangent to the curve at $(x_n, f(x_n))$ has gradient $f'(x_n)$ and equation $y - f(x_n) = f'(x_n)(x - x_n)$. Where it meets the $x$-axis, $y = 0$, so"),
        F(r"x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}", title="Newton-Raphson formula"),
        IMG("al-fmu2-newton-tangent.svg", alt="The curve y = x squared minus 7. A tangent at x0 = 4 meets the x-axis at x1 = 2.875; a second tangent there meets it at 2.6549, close to the root 2.6458.", caption="Figure 1. Newton-Raphson on y = x^2 - 7 from x0 = 4. Each tangent meets the x-axis closer to the root, the square root of 7."),
        D(r"If $f'(x_n) = 0$ the tangent is horizontal and never meets the axis: the formula breaks down. A starting value close to such a point may throw the iteration far away.", title="Condition"),
        H("A worked iteration"),
        CODE(_NEW_TAB, "text", title="Table 3. Newton-Raphson for x^3 - 2x - 5 = 0, x0 = 2 (computed by program)"),
        EX("Worked example 1: the first two steps by hand", intro=r"Solve $x^3 - 2x - 5 = 0$ starting from $x_0 = 2$.", steps=[
            S("The derivative", math=r"f(x) = x^3 - 2x - 5, \quad f'(x) = 3x^2 - 2"),
            S("Step 1", math=r"f(2) = -1, \ f'(2) = 10, \quad x_1 = 2 - \frac{-1}{10} = 2.1"),
            S("Step 2", math=r"f(2.1) = 0.061, \ f'(2.1) = 11.23, \quad x_2 = 2.1 - \frac{0.061}{11.23} = 2.09457"),
            S("Read Table 3", text=r"$x_3 = 2.094551482$ and $x_4 = 2.094551482$ agree to 9 decimal places, so the root is $2.094551$ to 6 d.p."),
        ], check=r"f(2.0945515) = 9.1888 - 4.1891 - 5 = 0.0000"),
        T(r"**Speed.** The error in the iterates is about $0.0945,\ 0.0054,\ 0.000017,\ 0.0000000002$. Each error is roughly the **square** of the one before (times a constant), so the number of correct digits about doubles at each step. This is called **quadratic convergence**. Bisection by comparison gains only one binary digit, about 0.3 of a decimal digit, per step."),
        H("Square roots"),
        T(r"To find $\sqrt{a}$ solve $x^2 - a = 0$. Then $f'(x) = 2x$ and the formula simplifies to $x_{n+1} = \dfrac{1}{2}\left(x_n + \dfrac{a}{x_n}\right)$: the average of $x_n$ and $a/x_n$. If $x_n$ is too small, $a/x_n$ is too large, and their mean is better than both."),
        CODE(_SQ_TAB, "text", title="Table 4. Newton-Raphson for x^2 - 7 = 0, x0 = 2 (computed by program)"),
        EX("Worked example 2: an equation with no algebraic solution", intro=r"Find the smaller positive root of $e^x = 5x$, starting from $x_0 = 0.5$.", steps=[
            S("Write as $f(x) = 0$", math=r"f(x) = e^x - 5x, \quad f'(x) = e^x - 5"),
            S("Step 1", math=r"x_1 = 0.5 - \frac{e^{0.5} - 2.5}{e^{0.5} - 5} = 0.5 - \frac{-0.85128}{-3.35128} = 0.24598"),
            S("Continue (Table 5)", text="The values are $0.2459839,\\ 0.2591411,\\ 0.2591711,\\ 0.2591711$. The root is $0.25917$ to 5 d.p."),
        ], check=r"e^{0.25917} = 1.29586, \quad 5 \times 0.25917 = 1.29585"),
        CODE(_EXP_TAB, "text", title="Table 5. Newton-Raphson for e^x - 5x = 0, x0 = 0.5 (computed by program)"),
        H("When Newton-Raphson fails"),
        KEY("Three ways to go wrong", "Always sketch the curve or check the first step before trusting the iteration.", cards=[
            ["A flat tangent", r"For $f(x) = x^3 - 2x - 5$ take $x_0 = 0.8$. Here $f'(0.8) = -0.08$, almost zero, so $x_1 = 0.8 - \dfrac{-6.088}{-0.08} = -75.3$. The iteration is flung far away from the root at 2.09."],
            ["A cycle", r"For $f(x) = x^3 - 2x + 2$ with $x_0 = 0$: $x_1 = 1$, then $x_2 = 0$, then $1$ again. The iterates swap between two values and never settle."],
            ["Another root", r"A start near a different root converges to that root. If an equation has several roots, the start decides which one you find."],
        ]),
        MISTAKE("Forgetting that the formula needs f' at the same point", r"Use $f'(x_n)$, not $f'(x_0)$ or a fixed value, in every step. Using $f'(x_0)$ throughout gives a slower method that is not Newton-Raphson."),
        MISTAKE("Rounding too early", "Keep at least two more decimal places in the working than you need in the answer. Rounding $x_1$ to 2 d.p. and then differentiating will contaminate the later steps. Quote the final answer only to the accuracy the table supports."),
        MISTAKE("Calculator mode", r"With trigonometric functions $x$ is in radians, and $\dfrac{d}{dx}\sin x = \cos x$ only holds in radians."),
        QUIZ(r"Which is the Newton-Raphson formula for $f(x) = x^2 - 5$?",
             [r"$x_{n+1} = x_n - \dfrac{x_n^2 - 5}{x_n}$", r"$x_{n+1} = \dfrac{1}{2}\left(x_n + \dfrac{5}{x_n}\right)$", r"$x_{n+1} = x_n + \dfrac{x_n^2 - 5}{2x_n}$", r"$x_{n+1} = \dfrac{5}{x_n}$"], 1,
             r"$x_n - \dfrac{x_n^2 - 5}{2x_n} = \dfrac{2x_n^2 - x_n^2 + 5}{2x_n} = \dfrac{x_n}{2} + \dfrac{5}{2x_n}$.", hint="Use f'(x) = 2x and simplify.",
             feedback=["The derivative of $x^2 - 5$ is $2x$, not $x$.", "", "The sign is wrong: the formula subtracts $f/f'$.", "That is just one half of the iteration and misses the average."]),
        QUIZ(r"Newton-Raphson on $f(x) = x^3 - 2x - 5$ gives iterates $2,\ 2.1,\ 2.09457,\ 2.0945515$. The error is about $0.0945,\ 0.0054,\ 0.000017$. What does this show?",
             ["The error halves each step", "The number of correct digits roughly doubles each step", "The error decreases by $0.09$ each step", "The method is slower than bisection"], 1,
             r"$0.0054 \approx 0.0945^2 \times 0.6$ and $0.000017 \approx 0.0054^2 \times 0.6$: each error is about a constant times the square of the previous one.", hint="Compare each error with the square of the one before.",
             feedback=["That is bisection.", "", "The errors fall by far more than a fixed amount.", "Here it is much faster."]),
        H("Practice questions"),
        PQ(r"Show that $x^3 - 3x - 1 = 0$ has a root between $1$ and $2$ and perform two Newton-Raphson steps from $x_0 = 2$.",
           r"$f(1) = -3 < 0$, $f(2) = 1 > 0$, continuous, so a root lies in $(1, 2)$. $f'(x) = 3x^2 - 3$. $x_1 = 2 - \dfrac{1}{9} = 1.8889$. $f(1.8889) = 6.7394 - 5.6667 - 1 = 0.0727$ and $f'(1.8889) = 7.7037$, so $x_2 = 1.8889 - 0.00944 = 1.8794$."),
        PQ(r"Use Newton-Raphson on $f(x) = x^2 - 10$ with $x_0 = 3$ to find $\sqrt{10}$ to 6 significant figures.",
           r"$x_{n+1} = \frac{1}{2}(x_n + 10/x_n)$. $x_1 = \frac{1}{2}(3 + 3.33333) = 3.166667$. $x_2 = \frac{1}{2}(3.166667 + 3.157895) = 3.162281$. $x_3 = \frac{1}{2}(3.162281 + 3.162275) = 3.162278$. So $\sqrt{10} = 3.16228$ to 6 s.f."),
        PQ(r"Explain what goes wrong when Newton-Raphson is applied to $f(x) = x^3 - 2x + 2$ with $x_0 = 0$.",
           r"$f(0) = 2$, $f'(0) = -2$ so $x_1 = 0 - \frac{2}{-2} = 1$. Then $f(1) = 1$, $f'(1) = 1$ so $x_2 = 1 - 1 = 0$. The iterates alternate $0, 1, 0, 1, \ldots$ and never converge: a cycle. (The real root is near $-1.77$; a start closer to it would work.)"),
        PQ(r"The equation $\cos x = 2x$ has a root near $0.45$. Use one step of Newton-Raphson from $x_0 = 0.5$.",
           r"$f(x) = \cos x - 2x$, $f'(x) = -\sin x - 2$. $f(0.5) = 0.87758 - 1 = -0.12242$, $f'(0.5) = -0.47943 - 2 = -2.47943$. $x_1 = 0.5 - \dfrac{-0.12242}{-2.47943} = 0.5 - 0.04938 = 0.45062$."),
        H("Summary"),
        SUM(r"Newton-Raphson: $x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}$, the $x$-intercept of the tangent.",
            "When it works, the number of correct digits roughly doubles each step (quadratic convergence).",
            r"For $\sqrt{a}$: $x_{n+1} = \frac{1}{2}(x_n + a/x_n)$.",
            r"It fails when $f'(x_n)$ is near zero, when the iterates cycle, or when the start is near the wrong root.",
            "Show the table, keep extra decimals, and stop when successive values agree to the required accuracy."),
    ],
))

# ---------------------------------------------------------------- Numerical integration
_f4 = lambda x: 4 / (1 + x * x)  # noqa: E731
_g1 = lambda x: math.exp(-x * x)  # noqa: E731
_ORD = "\n".join([f"x = {i / 4:.2f}   y = {_f4(i / 4):.5f}" for i in range(5)])
_T4, _S4, _T2, _S2 = _trap(_f4, 0, 1, 4), _simp(_f4, 0, 1, 4), _trap(_f4, 0, 1, 2), _simp(_f4, 0, 1, 2)
assert abs(_T4 - 3.13118) < 1e-5 and abs(_S4 - 3.14157) < 1e-5 and abs(_T2 - 3.1) < 1e-9 and abs(_S2 - 3.13333) < 1e-5
assert abs(_simp(_g1, 0, 1, 4) - 0.74686) < 1e-5 and abs(_trap(_g1, 0, 1, 4) - 0.74298) < 1e-5
_DEPTH = [0, 1.2, 2.1, 2.6, 2.2, 1.4, 0]
assert abs((2 / 2) * (sum(_DEPTH[0::6]) + 2 * sum(_DEPTH[1:-1])) - 19.0) < 1e-9
assert abs(2 / 3 * (0 + 0 + 4 * (1.2 + 2.6 + 1.4) + 2 * (2.1 + 2.2)) - 19.6) < 1e-9

LESSONS.append(lesson(
    module=NM, topic="Numerical integration",
    title="The trapezium rule and Simpson's rule",
    slug="fmu2-trapezium-simpson-rules",
    minutes=24,
    summary="Estimate definite integrals from ordinates with the trapezium rule and Simpson's rule, choose the number of strips correctly, compare accuracy and recognise over- and under-estimates.",
    objectives=[
        "Apply the trapezium rule and Simpson's rule with the correct step length h",
        "Explain why Simpson's rule needs an even number of strips and why it is usually more accurate",
        "Use tabulated data, not only formulas, to estimate an area",
        "Decide whether the trapezium rule over- or under-estimates, and improve an estimate by halving the step",
    ],
    key_concepts=["Strip width h", "Ordinates", "Trapezium rule", "Simpson's rule", "Error", "Convex and concave"],
    blocks=[
        H("Introduction"),
        T(r"A civil engineer in Maroua wants the area of a river's cross-section to decide how much water flows through it. She measures the depth every 2 metres across. There is no formula for the river bed, only a table of numbers. To find the area she must **estimate an integral from data**. The same idea is used when $\int f(x)\,dx$ cannot be found by hand, such as $\int e^{-x^2}\,dx$."),
        H("Strips and ordinates"),
        D(r"To estimate $\int_a^b y\,dx$ divide $[a, b]$ into $n$ **strips** of equal width $h = \dfrac{b - a}{n}$. This gives $n + 1$ **ordinates** (heights) $y_0, y_1, \dots, y_n$ at $x_k = a + kh$.", title="Strips and ordinates",
          note="n strips give n + 1 ordinates. The most common slip is using h = (b - a)/(n + 1), or counting strips as ordinates."),
        D(r"Join the tops of the ordinates by straight lines: each strip is a trapezium of area $\frac{h}{2}(y_{k-1} + y_k)$. Adding them:", title="The trapezium rule",
          formula=r"\int_a^b y\,dx \approx \frac{h}{2}\Big[\,y_0 + y_n + 2\,(y_1 + y_2 + \dots + y_{n-1})\Big]",
          note="First and last ordinates once, every other ordinate twice."),
        D(r"Replace the curve over each **pair** of strips by a parabola through three ordinates. This needs an **even** number of strips.", title="Simpson's rule",
          formula=r"\int_a^b y\,dx \approx \frac{h}{3}\Big[\,y_0 + y_n + 4\,(y_1 + y_3 + \dots + y_{n-1}) + 2\,(y_2 + y_4 + \dots + y_{n-2})\Big]",
          note="First and last once, odd-numbered ordinates times 4, even-numbered inner ordinates times 2. The pattern 1, 4, 2, 4, 2, ..., 4, 1."),
        IMG("al-fmu2-trapezium-simpson.svg", alt="Left: a curve over four strips approximated by straight-line tops (trapezia). Right: the same curve over two pairs of strips approximated by parabolic arcs.", caption="Figure 2. The trapezium rule uses straight tops over each strip; Simpson's rule uses a parabola over each pair of strips."),
        EX("Worked example 1: estimating pi", intro=r"Use four strips to estimate $\displaystyle\int_0^1 \frac{4}{1 + x^2}\,dx$ with (a) the trapezium rule and (b) Simpson's rule. The exact value is $\pi = 3.14159$.", steps=[
            S("Step length and ordinates", math=r"h = \frac{1 - 0}{4} = 0.25", text="Five ordinates, shown in the table below."),
            S("(a) Trapezium", math=r"T_4 = \frac{0.25}{2}\big[4 + 2 + 2(3.76471 + 3.2 + 2.56)\big] = 0.125 \times 25.04941 = 3.13118"),
            S("(b) Simpson", math=r"S_4 = \frac{0.25}{3}\big[4 + 2 + 4(3.76471 + 2.56) + 2(3.2)\big] = \frac{0.25}{3} \times 37.69882 = 3.14157"),
            S("Compare with $\\pi$", text=r"The trapezium error is $0.0104$. Simpson's error is $0.00002$: over 400 times smaller with the same ordinates."),
        ], check=r"T_2 = \frac{0.5}{2}[4 + 2 + 2(3.2)] = 3.1, \qquad S_2 = \frac{0.5}{3}[4 + 2 + 4(3.2)] = 3.1333"),
        CODE(_ORD, "text", title="Table 6. Ordinates of y = 4/(1 + x^2) (computed by program)"),
        H("Why Simpson is better, and how to improve an estimate"),
        T(r"The trapezium rule has error proportional to $h^2$: halving $h$ cuts the error by about 4. Simpson's rule has error proportional to $h^4$: halving $h$ cuts it by about 16. Simpson's rule is **exact for polynomials up to degree 3**. For $\int_0^1 x^3\,dx$ it gives exactly $\frac14$ with two strips; the trapezium rule would give $\frac12\left[0 + 1 + 2\cdot\frac18\right]\cdot\frac12 = 0.3125$."),
        T(r"**Which side?** If the curve is **convex** (bends upwards, $f'' > 0$), the straight tops lie above it and the trapezium rule **over-estimates**. If the curve is concave ($f'' < 0$), it under-estimates. For $y = x^2$ with two strips, $T = 0.375$ against the exact $\frac13$; Simpson gives $\frac13$ exactly."),
        T(r"**Improving an estimate.** From $T_2 = 3.1$ and $T_4 = 3.13118$ the combination $\dfrac{4T_4 - T_2}{3}$ gives $3.14157$, which is exactly $S_4$. Simpson's rule is a weighted average of two trapezium estimates."),
        EX("Worked example 2: area from measured data", intro=r"A river is 12 m wide. Its depth (invented measurements, in metres) at 2 m intervals from one bank is $0,\ 1.2,\ 2.1,\ 2.6,\ 2.2,\ 1.4,\ 0$. Estimate the cross-section area with Simpson's rule and the trapezium rule.", steps=[
            S("Strips and step", math=r"n = 6 \text{ strips (7 ordinates)}, \quad h = 2", text="Six strips: an even number, so Simpson's rule is allowed."),
            S("Simpson", math=r"A \approx \frac{2}{3}\big[0 + 0 + 4(1.2 + 2.6 + 1.4) + 2(2.1 + 2.2)\big] = \frac{2}{3}(29.4) = 19.6\ \text{m}^2"),
            S("Trapezium", math=r"A \approx \frac{2}{2}\big[0 + 0 + 2(1.2 + 2.1 + 2.6 + 2.2 + 1.4)\big] = 19.0\ \text{m}^2"),
            S("Interpret", text="The two estimates differ by 0.6 m$^2$. The river bed is curved (concave from above), so the trapezium rule slightly under-estimates; Simpson's value is the better estimate."),
        ]),
        EX("Worked example 3: a non-elementary integral", intro=r"Estimate $\displaystyle\int_0^1 e^{-x^2}\,dx$ with four strips using both rules.", steps=[
            S("Ordinates ($h = 0.25$)", math=r"y = 1,\ 0.93941,\ 0.77880,\ 0.56978,\ 0.36788"),
            S("Trapezium", math=r"T_4 = 0.125\,[1 + 0.36788 + 2(2.28800)] = 0.74298"),
            S("Simpson", math=r"S_4 = \tfrac{0.25}{3}\,[1 + 0.36788 + 4(1.50919) + 2(0.77880)] = 0.74686"),
            S("Compare", text=r"The true value is $0.74682$. Simpson is within $0.0001$ of it (error about $0.00004$); the trapezium rule is only within $0.004$."),
        ]),
        MISTAKE("Mixing up the two rules (a common error in the Board's report)", r"Candidates sometimes apply the trapezium pattern $1, 2, 2, \ldots, 1$ when asked for Simpson's rule, or write Simpson's weights $1, 4, 2, 4, 1$ with the factor $\frac{h}{2}$. Remember: trapezium has $\frac{h}{2}$ and all inner ordinates doubled; Simpson has $\frac{h}{3}$ and the pattern 4, 2, 4, 2, ..., 4."),
        MISTAKE("Wrong step length or an odd number of strips", r"With $n$ strips, $h = \dfrac{b - a}{n}$. For $\int_0^2$ with five ordinates, $n = 4$ and $h = 0.5$, not $0.4$. Simpson's rule needs an **even** number of strips, which means an **odd** number of ordinates."),
        MISTAKE("Rounding the ordinates too early", "Keep at least 5 decimal places in the ordinates. An estimate quoted to 4 d.p. can be spoiled by ordinates rounded to 3."),
        QUIZ(r"Simpson's rule is used with $\int_0^6$ and $h = 1.5$. How many ordinates are needed, and is the number of strips acceptable?",
             ["$4$ ordinates, acceptable", "$5$ ordinates, acceptable (4 strips)", "$6$ ordinates, acceptable", "$5$ ordinates, not acceptable"], 1,
             r"$n = 6 / 1.5 = 4$ strips (even, so allowed), giving $4 + 1 = 5$ ordinates.", hint="n = (b - a)/h, then add 1.",
             feedback=["Four is the number of strips, not ordinates.", "", "That is $n = 5$ strips: odd, so Simpson's rule cannot be applied.", "Four strips is an even number, which is allowed."]),
        QUIZ(r"A curve is convex (it bends upwards) on $[a, b]$. The trapezium rule estimate is:",
             ["always exact", "an under-estimate", "an over-estimate", "an under-estimate only when n is even"], 2,
             "On a convex curve the chords lie above the curve, so the trapezium areas are too large.", hint="Sketch a U-shaped curve and a chord.",
             feedback=["It is exact only for straight lines.", "That is the case for a concave curve.", "", "The parity of n does not decide the direction of the error."]),
        H("Practice questions"),
        PQ(r"Use the trapezium rule with four strips to estimate $\displaystyle\int_1^3 \frac{1}{x}\,dx$ and compare with the exact value.",
           r"$h = 0.5$; ordinates $1,\ 0.66667,\ 0.5,\ 0.4,\ 0.33333$. $T_4 = 0.25[1 + 0.33333 + 2(1.56667)] = 0.25 \times 4.46667 = 1.11667$. Exact: $\ln 3 = 1.09861$. The estimate is high (over-estimate) because $1/x$ is convex."),
        PQ(r"Use Simpson's rule with four strips on the same integral.",
           r"$S_4 = \frac{0.5}{3}[1 + 0.33333 + 4(0.66667 + 0.4) + 2(0.5)] = \frac{0.5}{3}(6.6) = 1.1000$. Error $0.0014$, far smaller than the trapezium error $0.018$."),
        PQ(r"The table gives the speed $v$ (m/s) of a taxi on a straight road at 5-second intervals: $0,\ 4,\ 9,\ 12,\ 14$ at $t = 0, 5, 10, 15, 20$ (invented data). Estimate the distance travelled by Simpson's rule.",
           r"Four strips, $h = 5$: $s \approx \frac{5}{3}[0 + 14 + 4(4 + 12) + 2(9)] = \frac{5}{3}(96) = 160$ m. (Trapezium: $\frac{5}{2}[14 + 2(25)] = 160$ m too, by coincidence of this data.)"),
        PQ(r"Show that Simpson's rule with two strips is exact for $\int_0^2 x^3\,dx$.",
           r"$h = 1$. $S = \frac{1}{3}[0 + 8 + 4(1)] = \frac{12}{3} = 4$. Exact: $\left[\frac{x^4}{4}\right]_0^2 = 4$."),
        H("Summary"),
        SUM(r"With $n$ strips, $h = (b - a)/n$ and there are $n + 1$ ordinates.",
            r"Trapezium: $\frac{h}{2}[\text{ends} + 2(\text{inner})]$. Simpson: $\frac{h}{3}[\text{ends} + 4(\text{odd}) + 2(\text{even inner})]$, with $n$ even.",
            r"Error $\propto h^2$ for the trapezium rule and $\propto h^4$ for Simpson, which is exact up to cubics.",
            "A convex curve makes the trapezium rule over-estimate; a concave curve, under-estimate.",
            "Keep ordinates to 5 decimal places and show the table."),
    ],
))

# ---------------------------------------------------------------- Numerical ODEs
_fx = lambda x, y: x + y  # noqa: E731
_EU = _ode_table(_fx, 0, 1, 0.1, 5, "e")
_HE = _ode_table(_fx, 0, 1, 0.1, 5, "h")
_RK = _ode_table(_fx, 0, 1, 0.1, 5, "r")
_EXACT = lambda x: 2 * math.exp(x) - x - 1  # noqa: E731
_ODE_TAB = "  x     Euler    Improved   RK4     Exact\n" + "\n".join(
    f"{_EU[i][0]:.1f}  {_EU[i][1]:8.5f} {_HE[i][1]:8.5f} {_RK[i][1]:8.5f} {_EXACT(_EU[i][0]):8.5f}" for i in range(6))
assert abs(_EU[5][1] - 1.72102) < 1e-5 and abs(_HE[5][1] - 1.79489) < 1e-5 and abs(_RK[5][1] - 1.79744) < 1e-5

LESSONS.append(lesson(
    module=NM, topic="Numerical solution of differential equations",
    title="Euler's method, improved Euler and Runge-Kutta",
    slug="fmu2-euler-improved-euler-runge-kutta",
    minutes=25,
    summary="Solve dy/dx = f(x, y) step by step with Euler's method, the improved Euler method and fourth-order Runge-Kutta, compare their accuracy and see the effect of the step size.",
    objectives=[
        "Apply Euler's method y_(n+1) = y_n + h f(x_n, y_n) and present a table of values",
        "Apply the improved Euler (predictor-corrector) method",
        "Carry out one step of the fourth-order Runge-Kutta method",
        "Compare the methods with an exact solution and explain the effect of halving the step size",
    ],
    key_concepts=["Initial value problem", "Euler's method", "Improved Euler method", "Runge-Kutta", "Step size", "Truncation error"],
    blocks=[
        H("Introduction"),
        T(r"A kettle of tea cools, a population grows, a tank empties. Each is described by a differential equation $\dfrac{dy}{dx} = f(x, y)$ with a known starting value. Often no formula solves it, but we can always **walk along the solution** in small steps: use the gradient where you stand to decide where to step next."),
        H("Euler's method"),
        D(r"For $\dfrac{dy}{dx} = f(x, y)$ with $y(x_0) = y_0$ and step $h$, follow the tangent for a distance $h$:", title="Euler's method",
          formula=r"y_{n+1} = y_n + h\,f(x_n, y_n), \qquad x_{n+1} = x_n + h",
          note="This is the first two terms of the Taylor series of y(x + h). The error in one step is of order h squared, and over a fixed interval the total error is of order h."),
        EX("Worked example 1: Euler's method", intro=r"Solve $\dfrac{dy}{dx} = x + y$, $y(0) = 1$, with $h = 0.1$, to estimate $y(0.3)$.", steps=[
            S("Step 1 ($x_0 = 0$, $y_0 = 1$)", math=r"f = 0 + 1 = 1, \quad y_1 = 1 + 0.1(1) = 1.1"),
            S("Step 2 ($x_1 = 0.1$, $y_1 = 1.1$)", math=r"f = 0.1 + 1.1 = 1.2, \quad y_2 = 1.1 + 0.12 = 1.22"),
            S("Step 3 ($x_2 = 0.2$, $y_2 = 1.22$)", math=r"f = 0.2 + 1.22 = 1.42, \quad y_3 = 1.22 + 0.142 = 1.362"),
        ], check=r"\text{Exact: } y = 2e^x - x - 1,\ y(0.3) = 1.39972"),
        T(r"Euler gives $1.362$ against the exact $1.39972$: an error of $0.038$ after only three steps. The curve is bending upwards, so the tangent always falls below it."),
        H("The improved Euler method"),
        D(r"Use the average of the gradients at both ends of the step. First **predict** with an Euler step, then **correct** with the mean gradient:", title="Improved Euler (predictor-corrector)",
          formula=r"y^*_{n+1} = y_n + h\,f(x_n, y_n), \qquad y_{n+1} = y_n + \frac{h}{2}\Big[f(x_n, y_n) + f(x_{n+1}, y^*_{n+1})\Big]",
          note="Some books call this Heun's method or a second-order Runge-Kutta method. The error over a fixed interval is of order h squared."),
        EX("Worked example 2: improved Euler, first step", intro=r"Apply one step to $\dfrac{dy}{dx} = x + y$, $y(0) = 1$, $h = 0.1$.", steps=[
            S("Predict", math=r"y^* = 1 + 0.1(1) = 1.1"),
            S("Gradient at the predicted point", math=r"f(0.1,\ 1.1) = 1.2"),
            S("Correct with the average gradient", math=r"y_1 = 1 + 0.05\,(1 + 1.2) = 1.11"),
        ], check=r"\text{Exact: } y(0.1) = 1.11034"),
        H("Fourth-order Runge-Kutta"),
        D(r"The classical fourth-order method takes four gradient estimates in each step and combines them:", title="Runge-Kutta (RK4)",
          formula=r"k_1 = f(x_n, y_n),\quad k_2 = f\!\left(x_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2}k_1\right),\quad k_3 = f\!\left(x_n + \tfrac{h}{2},\, y_n + \tfrac{h}{2}k_2\right),\quad k_4 = f(x_n + h,\, y_n + hk_3)",
          note=r"Then $y_{n+1} = y_n + \dfrac{h}{6}\,(k_1 + 2k_2 + 2k_3 + k_4)$. The error over a fixed interval is of order $h^4$."),
        EX("Worked example 3: one RK4 step", intro=r"Apply one RK4 step to $\dfrac{dy}{dx} = x + y$, $y(0) = 1$, $h = 0.1$.", steps=[
            S("$k_1$", math=r"k_1 = f(0, 1) = 1"),
            S("$k_2$", math=r"k_2 = f(0.05,\ 1 + 0.05) = 0.05 + 1.05 = 1.1"),
            S("$k_3$", math=r"k_3 = f(0.05,\ 1 + 0.055) = 0.05 + 1.055 = 1.105"),
            S("$k_4$", math=r"k_4 = f(0.1,\ 1 + 0.1105) = 0.1 + 1.1105 = 1.2105"),
            S("Combine", math=r"y_1 = 1 + \tfrac{0.1}{6}\,(1 + 2.2 + 2.21 + 1.2105) = 1 + \tfrac{0.1}{6}(6.6205) = 1.11034"),
        ], check=r"\text{Exact: } y(0.1) = 2e^{0.1} - 1.1 = 1.11034"),
        CODE(_ODE_TAB, "text", title="Table 7. dy/dx = x + y, y(0) = 1, h = 0.1 (computed by program)"),
        T(r"At $x = 0.5$ the errors are about $0.0764$ for Euler, $0.0026$ for improved Euler and under $0.00001$ for RK4. The price: Euler uses 1 evaluation of $f$ per step, the improved method 2, and RK4 4."),
        H("The effect of the step size"),
        T(r"For the same problem at $x = 0.5$, Euler's error is $0.0764$ with $h = 0.1$, $0.0397$ with $h = 0.05$ and $0.0202$ with $h = 0.025$. **Halving the step halves the error** for Euler (first order), quarters it for improved Euler and divides it by 16 for RK4. But a step too large can make Euler useless. A cooling cup of tea has $\dfrac{dT}{dt} = -0.1(T - 25)$, $T(0) = 90$. With one step of $h = 5$ minutes:"),
        CODE("Euler           T(5) = 90 + 5(-0.1)(65)          = 57.500\nImproved Euler  T(5) = 90 + 2.5(-6.5 - 3.25)      = 65.625\nRK4             T(5) = 64.440\nExact           T(5) = 25 + 65 e^(-0.5)           = 64.424", "text", title="One large step (computed by program)"),
        MISTAKE("Using the new y in Euler's gradient", r"In $y_{n+1} = y_n + hf(x_n, y_n)$ the gradient uses the **old** point $(x_n, y_n)$. Using $y_{n+1}$ makes the equation implicit, which is a different method."),
        MISTAKE("Forgetting to move x", r"Each step increases $x$ by $h$ as well as updating $y$. For $f(x, y) = x + y$ forgetting this keeps $x = 0$ throughout and gives wrong gradients. Keep a column for $x$ in your table."),
        MISTAKE("Mixing up the improved Euler with the Euler method", r"The improved method needs $f$ at **two** points in each step and averages the gradients: the second uses the predicted $y^*$, not the old $y_n$."),
        QUIZ(r"Euler's method, $h = 0.2$, is applied to $\dfrac{dy}{dx} = 2y$ with $y(0) = 3$. What is $y_1$?",
             ["$3.6$", "$4.2$", "$3.2$", "$9$"], 1,
             r"$f(0, 3) = 6$, so $y_1 = 3 + 0.2 \times 6 = 4.2$.", hint="Work out the gradient f(x0, y0) first.",
             feedback=["That uses the gradient 3 (the value of $y$) instead of $2y = 6$.", "", "That is $3 + 0.2$, forgetting to multiply by the gradient.", "That adds the gradient itself, $3 + 6$, without multiplying by the step size $h$."]),
        QUIZ(r"The step size of Euler's method is halved. The global error at a fixed $x$ will approximately:",
             ["halve", "quarter", "stay the same", "double"], 0,
             "Euler's method is first order: the global error is proportional to $h$.", hint="Think about the error order of Euler's method over a fixed interval.",
             feedback=["", "That is the improved Euler method, whose error is order $h^2$.", "A smaller step gives a smaller error.", "A smaller step reduces the error, not increases it."]),
        H("Practice questions"),
        PQ(r"Use Euler's method with $h = 0.2$ to estimate $y(0.4)$ for $\dfrac{dy}{dx} = x^2 + y$ with $y(0) = 1$.",
           r"Step 1: $f(0, 1) = 1$, $y_1 = 1 + 0.2 = 1.2$. Step 2: $f(0.2, 1.2) = 0.04 + 1.2 = 1.24$, $y_2 = 1.2 + 0.248 = 1.448$. So $y(0.4) \approx 1.448$."),
        PQ(r"Apply one step of the improved Euler method to the problem above with $h = 0.2$.",
           r"Predict: $y^* = 1.2$. Gradient at $(0.2, 1.2)$: $1.24$. Correct: $y_1 = 1 + 0.1(1 + 1.24) = 1.224$."),
        PQ(r"Apply one step of RK4 to $\dfrac{dy}{dx} = y$, $y(0) = 1$, with $h = 0.5$ and compare with $e^{0.5}$.",
           r"$k_1 = 1$; $k_2 = 1 + 0.25 = 1.25$; $k_3 = 1 + 0.25(1.25) = 1.3125$; $k_4 = 1 + 0.5(1.3125) = 1.65625$. $y_1 = 1 + \frac{0.5}{6}(1 + 2.5 + 2.625 + 1.65625) = 1 + \frac{0.5}{6}(7.78125) = 1.648438$. Exact $e^{0.5} = 1.648721$: the error is $0.0003$ even with one large step."),
        PQ(r"The solution of $\dfrac{dy}{dx} = x + y$ is concave up. Explain why Euler's method gives an under-estimate here.",
           r"Euler follows the tangent at the start of each step. For a curve bending upwards the tangent lies below the curve, so each step lands below the true curve, and the errors accumulate."),
        H("Summary"),
        SUM(r"Euler: $y_{n+1} = y_n + hf(x_n, y_n)$, a step along the tangent; global error $\propto h$.",
            r"Improved Euler: predict with Euler, then use the average of the gradients at both ends; error $\propto h^2$.",
            r"RK4: $y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$; error $\propto h^4$.",
            "Tabulate x and y at every step, keep extra decimals and move x each time.",
            "Smaller steps are more accurate; higher-order methods gain more per evaluation of f."),
    ],
))


# ================================================================ Advanced mechanics
LESSONS.append(lesson(
    module=MP, topic="Kinematics in polar coordinates",
    title="Velocity and acceleration in polar coordinates",
    slug="fmu2-polar-kinematics",
    minutes=24,
    summary="Describe motion by distance r from a fixed point and angle theta, derive the radial and transverse components of velocity and acceleration, and apply them to spirals, rotating rods and central motion.",
    objectives=[
        "Define the radial and transverse unit vectors and their rates of change",
        "State and use the polar components of velocity and acceleration",
        "Interpret the terms r theta-dot squared and 2 r-dot theta-dot physically",
        "Use the fact that no transverse force means r squared times theta-dot is constant",
    ],
    key_concepts=["Radial and transverse components", "Unit vectors r-hat and theta-hat", "Centripetal term", "Coriolis term", "Angular momentum per unit mass"],
    blocks=[
        H("Introduction"),
        T(r"A beetle crawls outward along a spoke of a spinning bicycle wheel. A sprinkler head sends water along a rotating arm. In both cases the natural description of position is not $(x, y)$ but **how far** from the centre ($r$) and **in which direction** ($\theta$). Using these polar coordinates for velocity and acceleration makes rotating problems much simpler."),
        H("Radial and transverse unit vectors"),
        D(r"At a point $P(r, \theta)$ define the **radial** unit vector $\hat{\mathbf{r}}$, pointing directly away from the origin $O$, and the **transverse** unit vector $\hat{\boldsymbol{\theta}}$, at right angles to it in the direction of increasing $\theta$. In Cartesian components:", title="Unit vectors",
          formula=r"\hat{\mathbf{r}} = (\cos\theta,\ \sin\theta), \qquad \hat{\boldsymbol{\theta}} = (-\sin\theta,\ \cos\theta)"),
        IMG("al-fmu2-polar-components.svg", alt="A point P at distance r from O on a line at angle theta to the initial line, with the radial unit vector along OP and the transverse unit vector at right angles to it.", caption="Figure 1. The radial and transverse unit vectors at P."),
        T(r"Unlike $\mathbf{i}$ and $\mathbf{j}$, these unit vectors **change direction** as $P$ moves. Differentiating with respect to time (chain rule) gives the key facts:"),
        F(r"\dot{\hat{\mathbf{r}}} = \dot\theta\,\hat{\boldsymbol{\theta}}, \qquad \dot{\hat{\boldsymbol{\theta}}} = -\dot\theta\,\hat{\mathbf{r}}", title="Rates of change"),
        H("Velocity and acceleration"),
        T(r"The position vector is $\mathbf{r} = r\,\hat{\mathbf{r}}$. Differentiate with the product rule:"),
        F(r"\mathbf{v} = \dot r\,\hat{\mathbf{r}} + r\dot{\hat{\mathbf{r}}} = \dot r\,\hat{\mathbf{r}} + r\dot\theta\,\hat{\boldsymbol{\theta}}"),
        T(r"Differentiate again, using the rates of change above:"),
        F(r"\mathbf{a} = (\ddot r - r\dot\theta^2)\,\hat{\mathbf{r}} + (r\ddot\theta + 2\dot r\dot\theta)\,\hat{\boldsymbol{\theta}}"),
        KEY("Polar components", "Memorise these four expressions.", cards=[
            ["Radial velocity", r"$v_r = \dot r$ (speed of moving away from $O$)"],
            ["Transverse velocity", r"$v_\theta = r\dot\theta$ (speed of turning round $O$)"],
            ["Radial acceleration", r"$a_r = \ddot r - r\dot\theta^2$. The term $-r\dot\theta^2$ is the centripetal acceleration."],
            ["Transverse acceleration", r"$a_\theta = r\ddot\theta + 2\dot r\dot\theta = \dfrac{1}{r}\dfrac{d}{dt}\left(r^2\dot\theta\right)$"],
        ]),
        T(r"**Meaning.** For motion in a circle of constant radius $r = a$ ($\dot r = 0$) at constant $\dot\theta = \omega$, the formulae give $a_r = -a\omega^2$ and $a_\theta = 0$: the familiar acceleration $a\omega^2$ towards the centre. The term $2\dot r\dot\theta$ is extra: it appears when the particle moves outward along a turning line (the Coriolis term). The speed is $\sqrt{v_r^2 + v_\theta^2}$: the components are **not** speeds on their own."),
        EX("Worked example 1: a beetle on a turntable", intro=r"A beetle crawls outward along a radial line painted on a turntable rotating at a constant $2$ rad/s. Its distance from the centre is $r = 0.3 + 0.5t$ metres. Find its acceleration components and speed at $t = 0$.", steps=[
            S("Data", math=r"r = 0.3,\ \dot r = 0.5,\ \ddot r = 0,\ \dot\theta = 2,\ \ddot\theta = 0"),
            S("Radial acceleration", math=r"a_r = 0 - 0.3(2)^2 = -1.2\ \text{m/s}^2", text="Negative: towards the centre."),
            S("Transverse acceleration", math=r"a_\theta = 0 + 2(0.5)(2) = 2\ \text{m/s}^2"),
            S("Magnitude of the acceleration", math=r"|\mathbf{a}| = \sqrt{1.2^2 + 2^2} = 2.33\ \text{m/s}^2"),
            S("Speed", math=r"v = \sqrt{0.5^2 + (0.3 \times 2)^2} = \sqrt{0.61} = 0.781\ \text{m/s}"),
        ], check=r"\text{Numerical differentiation of } (x, y) = r(\cos\theta, \sin\theta) \text{ gives the same values}"),
        EX("Worked example 2: a spiral", intro=r"A particle moves so that $r = 2t$ and $\theta = t$ (metres, radians, seconds). Find its velocity and acceleration components at $t = 1$.", steps=[
            S("Derivatives", math=r"\dot r = 2,\ \ddot r = 0,\ \dot\theta = 1,\ \ddot\theta = 0, \quad r = 2 \text{ at } t = 1"),
            S("Velocity", math=r"v_r = 2, \quad v_\theta = r\dot\theta = 2, \quad v = \sqrt{8} = 2.83\ \text{m/s}"),
            S("Acceleration", math=r"a_r = 0 - 2(1)^2 = -2, \quad a_\theta = 0 + 2(2)(1) = 4\ \text{m/s}^2"),
            S("Magnitude", math=r"|\mathbf{a}| = \sqrt{4 + 16} = \sqrt{20} = 4.47\ \text{m/s}^2"),
        ], check=r"\text{Check: } \mathbf{r} = 2t(\cos t, \sin t) \text{ differentiated twice at } t=1 \text{ gives } a_r = -2,\ a_\theta = 4"),
        EX("Worked example 3: a cardioid path", intro=r"A particle moves on the curve $r = a(1 + \cos\theta)$ with constant $\dot\theta = \omega$. Show that $v^2 = 2a^2\omega^2(1 + \cos\theta)$ and find the radial acceleration when $a = 1$, $\omega = 2$, $\theta = \dfrac{\pi}{3}$.", steps=[
            S("Differentiate $r$", math=r"\dot r = -a\sin\theta\,\dot\theta = -a\omega\sin\theta"),
            S("Speed squared", math=r"v^2 = \dot r^2 + r^2\dot\theta^2 = a^2\omega^2\left[\sin^2\theta + (1 + \cos\theta)^2\right] = 2a^2\omega^2(1 + \cos\theta)"),
            S("Second derivative of $r$", math=r"\ddot r = -a\omega^2\cos\theta"),
            S("Radial acceleration", math=r"a_r = \ddot r - r\dot\theta^2 = -a\omega^2\cos\theta - a\omega^2(1 + \cos\theta) = -a\omega^2(1 + 2\cos\theta)"),
            S("Put $a = 1$, $\\omega = 2$, $\\theta = \\pi/3$ ($\\cos\\theta = \\tfrac12$)", math=r"a_r = -4(1 + 1) = -8\ \text{m/s}^2"),
        ], check=r"\text{At } \theta = \tfrac{\pi}{3}:\ v_r = -\sqrt3,\ v_\theta = 3,\ v^2 = 12 = 2(1)(4)(1.5)\ \checkmark"),
        H("When there is no transverse force"),
        T(r"The transverse acceleration can be written $a_\theta = \dfrac{1}{r}\dfrac{d}{dt}\big(r^2\dot\theta\big)$. If the force on the particle is always directed towards $O$ (a central force), $a_\theta = 0$ and so $r^2\dot\theta$ is constant. This is the conservation of angular momentum per unit mass: $h = r^2\dot\theta$. When the particle comes closer, it spins faster. For example, if $r = 4$ m and $\dot\theta = 0.5$ rad/s, then $h = 8$ and at $r = 2$ m, $\dot\theta = \dfrac{8}{4} = 2$ rad/s."),
        MISTAKE("Dropping the 2 r-dot theta-dot term", r"When the particle moves along a **turning** line, $\dot r \neq 0$ and $\dot\theta \neq 0$, so the transverse acceleration is **not** just $r\ddot\theta$. In Example 1 $\ddot\theta = 0$ but $a_\theta = 2$ m/s$^2$. Forgetting $2\dot r\dot\theta$ is the most common slip."),
        MISTAKE("Treating components as speeds, or the radial acceleration as r-double-dot", r"The speed is $\sqrt{v_r^2 + v_\theta^2}$, not one of the components. And $a_r = \ddot r - r\dot\theta^2$, not just $\ddot r$. (The Board's report notes that candidates mistake components of velocity for speed.)"),
        MISTAKE("Using constant-acceleration formulas", r"Here the acceleration changes with time and position. The formulae $v = u + at$ and $s = ut + \frac12 at^2$ cannot be used: differentiate the given $r(t)$ and $\theta(t)$ instead. The Board's report notes that candidates fail to see when acceleration is variable."),
        QUIZ(r"A particle moves in a circle of radius $0.5$ m at $\dot\theta = 4$ rad/s (constant). What is $a_r$?",
             ["$+8$ m/s$^2$", "$-8$ m/s$^2$", "$-2$ m/s$^2$", "$0$"], 1,
             r"$a_r = \ddot r - r\dot\theta^2 = 0 - 0.5(16) = -8$: towards the centre.", hint="Use a_r = r-double-dot minus r times theta-dot squared with r constant.",
             feedback=["The sign is negative: the acceleration points towards the centre.", "", r"That is $r\dot\theta = 2$ m/s, the speed, not the acceleration.", "A circular motion always has a centripetal acceleration."]),
        QUIZ(r"A particle slides outward along a rod rotating at constant $\dot\theta$, with $\dot r = 3$ m/s. Which expression gives its transverse acceleration?",
             [r"$r\ddot\theta$", r"$\ddot r - r\dot\theta^2$", r"$2\dot r\dot\theta$", r"$r\dot\theta$"], 2,
             r"$a_\theta = r\ddot\theta + 2\dot r\dot\theta$ and $\ddot\theta = 0$, leaving $2\dot r\dot\theta$.", hint="Write the transverse acceleration formula and set the angular acceleration to zero.",
             feedback=["That is zero here because $\\dot\\theta$ is constant.", "That is the radial acceleration.", "", "That is the transverse velocity."]),
        H("Practice questions"),
        PQ(r"A particle moves with $r = 3 + 2t$ and $\theta = t^2$. Find its velocity components, its speed and its acceleration components at $t = 1$.",
           r"$r = 5$, $\dot r = 2$, $\ddot r = 0$, $\dot\theta = 2t = 2$, $\ddot\theta = 2$. $v_r = 2$, $v_\theta = 5(2) = 10$, speed $= \sqrt{104} = 10.2$ m/s. $a_r = 0 - 5(4) = -20$ m/s$^2$. $a_\theta = 5(2) + 2(2)(2) = 18$ m/s$^2$."),
        PQ(r"A particle moves with $r = 0.5e^{t}$ and $\theta = t$. Show that at every instant the radial acceleration is zero and find the transverse acceleration at $t = 0$.",
           r"$\dot r = \ddot r = 0.5e^t = r$, $\dot\theta = 1$, $\ddot\theta = 0$. $a_r = \ddot r - r\dot\theta^2 = r - r = 0$. $a_\theta = 0 + 2r(1) = 2r$; at $t = 0$, $r = 0.5$ so $a_\theta = 1$ m/s$^2$."),
        PQ(r"A particle moves under a force directed towards $O$. At $r = 4$ m it has $\dot\theta = 0.5$ rad/s. Find $\dot\theta$ at $r = 2$ m, and the transverse speed there.",
           r"No transverse force, so $r^2\dot\theta = 16(0.5) = 8$ is constant. At $r = 2$: $\dot\theta = 8/4 = 2$ rad/s. Transverse speed $v_\theta = r\dot\theta = 4$ m/s (it was $2$ m/s at $r = 4$: the transverse speed doubles when $r$ halves)."),
        PQ(r"Show that for the path $r = a$ (constant) with $\dot\theta = \omega(t)$ the acceleration has components $-a\omega^2$ and $a\dot\omega$. Interpret them.",
           r"With $\dot r = \ddot r = 0$: $a_r = -a\omega^2$ and $a_\theta = a\ddot\theta = a\dot\omega$. The first is the centripetal acceleration towards the centre (needed to keep the circular path); the second is the tangential acceleration, which changes the speed $a\omega$ ($\frac{d}{dt}(a\omega) = a\dot\omega$)."),
        H("Summary"),
        SUM(r"$\hat{\mathbf{r}}$ points away from $O$, $\hat{\boldsymbol{\theta}}$ is perpendicular to it; $\dot{\hat{\mathbf{r}}} = \dot\theta\hat{\boldsymbol{\theta}}$ and $\dot{\hat{\boldsymbol{\theta}}} = -\dot\theta\hat{\mathbf{r}}$.",
            r"Velocity: $\dot r\hat{\mathbf{r}} + r\dot\theta\hat{\boldsymbol{\theta}}$. Speed $= \sqrt{\dot r^2 + r^2\dot\theta^2}$.",
            r"Acceleration: $(\ddot r - r\dot\theta^2)\hat{\mathbf{r}} + (r\ddot\theta + 2\dot r\dot\theta)\hat{\boldsymbol{\theta}}$.",
            r"No transverse force: $r^2\dot\theta$ is constant.",
            "Differentiate the given r(t) and theta(t); never use constant-acceleration formulae for variable motion."),
    ],
))

# ---------------------------------------------------------------- Variable mass: rockets
_RK_V = 2000 * math.log(500 / 200) - 10 * 60
assert abs(_RK_V - 1232.58) < 0.01
assert abs(2500 * math.log(4) - 3465.74) < 0.01
LESSONS.append(lesson(
    module=MP, topic="Variable mass systems",
    title="Rockets and other variable-mass systems",
    slug="fmu2-variable-mass-rockets",
    minutes=24,
    summary="Derive the equation of motion of a rocket that ejects burnt fuel, find its thrust, acceleration, velocity and height, and use the logarithmic rocket equation.",
    objectives=[
        "Set up the momentum balance for a body that loses mass and derive m dv/dt = uk - mg",
        "Calculate thrust, initial acceleration and the condition for lift-off",
        "Integrate to obtain the velocity v = u ln(m0/m) - gt and the height reached",
        "Recognise when variable acceleration means the constant-acceleration formulae cannot be used",
    ],
    key_concepts=["Variable mass", "Exhaust speed", "Thrust", "Burn rate", "Rocket equation", "Momentum balance"],
    blocks=[
        H("Introduction"),
        T(r"A satellite launcher leaves the ground weighing hundreds of tonnes, but most of that mass is fuel. As the fuel burns the rocket becomes lighter and accelerates faster. Newton's second law in the form $F = ma$ assumes constant mass, so it cannot be applied directly: we must go back to **momentum**."),
        H("Setting up the equation of motion"),
        T(r"Consider a rocket moving upwards with speed $v$ at time $t$, with mass $m$. In a short time $\delta t$ it ejects fuel of mass $\delta m_f$ backwards at speed $u$ **relative to the rocket**. The rocket mass falls from $m$ to $m - \delta m_f$ and its speed rises from $v$ to $v + \delta v$. The ejected fuel has velocity $v - u$ (upwards positive)."),
        T(r"Momentum before: $mv$. Momentum after: $(m - \delta m_f)(v + \delta v) + \delta m_f(v - u)$. The change of momentum equals the impulse of the external force, $-mg\,\delta t$ (weight, with air resistance neglected):"),
        F(r"(m - \delta m_f)(v + \delta v) + \delta m_f(v - u) - mv = -mg\,\delta t"),
        T(r"Expanding and ignoring the product $\delta m_f\,\delta v$ (negligibly small) gives $m\,\delta v - u\,\delta m_f = -mg\,\delta t$. Divide by $\delta t$ and let $\delta t \to 0$. Write $k = \dfrac{\delta m_f}{\delta t} = -\dfrac{dm}{dt}$, the **burn rate** (mass of fuel ejected per second, positive):"),
        D(r"The motion of a rocket of changing mass $m$, ejecting fuel at rate $k$ with speed $u$ relative to the rocket, in a uniform gravitational field is", title="The rocket equation of motion",
          formula=r"m\,\frac{dv}{dt} = uk - mg \qquad\text{where } k = -\frac{dm}{dt}",
          note=r"The force $uk$ is the **thrust**. The rocket accelerates upwards only if $uk > mg$. Without gravity set $g = 0$."),
        T(r"For a constant burn rate, $m = m_0 - kt$ where $m_0$ is the initial mass. Dividing the equation by $m$ and integrating with respect to $t$ from rest ($v = 0$ at $t = 0$):"),
        F(r"v = \int_0^t \left(\frac{uk}{m_0 - kt} - g\right)dt = u\ln\frac{m_0}{m_0 - kt} - gt = u\ln\frac{m_0}{m} - gt", title="Velocity at time t"),
        EX("Worked example 1: thrust and acceleration at lift-off", intro=r"A rocket has total mass $500$ kg at lift-off, burns fuel at $5$ kg/s and ejects it at $2000$ m/s relative to the rocket. Take $g = 10$ m/s$^2$. Find (a) the thrust, (b) the initial acceleration, (c) the acceleration after $60$ s.", steps=[
            S("(a) Thrust", math=r"uk = 2000 \times 5 = 10\,000\ \text{N}"),
            S("(b) At $t = 0$ the weight is $500 \\times 10 = 5000$ N", math=r"a = \frac{uk - mg}{m} = \frac{10\,000 - 5000}{500} = 10\ \text{m/s}^2", text="Thrust exceeds weight, so it lifts off."),
            S("(c) At $t = 60$ the mass is $500 - 5(60) = 200$ kg", math=r"a = \frac{10\,000 - 200(10)}{200} = 40\ \text{m/s}^2", text="The acceleration has quadrupled: the rocket is lighter but the thrust is unchanged."),
        ], check=r"\text{Constant-acceleration formulae would be wrong: } a \text{ rises from } 10 \text{ to } 40"),
        EX("Worked example 2: speed after 60 seconds", intro=r"For the rocket in Example 1, find its speed after $60$ s, assuming constant $g$ and no air resistance.", steps=[
            S("Mass after 60 s", math=r"m = 500 - 5(60) = 200\ \text{kg}"),
            S("Apply the rocket equation", math=r"v = u\ln\frac{m_0}{m} - gt = 2000\ln\frac{500}{200} - 10(60)"),
            S("Calculate", math=r"= 2000(0.91629) - 600 = 1832.6 - 600 = 1232.6\ \text{m/s}", text=r"About $1.23$ km/s. The rocket carries $400$ kg of fuel, which lasts $80$ s; $60$ s is inside the burn time."),
        ], check=r"\text{Numerical integration of } a = \dfrac{10\,000}{500 - 5t} - 10 \text{ over } 60 \text{ s gives } 1232.6"),
        EX("Worked example 3: a rocket in free space and the height reached", intro=r"(a) A space rocket far from any planet has initial mass $1000$ kg, of which $750$ kg is fuel, ejected at $2500$ m/s relative to the rocket. Find its final speed from rest. (b) For the rocket in Example 1, find the height reached after $60$ s.", steps=[
            S("(a) No gravity: $g = 0$", math=r"v = u\ln\frac{m_0}{m} = 2500\ln\frac{1000}{250} = 2500\ln 4 = 3466\ \text{m/s}", text="Notice the speed depends on the ratio of masses and the exhaust speed, not on the burn rate."),
            S("(b) Integrate the velocity again", math=r"x = \int_0^t v\,dt = u\left[t - \frac{m}{k}\ln\frac{m_0}{m}\right] - \tfrac{1}{2}gt^2",
              text=r"(Using $\int \ln\frac{m_0}{m_0 - k\tau}\,d\tau = \tau - \frac{m}{k}\ln\frac{m_0}{m}$ with $m = m_0 - kt$.)"),
            S("Substitute $u = 2000$, $t = 60$, $m = 200$, $k = 5$", math=r"x = 2000\left[60 - 40\ln 2.5\right] - 5(3600) = 2000(23.348) - 18\,000 = 28\,697\ \text{m}", text="About 28.7 km."),
        ], check=r"\text{Numerical integration of } v(t) \text{ over } 0 \le t \le 60 \text{ gives } 28\,697\ \text{m}"),
        TIP("The answers depend on assumptions: constant $g$ (true to a few percent for the first 30 km), no air resistance and constant burn rate. Real launches differ: always state the assumptions."),
        MISTAKE("Using v = u + at", r"The acceleration of a rocket is not constant: it grows as the mass falls. Using $a = \dfrac{uk - mg}{m}$ evaluated once and then $v = at$ gives a wrong answer. Integrate, or use the logarithmic result."),
        MISTAKE("Mixing up u and the rocket's speed", r"The exhaust speed $u$ is measured **relative to the rocket**, not to the ground. The ground speed of the ejected fuel is $v - u$ (which can even be negative, so fuel falls backwards)."),
        MISTAKE("Using the wrong mass", r"In the weight term and in the division use the **current** mass $m = m_0 - kt$, not the initial mass. Also $\ln\dfrac{m_0}{m}$ has the initial mass on top; swapping gives a negative speed."),
        QUIZ(r"A rocket of mass $2000$ kg burns fuel at $10$ kg/s with exhaust speed $1500$ m/s ($g = 10$ m/s$^2$). Can it lift off?",
             ["No: the thrust 15 000 N is less than the weight 20 000 N", "Yes: the thrust 15 000 N exceeds the weight", "Yes: the thrust 150 N exceeds nothing", "No: the thrust 1500 N is too small"], 0,
             r"Thrust $= uk = 15\,000$ N, weight $= 2000 \times 10 = 20\,000$ N. Thrust $<$ weight, so the rocket stays on the ground.", hint="Compare uk with mg.",
             feedback=["", "15 000 N is less than 20 000 N.", "The thrust is $uk = 1500 \\times 10 = 15\\,000$ N.", "The thrust is $u \\times k$, not $u$ alone."]),
        QUIZ(r"A rocket in free space ($g = 0$) has initial mass $m_0$ and final mass $m_0/e$. Its exhaust speed is $u$. Its final speed from rest is:",
             [r"$u/e$", r"$u$", r"$eu$", r"$u\ln\frac{1}{e} = -u$"], 1,
             r"$v = u\ln\dfrac{m_0}{m} = u\ln e = u$.", hint="Use v = u ln(m0/m).",
             feedback=["That divides rather than takes a logarithm.", "", "That multiplies by $e$ instead of taking $\\ln e = 1$.", "The ratio is $m_0/m = e$, not $m/m_0$; the speed is positive."]),
        H("Practice questions"),
        PQ(r"A rocket of mass $800$ kg burns fuel at $4$ kg/s with exhaust speed $2500$ m/s. Find the thrust and the initial acceleration ($g = 10$ m/s$^2$). After what time does the mass fall to $600$ kg?",
           r"Thrust $= 2500 \times 4 = 10\,000$ N. $a = \dfrac{10\,000 - 8000}{800} = 2.5$ m/s$^2$. Mass $800 - 4t = 600$ gives $t = 50$ s."),
        PQ(r"For the rocket above, find the speed at $t = 50$ s.",
           r"$v = 2500\ln\dfrac{800}{600} - 10(50) = 2500(0.28768) - 500 = 719.2 - 500 = 219.2$ m/s."),
        PQ(r"A space probe has initial mass $400$ kg including $300$ kg of fuel, ejected at $3000$ m/s relative to the probe. Find its final speed in free space and the fuel mass needed to reach $4000$ m/s from the same $400$ kg start.",
           r"Final: $v = 3000\ln\frac{400}{100} = 3000\ln 4 = 4159$ m/s. For $4000$: $\ln\frac{400}{m} = \frac{4000}{3000} = 1.3333$, $\frac{400}{m} = e^{1.3333} = 3.794$, so $m = 105.4$ kg of final mass and $400 - 105.4 = 294.6$ kg of fuel."),
        PQ(r"Explain why the speed of a rocket in free space depends only on $u$ and the mass ratio, not on the rate at which fuel is burned.",
           r"The equation is $m\frac{dv}{dt} = uk$. Since $k = -\frac{dm}{dt}$, this gives $dv = -u\frac{dm}{m}$, which integrates to $u\ln\frac{m_0}{m}$. The time has disappeared: burning fast or slowly gives the same final speed in free space. (With gravity, slow burning wastes speed because of the $-gt$ term.)"),
        H("Summary"),
        SUM(r"Rocket equation of motion: $m\dfrac{dv}{dt} = uk - mg$, where $k = -\dfrac{dm}{dt}$ and $u$ is the exhaust speed relative to the rocket.",
            r"The thrust is $uk$; lift-off needs $uk > mg$.",
            r"With constant $k$: $v = u\ln\dfrac{m_0}{m} - gt$ and the height is $u\left[t - \dfrac{m}{k}\ln\dfrac{m_0}{m}\right] - \tfrac{1}{2}gt^2$.",
            "In free space the final speed is u ln(m0/m): only the mass ratio and u matter.",
            "The acceleration is variable: integrate, do not use constant-acceleration formulae."),
    ],
))

# ---------------------------------------------------------------- Oblique collisions
LESSONS.append(lesson(
    module=MP, topic="Oblique collisions",
    title="Oblique impacts: smooth spheres and smooth walls",
    slug="fmu2-oblique-collisions",
    minutes=24,
    summary="Analyse collisions in which the velocity is not along the line of centres, using conservation of momentum and Newton's law of restitution along the line of centres, and unchanged perpendicular components.",
    objectives=[
        "Resolve velocities along and perpendicular to the line of centres",
        "Apply conservation of momentum and Newton's law of restitution along the line of centres",
        "Solve oblique impacts of a sphere with a fixed smooth wall, finding speed, direction and energy lost",
        "Find the speeds and directions after an oblique collision of two smooth spheres",
    ],
    key_concepts=["Line of centres", "Coefficient of restitution", "Perpendicular component unchanged", "Oblique impact", "Energy loss"],
    blocks=[
        H("Introduction"),
        T(r"In a game of draughts or a game of pool in a Yaounde bar, one disc rarely hits another head-on. It strikes at an angle, and both discs fly off in new directions. A ball bouncing off a wall at an angle behaves in a similar way. These are **oblique impacts**, and they can be solved by splitting every velocity into two directions."),
        H("The two rules"),
        IMG("al-fmu2-oblique-collision.svg", alt="Sphere A moving towards sphere B at 30 degrees to the line of centres, with its velocity split into a component along the line (which changes) and a perpendicular component (which is unchanged). B is at rest and leaves along the line of centres.", caption="Figure 2. At impact the only force between smooth spheres acts along the line of centres."),
        KEY("Two sphere rules (smooth spheres)", r"The **line of centres** is the line through the centres of the two spheres at impact. The force between smooth spheres acts only along this line.", cards=[
            ["Perpendicular to the line", "The component of each sphere's velocity perpendicular to the line of centres is **unchanged**."],
            ["Along the line: momentum", r"$m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$ (components along the line)."],
            ["Along the line: restitution", r"$v_2 - v_1 = -e\,(u_2 - u_1)$ (Newton's law of restitution; $0 \le e \le 1$)."],
            ["Energy", r"If $e < 1$ kinetic energy is lost. Check by adding the KE of both components."],
        ]),
        T(r"**A fixed smooth wall** is the special case where the wall acts only perpendicular to itself. The component of velocity **parallel** to the wall is unchanged. The component **perpendicular** to the wall reverses and is multiplied by $e$: $v_\perp' = -e\,u_\perp$."),
        EX("Worked example 1: a ball hits a wall", intro=r"A smooth ball hits a smooth fixed wall with speed $12$ m/s at $30^\circ$ to the wall. The coefficient of restitution is $e = 0.6$. Find its speed and direction after the impact, and the fraction of its kinetic energy lost.", steps=[
            S("Resolve before the impact", math=r"\text{parallel: } 12\cos30^\circ = 10.392, \qquad \text{perpendicular: } 12\sin30^\circ = 6"),
            S("After the impact", math=r"\text{parallel: } 10.392\ \text{(unchanged)}, \qquad \text{perpendicular: } 0.6 \times 6 = 3.6\ \text{(reversed)}"),
            S("Speed after", math=r"v = \sqrt{10.392^2 + 3.6^2} = \sqrt{120.96} = 11.0\ \text{m/s}"),
            S("Direction after", math=r"\tan\alpha = \frac{3.6}{10.392} \Rightarrow \alpha = 19.1^\circ \text{ to the wall}"),
            S("Energy lost", math=r"1 - \frac{v^2}{12^2} = 1 - \frac{120.96}{144} = 0.16", text=r"16% of the KE is lost. (In general it is $(1 - e^2)\sin^2\theta$ of the original: here $0.64 \times 0.25 = 0.16$.)"),
        ], check=r"\text{The path turns through } 30^\circ + 19.1^\circ = 49.1^\circ \text{ (it would be } 60^\circ \text{ if } e = 1\text{)}"),
        H("Two spheres"),
        EX("Worked example 2: sphere meets sphere at an angle", intro=r"A smooth sphere $A$ of mass $2$ kg moves at $8$ m/s. It hits a stationary smooth sphere $B$ of mass $1$ kg. At impact the velocity of $A$ makes $30^\circ$ with the line of centres. The coefficient of restitution is $0.5$. Find the velocities of $A$ and $B$ after the impact.", steps=[
            S("Resolve $A$'s velocity", math=r"\text{along the line: } 8\cos30^\circ = 4\sqrt3 = 6.928, \qquad \text{perpendicular: } 8\sin30^\circ = 4"),
            S("Momentum along the line ($v_A$, $v_B$ after)", math=r"2(6.928) + 0 = 2v_A + v_B"),
            S("Restitution", math=r"v_B - v_A = 0.5(6.928 - 0) = 3.464"),
            S("Solve", math=r"3v_A = 13.856 - 3.464 \Rightarrow v_A = 3.464 = 2\sqrt3, \quad v_B = 6.928 = 4\sqrt3"),
            S("$B$ after", text="$B$ moves along the line of centres at $6.93$ m/s (it had no perpendicular component)."),
            S("$A$ after", math=r"\text{speed } = \sqrt{3.464^2 + 4^2} = \sqrt{28} = 5.29\ \text{m/s}, \quad \tan\beta = \frac{4}{3.464} \Rightarrow \beta = 49.1^\circ \text{ to the line}"),
        ], check=r"\text{KE before } = \tfrac12(2)(64) = 64\ \text{J};\ \text{after } = \tfrac12(2)(28) + \tfrac12(1)(48) = 52\ \text{J};\ \text{lost } 12\ \text{J}"),
        EX("Worked example 3: equal spheres, perfectly elastic", intro=r"A smooth sphere moving at speed $u$ hits an identical stationary sphere with $e = 1$. The line of centres makes angle $\alpha$ with the incoming velocity. Show that the spheres move apart at right angles.", steps=[
            S("Along the line (equal masses, $e = 1$)", math=r"v_A + v_B = u\cos\alpha, \quad v_B - v_A = u\cos\alpha \Rightarrow v_A = 0,\ v_B = u\cos\alpha"),
            S("After the impact", text=r"$A$ has only its perpendicular component $u\sin\alpha$, so it moves perpendicular to the line of centres. $B$ moves along the line of centres."),
            S("Conclusion", text="The two directions are at right angles to each other, whatever the angle $\\alpha$ (a fact used in pool)."),
        ], check=r"(u\cos\alpha)^2 + (u\sin\alpha)^2 = u^2 \quad \text{(kinetic energy conserved)}"),
        MISTAKE("Applying restitution to the whole velocity", r"$e$ multiplies only the component along the line of centres (or perpendicular to the wall). The other component is **unchanged**. Applying $e$ to the whole speed ignores the geometry."),
        MISTAKE("Putting the perpendicular components into the momentum equation", r"Momentum is conserved along the line of centres. The perpendicular components belong to each sphere separately and do not enter this equation."),
        MISTAKE("Confusing the angle of the velocity with the angle of the line of centres", r"Always draw the line of centres first and measure angles from it. For a wall, measure from the wall. Then check the final direction with a sketch: the perpendicular component after must point away from the wall."),
        QUIZ(r"A ball with velocity components $9$ m/s parallel to a smooth wall and $4$ m/s towards it rebounds with $e = 0.5$. The velocity after the impact has:",
             ["parallel 9 m/s, perpendicular 2 m/s away from the wall", "parallel 4.5 m/s, perpendicular 2 m/s away", "parallel 9 m/s, perpendicular 4 m/s away", "parallel 9 m/s, perpendicular 8 m/s away"], 0,
             "Parallel component unchanged; perpendicular component reverses and is multiplied by $e = 0.5$: $0.5 \\times 4 = 2$.", hint="Which component does e multiply?",
             feedback=["", "The parallel component is not changed by a smooth wall.", "That would be $e = 1$.", "That multiplies by $2$ instead of $e = 0.5$."]),
        QUIZ(r"Two smooth spheres collide. Which quantity is **not** changed in the collision for each sphere?",
             ["the component of velocity along the line of centres", "the component of velocity perpendicular to the line of centres", "the speed", "the kinetic energy"], 1,
             "The impulse acts along the line of centres, so the perpendicular component of each sphere's velocity does not change.", hint="Think about the direction of the force between smooth spheres.",
             feedback=["That component changes: it is the one that gets momentum and restitution.", "", "The speed changes because one component changes.", "Kinetic energy is lost when $e < 1$."]),
        H("Practice questions"),
        PQ(r"A smooth ball hits a smooth wall at $10$ m/s, making $60^\circ$ with the wall. $e = 0.5$. Find the speed after the impact and the angle it makes with the wall.",
           r"Parallel: $10\cos60^\circ = 5$. Perpendicular: $10\sin60^\circ = 8.660$, after: $0.5 \times 8.660 = 4.330$. Speed $= \sqrt{25 + 18.75} = \sqrt{43.75} = 6.61$ m/s. Angle: $\tan\alpha = 4.330/5$, $\alpha = 40.9^\circ$ to the wall."),
        PQ(r"A sphere of mass $3$ kg moving at $10$ m/s hits a stationary sphere of mass $2$ kg. Its velocity makes $60^\circ$ with the line of centres. $e = 0.8$. Find the speed of the $2$ kg sphere after the impact.",
           r"Along the line: $u = 10\cos60^\circ = 5$. Momentum: $3(5) = 3v_1 + 2v_2$. Restitution: $v_2 - v_1 = 0.8(5) = 4$. So $15 = 3v_1 + 2(v_1 + 4)$, $5v_1 = 7$, $v_1 = 1.4$ and $v_2 = 5.4$ m/s."),
        PQ(r"For the collision in the previous question, find the speed of the $3$ kg sphere after the impact and the kinetic energy lost.",
           r"Perpendicular component: $10\sin60^\circ = 8.660$. Speed $= \sqrt{1.4^2 + 8.660^2} = \sqrt{1.96 + 75} = 8.77$ m/s. KE before $= \frac12(3)(100) = 150$ J. After: $\frac12(3)(76.96) + \frac12(2)(5.4^2) = 115.44 + 29.16 = 144.6$ J. Lost $= 5.4$ J."),
        PQ(r"A smooth ball is thrown at speed $u$ towards a smooth wall at $45^\circ$ and rebounds at right angles to its original path. Find $e$.",
           r"Incoming components: parallel $\frac{u}{\sqrt2}$, perpendicular $\frac{u}{\sqrt2}$. After: parallel $\frac{u}{\sqrt2}$, perpendicular $\frac{eu}{\sqrt2}$. The angle of the outgoing path to the wall has $\tan\alpha = e$. The path before made $45^\circ$ with the wall on the incoming side; the paths are at right angles when $45^\circ + \alpha = 90^\circ$, so $\alpha = 45^\circ$ and $e = 1$."),
        H("Summary"),
        SUM("For smooth bodies the impulse acts only along the line of centres (or perpendicular to a wall).",
            "The component perpendicular to the line of centres (or parallel to the wall) is unchanged.",
            r"Along the line: conservation of momentum and Newton's law $v_2 - v_1 = -e(u_2 - u_1)$.",
            "After finding both components, combine them with Pythagoras and tan to get speed and direction.",
            "Check kinetic energy: it must not increase, and is conserved only if e = 1."),
    ],
))


# ---------------------------------------------------------------- Damped and forced oscillations
LESSONS.append(lesson(
    module=MP, topic="Damped and forced oscillations",
    title="Damped and forced simple harmonic motion",
    slug="fmu2-damped-forced-oscillations",
    minutes=25,
    summary="Model a spring or suspension with a resistive force, solve the three cases of damping, and find the steady response and resonance when a periodic force drives the system.",
    objectives=[
        "Write the equation x'' + 2k x' + w0^2 x = 0 for damped SHM and classify light, critical and heavy damping",
        "Solve the damped equation for given initial conditions and find the period and the decay of the amplitude",
        "Find the steady-state solution of a forced oscillation and its amplitude",
        "Explain resonance, and what happens with and without damping",
    ],
    key_concepts=["Damping force", "Light, critical and heavy damping", "Transient and steady state", "Forcing frequency", "Resonance", "Amplitude response"],
    blocks=[
        H("Introduction"),
        T(r"A car going over a pothole on a Cameroonian road bounces on its springs, but a good **shock absorber** stops the bouncing after one swing. A door closer, a weighing scale and the needle of a meter use the same idea. A resistive force removes energy and the motion fades away. On the other hand a child on a swing is pushed again and again at the right moment, and the swing rises higher and higher. That is a **forced** oscillation."),
        T("This lesson uses the second-order linear differential equations met in the Ordinary Differential Equations module: the auxiliary equation for the homogeneous part and a particular integral for the forcing term."),
        H("The damped equation"),
        T(r"A mass $m$ on a spring of stiffness $s$ is subject to a resistance $c\dot x$ proportional to velocity. Newton's second law gives $m\ddot x = -sx - c\dot x$. Divide by $m$ and write $2k = \dfrac{c}{m}$ and $\omega_0^2 = \dfrac{s}{m}$:"),
        D(r"Damped simple harmonic motion: $\omega_0$ is the angular frequency without damping and $k > 0$ the damping constant.", title="Damped SHM",
          formula=r"\ddot x + 2k\dot x + \omega_0^2 x = 0", note=r"Auxiliary equation $\lambda^2 + 2k\lambda + \omega_0^2 = 0$ with roots $\lambda = -k \pm \sqrt{k^2 - \omega_0^2}$. The sign of $k^2 - \omega_0^2$ gives three cases."),
        IMG("al-fmu2-damped-oscillation.svg", alt="Displacement against time for three damped motions with the same start: light damping oscillates with decreasing amplitude, critical damping returns to zero fastest without crossing, heavy damping returns slowly.", caption="Figure 1. Light, critical and heavy damping with the same starting conditions (omega0 = 2)."),
        KEY("The three cases", r"Let $\Delta = k^2 - \omega_0^2$.", cards=[
            [r"Light damping, $k < \omega_0$", r"Complex roots. $x = e^{-kt}(A\cos\omega t + B\sin\omega t)$ with $\omega = \sqrt{\omega_0^2 - k^2}$. Oscillates; amplitude falls like $e^{-kt}$."],
            [r"Critical damping, $k = \omega_0$", r"Repeated root. $x = (A + Bt)e^{-kt}$. Returns to equilibrium in the shortest time without oscillating."],
            [r"Heavy damping, $k > \omega_0$", r"Two negative real roots $\lambda_1, \lambda_2$. $x = Ae^{\lambda_1 t} + Be^{\lambda_2 t}$. No oscillation, slow return."],
        ]),
        EX("Worked example 1: light damping", intro=r"A block of mass $2$ kg is attached to a spring with stiffness $26$ N/m and moves in a medium giving a resistance $8\dot x$ N. It is released from rest at $x = 1$ m. Find $x(t)$, the period of the oscillation and the ratio of successive maximum displacements.", steps=[
            S("Equation", math=r"2\ddot x = -26x - 8\dot x \Rightarrow \ddot x + 4\dot x + 13x = 0", text=r"So $k = 2$ and $\omega_0^2 = 13$."),
            S("Auxiliary equation", math=r"\lambda^2 + 4\lambda + 13 = 0 \Rightarrow \lambda = -2 \pm 3i", text="Light damping ($k^2 = 4 < 13$), with $\\omega = 3$."),
            S("General solution", math=r"x = e^{-2t}(A\cos3t + B\sin3t)"),
            S("Initial conditions", math=r"x(0) = 1 \Rightarrow A = 1;\quad \dot x = e^{-2t}\left[(3B - 2A)\cos3t - (3A + 2B)\sin3t\right],\ \dot x(0) = 0 \Rightarrow 3B - 2 = 0 \Rightarrow B = \tfrac23"),
            S("Solution", math=r"x = e^{-2t}\left(\cos3t + \tfrac23\sin3t\right)"),
            S("Period and ratio", math=r"T = \frac{2\pi}{3} = 2.09\ \text{s}, \qquad \frac{x_n}{x_{n+1}} = e^{kT} = e^{4\pi/3} = 65.9", text="Each swing is about 66 times smaller than the one before: the motion dies out in about two swings. (The 'period' of a damped motion is the time between successive maxima.)"),
        ], check=r"x(0.5) = e^{-1}(\cos1.5 + \tfrac23\sin1.5) = 0.2707, \text{ matches numerical integration of the equation}"),
        EX("Worked example 2: critical damping", intro=r"A door closer is modelled by $\ddot x + 6\dot x + 9x = 0$, with $x(0) = 1$ (door open) and $\dot x(0) = 0$. Show that the damping is critical and find $x(t)$.", steps=[
            S("Auxiliary equation", math=r"\lambda^2 + 6\lambda + 9 = (\lambda + 3)^2 = 0", text="A repeated root $\\lambda = -3$: critical damping ($k = \\omega_0 = 3$)."),
            S("General solution", math=r"x = (A + Bt)e^{-3t}"),
            S("Initial conditions", math=r"x(0) = A = 1;\quad \dot x = (B - 3A - 3Bt)e^{-3t},\ \dot x(0) = B - 3 = 0 \Rightarrow B = 3"),
            S("Solution", math=r"x = (1 + 3t)e^{-3t}", text="This is never zero for $t > 0$: the door closes without swinging past the frame."),
        ], check=r"x(1) = 4e^{-3} = 0.1991"),
        T(r"**Heavy damping example.** For $\ddot x + 5\dot x + 4x = 0$ the roots are $-1$ and $-4$ and, with $x(0) = 1$, $\dot x(0) = 0$: $x = \dfrac{4e^{-t} - e^{-4t}}{3}$. Both exponentials decay, the slower $e^{-t}$ dominates, and the return to zero is slow compared with the critical case."),
        H("Forced oscillations"),
        D(r"A periodic driving force $F\cos\Omega t$ per unit mass acts on the system ($\Omega$ = **forcing frequency**):", title="Forced damped SHM",
          formula=r"\ddot x + 2k\dot x + \omega_0^2 x = F\cos\Omega t",
          note="The general solution is the complementary function (the damped solution, which dies away: the transient) plus a particular integral (the steady state, which persists)."),
        T(r"The steady state is a motion at the **forcing** frequency: $x_p = P\cos\Omega t + Q\sin\Omega t$. Its amplitude is"),
        F(r"a(\Omega) = \frac{F}{\sqrt{(\omega_0^2 - \Omega^2)^2 + 4k^2\Omega^2}}", title="Steady-state amplitude"),
        EX("Worked example 3: a steady state", intro=r"Find the steady-state solution of $\ddot x + 2\dot x + 5x = 10\cos2t$ and its amplitude.", steps=[
            S("Try $x_p = P\\cos2t + Q\\sin2t$", math=r"\dot x_p = -2P\sin2t + 2Q\cos2t, \quad \ddot x_p = -4P\cos2t - 4Q\sin2t"),
            S("Substitute", math=r"\cos2t:\ -4P + 4Q + 5P = 10, \qquad \sin2t:\ -4Q - 4P + 5Q = 0", text=r"That is $P + 4Q = 10$ and $Q - 4P = 0$."),
            S("Solve", math=r"Q = 4P \Rightarrow 17P = 10 \Rightarrow P = \tfrac{10}{17},\ Q = \tfrac{40}{17}"),
            S("Steady state and amplitude", math=r"x_p = \tfrac{10}{17}\cos2t + \tfrac{40}{17}\sin2t, \qquad a = \tfrac{10}{17}\sqrt{1 + 16} = \tfrac{10}{\sqrt{17}} = 2.43"),
        ], check=r"\text{Formula: } \frac{10}{\sqrt{(5 - 4)^2 + 4(1)(4)}} = \frac{10}{\sqrt{17}} \ \checkmark"),
        H("Resonance"),
        T(r"The amplitude $a(\Omega)$ is largest when the denominator is smallest. Setting the derivative of $(\omega_0^2 - \Omega^2)^2 + 4k^2\Omega^2$ to zero gives $\Omega^2 = \omega_0^2 - 2k^2$ (when this is positive): the amplitude peaks at a frequency just **below** $\omega_0$. In Example 3, $\omega_0^2 = 5$, $k = 1$, so the peak is at $\Omega = \sqrt{3} = 1.73$ with amplitude $\dfrac{F}{2k\sqrt{\omega_0^2 - k^2}} = \dfrac{10}{4} = 2.5$. (Some textbooks define resonance as $\Omega = \omega_0$, which is where the **velocity** amplitude peaks, or the case of light damping: check your textbook.)"),
        T(r"**Without damping** ($k = 0$) and forcing at the natural frequency, $\ddot x + 4x = 12\cos2t$ has the particular integral $x_p = 3t\sin2t$ (check: $\ddot x_p = 12\cos2t - 12t\sin2t$). The amplitude $3t$ grows without limit. Real systems have some damping, which keeps the amplitude finite, but a lightly damped bridge, shaker table or wine glass can be broken by a force at its natural frequency."),
        MISTAKE("Using the wrong test for the type of damping", r"For $\ddot x + b\dot x + c x = 0$ compare $b^2$ with $4c$: $b^2 < 4c$ light, $b^2 = 4c$ critical, $b^2 > 4c$ heavy. Writing $b$ instead of $b/2$ for $k$ before comparing with $\omega_0$ gives the wrong case."),
        MISTAKE("Forgetting the exponential decay, or the transient", r"In light damping $x = e^{-kt}(\ldots)$: dropping $e^{-kt}$ gives undamped SHM. And in a forced problem the **full** solution has both parts; only after a long time does it reduce to the steady state."),
        MISTAKE("Forced motion at the natural frequency", r"The steady state oscillates at the **forcing** frequency $\Omega$, not at $\omega_0$ or $\omega$. Only the transient oscillates at $\omega = \sqrt{\omega_0^2 - k^2}$."),
        QUIZ(r"A damped system obeys $\ddot x + 6\dot x + 5x = 0$. Which describes the motion?",
             ["Oscillation with decreasing amplitude", "Critical damping", "Heavy damping: no oscillation", "Undamped oscillation"], 2,
             r"Roots of $\lambda^2 + 6\lambda + 5 = 0$ are $-1$ and $-5$, both real and negative: heavy damping. ($b^2 = 36 > 4c = 20$.)", hint="Compare b squared with 4c.",
             feedback=["That needs complex roots ($b^2 < 4c$).", "Critical would need $b^2 = 4c$, i.e. $36 = 20$.", "", "There is a $6\\dot x$ term, so the motion is damped."]),
        QUIZ(r"A lightly damped system has natural frequency $\omega_0$. A force $F\cos\Omega t$ with $\Omega \approx \omega_0$ is applied. After a long time the system oscillates with:",
             [r"frequency $\omega = \sqrt{\omega_0^2 - k^2}$ and amplitude decaying to zero", r"frequency $\Omega$ and a constant, large amplitude", r"frequency $\omega_0$ and growing amplitude", "frequency $2\\Omega$"], 1,
             "The transient dies away; the steady state is at the forcing frequency, with a constant amplitude that is large near resonance.", hint="What remains after the transient has died away?",
             feedback=["That is the transient, which has died away.", "", "The amplitude grows only if there is no damping.", "The response has the same frequency as the force."]),
        H("Practice questions"),
        PQ(r"Classify $\ddot x + 4\dot x + 4x = 0$ and $\ddot x + 2\dot x + 10x = 0$, and write the general solution of each.",
           r"First: $\lambda^2 + 4\lambda + 4 = (\lambda + 2)^2$, repeated root: critical damping, $x = (A + Bt)e^{-2t}$. Second: $\lambda = -1 \pm 3i$, light damping, $x = e^{-t}(A\cos3t + B\sin3t)$."),
        PQ(r"A mass of $1$ kg on a spring with stiffness $16$ N/m has resistance $c\dot x$. For what value of $c$ is the damping critical? Find $x$ if $x(0) = 0$ and $\dot x(0) = 5$ in that case.",
           r"$\ddot x + c\dot x + 16x = 0$; critical when $c^2 = 4 \times 16 = 64$, $c = 8$ N s/m. Then $x = (A + Bt)e^{-4t}$. $x(0) = A = 0$; $\dot x = Be^{-4t}(1 - 4t)$ and $\dot x(0) = B = 5$. So $x = 5te^{-4t}$."),
        PQ(r"For $\ddot x + 4\dot x + 13x = 0$ find the time for the amplitude to fall to $1\%$ of its starting value, ignoring the oscillating factor.",
           r"The envelope is $e^{-2t}$. $e^{-2t} = 0.01 \Rightarrow t = \dfrac{\ln100}{2} = 2.30$ s."),
        PQ(r"Find the steady-state solution of $\ddot x + 4x = 8\cos t$. What happens when the forcing frequency is changed to $2$?",
           r"Try $x_p = A\cos t$: $-A + 4A = 8$, $A = \frac{8}{3}$, so $x_p = \frac{8}{3}\cos t$. With forcing $\cos2t$ the natural frequency $\omega_0 = 2$ is matched, so there is resonance: the particular integral has the form $Ct\sin2t$, whose amplitude grows without bound."),
        H("Summary"),
        SUM(r"Damped SHM: $\ddot x + 2k\dot x + \omega_0^2 x = 0$; roots $-k \pm \sqrt{k^2 - \omega_0^2}$.",
            r"Light ($k < \omega_0$): $e^{-kt}(A\cos\omega t + B\sin\omega t)$, $\omega = \sqrt{\omega_0^2 - k^2}$. Critical ($k = \omega_0$): $(A + Bt)e^{-kt}$. Heavy ($k > \omega_0$): two real exponentials.",
            "Forced motion: transient (dies away) plus steady state at the forcing frequency.",
            r"Steady-state amplitude $\dfrac{F}{\sqrt{(\omega_0^2 - \Omega^2)^2 + 4k^2\Omega^2}}$, largest near $\Omega = \sqrt{\omega_0^2 - 2k^2}$.",
            "Without damping, forcing at the natural frequency gives an amplitude that grows without limit."),
    ],
))

# ---------------------------------------------------------------- Moment of inertia
LESSONS.append(lesson(
    module=MP, topic="Moment of inertia of rigid bodies",
    title="Moment of inertia and the parallel and perpendicular axes theorems",
    slug="fmu2-moment-of-inertia",
    minutes=25,
    summary="Define the moment of inertia, derive it for a rod and a disc by integration, use the standard results, and apply the parallel and perpendicular axes theorems to find it about other axes.",
    objectives=[
        "Define moment of inertia I = sum of m r squared and the radius of gyration",
        "Derive I for a uniform rod and a uniform disc by integration",
        "Use the parallel axis theorem I = I_G + M d squared",
        "Use the perpendicular axes theorem for a plane lamina",
    ],
    key_concepts=["Moment of inertia", "Radius of gyration", "Standard results", "Parallel axis theorem", "Perpendicular axes theorem", "Composite bodies"],
    blocks=[
        H("Introduction"),
        T(r"A potter in Foumban sets a heavy wheel spinning with her foot. A flywheel in a bush-taxi engine smooths out the beats of the pistons. Both are hard to start and hard to stop, because of how their **mass is spread** around the axis of rotation. Mass far from the axis matters more than mass close to it. The quantity that measures this is the **moment of inertia**: the rotational counterpart of mass."),
        H("Definition"),
        D(r"For particles of masses $m_i$ at perpendicular distances $r_i$ from an axis, the **moment of inertia** about that axis is", title="Moment of inertia",
          formula=r"I = \sum m_i r_i^2 \qquad\text{(continuous body: } I = \int r^2\,dm\text{)}",
          note=r"Unit: kg m$^2$. It depends on the **axis** chosen. The **radius of gyration** $k$ is defined by $I = Mk^2$: the distance at which all the mass would have to be placed to give the same $I$."),
        EX("Worked example 1: particles", intro=r"Masses of $2$ kg, $3$ kg and $5$ kg are fixed at distances $0.5$ m, $1$ m and $0.4$ m from an axis. Find $I$ and the radius of gyration.", steps=[
            S("Sum $m r^2$", math=r"I = 2(0.25) + 3(1) + 5(0.16) = 0.5 + 3 + 0.8 = 4.3\ \text{kg m}^2"),
            S("Total mass $10$ kg; radius of gyration", math=r"k = \sqrt{\frac{4.3}{10}} = 0.656\ \text{m}"),
        ]),
        H("Deriving the standard results"),
        T(r"**Uniform rod** of mass $M$ and length $L$, axis through the centre perpendicular to the rod. A small piece of length $dx$ at distance $x$ from the centre has mass $\dfrac{M}{L}dx$:"),
        F(r"I_G = \int_{-L/2}^{L/2} x^2\,\frac{M}{L}\,dx = \frac{M}{L}\cdot\frac{2}{3}\left(\frac{L}{2}\right)^3 = \frac{ML^2}{12}"),
        T(r"**Uniform disc** of mass $M$ and radius $a$, axis through the centre perpendicular to the plane. Divide into thin rings of radius $r$ and width $dr$. The ring's area is $2\pi r\,dr$ so its mass is $\dfrac{M}{\pi a^2}\,2\pi r\,dr = \dfrac{2M}{a^2}r\,dr$:"),
        F(r"I = \int_0^a r^2\,\frac{2M}{a^2}\,r\,dr = \frac{2M}{a^2}\cdot\frac{a^4}{4} = \frac{Ma^2}{2}"),
        KEY("Standard results (uniform bodies)", r"Mass $M$. Learn these, or know how to derive them. They appear in the formula list of most textbooks.", cards=[
            ["Thin rod, length L, axis through centre perpendicular to rod", r"$\dfrac{1}{12}ML^2$"],
            ["Thin rod, axis through one end, perpendicular", r"$\dfrac{1}{3}ML^2$"],
            ["Ring (or thin hollow cylinder), radius a, axis through centre perpendicular to plane", r"$Ma^2$"],
            ["Disc (or solid cylinder), radius a, axis through centre perpendicular to plane", r"$\dfrac{1}{2}Ma^2$"],
            ["Solid sphere, radius a, about a diameter", r"$\dfrac{2}{5}Ma^2$"],
            ["Thin spherical shell, radius a, about a diameter", r"$\dfrac{2}{3}Ma^2$"],
        ]),
        H("Two theorems"),
        D(r"If $I_G$ is the moment of inertia about an axis through the centre of mass $G$, then about **any parallel axis** at distance $d$ from it,", title="Parallel axis theorem",
          formula=r"I = I_G + Md^2",
          note="The axis through G always has the smallest moment of inertia of all parallel axes."),
        IMG("al-fmu2-parallel-axes.svg", alt="A uniform rod with a dashed axis through its centre and a parallel dashed axis through one end, a distance L over 2 apart; formulas for the moment of inertia about each.", caption="Figure 2. The parallel axis theorem for a rod: from ML squared over 12 to ML squared over 3."),
        D(r"For a **plane lamina** (flat, thin body), the moment of inertia about an axis perpendicular to its plane through a point $O$ equals the sum of the moments of inertia about two perpendicular axes in the plane through $O$:", title="Perpendicular axes theorem",
          formula=r"I_z = I_x + I_y",
          note="This theorem applies to flat laminas only, not to solid bodies."),
        EX("Worked example 2: the rod about its end", intro=r"A uniform rod has mass $3$ kg and length $1.2$ m. Find its moment of inertia about (a) its centre, (b) one end.", steps=[
            S("(a) Centre", math=r"I_G = \tfrac{1}{12}(3)(1.2)^2 = 0.36\ \text{kg m}^2"),
            S("(b) Parallel axis, $d = 0.6$", math=r"I = 0.36 + 3(0.6)^2 = 0.36 + 1.08 = 1.44\ \text{kg m}^2"),
        ], check=r"\tfrac{1}{3}ML^2 = \tfrac{1}{3}(3)(1.44) = 1.44 \ \checkmark"),
        EX("Worked example 3: a disc, three axes", intro=r"A uniform disc has mass $4$ kg and radius $0.5$ m. Find $I$ about (a) the perpendicular axis through the centre, (b) a diameter, (c) a perpendicular axis through a point on the rim.", steps=[
            S("(a) Standard result", math=r"I_z = \tfrac12 Ma^2 = \tfrac12(4)(0.25) = 0.5\ \text{kg m}^2"),
            S("(b) Perpendicular axes: two diameters are equal, so $I_x = I_y$", math=r"2I_x = I_z \Rightarrow I_x = \tfrac14 Ma^2 = 0.25\ \text{kg m}^2"),
            S("(c) Parallel axis, $d = a = 0.5$", math=r"I = 0.5 + 4(0.25) = 1.5\ \text{kg m}^2 = \tfrac32 Ma^2"),
        ]),
        T(r"**Composite bodies** are handled by adding the moments of inertia of the parts about the **same** axis. A rod of mass $3$ kg and length $1.2$ m with a small sphere of mass $1$ kg (treated as a particle) attached at one end, about an axis through the other end: $I = \tfrac13(3)(1.2)^2 + 1(1.2)^2 = 1.44 + 1.44 = 2.88$ kg m$^2$."),
        T(r"**A square lamina** of side $a$ and mass $M$: each in-plane axis through the centre, parallel to a side, is like a rod of width $a$, so $I_x = I_y = \frac{1}{12}Ma^2$. By the perpendicular axes theorem, $I_z = \frac16 Ma^2$ through the centre. About a corner (perpendicular to the plane) the distance to the centre is $\frac{a}{\sqrt2}$, so $I = \frac16 Ma^2 + M\cdot\frac{a^2}{2} = \frac23 Ma^2$."),
        MISTAKE("Using the parallel axis theorem from a general axis", r"$I = I_G + Md^2$ needs $I_G$, the moment of inertia about the axis through the **centre of mass**. To go from one off-centre axis to another, first go **down** to $G$ (subtract $Md_1^2$) then up (add $Md_2^2$)."),
        MISTAKE("Applying perpendicular axes to a solid", r"The theorem $I_z = I_x + I_y$ holds for a thin flat lamina with $z$ perpendicular to it. For a solid sphere or cylinder it is false."),
        MISTAKE("Mixing up r and the distance to the centre", r"$r$ in $\sum m r^2$ is the **perpendicular distance to the axis**, not the distance to a point or the origin. For a rod with the axis at one end, the distances run from $0$ to $L$."),
        QUIZ(r"A uniform rod of mass $M$ and length $L$ has $I = \dfrac{1}{3}ML^2$ about one end. Its moment of inertia about the axis through the point $\dfrac{L}{4}$ from that end is:",
             [r"$\dfrac{1}{12}ML^2 + \dfrac{1}{16}ML^2 = \dfrac{7}{48}ML^2$", r"$\dfrac{1}{3}ML^2 - \dfrac{1}{16}ML^2$", r"$\dfrac{1}{12}ML^2$", r"$\dfrac{1}{3}ML^2 + \dfrac{1}{16}ML^2$"], 0,
             r"$G$ is $\frac{L}{4}$ from the new axis: $I = \frac{1}{12}ML^2 + M\left(\frac{L}{4}\right)^2 = \frac{ML^2}{12} + \frac{ML^2}{16} = \frac{7ML^2}{48}$.", hint="The centre is at L/2 from the end; the new axis is at L/4. How far apart are they?",
             feedback=["", "You subtracted $Md^2$ from the end value, but the end is not the centre.", "That is the value about the centre; the new axis is not at the centre.", "You added $Md^2$ to the end value, but the end is not the centre."]),
        QUIZ(r"For a thin square plate, $I$ about a side is $\dfrac{1}{3}Ma^2$. About an axis through the centre, parallel to a side, it is:",
             [r"$\dfrac{1}{3}Ma^2 - \dfrac{1}{4}Ma^2 = \dfrac{1}{12}Ma^2$", r"$\dfrac{1}{3}Ma^2 + \dfrac{1}{4}Ma^2$", r"$\dfrac{1}{6}Ma^2$", r"$\dfrac{1}{3}Ma^2$"], 0,
             r"The two axes are $d = \frac{a}{2}$ apart, so $\frac13 Ma^2 = I_G + M\frac{a^2}{4}$ and $I_G = \frac{1}{12}Ma^2$.", hint="The axis through the centre is the one with the smaller I; subtract Md squared.",
             feedback=["", "I at the centre must be smaller than at the side, so you subtract.", "That is the value about the perpendicular axis through the centre.", "The axes are not the same."]),
        H("Practice questions"),
        PQ(r"Find the moment of inertia of a uniform ring of mass $2$ kg and radius $0.3$ m about a tangent in the plane of the ring.",
           r"About a diameter (in the plane): by perpendicular axes $2I_d = Ma^2$, so $I_d = \frac12 Ma^2 = 0.09$. Parallel axis to the tangent, $d = 0.3$: $I = 0.09 + 2(0.09) = 0.27$ kg m$^2$ ($= \frac32 Ma^2$)."),
        PQ(r"A uniform solid sphere has mass $4$ kg and radius $0.5$ m. Find its moment of inertia about a tangent.",
           r"About a diameter $\frac25 Ma^2 = \frac25(4)(0.25) = 0.4$. Parallel axis to the tangent: $0.4 + 4(0.25) = 1.4$ kg m$^2$ ($= \frac75 Ma^2$)."),
        PQ(r"Two particles, of mass $m$ each, are attached to the ends of a light rod of length $2a$. Find $I$ about the perpendicular axis through (a) the centre, (b) one end.",
           r"(a) $m a^2 + m a^2 = 2ma^2$. (b) $m(0)^2 + m(2a)^2 = 4ma^2$. Check by the parallel axis theorem: $2ma^2 + (2m)a^2 = 4ma^2$."),
        PQ(r"Derive the moment of inertia of a uniform rod of mass $M$ and length $L$ about an axis through one end, perpendicular to the rod, by integration.",
           r"A piece at distance $x$ from the end has mass $\frac{M}{L}dx$. $I = \int_0^L x^2\frac{M}{L}dx = \frac{M}{L}\cdot\frac{L^3}{3} = \frac{1}{3}ML^2$."),
        H("Summary"),
        SUM(r"$I = \sum m r^2 = \int r^2\,dm$, with $r$ the distance from the axis; the radius of gyration is $k = \sqrt{I/M}$.",
            r"Rod about centre: $\frac{1}{12}ML^2$; about an end: $\frac13 ML^2$. Disc about the perpendicular axis through the centre: $\frac12 Ma^2$; ring $Ma^2$; solid sphere $\frac25 Ma^2$.",
            r"Parallel axis: $I = I_G + Md^2$ (from the centre of mass only).",
            r"Perpendicular axes (flat laminas only): $I_z = I_x + I_y$.",
            "For composite bodies add the moments of inertia about the same axis."),
    ],
))

# ---------------------------------------------------------------- Rotation about a fixed axis
LESSONS.append(lesson(
    module=MP, topic="Rotation about a fixed axis",
    title="Rotation about a fixed axis: torque, energy and angular momentum",
    slug="fmu2-rotation-fixed-axis",
    minutes=25,
    summary="Use torque = I alpha, the kinetic energy of rotation and conservation of angular momentum to solve problems on flywheels, pulleys and pendulums, including the small oscillations of a rod.",
    objectives=[
        "Apply the rotational equation of motion: torque = I times angular acceleration",
        "Use the kinetic energy 1/2 I w squared and energy conservation for rigid bodies",
        "Use conservation of angular momentum",
        "Find the period of small oscillations of a compound pendulum",
    ],
    key_concepts=["Torque", "Angular acceleration", "Rotational kinetic energy", "Angular momentum", "Compound pendulum", "Linear-rotational analogy"],
    blocks=[
        H("Introduction"),
        T(r"A rotating body behaves like a moving particle, but with rotational quantities in the place of linear ones. Where a force gives an acceleration through $F = ma$, a **torque** gives an angular acceleration through $\Gamma = I\alpha$. The moment of inertia $I$ (previous lesson) plays the role of mass."),
        KEY("The analogy", "Each linear law has a rotational twin about a fixed axis.", cards=[
            ["Linear", r"force $F$, mass $m$, acceleration $a$; $F = ma$; KE $\frac12 mv^2$; momentum $mv$; work $Fs$"],
            ["Rotational", r"torque $\Gamma$, moment of inertia $I$, angular acceleration $\alpha$; $\Gamma = I\alpha$; KE $\frac12 I\omega^2$; angular momentum $I\omega$; work $\Gamma\theta$"],
            ["Linking", r"A point at distance $r$ from the axis has speed $v = r\omega$ and tangential acceleration $a = r\alpha$."],
        ]),
        D(r"The torque (moment) of the external forces about the fixed axis equals the rate of change of angular momentum about that axis:", title="Equation of motion",
          formula=r"\Gamma = I\alpha = I\frac{d\omega}{dt}",
          note=r"Angular speed $\omega$ in rad/s; torque in N m. Reason: the force on a particle $m_i$ gives $F_i r_i = m_i r_i^2\alpha$; summing over all the particles gives $\Gamma = \left(\sum m_i r_i^2\right)\alpha$."),
        EX("Worked example 1: braking a flywheel", intro=r"A flywheel with $I = 3$ kg m$^2$ is turning at $40$ rad/s. A brake applies a constant torque of $6$ N m. How long does it take to stop, and how many revolutions does it make?", steps=[
            S("Angular deceleration", math=r"\alpha = \frac{\Gamma}{I} = \frac{6}{3} = 2\ \text{rad/s}^2"),
            S("Time to stop", math=r"0 = 40 - 2t \Rightarrow t = 20\ \text{s}"),
            S("Angle turned", math=r"\theta = \frac{\omega_0^2}{2\alpha} = \frac{1600}{4} = 400\ \text{rad}", text=r"$\dfrac{400}{2\pi} = 63.7$ revolutions."),
        ], check=r"\text{Work-energy: } \tfrac12 I\omega_0^2 = 2400\ \text{J} = \Gamma\theta = 6 \times 400 \ \checkmark"),
        EX("Worked example 2: a mass falling from a pulley", intro=r"A string is wound round a cylinder of radius $0.2$ m with $I = 0.5$ kg m$^2$ about its fixed horizontal axis. A mass of $4$ kg hangs from the free end and is released from rest. Take $g = 10$ m/s$^2$. Find the acceleration of the mass and the tension.", steps=[
            S("Mass: Newton's law", math=r"4g - T = 4a"),
            S("Cylinder: torque $= Tr$", math=r"T(0.2) = 0.5\alpha, \qquad a = r\alpha = 0.2\alpha \Rightarrow T = 0.5\,\frac{a}{0.2}\cdot\frac{1}{0.2} = 12.5a"),
            S("Eliminate $T$", math=r"40 - 12.5a = 4a \Rightarrow a = \frac{40}{16.5} = 2.42\ \text{m/s}^2"),
            S("Tension and $\\alpha$", math=r"T = 12.5(2.424) = 30.3\ \text{N}, \qquad \alpha = \frac{a}{r} = 12.1\ \text{rad/s}^2"),
        ], check=r"\text{Check the mass: } 40 - 30.3 = 9.7 = 4(2.42) \ \checkmark"),
        T(r"Notice $T = 30.3$ N is **less than the weight** $40$ N of the mass: if the string tension equalled the weight the mass would not accelerate. The general result is $a = \dfrac{mgr^2}{I + mr^2}$."),
        H("Energy and angular momentum"),
        D(r"A rigid body rotating about a fixed axis with angular speed $\omega$ has kinetic energy $\tfrac12 I\omega^2$ and angular momentum $L = I\omega$. If the external torque is zero, $L$ is conserved; if only conservative forces such as gravity do work, energy is conserved:", title="Rotational energy and momentum",
          formula=r"E_k = \tfrac12 I\omega^2 \qquad L = I\omega \qquad \Gamma = \dfrac{dL}{dt}",
          note=r"Gravity does work on a rigid body as if the whole weight acted at the centre of mass: the potential energy change is $Mg\,\Delta h_G$."),
        EX("Worked example 3: a rod pendulum", intro=r"A uniform rod of mass $M$ and length $1.2$ m can swing freely in a vertical plane about a horizontal axis through one end. It is released from the horizontal position. Find the angular speed at the lowest position, and the period of small oscillations about the vertical. ($g = 10$ m/s$^2$.)", steps=[
            S("$I$ about the pivot", math=r"I = \tfrac13 ML^2"),
            S("Energy: the centre of mass falls $\\frac{L}{2}$", math=r"\tfrac12 I\omega^2 = Mg\frac{L}{2} \Rightarrow \tfrac16 ML^2\omega^2 = \tfrac12 MgL \Rightarrow \omega^2 = \frac{3g}{L} = 25", text=r"$\omega = 5$ rad/s at the bottom."),
            S("Equation of motion at angle $\\theta$ from the vertical", math=r"I\ddot\theta = -Mg\frac{L}{2}\sin\theta \Rightarrow \ddot\theta = -\frac{3g}{2L}\sin\theta"),
            S("Small angles: $\\sin\\theta \\approx \\theta$", math=r"\ddot\theta = -\frac{3g}{2L}\theta \Rightarrow \text{SHM with } \omega_s^2 = \frac{3g}{2L} = 12.5"),
            S("Period", math=r"T = 2\pi\sqrt{\frac{2L}{3g}} = 2\pi\sqrt{0.08} = 1.78\ \text{s}", text="This is the period of a simple pendulum of length $\\frac{2L}{3} = 0.8$ m."),
        ], check=r"\text{Numerical solution of } \ddot\theta = -12.5\sin\theta \text{ for a small start gives a period of } 1.777\ \text{s}"),
        T(r"**Conservation of angular momentum.** A turntable with $I = 2$ kg m$^2$ spins at $3$ rad/s. A $0.5$ kg m$^2$ ring is gently dropped on to it so that they spin together. No external torque acts about the axis, so $2(3) = (2 + 0.5)\omega$ and $\omega = 2.4$ rad/s. Kinetic energy falls from $9$ J to $7.2$ J: the lost energy goes into friction as the two parts reach the same speed."),
        MISTAKE("Using the mass in place of I", r"The equation is $\Gamma = I\alpha$ with the moment of inertia **about the axis of rotation**. $Mr^2$ is right only if all the mass is at distance $r$. Check which axis the problem uses."),
        MISTAKE("Assuming the string tension equals the weight", r"If a hanging mass accelerates, $T = m(g - a) < mg$. Writing $T = mg$ in the torque equation would make the mass stay still."),
        MISTAKE("Forgetting rotational energy", r"For a rolling or swinging body, the kinetic energy is $\tfrac12 I\omega^2$ (about a fixed axis) and a falling mass attached to a pulley carries its own $\tfrac12 mv^2$ as well. Include both terms in the energy equation."),
        QUIZ(r"A wheel with $I = 2$ kg m$^2$ is acted on by a constant torque of $10$ N m, starting from rest. Its angular speed after $3$ s is:",
             ["$5$ rad/s", "$15$ rad/s", "$60$ rad/s", "$1.67$ rad/s"], 1,
             r"$\alpha = \frac{10}{2} = 5$ rad/s$^2$ and $\omega = \alpha t = 15$ rad/s.", hint="Find alpha from torque = I alpha first.",
             feedback=["That is $\\alpha$, not $\\omega$ after $3$ s.", "", "You multiplied torque, $I$ and time: $10 \\times 2 \\times 3$.", "You divided $5$ by $3$ instead of multiplying."]),
        QUIZ(r"A spinning skater pulls in her arms, reducing her moment of inertia from $I$ to $\frac{I}{2}$. No external torque acts. Her angular speed:",
             ["halves", "stays the same", "doubles", "increases by a factor of 4"], 2,
             r"$I_1\omega_1 = I_2\omega_2 \Rightarrow \omega_2 = 2\omega_1$.", hint="Conservation of angular momentum.",
             feedback=["The speed rises when I falls.", "Angular momentum is constant, not angular speed.", "", "The factor is the ratio $I_1/I_2 = 2$, not its square. (The kinetic energy, however, doubles.)"]),
        H("Practice questions"),
        PQ(r"A uniform disc of mass $6$ kg and radius $0.4$ m rotates about its axis. A tangential force of $15$ N acts at the rim. Find the angular acceleration.",
           r"$I = \frac12(6)(0.16) = 0.48$ kg m$^2$. Torque $= 15 \times 0.4 = 6$ N m. $\alpha = \frac{6}{0.48} = 12.5$ rad/s$^2$."),
        PQ(r"A uniform rod, mass $2$ kg, length $1.5$ m, is hinged at one end and released from rest in a horizontal position. Find the angular acceleration at the instant of release ($g = 10$ m/s$^2$).",
           r"$I = \frac13(2)(2.25) = 1.5$ kg m$^2$. Torque of the weight about the hinge $= 2(10)(0.75) = 15$ N m. $\alpha = \frac{15}{1.5} = 10$ rad/s$^2$."),
        PQ(r"Use energy to find the speed of the $4$ kg mass in Worked example 2 after it has fallen $1.5$ m from rest.",
           r"Energy: $mgh = \frac12 mv^2 + \frac12 I\omega^2$ with $\omega = \frac{v}{r} = 5v$: $4(10)(1.5) = 2v^2 + \frac12(0.5)(25v^2) = 2v^2 + 6.25v^2$. So $60 = 8.25v^2$, $v = 2.70$ m/s. (Check: $v^2 = 2as = 2(2.424)(1.5) = 7.27$, $v = 2.70$.)"),
        PQ(r"A uniform rod of length $0.6$ m swings as a compound pendulum about an axis through one end. Find the period of small oscillations ($g = 10$ m/s$^2$).",
           r"$T = 2\pi\sqrt{\frac{2L}{3g}} = 2\pi\sqrt{\frac{1.2}{30}} = 2\pi\sqrt{0.04} = 2\pi(0.2) = 1.26$ s."),
        H("Summary"),
        SUM(r"Torque about a fixed axis: $\Gamma = I\alpha$. Linear and rotational quantities are linked by $v = r\omega$ and $a_t = r\alpha$.",
            r"Kinetic energy $\frac12 I\omega^2$; angular momentum $I\omega$; the weight acts at the centre of mass.",
            "For a mass on a string over a pulley write one equation for the mass and one for the pulley, and link a = r alpha.",
            r"Compound pendulum, small angles: $\ddot\theta = -\dfrac{Mgh}{I}\theta$, so $T = 2\pi\sqrt{\dfrac{I}{Mgh}}$ with $h$ the distance from the axis to the centre of mass.",
            "With no external torque, I omega is conserved."),
    ],
))

# ---------------------------------------------------------------- Probability generating functions
LESSONS.append(lesson(
    module=MP, topic="Probability generating functions",
    title="Probability generating functions",
    slug="fmu2-probability-generating-functions",
    minutes=24,
    summary="Define the probability generating function G(t) = E(t^X), use it to find probabilities, the mean and the variance, and use products of generating functions for sums of independent random variables.",
    objectives=[
        "Write the probability generating function of a discrete random variable taking values 0, 1, 2, ...",
        "Use G(1) = 1, the mean G'(1) and the variance G''(1) + G'(1) - G'(1) squared",
        "Find the generating functions of the binomial, geometric and Poisson distributions",
        "Use the product rule for sums of independent random variables",
    ],
    key_concepts=["Probability generating function", "G(1) = 1", "Mean and variance from derivatives", "Independent sums", "Standard distributions"],
    blocks=[
        H("Introduction"),
        T(r"A mobile-money agent in Bamenda serves $X$ customers in a busy hour. Instead of listing every probability $P(X = 0), P(X = 1), \ldots$ we can pack **all of them into one function** of a dummy variable $t$. Differentiating this function then delivers the mean and variance with almost no working, and multiplying two such functions gives the distribution of a sum. This is the **probability generating function**."),
        H("Definition and basic properties"),
        D(r"For a random variable $X$ taking values $0, 1, 2, \ldots$ with $p_r = P(X = r)$, the **probability generating function** (pgf) is", title="Probability generating function",
          formula=r"G_X(t) = E(t^X) = \sum_{r = 0}^{\infty} p_r t^r = p_0 + p_1 t + p_2 t^2 + \cdots",
          note=r"The coefficient of $t^r$ is $P(X = r)$. Putting $t = 1$ adds all the probabilities, so $G_X(1) = 1$ always. Use it to check an answer."),
        KEY("Getting information out of G", "All from differentiating at t = 1.", cards=[
            ["Total probability", r"$G(1) = 1$"],
            ["Mean", r"$E(X) = G'(1)$"],
            ["Variance", r"$\operatorname{Var}(X) = G''(1) + G'(1) - \big(G'(1)\big)^2$"],
            ["Probabilities", r"$P(X = r) = \dfrac{G^{(r)}(0)}{r!}$, or read off the coefficient of $t^r$."],
        ]),
        T(r"Why: $G'(t) = \sum r p_r t^{r - 1}$, so $G'(1) = \sum r p_r = E(X)$. And $G''(1) = \sum r(r - 1)p_r = E(X^2) - E(X)$, so $E(X^2) = G''(1) + G'(1)$, giving the variance formula."),
        EX("Worked example 1: from a table", intro=r"$X$ has $P(X = 0) = 0.1$, $P(X = 1) = 0.3$, $P(X = 2) = 0.4$, $P(X = 3) = 0.2$. Find $G(t)$, the mean and the variance.", steps=[
            S("Write the pgf", math=r"G(t) = 0.1 + 0.3t + 0.4t^2 + 0.2t^3", text="Check: $G(1) = 0.1 + 0.3 + 0.4 + 0.2 = 1$."),
            S("Derivatives", math=r"G'(t) = 0.3 + 0.8t + 0.6t^2, \qquad G''(t) = 0.8 + 1.2t"),
            S("At $t = 1$", math=r"G'(1) = 1.7, \qquad G''(1) = 2.0"),
            S("Mean and variance", math=r"E(X) = 1.7, \qquad \operatorname{Var}(X) = 2.0 + 1.7 - 1.7^2 = 0.81"),
        ], check=r"\text{Direct: } E(X^2) = 0.3 + 1.6 + 1.8 = 3.7, \ \operatorname{Var} = 3.7 - 2.89 = 0.81 \ \checkmark"),
        H("Standard distributions"),
        KEY("Generating functions to know", r"Here $q = 1 - p$. Derive the first two quickly from the definition.", cards=[
            [r"Binomial $B(n, p)$", r"$G(t) = (q + pt)^n$. Mean $np$, variance $npq$."],
            [r"Geometric (trials up to the first success), $P(X = r) = q^{r-1}p$", r"$G(t) = \dfrac{pt}{1 - qt}$. Mean $\dfrac1p$, variance $\dfrac{q}{p^2}$."],
            [r"Poisson with mean $\lambda$", r"$G(t) = e^{\lambda(t - 1)}$. Mean $\lambda$, variance $\lambda$."],
        ]),
        EX("Worked example 2: moments of the geometric distribution", intro=r"A player rolls a fair die until a 6 appears. Let $X$ be the number of rolls. Find the pgf, and the mean and variance of $X$.", steps=[
            S("Parameters", math=r"p = \tfrac16, \quad q = \tfrac56, \quad P(X = r) = q^{r-1}p"),
            S("Pgf (geometric series)", math=r"G(t) = \sum_{r=1}^\infty q^{r-1}p\,t^r = pt\sum_{r=0}^\infty (qt)^r = \frac{pt}{1 - qt}"),
            S("Differentiate", math=r"G'(t) = \frac{p}{(1 - qt)^2}, \quad G''(t) = \frac{2pq}{(1 - qt)^3}"),
            S("At $t = 1$ ($1 - q = p$)", math=r"G'(1) = \frac{p}{p^2} = \frac1p = 6, \qquad G''(1) = \frac{2pq}{p^3} = \frac{2q}{p^2} = 60"),
            S("Variance", math=r"\operatorname{Var}(X) = 60 + 6 - 36 = 30 = \frac{q}{p^2}"),
        ], check=r"\frac{q}{p^2} = \frac{5/6}{1/36} = 30 \ \checkmark"),
        H("Sums of independent random variables"),
        D(r"If $X$ and $Y$ are **independent**, then $E(t^{X + Y}) = E(t^X)E(t^Y)$, so", title="Sum of independent variables",
          formula=r"G_{X + Y}(t) = G_X(t)\,G_Y(t)",
          note="This extends to any number of independent variables: n identical independent copies give G(t) to the power n."),
        EX("Worked example 3: sum of two dice", intro=r"$X$ and $Y$ are the scores on two fair six-sided dice. Use pgfs to find $P(X + Y = 7)$ and the mean of the total.", steps=[
            S("Pgf of one die", math=r"G(t) = \tfrac16\left(t + t^2 + t^3 + t^4 + t^5 + t^6\right)"),
            S("Pgf of the total", math=r"G_{X+Y}(t) = \left[G(t)\right]^2 = \tfrac{1}{36}\left(t + \cdots + t^6\right)^2"),
            S("Coefficient of $t^7$: pairs $(1,6), (2,5), \\ldots, (6,1)$", math=r"P(X + Y = 7) = \tfrac{6}{36} = \tfrac16"),
            S("Mean of the total", math=r"E(X + Y) = 2G'(1)G(1) = 2 \times 3.5 = 7"),
        ], check=r"\text{Sum of the coefficients } = \tfrac{1}{36}(36) = 1 \ \checkmark"),
        EX("Worked example 4: Poisson sums", intro=r"The number of customers arriving at a kiosk before noon is Poisson with mean $2$ and after noon is Poisson with mean $3$, independently. Find the distribution of the daily total and $P(\text{no customers})$.", steps=[
            S("Multiply the pgfs", math=r"G(t) = e^{2(t - 1)}\,e^{3(t - 1)} = e^{5(t - 1)}"),
            S("Recognise", text="This is the pgf of a Poisson distribution with mean $5$: the sum of independent Poisson variables is Poisson with the means added."),
            S("$P(0)$ is the constant term", math=r"G(0) = e^{-5} = 0.00674"),
        ]),
        MISTAKE("Using G'(1) for the variance", r"$G'(1)$ is the **mean**. The variance is $G''(1) + G'(1) - [G'(1)]^2$. Forgetting the $+G'(1)$ or the square is the most common error."),
        MISTAKE("Multiplying pgfs when the variables are not independent", r"$G_{X+Y} = G_XG_Y$ requires independence. For example $X + X = 2X$ is not obtained by squaring $G_X$ (that would give the sum of two **independent** copies)."),
        MISTAKE("Starting the geometric at 0", r"With $X$ = number of trials up to and including the first success, $X$ starts at $1$ and $G(t) = \dfrac{pt}{1 - qt}$. If $X$ counts the failures before the first success it starts at $0$ and $G(t) = \dfrac{p}{1 - qt}$. Read the definition in the question."),
        QUIZ(r"A random variable has pgf $G(t) = \dfrac{1}{4}(1 + t)^2$. What is $P(X = 1)$?",
             [r"$\dfrac14$", r"$\dfrac12$", r"$\dfrac34$", r"$1$"], 1,
             r"$G(t) = \frac14 + \frac12 t + \frac14 t^2$. The coefficient of $t$ is $\frac12$.", hint="Expand G(t) and read off the coefficient of t.",
             feedback=["That is $P(X = 0)$.", "", "That is $G(1) - P(X = 0)$, not a coefficient.", "That is $G(1)$."]),
        QUIZ(r"$X$ has pgf $G(t) = e^{4(t - 1)}$. Then $E(X)$ and $\operatorname{Var}(X)$ are:",
             ["$4$ and $4$", "$4$ and $16$", "$e^4$ and $e^4$", "$4$ and $0$"], 0,
             r"$G'(t) = 4e^{4(t-1)}$, $G'(1) = 4$; $G''(1) = 16$; $\operatorname{Var} = 16 + 4 - 16 = 4$ (a Poisson distribution).", hint="Differentiate twice and use the formula.",
             feedback=["", "That forgets $+G'(1) - [G'(1)]^2$ and reports $G''(1)$.", "You evaluated $e^{4}$, but at $t = 1$ the exponent is $0$.", "The variance is $G''(1) + G'(1) - 16 = 4$."]),
        H("Practice questions"),
        PQ(r"The pgf of $X$ is $G(t) = k(1 + t + 2t^2)$. Find $k$, the mean and the variance.",
           r"$G(1) = 4k = 1$, so $k = \frac14$. $G(t) = \frac14 + \frac14 t + \frac12 t^2$. $G'(t) = \frac14 + t$, $G'(1) = 1.25$. $G''(t) = 1$. Variance $= 1 + 1.25 - 1.5625 = 0.6875$."),
        PQ(r"Show that the pgf of $B(n, p)$ is $(q + pt)^n$ and use it to show the mean is $np$ and the variance is $npq$.",
           r"$G(t) = \sum \binom{n}{r}p^r q^{n-r}t^r = (q + pt)^n$ (binomial theorem). $G'(t) = np(q + pt)^{n-1}$, $G'(1) = np$. $G''(1) = n(n-1)p^2$. Variance $= n(n-1)p^2 + np - n^2p^2 = np - np^2 = npq$."),
        PQ(r"$X \sim B(3, 0.5)$ and $Y \sim B(2, 0.5)$ are independent. Find the pgf of $X + Y$ and hence $P(X + Y = 4)$.",
           r"$G_{X+Y} = (0.5 + 0.5t)^3(0.5 + 0.5t)^2 = (0.5 + 0.5t)^5$, the pgf of $B(5, 0.5)$. $P(X + Y = 4) = \binom{5}{4}(0.5)^5 = \frac{5}{32} = 0.156$."),
        PQ(r"The pgf of the number of heads when a coin is tossed three times is $\frac18(1 + t)^3$. Two independent such experiments are done and $S$ is the total number of heads. Find $E(S)$ and $P(S = 6)$.",
           r"$G_S = \left[\frac18(1+t)^3\right]^2 = \frac{1}{64}(1+t)^6$, the pgf of $B(6, \frac12)$. $E(S) = 3$ and $P(S = 6) = \frac{1}{64}$."),
        H("Summary"),
        SUM(r"$G_X(t) = E(t^X) = \sum p_r t^r$; $G(1) = 1$ and the coefficient of $t^r$ is $P(X = r)$.",
            r"Mean $= G'(1)$; variance $= G''(1) + G'(1) - [G'(1)]^2$.",
            r"Binomial $(q + pt)^n$; geometric $\dfrac{pt}{1 - qt}$; Poisson $e^{\lambda(t - 1)}$.",
            r"For independent $X, Y$: $G_{X+Y} = G_XG_Y$.",
            "Always check G(1) = 1 and state the independence you use."),
    ],
))


# ================================================================ Examination
LESSONS.append(lesson(
    module="Examination", topic="Paper 1",
    title="Paper 1 strategy: multiple-choice Further Mathematics questions",
    slug="fmxu-exam-paper-1-multiple-choice-strategy",
    minutes=22,
    summary="Plan your time on a multiple-choice Further Mathematics paper and use numerical checks, elimination and the typical wrong answers to choose the right option quickly and safely across all six Upper Sixth modules.",
    objectives=[
        "Plan time on a paper of 50 multiple-choice questions using KKEVO's practice timing",
        "Use numerical substitution, small test values and quick checks (rank plus nullity, Lagrange) to confirm or reject options",
        "Recognise the wrong answers that common slips produce in calculus, differential equations, groups, vector spaces, numerical methods and mechanics",
        "Avoid the errors the Board's report lists: mixing Simpson with trapezium, Maclaurin with Taylor, and constant with variable acceleration",
    ],
    key_concepts=["Multiple-choice strategy", "Numerical checking", "Elimination", "Distractors", "Time management", "Quick checks"],
    blocks=[
        H("Introduction"),
        T("Paper 1 is a multiple-choice paper. Each question has four options and one is correct. The wrong options are not random: each is the answer you get from a common slip, so a candidate who works carelessly is led straight to a wrong option. A good routine turns this around: you can use the options to check your answer."),
        T("This lesson gives that routine and applies it to all six modules of the Upper Sixth: calculus, differential equations, groups, vector spaces, numerical methods, and mechanics and probability."),
        H("Planning your time"),
        KEY("KKEVO practice settings", "In KKEVO practice, Paper 1 mock A has 50 four-option questions and a time limit of 90 minutes. These are KKEVO practice settings, not official examination times: read the instructions on your own paper.", cards=[
            ["Time per question", r"$90 \div 50 = 1.8$ minutes: about 100 seconds each."],
            ["First pass", "Answer every question you can do within 2 minutes. Flag the rest and move on."],
            ["Second pass", "Use the time you saved on the flagged questions."],
            ["Last 5 minutes", "Fill every answer. Re-check anything involving a calculator, a sign or a unit."],
        ]),
        TIP("Exam link: Paper 1 (multiple choice) tests every module with short questions, so the final answer is what counts and a quick method beats a long one. Further Mathematics papers also include written pure mathematics and mechanics questions and applied options: see the next lesson. Unless your paper's instructions say otherwise, answer every question."),
        H("The routine"),
        D("Use these four steps on every question:", title="Read, predict, eliminate, check",
          formula=r"\text{1. Read}\ \to\ \text{2. Predict}\ \to\ \text{3. Eliminate}\ \to\ \text{4. Check}",
          note="Read what is asked (and its units). Predict the kind of answer and its rough size before you look at the options. Eliminate impossible options. Check the survivor by a second method."),
        H("Technique 1: substitute a number"),
        T(r"For limits, series and identities, a calculator can test an option. Put in a small value of $x$ and compare."),
        EX("Worked example 1: a limit by test value", intro=r"Find $\displaystyle\lim_{x \to 0}\frac{e^x - 1 - x}{x^2}$.  A: $0$   B: $\tfrac12$   C: $1$   D: $\infty$", steps=[
            S("Predict", text=r"Both numerator and denominator tend to $0$: use the Maclaurin series $e^x = 1 + x + \frac{x^2}{2} + \cdots$ (or L'Hopital twice)."),
            S("Series", math=r"\frac{e^x - 1 - x}{x^2} = \frac{\frac{x^2}{2} + \frac{x^3}{6} + \cdots}{x^2} = \frac12 + \frac{x}{6} + \cdots \to \frac12"),
            S("Test a value", math=r"x = 0.01: \quad \frac{e^{0.01} - 1 - 0.01}{0.0001} = 0.5017", text="The value is close to $0.5$. Answer **B**."),
        ], check=r"x = -0.01:\ \frac{e^{-0.01} - 1 + 0.01}{0.0001} = 0.4983"),
        H("Technique 2: quick structural checks"),
        T(r"Pure mathematics at this level has built-in checks that cost a few seconds. **Rank-nullity**: for a matrix with $n$ columns, rank $+$ nullity $= n$. **Lagrange**: the order of a subgroup or element divides the order of the group. **Dimension count**: more than $n$ vectors in an $n$-dimensional space are dependent."),
        EX("Worked example 2: use Lagrange to eliminate", intro=r"$G$ is a group of order $15$. Which cannot be the order of an element of $G$?  A: $3$   B: $5$   C: $15$   D: $4$", steps=[
            S("The order of an element equals the order of the cyclic subgroup it generates", text="By Lagrange's theorem this must divide $15$."),
            S("Divisors of 15", math=r"1,\ 3,\ 5,\ 15"),
            S("Eliminate", text="$4$ does not divide $15$, so no element has order 4. Answer **D**."),
        ]),
        EX("Worked example 3: rank-nullity check", intro=r"A linear map $T : \mathbb{R}^5 \to \mathbb{R}^3$ has rank $2$. What is the dimension of its kernel?  A: $1$   B: $2$   C: $3$   D: $5$", steps=[
            S("Rank-nullity", math=r"\text{rank} + \text{nullity} = \dim(\text{domain}) = 5"),
            S("Solve", math=r"\text{nullity} = 5 - 2 = 3", text="Answer **C**. The wrong options: $2$ is the rank; $5$ is the dimension of the domain; $1$ comes from using $3 - 2$ (the dimension of the codomain)."),
        ]),
        H("Technique 3: know the wrong answers"),
        T("Each option is a plausible slip. Ask yourself which slip produces each distractor: if you can explain every wrong option you have probably understood the question."),
        KEY("Typical traps by module", "A short checklist to run through before the paper.", cards=[
            ["Calculus", r"Maclaurin expands about $0$, Taylor about $a$: a series 'in powers of $(x - 2)$' is a Taylor series. The derivative of $\arcsin(2x)$ has a factor $2$. Check limits of integration after a substitution."],
            ["Differential equations", r"Linear first order: multiply by the integrating factor on **both** sides. Bernoulli: $v = y^{1-n}$. Second order: check the sign of the discriminant before choosing the form of solution."],
            ["Groups", r"Closure, associativity, identity, inverse: a single missing inverse (such as $0$ under multiplication) rules a set out. Check the order of an element with $\operatorname{lcm}$ for permutations."],
            ["Vector spaces", r"Rank-nullity gives the nullity from the rank. A subspace must contain $\mathbf{0}$. Use the **original** columns for a basis of the range."],
            ["Numerical methods", r"$n$ strips give $n + 1$ ordinates and $h = (b - a)/n$. Simpson needs an even number of strips. Newton-Raphson subtracts $f/f'$."],
            ["Mechanics and probability", r"Radial acceleration is $\ddot r - r\dot\theta^2$, not $\ddot r$. In oblique impacts only the component along the line of centres changes. $G'(1)$ is the mean, not the variance."],
        ]),
        MISTAKE("Confusing Simpson's rule with the trapezium rule", r"The Board's report notes that candidates mix up the two rules and miscalculate the step length. Trapezium: $\frac{h}{2}[\text{ends} + 2(\text{inner})]$. Simpson: $\frac{h}{3}[\text{ends} + 4(\text{odd}) + 2(\text{even inner})]$. If you apply the wrong pattern, one of the distractors will match it."),
        MISTAKE("Using a Maclaurin series when the question needs a Taylor series", r"The Board's report notes that some candidates use the Maclaurin series where a Taylor series about another point is required. If the question says 'about $x = a$' or 'in powers of $(x - a)$', replace $x$ by $(x - a)$ in the derivatives' evaluation: $f(a), f'(a), \ldots$"),
        MISTAKE("Treating variable acceleration as constant", r"The Board's report notes that candidates fail to see when the acceleration is variable. If $a$ depends on $t$, $x$ or $v$ (as for a rocket, or $a = 4 - 2t$), the formulae $v = u + at$ and $s = ut + \frac12at^2$ do not apply: integrate."),
        QUIZ(r"You have $50$ questions and $90$ minutes (KKEVO practice setting). After $45$ minutes you have answered $20$ questions. What is the best action?",
             ["Slow down to avoid mistakes", "Move on from any question you cannot do in about 2 minutes, then return to flagged questions", "Leave the last 10 questions blank", "Spend 5 minutes on every remaining question"], 1,
             "20 questions in 45 minutes is 2.25 minutes each: slightly slow. Use the two-pass method and flag the hard ones.", hint="Use the two-pass method.",
             feedback=["That would reduce the number of questions answered further.", "", "A blank scores nothing. Unless your paper says otherwise, attempt every question.", "Only 9 questions could then be answered in the remaining time."]),
        QUIZ(r"A matrix $A$ is $3 \times 4$. Its kernel has dimension $2$. What is the rank?",
             ["$1$", "$2$", "$3$", "$6$"], 1,
             r"Rank $= 4 - 2 = 2$ (the domain is $\mathbb{R}^4$).", hint="Rank plus nullity equals the number of columns.",
             feedback=["That is $3 - 2$, using the number of rows instead of columns.", "", "That is the number of rows.", "That adds the two numbers instead of subtracting."]),
        H("Practice questions"),
        PQ(r"$\displaystyle\int_0^1 x e^x\,dx$ equals: A: $e - 1$, B: $1$, C: $e$, D: $\tfrac12$. Choose and justify with a second method.",
           r"Integration by parts: $[xe^x - e^x]_0^1 = (e - e) - (0 - 1) = 1$. Answer B. Check: $x e^x \approx 0.5$ near $x = 0.5$ (value $0.82$) and the integral of a function that rises from $0$ to $2.7$ over $[0, 1]$ is about $1$. $e - 1$ comes from $\int e^x\,dx$."),
        PQ(r"The order of the permutation $(1\ 2\ 3)(4\ 5)$ is A: $5$, B: $6$, C: $2$, D: $3$.",
           r"The order of a product of disjoint cycles is the lcm of the cycle lengths: $\operatorname{lcm}(3, 2) = 6$. Answer B. (A is the number of points moved, C and D are the order of one cycle only.)"),
        PQ(r"The trapezium rule with $4$ strips is applied to $\displaystyle\int_0^2 x^2\,dx$. The estimate is A: $2.5$, B: $2.75$, C: $2.67$, D: $3$.",
           r"$h = 0.5$; ordinates $0, 0.25, 1, 2.25, 4$. $\frac{0.5}{2}[0 + 4 + 2(0.25 + 1 + 2.25)] = 0.25 \times 11 = 2.75$. Answer B. C is the exact value $\frac83$; the trapezium rule over-estimates for the convex curve $y = x^2$, so the estimate must be above $2.67$."),
        H("Summary"),
        SUM(r"Plan about 100 seconds a question (KKEVO practice setting: 90 minutes for 50): first pass, flag, second pass.",
            "Read, predict, eliminate, check: predict before you look at the options.",
            "Use quick structural checks: rank plus nullity, Lagrange's theorem, dimension counts, the shape of the answer.",
            "Test a small value numerically to confirm limits, series and identities.",
            "Learn the traps: Simpson against trapezium, Maclaurin against Taylor, constant against variable acceleration."),
    ],
))

LESSONS.append(lesson(
    module="Examination", topic="Paper 2",
    title="Paper 2: structured pure mathematics and mechanics questions",
    slug="fmxu-exam-paper-2-structured-questions",
    minutes=24,
    summary="Set out multi-part Further Mathematics questions clearly: show-that questions, numerical tables, modelling in mechanics, recognising the right distribution, exact answers and checking.",
    objectives=[
        "Read a multi-part question and see how the parts build on each other",
        "Answer show-that questions with full working, without recopying what was to be proved",
        "Present numerical methods in tables with correct step length, rounding and conclusion",
        "State modelling assumptions in mechanics and recognise the correct probability distribution",
    ],
    key_concepts=["Structured question", "Show that", "Numerical table", "Modelling assumptions", "Choice of distribution", "Checking"],
    blocks=[
        H("Introduction"),
        T("Written papers in Further Mathematics ask structured questions: one situation, then parts (a), (b), (c). The Board's report shows a paper with eight questions covering pure mathematics, mechanics, numerical work and probability. The early parts are usually a stepping stone for the later ones, and working is part of the answer."),
        H("Timing and layout"),
        KEY("KKEVO practice settings", "KKEVO's Paper 2 practice paper has about 25 auto-marked parts in 7 numbered questions and a time limit of 150 minutes. These are KKEVO practice settings, not official examination times: read the instructions on your own paper.", cards=[
            ["Time per part", r"$150 \div 25 = 6$ minutes a part on average; short parts take less."],
            ["Read first", "Read the whole question, including the last part: it shows where the question is heading."],
            ["Show working", "Write each step on its own line. A correct method with an arithmetic slip still earns credit; a bare wrong answer does not."],
            ["Carry forward", "If part (a) gives a value you need in part (b), use it even if you could not prove part (a)."],
        ]),
        TIP("Exam link: written questions on this paper's topics are Paper 2 (pure mathematics and mechanics, with applied options). The same topics appear as multiple-choice questions in Paper 1. A written answer must show the method: a final number alone is not enough."),
        H("Command words"),
        D(r"**Show that**: the answer is given; reach it with every step of the working. **Hence**: use the previous result. **Find / Calculate**: a value is needed. **Estimate**: use a numerical method and state the accuracy. **Exact**: leave the answer in terms of $\pi$, $e$, $\ln$, surds or fractions. **State**: no working required, but give the assumption or value clearly.", title="Words to look for"),
        EX("Worked example 1: show that, then hence", intro=r"(a) Show that the Maclaurin series of $e^x\sin x$ begins $x + x^2 + \tfrac13x^3 + \cdots$. (b) Hence find $\displaystyle\lim_{x \to 0}\frac{e^x\sin x - x}{x^2}$.", steps=[
            S("(a) Write the two series", math=r"e^x = 1 + x + \frac{x^2}{2} + \cdots, \qquad \sin x = x - \frac{x^3}{6} + \cdots"),
            S("Multiply, collecting powers up to $x^3$", math=r"e^x\sin x = x + x^2 + \left(\frac12 - \frac16\right)x^3 + \cdots = x + x^2 + \frac13x^3 + \cdots", text="This is the stated result: each coefficient is shown, not copied."),
            S("(b) Use the result", math=r"\frac{e^x\sin x - x}{x^2} = \frac{x^2 + \frac13x^3 + \cdots}{x^2} = 1 + \frac13x + \cdots \to 1"),
        ], check=r"x = 0.01: \ \frac{e^{0.01}\sin0.01 - 0.01}{0.0001} = 1.0033"),
        H("Numerical methods in a written paper"),
        T(r"Numerical questions test method as much as arithmetic. Always write the step length, the ordinates in a table, the formula with the numbers substituted, and a conclusion in a sentence. Round only at the end."),
        EX("Worked example 2: Simpson's rule and Newton-Raphson", intro=r"(a) Use Simpson's rule with $4$ strips to estimate $\displaystyle\int_0^1\frac{4}{1 + x^2}\,dx$. (b) Use Newton-Raphson on $f(x) = x^3 - 2x - 5$ from $x_0 = 2$ to find $x_2$ to 4 decimal places.", steps=[
            S("(a) Step length", math=r"h = \frac{1 - 0}{4} = 0.25"),
            S("Ordinates", math=r"y_0 = 4,\ y_1 = 3.76471,\ y_2 = 3.2,\ y_3 = 2.56,\ y_4 = 2"),
            S("Simpson", math=r"\frac{0.25}{3}\left[4 + 2 + 4(3.76471 + 2.56) + 2(3.2)\right] = \frac{0.25}{3}(37.69882) = 3.1416", text=r"The exact value is $\pi = 3.14159$."),
            S("(b) $f'(x) = 3x^2 - 2$", math=r"x_1 = 2 - \frac{-1}{10} = 2.1, \qquad x_2 = 2.1 - \frac{0.061}{11.23} = 2.0946"),
        ], check=r"f(2.0946) = 9.1897 - 4.1892 - 5 = 0.0005 \approx 0"),
        H("Mechanics: model, then calculate"),
        T(r"State what you assume (constant gravity, no air resistance, smooth surfaces, a particle). Decide whether the acceleration is constant: if it depends on $t$, integrate."),
        EX("Worked example 3: variable acceleration", intro=r"A particle moves on a straight line with acceleration $a = 4 - 2t$ m/s$^2$. When $t = 0$ it is at the origin with velocity $1$ m/s. Find its velocity and displacement at $t = 3$.", steps=[
            S("Integrate the acceleration", math=r"v = \int (4 - 2t)\,dt = 4t - t^2 + c, \quad v(0) = 1 \Rightarrow c = 1"),
            S("Velocity at $t = 3$", math=r"v = 12 - 9 + 1 = 4\ \text{m/s}"),
            S("Integrate again", math=r"x = \int (1 + 4t - t^2)\,dt = t + 2t^2 - \frac{t^3}{3}, \quad x(0) = 0"),
            S("Displacement at $t = 3$", math=r"x = 3 + 18 - 9 = 12\ \text{m}"),
        ], check=r"\text{The suvat formula } s = ut + \tfrac12 at^2 \text{ would be wrong: } a \text{ is not constant}"),
        H("Probability: choose the distribution"),
        T(r"The Board's report notes that many candidates did not recognise a binomial situation: some used the geometric distribution and others a Poisson approximation even when $n$ was small. Ask: is there a fixed number of independent trials, each with two outcomes and the same probability? If so, it is binomial. A geometric distribution counts trials up to the first success. A Poisson approximation to a binomial needs $n$ large and $p$ small. A normal approximation to a binomial needs a **continuity correction**: $P(X \ge 24)$ becomes $P(Y \ge 23.5)$."),
        EX("Worked example 4: binomial with a normal approximation", intro=r"$X \sim B(40, 0.5)$. Use a normal approximation to estimate $P(X \ge 24)$, and compare with the exact value $0.1341$.", steps=[
            S("Parameters", math=r"\mu = np = 20, \quad \sigma^2 = npq = 10"),
            S("Continuity correction", math=r"P(X \ge 24) \approx P(Y \ge 23.5), \quad Y \sim N(20, 10)"),
            S("Standardise", math=r"z = \frac{23.5 - 20}{\sqrt{10}} = 1.107 \Rightarrow P(Z \ge 1.107) = 0.134"),
        ], check=r"\text{Without the correction: } z = \frac{24 - 20}{\sqrt{10}} = 1.265 \Rightarrow 0.103, \text{ noticeably worse}"),
        MISTAKE("Recopying what you were asked to prove", r"The Board's report says that most candidates scored poorly on a show-that question because they simply recopied the result. Start from the given information, show each step (in Example 1, the multiplication of the two series) and end on the given statement."),
        MISTAKE("Using a formula for an unusual case instead of the data", r"The Board's report notes that, when the acceleration and displacement were given, candidates used $v = \omega\sqrt{a^2 - x^2}$ and $T = 2\pi\sqrt{l/g}$ instead of $a = -\omega^2 x$ to find $\omega$. Read what is given and pick the formula that uses it directly."),
        MISTAKE("Mistaking components of velocity for speed", r"The Board's report notes that candidates mistook the components of velocity for speed. The speed is $\sqrt{v_r^2 + v_\theta^2}$ in polar coordinates, or the magnitude of the resultant after an impact."),
        QUIZ(r"A question says: 'Show that $\int_0^1 xe^x\,dx = 1$.' Which answer earns full marks?",
             ["Write $1 = 1$", "Use integration by parts, show $[xe^x - e^x]_0^1$ and evaluate each limit", "State that the integral is $1$ because the question says so", "Use the trapezium rule with 4 strips"], 1,
             "A show-that question needs the full working to the given result; a numerical estimate does not prove it.", hint="What does 'show that' require?",
             feedback=["That is recopying the target.", "", "That assumes what you must prove.", "An estimate does not prove an exact value."]),
        QUIZ(r"In a numerical-integration question the table has $9$ ordinates. The step length for $\displaystyle\int_1^5$ is:",
             ["$0.5$", "$0.4$", "$0.444$", "$4$"], 0,
             r"$9$ ordinates give $8$ strips: $h = \frac{5 - 1}{8} = 0.5$.", hint="Strips = ordinates - 1.",
             feedback=["", "That divides by 10 strips.", "That divides by 9, the number of ordinates.", "That is the interval length."]),
        H("Practice questions"),
        PQ(r"(a) Use the Taylor series of $\ln x$ about $x = 1$ to write the first three non-zero terms. (b) Use them to estimate $\ln 1.2$ and compare with the calculator value $0.18232$.",
           r"(a) $f = \ln x$, $f(1) = 0$, $f' = 1/x$, $f'(1) = 1$, $f'' = -1/x^2$, $f''(1) = -1$, $f''' = 2/x^3$, $f'''(1) = 2$. So $\ln x = (x - 1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \cdots$. (b) With $x - 1 = 0.2$: $0.2 - 0.02 + 0.002667 = 0.18267$. The error is $0.0003$, from the next term $-\frac{0.2^4}{4} = -0.0004$."),
        PQ(r"A rocket of mass $2000$ kg ejects fuel at $10$ kg/s with speed $1500$ m/s relative to it. State the assumption needed, and show that it cannot lift off from the ground ($g = 10$ m/s$^2$).",
           r"Assume uniform gravity, no air resistance and a constant burn rate. Thrust $= uk = 15\,000$ N; weight $= 2000 \times 10 = 20\,000$ N. Since $uk < mg$ the net force on the rocket at the start is downwards (the ground supports it) and the rocket stays on the ground."),
        PQ(r"A smooth sphere of mass $2$ kg moving at $8$ m/s hits a stationary smooth sphere of mass $1$ kg. Its velocity makes $30^\circ$ with the line of centres and $e = 0.5$. Find the speed of the $1$ kg sphere after the impact and the kinetic energy lost.",
           r"Along the line the $2$ kg sphere has $8\cos30^\circ = 6.928$. Momentum: $2(6.928) = 2v_A + v_B$. Restitution: $v_B - v_A = 0.5(6.928)$. So $v_B = 6.93$ m/s and $v_A = 3.46$ m/s. KE before $= 64$ J; after $= \frac12(2)(3.46^2 + 4^2) + \frac12(1)(6.93^2) = 28 + 24 = 52$ J; lost $= 12$ J."),
        PQ(r"The number of heads in $3$ tosses of a fair coin has pgf $\frac18(1 + t)^3$. Find the pgf of the total number of heads in $9$ tosses and hence $P(\text{exactly } 5)$ heads.",
           r"Three independent experiments: $\left[\frac18(1 + t)^3\right]^3 = \frac{1}{512}(1 + t)^9$. The coefficient of $t^5$ is $\frac{\binom95}{512} = \frac{126}{512} = 0.246$."),
        H("Summary"),
        SUM("Read the whole question first and carry values forward from earlier parts.",
            "Show that: start from the given data, show every step and reach the result; never just recopy it.",
            "Numerical methods: state h, tabulate the ordinates or iterates, substitute into the formula, round at the end and give a conclusion.",
            "Mechanics: state your model, decide whether the acceleration is constant, and use the formula that uses what you are given.",
            "Probability: decide the distribution from the situation; use a continuity correction for a normal approximation to a discrete variable."),
    ],
))

