"""Practice sets for A Level English Language, Lower Sixth: Vocabulary, Composition and Examination (Paper 1).

All passages and examples are original and invented for teaching. IPA is British Received Pronunciation (RP).
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "lower-sixth")

M_V = "Vocabulary"
M_C = "Composition"
M_X = "Examination"
T_CHOICE = "Word choice, redundancy and malapropism"
T_CONN = "Connotation and figures of speech"
T_AFF = "Affixes and word formation"
T_SYN = "Synonyms, antonyms, homonyms and homophones"
T_CONF = "Words often confused"
T_IDIOM = "Idioms and figurative expressions"
T_SPELL = "Spelling"
T_NARR = "Narrative essays"
T_DESC = "Descriptive essays"
T_EXPO = "Expository and discursive essays"
T_ARG = "Argumentative essays"
T_OPEN = "Open-ended titles"
T_VIS = "Responding to visual stimuli"
T_ASSESS = "How a composition is assessed"
T_P1 = "Paper 1"

POS = [1, 3, 0, 2, 2, 0, 3, 1]  # where the right option sits in a topic set (spread over A-D)


def Q(prompt, right, wrongs, whys, step, concept, skill, hint, pos, feedback="", passage="", diagram="", diagram_alt=""):
    """4-option multiple choice. `right` is the correct text, `wrongs` three wrong texts with one `why` each,
    `pos` (0-3) the place of the right option. `passage` is repeated in full in front of the question."""
    opts = list(wrongs)
    opts.insert(pos, right)
    ws = list(whys)
    ws.insert(pos, "")
    choices = [C(o, correct=(i == pos), why=ws[i]) for i, o in enumerate(opts)]
    steps = [S("Reasoning", text=s) for s in ([step] if isinstance(step, str) else step)]
    text = (passage + "\n\n" + prompt) if passage else prompt
    return MC(text, choices, steps, concept=concept, skill=skill, hint=hint, feedback=feedback, diagram=diagram, diagram_alt=diagram_alt)


SETS = []

# ================================================================== V1. Word choice
SETS.append(practice_set(
    module=M_V, topic=T_CHOICE, title="Word choice: register, redundancy and malapropisms",
    lesson="enl3-word-choice-redundancy-malapropism",
    questions=[
        Q("Which sentence contains a redundant phrase?",
          "The old man returned back to his village.",
          ["The old man returned to his village.", "The old man walked slowly to his village.", "The old man left his village early."],
          ["No repeated meaning.", "'Slowly' adds new information.", "'Early' adds new information."],
          "'Returned' already means 'went back', so 'back' repeats it.", "Redundancy", "Recall", "Look for a word that repeats the meaning of another.", POS[0]),
        Q("Which word is most appropriate in a formal letter to a school principal? 'I wish to ______ for a place in Lower Sixth.'",
          "apply", ["beg", "scrap", "chase"],
          ["Too emotional and humble for a formal request.", "Slang or wrong in meaning.", "Informal and wrong in meaning."],
          "'Apply for' is the standard formal phrase for requesting a place.", "Register", "Application", "Which verb would you find on an application form?", POS[1]),
        Q("In 'The company gave every customer a free gift', which word is redundant?",
          "free", ["company", "every", "customer"],
          ["Needed: it names who gave the gift.", "Needed: it shows all customers got one.", "Needed: it names who received it."],
          "A gift is something given without payment, so 'free' adds nothing.", "Redundancy", "Concept", "Ask: can a gift cost money to the receiver?", POS[2]),
        Q("'The principal praised her for being so conscience.' Which word should replace 'conscience'?",
          "conscientious", ["conscious", "consciously", "constant"],
          ["'Conscious' means awake or aware, not careful and hard-working.", "An adverb cannot follow 'so' here to describe a person.", "'Constant' means unchanging; it does not mean careful."],
          "The sentence needs an adjective meaning careful and hard-working: conscientious. 'Conscience' (a noun) is a malapropism here.", "Malapropism", "Application", "You need an adjective that describes a hard-working person.", POS[3]),
        Q("Which sentence is written in the most formal register?",
          "The committee has decided to postpone the meeting.", ["The committee has called off the meeting.", "The guys in charge put the meeting off.", "They have scrapped the meeting, apparently."],
          ["Acceptable but a phrasal verb; less formal than 'postpone'.", "'Guys' and 'put off' are informal.", "'Scrapped' and 'apparently' make it casual and uncertain."],
          "'Postpone' and 'decided' belong to formal writing.", "Register", "Concept", "Pick the sentence with no phrasal verbs or slang.", POS[4]),
        Q("Which is the best way to rewrite 'Due to the fact that it rained, the match was cancelled'?",
          "Because it rained, the match was cancelled.", ["Due to the fact of rain, the match was cancelled.", "It rained, the match was cancelled.", "The match was cancelled, because of the fact that rain."],
          ["Still wordy and the grammar is clumsy.", "A comma splice; two sentences joined only by a comma.", "Wordy and ungrammatical."],
          "'Due to the fact that' is a wordy way to say 'because'.", "Wordy phrases", "Application", "Replace the long phrase by one short linking word.", POS[5]),
        Q("A student writes: 'My grandmother has a sedative life; she sits in her chair all day.' What is the error?",
          "A malapropism: 'sedative' should be 'sedentary'.", ["A spelling error: it should be 'sedetive'.", "A redundancy: 'all day' repeats 'sits'.", "A register error: 'sedative' is slang."],
          ["The spelling of 'sedative' is correct; the word is the wrong one.", "'All day' says how long; it does not repeat the meaning of 'sits'.", "'Sedative' is not slang; it is a medicine."],
          "'Sedative' is a real word (a calming medicine) used in place of 'sedentary' (sitting a lot). That is a malapropism.", "Malapropism", "Reasoning", "Which word means 'spending a lot of time sitting'?", POS[6]),
        Q("Which sentence is both correct and free of redundancy?",
          "The two leaders met to discuss the plan.", ["The two leaders met together to discuss the plan.", "The two leaders met to discuss about the plan.", "The two leaders met to discuss the plan again and repeat it."],
          ["'Met' already means 'came together'.", "'Discuss' is not followed by 'about'.", "'Again' and 'repeat' say the same thing and add nothing."],
          "The correct sentence has no repeated meaning and no extra preposition.", "Word choice", "Reasoning", "Check each option for a word that repeats a meaning or an unnecessary word.", POS[7]),
    ]))

# ================================================================== V2. Connotation and figures of speech
SETS.append(practice_set(
    module=M_V, topic=T_CONN, title="Connotation and figures of speech: identify and explain",
    lesson="enl3-connotation-figures-of-speech",
    questions=[
        Q("Which word has a positive connotation?",
          "thrifty", ["stingy", "miserly", "tight-fisted"],
          ["Negative: unwilling to spend.", "Negative: hoards money unkindly.", "Negative: informal for being mean."],
          "All four describe careful spending, but only 'thrifty' praises it.", "Connotation", "Recall", "Which word would the person be happy to hear?", POS[1]),
        Q("'The old lorry groaned up the hill.' Which figure of speech is this?",
          "Personification", ["Simile", "Hyperbole", "Alliteration"],
          ["There is no 'like' or 'as'.", "It does not exaggerate; it gives human sound to a machine.", "The sounds at the start of the words do not repeat."],
          "A lorry cannot groan as a person does, so it is personification.", "Figures of speech", "Recall", "Which figure gives human actions to a non-human thing?", POS[2]),
        Q("Which sentence contains a simile?",
          "The baby slept like a log.", ["The baby was an angel.", "The baby slept for a hundred years.", "The silence screamed in the room."],
          ["A metaphor: the baby IS an angel.", "Hyperbole: an exaggeration.", "Personification: silence cannot scream."],
          "'Like a log' compares the baby to a log using 'like'.", "Simile", "Recall", "Look for 'like' or 'as'.", POS[3]),
        Q("What is the best description of the effect of this hyperbole? 'The queue at the bank was a mile long.'",
          "It stresses that the queue was very long and tiring.", ["It gives exact information about the length.", "It shows that the writer likes queues.", "It compares the queue to a road."],
          ["Hyperbole is exaggeration, so it is not exact.", "Nothing in the sentence shows liking.", "That would be a metaphor or simile about a road; here it is an exaggeration."],
          "The writer exaggerates to stress the length and the discomfort.", "Hyperbole", "Interpretation", "Is 'a mile long' meant exactly?", POS[0]),
        Q("Which is a euphemism?",
          "He is between jobs.", ["He is out of work and desperate.", "He has no job at all.", "He lost his job and cried bitterly."],
          ["This is a plain, strong statement.", "This is a direct statement.", "This is a direct statement of events."],
          "'Between jobs' is a gentler way to say 'unemployed'.", "Euphemism", "Concept", "Which phrase softens an unpleasant fact?", POS[4]),
        Q("Which pair of words is an oxymoron?",
          "a cruel kindness", ["a kind heart", "a cold wind", "a loud noise"],
          ["Both words agree in feeling; no contradiction.", "Both words agree; the wind is cold.", "Both words agree; a noise is loud."],
          "'Cruel' and 'kindness' have opposite meanings, so the pair is an oxymoron.", "Oxymoron", "Concept", "Which pair contradicts itself?", POS[5]),
        Q("'The headmaster is a lion in the classroom.' What does this metaphor suggest?",
          "He is strong, fierce and commands respect.", ["He has a mane.", "He lives in the bush.", "He is a wild animal that should be feared by everybody in the school at all times."],
          ["The comparison is about character, not appearance.", "That is a literal reading; metaphors are not literal.", "Too extreme; the metaphor suggests authority, not that everyone must fear him constantly."],
          "A lion suggests strength and power; the metaphor shows the headmaster's authority.", "Metaphor", "Interpretation", "What qualities do we link with a lion?", POS[6]),
        Q("A writer says a hurricane destroyed a town and calls it 'a bit of rough weather'. Which figure is this?",
          "Understatement", ["Hyperbole", "Onomatopoeia", "Alliteration"],
          ["Hyperbole makes things sound bigger, not smaller.", "There is no word imitating a sound.", "There is no repeated starting sound."],
          "The writer makes a very serious event sound small: understatement.", "Understatement", "Application", "Does the phrase make the event sound bigger or smaller than it was?", POS[7]),
    ]))

# ================================================================== V3. Affixes and word formation
SETS.append(practice_set(
    module=M_V, topic=T_AFF, title="Affixes and word formation: prefixes, suffixes and new words",
    lesson="enl3-affixes-word-formation",
    questions=[
        Q("Which word is the opposite of 'legal'?",
          "illegal", ["unlegal", "inlegal", "dislegal"],
          ["'Unlegal' is not standard English.", "'Inlegal' is not standard; in- changes to il- before l.", "'Dislegal' is not standard English."],
          "Before l, the negative prefix in- becomes il-.", "Negative prefixes", "Recall", "The word starts with l.", POS[0]),
        Q("In the word 'hopelessness', what is the root?",
          "hope", ["hopeless", "less", "ness"],
          ["'Hopeless' is a longer word built on the root.", "'Less' is a suffix.", "'Ness' is a suffix."],
          "The root is the part with the core meaning: hope. Then -less and -ness are suffixes.", "Root and affixes", "Recall", "Remove the suffixes one at a time.", POS[1]),
        Q("Choose the correct form: 'The ______ between the two schools ended in a draw.' (compete)",
          "competition", ["compete", "competitive", "competitively"],
          ["A verb cannot follow 'The' and be the subject here.", "An adjective needs a noun after it; 'between' follows.", "An adverb cannot be the subject of the sentence."],
          "The gap needs a noun after 'The': competition.", "Word class", "Application", "What word class follows 'The'?", POS[2]),
        Q("Which spelling is correct?",
          "happiness", ["happyness", "hapiness", "happines"],
          ["Change y to i before -ness.", "The p must be doubled in happy; only y changes.", "The suffix is -ness with two s."],
          "Happy ends in consonant + y, so y becomes i: happiness.", "Spelling rule", "Recall", "What happens to y before a suffix?", POS[3]),
        Q("The word 'brunch' was formed by",
          "blending", ["clipping", "compounding", "conversion"],
          ["Clipping shortens one word; brunch joins parts of two.", "Compounding joins whole words (e.g. classroom).", "Conversion changes word class without changing the form."],
          "Brunch takes br- from breakfast and -unch from lunch.", "Word formation", "Concept", "Which process joins parts of two words?", POS[4]),
        Q("Which sentence uses conversion?",
          "We will email the form to you.", ["The exam was long.", "She is unhappy.", "He is a teacher."],
          ["'Exam' is a clipping, not conversion.", "'Unhappy' uses a prefix.", "'Teacher' uses a suffix."],
          "'Email' is a noun used as a verb with no change in form.", "Conversion", "Concept", "Which word changes word class without any change in spelling?", POS[5]),
        Q("Which pair of words are both correctly formed negatives?",
          "impossible, irregular", ["unpossible, unregular", "inpossible, inregular", "dispossible, disregular"],
          ["Neither word exists in standard English.", "Before p the prefix is im-; before r it is ir-.", "These words do not exist."],
          "Before p we write im-, before r we write ir-.", "Negative prefixes", "Application", "Check the first letter of each root.", POS[6]),
        Q("Which word was formed by back-formation from 'editor'?",
          "edit", ["editorial", "edition", "editing"],
          ["'Editorial' adds a suffix to 'editor'.", "'Edition' is an older word from Latin.", "'Editing' is the -ing form of 'edit'."],
          "The verb 'edit' was made by cutting what looks like a suffix (-or) from 'editor'.", "Back-formation", "Concept", "Which word is shorter than 'editor'?", POS[7]),
    ]))

# ================================================================== V4. Synonyms, antonyms, homonyms, homophones
SETS.append(practice_set(
    module=M_V, topic=T_SYN, title="Synonyms, antonyms and homophones in context",
    lesson="enl3-synonyms-antonyms-homonyms-homophones",
    questions=[
        Q("Choose the word closest in meaning to 'abundant' in 'Mangoes are abundant in June.'",
          "plentiful", ["rare", "sweet", "expensive"],
          ["The opposite of abundant.", "Taste is not part of the meaning.", "Price is not part of the meaning."],
          "'Abundant' means existing in large amounts, as 'plentiful' does.", "Synonyms", "Recall", "Mangoes in June: many or few?", POS[0]),
        Q("Choose the opposite of 'victory'.",
          "defeat", ["triumph", "success", "prize"],
          ["A synonym of victory.", "A synonym of victory.", "A reward, not the opposite."],
          "Victory is winning; the opposite is losing: defeat.", "Antonyms", "Recall", "What is the opposite of winning?", POS[1]),
        Q("Which word is a homophone of 'knew'?",
          "new", ["now", "know", "kneel"],
          ["Different vowel sound.", "'Know' is /nəʊ/, not /njuː/.", "Different ending sound."],
          "'Knew' and 'new' are both pronounced /njuː/ but spelt differently.", "Homophones", "Recall", "Which word sounds exactly the same as 'knew'?", POS[2]),
        Q("Which sentence uses the correct word? ",
          "The principal announced the results.", ["The principle announced the results.", "The principel announced the results.", "The principall announced the results."],
          ["'Principle' means a rule or belief; it cannot announce.", "Misspelling.", "Misspelling."],
          "The head of a school is the principal.", "Homophones", "Application", "Who announces results in a school?", POS[3]),
        Q("What kind of antonyms are 'buy' and 'sell'?",
          "Relational (they describe two sides of one action)", ["Gradable", "Complementary", "They are synonyms"],
          ["There is no scale between buy and sell.", "Complementary means one or the other; here both sides are one transaction.", "They have opposite directions."],
          "A buyer and a seller take part in the same event from opposite sides: relational antonyms.", "Types of antonym", "Concept", "Can one happen without the other?", POS[4]),
        Q("Choose the best synonym of 'obstinate' in 'The obstinate donkey refused to move.'",
          "stubborn", ["slow", "tired", "hungry"],
          ["Slowness is not refusing.", "Tiredness is a cause, not the meaning.", "Hunger is not the meaning."],
          "'Obstinate' means refusing to change one's mind or behaviour: stubborn.", "Synonyms", "Application", "What does it mean to refuse to move?", POS[5]),
        Q("Which pair are homonyms in the strict sense (same spelling and same sound, different meanings)?",
          "bat (the animal) and bat (for cricket)", ["plain and plane", "tail and tale", "hole and whole"],
          ["These sound alike but are spelt differently: homophones.", "These sound alike but are spelt differently: homophones.", "These sound alike but are spelt differently: homophones."],
          "Both words are spelt 'bat' and sound the same but mean different things. (Textbooks differ on the term; check your textbook.)", "Homonyms and homophones", "Concept", "Homonyms are spelt the same.", POS[6]),
        Q("Choose the best synonym of 'commence' in 'The committee will commence its meeting at nine.'",
          "start", ["finish", "cancel", "delay"],
          ["Opposite meaning.", "Not the meaning.", "Not the meaning."],
          "'Commence' is the formal word for 'begin' or 'start'.", "Synonyms", "Application", "Which word means 'begin'?", POS[7]),
    ]))

# ================================================================== V5. Words often confused
SETS.append(practice_set(
    module=M_V, topic=T_CONF, title="Words often confused: choose the right word",
    lesson="enl3-words-often-confused",
    questions=[
        Q("Choose the correct word: 'The doctor gave her sound ______ about diet.'",
          "advice", ["advise", "advices", "adviced"],
          ["'Advise' is the verb; a noun is needed after 'sound'.", "'Advice' is uncountable and has no plural.", "Not a word."],
          "After the adjective 'sound' we need the noun: advice.", "advice / advise", "Recall", "Is the gap a noun or a verb?", POS[0]),
        Q("Choose the correct word: 'Heavy rain will ______ the harvest.'",
          "affect", ["effect", "effects", "affects the"],
          ["'Effect' is normally a noun; a verb is needed after 'will'.", "A noun, and plural.", "Not a single word and wrongly adds an article."],
          "After 'will' we need a verb meaning influence: affect.", "affect / effect", "Application", "After 'will' which word class is needed?", POS[1]),
        Q("Which sentence is correct?",
          "Everyone passed except Paul.", ["Everyone passed accept Paul.", "Everyone passed expect Paul.", "Everyone passed exempt Paul."],
          ["'Accept' means receive.", "'Expect' means to think something will happen.", "'Exempt' means free from a duty."],
          "'Except' means 'apart from'.", "accept / except", "Recall", "Say the sentence with 'apart from'.", POS[2]),
        Q("Which sentence is correct in British English?",
          "She practises the violin every evening.", ["She practices the violin every evening.", "She practice the violin every evening.", "She practicing the violin every evening."],
          ["In British English the verb is spelt practise.", "The verb needs -s with 'she'.", "A finite verb is needed, not a bare -ing form."],
          "The verb is 'practise' in British English; the noun is 'practice'.", "practice / practise", "Application", "Is the gap a noun or a verb?", POS[3]),
        Q("Choose the correct word: 'This shirt is too ______; it keeps falling off me.'",
          "loose", ["lose", "loss", "loosen"],
          ["'Lose' is a verb meaning to misplace.", "'Loss' is a noun.", "'Loosen' is a verb."],
          "After 'too' we need an adjective meaning 'not tight': loose.", "lose / loose", "Application", "Which word is an adjective?", POS[0]),
        Q("Which sentence is correct?",
          "The cat licked its paws.", ["The cat licked it's paws.", "The cat licked its' paws.", "The cat licked their paws."],
          ["'It's' means 'it is'.", "A form with an apostrophe after the s does not exist in standard English.", "'Their' does not agree with the singular 'cat'."],
          "'Its' without an apostrophe is the possessive.", "its / it's", "Recall", "Can you replace the word with 'it is'?", POS[1]),
        Q("Choose the correct word: 'The school ______ spoke to us with calm and wise words and advised the troubled pupils.'",
          "counsellor", ["councillor", "consular", "conscience"],
          ["A councillor is a member of a council.", "Not a word for a person who gives advice.", "A sense of right and wrong."],
          "The person who gives advice is a counsellor; a councillor sits on a council.", "council / counsel", "Reasoning", "Who gives advice?", POS[2]),
        Q("Which sentence is correct?",
          "There are fewer pupils in the class than last year.", ["There are less pupils in the class than last year.", "There are fewer pupils in the class then last year.", "There are less pupils in the class then last year."],
          ["Pupils can be counted: fewer.", "'Then' is time; comparison needs 'than'.", "Two errors: 'less' and 'then'."],
          "Countable nouns take 'fewer'; comparison takes 'than'.", "fewer / less", "Reasoning", "Can you count pupils?", POS[3]),
    ]))

# ================================================================== V6. Idioms
SETS.append(practice_set(
    module=M_V, topic=T_IDIOM, title="Idioms and proverbs: meaning and use",
    lesson="enl3-idioms-figurative-expressions",
    questions=[
        Q("What does 'a piece of cake' mean in 'The test was a piece of cake'?",
          "very easy", ["very sweet", "very long", "very difficult"],
          ["Taken literally.", "Not suggested by the idiom.", "The opposite meaning."],
          "The idiom means something is very easy to do.", "Idioms", "Recall", "Do you find eating cake hard?", POS[0]),
        Q("What does it mean to 'let the cat out of the bag'?",
          "to reveal a secret by mistake", ["to free a pet", "to carry a bag", "to make a loud noise"],
          ["Literal reading.", "Literal reading.", "Not suggested by the idiom."],
          "A secret was hidden 'in the bag' and was accidentally revealed.", "Idioms", "Recall", "What is hidden in a bag until it is let out?", POS[1]),
        Q("Choose the idiom that completes the sentence: 'He rarely visits; he comes only once in a ______.'",
          "blue moon", ["red sun", "full day", "long time ago"],
          ["Wrong colour and body; not the idiom.", "Not the idiom.", "Not the idiom."],
          "'Once in a blue moon' means very rarely.", "Idioms", "Application", "Which colour and which heavenly body make a rare event?", POS[2]),
        Q("Which sentence uses an idiom correctly?",
          "The new phone cost an arm and a leg.", ["The new phone cost a hand and a leg.", "The new phone cost two arms and a leg.", "The new phone cost an arm and a foot."],
          ["The wording is changed.", "The wording is changed.", "The wording is changed."],
          "The fixed idiom is 'cost an arm and a leg' (very expensive).", "Fixed wording", "Concept", "Idioms cannot change their words.", POS[3]),
        Q("'Don't count your chickens before they hatch' warns us not to",
          "rely on a success that has not happened yet", ["buy poultry", "ignore small problems", "work too hard"],
          ["Literal reading.", "That is 'a stitch in time saves nine'.", "Not the meaning."],
          "The chickens stand for expected successes; counting them early is overconfident.", "Proverbs", "Concept", "What are the 'chickens' in the picture?", POS[0]),
        Q("What is wrong with this sentence? 'We must nip this problem in the bud before it opens the floodgates and takes root.'",
          "It mixes metaphors (plants and water).", ["It has a spelling error.", "It uses a proverb.", "It is too short."],
          ["The spelling is correct.", "It uses idioms, but the problem is mixing images.", "Length is not the issue."],
          "Plants (bud, take root) and flooding (floodgates) are different pictures; mixing them confuses the reader.", "Mixed metaphor", "Reasoning", "Count the different pictures.", POS[1]),
        Q("What is the best meaning of 'burn the midnight oil'?",
          "work late at night", ["waste money", "start a fire", "sleep deeply"],
          ["Not suggested.", "Literal reading.", "Opposite of working late."],
          "The phrase comes from lamps burning oil at night to work or study.", "Idioms", "Recall", "What kind of person is awake at midnight with a lamp?", POS[2]),
        Q("A student writes in a formal letter: 'I have been under the weather, so I could not attend.' What is the best comment?",
          "The idiom is understood but is informal; 'unwell' is safer in a formal letter.", ["The idiom is wrong because it talks about weather.", "The idiom is perfect for any formal letter.", "The sentence has no verb."],
          ["It is a real idiom that means slightly ill.", "It is informal.", "'Have been' is the verb."],
          "'Under the weather' is correct but conversational; formal writing prefers plain words.", "Register of idioms", "Reasoning", "Think about the reader of a formal letter.", POS[3]),
    ]))

# ================================================================== V7. Spelling
SETS.append(practice_set(
    module=M_V, topic=T_SPELL, title="Spelling: rules and commonly misspelt words",
    lesson="enl3-spelling",
    questions=[
        Q("Which word is spelt correctly?",
          "receive", ["recieve", "receeve", "riceive"],
          ["After c the rule gives ei.", "The vowel group is ei, not ee.", "The first vowel is e."],
          "'I before e except after c': rec-ei-ve.", "ie / ei", "Recall", "What follows the letter c?", POS[0]),
        Q("Which is the correct plural of 'baby'?",
          "babies", ["babys", "babyes", "babis"],
          ["Consonant + y: change y to i.", "Do not add es to y.", "The ending is ies."],
          "Consonant + y changes to ies.", "Plurals", "Recall", "What comes before the y?", POS[1]),
        Q("Which word is misspelt?",
          "goverment", ["government", "environment", "argument"],
          ["Spelt correctly.", "Spelt correctly.", "Spelt correctly."],
          "'Government' has an n before the m (govern + ment).", "Commonly misspelt words", "Recall", "Look for a missing letter.", POS[2]),
        Q("Add -ed to 'occur'.",
          "occurred", ["occured", "occurd", "occurrd"],
          ["The final r must be doubled because the stress is on the last syllable.", "A letter is missing.", "Not a correct pattern."],
          "occur is stressed on the last syllable, so r is doubled: occurred.", "Doubling", "Application", "Say occur: which syllable is stressed?", POS[3]),
        Q("Which sentence is spelt in British English?",
          "The neighbours admired the colour of the centre.", ["The neighbors admired the color of the center.", "The neighbours admired the color of the centre.", "The neighbors admired the colour of the center."],
          ["American spellings.", "Mixes British and American.", "Mixes American and British."],
          "British spelling uses -our and -re: neighbours, colour, centre.", "British spelling", "Application", "Which spelling uses -our and -re throughout?", POS[4]),
        Q("Which word is spelt correctly?",
          "necessary", ["neccessary", "necesary", "nesessary"],
          ["There is only one c before the double s.", "The s must be doubled.", "The first soft sound is spelt with c, not s."],
          "One c and two s: ne-c-e-ss-ary.", "Commonly misspelt words", "Recall", "Remember: one collar, two sleeves.", POS[5]),
        Q("Which is the correct form of 'hope' + 'ing'?",
          "hoping", ["hopeing", "hopping", "hopin"],
          ["The silent e is dropped before a vowel ending.", "'Hopping' is the form of 'hop', a different word.", "The ending -ing is incomplete."],
          "Drop the silent e before -ing: hoping.", "Silent e", "Application", "Drop or keep the e?", POS[6]),
        Q("Which of these sentences has all words spelt correctly?",
          "The committee will meet on Wednesday in February.", ["The comittee will meet on Wensday in Febuary.", "The committee will meet on Wednesday in Febuary.", "The commitee will meet on Wednesday in February."],
          ["Three words are misspelt.", "'February' is misspelt.", "'Committee' is misspelt."],
          "Committee has double m and double t and double e; Wednesday and February keep their silent letters.", "Commonly misspelt words", "Reasoning", "Check each tricky word in turn.", POS[7]),
    ]))

# ================================================================== C1. Narrative essays
SETS.append(practice_set(
    module=M_C, topic=T_NARR, title="Narrative essays: plot, openings, showing and dialogue",
    lesson="enl3-narrative-essays",
    questions=[
        Q("Which is the correct order of the parts of a narrative plot?",
          "Opening, complication, climax, resolution, ending", ["Climax, opening, ending, complication, resolution", "Opening, ending, complication, climax, resolution", "Complication, opening, resolution, climax, ending"],
          ["The climax comes after the problem has built up.", "The ending comes last.", "The story must be introduced before the complication."],
          "A story is introduced, a problem develops, reaches a peak, is settled, and closes.", "Plot", "Recall", "Where does a story begin?", POS[0]),
        Q("Which sentence shows rather than tells?",
          "Her hands shook so much that the cup rattled on the saucer.", ["She was very nervous.", "She felt terrible fear.", "She was a nervous person."],
          ["This tells.", "This tells.", "This tells about her character."],
          "Physical detail lets the reader feel the nervousness.", "Showing, not telling", "Application", "Which sentence uses a physical action?", POS[1]),
        Q("Which is correctly punctuated dialogue?",
          "\"Where are you going?\" asked Mama.", ["\"Where are you going\"? asked Mama.", "Where are you going? asked Mama.", "\"Where are you going?\" Asked Mama."],
          ["The question mark belongs inside the speech marks.", "Speech marks are missing.", "'Asked' should not have a capital letter after the question mark."],
          "The question mark goes inside the speech marks and the word after stays in lower case.", "Dialogue", "Application", "Where does the question mark go?", POS[2]),
        Q("A candidate writes a 350-word narrative essay. What will most likely happen?",
          "Marks are reduced in proportion because the essay is under 500 words.", ["Nothing; length is never assessed.", "The essay is not marked.", "Only the accuracy mark is lost."],
          ["The syllabus says there will be a proportionate deduction.", "It will be marked, with a deduction.", "The deduction applies to the essay's marks in proportion."],
          "The Board states that a composition under 500 words suffers a proportionate deduction.", "Length", "Concept", "What does the syllabus say about under 500 words?", POS[3]),
        Q("Which opening begins in the middle of the action?",
          "The engine coughed twice and died.", ["I would like to tell you about a day I remember.", "It was a Saturday and the weather was fine.", "My name is Ruth and I live in Kumba."],
          ["It announces the essay.", "It gives general, dull information.", "It gives identity details, which the Board says to conceal."],
          "A sound and a sudden event pull the reader into the story.", "Openings", "Application", "Which sentence starts with something happening?", POS[2]),
        Q("A student writes: 'I opened the door and I see a snake.' What is the fault?",
          "A shift of tense from past to present", ["A missing capital letter", "Wrong spelling of 'snake'", "Too much dialogue"],
          ["The capital is present.", "The spelling is correct.", "There is no dialogue."],
          "'Opened' is past, 'see' is present; it should be 'saw'.", "Tense consistency", "Concept", "Compare the two verbs.", POS[0]),
        Q("Under which heading does the Board assess 'logical arrangement of ideas and paragraphing'?",
          "Content and organisation", ["Expression", "Accuracy", "Identity"],
          ["Expression covers range, clarity and style of language.", "Accuracy covers syntax, spelling and punctuation.", "Identity is a rule, not a heading."],
          "Content and organisation (10 marks) covers relevance, creativity, logical arrangement and paragraphing.", "Assessment", "Recall", "Which heading is about ideas and structure?", POS[1]),
        Q("Which ending best suits a narrative essay?",
          "An image or idea that follows from the story and shows what changed", ["'Thank you for reading my story.'", "'And then I woke up and it was a dream.'", "A new, unrelated event in the last line"],
          ["It addresses the reader instead of closing the story.", "A weak, rushed ending.", "An unrelated event confuses the reader."],
          "A good ending completes the story and shows the change or lesson.", "Endings", "Reasoning", "What should the ending connect to?", POS[3]),
    ]))

# ================================================================== C2. Descriptive essays
SETS.append(practice_set(
    module=M_C, topic=T_DESC, title="Descriptive essays: senses, order and precise language",
    lesson="enl3-descriptive-essays",
    questions=[
        Q("The main aim of a descriptive essay is to",
          "help the reader see, hear and feel what something is like", ["tell what happened in time order", "persuade the reader to take action", "explain how to do something"],
          ["That is narrative.", "That is argumentative writing.", "That is expository (how-to) writing."],
          "Description appeals to the senses to show what a subject is like.", "Descriptive purpose", "Recall", "What question does description answer?", POS[0]),
        Q("Which sentence appeals to the sense of hearing?",
          "A radio crackled while a goat bleated beside it.", ["The cloth was bright red.", "The mango tasted sweet.", "The stool was smooth to touch."],
          ["Sight.", "Taste.", "Touch."],
          "Crackling and bleating are sounds.", "Senses", "Recall", "Which sentence has a sound word?", POS[1]),
        Q("Which is the most precise rewriting of 'The woman went along the road'?",
          "The woman trudged along the road.", ["The woman went along the road slowly and sadly.", "The woman went along the big road.", "The woman went very much along the road."],
          ["Adverbs are used but the verb is still vague.", "'Big' adds nothing to the action.", "'Very much' is meaningless here."],
          "An exact verb ('trudged') says how she moved in one word.", "Precise vocabulary", "Application", "Replace the vague verb.", POS[2]),
        Q("Which organising principle best suits the title 'The market from morning to night'?",
          "Time order", ["Alphabetical order", "Random order", "Order by price of goods"],
          ["Not a sensible principle for a description.", "A description needs an order.", "Not suggested by the title."],
          "The title names a span of time, so paragraphs follow the hours.", "Organising principle", "Application", "Which word in the title tells you the order?", POS[3]),
        Q("What is the 'dominant impression' of a descriptive essay?",
          "The main feeling or quality that all the details support", ["The longest sentence in the essay", "The title of the essay", "The conclusion only"],
          ["Length of sentence is not impression.", "The title only names the subject.", "It runs through the whole essay."],
          "Details are chosen to support one main feeling, such as busy, peaceful or eerie.", "Dominant impression", "Concept", "What should every detail support?", POS[0]),
        Q("Which is a metaphor?",
          "The crowd was a living river.", ["The crowd was like a river.", "The crowd moved as slowly as a river.", "The crowd was very large."],
          ["A simile ('like').", "A simile ('as...as').", "A plain statement."],
          "A metaphor says one thing is another without 'like' or 'as'.", "Figures of speech", "Concept", "Look for 'like' and 'as'.", POS[1]),
        Q("A candidate describes a village market but spends two paragraphs telling the story of a quarrel. What is the main risk?",
          "The essay may stop being a description and lose focus.", ["The essay will have too many senses.", "The essay will be too accurate.", "There is no risk because stories are better."],
          ["Senses are the strength of a description.", "Accuracy is a mark, not a risk.", "The title asks for description."],
          "Too much narrative weakens relevance to a descriptive title.", "Relevance", "Reasoning", "What does the title ask for?", POS[2]),
        Q("Which sentence is the best improvement of 'It was a nice big beautiful place'?",
          "Terraced green hills rolled to the river, and the air smelt of woodsmoke and wet earth.", ["It was a very nice, big and really beautiful place.", "The place was nice, with a great many beautiful things.", "It was beautiful."],
          ["A pile of vague adjectives.", "Vague words.", "Too short and tells without showing."],
          "Exact nouns and senses show the place instead of labelling it.", "Show, don't tell", "Reasoning", "Which sentence has exact details?", POS[3]),
    ]))

# ================================================================== C3. Expository and discursive essays
SETS.append(practice_set(
    module=M_C, topic=T_EXPO, title="Expository and discursive essays: titles, structure and paragraphs",
    lesson="enl3-expository-discursive-essays",
    questions=[
        Q("Which title is most clearly expository?",
          "Explain the causes of floods in towns.", ["Convince the mayor to build more bridges.", "Tell the story of the day of the flood.", "Describe a flooded street at night."],
          ["Argumentative.", "Narrative.", "Descriptive."],
          "'Explain the causes' asks you to make a subject clear.", "Reading the title", "Recall", "Which title asks you to explain?", POS[0]),
        Q("Which title asks for a discursive essay?",
          "Discuss the advantages and disadvantages of mobile money.", ["Describe a market in the rain.", "Narrate a visit to a relative.", "Write a letter asking for a job."],
          ["Descriptive.", "Narrative.", "A letter, not a discussion."],
          "'Advantages and disadvantages' means weighing two sides.", "Reading the title", "Recall", "Which words signal two sides?", POS[1]),
        Q("In the PEEL pattern, what does the second E stand for?",
          "Example", ["Ending", "Emotion", "Error"],
          ["Not part of the pattern.", "Not part of the pattern.", "Not part of the pattern."],
          "P: point, E: explanation, E: example, L: link.", "PEEL", "Recall", "Recite the pattern.", POS[2]),
        Q("Which sentence is the best topic sentence for a paragraph on the causes of poor results?",
          "A lack of regular revision is a major cause of poor results.", ["Results.", "I will now tell you about results.", "Many students fail."],
          ["A single word is not a sentence with a point.", "It announces instead of making a point.", "It states a fact but gives no cause to develop."],
          "A topic sentence states one clear point that the paragraph will develop.", "Topic sentence", "Application", "Which sentence names a cause?", POS[3]),
        Q("Which linking word shows contrast?",
          "however", ["moreover", "therefore", "for example"],
          ["Adds a point.", "Shows result.", "Gives an illustration."],
          "'However' introduces an opposing idea.", "Linking words", "Recall", "Which word signals 'but'?", POS[0]),
        Q("A candidate is asked to 'discuss both sides' of school uniforms but writes only in favour. What is the likely weakness?",
          "The essay is not relevant to the instruction and is unbalanced.", ["The essay is too accurate.", "The essay has too many paragraphs.", "The essay uses too many linking words."],
          ["Accuracy is a strength.", "Paragraphing is a strength.", "Linking words help."],
          "A discursive title requires both sides to be weighed.", "Balance", "Reasoning", "What does 'both sides' require?", POS[1]),
        Q("Which sentence has a suitable formal, balanced tone?",
          "Many people believe that homework improves results, although others claim that it causes stress.", ["Homework is rubbish and everybody hates it.", "Homework is the best thing ever.", "Teachers give homework to punish students."],
          ["Informal and one-sided.", "Informal and exaggerated.", "A sweeping, unsupported claim."],
          "It reports two views without sweeping words.", "Tone", "Application", "Which sentence avoids 'everybody' and slang?", POS[2]),
        Q("What should a conclusion in a discursive essay do?",
          "Sum up the main points and give a balanced judgement", ["Introduce a brand-new argument", "Repeat the introduction word for word", "Apologise for any mistakes"],
          ["A conclusion should not open new points.", "Repetition adds nothing.", "Apologies lower the quality."],
          "A conclusion gathers the discussion and judges on balance.", "Conclusion", "Concept", "Does a conclusion open or close the discussion?", POS[3]),
    ]))

# ================================================================== C4. Argumentative essays
SETS.append(practice_set(
    module=M_C, topic=T_ARG, title="Argumentative essays: thesis, evidence, counter-argument and rebuttal",
    lesson="enl3-argumentative-essays",
    questions=[
        Q("What is a thesis in an argumentative essay?",
          "A sentence stating your position on the issue", ["A list of examples", "The last word of the essay", "A quotation from a book"],
          ["Examples support the thesis.", "A thesis is a statement of position.", "A quotation is not required."],
          "The thesis is the position the whole essay defends.", "Thesis", "Recall", "What do you want the reader to believe?", POS[0]),
        Q("Which sentence is the best thesis for the title 'Schools should teach farming'?",
          "Schools should teach farming because it provides food, jobs and useful knowledge.", ["Farming is a topic.", "Some people like farming and some do not.", "I will now write about farming."],
          ["Names a topic but takes no position.", "Takes no side; this belongs in a discursive essay.", "Announces instead of arguing."],
          "A thesis takes a clear side and gives the main reasons.", "Thesis", "Application", "Which sentence takes a side?", POS[1]),
        Q("The purpose of a counter-argument is to",
          "show that you have considered the opposite view and can answer it", ["prove that you are wrong", "make the essay longer", "avoid taking a side"],
          ["It is answered, not accepted.", "Length is not the aim.", "The essay still takes a side."],
          "Dealing with the other side fairly strengthens your case.", "Counter-argument", "Concept", "What comes after the counter-argument?", POS[2]),
        Q("Which is an example of overgeneralisation?",
          "All politicians are dishonest.", ["Some politicians have been accused of dishonesty.", "Many people distrust politicians.", "Politicians sometimes break promises."],
          ["A careful, limited claim.", "A claim about opinion that is probably true.", "A limited claim."],
          "'All' claims too much and is easily shown false by one exception.", "Weak arguments", "Concept", "Look for 'all', 'everyone', 'never'.", POS[3]),
        Q("Which sentence is a rhetorical question?",
          "Can a country grow if its youth cannot work?", ["What time does the speech begin?", "Please pass the notes.", "How old are you?"],
          ["A real question needing an answer.", "A request.", "A real question."],
          "A rhetorical question is asked for effect, not for an answer.", "Persuasive language", "Recall", "Which question has an obvious answer?", POS[0]),
        Q("A candidate writing a speech for a school assembly signs with his own full name and address. What is wrong?",
          "It breaks the rule to conceal identity; he should use only the name and address given on the paper.", ["Nothing; examiners like to know the candidate.", "The speech has too many paragraphs.", "A speech may not have a signature."],
          ["The Board tells candidates to conceal identity.", "Paragraphs are not the issue.", "The issue is whose name is used."],
          "The syllabus says candidates should use the name and address provided to conceal their identity.", "Identity rule", "Reasoning", "Whose name should appear?", POS[1]),
        Q("Which is the best rebuttal to 'Practical subjects will take time from Mathematics'?",
          "A fair balance of two periods a week and links to existing subjects solves the timetable problem.", ["That is stupid.", "Mathematics is not important.", "Nobody cares about the timetable."],
          ["An insult, not an answer.", "An unsupported, extreme claim.", "Dismisses the point instead of answering."],
          "A rebuttal answers the point with a reasoned solution.", "Rebuttal", "Application", "Which answer offers a solution?", POS[2]),
        Q("Which structure is best for an argumentative essay of 550 words?",
          "Introduction with thesis, three reasons, counter-argument with rebuttal, conclusion", ["Introduction, one long paragraph, conclusion", "Conclusion, introduction, reasons", "A list of bullet points"],
          ["One paragraph lacks organisation.", "The order is illogical.", "The essay must be in continuous paragraphs."],
          "This structure gives content and organisation clear steps.", "Structure", "Concept", "Does the order move from claim to support to close?", POS[3]),
    ]))

# ================================================================== C5. Open-ended titles
SETS.append(practice_set(
    module=M_C, topic=T_OPEN, title="Open-ended titles: angle, form and relevance",
    lesson="enl3-open-ended-titles",
    questions=[
        Q("What makes an open-ended (one-word) title different from other composition titles?",
          "It does not tell you the form, so you choose the angle and the form.", ["It must be answered in one word.", "It must be answered as a letter.", "It carries extra marks."],
          ["The essay is still 500+ words.", "No form is imposed.", "The marks are the same 20."],
          "A one-word title leaves the choice of angle and form to the candidate.", "Open-ended titles", "Recall", "What is left open?", POS[0]),
        Q("What should you do first with the title 'Courage'?",
          "Brainstorm meanings, examples and images", ["Start the conclusion", "Write a definition from a dictionary", "Count 500 words of padding"],
          ["You cannot conclude before developing.", "A dictionary definition does not create an angle.", "Padding earns no credit."],
          "Brainstorming produces ideas and a specific angle.", "Method", "Application", "Where do ideas come from?", POS[1]),
        Q("Which is the most specific angle on the title 'Water'?",
          "The day our village borehole broke down", ["Water is important", "Water is a liquid", "Water in the world"],
          ["Too general.", "Too general and scientific.", "Too general."],
          "A specific event gives you characters, places and details.", "Choosing an angle", "Reasoning", "Which can be told with real details?", POS[2]),
        Q("A candidate writes a story, then half-way through starts lecturing on the importance of education. What is the weakness?",
          "The form changes and the essay loses unity.", ["The essay is too accurate.", "The essay is too short.", "The essay has no title."],
          ["Accuracy is not the issue.", "Length is not the issue described.", "The title is given."],
          "Keep one form to the end.", "Form", "Reasoning", "What changed half-way?", POS[3]),
        Q("Which sentence best keeps an essay on 'Bridge' relevant?",
          "Without the bridge, the children could not reach school.", ["The football match was exciting.", "My aunt sells beans.", "Last year the weather was dry."],
          ["Not linked to the bridge.", "Not linked to the bridge.", "Not linked to the bridge."],
          "The sentence ties the event to the title word.", "Relevance", "Application", "Which sentence mentions the word's role?", POS[0]),
        Q("Which of these is a valid way to answer the title 'Silence'?",
          "A narrative about the silence in a classroom while results are read", ["A paragraph of random words", "Only a list of synonyms", "A copy of a model essay"],
          ["Not an essay.", "Not an essay.", "Copying is not original work."],
          "A focused narrative is a valid answer.", "Choosing a form", "Concept", "Which is a real essay form?", POS[1]),
        Q("The assessment of an open-ended essay differs from other essays in that",
          "it uses the same headings: content and organisation 10, expression 8, accuracy 2", ["it is marked out of 10 only", "accuracy carries 10 marks", "only the title is marked"],
          ["All Section A compositions carry 20 marks.", "Accuracy is 2 marks.", "The whole essay is marked."],
          "The same three-part scheme applies to every composition.", "Assessment", "Recall", "Is there a special scheme?", POS[2]),
        Q("Which is the best way to end an essay on 'Home'?",
          "Return to the idea of home and say what it means to the writer", ["Introduce a new subject", "Stop in the middle of a sentence", "Ask the reader to mark it kindly"],
          ["A conclusion should not open a new subject.", "An unfinished essay loses marks.", "Appeals to the examiner do not earn marks."],
          "Returning to the word gives unity.", "Conclusion", "Reasoning", "What should the last paragraph connect to?", POS[3]),
    ]))

# ================================================================== C6. Responding to visual stimuli
SETS.append(practice_set(
    module=M_C, topic=T_VIS, title="Responding to pictures and cartoons",
    lesson="enl3-visual-stimuli",
    questions=[
        Q("What should an essay based on a picture do?",
          "Use the picture as a starting point and develop ideas from it", ["Ignore the picture", "Only list what is in the picture", "Copy the caption"],
          ["The essay would be irrelevant.", "A list is not an essay.", "The caption is only part of the stimulus."],
          "The picture sets the topic; the essay develops it.", "Visual stimuli", "Recall", "Is the picture a start or an end?", POS[0]),
        Q("In a cartoon, a tiny man standing in front of a huge pile of coins most likely suggests",
          "the difference between a person and great wealth or power", ["a banking lesson", "a fashion show", "a farming method"],
          ["Not suggested.", "Not suggested.", "Not suggested."],
          "Size contrast in cartoons often shows power or wealth against weakness.", "Symbols", "Interpretation", "What does the contrast of size suggest?", POS[1]),
        Q("A picture shows a crowded market in the rain with traders under umbrellas. Which form suits best?",
          "A descriptive essay using sound, smell and touch", ["A mathematical proof", "A recipe", "A list of prices only"],
          ["Not an essay form in this paper.", "Not suggested.", "Not an essay."],
          "A scene with many senses suits description.", "Choosing a form", "Application", "What does the picture mainly show?", POS[2]),
        Q("Which sentence uses a picture of a flooded road well in a narrative?",
          "The minibus stood helplessly in the brown water as the young man waded towards me.", ["There is a minibus. There is water. There is a man.", "I like the colour of the picture.", "The picture was drawn by an artist."],
          ["A list with no story.", "A comment on the picture, not a story.", "A comment on the picture, not a story."],
          "The picture details are woven into the narrative.", "Using details", "Application", "Which sentence tells the story?", POS[3]),
        Q("A candidate sees a picture of a hospital queue but writes about a football match. What is the main problem?",
          "The essay is not relevant to the picture.", ["The essay is too accurate.", "The essay is too long.", "The essay has too many paragraphs."],
          ["Accuracy is not a problem.", "Length is not the point.", "Paragraphing is not the point."],
          "An essay must be suggested by the picture.", "Relevance", "Reasoning", "What was the topic?", POS[0]),
        Q("Which is a good first step in reading a cartoon?",
          "Ask what the objects and characters stand for", ["Count the colours", "Copy it exactly", "Ignore the caption"],
          ["Colour count gives no message.", "Copying gives no essay.", "The caption can give the message."],
          "Cartoons use symbols; the symbols reveal the message.", "Cartoons", "Concept", "What do the objects represent?", POS[1]),
        Q("A cartoon shows a very long queue at a window marked 'Open 10-10.05'. The message is most likely that",
          "service is very limited and people suffer delays", ["service is excellent", "the queue is short", "nobody wants the service"],
          ["The picture shows the opposite.", "The queue is long.", "The queue shows that many people want it."],
          "Five minutes of service for a long queue is a protest against poor service.", "Cartoons", "Interpretation", "What does the long queue against a short opening time suggest?", POS[2]),
        Q("For which assessment heading do you gain credit by using accurate details from the picture?",
          "Content and organisation (relevance to the topic)", ["Accuracy only", "Identity", "Handwriting only"],
          ["Accuracy is about language correctness.", "Identity is a rule.", "Handwriting is not a heading."],
          "Relevance is part of content and organisation.", "Assessment", "Concept", "Which heading includes relevance to the topic?", POS[3]),
    ]))

# ================================================================== C7. How a composition is assessed
SETS.append(practice_set(
    module=M_C, topic=T_ASSESS, title="How a composition is assessed: headings, marks and rules",
    lesson="enl3-how-composition-is-assessed",
    questions=[
        Q("How is the 20-mark composition divided?",
          "Content and organisation 10, expression 8, accuracy 2", ["Content 5, expression 5, accuracy 10", "Content 8, expression 10, accuracy 2", "Content 10, expression 5, accuracy 5"],
          ["Accuracy is only 2 marks.", "Content and expression are the other way round.", "Accuracy is 2 marks, expression 8."],
          "The syllabus divides 20 marks as 10 + 8 + 2.", "Mark scheme", "Recall", "Which heading has the most marks?", POS[0]),
        Q("What is the minimum length stated in the syllabus?",
          "500 words", ["250 words", "350 words", "1,000 words"],
          ["That is the length of the creative writing answer.", "Not stated in the syllabus.", "Not required."],
          "The composition should not be less than 500 words.", "Length", "Recall", "Look at the rule on proportionate deduction.", POS[1]),
        Q("A candidate writes a 400-word composition. What is the likely result?",
          "A proportionate deduction of marks", ["The essay is rejected", "No penalty", "A bonus for being concise"],
          ["The essay is marked.", "The syllabus states a deduction.", "There is no bonus."],
          "Marks are reduced in proportion if the essay is under 500 words.", "Length", "Application", "Which word appears in the syllabus?", POS[2]),
        Q("Which belongs under 'expression'?",
          "Range and aptness of vocabulary", ["Logical arrangement of paragraphs", "Spelling of common words", "Relevance to the topic"],
          ["That is content and organisation.", "That is accuracy.", "That is content and organisation."],
          "Vocabulary and figurative language are expression criteria.", "Headings", "Concept", "Which heading is about words and style?", POS[3]),
        Q("Which belongs under 'accuracy'?",
          "Punctuation that helps the sense and common words spelt correctly", ["Imagination and freshness", "A sense of audience", "Suitable tone"],
          ["Content and organisation.", "Content and organisation.", "Expression."],
          "Accuracy covers sentence structure, spelling and punctuation.", "Headings", "Concept", "Which heading is about correct English?", POS[0]),
        Q("What should a candidate do about identity?",
          "Use the name and address provided on the paper", ["Write full name and school", "Write the examination number and town", "Sign with initials"],
          ["This reveals identity.", "This reveals identity.", "This reveals identity."],
          "The syllabus tells candidates to conceal their identity using the name and address provided.", "Rules", "Recall", "Whose name should be used?", POS[1]),
        Q("A well-written essay includes obscene words in a dialogue. What does the syllabus say?",
          "Candidates must not use obscene language.", ["It is fine if the characters speak that way.", "It earns more marks for realism.", "It is allowed in the conclusion only."],
          ["The syllabus forbids obscene language.", "The syllabus forbids obscene language.", "The syllabus forbids obscene language."],
          "No obscene language is allowed in the composition.", "Rules", "Application", "Is there an exception for dialogue?", POS[2]),
        Q("Which action best improves a draft essay's accuracy mark?",
          "Re-reading it for tense, agreement, spelling and punctuation errors", ["Adding more adjectives", "Making the handwriting larger", "Repeating the introduction"],
          ["Adjectives do not fix errors.", "Handwriting size does not fix errors.", "Repetition does not fix errors."],
          "Proofreading finds and fixes accuracy errors.", "Proofreading", "Application", "What do you do with a finished draft?", POS[3]),
    ]))

# ================================================================== X1. Paper 1 (exam lesson set)
SETS.append(practice_set(
    module=M_X, topic=T_P1, title="Paper 1 structure, timing and technique",
    lesson="enx-paper-1-english-language",
    questions=[
        Q("How many multiple-choice questions are there in Paper 1?",
          "50", ["40", "60", "100"],
          ["Not the number in the paper.", "Not the number in the paper.", "Not the number in the paper."],
          "Paper 1 has 50 questions: 10 + 10 + 20 + 10.", "Paper 1 structure", "Recall", "Add the section totals.", POS[0]),
        Q("Which section of Paper 1 is the largest?",
          "Section C: Grammar (20 questions)", ["Section A: Reading comprehension", "Section B: Speech work", "Section D: Vocabulary"],
          ["It has 10 questions.", "It has 10 questions.", "It has 10 questions."],
          "Grammar has 20 of the 50 questions.", "Paper 1 structure", "Recall", "Which section has 20 questions?", POS[1]),
        Q("What is the duration of Paper 1?",
          "1 hour 30 minutes", ["1 hour", "2 hours 15 minutes", "3 hours"],
          ["Too short.", "That is the duration of Paper 2 and Paper 3.", "Too long."],
          "Paper 1 lasts 1 hour 30 minutes.", "Paper 1 structure", "Recall", "Which papers last 2 hours 15 minutes?", POS[2]),
        Q("In reading comprehension, the best way to choose an answer is to",
          "find words in the passage that support the option", ["choose the option you like best", "choose the longest option", "use general knowledge only"],
          ["Preference is not evidence.", "Length is not evidence.", "Answers must come from the passage."],
          "Support from the passage proves the answer.", "Reading method", "Application", "Where must the proof be?", POS[3]),
        Q("A candidate has about 1 minute 48 seconds per question on average. What does this suggest about time?",
          "Some sections can be answered faster so that time remains for reading questions and checking.", ["Every question needs exactly that time.", "Checking is not needed.", "Reading questions need no time."],
          ["The time varies by question.", "Checking should be done.", "Reading questions often need more time."],
          "Average time hides differences between sections.", "Timing", "Reasoning", "Do all questions need the same time?", POS[0]),
        Q("In speech work, why is it risky to answer from spelling?",
          "English spelling does not always show the sound.", ["English spelling always shows the sound.", "Speech work has no questions.", "Spelling is irrelevant to every part of English."],
          ["Words such as 'one' and 'women' break the pattern.", "Speech work has 10 questions.", "Spelling matters in Section D."],
          "Spelling and sound often differ in English.", "Speech work method", "Concept", "Think of 'one' and 'women'.", POS[1]),
        Q("'The news ______ very bad.' Which option is correct and why?",
          "is, because 'news' is uncountable and takes a singular verb", ["are, because it ends in s", "were, because it is plural", "have, because it is plural"],
          ["Ending in s does not make it plural.", "'News' is not plural.", "'News' takes a singular verb."],
          "'News' is an uncountable noun and takes a singular verb.", "Grammar method", "Application", "Is 'news' countable?", POS[2]),
        Q("What should you do if you cannot decide between two options?",
          "Eliminate what you know is wrong, test the remaining options in the sentence, then choose", ["Leave it blank and never return", "Always choose B", "Choose the longest option"],
          ["Answer every question.", "A fixed letter has no basis.", "Length is not a clue."],
          "Elimination followed by testing improves the chance of being right.", "Elimination", "Reasoning", "What do you do with options you know are wrong?", POS[3]),
    ]))

PASS_A = (
    '**The Bicycle Library of Tiko** (an invented news article)\n\n'
    'Last Monday, forty children in the Mile Four quarter of Tiko arrived at school before the first bell. For many of them, this was a small miracle. Until recently, most of these pupils walked more than an hour each way, and they were often tired and late.\n\n'
    'The change began with a retired teacher, Mr Samuel Ekema, who noticed how many bicycles lay unused in people\'s yards. "A bicycle that rests in a corner is a wasted road," he told neighbours at a meeting. He proposed a "bicycle library": families would lend their spare bicycles to a shared store, and pupils could borrow one each school day and return it in the evening.\n\n'
    'The idea spread quickly. Within three months, the store held thirty-two bicycles, donated by families, a church group and two small businesses. A local mechanic, Mrs Lydia Nkeng, offered to repair the bicycles free of charge on Saturdays. Older pupils were trained to check brakes and tyres, and each borrower signs a book when taking and returning a bicycle.\n\n'
    'The results have been striking. Teachers at the nearby school say that late arrivals have fallen sharply, although they have not yet counted exactly. One head of department said that pupils who once slept in class now seem more alert. A mother, who asked not to be named, said, "My son used to leave at five in the morning. Now he leaves at seven and has time to eat."\n\n'
    'The scheme also has rules. A pupil who damages a bicycle through carelessness must help to repair it, and a pupil who misses three days in a month loses the right to borrow until a parent visits the store. Mr Ekema says that these rules are not meant to punish children but to teach them to look after what belongs to everyone. "A shared thing survives only when everyone treats it as their own," he says.\n\n'
    'Not everyone is satisfied. Some parents worry about accidents on the busy main road, and a few bicycles have been damaged. Mr Ekema admits that the library is not perfect, but he insists that it is a good start. A group of volunteers now plans to paint a safe lane along the edge of the road and to give pupils a short lesson on road safety before they borrow a bicycle.\n\n'
    'Meanwhile, representatives from two neighbouring towns have asked to visit. "We do not need a large budget," Mr Ekema says. "We need goodwill, a few tools and the patience to keep a record." If the idea works elsewhere, he believes, thousands of children could reach school in half the time.'
)

PASS_B = (
    '**A letter to the editor** (invented)\n\n'
    'The Editor, The Highland Courier, P.O. Box 90, Bamenda\n\n'
    'Dear Sir,\n\n'
    'I am writing about your recent article on whether secondary schools should require every student to take part in a sport. Having coached football and handball for eleven years, I feel that I must reply.\n\n'
    'Your writer claims that compulsory sport is a waste of time. I disagree strongly. The schools in my area that make sport compulsory report fewer cases of fainting during assembly and better attendance on Fridays. Of course, these schools also have better water supplies, so we cannot say that sport alone is the cause. Nevertheless, it would be foolish to ignore the benefits.\n\n'
    "First, regular exercise keeps the body strong. Students who sit for long hours need to move. Secondly, team sports teach cooperation. A girl who passes the ball to a rival in order to win learns more about trust than a lesson on trust could teach. Thirdly, sport gives shy students a place to shine. One of my former players, who hardly spoke in class, became the captain of the school's handball team and later a school prefect.\n\n"
    "Some parents object that sport takes time from study. This worry is understandable, and no responsible coach would ask students to neglect their books. But two hours of exercise a week, taken after the main lessons, can hardly ruin anyone's marks. In fact, tired minds often work better after a run in the sun.\n\n"
    'Another complaint is cost. It is true that balls and nets are expensive for poor schools. Still, a ball made of rolled cloth costs nothing, and many fine footballers began that way. A little imagination can overcome a small budget.\n\n'
    'A further worry concerns injuries. Anyone who has watched a crowded football pitch knows that a sprained ankle is possible. Yet a trained teacher who warms up the students, checks the ground and keeps a first-aid box close by can reduce this risk greatly. In my experience, the injuries I have seen came mostly from rough play on bare, stony ground, not from sport itself.\n\n'
    "Finally, let us not forget that sport is a joy. A school without games is a garden without flowers. I therefore urge the Ministry and school heads to make sport a part of every child's week.\n\n"
    'Yours faithfully,\n\n'
    'Daniel Fomum (an invented writer)'
)

# ================================================================== X2. Paper 1 mock exam A (50 questions)
MP = [0, 0, 1, 1, 2, 3, 1, 2, 0, 2, 2, 3, 3, 0, 1, 3, 0, 2, 0, 1, 2, 0, 1, 1, 2, 0, 3, 3, 2, 3, 3, 2, 3, 3, 0, 0, 1, 1, 0, 2, 1, 3, 1, 1, 0, 1, 2, 3, 2, 0]
_N = [0]

RC_MAIN = "Main ideas and supporting details"
RC_PURP = "Writer's purpose, point of view and attitude"
RC_INF = "Inference and deduction"
RC_WORDS = "Words and figures of speech in context"
RC_FACT = "Facts, opinions and sequence"
RC_DISC = "Discourse markers and cohesion"
RC_CRIT = "Critical reasoning and evaluation"
SP_SOUNDS = "English consonant and vowel sounds"
SP_TRANS = "Phonemic transcription"
SP_STRESS = "Word stress"
SP_SENT = "Sentence stress and intonation"
SP_CONN = "Connected speech and spelling of unknown words"
G_PARTS = "Parts of speech"
G_NOUNS = "Nouns and quantifiers"
G_VERBS = "Verbs: tense, mood, modals and voice"
G_REP = "Reported speech"
G_GER = "Gerunds, infinitives and participles"
G_PRON = "Pronouns and determiners"
G_SENT = "Sentence types"
G_AGR = "Agreement, fragments, run-on sentences and modifiers"
G_CLAUSE = "Clauses"
G_COMP = "Comparatives, conjunctions and word order"
G_FORMS = "Word forms"
G_PUNCT = "Punctuation"


def QM(prompt, right, wrongs, whys, step, concept, skill, hint, passage=""):
    """One mock question: the place of the right option comes from the list MP, in order."""
    pos = MP[_N[0]]
    _N[0] += 1
    return Q(prompt, right, wrongs, whys, step, concept, skill, hint, pos, passage=passage)


MOCK = [
    # ---- Section A: Reading comprehension (10)
    QM("What is the main idea of the passage?",
       "A community scheme of shared bicycles helps pupils reach school sooner, although it has some difficulties.",
       ["Mr Ekema wants to earn money by selling bicycles.", "Bicycles are the safest way to travel on busy roads.", "Mechanics in Tiko repair bicycles every day of the week."],
       ["Nothing in the passage says he sells bicycles; they are lent.", "The passage mentions worries about accidents on the main road.", "Mrs Nkeng repairs bicycles only on Saturdays, and this is one detail."],
       "The passage covers the idea, the rules, the results and the difficulties, so the correct option is the one that covers all of it.", RC_MAIN, "Concept", "Which option covers the whole passage, not one detail?", passage=PASS_A),
    QM("How many bicycles did the store hold after three months?",
       "thirty-two", ["forty", "thirty", "sixty"],
       ["Forty is the number of children who arrived early last Monday.", "Thirty is close but not the number given.", "Sixty is not mentioned."],
       "Paragraph 3 says that within three months the store held thirty-two bicycles.", RC_MAIN, "Recall", "Find the sentence about three months.", passage=PASS_A),
    QM("The writer's main purpose in the passage is to",
       "report on a local scheme and show both its benefits and its problems", ["persuade readers to buy bicycles", "warn readers never to cycle on main roads", "amuse readers with a funny story"],
       ["Nothing in the passage urges readers to buy anything.", "The road worry is one detail only, and a safe lane is planned.", "The tone is informative, not humorous."],
       "It is a news report with results and difficulties.", RC_PURP, "Interpretation", "Is the tone informative, persuasive or funny?", passage=PASS_A),
    QM("The mother's remark that her son 'used to leave at five in the morning' and 'now leaves at seven' suggests that",
       "the bicycle makes his journey to school much shorter in time", ["he now attends a different school", "she wants him to wake up later for no reason", "he no longer goes to school every day"],
       ["Nothing says he changed school.", "The remark is about the time saved, and she adds that he has time to eat.", "The passage says pupils now arrive early."],
       "He leaves two hours later and still arrives on time, so the bicycle saves a great deal of travelling time.", RC_INF, "Reasoning", "Why can he leave later and still arrive in time?", passage=PASS_A),
    QM("Mr Ekema says, 'A bicycle that rests in a corner is a wasted road.' This sentence is",
       "a metaphor meaning that an unused bicycle is a lost chance to travel", ["a simile because it uses like or as", "a literal statement about a road", "a euphemism for a broken bicycle"],
       ["There is no 'like' or 'as' in the sentence.", "A bicycle cannot literally be a road.", "It does not soften an unpleasant word."],
       "The bicycle is said to BE a wasted road: a metaphor for lost opportunity.", RC_WORDS, "Interpretation", "Look for 'like' or 'as' first.", passage=PASS_A),
    QM("Which of these statements from the letter is an opinion, not a fact?",
       "Sport teaches trust better than any lesson can.", ["The writer has coached football and handball for eleven years.", "The letter is addressed to the editor of The Highland Courier.", "Schools in the writer's area that require sport report better attendance on Fridays."],
       ["This is stated as a fact about the writer.", "This is stated as a fact in the address.", "This is a reported observation that can be checked."],
       "'Better than any lesson can' is a judgement that different people may disagree with.", RC_FACT, "Reasoning", "Which statement can people disagree about?", passage=PASS_B),
    QM("In 'Nevertheless, it would be foolish to ignore the benefits', the word 'Nevertheless' shows",
       "contrast with the point just made", ["cause and effect", "the addition of an unrelated point", "the end of the letter"],
       ["Nothing here is a result of the previous sentence.", "The sentence continues the same topic, but against the admission before it.", "The letter continues after this sentence."],
       "The writer admits that water supply may be a cause, then says, in spite of that, the benefits should not be ignored.", RC_DISC, "Concept", "What does the previous sentence admit?", passage=PASS_B),
    QM("The writer notes that schools which require sport also have better water supplies. What does this show about his argument?",
       "He admits that sport may not be the only cause of the benefits.", ["He has no experience of schools.", "He is attacking the editor personally.", "He proves that sport has no effect."],
       ["He says he has coached for eleven years.", "He criticises the article's claim, not the editor as a person.", "He only says other causes may also be at work."],
       "By admitting another possible cause, the writer weakens the certainty of his claim, but he also shows fairness.", RC_CRIT, "Reasoning", "What does 'we cannot say that sport alone is the cause' admit?", passage=PASS_B),
    QM("'A school without games is a garden without flowers.' This suggests that",
       "a school without games lacks colour and life", ["a school needs a real garden", "games are grown in gardens", "flowers are expensive for schools"],
       ["The comparison is figurative, not about gardening.", "The image is a metaphor, not a literal statement.", "Cost is not the point of the image."],
       "The writer compares a school without games to a garden without flowers: dull and lifeless.", RC_WORDS, "Interpretation", "Is the sentence literal or figurative?", passage=PASS_B),
    QM("From the story of the former player who hardly spoke in class, we can infer that the writer believes sport",
       "can help shy students gain confidence", ["is only for strong students", "should replace all lessons", "makes students talk too much"],
       ["The example shows a shy student succeeding.", "The writer says no coach would ask students to neglect their books.", "The example shows confidence, not too much talking."],
       "The former player became captain and prefect, which the writer offers as proof that sport gives shy students a chance to shine.", RC_INF, "Reasoning", "What does the example prove, in the writer's view?", passage=PASS_B),
    # ---- Section B: Speech work (10)
    QM("Which word has the same vowel sound as 'seat'?",
       "bead", ["bid", "bed", "bad"],
       ["'Bid' /bɪd/ has the short vowel /ɪ/.", "'Bed' /bed/ has /e/.", "'Bad' /bæd/ has /æ/."],
       "'Seat' /siːt/ and 'bead' /biːd/ both have the long vowel /iː/.", SP_SOUNDS, "Recall", "Is the vowel in 'seat' long or short?"),
    QM("Which word ends with the consonant sound /ŋ/?",
       "sing", ["sin", "sink", "sign"],
       ["'Sin' ends in /n/.", "'Sink' ends in /k/ after /ŋ/.", "'Sign' /saɪn/ ends in /n/."],
       "'Sing' is /sɪŋ/; the final sound is /ŋ/.", SP_SOUNDS, "Recall", "Which word ends in the sound of 'ng' alone?"),
    QM("Which is the correct phonemic transcription of 'cheap'?",
       "/tʃiːp/", ["/ʃiːp/", "/tʃɪp/", "/dʒiːp/"],
       ["That is 'sheep'.", "That is 'chip'.", "That is 'jeep'."],
       "'Cheap' begins with /tʃ/, has the long vowel /iː/ and ends with /p/.", SP_TRANS, "Application", "Which symbol is the first sound of 'church'?"),
    QM("Which word is transcribed /θɪŋk/?",
       "think", ["thing", "sink", "drink"],
       ["'Thing' is /θɪŋ/ and has no final /k/.", "'Sink' begins with /s/, not /θ/.", "'Drink' begins with /d/ and /r/."],
       "/θ/ + /ɪ/ + /ŋ/ + /k/ spells 'think'.", SP_TRANS, "Application", "Which symbol is the first sound of 'thin'?"),
    QM("Which word has the main stress on the second syllable?",
       "begin", ["teacher", "window", "mother"],
       ["Stress is on the first syllable: TEA-cher.", "Stress is on the first syllable: WIN-dow.", "Stress is on the first syllable: MOTH-er."],
       "'Begin' is /bɪˈɡɪn/, with the stress on -gin.", SP_STRESS, "Recall", "Say each word and listen for the strong syllable."),
    QM("In which sentence is 'present' stressed on the second syllable?",
       "They will present the prize tomorrow.", ["The present is on the table.", "She bought a present for her aunt.", "At present, he is out."],
       ["Here 'present' is a noun /ˈpreznt/.", "Here 'present' is a noun /ˈpreznt/.", "Here 'present' is a noun phrase meaning 'now', stressed on the first syllable."],
       "As a verb, 'present' is /prɪˈzent/ (stress on the second syllable); as a noun it is /ˈpreznt/.", SP_STRESS, "Application", "Is the word a verb or a noun in each sentence?"),
    QM("Which words are normally stressed in the sentence 'The boy bought three loaves of bread'?",
       "boy, bought, three, loaves, bread", ["The, of", "The, boy, of, bread", "all the words equally"],
       ["These are weak function words, normally unstressed.", "This leaves out the verb and the number.", "English stresses content words and weakens function words."],
       "Content words carry meaning and are stressed; 'the' and 'of' are weak.", SP_SENT, "Concept", "Which words carry the main meaning?"),
    QM("Which sentence would normally end with a falling tone in British English?",
       "What is your name?", ["Is it ready?", "Are you coming?", "Did he go?"],
       ["A yes/no question usually rises.", "A yes/no question usually rises.", "A yes/no question usually rises."],
       "Wh-questions normally fall; yes/no questions normally rise (check your textbook for exceptions).", SP_SENT, "Concept", "Is the question a wh-question or a yes/no question?"),
    QM("In fast speech 'a pair of shoes' is often said with 'of' as /əv/ or /ə/. This is an example of",
       "a weak form, with the vowel reduced to a schwa", ["a minimal pair", "a diphthong", "a silent letter"],
       ["A minimal pair is two words differing in one sound.", "A diphthong is a gliding vowel.", "No letter is silent here."],
       "Function words such as 'of' have weak forms in connected speech.", SP_CONN, "Concept", "What happens to small words in fast speech?"),
    QM("In the word 'nation', the sound /ʃ/ is spelt",
       "ti", ["sh", "ch", "ss"],
       ["'Sh' spells /ʃ/ in 'ship' but not here.", "'Ch' is another spelling of /ʃ/ in some words, not in 'nation'.", "'Ss' spells /ʃ/ in 'mission', not in 'nation'."],
       "The ending -tion is pronounced /ʃn/.", SP_CONN, "Recall", "Look at the letters before -on in 'nation'."),
    # ---- Section C: Grammar (20)
    QM("In 'She spoke softly', the word 'softly' is",
       "an adverb", ["an adjective", "a noun", "a preposition"],
       ["It describes how she spoke, not a noun.", "It is not the name of anything.", "It does not link a noun to the sentence."],
       "'Softly' tells how she spoke, so it is an adverb of manner.", G_PARTS, "Recall", "Does the word describe a verb or a noun?"),
    QM("In 'He ran quickly after the bus', the preposition is",
       "after", ["ran", "quickly", "bus"],
       ["'Ran' is a verb.", "'Quickly' is an adverb.", "'Bus' is a noun."],
       "'After' links 'the bus' to the verb and shows relationship.", G_PARTS, "Recall", "Which word links 'the bus' to the rest?"),
    QM("Which of these nouns is uncountable?",
       "advice", ["chair", "student", "idea"],
       ["You can say 'two chairs'.", "You can say 'two students'.", "You can say 'two ideas'."],
       "We do not say 'advices'; 'a piece of advice' is used.", G_NOUNS, "Recall", "Can you put a number before it?"),
    QM("There isn't ______ water in the tank.",
       "much", ["many", "few", "a few"],
       ["'Many' is used with countable nouns.", "'Few' is used with countable nouns.", "'A few' is used with countable nouns."],
       "'Water' is uncountable; 'much' is used with uncountable nouns in negatives.", G_NOUNS, "Application", "Is 'water' countable?"),
    QM("By the time we arrived, the film ______.",
       "had started", ["has started", "starts", "is starting"],
       ["The present perfect does not fit 'by the time we arrived' (past).", "The simple present does not fit a past reference.", "The present continuous does not fit a past reference."],
       "The film started before we arrived: past perfect.", G_VERBS, "Application", "Which happened first?"),
    QM("You ______ wear a seat belt; it is the law.",
       "must", ["might", "may", "could"],
       ["'Might' shows a small possibility, not obligation.", "'May' gives permission or possibility.", "'Could' shows possibility or ability, not obligation."],
       "'Must' expresses a strong obligation.", G_VERBS, "Application", "Is this a duty or a possibility?"),
    QM("Which is the passive form of 'The council built the bridge in 2019'?",
       "The bridge was built by the council in 2019.", ["The bridge is built by the council in 2019.", "The bridge has built by the council in 2019.", "The bridge was build by the council in 2019."],
       ["The tense changes to present.", "'Has built' is not a passive form here.", "'Build' should be the past participle 'built'."],
       "Passive: object + was/were + past participle + by + agent.", G_VERBS, "Application", "Keep the same tense as the original."),
    QM("Change to reported speech: He said, 'I am tired.'",
       "He said that he was tired.", ["He said that I am tired.", "He said that he be tired.", "He said me that he was tired."],
       ["The pronoun should change to 'he' and the verb to the past.", "'Be' is not the correct form.", "'Said' is not followed by a person without 'to'."],
       "In reported speech after a past reporting verb, 'am' becomes 'was' and 'I' becomes 'he'.", G_REP, "Application", "Change the pronoun and the tense."),
    QM("Change to reported speech: 'Where do you live?' she asked me.",
       "She asked me where I lived.", ["She asked me where did I live.", "She asked me where do I live.", "She asked me that where I lived."],
       ["A reported question has normal statement order, without 'did'.", "A reported question keeps statement order and moves the tense back.", "'That' is not used with a reported question."],
       "Use statement word order and move the tense back.", G_REP, "Application", "Is a reported question still a question in form?"),
    QM("She enjoys ______ stories to her little brother.",
       "reading", ["to read", "read", "to reading"],
       ["'Enjoy' is followed by a gerund, not an infinitive.", "'Read' is the base form and does not fit.", "'To reading' is not a correct form."],
       "'Enjoy' is followed by the -ing form (gerund).", G_GER, "Application", "Which verb form follows 'enjoy'?"),
    QM("Give the book to Peter and ______.",
       "me", ["I", "myself", "mine"],
       ["'I' is a subject pronoun; an object is needed.", "'Myself' is reflexive and needs 'I' as the subject.", "'Mine' is a possessive pronoun."],
       "After the preposition 'to' we use the object pronoun 'me'.", G_PRON, "Application", "Is the pronoun subject or object?"),
    QM("She is ______ honest girl.",
       "an", ["a", "any", "much"],
       ["'Honest' begins with a vowel sound (the h is silent).", "'Any' is not used with a singular countable noun here.", "'Much' is used with uncountable nouns."],
       "We use 'an' before a vowel sound: an honest girl.", G_PRON, "Recall", "Is the first sound of 'honest' a vowel or a consonant?"),
    QM("Which of these is a complex sentence?",
       "Although it rained, we played football.", ["We played football and it rained.", "We played football.", "Play football!"],
       ["Two main clauses joined by 'and': a compound sentence.", "One clause: a simple sentence.", "One clause: a simple (imperative) sentence."],
       "A complex sentence has a main clause and a subordinate clause: 'although it rained'.", G_SENT, "Concept", "Which sentence has a clause that cannot stand alone?"),
    QM("Each of the girls ______ a prize.",
       "has won", ["have won", "were winning", "are won"],
       ["'Each' takes a singular verb.", "The verb form and number do not fit.", "'Are won' is passive and plural, and does not fit."],
       "'Each' is singular, so the verb is 'has'.", G_AGR, "Application", "Is 'each' singular or plural?"),
    QM("Which is a complete, correct sentence?",
       "The road was flooded, so we stayed home.", ["Because the road was flooded.", "The road was flooded, we stayed home.", "Flooded road, stayed home."],
       ["A fragment: a subordinate clause alone.", "A comma splice: two sentences joined by a comma.", "A fragment without a proper subject and verb structure."],
       "A comma plus the conjunction 'so' correctly joins two main clauses.", G_AGR, "Application", "Which option has two complete clauses properly joined?"),
    QM("In 'The woman who sells plantains lives next door', the clause 'who sells plantains' is",
       "a relative clause", ["a main clause", "a noun clause", "an adverbial clause of time"],
       ["It cannot stand alone.", "It does not act as a noun.", "It does not tell when."],
       "It begins with 'who' and describes 'the woman': a relative clause.", G_CLAUSE, "Concept", "Which noun does the clause describe?"),
    QM("Of the three sisters, Ada is the ______.",
       "tallest", ["taller", "more tall", "most tall"],
       ["'Taller' compares two.", "'More tall' is not standard.", "'Most tall' is not standard."],
       "Three or more: superlative 'tallest'.", G_COMP, "Recall", "How many are being compared?"),
    QM("Which sentence has the correct word order?",
       "She always arrives early.", ["She arrives always early.", "She early arrives always.", "Arrives she always early."],
       ["The frequency adverb goes before the main verb.", "The order is unnatural in standard English.", "This is not a normal statement order."],
       "Frequency adverbs such as 'always' normally come before the main verb.", G_COMP, "Application", "Where does 'always' normally go?"),
    QM("The ______ of the bridge took two years.",
       "construction", ["construct", "constructive", "constructively"],
       ["'Construct' is a verb.", "'Constructive' is an adjective.", "'Constructively' is an adverb."],
       "After 'The' and before 'of' we need a noun: construction.", G_FORMS, "Application", "Which word class follows 'The'?"),
    QM("Which sentence is correctly punctuated?",
       "My sister, who lives in Douala, is a nurse.", ["My sister who lives, in Douala is a nurse.", "My sister, who lives in Douala is a nurse.", "My sister who lives in Douala, is a nurse."],
       ["The comma is in the wrong place.", "The second comma is missing.", "The first comma is missing."],
       "A non-defining clause is set off with a pair of commas.", G_PUNCT, "Application", "Does the clause add extra information?"),
    # ---- Section D: Vocabulary (10)
    QM("Which sentence has no redundancy?",
       "He returned the book.", ["He returned back the book.", "He repeated again the answer.", "He joined together the two ropes."],
       ["'Return' already means 'give back'.", "'Repeat' already means 'say again'.", "'Join' already means 'put together'."],
       "Only the sentence with a bare 'returned' has no repeated meaning.", T_CHOICE, "Application", "Which verb already contains the meaning of the extra word?"),
    QM("He is a very ______ worker; he never leaves a job half done.",
       "conscientious", ["conscious", "conscience", "consciously"],
       ["'Conscious' means aware or awake.", "'Conscience' is a noun, the sense of right and wrong.", "'Consciously' is an adverb."],
       "'Conscientious' means careful and hard-working.", T_CHOICE, "Application", "You need an adjective meaning careful."),
    QM("Which sentence contains personification?",
       "The wind whispered through the maize.", ["The wind was strong.", "The maize is as tall as a man.", "He ran as fast as the wind."],
       ["A plain statement.", "A simile.", "A simile."],
       "The wind is given the human action of whispering.", T_CONN, "Concept", "Which sentence gives a human action to a non-human thing?"),
    QM("Which word is the opposite of 'regular'?",
       "irregular", ["unregular", "inregular", "disregular"],
       ["'Unregular' is not standard.", "'In-' becomes 'ir-' before r.", "'Disregular' is not standard."],
       "Before r, the negative prefix is ir-: irregular.", T_AFF, "Recall", "Check the first letter of the root."),
    QM("Which word is a noun formed from an adjective by adding a suffix?",
       "kindness", ["unkind", "kindly", "kinder"],
       ["'Unkind' adds a prefix and remains an adjective.", "'Kindly' is an adverb.", "'Kinder' is a comparative adjective."],
       "Kind + -ness forms a noun.", T_AFF, "Concept", "Which suffix makes a noun?"),
    QM("Choose the word closest in meaning to 'scarce' in 'Fresh water was scarce in the dry season.'",
       "in short supply", ["plentiful", "dirty", "cold"],
       ["The opposite meaning.", "Not the meaning.", "Not the meaning."],
       "'Scarce' means not available in enough quantity.", T_SYN, "Application", "Is there much or little water in the dry season?"),
    QM("The new law will ______ everyone in the town.",
       "affect", ["effect", "effects", "affected"],
       ["'Effect' is normally a noun.", "A noun in the plural.", "The past form does not fit after 'will'."],
       "After 'will' we need the base verb 'affect' (to influence).", T_CONF, "Application", "After 'will' which word class is needed?"),
    QM("The ______ of the school welcomed the guests.",
       "principal", ["principle", "principel", "principally"],
       ["'Principle' means a rule or belief.", "A misspelling.", "An adverb."],
       "The head of a school is the principal.", T_CONF, "Application", "Who welcomes guests at a school?"),
    QM("'She spilled the beans' means that she",
       "revealed a secret", ["dropped her food", "cooked a meal", "made a loud noise"],
       ["Literal reading.", "Literal reading.", "Not the idiom's meaning."],
       "The idiom 'spill the beans' means to reveal a secret.", T_IDIOM, "Recall", "Is the phrase literal?"),
    QM("Which word is spelt correctly?",
       "separate", ["seperate", "separete", "seperete"],
       ["The second vowel is a, not e.", "The ending is -ate.", "Two errors."],
       "Remember: there is 'a rat' in sep-a-rate.", T_SPELL, "Recall", "Which vowel comes after the p?"),
]

SETS.append(practice_set(
    module=M_X, topic=T_P1, title="Paper 1 mock exam A",
    lesson="enx-paper-1-english-language",
    questions=MOCK, mock=True, time_limit_minutes=90))
