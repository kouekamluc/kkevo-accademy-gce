"""Pure Mathematics with Statistics (A Level): the Examination lesson for Paper 3 (both years).

KKEVO draft content written against KKEVO's curriculum summary and the Board's 2023 Advanced Level
report for 0770. A reviewer checks it against the official syllabus before publishing. Practice-paper
timings are KKEVO practice settings, not official examination times. All data are invented for practice.
"""

from .dsl import *  # noqa: F403

COURSE = [("pure-mathematics-with-statistics", "lower-sixth"),
          ("pure-mathematics-with-statistics", "upper-sixth")]

LESSONS = []

# ---------------------------------------------------------------- Examination: Paper 3 strategy
LESSONS.append(lesson(
    module="Examination", topic="Paper 3",
    title="Paper 3 strategy: statistics and probability questions",
    slug="sex-paper-3-statistics-strategy",
    minutes=22,
    summary="Read statistics and probability questions carefully, choose and state the right model, set out working that earns credit, and check units, precision and sense, using the mistakes the Board's examiners report.",
    objectives=[
        "Use a routine of read, model, calculate, state and check on a statistics or probability question",
        "State the model and its conditions (events, distribution, hypotheses) before calculating",
        "Avoid the common errors that the Board's report lists for this paper",
        "Set out working, units and precision so that method and conclusion can be followed",
    ],
    key_concepts=["Paper 3 strategy", "Stating the model", "Setting out working", "Precision and units", "Checking for sense"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is the option paper: statistics and probability. Almost every mark in a statistics question comes from the same few habits: say which model you are using, write the formula before you put numbers in it, give the answer in context with the right precision, and ask whether it makes sense. The pure mathematics of the question is often easy. The slips happen in the reading and the setting out."),
        T("This lesson gives you a routine. It uses the mistakes that the Board's 2023 report lists for this paper, so you can see what has cost candidates marks."),
        H("What the Board says about the paper"),
        KEY("Facts from the Board's 2023 report", "These are the only facts about the papers this lesson states. Check the exact format of your own paper with your teacher.", cards=[
            ["Paper 1", "Fifty multiple-choice questions, all compulsory."],
            ["Paper 3", "Eight questions on the option (statistics and probability); candidates are to answer all eight."],
            ["Spread", "The report describes questions on probability, descriptive statistics, the Poisson and binomial distributions, continuous random variables, the normal distribution and its use to approximate the binomial, the distribution of the sample mean, hypothesis testing, and correlation and regression."],
        ]),
        KEY("KKEVO practice settings", "In KKEVO practice, Paper 3 practice paper A has about 20 auto-marked parts and a time limit of 150 minutes; Paper 1 mock exam B has 50 questions and a time limit of 90 minutes. These are KKEVO practice settings, not official examination times. Check the instructions on your real paper.", cards=[
            ["No choice", "All questions are compulsory, so a blank question loses every mark in it. Attempt every question and every part."],
            ["Time", "Spread time evenly over the questions. Do not spend long on one part."],
        ]),
        H("The routine"),
        D("Use these five steps on every question:", title="Read, model, calculate, state, check",
          formula=r"\text{1. Read} \to \text{2. Model} \to \text{3. Calculate} \to \text{4. State} \to \text{5. Check}",
          note="Read: underline what is asked. Model: name the distribution or the law and its conditions. Calculate: formula first, then numbers. State: the answer in context with units and a stated precision. Check: is it sensible?"),
        H("Step 1: read the question"),
        T("Read the whole question once before you start. Underline the key words and circle the numbers. Decide what each part wants: 'find', 'show that', 'estimate', 'test', 'comment'. A 'show that' question gives you the answer: your marks are for the steps that lead to it, so every step must be written."),
        T("Look for words that change the model. 'With replacement' or 'without replacement'. 'At least' or 'more than'. 'Independent'. 'Per hour' and 'in 3 hours'. 'Population' and 'sample'. 'Estimate'. Probability questions go wrong most often because a word was read as another."),
        MISTAKE("Mixing up independent and mutually exclusive", r"The Board's report notes that some candidates treated two events as independent, and others as mutually exclusive, without checking. Mutually exclusive means $P(A \cap B) = 0$. Independent means $P(A \cap B) = P(A)P(B)$. Do not assume either: test it with the numbers given, or use only the addition law $P(A \cup B) = P(A) + P(B) - P(A \cap B)$."),
        H("Step 2: state the model"),
        T("Write the model in one line before calculating. A fully stated model also earns marks if a calculation slip follows."),
        KEY("Models to name", "Write the model and its parameters.", cards=[
            ["Binomial", r"$X \sim B(n, p)$: fixed $n$, two outcomes, constant $p$, independent trials."],
            ["Poisson", r"$X \sim \text{Po}(\lambda)$: with $\lambda$ **for the period in the question**."],
            ["Normal", r"$X \sim N(\mu, \sigma^2)$: second parameter is the variance. For a sample mean: $N(\mu, \sigma^2/n)$."],
            ["Hypothesis test", r"$H_0$ and $H_1$ in terms of the **population** parameter ($\mu$, $p$ or $\lambda$), then the distribution under $H_0$."],
        ]),
        EX("Worked example 1: probability with the addition law", intro=r"$P(A) = 0.5$, $P(B) = 0.4$ and $P(A \cup B) = 0.8$ for two events $A$ and $B$. Find $P(A \cap B)$, say whether $A$ and $B$ are independent, and find $P(A \mid B)$.", steps=[
            S("Name the law", text="Addition law, rearranged so that the unknown is the subject."),
            S("Make the intersection the subject", math=r"P(A \cap B) = P(A) + P(B) - P(A \cup B) = 0.5 + 0.4 - 0.8 = 0.1"),
            S("Test independence", math=r"P(A)P(B) = 0.5 \times 0.4 = 0.2 \neq 0.1", text="The events are **not** independent. They are not mutually exclusive either, because $P(A \\cap B) \\neq 0$."),
            S("Conditional probability", math=r"P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{0.1}{0.4} = 0.25"),
        ], check=r"P(A \mid B) = 0.25 \neq P(A) = 0.5, \text{ which confirms the events are not independent}"),
        H("Step 3 and 4: calculate and state"),
        T("Write the formula, then substitute, then the value. Keep full calculator values and round only at the end. Give the answer to the precision asked (for example 3 decimal places, 3 significant figures) and with a unit where there is one. Say which table or calculator function you used when you read from a table."),
        EX("Worked example 2: a normal approximation", intro=r"$X \sim B(100, 0.4)$. Use a normal approximation to find $P(X \geq 45)$. Give your answer to 3 decimal places.", steps=[
            S("State why an approximation is reasonable", text=r"$n$ is large and $p$ is not close to $0$ or $1$ ($np = 40$ and $n(1-p) = 60$ are both well above $5$; check your textbook for the exact rule)."),
            S("Mean and variance", math=r"\mu = np = 40, \qquad \sigma^2 = np(1 - p) = 24, \qquad \sigma = 4.899"),
            S("State the approximation", math=r"X \approx Y \sim N(40,\ 24)"),
            S("Continuity correction: $X \\geq 45$ becomes $Y > 44.5$", math=r"P(Y > 44.5) = P\!\left(Z > \frac{44.5 - 40}{4.899}\right) = P(Z > 0.9186)"),
            S("Calculate and state", math=r"= 1 - 0.8208 = 0.1792", text="So $P(X \\geq 45) \\approx 0.179$ to 3 decimal places."),
        ], check=r"\text{exact binomial value } 0.1789 \text{ is very close}"),
        T(r"The Board's report says that candidates often failed to use the continuity correction, and could not state precisely when the normal approximation is allowed. 'n is large' is not enough: say that $p$ is not close to $0$ or $1$ as well, or give the product rule your textbook uses."),
        EX("Worked example 3: setting out a hypothesis test", intro=r"The mean daily rainfall in a month is claimed to be $24$ mm with standard deviation $5$ mm. In a random sample of $40$ days (invented for practice) the mean is $22.1$ mm. Test at the $5\%$ level whether the mean rainfall is less than $24$ mm.", steps=[
            S("Hypotheses", math=r"H_0: \mu = 24 \qquad H_1: \mu < 24", text="Written in terms of the **population** mean $\\mu$, with the direction taken from the word 'less'."),
            S("Distribution under $H_0$", math=r"\bar{X} \sim N\!\left(24, \frac{25}{40}\right), \qquad \text{standard error } 0.7906", text="The sample is large, so the central limit theorem applies."),
            S("State the rejection rule", text=r"Reject $H_0$ if $z < -1.645$."),
            S("Test statistic", math=r"z = \frac{22.1 - 24}{0.7906} = -2.403"),
            S("Conclusion in context", text=r"$-2.403 < -1.645$, so reject $H_0$. There is evidence at the 5% level that the mean daily rainfall is less than $24$ mm."),
        ], check=r"\text{p-value} = P(Z < -2.403) = 0.0081 < 0.05 \ \checkmark"),
        MISTAKE("Hypotheses about the sample mean, and the wrong tail", r"The Board's report notes that some candidates wrote the sample mean in the null hypothesis, wrote $\neq$ when the question said 'increased', and omitted the rejection rule, so no conclusion followed. Write $H_0$ and $H_1$ about $\mu$, take the direction from the words, state the rule before the conclusion."),
        H("Step 5: check"),
        T("Ask three questions at the end of every part. Is it in the right range (a probability must be between 0 and 1; a variance cannot be negative; a correlation coefficient is between -1 and 1)? Are the units right? Does it answer the question that was asked? One minute here catches most of the slips that the examiners report."),
        KEY("Other errors the Board's report lists for this paper", "Each is a small slip that costs marks. Check yourself against them.", cards=[
            ["Quartile deviation", r"It is $\frac{1}{2}(Q_3 - Q_1)$, the **semi**-interquartile range, not $Q_3 - Q_1$."],
            ["Cumulative frequency graph", "Plot the cumulative frequencies against the **upper class boundaries**, not mid-values or class limits and not the frequencies."],
            ["Poisson", r"Use the $\lambda$ for the period in the question; and $P(X > 2) = 1 - P(X \leq 2)$."],
            ["Continuous variables", r"Treat them with integrals, not sums; $F(x) = P(X \leq x) = \int f(t)\,dt$ from the lower end of the range up to $x$."],
            ["Regression", r"Do not mix the line of $y$ on $x$ with the line of $x$ on $y$; use the given summary values for the right quantities."],
        ]),
        QUIZ(r"In a question on a sample of size $n$ from a population with mean $\mu$ and variance $\sigma^2$, the Board's examiners report that candidates knew the sample mean was normal but lost marks. What is the **correct statement** of its distribution?",
             [r"$\bar{X} \sim N(\mu, \sigma^2)$", r"$\bar{X} \sim N\!\left(\mu, \dfrac{\sigma^2}{n}\right)$", r"$\bar{X} \sim N\!\left(n\mu, \sigma^2\right)$", r"$\bar{X} \sim N\!\left(\mu, \dfrac{\sigma}{n}\right)$"], 1,
             r"The mean is $\mu$ and the variance is $\sigma^2/n$.", hint="What happens to the variance when you average n observations?",
             feedback=["This is the distribution of one observation.", "", r"$n\mu$ is the mean of the **total**, not of the sample mean.", r"The variance is divided by $n$ as $\sigma^2/n$; $\sigma/n$ is neither the variance nor the standard deviation."]),
        QUIZ(r"A question says: 'The number of customers arriving at a kiosk in a $10$-minute period has a Poisson distribution with mean $3$. Find the probability that more than $2$ customers arrive in a $20$-minute period.' Which is the correct first line?",
             [r"$X \sim \text{Po}(3)$, find $1 - P(X \leq 2)$", r"$X \sim \text{Po}(6)$, find $1 - P(X \leq 2)$", r"$X \sim \text{Po}(6)$, find $1 - P(X \leq 3)$", r"$X \sim \text{Po}(6)$, find $P(X = 3)$"], 1,
             r"For $20$ minutes the mean is $2 \times 3 = 6$. 'More than $2$' is $1 - P(X \leq 2)$.", hint="Match the mean to the period, then translate 'more than 2'.",
             feedback=["The mean $3$ is for $10$ minutes, but the question asks about $20$ minutes.", "", r"$1 - P(X \leq 3)$ is $P(X > 3)$: 'more than 2' includes $3$.", "'More than 2' means all values above 2, not just 3."]),
        H("Practice questions"),
        PQ(r"$P(A) = 0.6$, $P(B) = 0.5$ and $P(A \cup B) = 0.8$. Find $P(A \cap B)$, say whether $A$ and $B$ are independent, and find $P(A \mid B)$.",
           r"$P(A \cap B) = 0.6 + 0.5 - 0.8 = 0.3$. $P(A)P(B) = 0.3 = P(A \cap B)$, so the events **are** independent. $P(A \mid B) = 0.3/0.5 = 0.6 = P(A)$, as expected for independent events."),
        PQ(r"$X \sim B(80, 0.25)$. Use a normal approximation to find $P(X \geq 25)$, to 3 decimal places, and state why the approximation is reasonable.",
           r"$n = 80$ is large and $p = 0.25$ is not close to $0$ or $1$ ($np = 20$, $n(1-p) = 60$). $\mu = 20$, $\sigma^2 = 15$, $\sigma = 3.873$. $P(X \geq 25) \approx P(Y > 24.5) = P(Z > 1.162) = 0.123$ (the exact value is $0.124$)."),
        PQ(r"A farmer believes that a new fertiliser has **increased** the mean yield from the usual $4.2$ tonnes per hectare. Write the hypotheses she should test and say whether the test is one-tailed or two-tailed.",
           r"$H_0: \mu = 4.2$, $H_1: \mu > 4.2$, where $\mu$ is the population mean yield with the new fertiliser. The test is one-tailed (upper), because the belief is that the mean has increased. The sample mean is used in the test statistic, not in the hypotheses."),
        PQ(r"The number of calls to a clinic in $10$ minutes is Poisson with mean $3$. Find the probability of more than $2$ calls in $10$ minutes, and in $20$ minutes, to 3 decimal places.",
           r"$10$ minutes: $X \sim \text{Po}(3)$, $P(X > 2) = 1 - P(X \leq 2) = 1 - 0.4232 = 0.577$. $20$ minutes: $X \sim \text{Po}(6)$, $P(X > 2) = 1 - P(X \leq 2) = 1 - 0.0620 = 0.938$."),
        H("Summary"),
        SUM("Read the whole question, underline what each part wants, and watch for words that change the model: with or without replacement, at least, per period, population or sample.",
            r"State the model before you calculate: the events and the law, or $B(n, p)$, $\text{Po}(\lambda)$, $N(\mu, \sigma^2)$, or $H_0$ and $H_1$ about the population parameter.",
            "Write the formula, then the numbers. Round only at the end, to the precision asked, with units, and say which table or function you used.",
            "In a hypothesis test: hypotheses, distribution under H0, rejection rule, test statistic, conclusion in context.",
            "Check every answer for sense. Learn the Board's listed slips: independent versus mutually exclusive, quartile deviation, plotting at upper class boundaries, the Poisson period, the continuity correction and the right regression line.",
            "The Board's report says candidates answer all eight questions of Paper 3: attempt every part, and ask your teacher to confirm the format of your own paper."),
    ],
))
