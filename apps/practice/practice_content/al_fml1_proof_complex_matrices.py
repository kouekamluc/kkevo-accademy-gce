"""Further Mathematics (A Level, Lower Sixth): practice sets for Proof, Series & Theory of Equations, Complex Numbers, and Matrices, Determinants & Linear Systems (one set per lesson).

KKEVO draft content. A reviewer checks it against the official GCE Board syllabus before publishing.
"""

from .dsl import *  # noqa: F403

COURSE = ("further-mathematics", "lower-sixth")

M1 = "Proof, Series & Theory of Equations"
M2 = "Complex Numbers"
M3 = "Matrices, Determinants & Linear Systems"

SETS = []

# ------------------------------------------------------------------ Induction beyond sums
SETS.append(practice_set(
    module=M1, topic="Proof by induction",
    title="Induction on matrices, derivatives, inequalities and recurrences", lesson="fml1-induction-beyond-sums",
    questions=[
        MC(r"A sequence is defined by $u_{n+2} = 6u_{n+1} - 5u_n$. A proof by induction of a formula for $u_n$ needs", [
            C("one base case, $n = 1$", why=r"The step uses both $u_k$ and $u_{k+1}$, so one starting value leaves the link from $n=1$ to $n=2$ unproved."),
            C(r"two base cases, $n = 1$ and $n = 2$, and an assumption for $n = k$ and $n = k+1$", correct=True),
            C(r"one base case, $n = 0$", why="The natural starting value is the first term given. $n = 0$ is not used here and one value is still not enough."),
            C("no base case, because the rule defines every term", why="The rule needs starting values, and the proof must check them against the formula."),
        ], steps=[S("What does the step use?", text=r"$u_{k+2}$ depends on $u_{k+1}$ and $u_k$."), S("Hence", text="The assumption covers two values of $n$, so two base cases are checked.")],
           concept="Two base cases for a recurrence", skill="Concept", hint="Count how many earlier terms the rule uses to build the next one.",
           feedback="A rule that looks back two terms needs two base cases and a two-value assumption."),
        MC(r"In a proof by induction about $\mathbf{A}^n$, the inductive step finds $\mathbf{A}^{k+1}$ by", [
            C(r"$\mathbf{A}^k + \mathbf{A}$", why="Powers are repeated multiplication, not addition."),
            C(r"$k\,\mathbf{A}^k$", why=r"Multiplying by the number $k$ is not the same as multiplying by $\mathbf{A}$."),
            C(r"$\mathbf{A}^k\mathbf{A}$, using the assumed formula for $\mathbf{A}^k$", correct=True),
            C(r"$\left(\mathbf{A}^k\right)^{k+1}$", why=r"This raises to the power $k+1$ again. It equals $\mathbf{A}^{k(k+1)}$, not $\mathbf{A}^{k+1}$."),
        ], steps=[S("Definition of a power", math=r"\mathbf{A}^{k+1} = \mathbf{A}^k\mathbf{A}"), S("Use the assumption", text=r"Replace $\mathbf{A}^k$ by the assumed matrix and multiply.")],
           concept="Inductive step for matrix powers", skill="Concept", hint=r"A power is a repeated product. How is $\mathbf{A}^{k+1}$ built from $\mathbf{A}^k$?",
           feedback="A^(k+1) = A^k × A, then substitute the assumed formula."),
        NUM(r"It is given that $\mathbf{A}^n = \begin{pmatrix} 2n+1 & -2n \\ 2n & 1-2n \end{pmatrix}$ for $\mathbf{A} = \begin{pmatrix} 3 & -2 \\ 2 & -1 \end{pmatrix}$. Find the top-left entry of $\mathbf{A}^{10}$.", 21,
            steps=[S("Substitute $n = 10$", math=r"2(10) + 1 = 21")],
            concept="Using a proved matrix power", skill="Calculation", hint="Put n = 10 into the top-left entry of the formula.",
            feedback="You substituted n = 10 into the entry 2n + 1."),
        MC(r"The inequality $2^n > n^2$ is true for $n = 1$ and for all $n \geq 5$. For which values is it false?", [
            C(r"$n = 2, 3, 4$", correct=True),
            C(r"$n = 1, 2, 3$", why=r"$n = 1$ is true: $2 > 1$. The false cases are $2, 3, 4$ ($4 = 4$, $8 < 9$, $16 = 16$)."),
            C(r"$n = 3, 4$ only", why=r"$n = 2$ gives $4 > 4$, which is false (equality is not strict inequality)."),
            C(r"$n = 4, 5$", why=r"$n = 5$ gives $32 > 25$, which is true."),
        ], steps=[S("Check small values", math=r"2^2 = 4 = 2^2,\quad 2^3 = 8 < 9,\quad 2^4 = 16 = 4^2"), S("So", text="The strict inequality fails for $n = 2, 3, 4$.")],
           concept="Starting value of an inequality", skill="Calculation", hint="Evaluate both sides for n = 1, 2, 3, 4, 5.",
           feedback="Only n = 2, 3, 4 fail, which is why the induction proof begins at n = 5."),
        MC(r"What is $\dfrac{d^4}{dx^4}\left(xe^x\right)$?", [
            C(r"$(x+3)e^x$", why=r"That is the third derivative: the formula is $(x+n)e^x$ for the $n$th."),
            C(r"$(x+4)e^x$", correct=True),
            C(r"$4e^x$", why="The factor $x$ is not lost: it stays in every derivative."),
            C(r"$xe^x$", why=r"Each derivative adds $1$ to the bracket: $e^x + xe^x$ is the first derivative, not the original."),
        ], steps=[S("Pattern from the proof", math=r"\frac{d^n}{dx^n}\left(xe^x\right) = (x+n)e^x"), S("Put $n = 4$", math=r"(x+4)e^x")],
           concept="nth derivative of a product", skill="Application", hint="Differentiate once or twice and look for the pattern.",
           feedback="Each differentiation adds 1 to the bracket, so the nth derivative is (x + n)e^x."),
        MC(r"In proving $n! > 2^n$ for $n \geq 4$, the step is $(k+1)! = (k+1)\,k! > (k+1)\,2^k$. Which fact finishes the proof?", [
            C(r"$k + 1 \geq 2$, so $(k+1)2^k \geq 2\cdot 2^k = 2^{k+1}$", correct=True),
            C(r"$k + 1 = 2$ for all $k$", why=r"$k+1$ is at least $5$ here, not $2$. We only need it to be at least $2$."),
            C(r"$k! = 2^k$", why="The assumption is a strict inequality, not an equality."),
            C(r"$(k+1)2^k = 2^{k+1}$", why=r"$(k+1)2^k$ is larger than $2\cdot 2^k$ unless $k = 1$. It is not equal."),
        ], steps=[S("Compare the multiplier", text=r"Since $k \geq 4$, $k + 1 \geq 5 > 2$."), S("Chain", math=r"(k+1)! > (k+1)2^k \geq 2\cdot 2^k = 2^{k+1}")],
           concept="Inequality inductive step", skill="Reasoning", hint="Compare the multiplier k + 1 with the 2 you need.",
           feedback="The multiplier k + 1 is at least 2, which is enough to reach 2^(k+1)."),
        NUM(r"A sequence has $u_1 = 1$, $u_2 = 5$ and $u_{n+2} = 5u_{n+1} - 6u_n$, with $u_n = 3^n - 2^n$. Find $u_5$.", 211,
            steps=[S("Substitute $n = 5$", math=r"3^5 - 2^5 = 243 - 32 = 211"), S("Check by the rule", math=r"u_3 = 19,\ u_4 = 5(19) - 6(5) = 65,\ u_5 = 5(65) - 6(19) = 211")],
            concept="Using a proved recurrence formula", skill="Calculation", hint="Use the formula u_n = 3^n − 2^n with n = 5.",
            feedback="Both the formula and the recurrence give 211."),
        MC(r"A student proves $u_n = 3^n - 1$ for $u_{n+2} = 4u_{n+1} - 3u_n$ by checking $n = 1$ and assuming only $u_k = 3^k - 1$. What is wrong?", [
            C("Nothing: the proof is complete", why=r"The step needs $u_{k+1}$ as well as $u_k$, and the second starting value is unchecked."),
            C(r"The formula should have $n!$ in it", why="Nothing in the question suggests this; the issue is the structure of the proof."),
            C(r"Induction cannot prove statements about sequences", why="It can, and does so well, if the structure is right."),
            C(r"It needs a second base case, $n = 2$, and an assumption for both $n = k$ and $n = k+1$", correct=True),
        ], steps=[S("The step", math=r"u_{k+2} = 4u_{k+1} - 3u_k"), S("So", text=r"Both $u_k$ and $u_{k+1}$ must be assumed, and both $u_1$ and $u_2$ checked.")],
           concept="Spotting a flaw in a proof", skill="Reasoning", hint="What does the rule for u(k+2) need as input?",
           feedback="A two-term rule needs two base cases and a two-value assumption."),
    ]))

# ------------------------------------------------------------------ Method of differences
SETS.append(practice_set(
    module=M1, topic="The method of differences and series",
    title="Telescoping sums and sums to infinity", lesson="fml1-method-of-differences",
    questions=[
        MC(r"If $u_r = f(r) - f(r+1)$, then $\displaystyle\sum_{r=1}^{n} u_r$ equals", [
            C(r"$f(n) - f(1)$", why="The sign and the end terms are wrong: the first term kept is $f(1)$ and the last is $f(n+1)$."),
            C(r"$f(1) - f(n+1)$", correct=True),
            C(r"$f(1) + f(n+1)$", why="The last surviving term has a minus sign, because it comes from the subtracted part."),
            C(r"$f(n+1) - f(2)$", why=r"$f(2)$ cancels with the $+f(2)$ in the second term. Only $f(1)$ survives at the start."),
        ], steps=[S("Write out", math=r"[f(1) - f(2)] + [f(2) - f(3)] + \cdots + [f(n) - f(n+1)]"), S("Cancel", math=r"f(1) - f(n+1)")],
           concept="The method of differences", skill="Recall", hint="Write out the first two terms and the last term.",
           feedback="All the middle terms cancel, leaving f(1) − f(n + 1)."),
        MC(r"Which is the partial fraction form of $\dfrac{1}{r(r+2)}$?", [
            C(r"$\dfrac1r - \dfrac1{r+2}$", why=r"Combining these gives $\frac{2}{r(r+2)}$, twice the required fraction."),
            C(r"$\dfrac1r + \dfrac1{r+2}$", why="A sum would give a numerator of $2r + 2$."),
            C(r"$\dfrac12\left(\dfrac1r - \dfrac1{r+2}\right)$", correct=True),
            C(r"$\dfrac1{2r} - \dfrac1{r+2}$", why=r"The factor $\frac12$ multiplies **both** terms."),
        ], steps=[S("Set up", math=r"\frac{1}{r(r+2)} = \frac Ar + \frac B{r+2}"), S("Solve", math=r"A = \tfrac12,\ B = -\tfrac12")],
           concept="Partial fractions for telescoping", skill="Calculation", hint="Check your answer by combining the two fractions.",
           feedback="Splitting gives 1/2 (1/r − 1/(r+2))."),
        NUM(r"Find $\displaystyle\sum_{r=1}^{10}\frac{1}{r(r+1)}$ as a decimal, to 3 decimal places.", 0.909, tolerance=0.002,
            steps=[S("Split", math=r"\frac1{r(r+1)} = \frac1r - \frac1{r+1}"), S("Telescope", math=r"1 - \tfrac{1}{11} = \tfrac{10}{11} \approx 0.909")],
            concept="Telescoping sum of unit gap", skill="Calculation", hint="Write 1/(r(r+1)) as a difference of two fractions.",
            feedback="The sum is 1 − 1/11 = 10/11."),
        MC(r"In $\displaystyle\sum_{r=1}^{n}\frac12\left(\frac1r - \frac1{r+2}\right)$, which terms survive after cancelling?", [
            C(r"$\frac12\left(1 + \frac12 - \frac1{n+1} - \frac1{n+2}\right)$", correct=True),
            C(r"$\frac12\left(1 - \frac1{n+2}\right)$", why="The gap is 2, so two terms survive at each end, not one."),
            C(r"$\frac12\left(\frac1n - \frac1{n+2}\right)$", why=r"The start terms $1$ and $\frac12$ never cancel, because nothing before them is negative."),
            C(r"$\frac12\left(1 - \frac1{n+1}\right)$", why="This is the sum for a gap of 1, not 2."),
        ], steps=[S("Front of the list", text=r"$\frac11$ and $\frac12$ have no partners."), S("End of the list", text=r"$-\frac1{n+1}$ and $-\frac1{n+2}$ have no partners.")],
           concept="Surviving terms", skill="Reasoning", hint="Write the first three and the last three terms and cross out partners.",
           feedback="With a gap of 2, two terms survive at each end."),
        MC(r"Which is $\displaystyle\sum_{r=1}^{n} r\cdot r!$?", [
            C(r"$n!$", why="The sum is bigger: for $n=2$ it is $1 + 4 = 5$, not $2$."),
            C(r"$(n+1)!$", why="This is one too many: for $n = 2$ it gives $6$, but the sum is $5$."),
            C(r"$n\cdot n!$", why="This is just the last term."),
            C(r"$(n+1)! - 1$", correct=True),
        ], steps=[S("Write the term as a difference", math=r"r\cdot r! = (r+1)! - r!"), S("Telescope", math=r"(n+1)! - 1!")],
           concept="Factorial telescoping", skill="Calculation", hint="Write r·r! as (r + 1)! minus something.",
           feedback="r·r! = (r + 1)! − r!, so the sum is (n + 1)! − 1."),
        NUM(r"Find the sum to infinity of $\displaystyle\sum_{r=1}^{\infty}\frac{1}{r(r+2)}$ as a decimal.", 0.75, tolerance=0.001,
            steps=[S("Sum of $n$ terms", math=r"\tfrac34 - \frac{2n+3}{2(n+1)(n+2)}"), S(r"Let $n \to \infty$", math=r"\frac{2n+3}{2(n+1)(n+2)} \to 0 \Rightarrow \tfrac34")],
            concept="Sum to infinity", skill="Calculation", hint="Find the sum of n terms, then see what the end terms do as n grows.",
            feedback="The end terms tend to 0, leaving 3/4."),
        MC(r"Find $\displaystyle\sum_{r=1}^{\infty}\frac{1}{(r+1)(r+3)}$.", [
            C(r"$\dfrac12$", why=r"This keeps only the term $\frac12$ and ignores the second surviving term $\frac13$ and the factor $\frac12$ in front."),
            C(r"$\dfrac{5}{12}$", correct=True),
            C(r"$\dfrac{5}{6}$", why=r"You forgot the factor $\frac12$ in front of the partial fractions."),
            C(r"$\dfrac{1}{3}$", why=r"The two surviving start terms already give $\frac12\left(\frac12 + \frac13\right) = \frac5{12}$, which is more than $\frac13$."),
        ], steps=[S("Split", math=r"\frac1{(r+1)(r+3)} = \tfrac12\left(\tfrac1{r+1} - \tfrac1{r+3}\right)"), S("Survivors at the start", math=r"\tfrac12\left(\tfrac12 + \tfrac13\right) = \tfrac5{12}"), S("End terms tend to 0", text=r"So the sum to infinity is $\frac5{12}$.")],
           concept="Sum to infinity with gap 2", skill="Calculation", hint="After splitting, which two fractions at the start are never cancelled?",
           feedback="Survivors 1/2 and 1/3, times 1/2, give 5/12."),
        MC(r"Find $\displaystyle\sum_{r=2}^{n}\frac{1}{r^2-1}$.", [
            C(r"$\dfrac34 - \dfrac1{n+1}$", why="Two terms survive at each end because the gap is 2."),
            C(r"$\dfrac12 - \dfrac{1}{2(n+1)}$", why=r"The sum starts at $r = 2$, so the survivors at the start are $1$ and $\frac12$, not just $\frac12$."),
            C(r"$\dfrac34 - \dfrac{2n+1}{2n(n+1)}$", correct=True),
            C(r"$\dfrac14 - \dfrac{2n+1}{2n(n+1)}$", why=r"The first terms are $1$ and $\frac12$ so the constant is $\frac12\cdot\frac32 = \frac34$."),
        ], steps=[S("Split", math=r"\frac1{r^2-1} = \tfrac12\left(\tfrac1{r-1} - \tfrac1{r+1}\right)"), S("Survivors", math=r"\tfrac12\left(1 + \tfrac12 - \tfrac1n - \tfrac1{n+1}\right) = \tfrac34 - \tfrac{2n+1}{2n(n+1)}"), S("Check $n = 3$", math=r"\tfrac13 + \tfrac18 = \tfrac{11}{24} = \tfrac34 - \tfrac7{24}")],
           concept="Method of differences from r = 2", skill="Reasoning", hint="Factorise r squared minus 1, split, and write out the first terms from r = 2.",
           feedback="Starting at r = 2 changes which terms survive at the start."),
    ]))

