"""Form 5 Additional Mathematics (O Level 575): Statistics option practice sets and Examination mocks.

Statistics: one 8-question set per lesson.
Paper 1 mock: 40 four-option multiple-choice questions covering every syllabus topic (concept = topic title).
Paper 2 mock: 8 extended questions written as separate parts (concept = topic title).
Mock timings are KKEVO practice timings, not official GCE timings.
Draft content: check against the official syllabus and the current GCE Board instructions.
"""

from .dsl import *  # noqa: F403

COURSE = ("additional-mathematics", "form-5")

# ---------------------------------------------------------------- Statistics 1
STATS_1 = [
    MC(r"$X$ takes the values 1, 2, 3 and 4 with probabilities $0.1$, $0.3$, $k$ and $0.2$. Find $k$.", [
        C("$0.4$", correct=True),
        C("$0.6$", why=r"0.6 is the total of the given probabilities. $k$ is what is left: $1 - 0.6$."),
        C("$0.25$", why="The values are not equally likely. Use the fact that all the probabilities add to 1."),
        C("$0.5$", why=r"You left out the $0.1$: $1 - 0.1 - 0.3 - 0.2 = 0.4$."),
    ], steps=[S("Probabilities add to 1", math=r"0.1 + 0.3 + k + 0.2 = 1"),
              S("Solve", math=r"k = 1 - 0.6 = 0.4")],
       concept="Sum of probabilities is 1", skill="Recall",
       hint="What must all the probabilities in a probability distribution add up to?"),
    MC("Which table could be a probability distribution? The values of $X$ are 0, 1, 2 in each case.", [
        C("$P(X = x)$: 0.5, 0.5, 0.5", why="These add to 1.5. The total must be exactly 1."),
        C("$P(X = x)$: 0.7, 0.4, −0.1", why="They add to 1, but a probability cannot be negative."),
        C("$P(X = x)$: 0.25, 0.45, 0.3", correct=True),
        C("$P(X = x)$: 0.2, 0.3, 0.4", why="These add to 0.9, not 1."),
    ], steps=[S("Check each probability", text="Each must be between 0 and 1."),
              S("Check the total", math=r"0.25 + 0.45 + 0.3 = 1")],
       concept="Valid probability distribution", skill="Concept",
       hint="Check two things: is every probability between 0 and 1, and is the total exactly 1?"),
    NUM(r"$X$ takes the values 1, 2, 3 and 4 with probabilities $0.1$, $0.3$, $0.4$ and $0.2$. Find $E(X)$.", 2.7,
        tolerance=0.001,
        steps=[S(r"Use $E(X) = \sum x\,P(X = x)$", math=r"1(0.1) + 2(0.3) + 3(0.4) + 4(0.2)"),
               S("Add", math=r"0.1 + 0.6 + 1.2 + 0.8 = 2.7")],
        concept="Expectation E(X)", skill="Calculation",
        hint="Multiply each value by its probability, then add the results."),
    MC(r"$X$ takes the values 1, 2, 3 and 4 with probabilities $0.1$, $0.3$, $0.4$ and $0.2$, and $E(X) = 2.7$. "
       r"Find $\text{Var}(X)$.", [
        C("$8.1$", why=r"8.1 is $E(X^2)$. You still need to subtract $[E(X)]^2 = 7.29$."),
        C("$5.4$", why=r"You subtracted $E(X)$, not $[E(X)]^2$: use $8.1 - 2.7^2$."),
        C("$0.9$", why=r"0.9 is $\sqrt{0.81}$, the standard deviation. The variance is not square-rooted."),
        C("$0.81$", correct=True),
    ], steps=[S("Find $E(X^2)$", math=r"1(0.1) + 4(0.3) + 9(0.4) + 16(0.2) = 0.1 + 1.2 + 3.6 + 3.2 = 8.1"),
              S("Variance", math=r"\text{Var}(X) = 8.1 - 2.7^2 = 8.1 - 7.29 = 0.81")],
       concept="Variance Var(X) = E(X²) − [E(X)]²", skill="Calculation",
       hint=r"Find $E(X^2) = \sum x^2 P(X = x)$ first."),
    MC(r"$X$ takes the values 0, 1, 2, 3 with probabilities 0.15, 0.35, 0.3, 0.2. Find $P(X \ge 2)$.", [
        C("$0.3$", why=r"This is only $P(X = 2)$. 'At least 2' also includes $X = 3$."),
        C("$0.5$", correct=True),
        C("$0.85$", why=r"This is $1 - P(X = 0) = P(X \ge 1)$. You must also leave out $X = 1$."),
        C("$0.2$", why=r"This is $P(X > 2) = P(X = 3)$. 'At least 2' includes 2."),
    ], steps=[S("List the values", text=r"$X \ge 2$ means $X = 2$ or $X = 3$."),
              S("Add", math=r"P(X \ge 2) = 0.3 + 0.2 = 0.5")],
       concept="Probabilities from a distribution table", skill="Interpretation",
       hint="Which values of X are 'at least 2'?"),
    NUM(r"$X$ takes the values 0, 1, 2, 3 with $P(X = x) = k(x + 1)$. Find $P(X = 2)$.", 0.3, tolerance=0.001,
        steps=[S("Probabilities add to 1", math=r"k(1) + k(2) + k(3) + k(4) = 10k = 1"),
               S("Find k", math=r"k = 0.1"),
               S("Substitute x = 2", math=r"P(X = 2) = 0.1 \times 3 = 0.3")],
        concept="Finding an unknown probability", skill="Calculation",
        hint="Write the four probabilities in terms of k and make them add to 1."),
    MC(r"$X$ takes the values 0, 1, 2, 3 with probabilities $0.2$, $a$, $b$ and $0.1$. Given that $E(X) = 1.4$, "
       r"find $a$ and $b$.", [
        C("$a = 0.4$, $b = 0.3$", why=r"These add to 0.7, but $E(X) = 0.4 + 0.6 + 0.3 = 1.3$, not 1.4. You swapped $a$ and $b$."),
        C("$a = 0.35$, $b = 0.35$", why="Splitting 0.7 equally ignores the information about E(X)."),
        C("$a = 0.3$, $b = 0.4$", correct=True),
        C("$a = 0.5$, $b = 0.2$", why=r"These add to 0.7, but $E(X) = 0.5 + 0.4 + 0.3 = 1.2$, not 1.4."),
    ], steps=[S("Equation 1", math=r"0.2 + a + b + 0.1 = 1 \;\Rightarrow\; a + b = 0.7"),
              S("Equation 2", math=r"0(0.2) + a + 2b + 3(0.1) = 1.4 \;\Rightarrow\; a + 2b = 1.1"),
              S("Subtract", math=r"b = 0.4, \quad a = 0.3")],
       concept="Unknowns from ΣP = 1 and E(X)", skill="Reasoning",
       hint="Write one equation from 'the probabilities add to 1' and another from E(X) = 1.4."),
    MC("At a school fun-fair, a player pays 200 FCFA to pick a card. With probability 0.2 the player wins and "
       "receives 800 FCFA; otherwise the player receives nothing. Find the expected gain per game and decide "
       "whether the game is fair.", [
        C(r"$0$ FCFA; the game is fair", why="You treated the whole 800 FCFA as gain. The player has already paid 200, so the net win is 600 FCFA."),
        C(r"$-40$ FCFA; the game is not fair", correct=True),
        C(r"$160$ FCFA; the game favours the player", why=r"$800 \times 0.2 = 160$ ignores the 200 FCFA the player pays every game."),
        C(r"$-40$ FCFA; the game is fair", why="The value is right, but a game is fair only when the expected gain is exactly 0."),
    ], steps=[S("Gains", text="Win: $800 - 200 = 600$ FCFA with probability 0.2. Lose: $-200$ FCFA with probability 0.8."),
              S("Expected gain", math=r"600(0.2) + (-200)(0.8) = 120 - 160 = -40 \text{ FCFA}"),
              S("Decide", text="The expected gain is not 0, so the game is not fair. On average the player loses 40 FCFA per game.")],
       concept="Expected gain and fair games", skill="Application",
       hint="Write the player's net gain for a win and for a loss, then find the expected value."),
]

