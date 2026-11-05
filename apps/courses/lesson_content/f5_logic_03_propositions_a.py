"""Form 5 Logic: Second Operation of the Mind, Judging (Propositions), part A (7 lessons, one practice set each).

Topics 1.4.1 to 1.4.4: components of a proposition, properties of categorical propositions (quantity, quality,
A E I O), distribution of terms, and symbolization with Venn diagrams (modern, Boolean view).
"""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "The Second Operation of the Mind: Judging (Propositions)"
T1 = "Definition and components of a proposition"
T2 = "Properties of categorical propositions"
T3 = "Distribution of terms in categorical propositions"
T4 = "Symbolization and Venn diagramming of categorical propositions"

LESSONS = []

# ------------------------------------------------------------------ 1. What is a proposition
LESSONS.append(lesson(
    module=MODULE,
    topic=T1,
    title="What is a proposition? Subject, predicate, copula and quantifier",
    slug="prop-what-is-a-proposition",
    minutes=20,
    summary="A proposition is what a statement says: something that can be true or false. This lesson separates propositions from other sentences and names the parts of a categorical proposition.",
    objectives=[
        "Define a proposition and tell it apart from questions, commands and exclamations",
        "Explain the difference between a sentence and the proposition it expresses",
        "Name the subject term, predicate term, copula and quantifier of a categorical proposition",
        "Recognise a categorical proposition as a statement about two classes",
    ],
    key_concepts=["Proposition", "Sentence", "Truth and falsity", "Subject term", "Predicate term", "Copula", "Quantifier", "Categorical proposition"],
    blocks=[
        H("Introduction"),
        T("A trader in Mokolo market says to a buyer, 'This bag of rice is 25 kg.' The buyer weighs it and says, 'No, it is only 23 kg.' "
          "They are arguing about whether one claim is true or false. That is what logic studies: claims that we can accept or reject, "
          "and the way they are put together."),
        T("In the first module you studied the **first operation of the mind**: simple apprehension, which gives us ideas and terms. "
          "Now we study the **second operation of the mind**: **judging**. When we judge, we join or separate two ideas and say "
          "'this is so' or 'this is not so'. The spoken or written result of a judgement is a **proposition**."),
        D("A **proposition** is a statement that says something is the case. It can be true or false. "
          "(Latin: propositio, 'something put forward'.)", title="Proposition"),
        H("Propositions and other sentences"),
        T("Not every sentence is a proposition. We ask one question: can it be called true or false?"),
        KEY("Four kinds of sentence", "Only the first kind is a proposition.", cards=[
            ["Statement", "'Yaoundé is the capital of Cameroon.' It can be true or false."],
            ["Question", "'Is the market open today?' It asks. It is neither true nor false."],
            ["Command", "'Close the door.' It orders. It is neither true nor false."],
            ["Exclamation", "'Hurray for the Lions!' It expresses feeling. It is neither true nor false."],
        ], note="A command can be obeyed or disobeyed, a question can be answered, but only a statement can be true or false."),
        T("A **false** proposition is still a proposition. 'Douala is the capital of Cameroon' is false, but it makes a claim, "
          "so it is a proposition. What matters is that it **can** be true or false, not that it **is** true."),
        D("A **sentence** is a string of words that follows the rules of a language. A **proposition** is the meaning that a "
          "declaring sentence expresses, the claim itself. Different sentences, even in different languages, can express the "
          "same proposition.", title="Sentence and proposition"),
        T("Here are three sentences: 'It is raining in Buea.' 'Il pleut à Buea.' 'Buea is receiving rain.' They are three sentences "
          "but one proposition. If it is raining, all three are true. If not, all three are false. In this course we often say "
          "'statement' for a proposition. We use the word 'proposition' when we talk about its truth and its parts."),
        H("The parts of a categorical proposition"),
        T("Most of the propositions in this module are **categorical propositions**. A categorical proposition makes a plain, "
          "unconditional claim about two **classes** (groups of things). For example, it may say that one class is wholly "
          "inside another, or that two classes have no members in common."),
        D("A **categorical proposition** is a proposition that affirms or denies that one class is included, wholly or partly, "
          "in another class.", title="Categorical proposition"),
        IMG("f5l-prop-parts.svg", alt="The proposition 'All farmers are hard workers' split into four labelled parts: quantifier All, subject term farmers, copula are, predicate term hard workers",
            caption="Figure 1. The four parts of a categorical proposition."),
        D("The **subject term** names the class we are talking about. The **predicate term** names the class we say the subject "
          "belongs to, or does not belong to. The **copula** is the form of the verb 'to be' (are, is, are not, is not) that "
          "joins them. The **quantifier** is the word that tells us how many members of the subject class the claim covers: "
          "all, no, or some.", title="Subject, predicate, copula, quantifier"),
        T("The word 'quantifier' comes from 'quantity', which means 'how much' or 'how many'. In 'All farmers are hard workers', "
          "the quantifier is 'All', the subject term is 'farmers', the copula is 'are' and the predicate term is 'hard workers'."),
        TIP("In a categorical proposition both the subject and the predicate are **terms**: names of classes, not whole sentences. "
            "If you can put 'a class of' before it, it is probably a term. 'Hard workers' is a class. 'Works hard' is not yet a term."),
        EX("Worked example 1: is it a proposition?", intro="Which of these sentences are propositions? (a) 'Does your cousin live in Bafoussam?' (b) 'Some mangoes are sweet.' (c) 'Please pass the water.' (d) 'Every taxi in the town is yellow.'", steps=[
            S("Ask the test question", text="For each one, can we say 'that is true' or 'that is false'?"),
            S("(a) and (c)", text="(a) is a question and (c) is a command (a polite request). Neither can be true or false, so neither is a proposition."),
            S("(b) and (d)", text="Both make a claim. (b) is probably true and (d) is probably false, but we do not need to know which. Both are propositions."),
            S("Answer", text="(b) and (d) are propositions."),
        ]),
        EX("Worked example 2: find the parts", intro="Name the quantifier, subject term, copula and predicate term of 'No student of this school is a prefect' and of 'Some traders are not honest'.", steps=[
            S("First proposition: quantifier", text="'No'. It tells us the claim covers every student of the school, and denies something of each."),
            S("First proposition: the rest", text="Subject term: 'student of this school'. Copula: 'is'. Predicate term: 'prefect'."),
            S("Second proposition: quantifier", text="'Some'. It covers at least one trader, not all of them."),
            S("Second proposition: the rest", text="Subject term: 'traders'. Copula: 'are not'. Predicate term: 'honest' (honest people)."),
            S("Answer", text="In 'No student of this school is a prefect', the quantifier is 'No' and the copula is 'is'. In 'Some traders are not honest', the quantifier is 'Some' and the copula is 'are not'."),
        ]),
        T("In everyday speech we often leave a part out or change it. 'Dogs bark' has no visible quantifier and no copula. "
          "Rewriting such sentences in full form is the work of a later lesson in this module on translating into standard forms."),
        H("Common mistakes"),
        MISTAKE("Thinking a proposition must be true", "A proposition only has to be the kind of sentence that can be true or false. 'The Wouri flows through Yaoundé' is false, and it is still a proposition."),
        MISTAKE("Confusing the sentence with the proposition", "Two different sentences can say the same thing. When we judge truth we look at the claim, not at the exact words."),
        MISTAKE("Calling a command or a question a proposition", "If nobody could reply 'that is true' or 'that is false', it is not a proposition."),
        MISTAKE("Putting the copula in the predicate", "In 'All farmers are hard workers', the predicate term is 'hard workers', not 'are hard workers'. 'Are' is the copula, written separately."),
        TIP("Exam link: Paper 1 (multiple choice) often asks you to pick the proposition from a list of sentences, or to name the subject term, predicate term or copula. Paper 2 Section A may ask you to define a proposition and name its parts.", title="Exam link"),
        QUIZ("Which of these is a proposition?",
             ["Is it Friday today?", "Do your homework now.", "What a beautiful goal!", "Some fish are not mammals."], 3,
             "Only the last one claims that something is so, and so can be true or false. The others are a question, a command and an exclamation.",
             hint="Try adding 'That is true.' after each sentence. Which one still makes sense?",
             feedback=["A question asks for an answer; it cannot be true or false.", "A command is obeyed or disobeyed; it is not true or false.",
                       "An exclamation expresses feeling and makes no claim.", ""]),
        QUIZ("In the proposition 'Some students are athletes', which word is the copula?",
             ["Some", "students", "are", "athletes"], 2,
             "The copula is the form of 'to be' that joins the subject and the predicate: 'are'.",
             hint="Which word links the two classes?",
             feedback=["'Some' is the quantifier.", "'students' is the subject term.", "", "'athletes' is the predicate term."]),
        H("Practice questions"),
        PQ("Give one example each of a question, a command and a proposition about school life.",
           "For example: question 'Is the exam on Monday?', command 'Bring your calculator.', proposition 'The exam is on Monday.' Only the proposition can be true or false."),
        PQ("Explain why 'Cameroon has twelve regions' is a proposition even if a student does not know whether it is true.",
           "A proposition only has to be a claim that can be true or false. This sentence makes a claim, so it is a proposition. Whether it is true is a separate question that we can check."),
        PQ("Name the quantifier, subject term, copula and predicate term in 'All mangoes in this basket are ripe'.",
           "Quantifier: All. Subject term: mangoes in this basket. Copula: are. Predicate term: ripe (ripe things)."),
        PQ("Are 'Elle est médecin' and 'She is a doctor' the same sentence, the same proposition, or both? Explain.",
           "They are two different sentences (different words and language) that express the same proposition, so they are true or false together."),
        SUM("A proposition is a statement that can be true or false. Questions, commands and exclamations are not propositions.",
            "A false proposition is still a proposition. A sentence is the words; a proposition is the claim they express.",
            "A categorical proposition makes a plain claim about two classes.",
            "Its parts are the quantifier, the subject term, the copula and the predicate term.",
            "Everyday sentences often leave parts out; we put them back when we write standard forms."),
    ],
))

