"""Form 5 Logic (O Level 0590), module "The Third Operation of the Mind: Reasoning (Inference)".
Draft content: check against the official syllabus.

Opposition and eduction use the TRADITIONAL (Aristotelian) view with existential import; the Boolean
difference is stated where it matters. Verified by brute force over all Venn-region fillings."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "The Third Operation of the Mind: Reasoning (Inference)"

LESSONS = [
    # ------------------------------------------------------------------ Methods of reasoning
    lesson(
        module=MODULE,
        topic="Methods of reasoning",
        title="Methods of reasoning: deduction, induction and analogy",
        slug="inf-methods-of-reasoning",
        minutes=20,
        summary="Reasoning moves from known facts to a new conclusion by deduction (certain if the premises are true), induction (probable) or analogy (probable, based on likeness).",
        objectives=[
            "Define reasoning and name its three main methods: deduction, induction and analogy",
            "Tell a deductive argument from an inductive one and from an argument by analogy",
            "Explain why a deductive conclusion is certain but an inductive one is only probable",
            "Recognise each method in everyday situations",
        ],
        key_concepts=["Reasoning", "Deduction", "Induction", "Analogy", "Premise", "Conclusion", "Certain and probable"],
        blocks=[
            H("Introduction"),
            T("A trader at the Mokolo market in Yaounde hears that the price of tomatoes went up three market days in a row. "
              "She thinks: \"It will probably go up again next week, so I will buy more today.\" "
              "Later she reads on her phone that all vehicles on a certain road must pay a toll, and she sees that her cousin's pick-up is on that road. "
              "She thinks: \"So my cousin must pay the toll.\""),
            T("Both thoughts are **reasoning**. In each case she starts from something she already knows and reaches something new. "
              "But the two thoughts are not equally strong. The second is certain, the first is only likely. "
              "This lesson shows the three main methods of reasoning and what each one can promise."),
            D("**Reasoning** is the mind's act of passing from one or more things already known to a new thing that follows from them. "
              "The known things are the **premises**. The new thing is the **conclusion**.",
              title="Definition: reasoning",
              note="Reasoning is the third operation of the mind. The first is simple apprehension (forming ideas and terms). The second is judging (forming propositions)."),
            H("Deduction"),
            D("**Deduction** is the method of reasoning in which the conclusion follows with certainty from the premises: "
              "if the premises are true and the reasoning is correct, the conclusion cannot be false.",
              title="Definition: deduction",
              note="Traditionally, deduction is described as going from the general to the particular. What matters most is the certainty of the link."),
            CODE("Premise 1: All students who miss the GCE registration deadline are refused entry.\n"
                 "Premise 2: Ngu missed the GCE registration deadline.\n"
                 "Conclusion: Ngu is refused entry.", "text", title="A deduction"),
            T("The conclusion is not \"probably\" true. If both premises are true, Ngu is refused entry. "
              "Nothing outside the premises can change that. This is why deduction is the strongest kind of reasoning."),
            H("Induction"),
            D("**Induction** is the method of reasoning in which we study some cases and conclude something about more cases, usually about all cases of that kind. "
              "The conclusion goes beyond the premises, so it is only **probable**, never certain.",
              title="Definition: induction",
              note="Traditionally, induction is described as going from the particular to the general."),
            CODE("Premise 1: The first mango I picked from this tree was sweet.\n"
                 "Premise 2: The second mango was sweet.\n"
                 "Premise 3: The third mango was sweet.\n"
                 "Conclusion: All the mangoes on this tree are sweet.", "text", title="An induction"),
            T("Three sweet mangoes make the conclusion likely. The fourth mango may still be sour, and then the conclusion is false even though all three premises were true. "
              "More cases, and more varied cases, make an induction stronger. A few cases make it weak. "
              "Weather forecasts, farming advice and medical findings all use induction."),
            H("Analogy"),
            D("**Analogy** is the method of reasoning in which two things are alike in some known ways, and we conclude that they are alike in one more way. "
              "The conclusion is **probable**, not certain.",
              title="Definition: argument by analogy",
              note="Not every book lists analogy as a third method. Some treat it as a kind of induction. Follow your teacher's textbook."),
            CODE("Premise 1: Last season, cocoa farm A and farm B had the same soil, the same rain and the same trees.\n"
                 "Premise 2: Farm A gave a good harvest after using the new fertiliser.\n"
                 "Conclusion: Farm B will also give a good harvest after using the new fertiliser.", "text", title="An argument by analogy"),
            KEY("Certain or probable?", "The method decides how strong the conclusion can be.", cards=[
                ["Deduction", "Conclusion follows with certainty if the premises are true. Nothing new is added beyond what the premises already contain."],
                ["Induction", "Conclusion is probable. It says more than the premises said, so it can be wrong."],
                ["Analogy", "Conclusion is probable. It rests on likeness, so the more important likenesses, the stronger it is."],
            ]),
            EX("Worked example 1: naming the method", intro=(
                "Name the method of reasoning: \"Every Form 5 student at our school has a school ID card. Mbarga is a Form 5 student at our school. So Mbarga has a school ID card.\""), steps=[
                S("Look at the premises", text="The first premise is about every Form 5 student. The second is about one student, Mbarga."),
                S("Look at the direction", text="We go from a general statement to one particular person."),
                S("Check the strength", text="If both premises are true, Mbarga certainly has an ID card. The conclusion is certain."),
                S("Name the method", text="This is **deduction**."),
            ]),
            EX("Worked example 2: naming the method", intro=(
                "Name the method: \"In June, July and August this year it rained every afternoon in Buea. So it will rain every afternoon next August too.\""), steps=[
                S("Look at the premises", text="They describe a few particular cases: three months of afternoon rain."),
                S("Look at the conclusion", text="It says the pattern will hold again. It goes beyond what we have seen."),
                S("Check the strength", text="The pattern may change. The conclusion is only probable."),
                S("Name the method", text="This is **induction**."),
            ]),
            EX("Worked example 3: comparing the strength of two conclusions", intro=(
                "Anna says: \"All taxis in this town have a yellow stripe. This car has a yellow stripe, so it is a taxi.\" "
                "Bih says: \"Four of the five taxis I took this week were late, so the next taxi will probably be late.\" Whose conclusion is certain?"), steps=[
                S("Read Bih's argument", text="It uses a few cases to say what will probably happen. It is induction, so the conclusion is only probable."),
                S("Read Anna's argument", text="It looks like deduction, but check the form. \"All taxis have a stripe\" does not say that only taxis have a stripe. "
                                              "A private car may also have a stripe."),
                S("Decide", text="Neither conclusion is certain. Bih's is probable by its nature. Anna's reasoning is badly built, so it proves nothing."),
                S("Lesson", text="A deductive method gives certainty only when the reasoning is also correct. You will study this under validity."),
            ]),
            H("Common mistakes and the exam"),
            MISTAKE("Thinking \"deduction means general to particular\" is the whole story",
                    "Use the strength of the conclusion as your test. In deduction the conclusion cannot be false if the premises are true. In induction and analogy it can."),
            MISTAKE("Calling a probable conclusion \"false\"",
                    "An inductive conclusion can be strong, weak, likely or unlikely. It is not called certain or false just by being inductive. Examiners expect the word probable."),
            MISTAKE("Mixing up induction and analogy",
                    "Induction goes from several cases of a kind to the whole kind. Analogy goes from one case to another case because they are alike."),
            TIP("Paper 1 asks you to identify the method in a short example, or to say which method gives a certain conclusion. "
                "Paper 2 Section A may ask you to define deduction and induction and give an example of each. Always give a one-line example from daily life.",
                title="Exam link"),
            QUIZ("\"Every student who scores below 10 in the test must repeat the exercise. Etta scored 7, so Etta must repeat the exercise.\" Which method is this?",
                 ["Induction", "Deduction", "Analogy", "None, because it is not reasoning"], 1,
                 "A general rule is applied to one case and the conclusion is certain if the premises are true: deduction.",
                 hint="Is the conclusion certain, given the premises?",
                 feedback=["Induction goes from a few cases to a general conclusion. Here the general rule is already given.", "",
                           "Analogy compares two similar things. Nothing is compared here.",
                           "It is reasoning: premises lead to a conclusion."]),
            QUIZ("Which statement about the conclusion of an induction is correct?",
                 ["It is certain if the premises are true.", "It is probable and may still be false.", "It is always false.", "It is always the same as one of the premises."], 1,
                 "An inductive conclusion goes beyond the premises, so it is only probable.",
                 hint="Think of the fourth mango.",
                 feedback=["That is true of deduction, not induction.", "",
                           "A good induction is likely to be true. It is not always false.",
                           "Then there would be nothing new in it."]),
            PQ("Define deduction and induction and say which gives the stronger conclusion. Give a daily-life example of each.",
               "Deduction is reasoning in which the conclusion follows with certainty from the premises. Example: all taxis must stop at the checkpoint; this is a taxi; so it must stop. "
               "Induction is reasoning in which a conclusion about many cases is drawn from some cases, so it is only probable. Example: the first five oranges I bought here were sour, so all oranges from this seller are probably sour. "
               "Deduction gives the stronger conclusion because it is certain when the premises are true."),
            PQ("Name the method and say whether the conclusion is certain or probable: \"Two football teams have the same trainer, the same number of good players and the same ground. Team A won the cup. So Team B will probably win the cup too.\"",
               "The method is analogy: the teams are alike in several ways and we conclude they are alike in one more way. The conclusion is only probable, as the word probably shows."),
            PQ("A student reads that the sun rose every day in recorded history and says it will rise tomorrow. Which method is this, and can he be completely certain?",
               "It is induction: many past cases lead to a conclusion about a future case. His conclusion is extremely probable but, by the nature of induction, not logically certain."),
            SUM("Reasoning passes from known premises to a new conclusion.",
                "Deduction: if the premises are true and the reasoning is correct, the conclusion is certain.",
                "Induction: from some cases to more cases or to all cases; the conclusion is only probable.",
                "Analogy: from likeness in some respects to likeness in one more; the conclusion is only probable.",
                "The more cases, the more varied they are, and the more important the likenesses, the stronger an induction or analogy."),
        ],
    ),
    # ------------------------------------------------------------------ Definition and types of inference
    lesson(
        module=MODULE,
        topic="Definition and types of inference",
        title="What inference is: immediate, mediate, deductive and inductive",
        slug="inf-what-is-inference-and-its-types",
        minutes=20,
        summary="An inference is the passage from known propositions to a new one. It is immediate if it uses one premise and mediate if it uses two or more, and it is deductive or inductive by strength.",
        objectives=[
            "Define inference and name its parts: premises and conclusion",
            "Distinguish immediate inference from mediate inference",
            "Distinguish deductive inference from inductive inference",
            "Classify a short example of inference by both pairs of types",
        ],
        key_concepts=["Inference", "Immediate inference", "Mediate inference", "Deductive inference", "Inductive inference", "Proposition"],
        blocks=[
            H("Introduction"),
            T("A school secretary in Bafoussam reads the rule: \"All students who pay the PTA levy receive a receipt.\" "
              "Without asking anyone, she concludes: \"So some students who receive a receipt have paid the PTA levy.\" "
              "She did not see any new fact. She simply drew a new statement out of what she already knew."),
            T("That act is called **inference**. This lesson defines it and sorts it into types so that you can name any inference you meet."),
            D("**Inference** is the mental act of passing from one or more propositions already accepted (the **premises**, also called the antecedent) "
              "to a new proposition (the **conclusion**, also called the consequent) that is claimed to follow from them.",
              title="Definition: inference",
              note="A **proposition** is a statement that is true or false, such as \"All students who pay the levy receive a receipt.\""),
            T("Inference is the act of the mind. When we put it into words, we call it an **argument**. In this module we use both words, and you will study the structure of arguments in the next module."),
            H("First division: immediate and mediate inference"),
            D("An **immediate inference** draws the conclusion from **one** premise, with no middle step between them.",
              title="Definition: immediate inference",
              note="Examples: opposition, conversion, obversion and contraposition, which you study in the coming lessons."),
            D("A **mediate inference** draws the conclusion from **two or more** premises. The premises are linked through a middle idea. "
              "The categorical syllogism is the main example.",
              title="Definition: mediate inference"),
            CODE("Immediate (one premise):\n"
                 "  Premise: No snakes are birds.\n"
                 "  Conclusion: No birds are snakes.\n"
                 "\n"
                 "Mediate (two premises):\n"
                 "  Premise 1: All cocoa farmers in this village sell at the cooperative.\n"
                 "  Premise 2: Fon is a cocoa farmer in this village.\n"
                 "  Conclusion: Fon sells at the cooperative.", "text", title="Immediate and mediate"),
            T("The word mediate comes from the Latin for \"middle\". In the second example the idea \"cocoa farmer in this village\" is the middle that connects Fon to the cooperative."),
            H("Second division: deductive and inductive inference"),
            D("A **deductive inference** is one in which the conclusion follows with certainty from the premises: if the premises are true and the form is correct, the conclusion cannot be false.",
              title="Definition: deductive inference"),
            D("An **inductive inference** is one in which the conclusion is made only probable by the premises. It says more than the premises say, so it may be false even when all the premises are true.",
              title="Definition: inductive inference"),
            KEY("Two divisions, four boxes", "The two divisions are separate. Any inference can be classified under both.", cards=[
                ["By number of premises", "Immediate: one premise. Mediate: two or more premises."],
                ["By strength of conclusion", "Deductive: certain if premises are true and form correct. Inductive: only probable."],
                ["Immediate and deductive", "No pigs fly. So nothing that flies is a pig. (one premise, certain)"],
                ["Mediate and deductive", "All taxis are insured. This is a taxi. So this is insured. (two premises, certain)"],
            ]),
            T("Some textbooks apply the immediate and mediate division only to deductive inference and treat induction on its own. Follow your teacher's textbook on this point."),
            T("Most of the inferences you meet in this course are deductive. Many conclusions in science, farming and everyday life are inductive."),
            EX("Worked example 1: classify an inference", intro=(
                "Classify by both divisions: \"Some nurses at the hospital are mothers. Therefore some mothers are nurses at the hospital.\""), steps=[
                S("Count the premises", text="There is one premise, so the inference is **immediate**."),
                S("Test the strength", text="If some nurses are mothers, then at least one person is both a nurse and a mother. So some mothers are nurses. The conclusion is certain."),
                S("Name it", text="It is an **immediate deductive** inference (conversion of an I proposition)."),
            ]),
            EX("Worked example 2: classify an inference", intro=(
                "Classify: \"Every Cameroonian who votes must be registered. Tanyi votes. So Tanyi is registered.\""), steps=[
                S("Count the premises", text="There are two premises, so the inference is **mediate**."),
                S("Test the strength", text="If both premises are true, Tanyi is certainly registered."),
                S("Name it", text="It is a **mediate deductive** inference (a syllogism)."),
            ]),
            EX("Worked example 3: classify an inference", intro=(
                "Classify: \"Five boys from Class A scored high marks after using the study group. So all pupils will score higher after using the study group.\""), steps=[
                S("Look at the premise", text="It reports one set of cases: five boys. The conclusion talks about all pupils."),
                S("Test the strength", text="Five boys cannot prove what will happen to all pupils. The conclusion goes far beyond the premise, so it is only probable."),
                S("Name it", text="It is an **inductive** inference. It is weak, because the sample is small."),
            ]),
            H("Common mistakes and the exam"),
            MISTAKE("Thinking immediate means quick",
                    "Immediate does not describe time. It means no middle step: the conclusion comes from one premise alone."),
            MISTAKE("Thinking all deductive inferences are valid",
                    "A deductive inference **claims** that its conclusion follows with certainty. A badly built one fails. Deductive describes the kind of claim made."),
            MISTAKE("Treating \"mediate\" as a synonym for \"inductive\"",
                    "The two divisions are different. A mediate inference can be deductive (a syllogism) or inductive. Count premises for the first division and judge strength for the second."),
            TIP("Paper 1 often gives a short argument and asks you to classify it, or asks which type uses one premise. "
                "Paper 2 Section A may ask you to define inference and describe its types with an example of each.",
                title="Exam link"),
            QUIZ("Which inference is immediate?",
                 ["All fishermen in Limbe sell at the beach; Ekema is one; so Ekema sells at the beach.",
                  "No taxi is a bus; so no bus is a taxi.",
                  "Three goats were sick; so all goats here are sick.",
                  "All birds fly; penguins are birds; so penguins fly."], 1,
                 "Only option B has one premise. The others have two or more.",
                 hint="Count the premises.",
                 feedback=["It has two premises, so it is mediate.", "",
                           "It is a generalisation from cases (induction). It is not the one-premise form that the question asks for: its premise is a report of several cases.",
                           "It has two premises, so it is mediate."]),
            QUIZ("A conclusion that is only made probable by its premises comes from an inference that is",
                 ["deductive", "inductive", "immediate", "contradictory"], 1,
                 "Inductive inferences give probable conclusions.",
                 hint="Which type goes beyond the premises?",
                 feedback=["Deductive conclusions follow with certainty.", "",
                           "Immediate only tells us the number of premises.",
                           "Contradictory is a relation between propositions, not a type of inference."]),
            PQ("Define inference and distinguish immediate from mediate inference with one example of each.",
               "Inference is passing from known propositions (premises) to a new proposition (conclusion) that is claimed to follow. "
               "An immediate inference uses one premise: No fish are birds, so no birds are fish. "
               "A mediate inference uses two or more premises joined by a middle idea: All teachers are graduates, Njoya is a teacher, so Njoya is a graduate."),
            PQ("Explain the difference between deductive and inductive inference.",
               "In a deductive inference the conclusion follows with certainty if the premises are true and the form is correct. "
               "In an inductive inference the premises only make the conclusion probable, because it says more than they say."),
            PQ("Classify by both divisions: \"All bakers get up early. Ayuk is a baker. So Ayuk gets up early.\"",
               "Two premises, so mediate. The conclusion is certain if the premises are true, so deductive. It is a mediate deductive inference."),
            SUM("Inference is passing from premises already known to a new conclusion.",
                "Immediate inference: one premise. Mediate inference: two or more premises with a middle idea.",
                "Deductive inference: the conclusion is certain if the premises are true and the form is correct.",
                "Inductive inference: the conclusion is only probable.",
                "The two divisions are independent: one inference can be immediate and deductive, or mediate and deductive, or inductive."),
        ],
    ),
    # ------------------------------------------------------------------ Contradictory and contrary
    lesson(
        module=MODULE,
        topic="Forms of opposition",
        title="Contradictory and contrary opposition",
        slug="inf-contradictory-and-contrary-opposition",
        minutes=22,
        summary="Contradictories (A and O, E and I) cannot be both true or both false. Contraries (A and E) cannot be both true but can be both false. Each relation lets us infer truth values.",
        objectives=[
            "State what opposition between propositions means",
            "Identify contradictory and contrary pairs among A, E, I and O with the same subject and predicate",
            "Say, for each relation, what can be inferred when one proposition is true or false",
            "Write the correct contradictory of a universal proposition",
        ],
        key_concepts=["Opposition", "A, E, I, O", "Contradictory", "Contrary", "True, false and doubtful", "Quantity and quality"],
        blocks=[
            H("Introduction"),
            T("After the Form 5 mock exam, the principal says in the assembly: \"All the students passed.\" "
              "A parent who has seen the results replies: \"That is not true.\" "
              "What exactly is the parent claiming? That no student passed? Or only that at least one student failed? "
              "Logic has an exact answer, and it depends on how two propositions are opposed to each other."),
            T("In this lesson and the next one you study the four relations of **opposition**. "
              "Here you study the first two: contradictory and contrary."),
            H("The four propositions and the idea of opposition"),
            T("You met the four categorical propositions in Module Four. Here they are again, with S for the subject term and P for the predicate term."),
            CODE("A  All S is P         universal affirmative    All the students passed.\n"
                 "E  No S is P          universal negative       No student passed.\n"
                 "I  Some S is P        particular affirmative   Some students passed.\n"
                 "O  Some S is not P    particular negative      Some students did not pass.", "text", title="The four forms"),
            D("**Quantity** says how much of the subject is covered: universal (all or none) or particular (some). "
              "**Quality** says whether we affirm or deny: affirmative or negative.",
              title="Definition: quantity and quality"),
            D("**Opposition** is the relation between two propositions that have the **same subject and the same predicate** but differ in quantity, in quality, or in both.",
              title="Definition: opposition",
              note="Opposition only compares propositions with the same S and the same P. \"All students passed\" and \"No teacher passed\" are not opposed."),
            KEY("Which view is used?", "This lesson and the next ones use the TRADITIONAL (Aristotelian) view of the square of opposition. "
                "In this view a universal proposition such as \"All S is P\" is taken to speak about things that exist (S has members). "
                "The modern Boolean view does not assume this and gives a smaller set of relations. "
                "Textbooks differ, so follow your teacher's textbook if it differs. The difference is explained in the lesson on the square of opposition."),
            H("Contradictory opposition"),
            D("**Contradictories** are two propositions that differ in **both quantity and quality**. They are A and O, and E and I. "
              "They cannot both be true and they cannot both be false: one is true and the other false.",
              title="Definition: contradictory opposition"),
            CODE("A  All S is P        and  O  Some S is not P\n"
                 "E  No S is P         and  I  Some S is P", "text", title="The two contradictory pairs"),
            T("From the truth of one we infer the falsity of the other, and from the falsity of one we infer the truth of the other. "
              "So with contradictories there is never a doubtful case."),
            T("Back to the assembly. The principal said A: \"All the students passed.\" The parent said it is false. By contradiction, the parent is claiming O: \"Some students did not pass.\" "
              "The parent is not claiming E (\"No student passed\"). One failure is enough to make A false."),
            H("Contrary opposition"),
            D("**Contraries** are two **universal** propositions that differ in quality only. They are A and E. "
              "They cannot both be true, but they can both be false.",
              title="Definition: contrary opposition"),
            T("\"All the students passed\" and \"No student passed\" cannot both be true. "
              "But both can be false: if half the class passed and half failed, then neither statement is correct."),
            KEY("What each relation lets you infer", "Read each line as: given that the first is true or false, what is the other?", cards=[
                ["Contradictories (A-O, E-I)", "First true: other false. First false: other true. Always decided."],
                ["Contraries (A-E)", "First true: other false. First false: other doubtful (it may be true or false)."],
            ]),
            T("**Doubtful** means that the truth value of the second proposition cannot be settled from the first alone: you would have to look at the facts."),
            EX("Worked example 1: using contradictories", intro=(
                "It is true that \"Some pupils in the class did not do their homework\" (O). What do we infer about \"All pupils in the class did their homework\" (A)?"), steps=[
                S("Find the relation", text="A and O have the same subject and predicate and differ in quantity and quality. They are contradictories."),
                S("Apply the rule", text="Contradictories cannot both be true. O is true, so A is false."),
                S("State the answer", text="\"All pupils did their homework\" is false."),
            ]),
            EX("Worked example 2: using contraries", intro=(
                "It is false that \"All the goats in the pen are healthy\" (A). What do we infer about \"No goat in the pen is healthy\" (E)?"), steps=[
                S("Find the relation", text="A and E are both universal and differ in quality. They are contraries."),
                S("Apply the rule", text="Contraries cannot both be true, but they can both be false. Knowing that A is false does not tell us whether E is true or false."),
                S("State the answer", text="E is **doubtful**. If one goat is sick and the others healthy, E is false. If every goat is sick, E is true."),
            ]),
            EX("Worked example 3: the contradictory of a universal", intro=(
                "A shopkeeper says: \"All my tomatoes are fresh.\" Write the proposition that you must show to prove him wrong."), steps=[
                S("Name his proposition", text="\"All my tomatoes are fresh\" is A."),
                S("Find its contradictory", text="The contradictory of A is O."),
                S("Write it out", text="\"Some of my tomatoes are not fresh.\" One rotten tomato is enough."),
            ]),
            H("Common mistakes and the exam"),
            MISTAKE("Using the contrary as the contradictory",
                    "To deny \"All S is P\" you do not say \"No S is P\". You say \"Some S is not P\". \"No S is P\" is too strong: it is the contrary, not the contradictory."),
            MISTAKE("Thinking contraries cannot both be false",
                    "Contraries cannot both be true. They can both be false when the truth lies in between. That is why a false A leaves E doubtful."),
            MISTAKE("Mixing the names",
                    "Contradictories differ in quantity and quality (A-O, E-I). Contraries are both universal (A-E). Remember: contrary = two universals, contradictory = across the diagonal."),
            TIP("Paper 1 asks for the contradictory of a given proposition, or what follows when a given proposition is true or false. "
                "Paper 2 Section A may ask you to define contradictory and contrary opposition and to give the inference rule for each.",
                title="Exam link"),
            QUIZ("\"All the candidates in the hall are Form 5 students\" is false. What follows about \"Some candidates in the hall are not Form 5 students\"?",
                 ["It is false.", "It is true.", "It is doubtful.", "It is contrary to the first."], 1,
                 "The two propositions are A and O. They are contradictories, so if A is false, O is true.",
                 hint="Which relation links A and O?",
                 feedback=["Only if they were true together, which contradictories never are.", "",
                           "Doubtful is for contraries. Contradictories are always decided.",
                           "Contrary is the relation between A and E, not A and O."]),
            QUIZ("\"No market woman in this row sells salt\" is true. What follows about \"All market women in this row sell salt\"?",
                 ["It is true.", "It is doubtful.", "It is false.", "It is subaltern to the first."], 2,
                 "They are contraries (E and A). Contraries cannot both be true, so A is false.",
                 hint="Both are universal and differ only in quality.",
                 feedback=["Both cannot be true.", "That would be so if E were false, not true.", "",
                           "Subaltern applies between universal and particular propositions."]),
            PQ("Write the contradictory of each: (a) All footballers in the team are fit. (b) No taxi in the queue is full. (c) Some houses in the village have electricity.",
               "(a) Some footballers in the team are not fit (A and O). (b) Some taxis in the queue are full (E and I). (c) No house in the village has electricity (I and E)."),
            PQ("Explain the difference between contradictory and contrary opposition. Give one pair of each, using the proposition \"All S is P\" as the starting point.",
               "Contradictories differ in quantity and quality and can be neither both true nor both false: All S is P and Some S is not P. "
               "Contraries are two universals differing in quality: they cannot both be true but can both be false: All S is P and No S is P."),
            PQ("\"No student in the class is late\" is false. What can you infer about (a) \"Some student in the class is late\" and (b) \"All students in the class are late\"?",
               "(a) I is the contradictory of E, so I is true. (b) A is the contrary of E. A false E leaves A doubtful: it may be true or false."),
            SUM("Opposition compares propositions with the same subject and predicate that differ in quantity, quality or both.",
                "Contradictories (A-O, E-I) differ in quantity and quality: one is true and the other false, always.",
                "Contraries (A-E) are two universals: not both true, but both can be false.",
                "A false A leaves E doubtful; a false E leaves A doubtful.",
                "The contradictory of \"All S is P\" is \"Some S is not P\", never \"No S is P\".",
                "This lesson uses the traditional view; the Boolean view is explained later."),
        ],
    ),
    # ------------------------------------------------------------------ Subcontrary and subalternate
    lesson(
        module=MODULE,
        topic="Forms of opposition",
        title="Subcontrary and subalternate opposition",
        slug="inf-subcontrary-and-subalternate-opposition",
        minutes=22,
        summary="Subcontraries (I and O) cannot be both false but can be both true. Subalterns (A to I, E to O) differ in quantity: truth passes down from universal to particular, and falsity passes up.",
        objectives=[
            "Identify subcontrary and subalternate pairs among A, E, I and O",
            "State what can be inferred for each relation when a proposition is true or false",
            "Explain that \"some\" in logic means at least one and does not exclude all",
            "Work out the truth values of related propositions from one given proposition",
        ],
        key_concepts=["Subcontrary", "Subalternate", "Superaltern", "Subaltern", "Particular proposition", "Existential import"],
        blocks=[
            H("Introduction"),
            T("A football coach says: \"Some of my players are injured.\" A journalist then says: \"Some of your players are not injured.\" "
              "Are they contradicting each other? Not necessarily. Both can be true: a team can have some players injured and some fit. "
              "These two statements have a special logical relation, and it is the third of four relations of opposition."),
            T("In the last lesson you learned contradictory and contrary opposition. Here you learn the other two: **subcontrary** and **subalternate**. "
              "We keep the **traditional view**, in which universal propositions are taken to speak about things that exist."),
            H("Subcontrary opposition"),
            D("**Subcontraries** are two **particular** propositions that differ in quality only. They are I and O. "
              "They cannot both be false, but they can both be true.",
              title="Definition: subcontrary opposition"),
            T("\"Some students passed\" (I) and \"Some students did not pass\" (O). If both were false, then no student passed and also no student failed, "
              "which is impossible when there are students. So at least one is true. Both can be true if some passed and some failed."),
            KEY("Inference rule for subcontraries", "Read as: given that one is true or false, what is the other?", cards=[
                ["I true", "O is doubtful: it may be true or false."],
                ["I false", "O is true."],
                ["O true", "I is doubtful: it may be true or false."],
                ["O false", "I is true."],
            ]),
            H("Subalternate opposition"),
            D("**Subalterns** are two propositions with the same quality that differ in **quantity**: A and I (both affirmative), and E and O (both negative). "
              "The universal one is the **superaltern** and the particular one is the **subaltern**.",
              title="Definition: subalternate opposition"),
            T("In the traditional view, if the universal proposition is true then the particular one under it is true. "
              "\"All the girls in the choir sing in tune\" being true makes \"Some girls in the choir sing in tune\" true. "
              "If the particular is false, then the universal above it is false: \"Some girls sing in tune\" false means \"All girls sing in tune\" is false."),
            KEY("Inference rules for subalterns", "Truth goes down and falsity goes up.", cards=[
                ["Superaltern true", "Subaltern true. (A true gives I true. E true gives O true.)"],
                ["Superaltern false", "Subaltern doubtful. (A false does not settle I.)"],
                ["Subaltern true", "Superaltern doubtful. (I true does not settle A.)"],
                ["Subaltern false", "Superaltern false. (I false gives A false. O false gives E false.)"],
            ]),
            T("Think of a house with a roof. If the whole roof is sound, some of it is sound. If no part is sound, the whole is not sound. "
              "But from \"some is sound\" you cannot know whether all is sound."),
            D("In logic, **some** means \"at least one, and possibly all\". It does not mean \"some but not all\". "
              "That is why \"Some S is P\" does not deny \"All S is P\".",
              title="Definition: the logical meaning of some"),
            D("**Existential import** is the claim that the subject term has members. The traditional view gives universal propositions existential import: "
              "\"All S is P\" is taken to say that S exists. Subalternation depends on this. "
              "The modern Boolean view gives universal propositions no existential import, so A does not imply I there.",
              title="Definition: existential import",
              note="Boolean view: \"All unicorns have horns\" does not claim that unicorns exist. Textbooks differ, so follow your teacher's textbook."),
            EX("Worked example 1: subcontraries", intro=(
                "It is false that \"Some bananas in the basket are ripe\" (I). What follows for \"Some bananas in the basket are not ripe\" (O)?"), steps=[
                S("Find the relation", text="I and O are both particular and differ in quality: subcontraries."),
                S("Apply the rule", text="Subcontraries cannot both be false. I is false, so O is true."),
                S("Check", text="If no banana is ripe, then every banana is unripe, so some are unripe. O is true."),
            ]),
            EX("Worked example 2: subalterns going down", intro=(
                "It is true that \"No student in the hall is carrying a phone\" (E). What follows for \"Some students in the hall are not carrying a phone\" (O)?"), steps=[
                S("Find the relation", text="E and O have the same quality (negative) and differ in quantity: subalterns. E is the superaltern."),
                S("Apply the rule", text="Truth passes down. E true gives O true."),
                S("Answer", text="O is true (traditional view, where the students exist)."),
            ]),
            EX("Worked example 3: subalterns going up", intro=(
                "It is false that \"Some cars on this road are fast.\" What follows for \"All cars on this road are fast\"?"), steps=[
                S("Find the relation", text="\"Some cars are fast\" is I. \"All cars are fast\" is A. They are subalterns, with A above I."),
                S("Apply the rule", text="Falsity passes up. I false gives A false."),
                S("Reason it through", text="If not even one car is fast, then certainly not all cars are fast."),
            ]),
            H("Common mistakes and the exam"),
            MISTAKE("Reading \"some\" as \"not all\"",
                    "In logic \"Some S is P\" only means at least one. It is still true if all S are P. In the traditional view, A true makes I true."),
            MISTAKE("Going up from truth",
                    "Truth goes down, not up. From \"some are\" you cannot conclude \"all are\". The upward step works only for falsity."),
            MISTAKE("Saying subcontraries cannot both be true",
                    "That belongs to contraries. Subcontraries cannot both be false. They can both be true."),
            TIP("Paper 1 asks you to name the relation between two propositions or to give the truth value of a related proposition. "
                "Paper 2 Section A may ask you to define all four relations and to state what each permits you to infer.",
                title="Exam link"),
            QUIZ("\"Some traders at the market are honest\" is true. What follows about \"Some traders at the market are not honest\"?",
                 ["It is true.", "It is false.", "It is doubtful.", "It is contradictory to the first."], 2,
                 "They are subcontraries. When I is true, O is doubtful: both may be true.",
                 hint="Subcontraries cannot both be false. What does that say about a true one?",
                 feedback=["Not necessarily: if all traders are honest, O is false.",
                           "Both can be true together, so O is not forced to be false.", "",
                           "Contradictories are different: A and O, E and I."]),
            QUIZ("\"All the schools in the division have libraries\" is true. In the traditional view, what follows for \"Some schools in the division have libraries\"?",
                 ["It is false.", "It is doubtful.", "It is true.", "It is a contrary of the first."], 2,
                 "They are subalterns. Truth passes down from the universal to the particular.",
                 hint="A is the superaltern of I.",
                 feedback=["Contradictories would give false, but I is not the contradictory of A.",
                           "It would be doubtful only if the universal were false.", "",
                           "Contraries are two universal propositions."]),
            PQ("Name the relation between each pair: (a) All S is P and Some S is P. (b) Some S is P and Some S is not P. (c) No S is P and Some S is not P.",
               "(a) Subalterns (A is the superaltern, I the subaltern). (b) Subcontraries (I and O). (c) Subalterns (E is the superaltern, O the subaltern)."),
            PQ("\"No player in the team is injured\" is true. In the traditional view, give the truth value of the other three propositions A, I and O on the same subject and predicate.",
               "A (All players are injured) is false, because A and E are contraries. I (Some players are injured) is false, because I is the contradictory of E. "
               "O (Some players are not injured) is true, because E is its superaltern and truth passes down."),
            PQ("Explain what \"some\" means in logic and why a statement such as \"Some of the students passed\" does not mean that some failed.",
               "In logic \"some\" means at least one and possibly all. \"Some students passed\" is true if all passed. It says nothing about the others, so it does not assert that any failed."),
            SUM("Subcontraries (I and O) are two particulars that differ in quality: not both false, but possibly both true.",
                "Subalterns have the same quality and differ in quantity: A and I, and E and O.",
                "Truth goes down: A true gives I true; E true gives O true. Falsity goes up: I false gives A false; O false gives E false.",
                "Universal false does not settle the particular, and particular true does not settle the universal.",
                "\"Some\" means at least one and possibly all.",
                "Subalternation needs existential import (the traditional view). The Boolean view does not allow it."),
        ],
    ),
    # ------------------------------------------------------------------ Square of opposition
    lesson(
        module=MODULE,
        topic="Squares and truth table for opposition",
        title="The square of opposition",
        slug="inf-the-square-of-opposition",
        minutes=20,
        summary="The square of opposition shows the four relations between A, E, I and O: contradictories on the diagonals, contraries on top, subcontraries at the bottom and subalterns on the sides (traditional view).",
        objectives=[
            "Draw and label the square of opposition",
            "Name the relation shown by each side and diagonal of the square",
            "Use the square to say what follows from one proposition being true or false",
            "Explain how the Boolean view differs from the traditional square",
        ],
        key_concepts=["Square of opposition", "Contradictories", "Contraries", "Subcontraries", "Subalterns", "Existential import", "Boolean view"],
        blocks=[
            H("Introduction"),
            T("A road map helps you remember towns and the roads between them. "
              "The **square of opposition** is a map of the four propositions A, E, I and O and the roads of logic between them. "
              "Each road is one of the four relations you have just studied."),
            T("Aristotle's logic gave rise to this diagram. It was drawn in this form by later logicians, and it is used in most textbooks. "
              "This lesson uses the **traditional (Aristotelian) view**, with existential import: universal propositions are taken to speak about things that exist."),
            H("Reading the square"),
            IMG("f5l-inf-square-of-opposition.svg",
                alt="A square with A (All S is P) top left, E (No S is P) top right, I (Some S is P) bottom left and O (Some S is not P) bottom right. The top side is labelled contraries, the bottom side subcontraries, the two vertical sides subalterns and the two diagonals contradictories.",
                caption="Figure 1. The traditional square of opposition."),
            D("The **square of opposition** is a diagram that places A and E on the top, I and O on the bottom, "
              "and shows the relation between each pair of the four propositions that have the same subject and predicate.",
              title="Definition: square of opposition"),
            KEY("Six lines, four relations", "Learn which line is which.", cards=[
                ["Top side: A - E", "Contraries. Not both true; both can be false."],
                ["Bottom side: I - O", "Subcontraries. Not both false; both can be true."],
                ["Left and right sides: A - I and E - O", "Subalterns. Truth goes down, falsity goes up."],
                ["The two diagonals: A - O and E - I", "Contradictories. Always one true and one false."],
            ]),
            T("A trick to remember: the diagonals are the strong ones. They give a definite answer in both directions. "
              "The top and the bottom each allow only one definite step. The sides allow one definite step in each direction (down for truth, up for falsity)."),
            H("Using the square"),
            EX("Worked example 1: one proposition true", intro=(
                "\"All the buses at the station are full\" (A) is true. What does the square tell us about E, I and O?"), steps=[
                S("Top side: A and E are contraries", text="A is true, so E is false."),
                S("Left side: A and I are subalterns", text="Truth goes down, so I is true."),
                S("Diagonal: A and O are contradictories", text="A is true, so O is false."),
                S("Result", text="E false, I true, O false."),
            ]),
            EX("Worked example 2: one proposition false", intro=(
                "\"Some of the eggs in the tray are broken\" (I) is false. What follows for A, E and O?"), steps=[
                S("Diagonal: E and I are contradictories", text="I is false, so E is true."),
                S("Left side: A and I are subalterns", text="Falsity goes up, so A is false."),
                S("Bottom side: I and O are subcontraries", text="They cannot both be false. I is false, so O is true."),
                S("Check", text="E is true: no egg is broken. Then some eggs are not broken, so O is true. This agrees with the answer."),
            ]),
            EX("Worked example 3: where the square gives no answer", intro=(
                "\"All the players in the team are tall\" (A) is false. What follows for E and I?"), steps=[
                S("Diagonal: A and O are contradictories", text="A is false, so O is true."),
                S("Top side: A and E are contraries", text="A false leaves E doubtful."),
                S("Left side: A and I are subalterns", text="A false leaves I doubtful."),
                S("Answer", text="O is true; E and I are doubtful. They depend on the facts about the team."),
            ]),
            H("The Boolean view of the square"),
            T("**Note: this section describes the modern view. The traditional square above and the Boolean view give different results, and you must not mix them.**"),
            D("In the **Boolean view** (after the logician George Boole), a universal proposition makes **no claim that its subject has members**. "
              "\"All S is P\" only says that there is nothing in S outside P. "
              "\"No S is P\" only says that there is nothing in both S and P. "
              "The particular propositions, I and O, still claim that something exists.",
              title="Definition: the Boolean view",
              note="In Venn-diagram terms: A shades the part of S outside P; E shades the overlap of S and P; I puts an X in the overlap; O puts an X in the part of S outside P."),
            T("Under this view, A and E can both be true when there is no S at all. "
              "For example, \"All the dragons in Cameroon breathe fire\" and \"No dragon in Cameroon breathes fire\" are both true, because there are no dragons. "
              "Also I and O can both be false for the same reason."),
            KEY("What the Boolean view keeps and loses", "Compare the two views.", cards=[
                ["Kept", "Contradictories (A-O and E-I) remain. They hold in both views."],
                ["Lost", "Contrary (A-E), subcontrary (I-O) and subalternate (A-I, E-O) relations no longer hold without the assumption that S has members."],
                ["In practice", "The traditional square is useful when we speak of things we know exist: students in a class, trees on a farm."],
            ]),
            T("Which view will your examiner use? The Board's references are traditional textbooks with modern additions, so both views occur in books. "
              "Textbooks differ, so follow your teacher's textbook. If a question does not say, state which view you are using."),
            H("Common mistakes and the exam"),
            MISTAKE("Joining the wrong corners",
                    "A is joined to E by the top line. A is joined to O by a diagonal. Check the corner letters before naming the relation."),
            MISTAKE("Using the square for propositions with different terms",
                    "The square works only for propositions with the same subject and predicate. \"All dogs bark\" and \"Some cats do not bark\" are not opposed."),
            MISTAKE("Mixing the two views",
                    "If you say \"A true gives I true\", you are using the traditional view. In the Boolean view that step is not allowed. Say which you are using."),
            TIP("Paper 1 asks you to read the square: which pair are contraries, or what follows from a given proposition. "
                "Paper 2 Section A may ask you to draw and label the square, and to state the rules. Practise drawing it from memory in under a minute.",
                title="Exam link"),
            QUIZ("In the square of opposition, which pair are subcontraries?",
                 ["A and E", "A and O", "I and O", "A and I"], 2,
                 "Subcontraries are the two particular propositions: I and O, at the bottom of the square.",
                 hint="Sub- means below.",
                 feedback=["A and E are contraries.", "A and O are contradictories (a diagonal).", "",
                           "A and I are subalterns (a side)."]),
            QUIZ("\"No pupil in the school is absent\" (E) is false. In the traditional view, what is the truth value of \"Some pupil in the school is absent\" (I)?",
                 ["False", "True", "Doubtful", "It has no relation to E"], 1,
                 "E and I are contradictories. If E is false, I is true.",
                 hint="Which line joins E and I?",
                 feedback=["That would need E to be true.", "", "Contradictories are never doubtful.",
                           "E and I are joined by a diagonal of the square."]),
            PQ("Draw the square of opposition. Label the corners A, E, I, O with an example sentence for each, and label every line.",
               "Draw a square. Put A (All S is P) top left, E (No S is P) top right, I (Some S is P) bottom left, O (Some S is not P) bottom right. "
               "Label the top line contraries, the bottom line subcontraries, the left and right sides subalterns, and the two diagonals contradictories."),
            PQ("\"Some of the mangoes are rotten\" (I) is true. State what the square tells you about A, E and O.",
               "E is false, because I and E are contradictories. A is doubtful, because A and I are subalterns and a true subaltern does not settle the universal. "
               "O is doubtful, because I and O are subcontraries and a true I leaves O open."),
            PQ("Explain why the Boolean view does not accept that \"All S is P\" implies \"Some S is P\".",
               "In the Boolean view, \"All S is P\" makes no claim that S has any members. If S is empty, \"All S is P\" is true but \"Some S is P\" is false, so the first cannot imply the second."),
            SUM("The square of opposition shows the relations between A, E, I and O with the same subject and predicate.",
                "Top: contraries. Bottom: subcontraries. Sides: subalterns. Diagonals: contradictories.",
                "Contradictories: always one true and one false. Contraries: not both true. Subcontraries: not both false.",
                "Subalterns: truth goes down and falsity goes up (traditional view).",
                "In the Boolean view universal propositions have no existential import, and only the contradictories remain.",
                "Say which view you use, and follow your teacher's textbook."),
        ],
    ),
    # ------------------------------------------------------------------ Truth table for opposition
    lesson(
        module=MODULE,
        topic="Squares and truth table for opposition",
        title="The truth table for opposition",
        slug="inf-truth-table-for-opposition",
        minutes=22,
        summary="The truth table for opposition gives, for each of A, E, I and O taken as true or false, the value (true, false or doubtful) of the other three under the traditional view.",
        objectives=[
            "Read the table of truth values for the traditional square of opposition",
            "Rebuild the table from the four relations of opposition",
            "Use the table to find the truth values of related propositions",
            "State briefly how the table changes in the Boolean view",
        ],
        key_concepts=["Truth table for opposition", "True, false and doubtful", "Traditional view", "Boolean view", "Existential import"],
        blocks=[
            H("Introduction"),
            T("A secretary receives the statement: \"No student has paid the exam fee.\" She is told that it is false. "
              "She must now decide quickly which of three other statements are true, false or unknown. "
              "A table that lists every case lets her answer without drawing the square each time."),
            T("This lesson gives that table. It is the square of opposition written in a list. "
              "We use the **traditional view**: the subject exists, so universal propositions have existential import."),
            H("How the table is built"),
            D("In the **truth table for opposition**, each row gives one of A, E, I or O as **true** (T) or **false** (F). "
              "The columns give the value of each of the other propositions: T (true), F (false) or ? (doubtful: not settled by the given proposition alone).",
              title="Definition: truth table for opposition"),
            T("To make the table you only need the four relations: contradictories give T and F in both directions; "
              "contraries (A-E) give F from T; subcontraries (I-O) give T from F; subalterns pass truth down and falsity up. "
              "Every other cell is \"?\"."),
            H("The table (traditional view)"),
            CODE("Given          A    E    I    O\n"
                 "-----------------------------------\n"
                 "A is true      -    F    T    F\n"
                 "A is false     -    ?    ?    T\n"
                 "E is true      F    -    F    T\n"
                 "E is false     ?    -    T    ?\n"
                 "I is true      ?    F    -    ?\n"
                 "I is false     F    T    -    T\n"
                 "O is true      F    ?    ?    -\n"
                 "O is false     T    F    T    -", "text", title="Table 1. Truth table for opposition (traditional view)"),
            T("How to read it: find the row of the proposition that you are given, then read across to the column of the proposition that you want. "
              "A dash means the proposition is the one that was given."),
            KEY("Patterns worth noticing", "These help you remember the table.", cards=[
                ["Universal true", "All the other three are decided. A true gives F, T, F. E true gives F, F, T."],
                ["Particular false", "All the other three are decided. I false gives F, T, T. O false gives T, F, T."],
                ["Universal false or particular true", "Only the contradictory is decided. The other two cells are doubtful (?)."],
            ]),
            T("In the third pattern the one decided proposition is always the contradictory: A false gives O true; E false gives I true; I true gives E false; O true gives A false."),
            EX("Worked example 1: a universal true", intro=(
                "\"No taxi driver at the station is drunk\" (E) is true. Find the values of A, I and O."), steps=[
                S("Find the row", text="E is true."),
                S("Read across", text="A is F, I is F, O is T."),
                S("Explain each", text="A is the contrary of E (not both true). I is the contradictory of E. O is the subaltern of E (truth passes down)."),
            ]),
            EX("Worked example 2: a particular false", intro=(
                "\"Some books in the library are on Logic\" (I) is false. Find A, E and O."), steps=[
                S("Find the row", text="I is false."),
                S("Read across", text="A is F, E is T, O is T."),
                S("Explain each", text="A is the superaltern of I (falsity goes up). E is the contradictory of I. O is the subcontrary of I (not both false)."),
            ]),
            EX("Worked example 3: a universal false", intro=(
                "\"All the sheep in the field are black\" (A) is false. What can we say about E, I and O?"), steps=[
                S("Find the row", text="A is false."),
                S("Read across", text="E is ?, I is ?, O is T."),
                S("Explain each", text="O is the contradictory of A, so it is true. E and I are not settled: all the sheep might be white (E true, I false), or some might be black (E false, I true)."),
            ]),
            H("Note: the Boolean view"),
            T("**Clearly labelled note. This section uses the modern Boolean view and not the traditional one.** "
              "Boolean logicians do not assume that the subject has members. Then only the contradictories remain, and the table becomes as follows."),
            CODE("Given          A    E    I    O\n"
                 "-----------------------------------\n"
                 "A is true      -    ?    ?    F\n"
                 "A is false     -    ?    ?    T\n"
                 "E is true      ?    -    F    ?\n"
                 "E is false     ?    -    T    ?\n"
                 "I is true      ?    F    -    ?\n"
                 "I is false     ?    T    -    ?\n"
                 "O is true      F    ?    ?    -\n"
                 "O is false     T    ?    ?    -", "text", title="Table 2. The same table in the Boolean view"),
            T("Compare the two tables. Every cell filled in Table 1 for contradictories is the same in Table 2. "
              "Every cell that came from the contrary, subcontrary or subalternate relations has become \"?\". "
              "Textbooks differ, so follow your teacher's textbook if it differs."),
            H("Common mistakes and the exam"),
            MISTAKE("Filling every cell",
                    "Do not force an answer. A universal that is false does not tell you whether the other universal is true. Write doubtful."),
            MISTAKE("Confusing the two tables",
                    "Table 1 uses subalternation (A true gives I true). In Table 2 the same cell is \"?\". Always say which view you are using."),
            MISTAKE("Reading the wrong row",
                    "\"A is false\" and \"O is false\" are different rows. Underline the proposition given and its truth value before looking at the table."),
            TIP("Paper 1 often gives one proposition with its truth value and asks for another, or asks which relation allows an inference. "
                "In Paper 2, write the relation you use at each step, for example \"I and E are contradictories, so E is false\". That shows your reasoning.",
                title="Exam link"),
            QUIZ("In the traditional view, \"All the girls in the class sing\" (A) is true. What is the value of \"Some girls in the class do not sing\" (O)?",
                 ["True", "Doubtful", "False", "It cannot be tested"], 2,
                 "A and O are contradictories. A true gives O false.",
                 hint="Use the diagonal.",
                 feedback=["That would be so if A were false.", "Contradictories are always decided.", "",
                           "The two propositions share subject and predicate, so they can be tested."]),
            QUIZ("\"Some students in the class are not tall\" (O) is true. In the traditional view, what is the value of the A proposition \"All students in the class are tall\"?",
                 ["True", "Doubtful", "False", "True, because of subalternation"], 2,
                 "A is the contradictory of O. O true gives A false.",
                 hint="A and O are on a diagonal.",
                 feedback=["Contradictories cannot both be true.", "Doubtful would be for the other propositions in that row.", "",
                           "Subalternation passes truth down from A to I, not up from O."]),
            PQ("Complete the row: \"I is true\". Give the values of A, E and O (traditional view) and the relation used for each.",
               "A is ? (subalterns: a true particular does not settle the universal). E is F (contradictory of I). O is ? (subcontraries: both may be true)."),
            PQ("\"No player scored\" (E) is false. Find the values of A, I and O in the traditional view.",
               "A is ? (contraries: false E leaves A open). I is T (contradictory of E). O is ? (subaltern of E, which is false, so O is open)."),
            PQ("Give one cell of Table 1 that is different in the Boolean view and explain why.",
               "If A is true, Table 1 gives I as T. In the Boolean view it is ?, because A does not claim that S has members. For example, if there are no dragons, \"All dragons breathe fire\" is true but \"Some dragons breathe fire\" is false."),
            SUM("The truth table for opposition lists, for each of A, E, I and O taken as true or false, the values of the other three.",
                "Use T, F and ? (doubtful).",
                "Traditional view: contradictories decide both ways, contraries decide only from true to false, subcontraries only from false to true, subalterns pass truth down and falsity up.",
                "Boolean view: only the contradictory cells remain decided.",
                "Always say which view you are using and follow your teacher's textbook."),
        ],
    ),
    # ------------------------------------------------------------------ Conversion and obversion
    lesson(
        module=MODULE,
        topic="Forms of eduction",
        title="Eduction: conversion and obversion",
        slug="inf-conversion-and-obversion",
        minutes=24,
        summary="Eduction draws a new proposition from one proposition by changing its form. Conversion swaps subject and predicate (valid simply for E and I). Obversion changes quality and complements the predicate (valid for all four).",
        objectives=[
            "Define eduction and name its three forms: conversion, obversion and contraposition",
            "Convert E and I simply, convert A by limitation and explain why O cannot be converted",
            "Obvert A, E, I and O correctly using the complement of the predicate",
            "Check a conversion with the rule about distribution of terms",
        ],
        key_concepts=["Eduction", "Conversion", "Convertend and converse", "Obversion", "Complementary term", "Distribution of terms", "Conversion by limitation"],
        blocks=[
            H("Introduction"),
            T("A shopkeeper in Douala puts a notice on her door: \"All my customers are people who pay in cash.\" "
              "A student reads it and says: \"So all people who pay in cash are your customers.\" The shopkeeper replies: \"No! A visitor can pay cash without being my customer.\" "
              "The student made a mistake in changing the form of a statement. Logic has exact rules for what may and may not be said."),
            D("**Eduction** is an immediate inference in which, from one given proposition, we draw another proposition by changing its form while keeping its meaning as far as the rules allow. "
              "The three forms taught in this course are **conversion**, **obversion** and **contraposition**.",
              title="Definition: eduction",
              note="Some books also list a fourth form, inversion. Your syllabus names only the forms of eduction, so check your textbook for which ones it expects."),
            T("In this lesson we study conversion and obversion. Contraposition and the limits of eduction come in the next lesson. "
              "We use the **traditional view**, in which universal propositions have existential import (the terms refer to things that exist). "
              "Where the modern Boolean view gives a different answer, we say so."),
            H("Reminder: distribution of terms"),
            D("A term is **distributed** in a proposition when the proposition says something about **every** member of the thing that the term names. "
              "A distributes its subject. E distributes both terms. I distributes neither. O distributes its predicate.",
              title="Definition: distribution of terms"),
            CODE("A  All S is P         S distributed\n"
                 "E  No S is P          S and P distributed\n"
                 "I  Some S is P        none distributed\n"
                 "O  Some S is not P    P distributed", "text", title="Distribution table"),
            H("Conversion"),
            D("**Conversion** is the eduction in which the subject and predicate **change places**, and the quality (affirmative or negative) is **not changed**. "
              "The given proposition is the **convertend** and the new one is the **converse**.",
              title="Definition: conversion"),
            D("**Rule of conversion:** no term may be distributed in the converse unless it was distributed in the convertend.",
              title="Rule of conversion"),
            KEY("Which forms can be converted?", "Apply the rule to each form.", cards=[
                ["E: simple conversion", "No S is P gives No P is S. Both terms are distributed in both, so the rule is kept. Valid."],
                ["I: simple conversion", "Some S is P gives Some P is S. No term is distributed in either. Valid."],
                ["A: by limitation", "All S is P gives Some P is S. Simple conversion (All P is S) would distribute P, which A did not. We reduce to I (conversion by limitation, also called per accidens)."],
                ["O: cannot be converted", "Some S is not P cannot give Some P is not S. P was distributed in O, but S is not distributed in O, so the converse would distribute S wrongly."],
            ]),
            T("Conversion by limitation changes the quantity: from universal A to particular I. It needs the traditional assumption that S exists. "
              "In the Boolean view, A does not give I, so conversion of A is not allowed at all. Textbooks differ, so follow your teacher's textbook."),
            T("Some textbooks also convert E by limitation (No S is P gives Some P is not S). This too needs existential import."),
            EX("Worked example 1: converting E and I", intro=(
                "Convert (a) \"No goat in this pen is a ram.\" (b) \"Some farmers in the village are women.\""), steps=[
                S("(a) E, simple conversion", text="Swap the terms, keep the quality: \"No ram is a goat in this pen.\" Valid."),
                S("(b) I, simple conversion", text="\"Some women are farmers in the village.\" Valid."),
                S("Check with a Venn diagram", text="In both, the shaded or marked region is the overlap of the two circles. That region is the same whichever way we read it."),
            ]),
            EX("Worked example 2: converting A", intro=(
                "Convert \"All students in the choir are Form 5 students.\""), steps=[
                S("Try the simple conversion", text="\"All Form 5 students are students in the choir.\" This is false: other Form 5 students may not be in the choir."),
                S("Use the rule", text="The convertend distributes only the subject. The simple converse would distribute its subject (Form 5 students), which was not distributed before. So it is invalid."),
                S("Convert by limitation", text="\"Some Form 5 students are students in the choir.\" Valid in the traditional view."),
            ]),
            EX("Worked example 3: O cannot be converted", intro=(
                "Show that \"Some animals are not dogs\" cannot be converted to \"Some dogs are not animals\"."), steps=[
                S("Test with the facts", text="\"Some animals are not dogs\" is true (cats are animals but not dogs)."),
                S("Test the converse", text="\"Some dogs are not animals\" is false: every dog is an animal."),
                S("Conclusion", text="True premise and false conclusion: the eduction is invalid. The fault is called **illicit conversion**."),
            ]),
            H("Obversion"),
            D("A **complementary term** (or complement) of a term P is the term **non-P**: it names everything that is **not** P. "
              "The complement of \"honest people\" is \"non-honest people\", not \"dishonest people\" (dishonest people are only some of the non-honest).",
              title="Definition: complementary term"),
            D("**Obversion** is the eduction in which the **quality** of the proposition is **changed** and the **predicate is replaced by its complement**. "
              "The subject is not changed, and the quantity is not changed.",
              title="Definition: obversion"),
            CODE("Given (obvertend)            Obverse\n"
                 "A  All S is P         gives  E  No S is non-P\n"
                 "E  No S is P          gives  A  All S is non-P\n"
                 "I  Some S is P        gives  O  Some S is not non-P\n"
                 "O  Some S is not P    gives  I  Some S is non-P", "text", title="Obversion of the four forms"),
            T("Obversion is valid for **all four** forms, in both the traditional and the Boolean view, and the obverse always means the same as the original. "
              "In Venn terms, \"All S is P\" says there is nothing in S outside P. \"No S is non-P\" says exactly the same thing."),
            EX("Worked example 4: obverting", intro=(
                "Obvert (a) \"All the roads in this town are paved.\" (b) \"Some pupils are not punctual.\""), steps=[
                S("(a) Change the quality, complement the predicate", text="A becomes E. \"No road in this town is non-paved.\" (Non-paved means unpaved.)"),
                S("(b) Same steps", text="O becomes I. \"Some pupils are non-punctual.\""),
                S("Check", text="In each case the meaning is the same as the original."),
            ]),
            EX("Worked example 5: conversion then obversion", intro=(
                "Start from \"No tourist in the hotel is a local.\" Convert it, then obvert the converse."), steps=[
                S("Convert (E, simple)", text="\"No local is a tourist in the hotel.\""),
                S("Obvert (E becomes A, predicate complemented)", text="\"All locals are non-tourists in the hotel.\""),
                S("Meaning", text="The three statements say the same thing in different forms."),
            ]),
            H("Common mistakes and the exam"),
            MISTAKE("Converting A simply",
                    "\"All S is P\" does not give \"All P is S\". All taxis are vehicles; not all vehicles are taxis. This error is called illicit conversion."),
            MISTAKE("Converting O",
                    "\"Some S is not P\" cannot be converted at all. Stop, and write \"no valid converse\"."),
            MISTAKE("Obverting without complementing the predicate",
                    "Changing only the quality gives a wrong statement. \"All S is P\" does not give \"No S is P\". The predicate must become non-P."),
            MISTAKE("Using a wrong complement",
                    "The complement of \"tall\" is \"non-tall\", not \"short\". Short people are only some of the non-tall people."),
            TIP("Paper 1 asks for the converse or obverse of a given proposition, or which form cannot be converted. "
                "Paper 2 Section A may ask you to define the terms and to convert and obvert four propositions. Always show the form letter before and after (for example A to E).",
                title="Exam link"),
            QUIZ("Which of these has a valid simple converse?",
                 ["All dogs are animals", "Some dogs are not pets", "No cat is a dog", "All pets are dogs"], 2,
                 "E propositions convert simply: \"No dog is a cat\" follows from \"No cat is a dog\".",
                 hint="Only E and I convert simply.",
                 feedback=["A cannot be converted simply. By limitation it gives Some animals are dogs.",
                           "O cannot be converted at all.", "",
                           "A cannot be converted simply."]),
            QUIZ("What is the obverse of \"No student in the class is lazy\"?",
                 ["No lazy student is in the class.", "All students in the class are non-lazy.", "Some students in the class are lazy.", "All lazy people are students in the class."], 1,
                 "E becomes A and the predicate is complemented: All students in the class are non-lazy.",
                 hint="Change the quality and replace the predicate with its complement.",
                 feedback=["That is the converse, not the obverse.", "",
                           "That is the contradictory of the original, not the obverse.",
                           "That changes terms and quality wrongly."]),
            PQ("Convert, where valid, and say which type of conversion is used: (a) No snake is harmless. (b) Some teachers are parents. (c) All lions are cats. (d) Some books are not novels.",
               "(a) No harmless thing is a snake (simple conversion of E). (b) Some parents are teachers (simple conversion of I). (c) Some cats are lions (by limitation, A to I). (d) No valid converse: O cannot be converted."),
            PQ("Obvert: (a) All the tomatoes are ripe. (b) No fish is a mammal. (c) Some markets are crowded. (d) Some markets are not crowded.",
               "(a) No tomato is non-ripe (A to E). (b) All fish are non-mammals (E to A). (c) Some markets are not non-crowded (I to O). (d) Some markets are non-crowded (O to I)."),
            PQ("Explain, using distribution, why \"All S is P\" cannot be converted simply.",
               "In \"All S is P\" only S is distributed. The simple converse \"All P is S\" distributes P. A term distributed in the converse but not in the convertend breaks the rule of conversion, so the simple conversion is invalid."),
            SUM("Eduction is an immediate inference that changes the form of one proposition. Its forms are conversion, obversion and contraposition.",
                "Conversion swaps subject and predicate and keeps quality. E and I convert simply, A converts by limitation to I, O cannot be converted.",
                "Rule: no term distributed in the converse unless distributed in the convertend.",
                "Obversion changes quality and replaces the predicate by its complement. It is valid for A, E, I and O.",
                "The complement of P is non-P, never a different opposite word.",
                "Conversion by limitation depends on the traditional view."),
        ],
    ),
    # ------------------------------------------------------------------ Contraposition and limits
    lesson(
        module=MODULE,
        topic="Forms of eduction",
        title="Contraposition and the limits of eduction",
        slug="inf-contraposition-and-limits-of-eduction",
        minutes=24,
        summary="Contraposition replaces the subject by the complement of the predicate and the predicate by the complement of the subject. It is valid for A and O, valid by limitation for E, and invalid for I.",
        objectives=[
            "Contrapose A and O, and E by limitation, using obversion and conversion in steps",
            "Explain why I has no valid contrapositive",
            "Give, for each of A, E, I and O, which of conversion, obversion and contraposition are valid",
            "Distinguish eductions that keep the same meaning from those that only follow by limitation",
        ],
        key_concepts=["Contraposition", "Contrapositive", "Complementary term", "Conversion by limitation", "Limits of eduction", "Valid eduction"],
        blocks=[
            H("Introduction"),
            T("A driving school in Bamenda says: \"All licensed drivers are people who passed the test.\" "
              "A new learner reasons: \"So anyone who did not pass the test is not a licensed driver.\" "
              "This reasoning is correct, and it is an example of **contraposition**. "
              "Learning it, and knowing which forms it works for, helps you to avoid false conclusions."),
            D("**Contraposition** is the eduction in which the **subject is replaced by the complement of the predicate**, and the **predicate is replaced by the complement of the subject**. "
              "The new proposition is the **contrapositive**.",
              title="Definition: contraposition",
              note="From All S is P we reach All non-P is non-S."),
            T("We continue with the traditional view. Contraposition for E uses conversion by limitation, so it needs existential import. The Boolean view differs, and we say where."),
            H("How to contrapose: three steps"),
            KEY("Obvert, convert, obvert", "Contraposition is made by combining the two forms you already know.", cards=[
                ["Step 1", "Obvert the given proposition."],
                ["Step 2", "Convert the result."],
                ["Step 3", "Obvert again."],
            ]),
            CODE("A  All S is P\n"
                 "   obvert:   No S is non-P        (E)\n"
                 "   convert:  No non-P is S        (E, simple)\n"
                 "   obvert:   All non-P is non-S   (A)\n"
                 "\n"
                 "O  Some S is not P\n"
                 "   obvert:   Some S is non-P      (I)\n"
                 "   convert:  Some non-P is S      (I, simple)\n"
                 "   obvert:   Some non-P is not non-S   (O)\n"
                 "\n"
                 "E  No S is P\n"
                 "   obvert:   All S is non-P       (A)\n"
                 "   convert:  Some non-P is S      (by limitation, A to I)\n"
                 "   obvert:   Some non-P is not non-S   (O)\n"
                 "\n"
                 "I  Some S is P\n"
                 "   obvert:   Some S is not non-P  (O)\n"
                 "   convert:  not possible: O cannot be converted", "text", title="Contraposition step by step"),
            T("So A has a **full** contrapositive (A to A), O also (O to O), E has one **by limitation** (E to O), and I has **none**."),
            D("A **valid eduction** is one in which the new proposition must be true whenever the given proposition is true. "
              "An eduction that gives a new proposition with exactly the same meaning as the original (obversion, simple conversion, full contraposition) is called an **equivalence**. "
              "An eduction by limitation gives only a weaker statement: from the new one you cannot return to the original.",
              title="Definition: valid eduction"),
            H("Summary of all valid eductions"),
            CODE("Form   Conversion          Obversion             Contraposition\n"
                 "---------------------------------------------------------------------\n"
                 "A      by limitation (I)   E: No S is non-P      full: All non-P is non-S (A)\n"
                 "E      simple (E)          A: All S is non-P     by limitation: Some non-P is not non-S (O)\n"
                 "I      simple (I)          O: Some S is not non-P   not valid\n"
                 "O      not valid           I: Some S is non-P    full: Some non-P is not non-S (O)", "text", title="Table 1. Valid eductions (traditional view)"),
            T("Notice the symmetry. A and O are good for contraposition, E and I for conversion. Obversion works for all four. "
              "Remember: obversion always works; conversion fails for O; contraposition fails for I."),
            T("In the Boolean view the entries that rely on limitation (A converting to I, E converting to O, E contraposing to O) are not valid. "
              "The others (obversion, simple conversion of E and I, full contraposition of A and O) remain valid. Textbooks differ, so follow your teacher's textbook."),
            H("Limits of eduction"),
            T("Eduction has limits. It cannot add new information: the new proposition says nothing that was not already in the given one, and sometimes says less. "
              "An invalid eduction is a mistake in reasoning. The best-known mistakes are **illicit conversion** (converting A or O simply) and **illicit contraposition** (contraposing I)."),
            T("A failed eduction does not prove that the new proposition is false. It only means that the given proposition does not settle it. "
              "For example, the invalid converse of \"All dogs are animals\" is \"All animals are dogs\", which is false. "
              "But the invalid converse of \"All members of the club are students\" is \"All students are members of the club\", which could happen to be true. "
              "So an invalid eduction gives no guarantee either way."),
            T("Another limit: if the given proposition is false, an eduction by limitation does not tell you that the new one is false. "
              "For equivalent eductions it does: if the original is false, the new one is false."),
            EX("Worked example 1: contraposition of A", intro=(
                "Find the contrapositive of \"All licensed drivers are people who passed the test.\""), steps=[
                S("Obvert", text="\"No licensed driver is a person who did not pass the test.\" (E)"),
                S("Convert", text="\"No person who did not pass the test is a licensed driver.\" (E, simple)"),
                S("Obvert", text="\"All persons who did not pass the test are non-licensed-drivers.\" (A)"),
                S("In plain words", text="Anyone who did not pass the test is not a licensed driver. The meaning is the same as the original."),
            ]),
            EX("Worked example 2: contraposition of E by limitation", intro=(
                "Find the contrapositive of \"No vegetable seller in this market is a fisherman.\""), steps=[
                S("Obvert", text="\"All vegetable sellers in this market are non-fishermen.\" (A)"),
                S("Convert by limitation", text="\"Some non-fishermen are vegetable sellers in this market.\" (I)"),
                S("Obvert", text="\"Some non-fishermen are not non-vegetable-sellers in this market.\" (O)"),
                S("Note", text="The contrapositive is weaker than the original, and it needs the traditional assumption that vegetable sellers exist."),
            ]),
            EX("Worked example 3: why I has no contrapositive", intro=(
                "Try to contrapose \"Some students are Form 5 pupils.\" What goes wrong?"), steps=[
                S("Obvert", text="\"Some students are not non-Form-5-pupils.\" (O)"),
                S("Convert", text="We now need to convert an O proposition, and O cannot be converted."),
                S("Use the Venn diagram", text="\"Some students are Form 5 pupils\" puts an X in the overlap of the two circles. Any contrapositive would speak about things outside both circles, and the X says nothing about that region."),
                S("Conclusion", text="I has no valid contrapositive."),
            ]),
            H("Common mistakes and the exam"),
            MISTAKE("Contraposing I",
                    "\"Some S is P\" has no contrapositive. The steps break at the conversion of O."),
            MISTAKE("Forgetting to complement both terms",
                    "In contraposition both terms are replaced by complements and exchanged. \"All S is P\" gives \"All non-P is non-S\", not \"All P is S\" and not \"All non-S is non-P\"."),
            MISTAKE("Stopping after one step",
                    "Contraposition is three steps. If your answer still has S as the subject, you have not finished."),
            TIP("Paper 1 asks for the contrapositive of a proposition or which form has no valid contrapositive or converse. "
                "Paper 2 Section A may give four propositions and ask for the valid conversion, obversion and contraposition of each. Fill in Table 1 as a checklist.",
                title="Exam link"),
            QUIZ("Which form has no valid contrapositive?",
                 ["A", "E", "I", "O"], 2,
                 "I has none. Obverting gives O, and O cannot be converted.",
                 hint="Look at the step that fails.",
                 feedback=["A has a full contrapositive: All non-P is non-S.", "E has one by limitation.", "",
                           "O has a full contrapositive: Some non-P is not non-S."]),
            QUIZ("What is the contrapositive of \"All members of the club are students\"?",
                 ["All students are members of the club.", "All non-students are non-members of the club.", "No members of the club are non-students.", "Some students are members of the club."], 1,
                 "A to A: All non-P is non-S. P is students, S is members of the club.",
                 hint="Complement both terms and swap them.",
                 feedback=["That is the simple converse of A, which is invalid.", "",
                           "That is the obverse, not the contrapositive.",
                           "That is the converse by limitation."]),
            PQ("Complete the table. For each form give a valid conversion, obversion and contraposition, or write none: A, E, I, O.",
               "A: conversion by limitation (I), obversion E, contraposition A. E: conversion simple (E), obversion A, contraposition by limitation (O). "
               "I: conversion simple (I), obversion O, contraposition none. O: conversion none, obversion I, contraposition O."),
            PQ("Find the contrapositive of \"Some taxis are not yellow.\" Show your three steps.",
               "Obvert: Some taxis are non-yellow (I). Convert: Some non-yellow things are taxis (I). Obvert: Some non-yellow things are not non-taxis (O). So the contrapositive is Some non-yellow things are not non-taxis."),
            PQ("A student contraposes \"All S is P\" and writes \"All P is S\". Name the error and give the correct contrapositive.",
               "He converted simply (illicit conversion) and did not complement the terms. The correct contrapositive is All non-P is non-S."),
            SUM("Contraposition replaces S with non-P and P with non-S. Make it by obverting, converting, then obverting.",
                "A: full contrapositive (All non-P is non-S). O: full contrapositive. E: by limitation, to O. I: none.",
                "Obversion works for all four; conversion fails for O; contraposition fails for I.",
                "Equivalent eductions keep the meaning; eductions by limitation give a weaker statement.",
                "Eductions that rely on limitation need existential import (traditional view).",
                "An invalid eduction does not prove the new proposition false: it only fails to prove it true."),
        ],
    ),
]
