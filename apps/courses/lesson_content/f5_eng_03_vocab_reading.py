"""Form 5 English Language: Vocabulary, Semantics & Register, and Reading Comprehension & Summary (16 lessons)."""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "form-5")

M3 = "Vocabulary, Semantics & Register"
M4 = "Reading Comprehension & Summary"

LESSONS = []

# ------------------------------------------------------------------ 1. Prefixes and suffixes
LESSONS.append(lesson(
    module=M3, topic="Word formation",
    title="Prefixes, suffixes and roots",
    slug="evo-prefixes-suffixes-roots",
    minutes=20,
    summary="Many English words are built from a root with a prefix in front or a suffix at the end. Knowing the parts helps you guess new words, form the right word class and spell correctly.",
    objectives=[
        "Name the root, prefix and suffix in a word",
        "Use common prefixes to change meaning (for example un-, dis-, mis-, re-, im-)",
        "Use common suffixes to change word class (noun, adjective, verb, adverb)",
        "Apply the main spelling changes when a suffix is added",
    ],
    key_concepts=["Root (base)", "Prefix", "Suffix", "Word class", "Spelling change"],
    blocks=[
        H("Introduction"),
        T("A trader in Bafoussam sells a TV on credit. The buyer is **unable** to pay, so the trader is **unhappy**. Later the buyer "
          "**repays** the money. Look at the words in bold. Each one is built from a smaller word with "
          "a part added at the front or at the end."),
        T("English builds thousands of words this way. If you know the parts, you can work out words you have never seen. "
          "Examiners also test the right form of a word, for example choosing between careful, carefully and care in a gap."),
        D("The **root** (or **base**) is the main part of a word that carries its basic meaning, such as *happy* in *unhappiness*.",
          title="Root (base)"),
        D("A **prefix** is a group of letters added at the **front** of a word. It usually changes the meaning but not the word class. "
          "Example: *un* + *happy* = *unhappy* (still an adjective).", title="Prefix"),
        D("A **suffix** is a group of letters added at the **end** of a word. It often changes the word class. "
          "Example: *happy* + *ness* = *happiness* (an adjective becomes a noun).", title="Suffix"),
        IMG("f5en-vo-word-parts.svg", alt="The word unhappiness split into prefix un, root happy and suffix ness",
            caption="Figure 1. The word unhappiness has three parts. The root happy keeps its meaning."),
        H("Common prefixes"),
        KEY("Prefixes that mean 'not' or 'the opposite'", "These make a negative meaning. Choose the one that matches the word.", cards=[
            ["un-", "unkind, unfair, unlock, untie"],
            ["dis-", "disagree, dislike, disappear, dishonest"],
            ["in- (im-, il-, ir-)", "incorrect, impossible, illegal, irregular"],
            ["non-", "nonsense, non-stop, non-smoker"],
        ]),
        T("The prefix **in-** changes its spelling to match the next letter. It becomes **im-** before b, m or p (*impossible*, *immature*, "
          "*imbalance*). It becomes **il-** before l (*illegal*) and **ir-** before r (*irregular*). The spelling of the root does not change."),
        KEY("Other useful prefixes", "These add other kinds of meaning.", cards=[
            ["re-", "again: rewrite, rebuild, repay"],
            ["mis-", "wrongly or badly: misspell, mislead, misuse"],
            ["pre-", "before: preview, prepaid, prehistoric"],
            ["over- / under-", "too much / too little: overcook, underpaid"],
            ["anti-", "against: antibiotic, anti-corruption"],
            ["inter-", "between: international, interschool"],
            ["sub-", "under or below: subway, subtitle"],
            ["co-", "together: co-operate, co-author"],
        ]),
        H("Common suffixes"),
        T("A suffix tells you what kind of word you have. This is very useful in gap-filling questions."),
        KEY("Suffixes that make nouns", "They name a person, a quality, an action or a state.", cards=[
            ["-er, -or, -ist (a person)", "teacher, actor, scientist"],
            ["-tion, -ment, -ance (an action or result)", "education, payment, performance"],
            ["-ness, -ity (a quality)", "kindness, honesty, ability"],
            ["-hood, -ship (a state)", "childhood, friendship"],
        ]),
        KEY("Suffixes that make adjectives, verbs and adverbs", "Look at the end of a gap word to see which class is needed.", cards=[
            ["Adjective: -ful, -less, -able, -ous, -ive, -al, -y", "helpful, hopeless, readable, dangerous, active, national, rainy"],
            ["Verb: -ise (-ize), -ify, -en, -ate", "modernise, simplify, widen, educate"],
            ["Adverb: -ly", "slowly, carefully, happily"],
        ]),
        H("Spelling changes"),
        T("Most of the time you simply join the parts. A few small changes are common."),
        CODE("""Rule                         Example
Drop a silent e              create + ion = creation
                             hope + ing = hoping
Change y to i                happy + ness = happiness
(after a consonant)          carry + ed = carried
Double the last letter       begin + ing = beginning
(short stressed vowel)       stop + ed = stopped
Keep the e before -ment      manage + ment = management
and -ful or -ly              care + ful = careful""", "text", title="Main spelling changes"),
        EX("Worked example 1: building words", intro="Build a noun, an adjective and an adverb from the verb or base given.", steps=[
            S("Start with the base", text="Base word: agree (verb)."),
            S("Add a suffix to make a noun", text="agree + ment = agreement. The silent e is kept before -ment."),
            S("Add a prefix for the opposite", text="dis + agree = disagree. The root does not change."),
            S("Make an adjective", text="agree + able = agreeable. The double e stays."),
            S("Make an adverb", text="agreeable becomes agreeably (able changes to ably)."),
        ]),
        EX("Worked example 2: choose the right form", intro="Complete the sentence with the correct form of the word in brackets. "
           "'Mama Rose is a very ______ (care) driver; she drives ______ (care) on the wet road to Buea.'", steps=[
            S("Look at the first gap", text="The gap comes before the noun 'driver'. A word that describes a noun is an adjective."),
            S("Form the adjective", text="care + ful = careful."),
            S("Look at the second gap", text="The gap tells how she drives. A word that describes a verb is an adverb."),
            S("Form the adverb", text="careful + ly = carefully."),
            S("Answer", text="Mama Rose is a very careful driver; she drives carefully on the wet road to Buea."),
        ]),
        MISTAKE("Changing the meaning with the wrong prefix", "Not every negative prefix fits every word. We say impossible, not unpossible, and "
                "dishonest, not unhonest. If you are not sure, use a dictionary. Learn the pairs as whole words."),
        MISTAKE("Forgetting the spelling change", "Write happiness, not happyness; beginning, not begining; hoping, not hopping "
                "(hopping comes from hop). Check the last letter of the root before you add the suffix."),
        TIP("In Paper 1 (multiple choice), a vocabulary or grammar question may leave a gap and give four forms of one word. Read the "
            "words around the gap first and decide the word class you need: noun, adjective, verb or adverb. Then pick the form with the matching ending."),
        QUIZ("Which word correctly completes the sentence? 'The judge said the evidence was ______.'",
             ["unlegal", "illegal", "inlegal", "dislegal"], 1,
             "Before the letter l, the prefix in- becomes il-: illegal.",
             hint="Look at the first letter of the root and think about how in- changes.",
             feedback=["There is no word 'unlegal' in standard English.", "", "The prefix in- changes to il- before l.",
                       "Dis- gives the meaning 'the opposite of an action' (dislike), not this word."]),
        QUIZ("The word 'kindness' is formed from 'kind'. What did the suffix -ness do?",
             ["It changed the word from an adjective to a noun", "It changed the word from a noun to a verb",
              "It changed the meaning to its opposite", "It did not change anything"], 0,
             "Kind is an adjective. Adding -ness makes a noun that names the quality.",
             hint="Ask what class of word kind is, then what class kindness is.",
             feedback=["", "Kindness is not a verb: we cannot say 'he kindnesses'.",
                       "Opposites come from prefixes like un- (unkind), not from -ness.", "The class changed from adjective to noun."]),
        PQ("Split these words into prefix, root and suffix: (a) unhelpful (b) rebuilding (c) disagreement.",
           "(a) un + help + ful. (b) re + build + ing. (c) dis + agree + ment."),
        PQ("Write the correct form of the word in brackets. (a) She spoke very ______ (polite) to the visitor. (b) The ______ (educate) of girls is important. (c) The river is too deep, so it is ______ (possible) to cross.",
           "(a) politely (adverb: it describes how she spoke). (b) education (noun after the). (c) impossible (the prefix in- becomes im- before p; 'too deep' shows the negative meaning)."),
        PQ("Add a suffix to make the word a noun for a person: teach, act, science.",
           "teacher (teach + er), actor (act + or), scientist (science + ist; the e is dropped)."),
        SUM("A word can have a root, a prefix at the front and a suffix at the end.",
            "A prefix usually changes the meaning; a suffix often changes the word class.",
            "The prefix in- becomes im-, il- or ir- before b/m/p, l and r.",
            "Common spelling changes: drop silent e, change y to i, double the last letter.",
            "In gap-filling, find the word class first, then choose the matching form."),
    ],
))

# ------------------------------------------------------------------ 2. Compounds, conversion
LESSONS.append(lesson(
    module=M3, topic="Word formation",
    title="Compounding, conversion, blending and shortening",
    slug="evo-compounds-conversion",
    minutes=20,
    summary="New words also come from joining two words (compounding), using a word in a new class (conversion), merging parts (blending) and shortening. Learn the hyphen rule for compound adjectives.",
    objectives=[
        "Form and recognise compound nouns and compound adjectives",
        "Use hyphens correctly in compound adjectives before a noun",
        "Explain conversion, blending, clipping and acronyms with examples",
        "Choose the correct word form in a sentence",
    ],
    key_concepts=["Compound word", "Hyphen", "Conversion", "Blend", "Clipping", "Acronym"],
    blocks=[
        H("Introduction"),
        T("Think about words you use every day: *classroom*, *mobile phone*, *well-known*, *brunch*, *text* (as in 'text me'), *ATM*. "
          "None of them is built with a prefix or a suffix. They come from other ways of making new words. "
          "This lesson explains four of these ways."),
        H("Compounding"),
        D("A **compound word** is made by joining two or more words to make one new word with its own meaning.", title="Compound word"),
        T("Compounds are written in three ways. Some are written as one word (classroom, football, bedroom). Some use a hyphen "
          "(mother-in-law, check-in, well-known). Some are written as two words (bus stop, post office, living room). "
          "There is no single rule, so check your dictionary when you are not sure."),
        KEY("Common patterns", "The last word usually tells you what kind of thing it is.", cards=[
            ["noun + noun", "schoolbag, bus stop, mobile money"],
            ["adjective + noun", "blackboard, highway, greenhouse"],
            ["verb + noun", "washing machine, playground"],
            ["adverb or preposition + word", "overcoat, income, outlook"],
        ]),
        H("Compound adjectives and the hyphen"),
        T("When two or more words work together as one adjective **before a noun**, they are joined with hyphens. "
          "The same group after the verb is usually written without them."),
        CODE("""Before the noun            After the verb
a well-known author        The author is well known.
a ten-year-old boy         The boy is ten years old.
a part-time job            She works part time.
a hard-working student     The student is hard working.""", "text", title="Hyphens in compound adjectives"),
        T("Notice that in 'a ten-year-old boy' the word *year* stays singular. We say 'a ten-year-old boy', not 'a ten-years-old boy'."),
        H("Conversion"),
        D("**Conversion** means using the same word in a different word class without changing its spelling.", title="Conversion"),
        T("Examples: *a book* (noun) and *to book a seat* (verb). *Water* (noun) and *to water the garden* (verb). "
          "*A text* and *to text a friend*. *A cool drink* (adjective) and *to cool the drink* (verb). "
          "The sentence around the word shows which class it has."),
        H("Blending and shortening"),
        KEY("Other ways to make words", "Each of these is common in newspapers and exams.", cards=[
            ["Blending (joining parts of two words)", "breakfast + lunch = brunch; smoke + fog = smog; motor + hotel = motel"],
            ["Clipping (cutting a long word)", "examination = exam; telephone = phone; influenza = flu"],
            ["Acronym (made from first letters, said as a word)", "UNESCO, NATO"],
            ["Initialism (first letters, said letter by letter)", "ATM, GCE, SIM"],
        ]),
        T("Textbooks differ in how they name the last two. Some use *acronym* for both. In this course, an acronym is said as a word "
          "and an initialism is said letter by letter. Check your textbook."),
        EX("Worked example 1: compound adjective", intro="Rewrite the sentence using a compound adjective before the noun: "
           "'The girl is twelve years old.'", steps=[
            S("Identify the pattern", text="number + year + old describes the noun 'girl'."),
            S("Join with hyphens and use the singular year", text="twelve-year-old."),
            S("Put it before the noun", text="She is a twelve-year-old girl."),
            S("Check", text="No s on year. Hyphens join all three words."),
        ]),
        EX("Worked example 2: identify the process", intro="Name the process that formed each word: (a) smog, (b) bike, (c) motel, (d) greenhouse.", steps=[
            S("(a) smog", text="smoke + fog, with parts of each word joined: blending."),
            S("(b) bike", text="From bicycle: clipping."),
            S("(c) motel", text="motor + hotel: blending."),
            S("(d) greenhouse", text="green + house: compounding (adjective + noun)."),
        ]),
        MISTAKE("Pluralising the number word", "Write 'a five-day course', not 'a five-days course'. In a hyphenated adjective, the noun part stays singular."),
        MISTAKE("Using a hyphen after the noun", "Write 'The report is well written', not 'The report is well-written' (some dictionaries allow it, so check). Before the noun, use the hyphen: 'a well-written report'."),
        TIP("Vocabulary and grammar items in Paper 1 sometimes show a sentence and ask which word is a verb (or a noun). Look at the position "
            "and the words around it: after 'to' or after a subject, a word is a verb; after 'a', 'the' or an adjective, it is a noun."),
        QUIZ("Which sentence is correct?", ["She has a three-years-old daughter.", "She has a three-year-old daughter.",
             "She has a three years-old daughter.", "She has a three-year old daughter."], 1,
             "In a compound adjective before a noun, all parts are joined by hyphens and the noun part (year) stays singular.",
             hint="Which version joins the whole expression and keeps year singular?",
             feedback=["Year must stay singular in the compound adjective.", "",
                       "The hyphen is in the wrong place.", "The hyphen before old is missing."]),
        QUIZ("In which sentence is the word 'water' a verb?",
             ["The water in the well is cold.", "Please water the beans before noon.", "Drink more water every day.", "The water level is rising."], 1,
             "After 'please', 'water' is an action word (to water). In the other sentences it names a thing.",
             hint="Ask what the word is doing in the sentence: naming a thing or showing an action.",
             feedback=["Here water is a noun.", "", "Here water is a noun.", "Here water names a thing that has a level; it is not an action."]),
        PQ("Rewrite using a compound adjective: (a) 'a lesson that lasts forty minutes' (b) 'a man who works hard'.",
           "(a) a forty-minute lesson. (b) a hard-working man."),
        PQ("Give the full word for each clipped form: exam, phone, flu.",
           "examination, telephone, influenza."),
        PQ("Use the word 'text' once as a noun and once as a verb in two sentences.",
           "Noun: I received a text from my sister. Verb: Please text me when you arrive."),
        SUM("A compound word joins two or more words; check the dictionary for spelling.",
            "Compound adjectives before a noun take hyphens and a singular noun part.",
            "Conversion changes the class of a word without changing its spelling.",
            "Blending, clipping, acronyms and initialisms are other ways to make words.",
            "Use the position of a word in the sentence to decide its class."),
    ],
))