# ------------------------------------------------------------------ Standard sums
SETS.append(practice_set(
    module=M1, topic="The method of differences and series",
    title="Sums of r, r squared and r cubed, and polynomial series", lesson="fml1-standard-sums",
    questions=[
        MC(r"Which is the formula for $\displaystyle\sum_{r=1}^{n} r^2$?", [
            C(r"$\dfrac{n(n+1)}{2}$", why=r"This is $\sum r$, the sum of the integers."),
            C(r"$\dfrac{n^2(n+1)^2}{4}$", why=r"This is $\sum r^3$."),
            C(r"$\dfrac{n(n+1)(2n+1)}{6}$", correct=True),
            C(r"$\dfrac{n(n+1)(2n+1)}{3}$", why="The denominator is 6, not 3."),
        ], steps=[S("Recall", math=r"\sum_{r=1}^{n} r^2 = \frac{n(n+1)(2n+1)}{6}"), S("Check", text=r"$n = 2$ gives $5 = \frac{2\cdot 3\cdot 5}{6}$.")],
           concept="Standard sums", skill="Recall", hint="Test each formula with n = 2: the sum is 1 + 4.",
           feedback="The sum of squares is n(n + 1)(2n + 1)/6."),
        NUM(r"Find $\displaystyle\sum_{r=1}^{12} r^2$.", 650,
            steps=[S("Substitute $n = 12$", math=r"\frac{12\times 13\times 25}{6} = 650")],
            concept="Evaluating the sum of squares", skill="Calculation", hint="Use n(n + 1)(2n + 1)/6 with n = 12.",
            feedback="12 × 13 × 25 ÷ 6 = 650."),
        MC(r"What is $\displaystyle\sum_{r=1}^{n} 4$?", [
            C(r"$4$", why="There are $n$ terms, each equal to 4."),
            C(r"$4n$", correct=True),
            C(r"$4n^2$", why="A constant is added $n$ times, giving $4n$, not $4n^2$."),
            C(r"$\dfrac{4n(n+1)}{2}$", why=r"That is $4\sum r$. The term $4$ does not contain $r$."),
        ], steps=[S("Add 4 a total of $n$ times", math=r"4 + 4 + \cdots + 4 = 4n")],
           concept="Sum of a constant", skill="Concept", hint="How many terms are there?",
           feedback="A constant summed n times is n times the constant."),
        NUM(r"Find $\displaystyle\sum_{r=1}^{10} r^3$.", 3025,
            steps=[S("Use the formula", math=r"\frac{10^2\times 11^2}{4} = 3025"), S("Or", text="The sum of the first 10 integers is 55 and $55^2 = 3025$.")],
            concept="Sum of cubes", skill="Calculation", hint="The sum of cubes equals the square of the sum of the integers.",
            feedback="55 squared is 3025."),
        MC(r"Which is $\displaystyle\sum_{r=1}^{n} r(r+2)$?", [
            C(r"$\dfrac{n(n+1)(2n+1)}{6}$", why=r"This is $\sum r^2$ only. The term $2r$ adds $n(n+1)$ more."),
            C(r"$\dfrac{n(n+1)(2n+7)}{3}$", why="The denominator is 6. Check with $n=1$: the sum is 3."),
            C(r"$\dfrac{n(n+1)(n+2)}{3}$", why=r"Check $n = 1$: this gives $2$, but the sum is $3$."),
            C(r"$\dfrac{n(n+1)(2n+7)}{6}$", correct=True),
        ], steps=[S("Expand", math=r"\sum r^2 + 2\sum r = \frac{n(n+1)(2n+1)}{6} + n(n+1)"), S("Combine", math=r"\frac{n(n+1)(2n+7)}{6}"), S("Check $n = 3$", math=r"3 + 8 + 15 = 26 = \frac{3\cdot 4\cdot 13}{6}")],
           concept="Polynomial series", skill="Calculation", hint="Expand r(r + 2) into powers of r first.",
           feedback="Split into Σr² and 2Σr, then take out n(n + 1)/6."),
        NUM(r"Find $\displaystyle\sum_{r=11}^{20} r^2$.", 2485,
            steps=[S("Difference of two sums", math=r"\sum_{r=1}^{20} r^2 - \sum_{r=1}^{10} r^2"), S("Evaluate", math=r"2870 - 385 = 2485")],
            concept="Sum over a range", skill="Calculation", hint="Subtract the sum to 10 from the sum to 20.",
            feedback="2870 − 385 = 2485."),
        MC(r"Which is $\displaystyle\sum_{r=n+1}^{2n} r^2$?", [
            C(r"$\dfrac{n(2n+1)(7n+1)}{6}$", correct=True),
            C(r"$\dfrac{2n(2n+1)(4n+1)}{6}$", why="This is the sum from $1$ to $2n$. The first $n$ squares must be subtracted."),
            C(r"$\dfrac{n(n+1)(2n+1)}{6}$", why=r"This is the sum to $n$, the part that must be removed."),
            C(r"$\dfrac{n(2n+1)(4n+1)}{6}$", why=r"Check $n = 1$: this gives $\frac{1\cdot 3\cdot 5}{6}$, not the required $4$."),
        ], steps=[S("Subtract", math=r"\frac{2n(2n+1)(4n+1)}{6} - \frac{n(n+1)(2n+1)}{6}"), S("Factorise", math=r"\frac{n(2n+1)(7n+1)}{6}"), S("Check $n = 1$", math=r"\frac{1\cdot 3\cdot 8}{6} = 4 = 2^2")],
           concept="Sum from n+1 to 2n", skill="Reasoning", hint="Write it as a sum to 2n minus a sum to n.",
           feedback="Subtract the sum to n from the sum to 2n and factorise."),
        MC(r"The sum of the first $20$ terms of $1\times 3 + 2\times 5 + 3\times 7 + \cdots$ is", [
            C(r"$5740$", why=r"You took $2\sum r^2$ and forgot to add $\sum r = 210$."),
            C(r"$3080$", why=r"You added $\sum r^2 + \sum r$ and forgot the factor 2 on $\sum r^2$."),
            C(r"$5950$", correct=True),
            C(r"$2870$", why=r"This is $\sum r^2$ alone."),
        ], steps=[S("General term", math=r"u_r = r(2r+1)"), S("Sum", math=r"2(2870) + 210 = 5950")],
           concept="Series from a pattern", skill="Application", hint="Find the r-th term first, then split it into sums of r squared and r.",
           feedback="u_r = r(2r + 1), and 2 × 2870 + 210 = 5950."),
    ]))

# ------------------------------------------------------------------ Quartics
SETS.append(practice_set(
    module=M1, topic="Roots and coefficients of polynomial equations",
    title="Roots and coefficients of a quartic", lesson="fml1-quartic-roots-coefficients",
    questions=[
        MC(r"For a quartic $ax^4 + bx^3 + cx^2 + dx + e = 0$ with roots $\alpha, \beta, \gamma, \delta$, the sum $\sum\alpha\beta\gamma$ of the triple products is", [
            C(r"$\dfrac{d}{a}$", why="The sign is wrong: triple products take the sign $-$."),
            C(r"$\dfrac{c}{a}$", why=r"$\frac ca$ is the sum of the **pair** products."),
            C(r"$-\dfrac{b}{a}$", why=r"That is the sum of the roots."),
            C(r"$-\dfrac{d}{a}$", correct=True),
        ], steps=[S("Alternating signs", math=r"-\frac ba,\ +\frac ca,\ -\frac da,\ +\frac ea"), S("Triples", text=r"Triple products go with $-\frac da$.")],
           concept="Relations for a quartic", skill="Recall", hint="The signs alternate starting with a minus for the sum of the roots.",
           feedback="The four relations have signs −, +, −, +."),
        NUM(r"The roots of $x^4 - 5x^3 + 2x^2 + 7x - 3 = 0$ are $\alpha, \beta, \gamma, \delta$. Find $\alpha^2 + \beta^2 + \gamma^2 + \delta^2$.", 21,
            steps=[S("Relations", math=r"e_1 = 5,\ e_2 = 2"), S("Sum of squares", math=r"e_1^2 - 2e_2 = 25 - 4 = 21")],
            concept="Sum of squares of roots", skill="Calculation", hint="Use e1 squared minus twice e2.",
            feedback="25 − 4 = 21."),
        MC(r"The roots of $2x^4 - 3x^3 + 5x^2 - x + 6 = 0$ are $\alpha, \beta, \gamma, \delta$. Find $\dfrac1\alpha + \dfrac1\beta + \dfrac1\gamma + \dfrac1\delta$.", [
            C(r"$\dfrac12$", why=r"This is $e_3$ alone. Divide by $e_4 = 3$."),
            C(r"$\dfrac16$", correct=True),
            C(r"$-\dfrac16$", why=r"Check the sign: $e_3 = -\frac da = \frac12$ is positive."),
            C(r"$\dfrac{5}{6}$", why=r"You used $e_2 = \frac52$ in the numerator. The numerator is the sum of **triple** products, $e_3$."),
        ], steps=[S("Values", math=r"e_3 = -\frac{-1}{2} = \tfrac12,\quad e_4 = \tfrac62 = 3"), S("Reciprocal sum", math=r"\frac{e_3}{e_4} = \tfrac16")],
           concept="Sum of reciprocals of roots", skill="Calculation", hint="Put the reciprocals over the common denominator αβγδ.",
           feedback="The sum of reciprocals is e3/e4."),
        MC(r"The roots of $x^4 - 5x^3 + 2x^2 + 7x - 3 = 0$ are $\alpha, \beta, \gamma, \delta$. Which equation has roots $\dfrac1\alpha, \dfrac1\beta, \dfrac1\gamma, \dfrac1\delta$?", [
            C(r"$3y^4 - 7y^3 - 2y^2 + 5y - 1 = 0$", correct=True),
            C(r"$y^4 - 5y^3 + 2y^2 + 7y - 3 = 0$", why="This is the original equation, which has the original roots."),
            C(r"$3y^4 - 7y^3 + 2y^2 + 5y - 1 = 0$", why=r"Reversing and multiplying by $-1$ changes **every** sign: the $y^2$ term becomes $-2y^2$."),
            C(r"$y^4 + 7y^3 + 2y^2 - 5y - 3 = 0$", why="Reversing the coefficients moves $-3$ to the front; it does not leave the leading coefficient at 1."),
        ], steps=[S(r"Substitute $x = \frac1y$ and multiply by $y^4$", math=r"1 - 5y + 2y^2 + 7y^3 - 3y^4 = 0"), S("Multiply by $-1$", math=r"3y^4 - 7y^3 - 2y^2 + 5y - 1 = 0")],
           concept="Reciprocal roots", skill="Application", hint="Substitute x = 1/y and clear the fractions.",
           feedback="For reciprocal roots the coefficients are reversed."),
        MC(r"A quartic has roots in arithmetic progression. If they are written $a-3d, a-d, a+d, a+3d$ and the quartic is $x^4 - 16x^3 + \cdots$, what is $a$?", [
            C(r"$16$", why="The sum of the roots is 16, but the sum is $4a$."),
            C(r"$8$", why=r"$4a = 16$ gives $a = 4$, not $8$."),
            C(r"$4$", correct=True),
            C(r"$2$", why="You divided 16 by 8 instead of by 4 (four roots)."),
        ], steps=[S("Sum of roots", math=r"(a-3d) + (a-d) + (a+d) + (a+3d) = 4a = 16"), S("So", math=r"a = 4")],
           concept="Roots in arithmetic progression", skill="Application", hint="Add the four roots; the d terms cancel.",
           feedback="The sum is 4a = 16, so a = 4."),
        NUM(r"Find the product of the roots of $3x^4 + 6x^3 - x^2 + 2x - 9 = 0$.", -3,
            steps=[S("Product of roots of a quartic", math=r"\alpha\beta\gamma\delta = \frac ea = \frac{-9}{3} = -3")],
            concept="Product of roots", skill="Calculation", hint="For a quartic the product has a plus sign.",
            feedback="e/a = −9/3 = −3."),
        MC(r"The roots of $x^4 + 2x^3 + 3x^2 + 4x + 5 = 0$ satisfy $\sum\alpha^2 = -2$. What does this show?", [
            C("There is a mistake: a sum of squares is never negative", why="Squares of complex numbers can be negative, so the sum can be negative."),
            C("All four roots are positive", why=r"Roots do not have to be positive, and a negative $\sum\alpha^2$ says nothing like that."),
            C(r"The equation has no roots", why="A quartic always has four roots (real or complex)."),
            C(r"The roots are not all real", correct=True),
        ], steps=[S("Real roots", text=r"If all roots were real, each $\alpha^2 \geq 0$, so $\sum\alpha^2 \geq 0$."), S("Conclusion", text="A negative sum is impossible, so some roots are complex.")],
           concept="Interpreting a negative sum of squares", skill="Interpretation", hint="What is the sign of the square of a real number?",
           feedback="A negative sum of squares proves some roots are non-real."),
        MC(r"The roots of $2x^4 - 3x^3 + 5x^2 - x + 6 = 0$ are $\alpha, \beta, \gamma, \delta$. Which equation has roots $2\alpha, 2\beta, 2\gamma, 2\delta$?", [
            C(r"$y^4 - 3y^3 + 10y^2 - 4y + 48 = 0$", correct=True),
            C(r"$32y^4 - 24y^3 + 20y^2 - 2y + 6 = 0$", why=r"This substitutes $x = 2y$, which gives roots **half** the originals."),
            C(r"$2y^4 - 6y^3 + 20y^2 - 8y + 96 = 0$", why="Doubling every coefficient does not double the roots."),
            C(r"$y^4 - 3y^3 + 5y^2 - y + 6 = 0$", why="This keeps the original coefficients except the leading one; the roots are not doubled."),
        ], steps=[S(r"Let $y = 2x$, $x = \frac y2$", math=r"2\cdot\frac{y^4}{16} - 3\cdot\frac{y^3}{8} + 5\cdot\frac{y^2}{4} - \frac y2 + 6 = 0"), S("Multiply by 8", math=r"y^4 - 3y^3 + 10y^2 - 4y + 48 = 0")],
           concept="Scaling the roots", skill="Application", hint="If y = 2x, what is x in terms of y?",
           feedback="Substitute x = y/2 and clear fractions."),
    ]))

