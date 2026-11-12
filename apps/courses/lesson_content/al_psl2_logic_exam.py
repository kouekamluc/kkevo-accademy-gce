"""A Level Philosophy (0790), Lower Sixth: Traditional Formal Logic; Symbolic / Propositional Logic; and the Examination
module (Paper 1, Paper 2, Paper 3).

Draft content written from KKEVO's master curriculum blueprint (PHI-0790-L6M4 and L6M5) and the topic list in
apps/academics/gce_curriculum.py. Exam facts are only those of the Board's 2023 Advanced Level subject report for 0790:
Paper 1 = 50 multiple-choice questions covering the whole syllabus; Paper 2 = Western philosophy, African philosophy and
textual analysis (marked by examiners); Paper 3 = Logic (traditional logic, propositional calculus, first-order predicate
calculus) and philosophical problems / systematic philosophy (marked by examiners). The report praises step-by-step
(item-, task- and skill-based) marking and criticises, for logic, answers that are not broken into sub-parts, fallacies
named in general terms instead of explained in the case, and symbolisation that does not begin with a paraphrase. The
blueprint's weights (30/35/35) and wording differ from the report in places; the report is followed, and students are
told to check the exact format with their teacher.

The logic is taught in the traditional (Aristotelian) manner with the Board's symbols: ~ (not), . (and), v (or),
> written as the horseshoe (if ... then) and = written as the triple bar (if and only if), using the letters A, E, I, O
for the categorical forms. EVERY truth table, syllogism (figure, mood, validity), immediate inference and proof line in
this file was checked by brute force in Python (all interpretations of three terms for syllogisms, all rows of the
truth table for propositional claims, and a proof checker that tests every line against its rule). Where textbooks
differ (existential import, the number of valid moods, the exact list of replacement rules, the order of premises, the
symbol for conjunction) the lesson says "check your textbook". All people, places and figures in examples are invented
for practice. No quotations are used.
"""

from .dsl import *  # noqa: F403

COURSE = ("philosophy", "lower-sixth")

M4 = "Traditional Formal Logic"
M5 = "Symbolic / Propositional Logic"
M_EXAM = "Examination"

LESSONS = []

# ---------------------------------------------------------------- M4.1 Terms and categorical propositions
LESSONS.append(lesson(
    module=M4,
    topic="Terms and categorical propositions",
    title="Terms and the four categorical propositions A, E, I and O",
    slug="psl2-terms-categorical-propositions",
    minutes=22,
    summary="Logic studies whether conclusions follow from premises. This lesson defines terms (extension and comprehension), the four categorical forms A, E, I and O, distribution of terms, and how to put ordinary sentences into standard form.",
    objectives=[
        "Distinguish the extension (denotation) from the comprehension (intension) of a term",
        "State the form, quantity and quality of the propositions A, E, I and O",
        "Say which terms are distributed in each form and why",
        "Translate everyday sentences, including 'only' and 'not all', into standard categorical form",
    ],
    key_concepts=["Term", "Extension", "Comprehension", "Categorical proposition", "Quantity and quality", "Distribution", "Standard form"],
    blocks=[
        H("Introduction: reasoning that can be checked"),
        T("A student in Bamenda argues: all the taxi drivers on this road are members of the union, Mbah drives a taxi on this road, so Mbah is a member of the union. "
          "Whether Mbah really is a member is a question of fact. Whether the conclusion *follows* from the two statements before it is a question of logic. "
          "Logic is the study of the correctness of reasoning: it gives us rules to test whether a conclusion follows, whatever the subject is about."),
        D("An **argument** is a set of statements in which some (the **premises**) are offered as reasons for another (the **conclusion**). "
          "An argument is **valid** when it is impossible for the premises to be true and the conclusion false. "
          "It is **sound** when it is valid and its premises are in fact true.", title="Argument, validity, soundness"),
        T("Validity concerns *form*, not truth. 'All fish are birds; all birds can swim; so all fish can swim' has false premises and a false conclusion, but it is valid in form, because if the premises were true the conclusion would have to be true. "
          "Traditional (Aristotelian) logic studies the forms of arguments built from statements about classes. This module begins with the building blocks."),
        H("Terms: extension and comprehension"),
        D("A **term** is a word or phrase that can be the subject or the predicate of a proposition and that stands for a class of things (for example *taxi driver*, *town in the Littoral Region*, *mortal*). "
          "The **extension** (or **denotation**) of a term is the class of things to which it applies. "
          "The **comprehension** (or **intension**, **connotation**) of a term is the set of attributes that something must have to be called by that term.", title="Term, extension, comprehension"),
        T("The extension of *river* is every river there is; its comprehension is something like 'a large natural flow of water in a channel'. "
          "Traditional logicians noted a relation between the two: when you add attributes to a term, you usually shrink its extension. *Town* applies to many places; *port town* applies to fewer; *port town on the Atlantic coast of Cameroon* applies to fewer still. "
          "More comprehension, less extension, and the other way round. (Textbooks state this 'inverse variation' with some care, because it holds for terms built by adding attributes to one another. Check your textbook.)"),
        KEY("Kinds of term to recognise", "Textbooks classify terms in several ways; these are the usual ones.", cards=[
            ["Singular and general", "A singular term names one individual (Douala, Mount Cameroon). A general term applies to many (city, mountain)."],
            ["Concrete and abstract", "A concrete term names things (table, teacher). An abstract term names an attribute (honesty, redness)."],
            ["Positive, negative, privative", "Positive: *healthy*. Negative: *non-healthy* (everything that is not healthy). Privative: *blind* (lacking a capacity that should be present)."],
            ["Collective and distributive use", "A term used collectively refers to the group as a whole (the team won); used distributively it refers to each member (the players are tired)."],
        ]),
        H("The four categorical propositions"),
        D("A **categorical proposition** asserts or denies that one class (the **subject term**, S) is included in another (the **predicate term**, P), wholly or in part. "
          "Its **quantity** is universal (all or none of S) or particular ('some' means at least one). Its **quality** is affirmative or negative.", title="Categorical proposition"),
        CODE("Name  Standard form        Quantity     Quality\n"
             "A     All S are P          universal    affirmative\n"
             "E     No S are P           universal    negative\n"
             "I     Some S are P         particular   affirmative\n"
             "O     Some S are not P     particular   negative", "text", title="Table 1. The four standard forms"),
        T("The letters come from the Latin words AffIrmo (I affirm) for A and I, and nEgO (I deny) for E and O. "
          "Remember that 'some' in logic means *at least one, and possibly all*. 'Some students passed' is true even if every student passed. It does not mean 'some but not all'."),
        IMG("alpsl2-aeio-venn.svg", alt="Four two-circle Venn diagrams for A, E, I and O: A shades the part of S outside P, E shades the overlap, I puts an X in the overlap, O puts an X in S outside P.",
            caption="Figure 1. The four forms as Venn diagrams. Shading means 'nothing here'; X means 'something here'."),
        H("Distribution of terms"),
        D("A term is **distributed** in a proposition when the proposition says something about *every* member of the class the term stands for. Otherwise it is **undistributed**.", title="Distribution"),
        CODE("Form  Subject (S)       Predicate (P)\n"
             "A     distributed       undistributed\n"
             "E     distributed       distributed\n"
             "I     undistributed     undistributed\n"
             "O     undistributed     distributed", "text", title="Table 2. Distribution of terms"),
        T("Why? 'All taxi drivers are union members' talks about every taxi driver, but not about every union member (there may be members who are teachers). So S is distributed and P is not. "
          "'No taxi driver is a thief' excludes every taxi driver from the thieves and every thief from the taxi drivers: both terms are distributed. "
          "'Some taxi drivers are union members' speaks of only some drivers and some members: neither is distributed. "
          "'Some taxi drivers are not union members' speaks of some drivers, but says that those drivers are outside the whole class of union members, so P is distributed. "
          "A memory rule: universal propositions distribute their subject; negative propositions distribute their predicate."),
        MISTAKE("Thinking the predicate of A is distributed", "'All S are P' does not say that all P are S. If you convert A simply you are reading a distribution that is not there. This error leads to the fallacy of illicit process (lesson 3)."),
        H("Putting sentences into standard form"),
        T("Ordinary sentences rarely come in the pattern 'All S are P'. To test an argument you first rewrite each sentence with the exact form: quantifier, subject term, copula 'are' or 'are not', predicate term. Both terms must be nouns or noun phrases, naming classes."),
        EX("Worked example 1: translating sentences", intro="Put each sentence into standard form and name it A, E, I or O: (a) Every candidate in the hall was nervous. (b) Not all bakers in Limbe sell bread. (c) Only members may vote. (d) Douala is a port. (e) No mango on this tree is ripe.", steps=[
            S("(a)", text="All candidates in the hall are nervous persons. Form A."),
            S("(b)", text="Some bakers in Limbe are not sellers of bread. Form O. 'Not all S are P' means that at least one S is not P."),
            S("(c)", text="All persons who may vote are members. Form A with the terms reversed: 'only' introduces the subject of the universal, not its predicate. It does not say that all members may vote."),
            S("(d)", text="All things identical with Douala are ports. Form A. A singular proposition about one named thing is treated as universal, because it speaks of the whole 'class' of one member. 'Douala is not a capital' would be E."),
            S("(e)", text="No mangoes on this tree are ripe fruits. Form E."),
        ]),
        KEY("Words that need care", "These words hide the form.", cards=[
            ["'Only', 'none but'", "'Only S are P' becomes 'All P are S'."],
            ["'Not all'", "'Not all S are P' is O: 'Some S are not P'."],
            ["'All ... are not'", "Ambiguous. 'All politicians are not honest' may mean E or O. Ask what is meant before choosing."],
            ["'Few', 'most', 'almost all'", "Not standard forms. Say what is asserted, usually 'Some S are P' (I), perhaps with a second proposition 'Some S are not P'."],
            ["'Whoever', 'anyone who'", "'Whoever cheats is punished' is 'All cheats are punished persons' (A)."],
        ]),
        EX("Worked example 2: naming the distributed terms", intro="State the distributed terms in: (a) All doctors are graduates. (b) Some tailors are not women. (c) No nurse is untrained.", steps=[
            S("(a)", text="A: subject 'doctors' is distributed; 'graduates' is not."),
            S("(b)", text="O: only the predicate 'women' is distributed. We say something about all women: the tailors in question are outside that class."),
            S("(c)", text="E: both 'nurses' and 'untrained persons' are distributed."),
        ]),
        MISTAKE("Mixing up truth and form", "A proposition can be of form A and be false ('All snakes are fish'). When you classify a statement as A, E, I or O you are describing its form, not judging whether it is true."),
        QUIZ("Which proposition distributes only its predicate?", ["A: All S are P", "E: No S are P", "I: Some S are P", "O: Some S are not P"], 3,
             "O: 'Some S are not P' says that the S in question are outside the whole of P, so P is distributed. S is not, because only some S are mentioned.",
             hint="Which form is both particular and negative?",
             feedback=["In A it is the subject that is distributed, not the predicate.", "In E both terms are distributed.", "In I neither term is distributed.", ""]),
        QUIZ("'Only members may enter' is best put in standard form as", ["All members are persons who may enter", "All persons who may enter are members", "Some members may enter", "No non-member is a member"], 1,
             "'Only members' marks the class that is the whole of the entrants: everyone who may enter is a member. It does not promise that every member may enter.",
             hint="Who is described by 'all'? The people who may enter, or the members?",
             feedback=["This reverses the sentence and claims more than it says.", "", "This is a weaker particular proposition; the sentence is universal.", "This is a contradiction in terms, not a translation."]),
        PQ("Practice question 1. Explain the difference between the extension and the comprehension of the term 'teacher'. How does the extension change if we use 'secondary-school teacher in Bafoussam'?",
           "Extension: all teachers, past, present and future if we count them; comprehension: the attributes that make a person a teacher (for example, a person who instructs others as a profession). "
           "Adding attributes (secondary school, in Bafoussam) increases the comprehension and reduces the extension, because fewer persons fit the narrower term."),
        PQ("Practice question 2. For each proposition give its form, quantity, quality and distributed terms: (a) No tortoise is quick. (b) Some farmers in Bamenda grow cocoa.",
           "(a) E, universal negative; subject 'tortoises' and predicate 'quick things' are both distributed. (b) I, particular affirmative; neither term is distributed."),
        PQ("Practice question 3. Put into standard form and name: 'Not all of the guests were invited.'",
           "Some guests are not invited persons. This is O, particular negative. 'Not all S are P' is contradicted by 'All S are P', and it means that at least one S is not P."),
        SUM("A term has an extension (the things it applies to) and a comprehension (the attributes that qualify something for the term).",
            "The four categorical forms are A (All S are P), E (No S are P), I (Some S are P) and O (Some S are not P); 'some' means at least one.",
            "Universal propositions distribute the subject; negative propositions distribute the predicate: A distributes S, E both, I neither, O only P.",
            "Before testing any argument, put each sentence in standard form: quantifier, subject class, copula, predicate class. 'Only S are P' is 'All P are S'.",
            "Validity is about form. A valid argument can have false premises, and a true conclusion does not prove validity."),
        TIP("Exam link: the Board's Paper 1 has 50 multiple-choice questions on the whole syllabus, and logic items test exactly these skills: naming forms, distribution, and standard-form translation. Paper 3 has logic problems; the report advises breaking each problem into sub-parts."),
    ],
))

