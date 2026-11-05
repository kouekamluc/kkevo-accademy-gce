"""Form 5 Logic (GCE O Level 0590), module "Other Types of Arguments" (syllabus 1.8.1-1.8.6).
Draft content: check against the official syllabus and your teacher's textbook.

Every validity claim here was checked by brute-force truth tables (all assignments of T and F)."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "Other Types of Arguments"

LESSONS = [
    # ------------------------------------------------------------------ 1. The enthymeme
    lesson(
        module=MODULE,
        topic="The enthymeme",
        title="The enthymeme: arguments with a missing part",
        slug="oth-the-enthymeme",
        minutes=18,
        summary="An enthymeme is an argument with one part left unstated. Learn to find the missing premise or conclusion, to name the order of the enthymeme and to test the argument once the gap is filled.",
        objectives=[
            "Define an enthymeme and say why people use them in everyday speech",
            "Find the unstated premise or conclusion of an argument",
            "Name first-order, second-order and third-order enthymemes",
            "Test an enthymeme by writing it out in full",
        ],
        key_concepts=["Enthymeme", "Suppressed premise", "Suppressed conclusion", "First-order enthymeme", "Second-order enthymeme", "Third-order enthymeme"],
        blocks=[
            H("Introduction"),
            T("A mother in Bamenda says to her son: \"Take an umbrella, because it is the rainy season.\" She did not say everything. "
              "She did not say \"When it is the rainy season, it often rains.\" She did not need to. You supplied that idea yourself."),
            T("People speak like this all the time. We leave out what everybody already knows. "
              "In Logic, an argument with a part left out is called an **enthymeme** (say: EN-thi-meem)."),
            D("An **enthymeme** is an argument in which one part is **not stated**: a premise or the conclusion is left in the mind of the speaker and the hearer. "
              "The word comes from Greek and means something like \"kept in the mind\".",
              title="Definition: enthymeme",
              note="The unstated part is called the suppressed (hidden) part. A premise is a reason. The conclusion is what the reasons support."),
            H("Why do people use enthymemes?"),
            T("There are three common reasons. First, speed: we do not repeat what is obvious. "
              "Second, style: a short argument is stronger than a long one. "
              "Third, sometimes the hidden part is hidden because it is doubtful. A speaker may hope that you will not notice it."),
            TIP("A hidden premise is not always a fault. But an argument is only as good as ALL its premises, including the ones nobody said. "
                "To test an enthymeme, first write it out in full."),
            H("Finding the missing part"),
            KEY("Three steps", "Use these steps with any argument that seems to have a gap.", cards=[
                ["1. Find the conclusion", "Look for words like so, therefore, because, since, hence."],
                ["2. Count the premises", "A syllogism has two premises. Which one is missing, or is the conclusion missing?"],
                ["3. Fill the gap", "Choose the missing statement that makes the argument valid and is a fair reading of what the speaker meant."],
            ]),
            T("The traditional textbooks (Copi, Hurley and others) mostly describe enthymemes as **syllogisms** with a missing part. "
              "A syllogism has a major premise, a minor premise and a conclusion. The order of the enthymeme tells you which part is missing."),
            D("A **first-order enthymeme** is a syllogism whose **major premise** is left out. "
              "A **second-order enthymeme** is a syllogism whose **minor premise** is left out. "
              "A **third-order enthymeme** is a syllogism whose **conclusion** is left out.",
              title="Definition: the three orders",
              note="Textbooks do not all use these names or this numbering. If your teacher's book uses a different system, follow your book."),
            EX("Worked example 1: a first-order enthymeme", intro="\"Nkemi is a nurse, so she has studied biology.\" Find the missing premise.", steps=[
                S("Find the conclusion", text="Nkemi has studied biology."),
                S("State the premise that is given", text="Nkemi is a nurse. This is the minor premise: it speaks about Nkemi."),
                S("Find what is missing", text="A general rule that joins them: All nurses are people who have studied biology. This is the major premise."),
                S("Write the full syllogism", text="All nurses are people who have studied biology. Nkemi is a nurse. So Nkemi has studied biology."),
                S("Name the order", text="The major premise was left out, so this is a first-order enthymeme. The full argument is valid. Whether it is sound depends on whether the missing premise is true."),
            ]),
            EX("Worked example 2: a second-order enthymeme", intro="\"Everything that pollutes the river should be stopped, so the dumping of waste at the quay should be stopped.\"", steps=[
                S("Find the conclusion", text="The dumping of waste at the quay should be stopped."),
                S("Find the given premise", text="Everything that pollutes the river should be stopped. This is the general rule, so it is the major premise."),
                S("Find what is missing", text="The dumping of waste at the quay pollutes the river. This is the minor premise."),
                S("Name the order", text="The minor premise was left out: a second-order enthymeme. Now we can see exactly what to question. Does the dumping really pollute the river?"),
            ]),
            EX("Worked example 3: a third-order enthymeme", intro="\"A person who tells lies cannot be trusted with the school money, and Fon tells lies.\"", steps=[
                S("Find the premises", text="Major: A person who tells lies cannot be trusted with the school money. Minor: Fon tells lies."),
                S("Find what is missing", text="No conclusion is stated. It is Fon cannot be trusted with the school money."),
                S("Name the order", text="The conclusion was left out: a third-order enthymeme. Here the speaker lets the hearer draw the conclusion. That can be a polite way to accuse someone."),
            ]),
            MISTAKE("Filling the gap with a false or unfair statement",
                    "Do not choose a missing premise just because it makes the argument valid. Choose the one the speaker most likely meant. "
                    "\"Ako is rich, so he is generous\" needs the premise \"All rich people are generous\". That premise is false, so the argument is unsound, even though the full syllogism is valid."),
            MISTAKE("Thinking a short argument is a bad argument",
                    "An enthymeme is not a fallacy. It is a normal way of speaking. Write the full argument, then test it for validity and for true premises."),
            H("Enthymemes in everyday speech"),
            T("\"He failed because he did not revise.\" Hidden: People who do not revise fail. "
              "\"It is a market day, so the road will be full.\" Hidden: On market days the road is full. "
              "Notice that the hidden premises are general statements that may have exceptions. Ask yourself: is this true always, or only usually?"),
            QUIZ("\"All footballers must train regularly, so Eto must train regularly.\" What is the missing part?",
                 ["The conclusion", "The major premise", "The minor premise: Eto is a footballer", "A second conclusion"], 2,
                 "The conclusion (Eto must train regularly) and the major premise (all footballers must train regularly) are both given. Missing: Eto is a footballer. This is a second-order enthymeme.",
                 hint="Which of the three parts of a syllogism is not in the sentence?",
                 feedback=["The conclusion is stated: after the word so.", "The major premise is the general rule about all footballers. It is stated.", "", "An argument that has been given one conclusion needs no second one."]),
            QUIZ("What is a third-order enthymeme?",
                 ["A syllogism with the major premise left out", "A syllogism with the minor premise left out", "A syllogism with three conclusions", "A syllogism with the conclusion left out"], 3,
                 "In the usual textbook system the order tells you what is left out: first order is the major premise, second order is the minor premise, third order is the conclusion.",
                 hint="Think of the order as the position of the part: first major premise, second minor premise, third conclusion.",
                 feedback=["That is a first-order enthymeme.", "That is a second-order enthymeme.", "A syllogism has only one conclusion.", ""]),
            PQ("Write out in full: \"Mimi is a Cameroonian, so she can vote at 20.\" Which part is missing and what is the order?",
               "The conclusion and one premise are given. The missing part is the major premise: All Cameroonians (of the right age and registered) can vote. Without the words in brackets the premise is too strong, so it needs care. Missing major premise: first-order enthymeme. Full syllogism: All Cameroonians of voting age can vote. Mimi is a Cameroonian of voting age. So Mimi can vote."),
            PQ("\"All good drivers obey the speed limit, and Tabi is a good driver.\" What is the unstated conclusion and what is the order?",
               "Conclusion: Tabi obeys the speed limit. Both premises are given and the conclusion is left out: a third-order enthymeme."),
            PQ("\"That meat is not fresh, because it smells bad.\" Give the hidden premise and say whether it is always true.",
               "Hidden premise: Meat that smells bad is not fresh. It is usually true, but some foods (some cheeses and fermented foods) smell strong and are fine. So the argument is strong but the premise has exceptions. Always ask whether the hidden premise is true in every case."),
            TIP("In Paper 1 you may be asked to name the missing part or the order of an enthymeme. In Paper 2 you may be asked to write an argument in full and test it. Always show the full syllogism.",
                title="Exam link"),
            SUM("An enthymeme is an argument with one part left unstated.",
                "First order: major premise missing. Second order: minor premise missing. Third order: conclusion missing (check your own textbook for its names).",
                "To test an enthymeme, write it out in full and check the validity of the full argument.",
                "A valid argument is sound only if all the premises are true, including the hidden one.",
                "Enthymemes are normal in speech, but hidden premises should be examined."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Hypothetical syllogism: valid forms
    lesson(
        module=MODULE,
        topic="The hypothetical syllogism",
        title="Valid hypothetical syllogisms: modus ponens, modus tollens and chains",
        slug="oth-hypothetical-syllogisms-valid-forms",
        minutes=22,
        summary="Learn the mixed hypothetical syllogism (affirming the antecedent and denying the consequent) and the pure hypothetical syllogism (a chain of conditionals), and prove each valid by truth table.",
        objectives=[
            "Identify the antecedent and the consequent of a conditional statement",
            "State and use modus ponens and modus tollens",
            "Use the pure hypothetical syllogism (a chain of conditionals)",
            "Prove each form valid with a truth table",
        ],
        key_concepts=["Conditional", "Antecedent", "Consequent", "Mixed hypothetical syllogism", "Modus ponens", "Modus tollens", "Pure hypothetical syllogism"],
        blocks=[
            H("Introduction"),
            T("A farmer in Dschang reasons: \"If the rains come in March, I plant maize in March. The rains have come. So I plant maize.\" "
              "Her argument is built around an **if ... then ...** statement. Arguments like this are very common: in farming, in school rules, in law and in science."),
            T("In the earlier module you learned the symbol ⊃ (horseshoe) for **material implication**. p ⊃ q is read \"if p then q\". "
              "It is false only in one case: p true and q false. This lesson shows the arguments built on it."),
            D("A **hypothetical (conditional) statement** has the form \"If p, then q\", written p ⊃ q. "
              "The part after if is the **antecedent** (p). The part after then is the **consequent** (q).",
              title="Definition: antecedent and consequent",
              note="Example: If the rains come, the maize grows. Antecedent: the rains come. Consequent: the maize grows."),
            D("A **hypothetical syllogism** is an argument that has a conditional statement as one or both premises. "
              "A **mixed** hypothetical syllogism has one conditional premise and one ordinary (categorical) premise. "
              "A **pure** hypothetical syllogism has conditional premises only.",
              title="Definition: hypothetical syllogism"),
            H("Modus ponens: affirming the antecedent"),
            T("The Latin name **modus ponens** means \"the way that affirms\". The second premise says the antecedent is true, and the conclusion says the consequent is true."),
            CODE("p ⊃ q\np\n-----\nq", "text", title="Modus ponens"),
            EX("Worked example 1: modus ponens", intro="If a student scores 50 or more, she passes. Ngo scored 62. So Ngo passes.", steps=[
                S("Write the symbols", text="p: Ngo scores 50 or more. q: Ngo passes. Premise 1: p ⊃ q. Premise 2: p. Conclusion: q."),
                S("Check the form", text="The second premise affirms (says yes to) the antecedent. This is modus ponens."),
            ]),
            H("Modus tollens: denying the consequent"),
            T("**Modus tollens** means \"the way that denies\". The second premise says the consequent is false, and the conclusion says the antecedent is false."),
            CODE("p ⊃ q\n~q\n-----\n~p", "text", title="Modus tollens"),
            EX("Worked example 2: modus tollens", intro="If the generator is working, the light is on. The light is not on. So the generator is not working.", steps=[
                S("Write the symbols", text="p: the generator is working. q: the light is on. Premises: p ⊃ q and ~q. Conclusion: ~p."),
                S("Check the form", text="The second premise denies (says no to) the consequent. This is modus tollens."),
                S("Why it works", text="If the generator were working, the light would be on. It is not on. So the generator cannot be working."),
            ]),
            H("Proof by truth table"),
            T("A form is **valid** if there is no row in the truth table where all the premises are true and the conclusion is false. Look at modus ponens first."),
            CODE("p q | p ⊃ q | p | q\nT T |   T   | T | T   <- both premises true, conclusion true\nT F |   F   | T | F\nF T |   T   | F | T\nF F |   T   | F | F", "text", title="Modus ponens"),
            T("Only the first row has both premises true. There the conclusion q is true. So modus ponens is valid. Now modus tollens."),
            CODE("p q | p ⊃ q | ~q | ~p\nT T |   T   |  F |  F\nT F |   F   |  T |  F\nF T |   T   |  F |  T\nF F |   T   |  T |  T   <- both premises true, conclusion true", "text", title="Modus tollens"),
            T("Only the last row has both premises true. There ~p is true. So modus tollens is valid."),
            H("The pure hypothetical syllogism: a chain"),
            D("The **pure hypothetical syllogism** links two conditionals. The consequent of the first is the antecedent of the second. The conclusion is a conditional.",
              title="Definition: pure hypothetical syllogism"),
            CODE("p ⊃ q\nq ⊃ r\n-----\np ⊃ r", "text", title="Chain argument"),
            T("Example: If I study, I pass. If I pass, I get my certificate. So if I study, I get my certificate."),
            CODE("p q r | p ⊃ q | q ⊃ r | p ⊃ r\nT T T |   T   |   T   |   T   <- both premises true\nT T F |   T   |   F   |   F\nT F T |   F   |   T   |   T\nT F F |   F   |   T   |   F\nF T T |   T   |   T   |   T   <- both premises true\nF T F |   T   |   F   |   T\nF F T |   T   |   T   |   T   <- both premises true\nF F F |   T   |   T   |   T   <- both premises true", "text", title="Truth table: 8 rows, because 2 to the power 3 is 8"),
            T("In every row where both premises are true, the conclusion is true. So the chain is valid."),
            TIP("A chain can have more than two links: if p then q, if q then r, if r then s, so if p then s. Check that each link joins to the next."),
            MISTAKE("Breaking the chain",
                    "Both conditionals must join in the middle. \"If p then q\" and \"If r then q\" do not give \"If p then r\". A truth table finds a counterexample: p true, q true, r false."),
            MISTAKE("Using the wrong word for the second premise",
                    "Modus ponens affirms the ANTECEDENT. Modus tollens denies the CONSEQUENT. Mixing them gives the fallacies of the next lesson."),
            QUIZ("If the tank is full, the pump stops. The pump has not stopped. What follows by a valid form?",
                 ["The tank is full", "The tank is not full", "The tank may or may not be full", "The pump is broken"], 1,
                 "p: the tank is full. q: the pump stops. We have p ⊃ q and ~q. By modus tollens, ~p: the tank is not full.",
                 hint="The second premise denies the consequent. Which form is that?",
                 feedback=["That would affirm the antecedent. Nothing in the premises says so.", "", "A valid form gives a definite conclusion here. Modus tollens applies.", "The premises say nothing about a broken pump."]),
            QUIZ("Which is a valid pure hypothetical syllogism?",
                 ["If p then q; if r then q; so if p then r", "If p then q; if q then r; so if p then r", "If p then q; if q then r; so if r then p", "If p then q; if r then s; so if p then s"], 1,
                 "Only the second joins the consequent of the first to the antecedent of the second, and concludes the outer parts.",
                 hint="Look for the link: the same letter must end the first conditional and begin the second.",
                 feedback=["The two conditionals share the consequent q, not a link. This form is invalid.", "", "The conclusion is the wrong way round. It reverses the chain.", "The two conditionals do not join."]),
            TIP("In Paper 1 you may be given an argument in words and asked to name its form, or given a form and asked whether it is valid. In Paper 2 you may be asked to prove validity with a truth table.",
                title="Exam link"),
            PQ("Write in symbols and name the form: \"If Tanyi studies, he will pass. Tanyi studies. So he will pass.\"",
               "p: Tanyi studies. q: he will pass. p ⊃ q, p, so q. This is modus ponens (affirming the antecedent). It is valid."),
            PQ("\"If it is a public holiday, the offices are closed. The offices are open. So it is not a public holiday.\" Name the form and say if it is valid.",
               "p: it is a public holiday. q: the offices are closed. p ⊃ q, ~q, so ~p. This is modus tollens (denying the consequent). It is valid."),
            PQ("Make a chain argument from: \"If the price of cocoa rises, farmers earn more.\" and \"If farmers earn more, they send more children to school.\"",
               "Conclusion: If the price of cocoa rises, farmers send more children to school. Form: p ⊃ q, q ⊃ r, so p ⊃ r. It is a valid pure hypothetical syllogism. (Whether the premises are true is a separate question.)"),
            SUM("A conditional p ⊃ q has an antecedent (p) and a consequent (q).",
                "Modus ponens: p ⊃ q, p, so q. Valid.",
                "Modus tollens: p ⊃ q, ~q, so ~p. Valid.",
                "The pure hypothetical syllogism (chain): p ⊃ q, q ⊃ r, so p ⊃ r. Valid.",
                "A truth table proves validity: no row has true premises and a false conclusion."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Hypothetical fallacies
    lesson(
        module=MODULE,
        topic="The hypothetical syllogism",
        title="Invalid hypothetical syllogisms: two fallacies to avoid",
        slug="oth-hypothetical-fallacies",
        minutes=20,
        summary="Learn the fallacies of affirming the consequent and denying the antecedent, see why a truth table and a counterexample show them invalid, and learn how to tell valid from invalid forms quickly.",
        objectives=[
            "Recognise the fallacy of affirming the consequent",
            "Recognise the fallacy of denying the antecedent",
            "Show that each is invalid with a truth table row or a counterexample",
            "Tell a valid conditional argument from an invalid one",
        ],
        key_concepts=["Affirming the consequent", "Denying the antecedent", "Counterexample", "Valid form", "Invalid form", "Necessary and sufficient"],
        blocks=[
            H("Introduction"),
            T("At a football match in Douala a fan says: \"If our striker plays, we win. We won. So our striker played.\" It sounds right. But the team may have won without him. "
              "The fan has mixed up two forms of reasoning. One is valid. This one is not."),
            T("In the last lesson you learned two valid conditional forms: modus ponens and modus tollens. "
              "Each has a look-alike that is **invalid**. Learning the look-alikes will protect you from bad reasoning."),
            H("Affirming the consequent"),
            D("The fallacy of **affirming the consequent** has the form: p ⊃ q, q, therefore p. "
              "The second premise affirms the consequent, and the conclusion claims the antecedent.",
              title="Definition: affirming the consequent"),
            CODE("p ⊃ q\nq\n-----\np      INVALID", "text", title="Affirming the consequent"),
            T("Why is it invalid? The conditional says that p is **enough** for q. It does not say that p is **needed** for q. q may be true for some other reason."),
            CODE("p q | p ⊃ q | q | p\nT T |   T   | T | T\nT F |   F   | F | T\nF T |   T   | T | F   <- both premises true, conclusion FALSE\nF F |   T   | F | F", "text", title="Counterexample row"),
            T("The third row gives a counterexample: p false and q true. Both premises are true, but the conclusion is false. One such row is enough to make the form invalid."),
            EX("Worked example 1: affirming the consequent", intro="If it is a goat, it has four legs. The animal has four legs. So it is a goat.", steps=[
                S("Symbols", text="p: it is a goat. q: it has four legs. Premises: p ⊃ q and q. Conclusion: p."),
                S("Name the form", text="The second premise affirms the consequent. This is the fallacy of affirming the consequent."),
                S("Find a counterexample", text="A cow has four legs and is not a goat. Both premises are true and the conclusion is false."),
            ]),
            H("Denying the antecedent"),
            D("The fallacy of **denying the antecedent** has the form: p ⊃ q, ~p, therefore ~q. "
              "The second premise denies the antecedent, and the conclusion denies the consequent.",
              title="Definition: denying the antecedent"),
            CODE("p ⊃ q\n~p\n-----\n~q     INVALID", "text", title="Denying the antecedent"),
            CODE("p q | p ⊃ q | ~p | ~q\nT T |   T   |  F |  F\nT F |   F   |  F |  T\nF T |   T   |  T |  F   <- both premises true, conclusion FALSE\nF F |   T   |  T |  T", "text", title="Counterexample row"),
            T("Again the third row (p false, q true) is a counterexample."),
            EX("Worked example 2: denying the antecedent", intro="If Ayuk works at the bank, he has a salary. Ayuk does not work at the bank. So he has no salary.", steps=[
                S("Symbols", text="p: Ayuk works at the bank. q: Ayuk has a salary. Premises: p ⊃ q and ~p. Conclusion: ~q."),
                S("Name the form", text="The second premise denies the antecedent. This is the fallacy of denying the antecedent."),
                S("Find a counterexample", text="Ayuk may teach at a school and have a salary. Both premises true, conclusion false."),
            ]),
            H("How to tell valid from invalid"),
            KEY("The four forms side by side", "Look at the second premise. It must connect to the conditional in the right way.", cards=[
                ["Valid: modus ponens", "Affirm the antecedent (p). Conclude the consequent (q)."],
                ["Valid: modus tollens", "Deny the consequent (~q). Conclude the denial of the antecedent (~p)."],
                ["Invalid: affirming the consequent", "Affirm the consequent (q). Conclude the antecedent (p). The arrow cannot be run backwards."],
                ["Invalid: denying the antecedent", "Deny the antecedent (~p). Conclude the denial of the consequent (~q). Wrong direction again."],
            ]),
            TIP("A quick test. The only valid moves go forward from the antecedent (modus ponens) or backward from a denied consequent (modus tollens). If you must go from the consequent to the antecedent by affirming, or from a denied antecedent to a denied consequent, the form is invalid. "
                "Then look for a counterexample to be sure."),
            T("Be careful with the word **if**. In everyday speech \"if\" is sometimes used to mean \"if and only if\" (p ≡ q). \"If you pay, you get the ticket\" is often understood as \"you get the ticket only when you pay\". "
              "With a biconditional p ≡ q, the reasoning from q back to p IS valid. In this course, unless the biconditional is stated, treat \"if\" as the ordinary conditional p ⊃ q."),
            MISTAKE("Trusting how natural the argument sounds",
                    "Both fallacies sound convincing because they are so common. Always ask: could the consequent be true for another reason? If so, affirming it proves nothing about the antecedent."),
            MISTAKE("Calling an invalid argument false",
                    "An invalid argument has a conclusion that does not follow. The conclusion may still be true by accident. Validity is about the link between premises and conclusion, not about the truth of the conclusion alone."),
            QUIZ("\"If the road is flooded, the bus is late. The bus is late. So the road is flooded.\" This is:",
                 ["modus ponens, valid", "modus tollens, valid", "affirming the consequent, invalid", "denying the antecedent, invalid"], 2,
                 "p ⊃ q, q, so p. The bus may be late for another reason, such as a breakdown. This is the fallacy of affirming the consequent.",
                 hint="Which part of the conditional is repeated in the second premise?",
                 feedback=["Modus ponens affirms the antecedent. Here the second premise is the consequent.", "Modus tollens denies the consequent. Here nothing is denied.", "", "Denying the antecedent would use a premise like: the road is not flooded."]),
            QUIZ("Which of these is VALID?",
                 ["If p then q; not p; so not q", "If p then q; q; so p", "If p then q; not q; so not p", "If p then q; p; so not q"], 2,
                 "Only the third is modus tollens. The first denies the antecedent, the second affirms the consequent, and the fourth contradicts the conditional.",
                 hint="One of these denies the consequent. Which?",
                 feedback=["That is denying the antecedent: invalid.", "That is affirming the consequent: invalid.", "", "If p and p ⊃ q are true, q must be true. This conclusion is the opposite."]),
            TIP("Paper 1 often gives an argument in words and asks you to name its form or say why it is invalid. In Paper 2 write the symbols, name the form, and give a counterexample or the truth table row.",
                title="Exam link"),
            PQ("\"If he is a thief, he is dishonest. He is not a thief. So he is not dishonest.\" Name the form and give a counterexample.",
               "p: he is a thief. q: he is dishonest. p ⊃ q, ~p, so ~q. Denying the antecedent: invalid. Counterexample: p false and q true. He is not a thief but he lies, so he is dishonest in another way."),
            PQ("Why is the form \"p ⊃ q, q, so p\" invalid? Use a truth table row.",
               "Take p false and q true. Then p ⊃ q is true (a false antecedent makes the conditional true) and q is true, but the conclusion p is false. Both premises true and conclusion false means the form is invalid."),
            PQ("A teacher says: \"If you cheat, you will be punished.\" A student concludes: \"I did not cheat, so I will not be punished.\" Is the reasoning valid? Explain.",
               "No. The student denies the antecedent (p ⊃ q, ~p, so ~q). The student could be punished for another offence, such as being late. The rule only says what happens if you cheat."),
            SUM("Affirming the consequent: p ⊃ q, q, so p. INVALID.",
                "Denying the antecedent: p ⊃ q, ~p, so ~q. INVALID.",
                "Each has a counterexample row: p false, q true. Both premises are true and the conclusion is false.",
                "The valid forms are modus ponens (affirm the antecedent) and modus tollens (deny the consequent).",
                "If \"if\" really means \"if and only if\" (p ≡ q), more arguments are valid. Use that only when it is stated."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Disjunctive syllogism
    lesson(
        module=MODULE,
        topic="The disjunctive syllogism",
        title="The disjunctive syllogism: either this or that",
        slug="oth-the-disjunctive-syllogism",
        minutes=20,
        summary="Learn the valid forms of the disjunctive syllogism (deny one alternative, affirm the other), the invalid form of affirming an alternative, and the difference between weak (inclusive) and strong (exclusive) disjunction.",
        objectives=[
            "Define a disjunction and its alternatives (disjuncts)",
            "Distinguish weak (inclusive) from strong (exclusive) disjunction",
            "State and use the valid disjunctive syllogism",
            "Explain why affirming an alternative is invalid when the disjunction is inclusive",
        ],
        key_concepts=["Disjunction", "Alternative (disjunct)", "Weak (inclusive) disjunction", "Strong (exclusive) disjunction", "Disjunctive syllogism", "Denying an alternative"],
        blocks=[
            H("Introduction"),
            T("A trader in Mokolo market says: \"Either the bus comes today or I travel on Friday. The bus did not come today. So I travel on Friday.\" "
              "This argument is built on an either ... or ... statement. In Logic such a statement is a **disjunction**."),
            D("A **disjunction** (or **alternation**) is a statement of the form \"p or q\", written p v q. "
              "The two parts are the **alternatives** (also called disjuncts).",
              title="Definition: disjunction",
              note="Example: Ako will study law or Ako will study medicine."),
            D("A **disjunctive syllogism** is an argument with a disjunction as one premise, a second premise that deals with one alternative, and a conclusion about the other alternative.",
              title="Definition: disjunctive syllogism"),
            H("Weak and strong disjunction"),
            T("The word \"or\" has two meanings in everyday speech. Think about the sentence \"You can pay by cash or by mobile money.\" You may be allowed to do both. "
              "But in the sentence \"The baby is a boy or a girl\" it cannot be both."),
            KEY("Two kinds of or", "The Board's symbol v stands for the weak kind.", cards=[
                ["Weak (inclusive) disjunction", "p v q is true when p is true, or q is true, or both are true. It is false only when both are false. This is the meaning of the symbol v."],
                ["Strong (exclusive) disjunction", "Either p or q, but not both. It is true when exactly one alternative is true. In words: \"either ... or ... but not both\"."],
            ]),
            CODE("p q | p v q\nT T |   T      (inclusive: both true is allowed)\nT F |   T\nF T |   T\nF F |   F", "text", title="Truth table of the weak disjunction"),
            H("The valid forms"),
            T("Here is the main rule. If one alternative is **false**, the other must be **true**. We deny one alternative and conclude the other."),
            CODE("p v q          p v q\n~p             ~q\n-----          -----\nq              p", "text", title="Two valid forms of the disjunctive syllogism"),
            CODE("p q | p v q | ~p | q\nT T |   T   |  F | T\nT F |   T   |  F | F\nF T |   T   |  T | T   <- both premises true, conclusion true\nF F |   F   |  T | F", "text", title="Truth-table proof of the first form"),
            T("Only the third row has both premises true, and there q is true. So the form is valid. The second form is proved in the same way: the only row with p v q and ~q both true is p true, q false, and p is true there."),
            EX("Worked example 1: a valid disjunctive syllogism", intro="The accused was at the market or at home. He was not at the market. So he was at home.", steps=[
                S("Symbols", text="p: he was at the market. q: he was at home. Premises: p v q and ~p. Conclusion: q."),
                S("Check the form", text="The second premise denies one alternative and the conclusion affirms the other. This is valid."),
                S("A warning", text="The argument is valid, but it is sound only if the disjunction is true. If the accused may have been somewhere else, the first premise is false."),
            ]),
            H("The invalid form"),
            T("What if we AFFIRM one alternative and try to deny the other? With a weak disjunction that is a fallacy."),
            CODE("p v q\np\n-----\n~q      INVALID (weak disjunction)", "text", title="Affirming an alternative"),
            CODE("p q | p v q | p | ~q\nT T |   T   | T | F   <- both premises true, conclusion FALSE\nT F |   T   | T | T\nF T |   T   | F | T\nF F |   F   | F | T", "text", title="Counterexample row"),
            T("The first row is a counterexample. Example: \"You can pay by cash or by mobile money. You paid by cash. So you did not pay by mobile money.\" You might have used both."),
            EX("Worked example 2: strong disjunction", intro="Either the exam is on Monday or it is on Tuesday (not both). The exam is on Monday. So it is not on Tuesday.", steps=[
                S("Notice the meaning", text="The words (not both) show that the disjunction is strong (exclusive)."),
                S("Test it", text="With an exclusive disjunction, exactly one alternative is true. If p is true, q must be false."),
                S("Result", text="This argument is valid. Checked by truth table: with the exclusive reading, no row has both premises true and the conclusion false."),
                S("Compare", text="With the weak reading of the same words, the argument would be invalid. So you must decide which kind of or is meant."),
            ]),
            MISTAKE("Always treating or as exclusive",
                    "If you read \"p v q, p, so ~q\" as valid, you have treated or as exclusive. Unless the words say \"but not both\" (or the two alternatives cannot be true together), use the weak (inclusive) meaning."),
            MISTAKE("Forgetting that the disjunction must cover all the cases",
                    "\"Either he is in Yaounde or in Douala\" leaves out every other town. If the first premise is false, a valid argument still has an unsound conclusion. Check that the alternatives really cover the cases."),
            QUIZ("\"Either Nana is at school or at home. Nana is not at home. So Nana is at school.\" This is:",
                 ["Valid: denying one alternative", "Invalid: affirming the consequent", "Invalid: denying the antecedent", "Valid: modus ponens"], 0,
                 "p v q and ~q give p. This is the valid disjunctive syllogism.",
                 hint="Is one alternative denied and the other affirmed?",
                 feedback=["", "There is no conditional here, so there is no consequent.", "There is no conditional here, so there is no antecedent.", "Modus ponens uses a conditional premise. This argument has a disjunction."]),
            QUIZ("\"The meeting is on Friday or Saturday. It is on Friday. So it is not on Saturday.\" If or is inclusive (weak), the argument is:",
                 ["Valid", "Invalid, because both alternatives could be true", "Valid, because one alternative was denied", "Invalid, because it has a conditional premise"], 1,
                 "The form p v q, p, so ~q is invalid when v is inclusive: a counterexample is p true and q true. (If the meeting cannot be on both days, the disjunction is exclusive and the reasoning is then valid.)",
                 hint="Ask whether both alternatives can be true.",
                 feedback=["Valid only if the disjunction is exclusive.", "", "The premise affirms an alternative; it does not deny one.", "There is no conditional premise."]),
            TIP("In Paper 1 you may be asked to decide whether a disjunctive argument is valid and to explain why. In Paper 2 use a truth table and say whether you read the disjunction as inclusive or exclusive.",
                title="Exam link"),
            PQ("Name the form: \"Either the water is boiled or it is unsafe. It is not boiled. So it is unsafe.\"",
               "p: the water is boiled. q: the water is unsafe. p v q, ~p, so q. A valid disjunctive syllogism (deny one alternative, affirm the other)."),
            PQ("Why is \"Either he is clever or hard-working. He is clever. So he is not hard-working.\" invalid?",
               "The disjunction is inclusive: a person can be both clever and hard-working. If both alternatives are true, both premises are true and the conclusion is false. So the form p v q, p, so ~q is invalid."),
            PQ("Explain the difference between weak and strong disjunction with one example each.",
               "Weak: p v q is true when at least one alternative is true, and also when both are. Example: A student may take French or German (and may take both). Strong: exactly one alternative is true, never both. Example: The baby is a boy or a girl."),
            SUM("A disjunction p v q has two alternatives. It is false only when both are false.",
                "Valid disjunctive syllogism: p v q, ~p, so q (or p v q, ~q, so p).",
                "Invalid: p v q, p, so ~q, when the disjunction is weak (inclusive).",
                "With a strong (exclusive) disjunction, affirming one alternative does let you deny the other.",
                "Always check that the alternatives really cover all the cases."),
        ],
    ),
    # ------------------------------------------------------------------ 5. What is a dilemma
    lesson(
        module=MODULE,
        topic="Definition, nature and importance of the dilemma",
        title="What is a dilemma? Two horns and how to meet them",
        slug="oth-what-is-a-dilemma",
        minutes=20,
        summary="A dilemma is an argument built from two conditionals and a disjunction. Learn its parts, why it matters in debate and in hard decisions, and the three ways to answer one: grasp the horns, go between the horns, or rebut it.",
        objectives=[
            "Define a dilemma and name its parts",
            "Explain why dilemmas are important in debate and decision-making",
            "Describe the three ways of meeting a dilemma",
            "Recognise a false dilemma",
        ],
        key_concepts=["Dilemma", "Horns of a dilemma", "Grasping the horns", "Going between the horns", "Rebutting a dilemma", "False dilemma"],
        blocks=[
            H("Introduction"),
            T("A young woman from Bafut has two offers. Company A is in Douala: \"If I take the job in Douala, I will earn well but I will live far from my family.\" "
              "Company B is in Bafut: \"If I stay at home, I will be near my family but I will earn little.\" She must take one or the other. "
              "Whatever she chooses, she gets something she does not want. This is a **dilemma**."),
            D("A **dilemma** is an argument that has a pair of conditional statements as one premise and a disjunction as the other premise. "
              "The conclusion is a disjunction (or, in the simple case, a single statement). Whichever alternative is chosen, an unwelcome result follows.",
              title="Definition: dilemma",
              note="The word comes from Greek: di (two) and lemma (proposition or something taken). The usual picture is a bull with two horns: either way, you get hurt."),
            H("The parts of a dilemma"),
            CODE("If p then q, and if r then s     (the two conditionals)\nEither p or r                      (the disjunction)\n-------------------------------\nSo q or s                          (the conclusion)", "text", title="A dilemma (the constructive form)"),
            IMG("f5l-oth-dilemma-horns.svg",
                alt="Diagram. Premise: p or r. From p an arrow labelled if p then q leads to q. From r an arrow labelled if r then s leads to s. The conclusion is q or s.",
                caption="Figure 1. The structure of a dilemma: a disjunction on top, two conditionals below, and a conclusion that is again a disjunction."),
            T("The two conditionals are the **horns** of the dilemma. The disjunction offers the two choices. Each choice leads along one horn to a result."),
            EX("Worked example 1: find the parts", intro="\"If I keep the shop open late, I will be tired. If I close early, I will lose customers. I must either keep it open late or close early. So I will be tired or I will lose customers.\"", steps=[
                S("Find the conditionals (the horns)", text="Horn 1: If I keep the shop open late, I will be tired. Horn 2: If I close early, I will lose customers."),
                S("Find the disjunction", text="Either I keep it open late or I close early."),
                S("Find the conclusion", text="I will be tired or I will lose customers."),
                S("Check", text="The argument is valid. The next two lessons show the exact forms and prove this by truth table."),
            ]),
            H("Why dilemmas matter"),
            T("**In debate:** a dilemma can trap an opponent. Whatever they answer, they appear to accept something unwelcome. A lawyer may ask a witness a question with two possible answers, both of which help the other side. "
              "A good debater must learn to see the dilemma coming and answer it."),
            T("**In decisions:** a dilemma describes a real hard choice: a family choosing between two schools, a farmer choosing between two crops, a manager choosing between cutting costs and losing staff. "
              "Seeing the structure shows exactly what each choice will cost."),
            TIP("A valid dilemma is not automatically convincing. It is valid, but the premises may not be true. Meeting a dilemma means examining its premises."),
            H("Three ways of meeting a dilemma"),
            KEY("How to answer a dilemma", "Traditional textbooks name three methods.", cards=[
                ["1. Grasp the horns", "Deny one of the conditionals (or both). Say that the consequence does not really follow. \"It is not true that closing early loses customers. My regular customers shop in the morning.\""],
                ["2. Go between the horns", "Deny the disjunction. Say that there is a third choice. \"I can keep the shop open until 6 pm: neither late nor early.\""],
                ["3. Rebut the dilemma", "Answer with another dilemma that reaches an opposite conclusion from the same choices. This is called a counter-dilemma."],
            ]),
            EX("Worked example 2: meeting a dilemma", intro="\"If you take the loan, you will be in debt. If you refuse the loan, your business will not grow. You must take it or refuse it. So you will be in debt or your business will not grow.\" Give an answer by going between the horns.", steps=[
                S("Look at the disjunction", text="Take the loan or refuse the loan. Is there another choice?"),
                S("Find a third choice", text="Save for a year and expand slowly, or find a partner to share the cost."),
                S("State the answer", text="The disjunction is false (there is a third choice), so the dilemma fails. Going between the horns is the strongest reply when it is honest, because the argument may be valid and still have a false premise."),
            ]),
            T("A **false dilemma** is a dilemma whose disjunction leaves out other possibilities. \"Either you pass this exam or your life is ruined\" is an example of the pattern. "
              "It is also met under the informal fallacies (a later module). Here, note only that going between the horns shows a dilemma to be false."),
            MISTAKE("Rebutting with a different conclusion and thinking the first argument is refuted",
                    "A rebuttal (counter-dilemma) gives an opposite conclusion, but it does not show that the first dilemma was invalid. "
                    "It shows that the same facts can be used on both sides. To refute a dilemma properly, show that a premise is false."),
            MISTAKE("Saying a dilemma is invalid because you dislike the conclusion",
                    "If the form is valid, the conclusion follows from the premises. Attack the premises (the conditionals or the disjunction), not the validity."),
            QUIZ("\"Either you pay the fine or you go to prison. But there is a third option: community service.\" What method is used to meet the dilemma?",
                 ["Grasping the horns", "Going between the horns", "Rebutting with a counter-dilemma", "Affirming the consequent"], 1,
                 "A third option denies the disjunction (\"either pay or go to prison\"). That is going between the horns.",
                 hint="Which part of the dilemma does the speaker attack: a conditional or the disjunction?",
                 feedback=["Grasping the horns would deny one of the conditionals.", "", "A rebuttal builds a new dilemma with the opposite conclusion.", "That is a fallacy of conditional reasoning, not a way of meeting a dilemma."]),
            QUIZ("A dilemma is made of:",
                 ["Two disjunctions and one conditional", "Two conditional statements and a disjunction", "Three conditionals", "Two universal propositions and a particular one"], 1,
                 "A dilemma combines two conditionals (the horns) with a disjunction that offers the choice.",
                 hint="Recall the picture: two horns, and a choice between them.",
                 feedback=["It is the other way round.", "", "A disjunction is also needed.", "That describes a categorical syllogism."]),
            TIP("In Paper 1 you may be asked to define a dilemma or to name the method used to meet one. In Paper 2 you may be given a short passage and asked to identify its horns and write a reply.",
                title="Exam link"),
            PQ("Identify the horns and the disjunction: \"If the school raises fees, some parents will withdraw their children. If it keeps fees low, it cannot pay its teachers well. It must raise fees or keep them low.\"",
               "Horns: if the school raises fees, some parents will withdraw their children; if it keeps fees low, it cannot pay its teachers well. Disjunction: the school raises fees or keeps them low. Conclusion: some parents will withdraw their children, or the school cannot pay its teachers well."),
            PQ("Give a reply to the dilemma in Question 1 by grasping a horn.",
               "Deny a conditional. Example: It is not true that raising fees by a small amount will make parents withdraw their children, because many would pay for good teaching. This attacks the first horn."),
            PQ("Explain why a valid dilemma may still have a false conclusion.",
               "Validity only says that if the premises are true, the conclusion must be true. A dilemma may have a false conditional or a disjunction that leaves out a third choice. Then a premise is false, and the conclusion may be false."),
            SUM("A dilemma has two conditionals (the horns) and a disjunction that offers a choice.",
                "Whichever choice is taken, an unwelcome result follows.",
                "Dilemmas appear in debate (to trap an opponent) and in real decisions.",
                "Three replies: grasp the horns (deny a conditional), go between the horns (deny the disjunction), rebut (give a counter-dilemma).",
                "A false dilemma leaves out other possible choices."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Constructive dilemma
    lesson(
        module=MODULE,
        topic="Constructive dilemma",
        title="The constructive dilemma: from choices to results",
        slug="oth-the-constructive-dilemma",
        minutes=22,
        summary="The constructive dilemma affirms the antecedents of two conditionals and concludes that one of the consequents holds. Learn the form, the simple case, and the truth-table proof that it is valid.",
        objectives=[
            "State the form of the constructive dilemma in symbols",
            "Recognise a simple constructive dilemma",
            "Prove the form valid by truth table",
            "Avoid the common errors in handling the premises and conclusion",
        ],
        key_concepts=["Constructive dilemma", "Simple constructive dilemma", "Antecedents", "Consequents", "Disjunctive conclusion"],
        blocks=[
            H("Introduction"),
            T("A student in Buea says: \"If I study the sciences, I will become an engineer. If I study the arts, I will become a teacher. I will study the sciences or the arts. So I will be an engineer or a teacher.\" "
              "The student looks at the possible choices and builds up (constructs) the results. This is a **constructive dilemma**."),
            D("A **constructive dilemma** has these parts: two conditionals joined together (with the dot, which means and), a disjunction of their antecedents, and a conclusion that is the disjunction of their consequents.",
              title="Definition: constructive dilemma",
              formula=""),
            CODE("(p ⊃ q) . (r ⊃ s)\np v r\n--------------------\nq v s", "text", title="The form of the constructive dilemma"),
            T("In words: if p then q, and if r then s. We have p or r. So we have q or s. The second premise AFFIRMS the antecedents. The conclusion states the consequents. That is why it is called constructive."),
            H("Proof by truth table"),
            T("The form has four letters, so the table has 2 to the power 4, which is 16 rows. The first premise is the conjunction of the two conditionals. We look for any row where both premises are true and the conclusion is false."),
            CODE("""p q r s | (p ⊃ q) . (r ⊃ s) | p v r | q v s