# ------------------------------------------------------------------ 3. Synonyms and antonyms
LESSONS.append(lesson(
    module=M3, topic="Synonyms, antonyms and homonyms",
    title="Synonyms and antonyms",
    slug="evo-synonyms-antonyms",
    minutes=20,
    summary="Synonyms are words with nearly the same meaning and antonyms have opposite meanings. Learn to choose the best word for the context, because synonyms are rarely exactly equal.",
    objectives=[
        "Define synonym and antonym and give examples",
        "Choose the synonym that fits the context, tone and formality",
        "Recognise three kinds of antonym",
        "Avoid false opposites such as flammable and inflammable",
    ],
    key_concepts=["Synonym", "Antonym", "Connotation", "Gradable antonym", "Context"],
    blocks=[
        H("Introduction"),
        T("A seller in Douala says her mangoes are 'cheap'. A buyer says the price is 'reasonable'. Another seller says his are "
          "'inexpensive'. Each word speaks about low price, yet each gives a slightly different feeling. 'Cheap' can also mean poor in quality, "
          "so a seller may avoid it. This is the main idea of the lesson: words with similar meanings are not always interchangeable."),
        D("A **synonym** is a word that has the same or nearly the same meaning as another word in a given context.", title="Synonym"),
        D("An **antonym** is a word that has the opposite meaning to another word.", title="Antonym"),
        H("Using synonyms well"),
        T("Three things decide whether a synonym fits."),
        KEY("Choosing a synonym", "Check all three before you decide.", cards=[
            ["Meaning in context", "'Fast' and 'quick' both fit 'a fast runner'. But 'a quick reply' is more natural than 'a fast reply'."],
            ["Feeling (connotation)", "'Slim' is a compliment. 'Skinny' can sound rude. 'Thrifty' is positive; 'stingy' is negative."],
            ["Formality", "'Begin' is neutral, 'commence' is formal, 'kick off' is informal."],
        ]),
        CODE("""Word      Synonyms (different strength)
big       large, huge, enormous
small     little, tiny, minute
walk      stroll, march, stagger
said      replied, shouted, whispered
happy     glad, cheerful, delighted, overjoyed""", "text", title="Synonyms differ in strength"),
        T("When an exam asks for 'the word closest in meaning' to an underlined word, use the whole sentence. "
          "Try each choice in the gap and check that the sentence still has the same meaning."),
        H("Kinds of antonyms"),
        KEY("Three kinds of opposite", "Knowing the kind helps you decide whether a middle position exists.", cards=[
            ["Gradable (a scale between them)", "hot / cold, rich / poor, big / small. There is warm, cool, average between them."],
            ["Complementary (one or the other)", "alive / dead, true / false, present / absent. No middle position."],
            ["Relational (one needs the other)", "buy / sell, teacher / student, parent / child, give / receive."],
        ]),
        T("Many antonyms are made with a prefix (*kind / unkind*, *possible / impossible*). But not all opposites work this way. "
          "The opposite of *rich* is *poor*, not *unrich*. And a few words with a prefix do not give the opposite: "
          "*flammable* and *inflammable* mean the same thing (easily set on fire); the opposite is *non-flammable*."),
        EX("Worked example 1: closest in meaning", intro="'The headmaster was furious when he saw the broken window.' Which word is closest in meaning to 'furious'? "
           "(A) amused (B) very angry (C) surprised (D) disappointed", steps=[
            S("Read the sentence", text="A headmaster sees a broken window. A strong feeling of anger is likely."),
            S("Test each choice", text="Amused means finding something funny. Surprised and disappointed are weaker, and neither says how strong the feeling is."),
            S("Choose", text="Furious means extremely angry: option B."),
        ]),
        EX("Worked example 2: opposite in meaning", intro="'The old market road is narrow, but the new one is ______.' Choose the antonym of 'narrow'.", steps=[
            S("Decide the kind of antonym", text="Narrow and wide are gradable opposites: width is on a scale."),
            S("Find the word", text="The opposite of narrow is wide (or broad)."),
            S("Check in the sentence", text="'The old market road is narrow, but the new one is wide.' The sentence makes sense."),
        ]),
        MISTAKE("Treating synonyms as exactly equal", "Do not replace a word without checking the sentence. 'The doctor was thin' and 'The doctor was skinny' do not "
                "carry the same attitude. 'Extremely tall' is not the same as 'tall'."),
        MISTAKE("Choosing a word that is only related", "A related word is not a synonym. 'Doctor' and 'hospital' go together but do not mean the same. "
                "Ask: can I replace the word and keep the meaning?"),
        TIP("In Paper 1 (multiple choice), vocabulary questions on synonyms and antonyms are usually set in a sentence. Read the whole sentence, eliminate "
            "choices that change the meaning or tone, and test the last choice in the gap."),
        QUIZ("Which word is closest in meaning to 'reluctant' in: 'The boy was reluctant to speak in front of the class'?",
             ["unwilling", "eager", "unable", "ready"], 0,
             "Reluctant means not wanting to do something; unwilling has the same sense.",
             hint="If he is reluctant, does he want to speak or not?",
             feedback=["", "Eager means very keen, the opposite.", "Unable means cannot; reluctant means does not want to.",
                       "Ready means prepared; it does not show unwillingness."]),
        QUIZ("Which pair is a pair of complementary antonyms (no middle position)?",
             ["hot and cold", "buy and sell", "rich and poor", "true and false"], 3,
             "A statement is either true or false: there is no middle. Hot/cold and rich/poor are gradable, and buy/sell are relational.",
             hint="Ask: is there something in between?",
             feedback=["Warm and cool lie between hot and cold.", "Buy and sell depend on each other (relational).", "A person can be neither rich nor poor.", ""]),
        PQ("Give a synonym for each word in the sentence: 'The teacher was *pleased* with the *brave* pupils.'",
           "pleased: glad, happy or satisfied. brave: courageous or bold. Check that the sentence still fits."),
        PQ("Write an antonym for each: generous, ancient, success, expand.",
           "generous: mean or stingy. ancient: modern. success: failure. expand: shrink or contract."),
        PQ("Why is 'inflammable' not the opposite of 'flammable'? Give the real opposite.",
           "In 'inflammable' the in- is not a negative prefix; the word means easily set on fire, the same as flammable. The opposite is non-flammable."),
        SUM("Synonyms have nearly the same meaning; they differ in strength, feeling and formality.",
            "Always test a synonym inside the sentence.",
            "Antonyms can be gradable, complementary or relational.",
            "A prefix does not always make an opposite (flammable and inflammable).",
            "Eliminate choices that change the meaning or tone."),
    ],
))

# ------------------------------------------------------------------ 4. Homonyms
LESSONS.append(lesson(
    module=M3, topic="Synonyms, antonyms and homonyms",
    title="Homonyms, homophones, homographs and words with many meanings",
    slug="evo-homonyms-homophones",
    minutes=20,
    summary="Some words look or sound the same but differ in meaning. Learn the terms homonym, homophone and homograph, and use the sentence to decide which meaning is meant.",
    objectives=[
        "Define homonym, homophone and homograph",
        "Use context to choose the correct meaning of a word",
        "Spell common homophones correctly",
        "Tell a word with many related senses from two different words",
    ],
    key_concepts=["Homonym", "Homophone", "Homograph", "Polysemy", "Context"],
    blocks=[
        H("Introduction"),
        T("On a school notice board in Bamenda you read: 'The match will begin at 3 p.m.' A little later a girl tells her friend: 'I need a match to light the stove.' "
          "The word *match* is spelt and sounds the same, but the meanings are very different. English has many such words."),
        D("**Homonyms** are words that have the same spelling and the same sound but different meanings. Example: *bank* (where money is kept) "
          "and *bank* (the side of a river).", title="Homonym"),
        D("**Homophones** are words that sound the same but have different spellings and meanings. Example: *write* and *right*.", title="Homophone"),
        D("**Homographs** are words that are spelt the same but have different meanings and may be pronounced differently. Example: *lead* "
          "(to guide) and *lead* (a metal).", title="Homograph"),
        T("Textbooks differ in how they use these terms. Some use *homonym* for all three. Check your textbook and your teacher."),
        H("Homonyms: same spelling, same sound"),
        CODE("""bank       the side of a river / a place for money
bat        a stick for hitting a ball / a flying animal
bear       a large animal / to carry or to tolerate
light      not heavy / not dark
match      a game / a stick for making fire
fair       just / a market or show / pale in colour""", "text", title="Common homonyms"),
        T("Only the sentence can tell you which meaning is used: 'He could not bear the noise' (tolerate). 'A bear came out of the forest' (animal)."),
        H("Homophones: same sound, different spelling"),
        CODE("""write / right       their / there / they're
two / too / to      piece / peace
new / knew          hear / here
whole / hole        weak / week
sea / see           buy / by / bye
principal / principle   stationary / stationery""", "text", title="Common homophones"),
        KEY("Memory help", "A short trick for a few pairs.", cards=[
            ["stationary / stationery", "Stationery with an e is for envelopes. Stationary with an a means standing still."],
            ["principal / principle", "The principal is a person (the head). A principle is a rule or belief."],
            ["their / there / they're", "their = belonging to them. there = a place. they're = they are."],
        ]),
        H("Homographs and one word with many meanings"),
        T("Some words are spelt the same but pronounced differently. The sound depends on the meaning: *tear* (a drop from the eye) and "
          "*tear* (to rip); *wind* (moving air) and *wind* (to turn); *lead* (to guide) and *lead* (the metal)."),
        T("Many words have several related meanings. This is called **polysemy**. The word *head* means a part of the body, a leader (the head of the school) and the top of a page. "
          "A dictionary usually lists related meanings under one entry. Words with unrelated meanings (the two senses of *bank*) have separate entries."),
        EX("Worked example 1: choose the meaning", intro="'The farmer kept the cattle close to the river bank.' What does 'bank' mean here?", steps=[
            S("Read the clues", text="The words 'river' and 'cattle' point to land and water."),
            S("Reject the other meaning", text="A place for money does not fit a river."),
            S("Answer", text="Bank means the land at the side of the river."),
        ]),
        EX("Worked example 2: choose the homophone", intro="Complete each sentence. (a) 'The ______ of the school welcomed the guests.' (principal / principle) "
           "(b) 'We buy pens and envelopes at the ______ shop.' (stationary / stationery)", steps=[
            S("(a) Decide the meaning", text="A person who welcomes guests and leads a school is the principal."),
            S("(b) Decide the meaning", text="A shop that sells pens, paper and envelopes is a stationery shop (with an e)."),
            S("Answer", text="(a) principal (b) stationery."),
        ]),
        MISTAKE("Spelling by sound only", "Their/there and two/too/to sound alike. Choose the spelling by meaning, not by sound: 'They left their bags there.'"),
        MISTAKE("Mixing up advice and advise", "Advice (noun, with an s sound) and advise (verb, with a z sound) are not homophones. "
                "Say: 'I need advice' and 'Please advise me'. In British spelling the same applies to practice (noun) and practise (verb)."),
        TIP("Paper 1 may give a sentence with a gap and four homophones, or ask which sentence uses a word in a different sense. Always check the meaning "
            "of the whole sentence, not just the word."),
        QUIZ("Which sentence uses the correct word?",
             ["The principle of our school is a kind man.", "She forgot to bring her stationary.", "He gave good advice to the new pupils.", "The whether was very cold."], 2,
             "'Advice' is a noun. The other sentences confuse principle/principal, stationery/stationary and whether/weather.",
             hint="Check each sentence by the meaning of the word.",
             feedback=["A person is a principal (a principle is a rule).", "Pens and paper are stationery (stationary means still).", "",
                       "Weather is about rain and sun; whether means if."]),
        QUIZ("In which pair of sentences does 'light' have the same meaning?",
             ["'Switch on the light.' / 'The box is light.'", "'The box is light.' / 'She carried a light bag.'",
              "'He chose a light colour.' / 'The light is bright.'", "'We travelled light.' / 'The light changed to green.'"], 1,
             "In the second pair, light means not heavy in both sentences.",
             hint="First write the meaning in each sentence, then compare.",
             feedback=["The first means brightness; the second means not heavy.", "",
                       "The first means pale; the second means brightness.", "The first means with little baggage; the second is a signal."]),
        PQ("Write two sentences to show two meanings of 'match'.", "A sample answer: 'We watched the football match.' 'He struck a match to light the lamp.'"),
        PQ("Complete with the correct homophone: (a) 'We went to the ______ (see/sea) at Limbe.' (b) 'I ______ (new/knew) the answer.'",
           "(a) sea (the place with water). (b) knew (the past of know)."),
        PQ("Explain the difference between 'homophone' and 'homograph'.",
           "Homophones sound the same but have different spellings (write, right). Homographs are spelt the same but have different meanings and may sound different (tear, tear)."),
        SUM("Homonyms: same spelling and sound, different meaning.",
            "Homophones: same sound, different spelling.",
            "Homographs: same spelling, different meaning (sometimes a different sound).",
            "Many words have several related meanings (polysemy).",
            "Choose by meaning in the sentence, not by sound."),
    ],
))

