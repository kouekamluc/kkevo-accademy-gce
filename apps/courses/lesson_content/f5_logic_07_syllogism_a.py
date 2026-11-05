"""Form 5 Logic (GCE O Level 0590), module "Mediate Inference (Arguments)": structure of an argument,
validity and soundness, the value and structure of the categorical syllogism, and its figures.
Draft content: check against the official syllabus and your class textbook."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "Mediate Inference (Arguments)"
ARG = "Structure of an argument"
VAL = "Validity and soundness"
VALUE = "Value of the syllogism and structure of the categorical syllogism"
FIG = "The figures of the categorical syllogism"

LESSONS = [
    # ------------------------------------------------------------------ 1. Premises and conclusion
    lesson(
        module=MODULE,
        topic=ARG,
        title="Premises and conclusion: what an argument is",
        slug="arg-premises-and-conclusion",
        minutes=20,
        summary="An argument is a set of statements in which premises are offered as reasons for a conclusion. Learn to tell arguments from explanations and opinions, spot indicator words, find the conclusion and write an argument in standard form.",
        objectives=[
            "Define an argument, a premise and a conclusion",
            "Tell an argument from an explanation and from an opinion",
            "Use indicator words and the question “What am I asked to accept?” to find the conclusion",
            "Rewrite an everyday argument in standard form: premises first, then the conclusion",
        ],
        key_concepts=["Argument", "Premise", "Conclusion", "Indicator words", "Explanation", "Opinion", "Standard form of an argument"],
        blocks=[
            H("Introduction"),
            T("At Mokolo market a buyer says: “I will not pay 5000 FCFA for this bag. The seam is already loose, "
              "and the same bag costs 3500 FCFA at the next stall.” She does not only say “no”. She gives **reasons**. "
              "Her seller may accept the reasons or answer them."),
            T("Logic is the study of this kind of reasoning. Before we can ask whether reasoning is good or bad, "
              "we must be able to see it clearly: which statements are the reasons, and which statement do they support? "
              "That is the skill of this lesson."),
            D("An **argument** is a group of statements in which one statement, the **conclusion**, is claimed to follow from "
              "the others, the **premises**. The premises are offered as reasons to accept the conclusion.",
              title="Definition: argument",
              note="A statement is a sentence that is either true or false. Questions and commands are not statements."),
            D("A **premise** is a statement given as a reason. A **conclusion** is the statement the reasons are meant to support.",
              title="Definition: premise and conclusion",
              note="In the buyer's argument the conclusion is “I will not pay 5000 FCFA”. The two reasons are the premises."),
            IMG("f5l-arg-structure.svg",
                alt="Diagram of an argument. Two blue boxes, premise 1 'All pupils must wear uniform' and premise 2 'Ayuk is a pupil', "
                    "have arrows to a green box, the conclusion 'Ayuk must wear uniform'. Below are lists of words that point to a conclusion "
                    "and words that point to a premise.",
                caption="Figure 1. Premises point to the conclusion. Indicator words often show which is which."),
            H("Argument, explanation or opinion?"),
            T("Not every passage that contains the word “because” is an argument. We must ask what the writer is trying to do."),
            KEY("Three kinds of passage", "The same sentence pattern can do three different jobs.", cards=[
                ["Argument", "Gives reasons to make us **accept a claim** that is still in doubt. “The river will flood, because rain has fallen for three days and the banks are low.”"],
                ["Explanation", "Tells us **why something that is already accepted** happened or is so. “The river flooded because rain fell for three days.”"],
                ["Opinion", "States a view and gives **no reasons**. “I think the river is dangerous.” An opinion becomes part of an argument only when reasons are added."],
            ]),
            TIP("A quick test. Ask: “Is the writer trying to prove something I might doubt (argument), or to tell me the cause of something we both already accept (explanation)?”"),
            EX("Worked example 1: argument, explanation or opinion?", intro=(
                "Classify each passage. "
                "(a) Our school team will win on Saturday. They have won their last five matches and the other team has lost three players. "
                "(b) The match was cancelled because the pitch was flooded. "
                "(c) Pidgin is the best language for the market."), steps=[
                S("(a) Is a claim being supported?", text="“Our team will win” is about the future, so it can be doubted. Two reasons are given for it. This is an **argument**. Conclusion: the team will win."),
                S("(b) Is the cancellation in doubt?", text="The cancellation has already happened. The sentence tells us its cause. This is an **explanation**."),
                S("(c) Are any reasons given?", text="Only a view is stated. This is an **opinion**."),
            ]),
            H("Indicator words"),
            D("**Indicator words** are words that often signal a premise or a conclusion. Conclusion indicators: therefore, so, thus, hence, consequently, it follows that. "
              "Premise indicators: because, since, for, as, given that, the reason is that.",
              title="Definition: indicator words",
              note="The indicator belongs to the statement that follows it. “Since the clinic is closed” marks a premise. “So we must go home” marks the conclusion."),
            MISTAKE("Trusting indicator words blindly",
                    "Indicator words are only clues. “Since” can mean “from the time that” (“Since 2020 he has lived in Douala”) and “because” can begin an explanation. "
                    "Always ask what the passage is trying to do. Many good arguments also have no indicator word at all."),
            H("Finding the conclusion"),
            T("The conclusion is not always the last sentence. It may come first, in the middle, or at the end. "
              "To find it, ask: **“What is the writer trying to make me accept?”** The other statements will be the reasons."),
            EX("Worked example 2: an argument with no indicator words", intro=(
                "“Mr Tabe wants his cocoa to dry well. Cocoa dries badly in wet weather. "
                "The rains in Kumba last until November. He should wait until December to dry it.” Find the conclusion and the premises."), steps=[
                S("Ask what the writer wants us to accept", text="The writer wants us to accept advice: he should wait until December."),
                S("Check the other sentences", text="Each one gives a reason: what Mr Tabe wants, how cocoa behaves in wet weather, when the rains stop."),
                S("State the result", text="Conclusion: Mr Tabe should wait until December to dry his cocoa. Premises: the other three sentences."),
            ]),
            EX("Worked example 3: conclusion first, then standard form", intro=(
                "“Since every student who is absent from the exam without permission loses marks, and Nkeng was absent without permission, "
                "Nkeng will lose marks.” Write the argument in standard form."), steps=[
                S("Find the conclusion", text="“Nkeng will lose marks” is what the writer wants us to accept."),
                S("List the premises, without the indicator words", text="Premise 1: Every student who is absent from the exam without permission loses marks. Premise 2: Nkeng was absent without permission."),
                S("Write the standard form", text="Premise 1: Every student who is absent from the exam without permission loses marks. Premise 2: Nkeng was absent without permission. Therefore: Nkeng will lose marks."),
            ]),
            KEY("Standard form of an argument", "To standardise an argument:", cards=[
                ["1. Find the conclusion", "Ask what the writer wants us to accept."],
                ["2. List the premises", "Write each one as a complete statement, one per line. Remove filler words and indicator words."],
                ["3. Put the conclusion last", "Mark it with “Therefore”. The order of the premises should be natural."],
            ]),
            MISTAKE("Thinking the conclusion is always the last sentence",
                    "“The new road should be repaired this year. It is the only road to the market, and farmers lose goods every rainy season.” "
                    "The conclusion comes first here. Use the question “What must I accept?”, not the position of the sentence."),
            QUIZ("Ada has studied logic every evening for a month. She is always attentive in class. Therefore, she will do well in the exam. Which statement is the conclusion?",
                 ["Ada has studied logic every evening for a month.", "She is always attentive in class.", "Ada will do well in the exam.", "Ada is a student."],
                 2, "“Therefore” points to the conclusion: she will do well in the exam. The first two statements are reasons.",
                 hint="Look for the indicator word, then ask what the writer wants you to accept.",
                 feedback=["This is a premise: a reason offered for the conclusion.", "This is also a premise.", "", "This is not stated in the passage."]),
            QUIZ("Which passage is an explanation and not an argument?",
                 ["The bus will be late, because the road is blocked.", "The bus was late because a tree fell across the road.", "The bus is always late, so I will walk.", "I think the bus driver is careless."],
                 1, "The lateness has already happened and is accepted. The sentence tells its cause. The others support a claim (A, C) or give a view with no reasons (D).",
                 hint="Ask whether the main claim is already accepted by everyone.",
                 feedback=["This supports a prediction that can be doubted: an argument.", "", "“So I will walk” is a conclusion supported by a reason: an argument.", "A view with no reasons is an opinion."]),
            TIP("Exam link: in Paper 1 you may be asked to pick the conclusion or to decide whether a passage is an argument, an explanation or an opinion. "
                "In Paper 2 Section A you may be asked to list the premises and the conclusion of a short passage.", title="Exam link"),
            PQ("Give the conclusion and the premises: “Since the clinic closes at 4 pm and it is now 4.30 pm, we cannot be seen today.”",
               "Conclusion: We cannot be seen today. Premises: (1) The clinic closes at 4 pm. (2) It is now 4.30 pm. “Since” marks the first premise. "
               "The word “so” is not written, but the last clause is what the writer wants us to accept."),
            PQ("Is this an argument or an explanation? (a) The bus was late because a tree blocked the road. (b) The bus will be late, because a tree is blocking the road.",
               "(a) is an explanation: the lateness has already happened and the sentence gives its cause. (b) is an argument: the lateness is a prediction that "
               "can be doubted, and the tree is offered as a reason to accept it."),
            PQ("Write in standard form: “Every member of the cooperative must attend the meeting, and Mbah is a member. Consequently, Mbah must attend.”",
               "Premise 1: Every member of the cooperative must attend the meeting. Premise 2: Mbah is a member of the cooperative. Therefore: Mbah must attend the meeting. "
               "“Consequently” marks the conclusion."),
            PQ("Why is the word “because” not a perfect sign of an argument? Give an example.",
               "“Because” can begin an explanation of something already accepted, for example “The match was cancelled because the pitch was flooded”. "
               "It signals an argument only when the writer is giving reasons to accept a claim that can be doubted."),
            SUM("An **argument** is a group of statements in which the **premises** are offered as reasons for the **conclusion**.",
                "An argument gives reasons to accept a doubtful claim. An explanation tells why something already accepted happened. An opinion gives no reasons.",
                "Indicator words (therefore, so, because, since) are clues, not proof. Ask what the passage is trying to do.",
                "To find the conclusion ask: “What is the writer trying to make me accept?” It can be first, middle or last.",
                "To standardise: list the premises, remove filler, and put the conclusion last after “Therefore”."),
        ],
    ),

    # ------------------------------------------------------------------ 2. Validity
    lesson(
        module=MODULE,
        topic=VAL,
        title="Validity: when the conclusion must follow",
        slug="arg-validity",
        minutes=22,
        summary="A valid argument is one whose conclusion must be true if its premises are true. Validity belongs to the form of the argument, not to the truth of its statements, so valid arguments can have false conclusions and invalid ones true conclusions.",
        objectives=[
            "Define a valid and an invalid argument",
            "Explain why validity concerns form and not truth",
            "Give examples of a valid argument with a false conclusion and an invalid argument with a true conclusion",
            "Say which combinations of true or false premises and conclusion a valid argument can have",
        ],
        key_concepts=["Validity", "Invalid argument", "Form of an argument", "Truth of statements", "Impossible combination"],
        blocks=[
            H("Introduction"),
            T("A magistrate listens to a witness and asks two different questions. First: “Are the facts you give true?” "
              "Second: “If the facts are true, does your conclusion really follow from them?” These are separate questions. "
              "A witness can answer the first well and the second badly."),
            T("Logic is mainly about the second question. The word for it is **validity**."),
            D("An argument is **valid** if it is impossible for all its premises to be true and its conclusion false. "
              "In other words, if the premises were true, the conclusion would have to be true.",
              title="Definition: valid argument",
              note="An argument that is not valid is **invalid**: it is possible for the premises to be true and the conclusion false."),
            KEY("Truth and validity are different", "They belong to different things.", cards=[
                ["Truth and falsity", "Belong to **statements**. “Yaoundé is the capital of Cameroon” is true."],
                ["Validity and invalidity", "Belong to **arguments**. We say an argument is valid or invalid, never that it is true or false."],
            ]),
            H("Validity depends on form"),
            T("The **form** of an argument is its pattern, what is left when we ignore the particular subjects. "
              "Consider this argument."),
            CODE("All mammals live in water.\nAll goats are mammals.\nTherefore, all goats live in water.", "text", title="Argument A"),
            T("The first premise is false: many mammals live on land. The conclusion is false too. Yet the argument is **valid**. "
              "Why? Suppose, for a moment, that both premises were true. Then every goat would be a mammal, and every mammal would live in water, "
              "so every goat would live in water. The conclusion could not fail. The argument has the pattern “All M are P. All S are M. So all S are P”, "
              "and this pattern always carries truth from premises to conclusion."),
            EX("Worked example 1: valid, but the conclusion is false", intro="Examine Argument A: is it valid? Are its statements true?", steps=[
                S("Check the truth of each statement", text="Premise 1: false. Premise 2: true. Conclusion: false."),
                S("Imagine that the premises are true", text="Then goats belong to the class of mammals, and that whole class lives in water."),
                S("Can the conclusion still be false?", text="No. Goats would live in water. It is impossible to have true premises and a false conclusion."),
                S("Decide", text="The argument is **valid**, even though a premise and the conclusion are false. Validity only says what follows **if** the premises are true."),
            ]),
            H("Invalid arguments can have true conclusions"),
            CODE("All dogs are animals.\nAll cats are animals.\nTherefore, no cat is a dog.", "text", title="Argument B"),
            T("Here both premises are true and the conclusion is also true: no cat is a dog. Yet Argument B is **invalid**. "
              "The premises do not guarantee the conclusion. They only say that dogs and cats are both inside the class of animals. "
              "They say nothing about whether the two groups overlap."),
            T("To see this, keep the pattern “All P are M. All S are M. So no S are P” and change the words. "
              "“All birds are animals. All hens are animals. Therefore, no hen is a bird.” Both premises are true and the conclusion is false. "
              "A pattern that can lead from truths to a falsehood is not valid."),
            EX("Worked example 2: invalid, but the conclusion is true", intro="Examine Argument B and explain why a true conclusion does not make it valid.", steps=[
                S("Check the truth of each statement", text="Both premises are true. The conclusion is true."),
                S("Look at the pattern", text="All P are M. All S are M. Therefore no S are P."),
                S("Try the same pattern with other words", text="P = birds, S = hens, M = animals: both premises are true and the conclusion “no hen is a bird” is false."),
                S("Decide", text="The pattern can fail, so the argument is **invalid**. Its conclusion is true by luck, not because it follows from the premises."),
            ]),
            KEY("What combinations are possible?", "Look at the truth of the premises and the conclusion.", cards=[
                ["Valid, true premises, true conclusion", "All birds are animals. All hens are birds. So all hens are animals."],
                ["Valid, false premise, true conclusion", "All animals can swim. All ducks are animals. So all ducks can swim."],
                ["Valid, false premise, false conclusion", "Argument A (goats and water)."],
                ["Valid, true premises, false conclusion", "**Impossible.** This is exactly what validity rules out."],
                ["Invalid", "Any combination can occur, as Argument B shows."],
            ]),
            D("If an argument is valid and its conclusion is false, then at least one premise must be false.",
              title="Useful consequence",
              note="This is how lawyers and scientists use validity: a false conclusion from a valid argument shows that a premise is wrong."),
            MISTAKE("“The conclusion is true, so the argument is valid”",
                    "Argument B has a true conclusion and is invalid. Validity is about whether the conclusion follows, not whether it happens to be true."),
            MISTAKE("“The conclusion is false, so the argument is invalid”",
                    "Argument A has a false conclusion and is valid. A false conclusion from a valid argument means a premise is false."),
            MISTAKE("Calling arguments “true” or “false”",
                    "Use valid and invalid for arguments, true and false for statements. The word “valid” is not used for a single statement."),
            QUIZ("Which statement about valid arguments is correct?",
                 ["A valid argument must have a true conclusion.", "A valid argument can have true premises and a false conclusion.",
                  "A valid argument can have a false conclusion if at least one premise is false.", "A valid argument must have only true premises."],
                 2, "If the conclusion of a valid argument is false, some premise must be false. A valid argument never has all premises true and a false conclusion.",
                 hint="Remember the one combination that validity rules out.",
                 feedback=["Argument A is valid and its conclusion is false.", "That combination is exactly what validity rules out.", "",
                           "Argument A is valid and one premise is false."]),
            QUIZ("“All members of the choir can sing. All sopranos are members of the choir. Therefore, all sopranos can sing.” This argument is:",
                 ["Invalid, because choir members may have weak voices.", "Valid, because the conclusion follows from the premises.", "Invalid, because it has two premises.", "Valid only if the premises are true."],
                 1, "If both premises were true the conclusion could not fail. The pattern is All M are P, All S are M, so All S are P.",
                 hint="Imagine the premises true. Can the conclusion still fail?",
                 feedback=["That questions the truth of a premise, not the validity.", "", "Two premises are usual in a syllogism.", "Validity does not depend on the premises being true."]),
            TIP("Exam link: Paper 1 asks whether an argument is valid or what follows from validity, and often tests the mistakes above. "
                "Paper 2 may ask you to explain why an argument with a true conclusion is invalid.", title="Exam link"),
            PQ("Can a valid argument have true premises and a false conclusion? Explain.",
               "No. A valid argument is one in which it is impossible for all premises to be true and the conclusion false. If the premises are true, the conclusion must be true."),
            PQ("Give an example of a valid argument with a false conclusion and say which statement is false.",
               "All fish walk on land. All tilapia are fish. Therefore, all tilapia walk on land. The first premise is false and the conclusion is false, "
               "but if the premises were true the conclusion would have to be true, so the argument is valid."),
            PQ("A student says: “This argument has a false conclusion, so it is invalid.” Comment.",
               "The student is not necessarily right. A valid argument can have a false conclusion when at least one premise is false. "
               "To judge validity, we ask whether the conclusion would follow if the premises were true."),
            PQ("“All dogs are animals. All cats are animals. Therefore, no cat is a dog.” The conclusion is true. Explain why the argument is still invalid.",
               "The premises only place dogs and cats inside the class of animals. The same pattern can lead from true premises to a false conclusion: "
               "All birds are animals. All hens are animals. Therefore, no hen is a bird. A pattern that can fail is invalid."),
            SUM("An argument is **valid** if it is impossible for the premises to be true and the conclusion false.",
                "Validity belongs to arguments and depends on their **form**. Truth belongs to statements.",
                "A valid argument can have false premises and a false conclusion. An invalid argument can have true premises and a true conclusion.",
                "A valid argument with a false conclusion must have at least one false premise.",
                "To test, imagine the premises true and ask whether the conclusion could still be false."),
        ],
    ),

    # ------------------------------------------------------------------ 3. Soundness and testing validity
    lesson(
        module=MODULE,
        topic=VAL,
        title="Soundness and the counterexample method",
        slug="arg-soundness-and-testing-validity",
        minutes=22,
        summary="A sound argument is valid and has all its premises true. The counterexample method tests validity by looking for a same-form argument with true premises and a false conclusion. Truth, validity and soundness are related in a two-by-two table.",
        objectives=[
            "Define a sound and an unsound argument",
            "Use the counterexample method to show that an argument is invalid",
            "Explain why failing to find a counterexample does not by itself prove validity",
            "Place an argument in the table of validity and truth of premises",
        ],
        key_concepts=["Soundness", "Unsound argument", "Counterexample", "Same form", "Testing validity"],
        blocks=[
            H("Introduction"),
            T("A cocoa buyer is told: “All the cocoa from this farm is organic. This sack came from this farm. So this sack is organic.” "
              "Should he accept the conclusion? He must make two checks. First: does the conclusion follow from the premises? "
              "Second: are the premises really true? If the answer to both is yes, he can trust the conclusion."),
            D("An argument is **sound** if it is **valid** and **all its premises are true**. "
              "An argument that is invalid, or has at least one false premise, is **unsound**.",
              title="Definition: sound and unsound",
              note="Validity is a check on the form. Soundness adds a check on the facts."),
            KEY("The two checks", "A good argument passes both tests.", cards=[
                ["Test 1: validity", "Could the premises be true and the conclusion false? If not, the argument is valid. Logic can often settle this by looking at form."],
                ["Test 2: truth of the premises", "Are the premises true? This is a question of fact: look at the evidence, the law, the measurements."],
            ]),
            T("If an argument is sound, its conclusion **must** be true. If it is unsound, we learn only that the argument does not prove its conclusion. "
              "The conclusion may still be true or false for other reasons."),
            H("Truth, validity and soundness together"),
            CODE("                   All premises TRUE         At least one premise FALSE\n"
                 "VALID              SOUND                     unsound\n"
                 "                   conclusion must be true   conclusion may be true or false\n"
                 "INVALID            unsound                   unsound\n"
                 "                   conclusion may be         conclusion may be\n"
                 "                   true or false             true or false",
                 "text", title="Table 1. Validity, truth of premises and soundness"),
            T("Read the table by rows and columns. Only one box gives a sound argument: valid form **and** true premises. "
              "Only one box lets us be certain of the conclusion: the sound one."),
            MISTAKE("“The argument is unsound, so its conclusion is false”",
                    "An unsound argument does not prove its conclusion, but it does not disprove it either. "
                    "Concluding “false” from “unsound” is a mistake in reasoning of its own."),
            H("Testing validity by counterexample"),
            D("A **counterexample** to an argument is another argument of the **same form** whose premises are clearly true and whose conclusion is clearly false. "
              "If one exists, the form can lead from truth to falsehood, so the argument is **invalid**.",
              title="Definition: counterexample method",
              note="Same form means the same pattern. We change the subjects but keep the pattern of the statements."),
            KEY("Steps of the method", "To test an argument:", cards=[
                ["1. Find the form", "Replace the subjects with letters, for example All P are M."],
                ["2. Choose new words", "Pick groups you know well so you can tell what is true."],
                ["3. Aim for true premises and a false conclusion", "If you can write such an argument, the original is invalid."],
                ["4. If you cannot", "Do not conclude “valid” too quickly. Failing to find a counterexample proves nothing. Use the Venn diagram test and the rules of the syllogism, taught later in this module."],
            ]),
            EX("Worked example 1: a counterexample", intro=(
                "Test: “All dogs are animals. All cats are animals. Therefore, no cat is a dog.”"), steps=[
                S("Find the form", text="All P are M. All S are M. Therefore no S are P."),
                S("Choose new words", text="P = birds, S = hens, M = animals."),
                S("Write the new argument and check it", text="All birds are animals (true). All hens are animals (true). Therefore, no hen is a bird (false)."),
                S("Decide", text="True premises and a false conclusion in the same form. The original argument is **invalid**, even though its own conclusion is true."),
            ]),
            EX("Worked example 2: a counterexample at once", intro=(
                "Test: “Some mangoes are green. Some green things are leaves. Therefore, some mangoes are leaves.”"), steps=[
                S("Check the statements", text="Some mangoes are green: true. Some green things are leaves: true. Some mangoes are leaves: false."),
                S("Decide", text="The argument itself has true premises and a false conclusion, so it is **invalid**. It is its own counterexample. "
                                 "The word “some” does not link the two groups: the green things that are leaves need not be the green things that are mangoes."),
            ]),
            EX("Worked example 3: sound or unsound?", intro=(
                "“All commercial motorbike riders must hold a licence. All of Mr Ndi's employees are commercial motorbike riders. "
                "Therefore, all of Mr Ndi's employees must hold a licence.” Is it sound?"), steps=[
                S("Test 1: validity", text="The form is All M are P. All S are M. So all S are P. If the premises are true, the conclusion cannot fail. The argument is valid."),
                S("Test 2: truth of the premises", text="Premise 1 is a rule that we can check in the traffic regulations. Premise 2 is a fact about Mr Ndi's staff: we must check who his employees are."),
                S("Decide", text="If both premises are true, the argument is **sound** and the conclusion is certain. If one employee is a cook and not a rider, "
                                 "premise 2 is false, the argument is **unsound**, and the conclusion needs another reason."),
            ]),
            T("Here is a counterexample in symbolic form. The argument “If p then q. q. Therefore p” is written p ⊃ q, q, therefore p. "
              "Look at the row where p is false and q is true."),
            CODE("p  q  |  p ⊃ q  |  q  |  p\n"
                 "T  T  |    T    |  T  |  T\n"
                 "T  F  |    F    |  F  |  T\n"
                 "F  T  |    T    |  T  |  F    <- premises true, conclusion false\n"
                 "F  F  |    T    |  F  |  F",
                 "text", title="Table 2. A truth-table counterexample"),
            T("In the third row both premises are true and the conclusion is false, so the form is invalid. "
              "Example: “If it is raining, the road is wet. The road is wet. So it is raining.” The road may be wet because a water tanker passed. "
              "By contrast, “If p then q. p. Therefore q” has no such row, so it is valid. Truth tables are taught in the symbolic logic module."),
            QUIZ("To show that an argument is invalid by the counterexample method, you must find:",
                 ["An argument of the same form with true premises and a false conclusion.", "An argument of the same form with false premises and a true conclusion.",
                  "A different form whose premises and conclusion are all true.", "An argument of the same form with all statements false."],
                 0, "A counterexample shows that the form can lead from truth to falsehood. That is exactly what validity forbids.",
                 hint="Which combination does validity rule out?",
                 feedback=["", "A valid form can have false premises and a true conclusion, so this proves nothing.", "A different form says nothing about the original.", "A valid form can have all statements false, so this proves nothing."]),
            QUIZ("An argument is valid, but one premise is false. It is:",
                 ["Sound, because it is valid.", "Unsound, and its conclusion must be false.", "Unsound, and its conclusion may be true or false.", "Invalid, because a premise is false."],
                 2, "Soundness needs valid form and true premises. With a false premise the argument is unsound, and it does not tell us whether the conclusion is true.",
                 hint="Which two conditions together make an argument sound?",
                 feedback=["Soundness also needs all premises true.", "An unsound argument does not prove the conclusion false.", "", "Validity does not depend on the truth of premises."]),
            TIP("Exam link: Paper 1 often asks you to classify an argument as valid, invalid, sound or unsound from a short description, "
                "or to pick a counterexample. In Paper 2 you may be asked to show invalidity by a counterexample.", title="Exam link"),
            PQ("Define a sound argument and say what we know about the conclusion of a sound argument.",
               "A sound argument is valid and has all its premises true. Its conclusion must be true, because a valid form carries truth from true premises to the conclusion."),
            PQ("Use a counterexample to show that this is invalid: “All goats are animals. All hens are animals. Therefore, all hens are goats.”",
               "The form is All P are M. All S are M. So all S are P. Check the statements: All goats are animals (true). All hens are animals (true). "
               "All hens are goats (false). The argument has true premises and a false conclusion, so it is invalid. It is its own counterexample."),
            PQ("A valid argument has one false premise. Is it sound? What can you say about its conclusion?",
               "It is not sound, because soundness needs every premise to be true. The conclusion may be true or false: the argument gives no guarantee."),
            PQ("A student says: “I could not find a counterexample, so the argument must be valid.” Comment.",
               "Failing to find a counterexample does not prove validity. The student may not have tried the right words. A complete test, such as the Venn diagram test "
               "or the rules of the syllogism, is needed to show that an argument is valid."),
            SUM("An argument is **sound** if it is valid and all its premises are true. Otherwise it is **unsound**.",
                "The conclusion of a sound argument must be true. An unsound argument leaves the conclusion open: true or false.",
                "In Table 1, only the box with valid form and true premises is sound.",
                "A **counterexample** is an argument of the same form with true premises and a false conclusion. It proves invalidity.",
                "Failing to find a counterexample does not prove validity. Use a full test."),
        ],
    ),

    # ------------------------------------------------------------------ 4. Value of the syllogism
    lesson(
        module=MODULE,
        topic=VALUE,
        title="Why the syllogism matters",
        slug="arg-value-of-the-syllogism",
        minutes=18,
        summary="The syllogism sets out reasoning in three steps, two premises and a conclusion. This makes hidden assumptions visible and lets us test the form and each premise separately. It also has limits.",
        objectives=[
            "Say what a syllogism is and who first studied it systematically",
            "Explain how a syllogism makes reasoning explicit and testable",
            "Bring a hidden premise into the open",
            "State two limits of the syllogism",
        ],
        key_concepts=["Syllogism", "Hidden premise", "Explicit reasoning", "Testing an argument", "Limits of the syllogism"],
        blocks=[
            H("Introduction"),
            T("In a family discussion someone says: “Ako is a trader, so he cannot be trusted.” Everyone feels that something is wrong, "
              "but nobody can say what. The sentence hides a premise: “All traders cannot be trusted.” Once that premise is written out, "
              "everybody can see it is false and unfair."),
            T("This is the main value of the syllogism: it brings reasoning into the open so that it can be examined."),
            D("A **syllogism** is an argument in which a conclusion is drawn from two premises. A **categorical syllogism** has three categorical statements, "
              "two premises and a conclusion, and uses exactly three terms.",
              title="Definition: syllogism",
              note="Categorical statements are the A, E, I and O statements, such as All S are P. The word syllogism comes from a Greek word for reasoning."),
            T("Aristotle, the Greek philosopher of the fourth century before Christ, was the first to study syllogisms systematically. "
              "His work was handed on through the traditional logic taught in schools and universities for many centuries, "
              "and this course follows that tradition."),
            H("What the syllogism gives us"),
            KEY("Four values", "Why logicians use the standard form.", cards=[
                ["It makes reasoning explicit", "Every step is written: two reasons and the conclusion they support. Hidden assumptions come out."],
                ["It makes reasoning testable", "We can test the form (does the conclusion follow?) and each premise (is it true?) **separately**."],
                ["It locates disagreement", "Two people can see exactly which premise they dispute, instead of quarrelling about the whole argument."],
                ["It trains clear thinking", "Used in law, ethics, science and everyday debate: give your reasons, then the conclusion."],
            ]),
            EX("Worked example 1: bringing a hidden premise into the open", intro=(
                "“Mbah is a farmer, so he knows about the weather.” Write this as a syllogism."), steps=[
                S("Find the conclusion", text="Mbah knows about the weather."),
                S("Find the premise that is stated", text="Mbah is a farmer."),
                S("Ask what must be assumed to link them", text="That all farmers know about the weather."),
                S("Write the full syllogism", text="All farmers know about the weather. Mbah is a farmer. Therefore, Mbah knows about the weather."),
                S("Test the premises", text="The form is valid. But the first premise is doubtful: some farmers know the weather well, others less well. "
                                           "The syllogism shows the weak point."),
            ]),
            EX("Worked example 2: locating a disagreement", intro=(
                "A school discussion: “Pupils who cheat must be sent home. Ndip cheated. So Ndip must be sent home.” "
                "One pupil objects that the rule is too hard. Another says Ndip did not cheat. Who disputes what?"), steps=[
                S("Set out the syllogism", text="Premise 1: Pupils who cheat must be sent home. Premise 2: Ndip cheated. Conclusion: Ndip must be sent home."),
                S("Test the form", text="The form is valid: if both premises were true, the conclusion would follow."),
                S("Match each objection to a premise", text="The first pupil disputes premise 1, the rule. The second disputes premise 2, a matter of fact."),
                S("Decide", text="Nobody disputes the logic. The syllogism shows that the discussion is about the rule and about the facts, and these can be settled by the school regulations and by evidence."),
            ]),
            EX("Worked example 3: the three tests in a syllogism", intro=(
                "“No honest person uses a false scale. Some stallholders use a false scale. Therefore, some stallholders are not honest.” Test it."), steps=[
                S("Test the form", text="The form is: No P are M. Some S are M. Therefore some S are not P. It is valid (this was checked by testing every possible arrangement of members in groups)."),
                S("Test the premises", text="Premise 1 is about honesty and false scales: most people would accept it. Premise 2 is a matter of fact that must be shown by evidence."),
                S("Decide", text="If both premises are true, the argument is sound and we must accept the conclusion. If we cannot show premise 2, the argument does not prove it."),
            ]),
            H("The limits of the syllogism"),
            KEY("Two limits", "The syllogism is a tool, not a machine for truth.", cards=[
                ["A valid syllogism can have a false conclusion", "Truth also needs true premises. Logic checks form, not facts."],
                ["It handles statements about classes", "Everyday arguments are often messy. They must be translated into standard form before testing. This is the subject of a later topic."],
            ]),
            MISTAKE("“A syllogism proves anything, because it is logical”",
                    "A syllogism with a false premise can reach a false conclusion. Always test both the form and the premises."),
            MISTAKE("Leaving the hidden premise unspoken",
                    "Many bad arguments sound good only because a doubtful premise stays hidden. Write it out and test it."),
            QUIZ("What is the main value of writing an argument as a syllogism?",
                 ["It guarantees that the conclusion is true.", "It makes the reasoning explicit so that the form and each premise can be tested.",
                  "It makes the argument shorter.", "It removes the need for evidence."],
                 1, "The standard form shows the premises and conclusion and lets us test them separately.",
                 hint="Think of what was hidden in “Ako is a trader, so he cannot be trusted.”",
                 feedback=["A valid syllogism needs true premises for a true conclusion.", "", "Some syllogisms are longer than the original sentence.", "Evidence is still needed to test the premises."]),
            QUIZ("“Ama is a nurse, so she is kind.” The hidden premise is:",
                 ["Ama is kind.", "All nurses are kind.", "Some nurses are kind.", "All kind people are nurses."],
                 1, "To link “nurse” to “kind” for every nurse, including Ama, the argument needs: all nurses are kind. A premise that is only “some” would not support the conclusion.",
                 hint="Write the premise that links the middle term (nurse) to the conclusion's predicate (kind).",
                 feedback=["That is the conclusion.", "", "“Some nurses” would not guarantee that Ama is kind.", "This reverses the link and is not what the argument assumes."]),
            TIP("Exam link: Paper 1 asks about the purpose and benefits of the syllogism. Paper 2 Section A may ask you to state its value or to supply a hidden premise.", title="Exam link"),
            PQ("Give the hidden premise: “Fon is a student, so he has no money.” Say whether you would accept it.",
               "Hidden premise: No student has any money. Full syllogism: No student has any money. Fon is a student. Therefore, Fon has no money. "
               "We should not accept the first premise, because many students have some money. Making it visible shows its weakness."),
            PQ("State two benefits of the syllogism.",
               "(1) It makes reasoning explicit: the premises and conclusion are written out. (2) It makes reasoning testable: we can test the form and each premise separately. "
               "(Also acceptable: it locates disagreement; it trains clear thinking.)"),
            PQ("State two limits of the syllogism.",
               "(1) A valid syllogism does not guarantee a true conclusion, because a premise may be false. (2) It deals with statements about classes, so everyday arguments "
               "must first be translated into standard form."),
            PQ("A pupil says: “This syllogism is valid, so its conclusion is certainly true.” Comment.",
               "Validity only says that the conclusion follows if the premises are true. The conclusion is certain only if the argument is sound, that is valid with all premises true. "
               "The pupil must check the premises."),
            SUM("A **syllogism** draws a conclusion from two premises. A **categorical syllogism** uses categorical statements and three terms.",
                "Aristotle was the first to study syllogisms systematically.",
                "The syllogism makes reasoning **explicit** (hidden premises appear) and **testable** (form and premises are tested separately).",
                "It helps to locate a disagreement: is it about the rule, the facts or the logic?",
                "Its limits: validity does not give truth, and everyday arguments must be put into standard form first."),
        ],
    ),

    # ------------------------------------------------------------------ 5. Structure of the categorical syllogism
    lesson(
        module=MODULE,
        topic=VALUE,
        title="Structure of the categorical syllogism: terms and premises",
        slug="arg-structure-of-the-categorical-syllogism",
        minutes=22,
        summary="A categorical syllogism has three categorical statements and exactly three terms: the minor term S, the major term P and the middle term M. The major premise comes first, the minor premise second and the conclusion last.",
        objectives=[
            "Name the three terms: minor, major and middle",
            "Name the major premise, the minor premise and the conclusion",
            "Write a syllogism in standard form order",
            "Identify the terms and premises in a worked example, even when the premises are not in standard order",
        ],
        key_concepts=["Categorical syllogism", "Minor term", "Major term", "Middle term", "Major premise", "Minor premise", "Standard form"],
        blocks=[
            H("Introduction"),
            T("A trader at Mokolo market says: “All traders at Mokolo market pay a daily fee. All fish sellers are traders at Mokolo market. "
              "So all fish sellers pay a daily fee.” The argument has two reasons and one conclusion, and three groups of people: "
              "traders at the market, fish sellers, and people who pay the fee. This is the shape of a **categorical syllogism**."),
            T("Before we can test a syllogism, we must name its parts. This lesson gives each part its name and its place."),
            D("A **categorical statement** says something about classes. There are four standard forms: "
              "**A** (All S are P), **E** (No S are P), **I** (Some S are P) and **O** (Some S are not P). "
              "S is the **subject term** and P is the **predicate term**.",
              title="Reminder: categorical statements",
              note="These forms belong to the module on propositions. This lesson only needs the idea of subject and predicate."),
            D("A **categorical syllogism** is an argument made of three categorical statements: two **premises** and a **conclusion**. "
              "It contains exactly three **terms**, and each term appears in two of the statements.",
              title="Definition: categorical syllogism"),
            H("The three terms"),
            D("The **minor term** (S) is the **subject** of the conclusion. "
              "The **major term** (P) is the **predicate** of the conclusion. "
              "The **middle term** (M) appears in **both premises** but **not** in the conclusion.",
              title="Definition: minor, major and middle terms",
              note="The middle term links the other two. It does its work in the premises and then disappears."),
            D("The **major premise** is the premise that contains the major term. The **minor premise** is the premise that contains the minor term.",
              title="Definition: major and minor premises",
              note="The names do not depend on length or importance. They depend on which term the premise contains."),
            KEY("Standard form order", "A syllogism is in standard form when:", cards=[
                ["1. Major premise first", "It contains the major term P and the middle term M."],
                ["2. Minor premise second", "It contains the minor term S and the middle term M."],
                ["3. Conclusion last", "It joins S and P: the subject is S, the predicate is P."],
            ]),
            IMG("f5l-arg-syllogism-terms.svg",
                alt="A syllogism about Mokolo market. Major premise: All traders at Mokolo market (middle term, orange) pay a daily fee (major term, blue). "
                    "Minor premise: All fish sellers (minor term, green) are traders at Mokolo market (middle term). "
                    "Conclusion: All fish sellers pay a daily fee. A key names P, S and M.",
                caption="Figure 1. P (blue) is the major term, S (green) the minor term and M (orange) the middle term."),
            KEY("How to name the parts", "Follow these steps in order.", cards=[
                ["Step 1", "Find the conclusion (look for therefore, so, hence)."],
                ["Step 2", "Its subject is S, the minor term. Its predicate is P, the major term."],
                ["Step 3", "The remaining term, found in both premises, is M, the middle term."],
                ["Step 4", "The premise with P is the major premise. The premise with S is the minor premise."],
                ["Step 5", "Rewrite in standard order if needed: major, minor, conclusion."],
            ]),
            EX("Worked example 1: naming the terms", intro=(
                "“All traders at Mokolo market pay a daily fee. All fish sellers are traders at Mokolo market. Therefore, all fish sellers pay a daily fee.” "
                "Name the terms and the premises."), steps=[
                S("Find the conclusion", text="All fish sellers pay a daily fee."),
                S("Name S and P", text="S (minor term) = fish sellers. P (major term) = people who pay a daily fee."),
                S("Name M", text="The term in both premises but not in the conclusion: traders at Mokolo market. M (middle term) = traders at Mokolo market."),
                S("Name the premises", text="Major premise (has P): All traders at Mokolo market pay a daily fee. Minor premise (has S): All fish sellers are traders at Mokolo market."),
            ]),
            EX("Worked example 2: premises in the wrong order", intro=(
                "“All goats are mammals. All mammals are warm-blooded. Therefore, all goats are warm-blooded.” Put it in standard form."), steps=[
                S("Find the conclusion", text="All goats are warm-blooded. S = goats. P = warm-blooded animals."),
                S("Find M", text="Mammals: it is in both premises and not in the conclusion."),
                S("Decide which premise is major", text="“All mammals are warm-blooded” contains P, so it is the major premise. “All goats are mammals” contains S, so it is the minor premise."),
                S("Rewrite in standard order", text="All mammals are warm-blooded (major). All goats are mammals (minor). Therefore, all goats are warm-blooded."),
            ]),
            EX("Worked example 3: a syllogism with particular and negative statements", intro=(
                "“No dishonest act is an act allowed by the school rules. Some actions done in the exam hall are dishonest acts. "
                "Therefore, some actions done in the exam hall are not allowed by the school rules.” Name the parts and the forms of the statements."), steps=[
                S("Conclusion and its terms", text="Some actions done in the exam hall are not allowed by the school rules. S = actions done in the exam hall. P = acts allowed by the school rules."),
                S("Middle term", text="Dishonest acts, in both premises and not in the conclusion."),
                S("Premises", text="Major premise: No dishonest act is an act allowed by the school rules (contains P). Minor premise: Some actions done in the exam hall are dishonest acts (contains S). The order is already standard."),
                S("Forms of the statements", text="Major premise: E. Minor premise: I. Conclusion: O. (The three letters together are called the mood, a later topic.)"),
            ]),
            MISTAKE("The major premise is not the longer or the more important premise",
                    "A premise is major because it contains the major term, the predicate of the conclusion. Find the conclusion first, then look at the premises."),
            MISTAKE("Changing the wording of a term",
                    "Each term must have the same meaning each time it appears. “All banks are near rivers. A bank pays interest. So some things near rivers pay interest.” "
                    "Here “bank” changes meaning, so there are really four terms. This mistake is called the fallacy of four terms and is met again in the rules of the syllogism."),
            MISTAKE("Putting the middle term in the conclusion",
                    "The middle term appears in the premises only. If it is in the conclusion, check whether you have found the right conclusion."),
            QUIZ("In this syllogism the minor term is: “All teachers are graduates. Some women are teachers. Therefore, some women are graduates.”",
                 ["Teachers", "Graduates", "Women", "Some"],
                 2, "The minor term is the subject of the conclusion: women. Graduates is the major term. Teachers is the middle term.",
                 hint="Look at the conclusion first.",
                 feedback=["Teachers is the middle term: it is in both premises and not in the conclusion.", "Graduates is the predicate of the conclusion: the major term.", "", "“Some” is a quantifier, not a term."]),
            QUIZ("The major premise of a syllogism is:",
                 ["The longer premise", "The premise that contains the major term", "The first premise written, whatever it contains", "The premise that contains the middle term only"],
                 1, "Major premise = the premise containing the major term P, the predicate of the conclusion.",
                 hint="Which term is the major term?",
                 feedback=["Length has nothing to do with it.", "", "The order in the passage may be wrong. Standard form puts the major premise first, but you identify it by its term.", "Both premises contain the middle term."]),
            TIP("Exam link: Paper 1 asks you to name the minor, major or middle term or the major premise of a given syllogism. "
                "Paper 2 Section A may ask you to put a syllogism in standard form and name its parts.", title="Exam link"),
            PQ("Name S, P and M: “All farmers who use fertiliser harvest more. All farmers in this village use fertiliser. Therefore, all farmers in this village harvest more.”",
               "Conclusion: all farmers in this village harvest more. S (minor term) = farmers in this village. P (major term) = those who harvest more. "
               "M (middle term) = farmers who use fertiliser."),
            PQ("Rewrite in standard form: “All Cameroonians are Africans. All Doualans are Cameroonians. Therefore, all Doualans are Africans.” (Name the major and minor premises.)",
               "Conclusion: All Doualans are Africans. S = Doualans, P = Africans, M = Cameroonians. Major premise (has P): All Cameroonians are Africans. "
               "Minor premise (has S): All Doualans are Cameroonians. Standard order: major, minor, conclusion."),
            PQ("How many terms does a categorical syllogism have, and how many times does each appear in the three statements?",
               "Three terms: S, P and M. S and P each appear twice (one premise and the conclusion). M appears twice (in both premises) and never in the conclusion."),
            PQ("Why must the middle term not appear in the conclusion?",
               "The middle term only links the two premises and so connects S and P. The conclusion states the connection between S and P themselves. "
               "If the same term is in the conclusion, the argument has not been analysed correctly."),
            SUM("A categorical syllogism has two premises, a conclusion and exactly three terms, each used twice.",
                "**Minor term S** = subject of the conclusion. **Major term P** = predicate of the conclusion. **Middle term M** = in both premises, not in the conclusion.",
                "The **major premise** contains P. The **minor premise** contains S.",
                "Standard form order: major premise, minor premise, conclusion.",
                "Find the conclusion first, then name the terms, then the premises."),
        ],
    ),

    # ------------------------------------------------------------------ 6. The four figures
    lesson(
        module=MODULE,
        topic=FIG,
        title="The four figures: where the middle term stands",
        slug="arg-the-four-figures",
        minutes=20,
        summary="The figure of a syllogism is fixed by the position of the middle term in the premises: figure 1 sub-pre, figure 2 pre-pre, figure 3 sub-sub and figure 4 pre-sub. The figure alone does not tell whether the argument is valid.",
        objectives=[
            "Define the figure of a categorical syllogism",
            "Name and draw the four figures: sub-pre, pre-pre, sub-sub and pre-sub",
            "Identify the figure of a given syllogism, even when the premises are not in standard order",
            "Explain why the figure alone does not decide validity",
        ],
        key_concepts=["Figure", "Position of the middle term", "Subject (sub) and predicate (pre)", "Figure 1", "Figure 2", "Figure 3", "Figure 4"],
        blocks=[
            H("Introduction"),
            T("In a market queue, people can stand in different places in line. In the same way the middle term M can stand in different places in a syllogism. "
              "In each premise it is either the **subject** or the **predicate**. That gives four possible arrangements. Each arrangement is called a **figure**."),
            D("The **figure** of a categorical syllogism is the arrangement of the middle term in the two premises: "
              "whether M is the subject or the predicate in the major premise and in the minor premise.",
              title="Definition: figure",
              note="In this lesson “sub” means subject and “pre” means predicate. The major premise is named first."),
            KEY("The four figures", "Read each name as major premise, then minor premise.", cards=[
                ["Figure 1: sub-pre", "M is the **subject** of the major premise and the **predicate** of the minor premise. Layout: M-P, S-M."],
                ["Figure 2: pre-pre", "M is the **predicate** of both premises. Layout: P-M, S-M."],
                ["Figure 3: sub-sub", "M is the **subject** of both premises. Layout: M-P, M-S."],
                ["Figure 4: pre-sub", "M is the **predicate** of the major premise and the **subject** of the minor premise. Layout: P-M, M-S."],
            ]),
            IMG("f5l-arg-four-figures.svg",
                alt="Four panels. Figure 1, sub-pre: M are P, S are M. Figure 2, pre-pre: P are M, S are M. "
                    "Figure 3, sub-sub: M are P, M are S. Figure 4, pre-sub: P are M, M are S. The conclusion is always S are P.",
                caption="Figure 1. The four figures. S is the minor term, P the major term and M the middle term. The conclusion is always S are P."),
            TIP("Memory aid: in figures 1 and 4 the middle term changes side (subject in one premise, predicate in the other), so the dashed line is slanted. "
                "In figures 2 and 3 it stays in the same column: always predicate (figure 2) or always subject (figure 3)."),
            T("A note on history. Aristotle described three figures. Later logicians added the fourth. Some textbooks teach only three figures, "
              "so follow your teacher's textbook if it differs."),
            H("Identifying the figure"),
            D("To find the figure: (1) find the conclusion and name S and P; (2) find M; (3) identify the major premise and the minor premise; "
              "(4) in each premise, say whether M is the subject or the predicate; (5) read the pattern.",
              title="Rule: identifying the figure"),
            EX("Worked example 1: an argument in standard order", intro=(
                "“No snake is safe to handle. All pythons are snakes. Therefore, no python is safe to handle.” Name the figure."), steps=[
                S("Conclusion", text="No python is safe to handle. S = pythons. P = things safe to handle."),
                S("Middle term", text="Snakes."),
                S("Premises", text="Major premise (has P): No snake is safe to handle. Minor premise (has S): All pythons are snakes."),
                S("Position of M", text="In the major premise M (snake) is the subject. In the minor premise M is the predicate."),
                S("Figure", text="Subject then predicate: sub-pre. It is **figure 1**."),
            ]),
            EX("Worked example 2: premises not in standard order", intro=(
                "“All pupils from Bafoussam are boarders. Some pupils from Bafoussam are footballers. Therefore, some boarders are footballers.” Name the figure."), steps=[
                S("Conclusion", text="Some boarders are footballers. S = boarders. P = footballers."),
                S("Middle term", text="Pupils from Bafoussam."),
                S("Premises", text="Major premise (has P): Some pupils from Bafoussam are footballers. Minor premise (has S): All pupils from Bafoussam are boarders. "
                                    "The premises were written in the wrong order."),
                S("Position of M", text="Subject in the major premise, and subject in the minor premise."),
                S("Figure", text="Sub-sub: **figure 3**."),
            ]),
            EX("Worked example 3: one example for each figure", intro="Each of these arguments has a different figure. Read the pattern of M.", steps=[
                S("Figure 1", text="No reckless driver is a safe driver (M-P). All drivers who overtake on a bend are reckless drivers (S-M). So no driver who overtakes on a bend is a safe driver."),
                S("Figure 2", text="All good farmers weed early (P-M). No lazy farmer weeds early (S-M). So no lazy farmer is a good farmer."),
                S("Figure 3", text="All members of the club are students (M-P). Some members of the club are footballers (M-S). So some footballers are students."),
                S("Figure 4", text="All taxis on this road are licensed vehicles (P-M). No licensed vehicle is a vehicle free to ignore the speed limit (M-S). "
                               "So no vehicle free to ignore the speed limit is a taxi on this road."),
            ]),
            T("The four arguments in the last example are all valid. Each valid form has a name in traditional logic, taught in the next topic on moods."),
            H("A figure is not a verdict"),
            T("The figure only tells us **where** M stands. It does not tell us whether the argument is valid. "
              "The arguments “All P are M. All S are M. So all S are P” and “All P are M. No S are M. So no S are P” both belong to figure 2. "
              "The first is invalid: All goats are animals. All hens are animals. So all hens are goats. The second (the good farmers example) is valid."),
            T("In all, three statements each with four forms (A, E, I, O) give 4 x 4 x 4 = 64 patterns in each figure, and 4 x 64 = 256 arrangements in the four figures. "
              "Only a small number of them are valid. Which ones are valid is the question of the next topic."),
            MISTAKE("Naming the figure from the order of the premises",
                    "The premises may be written in any order. First find the major premise by its term P, then read the position of M."),
            MISTAKE("Mixing up sub and pre",
                    "Sub means subject (the first term of the statement) and pre means predicate (the second). The major premise is always read first."),
            MISTAKE("Thinking that a figure tells us whether the argument is valid",
                    "A figure only describes layout. The same figure contains both valid and invalid arguments."),
            QUIZ("In which figure is the middle term the predicate of the major premise and the subject of the minor premise?",
                 ["Figure 1", "Figure 2", "Figure 3", "Figure 4"],
                 3, "Predicate then subject is pre-sub, which is figure 4.",
                 hint="Say the pattern in the order major premise, minor premise.",
                 feedback=["Figure 1 is sub-pre: M is the subject of the major premise.", "Figure 2 is pre-pre.", "Figure 3 is sub-sub.", ""]),
            QUIZ("“All taxis are licensed vehicles. Some licensed vehicles are old. Therefore, some old vehicles are taxis.” The figure is:",
                 ["Figure 1", "Figure 2", "Figure 3", "Figure 4"],
                 3, "S = old vehicles, P = taxis, M = licensed vehicles. The major premise (has P) is All taxis are licensed vehicles: M is the predicate. "
                    "The minor premise (has S) is Some licensed vehicles are old: M is the subject. Pre-sub, figure 4.",
                 hint="Find the conclusion, then S and P, then the major premise.",
                 feedback=["In figure 1, M is the subject of the major premise.", "In figure 2, M is the predicate of both premises.", "In figure 3, M is the subject of both premises.", ""]),
            TIP("Exam link: Paper 1 asks you to identify the figure of a given syllogism or to match a figure to a layout. "
                "Paper 2 may ask you to draw the four figures or to name the figure of an argument and explain how you found it.", title="Exam link"),
            PQ("Name the four figures by the position of the middle term.",
               "Figure 1: sub-pre (M subject of the major premise, predicate of the minor). Figure 2: pre-pre (M predicate of both). "
               "Figure 3: sub-sub (M subject of both). Figure 4: pre-sub (M predicate of the major premise, subject of the minor)."),
            PQ("Name the figure: “No lazy student passes. All students who copy are lazy students. Therefore, no student who copies passes.”",
               "Conclusion: no student who copies passes. S = students who copy. P = those who pass. M = lazy students. Major premise: No lazy student passes (M is the subject). "
               "Minor premise: All students who copy are lazy students (M is the predicate). Sub-pre, figure 1."),
            PQ("Name the figure: “Some members of the club are footballers. All members of the club are students. Therefore, some footballers are students.”",
               "Conclusion: some footballers are students. S = footballers. P = students. M = members of the club. Major premise (has P): All members of the club are students. "
               "Minor premise (has S): Some members of the club are footballers. M is the subject in both: sub-sub, figure 3."),
            PQ("Do all syllogisms of figure 2 have the same validity? Explain with an example.",
               "No. The figure only gives the position of M. In figure 2, “All good farmers weed early. No lazy farmer weeds early. So no lazy farmer is a good farmer” is valid, "
               "but “All goats are animals. All hens are animals. So all hens are goats” has true premises and a false conclusion, so it is invalid."),
            SUM("The **figure** is the arrangement of the middle term M in the two premises (major premise first).",
                "Figure 1: sub-pre. Figure 2: pre-pre. Figure 3: sub-sub. Figure 4: pre-sub.",
                "To identify the figure: conclusion, then S and P, then M, then the major premise, then the position of M in each premise.",
                "The figure does not decide validity: each figure has both valid and invalid forms.",
                "Aristotle described three figures; the fourth was added by later logicians. Follow your teacher's textbook."),
        ],
    ),
]