# ---------------------------------------------------------------- M4.2 Square of opposition and immediate inferences
LESSONS.append(lesson(
    module=M4,
    topic="The square of opposition and immediate inferences",
    title="The square of opposition, conversion, obversion and contraposition",
    slug="psl2-square-immediate-inferences",
    minutes=24,
    summary="The square of opposition shows how A, E, I and O contradict, oppose and imply one another; conversion, obversion and contraposition (eductions) rewrite one proposition as an equivalent or implied one. Existential import is the point on which logicians differ.",
    objectives=[
        "Use the square to infer the truth value of one form from another (contradictories, contraries, subcontraries, subalternation)",
        "Explain what existential import is and how it changes the square",
        "Apply conversion, obversion and contraposition and say when each is valid",
        "Avoid the usual errors: negating A with E, converting A simply, contraposing I",
    ],
    key_concepts=["Contradictory", "Contrary", "Subcontrary", "Subalternation", "Existential import", "Conversion", "Obversion", "Contraposition", "Immediate inference"],
    blocks=[
        H("Introduction: inferring from one statement"),
        T("An **immediate inference** draws a conclusion from a single premise. If it is false that 'all the buses leaving Yaoundé tonight are full', what can we say about 'some buses are not full'? And can we turn 'no teacher is idle' into 'no idle person is a teacher'? "
          "This lesson answers such questions exactly. There are two families of immediate inference: **opposition** (from the square) and **eduction** (conversion, obversion, contraposition)."),
        H("The square of opposition"),
        IMG("alpsl2-square.svg", alt="The square of opposition: A at top left, E at top right, I at bottom left, O at bottom right; diagonals are contradictories, top line contraries, bottom line subcontraries, left and right sides subalternation.",
            caption="Figure 1. The traditional square of opposition for propositions with the same subject and predicate."),
        D("Two propositions with the same subject and predicate that differ in quantity or quality are **opposed**. "
          "**Contradictories** (A and O, E and I) cannot both be true and cannot both be false: exactly one is true. "
          "**Contraries** (A and E) cannot both be true but can both be false. "
          "**Subcontraries** (I and O) cannot both be false but can both be true. "
          "**Subalternation** links a universal (the *superaltern*) to the particular of the same quality (the *subaltern*): A to I, E to O. If the universal is true the particular is true; if the particular is false the universal is false.", title="Kinds of opposition"),
        T("Check with a case. Let S be 'houses on Mile 17' and P be 'houses with water'. The contradictory of 'All S are P' is 'Some S are not P', *not* 'No S are P'. "
          "If it is false that all the houses have water, we only learn that at least one lacks water: perhaps most have it. 'No house has water' is not forced."),
        CODE("Given        A    E    I    O\n"
             "A is true    T    F    T    F\n"
             "A is false   F    ?    ?    T\n"
             "E is true    F    T    F    T\n"
             "E is false   ?    F    T    ?\n"
             "I is true    ?    F    T    ?\n"
             "I is false   F    T    F    T\n"
             "O is true    F    ?    ?    T\n"
             "O is false   T    F    T    F", "text", title="Table 1. What each truth value tells us (traditional square; ? = undetermined)"),
        H("Existential import"),
        D("A universal proposition has **existential import** when it is taken to assert that its subject class has members. On the traditional view all four forms have import, so 'All S are P' implies 'Some S are P'. "
          "On the modern (Boolean) view only particular propositions have import; universal propositions are read as 'if anything is S, it is P' and can be true of an empty class.", title="Existential import"),
        T("The difference matters. 'All dragons in this school are green' is true on the modern reading (there are no dragons) and awkward on the traditional one. "
          "On the Boolean view, A and E can both be true (when S is empty), I and O can both be false, and subalternation fails. Only the contradictory relations (A-O, E-I) survive unchanged. "
          "Most school texts teach the traditional square, which assumes that the terms are not empty. Many also mention the Boolean objection. Check which your teacher expects."),
        MISTAKE("Giving E as the contradictory of A", "'No S are P' is the *contrary* of 'All S are P': both can be false (some S are P and some are not). The contradictory of A is O. Examiners set this trap often; the Board's 2023 report shows a multiple-choice item on identifying an oppositional inference."),
        EX("Worked example 1: reading the square", intro="It is false that 'Some of the candidates in Hall B are absent' (I). What can be said about A, E and O for the same S and P (candidates in Hall B, absent persons)?", steps=[
            S("Contradictory", text="The contradictory of I is E: 'No candidates in Hall B are absent'. If I is false, E is true."),
            S("Contrary", text="A ('All candidates in Hall B are absent') is the contrary of E. E true makes A false."),
            S("Subalternation", text="E is true, so its subaltern O ('Some candidates in Hall B are not absent') is true."),
            S("Result", text="A false, E true, O true. This matches the row 'I is false' in Table 1."),
        ]),
        H("Eductions: conversion, obversion, contraposition"),
        T("An **eduction** (or *equivalent or implied inference*) rewrites a proposition so that it keeps its truth as far as the logic allows. The three to master:"),
        D("**Conversion** interchanges subject and predicate. It is valid *simply* (the converse has the same form) for E and I. For A it is valid only *per accidens* (by limitation): 'All S are P' gives 'Some P are S'. For O there is no valid conversion.", title="Conversion"),
        D("**Obversion** changes the quality of the proposition and replaces the predicate by its complement (non-P), keeping the subject. It is valid for all four forms: "
          "A to E, E to A, I to O, O to I.", title="Obversion"),
        D("**Contraposition** replaces the subject by the complement of the predicate and the predicate by the complement of the subject. It is valid simply for A and O, per accidens for E, and not at all for I. "
          "It can be done by obverting, converting, then obverting again.", title="Contraposition"),
        CODE("Original            Converse              Obverse               Contrapositive\n"
             "A All S are P      Some P are S (pa)     No S are non-P        All non-P are non-S\n"
             "E No S are P       No P are S            All S are non-P       Some non-P are not non-S (pa)\n"
             "I Some S are P     Some P are S          Some S are not non-P  none\n"
             "O Some S are not P none                  Some S are non-P      Some non-P are not non-S\n"
             "(pa) = per accidens: a weaker form is obtained", "text", title="Table 2. Eductions of A, E, I and O"),
        T("The complement of a class is everything outside it: non-P. Complementary classes together fill the whole universe of discourse and do not overlap. The report on the Board's 2023 examination shows items asking for the name of the process (for example, 'S is P' becoming 'non-P is non-S' is contraposition), so recognise the processes by their pattern as well as use them."),
        KEY("Inversion", "A fourth, less common eduction.", cards=[
            ["What it is", "Inversion gives a conclusion whose subject is the complement of the original subject. Applied to A it gives 'Some non-S are not P'; applied to E it gives 'Some non-S are P'."],
            ["How it is built", "Repeated obversion and conversion. It needs a particular conclusion and the assumption that non-S has members, so it is valid only on the traditional view. Many courses leave it out; check your textbook."],
        ]),
        EX("Worked example 2: a chain of eductions", intro="Starting from 'All trained nurses are registered persons' (A: S = trained nurses, P = registered persons) find its obverse, converse and contrapositive.", steps=[
            S("Obverse", text="Change quality, complement the predicate: 'No trained nurses are non-registered persons.' (E)"),
            S("Converse", text="Interchange the terms; A converts only per accidens: 'Some registered persons are trained nurses.' (I) A simple converse 'All registered persons are trained nurses' would be a fallacy."),
            S("Contrapositive", text="Complement and interchange: 'All non-registered persons are non-trained-nurses.' (A) This is equivalent to the original."),
            S("Check by reasoning", text="Anyone outside the registered class cannot be a trained nurse, since every trained nurse is inside it. The contrapositive is just that sentence."),
        ]),
        MISTAKE("Converting A simply, or contraposing I", "'All dogs are mammals' does not mean 'All mammals are dogs'. And 'Some students are girls' has no valid contrapositive: from 'Some non-girls are not students' nothing follows. When you see I, use conversion and obversion only; when you see O, use obversion and contraposition only."),
        QUIZ("If 'All tailors in the market are women' is false, which of the following must be true?", ["No tailors in the market are women", "Some tailors in the market are not women", "Some tailors in the market are women", "All women in the market are tailors"], 1,
             "The contradictory of A is O. A false means O is true: at least one tailor in the market is not a woman. E (option A) is only the contrary: it may be false too.",
             hint="Which form is the contradictory of A?",
             feedback=["E is the contrary of A: both can be false, so E is not forced.", "", "I is the subaltern of A; if A is false, I is undetermined.", "This reverses the terms and is not related by the square."]),
        QUIZ("The obverse of 'No teachers are idle persons' is", ["No idle persons are teachers", "All teachers are non-idle persons", "Some teachers are idle persons", "All non-teachers are idle persons"], 1,
             "Obversion changes quality and complements the predicate: E becomes A and 'idle' becomes 'non-idle'. Option A is the converse.",
             hint="Which two things change in obversion?",
             feedback=["That is the converse (simple conversion of E).", "", "That is the contradictory of the original (I), not the obverse.", "This changes the subject; obversion keeps it."]),
        PQ("Practice question 1. Name the relation between the following pairs and say whether both can be true: (a) 'All birds fly' and 'Some birds do not fly'; (b) 'Some metals are liquid' and 'Some metals are not liquid'.",
           "(a) A and O are contradictories: they cannot both be true and cannot both be false. (b) I and O are subcontraries: both can be true (and are, in fact: mercury is liquid; iron is not), but they cannot both be false."),
        PQ("Practice question 2. Obvert and convert 'Some candidates are late.' State the form of each result and say whether it is valid.",
           "Obverse: 'Some candidates are not non-late persons' (O), valid (obversion works for all forms). Converse: 'Some late persons are candidates' (I), valid by simple conversion."),
        PQ("Practice question 3. Give the contrapositive of 'No selfish person is a good leader' and say what kind of contraposition it is.",
           "Contraposition of E is valid only per accidens. Work in steps with S = selfish persons, P = good leaders. Obvert: 'All selfish persons are non-good-leaders.' (A) Convert per accidens: 'Some non-good-leaders are selfish persons.' (I) Obvert: 'Some non-good-leaders are not non-selfish persons.' (O) That is the contrapositive: valid, but weaker than the original."),
        SUM("The square gives: A and O contradictories, E and I contradictories, A and E contraries, I and O subcontraries, A to I and E to O by subalternation.",
            "On the Boolean view universal propositions have no existential import, so only the contradictories survive; the traditional square needs non-empty terms.",
            "Conversion is valid simply for E and I, per accidens for A, and not for O. Obversion is valid for all four. Contraposition is valid simply for A and O, per accidens for E, and not for I.",
            "The contradictory of A is O, never E. Never convert A simply or contrapose I."),
        TIP("Exam link: Paper 1 (multiple choice) regularly names an eduction from its pattern or asks which oppositional relation holds. In Paper 3, set out the steps (obvert, convert, obvert) so each step can be credited."),
    ],
))

# ---------------------------------------------------------------- M4.3 The categorical syllogism
LESSONS.append(lesson(
    module=M4,
    topic="The categorical syllogism",
    title="The categorical syllogism: figures, moods, rules and Venn diagrams",
    slug="psl2-categorical-syllogism",
    minutes=25,
    summary="A categorical syllogism has three categorical propositions and three terms. Its mood and figure are read off, the five rules and the named fallacies test it, and Venn diagrams check it; enthymemes and sorites are shortened or chained syllogisms.",
    objectives=[
        "Identify the major, minor and middle terms, the mood and the figure of a syllogism",
        "Apply the rules of the syllogism and name the fallacy committed when one is broken",
        "Test validity with a three-circle Venn diagram",
        "Recognise an enthymeme (and its order) and a sorites",
    ],
    key_concepts=["Major term", "Minor term", "Middle term", "Mood", "Figure", "Undistributed middle", "Illicit process", "Venn diagram", "Enthymeme", "Sorites"],
    blocks=[
        H("Introduction: two premises, one conclusion"),
        T("In a market in Mbouda you hear: all traders in the market pay the council tax; Ngu is a trader in the market; so Ngu pays the council tax. "
          "This is a **categorical syllogism**: a deductive argument made of exactly three categorical propositions (two premises and a conclusion) containing exactly three terms, each appearing twice."),
        D("The **minor term** (S) is the subject of the conclusion. The **major term** (P) is the predicate of the conclusion. The **middle term** (M) occurs in both premises but not in the conclusion; it links the other two. "
          "The **major premise** contains the major term and the **minor premise** the minor term. In standard form the major premise is written first.", title="Terms and premises"),
        T("In the example: conclusion 'Ngu pays the council tax' gives S = Ngu (the traders' class of one), P = persons who pay the council tax. M = traders in the market. "
          "Major premise: All M are P. Minor premise: All S are M (taking Ngu as a one-member class). Conclusion: All S are P."),
        H("Mood and figure"),
        D("The **mood** is the three letters (A, E, I, O) of the major premise, minor premise and conclusion in order, for example AAA or EIO. "
          "The **figure** is fixed by the position of the middle term in the premises. There are four figures and 4 x 4 x 4 x 4 = 256 forms.", title="Mood and figure"),
        CODE("Figure 1     Figure 2     Figure 3     Figure 4\n"
             "M - P        P - M        M - P        P - M\n"
             "S - M        S - M        M - S        M - S\n"
             "S - P        S - P        S - P        S - P", "text", title="Table 1. The four figures (subject - predicate in each premise)"),
        T("Method: (1) find the conclusion; (2) pick out S and P; (3) the other term is M; (4) write the major premise first; (5) put each statement in standard form and note A, E, I or O; (6) read the mood and figure. "
          "For the market example the mood is AAA and the figure is 1: AAA-1."),
        H("The rules of the syllogism"),
        KEY("Five rules (traditional version)", "Break one and the argument is invalid. Each broken rule has a name.", cards=[
            ["1. Three terms only", "Each used in the same sense. Breaking it by using a word in two senses is the fallacy of four terms (equivocation)."],
            ["2. The middle term is distributed at least once", "Otherwise the premises may talk about different parts of the middle class. Fallacy: undistributed middle."],
            ["3. A term distributed in the conclusion is distributed in its premise", "Fallacy: illicit major (P) or illicit minor (S): the conclusion says more than the premise did."],
            ["4. No two negative premises", "Fallacy: exclusive premises. Two exclusions do not link S to P."],
            ["5. A negative premise if and only if a negative conclusion", "Negative conclusion from two affirmative premises, or affirmative conclusion from a negative premise, is invalid."],
        ]),
        T("A related rule: two particular premises prove nothing (it follows from rules 2 to 5). "
          "On the modern view one more rule is added: two universal premises cannot give a particular conclusion (the *existential fallacy*), because universal propositions are then not taken to claim that their classes have members. Check which version your textbook uses."),
        MISTAKE("Naming the fallacy without saying why", "The Board's 2023 report asks candidates to explain a fallacy in the context of the question rather than in general terms. Write: 'Illicit minor: *taxpayers* is distributed in the conclusion (subject of an A) but undistributed in the minor premise (predicate of an A).'"),
        EX("Worked example 1: a valid syllogism", intro="All teachers are graduates. Some women are teachers. Therefore some women are graduates. Test it.", steps=[
            S("Terms", text="Conclusion: Some women are graduates. S = women, P = graduates, M = teachers."),
            S("Form", text="Major: All M are P (A). Minor: Some S are M (I). Conclusion: Some S are P (I). Mood AII, figure 1 (M-P, S-M)."),
            S("Distribution", text="Middle M is the subject of the A premise: distributed. Conclusion I distributes nothing. No illicit process."),
            S("Quality", text="Both premises affirmative, conclusion affirmative. No exclusive premises. All rules are met."),
            S("Result", text="Valid. This form is called Darii."),
        ]),
        EX("Worked example 2: undistributed middle", intro="All bakers are early risers. All farmers are early risers. Therefore all farmers are bakers.", steps=[
            S("Terms", text="S = farmers, P = bakers, M = early risers. Major: All P are M. Minor: All S are M."),
            S("Form", text="AAA in figure 2 (P-M, S-M)."),
            S("Test", text="M is the predicate of both A premises, so it is distributed in neither. Rule 2 is broken."),
            S("Why it fails", text="The bakers and the farmers may be different groups of early risers. Overlap with the same large class tells us nothing about overlap with each other."),
        ]),
        EX("Worked example 3: illicit major and illicit minor", intro="(a) All dogs are mammals. No cat is a dog. Therefore no cat is a mammal. (b) All farmers are traders. All traders are taxpayers. Therefore all taxpayers are farmers.", steps=[
            S("(a) Terms and form", text="S = cats, P = mammals, M = dogs. AEE in figure 1."),
            S("(a) Test", text="P is the predicate of a negative conclusion, so P is distributed there. In the major premise (All dogs are mammals) mammals is the predicate of an A, undistributed. Illicit major."),
            S("(b) Terms and form", text="S = taxpayers, P = farmers, M = traders. Major: All P are M. Minor: All M are S. AAA in figure 4."),
            S("(b) Test", text="The conclusion distributes its subject, taxpayers. In the minor premise 'taxpayers' is the predicate of an A, undistributed. Illicit minor."),
        ]),
        H("Valid forms"),
        T("Computing all 256 forms for every possible way the three classes can overlap gives 24 forms that never lead from true premises to a false conclusion, **provided the three classes are not empty** (the traditional assumption). Their traditional Latin names are in Table 2; the vowels give the mood. "
          "Of these 24, only 15 stay valid if empty classes are allowed (the modern view). The other 9 (marked with an asterisk below) need the assumption that a class has members."),
        CODE("Figure 1: Barbara AAA, Celarent EAE, Darii AII, Ferio EIO, Barbari* AAI, Celaront* EAO\n"
             "Figure 2: Cesare EAE, Camestres AEE, Festino EIO, Baroco AOO, Cesaro* EAO, Camestrop* AEO\n"
             "Figure 3: Datisi AII, Disamis IAI, Ferison EIO, Bocardo OAO, Darapti* AAI, Felapton* EAO\n"
             "Figure 4: Camenes AEE, Dimaris IAI, Fresison EIO, Bramantip* AAI, Fesapo* EAO, Camenop* AEO\n"
             "* valid only if the classes involved are not empty", "text", title="Table 2. The 24 valid forms (check your textbook for the spelling of the names)"),
        KEY("What the rules test", "Each rule tests one thing.", cards=[
            ["Terms", "Three terms, no ambiguity."],
            ["Distribution", "Middle distributed once; nothing distributed in the conclusion that was not in the premises."],
            ["Quality", "No two negative premises; negative conclusion exactly when there is a negative premise."],
        ]),
        H("Testing with Venn diagrams"),
        T("A **Venn diagram** for a syllogism uses three overlapping circles S, P and M, giving eight regions. The method: (1) draw the premises only, universal premise first; (2) for a universal proposition, shade the region(s) it says are empty; (3) for a particular proposition, put an X in the region it says is occupied (on a line if the premise does not settle which of two regions); (4) without drawing the conclusion, look to see whether it is already shown. "
          "If it is, the syllogism is valid. The Venn method tests validity on the modern (Boolean) view, so it confirms 15 forms; for the 9 conditional forms it shows the conclusion only if you add the assumption that a class is non-empty."),
        IMG("alpsl2-venn-barbara.svg", alt="Three-circle Venn diagram for All M are P and All S are M: the part of M outside P and the part of S outside M are shaded; the part of S outside P is therefore shaded too.",
            caption="Figure 1. Barbara (AAA-1). After shading the two premises, the whole region of S outside P is empty: All S are P."),
        EX("Worked example 4: Venn test of Darii", intro="All M are P. Some S are M. Therefore some S are P.", steps=[
            S("Universal premise first", text="All M are P: shade the part of M outside P (the regions M only, and S and M but not P)."),
            S("Particular premise", text="Some S are M: the X goes in the S-and-M overlap. Since the region S, M, not P is shaded, the X sits in the region S, M and P."),
            S("Read the conclusion", text="That region lies inside S and P: some S are P. The conclusion appears without being drawn. Valid."),
        ]),
        H("Shortened and chained syllogisms"),
        D("An **enthymeme** is a syllogism stated with one proposition suppressed because it is obvious. It is of the **first order** if the major premise is missing, **second order** if the minor premise is missing, and **third order** if the conclusion is missing. "
          "To test it, supply the missing proposition and test the full syllogism.", title="Enthymeme"),
        T("'All humans are fallible and all bishops are human' has no conclusion: third order. The full argument is: All humans are fallible; all bishops are human; so all bishops are fallible. "
          "'Ngu is a trader, so he pays the council tax' omits the major premise (All traders pay the council tax): first order."),
        D("A **sorites** is a chain of syllogisms in which the intermediate conclusions are omitted and only the premises and the final conclusion are stated: All A are B; all B are C; all C are D; so all A are D. "
          "In the Aristotelian form each premise's predicate is the next premise's subject; only the first premise may be particular and only the last may be negative. The Goclenian form reverses the order. "
          "The classification of a sorites by 'figure' differs between books (the Board's 2023 report treats the apparent figure as the figure): check your textbook.", title="Sorites"),
        QUIZ("The fallacy in 'All dogs are animals; all cats are animals; so all cats are dogs' is", ["Illicit minor", "Undistributed middle", "Exclusive premises", "Four terms"], 1,
             "The middle term 'animals' is the predicate of two A propositions and so is distributed in neither.",
             hint="Where does 'animals' stand in each premise?",
             feedback=["The minor term 'cats' is distributed in the conclusion and in the minor premise (subject of A), so there is no illicit minor.", "", "Both premises are affirmative.", "There are three terms: dogs, cats, animals."]),
        QUIZ("A syllogism has the middle term as the predicate of the major premise and the subject of the minor premise. Its figure is", ["Figure 1", "Figure 2", "Figure 3", "Figure 4"], 3,
             "Figure 4 is P-M, M-S: the middle is predicate of the major and subject of the minor.",
             hint="Write the two premises as _ - M and M - _.",
             feedback=["Figure 1 has M as subject of the major and predicate of the minor.", "Figure 2 has M as predicate in both.", "Figure 3 has M as subject in both.", ""]),
        PQ("Practice question 1. Identify the mood and figure, and test: 'No reptiles are mammals. All snakes are reptiles. So no snakes are mammals.'",
           "Conclusion: No snakes are mammals, S = snakes, P = mammals. M = reptiles. Major: No M are P (E). Minor: All S are M (A). Conclusion E. Mood EAE, figure 1 (M-P, S-M): Celarent. Test: M is distributed in the E major; the conclusion's distributed terms (snakes, mammals) are distributed in the premises (snakes as subject of A, mammals as predicate of E). One negative premise, negative conclusion. Valid."),
        PQ("Practice question 2. Test: 'Some farmers are rich. Some rich people are traders. So some farmers are traders.'",
           "S = farmers, P = traders, M = rich people. Both premises are particular (I), and I distributes no term, so M is undistributed in both premises: undistributed middle. Two particular premises prove nothing. Invalid, whatever the facts about farmers and traders. (Form III-1.)"),
        PQ("Practice question 3. Put in standard form and test: 'Every student of the school is a candidate, because all students of the school are persons who registered, and all persons who registered are candidates.'",
           "Conclusion: All students are candidates (S = students, P = candidates). M = persons who registered. Major: All M are P (All persons who registered are candidates). Minor: All S are M. Mood AAA, figure 1: Barbara. M is distributed (subject of the major), and the conclusion distributes only S, which is distributed in the minor premise. Valid."),
        SUM("A categorical syllogism has three terms (minor S, major P, middle M) and three propositions; mood is the letters, figure is the position of M.",
            "The rules: three terms; middle distributed once; no term distributed in the conclusion unless in a premise; no two negative premises; negative conclusion iff negative premise.",
            "Broken rules give named fallacies: four terms, undistributed middle, illicit major or minor, exclusive premises, affirmative/negative mismatch. Name the fallacy and show where it occurs in the argument.",
            "24 forms are valid if classes are non-empty, 15 if empty classes are allowed; Venn diagrams test the modern view.",
            "An enthymeme omits one proposition (first, second or third order); a sorites chains syllogisms."),
        TIP("Exam link: the Board's Paper 1 includes syllogism items (identifying fallacies, the order of an enthymeme, the figure of a sorites) and Paper 3 logic problems ask for tests of validity. Break the work into parts: terms, form, rules, verdict."),
    ],
))