# ------------------------------------------------------------------ 5. Idioms and proverbs
LESSONS.append(lesson(
    module=M3, topic="Idiomatic expressions and proverbs",
    title="Idioms and proverbs: meaning and use",
    slug="evo-idioms-proverbs",
    minutes=22,
    summary="An idiom is a fixed phrase whose meaning is different from its words. A proverb is a short well-known saying that gives advice. Learn common ones and use them in the right situation.",
    objectives=[
        "Explain what an idiom and a proverb are",
        "Give the meaning of common idioms and proverbs",
        "Use idioms correctly without changing their words",
        "Choose the idiom or proverb that fits a situation",
    ],
    key_concepts=["Idiom", "Proverb", "Literal meaning", "Figurative meaning", "Fixed expression"],
    blocks=[
        H("Introduction"),
        T("A father in Kumba tells his son who has not yet started revising: 'Make hay while the sun shines.' The boy does not "
          "go to cut grass. He understands: use your time well while the chance is there. The saying means something different from its words."),
        D("An **idiom** is a fixed group of words whose meaning is different from the meaning of the separate words. "
          "Example: *spill the beans* means to reveal a secret.", title="Idiom"),
        D("A **proverb** is a short, well-known saying that states a piece of advice or a general truth. Example: *Honesty is the best policy.*", title="Proverb"),
        T("A proverb is a full sentence that people say as wisdom. An idiom is usually a phrase that fits into a sentence, and its form may change a little "
          "(for example the verb tense)."),
        H("Common idioms"),
        CODE("""Idiom                       Meaning
a piece of cake             very easy
break the ice               start a conversation in a tense situation
hit the nail on the head    say exactly the right thing
under the weather           slightly ill
spill the beans             reveal a secret
let the cat out of the bag  reveal a secret by mistake
once in a blue moon         very rarely
cost an arm and a leg       be very expensive
in hot water                in trouble
on cloud nine               extremely happy
beat about the bush         avoid the main point
burn the midnight oil       work or study late at night
call it a day               stop working
a blessing in disguise      a good thing that seemed bad at first
see eye to eye              agree
get cold feet               become afraid before an important action
pull someone's leg          tease someone""", "text", title="Idioms with meanings"),
        T("Some idioms are informal (for example *kick the bucket*, meaning to die, which is rude in formal writing). Use informal idioms only in "
          "informal speech or dialogue."),
        H("Common proverbs"),
        CODE("""Proverb                                        Meaning
A stitch in time saves nine.                   Fix a small problem early.
Look before you leap.                          Think before you act.
Where there is a will, there is a way.         A determined person finds a way.
Too many cooks spoil the broth.                Too many people on one job spoil it.
A bird in the hand is worth two in the bush.   Keep what you have.
Do not count your chickens before they hatch.  Do not plan on results not yet certain.
Actions speak louder than words.               What you do matters more than what you say.
Practice makes perfect.                        Repeating improves skill.
Birds of a feather flock together.             People with alike habits stay together.
Haste makes waste.                             Hurrying produces mistakes.
Every cloud has a silver lining.               Even bad times have something good.
United we stand, divided we fall.              People are strong together.
A friend in need is a friend indeed.           A true friend helps in trouble.
All that glitters is not gold.                 Things that look good may not be.
It is no use crying over spilt milk.           Do not regret what cannot be changed.""", "text", title="Proverbs with meanings"),
        T("A few sayings are understood differently in different places. For example, 'A rolling stone gathers no moss' is "
          "read by some as praise for staying active and by others as a warning against moving often. Check your dictionary. "
          "'It takes a village to raise a child' is widely quoted as an African proverb, but its exact source is debated. Check your dictionary or textbook too."),
        H("Rules for using them"),
        KEY("Four rules", "These protect you from the commonest errors.", cards=[
            ["Do not change the words", "Say 'a piece of cake', not 'a slice of cake'."],
            ["Match the situation", "A proverb about haste is wrong for a case of delay."],
            ["Do not overuse them", "One well-chosen idiom in a composition is better than five forced ones."],
            ["Match the tone", "Avoid slang idioms in a formal letter."],
        ]),
        EX("Worked example 1: meaning in context", intro="'After the quarrel, it was a blessing in disguise that Ako and Neba stopped working together.' "
           "What does 'a blessing in disguise' mean here?", steps=[
            S("Do not use the literal words", text="No one is holding a blessing in disguise."),
            S("Look at the situation", text="The quarrel looked bad, but ending the partnership turned out to be good."),
            S("Answer", text="Something that seemed bad at first turned out to be good."),
        ]),
        EX("Worked example 2: choose a proverb", intro="A student leaves her revision until the night before the exam and makes many mistakes. "
           "Which proverb suits: 'Haste makes waste' or 'A friend in need is a friend indeed'?", steps=[
            S("Match the situation", text="The problem is hurry and late work."),
            S("Test the proverbs", text="'Haste makes waste' is about mistakes from hurrying. The other is about friendship."),
            S("Answer", text="Haste makes waste."),
        ]),
        MISTAKE("Changing a word or mixing two expressions", "Do not say 'to hit the nail in the head' or 'a stitch in time saves ten'. Learn the whole expression exactly."),
        MISTAKE("Taking an idiom literally", "'Under the weather' does not mean outside in the rain. Look at the sentence and think of the figurative meaning."),
        TIP("Paper 1 (multiple choice) can give an idiom or proverb in a sentence and ask for its meaning, or ask you to choose the one that fits. "
            "Learn each in a short sentence of your own. In essays, use a proverb only when it supports your point."),
        QUIZ("'I was under the weather on Monday, so I stayed in bed.' What does 'under the weather' mean?",
             ["standing in the rain", "slightly ill", "very busy", "afraid of the storm"], 1,
             "Under the weather means feeling slightly ill.",
             hint="Why would someone stay in bed?",
             feedback=["That is the literal reading, which is wrong for an idiom.", "", "A busy person would not stay in bed.", "Fear is not suggested."]),
        QUIZ("Which proverb best fits a team of nine people arguing about how to cook one pot of rice?",
             ["Practice makes perfect.", "Too many cooks spoil the broth.", "Look before you leap.", "Haste makes waste."], 1,
             "Too many people working on the same job can spoil it.",
             hint="Look for the proverb about many people doing one task.",
             feedback=["That is about repeating to improve.", "", "That is about thinking before acting.", "That is about hurrying."]),
        PQ("Explain the meaning of each: (a) a piece of cake (b) once in a blue moon (c) cost an arm and a leg.",
           "(a) something very easy. (b) very rarely. (c) very expensive."),
        PQ("Write one sentence with 'break the ice' to show you know the meaning.",
           "Sample: 'She told a joke to break the ice at the start of the meeting.'"),
        PQ("Choose the proverb for this case: 'A boy has a small job that is sure, but he leaves it for a big offer that may not come.'",
           "A bird in the hand is worth two in the bush (keep what you have instead of risking it for something uncertain)."),
        SUM("An idiom is a fixed phrase with a figurative meaning.",
            "A proverb is a short saying that gives advice or a general truth.",
            "Do not change the words of an idiom or proverb.",
            "Use the situation to choose the right one and check that the tone fits.",
            "Where meanings differ by region, check your dictionary."),
    ],
))

# ------------------------------------------------------------------ 6. Figurative language
LESSONS.append(lesson(
    module=M3, topic="Figurative language in context",
    title="Figures of speech and their effects",
    slug="evo-figurative-language",
    minutes=22,
    summary="Writers use figures of speech such as simile, metaphor and personification to make ideas vivid. Learn to identify each one in a sentence and to explain its effect.",
    objectives=[
        "Identify simile, metaphor, personification, hyperbole, irony and understatement",
        "Identify oxymoron, onomatopoeia, alliteration and euphemism",
        "Explain the effect of a figure of speech in context",
        "Tell a figure of speech from a literal statement",
    ],
    key_concepts=["Simile", "Metaphor", "Personification", "Hyperbole", "Irony", "Effect"],
    blocks=[
        H("Introduction"),
        T("A trader in Mokolo says: 'My shop is a beehive on market day.' Nobody thinks there are bees in the shop. "
          "She is comparing her shop to a beehive to show that it is crowded and busy. This is **figurative language**: words used in a "
          "non-literal way to create a picture, a feeling or an emphasis."),
        D("**Figurative language** uses words in an imaginative, non-literal way to make writing vivid or to stress an idea.", title="Figurative language"),
        H("Comparisons"),
        D("A **simile** compares two things using *like* or *as*. Example: 'The boy ran like the wind.'", title="Simile"),
        D("A **metaphor** says that one thing IS another. Example: 'Time is money.' 'The market was a beehive.'", title="Metaphor"),
        D("**Personification** gives human actions or feelings to things that are not human. Example: 'The wind whispered through the maize.'", title="Personification"),
        H("Exaggeration and the opposite"),
        D("**Hyperbole** is deliberate exaggeration for emphasis. Example: 'I have told you a thousand times.'", title="Hyperbole"),
        D("**Understatement** says less than the truth, to show strong feeling or to be polite. Example: 'The football was a bit rough' after a serious injury.", title="Understatement"),
        D("**Irony** is when what is said or what happens is the opposite of what is expected. Example: A fire station burned down.", title="Irony"),
        D("An **oxymoron** puts two opposite ideas together. Examples: 'deafening silence', 'bitter sweet'.", title="Oxymoron"),
        H("Sound and softening"),
        D("**Onomatopoeia** is a word that imitates a sound. Examples: buzz, hiss, thud, crash.", title="Onomatopoeia"),
        D("**Alliteration** repeats the same first sound in nearby words. Example: 'Peter picked a peck of pickled peppers.'", title="Alliteration"),
        D("A **euphemism** is a gentle word for something unpleasant. Example: 'passed away' for 'died'.", title="Euphemism"),
        KEY("How to explain an effect", "A good answer has three parts.", cards=[
            ["1. Name the figure", "This is a metaphor."],
            ["2. Say what is compared or shown", "The market is compared to a beehive."],
            ["3. Say what it makes the reader feel or see", "It shows that the market is crowded, noisy and full of busy people."],
        ]),
        EX("Worked example 1: identify and explain", intro="'The old lorry groaned up the hill.' Name the figure and explain its effect.", steps=[
            S("Find the non-literal word", text="Lorries do not groan. Groaning is a human action."),
            S("Name the figure", text="Personification (and also onomatopoeia, since groan imitates a sound)."),
            S("Explain the effect", text="It makes the lorry seem tired and shows how heavy the effort of climbing is."),
        ]),
        EX("Worked example 2: simile or metaphor?", intro="Decide: (a) 'Her voice was as sweet as honey.' (b) 'Her voice was honey.'", steps=[
            S("Look for like or as", text="(a) has 'as ... as'."),
            S("Classify", text="(a) is a simile. (b) says her voice IS honey, so it is a metaphor."),
            S("Compare the force", text="The metaphor is stronger because it does not say 'like'."),
        ]),
        MISTAKE("Calling every comparison a metaphor", "If the sentence uses 'like' or 'as', it is a simile. Only a direct statement that one thing is another is a metaphor."),
        MISTAKE("Naming the figure but not the effect", "The question often says 'explain the effect'. Naming the figure earns little. Say what picture or feeling it creates."),
        TIP("In Paper 1 reading questions, you may be asked what a phrase means or what effect it has. If the phrase makes no sense literally, treat it as figurative and ask what idea it stands for."),
        QUIZ("'The sun smiled on the village.' This is",
             ["a simile", "personification", "hyperbole", "irony"], 1,
             "The sun is given a human action (smiling), so it is personification.",
             hint="Can a sun really smile?",
             feedback=["A simile needs like or as.", "", "There is no exaggeration of amount.", "There is nothing opposite to what is expected."]),
        QUIZ("'The room was so hot that I was melting.' The best description is",
             ["understatement", "hyperbole", "euphemism", "oxymoron"], 1,
             "A person does not really melt; the exaggeration stresses the heat.",
             hint="Is the statement exaggerated or softened?",
             feedback=["Understatement says less than the truth.", "", "A euphemism softens an unpleasant word.", "An oxymoron joins two opposite words."]),
        PQ("Name the figure in each: (a) 'as quick as lightning' (b) 'The class was a zoo.' (c) 'He is between jobs.'",
           "(a) simile. (b) metaphor. (c) euphemism (for unemployed)."),
        PQ("Explain the effect of 'The thunder roared'.",
           "It is personification (a roaring animal) and onomatopoeia. It shows the thunder as loud and frightening."),
        PQ("Write one sentence containing alliteration.",
           "Sample: 'The busy bees buzzed beside the bright blossoms.'"),
        SUM("Figurative language uses words in a non-literal way for effect.",
            "Simile uses like or as; metaphor says one thing is another.",
            "Personification, hyperbole, understatement, irony, oxymoron, onomatopoeia, alliteration and euphemism each have a special purpose.",
            "Name the figure, say what it compares or shows, then say its effect."),
    ],
))