# ------------------------------------------------------------------ 2. Quantity and quality
LESSONS.append(lesson(
    module=MODULE,
    topic=T2,
    title="Quantity and quality: the standard forms A, E, I and O",
    slug="prop-quantity-and-quality",
    minutes=22,
    summary="Every categorical proposition has a quantity (universal or particular) and a quality (affirmative or negative). Together they give four standard forms, named A, E, I and O from the Latin Affirmo and Nego.",
    objectives=[
        "Distinguish universal from particular propositions (quantity)",
        "Distinguish affirmative from negative propositions (quality)",
        "State the four standard forms A, E, I and O and explain where the letters come from",
        "Classify everyday propositions by quantity, quality and form",
    ],
    key_concepts=["Quantity", "Universal", "Particular", "Quality", "Affirmative", "Negative", "A E I O", "Affirmo and Nego"],
    blocks=[
        H("Introduction"),
        T("Think about four things a parent might say about a school: 'All pupils wear the uniform.' 'No pupil is allowed to use a phone in class.' "
          "'Some pupils walk to school.' 'Some pupils do not eat at the canteen.' Each one is a categorical proposition. "
          "But they differ in two ways: how many pupils they talk about, and whether they say yes or no."),
        T("Logicians call these two differences **quantity** and **quality**. They sort every categorical proposition into one of four standard forms. "
          "This lesson gives you the four forms and their traditional names. Note: the lesson only classifies propositions, "
          "so it holds in both the traditional and the modern way of reading them."),
        H("Quantity: how many?"),
        D("The **quantity** of a categorical proposition tells how much of the subject class it covers. "
          "A proposition is **universal** if it speaks about every member of the subject class. "
          "It is **particular** if it speaks about only some members, at least one.", title="Quantity"),
        T("Universal propositions use words like **all**, **every**, **each**, **no** and **none**. "
          "Particular propositions use **some**, which in logic means 'at least one, and possibly all'."),
        TIP("In logic 'some' does not mean 'some but not all'. 'Some students are present' stays true if every student is present. "
            "It only rules out 'no student is present'."),
        H("Quality: yes or no?"),
        D("The **quality** of a categorical proposition tells whether it affirms or denies. It is **affirmative** if it says "
          "that the subject class is (wholly or partly) included in the predicate class. It is **negative** if it says that "
          "it is (wholly or partly) excluded from it.", title="Quality"),
        T("Compare 'Some farmers are traders' (affirmative: some farmers belong to the class of traders) with "
          "'Some farmers are not traders' (negative: some farmers are outside the class of traders). "
          "Where is the negative word? In 'No pupil is a thief' it is in the quantifier ('No'). In 'Some farmers are not traders' it is in the copula ('are not')."),
        H("The four standard forms"),
        T("Two quantities and two qualities give four combinations. The traditional logicians gave each one a vowel: A, E, I, O. "
          "The vowels come from two Latin words: **AffIrmo** (I affirm) for the affirmative propositions and **nEgO** (I deny) for the negative ones. "
          "The first vowel of AffIrmo is A and its second is I. The two vowels of nEgO are E and O."),
        KEY("Memory aid", "AffIrmo gives A and I. nEgO gives E and O. The first of each pair is universal, the second is particular.", cards=[
            ["Affirmo (I affirm)", "A: universal affirmative. I: particular affirmative."],
            ["Nego (I deny)", "E: universal negative. O: particular negative."],
        ], note="Say the two words aloud and tick off the vowels: A, I then E, O."),
        CODE(
            "Form  Quantity    Quality      Standard form        Example\n"
            "A     universal   affirmative  All S are P          All pupils wear uniform.\n"
            "E     universal   negative     No S are P           No pupil uses a phone in class.\n"
            "I     particular  affirmative  Some S are P         Some pupils walk to school.\n"
            "O     particular  negative     Some S are not P     Some pupils do not eat at the canteen.",
            "text", title="The four standard forms"),
        T("S stands for the **subject term** and P for the **predicate term**. These are the standard forms used in every textbook the Board lists. "
          "Some books write the forms as SaP, SeP, SiP and SoP; they mean the same thing."),
        D("A **standard-form categorical proposition** has exactly one of four patterns: All S are P (A), No S are P (E), "
          "Some S are P (I), Some S are not P (O).", title="Standard form"),
        EX("Worked example 1: classify a proposition", intro="Give the quantity, quality and form of 'Some taxi drivers in Douala are women'.", steps=[
            S("Quantity", text="'Some' covers only part of the class of taxi drivers in Douala. The quantity is particular."),
            S("Quality", text="The copula is 'are', with no negative word. It says the subject class is included in the class of women. The quality is affirmative."),
            S("Form", text="Particular and affirmative is form I. (Look it up: AffIrmo, second vowel.)"),
            S("Answer", text="Particular affirmative, form I."),
        ]),
        EX("Worked example 2: from the form to a proposition", intro="Write a proposition of form E about farming, with the terms 'cocoa farmers' and 'owners of a tractor'.", steps=[
            S("Which pattern?", text="E is universal negative: No S are P."),
            S("Choose S and P", text="S = cocoa farmers, P = owners of a tractor."),
            S("Write it", text="No cocoa farmers are owners of a tractor."),
            S("Check", text="It speaks of all cocoa farmers (universal) and denies something (negative). It does not matter whether it is true; its form is E."),
        ]),
        EX("Worked example 3: a mixed set", intro="Name the form of each: (a) 'Every footballer in the team is fit.' (b) 'Some players are not fit.' (c) 'None of the tickets is sold out.'", steps=[
            S("(a)", text="'Every' is universal. There is no negative word. Universal affirmative, form A."),
            S("(b)", text="'Some' is particular, 'are not' is negative. Particular negative, form O."),
            S("(c)", text="'None' is universal and negative. Universal negative, form E."),
            S("Answer", text="(a) A, (b) O, (c) E."),
        ]),
        H("Common mistakes"),
        MISTAKE("Reading 'some' as 'only some'", "Some means at least one. 'Some students passed' does not tell us that some students failed."),
        MISTAKE("Putting 'No S are P' in the particular group", "'No' speaks about every member of S, so it is universal. Its quality is negative. It is E."),
        MISTAKE("Mixing up the vowels", "A and I affirm (AffIrmo). E and O deny (nEgO). Universal ones are the first of each pair: A and E."),
        TIP("Exam link: Paper 1 often gives a sentence and asks 'This is a proposition of the form...'. Paper 2 Section A may ask you to state the quantity and quality of a list of propositions.", title="Exam link"),
        QUIZ("What is the quantity and quality of 'No snake is a mammal'?",
             ["Universal affirmative", "Universal negative", "Particular affirmative", "Particular negative"], 1,
             "'No' speaks of every snake (universal) and denies that snakes belong to mammals (negative). It is form E.",
             hint="Does it cover every snake or only some?",
             feedback=["There is a negative word ('No'), so the quality is negative.", "",
                       "'No' covers the whole class, so it is universal.", "'No' covers the whole class, so it is universal."]),
        QUIZ("Which Latin word gives the vowels of the two negative forms?",
             ["Affirmo", "Nego", "Universalis", "Particularis"], 1,
             "Nego ('I deny') contains E and O, the vowels of the universal negative (E) and the particular negative (O).",
             hint="The negative forms deny.",
             feedback=["Affirmo gives the affirmative forms A and I.", "", "Universality is the quantity of A and E, but the word does not give the vowels.",
                       "Particularity is the quantity of I and O, but the word does not give the vowels."]),
        H("Practice questions"),
        PQ("State the quantity and quality of 'All fishermen at Kribi are early risers' and give its form.", "Universal affirmative, form A."),
        PQ("State the form of 'Some taxi drivers are not careful'.", "Particular negative, form O."),
        PQ("Write one proposition of form I about the market.", "For example: 'Some traders at the market are women.' Particular (some) and affirmative (are)."),
        PQ("Explain what 'some' means in logic. Does 'Some students passed' tell you that some failed?", "Some means at least one, and possibly all. It does not tell us that any student failed."),
        SUM("Quantity says how many: universal (all, every, no) or particular (some, meaning at least one).",
            "Quality says yes or no: affirmative or negative.",
            "The four standard forms are A (All S are P), E (No S are P), I (Some S are P) and O (Some S are not P).",
            "The vowels come from AffIrmo (A, I) and nEgO (E, O).",
            "In logic 'some' means at least one and does not exclude all."),
    ],
))