# ---------------------------------------------------------------- M4.4 Hypothetical, disjunctive syllogisms, dilemmas
LESSONS.append(lesson(
    module=M4,
    topic="Hypothetical and disjunctive syllogisms and dilemmas",
    title="Hypothetical and disjunctive syllogisms, and the dilemma",
    slug="psl2-hypothetical-disjunctive-dilemma",
    minutes=24,
    summary="Conditional (hypothetical) and either-or (disjunctive) arguments have two valid forms each and two classic fallacies. A dilemma combines them, and can be met by grasping the horns, escaping between them or rebutting it.",
    objectives=[
        "Name the parts of a conditional proposition and state its valid and invalid inference patterns",
        "Test a disjunctive syllogism, noting the difference between inclusive and exclusive 'or'",
        "Identify the kinds of dilemma (simple or complex, constructive or destructive)",
        "Answer a dilemma by grasping the horns, escaping between the horns or rebutting it",
    ],
    key_concepts=["Antecedent and consequent", "Modus ponens", "Modus tollens", "Affirming the consequent", "Denying the antecedent", "Disjunctive syllogism", "Dilemma", "Horns", "Rebuttal"],
    blocks=[
        H("Introduction: arguments that are not about classes"),
        T("The syllogisms of the last lesson were about classes: all, no, some. Many everyday arguments are about *statements*. 'If it rains, the match will be cancelled' joins two statements. 'Either the bus is late or the driver is lost' offers alternatives. "
          "These arguments are the traditional counterpart of propositional logic and are tested by the same ideas: validity as the impossibility of true premises with a false conclusion."),
        H("Hypothetical (conditional) syllogisms"),
        D("A **conditional** (hypothetical) proposition has the form 'If A then B'. A is the **antecedent** (the condition) and B is the **consequent**. "
          "The proposition says that A cannot be true without B being true: A is *sufficient* for B and B is *necessary* for A. 'A only if B' says the same as 'If A then B'.", title="Conditional proposition"),
        T("A **mixed hypothetical syllogism** has a conditional as major premise and a categorical (plain) statement as minor premise. Only two forms are valid."),
        KEY("Two valid forms and two fallacies", "Remember: affirm the antecedent, deny the consequent.", cards=[
            ["Modus ponens (valid)", "If A then B. A. Therefore B."],
            ["Modus tollens (valid)", "If A then B. Not B. Therefore not A."],
            ["Affirming the consequent (invalid)", "If A then B. B. Therefore A."],
            ["Denying the antecedent (invalid)", "If A then B. Not A. Therefore not B."],
        ]),
        T("Why the fallacies fail: 'If it rains, the road is wet. The road is wet. Therefore it rained.' A water tank truck may have wet the road; rain is *sufficient* for a wet road, not *necessary*. "
          "'If Ada studies, she passes. She did not study. So she did not pass.' She may have passed through earlier knowledge: studying is sufficient, not necessary. "
          "Both mistakes confuse necessary and sufficient conditions, and the Board's 2023 report notes the same confusion in an item on a false-cause argument."),
        D("A **pure hypothetical syllogism** has conditionals for both premises and the conclusion: If A then B. If B then C. Therefore if A then C. It is valid (the chain rule).", title="Pure hypothetical syllogism"),
        EX("Worked example 1: testing a conditional argument", intro="(a) If the generator is working, the freezer is cold. The freezer is not cold. (b) If the generator is working, the freezer is cold. The freezer is cold. What can be concluded in each case?", steps=[
            S("(a) Form", text="If A then B; not B. This is modus tollens: valid. Conclusion: the generator is not working."),
            S("(a) Why", text="If the generator were working the freezer would be cold. It is not cold, so the generator cannot be working."),
            S("(b) Form", text="If A then B; B. This is affirming the consequent: invalid. Nothing follows. The freezer may be cold because of a charcoal ice box, or because the power supply is from the grid."),
            S("Test", text="To prove an argument invalid, give a case where the premises are true and the conclusion false: freezer cold, generator off, powered by the grid."),
        ]),
        H("Disjunctive syllogisms"),
        D("A **disjunctive** proposition has the form 'Either A or B'; A and B are the **alternatives** or disjuncts. "
          "In the **inclusive** sense 'or' allows both to be true; in the **exclusive** sense it says exactly one is true. "
          "The **disjunctive syllogism** (modus tollendo ponens) denies one alternative to affirm the other: Either A or B. Not A. Therefore B.", title="Disjunctive proposition"),
        T("If the disjunction is inclusive, only the forms that deny a disjunct are valid. 'Either the exam was difficult or the candidates were lazy. The exam was not difficult. So the candidates were lazy.' is valid. "
          "'Affirming a disjunct' (Either A or B. A. Therefore not B.) is valid only if the disjunction is exclusive, so the argument depends on what 'or' means. Say which reading you adopt."),
        MISTAKE("Treating every 'or' as exclusive", "'Either you pay the fee or you stay out' is naturally exclusive; 'Either the shop is closed or the owner is ill' is inclusive: both might be true. Wrongly assuming exclusive 'or' turns an invalid argument into a valid-looking one."),
        QUIZ("If the street is flooded, the buses do not run. The buses do run. What follows?", ["The street is not flooded", "The street is flooded", "The buses will run tomorrow", "Nothing follows"], 0,
             "Modus tollens: from 'If A then B' and 'not B' (the buses do run, so it is false that they do not) we conclude 'not A'.",
             hint="Which part of the conditional is denied?",
             feedback=["", "This contradicts the valid inference.", "Nothing about tomorrow follows from the premises.", "This would be true only for the fallacy forms; here modus tollens applies."]),
        H("The dilemma"),
        D("A **dilemma** is an argument with a conditional (or two) as major premise and a disjunctive minor premise that offers a choice between alternatives (the **horns**), each leading to an unwelcome (or welcome) result. "
          "**Constructive** dilemmas affirm the antecedents; **destructive** ones deny the consequents. **Simple** ones have the same consequent (or same antecedent); **complex** ones have different ones.", title="Dilemma"),
        CODE("Simple constructive:    If A then C. If B then C. Either A or B.        So C.\n"
             "Complex constructive:   If A then C. If B then D. Either A or B.        So either C or D.\n"
             "Complex destructive:    If A then C. If B then D. Either not C or not D. So either not A or not B.", "text", title="Table 1. Forms of the dilemma"),
        EX("Worked example 2: a dilemma and its three answers", intro="'If the council raises market fees, the traders will be angry. If it keeps the fees, the market will lack money for repairs. It must either raise or keep the fees. So either the traders will be angry or the market will lack money for repairs.'", steps=[
            S("Form", text="Complex constructive dilemma: two different consequents, the alternatives 'raise' and 'keep' are the horns. The form is valid."),
            S("Grasp the horns", text="Deny one conditional premise: 'If fees rise by a small, announced amount, the traders will not be angry'. We deny the first horn, so its consequent is not forced."),
            S("Escape between the horns", text="Deny that the alternatives are exhaustive: the council can raise some fees, cut costs and seek other income. Then the disjunction 'raise or keep' is false."),
            S("Rebut by a counter-dilemma", text="Offer another valid dilemma with the same alternatives: 'If it raises fees, the market will have money for repairs; if it keeps them, the traders will be content. It raises or keeps. So either the market has money for repairs or the traders are content.' It does not refute the first but shows it is not decisive."),
        ]),
        T("A valid dilemma can have a false conclusion if a premise is false. To criticise a dilemma, attack a premise (a conditional or the disjunction); you cannot attack the form. The Board's 2023 report has an item on exactly this: the response that denies the conditional premise (the first premise) is called grasping the horns."),
        MISTAKE("Calling every false-choice argument a dilemma", "A true dilemma has a form: conditionals plus a disjunction. 'Either you are with us or against us' is only a disjunction (a false dichotomy when other options exist). Check for the conditionals before naming it."),
        QUIZ("The reply to a dilemma that denies that the alternatives in the disjunctive premise are exhaustive is called", ["Grasping the horns", "Escaping between the horns", "Rebutting the dilemma", "Affirming the consequent"], 1,
             "Escaping between the horns shows that there is a third possibility, so the disjunction is false.",
             hint="Which premise do we attack?",
             feedback=["Grasping the horns denies a conditional premise.", "", "A rebuttal offers a counter-dilemma, it does not attack the disjunction.", "That is an invalid argument form, not an answer to a dilemma."]),
        PQ("Practice question 1. State the form (and say whether it is valid): 'If the tank is full, the pump works. The tank is not full. So the pump does not work.'",
           "Form: If A then B; not A; therefore not B. This is denying the antecedent, an invalid form. The pump may work for other reasons (for example, a partly filled tank). A counterexample: tank half full, pump working."),
        PQ("Practice question 2. Draw a valid conclusion if possible: 'Either Ngu is in Bamenda or he is in Bafoussam. He is not in Bafoussam.' What if instead the minor premise were 'He is in Bamenda'?",
           "First case: disjunctive syllogism denying an alternative: Ngu is in Bamenda. Second case: 'He is in Bamenda' affirms an alternative. If 'or' is exclusive (he cannot be in both places) we may conclude he is not in Bafoussam; if inclusive we cannot. Here the exclusive reading is natural, since one cannot be in two towns at once."),
        PQ("Practice question 3. A student argues: 'If I read the novel, I lose a night's sleep. If I do not read it, I fail the test. I either read it or not. So I lose a night's sleep or fail.' Name its form and give two ways to answer it.",
           "Complex constructive dilemma (valid in form). Its disjunction 'read it or do not read it' is exhaustive, so escaping between the horns is not available. Answers: (1) Grasp the horns: deny 'If I read the novel, I lose a night's sleep' by reading it over several afternoons. (2) Grasp the other horn: deny 'If I do not read it, I fail' by revising the other set texts well enough to pass. (3) Rebut: 'If I read it, I pass the test; if I do not, I keep my sleep; I read it or not; so I pass the test or keep my sleep.'"),
        SUM("Modus ponens (affirm the antecedent) and modus tollens (deny the consequent) are valid; affirming the consequent and denying the antecedent are invalid.",
            "A conditional makes its antecedent sufficient and its consequent necessary; 'A only if B' means 'If A then B'.",
            "A disjunctive syllogism denies one alternative to affirm the other; affirming an alternative is valid only for exclusive 'or'.",
            "A dilemma is a valid form (simple or complex, constructive or destructive); a dilemma is answered by grasping a horn, escaping between the horns or rebutting with a counter-dilemma.",
            "To show invalidity, give a counterexample: premises true, conclusion false."),
        TIP("Exam link: Paper 1 multiple choice includes items on the response to a dilemma and on the conclusion of a valid disjunctive syllogism; Paper 3 logic problems may ask you to name and answer a dilemma. Name the form, then answer the question asked."),
    ],
))