# ------------------------------------------------------------------ 7. Register: health and environment
LESSONS.append(lesson(
    module=M3, topic="Register: health, medicine and environment",
    title="Register: the language of health, medicine and the environment",
    slug="evo-register-health-environment",
    minutes=22,
    summary="Every subject has its own words. This lesson explains register and gives word banks for health, medicine and the environment, with example sentences and the pairs of words that are often confused.",
    objectives=[
        "Explain what register means and why it matters",
        "Use key words from health and medicine correctly",
        "Use key words about the environment correctly",
        "Tell apart confusable terms such as epidemic and pandemic, symptom and sign",
    ],
    key_concepts=["Register", "Formal and informal", "Technical vocabulary", "Health terms", "Environment terms"],
    blocks=[
        H("Introduction"),
        T("A nurse at a health centre in Ngaoundere says to a patient: 'You have malaria. I will prescribe a course of treatment and you must complete the dose.' "
          "A friend would say: 'You are sick with malaria. Take the drugs until they finish.' The ideas are the same, but the words are chosen for the place, "
          "the speaker and the listener. This choice of language is called **register**."),
        D("**Register** is the kind of language used in a particular situation or subject. It depends on the **field** (the topic), the **audience** and the **formality**.", title="Register"),
        T("Two parts of register matter in the exam. First, the **field**: health, the environment, science, commerce, law and so on. Each field has its own words. "
          "Second, **formality**: formal words for letters, reports and speeches, and informal words for friends."),
        KEY("Formal and informal pairs", "Use the formal word in formal writing.", cards=[
            ["buy / purchase", "We purchased new equipment for the clinic."],
            ["start / commence", "The vaccination campaign will commence on Monday."],
            ["help / assist", "Volunteers assisted the nurses."],
            ["get / obtain", "Patients obtain medicine at the pharmacy."],
        ]),
        H("Health and medicine"),
        CODE("""Word             Meaning
symptom          a change a patient feels (pain, tiredness)
sign             a change a doctor can see or measure (fever, rash)
diagnosis        the doctor's decision about what the illness is
prognosis        what the doctor expects to happen next
treatment        care to cure or ease an illness
prescription     the doctor's written order for a medicine
dose             the amount of medicine taken at one time
vaccination      an injection that gives protection from a disease
immunity         the body's protection against a disease
infection        illness caused by germs
epidemic         a disease spreading widely in a region for a time
pandemic         a disease spreading across many countries
chronic          lasting a long time (chronic illness)
acute            starting suddenly and severe (acute pain)
sanitation       clean water, toilets and waste disposal
malnutrition     illness from a poor or unbalanced diet
referral         sending a patient to a specialist or bigger hospital""", "text", title="Health word bank"),
        T("Example sentences: 'The doctor made a diagnosis of typhoid.' 'Regular vaccination gives children immunity.' "
          "'Poor sanitation can cause an outbreak of cholera.' 'The nurse referred the patient to the regional hospital.'"),
        H("The environment"),
        CODE("""Word               Meaning
environment        the land, water, air and living things around us
pollution          harmful substances in air, water or soil
deforestation      cutting down forests on a large scale
erosion            wearing away of soil by water or wind
drought            a long period with very little rain
desertification    land becoming desert
climate change     long-term change in temperature and weather patterns
global warming     rise in the earth's average temperature
emissions          gases released into the air (from vehicles, factories)
biodiversity       the variety of living things in an area
conservation       protecting nature and using it wisely
sustainable        able to continue without using up resources
renewable energy   energy from sources that do not run out (sun, wind, water)
waste disposal     the safe removal of rubbish""", "text", title="Environment word bank"),
        T("Example sentences: 'Deforestation causes soil erosion on the hillsides.' 'Burning fuel increases carbon emissions.' "
          "'Solar power is a renewable source of energy.' 'The community started a conservation project to protect the forest.'"),
        EX("Worked example 1: choose the right term", intro="Complete the sentence with the correct term: 'The ______ of the disease was not clear, so the doctor ordered more tests.' (diagnosis / prescription)", steps=[
            S("Check the meaning", text="'Not clear' and 'more tests' show that the doctor was still deciding what the illness is."),
            S("Select", text="The decision about what the illness is = diagnosis. A prescription is the written order for medicine."),
            S("Answer", text="diagnosis."),
        ]),
        EX("Worked example 2: formal rewrite", intro="Rewrite formally for a report: 'The council started a big clean-up and people helped to get rid of rubbish.'", steps=[
            S("Replace informal words", text="started = commenced; helped = assisted; get rid of = dispose of."),
            S("Replace vague words", text="big = large-scale; clean-up = cleaning campaign."),
            S("Write", text="The council commenced a large-scale cleaning campaign, and residents assisted in disposing of waste."),
        ]),
        MISTAKE("Mixing epidemic and pandemic", "An epidemic spreads within a region or country. A pandemic spreads across many countries. The difference is the size of the area."),
        MISTAKE("Mixing symptom and sign", "A symptom is what the patient feels (headache). A sign is what a person other than the patient can observe or measure (a high temperature)."),
        TIP("Words from these fields appear in reading passages in Paper 1, and are useful in composition and directed writing on health and the environment. When a passage uses a technical word, read the sentence for clues to its meaning."),
        QUIZ("A disease is spreading across many countries at the same time. The correct word is",
             ["an endemic", "a symptom", "a pandemic", "a prognosis"], 2,
             "A disease that spreads across many countries is a pandemic.",
             hint="Which word shows a very wide area?",
             feedback=["Endemic means always present in one area.", "A symptom is a feeling of the patient.", "", "A prognosis is a forecast."]),
        QUIZ("'Cutting down large areas of forest' is called",
             ["conservation", "emission", "deforestation", "biodiversity"], 2,
             "Deforestation means cutting down forests on a large scale.",
             hint="Which word carries the idea of removing forest?",
             feedback=["Conservation is protecting nature.", "Emissions are gases in the air.", "", "Biodiversity is the variety of living things."]),
        PQ("Write a sentence using each: (a) prescription (b) pollution (c) sustainable.",
           "Sample: (a) The doctor gave me a prescription for an antibiotic. (b) Pollution from the factory killed fish in the river. (c) Sustainable farming protects the soil."),
        PQ("Explain the difference between 'chronic' and 'acute'.",
           "Chronic means lasting a long time. Acute means starting suddenly and often severe."),
        PQ("Write two formal words for each informal one: buy, start, help.",
           "buy: purchase, acquire. start: commence, begin. help: assist, support."),
        SUM("Register is the language that suits the field, the audience and the formality.",
            "Health words: diagnosis, prescription, symptom, sign, vaccination, immunity, epidemic, pandemic.",
            "Environment words: pollution, deforestation, erosion, emissions, biodiversity, conservation, sustainable.",
            "Use formal words in formal writing.",
            "Learn confusable pairs by their exact meanings."),
    ],
))

# ------------------------------------------------------------------ 8. Register: science and ICT
LESSONS.append(lesson(
    module=M3, topic="Register: science, technology and ICT",
    title="Register: the language of science, technology and ICT",
    slug="evo-register-science-ict",
    minutes=22,
    summary="Science and technology use words in a precise way. This lesson gives word banks for scientific method and for ICT, shows how everyday words take special meanings and gives examples.",
    objectives=[
        "Use key words of scientific method (hypothesis, variable, data, conclusion)",
        "Use key ICT words (hardware, software, network, download, encryption)",
        "Explain how everyday words take special meanings in science and ICT",
        "Write precise sentences in a scientific style",
    ],
    key_concepts=["Hypothesis", "Variable", "Data", "Hardware and software", "Network", "Precision"],
    blocks=[
        H("Introduction"),
        T("A student in Yaounde tells her teacher: 'My phone is slow.' The ICT teacher asks: 'Is it the processor, the memory, or the network?' The teacher uses exact words because "
          "technical writing must be precise. In this lesson you learn some of these exact words."),
        D("**Technical vocabulary** is the set of exact words used in a field. They give one clear meaning, so experts avoid confusion.", title="Technical vocabulary"),
        H("Scientific method"),
        CODE("""Word          Meaning
experiment    a test carried out to find out something
hypothesis    a statement that can be tested (a proposed explanation)
variable      something that can change in an experiment
control       the part of an experiment kept unchanged for comparison
observation   what you see or measure
data          facts and figures collected (the word is usually plural)
analysis      studying the data to find patterns
evidence      facts that support a conclusion
conclusion    what you decide from the results
accurate      close to the true value
reliable      gives the same result when repeated
theory        a well-tested explanation of how something works""", "text", title="Science word bank"),
        T("Example sentences: 'The pupils tested the hypothesis that plants grow faster in sunlight.' 'The data show that temperature rose.' "
          "'Their conclusion was supported by the evidence.' 'The experiment was reliable because the result was the same each time.'"),
        KEY("Everyday words with special meanings", "Do not use these casually in scientific writing.", cards=[
            ["theory", "In daily speech, a guess. In science, a well-tested explanation."],
            ["force", "In science, a push or pull measured in newtons."],
            ["energy", "In science, the ability to do work, not just 'being active'."],
            ["mass and weight", "Mass is the amount of matter. Weight is the pull of gravity on that mass."],
        ]),
        H("Technology and ICT"),
        CODE("""Word          Meaning
hardware      the physical parts of a computer (screen, keyboard)
software      the programs that run on a computer
application   (app) a program for a task, such as a banking app
network       computers or devices linked to share data
internet      the worldwide network of networks
browser       a program for viewing web pages
download      to copy a file from the internet to your device
upload        to send a file from your device to the internet
bandwidth     how much data a connection can carry at one time
database      an organised collection of data
algorithm     a step-by-step set of instructions to solve a problem
password      a secret word that protects an account
encryption    changing data into code so only authorised people can read it
malware       harmful software (a virus is one kind)
firewall      a security system that blocks unauthorised access
cloud storage keeping files on remote servers through the internet""", "text", title="ICT word bank"),
        T("Example sentences: 'She downloaded the application from the app store.' 'The school network was down for an hour.' "
          "'The bank uses encryption to protect mobile money data.' 'He uploaded his photographs to the cloud.'"),
        EX("Worked example 1: precise wording", intro="Rewrite precisely for a science report: 'We tried the plants with different lights and saw which grew most.'", steps=[
            S("Name the process", text="'tried' = carried out an experiment; 'saw' = observed."),
            S("Name the changing factor", text="'different lights' = the independent variable (the amount of light)."),
            S("Write", text="We carried out an experiment in which the amount of light was the variable, and we observed which plants grew most."),
        ]),
        EX("Worked example 2: hardware or software?", intro="Classify: (a) a keyboard (b) a word processor (c) a hard disk (d) an operating system.", steps=[
            S("Ask: can I touch it?", text="A keyboard and a hard disk are physical parts: hardware."),
            S("Ask: is it a program?", text="A word processor and an operating system are programs: software."),
            S("Answer", text="(a) hardware (b) software (c) hardware (d) software."),
        ]),
        MISTAKE("Treating 'data' as always singular", "Traditionally, data is plural ('the data show'). Many writers also use it as singular ('the data shows'). In Cameroonian examinations use the plural verb for safety, or check your teacher's preference."),
        MISTAKE("Mixing up download and upload", "Download means copy TO your device. Upload means send FROM your device."),
        TIP("In reading passages on science and technology, the writer usually explains a new term in the same sentence, after a comma or a dash. Look for 'that is', 'which means' or 'called'."),
        QUIZ("'A statement that can be tested to explain something' is a",
             ["conclusion", "hypothesis", "variable", "control"], 1,
             "A hypothesis is a testable statement or proposed explanation.",
             hint="It comes before the experiment.",
             feedback=["A conclusion comes after the results.", "", "A variable is something that can change.", "A control is a part kept unchanged."]),
        QUIZ("Which of these is software?",
             ["a monitor", "a mouse", "a mobile banking app", "a router"], 2,
             "A mobile banking app is a program, so it is software. The other items are physical devices.",
             hint="Software is a program, not a device you can hold.",
             feedback=["A monitor is hardware.", "A mouse is hardware.", "", "A router is hardware."]),
        PQ("Give the meaning of: (a) bandwidth (b) encryption (c) reliable.",
           "(a) how much data a connection can carry. (b) changing data into code to keep it private. (c) giving the same result when repeated."),
        PQ("Write one sentence with 'hypothesis' and one with 'network'.",
           "Sample: Our hypothesis was that salt makes water boil at a higher temperature. The school's computers are connected on one network."),
        PQ("Explain the difference between 'mass' and 'weight'.",
           "Mass is the amount of matter in an object. Weight is the force of gravity on it."),
        SUM("Scientific writing uses precise words: hypothesis, variable, data, evidence, conclusion.",
            "ICT words: hardware, software, network, browser, download, upload, encryption, firewall.",
            "Some everyday words (theory, force, energy) have special scientific meanings.",
            "A term is often explained next to it in the passage: use the clue."),
    ],
))

