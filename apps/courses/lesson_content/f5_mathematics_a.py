"""Form 5 General Mathematics (O Level): sets and logic, commercial maths and variation,
quadratics, sequences and series. Draft content: check against the official syllabus."""

from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

LESSONS = [
    # ------------------------------------------------------------------ Set Theory & Logic
    lesson(
        module="Set Theory & Logic",
        topic="Venn diagrams",
        title="Venn diagrams with two and three sets",
        slug="venn-diagrams-two-and-three-sets",
        minutes=25,
        summary="Use two- and three-set Venn diagrams to count elements, solve problems with an unknown, and apply the laws of set algebra.",
        objectives=[
            "Use the notation for union, intersection and complement",
            "Fill in a two-set or three-set Venn diagram from given information",
            "Solve problems where one region is unknown",
            "Apply the laws of set algebra, including De Morgan's laws",
        ],
        key_concepts=["Universal set", "Union", "Intersection", "Complement", "Venn diagram", "De Morgan's laws"],
        blocks=[
            H("Introduction"),
            T("A school in Bamenda wants to know how many students belong to the Maths Club, the French Club, both, or neither. "
              "A **Venn diagram** answers questions like this quickly. It shows groups as circles inside a rectangle."),
            T("In this lesson you will fill in Venn diagrams for two and three sets, and use them to solve problems."),
            D(r"The **universal set** $\xi$ contains every element being considered. It is drawn as a rectangle. "
              r"Each set is a circle inside it. $n(A)$ means the number of elements in set $A$.",
              title="Definition: universal set"),
            KEY("Set notation", "Learn these four symbols. They appear in almost every question.", cards=[
                [r"Union $A \cup B$", "Elements in $A$, or in $B$, or in both."],
                [r"Intersection $A \cap B$", "Elements in both $A$ and $B$."],
                [r"Complement $A'$", r"Elements in $\xi$ that are **not** in $A$."],
                [r"Number $n(A)$", "How many elements are in $A$."],
            ]),
            F(r"n(A \cup B) = n(A) + n(B) - n(A \cap B)", title="Counting rule for two sets"),
            T("We subtract $n(A \\cap B)$ because the elements in the overlap were counted twice: once in $A$ and once in $B$."),
            EX("Worked example 1: two sets", intro=(
                "In a class of 40 students, 25 are in the Maths Club (M), 18 are in the French Club (F) and 7 are in both. "
                "How many students are in neither club?"), steps=[
                S("Start with the overlap", text="Write 7 in the region where the circles cross."),
                S("Find 'M only'", math=r"25 - 7 = 18"),
                S("Find 'F only'", math=r"18 - 7 = 11"),
                S("Add the regions inside the circles", math=r"18 + 7 + 11 = 36"),
                S("Subtract from the total", math=r"40 - 36 = 4 \text{ students in neither club}"),
            ], check=r"18 + 7 + 11 + 4 = 40"),
            IMG('f5-venn-two-sets.svg', 'Venn diagram in a rectangle labelled xi = 40, with two overlapping circles: Maths Club (M) and French Club (F). M only is 18, the overlap is 7, F only is 11 and 4 are outside both circles.',
                'Figure 1. Worked example 1: 18 + 7 + 11 + 4 = 40.'),
            TIP("Always fill a Venn diagram **from the middle outwards**. Write the intersection first, then the 'only' regions."),
            EX("Worked example 2: an unknown region", intro=(
                "30 students were asked about sport. 18 play football, 15 play basketball and 2 play neither. "
                "Let $x$ be the number who play both. Find $x$."), steps=[
                S("Write each region in terms of $x$", text="Both: $x$. Football only: $18 - x$. Basketball only: $15 - x$. Neither: 2."),
                S("The regions add up to the total", math=r"(18 - x) + x + (15 - x) + 2 = 30"),
                S("Simplify", math=r"35 - x = 30"),
                S("Solve", math=r"x = 5"),
            ], check=r"13 + 5 + 10 + 2 = 30"),
            IMG('f5-venn-unknown-region.svg', 'Venn diagram in a rectangle labelled xi = 30, with two overlapping circles: Football and Basketball. Football only is 18 minus x, the overlap is x, Basketball only is 15 minus x and 2 are outside both circles.',
                'Figure 2. Worked example 2: write every region in terms of x.'),
            H("Three-set Venn diagrams"),
            T("With three sets there are 8 regions: the centre (all three), three 'two only' regions, three 'one only' regions, and the outside."),
            EX("Worked example 3: three sets", intro=(
                "50 traders at Mokolo market were asked what they sell. 24 sell rice (R), 20 sell beans (B) and 18 sell oil (O). "
                "8 sell rice and beans, 6 sell beans and oil, 7 sell rice and oil, and 3 sell all three. "
                "How many sell rice only, and how many sell none of the three?"), steps=[
                S("Centre first", text="3 traders sell all three."),
                S("'Two only' regions", math=r"R \cap B \text{ only} = 8 - 3 = 5,\quad B \cap O \text{ only} = 6 - 3 = 3,\quad R \cap O \text{ only} = 7 - 3 = 4"),
                S("Rice only", math=r"24 - 5 - 4 - 3 = 12"),
                S("Beans only and oil only", math=r"20 - 5 - 3 - 3 = 9,\qquad 18 - 4 - 3 - 3 = 8"),
                S("Total inside the circles", math=r"12 + 9 + 8 + 5 + 3 + 4 + 3 = 44"),
                S("None of the three", math=r"50 - 44 = 6", text="12 sell rice only and 6 sell none."),
            ]),
            IMG('f5-venn-three-sets.svg', 'Three-set Venn diagram in a rectangle labelled xi = 50, with circles Rice (R), Beans (B) and Oil (O). Rice only 12, beans only 9, oil only 8, rice and beans only 5, beans and oil only 3, rice and oil only 4, all three 3, and 6 outside all circles.',
                'Figure 3. Worked example 3: fill from the centre outwards; 6 traders sell none of the three.'),
            H("Laws of set algebra"),
            KEY("Laws you should know", "Each law can be checked by shading a Venn diagram.", cards=[
                ["Commutative", r"$A \cup B = B \cup A$ and $A \cap B = B \cap A$"],
                ["Associative", r"$(A \cup B) \cup C = A \cup (B \cup C)$"],
                ["Distributive", r"$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$"],
                ["De Morgan", r"$(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$"],
            ]),
            H("Common mistakes"),
            MISTAKE("Writing the given totals straight into the 'only' regions",
                    "If 25 students are in M, the number 25 is the **whole circle**, not 'M only'. Subtract the overlap first."),
            MISTAKE("Forgetting the elements outside all circles",
                    "The regions inside the circles may not add up to $n(\\xi)$. The rest go outside the circles."),
            MISTAKE("Mixing up union and intersection",
                    "$\\cup$ means 'or' (everything in either set). $\\cap$ means 'and' (only the overlap)."),
            QUIZ(r"$n(A) = 12$, $n(B) = 9$ and $n(A \cap B) = 4$. What is $n(A \cup B)$?",
                 ["21", "17", "25", "13"], 1,
                 r"$n(A \cup B) = 12 + 9 - 4 = 17$.",
                 hint="Add the two sets, then remove the overlap that was counted twice.",
                 feedback=["You added 12 and 9 but did not subtract the overlap.", "",
                           "You added the overlap instead of subtracting it.", "You subtracted the overlap twice."]),
            H("Practice questions"),
            PQ(r"$\xi = \{1, 2, 3, \dots, 10\}$, $A = \{\text{even numbers}\}$ and $B = \{\text{multiples of } 3\}$. "
               r"List (a) $A \cap B$, (b) $A \cup B$, (c) $(A \cup B)'$.",
               r"$A = \{2, 4, 6, 8, 10\}$ and $B = \{3, 6, 9\}$. "
               r"(a) $A \cap B = \{6\}$. (b) $A \cup B = \{2, 3, 4, 6, 8, 9, 10\}$. (c) $(A \cup B)' = \{1, 5, 7\}$."),
            PQ("In a group of 100 students, 40 study Physics, 42 study Chemistry and 48 study Biology. "
               "15 study Physics and Chemistry, 18 study Chemistry and Biology, 12 study Physics and Biology, "
               "and 10 study none of the three. $x$ students study all three. (a) Find $x$. (b) How many study exactly one subject?",
               r"(a) Inside the circles there are $100 - 10 = 90$ students. "
               r"Using the regions: $40 + 42 + 48 - 15 - 18 - 12 + x = 90$, so $85 + x = 90$ and $x = 5$. "
               r"(b) Physics only $= 40 - 15 - 12 + 5 = 18$. Chemistry only $= 42 - 15 - 18 + 5 = 14$. "
               r"Biology only $= 48 - 18 - 12 + 5 = 23$. Exactly one subject: $18 + 14 + 23 = 55$."),
            PQ(r"$\xi = \{1, 2, \dots, 8\}$, $A = \{1, 2, 3, 4\}$ and $B = \{3, 4, 5, 6\}$. Show that $(A \cup B)' = A' \cap B'$.",
               r"$A \cup B = \{1, 2, 3, 4, 5, 6\}$, so $(A \cup B)' = \{7, 8\}$. "
               r"$A' = \{5, 6, 7, 8\}$ and $B' = \{1, 2, 7, 8\}$, so $A' \cap B' = \{7, 8\}$. Both sides equal $\{7, 8\}$."),
            H("Summary"),
            SUM(r"$\cup$ is 'or', $\cap$ is 'and', and $A'$ is everything not in $A$.",
                r"For two sets: $n(A \cup B) = n(A) + n(B) - n(A \cap B)$.",
                "Fill a Venn diagram from the centre outwards, then the outside region last.",
                "When a region is unknown, call it $x$ and make all the regions add up to the total.",
                r"De Morgan's laws: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$."),
        ],
    ),
    lesson(
        module="Set Theory & Logic",
        topic="Logic",
        title="Statements, truth values and logical deductions",
        slug="logic-statements-truth-values-deductions",
        minutes=25,
        summary="Find the truth value of simple and compound statements, build truth tables, and decide whether a deduction is valid.",
        objectives=[
            "Recognise a statement and give its truth value",
            "Use negation, 'and', 'or' and 'if ... then' to form compound statements",
            "Complete truth tables for compound statements",
            "Decide whether a logical deduction is valid",
        ],
        key_concepts=["Statement", "Truth value", "Negation", "Conjunction", "Disjunction", "Implication", "Contrapositive", "Valid deduction"],
        blocks=[
            H("Introduction"),
            T("Every day we reason like this: \"If it rains, the road to Kumba is muddy. It is raining. So the road is muddy.\" "
              "Logic studies which arguments like this are correct and which are not."),
            T("In mathematics we use symbols to make this reasoning short and exact."),
            D("A **statement** is a sentence that is either true or false, but not both. "
              "Its **truth value** is T (true) or F (false).", title="Definition: statement",
              note="\"Close the door\" and \"Is it hot?\" are not statements, because they are neither true nor false."),
            KEY("Joining statements", "Let $p$ and $q$ be statements.", cards=[
                [r"Negation $\sim p$", "\"not $p$\". True when $p$ is false."],
                [r"Conjunction $p \wedge q$", "\"$p$ and $q$\". True only when **both** are true."],
                [r"Disjunction $p \vee q$", "\"$p$ or $q$\". True when **at least one** is true."],
                [r"Implication $p \Rightarrow q$", "\"If $p$ then $q$\". False only when $p$ is true and $q$ is false."],
            ]),
            H("Truth tables"),
            T("A truth table lists every possible combination of truth values. With two statements there are 4 rows: TT, TF, FT, FF."),
            T(r"For $p \wedge q$ the column reads T, F, F, F. For $p \vee q$ it reads T, T, T, F. "
              r"For $p \Rightarrow q$ it reads T, F, T, T."),
            TIP(r"Remember $p \Rightarrow q$ as a promise: “If you pass, I will give you 5 000 FCFA.” "
                "The promise is only broken if you pass and you do not get the money."),
            EX("Worked example 1: truth values", intro=(
                r"Let $p$: “Douala is a town in Cameroon” and $q$: “5 is an even number”. "
                r"Find the truth values of $\sim q$, $p \wedge q$, $p \vee q$ and $p \Rightarrow q$."), steps=[
                S("Truth values of the simple statements", text="$p$ is true (T). $q$ is false (F)."),
                S("Negation", math=r"\sim q \text{ is T}"),
                S("Conjunction needs both true", math=r"p \wedge q \text{ is F}"),
                S("Disjunction needs at least one true", math=r"p \vee q \text{ is T}"),
                S("Implication with T then F", math=r"p \Rightarrow q \text{ is F}"),
            ]),
            EX("Worked example 2: a truth table", intro=r"Complete a truth table for $\sim p \vee q$ and compare it with $p \Rightarrow q$.", steps=[
                S("List the rows for $p$ and $q$", text="$p$: T, T, F, F. $q$: T, F, T, F."),
                S("Negate $p$", text=r"$\sim p$: F, F, T, T."),
                S("'Or' is true if at least one is true", text=r"$\sim p \vee q$: T, F, T, T."),
                S("Compare", text=r"$p \Rightarrow q$ is also T, F, T, T. The two statements are **equivalent**."),
            ]),
            H("Converse and contrapositive"),
            D(r"For the implication $p \Rightarrow q$: the **converse** is $q \Rightarrow p$, and the **contrapositive** is $\sim q \Rightarrow \sim p$.",
              title="Definition", note="An implication and its contrapositive always have the same truth value. The converse may not."),
            T("Example: \"If a number is divisible by 4, then it is even\" is true. "
              "Its converse, \"If a number is even, then it is divisible by 4\", is false: 6 is even but not divisible by 4."),
            H("Valid deductions"),
            T(r"A deduction is **valid** if the conclusion must be true whenever the premises are true. "
              r"Two valid patterns: from $p \Rightarrow q$ and $p$, conclude $q$. From $p \Rightarrow q$ and $\sim q$, conclude $\sim p$."),
            EX("Worked example 3: is the deduction valid?", intro=(
                "Premise 1: If it rains, the road to Kumba is muddy. Premise 2: The road to Kumba is muddy. "
                "Conclusion: It rained. Is this valid?"), steps=[
                S("Write it in symbols", text=r"$p$: it rains. $q$: the road is muddy. We have $p \Rightarrow q$ and $q$."),
                S("Look for a case where premises are true but the conclusion is false",
                  text="The road could be muddy because a water pipe burst, with no rain."),
                S("Decide", text="The premises can be true while the conclusion is false. The deduction is **not valid**."),
            ]),
            H("Common mistakes"),
            MISTAKE("Thinking an implication is false when $p$ is false",
                    r"If $p$ is false, $p \Rightarrow q$ is **true**, whatever $q$ is. Only T $\Rightarrow$ F is false."),
            MISTAKE("Confusing the converse with the contrapositive",
                    r"The contrapositive swaps **and** negates: $\sim q \Rightarrow \sim p$. The converse only swaps: $q \Rightarrow p$."),
            MISTAKE("Reasoning backwards from the conclusion",
                    r"Knowing $p \Rightarrow q$ and $q$ does **not** let you conclude $p$, as in worked example 3."),
            QUIZ("What is the contrapositive of \"If a number is divisible by 4, then it is even\"?",
                 ["If a number is even, then it is divisible by 4.",
                  "If a number is not even, then it is not divisible by 4.",
                  "If a number is not divisible by 4, then it is not even.",
                  "A number is divisible by 4 and it is not even."], 1,
                 r"The contrapositive of $p \Rightarrow q$ is $\sim q \Rightarrow \sim p$: swap the parts and negate both.",
                 feedback=["This is the converse: the parts are swapped but not negated.", "",
                           "This is the inverse: the parts are negated but not swapped.",
                           r"This is the negation of the implication ($p \wedge \sim q$), not its contrapositive."]),
            H("Practice questions"),
            PQ(r"$p$ is true, $q$ is false and $r$ is true. Find the truth value of (a) $(p \wedge q) \Rightarrow r$ (b) $\sim(p \vee q) \wedge r$.",
               r"(a) $p \wedge q$ is F. F $\Rightarrow$ T is **T**. "
               r"(b) $p \vee q$ is T, so $\sim(p \vee q)$ is F. F $\wedge$ T is **F**."),
            PQ(r"Copy and complete a truth table for $p \wedge \sim q$.",
               r"$p$: T, T, F, F. $q$: T, F, T, F. $\sim q$: F, T, F, T. $p \wedge \sim q$: F, T, F, F. "
               r"It is true only when $p$ is true and $q$ is false."),
            PQ("Premise 1: All Form 5 students write the GCE. Premise 2: Ngozi is a Form 5 student. "
               "(a) What can you conclude? (b) If instead Premise 2 were \"Ngozi writes the GCE\", could you conclude that Ngozi is a Form 5 student?",
               "(a) Ngozi writes the GCE. This is valid. "
               "(b) No. Other people, for example private candidates, may also write the GCE. "
               "From $p \\Rightarrow q$ and $q$ we cannot conclude $p$."),
            PQ(r"Show that “If $x = 3$, then $x^2 = 9$” is true, but its converse is false.",
               r"If $x = 3$ then $x^2 = 9$, so the statement is true. "
               r"The converse is “If $x^2 = 9$, then $x = 3$”. It is false, because $x = -3$ also gives $x^2 = 9$."),
            H("Summary"),
            SUM("A statement is either true or false, never both.",
                r"$p \wedge q$ needs both true. $p \vee q$ needs at least one true.",
                r"$p \Rightarrow q$ is false only when $p$ is true and $q$ is false.",
                r"An implication and its contrapositive $\sim q \Rightarrow \sim p$ always agree; the converse may not.",
                "A deduction is valid only if the conclusion must follow whenever the premises are true."),
        ],
    ),
    # ---------------------------------------------- Commercial Mathematics & Variation
    lesson(
        module="Commercial Mathematics & Variation",
        topic="Commercial arithmetic",
        title="Compound interest, depreciation, hire purchase and taxes",
        slug="compound-interest-depreciation-hire-purchase-taxes",
        minutes=30,
        summary="Calculate compound interest and depreciation with the multiplier method, compare hire purchase with cash prices, and work out taxes.",
        objectives=[
            "Calculate compound interest using a multiplier",
            "Calculate the value of an item after depreciation",
            "Find the total cost and extra cost of hire purchase",
            "Calculate income tax and sales tax from a given rate",
        ],
        key_concepts=["Compound interest", "Principal", "Depreciation", "Hire purchase", "Deposit", "Income tax", "Sales tax"],
        blocks=[
            H("Introduction"),
            T("Money changes value over time. Savings in a bank or a njangi grow. A motorbike bought in Bafoussam loses value as it gets older. "
              "A trader may buy a fridge on credit and pay more than the cash price."),
            T("This lesson covers four everyday money calculations. All prices are in FCFA."),
            H("Compound interest"),
            D("With **compound interest**, the interest earned each year is added to the money. "
              "Next year, interest is paid on this larger amount. The starting amount is the **principal** $P$.",
              title="Definition: compound interest",
              formula=r"A = P\left(1 + \frac{r}{100}\right)^n",
              note="$A$ is the amount after $n$ years at $r\\%$ per year. Interest $= A - P$."),
            EX("Worked example 1: compound interest", intro=(
                "A teacher in Buea saves 500 000 FCFA in a bank at 8% per year compound interest. "
                "Find the amount after 3 years and the interest earned."), steps=[
                S("Write the multiplier", math=r"1 + \frac{8}{100} = 1.08"),
                S("Multiply once for each year", math=r"A = 500\,000 \times 1.08^3"),
                S("Calculate", math=r"1.08^3 = 1.259712, \quad A = 629\,856 \text{ FCFA}"),
                S("Find the interest", math=r"629\,856 - 500\,000 = 129\,856 \text{ FCFA}"),
            ], check=r"\text{Year by year: } 540\,000 \to 583\,200 \to 629\,856"),
            H("Depreciation"),
            D("**Depreciation** is the loss in value of an item over time. When the value falls by $r\\%$ each year, "
              "we multiply by $\\left(1 - \\frac{r}{100}\\right)$ each year.",
              title="Definition: depreciation", formula=r"V = P\left(1 - \frac{r}{100}\right)^n"),
            EX("Worked example 2: depreciation", intro=(
                "A motorbike costs 1 200 000 FCFA. It depreciates by 15% each year. Find its value after 2 years."), steps=[
                S("Write the multiplier", math=r"1 - \frac{15}{100} = 0.85"),
                S("Multiply once for each year", math=r"V = 1\,200\,000 \times 0.85^2"),
                S("Calculate", math=r"V = 1\,200\,000 \times 0.7225 = 867\,000 \text{ FCFA}"),
            ], check=r"1\,200\,000 \to 1\,020\,000 \to 867\,000"),
            QUIZ("A phone worth 100 000 FCFA depreciates by 10% each year. What is it worth after 2 years?",
                 ["80 000 FCFA", "81 000 FCFA", "90 000 FCFA", "121 000 FCFA"], 1,
                 r"$100\,000 \times 0.9^2 = 100\,000 \times 0.81 = 81\,000$ FCFA.",
                 hint="Multiply by 0.9 once for each year.",
                 feedback=["You took 10% of the original price twice. Each year's 10% is taken from the new, lower value.", "",
                           "This is the value after only 1 year.", "You increased the value. Depreciation makes it smaller."]),
            H("Hire purchase"),
            D("With **hire purchase** (HP), you pay a **deposit** first, then a number of equal instalments. "
              "The total HP price is usually more than the cash price.", title="Definition: hire purchase",
              formula=r"\text{HP price} = \text{deposit} + (\text{number of instalments} \times \text{instalment})"),
            EX("Worked example 3: hire purchase", intro=(
                "A television has a cash price of 250 000 FCFA. On hire purchase, the buyer pays a deposit of 20% of the cash price "
                "and 12 monthly instalments of 18 500 FCFA. How much more does hire purchase cost?"), steps=[
                S("Deposit", math=r"20\% \times 250\,000 = 50\,000"),
                S("Total of the instalments", math=r"12 \times 18\,500 = 222\,000"),
                S("HP price", math=r"50\,000 + 222\,000 = 272\,000 \text{ FCFA}"),
                S("Extra cost", math=r"272\,000 - 250\,000 = 22\,000 \text{ FCFA}"),
            ]),
            H("Taxes"),
            T("**Income tax** is paid on the part of income left after allowances are removed. This part is the **taxable income**. "
              "A **sales tax** is a percentage added to the price of goods. The rates used below are examples only."),
            EX("Worked example 4: income tax", intro=(
                "A worker earns 2 400 000 FCFA per year. Allowances of 600 000 FCFA are tax-free. "
                "The rest is taxed at 10%. Find the tax paid."), steps=[
                S("Taxable income", math=r"2\,400\,000 - 600\,000 = 1\,800\,000"),
                S("Tax", math=r"10\% \times 1\,800\,000 = 180\,000 \text{ FCFA}"),
            ]),
            H("Common mistakes"),
            MISTAKE("Using simple interest instead of compound interest",
                    r"$500\,000 \times 8\% \times 3 = 120\,000$ is simple interest. Compound interest grows each year, so use $1.08^3$."),
            MISTAKE("Giving the amount when the question asks for the interest",
                    "Read carefully. Interest is the amount **minus** the principal."),
            MISTAKE("Taxing the whole income", "Subtract the allowances first, then apply the tax rate."),
            H("Practice questions"),
            PQ("Find the compound interest on 200 000 FCFA at 5% per year for 2 years.",
               r"$A = 200\,000 \times 1.05^2 = 200\,000 \times 1.1025 = 220\,500$ FCFA. Interest $= 220\,500 - 200\,000 = 20\,500$ FCFA."),
            PQ("A car bought for 6 000 000 FCFA depreciates by 20% each year. Find its value after 3 years.",
               r"$V = 6\,000\,000 \times 0.8^3 = 6\,000\,000 \times 0.512 = 3\,072\,000$ FCFA."),
            PQ("A fridge has a cash price of 180 000 FCFA. On hire purchase it costs a deposit of 30 000 FCFA and 10 monthly payments of 17 000 FCFA. "
               "(a) Find the hire purchase price. (b) Express the extra cost as a percentage of the cash price, to 1 decimal place.",
               r"(a) $30\,000 + 10 \times 17\,000 = 30\,000 + 170\,000 = 200\,000$ FCFA. "
               r"(b) Extra cost $= 200\,000 - 180\,000 = 20\,000$. Percentage $= \frac{20\,000}{180\,000} \times 100 = 11.1\%$."),
            PQ("A shop adds a sales tax of 15% to its prices. A bag costs 40 000 FCFA before tax. Find the price including tax.",
               r"Tax $= 15\% \times 40\,000 = 6\,000$ FCFA. Price $= 40\,000 + 6\,000 = 46\,000$ FCFA. "
               r"Or in one step: $40\,000 \times 1.15 = 46\,000$ FCFA."),
            H("Summary"),
            SUM(r"Compound interest: $A = P\left(1 + \frac{r}{100}\right)^n$, and interest $= A - P$.",
                r"Depreciation: $V = P\left(1 - \frac{r}{100}\right)^n$.",
                "Hire purchase price = deposit + all the instalments. Compare it with the cash price.",
                "Income tax is charged on taxable income: income minus allowances.",
                "Sales tax is a percentage added to the price before tax."),
        ],
    ),
    lesson(
        module="Commercial Mathematics & Variation",
        topic="Variation",
        title="Direct, inverse, joint and partial variation",
        slug="direct-inverse-joint-partial-variation",
        minutes=25,
        summary="Write variation statements as equations, find the constant, and use it to calculate unknown values in direct, inverse, joint and partial variation.",
        objectives=[
            "Write a variation statement as an equation with a constant $k$",
            "Find $k$ from a given pair of values and use it to find unknowns",
            "Solve problems on joint variation",
            "Solve problems on partial variation using two pairs of values",
        ],
        key_concepts=["Direct variation", "Inverse variation", "Joint variation", "Partial variation", "Constant of variation"],
        blocks=[
            H("Introduction"),
            T("If one kilogram of tomatoes costs 600 FCFA, two kilograms cost 1 200 FCFA. The cost **varies directly** with the mass. "
              "But if more workers build a wall, it takes fewer days. The time **varies inversely** with the number of workers."),
            T("Variation turns sentences like these into equations that we can solve."),
            KEY("The four types of variation", "Each one uses a constant, $k$ (or $a$ and $b$ for partial variation).", cards=[
                ["Direct", r"$y \propto x$ means $y = kx$"],
                ["Inverse", r"$y \propto \frac{1}{x}$ means $y = \frac{k}{x}$"],
                ["Joint", r"$y$ varies jointly as $x$ and $z$: $y = kxz$"],
                ["Partial", r"$y$ is partly constant and partly varies as $x$: $y = a + bx$"],
            ]),
            D("The number $k$ is the **constant of variation**. Find it first, using the values given, then use it to answer the question.",
              title="Definition: constant of variation"),
            T("The same idea works with powers and roots. For example, $y \\propto x^2$ means $y = kx^2$, and $y \\propto \\sqrt{x}$ means $y = k\\sqrt{x}$."),
            EX("Worked example 1: direct variation", intro="$y$ varies directly as $x^2$. When $x = 2$, $y = 12$. Find $y$ when $x = 5$.", steps=[
                S("Write the equation", math=r"y = kx^2"),
                S("Substitute the given values", math=r"12 = k \times 2^2 = 4k"),
                S("Find $k$", math=r"k = 3, \text{ so } y = 3x^2"),
                S("Use the equation", math=r"y = 3 \times 5^2 = 75"),
            ]),
            EX("Worked example 2: inverse variation", intro=(
                "The time to build a wall in Ebolowa varies inversely as the number of workers. 6 workers take 10 days. How long would 4 workers take?"), steps=[
                S("Write the equation", math=r"t = \frac{k}{w}"),
                S("Substitute the given values", math=r"10 = \frac{k}{6}, \text{ so } k = 60"),
                S("Use the equation", math=r"t = \frac{60}{4} = 15 \text{ days}"),
            ], check=r"\text{Fewer workers, more days: } 15 > 10"),
            QUIZ(r"$y$ is inversely proportional to $x$. When $x = 3$, $y = 8$. What is $y$ when $x = 6$?",
                 ["16", "4", "24", "2"], 1,
                 r"$k = xy = 3 \times 8 = 24$, so $y = \frac{24}{6} = 4$.",
                 hint="For inverse variation, $x \\times y$ stays the same.",
                 feedback=["That is direct variation: doubling $x$ doubled $y$. In inverse variation, doubling $x$ halves $y$.", "",
                           "24 is the constant $k$, not the value of $y$.", "You divided by $x^2$. The question says inversely as $x$, not $x^2$."]),
            EX("Worked example 3: joint variation", intro="$z$ varies jointly as $x$ and $y$. When $x = 2$ and $y = 3$, $z = 24$. Find $z$ when $x = 5$ and $y = 1.5$.", steps=[
                S("Write the equation", math=r"z = kxy"),
                S("Find $k$", math=r"24 = k \times 2 \times 3 = 6k, \text{ so } k = 4"),
                S("Use the equation", math=r"z = 4 \times 5 \times 1.5 = 30"),
            ]),
            H("Partial variation"),
            T("In partial variation one part is fixed and one part varies. There are two unknown constants, so you need **two** pairs of values. "
              "This gives two simultaneous equations."),
            EX("Worked example 4: partial variation", intro=(
                "The cost $C$ of hiring a hall in Buea is partly constant and partly varies as the number of guests $n$. "
                "It costs 150 000 FCFA for 50 guests and 250 000 FCFA for 100 guests. Find the cost for 80 guests."), steps=[
                S("Write the equation", math=r"C = a + bn"),
                S("Form two equations", math=r"a + 50b = 150\,000 \qquad a + 100b = 250\,000"),
                S("Subtract the first from the second", math=r"50b = 100\,000, \text{ so } b = 2\,000"),
                S("Find $a$", math=r"a = 150\,000 - 50 \times 2\,000 = 50\,000"),
                S("Cost for 80 guests", math=r"C = 50\,000 + 2\,000 \times 80 = 210\,000 \text{ FCFA}"),
            ], check=r"50\,000 + 2\,000 \times 100 = 250\,000"),
            H("Common mistakes"),
            MISTAKE("Using the wrong form of equation",
                    r"Read the words carefully. 'Inversely as the square of $x$' means $y = \frac{k}{x^2}$, not $y = \frac{k}{x}$ or $y = kx^2$."),
            MISTAKE("Not finding $k$ first", "Always find the constant from the given pair of values before you calculate anything new."),
            MISTAKE("Treating partial variation as direct variation",
                    r"If $C = a + bn$, doubling $n$ does **not** double $C$, because of the fixed part $a$."),
            H("Practice questions"),
            PQ(r"$p$ varies directly as the square root of $q$. When $q = 9$, $p = 6$. Find (a) $p$ when $q = 25$ (b) $q$ when $p = 14$.",
               r"$p = k\sqrt{q}$. $6 = k \times 3$, so $k = 2$ and $p = 2\sqrt{q}$. "
               r"(a) $p = 2 \times 5 = 10$. (b) $14 = 2\sqrt{q}$, so $\sqrt{q} = 7$ and $q = 49$."),
            PQ(r"$y$ varies directly as $x$ and inversely as the square of $z$. When $x = 4$ and $z = 2$, $y = 9$. Find $y$ when $x = 6$ and $z = 3$.",
               r"$y = \frac{kx}{z^2}$. $9 = \frac{k \times 4}{4}$, so $k = 9$. Then $y = \frac{9 \times 6}{3^2} = \frac{54}{9} = 6$."),
            PQ("A taxi fare $F$ is partly constant and partly varies as the distance $d$ km. A 5 km trip costs 1 500 FCFA and a 10 km trip costs 2 500 FCFA. "
               "Find the fare for an 8 km trip.",
               r"$F = a + bd$. $a + 5b = 1\,500$ and $a + 10b = 2\,500$. Subtracting: $5b = 1\,000$, so $b = 200$ and $a = 500$. "
               r"For 8 km: $F = 500 + 200 \times 8 = 2\,100$ FCFA."),
            PQ(r"$y \propto x^2$. What happens to $y$ when $x$ is doubled?",
               r"$y = kx^2$. Replacing $x$ by $2x$ gives $k(2x)^2 = 4kx^2 = 4y$. So $y$ is multiplied by 4."),
            H("Summary"),
            SUM(r"Direct: $y = kx$. Inverse: $y = \frac{k}{x}$. Joint: $y = kxz$. Partial: $y = a + bx$.",
                "Powers and roots go inside the equation, for example $y = kx^2$ or $y = k\\sqrt{x}$.",
                "Find the constant first from the given values, then substitute the new values.",
                "Partial variation has two constants, so it needs two pairs of values and simultaneous equations."),
        ],
    ),
    # ------------------------------------------------- Quadratic Functions & Equations
    lesson(
        module="Quadratic Functions & Equations",
        topic="Solving quadratics",
        title="Three ways to solve a quadratic equation",
        slug="solving-quadratics-three-methods",
        minutes=30,
        summary="Solve quadratic equations by factorization, by completing the square and by the quadratic formula, and choose a sensible method.",
        objectives=[
            "Solve a quadratic equation by factorization",
            "Solve a quadratic equation by completing the square",
            "Solve a quadratic equation using the quadratic formula",
            "Form and solve a quadratic equation from a word problem",
        ],
        key_concepts=["Quadratic equation", "Root", "Factorization", "Completing the square", "Quadratic formula"],
        blocks=[
            H("Introduction"),
            T("A farmer in Bafoussam wants a rectangular plot of area 84 m², with the length 5 m more than the width. "
              "Writing this as an equation gives $x(x + 5) = 84$, which is a **quadratic equation**."),
            T("There are three standard methods to solve it. This lesson shows each one and when to use it."),
            D("A **quadratic equation** can be written as $ax^2 + bx + c = 0$ with $a \\neq 0$. "
              "Its solutions are called **roots**. A quadratic has at most two real roots.",
              title="Definition: quadratic equation", formula=r"ax^2 + bx + c = 0"),
            H("Method 1: factorization"),
            T("If $(x - p)(x - q) = 0$, then $x - p = 0$ or $x - q = 0$. So the roots are $p$ and $q$. "
              "This works because a product is zero only if one of its factors is zero."),
            EX("Worked example 1: factorization", solve=r"x^2 + x - 12 = 0", steps=[
                S("Find two numbers that multiply to $-12$ and add to $1$", text="They are $4$ and $-3$."),
                S("Factorize", math=r"(x + 4)(x - 3) = 0"),
                S("Set each bracket to zero", math=r"x + 4 = 0 \quad\text{or}\quad x - 3 = 0"),
                S("Solve", math=r"x = -4 \quad\text{or}\quad x = 3"),
            ], check=r"3^2 + 3 - 12 = 0 \text{ and } (-4)^2 - 4 - 12 = 0"),
            H("Method 2: completing the square"),
            T("Use this when the quadratic does not factorize neatly. The idea is to write the left side as a perfect square."),
            F(r"x^2 + bx = \left(x + \frac{b}{2}\right)^2 - \left(\frac{b}{2}\right)^2", title="Key identity"),
            EX("Worked example 2: completing the square", solve=r"x^2 - 6x + 4 = 0", steps=[
                S("Move the constant to the right", math=r"x^2 - 6x = -4"),
                S("Add $\\left(\\frac{-6}{2}\\right)^2 = 9$ to both sides", math=r"x^2 - 6x + 9 = 5"),
                S("Write the left side as a square", math=r"(x - 3)^2 = 5"),
                S("Take the square root, remembering $\\pm$", math=r"x - 3 = \pm\sqrt{5}"),
                S("Solve", math=r"x = 3 \pm \sqrt{5}, \text{ so } x = 5.24 \text{ or } x = 0.76 \text{ (2 d.p.)}"),
            ]),
            TIP("If $a$ is not 1, divide every term by $a$ first, then complete the square."),
            H("Method 3: the quadratic formula"),
            D("The formula works for **every** quadratic equation $ax^2 + bx + c = 0$.", title="The quadratic formula",
              formula=r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
              note="If $b^2 - 4ac$ is negative, there are no real roots."),
            EX("Worked example 3: the formula", solve=r"2x^2 - 3x - 4 = 0", steps=[
                S("Identify $a$, $b$ and $c$", math=r"a = 2,\quad b = -3,\quad c = -4"),
                S("Find $b^2 - 4ac$", math=r"(-3)^2 - 4(2)(-4) = 9 + 32 = 41"),
                S("Substitute", math=r"x = \frac{3 \pm \sqrt{41}}{4}"),
                S("Calculate each root", math=r"x = \frac{3 + 6.403}{4} = 2.35 \quad\text{or}\quad x = \frac{3 - 6.403}{4} = -0.85"),
            ]),
            QUIZ(r"For $3x^2 - 5x - 1 = 0$, what is the value of $b^2 - 4ac$?",
                 ["13", "37", "-13", "28"], 1,
                 r"$b^2 - 4ac = (-5)^2 - 4(3)(-1) = 25 + 12 = 37$.",
                 hint="Be careful with the signs: $c = -1$.",
                 feedback=["You used $c = +1$. Here $c = -1$, so $-4ac = +12$.", "",
                           r"$(-5)^2$ is $+25$, not $-25$.", "You found $ac = -3$ but forgot to multiply by 4. The term is $-4ac = +12$."]),
            EX("Worked example 4: a word problem", intro=(
                "A rectangular plot in Bafoussam has an area of 84 m². Its length is 5 m more than its width. Find the dimensions."), steps=[
                S("Let the width be $x$ m", text="Then the length is $(x + 5)$ m."),
                S("Form the equation", math=r"x(x + 5) = 84 \;\Rightarrow\; x^2 + 5x - 84 = 0"),
                S("Factorize", math=r"(x + 12)(x - 7) = 0"),
                S("Solve", math=r"x = -12 \text{ or } x = 7"),
                S("Reject the impossible root", text="A width cannot be negative. The width is 7 m and the length is 12 m."),
            ], check=r"7 \times 12 = 84"),
            H("Common mistakes"),
            MISTAKE("Not making one side zero", "From $x(x + 5) = 84$ you cannot say $x = 84$. Expand and rearrange to $x^2 + 5x - 84 = 0$ first."),
            MISTAKE("Forgetting the $\\pm$ sign", "When you square-root both sides, there are two answers: $+\\sqrt{5}$ and $-\\sqrt{5}$."),
            MISTAKE("Sign errors with $-b$", r"If $b = -3$, then $-b = +3$. Write $a$, $b$ and $c$ down with their signs before substituting."),
            H("Practice questions"),
            PQ(r"Solve $2x^2 - 5x - 3 = 0$ by factorization.",
               r"$ac = -6$. Two numbers that multiply to $-6$ and add to $-5$ are $-6$ and $1$. "
               r"$2x^2 - 6x + x - 3 = 2x(x - 3) + 1(x - 3) = (2x + 1)(x - 3) = 0$. So $x = 3$ or $x = -\frac{1}{2}$."),
            PQ(r"Solve $x^2 + 4x - 7 = 0$ by completing the square. Give your answers to 2 decimal places.",
               r"$x^2 + 4x = 7$. Add 4: $(x + 2)^2 = 11$. So $x = -2 \pm \sqrt{11}$, giving $x = 1.32$ or $x = -5.32$."),
            PQ(r"Use the formula to solve $3x^2 + 2x - 2 = 0$, giving your answers to 2 decimal places.",
               r"$a = 3$, $b = 2$, $c = -2$. $b^2 - 4ac = 4 + 24 = 28$. "
               r"$x = \frac{-2 \pm \sqrt{28}}{6} = \frac{-2 \pm 5.292}{6}$, so $x = 0.55$ or $x = -1.22$."),
            PQ(r"Express $x^2 - 8x + 3$ in the form $(x - p)^2 - q$.",
               r"Half of $-8$ is $-4$. $(x - 4)^2 = x^2 - 8x + 16$, so $x^2 - 8x + 3 = (x - 4)^2 - 13$. Here $p = 4$ and $q = 13$."),
            H("Summary"),
            SUM("Always rearrange the equation so one side is zero.",
                "Factorization is fastest when the quadratic factorizes neatly.",
                r"Completing the square: add $\left(\frac{b}{2}\right)^2$ to both sides, then square-root with $\pm$.",
                r"The formula $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ works for every quadratic.",
                "In word problems, reject roots that make no sense, such as a negative length."),
        ],
    ),
    lesson(
        module="Quadratic Functions & Equations",
        topic="Quadratic graphs",
        title="Reading roots and turning points from quadratic graphs",
        slug="quadratic-graphs-roots-turning-points",
        minutes=30,
        summary="Draw the graph of a quadratic function from a table of values and read its roots, turning point and line of symmetry, then use it to solve related equations.",
        objectives=[
            "Complete a table of values and draw the graph of a quadratic function",
            "Read the roots of a quadratic equation from its graph",
            "Find the turning point and the line of symmetry, and say whether it is a minimum or a maximum",
            "Use a graph to solve equations such as $ax^2 + bx + c = k$",
        ],
        key_concepts=["Parabola", "Roots", "Turning point", "Minimum", "Maximum", "Line of symmetry"],
        blocks=[
            H("Introduction"),
            T("When a footballer kicks a ball high into the air, its path is a curve called a **parabola**. "
              "Every graph of $y = ax^2 + bx + c$ has this shape."),
            T("In this lesson you will draw these graphs and read important information from them."),
            D("The graph of $y = ax^2 + bx + c$ is a **parabola**. The points where it crosses the $x$-axis are the **roots** of $ax^2 + bx + c = 0$, "
              "because there $y = 0$.", title="Definition: parabola and roots"),
            KEY("The shape depends on the sign of $a$", "Look at the number in front of $x^2$.", cards=[
                ["$a > 0$", "The curve opens upwards like a cup. The turning point is a **minimum**."],
                ["$a < 0$", "The curve opens downwards like a hill. The turning point is a **maximum**."],
            ], note="The **turning point** lies on the **line of symmetry**, $x = -\\frac{b}{2a}$."),
            EX("Worked example 1: draw and read a graph", intro=(
                r"Draw the graph of $y = x^2 - 2x - 3$ for $-2 \le x \le 4$. Use it to find the roots and the turning point."), steps=[
                S("Make a table of values", text="$x$: −2, −1, 0, 1, 2, 3, 4. $y$: 5, 0, −3, −4, −3, 0, 5."),
                S("Check one value", math=r"x = -2:\; (-2)^2 - 2(-2) - 3 = 4 + 4 - 3 = 5"),
                S("Plot the points and join them with a smooth curve", text="Do not join the points with straight lines."),
                S("Read the roots", text="The curve crosses the $x$-axis at $x = -1$ and $x = 3$."),
                S("Read the turning point", text="The lowest point is $(1, -4)$. It is a minimum. The line of symmetry is $x = 1$."),
            ]),
            GRAPH([1, -2, -3], alt="Parabola opening upwards, crossing the x-axis at -1 and 3, with its lowest point at (1, -4)",
                  caption="Figure 1. $y = x^2 - 2x - 3$. The roots are $-1$ and $3$; the minimum point is $(1, -4)$.",
                  xmin=-2.5, xmax=4.5, ymin=-5, ymax=6, roots=[-1, 3], label="y = x² − 2x − 3"),
            TIP("The line of symmetry is exactly halfway between the two roots: $\\frac{-1 + 3}{2} = 1$. Use this to check your turning point."),
            EX("Worked example 2: a maximum point", intro=r"For $y = 4 + 3x - x^2$, find the roots, the line of symmetry and the maximum value.", steps=[
                S("Here $a = -1$, so the curve has a maximum", text="It opens downwards."),
                S("Roots: solve $4 + 3x - x^2 = 0$", math=r"x^2 - 3x - 4 = 0 \;\Rightarrow\; (x - 4)(x + 1) = 0"),
                S("So the roots are", math=r"x = -1 \text{ and } x = 4"),
                S("Line of symmetry", math=r"x = -\frac{b}{2a} = -\frac{3}{2(-1)} = 1.5"),
                S("Maximum value", math=r"y = 4 + 3(1.5) - 1.5^2 = 4 + 4.5 - 2.25 = 6.25"),
            ]),
            GRAPH([-1, 3, 4], alt="Parabola opening downwards, crossing the x-axis at -1 and 4, with its highest point at (1.5, 6.25)",
                  caption="Figure 2. $y = 4 + 3x - x^2$ has a maximum point at $(1.5, 6.25)$.",
                  xmin=-2, xmax=5, ymin=-6, ymax=7, roots=[-1, 4], label="y = 4 + 3x − x²"),
            QUIZ(r"What is the turning point of $y = x^2 - 6x + 5$?",
                 ["$(3, -4)$", "$(-3, 32)$", "$(3, 4)$", "$(6, 5)$"], 0,
                 r"$x = -\frac{-6}{2} = 3$ and $y = 9 - 18 + 5 = -4$. Since $a > 0$ it is a minimum at $(3, -4)$.",
                 hint="Use $x = -\\frac{b}{2a}$, then substitute to find $y$.",
                 feedback=["", r"You used $x = \frac{b}{2a}$ and lost the minus sign.",
                           r"Check the arithmetic: $9 - 18 + 5 = -4$, not $4$.",
                           "The turning point is not found by reading $b$ and $c$ off the equation."]),
            H("Using a graph to solve other equations"),
            T(r"To solve $x^2 - 2x - 3 = 2$, draw the horizontal line $y = 2$ on Figure 1. Read the $x$-values where the line meets the curve."),
            EX("Worked example 3: solving with a line", intro=r"Use the graph of $y = x^2 - 2x - 3$ to solve $x^2 - 2x - 3 = 2$.", steps=[
                S("Draw the line $y = 2$", text="It is a horizontal line through 2 on the $y$-axis."),
                S("Read where it crosses the curve", text="The intersections are at about $x = -1.4$ and $x = 3.4$."),
                S("Check with algebra", math=r"x^2 - 2x - 5 = 0 \;\Rightarrow\; x = 1 \pm \sqrt{6} \approx -1.45 \text{ or } 3.45"),
            ]),
            H("Common mistakes"),
            MISTAKE("Joining points with a ruler", "A parabola is a smooth curve. Near the turning point it is rounded, not a sharp 'V'."),
            MISTAKE("Squaring negative numbers wrongly", "$(-2)^2 = 4$, but typing $-2^2$ into some calculators gives $-4$. Use brackets."),
            MISTAKE("Reading the turning point at a plotted point only",
                    "The turning point may lie between two plotted points, as in worked example 2 at $x = 1.5$. Use the line of symmetry."),
            H("Practice questions"),
            PQ(r"(a) Complete a table of values for $y = x^2 - x - 6$ for $-3 \le x \le 4$. (b) State the roots of $x^2 - x - 6 = 0$. (c) Find the minimum point.",
               r"(a) $x$: −3, −2, −1, 0, 1, 2, 3, 4. $y$: 6, 0, −4, −6, −6, −4, 0, 6. "
               r"(b) The curve crosses the $x$-axis at $x = -2$ and $x = 3$. "
               r"(c) The line of symmetry is $x = \frac{-2 + 3}{2} = 0.5$. Then $y = 0.25 - 0.5 - 6 = -6.25$. Minimum point $(0.5, -6.25)$."),
            PQ(r"Using the graph of $y = x^2 - x - 6$, solve $x^2 - x - 6 = -4$.",
               r"Draw the line $y = -4$. It meets the curve at $x = -1$ and $x = 2$. "
               r"Check: $x^2 - x - 2 = 0$ gives $(x - 2)(x + 1) = 0$."),
            PQ(r"Find the maximum value of $y = 5 + 4x - x^2$ and the value of $x$ where it occurs. Also find the roots of $5 + 4x - x^2 = 0$.",
               r"$x = -\frac{4}{2(-1)} = 2$. $y = 5 + 8 - 4 = 9$. The maximum value is 9 at $x = 2$. "
               r"Roots: $x^2 - 4x - 5 = 0$, so $(x - 5)(x + 1) = 0$ and $x = 5$ or $x = -1$."),
            PQ(r"The line $y = x + 1$ is drawn on the graph of $y = x^2 - 2x - 3$. Find the points where they meet, and the equation they solve.",
               r"At the intersections $x^2 - 2x - 3 = x + 1$, so $x^2 - 3x - 4 = 0$. Then $(x - 4)(x + 1) = 0$ and $x = 4$ or $x = -1$. "
               r"The points are $(4, 5)$ and $(-1, 0)$."),
            H("Summary"),
            SUM("The graph of $y = ax^2 + bx + c$ is a parabola. Draw it as a smooth curve.",
                "The roots of $ax^2 + bx + c = 0$ are where the curve crosses the $x$-axis.",
                "If $a > 0$ the turning point is a minimum; if $a < 0$ it is a maximum.",
                r"The line of symmetry is $x = -\frac{b}{2a}$, halfway between the roots.",
                "To solve $ax^2 + bx + c = k$, draw the line $y = k$ and read the $x$-values of the intersections."),
        ],
    ),
    # ------------------------------------------------------------- Sequences & Series
    lesson(
        module="Sequences & Series",
        topic="Arithmetic progressions",
        title="The nth term and the sum of an arithmetic progression",
        slug="arithmetic-progressions-nth-term-and-sum",
        minutes=25,
        summary="Recognise an arithmetic progression, find its nth term and the sum of its first n terms, and use them in everyday problems.",
        objectives=[
            "Recognise an arithmetic progression and find its common difference",
            "Use $T_n = a + (n - 1)d$ to find any term",
            "Use $S_n = \\frac{n}{2}[2a + (n - 1)d]$ to find the sum of the first $n$ terms",
            "Find the first term, common difference or number of terms from given information",
        ],
        key_concepts=["Sequence", "Arithmetic progression", "Common difference", "nth term", "Sum of n terms"],
        blocks=[
            H("Introduction"),
            T("Amina is a student in Garoua. She saves 2 000 FCFA in the first week. Each week after that she saves 500 FCFA more than the week before: "
              "2 000, 2 500, 3 000, 3 500, and so on."),
            T("The amounts go up by the same number each time. A list like this is called an **arithmetic progression** (AP)."),
            D("An **arithmetic progression** is a sequence in which each term is found by adding the same number to the term before. "
              "This number is the **common difference** $d$. The first term is $a$.",
              title="Definition: arithmetic progression", formula=r"d = T_2 - T_1 = T_3 - T_2 = \dots",
              note="$d$ can be negative. For example, 20, 17, 14, ... has $d = -3$."),
            KEY("Two formulas to learn", "For an AP with first term $a$ and common difference $d$:", cards=[
                ["The nth term", r"$T_n = a + (n - 1)d$"],
                ["Sum of the first n terms", r"$S_n = \frac{n}{2}[2a + (n - 1)d]$ or $S_n = \frac{n}{2}(a + l)$, where $l$ is the last term"],
            ]),
            T("Why $(n - 1)d$? To get from the 1st term to the $n$th term you add $d$ exactly $n - 1$ times."),
            EX("Worked example 1: a term and a sum", intro="For the AP 3, 7, 11, ..., find the 20th term and the sum of the first 20 terms.", steps=[
                S("Find $a$ and $d$", math=r"a = 3,\quad d = 7 - 3 = 4"),
                S("Use the nth term formula", math=r"T_{20} = 3 + (20 - 1) \times 4 = 3 + 76 = 79"),
                S("Use the sum formula with the last term", math=r"S_{20} = \frac{20}{2}(3 + 79) = 10 \times 82 = 820"),
            ]),
            EX("Worked example 2: savings", intro=(
                "Amina saves 2 000 FCFA in week 1, and 500 FCFA more each week. How much does she save in week 12, and how much has she saved in total after 12 weeks?"), steps=[
                S("Identify the AP", math=r"a = 2\,000,\quad d = 500,\quad n = 12"),
                S("Savings in week 12", math=r"T_{12} = 2\,000 + 11 \times 500 = 7\,500 \text{ FCFA}"),
                S("Total savings", math=r"S_{12} = \frac{12}{2}(2\,000 + 7\,500) = 6 \times 9\,500 = 57\,000 \text{ FCFA}"),
            ]),
            QUIZ("What is the 10th term of the AP 2, 5, 8, ...?",
                 ["32", "29", "30", "27"], 1,
                 r"$T_{10} = 2 + 9 \times 3 = 29$.",
                 hint="Use $T_n = a + (n - 1)d$ with $a = 2$ and $d = 3$.",
                 feedback=["You used $n \\times d$ instead of $(n - 1) \\times d$.", "",
                           "You multiplied $10 \\times 3$ but forgot to start from the first term.",
                           "$9 \\times 3 = 27$ is correct, but you forgot to add the first term, 2."]),
            EX("Worked example 3: finding a and d", intro="The 5th term of an AP is 17 and the 12th term is 38. Find the first term and the common difference.", steps=[
                S("Write two equations", math=r"a + 4d = 17 \qquad a + 11d = 38"),
                S("Subtract the first from the second", math=r"7d = 21, \text{ so } d = 3"),
                S("Find $a$", math=r"a = 17 - 4 \times 3 = 5"),
            ], check=r"5 + 11 \times 3 = 38"),
            EX("Worked example 4: number of terms", intro="How many terms are there in the AP 5, 9, 13, ..., 201?", steps=[
                S("Find $a$ and $d$", math=r"a = 5,\quad d = 4"),
                S("Set the nth term equal to the last term", math=r"5 + (n - 1) \times 4 = 201"),
                S("Solve", math=r"(n - 1) \times 4 = 196 \;\Rightarrow\; n - 1 = 49 \;\Rightarrow\; n = 50"),
            ]),
            H("Common mistakes"),
            MISTAKE("Using $nd$ instead of $(n - 1)d$", "The first term has no $d$ added. So the $n$th term has $(n - 1)$ lots of $d$."),
            MISTAKE("Getting the sign of $d$ wrong", "For 8, 5, 2, ..., $d = 5 - 8 = -3$. Always calculate second term minus first term."),
            MISTAKE("Confusing $T_n$ and $S_n$", "$T_n$ is one term. $S_n$ is the total of the first $n$ terms. Read the question carefully."),
            H("Practice questions"),
            PQ("Find the sum of the first 15 terms of the AP 8, 5, 2, ...",
               r"$a = 8$, $d = -3$, $n = 15$. $S_{15} = \frac{15}{2}[2(8) + 14(-3)] = \frac{15}{2}(16 - 42) = \frac{15}{2}(-26) = -195$."),
            PQ("The 3rd term of an AP is 11 and the 8th term is 31. Find (a) the common difference (b) the first term (c) the sum of the first 10 terms.",
               r"(a) $a + 2d = 11$ and $a + 7d = 31$, so $5d = 20$ and $d = 4$. (b) $a = 11 - 8 = 3$. "
               r"(c) $S_{10} = \frac{10}{2}[2(3) + 9(4)] = 5(6 + 36) = 210$."),
            PQ("How many terms of the AP 3, 7, 11, ... must be added to give a sum of 210?",
               r"$S_n = \frac{n}{2}[6 + 4(n - 1)] = \frac{n}{2}(4n + 2) = n(2n + 1)$. Set $n(2n + 1) = 210$, so $2n^2 + n - 210 = 0$. "
               r"Factorize: $(2n + 21)(n - 10) = 0$. Since $n$ must be a positive whole number, $n = 10$."),
            PQ("A hall in Yaoundé has 15 rows of seats. The first row has 20 seats and each row has 2 more seats than the row in front. "
               "(a) How many seats are in the last row? (b) How many seats are there in total?",
               r"(a) $T_{15} = 20 + 14 \times 2 = 48$ seats. (b) $S_{15} = \frac{15}{2}(20 + 48) = \frac{15}{2} \times 68 = 510$ seats."),
            H("Summary"),
            SUM("In an AP you add the same common difference $d$ each time: $d = T_2 - T_1$.",
                r"The nth term is $T_n = a + (n - 1)d$.",
                r"The sum of the first $n$ terms is $S_n = \frac{n}{2}[2a + (n - 1)d] = \frac{n}{2}(a + l)$.",
                "Two given terms give two simultaneous equations for $a$ and $d$.",
                "To find the number of terms, set $T_n$ equal to the last term and solve for $n$."),
        ],
    ),
    lesson(
        module="Sequences & Series",
        topic="Geometric progressions",
        title="The nth term and the sum of a geometric progression",
        slug="geometric-progressions-nth-term-and-sum",
        minutes=25,
        summary="Recognise a geometric progression, find its common ratio, its nth term and the sum of its first n terms, and use them in growth problems.",
        objectives=[
            "Recognise a geometric progression and find its common ratio",
            "Use $T_n = ar^{n-1}$ to find any term",
            "Use the formula for $S_n$ to find the sum of the first $n$ terms",
            "Find the first term, common ratio or position of a term from given information",
        ],
        key_concepts=["Geometric progression", "Common ratio", "nth term", "Sum of n terms"],
        blocks=[
            H("Introduction"),
            T("A trader in Limbe sells 100 000 FCFA of goods in her first month. Her sales rise by 10% every month: "
              "100 000, then 110 000, then 121 000, and so on."),
            T("Each amount is found by **multiplying** the one before by the same number, 1.1. A list like this is a **geometric progression** (GP)."),
            D("A **geometric progression** is a sequence in which each term is found by multiplying the term before by the same number. "
              "This number is the **common ratio** $r$. The first term is $a$.",
              title="Definition: geometric progression", formula=r"r = \frac{T_2}{T_1} = \frac{T_3}{T_2} = \dots",
              note="$r$ can be a fraction or negative. For example, 5, −10, 20, ... has $r = -2$."),
            KEY("Two formulas to learn", "For a GP with first term $a$ and common ratio $r$:", cards=[
                ["The nth term", r"$T_n = ar^{n-1}$"],
                ["Sum of the first n terms", r"$S_n = \frac{a(r^n - 1)}{r - 1}$ (easier when $r > 1$), or $S_n = \frac{a(1 - r^n)}{1 - r}$ (easier when $r < 1$)"],
            ], note="Both sum formulas give the same answer. Neither works when $r = 1$."),
            T("Why $r^{n-1}$? To get from the 1st term to the $n$th term you multiply by $r$ exactly $n - 1$ times."),
            EX("Worked example 1: a term and a sum", intro="For the GP 3, 6, 12, ..., find the 8th term and the sum of the first 8 terms.", steps=[
                S("Find $a$ and $r$", math=r"a = 3,\quad r = \frac{6}{3} = 2"),
                S("Use the nth term formula", math=r"T_8 = 3 \times 2^7 = 3 \times 128 = 384"),
                S("Use the sum formula with $r > 1$", math=r"S_8 = \frac{3(2^8 - 1)}{2 - 1} = 3 \times 255 = 765"),
            ]),
            EX("Worked example 2: growing sales", intro=(
                "The trader's sales are 100 000 FCFA in month 1 and rise by 10% each month. Find her sales in month 4 and her total sales over the first 4 months."), steps=[
                S("Identify the GP", math=r"a = 100\,000,\quad r = 1.1"),
                S("Sales in month 4", math=r"T_4 = 100\,000 \times 1.1^3 = 133\,100 \text{ FCFA}"),
                S("Total sales", math=r"S_4 = \frac{100\,000(1.1^4 - 1)}{1.1 - 1} = \frac{100\,000 \times 0.4641}{0.1} = 464\,100 \text{ FCFA}"),
            ], check=r"100\,000 + 110\,000 + 121\,000 + 133\,100 = 464\,100"),
            QUIZ("What is the common ratio of the GP 5, −10, 20, −40, ...?",
                 ["2", "−2", "−15", "$-\\frac{1}{2}$"], 1,
                 r"$r = \frac{-10}{5} = -2$. Check: $-10 \times (-2) = 20$.",
                 hint="Divide the second term by the first term.",
                 feedback=["The signs alternate, so the ratio must be negative.", "",
                           "That is a difference ($-10 - 5$). A GP uses a ratio, not a difference.",
                           "You divided the first term by the second. Use second ÷ first."]),
            EX("Worked example 3: finding a and r", intro="The 2nd term of a GP is 12 and the 5th term is 96. Find the first term and the common ratio.", steps=[
                S("Write two equations", math=r"ar = 12 \qquad ar^4 = 96"),
                S("Divide the second by the first", math=r"r^3 = \frac{96}{12} = 8"),
                S("Find $r$", math=r"r = 2"),
                S("Find $a$", math=r"a = \frac{12}{2} = 6"),
            ], check=r"6 \times 2^4 = 96"),
            EX("Worked example 4: a ratio less than 1", intro=r"Find the sum of the first 5 terms of the GP 81, 27, 9, ...", steps=[
                S("Find $a$ and $r$", math=r"a = 81,\quad r = \frac{27}{81} = \frac{1}{3}"),
                S("Use the formula for $r < 1$", math=r"S_5 = \frac{81\left(1 - \left(\frac{1}{3}\right)^5\right)}{1 - \frac{1}{3}} = \frac{81 \times \frac{242}{243}}{\frac{2}{3}}"),
                S("Simplify", math=r"S_5 = \frac{242}{3} \times \frac{3}{2} = 121"),
            ], check=r"81 + 27 + 9 + 3 + 1 = 121"),
            H("Common mistakes"),
            MISTAKE("Using $r^n$ instead of $r^{n-1}$", r"The first term is $a = ar^0$. So the $n$th term is $ar^{n-1}$, not $ar^n$."),
            MISTAKE("Calculating $ar^{n-1}$ as $(ar)^{n-1}$", r"Work out the power first, then multiply by $a$: $3 \times 2^7 = 3 \times 128$, not $6^7$."),
            MISTAKE("Mixing up AP and GP", "Check whether the terms go up by **adding** the same number (AP) or by **multiplying** by the same number (GP)."),
            H("Practice questions"),
            PQ("Find the 6th term of the GP 2, 6, 18, ...",
               r"$a = 2$, $r = 3$. $T_6 = 2 \times 3^5 = 2 \times 243 = 486$."),
            PQ("Find the sum of the first 6 terms of the GP 64, 32, 16, ...",
               r"$a = 64$, $r = \frac{1}{2}$. $S_6 = \frac{64\left(1 - \left(\frac{1}{2}\right)^6\right)}{1 - \frac{1}{2}} = 128 \times \frac{63}{64} = 126$. "
               r"Check: $64 + 32 + 16 + 8 + 4 + 2 = 126$."),
            PQ("The 3rd term of a GP is 20 and the 6th term is 160. Find (a) the common ratio (b) the first term (c) the sum of the first 7 terms.",
               r"(a) $ar^2 = 20$ and $ar^5 = 160$. Dividing: $r^3 = 8$, so $r = 2$. (b) $a = \frac{20}{4} = 5$. "
               r"(c) $S_7 = \frac{5(2^7 - 1)}{2 - 1} = 5 \times 127 = 635$."),
            PQ("Which term of the GP 3, 6, 12, ... is 768?",
               r"$T_n = 3 \times 2^{n-1} = 768$, so $2^{n-1} = 256 = 2^8$. Then $n - 1 = 8$ and $n = 9$. 768 is the 9th term."),
            H("Summary"),
            SUM("In a GP you multiply by the same common ratio $r$ each time: $r = T_2 \\div T_1$.",
                r"The nth term is $T_n = ar^{n-1}$.",
                r"The sum of the first $n$ terms is $S_n = \frac{a(r^n - 1)}{r - 1}$, or $\frac{a(1 - r^n)}{1 - r}$ when $r < 1$.",
                "Two given terms: divide one equation by the other to find $r$, then find $a$.",
                "Percentage growth of $p\\%$ per period gives a GP with $r = 1 + \\frac{p}{100}$."),
        ],
    ),
]