# ------------------------------------------------------------------ 3. The four forms in practice
LESSONS.append(lesson(
    module=MODULE,
    topic=T2,
    title="Reading and writing A, E, I and O in practice",
    slug="prop-the-four-standard-forms-in-practice",
    minutes=22,
    summary="How to read each standard form correctly, how singular propositions are treated as universal, and the common mistakes with some, all and not all.",
    objectives=[
        "Read and write propositions of the forms A, E, I and O correctly",
        "Treat a singular proposition as universal and name its form",
        "Avoid the common confusions between some, all, no and not all",
        "Say which of two propositions is its everyday negation (Not all S are P)",
    ],
    key_concepts=["Standard form", "Singular proposition", "Some", "All", "Not all", "Reading A E I O"],
    blocks=[
        H("Introduction"),
        T("A football fan says, 'All the Indomitable Lions played well today.' A friend answers, 'Not true. Some of them did not play well.' "
          "They have contradicted each other, and the second sentence is not just 'the opposite' of the first. "
          "To argue clearly, you need to read and write the four standard forms accurately."),
        T("In the last lesson you learned the forms A, E, I and O. In this lesson we practise them. We also meet a special case: "
          "propositions about one named person or thing."),
        H("Reading the four forms"),
        KEY("What each form says", "Read the forms in plain words.", cards=[
            ["A: All S are P", "Every member of S is also a member of P. S is wholly inside P."],
            ["E: No S are P", "Not even one member of S is a member of P. The two classes have nothing in common."],
            ["I: Some S are P", "At least one member of S is also a member of P."],
            ["O: Some S are not P", "At least one member of S is not a member of P."],
        ], note="Each pair (A and O, E and I) is a pair of denials: when one is true, the other is false. A later lesson on opposition shows this."),
        T("Two details are important. First, 'All S are P' is about S, not about P. 'All doctors are graduates' does not say that all graduates are doctors. "
          "Second, 'Some S are P' and 'Some S are not P' can both be true. If some of my cousins are tall and some are not, both are true."),
        D("The **standard form** of a categorical proposition is its exact form with a quantifier (All, No, Some), a subject term, a copula "
          "(are or are not) and a predicate term. In standard form the terms are nouns or noun phrases, not adjectives or verbs.",
          title="Standard form"),
        H("Singular propositions"),
        D("A **singular proposition** is a proposition about one particular person or thing, named or pointed to, such as "
          "'Mbarga is a nurse' or 'This mango is ripe'.", title="Singular proposition"),
        T("A singular proposition is not in standard form, but we can write it as a universal proposition. "
          "'Mbarga is a nurse' says that the whole class 'persons identical with Mbarga' (a class with one member) belongs to the class of nurses. "
          "So it is treated as an A proposition. 'Mbarga is not a nurse' is treated as an E proposition."),
        KEY("Singular propositions are treated as universal", "Both the affirmative and the negative are universal because they speak about the whole one-member class.", cards=[
            ["Affirmative singular", "'This mango is ripe.' = All things identical with this mango are ripe things. Form A."],
            ["Negative singular", "'This mango is not ripe.' = No thing identical with this mango is a ripe thing. Form E."],
        ], note="Most textbooks follow this rule, including the ones listed by the Board. If your teacher's book does it differently, follow your teacher's book."),
        EX("Worked example 1: a singular proposition", intro="Write 'Ngwa is not a farmer' in standard form and name its form.", steps=[
            S("Spot that it is singular", text="'Ngwa' names one person."),
            S("Make the subject a class", text="The class is 'persons identical with Ngwa'."),
            S("Write the form", text="No persons identical with Ngwa are farmers. Singular negative propositions are treated as universal negative."),
            S("Answer", text="Standard form E: 'No person identical with Ngwa is a farmer'."),
        ]),
        EX("Worked example 2: from a sentence to a form", intro="A teacher says, 'Not every student passed.' Write it in standard form.", steps=[
            S("What is being denied?", text="'Every student passed' (that is, All students are passers) is denied."),
            S("What is the opposite?", text="If it is false that all students passed, then at least one student did not pass."),
            S("Write it", text="Some students are not passers."),
            S("Answer", text="Form O: 'Some students are not passers'. 'Not all S are P' means 'Some S are not P'."),
        ]),
        EX("Worked example 3: an opposite pair", intro="Ayuk says, 'All the buses to Bamenda leave on time.' Fon says it is not true. What exactly is Fon claiming?", steps=[
            S("Ayuk's form", text="Universal affirmative, A: All buses to Bamenda are buses that leave on time."),
            S("Fon denies A", text="To deny A, Fon only needs one bus that does not leave on time."),
            S("Fon's claim", text="Some buses to Bamenda are not buses that leave on time. This is form O."),
            S("Answer", text="Fon is claiming O. He is not saying that no bus leaves on time. That would be E, a stronger claim than he needs."),
        ]),
        H("Common mistakes"),
        MISTAKE("Turning 'not all' into 'no'", "'Not all students passed' means some did not pass (O). It does not mean that no student passed (E). Mixing these up is a very common error."),
        MISTAKE("Confusing 'some' and 'all'", "'Some farmers are poor' does not say all farmers are poor. And 'All farmers are poor' says much more than 'Some farmers are poor'."),
        MISTAKE("Reading 'All S are P' backwards", "'All cocoa is a crop' does not mean 'All crops are cocoa'. The claim runs from S to P only."),
        MISTAKE("Treating a singular proposition as particular", "'Mbarga is a nurse' is about the whole one-member class, so it is treated as universal (A), not as particular (I)."),
        TIP("'All S are not P' is ambiguous in everyday talk. It can mean 'No S are P' (E) or 'Not all S are P' (O). Ask what the speaker means before you classify it. Later lessons on translation give more help.", title="Watch the word order"),
        TIP("Exam link: Paper 1 asks you to pick the correct standard form of an everyday sentence, or to recognise what 'not all' means. Paper 2 Section A may ask you to classify a list of propositions.", title="Exam link"),
        QUIZ("Which standard form means the same as 'Not all taxi drivers are careful'?",
             ["All taxi drivers are careful.", "No taxi driver is careful.", "Some taxi drivers are careful.", "Some taxi drivers are not careful."], 3,
             "If it is false that all are careful, at least one is not careful: O. It does not say that none is careful.",
             hint="Deny 'all' with the least you need.",
             feedback=["This is the very claim being denied.", "This is far too strong. 'Not all' allows that many are careful.",
                       "This is a different claim; it does not follow from 'not all'.", ""]),
        QUIZ("How is the singular proposition 'This road is flooded' treated in standard form?",
             ["As a particular affirmative (I)", "As a universal affirmative (A)", "As a universal negative (E)", "It is not a categorical proposition"], 1,
             "A singular affirmative proposition speaks about the whole one-member class and is treated as an A proposition.",
             hint="How much of the class 'this road' does it cover?",
             feedback=["It covers the whole class with one member, not just part of it.", "",
                       "There is no negative word in it.", "It is categorical: it affirms that one class is inside another."]),
        H("Practice questions"),
        PQ("Write 'Not every student likes mathematics' in standard form and name the form.", "Some students are not people who like mathematics. Form O."),
        PQ("Treat 'Ngu is a pupil' as a categorical proposition. Write it in standard form and name the form.", "All persons identical with Ngu are pupils. Form A (a singular affirmative proposition is treated as universal)."),
        PQ("Explain, with an example, why 'All S are P' and 'All P are S' are different propositions.", "'All doctors are graduates' is true, but 'All graduates are doctors' is false. The first claim runs from S to P only."),
        PQ("Which of A, E, I or O can be true at the same time as 'Some pupils are girls'? Give one example of each that fits.", "Besides I itself, A can be true (if all the pupils are girls) and O can be true (if some pupils are not girls), but not both at once. E cannot be true, because it says no pupil is a girl."),
        SUM("A says S is wholly inside P; E says S and P have no member in common; I says at least one S is P; O says at least one S is not P.",
            "'All S are P' runs from S to P only: it does not say that all P are S.",
            "Singular propositions are treated as universal: affirmative as A, negative as E.",
            "'Not all S are P' means 'Some S are not P' (O), not 'No S are P'.",
            "Textbooks differ in detail: follow your teacher's textbook if it differs."),
    ],
))

