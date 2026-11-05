"""Form 5 Logic (O Level 0590): practice sets for the Examination module and two mock papers.

Draft content. Exam facts are only those of the Board's revised 0590 syllabus: Paper 1 is 50 multiple-choice
questions in 1 hour 30 minutes (40%); Paper 2 has six questions of 20 marks in 2 hours 30 minutes (60%), Section A
structural (three questions, all answered) and Section B problem solving (three questions, any two answered). The
mock papers use KKEVO practice settings, not official GCE Board settings. Essays cannot be marked automatically, so
the Paper 2 practice paper is a structured version with multiple-choice and numeric parts.

Logic conventions: opposition questions use the TRADITIONAL (Aristotelian) square and say so; Venn and syllogism
questions are chosen so that the answer is the same in the traditional and the Boolean view (checked by brute force
over all Venn-region fillings). Every logical claim was verified by script (see the build notes in the report).
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

M_EXAM = "Examination"


class _Bag:
    """Gives the position of the correct option so that A-D are used evenly."""

    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.items = []

    def next(self):
        if not self.items:
            self.items = [0, 1, 2, 3]
            self.rng.shuffle(self.items)
        return self.items.pop()


BAG = _Bag(1)


def use(seed):
    global BAG
    BAG = _Bag(seed)


def Q(prompt, correct, wrongs, steps, concept, skill, hint, diagram="", alt="", pos=None):
    """Four-option MC. `wrongs` = [(text, why)] x3; the correct option goes to a balanced position."""
    pos = BAG.next() if pos is None else pos
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(correct, correct=True))
    return MC(prompt, choices, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint,
              diagram=diagram, diagram_alt=alt)


def N(prompt, answer, steps, concept, skill, hint, tol=0, unit="", diagram="", alt=""):
    return NUM(prompt, answer, steps=[S(a, text=b) for a, b in steps], tolerance=tol, unit=unit, concept=concept,
               skill=skill, hint=hint, diagram=diagram, diagram_alt=alt)


# Exact syllabus topic titles (apps/academics/gce_curriculum.py, ("logic", "form-5")).
T_DEF = "Definition and origin of Logic"
T_REL = "Logic and related fields"
T_LAWS = "Laws of thought"
T_OPS = "Operations of the mind"
T_IDEAS = "Properties of ideas and terms"
T_QQ = "Classification of terms according to quantity and quality"
T_DM = "Classification of terms according to definiteness of meaning and relation"
T_LANG = "The basic functions of language"
T_DEFN = "Basic notions of definition"
T_KINDS = "Kinds of definition"
T_RULES = "Rules and fallacies of definition"
T_DIV = "Structure and rules of logical division"
T_PCOMP = "Definition and components of a proposition"
T_PPROP = "Properties of categorical propositions"
T_DIST = "Distribution of terms in categorical propositions"
T_VENN = "Symbolization and Venn diagramming of categorical propositions"
T_HYP = "Hypothetical proposition and types"
T_DISJ = "Disjunctive proposition and types"
T_MOD = "Modal proposition and types"
T_TRANS = "Translating ordinary propositions into standard forms"
T_BASIC = "Basic notions and the importance of symbolic logic"
T_CONN = "Connectives and symbols in symbolic logic"
T_CONST = "Logical constants (truth-functional statements)"
T_PUNCT = "Punctuation in symbolic logic"
T_STRUCT = "Structure of truth tables and their uses"
T_TT = "Truth tables and logical constants"
T_METH = "Methods of reasoning"
T_INF = "Definition and types of inference"
T_OPP = "Forms of opposition"
T_SQ = "Squares and truth table for opposition"
T_EDU = "Forms of eduction"
T_ARG = "Structure of an argument"
T_VS = "Validity and soundness"
T_SYLL = "Value of the syllogism and structure of the categorical syllogism"
T_FIG = "The figures of the categorical syllogism"
T_MOOD = "The moods of the categorical syllogism"
T_SVENN = "Representing categorical syllogisms on the Venn diagram"
T_GR = "The general rules of the syllogism and fallacies"
T_ENTH = "The enthymeme"
T_HSYL = "The hypothetical syllogism"
T_DSYL = "The disjunctive syllogism"
T_CD = "Constructive dilemma"
T_FDEF = "Definition, classification and significance of fallacies"
T_FNO = "Fallacies of relevance: fallacies of no evidence"
T_FLITTLE = "Fallacies of relevance: fallacies of little evidence"
T_FAMB = "Fallacies of ambiguity"

# =============================================================================================
# 1. Paper 1: multiple-choice strategies (practice set for lesson 1)
# =============================================================================================
use(11)
SET1 = [
    Q("Which line describes Paper 1 of the GCE Logic examination?",
      "50 multiple-choice questions, all answered, in 1 hour 30 minutes",
      [("50 multiple-choice questions, any 40 answered, in 2 hours", "All 50 are answered, and the time is 1 hour 30 minutes."),
       ("Six structured questions, five answered, in 1 hour 30 minutes", "That describes Paper 2 in outline, and Paper 2 takes 2 hours 30 minutes."),
       ("25 multiple-choice questions, all answered, in 45 minutes", "Paper 1 has 50 questions, not 25.")],
      [("Recall the facts", "Paper 1 has 50 multiple-choice questions, all answered, with 1 hour 30 minutes. Each question is worth 1 mark and Paper 1 carries 40% of the examination.")],
      "Paper 1 organisation", "Recall", "Count the questions, then think of the time in minutes."),
    N("Paper 1 has 50 questions and lasts 90 minutes. How many minutes is that for each question, on average?", 1.8,
      [("Divide", "90 divided by 50 = 1.8 minutes, which is a little less than two minutes.")],
      "Time management", "Calculation", "Divide the total minutes by the number of questions.", tol=0.05, unit="minutes"),
    Q("After about two minutes you are still undecided on one question. What does the two-pass method advise?",
      "Tick it, move on, and come back to it in the second pass",
      [("Stay on it until you are sure, however long it takes", "One hard question can cost you two or three easy ones."),
       ("Leave it blank and never return", "Every question is answered and a blank earns nothing, so return and choose the best option."),
       ("Choose the longest option and forget it", "Length is not a sign of the correct answer. Come back and reason about it.")],
      [("Apply the method", "Pass 1 collects the easy marks. A ticked question waits for pass 2, when you have time to eliminate options.")],
      "Two-pass method", "Application", "Easy marks first."),
    Q("The proposition 'All the mangoes in the basket are ripe' is false. Which statement MUST then be true?",
      "Some mangoes in the basket are not ripe",
      [("No mangoes in the basket are ripe", "This is the contrary, not the contradictory. It may be false too if some are ripe and some are not."),
       ("Some mangoes in the basket are ripe", "If the A proposition is false, we cannot tell whether any mango is ripe."),
       ("All the mangoes in the basket are unripe", "This says the same as 'none is ripe'. It is a contrary and is not forced.")],
      [("Find the contradictory", "The contradictory of 'All S are P' is 'Some S are not P'. They always have opposite truth values.")],
      "Quantifiers and negation", "Reasoning", "Which proposition is the exact opposite, one true when the other is false and the other way round?"),
    Q("Which sentence is a correct negation of 'All the students passed'?",
      "Not every student passed",
      [("No student passed", "That is much stronger than the negation: it is the contrary."),
       ("Some students passed", "This can be true together with 'All the students passed', so it does not deny it."),
       ("Every student failed", "Same as 'no student passed': too strong.")],
      [("Deny only what was claimed", "A negation must be true exactly when the original is false. 'Not every student passed' means that at least one did not.")],
      "Quantifiers and negation", "Concept", "A good negation denies the claim and nothing more."),
    Q("An argument has two true premises, and its conclusion follows with certainty from them. Which description is best?",
      "It is valid, and because the premises are true it is also sound",
      [("It is valid but we cannot say it is sound", "Soundness means valid form plus true premises, and the premises are true here."),
       ("It is invalid, because only the conclusion can be true or false", "The conclusion follows with certainty, so the argument is valid."),
       ("It is sound but we cannot say it is valid", "Soundness needs validity first: valid form plus true premises.")],
      [("Use the two tests", "Valid: the conclusion follows. Sound: valid AND all premises true. Both hold here.")],
      "Truth and validity", "Concept", "Two tests: form first, truth of the premises second."),
    Q("To show quickly that an argument is invalid, which method works?",
      "Find a case in which all the premises are true and the conclusion is false",
      [("Check that the conclusion is false in real life", "A false conclusion alone does not prove invalidity: a valid argument with a false premise can have one."),
       ("Check that the premises are boring", "How interesting the premises are has nothing to do with validity."),
       ("Count the words in the premises", "Length is not a test of validity.")],
      [("Counterexample", "One case with true premises and a false conclusion proves the form is invalid. A Venn sketch or a truth-table row does the same.")],
      "Testing validity quickly", "Reasoning", "What can never happen in a valid argument?"),
    Q("A student notes that 'hot' and 'cold' are CONTRARY terms, while 'voter' and 'non-voter' are CONTRADICTORY terms. Which statement about the difference is correct?",
      "Contraries leave a middle ground, so both can be false of one thing. Contradictories leave none",
      [("Contraries leave no middle ground, so one of them must be true", "It is the contradictories that leave no middle ground."),
       ("Contradictories can both be true of one thing", "They cannot: a person is a voter or a non-voter, never both."),
       ("There is no difference: the two words mean the same", "They differ: the trap in Paper 1 is to mix them up.")],
      [("Test the middle", "Water can be neither hot nor cold (lukewarm), so hot and cold are contraries. Everyone is exactly one of voter or non-voter, so those are contradictories.")],
      "Contrary and contradictory", "Concept", "Is there something that is neither one nor the other?"),
]

# =============================================================================================
# 2. Paper 2 Section A: structural questions (practice set for lesson 2)
# =============================================================================================
use(22)
SET2 = [
    N("Paper 2 has six questions. Section A has three questions, all answered. Section B has three questions, any two answered. How many questions must a candidate answer in all?", 5,
      [("Count", "Section A: 3 questions, all answered = 3. Section B: any 2 of 3 = 2. Total 3 + 2 = 5.")],
      "Paper 2 organisation", "Recall", "Section A: all. Section B: only two."),
    Q("Which instruction in Section A most clearly asks you to say what a term means?",
      "Define the term 'proposition'",
      [("Draw a Venn diagram for 'No S are P'", "This asks for a diagram, not for a meaning."),
       ("Test the following syllogism for validity", "This is a Section B type of task: you apply a test."),
       ("Symbolise the argument and build a truth table", "This is also an application task.")],
      [("Read the command word", "'Define' asks what the term means: give the class it belongs to and what marks it off from others.")],
      "Command words", "Recall", "Which command word means 'give the meaning'?"),
    Q("A good definition of 'triangle' in an answer is:",
      "A plane figure with three straight sides",
      [("A triangle is a triangle with three sides", "This is circular: it uses the word being defined."),
       ("A shape that is not a square", "A negative, too-wide definition: circles are not squares either."),
       ("The most beautiful shape", "Figurative and obscure: it does not say what the figure is.")],
      [("Genus and difference", "Genus: plane figure. Difference: three straight sides. This avoids circularity and is neither too wide nor too narrow.")],
      "Answering definition questions", "Application", "Name the class, then add what makes it different from the rest of that class."),
    Q("In a labelled Venn diagram for 'All S are P', which labelling is essential?",
      "Name each circle (S and P) and show the shading on the part of S outside P",
      [("Only write the word Venn at the top", "Circles must be named, and the shading shows the claim."),
       ("Shade the overlap of S and P", "Shading the overlap would say that no S are P."),
       ("Draw one circle only", "Two terms need two circles.")],
      [("Draw it correctly", "Two circles, named S and P. Shade the part of S that lies outside P: that part is empty. Add a short title.")],
      "Labelled diagrams", "Application", "What must be empty if every S is a P?"),
    Q("In the traditional square of opposition, which two corners are contradictories?",
      "A and O, and also E and I",
      [("A and E only", "A and E are contraries."),
       ("I and O only", "I and O are subcontraries."),
       ("A and I, and also E and O", "These pairs are subalternation (a general proposition and its particular).")],
      [("Read the diagonals", "The two diagonals of the square join the contradictories: A with O, and E with I.")],
      "Square of opposition", "Recall", "Which lines cross in the middle of the square?"),
    Q("A candidate is asked to obvert 'No mangoes are vegetables'. Which answer is correct?",
      "All mangoes are non-vegetables",
      [("No vegetables are mangoes", "This is the converse, not the obverse."),
       ("Some mangoes are non-vegetables", "Obversion keeps the quantity: universal stays universal."),
       ("All vegetables are non-mangoes", "The subject has been changed. Obversion keeps the subject and changes the predicate.")],
      [("Obversion", "Change the quality (negative to affirmative) and replace the predicate by its complement: No S are P becomes All S are non-P.")],
      "Eduction", "Application", "Two changes: the quality and the predicate."),
    Q("Which is the most common mistake in Section A answers?",
      "Giving a meaning without an example, or an example without the meaning",
      [("Writing neatly", "Neat writing is not a mistake."),
       ("Using the correct technical terms", "Correct terms are what is wanted."),
       ("Answering all three questions", "All three must be answered in Section A.")],
      [("Check yourself", "A strong answer states the idea in a sentence and supports it with a short example. Leaving either out weakens the answer.")],
      "Common mistakes", "Concept", "Think of definition PLUS illustration."),
    Q("In 'All traders are honest', which term is distributed?",
      "Only the subject, 'traders'",
      [("Only the predicate, 'honest'", "In an A proposition the predicate is not distributed: the claim is not about all honest persons."),
       ("Both terms", "Only E and O style propositions distribute the predicate."),
       ("Neither term", "The subject of an A proposition is distributed: it speaks of every trader.")],
      [("A proposition", "A: All S are P distributes S only. The statement says nothing about all the P, only that all S fall inside P.")],
      "Distribution", "Concept", "Does the sentence say something about every trader, or about every honest person?"),
]

# =============================================================================================
# 3. Paper 2 Section B: problem-solving questions (practice set for lesson 3)
# =============================================================================================
use(33)
SET3 = [
    N("You answer five questions in Paper 2, which lasts 150 minutes. If you shared the time equally, how many minutes would each question get? (In practice, plan a little less to leave time for checking. This is study advice, not an official rule.)", 30,
      [("Divide", "150 divided by 5 = 30 minutes for each question.")],
      "Time planning", "Calculation", "Divide the total minutes by the number of questions you answer.", unit="minutes"),
    Q("Which is the first step when testing a categorical syllogism?",
      "Put it in standard form and identify the major, minor and middle terms",
      [("Decide whether the conclusion is true in real life", "Truth of the conclusion does not decide validity."),
       ("Count the words", "Length is irrelevant."),
       ("Draw the conclusion on the diagram first", "Draw the premises first, then see whether the conclusion is already shown.")],
      [("Order of work", "Standard form first, then the three terms. After that apply the rules or the Venn test.")],
      "Testing syllogisms", "Application", "You cannot test what you cannot see in order."),
    Q("The syllogism 'All taxis are vehicles. All buses are vehicles. So all buses are taxis' is invalid. Which rule does it break?",
      "The middle term must be distributed at least once",
      [("A syllogism must have exactly four terms", "A categorical syllogism has three terms."),
       ("The conclusion must be negative", "No such rule: the conclusion may be affirmative."),
       ("The premises must be particular", "No such rule: universal premises are allowed.")],
      [("Check the middle term", "The middle term 'vehicles' is the predicate of two A propositions and so is distributed in neither. This is the fallacy of the undistributed middle.")],
      "Testing syllogisms", "Reasoning", "Is the shared term 'vehicles' distributed in an A proposition when it is the predicate?"),
    N("An argument is built from three different statement letters: p, q and r. How many rows does its truth table need?", 8,
      [("Use 2 to the power n", "With n = 3 statement letters there are 2 x 2 x 2 = 8 rows.")],
      "Truth tables", "Calculation", "Each letter doubles the number of rows."),
    Q("When symbolising 'If the rain comes early, the farmers plant maize', which symbolisation is correct, with r for 'the rain comes early' and m for 'the farmers plant maize'?",
      "r ⊃ m",
      [("m ⊃ r", "This reverses the direction: it says that planting maize leads to early rain."),
       ("r . m", "This says both are true, not that one leads to the other."),
       ("r v m", "This says at least one is true, which is a different meaning.")],
      [("Antecedent and consequent", "The part after 'if' is the antecedent and goes first: r ⊃ m.")],
      "Symbolising arguments", "Application", "Which part follows the word 'if'?"),
    Q("A passage says: 'Do not listen to her opinion on the exam rules. She failed the test last year.' What is the best description of the reasoning?",
      "It attacks the person instead of examining her reasons (argument against the person)",
      [("It is a valid syllogism", "No syllogism is stated."),
       ("It is a sound deductive argument", "No premise supports the conclusion about the rules."),
       ("It is a definition by genus and difference", "Nothing is being defined.")],
      [("Name the fallacy", "The argument rejects the opinion because of a fact about the speaker. The reasons for the opinion are never examined.")],
      "Identifying fallacies", "Application", "Is the argument about the rules or about the person?"),
    Q("To standardise the everyday argument 'Kofi has a fever, so he should see a doctor', what must you do?",
      "Supply the missing premise 'Everyone with a fever should see a doctor' and rewrite as premises and conclusion",
      [("Delete the word 'fever'", "The word carries the middle idea of the argument."),
       ("Turn it into a question", "An argument states premises and a conclusion."),
       ("Leave it as it is, because everyday arguments cannot be tested", "They can: standardise them first.")],
      [("Standard form", "Identify the conclusion (Kofi should see a doctor), then the stated and the missing premise, and write them in order.")],
      "Standardising everyday arguments", "Application", "What general statement is taken for granted?"),
    Q("In a Section B answer about a fallacy, which sentence best shows reasoning?",
      "The speaker concludes about all traders from two cases, so the sample is too small: a hasty generalisation",
      [("This is wrong because I disagree with it", "Disagreement is not an analysis of the reasoning."),
       ("This is a fallacy. The end.", "Always name it AND say why."),
       ("Fallacies are all bad", "Too general to earn credit.")],
      [("Name and justify", "Give the name of the fallacy and the reason, quoting the part of the passage that shows it.")],
      "Explaining fallacies", "Interpretation", "A good answer has a label and a reason."),
]

# =============================================================================================
# 4. Paper 1 mock exam A: 50 questions (Foundation 4, Terms 5, Definitions and division 6, Propositions 9,
#    Symbolic logic 7, Inference 5, Syllogism 7, Other arguments 4, Informal fallacies 3)
# =============================================================================================
use(77)
SQ = "f5l-exam-square-plain.svg"
SQ_ALT = "A rectangle with four corner boxes: A 'All S are P' top left, E 'No S are P' top right, I 'Some S are P' bottom left, O 'Some S are not P' bottom right, joined by sides and two diagonals."
VS = "f5l-exam-venn-shaded.svg"
VS_ALT = "Two overlapping circles labelled S and P. The part of circle S that lies outside circle P is shaded to show it is empty."

P1_QUESTIONS = [
    # ---- The Foundation of Logic (4)
    Q("The word 'logic' comes from the Greek word logos, meaning word or reason. Logic is best described as",
      "the study of the principles of correct reasoning",
      [("the study of the human brain and its cells", "That is neuroscience, a branch of biology."),
       ("the study of how people feel when they argue", "Feelings belong to psychology. Logic is about the correctness of reasoning."),
       ("a collection of all the true facts about the world", "Facts are the work of the sciences. Logic studies how conclusions follow.")],
      [("Recall", "Logic studies the principles by which correct reasoning is told from incorrect reasoning.")],
      T_DEF, "Recall", "Think of 'reason' in logos."),
    Q("A student says: 'Mount Cameroon is a volcano and it is not a volcano, in the same sense and at the same time.' Which law of thought does this break?",
      "The law of non-contradiction",
      [("The law of identity", "Identity says a thing is what it is. The statement does more: it affirms and denies together."),
       ("The law of excluded middle", "Excluded middle says that either P or not-P is true. It is not about asserting both."),
       ("None of them, because it is only an opinion", "The laws of thought govern every statement, whether or not it is an opinion.")],
      [("Match the law", "Something cannot both be and not be in the same respect at the same time. This is the law of non-contradiction.")],
      T_LAWS, "Concept", "The statement asserts a thing and its denial together."),
    Q("A farmer forms the idea 'rain', then says 'It will rain today', then argues 'Dark clouds bring rain; dark clouds are above us; so it will rain.' The three acts of the mind, in order, are",
      "simple apprehension, judging, reasoning",
      [("reasoning, judging, simple apprehension", "The order is reversed: reasoning is built from judgements, which are built from ideas."),
       ("judging, simple apprehension, reasoning", "A judgement combines ideas, so the ideas come first."),
       ("simple apprehension, reasoning, judging", "Reasoning uses judgements, so judging comes before it.")],
      [("Idea, statement, argument", "An idea (term) is formed by simple apprehension. A statement (proposition) is made by judging. An argument is built by reasoning.")],
      T_OPS, "Concept", "Idea first, then a statement, then an argument."),
    Q("Which statement correctly separates logic from psychology?",
      "Logic studies how we ought to reason correctly, while psychology studies how people actually think",
      [("Psychology studies how we ought to reason, logic how people actually think", "This is reversed."),
       ("Both study only the emotions of people", "Neither is limited to emotions, and logic is not about emotions at all."),
       ("Logic studies numbers and psychology studies words", "This is not the distinction.")],
      [("Rules and facts", "Logic gives standards (what makes reasoning correct). Psychology describes the mental processes that happen.")],
      T_REL, "Concept", "One is about standards, the other about description."),
    # ---- First Operation of the Mind: Terms (5)
    Q("Arrange from the greatest extension to the least: Fido (my dog), dog, mammal, animal.",
      "animal, mammal, dog, Fido",
      [("Fido, dog, mammal, animal", "This is the reverse. 'Animal' applies to the most individuals."),
       ("mammal, animal, dog, Fido", "'Animal' is wider than 'mammal'."),
       ("animal, dog, mammal, Fido", "'Mammal' is wider than 'dog': every dog is a mammal.")],
      [("Extension", "Extension is the number of things a term applies to. Animal includes mammals, which include dogs, which include Fido. As extension grows, comprehension (the qualities contained) shrinks.")],
      T_IDEAS, "Concept", "Which class contains all the others?"),
    Q("Which of these terms is singular?",
      "The Wouri River",
      [("Some rivers in Cameroon", "This is a particular term: it refers to part of a class."),
       ("All rivers in Cameroon", "This is a universal term: it refers to the whole class."),
       ("Every river in Africa", "Also universal, in 'every'.")],
      [("Singular, particular, universal", "A singular term names one individual. Particular terms speak of some members. Universal terms speak of all.")],
      T_QQ, "Recall", "Which term names exactly one thing?"),
    Q("Which of these is a negative term?",
      "non-smoker",
      [("smoker", "A positive term names the presence of a quality."),
       ("Buea", "A name of a town: positive (and singular)."),
       ("school", "Positive: it names what a thing is.")],
      [("Quality of terms", "A negative (infinite) term is formed with 'non-': it names what a thing is not.")],
      T_QQ, "Recall", "Look for the word that denies."),
    Q("The word 'bank' in 'I sat on the bank of the river' and in 'I saved money in the bank' is",
      "an equivocal term",
      [("a univocal term", "A univocal term keeps the same meaning in every use."),
       ("a singular term", "Singular describes the quantity of a term, not its meaning."),
       ("a negative term", "Negative describes quality, not meaning.")],
      [("Same word, different meanings", "A word with two unrelated meanings is equivocal. Equivocation can ruin an argument.")],
      T_DM, "Concept", "One word, two different meanings."),
    Q("Which pair of terms are contradictory?",
      "voter and non-voter",
      [("hot and cold", "These are contraries: something can be lukewarm."),
       ("teacher and pupil", "These are correlative terms: each implies the other."),
       ("rich and poor", "These are contraries: a person may be neither very rich nor poor.")],
      [("No middle ground", "Contradictory terms exclude each other and leave no middle. Everyone is either a voter or a non-voter.")],
      T_DM, "Concept", "Is there anything between the two?"),
    # ---- Definitions and Logical Division (6)
    Q("Which sentence mainly performs a directive function of language?",
      "Submit your assignment before Friday.",
      [("The meeting began at nine o'clock.", "This informs: it states a fact."),
       ("What a beautiful sunset!", "This expresses a feeling."),
       ("I am sorry for being late.", "This expresses feeling.")],
      [("Three functions", "Informative (gives facts), expressive (shows feeling), directive (tries to make someone act). A command is directive.")],
      T_LANG, "Concept", "Which sentence tries to make someone do something?"),
    Q("In the definition 'A triangle is a plane figure with three straight sides', the definiendum is",
      "triangle",
      [("a plane figure with three straight sides", "This is the definiens: the words that explain."),
       ("plane figure", "This is the genus."),
       ("three straight sides", "This is the difference.")],
      [("Two parts", "The definiendum is the term being defined. The definiens is what defines it.")],
      T_DEFN, "Recall", "Which term is being defined?"),
    Q("A teacher points to a mango tree and says: 'That is what I mean by a mango tree.' This is",
      "an ostensive definition",
      [("a definition by genus and difference", "That would name the class and what marks it off, in words."),
       ("a stipulative definition", "A stipulative definition gives a term a new meaning by decision."),
       ("a lexical definition", "A lexical definition reports the ordinary meaning of a word, as a dictionary does.")],
      [("Pointing", "An ostensive definition shows an example by pointing or displaying.")],
      T_KINDS, "Concept", "What is the teacher doing, rather than saying?"),
    Q("'A farmer is a person who farms.' Which rule of definition does this break?",
      "A definition must not be circular",
      [("A definition must not be too wide", "Everyone who farms is a farmer, so the definition is not too wide."),
       ("A definition must not be negative", "The definition is affirmative."),
       ("A definition must not be too narrow", "It covers every farmer, so it is not too narrow.")],
      [("Circular", "The word being defined (farmer) reappears in the definition (farms). The definition explains nothing.")],
      T_RULES, "Application", "Is the word being defined hiding in the definition?"),
    Q("'A chair is a piece of furniture with four legs.' This definition is faulty because it is",
      "both too wide and too narrow",
      [("only too wide", "It is too wide because a table also has four legs, but it is also too narrow."),
       ("only too narrow", "A chair with three legs or a single stem is left out, but tables are wrongly included."),
       ("circular", "The word 'chair' does not appear in the definition.")],
      [("Test both ways", "Too wide: includes things that are not chairs (tables). Too narrow: leaves out chairs without four legs.")],
      T_RULES, "Reasoning", "Think of a table, then of a three-legged chair."),
    Q("A teacher divides the 'students of a school which has Forms 1 to 5' into 'Form 1, Form 2 and Form 3 students'. Which rule of logical division is broken?",
      "The members together must make up the whole",
      [("Only one basis of division must be used", "One basis is used: the form of the student."),
       ("The members must exclude each other", "No student is in two of these forms."),
       ("Division must stop at three members", "There is no rule fixing the number of members.")],
      [("Omission", "Students in Forms 4 and 5 are left out, so the members do not add up to the whole.")],
      T_DIV, "Application", "Is any student left out?"),
    # ---- The Second Operation of the Mind: Propositions (9)
    Q("In the proposition 'All taxi drivers are careful', the copula is",
      "are",
      [("taxi drivers", "That is the subject."),
       ("careful", "That is the predicate."),
       ("All", "That is the quantifier.")],
      [("Components", "Subject (taxi drivers), copula (are), predicate (careful), with the quantifier 'All' showing quantity.")],
      T_PCOMP, "Recall", "Which word links the subject to the predicate?"),
    Q("'Some prefects are not boys' is a proposition that is",
      "particular and negative",
      [("universal and negative", "'Some' is particular, not universal."),
       ("particular and affirmative", "'Are not' makes it negative."),
       ("universal and affirmative", "'Some' makes it particular and 'not' makes it negative.")],
      [("Quantity and quality", "Quantity: some, so particular. Quality: 'are not', so negative. This is the O proposition.")],
      T_PPROP, "Recall", "Read the quantity word and the copula."),
    Q("Which of the four standard propositions distributes BOTH its subject and its predicate?",
      "E: No S are P",
      [("A: All S are P", "A distributes its subject only."),
       ("I: Some S are P", "I distributes neither term."),
       ("O: Some S are not P", "O distributes its predicate only.")],
      [("Distribution", "A distributes S. E distributes S and P. I distributes neither. O distributes P.")],
      T_DIST, "Recall", "Which proposition excludes the whole of one class from the whole of the other?"),
    N("The four standard propositions A, E, I and O each have a subject and a predicate, so there are 8 term places in all. How many of those places are distributed?", 4,
      [("Count", "A: 1 (subject). E: 2. I: 0. O: 1 (predicate)."), ("Add", "1 + 2 + 0 + 1 = 4.")],
      T_DIST, "Calculation", "Count the distributed terms in each of A, E, I and O, then add.", ),
    Q("In the Venn diagram, the part of S outside P is shaded, meaning it is empty. Which proposition does the diagram show?",
      "All S are P",
      [("No S are P", "That would shade the overlap of S and P."),
       ("Some S are P", "That would put an X in the overlap."),
       ("Some S are not P", "That would put an X in the part of S outside P.")],
      [("Read the shading", "Nothing is in S outside P, so every S is inside P: All S are P.")],
      T_VENN, "Interpretation", "If no S lies outside P, where must every S be?",
      diagram=VS, alt=VS_ALT),
    Q("In 'If the road is flooded, the bus will be late', the antecedent is",
      "the road is flooded",
      [("the bus will be late", "That is the consequent."),
       ("the bus", "It is only a term inside the consequent."),
       ("If", "'If' is the connecting word, not a part of the proposition.")],
      [("If-part", "In a hypothetical (conditional) proposition the 'if' clause is the antecedent and the 'then' clause is the consequent.")],
      T_HYP, "Recall", "Which clause follows the word 'if'?"),
    Q("'Maria is either in Bamenda or in Kumba tonight', where she cannot be in both. This disjunctive proposition is",
      "exclusive (strong)",
      [("inclusive (weak)", "An inclusive disjunction allows both parts to be true."),
       ("hypothetical", "There is no if-then structure."),
       ("categorical", "It does not join a subject to a predicate with a copula in the standard way.")],
      [("Both false? Both true?", "If both cannot be true, the disjunction is exclusive. If both may be true, it is inclusive.")],
      T_DISJ, "Concept", "Can both parts be true together here?"),
    Q("Which of these is a modal proposition?",
      "It is possible that it will rain tomorrow.",
      [("It rained yesterday.", "A plain statement of fact, with no mode."),
       ("All birds have feathers.", "A categorical proposition."),
       ("If it rains, the roads flood.", "A hypothetical proposition.")],
      [("Mode", "A modal proposition tells HOW something is true: possibly, necessarily, and so on.")],
      T_MOD, "Recall", "Which sentence says how the statement is true?"),
    Q("Which is the standard form of 'Every student in the school wears uniform'?",
      "All students in the school are persons who wear uniform.",
      [("Some students in the school are persons who wear uniform.", "Standard A form uses 'All', not 'Some'."),
       ("No students in the school are persons who wear uniform.", "This changes the quality."),
       ("All persons who wear uniform are students in the school.", "This reverses subject and predicate.")],
      [("Standard form", "Use All S are P with the copula 'are'. The verb phrase becomes a noun phrase: persons who wear uniform.")],
      T_TRANS, "Application", "Keep 'Every' as 'All' and make the predicate a class."),
    # ---- Introduction to Symbolic Logic (7)
    Q("Why do logicians use symbols such as p, q and the horseshoe?",
      "They show the form of an argument clearly, without being distracted by the words",
      [("They make the premises true", "Symbols do not change truth. They only show form."),
       ("They remove the need for a conclusion", "An argument still has a conclusion."),
       ("They make every argument valid", "Validity depends on the form, not on the use of symbols.")],
      [("Form", "A symbolised argument lets us test its pattern, whatever the topic.")],
      T_BASIC, "Concept", "What is the value of seeing only the pattern?"),
    Q("Which symbol is the horseshoe, used for material implication ('if ... then')?",
      "⊃",
      [("≡", "This is the biconditional ('if and only if')."),
       ("v", "This is disjunction ('or')."),
       (".", "This is conjunction ('and').")],
      [("The set of symbols", "Negation ~, conjunction ., disjunction v, material implication ⊃, biconditional ≡.")],
      T_CONN, "Recall", "Which symbol looks like a horseshoe?"),
    Q("A statement is truth-functional when",
      "its truth value depends only on the truth values of its components",
      [("it contains the word 'and'", "Truth-functionality is not a matter of one word."),
       ("it is true", "A truth-functional statement may be false."),
       ("its components are all true", "Components may have any truth values.")],
      [("Definition", "Given the truth values of the parts, the truth value of the whole is fixed. ~, ., v, ⊃ and ≡ build truth-functional compounds.")],
      T_CONST, "Concept", "What determines the truth value of the whole?"),
    Q("p is true and q is false. What are the truth values of ~(p . q) and of (~p) . q, in that order?",
      "true, false",
      [("false, true", "The two values are the wrong way round."),
       ("true, true", "(~p) . q is false because ~p is false and q is false."),
       ("false, false", "~(p . q) is true: p . q is false, and its negation is true.")],
      [("Brackets matter", "p . q is false, so ~(p . q) is true. ~p is false, so (~p) . q is false.")],
      T_PUNCT, "Calculation", "Work inside the brackets first."),
    N("A truth table for a formula with four different statement letters has how many rows?", 16,
      [("Use 2 to the power n", "2 x 2 x 2 x 2 = 16 rows.")],
      T_STRUCT, "Calculation", "Each letter doubles the rows.", ),
    Q("Which compound statement is false ONLY when p is true and q is false?",
      "p ⊃ q",
      [("p . q", "This is false in three rows, true only when both are true."),
       ("p v q", "This is false only when both are false."),
       ("p ≡ q", "This is false when p and q differ, in two rows.")],
      [("Truth table of the horseshoe", "p ⊃ q is false only in the row T, F and true in the other three.")],
      T_TT, "Concept", "Think of a promise broken only when the condition is met and the result fails."),
    Q("Which formula is true when p is true, q is false and r is true?",
      "~(p . q) . r",
      [("(p ⊃ q) . r", "p ⊃ q is false here, so the conjunction is false."),
       ("(p v q) ≡ ~r", "p v q is true but ~r is false, so the biconditional is false."),
       ("(q ≡ r) v ~p", "q ≡ r is false and ~p is false, so the disjunction is false.")],
      [("Substitute", "p . q is false, so ~(p . q) is true. With r true the conjunction is true. The other three are false.")],
      T_TT, "Calculation", "Substitute T, F, T and work out each in turn."),
    # ---- The Third Operation of the Mind: Reasoning (5)
    Q("A trader finds that the last five batches of mangoes from one supplier were sour and concludes that the next batch will probably be sour too. This method of reasoning is",
      "inductive",
      [("deductive", "In deduction, true premises guarantee the conclusion. Here they only make it probable."),
       ("definition", "Nothing is being defined."),
       ("division", "Nothing is being divided.")],
      [("From cases to a probable conclusion", "Reasoning from observed cases to a general or future conclusion is induction.")],
      T_METH, "Concept", "Does the conclusion follow with certainty or only probably?"),
    Q("Which of the following is an immediate inference?",
      "No bats are birds; therefore no birds are bats.",
      [("All men are mortal; Socrates is a man; so Socrates is mortal.", "This uses two premises: a mediate inference."),
       ("All cars need fuel; this is a car; so this needs fuel.", "Two premises again: mediate."),
       ("All gates here are locked, because five were locked.", "This is an inductive generalisation from several cases.")],
      [("One premise", "An immediate inference draws a conclusion from a single proposition, here by conversion.")],
      T_INF, "Concept", "How many premises does each option use?"),
    Q("Which pair of propositions are contradictories?",
      "All S are P and Some S are not P",
      [("All S are P and No S are P", "These are contraries."),
       ("Some S are P and Some S are not P", "These are subcontraries."),
       ("All S are P and Some S are P", "This is subalternation.")],
      [("A and O", "Contradictories have opposite truth values. A and O are contradictories, and so are E and I.")],
      T_OPP, "Recall", "Which pair can never be both true or both false?"),
    Q("The figure shows the traditional square of opposition. If the A proposition (top left) is true, which statement is correct?",
      "I is true, and E and O are false",
      [("E is true, and I and O are false", "A and E are contraries: they cannot both be true."),
       ("I and O are both true", "O is the contradictory of A, so it is false."),
       ("E, I and O are all undetermined", "Each is determined by the truth of A.")],
      [("Read the square", "A true: E false (contrary), O false (contradictory), I true (subalternation). This is the traditional view, in which the subject class has members.")],
      T_SQ, "Interpretation", "Use the three lines that leave the A corner.",
      diagram=SQ, alt=SQ_ALT),
    Q("The obverse of 'No mangoes are vegetables' is",
      "All mangoes are non-vegetables",
      [("No vegetables are mangoes", "This is the converse."),
       ("Some mangoes are non-vegetables", "Obversion keeps the quantity: universal stays universal."),
       ("All vegetables are non-mangoes", "This changes the subject. Obversion keeps it.")],
      [("Obversion", "Change the quality and replace the predicate by its complement: No S are P becomes All S are non-P.")],
      T_EDU, "Application", "Change quality, replace the predicate."),
    # ---- Mediate Inference (7)
    Q("In 'All students must wear uniform. Kofi is a student. Therefore Kofi must wear uniform', the conclusion is",
      "Kofi must wear uniform",
      [("All students must wear uniform", "This is a premise."),
       ("Kofi is a student", "This is a premise."),
       ("Kofi", "A single term is not a statement.")],
      [("Find the 'therefore'", "The conclusion is the statement that the premises are meant to support. The word 'Therefore' signals it.")],
      T_ARG, "Recall", "Which statement follows the word 'therefore'?"),
    Q("An argument is valid but one of its premises is false. Which statement is correct?",
      "The argument is valid but not sound",
      [("The argument is invalid because a premise is false", "Validity is about form, not about the truth of the premises."),
       ("The argument is sound because it is valid", "Soundness needs all premises true."),
       ("The conclusion must be false", "A valid argument with a false premise may still have a true conclusion.")],
      [("Two tests", "Valid: the conclusion follows from the premises. Sound: valid with all true premises.")],
      T_VS, "Concept", "Which test concerns form, which concerns truth?"),
    Q("In 'All cocoa is a cash crop. All cash crops earn money. So all cocoa earns money', the middle term is",
      "cash crop",
      [("cocoa", "This is the minor term, the subject of the conclusion."),
       ("earns money", "This is the major term, the predicate of the conclusion."),
       ("all", "'All' is a quantifier, not a term.")],
      [("Terms", "The middle term appears in both premises and not in the conclusion.")],
      T_SYLL, "Concept", "Which term is in both premises but not in the conclusion?"),
    Q("In a categorical syllogism the middle term is the subject of the major premise and the predicate of the minor premise. This is the",
      "first figure",
      [("second figure", "In the second figure the middle term is the predicate of both premises."),
       ("third figure", "In the third figure the middle term is the subject of both."),
       ("fourth figure", "In the fourth figure it is the predicate of the major and the subject of the minor.")],
      [("Figures", "Figure 1: M-P, S-M. Figure 2: P-M, S-M. Figure 3: M-P, M-S. Figure 4: P-M, M-S.")],
      T_FIG, "Recall", "Find the position of the middle term in each premise."),
    Q("A syllogism has the major premise 'All M are P', the minor premise 'Some S are M' and the conclusion 'Some S are P'. Its mood is",
      "AII",
      [("IAI", "The mood lists the major premise first: A for All M are P."),
       ("AAI", "The minor premise is particular: I, not A."),
       ("AAA", "The minor premise and conclusion are particular.")],
      [("Read the propositions", "Major: All M are P (A). Minor: Some S are M (I). Conclusion: Some S are P (I). The mood is AII.")],
      T_MOOD, "Recall", "Name each proposition by its letter in order."),
    Q("In the Venn diagram test of a syllogism, the argument is valid when",
      "drawing the premises alone already shows the conclusion",
      [("the conclusion is drawn first and the premises fit", "Draw the premises first. The conclusion must then already be there."),
       ("the conclusion is true in real life", "Real-life truth does not test validity."),
       ("there are three circles on the diagram", "Three circles are always used.")],
      [("Test", "Draw the premises on the three-circle diagram. If the conclusion is then already shown, without any further marking, the form is valid.")],
      T_SVENN, "Concept", "What must the premises do for the conclusion?"),
    Q("Which syllogism commits the fallacy of the undistributed middle?",
      "All taxis are vehicles. All buses are vehicles. So all buses are taxis.",
      [("All birds are animals. All eagles are birds. So all eagles are animals.", "Valid. The middle term 'birds' is distributed once."),
       ("No reptiles are mammals. All snakes are reptiles. So no snakes are mammals.", "Valid. The middle term 'reptiles' is distributed in the first premise."),
       ("All teachers are graduates. Some teachers are women. So some women are graduates.", "Valid. The middle term 'teachers' is distributed in the first premise.")],
      [("Check the middle", "In the correct option, 'vehicles' is the predicate of two A propositions, so it is distributed in neither premise.")],
      T_GR, "Reasoning", "In which argument is the shared term the predicate of two A propositions?"),
    # ---- Other Types of Arguments (4)
    Q("'Kofi has a fever, so he must see a doctor.' This is an enthymeme. Which premise is missing?",
      "Anyone with a fever must see a doctor",
      [("Kofi is a student", "This premise is irrelevant to the conclusion."),
       ("Some people with a fever see a doctor", "This is too weak to give the conclusion."),
       ("Kofi is a doctor", "That would change the argument.")],
      [("Hidden premise", "An enthymeme leaves one premise (or the conclusion) unstated. The hidden premise links the two stated ideas.")],
      T_ENTH, "Application", "Which general statement joins 'fever' to 'see a doctor'?"),
    Q("'If it rains, the road floods. The road did not flood. Therefore it did not rain.' This pattern is called",
      "modus tollens (denying the consequent), which is valid",
      [("modus ponens, which is valid", "Modus ponens affirms the antecedent."),
       ("affirming the consequent, which is invalid", "It would affirm that the road flooded."),
       ("denying the antecedent, which is invalid", "It would deny 'it rains' to reach 'no flood'.")],
      [("The pattern", "If p then q; not q; therefore not p. A truth-table check shows no row with true premises and a false conclusion.")],
      T_HSYL, "Concept", "Is it the consequent or the antecedent that is denied?"),
    Q("A shop sells mangoes or pawpaw, possibly both. 'The shop sells mangoes. Therefore it does not sell pawpaw.' This argument is",
      "invalid, because an inclusive 'or' allows both parts to be true",
      [("valid, by the disjunctive syllogism", "The disjunctive syllogism denies one part to affirm the other. It does not affirm one to deny the other."),
       ("valid, because the first premise is true", "A true premise does not make the form valid."),
       ("invalid, because the conclusion is negative", "A negative conclusion is allowed.")],
      [("Test", "If both parts may be true, the shop can sell mangoes and pawpaw. Premises true, conclusion false: invalid.")],
      T_DSYL, "Reasoning", "Can both parts of the 'or' be true?"),
    Q("'If we plant early, we get a good harvest. If we plant late, we avoid pests. We plant early or we plant late.' Which conclusion follows validly?",
      "We get a good harvest or we avoid pests",
      [("We get a good harvest and we avoid pests", "A constructive dilemma gives a disjunction. A conjunction does not follow."),
       ("We plant early", "The premises give a choice: one of the two."),
       ("If we plant early, we avoid pests", "The two 'if' statements are not mixed in this way.")],
      [("Constructive dilemma", "If p then q; if r then s; p or r; so q or s.")],
      T_CD, "Application", "Which consequent follows from each part of the 'or'?"),
    # ---- Informal Fallacies (3)
    Q("'Do not believe Mr Tabi's report on the water supply. He was once fined for littering.' The fallacy is",
      "argument against the person (ad hominem)",
      [("false cause", "No cause is claimed."),
       ("equivocation", "No word changes its meaning."),
       ("hasty generalisation", "The speaker does not generalise from cases.")],
      [("Man, not argument", "The report is rejected because of a fact about the man, not because of what the report says.")],
      T_FNO, "Application", "Is the attack on the argument or on the arguer?"),
    Q("'I met two rude taxi drivers in Yaounde. So all taxi drivers in Yaounde are rude.' The fallacy is",
      "hasty generalisation",
      [("ad hominem", "No person is attacked."),
       ("equivocation", "No word changes its meaning."),
       ("begging the question", "The conclusion is not simply restated.")],
      [("Too small a sample", "A conclusion about all is drawn from two cases.")],
      T_FLITTLE, "Application", "How many cases support the claim about all?"),
    Q("'Nothing is better than good health. A cold meal is better than nothing. So a cold meal is better than good health.' The fallacy is",
      "equivocation",
      [("ad hominem", "No person is attacked."),
       ("hasty generalisation", "No generalisation from cases is made."),
       ("false cause", "No cause is claimed.")],
      [("One word, two meanings", "'Nothing' means 'no thing' in the first premise and 'a lack of food' in the second.")],
      T_FAMB, "Application", "Which word is used in two ways?"),
]
random.Random(5).shuffle(P1_QUESTIONS)

# =============================================================================================
# 5. Paper 2 practice paper A (structured version: parts written as separate MC / NUM questions)
#    Section A: Questions 1-3 (all answered). Section B: Questions 4-6 (any two answered in the real paper;
#    here all three are given for practice).
# =============================================================================================
use(88)
VX = "f5l-exam-venn-x.svg"
VX_ALT = "Two overlapping circles labelled S and P with an X in the part of circle S that lies outside circle P."

CX1 = ("Question 1 (Section A). A school debate club uses these terms: 'Limbe', 'every nurse', 'some farmers' and "
       "'non-smoker'. ")
CX2 = "Question 2 (Section A). Study the proposition: 'Some farmers in the village are not members of the cooperative.' "
CX3 = ("Question 3 (Section A). Use the traditional square of opposition. Take the proposition "
       "'All the candidates passed the test.' ")
CX4 = ("Question 4 (Section B). Consider the argument: 'All farmers who grow cocoa are members of the cooperative. "
       "Some teachers are members of the cooperative. Therefore some teachers are farmers who grow cocoa.' ")
CX5 = ("Question 5 (Section B). Let r stand for 'the rain comes early' and m for 'the farmers plant maize'. Consider the "
       "argument: 'If the rain comes early, the farmers plant maize. The farmers planted maize. Therefore the rain "
       "came early.' ")
CX6 = ("Question 6 (Section B). Read this passage about a market. (1) 'Do not listen to Mr Ndi's objection to the new "
       "market fees. He is a trader and only wants to protect his own business.' (2) 'Three traders at the north gate "
       "said the fees are too high, so every trader in the town thinks so.' (3) 'Everybody on the main street is paying "
       "the fees without complaint, so the fees must be fair.' ")

P2_Q1 = [
    Q(CX1 + "Question 1(a). Which of these terms is a singular term?",
      "Limbe",
      [("every nurse", "A universal term: it refers to all nurses."),
       ("some farmers", "A particular term: it refers to part of a class."),
       ("non-smoker", "A negative general term, not a name of one individual.")],
      [("Singular term", "A singular term names one individual. Limbe is one town.")],
      T_QQ, "Recall", "Which term names exactly one thing?"),
    Q(CX1 + "Question 1(b). What is the quality of the term 'non-smoker'?",
      "Negative",
      [("Positive", "A positive term names the presence of a quality. 'Non-' denies it."),
       ("Singular", "Singular describes the quantity of a term, not its quality."),
       ("Universal", "Universal describes quantity, not quality.")],
      [("Quality of terms", "Terms are positive or negative in quality. 'Non-smoker' is negative.")],
      T_QQ, "Concept", "Quality means positive or negative."),
    Q(CX1 + "Question 1(c). Which term has the greater extension: 'tree' or 'mango tree'?",
      "'tree', because it applies to more things and has less comprehension",
      [("'mango tree', because it has more qualities", "More qualities means greater comprehension, but a smaller extension."),
       ("Both have the same extension", "Every mango tree is a tree, but not every tree is a mango tree, so the extensions differ."),
       ("'mango tree', because it is a longer phrase", "The number of words is not extension.")],
      [("Inverse relation", "When extension grows, comprehension shrinks. 'Tree' covers all trees, 'mango tree' only some.")],
      T_IDEAS, "Concept", "Which term applies to more individuals?"),
    Q(CX1 + "Question 1(d). In the definition 'A pentagon is a polygon with five sides', which word names the genus?",
      "polygon",
      [("pentagon", "This is the term being defined."),
       ("five sides", "This is the specific difference."),
       ("with", "A connecting word, not a part of the definition.")],
      [("Genus and difference", "The genus is the wider class to which the thing belongs (polygon). The difference marks it off (five sides).")],
      T_KINDS, "Recall", "Which word names the wider class?"),
    Q(CX1 + "Question 1(e). A school divides its students into 'boys, girls and prefects'. What is the main fault in this division?",
      "Two bases are used at once (sex and office), so the members overlap",
      [("The members together are less than the whole: some students are left out", "Every student is a boy or a girl, so no student is left out."),
       ("The whole is too small to be divided", "Any class with several members can be divided."),
       ("Division must have exactly two members", "No rule fixes the number of members.")],
      [("One basis at a time", "A good division uses one basis. A prefect is also a boy or a girl, so the members overlap.")],
      T_DIV, "Reasoning", "Can a student be in two of the three groups?"),
]

P2_Q2 = [
    Q(CX2 + "Question 2(a). What is the subject term of this proposition?",
      "farmers in the village",
      [("members of the cooperative", "This is the predicate term."),
       ("are not", "This is the copula."),
       ("Some", "This is the quantifier, which shows quantity.")],
      [("Components", "Subject: farmers in the village. Copula: are not. Predicate: members of the cooperative.")],
      T_PCOMP, "Recall", "What is the statement about?"),
    Q(CX2 + "Question 2(b). Name the type of this proposition by quantity and quality.",
      "Particular negative (O)",
      [("Universal negative (E)", "'Some' makes it particular, not universal."),
       ("Particular affirmative (I)", "'are not' makes it negative."),
       ("Universal affirmative (A)", "It is neither universal nor affirmative.")],
      [("Quantity and quality", "'Some' is particular and 'are not' is negative: an O proposition.")],
      T_PPROP, "Recall", "Look at 'Some' and 'are not'."),
    N(CX2 + "Question 2(c). How many terms are distributed in this proposition?", 1,
      [("Rule for O", "An O proposition (Some S are not P) distributes its predicate only."), ("Count", "Only 'members of the cooperative' is distributed. So the answer is 1.")],
      T_DIST, "Calculation", "O distributes one of its two terms: which?"),
    Q(CX2 + "Question 2(d). In the Venn diagram, S stands for 'farmers in the village' and P for 'members of the cooperative'. Which statement does the diagram show?",
      "Some farmers in the village are not members of the cooperative",
      [("All farmers in the village are members of the cooperative", "That would shade the part of S outside P."),
       ("No farmers in the village are members of the cooperative", "That would shade the overlap."),
       ("Some farmers in the village are members of the cooperative", "That would put the X in the overlap.")],
      [("Read the X", "The X is in S and outside P: at least one farmer is not a member.")],
      T_VENN, "Interpretation", "In which region of the circles is the X?",
      diagram=VX, alt=VX_ALT),
    Q(CX2 + "Question 2(e). Which is the correct standard form of 'Only members of the cooperative may vote'?",
      "All persons who may vote are members of the cooperative",
      [("All members of the cooperative are persons who may vote", "This reverses the statement. 'Only members' does not say that every member votes."),
       ("Some members of the cooperative are persons who may vote", "This is weaker and different in meaning."),
       ("No members of the cooperative are persons who may vote", "This contradicts the statement.")],
      [("'Only' reverses", "'Only S are P' becomes 'All P are S'. Here S = members, P = persons who may vote. Check your textbook for the rule on 'only'.")],
      T_TRANS, "Application", "Who is allowed to vote: members only, or everyone?"),
]

P2_Q3 = [
    Q(CX3 + "Question 3(a). Which proposition is the contradictory of the given proposition?",
      "Some candidates did not pass the test",
      [("No candidates passed the test", "This is the contrary, not the contradictory."),
       ("Some candidates passed the test", "This is the subaltern, which agrees with it."),
       ("All the candidates failed the test", "Too strong: it is a contrary form.")],
      [("Diagonals", "The contradictory of All S are P is Some S are not P.")],
      T_OPP, "Recall", "Which corner is on the other end of the diagonal?"),
    Q(CX3 + "Question 3(b). If 'All the candidates passed the test' is TRUE, what is the truth value of 'Some candidates passed the test'?",
      "True",
      [("False", "A false value would be for the contrary or the contradictory, not for the subaltern."),
       ("Undetermined", "Under the traditional square, a true universal makes its subaltern true."),
       ("Both true and false", "No proposition is both true and false at the same time in the same sense.")],
      [("Subalternation", "On the traditional square, from A true we may infer I true. In the modern Boolean view this step is not allowed unless the class is known to have members.")],
      T_SQ, "Reasoning", "What does the vertical line on the left of the square tell you?"),
    Q(CX3 + "Question 3(c). If 'All the candidates passed the test' is FALSE, which statement must then be true?",
      "Some candidates did not pass the test",
      [("No candidates passed the test", "The contrary can be false too, as when some candidates passed and some failed."),
       ("Some candidates passed the test", "This is not forced: it is possible that none passed."),
       ("Some candidates passed the test and some did not", "The second half is forced but the first half is not.")],
      [("Contradictory", "If A is false then its contradictory O is true. E and I remain undetermined.")],
      T_SQ, "Reasoning", "Which proposition always has the opposite truth value of A?"),
    Q(CX3 + "Question 3(d). Which is the obverse of the given proposition?",
      "No candidates are persons who did not pass the test",
      [("All persons who passed the test are candidates", "This is the converse."),
       ("Some candidates did not pass the test", "This is the contradictory."),
       ("All candidates are persons who did not pass the test", "The quality was not changed, so the meaning is reversed.")],
      [("Obversion", "Change the quality (A becomes E) and replace the predicate by its complement: No candidates are non-passers.")],
      T_EDU, "Application", "Change the quality and complement the predicate."),
    Q(CX3 + "Question 3(e). Which is the contrapositive of the given proposition?",
      "All persons who did not pass the test are non-candidates",
      [("All persons who passed the test are candidates", "This is the converse of the original."),
       ("No persons who did not pass the test are non-candidates", "This has the wrong quality."),
       ("All non-candidates are persons who did not pass the test", "This is the converse of the contrapositive. It is not equivalent to the original.")],
      [("Contraposition", "Replace the subject by the complement of the predicate and the predicate by the complement of the subject: All non-P are non-S.")],
      T_EDU, "Application", "Complement both terms and swap them."),
]

P2_Q4 = [
    Q(CX4 + "Question 4(a). Which is the major term of this syllogism?",
      "farmers who grow cocoa",
      [("members of the cooperative", "This is the middle term: it appears in both premises."),
       ("teachers", "This is the minor term: the subject of the conclusion."),
       ("cocoa", "A word inside a term, not a term by itself.")],
      [("Major term", "The major term is the predicate of the conclusion: farmers who grow cocoa.")],
      T_SYLL, "Recall", "Which term is the predicate of the conclusion?"),
    Q(CX4 + "Question 4(b). What are the mood and the figure of this syllogism?",
      "AII in the second figure",
      [("AII in the first figure", "In the first figure the middle term is the subject of the major and the predicate of the minor."),
       ("AII in the third figure", "In the third figure the middle term is the subject of both premises."),
       ("IAI in the second figure", "The major premise is universal affirmative (A) and the minor is particular affirmative (I): AII.")],
      [("Mood", "Major: All P are M (A). Minor: Some S are M (I). Conclusion: Some S are P (I)."), ("Figure", "The middle term is the predicate of both premises: figure 2.")],
      T_MOOD, "Application", "Order the propositions: major, minor, conclusion."),
    N(CX4 + "Question 4(c). In how many of the two premises is the middle term distributed?", 0,
      [("A proposition", "In 'All P are M' the predicate M is not distributed."), ("I proposition", "In 'Some S are M' neither term is distributed."), ("Count", "0 premises distribute the middle term.")],
      T_GR, "Calculation", "Is the predicate of an A proposition distributed? Of an I proposition?"),
    Q(CX4 + "Question 4(d). Which verdict and reason are correct?",
      "Invalid: the middle term is undistributed in both premises",
      [("Valid: the conclusion is particular and so it is safe", "A particular conclusion can still be invalid."),
       ("Valid: the premises are true", "Truth of the premises does not make the form valid."),
       ("Invalid: a universal premise cannot be used with a particular one", "No such rule: Barbara-type arguments with a universal and a particular premise can be valid.")],
      [("Rule", "The middle term must be distributed at least once. It is distributed in neither premise, so the form is invalid (fallacy of the undistributed middle).")],
      T_GR, "Reasoning", "Which general rule does the middle term break?"),
    Q(CX4 + "Question 4(e). Which argument has the same form and so shows, with true premises and a false conclusion, that this form is invalid?",
      "All dogs are animals. Some cats are animals. Therefore some cats are dogs.",
      [("All dogs are animals. Some animals are cats. Therefore some cats are dogs.", "This has true premises and a false conclusion, but its form is different: the middle term is in different places. It shows another form is invalid."),
       ("All dogs are animals. All cats are animals. Therefore all cats are dogs.", "The conclusion is universal (A), so the mood differs: AAA, not AII."),
       ("All dogs are fish. Some cats are fish. Therefore some cats are dogs.", "The premises are false, so this does not show that the form allows true premises with a false conclusion.")],
      [("Match the form", "Same form: All P are M; Some S are M; so Some S are P. With P = dogs, M = animals, S = cats the premises are true and the conclusion is false: a counterexample.")],
      T_SVENN, "Reasoning", "Replace P, M and S by everyday terms in the same positions."),
]

P2_Q5 = [
    Q(CX5 + "Question 5(a). Which is the correct symbolisation of the whole argument?",
      "r ⊃ m, m, therefore r",
      [("m ⊃ r, m, therefore r", "The first premise is reversed: it says maize planting brings early rain."),
       ("r . m, m, therefore r", "The first premise is a condition, not an 'and'."),
       ("r v m, m, therefore r", "The first premise is a condition, not an 'or'.")],
      [("Antecedent first", "'If r then m' is r ⊃ m. The second premise is m. The conclusion is r.")],
      T_CONN, "Application", "Which part follows 'if'?"),
    N(CX5 + "Question 5(b). How many rows does the truth table of this argument have?", 4,
      [("Two letters", "The argument has two statement letters, r and m."), ("Rows", "2 x 2 = 4 rows.")],
      T_STRUCT, "Calculation", "How many different letters are there?"),
    Q(CX5 + "Question 5(c). In the row where r is false and m is true, what are the truth values of premise 1 (r ⊃ m), premise 2 (m) and the conclusion (r), in that order?",
      "true, true, false",
      [("false, true, false", "r ⊃ m is true when its antecedent is false."),
       ("true, true, true", "The conclusion r is false in this row."),
       ("true, false, false", "m is true in this row.")],
      [("Substitute", "r ⊃ m with r false is true. m is true. r is false.")],
      T_TT, "Calculation", "A conditional with a false antecedent is true."),
    N(CX5 + "Question 5(d). In how many rows of the truth table are BOTH premises true?", 2,
      [("List rows (r, m)", "T,T: premises true, true. T,F: r ⊃ m false. F,T: true, true. F,F: premise 2 false."), ("Count", "Both premises are true in 2 rows: (T,T) and (F,T).")],
      T_TT, "Calculation", "Write the four rows and check both premises in each."),
    Q(CX5 + "Question 5(e). What is the verdict, with its reason?",
      "Invalid: in the row r false, m true, both premises are true and the conclusion is false",
      [("Valid: whenever r is true, m is true", "That is what the first premise says, but validity needs the conclusion to be true in every row where both premises are true."),
       ("Valid: the conclusion is true in one of the rows with true premises", "It must be true in every such row."),
       ("Invalid: the conclusion is false in every row", "It is true in two rows.")],
      [("Counterexample row", "A single row with true premises and a false conclusion proves invalidity. Here that row is r false, m true.")],
      T_VS, "Reasoning", "Look for a row with true premises and a false conclusion."),
    Q(CX5 + "Question 5(f). What is the name of this fallacy?",
      "Affirming the consequent",
      [("Denying the antecedent", "That would deny r to conclude not-m."),
       ("Modus ponens", "A valid form, which affirms the antecedent."),
       ("Modus tollens", "A valid form, which denies the consequent.")],
      [("Name it", "The second premise affirms the consequent (m) of the first, and the conclusion affirms the antecedent (r). This is the fallacy of affirming the consequent.")],
      T_HSYL, "Recall", "Which part of the conditional does the second premise affirm?"),
]

P2_Q6 = [
    Q(CX6 + "Question 6(a). Which fallacy is committed in sentence (1)?",
      "Argument against the person (ad hominem)",
      [("Hasty generalisation", "No generalisation from cases is made."),
       ("Equivocation", "No word changes its meaning."),
       ("False cause", "No cause is claimed.")],
      [("Person, not reasons", "The objection is dismissed because of who Mr Ndi is, without examining his reasons.")],
      T_FNO, "Application", "Is the attack on the objection or on the person?"),
    Q(CX6 + "Question 6(b). Which fallacy is committed in sentence (2)?",
      "Hasty generalisation",
      [("Argument against the person", "No person is attacked."),
       ("Equivocation", "No word changes its meaning."),
       ("Appeal to the people", "This is the reasoning of sentence (3), not (2).")],
      [("Small sample", "A conclusion about every trader is drawn from three traders at one gate.")],
      T_FLITTLE, "Application", "How many cases support the claim about all?"),
    Q(CX6 + "Question 6(c). Which fallacy is committed in sentence (3)?",
      "Appeal to the people (argumentum ad populum)",
      [("Argument against the person", "No person is attacked."),
       ("Equivocation", "No word changes its meaning."),
       ("False cause", "No cause is claimed.")],
      [("Popularity", "'Everybody is paying' says that many accept the fees. It does not say whether they are fair.")],
      T_FNO, "Application", "Is popularity the only reason given?"),
    Q(CX6 + "Question 6(d). Which change would make the reasoning of sentence (2) stronger?",
      "Ask traders chosen at random from every part of the town",
      [("Ask three more traders at the north gate", "A bigger group at the same gate is still a small and biased sample."),
       ("Say the word 'every' louder", "Emphasis is not evidence."),
       ("Ask only the traders who agree", "This makes the sample biased.")],
      [("Better sample", "A larger and representative sample, drawn from all parts of the town, gives better support.")],
      T_FLITTLE, "Interpretation", "How can the sample represent the whole town?"),
    Q(CX6 + "Question 6(e). If a critic shows that sentence (3) is a fallacy, what has been shown?",
      "The reasoning is weak, but this does not prove that the conclusion is false",
      [("The conclusion is false", "A fallacy shows poor support. The conclusion may still be true or false."),
       ("The speaker is dishonest", "A fallacy may be a mistake without any dishonesty."),
       ("The conclusion must be true", "Faulty reasoning does not prove a conclusion true.")],
      [("Fallacy and conclusion", "A fallacy is an error in reasoning. It means this argument does not support the conclusion, not that the conclusion is false.")],
      T_FDEF, "Interpretation", "A fallacy attacks the support, not the conclusion."),
]

P2_QUESTIONS = P2_Q1 + P2_Q2 + P2_Q3 + P2_Q4 + P2_Q5 + P2_Q6

SETS = [
    practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 strategies practice",
                 lesson="exam-paper-1-multiple-choice-strategies", questions=SET1),
    practice_set(module=M_EXAM, topic="Paper 2", title="Section A structural questions practice",
                 lesson="exam-paper-2-section-a-structural-questions", questions=SET2),
    practice_set(module=M_EXAM, topic="Paper 2", title="Section B problem-solving practice",
                 lesson="exam-paper-2-section-b-problem-solving-questions", questions=SET3),
    practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A",
                 lesson="exam-paper-1-multiple-choice-strategies", mock=True, time_limit_minutes=90,
                 questions=P1_QUESTIONS),
    practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A",
                 lesson="exam-paper-2-section-a-structural-questions", mock=True, time_limit_minutes=150,
                 questions=P2_QUESTIONS),
]
