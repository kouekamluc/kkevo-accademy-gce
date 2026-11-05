"""Form 5 General Mathematics (O Level 570): Matrices & Vectors, Trigonometry & Bearings,
Circle Theorems, Statistics & Probability. Draft content for review in the studio."""
from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

LESSONS = [
    # ------------------------------------------------------------------ 2×2 matrices
    lesson(
        module="Matrices & Vectors",
        topic="2×2 matrices",
        title="2×2 matrices: operations, determinant, inverse and simultaneous equations",
        slug="two-by-two-matrices",
        minutes=30,
        summary="Add, subtract and multiply 2×2 matrices, find the determinant and inverse, and use the inverse to solve a pair of simultaneous equations.",
        objectives=[
            "Add, subtract and multiply 2×2 matrices and multiply a matrix by a number",
            "Find the determinant of a 2×2 matrix and decide if it is singular",
            "Find the inverse of a 2×2 matrix",
            "Solve two simultaneous linear equations using the inverse matrix",
        ],
        key_concepts=["Matrix", "Order of a matrix", "Matrix multiplication", "Determinant",
                      "Singular matrix", "Inverse matrix", "Identity matrix"],
        blocks=[
            H("Introduction"),
            T("A **matrix** is a rectangular array of numbers. It is a neat way to store and work with "
              "several numbers at once."),
            T("For example, a trader in Bafoussam sells rice and beans on Monday and Tuesday. The bags "
              "sold each day can be written in one matrix. Matrices also give a quick method for solving "
              "simultaneous equations, which you will see at the end of this lesson."),
            D("A **matrix** with 2 rows and 2 columns is a **2×2 matrix**. Its **order** is 2×2 "
              "(rows first, then columns).", formula=r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}",
              note=r"The **identity matrix** $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ behaves like the number 1: $AI = IA = A$."),
            H("Adding, subtracting and multiplying by a number"),
            T("To add or subtract two matrices of the same order, add or subtract the numbers in the same "
              "positions. To multiply a matrix by a number $k$, multiply every entry by $k$."),
            F(r"\begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} + \begin{pmatrix} 1 & -2 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 4 & -1 \\ 2 & 9 \end{pmatrix}, \qquad 3\begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix} = \begin{pmatrix} 9 & 3 \\ 6 & 12 \end{pmatrix}"),
            H("Multiplying two matrices"),
            T("To multiply, take a **row** of the first matrix and a **column** of the second. Multiply "
              "matching entries and add. This gives one entry of the answer."),
            F(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} p & q \\ r & s \end{pmatrix} = \begin{pmatrix} ap + br & aq + bs \\ cp + dr & cq + ds \end{pmatrix}"),
            EX("Worked example 1: multiplying matrices", intro=(
                r"Given $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -2 \\ 0 & 5 \end{pmatrix}$, find $AB$."),
               steps=[
                   S("Row 1 of A times column 1 of B", math=r"3(1) + 1(0) = 3"),
                   S("Row 1 of A times column 2 of B", math=r"3(-2) + 1(5) = -6 + 5 = -1"),
                   S("Row 2 of A times column 1 of B", math=r"2(1) + 4(0) = 2"),
                   S("Row 2 of A times column 2 of B", math=r"2(-2) + 4(5) = -4 + 20 = 16"),
                   S("Write the answer", math=r"AB = \begin{pmatrix} 3 & -1 \\ 2 & 16 \end{pmatrix}"),
               ]),
            MISTAKE("Thinking AB = BA", r"In general $AB \neq BA$. With the matrices above, "
                    r"$BA = \begin{pmatrix} -1 & -7 \\ 10 & 20 \end{pmatrix}$, which is different. Always keep the order given in the question."),
            H("Determinant and inverse"),
            D(r"The **determinant** of $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is", title="Determinant",
              formula=r"\det A = |A| = ad - bc",
              note="If $\\det A = 0$ the matrix is **singular** and has no inverse."),
            D("The **inverse** $A^{-1}$ is the matrix with $AA^{-1} = A^{-1}A = I$. Swap $a$ and $d$, change the signs of $b$ and $c$, and divide by the determinant.",
              title="Inverse of a 2×2 matrix",
              formula=r"A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}"),
            QUIZ(r"What is the determinant of $\begin{pmatrix} 5 & 2 \\ 3 & 2 \end{pmatrix}$?",
                 ["$4$", "$16$", "$-4$", "$1$"], 0,
                 r"$ad - bc = 5(2) - 2(3) = 10 - 6 = 4$.",
                 hint="Multiply down the leading diagonal, then subtract the other diagonal.",
                 feedback=["", "You added the two products. The determinant is $ad - bc$, a subtraction.",
                           "You calculated $bc - ad$. The order is $ad - bc$.",
                           "You subtracted entries instead of multiplying diagonals."]),
            H("Solving simultaneous equations with matrices"),
            T(r"Write the equations as $A\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h \\ k \end{pmatrix}$. "
              r"Then multiply both sides on the **left** by $A^{-1}$ to get $\begin{pmatrix} x \\ y \end{pmatrix} = A^{-1}\begin{pmatrix} h \\ k \end{pmatrix}$."),
            EX("Worked example 2: simultaneous equations", intro="Use a matrix method to solve $2x + 3y = 13$ and $x - y = -1$.",
               steps=[
                   S("Write in matrix form", math=r"\begin{pmatrix} 2 & 3 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 13 \\ -1 \end{pmatrix}"),
                   S("Find the determinant", math=r"2(-1) - 3(1) = -2 - 3 = -5"),
                   S("Find the inverse", math=r"A^{-1} = \frac{1}{-5}\begin{pmatrix} -1 & -3 \\ -1 & 2 \end{pmatrix}"),
                   S("Multiply the inverse by the right-hand side", math=r"\frac{1}{-5}\begin{pmatrix} -1(13) + (-3)(-1) \\ -1(13) + 2(-1) \end{pmatrix} = \frac{1}{-5}\begin{pmatrix} -10 \\ -15 \end{pmatrix}"),
                   S("Simplify", math=r"x = 2,\quad y = 3"),
               ], check=r"2(2) + 3(3) = 13 \text{ and } 2 - 3 = -1"),
            MISTAKE("Forgetting to change the signs of b and c", "Only $b$ and $c$ change sign. $a$ and $d$ swap places but keep their signs."),
            MISTAKE("Multiplying on the wrong side", r"Write $A^{-1}\begin{pmatrix} h \\ k \end{pmatrix}$, not $\begin{pmatrix} h \\ k \end{pmatrix}A^{-1}$. A 2×1 matrix times a 2×2 matrix cannot be done."),
            QUIZ(r"For which value of $x$ is $\begin{pmatrix} x & 4 \\ 3 & 6 \end{pmatrix}$ singular?",
                 ["$x = 8$", "$x = 2$", "$x = -2$", "$x = 0.5$"], 1,
                 r"Singular means $\det = 0$: $6x - 12 = 0$, so $x = 2$.",
                 feedback=["That would need $6x = 48$. The product $bc$ is $4 \\times 3 = 12$, not 48.", "",
                           "Check the sign: $6x - 12 = 0$ gives $6x = 12$, so $x$ is positive.",
                           "You divided 3 by 6. Solve $6x = 12$."]),
            H("Practice questions"),
            PQ(r"Find the inverse of $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$.",
               r"Determinant $= 2(3) - 1(5) = 1$. So the inverse is $\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$. "
               r"Check: $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$."),
            PQ(r"Given $M = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, find $M^2$.",
               r"$M^2 = MM = \begin{pmatrix} 1(1) + 2(0) & 1(2) + 2(1) \\ 0(1) + 1(0) & 0(2) + 1(1) \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$. "
               "Note that you do not just square each entry."),
            PQ("At a market in Ebolowa, 2 pineapples and 3 avocados cost 1300 FCFA. 3 pineapples and 1 avocado cost 1250 FCFA. "
               "(a) Write this as a matrix equation. (b) Use the inverse matrix to find the price of one pineapple and one avocado.",
               r"(a) Let $p$ and $a$ be the prices in FCFA: $\begin{pmatrix} 2 & 3 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} p \\ a \end{pmatrix} = \begin{pmatrix} 1300 \\ 1250 \end{pmatrix}$. "
               r"(b) Determinant $= 2(1) - 3(3) = -7$. Inverse $= \frac{1}{-7}\begin{pmatrix} 1 & -3 \\ -3 & 2 \end{pmatrix}$. "
               r"Then $\begin{pmatrix} p \\ a \end{pmatrix} = \frac{1}{-7}\begin{pmatrix} 1300 - 3750 \\ -3900 + 2500 \end{pmatrix} = \frac{1}{-7}\begin{pmatrix} -2450 \\ -1400 \end{pmatrix} = \begin{pmatrix} 350 \\ 200 \end{pmatrix}$. "
               "A pineapple costs 350 FCFA and an avocado costs 200 FCFA. Check: $2(350) + 3(200) = 1300$ and $3(350) + 200 = 1250$."),
            SUM("Add or subtract matrices entry by entry; multiply rows by columns.",
                "Matrix multiplication is not commutative: usually $AB \\neq BA$.",
                "The determinant of $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ is $ad - bc$; if it is 0 the matrix is singular.",
                "Inverse: swap $a$ and $d$, change the signs of $b$ and $c$, divide by the determinant.",
                "To solve simultaneous equations, multiply both sides on the left by $A^{-1}$ and check your answers."),
        ],
    ),
    # ------------------------------------------------------------------ 2D vectors
    lesson(
        module="Matrices & Vectors",
        topic="2D vectors",
        title="Column vectors: magnitude, direction and collinearity",
        slug="column-vectors-magnitude-direction-collinearity",
        minutes=25,
        summary="Work with 2D column vectors: add them, multiply by a number, find magnitude and direction, and use vectors to show that points are collinear.",
        objectives=[
            "Write a displacement as a column vector and add, subtract and scale vectors",
            "Find the magnitude of a column vector",
            "Find the direction of a vector as an angle",
            "Use parallel vectors to show that three points are collinear",
        ],
        key_concepts=["Vector", "Column vector", "Position vector", "Magnitude", "Direction",
                      "Parallel vectors", "Collinear points"],
        blocks=[
            H("Introduction"),
            T("Some quantities need only a size, such as a price of 500 FCFA or a mass of 2 kg. Others need a "
              "size **and** a direction. A motorbike taxi that rides 4 km east and then 3 km north has a "
              "**displacement** that we describe with a vector."),
            T("In this lesson you will write vectors as columns of numbers and use them to find distances, "
              "directions and to show that points lie on one straight line."),
            D(r"A **vector** has both size and direction. In 2D we write it as a **column vector**: the top number "
              r"is the movement in the $x$-direction (right is positive) and the bottom number is the movement "
              r"in the $y$-direction (up is positive).", formula=r"\mathbf{a} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}",
              note=r"The vector from point $A$ to point $B$ is written $\overrightarrow{AB}$. The **position vector** of $A$ is $\overrightarrow{OA}$, where $O$ is the origin."),
            H("Adding, subtracting and scaling"),
            T(r"Add or subtract the top numbers together and the bottom numbers together. To multiply by a number $k$, multiply both numbers by $k$."),
            F(r"\begin{pmatrix} 2 \\ -1 \end{pmatrix} + \begin{pmatrix} -3 \\ 4 \end{pmatrix} = \begin{pmatrix} -1 \\ 3 \end{pmatrix}, \qquad 3\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 6 \\ -3 \end{pmatrix}"),
            D(r"To go from $A$ to $B$, go back to the origin and then out to $B$.", title="Vector between two points",
              formula=r"\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}"),
            H("Magnitude and direction"),
            D(r"The **magnitude** (length) of a vector comes from Pythagoras' theorem.", title="Magnitude",
              formula=r"\left|\begin{pmatrix} x \\ y \end{pmatrix}\right| = \sqrt{x^2 + y^2}",
              note=r"The **direction** can be given as the angle $\theta$ the vector makes with the positive $x$-axis, using $\tan\theta = \dfrac{y}{x}$. Draw a sketch to see which quadrant the vector is in."),
            EX("Worked example 1: magnitude and direction", intro=(
                r"A motorbike taxi's displacement is $\mathbf{a} = \begin{pmatrix} 4 \\ 3 \end{pmatrix}$ km (east, north). "
                "Find its magnitude and the angle it makes with the east direction."),
               steps=[
                   S("Square and add the components", math=r"4^2 + 3^2 = 16 + 9 = 25"),
                   S("Take the square root", math=r"|\mathbf{a}| = \sqrt{25} = 5 \text{ km}"),
                   S("Both components are positive, so the vector points up and to the right", math=r"\tan\theta = \frac{3}{4} = 0.75"),
                   S("Find the angle", math=r"\theta = \tan^{-1}(0.75) \approx 36.9^\circ \text{ north of east}"),
               ]),
            QUIZ(r"What is the magnitude of $\begin{pmatrix} -5 \\ 12 \end{pmatrix}$?",
                 ["$13$", "$7$", "$17$", r"$\sqrt{119}$"], 0,
                 r"$\sqrt{(-5)^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$.",
                 hint="Square both numbers first. A negative number squared is positive.",
                 feedback=["", "You added $-5$ and $12$. Use Pythagoras: square, add, square root.",
                           "You added 5 and 12. Magnitude is not the sum of the components.",
                           r"You worked out $144 - 25$. $(-5)^2 = +25$, so you must add."]),
            H("Parallel vectors and collinear points"),
            D(r"Two vectors are **parallel** if one is a number times the other: $\mathbf{b} = k\mathbf{a}$. "
              r"If $k$ is negative they point in opposite directions.", title="Parallel vectors"),
            D(r"Points $A$, $B$ and $C$ are **collinear** (on one straight line) if $\overrightarrow{AC} = k\,\overrightarrow{AB}$ "
              r"for some number $k$. The vectors are parallel **and** share the point $A$.", title="Collinear points"),
            EX("Worked example 2: showing points are collinear", intro=(
                "Show that $A(1, 2)$, $B(3, 5)$ and $C(7, 11)$ are collinear."),
               steps=[
                   S("Find AB", math=r"\overrightarrow{AB} = \begin{pmatrix} 3 - 1 \\ 5 - 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}"),
                   S("Find AC", math=r"\overrightarrow{AC} = \begin{pmatrix} 7 - 1 \\ 11 - 2 \end{pmatrix} = \begin{pmatrix} 6 \\ 9 \end{pmatrix}"),
                   S("Compare them", math=r"\overrightarrow{AC} = 3\begin{pmatrix} 2 \\ 3 \end{pmatrix} = 3\,\overrightarrow{AB}"),
                   S("Conclude", text="AB and AC are parallel and both pass through A, so A, B and C lie on one straight line."),
               ]),
            IMG('f5-collinear-points.svg', 'Grid with points A(1, 2), B(3, 5) and C(7, 11) on one straight line. A blue arrow from A to B goes 2 right and 3 up; a green arrow from A to C goes 6 right and 9 up. Beside the grid: AB = (2, 3) and AC = (6, 9) = 3 times (2, 3).',
                'Figure 1. AC is 3 times AB and both start at A, so A, B and C are collinear.'),
            MISTAKE("Subtracting in the wrong order", r"$\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$ (end minus start). Doing start minus end gives $\overrightarrow{BA}$, which points the other way."),
            MISTAKE("Saying 'parallel' is enough for collinear", "Parallel lines can be far apart. You must also say that the two vectors share a common point."),
            QUIZ(r"Which vector is parallel to $\begin{pmatrix} 2 \\ -3 \end{pmatrix}$?",
                 [r"$\begin{pmatrix} 4 \\ 6 \end{pmatrix}$", r"$\begin{pmatrix} -4 \\ 6 \end{pmatrix}$",
                  r"$\begin{pmatrix} 3 \\ -2 \end{pmatrix}$", r"$\begin{pmatrix} 6 \\ 9 \end{pmatrix}$"], 1,
                 r"$\begin{pmatrix} -4 \\ 6 \end{pmatrix} = -2\begin{pmatrix} 2 \\ -3 \end{pmatrix}$, so it is parallel (opposite direction).",
                 feedback=["The top is multiplied by 2 but the bottom by $-2$. Both must use the same number.", "",
                           "The numbers are swapped, not multiplied by one number.",
                           "Top times 3, bottom times $-3$: not the same number."]),
            H("Practice questions"),
            PQ(r"Given $\mathbf{p} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$ and $\mathbf{q} = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$, find $2\mathbf{p} + \mathbf{q}$ and its magnitude.",
               r"$2\mathbf{p} + \mathbf{q} = \begin{pmatrix} 4 \\ -2 \end{pmatrix} + \begin{pmatrix} -3 \\ 4 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$. "
               r"Magnitude $= \sqrt{1^2 + 2^2} = \sqrt{5} \approx 2.24$."),
            PQ(r"$\overrightarrow{OA} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$ and $\overrightarrow{OB} = \begin{pmatrix} 8 \\ -5 \end{pmatrix}$. Find (a) $\overrightarrow{AB}$, (b) $|\overrightarrow{AB}|$, (c) the position vector of $M$, the midpoint of $AB$.",
               r"(a) $\overrightarrow{AB} = \begin{pmatrix} 8 - 2 \\ -5 - 3 \end{pmatrix} = \begin{pmatrix} 6 \\ -8 \end{pmatrix}$. "
               r"(b) $|\overrightarrow{AB}| = \sqrt{36 + 64} = \sqrt{100} = 10$. "
               r"(c) $\overrightarrow{OM} = \overrightarrow{OA} + \tfrac{1}{2}\overrightarrow{AB} = \begin{pmatrix} 2 \\ 3 \end{pmatrix} + \begin{pmatrix} 3 \\ -4 \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \end{pmatrix}$."),
            PQ(r"Find the value of $k$ for which $\begin{pmatrix} k \\ 6 \end{pmatrix}$ is parallel to $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$.",
               r"The bottom number has been multiplied by $6 \div 3 = 2$. So the top must also be multiplied by 2: $k = 2 \times 2 = 4$."),
            PQ("A cyclist leaves Bamenda market and rides 4 km east and 3 km north, then 2 km east and 5 km north. (a) Write the total displacement as a column vector. (b) How far is the cyclist from the start in a straight line?",
               r"(a) $\begin{pmatrix} 4 \\ 3 \end{pmatrix} + \begin{pmatrix} 2 \\ 5 \end{pmatrix} = \begin{pmatrix} 6 \\ 8 \end{pmatrix}$ km. (b) $\sqrt{6^2 + 8^2} = \sqrt{100} = 10$ km."),
            SUM(r"A column vector $\begin{pmatrix} x \\ y \end{pmatrix}$ gives movement in the $x$- and $y$-directions.",
                r"Add, subtract and scale vectors component by component.",
                r"$\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$ (end minus start).",
                r"Magnitude $= \sqrt{x^2 + y^2}$; direction from $\tan\theta = y/x$ with a sketch.",
                r"Collinear: show $\overrightarrow{AC} = k\,\overrightarrow{AB}$ and state the common point."),
        ],
    ),
    # ------------------------------------------------------------------ Sine and cosine rules
    lesson(
        module="Trigonometry & Bearings",
        topic="Sine and cosine rules",
        title="The sine rule, the cosine rule and the area of a triangle",
        slug="sine-rule-cosine-rule-area-of-triangle",
        minutes=30,
        summary="Use the sine rule, the cosine rule and the formula ½ab sin C to find sides, angles and areas of triangles that do not have a right angle.",
        objectives=[
            "Label a triangle with sides a, b, c opposite angles A, B, C",
            "Use the sine rule to find a side or an angle",
            "Use the cosine rule to find a side or an angle",
            "Find the area of a triangle using ½ab sin C",
            "Choose the correct rule for the information given",
        ],
        key_concepts=["Sine rule", "Cosine rule", "Area of a triangle", "Included angle"],
        blocks=[
            H("Introduction"),
            T("SOH CAH TOA only works in right-angled triangles. But most triangles in real life, such as "
              "a triangular farm plot in Foumban or the triangle formed by three villages, have no right angle."),
            T("Two rules let us solve **any** triangle: the **sine rule** and the **cosine rule**. A third "
              "formula gives the area of any triangle when we know two sides and the angle between them."),
            KEY("Labelling the triangle", "Always label the triangle before you start.",
                cards=[["Angles", "Capital letters $A$, $B$, $C$ at the corners."],
                       ["Sides", "Small letters $a$, $b$, $c$. Side $a$ is **opposite** angle $A$, and so on."]]),
            IMG('f5-triangle-abc-labels.svg', 'Triangle ABC with corners labelled A, B and C. Side a is BC, opposite angle A, and is highlighted in blue together with angle A. Side b is AC, opposite angle B. Side c is AB, opposite angle C.',
                'Figure 1. Side a is opposite angle A, side b is opposite angle B and side c is opposite angle C.'),
            H("The sine rule"),
            D("In any triangle $ABC$, each side divided by the sine of its opposite angle gives the same value.",
              title="Sine rule", formula=r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}",
              note=r"To find an angle, use it upside down: $\dfrac{\sin A}{a} = \dfrac{\sin B}{b} = \dfrac{\sin C}{c}$."),
            T("Use the sine rule when you know a side and its opposite angle, plus one more side or angle."),
            EX("Worked example 1: sine rule for a side", intro=(
                r"In triangle $ABC$, $A = 40^\circ$, $B = 65^\circ$ and $a = 12$ cm. Find $b$."),
               steps=[
                   S("Write the part of the rule you need", math=r"\frac{b}{\sin B} = \frac{a}{\sin A}"),
                   S("Substitute", math=r"\frac{b}{\sin 65^\circ} = \frac{12}{\sin 40^\circ}"),
                   S("Multiply both sides by sin 65°", math=r"b = \frac{12 \sin 65^\circ}{\sin 40^\circ} = \frac{12 \times 0.9063}{0.6428}"),
                   S("Calculate", math=r"b \approx 16.9 \text{ cm}"),
               ]),
            TIP(r"Check that the answer makes sense: the longest side is opposite the largest angle. Here $B = 65^\circ$ is bigger than $A = 40^\circ$, so $b$ should be longer than $a$. It is."),
            H("The cosine rule"),
            D("Use the cosine rule when you know two sides and the angle **between** them (to find the third side), or all three sides (to find an angle).",
              title="Cosine rule", formula=r"a^2 = b^2 + c^2 - 2bc\cos A",
              note=r"Rearranged to find an angle: $\cos A = \dfrac{b^2 + c^2 - a^2}{2bc}$."),
            EX("Worked example 2: cosine rule for a side", intro=(
                r"In triangle $ABC$, $b = 8$ cm, $c = 11$ cm and $A = 50^\circ$. Find $a$."),
               steps=[
                   S("Write the rule", math=r"a^2 = b^2 + c^2 - 2bc\cos A"),
                   S("Substitute", math=r"a^2 = 8^2 + 11^2 - 2(8)(11)\cos 50^\circ"),
                   S("Work out each part", math=r"a^2 = 64 + 121 - 176 \times 0.6428 = 185 - 113.13"),
                   S("Simplify", math=r"a^2 = 71.87"),
                   S("Take the square root", math=r"a \approx 8.48 \text{ cm}"),
               ]),
            EX("Worked example 3: cosine rule for an angle", intro=(
                "A triangle has sides 7 cm, 8 cm and 9 cm. Find its largest angle."),
               steps=[
                   S("The largest angle is opposite the longest side", text="Call the 9 cm side $c$, so we want angle $C$, with $a = 7$ and $b = 8$."),
                   S("Write the rearranged rule", math=r"\cos C = \frac{a^2 + b^2 - c^2}{2ab}"),
                   S("Substitute", math=r"\cos C = \frac{49 + 64 - 81}{2 \times 7 \times 8} = \frac{32}{112}"),
                   S("Simplify", math=r"\cos C = 0.2857"),
                   S("Find the angle", math=r"C = \cos^{-1}(0.2857) \approx 73.4^\circ"),
               ]),
            MISTAKE("Subtracting before multiplying by cos A",
                    r"Work out $2bc\cos A$ as one number, then subtract it from $b^2 + c^2$. In example 2 that is $185 - 113.13$, not $(185 - 176) \times 0.6428$."),
            MISTAKE("Calculator in the wrong mode", "Make sure your calculator is in degrees (D or DEG on the screen), not radians."),
            QUIZ("You know two sides of a triangle and the angle between them. Which should you use to find the third side?",
                 ["The sine rule", "The cosine rule", "SOH CAH TOA", "Pythagoras' theorem"], 1,
                 r"Two sides and the included angle is the cosine rule situation: $a^2 = b^2 + c^2 - 2bc\cos A$.",
                 feedback=["The sine rule needs a side and its opposite angle. Here the angle is between the two known sides.", "",
                           "SOH CAH TOA only works in right-angled triangles.",
                           r"Pythagoras only works when the angle is $90^\circ$."]),
            H("Area of a triangle"),
            D("When you know two sides and the angle between them:", title="Area formula",
              formula=r"\text{Area} = \tfrac{1}{2}ab\sin C"),
            EX("Worked example 4: area of a farm plot", intro=(
                r"A farmer in Foumban has a triangular plot. Two sides are 30 m and 40 m, and the angle between them is $60^\circ$. "
                "One bag of fertiliser covers 100 m². How many bags does she need?"),
               steps=[
                   S("Write the formula", math=r"\text{Area} = \tfrac{1}{2}ab\sin C"),
                   S("Substitute", math=r"\text{Area} = \tfrac{1}{2} \times 30 \times 40 \times \sin 60^\circ = 600 \times 0.8660"),
                   S("Calculate", math=r"\text{Area} \approx 519.6 \text{ m}^2"),
                   S("Divide by 100 and round up", text=r"$519.6 \div 100 = 5.196$, so 5 bags are not enough. She needs **6 bags**."),
               ]),
            QUIZ(r"Find the area of a triangle with $a = 6$ cm, $b = 10$ cm and $C = 30^\circ$.",
                 [r"$30 \text{ cm}^2$", r"$15 \text{ cm}^2$", r"$60 \text{ cm}^2$", r"$26 \text{ cm}^2$"], 1,
                 r"$\tfrac{1}{2} \times 6 \times 10 \times \sin 30^\circ = 30 \times 0.5 = 15 \text{ cm}^2$.",
                 feedback=[r"You forgot to multiply by $\sin 30^\circ = 0.5$.", "",
                           r"You forgot the $\tfrac{1}{2}$ and the $\sin 30^\circ$.",
                           r"You used $\cos 30^\circ$ instead of $\sin 30^\circ$."]),
            H("Practice questions"),
            PQ(r"In triangle $PQR$, $p = 10$ cm, $q = 7$ cm and $P = 80^\circ$. Find angle $Q$.",
               r"Sine rule: $\dfrac{\sin Q}{7} = \dfrac{\sin 80^\circ}{10}$, so $\sin Q = \dfrac{7 \times 0.9848}{10} = 0.6894$. "
               r"$Q = \sin^{-1}(0.6894) \approx 43.6^\circ$. ($Q$ cannot be obtuse, because $q$ is shorter than $p$, so $Q$ must be smaller than $80^\circ$.)"),
            PQ(r"Two motorbike riders leave a road junction in Kumba along straight roads that make an angle of $120^\circ$. "
               "One rides 5 km and the other rides 6 km. How far apart are they?",
               r"Cosine rule: $d^2 = 5^2 + 6^2 - 2(5)(6)\cos 120^\circ = 25 + 36 - 60(-0.5) = 61 + 30 = 91$. "
               r"So $d = \sqrt{91} \approx 9.54$ km. Note: $\cos 120^\circ$ is negative, so the distance is larger than $\sqrt{61}$."),
            PQ("A triangle has sides 7 cm, 8 cm and 9 cm. Using the angle found in worked example 3, find its area.",
               r"Area $= \tfrac{1}{2} \times 7 \times 8 \times \sin 73.4^\circ = 28 \times 0.9583 \approx 26.8 \text{ cm}^2$."),
            SUM("Label the triangle: side $a$ is opposite angle $A$.",
                r"Sine rule $\dfrac{a}{\sin A} = \dfrac{b}{\sin B}$: use with a side and its opposite angle.",
                r"Cosine rule $a^2 = b^2 + c^2 - 2bc\cos A$: use with two sides and the included angle, or three sides.",
                r"Area $= \tfrac{1}{2}ab\sin C$, where $C$ is the angle between sides $a$ and $b$.",
                "Keep the calculator in degrees and check that the longest side faces the largest angle."),
        ],
    ),
    # ------------------------------------------------------------------ Bearings
    lesson(
        module="Trigonometry & Bearings",
        topic="Bearings",
        title="Three-figure bearings and navigation problems",
        slug="three-figure-bearings-navigation",
        minutes=25,
        summary="Read and write three-figure bearings, find back bearings, and solve journey problems with Pythagoras, trigonometry and the sine and cosine rules.",
        objectives=[
            "Give a direction as a three-figure bearing measured clockwise from north",
            "Find the back bearing (the bearing of A from B when you know the bearing of B from A)",
            "Draw a clear sketch for a journey with two stages",
            "Use Pythagoras, SOH CAH TOA and the sine and cosine rules to find distances and bearings",
        ],
        key_concepts=["Bearing", "Three-figure bearing", "Back bearing", "North line"],
        blocks=[
            H("Introduction"),
            T("Pilots at Douala airport, fishermen at Limbe and surveyors all need to describe directions exactly. "
              "Saying 'go north-east' is not precise enough. Instead they use **bearings**."),
            T("In this lesson you will learn to read and write bearings, and to solve problems about journeys "
              "with more than one stage."),
            D("A **bearing** is an angle measured **clockwise** from the **north** direction. It is always written "
              "with **three figures**.", title="Three-figure bearing",
              note=r"Examples: north is $000^\circ$, east is $090^\circ$, south is $180^\circ$, west is $270^\circ$. North-east is $045^\circ$ and an angle of $8^\circ$ is written $008^\circ$."),
            KEY("Three rules for every bearing", "Check these each time you draw or read a bearing.",
                cards=[["1. Start at north", "Draw a north line at the point you are measuring **from**."],
                       ["2. Turn clockwise", "Measure the angle clockwise from that north line."],
                       ["3. Three figures", r"Write $45^\circ$ as $045^\circ$ and $7^\circ$ as $007^\circ$."]]),
            T("The word 'from' tells you where to stand. 'The bearing of B **from** A' means: stand at A, face north, "
              "and turn clockwise until you face B."),
            H("Back bearings"),
            D("If the bearing of B from A is $\\theta$, the bearing of A from B points in exactly the opposite direction.",
              title="Back bearing",
              formula=r"\text{back bearing} = \theta + 180^\circ \ (\text{if } \theta < 180^\circ) \quad\text{or}\quad \theta - 180^\circ \ (\text{if } \theta \ge 180^\circ)"),
            T("Why does this work? The north lines at A and B are parallel. The line AB crosses them, so the two "
              "angles are co-interior angles (they add up to $180^\\circ$)."),
            EX("Worked example 1: back bearing", intro=(
                r"The bearing of Kribi from a fishing boat is $065^\circ$. Find the bearing of the boat from Kribi."),
               steps=[
                   S("The given bearing is less than 180°, so add 180°", math=r"065^\circ + 180^\circ"),
                   S("Answer", math=r"245^\circ"),
               ]),
            QUIZ("What is the three-figure bearing of south-west?",
                 [r"$045^\circ$", r"$135^\circ$", r"$225^\circ$", r"$315^\circ$"], 2,
                 r"South is $180^\circ$; south-west is halfway between south ($180^\circ$) and west ($270^\circ$), which is $225^\circ$.",
                 hint="Turn clockwise from north: east, then south, then halfway to west.",
                 feedback=[r"$045^\circ$ is north-east.", r"$135^\circ$ is south-east.", "", r"$315^\circ$ is north-west."]),
            H("Solving journey problems"),
            T("Always start with a sketch. Mark the starting point, draw a north arrow at **every** point where the "
              "direction changes, and label distances and angles. Then look for a right-angled triangle, or use the "
              "sine and cosine rules."),
            EX("Worked example 2: a right-angled journey", intro=(
                r"A lorry leaves a depot at D and travels 30 km due east (bearing $090^\circ$) to E. It then travels 40 km due south "
                r"(bearing $180^\circ$) to F. Find (a) the distance DF, (b) the bearing of F from D."),
               steps=[
                   S("Sketch", text="D is at the top left. E is 30 km to the right of D. F is 40 km directly below E. The angle at E is a right angle."),
                   S("Use Pythagoras for DF", math=r"DF = \sqrt{30^2 + 40^2} = \sqrt{2500} = 50 \text{ km}"),
                   S("Find angle EDF", math=r"\tan(\angle EDF) = \frac{40}{30}, \quad \angle EDF = 53.1^\circ"),
                   S("East is already 90° from north, so add", math=r"\text{bearing of F from D} = 90^\circ + 53.1^\circ = 143.1^\circ"),
               ], check=r"F \text{ is south-east of D, so the bearing lies between } 090^\circ \text{ and } 180^\circ"),
            IMG('f5-bearings-lorry.svg', 'Sketch with north arrows at D and E. D to E is 30 km due east, E to F is 40 km due south, with a right angle at E. DF is 50 km. At D, angle EDF is 53.1 degrees, and the bearing of F from D, measured clockwise from north, is 143.1 degrees.',
                'Figure 1. Worked example 2: the bearing of F from D is 090° + 53.1° = 143.1°.'),
            EX("Worked example 3: finding the angle between two stages", intro=(
                r"A boat sails 12 km from P to Q on a bearing of $050^\circ$. It then sails 9 km from Q to R on a bearing of $140^\circ$. "
                "Find the distance PR and the bearing of R from P."),
               steps=[
                   S("Find the bearing of P from Q (back bearing)", math=r"050^\circ + 180^\circ = 230^\circ"),
                   S("Angle PQR is the difference between the directions QP and QR", math=r"\angle PQR = 230^\circ - 140^\circ = 90^\circ"),
                   S("Right angle at Q, so use Pythagoras", math=r"PR = \sqrt{12^2 + 9^2} = \sqrt{225} = 15 \text{ km}"),
                   S("Find angle QPR", math=r"\tan(\angle QPR) = \frac{9}{12}, \quad \angle QPR = 36.9^\circ"),
                   S("Add to the first bearing", math=r"\text{bearing of R from P} = 050^\circ + 36.9^\circ = 086.9^\circ"),
               ]),
            IMG('f5-bearings-boat.svg', 'Sketch with north arrows at P and Q. P to Q is 12 km on a bearing of 050 degrees; Q to R is 9 km on a bearing of 140 degrees, measured clockwise from north at Q. The angle at Q is a right angle. PR is 15 km, angle QPR is 36.9 degrees, and the bearing of R from P is 086.9 degrees.',
                'Figure 2. Worked example 3: angle PQR is 90°, so PR = 15 km and the bearing of R from P is 086.9°.'),
            MISTAKE("Measuring from the wrong point", "The bearing of B from A uses the north line at **A**. Read the word 'from' carefully."),
            MISTAKE("Measuring anticlockwise or from east", "Bearings are always clockwise from north. An angle measured from east or anticlockwise is not a bearing."),
            MISTAKE("Writing two figures", r"Write $078^\circ$, not $78^\circ$. Examiners expect three figures."),
            QUIZ(r"The bearing of Q from P is $310^\circ$. What is the bearing of P from Q?",
                 [r"$130^\circ$", r"$490^\circ$", r"$050^\circ$", r"$230^\circ$"], 0,
                 r"$310^\circ$ is more than $180^\circ$, so subtract: $310^\circ - 180^\circ = 130^\circ$.",
                 feedback=["", r"A bearing cannot be more than $360^\circ$. Subtract $180^\circ$ when the bearing is $180^\circ$ or more.",
                           r"That is $360^\circ - 310^\circ$. The back bearing differs by $180^\circ$.",
                           r"You subtracted $80^\circ$. The difference must be $180^\circ$."]),
            H("Practice questions"),
            PQ(r"The bearing of a radio mast from Buea is $300^\circ$. What is the bearing of Buea from the mast?",
               r"$300^\circ \ge 180^\circ$, so subtract $180^\circ$: $300^\circ - 180^\circ = 120^\circ$."),
            PQ("Village Y is 5 km due north of village X. Village Z is 12 km due east of X. Find (a) the distance YZ, (b) the bearing of Z from Y.",
               r"(a) The angle at X is $90^\circ$, so $YZ = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$ km. "
               r"(b) At Y, the direction to X is due south ($180^\circ$). $\tan(\angle XYZ) = \dfrac{12}{5}$, so $\angle XYZ = 67.4^\circ$. "
               r"Z is east of the south line, so the bearing is $180^\circ - 67.4^\circ = 112.6^\circ$."),
            PQ(r"A hiker walks 8 km from A to B on a bearing of $060^\circ$, then 6 km from B to C on a bearing of $120^\circ$. "
               "(a) Show that angle ABC is 120°. (b) Find the distance AC. (c) Find the bearing of C from A.",
               r"(a) The bearing of A from B is $060^\circ + 180^\circ = 240^\circ$. So $\angle ABC = 240^\circ - 120^\circ = 120^\circ$. "
               r"(b) Cosine rule: $AC^2 = 8^2 + 6^2 - 2(8)(6)\cos 120^\circ = 100 + 48 = 148$, so $AC = \sqrt{148} \approx 12.2$ km. "
               r"(c) Sine rule: $\sin(\angle BAC) = \dfrac{6 \sin 120^\circ}{12.17} = 0.4271$, so $\angle BAC \approx 25.3^\circ$. "
               r"Bearing of C from A $= 060^\circ + 25.3^\circ = 085.3^\circ$."),
            IMG('f5-bearings-hiker.svg', 'Sketch with north arrows at A and B. A to B is 8 km on a bearing of 060 degrees; B to C is 6 km on a bearing of 120 degrees, each measured clockwise from north. A dashed line joins A to C, marked AC = ?.',
                "Figure 3. The hiker's journey: draw a north line at A and at B before finding angle ABC."),
            SUM("A bearing is measured clockwise from north and written with three figures.",
                "'The bearing of B from A' means stand at A and face north.",
                r"Back bearing: add $180^\circ$ if the bearing is under $180^\circ$, otherwise subtract $180^\circ$.",
                "Draw a sketch with a north line at every turning point.",
                "Use Pythagoras and SOH CAH TOA for right angles, and the sine and cosine rules otherwise."),
        ],
    ),
    # ------------------------------------------------------------------ Circle theorems
    lesson(
        module="Circle Theorems",
        topic="Circle theorems",
        title="Cyclic quadrilaterals and the alternate segment theorem",
        slug="cyclic-quadrilaterals-alternate-segment-theorem",
        minutes=30,
        summary="Use the angle properties of cyclic quadrilaterals and the alternate segment theorem to find unknown angles, giving a reason for every step.",
        objectives=[
            "Recognise a cyclic quadrilateral and use the fact that its opposite angles add up to 180°",
            "Use the exterior angle property of a cyclic quadrilateral",
            "State and use the alternate segment theorem",
            "Give a correct reason for each step when finding angles",
        ],
        key_concepts=["Cyclic quadrilateral", "Opposite angles", "Exterior angle of a cyclic quadrilateral",
                      "Tangent", "Chord", "Alternate segment theorem"],
        blocks=[
            H("Introduction"),
            T("Circles are everywhere: a bicycle wheel, the top of a water tank, a round market stall roof in Bafoussam. "
              "Circle theorems are facts about the angles we get when we draw chords and tangents in a circle."),
            T("In GCE answers you must give a **reason** for every angle you find. This lesson describes each diagram in "
              "words. Draw it yourself on paper as you read: this is the best way to learn the theorems."),
            KEY("Facts you will use", "These earlier results are often needed alongside today's theorems.",
                cards=[["Angle at the centre", "The angle at the centre is twice the angle at the circumference standing on the same arc."],
                       ["Same segment", "Angles in the same segment (standing on the same chord, same side) are equal."],
                       ["Tangent and radius", r"A tangent meets the radius at the point of contact at $90^\circ$."]]),
            H("Cyclic quadrilaterals"),
            D("A **cyclic quadrilateral** is a four-sided shape whose four corners all lie on the same circle.",
              title="Cyclic quadrilateral"),
            D("The **opposite angles** of a cyclic quadrilateral add up to $180^\\circ$.",
              title="Theorem 1: opposite angles", formula=r"\angle A + \angle C = 180^\circ, \qquad \angle B + \angle D = 180^\circ",
              note="Diagram in words: draw a circle and mark four points A, B, C, D in order around it. Join them to make the quadrilateral ABCD. Angle A and angle C are opposite each other; so are angle B and angle D."),
            IMG('f5-cyclic-quadrilateral.svg', 'Circle with four points A, B, C and D on it, joined to make quadrilateral ABCD. Angles A and C are marked in blue and angles B and D in green. Text: angle A plus angle C = 180 degrees, angle B plus angle D = 180 degrees.',
                'Figure 1. Opposite angles of a cyclic quadrilateral add up to 180°.'),
            D("If one side of a cyclic quadrilateral is extended, the **exterior angle** equals the **interior opposite angle**.",
              title="Theorem 2: exterior angle",
              note="Diagram in words: in cyclic quadrilateral ABCD, extend side AB beyond B to a point E. The angle CBE (outside the shape) is equal to angle ADC (the angle at the opposite corner D)."),
            IMG('f5-cyclic-exterior-angle.svg', 'Cyclic quadrilateral ABCD in a circle, with side AB extended beyond B to a point E as a dashed line. The exterior angle CBE and the interior opposite angle ADC are both marked x.',
                'Figure 2. The exterior angle CBE equals the interior opposite angle ADC.'),
            EX("Worked example 1: opposite angles", intro=(
                r"ABCD is a cyclic quadrilateral with $\angle A = 75^\circ$ and $\angle B = 110^\circ$. Find $\angle C$ and $\angle D$."),
               steps=[
                   S("A and C are opposite angles", math=r"\angle C = 180^\circ - 75^\circ = 105^\circ", text="Reason: opposite angles of a cyclic quadrilateral."),
                   S("B and D are opposite angles", math=r"\angle D = 180^\circ - 110^\circ = 70^\circ", text="Reason: opposite angles of a cyclic quadrilateral."),
               ], check=r"75^\circ + 110^\circ + 105^\circ + 70^\circ = 360^\circ"),
            EX("Worked example 2: exterior angle", intro=(
                r"ABCD is a cyclic quadrilateral. Side AB is extended to E so that $\angle CBE = 80^\circ$. Find $\angle ADC$ and $\angle ABC$."),
               steps=[
                   S("Use the exterior angle theorem", math=r"\angle ADC = \angle CBE = 80^\circ", text="Reason: exterior angle of a cyclic quadrilateral equals the interior opposite angle."),
                   S("ABE is a straight line", math=r"\angle ABC = 180^\circ - 80^\circ = 100^\circ", text="Reason: angles on a straight line add up to 180°."),
               ], check=r"\angle ABC + \angle ADC = 100^\circ + 80^\circ = 180^\circ"),
            QUIZ(r"In cyclic quadrilateral PQRS, $\angle P = 3x$ and $\angle R = x + 20^\circ$. What is $\angle P$?",
                 [r"$40^\circ$", r"$120^\circ$", r"$60^\circ$", r"$135^\circ$"], 1,
                 r"$3x + x + 20 = 180$, so $4x = 160$ and $x = 40$. Then $\angle P = 3 \times 40 = 120^\circ$.",
                 hint="P and R are opposite angles, so they add up to 180°.",
                 feedback=[r"$40^\circ$ is the value of $x$, not of $\angle P$.", "",
                           r"$60^\circ$ is $\angle R$, the other angle.",
                           r"You may have set $3x + x + 20 = 360^\circ$. Opposite angles add up to $180^\circ$."]),
            H("The alternate segment theorem"),
            D("The angle between a **tangent** and a **chord** at the point of contact is equal to the angle in the "
              "**alternate segment** (the angle subtended by the chord at the circumference on the other side).",
              title="Theorem 3: alternate segment theorem",
              note="Diagram in words: a circle with a point A on it. A straight line TS touches the circle only at A (the tangent). From A draw a chord AB. Mark a point C on the circle on the opposite side of AB from T, and join CA and CB. Then angle TAB (between the tangent and the chord) equals angle ACB."),
            IMG('f5-alternate-segment.svg', 'Circle with a tangent line TS touching it at A at the bottom. Chord AB goes up to the left; point C is on the circle on the other side of AB from T, and triangle ABC is drawn. Angle TAB, between the tangent and the chord, and angle ACB are both marked x.',
                'Figure 3. Alternate segment theorem: angle TAB = angle ACB.'),
            TIP("To find the 'alternate' angle: the angle between the tangent and the chord sits on one side of the chord. The equal angle is in the triangle on the **other** side of that chord, at the point opposite the chord."),
            EX("Worked example 3: alternate segment theorem", intro=(
                r"A tangent TS touches a circle at A. Chords AB and AC are drawn and BC is joined. $\angle TAB = 58^\circ$, where T is on the "
                r"opposite side of AB from C. Also $\angle BAC = 70^\circ$. Find $\angle ACB$ and $\angle ABC$."),
               steps=[
                   S("Angle between tangent TA and chord AB", math=r"\angle ACB = \angle TAB = 58^\circ", text="Reason: alternate segment theorem."),
                   S("Use the angle sum of triangle ABC", math=r"\angle ABC = 180^\circ - 70^\circ - 58^\circ = 52^\circ", text="Reason: angles in a triangle add up to 180°."),
               ]),
            IMG('f5-alternate-segment-example.svg', 'Circle with tangent TS touching at A and triangle ABC inside. Given angles in blue: angle TAB = 58 degrees and angle BAC = 70 degrees. Found angles in green: angle ACB = 58 degrees and angle ABC = 52 degrees.',
                'Figure 4. Worked example 3: angle ACB = 58° (alternate segment) and angle ABC = 52°.'),
            MISTAKE("Using the wrong chord", "The equal angle must stand on the **same chord** that makes the angle with the tangent. If the tangent angle is with chord AB, look for the angle that AB makes at C, which is angle ACB."),
            MISTAKE("Calling a quadrilateral cyclic without checking", "Opposite angles add to 180° only when all four corners are on the circle. A quadrilateral with a corner at the centre O is not cyclic."),
            MISTAKE("Giving no reasons", "Write a short reason after each step, for example 'opposite angles of a cyclic quadrilateral' or 'alternate segment theorem'. Answers without reasons can lose marks."),
            QUIZ(r"A tangent at A makes an angle of $35^\circ$ with chord AB. C is a point on the major arc. What is $\angle ACB$?",
                 [r"$55^\circ$", r"$145^\circ$", r"$35^\circ$", r"$70^\circ$"], 2,
                 r"By the alternate segment theorem, $\angle ACB$ equals the tangent-chord angle, $35^\circ$.",
                 feedback=[r"That is $90^\circ - 35^\circ$. The tangent is perpendicular to the radius, not to the chord.",
                           r"That is $180^\circ - 35^\circ$. The angles are equal, not supplementary.", "",
                           r"Doubling gives the angle at the centre, not the angle at the circumference."]),
            H("Practice questions"),
            PQ(r"ABCD is a cyclic quadrilateral with $\angle A = 2x$, $\angle C = x + 30^\circ$, $\angle B = y$ and $\angle D = y + 40^\circ$. Find $x$ and $y$.",
               r"Opposite angles: $2x + x + 30 = 180$, so $3x = 150$ and $x = 50^\circ$. "
               r"Also $y + y + 40 = 180$, so $2y = 140$ and $y = 70^\circ$. "
               r"Check: $\angle A = 100^\circ$, $\angle C = 80^\circ$, $\angle B = 70^\circ$, $\angle D = 110^\circ$; the total is $360^\circ$."),
            PQ(r"Triangle ABC is drawn inside a circle. A tangent at A makes an angle of $62^\circ$ with AB (on the side away from C) and "
               r"an angle of $48^\circ$ with AC (on the side away from B). Find the three angles of triangle ABC.",
               r"Alternate segment theorem: $\angle ACB = 62^\circ$ (it stands on chord AB) and $\angle ABC = 48^\circ$ (it stands on chord AC). "
               r"The angles on the straight tangent line give $\angle BAC = 180^\circ - 62^\circ - 48^\circ = 70^\circ$. "
               r"Check: $62^\circ + 48^\circ + 70^\circ = 180^\circ$."),
            IMG('f5-alternate-segment-practice.svg', 'Circle with a tangent touching at A and triangle ABC inside, B on the left and C on the right. The tangent makes 62 degrees with AB on the left and 48 degrees with AC on the right. The three angles of triangle ABC are marked with question marks.',
                'Figure 5. Practice question 2: the tangent at A makes 62° with AB and 48° with AC.'),
            PQ(r"O is the centre of a circle. A, B, C and D lie on the circle in that order, with B on the minor arc AC. $\angle AOC = 140^\circ$. Find $\angle ADC$ and $\angle ABC$.",
               r"$\angle ADC = \tfrac{1}{2} \times 140^\circ = 70^\circ$ (angle at the centre is twice the angle at the circumference). "
               r"ABCD is cyclic, so $\angle ABC = 180^\circ - 70^\circ = 110^\circ$ (opposite angles of a cyclic quadrilateral)."),
            IMG('f5-centre-angle-cyclic.svg', 'Circle with centre O and points A, B, C, D on it, with B at the bottom on the minor arc AC and D at the top. Radii OA and OC make an angle of 140 degrees at O. Angles ADC and ABC are marked with question marks.',
                'Figure 6. Practice question 3: angle AOC = 140°, with B on the minor arc AC.'),
            PQ(r"A quadrilateral has angles $88^\circ$, $97^\circ$, $92^\circ$ and $83^\circ$ in order. Can it be a cyclic quadrilateral?",
               r"Opposite pairs: $88^\circ + 92^\circ = 180^\circ$ and $97^\circ + 83^\circ = 180^\circ$. Both pairs add up to $180^\circ$, so yes, its corners can lie on one circle."),
            SUM(r"A cyclic quadrilateral has all four corners on a circle.",
                r"Its opposite angles add up to $180^\circ$.",
                "Its exterior angle equals the interior opposite angle.",
                "Alternate segment theorem: the tangent-chord angle equals the angle in the alternate segment on that chord.",
                "Draw your own diagram and give a reason for every angle."),
        ],
    ),
    # ------------------------------------------------------------------ Grouped data
    lesson(
        module="Statistics & Probability",
        topic="Grouped data",
        title="Grouped data: histograms, cumulative frequency, median and quartiles",
        slug="grouped-data-histograms-cumulative-frequency",
        minutes=30,
        summary="Work with grouped frequency tables: estimate the mean, find the modal class, draw histograms with frequency density, and use a cumulative frequency curve to estimate the median and quartiles.",
        objectives=[
            "Find the modal class and estimate the mean of grouped data using class mid-points",
            "Calculate frequency density and draw a histogram, including unequal class widths",
            "Draw a cumulative frequency curve (ogive) using upper class boundaries",
            "Estimate the median, quartiles and interquartile range from the ogive",
        ],
        key_concepts=["Grouped frequency table", "Class mid-point", "Modal class", "Histogram", "Frequency density",
                      "Cumulative frequency", "Ogive", "Median", "Quartiles", "Interquartile range"],
        blocks=[
            H("Introduction"),
            T("When a school in Bamenda records how long 40 students take to travel to school, it gets 40 different "
              "numbers. A long list is hard to read, so we put the data into **groups** (classes) and count how many "
              "fall in each group."),
            T("In this lesson we use one set of data all the way through. Each student's journey time $t$, in minutes, was put into a class:"),
            KEY("Journey times of 40 students", "Class (minutes) and frequency (number of students).",
                cards=[[r"$0 < t \le 10$", "4"], [r"$10 < t \le 20$", "10"], [r"$20 < t \le 30$", "14"],
                       [r"$30 < t \le 40$", "8"], [r"$40 < t \le 50$", "4"]],
                note="Total frequency: 4 + 10 + 14 + 8 + 4 = 40."),
            H("Modal class and estimated mean"),
            D("The **modal class** is the class with the highest frequency. The **mid-point** of a class is halfway "
              "between its lower and upper boundaries. We use mid-points because we do not know the exact values inside each class.",
              title="Modal class and mid-point",
              formula=r"\text{Estimated mean} = \frac{\sum f x}{\sum f}", note="Here $x$ is the class mid-point and $f$ is the frequency."),
            EX("Worked example 1: estimated mean", intro="Estimate the mean journey time for the 40 students and state the modal class.",
               steps=[
                   S("Find the mid-points", text="The mid-points are 5, 15, 25, 35 and 45."),
                   S("Multiply each mid-point by its frequency", math=r"5(4) = 20,\ 15(10) = 150,\ 25(14) = 350,\ 35(8) = 280,\ 45(4) = 180"),
                   S("Add the products", math=r"\sum fx = 20 + 150 + 350 + 280 + 180 = 980"),
                   S("Divide by the total frequency", math=r"\text{mean} \approx \frac{980}{40} = 24.5 \text{ minutes}"),
                   S("Modal class", text="The highest frequency is 14, so the modal class is $20 < t \\le 30$."),
               ]),
            H("Histograms and frequency density"),
            D("In a histogram the **area** of each bar shows the frequency. When classes have different widths, the "
              "height of each bar is the **frequency density**.", title="Frequency density",
              formula=r"\text{frequency density} = \frac{\text{frequency}}{\text{class width}}",
              note="If all classes have the same width you may plot frequency on the vertical axis. There are no gaps between the bars."),
            EX("Worked example 2: unequal class widths", intro=(
                "The daily earnings of 45 moto-taxi drivers, in thousands of FCFA, are grouped as follows: 0–2: 6 drivers, 2–3: 9 drivers, "
                "3–4: 12 drivers, 4–6: 10 drivers, 6–10: 8 drivers. Find the frequency density of each class for a histogram."),
               steps=[
                   S("Find each class width", text="The widths are 2, 1, 1, 2 and 4."),
                   S("Divide each frequency by its width", math=r"\tfrac{6}{2} = 3,\quad \tfrac{9}{1} = 9,\quad \tfrac{12}{1} = 12,\quad \tfrac{10}{2} = 5,\quad \tfrac{8}{4} = 2"),
                   S("Describe the histogram", text="Draw earnings on the horizontal axis and frequency density on the vertical axis. The bar for 0–2 is 2 units wide and 3 units tall; the bar for 6–10 is 4 units wide but only 2 units tall."),
               ]),
            IMG('f5-histogram-earnings.svg', 'Histogram of daily earnings in thousands of FCFA, with no gaps between bars. Bar 0 to 2 has frequency density 3, bar 2 to 3 has 9, bar 3 to 4 has 12, bar 4 to 6 has 5 and bar 6 to 10 has 2. The frequencies 6, 9, 12, 10 and 8 are written inside the bars.',
                'Figure 1. Worked example 2: bar height is frequency density, so the wide 6–10 class is only 2 units tall.'),
            QUIZ("A class $10 < x \\le 25$ has a frequency of 30. What is its frequency density?",
                 ["$2$", "$3$", "$1.2$", "$450$"], 0,
                 r"The class width is $25 - 10 = 15$, so the frequency density is $30 \div 15 = 2$.",
                 feedback=["", "You divided by 10, the lower boundary. Divide by the class width, 15.",
                           "You divided by the upper boundary, 25. Divide by the width.",
                           "You multiplied by the width instead of dividing."]),
            H("Cumulative frequency, median and quartiles"),
            D("The **cumulative frequency** is the running total of the frequencies. A **cumulative frequency curve** "
              "(ogive) plots each cumulative frequency against the **upper class boundary**.", title="Cumulative frequency"),
            T("For the journey times the cumulative frequencies are 4, 14, 28, 36 and 40. So we plot the points "
              "(10, 4), (20, 14), (30, 28), (40, 36) and (50, 40). We also plot (0, 0), because no student took 0 minutes or less."),
            T("Join the points with a smooth curve. The curve rises slowly, then steeply in the middle class, then slowly again, "
              "making a stretched S-shape."),
            D("With $n$ values, read across from these cumulative frequencies to the curve, then down to the horizontal axis.",
              title="Median and quartiles from an ogive",
              formula=r"Q_1 \text{ at } \tfrac{1}{4}n, \qquad \text{median at } \tfrac{1}{2}n, \qquad Q_3 \text{ at } \tfrac{3}{4}n",
              note=r"The **interquartile range** is $Q_3 - Q_1$. It measures the spread of the middle half of the data."),
            EX("Worked example 3: median and quartiles", intro="Estimate the median, the quartiles and the interquartile range of the journey times.",
               steps=[
                   S("Find the positions", math=r"\tfrac{1}{4}(40) = 10,\quad \tfrac{1}{2}(40) = 20,\quad \tfrac{3}{4}(40) = 30"),
                   S("Median: the 20th value lies in 20–30 (cumulative 14 to 28)", math=r"20 + \frac{20 - 14}{14} \times 10 \approx 24.3 \text{ min}",
                     text="Reading from a straight line between (20, 14) and (30, 28) gives this value. A smooth curve gives a value close to it."),
                   S("Lower quartile: the 10th value lies in 10–20 (cumulative 4 to 14)", math=r"Q_1 = 10 + \frac{10 - 4}{10} \times 10 = 16 \text{ min}"),
                   S("Upper quartile: the 30th value lies in 30–40 (cumulative 28 to 36)", math=r"Q_3 = 30 + \frac{30 - 28}{8} \times 10 = 32.5 \text{ min}"),
                   S("Interquartile range", math=r"Q_3 - Q_1 = 32.5 - 16 = 16.5 \text{ min}"),
               ]),
            IMG('f5-ogive-journey-times.svg', 'Cumulative frequency curve of journey times, a stretched S-shape through the points (0, 0), (10, 4), (20, 14), (30, 28), (40, 36) and (50, 40). Dashed lines read across from cumulative frequencies 10, 20 and 30 to the curve and down to the time axis at 16, 24.3 and 32.5 minutes.',
                'Figure 2. Reading the ogive: Q₁ = 16 min, median ≈ 24.3 min and Q₃ = 32.5 min.'),
            MISTAKE("Plotting at mid-points", "Cumulative frequency is plotted at the **upper** class boundary, because by the end of the class all those values have been counted."),
            MISTAKE("Using frequency as bar height with unequal widths", "With unequal class widths, the bar height must be frequency density, or wide classes will look far too important."),
            MISTAKE("Dividing by the number of classes", r"The mean is $\sum fx \div \sum f$ (the total frequency), not $\sum fx$ divided by the number of classes."),
            H("Practice questions"),
            PQ("The marks of 40 students are: 0–20: 3, 20–40: 7, 40–60: 15, 60–80: 10, 80–100: 5. (a) State the modal class. (b) Estimate the mean mark.",
               r"(a) The modal class is 40–60 (frequency 15). (b) Mid-points: 10, 30, 50, 70, 90. "
               r"$\sum fx = 30 + 210 + 750 + 700 + 450 = 2140$. Mean $\approx 2140 \div 40 = 53.5$ marks."),
            PQ("For the marks in the previous question, (a) write down the cumulative frequencies, (b) estimate the median and the interquartile range.",
               r"(a) 3, 10, 25, 35, 40, plotted at 20, 40, 60, 80, 100. "
               r"(b) Median at the 20th value: $40 + \frac{20 - 10}{15} \times 20 \approx 53.3$. "
               r"$Q_1$ at the 10th value: exactly 40. $Q_3$ at the 30th value: $60 + \frac{30 - 25}{10} \times 20 = 70$. "
               r"Interquartile range $= 70 - 40 = 30$ marks."),
            PQ("In a histogram, the bar for the class 20–30 has a frequency density of 1.6. (a) Find its frequency. (b) Another class, 30–35, has a frequency of 12. Find the height of its bar.",
               r"(a) Frequency $=$ frequency density $\times$ width $= 1.6 \times 10 = 16$. (b) Frequency density $= 12 \div 5 = 2.4$."),
            SUM("Estimated mean $= \\sum fx \\div \\sum f$, using class mid-points.",
                "The modal class has the highest frequency.",
                "Histogram bar height = frequency density = frequency ÷ class width.",
                "Plot cumulative frequency at the upper class boundary and join with a smooth curve.",
                r"Read $Q_1$, median and $Q_3$ at $\tfrac{1}{4}n$, $\tfrac{1}{2}n$ and $\tfrac{3}{4}n$; IQR $= Q_3 - Q_1$."),
        ],
    ),
    # ------------------------------------------------------------------ Probability
    lesson(
        module="Statistics & Probability",
        topic="Probability",
        title="Theoretical probability and tree diagrams",
        slug="theoretical-probability-tree-diagrams",
        minutes=30,
        summary="Calculate theoretical probabilities, use the AND and OR rules, and draw tree diagrams for two events, with and without replacement.",
        objectives=[
            "Calculate the theoretical probability of an event with equally likely outcomes",
            "Use P(not A) = 1 − P(A)",
            "Add probabilities of mutually exclusive events and multiply probabilities of independent events",
            "Draw and use tree diagrams, with and without replacement",
        ],
        key_concepts=["Probability", "Outcome", "Event", "Complementary events", "Mutually exclusive events",
                      "Independent events", "Tree diagram", "Without replacement"],
        blocks=[
            H("Introduction"),
            T("Will the bus from Yaoundé to Douala arrive on time? Will a mango picked from a basket be ripe? "
              "**Probability** measures how likely something is, on a scale from 0 (impossible) to 1 (certain)."),
            T("In this lesson you will calculate probabilities from equally likely outcomes, and use **tree diagrams** "
              "when there are two events, one after the other."),
            D("When all outcomes are equally likely, the **theoretical probability** of an event A is", title="Theoretical probability",
              formula=r"P(A) = \frac{\text{number of outcomes in } A}{\text{total number of possible outcomes}}",
              note=r"Every probability lies between 0 and 1: $0 \le P(A) \le 1$."),
            D("The event 'A does not happen' is the **complement** of A.", title="Complementary events",
              formula=r"P(\text{not } A) = 1 - P(A)"),
            EX("Worked example 1: simple probability", intro=(
                "A bag contains 5 red, 3 blue and 2 green balls. One ball is taken at random. Find (a) P(blue), (b) P(not green)."),
               steps=[
                   S("Count the total", math=r"5 + 3 + 2 = 10 \text{ balls}"),
                   S("(a) 3 of the 10 balls are blue", math=r"P(\text{blue}) = \frac{3}{10}"),
                   S("(b) Use the complement", math=r"P(\text{not green}) = 1 - \frac{2}{10} = \frac{8}{10} = \frac{4}{5}"),
               ]),
            H("The OR rule and the AND rule"),
            KEY("Two rules", "Decide which rule fits before you calculate.",
                cards=[["OR: add", r"If A and B are **mutually exclusive** (cannot happen together), $P(A \text{ or } B) = P(A) + P(B)$."],
                       ["AND: multiply", r"If A and B are **independent** (one does not affect the other), $P(A \text{ and } B) = P(A) \times P(B)$."]]),
            QUIZ("Two fair coins are tossed. What is the probability of getting two heads?",
                 [r"$\tfrac{1}{2}$", r"$\tfrac{1}{4}$", r"$\tfrac{1}{3}$", r"$1$"], 1,
                 r"The coins are independent: $\tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}$. The four outcomes are HH, HT, TH, TT.",
                 feedback=["That is the probability for one coin. For two heads you need head AND head, so multiply.", "",
                           "There are four equally likely outcomes, not three: HT and TH are different.",
                           r"You added $\tfrac{1}{2} + \tfrac{1}{2}$. Use 'and': multiply."]),
            H("Tree diagrams"),
            T("A tree diagram shows two (or more) events one after the other. Each set of branches starts from one point, "
              "and the probabilities on those branches add up to 1."),
            KEY("How to use a tree", "Two rules for reading a tree diagram.",
                cards=[["Along a path", "Multiply the probabilities along the branches."],
                       ["Several paths", "Add the results of all the paths that give the event you want."]]),
            EX("Worked example 2: independent events", intro=(
                "Amina travels by bus and Bih travels by taxi, independently. The probability that the bus is late is 0.3. "
                "The probability that the taxi is late is 0.1. Find the probability that (a) both are late, (b) exactly one is late, (c) at least one is late."),
               steps=[
                   S("Describe the tree", text="The first pair of branches is for the bus: late 0.3, on time 0.7. From the end of each, a second pair is for the taxi: late 0.1, on time 0.9. This gives four paths."),
                   S("(a) Both late: multiply along one path", math=r"0.3 \times 0.1 = 0.03"),
                   S("(b) Exactly one late: add two paths", math=r"0.3 \times 0.9 + 0.7 \times 0.1 = 0.27 + 0.07 = 0.34"),
                   S("(c) At least one late: use the complement of 'neither late'", math=r"1 - 0.7 \times 0.9 = 1 - 0.63 = 0.37"),
               ], check=r"0.03 + 0.34 + 0.63 = 1"),
            IMG('f5-tree-bus-taxi.svg', 'Tree diagram. First branches for the bus: late 0.3, on time 0.7. From each, branches for the taxi: late 0.1, on time 0.9. The four path probabilities are 0.03, 0.27, 0.07 and 0.63.',
                'Figure 1. Worked example 2: multiply along each path; the four results add up to 1.'),
            EX("Worked example 3: without replacement", intro=(
                "A trader in Mokolo market has a basket of 10 mangoes: 4 are ripe and 6 are not ripe. A customer picks two mangoes at random, one after the other, "
                "without putting the first back. Find the probability that (a) both are ripe, (b) one is ripe and one is not."),
               steps=[
                   S("First pick", text="P(ripe) $= \\tfrac{4}{10}$ and P(not ripe) $= \\tfrac{6}{10}$."),
                   S("Second pick: only 9 mangoes are left", text="After a ripe one: P(ripe) $= \\tfrac{3}{9}$, P(not ripe) $= \\tfrac{6}{9}$. After an unripe one: P(ripe) $= \\tfrac{4}{9}$, P(not ripe) $= \\tfrac{5}{9}$."),
                   S("(a) Both ripe", math=r"\frac{4}{10} \times \frac{3}{9} = \frac{12}{90} = \frac{2}{15}"),
                   S("(b) Ripe then not ripe, OR not ripe then ripe", math=r"\frac{4}{10} \times \frac{6}{9} + \frac{6}{10} \times \frac{4}{9} = \frac{24}{90} + \frac{24}{90} = \frac{48}{90} = \frac{8}{15}"),
               ], check=r"P(\text{both not ripe}) = \tfrac{6}{10} \times \tfrac{5}{9} = \tfrac{1}{3}, \text{ and } \tfrac{2}{15} + \tfrac{8}{15} + \tfrac{5}{15} = 1"),
            IMG('f5-tree-mangoes.svg', 'Tree diagram for two mangoes picked without replacement. First pick: ripe 4/10, not ripe 6/10. After a ripe mango: ripe 3/9, not ripe 6/9. After an unripe mango: ripe 4/9, not ripe 5/9. Path probabilities: 12/90, 24/90, 24/90 and 30/90.',
                'Figure 2. Worked example 3: the second-pick probabilities change because only 9 mangoes are left.'),
            MISTAKE("Forgetting that the total changes", "Without replacement, the second pick has one item fewer, so the denominator goes down by 1, and the count of the chosen type may change too."),
            MISTAKE("Adding along a path", "Along one path you **multiply**. You only **add** when you combine different paths."),
            MISTAKE("Counting only one order", "'One ripe and one not ripe' can happen in two orders. Include both paths."),
            QUIZ("A bag has 3 red and 2 blue counters. Two are taken without replacement. What is P(both red)?",
                 [r"$\tfrac{9}{25}$", r"$\tfrac{3}{10}$", r"$\tfrac{6}{25}$", r"$\tfrac{1}{2}$"], 1,
                 r"$\tfrac{3}{5} \times \tfrac{2}{4} = \tfrac{6}{20} = \tfrac{3}{10}$.",
                 feedback=[r"$\tfrac{3}{5} \times \tfrac{3}{5}$ is the answer **with** replacement. After one red is taken, 2 red remain out of 4.", "",
                           "The second denominator should be 4, not 5.",
                           "You may have added fractions. Multiply along the path."]),
            H("Practice questions"),
            PQ("A fair six-sided die is thrown once. Find (a) P(a prime number), (b) P(a number greater than 4).",
               r"(a) The primes are 2, 3 and 5, so P $= \tfrac{3}{6} = \tfrac{1}{2}$. (b) The numbers 5 and 6, so P $= \tfrac{2}{6} = \tfrac{1}{3}$."),
            PQ("Two fair dice are thrown. What is the probability that the total is 7?",
               r"There are $6 \times 6 = 36$ equally likely outcomes. A total of 7 comes from (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1): 6 outcomes. P $= \tfrac{6}{36} = \tfrac{1}{6}$."),
            PQ("A box contains 12 pens, of which 3 are faulty. Two pens are chosen at random without replacement. Find (a) P(both faulty), (b) P(at least one faulty).",
               r"(a) $\tfrac{3}{12} \times \tfrac{2}{11} = \tfrac{6}{132} = \tfrac{1}{22}$. "
               r"(b) P(neither faulty) $= \tfrac{9}{12} \times \tfrac{8}{11} = \tfrac{72}{132} = \tfrac{6}{11}$, so P(at least one faulty) $= 1 - \tfrac{6}{11} = \tfrac{5}{11}$."),
            PQ("The probability that Ngum passes Mathematics is 0.8 and the probability that she passes English is 0.6. The events are independent. Draw a tree diagram and find the probability that she passes exactly one of the two subjects.",
               r"Branches: Maths pass 0.8, fail 0.2; then English pass 0.6, fail 0.4. "
               r"P(exactly one) $= 0.8 \times 0.4 + 0.2 \times 0.6 = 0.32 + 0.12 = 0.44$."),
            SUM(r"$P(A) = \dfrac{\text{favourable outcomes}}{\text{total outcomes}}$ when outcomes are equally likely.",
                r"$P(\text{not } A) = 1 - P(A)$; it is often the quickest way to find 'at least one'.",
                "OR for mutually exclusive events: add. AND for independent events: multiply.",
                "On a tree diagram, multiply along a path and add different paths.",
                "Without replacement, the probabilities on the second set of branches change."),
        ],
    ),
]