# ------------------------------------------------------------------ Power sums, conjugates, repeated roots
SETS.append(practice_set(
    module=M1, topic="Roots and coefficients of polynomial equations",
    title="Power sums, conjugate roots and repeated roots", lesson="fml1-power-sums-conjugate-roots",
    questions=[
        MC(r"A cubic with real coefficients has roots $3$ and $2 - 5i$. The third root is", [
            C(r"$-2 + 5i$", why="That is the negative of the conjugate."),
            C(r"$-2 - 5i$", why="That negates both parts. The conjugate changes only the sign of the imaginary part."),
            C(r"$3$", why="A third root equal to 3 would leave $2-5i$ without its conjugate partner, so the coefficients could not be real."),
            C(r"$2 + 5i$", correct=True),
        ], steps=[S("Conjugate root theorem", text=r"Non-real roots of a real polynomial come in conjugate pairs."), S("Conjugate", math=r"\overline{2 - 5i} = 2 + 5i")],
           concept="Conjugate root theorem", skill="Concept", hint="What must accompany a non-real root of a polynomial with real coefficients?",
           feedback="The conjugate 2 + 5i must be a root."),
        NUM(r"The roots of $x^3 - 6x^2 + 11x - 6 = 0$ are $\alpha, \beta, \gamma$. Find $\alpha^3 + \beta^3 + \gamma^3$.", 36,
            steps=[S("Elementary sums", math=r"e_1 = 6,\ e_2 = 11,\ e_3 = 6"), S("$p_2$", math=r"36 - 22 = 14"), S("$p_3$", math=r"e_1p_2 - e_2p_1 + 3e_3 = 84 - 66 + 18 = 36")],
            concept="Newton's identities", skill="Calculation", hint="Find p1 and p2 first, then use p3 = e1 p2 − e2 p1 + 3 e3.",
            feedback="The roots are 1, 2, 3 and 1 + 8 + 27 = 36."),
        MC(r"A quadratic has real coefficients and a root $3 + 2i$. Its equation, with leading coefficient 1, is", [
            C(r"$x^2 - 6x + 13 = 0$", correct=True),
            C(r"$x^2 - 6x + 5 = 0$", why=r"The product of the roots is $3^2 + 2^2 = 13$, not $9 - 4$."),
            C(r"$x^2 + 6x + 13 = 0$", why="The sum of the roots is $+6$, so the coefficient of $x$ is $-6$."),
            C(r"$x^2 - 3x + 2 = 0$", why="You used the real and imaginary parts as the sum and product."),
        ], steps=[S("Sum and product", math=r"(3 + 2i) + (3 - 2i) = 6,\quad (3+2i)(3-2i) = 9 + 4 = 13"), S("Equation", math=r"x^2 - 6x + 13 = 0")],
           concept="Real quadratic from a complex root", skill="Calculation", hint="Use the root and its conjugate to find the sum and product.",
           feedback="Sum 6 and product 13 give x² − 6x + 13."),
        NUM(r"The roots of $x^3 - 6x^2 + 11x - 6 = 0$ are $\alpha, \beta, \gamma$. Find $\alpha^4 + \beta^4 + \gamma^4$.", 98,
            steps=[S("Recurrence from the equation", math=r"p_4 = 6p_3 - 11p_2 + 6p_1"), S("Substitute $p_1 = 6$, $p_2 = 14$, $p_3 = 36$", math=r"216 - 154 + 36 = 98")],
            concept="Higher power sums", skill="Calculation", hint="Multiply the equation by x, then add over the three roots.",
            feedback="1 + 16 + 81 = 98 as a check."),
        MC(r"$1 + 2i$ is a root of $x^3 - 3x^2 + 7x - 5 = 0$. The other roots are", [
            C(r"$1 + 2i$ and $5$", why="The conjugate $1 - 2i$ must be a root, and the roots must give product 5."),
            C(r"$-1 + 2i$ and $1$", why="The conjugate is $1 - 2i$, not $-1 + 2i$."),
            C(r"$1 - 2i$ and $1$", correct=True),
            C(r"$1 - 2i$ and $-1$", why=r"The product of the roots is $5$: $(1+2i)(1-2i)\gamma = 5\gamma = 5$, so $\gamma = 1$, not $-1$."),
        ], steps=[S("Conjugate", text=r"$1 - 2i$ is a root."), S("Product of roots", math=r"5\gamma = 5 \Rightarrow \gamma = 1")],
           concept="Finding roots from a complex root", skill="Application", hint="Write down the conjugate, then use the product of the three roots.",
           feedback="Conjugate 1 − 2i, product of roots 5, so the real root is 1."),
        MC(r"The equation $x^3 - 3x - k = 0$ has a repeated root. The possible values of $k$ are", [
            C(r"$k = 2$ only", why=r"$x = 1$ is also a root of $f'(x) = 3x^2 - 3$; it gives $k = -2$."),
            C(r"$k = \pm 2$", correct=True),
            C(r"$k = \pm 1$", why=r"The repeated roots are $x = \pm 1$, but $k$ is found from $f(\pm 1) = 0$: $k = \mp 2$."),
            C(r"$k = 0$", why=r"$x^3 - 3x = 0$ has three different roots $0, \pm\sqrt3$."),
        ], steps=[S("Roots of the derivative", math=r"f'(x) = 3x^2 - 3 = 0 \Rightarrow x = \pm 1"), S("Test in $f$", math=r"f(1) = -2 - k = 0 \Rightarrow k = -2,\quad f(-1) = 2 - k = 0 \Rightarrow k = 2")],
           concept="Repeated roots", skill="Calculation", hint="A repeated root is also a root of the derivative.",
           feedback="Root of f' and root of f together give k = ±2."),
        NUM(r"The roots of $x^3 - 3x^2 + 7x - 5 = 0$ are $\alpha, \beta, \gamma$. Find $\alpha^4 + \beta^4 + \gamma^4$.", -13,
            steps=[S("Recurrence", math=r"p_4 = 3p_3 - 7p_2 + 5p_1"), S("Values", math=r"p_1 = 3,\ p_2 = -5,\ p_3 = -21"), S("Calculate", math=r"-63 + 35 + 15 = -13")],
            concept="Power sums with complex roots", skill="Calculation", hint="Find p1, p2, p3 first; then use the equation x^3 = 3x^2 − 7x + 5 times x.",
            feedback="Power sums can be negative because some roots are complex."),
        MC(r"A real quartic has roots $3i$ and $1 + i$. With leading coefficient 1 it is", [
            C(r"$x^4 - 2x^3 + 11x^2 - 18x + 18$", correct=True),
            C(r"$x^4 + 2x^3 + 11x^2 + 18x + 18$", why="The signs of the odd powers are reversed; the sum of the roots is $+2$."),
            C(r"$x^4 - 2x^3 + 7x^2 - 18x + 18$", why=r"The $x^2$ coefficient is $2 + 9 = 11$ (pair products), not $2 + 5$."),
            C(r"$x^4 - 2x^3 + 11x^2 - 18x - 18$", why=r"The product of the roots is $9\times 2 = +18$."),
        ], steps=[S("Quadratic factors", math=r"(x^2 + 9)(x^2 - 2x + 2)"), S("Multiply", math=r"x^4 - 2x^3 + 11x^2 - 18x + 18")],
           concept="Real polynomial from complex roots", skill="Application", hint="The roots 3i and −3i give one real quadratic; 1 ± i give another.",
           feedback="Multiply the two real quadratic factors."),
    ]))

