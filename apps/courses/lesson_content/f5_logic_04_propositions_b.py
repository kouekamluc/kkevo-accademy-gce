"""Form 5 Logic (GCE O Level 0590), module "The Second Operation of the Mind: Judging (Propositions)": hypothetical, disjunctive and modal propositions; translating into standard forms.
Draft content: check against the official syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "The Second Operation of the Mind: Judging (Propositions)"

LESSONS = [
    # ------------------------------------------------------------------ 1. Hypothetical propositions
    lesson(
        module=MODULE,
        topic="Hypothetical proposition and types",
        title="Hypothetical propositions: if ... then",
        slug="prop2-hypothetical-propositions",
        minutes=22,
        summary="A hypothetical (conditional) proposition says that if one thing is so, another is so. Learn antecedent and consequent, the types, when it is true or false, and its safe rewrites.",
        objectives=[
            "Define a hypothetical (conditional) proposition and name its antecedent and consequent",
            "Recognise the common types of hypothetical proposition and the words that signal them",
            "State in plain words when an if-then proposition is true and when it is false",
            "Write the contrapositive and the negation of a conditional, and avoid the converse mistake",
        ],
        key_concepts=["Hypothetical proposition", "Antecedent", "Consequent", "Conditional", "Biconditional", "Sufficient and necessary condition", "Contrapositive"],
        blocks=[
            H("Introduction"),
            T("A trader in Mokolo market tells a customer: \"If you buy ten bags of rice, I will give you the price of nine.\" "
              "She has not said that you will buy ten bags. She has not said that she will give the discount. "
              "She has said only that the second thing **depends on** the first."),
            T("A sentence of this kind is a **hypothetical proposition**. We use it every day: school rules, football predictions, "
              "farming plans and court rulings are full of \"if ... then\" statements. In this lesson you learn its parts, "
              "its types and exactly when it is true or false."),
            D("A **hypothetical proposition** is a proposition made of two propositions joined so that one is said to depend on the other. "
              "The usual form is: **If** (first part) **then** (second part).",
              title="Definition: hypothetical proposition",
              note="Example: If the rains come, then the farmers will harvest well."),
            D("The part that follows \"if\" is the **antecedent** (it comes first in the reasoning: it is the condition). "
              "The part that follows \"then\" is the **consequent** (it follows from the condition).",
              title="Definition: antecedent and consequent",
              note="In \"If the rains come, then the farmers will harvest well\": antecedent = the rains come; consequent = the farmers will harvest well."),
            KEY("Words that signal a hypothetical proposition", "The words \"if ... then\" are not always written. Watch for these.", cards=[
                ["Introduce the antecedent", "if, provided that, on condition that, in case, whenever, as long as, supposing that"],
                ["Introduce the consequent", "then, only if (the part after \"only if\" is the consequent)"],
                ["Order can change", "\"The farmers will harvest well if the rains come\" means the same as \"If the rains come, the farmers will harvest well\". The antecedent is still the part after \"if\"."],
            ]),
            H("Types of hypothetical proposition"),
            T("Books do not all use the same list of types. The types below are the ones most often given in the textbooks the Board names. "
              "**Check your own textbook and follow your teacher's list where it differs.**"),
            KEY("Common types", "Hypothetical propositions are often divided like this.", cards=[
                ["Conditional (if ... then)", "One part is the condition of the other. If p then q. Example: If the bridge is repaired, the bus will run."],
                ["Biconditional (if and only if)", "Each part depends on the other. p if and only if q. Example: You may enter the examination hall if and only if you have your candidate card."],
                ["By the kind of link", "Some books also separate conditionals by the link they claim: a cause (If you heat water to 100 degrees Celsius at sea level, it boils), a reason or logical link (If a figure is a square, it has four sides), or a promise or rule (If you pass, I will buy you a phone)."],
            ]),
            T("Some traditional books treat \"hypothetical\" as a wider group that also holds the **disjunctive** (either ... or) and the **conjunctive** (not both ...) propositions. "
              "This course gives the disjunctive proposition its own lesson, as the syllabus does. The conditional is the main type for this lesson."),
            D("In \"If p then q\", p is a **sufficient condition** for q: when p is true, that is enough to make q true. "
              "And q is a **necessary condition** for p: if q is false, then p cannot be true.",
              title="Definition: sufficient and necessary condition",
              note="\"If a student is in Form 5, then the student is in secondary school.\" Being in Form 5 is sufficient for being in secondary school. Being in secondary school is necessary for being in Form 5."),
            H("When is a conditional true or false?"),
            T("Think of a promise. A mother says: \"If you pass the mock examination, I will buy you a phone.\" "
              "When has she **broken** her promise? Only in one case: you passed and she did **not** buy the phone. "
              "In every other case she has not broken it."),
            KEY("Truth conditions of if p then q", "In the modern symbolic reading, which the Board's symbol p ⊃ q (horseshoe) uses:", cards=[
                ["False", "Only when the antecedent is true and the consequent is false."],
                ["True", "In the other three cases: both true; antecedent false and consequent true; both false."],
            ]),
            CODE("p  q  |  p ⊃ q\nT  T  |    T\nT  F  |    F\nF  T  |    T\nF  F  |    T", "text", title="Truth table for p ⊃ q"),
            T("**Textbooks differ here.** In everyday speech an \"if\" often suggests a real link (a cause or a reason), so some traditional books say that "
              "a conditional with no link is meaningless, not true. The table above is the modern truth-functional reading. "
              "The Board's symbol set includes the horseshoe, so use the table when the question is symbolic, and follow your textbook for the wording of the traditional view."),
            H("Rewriting a conditional safely"),
            KEY("Three rewrites", "Take the conditional \"If p then q\" (p ⊃ q). Checked by truth table:", cards=[
                ["Contrapositive: same meaning", "If not q then not p (~q ⊃ ~p). Both are false in exactly the same case."],
                ["Converse: different meaning", "If q then p (q ⊃ p). It can be false when the original is true."],
                ["Inverse: different meaning", "If not p then not q (~p ⊃ ~q). It also can be false when the original is true."],
            ]),
            D("To **deny** (negate) \"If p then q\" you say that p is true **and** q is false: p . ~q. "
              "The negation of a conditional is not another conditional.",
              title="Definition: negation of a conditional",
              note="Negation of \"If it rains, the match is cancelled\": \"It rains and the match is not cancelled.\""),
            EX("Worked example 1: find the antecedent and the consequent", intro=(
                "Write each sentence in the form \"If ... then ...\" and name the antecedent and the consequent. "
                "(a) The farmers will harvest well provided that the rains come. "
                "(b) You may enter the hall only if you have a ticket. "
                "(c) Whenever the generator stops, the shop goes dark."), steps=[
                S("(a) \"Provided that\" introduces the condition", text="If the rains come, then the farmers will harvest well. Antecedent: the rains come. Consequent: the farmers will harvest well."),
                S("(b) \"Only if\" introduces the consequent", text="If you may enter the hall, then you have a ticket. Antecedent: you may enter. Consequent: you have a ticket. Having a ticket is necessary, not enough on its own."),
                S("(c) \"Whenever\" gives a condition", text="If the generator stops, then the shop goes dark. Antecedent: the generator stops. Consequent: the shop goes dark."),
            ]),
            EX("Worked example 2: true or false?", intro=(
                "Mama Ngu says: \"If you pass the mock, I will buy you a phone.\" "
                "Say whether her statement is true or false in each case."), steps=[
                S("Case 1: you pass and she buys the phone", text="Antecedent true, consequent true. She kept her word. The statement is **true**."),
                S("Case 2: you pass and she does not buy the phone", text="Antecedent true, consequent false. She broke her word. The statement is **false**."),
                S("Case 3: you fail and she buys the phone anyway", text="Antecedent false. She promised nothing about this case. The statement is **true**."),
                S("Case 4: you fail and she does not buy the phone", text="Antecedent false. Nothing was promised. The statement is **true**."),
            ]),
            EX("Worked example 3: denying a conditional", intro=(
                "The council says: \"If the road is repaired, the truck arrives on time.\" "
                "A driver wants to show that this is false. What must he show?"), steps=[
                S("A conditional is false in only one case", text="Antecedent true and consequent false."),
                S("Write that case", text="The road **is** repaired **and** the truck does **not** arrive on time. In symbols: p . ~q."),
                S("Check the wrong answer", text="\"If the road is repaired, the truck is late\" is a different conditional. It does not deny the first one: the road might not be repaired, and then both are true."),
            ]),
            MISTAKE("Confusing a conditional with its converse", "\"If a person lives in Bamenda, the person lives in Cameroon\" is true. Its converse, \"If a person lives in Cameroon, the person lives in Bamenda\", is false. Never swap the parts and expect the same truth."),
            MISTAKE("Thinking a false antecedent makes the conditional false", "When the antecedent is false the condition was never met, so nothing was broken. In the truth table the conditional is then true."),
            MISTAKE("Reading \"only if\" as \"if\"", "\"You may enter only if you have a ticket\" does not mean \"If you have a ticket, you may enter\". The ticket is necessary but may not be enough. The part after \"only if\" is the consequent."),
            TIP("Hypothetical propositions appear in Paper 1 multiple choice (naming the antecedent and consequent, spotting the contrapositive or the negation) "
                "and in Paper 2 Section A structural questions (definitions, types, truth conditions). They return in Module 5 (truth tables) and Module 8 (the hypothetical syllogism).", title="Exam link"),
            QUIZ("In the proposition \"The match will be cancelled if it rains\", which part is the antecedent?",
                 ["The match will be cancelled", "It rains", "The match", "if"], 1,
                 "The antecedent is the condition, the part introduced by \"if\": it rains. The sentence means \"If it rains, the match will be cancelled\".",
                 hint="Rewrite the sentence as \"If ..., then ...\" first.",
                 feedback=["That is the consequent. It comes first in the sentence but it is what follows from the condition.", "", "A bare term is not a proposition. The antecedent must be a whole statement.", "\"if\" is only the word that signals the condition."]),
            QUIZ("Which one case makes \"If Ako studies, then he passes\" false?",
                 ["Ako does not study and he passes", "Ako does not study and he fails", "Ako studies and he passes", "Ako studies and he fails"], 3,
                 "A conditional is false only when the antecedent is true and the consequent is false: Ako studies and he fails.",
                 hint="Think of a broken promise: the condition is met but the result does not follow.",
                 feedback=["The condition was not met, so the statement is not broken. It is true.", "The condition was not met, so the statement is not broken. It is true.", "Both parts true: the statement is kept, so it is true.", ""]),
            PQ("Name the antecedent and the consequent: \"A pupil will be punished provided that he is late.\"",
               "Rewrite: If a pupil is late, then he will be punished. Antecedent: a pupil is late (\"provided that\" introduces the condition). Consequent: he will be punished."),
            PQ("Write the contrapositive of \"If a number is divisible by 6, then it is even.\" Does it mean the same?",
               "Contrapositive: If a number is not even, then it is not divisible by 6. Yes, it means the same: the two are false in exactly the same case (a number divisible by 6 that is not even), and no such number exists."),
            PQ("Is this true or false in the truth-table reading? \"If 7 is greater than 10, then 7 is greater than 20.\" Explain.",
               "True. The antecedent (7 is greater than 10) is false, so the conditional cannot be broken. A conditional is false only when the antecedent is true and the consequent false."),
            PQ("Write the converse of \"If a person is in Bamenda, then the person is in Cameroon\" and say whether it follows from the original.",
               "Converse: If a person is in Cameroon, then the person is in Bamenda. It does not follow. The original is true, but the converse is false: a person in Douala is in Cameroon and not in Bamenda."),
            SUM("A hypothetical proposition makes one statement depend on another. In \"If p then q\", p is the antecedent and q is the consequent.",
                "Common types: conditional (if ... then) and biconditional (if and only if). Books differ on the full list, so check your textbook.",
                "A conditional is false only when the antecedent is true and the consequent is false. In the other three cases it is true.",
                "The contrapositive (if not q then not p) has the same meaning. The converse and the inverse do not.",
                "The negation of \"If p then q\" is \"p and not q\". The word \"only if\" introduces the consequent."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Disjunctive propositions
    lesson(
        module=MODULE,
        topic="Disjunctive proposition and types",
        title="Disjunctive propositions: either ... or",
        slug="prop2-disjunctive-propositions",
        minutes=20,
        summary="A disjunctive proposition offers alternatives: either p or q. Learn the weak (inclusive) and strong (exclusive) types, their truth conditions, how to tell which is meant, and how to deny one.",
        objectives=[
            "Define a disjunctive proposition and name its alternatives (disjuncts)",
            "Distinguish the weak (inclusive) and strong (exclusive) disjunction by their truth conditions",
            "Decide from the context which kind is meant in an everyday sentence",
            "Write the correct negation of a disjunctive proposition",
        ],
        key_concepts=["Disjunctive proposition", "Alternatives (disjuncts)", "Inclusive (weak) disjunction", "Exclusive (strong) disjunction", "Exhaustive alternatives"],
        blocks=[
            H("Introduction"),
            T("At a Mobile Money kiosk in Douala a sign says: \"We accept MTN Mobile Money or Orange Money.\" "
              "A customer with both phones may use either one. At the same kiosk another sign says: \"Pay now or leave the shop.\" "
              "Here the customer will not do both."),
            T("Both signs use the word \"or\", yet they do not mean exactly the same. In logic we study this carefully, because "
              "a wrong reading of \"or\" spoils an argument."),
            D("A **disjunctive proposition** is a proposition that offers **alternatives** and says that at least one of them holds. "
              "Its usual form is: **Either** p **or** q.",
              title="Definition: disjunctive proposition",
              note="Example: Either we sell the land or we borrow the money."),
            D("The parts joined by \"or\" are the **alternatives**. Many books also call them the **disjuncts** (or, in older books, the alternants). "
              "A disjunctive proposition can have two alternatives or more: p or q or r.",
              title="Definition: alternatives (disjuncts)"),
            T("The Board's symbol for disjunction (alternation) is **v**, written p v q. It comes from the Latin word **vel**, which means \"or, perhaps both\"."),
            H("Two types: weak and strong"),
            KEY("Weak (inclusive) and strong (exclusive)", "Textbooks use both pairs of names. They mean the same thing.", cards=[
                ["Weak or inclusive: p v q", "At least one alternative is true. Both may be true. Latin: vel. Example: Applicants must know English or French. (Someone who knows both is welcome.)"],
                ["Strong or exclusive", "Exactly one alternative is true. Both cannot be true. Latin: aut. Example: A pupil is either in Form 5 or in Form 6. (Not in both.)"],
            ]),
            CODE("p  q  |  p v q (inclusive)  |  exclusive\nT  T  |         T          |      F\nT  F  |         T          |      T\nF  T  |         T          |      T\nF  F  |         F          |      F", "text", title="Truth tables for \"or\""),
            KEY("The only difference", "Look at the first row of the table.", cards=[
                ["Both alternatives true", "Inclusive: true. Exclusive: false."],
                ["Both alternatives false", "Both kinds: false. A disjunction needs at least one true alternative."],
            ]),
            T("The exclusive disjunction can be built from symbols you know: (p v q) . ~(p . q). In words: at least one, **and** not both."),
            H("Which \"or\" is meant?"),
            T("The word \"or\" alone does not tell you. Use these clues."),
            KEY("Clues in everyday speech", "Read the sentence and think about the situation.", cards=[
                ["Signs of exclusive", "The alternatives cannot both be true by their nature (a number is even or odd), or the words \"but not both\", \"one or the other\" are added, or the situation is a choice (tea or coffee on a menu with one drink included)."],
                ["Signs of inclusive", "Rules, laws, job advertisements and conditions usually allow both: \"a pass in French or English\". The words \"and/or\" also signal inclusive. Law and logic books usually read a plain \"or\" as inclusive unless told otherwise."],
                ["When unclear", "Treat \"or\" as inclusive in symbolic work (the Board's symbol v is inclusive), and ask or add \"but not both\" if the exclusive meaning matters."],
            ]),
            T("**Textbooks differ** on how to classify further types. Some also speak of a **complete** disjunction, where the alternatives cover all the possibilities "
              "(\"A number is either even or odd\"), and an **incomplete** one, where other possibilities are left open (\"Kofi will study law or medicine\": he might choose engineering). "
              "Some also separate a disjunction of whole propositions (\"Either it rains or the road is dry\") from a disjunction inside one proposition (\"Every candidate is either a boy or a girl\"). "
              "Check your textbook for the types your teacher expects."),
            H("Denying a disjunction"),
            D("To deny \"p or q\" (inclusive) you say that **neither** is true: ~p . ~q, which is also ~(p v q). "
              "Not-p or not-q is a different statement: it only says that they are not both true.",
              title="Definition: negation of a disjunction",
              note="Negation of \"Either Ako or Bih is at home\": \"Neither Ako nor Bih is at home.\""),
            EX("Worked example 1: inclusive or exclusive?", intro=(
                "Say which kind of \"or\" is most likely meant. "
                "(a) This number is either even or odd. "
                "(b) Students who play football or volleyball may join the sports day. "
                "(c) Kofi will visit Douala or Limbe this holiday."), steps=[
                S("(a) Exclusive", text="No whole number is both even and odd. The alternatives cannot both be true. They also cover every case, so this is a complete disjunction."),
                S("(b) Inclusive", text="A student who plays both games should clearly be welcome. The sentence is a rule that opens a door, not a choice of one."),
                S("(c) Unclear", text="Kofi might visit both towns in two weeks. The sentence does not say. To make it exclusive we add \"but not both\". To make it inclusive we add \"or both\"."),
            ]),
            EX("Worked example 2: truth values", intro=(
                "Give the truth value of each, first as an inclusive disjunction, then as an exclusive one. "
                "(a) Either 2 is even or 3 is odd. "
                "(b) Either 5 is even or Yaounde is in Cameroon. "
                "(c) Either 5 is even or Yaounde is in Chad."), steps=[
                S("(a) Both alternatives true", text="Inclusive: true. Exclusive: false."),
                S("(b) First false, second true", text="Exactly one is true. Inclusive: true. Exclusive: true."),
                S("(c) Both false", text="Neither is true. Inclusive: false. Exclusive: false."),
            ]),
            EX("Worked example 3: denying an \"or\"", intro=(
                "A teacher says: \"Either Mary or John broke the window.\" John proves the teacher wrong. "
                "What exactly has John proved?"), steps=[
                S("Deny the inclusive \"or\"", text="Neither of them broke it: Mary did not break it **and** John did not break it."),
                S("Test the wrong answer", text="\"Mary did not break it or John did not break it\" is not the denial. It is true even if Mary alone broke the window, and then the teacher was right."),
            ]),
            MISTAKE("Assuming \"or\" always means one or the other, but not both", "In logic and in law a plain \"or\" is usually inclusive. Only treat it as exclusive when the situation or the words say so."),
            MISTAKE("Negating \"p or q\" as \"not p or not q\"", "The denial of \"p or q\" is \"neither p nor q\" (not p and not q). Not-p or not-q only says that at least one of them is false."),
            MISTAKE("Thinking a disjunction is false when both alternatives are true", "That is true of the exclusive kind only. For the inclusive kind, both true gives true."),
            TIP("Disjunctive propositions appear in Paper 1 (inclusive or exclusive, truth values, negations) and in Paper 2 Section A (definitions and types). "
                "They return in Module 5 (truth tables) and in Module 8 (the disjunctive syllogism and the dilemma).", title="Exam link"),
            QUIZ("\"Either the school bus comes or I walk.\" The bus comes and I walk anyway to buy bread. In the inclusive reading the proposition is:",
                 ["True, because at least one alternative is true", "False, because both are true", "Neither true nor false", "False, because the alternatives are not exhaustive"], 0,
                 "In the inclusive reading, a disjunction is true when at least one alternative is true. Here both are true, so it is true.",
                 hint="Recall the first row of the truth table for the inclusive disjunction.",
                 feedback=["", "That is the exclusive reading. The question asks for the inclusive one.", "Every proposition in this course is either true or false.", "Alternatives need not be exhaustive for an inclusive disjunction to be true."]),
            QUIZ("What is the denial of \"Either the shop is open or the bank is open\" (inclusive)?",
                 ["The shop is closed or the bank is closed", "The shop is closed and the bank is closed", "The shop is open and the bank is open", "The shop is open or the bank is closed"], 1,
                 "The denial of an inclusive \"or\" says that neither alternative holds: the shop is closed and the bank is closed.",
                 hint="For \"or\" to be false, how many alternatives must be true?",
                 feedback=["This is true if only one of them is closed. The original could still be true then.", "", "This asserts that both alternatives are true. That is not the denial.", "This is not the denial: it may be true while the original is true as well."]),
            PQ("Complete the sentence: In an inclusive disjunction both alternatives may be true; in an exclusive disjunction ____.",
               "In an exclusive disjunction exactly one alternative is true. If both are true, the exclusive disjunction is false."),
            PQ("Classify as inclusive or exclusive and give a reason: \"The candidate must have a pass in Mathematics or in Physics.\"",
               "Inclusive. It is a requirement: a candidate with passes in both subjects satisfies it. Nothing in the sentence forbids having both."),
            PQ("Write the denial of \"Either Awa will cook rice or she will cook plantains\" (inclusive).",
               "Awa will not cook rice and she will not cook plantains. (In other words: she will cook neither.)"),
            PQ("Write the exclusive disjunction of p and q using the symbols ~, . and v only.",
               "(p v q) . ~(p . q). At least one is true, and they are not both true."),
            SUM("A disjunctive proposition offers alternatives (disjuncts): either p or q. The Board's symbol is v.",
                "Weak or inclusive: at least one alternative is true, both allowed. Strong or exclusive: exactly one is true.",
                "Both kinds are false when both alternatives are false. They differ only when both are true.",
                "Use the situation and the wording to decide which \"or\" is meant. In symbolic work, v is inclusive.",
                "The denial of \"p or q\" is \"neither p nor q\", not \"not p or not q\"."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Modal propositions
    lesson(
        module=MODULE,
        topic="Modal proposition and types",
        title="Modal propositions: necessity, possibility, impossibility",
        slug="prop2-modal-propositions",
        minutes=20,
        summary="A modal proposition says how something is true or false: necessarily, possibly, impossibly or contingently. Learn the four modes, the traditional kinds of modality and how the modes relate.",
        objectives=[
            "Define a modal proposition and tell it from a plain (assertoric) proposition",
            "State the meaning of necessary, possible, impossible and contingent in plain words",
            "Classify examples by their mode and use the links between the modes",
            "Deny a modal proposition correctly",
        ],
        key_concepts=["Modal proposition", "Assertoric proposition", "Necessity", "Possibility", "Impossibility", "Contingency", "Modality"],
        blocks=[
            H("Introduction"),
            T("Two football fans argue in Limbe. One says: \"Cameroon won the match.\" The other says: \"Cameroon **must** win the next match.\" "
              "A third says: \"Cameroon **might** win.\" A fourth says: \"Cameroon **cannot** win: they have no players.\""),
            T("The first statement only reports a fact. The other three say something about **how** the result is related to the facts: it must, it might, it cannot. "
              "These are the statements that logic calls **modal**."),
            D("A **modal proposition** is a proposition that says in what **mode** (manner) the predicate belongs to the subject, "
              "or in what mode something is so: necessarily, possibly, impossibly or contingently. "
              "Typical words: must, cannot, can, may, necessarily, possibly, it is certain that, it is impossible that.",
              title="Definition: modal proposition",
              note="Example: It is necessary that every triangle has three sides."),
            D("A plain proposition that only says that something is or is not so, without a mode, is called **assertoric**.",
              title="Definition: assertoric proposition",
              note="Example: The market is open today."),
            H("The four modes"),
            KEY("Necessity, possibility, impossibility, contingency", "Think of all the cases that could happen. Ask in which of them the statement is true.", cards=[
                ["Necessary", "True in every possible case. It cannot be false. Example: Every square has four sides."],
                ["Impossible", "True in no possible case. It cannot be true. Example: A square is round."],
                ["Possible", "True in at least one possible case. It can be true. (Everything necessary is also possible.) Example: Mount Cameroon will erupt again."],
                ["Contingent", "True in some cases and false in others. It can be true and it can be false. Example: It will rain in Kumba tomorrow."],
            ]),
            IMG("f5l-prop2-modal-cases.svg",
                alt="Three rows of five circles, one row each for necessary, contingent and impossible. Necessary: all five circles green. Contingent: three green and two white. Impossible: all five white.",
                caption="Figure 1. A statement is necessary if it is true in every case, impossible if it is true in none, and contingent if it is true in some cases only."),
            T("**A warning about everyday speech.** In ordinary talk, \"it is possible\" often suggests \"but maybe not\". In logic, \"possible\" only means \"not impossible\". "
              "So a necessary statement is also possible. If you mean \"possible but not necessary\", the word is **contingent**."),
            H("How the modes are linked"),
            KEY("Links between the modes", "Each one can be said in terms of another. These links hold in the usual textbook treatment (checked on a model with several possible cases).", cards=[
                ["Necessary and impossible", "It is necessary that p means the same as: it is impossible that not-p."],
                ["Possible and necessary", "It is possible that p means the same as: it is not necessary that not-p."],
                ["Contingent", "It is contingent that p means: it is possible that p and it is possible that not-p."],
                ["Fact between them", "If p is necessary, then p is true. If p is true, then p is possible. The reverse steps do not hold."],
            ]),
            T("Be careful: a true statement is not necessarily a necessary one. \"Cameroon has ten regions\" is true, but it could have been otherwise. It is true and **contingent**."),
            H("Types of modal proposition"),
            T("Books list the types of modality in different ways. Here are the common ones. **Check your textbook and follow your teacher's list.**"),
            KEY("Common ways of dividing modality", "These divisions are given in the traditional textbooks.", cards=[
                ["By the mode", "Necessity, possibility, impossibility and contingency, as above. Some books list only necessity, possibility and impossibility (with contingency as the case where neither necessity nor impossibility holds)."],
                ["Kant's three kinds of judgement", "Apodictic (necessary: \"A must be B\"), problematic (possible: \"A may be B\") and assertoric (plain fact: \"A is B\"). Some textbooks follow this list."],
                ["By the kind of necessity", "Logical or absolute (denying it contradicts itself: a married bachelor), natural or physical (the laws of nature: a stone released from the hand falls), and moral (what ought to be done). Names vary from book to book."],
            ]),
            T("The Board's symbol set has no signs for these modes. In this course we write modal propositions in words. "
              "A modal proposition is also not decided by the truth of its parts alone: \"Yaounde is the capital\" is true, and still not necessary."),
            EX("Worked example 1: classify the mode", intro=(
                "Say whether each statement is necessary, impossible or contingent. "
                "(a) Every triangle has three sides. "
                "(b) Some married man is a bachelor. "
                "(c) The river Mfoundi will flood this year. "
                "(d) Cameroon has ten regions."), steps=[
                S("(a) Necessary", text="By the meaning of the word \"triangle\", it cannot be false."),
                S("(b) Impossible", text="By the meaning of \"bachelor\" (an unmarried man), it cannot be true."),
                S("(c) Contingent", text="It might happen and might not. Nothing in the meaning of the words settles it."),
                S("(d) Contingent", text="It is true today, but the number of regions could have been different. Truth is not necessity."),
            ]),
            EX("Worked example 2: say it another way", intro=(
                "Rewrite using the links between the modes. "
                "(a) It is impossible that the examination is cancelled. "
                "(b) It is possible that it rains tomorrow."), steps=[
                S("(a) Necessary and impossible are linked", text="It is necessary that the examination is **not** cancelled."),
                S("(b) Possible and necessary are linked", text="It is **not** necessary that it does **not** rain tomorrow."),
            ]),
            EX("Worked example 3: denying a modal proposition", intro=(
                "A manager says: \"It is necessary that the bus is on time.\" A driver wants to deny this. What does he need to show?"), steps=[
                S("Necessary means true in every case", text="To deny it, he needs one case where the bus is **not** on time."),
                S("State the denial", text="It is **possible** that the bus is not on time."),
                S("Check the wrong answer", text="\"It is necessary that the bus is not on time\" is far stronger. It says that the bus can never be on time. That is not the denial."),
            ]),
            MISTAKE("Treating \"true\" as \"necessary\"", "Most true statements about the world are contingent: they could have been false. Necessity means true in every possible case."),
            MISTAKE("Denying \"necessary\" by saying \"impossible\"", "The denial of \"it is necessary that p\" is \"it is possible that not-p\". Impossible is a much stronger claim."),
            MISTAKE("Mixing up \"possible\" and \"probable\"", "Probable means likely. A statement can be possible and very unlikely. Possible only means that it is not impossible."),
            TIP("Modal propositions appear mostly in Paper 1 (naming the mode, using the links between the modes) and in Paper 2 Section A (definition, types, examples). "
                "Always give an example of each mode and say clearly in plain words what it means.", title="Exam link"),
            QUIZ("\"A triangle has four sides.\" Its mode is:",
                 ["Necessary", "Contingent", "Impossible", "Possible but not impossible"], 2,
                 "By the meaning of \"triangle\" the statement cannot be true in any case. It is impossible.",
                 hint="Ask: could there be any case in which this is true?",
                 feedback=["Necessary would mean true in every case. Here it is true in none.", "Contingent statements are true in some cases. This one is true in none.", "", "A statement true in no case is not possible in the logical sense."]),
            QUIZ("\"The Cameroonian national team will qualify for the next tournament.\" Which description is best?",
                 ["Necessary", "Impossible", "Contingent", "Assertoric, with no mode at all"], 2,
                 "It may happen and it may not. It is contingent. It is not decided by the meaning of the words, and it can be true or false.",
                 hint="Can you imagine it turning out either way?",
                 feedback=["Nothing forces the team to qualify, so it is not true in every case.", "It is certainly not impossible that they qualify.", "", "It speaks about the future in a way that is not settled, and the question asks about its mode."]),
            PQ("Define a modal proposition and give one example.",
               "A modal proposition states the mode in which something is so: necessarily, possibly, impossibly or contingently. Example: It is impossible that a circle has corners. A plain proposition such as \"The shop is open\" is assertoric, not modal."),
            PQ("Rewrite \"It is necessary that water at sea level boils at 100 degrees Celsius\" using \"impossible\".",
               "It is impossible that water at sea level does not boil at 100 degrees Celsius. (Necessary p means impossible not-p.)"),
            PQ("Write the denial of \"It is possible that the road floods.\"",
               "It is not possible that the road floods, which means: it is impossible that the road floods. (If it is not possible that p, then it is necessary that not-p.)"),
            PQ("\"The school has 600 pupils\" is true. Is it therefore necessary? Explain.",
               "No. It is true but contingent. The school could have had a different number of pupils, so the statement is not true in every possible case."),
            SUM("A modal proposition says in what mode something is so. A plain statement of fact is assertoric.",
                "Necessary: true in every possible case. Impossible: true in none. Possible: true in at least one. Contingent: true in some and false in others.",
                "Necessary p means impossible not-p. Possible p means not necessary not-p. Necessary implies true implies possible.",
                "Types of modality are listed differently in different books: check your textbook.",
                "Do not confuse true with necessary, possible with probable, or the denial of necessary with impossible."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Translating ordinary sentences
    lesson(
        module=MODULE,
        topic="Translating ordinary propositions into standard forms",
        title="Translating ordinary sentences into A, E, I and O",
        slug="prop2-translating-ordinary-sentences-into-categorical-forms",
        minutes=25,
        summary="Turn everyday sentences into the four standard categorical forms A, E, I and O: singular statements, only, none but, all except, whenever, everyone who and nobody, with a check for each.",
        objectives=[
            "State the standard forms A, E, I and O and the five-step method for translating into them",
            "Translate singular propositions and sentences with quantity words such as every, no, some and not all",
            "Translate only, none but, all except and adverbial forms (whenever, wherever, never) correctly",
            "Test a translation to be sure that it keeps the meaning of the original",
        ],
        key_concepts=["Standard form", "Quantifier", "Copula", "Singular proposition", "Exceptive proposition", "Parameter", "Translation"],
        blocks=[
            H("Introduction"),
            T("Nobody speaks in the neat sentences of a logic book. A father says: \"Only members may vote.\" A teacher says: \"Whenever it rains heavily, the road floods.\" "
              "A neighbour says: \"Nobody who cheated passed.\" To reason about such sentences we first **translate** them into a standard shape, "
              "so that we can see exactly what they claim."),
            D("A categorical proposition is in **standard form** when it has this shape: **quantifier** (All, No, Some) + **subject term** + **copula** (are, are not) + **predicate term**. "
              "Both terms name classes (groups of things).",
              title="Definition: standard form",
              note="Quantity is universal (All, No) or particular (Some). Quality is affirmative or negative."),
            KEY("The four standard forms", "These are the forms from the earlier lessons of this module.", cards=[
                ["A: All S are P", "Universal affirmative"],
                ["E: No S are P", "Universal negative"],
                ["I: Some S are P", "Particular affirmative"],
                ["O: Some S are not P", "Particular negative"],
            ]),
            T("**Which reading?** The translations in this lesson are correct in the traditional reading and in the modern (Venn) reading. "
              "They differ only in whether \"All S are P\" also claims that there are S. Where your textbook says more, follow your teacher."),
            H("The five-step method"),
            KEY("Translate in five steps", "Use the same steps every time.", cards=[
                ["1. Find the two classes", "What is the sentence talking about (subject)? What does it say about them (predicate)?"],
                ["2. Decide the quantity", "Does it speak of every member (universal) or of some (particular)?"],
                ["3. Decide the quality", "Does it affirm (are) or deny (are not)?"],
                ["4. Make both terms class names", "Turn verbs and adjectives into nouns: \"Dogs bark\" becomes \"barking animals\". This noun is called a parameter."],
                ["5. Write and test", "Write the standard form, then test it on a case: does it say the same thing as the original?"],
            ]),
            H("Words that show quantity"),
            KEY("Quantity and quality words", "Many everyday words point to a standard form.", cards=[
                ["A: All S are P", "all, every, each, any, whoever, everyone who, a (meaning every, as in \"A lion is a carnivore\")"],
                ["E: No S are P", "no, none, nobody, no one, nothing, never, not any, \"not a single\""],
                ["I: Some S are P", "some, there are, there exist, at least one, a few, several, a (meaning some, as in \"A student came\")"],
                ["O: Some S are not P", "some ... are not, not all, not every, \"there are ... that are not\""],
            ]),
            T("The article \"a\" can mean \"every\" or \"some\". Decide from the sense. \"A whale is a mammal\" is about every whale. \"A student has called\" is about some student."),
            H("Singular propositions"),
            D("A **singular proposition** speaks about one named person or thing. Traditional textbooks treat it as universal and put it in **A** or **E**, "
              "because the whole of the one-member class is being spoken about.",
              title="Definition: singular proposition",
              note="\"Ako is a student\" becomes \"All persons identical with Ako are students\" (A). \"Ako did not cheat\" becomes \"No persons identical with Ako are persons who cheated\" (E)."),
            H("Only and none but"),
            D("\"Only S are P\", \"None but S are P\" and \"Nothing but S is P\" all translate to **All P are S**. The two terms **swap places**.",
              title="Rule: only and none but",
              note="\"Only members may vote\" becomes \"All persons who may vote are members.\""),
            IMG("f5l-prop2-only-venn.svg",
                alt="A large circle labelled M for members of the club. Inside it, a smaller circle labelled V for voters. Nothing in V lies outside M.",
                caption="Figure 1. \"Only members may vote.\" Every voter (V) is inside the circle of members (M). Members who do not vote are allowed: they are in M but outside V."),
            T("We checked this rule by testing all possible situations on a small set: \"Only S are P\" always has the same truth value as \"All P are S\" and as \"No non-S are P\". "
              "It is **not** the same as \"All S are P\"."),
            H("All except"),
            D("An **exceptive proposition** (all except, all but) makes two claims. \"All except S are P\" says: **No S are P** and **All non-S are P**. "
              "It is a pair of standard-form propositions. Some books treat it as one compound proposition, others as two statements: check your textbook.",
              title="Definition: exceptive proposition",
              note="\"All students except first-years may enter the hall\" becomes (1) No first-years are students who may enter the hall (E) and (2) All students who are not first-years are students who may enter the hall (A)."),
            IMG("f5l-prop2-except-venn.svg",
                alt="A large rectangle for all students, shaded green. A white circle inside it labelled F for first-years. The shaded green region outside the circle is labelled E, allowed to enter.",
                caption="Figure 2. \"All except first-years may enter.\" The shaded region (everyone outside the circle F) is exactly the group allowed to enter. The circle F is outside that group."),
            H("Adverbial forms and who, when, where"),
            T("Some sentences speak of times and places, or use words such as \"whenever\" and \"whoever\". Turn the time, the place or the person into the class."),
            KEY("Patterns", "Each pattern becomes a standard form with a class of times, places or persons.", cards=[
                ["Whenever / always", "\"Whenever it rains heavily, the road floods\" becomes \"All times when it rains heavily are times when the road floods.\" (A)"],
                ["Wherever", "\"Wherever there is smoke, there is fire\" becomes \"All places where there is smoke are places where there is fire.\" (A)"],
                ["Never", "\"He never arrives late\" becomes \"No times when he arrives are times when he is late.\" (E)"],
                ["Everyone who / whoever", "\"Everyone who cheats is punished\" becomes \"All persons who cheat are persons who are punished.\" (A)"],
                ["Nobody who", "\"Nobody who cheated passed\" becomes \"No persons who cheated are persons who passed.\" (E)"],
            ]),
            EX("Worked example 1: only", intro=(
                "Translate \"Only registered students may vote in the school election\" into standard form."), steps=[
                S("Find the classes", text="Voters (persons who may vote) and registered students."),
                S("\"Only\" swaps the terms", text="\"Only R are V\" becomes \"All V are R\"."),
                S("Write it", text="All persons who may vote in the school election are registered students. (A)"),
                S("Test with a case", text="Biye may vote. Does it follow that she is registered? Yes. Does it follow that every registered student votes? No. The translation says the first and not the second, as the original does."),
            ]),
            EX("Worked example 2: all except", intro=(
                "Translate \"All the girls except Biye passed the test\" into standard form."), steps=[
                S("It is exceptive: two claims", text="Biye did not pass; all other girls passed. (We assume that Biye is one of the girls.)"),
                S("First claim", text="No persons identical with Biye are girls who passed the test. (E)"),
                S("Second claim", text="All girls who are not Biye are girls who passed the test. (A)"),
            ]),
            EX("Worked example 3: mixed sentences", intro=(
                "Translate each sentence. "
                "(a) Mount Cameroon is a volcano. "
                "(b) Wherever there is a market, there is traffic. "
                "(c) Not every trader is honest. "
                "(d) Nobody who cheated passed."), steps=[
                S("(a) Singular, affirmative", text="All things identical with Mount Cameroon are volcanoes. (A)"),
                S("(b) Place word with \"wherever\"", text="All places where there is a market are places where there is traffic. (A)"),
                S("(c) \"Not every\" denies a universal", text="Some traders are not honest persons. (O)"),
                S("(d) \"Nobody\" is a universal negative", text="No persons who cheated are persons who passed. (E)"),
            ]),
            MISTAKE("Not swapping the terms for \"only\"", "\"Only S are P\" is \"All P are S\". Writing \"All S are P\" says something different: in the example \"Only members vote\", it would claim that every member votes."),
            MISTAKE("Reading \"All S are not P\" as O without asking", "\"All students are not present\" can mean \"No students are present\" (E) or \"Not all students are present\" (O). Decide from the context. In your own writing, avoid the phrase."),
            MISTAKE("Leaving a verb in the predicate", "A standard form needs a noun or a noun phrase after \"are\". Do not write \"All dogs bark\". Write \"All dogs are barking animals\"."),
            MISTAKE("Changing the meaning to fit the form", "\"Most traders are honest\" does not fit exactly into any of the four forms. Writing \"Some traders are honest\" keeps only part of the meaning. Check your textbook for how your course treats such sentences."),
            TIP("Translation into standard form appears in Paper 1 (which standard form matches the sentence) and in Paper 2 Sections A and B, as the first step before testing an argument. "
                "Write the translation, then test it with a case.", title="Exam link"),
            QUIZ("\"None but graduates are eligible for the post.\" The correct standard form is:",
                 ["All graduates are eligible persons", "All eligible persons are graduates", "No graduates are eligible persons", "Some graduates are eligible persons"], 1,
                 "\"None but\" works like \"only\": it swaps the terms. All eligible persons are graduates (A).",
                 hint="Who is being limited: the eligible persons or the graduates?",
                 feedback=["This keeps the terms in the same order. It says that every graduate is eligible, which the sentence does not say.", "", "The sentence is not about excluding graduates. It excludes non-graduates.", "This is too weak and the order is wrong."]),
            QUIZ("\"Whenever the generator runs, the machines work.\" Which is the correct translation?",
                 ["All machines are generators", "Some times when the generator runs are times when the machines work", "All times when the generator runs are times when the machines work", "No times when the generator runs are times when the machines work"], 2,
                 "\"Whenever\" speaks of every time: all times when the generator runs are times when the machines work (A).",
                 hint="Make the class \"times when ...\".",
                 feedback=["The classes must be times, not objects. The sentence is not about machines and generators as things.", "\"Whenever\" is universal, so \"some times\" is too weak.", "", "That is the opposite: it denies the claim."]),
            PQ("Translate into standard form: \"Only citizens may vote in a national election.\"",
               "All persons who may vote in a national election are citizens. (A) The terms swap places because of \"only\"."),
            PQ("Translate \"Nothing that is stolen is a gift\" into standard form.",
               "No stolen things are gifts. (E) \"Nothing\" gives a universal negative."),
            PQ("Translate \"Everyone except the captain came to training\" into two standard-form propositions.",
               "(1) No persons identical with the captain are persons who came to training. (E) (2) All persons who are not the captain are persons who came to training. (A) Assumed: the captain is one of the group."),
            PQ("Translate \"Not all pupils passed\" and say which form it is.",
               "Some pupils are not persons who passed. This is an O proposition. \"Not all\" denies the universal claim \"All pupils passed\"."),
            SUM("Standard form = quantifier + subject + copula + predicate. The four forms: A, E, I, O.",
                "Method: find the classes, decide quantity and quality, make both terms class names, write, then test.",
                "Singular propositions are treated as universal (A or E). \"Only\" and \"none but\" swap the terms. \"All except\" gives two propositions.",
                "Adverbial and pronoun forms (whenever, wherever, never, everyone who, nobody) use classes of times, places and persons.",
                "Always test your translation. Check your textbook where it handles singular propositions, exceptives or \"most\" differently."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Translating between forms
    lesson(
        module=MODULE,
        topic="Translating ordinary propositions into standard forms",
        title="Translating between forms: categorical, hypothetical, disjunctive",
        slug="prop2-translating-between-forms",
        minutes=24,
        summary="Say the same proposition in another form: categorical to hypothetical or disjunctive and back, if-then to either-or, and A to E by obversion. Only checked equivalences, plus the common mistakes.",
        objectives=[
            "Rewrite A, E, I and O propositions as general hypothetical and disjunctive propositions, and back",
            "Convert between if-then and either-or propositions using checked equivalences",
            "Say when a conversion is NOT allowed (converse, inverse, exclusive or)",
            "Test a conversion on a case to see that the meaning has not changed",
        ],
        key_concepts=["Equivalent propositions", "General hypothetical", "Obversion", "Contrapositive", "Unless", "Exclusive disjunction"],
        blocks=[
            H("Introduction"),
            T("The school rule can be written in three ways. \"All students who cheat are expelled.\" "
              "\"If a student cheats, then he is expelled.\" \"Either a student does not cheat or he is expelled.\" "
              "A good reasoner knows that these say the **same thing**, and also knows which similar-looking sentences do **not**."),
            D("Two propositions are **equivalent** when they are true in exactly the same situations and false in exactly the same situations. "
              "Only equivalent forms may replace each other in an argument.",
              title="Definition: equivalent propositions",
              note="Every equivalence below was tested on all situations of a small universe (by computer) or by a full truth table."),
            T("**Which view?** The links between categorical and hypothetical forms below use the modern (Venn) reading of \"All S are P\": "
              "it says that nothing is S and not P, and it does not claim that any S exists. "
              "In the traditional reading \"All S are P\" also implies that there are S, so the hypothetical form says slightly less. Check your textbook."),
            H("Categorical to hypothetical and disjunctive"),
            KEY("The four forms said in other ways", "\"x\" stands for any one thing in the universe we are talking about.", cards=[
                ["A: All S are P", "If anything is S, then it is P. Or: Everything is either not S or P. Or: No S are non-P."],
                ["E: No S are P", "If anything is S, then it is not P. Or: Everything is either not S or not P."],
                ["I: Some S are P", "There is something that is both S and P. (Not: if anything is S then it is P: that is the A form.)"],
                ["O: Some S are not P", "There is something that is S and is not P. It is the denial of the A form."],
            ]),
            T("This kind of conditional is called a **general hypothetical**. It speaks about any member of a class, not about one case. "
              "That is why \"All students who cheat are expelled\" can be written as \"If a student cheats, he is expelled\"."),
            H("Hypothetical back to categorical"),
            T("A hypothetical can be turned into a categorical when it is general: it speaks about any case. "
              "A conditional about one event can also be turned into a categorical by using classes of **cases** or **occasions**, as in the previous lesson."),
            KEY("Examples", "Reading left to right and right to left.", cards=[
                ["General conditional", "\"If a trader sells fake medicine, she is guilty\" becomes \"All traders who sell fake medicine are guilty persons.\""],
                ["Whenever form", "\"If it rains, the match is cancelled\" becomes \"All occasions when it rains are occasions when the match is cancelled.\""],
                ["Not allowed", "\"All traders who sell fake medicine are guilty\" does not become \"If a trader is guilty, she sells fake medicine.\" That swaps the terms."],
            ]),
            H("If-then and either-or"),
            T("Now we work with whole propositions p and q and the Board's symbols. Each line below has been checked by a truth table."),
            CODE("p  q  | p ⊃ q | ~p v q | ~(p . ~q) | ~q ⊃ ~p | q ⊃ p\nT  T  |   T   |   T    |     T     |    T     |   T\nT  F  |   F   |   F    |     F     |    F     |   T\nF  T  |   T   |   T    |     T     |    T     |   F\nF  F  |   T   |   T    |     T     |    T     |   T", "text", title="Equivalent forms of p ⊃ q"),
            KEY("What the table shows", "The first four columns are identical. The last column is different.", cards=[
                ["If p then q is the same as", "not-p or q (~p v q), and not (p and not-q) (~(p . ~q)), and if not-q then not-p (~q ⊃ ~p)."],
                ["Not the same", "q ⊃ p (the converse). In the table it differs from the first column in rows 2 and 3."],
                ["Either-or to if-then", "p v q is the same as ~p ⊃ q, and also the same as ~q ⊃ p. \"Either the bridge is repaired or the bus will not run\" is the same as \"If the bridge is not repaired, the bus will not run\"."],
            ]),
            D("\"p **unless** q\" is usually written as \"if not q then p\" (~q ⊃ p). This is equivalent to p v q.",
              title="Rule: unless",
              note="\"The match goes ahead unless it rains\" = \"If it does not rain, the match goes ahead\" = \"The match goes ahead or it rains\"."),
            KEY("Exclusive or is more than if-then", "The exclusive \"either p or q but not both\" cannot be written as ~p ⊃ q alone, because ~p ⊃ q is the inclusive one.", cards=[
                ["Exclusive or as two parts", "(p v q) . ~(p . q)"],
                ["Exclusive or as a biconditional", "p ≡ ~q: p is true exactly when q is false."],
            ]),
            H("From one categorical form to another"),
            T("There are also checked conversions between standard forms. They are studied again in the Module 6 lessons on eduction (obversion, conversion, contraposition). "
              "Two are safe here."),
            KEY("Safe conversions", "Checked in the same way as above.", cards=[
                ["All S are P = No S are non-P", "Change the quality and replace the predicate by its complement (obversion). Also: All S are P = All non-P are non-S."],
                ["Some S are P = Some S are not non-P", "Obversion of the I proposition."],
                ["Not equivalent", "All S are P and All P are S. Also: No S are P and Some S are not P. Also: All S are P and Some S are P in the modern reading."],
            ]),
            EX("Worked example 1: categorical to hypothetical and disjunctive", intro=(
                "Write \"All students who cheat are expelled\" as (a) a hypothetical and (b) a disjunctive proposition. Test it."), steps=[
                S("(a) Hypothetical", text="If a student cheats, then he is expelled."),
                S("(b) Disjunctive", text="For any person: either he is not a student who cheats, or he is expelled."),
                S("Test on a case", text="Kofi cheats and is not expelled. The original is false, and so are (a) and (b). Bih does not cheat and is not expelled: all three are true. Same truth in each case."),
            ]),
            EX("Worked example 2: either-or to if-then", intro=(
                "Write \"Either the bridge is repaired or the bus will not run\" as two different conditionals."), steps=[
                S("Name the parts", text="p: the bridge is repaired. q: the bus will not run."),
                S("p v q is the same as ~p ⊃ q", text="If the bridge is not repaired, then the bus will not run."),
                S("p v q is also the same as ~q ⊃ p", text="~q is \"the bus runs\". If the bus runs, then the bridge is repaired."),
                S("Test with the table", text="p false and q false is the only case in which the disjunction is false. The bridge is not repaired and the bus runs. Both conditionals are false in exactly that case."),
            ]),
            EX("Worked example 3: exclusive or", intro=(
                "\"Either I go to Limbe or I go to Kribi\" (not both). Write it as a biconditional."), steps=[
                S("Name the parts", text="p: I go to Limbe. q: I go to Kribi."),
                S("Exactly one is true", text="(p v q) . ~(p . q)"),
                S("Say it as a biconditional", text="p ≡ ~q: I go to Limbe if and only if I do not go to Kribi."),
                S("Check the table", text="p true and q true makes ~q false, so p ≡ ~q is false, as the exclusive reading wants. p true and q false gives true. p false and q true gives true. p false and q false gives false."),
            ]),
            MISTAKE("Using the converse as if it were equivalent", "\"All S are P\" and \"All P are S\" are different. \"If p then q\" and \"If q then p\" are different. Check by an example: All Cameroonians are Africans, not all Africans are Cameroonians."),
            MISTAKE("Using the inverse", "\"If not p then not q\" does not follow from \"If p then q\". The contrapositive (if not q then not p) does."),
            MISTAKE("Turning an exclusive or into ~p ⊃ q", "That keeps \"at least one\" but drops \"not both\". Add (not both) or use p ≡ ~q."),
            MISTAKE("Turning \"No S are P\" into \"Not all S are P\"", "\"No S are P\" (E) is stronger. \"Not all S are P\" is O. In the traditional reading E implies O, but O never implies E. In the modern reading neither implies the other. Do not treat them as equivalent."),
            TIP("Questions in Paper 1 often ask which proposition is equivalent to a given one (the contrapositive, the disjunctive form, the correct hypothetical). "
                "In Paper 2 a conversion is a step in an argument. Give the new form, then test it.", title="Exam link"),
            QUIZ("Which proposition is equivalent to \"If the shop is open, then the owner is present\"?",
                 ["If the owner is present, then the shop is open", "If the shop is not open, then the owner is not present", "If the owner is not present, then the shop is not open", "The shop is open and the owner is present"], 2,
                 "The equivalent form is the contrapositive: if the owner is not present, then the shop is not open.",
                 hint="Swap the parts and negate both.",
                 feedback=["That is the converse. It is not equivalent.", "That is the inverse. It is not equivalent.", "", "That asserts both parts. The original only links them."]),
            QUIZ("\"Either Ako pays the fee or he cannot sit the exam.\" (inclusive). Which is equivalent?",
                 ["If Ako pays the fee, he cannot sit the exam", "If Ako does not pay the fee, he cannot sit the exam", "If Ako cannot sit the exam, he paid the fee", "Ako pays the fee and he cannot sit the exam"], 1,
                 "p v q is equivalent to ~p ⊃ q: if he does not pay, he cannot sit.",
                 hint="Deny the first alternative and say that the second must hold.",
                 feedback=["This links paying to not sitting, the opposite of the sense of the sentence.", "", "This is the converse of the right conditional. It would be false when he cannot sit and did not pay, which is exactly the case the sentence expects.", "A conjunction is not a disjunction."]),
            PQ("Write \"All taxis in the town are registered\" as an if-then proposition and as an either-or proposition.",
               "If something is a taxi in the town, then it is registered. Either a thing is not a taxi in the town or it is registered."),
            PQ("Write \"The match goes ahead unless it rains\" as an if-then and as a disjunction.",
               "If it does not rain, then the match goes ahead (~q ⊃ p). The match goes ahead or it rains (p v q)."),
            PQ("Is \"If you work, you will pass\" equivalent to \"If you do not work, you will not pass\"? Give the reason.",
               "No. The second is the inverse. A person who does not work might still pass (by luck, or because he learned earlier) and then the second is false while the first is true. The contrapositive of the first is \"If you do not pass, you did not work\"."),
            PQ("Write \"No snakes are friendly animals\" in an if-then form.",
               "If something is a snake, then it is not a friendly animal."),
            SUM("Equivalent propositions are true and false in exactly the same cases. Only equivalent forms may replace each other.",
                "A: All S are P = if anything is S then it is P = everything is not S or P = No S are non-P. E: No S are P = if anything is S then it is not P.",
                "p ⊃ q = ~p v q = ~(p . ~q) = ~q ⊃ ~p. p v q = ~p ⊃ q. The word unless gives p unless q = ~q ⊃ p.",
                "Exclusive or is (p v q) . ~(p . q), or p ≡ ~q. It is not just ~p ⊃ q.",
                "Not equivalent: the converse, the inverse, All S are P versus All P are S. Check your textbook on the traditional versus modern reading of A."),
        ],
    ),
]
