"""Practice sets for the Statistics option, Upper Sixth: Further Distributions, and Correlation & Regression.

All data are invented for practice. Normal-table values are the 4-decimal values of the table in the lessons.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-statistics", "upper-sixth")]

M_DIST = "Further Distributions"
M_REG = "Correlation & Regression"

SETS = []

# ---------------------------------------------------------------- 1. Poisson
SETS.append(practice_set(
    module=M_DIST, topic="The Poisson distribution",
    title="Poisson probabilities, parameters and sums",
    lesson="stu1-poisson-distribution",
    questions=[
        MC(r"A random variable $X \sim \text{Po}(\lambda)$. Which statement about its mean and variance is correct?", [
            C(r"The mean is $\lambda$ and the variance is $\lambda^2$.", why=r"This mixes up Poisson with the standard deviation: the standard deviation is $\sqrt{\lambda}$, and the variance is $\lambda$."),
            C(r"The mean and the variance are both equal to $\lambda$.", correct=True),
            C(r"The mean is $\lambda$ and the variance is $\sqrt{\lambda}$.", why=r"$\sqrt{\lambda}$ is the standard deviation, not the variance."),
            C(r"The mean is $np$ and the variance is $npq$.", why=r"Those are the binomial results. The Poisson distribution has no n and p."),
        ], steps=[S("Recall the property", math=r"E(X) = \text{Var}(X) = \lambda")],
           concept="Mean and variance of a Poisson variable", skill="Recall", hint=r"A special feature of Poisson: the mean equals one other quantity.",
           feedback=r"Mean equal to variance is also a quick test of whether data are Poisson."),
        NUM(r"$X \sim \text{Po}(2.5)$. Find $P(X = 3)$ to 4 decimal places.", 0.2138, steps=[
            S("Use the formula", math=r"P(X = 3) = \frac{e^{-2.5}\,2.5^3}{3!}"),
            S("Calculate", math=r"= \frac{0.082085 \times 15.625}{6} = 0.2138"),
        ], tolerance=0.0005, concept="Poisson probability from the formula", skill="Calculation", hint=r"Substitute lambda = 2.5 and r = 3 into e^(-lambda) lambda^r / r!."),
        MC(r"Customers reach a stall at an average of 12 per hour. $X$ is the number of customers in a 15-minute period. What is the distribution of $X$?", [
            C(r"$\text{Po}(12)$", why=r"12 is the rate per hour, but the question asks about 15 minutes."),
            C(r"$\text{Po}(15)$", why=r"15 is the length of the interval in minutes, not the average number."),
            C(r"$\text{Po}(0.25)$", why=r"This is 15/60, the fraction of an hour. It must be multiplied by the rate 12."),
            C(r"$\text{Po}(3)$", correct=True),
        ], steps=[S("Scale the rate to the interval", math=r"\lambda = 12 \times \frac{15}{60} = 3"), S("State", math=r"X \sim \text{Po}(3)")],
           concept="Matching the Poisson parameter to the interval", skill="Application", hint=r"What fraction of an hour is 15 minutes? Multiply the hourly rate by it.",
           feedback=r"The Board's 2023 report notes many candidates used the wrong Poisson parameter."),
        MC(r"$X \sim \text{Po}(1.5)$. Which expression and value give $P(X > 2)$?", [
            C(r"$1 - P(X \leq 2) = 0.191$", correct=True),
            C(r"$1 - P(X \leq 1) = 0.442$", why=r"That is $P(X \geq 2)$: it includes the value 2, but 'more than 2' does not."),
            C(r"$1 - P(X \leq 3) = 0.066$", why=r"That is $P(X \geq 4)$: it leaves out the value 3."),
            C(r"$P(X \leq 2) = 0.809$", why=r"That is the opposite event: 2 or fewer."),
        ], steps=[
            S("More than 2 means 3, 4, 5, ...: use the complement", math=r"P(X > 2) = 1 - P(X \leq 2)"),
            S("Sum the three terms", math=r"P(X \leq 2) = e^{-1.5}\left(1 + 1.5 + 1.125\right) = 0.8088"),
            S("Subtract from 1", math=r"1 - 0.8088 = 0.1912"),
        ], concept="Complement for 'more than' in a Poisson distribution", skill="Calculation", hint=r"Which values are NOT included in 'more than 2'? Take them away from 1.",
           feedback=r"Check the boundary: more than 2 is 3 or more; at least 2 is 2 or more."),
        NUM(r"Calls to an office occur at random, on average 6 per hour. Find the probability of at least one call in a 20-minute period, to 4 decimal places.", 0.8647, steps=[
            S("Scale the rate", math=r"\lambda = 6 \times \frac{20}{60} = 2"),
            S("At least one is the complement of none", math=r"P(X \geq 1) = 1 - e^{-2} = 1 - 0.1353 = 0.8647"),
        ], tolerance=0.0005, concept="Poisson: at least one in a scaled interval", skill="Application", hint=r"First find lambda for 20 minutes. At least one = 1 minus the chance of none."),
        MC(r"$X \sim \text{Po}(2)$ and $Y \sim \text{Po}(3.5)$ are independent. What is the distribution of $X + Y$?", [
            C(r"$\text{Po}(7)$", why=r"That multiplies the parameters (2 × 3.5). They must be added."),
            C(r"$\text{Po}(1.75)$", why=r"That is the mean of the two parameters. For a sum we add."),
            C(r"$\text{Po}(5.5)$", correct=True),
            C("It is not a Poisson distribution.", why=r"The sum of independent Poisson variables is Poisson; the parameters add."),
        ], steps=[S("Add the parameters of independent Poisson variables", math=r"X + Y \sim \text{Po}(2 + 3.5) = \text{Po}(5.5)")],
           concept="Sum of independent Poisson variables", skill="Concept", hint=r"Two independent streams of events combine into one stream with what rate?",
           feedback=r"Independence is essential for the sum rule."),
        NUM(r"$X \sim \text{Po}(\lambda)$ and $P(X = 0) = 0.3$. Find $\lambda$ to 3 decimal places.", 1.204, steps=[
            S("Write $P(X = 0)$", math=r"e^{-\lambda} = 0.3"),
            S("Take natural logarithms", math=r"\lambda = -\ln 0.3 = 1.204"),
        ], tolerance=0.002, concept="Finding the Poisson parameter from a probability", skill="Calculation", hint=r"P(X = 0) simplifies to e to the power minus lambda. Take logs."),
        MC(r"Ten counts of cars at a junction in one-minute periods (invented) have mean 4.1 and variance 9.8. Which is the best conclusion about a Poisson model?", [
            C("A Poisson model is clearly suitable because the mean is about 4.", why=r"A Poisson model needs the variance to be close to the mean, not just the mean to be positive."),
            C("A Poisson model is doubtful: the variance is much larger than the mean, suggesting that cars come in clusters.", correct=True),
            C("A Poisson model is suitable because the variance is bigger than the mean.", why=r"Bigger is not suitable: it should be about equal."),
            C("A Poisson model is impossible because the mean is not an integer.", why=r"The mean of a Poisson variable need not be an integer; only the values taken are integers."),
        ], steps=[S("Compare mean and variance", text=r"For a Poisson variable the mean equals the variance. Here 4.1 and 9.8 differ a lot."),
                  S("Conclude", text=r"The data are more spread out than Poisson, suggesting events that are not independent or not at a constant rate (clusters, such as vehicles in convoys).")],
           concept="Testing a Poisson model by comparing mean and variance", skill="Reasoning", hint=r"What do you expect the mean and variance to be for Poisson data?"),
    ]))

# ---------------------------------------------------------------- 2. Continuous random variables
SETS.append(practice_set(
    module=M_DIST, topic="Continuous random variables",
    title="Density functions, cumulative distribution functions, median and variance",
    lesson="stu1-continuous-random-variables",
    questions=[
        MC(r"Which of these must be true for a probability density function $f(x)$?", [
            C(r"$f(x) \leq 1$ for every $x$.", why=r"A density can exceed 1: for example $f(x) = 2$ on $0 \leq x \leq 0.5$ has total area 1. Only areas are probabilities."),
            C(r"$f(x) = P(X = x)$.", why=r"For a continuous variable $P(X = x) = 0$. The height $f(x)$ is a density, not a probability."),
            C(r"The total area under the curve is 1 and $f(x) \geq 0$.", correct=True),
            C(r"The values of $f(x)$ add up to 1.", why=r"That is the rule for a discrete distribution. For a continuous variable we integrate, not add."),
        ], steps=[S("Recall", text=r"A pdf is never negative, and the total area under it is 1: $\int f(x)\,dx = 1$.")],
           concept="Properties of a probability density function", skill="Recall", hint=r"Think of area, not height.",
           feedback=r"The Board's 2023 report notes candidates treating a continuous variable as discrete."),
        NUM(r"The pdf of $X$ is $f(x) = kx^2$ for $0 \leq x \leq 3$, and 0 otherwise. Find $k$ as a decimal to 3 decimal places.", 0.111, steps=[
            S("Total area equals 1", math=r"\int_0^3 kx^2\,dx = k\left[\frac{x^3}{3}\right]_0^3 = 9k = 1"),
            S("Solve", math=r"k = \frac{1}{9} = 0.111"),
        ], tolerance=0.001, concept="Finding the constant in a pdf", skill="Calculation", hint=r"Integrate over the stated range and set the result equal to 1."),
        MC(r"$X$ is a continuous random variable. Which statement is **true**?", [
            C(r"$P(X \leq 2) = P(X < 2)$", correct=True),
            C(r"$P(X = 2) = f(2)$", why=r"$f(2)$ is a density. A single point has no width, so $P(X = 2) = 0$."),
            C(r"$P(X \leq 2) = P(X < 2) + f(2)$", why=r"Adding a density to a probability mixes up different things: the single point contributes 0."),
            C(r"$P(X > 2) = P(X \geq 2) + 0.5$", why=r"Nothing like this holds. The two probabilities are equal."),
        ], steps=[S("A single value has probability zero", math=r"P(X = 2) = 0 \Rightarrow P(X \leq 2) = P(X < 2) + 0 = P(X < 2)")],
           concept="P(X = a) = 0 for continuous variables", skill="Concept", hint=r"What is the area of a strip of zero width?"),
        NUM(r"$X$ has pdf $f(x) = \dfrac{x}{2}$ for $0 \leq x \leq 2$ and 0 otherwise. Find $P(X > 1.2)$.", 0.64, steps=[
            S("Find the cdf", math=r"F(x) = \int_0^x \frac{t}{2}\,dt = \frac{x^2}{4}"),
            S("Upper tail", math=r"P(X > 1.2) = 1 - F(1.2) = 1 - \frac{1.44}{4} = 0.64"),
        ], tolerance=0.001, concept="Upper-tail probability from the cdf", skill="Calculation", hint=r"Integrate from 0 to x to get F, then use 1 minus F."),
        MC(r"$X$ has pdf $f(x) = \dfrac{3}{8}x^2$ for $0 \leq x \leq 2$. What is the median?", [
            C(r"$1.26$", why=r"This solves $m^3 = 2$, which would come from $F(m) = m^3/4$. Here $F(m) = m^3/8$, so $m^3 = 4$."),
            C(r"$1.5$", why=r"This is the mean $E(X)$, not the median."),
            C(r"$1$", why=r"This is the midpoint of the range. The distribution is not symmetrical, so the median is not at the midpoint."),
            C(r"$1.59$", correct=True),
        ], steps=[
            S("Find the cdf", math=r"F(x) = \int_0^x \tfrac{3}{8}t^2\,dt = \frac{x^3}{8}"),
            S("Set $F(m) = 0.5$", math=r"\frac{m^3}{8} = \frac{1}{2} \Rightarrow m^3 = 4"),
            S("Solve", math=r"m = 4^{1/3} = 1.587"),
        ], concept="Median of a continuous distribution", skill="Calculation", hint=r"The median m satisfies F(m) = 0.5."),
        NUM(r"$X$ has pdf $f(x) = \dfrac{x}{2}$ for $0 \leq x \leq 2$ and 0 otherwise. Find $\text{Var}(X)$ to 3 decimal places.", 0.222, steps=[
            S("Mean", math=r"E(X) = \int_0^2 \frac{x^2}{2}\,dx = \frac{4}{3}"),
            S("Second moment", math=r"E(X^2) = \int_0^2 \frac{x^3}{2}\,dx = 2"),
            S("Variance", math=r"\text{Var}(X) = 2 - \left(\frac{4}{3}\right)^2 = \frac{2}{9} = 0.222"),
        ], tolerance=0.001, concept="Variance of a continuous variable", skill="Calculation", hint=r"Find E(X) and E(X squared) by integrating x f(x) and x squared f(x)."),
        MC(r"$X$ has cdf $F(x) = 0$ for $x < 1$, $F(x) = \dfrac{x^2 - 1}{8}$ for $1 \leq x \leq 3$ and $F(x) = 1$ for $x > 3$. What is the pdf for $1 \leq x \leq 3$?", [
            C(r"$\dfrac{x^2 - 1}{8}$", why=r"That is the cdf itself. The pdf is the derivative of the cdf."),
            C(r"$\dfrac{x}{4}$", correct=True),
            C(r"$\dfrac{x^3}{24} - \dfrac{x}{8}$", why=r"This integrates F instead of differentiating it. The pdf is the derivative."),
            C(r"$\dfrac{1}{8}$", why=r"This would be the derivative if F were $x/8$. The derivative of $x^2/8$ is $x/4$."),
        ], steps=[S("Differentiate", math=r"f(x) = \frac{dF}{dx} = \frac{2x}{8} = \frac{x}{4}"), S("Check", text=r"The area is F(3) − F(1) = 1 − 0 = 1.")],
           concept="Finding f(x) from F(x) by differentiation", skill="Concept", hint=r"Which operation takes you from F back to f?"),
        MC(r"The diagram shows the pdf of $X$: a triangle on $0 \leq x \leq 4$ with peak height $k$ at $x = 2$, and $f(x) = 0$ elsewhere. What is the value of $k$?", [
            C(r"$0.25$", why=r"This takes the area as $4k = 1$: the triangle's area is $\frac{1}{2} \times 4 \times k$, not $4 \times k$."),
            C(r"$1$", why=r"This would give an area of 2, not 1."),
            C(r"$0.5$", correct=True),
            C(r"$2$", why=r"That would give an area of 4. The area must be 1."),
        ], steps=[S("Area of the triangle equals 1", math=r"\tfrac{1}{2} \times 4 \times k = 1"), S("Solve", math=r"k = 0.5")],
           concept="Total area 1 for a triangular density", skill="Application", hint=r"What is the formula for the area of a triangle? Set it equal to 1.",
           diagram="apostu1-q-density.svg", diagram_alt="A triangular density curve on 0 to 4, rising from 0 at x = 0 to a peak of height k at x = 2 and falling to 0 at x = 4. The peak height k is not given."),
    ]))

# ---------------------------------------------------------------- 3. Normal distribution: tables
SETS.append(practice_set(
    module=M_DIST, topic="The normal distribution",
    title="Standardising and using the table of the normal distribution",
    lesson="stu1-normal-distribution-tables",
    questions=[
        MC(r"$X \sim N(60, 16)$. What is the standardised value of $x = 66$?", [
            C(r"$z = 0.375$", why=r"That divides by the variance 16. The standard deviation is $\sqrt{16} = 4$."),
            C(r"$z = 1.5$", correct=True),
            C(r"$z = 6$", why=r"That subtracts the mean but does not divide by the standard deviation."),
            C(r"$z = 16.5$", why=r"That divides 66 by 4 without subtracting the mean."),
        ], steps=[S("The variance is 16, so $\\sigma = 4$", math=r"z = \frac{66 - 60}{4} = 1.5")],
           concept="Standardising with the standard deviation", skill="Calculation", hint=r"The second number in N(mu, sigma squared) is the variance. What is sigma?"),
        NUM(r"$X \sim N(50, 10^2)$. Use the table of $\Phi(z)$ to find $P(X < 65)$ to 4 decimal places.", 0.9332, steps=[
            S("Standardise", math=r"z = \frac{65 - 50}{10} = 1.5"),
            S("Read the table", math=r"P(X < 65) = \Phi(1.5) = 0.9332"),
        ], tolerance=0.0005, concept="P(X < a) from the table", skill="Calculation", hint=r"Standardise first, then read the table row for 1.5."),
        MC(r"$X \sim N(30, 4^2)$. Which is $P(X < 26)$, given $\Phi(1) = 0.8413$?", [
            C(r"$0.1587$", correct=True),
            C(r"$0.8413$", why=r"This is $\Phi(1)$, the area for +1. The value 26 is below the mean, so $z = -1$."),
            C(r"$0.3413$", why=r"This is the area between the mean and $z = 1$ ($0.8413 - 0.5$), not the tail."),
            C(r"$0.0228$", why=r"This is $P(Z < -2)$. Here $z = (26 - 30)/4 = -1$, not $-2$."),
        ], steps=[S("Standardise", math=r"z = \frac{26 - 30}{4} = -1"), S("Use symmetry", math=r"P(Z < -1) = 1 - \Phi(1) = 1 - 0.8413 = 0.1587")],
           concept="Negative z and symmetry", skill="Calculation", hint=r"Is 26 above or below the mean? What does that do to the sign of z?"),
        NUM(r"$X \sim N(100, 20^2)$. Find $P(90 < X < 120)$ to 4 decimal places, using the table.", 0.5328, steps=[
            S("Standardise both ends", math=r"z_1 = \frac{90 - 100}{20} = -0.5, \qquad z_2 = \frac{120 - 100}{20} = 1"),
            S("Subtract", math=r"\Phi(1) - \Phi(-0.5) = 0.8413 - (1 - 0.6915) = 0.8413 - 0.3085 = 0.5328"),
        ], tolerance=0.0005, concept="Probability between two values", skill="Calculation", hint=r"Standardise both ends and subtract the smaller area from the larger."),
        MC(r"$X \sim N(20, 9)$. Which is the correct value of $P(X > 23)$?", [
            C(r"$0.8413$", why=r"This is $\Phi(1) = P(X < 23)$. For 'greater than' you must subtract from 1."),
            C(r"$0.3707$", why=r"This divides by the variance 9 ($z = 0.33$) instead of the standard deviation 3."),
            C(r"$0.1587$", correct=True),
            C(r"$0.0013$", why=r"This takes $z = 3$: the mean was subtracted but the division by $\sigma$ was forgotten."),
        ], steps=[S("The variance is 9 so $\\sigma = 3$", math=r"z = \frac{23 - 20}{3} = 1"), S("Upper tail", math=r"P(X > 23) = 1 - \Phi(1) = 0.1587")],
           concept="Upper-tail probability, variance versus standard deviation", skill="Calculation", hint=r"Take the square root of the variance first."),
        NUM(r"The masses of bags are $N(50.2, 0.4^2)$ kg. A depot packs 5000 bags. Use $P(X < 50) = 0.3085$ to estimate how many are under 50 kg.", 1542.5, steps=[
            S("Expected number is $n \\times$ probability", math=r"5000 \times 0.3085 = 1542.5"),
            S("Round sensibly", text=r"About 1540 bags (the answer is an estimate).")],
           tolerance=1, concept="Expected number from a normal probability", skill="Application", hint=r"Multiply the number of bags by the probability of one bag being under 50 kg."),
        MC(r"The diagram shows the curve of $X \sim N(40, 6^2)$. The point $a = 44.2$ is marked and the area to its right is shaded. Which is the shaded area? (Use $\Phi(0.7) = 0.7580$.)", [
            C(r"$0.7580$", why=r"That is the area to the **left** of $a$, the unshaded part."),
            C(r"$0.2580$", why=r"That is the area between the mean and $a$ ($0.7580 - 0.5$), not the tail."),
            C(r"$0.2420$", correct=True),
            C(r"$0.4522$", why=r"This divides by the variance 36 instead of the standard deviation 6, giving $z = 0.12$."),
        ], steps=[S("Standardise", math=r"z = \frac{44.2 - 40}{6} = 0.7"), S("Upper tail", math=r"1 - \Phi(0.7) = 1 - 0.7580 = 0.2420")],
           concept="Reading a shaded area from a diagram", skill="Interpretation", hint=r"Is the shaded region the area to the left or to the right of a?",
           diagram="apostu1-q-normal-shaded.svg", diagram_alt="A bell-shaped curve with the mean marked by a dashed line and a point a to the right of the mean. The area to the right of a is shaded."),
        MC(r"$X \sim N(100, 15^2)$. Between which two values do about 68% of the values lie?", [
            C(r"70 and 130", why=r"That is two standard deviations either side (about 95%)."),
            C(r"92.5 and 107.5", why=r"That is half a standard deviation either side: this contains about 38% only."),
            C(r"100 and 115", why=r"That is only from the mean to one standard deviation above: about 34%."),
            C(r"85 and 115", correct=True),
        ], steps=[S("About 68% lie within one standard deviation of the mean", math=r"100 \pm 15 = 85 \text{ to } 115"), S("Check", math=r"\Phi(1) - \Phi(-1) = 0.8413 - 0.1587 = 0.6826")],
           concept="Within one standard deviation of the mean", skill="Concept", hint=r"68% corresponds to z from −1 to +1."),
    ]))

# ---------------------------------------------------------------- 4. Normal distribution: inverse problems
SETS.append(practice_set(
    module=M_DIST, topic="The normal distribution",
    title="Inverse normal problems and finding the mean and standard deviation",
    lesson="stu1-normal-distribution-inverse",
    questions=[
        MC(r"For $Z \sim N(0, 1)$, which value of $z$ has $P(Z > z) = 0.05$?", [
            C(r"$1.6449$", correct=True),
            C(r"$1.96$", why=r"That is the value for $P(Z > z) = 0.025$, that is the middle 95% (two tails of 2.5%)."),
            C(r"$0.95$", why=r"0.95 is the area to the left, not the value of z."),
            C(r"$-1.6449$", why=r"That has 5% to its left, not to its right."),
        ], steps=[S("The area to the left is 0.95", math=r"P(Z < z) = 0.95 \Rightarrow z = 1.6449")],
           concept="Percentage point for an upper tail", skill="Recall", hint=r"Convert the tail area to the area on the left, then use the percentage-points table."),
        NUM(r"Marks are $X \sim N(70, 8^2)$. The top 10% of candidates get a distinction. Find the lowest mark for a distinction (to 1 decimal place).", 80.3, steps=[
            S("Area to the left is 0.90", math=r"z = 1.2816"),
            S("Convert to a mark", math=r"a = 70 + 1.2816 \times 8 = 80.25 \approx 80.3")],
           tolerance=0.06, concept="Finding a value from an upper-tail probability", skill="Calculation", hint=r"Top 10% means 90% lies below. Use x = mean + z times sigma."),
        MC(r"$X \sim N(\mu, \sigma^2)$ and $P(X < a) = 0.2$. Given $\Phi^{-1}(0.8) = 0.8416$, which equation is correct?", [
            C(r"$\dfrac{a - \mu}{\sigma} = 0.8416$", why=r"This has the wrong sign: only 20% lie below $a$, so $a$ is below the mean and $z$ is negative."),
            C(r"$\dfrac{a - \mu}{\sigma} = 0.2$", why=r"This puts the probability in place of $z$. The table gives $z$, not a probability."),
            C(r"$\dfrac{a - \mu}{\sigma} = -0.8416$", correct=True),
            C(r"$\dfrac{\mu - a}{\sigma} = -0.8416$", why=r"This has the wrong sign again: it would put $a$ above the mean."),
        ], steps=[S("20% below means $a$ is below the mean, so $z < 0$", math=r"z = -\Phi^{-1}(0.8) = -0.8416"), S("Write the equation", math=r"\frac{a - \mu}{\sigma} = -0.8416")],
           concept="Sign of z for a lower tail", skill="Concept", hint=r"Is a above or below the mean if only 20% of values are below it?"),
        NUM(r"$X \sim N(100, \sigma^2)$ and $P(X < 85) = 0.0668$. Use $\Phi(1.5) = 0.9332$ to find $\sigma$.", 10, steps=[
            S("Symmetry", math=r"P(Z < -1.5) = 1 - 0.9332 = 0.0668 \Rightarrow z = -1.5"),
            S("Equation", math=r"\frac{85 - 100}{\sigma} = -1.5 \Rightarrow \sigma = 10")],
           tolerance=0.01, concept="Finding sigma from a probability", skill="Calculation", hint=r"Which z value has 0.0668 below it?"),
        MC(r"For a normal distribution, the middle 99% of values lie within how many standard deviations of the mean?", [
            C(r"$1.96$", why=r"That is for the middle 95%."),
            C(r"$2.5758$", correct=True),
            C(r"$2.3263$", why=r"That is $P(Z < z) = 0.99$, which leaves 1% in one tail only: the middle would be 98%."),
            C(r"$0.99$", why=r"0.99 is a probability, not a number of standard deviations."),
        ], steps=[S("0.5% in each tail, so the area to the left is 0.995", math=r"z = 2.5758")],
           concept="Percentage point for a central interval", skill="Concept", hint=r"How much probability is left in each tail?"),
        NUM(r"$X$ is normal. $P(X < 25) = 0.0228$ and $P(X > 45) = 0.1587$. Find $\sigma$ to 2 decimal places.", 6.67, steps=[
            S("From the table", math=r"\Phi(-2) = 0.0228 \Rightarrow \frac{25 - \mu}{\sigma} = -2; \qquad P(X < 45) = 0.8413 \Rightarrow \frac{45 - \mu}{\sigma} = 1"),
            S("Write as equations", math=r"\mu - 2\sigma = 25, \qquad \mu + \sigma = 45"),
            S("Subtract", math=r"3\sigma = 20 \Rightarrow \sigma = 6.67 \text{ and } \mu = 38.33")],
           tolerance=0.01, concept="Two conditions: simultaneous equations for mu and sigma", skill="Reasoning", hint=r"Turn each probability into a z value, then write two equations in mu and sigma."),
        MC(r"Bag masses are $N(120, 10^2)$ g (invented). Which limits, symmetrical about the mean, contain the middle 90% of the masses?", [
            C(r"100.4 g and 139.6 g", why=r"This uses $z = 1.96$, the value for the middle 95%."),
            C(r"107.2 g and 132.8 g", why=r"This uses $z = 1.2816$, which cuts off 10% in one tail, not 5% in each."),
            C(r"110 g and 130 g", why=r"This is one standard deviation each side, which contains only about 68%."),
            C(r"103.6 g and 136.4 g", correct=True),
        ], steps=[S("5% in each tail so $p = 0.95$", math=r"z = 1.6449"), S("Limits", math=r"120 \pm 1.6449 \times 10 = 103.55 \text{ to } 136.45")],
           concept="Symmetrical interval containing a given probability", skill="Application", hint=r"What area is to the left of the upper limit?"),
        MC(r"A machine fills bags with mass $N(\mu, 4^2)$ g. The target is that only 2.5% of bags are under 500 g. What should $\mu$ be?", [
            C(r"507.8 g", correct=True),
            C(r"492.2 g", why=r"This subtracts instead of adds. 500 is the lower limit, so the mean must be **above** 500."),
            C(r"502.0 g", why=r"This adds 1.96 g, forgetting to multiply by $\sigma = 4$."),
            C(r"504.0 g", why=r"This uses $z = 1$, which is about 15.9% below, not 2.5%."),
        ], steps=[S("2.5% below 500 so the area to the left is 0.025", math=r"\frac{500 - \mu}{4} = -1.96"), S("Solve", math=r"\mu = 500 + 1.96 \times 4 = 507.84")],
           concept="Setting a mean to meet a tail condition", skill="Application", hint=r"Is the mean above or below the lower limit? How many sigma?"),
    ]))

# ---------------------------------------------------------------- 5. Normal approximations
SETS.append(practice_set(
    module=M_DIST, topic="Normal approximations",
    title="Conditions, parameters and continuity correction",
    lesson="stu1-normal-approximations",
    questions=[
        MC(r"Which statement gives the conditions under which $B(n, p)$ may be approximated by a normal distribution? (Check your textbook for the numerical rule.)", [
            C(r"$n$ is large.", why=r"This is not enough: with $p$ very small the binomial is very lopsided, however large $n$ is."),
            C(r"$n$ is large and $p$ is small.", why=r"This is the condition for a **Poisson** approximation, not a normal one. The Board expects more than 'n large, p small'."),
            C(r"$n$ is large and $p$ is not near 0 or 1, for example $np > 5$ and $nq > 5$.", correct=True),
            C(r"$np < 5$ and $nq < 5$.", why=r"The mean np must be large enough: the conditions are np > 5 and nq > 5 (some books use 10)."),
        ], steps=[S("State the conditions with numbers", text=r"The binomial is approximately normal when n is large and p is not close to 0 or 1: np > 5 and nq > 5, with q = 1 − p.")],
           concept="Conditions for the normal approximation to the binomial", skill="Recall", hint=r"Both np and nq must be large, so that the distribution is not lopsided.",
           feedback=r"The Board's 2023 report says precise conditions were expected."),
        NUM(r"$X \sim B(100, 0.5)$. Use a normal approximation with continuity correction to find $P(X \geq 58)$ to 3 decimal places.", 0.067, steps=[
            S("Approximating distribution", math=r"Y \sim N(50, 25), \; \sigma = 5"),
            S("Continuity correction", math=r"P(X \geq 58) \approx P(Y > 57.5), \quad z = \frac{57.5 - 50}{5} = 1.5"),
            S("Table", math=r"1 - 0.9332 = 0.0668 \approx 0.067")],
           tolerance=0.001, concept="Normal approximation to the binomial, upper tail", skill="Calculation", hint=r"At least 58 starts at the lower edge of the bar for 58."),
        MC(r"$X$ is a discrete variable and $Y$ is the normal approximation. Which is the correct continuity correction for $P(X < 30)$?", [
            C(r"$P(Y < 30.5)$", why=r"This includes the bar for 30. But $X < 30$ means 29 or fewer."),
            C(r"$P(Y < 29.5)$", correct=True),
            C(r"$P(Y < 30)$", why=r"This omits the continuity correction."),
            C(r"$P(Y > 29.5)$", why=r"This is the upper tail, the opposite event."),
        ], steps=[S("$X < 30$ means $X \\leq 29$, and the bar for 29 ends at 29.5", math=r"P(X < 30) = P(X \leq 29) \approx P(Y < 29.5)")],
           concept="Continuity correction for a strict inequality", skill="Concept", hint=r"Write the values X can take, then find the outer edge of the last bar."),
        NUM(r"$X \sim \text{Po}(49)$. Use a normal approximation to estimate $P(X \leq 52)$ to 3 decimal places.", 0.692, steps=[
            S("Approximating distribution", math=r"Y \sim N(49, 49), \; \sigma = 7"),
            S("Continuity correction", math=r"P(X \leq 52) \approx P(Y < 52.5), \quad z = \frac{52.5 - 49}{7} = 0.5"),
            S("Table", math=r"\Phi(0.5) = 0.6915 \approx 0.692")],
           tolerance=0.001, concept="Normal approximation to the Poisson", skill="Calculation", hint=r"The Poisson mean and variance are both lambda."),
        MC(r"$X \sim B(300, 0.25)$. Which normal distribution approximates $X$?", [
            C(r"$N(75, 75)$", why=r"This uses the variance equal to the mean, which is the Poisson rule. For the binomial the variance is npq."),
            C(r"$N(75, 7.5)$", why=r"7.5 is the **standard deviation** ($\sqrt{56.25}$ is 7.5). The second parameter must be the variance."),
            C(r"$N(0.25, 0.1875)$", why=r"These are the mean and variance of a single trial, not of 300 trials."),
            C(r"$N(75, 56.25)$", correct=True),
        ], steps=[S("Mean", math=r"np = 300 \times 0.25 = 75"), S("Variance", math=r"npq = 300 \times 0.25 \times 0.75 = 56.25")],
           concept="Mean and variance of the approximating normal", skill="Calculation", hint=r"Variance of a binomial: n p q."),
        NUM(r"$X \sim B(100, 0.5)$. Use a normal approximation to find $P(X = 55)$ to 4 decimal places.", 0.0484, steps=[
            S("Continuity correction for a single value", math=r"P(X = 55) \approx P(54.5 < Y < 55.5), \quad Y \sim N(50, 25)"),
            S("Standardise", math=r"z_1 = \frac{54.5 - 50}{5} = 0.9, \quad z_2 = \frac{55.5 - 50}{5} = 1.1"),
            S("Subtract", math=r"\Phi(1.1) - \Phi(0.9) = 0.8643 - 0.8159 = 0.0484")],
           tolerance=0.0005, concept="Single value with continuity correction", skill="Calculation", hint=r"A single value is a bar of width 1 centred on it."),
        MC(r"Which of these distributions **cannot** sensibly be approximated by a normal distribution?", [
            C(r"$B(500, 0.004)$", correct=True),
            C(r"$B(80, 0.5)$", why=r"np = 40 and nq = 40 are both large: the approximation is suitable."),
            C(r"$B(200, 0.4)$", why=r"np = 80 and nq = 120 are both large: the approximation is suitable."),
            C(r"$\text{Po}(30)$", why=r"The mean 30 is large, so a normal approximation is suitable."),
        ], steps=[S("Check np", math=r"500 \times 0.004 = 2 < 5"), S("Conclude", text=r"The mean is small, so the distribution is lopsided: a Poisson distribution with λ = 2 is better.")],
           concept="Recognising when the approximation fails", skill="Reasoning", hint=r"Work out np and nq for each distribution."),
        MC(r"A fair coin is tossed 400 times. Using a normal approximation, which is the probability of from 190 to 215 heads inclusive? (Use $\Phi(1.55) = 0.9394$, $\Phi(1.05) = 0.8531$.)", [
            C(r"$0.7745$", why=r"This uses 190 and 215 as the limits (no continuity correction)."),
            C(r"$0.7796$", why=r"This uses 189.5 and 214.5: the upper limit should be 215.5."),
            C(r"$0.7925$", correct=True),
            C(r"$0.7683$", why=r"This uses 190.5 and 215.5: the lower limit should be 189.5 to include the value 190."),
        ], steps=[
            S("Approximation", math=r"Y \sim N(200, 100), \; \sigma = 10"),
            S("Continuity correction: 190 to 215 inclusive", math=r"P(189.5 < Y < 215.5): \; z = -1.05 \text{ and } 1.55"),
            S("Subtract", math=r"0.9394 - (1 - 0.8531) = 0.9394 - 0.1469 = 0.7925")],
           concept="Range of values with continuity correction", skill="Application", hint=r"Both ends move outwards by 0.5 for an inclusive range."),
    ]))

# ---------------------------------------------------------------- 6. Correlation
SETS.append(practice_set(
    module=M_REG, topic="Correlation",
    title="Scatter diagrams, the correlation coefficient and its meaning",
    lesson="stu1-correlation-pmcc",
    questions=[
        MC(r"A scatter diagram shows points falling from top left to bottom right, close to a straight line, and $r = -0.92$. Which description is best?", [
            C("Strong positive linear correlation", why=r"Positive means that y increases with x. The points fall, so the correlation is negative."),
            C("Strong negative linear correlation", correct=True),
            C("Weak negative linear correlation", why=r"0.92 is close to 1 in size, so the correlation is strong, not weak."),
            C("No linear correlation", why=r"No correlation would give r near 0."),
        ], steps=[S("Sign and size", text=r"The sign is negative (points fall) and |r| = 0.92 is close to 1 (strong).")],
           concept="Describing correlation from r", skill="Interpretation", hint=r"Look at the sign for direction and the size for strength."),
        NUM(r"For some data $S_{xx} = 25$, $S_{yy} = 36$ and $S_{xy} = -27$. Find $r$.", -0.9, steps=[
            S("Formula", math=r"r = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} = \frac{-27}{\sqrt{25 \times 36}}"),
            S("Calculate", math=r"= \frac{-27}{30} = -0.9")],
           tolerance=0.001, concept="Calculating r from Sxx, Syy and Sxy", skill="Calculation", hint=r"Take the square root of the product of Sxx and Syy."),
        MC(r"The scatter diagram shows ten points. Which value is the best estimate of $r$?", [
            C(r"$+0.9$", why=r"The points fall to the right, so the correlation is negative."),
            C(r"$-0.5$", why=r"The points lie very close to a falling line: the correlation is much stronger than this."),
            C(r"$-0.1$", why=r"This would be a random cloud with almost no pattern."),
            C(r"$-0.95$", correct=True),
        ], steps=[S("Direction", text=r"The points fall from left to right: r is negative."), S("Strength", text=r"They lie very close to a straight line: |r| is close to 1, so about −0.95.")],
           concept="Estimating r from a scatter diagram", skill="Interpretation", hint=r"Is the pattern rising or falling? How tight is the cloud?",
           diagram="apostu1-q-scatter.svg", diagram_alt="Ten points falling from the top left to the bottom right, close to a straight line with a little scatter. The axes show no numbers."),
        NUM(r"Five pairs of values: $x = 2, 4, 6, 8, 10$ and $y = 9, 7, 8, 4, 2$. Calculate $r$ to 3 decimal places.", -0.922, steps=[
            S("Sums", math=r"\sum x = 30, \; \sum y = 30, \; \sum x^2 = 220, \; \sum y^2 = 214, \; \sum xy = 146"),
            S("Sums of squares and products", math=r"S_{xx} = 220 - 180 = 40, \; S_{yy} = 214 - 180 = 34, \; S_{xy} = 146 - 180 = -34"),
            S("Coefficient", math=r"r = \frac{-34}{\sqrt{40 \times 34}} = -0.922")],
           tolerance=0.001, concept="Calculating r from raw data", skill="Calculation", hint=r"Find the five sums first, then Sxx, Syy and Sxy."),
        MC(r"The correlation coefficient between $x$ and $y$ is $0.7$. What is the correlation coefficient between $2x - 1$ and $3 - y$?", [
            C(r"$-0.7$", correct=True),
            C(r"$0.7$", why=r"Multiplying y by −1 (in 3 − y) reverses the direction, so the sign changes."),
            C(r"$-1.4$", why=r"r cannot exceed 1 in size, and coding does not scale r by the multipliers."),
            C(r"$0.2$", why=r"This tries to apply the coding to r itself, which is not how r works. Adding and multiplying by positive numbers leaves r unchanged."),
        ], steps=[S("$2x - 1$ is a positive scaling and a shift: no change", text=r"r is unchanged by this."), S("$3 - y$ multiplies y by −1: the sign reverses", math=r"r = -0.7")],
           concept="Effect of coding on r", skill="Concept", hint=r"Which of the two codings reverses the direction of one variable?"),
        NUM(r"For $n = 10$ pairs, $\sum x = 60$, $\sum y = 120$, $\sum x^2 = 400$, $\sum y^2 = 1700$ and $\sum xy = 800$. Find $r$ to 3 decimal places.", 0.785, steps=[
            S("Sums of squares", math=r"S_{xx} = 400 - \frac{60^2}{10} = 40, \qquad S_{yy} = 1700 - \frac{120^2}{10} = 260"),
            S("Sum of products", math=r"S_{xy} = 800 - \frac{60 \times 120}{10} = 80"),
            S("Coefficient", math=r"r = \frac{80}{\sqrt{40 \times 260}} = \frac{80}{101.98} = 0.785")],
           tolerance=0.001, concept="r from summary statistics", skill="Calculation", hint=r"Use sum x squared minus (sum x) squared over n, and similar."),
        MC(r"A study finds $r = 0.9$ between the number of umbrellas sold and the number of colds treated at a clinic each week. Which comment is best?", [
            C("Selling umbrellas causes colds, because r is so close to 1.", why=r"A high r never proves cause."),
            C("Colds cause people to buy umbrellas.", why=r"This is also a causal claim with no support from r."),
            C("There is a strong positive association, but it does not prove cause: both may rise in the rainy season.", correct=True),
            C("There is no relationship because umbrellas cannot cause colds.", why=r"The data do show a strong association. The explanation, not the correlation, is the issue."),
        ], steps=[S("Interpret r", text=r"r = 0.9 is a strong positive linear association."), S("Warn about cause", text=r"Both variables probably depend on a third factor, the weather, so we cannot say one causes the other.")],
           concept="Correlation does not imply causation", skill="Reasoning", hint=r"Is there a third factor that could explain both?"),
        MC(r"The scatter diagram of a data set forms a clear U shape, and the calculated value is $r = 0.02$. Which conclusion is correct?", [
            C("There is no relationship between the variables.", why=r"The U shape shows a strong (curved) relationship, though not a linear one."),
            C("The data must contain an error, since r is so small.", why=r"There is no error: r measures only linear relationships."),
            C("There is a strong positive linear relationship.", why=r"r = 0.02 shows no linear relationship."),
            C("There is no linear relationship, but there may be a strong non-linear one.", correct=True),
        ], steps=[S("What r measures", text=r"r measures the strength of a straight-line relationship only."), S("Interpret", text=r"A U-shaped pattern has rising and falling parts that cancel, so r is near 0 even though the variables are related.")],
           concept="Limits of the product-moment coefficient", skill="Reasoning", hint=r"What kind of pattern does r measure?"),
    ]))

# ---------------------------------------------------------------- 7. Regression lines
SETS.append(practice_set(
    module=M_REG, topic="Regression lines",
    title="Regression lines of y on x and x on y, prediction and reliability",
    lesson="stu1-regression-lines",
    questions=[
        MC(r"Which point always lies on the regression line of $y$ on $x$?", [
            C(r"$(0, 0)$", why=r"The line has an intercept $a$ which is usually not 0."),
            C(r"The first data point.", why=r"The line is a best fit and need not pass through any data point."),
            C(r"The point where $x$ is largest.", why=r"Nothing makes the line pass through the extreme point."),
            C(r"The mean point $(\bar{x}, \bar{y})$.", correct=True),
        ], steps=[S("From the formula for the intercept", math=r"a = \bar{y} - b\bar{x} \;\Rightarrow\; \bar{y} = a + b\bar{x}")],
           concept="Regression line passes through the mean point", skill="Recall", hint=r"Look at how the intercept a is calculated."),
        NUM(r"For a data set $S_{xx} = 50$ and $S_{xy} = 120$. Find the gradient $b$ of the regression line of $y$ on $x$.", 2.4, steps=[
            S("Formula", math=r"b = \frac{S_{xy}}{S_{xx}} = \frac{120}{50} = 2.4")],
           tolerance=0.001, concept="Gradient b = Sxy/Sxx", skill="Calculation", hint=r"Which sum goes on the bottom for y on x?"),
        MC(r"The regression line of $y$ on $x$ is $y = 4 + 1.5x$ and $\bar{x} = 8$. What is $\bar{y}$?", [
            C(r"$16$", correct=True),
            C(r"$12$", why=r"This is 1.5 × 8, forgetting to add the intercept 4."),
            C(r"$9.5$", why=r"This adds the gradient to x-bar (1.5 + 8) instead of multiplying them."),
            C(r"$5.5$", why=r"This is a + b = 4 + 1.5, the value of y when x = 1, not at the mean."),
        ], steps=[S("The line passes through the mean point", math=r"\bar{y} = 4 + 1.5 \times 8 = 16")],
           concept="Using the mean point on the line", skill="Calculation", hint=r"Substitute the mean of x into the equation of the line."),
        NUM(r"For $n = 8$: $\sum x = 40$, $\sum y = 96$, $\sum x^2 = 240$ and $\sum xy = 520$. Find the regression line of $y$ on $x$ and use it to estimate $y$ when $x = 6$.", 13, steps=[
            S("Sums", math=r"S_{xx} = 240 - \frac{40^2}{8} = 40, \qquad S_{xy} = 520 - \frac{40 \times 96}{8} = 40"),
            S("Gradient and intercept", math=r"b = 1, \quad \bar{x} = 5, \; \bar{y} = 12, \quad a = 12 - 5 = 7"),
            S("Prediction", math=r"y = 7 + x = 13 \text{ when } x = 6")],
           tolerance=0.01, concept="Finding and using a regression line", skill="Calculation", hint=r"Find Sxx and Sxy, then b, then a using the means."),
        MC(r"The line $y = 20 + 4x$ links hours of study per week $x$ to the mark $y$ in a test, from data with $x$ between 2 and 12. What does the gradient 4 mean?", [
            C(r"A student who does no study scores 4.", why=r"That would be the intercept, and it is 20, not 4."),
            C(r"Each extra hour of study is associated with an average increase of 4 marks.", correct=True),
            C(r"Each extra mark needs 4 more hours of study.", why=r"This reverses the variables: the gradient is marks per hour, not hours per mark."),
            C(r"Every student who studies 4 hours gets a full mark.", why=r"Nothing like this follows from the gradient."),
        ], steps=[S("Gradient means change in y per unit of x", text=r"For each extra hour (x), the predicted mark (y) rises by 4 on average.")],
           concept="Interpreting the gradient in context", skill="Interpretation", hint=r"Gradient is change in y per one unit of x. What are the units?"),
        NUM(r"For a data set, $\bar{x} = 12$, $\bar{y} = 40$, $S_{yy} = 1500$ and $S_{xy} = -420$. Use the regression line of $x$ on $y$ to estimate $x$ when $y = 50$.", 9.2, steps=[
            S("Gradient of x on y", math=r"d = \frac{S_{xy}}{S_{yy}} = \frac{-420}{1500} = -0.28"),
            S("Line through the mean point", math=r"x = 12 - 0.28(y - 40)"),
            S("Substitute", math=r"x = 12 - 0.28 \times 10 = 9.2")],
           tolerance=0.05, concept="Regression line of x on y", skill="Calculation", hint=r"For x on y, divide Sxy by Syy."),
        MC(r"A stall owner has the regression line of $y$ (bottles sold) on $x$ (midday temperature). She knows tomorrow's sales and wants to estimate the temperature. Which method is best?", [
            C(r"Rearrange the line of $y$ on $x$ and solve for $x$.", why=r"This gives a different (less accurate) estimate: the y on x line minimises vertical, not horizontal, distances."),
            C(r"Use the regression line of $x$ on $y$.", correct=True),
            C(r"Read the line of $y$ on $x$ backwards on the graph.", why=r"Reading it backwards is the same as rearranging it: it minimises vertical distances, so it is not the best way to estimate x."),
            C(r"It is impossible to estimate $x$ from $y$.", why=r"It is possible: the line of x on y is for exactly this purpose."),
        ], steps=[S("Which variable do we want to estimate?", text=r"The temperature x. So use the regression line of x on y: x = x-bar + (Sxy/Syy)(y − y-bar).")],
           concept="Choosing between the lines of y on x and x on y", skill="Reasoning", hint=r"Which variable is being predicted?",
           feedback=r"The Board's 2023 report notes that the two lines were sometimes taken the wrong way round."),
        MC(r"A regression line of $y$ on $x$ was calculated from data with $x$ between 20 and 60. Which statement about predictions is best?", [
            C(r"Both estimates are equally reliable because the line is straight.", why=r"The line fits only the range of the data; the pattern outside it is unknown."),
            C(r"The estimate at $x = 15$ is reliable; the estimate at $x = 40$ is not.", why=r"This reverses the idea: 40 is inside the data range (interpolation) and 15 is outside (extrapolation)."),
            C(r"The estimate at $x = 40$ is reliable; the estimate at $x = 15$ is less reliable.", correct=True),
            C(r"Neither estimate is reliable, since a regression line only describes the data it was built from.", why=r"Estimates inside the range (interpolation) are reasonable if the correlation is strong."),
        ], steps=[S("Interpolation", text=r"x = 40 lies inside 20 to 60: interpolation, reasonably reliable if r is close to ±1."), S("Extrapolation", text=r"x = 15 lies outside: extrapolation, unreliable as the pattern may not continue.")],
           concept="Interpolation versus extrapolation", skill="Reasoning", hint=r"Is the x value inside or outside the range of the data?"),
    ]))

# ---------------------------------------------------------------- 8. Rank correlation
SETS.append(practice_set(
    module=M_REG, topic="Rank correlation",
    title="Ranking, ties and Spearman's coefficient",
    lesson="stu1-rank-correlation-spearman",
    questions=[
        MC(r"In a set of values, three values are tied for 2nd, 3rd and 4th place. What rank does each get?", [
            C("2", why=r"This gives all three the best of the ranks they share. Tied values share the average."),
            C("3", correct=True),
            C("4", why=r"This gives all three the worst of the ranks they share. Tied values share the average."),
            C("2.5", why=r"This averages only two of the three ranks (2 and 3). The ranks are 2, 3 and 4."),
        ], steps=[S("Average the ranks that the tied values occupy", math=r"\frac{2 + 3 + 4}{3} = 3")],
           concept="Average rank for tied values", skill="Calculation", hint=r"Add up all the ranks they would have taken and divide by how many values there are."),
        NUM(r"For $n = 8$ pairs of ranks $\sum d^2 = 21$. Find Spearman's coefficient.", 0.75, steps=[
            S("Substitute", math=r"r_s = 1 - \frac{6 \times 21}{8 \times 63} = 1 - \frac{126}{504} = 0.75")],
           tolerance=0.001, concept="Calculating r_s from the sum of d squared", skill="Calculation", hint=r"n(n squared minus 1) for n = 8 is 8 × 63."),
        MC(r"Two judges rank twelve dancers. Spearman's coefficient is $r_s = -0.8$. What does this show?", [
            C("The judges agree strongly.", why=r"Agreement gives a positive value. A negative value means disagreement."),
            C("The judges have almost no agreement.", why=r"No agreement gives a value near 0, not −0.8."),
            C("The judges tend to disagree strongly: dancers ranked high by one are ranked low by the other.", correct=True),
            C("The calculation must be wrong because a coefficient cannot be negative.", why=r"r_s can be negative, anywhere from −1 to +1."),
        ], steps=[S("Sign and size", text=r"Negative sign: opposite rankings. Size 0.8: strong.")],
           concept="Interpreting a negative r_s", skill="Interpretation", hint=r"What does a negative sign tell you about the direction of the agreement?"),
        NUM(r"Five students have scores in two tests: $x$: 10, 20, 30, 40, 50 and $y$: 31, 12, 20, 45, 38. Find $r_s$.", 0.6, steps=[
            S("Ranks", math=r"x \text{ ranks: } 1, 2, 3, 4, 5, \qquad y \text{ ranks: } 3, 1, 2, 5, 4"),
            S("Differences", math=r"d = -2, 1, 1, -1, 1 \;\Rightarrow\; \sum d^2 = 8"),
            S("Coefficient", math=r"r_s = 1 - \frac{6 \times 8}{5 \times 24} = 0.6")],
           tolerance=0.001, concept="r_s from raw data", skill="Calculation", hint=r"Rank both lists from smallest to largest first."),
        MC(r"For the data $x$: 1, 2, 3, 4, 5 and $y$: 1, 4, 9, 16, 25 ($y = x^2$), which statement is true?", [
            C(r"$r_s = 1$ and the product-moment coefficient is slightly less than 1.", correct=True),
            C(r"$r_s = 1$ and the product-moment coefficient is exactly 1.", why=r"The points lie on a curve, not a straight line, so the PMCC is less than 1 (0.981)."),
            C(r"$r_s$ is less than 1, because the points are not in a straight line.", why=r"$r_s$ depends only on the order: y always increases with x, so the ranks agree exactly."),
            C(r"Neither coefficient can be calculated.", why=r"Both can be calculated from the data."),
        ], steps=[S("Ranks", text=r"x ranks and y ranks are both 1, 2, 3, 4, 5, so d = 0 and r_s = 1."), S("PMCC", text=r"The points lie on a curve, so the PMCC is 0.981 (calculated), slightly less than 1.")],
           concept="r_s for a curved, always-increasing relationship", skill="Concept", hint=r"Compare the order of the x values with the order of the y values."),
        NUM(r"Six candidates have $x$: 7, 9, 9, 12, 15, 5 and $y$: 20, 31, 25, 31, 40, 18. Find $r_s$ by the formula, to 3 decimal places.", 0.957, steps=[
            S("Ranks (ties share the average)", math=r"x \text{ ranks: } 2, 3.5, 3.5, 5, 6, 1; \qquad y \text{ ranks: } 2, 4.5, 3, 4.5, 6, 1"),
            S("Differences", math=r"d = 0, -1, 0.5, 0.5, 0, 0 \;\Rightarrow\; \sum d^2 = 1 + 0.25 + 0.25 = 1.5"),
            S("Coefficient", math=r"r_s = 1 - \frac{6 \times 1.5}{6 \times 35} = 1 - \frac{9}{210} = 0.957")],
           tolerance=0.002, concept="r_s with tied values", skill="Calculation", hint=r"Rank both lists from smallest; ties get the average rank.",
           feedback=r"With ties the formula is approximate; the PMCC of the ranks gives 0.956."),
        MC(r"A student ranks the first variable from smallest to largest and the second from largest to smallest, and obtains $r_s = -0.9$ for data that clearly increase together. What is the mistake?", [
            C("The sum of $d$ was not squared.", why=r"Not squaring would not give a value this close to ±1; also the sum of plain d is zero."),
            C("The formula was used without the 1 at the start.", why=r"That would give a small positive number, not −0.9."),
            C("The sample is too small.", why=r"Sample size does not change the sign."),
            C("The two variables were ranked in opposite directions.", correct=True),
        ], steps=[S("Check the ranking direction", text=r"Both variables must be ranked in the same direction. Reversing one reverses the sign of r_s: the correct value is +0.9.")],
           concept="Common error: ranking in opposite directions", skill="Reasoning", hint=r"What happens to d if one list is ranked backwards?"),
        MC(r"For $n = 10$ pairs $\sum d^2 = 33$. Which is the value of $r_s$?", [
            C(r"$0.2$", why=r"This is $6 \sum d^2 / (n(n^2 - 1))$ without subtracting from 1."),
            C(r"$0.967$", why=r"This forgets the factor 6."),
            C(r"$0.8$", correct=True),
            C(r"$0.78$", why=r"This uses $n^2(n - 1) = 900$ in the denominator instead of $n(n^2 - 1) = 990$."),
        ], steps=[S("Substitute", math=r"r_s = 1 - \frac{6 \times 33}{10 \times 99} = 1 - \frac{198}{990} = 0.8")],
           concept="Evaluating the r_s formula accurately", skill="Calculation", hint=r"n(n squared minus 1) for n = 10 is 10 × 99."),
    ]))