# ================================================================== MODULE 2: COMPLEX NUMBERS
# ------------------------------------------------------------------ Algebra of complex numbers
SETS.append(practice_set(
    module=M2, topic="Algebra of complex numbers",
    title="Arithmetic, conjugates, square roots and equations", lesson="fml1-complex-algebra",
    questions=[
        MC(r"What is the conjugate of $3 - 5i$?", [
            C(r"$-3 + 5i$", why="This negates both parts. The conjugate changes only the sign of the imaginary part."),
            C(r"$-3 - 5i$", why="This changes the sign of the real part only."),
            C(r"$3 + 5i$", correct=True),
            C(r"$5 - 3i$", why="This swaps the real and imaginary parts, which is not the conjugate."),
        ], steps=[S("Definition", math=r"\overline{a + bi} = a - bi"), S("Apply", math=r"\overline{3 - 5i} = 3 + 5i")],
           concept="Conjugate", skill="Recall", hint="Which part of the number changes sign?",
           feedback="The conjugate of a + bi is a − bi."),
        NUM(r"Find the real part of $(2 + 3i)(4 - i)$.", 11,
            steps=[S("Expand", math=r"8 - 2i + 12i - 3i^2"), S("Use $i^2 = -1$", math=r"= 8 + 3 + 10i = 11 + 10i")],
            concept="Multiplying complex numbers", skill="Calculation", hint="Expand all four products, then replace i squared by −1.",
            feedback="(2 + 3i)(4 − i) = 11 + 10i."),
        MC(r"Write $\dfrac{1 + i}{2 - i}$ in the form $a + bi$.", [
            C(r"$\dfrac15 + \dfrac35 i$", correct=True),
            C(r"$\dfrac{1}{3} + \dfrac{1}{3}i$", why="The denominator after multiplying by the conjugate is $4 + 1 = 5$, not $4 - 1 = 3$."),
            C(r"$\dfrac15 - \dfrac15 i$", why=r"The numerator is $(1+i)(2+i) = 2 + i + 2i - 1 = 1 + 3i$. The imaginary part is $+3$."),
            C(r"$\dfrac35 + \dfrac15 i$", why="The real and imaginary parts have been swapped."),
        ], steps=[S("Multiply by the conjugate", math=r"\frac{(1+i)(2+i)}{(2-i)(2+i)}"), S("Calculate", math=r"\frac{2 + i + 2i - 1}{5} = \frac{1 + 3i}{5}")],
           concept="Dividing complex numbers", skill="Calculation", hint="Multiply the top and bottom by 2 + i.",
           feedback="The denominator becomes 5 and the numerator 1 + 3i."),
        MC(r"Find the modulus of $5 - 12i$.", [
            C(r"$7$", why="You added the parts $5 + 12$. The modulus uses a square root of the sum of squares."),
            C(r"$-7$", why="A modulus is never negative."),
            C(r"$169$", why="This is $|z|^2$. The modulus needs the square root."),
            C(r"$13$", correct=True),
        ], steps=[S("Formula", math=r"|z| = \sqrt{a^2 + b^2}"), S("Calculate", math=r"\sqrt{25 + 144} = \sqrt{169} = 13")],
           concept="Modulus", skill="Calculation", hint="Square both parts, add, then take the square root.",
           feedback="|5 − 12i| = 13."),
        MC(r"Find the square roots of $21 - 20i$.", [
            C(r"$\pm(5 + 2i)$", why=r"$(5 + 2i)^2 = 21 + 20i$. The sign of $2ab$ must be negative, so $a$ and $b$ have opposite signs."),
            C(r"$\pm(5 - 2i)$", correct=True),
            C(r"$5 - 2i$ only", why="Every non-zero complex number has two square roots, one the negative of the other."),
            C(r"$\pm(21 - 20i)^{1/2}$ cannot be simplified", why="The roots can be found by equating real and imaginary parts."),
        ], steps=[S("Equate", math=r"a^2 - b^2 = 21,\quad 2ab = -20"), S("Solve", math=r"a = \pm 5,\ b = \mp 2"), S("Check", math=r"(5 - 2i)^2 = 25 - 4 - 20i = 21 - 20i")],
           concept="Square roots of a complex number", skill="Calculation", hint="Let the root be a + bi and equate real and imaginary parts of its square.",
           feedback="The roots are ±(5 − 2i)."),
        NUM(r"Solve $z + 2\bar z = 3 - 4i$. Find $|z|$ to 2 decimal places.", 4.12, tolerance=0.01,
            steps=[S("Put $z = a + bi$", math=r"3a - bi = 3 - 4i \Rightarrow a = 1,\ b = 4"), S("Modulus", math=r"|1 + 4i| = \sqrt{17} \approx 4.12")],
            concept="Equations with z and its conjugate", skill="Calculation", hint="Write z as a + bi and compare real and imaginary parts.",
            feedback="z = 1 + 4i and |z| = √17."),
        MC(r"Solve $z^2 - 6z + 13 = 0$.", [
            C(r"$z = 3 \pm 4i$", why=r"$\sqrt{-16} = 4i$, but this is halved by the denominator $2$: $\frac{6 \pm 4i}{2} = 3 \pm 2i$."),
            C(r"$z = -3 \pm 2i$", why="The formula starts with $-b = +6$, so the real part is $+3$."),
            C(r"$z = 3 \pm 2i$", correct=True),
            C(r"$z = 3 \pm 2$", why="The square root of a negative discriminant is imaginary, not real."),
        ], steps=[S("Formula", math=r"z = \frac{6 \pm \sqrt{36 - 52}}{2}"), S("Simplify", math=r"= \frac{6 \pm 4i}{2} = 3 \pm 2i")],
           concept="Quadratics with complex roots", skill="Calculation", hint="The discriminant is negative: write its square root with i.",
           feedback="The roots are the conjugate pair 3 ± 2i."),
        MC(r"$z = 1$ is a root of $z^3 - 5z^2 + 17z - 13 = 0$. What are the other roots?", [
            C(r"$2 \pm 3i$", correct=True),
            C(r"$-2 \pm 3i$", why=r"The quadratic factor is $z^2 - 4z + 13$, whose roots have real part $+2$."),
            C(r"$4 \pm 3i$", why=r"The real part is half the sum, $\frac42 = 2$, not $4$."),
            C(r"$2 \pm 9i$", why="$\\sqrt{16 - 52} = \\sqrt{-36} = 6i$, which halves to $3i$, not $9i$."),
        ], steps=[S("Factorise", math=r"(z - 1)(z^2 - 4z + 13)"), S("Solve the quadratic", math=r"z = \frac{4 \pm \sqrt{-36}}{2} = 2 \pm 3i")],
           concept="Cubic with a complex pair", skill="Application", hint="Divide the cubic by (z − 1) first.",
           feedback="The quotient z² − 4z + 13 has roots 2 ± 3i."),
    ]))

# ------------------------------------------------------------------ Modulus-argument and exponential forms
SETS.append(practice_set(
    module=M2, topic="Modulus-argument and exponential forms",
    title="Modulus, argument and the exponential form", lesson="fml1-modulus-argument-exponential",
    questions=[
        MC(r"What is the principal argument of $-\sqrt3 + i$?", [
            C(r"$\dfrac{\pi}{6}$", why="This is the angle for $\\sqrt3 + i$. The point $-\\sqrt3 + i$ is in the second quadrant."),
            C(r"$\dfrac{5\pi}{6}$", correct=True),
            C(r"$-\dfrac{5\pi}{6}$", why="That is the angle of $-\\sqrt3 - i$ (third quadrant)."),
            C(r"$\dfrac{2\pi}{3}$", why=r"$\tan\frac{2\pi}3 = -\sqrt3$, which would correspond to $-1 + \sqrt3 i$."),
        ], steps=[S("Sketch", text="The point is in the second quadrant."), S("Reference angle", math=r"\tan^{-1}\frac{1}{\sqrt3} = \frac\pi6"), S("Argument", math=r"\pi - \frac\pi6 = \frac{5\pi}{6}")],
           concept="Principal argument", skill="Calculation", hint="Sketch the point and find the angle from the positive real axis.",
           feedback="The point is in the second quadrant: π − π/6 = 5π/6."),
        MC(r"What is $|(1 + i)(\sqrt3 + i)|$?", [
            C(r"$\sqrt2 + 2$", why="Moduli are multiplied, not added."),
            C(r"$2\sqrt2$", correct=True),
            C(r"$4$", why=r"$|1 + i| = \sqrt2$, not $2$. The product of the moduli is $\sqrt2 \times 2$."),
            C(r"$\sqrt{2} \cdot 3$", why=r"$|\sqrt3 + i| = 2$, not $3$."),
        ], steps=[S("Moduli", math=r"|1 + i| = \sqrt2,\quad |\sqrt3 + i| = 2"), S("Multiply", math=r"2\sqrt2")],
           concept="Modulus of a product", skill="Calculation", hint="The modulus of a product is the product of the moduli.",
           feedback="|z1 z2| = |z1||z2| = 2√2."),
        NUM(r"Find $|-2 - 2i|$ to 2 decimal places.", 2.83, tolerance=0.01,
            steps=[S("Calculate", math=r"\sqrt{4 + 4} = 2\sqrt2 \approx 2.83")],
            concept="Modulus", skill="Calculation", hint="Square each part, add, take the square root.",
            feedback="|−2 − 2i| = 2√2 ≈ 2.83."),
        MC(r"The principal argument of $-2 - 2i$ is", [
            C(r"$\dfrac{\pi}{4}$", why="This is the first quadrant. $-2 - 2i$ has negative real and imaginary parts."),
            C(r"$\dfrac{3\pi}{4}$", why="This is the second quadrant. The imaginary part of $-2 - 2i$ is negative."),
            C(r"$-\dfrac{\pi}{4}$", why="This is the fourth quadrant."),
            C(r"$-\dfrac{3\pi}{4}$", correct=True),
        ], steps=[S("Reference angle", math=r"\tan^{-1}1 = \frac\pi4"), S("Third quadrant, principal range", math=r"-\left(\pi - \frac\pi4\right) = -\frac{3\pi}{4}")],
           concept="Argument in the third quadrant", skill="Calculation", hint="Which quadrant is the point in? The principal range is −π to π.",
           feedback="Third quadrant: the argument is −3π/4."),
        MC(r"Write $4e^{-i\pi/3}$ in the form $a + bi$.", [
            C(r"$2 + 2\sqrt3\,i$", why="The argument is negative, so the imaginary part is negative."),
            C(r"$2\sqrt3 - 2i$", why=r"$\cos\frac\pi3 = \frac12$ gives the real part $2$, not $2\sqrt3$."),
            C(r"$-2 - 2\sqrt3\,i$", why="The real part $4\\cos\\frac\\pi3$ is positive."),
            C(r"$2 - 2\sqrt3\,i$", correct=True),
        ], steps=[S("Use cos and sin", math=r"4\left(\cos\tfrac\pi3 - i\sin\tfrac\pi3\right)"), S("Evaluate", math=r"4\left(\tfrac12 - \tfrac{\sqrt3}2 i\right) = 2 - 2\sqrt3\,i")],
           concept="Exponential to Cartesian form", skill="Calculation", hint="cos is even and sin is odd, so cos(−θ) = cos θ and sin(−θ) = −sin θ.",
           feedback="4(1/2 − (√3/2)i) = 2 − 2√3 i."),
        MC(r"$z_1 = 2e^{i\pi/3}$ and $z_2 = 3e^{i\pi/6}$. Then $z_1z_2$ equals", [
            C(r"$5e^{i\pi/2}$", why="Moduli are multiplied, not added."),
            C(r"$6e^{i\pi/18}$", why="Arguments are added, not multiplied."),
            C(r"$6i$", correct=True),
            C(r"$6e^{i\pi/6}$", why="This subtracts the arguments, which is the rule for division."),
        ], steps=[S("Multiply moduli, add arguments", math=r"6e^{i(\pi/3 + \pi/6)} = 6e^{i\pi/2}"), S("Convert", math=r"6i")],
           concept="Multiplying in exponential form", skill="Calculation", hint="Multiply the moduli and add the arguments.",
           feedback="6e^(iπ/2) = 6i."),
        NUM(r"Use $(1 + i)(\sqrt3 + i) = (\sqrt3 - 1) + (\sqrt3 + 1)i$ and its argument $\dfrac{5\pi}{12}$ to find $\tan\dfrac{5\pi}{12}$, to 2 decimal places.", 3.73, tolerance=0.01,
            steps=[S("Ratio of imaginary to real part", math=r"\frac{\sqrt3 + 1}{\sqrt3 - 1} = 2 + \sqrt3 \approx 3.73")],
            concept="Exact trigonometric values from products", skill="Application", hint="The tangent of the argument is the imaginary part divided by the real part.",
            feedback="tan(5π/12) = 2 + √3."),
        MC(r"Multiplying every point of the Argand diagram by $i$ has the effect of", [
            C(r"A reflection in the real axis", why="That is taking the conjugate."),
            C(r"A rotation through $90^{\circ}$ clockwise", why=r"$i = e^{i\pi/2}$ adds $+\frac\pi2$ to the argument: anticlockwise."),
            C(r"A rotation through $90^{\circ}$ anticlockwise about the origin", correct=True),
            C(r"An enlargement by scale factor $i$", why=r"$|i| = 1$: distances from the origin do not change."),
        ], steps=[S("Polar form", math=r"i = e^{i\pi/2}"), S("Effect", text=r"The modulus is multiplied by $1$ and the argument increases by $\frac\pi2$.")],
           concept="Geometry of multiplication", skill="Concept", hint="Write i in exponential form and see what it does to the argument.",
           feedback="Multiplying by i adds π/2 to the argument."),
    ]))