# ---------------------------------------------------------------- Statistics 2
STATS_2 = [
    MC("Which of these can be modelled by a binomial distribution?", [
        C("The number of rolls of a die until the first six appears", why="There is no fixed number of trials, so it is not binomial."),
        C("The number of red cards when 5 cards are drawn without replacement from a pack",
          why="Without replacement the probability changes from draw to draw, so the trials are not independent."),
        C("The total score from 10 rolls of a die", why="Each roll has six outcomes, and a total score is not a count of successes."),
        C("The number of heads when a fair coin is tossed 8 times", correct=True),
    ], steps=[S("Check the conditions", text="Fixed number of independent trials, two outcomes each time, the same probability of success."),
              S("Apply them", text=r"Eight tosses, success = a head, $p = 0.5$ each time: $X \sim B(8, 0.5)$.")],
       concept="Binomial conditions", skill="Concept",
       hint="Test each situation against the four binomial conditions."),
    MC(r"$X \sim B(6,\ 0.5)$. Find $P(X = 2)$, to 3 decimal places.", [
        C("$0.234$", correct=True),
        C("$0.016$", why=r"You left out $\binom{6}{2} = 15$. Without it you count only one order of the successes."),
        C("$0.333$", why=r"$\frac{2}{6}$ is not a binomial probability. Use $\binom{n}{r}p^r(1 - p)^{n - r}$."),
        C("$0.094$", why=r"You used $\binom{6}{1} = 6$. For $r = 2$ you need $\binom{6}{2} = 15$."),
    ], steps=[S("Binomial formula", math=r"P(X = 2) = \binom{6}{2}(0.5)^2(0.5)^4"),
              S("Work it out", math=r"15 \times \frac{1}{64} = \frac{15}{64} \approx 0.234")],
       concept="Binomial probability P(X = r)", skill="Calculation",
       hint=r"Use $P(X = r) = \binom{n}{r}p^r(1 - p)^{n - r}$ with $n = 6$, $p = 0.5$ and $r = 2$."),
    NUM("Each seed in a packet germinates with probability 0.3, independently. Four seeds are planted. Find the "
        "probability that at least one germinates. Give your answer to 4 decimal places.", 0.7599, tolerance=0.0005,
        steps=[S("Name the distribution", math=r"X \sim B(4,\ 0.3)"),
               S("Use the complement", math=r"P(X \ge 1) = 1 - P(X = 0)"),
               S("Work it out", math=r"1 - (0.7)^4 = 1 - 0.2401 = 0.7599")],
        concept="At least one, using the complement", skill="Application",
        hint="At least one is everything except none. Find P(X = 0) first."),
    MC(r"$X \sim B(20,\ 0.4)$. Find $\text{Var}(X)$.", [
        C("$8$", why=r"8 is the mean $np$. The variance is $np(1 - p)$."),
        C("$12$", why=r"12 is $n(1 - p)$, the expected number of failures."),
        C("$4.8$", correct=True),
        C("$2.19$", why=r"That is $\sqrt{4.8}$, the standard deviation, not the variance."),
    ], steps=[S("Use the formula", math=r"\text{Var}(X) = np(1 - p) = 20 \times 0.4 \times 0.6 = 4.8")],
       concept="Variance np(1 − p)", skill="Recall",
       hint=r"For $X \sim B(n, p)$ the variance is $np(1 - p)$."),
    MC(r"$X \sim B(5,\ 0.2)$. Find $P(X \le 1)$, to 3 decimal places.", [
        C("$0.410$", why=r"This is only $P(X = 1)$. 'At most 1' also includes $X = 0$."),
        C("$0.737$", correct=True),
        C("$0.263$", why=r"This is $P(X \ge 2)$, the complement of what was asked."),
        C("$0.328$", why=r"This is only $P(X = 0)$. Add $P(X = 1)$ as well."),
    ], steps=[S("At most 1 means 0 or 1", math=r"P(X \le 1) = P(X = 0) + P(X = 1)"),
              S("Each term", math=r"0.8^5 + 5(0.2)(0.8)^4 = 0.32768 + 0.4096"),
              S("Add", math=r"= 0.73728 \approx 0.737")],
       concept="Cumulative probability P(X ≤ r)", skill="Calculation",
       hint="List the values of X that are 'at most 1', then add their probabilities."),
    NUM(r"$X \sim B(n, p)$ has mean 6 and variance 2.4. Find $n$.", 10,
        steps=[S("Two equations", math=r"np = 6, \qquad np(1 - p) = 2.4"),
               S("Divide", math=r"1 - p = \frac{2.4}{6} = 0.4 \;\Rightarrow\; p = 0.6"),
               S("Find n", math=r"n = \frac{6}{0.6} = 10")],
        concept="Finding n and p from the mean and variance", skill="Reasoning",
        hint="Divide the variance by the mean: what does that give?"),
    MC(r"In a market, 25% of the oranges on a stall are bruised. Six oranges are chosen at random. Find the "
       r"probability that at least 2 are bruised, to 3 decimal places.", [
        C("$0.822$", why=r"This is $1 - P(X = 0) = P(X \ge 1)$. You must also subtract $P(X = 1)$."),
        C("$0.356$", why=r"This is $P(X = 1)$ alone."),
        C("$0.297$", why=r"This is $P(X = 2)$ only. 'At least 2' means 2, 3, 4, 5 or 6."),
        C("$0.466$", correct=True),
    ], steps=[S("Name the distribution", math=r"X \sim B(6,\ 0.25)"),
              S("Use the complement", math=r"P(X \ge 2) = 1 - P(X = 0) - P(X = 1)"),
              S("Each term", math=r"P(X = 0) = 0.75^6 = 0.17798, \quad P(X = 1) = 6(0.25)(0.75)^5 = 0.35596"),
              S("Answer", math=r"1 - 0.17798 - 0.35596 = 0.46606 \approx 0.466")],
       concept="Cumulative probability using the complement", skill="Application",
       hint="'At least 2' is everything except 0 and 1."),
    NUM("A quiz has 10 multiple-choice questions, each with 4 options. A student guesses every answer. Find the "
        "probability that exactly 3 answers are correct. Give your answer to 3 decimal places.", 0.250,
        tolerance=0.0015,
        steps=[S("Name the distribution", math=r"X \sim B(10,\ 0.25)"),
               S("Binomial formula", math=r"P(X = 3) = \binom{10}{3}(0.25)^3(0.75)^7"),
               S("Calculate", math=r"= 120 \times 0.015625 \times 0.13348 = 0.2503 \approx 0.250")],
        concept="Binomial probability in context", skill="Application",
        hint="What is the probability of guessing one question correctly? That is p."),
]
# ---------------------------------------------------------------- Paper 1 mock
# 40 questions: Polynomials 6, Trigonometry 6, Binomial expansion 5, Coordinate geometry 6, Differentiation 6,
# Integration 5, Mechanics option 3, Statistics option 3. Correct answers: 10 each of A, B, C, D.
P1_QUESTIONS = [
    # 1 B
    MC(r"Find the remainder when $x^3 - 2x^2 + 4x - 5$ is divided by $(x - 2)$.", [
        C("$-29$", why=r"This is $f(-2)$. For the divisor $(x - 2)$ substitute $x = 2$."),
        C("$3$", correct=True),
        C("$13$", why=r"You used $+5$ for the constant term. $f(2) = 8 - 8 + 8 - 5 = 3$."),
        C("$0$", why=r"A remainder of 0 would make $(x - 2)$ a factor. Work out $f(2)$ instead of assuming."),
    ], steps=[S("Remainder theorem", text=r"The remainder on division by $(x - a)$ is $f(a)$."),
              S("Substitute x = 2", math=r"f(2) = 8 - 8 + 8 - 5 = 3")],
       concept="Polynomials", skill="Calculation",
       hint="Use the remainder theorem: which value of x makes the divisor zero?"),
    # 2 A
    MC(r"Express $135^\circ$ in radians.", [
        C(r"$\frac{3\pi}{4}$", correct=True),
        C(r"$\frac{2\pi}{3}$", why=r"$\frac{2\pi}{3}$ is $120^\circ$."),
        C(r"$\frac{3\pi}{2}$", why=r"$\frac{3\pi}{2}$ is $270^\circ$, twice too big."),
        C(r"$\frac{4\pi}{3}$", why=r"$\frac{4\pi}{3}$ is $240^\circ$."),
    ], steps=[S("Degrees to radians", math=r"\theta_{\text{rad}} = \theta_{\text{deg}} \times \frac{\pi}{180}"),
              S("Substitute", math=r"135 \times \frac{\pi}{180} = \frac{3\pi}{4}")],
       concept="Trigonometry", skill="Recall",
       hint=r"$180^\circ = \pi$ radians."),
    # 3 C
    MC(r"Differentiate $y = 4x^3 - \dfrac{2}{x}$ with respect to $x$.", [
        C(r"$12x^2 - \dfrac{2}{x^2}$", why=r"$-2x^{-1}$ differentiates to $(-1)(-2)x^{-2} = +2x^{-2}$: the two minus signs make a plus."),
        C(r"$12x^2 + \dfrac{2}{x}$", why="You did not reduce the power of the second term by 1."),
        C(r"$12x^2 + \dfrac{2}{x^2}$", correct=True),
        C(r"$4x^2 - 2$", why=r"Multiply by the power, then reduce it by 1: $4x^3 \to 12x^2$."),
    ], steps=[S("Write with powers", math=r"y = 4x^3 - 2x^{-1}"),
              S("Differentiate each term", math=r"\frac{dy}{dx} = 12x^2 + 2x^{-2} = 12x^2 + \frac{2}{x^2}")],
       concept="Differentiation", skill="Calculation",
       hint=r"Write $\frac{2}{x}$ as $2x^{-1}$ first."),
    # 4 D
    MC(r"Find the gradient of the line through $(-1, 4)$ and $(3, -4)$.", [
        C("$2$", why=r"Sign slip: the change in $y$ is $-4 - 4 = -8$, which is negative."),
        C(r"$-\frac{1}{2}$", why="You divided the change in x by the change in y. Gradient = change in y ÷ change in x."),
        C("$-4$", why=r"The change in $x$ is $3 - (-1) = 4$, not $3 - 1 = 2$."),
        C("$-2$", correct=True),
    ], steps=[S("Gradient formula", math=r"m = \frac{y_2 - y_1}{x_2 - x_1}"),
              S("Substitute", math=r"m = \frac{-4 - 4}{3 - (-1)} = \frac{-8}{4} = -2")],
       concept="Coordinate geometry", skill="Calculation",
       hint="Gradient = change in y ÷ change in x. Watch the signs."),
    # 5 A
    MC(r"Find the coefficient of $x^2$ in the expansion of $(1 + 3x)^5$.", [
        C("$90$", correct=True),
        C("$30$", why=r"You used $3x^2$ instead of $(3x)^2 = 9x^2$: the 3 must be squared too."),
        C("$10$", why=r"10 is only $\binom{5}{2}$. Multiply by $3^2$."),
        C("$270$", why=r"270 is the coefficient of $x^3$: $\binom{5}{3} \times 27$."),
    ], steps=[S("Term in x²", math=r"\binom{5}{2}(3x)^2 = 10 \times 9x^2"),
              S("Coefficient", math=r"= 90x^2, \text{ so the coefficient is } 90")],
       concept="Binomial expansion", skill="Calculation",
       hint=r"The $x^2$ term is $\binom{5}{2}(3x)^2$."),
    # 6 B
    MC(r"Find $\int (6x^2 + 4x)\,dx$.", [
        C(r"$12x + 4 + c$", why="You differentiated instead of integrating."),
        C(r"$2x^3 + 2x^2 + c$", correct=True),
        C(r"$6x^3 + 4x^2 + c$", why="You raised the powers but did not divide by the new powers."),
        C(r"$3x^3 + 2x^2 + c$", why=r"Divide by the **new** power: $6x^2 \to \frac{6x^3}{3} = 2x^3$, not $\frac{6x^3}{2}$."),
    ], steps=[S("Rule", math=r"\int x^n\,dx = \frac{x^{n+1}}{n+1} + c"),
              S("Apply", math=r"\frac{6x^3}{3} + \frac{4x^2}{2} + c = 2x^3 + 2x^2 + c")],
       concept="Integration", skill="Calculation",
       hint="Add 1 to each power, then divide by the new power."),
    # 7 C
    MC(r"(Statistics option) $X$ takes the values 0, 1, 2 with probabilities 0.2, 0.5, 0.3. Find $E(X)$.", [
        C("$1$", why="1 is the middle value. E(X) weights each value by its probability."),
        C("$0.33$", why="This is the average of the three probabilities, not the expected value of X."),
        C("$1.1$", correct=True),
        C("$1.7$", why=r"1.7 is $E(X^2) = 0.5 + 4(0.3)$. For $E(X)$ do not square the values."),
    ], steps=[S("Formula", math=r"E(X) = \sum x\,P(X = x)"),
              S("Substitute", math=r"0(0.2) + 1(0.5) + 2(0.3) = 1.1")],
       concept="Statistics", skill="Calculation",
       hint="Multiply each value by its probability and add."),
    # 8 D
    MC(r"$(x + 2)$ is a factor of $x^3 + kx^2 - x - 2$. Find $k$.", [
        C("$-1$", why=r"You substituted $x = 2$. For the factor $(x + 2)$ substitute $x = -2$."),
        C("$3$", why=r"$-x$ at $x = -2$ is $+2$, not $-2$. Check the sign of each term."),
        C("$-2$", why=r"$(-2)^3 = -8$, not $+8$."),
        C("$2$", correct=True),
    ], steps=[S("Factor theorem", math=r"f(-2) = 0"),
              S("Substitute", math=r"-8 + 4k + 2 - 2 = 0 \;\Rightarrow\; 4k = 8 \;\Rightarrow\; k = 2")],
       concept="Polynomials", skill="Calculation",
       hint=r"If $(x + 2)$ is a factor, what is $f(-2)$?"),
    # 9 C
    MC("A sector of a circle has radius 8 cm and angle 0.75 radians. Find the arc length.", [
        C("24 cm", why=r"24 is the sector **area**, $\frac{1}{2}r^2\theta$, in cm²."),
        C("10.7 cm", why=r"You divided: $8 \div 0.75$. Arc length is $r\theta$."),
        C("6 cm", correct=True),
        C("0.105 cm", why="You treated 0.75 as degrees. The angle is already in radians, so use s = rθ directly."),
    ], steps=[S("Arc length formula (θ in radians)", math=r"s = r\theta"),
              S("Substitute", math=r"s = 8 \times 0.75 = 6 \text{ cm}")],
       concept="Trigonometry", skill="Calculation",
       hint="Which formula gives arc length when the angle is in radians?"),
    # 10 A
    MC(r"Find the distance between $(2, -1)$ and $(8, 7)$.", [
        C("$10$", correct=True),
        C("$14$", why=r"You added the changes $6 + 8$. Use Pythagoras: $\sqrt{6^2 + 8^2}$."),
        C("$8.49$", why=r"The change in $y$ is $7 - (-1) = 8$, not $7 - 1 = 6$."),
        C("$100$", why="You forgot the square root."),
    ], steps=[S("Distance formula", math=r"d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}"),
              S("Substitute", math=r"d = \sqrt{6^2 + 8^2} = \sqrt{100} = 10")],
       concept="Coordinate geometry", skill="Calculation",
       hint="Find the change in x and the change in y, then use Pythagoras."),
    # 11 B
    MC(r"Find the gradient of the curve $y = x^2 - 3x + 2$ at the point where $x = 4$.", [
        C("$6$", why=r"6 is the value of $y$ at $x = 4$. The gradient is the value of $\frac{dy}{dx}$."),
        C("$5$", correct=True),
        C("$8$", why=r"8 is $2x$ alone. The $-3x$ term differentiates to $-3$."),
        C("$11$", why=r"Sign slip: $\frac{dy}{dx} = 2x - 3$, not $2x + 3$."),
    ], steps=[S("Differentiate", math=r"\frac{dy}{dx} = 2x - 3"),
              S("Substitute x = 4", math=r"2(4) - 3 = 5")],
       concept="Differentiation", skill="Calculation",
       hint=r"Find $\frac{dy}{dx}$ first, then substitute."),
    # 12 D
    MC(r"(Mechanics option) A car starts from rest and accelerates uniformly at $3$ m/s². How far does it travel in "
       r"the first 4 seconds?", [
        C("12 m", why=r"12 m/s is the speed $at$ after 4 s, not the distance."),
        C("48 m", why=r"You forgot the $\frac{1}{2}$ in $s = ut + \frac{1}{2}at^2$."),
        C("6 m", why=r"You did not square $t$: $\frac{1}{2} \times 3 \times 4^2$."),
        C("24 m", correct=True),
    ], steps=[S("Choose the equation", math=r"s = ut + \tfrac{1}{2}at^2, \quad u = 0"),
              S("Substitute", math=r"s = \tfrac{1}{2} \times 3 \times 4^2 = 24 \text{ m}")],
       concept="Mechanics", skill="Calculation",
       hint="'From rest' means u = 0. Which suvat equation has s, u, a and t?"),
    # 13 C
    MC(r"Evaluate $\int_1^3 (2x + 1)\,dx$.", [
        C("$12$", why="12 is the value at the upper limit only. Subtract the value at x = 1."),
        C("$7$", why="7 is the integrand at x = 3. You must integrate first."),
        C("$10$", correct=True),
        C("$14$", why="You added the values at the two limits. Upper minus lower."),
    ], steps=[S("Integrate", math=r"\int (2x + 1)\,dx = x^2 + x"),
              S("Apply the limits", math=r"(9 + 3) - (1 + 1) = 12 - 2 = 10")],
       concept="Integration", skill="Calculation",
       hint="Integrate, then work out (value at 3) − (value at 1)."),
    # 14 D
    MC(r"Find the term independent of $x$ in the expansion of $\left(x + \dfrac{2}{x}\right)^6$.", [
        C("$20$", why=r"20 is $\binom{6}{3}$ only. Multiply by $2^3$."),
        C("$60$", why=r"60 is the coefficient of $x^2$ ($r = 2$). The term independent of $x$ has $r = 3$."),
        C("$8$", why=r"8 is $2^3$ only. Multiply by $\binom{6}{3} = 20$."),
        C("$160$", correct=True),
    ], steps=[S("General term", math=r"\binom{6}{r}x^{6 - r}\left(\frac{2}{x}\right)^r = \binom{6}{r}2^r x^{6 - 2r}"),
              S("Power of x is 0", math=r"6 - 2r = 0 \;\Rightarrow\; r = 3"),
              S("Term", math=r"\binom{6}{3} \times 2^3 = 20 \times 8 = 160")],
       concept="Binomial expansion", skill="Reasoning",
       hint="Write the general term and make the power of x equal to 0."),
    # 15 A
    MC(r"Express $\dfrac{5x + 1}{(x - 1)(x + 1)}$ in partial fractions.", [
        C(r"$\dfrac{3}{x - 1} + \dfrac{2}{x + 1}$", correct=True),
        C(r"$\dfrac{2}{x - 1} + \dfrac{3}{x + 1}$", why="You swapped the numerators. Check by putting x = 1: the numerator 6 ÷ 2 = 3 belongs over (x − 1)."),
        C(r"$\dfrac{3}{x - 1} - \dfrac{2}{x + 1}$", why=r"At $x = -1$: $B = \frac{-5 + 1}{-2} = +2$. Two negatives make a positive."),
        C(r"$\dfrac{6}{x - 1} + \dfrac{4}{x + 1}$", why=r"You did not divide by the value of the other bracket: at $x = 1$, $6 \div (1 + 1) = 3$."),
    ], steps=[S("Set up", math=r"\frac{5x + 1}{(x - 1)(x + 1)} = \frac{A}{x - 1} + \frac{B}{x + 1}"),
              S("Multiply through", math=r"5x + 1 = A(x + 1) + B(x - 1)"),
              S("Put x = 1 and x = −1", math=r"6 = 2A \Rightarrow A = 3; \quad -4 = -2B \Rightarrow B = 2")],
       concept="Polynomials", skill="Calculation",
       hint="Write A/(x − 1) + B/(x + 1), multiply through, then substitute x = 1 and x = −1."),
    # 16 B
    MC("A sector has radius 10 cm and angle 1.2 radians. Find its area.", [
        C("12 cm²", why=r"12 is the arc length $r\theta$ in cm, not the area."),
        C("60 cm²", correct=True),
        C("120 cm²", why=r"You forgot the $\frac{1}{2}$ in $\frac{1}{2}r^2\theta$."),
        C("1.05 cm²", why="You treated 1.2 as degrees. The angle is already in radians."),
    ], steps=[S("Sector area (θ in radians)", math=r"A = \tfrac{1}{2}r^2\theta"),
              S("Substitute", math=r"A = \tfrac{1}{2} \times 100 \times 1.2 = 60 \text{ cm}^2")],
       concept="Trigonometry", skill="Calculation",
       hint="Which formula gives the area of a sector when the angle is in radians?"),
    # 17 C
    MC(r"Find the equation of the line through $(4, 1)$ perpendicular to $y = 2x + 3$.", [
        C(r"$y = 2x - 7$", why="This line is parallel to y = 2x + 3, not perpendicular."),
        C(r"$y = -2x + 9$", why=r"Perpendicular gradients multiply to $-1$: $2 \times (-2) \neq -1$. Use $-\frac{1}{2}$."),
        C(r"$y = -\frac{1}{2}x + 3$", correct=True),
        C(r"$y = \frac{1}{2}x - 1$", why="You took the reciprocal but not the negative."),
    ], steps=[S("Perpendicular gradient", math=r"m = -\frac{1}{2}"),
              S("Point-gradient form", math=r"y - 1 = -\tfrac{1}{2}(x - 4)"),
              S("Simplify", math=r"y = -\tfrac{1}{2}x + 3")],
       concept="Coordinate geometry", skill="Calculation",
       hint=r"Perpendicular gradients satisfy $m_1 m_2 = -1$."),
    # 18 D
    MC(r"Find the coordinates of the stationary point of $y = 2x^2 - 8x + 1$.", [
        C(r"$(-2, 25)$", why=r"Sign slip: $4x - 8 = 0$ gives $x = +2$."),
        C(r"$(4, 1)$", why=r"$2x^2$ differentiates to $4x$, not $2x$."),
        C(r"$(2, 0)$", why=r"At a stationary point $\frac{dy}{dx} = 0$, not $y = 0$. Substitute $x = 2$ into $y$."),
        C(r"$(2, -7)$", correct=True),
    ], steps=[S("Differentiate", math=r"\frac{dy}{dx} = 4x - 8"),
              S("Set to zero", math=r"4x - 8 = 0 \;\Rightarrow\; x = 2"),
              S("Find y", math=r"y = 2(4) - 16 + 1 = -7")],
       concept="Differentiation", skill="Calculation",
       hint=r"Solve $\frac{dy}{dx} = 0$, then substitute back into $y$."),
    # 19 A
    MC(r"Evaluate $\int_0^2 3x^2\,dx$.", [
        C("$8$", correct=True),
        C("$12$", why="12 is the integrand at x = 2. Integrate first."),
        C("$24$", why=r"You did not divide by the new power: $\int 3x^2\,dx = x^3$, not $3x^3$."),
        C("$2$", why="2 is the width of the interval. The integrand is not 1."),
    ], steps=[S("Integrate", math=r"\int 3x^2\,dx = x^3"),
              S("Apply the limits", math=r"2^3 - 0^3 = 8")],
       concept="Integration", skill="Calculation",
       hint=r"Integrate $3x^2$, then substitute the limits."),
    # 20 B
    MC(r"(Statistics option) $X \sim B(4, 0.5)$. Find $P(X = 2)$.", [
        C("$0.0625$", why=r"You left out $\binom{4}{2} = 6$. There are 6 orders for 2 successes."),
        C("$0.375$", correct=True),
        C("$0.5$", why=r"$\frac{2}{4}$ is not a binomial probability."),
        C("$0.25$", why=r"You used $\binom{4}{1} = 4$ instead of $\binom{4}{2} = 6$."),
    ], steps=[S("Binomial formula", math=r"P(X = 2) = \binom{4}{2}(0.5)^2(0.5)^2"),
              S("Calculate", math=r"6 \times \frac{1}{16} = 0.375")],
       concept="Statistics", skill="Calculation",
       hint=r"Use $P(X = r) = \binom{n}{r}p^r(1 - p)^{n - r}$."),
    # 21 C
    MC(r"Find the remainder when $4x^3 - 2x^2 + x + 3$ is divided by $(2x - 1)$.", [
        C("$6$", why=r"You substituted $x = 1$. $(2x - 1) = 0$ when $x = \frac{1}{2}$."),
        C("$1.5$", why=r"You substituted $x = -\frac{1}{2}$. Sign slip."),
        C("$3.5$", correct=True),
        C("$29$", why=r"You substituted $x = 2$. Solve $2x - 1 = 0$ to find the value."),
    ], steps=[S("Value that makes the divisor zero", math=r"2x - 1 = 0 \;\Rightarrow\; x = \tfrac{1}{2}"),
              S("Remainder theorem", math=r"f\left(\tfrac{1}{2}\right) = 4\left(\tfrac{1}{8}\right) - 2\left(\tfrac{1}{4}\right) + \tfrac{1}{2} + 3 = 3.5")],
       concept="Polynomials", skill="Calculation",
       hint="Which value of x makes 2x − 1 equal to zero?"),
    # 22 B
    MC(r"Find the first three terms, in ascending powers of $x$, of $(2 - x)^4$.", [
        C(r"$16 + 32x + 24x^2$", why=r"The second term has $(-x)^1$, so it is negative."),
        C(r"$16 - 32x + 24x^2$", correct=True),
        C(r"$16 - 8x + 4x^2$", why=r"You left out the binomial coefficients $\binom{4}{1} = 4$ and $\binom{4}{2} = 6$."),
        C(r"$16 - 32x + 6x^2$", why=r"The $x^2$ term is $\binom{4}{2}2^2x^2 = 24x^2$: you forgot $2^2$."),
    ], steps=[S("Terms", math=r"2^4 + \binom{4}{1}2^3(-x) + \binom{4}{2}2^2(-x)^2"),
              S("Simplify", math=r"16 - 32x + 24x^2")],
       concept="Binomial expansion", skill="Calculation",
       hint=r"Use $\binom{4}{r}2^{4 - r}(-x)^r$ for $r = 0, 1, 2$."),
    # 23 D
    MC(r"Simplify $\sin\theta\tan\theta + \cos\theta$.", [
        C("$1$", why=r"$\sin^2\theta + \cos^2\theta = 1$ only after you write both over $\cos\theta$: the result is $\frac{1}{\cos\theta}$."),
        C(r"$2\cos\theta$", why=r"$\tan\theta = \frac{\sin\theta}{\cos\theta}$, not $\frac{\cos\theta}{\sin\theta}$."),
        C(r"$\sin^2\theta + \cos\theta$", why=r"$\sin\theta\tan\theta = \frac{\sin^2\theta}{\cos\theta}$: you forgot to divide by $\cos\theta$."),
        C(r"$\dfrac{1}{\cos\theta}$", correct=True),
    ], steps=[S("Write tan in terms of sin and cos", math=r"\sin\theta \cdot \frac{\sin\theta}{\cos\theta} + \cos\theta"),
              S("Common denominator", math=r"\frac{\sin^2\theta + \cos^2\theta}{\cos\theta}"),
              S("Use the identity", math=r"= \frac{1}{\cos\theta}")],
       concept="Trigonometry", skill="Reasoning",
       hint=r"Replace $\tan\theta$ by $\frac{\sin\theta}{\cos\theta}$."),
    # 24 A
    MC(r"Find the centre and radius of the circle $x^2 + y^2 - 6x + 4y - 12 = 0$.", [
        C(r"Centre $(3, -2)$, radius 5", correct=True),
        C(r"Centre $(-3, 2)$, radius 5", why=r"The centre is $(-g, -f)$ where the equation is $x^2 + y^2 + 2gx + 2fy + c = 0$: change the signs of half the coefficients."),
        C(r"Centre $(3, -2)$, radius $\sqrt{12}$", why=r"$r = \sqrt{g^2 + f^2 - c} = \sqrt{9 + 4 + 12}$, not $\sqrt{12}$."),
        C(r"Centre $(3, -2)$, radius 25", why="25 is r². Take the square root."),
    ], steps=[S("Complete the squares", math=r"(x - 3)^2 + (y + 2)^2 = 12 + 9 + 4 = 25"),
              S("Read off", text="Centre (3, −2), radius 5.")],
       concept="Coordinate geometry", skill="Calculation",
       hint="Complete the square in x and in y."),
    # 25 C
    MC(r"Find the equation of the tangent to $y = x^3$ at the point $(1, 1)$.", [
        C(r"$y = 3x - 3$", why=r"$y - 1 = 3(x - 1)$ gives $y = 3x - 2$: you forgot to add the 1."),
        C(r"$y = 3x$", why="This line does not pass through (1, 1)."),
        C(r"$y = 3x - 2$", correct=True),
        C(r"$y = -\frac{1}{3}x + \frac{4}{3}$", why="This is the normal, not the tangent."),
    ], steps=[S("Gradient", math=r"\frac{dy}{dx} = 3x^2 = 3 \text{ at } x = 1"),
              S("Equation", math=r"y - 1 = 3(x - 1) \;\Rightarrow\; y = 3x - 2")],
       concept="Differentiation", skill="Calculation",
       hint=r"The gradient of the tangent is $\frac{dy}{dx}$ at $x = 1$."),
    # 26 A
    MC(r"(Mechanics option) A ball is thrown vertically upwards at 20 m/s. Taking $g = 10$ m/s², find the greatest "
       r"height it reaches.", [
        C("20 m", correct=True),
        C("40 m", why=r"$v^2 = u^2 - 2gs$ gives $s = \frac{u^2}{2g}$: you forgot the 2."),
        C("2 m", why=r"$\frac{u}{g} = 2$ is the **time** to the top in seconds, not the height."),
        C("200 m", why=r"You divided $u^2$ by 2 but not by $g$."),
    ], steps=[S("At the top v = 0", math=r"v^2 = u^2 - 2gs \;\Rightarrow\; 0 = 400 - 20s"),
              S("Solve", math=r"s = 20 \text{ m}")],
       concept="Mechanics", skill="Application",
       hint="At the greatest height the velocity is 0. Use v² = u² + 2as with a = −10."),
    # 27 D
    MC(r"Find the area enclosed by $y = x^2 + 1$, the x-axis and the lines $x = 0$ and $x = 3$.", [
        C("10", why="10 is the value of y at x = 3. Area needs an integral."),
        C("9", why=r"You left out the $+1$ term: $\int 1\,dx = x$ adds 3."),
        C("30", why="30 is a rectangle 3 wide and 10 high, which lies above most of the curve."),
        C("12", correct=True),
    ], steps=[S("Area integral", math=r"\int_0^3 (x^2 + 1)\,dx = \left[\frac{x^3}{3} + x\right]_0^3"),
              S("Evaluate", math=r"9 + 3 - 0 = 12")],
       concept="Integration", skill="Calculation",
       hint="Area under the curve = the definite integral from 0 to 3."),
    # 28 B
    MC(r"Which of these is a factor of $x^3 - 7x + 6$?", [
        C("$(x + 1)$", why=r"$f(-1) = -1 + 7 + 6 = 12 \neq 0$."),
        C("$(x + 3)$", correct=True),
        C("$(x - 3)$", why=r"$f(3) = 27 - 21 + 6 = 12 \neq 0$. Did you test $x = -3$ for $(x - 3)$?"),
        C("$(x + 2)$", why=r"$f(-2) = -8 + 14 + 6 = 12 \neq 0$."),
    ], steps=[S("Test x = −3", math=r"f(-3) = -27 + 21 + 6 = 0"),
              S("Conclude", text="By the factor theorem, (x + 3) is a factor.")],
       concept="Polynomials", skill="Reasoning",
       hint="(x − a) is a factor when f(a) = 0. Test each option."),
    # 29 C
    MC(r"Solve $2\sin x = 1$ for $0 \le x \le 2\pi$.", [
        C(r"$x = \frac{\pi}{6}$ only", why=r"Sine is also positive in the second quadrant: $\pi - \frac{\pi}{6}$ is a solution too."),
        C(r"$x = \frac{\pi}{6}$ or $\frac{7\pi}{6}$", why=r"$\sin\frac{7\pi}{6} = -\frac{1}{2}$. Adding $\pi$ works for tangent, not sine."),
        C(r"$x = \frac{\pi}{6}$ or $\frac{5\pi}{6}$", correct=True),
        C(r"$x = \frac{\pi}{3}$ or $\frac{2\pi}{3}$", why=r"These solve $\sin x = \frac{\sqrt{3}}{2}$."),
    ], steps=[S("Rearrange", math=r"\sin x = \tfrac{1}{2}"),
              S("Principal value", math=r"x = \tfrac{\pi}{6}"),
              S("Second solution (sine positive in quadrants 1 and 2)", math=r"x = \pi - \tfrac{\pi}{6} = \tfrac{5\pi}{6}")],
       concept="Trigonometry", skill="Calculation",
       hint="Find the principal value, then use the CAST diagram for the other quadrant where sine is positive."),
    # 30 A
    MC(r"Find the coefficient of $x^3$ in the expansion of $(1 - 2x)^6$.", [
        C("$-160$", correct=True),
        C("$160$", why=r"$(-2)^3 = -8$: an odd power of a negative number is negative."),
        C("$-120$", why=r"You used $-2 \times 3$ instead of $(-2)^3$."),
        C("$-8$", why=r"You left out $\binom{6}{3} = 20$."),
    ], steps=[S("Term in x³", math=r"\binom{6}{3}(-2x)^3 = 20 \times (-8x^3)"),
              S("Coefficient", math=r"-160")],
       concept="Binomial expansion", skill="Calculation",
       hint=r"The $x^3$ term is $\binom{6}{3}(-2x)^3$."),
    # 31 D
    MC(r"Find the equation of the circle with centre $(-1, 2)$ and radius 3.", [
        C(r"$x^2 + y^2 - 2x + 4y - 4 = 0$", why=r"This has centre $(1, -2)$. $(x + 1)^2$ gives $+2x$."),
        C(r"$x^2 + y^2 + 2x - 4y + 2 = 0$", why=r"You used $r = 3$ instead of $r^2 = 9$: $1 + 4 - 9 = -4$."),
        C(r"$x^2 + y^2 + 2x - 4y - 9 = 0$", why=r"Expanding the brackets also gives $1 + 4$: the constant is $1 + 4 - 9$."),
        C(r"$x^2 + y^2 + 2x - 4y - 4 = 0$", correct=True),
    ], steps=[S("Standard form", math=r"(x + 1)^2 + (y - 2)^2 = 9"),
              S("Expand", math=r"x^2 + 2x + 1 + y^2 - 4y + 4 = 9"),
              S("Simplify", math=r"x^2 + y^2 + 2x - 4y - 4 = 0")],
       concept="Coordinate geometry", skill="Calculation",
       hint=r"Start from $(x - a)^2 + (y - b)^2 = r^2$."),
    # 32 B
    MC(r"For the curve $y = x^3 - 3x$, which statement is true?", [
        C(r"$(1, -2)$ is a maximum point", why=r"$\frac{d^2y}{dx^2} = 6x = 6 > 0$ at $x = 1$, so $(1, -2)$ is a minimum."),
        C(r"$(-1, 2)$ is a maximum point", correct=True),
        C(r"$(-1, 2)$ is a minimum point", why=r"$\frac{d^2y}{dx^2} = 6(-1) = -6 < 0$, which means a maximum."),
        C(r"$(0, 0)$ is a stationary point", why=r"$\frac{dy}{dx} = 3(0)^2 - 3 = -3 \neq 0$ at $x = 0$."),
    ], steps=[S("Stationary points", math=r"\frac{dy}{dx} = 3x^2 - 3 = 0 \;\Rightarrow\; x = \pm 1"),
              S("Coordinates", text="(1, −2) and (−1, 2)."),
              S("Nature", math=r"\frac{d^2y}{dx^2} = 6x: \; x = -1 \Rightarrow -6 < 0, \text{ maximum}")],
       concept="Differentiation", skill="Reasoning",
       hint=r"Find where $\frac{dy}{dx} = 0$, then use the sign of $\frac{d^2y}{dx^2}$."),
    # 33 D
    MC(r"(Statistics option) $X \sim B(10, 0.2)$. Find $\text{Var}(X)$.", [
        C("$2$", why=r"2 is the mean $np$."),
        C("$8$", why=r"8 is $n(1 - p)$, the expected number of failures."),
        C("$1.26$", why=r"1.26 is $\sqrt{1.6}$, the standard deviation."),
        C("$1.6$", correct=True),
    ], steps=[S("Formula", math=r"\text{Var}(X) = np(1 - p)"),
              S("Substitute", math=r"10 \times 0.2 \times 0.8 = 1.6")],
       concept="Statistics", skill="Recall",
       hint=r"For $B(n, p)$ the variance is $np(1 - p)$."),
    # 34 B
    MC(r"Evaluate $\int_1^4 \dfrac{1}{\sqrt{x}}\,dx$.", [
        C("$1$", why=r"$\int x^{-1/2}\,dx = \frac{x^{1/2}}{1/2} = 2\sqrt{x}$: you forgot to divide by $\frac{1}{2}$."),
        C("$2$", correct=True),
        C("$4$", why=r"4 is the value at the upper limit only: subtract $2\sqrt{1} = 2$."),
        C("$0.4375$", why="You differentiated instead of integrating."),
    ], steps=[S("Write as a power", math=r"\int_1^4 x^{-1/2}\,dx"),
              S("Integrate", math=r"\left[2x^{1/2}\right]_1^4"),
              S("Evaluate", math=r"2(2) - 2(1) = 2")],
       concept="Integration", skill="Calculation",
       hint=r"Write $\frac{1}{\sqrt{x}}$ as $x^{-1/2}$."),
    # 35 C
    MC(r"$f(x) = x^3 + ax + b$ leaves remainder 0 when divided by $(x - 1)$ and remainder 6 when divided by "
       r"$(x + 1)$. Find $a$.", [
        C("$4$", why=r"Sign slip. From $a + b = -1$ and $-a + b = 7$: $a = -4$."),
        C("$3$", why="3 is the value of b, not a."),
        C("$-4$", correct=True),
        C("$2$", why=r"You set $f(-1) = -6$ instead of $6$."),
    ], steps=[S("f(1) = 0", math=r"1 + a + b = 0 \;\Rightarrow\; a + b = -1"),
              S("f(−1) = 6", math=r"-1 - a + b = 6 \;\Rightarrow\; -a + b = 7"),
              S("Subtract", math=r"2a = -8 \;\Rightarrow\; a = -4 \;(b = 3)")],
       concept="Polynomials", skill="Reasoning",
       hint="Use the remainder theorem twice to get two equations in a and b."),
    # 36 A
    MC(r"$\sin\theta = \frac{3}{5}$ and $\theta$ is obtuse. Find $\tan\theta$.", [
        C(r"$-\frac{3}{4}$", correct=True),
        C(r"$\frac{3}{4}$", why=r"An obtuse angle is in the second quadrant, where $\tan\theta$ is negative."),
        C(r"$-\frac{4}{3}$", why=r"$\tan\theta = \frac{\sin\theta}{\cos\theta}$, not $\frac{\cos\theta}{\sin\theta}$."),
        C(r"$-\frac{4}{5}$", why=r"$-\frac{4}{5}$ is $\cos\theta$."),
    ], steps=[S("Find cos θ", math=r"\cos^2\theta = 1 - \tfrac{9}{25} = \tfrac{16}{25}, \; \cos\theta = -\tfrac{4}{5} \text{ (obtuse)}"),
              S("tan θ", math=r"\tan\theta = \frac{3/5}{-4/5} = -\frac{3}{4}")],
       concept="Trigonometry", skill="Reasoning",
       hint=r"Use $\sin^2\theta + \cos^2\theta = 1$, and decide the sign of $\cos\theta$ for an obtuse angle."),
    # 37 B
    MC(r"Find the point of intersection of the lines $2x + y = 7$ and $x - y = 2$.", [
        C(r"$(1, 3)$", why="You swapped x and y. Check: 2(1) + 3 = 5, not 7."),
        C(r"$(3, 1)$", correct=True),
        C(r"$(2, 3)$", why=r"$(2, 3)$ is on $2x + y = 7$ but $2 - 3 \neq 2$. A point of intersection must satisfy both."),
        C(r"$(3, -1)$", why=r"From $x - y = 2$: $y = 3 - 2 = 1$. Sign slip."),
    ], steps=[S("Add the equations", math=r"3x = 9 \;\Rightarrow\; x = 3"),
              S("Find y", math=r"3 - y = 2 \;\Rightarrow\; y = 1")],
       concept="Coordinate geometry", skill="Calculation",
       hint="Solve the two equations simultaneously: adding them removes y."),
    # 38 D
    MC(r"From first principles, $\dfrac{d}{dx}(3x^2) = \lim_{h \to 0} \dfrac{3(x + h)^2 - 3x^2}{h}$. "
       r"What does the fraction simplify to **before** letting $h \to 0$?", [
        C("$6x$", why=r"6x is the limit. Before $h \to 0$ there is still a term in $h$."),
        C("$6x + h$", why=r"$3(x + h)^2 = 3x^2 + 6xh + 3h^2$: the 3 multiplies $h^2$ too."),
        C("$6x + 3h^2$", why=r"Divide **every** term by $h$: $\frac{3h^2}{h} = 3h$."),
        C("$6x + 3h$", correct=True),
    ], steps=[S("Expand", math=r"3(x + h)^2 - 3x^2 = 6xh + 3h^2"),
              S("Divide by h", math=r"\frac{6xh + 3h^2}{h} = 6x + 3h"),
              S("Then the limit", text=r"As $h \to 0$ this tends to $6x$.")],
       concept="Differentiation", skill="Concept",
       hint=r"Expand $3(x + h)^2$, cancel $3x^2$, then divide each term by $h$."),
    # 39 C
    MC(r"(Mechanics option) A force of 10 N acts at $60^\circ$ above the horizontal. Find its horizontal component.", [
        C("8.66 N", why=r"$10\sin 60^\circ$ is the **vertical** component."),
        C("10 N", why="The whole force does not act horizontally. Resolve it."),
        C("5 N", correct=True),
        C("0.5 N", why=r"$0.5$ is $\cos 60^\circ$ alone. Multiply by the 10 N."),
    ], steps=[S("Resolve", math=r"F\cos\theta = 10\cos 60^\circ"),
              S("Calculate", math=r"10 \times 0.5 = 5 \text{ N}")],
       concept="Mechanics", skill="Calculation",
       hint="The component along a direction is F cos(angle with that direction)."),
    # 40 A
    MC(r"In the expansion of $(1 + ax)^n$, the coefficient of $x$ is 12 and the coefficient of $x^2$ is 60. Find $n$.", [
        C("$6$", correct=True),
        C("$12$", why=r"12 is $na$, not $n$."),
        C("$2$", why="2 is the value of a, not n."),
        C("$11$", why=r"The $x^2$ term is $\binom{n}{2}(ax)^2$: you forgot to square $a$."),
    ], steps=[S("Two equations", math=r"na = 12, \qquad \frac{n(n - 1)}{2}a^2 = 60"),
              S("Substitute a = 12/n", math=r"\frac{n(n - 1)}{2} \cdot \frac{144}{n^2} = 60 \;\Rightarrow\; \frac{72(n - 1)}{n} = 60"),
              S("Solve", math=r"72n - 72 = 60n \;\Rightarrow\; n = 6 \;(a = 2)")],
       concept="Binomial expansion", skill="Reasoning",
       hint=r"Write $na = 12$ and $\binom{n}{2}a^2 = 60$, then eliminate $a$."),
]

