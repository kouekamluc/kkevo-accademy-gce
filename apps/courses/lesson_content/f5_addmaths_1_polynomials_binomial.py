"""Form 5 Additional Mathematics: Polynomials and Binomial expansion (6 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("additional-mathematics", "form-5")

MODULE = "Pure Mathematics"
POLY = "Polynomials"
BINOM = "Binomial expansion"

LESSONS = []

# ------------------------------------------------------------------ Polynomials
LESSONS.append(lesson(
    module=MODULE,
    topic=POLY,
    title="Polynomials and algebraic division",
    slug="polynomials-and-algebraic-division",
    minutes=22,
    summary="Name the degree and coefficients of a polynomial, and divide a polynomial by (x − a) using long division or the shorter synthetic method to find the quotient and the remainder.",
    objectives=[
        "State the degree, leading coefficient and constant term of a polynomial",
        "Divide a polynomial by $(x - a)$ using long division",
        "Use synthetic division as a short way to divide by $(x - a)$",
        "Write the result in the form $f(x) = (x - a)Q(x) + R$",
    ],
    key_concepts=["Polynomial", "Degree", "Quotient", "Remainder", "Division identity", "Synthetic division"],
    blocks=[
        H("Introduction"),
        T("You already know how to divide numbers. When a farmer in Bafoussam shares 31 bags of maize equally "
          "between 4 buyers, each gets 7 bags and 3 are left over: $31 = 4 \\times 7 + 3$. "
          "Here 7 is the **quotient** and 3 is the **remainder**."),
        T("Polynomials can be divided in the same way. This skill is the base of the whole topic: the remainder "
          "theorem, the factor theorem and partial fractions in the next lessons all build on it. "
          "You will use your General Mathematics skills of expanding brackets and collecting like terms."),
        D(r"A **polynomial** in $x$ is a sum of terms $a x^n$ where each power $n$ is a whole number (0, 1, 2, ...). "
          r"The highest power is the **degree**. The number in front of the highest power is the **leading coefficient**, "
          r"and the term without $x$ is the **constant term**.",
          title="Definition: polynomial and degree", formula=r"f(x) = 2x^3 + 3x^2 - x + 5",
          note=r"This $f(x)$ has degree 3 (a cubic), leading coefficient 2 and constant term 5. "
               r"Expressions such as $\frac{1}{x}$ or $\sqrt{x}$ are not polynomials."),
        KEY("Names by degree", "A polynomial is named by its degree.", cards=[
            ["Degree 1", "Linear, e.g. $3x - 2$"],
            ["Degree 2", "Quadratic, e.g. $x^2 + 5x + 6$"],
            ["Degree 3", "Cubic, e.g. $x^3 - 7x + 6$"],
            ["Degree 4", "Quartic, e.g. $x^4 - 3x^2 + 1$"],
        ]),
        D(r"When $f(x)$ is divided by $(x - a)$, we get a quotient $Q(x)$ and a remainder $R$ (a number):",
          title="The division identity", formula=r"f(x) = (x - a)\,Q(x) + R",
          note=r"If $f(x)$ has degree $n$, the quotient $Q(x)$ has degree $n - 1$."),
        H("Long division"),
        EX("Worked example 1: long division",
           intro=r"Divide $2x^3 + 3x^2 - x + 5$ by $(x - 2)$. Use the same steps as long division of numbers: "
                 r"divide the leading terms, multiply back, subtract, bring down the next term, and repeat.", steps=[
            S(r"Divide the leading terms: $2x^3 \div x$", math=r"2x^2",
              text=r"Multiply back: $2x^2(x - 2) = 2x^3 - 4x^2$. Subtract from $2x^3 + 3x^2$ to get $7x^2$. Bring down $-x$."),
            S(r"Divide: $7x^2 \div x$", math=r"7x",
              text=r"Multiply back: $7x(x - 2) = 7x^2 - 14x$. Subtract from $7x^2 - x$ to get $13x$. Bring down $+5$."),
            S(r"Divide: $13x \div x$", math=r"13",
              text=r"Multiply back: $13(x - 2) = 13x - 26$. Subtract from $13x + 5$ to get $31$."),
            S("Write the result", math=r"2x^3 + 3x^2 - x + 5 = (x - 2)(2x^2 + 7x + 13) + 31",
              text=r"Quotient $2x^2 + 7x + 13$, remainder 31."),
        ], check=r"(x - 2)(2x^2 + 7x + 13) = 2x^3 + 3x^2 - x - 26, \text{ and } -26 + 31 = 5"),
        CODE("""
            2x^2 +  7x  + 13
         ________________________
 x - 2 | 2x^3 + 3x^2 -  x  +  5
         2x^3 - 4x^2
         -----------
                7x^2 -  x
                7x^2 - 14x
                ----------
                       13x +  5
                       13x - 26
                       --------
                             31
""", "text", title="Layout of worked example 1"),
        EX("Worked example 2: a missing term",
           intro=r"Divide $x^3 - 7x + 6$ by $(x + 3)$.", steps=[
            S("Put in a zero term for the missing power", math=r"x^3 + 0x^2 - 7x + 6",
              text="Without this, the columns get mixed up."),
            S(r"$x^3 \div x = x^2$", text=r"$x^2(x + 3) = x^3 + 3x^2$. Subtract: $0x^2 - 3x^2 = -3x^2$. Bring down $-7x$."),
            S(r"$-3x^2 \div x = -3x$", text=r"$-3x(x + 3) = -3x^2 - 9x$. Subtract: $-7x - (-9x) = 2x$. Bring down $+6$."),
            S(r"$2x \div x = 2$", text=r"$2(x + 3) = 2x + 6$. Subtract: remainder 0."),
            S("Write the result", math=r"x^3 - 7x + 6 = (x + 3)(x^2 - 3x + 2)",
              text="The remainder is 0, so $(x + 3)$ divides exactly."),
        ]),
        QUIZ(r"A polynomial of degree 4 is divided by $(x - 1)$. What is the degree of the quotient?",
             ["4", "3", "5", "1"], 1,
             r"Dividing by a linear factor lowers the degree by one: $4 - 1 = 3$.",
             hint="What do you get when you divide the leading term $ax^4$ by $x$?",
             feedback=[r"Dividing by $x$ lowers the power: $x^4 \div x = x^3$.", "",
                       "Division never raises the degree.", "That is the degree of the divisor $(x - 1)$, not of the quotient."]),
        H("Synthetic division: a short method"),
        T(r"To divide by $(x - a)$, you can work with the coefficients only. Write $a$ on the left and the coefficients "
          r"in a row (with 0 for any missing power). Bring down the first coefficient. Then repeat: multiply by $a$, "
          r"write the result under the next coefficient, and add."),
        EX("Worked example 3: synthetic division",
           intro=r"Divide $x^3 - 4x^2 + x + 5$ by $(x - 3)$.", steps=[
            S(r"Use $a = 3$ (because the divisor is $x - 3$) and the coefficients", math=r"1,\; -4,\; 1,\; 5"),
            S("Bring down the 1", text=r"Multiply: $1 \times 3 = 3$. Add to $-4$: $-1$."),
            S("Repeat", text=r"$-1 \times 3 = -3$. Add to $1$: $-2$. Then $-2 \times 3 = -6$. Add to $5$: $-1$."),
            S("Read off the answer", math=r"x^3 - 4x^2 + x + 5 = (x - 3)(x^2 - x - 2) - 1",
              text=r"The last number, $-1$, is the remainder. The others, $1, -1, -2$, are the coefficients of the quotient $x^2 - x - 2$."),
        ]),
        CODE("""
  3 |  1   -4    1    5
    |       3   -3   -6
    -------------------
       1   -1   -2 | -1
