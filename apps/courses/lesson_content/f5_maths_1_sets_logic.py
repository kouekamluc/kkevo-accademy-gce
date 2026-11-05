"""Form 5 General Mathematics (O Level), module "Set Theory & Logic": Venn diagrams and logic.
Draft content: check against the official syllabus."""

from .dsl import *  # noqa: F403

COURSE = ("mathematics", "form-5")

MODULE = "Set Theory & Logic"

LESSONS = [
    # ------------------------------------------------------------------ Venn diagrams
    lesson(
        module=MODULE,
        topic="Venn diagrams",
        title="Set notation and set language",
        slug="set-notation-and-set-language",
        minutes=20,
        summary="Read and write set notation: elements, subsets, the universal set, the empty set, complement, union, intersection and n(A).",
        objectives=[
            "List the elements of a set given in words or in set-builder form",
            "Use the symbols for 'is an element of', 'subset', universal set and empty set",
            "Find the union, intersection and complement of sets given as lists",
            "Count the elements of a set and the number of its subsets",
        ],
        key_concepts=["Set", "Element", "Subset", "Universal set", "Empty set", "Complement", "Union", "Intersection"],
        blocks=[
            H("Introduction"),
            T("A fruit seller at Bafoussam market sells mangoes, pawpaw, oranges and pineapples. "
              "In mathematics we can call this collection a **set**: {mango, pawpaw, orange, pineapple}."),
            T("Sets help us sort things into groups and count them. In this module they lead to Venn diagrams, "
              "which you will use to solve counting problems. First you need the language of sets."),
            D(r"A **set** is a well-defined collection of objects. Each object is an **element** (or member) of the set. "
              r"We write $x \in A$ for “$x$ is an element of $A$” and $x \notin A$ for “$x$ is not an element of $A$”.",
              title="Definition: set and element",
              note=r"If $A = \{2, 4, 6\}$, then $4 \in A$ and $5 \notin A$."),
            KEY("Two ways to write a set", "The same set can be written in two ways.", cards=[
                ["Listing", r"Write the elements inside curly brackets: $A = \{2, 3, 5, 7\}$."],
                ["Describing", r"Give a rule: $A = \{x : x \text{ is a prime number less than } 10\}$. Read the colon as “such that”."],
            ]),
            T(r"$n(A)$ means the **number of elements** in $A$. For $A = \{2, 3, 5, 7\}$, $n(A) = 4$. "
              "Each element is counted once, even if it is written twice."),
            EX("Worked example 1: listing sets", intro=(
                r"List the elements and give $n$ for each set. "
                r"(a) $A = \{x : x \text{ is a prime number less than } 12\}$ "
                r"(b) $B = \{x : x \text{ is an integer}, -2 \le x < 3\}$ "
                r"(c) $C = \{\text{months of the year beginning with J}\}$"), steps=[
                S("(a) Primes less than 12", math=r"A = \{2, 3, 5, 7, 11\},\quad n(A) = 5",
                  text="1 is not a prime number, so it is not in $A$."),
                S("(b) Integers from −2 up to, but not including, 3", math=r"B = \{-2, -1, 0, 1, 2\},\quad n(B) = 5",
                  text=r"$\le$ includes −2. $<$ leaves out 3."),
                S("(c) Months beginning with J", math=r"C = \{\text{January, June, July}\},\quad n(C) = 3"),
            ]),
            H("The universal set, the empty set and subsets"),
            D(r"The **universal set** $\xi$ contains every element being considered in a question. "
              r"The **empty set** has no elements. It is written $\emptyset$ or $\{\ \}$, and $n(\emptyset) = 0$.",
              title="Definition: universal set and empty set",
              note=r"$\{0\}$ is **not** empty: it has one element, the number 0."),
            D(r"$B$ is a **subset** of $A$, written $B \subset A$, if every element of $B$ is also an element of $A$.",
              title="Definition: subset",
              note=r"The empty set is a subset of every set. A set with $n$ elements has $2^n$ subsets."),
            IMG("f5m-venn-subset.svg",
                alt="Venn diagram: a rectangle for the universal set 1 to 10. Inside it a large oval A holds the even numbers 2, 6 and 10, "
                    "and a smaller oval B inside A holds 4 and 8. The odd numbers 1, 3, 5, 7 and 9 are outside A.",
                caption=r"Figure 1. $\xi = \{1, 2, \dots, 10\}$. $B = \{4, 8\}$ lies completely inside $A = \{2, 4, 6, 8, 10\}$, so $B \subset A$."),
            H("Union, intersection and complement"),
            KEY("Set operations", r"Let $A$ and $B$ be sets in a universal set $\xi$.", cards=[
                [r"Union $A \cup B$", "Elements in $A$, or in $B$, or in both. Think “or”."],
                [r"Intersection $A \cap B$", "Elements in both $A$ and $B$. Think “and”."],
                [r"Complement $A'$", r"Elements of $\xi$ that are **not** in $A$."],
            ]),
            EX("Worked example 2: union, intersection and complement", intro=(
                r"$\xi = \{1, 2, 3, \dots, 12\}$, $A = \{\text{factors of } 12\}$ and $B = \{\text{odd numbers}\}$. "
                r"Find $A \cap B$, $A \cup B$, $n(A \cup B)$ and $A'$."), steps=[
                S("List the sets", math=r"A = \{1, 2, 3, 4, 6, 12\},\quad B = \{1, 3, 5, 7, 9, 11\}"),
                S("Intersection: in both", math=r"A \cap B = \{1, 3\}"),
                S("Union: in either, each written once", math=r"A \cup B = \{1, 2, 3, 4, 5, 6, 7, 9, 11, 12\}"),
                S("Count the union", math=r"n(A \cup B) = 10"),
                S(r"Complement: in $\xi$ but not in $A$", math=r"A' = \{5, 7, 8, 9, 10, 11\}"),
            ], check=r"n(A) + n(A') = 6 + 6 = 12 = n(\xi)"),
            EX("Worked example 3: counting subsets", intro=r"List all the subsets of $\{a, b, c\}$.", steps=[
                S("No elements", math=r"\emptyset"),
                S("One element", math=r"\{a\},\ \{b\},\ \{c\}"),
                S("Two elements", math=r"\{a, b\},\ \{a, c\},\ \{b, c\}"),
                S("Three elements", math=r"\{a, b, c\}"),
                S("Count them", math=r"1 + 3 + 3 + 1 = 8 = 2^3"),
            ]),
            H("Common mistakes"),
            MISTAKE(r"Mixing up $\in$ and $\subset$",
                    r"$\in$ links an **element** to a set: $3 \in \{1, 3, 5\}$. $\subset$ links a **set** to a set: $\{3\} \subset \{1, 3, 5\}$. "
                    r"Writing $3 \subset \{1, 3, 5\}$ is wrong."),
            MISTAKE("Writing an element twice in a union",
                    r"In $A \cup B$, an element that is in both sets is written **once**. Otherwise $n(A \cup B)$ comes out too big."),
            MISTAKE(r"Thinking $\{0\}$ is the empty set",
                    r"$\{0\}$ has one element. The empty set $\emptyset$ has none."),
            QUIZ(r"$A = \{2, 4, 6, 8\}$. Which statement is true?",
                 [r"$4 \subset A$", r"$\{2, 8\} \subset A$", r"$5 \in A$", r"$n(A) = 20$"], 1,
                 r"Every element of $\{2, 8\}$ is in $A$, so $\{2, 8\} \subset A$.",
                 hint=r"Is each option about an element or a set? Use $\in$ for elements and $\subset$ for sets.",
                 feedback=[r"4 is an element, not a set. The correct statement is $4 \in A$.", "",
                           r"5 is odd, so $5 \notin A$.",
                           r"$n(A)$ counts the elements (there are 4). It does not add them up."]),
            QUIZ(r"$\xi = \{1, 2, 3, \dots, 10\}$ and $A = \{1, 2, 3, 4\}$. Find $n(A')$.",
                 ["4", "10", "6", "14"], 2,
                 r"$A' = \{5, 6, 7, 8, 9, 10\}$, so $n(A') = 10 - 4 = 6$.",
                 hint=r"$A'$ is everything in $\xi$ that is not in $A$.",
                 feedback=[r"4 is $n(A)$, not $n(A')$.", r"10 is $n(\xi)$. Remove the elements of $A$.", "",
                           r"You added $n(\xi)$ and $n(A)$. Subtract instead."]),
            H("Practice questions"),
            PQ(r"$\xi = \{x : x \text{ is an integer}, 1 \le x \le 15\}$, $P = \{\text{multiples of } 3\}$ and $Q = \{\text{factors of } 15\}$. "
               r"(a) List $P$ and $Q$. (b) Find $P \cap Q$ and $P \cup Q$. (c) Find $n(Q')$.",
               r"(a) $P = \{3, 6, 9, 12, 15\}$ and $Q = \{1, 3, 5, 15\}$. "
               r"(b) $P \cap Q = \{3, 15\}$ and $P \cup Q = \{1, 3, 5, 6, 9, 12, 15\}$. "
               r"(c) $n(Q') = 15 - 4 = 11$."),
            PQ(r"Say whether each statement is true or false: (a) $\{2\} \subset \{1, 2, 3\}$ (b) $2 \subset \{1, 2, 3\}$ (c) $\emptyset \subset \{1, 2, 3\}$ (d) $7 \notin \{1, 2, 3\}$.",
               r"(a) True. (b) False: 2 is an element, so write $2 \in \{1, 2, 3\}$. "
               r"(c) True: the empty set is a subset of every set. (d) True."),
            PQ("Describe the set $\\{1, 4, 9, 16, 25\\}$ in words and in set-builder form.",
               r"It is the set of square numbers from 1 to 25: $\{x : x = k^2,\ k \text{ an integer},\ 1 \le k \le 5\}$."),
            PQ("A set has 16 subsets. How many elements does it have?",
               r"A set with $n$ elements has $2^n$ subsets. $2^4 = 16$, so the set has **4** elements."),
            H("Summary"),
            SUM(r"$x \in A$ means $x$ is an element of $A$; $B \subset A$ means every element of $B$ is in $A$.",
                r"$\xi$ is the universal set; $\emptyset$ is the empty set, with $n(\emptyset) = 0$.",
                r"$A \cup B$ is “in $A$ or $B$”, $A \cap B$ is “in both”, and $A'$ is “in $\xi$ but not in $A$”.",
                r"$n(A)$ is the number of elements in $A$, each counted once.",
                r"A set with $n$ elements has $2^n$ subsets, including $\emptyset$ and the set itself."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="Venn diagrams",
        title="Two-set Venn diagrams and problems",
        slug="two-set-venn-diagrams-and-problems",
        minutes=22,
        summary="Shade the regions of a two-set Venn diagram, use n(A ∪ B) = n(A) + n(B) − n(A ∩ B), and solve problems with an unknown region x.",
        objectives=[
            "Name and shade the four regions of a two-set Venn diagram",
            "Fill in a two-set Venn diagram from the centre outwards",
            r"Use the rule n(A ∪ B) = n(A) + n(B) − n(A ∩ B)",
            "Solve problems where one region is an unknown x",
        ],
        key_concepts=["Venn diagram", "Region", "Counting rule for two sets", "Unknown region"],
        blocks=[
            H("Introduction"),
            T("A school in Bamenda wants to know how many students belong to the Maths Club, the French Club, both, or neither. "
              "A **Venn diagram** answers questions like this quickly. "
              r"In the previous lesson you met $\cup$, $\cap$ and $A'$ as lists. Now you will draw them as regions and use them to count."),
            D(r"A **Venn diagram** shows the universal set $\xi$ as a rectangle and each set as a circle inside it. "
              "Two overlapping circles split the rectangle into **four regions**.",
              title="Definition: Venn diagram"),
            KEY("The four regions of a two-set diagram", "Every element of $\\xi$ is in exactly one of these regions.", cards=[
                [r"$A \cap B'$", "In $A$ only."],
                [r"$A \cap B$", "In both $A$ and $B$ (the overlap)."],
                [r"$A' \cap B$", "In $B$ only."],
                [r"$(A \cup B)'$", "In neither set (outside both circles)."],
            ]),
            IMG("f5m-venn-shading-regions.svg",
                alt="Four small Venn diagrams with circles A and B in a rectangle. Top left: only the overlap is shaded, A intersect B. "
                    "Top right: both circles are shaded, A union B. Bottom left: everything outside circle A is shaded, A complement. "
                    "Bottom right: circle A without the overlap is shaded, A only.",
                caption=r"Figure 1. Shading $A \cap B$, $A \cup B$, $A'$ and $A \cap B'$."),
            TIP("Always fill a Venn diagram **from the middle outwards**: write the overlap first, then the 'only' regions, "
                "then the outside region last."),
            EX("Worked example 1: filling a diagram", intro=(
                "In a class of 40 students, 25 are in the Maths Club (M), 18 are in the French Club (F) and 7 are in both. "
                "(a) How many are in neither club? (b) How many are in exactly one club?"), steps=[
                S("Start with the overlap", text="Write 7 where the circles cross."),
                S("M only", math=r"25 - 7 = 18"),
                S("F only", math=r"18 - 7 = 11"),
                S("Inside the circles", math=r"18 + 7 + 11 = 36"),
                S("(a) Neither club", math=r"40 - 36 = 4"),
                S("(b) Exactly one club", math=r"18 + 11 = 29"),
            ], check=r"18 + 7 + 11 + 4 = 40"),
            IMG("f5-venn-two-sets.svg",
                alt="Venn diagram in a rectangle labelled xi = 40, with two overlapping circles: Maths Club (M) and French Club (F). "
                    "M only is 18, the overlap is 7, F only is 11 and 4 are outside both circles.",
                caption="Figure 2. Worked example 1: 18 + 7 + 11 + 4 = 40."),
            H("The counting rule"),
            F(r"n(A \cup B) = n(A) + n(B) - n(A \cap B)", title="Counting rule for two sets"),
            T(r"When you add $n(A)$ and $n(B)$, the elements in the overlap are counted twice: once in $A$ and once in $B$. "
              r"Subtracting $n(A \cap B)$ once corrects this."),
            EX("Worked example 2: using the rule", intro=(
                "There are 50 Form 5 students in a school in Limbe. 32 take Biology and 27 take Chemistry. "
                "Every student takes at least one of the two. How many take both?"), steps=[
                S("Every student is in at least one set", math=r"n(B \cup C) = 50"),
                S("Use the rule", math=r"50 = 32 + 27 - n(B \cap C)"),
                S("Solve", math=r"n(B \cap C) = 59 - 50 = 9"),
            ], check=r"23 + 9 + 18 = 50"),
            QUIZ("Which set is the region inside circle $A$ but outside circle $B$?",
                 [r"$A \cap B$", r"$A \cup B$", r"$A \cap B'$", r"$A'$"], 2,
                 r"Inside $A$ means $A$; outside $B$ means $B'$. Both together: $A \cap B'$.",
                 hint=r"“Inside A” and “outside B” must both be true. Which symbol means “and”?",
                 feedback=[r"$A \cap B$ is the overlap, which is inside $B$.",
                           r"$A \cup B$ includes all of circle $B$ as well.", "",
                           r"$A'$ is everything outside $A$, the opposite region."]),
            H("Problems with an unknown region"),
            T("Sometimes the number in a region is not given. Call it $x$, write every other region in terms of $x$, "
              "and make all the regions add up to the total."),
            EX("Worked example 3: an unknown region", intro=(
                "30 students were asked about sport. 18 play football, 15 play basketball and 2 play neither. "
                "Let $x$ be the number who play both. Find $x$."), steps=[
                S("Write each region in terms of $x$", text="Both: $x$. Football only: $18 - x$. Basketball only: $15 - x$. Neither: 2."),
                S("The regions add up to the total", math=r"(18 - x) + x + (15 - x) + 2 = 30"),
                S("Simplify", math=r"35 - x = 30"),
                S("Solve", math=r"x = 5"),
            ], check=r"13 + 5 + 10 + 2 = 30"),
            IMG("f5-venn-unknown-region.svg",
                alt="Venn diagram in a rectangle labelled xi = 30, with two overlapping circles: Football and Basketball. "
                    "Football only is 18 minus x, the overlap is x, Basketball only is 15 minus x and 2 are outside both circles.",
                caption="Figure 3. Worked example 3: write every region in terms of x."),
            H("Common mistakes"),
            MISTAKE("Writing the given totals straight into the 'only' regions",
                    "If 25 students are in M, the number 25 is the **whole circle**, not 'M only'. Subtract the overlap first."),
            MISTAKE("Forgetting the region outside the circles",
                    r"The regions inside the circles may not add up to $n(\xi)$. The rest go outside both circles."),
            MISTAKE("Adding the overlap in the counting rule",
                    r"It is $n(A) + n(B) - n(A \cap B)$, with a **minus**. The overlap is removed once, not added."),
            QUIZ(r"$n(A) = 12$, $n(B) = 9$ and $n(A \cap B) = 4$. What is $n(A \cup B)$?",
                 ["21", "17", "25", "13"], 1,
                 r"$n(A \cup B) = 12 + 9 - 4 = 17$.",
                 hint="Add the two sets, then remove the overlap that was counted twice.",
                 feedback=["You added 12 and 9 but did not subtract the overlap.", "",
                           "You added the overlap instead of subtracting it.", "You subtracted the overlap twice."]),
            H("Practice questions"),
            PQ("Of 60 moto-taxi drivers in Douala, 35 own a smartphone, 28 have a driving licence and 10 have neither. "
               "(a) How many have both? (b) How many have a smartphone but no licence?",
               r"(a) Inside the circles: $60 - 10 = 50$. So $50 = 35 + 28 - x$, giving $x = 13$. "
               r"(b) Smartphone only: $35 - 13 = 22$. Check: $22 + 13 + 15 + 10 = 60$."),
            PQ(r"$n(\xi) = 48$, $n(A) = 20$, $n(B) = 25$ and $n\big((A \cup B)'\big) = 10$. Find (a) $n(A \cap B)$ (b) $n(A \cap B')$.",
               r"(a) $n(A \cup B) = 48 - 10 = 38$, so $n(A \cap B) = 20 + 25 - 38 = 7$. "
               r"(b) $n(A \cap B') = 20 - 7 = 13$."),
            PQ("In a class of 40 students, 22 like rice (R) and $3x$ like fufu (F). $x$ like both and 4 like neither. "
               "(a) Write the number who like fufu only in terms of $x$. (b) Find $x$. (c) How many like rice only?",
               r"(a) Fufu only $= 3x - x = 2x$. "
               r"(b) $(22 - x) + x + 2x + 4 = 40$, so $26 + 2x = 40$ and $x = 7$. "
               r"(c) Rice only $= 22 - 7 = 15$. Check: $15 + 7 + 14 + 4 = 40$."),
            H("Summary"),
            SUM("Two circles split the rectangle into four regions: A only, both, B only and neither.",
                "Fill a Venn diagram from the centre outwards, and the outside region last.",
                r"Counting rule: $n(A \cup B) = n(A) + n(B) - n(A \cap B)$.",
                "If a region is unknown, call it $x$, write every region in terms of $x$, and make the regions add up to the total."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="Venn diagrams",
        title="Three-set Venn diagrams",
        slug="three-set-venn-diagrams",
        minutes=25,
        summary="Fill in a three-set Venn diagram from the centre outwards, read its eight regions, and solve word problems, including ones with an unknown x.",
        objectives=[
            "Name the eight regions of a three-set Venn diagram",
            "Fill in a three-set diagram from the centre outwards",
            "Answer questions such as 'exactly two' or 'none' from a completed diagram",
            "Solve three-set problems with an unknown region",
        ],
        key_concepts=["Three-set Venn diagram", "Centre region", "'Only' regions", "Exactly one / exactly two"],
        blocks=[
            H("Introduction"),
            T("At Mokolo market in Yaoundé, many traders sell more than one product: rice, beans and oil. "
              "To count them we need **three** circles."),
            T("In the previous lesson you filled two-set diagrams from the middle outwards. "
              "The same idea works for three sets. There are just more regions."),
            D(r"Three overlapping circles $A$, $B$ and $C$ split the rectangle into **8 regions**: "
              r"the centre $A \cap B \cap C$, three 'two only' regions (such as $A \cap B \cap C'$), "
              r"three 'one only' regions (such as $A \cap B' \cap C'$), and the outside $(A \cup B \cup C)'$.",
              title="The eight regions"),
            KEY("Order for filling a three-set diagram", "Each step uses numbers you already have.", cards=[
                ["1. Centre", "Write the number in all three sets."],
                ["2. Two only", "Each 'both' total minus the centre."],
                ["3. One only", "Each circle total minus the three regions already in it."],
                ["4. Outside", "The universal total minus everything inside the circles."],
            ]),
            EX("Worked example 1: filling a three-set diagram", intro=(
                "50 traders at Mokolo market were asked what they sell. 24 sell rice (R), 20 sell beans (B) and 18 sell oil (O). "
                "8 sell rice and beans, 6 sell beans and oil, 7 sell rice and oil, and 3 sell all three. "
                "How many sell rice only, and how many sell none of the three?"), steps=[
                S("Centre first", text="3 traders sell all three."),
                S("'Two only' regions", math=r"R \cap B \text{ only} = 8 - 3 = 5,\quad B \cap O \text{ only} = 6 - 3 = 3,\quad R \cap O \text{ only} = 7 - 3 = 4"),
                S("Rice only", math=r"24 - 5 - 4 - 3 = 12"),
                S("Beans only and oil only", math=r"20 - 5 - 3 - 3 = 9,\qquad 18 - 4 - 3 - 3 = 8"),
                S("Total inside the circles", math=r"12 + 9 + 8 + 5 + 3 + 4 + 3 = 44"),
                S("None of the three", math=r"50 - 44 = 6", text="12 sell rice only and 6 sell none."),
            ], check=r"44 + 6 = 50"),
            IMG("f5-venn-three-sets.svg",
                alt="Three-set Venn diagram in a rectangle labelled xi = 50, with circles Rice (R), Beans (B) and Oil (O). "
                    "Rice only 12, beans only 9, oil only 8, rice and beans only 5, beans and oil only 3, rice and oil only 4, "
                    "all three 3, and 6 outside all circles.",
                caption="Figure 1. Worked example 1: fill from the centre outwards; 6 traders sell none of the three."),
            QUIZ("Using Figure 1, how many traders sell beans and oil but **not** rice?",
                 ["6", "3", "9", "5"], 1,
                 r"The region $B \cap O \cap R'$ is the 'beans and oil only' region, which holds 3.",
                 hint="Find the region inside both the beans and oil circles but outside the rice circle.",
                 feedback=["6 is everyone who sells beans and oil, including the 3 who also sell rice.", "",
                           "9 is the number who sell beans only.",
                           "5 is the number who sell rice and beans only."]),
            EX("Worked example 2: reading a completed diagram", intro=(
                "Use Figure 1. How many traders sell (a) exactly two of the products, (b) rice or beans but not oil, "
                r"(c) neither rice nor beans, that is $n(R' \cap B')$?"), steps=[
                S("(a) Add the three 'two only' regions", math=r"5 + 3 + 4 = 12"),
                S("(b) Regions in R or B but outside O", text="Rice only, rice and beans only, beans only.",
                  math=r"12 + 5 + 9 = 26"),
                S("(c) Regions outside both R and B", text="Oil only, and the outside region.",
                  math=r"8 + 6 = 14"),
            ]),
            H("Problems with an unknown"),
            T("When the centre is unknown, call it $x$. Then every 'two only' region and every 'one only' region "
              "can be written in terms of $x$. The regions add up to the total."),
            EX("Worked example 3: an unknown centre", intro=(
                "In a group of 100 students, 40 study Physics (P), 42 study Chemistry (C) and 48 study Biology (B). "
                "15 study Physics and Chemistry, 18 study Chemistry and Biology, 12 study Physics and Biology, "
                "and 10 study none of the three. $x$ students study all three. Find $x$, and the number who study exactly one subject."), steps=[
                S("Two only regions", math=r"P \cap C: 15 - x,\quad C \cap B: 18 - x,\quad P \cap B: 12 - x"),
                S("One only regions", math=r"P: 40 - (15 - x) - (12 - x) - x = 13 + x"),
                S("The other two", math=r"C: 42 - (15 - x) - (18 - x) - x = 9 + x,\quad B: 48 - (18 - x) - (12 - x) - x = 18 + x"),
                S("Inside the circles", math=r"100 - 10 = 90"),
                S("Add all seven regions", math=r"(13 + x) + (9 + x) + (18 + x) + (15 - x) + (18 - x) + (12 - x) + x = 85 + x"),
                S("Solve", math=r"85 + x = 90 \;\Rightarrow\; x = 5"),
                S("Exactly one subject", math=r"18 + 14 + 23 = 55"),
            ], check=r"55 + (10 + 13 + 7) + 5 + 10 = 100"),
            TIP(r"Quick check for three sets: $n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(A \cap C) + n(A \cap B \cap C)$. "
                r"In worked example 3: $40 + 42 + 48 - 15 - 18 - 12 + x = 90$ gives $x = 5$ again."),
            H("Common mistakes"),
            MISTAKE("Forgetting to remove the centre from the 'both' totals",
                    r"“8 sell rice and beans” includes the 3 who sell all three. The 'rice and beans only' region is $8 - 3 = 5$."),
            MISTAKE("Subtracting the centre twice",
                    "Rice only is the rice total minus the **two only** regions and the centre. "
                    "If you subtract the full 'both' totals (8 and 7), you remove the centre twice."),
            MISTAKE("Using the universal total for the circles",
                    "If some elements are in none of the sets, the circles hold only $n(\\xi)$ minus that number."),
            QUIZ("A three-set Venn diagram, including the region outside the circles, has how many regions?",
                 ["6", "7", "8", "9"], 2,
                 "1 centre + 3 'two only' + 3 'one only' + 1 outside = 8.",
                 hint="Count the centre, the 'two only' regions, the 'one only' regions and the outside.",
                 feedback=["You may have missed the centre and the outside.",
                           "7 is the number of regions inside the circles. Add the outside region.", "",
                           "There is no ninth region: every element is in exactly one of 8 regions."]),
            H("Practice questions"),
            PQ("80 households in Ebolowa were surveyed. 45 have a radio (R), 38 a television (T) and 30 a computer (C). "
               "20 have a radio and a television, 15 a television and a computer, 12 a radio and a computer, and 8 have all three. "
               "Find the number of households that have (a) none of the three (b) exactly two (c) a radio only.",
               r"Centre 8. Two only: $R \cap T$: $20 - 8 = 12$, $T \cap C$: $15 - 8 = 7$, $R \cap C$: $12 - 8 = 4$. "
               r"One only: $R$: $45 - 12 - 4 - 8 = 21$, $T$: $38 - 12 - 7 - 8 = 11$, $C$: $30 - 7 - 4 - 8 = 11$. "
               r"Inside: $21 + 11 + 11 + 12 + 7 + 4 + 8 = 74$. "
               r"(a) $80 - 74 = 6$ (b) $12 + 7 + 4 = 23$ (c) 21."),
            PQ("In a class of 40 students, the regions of a Venn diagram for Maths (M), Physics (P) and Chemistry (C) are: "
               "M only 10, P only 8, C only 6, M and P only $x$, P and C only 3, M and C only 4, all three $2x$, and 3 take none. "
               "(a) Find $x$. (b) How many take Maths?",
               r"(a) $10 + 8 + 6 + x + 3 + 4 + 2x + 3 = 40$, so $34 + 3x = 40$ and $x = 2$. "
               r"(b) $n(M) = 10 + x + 4 + 2x = 14 + 3(2) = 20$."),
            PQ("Using Figure 1, find $n(R \\cup O)$ and $n\\big((R \\cup B \\cup O)'\\big)$.",
               r"$R \cup O$ contains every region in the rice or oil circles: $12 + 5 + 4 + 3 + 3 + 8 = 35$. "
               r"$(R \cup B \cup O)'$ is the outside region: 6."),
            H("Summary"),
            SUM("A three-set Venn diagram has 8 regions, including the outside.",
                "Fill it in this order: centre, 'two only', 'one only', outside.",
                "A 'both' total includes the centre, so subtract the centre to get the 'two only' region.",
                "With an unknown centre, write every region in terms of $x$ and make the regions add to the number inside the circles."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="Venn diagrams",
        title="Laws of set algebra",
        slug="laws-of-set-algebra",
        minutes=22,
        summary="State and use the commutative, associative and distributive laws and De Morgan's laws, and check them by shading Venn diagrams or listing elements.",
        objectives=[
            "State the commutative, associative and distributive laws for sets",
            "State and use De Morgan's laws",
            "Check a law by shading both sides of a Venn diagram or by listing elements",
            "Simplify set expressions using the laws",
        ],
        key_concepts=["Commutative law", "Associative law", "Distributive law", "De Morgan's laws", "Complement laws"],
        blocks=[
            H("Introduction"),
            T("In ordinary arithmetic, $3 + 5 = 5 + 3$ and $2 \\times (4 + 1) = 2 \\times 4 + 2 \\times 1$. "
              "Sets have similar rules, called the **laws of set algebra**."),
            T("In the previous lessons you shaded regions of Venn diagrams. Now you will use shading to check that two "
              "different expressions describe the same region."),
            KEY("The main laws", r"These hold for any sets $A$, $B$ and $C$ in $\xi$.", cards=[
                ["Commutative", r"$A \cup B = B \cup A$ and $A \cap B = B \cap A$"],
                ["Associative", r"$(A \cup B) \cup C = A \cup (B \cup C)$ and $(A \cap B) \cap C = A \cap (B \cap C)$"],
                ["Distributive", r"$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ and $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$"],
                ["De Morgan", r"$(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$"],
            ]),
            D(r"$A \cup A' = \xi$, $\quad A \cap A' = \emptyset$, $\quad (A')' = A$, $\quad A \cup \emptyset = A$, $\quad A \cap \xi = A$.",
              title="Complement and identity results",
              note=r"Each one is easy to see on a Venn diagram. For example, $A$ and $A'$ together fill the whole rectangle."),
            H("Checking a law by shading"),
            T("To check that two expressions are equal, shade the region for the left side on one diagram and the region for the "
              "right side on another. If the shaded regions are the same, the law holds."),
            IMG("f5m-venn-de-morgan.svg",
                alt="Four Venn diagrams of A and B. Top row, (A union B)' and A' intersect B': only the region outside both circles is shaded. "
                    "Bottom row, (A intersect B)' and A' union B': everything except the overlap is shaded.",
                caption=r"Figure 1. De Morgan's laws: each row shows two expressions that shade the same region."),
            T(r"Top row: $A'$ is everything outside $A$ and $B'$ is everything outside $B$. Their intersection is the part outside **both** circles, "
              r"which is exactly $(A \cup B)'$. Bottom row: $A' \cup B'$ is everything except the overlap, which is $(A \cap B)'$."),
            EX("Worked example 1: De Morgan's laws by listing", intro=(
                r"$\xi = \{1, 2, \dots, 8\}$, $A = \{1, 2, 3, 4\}$ and $B = \{3, 4, 5, 6\}$. "
                r"Show that $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$."), steps=[
                S("Complements", math=r"A' = \{5, 6, 7, 8\},\quad B' = \{1, 2, 7, 8\}"),
                S("First law, left side", math=r"A \cup B = \{1, 2, 3, 4, 5, 6\} \;\Rightarrow\; (A \cup B)' = \{7, 8\}"),
                S("First law, right side", math=r"A' \cap B' = \{7, 8\}"),
                S("Second law, left side", math=r"A \cap B = \{3, 4\} \;\Rightarrow\; (A \cap B)' = \{1, 2, 5, 6, 7, 8\}"),
                S("Second law, right side", math=r"A' \cup B' = \{1, 2, 5, 6, 7, 8\}", text="Both laws hold for these sets."),
            ]),
            EX("Worked example 2: the distributive law", intro=(
                r"$\xi = \{1, 2, \dots, 10\}$, $A = \{1, 2, 3, 4, 5\}$, $B = \{2, 4, 6, 8\}$ and $C = \{3, 6, 9\}$. "
                r"Verify that $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$."), steps=[
                S("Bracket first on the left", math=r"B \cup C = \{2, 3, 4, 6, 8, 9\}"),
                S("Left side", math=r"A \cap (B \cup C) = \{2, 3, 4\}"),
                S("Pieces of the right side", math=r"A \cap B = \{2, 4\},\quad A \cap C = \{3\}"),
                S("Right side", math=r"(A \cap B) \cup (A \cap C) = \{2, 3, 4\}", text="The two sides are equal."),
            ]),
            QUIZ(r"Which set is always equal to $(A \cap B)'$?",
                 [r"$A' \cap B'$", r"$A' \cup B'$", r"$A \cup B$", r"$(A \cup B)'$"], 1,
                 r"De Morgan: complementing an intersection gives the union of the complements.",
                 hint=r"Shade $(A \cap B)'$: everything except the overlap. Which option shades the same?",
                 feedback=[r"$A' \cap B'$ is the region outside both circles. It equals $(A \cup B)'$.", "",
                           r"$A \cup B$ does not include the region outside both circles, but $(A \cap B)'$ does.",
                           r"$(A \cup B)'$ is only the outside region."]),
            H("Simplifying with the laws"),
            EX("Worked example 3: simplifying expressions", intro=r"Simplify (a) $(A \cap B) \cup (A \cap B')$ (b) $(A' \cup B')'$.", steps=[
                S("(a) Distributive law in reverse", math=r"(A \cap B) \cup (A \cap B') = A \cap (B \cup B')"),
                S("(a) Complement law, then identity", math=r"A \cap (B \cup B') = A \cap \xi = A"),
                S("(b) De Morgan", math=r"(A' \cup B')' = (A')' \cap (B')'"),
                S("(b) Double complement", math=r"(A')' \cap (B')' = A \cap B"),
            ]),
            TIP("Check a simplification with a diagram: in (a), 'A and B' together with 'A but not B' is the whole of circle A."),
            H("Common mistakes"),
            MISTAKE("Forgetting to change the sign in De Morgan's laws",
                    r"When you take the complement of a bracket, complement **each** set **and** swap $\cup$ with $\cap$. "
                    r"$(A \cup B)' = A' \cup B'$ is wrong."),
            MISTAKE("Distributing only to the first set",
                    r"$A \cap (B \cup C)$ is **not** $(A \cap B) \cup C$. $A$ must be combined with both $B$ and $C$."),
            MISTAKE("Testing one example and calling it a proof",
                    "Listing elements checks a law for those sets only. Shading a general Venn diagram shows the law for all sets."),
            QUIZ(r"What is $A \cap A'$?", [r"$\xi$", r"$A$", r"$\emptyset$", r"$A'$"], 2,
                 r"No element can be in $A$ and not in $A$ at the same time, so $A \cap A' = \emptyset$.",
                 hint=r"Can an element be inside $A$ and outside $A$ at once?",
                 feedback=[r"$\xi$ is $A \cup A'$, the union, not the intersection.",
                           r"$A$ is $A \cap \xi$. Here we intersect with $A'$.", "",
                           r"$A'$ is $A' \cap \xi$, not $A \cap A'$."]),
            H("Practice questions"),
            PQ(r"$\xi = \{1, 2, \dots, 12\}$, $A = \{\text{even numbers}\}$ and $B = \{\text{multiples of } 3\}$. Show that $(A \cap B)' = A' \cup B'$.",
               r"$A \cap B = \{6, 12\}$, so $(A \cap B)' = \{1, 2, 3, 4, 5, 7, 8, 9, 10, 11\}$. "
               r"$A' = \{1, 3, 5, 7, 9, 11\}$ and $B' = \{1, 2, 4, 5, 7, 8, 10, 11\}$, so "
               r"$A' \cup B' = \{1, 2, 3, 4, 5, 7, 8, 9, 10, 11\}$. The two sides are equal."),
            PQ(r"$\xi = \{1, 2, \dots, 6\}$, $A = \{1, 2\}$, $B = \{2, 3, 4\}$ and $C = \{4, 5\}$. Verify that $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$.",
               r"$B \cap C = \{4\}$, so the left side is $\{1, 2, 4\}$. "
               r"$A \cup B = \{1, 2, 3, 4\}$ and $A \cup C = \{1, 2, 4, 5\}$, so the right side is $\{1, 2, 4\}$. Equal."),
            PQ(r"$n(\xi) = 30$ and $n(A' \cap B') = 6$. Use De Morgan's law to find $n(A \cup B)$.",
               r"$A' \cap B' = (A \cup B)'$, so $n\big((A \cup B)'\big) = 6$ and $n(A \cup B) = 30 - 6 = 24$."),
            PQ(r"Use a Venn diagram to simplify $A \cup (A \cap B)$.",
               r"$A \cap B$ is the overlap, which lies inside $A$. Adding it to $A$ adds nothing new, so $A \cup (A \cap B) = A$."),
            H("Summary"),
            SUM(r"Commutative: order does not matter, $A \cup B = B \cup A$, $A \cap B = B \cap A$.",
                "Associative: with only $\\cup$ (or only $\\cap$), brackets can move.",
                r"Distributive: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ and $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$.",
                r"De Morgan: $(A \cup B)' = A' \cap B'$ and $(A \cap B)' = A' \cup B'$: complement each set and swap the sign.",
                "Check a law by shading both sides of a Venn diagram; listing elements checks one example."),
        ],
    ),
    # ------------------------------------------------------------------ Logic
    lesson(
        module=MODULE,
        topic="Logic",
        title="Statements, negation and connectives",
        slug="statements-negation-and-connectives",
        minutes=20,
        summary="Recognise statements and their truth values, form negations, and find the truth value of compound statements using 'and' (∧) and 'or' (∨).",
        objectives=[
            "Decide whether a sentence is a statement and give its truth value",
            "Write the negation ∼p of a statement, including statements with 'all' and 'some'",
            "Find the truth value of p ∧ q and p ∨ q",
            "Translate between compound statements in words and in symbols",
        ],
        key_concepts=["Statement", "Truth value", "Negation", "Conjunction", "Disjunction"],
        blocks=[
            H("Introduction"),
            T("Every day we reason with sentences like “It is raining in Buea” or “The bus to Kumba is full”. "
              "Each of these is either true or false. Logic studies such sentences and how to combine them."),
            T("In this lesson you will learn the basic words of logic and their symbols. The next lessons build on them."),
            D("A **statement** is a sentence that is either true or false, but not both. "
              "Its **truth value** is T (true) or F (false). We name statements with small letters such as $p$, $q$ and $r$.",
              title="Definition: statement",
              note="Questions (“Is it hot?”), commands (“Close the door”) and exclamations (“What a match!”) are not statements: "
                   "they cannot be true or false. Opinions such as “Ndolé is the best dish” are also not treated as statements."),
            EX("Worked example 1: statements and truth values", intro=(
                "Which of these are statements? Give the truth value of each statement. "
                "(a) Yaoundé is the capital of Cameroon. (b) Pass me the salt. (c) $7 + 5 = 13$. (d) Did you finish your homework?"), steps=[
                S("(a)", text="A statement. It is true (T)."),
                S("(b)", text="A command, not a statement."),
                S("(c)", text=r"A statement. $7 + 5 = 12$, so it is false (F). A false sentence is still a statement."),
                S("(d)", text="A question, not a statement."),
            ]),
            H("Negation"),
            D(r"The **negation** of $p$ is written $\sim p$ and read “not $p$”. "
              r"If $p$ is true, $\sim p$ is false; if $p$ is false, $\sim p$ is true.",
              title="Definition: negation",
              note=r"$p$: “Garoua is in Cameroon” (T). $\sim p$: “Garoua is not in Cameroon” (F)."),
            T("Be careful with “all” and “some”. The negation of “All the students passed” is "
              "“Not all the students passed”, which means “At least one student did not pass”. It is **not** “All the students failed”."),
            H("Joining statements: and, or"),
            KEY("Two connectives", r"Let $p$ and $q$ be statements.", cards=[
                [r"Conjunction $p \wedge q$", "“$p$ and $q$”. True only when **both** $p$ and $q$ are true."],
                [r"Disjunction $p \vee q$", "“$p$ or $q$”. True when **at least one** of $p$, $q$ is true. False only when both are false."],
            ]),
            T(r"For the four cases $(p, q)$ = (T, T), (T, F), (F, T), (F, F): "
              r"$p \wedge q$ is T, F, F, F and $p \vee q$ is T, T, T, F. You will set these out as truth tables in the next lesson."),
            TIP("In logic, “or” includes “both”. “I will buy rice or beans” is true if you buy both."),
            EX("Worked example 2: truth values of compound statements", intro=(
                r"Let $p$: “Douala is a town in Cameroon” and $q$: “5 is an even number”. "
                r"Find the truth values of $\sim p$, $\sim q$, $p \wedge q$, $p \vee q$ and $\sim p \vee q$."), steps=[
                S("Simple statements", text="$p$ is true (T). $q$ is false (F)."),
                S("Negations", math=r"\sim p \text{ is F},\qquad \sim q \text{ is T}"),
                S("“And” needs both true", math=r"p \wedge q = \text{T} \wedge \text{F} = \text{F}"),
                S("“Or” needs at least one true", math=r"p \vee q = \text{T} \vee \text{F} = \text{T}"),
                S("Negate first, then join", math=r"\sim p \vee q = \text{F} \vee \text{F} = \text{F}"),
            ]),
            EX("Worked example 3: words and symbols", intro=(
                r"Let $p$: “Amina is tall” and $q$: “Amina plays basketball”. Write in symbols: "
                r"(a) Amina is tall but she does not play basketball. (b) Amina is neither tall nor does she play basketball. "
                r"Then write $\sim(p \wedge q)$ in words."), steps=[
                S("(a) “But” means “and”", math=r"p \wedge \sim q"),
                S("(b) “Neither … nor” means “not … and not”", math=r"\sim p \wedge \sim q"),
                S(r"$\sim(p \wedge q)$ in words", text="It is not true that Amina is tall and plays basketball. (She is not both.)"),
            ]),
            QUIZ("Which of these is a statement?",
                 ["Close the window.", "Is the market open today?", "Mount Cameroon is in the South West Region.", "What a beautiful day!"], 2,
                 "It can be checked as true or false (it is true), so it is a statement.",
                 hint="Ask of each sentence: can it be called true or false?",
                 feedback=["This is a command. It is neither true nor false.",
                           "This is a question. It has no truth value.", "",
                           "This is an exclamation. It cannot be true or false."]),
            H("Common mistakes"),
            MISTAKE("Negating “all” as “none”",
                    "The negation of “All boys like football” is “Not all boys like football” (some boy does not). "
                    "“No boy likes football” says much more and is wrong."),
            MISTAKE("Treating “or” as “one but not both”",
                    r"$p \vee q$ is true when both are true. It is false only when both are false."),
            MISTAKE(r"Writing “neither $p$ nor $q$” as $\sim p \vee \sim q$",
                    r"“Neither … nor” means both are false: $\sim p \wedge \sim q$. "
                    r"$\sim p \vee \sim q$ only says that at least one is false."),
            QUIZ(r"$p$ is true and $q$ is false. Which compound statement is true?",
                 [r"$p \wedge q$", r"$\sim p$", r"$\sim p \vee q$", r"$p \vee q$"], 3,
                 r"$p \vee q$ needs at least one part true, and $p$ is true.",
                 hint=r"Work out each one: $\wedge$ needs both true, $\vee$ needs at least one.",
                 feedback=[r"$q$ is false, so $p \wedge q$ is false.",
                           r"$p$ is true, so $\sim p$ is false.",
                           r"$\sim p$ is F and $q$ is F, so $\sim p \vee q$ is F.", ""]),
            H("Practice questions"),
            PQ("Write the negation of each statement: (a) Bafoussam is in the West Region. (b) All the taxis are yellow. (c) Some mangoes are ripe.",
               "(a) Bafoussam is not in the West Region. "
               "(b) Not all the taxis are yellow (at least one taxi is not yellow). "
               "(c) No mangoes are ripe."),
            PQ(r"$p$ is true, $q$ is false and $r$ is true. Find the truth value of (a) $\sim p \vee r$ (b) $p \wedge \sim r$ (c) $\sim(q \vee r)$.",
               r"(a) $\sim p$ is F, F $\vee$ T is **T**. (b) $\sim r$ is F, T $\wedge$ F is **F**. "
               r"(c) $q \vee r$ is T, so $\sim(q \vee r)$ is **F**."),
            PQ(r"Let $p$: “Ewane is a farmer” and $q$: “Ewane lives in Foumbot”. "
               r"(a) Write $p \wedge \sim q$ in words. (b) Write “Ewane is not a farmer or he lives in Foumbot” in symbols.",
               r"(a) Ewane is a farmer and he does not live in Foumbot. (b) $\sim p \vee q$."),
            H("Summary"),
            SUM("A statement is a sentence that is either true or false, never both.",
                r"$\sim p$ has the opposite truth value to $p$. The negation of “all …” is “not all …”.",
                r"$p \wedge q$ (and) is true only when both are true.",
                r"$p \vee q$ (or) is false only when both are false.",
                r"“But” means $\wedge$; “neither $p$ nor $q$” is $\sim p \wedge \sim q$."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="Logic",
        title="Truth tables and implication",
        slug="truth-tables-and-implication",
        minutes=24,
        summary="Use the implication p ⇒ q and the equivalence p ⇔ q, build truth tables column by column, and recognise tautologies and equivalent statements.",
        objectives=[
            "State when p ⇒ q and p ⇔ q are true or false",
            "Build a truth table with 4 rows (two statements) or 8 rows (three statements)",
            "Use a truth table to show that two statements are equivalent",
            "Recognise a tautology and a contradiction",
        ],
        key_concepts=["Implication", "Equivalence (if and only if)", "Truth table", "Equivalent statements", "Tautology", "Contradiction"],
        blocks=[
            H("Introduction"),
            T("A father in Kumba tells his son: “If you pass the GCE, I will give you 5 000 FCFA.” "
              "When has the father broken his promise? Only if the son passes and does not get the money."),
            T(r"This is the idea behind the **implication** $p \Rightarrow q$. In the previous lesson you met $\sim$, $\wedge$ and $\vee$. "
              "Now you will add $\\Rightarrow$ and $\\Leftrightarrow$ and set everything out in truth tables."),
            D(r"$p \Rightarrow q$ is read “if $p$ then $q$” or “$p$ implies $q$”. $p$ is the **hypothesis** and $q$ is the **conclusion**. "
              r"$p \Rightarrow q$ is false **only** when $p$ is true and $q$ is false. In every other case it is true.",
              title="Definition: implication"),
            D(r"$p \Leftrightarrow q$ is read “$p$ if and only if $q$”. It is true when $p$ and $q$ have the **same** truth value, "
              r"and false when they differ. It means $(p \Rightarrow q) \wedge (q \Rightarrow p)$.",
              title="Definition: equivalence (biconditional)"),
            H("Truth tables"),
            T("A **truth table** lists every possible combination of truth values. "
              "With two statements there are $2^2 = 4$ rows; with three statements there are $2^3 = 8$ rows. "
              "Always list the rows in the same order so you can compare columns."),
            CODE("""
p   q   | p ∧ q   p ∨ q   p ⇒ q   p ⇔ q
T   T   |   T       T       T       T
T   F   |   F       T       F       F
F   T   |   F       T       T       F
F   F   |   F       F       T       T
""", "text", title="The basic truth tables", caption="Learn these four columns by heart."),
            TIP(r"Remember $p \Rightarrow q$ as the promise: it is broken only in the row T, F. "
                r"If $p$ is false (the son fails), the promise is not broken, so $p \Rightarrow q$ is true."),
            EX("Worked example 1: building a truth table", intro=r"Complete a truth table for $\sim p \vee q$ and compare it with $p \Rightarrow q$.", steps=[
                S("List the rows for $p$ and $q$", text="$p$: T, T, F, F. $q$: T, F, T, F."),
                S("Negate $p$", text=r"$\sim p$: F, F, T, T."),
                S("“Or” is true if at least one part is true", text=r"$\sim p \vee q$: T, F, T, T."),
                S("Compare", text=r"$p \Rightarrow q$ is also T, F, T, T. The two statements are **equivalent**: they have identical columns."),
            ]),
            D(r"Two statements are **equivalent** if their truth-table columns are identical. "
              r"A **tautology** is a statement that is true in every row. A **contradiction** is false in every row.",
              title="Definition: equivalent, tautology, contradiction",
              note=r"$p \vee \sim p$ is a tautology. $p \wedge \sim p$ is a contradiction."),
            EX("Worked example 2: a tautology", intro=r"Show that $[(p \Rightarrow q) \wedge p] \Rightarrow q$ is a tautology.", steps=[
                S("Rows", text="$p$: T, T, F, F. $q$: T, F, T, F."),
                S(r"Column for $p \Rightarrow q$", text="T, F, T, T."),
                S(r"Column for $(p \Rightarrow q) \wedge p$", text="T, F, F, F (both parts true only in row 1)."),
                S(r"Final column, $\ldots \Rightarrow q$", text="Row 1: T ⇒ T is T. Rows 2–4 start with F, so they are T. Column: T, T, T, T."),
                S("Conclusion", text="True in every row, so it is a tautology."),
            ]),
            QUIZ(r"$p \Rightarrow q$ is false in exactly one row. Which one?",
                 ["$p$ false, $q$ true", "$p$ true, $q$ false", "$p$ false, $q$ false", "$p$ true, $q$ true"], 1,
                 "The promise is broken only when the hypothesis is true and the conclusion is false.",
                 hint="Think of the promise: when is it broken?",
                 feedback=[r"With $p$ false, the implication is true whatever $q$ is.", "",
                           r"With $p$ false, the implication is true.",
                           r"T $\Rightarrow$ T is true: the promise was kept."]),
            EX("Worked example 3: a table with three statements", intro=r"Complete a truth table for $(p \wedge q) \Rightarrow r$.", steps=[
                S("8 rows", text="$p$: T, T, T, T, F, F, F, F. $q$: T, T, F, F, T, T, F, F. $r$: T, F, T, F, T, F, T, F."),
                S(r"Column for $p \wedge q$", text="T, T, F, F, F, F, F, F."),
                S(r"Final column", text=r"Only row 2 has T $\Rightarrow$ F. Column: T, F, T, T, T, T, T, T."),
            ]),
            TIP("For 8 rows: the first column is 4 T then 4 F, the second alternates in pairs, the third alternates T, F."),
            H("Common mistakes"),
            MISTAKE("Thinking an implication is false when $p$ is false",
                    r"If $p$ is false, $p \Rightarrow q$ is **true**, whatever $q$ is. Only T $\Rightarrow$ F is false."),
            MISTAKE(r"Mixing up $\Rightarrow$ and $\Leftrightarrow$",
                    r"In row F, T: $p \Rightarrow q$ is T but $p \Leftrightarrow q$ is F, because the truth values differ."),
            MISTAKE("Skipping columns",
                    r"Build a table one small piece at a time: negations first, then brackets, then the main connective."),
            QUIZ("How many rows does a truth table with three statements $p$, $q$ and $r$ need?",
                 ["3", "6", "9", "8"], 3,
                 r"Each statement doubles the number of rows: $2^3 = 8$.",
                 hint="Two statements need 4 rows. What happens when you add a third?",
                 feedback=["One row per statement is not enough: you need every combination.",
                           r"$2 \times 3 = 6$ is not right; the rows double each time.",
                           r"$3^2 = 9$ swaps the base and the power. Use $2^3$.", ""]),
            H("Practice questions"),
            PQ(r"$p$ is true, $q$ is false and $r$ is true. Find the truth value of (a) $(p \wedge q) \Rightarrow r$ (b) $p \Rightarrow (q \wedge r)$ (c) $q \Leftrightarrow \sim r$.",
               r"(a) $p \wedge q$ is F, and F $\Rightarrow$ T is **T**. "
               r"(b) $q \wedge r$ is F, and T $\Rightarrow$ F is **F**. "
               r"(c) $\sim r$ is F, and F $\Leftrightarrow$ F is **T** (same truth values)."),
            PQ(r"Copy and complete a truth table for $p \wedge \sim q$.",
               r"$p$: T, T, F, F. $q$: T, F, T, F. $\sim q$: F, T, F, T. $p \wedge \sim q$: F, T, F, F. "
               r"It is true only when $p$ is true and $q$ is false."),
            PQ(r"Use a truth table to show that $(p \Rightarrow q) \wedge (q \Rightarrow p)$ is equivalent to $p \Leftrightarrow q$.",
               r"$p \Rightarrow q$: T, F, T, T. $q \Rightarrow p$: T, T, F, T. Their conjunction: T, F, F, T. "
               r"$p \Leftrightarrow q$: T, F, F, T. The columns are identical, so the statements are equivalent."),
            PQ(r"Is $p \Rightarrow (p \vee q)$ a tautology? Give a reason.",
               r"$p \vee q$: T, T, T, F. $p \Rightarrow (p \vee q)$: T, T, T, T (rows 3 and 4 start with F). "
               r"It is true in every row, so it is a tautology."),
            H("Summary"),
            SUM(r"$p \Rightarrow q$ is false only when $p$ is true and $q$ is false.",
                r"$p \Leftrightarrow q$ is true when $p$ and $q$ have the same truth value.",
                "A truth table has 4 rows for two statements and 8 rows for three; build it column by column.",
                "Statements with identical columns are equivalent.",
                "A tautology is true in every row; a contradiction is false in every row."),
        ],
    ),
    lesson(
        module=MODULE,
        topic="Logic",
        title="Converse, inverse, contrapositive and valid arguments",
        slug="converse-inverse-contrapositive-and-valid-arguments",
        minutes=25,
        summary="Write the converse, inverse and contrapositive of an implication, know which ones are equivalent, and decide whether a logical deduction is valid.",
        objectives=[
            "Write the converse, inverse and contrapositive of p ⇒ q",
            "Know that an implication and its contrapositive are equivalent, but the converse may not be",
            "Use the valid patterns of deduction to draw conclusions",
            "Recognise invalid arguments and give a counter-example",
        ],
        key_concepts=["Converse", "Inverse", "Contrapositive", "Premise", "Conclusion", "Valid argument", "Counter-example"],
        blocks=[
            H("Introduction"),
            T("“If it rains, the road to Kumba is muddy. The road is muddy. So it rained.” Is this good reasoning? "
              "Many people think so, but it is not. In this lesson you will learn how to tell valid reasoning from invalid reasoning."),
            T(r"In the previous lesson you met the implication $p \Rightarrow q$ and truth tables. Both are the tools you need here."),
            D(r"For the implication $p \Rightarrow q$: the **converse** is $q \Rightarrow p$; the **inverse** is $\sim p \Rightarrow \sim q$; "
              r"the **contrapositive** is $\sim q \Rightarrow \sim p$.",
              title="Definition: converse, inverse, contrapositive",
              note="Converse: swap. Inverse: negate both. Contrapositive: swap and negate both."),
            EX("Worked example 1: the three related statements", intro=(
                "Write the converse, inverse and contrapositive of “If a number is divisible by 4, then it is even”. "
                "Say whether each is true or false."), steps=[
                S("Name the parts", text=r"$p$: a number is divisible by 4. $q$: it is even. The statement $p \Rightarrow q$ is true."),
                S("Converse $q \\Rightarrow p$", text="If a number is even, then it is divisible by 4. **False**: 6 is even but not divisible by 4."),
                S("Inverse $\\sim p \\Rightarrow \\sim q$", text="If a number is not divisible by 4, then it is not even. **False**: 6 again."),
                S("Contrapositive $\\sim q \\Rightarrow \\sim p$", text="If a number is not even, then it is not divisible by 4. **True**."),
            ]),
            EX("Worked example 2: proving the equivalence with a truth table",
               intro=r"Show that $p \Rightarrow q$ and its contrapositive $\sim q \Rightarrow \sim p$ are equivalent.", steps=[
                S("Rows", text="$p$: T, T, F, F. $q$: T, F, T, F."),
                S(r"$p \Rightarrow q$", text="T, F, T, T."),
                S(r"$\sim q$ and $\sim p$", text=r"$\sim q$: F, T, F, T. $\sim p$: F, F, T, T."),
                S(r"$\sim q \Rightarrow \sim p$", text="Row 2 is T ⇒ F, so F; all others are T. Column: T, F, T, T."),
                S("Compare", text="The columns are identical, so the statements are equivalent."),
            ]),
            KEY("Which statements agree?", "From truth tables:", cards=[
                ["Always agree", r"$p \Rightarrow q$ and its contrapositive $\sim q \Rightarrow \sim p$."],
                ["Always agree", r"The converse $q \Rightarrow p$ and the inverse $\sim p \Rightarrow \sim q$."],
                ["May disagree", "A statement and its converse. A true statement can have a false converse."],
            ]),
            QUIZ("What is the contrapositive of “If a number is divisible by 4, then it is even”?",
                 ["If a number is even, then it is divisible by 4.",
                  "If a number is not even, then it is not divisible by 4.",
                  "If a number is not divisible by 4, then it is not even.",
                  "A number is divisible by 4 and it is not even."], 1,
                 r"The contrapositive of $p \Rightarrow q$ is $\sim q \Rightarrow \sim p$: swap the parts and negate both.",
                 hint="The contrapositive does two things to the parts. What are they?",
                 feedback=["This is the converse: the parts are swapped but not negated.", "",
                           "This is the inverse: the parts are negated but not swapped.",
                           r"This is the negation of the implication ($p \wedge \sim q$), not its contrapositive."]),
            H("Valid arguments"),
            D(r"An **argument** has one or more **premises** (statements we accept) and a **conclusion**. "
              r"It is **valid** if the conclusion must be true whenever all the premises are true.",
              title="Definition: valid argument",
              note="To show an argument is not valid, find a **counter-example**: a case where the premises are true but the conclusion is false."),
            KEY("Valid and invalid patterns", r"Here $p \Rightarrow q$ is always the first premise.", cards=[
                ["Valid", r"$p \Rightarrow q$ and $p$. Conclude $q$."],
                ["Valid", r"$p \Rightarrow q$ and $\sim q$. Conclude $\sim p$ (the contrapositive at work)."],
                ["Valid", r"$p \Rightarrow q$ and $q \Rightarrow r$. Conclude $p \Rightarrow r$ (a chain)."],
                ["Not valid", r"$p \Rightarrow q$ and $q$, so $p$. Or: $p \Rightarrow q$ and $\sim p$, so $\sim q$."],
            ]),
            T(r"A sentence like “All Form 5 students write the GCE” is an implication too: "
              r"“If a person is a Form 5 student, then that person writes the GCE.”"),
            EX("Worked example 3: is the deduction valid?", intro=(
                "Premise 1: If it rains, the road to Kumba is muddy. Premise 2: The road to Kumba is muddy. "
                "Conclusion: It rained. Is this valid?"), steps=[
                S("Write it in symbols", text=r"$p$: it rains. $q$: the road is muddy. We have $p \Rightarrow q$ and $q$, and conclude $p$."),
                S("Compare with the patterns", text="This is the invalid pattern: reasoning backwards from $q$ to $p$."),
                S("Give a counter-example", text="The road could be muddy because a water pipe burst, with no rain."),
                S("Decide", text="The premises can be true while the conclusion is false. The deduction is **not valid**."),
            ]),
            EX("Worked example 4: drawing valid conclusions", intro=(
                "Premise 1: If the rains come early, farmers in Foumbot plant maize in March. "
                "Premise 2: If farmers plant maize in March, there is fresh maize in the market by June. "
                "(a) What can you conclude from the two premises? (b) Fresh maize is **not** in the market by June. What follows?"), steps=[
                S("Name the parts", text="$p$: rains come early. $q$: maize planted in March. $r$: fresh maize by June."),
                S("(a) Chain the premises", math=r"p \Rightarrow q,\ q \Rightarrow r \;\therefore\; p \Rightarrow r",
                  text="If the rains come early, there is fresh maize in the market by June."),
                S(r"(b) Use $\sim r$ with $q \Rightarrow r$", text="Maize was not planted in March."),
                S(r"(b) Use $\sim q$ with $p \Rightarrow q$", text="So the rains did not come early."),
            ]),
            H("Common mistakes"),
            MISTAKE("Confusing the converse with the contrapositive",
                    r"The contrapositive swaps **and** negates: $\sim q \Rightarrow \sim p$. The converse only swaps: $q \Rightarrow p$."),
            MISTAKE("Assuming the converse is true",
                    "“If $x = 3$, then $x^2 = 9$” is true, but “If $x^2 = 9$, then $x = 3$” is false, because $x = -3$ also works."),
            MISTAKE("Reasoning backwards from the conclusion",
                    r"Knowing $p \Rightarrow q$ and $q$ does **not** let you conclude $p$. Knowing $p \Rightarrow q$ and $\sim p$ does not give $\sim q$."),
            QUIZ("Premise 1: If a student studies, she passes. Premise 2: Mbah did not pass. What can be validly concluded?",
                 ["Mbah studied.", "No conclusion can be drawn.", "Mbah will pass next year.", "Mbah did not study."], 3,
                 r"From $p \Rightarrow q$ and $\sim q$ we can conclude $\sim p$.",
                 hint=r"Let $p$ be “Mbah studies” and $q$ be “Mbah passes”. Write Premise 2 in symbols.",
                 feedback=["If Mbah had studied, Premise 1 says she would have passed. That contradicts Premise 2.",
                           r"From $p \Rightarrow q$ and $\sim q$ we can always conclude $\sim p$.",
                           "Nothing in the premises is about next year.", ""]),
            H("Practice questions"),
            PQ("Write the converse, inverse and contrapositive of “If a shape is a square, then it has four sides”. Which of them are true?",
               "Converse: If a shape has four sides, then it is a square (false: a rectangle). "
               "Inverse: If a shape is not a square, then it does not have four sides (false: a rectangle). "
               "Contrapositive: If a shape does not have four sides, then it is not a square (true)."),
            PQ("Premise 1: All Form 5 students write the GCE. Premise 2: Ngozi is a Form 5 student. "
               "(a) What can you conclude? (b) If instead Premise 2 were “Ngozi writes the GCE”, could you conclude that Ngozi is a Form 5 student?",
               "(a) Ngozi writes the GCE. This is valid. "
               "(b) No. Other people, for example private candidates, may also write the GCE. "
               r"From $p \Rightarrow q$ and $q$ we cannot conclude $p$."),
            PQ(r"Show that “If $x = 3$, then $x^2 = 9$” is true, but its converse is false.",
               r"If $x = 3$ then $x^2 = 9$, so the statement is true. "
               r"The converse is “If $x^2 = 9$, then $x = 3$”. It is false, because $x = -3$ also gives $x^2 = 9$."),
            PQ("Is this argument valid? “If a trader sells oil, she sells rice. Ma Ngono does not sell oil. So she does not sell rice.”",
               r"No. In symbols: $p \Rightarrow q$ and $\sim p$, so $\sim q$. This is an invalid pattern. "
               "Counter-example: Ma Ngono may sell rice but not oil; both premises are then true and the conclusion is false."),
            H("Summary"),
            SUM(r"For $p \Rightarrow q$: converse $q \Rightarrow p$, inverse $\sim p \Rightarrow \sim q$, contrapositive $\sim q \Rightarrow \sim p$.",
                "An implication and its contrapositive always have the same truth value; the converse may not.",
                r"Valid: from $p \Rightarrow q$ and $p$, conclude $q$; from $p \Rightarrow q$ and $\sim q$, conclude $\sim p$; chain $p \Rightarrow q$, $q \Rightarrow r$ to get $p \Rightarrow r$.",
                r"Not valid: from $p \Rightarrow q$ and $q$, concluding $p$; or from $\sim p$, concluding $\sim q$.",
                "To show an argument is not valid, give a counter-example."),
        ],
    ),
]