# ---------------------------------------------------------------- M4.5 Informal fallacies
LESSONS.append(lesson(
    module=M4,
    topic="Informal fallacies",
    title="Informal fallacies: relevance, presumption and ambiguity",
    slug="psl2-informal-fallacies",
    minutes=24,
    summary="An informal fallacy is a mistake in reasoning that depends on the content of the argument, not its form. The usual groups are fallacies of relevance, of presumption and of ambiguity; each must be named and explained in the context of the argument.",
    objectives=[
        "Distinguish formal from informal fallacies",
        "Recognise the main fallacies of relevance, presumption and ambiguity",
        "Explain why a given argument commits a fallacy, in the context of that argument",
        "Distinguish a fallacy from a legitimate use of a similar argument",
    ],
    key_concepts=["Formal and informal fallacy", "Ad hominem", "Appeal to authority", "Begging the question", "False cause", "Hasty generalisation", "Equivocation", "Composition and division", "Missing the point"],
    blocks=[
        H("Introduction: arguments that persuade but do not prove"),
        T("A radio caller says: 'Doctor Ngwa says this herbal drink cures all fevers, and he is a famous man, so it must be true.' Is that good reasoning? "
          "The syllogism rules of the last lessons catch errors of *form*. Many bad arguments have no wrong form but are still bad: they distract, assume what they should prove, or play on words. These are **informal fallacies**."),
        D("A **fallacy** is an error of reasoning that makes an argument defective although it may look convincing. A **formal fallacy** is detected from the form alone (affirming the consequent, undistributed middle). "
          "An **informal fallacy** depends on the content, the context or the wording of the argument, and cannot be found by looking at its form alone.", title="Formal and informal fallacy"),
        KEY("Three groups (a common classification)", "Textbooks group the fallacies in slightly different ways; this three-way scheme is widely used. Check your textbook's list.", cards=[
            ["Relevance", "The premises are not relevant to the conclusion, though they may stir feeling. Examples: attacking the person, threat, pity, popularity."],
            ["Presumption", "The argument assumes what has not been shown. Examples: begging the question, false cause, hasty generalisation, complex question, false dilemma."],
            ["Ambiguity", "A word or phrase shifts meaning inside the argument. Examples: equivocation, amphiboly, accent, composition, division."],
        ]),
        H("Fallacies of relevance"),
        KEY("Common fallacies of relevance", "In each, the premise has psychological pull but little logical force.", cards=[
            ["Argument against the person (ad hominem)", "Rejecting a claim by attacking the speaker's character (abusive), circumstances (circumstantial) or inconsistency (tu quoque) instead of the reasons. 'You cannot trust her plan; she failed her own exam.'"],
            ["Appeal to force (ad baculum)", "A threat in place of a reason: 'Support the proposal, or you will lose your place on the committee.'"],
            ["Appeal to pity (ad misericordiam)", "Using sympathy as proof: 'Give me a pass mark; I have had a hard year.' (Pity may matter morally but does not show the answers were right.)"],
            ["Appeal to the people (ad populum)", "Popularity as proof: 'Everyone in the neighbourhood buys this brand, so it is the best.'"],
            ["Appeal to authority (ad verecundiam)", "Citing an authority outside his field, or one who is disputed or anonymous. Citing an expert within the expert's field is a legitimate argument that can be strong."],
            ["Appeal to ignorance (ad ignorantiam)", "'No one has proved the village well is safe, so it is dangerous' (or 'no one has proved it dangerous, so it is safe'). Lack of proof is not proof of the opposite."],
            ["Missing the point (irrelevant conclusion)", "Premises that support a different conclusion from the one drawn. A red herring drags in a side issue. A straw man attacks a weakened version of the opponent's view."],
        ]),
        MISTAKE("Calling every personal remark ad hominem", "Pointing out that a witness has a financial stake in the case is not always a fallacy: it may be a good reason to examine his claims more carefully. It is a fallacy only when it is used to say the claim is *false* without examining the reasons."),
        H("Fallacies of presumption"),
        KEY("Common fallacies of presumption", "The argument slips in a claim that needs proof.", cards=[
            ["Begging the question (petitio principii)", "The conclusion is assumed in a premise, perhaps in other words. 'The captain is right, because what the captain says is always correct.'"],
            ["Complex question", "A question that carries an unproved assumption: 'Have you stopped copying in tests?' Any yes or no answer admits the assumption."],
            ["False cause", "Treating something as a cause without showing a real causal link. 'Post hoc ergo propter hoc': B followed A, so A caused B. Another form treats a necessary condition (or a mere correlation) as the sufficient cause."],
            ["Hasty generalisation (converse accident)", "Drawing a general rule from too few or atypical cases: 'Two taxis were late, so all taxis in this town are late.'"],
            ["Accident", "Applying a general rule to a case it was not meant for: 'Everyone should be free to travel, so the prisoner must be allowed to go.'"],
            ["False dilemma (bifurcation)", "Offering two options as if there were no others: 'Either we build the road or the village will die.'"],
        ]),
        H("Fallacies of ambiguity"),
        KEY("Common fallacies of ambiguity", "The meaning shifts, or the grammar allows more than one reading.", cards=[
            ["Equivocation", "A key word is used in two senses. 'A good thief is good at stealing; so a good thief is good.'"],
            ["Amphiboly", "A badly built sentence has two readings and the argument uses the unintended one: 'The bus will pass the market in the morning.' ('Pass' as 'go beyond' or 'cross'.)"],
            ["Accent", "A change of emphasis changes the meaning: 'We should not speak ill of our friends' read as 'of our *friends*' (so enemies are fair game)."],
            ["Composition", "Reasoning from the parts to the whole: 'Each player in the team is excellent, so the team is excellent.' (The team may not play together well.)"],
            ["Division", "Reasoning from the whole to the parts: 'The school is large, so each classroom is large.'"],
        ]),
        T("Composition and division are close to the ideas of collective and distributive use of terms, met in the first lesson of this module."),
        H("A method for naming a fallacy"),
        KEY("Five steps", "Do these in order.", cards=[
            ["1. Restate", "Write the premises and the conclusion in your own words."],
            ["2. Relevance", "Do the premises bear on the truth of the conclusion?"],
            ["3. Presumption", "Is something assumed that needs proof, including the conclusion itself?"],
            ["4. Ambiguity", "Does any word or phrase shift its meaning?"],
            ["5. Name and explain", "Give the fallacy's name and show where it occurs in this argument."],
        ]),
        EX("Worked example 1: relevance", intro="'The councillor who proposes the school-fees reduction once paid his own children's fees late, so his proposal is worthless.' Name the fallacy and explain.", steps=[
            S("Restate", text="Premise: the proposer once paid late. Conclusion: his proposal is worthless."),
            S("Relevance", text="The premise concerns the proposer's conduct, not the merits of the proposal."),
            S("Name", text="Argument against the person (ad hominem, circumstantial or abusive)."),
            S("Explain in context", text="Whether fees should be reduced depends on costs, schools and families, not on how the proposer paid his own fees years ago."),
        ]),
        EX("Worked example 2: presumption", intro="'Every time Ada wears her blue scarf to the test, she passes; so the scarf makes her pass.' Name the fallacy and explain.", steps=[
            S("Restate", text="Premise: passes followed the scarf. Conclusion: the scarf causes passing."),
            S("Presumption", text="A real link is assumed from mere succession."),
            S("Name", text="False cause (post hoc ergo propter hoc)."),
            S("Explain in context", text="She may pass because she studies on those weeks. Showing a cause needs a mechanism, or a comparison of tests with and without the scarf."),
        ]),
        EX("Worked example 3: ambiguity", intro="'Nothing is better than good health. A cold drink is better than nothing. Therefore a cold drink is better than good health.' Name the fallacy.", steps=[
            S("Check the key term", text="'Nothing' means 'no thing at all' in the first premise ('there is no thing better') and 'the absence of anything' in the second."),
            S("Name", text="Equivocation (the ambiguity also gives the argument four terms, a formal fault)."),
            S("Explain in context", text="The conclusion follows only if 'nothing' has one meaning throughout. Read consistently, either the second premise is trivial or the conclusion does not follow."),
        ]),
        QUIZ("'Many people are buying this phone, so it must be the best phone.' The fallacy is", ["Ad hominem", "Ad populum (appeal to the people)", "False cause", "Equivocation"], 1,
             "Popularity (the number of buyers) is offered as proof of quality. The premise is not relevant to the truth of the conclusion.",
             hint="What is the reason being offered?",
             feedback=["No person is being attacked.", "", "No causal claim is made about what produced anything.", "No word changes its meaning."]),
        QUIZ("'Each of the players is excellent, so the team is excellent.' This is", ["Division", "Composition", "Amphiboly", "Begging the question"], 1,
             "Composition: what is true of the parts is wrongly said to be true of the whole.",
             hint="Are we moving from parts to the whole, or from the whole to the parts?",
             feedback=["Division goes from the whole to the parts.", "", "Amphiboly needs a sentence that can be read two ways.", "The conclusion is not simply a restatement of the premise."]),
        PQ("Practice question 1. Name the fallacy and explain it in context: 'We should reject the proposal to extend the school day because it comes from the principal who always wants more control.'",
           "Argument against the person (ad hominem, abusive or circumstantial). The principal's motives are not the evidence on the length of the school day. The proposal should be examined on its reasons (learning time, transport, rest)."),
        PQ("Practice question 2. 'No one has proved there are no ghosts in the old house, so there must be ghosts.' Name the fallacy and say what follows if the argument is reversed.",
           "Appeal to ignorance (ad ignorantiam). Failure to prove 'no ghosts' is not proof of ghosts. The reverse argument ('No one has proved there are ghosts, so there are none') is the same fallacy: ignorance cannot establish either side."),
        PQ("Practice question 3. Name the fallacy and explain it in context: 'Either you support the new bridge or you want the town to stay poor.'",
           "False dilemma (bifurcation, or false alternatives). The argument presents two options as if there were no others. A person may support other ways to develop the town (roads, water, schools), or doubt the bridge's cost, without wanting poverty. The disjunction is not exhaustive."),
        SUM("An informal fallacy is a flaw in content, context or wording, not in form.",
            "The common groups are relevance (attacking the person, force, pity, the crowd, authority, ignorance, missing the point), presumption (begging the question, complex question, false cause, hasty generalisation, false dilemma) and ambiguity (equivocation, amphiboly, accent, composition, division).",
            "The same pattern can be legitimate: an expert within his field, or a doubt about a witness with a stake, may be a good reason.",
            "Name the fallacy and explain where it occurs in the given argument. The Board's report asks for the explanation in context, not in generalities."),
        TIP("Exam link: the Board's Paper 1 includes items that name a fallacy in a short argument (for example the confusion between a necessary condition and a sufficient cause), and Paper 3 logic problems ask you to explain a fallacy in the context of the argument."),
    ],
))

# ---------------------------------------------------------------- M5.1 Propositional variables and connectives
LESSONS.append(lesson(
    module=M5,
    topic="Propositional variables and connectives",
    title="Propositional variables and the five truth-functional connectives",
    slug="psl2-variables-connectives",
    minutes=23,
    summary="Propositional logic abbreviates whole statements by letters and joins them with five truth-functional connectives: not, and, or, if-then and if-and-only-if. Symbolising begins with a paraphrase that makes the logical form clear.",
    objectives=[
        "Distinguish simple from compound statements and explain truth-functionality",
        "State the truth conditions of ~, · (and), v (or), ⊃ (if ... then) and ≡ (if and only if)",
        "Symbolise English sentences, including 'only if', 'unless', 'neither ... nor' and 'not both'",
        "Identify the main connective of a compound formula and read brackets correctly",
    ],
    key_concepts=["Statement", "Simple and compound", "Truth-functional connective", "Negation", "Conjunction", "Disjunction", "Conditional", "Biconditional", "Main connective", "Paraphrase"],
    blocks=[
        H("Introduction: from classes to statements"),
        T("Traditional logic looks inside statements at their subject and predicate terms. **Propositional logic** (also called propositional calculus or sentential logic) works at a coarser level: it treats a whole statement as a unit and studies how statements combine. "
          "'The market is open and the road is clear' is built from two statements joined by 'and'. To see its structure we give each statement a letter and each joining word a symbol."),
        D("A **statement** (proposition) is a sentence that is either true or false, not both. A **simple** statement contains no other statement as a part: 'Ada is a nurse.' "
          "A **compound** statement contains other statements joined by a connective or negated: 'Ada is a nurse and Ngu is a teacher.' "
          "A **propositional variable** (p, q, r, s ...) stands for any statement; a statement constant is a particular statement abbreviated by a letter (for example A: Ada is a nurse).", title="Statements and variables"),
        D("A connective is **truth-functional** when the truth value of the compound is completely fixed by the truth values of the parts. "
          "In propositional logic we use only such connectives, so a compound can be evaluated from its parts without asking what the statements are about.", title="Truth-functional"),
        H("The five connectives"),
        CODE("Name           Symbol   Reads                  Example\n"
             "Negation       ~        not                    ~p\n"
             "Conjunction    ·        and                    p · q   (some books write & or a dot)\n"
             "Disjunction    v        or (inclusive)         p v q\n"
             "Conditional    ⊃        if ... then            p ⊃ q\n"
             "Biconditional  ≡        if and only if         p ≡ q", "text", title="Table 1. Connectives and symbols (as listed in the blueprint; check your textbook for the symbol for 'and')"),
        T("The sign ⊃ is called the horseshoe and ≡ the triple bar. So p ⊃ q is 'if p then q' and p ≡ q is 'p if and only if q'."),
        CODE("p  ~p\n"
             "T  F\n"
             "F  T\n"
             "\n"
             "p  q  p . q  p v q  p ⊃ q  p ≡ q\n"
             "T  T    T      T      T      T\n"
             "T  F    F      T      F      F\n"
             "F  T    F      T      T      F\n"
             "F  F    F      F      T      T", "text", title="Table 2. Truth tables of the connectives (T = true, F = false)"),
        KEY("Reading the tables", "Learn these by meaning, not only by heart.", cards=[
            ["~p", "Reverses the truth value."],
            ["p · q", "True only when both are true."],
            ["p v q", "False only when both are false (inclusive 'or')."],
            ["p ⊃ q", "False only when p is true and q is false. A false antecedent makes the conditional true (it has not been broken)."],
            ["p ≡ q", "True when p and q have the same truth value."],
        ]),
        T("Why is ⊃ true when p is false? The conditional 'If the bridge is built, trade will rise' is not refuted by a world in which the bridge is never built. This material conditional is the only truth-functional reading, and it is sometimes odd: 'If Paris is in Brazil then the sea is dry' counts as true. Some English 'if' sentences carry more (a causal link) than the symbol ⊃ does. The symbol captures only the case of broken promise: true antecedent, false consequent."),
        MISTAKE("Reading p v q as 'exactly one of p, q'", "The sign v is inclusive: p v q is true when both are true. For 'exactly one' (exclusive or) write (p v q) · ~(p · q)."),
        H("Brackets and the main connective"),
        T("Brackets (or the dots used in older texts) show how to group. '~p · q' and '~(p · q)' are different: the first negates only p; the second negates the conjunction. "
          "In every compound formula there is one **main connective**, the last one applied when you build the formula from its parts. It decides the type of the whole statement. In ~(p · q) ⊃ r the main connective is ⊃, and the antecedent is the negation ~(p · q)."),
        EX("Worked example 1: finding the main connective", intro="Name the main connective of (a) ~(p v q), (b) ~p v q, (c) (p · q) ⊃ (r v s), (d) p ≡ (q · ~r).", steps=[
            S("(a)", text="The negation sign applies to the whole bracket: the main connective is ~ (a negation)."),
            S("(b)", text="~ applies only to p. The main connective is v: a disjunction of ~p and q."),
            S("(c)", text="The brackets separate two parts joined by ⊃: a conditional."),
            S("(d)", text="The biconditional joins p and the bracket: ≡ is the main connective."),
        ]),
        H("Symbolising English sentences"),
        T("The Board's 2023 report advises that symbolisation should start with a paraphrase, then build up in symbols. First dictionary (which letter means which statement), then paraphrase in 'if', 'and', 'or', 'not' language, then symbols."),
        CODE("English                              Symbolisation\n"
             "p and q; p but q; p although q       p . q\n"
             "p or q; either p or q                p v q\n"
             "not p; it is false that p            ~p\n"
             "if p then q; p implies q             p ⊃ q\n"
             "p only if q                          p ⊃ q\n"
             "p if q; p provided that q            q ⊃ p\n"
             "p if and only if q; p just in case q p ≡ q\n"
             "p unless q                           p v q  (or ~q ⊃ p)\n"
             "neither p nor q                      ~p . ~q  (or ~(p v q))\n"
             "not both p and q                     ~(p . q)\n"
             "p or q but not both                  (p v q) . ~(p . q)", "text", title="Table 3. Common translations"),
        KEY("Words that trap", "Watch these.", cards=[
            ["'Only if' and 'if'", "'p only if q' is p ⊃ q: q is necessary for p. 'p if q' is q ⊃ p: q is sufficient for p. Do not swap them."],
            ["'Neither ... nor'", "Both are false: ~p · ~q. It is not ~(p · q), which says only that they are not both true."],
            ["'Not both' and 'both not'", "~(p · q) allows one of them to be true. ~p · ~q allows neither."],
            ["'But', 'although', 'yet'", "Logically conjunctions. The symbol does not show the contrast in tone."],
        ]),
        EX("Worked example 2: symbolising", intro="Use R: it rains; F: the road floods; C: the match is cancelled. Symbolise (a) If it rains and the road floods, the match is cancelled. (b) The match is cancelled only if it rains. (c) Either the road floods or the match goes on, but not both.", steps=[
            S("(a) Paraphrase", text="If (it rains and the road floods) then the match is cancelled."),
            S("(a) Symbols", text="(R · F) ⊃ C. The main connective is ⊃."),
            S("(b) Symbols", text="'Only if' marks the necessary condition: C ⊃ R. Cancellation requires rain."),
            S("(c) Paraphrase and symbols", text="Let G: the match goes on. Either F or G, and not both: (F v G) · ~(F · G)."),
        ]),
        EX("Worked example 3: negations", intro="Symbolise (a) Neither Ada nor Ngu passed (A: Ada passed; N: Ngu passed). (b) Ada and Ngu did not both pass. (c) Ada passes unless she is ill (A: Ada passes; I: Ada is ill).", steps=[
            S("(a)", text="~A · ~N (or ~(A v N)). Both failed."),
            S("(b)", text="~(A · N). At least one failed; one may have passed."),
            S("(c)", text="'A unless I' is: if she is not ill then she passes: ~I ⊃ A, which is equivalent to A v I."),
            S("Why it matters", text="(a) and (b) differ: if Ada passed and Ngu failed, (b) is true and (a) is false."),
        ]),
        T("Compositionality: the meaning of a compound depends on the meanings of its parts and the connectives. A symbolisation fails when the sentence has structure that you ignored, for example 'Ada and Ngu are friends' where 'and' joins two names, not two statements: the sentence is simple (it cannot be split into 'Ada is a friend' and 'Ngu is a friend')."),
        QUIZ("Which is the correct symbolisation of 'Ada passes only if she studies' (P: Ada passes; S: Ada studies)?", ["S ⊃ P", "P ⊃ S", "P · S", "P ≡ S"], 1,
             "'Only if' marks a necessary condition: P ⊃ S. If she passes, then she has studied.",
             hint="Which condition is necessary for which?",
             feedback=["This says that studying guarantees passing, which is the 'if' reading.", "", "This says both are true, not a conditional.", "This says she passes exactly when she studies: stronger than 'only if'."]),
        QUIZ("The compound ~(p · q) is false when", ["p and q are both true", "p is true and q is false", "p is false and q is true", "p and q are both false"], 0,
             "p · q is true only when both are true; then its negation is false.",
             hint="When is p · q true?",
             feedback=["", "Then p · q is false and its negation is true.", "Then p · q is false and its negation is true.", "Then p · q is false and its negation is true."]),
        PQ("Practice question 1. Use S: Ngu studies; P: Ngu passes; L: Ngu is lucky. Symbolise 'If Ngu studies, he passes; and if he does not study, he passes only if he is lucky.'",
           "Paraphrase: (if S then P) and (if not S then (P only if L)). Symbols: (S ⊃ P) · (~S ⊃ (P ⊃ L)). The main connective is the dot."),
        PQ("Practice question 2. Name the main connective of ~(p ⊃ q) ≡ (p · ~q) and say how many different connectives appear.",
           "The main connective is ≡ (the biconditional), joining ~(p ⊃ q) and (p · ~q). Four connectives appear: ~, ⊃, · and ≡. (The two sides are equivalent: a conditional is false exactly when its antecedent is true and its consequent is false.)"),
        PQ("Practice question 3. Symbolise: 'The road is passable only if it has not rained or the drains are clear' (P: passable; R: it has rained; D: drains clear).",
           "Paraphrase: if the road is passable then (it has not rained or the drains are clear). Symbols: P ⊃ (~R v D). 'Only if' puts P in the antecedent."),
        SUM("A compound statement is built from simple ones by truth-functional connectives; the value of the compound depends only on the values of the parts.",
            "The five connectives are ~, · (and), v (inclusive or), ⊃ (if ... then) and ≡ (if and only if); ⊃ is false only when the antecedent is true and the consequent false.",
            "Symbolise in three steps: dictionary, paraphrase, symbols. Find the main connective with the brackets.",
            "'Only if' gives the conditional in the direction p ⊃ q; 'neither ... nor' is ~p · ~q; 'not both' is ~(p · q); 'unless' is v."),
        TIP("Exam link: the Board's 2023 report says symbolisation begins with paraphrase and analysis before building up in the symbols, and that the question's compositionality (how its parts combine) must be respected. Paper 1 asks for the correct symbolisation of an English sentence; Paper 3 asks for symbolisation with a stated dictionary."),
    ],
))