# ------------------------------------------------------------------ De Moivre's theorem
SETS.append(practice_set(
    module=M2, topic="De Moivre's theorem",
    title="De Moivre's theorem and powers of complex numbers", lesson="fml1-de-moivre-theorem",
    questions=[
        MC(r"What is $\left(\cos\dfrac\pi6 + i\sin\dfrac\pi6\right)^6$?", [
            C(r"$1$", why=r"The angle is $6\times\frac\pi6 = \pi$, not $2\pi$."),
            C(r"$i$", why=r"$i$ corresponds to the angle $\frac\pi2$."),
            C(r"$-i$", why=r"$-i$ corresponds to the angle $-\frac\pi2$."),
            C(r"$-1$", correct=True),
        ], steps=[S("De Moivre", math=r"\cos\pi + i\sin\pi"), S("Evaluate", math=r"-1")],
           concept="De Moivre's theorem", skill="Calculation", hint="Multiply the angle by the power.",
           feedback="The angle becomes π, giving −1."),
        NUM(r"Find $(1 + i)^8$.", 16,
            steps=[S("Polar form", math=r"1 + i = \sqrt2\,e^{i\pi/4}"), S("Power", math=r"\left(\sqrt2\right)^8e^{2\pi i} = 16")],
            concept="Powers by De Moivre", skill="Calculation", hint="Write 1 + i in polar form first.",
            feedback="(1 + i)^8 = 16."),
        MC(r"Find $(1 - i)^{12}$.", [
            C(r"$64$", why=r"The argument is $12\times\left(-\frac\pi4\right) = -3\pi$, which gives $\cos(-3\pi) = -1$, so the sign is negative."),
            C(r"$-64$", correct=True),
            C(r"$4096$", why=r"The modulus is $\left(\sqrt2\right)^{12} = 2^6 = 64$, not $2^{12}$."),
            C(r"$-64i$", why=r"The angle $-3\pi$ is a half-turn multiple, so the result is real."),
        ], steps=[S("Polar form", math=r"1 - i = \sqrt2\,e^{-i\pi/4}"), S("Power", math=r"2^6e^{-3\pi i} = 64(-1) = -64")],
           concept="Powers by De Moivre", skill="Calculation", hint="Write 1 − i in polar form: modulus √2, argument −π/4.",
           feedback="(1 − i)^12 = 64 e^(−3πi) = −64."),
        MC(r"In the inductive step of the proof of De Moivre's theorem, the expansion of $(\cos k\theta + i\sin k\theta)(\cos\theta + i\sin\theta)$ is turned into $\cos(k+1)\theta + i\sin(k+1)\theta$ using", [
            C(r"The double-angle formulae", why="Those relate $2\\theta$ to $\\theta$. Here we need $k\\theta + \\theta$."),
            C(r"The addition formulae for $\cos(A+B)$ and $\sin(A+B)$", correct=True),
            C(r"The binomial theorem", why="The binomial theorem is not needed: the product has just two factors."),
            C(r"The factor theorem", why="This is about polynomial roots, not trigonometry."),
        ], steps=[S("Expand", math=r"(\cos k\theta\cos\theta - \sin k\theta\sin\theta) + i(\sin k\theta\cos\theta + \cos k\theta\sin\theta)"), S("Recognise", text="These are cos(kθ + θ) and sin(kθ + θ).")],
           concept="Proof of De Moivre's theorem", skill="Reasoning", hint="Look at the brackets: they match two familiar compound-angle formulae.",
           feedback="The addition formulae combine the products into cos(k+1)θ and sin(k+1)θ."),
        NUM(r"Find the smallest positive integer $n$ for which $\left(\sqrt3 + i\right)^n$ is a real number.", 6,
            steps=[S("Polar form", math=r"\sqrt3 + i = 2e^{i\pi/6}"), S("Argument of the power", math=r"\frac{n\pi}{6} = k\pi \Rightarrow n = 6k"), S("Smallest", text="n = 6, and the value is $-64$.")],
            concept="Real powers of a complex number", skill="Reasoning", hint="The power is real when its argument is a multiple of π.",
            feedback="n = 6 gives (√3 + i)^6 = −64."),
        MC(r"Simplify $\dfrac{(\cos2\theta + i\sin2\theta)^3}{(\cos\theta - i\sin\theta)^2}$.", [
            C(r"$\cos4\theta + i\sin4\theta$", why=r"The denominator $e^{-2i\theta}$ **adds** $2\theta$ to the argument when you divide: $6\theta + 2\theta = 8\theta$, not $6\theta - 2\theta$."),
            C(r"$\cos6\theta + i\sin6\theta$", why="The denominator has been ignored."),
            C(r"$\cos8\theta + i\sin8\theta$", correct=True),
            C(r"$\cos12\theta - i\sin12\theta$", why="The numerator's angle is $2\\theta\\times 3 = 6\\theta$, not $12\\theta$."),
        ], steps=[S("Numerator", math=r"e^{6i\theta}"), S("Denominator", math=r"e^{-2i\theta}"), S("Quotient", math=r"e^{8i\theta}")],
           concept="Simplifying expressions with De Moivre", skill="Application", hint="Write both brackets in exponential form; cos θ − i sin θ is e to the minus iθ.",
           feedback="e^(6iθ) divided by e^(−2iθ) is e^(8iθ)."),
        MC(r"Find $\left(-1 + \sqrt3\,i\right)^{10}$.", [
            C(r"$-512 + 512\sqrt3\,i$", correct=True),
            C(r"$1024$", why=r"The argument is $\frac{20\pi}{3} \equiv \frac{2\pi}{3}$, not a multiple of $2\pi$."),
            C(r"$512 - 512\sqrt3\,i$", why=r"This is the value with the angle $-\frac{\pi}{3}$; check the quadrant of $\frac{2\pi}3$."),
            C(r"$-1 + \sqrt3\,i$", why=r"The modulus must be $2^{10} = 1024$, not $2$."),
        ], steps=[S("Polar form", math=r"2e^{2\pi i/3}"), S("Power", math=r"1024e^{20\pi i/3} = 1024e^{2\pi i/3}"), S("Convert", math=r"1024\left(-\tfrac12 + \tfrac{\sqrt3}2 i\right)")],
           concept="Large powers with angle reduction", skill="Calculation", hint="Reduce the angle 20π/3 by whole turns before reading cos and sin.",
           feedback="20π/3 − 6π = 2π/3."),
        MC(r"Find $\left(\dfrac{1+i}{1-i}\right)^{9}$.", [
            C(r"$1$", why=r"$\frac{1+i}{1-i} = i$, and $i^9 = i^8 \cdot i = i$, not $1$."),
            C(r"$i$", correct=True),
            C(r"$-1$", why=r"$i^2 = -1$ but $i^9$ is not an even power."),
            C(r"$-i$", why=r"$i^9 = i^{8+1} = i$. The sign $-i$ would be $i^3$."),
        ], steps=[S("Simplify the quotient", math=r"\frac{1+i}{1-i} = \frac{(1+i)^2}{2} = \frac{2i}{2} = i"), S("Power", math=r"i^9 = \left(i^4\right)^2 i = i")],
           concept="Powers of a quotient", skill="Application", hint="Simplify the fraction first.",
           feedback="The quotient is i, and i^9 = i."),
    ]))

# ------------------------------------------------------------------ De Moivre: identities
SETS.append(practice_set(
    module=M2, topic="De Moivre's theorem",
    title="Multiple-angle and power-reduction identities", lesson="fml1-de-moivre-identities",
    questions=[
        MC(r"Which is the formula for $\cos3\theta$?", [
            C(r"$3\cos\theta - 4\cos^3\theta$", why="This reverses the formula. It resembles $\\sin3\\theta = 3\\sin\\theta - 4\\sin^3\\theta$."),
            C(r"$3\cos\theta$", why="Multiplying the angle by 3 does not multiply the cosine by 3."),
            C(r"$4\cos^3\theta - 3\cos\theta$", correct=True),
            C(r"$\cos^3\theta - 3\cos\theta\sin^2\theta - 1$", why="The correct real part is $c^3 - 3cs^2$, with no extra $-1$; and in terms of $c$ alone it is $4c^3 - 3c$."),
        ], steps=[S("Real part of $(c + is)^3$", math=r"c^3 - 3cs^2"), S("Use $s^2 = 1 - c^2$", math=r"4c^3 - 3c")],
           concept="cos 3θ formula", skill="Recall", hint="Expand (cos θ + i sin θ)^3 and take the real part.",
           feedback="cos 3θ = 4cos³θ − 3cos θ."),
        MC(r"With $z = \cos\theta + i\sin\theta$, the expression $z^n + \dfrac{1}{z^n}$ equals", [
            C(r"$2i\sin n\theta$", why="That is the difference $z^n - z^{-n}$."),
            C(r"$\cos n\theta$", why="The factor 2 is missing."),
            C(r"$2\cos\theta^n$", why="The angle is multiplied by $n$; the cosine is not raised to a power."),
            C(r"$2\cos n\theta$", correct=True),
        ], steps=[S("De Moivre", math=r"z^n = \cos n\theta + i\sin n\theta,\quad z^{-n} = \cos n\theta - i\sin n\theta"), S("Add", math=r"2\cos n\theta")],
           concept="z^n + 1/z^n", skill="Concept", hint="Write z^n and 1/z^n with De Moivre and add.",
           feedback="The sine terms cancel and the cosines add."),
        NUM(r"Use $\cos3\theta = 4\cos^3\theta - 3\cos\theta$ to find $\cos3\theta$ when $\cos\theta = \dfrac12$.", -1,
            steps=[S("Substitute", math=r"4\left(\tfrac18\right) - 3\left(\tfrac12\right) = \tfrac12 - \tfrac32 = -1"), S("Check", text=r"$\theta = 60^{\circ}$ and $\cos180^{\circ} = -1$.")],
            concept="Using the cos 3θ formula", skill="Calculation", hint="Cube the cosine and substitute.",
            feedback="θ = 60° gives cos 180° = −1."),
        MC(r"Which is $\cos^4\theta$ in terms of multiple angles?", [
            C(r"$\dfrac18\left(\cos4\theta + 4\cos2\theta + 3\right)$", correct=True),
            C(r"$\dfrac18\left(\cos4\theta - 4\cos2\theta + 3\right)$", why=r"This is $\sin^4\theta$. For cosine the middle term is $+4\cos2\theta$."),
            C(r"$\dfrac1{16}\left(\cos4\theta + 4\cos2\theta + 3\right)$", why=r"$\left(z + \frac1z\right)^4 = 16\cos^4\theta$ gives $2\cos4\theta + 8\cos2\theta + 6$; dividing by 16 gives $\frac18(\ldots)$."),
            C(r"$\cos4\theta$", why="A fourth power of cosine is not the cosine of four times the angle."),
        ], steps=[S("Expand", math=r"\left(z + \tfrac1z\right)^4 = z^4 + 4z^2 + 6 + \tfrac4{z^2} + \tfrac1{z^4}"), S("Pair terms", math=r"16\cos^4\theta = 2\cos4\theta + 8\cos2\theta + 6")],
           concept="Power reduction for cos^4", skill="Calculation", hint="Expand (z + 1/z)^4 and group z^k with z^(-k).",
           feedback="cos⁴θ = (cos 4θ + 4cos 2θ + 3)/8."),
        NUM(r"Use $\cos^4\theta = \frac18(\cos4\theta + 4\cos2\theta + 3)$ to evaluate $\displaystyle\int_0^{\pi/2}\cos^4\theta\,d\theta$, to 3 decimal places.", 0.589, tolerance=0.002,
            steps=[S("Integrate term by term", math=r"\frac18\left[\frac{\sin4\theta}{4} + 2\sin2\theta + 3\theta\right]_0^{\pi/2}"), S("Evaluate", math=r"\frac18\cdot\frac{3\pi}{2} = \frac{3\pi}{16} \approx 0.589")],
            concept="Integrating powers of cosine", skill="Calculation", hint="The sine terms vanish at 0 and π/2; only the constant term contributes.",
            feedback="The integral is 3π/16."),
        MC(r"With $t = \tan\theta$, $\tan3\theta$ equals", [
            C(r"$3t$", why="Tripling the angle does not triple the tangent."),
            C(r"$\dfrac{3t - t^3}{1 - 3t^2}$", correct=True),
            C(r"$\dfrac{3t + t^3}{1 + 3t^2}$", why="The signs are wrong: the numerator has $-t^3$ and the denominator $-3t^2$."),
            C(r"$\dfrac{t^3 - 3t}{1 - 3t^2}$", why="The numerator has its terms in the wrong order: it should be $3t - t^3$."),
        ], steps=[S("Ratio", math=r"\frac{3c^2s - s^3}{c^3 - 3cs^2}"), S("Divide by $c^3$", math=r"\frac{3t - t^3}{1 - 3t^2}")],
           concept="tan 3θ", skill="Calculation", hint="Divide sin 3θ by cos 3θ, then divide top and bottom by cos cubed.",
           feedback="tan 3θ = (3t − t³)/(1 − 3t²)."),
        MC(r"$x = \cos\dfrac\pi9$ is a root of which equation?", [
            C(r"$8x^3 - 6x + 1 = 0$", why=r"$4x^3 - 3x = \cos\frac\pi3 = +\frac12$, so the constant is $-1$, not $+1$."),
            C(r"$4x^3 - 3x = 1$", why=r"$\cos\frac\pi3 = \frac12$, not $1$."),
            C(r"$8x^3 - 6x - 1 = 0$", correct=True),
            C(r"$x^3 - 3x + 1 = 0$", why="The cubic comes from $4x^3 - 3x = \\frac12$ and its coefficients are $8, 0, -6, -1$."),
        ], steps=[S("Put $\\theta = \\frac\\pi9$", math=r"\cos3\theta = \cos\tfrac\pi3 = \tfrac12"), S("Use the formula", math=r"4x^3 - 3x = \tfrac12 \Rightarrow 8x^3 - 6x - 1 = 0")],
           concept="Cubic with a cosine root", skill="Application", hint="Use cos 3θ = 4cos³θ − 3cos θ with 3θ = π/3.",
           feedback="cos 3θ = ½ gives 8x³ − 6x − 1 = 0."),
        NUM(r"Use $\sin^5\theta = \frac1{16}(10\sin\theta - 5\sin3\theta + \sin5\theta)$ to evaluate $\displaystyle\int_0^{\pi/2}\sin^5\theta\,d\theta$, to 3 decimal places.", 0.533, tolerance=0.002,
            steps=[S("Integrals", math=r"\int_0^{\pi/2}\sin\theta = 1,\ \int_0^{\pi/2}\sin3\theta = \tfrac13,\ \int_0^{\pi/2}\sin5\theta = \tfrac15"), S("Combine", math=r"\tfrac{1}{16}\left(10 - \tfrac53 + \tfrac15\right) = \tfrac{8}{15} \approx 0.533")],
            concept="Integrating powers of sine", skill="Calculation", hint="Integrate each sine term from 0 to π/2: the integral of sin kθ is (1 − cos(kπ/2))/k.",
            feedback="The integral is 8/15."),
    ]))

