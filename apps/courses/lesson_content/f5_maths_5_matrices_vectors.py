"""Form 5 General Mathematics (O Level 570): Matrices & Vectors.

Six focused lessons: three on 2×2 matrices and three on 2D vectors.
Draft content for review in the studio."""
from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

MOD = "Matrices & Vectors"
T_MAT = "2×2 matrices"
T_VEC = "2D vectors"

LESSONS = [
    # ------------------------------------------------------------------ 1. Matrix operations
    lesson(
        module=MOD,
        topic=T_MAT,
        title="Matrix operations: adding, scaling and multiplying",
        slug="matrix-operations-2x2",
        minutes=22,
        summary="Find the order of a matrix, add and subtract matrices, multiply by a number, multiply two 2×2 matrices and a 2×2 by a 2×1 matrix, and use the identity matrix.",
        objectives=[
            "State the order of a matrix and add or subtract matrices of the same order",
            "Multiply a matrix by a number",
            "Multiply two 2×2 matrices, and a 2×2 matrix by a 2×1 matrix, row by column",
            "Explain why AB is usually not equal to BA and use the identity matrix",
        ],
        key_concepts=["Matrix", "Order of a matrix", "Scalar multiple", "Matrix multiplication",
                      "Identity matrix"],
        blocks=[
            H("Introduction"),
            T("A **matrix** is a rectangular array of numbers written inside brackets. It is a neat way to "
              "store several numbers at once and work with them together."),
            T("For example, Mama Ngono buys tomatoes and onions at Bafoussam market on Monday and Tuesday. "
              "The kilograms she buys each day fit into one matrix, and the prices fit into another. "
              "Multiplying the two matrices gives what she spends each day. In this lesson you learn the "
              "basic operations on matrices."),
            D("A matrix with $m$ rows and $n$ columns has **order** $m \\times n$ (rows first, then columns). "
              "Each number in it is called an **entry** (or element).",
              formula=r"A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \text{ has order } 2 \times 2, \qquad \begin{pmatrix} 5 \\ -1 \end{pmatrix} \text{ has order } 2 \times 1"),
            QUIZ(r"What is the order of $\begin{pmatrix} 1 & 0 & 7 \\ 4 & 2 & 3 \end{pmatrix}$?",
                 ["$2 \\times 3$", "$3 \\times 2$", "$6$", "$2 \\times 2$"], 0,
                 "There are 2 rows and 3 columns. Rows come first, so the order is $2 \\times 3$.",
                 hint="Count the rows (across) first, then the columns (down).",
                 feedback=["", "You wrote columns first. The order is always rows × columns.",
                           "6 is the number of entries, not the order.",
                           "Count again: there are three columns, not two."]),
            H("Adding, subtracting and multiplying by a number"),
            T("You can only add or subtract two matrices of the **same order**. Add or subtract the entries "
              "in the same positions. To multiply a matrix by a number $k$ (a **scalar**), multiply **every** entry by $k$."),
            EX("Worked example 1: adding, subtracting and scaling", intro=(
                r"Given $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -2 \\ 0 & 5 \end{pmatrix}$, "
                r"find (a) $A + B$, (b) $A - B$, (c) $2A - B$."),
               steps=[
                   S("(a) Add entries in the same positions", math=r"A + B = \begin{pmatrix} 3 + 1 & 1 + (-2) \\ 2 + 0 & 4 + 5 \end{pmatrix} = \begin{pmatrix} 4 & -1 \\ 2 & 9 \end{pmatrix}"),
                   S("(b) Subtract entries in the same positions", math=r"A - B = \begin{pmatrix} 3 - 1 & 1 - (-2) \\ 2 - 0 & 4 - 5 \end{pmatrix} = \begin{pmatrix} 2 & 3 \\ 2 & -1 \end{pmatrix}"),
                   S("(c) First double every entry of A", math=r"2A = \begin{pmatrix} 6 & 2 \\ 4 & 8 \end{pmatrix}"),
                   S("Then subtract B", math=r"2A - B = \begin{pmatrix} 6 - 1 & 2 + 2 \\ 4 - 0 & 8 - 5 \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 4 & 3 \end{pmatrix}"),
               ]),
            MISTAKE("Losing a negative sign when subtracting",
                    r"Subtracting a negative entry adds it: $1 - (-2) = 3$. Write each subtraction in brackets before you simplify."),
            H("Multiplying two matrices"),
            T("To multiply two matrices, take a **row** of the first matrix and a **column** of the second. "
              "Multiply the matching entries and add the results. This gives one entry of the answer. "
              "Row 1 with column 1 gives the top-left entry, row 1 with column 2 gives the top-right entry, "
              "and so on. Two 2×2 matrices always give a 2×2 answer."),
            F(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} p & q \\ r & s \end{pmatrix} = \begin{pmatrix} ap + br & aq + bs \\ cp + dr & cq + ds \end{pmatrix}"),
            EX("Worked example 2: multiplying two 2×2 matrices", intro=(
                r"With $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -2 \\ 0 & 5 \end{pmatrix}$, find $AB$."),
               steps=[
                   S("Row 1 of A with column 1 of B", math=r"3(1) + 1(0) = 3"),
                   S("Row 1 of A with column 2 of B", math=r"3(-2) + 1(5) = -6 + 5 = -1"),
                   S("Row 2 of A with column 1 of B", math=r"2(1) + 4(0) = 2"),
                   S("Row 2 of A with column 2 of B", math=r"2(-2) + 4(5) = -4 + 20 = 16"),
                   S("Write the answer", math=r"AB = \begin{pmatrix} 3 & -1 \\ 2 & 16 \end{pmatrix}"),
               ]),
            MISTAKE("Thinking AB = BA",
                    r"With the same matrices, $BA = \begin{pmatrix} -1 & -7 \\ 10 & 20 \end{pmatrix}$, which is different from $AB$. "
                    r"Matrix multiplication is **not commutative**: in general $AB \neq BA$. Keep the order given in the question."),
            MISTAKE("Multiplying entries in the same positions",
                    "Matrix multiplication is not done position by position. Always go along a row of the first matrix and down a column of the second."),
            H("A 2×2 matrix times a 2×1 matrix"),
            T("A 2×2 matrix times a 2×1 column gives a 2×1 column. Each row of the 2×2 matrix meets the "
              "single column. The product is only possible when the number of **columns** in the first "
              "matrix equals the number of **rows** in the second."),
            EX("Worked example 3: spending at the market", intro=(
                "On Monday Mama Ngono buys 3 kg of tomatoes and 2 kg of onions. On Tuesday she buys 1 kg of tomatoes "
                "and 5 kg of onions. Tomatoes cost 400 FCFA per kg and onions cost 300 FCFA per kg. Use matrices to "
                "find what she spends each day."),
               steps=[
                   S("Quantity matrix (rows = days) and price column", math=r"\begin{pmatrix} 3 & 2 \\ 1 & 5 \end{pmatrix}\begin{pmatrix} 400 \\ 300 \end{pmatrix}"),
                   S("Row 1 with the column (Monday)", math=r"3(400) + 2(300) = 1200 + 600 = 1800"),
                   S("Row 2 with the column (Tuesday)", math=r"1(400) + 5(300) = 400 + 1500 = 1900"),
                   S("Answer", math=r"\begin{pmatrix} 1800 \\ 1900 \end{pmatrix}", text="She spends 1800 FCFA on Monday and 1900 FCFA on Tuesday."),
               ]),
            TIP(r"The order of the answer comes from the outside numbers: $(2 \times 2)(2 \times 1)$ gives $2 \times 1$. "
                r"A $2 \times 1$ matrix times a $2 \times 2$ matrix is **not possible**, because the inside numbers (1 and 2) differ."),
            H("The identity matrix"),
            D(r"The **identity matrix** $I$ has 1s on the leading diagonal and 0s elsewhere. It behaves like the number 1: "
              r"multiplying by it changes nothing.", title="Identity matrix",
              formula=r"I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad AI = IA = A"),
            QUIZ(r"Given $P = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$ and $Q = \begin{pmatrix} 1 & 4 \\ -1 & 2 \end{pmatrix}$, find $PQ$.",
                 [r"$\begin{pmatrix} 2 & 0 \\ -1 & 6 \end{pmatrix}$", r"$\begin{pmatrix} 6 & 12 \\ 0 & 6 \end{pmatrix}$",
                  r"$\begin{pmatrix} 2 & 8 \\ -2 & 10 \end{pmatrix}$", r"$\begin{pmatrix} 2 & 8 \\ 4 & 10 \end{pmatrix}$"], 2,
                 r"Row 1: $2(1) + 0(-1) = 2$ and $2(4) + 0(2) = 8$. Row 2: $1(1) + 3(-1) = -2$ and $1(4) + 3(2) = 10$.",
                 hint="Take row 1 of P and column 1 of Q: multiply matching entries and add.",
                 feedback=["You multiplied entries in the same positions. Use row times column.",
                           "This is $QP$, not $PQ$. The order matters.", "",
                           r"Bottom-left: $1(1) + 3(-1) = 1 - 3 = -2$. You lost the negative sign."]),
            H("Practice questions"),
            PQ(r"Given $P = \begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix}$ and $Q = \begin{pmatrix} 1 & 4 \\ -2 & 1 \end{pmatrix}$, find $3P - 2Q$.",
               r"$3P = \begin{pmatrix} 6 & -3 \\ 0 & 9 \end{pmatrix}$ and $2Q = \begin{pmatrix} 2 & 8 \\ -4 & 2 \end{pmatrix}$. "
               r"So $3P - 2Q = \begin{pmatrix} 6 - 2 & -3 - 8 \\ 0 - (-4) & 9 - 2 \end{pmatrix} = \begin{pmatrix} 4 & -11 \\ 4 & 7 \end{pmatrix}$."),
            PQ(r"Given $M = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, find $M^2$.",
               r"$M^2 = MM = \begin{pmatrix} 1(1) + 2(0) & 1(2) + 2(1) \\ 0(1) + 1(0) & 0(2) + 1(1) \end{pmatrix} = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$. "
               "You do not just square each entry."),
            PQ(r"Show that $AI = A$ when $A = \begin{pmatrix} 5 & -2 \\ 3 & 1 \end{pmatrix}$.",
               r"$AI = \begin{pmatrix} 5(1) + (-2)(0) & 5(0) + (-2)(1) \\ 3(1) + 1(0) & 3(0) + 1(1) \end{pmatrix} = \begin{pmatrix} 5 & -2 \\ 3 & 1 \end{pmatrix} = A$."),
            PQ(r"Given that $\begin{pmatrix} 2 & x \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 4 \\ 1 \end{pmatrix} = \begin{pmatrix} 11 \\ y \end{pmatrix}$, find $x$ and $y$.",
               r"Row 1: $2(4) + x(1) = 11$, so $8 + x = 11$ and $x = 3$. Row 2: $1(4) + 3(1) = y$, so $y = 7$."),
            SUM("The order of a matrix is rows × columns.",
                "Add, subtract and multiply by a number entry by entry; adding needs matrices of the same order.",
                "Multiply matrices row by column; a 2×2 times a 2×1 gives a 2×1.",
                r"In general $AB \neq BA$, so keep the order given.",
                r"The identity matrix $I$ has 1s on the leading diagonal and $AI = IA = A$."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Determinant and inverse
    lesson(
        module=MOD,
        topic=T_MAT,
        title="The determinant and inverse of a 2×2 matrix",
        slug="determinant-and-inverse-2x2",
        minutes=22,
        summary="Find the determinant ad − bc of a 2×2 matrix, recognise singular matrices, find the inverse and check that AA⁻¹ = I, and find an unknown that makes a matrix singular.",
        objectives=[
            "Calculate the determinant of a 2×2 matrix",
            "Decide whether a matrix is singular and explain why it has no inverse",
            "Find the inverse of a 2×2 matrix and check that the product is the identity matrix",
            "Find an unknown entry that makes a matrix singular",
        ],
        key_concepts=["Determinant", "Singular matrix", "Non-singular matrix", "Inverse matrix", "Identity matrix"],
        blocks=[
            H("Introduction"),
            T("In ordinary numbers, every number except 0 has a reciprocal: $5 \\times \\tfrac{1}{5} = 1$. "
              "Matrices have something similar, called the **inverse**. Multiplying a matrix by its inverse "
              "gives the identity matrix $I$ from the previous lesson."),
            T("Not every matrix has an inverse. One number, the **determinant**, tells you whether it does. "
              "In the next lesson you will use inverses to solve simultaneous equations, such as finding market prices."),
            H("The determinant"),
            D(r"The **determinant** of $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is the product of the leading diagonal "
              r"minus the product of the other diagonal.", title="Determinant",
              formula=r"\det A = |A| = ad - bc"),
            EX("Worked example 1: finding determinants", intro=(
                r"Find the determinant of (a) $\begin{pmatrix} 4 & -3 \\ 2 & 5 \end{pmatrix}$, (b) $\begin{pmatrix} 6 & 3 \\ 4 & 2 \end{pmatrix}$."),
               steps=[
                   S("(a) Leading diagonal and other diagonal", math=r"ad = 4(5) = 20, \quad bc = (-3)(2) = -6"),
                   S("Subtract", math=r"ad - bc = 20 - (-6) = 26"),
                   S("(b) Same method", math=r"6(2) - 3(4) = 12 - 12 = 0"),
                   S("Answer", text="(a) 26. (b) 0, so this matrix is singular."),
               ]),
            QUIZ(r"What is the determinant of $\begin{pmatrix} 5 & 2 \\ 3 & 2 \end{pmatrix}$?",
                 ["$16$", "$4$", "$-4$", "$1$"], 1,
                 r"$ad - bc = 5(2) - 2(3) = 10 - 6 = 4$.",
                 hint="Multiply down the leading diagonal, then subtract the other diagonal.",
                 feedback=["You added the two products. The determinant is $ad - bc$, a subtraction.", "",
                           "You calculated $bc - ad$. The order is $ad - bc$.",
                           "You subtracted entries instead of multiplying the diagonals."]),
            H("Singular matrices"),
            D(r"A matrix with determinant 0 is **singular**. It has **no inverse**. "
              r"A matrix with a non-zero determinant is **non-singular** and has an inverse.", title="Singular matrix",
              note="The reason: the inverse formula divides by the determinant, and you cannot divide by 0."),
            H("The inverse of a 2×2 matrix"),
            D(r"The **inverse** $A^{-1}$ is the matrix with $AA^{-1} = A^{-1}A = I$. To find it: swap $a$ and $d$, "
              r"change the signs of $b$ and $c$, then divide every entry by the determinant.", title="Inverse of a 2×2 matrix",
              formula=r"A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}"),
            EX("Worked example 2: an inverse, with a check", intro=(
                r"Find the inverse of $A = \begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix}$ and check your answer."),
               steps=[
                   S("Determinant", math=r"5(3) - 2(7) = 15 - 14 = 1"),
                   S("Swap a and d, change the signs of b and c", math=r"\begin{pmatrix} 3 & -2 \\ -7 & 5 \end{pmatrix}"),
                   S("Divide by the determinant (1)", math=r"A^{-1} = \begin{pmatrix} 3 & -2 \\ -7 & 5 \end{pmatrix}"),
                   S("Check that AA⁻¹ = I", math=r"\begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix}\begin{pmatrix} 3 & -2 \\ -7 & 5 \end{pmatrix} = \begin{pmatrix} 15 - 14 & -10 + 10 \\ 21 - 21 & -14 + 15 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}"),
               ]),
            EX("Worked example 3: a negative determinant", intro=(
                r"Find the inverse of $B = \begin{pmatrix} 4 & 2 \\ 3 & 1 \end{pmatrix}$."),
               steps=[
                   S("Determinant", math=r"4(1) - 2(3) = 4 - 6 = -2"),
                   S("Swap a and d, change the signs of b and c", math=r"\begin{pmatrix} 1 & -2 \\ -3 & 4 \end{pmatrix}"),
                   S("Divide every entry by −2", math=r"B^{-1} = \frac{1}{-2}\begin{pmatrix} 1 & -2 \\ -3 & 4 \end{pmatrix} = \begin{pmatrix} -\tfrac{1}{2} & 1 \\ \tfrac{3}{2} & -2 \end{pmatrix}"),
               ], check=r"BB^{-1}: \ 4(-\tfrac{1}{2}) + 2(\tfrac{3}{2}) = 1, \quad 4(1) + 2(-2) = 0, \quad 3(-\tfrac{1}{2}) + 1(\tfrac{3}{2}) = 0, \quad 3(1) + 1(-2) = 1"),
            MISTAKE("Changing the wrong signs",
                    "Only $b$ and $c$ change sign. $a$ and $d$ swap places but keep their own signs."),
            MISTAKE("Forgetting to divide by the determinant",
                    r"The matrix $\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$ is only the inverse when the determinant is 1. "
                    "Otherwise divide every entry by the determinant. Always check: the product must be $I$."),
            QUIZ(r"Which matrix is the inverse of $\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$?",
                 [r"$\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$", r"$\begin{pmatrix} -2 & 1 \\ 5 & -3 \end{pmatrix}$",
                  r"$\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$", r"$\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$"], 3,
                 r"The determinant is $3(2) - 1(5) = 1$. Swap 3 and 2, change the signs of 1 and 5: $\begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$.",
                 hint="Find the determinant first, then use swap-and-change-signs.",
                 feedback=["You swapped $a$ and $d$ but did not change the signs of $b$ and $c$.",
                           "You changed the signs of $a$ and $d$ instead of $b$ and $c$.",
                           "You changed the signs of $b$ and $c$ but forgot to swap $a$ and $d$.", ""]),
            H("Finding an unknown that makes a matrix singular"),
            EX("Worked example 4: singular matrix with an unknown", intro=(
                r"Find the values of $x$ for which $\begin{pmatrix} x & 3 \\ 4 & x + 4 \end{pmatrix}$ is singular."),
               steps=[
                   S("Singular means the determinant is 0", math=r"x(x + 4) - 3(4) = 0"),
                   S("Expand", math=r"x^2 + 4x - 12 = 0"),
                   S("Factorize", math=r"(x + 6)(x - 2) = 0"),
                   S("Solve", math=r"x = -6 \text{ or } x = 2"),
               ], check=r"x = 2: \ 2(6) - 12 = 0; \quad x = -6: \ (-6)(-2) - 12 = 0"),
            H("Practice questions"),
            PQ(r"Find the inverse of $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$ and check your answer.",
               r"Determinant $= 2(3) - 1(5) = 1$. Inverse $= \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$. "
               r"Check: $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 6 - 5 & -2 + 2 \\ 15 - 15 & -5 + 6 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$."),
            PQ(r"Find the value of $x$ for which $\begin{pmatrix} 3 & x \\ 2 & 4 \end{pmatrix}$ has no inverse.",
               r"No inverse means singular, so the determinant is 0: $3(4) - 2x = 0$, so $12 = 2x$ and $x = 6$."),
            PQ(r"Given $A = \begin{pmatrix} 3 & 2 \\ 4 & 2 \end{pmatrix}$, find $A^{-1}$ and show that $AA^{-1} = I$.",
               r"Determinant $= 3(2) - 2(4) = -2$. $A^{-1} = \frac{1}{-2}\begin{pmatrix} 2 & -2 \\ -4 & 3 \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 2 & -\tfrac{3}{2} \end{pmatrix}$. "
               r"Check: $\begin{pmatrix} 3(-1) + 2(2) & 3(1) + 2(-\tfrac{3}{2}) \\ 4(-1) + 2(2) & 4(1) + 2(-\tfrac{3}{2}) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$."),
            PQ(r"The determinant of $\begin{pmatrix} x & 5 \\ 2 & 3 \end{pmatrix}$ is 11. Find $x$.",
               r"$3x - 5(2) = 11$, so $3x - 10 = 11$, $3x = 21$ and $x = 7$."),
            SUM(r"The determinant of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is $ad - bc$.",
                "If the determinant is 0 the matrix is singular and has no inverse.",
                "Inverse: swap $a$ and $d$, change the signs of $b$ and $c$, divide by the determinant.",
                r"Always check that $AA^{-1} = I$.",
                "To make a matrix singular, set its determinant equal to 0 and solve."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Simultaneous equations
    lesson(
        module=MOD,
        topic=T_MAT,
        title="Solving simultaneous equations with matrices",
        slug="simultaneous-equations-matrix-method",
        minutes=22,
        summary="Write a pair of linear simultaneous equations as a matrix equation, solve it with the inverse matrix, check the answer, and use the method for market-price problems.",
        objectives=[
            "Write two linear simultaneous equations as a single matrix equation",
            "Solve the matrix equation by multiplying on the left by the inverse",
            "Check the solution in both original equations",
            "Set up and solve a word problem, such as market prices, by the matrix method",
        ],
        key_concepts=["Matrix equation", "Coefficient matrix", "Inverse matrix", "Unique solution"],
        blocks=[
            H("Introduction"),
            T("At a market in Ebolowa, 2 pineapples and 3 avocados cost 1300 FCFA, while 3 pineapples and 1 avocado "
              "cost 1250 FCFA. What does one of each cost? This is a pair of **simultaneous equations**."),
            T("You already know how to solve such pairs by substitution or elimination. In this lesson you use the "
              "determinant and inverse from the previous lesson to solve them with matrices. GCE questions often say "
              "\"use a matrix method\", so you must show the matrix working."),
            H("Writing the matrix equation"),
            D(r"The equations $ax + by = h$ and $cx + dy = k$ become one matrix equation. The numbers in front of $x$ and $y$ "
              r"form the **coefficient matrix** $A$.", title="Matrix form",
              formula=r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h \\ k \end{pmatrix}",
              note="Multiply out the left side to check: row 1 gives ax + by and row 2 gives cx + dy."),
            QUIZ(r"Which matrix equation represents $4x - y = 7$ and $x + 2y = 4$?",
                 [r"$\begin{pmatrix} 4 & 1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 7 \\ 4 \end{pmatrix}$",
                  r"$\begin{pmatrix} 4 & 1 \\ -1 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 7 \\ 4 \end{pmatrix}$",
                  r"$\begin{pmatrix} 4 & -1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 7 \\ 4 \end{pmatrix}$",
                  r"$\begin{pmatrix} 4 & -1 \\ 1 & 2 \end{pmatrix}\begin{pmatrix} 7 \\ 4 \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}$"], 2,
                 r"Row 1 holds the coefficients of the first equation, $4$ and $-1$; row 2 holds $1$ and $2$.",
                 hint="Each row of the matrix is one equation: the number in front of $x$, then the number in front of $y$.",
                 feedback=["The coefficient of $y$ in the first equation is $-1$, not $1$.",
                           "You put the coefficients of each equation in a column. Each equation goes in a row.", "",
                           "The unknowns $x$ and $y$ go in the column that multiplies the matrix, not on the right."]),
            H("Using the inverse"),
            T(r"If $A\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h \\ k \end{pmatrix}$, multiply both sides on the **left** by $A^{-1}$. "
              r"Since $A^{-1}A = I$ and $I\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ y \end{pmatrix}$, you get the answer directly."),
            F(r"\begin{pmatrix} x \\ y \end{pmatrix} = A^{-1}\begin{pmatrix} h \\ k \end{pmatrix}"),
            EX("Worked example 1: the matrix method", intro="Use a matrix method to solve $2x + 3y = 13$ and $x - y = -1$.",
               steps=[
                   S("Write in matrix form", math=r"\begin{pmatrix} 2 & 3 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 13 \\ -1 \end{pmatrix}"),
                   S("Find the determinant", math=r"2(-1) - 3(1) = -2 - 3 = -5"),
                   S("Find the inverse", math=r"A^{-1} = \frac{1}{-5}\begin{pmatrix} -1 & -3 \\ -1 & 2 \end{pmatrix}"),
                   S("Multiply the inverse by the right-hand side", math=r"\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{-5}\begin{pmatrix} -1(13) + (-3)(-1) \\ -1(13) + 2(-1) \end{pmatrix} = \frac{1}{-5}\begin{pmatrix} -10 \\ -15 \end{pmatrix}"),
                   S("Simplify", math=r"x = 2,\quad y = 3"),
               ], check=r"2(2) + 3(3) = 13 \text{ and } 2 - 3 = -1"),
            MISTAKE("Multiplying on the wrong side",
                    r"Write $A^{-1}\begin{pmatrix} h \\ k \end{pmatrix}$, not $\begin{pmatrix} h \\ k \end{pmatrix}A^{-1}$. A 2×1 matrix times a 2×2 matrix cannot be done."),
            MISTAKE("Not lining up the equations first",
                    "Before writing the matrix, put both equations in the form $ax + by = h$, with $x$ first, then $y$, then the number on the right."),
            EX("Worked example 2: rearranging first", intro="Use a matrix method to solve $y = 2x - 5$ and $3x + y = 10$.",
               steps=[
                   S("Rearrange the first equation", math=r"-2x + y = -5"),
                   S("Matrix form", math=r"\begin{pmatrix} -2 & 1 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -5 \\ 10 \end{pmatrix}"),
                   S("Determinant and inverse", math=r"\det = -2(1) - 1(3) = -5, \quad A^{-1} = \frac{1}{-5}\begin{pmatrix} 1 & -1 \\ -3 & -2 \end{pmatrix}"),
                   S("Multiply on the left", math=r"\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{-5}\begin{pmatrix} -5 - 10 \\ 15 - 20 \end{pmatrix} = \frac{1}{-5}\begin{pmatrix} -15 \\ -5 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}"),
               ], check=r"y = 2(3) - 5 = 1 \text{ and } 3(3) + 1 = 10"),
            KEY("When the method fails", "If the coefficient matrix is singular (determinant 0), it has no inverse.",
                cards=[["Determinant not 0", "There is exactly one solution, found with the inverse."],
                       ["Determinant 0", "There is no unique solution: the lines are parallel or the same line."]]),
            H("A market-prices word problem"),
            EX("Worked example 3: prices at Ebolowa market", intro=(
                "2 pineapples and 3 avocados cost 1300 FCFA. 3 pineapples and 1 avocado cost 1250 FCFA. "
                "Use a matrix method to find the price of one pineapple and one avocado."),
               steps=[
                   S("Choose letters", text="Let p FCFA be the price of a pineapple and a FCFA the price of an avocado."),
                   S("Matrix equation", math=r"\begin{pmatrix} 2 & 3 \\ 3 & 1 \end{pmatrix}\begin{pmatrix} p \\ a \end{pmatrix} = \begin{pmatrix} 1300 \\ 1250 \end{pmatrix}"),
                   S("Determinant and inverse", math=r"\det = 2(1) - 3(3) = -7, \quad A^{-1} = \frac{1}{-7}\begin{pmatrix} 1 & -3 \\ -3 & 2 \end{pmatrix}"),
                   S("Multiply on the left", math=r"\begin{pmatrix} p \\ a \end{pmatrix} = \frac{1}{-7}\begin{pmatrix} 1300 - 3750 \\ -3900 + 2500 \end{pmatrix} = \frac{1}{-7}\begin{pmatrix} -2450 \\ -1400 \end{pmatrix} = \begin{pmatrix} 350 \\ 200 \end{pmatrix}"),
                   S("Answer in words", text="A pineapple costs 350 FCFA and an avocado costs 200 FCFA."),
               ], check=r"2(350) + 3(200) = 1300 \text{ and } 3(350) + 200 = 1250"),
            QUIZ(r"What happens when you try to solve $2x + 4y = 6$ and $x + 2y = 5$ by the matrix method?",
                 ["You get $x = 1$, $y = 1$",
                  "The determinant is 0, so there is no inverse and no unique solution",
                  "The determinant is 8, so the method works",
                  "You must swap the two equations first"], 1,
                 r"$\det = 2(2) - 4(1) = 0$. The matrix is singular. (The lines $2x + 4y = 6$ and $x + 2y = 5$ are parallel, so they never meet.)",
                 hint="Find the determinant of the coefficient matrix before anything else.",
                 feedback=[r"Check in the second equation: $1 + 2(1) = 3$, not 5. This pair has no solution.", "",
                           r"You added $ad + bc$. The determinant is $ad - bc = 4 - 4 = 0$.",
                           "Swapping the equations does not change whether the determinant is 0."]),
            H("Practice questions"),
            PQ("Use a matrix method to solve $5x + 2y = 19$ and $3x + y = 11$.",
               r"$\det = 5(1) - 2(3) = -1$, so $A^{-1} = \frac{1}{-1}\begin{pmatrix} 1 & -2 \\ -3 & 5 \end{pmatrix}$. "
               r"Then $\begin{pmatrix} x \\ y \end{pmatrix} = -1\begin{pmatrix} 19 - 22 \\ -57 + 55 \end{pmatrix} = -1\begin{pmatrix} -3 \\ -2 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$. "
               r"Check: $5(3) + 2(2) = 19$ and $3(3) + 2 = 11$."),
            PQ("A school buys 3 exercise books and 2 pens for 1100 FCFA, and 1 exercise book and 4 pens for 1200 FCFA. "
               "(a) Write a matrix equation for the price $b$ FCFA of a book and $p$ FCFA of a pen. (b) Solve it.",
               r"(a) $\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}\begin{pmatrix} b \\ p \end{pmatrix} = \begin{pmatrix} 1100 \\ 1200 \end{pmatrix}$. "
               r"(b) $\det = 12 - 2 = 10$, $A^{-1} = \frac{1}{10}\begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix}$, so "
               r"$\begin{pmatrix} b \\ p \end{pmatrix} = \frac{1}{10}\begin{pmatrix} 4400 - 2400 \\ -1100 + 3600 \end{pmatrix} = \begin{pmatrix} 200 \\ 250 \end{pmatrix}$. "
               r"A book costs 200 FCFA and a pen 250 FCFA. Check: $600 + 500 = 1100$ and $200 + 1000 = 1200$."),
            PQ("Explain why the equations $3x - 6y = 4$ and $x - 2y = 1$ cannot be solved by the matrix method.",
               r"The coefficient matrix is $\begin{pmatrix} 3 & -6 \\ 1 & -2 \end{pmatrix}$ with determinant $3(-2) - (-6)(1) = -6 + 6 = 0$. "
               "It is singular, so it has no inverse and the pair has no unique solution."),
            PQ("A moto-taxi driver in Douala earns 2400 FCFA for 3 short trips and 2 long trips, and 3800 FCFA for 1 short trip and "
               "4 long trips. Use a matrix method to find the fare for each kind of trip.",
               r"Let $s$ and $l$ be the fares in FCFA: $\begin{pmatrix} 3 & 2 \\ 1 & 4 \end{pmatrix}\begin{pmatrix} s \\ l \end{pmatrix} = \begin{pmatrix} 2400 \\ 3800 \end{pmatrix}$. "
               r"$\det = 10$, so $\begin{pmatrix} s \\ l \end{pmatrix} = \frac{1}{10}\begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix}\begin{pmatrix} 2400 \\ 3800 \end{pmatrix} = \frac{1}{10}\begin{pmatrix} 2000 \\ 9000 \end{pmatrix} = \begin{pmatrix} 200 \\ 900 \end{pmatrix}$. "
               r"A short trip costs 200 FCFA and a long trip 900 FCFA. Check: $600 + 1800 = 2400$ and $200 + 3600 = 3800$."),
            SUM(r"Write $ax + by = h$, $cx + dy = k$ as $\begin{pmatrix} a & b \\ c & d \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} h \\ k \end{pmatrix}$.",
                r"Solve with $\begin{pmatrix} x \\ y \end{pmatrix} = A^{-1}\begin{pmatrix} h \\ k \end{pmatrix}$, multiplying on the left.",
                "Line up both equations as ax + by = h before writing the matrix.",
                "If the determinant is 0 there is no unique solution.",
                "Always check your answer in both original equations and answer word problems in words."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Column vectors
    lesson(
        module=MOD,
        topic=T_VEC,
        title="Column vectors and vector arithmetic",
        slug="column-vectors-and-vector-arithmetic",
        minutes=20,
        summary="Write movements as column vectors, read and draw vectors on a grid, and add, subtract and multiply vectors by a number.",
        objectives=[
            "Write a movement on a grid as a column vector and draw a vector from its column",
            "Recognise equal vectors and the negative of a vector",
            "Add and subtract column vectors and draw the result nose to tail",
            "Multiply a vector by a number (a scalar)",
        ],
        key_concepts=["Vector", "Scalar", "Column vector", "Equal vectors", "Negative vector", "Scalar multiple"],
        blocks=[
            H("Introduction"),
            T("Some quantities need only a size, such as a price of 500 FCFA or a mass of 2 kg. These are **scalars**. "
              "Others need a size **and** a direction. A moto-taxi that rides 4 km east and then 3 km north has a "
              "**displacement**, which we describe with a **vector**."),
            T("In this topic you will work with vectors in two dimensions. This first lesson shows how to write them, "
              "draw them and do arithmetic with them."),
            D(r"A **column vector** shows a movement. The top number is the movement in the $x$-direction (right is positive, "
              r"left is negative). The bottom number is the movement in the $y$-direction (up is positive, down is negative).",
              title="Column vector", formula=r"\mathbf{a} = \begin{pmatrix} 3 \\ 2 \end{pmatrix} \text{ means 3 right and 2 up}",
              note=r"In print a vector is written in bold, $\mathbf{a}$. By hand, underline it: $\underline{a}$. The vector from point $A$ to point $B$ is written $\overrightarrow{AB}$."),
            QUIZ("Which column vector describes a movement of 2 units left and 5 units up?",
                 [r"$\begin{pmatrix} 2 \\ 5 \end{pmatrix}$", r"$\begin{pmatrix} -2 \\ 5 \end{pmatrix}$",
                  r"$\begin{pmatrix} 5 \\ -2 \end{pmatrix}$", r"$\begin{pmatrix} -2 \\ -5 \end{pmatrix}$"], 1,
                 r"Left is negative and up is positive, with the $x$-movement on top: $\begin{pmatrix} -2 \\ 5 \end{pmatrix}$.",
                 hint="The top number is the left-right movement. Which direction is negative?",
                 feedback=["Left is the negative $x$-direction, so the top number must be $-2$.", "",
                           "You put the up-down movement on top. The top number is always the $x$-movement.",
                           "Up is positive, so the bottom number is $+5$."]),
            H("Drawing vectors on a grid"),
            T("To draw a vector, choose a starting point, count the top number across and the bottom number up or down, "
              "then draw an arrow from the start to the end. The arrow shows the direction."),
            KEY("Equal and negative vectors", "Position on the grid does not matter for a vector: only its size and direction.",
                cards=[["Equal vectors", "Same size and same direction. They have the same column, wherever they are drawn."],
                       ["Negative vector", r"$-\mathbf{a}$ has the same size as $\mathbf{a}$ but the opposite direction: change both signs."]]),
            H("Adding and subtracting vectors"),
            T("Add or subtract the top numbers together and the bottom numbers together. On a grid, adding means joining "
              r"the vectors **nose to tail**: draw $\mathbf{b}$ starting where $\mathbf{a}$ ends. The **resultant** $\mathbf{a} + \mathbf{b}$ goes "
              r"from the start of $\mathbf{a}$ to the end of $\mathbf{b}$."),
            IMG("f5m-vector-addition.svg",
                "Grid showing vector a, 3 right and 2 up, followed nose to tail by vector b, 1 right and 3 down. A green arrow a + b goes from the start of a to the end of b and equals the column 4, minus 1.",
                "Figure 1. Adding vectors nose to tail: a + b = (4, −1)."),
            T(r"To subtract, add the negative: $\mathbf{a} - \mathbf{b} = \mathbf{a} + (-\mathbf{b})$."),
            H("Multiplying by a scalar"),
            D(r"To multiply a vector by a number $k$, multiply both components by $k$. The new vector $k\mathbf{a}$ is "
              r"parallel to $\mathbf{a}$ and $k$ times as long. If $k$ is negative it points the opposite way.",
              title="Scalar multiple", formula=r"k\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} kx \\ ky \end{pmatrix}"),
            EX("Worked example 1: vector arithmetic", intro=(
                r"Given $\mathbf{a} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 1 \\ -3 \end{pmatrix}$, "
                r"find (a) $\mathbf{a} + \mathbf{b}$, (b) $\mathbf{a} - \mathbf{b}$, (c) $2\mathbf{a} - 3\mathbf{b}$."),
               steps=[
                   S("(a) Add top and bottom separately", math=r"\begin{pmatrix} 3 + 1 \\ 2 + (-3) \end{pmatrix} = \begin{pmatrix} 4 \\ -1 \end{pmatrix}"),
                   S("(b) Subtract top and bottom separately", math=r"\begin{pmatrix} 3 - 1 \\ 2 - (-3) \end{pmatrix} = \begin{pmatrix} 2 \\ 5 \end{pmatrix}"),
                   S("(c) Scale each vector first", math=r"2\mathbf{a} = \begin{pmatrix} 6 \\ 4 \end{pmatrix}, \quad 3\mathbf{b} = \begin{pmatrix} 3 \\ -9 \end{pmatrix}"),
                   S("Then subtract", math=r"2\mathbf{a} - 3\mathbf{b} = \begin{pmatrix} 6 - 3 \\ 4 - (-9) \end{pmatrix} = \begin{pmatrix} 3 \\ 13 \end{pmatrix}"),
               ]),
            EX("Worked example 2: a cyclist's journey", intro=(
                "A cyclist leaves Bamenda market and rides 4 km east and 3 km north, then 2 km east and 5 km north. "
                "Taking east and north as positive, write the total displacement as a column vector."),
               steps=[
                   S("First stage", math=r"\begin{pmatrix} 4 \\ 3 \end{pmatrix}"),
                   S("Second stage", math=r"\begin{pmatrix} 2 \\ 5 \end{pmatrix}"),
                   S("Add the stages", math=r"\begin{pmatrix} 4 \\ 3 \end{pmatrix} + \begin{pmatrix} 2 \\ 5 \end{pmatrix} = \begin{pmatrix} 6 \\ 8 \end{pmatrix}", text="The cyclist ends 6 km east and 8 km north of the market."),
               ]),
            MISTAKE("Mixing up the top and bottom numbers",
                    "The top number is always the movement across ($x$) and the bottom number the movement up or down ($y$)."),
            MISTAKE("Sign errors when subtracting",
                    r"Subtracting a negative component adds it: $2 - (-3) = 5$. Write each subtraction with brackets."),
            QUIZ(r"Given $\mathbf{a} = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} -1 \\ 4 \end{pmatrix}$, find $2\mathbf{a} - \mathbf{b}$.",
                 [r"$\begin{pmatrix} 5 \\ 0 \end{pmatrix}$", r"$\begin{pmatrix} 4 \\ -6 \end{pmatrix}$",
                  r"$\begin{pmatrix} 7 \\ 0 \end{pmatrix}$", r"$\begin{pmatrix} 7 \\ -8 \end{pmatrix}$"], 3,
                 r"$2\mathbf{a} = \begin{pmatrix} 6 \\ -4 \end{pmatrix}$, then $\begin{pmatrix} 6 - (-1) \\ -4 - 4 \end{pmatrix} = \begin{pmatrix} 7 \\ -8 \end{pmatrix}$.",
                 hint=r"Find $2\mathbf{a}$ first, then subtract the top numbers and the bottom numbers separately.",
                 feedback=[r"This is $2\mathbf{a} + \mathbf{b}$. You added $\mathbf{b}$ instead of subtracting it.",
                           r"This is $\mathbf{a} - \mathbf{b}$. You forgot to multiply $\mathbf{a}$ by 2.",
                           r"Bottom number: $-4 - 4 = -8$, not 0.", ""]),
            H("Practice questions"),
            PQ(r"Given $\mathbf{u} = \begin{pmatrix} 5 \\ -2 \end{pmatrix}$ and $\mathbf{v} = \begin{pmatrix} -1 \\ 3 \end{pmatrix}$, find (a) $\mathbf{u} + \mathbf{v}$, (b) $\mathbf{u} - \mathbf{v}$, (c) $4\mathbf{v}$.",
               r"(a) $\begin{pmatrix} 4 \\ 1 \end{pmatrix}$. (b) $\begin{pmatrix} 5 - (-1) \\ -2 - 3 \end{pmatrix} = \begin{pmatrix} 6 \\ -5 \end{pmatrix}$. (c) $\begin{pmatrix} -4 \\ 12 \end{pmatrix}$."),
            PQ(r"Find $x$ and $y$ given that $\begin{pmatrix} x \\ 3 \end{pmatrix} + 2\begin{pmatrix} 1 \\ y \end{pmatrix} = \begin{pmatrix} 7 \\ -1 \end{pmatrix}$.",
               r"Top: $x + 2 = 7$, so $x = 5$. Bottom: $3 + 2y = -1$, so $2y = -4$ and $y = -2$."),
            PQ(r"$\mathbf{a} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$. Find the vector $\mathbf{c}$ such that $\mathbf{a} + \mathbf{c} = \begin{pmatrix} -3 \\ 4 \end{pmatrix}$.",
               r"$\mathbf{c} = \begin{pmatrix} -3 \\ 4 \end{pmatrix} - \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} -5 \\ 3 \end{pmatrix}$."),
            PQ(r"On a grid, $\mathbf{p} = \begin{pmatrix} -2 \\ 3 \end{pmatrix}$. Describe how to draw $\mathbf{p}$ and $-\mathbf{p}$ starting from the same point.",
               r"For $\mathbf{p}$: from the start, go 2 units left and 3 units up, and draw the arrow to that point. "
               r"$-\mathbf{p} = \begin{pmatrix} 2 \\ -3 \end{pmatrix}$: go 2 right and 3 down. The two arrows have the same length but point in opposite directions."),
            SUM(r"A column vector $\begin{pmatrix} x \\ y \end{pmatrix}$ means $x$ across (right positive) and $y$ up (up positive).",
                "Equal vectors have the same column; the negative vector has both signs changed.",
                "Add or subtract vectors component by component; on a grid, join them nose to tail.",
                r"$k\mathbf{a}$ multiplies both components by $k$ and is parallel to $\mathbf{a}$."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Magnitude and direction
    lesson(
        module=MOD,
        topic=T_VEC,
        title="Magnitude and direction of a vector",
        slug="vector-magnitude-and-direction",
        minutes=22,
        summary="Find the magnitude of a column vector with Pythagoras' theorem, in surd form or to 1 decimal place, and give its direction as an angle from the positive x-axis or as a bearing.",
        objectives=[
            "Find the magnitude of a column vector using Pythagoras' theorem",
            "Give a magnitude exactly in surd form or correct to 1 decimal place",
            "Find the direction of a vector as an angle measured from the positive x-axis",
            "Give the direction of a displacement as a three-figure bearing",
        ],
        key_concepts=["Magnitude", "Modulus", "Direction", "Surd form", "Bearing"],
        blocks=[
            H("Introduction"),
            T(r"In the previous lesson a cyclist rode from Bamenda market and ended with displacement $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$ km, "
              "6 km east and 8 km north. But how far is the cyclist from the market in a straight line, and in which direction?"),
            T("The straight-line distance is the **magnitude** of the vector. The direction can be given as an angle or as a "
              "bearing. Both come from the right-angled triangle formed by the two components."),
            H("Magnitude"),
            D(r"The **magnitude** (or **modulus**) of a vector is its length. The two components are the sides of a right-angled "
              r"triangle, so Pythagoras' theorem gives the length.", title="Magnitude",
              formula=r"\left|\begin{pmatrix} x \\ y \end{pmatrix}\right| = \sqrt{x^2 + y^2}",
              note=r"The magnitude of $\mathbf{a}$ is written $|\mathbf{a}|$, and the magnitude of $\overrightarrow{AB}$ is written $|\overrightarrow{AB}|$ or $AB$. A magnitude is never negative."),
            EX("Worked example 1: magnitudes", intro=(
                r"Find the magnitude of (a) $\begin{pmatrix} 6 \\ 8 \end{pmatrix}$, (b) $\begin{pmatrix} 3 \\ -5 \end{pmatrix}$ correct to 1 decimal place, "
                r"(c) $\begin{pmatrix} 2 \\ 4 \end{pmatrix}$ in surd form."),
               steps=[
                   S("(a) Square, add, square root", math=r"\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10", text="The cyclist is 10 km from the market."),
                   S("(b) A negative component squared is positive", math=r"\sqrt{3^2 + (-5)^2} = \sqrt{9 + 25} = \sqrt{34} \approx 5.8"),
                   S("(c) Simplify the surd", math=r"\sqrt{2^2 + 4^2} = \sqrt{20} = \sqrt{4 \times 5} = 2\sqrt{5}"),
               ]),
            TIP(r"When a question says 'exact' or 'surd form', leave the square root: $\sqrt{34}$ or $2\sqrt{5}$. "
                "Otherwise round as asked, usually to 1 decimal place or 3 significant figures."),
            QUIZ(r"What is the magnitude of $\begin{pmatrix} -5 \\ 12 \end{pmatrix}$?",
                 ["$7$", r"$\sqrt{119}$", "$13$", "$17$"], 2,
                 r"$\sqrt{(-5)^2 + 12^2} = \sqrt{25 + 144} = \sqrt{169} = 13$.",
                 hint="Square both numbers first. A negative number squared is positive.",
                 feedback=["You added $-5$ and $12$. Use Pythagoras: square, add, square root.",
                           r"You worked out $144 - 25$. $(-5)^2 = +25$, so you must add.", "",
                           "You added 5 and 12. The magnitude is not the sum of the components."]),
            MISTAKE("Adding the components instead of using Pythagoras",
                    r"$\left|\begin{pmatrix} 6 \\ 8 \end{pmatrix}\right|$ is $10$, not $6 + 8 = 14$. Square each component, add, then take the square root."),
            H("Direction as an angle"),
            D(r"The **direction** of a vector can be given as the angle $\theta$ it makes with the positive $x$-axis, measured "
              r"anticlockwise. Find the angle in the triangle with $\tan = \dfrac{\text{opposite}}{\text{adjacent}}$, then use a sketch to decide the quadrant.",
              title="Direction", formula=r"\tan\alpha = \frac{|y|}{|x|}"),
            T("When the components are east and north, the direction is often given as a **bearing**: the angle measured "
              "**clockwise from north**, written with three figures, such as 053.1°."),
            IMG("f5m-vector-direction.svg",
                "Vector OP from the origin, 4 units east and 3 units north, with length 5. The angle theta between OP and the east axis is 36.9 degrees; the angle beta between north and OP is 53.1 degrees, so the bearing is 053.1 degrees.",
                "Figure 1. For OP = (4, 3): θ = 36.9° from east, bearing 053.1°."),
            EX("Worked example 2: angle and bearing", intro=(
                r"A moto-taxi's displacement is $\begin{pmatrix} 4 \\ 3 \end{pmatrix}$ km (east, north). Find the angle it makes with east and its bearing."),
               steps=[
                   S("Both components are positive", text="The vector points up and to the right (north-east)."),
                   S("Angle with east", math=r"\tan\theta = \frac{3}{4} = 0.75 \Rightarrow \theta = \tan^{-1}(0.75) \approx 36.9^\circ"),
                   S("Angle from north, clockwise", math=r"90^\circ - 36.9^\circ = 53.1^\circ"),
                   S("Answer", text="36.9° north of east, which is a bearing of 053.1°."),
               ]),
            EX("Worked example 3: a vector pointing left", intro=(
                r"Find the magnitude and direction of $\mathbf{v} = \begin{pmatrix} -6 \\ 8 \end{pmatrix}$, giving the direction both as an angle "
                r"from the positive $x$-axis and as a bearing (with $x$ east and $y$ north)."),
               steps=[
                   S("Magnitude", math=r"|\mathbf{v}| = \sqrt{36 + 64} = 10"),
                   S("Sketch", text="6 left and 8 up: the vector is in the second quadrant (north-west)."),
                   S("Angle with the negative x-axis", math=r"\tan\alpha = \frac{8}{6} \Rightarrow \alpha \approx 53.1^\circ"),
                   S("Angle from the positive x-axis", math=r"\theta = 180^\circ - 53.1^\circ = 126.9^\circ"),
                   S("Bearing: angle west of north, then subtract from 360°", math=r"\tan\beta = \frac{6}{8} \Rightarrow \beta \approx 36.9^\circ, \quad 360^\circ - 36.9^\circ = 323.1^\circ"),
               ]),
            MISTAKE("Trusting the calculator angle without a sketch",
                    r"$\tan^{-1}\left(\frac{8}{-6}\right)$ gives $-53.1^\circ$ on a calculator, which is the wrong quadrant. Always sketch the vector first."),
            QUIZ(r"A boat's displacement is $\begin{pmatrix} 3 \\ -3 \end{pmatrix}$ km (east, north). What is its bearing?",
                 ["$045^\\circ$", "$135^\\circ$", "$315^\\circ$", "$-45^\\circ$"], 1,
                 r"3 km east and 3 km south is south-east. The angle from north, clockwise, is $90^\circ + 45^\circ = 135^\circ$.",
                 hint="Sketch it: east is right and a negative north component means south.",
                 feedback=["That is north-east. The second component is negative, so the boat goes south.", "",
                           "315° is north-west, the direction of $\\begin{pmatrix} -3 \\\\ 3 \\end{pmatrix}$.",
                           "Bearings are measured clockwise from north and are never negative."]),
            H("Practice questions"),
            PQ(r"Find the magnitude of $\begin{pmatrix} -7 \\ 24 \end{pmatrix}$.",
               r"$\sqrt{(-7)^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25$."),
            PQ(r"The vector $\begin{pmatrix} k \\ 12 \end{pmatrix}$ has magnitude 13. Find the possible values of $k$.",
               r"$k^2 + 144 = 169$, so $k^2 = 25$ and $k = 5$ or $k = -5$."),
            PQ(r"$\mathbf{a} = \begin{pmatrix} 1 \\ 3 \end{pmatrix}$ and $\mathbf{b} = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$. Find $|\mathbf{a} + \mathbf{b}|$ in surd form and correct to 1 decimal place.",
               r"$\mathbf{a} + \mathbf{b} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$, so $|\mathbf{a} + \mathbf{b}| = \sqrt{9 + 4} = \sqrt{13} \approx 3.6$."),
            PQ(r"A hiker's displacement is $\begin{pmatrix} -3 \\ -4 \end{pmatrix}$ km (east, north). Find (a) the distance from the start, (b) the bearing of the hiker from the start.",
               r"(a) $\sqrt{9 + 16} = 5$ km. (b) 3 km west and 4 km south is south-west. The angle west of south is $\tan^{-1}\left(\frac{3}{4}\right) \approx 36.9^\circ$, "
               r"so the bearing is $180^\circ + 36.9^\circ = 216.9^\circ$."),
            SUM(r"Magnitude: $\left|\begin{pmatrix} x \\ y \end{pmatrix}\right| = \sqrt{x^2 + y^2}$, never negative.",
                "Give exact answers in surd form when asked; otherwise round to 1 decimal place.",
                r"Direction: find the angle in the right-angled triangle with $\tan$, then use a sketch for the quadrant.",
                "A bearing is measured clockwise from north and written with three figures."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Position vectors and collinearity
    lesson(
        module=MOD,
        topic=T_VEC,
        title="Position vectors, parallel vectors and collinear points",
        slug="position-vectors-parallel-collinear",
        minutes=24,
        summary="Use position vectors to find the vector between two points and the midpoint of a line, recognise parallel vectors as multiples, and prove that three points are collinear.",
        objectives=[
            "Write the position vector of a point and find AB = OB − OA",
            "Find the position vector of the midpoint of a line segment",
            "Decide whether two vectors are parallel and find an unknown that makes them parallel",
            "Prove that three points are collinear, and find an unknown coordinate that makes them collinear",
        ],
        key_concepts=["Position vector", "Vector between two points", "Midpoint", "Parallel vectors", "Collinear points"],
        blocks=[
            H("Introduction"),
            T("Surveyors planning a straight road between Yaoundé and a new village need to know whether three marker posts "
              "lie on one straight line. Vectors answer questions like this neatly."),
            T("In this lesson you join the ideas of the previous two lessons: you find vectors between points, their midpoints, "
              "and use multiples of vectors to test for parallel lines and points on a line."),
            H("Position vectors"),
            D(r"The **position vector** of a point $A$ is the vector $\overrightarrow{OA}$ from the origin $O$ to $A$. "
              r"If $A$ is the point $(2, 3)$, then $\overrightarrow{OA} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$.", title="Position vector",
              note=r"Position vectors are often given letters: $\overrightarrow{OA} = \mathbf{a}$, $\overrightarrow{OB} = \mathbf{b}$."),
            D(r"To go from $A$ to $B$, go back from $A$ to $O$ and then out to $B$: end minus start.", title="Vector between two points",
              formula=r"\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = \mathbf{b} - \mathbf{a}"),
            D(r"The midpoint $M$ of $AB$ is half way along $\overrightarrow{AB}$, starting from $A$.", title="Midpoint",
              formula=r"\overrightarrow{OM} = \overrightarrow{OA} + \tfrac{1}{2}\overrightarrow{AB} = \tfrac{1}{2}(\mathbf{a} + \mathbf{b})"),
            EX("Worked example 1: vector, length and midpoint", intro=(
                r"$\overrightarrow{OA} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$ and $\overrightarrow{OB} = \begin{pmatrix} 8 \\ -5 \end{pmatrix}$. "
                r"Find (a) $\overrightarrow{AB}$, (b) $|\overrightarrow{AB}|$, (c) the position vector of $M$, the midpoint of $AB$."),
               steps=[
                   S("(a) End minus start", math=r"\overrightarrow{AB} = \begin{pmatrix} 8 - 2 \\ -5 - 3 \end{pmatrix} = \begin{pmatrix} 6 \\ -8 \end{pmatrix}"),
                   S("(b) Magnitude", math=r"|\overrightarrow{AB}| = \sqrt{6^2 + (-8)^2} = \sqrt{100} = 10"),
                   S("(c) Half the sum of the position vectors", math=r"\overrightarrow{OM} = \tfrac{1}{2}\begin{pmatrix} 2 + 8 \\ 3 + (-5) \end{pmatrix} = \tfrac{1}{2}\begin{pmatrix} 10 \\ -2 \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \end{pmatrix}"),
               ], check=r"\overrightarrow{OA} + \tfrac{1}{2}\overrightarrow{AB} = \begin{pmatrix} 2 + 3 \\ 3 - 4 \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \end{pmatrix}"),
            MISTAKE("Subtracting in the wrong order",
                    r"$\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$ (end minus start). Start minus end gives $\overrightarrow{BA}$, which points the other way."),
            H("Parallel vectors"),
            D(r"Two vectors are **parallel** if one is a number times the other: $\mathbf{b} = k\mathbf{a}$. "
              r"If $k$ is negative they point in opposite directions.", title="Parallel vectors"),
            QUIZ(r"Which vector is parallel to $\begin{pmatrix} 2 \\ -3 \end{pmatrix}$?",
                 [r"$\begin{pmatrix} 4 \\ 6 \end{pmatrix}$", r"$\begin{pmatrix} 3 \\ -2 \end{pmatrix}$",
                  r"$\begin{pmatrix} 6 \\ 9 \end{pmatrix}$", r"$\begin{pmatrix} -4 \\ 6 \end{pmatrix}$"], 3,
                 r"$\begin{pmatrix} -4 \\ 6 \end{pmatrix} = -2\begin{pmatrix} 2 \\ -3 \end{pmatrix}$, so it is parallel (opposite direction).",
                 hint="Look for one number that multiplies both the top and the bottom.",
                 feedback=["The top is multiplied by 2 but the bottom by $-2$. Both must use the same number.",
                           "The numbers are swapped, not multiplied by one number.",
                           "Top times 3, bottom times $-3$: not the same number.", ""]),
            H("Collinear points"),
            D(r"Points $A$, $B$ and $C$ are **collinear** (on one straight line) if $\overrightarrow{AC} = k\,\overrightarrow{AB}$ "
              r"for some number $k$. The vectors are parallel **and** share the point $A$.", title="Collinear points"),
            EX("Worked example 2: proving points are collinear", intro=(
                "Show that $A(1, 2)$, $B(3, 5)$ and $C(7, 11)$ are collinear."),
               steps=[
                   S("Find AB", math=r"\overrightarrow{AB} = \begin{pmatrix} 3 - 1 \\ 5 - 2 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}"),
                   S("Find AC", math=r"\overrightarrow{AC} = \begin{pmatrix} 7 - 1 \\ 11 - 2 \end{pmatrix} = \begin{pmatrix} 6 \\ 9 \end{pmatrix}"),
                   S("Compare them", math=r"\overrightarrow{AC} = 3\begin{pmatrix} 2 \\ 3 \end{pmatrix} = 3\,\overrightarrow{AB}"),
                   S("Conclude", text="AB and AC are parallel and both pass through A, so A, B and C lie on one straight line."),
               ]),
            IMG("f5-collinear-points.svg",
                "Grid with points A(1, 2), B(3, 5) and C(7, 11) on one straight line. A blue arrow from A to B goes 2 right and 3 up; a green arrow from A to C goes 6 right and 9 up. Beside the grid: AB = (2, 3) and AC = (6, 9) = 3 times (2, 3).",
                "Figure 1. AC is 3 times AB and both start at A, so A, B and C are collinear."),
            EX("Worked example 3: an unknown coordinate", intro=(
                "The points $A(1, -1)$, $B(3, 2)$ and $C(9, k)$ are collinear. Find $k$."),
               steps=[
                   S("Find AB and AC", math=r"\overrightarrow{AB} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}, \quad \overrightarrow{AC} = \begin{pmatrix} 8 \\ k + 1 \end{pmatrix}"),
                   S("Find the multiplier from the top numbers", math=r"8 = 4 \times 2, \text{ so } \overrightarrow{AC} = 4\,\overrightarrow{AB}"),
                   S("Use it on the bottom numbers", math=r"k + 1 = 4 \times 3 = 12"),
                   S("Solve", math=r"k = 11"),
               ]),
            MISTAKE("Saying 'parallel' is enough for collinear",
                    "Parallel lines can be far apart. You must also state that the two vectors share a common point."),
            H("Practice questions"),
            PQ(r"Find the value of $k$ for which $\begin{pmatrix} k \\ 6 \end{pmatrix}$ is parallel to $\begin{pmatrix} 2 \\ 3 \end{pmatrix}$.",
               r"The bottom number has been multiplied by $6 \div 3 = 2$. So the top must also be multiplied by 2: $k = 2 \times 2 = 4$."),
            PQ("Show that $P(-1, 4)$, $Q(1, 1)$ and $R(5, -5)$ are collinear.",
               r"$\overrightarrow{PQ} = \begin{pmatrix} 2 \\ -3 \end{pmatrix}$ and $\overrightarrow{PR} = \begin{pmatrix} 6 \\ -9 \end{pmatrix} = 3\,\overrightarrow{PQ}$. "
               "The vectors are parallel and share the point P, so P, Q and R are collinear."),
            PQ("Are the points $D(0, 0)$, $E(2, 3)$ and $F(5, 7)$ collinear? Give a reason.",
               r"$\overrightarrow{DE} = \begin{pmatrix} 2 \\ 3 \end{pmatrix}$ and $\overrightarrow{DF} = \begin{pmatrix} 5 \\ 7 \end{pmatrix}$. "
               r"For the top numbers the multiplier would be $5 \div 2 = 2.5$, but $3 \times 2.5 = 7.5 \neq 7$. "
               "So DF is not a multiple of DE and the points are not collinear."),
            PQ(r"$\overrightarrow{OA} = \begin{pmatrix} -2 \\ 3 \end{pmatrix}$ and $\overrightarrow{OB} = \begin{pmatrix} 0 \\ 4 \end{pmatrix}$. "
               r"$C$ is the point $(6, k)$ and $A$, $B$, $C$ are collinear. Find $k$ and the position vector of the midpoint of $AC$.",
               r"$\overrightarrow{AB} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ and $\overrightarrow{AC} = \begin{pmatrix} 8 \\ k - 3 \end{pmatrix} = 4\,\overrightarrow{AB}$, "
               r"so $k - 3 = 4$ and $k = 7$. Midpoint: $\tfrac{1}{2}\begin{pmatrix} -2 + 6 \\ 3 + 7 \end{pmatrix} = \begin{pmatrix} 2 \\ 5 \end{pmatrix}$."),
            SUM(r"The position vector of $A$ is $\overrightarrow{OA}$; $\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA}$ (end minus start).",
                r"Midpoint of $AB$: $\overrightarrow{OM} = \tfrac{1}{2}(\overrightarrow{OA} + \overrightarrow{OB})$.",
                r"Vectors are parallel when one is a number times the other.",
                r"Collinear: show $\overrightarrow{AC} = k\,\overrightarrow{AB}$ and state the common point $A$."),
        ],
    ),
]