# ---------------------------------------------------------------- M5.2 Truth tables
LESSONS.append(lesson(
    module=M5,
    topic="Truth tables",
    title="Truth tables: building them and testing validity",
    slug="psl2-truth-tables",
    minutes=25,
    summary="A truth table lists every combination of truth values of the variables (2 to the power n rows) and computes a compound statement column by column. It tests validity directly, and a shorter indirect method looks for a counterexample.",
    objectives=[
        "Build a complete truth table in a standard row order for any formula of up to three variables",
        "Compute the columns of a compound statement from its main parts, working inside out",
        "Test an argument for validity by the full truth table and read off a counterexample if it is invalid",
        "Use the shorter (indirect) method of assuming the premises true and the conclusion false",
    ],
    key_concepts=["Truth table", "Rows 2 to the n", "Column by column", "Valid argument", "Counterexample row", "Indirect (short) method"],
    blocks=[
        H("Introduction: a decision procedure"),
        T("In traditional logic we tested syllogisms by rules and diagrams. In propositional logic we can do something more complete: for any argument we can write down every possible case and check them one by one. "
          "A **truth table** does exactly this. It is a *decision procedure*: it always settles whether an argument is valid, given enough rows and care."),
        H("Building a truth table"),
        D("For n propositional variables there are $2^n$ combinations of truth values, so the table has $2^n$ rows: 2 variables give 4, 3 give 8, 4 give 16. "
          "Write the variables on the left. In a standard order the first variable's column is half T and half F, the second alternates in quarters, and so on, ending with the last variable alternating T, F, T, F.", title="Rows of a truth table"),
        KEY("Method", "Five steps for any formula.", cards=[
            ["1. Count variables", "Write the variables (alphabetical order) and the $2^n$ rows."],
            ["2. Find the main connective", "That is the last column to compute."],
            ["3. List the parts", "Write the sub-formulas as column headings, from the smallest to the whole."],
            ["4. Compute column by column", "Use the connective tables from the last lesson, row by row. Check each column once before going on."],
            ["5. Read the answer", "The final column gives the truth value of the whole in each case."],
        ]),
        EX("Worked example 1: a compound with three variables", intro="Make the truth table of ~(p v q) ⊃ r.", steps=[
            S("Variables and rows", text="p, q, r: 8 rows."),
            S("Main connective", text="⊃, with antecedent ~(p v q) and consequent r. Columns: p v q, then ~(p v q), then the whole."),
        ]),
        CODE("p  q  r  p v q  ~(p v q)  ~(p v q) ⊃ r\n"
             "T  T  T  T      F         T\n"
             "T  T  F  T      F         T\n"
             "T  F  T  T      F         T\n"
             "T  F  F  T      F         T\n"
             "F  T  T  T      F         T\n"
             "F  T  F  T      F         T\n"
             "F  F  T  F      T         T\n"
             "F  F  F  F      T         F", "text", title="Table 1. Truth table of ~(p v q) ⊃ r"),
        T("The whole statement is false in exactly one row: p false, q false, r false (the antecedent is true and the consequent false). In all other rows it is true. A table with a mixture of T and F in the final column shows a *contingent* statement (next lesson)."),
        MISTAKE("Mixing up the row order, or leaving rows out", "A missing row means a missing case, and the verdict on validity may be wrong. Count the rows: 2, 4, 8 or 16. Always use the same order so you can compare tables."),
        H("Testing validity by truth table"),
        D("An argument is **valid** when there is no row of the truth table in which all the premises are true and the conclusion is false. "
          "A row with true premises and a false conclusion is a **counterexample row**; one such row makes the argument invalid.", title="Validity by truth table"),
        EX("Worked example 2: a valid argument", intro="Test: p ⊃ q; q ⊃ r; therefore p ⊃ r (the chain rule, from the last lesson).", steps=[
            S("Table", text="Columns for the two premises and the conclusion."),
        ]),
        CODE("p  q  r  p ⊃ q  q ⊃ r  p ⊃ r\n"
             "T  T  T  T      T      T\n"
             "T  T  F  T      F      F\n"
             "T  F  T  F      T      T\n"
             "T  F  F  F      T      F\n"
             "F  T  T  T      T      T\n"
             "F  T  F  T      F      T\n"
             "F  F  T  T      T      T\n"
             "F  F  F  T      T      T", "text", title="Table 2. Testing p ⊃ q, q ⊃ r therefore p ⊃ r"),
        T("Rows where both premises are true: rows 1, 5, 7 and 8. In each of them the conclusion is true. There is no counterexample row, so the argument is valid. "
          "Notice rows 2 and 4, where the conclusion is false: in each, at least one premise is also false. That is what validity means."),
        EX("Worked example 3: an invalid argument", intro="Test: p ⊃ q; q; therefore p (affirming the consequent).", steps=[
            S("Table", text="Two variables, 4 rows."),
        ]),
        CODE("p  q  p ⊃ q  q  p\n"
             "T  T  T      T  T\n"
             "T  F  F      F  T\n"
             "F  T  T      T  F    <- counterexample row\n"
             "F  F  T      F  F", "text", title="Table 3. Testing p ⊃ q, q therefore p"),
        T("In row 3 both premises are true (p ⊃ q and q) while the conclusion p is false. This one row shows the argument is invalid. If p is 'it rained' and q is 'the road is wet', the row is: it did not rain, but the road is wet (the water-truck case)."),
        H("The shorter (indirect) method"),
        T("A table for 5 variables has 32 rows. The **indirect method** (reductio-style test) tries to build only the counterexample: assume the conclusion false and all premises true, and see whether the values can be assigned without contradiction. "
          "If a contradiction is forced, no counterexample exists and the argument is valid; if the assignment succeeds, it is the counterexample and the argument is invalid."),
        EX("Worked example 4: indirect method, valid", intro="Test: (p ⊃ q) · (r ⊃ s); p v r; therefore q v s.", steps=[
            S("Assume the conclusion false", text="q v s false: so q is F and s is F."),
            S("First premise true", text="p ⊃ q true with q false forces p to be F. r ⊃ s true with s false forces r to be F."),
            S("Second premise", text="p v r with p and r both F is false. But we needed it true: contradiction."),
            S("Verdict", text="No counterexample can exist: the argument is valid (constructive dilemma)."),
        ]),
        EX("Worked example 5: indirect method, invalid", intro="Test: p ⊃ q; ~q ⊃ r; therefore p v r.", steps=[
            S("Assume the conclusion false", text="p v r false: p is F and r is F."),
            S("Premise 2", text="~q ⊃ r true with r false forces ~q to be F, so q is T."),
            S("Premise 1", text="p ⊃ q with p F is true whatever q is. All premises are true."),
            S("Verdict", text="p = F, q = T, r = F is a counterexample: premises true, conclusion false. Invalid."),
        ]),
        QUIZ("How many rows are needed in a complete truth table for a formula containing four different variables?", ["4", "8", "16", "32"], 2,
             "$2^4 = 16$.",
             hint="Each new variable doubles the number of rows.",
             feedback=["That is for two variables.", "That is for three variables.", "", "That is for five variables."]),
        QUIZ("In a truth table test, an argument is invalid if", ["Some row has true premises and a false conclusion", "Some row has a false conclusion", "Every row has a false premise", "Some row has a false premise"], 0,
             "Validity forbids exactly the combination: all premises true, conclusion false.",
             hint="What would a counterexample need?",
             feedback=["", "A false conclusion is allowed if some premise is also false.", "Then the argument would be vacuously valid, not invalid.", "A false premise in some rows is harmless as long as a row with all premises true has a true conclusion."]),
        PQ("Practice question 1. Complete the truth table for p · ~q and say in how many rows it is true.",
           "Rows (p, q): TT gives T · F = F; TF gives T · T = T; FT gives F; FF gives F. It is true in exactly one row (p true, q false), so in 1 of 4 rows."),
        PQ("Practice question 2. Test by truth table: p v q; ~p; therefore q (disjunctive syllogism).",
           "Rows: TT: premises T, F so not both true; TF: p v q T, ~p F; FT: p v q T, ~p T, q T (conclusion true); FF: p v q F. The only row where both premises are true is FT, and there the conclusion q is true. Valid."),
        PQ("Practice question 3. Use the indirect method on p ⊃ q; r ⊃ q; therefore (p v r) ⊃ q.",
           "Assume the conclusion false: p v r true and q false. Premise 1: p ⊃ q true with q false forces p false. Premise 2: r ⊃ q true with q false forces r false. Then p v r is false, contradicting its being true. No counterexample: valid."),
        SUM("A truth table for n variables has 2 to the n rows; compute the columns inside out and finish with the main connective.",
            "An argument is valid if no row makes all premises true and the conclusion false; one such row proves invalidity.",
            "The indirect method assumes true premises and false conclusion and looks for a consistent assignment; a contradiction proves validity, success gives a counterexample.",
            "Always check the row count and write all the rows."),
        TIP("Exam link: the Board's 2023 report says that, in Paper 3, the mere construction of the truth table should be credited as an acquired skill; build the table fully and neatly, then read the answer. Paper 1 gives a small table and asks for the status of the statement."),
    ],
))