T T T T |         T         |   T   |  T   <- both premises true
T T T F |         F         |   T   |  T
T T F T |         T         |   T   |  T   <- both premises true
T T F F |         T         |   T   |  T   <- both premises true
T F T T |         F         |   T   |  T
T F T F |         F         |   T   |  F
T F F T |         F         |   T   |  T
T F F F |         F         |   T   |  F
F T T T |         T         |   T   |  T   <- both premises true
F T T F |         F         |   T   |  T
F T F T |         T         |   F   |  T
F T F F |         T         |   F   |  T
F F T T |         T         |   T   |  T   <- both premises true
F F T F |         F         |   T   |  F
F F F T |         T         |   F   |  T
F F F F |         T         |   F   |  F""", "text", title="Truth table: 16 rows"),
            T("There are five rows with both premises true. In every one of them q v s is true. The rows where q v s is false (rows 6, 8, 14 and 16) all have a false premise. So the constructive dilemma is **valid**."),
            TIP("You do not need to write all 16 rows in an exam if you use the shorter method. Assume the conclusion false (q false and s false). Then p ⊃ q forces p false, and r ⊃ s forces r false. So p v r is false: a premise is false. The conclusion cannot be false while the premises are true."),
            H("The simple constructive dilemma"),
            D("In a **simple constructive dilemma** the two conditionals have the **same consequent**. The conclusion is that single consequent, not a disjunction.",
              title="Definition: simple constructive dilemma"),
            CODE("(p ⊃ q) . (r ⊃ q)\np v r\n--------------------\nq", "text", title="Simple constructive dilemma"),
            T("Example: If it rains, the match is postponed. If the pitch is flooded, the match is postponed. It rains or the pitch is flooded. So the match is postponed. "
              "This form is also valid (checked with a truth table of 8 rows)."),
            EX("Worked example 1: a constructive dilemma in words", intro="If the harvest is good, prices fall. If the harvest is bad, food is scarce. The harvest is good or bad. So prices fall or food is scarce.", steps=[
                S("Write the symbols", text="p: the harvest is good. q: prices fall. r: the harvest is bad. s: food is scarce."),
                S("Write the form", text="(p ⊃ q) . (r ⊃ s), p v r, so q v s."),
                S("Name it", text="The second premise affirms the antecedents, and the conclusion is the disjunction of the consequents. It is a constructive dilemma, and it is valid."),
            ]),
            EX("Worked example 2: a simple constructive dilemma", intro="If I go by road, I will arrive tired. If I go by river, I will arrive tired. I go by road or by river. So I will arrive tired.", steps=[
                S("Write the symbols", text="p: I go by road. r: I go by river. q: I will arrive tired."),
                S("Write the form", text="(p ⊃ q) . (r ⊃ q), p v r, so q."),
                S("Name it", text="Same consequent, so it is a simple constructive dilemma. Valid."),
            ]),
            H("Common errors"),
            MISTAKE("Changing the conclusion to a conjunction",
                    "From (p ⊃ q) . (r ⊃ s) and p v r you may conclude q v s, but NOT q . s. A truth-table row such as p true, q true, r false, s false makes both premises true and q . s false."),
            MISTAKE("Using the consequents as the disjunction",
                    "\"(p ⊃ q) . (r ⊃ s), q v s, so p v r\" is invalid. This affirms the consequents: it is the dilemma form of affirming the consequent. A counterexample: p false, q true, r false, s false makes the premises true and the conclusion false."),
            MISTAKE("A valid dilemma with false premises",
                    "The form is valid, but the argument is sound only if the conditionals and the disjunction are true. Always check that the two choices cover all the cases."),
            QUIZ("Which is the correct conclusion of: If p then q, and if r then s; p or r?",
                 ["q and s", "p or r", "q or s", "not q or not s"], 2,
                 "The constructive dilemma concludes the disjunction of the consequents: q v s.",
                 hint="The conclusion takes the consequents and joins them with or.",
                 feedback=["The conclusion cannot be a conjunction. If p is true and r false, only q is guaranteed.", "That repeats a premise.", "", "That belongs to the destructive dilemma, with different premises."]),
            QUIZ("(p ⊃ q) . (r ⊃ s), q v s, therefore p v r. This argument is:",
                 ["a valid constructive dilemma", "invalid: it affirms the consequents", "valid: it is modus ponens", "invalid: it has no conditionals"], 1,
                 "In the constructive dilemma the second premise affirms the antecedents (p v r). Here it affirms the consequents. The form is invalid.",
                 hint="Which parts does the second premise contain: antecedents or consequents?",
                 feedback=["The valid form has p v r as the second premise and q v s as the conclusion.", "", "Modus ponens affirms the antecedent of a conditional.", "The argument does have two conditionals."]),
            TIP("Paper 1 often shows a form in symbols and asks you to name it or say whether it is valid. Paper 2 may ask for the symbols of an argument in words, then a truth-table proof.",
                title="Exam link"),
            PQ("Write in symbols: \"If we use the highway, we arrive early. If we use the village road, we save fuel. We use the highway or the village road. So we arrive early or we save fuel.\"",
               "p: we use the highway. q: we arrive early. r: we use the village road. s: we save fuel. (p ⊃ q) . (r ⊃ s), p v r, so q v s. This is a valid constructive dilemma."),
            PQ("How many rows does the truth table of a constructive dilemma have, and why?",
               "Sixteen. There are four different letters (p, q, r, s) and each can be true or false, so 2 to the power 4 = 16 rows."),
            PQ("Show that \"(p ⊃ q) . (r ⊃ s), p v r, so q . s\" is invalid.",
               "Take p true, q true, r false, s false. Then p ⊃ q is true and r ⊃ s is true (false antecedent), so the first premise is true. p v r is true. But q . s is false because s is false. Both premises true and the conclusion false: invalid."),
            SUM("Constructive dilemma: (p ⊃ q) . (r ⊃ s), p v r, so q v s. Valid.",
                "The second premise affirms the antecedents; the conclusion states the consequents (joined by or).",
                "Simple constructive dilemma: (p ⊃ q) . (r ⊃ q), p v r, so q. Valid.",
                "The truth table has 16 rows; no row has true premises and a false conclusion.",
                "Do not conclude q . s, and do not affirm the consequents to get the antecedents."),
        ],
    ),
    # ------------------------------------------------------------------ 7. Destructive dilemma
    lesson(
        module=MODULE,
        topic="Destructive dilemma",
        title="The destructive dilemma: from denied results to denied causes",
        slug="oth-the-destructive-dilemma",
        minutes=22,
        summary="The destructive dilemma denies the consequents of two conditionals and concludes that at least one antecedent is false. Learn the form, the truth-table proof, how it differs from the constructive dilemma, and the common mistakes.",
        objectives=[
            "State the form of the destructive dilemma in symbols",
            "Prove the form valid by truth table",
            "Compare the destructive dilemma with the constructive dilemma",
            "Spot and correct common mistakes",
        ],
        key_concepts=["Destructive dilemma", "Denying the consequents", "Simple destructive dilemma", "Constructive dilemma", "Modus tollens"],
        blocks=[
            H("Introduction"),
            T("A shopkeeper in Kumba says: \"If the new stock arrives, I will pay the supplier. If the shop makes a profit this week, I will pay the staff bonus. But I will not pay the supplier, or I will not pay the bonus. So the new stock has not arrived, or the shop has not made a profit.\" "
              "Here the speaker works backwards from results that did not happen. This is a **destructive dilemma**."),
            D("A **destructive dilemma** has two conditionals joined together, a disjunction that **denies the consequents** (at least one of the two results does not happen), and a conclusion that at least one **antecedent is false**.",
              title="Definition: destructive dilemma"),
            CODE("(p ⊃ q) . (r ⊃ s)\n~q v ~s\n--------------------\n~p v ~r", "text", title="The form of the destructive dilemma"),
            T("The word destructive means that this form tears down (denies) the antecedents. It is modus tollens (denying the consequent) used for two conditionals at once. "
              "In modus tollens, we deny q and conclude ~p. Here we know that q fails or s fails. So p fails or r fails."),
            H("Proof by truth table"),
            T("Again there are four letters and 2 to the power 4 = 16 rows. We look for rows with both premises true."),
            CODE("""p q r s | (p ⊃ q) . (r ⊃ s) | ~q v ~s | ~p v ~r
