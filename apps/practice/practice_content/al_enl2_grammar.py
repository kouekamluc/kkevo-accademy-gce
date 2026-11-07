"""Practice sets for A Level English Language, Lower Sixth: Grammar (one set per lesson, 8 questions each, Paper 1 Section C style).

All sentences are original and invented. Each question has exactly one correct option; where British and other usage differ,
the question avoids the disputed point.
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "lower-sixth")

M = "Grammar"
T_POS = "Parts of speech"
T_NOUN = "Nouns and quantifiers"
T_VERB = "Verbs: tense, mood, modals and voice"
T_REP = "Reported speech"
T_VERBAL = "Gerunds, infinitives and participles"
T_PRON = "Pronouns and determiners"
T_STYPE = "Sentence types"
T_AGR = "Agreement, fragments, run-on sentences and modifiers"
T_CLAUSE = "Clauses"
T_COMP = "Comparatives, conjunctions and word order"
T_FORMS = "Word forms"
T_PUNCT = "Punctuation"

_POS = [1, 3, 0, 2, 2, 0, 3, 1]   # position of the correct option, so every 8-question set has two of each letter
_count = [0]


def Q(prompt, right, wrongs, step, concept, skill, hint, feedback=""):
    """4-option MC. `right` is the correct option text; `wrongs` is 3 (text, why) pairs. The correct option is placed by a
    fixed cycle so that each set of 8 has A, B, C and D twice."""
    pos = _POS[_count[0] % 8]
    _count[0] += 1
    assert len(wrongs) == 3
    choices = []
    w = iter(wrongs)
    for i in range(4):
        if i == pos:
            choices.append(C(right, correct=True))
        else:
            t, why = next(w)
            choices.append(C(t, why=why))
    steps = [S("Reasoning", text=s) for s in ([step] if isinstance(step, str) else step)]
    return MC(prompt, choices, steps, concept=concept, skill=skill, hint=hint, feedback=feedback)


SETS = []

# ================================================================== 1. Parts of speech
SETS.append(practice_set(
    module=M, topic=T_POS, title="Parts of speech: word class from function",
    lesson="enl2-parts-of-speech-function",
    questions=[
        Q("In the sentence 'The teacher spoke quietly', the word *quietly* is a(n)",
          "adverb", [("adjective", "*Quietly* does not describe a noun; it says how she spoke."), ("preposition", "It links nothing to a noun phrase."), ("conjunction", "It joins no clauses.")],
          "*Quietly* tells how the verb *spoke* happened, so it is an adverb.", "Adverbs of manner", "Recall", "What question does the word answer: what, who or how?"),
        Q("In which sentence is *fast* an adverb?",
          "The bus travelled fast.", [("It was a fast bus.", "Here *fast* describes the noun *bus*: adjective."), ("The fast ended at sunset.", "Here *fast* names the thing (a period of not eating): noun."), ("They fast during the holy month.", "Here *fast* is the action: verb.")],
          "Only in 'The bus travelled fast' does *fast* describe a verb (*travelled*). That is an adverb.", "Conversion", "Concept", "Which sentence has *fast* describing how something moved?"),
        Q("In 'We stayed indoors until the rain stopped', the word *until* is a",
          "conjunction", [("preposition", "A preposition would be followed by a noun phrase, such as *until noon*."), ("adverb", "*Until* does not stand alone here."), ("pronoun", "It does not replace a noun.")],
          "A clause (*the rain stopped*, with its own subject and verb) follows *until*, so it joins two clauses: a conjunction.", "Preposition v conjunction", "Concept", "What follows the word: a noun phrase or a clause with a verb?"),
        Q("In 'She bought a school bag', the word *school* is best described as a",
          "noun used as a modifier of *bag*", [("verb describing the bag", "*School* is not an action here."), ("preposition linking *bag* to *she*", "Nothing is linked by a relation of place or time."), ("pronoun replacing *bag*", "*Bag* is still there; nothing is replaced.")],
          "*School* is a noun by form but modifies *bag* (a noun adjunct). Some textbooks call it an adjective: check your textbook.", "Noun adjunct", "Concept", "What does the word do to the noun after it?"),
        Q("Which sentence uses *before* as a conjunction?",
          "Close the windows before the storm arrives.", [("We met before.", "Nothing follows *before*: adverb."), ("She arrived before noon.", "A noun phrase follows: preposition."), ("The days before were quiet.", "*Before* here follows the noun *days* and gives time: adverb.")],
          "In 'before the storm arrives', *before* introduces a clause (subject *the storm*, verb *arrives*), so it is a conjunction.", "Preposition v conjunction", "Application", "Look for the option where a subject and verb follow *before*."),
        Q("In 'The light in the room was weak', the word *light* is a",
          "noun", [("verb", "It is not an action; the verb is *was*."), ("adjective", "It does not describe another noun; *the* introduces it as a thing."), ("adverb", "It does not describe a verb.")],
          "*The light* names a thing and is the subject of the sentence: a noun.", "Conversion", "Recall", "Is *light* naming something or describing something?"),
        Q("Which word is an adjective?",
          "friendly (in 'a friendly shopkeeper')", [("quickly (in 'She walked quickly')", "This describes *walked*: adverb."), ("beside (in 'beside the door')", "It links a noun phrase to the sentence: preposition."), ("because (in 'because it rained')", "It joins clauses: conjunction.")],
          "*Friendly* ends in *-ly* but describes the noun *shopkeeper*, so it is an adjective.", "Word class by function", "Application", "Do not trust the ending: which word describes a noun?"),
        Q("In 'He walked round the compound slowly and then he looked round', the two uses of *round* are",
          "preposition, then adverb", [("adjective, then adverb", "Neither use describes a noun."), ("preposition, then noun", "The second *round* has no determiner and describes how he looked."), ("adverb, then preposition", "The order is reversed: the first has a noun phrase after it.")],
          "First: *round the compound* links a noun phrase to the verb (preposition; British usage, check your textbook). Second: *looked round* stands alone: adverb.", "Same word, different class", "Analysis", "Does a noun phrase follow each *round*?"),
    ]))

# ================================================================== 2. Nouns and quantifiers
SETS.append(practice_set(
    module=M, topic=T_NOUN, title="Count and non-count nouns, quantifiers",
    lesson="enl2-count-noncount-quantifiers",
    questions=[
        Q("Which sentence is correct?",
          "The traveller carried a lot of luggage.", [("The traveller carried a lot of luggages.", "*Luggage* has no plural."), ("The traveller carried many luggage.", "*Many* needs a plural count noun."), ("The traveller carried a luggage.", "*Luggage* cannot take *a*.")],
          "*Luggage* is non-count: no plural, no *a*, and it takes *a lot of* or *much*.", "Non-count nouns", "Recall", "Can you say 'two luggages'?"),
        Q("Choose the correct word: 'The teacher gave us some useful ______ on how to revise.'",
          "advice", [("advices", "*Advice* is non-count and has no plural."), ("an advice", "It cannot take *an*."), ("advicies", "This is not a word.")],
          "Use the non-count form *advice* after *some*.", "Non-count nouns", "Recall", "Is *advice* a noun you can count?"),
        Q("'There is ______ time left, so we can still finish the experiment.' The word that fits best is",
          "a little", [("a few", "*Few* goes with plural count nouns; *time* here is non-count."), ("few", "Same problem."), ("little", "*Little* means hardly any, which contradicts 'we can still finish'.")],
          "*Time* is non-count, and the second clause is positive, so *a little*.", "Few, little", "Application", "Non-count noun; positive meaning."),
        Q("Which sentence is correct by the traditional rule?",
          "The number of road accidents has fallen.", [("The amount of road accidents has fallen.", "*Accidents* can be counted, so *number*."), ("The number of road accidents have fallen.", "*The number* is singular, so *has*."), ("The amount of road accidents have fallen.", "Two errors.")],
          "*Accidents* are count, so *number*; *the number* is the subject, so the verb is singular: *has*.", "Number v amount", "Application", "What is the subject: *the number* or *accidents*?"),
        Q("Which of these is a plural-only noun?",
          "trousers", [("furniture", "*Furniture* is non-count (singular)."), ("advice", "Non-count (singular)."), ("information", "Non-count (singular).")],
          "*Trousers* has no singular form: we say *a pair of trousers*.", "Plural-only nouns", "Recall", "Which one needs *a pair of* for a single item?"),
        Q("'She has ______ experience as a nurse, so the hospital hired her.' Choose the best word.",
          "a lot of", [("many", "*Experience* here means skill over time: non-count, so not *many*."), ("a few", "*A few* needs a plural count noun."), ("several", "*Several* needs a plural count noun.")],
          "*Experience* meaning skill is non-count: *a lot of* fits.", "Nouns with two meanings", "Application", "Which quantifier fits a non-count noun?"),
        Q("Which sentence is grammatically correct?",
          "The news from the village was encouraging.", [("The news from the village were encouraging.", "*News* is singular."), ("The news from the village were a good news.", "*News* cannot take *a*."), ("The newses from the village were encouraging.", "*News* has no plural form.")],
          "*News* looks plural but is singular and non-count: it takes *was*.", "Singular nouns ending -s", "Concept", "Is *news* one thing or many?"),
        Q("Which sentence is correct?",
          "She has little money, so she cannot buy a phone.", [("She has few money, so she cannot buy a phone.", "*Few* goes with count nouns; *money* is non-count."), ("She has a little money, so she cannot buy a phone.", "*A little* means some; it contradicts 'cannot buy'."), ("She has a few money, so she cannot buy a phone.", "*A few* goes with count nouns.")],
          "*Money* is non-count, so *little* or *a little*. The result 'cannot buy' shows a negative meaning: *little*.", "Few, little", "Reasoning", "Check both the noun type and the meaning of the second clause."),
    ]))

# ================================================================== 3. Tense and aspect
SETS.append(practice_set(
    module=M, topic=T_VERB, title="Tense and aspect: the form that fits the clue",
    lesson="enl2-tense-aspect-state-verbs",
    questions=[
        Q("'My cousin ______ in Limbe since 2018.'",
          "has lived", [("lives", "The simple present does not carry the *since* link."), ("lived", "The past simple would mean she no longer lives there."), ("was living", "The past continuous does not connect to now.")],
          "*Since 2018* requires the present perfect (or perfect continuous).", "Present perfect with since", "Recall", "What does *since* demand?"),
        Q("Choose the correct sentence.",
          "I met her at the market yesterday.", [("I have met her at the market yesterday.", "*Yesterday* names a finished time: no present perfect."), ("I meet her at the market yesterday.", "The present simple does not fit a past time."), ("I am meeting her at the market yesterday.", "The present continuous does not fit a past time.")],
          "A named finished time (*yesterday*) needs the past simple.", "Past simple v present perfect", "Recall", "Look at the time word."),
        Q("'By the time the ambulance arrived, the patient ______ to the clinic by his neighbours.'",
          "had been taken", [("has been taken", "The present perfect clashes with a past time marker."), ("was taking", "Wrong form and voice: he did not take anyone."), ("is taken", "The present does not fit a past story.")],
          "Two past events: being taken came first, so the past perfect passive: *had been taken*.", "Past perfect", "Application", "Which event happened earlier?"),
        Q("Which sentence is correct?",
          "If it rains tomorrow, the football match will be postponed.", [("If it will rain tomorrow, the football match will be postponed.", "No *will* in the *if* clause."), ("If it rained tomorrow, the football match will be postponed.", "The tenses do not match."), ("If it rain tomorrow, the football match will be postponed.", "*It* is singular, so the verb must be *rains*.")],
          "In a condition clause about the future, use the present simple: *rains*.", "Future time clauses", "Application", "What verb form follows *if*?"),
        Q("'As soon as the guests ______, the choir will begin to sing.'",
          "arrive", [("will arrive", "No *will* in a time clause."), ("would arrive", "Wrong mood and time."), ("are going to arrive", "*Going to* does not belong in a time clause like this.")],
          "After *as soon as* we use the present simple for future time.", "Future time clauses", "Application", "Which words introduce time clauses?"),
        Q("Which sentence is grammatically correct?",
          "Do you know the answer?", [("Are you knowing the answer?", "*Know* is a state verb: no continuous."), ("Have you been knowing the answer?", "State verb again."), ("Are you known the answer?", "Wrong voice.")],
          "State verbs such as *know* are used in simple forms.", "State verbs", "Concept", "Is *know* an action in progress?"),
        Q("In which sentence is the verb *have* an action verb that can be continuous?",
          "They are having a meeting.", [("She has a new phone.", "This is possession: a state."), ("He has two brothers.", "This is a relationship: a state."), ("We have enough time.", "This is a state.")],
          "*Having a meeting* means holding it: an action, so the continuous is possible.", "State and action meanings", "Reasoning", "Which sentence describes something happening, not possessing?"),
        Q("Which sentence contains an error in tense?",
          "She has visited her aunt two days ago.", [("She visited her aunt two days ago.", "This is correct."), ("She has visited her aunt this week.", "*This week* is an unfinished period, so the perfect is acceptable."), ("She had visited her aunt before the storm began.", "Correct past perfect for the earlier event.")],
          "*Two days ago* is a finished time, so the present perfect is wrong.", "Error spotting", "Analysis", "Find the time marker that names a finished time."),
    ]))

# ================================================================== 4. Modals
SETS.append(practice_set(
    module=M, topic=T_VERB, title="Modal verbs: meaning and form",
    lesson="enl2-modal-verbs",
    questions=[
        Q("Which sentence is correct?",
          "She can speak three languages.", [("She cans speak three languages.", "Modals take no -s."), ("She can to speak three languages.", "Modals are followed by the base verb with no *to*."), ("She does can speak three languages.", "Modals take no *do*.")],
          "Modal + base verb: no -s, no *to*, no *do*.", "Modal form", "Recall", "What follows a modal?"),
        Q("'You ______ wear a seat belt; it is the law.' Which word shows obligation from a rule?",
          "have to", [("needn't", "That means it is not necessary."), ("might", "That shows possibility."), ("may not", "That would forbid it, but the rule requires it.")],
          "A law is an outside rule, so *have to* (or *must*).", "Obligation", "Recall", "Is the law forcing it or allowing it?"),
        Q("'You ______ park here; the sign says it is forbidden.'",
          "mustn't", [("needn't", "That means it is not necessary, but it is forbidden."), ("don't have to", "Same meaning as *needn't*."), ("shouldn't have", "It is incomplete and has the wrong meaning.")],
          "*Mustn't* expresses prohibition.", "Prohibition", "Concept", "Forbidden or not necessary?"),
        Q("'The candidate looks very pale. He ______ be ill.' The speaker is almost sure. Choose the best word.",
          "must", [("might", "That shows only a weak possibility."), ("needn't", "That is about necessity, not certainty."), ("shall", "That is for offers or promises.")],
          "Strong deduction from evidence: *must*.", "Deduction", "Application", "How sure is the speaker?"),
        Q("'The ground is dry, so it ______ rained last night.'",
          "can't have", [("must have", "That would mean the speaker is sure it rained, but the ground is dry."), ("should have", "That is criticism, not deduction."), ("needn't have", "That means an unnecessary action.")],
          "Dry ground is evidence that it did not rain: *can't have rained*.", "Past deduction", "Application", "Does the evidence support rain or not?"),
        Q("'Efe failed because she did not revise. She ______ harder.'",
          "should have studied", [("must have studied", "That is deduction that she studied, which is false here."), ("can't have studied", "The sentence criticises, not deduces."), ("needn't have studied", "That says studying was unnecessary.")],
          "Regret or criticism about the past: *should have + past participle*.", "Should have", "Application", "Is the speaker criticising or guessing?"),
        Q("Which sentence uses *was able to* correctly for one particular success?",
          "Although the road was blocked, the driver was able to reach the village.", [("Although the road was blocked, the driver can reach the village.", "*Can* is present tense."), ("Although the road was blocked, the driver able to reach the village.", "The verb *be* is missing."), ("Although the road was blocked, the driver was can reach the village.", "Modal *can* cannot follow *was*.")],
          "A single past achievement takes *was able to* (not general *could*).", "Ability", "Concept", "Past, single success."),
        Q("Which sentence has a modal-verb error?",
          "He musts finish before noon.", [("He must finish before noon.", "This is correct."), ("Must he finish before noon?", "This is correct."), ("He mustn't finish after noon.", "This is correct (a prohibition).")],
          "Modals take no -s: *He must finish*.", "Modal form", "Analysis", "Which modal has an ending it should not have?"),
    ]))

# ================================================================== 5. Mood and voice
SETS.append(practice_set(
    module=M, topic=T_VERB, title="Mood and voice: subjunctive and passive",
    lesson="enl2-mood-and-voice",
    questions=[
        Q("Which sentence is in the imperative mood?",
          "Please close the door.", [("The door is closed.", "A statement of fact: indicative."), ("I wish the door were closed.", "A wish: subjunctive."), ("She closes the door.", "A statement: indicative.")],
          "The imperative gives a command or request, usually with no subject.", "Mood", "Recall", "Which sentence tells someone to do something?"),
        Q("'If I ______ you, I would apply for the scholarship.'",
          "were", [("am", "The condition is unreal, so not the indicative."), ("will be", "*Will* is not used in an *if* clause of this type."), ("have been", "Wrong form for an unreal present condition.")],
          "An unreal condition uses the past subjunctive *were*.", "Subjunctive", "Recall", "Is the speaker really 'you'?"),
        Q("'The committee recommends that the treasurer ______ a report every month.'",
          "submit", [("submits", "After *recommends that*, the base form is used (present subjunctive), even with *he/she*."), ("submitted", "The subjunctive uses the base form, not the past."), ("is submitting", "Not used in the pattern.")],
          "Verb of recommendation + *that* + base form.", "Subjunctive", "Application", "What kind of verb is *recommends*?"),
        Q("The correct passive of 'The headmaster has announced the results' is",
          "The results have been announced by the headmaster.", [("The results are announced by the headmaster.", "This is present simple."), ("The results had been announced by the headmaster.", "This is past perfect."), ("The results were announced by the headmaster.", "This is past simple.")],
          "Active present perfect becomes *have been + past participle*.", "Passive forms", "Application", "Copy the tense: present perfect."),
        Q("Which sentence is the correct passive of 'You must complete the form'?",
          "The form must be completed.", [("The form must complete.", "No *be* and no participle."), ("The form must be completing.", "Wrong participle."), ("The form must been completed.", "*Been* cannot follow a modal directly.")],
          "Modal + *be* + past participle.", "Modal passive", "Application", "What follows a modal in the passive?"),
        Q("Which sentence cannot be turned into a passive?",
          "The meeting began at nine.", [("The council built the school.", "It has an object (*the school*), so it can be passive."), ("The students painted the hall.", "It has an object."), ("The mechanic repaired the generator.", "It has an object.")],
          "*Begin* here is intransitive: no object, so no passive.", "Transitive and intransitive", "Concept", "Which sentence has no object?"),
        Q("'I wish I ______ taller.' The most formal correct form is",
          "were", [("am", "A wish is unreal; the present indicative is wrong."), ("be", "The base form is not used here."), ("would be", "*Would* is not used after *wish* for *be* in this way.")],
          "*Wish* takes the past subjunctive *were* for all persons in formal English (informal speech uses *was*; check your textbook).", "Subjunctive", "Concept", "Is the wish real?"),
        Q("Which sentence is in the passive voice?",
          "The match was postponed because of the rain.", [("The referee postponed the match.", "Active: the subject does the action."), ("The match began at four.", "Active and intransitive."), ("Everyone enjoyed the match.", "Active.")],
          "*Was postponed* = be + past participle with the match as receiver.", "Voice", "Analysis", "Which subject receives the action?"),
    ]))

# ================================================================== 6. Reported speech
SETS.append(practice_set(
    module=M, topic=T_REP, title="Reported speech: tense, questions and reporting verbs",
    lesson="enl2-reported-speech",
    questions=[
        Q("'I am tired,' said Mbah last week. In the standard exam form, the report is: Mbah said that he ______ tired.",
          "was", [("is", "Backshift: present moves to past."), ("has been", "Present perfect is a different tense."), ("had been", "Too far back for a simple present.")],
          "Simple present becomes simple past after a past reporting verb.", "Backshift", "Recall", "One step back."),
        Q("'We will leave tomorrow,' said the guide. The correct report is:",
          "The guide said that they would leave the next day.", [("The guide said that they will leave tomorrow.", "No backshift and no change of time word."), ("The guide said that we would leave tomorrow.", "Pronoun and time word not changed."), ("The guide said that they would leave yesterday.", "Wrong time word.")],
          "*Will* becomes *would*, *we* becomes *they*, *tomorrow* becomes *the next day*.", "Backshift and time words", "Application", "Change three things."),
        Q("'Where is the library?' she asked. The correct report is: She asked ______.",
          "where the library was", [("where was the library", "A reported question uses statement order."), ("where the library is?", "No question mark and no backshift."), ("that where the library was", "*That* is not used with a question word.")],
          "Statement order and past tense: *where the library was*.", "Reported questions", "Recall", "Is the order a question or a statement?"),
        Q("'Do you play football?' he asked me. The correct report is:",
          "He asked me whether I played football.", [("He asked me that I played football.", "A yes/no question needs *if* or *whether*."), ("He asked me did I play football.", "Question order is kept."), ("He asked me if I do play football.", "The tense is not backshifted.")],
          "Yes/no question: *if/whether* + statement order + backshift.", "Reported questions", "Application", "Which linking word starts a yes/no question?"),
        Q("'Please wait here,' the receptionist said to us. The correct report is:",
          "The receptionist asked us to wait there.", [("The receptionist asked us wait there.", "*To* is missing."), ("The receptionist asked that we wait here.", "*Here* should become *there*; the command pattern is better."), ("The receptionist said us to wait there.", "*Say* does not take this pattern; use *tell* or *ask*.")],
          "Request: ask + object + to + base verb; *here* becomes *there*.", "Reported commands", "Application", "Pattern: ask + object + to."),
        Q("'I didn't break the window,' said Joe. Which is the best report using one reporting verb?",
          "Joe denied breaking the window.", [("Joe admitted breaking the window.", "*Admit* means he did it."), ("Joe promised to break the window.", "Wrong meaning."), ("Joe denied to break the window.", "*Deny* takes the -ing form.")],
          "*Deny* + -ing.", "Reporting verbs", "Application", "Which verb means 'say it is not true'?"),
        Q("'You cheated in the exam!' the examiner said to Ako. Which report is correct?",
          "The examiner accused Ako of cheating in the exam.", [("The examiner accused Ako for cheating in the exam.", "*Accuse* goes with *of*."), ("The examiner accused Ako to cheat in the exam.", "Wrong pattern."), ("The examiner accused Ako that he cheated in the exam.", "*Accuse* does not take a *that*-clause.")],
          "Accuse + object + of + -ing.", "Reporting verbs", "Application", "Which preposition follows *accuse*?"),
        Q("'I can't find my keys,' said Linda. Which report has correct backshift and pronouns?",
          "Linda said that she couldn't find her keys.", [("Linda said that I couldn't find my keys.", "The pronouns are not changed to suit the reporter."), ("Linda said that she not could find her keys.", "The negative is misplaced: modals take *not* after them."), ("Linda said that she couldn't found her keys.", "A modal is followed by the base verb, not the past form.")],
          "*Can't* becomes *couldn't*; *I* becomes *she*; *my* becomes *her*; the modal is followed by the base verb.", "Modals in reported speech", "Reasoning", "Change the modal, the subject pronoun and the possessive."),
    ]))

# ================================================================== 7. Gerunds and infinitives
SETS.append(practice_set(
    module=M, topic=T_VERBAL, title="Gerunds and infinitives: verb patterns",
    lesson="enl2-gerunds-infinitives",
    questions=[
        Q("'She enjoys ______ stories to her younger brother.'",
          "reading", [("to read", "*Enjoy* is followed by a gerund."), ("read", "A bare infinitive does not follow *enjoys*."), ("to reading", "*To* is not used here.")],
          "*Enjoy* + gerund.", "Gerund after enjoy", "Recall", "Is *enjoy* in the gerund list?"),
        Q("'The company has decided ______ twenty new workers.'",
          "to employ", [("employing", "*Decide* takes an infinitive."), ("employ", "The bare infinitive does not follow *decided*."), ("employed", "The past form does not fit the pattern.")],
          "*Decide* + infinitive.", "Infinitive after decide", "Recall", "Which list is *decide* in?"),
        Q("'He is interested in ______ a career in nursing.'",
          "pursuing", [("to pursue", "After a preposition use a gerund."), ("pursue", "A bare infinitive cannot follow a preposition."), ("pursued", "The past tense does not fit.")],
          "Preposition *in* + gerund.", "Preposition + gerund", "Application", "What kind of word is *in*?"),
        Q("'We are looking forward to ______ you at the ceremony.'",
          "seeing", [("see", "*To* here is a preposition, so a bare infinitive is wrong."), ("seen", "The participle does not fit the pattern."), ("having see", "Incorrect form.")],
          "*Look forward to* + gerund.", "To as a preposition", "Concept", "Can you put a noun after *to*?"),
        Q("'The teacher made the students ______ the exercise again.'",
          "do", [("to do", "After *made* + object, use the bare infinitive."), ("doing", "A gerund is wrong here."), ("done", "Not the pattern with active *made*.")],
          "*Make* + object + bare infinitive.", "Bare infinitive", "Recall", "Which verb is followed by an infinitive without *to*?"),
        Q("Which sentence means that the speaker no longer does the activity?",
          "He stopped smoking.", [("He stopped to smoke.", "He paused in order to smoke."), ("He remembered to smoke.", "A different meaning altogether."), ("He tried to smoke.", "A different meaning.")],
          "*Stop* + gerund = end the activity.", "Stop + -ing", "Concept", "Does the action end, or does he pause to do it?"),
        Q("Which sentence has the same meaning as 'I did not post the letter because I forgot'?",
          "I forgot to post the letter.", [("I forgot posting the letter.", "That means I posted it but cannot recall."), ("I remember posting the letter.", "That means I did post it."), ("I stopped posting the letter.", "A different meaning.")],
          "*Forget to* = fail to do what you should.", "Remember/forget", "Reasoning", "Was the letter posted or not?"),
        Q("Which sentence contains an error?",
          "He avoided to meet the manager.", [("He avoided meeting the manager.", "Correct."), ("He managed to meet the manager.", "Correct."), ("He refused to meet the manager.", "Correct.")],
          "*Avoid* takes a gerund, so *avoided to meet* is wrong.", "Error spotting", "Analysis", "Check each verb's pattern."),
    ]))

# ================================================================== 8. Participles
SETS.append(practice_set(
    module=M, topic=T_VERBAL, title="Participles and participle phrases",
    lesson="enl2-participles-phrases",
    questions=[
        Q("'The students were ______ by the long journey.' Choose the correct word.",
          "exhausted", [("exhausting", "That describes what causes tiredness, not the people who feel it."), ("exhaust", "Not an adjective."), ("exhausts", "A verb form, not an adjective.")],
          "People who feel the effect: the *-ed* participle.", "-ed adjectives", "Recall", "Is the word describing the students or the cause?"),
        Q("'The film was so ______ that nobody left their seats.'",
          "exciting", [("excited", "That would describe people, not the film."), ("excite", "Not an adjective."), ("excitedly", "An adverb.")],
          "The film causes the excitement: *-ing* form.", "-ing adjectives", "Recall", "Cause or feeling?"),
        Q("Choose the sentence in which the participle phrase is correct.",
          "Opening the door, the teacher found the room empty.", [("Opening the door, the room was empty.", "The room did not open the door."), ("Opening the door, the empty room surprised him.", "The room did not open the door."), ("Opening the door, it was empty.", "*It* did not open the door.")],
          "The phrase must belong to the subject of the main clause: *the teacher*.", "Subject of the phrase", "Application", "Who opened the door?"),
        Q("'______ the exam, the candidates left the hall quietly.' Which fits best, showing the earlier action?",
          "Having finished", [("Finishing", "Suggests that the two actions were at the same time."), ("Finished", "Passive meaning; the candidates did the action."), ("To finish", "Expresses purpose.")],
          "The finishing came before leaving: perfect participle.", "Perfect participle", "Application", "Which action came first?"),
        Q("In 'Swimming in the river is dangerous', the word *swimming* is a",
          "gerund", [("present participle", "It does not describe a noun or begin a phrase; it is the subject."), ("past participle", "Wrong form."), ("infinitive", "Not *to swim*.")],
          "It is the subject of the sentence: a noun job, so a gerund.", "Gerund v participle", "Concept", "Is it the subject?"),
        Q("In 'The crying child ran to its mother', the word *crying* is a",
          "present participle used as an adjective", [("gerund used as subject", "It is not the subject; *child* is."), ("past participle", "It ends in -ing."), ("preposition", "Not a preposition.")],
          "It describes the noun *child*: participle as adjective.", "Gerund v participle", "Concept", "What does the word describe?"),
        Q("Which sentence uses a past participle phrase correctly?",
          "Built in 1960, the school is still in use.", [("Building in 1960, the school is still in use.", "The school did not build."), ("Having built in 1960, the school is still in use.", "Wrong participle for a passive meaning."), ("Build in 1960, the school is still in use.", "Wrong form.")],
          "The school received the action (it was built): past participle.", "Past participle", "Application", "Did the school do the building or receive it?"),
        Q("Which sentence is correct?",
          "The boy standing near the gate is my cousin.", [("The boy stand near the gate is my cousin.", "Missing -ing: the phrase needs a participle."), ("The boy stood near the gate is my cousin.", "Wrong participle."), ("The boy to stand near the gate is my cousin.", "An infinitive does not describe in this way.")],
          "A participle can replace *who is standing*.", "Participle replacing relative clause", "Analysis", "Which form replaces 'who is standing'?"),
    ]))

# ================================================================== 9. Pronouns
SETS.append(practice_set(
    module=M, topic=T_PRON, title="Pronouns: case, reflexives, who and whom",
    lesson="enl2-pronouns-forms-omission",
    questions=[
        Q("'The principal spoke to Abena and ______ after the meeting.'",
          "me", [("I", "The pronoun is the object of *to*: use the object form."), ("myself", "The subject is *the principal*, so no reflexive."), ("mine", "A possessive pronoun cannot be the object here.")],
          "Remove *Abena and*: 'spoke to me'.", "Pronoun case", "Recall", "Is the pronoun a subject or an object?"),
        Q("'______ and Efe are going to the market.'",
          "He", [("Him", "Subjects take the subject form."), ("Himself", "No reflexive is needed."), ("His", "A possessive adjective cannot be a subject.")],
          "Subject position: *He*.", "Pronoun case", "Recall", "Remove *and Efe*: 'Him is going'?"),
        Q("'The candidate ______ the examiners interviewed last was the youngest.' Choose the formal correct pronoun.",
          "whom", [("who", "The pronoun is the object of *interviewed*; formal English prefers *whom*."), ("whose", "Shows possession, not an object."), ("which", "Used for things, not people.")],
          "Replace with *him*: 'the examiners interviewed him'.", "Who v whom", "Application", "Can you replace it with *he* or *him*?"),
        Q("'The old man ______ lives near the church repairs radios.'",
          "who", [("whom", "The pronoun is the subject of *lives*."), ("whose", "Shows possession."), ("whoever", "Wrong form for a defining relative clause.")],
          "Replace with *he*: 'he lives near the church'.", "Who v whom", "Application", "Subject or object of *lives*?"),
        Q("Which sentence uses a reflexive pronoun correctly?",
          "She taught herself to type.", [("The principal asked Efe and myself to wait.", "Reflexive is not needed: *me*."), ("Ngu and myself won the prize.", "The subject form *I* is needed."), ("He gave the letter to the clerk and himself.", "Unclear and unnatural: *himself* has no matching subject action.")],
          "Subject and object are the same person: *She ... herself*.", "Reflexive pronouns", "Concept", "Is the object the same person as the subject?"),
        Q("Which sentence contains a double subject?",
          "My sister she works in Douala.", [("My sister works in Douala.", "Correct."), ("She works in Douala.", "Correct."), ("My sister, who works in Douala, called.", "Correct.")],
          "*My sister she* repeats the subject.", "Double subject", "Concept", "Is the subject named twice?"),
        Q("In which sentence can the pronoun *that* be omitted?",
          "The phone that I lost was new.", [("The phone that rang was new.", "*That* is the subject of *rang*."), ("The phone that is on the desk is new.", "*That* is the subject of *is*."), ("The phone that costs 30,000 FCFA is new.", "*That* is the subject of *costs*.")],
          "In the first, *that* is the object of *lost*: it can be dropped.", "Omitting relative pronouns", "Reasoning", "Is *that* the subject of its own clause?"),
        Q("Which sentence is correct?",
          "Everyone has finished the work.", [("Everyone have finished the work.", "*Everyone* takes a singular verb."), ("Everyone has finished it's work.", "*It's* means *it is*."), ("Everyone are finished the work.", "Singular verb needed; also wrong participle phrasing.")],
          "*Everyone* takes a singular verb: *has*.", "Indefinite pronouns", "Analysis", "Singular or plural verb after *everyone*?"),
    ]))

# ================================================================== 10. Determiners
SETS.append(practice_set(
    module=M, topic=T_PRON, title="Determiners: articles, numerals and quantifiers",
    lesson="enl2-determiners",
    questions=[
        Q("'She has ______ unusual hobby: she collects old coins.'",
          "an", [("a", "*Unusual* starts with a vowel sound."), ("the", "The hobby is introduced for the first time."), ("no article", "A singular count noun needs a determiner.")],
          "A vowel sound follows: *an*.", "A or an", "Recall", "Say the next word aloud."),
        Q("'He is studying at ______ university in Buea.'",
          "a", [("an", "*University* begins with a consonant sound /j/."), ("the", "Not a specific, known university."), ("no article", "A singular count noun needs a determiner.")],
          "Sound /j/ (consonant): *a*.", "A or an", "Recall", "What is the first sound of *university*?"),
        Q("Which sentence is correct?",
          "Honesty is the best policy.", [("The honesty is the best policy.", "General ideas take no article."), ("Honesty is best the policy.", "Word order error."), ("An honesty is the best policy.", "*Honesty* is non-count.")],
          "No article for the general idea; *the* with the superlative-like *best policy*.", "Zero article", "Recall", "Is the idea general?"),
        Q("'The principal addressed ______ students in the hall.'",
          "two hundred", [("two hundreds", "No -s after an exact number."), ("two hundred of", "*Of* does not follow an exact number here."), ("hundred two", "Wrong order.")],
          "Exact number: *hundred* takes no -s.", "Numerals", "Recall", "Is the number exact?"),
        Q("Which sentence is correct?",
          "Each of the girls has finished her task.", [("Each of the girls have finished her task.", "*Each* takes a singular verb."), ("Each girls has finished her task.", "*Each* is followed by a singular noun."), ("Every of the girls has finished her task.", "*Every of* is wrong; use *each of* or *every one of*.")],
          "*Each of the* + plural noun + singular verb.", "Distributive determiners", "Application", "Check the noun and the verb."),
        Q("'I have two sisters. ______ of them is a nurse; the other is a teacher.'",
          "One", [("Both", "*Both* would mean the two of them, but the sentence says the other is different."), ("None", "That contradicts 'the other is a teacher'."), ("All", "*All* is for three or more.")],
          "One of two, then *the other*.", "One, the other", "Application", "Which word starts the pair 'one ... the other'?"),
        Q("Which sentence uses *the* correctly?",
          "Mount Cameroon rises near the Atlantic Ocean.", [("The Mount Cameroon rises near the Atlantic Ocean.", "A mountain name with *Mount* takes no article."), ("Mount Cameroon rises near Atlantic Ocean.", "Oceans take *the*."), ("The Mount Cameroon rises near Atlantic Ocean.", "Both uses are wrong.")],
          "No article before *Mount Cameroon*; *the* before an ocean.", "Articles with names", "Reasoning", "Which name needs *the*: a mountain or an ocean?"),
        Q("Which sentence has the correct determiner order?",
          "Both my brothers live in Douala.", [("My both brothers live in Douala.", "The predeterminer *both* comes first."), ("Both brothers my live in Douala.", "A determiner comes before the noun."), ("Brothers both my live in Douala.", "The noun must come last.")],
          "Predeterminer, determiner, noun: *both my brothers*.", "Determiner order", "Analysis", "Which word comes first?"),
    ]))

# ================================================================== 11. Sentence types
SETS.append(practice_set(
    module=M, topic=T_STYPE, title="Sentence types: simple, compound, complex, compound-complex",
    lesson="enl2-sentence-types",
    questions=[
        Q("'The farmers sold their cocoa at the market.' This sentence is",
          "simple", [("compound", "There is only one clause."), ("complex", "There is no dependent clause."), ("compound-complex", "There is only one clause.")],
          "One subject and one verb: one independent clause.", "Simple sentences", "Recall", "How many clauses?"),
        Q("'Efe likes football, but her brother prefers athletics.' This sentence is",
          "compound", [("simple", "It has two clauses."), ("complex", "There is no dependent clause; *but* joins equal clauses."), ("compound-complex", "There is no dependent clause.")],
          "Two independent clauses joined by *but*.", "Compound sentences", "Recall", "Are the two clauses equal?"),
        Q("'Because the road was flooded, the bus did not arrive.' This sentence is",
          "complex", [("simple", "It has two clauses."), ("compound", "*Because* introduces a dependent clause."), ("compound-complex", "There is only one independent clause.")],
          "One dependent (*Because the road was flooded*) and one independent clause.", "Complex sentences", "Recall", "Which clause cannot stand alone?"),
        Q("'She opened the window and called to her friend.' This sentence is",
          "simple", [("compound", "*And* joins two verbs with one subject, not two clauses."), ("complex", "No dependent clause."), ("compound-complex", "Only one subject and no dependent clause.")],
          "One subject, two verbs: a compound predicate in a simple sentence.", "Simple sentences", "Concept", "How many subjects are there?"),
        Q("'The man who sold me the phone said that it was new, but it broke in a week.' This sentence is",
          "compound-complex", [("simple", "Several clauses are present."), ("compound", "It also contains dependent clauses (*who sold me the phone*, *that it was new*)."), ("complex", "There are two independent clauses joined by *but*.")],
          "Independent clauses: *the man said* and *it broke in a week*; dependent: *who...* and *that...*.", "Compound-complex sentences", "Analysis", "Count the independent clauses."),
        Q("Which sentence is punctuated correctly?",
          "The exam was long; however, most candidates finished.", [("The exam was long, however, most candidates finished.", "A comma splice."), ("The exam was long however, most candidates finished.", "Missing the semicolon or full stop."), ("The exam was long; however most candidates finished.", "A comma is needed after *however*.")],
          "A conjunctive adverb between independent clauses: semicolon before, comma after.", "Conjunctive adverbs", "Application", "How do you join two clauses with *however*?"),
        Q("Which option combines these sentences into a complex sentence? Original: 'It rained heavily. The match was cancelled.'",
          "Because it rained heavily, the match was cancelled.", [("It rained heavily, so the match was cancelled.", "That is compound."), ("It rained heavily; the match was cancelled.", "That is compound."), ("It rained heavily and the match was cancelled.", "That is compound.")],
          "A subordinating conjunction (*because*) makes one clause dependent.", "Combining sentences", "Application", "Which option uses a subordinator?"),
        Q("Which of these is a dependent clause? (a) 'We left after lunch.' (b) 'We left after we had eaten.' (c) 'We left, and they stayed.' (d) 'We left.'",
          "(b) 'after we had eaten' in 'We left after we had eaten.'", [("(a) 'after lunch'", "A phrase: no verb of its own."), ("(c) 'they stayed'", "An independent clause."), ("(d) 'We left'", "An independent clause.")],
          "*After we had eaten* has a subject and verb but cannot stand alone.", "Clause or phrase", "Analysis", "Look for a subject and verb that depends on another clause."),
    ]))

# ================================================================== 12. Agreement
SETS.append(practice_set(
    module=M, topic=T_AGR, title="Agreement: difficult subjects",
    lesson="enl2-agreement-difficult-cases",
    questions=[
        Q("'The box of old books ______ on the table.'",
          "was", [("were", "The subject is *box*, not *books*."), ("are", "Plural and present."), ("have been", "Plural.")],
          "The subject is *box*: singular.", "True subject", "Recall", "What is on the table: the box or the books?"),
        Q("'The teacher, together with her pupils, ______ visiting the museum.'",
          "is", [("are", "*Together with* does not make the subject plural."), ("were", "Plural, and past tense."), ("have been", "Plural.")],
          "Subject: *the teacher*.", "Together with", "Recall", "Which word is the subject?"),
        Q("'Neither the manager nor the clerks ______ aware of the problem.'",
          "were", [("was", "The nearer subject *clerks* is plural."), ("is", "Singular and present."), ("has been", "Singular.")],
          "Proximity: *clerks* is nearer.", "Neither/nor", "Application", "Which subject is nearer to the verb?"),
        Q("'A number of candidates ______ arrived late.'",
          "have", [("has", "*A number of* means several: plural."), ("is", "Not a past/perfect structure."), ("was", "Wrong form.")],
          "*A number of* + plural noun + plural verb.", "A number of", "Application", "Does the phrase mean several or one count?"),
        Q("'The number of candidates ______ risen this year.'",
          "has", [("have", "*The number* is singular."), ("are", "Wrong form."), ("were", "Wrong form.")],
          "Subject *number*: singular.", "The number of", "Application", "What is the subject?"),
        Q("'Mathematics ______ my favourite subject.'",
          "is", [("are", "*Mathematics* is singular."), ("were", "Past plural."), ("have been", "Plural.")],
          "A field of study ending in -s is singular.", "Singular nouns in -s", "Recall", "Is it one subject or many?"),
        Q("'She is one of the nurses who ______ trained in Germany.'",
          "were", [("was", "*Who* refers to *nurses*, plural."), ("has", "Singular."), ("is", "Singular and present.")],
          "*Who* stands for *nurses*: plural.", "One of the ... who", "Reasoning", "What does *who* refer to?"),
        Q("Which sentence is correct?",
          "The cost of the repairs is very high.", [("The cost of the repairs are very high.", "The subject is *cost*."), ("The costs of the repairs is very high.", "*Costs* is plural."), ("The cost of the repairs were very high.", "Plural verb with a singular subject.")],
          "Subject: *cost*, singular.", "True subject", "Analysis", "Which word is the subject?"),
    ]))

# ================================================================== 13. Fragments, run-ons, modifiers
SETS.append(practice_set(
    module=M, topic=T_AGR, title="Fragments, run-ons and modifiers",
    lesson="enl2-fragments-runons-modifiers",
    questions=[
        Q("Which is a sentence fragment?",
          "Because the road was closed.", [("The road was closed.", "A complete sentence."), ("Close the road.", "A complete command."), ("The road closed early.", "A complete sentence.")],
          "A dependent clause alone is a fragment.", "Fragments", "Recall", "Which group cannot stand alone?"),
        Q("Which is a comma splice?",
          "The shop was closed, we went home.", [("The shop was closed, so we went home.", "A conjunction is present."), ("The shop was closed; we went home.", "A semicolon is correct."), ("The shop was closed. We went home.", "Two sentences.")],
          "Two independent clauses with only a comma.", "Comma splice", "Recall", "Look for two clauses and a bare comma."),
        Q("Which is a correct repair of 'It rained all night the river rose'?",
          "It rained all night, so the river rose.", [("It rained all night, the river rose.", "Still a comma splice."), ("It rained all night the river, rose.", "The comma is in the wrong place."), ("It rained all night so, the river rose.", "The comma is in the wrong place.")],
          "Comma + coordinating conjunction.", "Run-on repair", "Application", "Which option uses a conjunction correctly?"),
        Q("Which sentence has a dangling modifier?",
          "Walking along the road, the rain began.", [("Walking along the road, I saw a snake.", "The phrase fits the subject *I*."), ("As I walked along the road, the rain began.", "A full clause."), ("The rain began as I walked along the road.", "A full clause.")],
          "The rain was not walking.", "Dangling modifiers", "Application", "Who is walking?"),
        Q("Which sentence places its modifier correctly?",
          "I bought a leather bag from a trader.", [("I bought a bag from a trader made of leather.", "The phrase seems to describe the trader."), ("Made of leather, I bought a bag from a trader.", "The phrase dangles: I am not made of leather."), ("I bought from a trader made of leather a bag.", "The phrase again seems to describe the trader.")],
          "Put the descriptive word next to the noun it describes: *a leather bag*.", "Misplaced modifiers", "Reasoning", "Which noun is made of leather?"),
        Q("Which sentence is a correct repair of 'Tired after the match, the bed felt wonderful'?",
          "Tired after the match, the players found the bed wonderful.", [("Tired after the match, the bed felt wonderful.", "The bed was not tired."), ("The bed felt wonderful tired after the match.", "The modifier is still attached to the wrong word."), ("After the match tired, the bed felt wonderful.", "The modifier is misplaced and ungrammatical.")],
          "The doer of *tired* must be the subject.", "Dangling modifier repair", "Application", "Who is tired?"),
        Q("Which sentence has a misplaced modifier?",
          "The man bought a goat from the farmer with a limp.", [("The man with a limp bought a goat from the farmer.", "The modifier is next to the man."), ("The man bought a goat from the farmer who limps.", "Clear."), ("The man bought a limping goat from the farmer.", "Clear.")],
          "'With a limp' is next to *farmer* but may be meant for the goat or the man: unclear.", "Misplaced modifiers", "Analysis", "To which noun is the phrase attached?"),
        Q("Which is NOT a correct way to repair a run-on sentence?",
          "Add a second comma between the clauses.", [("Add a full stop between the clauses.", "A correct repair."), ("Add a semicolon between the clauses.", "A correct repair."), ("Add a coordinating conjunction after a comma.", "A correct repair.")],
          "A comma alone, even doubled, does not join two independent clauses.", "Repair methods", "Concept", "Find the option that still leaves the clauses fused."),
    ]))

# ================================================================== 14. Noun and adverb clauses
SETS.append(practice_set(
    module=M, topic=T_CLAUSE, title="Noun clauses and adverb clauses",
    lesson="enl2-noun-adverb-clauses",
    questions=[
        Q("In 'I know that the bus is late', the clause *that the bus is late* is a",
          "noun clause", [("adjective clause", "It does not describe a noun."), ("adverb clause", "It does not tell when, where or why."), ("main clause", "It cannot stand alone.")],
          "It is the object of *know*: a noun job.", "Noun clauses", "Recall", "What job does it do for the verb *know*?"),
        Q("'She asked ______.'",
          "where he lived", [("where did he live", "Question order is not used in a noun clause."), ("where he does live", "Tense not changed, and unnatural."), ("that where he lived", "*That* is not used with a question word.")],
          "Statement order and past tense: *where he lived*.", "Indirect questions", "Application", "Which option has statement order?"),
        Q("'______ the heavy traffic, we reached the airport on time.'",
          "Despite", [("Although", "*Although* needs a clause."), ("Because", "Wrong meaning and needs a clause."), ("Unless", "Wrong meaning and needs a clause.")],
          "A noun phrase follows: *despite*.", "Although v despite", "Recall", "Noun phrase or clause?"),
        Q("Which sentence is correct?",
          "Although he was tired, he finished the work.", [("Although he was tired, but he finished the work.", "Two linking words."), ("Despite he was tired, he finished the work.", "*Despite* needs a noun phrase."), ("Though he was tired, however he finished the work.", "Two linking words.")],
          "One conjunction only.", "Double conjunctions", "Application", "Count the linking words."),
        Q("'The bag was ______ heavy that she could not lift it.'",
          "so", [("such", "*Such* is followed by a noun phrase."), ("very", "*Very* does not take *that*."), ("too", "*Too* is followed by *to* + infinitive.")],
          "*So* + adjective + *that*.", "So ... that", "Recall", "Which word fits an adjective?"),
        Q("'It was ______ a heavy bag that she could not lift it.'",
          "such", [("so", "*So* would need an adjective directly."), ("very", "*Very* does not fit this structure."), ("too", "*Too* does not fit this structure.")],
          "*Such* + a/an + adjective + noun.", "Such ... that", "Application", "A noun phrase follows."),
        Q("The adverb clause in 'He saved money so that he could buy a bicycle' shows",
          "purpose", [("reason", "It states the aim, not the cause."), ("result", "*Result* would be 'so ... that' with a fact."), ("condition", "No *if* idea.")],
          "*So that* + *could* = purpose.", "Adverb clauses", "Concept", "What does the saver want?"),
        Q("Which sentence contains a noun clause as the subject?",
          "What the teacher said surprised the class.", [("The class was surprised by the teacher.", "No clause as subject."), ("The teacher spoke when the class was quiet.", "An adverb clause."), ("The class that sat in front was surprised.", "An adjective clause.")],
          "*What the teacher said* is the subject of *surprised*.", "Noun clauses", "Analysis", "Find the clause that acts as the subject."),
    ]))

# ================================================================== 15. Relative clauses
SETS.append(practice_set(
    module=M, topic=T_CLAUSE, title="Relative clauses",
    lesson="enl2-relative-clauses",
    questions=[
        Q("'The girl ______ won the prize is my cousin.'",
          "who", [("whom", "The pronoun is the subject of *won*."), ("whose", "Shows possession."), ("which", "Used for things.")],
          "A person, subject: *who*.", "Relative pronouns", "Recall", "Person or thing? Subject or object?"),
        Q("'The man ______ car was stolen reported it.'",
          "whose", [("who", "Possession is needed."), ("whom", "Possession is needed."), ("which", "Possession of a person.")],
          "*Whose* shows possession.", "Whose", "Recall", "Whose car?"),
        Q("'Mount Cameroon, ______ is a volcano, is popular with hikers.'",
          "which", [("that", "*That* is not used in non-defining clauses."), ("what", "Not a relative pronoun here."), ("who", "Used for people.")],
          "Non-defining clause about a thing: *which*, with commas.", "Non-defining clauses", "Application", "Are there commas?"),
        Q("'The village ______ I was born is near Bafia.'",
          "where", [("which", "*Which where* would need a preposition: *in which*."), ("whose", "Not possession."), ("when", "Refers to time.")],
          "A place: *where*.", "Where", "Recall", "Place, time or reason?"),
        Q("Which sentence is correct and formal?",
          "This is the lady to whom I spoke.", [("This is the lady to who I spoke.", "After a preposition use *whom*."), ("This is the lady to that I spoke.", "*That* does not follow a preposition."), ("This is the lady whom I spoke.", "The preposition *to* is missing.")],
          "Preposition + whom.", "Prepositions in relative clauses", "Application", "What follows a preposition?"),
        Q("Which sentence says that all the students were absent?",
          "The students, who were ill, were absent.", [("The students who were ill were absent.", "Only some students were ill."), ("The students that were ill were absent.", "Only some students were ill."), ("The students who ill were absent.", "Ungrammatical.")],
          "Commas give extra information about all of them.", "Defining v non-defining", "Reasoning", "What do the commas signal?"),
        Q("Which sentence is incorrect?",
          "The book which I read it was interesting.", [("The book which I read was interesting.", "Correct."), ("The book I read was interesting.", "Correct (pronoun omitted)."), ("The book that I read was interesting.", "Correct.")],
          "*It* repeats the object that *which* already stands for.", "Repeated pronoun", "Analysis", "Is the object stated twice?"),
        Q("'The bus broke down, ______ made us late.'",
          "which", [("what", "Not a relative pronoun here."), ("that", "Not used after a comma for a whole clause."), ("who", "Used for people.")],
          "*Which* can refer to the whole preceding clause.", "Which for a clause", "Application", "What does the pronoun refer to?"),
    ]))

# ================================================================== 16. Comparatives and conjunctions
SETS.append(practice_set(
    module=M, topic=T_COMP, title="Comparatives, superlatives and conjunctions",
    lesson="enl2-comparison-conjunctions",
    questions=[
        Q("'This exercise is ______ than the last one.'",
          "easier", [("more easier", "Double comparison."), ("easiest", "Superlative is for three or more."), ("most easy", "Wrong form.")],
          "Short -y word: *easier*.", "Comparatives", "Recall", "Is it a comparison of two?"),
        Q("'She is the ______ student in the whole school.' (three or more)",
          "best", [("better", "Comparative is for two."), ("most good", "Irregular word: *good* becomes *best*."), ("goodest", "Not a word.")],
          "Irregular superlative: *best*.", "Irregular comparison", "Recall", "What is the superlative of *good*?"),
        Q("Which sentence is correct?",
          "Her marks are better than her sister's.", [("Her marks are more better than her sister's.", "Double comparative."), ("Her marks are better than her sister.", "Marks compared with a person."), ("Her marks are best than her sister's.", "Superlative with *than*.")],
          "Compare like with like; no double comparison.", "Comparing correctly", "Application", "What is being compared?"),
        Q("'He is ______ a nurse nor a doctor; he is a pharmacist.'",
          "neither", [("either", "*Either* needs *or*."), ("both", "*Both* needs *and*."), ("not", "Does not pair with *nor*.")],
          "*Neither ... nor*.", "Correlative conjunctions", "Recall", "Which word pairs with *nor*?"),
        Q("Which sentence is parallel in structure?",
          "She enjoys swimming and dancing.", [("She enjoys swimming and to dance.", "A gerund and an infinitive are mixed."), ("She enjoys to swim and dancing.", "An infinitive and a gerund are mixed."), ("She enjoys swimming and she dances.", "A gerund and a clause are mixed.")],
          "Both objects are gerunds.", "Parallel structure", "Application", "Do both halves have the same form?"),
        Q("'It rained heavily; ______, the match went ahead.' Choose the conjunctive adverb of contrast.",
          "nevertheless", [("therefore", "Shows result."), ("moreover", "Adds information."), ("consequently", "Shows result.")],
          "A match going ahead despite rain is a contrast: *nevertheless*.", "Conjunctions by meaning", "Concept", "Contrast, result or addition?"),
        Q("Which sentence is correct?",
          "Mount Cameroon is higher than any other mountain in the country.", [("Mount Cameroon is higher than any mountain in the country.", "It must exclude itself: *any other*."), ("Mount Cameroon is more higher than any other mountain in the country.", "Double comparative."), ("Mount Cameroon is highest than any other mountain in the country.", "Superlative with *than*.")],
          "Add *other* when the item belongs to the group.", "Comparisons", "Reasoning", "Does the item belong to the group it is compared with?"),
        Q("Which sentence is correct?",
          "Not only did she pass, but she also won a scholarship.", [("Not only she passed, but she also won a scholarship.", "After *not only* at the start, the auxiliary comes first."), ("Not only did she passed, but she also won a scholarship.", "After *did*, the base form *pass* is used."), ("Not only she did pass, but she also won a scholarship.", "Subject and auxiliary are in the wrong order.")],
          "Inversion: auxiliary + subject + base verb.", "Not only ... but also", "Analysis", "What happens to the word order after *Not only*?"),
    ]))

# ================================================================== 17. Word order
SETS.append(practice_set(
    module=M, topic=T_COMP, title="Word order in questions, tags and phrases",
    lesson="enl2-word-order",
    questions=[
        Q("Which question is correct?",
          "Where did she go yesterday?", [("Where she went yesterday?", "Needs an auxiliary and inversion."), ("Where did she went yesterday?", "After *did* the base form is used."), ("Where went she yesterday?", "Needs *did*.")],
          "Wh-word + auxiliary + subject + base verb.", "Questions", "Recall", "What follows *did*?"),
        Q("Which subject question is correctly formed?",
          "Which student won the prize?", [("Which student did won the prize?", "After *did* the base form is needed, and a subject question takes no *did*."), ("Which student the prize won?", "Wrong order."), ("Which won student the prize?", "Wrong order.")],
          "The question phrase is the subject, so the order is subject + verb + object.", "Subject questions", "Recall", "Is the question word the subject?"),
        Q("'Could you tell me ______?'",
          "where the bank is", [("where is the bank", "Indirect questions keep statement order."), ("where does the bank", "Incomplete."), ("that where the bank is", "*That* is not used with a question word.")],
          "Statement order after the polite opening.", "Indirect questions", "Application", "Is it a direct or an indirect question?"),
        Q("'She can swim, ______?'",
          "can't she", [("does she", "A positive statement needs a negative tag."), ("isn't she", "Wrong auxiliary."), ("can she", "A positive statement needs a negative tag.")],
          "Repeat *can*, reverse the polarity.", "Question tags", "Recall", "Positive statement, so negative tag."),
        Q("'Nobody phoned, ______?'",
          "did they", [("didn't they", "*Nobody* makes the statement negative; the tag is positive."), ("did he", "Use *they* after *nobody*."), ("didn't he", "Wrong polarity and pronoun.")],
          "Negative in meaning: positive tag with *they*.", "Question tags", "Application", "Is *nobody* positive or negative?"),
        Q("Which phrase has the adjectives in the correct order?",
          "a lovely old wooden chair", [("a wooden old lovely chair", "Opinion should come first and material last."), ("an old lovely wooden chair", "Opinion comes before age."), ("a wooden lovely old chair", "Material should come last.")],
          "Opinion, age, material.", "Adjective order", "Application", "Which comes first, opinion or age?"),
        Q("Which sentence is correct?",
          "She is old enough to vote.", [("She is enough old to vote.", "*Enough* follows the adjective."), ("She enough is old to vote.", "Wrong position."), ("She is old to vote enough.", "Wrong position.")],
          "Adjective + enough.", "Enough", "Recall", "Where does *enough* go with an adjective?"),
        Q("Which sentence has the adverb correctly placed?",
          "He always arrives late.", [("He arrives always late.", "Frequency adverbs go before the main verb."), ("Always he arrives late.", "Not the normal position."), ("He arrives late always.", "Not the normal position.")],
          "Before the main verb.", "Adverb position", "Analysis", "Where do frequency adverbs go?"),
    ]))

# ================================================================== 18. Word forms
SETS.append(practice_set(
    module=M, topic=T_FORMS, title="Word forms: noun, verb, adjective, adverb",
    lesson="enl2-word-forms",
    questions=[
        Q("'Her ______ (decide) to resign surprised everyone.'",
          "decision", [("decisive", "An adjective; a noun is needed after *Her*."), ("decisively", "An adverb."), ("decided", "A verb form.")],
          "A noun after the possessive *Her*.", "Noun forms", "Recall", "What part of speech follows *her* and precedes the verb?"),
        Q("'The driver drove very ______ (care).'",
          "carefully", [("careful", "An adjective cannot modify the verb."), ("care", "A noun."), ("careless", "Wrong meaning and part of speech.")],
          "An adverb modifies the verb *drove*.", "Adverb forms", "Recall", "What does the gap describe?"),
        Q("'He is a ______ (success) farmer.'",
          "successful", [("success", "A noun."), ("successfully", "An adverb."), ("succeed", "A verb.")],
          "An adjective before the noun *farmer*.", "Adjective forms", "Recall", "What follows the gap?"),
        Q("'She sang so ______ that everyone applauded.'",
          "well", [("good", "An adjective; the verb needs an adverb."), ("goodly", "Not the standard adverb."), ("best", "Superlative, wrong meaning.")],
          "Adverb of *good*: *well*.", "Good v well", "Application", "What does the gap describe?"),
        Q("'There were ______ any students in the hall; it was almost empty.'",
          "hardly", [("hard", "Means with effort."), ("hardy", "Means tough."), ("harder", "A comparative.")],
          "*Hardly any* = almost none.", "Hard v hardly", "Application", "What does the sentence mean?"),
        Q("Which is the correct plural?",
          "criteria", [("criterions", "The irregular plural is needed."), ("criterias", "No such form."), ("criterion", "This is the singular.")],
          "criterion → criteria.", "Irregular plurals", "Recall", "What is the Latin plural?"),
        Q("'The report has been ______ (write) by the committee.'",
          "written", [("wrote", "The past participle is needed after *been*."), ("writing", "Present participle."), ("writ", "Not standard.")],
          "Past participle of *write*.", "Past participles", "Application", "What follows *has been*?"),
        Q("'The ______ (economy) of the region improved last year, and a number of ______ experts agreed.'",
          "economy ... economic", [("economic ... economy", "The forms are reversed."), ("economical ... economics", "Wrong forms."), ("economically ... economy", "Wrong parts of speech.")],
          "First gap: noun after *The*; second: adjective before *experts*.", "Word families", "Analysis", "Name the part of speech of each gap."),
    ]))

# ================================================================== 19. Punctuation
SETS.append(practice_set(
    module=M, topic=T_PUNCT, title="Punctuation: commas, apostrophes, semicolons, speech",
    lesson="enl2-punctuation",
    questions=[
        Q("Which sentence is correctly punctuated?",
          "When the rain stopped, we went outside.", [("When the rain stopped we, went outside.", "The comma is in the wrong place."), ("When, the rain stopped we went outside.", "The comma is in the wrong place."), ("When the rain stopped we went outside,.", "Misplaced punctuation.")],
          "Comma after the introductory clause.", "Commas", "Recall", "Where does the introductory clause end?"),
        Q("Choose the correct sentence.",
          "The dog wagged its tail.", [("The dog wagged it's tail.", "*It's* means *it is*."), ("The dog wagged its' tail.", "No such form."), ("The dog wagged its tail's.", "No such form.")],
          "Possessive *its* has no apostrophe.", "Its v it's", "Recall", "Does *it is* fit?"),
        Q("Which is correct for several girls who own the room?",
          "the girls' room", [("the girl's room", "That is one girl."), ("the girls room", "Missing the apostrophe."), ("the girls's room", "Not standard.")],
          "Plural possessive: girls'.", "Apostrophes", "Application", "How many girls?"),
        Q("Which is correct?",
          "the children's playground", [("the childrens playground", "Missing the apostrophe."), ("the childrens' playground", "Wrong placement."), ("the children playground", "Missing the possessive.")],
          "Irregular plural: children's.", "Apostrophes", "Application", "Does the plural end in -s?"),
        Q("Which sentence is correctly punctuated?",
          "'Where are you going?' she asked.", [("'Where are you going,' she asked?", "A direct question takes its question mark inside."), ("'Where are you going.' she asked.", "A full stop cannot replace the question mark."), ("Where are you going? she asked.", "Quotation marks are missing.")],
          "Question mark inside the closing mark; lowercase *she asked*.", "Direct speech", "Application", "Is the spoken part a question?"),
        Q("Which sentence uses a colon correctly?",
          "She bought three things: rice, oil and salt.", [("She bought: rice, oil and salt.", "A colon should follow a complete clause."), ("She bought three things, rice: oil and salt.", "Misplaced."), ("She: bought three things rice, oil and salt.", "Misplaced.")],
          "Complete clause before the colon.", "Colon", "Concept", "Is the clause before the colon complete?"),
        Q("Which is the correct form with hyphens?",
          "a ten-year-old boy", [("a ten year-old boy", "Hyphen misplaced."), ("a ten-year old boy", "Hyphen misplaced."), ("a ten year old boy", "Hyphens needed for the compound modifier.")],
          "Compound modifier before a noun is hyphenated.", "Hyphens", "Concept", "Which words together modify *boy*?"),
        Q("Which sentence has an error in punctuation?",
          "The students of this school, are clever.", [("The students of this school are clever.", "Correct."), ("My brother, who is a pilot, lives in Garoua.", "Correct."), ("We bought rice, beans and oil.", "Correct.")],
          "A comma must not separate subject and verb.", "Error spotting", "Analysis", "Check each comma."),
    ]))