# ---------------------------------------------------------------- M5.3 Tautologies, contradictions and contingencies
LESSONS.append(lesson(
    module=M5,
    topic="Tautologies, contradictions and contingencies",
    title="Tautologies, contradictions, contingencies and logical equivalence",
    slug="psl2-tautology-contradiction-contingency",
    minutes=23,
    summary="A statement form is a tautology if it is true in every row of its truth table, a contradiction if false in every row, and contingent otherwise. Tautological biconditionals give logical equivalence, and a valid argument corresponds to a tautological conditional.",
    objectives=[
        "Classify a statement form as a tautology, a contradiction or a contingency by truth table",
        "Define logical equivalence and test it with a biconditional",
        "State and verify the main equivalences (De Morgan, implication, transposition, exportation)",
        "Link valid arguments to tautological conditionals",
    ],
    key_concepts=["Tautology", "Contradiction", "Contingency", "Logical equivalence", "De Morgan's laws", "Material implication", "Transposition", "Exportation"],
    blocks=[
        H("Introduction: statements that say everything, nothing, or something"),
        T("'It will rain tomorrow or it will not rain tomorrow' is true whatever the weather. 'It will rain and it will not rain' is false whatever the weather. 'It will rain' is true or false depending on the weather. "
          "Propositional logic classifies statement forms in exactly these three ways, by looking at the final column of the truth table."),
        D("A statement form is a **tautology** (logically true) if it is true in every row of its truth table; a **contradiction** (self-contradictory, logically false) if it is false in every row; and a **contingency** (contingent statement) if it is true in some rows and false in others.", title="Three classes"),
        CODE("p  ~p  p v ~p  p . ~p\n"
             "T  F   T       F\n"
             "F  T   T       F", "text", title="Table 1. p v ~p is a tautology; p . ~p is a contradiction"),
        T("The tautology p v ~p is the **law of excluded middle**; ~(p · ~p) is the **law of non-contradiction**. "
          "A tautology tells us nothing about the world: it is true by form alone. A contradiction is excluded by form alone. A contingency's truth depends on the facts."),
        MISTAKE("Saying a contingent statement is 'sometimes false' when you mean it may be false", "Contingent means the table has both T and F. A statement that happens to be true in the actual world may still be contingent. Look at the table, not at the facts."),
        H("Testing and classifying"),
        EX("Worked example 1: classify with a table", intro="Classify (p · q) ⊃ p and (p ⊃ q) ⊃ (q ⊃ p).", steps=[
            S("(p · q) ⊃ p", text="Column of p · q: T, F, F, F. Conditional with antecedent p · q and consequent p: T, T, T, T. Every row is true: a tautology (a conjunction implies each of its parts)."),
            S("(p ⊃ q) ⊃ (q ⊃ p)", text="p ⊃ q: T, F, T, T. q ⊃ p: T, T, F, T. The whole conditional is T, T, F, T. Row 3 (p false, q true) makes the antecedent true and the consequent false. Contingent."),
        ]),
        CODE("p  q  p . q  (p . q) ⊃ p\n"
             "T  T  T      T\n"
             "T  F  F      T\n"
             "F  T  F      T\n"
             "F  F  F      T\n"
             "\n"
             "p  q  p ⊃ q  q ⊃ p  (p ⊃ q) ⊃ (q ⊃ p)\n"
             "T  T  T      T      T\n"
             "T  F  F      T      T\n"
             "F  T  T      F      F\n"
             "F  F  T      T      T", "text", title="Table 2. The two tables of worked example 1"),
        T("A quick check: to show a form is *not* a tautology, find one row where it is false (use the indirect method). To show it is *not* a contradiction, find one row where it is true. To show it is contingent, find both. "
          "Example: p ⊃ ~q. Row p = T, q = T gives F; row p = T, q = F gives T. So it is contingent. (The Board's 2023 report includes an item on classifying a short truth-table compound as contingent.)"),
        H("Logical equivalence"),
        D("Two statement forms are **logically equivalent** if they have the same truth value in every row: that is, if their biconditional is a tautology. "
          "Equivalent forms can replace one another in any context without changing truth value. A related idea: A **implies** B (logically) when A ⊃ B is a tautology.", title="Logical equivalence and implication"),
        CODE("Name                         Equivalence\n"
             "Double negation              ~~p  ≡  p\n"
             "De Morgan                    ~(p · q)  ≡  ~p v ~q\n"
             "De Morgan                    ~(p v q)  ≡  ~p · ~q\n"
             "Material implication         p ⊃ q  ≡  ~p v q\n"
             "Transposition                p ⊃ q  ≡  ~q ⊃ ~p\n"
             "Exportation                  (p · q) ⊃ r  ≡  p ⊃ (q ⊃ r)\n"
             "Material equivalence         p ≡ q  ≡  (p ⊃ q) · (q ⊃ p)\n"
             "Negated conditional          ~(p ⊃ q)  ≡  p · ~q\n"
             "Distribution                 p · (q v r)  ≡  (p · q) v (p · r)", "text", title="Table 3. Useful equivalences (each checked by a full truth table)"),
        T("De Morgan's laws: the negation of a conjunction is the disjunction of the negations, and the negation of a disjunction is the conjunction of the negations. 'It is not true that both Ada and Ngu came' is the same as 'Ada did not come or Ngu did not come'. "
          "'Neither Ada nor Ngu came' is the same as 'Ada did not come and Ngu did not come'. The Board's 2023 report includes items asking which rule an equivalence illustrates and what De Morgan's theorem establishes."),
        MISTAKE("Pushing a negation through without changing the connective", "~(p · q) is NOT ~p · ~q. De Morgan changes the connective as well: and becomes or, or becomes and. A table confirms it: when p is true and q false, ~(p · q) is true but ~p · ~q is false."),
        EX("Worked example 2: proving an equivalence by table", intro="Show that p ⊃ q is equivalent to ~p v q.", steps=[
            S("Columns", text="p ⊃ q: T, F, T, T. ~p: F, F, T, T. ~p v q: T, F, T, T (rows TT, TF, FT, FF)."),
            S("Compare", text="The two columns are identical, so p ⊃ q ≡ (~p v q) is a tautology."),
            S("Use", text="Any conditional can be rewritten as a disjunction, which is the basis of the replacement rule called Implication (next lesson)."),
        ]),
        H("Validity and tautologies"),
        KEY("The link", "An argument form with premises P1, ..., Pn and conclusion C is valid exactly when the conditional (P1 · ... · Pn) ⊃ C is a tautology.", cards=[
            ["Why", "A counterexample row (all premises true, conclusion false) is exactly a row where the conditional is false."],
            ["Example", "Modus ponens: ((p ⊃ q) · p) ⊃ q is a tautology. Affirming the consequent: ((p ⊃ q) · q) ⊃ p is false when p is false and q true, so it is contingent."],
        ]),
        T("This gives two routes to the same verdict: test the argument for a counterexample row, or test whether the corresponding conditional is a tautology."),
        QUIZ("The statement form p v ~p is", ["A tautology", "A contradiction", "A contingency", "An equivalence"], 0,
             "Whatever the value of p, one of p and ~p is true, so the disjunction is true in every row.",
             hint="Try p true, then p false.",
             feedback=["", "A contradiction is false in every row; this form is never false.", "A contingency has some false rows. This form does not.", "An equivalence is a relation between two forms, not a class of a single form."]),
        QUIZ("Which is equivalent to ~(p v q)?", ["~p v ~q", "~p · ~q", "~p · q", "p · q"], 1,
             "De Morgan: the negation of a disjunction is the conjunction of the negations. Option A is the equivalent of ~(p · q).",
             hint="Neither p nor q.",
             feedback=["That is the equivalent of ~(p · q).", "", "This leaves q unnegated.", "This is the opposite of 'neither'."]),
        PQ("Practice question 1. Classify with a truth table: (p ⊃ q) · (p · ~q).",
           "Rows (p, q): TT: p ⊃ q T, p · ~q F, whole F. TF: p ⊃ q F, whole F. FT: p ⊃ q T, p · ~q F, whole F. FF: p ⊃ q T, p · ~q F, whole F. False in every row: a contradiction. (It asserts that p implies q and also that p is true while q is false.)"),
        PQ("Practice question 2. Show by table that p ≡ ~q is contingent and state the rows that make it true.",
           "Use the columns for p, q, ~q and p ≡ ~q. Row TT: p is T, ~q is F, different values, so F. Row TF: p is T, ~q is T, so T. Row FT: p is F, ~q is F, so T. Row FF: p is F, ~q is T, so F. The column is F, T, T, F. It is true in rows TF and FT (when p and q have different values). Both T and F occur: contingent."),
        PQ("Practice question 3. Use De Morgan to rewrite 'It is not the case that the road is both wide and paved' without negating the whole statement.",
           "Let W: the road is wide; D: the road is paved. ~(W · D) is equivalent to ~W v ~D: the road is not wide or it is not paved (or both). Check: when W is true and D false, both forms are true."),
        SUM("A tautology is true in all rows, a contradiction false in all rows, a contingency has both; read the final column of the table.",
            "Two forms are equivalent when their biconditional is a tautology; the main equivalences are double negation, De Morgan, implication, transposition, exportation and equivalence.",
            "An argument is valid exactly when the conditional of its premises' conjunction and its conclusion is a tautology.",
            "De Morgan changes the connective when a negation passes through it."),
        TIP("Exam link: Paper 1 asks for the status of a compound from a given truth table (tautologous, contingent, contradictory or equivalent) and which rule a given equivalence illustrates; Paper 3 asks you to build the table and state your verdict."),
    ],
))

# ---------------------------------------------------------------- M5.4 Formal proofs of validity
LESSONS.append(lesson(
    module=M5,
    topic="Formal proofs of validity",
    title="Formal proofs of validity: rules of inference and replacement",
    slug="psl2-formal-proofs",
    minutes=26,
    summary="A formal proof derives the conclusion of an argument from its premises by a sequence of lines, each justified by a rule of inference (applied to whole lines) or a rule of replacement (applied to parts of lines).",
    objectives=[
        "State the eight rules of inference (MP, MT, HS, DS, Simp, Conj, Add, CD) and check an application of each",
        "State the ten rules of replacement (DeM, Com, Assoc, Dist, DN, Trans, Impl, Equiv, Exp, Taut)",
        "Construct a proof of validity line by line with a correct justification for each line",
        "Plan a proof by working backwards from the conclusion and avoid the usual mistakes",
    ],
    key_concepts=["Formal proof", "Rule of inference", "Rule of replacement", "Justification", "Working backwards", "Modus ponens", "De Morgan", "Transposition"],
    blocks=[
        H("Introduction: proving instead of testing"),
        T("The truth table tests an argument by checking every case: reliable, but for 6 variables it has 64 rows. A **formal proof** is a different method: starting from the premises, we write a sequence of lines, each following from earlier lines by a rule that is itself valid. "
          "If the last line is the conclusion, the argument is valid. This is how mathematicians reason, and it shows *why* the conclusion follows."),
        D("A **formal proof of validity** for an argument is a sequence of statements, each either a premise or a statement that follows from earlier lines by a stated rule, ending with the conclusion. "
          "Each line has a **justification**: the rule used and the numbers of the lines it comes from.", title="Formal proof"),
        H("Rules of inference"),
        T("A **rule of inference** is a valid argument form. It may be applied only to *whole lines* (not to a part of a line), and it gives a new line that follows from the lines cited. There are eight in this course; letters p, q, r, s stand for any statements, simple or compound."),
        CODE("Name                      Form\n"
             "Modus ponens (MP)         p ⊃ q, p               therefore q\n"
             "Modus tollens (MT)        p ⊃ q, ~q              therefore ~p\n"
             "Hypothetical syllogism (HS)  p ⊃ q, q ⊃ r        therefore p ⊃ r\n"
             "Disjunctive syllogism (DS)   p v q, ~p           therefore q\n"
             "Simplification (Simp)     p · q                  therefore p\n"
             "Conjunction (Conj)        p, q                   therefore p · q\n"
             "Addition (Add)            p                      therefore p v q\n"
             "Constructive dilemma (CD) (p ⊃ q) · (r ⊃ s), p v r  therefore q v s", "text", title="Table 1. Rules of inference (each checked as a valid form)"),
        T("Check an application by matching the *shape*, not the letters. From (a v b) ⊃ ~c and (a v b), MP gives ~c, because the antecedent a v b is matched as a whole. "
          "Some books add Absorption or other names, and some books number the rules differently or add Conditional Proof. Check your textbook."),
        H("Rules of replacement"),
        T("A **rule of replacement** says that two forms are logically equivalent, so one can be replaced by the other *anywhere* in a line, including inside a larger formula. They work in both directions and each is a tautological equivalence."),
        CODE("De Morgan (DeM)       ~(p · q)  ≡  ~p v ~q          ~(p v q)  ≡  ~p · ~q\n"
             "Commutation (Com)     p · q  ≡  q · p              p v q  ≡  q v p\n"
             "Association (Assoc)   (p · q) · r  ≡  p · (q · r)   (p v q) v r  ≡  p v (q v r)\n"
             "Distribution (Dist)   p · (q v r)  ≡  (p · q) v (p · r)   p v (q · r)  ≡  (p v q) · (p v r)\n"
             "Double negation (DN)  p  ≡  ~~p\n"
             "Transposition (Trans) p ⊃ q  ≡  ~q ⊃ ~p\n"
             "Implication (Impl)    p ⊃ q  ≡  ~p v q\n"
             "Equivalence (Equiv)   p ≡ q  ≡  (p ⊃ q) · (q ⊃ p)   p ≡ q  ≡  (p · q) v (~p · ~q)\n"
             "Exportation (Exp)     (p · q) ⊃ r  ≡  p ⊃ (q ⊃ r)\n"
             "Tautology (Taut)      p  ≡  p v p        p  ≡  p · p", "text", title="Table 2. Rules of replacement (each verified by truth table)"),
        KEY("Inference or replacement?", "The difference decides what you may do.", cards=[
            ["Inference", "Whole lines only. From p · q you may infer p by Simp; you may not infer p from (p · q) ⊃ r."],
            ["Replacement", "Any part of a line. In (p ⊃ q) ⊃ r you may replace p ⊃ q by ~p v q (Impl) to get (~p v q) ⊃ r."],
        ]),
        MISTAKE("Using an inference rule on part of a line", "If line 1 is (p ⊃ q) · r and line 2 is p, you may not write q by MP: the conditional is only one conjunct, not a whole line. First write p ⊃ q by Simp, then use MP."),
        H("How to write a proof"),
        T("Number the premises, then write each new line with its justification in the form 'rule, line numbers'. Layout: line number, statement, justification. The conclusion is often written after a sign such as 'therefore'."),
        EX("Worked example 1: a short proof", intro="Prove: p ⊃ q; ~q; p v r; therefore r.", steps=[
            S("Plan", text="r is the right disjunct of line 3. Deny the left disjunct p to use DS. p is denied by MT from lines 1 and 2."),
            S("Line 4", text="~p, by MT on lines 1 and 2."),
            S("Line 5", text="r, by DS on lines 3 and 4."),
        ]),
        CODE("1. p ⊃ q       Premise\n"
             "2. ~q          Premise\n"
             "3. p v r       Premise\n"
             "4. ~p          1, 2 MT\n"
             "5. r           3, 4 DS", "text", title="Proof 1"),
        EX("Worked example 2: using replacement", intro="Prove: ~(p · q); p; therefore ~q.", steps=[
            S("Plan", text="De Morgan turns the negated conjunction into a disjunction. Then p must be turned into ~~p to apply DS."),
            S("Lines", text="Line 3: ~p v ~q (DeM on 1). Line 4: ~~p (DN on 2). Line 5: ~q (DS on 3, 4)."),
        ]),
        CODE("1. ~(p · q)    Premise\n"
             "2. p          Premise\n"
             "3. ~p v ~q    1 DeM\n"
             "4. ~~p        2 DN\n"
             "5. ~q         3, 4 DS", "text", title="Proof 2"),
        EX("Worked example 3: exportation and dilemma", intro="Prove (a): p ⊃ (q ⊃ r); p · q; therefore r. Prove (b): p ⊃ q; p v r; r ⊃ s; therefore q v s.", steps=[
            S("(a) Plan", text="Exportation changes line 1 to (p · q) ⊃ r; MP with line 2 gives r."),
            S("(b) Plan", text="The constructive dilemma needs (p ⊃ q) · (r ⊃ s) as a single line: join lines 1 and 3 by Conj, then CD with line 2."),
        ]),
        CODE("(a) 1. p ⊃ (q ⊃ r)   Premise\n"
             "    2. p · q          Premise\n"
             "    3. (p · q) ⊃ r    1 Exp\n"
             "    4. r              3, 2 MP\n"
             "\n"
             "(b) 1. p ⊃ q          Premise\n"
             "    2. p v r          Premise\n"
             "    3. r ⊃ s          Premise\n"
             "    4. (p ⊃ q) · (r ⊃ s)   1, 3 Conj\n"
             "    5. q v s          4, 2 CD", "text", title="Proof 3"),
        KEY("Strategy", "A good proof is planned, not guessed.", cards=[
            ["Work backwards", "Ask what the last line is and which rule could produce it. Then ask what lines that rule needs."],
            ["Look at the connectives", "A conditional goal ~r ⊃ ~p suggests Trans or HS. A disjunction goal may need Add or Impl."],
            ["Break and join", "Simp pulls a conjunct out; Conj joins lines; DeM and Impl change the connective."],
            ["Check each line", "Match the rule's pattern exactly, and cite the right line numbers."],
        ]),
        EX("Worked example 4: a longer proof", intro="Prove: p ⊃ q; q ⊃ r; therefore ~r ⊃ ~p.", steps=[
            S("Plan", text="The goal is the transposition of p ⊃ r. So first get p ⊃ r by HS, then use Trans."),
            S("Lines", text="Line 3: p ⊃ r (HS 1, 2). Line 4: ~r ⊃ ~p (Trans 3)."),
        ]),
        CODE("1. p ⊃ q       Premise\n"
             "2. q ⊃ r       Premise\n"
             "3. p ⊃ r       1, 2 HS\n"
             "4. ~r ⊃ ~p     3 Trans", "text", title="Proof 4"),
        QUIZ("From the premises p ⊃ q and p ⊃ r and the line p, which rule gives q · r?", ["Conj, after two uses of MP", "Simplification", "Addition", "Constructive dilemma"], 0,
             "MP on 1 and 3 gives q; MP on 2 and 3 gives r; Conj joins them: q · r.",
             hint="Derive q and r separately first.",
             feedback=["", "Simp takes a conjunct out of a conjunction; here we need to build one.", "Add gives q v something, not q · r.", "CD needs a disjunction as a premise."]),
        QUIZ("Which of these is NOT a legitimate step?", ["From p ⊃ q and ~q, ~p", "From p v q and ~p, q", "From p ⊃ q and q, p", "From p · q, q"], 2,
             "From p ⊃ q and q, concluding p is affirming the consequent, an invalid form (no rule of inference corresponds to it).",
             hint="Which pattern was shown to be invalid in the earlier lessons?",
             feedback=["This is modus tollens, a valid rule.", "This is the disjunctive syllogism, a valid rule.", "", "Simplification applies to either conjunct (with Com if needed)."]),
        PQ("Practice question 1. Prove: p ⊃ q; p · r; therefore q. Give the justification for each line.",
           "1. p ⊃ q (Premise). 2. p · r (Premise). 3. p, by Simp on 2. 4. q, by MP on 1 and 3."),
        PQ("Practice question 2. Prove: ~(p v q); r ⊃ p; therefore ~r.",
           "1. ~(p v q) Premise. 2. r ⊃ p Premise. 3. ~p · ~q, by DeM on 1. 4. ~p, by Simp on 3. 5. ~r, by MT on 2 and 4."),
        PQ("Practice question 3. Prove: p ⊃ q; therefore ~(p · ~q).",
           "1. p ⊃ q Premise. 2. ~p v q, by Impl on 1. 3. ~p v ~~q, by DN on 2 (q replaced by ~~q). 4. ~(p · ~q), by DeM on 3. The conclusion says p and not-q cannot both hold, which is what the conditional says."),
        SUM("A formal proof is a numbered sequence of lines, each a premise or derived by a stated rule from earlier lines, ending with the conclusion.",
            "Eight rules of inference (MP, MT, HS, DS, Simp, Conj, Add, CD) apply to whole lines; ten rules of replacement (DeM, Com, Assoc, Dist, DN, Trans, Impl, Equiv, Exp, Taut) apply to parts of lines in both directions.",
            "Plan by working backwards from the conclusion; match each rule's pattern exactly.",
            "Never convert a fallacy into a rule: affirming the consequent and denying the antecedent are not rules."),
        TIP("Exam link: the Board's 2023 report names the propositional calculus as part of Paper 3 and recommends careful teaching of it. Paper 1 asks which rule an equivalence illustrates (for example De Morgan). Write every line with its justification so that each step can be credited."),
    ],
))