# ------------------------------------------------------------------ 9. Register: commerce
LESSONS.append(lesson(
    module=M3, topic="Register: commerce, finance and administration",
    title="Register: the language of commerce, finance and administration",
    slug="evo-register-commerce-admin",
    minutes=22,
    summary="Business and office language has set words and set phrases. This lesson gives word banks for trade, banking and office administration, with example sentences and notes on formal phrases.",
    objectives=[
        "Use trade and finance words correctly (invoice, receipt, profit, loan)",
        "Use office and administration terms (memo, agenda, minutes, applicant)",
        "Choose formal wording for business letters",
        "Explain pairs such as revenue and profit, wholesale and retail",
    ],
    key_concepts=["Trade terms", "Finance terms", "Administration terms", "Formal phrases"],
    blocks=[
        H("Introduction"),
        T("Mama Njoh buys cartons of tomatoes from a farmer and sells them in small heaps in the market. She keeps a notebook of what she buys, what she sells and what she pays for transport. "
          "In the language of commerce, she buys **wholesale**, sells **retail**, and makes a **profit** if her income is more than her costs. These words appear in newspapers, letters and exam passages."),
        H("Trade and finance"),
        CODE("""Word          Meaning
wholesale     selling goods in large amounts, usually to traders
retail        selling goods in small amounts to the public
customer      a person who buys goods or services
supplier      a person or company that provides goods
invoice       a bill sent by a seller, showing what is owed
receipt       a paper showing that payment has been made
profit        money left when costs are taken from income
loss          when costs are more than income
revenue       the total money received from sales
expenditure   money spent
budget        a plan for income and spending
deposit       money put into a bank account (or a part-payment)
withdrawal    money taken out of a bank account
interest      money paid for borrowing, or earned on savings
loan          money borrowed that must be repaid
credit        buying now and paying later
debit         money taken from an account
tax           money paid to the government
import        to bring goods into a country
export        to send goods out of a country
commission    a fee paid to an agent for a sale""", "text", title="Trade and finance word bank"),
        T("Example sentences: 'The shop earned a revenue of 500,000 FCFA, but a profit of only 60,000 FCFA after costs.' "
          "'She repaid the loan with interest.' 'The farmers export cocoa and import fertiliser.' 'He asked for a receipt as proof of payment.'"),
        H("Administration and office language"),
        CODE("""Word            Meaning
memo            a short written message within an organisation
circular        a notice sent to many people
agenda          the list of items to discuss at a meeting
minutes         the written record of a meeting
chairperson     the person who leads a meeting
quorum          the smallest number of members needed for a meeting to go ahead
applicant       a person who applies for a job or a place
vacancy         a job that is available
curriculum vitae  a written summary of a person's education and work (CV)
referee         a person who vouches for an applicant's character
correspondence  letters and messages exchanged
enclosed        placed inside the same envelope
attached        joined to an email or message
pending         waiting to be settled
per annum       each year""", "text", title="Administration word bank"),
        T("Example sentences: 'The meeting started because a quorum was present.' 'The secretary took minutes.' 'Please find attached my curriculum vitae.' "
          "'The application is still pending.'"),
        KEY("Formal phrases for business letters", "Learn them as whole phrases.", cards=[
            ["Opening", "I am writing to apply for ... / I wish to complain about ..."],
            ["Referring", "With reference to your letter of ... / Further to our conversation ..."],
            ["Enclosing", "I enclose a copy of ... / Please find attached ..."],
            ["Closing", "I look forward to hearing from you. / Yours faithfully (if you do not know the name); Yours sincerely (if you do)."],
        ]),
        EX("Worked example 1: profit", intro="A shop receives 80,000 FCFA from sales and spends 65,000 FCFA on goods and rent. Find the profit and say what 80,000 FCFA is called.", steps=[
            S("Name the terms", text="80,000 FCFA received from sales is revenue. 65,000 FCFA spent is expenditure."),
            S("Find the profit", math=r"80\,000 - 65\,000 = 15\,000 \text{ FCFA}", text="Profit = revenue minus costs."),
            S("Answer", text="The profit is 15,000 FCFA; the revenue is 80,000 FCFA."),
        ]),
        EX("Worked example 2: choose the word", intro="Complete the sentence: 'The farmer sold the cocoa in bags of 50 kg to a trader. This is a ______ sale.' (wholesale / retail)", steps=[
            S("Check the amount", text="Bags of 50 kg sold to a trader are large amounts."),
            S("Select", text="Large amounts to traders = wholesale."),
            S("Answer", text="wholesale."),
        ]),
        MISTAKE("Confusing revenue with profit", "Revenue is all the money received. Profit is what is left after costs. A shop can have large revenue and no profit."),
        MISTAKE("Yours faithfully or yours sincerely", "Use Yours faithfully after 'Dear Sir or Madam', and Yours sincerely after a name ('Dear Mr Tabi')."),
        TIP("Directed writing and formal letters in Paper 2 need correct office language, and passages in Paper 1 often use commerce words. Learn the word banks as families."),
        QUIZ("A bill sent by a seller showing the amount to be paid is",
             ["a receipt", "an invoice", "a deposit", "a budget"], 1,
             "An invoice asks for payment. A receipt shows that payment has been made.",
             hint="Does the customer still need to pay?",
             feedback=["A receipt is given after payment.", "", "A deposit is money put in.", "A budget is a plan for money."]),
        QUIZ("The written record of what was said and decided at a meeting is called",
             ["the agenda", "the minutes", "a memo", "a circular"], 1,
             "Minutes record what happened at a meeting. The agenda is the list of items before the meeting.",
             hint="The record is written after or during the meeting.",
             feedback=["The agenda comes before.", "", "A memo is a short message.", "A circular is a notice to many people."]),
        PQ("A trader buys goods for 120,000 FCFA and sells them for 150,000 FCFA. What is his profit?",
           "150,000 - 120,000 = 30,000 FCFA."),
        PQ("Write one sentence with each: (a) vacancy (b) deposit (c) enclosed.",
           "Sample: (a) The company has a vacancy for an accountant. (b) She made a deposit at the bank. (c) I have enclosed my certificate."),
        PQ("Explain 'import' and 'export'.",
           "Import means bringing goods into a country. Export means sending goods out of a country to sell."),
        SUM("Trade words: wholesale, retail, invoice, receipt, revenue, profit, loss.",
            "Finance words: deposit, withdrawal, interest, loan, credit, tax.",
            "Office words: memo, agenda, minutes, vacancy, applicant, enclosed.",
            "Revenue is all the money received; profit is what is left after costs.",
            "Use set phrases in business letters."),
    ],
))

# ------------------------------------------------------------------ 10. Register: law and governance
LESSONS.append(lesson(
    module=M3, topic="Register: law, governance and human rights",
    title="Register: the language of law, governance and human rights",
    slug="evo-register-law-governance",
    minutes=22,
    summary="Law and government use exact words. This lesson gives word banks for courts, government and human rights, with example sentences, and warns about words that look alike.",
    objectives=[
        "Use court and legal words correctly (plaintiff, accused, verdict, bail)",
        "Use governance words (constitution, legislature, executive, judiciary)",
        "Use human-rights words (freedom, dignity, discrimination, citizen)",
        "Distinguish pairs such as law and bill, convict and acquit",
    ],
    key_concepts=["Constitution", "Legislature, executive, judiciary", "Court terms", "Rights and duties"],
    blocks=[
        H("Introduction"),
        T("In a newspaper in Cameroon you may read: 'The National Assembly passed the bill. The court heard evidence from the witness. "
          "The accused was granted bail.' Each word has an exact meaning in law and government. If you mix them up, your sentence is wrong or confusing. "
          "This lesson explains the common ones in a neutral way."),
        H("Government"),
        CODE("""Word           Meaning
constitution   the basic set of rules by which a country is governed
government     the people who run the country
legislature    the body that makes laws (for example parliament)
executive      the body that carries out the laws (the government)
judiciary      the courts and judges who interpret the law
bill           a proposed law before it is passed
act (of parliament) a bill that has been passed and has become law
law            a rule made by the state that everyone must obey
citizen        a person who legally belongs to a country
election       a process of choosing leaders by voting
ballot         a vote cast (the paper or system used)
candidate      a person standing for election
constituency   an area represented by an elected member
mandate        the authority given to those elected
administration the management of public affairs
decentralisation transferring some powers to local authorities""", "text", title="Governance word bank"),
        T("Example sentences: 'Parliament passed the bill and it became an act.' 'Every citizen over the legal age may vote.' "
          "'The council is responsible for local administration.'"),
        H("Courts and the law"),
        CODE("""Word          Meaning
court         a place where legal cases are heard
judge         the person who decides a case
magistrate    a judge in a lower court
lawyer        a person trained to give legal advice and speak in court
plaintiff     the person who brings a case to court (civil case)
defendant     the person against whom a case is brought
accused       a person charged with a crime
witness       a person who tells the court what they saw or know
evidence      facts or objects shown to prove something
verdict       the decision of the court
convict       to find a person guilty (verb); a convict is a person found guilty
acquit        to declare a person not guilty
sentence      the punishment given by a court
bail          temporary release of an accused person before trial
appeal        a request to a higher court to change a decision
contract      a legal agreement
offence       an act that breaks the law""", "text", title="Court word bank"),
        T("Example sentences: 'The witness gave evidence in court.' 'The accused was acquitted for lack of evidence.' 'The judge announced the verdict.' "
          "'The company signed a contract with the supplier.'"),
        H("Human rights"),
        CODE("""Word                    Meaning
human rights            basic rights every person has
dignity                 the right to be treated with respect
equality                being treated the same in rights and chances
freedom of expression   the right to say and share opinions
discrimination          unfair treatment because of who a person is
fundamental             basic and very important
duty                    something a person must do (pay tax, obey the law)
declaration             a formal statement
privacy                 the right to keep personal life and information private
justice                 fair treatment under the law""", "text", title="Human rights word bank"),
        T("The Universal Declaration of Human Rights was adopted by the United Nations in 1948. It lists rights such as the right to life, education and equal treatment. "
          "Rights go with duties: citizens enjoy rights, and they must also respect the rights of others and obey the law."),
        EX("Worked example 1: choose the right word", intro="'The judge found the accused not guilty. The accused was ______.' (convicted / acquitted)", steps=[
            S("Check the meaning", text="Not guilty means the court cleared the accused."),
            S("Select", text="Acquit means to declare not guilty. Convict means to declare guilty."),
            S("Answer", text="acquitted."),
        ]),
        EX("Worked example 2: bill or act?", intro="'A proposed law before the National Assembly is a ______; once passed, it becomes an ______.'", steps=[
            S("Think of the stage", text="A proposed law is not yet in force."),
            S("Select", text="Before passing: a bill. After passing: an act."),
            S("Answer", text="bill ... act."),
        ]),
        MISTAKE("Confusing plaintiff and accused", "A plaintiff starts a civil case to claim something. An accused person is charged with a crime. They are different kinds of case."),
        MISTAKE("Using 'law' and 'bill' as the same word", "A bill is a proposal. It becomes a law only after it is passed."),
        TIP("Words from law and governance appear in news-style reading passages. They are also useful in speeches, reports and argumentative essays. Keep your tone neutral and respectful."),
        QUIZ("The body that makes laws is called the",
             ["judiciary", "legislature", "executive", "witness"], 1,
             "The legislature (parliament) makes laws. The executive carries them out; the judiciary interprets them.",
             hint="It makes laws.",
             feedback=["The judiciary is the courts.", "", "The executive carries out the laws.", "A witness gives evidence."]),
        QUIZ("A person who tells the court what he or she saw is a",
             ["plaintiff", "magistrate", "witness", "lawyer"], 2,
             "A witness tells the court what he or she saw or knows.",
             hint="This person gives evidence.",
             feedback=["A plaintiff brings the case.", "A magistrate is a judge.", "", "A lawyer represents a party."]),
        PQ("Explain the difference between 'convict' and 'acquit'.",
           "To convict is to find a person guilty. To acquit is to declare a person not guilty."),
        PQ("Write one sentence with each word: (a) verdict (b) citizen (c) bail.",
           "Sample: (a) The court gave its verdict yesterday. (b) A citizen has the right to vote. (c) The accused was granted bail."),
        PQ("Name the three arms of government and say what each does.",
           "Legislature: makes laws. Executive: carries out laws. Judiciary: interprets laws and settles cases."),
        SUM("Government words: constitution, legislature, executive, judiciary, bill, act, citizen, election.",
            "Court words: plaintiff, accused, witness, evidence, verdict, convict, acquit, sentence, bail, appeal.",
            "Human rights words: dignity, equality, freedom of expression, discrimination, duty.",
            "Rights come with duties.",
            "A bill is a proposed law; it becomes an act after it is passed."),
    ],
))

