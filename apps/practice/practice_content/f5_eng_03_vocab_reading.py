"""Form 5 English Language: Vocabulary, Semantics & Register, and Reading Comprehension & Summary (practice sets, one per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "form-5")

M3 = "Vocabulary, Semantics & Register"
M4 = "Reading Comprehension & Summary"


import itertools

_POS = [2, 0, 3, 1, 1, 3, 0, 2]
_COUNT = itertools.count()


def Q(prompt, right, wrongs, pos, why_right, concept, skill, hint):
    """4-option MC. `wrongs` is three (text, why) pairs; the correct option goes at index `pos`."""
    pos = _POS[next(_COUNT) % 8]  # spread the correct option across A-D (the platform does not shuffle)
    opts = [C(t, why=w) for t, w in wrongs]
    opts.insert(pos, C(right, correct=True))
    return MC(prompt, opts, steps=[S("Reasoning", text=why_right)], concept=concept, skill=skill, hint=hint,
              feedback=why_right)


SETS = []

# ------------------------------------------------------------------ 1. Prefixes and suffixes
SETS.append(practice_set(
    module=M3, topic="Word formation", title="Prefixes, suffixes and roots", lesson="evo-prefixes-suffixes-roots",
    questions=[
        Q("In the word 'unhappy', 'un' is a", "prefix",
          [("suffix", "A suffix comes at the end of a word."), ("root", "The root is 'happy'."), ("compound", "A compound joins two whole words.")],
          0, "'Un' comes at the front of the root 'happy', so it is a prefix.", "Prefix", "Recall", "Where in the word does 'un' stand?"),
        Q("Which word correctly means 'not legal'?", "illegal",
          [("unlegal", "There is no such word."), ("inlegal", "In- becomes il- before the letter l."), ("dislegal", "Dis- does not form this word.")],
          1, "Before l, the prefix in- changes to il-: illegal.", "Prefix in- spelling", "Concept", "Look at the first letter of 'legal'."),
        Q("Adding the suffix -ness to 'kind' gives 'kindness'. The word class changes from", "adjective to noun",
          [("noun to adjective", "Kind is the adjective; kindness is the noun."), ("verb to noun", "Kind is not a verb."), ("adverb to adjective", "Kind is not an adverb.")],
          2, "The suffix -ness makes a noun from an adjective.", "Suffix and word class", "Concept", "Ask what class 'kind' is, and what class 'kindness' is."),
        Q("Choose the correct word. 'The ______ of the new bridge made the journey shorter.' (open)", "opening",
          [("opened", "This is the past tense and cannot follow 'The' as a noun."), ("openly", "An adverb cannot be the subject here."), ("openness", "It means being honest, not the action of opening.")],
          3, "A noun is needed after 'The'. 'Opening' names the action here.", "Choosing the word form", "Application", "The gap follows 'The' and is followed by 'of'. What class is needed?"),
        Q("Complete the sentence. 'Mama Rose drives very ______ on wet roads.' (care)", "carefully",
          [("careful", "An adjective describes a noun; here we need a word describing the verb 'drives'."), ("careless", "This has the opposite meaning."), ("care", "A noun does not fit here.")],
          0, "A word that describes how she drives is an adverb: care + ful + ly = carefully.", "Adverb suffix -ly", "Application", "Does the gap describe a noun or the verb 'drives'?"),
        Q("Which word is spelt correctly?", "happiness",
          [("happyness", "The y changes to i before -ness."), ("hapiness", "The word keeps two p's, from happy."), ("happines", "The suffix is -ness with two s's.")],
          1, "Happy + ness: change y to i, giving happiness.", "Spelling change y to i", "Recall", "What happens to the y when -ness is added?"),
        Q("Which prefix means 'again'?", "re-",
          [("mis-", "Mis- means wrongly."), ("pre-", "Pre- means before."), ("anti-", "Anti- means against.")],
          2, "Re- means again: rebuild means build again.", "Prefix meanings", "Recall", "Think of 'rewrite' and 'repay'."),
        Q("In which pair does the prefix make the word an opposite?", "kind / unkind",
          [("play / replay", "Replay means play again, not the opposite."), ("view / preview", "Preview means view before."), ("take / retake", "Retake means take again.")],
          3, "Un- makes the opposite of kind. The other prefixes add time or repetition.", "Prefixes and meaning", "Analysis", "Which pair shows a change to 'not'?"),
    ]))

# ------------------------------------------------------------------ 2. Compounds and conversion
SETS.append(practice_set(
    module=M3, topic="Word formation", title="Compounds, conversion, blends and clippings", lesson="evo-compounds-conversion",
    questions=[
        Q("Which of these is a compound noun?", "classroom",
          [("teacher", "This is a root plus a suffix, not two whole words."), ("unhappy", "This is a prefix plus a root."), ("quickly", "This is a root plus a suffix.")],
          0, "Class + room: two words joined.", "Compound words", "Recall", "Which word is made of two whole words?"),
        Q("Complete: 'She has a ______ daughter.'", "three-year-old",
          [("three-years-old", "The noun in a compound adjective stays singular."), ("three year old", "The hyphens are missing."), ("three years-old", "The hyphen is in the wrong place.")],
          1, "Before a noun, hyphens join the words and 'year' stays singular.", "Compound adjectives", "Application", "Before a noun, how is a number-year-old group written?"),
        Q("In 'Please book a seat for me', the word 'book' is a", "verb",
          [("noun", "A noun would name a thing, as in 'a book'."), ("adjective", "It does not describe anything here."), ("adverb", "It does not describe a verb here.")],
          2, "'Book a seat' is an action. This is conversion: the noun 'book' is used as a verb.", "Conversion", "Concept", "Does 'book' name a thing here, or tell what to do?"),
        Q("'Phone' is a shortened form of 'telephone'. This process is called", "clipping",
          [("blending", "Blending joins parts of two words."), ("conversion", "Conversion changes class without changing the word."), ("compounding", "Compounding joins two whole words.")],
          3, "Cutting a long word to make a short one is clipping.", "Clipping", "Recall", "What happened to the long word?"),
        Q("'Smog' comes from smoke and fog. This process is called", "blending",
          [("clipping", "Clipping shortens one word."), ("prefixing", "No prefix has been added."), ("conversion", "Conversion does not change the spelling.")],
          0, "Parts of two words are joined to make a new word: blending.", "Blending", "Recall", "Which two words does 'smog' come from?"),
        Q("Which sentence is correct?", "She is a hard-working student.",
          [("She is a hard working-student.", "The hyphen must join hard and working."), ("She is a hard-working-student.", "Only the adjective is hyphenated."), ("She is a hardworking, student.", "A comma is not needed here.")],
          1, "Before a noun, the compound adjective hard-working takes a hyphen.", "Hyphen in compound adjectives", "Application", "Which words work together as one adjective?"),
        Q("Which of these is said as a word (an acronym)?", "UNESCO",
          [("ATM", "People say the letters A-T-M."), ("GCE", "People say the letters G-C-E."), ("SIM", "In this course it is treated as an initialism; check your textbook.")],
          2, "UNESCO is pronounced as one word. (Textbooks differ on the terms; check your textbook.)", "Acronyms", "Recall", "Which one do you pronounce as a word, not letter by letter?"),
        Q("Which sentence uses 'text' as a verb?", "Please text me when you arrive.",
          [("I got a text from my sister.", "Here 'text' is a noun."), ("Read the text on page ten.", "Here 'text' is a noun."), ("The text was very long.", "Here 'text' is a noun.")],
          0, "'Text me' is an action, so 'text' is a verb.", "Conversion", "Analysis", "In which sentence does the word show an action?"),
    ]))

# ------------------------------------------------------------------ 3. Synonyms and antonyms
SETS.append(practice_set(
    module=M3, topic="Synonyms, antonyms and homonyms", title="Synonyms and antonyms", lesson="evo-synonyms-antonyms",
    questions=[
        Q("Which word is closest in meaning to 'furious'?", "very angry",
          [("amused", "Amused means finding something funny."), ("tired", "This is not about anger."), ("puzzled", "This means confused.")],
          0, "Furious means extremely angry.", "Synonym", "Recall", "Think about how the headmaster feels about a broken window."),
        Q("The antonym of 'ancient' is", "modern",
          [("old", "That is a synonym."), ("broken", "That is not an opposite."), ("early", "That is not the opposite either.")],
          1, "Ancient means very old; modern is the opposite.", "Antonym", "Recall", "What describes something new or recent?"),
        Q("'The boy was reluctant to speak.' Reluctant means", "unwilling",
          [("eager", "Eager is the opposite."), ("unable", "Unable means cannot, not does not want to."), ("ready", "Ready does not show unwillingness.")],
          2, "Reluctant means not wanting to do something: unwilling.", "Synonym in context", "Concept", "Did the boy want to speak?"),
        Q("Which pair are complementary antonyms (no middle position)?", "alive and dead",
          [("hot and cold", "Warm lies between hot and cold."), ("big and small", "Medium lies between big and small."), ("rich and poor", "A person can be neither rich nor poor.")],
          3, "A living thing is alive or dead, with no middle state.", "Types of antonym", "Concept", "Which pair has nothing in between?"),
        Q("Which pair are relational antonyms (one depends on the other)?", "buy and sell",
          [("early and late", "These are gradable."), ("true and false", "These are complementary."), ("tall and short", "These are gradable.")],
          0, "You cannot buy unless someone sells: the meanings depend on each other.", "Relational antonyms", "Concept", "Which pair needs two people in opposite roles?"),
        Q("'Inflammable' means", "easily set on fire",
          [("not able to burn", "The prefix in- does not make this word negative."), ("wet", "Nothing in the word means wet."), ("hard to see", "It has nothing to do with sight.")],
          1, "Inflammable means the same as flammable. The opposite is non-flammable.", "False opposites", "Concept", "Is the in- here a negative prefix?"),
        Q("'The farmer was thrifty.' Which word has the closest meaning and a similarly positive feeling?", "economical",
          [("stingy", "Stingy has a negative feeling."), ("careless", "This does not suit saving money."), ("generous", "Generous means giving freely, which is different.")],
          2, "Thrifty and economical are both positive words about careful use of money.", "Connotation", "Analysis", "Choose the word with the same meaning and the same feeling."),
        Q("'The road was narrow, but the new one is ______.' Which word fits as an antonym?", "wide",
          [("long", "Length is not the opposite of width."), ("old", "The sentence is about width."), ("short", "That is the opposite of long.")],
          3, "Narrow and wide are opposites on the scale of width.", "Antonym in context", "Application", "Which word is the opposite of narrow?"),
    ]))

# ------------------------------------------------------------------ 4. Homonyms
SETS.append(practice_set(
    module=M3, topic="Synonyms, antonyms and homonyms", title="Homonyms, homophones and homographs", lesson="evo-homonyms-homophones",
    questions=[
        Q("'Write' and 'right' are", "homophones",
          [("homographs", "Homographs are spelt the same."), ("synonyms", "They do not mean the same thing."), ("antonyms", "They are not opposites.")],
          0, "They sound the same but are spelt differently.", "Homophones", "Recall", "Do they sound the same, and are they spelt the same?"),
        Q("Which sentence uses the correct word?", "They left their bags there.",
          [("They left there bags their.", "The words are in the wrong places."), ("They left they're bags their.", "They're means they are."), ("They left there bags there.", "The first 'there' should be 'their'.")],
          1, "'Their' shows ownership; 'there' shows a place.", "Their and there", "Application", "Which word shows that the bags belong to them?"),
        Q("'The ______ of the school welcomed the visitors.' Choose the correct word.", "principal",
          [("principle", "A principle is a rule or belief."), ("principel", "This word does not exist."), ("principall", "This word does not exist.")],
          2, "The principal is the head of the school.", "Principal and principle", "Application", "The gap needs a person."),
        Q("Which word means 'paper, pens and envelopes'?", "stationery",
          [("stationary", "This means not moving."), ("stationnery", "This word does not exist."), ("stationry", "This word does not exist.")],
          3, "Stationery with an e refers to writing materials.", "Stationery and stationary", "Recall", "Remember: e for envelopes."),
        Q("The word 'bank' in 'We sat on the bank of the river' means", "the land beside a river",
          [("a place for money", "That meaning does not fit a river."), ("a pile of bricks", "This is not the meaning in the sentence."), ("a long wait", "This is not a meaning of bank.")],
          0, "'River' tells you that it is the side of the river.", "Homonym meaning", "Concept", "Which word in the sentence is a clue?"),
        Q("'Tear' (a drop from the eye) and 'tear' (to rip) are examples of", "homographs",
          [("homophones", "Homophones are spelt differently."), ("synonyms", "They do not have the same meaning."), ("compounds", "They are not made of two words.")],
          1, "Same spelling, different meaning and different sound: homographs. (Some books call them homonyms; check your textbook.)", "Homographs", "Concept", "Same spelling but different sounds."),
        Q("Which sentence is correct?", "The weather was very hot.",
          [("The whether was very hot.", "Whether means if."), ("The wether was very hot.", "This is not a word for climate."), ("The wheather was very hot.", "This spelling is wrong.")],
          2, "Weather is about sun, rain and temperature; whether means if.", "Weather and whether", "Application", "Which word is about sun and rain?"),
        Q("Which sentence gives 'advice' correctly?", "The nurse gave me good advice.",
          [("The nurse advice me to rest.", "A verb is needed here: advised."), ("The nurse gave me good advise.", "Advise is a verb."), ("I need your advise.", "A noun is needed: advice.")],
          0, "Advice is the noun; advise is the verb.", "Advice and advise", "Application", "Which word is a noun after 'good'?"),
    ]))

# ------------------------------------------------------------------ 5. Idioms and proverbs
SETS.append(practice_set(
    module=M3, topic="Idiomatic expressions and proverbs", title="Idioms and proverbs", lesson="evo-idioms-proverbs",
    questions=[
        Q("'The exam was a piece of cake.' This means the exam was", "very easy",
          [("very sweet", "That is the literal reading."), ("very long", "Nothing suggests length."), ("very difficult", "That is the opposite.")],
          0, "'A piece of cake' means very easy.", "Idiom meaning", "Recall", "Is it about food or about difficulty?"),
        Q("'She was under the weather and stayed at home.' She was", "slightly ill",
          [("angry", "The idiom is not about anger."), ("late", "The idiom is not about time."), ("very rich", "The idiom is not about money.")],
          1, "'Under the weather' means slightly ill.", "Idiom meaning", "Recall", "Why would someone stay at home?"),
        Q("Which proverb means 'Think before you act'?", "Look before you leap.",
          [("Haste makes waste.", "This means that hurrying causes mistakes."), ("Practice makes perfect.", "This is about repeating to improve."), ("Birds of a feather flock together.", "This is about people with similar habits.")],
          2, "'Look before you leap' warns us to think before acting.", "Proverb meaning", "Recall", "Which proverb tells you to look first?"),
        Q("A man spills the beans about a surprise party. He", "reveals the secret",
          [("makes a meal", "That is the literal reading."), ("wastes food", "That is the literal reading."), ("organises the party", "Nothing says he organises it.")],
          3, "To spill the beans means to reveal a secret.", "Idiom meaning", "Concept", "What would ruin a surprise?"),
        Q("Which proverb suits a nurse who fixes a small problem before it grows?", "A stitch in time saves nine.",
          [("Too many cooks spoil the broth.", "That is about too many people on one task."), ("All that glitters is not gold.", "That is about appearances."), ("Birds of a feather flock together.", "That is about friendship.")],
          1, "Mending a small tear early prevents a bigger one.", "Proverb in context", "Application", "Which proverb is about early repair?"),
        Q("'It cost an arm and a leg' means it was", "very expensive",
          [("painful", "The idiom does not refer to injury."), ("badly made", "The idiom is about price."), ("a bargain", "That is the opposite.")],
          2, "The idiom means a very high price.", "Idiom meaning", "Concept", "What is lost when something 'costs' so much?"),
        Q("Which sentence uses the idiom correctly?", "We hit the nail on the head when we named the problem.",
          [("We hit the nail in the head when we named the problem.", "The idiom is 'on the head'."), ("We hit the nail with the head when we named the problem.", "The idiom has fixed words."), ("We hit the nail on the hammer when we named the problem.", "The idiom has fixed words.")],
          0, "Idioms must keep their exact wording.", "Using idioms", "Application", "Which version keeps the whole fixed phrase?"),
        Q("A student has a sure job but leaves it for an uncertain offer. Which proverb warns about this?", "A bird in the hand is worth two in the bush.",
          [("Where there is a will, there is a way.", "This is about determination."), ("A friend in need is a friend indeed.", "This is about true friends."), ("Actions speak louder than words.", "This is about deeds versus words.")],
          3, "Keep what you have rather than risk it for something uncertain.", "Proverb in context", "Analysis", "Which proverb compares what you hold with what you might get?"),
    ]))

# ------------------------------------------------------------------ 6. Figurative language
SETS.append(practice_set(
    module=M3, topic="Figurative language in context", title="Figures of speech", lesson="evo-figurative-language",
    questions=[
        Q("'She runs like the wind.' This is a", "simile",
          [("metaphor", "A metaphor does not use like or as."), ("hyperbole", "It compares; it is not simple exaggeration."), ("irony", "Nothing is the opposite of what is expected.")],
          0, "It uses 'like' to compare.", "Simile", "Recall", "Look for the word 'like'."),
        Q("'The market was a beehive.' This is a", "metaphor",
          [("simile", "There is no like or as."), ("personification", "A beehive is not a human action."), ("oxymoron", "No two opposites are joined.")],
          1, "It says the market IS a beehive.", "Metaphor", "Recall", "Does it say 'like' or 'is'?"),
        Q("'The wind whispered through the trees.' This is", "personification",
          [("simile", "There is no like or as."), ("onomatopoeia only", "Whisper imitates a sound, but the wind is also given a human action."), ("hyperbole", "There is no exaggeration.")],
          2, "Wind cannot whisper; whispering is a human action, so this is personification.", "Personification", "Concept", "Who or what normally whispers?"),
        Q("'I have told you a million times.' This is", "hyperbole",
          [("understatement", "That would say less than the truth."), ("irony", "Nothing is the opposite of expected."), ("simile", "There is no comparison with like or as.")],
          3, "It exaggerates for emphasis.", "Hyperbole", "Concept", "Is the number literal?"),
        Q("'Deafening silence' is an example of", "an oxymoron",
          [("alliteration", "The sounds do not repeat."), ("onomatopoeia", "It does not imitate a sound."), ("a simile", "No like or as.")],
          0, "Deafening (very loud) and silence (no sound) are opposites joined together.", "Oxymoron", "Concept", "Do the two words contradict each other?"),
        Q("'He passed away last year' is a", "euphemism",
          [("hyperbole", "Nothing is exaggerated."), ("metaphor", "It does not say one thing is another."), ("irony", "Nothing is the opposite of what is expected.")],
          1, "'Passed away' is a gentle way to say 'died'.", "Euphemism", "Concept", "Is it a softer way of saying something sad?"),
        Q("Which word is an example of onomatopoeia?", "hiss",
          [("quickly", "It does not imitate a sound."), ("silent", "It is the absence of sound."), ("beautiful", "It does not imitate a sound.")],
          2, "The word 'hiss' sounds like what it names.", "Onomatopoeia", "Recall", "Which word sounds like its meaning?"),
        Q("'The old lorry groaned up the hill.' What is the effect of 'groaned'?", "It makes the lorry seem tired and shows how hard the climb is.",
          [("It shows that the lorry is new.", "Old is stated, and groaning suggests effort."), ("It shows that the lorry is quiet.", "Groaning is a noise."), ("It shows that the driver is angry.", "The driver is not mentioned.")],
          3, "Groaning is a human sound of effort; it personifies the lorry.", "Effect of figures of speech", "Analysis", "What does a groan tell you about effort?"),
    ]))

# ------------------------------------------------------------------ 7. Register: health and environment
SETS.append(practice_set(
    module=M3, topic="Register: health, medicine and environment", title="Health and environment vocabulary", lesson="evo-register-health-environment",
    questions=[
        Q("The doctor's decision about what illness a patient has is the", "diagnosis",
          [("prescription", "A prescription is the written order for medicine."), ("symptom", "A symptom is what the patient feels."), ("dose", "A dose is the amount of medicine.")],
          0, "A diagnosis names the illness.", "Health terms", "Recall", "Which word is about deciding what the illness is?"),
        Q("A disease that spreads across many countries is a", "pandemic",
          [("symptom", "A symptom is a feeling of the patient."), ("prescription", "A prescription is a written order."), ("dose", "A dose is an amount of medicine.")],
          0, "A pandemic affects many countries; an epidemic is more local.", "Epidemic and pandemic", "Concept", "Which word shows a very wide area?"),
        Q("Which is a SIGN of illness (something a doctor can measure)?", "a high temperature",
          [("a headache", "A headache is felt by the patient: a symptom."), ("tiredness", "Tiredness is felt by the patient: a symptom."), ("nausea", "Nausea is felt by the patient: a symptom.")],
          0, "A temperature can be measured by someone else, so it is a sign.", "Symptom and sign", "Concept", "Which one can be measured by the nurse?"),
        Q("'Cutting down large areas of forest' is called", "deforestation",
          [("conservation", "Conservation protects nature."), ("erosion", "Erosion wears away soil."), ("biodiversity", "Biodiversity is the variety of living things.")],
          0, "Deforestation means removing forests on a large scale.", "Environment terms", "Recall", "Which word means removing forest?"),
        Q("Which sentence uses 'sustainable' correctly?", "Sustainable farming protects the soil for the future.",
          [("The sustainable farmer lost all his crops.", "Sustainable means able to continue; it does not suggest loss."), ("She felt sustainable after lunch.", "Sustainable does not describe a feeling."), ("The sustainable was very long.", "It is an adjective and needs a noun.")],
          0, "Sustainable describes practices that can continue without using up resources.", "Sustainable", "Application", "Which use describes ways of working that last?"),
        Q("Which is the best formal word for 'start' in a report?", "commence",
          [("kick off", "This is informal."), ("get going", "This is informal."), ("fire up", "This is informal.")],
          0, "'Commence' is formal; the others are informal.", "Formal register", "Application", "Which word would suit a letter to a minister?"),
        Q("'The slow wearing away of soil by rain and wind' is", "erosion",
          [("pollution", "Pollution is harmful substances."), ("drought", "Drought is lack of rain."), ("emission", "An emission is gas released.")],
          0, "Erosion wears soil away.", "Erosion", "Recall", "Which word is about soil being removed?"),
        Q("'The illness lasted for years.' Which word describes this illness?", "chronic",
          [("acute", "Acute means sudden and severe."), ("endemic", "Endemic describes a disease always present in a place."), ("sanitary", "Sanitary relates to cleanliness.")],
          0, "A long-lasting illness is chronic.", "Chronic and acute", "Concept", "Which word means lasting a long time?"),
    ]))

# ------------------------------------------------------------------ 8. Register: science and ICT
SETS.append(practice_set(
    module=M3, topic="Register: science, technology and ICT", title="Science and ICT vocabulary", lesson="evo-register-science-ict",
    questions=[
        Q("A statement that can be tested to explain something is a", "hypothesis",
          [("conclusion", "A conclusion comes after the results."), ("control", "A control is the part kept unchanged."), ("observation", "An observation is something seen or measured.")],
          0, "A hypothesis is a testable statement or proposed explanation.", "Scientific terms", "Recall", "Which word comes before the experiment?"),
        Q("Which of these is software?", "a word processor",
          [("a keyboard", "A keyboard is hardware."), ("a monitor", "A monitor is hardware."), ("a hard disk", "A hard disk is hardware.")],
          0, "A word processor is a program, so it is software.", "Hardware and software", "Concept", "Which one is a program and not a device?"),
        Q("To copy a file from the internet to your phone is to", "download it",
          [("upload it", "Uploading sends a file from your device to the internet."), ("encrypt it", "Encrypting changes data into code."), ("delete it", "Deleting removes a file.")],
          0, "Download means copy to your device.", "Download and upload", "Recall", "In which direction does the file move?"),
        Q("Changing data into code so that only authorised people can read it is", "encryption",
          [("a firewall", "A firewall blocks unauthorised access."), ("bandwidth", "Bandwidth is how much data a connection carries."), ("a database", "A database is an organised collection of data.")],
          0, "Encryption protects data by coding it.", "ICT terms", "Recall", "Which word is about secret code?"),
        Q("Choose the best sentence in scientific style.", "The data show that the temperature rose.",
          [("The data shows that temperature kind of went up.", "'Kind of went up' is informal and not precise."), ("Temperature went up lots, I think.", "This is informal and vague."), ("The temperature was like, higher.", "This is informal and vague.")],
          0, "Scientific writing is precise and formal; 'data' is plural.", "Scientific style", "Application", "Which sentence is precise?"),
        Q("An experiment gives the same result every time it is repeated. It is", "reliable",
          [("accurate", "Accurate means close to the true value."), ("hypothetical", "That relates to a hypothesis."), ("controlled", "That relates to a control.")],
          0, "Reliable means repeatable results.", "Reliable and accurate", "Concept", "Which word is about repeating?"),
        Q("In science, the word 'theory' means", "a well-tested explanation",
          [("a guess", "That is the everyday use."), ("an opinion", "That is not its scientific meaning."), ("a hope", "That is not its scientific meaning.")],
          0, "A scientific theory is a well-tested explanation.", "Everyday words with special meanings", "Concept", "Is a scientific theory a wild guess?"),
        Q("'The firewall blocked unauthorised access to the school network.' What does a firewall do?", "It protects a network by blocking unauthorised access.",
          [("It makes the network faster.", "That is bandwidth, not a firewall."), ("It stores files online.", "That is cloud storage."), ("It copies files to a phone.", "That is downloading.")],
          0, "The sentence itself says the firewall blocked unauthorised access.", "Context in ICT", "Analysis", "What did it do, according to the sentence?"),
    ]))

# ------------------------------------------------------------------ 9. Register: commerce
SETS.append(practice_set(
    module=M3, topic="Register: commerce, finance and administration", title="Commerce and administration vocabulary", lesson="evo-register-commerce-admin",
    questions=[
        Q("Selling goods in small amounts to the public is", "retail",
          [("wholesale", "Wholesale means large amounts, usually to traders."), ("export", "Export means sending goods abroad."), ("deposit", "A deposit is money paid in.")],
          0, "Retail is selling in small amounts to customers.", "Trade terms", "Recall", "Which word is about selling to the public?"),
        Q("A paper that shows payment has been made is a", "receipt",
          [("invoice", "An invoice asks for payment."), ("budget", "A budget is a plan."), ("loan", "A loan is borrowed money.")],
          0, "A receipt is proof of payment.", "Receipt and invoice", "Recall", "Does it ask for payment or confirm it?"),
        NUM("A shop receives 80,000 FCFA from sales and spends 65,000 FCFA on goods and rent. Find the profit in FCFA.", 15000,
            steps=[S("Profit = revenue minus costs", math=r"80\,000 - 65\,000 = 15\,000")], tolerance=0, unit="FCFA",
            concept="Profit", skill="Calculation", hint="Subtract the money spent from the money received.",
            feedback="Profit is what is left after costs."),
        Q("The written record of what was decided at a meeting is called the", "minutes",
          [("agenda", "The agenda is the list of items before the meeting."), ("memo", "A memo is a short message."), ("circular", "A circular is a notice to many people.")],
          0, "Minutes record what was said and decided.", "Administration terms", "Concept", "Is the record made during or after the meeting?"),
        Q("Which closing is correct after 'Dear Sir or Madam'?", "Yours faithfully",
          [("Yours sincerely", "Use this when you know the person's name."), ("Your friend", "This is informal."), ("Best wishes", "This is informal.")],
          0, "Yours faithfully follows 'Dear Sir or Madam'.", "Formal letters", "Application", "Do you know the person's name?"),
        Q("Which of these means 'money paid for borrowing'?", "interest",
          [("deposit", "A deposit is money paid into an account."), ("tax", "A tax is paid to government."), ("commission", "A commission is paid to an agent.")],
          0, "Interest is paid on a loan.", "Finance terms", "Recall", "What do you pay in addition to the amount borrowed?"),
        Q("'The company has a vacancy for an accountant.' A vacancy is", "a job that is available",
          [("a holiday", "That is not its meaning."), ("a bank account", "That is not its meaning."), ("a tax form", "That is not its meaning.")],
          0, "A vacancy is an available job.", "Administration terms", "Concept", "What does the company want to do?"),
        Q("A farmer sells cocoa in 50 kg bags to a trader. This is a", "wholesale sale",
          [("retail sale", "Retail is in small amounts to the public."), ("withdrawal", "A withdrawal is money taken from a bank."), ("receipt", "A receipt is a proof of payment.")],
          0, "Large amounts sold to a trader are wholesale.", "Wholesale and retail", "Application", "Is the amount large or small?"),
    ]))

# ------------------------------------------------------------------ 10. Register: law and governance
SETS.append(practice_set(
    module=M3, topic="Register: law, governance and human rights", title="Law and governance vocabulary", lesson="evo-register-law-governance",
    questions=[
        Q("The body that makes laws is the", "legislature",
          [("judiciary", "The judiciary is the courts."), ("executive", "The executive carries out laws."), ("witness", "A witness gives evidence.")],
          0, "The legislature makes laws.", "Government terms", "Recall", "Which body makes laws?"),
        Q("A person who tells the court what he or she saw is a", "witness",
          [("plaintiff", "A plaintiff brings a case."), ("magistrate", "A magistrate is a judge."), ("lawyer", "A lawyer represents a party.")],
          0, "A witness gives evidence.", "Court terms", "Recall", "Who describes events to the court?"),
        Q("A proposed law that has not yet been passed is a", "bill",
          [("act", "An act is a bill that has been passed."), ("verdict", "A verdict is a decision in a case."), ("sentence", "A sentence is a punishment.")],
          0, "A bill becomes an act after it is passed.", "Bill and act", "Concept", "Has it been passed yet?"),
        Q("The court declared the accused not guilty. The accused was", "acquitted",
          [("convicted", "Convicted means found guilty."), ("sentenced", "A sentence is a punishment."), ("appealed", "An appeal is a request to a higher court.")],
          0, "To acquit means to declare not guilty.", "Convict and acquit", "Concept", "Which word means cleared?"),
        Q("Temporary release of an accused person before the trial is", "bail",
          [("appeal", "An appeal is made after a decision."), ("verdict", "A verdict is the decision."), ("offence", "An offence is a crime.")],
          0, "Bail allows release before trial.", "Bail", "Recall", "Which word is about release before the trial?"),
        Q("Treating people unfairly because of who they are is", "discrimination",
          [("equality", "Equality means equal treatment."), ("dignity", "Dignity means respect."), ("justice", "Justice means fair treatment.")],
          0, "Discrimination is unfair treatment.", "Human rights terms", "Recall", "Which word describes unfair treatment?"),
        Q("Which sentence uses 'citizen' correctly?", "A citizen of a country may vote when old enough.",
          [("The citizen was acquitted of a law.", "'Acquitted of a law' is wrong; one is acquitted of a charge."), ("The citizen made a bill with a loan.", "This does not make sense."), ("The citizen is a kind of court.", "A citizen is a person.")],
          0, "A citizen is a person who legally belongs to a country.", "Citizen", "Application", "Which sentence describes a person and a right?"),
        Q("The three arms of government are", "legislature, executive and judiciary",
          [("bill, act and law", "These are kinds of legal documents."), ("plaintiff, defendant and witness", "These are people in a court case."), ("ballot, candidate and constituency", "These are election words.")],
          0, "The legislature makes laws, the executive carries them out and the judiciary applies them.", "Governance", "Concept", "Which group names the three main bodies of government?"),
    ]))

# ================================================================== Reading passages
WATER = (
    "Water for Our School\n\n"
    "Last year, the pupils of Government Primary School Nkoteng walked nearly two kilometres each morning to fetch water from a stream. Many arrived late, and some fell ill after drinking water that was not clean.\n\n"
    "In March, the Parent-Teacher Association decided to act. Each family gave 2,000 FCFA, and the local council added money for materials. A well was dug beside the school and covered with a concrete top, and a hand pump was fitted.\n\n"
    "The results were clear within one term. Pupils now arrive on time, cases of stomach illness have dropped, and a school garden has been planted with vegetables watered from the well.\n\n"
    "The headmistress says the project shows what a community can do together. The Association plans to repair the school's toilets next year."
)

RACE = (
    "The Hill Race\n\n"
    "Every February, more than two hundred runners gather at the foot of a hill near Kumba for the annual hill race. The course is eight kilometres long, and the climb is steep and rocky. "
    "The fastest runners reach the top in just over an hour, while others walk the last part and finish in three.\n\n"
    "Local families line the path with water, oranges and drums to encourage everybody. Last year a boy of fourteen finished third, and the crowd cheered him all the way down. "
    "The winner gave her prize to the village clinic. Organisers say the race is not only about speed: it brings the community together and raises money for local projects."
)

ROAD = (
    "A New Market Road\n\n"
    "For years, the road to Ngomo market was little more than a narrow, muddy track. During the rains, lorries sank to their axles, and traders carried their loads on their heads for hours. "
    "Many farmers earned meagre profits because they could not reach the market before their tomatoes rotted.\n\n"
    "Last year the council tarred the road. Now the village is bustling with activity: lorries arrive daily, and shops have opened along the route. Farmers who once struggled have begun to prosper, and some have built new houses. "
    "Not everyone is pleased, however. A few elderly residents complain that the noise has destroyed the peace they once enjoyed, and they miss the quiet of the old track."
)

LETTER = (
    "Dear Editor,\n\n"
    "For three months the street lights on Independence Avenue have been out. Children walk home in darkness, and last week a student was knocked down by a motorbike. "
    "The council has promised repairs at every meeting, yet nothing has been done. Is it too much to ask that those who are paid to serve us do their work? "
    "I urge the council to act now, before another person is hurt."
)

UNCLE = (
    "My uncle believes he is the finest driver in Cameroon. He has only hit three goats, two bicycles and one very surprised mango tree, he explains, and all of them were standing in the wrong place. "
    "We travel with him only when we are carrying nothing valuable, including ourselves."
)

BAKERY = (
    "The Bakery\n\n"
    "Maman Ruth opens her bakery at four every morning, long before the first taxi passes. By six o'clock, the smell of fresh bread fills the street and a line of customers waits at her window. "
    "She uses a wood-fired oven that her late husband built, and she refuses to change it, even though her son has offered to buy an electric one.\n\n"
    "'Machines cannot give bread this taste,' she says with a smile. Her loaves are sold out by nine. Yet the shop next door, which has an electric oven, still has bread on its shelves at noon. "
    "Some neighbours say that Maman Ruth works too hard for her age, but she says that her day would feel empty without the dough on her hands."
)

TAXI = (
    "The Taxi Driver\n\n"
    "Mr Etoa has driven a taxi in Yaounde for twenty years. He never plays music while he drives, and he keeps a small cloth to wipe the seats after every passenger. "
    "When the rains start, he carries an umbrella for elderly customers. Regular customers call him before they travel, and on busy mornings he politely turns away new ones. "
    "'A driver who is clean and calm,' he says, 'never needs to look for passengers.'"
)

MOBILE = (
    "Mobile Money in Our Town\n\n"
    "Ten years ago, if Mr Fon in Bamenda wanted to send money to his mother in a village near Wum, he had to travel for six hours or pay a bus driver to carry an envelope. "
    "The journey was tiring, costly and risky. Today he sends the money in less than a minute using his mobile phone. This service, called mobile money, has changed life in many parts of Cameroon.\n\n"
    "Mobile money allows people to store small amounts of money on a phone, to send it to others and to pay bills. Traders use it to buy goods from suppliers in other towns without carrying cash. "
    "Parents use it to pay school fees. Farmers receive payments directly from buyers. As a result, people are less afraid of theft, and they save time and transport costs.\n\n"
    "However, there are also dangers. Some people lose money to criminals who pretend to be agents and ask for secret codes. Others forget to check the amount before they confirm a payment. "
    "In addition, the service is of little use in places where the network is weak. Experts therefore advise users never to share their secret codes, to check each message carefully and to keep their phones safe."
)

PLASTIC = (
    "In many towns, plastic bags are thrown into drains. When the rains come, the drains block, and water floods the roads and houses. Flooding spreads diseases such as cholera. "
    "Moreover, burning plastic fills the air with harmful smoke. To solve the problem, councils should provide bins, shops should charge for bags, and citizens should reuse bags or use baskets."
)


def R(passage, question):
    """Question prompt with its passage (the platform shows paragraphs separated by blank lines)."""
    return "Read the passage and answer the question.\n\n" + passage + "\n\n" + question


# ------------------------------------------------------------------ 11. Skim and scan
SETS.append(practice_set(
    module=M4, topic="Skimming, scanning and main ideas", title="Skimming, scanning and the main idea", lesson="evo-skim-scan-main-idea",
    questions=[
        Q("Which reading skill do you use to find a date, a name or a number quickly?", "scanning",
          [("skimming", "Skimming gives the general idea."), ("summarising", "Summarising shortens a whole text."), ("predicting", "Predicting is guessing before you read.")],
          0, "Scanning means looking for one particular detail.", "Scanning", "Recall", "Is it for the general idea or one detail?"),
        Q("The first sentence of a paragraph that states its main idea is called the", "topic sentence",
          [("conclusion", "A conclusion ends an argument."), ("title", "The title belongs to the whole text."), ("supporting detail", "A supporting detail explains the main idea.")],
          0, "The topic sentence states the main idea of a paragraph.", "Topic sentence", "Recall", "Which sentence states the idea of the paragraph?"),
        Q(R(WATER, "What is the passage mainly about?"), "How a community gave its school clean water and improved the school",
          [("The cost of digging a well", "The cost is only a detail."), ("The illness of pupils", "Illness is only part of the problem in paragraph 1."), ("The work of the council", "The council gives money but is not the main subject.")],
          0, "The passage describes the problem, the community action and the good results.", "Main idea", "Comprehension", "Choose the idea that covers all four paragraphs."),
        Q(R(WATER, "How much did each family give?"), "2,000 FCFA",
          [("20,000 FCFA", "This has an extra zero."), ("200 FCFA", "A zero is missing."), ("Nothing; the council paid", "The council added money but each family also gave.")],
          0, "Paragraph 2 says each family gave 2,000 FCFA. Scanning for FCFA finds it.", "Scanning for numbers", "Recall", "Scan paragraph 2 for an amount of money."),
        Q(R(WATER, "Which is the best title for the passage?"), "A Well for Our School",
          [("The Danger of Streams", "Streams are only mentioned in paragraph 1."), ("Pupils Who Fell Ill", "Illness is only part of the problem."), ("A School Garden", "The garden is a detail in paragraph 3.")],
          0, "The title must cover the whole passage; the well is the centre of the story.", "Title and main idea", "Comprehension", "Which title fits the whole text and not one detail?"),
        Q(R(RACE, "How long is the course of the hill race?"), "eight kilometres",
          [("two hundred kilometres", "Two hundred is the number of runners."), ("three kilometres", "Three is the number of hours for slower runners."), ("fourteen kilometres", "Fourteen is the boy's age.")],
          0, "Scan for 'kilometres': 'The course is eight kilometres long.'", "Scanning", "Recall", "Scan paragraph 1 for the distance."),
        Q(R(RACE, "What is the main idea of the second paragraph?"), "The race is supported by the community and benefits local projects",
          [("A boy finished third", "This is a detail."), ("The winner was rich", "This is not stated."), ("The path is rocky", "That is in the first paragraph.")],
          0, "The paragraph shows families encouraging the runners, the prize given to the clinic and money raised: community support and benefit.", "Main idea of a paragraph", "Comprehension", "Which idea joins all the sentences in paragraph 2?"),
        Q(R(RACE, "Who gave her prize to the village clinic?"), "the winner of the race",
          [("the boy of fourteen", "He finished third; he is not said to have given a prize."), ("the organisers", "The organisers speak about the race but do not give the prize."), ("the families on the path", "They gave water, oranges and encouragement.")],
          0, "'The winner gave her prize to the village clinic.' Scanning for 'clinic' finds it.", "Scanning for a name or role", "Recall", "Scan for the word 'clinic'."),
    ]))

# ------------------------------------------------------------------ 12. Context clues
SETS.append(practice_set(
    module=M4, topic="Contextual vocabulary deduction", title="Meanings from context", lesson="evo-context-clues",
    questions=[
        Q(R(ROAD, "In the passage, 'meagre' means"), "very small",
          [("very large", "Farmers whose tomatoes rotted did not earn large profits."), ("steady", "Nothing in the passage suggests steadiness."), ("unfair", "The passage does not discuss fairness.")],
          0, "Because tomatoes rotted before reaching the market, the profits were very small.", "Context clue: cause and effect", "Comprehension", "What happens to a farmer whose tomatoes rot?"),
        Q(R(ROAD, "In the passage, 'bustling' means"), "full of busy activity",
          [("silent", "Lorries arrive and shops open, so it is not silent."), ("poor", "The farmers are beginning to prosper."), ("empty", "Lorries arrive daily, so it is not empty.")],
          0, "Lorries arrive daily and shops open: the village is busy.", "Context clue", "Comprehension", "What is happening in the village?"),
        Q(R(ROAD, "In the passage, 'prosper' means"), "do well and become successful",
          [("struggle", "'Who once struggled' signals the opposite."), ("complain", "The complaints come from the elderly residents."), ("travel", "The word is about success, not travel.")],
          0, "'Once struggled' contrasts with 'prosper', and building new houses shows success.", "Contrast clue", "Comprehension", "Look at the contrast with 'once struggled'."),
        Q("'Unlike his frugal brother, who saved every coin, Ako spent freely.' 'Frugal' means", "careful with money",
          [("generous", "Generous is similar to Ako, not to his brother."), ("lazy", "Nothing says the brother is lazy."), ("rich", "Saving coins does not show wealth.")],
          0, "'Unlike' shows the opposite of Ako, who spent freely: the brother is careful with money.", "Contrast clue", "Application", "What is the opposite of spending freely?"),
        Q("'A nomad is a person who moves from place to place.' This sentence gives the meaning of 'nomad' by", "a definition",
          [("a contrast", "There is no opposite signal."), ("an example", "No examples are given."), ("a word part", "No prefix or suffix is used.")],
          0, "The sentence directly defines the word.", "Types of clue", "Concept", "Does the sentence state the meaning directly?"),
        Q("'Many tubers, for example yams, cassava and cocoyams, grow underground.' A tuber is", "a plant part that grows underground",
          [("a kind of fruit", "The examples are not fruits growing above ground."), ("a farming tool", "The examples are plants."), ("a bird", "The examples are plants.")],
          0, "The examples and 'grow underground' show the meaning.", "Example clue", "Application", "What do yams, cassava and cocoyams have in common?"),
        Q("Which word part helps you to work out that 'disappear' means 'stop being seen'?", "the prefix dis-",
          [("the suffix -ar", "There is no such suffix here."), ("the root 'sap'", "The root is 'appear'."), ("the letter p", "A single letter gives no meaning.")],
          0, "Dis- gives the opposite sense of appear.", "Word parts", "Concept", "Which part has a negative meaning?"),
        Q("'Her enthusiasm was contagious; soon the whole class was eager to start.' 'Contagious' means", "spreading from one person to another",
          [("boring", "A boring feeling would not make everyone eager."), ("invisible", "Nothing is said about being unseen."), ("false", "Nothing suggests it was false.")],
          0, "The whole class became eager, so the feeling spread.", "Cause and effect clue", "Comprehension", "What happened to the class?"),
    ]))

# ------------------------------------------------------------------ 13. Tone, attitude, purpose
SETS.append(practice_set(
    module=M4, topic="Tone, attitude and purpose", title="Tone, attitude and purpose in passages", lesson="evo-tone-attitude-purpose",
    questions=[
        Q("The tone of the following sentence is: 'Oh, thank you very much for waking the whole street at four in the morning.'", "sarcastic",
          [("appreciative", "The thanks are not sincere."), ("formal", "The language is not formal."), ("sympathetic", "There is no sorrow shown.")],
          0, "The speaker says thanks but means the opposite.", "Sarcasm", "Concept", "Is the speaker really grateful?"),
        Q(R(LETTER, "What is the writer's attitude to the council?"), "critical and concerned",
          [("admiring", "He is not praising the council."), ("indifferent", "He cares enough to write."), ("amused", "The topic is serious.")],
          0, "He criticises the council for failing to act and shows concern for the children.", "Attitude", "Comprehension", "Does he approve of the council's work?"),
        Q(R(LETTER, "What is the main purpose of the letter?"), "to complain and to urge action",
          [("to entertain readers", "The subject is serious."), ("to give directions", "No directions are given."), ("to advertise a service", "Nothing is advertised.")],
          0, "He complains about the lights and urges the council to act.", "Purpose", "Comprehension", "What does he want to happen?"),
        Q(R(LETTER, "Which phrase shows urgency?"), "act now, before another person is hurt",
          [("for three months", "This gives the length of the problem."), ("on Independence Avenue", "This names the place."), ("Dear Editor", "This is a greeting.")],
          0, "'Now' and 'before another person is hurt' press for quick action.", "Clues to tone", "Application", "Which words call for immediate action?"),
        Q(R(UNCLE, "What is the tone of the passage?"), "humorous",
          [("angry", "There is no anger."), ("sorrowful", "The passage is meant to amuse."), ("scientific", "It is not objective or technical.")],
          0, "The exaggerated list of things he hit and the final joke show humour.", "Humorous tone", "Comprehension", "Is the writer trying to make us smile?"),
        Q(R(UNCLE, "What does the final sentence suggest about the uncle's driving?"), "It is dangerous, and the writer is joking about it.",
          [("It is very safe.", "That is the opposite."), ("It is the best in the country.", "That is what the uncle believes, not the writer."), ("It is slow.", "Speed is not mentioned.")],
          0, "The writer says they never carry anything valuable, 'including ourselves'. This hints at danger in a comic way.", "Irony and attitude", "Analysis", "Why would no one carry valuable things, even themselves?"),
        Q("A notice reads: 'Beware of the dog. Never enter without permission.' The purpose is to", "warn",
          [("entertain", "There is no humour."), ("complain", "No complaint is made."), ("praise", "Nothing is praised.")],
          0, "'Beware' and 'Never' are signals of a warning.", "Purpose", "Application", "Which words are commands about danger?"),
        Q("Which word best describes someone who is longing for the days of their childhood?", "nostalgic",
          [("sarcastic", "Sarcasm says the opposite of what is meant."), ("objective", "Objective means giving facts only."), ("urgent", "Urgent means needing quick action.")],
          0, "Nostalgic means longing for the past.", "Tone vocabulary", "Recall", "Which word is about the past?"),
    ]))

# ------------------------------------------------------------------ 14. Factual and inferential
SETS.append(practice_set(
    module=M4, topic="Factual and inferential questions", title="Factual and inferential questions", lesson="evo-factual-inferential",
    questions=[
        Q(R(BAKERY, "At what time does Maman Ruth open her bakery?"), "at four in the morning",
          [("at six in the morning", "At six the smell fills the street."), ("at nine in the morning", "By nine her loaves are sold out."), ("at noon", "At noon the shop next door still has bread.")],
          0, "This is a factual question: 'opens her bakery at four every morning'.", "Factual question", "Recall", "Scan for the time she opens."),
        Q(R(BAKERY, "Who built the oven?"), "her late husband",
          [("her son", "He offered to buy an electric one."), ("a neighbour", "No neighbour is said to have built it."), ("herself", "The passage does not say so.")],
          0, "'a wood-fired oven that her late husband built' is stated.", "Factual question", "Recall", "Look for the sentence that mentions the oven."),
        Q(R(BAKERY, "What can be inferred about Maman Ruth's bread?"), "Many customers prefer it to the bread of the shop next door.",
          [("It is the cheapest in the town.", "Price is not mentioned."), ("It is made by machines.", "She uses a wood-fired oven."), ("It is sold at noon.", "It is sold out by nine.")],
          0, "Her bread is sold out by nine while the next shop still has bread at noon.", "Inference", "Comprehension", "Compare the two shops."),
        Q(R(BAKERY, "Which of these is NOT stated or supported by the passage?"), "Maman Ruth is the richest woman in the town.",
          [("She uses a wood-fired oven.", "This is stated."), ("Her son offered her an electric oven.", "This is stated."), ("Her loaves are sold out by nine.", "This is stated.")],
          0, "There is no evidence about her wealth.", "Not stated", "Analysis", "Which statement has no evidence in the text?"),
        Q(R(TAXI, "What does Mr Etoa keep to wipe the seats?"), "a small cloth",
          [("an umbrella", "The umbrella is for elderly customers in the rain."), ("a towel and soap", "Only a small cloth is mentioned."), ("a brush", "A brush is not mentioned.")],
          0, "A factual detail: 'he keeps a small cloth to wipe the seats'.", "Factual question", "Recall", "Scan for the word 'wipe'."),
        Q(R(TAXI, "Why does Mr Etoa politely turn away new customers on busy mornings?"), "His regular customers have already booked him.",
          [("He dislikes strangers.", "He is polite, not unfriendly."), ("His taxi is broken.", "Nothing suggests this."), ("He is lazy.", "Nothing suggests this.")],
          0, "Regular customers call him before they travel, so on busy mornings he has no space for new ones. This is an inference.", "Inference", "Comprehension", "Who calls him before they travel?"),
        Q(R(TAXI, "What can be inferred from 'A driver who is clean and calm never needs to look for passengers'?"), "Passengers choose drivers who are clean and calm.",
          [("Passengers do not care about cleanliness.", "That is the opposite."), ("Mr Etoa avoids work.", "He is busy, not avoiding work."), ("Taxis are not needed in the town.", "The passage shows demand.")],
          0, "His own experience is that customers come to him because he is clean and calm.", "Inference", "Analysis", "Why does he never need to look for passengers?"),
        Q("Which question is inferential?", "Why do you think the customers trust Mr Etoa?",
          [("Where does Mr Etoa work?", "The passage states this."), ("How long has he driven a taxi?", "The passage states this."), ("What does he carry for elderly customers?", "The passage states this.")],
          0, "'Why do you think' needs reasoning from clues. The others ask for stated facts.", "Question types", "Concept", "Which question asks you to think beyond the text?"),
    ]))

# ------------------------------------------------------------------ 15. Summary 1
SETS.append(practice_set(
    module=M4, topic="Summary writing", title="Selecting the main points for a summary", lesson="evo-summary-select-points",
    questions=[
        Q("A summary should be", "shorter than the passage and in your own words",
          [("longer than the passage", "A summary shortens the text."), ("a copy of the best sentences", "Copying is called lifting and loses marks."), ("full of your own opinions", "Use only the passage.")],
          0, "A summary keeps the main points in fewer words and in your own words.", "Summary", "Recall", "What does 'short' mean for a summary?"),
        Q("Which of these should usually be left out of a summary?", "examples such as the name of one person and one village",
          [("the main reasons", "These are main points."), ("the main result", "This is a main point."), ("the key facts", "These are main points.")],
          0, "Examples and named details are usually not main points.", "Selecting points", "Concept", "Which is a detail, not a main point?"),
        Q(R(MOBILE, "Task: summarise the dangers of mobile money. Which point should be INCLUDED?"), "Criminals pretending to be agents ask users for secret codes.",
          [("Mr Fon sent money to Wum.", "This is an example from paragraph 1."), ("Parents use it to pay school fees.", "This is an advantage, not a danger."), ("Ten years ago people travelled for six hours.", "This is background.")],
          0, "It is a danger stated in paragraph 3.", "Selecting points", "Application", "Which one is a danger?"),
        Q(R(MOBILE, "Task: summarise the dangers of mobile money. Which point should be LEFT OUT?"), "People save time and transport costs.",
          [("Users sometimes forget to check the amount.", "This is a danger and must be included."), ("The service is of little use where the network is weak.", "This is a danger and must be included."), ("Criminals ask for secret codes.", "This is a danger and must be included.")],
          0, "It is an advantage, so it is not asked for in a task about dangers.", "Task focus", "Analysis", "Which one is not a danger?"),
        Q("Two notes read 'saves time' and 'does not take long'. What should you do?", "Keep one, since they repeat the same idea",
          [("Keep both", "This wastes words."), ("Remove both", "The idea is relevant."), ("Write both in full sentences", "This makes the summary longer.")],
          0, "A repeated idea is counted once.", "Removing repetition", "Application", "Do the two notes add a new idea?"),
        Q(R(PLASTIC, "Task: list the problems caused by plastic bags. Which is a problem and NOT a solution?"), "Blocked drains cause floods.",
          [("Councils should provide bins.", "This is a solution."), ("Shops should charge for bags.", "This is a solution."), ("Citizens should use baskets.", "This is a solution.")],
          0, "Blocked drains and floods are problems. The others are solutions.", "Selecting points", "Application", "Which one is a problem?"),
        Q(R(PLASTIC, "Which problem does the passage link to burning plastic?"), "harmful smoke in the air",
          [("blocked drains", "Blocked drains come from throwing bags into drains."), ("the spread of cholera", "Cholera is linked to flooding."), ("a shortage of bins", "The passage says councils should provide bins, but it does not link this to burning.")],
          0, "The passage says burning plastic fills the air with harmful smoke.", "Selecting points", "Analysis", "Find the sentence about burning."),
        Q("A summary question says 'in not more than 60 words'. A student writes 75 words. What is the problem?", "The limit has been exceeded.",
          [("Nothing; the limit is only a guide", "Limits must be obeyed."), ("The summary is too short", "75 is more than 60."), ("Numbers do not count as words", "They are counted.")],
          0, "A word limit is a maximum. The student must cut to 60 or fewer.", "Word limit", "Concept", "Compare 75 with 60."),
    ]))

# ------------------------------------------------------------------ 16. Summary 2
SETS.append(practice_set(
    module=M4, topic="Summary writing", title="Paraphrasing and writing the summary", lesson="evo-summary-paraphrase-write",
    questions=[
        Q("Which is the best paraphrase of 'Farmers receive payments directly from buyers'?", "Buyers pay farmers directly.",
          [("Farmers receive payments directly from buyers.", "This is a copy (lifting)."), ("Farmers are lucky.", "This adds an opinion."), ("Buyers are paid by farmers.", "This reverses the meaning.")],
          0, "It keeps the meaning, changes the structure and uses fewer words.", "Paraphrase", "Application", "Which one keeps the meaning in different words?"),
        Q("Copying words from the passage without changing them is called", "lifting",
          [("paraphrasing", "Paraphrasing means using different words."), ("skimming", "Skimming is quick reading."), ("scanning", "Scanning is looking for a detail.")],
          0, "Lifting loses marks.", "Lifting", "Recall", "What do we call word-for-word copying?"),
        Q("Which connective is standard English?", "Moreover",
          [("Nextly", "This is not a standard connective."), ("Further still", "This is not a standard connective."), ("More again", "This is not a standard connective.")],
          0, "'Moreover' adds a point. The others are not used in standard English.", "Connectives", "Concept", "Which would you find in a dictionary as a connective?"),
        Q("Which is the best way to shorten 'in order to'?", "to",
          [("so that in order", "This makes it longer."), ("order to", "This is wrong."), ("in to", "This is wrong.")],
          0, "'In order to' can be shortened to 'to'.", "Cutting words", "Application", "Which one-word version keeps the meaning?"),
        Q("A summary is normally written as", "one paragraph of continuous prose",
          [("a list with numbers", "A list is not continuous prose."), ("several short paragraphs with headings", "Headings are not used."), ("a table", "A table is not continuous prose.")],
          0, "A summary is usually one paragraph of full sentences unless the task says otherwise.", "Form of a summary", "Recall", "Does the task ask for a list?"),
        Q("Which is the best paraphrase of 'Some people lose money to criminals who pretend to be agents'?", "Criminals posing as agents steal money from some users.",
          [("Some people lose money to criminals who pretend to be agents.", "This is a copy."), ("Criminals are agents.", "This changes the meaning."), ("Agents lose money to criminals.", "This changes the meaning.")],
          0, "It uses different words and a different structure and keeps the meaning.", "Paraphrase", "Application", "Which keeps the meaning and changes the words?"),
        NUM("Count the words in this summary: 'Plastic bags block drains, so rain floods roads and houses and spreads disease. Burning them also pollutes the air with harmful smoke.'", 22,
            steps=[S("Count each word", text="Plastic(1) bags(2) block(3) drains,(4) so(5) rain(6) floods(7) roads(8) and(9) houses(10) and(11) spreads(12) disease.(13) Burning(14) them(15) also(16) pollutes(17) the(18) air(19) with(20) harmful(21) smoke.(22)"),
                   S("Total", text="22 words.")],
            tolerance=0, unit="words", concept="Word count", skill="Calculation", hint="Count each word, including 'and' and 'so'.",
            feedback="Every word counts, including small words."),
        Q("Which sentence belongs in a good summary?", "Mobile money lets people send, store and pay money by phone.",
          [("In my opinion, mobile money is the best invention.", "A summary has no personal opinion."), ("Mr Fon sent money to his mother in Wum.", "This is an example, not a main point."), ("Ten years ago, journeys were tiring.", "This is background.")],
          0, "It states the main idea in general terms, with no opinion and no example.", "Writing the summary", "Analysis", "Which sentence is a general point from the passage?"),
    ]))
