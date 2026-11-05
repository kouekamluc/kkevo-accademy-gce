"""Form 5 Logic: Informal Fallacies, practice sets (one per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

MODULE = "Informal Fallacies"
T1 = "Definition, classification and significance of fallacies"
T2 = "Fallacies of relevance: fallacies of no evidence"
T3 = "Fallacies of relevance: fallacies of little evidence"
T4 = "Fallacies of ambiguity"


def Q(prompt, right, wrongs, pos, why_right, concept, skill, hint):
    """4-option MC. `wrongs` is three (text, why) pairs; the correct option goes at index `pos`."""
    opts = [C(t, why=w) for t, w in wrongs]
    opts.insert(pos, C(right, correct=True))
    return MC(prompt, opts, steps=[S("Reasoning", text=why_right)], concept=concept, skill=skill, hint=hint,
              feedback=why_right)


SETS = []

# ------------------------------------------------------------------ 1
SETS.append(practice_set(
    module=MODULE, topic=T1, title="Fallacies: meaning and classification", lesson="fal-what-are-fallacies",
    questions=[
        Q("A fallacy is best defined as", "a mistake in reasoning that seems to support a conclusion better than it does",
          [("an argument with a false conclusion", "A fallacy can have a true conclusion; the fault is in the support."),
           ("a lie told on purpose", "Fallacies are often committed honestly."),
           ("any argument that someone dislikes", "Disliking an argument does not make it fallacious.")],
          0, "A fallacy is a faulty argument that looks stronger than it is. The truth of the conclusion is not the test.",
          "Definition of fallacy", "Recall", "Think of the argument, not of the conclusion."),
        Q("A formal fallacy is a mistake in", "the pattern (form) of the argument",
          [("the meaning of one word only", "That would be an informal fallacy."),
           ("the speaker's character", "Character is not the issue; the argument is."),
           ("the number of premises", "A valid argument can have any number of premises.")],
          2, "A formal fallacy is detected from the pattern alone, without knowing what the words mean.",
          "Formal fallacy", "Recall", "Which kind of fallacy can be found without reading the words?"),
        Q("'If the match is cancelled, the pitch is empty. The pitch is empty. So the match is cancelled.' This pattern is", "a formal fallacy (affirming the consequent)",
          [("an informal fallacy of ambiguity", "No word changes meaning; the pattern is the fault."),
           ("a valid argument", "The pitch could be empty for other reasons."),
           ("an appeal to force", "No threat is made.")],
          3, "The pattern p ⊃ q, q, therefore p is invalid whatever p and q say.",
          "Formal fallacy", "Application", "Write the argument as p ⊃ q and look at which part is affirmed."),
        Q("Which is an informal fallacy?", "Using a word with two meanings to reach a conclusion",
          [("Writing a conclusion before the premises", "The order of writing is not a fallacy."),
           ("Using three premises", "The number of premises is irrelevant."),
           ("Having a true conclusion", "A true conclusion is not a fault.")],
          1, "Shifting meaning is a fault in content, so it is informal.",
          "Informal fallacy", "Concept", "Informal fallacies concern content, not pattern."),
        Q("Which is NOT a main reason why fallacies persuade?", "They always have false premises",
          [("They appeal to feelings", "Feelings are a main reason."),
           ("They resemble good arguments", "Resemblance is a main reason."),
           ("They use words with more than one meaning", "Ambiguity is a main reason.")],
          0, "Fallacies can have true premises. The fault is lack of support, not falsity.",
          "Why fallacies persuade", "Concept", "One option says something false about fallacies."),
        Q("This course groups informal fallacies as", "no evidence, little evidence and ambiguity",
          [("Aristotelian, Boolean and modern", "These names belong to views of propositions."),
           ("formal, symbolic and verbal", "These are not the Board's groups."),
           ("true, false and doubtful", "These describe statements, not groups of fallacies.")],
          1, "These are the Board's labels. Textbooks group the fallacies differently: check your textbook.",
          "Classification", "Recall", "Recall the three boxes under 'Informal fallacies' in Figure 1."),
        Q("A student hears 'Everyone is buying this phone, so it is the best.' What is the best polite reply?", "'The number of buyers does not show that it is best. What evidence shows its quality?'",
          [("'You are stupid to believe that.'", "That attacks the person, not the reasoning."),
           ("'You are lying.'", "A fallacy does not prove dishonesty."),
           ("'Then I will not talk to you.'", "That ends the discussion without a reason.")],
          2, "A polite challenge names the gap and asks for evidence.",
          "Challenging fallacies politely", "Application", "Which reply deals with the reasoning rather than the person?"),
        NUM("A student lists five arguments: (1) affirming the consequent, (2) equivocation, (3) hasty generalization, (4) an invalid syllogism with an undistributed middle term, "
            "(5) a straw man. How many of the five are INFORMAL fallacies?", 3,
            steps=[S("Sort", text="Formal (fault in pattern): the first and the fourth. Informal: equivocation, hasty generalization, straw man."),
                   S("Count", text="3 informal.")],
            concept="Formal and informal", skill="Reasoning", hint="Which faults can be found from the pattern alone?"),
    ]))

# ------------------------------------------------------------------ 2
SETS.append(practice_set(
    module=MODULE, topic=T2, title="Appeals: force, pity, the people and the person", lesson="fal-no-evidence-appeals",
    questions=[
        Q("'Agree that my team is the best, or I will not share my lunch with you.' This is", "appeal to force",
          [("appeal to pity", "No sympathy is sought."), ("appeal to the people", "No crowd is mentioned."), ("tu quoque", "Nobody's own behaviour is attacked.")],
          0, "A threat replaces evidence: appeal to force.", "Appeal to force", "Application", "What is offered in place of a reason?"),
        Q("'Please pass my answer, sir. My mother is ill and I have not slept.' The fallacy is", "appeal to pity",
          [("appeal to force", "There is no threat."), ("appeal to the people", "No number of people is cited."), ("straw man", "No position is distorted.")],
          1, "Sympathy is used in place of evidence that the answer is correct.", "Appeal to pity", "Application", "What feeling does the speaker try to raise?"),
        Q("'Most people in this street use this brand of rice, so it must be the best.' This is", "appeal to the people",
          [("argument against the person", "No person is attacked."), ("appeal to force", "No threat."), ("appeal to pity", "No sorrow story.")],
          2, "Popularity is the only reason given.", "Appeal to the people", "Application", "What is the only reason offered?"),
        Q("'You say I should save more, but you spent a lot on your last party.' This is", "argument against the person (tu quoque)",
          [("appeal to force", "No threat."), ("appeal to ignorance", "No lack of proof is used."), ("begging the question", "The conclusion is not assumed.")],
          3, "The reply points to the speaker's own behaviour and ignores whether saving is a good idea.", "Tu quoque", "Application", "Whose behaviour does the reply attack?"),
        Q("'Of course the shopkeeper says this stove is good. He sells stoves.' This is", "circumstantial argument against the person",
          [("abusive argument against the person", "No insult is used."), ("tu quoque", "No inconsistency in conduct is claimed."), ("appeal to pity", "No sympathy.")],
          1, "The reply points to the speaker's situation (the interest in selling).", "Circumstantial ad hominem", "Application", "What does the reply point to?"),
        Q("In which case is pity NOT a fallacy?", "Deciding to give a student with a broken arm extra writing time",
          [("Claiming that a badly argued essay is correct because the writer is poor", "Sympathy is used as evidence of correctness."),
           ("Claiming that a claim is true because the speaker is sad", "Sadness is not evidence."),
           ("Claiming that a driver was not at fault because he is old", "Age is not evidence about fault.")],
          2, "Pity is relevant to a decision about kindness, not to the truth of a claim.", "When pity is relevant", "Reasoning", "Ask what the pity is used to show."),
        Q("A witness in a court case is shown to have been paid by one side. Questioning her evidence is", "reasonable if the payment affects how far her evidence can be trusted",
          [("always a fallacy of argument against the person", "Interest can matter for reliability."),
           ("an appeal to force", "No threat."), ("never allowed", "Courts weigh reliability.")],
          0, "The speaker's interest is relevant to reliability. It is a fallacy only when used to say the claim is false without examining it.", "Limits of ad hominem", "Reasoning", "Does the attack bear on how far to trust the evidence?"),
        Q("What do all four fallacies of this lesson have in common?", "The reason offered is not logically relevant to the truth of the claim",
          [("They all have false conclusions", "A conclusion may be true."), ("They all use ambiguous words", "That is a different group."),
           ("They all have two premises", "Number of premises is irrelevant.")],
          3, "Threat, sympathy, popularity or an attack on the speaker do not show the claim is true.", "Fallacies of no evidence", "Concept", "What do force, pity, crowds and attacks fail to show?"),
    ]))

# ------------------------------------------------------------------ 3
SETS.append(practice_set(
    module=MODULE, topic=T2, title="Straw man, red herring, begging the question, complex question",
    lesson="fal-no-evidence-diversions-and-begging-the-question",
    questions=[
        Q("Ama: 'Exams should have fewer questions.' Kofi: 'Ama wants no exams at all.' This is", "straw man",
          [("red herring", "Kofi does not change the subject; he distorts Ama's claim."), ("begging the question", "No circle."), ("appeal to pity", "No sympathy.")],
          0, "Kofi attacks a stronger, distorted version of Ama's position.", "Straw man", "Application", "Is Ama's claim reported fairly?"),
        Q("Asked why the bus fare rose, the driver says: 'Look at how clean my bus is.' This is", "red herring",
          [("straw man", "Nothing is distorted."), ("complex question", "The driver asks no question."), ("equivocation", "No word shifts.")],
          1, "The driver changes the subject from the fare to cleanliness.", "Red herring", "Application", "Does the reply deal with the fare?"),
        Q("'The law is just, because it is a fair rule.' This is", "begging the question",
          [("complex question", "No question."), ("red herring", "The subject stays the same."), ("straw man", "Nobody's position is distorted.")],
          2, "'Just' and 'fair' mean nearly the same, so the premise repeats the conclusion.", "Begging the question", "Application", "Does the premise add anything to the conclusion?"),
        Q("'Have you stopped copying homework?' is", "a complex question",
          [("a red herring", "The subject is not changed."), ("begging the question", "It is a question, not an argument."), ("a straw man", "No position is distorted.")],
          3, "It assumes that you copied before.", "Complex question", "Application", "What does the question assume?"),
        Q("The difference between straw man and red herring is that a straw man", "attacks a distorted version of the claim, while a red herring changes the subject",
          [("changes the subject, while a red herring distorts the claim", "The two are reversed."),
           ("is always an insult", "Not necessarily."), ("is a formal fallacy", "Both are informal.")],
          0, "Straw man distorts; red herring diverts.", "Straw man vs red herring", "Concept", "One distorts, the other drops the claim."),
        Q("The best way to answer 'Why did you cheat on the test?' when you did not cheat is to", "reject the assumption first, then answer",
          [("answer 'because I was tired'", "That accepts the hidden assumption."), ("answer 'yes'", "That admits cheating."), ("stay silent and walk away", "That leaves the assumption in place.")],
          1, "A complex question needs its hidden assumption rejected before any direct answer.", "Answering complex questions", "Reasoning", "Do not accept what the question assumes."),
        Q("To test whether an argument begs the question, ask whether", "a person who doubts the conclusion could accept the premise",
          [("the conclusion is long", "Length does not matter."), ("the premises are many", "Number does not matter."), ("the speaker is polite", "Politeness does not matter.")],
          2, "If a doubter could not accept the premise, it already assumes the conclusion.", "Test for circularity", "Reasoning", "Think of someone who doubts the conclusion."),
        Q("'The minister is honest because he never tells lies.' Evaluate.", "It begs the question: 'never tells lies' is what 'honest' means",
          [("It is a straw man", "No position is distorted."), ("It is a red herring", "The subject is unchanged."), ("It is sound, because both parts are true", "The premise only repeats the conclusion.")],
          3, "The premise restates the conclusion; it gives no independent evidence.", "Begging the question", "Reasoning", "Compare the meaning of 'honest' with 'never tells lies'."),
    ]))

# ------------------------------------------------------------------ 4
SETS.append(practice_set(
    module=MODULE, topic=T3, title="Generalization, false cause and slippery slope",
    lesson="fal-little-evidence-generalisations-and-causes",
    questions=[
        Q("'I met two rude shop assistants today, so all shop assistants are rude.' This is", "hasty generalization",
          [("slippery slope", "No chain of results."), ("appeal to pity", "No sympathy."), ("begging the question", "No circle.")],
          0, "Two cases are too few for a claim about all shop assistants.", "Hasty generalization", "Application", "How big is the sample?"),
        Q("A hasty generalization uses a sample that is", "too small or unrepresentative",
          [("always large", "Large samples can be fine."), ("always taken from experts", "Not required."), ("never checked", "The point is size and fairness.")],
          1, "A weak sample is too small or not fair.", "Samples", "Recall", "Recall the two ways a sample can fail."),
        Q("'After the new principal came, the river flooded. So the principal caused the flood.' This is", "false cause (post hoc)",
          [("hasty generalization", "No generalization is made."), ("appeal to ignorance", "No lack of proof is used."), ("weak analogy", "No comparison.")],
          2, "Order in time is treated as cause.", "Post hoc", "Application", "What is the only link given?"),
        Q("'Allow students to use calculators in class today, and soon they will not learn arithmetic at all, and then the country will have no engineers.' This is", "slippery slope",
          [("straw man", "No distortion."), ("false cause", "No past event is called a cause."), ("appeal to force", "No threat.")],
          3, "A chain of disasters is predicted without evidence for each link.", "Slippery slope", "Application", "Is there evidence for each step?"),
        Q("Ice cream sales and drowning both rise in hot months. The claim 'ice cream causes drowning' ignores", "a common cause (the hot weather)",
          [("the speaker's character", "Not the issue."), ("the meaning of 'ice cream'", "No ambiguity."), ("the number of premises", "Not the issue.")],
          0, "A third factor causes both, so the link is false.", "Common cause", "Reasoning", "Is there something that explains both?"),
        Q("Which survey is the best basis for a claim about all students in a school?", "Students chosen at random from every class",
          [("The first three students at the gate", "Small and unfair."), ("Only the school choir", "Not representative."), ("Only friends of the speaker", "Not representative.")],
          1, "A random, wide sample is the fairest.", "Good samples", "Application", "Which sample is both large and fair?"),
        Q("A warning that 'if we skip the weeding, the maize will be poor' is not a slippery slope because", "the link is well known and supported by evidence",
          [("it is a short sentence", "Length does not matter."), ("it has two words", "Not relevant."), ("it is said in anger", "Mood does not matter.")],
          2, "A reasonable warning has evidence for the link.", "Reasonable warnings", "Reasoning", "What would make the chain acceptable?"),
        Q("'A man in a red shirt fell, so red shirts make people fall.' The best repair is to", "compare many cases for a causal link while other things are equal",
          [("shout louder", "Volume gives no evidence."), ("change the shirt colour", "That does not test the link."), ("agree with the speaker", "That accepts the fallacy.")],
          3, "A causal claim needs repeated, controlled cases.", "Testing causes", "Reasoning", "What kind of evidence supports a cause?"),
    ]))

# ------------------------------------------------------------------ 5
SETS.append(practice_set(
    module=MODULE, topic=T3, title="Analogy, authority, ignorance and false dichotomy",
    lesson="fal-little-evidence-analogies-authority-and-ignorance",
    questions=[
        Q("'Either you give me the job or you want my family to starve.' This is", "false dichotomy",
          [("appeal to ignorance", "No lack of proof."), ("weak analogy", "No comparison."), ("composition", "No whole and part.")],
          0, "It offers only two options when there are others.", "False dichotomy", "Application", "How many options are given?"),
        Q("'A famous athlete says this tablet cures all disease, so it does.' This is", "appeal to unqualified authority",
          [("appeal to force", "No threat."), ("hasty generalization", "No sample."), ("straw man", "No distortion.")],
          1, "Athletics is not expertise in medicine.", "Unqualified authority", "Application", "Is the speaker an expert in this field?"),
        Q("'No one has proved there are no fish in this pond, so there are fish.' This is", "appeal to ignorance",
          [("false cause", "No cause."), ("slippery slope", "No chain."), ("begging the question", "No circle.")],
          2, "Lack of proof is treated as proof.", "Appeal to ignorance", "Application", "What is treated as evidence?"),
        Q("'A school is like a shop, and a shop must make a profit, so a school must make a profit.' The weakness is that", "a school and a shop differ in their main purpose",
          [("both have staff", "Similarity is not the weakness."), ("both have buildings", "Similarity is not the weakness."), ("the sentence is long", "Length is irrelevant.")],
          3, "A weak analogy ignores relevant differences.", "Weak analogy", "Reasoning", "Where do the two things differ?"),
        Q("When is relying on an expert reasonable?", "When the expert is qualified in the exact field and other experts agree",
          [("When the expert is famous", "Fame is not expertise."), ("When the expert is older", "Age is not expertise."), ("When many people trust the expert", "That is the appeal to the people.")],
          0, "Expertise in the field, agreement of others, and no bias.", "Reasonable authority", "Concept", "Think of qualification and agreement."),
        Q("A careful test finds no trace of a poison in a water sample. This evidence is", "reasonable evidence against the presence of the poison",
          [("a fallacy of ignorance in every case", "A proper search is evidence."), ("an appeal to force", "No threat."), ("an appeal to pity", "No sympathy.")],
          1, "After a proper search, failing to find something is evidence. The fallacy is when no search has been made.", "Limits of ignorance", "Reasoning", "Was a proper search made?"),
        Q("'Either we ban all phones in school or students will learn nothing.' A third option is", "a rule on when phones may be used",
          [("a second ban", "That is the same option."), ("a ban on books", "Not a real alternative."), ("agree with both", "That does not add an option.")],
          2, "Finding a third option breaks the false dichotomy.", "False dichotomy", "Application", "Is there a middle way?"),
        Q("Which is the best test for an analogy?", "Are the two things alike in ways that matter for the conclusion?",
          [("Are they the same colour?", "Irrelevant."), ("Is the speaker famous?", "Irrelevant."), ("Is the analogy short?", "Irrelevant.")],
          3, "An analogy is strong when the relevant similarities outweigh the differences.", "Testing analogy", "Concept", "What should the similarities concern?"),
    ]))

# ------------------------------------------------------------------ 6
SETS.append(practice_set(
    module=MODULE, topic=T4, title="Equivocation and amphiboly", lesson="fal-ambiguity-equivocation-and-amphiboly",
    questions=[
        Q("Equivocation is the fallacy of", "using a key word in two meanings in the same argument",
          [("using a badly built sentence", "That is amphiboly."), ("attacking a person", "That is argument against the person."), ("emphasising a word", "That is accent.")],
          0, "A shift in the meaning of a word.", "Equivocation", "Recall", "It is about one word."),
        Q("'A bank keeps money safe. The river has a bank. So the river keeps money safe.' The word that shifts is", "'bank'",
          [("'money'", "Keeps its meaning."), ("'river'", "Keeps its meaning."), ("'safe'", "Keeps its meaning.")],
          1, "'Bank' is an institution in one place and a river edge in the other.", "Equivocation", "Application", "Which word has two ordinary meanings?"),
        Q("'I saw the girl with the binoculars.' This is ambiguous because", "the grammar allows two readings",
          [("a word has two meanings", "Each word has one."), ("it begs the question", "No circle."), ("it is vague", "It is not vague.")],
          2, "'With the binoculars' can attach to the seer or to the girl: amphiboly.", "Amphiboly", "Concept", "Is it the words or their arrangement?"),
        Q("The difference between equivocation and amphiboly is that equivocation depends on", "a word, while amphiboly depends on sentence structure",
          [("sentence structure, while amphiboly depends on a word", "The two are reversed."), ("emphasis, while amphiboly depends on tone", "Emphasis is accent."), ("feelings, while amphiboly depends on facts", "Not the difference.")],
          3, "Equivocation: one word. Amphiboly: structure.", "Equivocation vs amphiboly", "Concept", "One concerns a word, the other the grammar."),
        Q("'Nothing is better than good health. Rice is better than nothing. So rice is better than good health.' This is", "equivocation on 'nothing'",
          [("amphiboly", "The structure is clear."), ("accent", "No emphasis shift."), ("composition", "No whole and part.")],
          0, "'Nothing' means 'no thing' first and 'having nothing' second.", "Equivocation", "Application", "Which word links the premises?"),
        Q("Which is NOT a fallacy of ambiguity?", "A hasty generalization from two cases",
          [("Equivocation", "It is one."), ("Amphiboly", "It is one."), ("Accent", "It is one.")],
          1, "Hasty generalization is a fallacy of little evidence.", "Classification", "Concept", "Which belongs to another group?"),
        Q("'Teachers and pupils with passes may enter.' The best repair to remove ambiguity is", "'Teachers, and pupils who have passes, may enter.' or 'Teachers and pupils may enter if they have passes.'",
          [("'Teachers and pupils with passes may enter!'", "Punctuation does not fix it."), ("'Passes may enter teachers and pupils.'", "That is worse."), ("Leave it unchanged", "It stays ambiguous.")],
          2, "Rewrite so that the scope of 'with passes' is clear.", "Removing ambiguity", "Application", "Make clear whom 'with passes' describes."),
        Q("A speaker says 'A pen is a place for animals. My pen is in my bag. So my bag is a place for animals.' The best reply is", "'Pen' changes meaning between the premises",
          [("'You are lying.'", "That attacks the person."), ("'Many people disagree.'", "That is an appeal to the people."), ("'You have too few cases.'", "That is hasty generalization.")],
          3, "Naming the shifting word exposes the equivocation.", "Equivocation", "Reasoning", "What changes between the sentences?"),
    ]))

# ------------------------------------------------------------------ 7
SETS.append(practice_set(
    module=MODULE, topic=T4, title="Accent, composition and division", lesson="fal-ambiguity-accent-composition-and-division",
    questions=[
        Q("The fallacy of accent arises from", "a shift of emphasis or quotation out of context",
          [("an argument with too few cases", "That is hasty generalization."), ("a threat", "That is appeal to force."), ("a word with two meanings", "That is equivocation.")],
          0, "A change in stress or context changes the meaning.", "Accent", "Recall", "Think of stress and context."),
        Q("'Each seat in the bus is cheap, so the bus is cheap.' This is", "composition",
          [("division", "That moves from whole to parts."), ("accent", "No emphasis."), ("amphiboly", "No grammar problem.")],
          1, "It moves from parts to whole.", "Composition", "Application", "Which way does the argument move?"),
        Q("'The bus is expensive, so each seat is expensive.' This is", "division",
          [("composition", "That moves from parts to whole."), ("equivocation", "No word shifts."), ("false cause", "No cause.")],
          2, "It moves from whole to parts.", "Division", "Application", "Which way does the argument move?"),
        Q("A headline reads 'Team WINS'; the story says the team won one match and lost five. The fallacy is", "accent",
          [("composition", "No part and whole."), ("division", "No part and whole."), ("straw man", "No position distorted.")],
          3, "Emphasis gives a different impression from the full statement.", "Accent", "Application", "What is stressed?"),
        Q("Which reasoning from parts to whole is SOUND?", "Every plank is wood, so the table is wooden",
          [("Every player is excellent, so the team is excellent", "Teamwork matters."), ("Each brick is light, so the wall is light", "The wall's weight adds up."), ("Each ticket is cheap, so the trip is cheap", "The total may be large.")],
          0, "'Made of wood' passes from parts to whole.", "Sound part-whole reasoning", "Reasoning", "Which property passes from parts to whole?"),
        Q("Composition and division differ because", "the direction of the move is opposite",
          [("one uses words and the other uses numbers", "Not the difference."), ("one is formal and the other is informal", "Both are informal."), ("one needs two premises", "Not the difference.")],
          1, "Composition: parts to whole. Division: whole to parts.", "Composition vs division", "Concept", "Think about direction."),
        Q("The small print 'only on selected items' under a big 'Everything half price' sign is", "accent",
          [("composition", "No part-whole move."), ("complex question", "No question."), ("appeal to pity", "No sympathy.")],
          2, "Emphasis creates a meaning that the full statement does not support.", "Accent", "Application", "What does the big print stress?"),
        Q("The sentence 'The class is noisy' is true. 'So each student in the class is noisy' is", "a fallacy of division",
          [("a valid inference", "A group property need not belong to each member."), ("an appeal to force", "No threat."), ("a fallacy of accent", "No emphasis.")],
          3, "A property of the group is wrongly given to each member.", "Division", "Reasoning", "Does the group property belong to each member?"),
    ]))