""", "text", title="Layout of worked example 3"),
        TIP(r"For a divisor $(x + 3)$, use $a = -3$, because $x + 3 = x - (-3)$."),
        H("Common mistakes"),
        MISTAKE("Leaving out a missing power",
                r"In $x^3 - 7x + 6$ there is no $x^2$ term. Write $x^3 + 0x^2 - 7x + 6$ before you divide."),
        MISTAKE("Subtracting signs wrongly",
                r"When you subtract $(7x^2 - 14x)$ from $(7x^2 - x)$, you get $-x + 14x = 13x$. Put brackets round what you subtract."),
        MISTAKE("Using the wrong sign of a in synthetic division",
                r"For $(x - 3)$ use $3$; for $(x + 3)$ use $-3$."),
        QUIZ(r"Divide $x^2 + 5x + 7$ by $(x + 2)$.",
             [r"Quotient $x + 7$, remainder $21$", r"Quotient $x + 3$, remainder $13$",
              r"Quotient $x + 3$, remainder $1$", r"Quotient $x + 2$, remainder $3$"], 2,
             r"$x(x + 2) = x^2 + 2x$, leaving $3x + 7$. Then $3(x + 2) = 3x + 6$, leaving 1. So $x^2 + 5x + 7 = (x + 2)(x + 3) + 1$.",
             hint="Divide the leading terms first, multiply back, and subtract.",
             feedback=[r"You added $2x$ instead of subtracting it. $5x - 2x = 3x$.",
                       r"You used $a = +2$ instead of $-2$ for the divisor $(x + 2)$.", "",
                       r"Check by expanding: $(x + 2)(x + 2) + 3 = x^2 + 4x + 7$, not $x^2 + 5x + 7$."]),
        H("Practice questions"),
        PQ(r"Find the quotient and remainder when $3x^3 - 2x^2 + 4$ is divided by $(x - 1)$.",
           r"Coefficients $3, -2, 0, 4$ with $a = 1$. Bring down 3; $3 + (-2) = 1$; $1 + 0 = 1$; $1 + 4 = 5$. "
           r"Quotient $3x^2 + x + 1$, remainder 5. So $3x^3 - 2x^2 + 4 = (x - 1)(3x^2 + x + 1) + 5$."),
        PQ(r"Show that $(x + 2)$ divides $x^3 + 8$ exactly, and state the quotient.",
           r"Coefficients $1, 0, 0, 8$ with $a = -2$. Bring down 1; $-2$; then $4$; then $8 - 8 = 0$. "
           r"The remainder is 0, so $(x + 2)$ divides exactly, and the quotient is $x^2 - 2x + 4$."),
        PQ(r"Divide $2x^3 + x^2 - 13x + 6$ by $(x - 2)$.",
           r"Coefficients $2, 1, -13, 6$ with $a = 2$: bring down 2; $1 + 4 = 5$; $-13 + 10 = -3$; $6 - 6 = 0$. "
           r"So $2x^3 + x^2 - 13x + 6 = (x - 2)(2x^2 + 5x - 3)$, remainder 0."),
        H("Summary"),
        SUM("The degree of a polynomial is its highest power of $x$.",
            r"Division by $(x - a)$ gives $f(x) = (x - a)Q(x) + R$, where $Q(x)$ has degree one less than $f(x)$.",
            "Long division: divide the leading terms, multiply back, subtract, bring down, repeat.",
            "Write a 0 coefficient for every missing power before dividing.",
            r"Synthetic division uses $a$ and the coefficients only; the last number is the remainder."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=POLY,
    title="The remainder theorem",
    slug="the-remainder-theorem",
    minutes=22,
    summary="Use the remainder theorem to find the remainder on dividing a polynomial by (x − a) or (ax − b) without long division, and use given remainders to find unknown coefficients.",
    objectives=[
        r"State and explain the remainder theorem",
        r"Find the remainder when $f(x)$ is divided by $(x - a)$ by working out $f(a)$",
        r"Find the remainder when $f(x)$ is divided by $(ax - b)$",
        "Form and solve equations to find unknown coefficients from given remainders",
    ],
    key_concepts=["Remainder theorem", "Divisor (ax − b)", "Unknown coefficients", "Simultaneous equations"],
    blocks=[
        H("Introduction"),
        T(r"In the last lesson you found the remainder of $2x^3 + 3x^2 - x + 5$ divided by $(x - 2)$ using long division. "
          r"It took several lines and the answer was 31."),
        T(r"Now try this: put $x = 2$ into the polynomial. $2(8) + 3(4) - 2 + 5 = 31$. The same number! "
          "This is no accident. It is the **remainder theorem**, and it saves a lot of time in the examination."),
        D(r"When a polynomial $f(x)$ is divided by $(x - a)$, the remainder is $f(a)$.",
          title="The remainder theorem", formula=r"\text{remainder} = f(a)",
          note=r"Reason: $f(x) = (x - a)Q(x) + R$. Put $x = a$: $f(a) = 0 \times Q(a) + R = R$."),
        D(r"When $f(x)$ is divided by $(ax - b)$, the remainder is $f\left(\frac{b}{a}\right)$, because $ax - b = 0$ when $x = \frac{b}{a}$.",
          title="Dividing by (ax − b)", formula=r"\text{remainder} = f\left(\tfrac{b}{a}\right)"),
        TIP("To find the value to substitute, set the divisor equal to zero and solve. For $(x + 2)$, $x = -2$. For $(2x - 1)$, $x = \\frac{1}{2}$."),
        H("Worked examples"),
        EX("Worked example 1: a simple remainder",
           intro=r"Find the remainder when $f(x) = x^3 - 3x^2 + 4x - 5$ is divided by $(x + 2)$.", steps=[
            S("Set the divisor to zero", math=r"x + 2 = 0 \Rightarrow x = -2"),
            S("Substitute into $f(x)$", math=r"f(-2) = (-2)^3 - 3(-2)^2 + 4(-2) - 5"),
            S("Work out each term carefully", math=r"= -8 - 12 - 8 - 5"),
            S("State the remainder", math=r"f(-2) = -33", text="The remainder is $-33$."),
        ]),
        EX("Worked example 2: dividing by (2x − 1)",
           intro=r"Find the remainder when $f(x) = 4x^3 - 2x^2 + 6x - 1$ is divided by $(2x - 1)$.", steps=[
            S("Set the divisor to zero", math=r"2x - 1 = 0 \Rightarrow x = \tfrac{1}{2}"),
            S("Substitute", math=r"f\left(\tfrac{1}{2}\right) = 4\left(\tfrac{1}{8}\right) - 2\left(\tfrac{1}{4}\right) + 6\left(\tfrac{1}{2}\right) - 1"),
            S("Simplify", math=r"= \tfrac{1}{2} - \tfrac{1}{2} + 3 - 1 = 2", text="The remainder is 2."),
        ]),
        QUIZ(r"What is the remainder when $x^3 + 2x - 1$ is divided by $(x + 1)$?",
             ["$2$", "$-4$", "$0$", "$-2$"], 1,
             r"Use $x = -1$: $(-1)^3 + 2(-1) - 1 = -1 - 2 - 1 = -4$.",
             hint=r"Which value of $x$ makes $x + 1 = 0$?",
             feedback=[r"That is $f(1)$. For $(x + 1)$ you must substitute $x = -1$.", "",
                       r"A remainder of 0 would mean $(x + 1)$ divides exactly. Work out $f(-1)$.",
                       r"Check the cube: $(-1)^3 = -1$, so the total is $-1 - 2 - 1 = -4$."]),
        H("Finding unknown coefficients"),
        T("If you are told the remainder, substitute and you get an equation. One unknown needs one remainder; "
          "two unknowns need two remainders, giving simultaneous equations (a General Mathematics skill)."),
        EX("Worked example 3: one unknown",
           intro=r"When $2x^3 + ax^2 - 4x + 3$ is divided by $(x - 1)$, the remainder is 5. Find $a$.", steps=[
            S("Remainder theorem: $f(1) = 5$", math=r"2 + a - 4 + 3 = 5"),
            S("Simplify", math=r"a + 1 = 5"),
            S("Solve", math=r"a = 4"),
        ], check=r"f(1) = 2 + 4 - 4 + 3 = 5"),
        EX("Worked example 4: two unknowns",
           intro=r"$f(x) = x^3 + px^2 + qx + 2$. The remainder on dividing by $(x - 1)$ is 6, and on dividing by $(x + 1)$ is 2. Find $p$ and $q$.", steps=[
            S("$f(1) = 6$", math=r"1 + p + q + 2 = 6 \Rightarrow p + q = 3"),
            S("$f(-1) = 2$", math=r"-1 + p - q + 2 = 2 \Rightarrow p - q = 1"),
            S("Add the two equations", math=r"2p = 4 \Rightarrow p = 2"),
            S("Substitute back", math=r"q = 3 - 2 = 1"),
        ], check=r"f(x) = x^3 + 2x^2 + x + 2:\ f(1) = 6,\ f(-1) = -1 + 2 - 1 + 2 = 2"),
        H("Common mistakes"),
        MISTAKE("Using the wrong sign", r"For the divisor $(x + 3)$ substitute $x = -3$, not $x = 3$."),
        MISTAKE("Substituting b instead of b/a",
                r"The remainder on dividing by $(2x - 1)$ is $f\left(\tfrac{1}{2}\right)$, not $f(1)$ or $f(2)$."),
        MISTAKE("Sign errors with negative powers",
                r"$(-2)^2 = 4$ but $(-2)^3 = -8$, and $-3(-2)^2 = -12$. Work out the power first, then multiply."),
        QUIZ(r"The remainder when $f(x)$ is divided by $(3x + 2)$ is",
             [r"$f(2)$", r"$f(-2)$", r"$f\left(\tfrac{2}{3}\right)$", r"$f\left(-\tfrac{2}{3}\right)$"], 3,
             r"$3x + 2 = 0$ gives $x = -\frac{2}{3}$, so the remainder is $f\left(-\frac{2}{3}\right)$.",
             hint="Set the divisor equal to zero and solve for $x$.",
             feedback=[r"You used the number in the bracket with the wrong sign and forgot to divide by 3.",
                       r"You forgot to divide by 3: $3x = -2$ gives $x = -\frac{2}{3}$.",
                       r"The sign is wrong: $3x + 2 = 0$ gives a negative value of $x$.", ""]),
        H("Practice questions"),
        PQ(r"Find the remainder when $2x^3 - x^2 + 4$ is divided by $(2x + 1)$.",
           r"$2x + 1 = 0$ gives $x = -\tfrac{1}{2}$. "
           r"$f\left(-\tfrac{1}{2}\right) = 2\left(-\tfrac{1}{8}\right) - \tfrac{1}{4} + 4 = -\tfrac{1}{4} - \tfrac{1}{4} + 4 = \tfrac{7}{2}$. "
           r"The remainder is $\tfrac{7}{2}$."),
        PQ(r"$f(x) = x^3 + ax^2 + bx - 3$. When $f(x)$ is divided by $(x - 1)$ the remainder is $-5$, and when divided by $(x + 2)$ the remainder is 7. Find $a$ and $b$.",
           r"$f(1) = 1 + a + b - 3 = -5$, so $a + b = -3$. "
           r"$f(-2) = -8 + 4a - 2b - 3 = 7$, so $4a - 2b = 18$, that is $2a - b = 9$. "
           r"Add: $3a = 6$, so $a = 2$ and $b = -5$. Check: $f(-2) = -8 + 8 + 10 - 3 = 7$."),
        PQ(r"When $x^3 + kx^2 - 2$ is divided by $(x - 1)$ and by $(x + 2)$, the remainders are equal. Find $k$ and the remainder.",
           r"$f(1) = 1 + k - 2 = k - 1$. $f(-2) = -8 + 4k - 2 = 4k - 10$. "
           r"Equal: $k - 1 = 4k - 10$, so $3k = 9$ and $k = 3$. The remainder is $3 - 1 = 2$."),
        PQ(r"Find the remainder when $x^4 - 3x^2 + 2x + 1$ is divided by $(x - 2)$.",
           r"$f(2) = 16 - 12 + 4 + 1 = 9$. The remainder is 9."),
        H("Summary"),
        SUM(r"Remainder theorem: dividing $f(x)$ by $(x - a)$ leaves remainder $f(a)$.",
            r"For a divisor $(ax - b)$, the remainder is $f\left(\tfrac{b}{a}\right)$.",
            "Find the value to substitute by setting the divisor equal to zero.",
            "A given remainder gives an equation; two remainders give simultaneous equations for two unknowns.",
            "Work out powers of negative numbers and fractions carefully."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=POLY,
    title="The factor theorem and solving cubic equations",
    slug="factor-theorem-and-cubic-equations",
    minutes=25,
    summary="Use the factor theorem to test for linear factors, find unknown coefficients, factorize cubic polynomials completely and solve cubic equations.",
    objectives=[
        r"State the factor theorem and use it to test whether $(x - a)$ is a factor",
        "Find one factor of a cubic by trial, then the quadratic factor",
        "Factorize a cubic polynomial completely",
        r"Solve cubic equations $f(x) = 0$",
    ],
    key_concepts=["Factor theorem", "Trial of factors", "Complete factorization", "Cubic equation", "Root"],
    blocks=[
        H("Introduction"),
        T("A carpenter in Douala makes a wooden box whose volume, in cubic decimetres, is given by a cubic expression in $x$. "
          "To find which values of $x$ give a certain volume, he must solve a **cubic equation**."),
        T("In General Mathematics you solved quadratic equations by factorizing. For cubics, the remainder theorem gives a way "
          "to find the first factor. Then the cubic becomes a linear factor times a quadratic, which you already know how to handle."),
        D(r"$(x - a)$ is a factor of $f(x)$ if and only if $f(a) = 0$.",
          title="The factor theorem", formula=r"f(a) = 0 \iff (x - a) \text{ is a factor of } f(x)",
          note=r"This is the remainder theorem with remainder 0. In the same way, $(ax - b)$ is a factor exactly when $f\left(\frac{b}{a}\right) = 0$."),
        KEY("Which values should you try?", "For a cubic with whole-number coefficients:", cards=[
            ["Leading coefficient 1", r"Try the factors of the constant term: $\pm 1, \pm 2, \pm 3, \dots$"],
            ["Leading coefficient not 1", r"Also try fractions $\pm \frac{p}{q}$, where $p$ divides the constant term and $q$ divides the leading coefficient."],
            ["Quick test", r"If the coefficients add up to 0, then $f(1) = 0$ and $(x - 1)$ is a factor."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: testing factors",
           intro=r"$f(x) = x^3 - 3x^2 - 4x + 12$. Is $(x - 2)$ a factor? Is $(x + 1)$ a factor?", steps=[
            S("Test $(x - 2)$: work out $f(2)$", math=r"f(2) = 8 - 12 - 8 + 12 = 0",
              text=r"$f(2) = 0$, so $(x - 2)$ is a factor."),
            S("Test $(x + 1)$: work out $f(-1)$", math=r"f(-1) = -1 - 3 + 4 + 12 = 12",
              text=r"$f(-1) \neq 0$, so $(x + 1)$ is not a factor. (Dividing by it leaves remainder 12.)"),
        ]),
        EX("Worked example 2: factorize completely and solve",
           intro=r"Factorize $f(x) = x^3 - 2x^2 - 5x + 6$ completely. Hence solve $f(x) = 0$.", steps=[
            S("Try $x = 1$", math=r"f(1) = 1 - 2 - 5 + 6 = 0", text=r"So $(x - 1)$ is a factor."),
            S("Divide by $(x - 1)$ (synthetic division with $a = 1$)", text=r"Coefficients $1, -2, -5, 6$ give $1, -1, -6$, remainder 0."),
            S("Write the cubic as linear times quadratic", math=r"f(x) = (x - 1)(x^2 - x - 6)"),
            S("Factorize the quadratic", math=r"f(x) = (x - 1)(x + 2)(x - 3)"),
            S("Solve $f(x) = 0$", math=r"x = 1, \quad x = -2, \quad x = 3"),
        ], check=r"f(-2) = -8 - 8 + 10 + 6 = 0,\quad f(3) = 27 - 18 - 15 + 6 = 0"),
        GRAPH([1, -2, -5, 6], alt="Cubic curve crossing the x-axis at minus 2, 1 and 3",
              caption="Figure 1. The roots of $x^3 - 2x^2 - 5x + 6 = 0$ are where the curve meets the $x$-axis.",
              xmin=-3, xmax=4, ymin=-10, ymax=10, roots=[-2, 1, 3], label="y = x³ − 2x² − 5x + 6"),
        T(r"You can also find the quadratic factor by **comparing coefficients**: write $x^3 - 2x^2 - 5x + 6 = (x - 1)(x^2 + bx - 6)$. "
          r"The $x^2$ terms give $b - 1 = -2$, so $b = -1$. Use whichever method you find safer."),
        QUIZ(r"Which of these is a factor of $x^3 - 7x + 6$?",
             [r"$(x - 3)$", r"$(x + 2)$", r"$(x + 3)$", r"$(x - 6)$"], 2,
             r"$f(-3) = -27 + 21 + 6 = 0$, so $(x + 3)$ is a factor.",
             hint=r"For each bracket, find the value of $x$ that makes it zero and work out $f$ of that value.",
             feedback=[r"$f(3) = 27 - 21 + 6 = 12 \neq 0$.", r"$f(-2) = -8 + 14 + 6 = 12 \neq 0$.", "",
                       r"$f(6) = 216 - 42 + 6 = 180 \neq 0$."]),
        H("Finding unknowns and harder cubics"),
        EX("Worked example 3: an unknown coefficient",
           intro=r"$(x - 2)$ is a factor of $f(x) = x^3 + ax^2 - x - 2$. Find $a$, then show that $f(x) = 0$ has only one real root.", steps=[
            S("A factor means $f(2) = 0$", math=r"8 + 4a - 2 - 2 = 0 \Rightarrow 4a = -4 \Rightarrow a = -1"),
            S("Divide $x^3 - x^2 - x - 2$ by $(x - 2)$", math=r"f(x) = (x - 2)(x^2 + x + 1)"),
            S("Check the quadratic factor with the discriminant", math=r"b^2 - 4ac = 1 - 4 = -3 < 0",
              text=r"$x^2 + x + 1 = 0$ has no real roots."),
            S("Conclusion", text=r"The only real root is $x = 2$."),
        ]),
        EX("Worked example 4: leading coefficient not 1", solve=r"2x^3 + x^2 - 13x + 6 = 0", steps=[
            S("Try $x = 2$", math=r"f(2) = 16 + 4 - 26 + 6 = 0", text=r"So $(x - 2)$ is a factor."),
            S("Divide (coefficients $2, 1, -13, 6$ with $a = 2$)", math=r"f(x) = (x - 2)(2x^2 + 5x - 3)"),
            S("Factorize the quadratic", math=r"2x^2 + 5x - 3 = (2x - 1)(x + 3)"),
            S("Solve", math=r"x = 2, \quad x = \tfrac{1}{2}, \quad x = -3"),
        ], check=r"f\left(\tfrac{1}{2}\right) = \tfrac{1}{4} + \tfrac{1}{4} - \tfrac{13}{2} + 6 = 0"),
        H("Common mistakes"),
        MISTAKE("Stopping after one factor", "When asked to factorize completely, also factorize the quadratic factor if you can."),
        MISTAKE("Giving factors when roots are asked",
                r"The factor $(x + 2)$ gives the root $x = -2$. Read the question: factorize, or solve?"),
        MISTAKE("Forgetting fractional roots",
                r"A factor $(2x - 1)$ gives the root $x = \frac{1}{2}$, not $x = 1$ or $x = 2$."),
        QUIZ(r"$x^3 - 2x^2 + x - 2 = (x - 2)(x^2 + 1)$. How many real roots does $x^3 - 2x^2 + x - 2 = 0$ have?",
             ["Three", "Two", "One", "None"], 2,
             r"$x - 2 = 0$ gives $x = 2$. But $x^2 + 1 = 0$ has no real roots, since $x^2 = -1$ is impossible. So there is one real root.",
             hint=r"Solve each factor equal to zero. Can $x^2 + 1$ ever be zero?",
             feedback=[r"A cubic has at most three roots, but $x^2 + 1 = 0$ has none.",
                       r"$x^2 + 1 = 0$ does not give $x = \pm 1$: that would need $x^2 = 1$.", "",
                       r"$x = 2$ is a root: $8 - 8 + 2 - 2 = 0$."]),
        H("Practice questions"),
        PQ(r"Solve $x^3 - 6x^2 + 11x - 6 = 0$.",
           r"The coefficients add to 0, so $f(1) = 0$ and $(x - 1)$ is a factor. Dividing gives $x^2 - 5x + 6 = (x - 2)(x - 3)$. "
           r"So $(x - 1)(x - 2)(x - 3) = 0$ and $x = 1, 2$ or $3$."),
        PQ(r"$f(x) = x^3 + px^2 + qx + 6$. $(x - 1)$ and $(x - 2)$ are factors of $f(x)$. Find $p$ and $q$, then find the third factor.",
           r"$f(1) = 0$: $1 + p + q + 6 = 0$, so $p + q = -7$. "
           r"$f(2) = 0$: $8 + 4p + 2q + 6 = 0$, so $2p + q = -7$. "
           r"Subtract: $p = 0$, then $q = -7$. So $f(x) = x^3 - 7x + 6$. "
           r"The third factor is $(x + c)$ with $(-1)(-2)c = 6$, so $c = 3$: the factor is $(x + 3)$. Check: $f(-3) = -27 + 21 + 6 = 0$."),
        PQ(r"Show that $(x - 3)$ is a factor of $2x^3 - 3x^2 - 11x + 6$, and hence solve $2x^3 - 3x^2 - 11x + 6 = 0$.",
           r"$f(3) = 54 - 27 - 33 + 6 = 0$, so $(x - 3)$ is a factor. Dividing gives $2x^2 + 3x - 2 = (2x - 1)(x + 2)$. "
           r"So $x = 3$, $x = \frac{1}{2}$ or $x = -2$."),
        PQ(r"Factorize $x^3 + 3x^2 - x - 3$ completely.",
           r"$f(1) = 1 + 3 - 1 - 3 = 0$, so $(x - 1)$ is a factor. Dividing gives $x^2 + 4x + 3 = (x + 1)(x + 3)$. "
           r"So $x^3 + 3x^2 - x - 3 = (x - 1)(x + 1)(x + 3)$."),
        H("Summary"),
        SUM(r"Factor theorem: $(x - a)$ is a factor of $f(x)$ exactly when $f(a) = 0$.",
            "Try factors of the constant term first; if the coefficients add to 0, $(x - 1)$ is a factor.",
            "Divide (or compare coefficients) to get the quadratic factor, then factorize it.",
            "Each linear factor gives one root of $f(x) = 0$.",
            "If the quadratic factor has a negative discriminant, the cubic has only one real root."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=POLY,
    title="Partial fractions",
    slug="partial-fractions-with-linear-factors",
    minutes=25,
    summary="Split an algebraic fraction into partial fractions when the denominator has distinct linear factors or a repeated linear factor, dividing first when the fraction is improper.",
    objectives=[
        "Write the correct form of partial fractions for distinct and repeated linear factors",
        "Find the unknown constants by substituting values and comparing coefficients",
        "Divide first when the fraction is improper",
        "Check a partial fraction answer by recombining",
    ],
    key_concepts=["Partial fractions", "Proper and improper fractions", "Distinct linear factors", "Repeated linear factor"],
    blocks=[
        H("Introduction"),
        T(r"In General Mathematics you added algebraic fractions: $\frac{2}{x - 1} + \frac{3}{x + 2} = \frac{5x + 1}{(x - 1)(x + 2)}$. "
          "**Partial fractions** do the reverse. They split one complicated fraction into a sum of simple ones."),
        T("Simple fractions are much easier to work with, and you will meet partial fractions again "
          "in calculus at A Level. In this lesson the denominators always factorize into linear factors."),
        D(r"A fraction $\frac{P(x)}{Q(x)}$ is **proper** if the degree of $P$ is less than the degree of $Q$, and **improper** otherwise.",
          title="Proper and improper fractions",
          note=r"$\frac{5x + 1}{x^2 + x - 2}$ is proper (degree 1 over degree 2). $\frac{2x^2 + 5x - 4}{x^2 + x - 2}$ is improper (degree 2 over degree 2)."),
        KEY("The forms to use", "First factorize the denominator. Then write one of these forms (for a proper fraction):", cards=[
            ["Distinct linear factors", r"$\frac{px + q}{(x - a)(x - b)} = \frac{A}{x - a} + \frac{B}{x - b}$"],
            ["Repeated linear factor", r"$\frac{\dots}{(x - a)(x - b)^2} = \frac{A}{x - a} + \frac{B}{x - b} + \frac{C}{(x - b)^2}$"],
            ["Improper fraction", "Divide first: whole part + proper fraction, then split the proper fraction."],
        ]),
        H("Distinct linear factors"),
        EX("Worked example 1: two distinct factors",
           intro=r"Express $\dfrac{5x + 1}{(x - 1)(x + 2)}$ in partial fractions.", steps=[
            S("Write the form", math=r"\frac{5x + 1}{(x - 1)(x + 2)} = \frac{A}{x - 1} + \frac{B}{x + 2}"),
            S("Multiply both sides by $(x - 1)(x + 2)$", math=r"5x + 1 = A(x + 2) + B(x - 1)"),
            S("Put $x = 1$ (this removes $B$)", math=r"6 = 3A \Rightarrow A = 2"),
            S("Put $x = -2$ (this removes $A$)", math=r"-9 = -3B \Rightarrow B = 3"),
            S("Write the answer", math=r"\frac{5x + 1}{(x - 1)(x + 2)} = \frac{2}{x - 1} + \frac{3}{x + 2}"),
        ], check=r"2(x + 2) + 3(x - 1) = 5x + 1"),
        QUIZ(r"In $\dfrac{7}{(x - 3)(x + 4)} = \dfrac{A}{x - 3} + \dfrac{B}{x + 4}$, what is $A$?",
             [r"$-1$", r"$7$", r"$\tfrac{1}{7}$", r"$1$"], 3,
             r"$7 = A(x + 4) + B(x - 3)$. Put $x = 3$: $7 = 7A$, so $A = 1$ (and $B = -1$).",
             hint=r"Multiply through, then choose the value of $x$ that makes the $B$ term vanish.",
             feedback=[r"$-1$ is the value of $B$. Put $x = 3$ to find $A$.",
                       r"7 is the numerator. You still need to divide by $(3 + 4)$.",
                       r"With $x = 3$ you get $7 = 7A$, so $A = 1$, not $\tfrac{1}{7}$.", ""]),
        H("A repeated linear factor"),
        T(r"If a factor such as $(x + 1)$ appears squared, you need **two** fractions for it: one over $(x + 1)$ and one over $(x + 1)^2$. "
          r"Substitution finds two of the constants; compare the coefficients of $x^2$ to find the last one."),
        EX("Worked example 2: a repeated factor",
           intro=r"Express $\dfrac{5x - 1}{(x - 2)(x + 1)^2}$ in partial fractions.", steps=[
            S("Write the form", math=r"\frac{5x - 1}{(x - 2)(x + 1)^2} = \frac{A}{x - 2} + \frac{B}{x + 1} + \frac{C}{(x + 1)^2}"),
            S("Multiply by $(x - 2)(x + 1)^2$", math=r"5x - 1 = A(x + 1)^2 + B(x - 2)(x + 1) + C(x - 2)"),
            S("Put $x = 2$", math=r"9 = 9A \Rightarrow A = 1"),
            S("Put $x = -1$", math=r"-6 = -3C \Rightarrow C = 2"),
            S("Compare coefficients of $x^2$", math=r"0 = A + B \Rightarrow B = -1",
              text=r"The left side has no $x^2$ term. On the right, $x^2$ comes from $A(x + 1)^2$ and $B(x - 2)(x + 1)$."),
            S("Write the answer", math=r"\frac{1}{x - 2} - \frac{1}{x + 1} + \frac{2}{(x + 1)^2}"),
        ], check=r"x = 0:\ \frac{-1}{(-2)(1)} = \frac{1}{2} \text{ and } -\frac{1}{2} - 1 + 2 = \frac{1}{2}"),
        H("Improper fractions: divide first"),
        EX("Worked example 3: an improper fraction",
           intro=r"Express $\dfrac{2x^2 + 5x - 4}{(x - 1)(x + 2)}$ in partial fractions.", steps=[
            S("The fraction is improper, so divide", math=r"(x - 1)(x + 2) = x^2 + x - 2",
              text=r"$2x^2 + 5x - 4 = 2(x^2 + x - 2) + 3x$. The whole part is 2 and the remainder is $3x$."),
            S("Write as whole part plus proper fraction", math=r"\frac{2x^2 + 5x - 4}{(x - 1)(x + 2)} = 2 + \frac{3x}{(x - 1)(x + 2)}"),
            S("Split the proper fraction", math=r"3x = A(x + 2) + B(x - 1)"),
            S("Put $x = 1$ and $x = -2$", math=r"3 = 3A \Rightarrow A = 1, \qquad -6 = -3B \Rightarrow B = 2"),
            S("Write the answer", math=r"2 + \frac{1}{x - 1} + \frac{2}{x + 2}"),
        ]),
        TIP(r"Always check by substituting a convenient value such as $x = 0$ into both the question and your answer."),
        H("Common mistakes"),
        MISTAKE("Splitting an improper fraction without dividing",
                "If the top has the same or higher degree than the bottom, divide first. Otherwise no values of A and B will work."),
        MISTAKE("Missing a term for the repeated factor",
                r"$(x + 1)^2$ needs both $\frac{B}{x + 1}$ and $\frac{C}{(x + 1)^2}$."),
        MISTAKE("Not factorizing the denominator first",
                r"For $\frac{x + 7}{x^2 - x - 2}$, first write $x^2 - x - 2 = (x + 1)(x - 2)$."),
        QUIZ(r"Which is the correct form for $\dfrac{x + 4}{(x - 1)(x + 3)^2}$?",
             [r"$\frac{A}{x - 1} + \frac{B}{x + 3} + \frac{C}{(x + 3)^2}$", r"$\frac{A}{x - 1} + \frac{B}{(x + 3)^2}$",
              r"$\frac{A}{x - 1} + \frac{B}{x + 3}$", r"$\frac{A}{x - 1} + \frac{Bx + C}{x + 3}$"], 0,
             r"A repeated factor $(x + 3)^2$ needs a fraction over $(x + 3)$ and one over $(x + 3)^2$.",
             hint="Count the factors in the denominator, including the repeated one twice.",
             feedback=["", r"You left out $\frac{B}{x + 3}$. The repeated factor needs both powers.",
                       r"This ignores the square on $(x + 3)$.",
                       r"Over a linear factor the top is a constant, and the square on $(x + 3)$ is lost."]),
        H("Practice questions"),
        PQ(r"Express $\dfrac{x + 7}{x^2 - x - 2}$ in partial fractions.",
           r"$x^2 - x - 2 = (x + 1)(x - 2)$. Then $x + 7 = A(x - 2) + B(x + 1)$. Put $x = 2$: $9 = 3B$, $B = 3$. Put $x = -1$: $6 = -3A$, $A = -2$. "
           r"Answer: $\dfrac{3}{x - 2} - \dfrac{2}{x + 1}$. Check: $3(x + 1) - 2(x - 2) = x + 7$."),
        PQ(r"Express $\dfrac{3x + 1}{(x + 1)(x - 1)}$ in partial fractions.",
           r"$3x + 1 = A(x - 1) + B(x + 1)$. Put $x = 1$: $4 = 2B$, so $B = 2$. Put $x = -1$: $-2 = -2A$, so $A = 1$. "
           r"Answer: $\dfrac{1}{x + 1} + \dfrac{2}{x - 1}$."),
        PQ(r"Express $\dfrac{4}{(x - 1)(x + 1)^2}$ in partial fractions.",
           r"$4 = A(x + 1)^2 + B(x - 1)(x + 1) + C(x - 1)$. Put $x = 1$: $4 = 4A$, $A = 1$. Put $x = -1$: $4 = -2C$, $C = -2$. "
           r"$x^2$ terms: $0 = A + B$, so $B = -1$. Answer: $\dfrac{1}{x - 1} - \dfrac{1}{x + 1} - \dfrac{2}{(x + 1)^2}$."),
        PQ(r"Express $\dfrac{x^2 + 1}{x^2 - 1}$ in partial fractions.",
           r"Improper, so divide: $x^2 + 1 = (x^2 - 1) + 2$, giving $1 + \dfrac{2}{(x - 1)(x + 1)}$. "
           r"$2 = A(x + 1) + B(x - 1)$: $x = 1$ gives $A = 1$, $x = -1$ gives $B = -1$. Answer: $1 + \dfrac{1}{x - 1} - \dfrac{1}{x + 1}$."),
        H("Summary"),
        SUM("Factorize the denominator first.",
            r"Distinct linear factors: $\frac{A}{x - a} + \frac{B}{x - b}$.",
            r"A repeated factor $(x - b)^2$ needs $\frac{B}{x - b} + \frac{C}{(x - b)^2}$.",
            "Multiply through, substitute the values that make each factor zero, and compare coefficients for any constant left.",
            "If the fraction is improper, divide first to get a whole part plus a proper fraction.",
            "Check your answer by substituting a value such as x = 0."),
    ],
))

# ------------------------------------------------------------------ Binomial expansion
LESSONS.append(lesson(
    module=MODULE,
    topic=BINOM,
    title="Pascal's triangle and expanding (a + b)ⁿ",
    slug="pascals-triangle-and-binomial-expansion",
    minutes=22,
    summary="Build Pascal's triangle and use it to expand (a + b)ⁿ for a positive whole number n, including expansions with a minus sign and the first terms of (1 + kx)ⁿ.",
    objectives=[
        "Build Pascal's triangle and read off the coefficients for $(a + b)^n$",
        "Expand $(a + b)^n$ fully for a positive whole number $n$",
        "Handle signs correctly when expanding $(a - b)^n$",
        "Write the first few terms of $(1 + kx)^n$ in ascending powers of $x$",
    ],
    key_concepts=["Binomial", "Pascal's triangle", "Binomial coefficients", "Ascending powers"],
    blocks=[
        H("Introduction"),
        T(r"A **binomial** is an expression with two terms, such as $(2 + x)$ or $(a - b)$. In General Mathematics you expanded "
          r"$(a + b)^2 = a^2 + 2ab + b^2$. But multiplying out $(2 + x)^5$ bracket by bracket is slow and easy to get wrong."),
        T("Look at the first few expansions and you will see a clear pattern. Once you know it, you can write any expansion straight down."),
        F(r"(a + b)^1 = a + b \qquad (a + b)^2 = a^2 + 2ab + b^2 \qquad (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3", title="The first expansions"),
        IMG("f5a-pascals-triangle.svg", alt="Pascal's triangle with rows n = 0 to n = 6. The numbers 4 and 6 in row 4 add to give 10 in row 5.",
            caption="Figure 1. Pascal's triangle: each number is the sum of the two numbers above it."),
        D(r"Row $n$ of Pascal's triangle gives the coefficients of $(a + b)^n$. Each row starts and ends with 1, and every other number "
          r"is the sum of the two numbers just above it.",
          title="Pascal's triangle", formula=r"n = 5:\quad 1 \quad 5 \quad 10 \quad 10 \quad 5 \quad 1"),
        KEY("Patterns in the expansion of (a + b)ⁿ", "Use these three facts every time.", cards=[
            ["Number of terms", r"There are $n + 1$ terms."],
            ["Powers", r"The power of $a$ goes down from $n$ to 0, and the power of $b$ goes up from 0 to $n$."],
            ["Check", r"In every term the two powers add up to $n$."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: a full expansion", intro=r"Expand $(2 + x)^4$.", steps=[
            S("Coefficients from row 4", text="1, 4, 6, 4, 1"),
            S("Write each term with the powers", math=r"1(2^4) + 4(2^3)x + 6(2^2)x^2 + 4(2)x^3 + 1x^4"),
            S("Simplify each term", math=r"(2 + x)^4 = 16 + 32x + 24x^2 + 8x^3 + x^4"),
        ], check=r"x = 1:\ 16 + 32 + 24 + 8 + 1 = 81 = 3^4"),
        EX("Worked example 2: a minus sign", intro=r"Expand $(3 - 2x)^4$.", steps=[
            S(r"Treat it as $(a + b)^4$ with $a = 3$ and $b = -2x$", text="Coefficients from row 4: 1, 4, 6, 4, 1."),
            S("Write the terms with brackets round b", math=r"3^4 + 4(3^3)(-2x) + 6(3^2)(-2x)^2 + 4(3)(-2x)^3 + (-2x)^4"),
            S("Work out each term", math=r"81 - 216x + 216x^2 - 96x^3 + 16x^4"),
        ], check=r"x = 1:\ 81 - 216 + 216 - 96 + 16 = 1 = (3 - 2)^4"),
        TIP("With a minus sign, the signs of the terms alternate: +, −, +, −, ... Odd powers of a negative number are negative."),
        QUIZ(r"What is the coefficient of $x^2$ in $(1 + x)^5$?", ["$5$", "$10$", "$20$", "$25$"], 1,
             r"Row 5 is 1, 5, 10, 10, 5, 1. The $x^2$ term is the third term, so the coefficient is 10.",
             hint="Write down row 5 of Pascal's triangle. Which entry goes with $x^2$?",
             feedback=[r"5 is the coefficient of $x$ (the second term).", "",
                       "20 is not in row 5. Rebuild the row by adding pairs from row 4: 1, 4, 6, 4, 1.",
                       r"$5^2$ is not a binomial coefficient. Use row 5 of the triangle."]),
        H("Expanding (1 + kx)ⁿ"),
        T(r"Often you only need the first few terms, written in **ascending powers of $x$** (constant first, then $x$, then $x^2$, ...). "
          r"For $(1 + kx)^n$ the powers of 1 are all 1, so only the coefficients and the powers of $kx$ matter."),
        EX("Worked example 3: first three terms",
           intro=r"Find the first three terms, in ascending powers of $x$, of (a) $(1 + 2x)^5$ and (b) $\left(1 - \frac{x}{2}\right)^6$.", steps=[
            S("(a) Row 5 starts 1, 5, 10", math=r"(1 + 2x)^5 = 1 + 5(2x) + 10(2x)^2 + \dots"),
            S("(a) Simplify", math=r"= 1 + 10x + 40x^2 + \dots"),
            S("(b) Row 6 starts 1, 6, 15", math=r"\left(1 - \tfrac{x}{2}\right)^6 = 1 + 6\left(-\tfrac{x}{2}\right) + 15\left(-\tfrac{x}{2}\right)^2 + \dots"),
            S("(b) Simplify", math=r"= 1 - 3x + \tfrac{15}{4}x^2 + \dots"),
        ]),
        H("Common mistakes"),
        MISTAKE("Not raising the number with x",
                r"In $(1 + 2x)^5$, the $x^2$ term is $10(2x)^2 = 40x^2$, not $10 \times 2x^2 = 20x^2$. Put brackets round the whole second term."),
        MISTAKE("Losing the minus sign", r"In $(3 - 2x)^4$, $b = -2x$, so $(-2x)^3 = -8x^3$ is negative."),
        MISTAKE("Forgetting the powers of a", r"In $(2 + x)^4$ the first term is $2^4 = 16$, not 2."),
        QUIZ(r"How many terms are there in the expansion of $(a + b)^8$?", ["$8$", "$16$", "$7$", "$9$"], 3,
             r"The powers of $b$ run from 0 to 8, which is 9 terms.",
             hint="List the powers of $b$, starting from 0.",
             feedback=[r"Remember the term with $b^0$. Powers 0 to 8 give 9 terms.", "Doubling $n$ has no meaning here.",
                       r"Count the powers $0, 1, 2, \dots, 8$: there are 9.", ""]),
        H("Practice questions"),
        PQ(r"Expand $(1 + 3x)^4$ fully.",
           r"Row 4: 1, 4, 6, 4, 1. $1 + 4(3x) + 6(3x)^2 + 4(3x)^3 + (3x)^4 = 1 + 12x + 54x^2 + 108x^3 + 81x^4$."),
        PQ(r"Expand $(x - 2)^5$.",
           r"Row 5: 1, 5, 10, 10, 5, 1, with $a = x$ and $b = -2$. "
           r"$x^5 + 5x^4(-2) + 10x^3(4) + 10x^2(-8) + 5x(16) + (-32) = x^5 - 10x^4 + 40x^3 - 80x^2 + 80x - 32$."),
        PQ(r"The first three terms of $(1 + ax)^4$ are $1 + 12x + bx^2$. Find $a$ and $b$.",
           r"$(1 + ax)^4 = 1 + 4ax + 6a^2x^2 + \dots$. So $4a = 12$, giving $a = 3$, and $b = 6a^2 = 54$."),
        PQ(r"Find the coefficient of $x^2$ in the expansion of $(1 + x)(1 - 2x)^5$.",
           r"$(1 - 2x)^5 = 1 - 10x + 40x^2 + \dots$. Multiply by $(1 + x)$: the $x^2$ terms are $1 \times 40x^2$ and $x \times (-10x)$. "
           r"Coefficient $= 40 - 10 = 30$."),
        H("Summary"),
        SUM(r"Row $n$ of Pascal's triangle gives the coefficients of $(a + b)^n$; each entry is the sum of the two above it.",
            r"$(a + b)^n$ has $n + 1$ terms; the powers of $a$ go down, the powers of $b$ go up, and they add to $n$.",
            r"For $(a - b)^n$ use $b$ with its minus sign: the signs alternate.",
            "Put brackets round the whole second term, including its number and sign.",
            "Ascending powers of x means constant term first, then x, then x², and so on."),
    ],
))

LESSONS.append(lesson(
    module=MODULE,
    topic=BINOM,
    title="The general term and applications of the binomial expansion",
    slug="binomial-general-term-and-applications",
    minutes=25,
    summary="Use the notation ⁿCᵣ and the general term to find a particular term, the coefficient of a given power of x or the term independent of x, and use expansions to approximate values such as 1.02⁵.",
    objectives=[
        r"Work out binomial coefficients ${}^nC_r$ without drawing Pascal's triangle",
        r"Use the general term $\binom{n}{r}a^{n-r}b^r$ to find a given term or coefficient",
        r"Find the term independent of $x$",
        "Use the first terms of an expansion to approximate a number",
    ],
    key_concepts=["Binomial coefficient ⁿCᵣ", "Factorial", "General term", "Term independent of x", "Approximation"],
    blocks=[
        H("Introduction"),
        T(r"Pascal's triangle is fine for small powers. But to find just the $x^3$ term in $(1 - 2x)^7$, or a term in $(2 + x)^{12}$, "
          r"drawing many rows is slow. A formula gives any coefficient directly."),
        T(r"Binomial expansions also help with estimates. A savings group (njangi) in Bamenda that grows by 2% a year multiplies by $1.02$ each year. "
          r"After 5 years the factor is $1.02^5$, and the expansion gives a quick, accurate estimate of it."),
        D(r"$n!$ (read as $n$ factorial) means $n \times (n - 1) \times \dots \times 2 \times 1$, with $0! = 1$. The binomial coefficient is",
          title="Binomial coefficients", formula=r"\binom{n}{r} = {}^nC_r = \frac{n!}{r!\,(n - r)!}",
          note=r"For example, $\binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$. Also $\binom{n}{r} = \binom{n}{n - r}$, so $\binom{7}{4} = 35$ too."),
        D(r"The term containing $b^r$ in the expansion of $(a + b)^n$ is the $(r + 1)$th term:",
          title="The general term", formula=r"T_{r+1} = \binom{n}{r}\,a^{n-r}\,b^r",
          note=r"The 1st term has $r = 0$, the 4th term has $r = 3$, and so on."),
        F(r"(a + b)^n = a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \dots + \binom{n}{r}a^{n-r}b^r + \dots + b^n", title="The binomial theorem"),
        H("Worked examples"),
        EX("Worked example 1: one coefficient", intro=r"Find the coefficient of $x^3$ in the expansion of $(1 - 2x)^7$.", steps=[
            S(r"General term with $a = 1$, $b = -2x$, $n = 7$", math=r"T_{r+1} = \binom{7}{r}(1)^{7-r}(-2x)^r"),
            S(r"For $x^3$ take $r = 3$", math=r"\binom{7}{3}(-2x)^3 = 35 \times (-8x^3) = -280x^3"),
            S("State the coefficient", math=r"-280"),
        ]),
        EX("Worked example 2: a term in the middle", intro=r"Find the term in $x^4$ in the expansion of $(2 + x)^7$.", steps=[
            S("General term", math=r"T_{r+1} = \binom{7}{r}2^{7-r}x^r"),
            S(r"Take $r = 4$", math=r"\binom{7}{4}2^3x^4 = 35 \times 8 \times x^4"),
            S("Simplify", math=r"280x^4"),
        ]),
        QUIZ(r"What is the value of $\binom{6}{2}$?", ["$15$", "$30$", "$12$", "$3$"], 0,
             r"$\binom{6}{2} = \frac{6 \times 5}{2 \times 1} = 15$.",
             hint=r"Use $\frac{6 \times 5}{2 \times 1}$.",
             feedback=["", r"You forgot to divide by $2! = 2$.", r"$6 \times 2$ is not the formula.", r"$6 \div 2$ is not the formula."]),
        H("The term independent of x"),
        T(r"When both terms of the binomial contain $x$, such as $\left(x + \frac{2}{x}\right)^6$, one term may have no $x$ at all. "
          r"It is called the **term independent of $x$** (the constant term). Find the power of $x$ in the general term and set it equal to 0."),
        EX("Worked example 3: the term independent of x", intro=r"Find the term independent of $x$ in $\left(x + \frac{2}{x}\right)^6$.", steps=[
            S("Write the general term", math=r"\binom{6}{r}x^{6-r}\left(\frac{2}{x}\right)^r = \binom{6}{r}2^r x^{6-r}x^{-r}"),
            S("Collect the powers of x", math=r"\binom{6}{r}2^r x^{6-2r}"),
            S("Independent of $x$ means power 0", math=r"6 - 2r = 0 \Rightarrow r = 3"),
            S("Work out the term", math=r"\binom{6}{3} \times 2^3 = 20 \times 8 = 160"),
        ]),
        QUIZ(r"In the expansion of $\left(2x - \frac{1}{x}\right)^6$, which value of $r$ gives the term independent of $x$?",
             ["$r = 2$", "$r = 6$", "$r = 3$", "$r = 0$"], 2,
             r"The power of $x$ in the general term is $(6 - r) - r = 6 - 2r$. Setting $6 - 2r = 0$ gives $r = 3$.",
             hint=r"Write the power of $x$ in the general term in terms of $r$.",
             feedback=[r"With $r = 2$ the power is $6 - 4 = 2$, not 0.", r"With $r = 6$ the power is $6 - 12 = -6$.", "",
                       r"With $r = 0$ the term is $(2x)^6$, which contains $x^6$."]),
        H("Approximations"),
        EX("Worked example 4: estimating 1.02⁵",
           intro=r"Write the first three terms of $(1 + 2x)^5$. Use them to estimate $1.02^5$.", steps=[
            S("Expand", math=r"(1 + 2x)^5 = 1 + 5(2x) + 10(2x)^2 + \dots = 1 + 10x + 40x^2 + \dots"),
            S(r"Choose $x$ so that $1 + 2x = 1.02$", math=r"2x = 0.02 \Rightarrow x = 0.01"),
            S("Substitute", math=r"1 + 10(0.01) + 40(0.01)^2 = 1 + 0.1 + 0.004 = 1.104"),
        ], check=r"1.02^5 = 1.10408\ldots \text{ (calculator)}"),
        TIP("The approximation is good only when x is small, because the higher powers of x are then tiny. Always show how you chose x."),
        H("Common mistakes"),
        MISTAKE("Mixing up r and the term number", r"$T_{r+1}$ contains $b^r$. The 4th term has $r = 3$, not $r = 4$."),
        MISTAKE("Dropping the number in the second term",
                r"In $(1 - 2x)^7$, the $x^3$ term uses $(-2x)^3 = -8x^3$, not $-2x^3$."),
        MISTAKE("Wrong powers with fractions in x", r"$\left(\frac{2}{x}\right)^r = 2^r x^{-r}$. The power of $x$ is negative."),
        H("Practice questions"),
        PQ(r"The coefficient of $x^2$ in the expansion of $(1 + ax)^6$ is 60. Find the positive value of $a$.",
           r"The $x^2$ term is $\binom{6}{2}(ax)^2 = 15a^2x^2$. So $15a^2 = 60$, $a^2 = 4$ and $a = 2$."),
        PQ(r"Find the term independent of $x$ in $\left(2x - \frac{1}{x}\right)^6$.",
           r"General term: $\binom{6}{r}(2x)^{6-r}\left(-\frac{1}{x}\right)^r$, with power of $x$ equal to $6 - 2r$. "
           r"So $r = 3$: $\binom{6}{3}(2)^3(-1)^3 = 20 \times 8 \times (-1) = -160$."),
        PQ(r"Find the coefficient of $x^5$ in the expansion of $\left(x^2 + \frac{1}{x}\right)^7$.",
           r"General term: $\binom{7}{r}(x^2)^{7-r}(x^{-1})^r = \binom{7}{r}x^{14-3r}$. Set $14 - 3r = 5$: $r = 3$. Coefficient $\binom{7}{3} = 35$."),
        PQ(r"Expand $(2 + x)^6$ up to the term in $x^2$. Use your answer to estimate $2.01^6$.",
           r"$(2 + x)^6 = 64 + 6(32)x + 15(16)x^2 + \dots = 64 + 192x + 240x^2 + \dots$. "
           r"Put $x = 0.01$: $64 + 1.92 + 0.024 = 65.944$. (A calculator gives $65.9442\ldots$)"),
        H("Summary"),
        SUM(r"${}^nC_r = \binom{n}{r} = \frac{n!}{r!(n - r)!}$, and $\binom{n}{r} = \binom{n}{n - r}$.",
            r"General term of $(a + b)^n$: $T_{r+1} = \binom{n}{r}a^{n-r}b^r$.",
            "To find a given power of x, write the power of x in the general term and solve for r.",
            "The term independent of x is the term where the power of x is 0.",
            "For approximations, choose a small x that makes the bracket equal the number you need."),
    ],
))