# ------------------------------------------------------------------ Roots of unity
SETS.append(practice_set(
    module=M2, topic="Roots of unity",
    title="Roots of unity and nth roots of complex numbers", lesson="fml1-roots-of-unity",
    questions=[
        MC(r"How many roots does the equation $z^7 = 3 + 4i$ have, and what is the modulus of each?", [
            C(r"$7$ roots, each of modulus $5$", why=r"$|z|^7 = 5$, so $|z| = 5^{1/7}$. The modulus $5$ belongs to the right-hand side."),
            C(r"$1$ root, of modulus $5^{1/7}$", why="A polynomial equation of degree 7 has 7 roots (counted with multiplicity)."),
            C(r"$7$ roots, each of modulus $5^{1/7}$", correct=True),
            C(r"$7$ roots, each of modulus $\dfrac57$", why="The modulus of the root is the seventh root of 5, not 5 divided by 7."),
        ], steps=[S("Take moduli", math=r"|z|^7 = |3 + 4i| = 5"), S("Solve", math=r"|z| = 5^{1/7}")],
           concept="Number and modulus of nth roots", skill="Concept", hint="Take the modulus of both sides, and count using the degree.",
           feedback="There are seven roots with equal modulus 5^(1/7)."),
        MC(r"Which of the following is a root of $z^3 = 8i$?", [
            C(r"$2i$", why=r"$(2i)^3 = 8i^3 = -8i$."),
            C(r"$2$", why=r"$2^3 = 8$, which is real."),
            C(r"$-2i$", correct=True),
            C(r"$\sqrt3 - i$", why=r"$\sqrt3 - i = 2e^{-i\pi/6}$ and its cube is $8e^{-i\pi/2} = -8i$."),
        ], steps=[S("Check $-2i$", math=r"(-2i)^3 = -8i^3 = -8(-i) = 8i")],
           concept="Roots of z^n = w", skill="Calculation", hint="Cube each option, using i cubed equals −i.",
           feedback="(−2i)³ = 8i."),
        NUM(r"Find the sum of all five fifth roots of unity.", 0,
            steps=[S("The equation", math=r"z^5 - 1 = 0 \text{ has no } z^4 \text{ term}"), S("Sum of roots", math=r"-\frac{0}{1} = 0")],
            concept="Sum of roots of unity", skill="Concept", hint="Use the sum of roots of a polynomial: look at the coefficient of z^4.",
            feedback="The roots of unity always sum to zero."),
        MC(r"The diagram shows all the solutions of $z^n = 1$ in the Argand diagram. What is $n$?", [
            C(r"$4$", why="Count the points on the circle: there are more than four."),
            C(r"$6$", why="Count again: the polygon has fewer than six vertices."),
            C(r"$5$", correct=True),
            C(r"$10$", why="There are only as many points as the degree of the equation."),
        ], steps=[S("Count the vertices", text="The points are the vertices of a regular polygon with 5 corners, one of them at the point 1."), S("So", math=r"n = 5")],
           diagram="al-fml1-roots-of-unity-q.svg", diagram_alt="A unit circle with five equally spaced points, one on the positive real axis, joined to form a regular pentagon",
           concept="Roots of unity as a polygon", skill="Interpretation", hint="The number of solutions equals the degree n.",
           feedback="A regular pentagon: the five fifth roots of unity."),
        MC(r"The equation $z^4 = -16$ has the root", [
            C(r"$2$", why=r"$2^4 = 16$, not $-16$."),
            C(r"$\sqrt2 + \sqrt2\,i$", correct=True),
            C(r"$4i$", why=r"$(4i)^4 = 256$."),
            C(r"$-2i$", why=r"$(-2i)^4 = 16$."),
        ], steps=[S("Square", math=r"\left(\sqrt2 + \sqrt2 i\right)^2 = 2 - 2 + 4i = 4i"), S("Square again", math=r"(4i)^2 = -16")],
           concept="Fourth roots of a negative number", skill="Calculation", hint="Square the option twice.",
           feedback="The four roots are √2(±1 ± i)."),
        MC(r"If $\omega$ is a complex cube root of unity, what is $\left(1 + \omega\right)^3$?", [
            C(r"$1$", why=r"$1 + \omega = -\omega^2$, and $(-\omega^2)^3 = -\omega^6 = -1$."),
            C(r"$8$", why="This treats $\\omega$ as $1$."),
            C(r"$0$", why=r"$1 + \omega + \omega^2 = 0$, but $1 + \omega = -\omega^2$ is not zero."),
            C(r"$-1$", correct=True),
        ], steps=[S("Use the sum", math=r"1 + \omega = -\omega^2"), S("Cube", math=r"(-\omega^2)^3 = -\omega^6 = -(\omega^3)^2 = -1")],
           concept="Cube roots of unity", skill="Reasoning", hint="Replace 1 + ω using 1 + ω + ω² = 0.",
           feedback="(1 + ω)³ = −1."),
        NUM(r"Using $z^4 + z^3 + z^2 + z + 1 = 0$ and $2\cos\frac{2\pi}{5} = \frac{-1 + \sqrt5}{2}$, find $\cos72^{\circ}$ to 3 decimal places.", 0.309, tolerance=0.001,
            steps=[S("Solve", math=r"\cos72^{\circ} = \frac{\sqrt5 - 1}{4} \approx 0.309")],
            concept="Exact cosines from roots of unity", skill="Calculation", hint="72 degrees is 2π/5. Divide the given value by 2.",
            feedback="cos 72° = (√5 − 1)/4 ≈ 0.309."),
        MC(r"How many solutions does $(z - 1)^4 = z^4$ have?", [
            C(r"$4$", why=r"Dividing by $z^4$ gives $\left(\frac{z-1}z\right)^4 = 1$, but the root $w = 1$ gives $0 = 1$, so one of the four values is rejected."),
            C(r"$3$", correct=True),
            C(r"$1$", why=r"Only the real solution $z = \frac12$ has been found; the roots $\frac{1 \pm i}2$ are missed."),
            C(r"$0$", why="The equation has solutions: $z = \\frac12$ satisfies $\\left(-\\frac12\\right)^4 = \\left(\\frac12\\right)^4$."),
        ], steps=[S("Quotient", math=r"w = \frac{z-1}{z},\ w^4 = 1"), S("Reject $w = 1$", text="It gives 0 = 1."), S("Solutions", math=r"z = \frac{1}{1 - w} \text{ for } w = i, -1, -i")],
           concept="Equations reducing to roots of unity", skill="Reasoning", hint="Divide by z^4 and treat (z − 1)/z as an unknown.",
           feedback="The equation is really cubic: the z⁴ terms cancel."),
    ]))

# ------------------------------------------------------------------ Loci
SETS.append(practice_set(
    module=M2, topic="Loci in the Argand plane",
    title="Loci: circles, bisectors, half-lines and transformations", lesson="fml1-loci-argand-plane",
    questions=[
        MC(r"The locus $|z + 2 - 3i| = 1$ is a circle with", [
            C(r"centre $2 - 3i$, radius $1$", why="The expression is $z - (-2 + 3i)$, so the centre has the opposite signs."),
            C(r"centre $-2 + 3i$, radius $1$", correct=True),
            C(r"centre $-2 - 3i$, radius $1$", why="The imaginary part of the centre is $+3$: $-3i$ is subtracted inside."),
            C(r"centre $0$, radius $\sqrt{13}$", why=r"$\sqrt{13}$ is $|{-2} + 3i|$, the distance of the centre from the origin."),
        ], steps=[S("Rewrite", math=r"|z - (-2 + 3i)| = 1"), S("Read", text="Centre −2 + 3i, radius 1.")],
           concept="Circle locus", skill="Calculation", hint="Write the expression as z minus a single complex number.",
           feedback="The centre is the number subtracted from z."),
        MC(r"The circle in the diagram has its centre at $2 + i$ and passes through $5 + i$. Which equation describes it?", [
            C(r"$|z - 2 - i| = 3$", correct=True),
            C(r"$|z + 2 + i| = 3$", why="This circle has centre $-2 - i$. The centre of the given circle is $2 + i$."),
            C(r"$|z - 2 - i| = 5$", why=r"The radius is the distance from the centre to $5 + i$, which is $3$."),
            C(r"$|z - 5 - i| = 3$", why=r"The centre is $2 + i$, not the point on the circle."),
        ], steps=[S("Centre", text="The centre is 2 + i."), S("Radius", math=r"|(5 + i) - (2 + i)| = 3"), S("Equation", math=r"|z - (2 + i)| = 3")],
           diagram="al-fml1-locus-q.svg", diagram_alt="A circle on an Argand diagram with grid lines, centre at the point 2 + i, passing through the point 5 + i",
           concept="Reading a locus from a diagram", skill="Interpretation", hint="Find the centre and a point on the circle, then work out the distance.",
           feedback="Centre 2 + i, radius 3."),
        MC(r"The locus $|z| = |z - 4|$ is", [
            C(r"a circle, centre $2$, radius $2$", why="A circle needs a fixed distance from a point. Here two distances are equal."),
            C(r"the line $x = 4$", why="This is the vertical line through the point $4$, not the bisector of $0$ and $4$."),
            C(r"the line $x = 2$", correct=True),
            C(r"the half-line $\arg z = 4$", why="An argument is an angle, not a distance."),
        ], steps=[S("Square", math=r"x^2 + y^2 = (x-4)^2 + y^2"), S("Simplify", math=r"8x = 16 \Rightarrow x = 2")],
           concept="Perpendicular bisector locus", skill="Calculation", hint="The points are equally far from 0 and from 4.",
           feedback="The perpendicular bisector of 0 and 4 is x = 2."),
        NUM(r"The locus $|z - 6| = 2|z|$ is a circle. Find its radius.", 4,
            steps=[S("Square", math=r"(x-6)^2 + y^2 = 4x^2 + 4y^2"), S("Simplify", math=r"x^2 + 4x + y^2 = 12"), S("Complete the square", math=r"(x+2)^2 + y^2 = 16")],
            concept="Circle of Apollonius", skill="Calculation", hint="Put z = x + iy, square both sides and complete the square.",
            feedback="The circle has centre −2 and radius 4."),
        MC(r"The locus $\arg(z - 1 - i) = \dfrac\pi4$ is", [
            C(r"the line $y = x$", why="This is the full line. The argument condition gives only the half-line with $x > 1$."),
            C(r"the half-line $y = x$, $x > 1$", correct=True),
            C(r"the half-line $y = x$, $x < 1$", why=r"An argument of $\frac\pi4$ points up and to the right of $1 + i$, so $x > 1$."),
            C(r"a circle with centre $1 + i$", why="An argument condition gives a half-line, not a circle."),
        ], steps=[S("Meaning", text=r"The line from $1 + i$ to $z$ makes an angle $\frac\pi4$ with the positive real axis."), S("Cartesian form", math=r"y - 1 = x - 1,\ x > 1")],
           concept="Half-line locus", skill="Calculation", hint="The line starts at 1 + i. In which direction does it go?",
           feedback="A half-line starting at (1, 1), excluding that point."),
        MC(r"The locus $|z - 4| = |z + 2i|$ has Cartesian equation", [
            C(r"$2x + y = 3$", correct=True),
            C(r"$2x - y = 3$", why=r"Expanding $(y+2)^2$ gives $+4y$, so the $y$ term has the opposite sign to $2x$ on the same side."),
            C(r"$x + 2y = 3$", why="The coefficients are swapped."),
            C(r"$(x - 4)^2 + (y + 2)^2 = 0$", why="That is a single point, not the equal-distance condition."),
        ], steps=[S("Square", math=r"(x-4)^2 + y^2 = x^2 + (y+2)^2"), S("Expand", math=r"-8x + 16 = 4y + 4"), S("Simplify", math=r"2x + y = 3")],
           concept="Cartesian form of a bisector", skill="Calculation", hint="Put z = x + iy and square both sides; the x² and y² terms cancel.",
           feedback="The bisector is the line 2x + y = 3."),
        NUM(r"The point $z$ moves on the circle $|z| = 2$. Find the radius of the circle traced by $w = 3z + 1 - 2i$.", 6,
            steps=[S("Solve for $z$", math=r"z = \frac{w - 1 + 2i}{3}"), S("Substitute", math=r"|w - (1 - 2i)| = 6")],
            concept="Transformation of a circle", skill="Application", hint="Solve for z in terms of w and substitute into |z| = 2.",
            feedback="The radius is multiplied by |3| = 3."),
        MC(r"The locus $\arg\left(\dfrac{z - 1}{z + 1}\right) = \dfrac\pi2$ is", [
            C(r"the whole unit circle", why=r"The condition $y > 0$ (positive imaginary part) restricts it to the upper half."),
            C(r"the line $x = 0$", why="That is the bisector of $-1$ and $1$, the locus of $|z - 1| = |z + 1|$."),
            C(r"the upper half of the unit circle, without $\pm1$", correct=True),
            C(r"the lower half of the unit circle", why=r"An argument of $+\frac\pi2$ needs a positive imaginary part, so $y > 0$."),
        ], steps=[S("Real part zero", math=r"x^2 + y^2 - 1 = 0"), S("Imaginary part positive", math=r"y > 0")],
           concept="Argument of a quotient", skill="Reasoning", hint="Multiply by the conjugate and require real part 0 and imaginary part positive.",
           feedback="The angle in a semicircle is a right angle: the upper semicircle."),
    ]))

