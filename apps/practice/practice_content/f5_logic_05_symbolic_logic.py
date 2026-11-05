"""Form 5 Logic practice: Introduction to Symbolic Logic (one set per lesson, 8 questions each).

Symbols: ~ (not), . (and), v (inclusive or), ⊃ (if ... then), ≡ (if and only if).
"""
from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")
_M = "Introduction to Symbolic Logic"


def _mc(prompt, right, wrongs, pos, steps, concept, skill, hint, feedback=""):
    """Multiple choice: `right` is the correct text, `wrongs` three (text, why) pairs, `pos` the 0-based place of the right one."""
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(right, correct=True))
    return MC(prompt, choices, steps=steps, concept=concept, skill=skill, hint=hint, feedback=feedback)


SETS = []


SETS.append(practice_set(
    module=_M, topic="Basic notions and the importance of symbolic logic",
    title="Statements, forms and symbols", lesson="sym-what-is-symbolic-logic",
    questions=[
        _mc("Which of these is a statement?", "Limbe is on the coast.", [
            ("Close the window.", "This is a command. It cannot be true or false."),
            ("Is Kumba far from Buea?", "This is a question. It cannot be true or false."),
            ("What a lovely day!", "This is an exclamation. It cannot be true or false."),
        ], 2, [S("Test each sentence", text="A statement is true or false. A command, a question and an exclamation are neither."),
               S("Decide", text="“Limbe is on the coast” is a statement.")],
            "Statement", "Recall", "Ask yourself: can this sentence be true or false?",
            "A statement is a sentence that is true or false, but not both."),
        _mc("What is the main advantage of writing arguments with symbols?", "They show the form clearly and remove ambiguity.", [
            ("They make false statements true.", "Symbols do not change the truth of a statement."),
            ("They tell us whether the facts are true.", "Logic studies reasoning from given statements. Facts come from observation."),
            ("They can be used only in mathematics.", "Symbols are used for statements of every subject."),
        ], 1, [S("Recall the reasons", text="Clarity, no ambiguity, and study of form apart from content."),
               S("Match", text="The first option says this.")],
            "Importance of symbolic logic", "Concept", "Think of the sentence about Mathematics, Physics and Chemistry that could be read in two ways.",
            "Symbols have fixed meanings and brackets show grouping."),
        _mc("Which of these is a compound statement?", "Ama sings and Bih dances.", [
            ("Ama sings.", "It has one claim and no part that is itself a statement: a simple statement."),
            ("Where is Ama?", "This is a question, not a statement at all."),
            ("Sing, Ama!", "This is a command, not a statement."),
        ], 3, [S("Look for a connective", text="A compound statement contains simple statements joined by words such as and, or, not, if."),
               S("Find it", text="“Ama sings and Bih dances” joins two simple statements by “and”.")],
            "Simple and compound statements", "Recall", "Look for two statements joined by a connective.",
            "A compound statement is built from simple statements and connectives."),
        _mc("In “It is raining and the road is wet”, the simple statements and the connective are:", "“It is raining”, “The road is wet” and the connective “and”.", [
            ("“It is raining and the road is wet” and no connective.", "The sentence is compound: “and” joins two parts."),
            ("“It is raining”, “The road is wet” and the connective “wet”.", "“Wet” is part of a simple statement, not a connective."),
            ("Only one simple statement and the connective “raining”.", "There are two claims, so two simple statements."),
        ], 0, [S("Split at the connective", text="“and” joins “It is raining” and “The road is wet”."),
               S("Count", text="Two simple statements and one connective.")],
            "Simple and compound statements", "Application", "Which word joins two complete claims?",
            "Connectives join statements."),
        _mc("“Ama sings and Bih dances” and “The sun is hot and the sea is calm” differ in:", "content only: they have the same form.", [
            ("form only: they have the same content.", "Their content is different (singing and dancing versus sun and sea)."),
            ("both form and content.", "Both have the form “p and q”."),
            ("neither form nor content.", "The topics are different, so the content differs."),
        ], 0, [S("Replace each simple statement by a letter", text="The first is p and q. The second is also p and q."),
               S("Compare", text="Same form, different content.")],
            "Form and content", "Concept", "Replace the simple statements by letters and compare the patterns.",
            "Form is the pattern; content is the subject matter."),
        _mc("“Students who pass Mathematics or Physics and Chemistry get a prize.” Why is this sentence a problem for clear reasoning?", "It is ambiguous: it can be grouped in more than one way.", [
            ("It is a question.", "It is a statement."),
            ("It contains no connective.", "It contains “or” and “and”."),
            ("It is false.", "The difficulty is not its truth but its different possible readings."),
        ], 1, [S("Look at the grouping", text="“(Mathematics or Physics) and Chemistry” and “Mathematics or (Physics and Chemistry)” are two different readings."),
               S("Name the problem", text="Ambiguity.")],
            "Ambiguity", "Reasoning", "Try to read it in two ways.",
            "Symbols and brackets remove ambiguity."),
        NUM("How many simple statements are in: “Ama sings, Bih dances and Cara plays the drums”?", 3,
            steps=[S("Split", text="Ama sings. Bih dances. Cara plays the drums."), S("Count", text="Three simple statements joined by connectives.")],
            concept="Simple and compound statements", skill="Application", hint="Mark each complete claim separately.",
            feedback="Each complete claim is a simple statement."),
        _mc("Which of these is NOT a reason for using symbols in logic?", "Symbols prove that the premises are true.", [
            ("Symbols give clarity: long sentences become short formulas.", "This is a real reason."),
            ("Symbols remove ambiguity.", "This is a real reason."),
            ("Symbols let us study the form of reasoning apart from content.", "This is a real reason."),
        ], 3, [S("Check each option", text="The first three are the standard benefits of symbols."),
               S("Find the odd one", text="Symbols describe form. They cannot prove that a premise is true.")],
            "Importance of symbolic logic", "Reasoning", "Which option claims more than symbols can do?",
            "Symbols help with form, not with facts."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Connectives and symbols in symbolic logic",
    title="Negation, conjunction and disjunction", lesson="sym-negation-conjunction-disjunction",
    questions=[
        _mc("p is true and q is false. Which of these is true?", "p v q", [
            ("p . q", "A conjunction needs both parts true, but q is false."),
            ("~p v q", "~p is false and q is false, so the disjunction is false."),
            ("~p . q", "~p is false, so the conjunction is false."),
        ], 2, [S("Find the values", text="p = T, q = F, ~p = F, ~q = T."),
               S("Evaluate", text="p . q = F; ~p v q = F; p v q = T; ~p . q = F.")],
            "Truth values of ~, . and v", "Calculation", "Work out ~p first.",
            "p v q is true when at least one disjunct is true."),
        _mc("The disjunction p v q is false only when:", "p and q are both false.", [
            ("exactly one of p, q is false.", "If one is true, the disjunction is true."),
            ("p and q are both true.", "v is inclusive: both true makes it true."),
            ("p is false, whatever q is.", "If q is true, the disjunction is still true."),
        ], 0, [S("Recall the table", text="p v q is T, T, T, F in the rows TT, TF, FT, FF."),
               S("Read", text="The only F is the row with both false.")],
            "Disjunction", "Recall", "Look at the last row of the truth table of v.",
            "p v q is false only if both disjuncts are false."),
        _mc("“The bus is old but it is fast.” With p for “The bus is old” and q for “The bus is fast”, the symbolic form is:", "p . q", [
            ("p v q", "“But” does not mean “or”. Both parts are claimed."),
            ("~p . q", "Nothing in the sentence is negated."),
            ("p ⊃ q", "There is no “if ... then” in the sentence."),
        ], 1, [S("Translate “but”", text="But, although, however and yet have the same truth conditions as “and”."),
               S("Write", text="p . q.")],
            "Translating but and and", "Application", "What makes the sentence true? Both facts.",
            "“But” is written with the dot."),
        _mc("“The match will be played unless it rains.” With m for “The match is played” and r for “It rains”, the usual symbolic form is:", "m v r", [
            ("m . r", "This says that the match is played and it rains, which is not what “unless” says."),
            ("m . ~r", "This is stronger: it rules out the match being played in the rain."),
            ("m ⊃ r", "This says that if the match is played, it rains: the wrong direction."),
        ], 3, [S("Rule", text="“p unless q” is written p v q (most textbooks)."),
               S("Write", text="m v r.")],
            "Translating unless", "Application", "“Unless” is written with the same connective as “or”.",
            "p unless q = p v q."),
        NUM("How many of the four rows of the truth table of p v q make p v q true?", 3,
            steps=[S("List", text="Rows TT, TF, FT, FF give T, T, T, F."), S("Count", text="Three rows are true.")],
            concept="Disjunction", skill="Calculation", hint="Write the four rows and evaluate each.",
            feedback="p v q is true in every row except the one where both are false."),
        _mc("Ama buys both rice and beans. Let p be “Ama buys rice” and q be “Ama buys beans”. With the symbol v, the truth value of p v q is:", "true, because v is the inclusive “or”.", [
            ("false, because “or” means only one of them.", "That is the exclusive “or”. The symbol v is inclusive."),
            ("false, because both are true.", "A disjunction is false only when both disjuncts are false."),
            ("it cannot be decided.", "The truth table settles it: row TT gives T."),
        ], 3, [S("Recall", text="v means “p, or q, or both”."),
               S("Evaluate", text="Both p and q are true, which is row TT of p v q: T.")],
            "Inclusive or", "Concept", "Does v exclude the case where both are true?",
            "In symbolic logic, v is inclusive."),
        _mc("p is true, q is true and r is false. Which of these is true?", "q . ~r", [
            ("p . r", "r is false, so the conjunction is false."),
            ("~p v r", "~p is false and r is false."),
            ("~q v r", "~q is false and r is false."),
        ], 2, [S("Values", text="~p = F, ~q = F, ~r = T."),
               S("Evaluate", text="p . r = F; ~p v r = F; q . ~r = T; ~q v r = F.")],
            "Truth values of ~, . and v", "Calculation", "Write down ~p, ~q and ~r before you start.",
            "Only q . ~r has both parts true."),
        _mc("Which pair of everyday expressions is normally written with the same symbol?", "“and” and “although”", [
            ("“or” and “and”", "They are written with different symbols (v and the dot)."),
            ("“not” and “unless”", "“Not” is ~, and “unless” is v."),
            ("“although” and “or”", "“Although” is the dot and “or” is v."),
        ], 0, [S("Recall", text="Dot: and, but, although, however, yet. v: or, unless. ~: not."),
               S("Match", text="“And” and “although” are both the dot.")],
            "Translating everyday words", "Concept", "List the words that mean that both parts are claimed.",
            "The connective is chosen by truth conditions, not by the feeling of the word."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Connectives and symbols in symbolic logic",
    title="Implication and the biconditional", lesson="sym-implication-and-biconditional",
    questions=[
        _mc("The implication p ⊃ q is false only when:", "p is true and q is false.", [
            ("p and q are both true.", "Then the promise is kept: the implication is true."),
            ("p is false and q is true.", "A false antecedent makes the implication true."),
            ("p and q are both false.", "A false antecedent makes the implication true."),
        ], 0, [S("Think of a promise", text="“If you pass, I buy a phone” is broken only when you pass and there is no phone."),
               S("Match", text="Antecedent true, consequent false.")],
            "Material implication", "Recall", "When is a promise broken?",
            "p ⊃ q is false only for T then F."),
        _mc("“If it rains, the match is cancelled.” With r for “It rains” and m for “The match is cancelled”, the symbolic form is:", "r ⊃ m", [
            ("m ⊃ r", "This reverses the sentence: it says that if the match is cancelled, it rains."),
            ("r ≡ m", "This would say “if and only if”, which is stronger."),
            ("r . m", "This says that both happen, which the sentence does not claim."),
        ], 2, [S("Antecedent", text="The “if” part is “It rains”: r."),
               S("Write", text="r ⊃ m.")],
            "Translating if", "Application", "Which statement follows the word “if”?",
            "The “if” part is the antecedent."),
        _mc("“Ama passes only if she studies.” With p for “Ama passes” and s for “Ama studies”, the symbolic form is:", "p ⊃ s", [
            ("s ⊃ p", "This says that studying is enough to pass. “Only if” does not say this."),
            ("p ≡ s", "“Only if” gives one direction only."),
            ("p . s", "The sentence does not claim that both are true."),
        ], 3, [S("Rule", text="“p only if q” is p ⊃ q: the part after “only if” is the consequent."),
               S("Write", text="p ⊃ s.")],
            "Only if", "Application", "Which part follows “only if”? It is the consequent.",
            "“Only if” introduces the consequent."),
        NUM("How many of the four rows of the truth table of p ≡ q make p ≡ q true?", 2,
            steps=[S("Recall", text="p ≡ q is true when p and q have the same truth value."),
                   S("Count", text="Row TT and row FF: two rows.")],
            concept="Biconditional", skill="Calculation", hint="In which rows do p and q have the same value?",
            feedback="p ≡ q is T, F, F, T."),
        _mc("A father promises: “If you pass, I will buy you a phone.” You fail, but he buys you a phone anyway. Was his promise broken?", "No: with a false antecedent the implication is true.", [
            ("Yes: he bought a phone although you failed.", "The promise only spoke about what happens if you pass. Buying a phone otherwise does not break it."),
            ("Yes: the promise needs both parts to be true.", "That would be a conjunction, not an implication."),
            ("It cannot be decided.", "The truth table settles it: F antecedent, T consequent gives T."),
        ], 3, [S("Values", text="Antecedent (you pass): false. Consequent (phone): true."),
               S("Row", text="False antecedent, true consequent: the implication is true.")],
            "Material implication", "Application", "In which cases is the promise broken?",
            "A conditional is false only for true antecedent and false consequent."),
        _mc("p is false and q is false. Which of these is false?", "p . ~q", [
            ("p ⊃ q", "A false antecedent makes it true."),
            ("q ⊃ p", "A false antecedent makes it true."),
            ("~p ≡ ~q", "~p and ~q are both true, so the biconditional is true."),
        ], 3, [S("Values", text="~p = T and ~q = T."),
               S("Evaluate", text="p ⊃ q = T; q ⊃ p = T; ~p ≡ ~q = T; p . ~q = F . T = F.")],
            "Truth values of ⊃ and ≡", "Calculation", "Work out ~p and ~q first.",
            "Only the conjunction with a false conjunct is false."),
        _mc("“You can enter the hall if and only if you have your identity card.” With e for “You can enter the hall” and i for “You have your identity card”, the symbolic form is:", "e ≡ i", [
            ("i ⊃ e", "This says only that having the card is enough. It misses “only if”."),
            ("e ⊃ i", "This says only that the card is necessary. It misses “if”."),
            ("e . i", "This says that both are true, which the sentence does not claim."),
        ], 2, [S("Meaning", text="“If and only if” means both directions: e ⊃ i and i ⊃ e."),
               S("Write", text="e ≡ i.")],
            "Biconditional", "Application", "Is the sentence about one direction or two?",
            "“If and only if” is the biconditional."),
        _mc("p ⊃ q is true and q is false. What can you say about p?", "p is false.", [
            ("p is true.", "If p were true and q false, p ⊃ q would be false."),
            ("p can be true or false.", "Only one value of p makes p ⊃ q true when q is false."),
            ("Nothing can be said.", "The row TF is excluded because it makes p ⊃ q false, so p must be false."),
        ], 1, [S("Rows with q false", text="TF: p ⊃ q is F. FF: p ⊃ q is T."),
               S("Choose the row where p ⊃ q is true", text="Row FF: p is false.")],
            "Material implication", "Reasoning", "Which row with q false makes p ⊃ q true?",
            "Use the truth table in reverse."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Logical constants (truth-functional statements)",
    title="Logical constants and truth-functional statements", lesson="sym-logical-constants-and-truth-functional-statements",
    questions=[
        _mc("Which list contains the logical constants used in this course?", "~, ., v, ⊃, ≡", [
            ("p, q, r, s, t", "These are statement variables, which change from one example to another."),
            ("T, F", "These are truth values, not connectives."),
            ("+, -, x, ÷", "These are arithmetic signs."),
        ], 0, [S("Recall", text="The constants are the connectives with fixed meaning."),
               S("List", text="Not, and, or, if ... then, if and only if: ~, ., v, ⊃, ≡.")],
            "Logical constants", "Recall", "Which symbols have a fixed meaning in every example?",
            "Variables change; constants do not."),
        _mc("A compound statement is truth-functional when:", "its truth value is fixed by the truth values of its components.", [
            ("all its components are true.", "A truth-functional statement can have false components."),
            ("its components are about the same subject.", "The subject does not matter."),
            ("it is always true.", "Only tautologies are always true."),
        ], 1, [S("Recall the definition", text="“Function” means one output for each input."),
               S("Apply", text="The truth values of the parts settle the truth value of the whole.")],
            "Truth-functional statements", "Recall", "Think of the word “function”.",
            "Truth-functional: the truth value of the whole depends only on the truth values of the parts."),
        _mc("Which of these compound statements is NOT truth-functional?", "Ama believes that the exam is easy.", [
            ("The exam is easy and the paper is short.", "This is a conjunction, a logical constant."),
            ("The exam is not easy.", "This is a negation, a logical constant."),
            ("If the exam is easy, then everybody passes.", "This is an implication, a logical constant."),
        ], 2, [S("Test", text="Does the truth of “the exam is easy” settle the truth of the whole?"),
               S("Decide", text="For “Ama believes ...”, it does not. Ama may believe falsely or fail to believe a true thing.")],
            "Truth-functional statements", "Concept", "Which compound uses a word that is not one of the five connectives?",
            "“Believes” is not a truth-functional connective."),
        NUM("p is true, q is false and r is true. How many of these four statements are true: p . q, p v q, q ⊃ r, p ≡ q?", 2,
            steps=[S("p . q", text="F."), S("p v q", text="T."), S("q ⊃ r", text="Antecedent q is false: T."),
                   S("p ≡ q", text="Different values: F."), S("Count", text="Two are true.")],
            concept="Truth values of compound statements", skill="Calculation", hint="Evaluate the four statements one at a time.",
            feedback="p v q and q ⊃ r are true."),
        _mc("p is true and q is false. Which of these is true?", "q ⊃ p", [
            ("p ⊃ q", "True antecedent and false consequent: false."),
            ("p ≡ q", "Different truth values: false."),
            ("~p v q", "~p is false and q is false: false."),
        ], 1, [S("Evaluate", text="p ⊃ q = F; q ⊃ p = T (false antecedent); p ≡ q = F; ~p v q = F."),
               S("Choose", text="q ⊃ p.")],
            "Truth values of compound statements", "Calculation", "A false antecedent makes an implication true.",
            "Check each option with the truth tables."),
        _mc("Let p be “Yaoundé is in Cameroon” (true) and q be “2 + 2 = 5” (false). The statement p v q is:", "true, because one disjunct is true.", [
            ("false, because q is false.", "A disjunction is false only if both disjuncts are false."),
            ("false, because the two statements are about different subjects.", "The subject does not matter in a truth table."),
            ("neither true nor false.", "A compound of two statements is true or false."),
        ], 2, [S("Values", text="p = T, q = F."), S("v", text="T v F is T.")],
            "Truth values of compound statements", "Application", "One true disjunct is enough.",
            "Truth tables use only truth values."),
        _mc("“The road is flooded because it rained.” Can this be written as p . q with p for “It rained” and q for “The road is flooded”?", "No, because “because” is not truth-functional: p and q may both be true and the “because” claim false.", [
            ("Yes, because “because” means “and”.", "“Because” claims a link that “and” does not claim."),
            ("Yes, because every compound statement is truth-functional.", "Some compounds are not, such as those with “because” or “believes”."),
            ("No, because the sentence is a question.", "It is a statement."),
        ], 2, [S("Test", text="Suppose p and q are both true. Is the “because” claim certainly true?"),
               S("Decide", text="No: the road might be flooded because a pipe burst. So the truth values of the parts do not settle the truth of the whole.")],
            "Truth-functional statements", "Reasoning", "Does knowing that both parts are true settle the “because” claim?",
            "Do not translate “because” with the dot."),
        _mc("p is false and q is false. Which of these compound statements is true?", "p ⊃ q", [
            ("p . q", "A conjunction with a false conjunct is false."),
            ("p v q", "A disjunction with both disjuncts false is false."),
            ("p . ~q", "p is false, so the conjunction is false."),
        ], 3, [S("Evaluate", text="p . q = F; p v q = F; p ⊃ q = T (false antecedent); p . ~q = F.")],
            "Truth values of compound statements", "Reasoning", "Which connective gives T when both parts are false?",
            "A compound can be true although its components are false."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Punctuation in symbolic logic",
    title="Brackets and the main connective", lesson="sym-punctuation-brackets-and-main-connective",
    questions=[
        _mc("Why are brackets needed in a formula such as p . q v r?", "Without them the formula can be grouped in two ways with different meanings.", [
            ("Brackets make the formula true.", "Brackets show grouping. They do not change truth values by themselves."),
            ("Brackets show which variables are false.", "Brackets say nothing about truth values."),
            ("Brackets are decoration only.", "Different groupings give different truth tables."),
        ], 0, [S("Compare", text="(p . q) v r and p . (q v r) differ when p is false and r is true."),
               S("Conclude", text="So the grouping must be shown.")],
            "Punctuation", "Concept", "Try to read p . q v r in two ways.",
            "Brackets remove ambiguity."),
        _mc("What is the main connective of ~(p . q)?", "~", [
            ("The dot.", "The dot is inside the brackets: it joins only p and q."),
            ("There is no main connective.", "Every formula with a connective has one."),
            ("p", "p is a variable, not a connective."),
        ], 2, [S("Look outside the brackets", text="A ~ stands in front of the whole bracket."),
               S("Name", text="The main connective is ~: the formula is a negation.")],
            "Main connective", "Recall", "Which sign governs the whole formula?",
            "The sign ~ is the main connective when it negates the whole formula."),
        _mc("What is the main connective of ~p . q?", "The dot", [
            ("~", "~ acts only on p here."),
            ("There is none.", "The dot joins ~p and q."),
            ("p", "p is a variable, not a connective."),
        ], 1, [S("Scope", text="~ applies only to the letter that follows it: ~p."),
               S("Main connective", text="The dot joins ~p and q.")],
            "Main connective", "Application", "Where does the negation sign stop?",
            "The formula is a conjunction."),
        _mc("“Neither Ama nor Bih passed.” With a for “Ama passed” and b for “Bih passed”, a correct symbolic form is:", "~(a v b)", [
            ("~a v ~b", "This says that at least one of them failed. It would be true if only Bih passed."),
            ("~(a . b)", "“Not both” allows one of them to pass."),
            ("a v b", "This says that at least one passed: the opposite."),
        ], 3, [S("Meaning", text="“Neither ... nor” means that it is false that either passed."),
               S("Write", text="~(a v b), which is also ~a . ~b.")],
            "Translating neither ... nor", "Application", "Which sentence says that none of them passed?",
            "Neither p nor q is ~(p v q)."),
        NUM("p is false, q is true and r is true. How many of these three formulas are true: (p . q) v r, p . (q v r), ~(p . q)?", 2,
            steps=[S("(p . q) v r", text="p . q = F, r = T, so T."),
                   S("p . (q v r)", text="p is false, so F."),
                   S("~(p . q)", text="p . q = F, so ~(p . q) = T."),
                   S("Count", text="Two are true.")],
            concept="Evaluating grouped formulas", skill="Calculation", hint="Work from the inside of the brackets.",
            feedback="Work from the innermost brackets outwards."),
        _mc("“If it rains and the road floods, then traffic stops.” With r, f and t, the correct form is:", "(r . f) ⊃ t", [
            ("r . (f ⊃ t)", "This says that it rains and that if the road floods, traffic stops: the main break is in the wrong place."),
            ("r ⊃ (f . t)", "This says that if it rains, both the road floods and traffic stops."),
            ("(r ⊃ f) . t", "This says that traffic stops and that rain gives floods."),
        ], 0, [S("Find the main break", text="“If ... then”: the antecedent is “it rains and the road floods”."),
               S("Write", text="(r . f) ⊃ t.")],
            "Translating with grouping", "Application", "What is the antecedent of the sentence?",
            "The main connective is ⊃."),
        _mc("What is the main connective of [(p ⊃ q) . (q ⊃ r)] ⊃ (p ⊃ r)?", "The ⊃ outside all brackets (the third one)", [
            ("The dot.", "The dot is inside the square brackets."),
            ("The first ⊃ (between p and q).", "It is inside the round and square brackets."),
            ("There is none.", "The ⊃ outside the brackets is the main connective."),
        ], 1, [S("Look outside the brackets", text="The square bracket and the round bracket (p ⊃ r) are joined by a ⊃."),
               S("Name", text="An implication whose antecedent is a conjunction.")],
            "Main connective", "Analysis", "Cover everything inside brackets. What is left?",
            "Only the connective outside all brackets is the main connective."),
        _mc("p is true and q is false. Which of these is true?", "~(p . q)", [
            ("~p . ~q", "~p is false, so the conjunction is false."),
            ("p . q", "q is false."),
            ("~p . q", "Both ~p and q are false."),
        ], 3, [S("Values", text="p . q = F. ~p = F, ~q = T."),
               S("Evaluate", text="~(p . q) = T; ~p . ~q = F; p . q = F; ~p . q = F.")],
            "Scope of negation", "Calculation", "Evaluate the inside of the bracket first.",
            "~(p . q) is not the same as ~p . ~q."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Structure of truth tables and their uses",
    title="Building truth tables", lesson="sym-building-truth-tables",
    questions=[
        NUM("How many rows does the truth table of a formula with three different variables have?", 8,
            steps=[S("Rule", text="n variables give 2 to the power n rows."), S("Calculate", text="2 x 2 x 2 = 8.")],
            concept="Number of rows", skill="Calculation", hint="Each variable doubles the number of rows.",
            feedback="Three variables give 2^3 = 8 rows."),
        _mc("How many rows does the truth table of (p ⊃ q) . (q ⊃ p) have?", "4", [
            ("2", "There are two variables, so more than 2 rows are needed."),
            ("8", "There are only two different variables, p and q."),
            ("16", "16 rows are for four variables."),
        ], 0, [S("Count variables, not letters", text="Only p and q appear."),
               S("Rows", text="2^2 = 4.")],
            "Number of rows", "Application", "Count the different variables.",
            "p and q each appear twice but count once."),
        _mc("In the standard order for three variables p, q, r, the column of r (the last variable) reads, from the first row:", "T, F, T, F, T, F, T, F", [
            ("T, T, T, T, F, F, F, F", "This is the pattern of p, the first variable."),
            ("T, T, F, F, T, T, F, F", "This is the pattern of q, the middle variable."),
            ("T, F, F, T, T, F, F, T", "No standard order uses this pattern."),
        ], 1, [S("Rule", text="The last variable alternates on every row."),
               S("Write", text="T, F, T, F, T, F, T, F.")],
            "Standard order of rows", "Recall", "Which variable changes fastest?",
            "The last variable changes on every row."),
        _mc("In a truth table with three variables, the column of the first variable p reads:", "four T’s followed by four F’s.", [
            ("T, F, T, F, T, F, T, F.", "This is the pattern of the last variable."),
            ("T, T, F, F, T, T, F, F.", "This is the pattern of the middle variable."),
            ("all T’s.", "Each variable is true in half the rows and false in half."),
        ], 0, [S("Rule", text="The first variable is T for the first half of the rows, F for the second half."),
               S("Apply", text="Eight rows: TTTT FFFF.")],
            "Standard order of rows", "Recall", "Which variable changes slowest?",
            "p is T in the first half of the rows."),
        _mc("To build the table of ~(p . q) ⊃ p, the columns after p and q should be, in order:", "p . q, then ~(p . q), then ~(p . q) ⊃ p", [
            ("~(p . q) ⊃ p, then p . q, then ~(p . q)", "Work from the inside outwards, not the other way."),
            ("~p, then ~q, then ~(p . q) ⊃ p", "~p and ~q are not sub-formulas of ~(p . q) ⊃ p: ~(p . q) is the negation of the whole conjunction."),
            ("p . q, then p ⊃ q", "p ⊃ q is not a part of the formula."),
        ], 2, [S("Sub-formulas, innermost first", text="p . q is inside the brackets. Then its negation. Then the whole implication.")],
            "Building a table", "Application", "Which part is inside the brackets?",
            "Work from the innermost brackets outwards."),
        NUM("In the truth table of (p v q) . ~r, in how many of the eight rows is the formula true?", 3,
            steps=[S("p v q", text="T, T, T, T, T, T, F, F (rows 1 to 8)."),
                   S("~r", text="F, T, F, T, F, T, F, T."),
                   S("Conjunction", text="True only when both are true: rows 2, 4 and 6."),
                   S("Count", text="3 rows.")],
            concept="Building a table", skill="Calculation", hint="Compute p v q and ~r separately and then join them with the dot.",
            feedback="The formula is true in rows 2, 4 and 6."),
        _mc("What is the final column of p ⊃ ~q, in the order TT, TF, FT, FF?", "F, T, T, T", [
            ("T, F, T, T", "This is the column of p ⊃ q: ~q has been forgotten."),
            ("T, T, T, F", "This is the column of p v q."),
            ("F, F, F, T", "This is the column of ~(p v q)."),
        ], 3, [S("~q", text="F, T, F, T."),
               S("p ⊃ ~q", text="Row 1: T ⊃ F = F. Row 2: T ⊃ T = T. Row 3: F ⊃ F = T. Row 4: F ⊃ T = T.")],
            "Building a table", "Calculation", "Write the column of ~q first.",
            "The implication is false only when p is T and ~q is F."),
        _mc("A student writes 7 rows for the truth table of a formula with the variables p, q and r. What is wrong?", "One row is missing: 8 rows are needed.", [
            ("Nothing: 7 rows are enough.", "Three variables need 2^3 = 8 rows."),
            ("Two rows are repeated.", "The error is not repetition; the number of rows is too small."),
            ("Too many rows: 4 are enough.", "4 rows are for two variables."),
        ], 1, [S("Count", text="2^3 = 8 rows."), S("Conclude", text="With 7 rows, one combination of truth values has been left out.")],
            "Number of rows", "Reasoning", "How many rows should the table have?",
            "Check the number of rows against 2^n."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Structure of truth tables and their uses",
    title="Using truth tables to test equivalence and validity", lesson="sym-uses-of-truth-tables",
    questions=[
        _mc("Two statements are logically equivalent when:", "their final columns are identical in every row.", [
            ("they are both true in at least one row.", "Statements can agree in some rows and differ in others."),
            ("they use the same variables.", "p ⊃ q and q ⊃ p use the same variables but are not equivalent."),
            ("they are both true in the first row.", "One row is not enough: every row must agree."),
        ], 3, [S("Recall", text="Equivalent means the same truth value in every row.")],
            "Logical equivalence", "Recall", "Compare the final columns.",
            "Identical final columns mean equivalence."),
        _mc("Which statement is equivalent to p ⊃ q?", "~p v q", [
            ("q ⊃ p", "This is the converse. Its column differs from p ⊃ q in rows 2 and 3."),
            ("p . ~q", "This is the negation of p ⊃ q: it is true exactly when p ⊃ q is false."),
            ("p ≡ q", "This is false in row 3 while p ⊃ q is true."),
        ], 0, [S("Columns", text="p ⊃ q: T, F, T, T. ~p v q: T, F, T, T."),
               S("Compare", text="Identical.")],
            "Logical equivalence", "Application", "Compute the final column of each option.",
            "~p v q has the same column as p ⊃ q."),
        _mc("In testing an argument form with a truth table, a counterexample row is a row in which:", "all premises are true and the conclusion is false.", [
            ("all premises are false.", "A false premise cannot show invalidity."),
            ("the conclusion is true.", "A true conclusion is no problem for validity."),
            ("the premises and the conclusion are all true.", "True premises with a true conclusion are consistent with validity."),
        ], 1, [S("Recall", text="Validity: true premises can never lead to a false conclusion."),
               S("Counterexample", text="A row where this does happen.")],
            "Validity test", "Recall", "What would show that the premises do not guarantee the conclusion?",
            "One counterexample row is enough to show invalidity."),
        _mc("Which of these argument forms is valid?", "p ⊃ q, ~q ∴ ~p", [
            ("p ⊃ q, q ∴ p", "Row p false, q true: premises true, conclusion false."),
            ("p ⊃ q, ~p ∴ ~q", "Row p false, q true: both premises true, conclusion ~q false."),
            ("p v q, p ∴ ~q", "Row p true, q true: both premises true, conclusion ~q false."),
        ], 3, [S("Test p ⊃ q, ~q ∴ ~p", text="Both premises are true only when p and q are both false (row 4). There the conclusion ~p is true."),
               S("Test the others", text="Each of the other forms has a counterexample row.")],
            "Validity test", "Analysis", "Look for a row with true premises and a false conclusion.",
            "A form is valid when no counterexample row exists."),
        _mc("In the form p ⊃ q, q ∴ p, which row is a counterexample row?", "p false, q true", [
            ("p true, q false", "In this row the premise p ⊃ q is false."),
            ("p true, q true", "The conclusion p is true here."),
            ("p false, q false", "In this row the premise q is false."),
        ], 1, [S("Rows with both premises true", text="q is true in rows TT and FT, and p ⊃ q is true in both of them: these are the rows with both premises true."),
               S("Check the conclusion p", text="In FT it is false: a counterexample.")],
            "Validity test", "Application", "In which rows are both premises true?",
            "The form is invalid."),
        NUM("In the argument form p v q, ~p ∴ q, how many of the four rows have both premises true?", 1,
            steps=[S("Premises", text="p v q: T, T, T, F. ~p: F, F, T, T."),
                   S("Both true", text="Only row 3 (p false, q true)."),
                   S("Conclusion", text="q is true there, so the form is valid.")],
            concept="Validity test", skill="Calculation", hint="Write the columns of p v q and ~p.",
            feedback="Only the row p false, q true has both premises true. There q is true, so the form is valid."),
        _mc("The argument form p v q, p ∴ ~q is:", "invalid: when p and q are both true the premises are true and ~q is false.", [
            ("valid: if p is true then q is false.", "v is inclusive: p true does not make q false."),
            ("valid: v means that only one of the two is true.", "v is the inclusive “or”."),
            ("invalid: because the first premise is false.", "The premise p v q is true when p is true."),
        ], 0, [S("Row TT", text="p v q = T, p = T, ~q = F."),
               S("Counterexample", text="So the form is invalid.")],
            "Validity test", "Reasoning", "Check the row where p and q are both true.",
            "The mistake is to read v as exclusive."),
        _mc("A student finds one row in which all premises and the conclusion are true and says “the form is valid”. She is:", "wrong: she must check every row in which all premises are true.", [
            ("right: one row is enough to prove validity.", "One row is enough only to show invalidity (a counterexample row)."),
            ("right: true premises and a true conclusion are all we need.", "Other rows may still have true premises and a false conclusion."),
            ("wrong: validity cannot be tested by tables.", "A truth table is a standard test of validity for these forms."),
        ], 2, [S("Method", text="List all rows with all premises true and check the conclusion in each.")],
            "Validity test", "Reasoning", "What would a counterexample look like?",
            "Validity needs every such row to have a true conclusion."),
    ]))


SETS.append(practice_set(
    module=_M, topic="Truth tables and logical constants",
    title="Tautologies, contradictions and equivalences", lesson="sym-tautologies-contradictions-and-contingent-statements",
    questions=[
        _mc("A tautology is a compound statement whose final column is:", "T in every row.", [
            ("F in every row.", "That is a contradiction."),
            ("T in some rows and F in others.", "That is a contingent statement."),
            ("T in the first row only.", "A tautology must be true in every row."),
        ], 0, [S("Recall", text="Tautology: always true by form.")],
            "Tautology", "Recall", "Think of p v ~p.", "All T means tautology."),
        _mc("p . ~p is:", "a contradiction.", [
            ("a tautology.", "A statement cannot be true and false at once, so it is never true."),
            ("a contingent statement.", "Its column has no T."),
            ("equivalent to p v ~p.", "p v ~p is always true and p . ~p is always false."),
        ], 2, [S("Table", text="p = T: T . F = F. p = F: F . T = F."), S("Final column", text="F, F: a contradiction.")],
            "Contradiction", "Application", "Evaluate it for p true and p false.", "All F means contradiction."),
        _mc("The truth table of p ⊃ q has the final column T, F, T, T. The statement is:", "contingent.", [
            ("a tautology.", "A tautology has T in every row."),
            ("a contradiction.", "A contradiction has F in every row."),
            ("invalid.", "Validity is a property of arguments, not single statements."),
        ], 2, [S("Look at the column", text="It contains T and F.")],
            "Contingent statement", "Concept", "Does the column contain both values?", "T and F together: contingent."),
        _mc("Which of these is a tautology?", "(p . q) ⊃ p", [
            ("p ⊃ q", "Its column is T, F, T, T: contingent."),
            ("p . q", "Its column is T, F, F, F: contingent."),
            ("p ≡ ~p", "A statement and its negation always differ: this is a contradiction."),
        ], 3, [S("Evaluate", text="(p . q) ⊃ p: if the antecedent is true then p is true, so the implication is never false. Column: T, T, T, T.")],
            "Tautology", "Analysis", "Can the antecedent be true when p is false?", "Check the final column."),
        NUM("In how many of its four rows is the statement ~(p . q) ≡ (~p v ~q) true?", 4,
            steps=[S("Columns", text="~(p . q): F, T, T, T. ~p v ~q: F, T, T, T."),
                   S("Biconditional", text="The columns agree in every row, so the biconditional is true in all 4 rows.")],
            concept="De Morgan's equivalences", skill="Calculation", hint="Compare the two columns row by row.",
            feedback="It is a tautology: this is De Morgan’s first law."),
        _mc("Which statement is equivalent to ~(p v q)?", "~p . ~q", [
            ("~p v ~q", "This is equivalent to ~(p . q), not to ~(p v q)."),
            ("p . q", "This is true only when both are true, while ~(p v q) is true only when both are false."),
            ("~p ⊃ q", "This is equivalent to p v q."),
        ], 3, [S("De Morgan", text="~(p v q) means neither p nor q: both are false: ~p . ~q.")],
            "De Morgan's equivalences", "Concept", "Neither ... nor.", "Law 2 of De Morgan."),
        _mc("“If a student studies, she passes.” Which statement is equivalent to it?", "If she does not pass, she did not study.", [
            ("If she passes, she studied.", "This is the converse: it is not equivalent."),
            ("If she does not study, she does not pass.", "This is the inverse: it is not equivalent."),
            ("She studies and passes.", "This is a conjunction, which says more."),
        ], 1, [S("Symbols", text="s ⊃ p."), S("Contrapositive", text="~p ⊃ ~s: if she does not pass, she did not study.")],
            "Contrapositive", "Application", "Reverse the order and negate both parts.",
            "p ⊃ q is equivalent to ~q ⊃ ~p."),
        _mc("Which of these is equivalent to p ⊃ q?", "~q ⊃ ~p", [
            ("q ⊃ p", "The converse: not equivalent."),
            ("~p ⊃ ~q", "The inverse: not equivalent (it has the same column as the converse)."),
            ("p . q", "A conjunction is true in fewer cases than p ⊃ q."),
        ], 2, [S("Columns", text="p ⊃ q: T, F, T, T. ~q ⊃ ~p: T, F, T, T. q ⊃ p: T, T, F, T. ~p ⊃ ~q: T, T, F, T. p . q: T, F, F, F.")],
            "Contrapositive", "Reasoning", "Compare final columns.", "Only the contrapositive matches."),
    ]))