# ------------------------------------------------------------------ 11. Skimming and scanning
LESSONS.append(lesson(
    module=M4, topic="Skimming, scanning and main ideas",
    title="Skimming, scanning and finding the main idea",
    slug="evo-skim-scan-main-idea",
    minutes=20,
    summary="Skimming gives you the main idea quickly; scanning finds one detail. Learn the two skills, how a paragraph is built, and how to find the topic sentence and the main idea of a passage.",
    objectives=[
        "Explain the difference between skimming and scanning",
        "Skim a passage for its main idea in under a minute",
        "Scan a passage for a name, number or date",
        "Find the topic sentence and the main idea of a paragraph",
    ],
    key_concepts=["Skimming", "Scanning", "Main idea", "Topic sentence", "Supporting details"],
    blocks=[
        H("Introduction"),
        T("When you open a newspaper, you do not read every word. You look at the headline and the first lines to see if the story matters to you. Then, if you want to know the price "
          "of a bus ticket in the same story, you let your eyes run down the page looking only for a number. You are using two different ways of reading."),
        D("**Skimming** is reading quickly to get the general idea of a text. You read the title, the first sentence of each paragraph and the last sentence, and you ignore details.", title="Skimming"),
        D("**Scanning** is looking quickly through a text to find one particular piece of information, such as a name, a date, a number or a keyword. You do not read the rest.", title="Scanning"),
        KEY("When to use each", "Use the right skill for the question.", cards=[
            ["Skim", "'What is the passage mainly about?' 'What is the best title?'"],
            ["Scan", "'How much did each family give?' 'When did the project start?' 'Who is the head of the school?'"],
        ]),
        H("How paragraphs are built"),
        D("The **main idea** is the central point the writer wants to make. A paragraph usually has one main idea; a passage has an overall main idea made from the paragraphs.", title="Main idea"),
        D("A **topic sentence** states the main idea of a paragraph. It is often the first sentence, sometimes the last. The other sentences are **supporting details**: reasons, examples and facts.", title="Topic sentence"),
        T("Read the passage below. It is short, so you can practise skimming first: read only the title and the first sentence of each paragraph."),
        T("**Water for Our School**\n\nLast year, the pupils of Government Primary School Nkoteng walked nearly two kilometres each morning to fetch water from a stream. Many arrived late, and some fell ill after drinking water that was not clean.\n\n"
          "In March, the Parent-Teacher Association decided to act. Each family gave 2,000 FCFA, and the local council added money for materials. A well was dug beside the school and covered with a concrete top, and a hand pump was fitted.\n\n"
          "The results were clear within one term. Pupils now arrive on time, cases of stomach illness have dropped, and a school garden has been planted with vegetables watered from the well.\n\n"
          "The headmistress says the project shows what a community can do together. The Association plans to repair the school's toilets next year."),
        EX("Worked example 1: skimming", intro="Skim 'Water for Our School'. What is the passage mainly about?", steps=[
            S("Read the title", text="'Water for Our School' tells us the topic."),
            S("Read the first sentence of each paragraph", text="Paragraph 1: the problem of walking far for water. Paragraph 2: the Association acts. Paragraph 3: the results. Paragraph 4: the community and future plan."),
            S("Join the ideas", text="A problem, then action by the community, then good results."),
            S("Main idea", text="A community solved its school's water problem together, and the school improved."),
        ]),
        EX("Worked example 2: scanning", intro="Scan the passage to answer: 'How much did each family give?'", steps=[
            S("Decide the keyword", text="A money amount: look for numbers and FCFA."),
            S("Run your eyes down the text", text="Ignore the sentences without numbers. Paragraph 2 contains '2,000 FCFA'."),
            S("Read around the number", text="'Each family gave 2,000 FCFA.'"),
            S("Answer", text="2,000 FCFA."),
        ]),
        H("Finding the main idea of a passage"),
        KEY("A simple method", "Use this for any passage.", cards=[
            ["Step 1", "Read the title and the first and last paragraphs."],
            ["Step 2", "Find the topic sentence of each paragraph."],
            ["Step 3", "Ask: what do these sentences have in common?"],
            ["Step 4", "Check the answer: it must cover the whole passage, not only one part."],
        ]),
        T("Wrong answers in multiple-choice main-idea questions are usually of three kinds. Some are **too narrow** (one detail only). Some are **too wide** (a general statement that the passage does not make). Some are **not stated** (true in life but not in the passage)."),
        MISTAKE("Choosing a detail as the main idea", "'Each family gave 2,000 FCFA' is true but it is only a detail in one paragraph. The main idea covers the whole passage."),
        MISTAKE("Reading every word when scanning", "If you read everything you waste time. Fix the keyword in your mind (a number, a name, a capital letter) and move your eyes quickly."),
        TIP("Paper 1 has a reading comprehension part within its 50 multiple-choice questions and the time is limited. Skim first to know what the passage is about, then read the question and scan for the answer. Then read that part closely."),
        QUIZ("Which is the best title for the passage 'Water for Our School'?",
             ["The Importance of Gardens", "How a Community Gave Its School Clean Water", "Illness in Primary Schools", "The Work of the Local Council"], 1,
             "The best title covers the whole passage: the community acting to give the school clean water.",
             hint="Choose the title that fits all four paragraphs.",
             feedback=["The garden is a small detail in paragraph 3.", "", "Illness is mentioned only as part of the problem.", "The council gives money but is not the main subject."]),
        QUIZ("You are asked: 'In which month did the Association decide to act?' The best skill is",
             ["skimming", "scanning", "summarising", "predicting"], 1,
             "You need one detail (a month), so you scan for it.",
             hint="Is the question about the whole passage or one detail?",
             feedback=["Skimming gives the main idea, not a specific detail.", "", "Summarising shortens the whole text.", "Predicting is guessing before reading."]),
        PQ("Scan 'Water for Our School' and write the distance the pupils walked each morning.",
           "Nearly two kilometres (paragraph 1)."),
        PQ("Write the topic sentence of paragraph 3 of 'Water for Our School'.",
           "'The results were clear within one term.' It states the main idea of the paragraph; the other sentences give the results."),
        PQ("Why is 'The pupils walked far' not a good answer to 'What is the main idea of the passage?'",
           "It is too narrow: it is only the problem in paragraph 1. The main idea covers the whole passage, including the action and the results."),
        SUM("Skimming gets the main idea; scanning finds a detail.",
            "A topic sentence states the main idea of a paragraph.",
            "The main idea of a passage must cover the whole passage.",
            "Wrong answers are often too narrow, too wide or not stated.",
            "Skim first, then scan for the answer, then read that part closely."),
    ],
))

# ------------------------------------------------------------------ 12. Contextual vocabulary
LESSONS.append(lesson(
    module=M4, topic="Contextual vocabulary deduction",
    title="Working out word meanings from context",
    slug="evo-context-clues",
    minutes=20,
    summary="You can often work out a new word from the sentence around it. Learn the clue types (definition, synonym, contrast, example, cause and effect), use word parts, and check your guess in the sentence.",
    objectives=[
        "Name five kinds of context clue",
        "Use word parts to guess a meaning",
        "Choose the word class first, then the meaning",
        "Check a guess by replacing the word in the sentence",
    ],
    key_concepts=["Context clue", "Definition clue", "Contrast clue", "Example clue", "Word parts", "Replacement test"],
    blocks=[
        H("Introduction"),
        T("You are in a shop in Limbe. The shopkeeper says to a customer, 'I cannot reduce the price; the margin is very meagre.' If you do not know the word *meagre*, "
          "you can still guess that it means very small, because a shopkeeper who cannot reduce a price is probably earning very little. You used the **context**."),
        D("**Context** is the words and sentences around a word. A **context clue** is a hint in the context that helps you work out the meaning of an unknown word.", title="Context clue"),
        H("Kinds of clues"),
        KEY("Five common clues", "Look for the signal words in bold.", cards=[
            ["Definition", "The meaning is given: 'A *nomad* is a person who moves from place to place.'"],
            ["Synonym", "A similar word nearby: 'The road was *treacherous*, that is, dangerous.'"],
            ["Contrast (antonym)", "An opposite signal: 'Unlike his *frugal* brother, who saved every coin, Ako spent freely.'"],
            ["Example", "Examples follow: 'She grows *cereals*, such as maize, millet and rice.'"],
            ["Cause and effect", "'Because the roof had a leak, the *saturated* mattress could not be used.'"],
        ]),
        T("Signal words help: *that is*, *called*, *which means*, *or* (definition and synonym); *but*, *unlike*, *however*, *on the other hand* (contrast); "
          "*such as*, *for example* (example); *because*, *so*, *therefore* (cause and effect)."),
        H("Other helps"),
        KEY("Word parts and word class", "Use these before and after the clue.", cards=[
            ["Word parts", "*unbelievable* = un (not) + believe + able. *Prehistoric* = pre (before) + history."],
            ["Word class", "Decide first: is the word a noun, verb, adjective or adverb? The slot in the sentence tells you."],
            ["Replacement test", "Put your guess into the sentence. Does the sentence still make sense?"],
        ]),
        EX("Worked example 1: contrast clue", intro="'Unlike his frugal brother, who saved every coin, Ako spent freely.' What does 'frugal' mean?", steps=[
            S("Find the signal", text="'Unlike' tells you that the brother is the opposite of Ako."),
            S("Read the opposite", text="Ako spent freely; his brother saved every coin."),
            S("Guess", text="Frugal means careful with money."),
            S("Test", text="'Unlike his careful-with-money brother, Ako spent freely.' The sentence fits."),
        ]),
        EX("Worked example 2: word parts and word class", intro="'The farmers were jubilant after the harvest, and they sang and danced.' What does 'jubilant' mean?", steps=[
            S("Word class", text="'Were jubilant' comes after the verb 'were' and describes the farmers: an adjective."),
            S("Look at the effect", text="They sang and danced after the harvest."),
            S("Guess", text="Jubilant means very happy and joyful."),
            S("Test", text="'The farmers were very happy after the harvest, and they sang and danced.' It fits."),
        ]),
        MISTAKE("Choosing a meaning you already know", "Some words have more than one meaning. 'Fair' can mean pale or just. Let the sentence decide: do not pick the first meaning that comes to mind."),
        MISTAKE("Ignoring the signal word", "'However' or 'unlike' turns a meaning to its opposite. If you skip it, you may choose the opposite of the correct answer."),
        TIP("In Paper 1 reading comprehension, a question may ask what a word 'means as used in the passage'. All four choices may be real meanings of the word. Choose the one that fits this sentence, and test it by replacement."),
        QUIZ("'The path was so narrow and steep that only the most agile goats could climb it.' The word 'agile' most likely means",
             ["slow and heavy", "quick and able to move easily", "old and weak", "noisy"], 1,
             "A narrow, steep path needs animals that move easily and quickly.",
             hint="What kind of goat could climb a steep, narrow path?",
             feedback=["A slow, heavy goat could not climb it.", "", "Weak goats could not climb it.", "Noise is not suggested."]),
        QUIZ("'Many tubers, for example yams, cassava and cocoyams, grow underground.' A 'tuber' is",
             ["a kind of fruit", "a plant part that grows underground and stores food", "a tool for farming", "a bird"], 1,
             "The examples (yams, cassava, cocoyams) and the words 'grow underground' show the meaning.",
             hint="What do yams, cassava and cocoyams have in common?",
             feedback=["The clue 'grow underground' does not suit most fruit.", "", "The examples are plants, not tools.", "The examples are plants, not birds."]),
        PQ("'The teacher was lenient, so the pupils were surprised when she did not punish the late boy.' Give the likely meaning of 'lenient' and the clue.",
           "Lenient means not strict, gentle in punishing. Clue: the pupils were surprised that she did not punish him; a strict teacher would."),
        PQ("Use word parts to explain the meaning of 'disappear' and 'rebuild'.",
           "disappear: dis (opposite) + appear = stop being seen. rebuild: re (again) + build = build again."),
        PQ("'Her enthusiasm was contagious; soon the whole class was eager to start.' What does 'contagious' mean here?",
           "Spreading easily from one person to another. Clue: soon the whole class was eager."),
        SUM("Use the words around an unknown word: definition, synonym, contrast, example, cause and effect.",
            "Signal words (that is, but, such as, because) show the type of clue.",
            "Decide the word class and look at the word parts.",
            "Test your guess by putting it in the sentence.",
            "Choose the meaning that fits this sentence."),
    ],
))