# ---------------------------------------------------------------- Paper 2 mock
# Shared context: each part repeats it so it stands alone.
Q1 = r"$f(x) = 2x^3 + ax^2 + bx - 6$. $(x - 2)$ is a factor of $f(x)$, and when $f(x)$ is divided by $(x - 1)$ the remainder is $-12$. "
Q2 = r"A sector OAB of a circle with centre O has radius 6 cm and angle $AOB = 1.2$ radians. "
Q2E = r"This part is about the equation $2\cos^2\theta + 3\sin\theta - 3 = 0$ for $0 \le \theta \le 2\pi$. "
Q3 = r"This question is about the expansion of $(1 + 2x)^5$ in ascending powers of $x$. "
Q4 = r"A is the point $(1, 2)$ and B is the point $(7, 10)$. "
Q5 = r"A curve has equation $y = x^3 - 6x^2 + 9x + 1$. "
Q6 = r"The curve $y = 4x - x^2$ meets the x-axis at O(0, 0) and at A. "
Q7 = (r"(Mechanics option) A car starts from rest and accelerates uniformly at 2 m/s² for 5 s. It then travels at "
      r"constant speed for 10 s, and then decelerates uniformly to rest in 4 s. ")
Q8 = r"(Statistics option) A random variable $X$ takes the values 1, 2, 3, 4 with $P(X = x) = kx$. "
Q8B = (r"(Statistics option) Each seed in a farmer's packet germinates with probability 0.3, independently of the "
       r"others. Six seeds are planted and $Y$ is the number that germinate. ")