# ---------------------------------------------------------------- Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: working through 50 multiple-choice questions in philosophy",
    slug="psl2-paper1-multiple-choice",
    minutes=22,
    summary="How to approach the 50 multiple-choice questions of Paper 1, which cover the whole philosophy syllabus: reading stems, attributing ideas to the right philosopher, logic items, common distractors and a revision map of the five Lower Sixth modules.",
    objectives=[
        "Use a routine of reading the stem, predicting, eliminating and checking",
        "Attribute doctrines to the right thinker and avoid group generalisations",
        "Answer logic items quickly: forms, distribution, eductions, truth tables and fallacies",
        "Plan revision with a map of the five Lower Sixth modules",
    ],
    key_concepts=["Stem", "Distractor", "Best answer", "Attribution", "Elimination", "Revision map"],
    blocks=[
        H("Introduction: what Paper 1 is"),
        T("According to the Board's 2023 subject report for Advanced Level Philosophy, Paper 1 is made of 50 multiple-choice questions and covers the whole syllabus. "
          "The report describes the items by the skills they test (knowledge, understanding and analysis), and warns that loose or imprecise wording can mislead candidates. "
          "Because the paper samples the entire syllabus (Western philosophy, African philosophy and logic), no module can be skipped. "
          "The weight of this paper in the final mark is not given in the report: check the exact format with your teacher. "
          "The KKEVO mock that goes with this lesson has 50 questions in 90 minutes (a KKEVO practice setting) and covers the five Lower Sixth modules in proportion to their topics."),
        H("A routine for every question"),
        KEY("Four steps", "Do them in order and quickly.", cards=[
            ["1. Read the stem", "Underline the command word: which is, which is NOT, identify, according to. Note the thinker or the logical term named."],
            ["2. Predict", "Say the answer to yourself before reading the options. If the stem names a philosopher, recall his central idea."],
            ["3. Eliminate", "Cross out options that fail, and say why. Each wrong option is built on a misconception or on another thinker's idea."],
            ["4. Check", "Re-read the stem against your choice. Does the option answer exactly what is asked?"],
        ]),
        T("Take about one and three-quarter minutes per question on average. If a question holds you for more than two minutes, mark your best guess and return to it. Never leave a question blank; a blank cannot score. Ask your teacher how wrong answers are treated."),
        H("Philosophy items: attribute carefully"),
        T("The Board's report advises candidates and teachers to respect scientific and linguistic orthodoxy (use technical terms correctly) and to evaluate individual philosophers rather than groups. In multiple-choice terms: do not answer 'what do empiricists think?' with one empiricist's view. "
          "Learn each thinker's own contribution: Thales and water as the first principle (arche); Heraclitus and flux; Parmenides and unchanging being; Democritus and atoms; Protagoras and relativism; Socrates and the method of questioning; Plato and the Forms; Aristotle and matter and form; Descartes and methodic doubt; Locke and ideas from experience; Hume and the problem of causation; Kant and the categorical imperative."),
        KEY("Common distractors in philosophy", "Recognise them.", cards=[
            ["The right idea, wrong thinker", "An option that is true of another philosopher (Plato's Forms offered for Aristotle, Descartes' doubt for Locke)."],
            ["The group generalisation", "'Empiricists think X' when only one empiricist did."],
            ["The reversal", "The opposite of the thinker's position (for example, relativism offered for Socrates' search for definitions, or reason and faith as hostile for Aquinas)."],
            ["The half-truth", "An option that names the right topic but states it incompletely."],
            ["The look-alike term", "Terms that sound alike (extension and comprehension; conversion and contraposition; ethics and aesthetics)."],
        ]),
        MISTAKE("Answering from the first word you recognise", "In multiple-choice philosophy, the option that mentions a famous word is often a distractor. Read all four options before choosing."),
        H("Logic items: quick methods"),
        T("In the Board's 2023 paper, logic items include naming a form of immediate inference, identifying a fallacy in a short syllogism or informal argument, naming the order of an enthymeme, the response to a dilemma, the status of a compound from a truth table, and the rule behind an equivalence. Each has a fast method."),
        CODE("Item type                  Fast method\n"
             "Name the eduction          'S is P' to 'non-P is non-S' is contraposition. Swap terms only: conversion.\n"
             "                           Change quality and complement the predicate: obversion.\n"
             "Fallacy in a syllogism     Find S, P, M. Check the middle (distributed?), then the conclusion's terms.\n"
             "Order of an enthymeme      Which proposition is missing: major (1st), minor (2nd), conclusion (3rd)?\n"
             "Status from a table        Look at the final column only: all T, all F, or mixed.\n"
             "Which rule?                Match the shape: not-(p and q) with not-p or not-q is De Morgan.\n"
             "Symbolisation              'Only if' is p ⊃ q; 'neither ... nor' is ~p · ~q.", "text", title="Table 1. Fast methods for logic items"),
        EX("Worked example 1: a table item", intro="The final column of the truth table of (p ⊃ q) ⊃ p reads T, T, F, F for rows TT, TF, FT, FF. The statement is: A a tautology, B a contradiction, C a contingency, D equivalent to q.", steps=[
            S("Predict", text="Mixed column: both T and F occur."),
            S("Eliminate", text="A needs all T; B needs all F; D confuses a status with an equivalence (the column is the same as p's, not q's)."),
            S("Answer", text="C, contingency."),
        ]),
        EX("Worked example 2: a syllogism item", intro="Which fallacy is committed? 'All teachers are graduates; all nurses are graduates; so all nurses are teachers.' A undistributed middle, B illicit major, C illicit minor, D exclusive premises.", steps=[
            S("Terms", text="S = nurses, P = teachers, M = graduates."),
            S("Test the middle", text="M is the predicate of two A propositions: distributed in neither."),
            S("Answer", text="A. The conclusion's distributed term (nurses) is distributed in the minor premise (subject of A), so there is no illicit minor."),
        ]),
        H("A map of the five Lower Sixth modules"),
        CODE("Module                                  Ideas to be ready for\n"
             "Nature, Origins & Methods               myth and logos; branches of philosophy;\n"
             "                                        maieutics, Cartesian doubt, dialectic, phenomenology\n"
             "Ancient Greek & Medieval                Pre-Socratic first principles; Sophists; Socrates;\n"
             "                                        Plato's Forms; Aristotle's causes; Hellenistic schools;\n"
             "                                        Augustine; Aquinas, faith and reason\n"
             "Modern Western                          Descartes, Spinoza, Leibniz; Locke, Berkeley, Hume;\n"
             "                                        Hobbes, Locke, Rousseau; Kant\n"
             "Traditional Formal Logic                A, E, I, O; distribution; square; eductions;\n"
             "                                        syllogism; dilemma; informal fallacies\n"
             "Symbolic / Propositional Logic          connectives; truth tables; tautology; proofs", "text", title="Table 2. Revision map (Upper Sixth topics, such as African philosophy, are in the real paper too)"),
        IMG("alpsl2-argument-test.svg", alt="A flowchart: an argument about classes (all, no, some) goes to categorical logic; an argument about statements joined by if, and, or, not goes to propositional logic; a persuasive but poor argument may contain an informal fallacy.",
            caption="Figure 1. Which kind of logic problem is it? The first decision speeds up every logic item."),
        QUIZ("A stem asks: 'Which of the following is NOT an eduction?' The options are conversion, obversion, contraposition and contrariety. The answer is", ["Conversion", "Obversion", "Contraposition", "Contrariety"], 3,
             "Contrariety is a relation of opposition on the square (A and E). Conversion, obversion and contraposition are eductions.",
             hint="Which one belongs to the square of opposition?",
             feedback=["Conversion is an eduction.", "Obversion is an eduction.", "Contraposition is an eduction.", ""]),
        QUIZ("Which approach is best when two options both look partly right?", ["Choose the longer option", "Re-read the stem for the exact command word and thinker, then choose the option that answers exactly that", "Choose the option with a famous name", "Leave the question blank"], 1,
             "The task is to answer the stem. Compare each option with the stem's exact words.",
             hint="What exactly is the stem asking?",
             feedback=["Length is not a reliable clue.", "", "A famous name is a frequent distractor.", "A blank cannot score."]),
        PQ("Practice question 1. In a multiple-choice question, the stem says: 'For Aquinas, faith and reason are:' and the options are mutually exclusive, independent, hierarchically related, and identical. Explain how to reach the best answer.",
           "Predict first: Aquinas holds that reason and faith are both sources of truth that cannot finally conflict, with faith (revealed theology) above natural reason in rank, while philosophy serves theology. Eliminate 'mutually exclusive' and 'independent' (both deny the link), and 'identical' (he distinguishes them). The best answer is 'hierarchically related'. This matches the standard textbook account: check your textbook for the wording of the options."),
        PQ("Practice question 2. State the form of the following and its status: 'If the road is flooded, the bus is late. The bus is late. Therefore the road is flooded.'",
           "Form: If A then B; B; therefore A. This is affirming the consequent, invalid. Quick way: the conclusion is the antecedent, and the minor premise affirms the consequent."),
        PQ("Practice question 3. Plan how to use 90 minutes for 50 questions.",
           "About 60 minutes for a first pass (an average of about 70 seconds each, spending longer on logic items that need a table), 20 minutes to return to marked questions, 10 minutes to check that every question has an answer and to recheck calculations or tables. Adjust to your own speed."),
        SUM("Paper 1 has 50 multiple-choice questions over the whole syllabus; read the stem, predict, eliminate and check.",
            "Attribute ideas to the right individual thinker; groups are traps.",
            "For logic items use the fast methods in Table 1 and start by deciding whether the argument is about classes or statements.",
            "Use the revision map: every module is sampled."),
        TIP("Use the KKEVO 'Paper 1 mock exam A' after finishing the five Lower Sixth modules and look at the results by topic to decide what to revise."),
    ],
))