# ================================================================== MODULE 3: MATRICES, DETERMINANTS & LINEAR SYSTEMS
# ------------------------------------------------------------------ Determinants and inverses
SETS.append(practice_set(
    module=M3, topic="Determinants and inverses of 3 by 3 matrices",
    title="Determinants, singular matrices and inverses", lesson="fml1-determinants-inverses",
    questions=[
        MC(r"A $3\times3$ matrix has two identical rows. Its determinant is", [
            C(r"$1$", why="The identity matrix has determinant 1, but a matrix with repeated rows is squashed flat."),
            C(r"$2$", why="There is no rule that gives the number of repeated rows as the determinant."),
            C(r"the sum of its diagonal entries", why="That is the trace, not the determinant."),
            C(r"$0$", correct=True),
        ], steps=[S("Swap the two identical rows", text=r"The matrix is unchanged, but the determinant changes sign. So $\det = -\det$."), S("Conclude", math=r"\det = 0")],
           concept="Properties of determinants", skill="Concept", hint="What happens to the determinant when you swap two rows? And what happens to the matrix if they are equal?",
           feedback="Two equal rows give a determinant of zero."),
        NUM(r"Evaluate $\begin{vmatrix} 3 & 1 & 2 \\ 0 & 2 & -1 \\ 1 & 0 & 4 \end{vmatrix}$.", 19,
            steps=[S("Expand along the first row", math=r"3(8 - 0) - 1(0 + 1) + 2(0 - 2)"), S("Calculate", math=r"24 - 1 - 4 = 19")],
            concept="3 by 3 determinant", skill="Calculation", hint="Expand along the first row with signs plus, minus, plus.",
            feedback="The determinant is 19."),
        MC(r"The $3\times3$ matrix $\mathbf{A}$ has $\det\mathbf{A} = 5$. What is $\det(2\mathbf{A})$?", [
            C(r"$10$", why="Each of the three rows is doubled, so the factor is $2^3$, not $2$."),
            C(r"$20$", why=r"$2^2$ is the factor for a $2\times2$ matrix."),
            C(r"$40$", correct=True),
            C(r"$25$", why="The determinant is not squared when you double the matrix."),
        ], steps=[S("Each row is multiplied by 2", math=r"\det(2\mathbf{A}) = 2^3\det\mathbf{A} = 8\times5 = 40")],
           concept="Determinant of a scalar multiple", skill="Application", hint="How many rows are multiplied by 2?",
           feedback="det(kA) = k³ det A for a 3 by 3 matrix."),
        MC(r"Find $\begin{vmatrix} 2 & -1 & 0 \\ 1 & 3 & 2 \\ 0 & 1 & 1 \end{vmatrix}$.", [
            C(r"$1$", why=r"The middle term is $-(-1)\times\begin{vmatrix} 1 & 2 \\ 0 & 1 \end{vmatrix} = +1$. The signs have been applied wrongly."),
            C(r"$2$", why="This stops after the first term. The second term contributes $+1$."),
            C(r"$-3$", why="The overall sign is wrong: the first-row expansion gives a positive result."),
            C(r"$3$", correct=True),
        ], steps=[S("Expand along the first row", math=r"2(3 - 2) - (-1)(1 - 0) + 0 = 2 + 1"), S("Answer", math=r"3")],
           concept="Cofactor signs", skill="Calculation", hint="The middle term has a minus sign in front of the entry, and the entry is −1.",
           feedback="2(1) + 1(1) + 0 = 3."),
        MC(r"For which value of $k$ is $\begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & k \end{pmatrix}$ singular?", [
            C(r"$k = 3$", why="$3$ is the entry in the first row; the determinant is $27 - 3k$, which is not zero at $k = 3$."),
            C(r"$k = 6$", why="The determinant at $k = 6$ is $27 - 18 = 9$, not zero."),
            C(r"$k = 9$", correct=True),
            C(r"$k = 0$", why=r"At $k = 0$ the determinant is $27$, so the matrix is not singular."),
        ], steps=[S("Determinant", math=r"1(5k - 48) - 2(4k - 42) + 3(32 - 35) = 27 - 3k"), S("Set to zero", math=r"k = 9")],
           concept="Singular matrix with a parameter", skill="Calculation", hint="Expand the determinant as an expression in k and set it equal to zero.",
           feedback="The determinant is 27 − 3k, zero when k = 9."),
        NUM(r"The matrix $\begin{pmatrix} k & 1 & 1 \\ 1 & k & 1 \\ 1 & 1 & k \end{pmatrix}$ has determinant $(k - 1)^2(k + 2)$. Find the larger of the two values of $k$ for which it is singular.", 1,
            steps=[S("Set to zero", math=r"(k - 1)^2(k + 2) = 0 \Rightarrow k = 1 \text{ or } k = -2"), S("Larger", text="The larger value is $k = 1$.")],
            concept="Singular values of a parameter", skill="Calculation", hint="A product is zero when one of its factors is zero.",
            feedback="k = 1 (repeated) and k = −2."),
        MC(r"$\mathbf{A}$ and $\mathbf{B}$ are invertible $3\times3$ matrices. Which is equal to $(\mathbf{AB})^{-1}$?", [
            C(r"$\mathbf{A}^{-1}\mathbf{B}^{-1}$", why=r"The order must be reversed: $(\mathbf{AB})\left(\mathbf{A}^{-1}\mathbf{B}^{-1}\right)$ does not simplify."),
            C(r"$\mathbf{B}^{-1}\mathbf{A}^{-1}$", correct=True),
            C(r"$\mathbf{A}\mathbf{B}$", why=r"This is the product itself, not its inverse."),
            C(r"$\dfrac{1}{\mathbf{A}\mathbf{B}}$", why="There is no division of matrices. The inverse is a matrix, found by the reversed product."),
        ], steps=[S("Check", math=r"(\mathbf{AB})\left(\mathbf{B}^{-1}\mathbf{A}^{-1}\right) = \mathbf{A}\left(\mathbf{B}\mathbf{B}^{-1}\right)\mathbf{A}^{-1} = \mathbf{A}\mathbf{A}^{-1} = \mathbf{I}")],
           concept="Inverse of a product", skill="Concept", hint="Put on your shoes after your socks; to undo, take the shoes off first.",
           feedback="The inverse of a product reverses the order."),
        MC(r"For $\mathbf{M} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$, with $\det\mathbf{M} = 1$, the entry in row 1, column 2 of $\mathbf{M}^{-1}$ is", [
            C(r"$20$", why=r"This is the cofactor in row 1, column 2. The adjugate is the **transpose** of the cofactor matrix, so we need the cofactor of row 2, column 1."),
            C(r"$-18$", why="The cofactor of row 2, column 1 is $+18$; the sign comes from the pattern, not from the minor alone."),
            C(r"$18$", correct=True),
            C(r"$-24$", why=r"This is the entry in row 1, column 1 of $\mathbf{M}^{-1}$."),
        ], steps=[S("Entry (1, 2) of the adjugate = cofactor of entry (2, 1)", math=r"-\begin{vmatrix} 2 & 3 \\ 6 & 0 \end{vmatrix} = -(0 - 18) = 18"), S("Divide by the determinant", math=r"\frac{18}{1} = 18")],
           concept="Adjugate and inverse", skill="Calculation", hint="The adjugate is the transposed cofactor matrix: delete row 2 and column 1.",
           feedback="The (1, 2) entry of the inverse uses the cofactor of the (2, 1) entry."),
    ]))

# ------------------------------------------------------------------ Gaussian elimination
SETS.append(practice_set(
    module=M3, topic="Gaussian elimination and linear systems",
    title="Row operations, consistency and planes", lesson="fml1-gaussian-elimination-systems",
    questions=[
        MC(r"Which of these is **not** an allowed row operation in Gaussian elimination?", [
            C(r"Swap two rows", why="Swapping two equations does not change the solution."),
            C(r"Add $2\times$ row 1 to row 3", why="Adding a multiple of one equation to another is allowed."),
            C(r"Multiply a row by $0$", correct=True),
            C(r"Multiply a row by $-3$", why="Multiplying an equation by a non-zero number is allowed."),
        ], steps=[S("Why", text="Multiplying by 0 turns an equation into 0 = 0 and loses information, so the new system could have extra solutions.")],
           concept="Row operations", skill="Concept", hint="Which operation can lose information about the system?",
           feedback="Only a non-zero multiple of a row is allowed."),
        MC(r"After row operations the last row of an augmented matrix is $\begin{pmatrix} 0 & 0 & 0 & | & 7 \end{pmatrix}$. The system has", [
            C(r"a unique solution", why="A unique solution needs a leading entry in every row."),
            C(r"infinitely many solutions", why="That needs a last row $0 = 0$, not $0 = 7$."),
            C(r"no solution", correct=True),
            C(r"the solution $x = y = z = 7$", why="The row says $0 = 7$, an impossible statement."),
        ], steps=[S("Read the row", math=r"0x + 0y + 0z = 7 \Rightarrow 0 = 7")],
           concept="Inconsistent systems", skill="Interpretation", hint="Write the last row as an equation.",
           feedback="0 = 7 is impossible."),
        NUM(r"Solve $x + y + z = 6$, $2x + y - z = 1$, $x - y + 2z = 5$. Give the value of $z$.", 3,
            steps=[S("Eliminate $x$", math=r"R_2 - 2R_1: -y - 3z = -11,\quad R_3 - R_1: -2y + z = -1"), S("Eliminate $y$", math=r"R_3 - 2R_2: 7z = 21"), S("Solve", math=r"z = 3,\ y = 2,\ x = 1")],
            concept="Gaussian elimination", skill="Calculation", hint="Use row 1 to remove x from rows 2 and 3, then remove y from row 3.",
            feedback="The solution is (1, 2, 3)."),
        MC(r"The system has $\det\mathbf{A} = 0$ and elimination ends with a last row $0 = 0$. The three planes", [
            C(r"meet at a single point", why="A single point needs $\\det\\mathbf{A} \\neq 0$."),
            C(r"form a triangular prism", why="A prism has no common point, which would give a last row $0 = $ non-zero."),
            C(r"share a common line (or are identical)", correct=True),
            C(r"are all parallel and different", why="Parallel different planes give no common point."),
        ], steps=[S("Free parameter", text=r"The row $0 = 0$ leaves one unknown free: a line of solutions.")],
           concept="Planes and solutions", skill="Interpretation", hint="How many solutions does a last row 0 = 0 allow?",
           feedback="Infinitely many solutions means a common line or a common plane."),
        MC(r"For which values of $k$ does $x + y + z = 1$, $x + 2y + 3z = 2$, $x + 3y + 5z = k$ have **no** solution?", [
            C(r"$k = 3$", why="At $k = 3$ the last row is $0 = 0$ and there are infinitely many solutions."),
            C(r"$k = 1$ only", why="Every value except $3$ gives a last row $0 = k - 3 \\neq 0$."),
            C(r"all $k \neq 3$", correct=True),
            C(r"no value of $k$", why="The row $0 = k - 3$ is impossible whenever $k \\neq 3$."),
        ], steps=[S("Eliminate", math=r"\text{last row: } 0 = k - 3"), S("Conclude", text="No solution unless k = 3.")],
           concept="Consistency with a parameter", skill="Reasoning", hint="Reduce to echelon form and read the last row.",
           feedback="The last row is 0 = k − 3."),
        NUM(r"At a market, $2r + o + s = 3100$, $r + 2o + s = 3700$ and $r + o + 3s = 3900$, where $r$, $o$, $s$ are the prices (in FCFA) of rice, oil and sugar. Find $o$.", 1200,
            steps=[S("Eliminate", math=r"7s = 4900 \Rightarrow s = 700"), S("Back-substitute", math=r"o = 1200,\quad r = 600")], unit="FCFA",
            concept="Setting up and solving a system", skill="Application", hint="Use row operations to eliminate r, then o.",
            feedback="Rice 600, oil 1200, sugar 700 FCFA."),
        MC(r"The system $x + y + z = 1$, $x + 2y + 3z = 4$, $2x + 3y + \lambda z = \mu$ has a unique solution when", [
            C(r"$\lambda = 4$ and $\mu = 5$", why="This is the case with infinitely many solutions."),
            C(r"$\lambda = 4$ and $\mu \neq 5$", why="This is the case with no solution."),
            C(r"$\lambda \neq 4$, for any $\mu$", correct=True),
            C(r"$\mu \neq 5$, for any $\lambda$", why=r"If $\lambda = 4$ and $\mu \neq 5$ there is no solution at all."),
        ], steps=[S("After elimination", math=r"(\lambda - 4)z = \mu - 5"), S("Unique solution", text=r"Possible exactly when the coefficient of $z$ is non-zero, $\lambda \neq 4$.")],
           concept="Parameters and uniqueness", skill="Reasoning", hint="Reduce to a last equation containing only z.",
           feedback="The coefficient of z is λ − 4."),
        MC(r"Three planes meet in pairs along three parallel lines, and there is no point common to all three. The corresponding system is", [
            C(r"consistent with a unique solution", why="A unique solution is a single common point."),
            C(r"consistent with infinitely many solutions", why="Infinitely many solutions need a common line or plane."),
            C(r"inconsistent (a triangular prism)", correct=True),
            C(r"the zero system", why="The zero system has every point as a solution."),
        ], steps=[S("Meaning", text="No point lies on all three planes, so the system has no solution: it is inconsistent.")],
           concept="Triangular prism", skill="Interpretation", hint="Is there a point on all three planes?",
           feedback="A triangular prism means no common point."),
    ]))