# ------------------------------------------------------------------ 13. Tone, attitude and purpose
LESSONS.append(lesson(
    module=M4, topic="Tone, attitude and purpose",
    title="Identifying tone, attitude and purpose",
    slug="evo-tone-attitude-purpose",
    minutes=20,
    summary="Writers show feeling through word choice and style. Learn to name common tones, read clues such as choice of words and punctuation, and decide whether the purpose is to inform, persuade, entertain, advise or warn.",
    objectives=[
        "Define tone, attitude and purpose",
        "Name common tones (humorous, sarcastic, critical, appreciative and others)",
        "Use word choice and punctuation as clues",
        "Decide the writer's purpose",
    ],
    key_concepts=["Tone", "Attitude", "Purpose", "Word choice", "Sarcasm"],
    blocks=[
        H("Introduction"),
        T("Two people describe the same bus ride. One says: 'The journey from Bamenda to Douala was long, but the driver was careful and we arrived safely.' "
          "The other says: 'Another wonderful trip: six hours squeezed like sardines and nobody even said sorry.' The facts are similar. The feelings are very different. "
          "The first writer is calm. The second is sarcastic. We call this difference **tone**."),
        D("**Tone** is the writer's manner of speaking, shown by the words chosen. It shows the feeling in the writing, such as angry, humorous or calm.", title="Tone"),
        D("**Attitude** is what the writer thinks or feels about the subject, such as approval, concern or disapproval.", title="Attitude"),
        D("**Purpose** is the reason for writing: to inform, to persuade, to entertain, to advise, to warn or to complain.", title="Purpose"),
        H("Tone words"),
        CODE("""Tone            Sounds like                              Clue words
formal          serious, correct, impersonal             'It is regretted that ...'
informal        friendly, chatty                         'Guess what!'
humorous        funny, light                             jokes, exaggeration
sarcastic       saying the opposite to mock              'Oh, how kind of you!'
critical        finding fault                            'failed to', 'poor', 'careless'
appreciative    thankful, admiring                       'grateful', 'excellent'
optimistic      hopeful                                  'promising', 'bright future'
pessimistic     expecting the worst                      'hopeless', 'no chance'
objective       fair, giving facts only                  numbers, neutral words
urgent          pressing, needing quick action           'immediately', 'at once'
sympathetic     showing sorrow for another               'sorry to hear'
nostalgic       longing for the past                     'in those days', 'we used to'""", "text", title="Common tones"),
        H("How to find the tone"),
        KEY("Three kinds of clue", "Collect at least two before you decide.", cards=[
            ["Word choice", "'Wonderful' and 'marvellous' suggest approval. 'Careless' and 'shameful' suggest disapproval."],
            ["Punctuation", "Exclamation marks show strong feeling. Question marks may show doubt or sarcasm."],
            ["Style", "Short sentences may show urgency or anger. Long, careful sentences suggest formality."],
        ]),
        T("Sarcasm is the hardest tone to see. The words sound positive but the situation shows the opposite: 'What a brilliant idea to leave the door open in the rain.'"),
        H("Purpose"),
        KEY("Match the purpose", "Look at the type of text and the verbs used.", cards=[
            ["To inform", "facts, dates, explanations (news report)"],
            ["To persuade", "'must', 'should', 'we urge you' (campaign, advertisement)"],
            ["To entertain", "humour, a story, lively description"],
            ["To advise", "'you should', 'it is better to' (health notice)"],
            ["To warn", "'beware', 'never', 'do not' (danger notice)"],
        ]),
        EX("Worked example 1: tone", intro="'Our teacher lost his keys again. What a surprise! The man is so organised that he once searched for his glasses while wearing them.' What is the tone?", steps=[
            S("Look at the words", text="'What a surprise!' and 'so organised' are said about a man who loses things: the opposite of what is true."),
            S("Look at the extra detail", text="Searching for glasses while wearing them is a funny exaggeration."),
            S("Decide", text="The tone is humorous, with a gentle sarcasm."),
        ]),
        EX("Worked example 2: purpose", intro="'Never dry clothes on electric wires. A wet cable can kill. Report any broken wire to the electricity company at once.' What is the purpose?", steps=[
            S("Look at the verbs", text="'Never dry', 'Report' are commands."),
            S("Look at the topic", text="Danger: 'can kill'."),
            S("Decide", text="The purpose is to warn people (and to advise them what to do)."),
        ]),
        MISTAKE("Confusing tone with topic", "A sad story can be written in a calm tone. Do not decide the tone from the subject only: look at the words."),
        MISTAKE("Choosing an extreme tone", "Do not choose 'angry' when the writer is only 'concerned'. Pick the tone that matches the strength of the words."),
        TIP("Paper 1 reading questions may ask 'What is the writer's attitude to ...?' or 'What is the purpose of the passage?'. Eliminate extreme words and keep the option that matches the clue words in the passage."),
        QUIZ("'Oh, thank you very much for waking the whole street at four in the morning.' The tone is",
             ["appreciative", "sarcastic", "formal", "sympathetic"], 1,
             "The thanks are false: the speaker is annoyed. Saying the opposite to mock is sarcasm.",
             hint="Is the speaker really grateful?",
             feedback=["He is not truly thankful.", "", "The language is not formal.", "He is not showing sympathy."]),
        QUIZ("A notice reads: 'All pupils must wash their hands before meals. Clean hands protect you from disease.' The purpose is mainly to",
             ["entertain", "advise", "complain", "mock"], 1,
             "The notice tells pupils what to do and why: it advises.",
             hint="Look at 'must' and the reason given.",
             feedback=["There is no humour or story.", "", "There is no complaint.", "Nothing is mocked."]),
        PQ("Name the tone of each: (a) 'We are most grateful to the nurses for their patient care.' (b) 'This road is a disgrace; nothing has been repaired for ten years.'",
           "(a) appreciative. (b) critical (angry or disapproving)."),
        PQ("Give two clues that show a writer is urgent.",
           "Commands and time words such as 'at once' or 'immediately'; short sentences; exclamation marks."),
        PQ("What is the difference between tone and purpose?",
           "Tone is the feeling or manner of the writing (angry, humorous). Purpose is the reason for writing (inform, persuade, warn)."),
        SUM("Tone is the writer's manner; attitude is what the writer thinks; purpose is why the writer writes.",
            "Look at word choice, punctuation and style to find the tone.",
            "Sarcasm says the opposite of what is meant.",
            "Purposes include to inform, persuade, entertain, advise, warn and complain.",
            "Avoid extreme answers that go beyond the clues."),
    ],
))

# ------------------------------------------------------------------ 14. Factual vs inferential
LESSONS.append(lesson(
    module=M4, topic="Factual and inferential questions",
    title="Factual and inferential questions",
    slug="evo-factual-inferential",
    minutes=22,
    summary="Some questions ask for what the passage says; others ask what it suggests. Learn to tell them apart, find evidence in the text, and avoid answers that go beyond it.",
    objectives=[
        "Tell a factual (literal) question from an inferential one",
        "Find evidence in a passage for an answer",
        "Draw reasonable inferences without going beyond the text",
        "Avoid not-stated and over-strong answers",
    ],
    key_concepts=["Factual question", "Inference", "Evidence", "Evaluative question", "Not stated"],
    blocks=[
        H("Introduction"),
        T("A woman walks into the market, sees that the stalls are closed and the street is empty, and says: 'It must be a public holiday.' Nobody told her. She worked it out from clues. "
          "Reading comprehension asks you to do two things: find what the writer states, and work out what the writer suggests."),
        D("A **factual (literal) question** asks for information that is stated directly in the passage. The answer is in the text, perhaps in different words.", title="Factual question"),
        D("An **inferential question** asks you to work out something that is not stated directly but is suggested by the clues in the text. An **inference** is a logical conclusion from evidence.", title="Inference"),
        T("An **evaluative question** asks for your judgement (for example, whether an argument is fair). The judgement must still be based on the text."),
        T("Read this passage."),
        T("**The Bakery**\n\nMaman Ruth opens her bakery at four every morning, long before the first taxi passes. By six o'clock, the smell of fresh bread fills the street and a line of customers waits at her window. "
          "She uses a wood-fired oven that her late husband built, and she refuses to change it, even though her son has offered to buy an electric one.\n\n"
          "'Machines cannot give bread this taste,' she says with a smile. Her loaves are sold out by nine. Yet the shop next door, which has an electric oven, still has bread on its shelves at noon. "
          "Some neighbours say that Maman Ruth works too hard for her age, but she says that her day would feel empty without the dough on her hands."),
        EX("Worked example 1: a factual question", intro="'At what time does Maman Ruth open her bakery?'", steps=[
            S("Spot the type", text="This asks for a detail stated in the passage: a factual question."),
            S("Scan", text="Look for a time: 'four every morning'."),
            S("Answer", text="At four o'clock in the morning."),
        ]),
        EX("Worked example 2: an inferential question", intro="'What can you infer about the bread from Maman Ruth's oven?'", steps=[
            S("Spot the type", text="'Infer' means the answer is suggested, not stated."),
            S("Collect the clues", text="Her loaves are sold out by nine; the neighbour's shop still has bread at noon; customers line up at six."),
            S("Reason", text="Customers prefer her bread."),
            S("Answer", text="Her bread is popular because customers like the taste. (The passage does not say 'popular', but the evidence shows it.)"),
        ]),
        H("A method for inference"),
        KEY("Evidence first", "Use these steps.", cards=[
            ["1", "Read the question and decide the type."],
            ["2", "Find the lines that give clues."],
            ["3", "Ask: what must be true if these clues are true?"],
            ["4", "Choose the answer that the evidence supports and nothing more."],
        ]),
        CODE("""Statement about 'The Bakery'                        Type
She opens at four.                                  stated (true)
Her husband built the oven.                         stated (true)
Her son wants her to stop working.                  NOT stated: he offered an electric oven
Her customers like her bread.                       inferred (sold out by nine)
She is the richest person in the town.              not stated, no evidence""", "text", title="Stated, inferred or not stated"),
        T("A good answer to an inferential question is **reasonable** and **supported**. Do not use outside knowledge or guess wildly."),
        MISTAKE("Giving an answer that goes beyond the text", "'Her son wants her to stop working' sounds possible, but he only offered an electric oven. It could be to help her. Stay close to the evidence."),
        MISTAKE("Answering a factual question with an opinion", "If the question asks 'What does the passage say ...?', do not add your own ideas."),
        TIP("In Paper 1 (multiple choice), wrong options often contain words that look like the passage but change its meaning, or extreme words such as 'always', 'never' and 'all'. Check each option against the passage."),
        QUIZ("What can be inferred about the shop next door?",
             ["It sells fresher bread.", "It is less popular than Maman Ruth's bakery.", "It opens before four.", "It belongs to Maman Ruth's son."], 1,
             "Its shelves still have bread at noon, while hers is sold out by nine, so fewer customers choose it.",
             hint="Compare when the bread runs out in the two shops.",
             feedback=["Nothing says its bread is fresher.", "", "Only Maman Ruth's opening time is given.", "The owner is not stated."]),
        QUIZ("Which question is inferential?",
             ["Who built the oven?", "What time are the loaves sold out?", "Why do you think Maman Ruth refuses an electric oven?", "Where does the smell of fresh bread spread?"], 2,
             "'Why do you think ...' needs reasoning from clues. The others ask for stated facts.",
             hint="Which question asks you to think beyond the text?",
             feedback=["The passage states who built the oven.", "The passage states 'sold out by nine'.", "", "The passage states that the smell fills the street."]),
        PQ("Say whether each statement about 'The Bakery' is stated, inferred or not stated: (a) The oven uses wood. (b) Maman Ruth loves her work. (c) She has three children.",
           "(a) stated. (b) inferred (her day would feel empty without the dough on her hands). (c) not stated."),
        PQ("Answer in your own words: Why does Maman Ruth keep the old oven?",
           "She believes machines cannot give the bread the same taste (and it was built by her late husband)."),
        PQ("Why is 'Maman Ruth is the richest woman in town' a poor answer to an inference question?",
           "There is no evidence for it in the passage. An inference must be supported by clues."),
        SUM("A factual question asks what is stated; an inferential question asks what is suggested.",
            "Inferences must be supported by evidence in the text.",
            "Avoid answers that add facts not in the passage.",
            "Beware of extreme words (always, never, all).",
            "Find the evidence lines before choosing your answer."),
    ],
))

MM_PASSAGE = (
    "**Mobile Money in Our Town**\n\n"
    "Ten years ago, if Mr Fon in Bamenda wanted to send money to his mother in a village near Wum, he had to travel for six hours or pay a bus driver to carry an envelope. "
    "The journey was tiring, costly and risky. Today he sends the money in less than a minute using his mobile phone. This service, called mobile money, has changed life in many parts of Cameroon.\n\n"
    "Mobile money allows people to store small amounts of money on a phone, to send it to others and to pay bills. Traders use it to buy goods from suppliers in other towns without carrying cash. "
    "Parents use it to pay school fees. Farmers receive payments directly from buyers. As a result, people are less afraid of theft, and they save time and transport costs.\n\n"
    "However, there are also dangers. Some people lose money to criminals who pretend to be agents and ask for secret codes. Others forget to check the amount before they confirm a payment. "
    "In addition, the service is of little use in places where the network is weak. Experts therefore advise users never to share their secret codes, to check each message carefully and to keep their phones safe."
)