P2_QUESTIONS = [
    # ---------------------------------------------------------------- Question 1: polynomials
    MC("Question 1(a). " + Q1 + "Which pair of equations do $a$ and $b$ satisfy?", [
        C(r"$4a + 2b = -10$ and $a + b = -12$", why=r"$f(1) = 2 + a + b - 6$: you left out the 2 and the $-6$ when you set $f(1) = -12$."),
        C(r"$2a + b = -5$ and $a + b = -8$", correct=True),
        C(r"$2a + b = 5$ and $a + b = -8$", why=r"$16 + 4a + 2b - 6 = 0$ gives $4a + 2b = -10$: the 10 changes sign when it moves across."),
        C(r"$2a - b = 11$ and $a + b = -8$", why=r"You used $f(-2) = 0$. For the factor $(x - 2)$ use $f(2) = 0$."),
    ], steps=[S("Factor theorem", math=r"f(2) = 16 + 4a + 2b - 6 = 0 \;\Rightarrow\; 2a + b = -5"),
              S("Remainder theorem", math=r"f(1) = 2 + a + b - 6 = -12 \;\Rightarrow\; a + b = -8")],
       concept="Polynomials", skill="Reasoning",
       hint="Use the factor theorem with x = 2 and the remainder theorem with x = 1."),
    NUM("Question 1(b). " + Q1 + r"Given that $2a + b = -5$ and $a + b = -8$, find $a$.", 3,
        steps=[S("Subtract the equations", math=r"(2a + b) - (a + b) = -5 - (-8)"),
               S("Solve", math=r"a = 3")],
        concept="Polynomials", skill="Calculation",
        hint="Subtract the second equation from the first."),
    NUM("Question 1(c). " + Q1 + r"Given that $a = 3$, find $b$.", -11,
        steps=[S("Use a + b = −8", math=r"3 + b = -8"),
               S("Solve", math=r"b = -11")],
        concept="Polynomials", skill="Calculation",
        hint=r"Substitute $a = 3$ into $a + b = -8$, which comes from $f(1) = -12$."),
    MC("Question 1(d). " + r"$f(x) = 2x^3 + 3x^2 - 11x - 6$, and $(x - 2)$ is a factor. Factorize $f(x)$ completely.", [
        C(r"$(x - 2)(2x - 1)(x - 3)$", why=r"Expanding gives $2x^3 - 11x^2 + 17x - 6$, not $f(x)$. Check the signs in the brackets."),
        C(r"$(x - 2)(x + 1)(2x + 3)$", why=r"Expanding gives $2x^3 + x^2 - 7x - 6$, not $f(x)$."),
        C(r"$(x - 2)(2x + 1)(x + 3)$", correct=True),
        C(r"$(x + 2)(2x - 1)(x - 3)$", why=r"This has the factor $(x + 2)$, but we know $(x - 2)$ is a factor."),
    ], steps=[S("Divide by (x − 2)", math=r"f(x) = (x - 2)(2x^2 + 7x + 3)"),
              S("Factorize the quadratic", math=r"2x^2 + 7x + 3 = (2x + 1)(x + 3)"),
              S("Answer", math=r"f(x) = (x - 2)(2x + 1)(x + 3)")],
       concept="Polynomials", skill="Calculation",
       hint=r"Find the quadratic $Q(x)$ with $f(x) = (x - 2)Q(x)$, then factorize it."),
    NUM("Question 1(e). " + r"Express $\dfrac{5x + 5}{(x - 2)(x + 3)}$ in the form $\dfrac{A}{x - 2} + \dfrac{B}{x + 3}$. Find $A$.", 3,
        steps=[S("Multiply through", math=r"5x + 5 = A(x + 3) + B(x - 2)"),
               S("Put x = 2", math=r"15 = 5A \;\Rightarrow\; A = 3"),
               S("(Also) put x = −3", math=r"-10 = -5B \;\Rightarrow\; B = 2")],
        concept="Polynomials", skill="Calculation",
        hint="Multiply both sides by (x − 2)(x + 3), then choose the value of x that removes B."),
    # ---------------------------------------------------------------- Question 2: trigonometry
    NUM("Question 2(a). " + Q2 + "Find the length of the arc AB.", 7.2, tolerance=0.01, unit="cm",
        steps=[S("Arc length (θ in radians)", math=r"s = r\theta"),
               S("Substitute", math=r"s = 6 \times 1.2 = 7.2 \text{ cm}")],
        concept="Trigonometry", skill="Calculation",
        hint="Use the arc length formula for an angle in radians."),
    NUM("Question 2(b). " + Q2 + "Find the area of the sector OAB.", 21.6, tolerance=0.01, unit="cm²",
        steps=[S("Sector area (θ in radians)", math=r"A = \tfrac{1}{2}r^2\theta"),
               S("Substitute", math=r"A = \tfrac{1}{2} \times 36 \times 1.2 = 21.6 \text{ cm}^2")],
        concept="Trigonometry", skill="Calculation",
        hint="Use the sector area formula for an angle in radians."),
    MC("Question 2(c). " + Q2E + r"Using $\cos^2\theta = 1 - \sin^2\theta$, which equation in $\sin\theta$ do you obtain?", [
        C(r"$2\sin^2\theta + 3\sin\theta - 1 = 0$", why=r"$2(1 - \sin^2\theta) + 3\sin\theta - 3 = -2\sin^2\theta + 3\sin\theta - 1$. Multiplying by $-1$ changes every sign."),
        C(r"$2\sin^2\theta + 3\sin\theta - 5 = 0$", why=r"You replaced $\cos^2\theta$ by $\sin^2\theta - 1$. The identity gives $1 - \sin^2\theta$."),
        C(r"$\sin^2\theta - 3\sin\theta + 1 = 0$", why=r"The 2 multiplies the whole bracket: $2(1 - \sin^2\theta) = 2 - 2\sin^2\theta$."),
        C(r"$2\sin^2\theta - 3\sin\theta + 1 = 0$", correct=True),
    ], steps=[S("Substitute", math=r"2(1 - \sin^2\theta) + 3\sin\theta - 3 = 0"),
              S("Simplify", math=r"-2\sin^2\theta + 3\sin\theta - 1 = 0"),
              S("Multiply by −1", math=r"2\sin^2\theta - 3\sin\theta + 1 = 0")],
       concept="Trigonometry", skill="Reasoning",
       hint=r"Replace $\cos^2\theta$, expand the bracket and collect terms."),
    MC("Question 2(d). " + Q2E + r"It can be written as $(2\sin\theta - 1)(\sin\theta - 1) = 0$. Find all the solutions.", [
        C(r"$\theta = \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}$", correct=True),
        C(r"$\theta = \frac{\pi}{6}, \frac{5\pi}{6}$", why=r"$\sin\theta = 1$ gives a third solution, $\theta = \frac{\pi}{2}$."),
        C(r"$\theta = \frac{\pi}{6}, \frac{\pi}{2}, \frac{7\pi}{6}$", why=r"$\sin\frac{7\pi}{6} = -\frac{1}{2}$. The second solution of $\sin\theta = \frac{1}{2}$ is $\pi - \frac{\pi}{6}$."),
        C(r"$\theta = \frac{\pi}{3}, \frac{\pi}{2}, \frac{2\pi}{3}$", why=r"These come from $\sin\theta = \frac{\sqrt{3}}{2}$, not $\frac{1}{2}$."),
    ], steps=[S("Two equations", math=r"\sin\theta = \tfrac{1}{2} \quad \text{or} \quad \sin\theta = 1"),
              S("Solve the first", math=r"\theta = \tfrac{\pi}{6}, \; \pi - \tfrac{\pi}{6} = \tfrac{5\pi}{6}"),
              S("Solve the second", math=r"\theta = \tfrac{\pi}{2}")],
       concept="Trigonometry", skill="Calculation",
       hint="Set each bracket equal to zero and solve each equation in the given range."),
    # ---------------------------------------------------------------- Question 3: binomial expansion
    MC("Question 3(a). " + Q3 + "Which gives the first four terms?", [
        C(r"$1 + 10x + 20x^2 + 20x^3$", why=r"You left out the powers of 2: $(2x)^2 = 4x^2$ and $(2x)^3 = 8x^3$."),
        C(r"$1 + 10x + 40x^2 + 80x^3$", correct=True),
        C(r"$1 + 2x + 4x^2 + 8x^3$", why="You left out the binomial coefficients 5, 10 and 10."),
        C(r"$1 + 10x + 40x^2 + 40x^3$", why=r"The $x^3$ term is $\binom{5}{3}(2x)^3 = 10 \times 8x^3 = 80x^3$."),
    ], steps=[S("Binomial terms", math=r"1 + \binom{5}{1}(2x) + \binom{5}{2}(2x)^2 + \binom{5}{3}(2x)^3"),
              S("Simplify", math=r"1 + 10x + 40x^2 + 80x^3")],
       concept="Binomial expansion", skill="Calculation",
       hint=r"Use $\binom{5}{r}(2x)^r$ for $r = 0, 1, 2, 3$."),
    NUM("Question 3(b). " + Q3 + r"Given that $(1 + 2x)^5 = 1 + 10x + 40x^2 + 80x^3 + \dots$, find the coefficient of "
        r"$x^2$ in the expansion of $(1 + 2x)^5(1 - x)$.", 30,
        steps=[S("Terms that give x²", math=r"1 \times 40x^2 + (-x) \times 10x"),
               S("Add", math=r"40x^2 - 10x^2 = 30x^2")],
        concept="Binomial expansion", skill="Reasoning",
        hint=r"Which pairs of terms multiply to give $x^2$? There are two."),
    NUM("Question 3(c). " + Q3 + r"Use $(1 + 2x)^5 \approx 1 + 10x + 40x^2 + 80x^3$ with a suitable value of $x$ to "
        r"estimate $1.02^5$. Give your answer to 5 decimal places.", 1.10408, tolerance=0.00001,
        steps=[S("Choose x", math=r"1 + 2x = 1.02 \;\Rightarrow\; x = 0.01"),
               S("Substitute", math=r"1 + 0.1 + 0.004 + 0.00008"),
               S("Answer", math=r"1.02^5 \approx 1.10408")],
        concept="Binomial expansion", skill="Application",
        hint="Which value of x makes 1 + 2x equal to 1.02?"),
    # ---------------------------------------------------------------- Question 4: coordinate geometry
    NUM("Question 4(a). " + Q4 + "Find the length of AB.", 10, tolerance=0.01,
        steps=[S("Distance formula", math=r"AB = \sqrt{(7 - 1)^2 + (10 - 2)^2}"),
               S("Calculate", math=r"= \sqrt{36 + 64} = 10")],
        concept="Coordinate geometry", skill="Calculation",
        hint="Use Pythagoras with the change in x and the change in y."),
    MC("Question 4(b). " + Q4 + "Find the equation of the perpendicular bisector of AB.", [
        C(r"$4x - 3y = -2$", why=r"This line has gradient $\frac{4}{3}$, the gradient of AB itself. The bisector is perpendicular."),
        C(r"$3x + 4y = 36$", correct=True),
        C(r"$3x + 4y = 11$", why="This passes through A, not through the midpoint (4, 6) of AB."),
        C(r"$3x - 4y = -12$", why=r"This has gradient $+\frac{3}{4}$. The perpendicular gradient is $-\frac{3}{4}$."),
    ], steps=[S("Midpoint", math=r"\left(\frac{1 + 7}{2}, \frac{2 + 10}{2}\right) = (4, 6)"),
              S("Gradients", math=r"m_{AB} = \frac{8}{6} = \frac{4}{3}, \quad m_{\perp} = -\frac{3}{4}"),
              S("Equation", math=r"y - 6 = -\tfrac{3}{4}(x - 4) \;\Rightarrow\; 3x + 4y = 36")],
       concept="Coordinate geometry", skill="Calculation",
       hint="The perpendicular bisector passes through the midpoint of AB and is perpendicular to AB."),
    MC("Question 4(c). " + Q4 + "Find the equation of the circle with AB as a diameter.", [
        C(r"$(x - 4)^2 + (y - 6)^2 = 100$", why="100 is the square of the diameter. The radius is 5, so r² = 25."),
        C(r"$(x + 4)^2 + (y + 6)^2 = 25$", why=r"This has centre $(-4, -6)$. The centre $(a, b)$ gives $(x - a)^2 + (y - b)^2$."),
        C(r"$(x - 4)^2 + (y - 6)^2 = 5$", why="The right-hand side is r² = 25, not r."),
        C(r"$(x - 4)^2 + (y - 6)^2 = 25$", correct=True),
    ], steps=[S("Centre = midpoint of AB", math=r"(4, 6)"),
              S("Radius = half of AB", math=r"r = 5"),
              S("Equation", math=r"(x - 4)^2 + (y - 6)^2 = 25")],
       concept="Coordinate geometry", skill="Calculation",
       hint="The centre is the midpoint of the diameter and the radius is half its length."),
    MC("Question 4(d). " + r"The point P(8, 3) lies on the circle $(x - 4)^2 + (y - 6)^2 = 25$. Find the equation of the tangent to the circle at P.", [
        C(r"$4x - 3y = 23$", correct=True),
        C(r"$3x + 4y = 36$", why="This line passes through the centre: it contains the radius, not the tangent."),
        C(r"$4x + 3y = 41$", why=r"This has gradient $-\frac{4}{3}$. The tangent gradient is the negative reciprocal of $-\frac{3}{4}$, which is $+\frac{4}{3}$."),
        C(r"$4x - 3y = 7$", why="This has the right gradient but does not pass through P: 32 − 9 = 23."),
    ], steps=[S("Gradient of the radius CP", math=r"\frac{3 - 6}{8 - 4} = -\frac{3}{4}"),
              S("Tangent is perpendicular to the radius", math=r"m = \frac{4}{3}"),
              S("Equation", math=r"y - 3 = \tfrac{4}{3}(x - 8) \;\Rightarrow\; 4x - 3y = 23")],
       concept="Coordinate geometry", skill="Reasoning",
       hint="The tangent at P is perpendicular to the radius from the centre (4, 6) to P."),
    # ---------------------------------------------------------------- Question 5: differentiation
    MC("Question 5(a). " + Q5 + r"Find $\frac{dy}{dx}$.", [
        C(r"$3x^2 - 12x + 9$", correct=True),
        C(r"$3x^2 - 12x + 10$", why="The constant 1 differentiates to 0, and 9x differentiates to 9."),
        C(r"$x^2 - 6x + 9$", why="Multiply each term by its power: x³ → 3x², 6x² → 12x."),
        C(r"$3x^2 - 6x + 9$", why=r"$6x^2$ differentiates to $12x$, not $6x$."),
    ], steps=[S("Differentiate term by term", math=r"\frac{dy}{dx} = 3x^2 - 12x + 9")],
       concept="Differentiation", skill="Calculation",
       hint=r"Use $\frac{d}{dx}(x^n) = nx^{n - 1}$ on each term."),
    MC("Question 5(b). " + Q5 + r"Given that $\frac{dy}{dx} = 3x^2 - 12x + 9$, find the x-coordinates of the stationary points.", [
        C(r"$x = -1$ and $x = -3$", why=r"Sign slip: $3(x - 1)(x - 3) = 0$ gives positive roots."),
        C(r"$x = 1$ and $x = 3$", correct=True),
        C(r"$x = 2$ only", why=r"$x = 2$ is where $\frac{d^2y}{dx^2} = 0$, not where $\frac{dy}{dx} = 0$."),
        C(r"$x = 0$ and $x = 4$", why=r"These solve $3x^2 - 12x = 0$: you dropped the $+9$."),
    ], steps=[S("Set dy/dx = 0", math=r"3x^2 - 12x + 9 = 0"),
              S("Factorize", math=r"3(x - 1)(x - 3) = 0"),
              S("Solve", math=r"x = 1 \text{ or } x = 3")],
       concept="Differentiation", skill="Calculation",
       hint=r"Stationary points are where $\frac{dy}{dx} = 0$. Take out the common factor 3 first."),
    NUM("Question 5(c). " + Q5 + "The stationary points are at $x = 1$ and $x = 3$. The point at $x = 1$ is a maximum. "
        "Find the maximum value of $y$.", 5,
        steps=[S("Substitute x = 1 into y", math=r"y = 1 - 6 + 9 + 1"),
               S("Calculate", math=r"y = 5")],
        concept="Differentiation", skill="Calculation",
        hint="Substitute x = 1 into the equation of the curve, not into dy/dx."),
    MC("Question 5(d). " + Q5 + "Determine the nature of the stationary point at $x = 3$.", [
        C(r"Maximum, because $\frac{d^2y}{dx^2} = 6 > 0$", why=r"A positive second derivative means a **minimum**."),
        C(r"Minimum, because $\frac{d^2y}{dx^2} = -6 < 0$", why=r"$\frac{d^2y}{dx^2} = 6x - 12 = 6$ at $x = 3$; $-6$ is its value at $x = 1$."),
        C(r"Minimum, because $\frac{d^2y}{dx^2} = 6 > 0$", correct=True),
        C(r"Point of inflection, because $y = 1$ there", why=r"The value of $y$ does not decide the nature: use $\frac{d^2y}{dx^2}$."),
    ], steps=[S("Second derivative", math=r"\frac{d^2y}{dx^2} = 6x - 12"),
              S("At x = 3", math=r"6(3) - 12 = 6 > 0"),
              S("Conclusion", text="The second derivative is positive, so (3, 1) is a minimum point.")],
       concept="Differentiation", skill="Reasoning",
       hint=r"Find $\frac{d^2y}{dx^2}$ and look at its sign at $x = 3$."),
    MC("Question 5(e). " + Q5 + "Find the equation of the normal to the curve at the point where $x = 2$.", [
        C(r"$y = -3x + 9$", why="This is the tangent (gradient −3). The normal is perpendicular to it."),
        C(r"$3y = -x + 11$", why=r"The normal gradient is the **negative** reciprocal of $-3$, which is $+\frac{1}{3}$."),
        C(r"$3y = x + 1$", why=r"This has the right gradient but does not pass through $(2, 3)$."),
        C(r"$3y = x + 7$", correct=True),
    ], steps=[S("Point on the curve", math=r"y = 8 - 24 + 18 + 1 = 3 \;\Rightarrow\; (2, 3)"),
              S("Gradient of the tangent", math=r"\frac{dy}{dx} = 12 - 24 + 9 = -3"),
              S("Gradient of the normal", math=r"m = \frac{1}{3}"),
              S("Equation", math=r"y - 3 = \tfrac{1}{3}(x - 2) \;\Rightarrow\; 3y = x + 7")],
       concept="Differentiation", skill="Application",
       hint="Find the point and the gradient of the tangent at x = 2; the normal is perpendicular to the tangent."),
    # ---------------------------------------------------------------- Question 6: integration
    NUM("Question 6(a). " + r"Evaluate $\displaystyle\int_1^2 \left(3x^2 + \frac{2}{x^2}\right)dx$.", 8, tolerance=0.001,
        steps=[S("Write with powers", math=r"\int_1^2 (3x^2 + 2x^{-2})\,dx"),
               S("Integrate", math=r"\left[x^3 - 2x^{-1}\right]_1^2 = \left[x^3 - \frac{2}{x}\right]_1^2"),
               S("Evaluate", math=r"(8 - 1) - (1 - 2) = 7 + 1 = 8")],
        concept="Integration", skill="Calculation",
        hint=r"Write $\frac{2}{x^2}$ as $2x^{-2}$ before integrating."),
    NUM("Question 6(b). " + Q6 + "Find the area of the region enclosed by the curve and the x-axis. Give your answer to "
        "2 decimal places.", 10.67, tolerance=0.01,
        steps=[S("Find A", math=r"4x - x^2 = 0 \;\Rightarrow\; x(4 - x) = 0 \;\Rightarrow\; x = 0, \; 4"),
               S("Area integral", math=r"\int_0^4 (4x - x^2)\,dx = \left[2x^2 - \frac{x^3}{3}\right]_0^4"),
               S("Evaluate", math=r"32 - \frac{64}{3} = \frac{32}{3} \approx 10.67")],
        concept="Integration", skill="Calculation",
        hint="Find where the curve meets the x-axis to get the limits."),
    NUM("Question 6(c). " + Q6 + r"The line $y = x$ meets the curve at O and at a point B. Find the x-coordinate of B.", 3,
        steps=[S("Set equal", math=r"4x - x^2 = x"),
               S("Rearrange", math=r"x^2 - 3x = 0 \;\Rightarrow\; x(x - 3) = 0"),
               S("Answer", math=r"x = 3 \text{ (O is } x = 0)")],
        concept="Integration", skill="Calculation",
        hint="Solve 4x − x² = x."),
    NUM("Question 6(d). " + Q6 + r"The line $y = x$ meets the curve at O(0, 0) and B(3, 3). Find the area of the region "
        r"between the curve and the line.", 4.5, tolerance=0.01,
        steps=[S("Curve minus line (curve on top)", math=r"(4x - x^2) - x = 3x - x^2"),
               S("Integrate", math=r"\int_0^3 (3x - x^2)\,dx = \left[\frac{3x^2}{2} - \frac{x^3}{3}\right]_0^3"),
               S("Evaluate", math=r"\frac{27}{2} - 9 = 4.5")],
        concept="Integration", skill="Application",
        hint="Integrate (upper curve − lower line) between the two x-values where they meet."),
    # ---------------------------------------------------------------- Question 7: Mechanics option
    NUM("Question 7(a). " + Q7 + "Find the greatest speed of the car.", 10, unit="m/s",
        steps=[S("v = u + at", math=r"v = 0 + 2 \times 5 = 10 \text{ m/s}")],
        concept="Mechanics", skill="Calculation",
        hint="Use v = u + at for the first 5 seconds."),
    NUM("Question 7(b). " + Q7 + "The greatest speed is 10 m/s. Find the total distance travelled.", 145, tolerance=0.5, unit="m",
        steps=[S("Area under the velocity–time graph", text="The graph is a trapezium: up for 5 s, flat for 10 s, down for 4 s."),
               S("Each stage", math=r"\tfrac{1}{2}(5)(10) + 10(10) + \tfrac{1}{2}(4)(10) = 25 + 100 + 20"),
               S("Total", math=r"145 \text{ m}")],
        concept="Mechanics", skill="Application",
        hint="Sketch the velocity–time graph; the distance is the area under it."),
    NUM("Question 7(c). " + Q7 + "The greatest speed is 10 m/s. Find the magnitude of the deceleration.", 2.5,
        tolerance=0.01, unit="m/s²",
        steps=[S("Change in speed ÷ time", math=r"a = \frac{0 - 10}{4} = -2.5 \text{ m/s}^2"),
               S("Magnitude", math=r"2.5 \text{ m/s}^2")],
        concept="Mechanics", skill="Calculation",
        hint="The car loses 10 m/s in 4 s."),
    MC("Question 7(d). (Mechanics option) A box of mass 4 kg rests on a smooth horizontal floor. It is pulled by a "
       r"force of 20 N acting at $30^\circ$ above the horizontal. Find the acceleration of the box, to 3 significant figures.", [
        C("5 m/s²", why=r"Only the horizontal component $20\cos 30^\circ$ accelerates the box along the floor."),
        C("2.5 m/s²", why=r"You used $20\sin 30^\circ$, the vertical component."),
        C("4.33 m/s²", correct=True),
        C("17.3 m/s²", why=r"17.3 N is the horizontal **force**. Divide by the mass: $a = \frac{F}{m}$."),
    ], steps=[S("Horizontal component", math=r"20\cos 30^\circ = 17.32 \text{ N}"),
              S("Newton's second law", math=r"a = \frac{17.32}{4} = 4.33 \text{ m/s}^2")],
       concept="Mechanics", skill="Application",
       hint="Resolve the 20 N force horizontally, then use F = ma."),
    # ---------------------------------------------------------------- Question 8: Statistics option
    NUM("Question 8(a). " + Q8 + "Find $k$.", 0.1, tolerance=0.001,
        steps=[S("Probabilities add to 1", math=r"k + 2k + 3k + 4k = 10k = 1"),
               S("Solve", math=r"k = 0.1")],
        concept="Statistics", skill="Calculation",
        hint="Write the four probabilities in terms of k and make them add to 1."),
    NUM("Question 8(b). " + Q8 + r"Given that $k = 0.1$, find $E(X)$.", 3, tolerance=0.001,
        steps=[S("Probabilities", text="0.1, 0.2, 0.3, 0.4 for x = 1, 2, 3, 4."),
               S("Expectation", math=r"E(X) = 0.1 + 0.4 + 0.9 + 1.6 = 3")],
        concept="Statistics", skill="Calculation",
        hint="Multiply each value by its probability and add."),
    NUM("Question 8(c). " + Q8 + r"Given that $k = 0.1$ and $E(X) = 3$, find $\text{Var}(X)$.", 1, tolerance=0.001,
        steps=[S("E(X²)", math=r"E(X^2) = 1(0.1) + 4(0.2) + 9(0.3) + 16(0.4) = 10"),
               S("Variance", math=r"\text{Var}(X) = 10 - 3^2 = 1")],
        concept="Statistics", skill="Calculation",
        hint=r"Find $E(X^2)$ first, then subtract $[E(X)]^2$."),
    NUM("Question 8(d). " + Q8B + r"Find $P(Y = 2)$, to 3 decimal places.", 0.324, tolerance=0.001,
        steps=[S("Distribution", math=r"Y \sim B(6,\ 0.3)"),
               S("Formula", math=r"P(Y = 2) = \binom{6}{2}(0.3)^2(0.7)^4"),
               S("Calculate", math=r"15 \times 0.09 \times 0.2401 = 0.324")],
        concept="Statistics", skill="Calculation",
        hint=r"Use $P(Y = r) = \binom{n}{r}p^r(1 - p)^{n - r}$."),
    NUM("Question 8(e). " + Q8B + "Find the probability that at least one seed germinates, to 3 decimal places.", 0.882,
        tolerance=0.001,
        steps=[S("Complement", math=r"P(Y \ge 1) = 1 - P(Y = 0)"),
               S("Calculate", math=r"1 - 0.7^6 = 1 - 0.117649 = 0.882")],
        concept="Statistics", skill="Application",
        hint="At least one is everything except none."),
]

SETS = [
    practice_set(
        module="Applied option", topic="Statistics",
        title="Discrete random variables: mean and variance", lesson="discrete-random-variables-mean-variance",
        questions=STATS_1),
    practice_set(
        module="Applied option", topic="Statistics",
        title="The binomial distribution", lesson="binomial-distribution-probabilities",
        questions=STATS_2),
    practice_set(
        module="Examination", topic="Paper 1",
        title="Paper 1 mock exam A", lesson="addmaths-paper-1-multiple-choice-strategies",
        mock=True, time_limit_minutes=75,
        questions=P1_QUESTIONS),
    practice_set(
        module="Examination", topic="Paper 2",
        title="Paper 2 mock exam A", lesson="addmaths-paper-2-extended-response",
        mock=True, time_limit_minutes=120,
        questions=P2_QUESTIONS),
]