# ------------------------------------------------------------------ Eigenvalues and eigenvectors
SETS.append(practice_set(
    module=M3, topic="Eigenvalues and eigenvectors",
    title="Eigenvalues, eigenvectors and the characteristic equation", lesson="fml1-eigenvalues-eigenvectors",
    questions=[
        MC(r"Which equation defines an eigenvector $\mathbf{v}$ and eigenvalue $\lambda$ of $\mathbf{A}$?", [
            C(r"$\mathbf{A}\mathbf{v} = \lambda\mathbf{v}$, with $\mathbf{v} \neq \mathbf{0}$", correct=True),
            C(r"$\mathbf{A}\mathbf{v} = \mathbf{v}\mathbf{A}$", why="This compares two products, which is not the definition."),
            C(r"$\mathbf{A} + \mathbf{v} = \lambda$", why="A matrix and a vector cannot be added."),
            C(r"$\det\mathbf{A} = \lambda\mathbf{v}$", why="A determinant is a number and $\\lambda\\mathbf{v}$ is a vector."),
        ], steps=[S("Definition", math=r"\mathbf{A}\mathbf{v} = \lambda\mathbf{v},\quad \mathbf{v} \neq \mathbf{0}")],
           concept="Definition of eigenvectors", skill="Recall", hint="The matrix sends the vector to a multiple of itself.",
           feedback="An eigenvector is only stretched by the matrix."),
        NUM(r"Find the larger eigenvalue of $\begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$.", 5,
            steps=[S("Characteristic equation", math=r"\lambda^2 - 7\lambda + 10 = 0"), S("Solve", math=r"(\lambda - 2)(\lambda - 5) = 0")],
            concept="Characteristic equation", skill="Calculation", hint="Solve det(A − λI) = 0.",
            feedback="The eigenvalues are 2 and 5."),
        MC(r"A $2\times2$ matrix has trace $5$ and determinant $6$. Its eigenvalues are", [
            C(r"$1$ and $6$", why="These multiply to $6$ but add to $7$."),
            C(r"$2$ and $3$", correct=True),
            C(r"$-2$ and $-3$", why="These multiply to $6$ but add to $-5$."),
            C(r"$5$ and $6$", why="These are the trace and determinant themselves."),
        ], steps=[S("Characteristic equation", math=r"\lambda^2 - 5\lambda + 6 = 0 \Rightarrow (\lambda - 2)(\lambda - 3) = 0")],
           concept="Trace and determinant", skill="Application", hint="The eigenvalues add to the trace and multiply to the determinant.",
           feedback="2 + 3 = 5 and 2 × 3 = 6."),
        MC(r"An eigenvector of $\begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ for the eigenvalue $2$ is", [
            C(r"$\begin{pmatrix} 1 \\ 1 \end{pmatrix}$", why="This is the eigenvector for $\\lambda = 5$: the matrix maps it to $(5, 5)$."),
            C(r"$\begin{pmatrix} 1 \\ 2 \end{pmatrix}$", why=r"The matrix maps this to $(6, 8)$, which is not a multiple of $(1, 2)$."),
            C(r"$\begin{pmatrix} 2 \\ 1 \end{pmatrix}$", why=r"The matrix maps this to $(9, 7)$, not a multiple of $(2, 1)$."),
            C(r"$\begin{pmatrix} 1 \\ -2 \end{pmatrix}$", correct=True),
        ], steps=[S("Equation", math=r"(\mathbf{A} - 2\mathbf{I})\mathbf{v} = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix}\mathbf{v} = \mathbf{0} \Rightarrow y = -2x"), S("Check", math=r"\mathbf{A}\begin{pmatrix} 1 \\ -2 \end{pmatrix} = \begin{pmatrix} 2 \\ -4 \end{pmatrix}")],
           concept="Finding an eigenvector", skill="Calculation", hint="Solve (A − 2I)v = 0, or multiply each option by A and compare.",
           feedback="A(1, −2) = (2, −4) = 2(1, −2)."),
        NUM(r"$\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ is an eigenvector of $\begin{pmatrix} k & 2 \\ 3 & 1 \end{pmatrix}$. Find $k$.", 2,
            steps=[S("Multiply", math=r"\begin{pmatrix} k + 2 \\ 4 \end{pmatrix} = \lambda\begin{pmatrix} 1 \\ 1 \end{pmatrix}"), S("Solve", math=r"\lambda = 4,\quad k + 2 = 4 \Rightarrow k = 2")],
            concept="Eigenvector with a parameter", skill="Application", hint="Both components of the product must be equal to λ.",
            feedback="The second component gives λ = 4, then k = 2."),
        MC(r"The eigenvalues of $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & -1 \end{pmatrix}$ are", [
            C(r"$2, 3, -1$", correct=True),
            C(r"$5, 1, 4$", why="These are the off-diagonal entries."),
            C(r"$2, 3, 1$", why="The last diagonal entry is $-1$, not $1$."),
            C(r"$0, 0, 0$", why="The zeros are the entries below the diagonal. The eigenvalues of a triangular matrix are its diagonal entries."),
        ], steps=[S("Characteristic polynomial of a triangular matrix", math=r"(2 - \lambda)(3 - \lambda)(-1 - \lambda) = 0")],
           concept="Eigenvalues of a triangular matrix", skill="Concept", hint="Expand det(A − λI) for a triangular matrix.",
           feedback="The eigenvalues of a triangular matrix are the diagonal entries."),
        MC(r"A $2\times2$ matrix $\mathbf{A}$ has eigenvalues $2$ and $5$. The eigenvalues of $\mathbf{A}^2$ are", [
            C(r"$4$ and $10$", why=r"Only the first eigenvalue has been squared. Both must be squared: $2^2$ and $5^2$."),
            C(r"$4$ and $25$", correct=True),
            C(r"$7$ and $10$", why="These are the trace and determinant of $\\mathbf{A}$."),
            C(r"$2$ and $5$", why=r"The eigenvalues change: $\mathbf{A}^2\mathbf{v} = \lambda^2\mathbf{v}$."),
        ], steps=[S("Apply twice", math=r"\mathbf{A}^2\mathbf{v} = \mathbf{A}(\lambda\mathbf{v}) = \lambda^2\mathbf{v}")],
           concept="Eigenvalues of powers", skill="Reasoning", hint="Apply A twice to an eigenvector.",
           feedback="The eigenvalues of A² are the squares."),
        MC(r"For $\mathbf{S} = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$, which vector is an eigenvector with eigenvalue $1$?", [
            C(r"$\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$", why="This is the eigenvector for eigenvalue $4$: $\\mathbf{S}\\mathbf{v} = (4, 4, 4)$."),
            C(r"$\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$", why=r"$\mathbf{S}\mathbf{v} = (3, 3, 2)$, not a multiple of $(1, 1, 0)$."),
            C(r"$\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$", correct=True),
            C(r"$\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$", why=r"$\mathbf{S}\mathbf{v} = (7, 8, 9)$, not a multiple of $(1, 2, 3)$."),
        ], steps=[S("Multiply", math=r"\mathbf{S}\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 - 1 \\ 1 - 2 \\ 1 - 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}")],
           concept="Repeated eigenvalue", skill="Calculation", hint="Multiply S by each option and see which is mapped to itself.",
           feedback="S(1, −1, 0) = (1, −1, 0), an eigenvalue of 1."),
    ]))

# ------------------------------------------------------------------ Diagonalization
SETS.append(practice_set(
    module=M3, topic="Diagonalization",
    title="Diagonalizing a matrix and finding its powers", lesson="fml1-diagonalization",
    questions=[
        MC(r"If $\mathbf{A}$ can be diagonalized, which equation is correct?", [
            C(r"$\mathbf{A} = \mathbf{P}^{-1}\mathbf{D}\mathbf{P}$", why=r"The order is reversed. Check with $\mathbf{A}\mathbf{P} = \mathbf{P}\mathbf{D}$, which gives $\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$."),
            C(r"$\mathbf{A} = \mathbf{D}\mathbf{P}\mathbf{D}^{-1}$", why="The matrix $\\mathbf{P}$ of eigenvectors must be on the outside."),
            C(r"$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}$", correct=True),
            C(r"$\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}$", why="The inverse of $\\mathbf{P}$ is needed on the right."),
        ], steps=[S("Each eigenvector", math=r"\mathbf{A}\mathbf{v}_i = \lambda_i\mathbf{v}_i \Rightarrow \mathbf{A}\mathbf{P} = \mathbf{P}\mathbf{D}"), S("Multiply by $\\mathbf{P}^{-1}$ on the right", math=r"\mathbf{A} = \mathbf{P}\mathbf{D}\mathbf{P}^{-1}")],
           concept="Diagonalization formula", skill="Recall", hint="Start from AP = PD.",
           feedback="A = P D P⁻¹."),
        NUM(r"For $\mathbf{A} = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$, use $\mathbf{A}^n = \frac13\begin{pmatrix} 2\cdot5^n + 2^n & 5^n - 2^n \\ 2\cdot5^n - 2\cdot2^n & 5^n + 2\cdot2^n \end{pmatrix}$ to find the top-left entry of $\mathbf{A}^3$.", 86,
            steps=[S("Substitute $n = 3$", math=r"\frac{2(125) + 8}{3} = \frac{258}{3} = 86")],
            concept="Using a matrix power formula", skill="Calculation", hint="Put n = 3 into the top-left entry.",
            feedback="A³ = [[86, 39], [78, 47]]."),
        MC(r"A matrix has eigenvalues $3$ and $-1$. In $\mathbf{A}^5 = \mathbf{P}\mathbf{D}^5\mathbf{P}^{-1}$, the matrix $\mathbf{D}^5$ is", [
            C(r"$\begin{pmatrix} 15 & 0 \\ 0 & -5 \end{pmatrix}$", why="This multiplies by 5. A power means repeated multiplication."),
            C(r"$\begin{pmatrix} 243 & 0 \\ 0 & -1 \end{pmatrix}$", correct=True),
            C(r"$\begin{pmatrix} 243 & 0 \\ 0 & 1 \end{pmatrix}$", why=r"$(-1)^5 = -1$ because the power is odd."),
            C(r"$\begin{pmatrix} 3 & 0 \\ 0 & -1 \end{pmatrix}^{5}$ cannot be simplified", why="A diagonal matrix is raised to a power entry by entry."),
        ], steps=[S("Raise each diagonal entry to the 5th power", math=r"3^5 = 243,\quad (-1)^5 = -1")],
           concept="Powers of a diagonal matrix", skill="Calculation", hint="Raise each diagonal entry to the power 5.",
           feedback="D⁵ = diag(243, −1)."),
        MC(r"Which of these matrices cannot be diagonalized?", [
            C(r"$\begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$", why="It has two distinct eigenvalues, $2$ and $5$, so it can be diagonalized."),
            C(r"$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$", why="It is already diagonal, so it is trivially diagonalizable."),
            C(r"$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$", correct=True),
            C(r"$\begin{pmatrix} 1 & 2 \\ 3 & 2 \end{pmatrix}$", why="It has eigenvalues $4$ and $-1$, which are distinct."),
        ], steps=[S("The matrix with a repeated eigenvalue", math=r"(1 - \lambda)^2 = 0 \Rightarrow \lambda = 1"), S("Only one independent eigenvector", text="Every eigenvector is a multiple of (1, 0), so P cannot be invertible.")],
           concept="When diagonalization fails", skill="Reasoning", hint="Look for a repeated eigenvalue with too few eigenvectors.",
           feedback="[[1, 1], [0, 1]] has a single eigenvector direction."),
        NUM(r"$\mathbf{B}$ has eigenvalues $1$, $2$, $3$. Find the trace of $\mathbf{B}^4$ (the sum of its diagonal entries).", 98,
            steps=[S("Eigenvalues of $\\mathbf{B}^4$", math=r"1^4,\ 2^4,\ 3^4 = 1,\ 16,\ 81"), S("Trace = sum of eigenvalues", math=r"1 + 16 + 81 = 98")],
            concept="Trace and powers", skill="Application", hint="The trace of a matrix is the sum of its eigenvalues.",
            feedback="The eigenvalues of B⁴ are 1, 16, 81."),
        MC(r"For $\mathbf{A} = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$ with eigenvectors $\begin{pmatrix} 1 \\ -2 \end{pmatrix}$ (eigenvalue $2$) and $\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ (eigenvalue $5$), which pair $\mathbf{P}$, $\mathbf{D}$ is correct?", [
            C(r"$\mathbf{P} = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$, $\mathbf{D} = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$", why="The columns of $\\mathbf{P}$ are in the order $(1,1), (1,-2)$ but $\\mathbf{D}$ lists $2$ first: the order does not match."),
            C(r"$\mathbf{P} = \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix}$, $\mathbf{D} = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$", correct=True),
            C(r"$\mathbf{P} = \begin{pmatrix} 1 & 1 \\ -2 & 1 \end{pmatrix}$, $\mathbf{D} = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}$", why="The first column of $\\mathbf{P}$ belongs to eigenvalue $2$, but $\\mathbf{D}$ has $5$ first."),
            C(r"$\mathbf{P} = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}$, $\mathbf{D} = \begin{pmatrix} 7 & 0 \\ 0 & 10 \end{pmatrix}$", why="The diagonal of $\\mathbf{D}$ must be the eigenvalues, not the trace and determinant."),
        ], steps=[S("Match the order", text=r"First column $(1, -2)$ with first entry $2$; second column $(1, 1)$ with second entry $5$."), S("Check", math=r"\mathbf{A}\mathbf{P} = \begin{pmatrix} 2 & 5 \\ -4 & 5 \end{pmatrix} = \mathbf{P}\mathbf{D}")],
           concept="Matching P and D", skill="Application", hint="Each column of P goes with the diagonal entry in the same position.",
           feedback="The columns of P and the entries of D must be in the same order."),
        NUM(r"In the stall model $\mathbf{M}^n \to \frac13\begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix}$. Starting from any shares with $x + y = 1$, what fraction of the customers is at stall $X$ in the long run? Give a decimal to 3 places.", 0.667, tolerance=0.002,
            steps=[S("Multiply", math=r"x_\infty = \tfrac13(2x + 2y) = \tfrac23(x + y) = \tfrac23")],
            concept="Long-run behaviour", skill="Interpretation", hint="Multiply the limiting matrix by (x, y) and use x + y = 1.",
            feedback="The long-run share is 2/3, whatever the start."),
        MC(r"For $\mathbf{A} = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$, $\mathbf{A}^2 - 7\mathbf{A} + 10\mathbf{I} = \mathbf{0}$. Therefore $\mathbf{A}^{-1}$ is", [
            C(r"$\dfrac{1}{10}\begin{pmatrix} 3 & -1 \\ -2 & 4 \end{pmatrix}$", correct=True),
            C(r"$\dfrac{1}{10}\begin{pmatrix} 11 & 1 \\ 2 & 10 \end{pmatrix}$", why=r"This is $\frac{1}{10}(7\mathbf{I} + \mathbf{A})$. The sign of $\mathbf{A}$ must be negative."),
            C(r"$\dfrac{1}{7}\begin{pmatrix} 3 & -1 \\ -2 & 4 \end{pmatrix}$", why="The divisor is the constant term $10$, which is the determinant, not $7$."),
            C(r"$\begin{pmatrix} \frac14 & 1 \\ \frac12 & \frac13 \end{pmatrix}$", why="Taking the reciprocal of each entry does not give the inverse matrix."),
        ], steps=[S("Rearrange", math=r"\mathbf{A}(7\mathbf{I} - \mathbf{A}) = 10\mathbf{I}"), S("Inverse", math=r"\mathbf{A}^{-1} = \tfrac{1}{10}(7\mathbf{I} - \mathbf{A}) = \tfrac{1}{10}\begin{pmatrix} 3 & -1 \\ -2 & 4 \end{pmatrix}")],
           concept="Inverse from the characteristic equation", skill="Reasoning", hint="Rearrange A² − 7A = −10I so that A appears as a factor on one side.",
           feedback="A(7I − A) = 10I, so A⁻¹ = (7I − A)/10."),
    ]))

# ------------------------------------------------------------------ Spread the correct option over A-D
# The platform does not shuffle options, so the correct choice is moved to a rotating position (A, B, C, D in turn).
_TARGETS = [2, 0, 3, 1]


def _spread_correct_options(sets):
    n = 0
    for s in sets:
        for q in s["questions"]:
            if q["kind"] != "choice":
                continue
            target = _TARGETS[n % len(_TARGETS)]
            n += 1
            ci = next(i for i, c in enumerate(q["choices"]) if c["correct"])
            q["choices"][ci], q["choices"][target] = q["choices"][target], q["choices"][ci]


_spread_correct_options(SETS)