# ------------------------------------------------------------------ 15. Summary 1
LESSONS.append(lesson(
    module=M4, topic="Summary writing",
    title="Summary writing 1: selecting the main points",
    slug="evo-summary-select-points",
    minutes=22,
    summary="A summary keeps only the main points of a passage. Learn to read the task, mark the relevant points, remove examples, repetition and extra detail, and make a short list of points ready to write up.",
    objectives=[
        "Read a summary task and decide what it asks for",
        "Select the main points paragraph by paragraph",
        "Remove examples, repetition, illustration and unwanted detail",
        "Make a clear list of points within the word limit",
    ],
    key_concepts=["Summary", "Main point", "Redundancy", "Task focus", "Note-making"],
    blocks=[
        H("Introduction"),
        T("A friend in Garoua asks you what a long newspaper article was about. You do not read it aloud. You say: 'The article says the town needs more clean water, that the council has a plan, and that residents must help.' "
          "That is a summary: a short version of a longer text, with the same main points and fewer words."),
        D("A **summary** is a short account of the main points of a text, in your own words, in fewer words than the original.", title="Summary"),
        T("A good summary has four qualities. It is **accurate** (the points are in the text), **complete** (all the main points asked for), **short** (within the word limit) and **clear** (continuous sentences)."),
        H("Step 1: read the task"),
        T("The task tells you what to select. Compare two tasks on the same passage: 'Summarise the advantages of mobile money' and 'Summarise the advantages and the dangers of mobile money.' "
          "The second needs more points. Underline the key words in the task: what to summarise, how many words, and in what form."),
        T("Here is our practice passage. We will use it in this lesson and in the next."),
        T(MM_PASSAGE),
        T("**Task:** In not more than 70 words, summarise the advantages of mobile money and the dangers connected with it."),
        H("Step 2: mark the points"),
        KEY("What to keep and what to drop", "Decide for every sentence.", cards=[
            ["Keep", "Main points that answer the task: reasons, results, causes, key facts."],
            ["Drop: examples", "Named people and places (Mr Fon, Bamenda, Wum)."],
            ["Drop: repetition", "The same idea said twice in different words."],
            ["Drop: illustration and background", "'Ten years ago ...' and descriptions that only make the story lively."],
            ["Drop: extras", "Points that the task does not ask for."],
        ]),
        EX("Worked example 1: paragraph by paragraph", intro="Select the points for the task on the mobile money passage.", steps=[
            S("Paragraph 1", text="Mr Fon's journey is an illustration. The only general point is that money can now be sent from a phone in less than a minute (quickly). Keep: sends money quickly."),
            S("Paragraph 2", text="Keep: stores, sends, pays bills; traders, parents and farmers use it for payments; less fear of theft; saves time and transport costs."),
            S("Paragraph 3", text="Keep the dangers: criminals pretend to be agents and ask for secret codes; people forget to check the amount; the service is of little use where the network is weak."),
            S("Leave out", text="The advice at the end (never share codes, check messages, keep phones safe) is not asked for. Mr Fon and the place names are examples."),
        ]),
        EX("Worked example 2: remove repetition", intro="A student's list has these points. Remove what is repeated or not needed: (1) sends money fast; (2) very quick; (3) can pay bills; (4) Mr Fon sent money to Wum; (5) less theft.", steps=[
            S("Find repeated ideas", text="(1) and (2) both say speed: keep one."),
            S("Find examples", text="(4) is an example about a named person and place: remove."),
            S("Final list", text="Sends money quickly; pays bills; less theft."),
        ]),
        CODE("""Points selected for the 70-word task
Advantages
 1. send, store and receive money and pay bills by phone
 2. quick
 3. traders, parents and farmers use it for payments
 4. less danger of theft
 5. saves time and transport costs
Dangers
 6. criminals pretending to be agents ask for secret codes
 7. users forget to check the amount before confirming
 8. little use where the network is weak""", "text", title="A list of points (notes)"),
        T("This list has eight points. A good habit: write your notes in a few words each, so you do not copy sentences. The next lesson turns these notes into a summary."),
        IMG("f5en-vo-summary-steps.svg", alt="Four steps for a summary: read the task, mark the points, make notes, write the summary",
            caption="Figure 2. Four steps in summary writing. This lesson covers the first three."),
        MISTAKE("Copying whole sentences", "Do not underline and copy. Write short notes in your own words. Copying wastes words and is called lifting."),
        MISTAKE("Including your own ideas", "Use only what is in the passage. Do not add your own knowledge or opinion, even if it is true. The Board's report on directed writing makes the same point: use only the material given."),
        TIP("The Board's 2023 report describes Paper 1 as 50 multiple-choice questions, with reading comprehension as one part, and Paper 2 as Directed Writing and Composition. Your teacher will tell you whether a written summary is set in your class tests. Choosing relevant points and not lifting are skills you also need in directed writing, so practise them. Check with your teacher."),
        QUIZ("Which of these should be LEFT OUT of a summary on 'the advantages and dangers of mobile money'?",
             ["Criminals ask for secret codes", "Money can be sent quickly", "Mr Fon's mother lives in a village near Wum", "Weak networks limit the service"], 2,
             "The details about Mr Fon and his mother are an example, not a general point.",
             hint="Which point is only about one named person?",
             feedback=["This is a danger, and the task asks for dangers.", "This is an advantage.", "", "This is a danger."]),
        QUIZ("Two notes read 'saves time' and 'does not take long'. What should you do?",
             ["Keep both because they are in the passage", "Keep one, since they repeat the same idea", "Remove both", "Write both in full sentences"], 1,
             "Repeated ideas count once, so you keep one.",
             hint="Do the notes add a new idea?",
             feedback=["Repeating wastes words.", "", "The idea is relevant, so keep it once.", "That makes the summary longer, not shorter."]),
        PQ("Read: 'In many towns, plastic bags are thrown into drains. When the rains come, the drains block, and water floods the roads and houses. Flooding spreads diseases such as cholera. Moreover, burning plastic fills the air with harmful smoke. To solve the problem, councils should provide bins, shops should charge for bags, and citizens should reuse bags or use baskets.' "
           "Make notes of the problems caused by plastic bags only.",
           "Drains block; floods roads and houses; spreads diseases (cholera); burning gives harmful smoke. (The solutions are not asked for.)"),
        PQ("In the same plastic bags passage, which is an example and not a main point: 'blocked drains' or 'cholera'?",
           "Cholera is an example of a disease; the main point is that flooding spreads diseases. (You may keep the example only if you have words to spare; the general point is enough.)"),
        PQ("List three kinds of detail that you remove when you select points for a summary.",
           "Examples (named people and places), repeated ideas, and illustration or background that does not answer the task."),
        SUM("A summary keeps the main points in fewer words and in your own words.",
            "Read the task first; it tells you what to select.",
            "Remove examples, repetition, illustration and points the task does not ask for.",
            "Make short notes, not copied sentences.",
            "Check your list against the task before you write."),
    ],
))

# ------------------------------------------------------------------ 16. Summary 2
LESSONS.append(lesson(
    module=M4, topic="Summary writing",
    title="Summary writing 2: paraphrasing and writing the final summary",
    slug="evo-summary-paraphrase-write",
    minutes=25,
    summary="Turn your notes into a short paragraph in your own words. Learn four ways to paraphrase, join ideas with correct connectives, keep to the word limit, and see a full model summary.",
    objectives=[
        "Paraphrase a sentence by changing words and structure",
        "Join points into continuous prose with correct connectives",
        "Count words and keep to the limit",
        "Write a complete model summary from a list of points",
    ],
    key_concepts=["Paraphrase", "Lifting", "Connective", "Continuous prose", "Word limit"],
    blocks=[
        H("Introduction"),
        T("Your notes are ready. Now you must write them as a summary. The rule is simple: say the same thing in fewer words, with your own words, in one paragraph of continuous sentences. "
          "This lesson shows how."),
        D("To **paraphrase** is to express the meaning of a text in different words. **Lifting** is copying the words of the passage without changing them.", title="Paraphrase"),
        H("Four ways to paraphrase"),
        KEY("Change the words, the class, the structure or the length", "Use at least one for every sentence.", cards=[
            ["1. Use synonyms", "'carry an envelope' becomes 'deliver a packet'. Do not change technical words that have no good synonym (for example 'mobile money', 'network')."],
            ["2. Change the word class", "'they save time' becomes 'time is saved'; 'afraid of theft' becomes 'fear theft less'."],
            ["3. Change the structure", "Active to passive, or change the order of the clauses."],
            ["4. Combine and shorten", "Put two short sentences into one: 'Traders use it. Parents use it.' becomes 'Traders and parents use it.'"],
        ]),
        CODE("""Passage (original)                              Paraphrase
Today he sends the money in less than a minute  Money can now be sent almost at once.
Farmers receive payments directly from buyers   Buyers pay farmers directly.
the service is of little use where the network  the service does not work well in
is weak                                         areas with a poor network
Some people lose money to criminals who         Criminals who act as agents steal
pretend to be agents                            money from some users.""", "text", title="Paraphrase examples"),
        H("Connectives and style"),
        T("Join the points with connectives that show the relationship: *and*, *also*, *however*, *therefore*, *so*, *because*, *in addition*, *moreover*, *furthermore*, *nevertheless*. "
          "The Board's report on directed writing warns about made-up connectives such as 'better still', 'more still', 'more again', 'further still' and 'nextly', and about writing 'moreso' as one word. Use only standard connectives. Do not repeat the same one in a sentence."),
        KEY("Style rules", "Check them before you finish.", cards=[
            ["One paragraph", "Unless the task says otherwise, write one paragraph of continuous prose, not a list."],
            ["Tense and person", "Use the present tense for general facts. Write in the third person: do not use 'I'."],
            ["No opinions", "Do not add your own view. Do not write 'The writer says'."],
            ["Word limit", "Count your words. Numbers and short words count as words. Stay within the limit."],
        ]),
        H("A model summary"),
        T("Task: In not more than 70 words, summarise the advantages of mobile money and the dangers connected with it. We use the notes from the last lesson."),
        T("**Model summary:**\n\n"
          "Mobile money lets people send, store and receive money and pay bills quickly by phone. Traders buy goods without cash and farmers are paid directly, so users save time and transport costs and are safer from theft. "
          "However, criminals pretending to be agents may steal secret codes, careless users may confirm wrong amounts, and the service is of little use where the network is weak."),
        EX("Worked example 1: from notes to sentences", intro="Turn notes 1 to 5 (the advantages) into sentences.", steps=[
            S("Start with the main subject", text="Mobile money lets people send, store and receive money and pay bills quickly by phone."),
            S("Join the uses and results", text="Traders and farmers use it for payments, so users save time and transport costs and are safer from theft."),
            S("Check for lifting", text="The passage says 'they save time and transport costs'. The summary says 'users save time and transport costs', which joins the point to a new sentence. Where you can, change more: 'users spend less time and money travelling'."),
            S("Result", text="Two sentences that contain all five advantages."),
        ]),
        EX("Worked example 2: count and trim", intro="A draft has 78 words. The limit is 70. What can you cut?", steps=[
            S("Look for repetition", text="Cut a repeated idea ('quickly' and 'in a short time')."),
            S("Look for unneeded words", text="Cut 'in the town of', 'as we all know', 'it is important to say that'."),
            S("Shorten phrases", text="'in order to' becomes 'to'; 'due to the fact that' becomes 'because'."),
            S("Recount", text="Stop when you are within 70 words and no main point has gone."),
        ]),
        MISTAKE("Lifting long phrases", "Copying 'criminals who pretend to be agents and ask for secret codes' word for word is lifting. Say 'criminals posing as agents trick users into giving secret codes'."),
        MISTAKE("Writing a list or two paragraphs", "A summary is continuous prose in one paragraph. Do not use numbers, bullet points or sub-headings."),
        MISTAKE("Using more words than allowed", "Going over the limit loses marks and the extra words are often not read. Count carefully and keep a few words in hand."),
        TIP("The Board's report says final answers in Paper 2 must be in black or blue ink, and any plan must be cancelled. Always read your work again and check your tenses, spelling and punctuation."),
        QUIZ("Which is the best paraphrase of 'Farmers receive payments directly from buyers'?",
             ["Farmers receive payments directly from buyers.", "Buyers pay farmers directly.", "Farmers are very lucky.", "Buyers are directly paid."], 1,
             "It keeps the meaning, changes the structure and uses fewer words.",
             hint="Which keeps the same meaning in different words?",
             feedback=["That is a copy (lifting).", "", "This adds an opinion and changes the meaning.", "This reverses who pays."]),
        QUIZ("Which connective is correct and standard?",
             ["Nextly", "Further still", "Moreover", "More again"], 2,
             "'Moreover' is a standard connective of addition. The others are not used in standard English.",
             hint="Which one is in your dictionary as a connective?",
             feedback=["'Nextly' is not standard.", "Not a standard connective.", "", "Not a standard connective."]),
        PQ("Paraphrase: 'People are less afraid of theft, and they save time and transport costs.'",
           "Sample: Users worry less about being robbed and spend less time and money travelling."),
        PQ("Rewrite to avoid lifting: 'Some people lose money to criminals who pretend to be agents and ask for secret codes.'",
           "Sample: Criminals posing as agents trick some users into giving secret codes, so they lose their money."),
        PQ("Count the words in the model summary and say whether it is within 70 words.",
           "The model summary has 65 words (counting each word, including 'and' and 'to'). It is within the limit of 70."),
        PQ("Write a summary of two sentences of the plastic bag passage: 'In many towns, plastic bags are thrown into drains. When the rains come, the drains block, and water floods the roads and houses. Flooding spreads diseases such as cholera. Moreover, burning plastic fills the air with harmful smoke.' (maximum 30 words).",
           "Sample: Plastic bags block drains, so rain floods roads and houses and spreads disease. Burning them also pollutes the air with harmful smoke. (22 words)"),
        SUM("Paraphrase by changing words, word class, structure and length.",
            "Do not lift: copying the passage word for word loses marks.",
            "Join the points with standard connectives into one paragraph of continuous prose.",
            "Use the third person, present tense for general facts, no opinions.",
            "Count the words, trim repetition, and keep within the limit."),
    ],
))