T T T T |         T         |    F    |    F
T T T F |         F         |    T    |    F
T T F T |         T         |    F    |    T
T T F F |         T         |    T    |    T   <- both premises true
T F T T |         F         |    T    |    F
T F T F |         F         |    T    |    F
T F F T |         F         |    T    |    T
T F F F |         F         |    T    |    T
F T T T |         T         |    F    |    T
F T T F |         F         |    T    |    T
F T F T |         T         |    F    |    T
F T F F |         T         |    T    |    T   <- both premises true
F F T T |         T         |    T    |    T   <- both premises true
F F T F |         F         |    T    |    T
F F F T |         T         |    T    |    T   <- both premises true
F F F F |         T         |    T    |    T   <- both premises true""", "text", title="Truth table: 16 rows"),
            T("Five rows have both premises true (marked). In each of them ~p v ~r is true. No row has true premises and a false conclusion. So the destructive dilemma is **valid**."),
            TIP("Short method: suppose the conclusion false. Then p is true and r is true. The conditionals now force q true and s true. But then ~q v ~s is false. So the premises cannot both be true."),
            H("The simple destructive dilemma"),
            D("In a **simple destructive dilemma** the two conditionals have the **same antecedent**. The conclusion is the denial of that antecedent.",
              title="Definition: simple destructive dilemma"),
            CODE("(p ⊃ q) . (p ⊃ r)\n~q v ~r\n--------------------\n~p", "text", title="Simple destructive dilemma"),
            T("Example: If the plan is carried out, the cost is too high. If the plan is carried out, it takes too long. Either the cost is not too high or it does not take too long. So the plan is not carried out. "
              "This is valid (checked by truth table with 8 rows)."),
            EX("Worked example 1: a destructive dilemma", intro="If it is a snake, it can bite. If it is a lizard, it can climb. Either it cannot bite or it cannot climb. So it is not a snake or it is not a lizard.", steps=[
                S("Write the symbols", text="p: it is a snake. q: it can bite. r: it is a lizard. s: it can climb."),
                S("Write the form", text="(p ⊃ q) . (r ⊃ s), ~q v ~s, so ~p v ~r."),
                S("Name it", text="The second premise denies the consequents and the conclusion denies the antecedents. Valid destructive dilemma."),
            ]),
            EX("Worked example 2: telling constructive from destructive", intro="Decide whether each form is constructive or destructive. (a) (p ⊃ q) . (r ⊃ s), p v r, so q v s. (b) (p ⊃ q) . (r ⊃ s), ~q v ~s, so ~p v ~r.", steps=[
                S("Look at the second premise of (a)", text="p v r: it AFFIRMS the antecedents. So (a) is constructive."),
                S("Look at the second premise of (b)", text="~q v ~s: it DENIES the consequents. So (b) is destructive."),
                S("Compare the conclusions", text="(a) concludes the consequents (q v s). (b) concludes the denial of the antecedents (~p v ~r)."),
            ]),
            KEY("Constructive and destructive side by side", "Both are valid and have the same first premise.", cards=[
                ["Constructive", "Second premise: p v r (affirms the antecedents). Conclusion: q v s."],
                ["Destructive", "Second premise: ~q v ~s (denies the consequents). Conclusion: ~p v ~r."],
            ]),
            T("The link with the earlier lessons: the constructive dilemma is a two-conditional version of modus ponens. The destructive dilemma is a two-conditional version of modus tollens."),
            H("Common mistakes"),
            MISTAKE("Denying the antecedents to conclude the denial of the consequents",
                    "\"(p ⊃ q) . (r ⊃ s), ~p v ~r, so ~q v ~s\" is invalid. It is the dilemma version of denying the antecedent. Counterexample: p true, q true, r false, s true."),
            MISTAKE("Concluding a conjunction",
                    "From ~q v ~s you can only conclude ~p v ~r, not ~p . ~r. A row such as p true, q true, r false, s false makes the premises true and ~p . ~r false."),
            MISTAKE("Mixing up the two dilemmas",
                    "Check the second premise. If it says that the antecedents are true (or), the form is constructive. If it says that the consequents are false (not ... or not ...), it is destructive."),
            QUIZ("In the destructive dilemma, the second premise:",
                 ["affirms the antecedents", "denies the consequents", "affirms the consequents", "denies the antecedents"], 1,
                 "The destructive dilemma has the second premise ~q v ~s, which denies the consequents.",
                 hint="Think of modus tollens, which denies the consequent.",
                 feedback=["That is the constructive dilemma.", "", "That is the fallacy of affirming the consequent.", "That is the fallacy of denying the antecedent."]),
            QUIZ("If p then q; if r then s; not q or not s. The valid conclusion is:",
                 ["not p and not r", "not p or not r", "p or r", "q or s"], 1,
                 "A destructive dilemma concludes ~p v ~r: at least one antecedent is false. It cannot say that both are false.",
                 hint="At least one of the results failed, so at least one cause failed.",
                 feedback=["That would need both results to fail.", "", "That is the premise of a constructive dilemma.", "That is the conclusion of a constructive dilemma."]),
            TIP("Paper 1 may show a dilemma in words and ask whether it is constructive or destructive. In Paper 2 you may be asked to compare the two and prove one with a truth table.",
                title="Exam link"),
            PQ("Name the form: \"If the dam is full, the village has water. If the rains come, the farms are green. Either the village has no water or the farms are not green. So the dam is not full or the rains have not come.\"",
               "p: the dam is full. q: the village has water. r: the rains come. s: the farms are green. (p ⊃ q) . (r ⊃ s), ~q v ~s, so ~p v ~r. Destructive dilemma. Valid."),
            PQ("State one difference between the constructive and the destructive dilemma.",
               "The constructive dilemma has the antecedents affirmed (p v r) and concludes the consequents (q v s). The destructive dilemma has the consequents denied (~q v ~s) and concludes the antecedents denied (~p v ~r)."),
            PQ("Why is \"(p ⊃ q) . (r ⊃ s), ~p v ~r, so ~q v ~s\" invalid?",
               "It denies the antecedents. Take p true, q true, r false, s true. Both conditionals are true, ~p v ~r is true (r is false), but ~q v ~s is false (q and s are both true). True premises with a false conclusion: invalid."),
            SUM("Destructive dilemma: (p ⊃ q) . (r ⊃ s), ~q v ~s, so ~p v ~r. Valid.",
                "The second premise denies the consequents; the conclusion denies the antecedents (at least one).",
                "Simple destructive dilemma: (p ⊃ q) . (p ⊃ r), ~q v ~r, so ~p. Valid.",
                "Constructive: affirm the antecedents, conclude the consequents. Destructive: deny the consequents, conclude the antecedents denied.",
                "Invalid look-alikes: affirming the consequents, denying the antecedents, concluding a conjunction."),
        ],
    ),
]
