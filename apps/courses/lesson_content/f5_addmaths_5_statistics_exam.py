"""Form 5 Additional Mathematics (O Level 575): Applied option (Statistics) and the Examination module.

Draft content. The only exam facts stated here come from the syllabus outline in
apps/academics/gce_curriculum.py (Paper 1: 33.3%, multiple choice; Paper 2: 66.7%, extended response;
the applied part is an option, Mechanics or Statistics). Students are told to check the current GCE
Board instructions for the number of questions, the durations and everything else.
"""

from .dsl import *  # noqa: F403

COURSE = ("additional-mathematics", "form-5")

LESSONS = [
    # ------------------------------------------------------------------ Statistics 1
    lesson(
        module="Applied option", topic="Statistics",
        title="Discrete random variables: distributions, mean and variance",
        slug="discrete-random-variables-mean-variance",
        minutes=25,
        summary="Write the probability distribution of a discrete random variable in a table, use the fact that the "
                "probabilities add to 1 to find unknowns, and calculate E(X) and Var(X) = E(X²) − [E(X)]².",
        objectives=[
            "Recognise a valid probability distribution and find an unknown probability using ΣP = 1",
            "Find probabilities such as P(X ≥ 2) from a distribution table",
            "Calculate the expectation E(X) and use it to judge whether a game is fair",
            "Calculate E(X²), the variance Var(X) and the standard deviation",
        ],
        key_concepts=["Discrete random variable", "Probability distribution", "Sum of probabilities is 1",
                      "Expectation E(X)", "E(X²)", "Variance Var(X)", "Standard deviation", "Fair game"],
        blocks=[
            H("Introduction"),
            T("The applied part of Additional Mathematics is an **option**: you study **either Mechanics or "
              "Statistics**, not both. These two lessons are the Statistics option. If your school prepares you for "
              "the Mechanics option instead, use the Mechanics lessons."),
            T("A taxi driver in Yaoundé counts how many passengers he picks up on each trip from the junction: 1, 2, "
              "3 or 4. He cannot know the number before the trip, but after many trips he knows how likely each "
              "number is. Statistics turns this kind of information into a **probability distribution**, and from "
              "it we can find the average number and how much the numbers spread out."),
            T("You already know basic probability from General Mathematics (probabilities between 0 and 1, adding "
              "for 'or', multiplying for independent events). We build on that here."),
            H("Random variables and distributions"),
            D(r"A **discrete random variable** $X$ is a quantity that takes separate values $x_1, x_2, x_3, \dots$ "
              r"by chance. Its **probability distribution** gives the probability $P(X = x)$ of each value, usually "
              r"in a table.",
              title="Discrete random variable",
              formula=r"\sum P(X = x) = 1, \qquad 0 \le P(X = x) \le 1",
              note="Capital X names the random variable; small x stands for one of its values."),
            T(r"For example, the taxi driver's distribution might be: $x$ = 1, 2, 3, 4 with $P(X = x)$ = 0.1, 0.4, "
              r"0.3, 0.2. Every probability is between 0 and 1, and $0.1 + 0.4 + 0.3 + 0.2 = 1$, so this is a valid "
              r"distribution. The probability of 'at least 3 passengers' is $P(X \ge 3) = 0.3 + 0.2 = 0.5$."),
            KEY("Mean and spread of X", "Two numbers summarise a distribution.",
                cards=[["Expectation (mean)", r"$E(X) = \sum x\,P(X = x)$: multiply each value by its probability and add."],
                       ["E(X²)", r"$E(X^2) = \sum x^2\,P(X = x)$: square each value first, then multiply and add."],
                       ["Variance", r"$\text{Var}(X) = E(X^2) - [E(X)]^2$. The standard deviation is $\sqrt{\text{Var}(X)}$."]]),
            F(r"E(X) = \sum x\,P(X = x), \qquad \text{Var}(X) = E(X^2) - [E(X)]^2", title="Key formulas"),
            EX("Worked example 1: find an unknown, then E(X) and Var(X)", intro=(
                r"$X$ takes the values 0, 1, 2, 3 with probabilities $0.1$, $k$, $0.3$ and $2k$. Find $k$, "
                r"$E(X)$ and $\text{Var}(X)$."), steps=[
                S("The probabilities add to 1", math=r"0.1 + k + 0.3 + 2k = 1"),
                S("Solve for k", math=r"3k = 0.6 \;\Rightarrow\; k = 0.2"),
                S("Write the full distribution", text=r"$P(X = x)$ = 0.1, 0.2, 0.3, 0.4 for $x$ = 0, 1, 2, 3."),
                S("Expectation", math=r"E(X) = 0(0.1) + 1(0.2) + 2(0.3) + 3(0.4) = 2"),
                S("Find E(X²)", math=r"E(X^2) = 0(0.1) + 1(0.2) + 4(0.3) + 9(0.4) = 5"),
                S("Variance", math=r"\text{Var}(X) = 5 - 2^2 = 1"),
            ], check=r"0.1 + 0.2 + 0.3 + 0.4 = 1"),
            EX("Worked example 2: two unknowns", intro=(
                r"$X$ takes the values 1, 2, 3, 4 with probabilities $0.1$, $a$, $b$ and $0.2$. Given that "
                r"$E(X) = 2.6$, find $a$ and $b$, then find $\text{Var}(X)$."), steps=[
                S("Equation 1: the probabilities add to 1", math=r"0.1 + a + b + 0.2 = 1 \;\Rightarrow\; a + b = 0.7"),
                S("Equation 2: use E(X)", math=r"1(0.1) + 2a + 3b + 4(0.2) = 2.6 \;\Rightarrow\; 2a + 3b = 1.7"),
                S("Solve the simultaneous equations", text="From equation 1, $a = 0.7 - b$. Substitute:",
                  math=r"2(0.7 - b) + 3b = 1.7 \;\Rightarrow\; b = 0.3, \; a = 0.4"),
                S("Find E(X²)", math=r"E(X^2) = 1(0.1) + 4(0.4) + 9(0.3) + 16(0.2) = 7.6"),
                S("Variance", math=r"\text{Var}(X) = 7.6 - 2.6^2 = 7.6 - 6.76 = 0.84"),
            ], check=r"1(0.1) + 2(0.4) + 3(0.3) + 4(0.2) = 2.6"),
            TIP("Two unknowns need two equations: one from 'the probabilities add to 1' and one from the information "
                "given (usually E(X)). Solving them uses the simultaneous-equation skills from General Mathematics."),
            QUIZ("Which list could be the probabilities of a probability distribution?",
                 ["0.4, 0.4, 0.4", "0.6, −0.1, 0.5", "0.2, 0.5, 0.3", "0.3, 0.3, 0.3"], 2,
                 "All the probabilities must be between 0 and 1 and add to exactly 1. Only 0.2 + 0.5 + 0.3 = 1.",
                 hint="Check two things: is every number between 0 and 1, and is the total exactly 1?",
                 feedback=["These add to 1.2, which is more than 1.",
                           "They add to 1, but a probability can never be negative.", "",
                           "These add to 0.9, not 1."]),
            H("Expectation and fair games"),
            D("A game is **fair** when the player's expected gain is 0: on average the player neither wins nor loses "
              "money. Write the gain as the prize minus the cost of playing.",
              title="Fair game"),
            EX("Worked example 3: is the game fair?", intro=(
                "At a stall in Mokolo market, a player pays 200 FCFA to spin a wheel. With probability 0.1 the player "
                "receives 1000 FCFA, with probability 0.2 the player receives 500 FCFA, and otherwise nothing. "
                "Let $X$ be the player's gain in FCFA. Find $E(X)$ and decide whether the game is fair."), steps=[
                S("Gains (prize minus the 200 FCFA paid)", text="1000 − 200 = 800 FCFA, 500 − 200 = 300 FCFA, "
                                                                "and 0 − 200 = −200 FCFA."),
                S("Probabilities", math=r"P(X = 800) = 0.1, \; P(X = 300) = 0.2, \; P(X = -200) = 0.7"),
                S("Expectation", math=r"E(X) = 800(0.1) + 300(0.2) + (-200)(0.7) = 80 + 60 - 140 = 0"),
                S("Conclusion", text="The expected gain is 0 FCFA, so the game is fair."),
            ], check=r"0.1 + 0.2 + 0.7 = 1"),
            T(r"$E(X)$ is a **long-run average**. It need not be a value $X$ can take. A fair die has $E(X) = 3.5$, "
              "although no single roll shows 3.5."),
            H("Common mistakes"),
            MISTAKE("Using [E(X)]² in place of E(X²)",
                    r"$E(X^2)$ means square each value, then multiply by its probability and add. In worked example 1, "
                    r"$E(X^2) = 5$ but $[E(X)]^2 = 4$. The variance needs both: $5 - 4 = 1$."),
            MISTAKE("Forgetting to subtract in the variance",
                    r"$E(X^2)$ alone is not the variance. Always finish with $\text{Var}(X) = E(X^2) - [E(X)]^2$. "
                    "A variance can never be negative: if you get a negative answer, check your working."),
            MISTAKE("Using the prize as the gain",
                    "In a game, the gain is the prize minus the cost of playing. The player who loses has a gain of "
                    "minus the cost, not 0."),
            QUIZ(r"For a random variable, $E(X) = 1.5$ and $E(X^2) = 3$. Find $\text{Var}(X)$.",
                 ["$1.5$", "$0.75$", "$0.866$", "$5.25$"], 1,
                 r"$\text{Var}(X) = E(X^2) - [E(X)]^2 = 3 - 1.5^2 = 3 - 2.25 = 0.75$.",
                 hint=r"Square $E(X)$ before you subtract.",
                 feedback=[r"You subtracted $E(X)$, not $[E(X)]^2$: $3 - 1.5 = 1.5$.", "",
                           r"0.866 is $\sqrt{0.75}$, the standard deviation, not the variance.",
                           r"You added $[E(X)]^2$ instead of subtracting it."]),
            H("Practice questions"),
            PQ(r"$X$ takes the values 1, 2 and 3 with $P(X = x) = kx$. Find $k$, $E(X)$ and $\text{Var}(X)$.",
               r"$k + 2k + 3k = 1$, so $k = \frac{1}{6}$. "
               r"$E(X) = 1 \cdot \frac{1}{6} + 2 \cdot \frac{2}{6} + 3 \cdot \frac{3}{6} = \frac{14}{6} = \frac{7}{3}$. "
               r"$E(X^2) = \frac{1 + 8 + 27}{6} = 6$, so $\text{Var}(X) = 6 - \frac{49}{9} = \frac{5}{9}$."),
            PQ(r"$X$ takes the values 0, 1, 2, 3 with probabilities 0.15, 0.35, 0.3, 0.2. Find (a) $P(X \ge 2)$ "
               r"(b) $P(1 \le X < 3)$ (c) $E(X)$.",
               r"(a) $0.3 + 0.2 = 0.5$. (b) $X = 1$ or $2$: $0.35 + 0.3 = 0.65$ (3 is not included). "
               r"(c) $E(X) = 0 + 0.35 + 0.6 + 0.6 = 1.55$."),
            PQ(r"$X$ takes the values 2, 4, 6 with probabilities 0.25, 0.5, 0.25. Find $E(X)$, $\text{Var}(X)$ and the "
               "standard deviation of $X$ to 3 significant figures.",
               r"$E(X) = 0.5 + 2 + 1.5 = 4$. $E(X^2) = 4(0.25) + 16(0.5) + 36(0.25) = 1 + 8 + 9 = 18$. "
               r"$\text{Var}(X) = 18 - 16 = 2$. Standard deviation $= \sqrt{2} \approx 1.41$."),
            PQ("At a school fun-fair, a player pays 500 FCFA to roll a fair die. If the die shows a six, the player "
               "receives 2000 FCFA. Find the player's expected gain per game. Is the game fair?",
               r"Gain $= 2000 - 500 = 1500$ FCFA with probability $\frac{1}{6}$, and $-500$ FCFA with probability "
               r"$\frac{5}{6}$. $E(\text{gain}) = 1500 \times \frac{1}{6} - 500 \times \frac{5}{6} = 250 - 416.67 "
               r"\approx -167$ FCFA. The expected gain is not 0, so the game is not fair: on average the player loses "
               "about 167 FCFA per game."),
            SUM("The applied part is an option: you study Mechanics or Statistics. These lessons are the Statistics option.",
                "A probability distribution lists each value of X with its probability; the probabilities add to 1.",
                "Use ΣP = 1 (and E(X) if given) to find unknown probabilities.",
                r"$E(X) = \sum x\,P(X = x)$ is the long-run average; a game is fair when the expected gain is 0.",
                r"$\text{Var}(X) = E(X^2) - [E(X)]^2$, where $E(X^2) = \sum x^2 P(X = x)$; the standard deviation is its square root."),
        ],
    ),
    # ------------------------------------------------------------------ Statistics 2
    lesson(
        module="Applied option", topic="Statistics",
        title="The binomial distribution",
        slug="binomial-distribution-probabilities",
        minutes=25,
        summary="Recognise when the binomial distribution B(n, p) applies, use P(X = r) = nCr pʳ(1 − p)ⁿ⁻ʳ, find "
                "cumulative probabilities such as P(X ≤ 2) and 'at least one', and use the mean np and variance np(1 − p).",
        objectives=[
            "State the conditions for a binomial distribution and decide whether a situation fits them",
            "Calculate P(X = r) for X ~ B(n, p)",
            "Find cumulative probabilities such as P(X ≤ 2) and P(at least one) using the complement",
            "Use E(X) = np and Var(X) = np(1 − p), including finding n and p",
        ],
        key_concepts=["Binomial conditions", "B(n, p)", "Binomial probability formula", "nCr",
                      "Cumulative probability", "Complement: at least one", "Mean np", "Variance np(1 − p)"],
        blocks=[
            H("Introduction"),
            T("A farmer near Bafoussam plants 5 maize seeds. Each seed germinates with probability 0.8, whatever the "
              "other seeds do. How likely is it that exactly 4 germinate? That at least 4 do? Questions like this, "
              "with a fixed number of tries and 'success or failure' each time, use the **binomial distribution**."),
            T(r"You will need $\binom{n}{r}$ (also written ${}^nC_r$), the number of ways of choosing $r$ items from $n$. "
              r"It is the same number you met in the Binomial expansion topic, and your calculator has an nCr key."),
            H("When is a situation binomial?"),
            D("A random variable $X$ has a **binomial distribution** when it counts the number of successes in a "
              "situation where: (1) there is a **fixed number** $n$ of trials; (2) each trial has only **two "
              "outcomes**, success or failure; (3) the probability of success $p$ is **the same** for every trial; "
              r"(4) the trials are **independent**. We write $X \sim B(n, p)$.",
              title="Binomial conditions"),
            QUIZ("Which of these can be modelled by a binomial distribution?",
                 ["The number of rolls of a die until the first six appears",
                  "The total score from 10 rolls of a die",
                  "The number of red cards when 5 cards are drawn without replacement from a pack",
                  "The number of sixes in 10 rolls of a fair die"], 3,
                 r"Ten rolls (fixed $n$), success = a six, $p = \frac{1}{6}$ every time, and the rolls are independent: "
                 r"$X \sim B(10, \frac{1}{6})$.",
                 hint="Test each situation against the four conditions.",
                 feedback=["There is no fixed number of trials, so it is not binomial.",
                           "A total score is not a count of successes, and each roll has six outcomes.",
                           "Without replacement the probability changes from draw to draw, so the trials are not independent.",
                           ""]),
            H("The binomial formula"),
            D(r"If $X \sim B(n, p)$, the probability of exactly $r$ successes is given below. $\binom{n}{r}$ counts "
              r"the orders in which the $r$ successes can happen; $p^r$ is for the successes and $(1 - p)^{n - r}$ "
              r"for the failures.",
              title="Binomial probability",
              formula=r"P(X = r) = \binom{n}{r} p^r (1 - p)^{n - r}, \qquad r = 0, 1, 2, \dots, n"),
            EX("Worked example 1: germinating seeds", intro=(
                "Each maize seed germinates with probability 0.8, independently. A farmer plants 5 seeds. Find the "
                "probability that (a) exactly 4 germinate (b) at least 4 germinate."), steps=[
                S("Name the distribution", math=r"X \sim B(5,\ 0.8)"),
                S("(a) Use the formula with r = 4", math=r"P(X = 4) = \binom{5}{4}(0.8)^4(0.2)^1"),
                S("(a) Calculate", math=r"= 5 \times 0.4096 \times 0.2 = 0.4096"),
                S("(b) 'At least 4' means 4 or 5", math=r"P(X = 5) = (0.8)^5 = 0.32768"),
                S("(b) Add", math=r"P(X \ge 4) = 0.4096 + 0.32768 = 0.73728 \approx 0.737"),
            ]),
            IMG("f5a-binomial-b5-08.svg",
                alt="Bar chart of the binomial distribution B(5, 0.8). The bars for x = 0, 1, 2, 3, 4, 5 have heights "
                    "0.0003, 0.0064, 0.0512, 0.2048, 0.4096 and 0.3277. The bars for 4 and 5 are highlighted.",
                caption="Figure 1. X ~ B(5, 0.8). The highlighted bars add up to P(X ≥ 4) ≈ 0.737."),
            H("Cumulative probabilities and 'at least one'"),
            T(r"'At most 2' means $X \le 2$, that is 0, 1 or 2. 'Fewer than 2' means $X \le 1$. 'At least 1' means "
              r"$X \ge 1$. When the list of values is long, use the **complement**: "
              r"$P(X \ge 1) = 1 - P(X = 0)$."),
            EX("Worked example 2: at most 2", intro=(
                "In a town, 25% of moto-taxi drivers wear a helmet. Eight drivers are chosen at random. Find the "
                "probability that at most 2 of them wear a helmet, to 3 significant figures."), steps=[
                S("Name the distribution", math=r"X \sim B(8,\ 0.25)"),
                S("At most 2 means 0, 1 or 2", math=r"P(X \le 2) = P(X = 0) + P(X = 1) + P(X = 2)"),
                S("Each term", math=r"0.75^8 + 8(0.25)(0.75)^7 + 28(0.25)^2(0.75)^6"),
                S("Calculate", math=r"= 0.10011 + 0.26697 + 0.31146 = 0.67854"),
                S("Round at the end", math=r"P(X \le 2) \approx 0.679"),
            ]),
            EX("Worked example 3: at least one", intro=(
                "A machine makes bottle tops, and 5% of them are faulty, independently. A sample of 10 is taken. "
                "Find the probability that at least one is faulty, to 3 significant figures."), steps=[
                S("Name the distribution", math=r"X \sim B(10,\ 0.05)"),
                S("Use the complement", math=r"P(X \ge 1) = 1 - P(X = 0)"),
                S("None faulty", math=r"P(X = 0) = 0.95^{10} = 0.59874"),
                S("Answer", math=r"P(X \ge 1) = 1 - 0.59874 = 0.40126 \approx 0.401"),
            ]),
            H("Mean and variance"),
            D(r"If $X \sim B(n, p)$, the mean and variance are given by short formulas, so you do not need the full table.",
              title="Mean and variance of B(n, p)",
              formula=r"E(X) = np, \qquad \text{Var}(X) = np(1 - p)"),
            EX("Worked example 4: finding n and p", intro=(
                r"$X \sim B(n, p)$ with mean 6 and variance 4.2. Find $p$ and $n$."), steps=[
                S("Write two equations", math=r"np = 6, \qquad np(1 - p) = 4.2"),
                S("Divide the second by the first", math=r"1 - p = \frac{4.2}{6} = 0.7"),
                S("Find p", math=r"p = 0.3"),
                S("Find n", math=r"n = \frac{6}{0.3} = 20"),
            ], check=r"20 \times 0.3 \times 0.7 = 4.2"),
            H("Common mistakes"),
            MISTAKE("Leaving out nCr",
                    r"$P(X = 4)$ for $B(5, 0.8)$ is $5 \times 0.8^4 \times 0.2$. Without the $\binom{5}{4} = 5$ you count "
                    "only one order of the successes."),
            MISTAKE("Misreading 'at least' and 'at most'",
                    r"'At least 4' is 4 or more; 'at most 2' is 2 or fewer; 'fewer than 2' does not include 2. "
                    "Write the list of values before you calculate."),
            MISTAKE("Mixing up variance and standard deviation",
                    r"$np(1 - p)$ is the variance. The standard deviation is $\sqrt{np(1 - p)}$."),
            QUIZ(r"$X \sim B(10,\ 0.3)$. What is $E(X)$?", ["$3$", "$0.3$", "$7$", "$2.1$"], 0,
                 r"$E(X) = np = 10 \times 0.3 = 3$.",
                 hint=r"Use $E(X) = np$.",
                 feedback=["", "0.3 is the probability of one success, not the mean.",
                           r"7 is $n(1 - p)$, the expected number of failures.",
                           r"2.1 is the variance $np(1 - p)$."]),
            H("Practice questions"),
            PQ(r"$X \sim B(6,\ 0.5)$. Find $P(X = 2)$.",
               r"$P(X = 2) = \binom{6}{2}(0.5)^2(0.5)^4 = 15 \times \frac{1}{64} = \frac{15}{64} \approx 0.234$."),
            PQ("Each seed in a packet germinates with probability 0.3, independently. Four seeds are planted. Find the "
               "probability that at least one germinates.",
               r"$X \sim B(4, 0.3)$. $P(X \ge 1) = 1 - P(X = 0) = 1 - 0.7^4 = 1 - 0.2401 = 0.7599$."),
            PQ(r"$X \sim B(5,\ 0.1)$. Find $P(X \ge 2)$ to 3 significant figures.",
               r"$P(X \ge 2) = 1 - P(X = 0) - P(X = 1) = 1 - 0.9^5 - 5(0.1)(0.9)^4 = 1 - 0.59049 - 0.32805 = 0.08146 "
               r"\approx 0.0815$."),
            PQ(r"A binomial random variable has mean 4 and variance 2.4. Find $n$ and $p$.",
               r"$np = 4$ and $np(1 - p) = 2.4$. Dividing, $1 - p = 0.6$, so $p = 0.4$ and $n = 4 \div 0.4 = 10$."),
            SUM("Binomial conditions: fixed n, two outcomes, the same p, independent trials. Write X ~ B(n, p).",
                r"$P(X = r) = \binom{n}{r} p^r (1 - p)^{n - r}$.",
                "Write the list of values for 'at least', 'at most' and 'fewer than' before calculating.",
                r"Use the complement for 'at least one': $P(X \ge 1) = 1 - P(X = 0)$.",
                r"$E(X) = np$ and $\text{Var}(X) = np(1 - p)$; divide them to find $1 - p$."),
        ],
    ),
    # ------------------------------------------------------------------ Paper 1
    lesson(
        module="Examination", topic="Paper 1",
        title="Paper 1: multiple choice strategies for Additional Maths",
        slug="addmaths-paper-1-multiple-choice-strategies",
        minutes=25,
        summary="What we know about Additional Maths Paper 1 (33.3% of the mark, multiple choice, with an applied "
                "option) and five strategies: plan your time, substitute options back, test a value, differentiate "
                "to check, and estimate with a sketch.",
        objectives=[
            "State what Paper 1 is worth and plan a time budget once you know the official number of questions",
            "Eliminate options by substituting them back or testing a convenient value",
            "Check integration and other answers by working backwards",
            "Estimate with a sketch and avoid the common traps, such as degree mode",
        ],
        key_concepts=["Paper 1 format", "Applied option", "Time budget", "Substituting options back",
                      "Testing a value", "Working backwards", "Estimation", "Distractor"],
        blocks=[
            H("Introduction"),
            T("Paper 1 tests the **whole course** quickly: polynomials, trigonometry, binomial expansion, coordinate "
              "geometry, differentiation, integration and your applied option. Each question is short, so the skill is "
              "to be fast **and** careful."),
            D("Paper 1 counts for **33.3%** (one third) of the Additional Mathematics mark, and it is **multiple "
              "choice**: you choose one answer from the options given in each question.",
              title="Paper 1: what the syllabus tells us",
              note="The syllabus guide used for this course does not give the number of questions or the length of "
                   "the paper. Check the current GCE Board instructions (and ask your teacher) for the number of "
                   "questions, the time allowed, how to record answers and which calculators are allowed."),
            D("The applied part of the course is an **option**: you study **Mechanics or Statistics**. Answer the "
              "questions for the option you studied. Check the current GCE Board instructions for exactly how the "
              "option questions are set out on the paper.",
              title="The applied option",
              note="In the KKEVO Paper 1 mock, option questions start with '(Mechanics option)' or "
                   "'(Statistics option)'. Answer only your option's questions, as you would in the real exam. "
                   "Your mock score counts all 40 questions, so use the score by topic and ignore the option you do not study."),
            KEY("Your time budget",
                r"Time per question = total minutes ÷ number of questions. The KKEVO mock uses a practice timing of "
                r"75 minutes for 40 questions: $75 \div 40 \approx 1.9$ minutes each. When you know the official "
                "numbers, do the same division.",
                cards=[["First pass", "Answer every question you can do quickly. Mark the hard ones and move on."],
                       ["Second pass", "Return to the marked questions with the time you saved."],
                       ["Last minutes", "Make sure every question has an answer, recorded on the right line."]]),
            H("Strategy 1: substitute the options back"),
            EX("Worked example 1: factor theorem in reverse", intro=(
                r"Which of these is a factor of $f(x) = x^3 - 4x^2 + x + 6$? A: $(x + 2)$. B: $(x - 1)$. "
                r"C: $(x + 1)$. D: $(x + 3)$."), steps=[
                S("Use the factor theorem", text=r"$(x - a)$ is a factor when $f(a) = 0$. So test $a = -2, 1, -1, -3$."),
                S("Test B first (easiest)", math=r"f(1) = 1 - 4 + 1 + 6 = 4 \neq 0"),
                S("Test C", math=r"f(-1) = -1 - 4 - 1 + 6 = 0 \;\checkmark"),
                S("Answer", text=r"**C**. A wrong option often comes from a sign slip: $(x + 2)$ means testing $x = -2$, not $x = 2$."),
            ], check=r"f(x) = (x + 1)(x - 2)(x - 3)"),
            H("Strategy 2: test a convenient value"),
            EX("Worked example 2: an identity", intro=(
                r"Simplify $\dfrac{1 - \cos^2\theta}{\sin\theta\cos\theta}$. A: $\sin\theta$. B: $\tan\theta$. "
                r"C: $\cot\theta$. D: $1$."), steps=[
                S("Choose a value that separates the options", text=r"$\theta = \frac{\pi}{4}$ makes $\tan\theta$, "
                  r"$\cot\theta$ and 1 all equal, so it cannot decide. Use $\theta = \frac{\pi}{3}$ instead."),
                S("Value of the expression", math=r"\frac{1 - \frac{1}{4}}{\frac{\sqrt{3}}{2} \cdot \frac{1}{2}} "
                  r"= \frac{3/4}{\sqrt{3}/4} = \sqrt{3}"),
                S("Compare", text=r"$\tan\frac{\pi}{3} = \sqrt{3}$, while $\sin\frac{\pi}{3} \approx 0.866$ and "
                                  r"$\cot\frac{\pi}{3} \approx 0.577$."),
                S("Answer, confirmed by algebra", math=r"\frac{\sin^2\theta}{\sin\theta\cos\theta} = \frac{\sin\theta}{\cos\theta} = \tan\theta \quad (\textbf{B})"),
            ]),
            TIP("Your calculator must be in **radian** mode when angles are in radians (as in the example above) and in "
                "degree mode when they are in degrees. Check the mode at the start of the paper."),
            H("Strategy 3: work backwards"),
            EX("Worked example 3: check an integral by differentiating", intro=(
                r"Find $\int (6x^2 - 2x)\,dx$. A: $12x - 2 + c$. B: $2x^3 - x^2 + c$. C: $6x^3 - 2x^2 + c$. "
                r"D: $3x^3 - x^2 + c$."), steps=[
                S("Differentiate each option", text="The right answer differentiates back to $6x^2 - 2x$."),
                S("A", text="A is the derivative of the expression, not its integral. Eliminate."),
                S("Test B", math=r"\frac{d}{dx}(2x^3 - x^2) = 6x^2 - 2x \;\checkmark"),
                S("Answer", text=r"**B**. C forgot to divide by the new power; D divided $6x^2$ by 2 instead of 3."),
            ]),
            H("Strategy 4: estimate with a sketch"),
            EX("Worked example 4: an area", intro=(
                r"Find the area enclosed by $y = 4 - x^2$ and the x-axis. A: $\frac{16}{3}$. B: $8$. "
                r"C: $\frac{32}{3}$. D: $\frac{64}{3}$."), steps=[
                S("Sketch", text=r"The curve is an upside-down parabola that crosses the x-axis at $x = -2$ and "
                                 r"$x = 2$, with its top at $(0, 4)$."),
                S("Box it in", text=r"The region fits inside a 4 by 4 rectangle (area 16) and contains the triangle "
                                    r"with vertices $(-2, 0)$, $(2, 0)$, $(0, 4)$ (area 8). So the answer is between 8 and 16."),
                S("Eliminate", text=r"Only C ($\approx 10.7$) is between 8 and 16. A is too small and D too large."),
                S("Confirm if time allows", math=r"\int_{-2}^{2} (4 - x^2)\,dx = \left[4x - \tfrac{x^3}{3}\right]_{-2}^{2} = \tfrac{16}{3} + \tfrac{16}{3} = \tfrac{32}{3}"),
            ]),
            H("Common traps"),
            MISTAKE("Sign slips in the factor theorem",
                    r"$(x + 3)$ is a factor when $f(-3) = 0$, not $f(3) = 0$. Many wrong options are built from this slip."),
            MISTAKE("Testing a value that does not separate the options",
                    r"If two options give the same value for your test (like $\tan\frac{\pi}{4} = \cot\frac{\pi}{4}$), "
                    r"choose another value. Avoid 0 and $\frac{\pi}{4}$ for trigonometry tests."),
            MISTAKE("Spending too long on one question",
                    "Every multiple-choice question carries the same weight. Mark a hard question, move on, and come "
                    "back on the second pass."),
            QUIZ("According to the syllabus, what share of the Additional Mathematics mark does Paper 1 carry?",
                 ["66.7%", "50%", "33.3%", "30%"], 2,
                 "Paper 1 is 33.3% (one third) of the mark; Paper 2 is 66.7%.",
                 hint="Paper 1 is the smaller of the two papers.",
                 feedback=["66.7% is Paper 2, the extended-response paper.",
                           "The two papers are not equal: Paper 2 carries twice the weight of Paper 1.", "",
                           "30% is the General Mathematics Paper 1, a different subject."]),
            QUIZ(r"Which value of $x$ is a root of $2x^3 - 3x^2 - 3x + 2 = 0$?",
                 ["$1$", "$2$", "$3$", "$-2$"], 1,
                 r"$2(8) - 3(4) - 3(2) + 2 = 16 - 12 - 6 + 2 = 0$.",
                 hint="Substitute each option into the left-hand side.",
                 feedback=[r"$2 - 3 - 3 + 2 = -2 \neq 0$.", "", r"$54 - 27 - 9 + 2 = 20 \neq 0$.",
                           r"$-16 - 12 + 6 + 2 = -20 \neq 0$."]),
            H("Practice questions"),
            PQ(r"Find the coefficient of $x^2$ in the expansion of $(1 - 2x)^5$. A: $-40$. B: $-10$. C: $10$. D: $40$.",
               r"**D**. The term is $\binom{5}{2}(-2x)^2 = 10 \times 4x^2 = 40x^2$. A squared term is positive, which "
               r"removes A and B at once; C forgets to square the 2."),
            PQ(r"Find the gradient of the tangent to $y = x^2 - 4x + 1$ at $x = 3$. A: $-2$. B: $2$. C: $6$. D: $-4$.",
               r"**B**. $\frac{dy}{dx} = 2x - 4$, so at $x = 3$ the gradient is $6 - 4 = 2$. C is $2x$ alone; "
               r"A and D are sign slips. A quick sketch of the parabola (minimum at $x = 2$) shows the curve is rising at $x = 3$, so the gradient is positive."),
            PQ(r"Find the centre and radius of the circle $x^2 + y^2 - 4x + 6y - 3 = 0$. A: $(2, -3)$, 4. "
               r"B: $(-2, 3)$, 4. C: $(2, -3)$, $\sqrt{3}$. D: $(-4, 6)$, 3.",
               r"**A**. The centre is $(2, -3)$: halve the coefficients of $x$ and $y$ and change the signs. "
               r"$r = \sqrt{2^2 + (-3)^2 + 3} = \sqrt{16} = 4$. B forgets to change the signs; C uses only the constant."),
            PQ(r"(Statistics option) $X \sim B(4, 0.5)$. Find $P(X = 2)$. A: $0.25$. B: $0.375$. C: $0.5$. D: $0.0625$. "
               r"(Mechanics option) A cyclist moving at 4 m/s accelerates at 2 m/s² for 3 s. Find her final speed. "
               r"A: 6 m/s. B: 10 m/s. C: 12 m/s. D: 24 m/s.",
               r"Statistics: **B**. $\binom{4}{2}(0.5)^4 = \frac{6}{16} = 0.375$; D leaves out $\binom{4}{2}$. "
               r"Mechanics: **B**. $v = u + at = 4 + 2 \times 3 = 10$ m/s; A is $at$ alone "
               r"($2 \times 3 = 6$, forgetting the starting speed), C is $u \times t$ and D multiplies all three numbers. Answer only the option you studied."),
            SUM("Paper 1: 33.3% of the mark, multiple choice. Check the current GCE Board instructions for the number "
                "of questions and the time allowed.",
                "The applied part is an option (Mechanics or Statistics): answer the questions for your option.",
                "Plan a time budget (total minutes ÷ number of questions) and work in two passes.",
                "Eliminate by substituting options back, testing a value that separates them, or working backwards.",
                "Sketch and estimate to remove options that are too big or too small; keep the calculator in the right angle mode."),
        ],
    ),
    # ------------------------------------------------------------------ Paper 2
    lesson(
        module="Examination", topic="Paper 2",
        title="Paper 2: extended response, setting out full solutions",
        slug="addmaths-paper-2-extended-response",
        minutes=25,
        summary="What we know about Paper 2 (66.7% of the mark, extended response) and how to set out full "
                "solutions: show every step, answer 'show that' and 'hence' correctly, give exact or rounded answers "
                "as asked, and justify stationary points.",
        objectives=[
            "State what Paper 2 is worth and what an extended-response answer needs",
            "Set out a full solution with the method, the working and a clear final answer",
            "Respond correctly to 'show that', 'hence', 'exact' and 'to 3 significant figures'",
            "Justify conclusions such as the nature of a stationary point or a tangency",
        ],
        key_concepts=["Paper 2 format", "Extended response", "Showing working", "Show that", "Hence",
                      "Exact answers", "Accuracy", "Justifying conclusions"],
        blocks=[
            H("Introduction"),
            T("Paper 2 is where two thirds of your Additional Mathematics mark is earned. Its questions are longer and "
              "in parts, and the examiner reads your **method**, not only your answer. A tidy, complete solution is "
              "like a well-built road from Douala to Yaoundé: every step connects to the next, and anyone can follow it."),
            D("Paper 2 counts for **66.7%** (two thirds) of the Additional Mathematics mark, and it is **extended "
              "response**: you write full solutions, often in several parts.",
              title="Paper 2: what the syllabus tells us",
              note="The syllabus guide used for this course does not give the number of questions, the choice of "
                   "questions or the length of the paper. Check the current GCE Board instructions and your teacher "
                   "for these details."),
            T("The applied part is an option, so answer the Mechanics **or** the Statistics questions, whichever you "
              "studied. The KKEVO Paper 2 mock has a practice timing of 120 minutes (a KKEVO choice, not an official "
              "time); its two option questions are labelled, and you answer only yours."),
            KEY("What a full solution contains", "Every part of an extended answer has the same three layers.",
                cards=[["Method", "Write the rule or formula you use: the factor theorem, dy/dx = 0, the area integral."],
                       ["Working", "One step per line, each line following from the one before."],
                       ["Answer", "A clear final line with the accuracy and units asked for, and a sentence where a conclusion is needed."]]),
            H("Command words"),
            D(r"**Show that**: the answer is given, so the marks are for a complete argument that reaches it. "
              r"**Hence**: use the result you have just found. **Exact**: leave answers as fractions, surds or "
              r"multiples of $\pi$. **To 3 significant figures**: keep full values in your working and round only "
              "at the end.",
              title="What the question words ask for"),
            EX("Worked example 1: 'show that' then 'hence'", intro=(
                r"$f(x) = x^3 - x^2 - 4x + 4$. (a) Show that $(x - 2)$ is a factor of $f(x)$. (b) Hence solve "
                r"$f(x) = 0$."), steps=[
                S("(a) State the method", text=r"By the factor theorem, $(x - 2)$ is a factor if $f(2) = 0$."),
                S("(a) Substitute and conclude", math=r"f(2) = 8 - 4 - 8 + 4 = 0, \text{ so } (x - 2) \text{ is a factor.}"),
                S("(b) 'Hence': divide by (x − 2)", math=r"f(x) = (x - 2)(x^2 + x - 2)"),
                S("(b) Factorize the quadratic", math=r"f(x) = (x - 2)(x + 2)(x - 1)"),
                S("(b) Solve", math=r"x = 2, \; x = -2 \text{ or } x = 1"),
            ], check=r"(x - 2)(x^2 + x - 2) = x^3 - x^2 - 4x + 4"),
            T("In (a), a bare '= 0' is not enough: write the conclusion in words. In (b), 'hence' tells you to use "
              "the factor from (a), not to start again."),
            EX("Worked example 2: stationary points with justification", intro=(
                r"Find the coordinates of the stationary points of $y = x^3 - 3x^2 - 9x + 5$ and determine their nature."), steps=[
                S("Differentiate", math=r"\frac{dy}{dx} = 3x^2 - 6x - 9"),
                S("Set dy/dx = 0", math=r"3(x^2 - 2x - 3) = 0 \;\Rightarrow\; 3(x - 3)(x + 1) = 0"),
                S("x-coordinates", math=r"x = 3 \text{ or } x = -1"),
                S("y-coordinates", math=r"x = 3: y = 27 - 27 - 27 + 5 = -22; \quad x = -1: y = -1 - 3 + 9 + 5 = 10"),
                S("Second derivative", math=r"\frac{d^2y}{dx^2} = 6x - 6"),
                S("Nature, with reasons", text=r"At $x = 3$: $6(3) - 6 = 12 > 0$, so $(3, -22)$ is a **minimum**. "
                  r"At $x = -1$: $6(-1) - 6 = -12 < 0$, so $(-1, 10)$ is a **maximum**."),
            ]),
            EX("Worked example 3: an exact area", intro=(
                r"Find the exact area of the region enclosed by the curve $y = x^2$ and the line $y = 2x$."), steps=[
                S("Find where they meet", math=r"x^2 = 2x \;\Rightarrow\; x(x - 2) = 0 \;\Rightarrow\; x = 0 \text{ or } x = 2"),
                S("Which is on top?", text=r"At $x = 1$: the line gives 2 and the curve gives 1, so the line is above."),
                S("Set up the integral", math=r"\text{Area} = \int_0^2 (2x - x^2)\,dx"),
                S("Integrate", math=r"= \left[x^2 - \frac{x^3}{3}\right]_0^2 = 4 - \frac{8}{3}"),
                S("Exact answer", math=r"= \frac{4}{3} \text{ square units}"),
            ]),
            TIP("If the question says 'exact', 1.33 loses the accuracy mark: write 4/3. If it asks for 3 significant "
                "figures, give 1.33. When it says neither, an exact answer is always safe."),
            H("Common mistakes"),
            MISTAKE("Stating a 'show that' result without the argument",
                    "The answer is already printed on the paper, so writing it down earns nothing. The marks are for the "
                    "steps and the concluding sentence."),
            MISTAKE("Ignoring 'hence'",
                    "If a part says 'hence', use the previous result. A method that ignores it may not earn the marks, "
                    "and it usually takes longer."),
            MISTAKE("Naming a maximum or minimum without a reason",
                    "Give the evidence: the sign of the second derivative, or the sign of dy/dx on each side of the point."),
            MISTAKE("Rounding in the middle",
                    "Keep full calculator values (or exact fractions) until the last line. Rounding early can change the "
                    "final answer."),
            QUIZ("According to the syllabus, what share of the Additional Mathematics mark does Paper 2 carry?",
                 ["33.3%", "66.7%", "70%", "100%"], 1,
                 "Paper 2 is 66.7% (two thirds) of the mark; Paper 1 is the other 33.3%.",
                 hint="The two papers together make 100%, and Paper 1 is 33.3%.",
                 feedback=["33.3% is Paper 1, the multiple-choice paper.", "",
                           "70% is the General Mathematics Paper 2, a different subject.",
                           "Paper 1 also counts, so Paper 2 cannot be the whole mark."]),
            QUIZ(r"Part (a) asks you to show that $(x - 2)$ is a factor of $f(x)$. Part (b) says 'Hence solve "
                 r"$f(x) = 0$'. What should you do in (b)?",
                 ["Start again with a new method, such as a graph",
                  "Write only the answer x = 2",
                  "Divide f(x) by (x − 2), factorize the quadratic and give all the roots",
                  "Show again that f(2) = 0"], 2,
                 "'Hence' means use the result of (a): (x − 2) is a factor, so divide by it and solve what is left.",
                 hint="What does 'hence' tell you to use?",
                 feedback=["'Hence' tells you to use part (a). A new method may not earn the marks.",
                           "x = 2 is only one root; a cubic can have three.", "",
                           "That repeats part (a) and does not solve the equation."]),
            H("Practice questions"),
            PQ(r"Find the equation of the normal to the curve $y = x^2 - 3x + 4$ at the point where $x = 2$.",
               r"Point: $y = 4 - 6 + 4 = 2$, so $(2, 2)$. Gradient of the tangent: $\frac{dy}{dx} = 2x - 3 = 1$ at $x = 2$. "
               r"Gradient of the normal: $-1$ (the negative reciprocal). Equation: $y - 2 = -1(x - 2)$, so $y = -x + 4$."),
            PQ(r"Show that the line $y = x + 4$ is a tangent to the circle $x^2 + y^2 = 8$, and find the point of contact.",
               r"Substitute: $x^2 + (x + 4)^2 = 8 \Rightarrow 2x^2 + 8x + 8 = 0 \Rightarrow x^2 + 4x + 4 = 0$. "
               r"The discriminant is $16 - 16 = 0$, so the line meets the circle at exactly one point: it is a tangent. "
               r"$(x + 2)^2 = 0$ gives $x = -2$, $y = 2$. Point of contact: $(-2, 2)$."),
            PQ(r"Expand $\left(1 + \frac{x}{2}\right)^6$ in ascending powers of $x$ up to the term in $x^3$. Hence find "
               r"the value of $1.005^6$ to 6 decimal places.",
               r"$\left(1 + \frac{x}{2}\right)^6 = 1 + 6\left(\frac{x}{2}\right) + 15\left(\frac{x}{2}\right)^2 + 20\left(\frac{x}{2}\right)^3 + \dots "
               r"= 1 + 3x + \frac{15}{4}x^2 + \frac{5}{2}x^3 + \dots$ "
               r"Hence: $1 + \frac{x}{2} = 1.005$ when $x = 0.01$, so $1.005^6 \approx 1 + 0.03 + 0.000375 + 0.0000025 = 1.0303775 \approx 1.030378$."),
            SUM("Paper 2: 66.7% of the mark, extended response. Check the current GCE Board instructions for the number "
                "of questions, any choice and the time allowed.",
                "Answer the applied questions for your option only: Mechanics or Statistics.",
                "Every part needs the method, the working line by line, and a clear final answer.",
                "'Show that' needs a complete argument and a conclusion; 'hence' means use the previous result.",
                "Give exact answers when asked; otherwise round only at the end to the accuracy stated.",
                "Justify conclusions, for example with the sign of the second derivative or the discriminant."),
        ],
    ),
]