# ------------------------------------------------------------------ 4. What distribution means
LESSONS.append(lesson(
    module=MODULE,
    topic=T3,
    title="What distribution means: when a proposition speaks of a whole class",
    slug="prop-what-distribution-means",
    minutes=20,
    summary="A term is distributed in a proposition when the proposition says something about every member of its class. This lesson explains the idea and gives a simple test you can use on any term.",
    objectives=[
        "Define a distributed and an undistributed term",
        "Explain why distribution belongs to a term in a proposition, not to the term alone",
        "Use the sub-class test to decide whether a term is distributed",
        "Give everyday examples of distributed and undistributed terms",
    ],
    key_concepts=["Distributed term", "Undistributed term", "Class", "Sub-class test", "Reference to a whole class"],
    blocks=[
        H("Introduction"),
        T("In a village near Bafia, a chief says, 'All the cattle owners will pay the new tax.' What does this tell us about cattle owners? "
          "It tells us about every one of them. What does it tell us about taxpayers in general? Very little. The tax may be paid by other people too."),
        T("This is the idea of **distribution**: whether a proposition speaks about the **whole** of a class or only about part of it. "
          "It is a small idea with big uses. It will help you judge arguments (syllogisms) later in this course."),
        H("Distributed and undistributed terms"),
        D("A term is **distributed** in a proposition if the proposition says something about **every** member of the class the term names. "
          "A term is **undistributed** if the proposition speaks only about some members (at least one) and does not tell us about the rest.",
          title="Distributed term"),
        T("Look at 'All teachers are graduates'. It talks about every teacher: Mrs Fon, Mr Tabi, and all the others. "
          "So 'teachers' is distributed. But it does not talk about every graduate. Many graduates are doctors, lawyers or engineers, not teachers. "
          "So 'graduates' is undistributed."),
        KEY("Distribution is about the class, in this proposition", "The same term can be distributed in one proposition and undistributed in another.", cards=[
            ["Distributed", "'All teachers are graduates': the term 'teachers' is distributed (it covers every teacher)."],
            ["Undistributed", "'Some teachers are women': the term 'teachers' is undistributed (it covers only some of them)."],
        ], note="So we always say 'the term T is distributed in this proposition', never just 'the term T is distributed'."),
        H("A simple test: the sub-class test"),
        T("There is a way to test any term. Replace the term by a **sub-class**, a smaller part of the same class, and ask: "
          "'Does the proposition stay true?' If it always does, the term is distributed. If it can become false, the term is undistributed."),
        D("**Sub-class test.** A term is distributed in a true proposition if the proposition stays true when we replace the term by any "
          "sub-class of it. If it may turn false, the term is undistributed.", title="Sub-class test"),
        T("Why does this work? If a proposition speaks about the whole class, then it also speaks about every part of the class. "
          "If it speaks only about some members, those members may not be in the part that we chose."),
        EX("Worked example 1: All teachers are graduates", intro="Apply the sub-class test to both terms of 'All teachers are graduates'.", steps=[
            S("Subject term 'teachers'", text="Replace it by 'mathematics teachers'. 'All mathematics teachers are graduates' is true whenever the original is. So 'teachers' is distributed."),
            S("Predicate term 'graduates'", text="Replace it by 'women graduates'. 'All teachers are women graduates' can be false (there are male teachers). So 'graduates' is undistributed."),
            S("Answer", text="'Teachers' is distributed; 'graduates' is not."),
        ]),
        EX("Worked example 2: No snakes are mammals", intro="Apply the sub-class test to both terms of 'No snakes are mammals'.", steps=[
            S("Subject term 'snakes'", text="Replace by 'pythons': 'No pythons are mammals' is still true. Distributed."),
            S("Predicate term 'mammals'", text="Replace by 'goats': 'No snakes are goats' is still true. Distributed."),
            S("Why?", text="Saying that the two classes have no member in common says something about every snake and about every mammal."),
            S("Answer", text="Both terms are distributed."),
        ]),
        EX("Worked example 3: Some farmers are traders", intro="Apply the sub-class test to both terms of 'Some farmers are traders'.", steps=[
            S("Subject term 'farmers'", text="Replace by 'cocoa farmers': 'Some cocoa farmers are traders' may be false (maybe the farmer-traders grow only maize). Undistributed."),
            S("Predicate term 'traders'", text="Replace by 'wholesale traders': 'Some farmers are wholesale traders' may be false. Undistributed."),
            S("Answer", text="Neither term is distributed."),
        ]),
        T("The fourth case, 'Some S are not P', has an interesting result: the predicate term turns out to be distributed. "
          "We look at it in the next lesson. For now, remember that distribution is not the same as using the word 'all'."),
        H("Common mistakes"),
        MISTAKE("Thinking 'distributed' means 'universal'", "A term can be distributed without a quantifier next to it. In 'No snakes are mammals' the predicate 'mammals' is distributed although no quantifier stands before it."),
        MISTAKE("Saying a term is distributed by itself", "Always say 'in this proposition'. 'Farmers' is distributed in 'No farmers are thieves' but not in 'Some farmers are thieves'."),
        MISTAKE("Mixing 'distributed' with 'spread out' in the everyday sense", "In logic, 'distributed' only means that the proposition says something about every member of the class."),
        TIP("Exam link: this idea is not examined alone as often as it is used. Paper 1 tests it directly ('Which term is distributed in...') and Paper 2 uses it in the rules of the syllogism, where a term that is not distributed cannot be used for a conclusion about the whole class.", title="Exam link"),
        QUIZ("In 'All cars are vehicles', which statement is correct?",
             ["'Cars' is distributed.", "'Vehicles' is distributed.", "Both terms are distributed.", "Neither term is distributed."], 0,
             "The proposition speaks about every car. It does not speak about every vehicle (buses and bicycles are vehicles too).",
             hint="Does the proposition say something about every vehicle?",
             feedback=["", "Not every vehicle is a car, so we are told nothing about all vehicles.",
                       "Only the subject covers its whole class.", "The subject 'cars' is covered completely."]),
        QUIZ("A term is distributed in a proposition when the proposition",
             ["uses the word 'all' before it", "says something about every member of the class", "is true", "uses it as the subject"], 1,
             "Distribution means reference to the whole class named by the term.",
             hint="Think about members of the class, not about words.",
             feedback=["The predicate of 'No S are P' is distributed without any 'all'.", "",
                       "A false proposition can also distribute its terms.", "Predicates can be distributed too, and some subjects are not."]),
        H("Practice questions"),
        PQ("Define a distributed term in your own words.", "A term is distributed in a proposition when the proposition says something about every member of the class that the term names."),
        PQ("Use the sub-class test to decide whether 'students' is distributed in 'All students are learners'.", "Replace 'students' by 'Form 5 students': 'All Form 5 students are learners' stays true. So 'students' is distributed."),
        PQ("Explain why 'graduates' is undistributed in 'All teachers are graduates'.", "The proposition tells us about teachers only. It says nothing about every graduate, since graduates include people who are not teachers."),
        PQ("Why must we say 'distributed in this proposition' and not just 'distributed'?", "The same term can be distributed in one proposition and undistributed in another, for example 'teachers' in 'All teachers are graduates' and in 'Some teachers are women'."),
        SUM("A term is distributed when the proposition speaks about every member of its class; otherwise it is undistributed.",
            "Distribution belongs to a term in a proposition, not to the term alone.",
            "Sub-class test: replace the term by a smaller class. If the proposition stays true, the term is distributed.",
            "Distribution is not the same as using the word 'all'.",
            "Distribution is used later to check syllogisms."),
    ],
))

