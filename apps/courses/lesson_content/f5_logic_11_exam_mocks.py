"""Form 5 Logic (O Level 0590): the Examination module, Paper 1 and Paper 2 (three lessons).

Draft content. The only exam facts stated are those of the Board's revised 0590 syllabus (see
docs/curriculum/LOGIC_0590_SOURCE.md): Paper 1 is 50 multiple-choice questions, all answered, 1 mark each, in
1 hour 30 minutes, for 40% of the marks; Paper 2 is 2 hours 30 minutes for 60%, six questions of 20 marks each, with
Section A structural (three questions, all answered) and Section B problem solving (three questions, any two
answered), five questions in all. Assessment objectives: knowledge 40%, understanding 30%, application 20%,
higher-level abilities 10%. Time plans, checklists and answer plans are KKEVO study advice, not official mark
schemes: no mark splits inside a question are stated. Every logical claim (validity of the syllogisms and
propositional forms, opposition and eduction, truth tables) was checked by brute-force script. Opposition uses the
traditional square and says so; the Venn work follows the modern view; textbooks differ.
"""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

M_EXAM = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. Paper 1 strategies
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1: multiple-choice strategies",
        slug="exam-paper-1-multiple-choice-strategies",
        minutes=24,
        summary="How Paper 1 works (50 questions, 90 minutes), a time plan of about 1.8 minutes a question, the two-pass "
                "method, elimination, reading all, some, not all and no with care, and quick tests for validity.",
        objectives=[
            "Describe how Paper 1 is organised: 50 multiple-choice questions, all answered, in 1 hour 30 minutes",
            "Use the two-pass method and calculate the average time for each question",
            "Read quantifiers and negations carefully, and tell contrary from contradictory",
            "Test an argument quickly with a counterexample, a Venn sketch or a truth-table shortcut",
        ],
        key_concepts=["Paper 1", "Two-pass method", "Elimination", "Contradictory", "Counterexample", "Validity and truth"],
        blocks=[
            H("Introduction"),
            T("Think of a candidate in an exam hall in Bamenda. The invigilator says, \"You may begin.\" Fifty questions wait on the "
              "page. One asks about the three operations of the mind. The next asks for the middle term of a syllogism. "
              "Another asks which of two sentences is the denial of a claim about market traders.\n\n"
              "Paper 1 covers the **whole syllabus**, from the foundation of logic to informal fallacies. Knowing the content is "
              "the first half of success. Knowing how to read and answer multiple-choice questions is the second half. "
              "This lesson teaches the second half."),
            D("Paper 1 has **50 multiple-choice questions** and **all** of them are answered. The time allowed is "
              "**1 hour 30 minutes**. Each question is worth **1 mark**. Paper 1 carries **40%** of the marks for the whole "
              "examination (Paper 2 carries 60%).", title="Paper 1: the official facts"),
            T("The Board sets four assessment objectives. **Knowledge** (40%) asks you to recall "
              "definitions, names and rules. **Understanding** (30%) asks you to explain. **Application** (20%) asks you to use a rule "
              "on a new case, for example an everyday argument about a school rule or a market bargain. **Higher-level abilities** (10%) "
              "ask you to analyse and judge. Questions may be set in situations such as ethics, environment, economy, religion, "
              "culture, management and jurisprudence. You are always asked about the **structure** of the reasoning, not whether "
              "you agree with the conclusion."),
            TIP("Paper 1 questions come from all nine modules of the syllabus. Paper 2 Section A and Section B use the same ideas "
                "in written form. Every lesson in this course helps in both papers.", title="Exam link"),
            H("Time: about 1.8 minutes a question"),
            T("90 minutes divided by 50 questions is **1.8 minutes** for each question: a little under two minutes. A recall "
              "question may take 20 seconds. A syllogism or truth-table question may take three minutes. The aim is to keep to the "
              "average and never to get stuck."),
            IMG("f5l-exam-timeplan.svg",
                alt="A bar showing 90 minutes: Pass 1 up to 55 minutes, Pass 2 from 55 to 80 minutes, and a final check from 80 to 90 minutes.",
                caption="Figure 1. A suggested plan for the 90 minutes (KKEVO study advice, not an official rule)."),
            KEY("The two-pass method",
                "Go through the paper twice. The first pass collects the marks that are easy. The second pass uses the time that is left "
                "for the hard questions.",
                cards=[["Pass 1 (about 55 minutes)", "Answer every question you can do quickly. If you are not sure after about two minutes, tick it and move on."],
                       ["Pass 2 (about 25 minutes)", "Return to the ticked questions. Use elimination and the quick tests below. Choose the best answer."],
                       ["Check (about 10 minutes)", "Make sure every question has an answer. Re-read questions that contain not, only, all or some."]]),
            H("Reading a question and eliminating options"),
            D("The **stem** is the question. The **key** is the one correct option. The **distractors** are the wrong options. "
              "A good distractor looks attractive because it contains a true fact or a common mistake, but it does not answer "
              "this question. Read the stem twice, then cross out options that are clearly wrong. An option can be true and still be wrong for this question.", title="Stem, key and distractors"),
            H("Reading all, some, not all and no"),
            KEY("Contradictories of the standard propositions",
                "Many wrong answers come from reading a quantifier too quickly. Two statements are contradictories if they can never be both true and never both false. This holds in both the "
                "traditional and the modern view of the square.",
                cards=[["All S are P", "Its contradictory is: Some S are not P. 'Not all S are P' says the same as 'Some S are not P'."],
                       ["No S are P", "Its contradictory is: Some S are P."],
                       ["Some S are P", "Its contradictory is: No S are P."],
                       ["Some S are not P", "Its contradictory is: All S are P."]]),
            MISTAKE("Contrary or contradictory?",
                    "The denial of 'All the mangoes are ripe' is NOT 'No mango is ripe'. If some are ripe and some are not, both "
                    "statements are false. 'All are ripe' and 'No one is ripe' are contraries: they cannot both be true, but "
                    "they can both be false. Contradictories leave no middle ground."),
            H("Testing validity quickly"),
            T("An argument is **valid** when it is impossible for all the premises to be true and the conclusion false. So to show "
              "that an argument is invalid you need only **one case** in which the premises are true and the conclusion is false. "
              "That case is a **counterexample**."),
            EX("Worked example 1: counterexample",
               intro="A paper asks: 'All taxi drivers are licensed. Some women are licensed. Therefore some women are taxi drivers.' Is it valid?",
               steps=[
                   S("Keep the form", text="All P are M. Some S are M. Therefore some S are P, with P = taxi drivers, M = licensed persons, S = women."),
                   S("Build a parallel argument", text="Replace the terms by ones whose truth you know: All dogs are animals. Some cats are animals. Therefore some cats are dogs."),
                   S("Check", text="Both premises are true. The conclusion is false. The same form gives true premises and a false conclusion."),
                   S("Verdict", text="The argument is invalid. The middle term 'licensed' is distributed in neither premise."),
               ]),
            EX("Worked example 2: a truth-table shortcut",
               intro="Test: 'If the market is open, prices are posted. Prices are not posted. So the market is not open.' Let o = the market is open and p = prices are posted. The form is o ⊃ p, ~p, therefore ~o.",
               steps=[
                   S("Try to make the conclusion false", text="~o is false when o is true. Put o = T."),
                   S("Try to make the premises true", text="With o = T, o ⊃ p is true only if p = T. But then ~p is false."),
                   S("Conclude", text="No row has true premises and a false conclusion. The argument is valid (this pattern is called modus tollens)."),
                   S("Compare", text="For 'o ⊃ p, p, therefore o' the row o = F, p = T makes the premises true and the conclusion false, so that form is invalid."),
               ]),
            H("Worked questions from every module"),
            KEY("Nine modules, nine quick questions",
                "One typical Paper 1 question idea from each module, with the quick answer. These are KKEVO examples, not questions from past papers.",
                cards=[["Foundation of Logic", "Which operation of the mind produces a proposition? Judging."],
                       ["Terms", "Which term has the greater extension, 'tree' or 'mango tree'? 'Tree'."],
                       ["Definitions and division", "'A teacher is one who teaches' breaks which rule? It is circular."],
                       ["Propositions", "Which standard proposition distributes both terms? E: No S are P."],
                       ["Symbolic logic", "When is p ⊃ q false? Only when p is true and q is false."],
                       ["Inference", "What is the contradictory of 'No S are P'? Some S are P."],
                       ["Syllogism", "A syllogism with the middle term undistributed in both premises commits which fallacy? Undistributed middle."],
                       ["Other arguments", "Which is valid: denying the consequent or affirming the consequent? Denying the consequent."],
                       ["Informal fallacies", "Concluding about all traders from two cases is a hasty generalisation."]]),
            MISTAKE("Mixing truth and validity",
                    "Validity is about the **form**: does the conclusion follow? Truth is about the **statements**. A valid argument can "
                    "have a false conclusion if a premise is false. An invalid argument can have a true conclusion. Never choose an "
                    "option only because its conclusion sounds true in real life."),
            QUIZ("Which option is a correct negation of 'All the students passed'?",
                 ["Not every student passed", "No student passed", "Some students passed", "Every student failed"], 0,
                 "'Not every student passed' means that at least one did not pass. It is true exactly when the original is false.",
                 hint="A negation must be true exactly when the original is false.",
                 feedback=["", "This is a contrary: stronger than the denial.", "This can be true together with 'All passed'.", "This is the same as 'none passed': too strong."]),
            QUIZ("An argument is valid and its conclusion is false. What must be true?",
                 ["At least one premise is false", "All the premises are true", "The argument is sound", "The conclusion is true"], 0,
                 "If the form is valid and the conclusion false, the premises cannot all be true. At least one premise is false.",
                 hint="Valid: true premises never give a false conclusion.",
                 feedback=["", "True premises in a valid argument would force a true conclusion.", "Soundness needs valid form and true premises.", "The conclusion is false, as given."]),
            PQ("You have used 40 minutes and have dealt with 30 of the 50 questions. At the average rate of 1.8 minutes a question, are you ahead or behind?",
               "30 x 1.8 = 54 minutes at the average pace. You used 40, so you are ahead by 14 minutes. Use the extra time in pass 2."),
            PQ("Write the contradictory of 'No Form 5 student is late'. Why is 'All Form 5 students are late' not the contradictory?",
               "The contradictory is 'Some Form 5 students are late'. 'All are late' is not the contradictory because both statements can be false: if some students are late and some are not, 'No one is late' and 'All are late' are both false."),
            PQ("Test the argument: 'All nurses are women. Some women are teachers. Therefore some teachers are nurses.' Give a counterexample if it is invalid.",
               "The form is: All P are M, Some M are S, so some S are P. It is invalid, because the middle term 'women' is undistributed. Counterexample: All dogs are animals. Some animals are cats. Therefore some cats are dogs. The premises are true and the conclusion is false."),
            PQ("Use the shortcut to test: 'If it rains, the road floods. The road is not flooded. So it did not rain.'",
               "Form: r ⊃ f, ~f, therefore ~r. Make the conclusion false: r = T. Then r ⊃ f needs f = T, but then ~f is false. No row makes the premises true and the conclusion false, so the argument is valid."),
            SUM("Paper 1 has 50 multiple-choice questions, all answered, in 90 minutes. Each is worth 1 mark and the paper carries 40%.",
                "Plan about 1.8 minutes a question. Use two passes and keep the last minutes for checking (study advice).",
                "Read quantifiers slowly. The contradictory of All S are P is Some S are not P, not No S are P.",
                "To show invalidity, find one case with true premises and a false conclusion.",
                "Validity is about form and truth is about statements. Do not choose an option only because it sounds true."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Paper 2 Section A
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2 Section A: structural questions",
        slug="exam-paper-2-section-a-structural-questions",
        minutes=24,
        summary="How to answer Section A of Paper 2 (three structural questions, all answered): definitions and explanations, "
                "propositions and distribution, labelled Venn and square diagrams, opposition and eduction, with model plans.",
        objectives=[
            "Describe the structure of Paper 2 and the Section A rule that all three questions are answered",
            "Answer a definition question using the genus, the difference and an example",
            "Draw and label a two-circle Venn diagram and the square of opposition",
            "Give a clear analysis of a proposition: components, quantity, quality, distribution, opposition and eduction",
        ],
        key_concepts=["Paper 2", "Section A", "Command words", "Labelled diagram", "Square of opposition", "Eduction"],
        blocks=[
            H("Introduction"),
            T("A student in Kumba opens Paper 2 and reads: 'Define a proposition and illustrate with an example. Draw a Venn diagram "
              "for No S are P. State the contradictory of the proposition.' This is a typical Section A style: short, structured parts "
              "that test what you know and understand. The aim is clear, correct and complete written answers."),
            D("Paper 2 lasts **2 hours 30 minutes** and carries **60%** of the marks. It has **six questions of 20 marks each**. "
              "**Section A** has three structural questions and **all three are answered**. **Section B** has three "
              "problem-solving questions and **any two** are answered. So five questions are answered in all. Paper 2 is designed "
              "to test comprehension, interpretation, explanation and elementary analysis.", title="Paper 2: the official facts"),
            TIP("Section A tests the ideas of the first modules: terms, definitions, propositions, opposition and eduction. The same "
                "ideas appear in Paper 1 as multiple-choice questions. Section B (the next lesson) tests problem-solving.", title="Exam link"),
            H("Read the command word"),
            KEY("Common command words",
                "A command word tells you what to do. These are KKEVO study suggestions. Always do exactly what the word asks, then check you have not left a part out.",
                cards=[["Define", "Say what the term means: the class it belongs to and what marks it off from other members of that class."],
                       ["Explain", "Give the reason or the idea, with at least one example."],
                       ["Distinguish", "Say how two things differ. Give one point about each."],
                       ["Illustrate", "Give a short example from everyday life."],
                       ["Draw", "Make a diagram and label every part."],
                       ["State", "Give a short answer. No long argument is needed."]]),
            H("Answering a definition question"),
            D("A good definition names the **genus** (the wider class) and the **specific difference** (what separates this thing "
              "from others in the class). It must not be circular, too wide, too narrow, negative without need, or obscure.",
              title="Genus and difference"),
            EX("Model answer plan 1: definition and distinction",
               intro="Define a term and a proposition and distinguish them. (A KKEVO model plan, not an official mark scheme.)",
               steps=[
                   S("Define a term", text="A term is a word or group of words that stands for an idea and can be the subject or predicate of a proposition. Example: 'student'."),
                   S("Define a proposition", text="A proposition is a statement that affirms or denies something and can be true or false. Example: 'Every student in the school wears uniform.'"),
                   S("Distinguish", text="A term is only an idea in words: it is not true or false by itself. A proposition combines terms and is true or false."),
                   S("Relate to the operations of the mind", text="Terms come from simple apprehension. Propositions come from judging."),
               ]),
            H("Analysing a proposition"),
            KEY("Distribution in the four standard propositions",
                "Section A often gives one proposition and asks several things about it. A term is distributed when the proposition says something about every member of its class.",
                cards=[["A: All S are P", "Subject S is distributed. P is not."],
                       ["E: No S are P", "S and P are both distributed."],
                       ["I: Some S are P", "Neither term is distributed."],
                       ["O: Some S are not P", "P is distributed. S is not."]]),
            EX("Model answer plan 2: analysing 'No students are cheats'",
               intro="Analyse the proposition 'No students are cheats'.",
               steps=[
                   S("Components", text="Subject: students. Predicate: cheats. Copula: are. Quantifier: No."),
                   S("Quantity and quality", text="It is universal (it speaks of all students) and negative: an E proposition."),
                   S("Distribution", text="Both terms are distributed: it says something about every student and about every cheat."),
                   S("Contradictory", text="Some students are cheats (an I proposition). They can never be both true or both false."),
                   S("Converse", text="No cheats are students. The converse of an E proposition says the same as the original."),
               ]),
            H("Diagrams that earn their marks"),
            T("A diagram is only worth marks when it is **labelled** and **correct**. Name every circle, show shading or the X "
              "clearly, and add a short title. In this course, shading means a region is empty and an X means at least one "
              "member exists there. This is the modern (Boolean) way of reading a Venn diagram."),
            IMG("f5l-exam-venn-shaded.svg",
                alt="Two overlapping circles S and P. The part of S outside P is shaded to show it is empty. This shows All S are P.",
                caption="Figure 1. A labelled Venn diagram for All S are P: the part of S outside P is empty."),
            IMG("f5l-exam-square.svg",
                alt="The traditional square of opposition with A top left, E top right, I bottom left and O bottom right, and the lines labelled contraries, subcontraries, subalternation and contradictories.",
                caption="Figure 2. The traditional square of opposition. Textbooks differ on subalternation: follow your teacher's textbook."),
            T("**Two views.** On the **traditional** (Aristotelian) square, a true universal proposition makes its particular true (A "
              "implies I and E implies O). In the **modern** Boolean view, a universal proposition does not say that its subject "
              "class has members, so subalternation is not allowed, but the contradictories A and O, and E and I, still hold. "
              "Say which view you are using. If your textbook differs, follow your teacher's textbook."),
            H("Opposition and eduction"),
            KEY("The square: what follows from a true or false proposition (traditional view)",
                "Contradictories (A and O, E and I) always have opposite truth values.",
                cards=[["If A is true", "E is false, I is true and O is false."],
                       ["If A is false", "O is true. E and I are undetermined."],
                       ["If O is false", "A is true, I is true and E is false."],
                       ["If E is true", "A is false, O is true and I is false."]]),
            KEY("Eduction: new propositions from one",
                "Eduction draws a new proposition from one proposition, without a second premise.",
                cards=[["Obversion", "Change the quality and replace the predicate by its complement. All S are P becomes No S are non-P. No S are P becomes All S are non-P."],
                       ["Conversion", "Swap subject and predicate. E and I convert simply: No S are P gives No P are S. Some S are P gives Some P are S. A gives Some P are S (by limitation, traditional view)."],
                       ["Contraposition", "Replace each term by the complement of the other. All S are P gives All non-P are non-S."]]),
            MISTAKE("Converting A simply",
                    "From 'All dogs are animals' you may not conclude 'All animals are dogs'. That is the most common error in "
                    "conversion. Only E and I convert simply."),
            QUIZ("In the traditional square of opposition, which pair are contradictories?",
                 ["All S are P and Some S are not P", "All S are P and No S are P", "Some S are P and Some S are not P", "No S are P and Some S are not P"], 0,
                 "A and O (and E and I) are contradictories: they always have opposite truth values.",
                 hint="Which pair are on the two diagonals of the square?",
                 feedback=["", "These are contraries.", "These are subcontraries.", "This is subalternation."]),
            QUIZ("What is the obverse of 'No students are cheats'?",
                 ["All students are non-cheats", "No cheats are students", "Some students are non-cheats", "All cheats are non-students"], 0,
                 "Change the quality (E to A) and take the complement of the predicate: All students are non-cheats.",
                 hint="Two changes: the quality and the predicate.",
                 feedback=["", "This is the converse.", "The quantity must stay universal.", "This changes the subject. Obversion does not."]),
            PQ("Define 'proposition' and give one example. (Model answer.)",
               "A proposition is a statement that affirms or denies something and can be true or false. Example: 'Some farmers in the village are cocoa growers.' It is made of a subject, a predicate and a copula."),
            PQ("For 'No students are cheats', state the quantity, the quality, the subject, the predicate and the distributed terms.",
               "Quantity: universal. Quality: negative. This is an E proposition. Subject: students. Predicate: cheats. Both terms are distributed."),
            PQ("On the traditional square, 'All farmers are workers' is true. State the truth values of 'No farmers are workers', 'Some farmers are workers' and 'Some farmers are not workers'.",
               "'No farmers are workers' (E) is false. 'Some farmers are workers' (I) is true. 'Some farmers are not workers' (O) is false."),
            PQ("Give the converse and the obverse of 'Some teachers are women'.",
               "Converse: Some women are teachers (an I proposition converts simply). Obverse: Some teachers are not non-women (change the quality from I to O and take the complement of the predicate)."),
            SUM("Section A of Paper 2: three structural questions, all answered. Paper 2 as a whole lasts 2 hours 30 minutes and carries 60%.",
                "Read the command word and do exactly what it asks. Give a meaning plus an example.",
                "Analyse a proposition in order: components, quantity and quality, distribution, diagram, opposition, eduction.",
                "A, E, I and O distribute 1, 2, 0 and 1 terms. The contradictories are A with O and E with I.",
                "Draw clean, labelled diagrams. Say whether you use the traditional or the modern view."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Paper 2 Section B
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2 Section B: problem-solving questions",
        slug="exam-paper-2-section-b-problem-solving-questions",
        minutes=26,
        summary="How to answer Section B of Paper 2 (three problem-solving questions, any two answered): test a syllogism, symbolise "
                "an argument and build a truth table, standardise an everyday argument and spot fallacies, with step-by-step models.",
        objectives=[
            "Describe Section B and plan time across the five questions of Paper 2",
            "Test a categorical syllogism step by step and name the rule it breaks",
            "Symbolise an argument and build a truth table to test it",
            "Standardise an everyday argument and identify the fallacies in a short passage",
        ],
        key_concepts=["Section B", "Problem solving", "Standard form", "Counterexample row", "Informal fallacy"],
        blocks=[
            H("Introduction"),
            T("A school debate in Douala is argued about market fees. One speaker says: 'If the fees are fair, traders will pay. The "
              "traders did not pay. So the fees are not fair.' Is the speaker's reasoning correct? Section B asks you to solve "
              "problems like this: to test, symbolise, standardise and identify. You apply the tools of the earlier modules to a "
              "real case, and you show your steps."),
            D("**Section B** of Paper 2 has **three problem-solving questions, and any two are answered**. Together with the three "
              "questions of Section A, a candidate answers five questions of 20 marks each in **2 hours 30 minutes**.", title="Section B: the official facts"),
            TIP("Section B draws mainly on the syllogism, symbolic logic, other arguments and informal fallacies. The questions apply "
                "logic to situations such as ethics, environment, economy, religion, culture, management and jurisprudence. "
                "Argue about the structure of the reasoning, not about whether you like the conclusion.", title="Exam link"),
            H("Time planning for five questions"),
            T("150 minutes divided by 5 questions is **30 minutes** for each. Most candidates need a little less than that for "
              "each question to leave time to check. This is **KKEVO study advice, not an official rule**."),
            KEY("A study plan for Paper 2",
                "Adapt it to your own speed.",
                cards=[["First 5 minutes", "Read the whole paper. Choose the two Section B questions where you are strongest."],
                       ["Section A (about 75 minutes)", "Three questions, about 25 minutes each, all answered."],
                       ["Section B (about 55 minutes)", "Two questions, about 27 minutes each, chosen after the first reading."],
                       ["Last 15 minutes", "Check names, symbols, labels and that every part is answered."]]),
            H("Skill 1: testing a syllogism"),
            KEY("Six steps for testing a categorical syllogism",
                "Keep to the order and show each step.",
                cards=[["1. Standard form", "Write the three propositions as A, E, I or O with the 'All S are P' pattern."],
                       ["2. Terms", "Minor term S: subject of the conclusion. Major term P: its predicate. Middle term M: in both premises, not in the conclusion."],
                       ["3. Mood and figure", "Mood: the three letters (major premise, minor premise, conclusion). Figure: the position of M."],
                       ["4. Distribution", "Which terms are distributed? Is M distributed at least once?"],
                       ["5. Test", "Use the general rules, or draw the premises on the Venn diagram."],
                       ["6. Verdict", "Valid or invalid, with the rule broken or a counterexample."]]),
            EX("Worked example 1: testing a syllogism",
               intro="Test: 'All traders are taxpayers. Some taxpayers are women. Therefore some women are traders.'",
               steps=[
                   S("Terms", text="Minor term S = women. Major term P = traders. Middle term M = taxpayers."),
                   S("Standard form", text="Major premise: All P are M (A). Minor premise: Some M are S (I). Conclusion: Some S are P (I)."),
                   S("Mood and figure", text="Mood AII. The middle term is the predicate of the major premise and the subject of the minor: the fourth figure. So AII-4."),
                   S("Distribution", text="In an A proposition only the subject is distributed, so M (the predicate of the major premise) is not. In an I proposition nothing is distributed. So M is distributed in neither premise."),
                   S("Verdict", text="Invalid: the middle term is undistributed. Counterexample of the same form: All dogs are animals. Some animals are cats. So some cats are dogs. The premises are true and the conclusion is false."),
               ]),
            H("Skill 2: symbolising and building a truth table"),
            T("Pick one letter for each simple statement. Use only the five symbols of the syllabus: ~ (not), . (and), v (or), "
              "⊃ (if ... then) and ≡ (if and only if). Write the premises and the conclusion. Then build the table with 2 to the power n "
              "rows, where n is the number of different letters. Mark every row where all the premises are true. If the conclusion is "
              "false in any of those rows, the argument is invalid."),
            EX("Worked example 2: symbolise and test",
               intro="'If the rain comes early, the farmers plant maize. The rain did not come early. So the farmers did not plant maize.'",
               steps=[
                   S("Symbolise", text="Let r = the rain comes early and m = the farmers plant maize. Premises: r ⊃ m and ~r. Conclusion: ~m."),
                   S("Rows", text="Two letters, so 2 x 2 = 4 rows."),
                   S("Table", text="Columns: r, m, r ⊃ m, ~r, ~m. See the table below."),
                   S("Verdict", text="In the row r = F, m = T both premises are true and the conclusion ~m is false. The argument is invalid (denying the antecedent)."),
               ]),
            CODE("r  m | r ⊃ m | ~r | ~m\nT  T |   T    |  F |  F\nT  F |   F    |  F |  T\nF  T |   T    |  T |  F   <- premises true, conclusion false\nF  F |   T    |  T |  T",
                 "text", title="Truth table for Worked example 2"),
            H("Skill 3: standardising an everyday argument"),
            T("An everyday argument is rarely in standard form. Premises may be hidden, words may differ and the order may be "
              "reversed. **Standardising** means rewriting it as premises and a conclusion in standard form, ready to test."),
            EX("Worked example 3: standardising",
               intro="'No sensible person drives at night in the rainy season, and Paul drives at night. So Paul is not sensible.'",
               steps=[
                   S("Find the conclusion", text="The word 'So' signals it: Paul is not sensible."),
                   S("Terms", text="Minor term S = persons identical with Paul. Major term P = sensible persons. Middle term M = persons who drive at night in the rainy season."),
                   S("Write the premises in standard form", text="Major premise: No sensible persons are persons who drive at night in the rainy season (No P are M, an E proposition). Minor premise: All persons identical with Paul are persons who drive at night (All S are M, an A proposition). A statement about one individual is treated as a universal one."),
                   S("Conclusion and test", text="Conclusion: No persons identical with Paul are sensible persons (No S are P). The mood is EAE. The middle term is the predicate of both premises, so this is the second figure. EAE-2 is valid (called Cesare)."),
               ]),
            H("Skill 4: fallacies in a passage"),
            EX("Worked example 4: naming fallacies",
               intro="'Ignore Ada's views on the school bell. She is only a first-year student. And last week two boys came late, so all boys in Form 5 are lazy.'",
               steps=[
                   S("Sentence 1", text="The views are rejected because of who Ada is, not because of her reasons: argument against the person (ad hominem)."),
                   S("Sentence 2", text="A claim about all Form 5 boys is based on two cases: hasty generalisation."),
                   S("Significance", text="A fallacy shows that the reasoning is weak. It does not by itself show that the conclusion is false."),
               ]),
            MISTAKE("Testing the conclusion instead of the argument",
                    "A syllogism may have a conclusion you know is false or true. Validity does not depend on that. Test the form: "
                    "distribution, a counterexample or the Venn diagram."),
            MISTAKE("Wrong order of premises",
                    "Write the major premise (the one containing the major term) first. If you write the premises in the wrong order, "
                    "you may name the wrong figure."),
            QUIZ("A truth table of 3 statement letters has how many rows?",
                 ["8", "6", "9", "4"], 0,
                 "Each letter doubles the rows: 2 x 2 x 2 = 8.",
                 hint="The number of rows is 2 to the power of the number of letters.",
                 feedback=["", "6 is not a power of 2.", "9 would be 3 times 3, but each letter has only two values.", "4 rows are enough for two letters only."]),
            QUIZ("Which fallacy is committed by 'Reject Kofi's idea. He failed last year'?",
                 ["Argument against the person", "Hasty generalisation", "Equivocation", "Undistributed middle"], 0,
                 "The idea is rejected because of a fact about Kofi, not because of its reasons.",
                 hint="Is the attack on the argument or on the person?",
                 feedback=["", "No cases are generalised.", "No word has two meanings.", "That is a fault of a syllogism, not of this reasoning."]),
            PQ("Test: 'No lawyers are farmers. All judges are lawyers. Therefore no judges are farmers.' State its mood and figure and give a verdict.",
               "Terms: S = judges, M = lawyers, P = farmers. Major premise: No M are P (E). Minor premise: All S are M (A). Conclusion: No S are P (E). Mood EAE. The middle term is the subject of the major premise and the predicate of the minor: the first figure. EAE-1 is valid (called Celarent)."),
            PQ("Symbolise 'If it rains the road floods, and if the road floods the bus is late. So if it rains the bus is late.' How many rows has its truth table? Is it valid?",
               "Let r, f and b be the three simple statements. Premises: r ⊃ f and f ⊃ b. Conclusion: r ⊃ b. Three letters give 2 to the power 3 = 8 rows. In no row are both premises true and the conclusion false, so the argument is valid (a hypothetical syllogism)."),
            PQ("Standardise: 'Only citizens may vote. Esther is not a citizen. So Esther may not vote.' Say whether it is valid.",
               "Major premise: All persons who may vote are citizens (A). Minor premise: No persons identical with Esther are citizens (E). Conclusion: No persons identical with Esther are persons who may vote (E). Mood AEE with the middle term as the predicate of both premises: the second figure. AEE-2 is valid. The 'Only' rule varies by textbook: check yours."),
            PQ("Name the fallacy: 'The headmaster's rule on phones must be wrong: he cannot even keep his own office tidy.'",
               "Argument against the person (ad hominem): the rule is rejected because of a fact about the headmaster, not because of what the rule says."),
            SUM("Section B of Paper 2: three problem-solving questions, any two answered. All five questions together take 2 hours 30 minutes.",
                "A plan of about 30 minutes a question is study advice, not an official rule. Leave time to check.",
                "Test a syllogism in six steps: standard form, terms, mood and figure, distribution, test, verdict.",
                "Symbolise with ~, ., v, ⊃ and ≡, build 2 to the power n rows, and look for a row with true premises and a false conclusion.",
                "Standardise an everyday argument before testing it, and name fallacies with a reason."),
        ],
    ),
]
