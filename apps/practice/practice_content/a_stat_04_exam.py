"""Pure Mathematics with Statistics (A Level): practice set for the Paper 3 lesson (both years).

KKEVO draft content. All data sets are invented for practice. Questions are based on the kinds of
mistakes listed in the Board's 2023 report for this paper; none is taken from a past paper.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-statistics", "lower-sixth"),
          ("pure-mathematics-with-statistics", "upper-sixth")]


def _mc(prompt, right, wrongs, pos, steps, concept, skill, hint, feedback="", **kw):
    """Four-option question: `wrongs` is three (text, why) pairs; the right option goes at index `pos`."""
    options = [C(t, why=w) for t, w in wrongs]
    options.insert(pos, C(right, correct=True))
    return MC(prompt, options, steps=steps, concept=concept, skill=skill, hint=hint, feedback=feedback, **kw)


P3 = [
    _mc(r"A school claims that the mean time its students spend on homework is $3.5$ hours a week. A parent believes that the mean has **increased**. Which alternative hypothesis should be used?",
        r"$H_1: \mu > 3.5$",
        [(r"$H_1: \mu \neq 3.5$", "The belief has a direction ('increased'), so a one-tailed alternative is needed. Writing $\\neq$ leads to a two-tailed test."),
         (r"$H_1: \bar{x} > 3.5$", "The alternative is about the population mean $\\mu$, not the sample mean."),
         (r"$H_1: \mu < 3.5$", "This is the wrong direction: 'increased' means greater than.")], 2,
        [S("Parameter", text=r"The hypotheses are about the population mean $\mu$."), S("Direction", text="'Increased' means the alternative is $\\mu > 3.5$ (one-tailed).")],
        "Writing hypotheses", "Concept", "Is the hypothesis about the population or the sample? Which direction?",
        feedback="Population parameter, direction from the words."),
    _mc(r"$P(A) = 0.7$, $P(B) = 0.5$ and $P(A \cup B) = 0.85$. Which statement is correct?",
        r"$P(A \cap B) = 0.35$, so $A$ and $B$ are independent",
        [(r"$P(A \cap B) = 0.35$, so $A$ and $B$ are mutually exclusive", r"Mutually exclusive means $P(A \cap B) = 0$, which is not the case."),
         (r"$P(A \cap B) = 0.35$, so $A$ and $B$ are not independent because $P(A \cap B) \neq 0$", r"Independence needs $P(A \cap B) = P(A)P(B)$, not $0$. Here $0.7 \times 0.5 = 0.35$."),
         (r"$P(A \cap B) = 0.15$, so $A$ and $B$ are not independent", r"You subtracted $P(A)$ from $P(A \cup B)$. The addition law gives $P(A \cap B) = 0.7 + 0.5 - 0.85$.")], 0,
        [S("Addition law", math=r"P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.7 + 0.5 - 0.85 = 0.35"), S("Test independence", math=r"P(A)P(B) = 0.35 = P(A \cap B)", text="So the events are independent.")],
        "Addition law and independence", "Reasoning", "Make the intersection the subject of the addition law, then compare with the product.",
        feedback="Independent means the intersection equals the product."),
    NUM(r"In a set of ordered data the lower quartile is $34$ and the upper quartile is $52$. Find the quartile deviation.", 9,
        steps=[S("Quartile deviation is the semi-interquartile range", math=r"\frac{1}{2}(Q_3 - Q_1) = \frac{1}{2}(52 - 34) = 9")],
        concept="Quartile deviation", skill="Recall", hint="Is the quartile deviation the whole interquartile range?",
        feedback="Quartile deviation = half the interquartile range."),
    _mc(r"Calls arrive at a rate of $2.5$ per hour (Poisson). Find the probability of **more than $4$** calls in $2$ hours.",
        r"$1 - P(X \leq 4)$ with $X \sim \text{Po}(5)$, which is $0.560$",
        [(r"$1 - P(X \leq 4)$ with $X \sim \text{Po}(2.5)$, which is $0.109$", "The mean $2.5$ is for one hour. For $2$ hours it is $5$."),
         (r"$1 - P(X \leq 5)$ with $X \sim \text{Po}(5)$, which is $0.384$", "This is $P(X > 5)$. 'More than 4' means 5 or more, so subtract $P(X \\leq 4)$."),
         (r"$1 - P(X \leq 3)$ with $X \sim \text{Po}(5)$, which is $0.735$", "This is $P(X > 3)$, which includes $4$. 'More than 4' starts at $5$.")], 1,
        [S("Match the mean to the period", math=r"\lambda = 2 \times 2.5 = 5"), S("More than 4", math=r"P(X > 4) = 1 - P(X \leq 4) = 1 - 0.4405 = 0.5595")],
        "Poisson parameter and complement", "Application", "Find the mean for two hours, then write 'more than 4' as one minus a cumulative probability.",
        feedback="Scale lambda; complement 1 - P(X <= 4)."),
    NUM(r"$X \sim B(50, 0.3)$. Use a normal approximation with a continuity correction to estimate $P(X \leq 12)$. Give your answer to 3 decimal places.", 0.220, tolerance=0.002,
        steps=[S("Mean and variance", math=r"\mu = 15, \quad \sigma^2 = 10.5, \quad \sigma = 3.240"),
               S("Continuity correction", math=r"P(X \leq 12) \approx P(Y < 12.5) = P\!\left(Z < \frac{12.5 - 15}{3.240}\right) = P(Z < -0.772)"),
               S("Table", math=r"= 0.220")],
        concept="Normal approximation and continuity correction", skill="Calculation", hint="Which boundary do you use for 'less than or equal to 12'?",
        feedback="Use 12.5 as the boundary."),
    _mc(r"The regression line of $y$ on $x$ is found from a sample of pairs of values. A candidate uses it to estimate $x$ when $y = 20$. What is the best advice?",
        r"Use the regression line of $x$ on $y$, calculated separately",
        [(r"Rearrange the line of $y$ on $x$ to make $x$ the subject", "The two regression lines are different lines. The line of $y$ on $x$ minimises the vertical distances, so rearranging it does not give the best estimate of $x$."),
         (r"Use the line of $y$ on $x$: it is the only regression line", "There are two regression lines. The one to use depends on which variable you want to estimate."),
         (r"Use the mean of $x$, because $y$ does not help", "A strong correlation makes $y$ useful for estimating $x$.")], 3,
        [S("Two regression lines", text="The line of $y$ on $x$ estimates $y$ from $x$. To estimate $x$ from $y$, use the line of $x$ on $y$.")],
        "Choosing the regression line", "Reasoning", "Which variable is being estimated?",
        feedback="Estimate x from y with the line of x on y."),
    NUM(r"A population has mean $40$ and standard deviation $10$. A random sample of $25$ observations is taken from this normal population. Find the probability that the sample mean exceeds $43$. Give your answer to 3 decimal places.", 0.067, tolerance=0.001,
        steps=[S("Distribution of the sample mean", math=r"\bar{X} \sim N\!\left(40, \frac{100}{25}\right) = N(40, 4), \quad \text{standard error } 2"),
               S("Standardise", math=r"P(\bar{X} > 43) = P(Z > 1.5) = 1 - 0.9332 = 0.0668 \approx 0.067")],
        concept="Sample mean probability", skill="Calculation", hint="State the distribution of the sample mean first.",
        feedback="Standardise with the standard error."),
    _mc(r"When drawing a cumulative frequency graph (ogive) for grouped data, where should each cumulative frequency be plotted?",
        "At the **upper class boundary** of its class",
        [("At the mid-value of its class", "Cumulative frequency up to a class is reached only at the end of the class, not in the middle."),
         ("At the upper class limit as printed, for example $29$ for the class $20$ to $29$", "For continuous data the boundary is $29.5$. The upper boundary is where the data in that class end."),
         ("At the class width", "The class width is a length. The horizontal axis shows the variable, so use boundaries.")], 0,
        [S("Cumulative frequency", text="It counts all values up to the end of a class, so plot against the upper boundary of that class.")],
        "Cumulative frequency graph", "Recall", "Where do the data in a class end?",
        feedback="Plot at the upper class boundary."),
]

SETS = [
    practice_set(module="Examination", topic="Paper 3", title="Paper 3 technique: statistics and probability",
                 lesson="sex-paper-3-statistics-strategy", questions=P3),
]