# ------------------------------------------------------------------ 5. Distribution in A, E, I, O
LESSONS.append(lesson(
    module=MODULE,
    topic=T3,
    title="Distribution in A, E, I and O: the table and the rule of thumb",
    slug="prop-distribution-in-a-e-i-o",
    minutes=22,
    summary="Which terms are distributed in each standard form: A distributes its subject, E both terms, I neither, O its predicate. A two-part rule of thumb makes the table easy to remember.",
    objectives=[
        "State which terms are distributed in each of A, E, I and O",
        "Use the rule: universal propositions distribute the subject, negative propositions distribute the predicate",
        "Count the distributed terms in a proposition",
        "Identify distributed terms in everyday propositions and singular propositions",
    ],
    key_concepts=["Distribution table", "Universal distributes subject", "Negative distributes predicate", "A E I O", "Counting distributed terms"],
    blocks=[
        H("Introduction"),
        T("Imagine a market inspector who says: 'No stall in this row sells expired goods.' Here the inspector has checked every stall and has "
          "also looked at all expired goods and found none of them in that row. The claim covers both classes completely. "
          "Another inspector says: 'Some stalls sell fake goods.' This one covers neither class completely."),
        T("In the last lesson you learned what distribution is. Now you will see which terms are distributed in each of the four standard forms. "
          "The pattern is the same in the traditional and in the modern reading of the propositions, so you can learn it once."),
        H("The table"),
        CODE(
            "Form  Proposition         Subject (S)     Predicate (P)   Distributed\n"
            "A     All S are P         distributed     undistributed   S only\n"
            "E     No S are P          distributed     distributed     S and P\n"
            "I     Some S are P        undistributed   undistributed   none\n"
            "O     Some S are not P    undistributed   distributed     P only",
            "text", title="Distribution in the four standard forms"),
        T("A has one distributed term, E has two, I has none and O has one. Altogether the four forms have four distributed terms."),
        H("Why each result is as it is"),
        KEY("Reasons", "Apply the sub-class test from the last lesson, or think in words.", cards=[
            ["A: All S are P", "Says that every S is in P. Subject distributed. P may be larger than S (all graduates, not only teachers). Predicate undistributed."],
            ["E: No S are P", "S and P have nothing in common, so the claim covers every S and every P. Both distributed."],
            ["I: Some S are P", "Speaks of only some S and only some P. Neither is distributed."],
            ["O: Some S are not P", "Some S are outside the whole class P. P is distributed; S is not (only some S are mentioned)."],
        ], note="The predicate of O is the surprising one: the 'some S' are said to be completely outside P, so the claim reaches every member of P."),
        H("The rule of thumb"),
        D("**Rule of thumb for distribution.** (1) A universal proposition (A or E) distributes its subject term. "
          "(2) A negative proposition (E or O) distributes its predicate term. Nothing else is distributed.", title="Rule of thumb"),
        T("Check the rule against the table. A is universal, so S is distributed; A is affirmative, so P is not. "
          "E is universal and negative, so both are distributed. I is particular and affirmative, so nothing is distributed. "
          "O is particular and negative, so only P is distributed."),
        T("A short way to say it is: **universals open the subject, negatives open the predicate**. This works for every standard form. "
          "It was checked by running through all possible cases of classes in a small universe, and the result agrees with the table."),
        EX("Worked example 1: everyday propositions", intro="Name the distributed terms: (a) 'All lawyers are graduates.' (b) 'No taxi drivers are teachers.' (c) 'Some pupils are prefects.' (d) 'Some Cameroonians are not footballers.'", steps=[
            S("(a) A form", text="Universal affirmative. The subject 'lawyers' is distributed; 'graduates' is not."),
            S("(b) E form", text="Both 'taxi drivers' and 'teachers' are distributed."),
            S("(c) I form", text="Particular affirmative. No term is distributed."),
            S("(d) O form", text="Particular negative. Only the predicate 'footballers' is distributed."),
            S("Answer", text="(a) lawyers; (b) taxi drivers and teachers; (c) none; (d) footballers."),
        ]),
        EX("Worked example 2: a singular proposition", intro="Which terms are distributed in 'Mbarga is a nurse'?", steps=[
            S("Standard form", text="A singular affirmative proposition is treated as A: All persons identical with Mbarga are nurses."),
            S("Apply the table", text="In A the subject is distributed and the predicate is not."),
            S("Answer", text="The subject 'persons identical with Mbarga' is distributed; 'nurses' is not."),
        ]),
        EX("Worked example 3: count the distributed terms", intro="How many terms are distributed in 'No student of this school is a prefect' and in 'Some students are not prefects'? How many does each form have?", steps=[
            S("First proposition: E", text="Both terms are distributed: 2."),
            S("Second proposition: O", text="Only the predicate 'prefects' is distributed: 1."),
            S("Answer", text="2 and 1."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking the predicate of A is distributed", "'All teachers are graduates' does not tell us about every graduate. The predicate of A is undistributed."),
        MISTAKE("Thinking the subject of O is distributed", "'Some S are not P' speaks only about some S. The subject of O is undistributed. Only its predicate is distributed."),
        MISTAKE("Saying that I distributes a term", "The words 'some' and 'are' tell us only about part of each class. I distributes nothing."),
        MISTAKE("Mixing up the two rules", "Universal means the subject is distributed. Negative means the predicate is distributed. They are about different terms."),
        TIP("Exam link: Paper 1 asks 'Which term is distributed in...' or 'In which proposition are both terms distributed?'. In Paper 2 these facts are needed for the rules of the syllogism: undistributed middle and illicit process are fallacies about distribution.", title="Exam link"),
        QUIZ("In which standard form are BOTH terms distributed?",
             ["A", "E", "I", "O"], 1,
             "E, the universal negative: it is universal (subject distributed) and negative (predicate distributed).",
             hint="Which form is both universal and negative?",
             feedback=["A distributes only its subject.", "", "I distributes neither term.", "O distributes only its predicate."]),
        QUIZ("Which term is distributed in 'Some farmers are not traders'?",
             ["Farmers", "Traders", "Both farmers and traders", "Neither"], 1,
             "It is an O proposition: negative, so the predicate 'traders' is distributed. The subject, with 'some', is not.",
             hint="Negative propositions distribute the predicate.",
             feedback=["Only some farmers are covered, so the subject is undistributed.", "", "The subject is undistributed.", "The predicate of a negative proposition is distributed."]),
        H("Practice questions"),
        PQ("Complete: A distributes its ____, E distributes ____, I distributes ____, O distributes its ____.", "A: its subject. E: both terms. I: no term. O: its predicate."),
        PQ("State the rule of thumb for distribution in two sentences.", "A universal proposition distributes its subject. A negative proposition distributes its predicate."),
        PQ("Name the distributed terms in 'No fruit in this basket is rotten'.", "It is form E (No S are P), so both 'fruit in this basket' and 'rotten things' are distributed."),
        PQ("Explain why the predicate of 'Some students are not prefects' is distributed.", "It says that some students are outside the whole class of prefects, so the proposition reaches every prefect: none of them is one of those students. This is why the predicate of O is distributed."),
        SUM("A distributes its subject only; E distributes both terms; I distributes none; O distributes its predicate only.",
            "Rule of thumb: universal propositions distribute the subject; negative propositions distribute the predicate.",
            "The four forms together have four distributed terms.",
            "Singular propositions follow the form they are treated as (A or E).",
            "Distribution is used later to test syllogisms."),
    ],
))

# ------------------------------------------------------------------ 6. Symbolizing categorical propositions
LESSONS.append(lesson(
    module=MODULE,
    topic=T4,
    title="Symbolizing categorical propositions with S and P",
    slug="prop-symbolizing-categorical-propositions",
    minutes=20,
    summary="How to write the four standard forms with the letters S and P, how to choose letters for real terms, and the optional Boolean equations that prepare for Venn diagrams.",
    objectives=[
        "Write the standard symbolic forms of A, E, I and O using S and P",
        "Choose capital letters for the terms of a real proposition and write it in symbolic form",
        "Read the Boolean equations that match each form (optional notation)",
        "Avoid reversing the subject and the predicate when symbolizing",
    ],
    key_concepts=["Symbolization", "S and P", "Standard symbolic forms", "Term letters", "Complement (non-P)", "Boolean equations"],
    blocks=[
        H("Introduction"),
        T("A teacher in Limbe writes on the board: 'All the girls in Form 5 are prefects.' A friend copies it into his notebook as 'G all P'. "
          "He has shortened it. Logic does the same thing, but in a careful way: it replaces the terms by letters so that we can see the form "
          "of a proposition and forget about its subject matter."),
        T("This lesson is about **symbolization**: writing propositions with letters. It prepares you for the Venn diagrams in the next lesson. "
          "(The symbols ~, ., v, ⊃ and ≡ belong to the lessons on symbolic logic and are not needed here.)"),
        D("**Symbolization** means replacing words by letters and signs so that the logical form of a proposition is clear.", title="Symbolization"),
        H("The standard symbolic forms"),
        T("We use the letter **S** for the subject term and the letter **P** for the predicate term. (The letters are from 'subject' and 'predicate'.) "
          "Then the four standard forms become the following."),
        CODE(
            "Form  Standard symbolic form   Short form\n"
            "A     All S are P              SaP\n"
            "E     No S are P               SeP\n"
            "I     Some S are P             SiP\n"
            "O     Some S are not P         SoP",
            "text", title="The standard symbolic forms"),
        T("S and P stand for **classes**, not for single things. The short forms SaP, SeP, SiP, SoP are used in some traditional books: "
          "the vowel in the middle is the form, as you learned in the first lessons of this topic."),
        H("Using letters for real terms"),
        T("When we meet a real proposition, we choose a capital letter for each term. We write what each letter stands for. "
          "This list is called a **key**. For example, in 'All taxi drivers are tired people' we may use D for taxi drivers and T for tired people. "
          "Then the proposition is 'All D are T'. The order matters: the subject term comes first."),
        KEY("How to symbolize", "Four short steps.", cards=[
            ["1. Put it in standard form", "Make sure you have a quantifier, a subject term, a copula and a predicate term."],
            ["2. Pick the letters", "Choose S and P, or a capital letter for each term, and write the key."],
            ["3. Choose the form", "Decide A, E, I or O from the quantity and quality."],
            ["4. Write it", "Put the letters into the standard symbolic form, subject first."],
        ], note="A wrong order changes the meaning: All D are T is not the same as All T are D."),
        EX("Worked example 1: symbolize", intro="Symbolize 'No student of this school is a thief'.", steps=[
            S("Standard form", text="It is already in standard form: quantifier No, subject 'student of this school', copula 'is', predicate 'thief'."),
            S("Key", text="Let S = students of this school and T = thieves."),
            S("Form", text="Universal and negative: E."),
            S("Answer", text="No S are T. (Short form: SeT.)"),
        ]),
        EX("Worked example 2: symbolize a particular proposition", intro="Symbolize 'Some mangoes in this basket are not ripe'.", steps=[
            S("Key", text="M = mangoes in this basket, R = ripe things."),
            S("Form", text="'Some' makes it particular; 'are not' makes it negative. Form O."),
            S("Answer", text="Some M are not R. (Short form: MoR.)"),
        ]),
        EX("Worked example 3: from symbols to words", intro="Key: F = footballers, C = Cameroonians. What does 'All F are C' say? What does 'All C are F' say?", steps=[
            S("First", text="'All F are C' means 'All footballers are Cameroonians'."),
            S("Second", text="'All C are F' means 'All Cameroonians are footballers'."),
            S("Compare", text="These are different propositions. The subject comes first in each."),
            S("Answer", text="All footballers are Cameroonians; all Cameroonians are footballers."),
        ]),
        H("Boolean equations (optional extra)"),
        T("Some textbooks add a second way to write the four forms. It uses the idea of a **complement**: the class of everything that is **not** in a class. "
          "We write P' (read 'non-P') for it. If P is 'people who are late', then P' is everything and everyone who is not late. "
          "We write SP for 'things that are both S and P', and SP' for 'things that are S and not P'."),
        D("**Equation notation.** '= 0' says a class is **empty** (it has no members). '≠ 0' says it has **at least one** member.", title="Empty and not empty"),
        CODE(
            "Form  Words                Equation   Reads\n"
            "A     All S are P          SP' = 0    S-and-not-P is empty\n"
            "E     No S are P           SP  = 0    S-and-P is empty\n"
            "I     Some S are P         SP  != 0   S-and-P has a member\n"
            "O     Some S are not P     SP' != 0   S-and-not-P has a member",
            "text", title="The Boolean equations"),
        T("These match the Venn diagrams of the next lesson. We checked each equation by running through all possible small cases and it agrees with the forms. "
          "Note that SP is the same as PS: 'things that are both' has no order. So I and E can be turned round (Some S are P means Some P are S) but A and O cannot. "
          "The notation is the modern, Boolean one. If your textbook writes it differently, follow your textbook."),
        H("Common mistakes"),
        MISTAKE("Reversing S and P", "In 'All doctors are graduates' the subject is 'doctors'. Writing it as 'All G are D' says that all graduates are doctors, which is a different claim."),
        MISTAKE("Using a letter for a single person without saying it is a class", "S and P stand for classes. For a singular proposition like 'Mbarga is a nurse', S stands for 'persons identical with Mbarga', and the form is A."),
        MISTAKE("Forgetting the 'not' in O", "'Some S are P' is I and 'Some S are not P' is O. The only difference is the word 'not'."),
        MISTAKE("Using the same letter for two different terms", "Give each term its own letter. If S means farmers, do not let it also mean students."),
        TIP("Exam link: Paper 1 may ask you to pick the correct symbolic form of a sentence, or to say what a symbolic form means. Paper 2 Section A may ask you to symbolize a list of propositions with a key.", title="Exam link"),
        QUIZ("Which is the standard symbolic form of 'Some tailors are not women'?",
             ["All T are W", "No T are W", "Some T are W", "Some T are not W"], 3,
             "'Some' makes it particular and 'are not' makes it negative: O, Some S are not P.",
             hint="Look for the word 'not' and for 'some'.",
             feedback=["That would be A: universal and affirmative.", "That would be E: universal and negative.", "That would be I: it drops the 'not'.", ""]),
        QUIZ("In 'SP' = 0', what is being said?",
             ["Everything in S is in P.", "No member of S is a member of P.", "Some S are P.", "Some S are not P."], 0,
             "SP' = 0 says that the class of things that are S and not P is empty. So every S is P: form A.",
             hint="The class S and not P is empty.",
             feedback=["", "That would be SP = 0 (form E).", "That would be SP != 0 (form I).", "That would be SP' != 0 (form O)."]),
        H("Practice questions"),
        PQ("Symbolize 'Every pupil of this class is present' with a key and name the form.", "Key: P = pupils of this class, R = persons present. All P are R. Form A."),
        PQ("Symbolize 'No dog is a cat' with D and C.", "No D are C. Form E."),
        PQ("Write the Boolean equation for 'Some S are not P'.", "SP' != 0 (the class of things that are S and not P has at least one member)."),
        PQ("Explain why 'All S are P' is not the same as 'All P are S', using the Boolean equations.", "'All S are P' is SP' = 0 (S and not P is empty). 'All P are S' is PS' = 0 (P and not S is empty). These are different classes, so the equations say different things."),
        SUM("S stands for the subject term and P for the predicate term; both are classes.",
            "The standard symbolic forms are All S are P (A), No S are P (E), Some S are P (I) and Some S are not P (O).",
            "To symbolize a real proposition, put it in standard form, choose letters, name the form and keep the subject first.",
            "Optional Boolean equations: SP' = 0 (A), SP = 0 (E), SP != 0 (I), SP' != 0 (O).",
            "Textbooks differ in notation: follow your teacher's book if it differs."),
    ],
))

# ------------------------------------------------------------------ 7. Venn diagrams for A, E, I, O
LESSONS.append(lesson(
    module=MODULE,
    topic=T4,
    title="Venn diagrams for A, E, I and O (modern view)",
    slug="prop-venn-diagrams-for-a-e-i-o",
    minutes=25,
    summary="How to draw the four standard forms on a two-circle Venn diagram: shade for empty, X for at least one member. This lesson uses the modern (Boolean) view and explains how it differs from the traditional view.",
    objectives=[
        "Draw a two-circle Venn diagram and name its four regions",
        "Represent each of A, E, I and O correctly with shading or an X",
        "Read a Venn diagram and state the proposition it shows",
        "Explain how the modern (Boolean) view differs from the traditional view",
    ],
    key_concepts=["Venn diagram", "Shading (empty)", "X (at least one member)", "Regions", "Boolean view", "Existential import"],
    blocks=[
        H("Introduction"),
        T("Suppose a teacher says, 'All the girls in our class are prefects.' How can we see exactly what that says? "
          "We can draw two circles: one for 'girls in our class' and one for 'prefects'. We then show, in the picture, which parts are empty. "
          "This is a **Venn diagram**, named after the English logician John Venn, who developed the method in the late nineteenth century. "
          "It uses ideas from George Boole's logic of classes."),
        KEY("Which view does this lesson use?", "Logic books give two readings of A, E, I and O. They differ on one point.", cards=[
            ["Traditional (Aristotelian)", "A universal proposition (A or E) is taken to imply that its subject class has members. So A implies I and E implies O."],
            ["Modern (Boolean)", "A and E make no claim that the subject class has members. Only I and O say that something exists."],
        ], note="This lesson draws the diagrams in the MODERN view. The traditional square of opposition comes in the lessons on opposition. Textbooks differ: follow your teacher's textbook if it differs."),
        H("Drawing the diagram"),
        T("Draw two circles that overlap. Label one S (the subject class) and the other P (the predicate class). They make **four regions**: "
          "S but not P, S and P (the overlap), P but not S, and the outside, which holds things that are neither."),
        IMG("f5l-prop-venn-regions.svg", alt="Two overlapping circles labelled S and P with four regions: S but not P on the left, S and P in the overlap, P but not S on the right, neither outside",
            caption="Figure 1. The four regions of a two-circle Venn diagram."),
        D("**Two marks only.** **Shading** a region means that region is **empty**: it has no members. An **X** in a region means that "
          "region has **at least one member**. A region with neither shading nor X is **unknown**: the proposition does not tell us.",
          title="Shading and X"),
        T("This rule has the key to the whole lesson. A universal proposition (A or E) says that something is **empty**, so we shade. "
          "A particular proposition (I or O) says that something **exists**, so we put an X. The X goes in the one region that the proposition mentions."),
        H("The four diagrams"),
        T("**A: All S are P.** It says that there are no S that are outside P. So the region 'S but not P' is empty. We shade it."),
        IMG("f5l-prop-venn-a.svg", alt="Venn diagram for All S are P: the part of circle S outside circle P is shaded green",
            caption="Figure 2. A: All S are P. The S-but-not-P region is shaded (empty)."),
        T("**E: No S are P.** It says that S and P have no member in common. So the overlap is empty. We shade it."),
        IMG("f5l-prop-venn-e.svg", alt="Venn diagram for No S are P: the overlap of the two circles is shaded green",
            caption="Figure 3. E: No S are P. The overlap is shaded (empty)."),
        T("**I: Some S are P.** It says that something is both S and P. We put an X in the overlap."),
        IMG("f5l-prop-venn-i.svg", alt="Venn diagram for Some S are P: an X in the overlap of the two circles",
            caption="Figure 4. I: Some S are P. An X in the overlap (at least one member)."),
        T("**O: Some S are not P.** It says that something is S and not P. We put an X in the part of S that is outside P."),
        IMG("f5l-prop-venn-o.svg", alt="Venn diagram for Some S are not P: an X in the part of circle S outside circle P",
            caption="Figure 5. O: Some S are not P. An X in the S-but-not-P region."),
        CODE(
            "Form  Region                 Mark\n"
            "A     S but not P            shade (empty)\n"
            "E     S and P (overlap)      shade (empty)\n"
            "I     S and P (overlap)      X (at least one)\n"
            "O     S but not P            X (at least one)",
            "text", title="Summary of the four diagrams"),
        T("Notice the pattern: A and O use the same region but opposite marks. E and I use the same region (the overlap) but opposite marks. "
          "This matches the fact that A and O deny each other, and so do E and I. We checked it by running through all the possible fillings of the regions in a small universe. "
          "This is why these two pairs are called **contradictories**, as the lessons on opposition will explain."),
        H("How this differs from the traditional view"),
        T("In the diagram of A there is **no X** anywhere. So the diagram does not say that any S exists. 'All unicorns are horses' can be drawn on it. "
          "This is the modern, Boolean view. In the traditional view, A also says that S has members, so a traditional textbook may draw an A diagram with an extra X in the overlap. "
          "In the same way a traditional E diagram has an extra X in the S-but-not-P region."),
        T("That is why, on the diagrams above, **A does not give I** and **E does not give O** (the modern view). In the traditional view they do. "
          "The lessons on the square of opposition show which relations remain in each view. In the modern view only the contradictories (A and O, E and I) are left."),
        EX("Worked example 1: draw a proposition", intro="Draw 'All cocoa farmers are growers of cash crops'.", steps=[
            S("Letters", text="S = cocoa farmers, P = growers of cash crops. The form is A."),
            S("Circles", text="Draw two overlapping circles labelled S and P."),
            S("Mark", text="A says there are no S outside P. Shade the part of S that lies outside P."),
            S("Answer", text="Left crescent of S shaded; no X anywhere (the diagram does not claim that cocoa farmers exist)."),
        ]),
        EX("Worked example 2: draw an O proposition", intro="Draw 'Some bus drivers are not careful'.", steps=[
            S("Letters", text="S = bus drivers, P = careful people. The form is O."),
            S("Region", text="O speaks about S but not P: the left crescent of S."),
            S("Mark", text="Put an X in that region. Do not shade anything."),
            S("Answer", text="One X in the S-but-not-P region."),
        ]),
        EX("Worked example 3: read a diagram", intro="Two circles S and P. The overlap is shaded and there is nothing else. What proposition does it show?", steps=[
            S("What is shaded?", text="The overlap, the region 'S and P'. Shading means empty."),
            S("What does that say?", text="Nothing is both S and P."),
            S("Answer", text="No S are P (form E). Because the overlap has no order, it also shows 'No P are S'."),
        ]),
        H("Common mistakes"),
        MISTAKE("Shading for particular propositions", "Shading always means empty. For 'Some' you write an X, never shading."),
        MISTAKE("Putting an X in a universal diagram", "'All S are P' only empties a region. In the modern view it does not put an X anywhere."),
        MISTAKE("Marking the wrong region for O", "'Some S are not P' is about S outside P, not about P outside S. Put the X in the left crescent."),
        MISTAKE("Reading an unmarked region as empty", "A region with neither shading nor X is unknown. Only shading means empty."),
        TIP("Exam link: Paper 1 may show a Venn diagram and ask which proposition it shows. Paper 2 Section A may ask you to draw all four. Later you will use Venn diagrams to test syllogisms. Always say that you are using the modern view, and check your textbook if it differs.", title="Exam link"),
        QUIZ("Which Venn diagram shows 'Some S are not P'?",
             ["The overlap shaded", "The S-but-not-P region shaded", "An X in the overlap", "An X in the S-but-not-P region"], 3,
             "O says there is at least one S that is not P. We put an X in the part of S outside P.",
             hint="Some means X. Which region is S without P?",
             feedback=["Shading the overlap shows E.", "Shading the S-but-not-P region shows A.", "An X in the overlap shows I.", ""]),
        QUIZ("In the modern view, what does the diagram for 'All S are P' tell us about whether any S exist?",
             ["That some S exist.", "That no S exist.", "Nothing: it only says there is no S outside P.", "That all P are S."], 2,
             "The diagram only shades S-but-not-P. It has no X, so it does not say that S has members.",
             hint="Look for an X in the diagram.",
             feedback=["That would need an X, which A does not have in the modern view.", "The overlap is not shaded, and the S circle is not shaded as a whole.",
                       "", "A runs from S to P only; it does not say that all P are S."]),
        H("Practice questions"),
        PQ("Draw and name the four regions of a two-circle diagram.", "Two overlapping circles S and P. Regions: S but not P; S and P (overlap); P but not S; neither (outside both)."),
        PQ("Draw the diagram of 'No taxis are free'.", "Key: S = taxis, P = free things. E: shade the overlap of S and P."),
        PQ("Which region contains the X in the diagram of 'Some S are P', and which in 'Some S are not P'?", "'Some S are P': the overlap. 'Some S are not P': the part of S outside P."),
        PQ("State one difference between the traditional and the modern reading of A.", "In the traditional reading A is taken to imply that S has members (so A implies I). In the modern reading it makes no such claim, so the diagram of A has no X."),
        SUM("A Venn diagram of two overlapping circles has four regions: S not P, S and P, P not S, and neither.",
            "Shading means empty. An X means at least one member. No mark means unknown.",
            "A: shade S-but-not-P. E: shade the overlap. I: X in the overlap. O: X in S-but-not-P.",
            "This lesson uses the modern (Boolean) view, where A and E make no claim that S has members; the traditional view says they do.",
            "Contradictories (A with O, E with I) use the same region with opposite marks."),
    ],
))
