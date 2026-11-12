"""A Level Philosophy (0790), Lower Sixth: practice sets for Traditional Formal Logic, Symbolic / Propositional Logic and the
Examination module.

One 8-question set per lesson (9 topic lessons, 3 examination lessons), plus 'Paper 1 mock exam A' (50 multiple-choice
questions across all five Lower Sixth modules in proportion to their topic counts), 'Paper 2 practice paper A' (about 25
auto-markable parts on essay planning, text analysis, key arguments and logic) and 'Paper 3 practice paper A' (about 20
auto-markable logic problems and text-commentary method items). Exam facts are only those of the Board's 2023 subject
report (Paper 1 = 50 multiple-choice questions over the whole syllabus; Paper 2 = Western philosophy, African philosophy and
textual analysis; Paper 3 = logic and philosophical problems). The timings of the mock papers (90 and 150 minutes) are KKEVO
practice settings, not Board settings. Essays and commentaries cannot be auto-marked, so the Paper 2 and Paper 3 practice
papers use multiple-choice and numeric parts. Passages are written by KKEVO for practice. Every logical claim (truth
table, syllogism, immediate inference, proof line) was checked by brute force in Python. No quotations are used.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("philosophy", "lower-sixth")

M1 = "Nature, Origins & Methods of Philosophy"
M2 = "Ancient Greek & Medieval Philosophy"
M3 = "Modern Western Philosophy"
M4 = "Traditional Formal Logic"
M5 = "Symbolic / Propositional Logic"
M_EXAM = "Examination"


def Q(prompt, correct, wrongs, sol, concept, skill, hint, diagram="", alt=""):
    """Four-option MC spec. wrongs = [(text, why)] x3; sol = solution text or [(title, text)]. Position balanced by build()."""
    assert len(wrongs) == 3, prompt
    if isinstance(sol, str):
        sol = [("Reasoning", sol)]
    return {"k": "mc", "prompt": prompt, "correct": correct, "wrongs": wrongs, "steps": sol, "concept": concept,
            "skill": skill, "hint": hint, "diagram": diagram, "alt": alt}


def N(prompt, answer, sol, concept, skill, hint, tol=0, unit=""):
    if isinstance(sol, str):
        sol = [("Working", sol)]
    return {"k": "num", "prompt": prompt, "answer": answer, "steps": sol, "concept": concept, "skill": skill,
            "hint": hint, "tol": tol, "unit": unit}


def build(specs, seed):
    """MC/NUM questions with the correct option spread evenly over A-D."""
    rng = random.Random(seed)
    counts = [0, 0, 0, 0]
    out = []
    for s in specs:
        st = [S(a, text=b) for a, b in s["steps"]]
        assert s["concept"] and len(s["concept"]) <= 80, s["concept"]
        assert s["hint"] and s["skill"] and st, s["prompt"]
        if s["k"] == "num":
            out.append(NUM(s["prompt"], s["answer"], steps=st, tolerance=s["tol"], unit=s["unit"], concept=s["concept"],
                           skill=s["skill"], hint=s["hint"]))
            continue
        m = min(counts)
        pos = rng.choice([i for i in range(4) if counts[i] == m])
        counts[pos] += 1
        ch = [C(t, why=w) for t, w in s["wrongs"]]
        assert all(w for _, w in s["wrongs"]), s["prompt"]
        ch.insert(pos, C(s["correct"], correct=True))
        out.append(MC(s["prompt"], ch, steps=st, concept=s["concept"], skill=s["skill"], hint=s["hint"],
                      diagram=s["diagram"], diagram_alt=s["alt"]))
    return out


SETS = []

# ---------------------------------------------------------------- 1. Terms and categorical propositions
SETS.append(practice_set(
    module=M4, topic="Terms and categorical propositions", title="Terms, A E I O forms and distribution",
    lesson="psl2-terms-categorical-propositions",
    questions=build([
        Q("The class of all the things to which a term applies is called its", "extension (denotation)",
          [("comprehension (intension)", "Comprehension is the set of attributes, not the things."),
           ("distribution", "Distribution is a property of a term in a proposition, not of the term alone."),
           ("quantity", "Quantity (universal or particular) belongs to propositions.")],
          "The extension of 'river' is all rivers; its comprehension is the attributes that make something a river.",
          "Extension and comprehension", "Recall", "Think of 'the things' versus 'the attributes'."),
        Q("Which of the following is a proposition of the form E?", "No tortoise is quick.",
          [("All tortoises are slow.", "This is A: all S are P (affirmative)."),
           ("Some tortoises are not quick.", "This is O: particular negative."),
           ("Some tortoises are slow.", "This is I: particular affirmative.")],
          "E is universal negative: 'No S are P'.", "The four categorical forms", "Recall", "E is universal and negative."),
        Q("In the proposition 'Some students are not athletes', which term is distributed?", "'athletes' only",
          [("'students' only", "The subject of a particular proposition is not distributed."),
           ("both terms", "Only E distributes both terms."),
           ("neither term", "Neither term is distributed in I, but in O the predicate is.")],
          "O ('Some S are not P') distributes only its predicate: the students in question are outside all athletes.",
          "Distribution of terms", "Concept", "Which form is this, and which terms does it distribute?"),
        Q("'Only members may vote' is best put in standard form as", "All persons who may vote are members.",
          [("All members are persons who may vote.", "This reverses the sentence: it claims every member may vote."),
           ("Some members may vote.", "The sentence is universal about voters, not particular."),
           ("No members may vote.", "This contradicts the sentence.")],
          "'Only S are P' becomes 'All P are S': everyone who may vote is a member.", "Translating into standard form", "Application",
          "Who is described by 'all'?"),
        Q("'Not all candidates passed' is equivalent to the standard form", "Some candidates are not persons who passed. (O)",
          [("No candidates are persons who passed. (E)", "'Not all' does not say none."),
           ("All candidates are persons who did not pass. (A)", "This says every candidate failed."),
           ("Some candidates are persons who passed. (I)", "This is a different proposition; it neither contradicts nor equals 'not all passed'.")],
          "The contradictory of 'All S are P' is 'Some S are not P'.", "Translating into standard form", "Application",
          "What is the contradictory of 'all'?"),
        Q("Panel 3 of the diagram shows two circles S and P with an X in the part of S outside P. Panel 3 represents",
          "Some S are not P (O)",
          [("No S are P (E)", "E shades the overlap; it contains no X."),
           ("All S are P (A)", "A shades the part of S outside P instead of placing an X there."),
           ("Some S are P (I)", "I places the X in the overlap.")],
          "An X in S outside P says that at least one S is not P: form O.", "Venn diagrams of A, E, I and O", "Interpretation",
          "Where is the X placed?", diagram="alpsl2-aeio-venn-q.svg",
          alt="Four two-circle Venn diagrams labelled Panel 1 to Panel 4; panel 1 has the overlap shaded, panel 2 has S outside P shaded, panel 3 has an X in S outside P, panel 4 has an X in the overlap."),
        N("Count the distributed terms altogether in these three propositions: All S are P; No S are P; Some S are not P.", 4,
          [("A", "All S are P: S distributed, 1."), ("E", "No S are P: both, 2."), ("O", "Some S are not P: P only, 1."), ("Total", "1 + 2 + 1 = 4.")],
          "Distribution of terms", "Calculation", "Use the distribution table: A one, E two, I none, O one."),
        Q("Which statement about validity is correct?", "A valid argument can have a false conclusion if at least one premise is false.",
          [("A valid argument always has a true conclusion.", "Validity only says that true premises would force a true conclusion."),
           ("An argument with false premises is invalid.", "Invalid depends on form, not on the truth of the premises."),
           ("A sound argument has at least one false premise.", "A sound argument is valid with all premises true.")],
          "Validity concerns form: it is impossible for the premises to be true and the conclusion false.",
          "Argument, validity, soundness", "Concept", "Does validity depend on the facts or on the form?"),
    ], seed=11)))

# ---------------------------------------------------------------- 2. Square of opposition and immediate inferences
SETS.append(practice_set(
    module=M4, topic="The square of opposition and immediate inferences", title="Opposition, conversion, obversion and contraposition",
    lesson="psl2-square-immediate-inferences",
    questions=build([
        Q("The contradictory of 'All traders are honest' is", "Some traders are not honest.",
          [("No traders are honest.", "This is the contrary of A: both can be false."),
           ("Some traders are honest.", "This is the subaltern of A; it is compatible with A."),
           ("All honest persons are traders.", "This reverses the terms and is not an opposition.")],
          "A and O are contradictories: exactly one is true.", "Contradictories", "Recall", "Which form is the exact denial of A?"),
        Q("If 'No S are P' is true, then 'Some S are P' is", "false",
          [("true", "E and I are contradictories: they cannot both be true."),
           ("undetermined", "Contradictories always determine each other."),
           ("true only if S is empty", "Emptiness of S is a Boolean complication and does not make I true.")],
          "E and I are contradictories on the square.", "Square of opposition", "Concept", "E and I stand diagonally on the square."),
        Q("If 'Some students are absent' (I) is false, then 'All students are absent' (A) is", "false",
          [("true", "If the particular is false, its universal (superaltern) is false."),
           ("undetermined", "Subalternation fixes this case: A cannot be true if I is false."),
           ("true only if the class is empty", "On the traditional square, terms have members.")],
          "A implies I; so if I is false, A is false (and also E is true, O true).", "Subalternation", "Reasoning",
          "A being true would make I true."),
        Q("The simple converse of 'No tortoise is quick' is", "No quick thing is a tortoise.",
          [("Some quick things are not tortoises.", "This is a different (weaker) proposition."),
           ("All tortoises are slow.", "This is an obverse-like change, not a converse."),
           ("No non-quick thing is a non-tortoise.", "This is a contrapositive-style form.")],
          "E converts simply: the subject and predicate swap and the form is unchanged.", "Conversion", "Application", "Swap the terms only."),
        Q("The obverse of 'All dogs are mammals' is", "No dogs are non-mammals.",
          [("All mammals are dogs.", "This converts A simply, a fallacy."),
           ("Some dogs are mammals.", "This is subalternation, not obversion."),
           ("All non-mammals are non-dogs.", "That is the contrapositive.")],
          "Obversion changes the quality (A to E) and replaces the predicate by its complement.", "Obversion", "Application",
          "Change the quality and complement the predicate."),
        Q("The contrapositive of 'All S are P' is", "All non-P are non-S.",
          [("All P are S.", "This is an invalid simple converse."),
           ("No S are non-P.", "This is the obverse."),
           ("Some non-S are non-P.", "This does not follow as a contrapositive and is unrelated.")],
          "Contraposition replaces the subject by non-P and the predicate by non-S: A stays A.", "Contraposition", "Application",
          "Complement both terms and interchange them."),
        Q("Which of the following is NOT a valid immediate inference?", "From 'Some S are not P' to 'Some P are not S'",
          [("From 'No S are P' to 'No P are S'", "This is valid simple conversion of E."),
           ("From 'Some S are P' to 'Some P are S'", "This is valid simple conversion of I."),
           ("From 'All S are P' to 'No S are non-P'", "This is valid obversion.")],
          "O has no valid conversion: 'Some animals are not dogs' does not give 'Some dogs are not animals'.",
          "Conversion", "Reasoning", "Try a concrete example with animals and dogs."),
        N("On the traditional square, how many of the six pairs of corners (A-E, A-I, A-O, E-I, E-O, I-O) can NOT both be true?", 3,
          [("A and E", "Contraries: not both true."), ("A and O", "Contradictories: not both true."), ("E and I", "Contradictories: not both true."),
           ("Others", "A-I, E-O and I-O can both be true. Total 3.")],
          "Square of opposition", "Reasoning", "Check each pair: contraries and contradictories cannot both be true."),
    ], seed=12)))

# ---------------------------------------------------------------- 3. The categorical syllogism
SETS.append(practice_set(
    module=M4, topic="The categorical syllogism", title="Figures, moods, rules and Venn tests",
    lesson="psl2-categorical-syllogism",
    questions=build([
        Q("In 'All nurses are graduates. Some women are nurses. Therefore some women are graduates', the middle term is", "nurses",
          [("women", "'Women' is the minor term (subject of the conclusion)."),
           ("graduates", "'Graduates' is the major term (predicate of the conclusion)."),
           ("some", "A quantifier is not a term.")],
          "The middle term occurs in both premises and not in the conclusion.", "Terms of a syllogism", "Recall", "Which term is missing from the conclusion?"),
        Q("'No reptiles are mammals. All snakes are reptiles. Therefore no snakes are mammals.' has mood and figure", "EAE in figure 1",
          [("AEE in figure 1", "The major premise is E and the minor is A: the letters are E then A."),
           ("EAE in figure 2", "The middle term is subject of the major and predicate of the minor: figure 1."),
           ("EIO in figure 1", "There is no particular proposition in this syllogism.")],
          "Major: No M are P (E). Minor: All S are M (A). Conclusion: No S are P (E). M-P, S-M: figure 1 (Celarent).",
          "Mood and figure", "Application", "Write major premise first, then read the letters."),
        Q("'All cats are animals. All dogs are animals. Therefore all dogs are cats.' commits the fallacy of", "undistributed middle",
          [("illicit minor", "'Dogs' is distributed in the conclusion and in the minor premise (subject of A)."),
           ("illicit major", "'Cats' is the predicate of an A conclusion: undistributed, so no illicit major."),
           ("exclusive premises", "Both premises are affirmative.")],
          "The middle term 'animals' is the predicate of two A propositions, distributed in neither.", "Fallacies of the syllogism", "Application",
          "Where does the middle term stand in each premise?"),
        Q("'All dogs are mammals. No cat is a dog. Therefore no cat is a mammal.' commits the fallacy of", "illicit major",
          [("illicit minor", "'Cats' is distributed in the conclusion and also as subject of the E minor premise."),
           ("undistributed middle", "'Dogs' is the subject of A in the major premise: distributed."),
           ("four terms", "There are three terms: cats, dogs, mammals.")],
          "'Mammals' is distributed in the negative conclusion but is the predicate of an A premise: undistributed. Illicit process of the major term.",
          "Fallacies of the syllogism", "Application", "Which term is distributed in the conclusion but not in its premise?"),
        Q("The diagram shades the regions known to be empty after two premises are drawn. The conclusion about S and P that can be read off is",
          "No S are P",
          [("All S are P", "The part of S outside P is not wholly shaded."),
           ("Some S are P", "The overlap of S and P is shaded: it is empty."),
           ("Some S are not P", "The part of S outside P that lies in M is not shaded, so nothing is proved there.")],
          "All regions where S and P overlap (inside M and outside M) are shaded, so there are no S that are P.",
          "Venn tests of syllogisms", "Interpretation", "Look at the overlap of S and P: is any of it unshaded?",
          diagram="alpsl2-venn-premises-q.svg",
          alt="Three-circle Venn diagram of S, P and M. The part of S outside M is shaded and the overlap of M and P is shaded."),
        N("How many valid syllogistic forms are there in all four figures when the traditional assumption is made that the classes are not empty?", 24,
          [("Count", "Checking all 256 forms against every arrangement of non-empty classes leaves 24 valid forms.")],
          "Valid forms of the syllogism", "Recall", "Recall the total of valid forms in the traditional list."),
        Q("Which pair of premises can give a valid conclusion?", "All M are P; some S are M",
          [("No M are P; no S are M", "Two negative premises give no conclusion."),
           ("Some M are P; some S are M", "Two particular premises give no conclusion."),
           ("All P are M; all S are M", "The middle term is the predicate of two A premises: undistributed.")],
          "AI in figure 1 gives 'Some S are P' (Darii).", "Rules of the syllogism", "Reasoning", "Check each pair against the rules about quality, quantity and the middle term."),
        Q("'All lawyers are literate, and Ada is a lawyer.' This enthymeme omits the conclusion and is of the", "third order",
          [("first order", "First order omits the major premise."),
           ("second order", "Second order omits the minor premise."),
           ("fourth order", "There are only three orders.")],
          "Both premises are given, so the missing proposition is the conclusion: third order.", "Enthymeme and sorites", "Recall",
          "Which proposition is not stated?"),
    ], seed=13)))

# ---------------------------------------------------------------- 4. Hypothetical and disjunctive syllogisms and dilemmas
SETS.append(practice_set(
    module=M4, topic="Hypothetical and disjunctive syllogisms and dilemmas", title="Conditional, either-or and dilemma arguments",
    lesson="psl2-hypothetical-disjunctive-dilemma",
    questions=build([
        Q("'If it rains, the match is cancelled. The match was not cancelled. So it did not rain.' is", "modus tollens",
          [("modus ponens", "Modus ponens affirms the antecedent; here the consequent is denied."),
           ("affirming the consequent", "The consequent is denied, not affirmed."),
           ("denying the antecedent", "The antecedent is not denied in a premise; it is the conclusion.")],
          "If A then B; not B; therefore not A.", "Modus ponens and modus tollens", "Recall", "Which part of the conditional is denied in the second premise?"),
        Q("'If the road is flooded, the bus is late. The bus is late. So the road is flooded.' is", "invalid: it affirms the consequent",
          [("valid: modus ponens", "Modus ponens affirms the antecedent, not the consequent."),
           ("valid: modus tollens", "Modus tollens denies the consequent."),
           ("invalid: it denies the antecedent", "The second premise affirms a part; the antecedent is not denied.")],
          "The bus may be late for other reasons (a breakdown). The conditional makes flooding sufficient, not necessary.",
          "Fallacies of conditional arguments", "Application", "Is flooding the only way for the bus to be late?"),
        Q("'Either the exam was difficult or the candidates were lazy. The candidates were not lazy.' The conclusion of the valid disjunctive syllogism is",
          "The exam was difficult.",
          [("The exam was easy.", "Nothing is said about the exam being easy; the disjunction gives only 'difficult'."),
           ("The candidates were lazy.", "This contradicts the second premise."),
           ("The exam was difficult and the candidates were lazy.", "This is a conjunction that contradicts the denial of laziness.")],
          "Deny one alternative and affirm the other.", "Disjunctive syllogism", "Application", "Which alternative has been removed?"),
        Q("'The match is cancelled only if it rains' means", "If the match is cancelled, then it rains.",
          [("If it rains, the match is cancelled.", "That is 'cancelled if it rains', the other direction."),
           ("The match is cancelled if and only if it rains.", "'Only if' gives one direction, not both."),
           ("It never rains when the match is cancelled.", "This contradicts the sentence.")],
          "'A only if B' means 'If A then B'; here A is cancellation and B is rain.", "Conditional proposition", "Concept",
          "Which condition is necessary for which?"),
        Q("Which of the following is a counterexample to the argument 'If Ada studies, she passes. Ada did not study. So Ada did not pass'?",
          "Ada did not study but passed because she already knew the material.",
          [("Ada studied and passed.", "This makes both the antecedent and the consequent true; the premise 'did not study' is false in this case."),
           ("Ada did not study and failed.", "This is consistent with the conclusion: not a counterexample."),
           ("Ada studied and failed.", "This breaks the first premise, not a counterexample to the form.")],
          "A counterexample makes the premises true and the conclusion false: antecedent false, consequent true.",
          "Fallacies of conditional arguments", "Reasoning", "Premises true, conclusion false: what values do they need?"),
        Q("'If A then C. If B then D. Either A or B. Therefore either C or D.' is a", "complex constructive dilemma",
          [("simple constructive dilemma", "In a simple dilemma the consequents are the same."),
           ("complex destructive dilemma", "A destructive dilemma denies consequents."),
           ("pure hypothetical syllogism", "A pure hypothetical syllogism has only conditionals.")],
          "The consequents differ (C, D) and the antecedents are affirmed: complex constructive.", "Kinds of dilemma", "Recall",
          "Are the consequents the same or different? Are antecedents affirmed or consequents denied?"),
        Q("Replying to a dilemma by denying one of its conditional premises is called", "grasping the horns",
          [("escaping between the horns", "That denies the disjunctive premise."),
           ("rebutting the dilemma", "A rebuttal offers a counter-dilemma."),
           ("affirming the consequent", "That is an invalid form of argument, not a reply.")],
          "Grasping the horns attacks a conditional premise; escaping attacks the disjunction.", "Meeting a dilemma", "Recall",
          "Which premise is attacked: the conditional or the either-or?"),
        N("Of the four mixed hypothetical forms (affirming the antecedent, denying the consequent, affirming the consequent, denying the antecedent), how many are valid?", 2,
          [("Valid", "Affirming the antecedent (modus ponens) and denying the consequent (modus tollens)."),
           ("Invalid", "Affirming the consequent and denying the antecedent. Total valid: 2.")],
          "Mixed hypothetical syllogisms", "Recall", "Name the two valid forms."),
    ], seed=14)))

# ---------------------------------------------------------------- 5. Informal fallacies
SETS.append(practice_set(
    module=M4, topic="Informal fallacies", title="Recognising and explaining informal fallacies",
    lesson="psl2-informal-fallacies",
    questions=build([
        Q("'You cannot trust her plan because she once failed an exam.' The fallacy is", "argument against the person (ad hominem)",
          [("appeal to force", "No threat is made."),
           ("false cause", "No cause is claimed."),
           ("equivocation", "No word shifts meaning.")],
          "The premise concerns the person's past, not the merits of the plan.", "Fallacies of relevance", "Application", "What is the premise about: the plan or the person?"),
        Q("'Everyone in town buys this phone, so it is the best phone.' The fallacy is", "appeal to the people (ad populum)",
          [("appeal to authority", "No expert is cited."),
           ("hasty generalisation", "No general rule is drawn from a few cases; popularity is used as proof."),
           ("begging the question", "The conclusion is not simply restated in the premise.")],
          "Popularity is offered as proof of quality.", "Fallacies of relevance", "Application", "What reason is given for quality?"),
        Q("'The captain is always right, because what the captain says is always correct.' The fallacy is", "begging the question",
          [("equivocation", "The two phrases mean the same, not different things."),
           ("false cause", "No causal claim is made."),
           ("composition", "No part-to-whole inference is made.")],
          "The premise just restates the conclusion in other words.", "Fallacies of presumption", "Application", "Does the premise say anything new?"),
        Q("'Every time Ada wears her blue scarf to a test, she passes; so the scarf makes her pass.' The fallacy is", "false cause (post hoc)",
          [("composition", "No part-to-whole reasoning."),
           ("ad hominem", "No person is attacked."),
           ("appeal to ignorance", "No claim rests on lack of proof.")],
          "Succession is treated as causation without any evidence of a link.", "Fallacies of presumption", "Application", "What is assumed from the order of events?"),
        Q("'Nothing is better than good health. A cold drink is better than nothing. So a cold drink is better than good health.' The fallacy is",
          "equivocation",
          [("division", "The argument does not go from whole to parts."),
           ("false dilemma", "No either-or is offered."),
           ("missing the point", "The conclusion is drawn from the premises' words, not a different issue.")],
          "'Nothing' means 'no thing' in the first premise and 'the absence of anything' in the second.", "Fallacies of ambiguity", "Application",
          "Does the key word keep one meaning?"),
        Q("'Each player is excellent, so the team is excellent.' is a fallacy of", "composition",
          [("division", "Division goes from the whole to the parts."),
           ("accent", "No emphasis changes the meaning."),
           ("amphiboly", "The sentence has only one reading.")],
          "What is true of the parts is wrongly said to be true of the whole.", "Fallacies of ambiguity", "Application",
          "Does the reasoning move from parts to whole or whole to parts?"),
        Q("'Two taxis were late, so all taxis in this town are late.' is", "hasty generalisation",
          [("accident", "Accident applies a general rule to a case it was not meant for."),
           ("false dilemma", "No two alternatives are offered."),
           ("appeal to pity", "No sympathy is invoked.")],
          "A general claim is drawn from too few cases.", "Fallacies of presumption", "Application", "How many cases support the general claim?"),
        Q("Which is NOT necessarily a fallacy?", "Citing a recognised medical expert about a disease in her field",
          [("Citing a famous footballer about cancer treatment", "An authority outside his field: appeal to authority fallacy."),
           ("Saying 'Nobody has proved it is unsafe, so it is safe'", "Appeal to ignorance."),
           ("Saying 'Everyone is doing it, so it is right'", "Appeal to the people.")],
          "Expertise within the field is relevant, though not infallible.", "Fallacies of relevance", "Reasoning",
          "Is the authority qualified to speak on this subject?"),
    ], seed=15)))

# ---------------------------------------------------------------- 6. Propositional variables and connectives
SETS.append(practice_set(
    module=M5, topic="Propositional variables and connectives", title="Connectives, symbolisation and main connectives",
    lesson="psl2-variables-connectives",
    questions=build([
        Q("The main connective of ~(p · q) ⊃ r is", "⊃ (the conditional)",
          [("~ (negation)", "The negation applies only to the bracket (p · q)."),
           ("· (conjunction)", "The conjunction is inside the bracket."),
           ("r", "A letter is not a connective.")],
          "The conditional joins ~(p · q) and r; it is the last connective applied.", "Main connective", "Concept", "Which connective joins the two big parts?"),
        Q("'Ada passes only if she studies' (P: she passes; S: she studies) is", "P ⊃ S",
          [("S ⊃ P", "That says studying guarantees passing: the 'if' reading."),
           ("P · S", "That says both are true."),
           ("P ≡ S", "'Only if' gives one direction; ≡ gives both.")],
          "'Only if' marks a necessary condition: passing requires studying.", "Symbolising conditionals", "Application", "Which is the necessary condition?"),
        Q("'Neither Ada nor Ngu passed' (A, N) is", "~A · ~N",
          [("~(A · N)", "That says only that they did not both pass."),
           ("~A v ~N", "That says at least one failed."),
           ("A v N", "That says at least one passed.")],
          "Both failed: not-A and not-N.", "Symbolising negations", "Application", "How many people failed?"),
        N("In how many of the four rows of its truth table is p ⊃ q false?", 1,
          [("Rule", "A conditional is false only when the antecedent is true and the consequent false."), ("Count", "Row p true, q false: 1 row.")],
          "Truth conditions of connectives", "Calculation", "When is a conditional broken?"),
        Q("'Not both Ada and Ngu passed' is", "~(A · N)",
          [("~A · ~N", "That says both failed."),
           ("~A v N", "This is a different compound."),
           ("A · N", "This is the denial of the sentence.")],
          "'Not both' negates the conjunction.", "Symbolising negations", "Application", "Which connective is negated?"),
        Q("'Ada passes unless she is ill' (P, I) is best symbolised as", "P v I",
          [("P · I", "That says she passes and is ill."),
           ("P ⊃ I", "That says if she passes, then she is ill."),
           ("~P v ~I", "That is 'not both'.")],
          "'A unless B' means 'if not B then A', equivalent to A v B.", "Symbolising 'unless'", "Application", "Rewrite 'unless' as 'if not'."),
        Q("'Either the bus is late or the driver is ill, but not both' (B, D) is", "(B v D) · ~(B · D)",
          [("B v D", "This allows both."),
           ("B · D", "This says both."),
           ("~(B v D)", "This says neither.")],
          "Exclusive or: at least one, and not both.", "Exclusive disjunction", "Application", "Combine 'or' and 'not both'."),
        Q("When p is false and q is true, the conditional p ⊃ q is", "true",
          [("false", "A conditional is false only with a true antecedent and false consequent."),
           ("undefined", "A truth-functional connective always has a value."),
           ("the same as q ⊃ p", "Here q ⊃ p is false: they differ.")],
          "A false antecedent leaves the promise unbroken.", "Truth conditions of connectives", "Concept", "Is the promise broken?"),
    ], seed=16)))

# ---------------------------------------------------------------- 7. Truth tables
SETS.append(practice_set(
    module=M5, topic="Truth tables", title="Building and using truth tables",
    lesson="psl2-truth-tables",
    questions=build([
        N("How many rows does a complete truth table need for a formula with four different variables?", 16,
          [("Rule", "Each variable doubles the rows."), ("Count", "2 x 2 x 2 x 2 = 16.")],
          "Rows of a truth table", "Calculation", "Two to the power of the number of variables."),
        N("In how many of the four rows of its truth table is p v ~q true?", 3,
          [("Rows", "TT: T v F = T. TF: T v T = T. FT: F v F = F. FF: F v T = T."), ("Count", "True in 3 rows.")],
          "Evaluating compound statements", "Calculation", "Evaluate row by row."),
        Q("For the argument 'p ⊃ q; q; therefore p', the counterexample row is", "p false, q true",
          [("p true, q true", "Here the conclusion p is true: no counterexample."),
           ("p true, q false", "The premise q is false here."),
           ("p false, q false", "The premise q is false here.")],
          "p ⊃ q is true, q is true and the conclusion p is false only when p is false and q is true.", "Testing validity by truth table", "Reasoning",
          "You need both premises true and the conclusion false."),
        Q("Which of the following arguments is valid?", "p v q; ~p; therefore q",
          [("p ⊃ q; ~p; therefore ~q", "Denying the antecedent: row p false, q true is a counterexample."),
           ("p ⊃ q; q; therefore p", "Affirming the consequent: invalid."),
           ("p v q; p; therefore ~q", "Valid only for exclusive 'or'; with inclusive v the row p true, q true is a counterexample.")],
          "In the only row where p v q and ~p are both true (p false, q true) the conclusion q is true.",
          "Testing validity by truth table", "Reasoning", "Look for a row with true premises and a false conclusion in each."),
        N("In how many rows of the truth table of ~(p v q) ⊃ r is the whole statement false?", 1,
          [("Rule", "A conditional is false only with a true antecedent and false consequent."),
           ("Rows", "~(p v q) is true only when p and q are both false; with r false: p F, q F, r F. One row.")],
          "Truth table of a compound", "Calculation", "When is ~(p v q) true, and what must r be?"),
        Q("To test 'p ⊃ q; r ⊃ s; p v r; therefore q v s' by the indirect method, we assume the conclusion false. The result is",
          "p and r are forced false, so p v r is false: a contradiction, and the argument is valid",
          [("q and s are forced true, so the argument is invalid", "Assuming q v s false makes q and s false, not true."),
           ("a consistent assignment, so the argument is invalid", "The assignment contradicts the premise p v r."),
           ("nothing is forced, so the test fails", "q and s false force p and r false.")],
          "q F and s F; p ⊃ q true forces p F; r ⊃ s true forces r F; then p v r is F, contradicting the premise.",
          "Indirect truth table method", "Reasoning", "Assume the conclusion false and see what the conditionals force."),
        Q("When p is true, q is true and r is false, the value of p ⊃ (q ⊃ r) is", "false",
          [("true", "The inner conditional q ⊃ r is false (true antecedent, false consequent), so p ⊃ (false) with p true is false."),
           ("true, because p is true", "A true antecedent does not make the whole conditional true."),
           ("cannot be found without more rows", "A single assignment gives a value.")],
          "q ⊃ r is F; p ⊃ F with p true is F.", "Evaluating compound statements", "Calculation", "Evaluate the inner bracket first."),
        Q("In the table for 'p ⊃ q; q ⊃ r; therefore p ⊃ r', the conclusion is false in two rows. This does not make the argument invalid because",
          "in each of those rows at least one premise is also false",
          [("the conclusion is true in the other rows", "Validity concerns the rows with true premises."),
           ("a false conclusion is always acceptable", "It is acceptable only when some premise is false."),
           ("the table has too many rows", "The number of rows does not decide validity.")],
          "Rows 2 and 4: in row 2 the second premise is false; in row 4 the first premise is false.", "Testing validity by truth table", "Reasoning",
          "Check the premises in the rows where the conclusion is false."),
    ], seed=17)))

# ---------------------------------------------------------------- 8. Tautologies, contradictions, contingencies
SETS.append(practice_set(
    module=M5, topic="Tautologies, contradictions and contingencies", title="Classifying statement forms and equivalences",
    lesson="psl2-tautology-contradiction-contingency",
    questions=build([
        Q("The statement form p v ~p is", "a tautology",
          [("a contradiction", "A contradiction is false in every row; this is true in every row."),
           ("a contingency", "A contingency has some false rows."),
           ("equivalent to p", "It is true even when p is false.")],
          "One of p and ~p is always true.", "Tautologies", "Concept", "Try p true and p false."),
        Q("The statement form p · ~p is", "a contradiction",
          [("a tautology", "It is never true."),
           ("a contingency", "It is false in every row."),
           ("equivalent to p v ~p", "These have opposite values in every row.")],
          "p and ~p cannot both be true.", "Contradictions", "Concept", "Can a statement and its negation be true together?"),
        Q("The form p ⊃ q is", "contingent",
          [("a tautology", "It is false when p is true and q false."),
           ("a contradiction", "It is true in three rows."),
           ("equivalent to q ⊃ p", "The converse has a different column (false when p false, q true).")],
          "Column T, F, T, T: both values occur.", "Contingencies", "Concept", "Read the final column of its table."),
        Q("(p · q) ⊃ p is", "a tautology",
          [("a contingency", "The column is T, T, T, T."),
           ("a contradiction", "It is never false."),
           ("false when p is false", "With p false the antecedent p · q is also false, so the conditional is true.")],
          "A conjunction implies each of its parts.", "Tautologies", "Reasoning", "When is the consequent false? What happens to the antecedent then?"),
        Q("Which is equivalent to ~(p v q)?", "~p · ~q",
          [("~p v ~q", "That is the equivalent of ~(p · q)."),
           ("~p · q", "q is not negated."),
           ("p · q", "This is the opposite of 'neither'.")],
          "De Morgan: not (p or q) is not-p and not-q.", "De Morgan's laws", "Application", "'Neither p nor q'."),
        N("In how many of the four rows of its truth table is p ≡ ~q true?", 2,
          [("Rows", "TT: T and F differ, F. TF: T and T, T. FT: F and F, T. FF: F and T differ, F."), ("Count", "True in 2 rows.")],
          "Truth conditions of the biconditional", "Calculation", "≡ is true when both sides have the same value."),
        Q("An argument is valid exactly when", "the conditional of the conjunction of its premises and its conclusion is a tautology",
          [("its premises are all tautologies", "Validity does not require tautological premises."),
           ("its conclusion is a tautology", "A tautologous conclusion makes any argument valid, but it is not required."),
           ("its premises and conclusion are all true", "Truth of the actual statements is not required for validity.")],
          "A counterexample row is exactly a row where that conditional is false.", "Validity and tautologies", "Concept",
          "Link counterexample rows with a false conditional."),
        Q("Which pair is logically equivalent?", "p ⊃ q and ~q ⊃ ~p",
          [("p ⊃ q and q ⊃ p", "These are converses, not equivalent."),
           ("p ⊃ q and ~p ⊃ ~q", "This is the inverse, not equivalent."),
           ("~(p · q) and ~p · ~q", "De Morgan changes the connective: ~(p · q) is ~p v ~q.")],
          "Transposition: a conditional is equivalent to its contrapositive.", "Logical equivalence", "Application",
          "Which form is the contrapositive of p ⊃ q?"),
    ], seed=18)))

# ---------------------------------------------------------------- 9. Formal proofs of validity
SETS.append(practice_set(
    module=M5, topic="Formal proofs of validity", title="Rules of inference and replacement in proofs",
    lesson="psl2-formal-proofs",
    questions=build([
        Q("From the lines p ⊃ q and p, the line q is justified by", "modus ponens",
          [("modus tollens", "Modus tollens needs ~q."),
           ("disjunctive syllogism", "There is no disjunction."),
           ("simplification", "Simplification needs a conjunction.")],
          "If p then q; p; therefore q.", "Rules of inference", "Application", "Which part of the conditional is affirmed?"),
        Q("From p v q and ~p, the line q is justified by", "disjunctive syllogism",
          [("modus ponens", "There is no conditional."),
           ("addition", "Addition makes a disjunction from one statement."),
           ("constructive dilemma", "That needs two conditionals.")],
          "Deny one alternative to affirm the other.", "Rules of inference", "Application", "What kind of statement is p v q?"),
        Q("From p ⊃ q and q ⊃ r, the line p ⊃ r is justified by", "hypothetical syllogism",
          [("modus ponens", "No premise affirms an antecedent."),
           ("transposition", "Transposition rewrites one conditional."),
           ("exportation", "Exportation moves a conjunction into a conditional.")],
          "A chain of conditionals gives a conditional.", "Rules of inference", "Application", "Two conditionals share a middle statement."),
        Q("From ~(p · q), the line ~p v ~q is justified by", "De Morgan's rule",
          [("Implication", "Implication changes a conditional into a disjunction."),
           ("Commutation", "Commutation only swaps the order of the parts."),
           ("Double negation", "Double negation adds or removes ~~.")],
          "The negation of a conjunction becomes the disjunction of the negations.", "Rules of replacement", "Application", "Which rule changes the connective when a negation passes through?"),
        Q("Which of the following is NOT a legitimate step?", "From p ⊃ q and q, conclude p",
          [("From p ⊃ q and ~q, conclude ~p", "This is modus tollens."),
           ("From p · q, conclude q", "This is simplification (the second conjunct)."),
           ("From p, conclude p v r", "This is addition.")],
          "Affirming the consequent is an invalid form, so no rule of inference corresponds to it.", "Rules of inference", "Reasoning",
          "Which step is a fallacy from the earlier lessons?"),
        N("What is the least number of lines (after the premises) needed to prove q from the premises p ⊃ q and p · r?", 2,
          [("Line 3", "p, by simplification on p · r."), ("Line 4", "q, by modus ponens on lines 1 and 3. Two lines.")],
          "Planning a proof", "Reasoning", "Take p out of p · r first."),
        Q("Given the premises (p ⊃ q) · r and p, a student writes q by modus ponens. The error is", "an inference rule was applied to part of a line",
          [("modus ponens needs a disjunction", "Modus ponens uses a conditional."),
           ("the conclusion is not valid", "q does follow validly: first p ⊃ q by Simp, then q by MP."),
           ("p was not a premise", "p is a premise.")],
          "p ⊃ q is only one conjunct of line 1. It must first be extracted by simplification.", "Using rules correctly", "Reasoning",
          "Is p ⊃ q a whole line?"),
        Q("In the proof of ~r from ~(p v q) and r ⊃ p, the line ~p · ~q is justified by", "De Morgan's rule applied to line 1",
          [("simplification on line 1", "Line 1 is a negation, not a conjunction."),
           ("hypothetical syllogism on lines 1 and 2", "The lines do not form a chain."),
           ("modus tollens on lines 1 and 2", "Line 1 is not a conditional.")],
          "Not (p or q) becomes not-p and not-q. Then Simp gives ~p, and MT with r ⊃ p gives ~r.", "Planning a proof", "Application",
          "What shape does line 1 have?"),
    ], seed=19)))

# ---------------------------------------------------------------- 10. Paper 1 lesson set
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 technique: stems, distractors and logic items",
    lesson="psl2-paper1-multiple-choice",
    questions=build([
        Q("The best first step with a multiple-choice question is to", "read the stem, note the command word and predict an answer",
          [("read the options and pick the one with a famous name", "A famous name is a common distractor."),
           ("choose the longest option", "Length is not a reliable clue."),
           ("leave it for the end if it names a philosopher", "Questions naming a philosopher are often straightforward recall.")],
          "Predict before you look at the options so that distractors do not steer you.", "Multiple-choice technique", "Application", "What should you do before reading the options?"),
        Q("An option that states a true doctrine but belongs to a different philosopher is an example of", "the right idea, wrong thinker",
          [("the group generalisation", "A group generalisation attributes one thinker's view to a school."),
           ("the reversal", "A reversal states the opposite position."),
           ("the look-alike term", "A look-alike term is a word that sounds like the correct one.")],
          "Plato's Forms offered as Aristotle's theory is a typical case.", "Distractors in philosophy", "Concept", "Is the doctrine false, or just wrongly attributed?"),
        Q("The change from 'S is P' to 'non-P is non-S' is called", "contraposition",
          [("conversion", "Conversion only swaps the terms."),
           ("obversion", "Obversion changes quality and complements only the predicate."),
           ("contrariety", "Contrariety is a relation on the square of opposition, not an eduction.")],
          "Complement both terms and interchange them.", "Traditional Formal Logic", "Recall", "Both terms are complemented and swapped."),
        Q("The final column of a truth table reads T, T, T, T. The statement is", "a tautology",
          [("a contradiction", "A contradiction has only F."),
           ("a contingency", "A contingency has both T and F."),
           ("an equivalence", "Equivalence is a relation between two statements.")],
          "All rows true.", "Symbolic / Propositional Logic", "Interpretation", "Look only at the final column."),
        N("If the KKEVO Paper 1 mock has 50 questions in 90 minutes, how many minutes per question is that on average?", 1.8,
          [("Divide", "90 / 50 = 1.8 minutes (1 minute 48 seconds).")], "Time management", "Calculation", "Total time over the number of questions.", tol=0.05, unit="minutes"),
        Q("A stem asks which module deals with dilemmas and the rule of the disjunctive syllogism. The module is", "Traditional Formal Logic",
          [("Symbolic / Propositional Logic", "Dilemmas and conditional and disjunctive syllogisms are in the traditional logic module here, though they use statement logic."),
           ("Modern Western Philosophy", "This module covers rationalism, empiricism, the social contract and Kant."),
           ("Nature, Origins & Methods of Philosophy", "This module covers myth and logos, branches and methods of philosophy.")],
          "Topic list: hypothetical and disjunctive syllogisms and dilemmas belong to Traditional Formal Logic.", "Revision planning", "Recall",
          "Check the topic list of the logic modules."),
        Q("The Board's 2023 report advises that questions should be evaluated on", "individual philosophers, not groups",
          [("schools of thought, not individuals", "The report says the opposite."),
           ("dates, not ideas", "Ideas are tested, with dates secondary."),
           ("popular opinion", "The report does not advise this.")],
          "Learn each thinker's own view; answers about groups are often wrong for individual members.", "Multiple-choice technique", "Concept",
          "Think of the report's advice on attribution."),
        Q("A student cannot decide between two options after two minutes. A sensible action is to", "mark the best guess, move on and return later",
          [("leave the answer blank forever", "A blank cannot score."),
           ("spend ten more minutes on it", "That costs time for other questions."),
           ("change all other answers", "That is pointless and risky.")],
          "Time is limited, so guess, mark and return.", "Time management", "Application", "How do you protect time for the other questions?"),
    ], seed=21)))

# ---------------------------------------------------------------- 11. Paper 2 lesson set
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 technique: essays and textual analysis",
    lesson="psl2-paper2-essays-textual-analysis",
    questions=build([
        Q("According to the Board's 2023 report, Paper 2's Section 2 deals with", "African philosophy",
          [("Western philosophy", "That is Section 1."),
           ("textual analysis", "That is Section 3."),
           ("logic", "Logic is in Paper 3.")],
          "Section 1: Western philosophy; Section 2: African philosophy; Section 3: textual analysis.", "Structure of Paper 2", "Recall", "Recall the three sections in order."),
        Q("Which of the following is an internal critique of a thinker's position?", "Its premises contradict each other.",
          [("Another school rejects its conclusion.", "That is an external objection."),
           ("Modern science disagrees.", "That is an external objection from outside the system."),
           ("Few people accept it today.", "Popularity is not a critique.")],
          "Internal critique tests consistency, clarity and validity from within.", "Internal and external critique", "Concept", "Internal means from within the position."),
        Q("The first thing to do before planning an essay is to", "identify the command word, key terms, scope and problem",
          [("write the conclusion", "The conclusion depends on the analysis."),
           ("copy out everything you know about the topic", "That produces narration."),
           ("choose the longest quotation to learn", "Quotations are not required and are not the first step.")],
          "Question analysis shapes the whole essay.", "Reading a question", "Application", "What does the question actually ask?"),
        Q("An essay on the first principles of the Pre-Socratics lists each philosopher's view with no evaluation. Its main weakness is", "narration without critique",
          [("it is too short to be valid", "Length is not the main issue."),
           ("it mentions too many philosophers", "The weakness is the lack of argument, not the number."),
           ("it uses technical terms", "Technical terms are encouraged.")],
          "The examiners ask candidates to philosophise: expound, then evaluate.", "Essay writing", "Analysis", "What is missing after each exposition?"),
        Q("In the 2023 report, many candidates answered a question about the vital force by writing about witchcraft. The lesson is to", "answer the intent of the question",
          [("write on every related topic to be safe", "That diverts from the question."),
           ("avoid African philosophy", "The section is part of Paper 2."),
           ("use only the first word of the question", "The whole question must be read.")],
          "A relevant topic is not the same as the question asked.", "Reading a question", "Analysis", "Does the answer address what was asked?"),
        Q("In a commentary, the step that states the question the text answers is the", "problem",
          [("theme", "The theme is the general subject."),
           ("thesis", "The thesis is the author's answer."),
           ("situating the text", "Situating gives author, work and context.")],
          "Problem: the question; thesis: the answer.", "Textual analysis", "Concept", "Is it the question or the answer?"),
        Q("The Board's report says answers are marked by examiners using", "broken-down criteria that credit worthwhile attempts (item, task and skill)",
          [("one overall impression only", "The report describes segmented marking."),
           ("computer scoring", "Examiners mark the scripts."),
           ("the first paragraph only", "The whole answer is credited.")],
          "Segmented marking rewards each well-placed point.", "Marking of Paper 2", "Recall", "Recall what the report says about marking."),
        Q("A well-formed essay has", "an introduction stating the problem, a development with exposition and critique, and a conclusion that answers the problem",
          [("a conclusion only", "A bare conclusion shows no reasoning."),
           ("a list of definitions", "Definitions belong in the introduction, but are not the essay."),
           ("two expositions and no critique", "Critique is needed for analysis and evaluation.")],
          "Introduction, development, conclusion.", "Essay writing", "Concept", "How is the essay organised?"),
    ], seed=22)))

# ---------------------------------------------------------------- 12. Paper 3 lesson set
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 3", title="Paper 3 technique: logic problems and symbolisation",
    lesson="psl2-paper3-logic-problems",
    questions=build([
        Q("In the Board's 2023 report, Paper 3 Section 1 (Questions 1 to 3) is", "Logic",
          [("African philosophy", "That is in Paper 2."),
           ("textual analysis", "That is in Paper 2, Section 3."),
           ("Western philosophy essays", "Those are in Paper 2.")],
          "Section 1: Logic. Section 2: Philosophical Problems.", "Structure of Paper 3", "Recall", "Recall the two sections of Paper 3."),
        Q("The report advises that symbolisation should begin with", "a paraphrase of the sentence",
          [("the final symbols", "Starting with symbols causes structural errors."),
           ("a truth table", "A table comes after symbolisation."),
           ("naming a fallacy", "That belongs to informal arguments.")],
          "Analyse the sentence first, then build it up in symbols.", "Symbolisation", "Recall", "Where does the report say symbolisation starts?"),
        Q("The report says that constructing the truth table itself", "should be credited as an acquired skill",
          [("earns no marks without the verdict", "The report suggests that the mere construction should be credited."),
           ("is unnecessary if you can see the answer", "The table is the method."),
           ("should be omitted for three variables", "Three-variable tables are standard.")],
          "Show the whole table neatly; it earns credit by itself.", "Truth tables", "Recall", "What credit does the table earn?"),
        Q("'All students are candidates' in predicate notation (Sx, Cx) is", "(x)(Sx ⊃ Cx)",
          [("(x)(Sx · Cx)", "That says everything is both a student and a candidate."),
           ("(∃x)(Sx ⊃ Cx)", "That is true if anything is not a student."),
           ("(∃x)(Sx · Cx)", "That is the I form: some students are candidates.")],
          "Universal statements take the conditional.", "Quantifier notation", "Application", "A universal statement uses ⊃, not ·."),
        Q("'Only women are traders' (Wx: x is a woman; Tx: x is a trader) is", "(x)(Tx ⊃ Wx)",
          [("(x)(Wx ⊃ Tx)", "That says all women are traders."),
           ("(∃x)(Wx · Tx)", "That says some women are traders."),
           ("~(∃x)(Tx · Wx)", "That says no trader is a woman.")],
          "Whoever is a trader is a woman.", "Quantifier notation", "Application", "'Only' reverses the direction."),
        Q("'Some students are not candidates' in predicate notation is", "(∃x)(Sx · ~Cx)",
          [("(x)(Sx ⊃ ~Cx)", "That says no student is a candidate (E)."),
           ("(∃x)(Sx ⊃ ~Cx)", "Using ⊃ with ∃ is a standard error."),
           ("~(∃x)(Sx · ~Cx)", "That says every student is a candidate (A).")],
          "Some x is a student and not a candidate.", "Quantifier notation", "Application", "Particular statements use ∃ with ·."),
        Q("The examiners ask that a fallacy be explained", "in the context of the argument, not in general terms",
          [("in one word", "A word alone does not show understanding."),
           ("without examples", "Reference to the argument's content is needed."),
           ("only in symbols", "An informal fallacy has no symbols to show.")],
          "Show where the fallacy occurs in this argument.", "Informal fallacies", "Concept", "General definition or this case?"),
        N("The premises S ⊃ P, P ⊃ H and S are all true in how many rows of an eight-row truth table?", 1,
          [("Row S, P, H all true", "S true forces P true (first premise) and H true (second premise)."), ("Count", "Only that one row.")],
          "Truth tables", "Reasoning", "S is true, so what do the conditionals force?"),
    ], seed=23)))

# ---------------------------------------------------------------- Mock: Paper 1 mock exam A (50 multiple-choice questions)
_m1 = []
_b = _m1.append
_T = {
    "myth": "From myth to logos", "branch": "The branches of philosophy", "meth": "Philosophical methods",
    "pre": "The Pre-Socratics", "soph": "The Sophists and Socrates", "plato": "Plato", "arist": "Aristotle",
    "hell": "The Hellenistic schools", "augaq": "Augustine and Aquinas",
    "rat": "Rationalism", "emp": "British empiricism", "sc": "The social contract theorists", "kant": "Kant's critical philosophy and ethics",
    "terms": "Terms and categorical propositions", "sq": "The square of opposition and immediate inferences",
    "syl": "The categorical syllogism", "hyp": "Hypothetical and disjunctive syllogisms and dilemmas", "inf": "Informal fallacies",
    "var": "Propositional variables and connectives", "tt": "Truth tables", "tc": "Tautologies, contradictions and contingencies",
    "pf": "Formal proofs of validity",
}


def _q(topic, prompt, correct, wrongs, sol, skill="Recall", hint="Recall what the lesson taught about this topic."):
    _b(Q(prompt, correct, wrongs, sol, _T[topic], skill, hint))


# ---- Nature, Origins & Methods of Philosophy (7)
_q("myth", "The change 'from myth to logos' is best described as a move from", "explanations by stories of gods to explanations by reasons and argument",
   [("reason to superstition", "This reverses the direction of the change."),
    ("written laws to oral tradition", "The change concerns kinds of explanation, not writing."),
    ("philosophy to natural science only", "Philosophy itself began with this move.")],
   "Early Greek thinkers began to ask for natural explanations supported by reasons.")
_q("myth", "Which of the following is a function of myth in a traditional community?", "To express shared beliefs about origins and to support values and rituals",
   [("To test claims by controlled experiment", "Myth does not proceed by experiment."),
    ("To prove theorems from axioms", "That is a feature of mathematics."),
    ("To replace tradition with logic", "Myth carries tradition rather than replacing it.")],
   "Myths give a community its story of where the world and the people came from and why customs matter.")
_q("branch", "Epistemology is the branch of philosophy that studies", "the nature, sources and limits of knowledge",
   [("being and reality", "That is metaphysics."),
    ("right and wrong conduct", "That is ethics."),
    ("beauty and art", "That is aesthetics.")],
   "Epistemology asks what knowledge is and how we can have it.")
_q("branch", "Which question belongs to metaphysics?", "What kinds of things exist, and what is their nature?",
   [("How should we live?", "That is an ethical question."),
    ("What makes an argument valid?", "That is a logical question."),
    ("What makes a work of art beautiful?", "That is an aesthetic question.")],
   "Metaphysics studies being and reality.")
_q("meth", "Socratic maieutics is", "the method of drawing out a person's own ideas by questioning, likened to midwifery",
   [("a method of doubting everything to find certainty", "That is Descartes' methodic doubt."),
    ("a method of bracketing assumptions to describe experience", "That is phenomenology."),
    ("a method of reconciling opposites in history", "That is Hegelian dialectic.")],
   "Socrates compared his questioning to helping others give birth to ideas.")
_q("meth", "Descartes' doubt is called 'methodic' because it is", "a deliberate and temporary tool for finding certainty, not a final conclusion",
   [("a permanent sceptical belief", "Descartes did not remain a sceptic."),
    ("a doubt about logic only", "It covers the senses and also reason, as a method."),
    ("limited to religious claims", "It covers all beliefs that can be doubted.")],
   "He doubts in order to find something indubitable.", "Concept")
_q("meth", "In Husserl's phenomenology, the 'epoche' is", "suspending assumptions about the existence of the world in order to describe experience as it appears",
   [("a proof that the world does not exist", "It suspends the assumption; it does not deny the world."),
    ("a Socratic way of ending a conversation", "It is a Husserlian technique."),
    ("the third stage of Hegel's dialectic", "That is synthesis.")],
   "Bracketing lets the philosopher describe how things are given in consciousness.")

# ---- Ancient Greek & Medieval Philosophy (14)
_q("pre", "Thales is traditionally reported to have taken as the first principle (arche)", "water",
   [("air", "That is Anaximenes."), ("fire", "That is associated with Heraclitus."), ("atoms and void", "That is Democritus.")],
   "Thales held that water is the underlying stuff.")
_q("pre", "Heraclitus emphasised", "constant change, with logos as the pattern within it",
   [("unchanging being", "That is Parmenides."), ("atoms and void", "That is Democritus."), ("number as the first principle", "That is associated with Pythagoras.")],
   "Everything flows, but the change follows a pattern (logos).")
_q("pre", "Democritus explained the world by", "atoms moving in the void",
   [("a single unchanging being", "That is Parmenides."), ("water as the origin", "That is Thales."), ("a boundless principle", "That is Anaximander.")],
   "Many unchanging atoms and empty space.")
_q("soph", "Protagoras is associated with", "relativism: truth and value depend on the human observer",
   [("the theory of Forms", "That is Plato."), ("the doctrine of the four causes", "That is Aristotle."), ("the elenchus as a search for definitions", "That is Socrates.")],
   "Protagoras' man-the-measure doctrine is a form of relativism.")
_q("soph", "The Socratic elenchus is", "cross-examination that tests a claim or definition by drawing out its consequences",
   [("the use of speeches to persuade a crowd", "That is rhetoric as taught by Sophists."),
    ("a proof from first principles", "The elenchus is a conversation, not a proof."),
    ("a vow of silence", "It is a method of questioning.")],
   "Socrates examined others' definitions by questions.")
_q("plato", "For Plato the Forms are", "eternal, unchanging and grasped by reason, the objects of true knowledge",
   [("generalisations that the mind forms from experience", "This is the empiricist view of general ideas."),
    ("sensible things that change", "These are the particulars."),
    ("the four elements", "The elements are not the Forms.")],
   "Forms are the real and unchanging patterns of which sensible things are copies.")
_q("plato", "The three parts of the soul in Plato's Republic are", "reason, spirit and appetite",
   [("matter, form and soul", "Matter and form are Aristotle's terms."),
    ("body, mind and spirit", "These are not Plato's parts in the Republic."),
    ("sensation, reflection and memory", "These are not Plato's parts of the soul.")],
   "Each part has its virtue, and justice is the right order among them.")
_q("arist", "Aristotle's hylomorphism says that a substance is composed of", "matter and form",
   [("atoms and void", "That is the atomist view."), ("a Form and a copy", "That is Plato's two-world view."), ("impressions and ideas", "That is Hume's vocabulary.")],
   "Hyle is matter; morphe is form.")
_q("arist", "The final cause of a knife, in Aristotle's four causes, is", "cutting (its purpose)",
   [("the steel", "That is the material cause."), ("the shape of the blade", "That is the formal cause."), ("the blacksmith's work", "That is the efficient cause.")],
   "The final cause is the end or purpose for which a thing exists.", "Application")
_q("hell", "In Epicureanism, ataraxia is", "freedom from disturbance of the mind, a calm life",
   [("the pursuit of physical luxury", "Epicurus advised simple pleasures."), ("the suppression of all feeling", "That is closer to a Stoic idea of apatheia."), ("belief in fate", "That is a Stoic emphasis, not ataraxia.")],
   "Pleasure for Epicurus is mainly absence of pain and mental disturbance.")
_q("hell", "The Stoics advised us to distinguish what is", "up to us from what is not, and to live according to nature and reason",
   [("pleasant from painful, and avoid all pain", "That is closer to Epicurean hedonism."),
    ("true from false, and suspend all judgement", "That is Pyrrhonian scepticism."),
    ("holy from profane", "This is not the central Stoic distinction.")],
   "The dichotomy of control is central to Stoic ethics.")
_q("hell", "Pyrrhonian scepticism recommends", "suspension of judgement (epoche) in order to reach tranquillity",
   [("rejecting the existence of the world", "Pyrrhonists did not assert that the world does not exist."),
    ("accepting the Stoic logos", "That is Stoicism."),
    ("the pursuit of pleasure as the goal", "That is Epicureanism.")],
   "Equal arguments on both sides lead to suspended judgement.")
_q("augaq", "Augustine explains evil as", "a privation (lack) of good, not a substance",
   [("a substance created by God", "Augustine denied that evil is a thing."), ("an illusion with no effect", "He treats it as a real lack of good."), ("a second equal principle", "That is a dualist view he rejected.")],
   "Evil is a defect in what is good.")
_q("augaq", "The first of Aquinas' Five Ways argues from", "motion or change in the world to a first unmoved mover",
   [("the idea of a perfect being to its existence", "That is the ontological argument, which Aquinas did not use as a Way."),
    ("moral law to a lawgiver in the Kantian way", "That is a Kantian-style argument."),
    ("personal faith to certainty", "The Ways are arguments from the world, not from faith.")],
   "Things in motion are moved by something else, and a regress must stop.")

# ---- Modern Western Philosophy (9)
_q("rat", "The first indubitable truth found by Descartes' method is", "that he exists as a thinking thing (cogito)",
   [("that material things exist", "This is established later, if at all."), ("that God exists", "This comes after the cogito."), ("that the senses are reliable", "The senses are among the things he first doubts.")],
   "Even if he is deceived, he must exist in order to be deceived.")
_q("rat", "Spinoza held that there is", "one infinite substance, God or Nature",
   [("two substances, mind and matter", "That is Descartes' dualism."), ("an infinite number of monads", "That is Leibniz."), ("no substance, only impressions", "That is a Humean view.")],
   "Everything is a mode of the one substance.")
_q("emp", "Locke compared the mind at birth to", "a blank sheet (tabula rasa) on which experience writes",
   [("a store of innate ideas", "That is the rationalist view Locke attacked."), ("a mirror of the Forms", "That is a Platonic picture."), ("a divine light", "That is not Locke's view.")],
   "Ideas come from sensation and reflection.")
_q("emp", "Hume argued that our idea of causation comes from", "the habit of expecting one event after another that is constantly conjoined",
   [("direct perception of a necessary connection", "He argued we never perceive one."), ("an innate idea", "He denied innate ideas."), ("the Forms", "That is Plato.")],
   "We see succession and constant conjunction, and the mind adds the expectation.")
_q("sc", "In Hobbes' state of nature, life without a common power is", "a war of all against all, in which life is insecure",
   [("peaceful and rich", "That is not Hobbes' view."), ("governed by perfect natural law enforced by all", "That is closer to Locke."), ("a life guided by the general will", "That is Rousseau's idea.")],
   "He argues that fear and competition make an absolute sovereign rational.")
_q("sc", "Locke held that people have natural rights to", "life, liberty and property, and that a government that betrays its trust may be resisted",
   [("only the rights the sovereign grants", "That is nearer to Hobbes."), ("nothing before the state exists", "Locke thought natural rights come before the state."), ("rule by a philosopher-king", "That is Plato.")],
   "Government is limited by consent and the protection of rights.")
_q("sc", "Rousseau's 'general will' is", "the will of the people as a body aiming at the common good",
   [("the sum of every individual's private wishes", "He distinguishes it from the will of all."), ("the commands of an absolute king", "That is not his meaning."), ("the market's demand", "Not his meaning.")],
   "Citizens obey laws they give themselves as a body.")
_q("kant", "A categorical imperative is a command that", "binds a rational agent regardless of their desires",
   [("applies only if you want a particular goal", "That is a hypothetical imperative."), ("states what most people do", "It is a rule of duty, not a statistic."), ("is a law of nature in physics", "It is a moral law.")],
   "One formulation asks whether your rule of action could be willed as a universal law.")
_q("kant", "For Kant, phenomena are", "things as they appear to us, shaped by the mind's forms and categories",
   [("things as they are in themselves", "These are noumena."), ("innate ideas of God", "These are not phenomena."), ("illusions without any reality", "Phenomena are real appearances.")],
   "We know appearances, not things in themselves.")

# ---- Traditional Formal Logic (11)
_q("terms", "Which categorical form distributes both its subject and its predicate?", "E: No S are P",
   [("A: All S are P", "A distributes only its subject."), ("I: Some S are P", "I distributes neither."), ("O: Some S are not P", "O distributes only its predicate.")],
   "Universal negative: both terms distributed.", "Concept", "Use the distribution table.")
_q("terms", "'Not all birds fly' is equivalent to", "Some birds are not flyers (O)",
   [("No birds are flyers (E)", "'Not all' does not say none."), ("All birds are non-flyers (A)", "This says no bird flies."), ("Some birds are flyers (I)", "This is compatible with 'all birds fly'.")],
   "The contradictory of A is O.", "Application", "Which form contradicts A?")
_q("sq", "The contrary of 'All S are P' is", "No S are P",
   [("Some S are not P", "This is its contradictory."), ("Some S are P", "This is its subaltern."), ("All P are S", "This reverses the terms.")],
   "A and E are contraries: they cannot both be true but both can be false.", "Concept", "Which form is the opposite universal?")
_q("sq", "On the traditional square, if 'No S are P' is false, then 'Some S are P' is", "true",
   [("false", "E and I are contradictories, so one is true."), ("undetermined", "Contradictories determine each other."), ("true only if S is empty", "The traditional square assumes non-empty terms.")],
   "Contradictories cannot both be false.", "Reasoning", "Which relation holds between E and I?")
_q("syl", "'All farmers are traders. All traders are taxpayers. Therefore all taxpayers are farmers.' commits", "the fallacy of illicit minor",
   [("undistributed middle", "The middle term 'traders' is the subject of an A premise, distributed."),
    ("illicit major", "'Farmers' is the predicate of an A conclusion: undistributed, so no illicit major."),
    ("exclusive premises", "Both premises are affirmative.")],
   "'Taxpayers' is distributed in the conclusion but undistributed in the minor premise (predicate of an A).", "Application", "Which term is distributed in the conclusion but not in its premise?")
_q("syl", "Which mood is valid in figure 1?", "AAA",
   [("AEE", "AEE in figure 1 commits illicit major."), ("IAI", "IAI in figure 1 has an undistributed middle."), ("EEE", "Two negative premises.")],
   "AAA-1 is Barbara.", "Recall", "Recall the names Barbara, Celarent, Darii, Ferio.")
_q("syl", "If a valid syllogism has a negative premise, its conclusion must be", "negative",
   [("affirmative", "A negative premise forces a negative conclusion."), ("particular", "Quantity is a separate matter."), ("undistributed", "Distribution depends on the form.")],
   "Rule: a negative premise if and only if a negative conclusion.", "Concept", "Think of the rule on quality.")
_q("hyp", "'If it rains the match is cancelled. The match is not cancelled. So it did not rain.' is", "modus tollens",
   [("modus ponens", "That affirms the antecedent."), ("affirming the consequent", "The consequent is denied, not affirmed."), ("a disjunctive syllogism", "There is no disjunction.")],
   "Denying the consequent gives the denial of the antecedent.", "Application", "Which part of the conditional is denied?")
_q("hyp", "Replying to a dilemma by showing the alternatives are not exhaustive is", "escaping between the horns",
   [("grasping the horns", "That denies a conditional premise."), ("rebutting the dilemma", "That offers a counter-dilemma."), ("affirming the consequent", "That is an invalid argument form.")],
   "Showing a third possibility denies the disjunctive premise.", "Concept", "Which premise is attacked?")
_q("inf", "'Don't listen to her proposal; she failed her own exam.' is an example of", "argument against the person (ad hominem)",
   [("false cause", "No cause is claimed."), ("composition", "No part-to-whole inference."), ("begging the question", "The conclusion is not restated.")],
   "The speaker's past is used instead of the proposal's merits.", "Application", "What is attacked, the argument or the person?")
_q("inf", "'Every time the goat enters the yard, the rain falls, so the goat brings the rain.' is", "false cause",
   [("equivocation", "No word changes meaning."), ("appeal to pity", "No sympathy is invoked."), ("division", "No whole-to-part inference.")],
   "Succession is mistaken for causation.", "Application", "What is assumed from the order of events?")

# ---- Symbolic / Propositional Logic (9)
_q("var", "'Neither Ada nor Ngu passed' (A, N) is symbolised", "~A · ~N",
   [("~(A · N)", "That only denies that both passed."), ("~A v ~N", "At least one failed."), ("A v N", "At least one passed.")],
   "Both did not pass.", "Application", "Both are false.")
_q("var", "A conditional p ⊃ q is false only when", "p is true and q is false",
   [("p is false and q is true", "Here p ⊃ q is true."), ("p and q are both false", "Here p ⊃ q is true."), ("p and q are both true", "Here p ⊃ q is true.")],
   "A true antecedent with a false consequent breaks the promise.", "Recall", "When is the promise broken?")
_q("tt", "A complete truth table for a formula with three variables has", "8 rows",
   [("3 rows", "The number is not the number of variables."), ("6 rows", "3 x 2 is not the rule."), ("9 rows", "3 squared is not the rule.")],
   "Two to the power of 3.", "Recall", "Two to the power of the number of variables.")
_q("tt", "The argument 'p ⊃ q; q; therefore p' is invalid because", "there is a row with p false and q true: both premises true and the conclusion false",
   [("every row makes the conclusion false", "Rows with p true make it true."), ("p ⊃ q is false in every row", "It is true in three rows."), ("the premises are contradictory", "They are jointly satisfiable.")],
   "That row is the counterexample.", "Reasoning", "Find a row with true premises and a false conclusion.")
_q("tc", "p ⊃ (q ⊃ p) is", "a tautology",
   [("a contradiction", "It is never false."), ("a contingency", "Every row makes it true."), ("equivalent to q ⊃ p", "Not the same truth conditions.")],
   "If p is true the inner conditional q ⊃ p is true; if p is false the whole is true, because the antecedent is false.", "Reasoning", "Check what happens when p is true and when it is false.")
_q("tc", "~(p v q) is logically equivalent to", "~p · ~q",
   [("~p v ~q", "That is equivalent to ~(p · q)."), ("p · q", "That is not related."), ("~p · q", "q is not negated.")],
   "De Morgan's law.", "Application", "'Neither p nor q'.")
_q("pf", "From p ⊃ q and p we may write q by", "modus ponens",
   [("modus tollens", "That needs ~q."), ("disjunctive syllogism", "That needs a disjunction."), ("addition", "That makes a disjunction.")],
   "If p then q; p; so q.", "Recall", "Which part of the conditional is affirmed?")
_q("pf", "From p ⊃ q and q ⊃ r we may write p ⊃ r by", "hypothetical syllogism",
   [("modus ponens", "No antecedent is affirmed."), ("simplification", "There is no conjunction."), ("exportation", "That rewrites (p · q) ⊃ r.")],
   "A chain of conditionals gives a conditional.", "Recall", "Two conditionals share a middle statement.")
_q("pf", "The rule that changes p ⊃ q into ~p v q is", "Implication (Impl)",
   [("Transposition", "That gives ~q ⊃ ~p."), ("De Morgan", "That changes a negated conjunction or disjunction."), ("Exportation", "That moves a conjunction into a conditional.")],
   "Replacement rule: a conditional is equivalent to a disjunction with the antecedent negated.", "Recall", "Which replacement rule turns a conditional into a disjunction?")

assert len(_m1) == 50, len(_m1)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="psl2-paper1-multiple-choice",
    mock=True, time_limit_minutes=90, questions=build(_m1, seed=31)))

# ---------------------------------------------------------------- Mock: Paper 2 practice paper A (25 parts)
_m2 = []
_b = _m2.append
_PRE, _MET, _RAT, _EMP = _T["pre"], _T["meth"], _T["rat"], _T["emp"]
_SC, _PLATO, _ARIST, _KANT, _AQ = _T["sc"], _T["plato"], _T["arist"], _T["kant"], _T["augaq"]

# Question 1: an essay on the Pre-Socratics
_b(Q("Question 1 (a). An essay question begins 'Examine the Pre-Socratic search for the first principle.' The command word 'examine' asks you to", "investigate the topic closely, setting out positions and judging them",
     [("list the names of the philosophers", "A list is narration, not examination."),
      ("agree with the Pre-Socratics", "Examine does not mean agree."),
      ("write only a definition of arche", "A definition belongs to the introduction.")],
     "Examine: expound carefully and assess.", _PRE, "Reasoning", "What does the examiner want beyond description?"))
_b(Q("Question 1 (b). Which pair of thinkers both explained the world by a single basic stuff (monists)?", "Thales and Anaximenes",
     [("Democritus and Anaximenes", "Democritus is a pluralist: many atoms."),
      ("Parmenides and Democritus", "Democritus is a pluralist."),
      ("Heraclitus and Democritus", "Democritus is a pluralist.")],
     "Thales: water. Anaximenes: air.", _PRE, "Recall", "Which thinkers named one underlying stuff?"))
_b(Q("Question 1 (c). Which thinker would you use as the main support for the claim that real being is one and unchanging?", "Parmenides",
     [("Heraclitus", "He stresses change."), ("Democritus", "He explains change by moving atoms."), ("Thales", "He gives an arche (water) from which change arises.")],
     "Parmenides argued that change is an illusion.", _PRE, "Recall", "Who denied change?"))
_b(Q("Question 1 (d). Which sentence is an INTERNAL critique of Thales' claim that water is the arche?", "It does not say how water becomes other things such as fire or stone.",
     [("Modern chemistry shows that water is made of hydrogen and oxygen.", "This is an external objection from later science."),
      ("Aristotle preferred four elements.", "This is an external alternative."),
      ("Many Greeks worshipped gods of the sea.", "This is irrelevant to the argument's coherence.")],
     "An internal critique points to a gap within the position.", _PRE, "Analysis", "Which objection finds a gap in the position itself?"))
_b(Q("Question 1 (e). A good conclusion to the essay would be that the search for an arche mattered mainly because it", "replaced story by explanation based on reasons, even though the answers were weak",
     [("proved that water is the origin of everything", "The essay does not support this."),
      ("showed that philosophy began in Egypt", "The question concerns the Greek search."),
      ("ended the use of myth in Greece", "Myth continued.")],
     "The value lies in the method.", _PRE, "Evaluation", "What is the lasting contribution?"))

# Question 2: Descartes and method
_b(Q("Question 2 (a). Descartes' doubt is 'methodic' because it is", "a temporary tool to find certainty",
     [("his final position", "He did not end as a sceptic."), ("directed only at religion", "It reaches the senses, dreams and a possible deceiver."), ("a way of avoiding all questions", "It is a method of inquiry.")],
     "He doubts in order to find an indubitable foundation.", _MET, "Concept", "Is the doubt the goal or the means?"))
_b(Q("Question 2 (b). In what order does Descartes' doubt proceed?", "the senses, then dreaming and waking, then reason itself (a deceiving power)",
     [("reason, then the senses, then dreams", "This reverses the order."),
      ("God, then the world, then the self", "This is the order of his reconstruction."),
      ("the self, then the senses, then dreams", "The self is found at the end of the doubt.")],
     "He starts with the least secure beliefs and goes to the most secure.", _RAT, "Recall", "Which beliefs does he doubt first?"))
_b(Q("Question 2 (c). The role of the cogito in the argument is to", "supply a first truth that survives all doubt",
     [("prove that God exists directly", "God is proved later."), ("show that the body exists", "The body is not yet established."), ("end the method of doubt by refuting it", "The cogito is found by pushing the doubt to the limit.")],
     "Even a deceiver cannot deceive him unless he exists.", _RAT, "Concept", "What does he find that he cannot doubt?"))
_b(Q("Question 2 (d). The objection called the 'Cartesian circle' is best classified as", "an internal critique",
     [("an external critique from science", "It concerns the coherence of his argument."),
      ("an objection about his dates", "It is an argument about logic."),
      ("a defence of his method", "It is an objection.")],
     "It claims his argument uses clear and distinct ideas to prove God, and God to guarantee those ideas.", _RAT, "Analysis", "Does the objection test the argument from within?"))
_b(Q("Question 2 (e). Which thinker is the best opponent for an external critique of Descartes' innate ideas?", "Locke",
     [("Spinoza", "He is a rationalist like Descartes."), ("Leibniz", "He defended innate ideas in his own way."), ("Plato", "His doctrine of recollection supports innate knowledge.")],
     "Locke argued that the mind begins as a blank slate and ideas come from experience.", _EMP, "Application", "Which empiricist opposed innate ideas?"))

# Question 3: a passage (written by KKEVO for practice)
_PASSAGE = ("Passage (written by KKEVO for practice): 'People who live without any authority fear one another. Because each fears the others, each prepares to strike first, and fear turns to violence. "
            "To escape this, people should hand their power to one ruler who can keep the peace for all.'")
_b(Q(_PASSAGE + " Question 3 (a). The theme of the passage is", "the reason for having a state",
     [("the nature of beauty", "The passage concerns authority and peace."), ("the validity of syllogisms", "It is not about logic."), ("the existence of God", "God is not mentioned.")],
     "The passage explains why authority is needed.", _SC, "Concept", "What is it about overall?"))
_b(Q("Question 3 (b). The problem that the passage answers is best stated as", "Why should people accept a ruler's authority?",
     [("What is the best form of art?", "Not the problem here."), ("Is the soul immortal?", "Not the problem here."), ("How do we know the external world exists?", "A different question.")],
     "The passage justifies authority by the dangers of life without it.", _SC, "Analysis", "What question does the argument answer?"))
_b(Q("Question 3 (c). The thesis of the passage is that", "people should hand over their power to one ruler who keeps the peace",
     [("people should rule themselves directly in every case", "The passage argues the opposite."), ("fear is a virtue", "The passage treats fear as a problem."), ("violence is natural and good", "It treats violence as a danger.")],
     "The author's answer.", _SC, "Comprehension", "What does the author want us to accept?"))
_b(Q("Question 3 (d). Which is an INTERNAL critique of the passage?", "It assumes that the ruler will not himself abuse the power given to him.",
     [("Another school of thought disagrees.", "That is external."), ("The author lived long ago.", "That is irrelevant."), ("Most people dislike rulers.", "That is not an argument about the passage's coherence.")],
     "The passage gives the ruler absolute power without explaining why he would act for all.", _SC, "Evaluation", "Which objection finds a gap inside the argument?"))
_b(Q("Question 3 (e). A thinker who would reply with an EXTERNAL critique, urging that government be limited and may be resisted if it betrays its trust, is", "Locke",
     [("Hobbes", "The passage resembles his position."), ("Plato", "He defended rule by philosopher-kings."), ("Heraclitus", "He is not a political theorist.")],
     "Locke defended natural rights and limited government.", _SC, "Application", "Which contract theorist limited the ruler's power?"))

# Question 4: Plato, Aristotle, Aquinas, Kant
_b(Q("Question 4 (a). In an essay comparing Plato and Aristotle on the Forms, a clear thesis would be", "Plato places the Forms apart from things, while Aristotle places form within things",
     [("Plato and Aristotle both rejected form", "Both used form in some way."), ("Aristotle held that Forms exist apart in a separate world", "That is Plato's view."), ("Neither thinker discussed substance", "Aristotle's theory of substance is central.")],
     "Aristotle criticised separate Forms and used hylomorphism.", _ARIST, "Analysis", "Where is the form located in each view?"))
_b(Q("Question 4 (b). Which of Aristotle's four causes explains 'for the sake of what'?", "the final cause",
     [("the material cause", "The matter."), ("the formal cause", "The pattern."), ("the efficient cause", "The agent or source of change.")],
     "The end or purpose.", _ARIST, "Recall", "Which cause concerns purpose?"))
_b(N("Question 4 (c). How many levels are there on Plato's divided line?", 4,
     [("Count", "Two for the visible world (imagining, belief) and two for the intelligible (thought, understanding): 4.")], _PLATO, "Recall", "Two main sections, each divided in two."))
_b(N("Question 4 (d). How many 'Ways' does Aquinas set out in his proofs of God's existence?", 5,
     [("Count", "The Five Ways.")], _AQ, "Recall", "Recall the name of the arguments."))
_b(Q("Question 4 (e). Kant's test of the categorical imperative asks whether", "your rule of action could be willed as a universal law",
     [("the action will bring the most pleasure", "That is a utilitarian test."), ("the action is allowed by the government", "That is not the test."), ("the action follows the mean between two vices", "That is Aristotle.")],
     "Universalisability.", _KANT, "Concept", "Which test is Kantian?"))

# Question 5: logic in philosophical writing
_b(Q("Question 5 (a). A writer argues: 'Everyone believes that luck exists, so luck exists.' The fallacy is", "appeal to the people (ad populum)",
     [("begging the question", "The conclusion is not just restated."), ("equivocation", "No word shifts meaning."), ("composition", "No whole-part inference.")],
     "Popularity is offered as proof.", _T["inf"], "Application", "What reason is given for the conclusion?"))
_b(Q("Question 5 (b). 'All philosophers are thinkers. All teachers are thinkers. So all teachers are philosophers.' commits", "undistributed middle",
     [("illicit minor", "'Teachers' is distributed in the conclusion and in the minor premise, so no illicit minor."),
      ("illicit major", "'Philosophers' is the predicate of an A conclusion: undistributed."),
      ("exclusive premises", "Both premises are affirmative.")],
     "'Thinkers' is the predicate of two A propositions: distributed in neither.", _T["syl"], "Application", "Where does the middle term stand in each premise?"))
_b(Q("Question 5 (c). 'If reason alone gives knowledge (R), then the senses are not needed (~S)' is symbolised", "R ⊃ ~S",
     [("~S ⊃ R", "That reverses the direction."), ("R · ~S", "That asserts both, not a conditional."), ("~(R ⊃ S)", "That is a different statement.")],
     "If R then not-S.", _T["var"], "Application", "Which part is the antecedent?"))
_b(Q("Question 5 (d). From R ⊃ ~S and R, the line ~S is justified by", "modus ponens",
     [("modus tollens", "That needs the denial of the consequent."), ("disjunctive syllogism", "There is no disjunction."), ("hypothetical syllogism", "There is only one conditional.")],
     "Affirming the antecedent.", _T["pf"], "Application", "Which part of the conditional is given?"))
_b(N("Question 5 (e). How many rows are there in a complete truth table for an argument with the three variables R, S and K?", 8,
     [("Rule", "2 x 2 x 2 = 8.")], _T["tt"], "Calculation", "Two to the power of the number of variables."))

for _s in _m2:
    if _s["prompt"].startswith("Question 3") and not _s["prompt"].startswith(_PASSAGE):
        _s["prompt"] = _PASSAGE + " " + _s["prompt"]
assert len(_m2) == 25, len(_m2)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="psl2-paper2-essays-textual-analysis",
    mock=True, time_limit_minutes=150, questions=build(_m2, seed=41)))

# ---------------------------------------------------------------- Mock: Paper 3 practice paper A (20 parts)
_m3 = []
_b = _m3.append
_ARG = ("Argument for Question 1: 'If the bridge is built, trade rises. Trade rises only if the roads are repaired. The roads are not repaired. So the bridge is not built.' "
        "(B: the bridge is built; T: trade rises; R: the roads are repaired.)")
_b(Q(_ARG + " Question 1 (a). 'Trade rises only if the roads are repaired' is symbolised", "T ⊃ R",
     [("R ⊃ T", "That says repairing roads guarantees trade: the 'if' reading."), ("T · R", "That asserts both."), ("T ≡ R", "'Only if' gives one direction.")],
     "'Only if' marks the necessary condition: T ⊃ R.", _T["var"], "Application", "Which condition is necessary for which?"))
_b(N("Question 1 (b). In the eight-row truth table of the argument (premises B ⊃ T, T ⊃ R, ~R; conclusion ~B), in how many rows are all three premises true?", 1,
     [("~R", "R is false."), ("T ⊃ R", "With R false this forces T false."), ("B ⊃ T", "With T false this forces B false."), ("Count", "Only the row B, T, R all false: 1 row.")],
     _T["tt"], "Reasoning", "~R is a premise: start there."))
_b(Q("Question 1 (c). Since the conclusion ~B is true in that row, the argument is", "valid",
     [("invalid, because a premise is false in other rows", "False premises in other rows do not matter."),
      ("invalid, because the conclusion is a negation", "The form of the conclusion does not decide validity."),
      ("sound but not valid", "Soundness requires validity.")],
     "No row has all premises true and the conclusion false.", _T["tt"], "Reasoning", "Is there a counterexample row?"))
_b(Q("Question 1 (d). In a formal proof, the line B ⊃ R is justified by", "hypothetical syllogism on the first two premises",
     [("modus ponens on the first two premises", "No antecedent is affirmed."), ("modus tollens on lines 1 and 3", "Line 3 is ~R, which denies R, not T."), ("simplification", "There is no conjunction.")],
     "Then MT with ~R gives ~B.", _T["pf"], "Application", "Two conditionals share a middle statement T."))
_ARG2 = "Argument for Question 2: 'All birds are egg-layers. Some reptiles are egg-layers. So some reptiles are birds.'"
_b(Q(_ARG2 + " Question 2 (a). Its mood and figure are", "AII in figure 2",
     [("AII in figure 1", "The middle term is the predicate of both premises: figure 2."), ("AAI in figure 2", "The minor premise and conclusion are particular, I."), ("IAI in figure 3", "The major premise is universal.")],
     "Major: All P are M. Minor: Some S are M. Conclusion: Some S are P.", _T["syl"], "Application", "Which term is the middle and where is it placed?"))
_b(Q("Question 2 (b). The fallacy committed, explained in context, is", "undistributed middle: egg-layers is the predicate of an A and of an I, so some reptiles that lay eggs need not be birds",
     [("illicit major: 'birds' is distributed in the conclusion", "'Birds' is the predicate of an I conclusion, undistributed."),
      ("exclusive premises: both premises are negative", "Both premises are affirmative."),
      ("four terms: 'egg-layers' changes meaning", "The meaning does not shift.")],
     "Being an egg-layer does not link reptiles to birds.", _T["syl"], "Analysis", "Where does the middle term stand?"))
_b(N("Question 2 (c). How many terms are distributed altogether in the two premises of the argument?", 1,
     [("Major (A)", "Only the subject 'birds' is distributed."), ("Minor (I)", "Neither term is distributed."), ("Total", "1.")], _T["terms"], "Calculation", "Use the distribution table for A and I."))
_b(Q("Question 2 (d). 'All whales are mammals, and Moby is a whale.' is an enthymeme of the", "third order",
     [("first order", "The major premise is given."), ("second order", "The minor premise is given."), ("fourth order", "There are only three orders.")],
     "Both premises are stated; the conclusion is missing.", _T["syl"], "Recall", "Which proposition is missing?"))
_b(Q("Question 3 (a). 'Only members who have paid may vote' (Vx: x may vote; Mx: x is a member; Px: x has paid) is", "(x)(Vx ⊃ (Mx · Px))",
     [("(x)((Mx · Px) ⊃ Vx)", "That says all paying members may vote."), ("(∃x)(Vx · Mx · Px)", "That says some paying member may vote."), ("(x)(Vx · Mx · Px)", "That says everything is a voting paying member.")],
     "Whoever may vote is a member who has paid.", _T["var"], "Application", "'Only' puts the voting condition first."))
_b(Q("Question 3 (b). 'Some nurses are not graduates' (Nx, Gx) is", "(∃x)(Nx · ~Gx)",
     [("(x)(Nx ⊃ ~Gx)", "That says no nurse is a graduate."), ("(∃x)(Nx ⊃ ~Gx)", "Using ⊃ with ∃ is a standard error."), ("~(∃x)(Nx · ~Gx)", "That says every nurse is a graduate.")],
     "Particular statements use ∃ with ·.", _T["terms"], "Application", "Some x is a nurse and not a graduate."))
_b(Q("Question 3 (c). 'No politician is honest' (Px, Hx) is", "(x)(Px ⊃ ~Hx)",
     [("(∃x)(Px · ~Hx)", "That says some politician is dishonest."), ("(x)(Px · ~Hx)", "That says everything is a dishonest politician."), ("(x)(Hx ⊃ Px)", "That says all honest persons are politicians.")],
     "A universal negative uses ⊃ and ~.", _T["terms"], "Application", "A universal takes the conditional."))
_b(Q("Question 3 (d). Before symbolising 'Not every trader is honest', the best paraphrase is", "Some trader is not honest",
     [("Every trader is dishonest", "That says none is honest."), ("No trader is honest", "That says none is honest."), ("Some trader is honest", "That does not deny that every trader is honest.")],
     "The contradictory of A is O.", _T["sq"], "Application", "What is the contradictory of 'every'?"))
_PASS = ("Passage for Questions 4 and 5 (written by KKEVO for practice): 'Whatever I perceive may be a dream. But two and three make five whether I dream or wake. "
         "So mathematical truths are surer than the evidence of the senses, and reason, not the senses, should guide our search for knowledge.'")
_b(Q(_PASS + " Question 4 (a). The problem the passage addresses is best stated as", "What should be the basis of our knowledge: reason or the senses?",
     [("What is the best form of government?", "The passage is about knowledge."), ("Is the soul immortal?", "Not raised."), ("What makes an action morally right?", "Not raised.")],
     "The passage compares the reliability of reason and the senses.", _RAT, "Analysis", "What question does the argument answer?"))
_b(Q("Question 4 (b). The thesis of the passage is that", "reason, not the senses, should guide the search for knowledge",
     [("the senses are the only source of knowledge", "That is the opposite."), ("mathematics is a dream", "The passage says the opposite about mathematics."), ("dreams prove that the world exists", "Not claimed.")],
     "The author's answer.", _RAT, "Comprehension", "What does the author want us to accept?"))
_b(Q("Question 4 (c). The structure of the argument is", "a doubt about the senses, a contrast with mathematics, and a conclusion",
     [("two examples and no conclusion", "There is a conclusion."), ("a definition followed by a story", "It is an argument, not a story."), ("a series of questions with no answers", "It makes assertions.")],
     "Premise on dreams, premise on mathematics, conclusion.", _MET, "Analysis", "What are the three moves?"))
_b(Q("Question 4 (d). The tradition to which this position is closest is", "rationalism",
     [("empiricism", "Empiricists make the senses the source."), ("Epicureanism", "That is an ancient school about pleasure."), ("contract theory", "That concerns the state.")],
     "It places reason above sense experience.", _RAT, "Application", "Which tradition favours reason over the senses?"))
_b(Q("Question 5 (a). An INTERNAL critique of the passage is that", "a dream can also contain mathematical beliefs, so the argument does not show that mathematical truths are more certain",
     [("empiricists disagree", "That is external."), ("the author is unknown", "Irrelevant."), ("many people trust their eyes", "Popularity is not a critique.")],
     "The premise may not support the conclusion as strongly as claimed.", _RAT, "Evaluation", "Which objection finds a gap inside the argument?"))
_b(Q("Question 5 (b). An EXTERNAL critique from British empiricism would stress that", "knowledge begins in experience, and mathematics itself is learned by experience of objects",
     [("knowledge is innate", "That is the rationalist reply."), ("dreams are real", "Not an empiricist claim."), ("all philosophy is useless", "Not an empiricist claim.")],
     "Locke and Hume made experience the source of ideas.", _EMP, "Application", "What did empiricists make the source of ideas?"))
_b(Q("Question 5 (c). A sound conclusion to a commentary on the passage is that", "it gives a reason to be cautious about the senses, but whether reason alone can found knowledge is still disputed",
     [("it proves that the senses are always wrong", "The passage does not show this."), ("it proves that mathematics is false", "It claims the opposite."), ("it settles the debate for all time", "No single passage settles a debate.")],
     "A balanced assessment.", _MET, "Evaluation", "Which conclusion is balanced?"))
_b(Q("Question 5 (d). To plan a problem essay on 'Can we have certain knowledge?', the best way to state the problem in the introduction is", "as a question showing a tension: if the senses sometimes deceive and reason can err, on what can certainty rest?",
     [("as a list of philosophers' names", "A list is not a problem."), ("as the author's opinion with no argument", "The problem must be shown."), ("as a definition of 'certainty' only", "A definition is part of the introduction but is not the problem.")],
     "Define terms, show the difficulty and state it as a question.", _MET, "Application", "What does the introduction have to state?"))

for _s in _m3:
    _p = _s["prompt"]
    if _p.startswith(("Question 1 (b)", "Question 1 (c)", "Question 1 (d)")):
        _s["prompt"] = _ARG + " " + _p
    elif _p.startswith(("Question 2 (b)", "Question 2 (c)")):
        _s["prompt"] = _ARG2 + " " + _p
    elif _p.startswith(("Question 4 (b)", "Question 4 (c)", "Question 4 (d)", "Question 5 (a)", "Question 5 (b)", "Question 5 (c)")):
        _s["prompt"] = _PASS + " " + _p
assert len(_m3) == 20, len(_m3)
SETS.append(practice_set(
    module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="psl2-paper3-logic-problems",
    mock=True, time_limit_minutes=150, questions=build(_m3, seed=51)))
