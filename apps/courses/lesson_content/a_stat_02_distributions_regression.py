"""Statistics option, Upper Sixth: Further Distributions, and Correlation & Regression.

Pure Mathematics with Statistics (A Level, 770), Upper Sixth. KKEVO's own lessons, written in standard A Level
style and checked against the topic descriptions in the outline. All data sets are invented for practice.
"""

import math

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-statistics", "upper-sixth")]

M_DIST = "Further Distributions"
M_REG = "Correlation & Regression"


def _phi(z):
    """Standard normal cumulative distribution function, from math.erf."""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def _normal_table():
    """Table of Phi(z) to 4 decimal places for z = 0.00 to 3.49, built with math.erf."""
    rows = ["  z   " + "".join(f"{c / 100:6.2f}" for c in range(10))]
    for i in range(35):
        z = i / 10
        rows.append(f" {z:.1f}  " + "".join(f"{_phi(round(z + c / 100, 2)):6.4f}" for c in range(10)))
    return "\n".join(rows)


def _inv_phi(p):
    """Inverse of Phi by bisection."""
    lo, hi = -10.0, 10.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if _phi(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def _pp_table():
    """Percentage points of the standard normal: z such that Phi(z) = p."""
    rows = ["   p       z"]
    for p in (0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.975, 0.99, 0.995):
        rows.append(f"{p:6.3f}  {_inv_phi(p):7.4f}")
    return "\n".join(rows)


def _poisson_table(lam, kmax):
    rows = [" r    P(X = r)   P(X <= r)"]
    p = math.exp(-lam)
    cum = 0.0
    for r in range(kmax + 1):
        if r:
            p = p * lam / r
        cum += p
        rows.append(f"{r:2d}    {p:.4f}     {cum:.4f}")
    return "\n".join(rows)


LESSONS = []

# ---------------------------------------------------------------- 1. The Poisson distribution
LESSONS.append(lesson(
    module=M_DIST,
    topic="The Poisson distribution",
    title="The Poisson distribution: events at random in time",
    slug="stu1-poisson-distribution",
    minutes=22,
    summary="Use the Poisson model for events that occur singly, independently and at a constant average rate; find probabilities, match the parameter to the interval and add independent Poisson variables.",
    objectives=[
        "State when a situation can be modelled by a Poisson distribution",
        "Calculate P(X = r) and cumulative probabilities for X ~ Po(λ)",
        "Scale the parameter λ to the length of the interval in the question",
        "Use mean = variance = λ and the sum of independent Poisson variables",
    ],
    key_concepts=["Poisson distribution", "Parameter λ", "Mean equals variance", "Sum of Poisson variables"],
    blocks=[
        H("Introduction"),
        T(r"A mobile-money kiosk at Mokolo market in Yaoundé serves customers who arrive one at a time, at random, at an average of 18 per hour (data invented for practice). You cannot say exactly how many will come in the next 10 minutes, but you can say how likely 0, 1, 2 or more customers are. Events that happen at random in time (or along a road, or over an area) at a steady average rate are modelled by the **Poisson distribution**."),
        T(r"You have already met the binomial distribution, where there is a fixed number of trials. The Poisson distribution has **no fixed number of trials**: the count can be 0, 1, 2, 3, ... with no upper limit."),
        H("The Poisson model"),
        D(r"A random variable $X$ has a **Poisson distribution** with parameter $\lambda$ (written $X \sim \text{Po}(\lambda)$) if it counts events in a fixed interval of time or space, and for $r = 0, 1, 2, \dots$", title="Poisson distribution",
          formula=r"P(X = r) = \frac{e^{-\lambda}\lambda^{r}}{r!}",
          note=r"$\lambda$ is the average number of events in the interval you are asked about. $e \approx 2.71828$."),
        T(r"For the Poisson model to be sensible, four conditions are needed. Events occur **singly** (never two at exactly the same instant), **independently** of each other, at a **constant average rate**, and **at random**. If customers arrive in a crowd after each church service, the rate is not constant and the model fits badly."),
        KEY("Mean and variance", r"For $X \sim \text{Po}(\lambda)$ the mean and the variance are both equal to $\lambda$.", cards=[
            ["Mean", r"$E(X) = \lambda$"],
            ["Variance", r"$\text{Var}(X) = \lambda$"],
            ["Quick test", "If a data set has mean close to its variance, a Poisson model is plausible. A variance much larger than the mean suggests the events come in clusters."],
        ]),
        IMG("apostu1-poisson-bars.svg", alt="Bar chart of P(X = r) for a Poisson distribution with mean 3, r from 0 to 9. The bars for 0, 1 and 2 are dark. The tallest bars are at r = 2 and r = 3, each 0.224.",
            caption="Figure 1. The distribution Po(3). The three dark bars add up to P(X ≤ 2) = 0.423. The distribution is skewed to the right."),
        CODE(_poisson_table(3, 9), "text", title="Po(3): probabilities computed with Python (4 decimal places)",
             caption="Calculators give the same values. In an exam use your calculator's Poisson function or the formula and say which you used."),
        H("Matching the parameter to the interval"),
        T(r"The parameter $\lambda$ must be the average **for the interval in the question**. If the average is 18 customers per hour, then for 10 minutes $\lambda = 18 \times \frac{10}{60} = 3$, and for 20 minutes $\lambda = 6$. The Board's 2023 report says that many candidates took the wrong value for the Poisson parameter. Write the distribution down every time: \"$X \sim \text{Po}(3)$, the number of customers in 10 minutes\"."),
        EX("Worked example 1: scaling the rate", intro=r"Customers arrive at the kiosk at an average of 18 per hour. Find the probability that (a) exactly 2 customers arrive in a given 10 minutes, (b) at least 1 arrives in a given 10 minutes, (c) none arrives in a given 20 minutes.", steps=[
            S("Choose the interval and find $\\lambda$ for part (a)", math=r"\lambda = 18 \times \tfrac{10}{60} = 3, \qquad X \sim \text{Po}(3)", text=r"X is the number of customers in 10 minutes."),
            S("(a) Use the formula with $r = 2$", math=r"P(X = 2) = \frac{e^{-3}\,3^{2}}{2!} = 0.2240", text=r"To 4 decimal places."),
            S("(b) At least 1 is the complement of none", math=r"P(X \geq 1) = 1 - P(X = 0) = 1 - e^{-3} = 0.9502"),
            S("(c) New interval, so a new parameter", math=r"Y \sim \text{Po}(6), \qquad P(Y = 0) = e^{-6} = 0.00248", text=r"Y is the number of customers in 20 minutes. Do not keep using $\lambda = 3$."),
        ], check=r"e^{-3} = 0.049787,\ \ 0.049787 \times 9 \div 2 = 0.2240"),
        MISTAKE("Using the rate for the wrong interval", r"Writing $X \sim \text{Po}(18)$ because \"18 per hour\" is in the question, when the question asks about 10 minutes. First decide the interval, then scale the rate to it."),
        H("At least, more than, fewer than"),
        T(r"The Poisson variable takes the values $0, 1, 2, \dots$ without end, so \"more than 2\" cannot be added up term by term. Use the complement. Be careful with the boundary: \"more than 2\" means $3, 4, 5, \dots$, so"),
        F(r"P(X > 2) = 1 - P(X \leq 2) = 1 - \left[P(0) + P(1) + P(2)\right]"),
        T(r"Similarly $P(X \geq 3) = 1 - P(X \leq 2)$ and $P(X < 3) = P(X \leq 2)$. Taking the wrong complement for \"more than 2\", for example $1 - P(X \leq 3)$ or $1 - P(X < 2)$, is a mistake of exactly this kind."),
        EX("Worked example 2: more than, and a range", intro=r"For $X \sim \text{Po}(3)$ find (a) $P(X > 2)$, (b) $P(2 \leq X < 5)$.", steps=[
            S("(a) Complement. \"More than 2\" is everything except 0, 1 and 2", math=r"P(X > 2) = 1 - e^{-3}\left(1 + 3 + \tfrac{9}{2}\right) = 1 - 0.4232 = 0.5768"),
            S("(b) List the values 2, 3 and 4 (5 is not included)", math=r"P(2 \leq X < 5) = P(2) + P(3) + P(4)"),
            S("Calculate each term", math=r"0.2240 + 0.2240 + 0.1680 = 0.6161"),
        ], check=r"e^{-3}\left(\tfrac{9}{2} + \tfrac{27}{6} + \tfrac{81}{24}\right) = 12.375 \times 0.049787 = 0.6161"),
        H("Adding Poisson variables"),
        D(r"If $X \sim \text{Po}(\lambda)$ and $Y \sim \text{Po}(\mu)$ are **independent**, then $X + Y \sim \text{Po}(\lambda + \mu)$.", title="Sum of independent Poisson variables",
          note="This is natural: two independent streams of events, each at a steady rate, together give a stream at the combined rate."),
        EX("Worked example 3: two kiosks and an unknown parameter", intro=r"Two kiosks receive customers independently. The numbers in 10 minutes are $X \sim \text{Po}(3)$ and $Y \sim \text{Po}(2)$. (a) Find the probability that together they receive exactly 7 customers in 10 minutes. (b) A third kiosk has $W \sim \text{Po}(\lambda)$ with $P(W = 0) = 0.2$. Find $\lambda$.", steps=[
            S("(a) Add the parameters", math=r"X + Y \sim \text{Po}(5)"),
            S("Use the formula with $r = 7$", math=r"P(X + Y = 7) = \frac{e^{-5}\,5^{7}}{7!} = 0.1044"),
            S("(b) Write $P(W = 0)$ and solve", math=r"e^{-\lambda} = 0.2 \;\Rightarrow\; \lambda = -\ln 0.2 = \ln 5 = 1.609"),
        ], check=r"e^{-1.609} = 0.2000"),
        QUIZ(r"Calls to a school office average 0.5 per minute. Which gives the probability of no calls in one minute?",
             [r"$e^{-0.5}$", r"$1 - e^{-0.5}$", r"$0.5\,e^{-0.5}$", r"$e^{0.5}$"], 0,
             r"$P(X = 0) = e^{-0.5}\lambda^0/0! = e^{-0.5} = 0.6065$.",
             hint=r"Put r = 0 into the Poisson formula. What are 0! and a number to the power 0?",
             feedback=["", r"That is $P(X \geq 1)$, at least one call.", r"That is $P(X = 1)$.", "The exponent should be negative: $e^{0.5}$ is bigger than 1, and a probability cannot be."]),
        QUIZ(r"Which situation is the **least** suitable for a Poisson model?",
             ["Faults per 100 metres in a new tarred road, assumed to occur at random", "Customers arriving at a kiosk at a steady rate through the afternoon",
              "Number of students who pass out of 30 who each pass with probability 0.7", "Lorries passing a quiet checkpoint at a steady average rate"], 2,
             r"There is a fixed number of trials (30), each with success or failure: that is a binomial situation, $B(30, 0.7)$, not Poisson.",
             hint=r"Which one has a fixed number of trials with a fixed probability of success?",
             feedback=["This is a rate over a length, events occur singly at random: Poisson is reasonable.", "A steady rate and independent arrivals: Poisson is reasonable.", "", "Steady rate, events one at a time, independent: Poisson is reasonable."]),
        TIP(r"Exam link: the Poisson distribution appears in the multiple-choice Paper 1 and in the statistics essay-style paper. The Board's 2023 report for 0770 mentions candidates using the wrong parameter and mishandling the complement for \"more than\". Check the exact format with your teacher."),
        PQ(r"Power cuts in a quarter of Douala occur at random, on average 2 per week (invented). Find the probability of (a) no power cut in a week, (b) at least 3 power cuts in a two-week period.",
           r"(a) $X \sim \text{Po}(2)$, $P(X = 0) = e^{-2} = 0.1353$. (b) For two weeks $Y \sim \text{Po}(4)$. $P(Y \geq 3) = 1 - P(Y \leq 2) = 1 - e^{-4}(1 + 4 + 8) = 1 - 13e^{-4} = 0.7619$."),
        PQ(r"Vehicles pass a checkpoint on the Bafoussam road at an average of 90 per hour, at random. Find the probability that fewer than 3 vehicles pass in a 2-minute interval.",
           r"In 2 minutes $\lambda = 90 \times \frac{2}{60} = 3$. Fewer than 3 means 0, 1 or 2: $P(X \leq 2) = e^{-3}(1 + 3 + 4.5) = 0.4232$."),
        PQ(r"$X \sim \text{Po}(1.2)$ and $Y \sim \text{Po}(2.3)$ are independent. Find $P(X + Y = 4)$.",
           r"$X + Y \sim \text{Po}(3.5)$. $P(X + Y = 4) = \dfrac{e^{-3.5}\,3.5^{4}}{4!} = 0.1888$."),
        PQ(r"$X \sim \text{Po}(\lambda)$ and $P(X = 1) = 2P(X = 0)$. Find $\lambda$ and then $P(X \geq 2)$.",
           r"$\lambda e^{-\lambda} = 2e^{-\lambda}$, so $\lambda = 2$. $P(X \geq 2) = 1 - P(0) - P(1) = 1 - e^{-2}(1 + 2) = 1 - 3e^{-2} = 0.5940$."),
        SUM(r"$X \sim \text{Po}(\lambda)$ counts events at random, singly, independently and at a constant rate; $P(X = r) = e^{-\lambda}\lambda^r/r!$.",
            r"The mean and the variance are both $\lambda$, and $\lambda$ must be the average for the interval in the question.",
            r"For \"more than\" or \"at least\" use the complement, and check the boundary value.",
            r"Independent $\text{Po}(\lambda)$ and $\text{Po}(\mu)$ variables add to $\text{Po}(\lambda + \mu)$."),
    ],
))

# ---------------------------------------------------------------- 2. Continuous random variables
LESSONS.append(lesson(
    module=M_DIST,
    topic="Continuous random variables",
    title="Continuous random variables: density and cumulative distribution functions",
    slug="stu1-continuous-random-variables",
    minutes=24,
    summary="Work with a probability density function f(x) and the cumulative distribution function F(x): find constants, probabilities, the median, the mean and the variance by integration.",
    objectives=[
        "Explain why probabilities for a continuous variable are areas, and why P(X = a) = 0",
        "Find a constant so that a probability density function has total area 1",
        "Find F(x) from f(x) by integration, and f(x) from F(x) by differentiation",
        "Calculate the median, mean and variance of a continuous variable",
    ],
    key_concepts=["Probability density function", "Cumulative distribution function", "Median", "Mean and variance by integration"],
    blocks=[
        H("Introduction"),
        T(r"The time a passenger waits at the garage in Bafoussam for a bus to fill is not restricted to whole minutes: it could be 12.4 minutes, 12.43 minutes and so on. A variable that can take **any value in an interval** is called **continuous**. With a discrete variable we could list the probabilities. With a continuous variable there are infinitely many values, so we describe the distribution with a curve, and probabilities are **areas under the curve**."),
        D(r"A **probability density function** (pdf) $f(x)$ describes a continuous random variable $X$. It must satisfy $f(x) \geq 0$ for all $x$, and the total area under the curve is 1. The probability that $X$ lies between $a$ and $b$ is the area between $a$ and $b$:", title="Probability density function",
          formula=r"P(a < X < b) = \int_a^b f(x)\,dx, \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1"),
        T(r"The pdf is often given in pieces, for example $f(x) = kx(3 - x)$ for $0 \leq x \leq 3$ and $f(x) = 0$ otherwise. Outside the stated range the density is zero, so only integrate over the stated range."),
        IMG("apostu1-pdf-area.svg", alt="Curve f(x) = 2x(3 - x)/9 on 0 to 3, rising to a maximum at x = 1.5 and falling to zero at 3. The area under the curve between 0 and 1 is shaded and labelled P(X < 1).",
            caption="Figure 1. The probability P(X < 1) is the shaded area. The curve itself gives a density, not a probability."),
        H("A single value has probability zero"),
        T(r"The area above a single point has no width, so $P(X = a) = 0$ for every $a$. This has an important consequence: **$<$ and $\leq$ make no difference** for a continuous variable."),
        F(r"P(X \leq a) = P(X < a), \qquad P(a \leq X \leq b) = P(a < X < b)"),
        MISTAKE("Treating a continuous variable as discrete", r"The Board's 2023 report says that many candidates treated a continuous random variable as discrete and lost the marks for the whole question. Do not add up values of $f(x)$ and do not look for $P(X = 2)$. Integrate $f(x)$ over an interval. And remember that $f(x)$ can be greater than 1: it is a density, and only areas are probabilities."),
        EX("Worked example 1: the constant, a probability, the mean and the variance", intro=r"The waiting time $X$ hours (invented for practice) has pdf $f(x) = kx(3 - x)$ for $0 \leq x \leq 3$ and $f(x) = 0$ otherwise. Find $k$, $P(X < 1)$, $E(X)$ and $\text{Var}(X)$.", steps=[
            S("Total area must be 1", math=r"\int_0^3 kx(3 - x)\,dx = k\left[\frac{3x^2}{2} - \frac{x^3}{3}\right]_0^3 = k\left(\frac{27}{2} - 9\right) = \frac{9k}{2} = 1 \;\Rightarrow\; k = \frac{2}{9}"),
            S("Probability: integrate from 0 to 1", math=r"P(X < 1) = \frac{2}{9}\left[\frac{3x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{2}{9}\cdot\frac{7}{6} = \frac{7}{27} = 0.2593"),
            S(r"Mean: $E(X) = \int x f(x)\,dx$", math=r"E(X) = \frac{2}{9}\int_0^3 (3x^2 - x^3)\,dx = \frac{2}{9}\left[x^3 - \frac{x^4}{4}\right]_0^3 = \frac{2}{9}\cdot\frac{27}{4} = 1.5"),
            S(r"Second moment: $E(X^2) = \int x^2 f(x)\,dx$", math=r"E(X^2) = \frac{2}{9}\int_0^3 (3x^3 - x^4)\,dx = \frac{2}{9}\left[\frac{3x^4}{4} - \frac{x^5}{5}\right]_0^3 = \frac{2}{9}\cdot\frac{243}{20} = 2.7"),
            S("Variance", math=r"\text{Var}(X) = E(X^2) - [E(X)]^2 = 2.7 - 2.25 = 0.45"),
        ], check=r"\text{The curve is symmetrical about } x = 1.5, \text{ so } E(X) = 1.5 \text{ as found}"),
        KEY("Mean, variance, mode and median", r"For a continuous variable with pdf $f(x)$ these replace the sums used for discrete variables.", cards=[
            ["Mean", r"$E(X) = \int x f(x)\,dx$"],
            ["Variance", r"$\text{Var}(X) = \int x^2 f(x)\,dx - [E(X)]^2$"],
            ["Mode", r"The value of $x$ where $f(x)$ is greatest (a maximum of the curve)."],
            ["Median $m$", r"$\int_{-\infty}^{m} f(x)\,dx = \tfrac{1}{2}$, that is $F(m) = 0.5$."],
        ], note=r"Integrate over the range where $f$ is not zero. If $f$ has several pieces, split the integral at the boundaries."),
        H("The cumulative distribution function"),
        D(r"The **cumulative distribution function** (cdf) is $F(x) = P(X \leq x)$. If $f(t) = 0$ for $t < a$, then for $x$ in the range", title="Cumulative distribution function",
          formula=r"F(x) = \int_{a}^{x} f(t)\,dt, \qquad f(x) = \frac{dF}{dx}",
          note=r"Use a different letter, $t$, inside the integral, because $x$ is the upper limit. $F(x) = 0$ below the range and $F(x) = 1$ above it."),
        MISTAKE("Missing the lower limit when finding F", r"Candidates often write $F(x) = \int f(x)\,dx$ with no limits and no constant, or confuse $F$ with $f$. Integrate from the start of the range up to $x$, so that $F$ starts at 0, and check that $F$ ends at 1."),
        EX("Worked example 2: the cdf and the median", intro=r"$X$ has pdf $f(x) = \frac{3}{8}x^2$ for $0 \leq x \leq 2$, and 0 otherwise. Find $F(x)$, the median, $P(X > 1.5)$ and $\text{Var}(X)$.", steps=[
            S("Integrate from 0 to $x$", math=r"F(x) = \int_0^x \tfrac{3}{8}t^2\,dt = \frac{x^3}{8} \qquad (0 \leq x \leq 2)", text=r"F(x) = 0 for x < 0 and F(x) = 1 for x > 2. Check: F(2) = 1."),
            S("Median: $F(m) = 0.5$", math=r"\frac{m^3}{8} = \frac{1}{2} \;\Rightarrow\; m^3 = 4 \;\Rightarrow\; m = 1.587 \text{ (4 s.f.)}"),
            S("Upper tail: $P(X > 1.5) = 1 - F(1.5)$", math=r"1 - \frac{1.5^3}{8} = 1 - \frac{27}{64} = \frac{37}{64} = 0.5781"),
            S("Mean and second moment", math=r"E(X) = \int_0^2 \tfrac{3}{8}x^3\,dx = \tfrac{3}{8}\cdot 4 = 1.5, \qquad E(X^2) = \int_0^2 \tfrac{3}{8}x^4\,dx = \tfrac{3}{8}\cdot\tfrac{32}{5} = 2.4"),
            S("Variance", math=r"\text{Var}(X) = 2.4 - 1.5^2 = 0.15"),
        ], check=r"\text{Mean } 1.5 \text{ is less than the upper end } 2; \text{ the median } 1.587 \text{ is above the mean: skewed to the left}"),
        EX("Worked example 3: from the cdf to the pdf", intro=r"$X$ has cdf $F(x) = 0$ for $x < 1$, $F(x) = \frac{x^2 - 1}{8}$ for $1 \leq x \leq 3$, and $F(x) = 1$ for $x > 3$. Find $f(x)$, $P(1.5 < X < 2.5)$ and $E(X)$.", steps=[
            S("Differentiate $F$ on the range", math=r"f(x) = \frac{dF}{dx} = \frac{x}{4} \quad (1 \leq x \leq 3), \qquad f(x) = 0 \text{ otherwise}"),
            S("Probability from $F$", math=r"P(1.5 < X < 2.5) = F(2.5) - F(1.5) = \frac{6.25 - 1}{8} - \frac{2.25 - 1}{8} = \frac{4}{8} = 0.5"),
            S("Mean from $f$", math=r"E(X) = \int_1^3 x\cdot\frac{x}{4}\,dx = \left[\frac{x^3}{12}\right]_1^3 = \frac{27 - 1}{12} = \frac{13}{6} = 2.167"),
        ], check=r"F(3) = \frac{9 - 1}{8} = 1 \text{ and } F(1) = 0"),
        TIP(r"Exam link: continuous random variables are examined in the statistics essay-style paper, usually as a 'find $k$, find $F(x)$, find the median, mean and variance' question; the Board's 2023 report comments on it. Show the limits of every integral and state the range of $x$ for each piece of $F$. Check the exact format with your teacher."),
        QUIZ(r"A pdf is $f(x) = 0.5x$ for $0 \leq x \leq 2$. What is $P(X = 1)$?",
             ["0.5", "0", "0.25", "0.75"], 1,
             r"For a continuous variable a single value has no width, so $P(X = 1) = 0$. The value 0.5 is the density $f(1)$, not a probability.",
             hint=r"Is a probability the height of the curve or an area?",
             feedback=["That is f(1), the height of the curve. Probabilities are areas.", "", "That is the area from 0 to 1, which is P(X < 1), not P(X = 1).", "That is the area to the right of 1, P(X > 1), not P(X = 1)."]),
        QUIZ(r"The median $m$ of a continuous variable with cdf $F$ satisfies",
             [r"$f(m) = 0.5$", r"$F(m) = 0.5$", r"$F(m) = 1$", r"$f(m) = 1$"], 1,
             r"Half of the probability lies below the median, so $F(m) = P(X \leq m) = 0.5$.",
             hint=r"The median splits the total area of 1 into two equal parts.",
             feedback=["f is a height, not a probability.", "", "F = 1 only at the top of the range.", "f is a height, not a probability."]),
        IMG("apostu1-q-density.svg", alt="A triangular density curve on 0 to 4, rising from 0 at x = 0 to a peak of height k at x = 2 and falling to 0 at x = 4.", caption="Figure 2. Triangular pdf for practice question 1. The peak height k is not given."),
        PQ(r"The diagram shows a continuous variable with a triangular pdf on $0 \leq x \leq 4$, peak height $k$ at $x = 2$. Find $k$ and $P(X < 1)$.",
           r"Area of the triangle $= \frac{1}{2}\times 4 \times k = 2k = 1$, so $k = 0.5$. For $0 \leq x \leq 2$, $f(x) = \frac{k}{2}x = 0.25x$, so $P(X < 1) = \int_0^1 0.25x\,dx = 0.125$."),
        PQ(r"$f(x) = \frac{3}{4}x^2(2 - x)$ for $0 \leq x \leq 2$, and 0 otherwise. Show that $f$ is a pdf, and find $E(X)$ and $\text{Var}(X)$.",
           r"$\int_0^2 \frac{3}{4}(2x^2 - x^3)\,dx = \frac{3}{4}\left[\frac{2x^3}{3} - \frac{x^4}{4}\right]_0^2 = \frac{3}{4}\left(\frac{16}{3} - 4\right) = 1$, and $f \geq 0$ on the range. $E(X) = \frac{3}{4}\int_0^2 (2x^3 - x^4)\,dx = \frac{3}{4}\left(8 - \frac{32}{5}\right) = 1.2$. $E(X^2) = \frac{3}{4}\int_0^2 (2x^4 - x^5)\,dx = \frac{3}{4}\left(\frac{64}{5} - \frac{32}{3}\right) = 1.6$, so $\text{Var}(X) = 1.6 - 1.44 = 0.16$."),
        PQ(r"For the same pdf as the previous question find the cdf $F(x)$ and $P(X < 1)$.",
           r"$F(x) = \frac{3}{4}\int_0^x (2t^2 - t^3)\,dt = \frac{x^3}{2} - \frac{3x^4}{16}$ for $0 \leq x \leq 2$. Then $P(X < 1) = F(1) = \frac{1}{2} - \frac{3}{16} = \frac{5}{16} = 0.3125$. Check: $F(2) = 4 - 3 = 1$."),
        PQ(r"$X$ has cdf $F(x) = 1 - x^{-3}$ for $x \geq 1$ (and $F(x) = 0$ for $x < 1$). Find the median and $f(x)$.",
           r"Median: $1 - m^{-3} = 0.5$, so $m^{-3} = 0.5$ and $m = 2^{1/3} = 1.260$. Differentiate: $f(x) = 3x^{-4}$ for $x \geq 1$, and 0 otherwise."),
        SUM(r"A pdf $f(x) \geq 0$ has total area 1; probabilities are areas, and $P(X = a) = 0$, so $<$ and $\leq$ are the same.",
            r"$F(x) = \int_a^x f(t)\,dt$ and $f = F'$; $F$ rises from 0 to 1, and the median $m$ satisfies $F(m) = 0.5$.",
            r"$E(X) = \int x f\,dx$ and $\text{Var}(X) = \int x^2 f\,dx - [E(X)]^2$, integrated over the range where $f \neq 0$.",
            r"Never treat a continuous variable as discrete: integrate, do not add."),
    ],
))

# ---------------------------------------------------------------- 3. The normal distribution 1
LESSONS.append(lesson(
    module=M_DIST,
    topic="The normal distribution",
    title="The normal distribution: standardising and using tables",
    slug="stu1-normal-distribution-tables",
    minutes=24,
    summary="Describe the normal curve N(μ, σ²), standardise with Z = (X − μ)/σ and use the table of Φ(z) to find probabilities above, below and between values.",
    objectives=[
        "Describe the normal curve and read μ and σ from N(μ, σ²)",
        "Standardise a normal variable using Z = (X − μ)/σ",
        "Use the table of Φ(z), with symmetry for negative z",
        "Find probabilities of the types P(X < a), P(X > a) and P(a < X < b)",
    ],
    key_concepts=["Normal distribution", "Standard normal Z", "Standardising", "Table of Φ(z)", "Symmetry"],
    blocks=[
        H("Introduction"),
        T(r"A rice depot in Douala packs rice in bags labelled 50 kg. The masses are not all exactly equal: most are close to the average, a few are much lighter or much heavier, and the pattern is symmetrical. Measurements such as heights, masses and examination marks very often follow this bell-shaped pattern, called the **normal distribution**."),
        D(r"A continuous random variable $X$ has a **normal distribution** with mean $\mu$ and variance $\sigma^2$, written $X \sim N(\mu, \sigma^2)$, if its pdf is a bell-shaped curve that is symmetrical about $x = \mu$.", title="Normal distribution",
          note=r"The second number in $N(\mu, \sigma^2)$ is the **variance**. The standard deviation is $\sigma$. So $N(50.2, 0.4^2)$ has standard deviation 0.4."),
        T(r"The total area under the curve is 1. The curve is highest at $\mu$ and falls away on both sides; the area to the left of $\mu$ is 0.5. About 68% of values lie within one standard deviation of the mean, about 95% within two, and about 99.7% within three. More exactly $P(|Z| < 1) = 0.683$, $P(|Z| < 2) = 0.954$ and $P(|Z| < 3) = 0.997$."),
        IMG("apostu1-normal-below.svg", alt="A bell-shaped curve for bag masses with mean 50.2 kg, axis marked 49.4 to 51.0. The area to the left of 50 kg is shaded and labelled P(X < 50) = 0.3085.",
            caption="Figure 1. X ~ N(50.2, 0.4²). The shaded area to the left of 50 kg is the probability that a bag is under 50 kg."),
        H("Standardising"),
        T(r"There is a different normal curve for every $\mu$ and $\sigma$, but they all have the same shape. We convert any normal variable to the **standard normal variable** $Z \sim N(0, 1)$, whose areas are tabulated."),
        D(r"If $X \sim N(\mu, \sigma^2)$ then", title="Standardising", formula=r"Z = \frac{X - \mu}{\sigma} \sim N(0, 1)",
          note=r"$z$ counts how many standard deviations $x$ is above ($z > 0$) or below ($z < 0$) the mean. The cumulative probability is written $\Phi(z) = P(Z \leq z)$."),
        CODE(_normal_table(), "text", title="Table of Φ(z) = P(Z ≤ z), computed with Python (math.erf), 4 decimal places",
             caption="Read the row for z to one decimal place and the column for the second decimal place. For example Φ(1.25) is in row 1.2, column 0.05: 0.8944. For z above 3.49 the value is 1.0000 to 4 decimal places. Calculators give the same values: say whether you used a table or a calculator."),
        H("Reading probabilities"),
        KEY("Four rules for the table", r"Always sketch the curve and shade the area first.", cards=[
            ["Below a value", r"$P(Z < z) = \Phi(z)$, read straight from the table."],
            ["Above a value", r"$P(Z > z) = 1 - \Phi(z)$."],
            ["Negative $z$", r"The table has $z \geq 0$ only. Use symmetry: $\Phi(-z) = 1 - \Phi(z)$."],
            ["Between", r"$P(a < Z < b) = \Phi(b) - \Phi(a)$."],
        ]),
        EX("Worked example 1: bag masses", intro=r"The mass $X$ kg of a bag from the depot is $X \sim N(50.2, 0.4^2)$ (invented for practice). Find (a) $P(X < 50)$, (b) $P(X > 50.5)$, (c) $P(49.8 < X < 50.6)$.", steps=[
            S("Identify $\\mu$ and $\\sigma$", math=r"\mu = 50.2, \qquad \sigma = \sqrt{0.4^2} = 0.4"),
            S("(a) Standardise $x = 50$", math=r"z = \frac{50 - 50.2}{0.4} = -0.5, \qquad P(X < 50) = \Phi(-0.5) = 1 - \Phi(0.5) = 1 - 0.6915 = 0.3085"),
            S("(b) Standardise $x = 50.5$", math=r"z = \frac{50.5 - 50.2}{0.4} = 0.75, \qquad P(X > 50.5) = 1 - \Phi(0.75) = 1 - 0.7734 = 0.2266"),
            S("(c) Standardise both ends", math=r"z_1 = \frac{49.8 - 50.2}{0.4} = -1, \qquad z_2 = \frac{50.6 - 50.2}{0.4} = 1"),
            S("Subtract the two areas", math=r"P(49.8 < X < 50.6) = \Phi(1) - \Phi(-1) = 0.8413 - 0.1587 = 0.6826", text=r"This is 0.683 to 3 significant figures; a calculator gives 0.6827."),
        ], check=r"\text{(c) agrees with the 68\% rule for one standard deviation either side of the mean}"),
        MISTAKE("Using the variance as the standard deviation", r"In $X \sim N(50.2, 0.4^2)$ the standard deviation is 0.4, not $0.4^2 = 0.16$. If the question gives $N(20, 9)$, the variance is 9 and the standard deviation is $\sqrt{9} = 3$. Always write $\sigma$ down before standardising."),
        MISTAKE("Forgetting to standardise or to subtract", r"Looking up $\Phi(50)$ is meaningless: the table is for $z$ values. And for an upper tail the answer is $1 - \Phi(z)$, which must be less than 0.5 when $z > 0$. If your upper-tail answer for positive $z$ is above 0.5, you forgot the subtraction."),
        EX("Worked example 2: marks, with symmetry", intro=r"Marks in a school examination are $X \sim N(58, 16^2)$ (invented for practice). Find (a) $P(X > 90)$, (b) $P(50 < X < 90)$.", steps=[
            S("(a) Standardise 90", math=r"z = \frac{90 - 58}{16} = 2, \qquad P(X > 90) = 1 - \Phi(2) = 1 - 0.9772 = 0.0228"),
            S("(b) Standardise 50", math=r"z = \frac{50 - 58}{16} = -0.5, \qquad \Phi(-0.5) = 1 - 0.6915 = 0.3085"),
            S("Subtract", math=r"P(50 < X < 90) = \Phi(2) - \Phi(-0.5) = 0.9772 - 0.3085 = 0.6687"),
        ], check=r"\text{A calculator gives } 0.6687"),
        EX("Worked example 3: from a probability to an expected number", intro=r"The depot packs 2000 bags a week from the distribution in Worked example 1. How many bags are expected to be under 50 kg, and what is the probability that two bags chosen at random are both under 50 kg?", steps=[
            S("Use the probability found in example 1", math=r"P(X < 50) = 0.3085"),
            S("Expected number out of 2000", math=r"2000 \times 0.3085 = 617"),
            S("Two independent bags, multiply", math=r"0.3085^2 = 0.0952 \text{ (3 s.f.)}"),
        ]),
        TIP(r"Exam link: the normal distribution is tested in the statistics papers, in the multiple-choice Paper 1 (a standardising and table question) and in the longer papers. State your distribution, show the standardised value, and say which table or calculator function you used. Check the exact format with your teacher."),
        QUIZ(r"$X \sim N(40, 25)$. Which is the correct standardised value for $x = 47.5$?",
             [r"$z = 7.5/25 = 0.3$", r"$z = 7.5/5 = 1.5$", r"$z = 47.5/5 = 9.5$", r"$z = 7.5/\sqrt{25 - 40}$"], 1,
             r"The variance is 25, so $\sigma = 5$. $z = (47.5 - 40)/5 = 1.5$.",
             hint=r"The second number in N(μ, σ²) is the variance. What is the standard deviation?",
             feedback=["That divides by the variance 25 instead of the standard deviation 5.", "", "That forgets to subtract the mean.", "That is nonsense: the denominator is σ = 5."]),
        QUIZ(r"For $Z \sim N(0, 1)$, which is the value of $P(Z < -1.25)$, given $\Phi(1.25) = 0.8944$?",
             ["0.8944", "0.1056", "0.3944", "1.1056"], 1,
             r"By symmetry $\Phi(-1.25) = 1 - \Phi(1.25) = 1 - 0.8944 = 0.1056$.",
             hint=r"The area to the left of −1.25 equals the area to the right of +1.25.",
             feedback=["That is P(Z < 1.25), the area on the other side.", "", "That is the area between 0 and 1.25 (0.8944 − 0.5), not the tail.", "A probability can never be greater than 1."]),
        PQ(r"$X \sim N(100, 15^2)$. Find (a) $P(X > 115)$, (b) $P(85 < X < 130)$.",
           r"(a) $z = 1$, $1 - \Phi(1) = 1 - 0.8413 = 0.1587$. (b) $z_1 = -1$, $z_2 = 2$: $\Phi(2) - \Phi(-1) = 0.9772 - 0.1587 = 0.8185$."),
        PQ(r"The time $T$ minutes for a bush-taxi journey is $T \sim N(35, 4^2)$ (invented). Find the probability that a journey takes (a) less than 30 minutes, (b) more than 41 minutes.",
           r"(a) $z = (30 - 35)/4 = -1.25$, so $P = 1 - \Phi(1.25) = 1 - 0.8944 = 0.1056$. (b) $z = (41 - 35)/4 = 1.5$, so $P = 1 - 0.9332 = 0.0668$."),
        PQ(r"$Y \sim N(20, 9)$. Find $P(Y < 21.5)$ and $P(Y > 14)$.",
           r"$\sigma = 3$. $P(Y < 21.5)$: $z = 0.5$, $\Phi(0.5) = 0.6915$. $P(Y > 14)$: $z = -2$, $P = 1 - \Phi(-2) = \Phi(2) = 0.9772$."),
        PQ(r"The masses in worked example 1 are $N(50.2, 0.4^2)$. Find the probability that a bag is within 0.4 kg of 50 kg, that is $49.6 < X < 50.4$.",
           r"$z_1 = (49.6 - 50.2)/0.4 = -1.5$, $z_2 = (50.4 - 50.2)/0.4 = 0.5$. $P = \Phi(0.5) - \Phi(-1.5) = 0.6915 - (1 - 0.9332) = 0.6915 - 0.0668 = 0.6247$."),
        SUM(r"$X \sim N(\mu, \sigma^2)$ has a symmetrical bell-shaped curve centred on $\mu$; the second parameter is the **variance**.",
            r"Standardise with $z = (x - \mu)/\sigma$, then use the table of $\Phi(z) = P(Z \leq z)$.",
            r"Upper tails use $1 - \Phi(z)$, negative $z$ uses $\Phi(-z) = 1 - \Phi(z)$, and a range is a difference of two values of $\Phi$.",
            r"Sketch and shade the area first, and state which table or calculator function you used."),
    ],
))

# ---------------------------------------------------------------- 4. The normal distribution 2
LESSONS.append(lesson(
    module=M_DIST,
    topic="The normal distribution",
    title="The normal distribution: finding values, and unknown μ and σ",
    slug="stu1-normal-distribution-inverse",
    minutes=24,
    summary="Work backwards from a probability to a value using percentage points, and form and solve equations to find an unknown mean, standard deviation or both.",
    objectives=[
        "Find z from a probability using the percentage-points table or the inverse normal function",
        "Convert z back to x using x = μ + zσ",
        "Find an unknown σ or μ from one probability condition",
        "Find μ and σ together from two probability conditions",
    ],
    key_concepts=["Inverse normal", "Percentage points", "x = μ + zσ", "Simultaneous equations for μ and σ"],
    blocks=[
        H("Introduction"),
        T(r"In the last lesson you were given a value and found a probability. Many practical questions go the other way: \"What mark must a student reach to be in the top 10%?\" or \"What mass should the machine be set to so that only 5% of bags are underweight?\". Here the **probability is given** and you must find the **value**, or find the unknown parameters $\mu$ and $\sigma$."),
        T(r"The method is always: **sketch, find $z$ from the probability, then write the equation $z = \dfrac{x - \mu}{\sigma}$**."),
        H("Finding z from a probability"),
        T(r"The table of $\Phi(z)$ can be read backwards, but for most probabilities you will not find the exact number and would need to interpolate. For this reason the examination tables include a short table of **percentage points**: the value $z$ with $\Phi(z) = p$ for common $p$. A calculator's \"inverse normal\" key does the same. Here is the table, computed with Python."),
        CODE(_pp_table(), "text", title="Percentage points: Φ(z) = p (4 decimal places)",
             caption="Example: for the top 10% the area to the left is p = 0.90, so z = 1.2816. For p below 0.5 use symmetry: z for p = 0.3 is minus z for p = 0.7, that is −0.5244."),
        KEY("From probability to value", r"Make sure the area in the table is the area to the **left**.", cards=[
            ["Top $q$ of the values", r"Area to the left is $1 - q$. Use $p = 1 - q$, then $x = \mu + z\sigma$."],
            ["Bottom $q$", r"Area to the left is $q$. If $q < 0.5$ then $z$ is negative: $z = -z_{1-q}$."],
            ["Symmetric middle", r"The middle 95% leaves 2.5% in each tail, so use $p = 0.975$, $z = 1.96$, and the interval $\mu \pm 1.96\sigma$."],
        ]),
        IMG("apostu1-normal-tail.svg", alt="A bell-shaped curve centred on 58 with the area to the right of 78.5 shaded and labelled 10 percent; the area to the left is labelled 90 percent.",
            caption="Figure 1. X ~ N(58, 16²). The top 10% starts at a, where the area to the left is 0.90, so z = 1.2816 and a = 78.5."),
        EX("Worked example 1: a cut-off value", intro=r"Marks in an examination are $X \sim N(58, 16^2)$ (invented for practice). The top 10% of candidates get a distinction. Find the lowest mark for a distinction.", steps=[
            S("Write the condition and sketch", math=r"P(X > a) = 0.10 \;\Rightarrow\; P(X < a) = 0.90"),
            S("Percentage point for $p = 0.90$", math=r"z = 1.2816"),
            S("Convert back to a mark", math=r"a = \mu + z\sigma = 58 + 1.2816 \times 16 = 78.5 \text{ (1 d.p.)}"),
        ], check=r"z = \frac{78.5 - 58}{16} = 1.281, \quad 1 - \Phi(1.28) = 0.1003 \approx 0.10"),
        H("Finding an unknown σ or μ"),
        T(r"When one of $\mu$ or $\sigma$ is unknown, the given probability gives one equation. Standardise the boundary value, find $z$ from the probability, and solve for the unknown. Be careful with the sign of $z$: a value **below** the mean has a **negative** $z$."),
        EX("Worked example 2: finding σ", intro=r"The journey time $X$ hours of a lorry from Douala to Yaoundé is normal with mean 4.8. It is known that 10% of journeys take longer than 5.5 hours (invented for practice). Find $\sigma$.", steps=[
            S("Condition", math=r"P(X > 5.5) = 0.10 \;\Rightarrow\; P(X < 5.5) = 0.90"),
            S("Percentage point", math=r"\frac{5.5 - 4.8}{\sigma} = 1.2816"),
            S("Solve", math=r"\sigma = \frac{0.7}{1.2816} = 0.546 \text{ hours (3 s.f.)}"),
        ], check=r"4.8 + 1.2816 \times 0.5462 = 5.5000"),
        MISTAKE("Wrong sign for z", r"If the given value is below the mean, the probability to its left is less than 0.5 and $z$ is **negative**. Writing $\frac{x - \mu}{\sigma} = +0.8416$ for $P(X < 40) = 0.2$ gives a negative $\sigma$, or a nonsense answer. Check: is the value on the correct side of the mean?"),
        H("Two unknowns: μ and σ together"),
        T(r"If both are unknown you need two conditions. Each gives one equation of the form $x = \mu + z\sigma$, and you solve the pair as **simultaneous equations**. Do not try to divide: subtract the equations to eliminate $\mu$."),
        EX("Worked example 3: finding both parameters", intro=r"The length $X$ cm of fish of a certain kind is normal. 10% are shorter than 30 cm and 20% are longer than 50 cm (invented for practice). Find $\mu$ and $\sigma$.", steps=[
            S("First condition: $P(X < 30) = 0.10$ so $z$ is negative", math=r"\frac{30 - \mu}{\sigma} = -1.2816 \;\Rightarrow\; \mu - 1.2816\sigma = 30"),
            S("Second condition: $P(X > 50) = 0.20$, so $P(X < 50) = 0.80$", math=r"\frac{50 - \mu}{\sigma} = 0.8416 \;\Rightarrow\; \mu + 0.8416\sigma = 50"),
            S("Subtract the first equation from the second", math=r"(0.8416 + 1.2816)\sigma = 20 \;\Rightarrow\; \sigma = \frac{20}{2.1232} = 9.42"),
            S("Substitute back", math=r"\mu = 30 + 1.2816 \times 9.4197 = 42.1"),
        ], check=r"\mu + 0.8416\sigma = 42.07 + 7.93 = 50.00 \text{ and } \mu - 1.2816\sigma = 42.07 - 12.07 = 30.00"),
        TIP(r"Exam link: inverse normal questions, including two-unknown problems, are a typical longer question in the statistics papers. Keep $z$ to 4 decimal places from the percentage-points table or calculator, and round only the final answer. Check the exact format with your teacher."),
        QUIZ(r"$X \sim N(\mu, 10^2)$ and $P(X < 40) = 0.2$. Which equation is correct, given $\Phi^{-1}(0.8) = 0.8416$?",
             [r"$\dfrac{40 - \mu}{10} = 0.8416$", r"$\dfrac{40 - \mu}{10} = 0.2$", r"$\dfrac{40 - \mu}{10} = -0.8416$", r"$\dfrac{\mu - 40}{10} = -0.8416$"], 2,
             r"$P(Z < z) = 0.2$ gives $z = -0.8416$. So $\frac{40 - \mu}{10} = -0.8416$ and $\mu = 48.416$. The value 40 is below the mean.",
             hint=r"Is the area to the left of 40 more or less than 0.5? What does that say about the sign of z?",
             feedback=["Positive z would put 40 above the mean, but only 20% lie below it.", "That sets z equal to the probability: the table gives z, not probability.", "", "That has the wrong sign: it would give mu below 40."]),
        QUIZ(r"The middle 90% of a $N(\mu, \sigma^2)$ distribution lies between",
             [r"$\mu \pm 1.2816\sigma$", r"$\mu \pm 1.96\sigma$", r"$\mu \pm 1.6449\sigma$", r"$\mu \pm 0.9\sigma$"], 2,
             r"The middle 90% leaves 5% in each tail, so $p = 0.95$ and $z = 1.6449$.",
             hint=r"How much probability is left in each tail?",
             feedback=["That is for the top 10% only (one tail).", "That is the middle 95%.", "", "0.9 is a probability, not a z value."]),
        PQ(r"$X \sim N(80, 12^2)$. Find $a$ such that $P(X > a) = 0.05$.",
           r"$P(X < a) = 0.95$, $z = 1.6449$. $a = 80 + 1.6449 \times 12 = 99.7$."),
        PQ(r"$X \sim N(120, \sigma^2)$ and $P(X < 100) = 0.1587$. Find $\sigma$.",
           r"From the table $\Phi(1) = 0.8413$, so $P(Z < -1) = 0.1587$. Then $\frac{100 - 120}{\sigma} = -1$ and $\sigma = 20$."),
        PQ(r"$X \sim N(\mu, \sigma^2)$ with $P(X < 40) = 0.1587$ and $P(X < 70) = 0.9772$. Find $\mu$ and $\sigma$.",
           r"From the table $\Phi(-1) = 0.1587$ and $\Phi(2) = 0.9772$. So $40 = \mu - \sigma$ and $70 = \mu + 2\sigma$. Subtract: $30 = 3\sigma$, so $\sigma = 10$ and $\mu = 50$."),
        PQ(r"Bag masses are $N(50.2, 0.4^2)$ kg. Find the limits symmetrical about the mean that contain the middle 95% of bags.",
           r"$z = 1.96$ (from $p = 0.975$). Limits $50.2 \pm 1.96 \times 0.4 = 50.2 \pm 0.784$, that is 49.42 kg to 50.98 kg."),
        SUM(r"Work backwards: sketch, find the area to the **left**, read $z$ from the percentage-points table or inverse normal key, then $x = \mu + z\sigma$.",
            r"Below the mean means negative $z$; the middle 95% uses $z = 1.96$ and the middle 90% uses $z = 1.6449$.",
            r"One unknown parameter gives one equation; two unknowns give two equations, solved simultaneously.",
            r"Keep $z$ to four decimal places and round only the final answer."),
    ],
))

# ---------------------------------------------------------------- 5. Normal approximations
LESSONS.append(lesson(
    module=M_DIST,
    topic="Normal approximations",
    title="Normal approximations to the binomial and Poisson, with continuity correction",
    slug="stu1-normal-approximations",
    minutes=24,
    summary="Approximate B(n, p) by N(np, npq) and Po(λ) by N(λ, λ) when the conditions hold, state the conditions precisely, and apply the continuity correction.",
    objectives=[
        "State the conditions under which a binomial or Poisson distribution can be approximated by a normal distribution",
        "Write down the mean and variance of the approximating normal distribution",
        "Apply the continuity correction correctly to each type of inequality",
        "Compare the approximation with the exact value",
    ],
    key_concepts=["Normal approximation", "Conditions: n large, np and nq large", "Continuity correction", "Approximating Poisson"],
    blocks=[
        H("Introduction"),
        T(r"A binomial probability such as $P(X \geq 58)$ for $X \sim B(100, 0.5)$ needs 43 separate terms: far too long by hand. Look at the bar chart of a binomial distribution with large $n$: the bars follow a bell-shaped curve. This is why a normal distribution can be used to **approximate** the binomial, and in the same way the Poisson distribution with a large mean."),
        D(r"If $X \sim B(n, p)$ with $q = 1 - p$, and **$n$ is large and $p$ is not close to 0 or 1** (a common rule is $np > 5$ and $nq > 5$; some textbooks use 10), then $X$ is approximately normal:", title="Normal approximation to the binomial",
          formula=r"X \approx Y \sim N(np,\; npq)",
          note="Check your textbook for the numerical rule. The Board's 2023 report says examiners expected precise conditions, not just 'n is large' and 'p is small'. Always give both conditions and show the numbers."),
        D(r"If $X \sim \text{Po}(\lambda)$ with **$\lambda$ large** (a common rule is $\lambda > 10$; check your textbook), then", title="Normal approximation to the Poisson",
          formula=r"X \approx Y \sim N(\lambda,\; \lambda)",
          note=r"The Poisson mean and variance are both $\lambda$, so the normal mean and variance are both $\lambda$."),
        T(r"Notice the behaviour of $p$. If $p$ is small (say 0.02) the binomial is very lopsided and the normal curve fits badly, whatever $n$ is. For a rare event with $n$ large and $np$ moderate, a Poisson model is better. A common error in the Board's report is to treat the probability of success as the wrong value, so identify $p$ carefully before testing the conditions."),
        H("The continuity correction"),
        T(r"The binomial and Poisson variables take whole-number values; the normal variable is continuous. In the bar chart the bar for $X = 12$ occupies the interval from 11.5 to 12.5 on the number line. So when you replace the bars with a smooth area, you must use the **boundaries 11.5 and 12.5**. This adjustment of $\pm 0.5$ is the **continuity correction**. The Board's 2023 report notes that candidates frequently failed to use it."),
        IMG("apostu1-approx-bars.svg", alt="Bars of B(20, 0.5) with a normal curve of mean 10 and variance 5 drawn over them. The bars for 12 and above are dark. A dashed line at 11.5 marks the left edge of the bar for 12.",
            caption="Figure 1. P(X ≥ 12) is the area of the dark bars, which starts at 11.5. So P(X ≥ 12) ≈ P(Y > 11.5)."),
        KEY("Continuity correction rules", r"Think about which bars you want, then find the outer edge of the first and last bar. Always sketch.", cards=[
            [r"$P(X \leq k)$", r"$P(Y < k + 0.5)$"],
            [r"$P(X < k)$", r"$P(Y < k - 0.5)$"],
            [r"$P(X \geq k)$", r"$P(Y > k - 0.5)$"],
            [r"$P(X > k)$", r"$P(Y > k + 0.5)$"],
            [r"$P(X = k)$", r"$P(k - 0.5 < Y < k + 0.5)$"],
            [r"$P(a \leq X \leq b)$", r"$P(a - 0.5 < Y < b + 0.5)$"],
        ], note="Some books state the rules differently; the idea of using the outer edges of the bars is the same."),
        EX("Worked example 1: binomial, upper tail and a single value", intro=r"At a district hospital, each of 100 births is a girl with probability 0.5 (assumed; invented for practice). Let $X$ be the number of girls. Find (a) $P(X \geq 58)$, (b) $P(X = 50)$.", steps=[
            S("Check the conditions", math=r"X \sim B(100, 0.5), \quad np = 50 > 5, \quad nq = 50 > 5", text=r"n is large and p is not close to 0 or 1, so the approximation is suitable."),
            S("State the approximating distribution", math=r"X \approx Y \sim N(50, 25), \qquad \sigma = 5"),
            S("(a) Continuity correction: $X \\geq 58$ starts at 57.5", math=r"P(X \geq 58) \approx P(Y > 57.5) = P\left(Z > \frac{57.5 - 50}{5}\right) = P(Z > 1.5) = 1 - 0.9332 = 0.0668"),
            S("(b) Continuity correction: $X = 50$ is the interval 49.5 to 50.5", math=r"P(49.5 < Y < 50.5) = P(-0.1 < Z < 0.1) = 0.5398 - 0.4602 = 0.0796"),
        ], check=r"\text{Exact binomial values: } 0.0666 \text{ and } 0.0796"),
        MISTAKE("Leaving out the continuity correction", r"Using $P(Y > 58)$ instead of $P(Y > 57.5)$ gives $z = 1.6$ and $0.0548$, which is clearly different from the exact $0.0666$. The correction matters most when the variance is small."),
        EX("Worked example 2: Poisson", intro=r"The number $X$ of customers per day at a market stall is $\text{Po}(25)$ (invented for practice). Use a normal approximation to find $P(X \leq 20)$.", steps=[
            S("Condition and distribution", math=r"\lambda = 25 \text{ is large}, \quad X \approx Y \sim N(25, 25), \quad \sigma = 5"),
            S("Continuity correction: $X \\leq 20$ ends at 20.5", math=r"P(X \leq 20) \approx P(Y < 20.5) = P\left(Z < \frac{20.5 - 25}{5}\right) = P(Z < -0.9)"),
            S("Symmetry and the table", math=r"= 1 - \Phi(0.9) = 1 - 0.8159 = 0.1841"),
        ], check=r"\text{The exact Poisson value is } 0.1855"),
        EX("Worked example 3: a range", intro=r"A fair coin is tossed 400 times (a model, invented for practice). Find the probability that the number of heads is from 190 to 215 inclusive.", steps=[
            S("Check and approximate", math=r"X \sim B(400, 0.5): \; np = 200, \; nq = 200 \;\Rightarrow\; Y \sim N(200, 100), \; \sigma = 10"),
            S("Both ends: 190 starts at 189.5 and 215 ends at 215.5", math=r"P(189.5 < Y < 215.5) = P(-1.05 < Z < 1.55)"),
            S("Subtract", math=r"= \Phi(1.55) - \Phi(-1.05) = 0.9394 - 0.1469 = 0.7925"),
        ], check=r"\text{Exact: } 0.7926"),
        CODE("""Comparison of the approximation with the exact value (4 d.p.)

Question                               Exact     Normal
B(100, 0.5)  P(X >= 58)                0.0666    0.0668
B(100, 0.5)  P(X = 50)                 0.0796    0.0796
Po(25)       P(X <= 20)                0.1855    0.1841
B(400, 0.5)  P(190 <= X <= 215)        0.7926    0.7925""", "text", title="Exact values computed with Python, normal values from the table above"),
        TIP(r"Exam link: normal approximations are examined in the statistics papers and sometimes in the multiple-choice Paper 1. Write: the conditions with their values, the approximating distribution with its mean and **variance**, the continuity correction, then the standardised value. Check the exact format with your teacher."),
        QUIZ(r"$X \sim B(60, 0.4)$. Which statement about approximating $P(X > 30)$ is correct?",
             [r"Not suitable because $n = 60$ is small.", r"Suitable: $X \approx N(24, 14.4)$, and $P(X > 30) \approx P(Y > 30.5)$.",
              r"Suitable: $X \approx N(24, 14.4)$, and $P(X > 30) \approx P(Y > 29.5)$.", r"Suitable: $X \approx N(24, 24)$, and $P(X > 30) \approx P(Y > 30.5)$."], 1,
             r"$np = 24 > 5$ and $nq = 36 > 5$, so use $N(24, 14.4)$. 'More than 30' means 31 or more, so the bars start at 30.5.",
             hint=r"Find np and nq, then npq for the variance. Which whole number is the first bar you want?",
             feedback=["The conditions are about np and nq, which are 24 and 36: both large.", "", "29.5 would include the bar for 30, which is not wanted.", "The variance is npq = 24 x 0.6 = 14.4, not np."]),
        QUIZ(r"Why is a normal approximation unsuitable for $X \sim B(500, 0.004)$?",
             [r"$n$ is too large.", r"$np = 2$ is small and the distribution is very skewed.", r"The binomial is never approximated by the normal.", r"$p$ must be greater than 0.5."], 1,
             r"The mean $np = 2$ is small, so most of the probability is on 0, 1, 2, 3 and the shape is lopsided, not bell-shaped. A Poisson model with $\lambda = 2$ would be better.",
             hint=r"Work out np and nq and compare them with 5.",
             feedback=["A large n helps; it is not the problem.", "", "It can be, when the conditions are met.", "p only needs to be not too close to 0 or 1; it need not exceed 0.5."]),
        PQ(r"$X \sim B(300, 0.25)$. Use a normal approximation to find (a) $P(X \leq 82)$, (b) $P(X \geq 68)$. State the conditions.",
           r"$np = 75 > 5$, $nq = 225 > 5$, so $X \approx Y \sim N(75, 56.25)$, $\sigma = 7.5$. (a) $P(Y < 82.5)$, $z = 1$: $0.8413$. (b) $P(Y > 67.5)$, $z = -1$: $1 - \Phi(-1) = 0.8413$. (Exact values: 0.8414 and 0.8414.)"),
        PQ(r"The number of customers per day at a stall is $\text{Po}(49)$ (invented). Estimate the probability that between 46 and 59 customers inclusive come in a day.",
           r"$Y \sim N(49, 49)$, $\sigma = 7$. $P(45.5 < Y < 59.5)$: $z_1 = -0.5$, $z_2 = 1.5$. $\Phi(1.5) - \Phi(-0.5) = 0.9332 - 0.3085 = 0.6247$. (The exact Poisson value is 0.6148, so the approximation is rough but acceptable.)"),
        PQ(r"State, with reasons, whether a normal approximation is suitable for (a) $B(40, 0.5)$, (b) $B(40, 0.05)$. For the suitable one, give the approximating distribution.",
           r"(a) $np = 20$ and $nq = 20$ are both greater than 5, so suitable: $N(20, 10)$. (b) $np = 2 < 5$, so not suitable (the distribution is very skewed)."),
        PQ(r"$X \sim B(100, 0.5)$. Find $P(45 < X \leq 55)$ using a normal approximation.",
           r"$Y \sim N(50, 25)$. $X \geq 46$ starts at 45.5 and $X \leq 55$ ends at 55.5: $P(45.5 < Y < 55.5)$, $z = -0.9$ and $1.1$. $\Phi(1.1) - \Phi(-0.9) = 0.8643 - 0.1841 = 0.6802$."),
        SUM(r"$B(n, p)$ is approximately $N(np, npq)$ when $n$ is large and $np$ and $nq$ are both large; $\text{Po}(\lambda)$ is approximately $N(\lambda, \lambda)$ for large $\lambda$. Give the numbers when stating conditions.",
            r"The second parameter of the normal is the **variance**: $npq$ for the binomial.",
            r"The continuity correction uses the outer edges of the bars: add or subtract 0.5 according to the inequality, and sketch to check.",
            r"If $np$ is small, a binomial is better treated with the Poisson distribution, not the normal."),
    ],
))

# ---------------------------------------------------------------- 6. Correlation
def _sums_table(xs, ys):
    rows = ["  x     y     x^2     y^2      xy"]
    for a, b in zip(xs, ys):
        rows.append(f"{a:3d}   {b:3d}   {a * a:5d}   {b * b:6d}   {a * b:6d}")
    rows.append("-" * 38)
    rows.append(f"{sum(xs):3d}   {sum(ys):3d}   {sum(a * a for a in xs):5d}   {sum(b * b for b in ys):6d}   {sum(a * b for a, b in zip(xs, ys)):6d}")
    return "\n".join(rows)


LESSONS.append(lesson(
    module=M_REG,
    topic="Correlation",
    title="Scatter diagrams and the product-moment correlation coefficient",
    slug="stu1-correlation-pmcc",
    minutes=24,
    summary="Draw and describe scatter diagrams, calculate the product-moment correlation coefficient r from Sxx, Syy and Sxy, and interpret it without confusing correlation with cause.",
    objectives=[
        "Describe a scatter diagram: direction, strength and shape",
        "Calculate Sxx, Syy, Sxy and r from raw data or from summary statistics",
        "State the range of r and what values near −1, 0 and 1 mean",
        "Interpret r in context and explain why correlation does not prove cause",
    ],
    key_concepts=["Scatter diagram", "Positive and negative correlation", "Sxx, Syy, Sxy", "Product-moment correlation coefficient r", "Correlation and cause"],
    blocks=[
        H("Introduction"),
        T(r"Do students who study more hours get higher marks? A teacher at a lycée in Bafoussam records, for eight students, the hours of study per week ($x$) and the mark in a test ($y$) (data invented for practice). To see whether there is a relationship, we plot one point for each student: a **scatter diagram**. To measure the strength of the relationship with one number we use the **product-moment correlation coefficient** $r$, often written PMCC."),
        IMG("apostu1-scatter-hours.svg", alt="Scatter diagram of eight points with hours of study from 0 to 14 on the horizontal axis and test mark from 20 to 80 on the vertical axis. The points rise from lower left to upper right with some scatter. The mean point (6.75, 57) is marked.",
            caption="Figure 1. The points rise from left to right: positive correlation. The mean point (x-bar, y-bar) lies in the middle of the cloud."),
        H("Describing a scatter diagram"),
        KEY("Direction, strength, shape", r"Describe three things.", cards=[
            ["Positive correlation", r"As $x$ increases, $y$ tends to increase. The points rise to the right."],
            ["Negative correlation", r"As $x$ increases, $y$ tends to decrease. The points fall to the right."],
            ["No correlation", r"No pattern: the points look like a random cloud, $r$ is close to 0."],
            ["Strength", r"The closer the points lie to a straight line, the stronger the correlation."],
        ]),
        H("The correlation coefficient"),
        T(r"We measure how far $x$ and $y$ vary together using three sums of squares and products. For $n$ pairs of values:"),
        F(r"S_{xx} = \sum x^2 - \frac{(\sum x)^2}{n}, \qquad S_{yy} = \sum y^2 - \frac{(\sum y)^2}{n}, \qquad S_{xy} = \sum xy - \frac{\sum x \sum y}{n}"),
        D(r"The **product-moment correlation coefficient** is", title="PMCC", formula=r"r = \frac{S_{xy}}{\sqrt{S_{xx}\,S_{yy}}}",
          note=r"$S_{xx}$ and $S_{yy}$ are never negative. The sign of $r$ is the sign of $S_{xy}$."),
        KEY("Properties of r", r"These facts are used in many exam questions.", cards=[
            ["Range", r"$-1 \leq r \leq 1$. A value outside this range is a calculation error."],
            ["$r = 1$ or $r = -1$", r"All points lie exactly on a straight line (rising for $+1$, falling for $-1$)."],
            ["$r$ near 0", r"No **linear** relationship. There may still be a curved relationship."],
            ["Unchanged by coding", r"Adding a number to every $x$, or multiplying by a **positive** number, does not change $r$. Multiplying by a negative number changes its sign."],
        ]),
        CODE(_sums_table([2, 3, 5, 6, 7, 9, 10, 12], [45, 38, 58, 47, 66, 60, 72, 70]), "text", title="Working table for the eight students (columns computed with Python)",
             caption="The last row gives: sum x = 54, sum y = 456, sum x^2 = 448, sum y^2 = 27 082, sum xy = 3338, with n = 8."),
        EX("Worked example 1: calculating r", intro=r"Use the sums above ($n = 8$, $\sum x = 54$, $\sum y = 456$, $\sum x^2 = 448$, $\sum y^2 = 27\,082$, $\sum xy = 3338$) to find $r$.", steps=[
            S("$S_{xx}$", math=r"S_{xx} = 448 - \frac{54^2}{8} = 448 - 364.5 = 83.5"),
            S("$S_{yy}$", math=r"S_{yy} = 27\,082 - \frac{456^2}{8} = 27\,082 - 25\,992 = 1090"),
            S("$S_{xy}$", math=r"S_{xy} = 3338 - \frac{54 \times 456}{8} = 3338 - 3078 = 260"),
            S("Put them in the formula", math=r"r = \frac{260}{\sqrt{83.5 \times 1090}} = \frac{260}{301.69} = 0.862 \text{ (3 s.f.)}"),
            S("Interpret in context", text=r"There is a strong positive linear correlation between hours of study and test mark for these students: students who study more hours tend to score higher."),
        ], check=r"\text{A calculator's statistics mode gives } r = 0.8618"),
        MISTAKE("Correlation is not cause", r"A high $r$ shows that two variables move together. It does not show that one **causes** the other. Both may depend on a third factor: for example, the number of motorbikes and the number of phone-credit shops in a town both rise with the size of the population. Say 'is associated with' or 'tends to', and in context."),
        MISTAKE("Using r when the pattern is curved", r"If the points follow a clear curve (for example a U shape), $r$ can be close to 0 even though the relationship is very strong. Always look at the scatter diagram before quoting $r$. Outliers can also change $r$ a lot."),
        EX("Worked example 2: negative correlation from summary statistics", intro=r"A trader records the price $x$ (FCFA per kg) and the quantity sold $y$ (kg) of tomatoes on $n = 10$ days (invented). $\sum x = 500$, $\sum y = 620$, $\sum x^2 = 25\,360$, $\sum y^2 = 38\,850$, $\sum xy = 30\,710$. Find $r$ and interpret it.", steps=[
            S("Sums of squares", math=r"S_{xx} = 25\,360 - \frac{500^2}{10} = 360, \qquad S_{yy} = 38\,850 - \frac{620^2}{10} = 410"),
            S("Sum of products", math=r"S_{xy} = 30\,710 - \frac{500 \times 620}{10} = 30\,710 - 31\,000 = -290"),
            S("Correlation coefficient", math=r"r = \frac{-290}{\sqrt{360 \times 410}} = \frac{-290}{384.19} = -0.755"),
            S("Interpret", text=r"There is a moderate to strong negative linear correlation: on days when the price was higher, the quantity sold tended to be lower. This does not prove that the price caused the change in sales."),
        ]),
        EX("Worked example 3: effect of coding", intro=r"For the eight students, $r = 0.862$ between hours $x$ and mark $y$ (out of 100). What is $r$ between $x$ and $y' = y/5$ (the mark out of 20), and between $x$ and $w = 100 - y$ (marks lost)?", steps=[
            S("Dividing by a positive number does not change $r$", math=r"r(x, y') = 0.862"),
            S("$w = 100 - y$ reverses the direction because $y$ is multiplied by $-1$", math=r"r(x, w) = -0.862"),
        ], check=r"\text{Computed directly: } r(x, y/5) = 0.8618, \quad r(x, 100 - y) = -0.8618"),
        TIP(r"Exam link: correlation appears in the statistics papers as a calculation of $r$ from given sums, with an interpretation in context. The Board's 2023 report gives the regression lines as a recurring difficulty, so keep $S_{xx}$, $S_{yy}$ and $S_{xy}$ clearly labelled. State the strength and direction, and avoid 'causes'. Check the exact format with your teacher."),
        QUIZ(r"Which of these cannot be a value of the product-moment correlation coefficient?",
             ["−0.95", "0", "1.2", "0.03"], 2,
             r"$r$ always satisfies $-1 \leq r \leq 1$, so 1.2 must contain an error.",
             hint=r"Recall the range of r.",
             feedback=["That is allowed: strong negative correlation.", "That is allowed: no linear correlation.", "", "That is allowed: almost no linear correlation."]),
        QUIZ(r"The points on a scatter diagram form a clear U shape (a symmetrical curve). The value of $r$ is most likely",
             ["close to 1", "close to −1", "close to 0, although there is a strong relationship", "exactly 0.5"], 2,
             r"The relationship is strong but not linear, and the rising and falling parts cancel in $S_{xy}$, so $r$ is near 0. This is why you must look at the scatter diagram.",
             hint=r"r measures only straight-line (linear) relationships.",
             feedback=["The points do not lie near a rising line.", "The points do not lie near a falling line.", "", "There is no reason for this value."]),
        PQ(r"For some data $S_{xx} = 40$, $S_{yy} = 90$ and $S_{xy} = 48$. Find $r$ and describe the correlation.",
           r"$r = \dfrac{48}{\sqrt{40 \times 90}} = \dfrac{48}{60} = 0.8$. A strong positive linear correlation."),
        PQ(r"Five pairs of values: $x = 1, 2, 3, 4, 5$ and $y = 2, 4, 5, 4, 5$. Calculate $r$.",
           r"$\sum x = 15$, $\sum y = 20$, $\sum x^2 = 55$, $\sum y^2 = 86$, $\sum xy = 66$. $S_{xx} = 55 - 45 = 10$, $S_{yy} = 86 - 80 = 6$, $S_{xy} = 66 - 60 = 6$. $r = \dfrac{6}{\sqrt{60}} = 0.775$."),
        PQ(r"A student finds $r = 0.85$ between the number of motorbikes and the number of phone-credit shops in 12 towns. She says more motorbikes cause more shops. Comment.",
           r"$r = 0.85$ shows a strong positive linear correlation: towns with more motorbikes tend to have more shops. It does not show cause: both are likely to depend on the size of the town's population."),
        PQ(r"$r = -0.6$ between $x$ and $y$. Write down $r$ between $u = 3 - 2x$ and $y$, explaining your answer.",
           r"$u = 3 - 2x$ multiplies $x$ by a negative number, which reverses the direction. The size is unchanged: $r = +0.6$."),
        SUM(r"A scatter diagram shows direction (positive or negative), strength and shape; look at it before quoting $r$.",
            r"$r = \dfrac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}$ with $S_{xx} = \sum x^2 - \frac{(\sum x)^2}{n}$, and similarly for $S_{yy}$ and $S_{xy}$.",
            r"$-1 \leq r \leq 1$; values near $\pm 1$ mean a strong linear relationship, near 0 means none; coding with a positive multiplier does not change $r$.",
            r"Correlation does not prove cause: interpret in context with 'tends to'."),
    ],
))

# ---------------------------------------------------------------- 7. Regression lines
LESSONS.append(lesson(
    module=M_REG,
    topic="Regression lines",
    title="Least-squares regression lines: y on x, prediction and its limits",
    slug="stu1-regression-lines",
    minutes=24,
    summary="Find the least-squares regression line of y on x, interpret its gradient and intercept, predict by interpolation, and avoid extrapolation and the wrong choice between the line of y on x and of x on y.",
    objectives=[
        "Calculate the regression line y = a + bx from raw data or summary statistics",
        "Interpret the gradient and intercept in context",
        "Predict values by interpolation and explain why extrapolation is unreliable",
        "Choose between the regression line of y on x and the line of x on y",
    ],
    key_concepts=["Least squares", "Regression line of y on x", "Gradient b = Sxy/Sxx", "Interpolation and extrapolation", "Line of x on y"],
    blocks=[
        H("Introduction"),
        T(r"A roadside stall in Maroua sells cold drinks. Over seven days the owner records the midday temperature $x$ (in degrees Celsius) and the number of bottles sold $y$ (data invented for practice). The points lie close to a rising line. If a hot day is forecast, how many bottles should the owner stock? We need the **equation of the line that best fits the points**."),
        D(r"The **regression line of $y$ on $x$** is the line $y = a + bx$ that minimises the sum of the squares of the **vertical** distances from the points to the line (the **least-squares** line). It is used to predict $y$ from a given $x$. The variable $x$ is the **independent** (or explanatory) variable and $y$ is the **dependent** (or response) variable.", title="Regression line",
          formula=r"b = \frac{S_{xy}}{S_{xx}}, \qquad a = \bar{y} - b\bar{x}"),
        T(r"Because $a = \bar{y} - b\bar{x}$, the line passes through the **mean point** $(\bar{x}, \bar{y})$. This is a good check on any line you draw."),
        IMG("apostu1-regression.svg", alt="Scatter diagram of temperature (20 to 40 degrees) against bottles sold. Seven points lie close to the rising line y = 1.90x - 32.8, which passes through the mean point. Short vertical segments join points to the line. The parts of the line outside the data range are dashed.",
            caption="Figure 1. The regression line of y on x. The short vertical segments are the distances whose squares are minimised. The dashed parts are outside the range of the data."),
        EX("Worked example 1: finding the line", intro=r"The data are: $x$: 24, 26, 28, 29, 31, 33, 35 and $y$: 14, 17, 21, 19, 27, 28, 36. Here $n = 7$, $\sum x = 206$, $\sum y = 162$, $\sum x^2 = 6152$, $\sum y^2 = 4096$, $\sum xy = 4938$. Find the regression line of $y$ on $x$.", steps=[
            S("$S_{xx}$", math=r"S_{xx} = 6152 - \frac{206^2}{7} = 89.714"),
            S("$S_{xy}$", math=r"S_{xy} = 4938 - \frac{206 \times 162}{7} = 170.571"),
            S("Gradient", math=r"b = \frac{S_{xy}}{S_{xx}} = \frac{170.571}{89.714} = 1.9013"),
            S("Means", math=r"\bar{x} = \frac{206}{7} = 29.429, \qquad \bar{y} = \frac{162}{7} = 23.143"),
            S("Intercept", math=r"a = \bar{y} - b\bar{x} = 23.143 - 1.9013 \times 29.429 = -32.81"),
            S("Write the line", math=r"y = -32.81 + 1.90x \quad (3 \text{ s.f.})"),
        ], check=r"\text{At } x = \bar{x}: -32.81 + 1.9013 \times 29.429 = 23.14 = \bar{y}"),
        H("Interpreting the line"),
        T(r"The **gradient** $b = 1.90$ means: for each extra degree in the midday temperature, about 1.9 more bottles are sold, on average. The **intercept** $a = -32.8$ would be the number of bottles sold at 0 degrees, which is impossible (negative) and far outside the data, so it has no practical meaning. The sign of $b$ is always the sign of $r$."),
        KEY("Interpolation and extrapolation", r"Predictions are safest inside the range of the data.", cards=[
            ["Interpolation", r"Predicting $y$ for an $x$ **inside** the range of the data (here 24 to 35 degrees). Usually reliable if $r$ is close to $\pm 1$."],
            ["Extrapolation", r"Predicting **outside** the range (for example 40 degrees). Unreliable: we do not know that the straight-line pattern continues."],
        ]),
        EX("Worked example 2: predictions", intro=r"Using the line $y = -32.81 + 1.9013x$, estimate the bottles sold when the temperature is (a) 30 degrees, (b) 40 degrees. Comment on each. (c) Estimate the temperature on a day when 20 bottles were sold.", steps=[
            S("(a) Interpolation, since 24 < 30 < 35", math=r"y = -32.81 + 1.9013 \times 30 = 24.2", text=r"About 24 bottles. This is a reasonable estimate."),
            S("(b) Extrapolation, since 40 is outside the data", math=r"y = -32.81 + 1.9013 \times 40 = 43.2", text=r"About 43 bottles, but unreliable: at very high temperatures sales may level off, or the stall may run out of stock."),
            S("(c) We want $x$ from $y$, so use the regression line of $x$ on $y$", math=r"x = \bar{x} + \frac{S_{xy}}{S_{yy}}(y - \bar{y}) = 29.429 + 0.4918 \times (20 - 23.143) = 27.9", text=r"Here $S_{yy} = 4096 - 162^2/7 = 346.857$ and $S_{xy}/S_{yy} = 0.4918$."),
        ]),
        H("Two regression lines"),
        T(r"There are **two** different regression lines for the same data. The line of $y$ on $x$ minimises the vertical distances and predicts $y$ from $x$. The line of $x$ on $y$ minimises the **horizontal** distances and predicts $x$ from $y$:"),
        F(r"x = c + dy, \quad d = \frac{S_{xy}}{S_{yy}}, \quad c = \bar{x} - d\bar{y}"),
        T(r"Both pass through $(\bar{x}, \bar{y})$ but have different gradients (unless $r = \pm 1$, when they are the same line). A useful check is $b \times d = r^2$. For the stall: $1.9013 \times 0.4918 = 0.935 = 0.9669^2$."),
        MISTAKE("Mixing up the two lines", r"The Board's 2023 report notes candidates taking the regression lines of $y$ on $x$ and $x$ on $y$ the wrong way round. Ask: which variable do I want to **find**? Predict $y$ from a given $x$: use $y$ on $x$. Predict $x$ from a given $y$: use $x$ on $y$. Rearranging the line of $y$ on $x$ to get $x$ is **not** the same, and gives a slightly different (and less accurate) answer: here it gives 27.8 instead of 27.9."),
        MISTAKE("Extrapolating and ignoring context", r"A negative number of bottles, or a prediction for 60 degrees, is not meaningful. Always check that $x$ is inside the data range and that the answer makes sense (a count cannot be negative, and should be rounded to a whole number if the question is about whole items)."),
        EX("Worked example 3: from summary statistics", intro=r"For $n = 10$ pairs, $\bar{x} = 12$, $\bar{y} = 40$, $S_{xx} = 150$ and $S_{xy} = -420$. Find the regression line of $y$ on $x$ and estimate $y$ when $x = 10$.", steps=[
            S("Gradient", math=r"b = \frac{-420}{150} = -2.8"),
            S("Intercept, using the mean point", math=r"a = 40 - (-2.8)(12) = 73.6"),
            S("Line and prediction", math=r"y = 73.6 - 2.8x, \qquad x = 10:\ y = 73.6 - 28 = 45.6"),
        ], check=r"\text{The gradient is negative, matching the negative } S_{xy} \text{ (negative correlation)}"),
        TIP(r"Exam link: regression lines are examined in the statistics papers: find the line, interpret $b$, predict, and comment on reliability. The Board's 2023 report mentions the confusion between the two lines. Say 'regression line of y on x' in your answer. Check the exact format with your teacher."),
        QUIZ(r"The regression line of $y$ on $x$ is $y = 3 + 2x$ and $\bar{x} = 5$. What is $\bar{y}$?",
             ["10", "13", "8", "7"], 1,
             r"The line passes through the mean point, so $\bar{y} = 3 + 2 \times 5 = 13$.",
             hint=r"Which point must the regression line always pass through?",
             feedback=["That is 2 × 5, forgetting the intercept 3.", "", "That is 3 + 5, forgetting to multiply by the gradient.", "That is 2 + 5, mixing up a and b."]),
        QUIZ(r"The regression line of $y$ on $x$ was found from values of $x$ between 10 and 50. The best description of using it for $x = 120$ is",
             ["interpolation, which is reliable", "extrapolation, which is unreliable", "interpolation, which is unreliable", "extrapolation, which is reliable"], 1,
             r"120 is outside the range 10 to 50, so this is extrapolation. We do not know the pattern continues, so the estimate is unreliable.",
             hint=r"Is 120 inside or outside the data range?",
             feedback=["It is outside the range, so it is not interpolation.", "", "It is outside the range, so it is not interpolation.", "Extrapolation is generally unreliable."]),
        PQ(r"For $n = 10$ pairs: $\sum x = 100$, $\sum y = 250$, $\sum x^2 = 1100$, $\sum xy = 2700$. Find the regression line of $y$ on $x$ and interpret the gradient.",
           r"$S_{xx} = 1100 - 1000 = 100$, $S_{xy} = 2700 - 2500 = 200$. $b = 2$. $\bar{x} = 10$, $\bar{y} = 25$, $a = 25 - 20 = 5$. The line is $y = 5 + 2x$. Gradient: on average $y$ increases by 2 for each increase of 1 in $x$."),
        PQ(r"For the data in the previous question, $\sum y^2 = 6850$. Find $r$, and the regression line of $x$ on $y$. Check that $b \times d = r^2$.",
           r"$S_{yy} = 6850 - 6250 = 600$. $r = 200/\sqrt{100 \times 600} = 0.8165$. $d = 200/600 = \frac{1}{3}$, $c = 10 - \frac{25}{3} = \frac{5}{3}$, so $x = \frac{5}{3} + \frac{1}{3}y$. Check: $2 \times \frac{1}{3} = 0.6667 = 0.8165^2$."),
        PQ(r"Five pairs: $x = 1, 2, 3, 4, 5$ and $y = 2, 4, 5, 4, 5$. Find the regression line of $y$ on $x$ and estimate $y$ for $x = 3.5$.",
           r"$S_{xx} = 10$, $S_{xy} = 6$, so $b = 0.6$. $\bar{x} = 3$, $\bar{y} = 4$, $a = 4 - 1.8 = 2.2$. Line: $y = 2.2 + 0.6x$. For $x = 3.5$: $y = 2.2 + 2.1 = 4.3$ (interpolation, so reasonable)."),
        PQ(r"A line $y = -32.8 + 1.90x$ (temperature $x$, bottles $y$, data range 24 to 35 degrees) is used to predict sales at 20 degrees. Calculate the prediction and comment.",
           r"$y = -32.8 + 38 = 5.2$, about 5 bottles. 20 degrees is outside the range 24 to 35, so this is extrapolation and unreliable: for a lower temperature the straight-line pattern may not continue (for example, sales cannot go below zero)."),
        SUM(r"The regression line of $y$ on $x$ is $y = a + bx$ with $b = \dfrac{S_{xy}}{S_{xx}}$ and $a = \bar{y} - b\bar{x}$; it passes through $(\bar{x}, \bar{y})$.",
            r"The gradient is the average change in $y$ for one unit of $x$; the intercept may have no practical meaning.",
            r"Interpolation (inside the data range) is reasonable; extrapolation is unreliable.",
            r"Use $y$ on $x$ to predict $y$, and $x$ on $y$ to predict $x$; the two lines differ unless $r = \pm 1$, and $b \times d = r^2$."),
    ],
))

# ---------------------------------------------------------------- 8. Rank correlation
LESSONS.append(lesson(
    module=M_REG,
    topic="Rank correlation",
    title="Spearman's rank correlation coefficient",
    slug="stu1-rank-correlation-spearman",
    minutes=22,
    summary="Rank data, including tied values, calculate Spearman's coefficient r_s = 1 − 6Σd²/(n(n² − 1)), interpret it, and decide when it is more suitable than the product-moment coefficient.",
    objectives=[
        "Rank a set of values, giving tied values their average rank",
        "Calculate Spearman's rank correlation coefficient from the differences in ranks",
        "Interpret r_s between −1 and +1",
        "Explain when rank correlation is more suitable than the PMCC",
    ],
    key_concepts=["Ranking", "Tied ranks", "Spearman's coefficient", "Differences in ranks d", "Monotonic relationship"],
    blocks=[
        H("Introduction"),
        T(r"Two buyers at a cocoa market each rank eight samples of beans from best (1) to worst (8). Do they agree? We cannot use the product-moment coefficient directly: the data are **ranks**, not measurements. **Spearman's rank correlation coefficient**, written $r_s$, measures how well two rankings agree."),
        T(r"It is also used when the data are measured, but the relationship is not a straight line, or there are extreme values, or only the order matters (for example subjective scores for a school talent contest)."),
        H("Ranking the data"),
        T(r"To rank, give rank 1 to the smallest value (or to the largest: **choose one direction and use it for both variables**), rank 2 to the next, and so on. If two or more values are **tied**, give each the **average** of the ranks they would have taken. For example, two values tied for 3rd and 4th place each get rank $3.5$."),
        D(r"For $n$ pairs of ranks, let $d$ be the difference between the two ranks of each pair. **Spearman's rank correlation coefficient** is", title="Spearman's coefficient", formula=r"r_s = 1 - \frac{6\sum d^2}{n(n^2 - 1)}",
          note=r"$-1 \leq r_s \leq 1$. A value of $+1$ means the rankings agree exactly, $-1$ means they are exactly opposite, and $0$ means no agreement. Some books write $n(n^2 - 1)$ as $n^3 - n$: they are the same."),
        EX("Worked example 1: two buyers", intro=r"Two buyers rank eight cocoa samples A to H (invented for practice). Find $r_s$.", steps=[
            S("Write the ranks and the differences", text=r"See the table below."),
            S("Square the differences and add", math=r"\sum d^2 = 1 + 0 + 1 + 4 + 1 + 4 + 4 + 1 = 16"),
            S("Substitute with $n = 8$", math=r"r_s = 1 - \frac{6 \times 16}{8 \times (64 - 1)} = 1 - \frac{96}{504} = 0.810 \text{ (3 s.f.)}"),
            S("Interpret", text=r"There is a strong positive agreement between the two buyers' rankings."),
        ], check=r"\frac{96}{504} = 0.1905, \quad 1 - 0.1905 = 0.8095"),
        CODE("""Sample   Buyer 1   Buyer 2    d    d^2
A           3         2       1     1
B           1         1       0     0
C           4         3       1     1
D           2         4      -2     4
E           6         5       1     1
F           5         7      -2     4
G           8         6       2     4
H           7         8      -1     1
                          sum d^2  = 16""", "text", title="Working for example 1"),
        MISTAKE("Forgetting a step in the arithmetic", r"The most common errors are: forgetting to **square** $d$ before adding (the sum of the plain differences is always 0), forgetting the 1 at the start (so that a good agreement gives a small answer), and ranking one variable from smallest and the other from largest, which reverses the sign. Check: $r_s$ must lie between $-1$ and $1$."),
        EX("Worked example 2: ranking measured data", intro=r"Six farms record the annual rainfall $x$ (mm) and the maize yield $y$ (tonnes per hectare) (invented for practice). $x$: 820, 640, 910, 700, 760, 980. $y$: 2.1, 1.4, 2.9, 1.8, 2.2, 2.6. Find $r_s$.", steps=[
            S("Rank $x$ from smallest to largest", math=r"x \text{ ranks: } 4, 1, 5, 2, 3, 6"),
            S("Rank $y$ in the same direction", math=r"y \text{ ranks: } 3, 1, 6, 2, 4, 5"),
            S("Differences $d$ and their squares", math=r"d = 1, 0, -1, 0, -1, 1 \;\Rightarrow\; \sum d^2 = 4"),
            S("Substitute with $n = 6$", math=r"r_s = 1 - \frac{6 \times 4}{6 \times 35} = 1 - \frac{24}{210} = 0.886"),
        ], check=r"\text{The product-moment coefficient of the ranks is also } 0.886"),
        H("Tied values"),
        EX("Worked example 3: ties", intro=r"Seven students have scores $x$: 12, 15, 15, 18, 20, 9, 16 in one test and $y$: 40, 55, 48, 62, 62, 35, 50 in another (invented). Find $r_s$.", steps=[
            S("Rank $x$ from smallest. The two 15s share ranks 3 and 4", math=r"x \text{ ranks: } 2, 3.5, 3.5, 6, 7, 1, 5"),
            S("Rank $y$. The two 62s share ranks 6 and 7", math=r"y \text{ ranks: } 2, 5, 3, 6.5, 6.5, 1, 4"),
            S("Differences and squares", math=r"d = 0, -1.5, 0.5, -0.5, 0.5, 0, 1 \;\Rightarrow\; \sum d^2 = 0 + 2.25 + 0.25 + 0.25 + 0.25 + 0 + 1 = 4"),
            S("Substitute with $n = 7$", math=r"r_s = 1 - \frac{6 \times 4}{7 \times 48} = 1 - \frac{24}{336} = 0.929"),
        ], check=r"\text{The exact product-moment coefficient of the ranks is } 0.927"),
        T(r"When there are ties, the formula above is only approximate. The exact value is the product-moment correlation coefficient of the two sets of ranks (here 0.927 against 0.929). Textbooks differ on which to use, so check your textbook and your teacher; the difference is small when there are few ties."),
        H("When to use rank correlation"),
        IMG("apostu1-rank-monotone.svg", alt="Scatter diagram with seven points rising along a curve that gets steeper, with x from 1 to 7 and y from about 1.5 to 25. A line joins the points to show the curve.",
            caption="Figure 1. y always increases when x increases, so the ranks agree exactly and r_s = 1. The points are not on a straight line, so the product-moment coefficient is only 0.90."),
        KEY("Choosing between r and r_s", r"Look at the data and the type of relationship.", cards=[
            ["Use $r$ (PMCC)", r"Measured values, with a roughly straight-line relationship and no extreme outliers."],
            ["Use $r_s$", r"Data that are ranks or scores where only the order is reliable; or a relationship that always rises (or always falls) but is curved; or data with extreme values."],
        ]),
        TIP(r"Exam link: rank correlation is part of the Correlation and Regression module. The part of the Board's 2023 report available for 0770 does not single this topic out, so check with your teacher how it appears. Show the ranks, $d$ and $d^2$ in a table, and interpret $r_s$ in context."),
        QUIZ(r"Two values are tied for 3rd and 4th place. What rank does each get?",
             ["3", "4", "3.5", "7"], 2,
             r"Tied values share the average of the ranks they would have occupied: $(3 + 4)/2 = 3.5$.",
             hint=r"They take up ranks 3 and 4 between them.",
             feedback=["That gives one of them an advantage.", "That gives one of them a disadvantage.", "", "That is the sum, not the average."]),
        QUIZ(r"Which situation is best suited to Spearman's coefficient?",
             ["Heights and masses of 40 adults, roughly linear", "Rankings given by two judges to ten singers", "Exact temperature and exact rainfall for 30 days", "Time and distance of a car at constant speed"], 1,
             r"Judges give ranks only, so the actual scores are not reliable measurements. The other situations give accurate measured values with a linear pattern, where the PMCC is suitable.",
             hint=r"Which data are already ranks?",
             feedback=["Measured and linear: PMCC is suitable.", "", "Measured values: PMCC is suitable if the pattern is linear.", "Exactly linear: PMCC is suitable (it would be 1)."]),
        PQ(r"For $n = 10$ pairs $\sum d^2 = 22$. Find $r_s$.",
           r"$r_s = 1 - \dfrac{6 \times 22}{10 \times 99} = 1 - \dfrac{132}{990} = 0.867$."),
        PQ(r"Hours of study $x$: 5, 3, 8, 6, 9, 2, 7, 4 and marks $y$: 60, 45, 70, 80, 75, 40, 55, 50. Find $r_s$.",
           r"Ranks of $x$: 4, 2, 7, 5, 8, 1, 6, 3. Ranks of $y$: 5, 2, 6, 8, 7, 1, 4, 3. $d = -1, 0, 1, -3, 1, 0, 2, 0$, $\sum d^2 = 1 + 0 + 1 + 9 + 1 + 0 + 4 + 0 = 16$. $r_s = 1 - \dfrac{96}{504} = 0.810$."),
        PQ(r"Two judges rank six dancers: judge P gives 1, 2, 3, 4, 5, 6 and judge Q gives 6, 5, 4, 3, 2, 1. Find $r_s$ and interpret.",
           r"$d = -5, -3, -1, 1, 3, 5$, $\sum d^2 = 25 + 9 + 1 + 1 + 9 + 25 = 70$. $r_s = 1 - \dfrac{6 \times 70}{6 \times 35} = 1 - 2 = -1$. The judges disagree completely: one ranking is the exact reverse of the other."),
        PQ(r"Explain why Spearman's coefficient might be better than the PMCC to compare a pupil's rankings in two subjects with 20 pupils, and state what $r_s = 0.9$ would show.",
           r"Rankings only show order, not the size of the differences in marks, so ranks are reliable but marks (which are on different scales) may not be linear in each other. $r_s = 0.9$ shows a strong positive agreement: pupils who rank high in one subject tend to rank high in the other."),
        SUM(r"Rank both variables in the same direction; tied values share the average rank.",
            r"$r_s = 1 - \dfrac{6\sum d^2}{n(n^2 - 1)}$, with $d$ the difference between the two ranks of each pair; $-1 \leq r_s \leq 1$.",
            r"Use $r_s$ for ranked data, for curved but always rising or falling relationships, or when there are extreme values.",
            r"With ties the formula is approximate; the exact value is the PMCC of the ranks. Check your textbook."),
    ],
))