# ---------------------------------------------------------------- Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: philosophical essays and textual analysis",
    slug="psl2-paper2-essays-textual-analysis",
    minutes=24,
    summary="Paper 2 tests philosophical writing on Western philosophy, African philosophy and the analysis of a text. This lesson teaches how to read a question, plan an essay with exposition and critique, and comment on a passage, using the Board's 2023 observations.",
    objectives=[
        "Analyse an essay question: command, key terms, scope and thinker",
        "Plan an essay with introduction, exposition and critique (internal before external) and a conclusion",
        "Avoid narration: philosophise by evaluating, not only by describing",
        "Comment on a short argumentative text in eight steps",
    ],
    key_concepts=["Question analysis", "Problématique", "Exposition", "Internal critique", "External critique", "Textual analysis", "Criteria-based marking"],
    blocks=[
        H("Introduction: what the Board's report tells us"),
        T("The Board's 2023 subject report describes Paper 2 as philosophical writing. It has three sections of two questions each: Section 1 on Western philosophy, Section 2 on African philosophy, and Section 3 on textual analysis. "
          "Check on your own paper how many questions are to be answered and from which sections. "
          "The report says essay and logic answers are marked by examiners using broken-down criteria (item-, task- and skill-based) that credit every worthwhile attempt, so a clear plan that earns points step by step is the best strategy. "
          "It also lists the skills it tests: understanding, application, analysis, synthesis and evaluation."),
        KEY("What the report advises (paraphrased)", "These comments come from the examiners' observations on 2023.", cards=[
            ["Philosophise, do not narrate", "A very broad question invites a history lesson. Choose individual philosophers and argue about them."],
            ["Know the vocabulary", "Use the technical terms from the first lesson on, for example 'cosmogony' (an account of the origin of the world)."],
            ["Internal critique first", "Examiners stress internal critique of a philosopher (does it hold together?) rather than only external critique (what others say)."],
            ["Answer the intent", "On one African philosophy question many candidates wrote about witchcraft instead of the 'vital force' the question was about. Read for what the question really asks."],
            ["Textual analysis", "Choose clear argumentative passages and use the text; sub-questions can guide you."],
        ]),
        H("Reading a question"),
        KEY("Four questions to ask", "Do this before writing a word.", cards=[
            ["1. Command", "Discuss, examine, evaluate, compare, explain: 'evaluate' demands judgement."],
            ["2. Key terms", "Define each: they become the first paragraph."],
            ["3. Scope", "Which thinkers or period? Choose a few you can treat in depth."],
            ["4. Problem", "What difficulty does the question raise? State it as a question; it is your problématique."],
        ]),
        H("The essay architecture"),
        D("**Introduction**: define the key terms, situate the topic, state the problem and announce the plan. "
          "**Development**: exposition of each position (what is claimed and why), then critique. "
          "**Conclusion**: an answer to the problem, not a summary only.", title="Three parts"),
        D("An **internal critique** examines a position from within: are its premises consistent, are its terms clear, does the conclusion follow? "
          "An **external critique** brings objections from other positions or from facts it ignores. Give internal critique first; then give external critique, and where possible a reply on the thinker's behalf. "
          "Teachers' methods of organising the development (for example thesis, antithesis, synthesis) differ: follow the method your teacher has taught.", title="Internal and external critique"),
        EX("Worked example 1: a Western philosophy plan", intro="Question: 'Examine the Pre-Socratic search for the first principle (arche) and assess its value for the birth of philosophy.'", steps=[
            S("Key terms", text="Arche: the first principle from which everything comes and into which it returns. Cosmogony: an account of the origin of the world. Monism: one basic stuff."),
            S("Introduction", text="Myth explained origins through gods and stories. Early Greek thinkers asked instead for one natural principle. Problem: how far was the search for an arche a real step towards philosophy?"),
            S("Exposition", text="Thales: water. Anaximander: the boundless (apeiron). Anaximenes: air, with thickening and thinning. Heraclitus: constant change, with fire and logos as pattern. Parmenides: being is one and changeless, change is illusion of the senses. Democritus: atoms and void, many unchanging bodies. Pythagoras: number and harmony (check your textbook for the details attributed to him)."),
            S("Internal critique", text="Thales' water explains many things but does not say how water becomes other things; Anaximenes adds a mechanism. Parmenides' argument, if accepted, makes motion and change impossible; critics ask whether his premise that what is not cannot be thought or said is too strong."),
            S("External critique", text="Aristotle and later thinkers judged these accounts partial; modern science treats them as speculation without experiment. Reply: the value lies in the method of giving reasons, not in the answers."),
            S("Conclusion", text="The search for an arche was a real step because it replaced story by argument, even though the answers were weak."),
        ]),
        MISTAKE("Narration instead of argument", "A paragraph that lists what each philosopher said, in order, will score for knowledge but not for analysis or evaluation. After each exposition write one or two sentences of critique: 'This fails because ...' or 'The strongest reply is ...'."),
        EX("Worked example 2: a method question plan", intro="Question: 'Assess the role of methodic doubt in Descartes' search for certainty.'", steps=[
            S("Key terms", text="Methodic doubt: a deliberate and temporary doubt used as a method, not as a conclusion. Certainty: what cannot be doubted."),
            S("Exposition", text="Descartes doubts the senses (they sometimes deceive), then even waking experience (dreams), then reason itself (the supposition of an all-powerful deceiver). He finds that he cannot doubt that he is doubting and so thinking: 'I think, therefore I am' (a standard paraphrase). From this he builds: the clear and distinct idea as the mark of truth, God, and the external world."),
            S("Internal critique", text="Critics argue that trusting clear and distinct ideas depends on God's goodness, proved by those same ideas: the 'Cartesian circle'. Defenders reply that the cogito and simple intuitions are not in doubt in the moment they are grasped."),
            S("External critique", text="Empiricists reject innate ideas; some argue the cogito proves only that thinking is occurring, not a substantial self."),
            S("Conclusion", text="Doubt is useful as a method to clear away unproved beliefs, while its success in rebuilding knowledge is disputed."),
        ]),
        H("Textual analysis: a method"),
        IMG("alpsl2-commentary-steps.svg", alt="Eight boxes in two rows: situate, theme, problem, thesis, structure, internal critique, external critique, conclusion.",
            caption="Figure 1. A method for commenting on a philosophical text (follow your teacher's own method if it differs)."),
        T("Here is a short passage written by KKEVO for practice (it is not from any book): 'We should not trust a witness who has deceived us even once. Our senses have deceived us: a stick in water looks bent, a far tower looks round, a dream feels real. So we should doubt what the senses tell us, and seek a truth that does not depend on them.'"),
        EX("Worked example 3: commentary skeleton", intro="Comment on the passage above.", steps=[
            S("Situate", text="Position of a type found in rationalism: sense experience is an unreliable basis for knowledge. (For a real text, give author, work and context.)"),
            S("Theme and problem", text="Theme: the reliability of the senses. Problem: can knowledge be built on sense experience?"),
            S("Thesis", text="We should doubt the senses and seek a truth independent of them."),
            S("Structure", text="An analogy (the untrustworthy witness) leads to examples (the bent stick, the far tower, the dream) and then to the conclusion."),
            S("Internal critique", text="The principle 'distrust anything that has ever deceived' is strong: the senses usually serve us well, and we discover the illusions by using other senses. Moving from 'sometimes' to 'always doubt' is a hasty step."),
            S("External critique", text="An empiricist replies that sense experience, checked and corrected, is the source of all our knowledge. A rationalist would reply that reasoning gives a more certain base."),
            S("Conclusion", text="The passage justifies caution about the senses, not necessarily rejecting them; whether any base independent of experience exists is the issue to settle."),
        ]),
        MISTAKE("Paraphrasing the text without commenting on it", "A commentary that only repeats the passage is not an analysis. Each section (theme, problem, thesis, structure, critiques) must say something about the text that the text does not say itself."),
        QUIZ("Which is an internal critique of a philosopher's position?", ["Another school rejects it", "It contradicts a scientific fact the philosopher did not know", "Its premises are inconsistent with each other", "It is unpopular today"], 2,
             "An internal critique tests the position from within: consistency, clarity, validity.",
             hint="Internal means within the system itself.",
             feedback=["That is an external objection.", "That is an external objection (from outside the system).", "", "Popularity is not an argument."]),
        QUIZ("In an essay, what should follow the exposition of a position?", ["Another exposition", "A critique (internal, then external) with a reply if possible", "The conclusion", "The title again"], 1,
             "Philosophy requires evaluation after description.",
             hint="Narration is not enough for the highest skills.",
             feedback=["Several expositions without critique leads to narration.", "", "A conclusion needs the evaluation first.", "Repeating the title adds nothing."]),
        PQ("Practice question 1. Analyse the question 'Evaluate Plato's theory of the Forms' in four lines.",
           "Command: evaluate (judgement needed). Key terms: Forms, participation, knowledge and opinion. Scope: Plato (Republic's divided line and cave, if taught). Problem: does the theory explain knowledge and reality, or create new problems (such as how Forms relate to particulars)? The essay should expound the theory, then argue internal (the relation of Forms to things) and external (Aristotle's rejection of separate Forms) critiques."),
        PQ("Practice question 2. A candidate writes a long essay on 'Hume on causation' that lists what Hume wrote about everything from impressions to miracles. What is wrong, and how can it be repaired?",
           "It is narration and off-target. Repair: define causation and the problem, state Hume's analysis (we perceive succession and constant conjunction, but not necessary connection; belief in causes comes from habit), give an internal critique (does his account make science unsupported?) and an external critique (Kant's reply), then conclude."),
        PQ("Practice question 3. Give a thesis, a structure and one internal critique for this practice passage: 'Every free action is praiseworthy. Building the bridge was a free action. So building the bridge was praiseworthy.'",
           "Thesis: every free action is praiseworthy, so the bridge-building was. Structure: general premise, particular premise, conclusion (a syllogism, AAA in figure 1, Barbara). Internal critique: the general premise is too strong (a free action that harms others is not praiseworthy), so the argument is valid but not sound."),
        SUM("Paper 2 has Western philosophy, African philosophy and textual analysis; check on your paper how many questions to answer.",
            "Read the question for command, key terms, scope and problem, and answer its real intent.",
            "Use introduction, exposition with critique (internal first), then external critique and a real conclusion; philosophise, do not narrate.",
            "In a commentary, situate, identify theme, problem, thesis and structure, then critique and conclude.",
            "Marking is broken down into items, tasks and skills: every well-placed point earns credit."),
        TIP("Exam link: this lesson prepares the method. The Upper Sixth module on African philosophy and the module on methodology develop it. Use the KKEVO 'Paper 2 practice paper A' to practise planning and analysis."),
    ],
))

# ---------------------------------------------------------------- Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: logic problems and philosophical problems",
    slug="psl2-paper3-logic-problems",
    minutes=24,
    summary="Paper 3 tests critical thinking: logic problems (traditional logic, propositional calculus and predicate calculus) and philosophical problems. This lesson shows how to break a logic problem into sub-parts, paraphrase before symbolising, explain fallacies in context and plan a problem essay.",
    objectives=[
        "Break a multi-part logic problem into sub-parts and answer each with working shown",
        "Begin symbolisation with a paraphrase and respect the structure of the sentence",
        "Explain a fallacy in the context of the given argument",
        "Link the categorical forms to quantifier notation and plan a philosophical-problem essay",
    ],
    key_concepts=["Sub-parts", "Paraphrase", "Compositionality", "Truth table credit", "Fallacy in context", "Quantifier notation", "Philosophical problem"],
    blocks=[
        H("Introduction: what the Board's report says about Paper 3"),
        T("In the Board's 2023 subject report, Paper 3 is described as critical thinking: problem-solving and analysis. "
          "Section 1 is Logic (Questions 1 to 3) and Section 2 is Philosophical Problems (Questions 4 to 6). The report states that the logic covered traditional logic, the propositional calculus and first-order predicate calculus, and that all three sections of systematic philosophy were covered. "
          "It estimates performance at about 80% in logic and about 85% in philosophical problems, and says the logic exercises were within the reach of students, with accommodating levels of difficulty. "
          "Check on your own paper how many questions are to be answered and from which sections."),
        KEY("What the examiners advise (paraphrased from the 2023 report)", "Use these as a checklist.", cards=[
            ["Break the solution into sub-parts", "Learners should divide a problem into steps and show each step; paraphrasing the solution is an extra advantage."],
            ["Explain a fallacy in context", "Name it and show where it occurs in this argument, not in general terms."],
            ["Credit for the table itself", "Building a correct truth table is a skill that earns credit by itself, even if your final verdict goes wrong."],
            ["Symbolise from a paraphrase", "Analyse the sentence first, then rebuild it in symbols; respect how the parts are combined (compositionality)."],
            ["Take care with the calculi", "The examiners ask for more careful teaching of propositional and predicate calculus: practise them early."],
        ]),
        H("A routine for a logic problem"),
        IMG("alpsl2-argument-test.svg", alt="A flowchart: arguments about classes go to categorical logic; arguments about statements go to propositional logic; persuasive but poor arguments may contain an informal fallacy.",
            caption="Figure 1. First decide what kind of problem it is."),
        KEY("Five steps", "Each step can earn marks independently.", cards=[
            ["1. Paraphrase", "Restate the argument in plain logical language: premises, conclusion, connectives or quantifiers."],
            ["2. Symbolise", "Give a dictionary (letter = statement or term), then the formulas."],
            ["3. Choose the method", "Syllogism rules or Venn diagram; truth table, indirect method or proof."],
            ["4. Work it out in view", "Show every column, line or rule. Neatness earns credit."],
            ["5. State the verdict", "A sentence: 'The argument is valid because ...' or 'invalid, as row 3 shows'."],
        ]),
        EX("Worked example 1: a multi-part problem", intro="Argument: If Ngu studies, he passes. If he passes, his parents are happy. Ngu studies. Therefore his parents are happy. (a) Symbolise. (b) Test by truth table. (c) Give a formal proof. (d) Name the form.", steps=[
            S("(a) Dictionary and symbols", text="S: Ngu studies; P: Ngu passes; H: his parents are happy. Premises: S ⊃ P; P ⊃ H; S. Conclusion: H."),
            S("(b) Truth table", text="Three variables, 8 rows. The premises S ⊃ P, P ⊃ H and S are all true in one row only: S, P, H all true. There the conclusion H is true. No counterexample row: valid."),
            S("(c) Proof", text="1. S ⊃ P (Premise). 2. P ⊃ H (Premise). 3. S (Premise). 4. S ⊃ H (HS 1, 2). 5. H (MP 4, 3)."),
            S("(d) Form", text="A chain of two conditionals with a categorical minor premise: hypothetical syllogism followed by modus ponens (valid)."),
        ]),
        CODE("S  P  H  S ⊃ P  P ⊃ H  S  | H\n"
             "T  T  T  T      T      T  | T   <- the only row with all premises true\n"
             "T  T  F  T      F      T  | F\n"
             "T  F  T  F      T      T  | T\n"
             "T  F  F  F      T      T  | F\n"
             "F  T  T  T      T      F  | T\n"
             "F  T  F  T      F      F  | F\n"
             "F  F  T  T      T      F  | T\n"
             "F  F  F  T      T      F  | F", "text", title="Table 1. Truth table for worked example 1"),
        MISTAKE("Symbolising without paraphrase", "Rushing to symbols leads to errors such as writing 'neither Ada nor Ngu' as ~(A · N). Always write the paraphrase first ('Ada did not and Ngu did not') and build up."),
        H("Fallacy in context"),
        EX("Worked example 2: naming and explaining", intro="'All members of the choir are cheerful persons. Some teachers are cheerful persons. Therefore some teachers are members of the choir.' Test and explain.", steps=[
            S("Terms and form", text="S = teachers, P = members of the choir, M = cheerful persons. Major: All P are M (the premise containing the choir members). Minor: Some S are M. Conclusion: Some S are P. Mood AII, figure 2."),
            S("Fallacy", text="Undistributed middle: 'cheerful persons' is the predicate of an A and of an I, so it is distributed in neither premise."),
            S("In context", text="The teachers who are cheerful may be a different part of the class of cheerful persons from the choir members. Being cheerful does not link the two classes."),
        ]),
        H("A glimpse of predicate (quantifier) notation"),
        T("The report names first-order predicate calculus among the logic covered in Paper 3, although the Lower Sixth topic list in this course only names traditional and propositional logic. Here is the link between the two; your textbook develops it further and may use a different notation."),
        D("In predicate notation Fx means 'x is F'. The **universal quantifier** (x) means 'for every x'; the **existential quantifier** (∃x) means 'for at least one x'.", title="Quantifiers"),
        CODE("A  All F are G          (x)(Fx ⊃ Gx)\n"
             "E  No F are G           (x)(Fx ⊃ ~Gx)\n"
             "I  Some F are G         (∃x)(Fx · Gx)\n"
             "O  Some F are not G     (∃x)(Fx · ~Gx)\n"
             "   Only F are G         (x)(Gx ⊃ Fx)\n"
             "   Not all F are G      ~(x)(Fx ⊃ Gx)", "text", title="Table 2. The categorical forms in predicate notation (checked against all small models)"),
        T("Notice the pattern: a universal statement takes the conditional ⊃ and a particular statement takes the conjunction ·. Using ⊃ with ∃ is a common mistake: (∃x)(Fx ⊃ Gx) is true whenever something is not F, so it says almost nothing. "
          "'Only women are traders' means: whoever is a trader is a woman: (x)(Tx ⊃ Wx). The same care about 'only' that we took in propositional logic applies here."),
        H("Philosophical problems"),
        T("Section 2 of Paper 3 is described in the report as Philosophical Problems, and it says candidates did well here, with the examiners recommending that the teaching of systematic philosophy be placed in context. "
          "Here a problem question is one that sets a difficulty, for instance whether we can have certain knowledge, and asks you to investigate it. The Upper Sixth module on methodology develops the dissertation method; for now use the same architecture as in Paper 2."),
        KEY("Plan for a problem essay", "Keep it simple.", cards=[
            ["Introduction", "Define terms, show why the problem is a problem (a tension or apparent contradiction), and state it as a question."],
            ["Development", "Present two or three positions fairly with reasons (for knowledge: rationalist, empiricist, sceptical), then discuss their strengths and weaknesses in turn."],
            ["Conclusion", "Give your reasoned answer and say what remains open."],
        ]),
        QUIZ("Which is the correct predicate-notation form of 'Some students are not candidates' (Sx: x is a student; Cx: x is a candidate)?", ["(x)(Sx ⊃ ~Cx)", "(∃x)(Sx · ~Cx)", "(∃x)(Sx ⊃ ~Cx)", "~(∃x)(Sx · Cx)"], 1,
             "O takes ∃ with the conjunction: some x is a student and not a candidate.",
             hint="A particular statement uses ∃ and ·.",
             feedback=["That is E: no students are candidates.", "", "∃ with ⊃ is a standard error: it is true if anything at all is not a student.", "That says there is no student who is a candidate: E."]),
        QUIZ("In a Paper 3 symbolisation question, the first step is", ["Write the final symbols", "Give a paraphrase and a dictionary", "Draw the truth table", "Name the fallacy"], 1,
             "The Board's report advises starting from a paraphrase and building up in symbols.",
             hint="What does the report say about where symbolisation begins?",
             feedback=["Starting with symbols causes structural errors.", "", "The table comes after the symbolisation.", "Fallacy naming belongs to informal arguments."]),
        PQ("Practice question 1. Symbolise 'Only members who have paid may vote' in predicate notation and propositional notation (use Vx, Mx, Px for the individual form; V, M, P for the propositional form).",
           "Paraphrase: whoever may vote is a member who has paid. Predicate: (x)(Vx ⊃ (Mx · Px)). Propositional (for one person): V ⊃ (M · P). 'Only' puts the voting condition in the antecedent."),
        PQ("Practice question 2. Test: 'If the exam is hard, the pass rate falls. The pass rate fell. So the exam was hard.' Name the form and give a counterexample.",
           "Form: affirming the consequent, invalid. Counterexample: the exam was easy but the pass rate fell because many candidates were absent. Premises true, conclusion false."),
        PQ("Practice question 3. Prove: p ⊃ q; q ⊃ r; ~r; therefore ~p.",
           "1. p ⊃ q (Premise). 2. q ⊃ r (Premise). 3. ~r (Premise). 4. p ⊃ r (HS 1, 2). 5. ~p (MT 4, 3)."),
        SUM("Paper 3 covers logic (traditional, propositional, predicate) and philosophical problems; check the number of questions to answer on your paper.",
            "Break each problem into sub-parts, begin with a paraphrase, give a dictionary, show every step and state a verdict.",
            "Explain a fallacy in the context of the argument; construct the whole truth table neatly (it earns credit by itself).",
            "In predicate notation universals use ⊃ and particulars use ·; 'only' reverses the conditional.",
            "A problem essay has an introduction that states the problem as a question, a development with positions and critique, and a reasoned conclusion."),
        TIP("Use the KKEVO 'Paper 3 practice paper A' for the logic and text-method parts, and write out the answers in full on paper as well."),
    ],
))

