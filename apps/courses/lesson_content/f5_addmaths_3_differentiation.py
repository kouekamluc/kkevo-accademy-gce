"""Form 5 Additional Mathematics: Calculus, Differentiation (5 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("additional-mathematics", "form-5")

MODULE = "Calculus"
TOPIC = "Differentiation"

LESSONS = []

# ------------------------------------------------------------------ 1. First principles
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Gradients and differentiation from first principles",
    slug="gradient-of-a-curve-from-first-principles",
    minutes=24,
    summary="See how the gradient of a chord approaches the gradient of the tangent, use the limit definition of the derivative, and differentiate x², x³ and simple polynomials from first principles.",
    objectives=[
        "Find the gradient of a chord joining two points on a curve",
        "Explain why the gradient of a curve at a point is the gradient of the tangent there",
        r"State the definition $\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$",
        "Differentiate $x^2$, $x^3$ and simple polynomials from first principles",
    ],
    key_concepts=["Gradient of a chord", "Tangent to a curve", "Limit as h tends to 0", "Derivative from first principles", "dy/dx notation"],
    blocks=[
        H("Introduction"),
        T("Think of the road that climbs from Dschang towards the Bafoussam plateau. On some stretches it is steep, on others almost flat. "
          "The steepness changes as you move along the road."),
        T("In General Mathematics you found the gradient of a straight line: $m = \\frac{\\text{change in } y}{\\text{change in } x}$. "
          "A straight line has the same gradient everywhere. A curve does not. "
          "**Differentiation** is the method that gives the gradient of a curve at any point. This lesson shows where it comes from."),
        D("The **gradient of a curve** at a point $P$ is the gradient of the **tangent** to the curve at $P$. "
          "The tangent is the straight line that just touches the curve at $P$ and has the same direction as the curve there.",
          title="Definition: gradient of a curve"),
        H("From a chord to a tangent"),
        T("We cannot find the gradient of a tangent from one point only. So we take a second point $Q$ on the curve, close to $P$, "
          "and draw the **chord** $PQ$. Then we move $Q$ closer and closer to $P$."),
        IMG("f5a-chord-to-tangent.svg",
            alt="The curve y = x squared with the point P(1, 1) and a second point Q(1 + h, (1 + h) squared). The chord PQ is drawn in blue and the tangent at P in green. A horizontal step of length h and a vertical step f(1 + h) minus f(1) form a right-angled triangle under the chord.",
            caption="Figure 1. As $h$ gets smaller, $Q$ slides down the curve towards $P$ and the chord $PQ$ turns into the tangent at $P$."),
        EX("Worked example 1: chords on y = x² through P(1, 1)",
           intro=r"For $y = x^2$, find the gradient of the chord from $P(1, 1)$ to $Q(1 + h, (1 + h)^2)$, and see what happens as $h$ gets small.", steps=[
            S("Gradient of the chord", math=r"m_{PQ} = \frac{(1 + h)^2 - 1}{(1 + h) - 1} = \frac{1 + 2h + h^2 - 1}{h}"),
            S("Simplify", math=r"m_{PQ} = \frac{2h + h^2}{h} = 2 + h"),
            S("Try some values of $h$", text=r"$h = 1$ gives 3, $h = 0.1$ gives 2.1, $h = 0.01$ gives 2.01, $h = 0.001$ gives 2.001."),
            S("Let $h$ shrink towards 0", math=r"m_{PQ} = 2 + h \;\to\; 2",
              text="The gradient of the curve at $P(1, 1)$ is **2**."),
        ]),
        H("The definition of the derivative"),
        T("Do the same thing at a general point $(x, f(x))$. The second point is $(x + h, f(x + h))$, so the chord has gradient "
          "$\\frac{f(x + h) - f(x)}{h}$. Letting $h$ tend to 0 gives the gradient of the tangent."),
        D(r"The **derivative** of $y = f(x)$ is the gradient function. We write it $\frac{dy}{dx}$ or $f'(x)$. "
          r"Finding it from this limit is called differentiating **from first principles**.",
          title="Definition: derivative from first principles",
          formula=r"\frac{dy}{dx} = f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}",
          note=r'Read $\lim_{h \to 0}$ as "the limit as $h$ tends to 0". You must divide by $h$ **before** letting $h$ become 0.'),
        KEY("Four steps for first principles", "Use these steps every time.", cards=[
            ["Step 1", "Write $f(x + h)$ and expand it fully."],
            ["Step 2", "Subtract $f(x)$. Every term without $h$ cancels."],
            ["Step 3", "Divide every term by $h$."],
            ["Step 4", "Let $h \\to 0$: the terms that still contain $h$ vanish."],
        ]),
        EX("Worked example 2: y = x²", intro=r"Differentiate $y = x^2$ from first principles.", steps=[
            S("Step 1: expand $f(x + h)$", math=r"f(x + h) = (x + h)^2 = x^2 + 2xh + h^2"),
            S("Step 2: subtract $f(x)$", math=r"f(x + h) - f(x) = 2xh + h^2"),
            S("Step 3: divide by $h$", math=r"\frac{f(x + h) - f(x)}{h} = 2x + h"),
            S("Step 4: let $h \\to 0$", math=r"\frac{dy}{dx} = 2x"),
        ], check=r"\text{At } x = 1:\ 2(1) = 2, \text{ as in Worked example 1}"),
        EX("Worked example 3: y = x³", intro=r"Differentiate $y = x^3$ from first principles.", steps=[
            S("Step 1: expand, using the binomial expansion", math=r"(x + h)^3 = x^3 + 3x^2h + 3xh^2 + h^3"),
            S("Step 2: subtract $x^3$", math=r"f(x + h) - f(x) = 3x^2h + 3xh^2 + h^3"),
            S("Step 3: divide by $h$", math=r"3x^2 + 3xh + h^2"),
            S("Step 4: let $h \\to 0$", math=r"\frac{dy}{dx} = 3x^2"),
        ]),
        EX("Worked example 4: a polynomial", intro=r"Differentiate $y = 2x^2 - 5x + 1$ from first principles, and find the gradient at $x = 3$.", steps=[
            S("Step 1: expand $f(x + h)$", math=r"2(x + h)^2 - 5(x + h) + 1 = 2x^2 + 4xh + 2h^2 - 5x - 5h + 1"),
            S("Step 2: subtract $f(x) = 2x^2 - 5x + 1$", math=r"f(x + h) - f(x) = 4xh + 2h^2 - 5h"),
            S("Step 3: divide by $h$", math=r"4x + 2h - 5"),
            S("Step 4: let $h \\to 0$", math=r"\frac{dy}{dx} = 4x - 5"),
            S("Gradient at $x = 3$", math=r"4(3) - 5 = 7"),
        ]),
        QUIZ(r"For $y = x^2$, the chord from $x = 3$ to $x = 3 + h$ has gradient $6 + h$. What is the gradient of the curve at $x = 3$?",
             ["$6 + h$", "$9$", "$6$", "$3$"], 2,
             r"Let $h \to 0$: $6 + h \to 6$. This agrees with $\frac{dy}{dx} = 2x = 6$.",
             hint="What happens to the chord gradient when $h$ becomes very small?",
             feedback=[r"That is still the chord gradient. Let $h \to 0$ to get the tangent gradient.",
                       r"9 is the $y$-value $3^2$, not the gradient.", "",
                       r"3 is the $x$-value. The gradient of $y = x^2$ at $x$ is $2x$."]),
        H("Common mistakes"),
        MISTAKE("Expanding (x + h)² as x² + h²",
                r"$(x + h)^2 = x^2 + 2xh + h^2$. The middle term $2xh$ is the one that gives the derivative, so you cannot lose it."),
        MISTAKE("Putting h = 0 too early",
                r"If you put $h = 0$ in $\frac{2xh + h^2}{h}$ you get $\frac{0}{0}$, which means nothing. Divide by $h$ first, then let $h \to 0$."),
        MISTAKE("Subtracting only part of f(x)",
                r"Put brackets round $f(x)$: $f(x + h) - (2x^2 - 5x + 1)$. Every sign inside changes, so $-5x$ becomes $+5x$ and cancels."),
        QUIZ(r"Differentiating $y = 5x^2$ from first principles, what does $\frac{f(x + h) - f(x)}{h}$ simplify to, before $h \to 0$?",
             [r"$10x + 5h$", r"$10x$", r"$10xh + 5h^2$", r"$5x + h$"], 0,
             r"$5(x + h)^2 - 5x^2 = 10xh + 5h^2$. Dividing by $h$ gives $10x + 5h$.",
             hint=r"Expand $5(x + h)^2$, subtract $5x^2$, then divide by $h$.",
             feedback=["", r"That is the limit after $h \to 0$. Before the limit, a $5h$ term is still there.",
                       r"That is $f(x + h) - f(x)$. You still need to divide by $h$.",
                       r"You forgot to multiply every term of $(x + h)^2$ by 5."]),
        H("Practice questions"),
        PQ(r"Find the gradient of the chord joining the points on $y = x^2 + 1$ where $x = 2$ and $x = 2.1$. What value does this suggest for the gradient at $x = 2$?",
           r"At $x = 2$, $y = 5$. At $x = 2.1$, $y = 4.41 + 1 = 5.41$. Gradient $= \frac{5.41 - 5}{2.1 - 2} = \frac{0.41}{0.1} = 4.1$. "
           r"As the second point moves closer, the gradient approaches 4 (and indeed $\frac{dy}{dx} = 2x = 4$ at $x = 2$)."),
        PQ(r"Differentiate $y = 3x^2$ from first principles.",
           r"$f(x + h) - f(x) = 3(x^2 + 2xh + h^2) - 3x^2 = 6xh + 3h^2$. Divide by $h$: $6x + 3h$. As $h \to 0$, $\frac{dy}{dx} = 6x$."),
        PQ(r"Differentiate $y = x^2 - 4x$ from first principles. Hence find the gradient of the curve at $x = 5$.",
           r"$f(x + h) - f(x) = (x^2 + 2xh + h^2 - 4x - 4h) - (x^2 - 4x) = 2xh + h^2 - 4h$. "
           r"Divide by $h$: $2x + h - 4$. As $h \to 0$, $\frac{dy}{dx} = 2x - 4$. At $x = 5$ the gradient is $10 - 4 = 6$."),
        PQ(r"Differentiate $y = x^3 + 2x$ from first principles.",
           r"$f(x + h) = x^3 + 3x^2h + 3xh^2 + h^3 + 2x + 2h$. Subtract $f(x)$: $3x^2h + 3xh^2 + h^3 + 2h$. "
           r"Divide by $h$: $3x^2 + 3xh + h^2 + 2$. As $h \to 0$, $\frac{dy}{dx} = 3x^2 + 2$."),
        H("Summary"),
        SUM("The gradient of a curve at a point is the gradient of the tangent at that point.",
            r"The chord from $(x, f(x))$ to $(x + h, f(x + h))$ has gradient $\frac{f(x + h) - f(x)}{h}$.",
            r"First principles: $\frac{dy}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$.",
            "Expand, subtract, divide by $h$, then let $h \\to 0$, in that order.",
            r"Results: $\frac{d}{dx}(x^2) = 2x$, $\frac{d}{dx}(x^3) = 3x^2$, and a constant term gives 0."),
    ],
))

# ------------------------------------------------------------------ 2. Powers of x
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Differentiating powers of x",
    slug="differentiating-powers-of-x",
    minutes=24,
    summary="Use the rule d/dx(xⁿ) = nxⁿ⁻¹ for whole, negative and fractional powers, differentiate sums and constant multiples, rewrite roots and fractions as powers, and find the gradient at a point.",
    objectives=[
        r"Use $\frac{d}{dx}(x^n) = nx^{n-1}$ for whole, negative and fractional values of $n$",
        "Differentiate sums, differences and constant multiples term by term",
        "Rewrite roots, fractions and brackets as sums of powers of $x$ before differentiating",
        "Find the gradient of a curve at a given point",
    ],
    key_concepts=["Power rule", "Constant multiple rule", "Derivative of a constant", "Negative and fractional indices", "Gradient at a point"],
    blocks=[
        H("Introduction"),
        T("In the last lesson you found, from first principles, that $x^2$ gives $2x$ and $x^3$ gives $3x^2$. "
          "Doing a limit every time is slow. In this lesson you learn the shortcut that examiners expect you to use."),
        T("Look at the pattern: the power comes down in front, and the new power is one less. "
          "This works for every power of $x$, including negative powers and fractions. "
          "You need the laws of indices from General Mathematics, for example $\\frac{1}{x^2} = x^{-2}$ and $\\sqrt{x} = x^{\\frac{1}{2}}$."),
        D("Multiply by the power, then reduce the power by one.",
          title="The power rule", formula=r"y = x^n \quad\Rightarrow\quad \frac{dy}{dx} = nx^{n-1}",
          note="This holds for any rational $n$: positive, negative or a fraction."),
        KEY("Three more rules", "These let you differentiate any sum of powers.", cards=[
            ["Constant multiple", r"$\frac{d}{dx}(ax^n) = anx^{n-1}$, e.g. $\frac{d}{dx}(5x^4) = 20x^3$"],
            ["Sum or difference", "Differentiate term by term."],
            ["Constant", r"$\frac{d}{dx}(c) = 0$ and $\frac{d}{dx}(ax) = a$"],
        ]),
        D(r"$\frac{dy}{dx}$ is the derivative of $y$ with respect to $x$. If $f(x) = x^3$, then $f'(x) = 3x^2$. "
          r"The operator $\frac{d}{dx}$ placed in front of an expression means: differentiate it with respect to $x$.",
          title="Notation"),
        H("Worked examples"),
        EX("Worked example 1: polynomials and negative powers",
           intro=r"Differentiate (a) $y = 4x^3 - 5x^2 + 7x - 2$ (b) $y = \frac{6}{x^2}$.", steps=[
            S("(a) Term by term", math=r"\frac{dy}{dx} = 4(3x^2) - 5(2x) + 7 - 0 = 12x^2 - 10x + 7"),
            S("(b) Write as a power first", math=r"y = 6x^{-2}"),
            S("(b) Bring down $-2$ and reduce the power to $-3$", math=r"\frac{dy}{dx} = 6(-2)x^{-3} = -12x^{-3}"),
            S("(b) Write without a negative index", math=r"\frac{dy}{dx} = -\frac{12}{x^3}"),
        ]),
        EX("Worked example 2: roots and a gradient at a point",
           intro=r"Find the gradient of $y = 2\sqrt{x} + \frac{3}{x}$ at the point where $x = 4$.", steps=[
            S("Rewrite as powers", math=r"y = 2x^{\frac{1}{2}} + 3x^{-1}"),
            S("Differentiate", math=r"\frac{dy}{dx} = 2 \cdot \tfrac{1}{2}x^{-\frac{1}{2}} + 3(-1)x^{-2} = x^{-\frac{1}{2}} - 3x^{-2}"),
            S("In fraction form", math=r"\frac{dy}{dx} = \frac{1}{\sqrt{x}} - \frac{3}{x^2}"),
            S("Substitute $x = 4$", math=r"\frac{1}{2} - \frac{3}{16} = \frac{8}{16} - \frac{3}{16} = \frac{5}{16}"),
        ]),
        QUIZ(r"What is $\frac{d}{dx}(5x^4)$?", [r"$5x^3$", r"$20x^5$", r"$20x^3$", r"$x^5$"], 2,
             r"Multiply by the power 4 and reduce the power by 1: $5 \times 4x^3 = 20x^3$.",
             hint="Bring the power down and multiply, then lower the power by one.",
             feedback=["You reduced the power but forgot to multiply by 4.", "The power goes down by 1, not up.", "",
                       "That looks like integration, not differentiation."]),
        H("Rewrite before you differentiate"),
        T("There is no simple rule here for a product of brackets or a fraction with $x$ on top and bottom. "
          "So first **expand** brackets, or **divide** each term of the numerator by the denominator. "
          "Then every term is a power of $x$."),
        EX("Worked example 3: brackets and a fraction",
           intro=r"Differentiate (a) $y = (2x + 1)(x - 3)$ (b) $y = \frac{x^2 + 3}{x}$.", steps=[
            S("(a) Expand first", math=r"y = 2x^2 - 6x + x - 3 = 2x^2 - 5x - 3"),
            S("(a) Differentiate", math=r"\frac{dy}{dx} = 4x - 5"),
            S("(b) Divide each term by $x$", math=r"y = \frac{x^2}{x} + \frac{3}{x} = x + 3x^{-1}"),
            S("(b) Differentiate", math=r"\frac{dy}{dx} = 1 - 3x^{-2} = 1 - \frac{3}{x^2}"),
        ]),
        EX("Worked example 4: using the f'(x) notation",
           intro=r"Given $f(x) = x^3 - 6x + 2$, find $f'(2)$ and $f'(-1)$.", steps=[
            S("Differentiate", math=r"f'(x) = 3x^2 - 6"),
            S("Substitute $x = 2$", math=r"f'(2) = 3(4) - 6 = 6"),
            S("Substitute $x = -1$", math=r"f'(-1) = 3(1) - 6 = -3",
              text="The curve is going up at $x = 2$ (positive gradient) and going down at $x = -1$ (negative gradient)."),
        ]),
        H("Common mistakes"),
        MISTAKE("Keeping the constant term",
                r"The derivative of a constant is 0. For $y = x^2 + 7$, $\frac{dy}{dx} = 2x$, not $2x + 7$."),
        MISTAKE("Getting negative powers wrong",
                r"For $x^{-2}$ the power comes down as $-2$ and the new power is $-3$ (one **less**, not $-1$). So $\frac{d}{dx}(x^{-2}) = -2x^{-3}$."),
        MISTAKE("Differentiating brackets one at a time",
                r"$(2x + 1)(x - 3)$ does not give $2 \times 1 = 2$. Expand first, then differentiate: $4x - 5$."),
        MISTAKE("Differentiating the bottom of a fraction",
                r"$\frac{6}{x^2}$ does not give $\frac{6}{2x}$. Rewrite it as $6x^{-2}$, which gives $-\frac{12}{x^3}$."),
        QUIZ(r"Differentiate $y = 8\sqrt{x}$.", [r"$4\sqrt{x}$", r"$\frac{4}{\sqrt{x}}$", r"$\frac{16}{3}x^{\frac{3}{2}}$", r"$\frac{8}{2x}$"], 1,
             r"$y = 8x^{\frac{1}{2}}$, so $\frac{dy}{dx} = 8 \cdot \frac{1}{2}x^{-\frac{1}{2}} = 4x^{-\frac{1}{2}} = \frac{4}{\sqrt{x}}$.",
             hint=r"Write $\sqrt{x}$ as $x^{\frac{1}{2}}$ first.",
             feedback=[r"You multiplied by $\frac{1}{2}$ but did not reduce the power. $\frac{1}{2} - 1 = -\frac{1}{2}$.", "",
                       "You raised the power, which is integration.",
                       r"You differentiated $x$ under the root sign as if it were $x^1$. Use the power $\frac{1}{2}$."]),
        H("Practice questions"),
        PQ(r"Differentiate $y = 3x^4 - \frac{2}{x} + 5$.",
           r"$y = 3x^4 - 2x^{-1} + 5$. Then $\frac{dy}{dx} = 12x^3 + 2x^{-2} = 12x^3 + \frac{2}{x^2}$."),
        PQ(r"Find the gradient of $y = x\sqrt{x}$ at the point where $x = 9$.",
           r"$y = x^{\frac{3}{2}}$, so $\frac{dy}{dx} = \frac{3}{2}x^{\frac{1}{2}} = \frac{3}{2}\sqrt{x}$. At $x = 9$: $\frac{3}{2} \times 3 = 4.5$."),
        PQ(r"Differentiate $y = (x - 2)^2$.",
           r"Expand: $y = x^2 - 4x + 4$. Then $\frac{dy}{dx} = 2x - 4$."),
        PQ(r"Given $f(x) = \frac{x^3 + 1}{x^2}$, find $f'(x)$ and $f'(1)$.",
           r"$f(x) = x + x^{-2}$, so $f'(x) = 1 - 2x^{-3} = 1 - \frac{2}{x^3}$. Then $f'(1) = 1 - 2 = -1$."),
        H("Summary"),
        SUM(r"Power rule: $\frac{d}{dx}(x^n) = nx^{n-1}$ for any rational $n$.",
            r"Constant multiples stay: $\frac{d}{dx}(ax^n) = anx^{n-1}$. A constant term differentiates to 0.",
            "Differentiate a sum or difference term by term.",
            r"Rewrite first: $\frac{a}{x^n} = ax^{-n}$, $\sqrt{x} = x^{\frac{1}{2}}$; expand brackets and split fractions.",
            r"To find the gradient at a point, differentiate first, then substitute the $x$-value."),
    ],
))

# ------------------------------------------------------------------ 3. Tangents and normals
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Equations of tangents and normals",
    slug="equations-of-tangents-and-normals",
    minutes=24,
    summary="Find the equations of the tangent and the normal to a curve at a given point, and find the points on a curve where the gradient has a given value, such as where a tangent is parallel to a given line.",
    objectives=[
        "Find the gradient of the tangent to a curve at a given point",
        r"Find the gradient of the normal using $m_1 m_2 = -1$",
        "Write the equations of the tangent and the normal in the form required",
        "Find the points on a curve where the gradient has a given value",
    ],
    key_concepts=["Tangent", "Normal", "Perpendicular gradients", "Point-gradient form of a line", "Parallel tangents"],
    blocks=[
        H("Introduction"),
        T("When a motorbike taxi takes a bend on a wet road and skids, it carries on in a straight line in the direction it was moving at that instant. "
          "That straight line is the **tangent** to its curved path."),
        T("You can now find the gradient of a curve at any point. Together with the equation of a straight line from General Mathematics, "
          "$y - y_1 = m(x - x_1)$, that is all you need to find tangents and normals."),
        D(r"The **tangent** at $P$ touches the curve at $P$ and has gradient $m = \frac{dy}{dx}$ at $P$. "
          r"The **normal** at $P$ is the line through $P$ perpendicular to the tangent.",
          title="Definition: tangent and normal",
          note=r"Two lines with gradients $m_1$ and $m_2$ are perpendicular when $m_1 m_2 = -1$. So the normal has gradient $-\frac{1}{m}$."),
        IMG("f5a-tangent-and-normal.svg",
            alt="A curve y = f(x) with a point P(x1, y1). The tangent at P, drawn in blue, has gradient m. The normal at P, drawn in green, is perpendicular to the tangent and has gradient minus 1 over m. A right-angle mark is drawn at P.",
            caption="Figure 1. The tangent and the normal at $P$ are perpendicular, so the product of their gradients is $-1$."),
        KEY("Method", r"To find the tangent and normal at the point where $x = a$:", cards=[
            ["1. The point", "Substitute $x = a$ into the curve to get $y_1$."],
            ["2. The gradient", r"Differentiate and substitute $x = a$ to get $m$."],
            ["3. Tangent", r"$y - y_1 = m(x - x_1)$"],
            ["4. Normal", r"$y - y_1 = -\frac{1}{m}(x - x_1)$"],
        ]),
        H("Worked examples"),
        EX("Worked example 1: tangent and normal to a cubic",
           intro=r"Find the equations of the tangent and the normal to $y = x^3 - 3x + 2$ at the point where $x = 2$.", steps=[
            S("Find $y$ at $x = 2$", math=r"y = 8 - 6 + 2 = 4", text="The point is $(2, 4)$."),
            S("Gradient of the tangent", math=r"\frac{dy}{dx} = 3x^2 - 3 = 3(4) - 3 = 9"),
            S("Tangent", math=r"y - 4 = 9(x - 2) \;\Rightarrow\; y = 9x - 14"),
            S(r"Normal gradient $-\frac{1}{9}$", math=r"y - 4 = -\tfrac{1}{9}(x - 2)"),
            S("Multiply by 9 and tidy", math=r"9y - 36 = -x + 2 \;\Rightarrow\; x + 9y = 38"),
        ], check=r"(2, 4):\quad 9(2) - 14 = 4, \qquad 2 + 9(4) = 38"),
        EX("Worked example 2: a curve with a negative power",
           intro=r"Find the equations of the tangent and the normal to $y = \frac{4}{x}$ at the point $(2, 2)$.", steps=[
            S("Rewrite and differentiate", math=r"y = 4x^{-1} \;\Rightarrow\; \frac{dy}{dx} = -4x^{-2} = -\frac{4}{x^2}"),
            S("Gradient at $x = 2$", math=r"m = -\frac{4}{4} = -1"),
            S("Tangent", math=r"y - 2 = -1(x - 2) \;\Rightarrow\; y = 4 - x"),
            S("Normal gradient", math=r"-\frac{1}{-1} = 1"),
            S("Normal", math=r"y - 2 = 1(x - 2) \;\Rightarrow\; y = x"),
        ]),
        QUIZ(r"The tangent to a curve at a point has gradient 4. What is the gradient of the normal at that point?",
             [r"$-4$", r"$\frac{1}{4}$", r"$4$", r"$-\frac{1}{4}$"], 3,
             r"The normal is perpendicular to the tangent, so $m_{\text{normal}} = -\frac{1}{4}$. Check: $4 \times (-\frac{1}{4}) = -1$.",
             hint=r"Use $m_1 m_2 = -1$.",
             feedback=[r"You changed the sign but did not turn it upside down. $4 \times (-4) = -16$, not $-1$.",
                       r"You turned it upside down but did not change the sign. $4 \times \frac{1}{4} = +1$, not $-1$.",
                       "That is the gradient of the tangent itself.", ""]),
        H("Points where the gradient has a given value"),
        T("Sometimes you are given the gradient and must find the point. Set $\\frac{dy}{dx}$ equal to the given value and solve for $x$. "
          "Then substitute each $x$ into the equation of the **curve** to get $y$. "
          "A tangent **parallel** to a line has the same gradient as that line."),
        EX("Worked example 3: finding the point",
           intro=r"Find the point on $y = x^2 - 4x + 5$ where the gradient is 2.", steps=[
            S("Differentiate", math=r"\frac{dy}{dx} = 2x - 4"),
            S("Set the gradient equal to 2", math=r"2x - 4 = 2 \;\Rightarrow\; x = 3"),
            S("Find $y$ from the curve", math=r"y = 9 - 12 + 5 = 2", text="The point is $(3, 2)$."),
        ]),
        EX("Worked example 4: tangents parallel to a line",
           intro=r"Find the equations of the tangents to $y = x^3 - 6x + 1$ that are parallel to the line $y = 6x + 1$.", steps=[
            S("The line has gradient 6, so set $\\frac{dy}{dx} = 6$", math=r"3x^2 - 6 = 6 \;\Rightarrow\; x^2 = 4 \;\Rightarrow\; x = 2 \text{ or } x = -2"),
            S("Find the points", math=r"x = 2:\ y = 8 - 12 + 1 = -3 \qquad x = -2:\ y = -8 + 12 + 1 = 5"),
            S("Tangent at $(2, -3)$", math=r"y + 3 = 6(x - 2) \;\Rightarrow\; y = 6x - 15"),
            S("Tangent at $(-2, 5)$", math=r"y - 5 = 6(x + 2) \;\Rightarrow\; y = 6x + 17"),
        ]),
        H("Common mistakes"),
        MISTAKE("Using the y-value as the gradient",
                r"The gradient comes from $\frac{dy}{dx}$, not from the curve. In Worked example 1 the point is $(2, 4)$ but the gradient is 9."),
        MISTAKE("Getting the normal gradient wrong",
                r"Turn the tangent gradient upside down **and** change its sign. If $m = -\frac{2}{3}$, the normal gradient is $+\frac{3}{2}$."),
        MISTAKE("Substituting into dy/dx to find y",
                r"Once you have $x$, put it into the equation of the curve to find $y$. Putting it into $\frac{dy}{dx}$ only gives the gradient back."),
        QUIZ(r"Find the equation of the tangent to $y = x^2$ at the point $(3, 9)$.",
             [r"$y = 6x - 9$", r"$y = 6x + 9$", r"$y = 9x - 18$", r"$y = -\frac{1}{6}x + \frac{19}{2}$"], 0,
             r"$\frac{dy}{dx} = 2x = 6$ at $x = 3$. Then $y - 9 = 6(x - 3)$, so $y = 6x - 9$.",
             hint=r"Find $\frac{dy}{dx}$ at $x = 3$, then use $y - y_1 = m(x - x_1)$.",
             feedback=["", r"Expanding $y - 9 = 6(x - 3)$ gives $y = 6x - 18 + 9 = 6x - 9$. Check: at $x = 3$, $6x + 9 = 27$, not 9.",
                       r"You used the $y$-value 9 as the gradient. The gradient is $2x = 6$.",
                       r"That is the normal. The tangent has gradient $+6$."]),
        H("Practice questions"),
        PQ(r"Find the equation of the normal to $y = 2x^2 - 3x$ at the point $(1, -1)$.",
           r"$\frac{dy}{dx} = 4x - 3 = 1$ at $x = 1$. Normal gradient $= -1$. "
           r"$y + 1 = -1(x - 1)$, so $y = -x$. Check: $(1, -1)$ satisfies $y = -x$."),
        PQ(r"Find the equation of the tangent to $y = x^3 - 2x^2 + 1$ at the point where $x = 2$.",
           r"$y = 8 - 8 + 1 = 1$, so the point is $(2, 1)$. $\frac{dy}{dx} = 3x^2 - 4x = 12 - 8 = 4$. "
           r"Tangent: $y - 1 = 4(x - 2)$, so $y = 4x - 7$."),
        PQ(r"Find the coordinates of the points on $y = 2x^3 - 3x^2$ where the gradient is 12.",
           r"$\frac{dy}{dx} = 6x^2 - 6x = 12$, so $x^2 - x - 2 = 0$, $(x - 2)(x + 1) = 0$, $x = 2$ or $x = -1$. "
           r"$x = 2$: $y = 16 - 12 = 4$. $x = -1$: $y = -2 - 3 = -5$. The points are $(2, 4)$ and $(-1, -5)$."),
        PQ(r"The tangent to $y = x^2 - 5x + 6$ at the point where $x = 1$ meets the $x$-axis at $A$ and the $y$-axis at $B$. Find the area of triangle $OAB$.",
           r"At $x = 1$: $y = 2$ and $\frac{dy}{dx} = 2x - 5 = -3$. Tangent: $y - 2 = -3(x - 1)$, so $y = -3x + 5$. "
           r"$A = (\frac{5}{3}, 0)$ and $B = (0, 5)$. Area $= \frac{1}{2} \times \frac{5}{3} \times 5 = \frac{25}{6}$ square units."),
        H("Summary"),
        SUM(r"Tangent at $(x_1, y_1)$: gradient $m = \frac{dy}{dx}$ there, equation $y - y_1 = m(x - x_1)$.",
            r"Normal: perpendicular to the tangent, gradient $-\frac{1}{m}$, equation $y - y_1 = -\frac{1}{m}(x - x_1)$.",
            "Find $y_1$ from the curve and $m$ from the derivative: do not mix them up.",
            r"For a given gradient $k$, solve $\frac{dy}{dx} = k$, then find $y$ from the curve.",
            "Parallel lines have equal gradients; perpendicular gradients multiply to $-1$."),
    ],
))

# ------------------------------------------------------------------ 4. Stationary points
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Stationary points: maximum and minimum points",
    slug="stationary-points-maxima-and-minima",
    minutes=25,
    summary="Find stationary points by solving dy/dx = 0, decide whether each is a maximum or a minimum using the second derivative or the sign of the gradient, and use them to sketch cubic curves.",
    objectives=[
        r"Find the stationary points of a curve by solving $\frac{dy}{dx} = 0$",
        r"Find the second derivative $\frac{d^2y}{dx^2}$ and use its sign to classify a stationary point",
        "Classify a stationary point by the change in sign of the gradient",
        "Sketch a cubic curve using its stationary points and intercepts",
    ],
    key_concepts=["Stationary point", "Maximum point", "Minimum point", "Second derivative", "Sign of the gradient", "Sketching a cubic"],
    blocks=[
        H("Introduction"),
        T("A cocoa cooperative near Kumba records how its profit changes as it hires more workers. At first profit rises, then it reaches a peak, "
          "then it falls. At the peak the curve is level for an instant: it is neither going up nor going down."),
        T("Points where a curve is level are called **stationary points**. Finding them is the key step in sketching curves "
          "and, in the next lesson, in finding the largest or smallest value of a quantity."),
        D(r"A **stationary point** is a point on a curve where the gradient is zero, so the tangent is horizontal. "
          r"A **maximum point** is higher than the points close to it on both sides. A **minimum point** is lower than the points close to it on both sides.",
          title="Definition: stationary point", formula=r"\frac{dy}{dx} = 0"),
        D(r"Differentiating $\frac{dy}{dx}$ again gives the **second derivative**, written $\frac{d^2y}{dx^2}$ or $f''(x)$. "
          r"It tells you how the gradient itself is changing.",
          title="Definition: second derivative",
          formula=r"y = x^3 - 3x \;\Rightarrow\; \frac{dy}{dx} = 3x^2 - 3 \;\Rightarrow\; \frac{d^2y}{dx^2} = 6x"),
        KEY("Two ways to decide the nature", r"At a stationary point, where $\frac{dy}{dx} = 0$:", cards=[
            ["Second derivative test", r"$\frac{d^2y}{dx^2} < 0$: maximum. $\frac{d^2y}{dx^2} > 0$: minimum. If it is 0, use the sign test."],
            ["Sign of the gradient", r"Check $\frac{dy}{dx}$ just to the left and right. $+\;0\;-$ is a maximum. $-\;0\;+$ is a minimum."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: second derivative test",
           intro=r"Find the stationary points of $y = 2x^3 - 3x^2 - 12x + 4$ and determine their nature.", steps=[
            S("Differentiate and set equal to 0", math=r"\frac{dy}{dx} = 6x^2 - 6x - 12 = 0"),
            S("Divide by 6 and factorize", math=r"x^2 - x - 2 = 0 \;\Rightarrow\; (x - 2)(x + 1) = 0 \;\Rightarrow\; x = 2 \text{ or } x = -1"),
            S("Find the $y$-values from the curve", math=r"x = -1:\ y = -2 - 3 + 12 + 4 = 11 \qquad x = 2:\ y = 16 - 12 - 24 + 4 = -16"),
            S("Second derivative", math=r"\frac{d^2y}{dx^2} = 12x - 6"),
            S("Classify", text=r"At $x = -1$: $-18 < 0$, so $(-1, 11)$ is a maximum. At $x = 2$: $18 > 0$, so $(2, -16)$ is a minimum."),
        ]),
        QUIZ(r"At a stationary point, $\frac{d^2y}{dx^2} = -3$. What type of point is it?", ["A minimum", "A maximum", "Not a stationary point", "It cannot be decided"], 1,
             r"A negative second derivative means the gradient is decreasing: it goes from positive to zero to negative. The curve turns from going up to going down, so it is a maximum.",
             hint=r"Negative $\frac{d^2y}{dx^2}$: is the gradient increasing or decreasing?",
             feedback=["A minimum has a positive second derivative.", "",
                       r"The question says it is stationary, so $\frac{dy}{dx} = 0$ there.",
                       r"The test only fails when $\frac{d^2y}{dx^2} = 0$."]),
        EX("Worked example 2: sign of the gradient, then sketch",
           intro=r"Find the stationary points of $y = x^3 - 6x^2 + 9x$, classify them using the sign of the gradient, and sketch the curve.", steps=[
            S("Set the gradient to zero", math=r"\frac{dy}{dx} = 3x^2 - 12x + 9 = 3(x - 1)(x - 3) = 0 \;\Rightarrow\; x = 1 \text{ or } x = 3"),
            S("Find $y$", math=r"x = 1:\ y = 1 - 6 + 9 = 4 \qquad x = 3:\ y = 27 - 54 + 27 = 0"),
            S("Sign of the gradient around $x = 1$", math=r"x = 0:\ \tfrac{dy}{dx} = 9 > 0 \qquad x = 2:\ \tfrac{dy}{dx} = -3 < 0",
              text="The sign goes $+\\;0\\;-$, so $(1, 4)$ is a maximum."),
            S("Sign of the gradient around $x = 3$", math=r"x = 2:\ \tfrac{dy}{dx} = -3 < 0 \qquad x = 4:\ \tfrac{dy}{dx} = 9 > 0",
              text="The sign goes $-\\;0\\;+$, so $(3, 0)$ is a minimum."),
            S("Intercepts for the sketch", math=r"y = x(x - 3)^2",
              text="The curve passes through the origin and touches the $x$-axis at $(3, 0)$."),
        ]),
        GRAPH([1, -6, 9, 0], alt="Cubic curve y = x cubed minus 6x squared plus 9x. It rises through the origin to a maximum at (1, 4), falls to a minimum at (3, 0) where it touches the x-axis, then rises again.",
              caption="Figure 1. $y = x^3 - 6x^2 + 9x$: maximum at $(1, 4)$, minimum at $(3, 0)$, where the curve touches the $x$-axis.",
              xmin=-0.8, xmax=4.6, ymin=-3, ymax=6, roots=[0, 3], label="y = x³ − 6x² + 9x"),
        T("A cubic with a **positive** $x^3$ coefficient rises from bottom left to top right, so its maximum comes before its minimum. "
          "With a **negative** $x^3$ coefficient it falls from top left to bottom right, so the minimum comes first, as in Figure 2."),
        GRAPH([-1, 3, 0, 0], alt="Cubic curve y = 3x squared minus x cubed. It comes down from the top left to a minimum at the origin, rises to a maximum at (2, 4), then falls, crossing the x-axis at x = 3.",
              caption="Figure 2. $y = 3x^2 - x^3$: minimum at $(0, 0)$ and maximum at $(2, 4)$.",
              xmin=-1.5, xmax=3.6, ymin=-3, ymax=6, roots=[0, 3], label="y = 3x² − x³"),
        TIP(r"If $\frac{d^2y}{dx^2} = 0$ at a stationary point, the second derivative test gives no answer. Use the sign test. "
            r"For example, $y = x^3$ has $\frac{dy}{dx} = 3x^2 = 0$ at the origin, but the gradient is positive on both sides ($+\;0\;+$): "
            r"the origin is neither a maximum nor a minimum. It is called a **point of inflexion**."),
        H("Common mistakes"),
        MISTAKE("Giving only the x-coordinate",
                "A stationary point is a point. Substitute each $x$ into the equation of the curve and give both coordinates."),
        MISTAKE("Substituting into the wrong equation",
                r"Use the **curve** to find $y$, and use $\frac{d^2y}{dx^2}$ to classify. Putting $x$ into $\frac{dy}{dx}$ just gives 0 again."),
        MISTAKE("Reversing the test",
                r"Negative second derivative means **maximum** (think of a hill: the gradient goes from $+$ to $-$). Positive means minimum."),
        QUIZ(r"Find the stationary point of $y = x^2 - 8x + 3$ and state its nature.",
             [r"Maximum at $(4, -13)$", r"Minimum at $(4, 3)$", r"Minimum at $(-4, 51)$", r"Minimum at $(4, -13)$"], 3,
             r"$\frac{dy}{dx} = 2x - 8 = 0$ gives $x = 4$, and $y = 16 - 32 + 3 = -13$. $\frac{d^2y}{dx^2} = 2 > 0$, so it is a minimum.",
             hint=r"Solve $2x - 8 = 0$, then use the curve for $y$ and the second derivative for the nature.",
             feedback=[r"$\frac{d^2y}{dx^2} = 2$ is positive, so the point is a minimum.",
                       r"You did not find $y$ correctly: substitute $x = 4$ into the whole curve, $16 - 32 + 3 = -13$.",
                       r"$2x - 8 = 0$ gives $x = +4$, not $-4$.", ""]),
        H("Practice questions"),
        PQ(r"Find the stationary points of $y = 2x^3 - 9x^2 + 12x$ and determine their nature.",
           r"$\frac{dy}{dx} = 6x^2 - 18x + 12 = 6(x - 1)(x - 2) = 0$, so $x = 1$ or $x = 2$. "
           r"$x = 1$: $y = 2 - 9 + 12 = 5$. $x = 2$: $y = 16 - 36 + 24 = 4$. "
           r"$\frac{d^2y}{dx^2} = 12x - 18$: at $x = 1$ it is $-6$ (maximum at $(1, 5)$); at $x = 2$ it is $6$ (minimum at $(2, 4)$)."),
        PQ(r"Find the stationary points of $y = x + \frac{4}{x}$ and determine their nature.",
           r"$y = x + 4x^{-1}$, so $\frac{dy}{dx} = 1 - 4x^{-2} = 0$, giving $x^2 = 4$, $x = 2$ or $x = -2$. "
           r"$x = 2$: $y = 4$. $x = -2$: $y = -4$. $\frac{d^2y}{dx^2} = 8x^{-3}$: at $x = 2$ it is $1 > 0$ (minimum at $(2, 4)$); "
           r"at $x = -2$ it is $-1 < 0$ (maximum at $(-2, -4)$). Notice the maximum is lower than the minimum: they are only highest or lowest **locally**."),
        PQ(r"Find the stationary points of $y = x^4 - 2x^2$ and determine their nature.",
           r"$\frac{dy}{dx} = 4x^3 - 4x = 4x(x - 1)(x + 1) = 0$, so $x = 0$, $1$ or $-1$. "
           r"$y(0) = 0$, $y(1) = y(-1) = -1$. $\frac{d^2y}{dx^2} = 12x^2 - 4$: at $x = 0$ it is $-4$ (maximum at $(0, 0)$); "
           r"at $x = \pm 1$ it is $8$ (minima at $(1, -1)$ and $(-1, -1)$)."),
        PQ(r"Sketch $y = 12x - x^3$, showing its stationary points and where it crosses the axes.",
           r"$\frac{dy}{dx} = 12 - 3x^2 = 0$ gives $x = \pm 2$. $y(2) = 24 - 8 = 16$, $y(-2) = -16$. "
           r"$\frac{d^2y}{dx^2} = -6x$: maximum at $(2, 16)$, minimum at $(-2, -16)$. "
           r"$y = x(12 - x^2) = 0$ at $x = 0$ and $x = \pm 2\sqrt{3} \approx \pm 3.46$. The $x^3$ coefficient is negative, so the curve comes down from the top left, "
           r"through the minimum, up through the origin to the maximum, then down to the bottom right."),
        H("Summary"),
        SUM(r"At a stationary point $\frac{dy}{dx} = 0$: the tangent is horizontal.",
            r"Solve $\frac{dy}{dx} = 0$ for $x$, then find each $y$ from the curve.",
            r"$\frac{d^2y}{dx^2} < 0$ means maximum; $\frac{d^2y}{dx^2} > 0$ means minimum.",
            r"Sign test: $\frac{dy}{dx}$ going $+\;0\;-$ is a maximum, $-\;0\;+$ is a minimum. Use it when $\frac{d^2y}{dx^2} = 0$.",
            "To sketch a cubic: stationary points, intercepts with the axes, and the sign of the $x^3$ term."),
    ],
))

# ------------------------------------------------------------------ 5. Optimisation and rates of change
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Applications: optimisation and rates of change",
    slug="optimisation-and-rates-of-change",
    minutes=25,
    summary="Use differentiation to find the greatest or least value of a quantity, such as the largest area of a fenced field or the largest volume of an open box, and interpret a derivative as a rate of change.",
    objectives=[
        "Write a quantity to be maximised or minimised in terms of one variable",
        "Use stationary points to find the greatest or least value and justify its nature",
        r"Interpret $\frac{dy}{dx}$ and $\frac{dy}{dt}$ as rates of change in context",
        "Solve a simple connected rates of change problem",
    ],
    key_concepts=["Optimisation", "Maximum area and volume", "Rate of change", "Rate of change with respect to time", "Connected rates of change"],
    blocks=[
        H("Introduction"),
        T("A farmer in Foumban wants the biggest pen she can make with the fencing she has. A carpenter in Bamenda wants the biggest box he can fold from one sheet. "
          "A baker in Buea wants the number of loaves that gives the most profit. "
          "Each of these asks for a **maximum**, and the previous lesson gives the tool: set the derivative to zero."),
        KEY("Method for optimisation problems", "Work through these steps and show each one.", cards=[
            ["1. Variables", "Draw a diagram. Name the quantity to optimise and one variable, say $x$."],
            ["2. One variable", "Use the given condition to write the quantity in terms of $x$ only."],
            ["3. Differentiate", r"Solve $\frac{dA}{dx} = 0$ (or $\frac{dV}{dx} = 0$)."],
            ["4. Justify and answer", "Use the second derivative to show it is a maximum or minimum, then answer the question asked."],
        ]),
        H("Maximum area and volume"),
        EX("Worked example 1: fencing a pen against a wall",
           intro="A farmer in Foumban has 40 m of fencing. She builds a rectangular pen against a long wall, so only three sides need "
                 "fencing. Find the greatest area she can enclose.", steps=[
            S("Name the sides", text=r"Let the two sides at right angles to the wall be $x$ m. The side parallel to the wall is $40 - 2x$ m."),
            S("Area in terms of $x$", math=r"A = x(40 - 2x) = 40x - 2x^2"),
            S(r"Set $\frac{dA}{dx} = 0$", math=r"40 - 4x = 0 \;\Rightarrow\; x = 10"),
            S("Check it is a maximum", math=r"\frac{d^2A}{dx^2} = -4 < 0"),
            S("Greatest area", math=r"A = 10 \times 20 = 200 \text{ m}^2",
              text="The pen is 10 m by 20 m, with the 20 m side along the wall."),
        ]),
        IMG("f5a-open-box.svg",
            alt="Left: a square sheet of side 12 cm with a small square of side x cut from each corner and dashed fold lines; the middle square has side 12 minus 2x. Right: the open box folded from it, with height x and a square base of side 12 minus 2x. Its volume is V = x(12 minus 2x) squared.",
            caption="Figure 1. Cutting a square of side $x$ from each corner and folding up the sides gives an open box of height $x$ and base $(12 - 2x)$ by $(12 - 2x)$."),
        EX("Worked example 2: the largest open box",
           intro="A square sheet of metal of side 12 cm has a square of side $x$ cm cut from each corner. The sides are folded up to make an open box. "
                 "Find the value of $x$ that gives the largest volume, and that volume.", steps=[
            S("Volume in terms of $x$", math=r"V = x(12 - 2x)^2"),
            S("Expand", math=r"V = x(144 - 48x + 4x^2) = 4x^3 - 48x^2 + 144x"),
            S("Differentiate and set to zero", math=r"\frac{dV}{dx} = 12x^2 - 96x + 144 = 12(x - 2)(x - 6) = 0"),
            S("Choose the sensible root", text=r"$x = 6$ would leave a base of side $12 - 12 = 0$, so $V = 0$. Take $x = 2$."),
            S("Check it is a maximum", math=r"\frac{d^2V}{dx^2} = 24x - 96 = 48 - 96 = -48 < 0"),
            S("Largest volume", math=r"V = 2 \times 8^2 = 128 \text{ cm}^3"),
        ]),
        QUIZ(r"The area of a rectangle with perimeter 60 m is $A = 30x - x^2$, where $x$ m is one side. For which value of $x$ is the area greatest?",
             ["$x = 30$", "$x = 15$", "$x = 225$", "$x = 60$"], 1,
             r"$\frac{dA}{dx} = 30 - 2x = 0$ gives $x = 15$, and $\frac{d^2A}{dx^2} = -2 < 0$, so it is a maximum. The rectangle is a 15 m square.",
             hint=r"Solve $\frac{dA}{dx} = 0$.",
             feedback=[r"At $x = 30$ the other side is $30 - 30 = 0$, so the area is 0.", "",
                       "225 is the greatest area, not the value of $x$.",
                       "60 is the perimeter, not a side."]),
        H("Rates of change"),
        D(r"$\frac{dy}{dx}$ is the **rate of change** of $y$ with respect to $x$: how fast $y$ changes as $x$ increases. "
          r"When the variable is time $t$, $\frac{dh}{dt}$ is how fast $h$ changes per unit of time. "
          r"A positive rate means the quantity is increasing; a negative rate means it is decreasing.",
          title="Definition: rate of change"),
        EX("Worked example 3: the height of a ball",
           intro=r"A ball is thrown straight up. Its height after $t$ seconds is $h = 20t - 5t^2$ metres. "
                 r"Find the rate of change of height at $t = 1$ and at $t = 3$, and the greatest height.", steps=[
            S("Rate of change of height", math=r"\frac{dh}{dt} = 20 - 10t"),
            S("At $t = 1$", math=r"\frac{dh}{dt} = 10 \text{ m/s}", text="Positive: the ball is going up at 10 m/s."),
            S("At $t = 3$", math=r"\frac{dh}{dt} = -10 \text{ m/s}", text="Negative: the ball is coming down at 10 m/s."),
            S("Greatest height when $\\frac{dh}{dt} = 0$", math=r"20 - 10t = 0 \;\Rightarrow\; t = 2"),
            S("Greatest height", math=r"h = 40 - 20 = 20 \text{ m}", text=r"$\frac{d^2h}{dt^2} = -10 < 0$ confirms a maximum."),
        ]),
        T("Sometimes two quantities change together. If the radius $r$ of a circle grows with time, so does its area $A$. "
          "The rates are linked by multiplying the two derivatives: $\\frac{dA}{dt} = \\frac{dA}{dr} \\times \\frac{dr}{dt}$."),
        EX("Worked example 4: a spreading oil spot",
           intro="Palm oil spilt on a table spreads in a circle. Its radius increases at 0.5 cm/s. How fast is the area increasing when the radius is 4 cm?", steps=[
            S("Link area and radius", math=r"A = \pi r^2 \;\Rightarrow\; \frac{dA}{dr} = 2\pi r"),
            S("Connect the rates", math=r"\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt} = 2\pi r \times 0.5"),
            S("Substitute $r = 4$", math=r"\frac{dA}{dt} = 2\pi(4)(0.5) = 4\pi \approx 12.6 \text{ cm}^2/\text{s}"),
        ]),
        H("Common mistakes"),
        MISTAKE("Differentiating before using the condition",
                r"An area $A = xy$ has two variables. Use the given fact (fixed perimeter, fixed volume) to remove $y$ first, then differentiate."),
        MISTAKE("Answering the wrong question",
                "If the question asks for the greatest volume, finding $x = 2$ is not the end. Substitute back to get the volume, with units."),
        MISTAKE("Keeping an impossible root",
                "Check that each answer makes sense. A length cannot be negative, and a cut of $x = 6$ cm from a 12 cm sheet leaves no base."),
        QUIZ(r"Water flows into a tank so that the volume after $t$ minutes is $V = 50t + 2t^2$ litres. At what rate is the volume increasing when $t = 5$?",
             ["$300$ litres", "$60$ litres per minute", "$70$ litres per minute", "$20$ litres per minute"], 2,
             r"$\frac{dV}{dt} = 50 + 4t = 50 + 20 = 70$ litres per minute.",
             hint=r"Differentiate $V$ with respect to $t$, then substitute $t = 5$.",
             feedback=[r"That is the volume at $t = 5$, $250 + 50 = 300$ litres, not the rate.",
                       r"You differentiated $2t^2$ as $2t$. It is $4t$.", "",
                       r"You forgot the 50 from the $50t$ term."]),
        H("Practice questions"),
        PQ("A square sheet of card of side 18 cm has a square of side $x$ cm cut from each corner and is folded into an open box. Find the greatest volume.",
           r"$V = x(18 - 2x)^2 = 4x^3 - 72x^2 + 324x$. $\frac{dV}{dx} = 12x^2 - 144x + 324 = 12(x - 3)(x - 9) = 0$. "
           r"$x = 9$ gives no base, so $x = 3$. $\frac{d^2V}{dx^2} = 24x - 144 = -72 < 0$, a maximum. $V = 3 \times 12^2 = 432 \text{ cm}^3$."),
        PQ(r"A closed cylindrical tin has volume $128\pi$ cm³. Show that its surface area is $A = 2\pi r^2 + \frac{256\pi}{r}$ and find the radius that makes $A$ least.",
           r"$\pi r^2 h = 128\pi$, so $h = \frac{128}{r^2}$. $A = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{256\pi}{r}$. "
           r"$\frac{dA}{dr} = 4\pi r - \frac{256\pi}{r^2} = 0$ gives $r^3 = 64$, $r = 4$ cm. "
           r"$\frac{d^2A}{dr^2} = 4\pi + \frac{512\pi}{r^3} > 0$, a minimum. Then $h = 8$ cm and $A = 32\pi + 64\pi = 96\pi$ cm²."),
        PQ(r"A baker in Buea finds that her daily profit from selling $x$ loaves is $P = 400x - 2x^2$ FCFA. How many loaves give the greatest profit, and what is it?",
           r"$\frac{dP}{dx} = 400 - 4x = 0$ gives $x = 100$. $\frac{d^2P}{dx^2} = -4 < 0$, a maximum. "
           r"$P = 40\,000 - 20\,000 = 20\,000$ FCFA."),
        PQ(r"The edge of a metal cube expands at 0.1 cm/s when heated. Find the rate at which its volume is increasing when the edge is 5 cm.",
           r"$V = x^3$, so $\frac{dV}{dx} = 3x^2$. $\frac{dV}{dt} = 3x^2 \times \frac{dx}{dt} = 3(25)(0.1) = 7.5 \text{ cm}^3/\text{s}$."),
        H("Summary"),
        SUM("Write the quantity to optimise in terms of one variable, using the given condition.",
            r"Set its derivative to zero, solve, and reject values that make no sense in the problem.",
            r"Use the second derivative to justify a maximum or minimum, then answer the question with units.",
            r"$\frac{dy}{dt}$ is a rate of change: positive means increasing, negative means decreasing.",
            r"Connected rates: $\frac{dA}{dt} = \frac{dA}{dr} \times \frac{dr}{dt}$."),
    ],
))
