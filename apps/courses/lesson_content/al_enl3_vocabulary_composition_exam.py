"""A Level English Language (0730), Lower Sixth: Vocabulary (7 lessons), Composition (7 lessons) and Examination, Paper 1 (1 lesson).

All passages, sample essays and examples are original and invented for teaching (names, places and figures are invented).
Spelling is British. Where textbooks differ we say 'check your textbook'.
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

LESSONS = []

# ------------------------------------------------------------------ V1. Word choice, redundancy and malapropism
LESSONS.append(lesson(
    module=M_V,
    topic=T_CHOICE,
    title="Choosing the right word: correctness, appropriateness, redundancy and malapropism",
    slug="enl3-word-choice-redundancy-malapropism",
    minutes=22,
    summary="A good word is correct in meaning, right for the reader and no longer than it needs to be. Learn to spot wrong words, words in the wrong register, redundant phrases and malapropisms.",
    objectives=[
        "Decide whether a word is correct in meaning and appropriate in register",
        "Remove redundant words and phrases without changing the meaning",
        "Recognise a malapropism and replace it with the intended word",
        "Choose the best word for a gap in a Paper 1 vocabulary question",
    ],
    key_concepts=["Correctness", "Appropriateness", "Register", "Redundancy", "Malapropism"],
    blocks=[
        H("Introduction"),
        T("A trader in Bamenda sends a text to a supplier: 'I want your goods now now, or else.' The supplier understands the words, but "
          "he feels insulted. The same trader writes to a bank manager: 'Hey boss, lend me money.' Both messages have the right idea and "
          "the wrong words for the reader. Choosing words is not only about meaning. It is also about who is reading and what you want."),
        T("In Paper 1, Section D (Vocabulary), you will meet questions such as 'Choose the word that best completes the sentence' or "
          "'Choose the sentence that is correct and clear'. This lesson gives you the tools: a test for correctness, a test for "
          "appropriateness, a way to cut redundancy and a way to catch malapropisms."),
        H("Correctness and appropriateness"),
        D("A word is **correct** when its meaning, spelling and grammar fit the sentence. 'The council *banned* the new rule' and 'The council *ordered* the new rule' mean different things; if the writer meant to say the rule was introduced, one of the words is wrong. Always ask: does this word mean what I want to say?", title="Correctness"),
        D("A word is **appropriate** when its level of formality, its tone and its subject match the situation and the reader. "
          "This level of formality is called **register**. Formal writing (an application, a report, an examination essay) uses full forms and "
          "careful words. Informal writing (a message to a friend) can use slang and short forms.", title="Appropriateness and register"),
        KEY("Same idea, three registers", "Notice how the choice of word changes the effect.", cards=[
            ["Informal", "The kids were mad about the rubbish. They asked the chief to sort it out."],
            ["Neutral", "The children were angry about the rubbish. They asked the chief to deal with it."],
            ["Formal", "The residents were indignant about the accumulation of refuse. They petitioned the chief to resolve the matter."],
        ]),
        TIP("In examination essays and formal letters, write in neutral to formal register. Avoid slang ('guys', 'stuff', 'a lot of kids'), text-message "
            "forms ('u', 'gonna') and heavy, rare words that you are not sure of. A simple word used correctly beats a grand word used wrongly."),
        H("Redundancy"),
        D("**Redundancy** (also called **pleonasm** or **tautology**) means using more words than needed, or repeating an idea that the "
          "word already contains. Cutting redundancy makes writing clear and strong.", title="Redundancy"),
        KEY("Common redundant phrases", "The part in brackets adds nothing, so remove it.", cards=[
            ["Repeated meaning", "return (back); repeat (again); revert (back); join (together); merge (together); reflect (back)"],
            ["Meaning already inside the noun", "(free) gift; (past) history; (future) plans; (final) outcome; (unexpected) surprise; (advance) warning"],
            ["Empty intensifiers", "(absolutely) essential; (completely) unique; (very) unique; (totally) destroyed; (close) proximity"],
            ["Wordy phrases", "'due to the fact that' becomes 'because'; 'in the event that' becomes 'if'; 'at this point in time' becomes 'now'; 'the reason is because' becomes 'the reason is that'"],
        ]),
        H("Malapropism"),
        D("A **malapropism** is the mistaken use of a real word in place of another word that sounds similar, so the sentence "
          "becomes wrong or funny. The writer meant one word but used another that sounds a little like it. The name comes from Mrs Malaprop, a comic "
          "character in an eighteenth-century play.", title="Malapropism"),
        T("Compare these invented examples. The wrong word is a real English word, so a spell-checker will not catch it."),
        CODE("Wrong word used            Word intended\n"
             "a conscience worker         conscientious\n"
             "a great assent to the town  asset\n"
             "for all intensive purposes  for all intents and purposes\n"
             "a sedative lifestyle        sedentary\n"
             "the pacific question        the specific question", "text", title="Malapropisms and the words intended"),
        T("How do you catch one? Read the sentence slowly and ask whether the word makes sense in this place. A 'sedative lifestyle' makes no "
          "sense, because a sedative is a calming medicine. A person who sits all day has a *sedentary* lifestyle."),
        H("Worked examples"),
        EX("Worked example 1: correct but not appropriate",
           intro="A student writes in a letter to the Divisional Officer: 'Our school needs a new borehole badly because the old one is rubbish and the kids are suffering.' Rewrite it in a suitable register.",
           steps=[
               S("Find the informal words", text="'badly', 'rubbish' and 'kids' are informal for a letter to an official."),
               S("Replace each one", text="'badly' becomes 'urgently'; 'rubbish' becomes 'no longer working'; 'kids' becomes 'pupils'."),
               S("Write the sentence", text="Our school urgently needs a new borehole because the old one is no longer working and the pupils are suffering."),
           ]),
        EX("Worked example 2: removing redundancy",
           intro="Rewrite without redundancy: 'The reason why the road was closed is because of the fact that the bridge collapsed in the past year.'",
           steps=[
               S("Spot the repeats", text="'The reason why ... is because' repeats the idea of cause. 'Because of the fact that' is a wordy way to say 'because'. 'In the past year' is fine, but 'collapsed' already places it in the past."),
               S("Choose one clear link", text="Use only 'because'."),
               S("Rewrite", text="The road was closed because the bridge collapsed last year."),
           ]),
        EX("Worked example 3: finding the malapropism",
           intro="Which word is wrong? 'The headmaster was very adverse to latecomers, so he locked the gate at 7.30.'",
           steps=[
               S("Test the meaning", text="*Adverse* means harmful or unfavourable (adverse weather). A person who dislikes something is *averse* to it."),
               S("Replace", text="'adverse' should be 'averse'. The sentence now reads: The headmaster was very averse to latecomers."),
           ]),
        MISTAKE("Using a long word to sound clever",
                "Writers sometimes replace a simple word with a rare one they half-know, and produce a malapropism ('the visitor was *infamous* for his kindness' when "
                "they meant *famous*). Use a word only if you are sure of its meaning and can use it in a sentence of your own."),
        MISTAKE("Cutting a word that carries meaning",
                "Not every repeated word is redundant. 'He walked slowly and carefully' has two different ideas. Redundancy means the word adds "
                "NO new meaning. Test: if you remove it and the meaning is unchanged, it was redundant."),
        TIP("Paper 1 vocabulary questions on word choice often ask you to pick the sentence without redundancy, or the word that best fits a "
            "formal sentence. Read all four options before choosing, and test each wrong option for a clear fault: wrong meaning, wrong register or repeated meaning."),
        QUIZ("Which sentence contains redundancy?",
             ["The committee will meet on Friday.", "Please return back the books to the library.", "She completed the exercise carefully.", "The bridge collapsed after the storm."],
             1, "'Return' already means 'go or give back', so 'back' repeats the idea. The sentence should read 'Please return the books to the library.'",
             hint="Look for a word that repeats the meaning of another word.",
             feedback=["Nothing is repeated.", "", "'Carefully' adds how she did it, so it is not redundant.", "'After the storm' gives the time and adds information."]),
        QUIZ("Which word best completes the sentence in a formal report? 'The committee ______ the proposal because of the cost.'",
             ["binned", "rejected", "chucked out", "ditched"],
             1, "'Rejected' is neutral to formal. The other three are informal or slang and are not suitable in a report.",
             hint="Think about register: which word would you write in a report?",
             feedback=["Slang.", "", "Informal.", "Informal."]),
        PQ("Rewrite in a suitable formal register: 'The kids in our area are mad because there is no electricity and the council guys do nothing.'",
           "Suggested answer: 'The children in our area are angry because there is no electricity and the council officials have taken no action.' "
           "(kids to children, mad to angry, guys to officials, 'do nothing' to a formal verb phrase.) Other suitable wordings are accepted."),
        PQ("Remove the redundancy: 'The new teacher joined together with the staff to plan future plans for the end of term.'",
           "'The new teacher joined the staff to plan for the end of term.' ('joined together' repeats; 'future plans' repeats because plans are always for the future.)"),
        PQ("The sentence 'She is a very conscience student who revises every night' contains a malapropism. Name the wrong word, the word intended and its meaning.",
           "Wrong word: 'conscience' (a person's sense of right and wrong, a noun). Intended: 'conscientious' (careful and hard-working). "
           "Corrected: 'She is a very conscientious student who revises every night.'"),
        PQ("Explain the difference between a word that is correct and a word that is appropriate. Give one example of a word that is correct but not appropriate in an examination essay.",
           "A correct word has the right meaning, spelling and grammar. An appropriate word also suits the reader, the subject and the level of formality. "
           "Example: 'kids' is correct English for children, but it is informal and not appropriate in an examination essay; 'children' is appropriate."),
        SUM("A good word is correct in meaning and appropriate in register for the reader.",
            "Redundancy is the use of words that add no new meaning (return back, free gift, future plans). Cut them.",
            "A malapropism is a real word wrongly used in place of a similar-sounding word (conscience for conscientious).",
            "Use only words whose meaning you are sure of; a simple, accurate word is better than a rare, doubtful one.",
            "In Paper 1, test each option for wrong meaning, wrong register or repeated meaning."),
    ],
))

# ------------------------------------------------------------------ V2. Connotation and figures of speech
LESSONS.append(lesson(
    module=M_V,
    topic=T_CONN,
    title="Connotation and figures of speech",
    slug="enl3-connotation-figures-of-speech",
    minutes=22,
    summary="Words carry feelings as well as meanings. Learn denotation and connotation, then recognise and use the common figures of speech: simile, metaphor, personification, hyperbole, irony, oxymoron, euphemism, understatement, alliteration, onomatopoeia, metonymy and pun.",
    objectives=[
        "Distinguish denotation from connotation and rank words as positive, neutral or negative",
        "Recognise the common figures of speech in a sentence",
        "Explain the effect of a figure of speech in one sentence",
        "Use a figure of speech accurately in your own writing",
    ],
    key_concepts=["Denotation", "Connotation", "Simile", "Metaphor", "Personification", "Hyperbole", "Irony", "Euphemism"],
    blocks=[
        H("Introduction"),
        T("Three people describe the same man who spends little money. One says he is *thrifty*. Another says he is *economical*. A third says he is *stingy*. "
          "All three words mean 'careful with money', yet the first two sound like praise and the third sounds like blame. "
          "The feeling a word carries, beyond its dictionary meaning, is its **connotation**."),
        T("The syllabus asks you to recognise 'simple connotations and figures of speech'. In Paper 1 you may be asked which word has a negative "
          "meaning, which figure of speech a sentence uses, or what a phrase suggests."),
        H("Denotation and connotation"),
        D("The **denotation** of a word is its basic dictionary meaning. The **connotation** is the extra feeling, attitude or association that the word carries. "
          "Connotations can be **positive**, **neutral** or **negative**.", title="Denotation and connotation"),
        KEY("Same meaning, different feeling", "Each card gives three words for the same idea, from positive to negative.", cards=[
            ["slim / thin / skinny", "positive / neutral / negative"],
            ["thrifty / careful with money / stingy", "positive / neutral / negative"],
            ["determined / firm / stubborn", "positive / neutral / negative"],
            ["confident / sure of himself / arrogant", "positive / neutral / negative"],
            ["childlike / young in manner / childish", "positive / neutral / negative"],
        ]),
        T("Writers choose connotations on purpose. A newspaper that calls a crowd 'protesters' sounds neutral, 'activists' sounds positive and 'rioters' sounds negative. "
          "As a reader, notice which word was chosen. As a writer, choose the word whose feeling matches your purpose."),
        MISTAKE("Using a word with the wrong feeling",
                "A student wants to praise her teacher and writes 'Madam Njoh is very strict and bossy'. 'Strict' is mildly neutral, but 'bossy' is negative. "
                "Check the connotation of every adjective that describes a person."),
        H("Figures of speech"),
        D("A **figure of speech** uses words in a non-literal way to make an idea clearer, stronger or more interesting. "
          "The words mean something different from their ordinary, literal meaning.", title="Figure of speech"),
        KEY("The main figures of speech", "Learn the name, the idea and an example for each.", cards=[
            ["Simile", "Compares two things using 'like' or 'as'. Example: The market was as busy as an anthill."],
            ["Metaphor", "Says one thing IS another, without 'like' or 'as'. Example: The market was an anthill."],
            ["Personification", "Gives human actions or feelings to something that is not human. Example: The old bridge groaned under the lorry."],
            ["Hyperbole", "Deliberate exaggeration for effect. Example: I have told you a thousand times to close the gate."],
            ["Understatement", "Deliberately makes something sound smaller than it is. Example: The flood caused a little inconvenience to the town (when it destroyed many homes)."],
            ["Irony", "Says or shows the opposite of what is meant, or an outcome opposite to what is expected. Example: A fire station burned down."],
            ["Oxymoron", "Joins two words of opposite meaning. Example: a deafening silence; bitter sweet."],
            ["Euphemism", "A gentler word for something unpleasant. Example: 'passed away' for 'died'."],
            ["Alliteration", "Repeats the same starting sound in nearby words. Example: The busy bus bumped over the bad road."],
            ["Onomatopoeia", "A word whose sound imitates the sound it names. Example: buzz, sizzle, splash."],
            ["Metonymy", "Uses the name of something closely linked to stand for the thing meant. Example: The Crown (the monarchy); the press (journalists)."],
            ["Pun", "A joke playing on a word with two meanings or two similar sounds. Example: 'The baker was fired because he kneaded the dough' (needed / kneaded)."],
        ]),
        TIP("Simile or metaphor? Look for 'like' or 'as'. If the comparison has one of them, it is a simile. If one thing simply IS the other, it is a metaphor. "
            "Remember that 'as' is also an ordinary word: 'as he left' is not a simile."),
        H("Explaining the effect"),
        T("Naming a figure is only half the answer. Examiners also want its effect. Use this pattern: name the figure, say what it compares or does, and "
          "say what it makes the reader feel or understand."),
        EX("Worked example 1: name and effect",
           intro="'The sun was a furnace over the motor park.' Name the figure and explain its effect.",
           steps=[
               S("Check for like or as", text="There is no 'like' or 'as'. The sun IS a furnace. So it is a metaphor."),
               S("What is compared?", text="The sun is compared to a furnace, a place of fierce heat."),
               S("Effect", text="It makes the reader feel how fierce and uncomfortable the heat was. Answer: metaphor; it shows the heat was fierce and hard to bear."),
           ]),
        EX("Worked example 2: ranking connotations",
           intro="Arrange in order from most positive to most negative: sly, clever, cunning.",
           steps=[
               S("Check the meaning", text="All three describe a person who is good at getting what he wants by thinking."),
               S("Check the feeling", text="'Clever' is positive (praise for intelligence). 'Cunning' is negative (clever in a dishonest way). 'Sly' is also negative and suggests secret tricks."),
               S("Order", text="clever, cunning, sly. (Dictionaries may rank 'cunning' and 'sly' close together; the key point is that 'clever' is positive and the other two are negative.)"),
           ]),
        EX("Worked example 3: tell the figures apart",
           intro="Name the figure in each: (a) 'Her words were music to my ears.' (b) 'The wind whispered through the maize.' (c) 'I'm so hungry I could eat a whole goat.' (d) 'My uncle has gone to be with his ancestors.'",
           steps=[
               S("(a)", text="Words are music: a metaphor (no 'like' or 'as')."),
               S("(b)", text="The wind does something only a human can do (whisper): personification."),
               S("(c)", text="Eating a whole goat is an exaggeration: hyperbole."),
               S("(d)", text="A gentle way to say 'has died': euphemism."),
           ]),
        MISTAKE("Calling every comparison a simile",
                "Only a comparison with 'like' or 'as' is a simile. 'Life is a journey' is a metaphor. 'Life is like a journey' is a simile."),
        MISTAKE("Explaining the figure but not the effect",
                "Writing 'This is a simile' earns little. Add what the comparison shows or makes you feel, in your own words."),
        TIP("Exam link: Paper 1 Sections A and D can ask you to identify a figure of speech or the connotation of a word. Section A (Reading comprehension) "
            "also tests figures of speech in a passage. Read the whole sentence before you decide."),
        QUIZ("Which sentence contains personification?",
             ["The classroom was as hot as an oven.", "The old taxi coughed and refused to start.", "He is the king of the football pitch.", "We waited for ages."],
             1, "A taxi cannot cough or refuse. Giving human actions to a non-human object is personification.",
             hint="Which sentence gives something non-human a human action?",
             feedback=["That is a simile ('as hot as').", "", "That is a metaphor.", "'Ages' exaggerates: hyperbole."]),
        QUIZ("Which word has the most negative connotation?",
             ["frugal", "economical", "stingy", "careful"],
             2, "'Stingy' suggests unwillingness to spend, even when it is right to do so. The others are neutral or positive.",
             hint="Which word would the person described be least happy to hear?",
             feedback=["Positive or neutral: careful with money.", "Positive: avoids waste.", "", "Neutral."]),
        PQ("Identify the figure of speech in each: (a) 'The thunder roared in anger.' (b) 'The exam was a piece of cake.' (c) 'It was an honest lie.' (d) 'Seven shy sisters sold silk.'",
           "(a) personification (thunder roars in anger like an animal or a person). (b) metaphor (idiomatic: the exam was very easy). (c) oxymoron ('honest' and 'lie' are opposites). "
           "(d) alliteration (repeated s sound). Note: (b) is also an idiom; the figure used in the idiom is metaphor."),
        PQ("Two words describe a man who does not talk much: 'reserved' and 'sullen'. Which is more positive? Explain the difference.",
           "'Reserved' is more positive or neutral: the man keeps his feelings to himself, perhaps from modesty or shyness. 'Sullen' is negative: it suggests he is gloomy, bad-tempered and unfriendly. "
           "Both mean 'quiet' but they carry different attitudes."),
        PQ("Explain the effect of the simile in this sentence: 'The students sat as still as stones while the headmaster read the results.'",
           "The comparison to stones shows that the students did not move at all. It makes the reader feel how tense, nervous or frightened they were while waiting for the results."),
        PQ("Write one sentence with a metaphor and one with a simile, each about a market in the rainy season.",
           "Model answer: Metaphor: The market in the rainy season is a brown river of mud and umbrellas. Simile: The market in the rainy season is as slippery as a freshly oiled floor. "
           "(Any correct metaphor without 'like'/'as' and any correct simile with 'like' or 'as' is accepted.)"),
        SUM("Denotation is the dictionary meaning; connotation is the feeling or attitude a word carries (positive, neutral or negative).",
            "Choose the word whose connotation matches your purpose and your reader.",
            "A simile uses 'like' or 'as'; a metaphor says one thing IS another; personification gives human actions to non-human things.",
            "Hyperbole exaggerates; understatement plays down; irony shows the opposite of what is expected; oxymoron joins opposites; euphemism softens.",
            "In answers, name the figure AND explain its effect."),
    ],
))

# ------------------------------------------------------------------ V3. Affixes and word formation
LESSONS.append(lesson(
    module=M_V,
    topic=T_AFF,
    title="Prefixes, suffixes and the ways English forms new words",
    slug="enl3-affixes-word-formation",
    minutes=23,
    summary="Learn the common prefixes and suffixes, the spelling changes they cause, and the main ways English makes new words: affixation, compounding, conversion, blending, clipping, acronyms and back-formation.",
    objectives=[
        "Name the root, prefix and suffix in a word",
        "Choose the correct negative prefix (un-, in-, im-, il-, ir-, dis-, non-)",
        "Form nouns, adjectives, verbs and adverbs from a root with the right suffix and spelling",
        "Identify compounding, conversion, blending, clipping, acronyms and back-formation",
    ],
    key_concepts=["Root", "Prefix", "Suffix", "Compounding", "Conversion", "Blending", "Clipping", "Back-formation"],
    blocks=[
        H("Introduction"),
        T("A student in Buea meets the word *unemployable* for the first time. She has never seen it, yet she can work out its meaning: "
          "*un-* (not) + *employ* (give work to) + *-able* (able to be). The word breaks into parts, and each part has a meaning. "
          "Knowing the common parts lets you work out thousands of words and form the right word in a gap-filling question."),
        T("The Board's syllabus lists two items: **affixes** (prefixes and suffixes) and **the formation of words**. Paper 1, Section D, tests both: "
          "you may be asked for the opposite of a word, the correct form of a word to fill a gap, or the process by which a word was made."),
        H("Root, prefix and suffix"),
        D("A **root** (or **base**) is the main part of a word that carries its core meaning (*happy*, *employ*, *act*). "
          "A **prefix** is a group of letters added to the front of a root; it changes the meaning (*un*happy). "
          "A **suffix** is added to the end; it usually changes the word class (noun, verb, adjective, adverb) (happi*ness*). "
          "Prefixes and suffixes together are called **affixes**.", title="Root, prefix, suffix"),
        KEY("Common prefixes", "A prefix changes the meaning but not usually the word class.", cards=[
            ["Negative: un-, in-, im-, il-, ir-, dis-, non-, mis-", "unkind, incomplete, impossible, illegal, irregular, disagree, nonsense, misunderstand"],
            ["Again / back: re-", "rewrite, return, reconsider"],
            ["Before / after: pre-, post-", "prepare, preview; postpone, postgraduate"],
            ["Against / opposite: anti-, counter-", "antibiotic, anticlockwise; counterattack"],
            ["Between / across: inter-, trans-", "international, interact; transport, transfer"],
            ["Position / degree: sub-, super-, over-, under-, mid-", "subway, supermarket, overcrowded, underpaid, midnight"],
            ["Together / out of: co-, ex-", "co-operate, coexist; export, ex-president"],
            ["Wrong / bad: mal-, mis-", "malnutrition, misuse"],
        ]),
        KEY("Common suffixes", "A suffix usually decides the word class.", cards=[
            ["Noun suffixes", "-ness (kindness), -ment (agreement), -tion/-sion (decision), -ity (honesty, ability), -ship (friendship), -hood (childhood), -er/-or (teacher, doctor), -ist (artist), -ism (tourism), -ance/-ence (importance, absence)"],
            ["Adjective suffixes", "-ful (helpful), -less (hopeless), -able/-ible (comfortable, possible), -ous (dangerous), -ive (active), -al (national), -ic (economic), -y (rainy), -ish (childish), -ent/-ant (different, important)"],
            ["Verb suffixes", "-ify (simplify), -ise/-ize (modernise), -en (widen), -ate (activate)"],
            ["Adverb suffix", "-ly (quickly, happily)"],
        ]),
        H("The negative prefixes: which one?"),
        T("English has several ways to make a word negative. There is no single rule that covers every word, but these patterns help."),
        CODE("un-    most common; used with native English adjectives and participles:\n"
             "        unhappy, unkind, unable, untidy, unknown\n"
             "in-    from Latin words: incomplete, inactive, invisible, incorrect\n"
             "im-    before b, m, p:  impossible, immature, imbalance, impolite\n"
             "il-    before l:        illegal, illogical, illiterate\n"
             "ir-    before r:        irregular, irrelevant, irresponsible\n"
             "dis-   dislike, disagree, disappear, dishonest, disobey\n"
             "non-   nonsense, non-stop, non-fiction\n"
             "mis-   wrongly: misunderstand, misspell, mislead", "text",
             title="Negative prefixes"),
        TIP("Check your dictionary when you are not sure which prefix to use. Forms such as 'unpossible' or 'inhappy' do not exist in standard English. "
            "Only a dictionary can tell you which prefix a word takes."),
        H("Spelling when you add a suffix"),
        CODE("1. Final -e is dropped before a suffix that starts with a vowel:\n"
             "     hope + ing = hoping      create + ion = creation\n"
             "   but kept before a consonant:  hope + ful = hopeful   care + less = careless\n"
             "   exceptions: noticeable, courageous (keep the e to keep the soft c/g sound)\n"
             "2. Consonant + y: change y to i before a suffix (but not before -ing):\n"
             "     happy + ness = happiness   carry + ed = carried   but carry + ing = carrying\n"
             "3. One syllable, one vowel, one consonant at the end: double the consonant:\n"
             "     stop + ing = stopping   big + er = bigger\n"
             "   For longer words, double only if the last syllable is stressed:\n"
             "     begin + ing = beginning   but visit + ing = visiting\n"
             "4. The suffix -ful has one l: careful, useful. The adverb adds -ly: carefully, usefully", "text",
             title="Four spelling rules for suffixes"),
        H("Other ways of forming words"),
        KEY("How English makes new words", "Affixation is only one method.", cards=[
            ["Compounding", "Two words joined: classroom, sunrise, mother-in-law, blackboard, motorbike."],
            ["Conversion", "A word changes class without any change in form: to text (verb, from noun 'a text'); a run (noun from verb); to google. Also called zero derivation."],
            ["Blending", "Parts of two words combine: brunch (breakfast + lunch), smog (smoke + fog), motel (motor + hotel), Spanglish."],
            ["Clipping", "A long word is shortened: exam (examination), ad (advertisement), phone (telephone), lab (laboratory)."],
            ["Acronym", "Initial letters said as a word: UNESCO, NATO, AIDS; or as letters (an initialism): BBC, CRTV, GCE."],
            ["Back-formation", "A new word made by cutting what looks like a suffix from an older word: edit from editor; burgle from burglar; televise from television."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: analysing a word",
           intro="Analyse the word 'unfaithfulness' into root, prefix and suffixes and give its word class.",
           steps=[
               S("Find the root", text="faith (noun)."),
               S("Add the suffixes in order", text="faith + ful = faithful (adjective); faithful + ness = faithfulness (noun)."),
               S("Add the prefix", text="un + faithfulness = unfaithfulness. The word is a noun."),
               S("Answer", text="Prefix un-; root faith; suffixes -ful and -ness; the word is a noun meaning lack of loyalty."),
           ]),
        EX("Worked example 2: choose the right form",
           intro="Fill the gap with the correct form of the word in brackets: 'The ______ of the new library pleased everyone.' (open)",
           steps=[
               S("Decide the word class needed", text="After 'The' and before 'of' we need a noun."),
               S("Form the noun from 'open'", text="open + ing = opening (the noun for the act or event of opening)."),
               S("Answer", text="opening. (The adjective 'open' or the adverb 'openly' would not fit.)"),
           ]),
        EX("Worked example 3: how was the word formed?",
           intro="Say how each word was formed: (a) brunch (b) gym (c) ECOWAS (d) bookshelf (e) to email.",
           steps=[
               S("(a) brunch", text="Blend of breakfast + lunch."),
               S("(b) gym", text="Clipping of gymnasium."),
               S("(c) ECOWAS", text="Acronym, said as a word."),
               S("(d) bookshelf", text="Compound: book + shelf."),
               S("(e) to email", text="Conversion: the noun 'email' used as a verb."),
           ]),
        MISTAKE("Wrong spelling when adding a suffix",
                "Writers often forget to drop the silent e (hopeing), forget to change y to i (happyness), or forget to double the consonant (stoping). "
                "Learn the four rules above and check each time you add a suffix."),
        MISTAKE("Using the wrong word class",
                "'She is a very success woman' needs the adjective 'successful'. 'He decided to quickly' fails because 'quickly' needs a verb to follow. "
                "Before filling a gap, decide whether you need a noun, a verb, an adjective or an adverb."),
        TIP("Exam link: Paper 1 vocabulary questions give a sentence with a gap and a word to change, or ask for the opposite of a word, or ask what a prefix or suffix "
            "does. Always identify the word class the gap needs before you choose."),
        QUIZ("Which prefix makes the opposite of 'responsible'?",
             ["un-", "dis-", "in-", "ir-"],
             3, "Before r the negative prefix is ir-: irresponsible.",
             hint="The word starts with r.",
             feedback=["'Unresponsible' is not standard English.", "'Disresponsible' is not standard English.", "'Inresponsible' is not standard English; in- changes to ir- before r.", ""]),
        QUIZ("Which spelling is correct?",
             ["beginning", "begining", "beggining", "begginning"],
             0, "Begin ends in one vowel and one consonant with stress on the last syllable, so the n is doubled: beginning.",
             hint="The stress is on the second syllable: be-GIN.",
             feedback=["", "The final consonant must be doubled.", "The g is not doubled; the n is.", "Only the final consonant n is doubled."]),
        PQ("Form (a) a noun from 'decide', (b) an adjective from 'danger', (c) a verb from 'wide', (d) an adverb from 'happy'.",
           "(a) decision; (b) dangerous; (c) widen; (d) happily. (Remember: happy changes y to i before -ly.)"),
        PQ("Give the opposite of each by adding a prefix: legal, patient, correct, possible, regular, honest.",
           "illegal, impatient, incorrect, impossible, irregular, dishonest."),
        PQ("Explain how each of these words was formed: smog, ad, sunrise, to text.",
           "smog: blend of smoke + fog; ad: clipping of advertisement; sunrise: compound (sun + rise); to text: conversion (noun used as a verb)."),
        PQ("Break 'misunderstanding' into its parts and say what each part adds.",
           "mis- (prefix: wrongly) + understand (root: grasp the meaning) + -ing (suffix: makes a noun from the verb). The word means a wrong understanding of something."),
        SUM("A root carries the core meaning; prefixes change meaning, suffixes usually change the word class.",
            "Use un-, in-, im- (before b, m, p), il- (before l), ir- (before r), dis- and non- as negative prefixes; check your dictionary.",
            "When adding a suffix: drop silent e before a vowel, change y to i after a consonant, double the final consonant if the syllable is stressed.",
            "Words are also made by compounding, conversion, blending, clipping, acronyms and back-formation.",
            "Decide the word class a gap needs before choosing the form."),
    ],
))

# ------------------------------------------------------------------ V4. Synonyms, antonyms, homonyms and homophones
LESSONS.append(lesson(
    module=M_V,
    topic=T_SYN,
    title="Synonyms, antonyms, homonyms and homophones",
    slug="enl3-synonyms-antonyms-homonyms-homophones",
    minutes=21,
    summary="Words are related by meaning (synonyms, antonyms) and by sound or spelling (homophones, homonyms, homographs). Learn to choose the synonym that fits the context, find the true opposite, and avoid homophone errors.",
    objectives=[
        "Choose the synonym that best fits a sentence, not just any near-meaning",
        "Identify the antonym of a word and the type of opposite it is",
        "Distinguish homophones, homonyms and homographs",
        "Use the right homophone in a sentence",
    ],
    key_concepts=["Synonym", "Antonym", "Homophone", "Homonym", "Homograph"],
    blocks=[
        H("Introduction"),
        T("A market woman in Limbe says her tomatoes are *fresh*. A customer says the water is *fresh* (not salty). The fish seller says the fish is *fresh* (not old). One word, three meanings. "
          "Another day, the same customer writes 'I want to *by* some tomatoes' and loses a mark, because *by* and *buy* sound the same but are spelt differently. "
          "This lesson sorts out how words are related by meaning, and how they are confused by sound and spelling."),
        T("The syllabus names four relations: **synonyms**, **antonyms**, **homonyms** and **homophones**. Paper 1, Section D, may ask for a word closest in meaning, "
          "a word opposite in meaning, or the correct homophone in a sentence."),
        H("Synonyms"),
        D("**Synonyms** are words with the same or nearly the same meaning (*begin* / *start*; *big* / *large*). "
          "Few synonyms are exactly alike. They usually differ in strength, register or the words they go with.", title="Synonym"),
        T("Compare 'ask', 'request' and 'demand'. All mean to try to get something by speaking, but 'request' is polite and formal, "
          "while 'demand' is strong and may sound rude. Likewise 'small', 'tiny' and 'minute' differ in degree."),
        KEY("Choosing the right synonym", "Three tests when a question asks for the closest meaning.", cards=[
            ["1. Meaning in context", "A word may have several meanings. 'Fine' means 'thin' in 'fine thread' but 'good' in 'a fine day'. Read the whole sentence."],
            ["2. Strength", "'Angry', 'furious' and 'annoyed' differ in strength. Match the degree."],
            ["3. Register and partners", "'Commence' is formal; 'start' is neutral. We say 'heavy rain', not 'strong rain'; 'strong tea', not 'heavy tea'."],
        ]),
        H("Antonyms"),
        D("**Antonyms** are words with opposite meanings. There are three common kinds.", title="Antonym"),
        KEY("Types of antonym", "Knowing the type helps you find the true opposite.", cards=[
            ["Gradable", "A scale with a middle: hot / cold (warm and cool are between). 'Not hot' does not mean 'cold'."],
            ["Complementary", "One or the other, nothing between: alive / dead; present / absent; true / false. 'Not alive' means dead."],
            ["Relational (converse)", "Two sides of one relationship: buy / sell; teacher / pupil; parent / child; above / below."],
        ]),
        T("Many words have a different antonym in each meaning. The opposite of *light* is *heavy* (weight) but *dark* (brightness). "
          "The opposite of *fresh* is *stale* (bread) or *salty* (water). Always check the meaning in the sentence first."),
        H("Homophones, homonyms and homographs"),
        D("**Homophones** are words that sound the same but differ in spelling and meaning: *write / right*, *flour / flower*. "
          "**Homonyms** (in the strict sense) are words with the same spelling AND the same sound but different meanings: *bank* (of a river / for money), *bat* (animal / for cricket). "
          "**Homographs** have the same spelling but different sounds and meanings: *lead* /li:d/ (to guide) and *lead* /led/ (a metal); *tear* /tɪə/ (from the eye) and *tear* /teə/ (to rip).", title="Homophones, homonyms, homographs"),
        TIP("Textbooks differ on these terms. Some books use 'homonym' for both homophones and homographs. In the examination, read what the question asks for and check your textbook."),
        CODE("their / there / they're       knew / new         write / right / rite\n"
             "to / too / two               hear / here        weather / whether\n"
             "piece / peace                weak / week        wait / weight\n"
             "plain / plane                tail / tale        sail / sale\n"
             "meet / meat                  steel / steal      sea / see\n"
             "bored / board                break / brake      course / coarse\n"
             "principal / principle        stationary / stationery\n"
             "flour / flower               role / roll        which / witch", "text",
             title="Homophones to learn (British English)"),
        H("Worked examples"),
        EX("Worked example 1: the closest synonym in context",
           intro="Choose the word closest in meaning to 'reluctant' in 'The manager was reluctant to sign the form.' A. eager B. unwilling C. able D. quick",
           steps=[
               S("Understand the word", text="'Reluctant' means not wanting to do something."),
               S("Test the options", text="'Eager' is the opposite; 'able' and 'quick' do not fit the meaning."),
               S("Answer", text="B. unwilling."),
           ]),
        EX("Worked example 2: the antonym",
           intro="Choose the opposite of 'generous' in 'a generous donation': A. large B. selfish C. kind D. rich",
           steps=[
               S("Meaning in context", text="'Generous' means ready to give more than is expected."),
               S("Find the opposite", text="A person unwilling to give is selfish (or mean). 'Large' is about size; 'kind' is close in meaning; 'rich' is about wealth."),
               S("Answer", text="B. selfish."),
           ]),
        EX("Worked example 3: the right homophone",
           intro="Choose the correct word: 'The ______ of the school welcomed the visitors.' (principal / principle)",
           steps=[
               S("Meanings", text="*Principal* = the head of a school (noun) or main (adjective). *Principle* = a rule or belief."),
               S("Fit the sentence", text="A person welcomes visitors, so we need the head of the school."),
               S("Answer", text="principal. Memory aid: the principal is your pal."),
           ]),
        MISTAKE("Choosing a word that is related but not a synonym",
                "'Rich' and 'wealthy' are synonyms. 'Rich' and 'expensive' are not: a person is rich, but a car is expensive. Words in the same topic are not always synonyms."),
        MISTAKE("Spell-checkers do not catch homophones",
                "'I went too the market' is spelt with real words, so the computer may not flag it. Reread your essay for there/their/they're, to/too/two, your/you're and its/it's."),
        TIP("Exam link: Paper 1, Section D. If a question gives a word in a sentence, answer for the meaning in THAT sentence. For antonyms, check the part of speech: "
            "the opposite of a verb is a verb."),
        QUIZ("Which word is a gradable antonym of 'hot'?",
             ["cold", "alive", "present", "buy"],
             0, "Hot and cold are opposite ends of a scale of temperature, so they are gradable antonyms.",
             hint="Which pair has 'warm' and 'cool' somewhere in between?",
             feedback=["", "Alive/dead is a complementary pair, not related to hot.", "Present/absent is complementary and unrelated to hot.", "Buy/sell is relational and unrelated to hot."]),
        QUIZ("Which sentence uses the correct homophone?",
             ["The whether was cold and wet.", "She could not decide weather to go.", "We will go whether it rains or not.", "He asked the whether man for help."],
             2, "'Whether' introduces a choice or condition ('whether it rains or not'). 'Weather' is about rain, sun and wind.",
             hint="One word is about the atmosphere; the other introduces a choice.",
             feedback=["'Weather' is needed here: the weather was cold.", "'Whether' is needed here (weather means rain, sun...).", "", "'Weather' is needed: the weather man."]),
        PQ("Give a synonym and an antonym of 'ancient'.",
           "Synonyms: old, aged, very old. Antonyms: modern, new, recent. (Any correct answer is accepted.)"),
        PQ("Write two sentences that show the difference between the homophones 'piece' and 'peace'.",
           "Model answer: She ate a piece of cake. After the war, the country longed for peace. (Piece = a part of something; peace = calm without war.)"),
        PQ("The word 'lead' can be pronounced /li:d/ or /led/. What name is given to a pair of words like this, and what does each mean?",
           "They are homographs (same spelling, different sound and meaning). /li:d/ means to guide or be in front; /led/ is a heavy grey metal. Check your textbook for the term used in your course."),
        PQ("Choose the correct word and explain: 'The (stationary / stationery) shop sells pens, paper and rulers.'",
           "stationery. 'Stationery' (spelt with -er) means writing materials and is a noun. 'Stationary' (with -ar) means not moving. A memory aid: stationEry has E for envelope."),
        SUM("Synonyms have nearly the same meaning but differ in strength, register and partner words; choose by context.",
            "Antonyms are opposites: gradable (hot/cold), complementary (alive/dead), relational (buy/sell). The antonym may change with the meaning.",
            "Homophones sound alike and are spelt differently; homonyms share spelling and sound; homographs share spelling but differ in sound. Textbooks vary.",
            "Spell-checkers do not catch homophone errors: proofread for them.",
            "Always answer for the meaning in the given sentence."),
    ],
))

# ------------------------------------------------------------------ V5. Words often confused
LESSONS.append(lesson(
    module=M_V,
    topic=T_CONF,
    title="Words often confused",
    slug="enl3-words-often-confused",
    minutes=22,
    summary="Pairs such as affect/effect, advice/advise and lose/loose cause many errors. Learn the meaning, class and a memory aid for the most common confused words, and test your choice by substituting a meaning.",
    objectives=[
        "Give the meaning and word class of the commonly confused pairs",
        "Use affect/effect, advice/advise, practice/practise, lose/loose and similar pairs correctly",
        "Apply a memory aid or a substitution test when unsure",
        "Correct confusion errors in a short text",
    ],
    key_concepts=["Confused words", "Noun and verb pairs", "Substitution test", "Memory aid"],
    blocks=[
        H("Introduction"),
        T("A candidate writes: 'The new law will have a big *affect* on traders.' The idea is right and the sentence is clear, but the word is wrong: "
          "the noun is *effect*. A single confused word may not cost many marks, but in Paper 1 whole questions are built on these pairs, and in Paper 2 and Paper 3 "
          "they reduce your accuracy mark."),
        T("The syllabus says candidates will be tested on 'words often confused'. The list is open, so we cannot list every pair. "
          "Instead, we teach the most common pairs and a method you can use on any pair."),
        H("A method for any confused pair"),
        KEY("Three questions", "Use them whenever you are not sure.", cards=[
            ["1. What word class is needed?", "Is the gap a noun, a verb, an adjective? Many pairs differ by class (advice is a noun; advise is a verb)."],
            ["2. What do I mean?", "Say the meaning in other words, then test which word has that meaning."],
            ["3. Is there a memory aid?", "Use a trick: A for Affect is an Action (verb); E for Effect is the End result (noun)."],
        ]),
        H("Noun and verb pairs (often spelt with c and s)"),
        CODE("advice (noun)      advise (verb)\n"
             "   Take my advice.        I advise you to wait.\n"
             "practice (noun)    practise (verb)    [British English]\n"
             "   Football practice.     She practises every day.\n"
             "licence (noun)     license (verb)     [British English]\n"
             "   a driving licence.     The council licenses the market.\n"
             "prophecy (noun)    prophesy (verb)\n"
             "device (noun)      devise (verb)\n"
             "   a safety device.       They devised a plan.\n"
             "effect (noun)      affect (verb)\n"
             "   the effect of rain.    Rain affects crops.", "text",
             title="Pairs where the noun has c and the verb has s"),
        TIP("In American English 'practice' is used for both noun and verb. In British English, which the Board's papers follow, 'practice' is the noun and 'practise' the verb. "
            "If your textbook differs, follow your teacher, but be consistent."),
        H("Pairs of different meaning"),
        CODE("accept (receive)           except (leave out; apart from)\n"
             "affect (influence)         effect (result)  [effect as a verb = bring about]\n"
             "principal (head; main)     principle (rule, belief)\n"
             "stationary (not moving)    stationery (writing materials)\n"
             "lose (not win; misplace)   loose (not tight)\n"
             "then (at that time)        than (comparing)\n"
             "complement (complete)      compliment (praise)\n"
             "council (a group)          counsel (advice; to advise)\n"
             "quiet (silent)             quite (fairly; completely)\n"
             "personal (private)         personnel (staff)\n"
             "precede (come before)      proceed (go on)\n"
             "ensure (make certain)      insure (cover with insurance)    assure (promise to someone)\n"
             "elicit (draw out)          illicit (illegal)\n"
             "eminent (famous)           imminent (about to happen)\n"
             "sensible (practical)       sensitive (easily hurt; reacting quickly)\n"
             "born (given birth)         borne (carried)\n"
             "lie, lay, lain (rest)      lay, laid, laid (put down)", "text",
             title="Pairs with different meanings"),
        H("Everyday troublemakers"),
        KEY("Small words that cause big errors", "Memorise these four-in-one sets.", cards=[
            ["its / it's", "its = belonging to it (The dog wagged its tail). it's = it is or it has (It's raining)."],
            ["your / you're", "your = belonging to you. you're = you are."],
            ["who's / whose", "who's = who is or who has. whose = belonging to which person."],
            ["fewer / less", "fewer + countable nouns (fewer pupils). less + uncountable nouns (less water)."],
            ["borrow / lend", "borrow = take for a time. lend = give for a time. 'Can you lend me your pen?' not 'borrow me'."],
            ["bring / take", "bring = carry towards the speaker; take = carry away from the speaker."],
            ["farther / further", "Both can be used for distance. 'Further' also means 'more' or 'additional' (further information). Check your textbook."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: noun or verb?",
           intro="Choose the correct word: 'The doctor gave me good ______ , so I ______ you to see her too.' (advice / advise)",
           steps=[
               S("First gap", text="After 'good' we need a noun: advice."),
               S("Second gap", text="After 'I' we need a verb: advise."),
               S("Answer", text="advice; advise."),
           ]),
        EX("Worked example 2: use the meaning",
           intro="Choose the right word: 'Everyone came to the party ______ Peter, who was ill.' (accept / except)",
           steps=[
               S("Say the meaning", text="The sentence means 'everyone but Peter'. We need 'apart from'."),
               S("Match", text="'Except' means apart from. 'Accept' means to receive or agree to."),
               S("Answer", text="except."),
           ]),
        EX("Worked example 3: correct the text",
           intro="Correct the confused words: 'Its important to practice your english every day, because it will effect your results. Their are fewer mistakes when you loose your fear.'",
           steps=[
               S("Its", text="'It's' (it is) important."),
               S("practice", text="Verb after 'to', so 'practise' (British English)."),
               S("effect", text="Verb meaning 'influence', so 'affect'."),
               S("Their", text="'There are' (there = exists)."),
               S("loose", text="Verb meaning 'not win/misplace', so 'lose'. The corrected text reads: It's important to practise your English every day, because it will affect your results. There are fewer mistakes when you lose your fear. (Also capital E in English.)"),
           ]),
        MISTAKE("Trusting the sound of a word",
                "Many confused words sound alike, so your ear cannot help. Check the meaning and word class instead, and learn the memory aids."),
        MISTAKE("Writing 'alot', 'alright' and 'infact'",
                "Write 'a lot' (two words) and 'in fact' (two words). 'Alright' is widely used but many teachers and examiners prefer 'all right' in formal writing. 'Altogether' (entirely) and 'all together' (everyone together) are different."),
        TIP("Exam link: Paper 1, Section D asks you to choose the right word in a sentence. Paper 3, Section C (Editing) tests your ability to correct such errors; Paper 2 essays are marked for accuracy. "
            "Make your own list of the pairs you get wrong and revise it weekly."),
        QUIZ("Choose the correct sentence.",
             ["The weather will effect the match.", "The weather will affect the match.", "The weather will have an affect on the match.", "The weather will have a affect on the match."],
             1, "'Affect' is the verb: the weather will influence the match.",
             hint="Which word is a verb here?",
             feedback=["'Effect' is a noun (or rarely 'bring about').", "", "After 'an' we need the noun 'effect', not 'affect'.", "Same error as the third option, and 'a' before a vowel sound should be 'an'."]),
        QUIZ("Which word completes the sentence? 'She is ______ tired to walk home.'",
             ["to", "too", "two", "tow"],
             1, "'Too' means 'more than is needed'. 'Too tired' to walk shows an excess.",
             hint="Which word means 'more than enough' here?",
             feedback=["'To' is a preposition or part of an infinitive.", "", "'Two' is the number.", "'Tow' means to pull."]),
        PQ("Choose the right word: (a) The (principal / principle) reason for the delay was rain. (b) It is against my (principal / principle) to lie.",
           "(a) principal (main). (b) principle (a rule or belief)."),
        PQ("Correct the errors: 'Can you borrow me your dictionary? I will bring it back after lunch, and I will give it to the personal officer.'",
           "'Can you lend me your dictionary? I will bring it back after lunch ...' 'Borrow' should be 'lend'. 'Bring it back' is acceptable (bringing it towards the speaker); and 'personal officer' should be 'personnel officer' (the officer in charge of staff)."),
        PQ("Write sentences showing the difference between 'compliment' and 'complement'.",
           "Model answer: The head girl paid her a compliment on her speech (praise). The red scarf complements her black dress (completes or goes well with it)."),
        PQ("Explain why 'There are less pupils in Form 4 this year' is incorrect, and correct it.",
           "'Pupils' can be counted, so we need 'fewer'. Corrected: There are fewer pupils in Form 4 this year. ('Less' is used with uncountable nouns such as water or money.)"),
        SUM("Use three questions on any confused pair: what word class, what meaning, what memory aid?",
            "In British English, noun/verb pairs often use c for the noun and s for the verb: advice/advise, practice/practise, licence/license.",
            "Learn the common pairs: affect/effect, accept/except, principal/principle, lose/loose, then/than, complement/compliment, council/counsel.",
            "Small words matter: its/it's, your/you're, who's/whose, fewer/less, borrow/lend, bring/take.",
            "Spell-checkers cannot decide for you: check the meaning every time."),
    ],
))

# ------------------------------------------------------------------ V6. Idioms and figurative expressions
LESSONS.append(lesson(
    module=M_V,
    topic=T_IDIOM,
    title="Idioms and figurative expressions",
    slug="enl3-idioms-figurative-expressions",
    minutes=21,
    summary="An idiom is a fixed expression whose meaning cannot be guessed from its words. Learn how to read idioms and proverbs, the common ones, and the traps: changing the wording, reading them literally and mixing metaphors.",
    objectives=[
        "Explain what an idiom is and how it differs from a literal phrase",
        "Give the meaning of at least twenty common idioms and proverbs",
        "Complete an idiom correctly without changing its wording",
        "Choose the idiom that fits a context and avoid mixed metaphors",
    ],
    key_concepts=["Idiom", "Figurative expression", "Proverb", "Fixed wording", "Mixed metaphor"],
    blocks=[
        H("Introduction"),
        T("A mother in Douala tells her son, 'Stop beating about the bush and tell me where the money went.' The boy looks around the yard. "
          "Of course there is no bush. She means 'Stop avoiding the point and speak directly.' "
          "The words together mean something different from the words separately. That is an **idiom**."),
        T("The syllabus lists 'expressions: figurative; idiomatic'. Paper 1, Section D, may ask for the meaning of an idiom, "
          "the idiom that completes a sentence, or the sentence in which an idiom is used correctly. "
          "Idioms also lift your essay writing, when used naturally and accurately."),
        H("What is an idiom?"),
        D("An **idiom** is a fixed group of words whose meaning is different from the meanings of the separate words. "
          "You cannot work out an idiom by translating word for word, and you cannot change its words.", title="Idiom"),
        D("A **figurative expression** uses words in a non-literal way (a metaphor, simile, hyperbole). "
          "A **proverb** is a short traditional saying that gives advice or states a truth ('A stitch in time saves nine'). "
          "Many idioms are figurative, but not every figurative expression is fixed like an idiom.", title="Figurative expressions and proverbs"),
        CODE("break the ice            start a conversation in an awkward situation\n"
             "burn the midnight oil    work late into the night\n"
             "a blessing in disguise   something that seems bad but turns out good\n"
             "cost an arm and a leg    be very expensive\n"
             "let the cat out of the bag   reveal a secret by mistake\n"
             "spill the beans          reveal a secret\n"
             "hit the nail on the head say exactly the right thing\n"
             "under the weather        slightly ill\n"
             "once in a blue moon      very rarely\n"
             "bite the bullet          face something unpleasant bravely\n"
             "the last straw           the final problem that makes you lose patience\n"
             "turn a blind eye         pretend not to see something wrong\n"
             "a piece of cake          something very easy\n"
             "beat about the bush      avoid the main point\n"
             "sit on the fence         refuse to take a side\n"
             "call it a day            stop working for the day\n"
             "pull someone's leg       tease someone in fun\n"
             "in the nick of time      just before it is too late\n"
             "cut corners              do a job badly to save time or money\n"
             "keep an eye on           watch carefully\n"
             "a storm in a teacup      much fuss about something small", "text",
             title="Twenty-one common idioms"),
        H("Some common proverbs"),
        KEY("Proverbs and their meanings", "Proverbs are often used to end an argument or give advice.", cards=[
            ["A stitch in time saves nine", "Deal with a small problem early before it grows."],
            ["Too many cooks spoil the broth", "If too many people try to do one job, it goes wrong."],
            ["All that glitters is not gold", "Things that look attractive may not be valuable."],
            ["Practice makes perfect", "You improve by repeating a skill."],
            ["Don't count your chickens before they hatch", "Do not rely on a success that has not happened yet."],
            ["Where there is a will there is a way", "A determined person can find a solution."],
            ["A bird in the hand is worth two in the bush", "A sure thing is better than a possible bigger gain."],
            ["Do not judge a book by its cover", "Appearances can mislead."],
        ]),
        TIP("Proverbs from our own languages say much the same things. Translating a home-language proverb word for word may confuse an English reader, "
            "so in an examination use English proverbs and idioms you know well."),
        H("Rules for using idioms"),
        KEY("Four rules", "Keep these in mind when you write.", cards=[
            ["1. Keep the wording", "Say 'cost an arm and a leg', not 'cost a hand and a leg'. Do not change words, singular/plural or order."],
            ["2. Change only the verb form", "Idioms allow normal changes of tense: 'He spilled the beans', 'She is burning the midnight oil'."],
            ["3. Match the register", "Many idioms are informal ('a piece of cake'). In a formal letter use plain words or a safer expression."],
            ["4. Do not mix metaphors", "'We must nip this problem in the bud before it snowballs out of control' mixes plants and snow. Choose one picture."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: the meaning",
           intro="What does 'turned a blind eye' mean in 'The inspector turned a blind eye to the broken fence'? A. He could not see. B. He pretended not to notice. C. He closed his eyes. D. He fixed it.",
           steps=[
               S("Do not translate literally", text="The inspector did not literally turn his eye."),
               S("Use the idea", text="The idiom means to pretend not to see a fault on purpose."),
               S("Answer", text="B."),
           ]),
        EX("Worked example 2: complete the idiom",
           intro="Choose the word that completes the idiom: 'It was only a small leak, but when the water reached the books it was the last ______.' A. bucket B. drop C. straw D. stone",
           steps=[
               S("Recall the idiom", text="'The last straw' (the final problem that is too much). The idiom comes from 'the last straw that breaks the camel's back'."),
               S("Check the others", text="'Last drop' is a phrase about liquid but not this idiom; 'last bucket' and 'last stone' are not idioms."),
               S("Answer", text="C. straw."),
           ]),
        EX("Worked example 3: mixed metaphor",
           intro="Explain what is wrong with: 'The minister is walking on thin ice, but he has a card up his sleeve and is burning bridges.'",
           steps=[
               S("List the pictures", text="Thin ice, a card up the sleeve (cheating at cards) and burning bridges are three separate pictures."),
               S("State the problem", text="Mixing them confuses the reader: the sentence does not give one clear image."),
               S("Repair", text="Use one idea: 'The minister is walking on thin ice, and one more mistake may cost him his job.'"),
           ]),
        MISTAKE("Changing the wording of an idiom",
                "'It's raining cats and dogs' is correct; 'It's raining dogs and cats' is not. 'Kill two birds with one stone' not 'kill two birds by one stone'. Learn each idiom as a unit."),
        MISTAKE("Reading an idiom literally",
                "If a phrase makes no sense word for word, it may be an idiom. 'He kicked the bucket' means he died, not that he kicked a bucket. Ask what the whole phrase suggests in the context."),
        MISTAKE("Overusing idioms in an essay",
                "One or two apt idioms add colour; a paragraph packed with them sounds forced and clumsy. Use them where they fit naturally."),
        TIP("Exam link: Paper 1 Section D tests idioms and figurative expressions, often by asking which meaning fits or which idiom completes a sentence. "
            "In Section A the questions on words in context may include idioms inside a passage."),
        QUIZ("What does 'a blessing in disguise' mean?",
             ["A prayer said quietly", "Something that seems bad but has a good result", "A gift hidden in a box", "A person wearing a costume"],
             1, "A 'blessing in disguise' is a bad-looking event that turns out well. Missing the bus and then meeting your future employer on the next one is an example.",
             hint="The word 'disguise' tells you the good thing is hidden.",
             feedback=["Too literal.", "", "Too literal.", "Too literal."]),
        QUIZ("Which is the correct idiom?",
             ["He was over the moon about the results.", "He was over the sun about the results.", "He was on the moon about the results.", "He was under the moon about the results."],
             0, "'Over the moon' means extremely happy. The wording is fixed.",
             hint="Which preposition and which heavenly body does the idiom use?",
             feedback=["", "The word is moon, not sun.", "Wrong preposition and not the idiom.", "Wrong preposition."]),
        PQ("Explain the meaning of each: (a) a piece of cake, (b) under the weather, (c) burn the midnight oil.",
           "(a) something very easy; (b) feeling slightly ill; (c) work late into the night, for example to study."),
        PQ("Rewrite using an idiom from this lesson: 'The students did not know what to do, so they started a conversation to relax everyone at the new school.'",
           "'The students did not know what to do, so they broke the ice at the new school.' (Break the ice = start a conversation in an awkward situation.)"),
        PQ("Choose and complete: 'When the headmaster found out who had broken the window, he did not punish the boy, because he decided to ______ a blind eye.' State the idiom and its meaning.",
           "'turn'. The idiom 'turn a blind eye' means to pretend not to see something wrong."),
        PQ("Explain what the proverb 'Don't count your chickens before they hatch' teaches, and use it in a sentence about a football match.",
           "It teaches that we should not rely on a success that has not happened yet. Model sentence: The team had not yet scored, but its fans were already celebrating; as the coach said, they should not count their chickens before they hatch."),
        SUM("An idiom is a fixed group of words whose meaning is different from its parts; you cannot change the wording.",
            "A proverb is a short traditional saying that gives advice or states a truth.",
            "Learn the common idioms and proverbs as units with their meanings.",
            "Avoid literal reading, wording changes, mixed metaphors and too many idioms.",
            "In Paper 1, ask what the whole phrase suggests in context."),
    ],
))

# ------------------------------------------------------------------ V7. Spelling
LESSONS.append(lesson(
    module=M_V,
    topic=T_SPELL,
    title="Spelling: rules, patterns and commonly misspelt words",
    slug="enl3-spelling",
    minutes=22,
    summary="English spelling has more patterns than people think. Learn the main rules (ie/ei, plurals, endings, doubling), British spellings, the commonly misspelt words and a simple way to learn and check them.",
    objectives=[
        "Apply the main spelling rules for ie/ei, plurals, silent e, y to i and doubling",
        "Use British spellings consistently (colour, centre, organise, travelled)",
        "Spell at least forty commonly misspelt words",
        "Use a learn-and-check routine to cut spelling errors in your own writing",
    ],
    key_concepts=["Spelling rule", "ie / ei", "Plurals", "Doubling", "British spelling", "Commonly misspelt words"],
    blocks=[
        H("Introduction"),
        T("Two candidates write about the same thing. One spells *government*, *necessary* and *environment* correctly. The other writes *goverment*, *neccessary* and *enviroment*. "
          "Both have good ideas, but the second looks careless, and in Paper 2 the accuracy mark and the expression mark are both affected."),
        T("The syllabus lists 'spelling' as a Vocabulary topic, and 'common words should be spelt correctly' is a requirement in the composition assessment. "
          "In Paper 1, Section D, you may be asked to choose the correct spelling or to spot the misspelt word."),
        H("Rules that work"),
        KEY("Rule 1: i before e, except after c", "When the sound is /i:/ (as in see).", cards=[
            ["i before e", "believe, achieve, field, piece, thief, relief, brief"],
            ["except after c", "receive, receipt, deceive, ceiling, perceive"],
            ["Exceptions", "seize, weird, protein, either, neither, caffeine. Note also science, species, ancient, society: here c is followed by ie, but the sound is not /i:/."],
            ["ei with a different sound", "eight, neighbour, weigh, reign, foreign, height"],
        ]),
        KEY("Rule 2: plurals", "Most nouns add -s. Others follow patterns.", cards=[
            ["-s, -x, -z, -ch, -sh", "add -es: buses, boxes, churches, wishes"],
            ["consonant + y", "change y to ies: city to cities, baby to babies. (vowel + y: add s: boys, keys)"],
            ["-f / -fe", "often change to ves: leaf to leaves, knife to knives, life to lives; but roofs, chiefs, beliefs"],
            ["-o", "potatoes, tomatoes, heroes; but photos, pianos, radios"],
            ["Irregular", "man to men, woman to women, child to children, foot to feet, tooth to teeth, person to people"],
        ]),
        KEY("Rule 3: adding endings", "Review from the lesson on affixes.", cards=[
            ["Silent e", "Drop before a vowel ending: hope to hoping, create to creation. Keep before a consonant: hopeful, careless."],
            ["Consonant + y", "Change y to i: happy to happiness, carry to carried, but carrying."],
            ["Doubling", "Double the final consonant when the syllable is stressed and ends in one vowel + one consonant: stop to stopping, begin to beginning, occur to occurred; visit to visiting."],
            ["Keep both letters", "unnecessary (un + necessary), dissatisfied (dis + satisfied), misspell (mis + spell), meanness (mean + ness), accidentally."],
        ]),
        KEY("British spelling", "The Board's papers follow British English; be consistent.", cards=[
            ["-our", "colour, honour, neighbour, favourite, labour"],
            ["-re", "centre, metre, theatre, litre"],
            ["-ise / -ize", "organise or organize, realise or realize: both are accepted in British English. Choose one and stay with it. (Words like advertise, supervise, surprise always have -ise.)"],
            ["Doubled l", "travelled, cancelled, travelling, counsellor, jewellery"],
            ["-ence / -ense", "licence (noun), defence, offence, practise (verb); the American forms are license, defense, offense, practice"],
        ]),
        H("Forty words to master"),
        CODE("accommodation   achieve       address       argument     beginning\n"
             "believe         business      calendar      committee    conscience\n"
             "definitely      develop       disappear     disappoint   embarrass\n"
             "environment     February      foreign       government   guarantee\n"
             "height          independent   interrupt     knowledge    library\n"
             "necessary       neighbour     occasion      occurrence   parliament\n"
             "possession      privilege     receive       recommend    restaurant\n"
             "separate        successful    tomorrow      Wednesday    whether", "text",
             title="Commonly misspelt words"),
        TIP("Look for the tricky part and make a memory aid. necessary: one Collar and two Sleeves (one c, two s). separate: there is 'a rat' in sep-a-rate. "
            "accommodation: two c's and two m's. Weak spots differ for everybody, so make your own aids."),
        H("A routine for learning spellings"),
        KEY("Look, cover, write, check", "Five minutes a day works better than one hour a week.", cards=[
            ["1. Look", "Look at the word; notice the tricky part."],
            ["2. Say", "Say it in syllables: Wed-nes-day, Feb-ru-ar-y."],
            ["3. Cover and write", "Cover the word and write it from memory."],
            ["4. Check", "Compare letter by letter; if wrong, start again."],
            ["5. Keep a list", "Keep a notebook of your own misspelt words, and test yourself weekly."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: choose the correct spelling",
           intro="Which is correct? A. recieve B. receive C. receeve D. riceive",
           steps=[
               S("Sound", text="The vowel sound is /i:/."),
               S("Rule", text="After c we write ei: rec-ei-ve."),
               S("Answer", text="B. receive."),
           ]),
        EX("Worked example 2: add the ending",
           intro="Add the endings: (a) occur + ed (b) hope + ing (c) happy + ly (d) travel + er (British).",
           steps=[
               S("(a) occur + ed", text="The stress is on the second syllable (oc-CUR), so double r: occurred."),
               S("(b) hope + ing", text="Drop the silent e: hoping."),
               S("(c) happy + ly", text="Change y to i: happily."),
               S("(d) travel + er", text="British English doubles the l: traveller."),
           ]),
        EX("Worked example 3: find the misspelt word",
           intro="Which word is misspelt? 'The goverment needs to protect the enviroment.'",
           steps=[
               S("Check each word", text="'The', 'needs', 'to', 'protect' are correct."),
               S("Misspelt words", text="'government' has an n before the m (govern + ment); 'environment' has an n before the m (environ + ment)."),
               S("Answer", text="goverment and enviroment are both misspelt."),
           ]),
        MISTAKE("Spelling by sound",
                "Many English words are not spelt as they sound: Wednesday, knowledge, February. When a word has silent letters or unusual vowel groups, learn it as a picture."),
        MISTAKE("Mixing British and American spellings",
                "Writing 'colour' in one line and 'color' in another loses marks for inconsistency. Choose British spelling throughout, as the Board's papers do."),
        MISTAKE("Relying on the spell-checker only",
                "A spell-checker accepts real words in the wrong place (there/their, form/from, principle/principal) and may suggest wrong words. In the examination you have no spell-checker, so build your own memory."),
        H("Correct English"),
        T("The last item of the Board's Vocabulary list is 'correct English used'. It means that every word you choose, spell and place must be right for standard English. "
          "In a vocabulary question, if two options mean the same, choose the one with correct spelling, correct word class and correct fixed phrases."),
        TIP("Exam link: Paper 1, Section D can ask for the correctly spelt word. In Paper 2, Section A, the accuracy mark rewards 'common words spelt correctly'. "
            "In Paper 3, Section C (Editing), spelling errors are among the errors you may need to correct."),
        QUIZ("Which word is spelt correctly?",
             ["accomodation", "accommodation", "acommodation", "accomodasion"],
             1, "Accommodation has double c and double m.",
             hint="The word has two doubled consonants.",
             feedback=["The m must be doubled.", "", "The c must be doubled.", "The ending is -tion and the m is doubled."]),
        QUIZ("Which is the plural of 'city'?",
             ["citys", "cityes", "cities", "citis"],
             2, "Consonant + y changes to ies.",
             hint="What comes before the y?",
             feedback=["Do not just add s after a consonant + y.", "Do not add es without changing y.", "", "The ending is ies, not is."]),
        PQ("Correct the spelling errors: 'The goverment recieved a letter from the neighbours about their enviroment and the occurence of floods.'",
           "government; received; environment; occurrence. ('neighbours' is correct British spelling.)"),
        PQ("Add the endings and write the new word: (a) begin + ing (b) happy + ness (c) argue + ment (d) refer + ed (e) visit + ing.",
           "(a) beginning; (b) happiness; (c) argument (the e is dropped, an exception); (d) referred (stress on the second syllable, so r is doubled); (e) visiting (stress on the first syllable, so no doubling)."),
        PQ("Write the British spellings of these American spellings: color, center, traveling, defense, organize.",
           "colour; centre; travelling; defence; organise (organize is also accepted in British English)."),
        PQ("Describe a routine you will use to learn ten words you often misspell.",
           "Model answer: I will keep a notebook of my own misspelt words. Each day I will look at the word, say it in syllables, cover it, write it from memory, and check letter by letter. I will test myself weekly and drop the words I get right three weeks in a row."),
        SUM("Apply the main rules: ie/ei, plurals, silent e, y to i and doubling.",
            "Use British spellings and be consistent: colour, centre, travelled, defence.",
            "Learn the commonly misspelt words, using memory aids.",
            "Use look, say, cover, write, check, and keep a list of your own errors.",
            "A spell-checker will not catch real words in the wrong place."),
    ],
))

NARR_ESSAY = (
    'The night bus to Bamenda was already forty minutes late when the driver finally honked three times and the whole motor park rose like a flock of startled birds. I was twelve, travelling alone for the first time, with a bag of my mother\'s roasted groundnuts in my lap and her last warning still ringing in my ears: "Do not talk to strangers, and do not fall asleep."\n\n'
    'By midnight the bus was climbing through thick fog. The headlamps made two weak tunnels in the white darkness, and the passengers had fallen silent. Beside me sat an old woman who hummed softly and clutched a basket of eggs. I kept my eyes open, as I had promised, and counted the bends in the road.\n\n'
    'Suddenly the engine coughed twice and died. The bus rolled backwards for a terrible second before the driver pulled the handbrake with a shriek of metal. "Everybody stay in your seats!" he shouted, but nobody listened. Voices rose, children cried, and somebody began to pray aloud. Through the window I saw nothing but fog and, below it, a darkness that seemed to have no bottom.\n\n'
    'The driver climbed down with a torch and returned with a face the colour of ash. A rear tyre had burst, and the spare was flat. We were stranded on a mountain road, miles from the nearest village, with a cliff on one side and a ditch on the other.\n\n'
    '"We must walk," a young man declared. "No, we must wait," argued another. Their quarrel grew louder until the old woman beside me stood up. She was small, but her voice cut through the noise like a knife. "Quiet, all of you! Panic will not mend a tyre. Who has a phone with credit?"\n\n'
    'Two phones appeared, but neither had a signal. Then I remembered something. At the last stop, I had noticed a signal tower on a hill behind the road, with a red light blinking at its top. "Madam," I said, my voice trembling, "there is a tower not far behind us. Perhaps the signal is better there."\n\n'
    'Everyone turned to look at me. For a moment I wished the ground would swallow me. Then the old woman smiled and said, "The child has eyes. Who will go with him?" The young man who had wanted to walk raised his hand, a little ashamed, and together we climbed the slope with the torch bobbing in front of us like a small, brave star.\n\n'
    'At the top, the bars on his phone flickered into life. He called the transport agency, gave our position, and promised help. When we came down, the passengers had lit a small fire of dry branches beside the road, and the old woman was sharing out boiled eggs from her basket. Nobody was frightened any more. They were singing.\n\n'
    'A rescue van arrived at dawn with a new tyre and a mechanic who yawned continuously. As the bus pulled away, the old woman pressed an egg into my palm. "You were not asleep," she whispered, "and you did not walk away from trouble."\n\n'
    'That night taught me two lessons that I have never forgotten. The first is that a warning from a mother is given in love, but wisdom sometimes means knowing when a stranger can become a friend. The second is that even the smallest person in a crowd may be the one who sees the light on the hill. When I think of that journey, I no longer remember the fear. I remember the fire, the singing, and the egg, still warm in my hand.'
)

def assess_key(focus_c, focus_e, focus_a):
    """The official three-part assessment, with advice for this essay type."""
    return KEY("How this essay is marked (20 marks)",
               "The Board assesses every Section A composition under three headings. Write at least 500 words: quality matters more than quantity, "
               "but marks are reduced in proportion if you write fewer.", cards=[
                   ["Content and organisation: 10 marks", focus_c],
                   ["Expression: 8 marks", focus_e],
                   ["Accuracy: 2 marks", focus_a],
               ])


IDENTITY = ("**Identity.** The Board tells candidates to use the name and address provided on the paper to conceal their identity. "
            "Never write your own name, school, town or other personal details in the essay. If a title asks for a letter or a signature, use only "
            "the name and address given on the paper, and follow the instruction on your own paper. Do not use obscene language.")

# ------------------------------------------------------------------ C1. Narrative essays
LESSONS.append(lesson(
    module=M_C,
    topic=T_NARR,
    title="Narrative essays: telling a story with shape and feeling",
    slug="enl3-narrative-essays",
    minutes=25,
    summary="A narrative essay tells a story about real or imagined events. Learn the story shape, how to open and end, how to use dialogue and detail, and study a full model essay marked against the Board's three headings.",
    objectives=[
        "Recognise a narrative title and choose a story you can tell well in 500 words or more",
        "Plan a story with an opening, a complication, a climax and an ending",
        "Use dialogue, sensory detail and varied sentences to bring a story alive",
        "Assess a narrative essay under content and organisation, expression and accuracy",
    ],
    key_concepts=["Narrative essay", "Plot", "Climax", "Dialogue", "Point of view", "Showing, not telling"],
    blocks=[
        H("Introduction"),
        T("Every Cameroonian family has a favourite story: the day the river flooded, the day an uncle came home from abroad, the night the lights failed during an exam. "
          "People remember these stories because they have a shape: something happens, trouble comes, and something changes. "
          "That is what a **narrative essay** is: a story told in an orderly, interesting and accurate way."),
        T("In Paper 2, Section A (Composition), you are given six topics and you write on one. Narrative is the first kind of topic named in the Board's syllabus, along with descriptive, "
          "expository and discursive, argumentative, open-ended and visual stimuli. The paper lasts 2 hours 15 minutes in all and Section A carries 20 marks. "
          "The topic may be a title such as 'The day I will never forget', or a sentence to finish such as 'It was then that I knew the truth'."),
        assess_key(
            "Is the story relevant to the title? Is it original and lively? Are the ideas in a logical order, in clear paragraphs, from introduction through development to conclusion? Does it suit the reader?",
            "A range of vocabulary and sentence patterns; clear and coherent language; apt and imaginative figures of speech; a tone that suits the story.",
            "Sentence structure without lapses; common words spelt correctly; punctuation that helps the reader (especially speech marks)."),
        H("The shape of a story"),
        D("**Plot** is the order in which events are told. Most stories follow five steps: **opening** (who, where, when), **complication** (the problem begins), "
          "**climax** (the most intense moment), **resolution** (how the problem ends) and **ending** (what has changed or been learnt).", title="Plot"),
        CODE("Opening          introduce the narrator, place, time (about 80-100 words)\n"
             "Complication     the problem begins; tension builds (about 150 words)\n"
             "Climax           the most exciting or frightening moment (about 150 words)\n"
             "Resolution       how the problem ends (about 100 words)\n"
             "Ending           what changed or was learnt (about 60-80 words)\n"
             "                 Total: 540 to 580 words", "text",
             title="A plan for about 550 words"),
        TIP("Do not try to tell a whole year in 500 words. A good narrative covers a short time (an hour, a night, a journey) and slows down at the climax."),
        H("Opening and ending"),
        KEY("Four ways to open", "Avoid the dull opening 'My name is...' and the long weather report.", cards=[
            ["Action", "Begin in the middle of events: 'The engine coughed twice and died.'"],
            ["Dialogue", "'Do not fall asleep,' my mother warned."],
            ["Setting with mood", "By half past five the sky over the motor park had turned the colour of a bruise."],
            ["A surprising statement", "I was twelve the first time I thought I would die."],
        ]),
        KEY("Four ways to end", "End with the change, not with a rushed 'and then I woke up'.", cards=[
            ["A lesson learnt", "State, in your own words, what the experience taught you."],
            ["An image", "Close on a picture that sums up the feeling."],
            ["A return to the opening", "Echo the first line to give the story a circle."],
            ["A twist", "A last small surprise, if it fits the story and does not feel forced."],
        ]),
        H("Techniques that bring a story alive"),
        KEY("Showing, not telling", "Tell the reader what the character does and senses, and let them feel the emotion.", cards=[
            ["Telling", "I was very afraid."],
            ["Showing", "My knees turned to water and my hands would not stop shaking."],
            ["Telling", "The market was crowded."],
            ["Showing", "Elbows, baskets and bicycles pressed in from every side, and I could not turn without bumping someone."],
        ]),
        D("**Dialogue** is the words characters say. Each speaker gets a new line. Use speech marks around the spoken words; the punctuation goes inside them. "
          "Example: \"Who has a phone?\" she asked. / \"Quiet, all of you,\" she said. Do not use too much: a few lines at the right moments do more than a page of talk.", title="Dialogue"),
        T("Use the five senses (sight, sound, smell, touch, taste), vary the length of your sentences (a short sentence can follow a long one for effect), and keep one point of view. "
          "Use the past tense for the story, and do not slip into the present by accident. Use first person ('I') for a personal story. If you use third person ('he', 'she'), say who is telling it."),
        T(IDENTITY),
        H("A model essay"),
        T("The essay below is original and was written for this lesson. It answers the title 'A journey I shall never forget'. It is about 600 words. Read it once for the story; then read the notes that follow."),
        T(NARR_ESSAY, title="Model essay: A journey I shall never forget"),
        H("How the model essay meets the criteria"),
        KEY("Reading the model against the three headings", "Notice how each heading is earned.", cards=[
            ["Content and organisation", "The title is answered directly. The opening sets up the journey and the mother's warning. The complication is the breakdown; the climax is the quarrel and the narrator's idea; the resolution is the call, the fire and the rescue. The ending states what was learnt and returns to the egg. The paragraphs each have one job."],
            ["Expression", "Figures of speech: 'like a flock of startled birds', 'cut through the noise like a knife', 'a small, brave star'. Mood is shown, not told ('a face the colour of ash'). Sentence length varies. The tone is suitable for a personal story."],
            ["Accuracy", "Tenses are consistent. Speech marks are used correctly; each new speaker begins a new paragraph or clearly changes. British spelling (colour, neighbour) is used. There are no run-on sentences."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: a plan for a title",
           intro="Title: 'The day the lights went out during my examination.' Make a plan.",
           steps=[
               S("Opening", text="Morning of the Mathematics paper; narrator nervous but well prepared; thick clouds. (80 words)"),
               S("Complication", text="Halfway through, the power fails; the hall goes dark; some candidates panic; the invigilator calls for calm. (150 words)"),
               S("Climax", text="Time is running out; the narrator moves to the window to catch the light; a classmate begins to cry. (150 words)"),
               S("Resolution", text="Candles are brought; the supervisor adds extra minutes; the narrator finishes. (100 words)"),
               S("Ending", text="What the narrator learnt about staying calm and helping others. (70 words)"),
           ]),
        EX("Worked example 2: telling to showing",
           intro="Rewrite to show, not tell: 'Mother was angry when I came home late.'",
           steps=[
               S("Pick two physical details", text="Her lips pressed into a thin line; the wooden spoon stopped in mid-air."),
               S("Add a sound or action", text="She did not shout; she only said my name once, very quietly."),
               S("Write", text="When I stepped through the door, Mother's lips pressed into a thin line and the wooden spoon froze in the air. She did not shout. She only said my name once, very quietly, and that was worse."),
           ]),
        EX("Worked example 3: punctuating dialogue",
           intro="Punctuate: where is the money asked the trader I gave it to your brother replied the boy.",
           steps=[
               S("Mark the first speaker", text="\"Where is the money?\" asked the trader."),
               S("Mark the second speaker (new line)", text="\"I gave it to your brother,\" replied the boy."),
               S("Check", text="Capital letter at the start of each speech; question mark inside the marks; comma inside the marks before 'replied'."),
           ]),
        MISTAKE("Too many events, too little detail",
                "A story that races through ten events in 500 words reads like a list. Choose two or three moments and tell them well."),
        MISTAKE("Changing tense in the middle of the story",
                "'I opened the door and I see a snake' mixes past and present. Keep to the past tense unless you have a clear reason."),
        MISTAKE("A rushed or weak ending",
                "'It was all a dream' or 'And that is how I learnt my lesson' with no detail leaves the reader unsatisfied. End with an image or an idea that follows from the story."),
        MISTAKE("Writing under 500 words",
                "A short essay loses marks in proportion. Keep an eye on your length: a handwritten page of about ten to twelve words per line and twenty-five lines is about 250-300 words, so plan about two full pages."),
        TIP("Exam link: Narrative titles are one of the six Section A choices. If you choose narrative, plan for five minutes and write about 550 words; leave five minutes to check tenses, speech marks and spelling."),
        QUIZ("Which opening is the most effective for a 550-word narrative?",
             ["My name is Mary and I want to tell you a story.", "The engine coughed twice and died; fog pressed against the windows.", "It was a nice day and the sun was shining as it usually does in our town.", "In this essay I will describe a day I remember."],
             1, "It starts in action, with a sound and a picture, and makes the reader want to know what happens next. The others announce the essay or give no interest.",
             hint="Which opening begins in the middle of events?",
             feedback=["It gives the name (against the identity rule) and announces instead of showing.", "", "Dull and general.", "It announces the essay; a story should simply begin."]),
        QUIZ("Which sentence shows rather than tells?",
             ["She was nervous.", "She was very very nervous.", "Her fingers twisted the corner of her scarf until it frayed.", "Nervousness filled her heart."],
             2, "The third sentence shows what she does, so the reader infers the nervousness.",
             hint="Which sentence uses a physical action?",
             feedback=["It tells.", "It tells with an intensifier.", "", "It tells in a clichéd way."]),
        PQ("Make a five-part plan (opening, complication, climax, resolution, ending) for the title 'A market day I will never forget'. Add a word target to each part.",
           "Model plan: Opening (80 words): early morning, the narrator helps an aunt carry tomatoes to the market. Complication (150): heavy rain floods the stalls and the aunt's money box is missing. "
           "Climax (150): the narrator sees a boy running away with the box and chases him through the crowd. Resolution (100): the boy is caught by traders; the money is found; the narrator is surprised to see the boy is hungry. "
           "Ending (70): the aunt gives the boy food; the narrator learns that anger and kindness can sit side by side. Total about 550 words. Any logical plan with the five parts is accepted."),
        PQ("Rewrite to show, not tell: 'The room was silent and everyone was afraid when the principal entered.'",
           "Model answer: When the principal stepped through the door, the chatter died as if someone had switched off a radio. Pens froze above exercise books, and somebody at the back swallowed loudly. "
           "(Any version that uses actions, sounds and details instead of the words silent and afraid.)"),
        PQ("Punctuate this dialogue correctly: do you have the key asked the caretaker its in the office answered the girl",
           "\"Do you have the key?\" asked the caretaker.\n\"It's in the office,\" answered the girl.\n(New line for each speaker; capital letter at the start of each speech; the question mark and comma inside the marks; the apostrophe in It's.)"),
        PQ("List three things the Board's assessment looks for in the content and organisation of a narrative essay, and two things in expression.",
           "Content and organisation: relevance to the topic; creativity and a lively imagination; logical arrangement of ideas and paragraphing; progression from introduction through development to conclusion; an appropriate point of view and a sense of audience. "
           "Expression: clarity and coherence; range and aptness of vocabulary; judicious and imaginative use of figurative language; tone suited to the reader."),
        SUM("A narrative essay tells a story with a shape: opening, complication, climax, resolution, ending.",
            "Cover a short time and slow down at the climax. Open with action or a strong picture and end with the change or lesson.",
            "Show, do not tell. Use dialogue sparingly, with correct speech marks, and keep one tense and one point of view.",
            "Marks: content and organisation 10, expression 8, accuracy 2; at least 500 words; conceal your identity; no obscene language.",
            "Plan for five minutes, write about 550 words, check for five minutes."),
    ],
))

DESC_ESSAY = (
    'Before the sun has properly climbed over the hills, Sunday market at Foumban is already awake. From the road it looks like a shifting patchwork of colour: red tomatoes piled in neat pyramids, green plantains stacked like firewood, and bright cloth hanging from poles like flags at a festival. Even before I enter, the market announces itself to my nose with the smell of woodsmoke and frying fish.\n\n'
    'At the gate, the noise rushes over me like a wave. Traders call out the price of their goods in three languages at once. A radio on a stall plays a lively tune, a goat bleats in protest, and the clang of a blacksmith\'s hammer beats a steady rhythm beneath it all. A boy pushes a loaded wheelbarrow through the crowd and shouts, "Excuse me, excuse me!" in a voice so cracked that he sounds like a rusty gate.\n\n'
    'The crowd itself is a living river. Women with babies tied to their backs weave between baskets, balancing enormous bowls of groundnuts on their heads with the grace of dancers. Old men in embroidered gowns sit under a mango tree, arguing happily over a draughts board. Schoolchildren in blue uniforms dart through the gaps, clutching coins and licking sticky pieces of sugarcane.\n\n'
    'In the food section the air grows thick and warm. Charcoal glows under a great black pot, and a plump woman stirs it with a wooden paddle as long as her arm. Spices rise from the steam and tickle my throat. Beside her, a heap of ripe mangoes glows gold, and their sweet scent mixes with the sharper smell of fresh pepper until my eyes water and my mouth fills with water.\n\n'
    'Further along, the craft stalls glitter in the growing heat. Carved stools stand in rows, their smooth wood polished to the colour of honey. Beaded necklaces catch the sunlight and throw tiny rainbows on the dusty ground. A young potter turns a damp clay bowl in her hands, her fingers leaving patient, curving lines, and the clay feels cool and rough when she offers it to me to touch.\n\n'
    "By midday, the market is at its fiercest. The sun beats down on the tin roofs until they shimmer, and the ground is hot beneath my sandals. Flies hum above the fish stalls, sweat runs down the traders' faces, and the shade of every umbrella is guarded jealously. Yet no one leaves. Bargaining continues in loud, good-humoured voices, and a trader laughs so heartily that the whole stall seems to shake.\n\n"
    'As evening approaches, the market slowly begins to sleep. Stalls are folded, baskets are emptied, and children carry the last bundles home on their heads. The colours soften to orange and purple in the low light, and the roar of the morning fades to a murmur. A single lamp flickers on, and the smell of woodsmoke returns, now mixed with the quiet smell of dust settling.\n\n'
    'I have visited many places, but none has taught my senses so much as that market. It is noisy, crowded and hot, yet it is also generous, warm and alive. When I close my eyes I can still hear the hammer, smell the mangoes and see the colours dancing, and I know that the market, like the village itself, is a heartbeat that never quite stops.'
)

# ------------------------------------------------------------------ C2. Descriptive essays
LESSONS.append(lesson(
    module=M_C,
    topic=T_DESC,
    title="Descriptive essays: painting a place, person or event in words",
    slug="enl3-descriptive-essays",
    minutes=24,
    summary="A descriptive essay makes the reader see, hear, smell, touch and taste a place, a person or an event. Learn to choose a focus, organise the description, use the senses and figures of speech, and study a full model essay.",
    objectives=[
        "Distinguish description from narrative and choose a clear organising principle",
        "Use the five senses, precise vocabulary and figures of speech",
        "Plan paragraphs by place, time or feature so the description is orderly",
        "Assess a descriptive essay under the Board's three headings",
    ],
    key_concepts=["Descriptive essay", "Sensory detail", "Organising principle", "Precise vocabulary", "Dominant impression"],
    blocks=[
        H("Introduction"),
        T("Imagine you must tell a friend in Yaounde what the Foumban market is like, and she has never been there. You cannot say 'it is nice and big'. "
          "You must help her see the colours, hear the noise and smell the smoke. That is the work of a **descriptive essay**."),
        T("Descriptive is the second kind of topic in Paper 2, Section A. Titles are often 'Describe...' or 'A busy market', 'The person I admire most', 'A village at night', 'A festival'. "
          "In a descriptive essay little happens; the writer's skill is in what the reader can see and feel."),
        assess_key(
            "Is the description relevant to the title and consistent in its focus? Is it fresh and imaginative? Is it arranged in a clear order with paragraphs, from an introduction to a conclusion?",
            "Vivid, precise and varied vocabulary; apt, imaginative figures of speech; clear sentences of different lengths; a tone suited to the subject.",
            "Correct sentence structure, common words spelt right, punctuation that helps the reader."),
        H("Description versus narrative"),
        KEY("What is the difference?", "Both need good language, but the aim is different.", cards=[
            ["Narrative", "Tells what happened, in time order. The main question: what happens next?"],
            ["Descriptive", "Shows what something is like, using the senses. The main question: what is it like?"],
            ["Both", "A descriptive essay may include a little action (a boy pushes a wheelbarrow) and a narrative may include a lot of description."],
        ]),
        H("Organising a description"),
        D("A description needs an **organising principle**, a clear order for the reader to follow. Without one, the details pile up randomly.", title="Organising principle"),
        KEY("Four ways to organise", "Pick one and keep to it.", cards=[
            ["By place (spatial)", "Move from the gate to the centre to the far end: near to far, left to right, top to bottom."],
            ["By time", "Morning, midday, evening: the same place at different times."],
            ["By sense", "One paragraph on sound, one on smell, one on sight, and so on."],
            ["By feature or importance", "The most striking feature first, then the others; or start with the whole and move to details."],
        ]),
        CODE("Paragraph 1  Introduction: the first impression of the whole market\n"
             "Paragraph 2  Sound: voices, radio, goat, hammer\n"
             "Paragraph 3  The crowd: people and movement\n"
             "Paragraph 4  Smell and taste: the food section\n"
             "Paragraph 5  Touch and sight: the craft stalls\n"
             "Paragraph 6  Midday heat\n"
             "Paragraph 7  Evening: the market sleeps\n"
             "Paragraph 8  Conclusion: what the place means", "text",
             title="Plan of the model essay (mixed: by sense, then by time)"),
        H("Tools of description"),
        KEY("Five tools", "Use them in every paragraph.", cards=[
            ["1. The five senses", "Do not only describe what you see. Add sound, smell, touch and taste."],
            ["2. Precise words", "Say 'the woman hurried' or 'the woman trudged'. Replace 'big' with 'enormous', 'tiny', 'towering'. Use exact nouns: 'plantains', not 'food'."],
            ["3. Figures of speech", "Similes, metaphors and personification: 'the crowd is a living river'."],
            ["4. Dominant impression", "Choose one main feeling (busy, peaceful, eerie) and let every detail support it."],
            ["5. Varied sentences", "Mix long sentences full of detail with short sentences that strike."],
        ]),
        TIP("Do not list adjectives in a pile: 'a big, beautiful, wonderful, nice market'. Choose one strong, exact word in place of four weak ones."),
        T(IDENTITY),
        H("A model essay"),
        T("The title is 'A busy market'. The essay below is original and is about 550 words. Read it and notice how many senses are used."),
        T(DESC_ESSAY, title="Model essay: A busy market"),
        H("How the model essay is built"),
        KEY("Notes on the model", "Check each heading.", cards=[
            ["Content and organisation", "The dominant impression is a busy, lively, generous market. The essay moves from the first impression through sound, crowd, food, crafts, midday and evening to a conclusion. Each paragraph has one focus."],
            ["Expression", "Similes ('like a wave', 'like a rusty gate'), metaphors ('a living river', 'a heartbeat'), exact nouns (plantains, draughts, embroidered gowns) and all five senses."],
            ["Accuracy", "Present tense throughout; sentences complete; spelling and punctuation correct; British spelling (colour, neighbour)."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: improve weak description",
           intro="Improve: 'The market was big and noisy and had many people and things.'",
           steps=[
               S("Name the problem", text="'Big', 'noisy', 'many people and things' are vague."),
               S("Add senses and exact nouns", text="Sound: traders shouting. Sight: baskets of plantains, cloth on poles."),
               S("Add a figure of speech", text="The noise rushes like a wave."),
               S("Rewrite", text="The market rushed over me like a wave: traders shouted their prices, a goat bleated, and baskets of plantains swayed above a hundred bobbing heads."),
           ]),
        EX("Worked example 2: choose an organising principle",
           intro="Title: 'The school compound at different times of the day.' Which organising principle suits, and how many paragraphs?",
           steps=[
               S("Look at the title", text="'Different times of the day' points to time order."),
               S("Plan", text="Introduction (early morning, empty compound); assembly; lessons and break; the closing hour; evening silence; conclusion. About 6 paragraphs of 90 words."),
           ]),
        EX("Worked example 3: describing a person",
           intro="Describe a grandmother in three sentences using appearance, voice and action.",
           steps=[
               S("Appearance", text="Her face was a map of fine lines and her white headscarf glowed against her dark skin."),
               S("Voice", text="Her voice was low and warm like thick soup."),
               S("Action", text="She pounded cassava with slow, certain strokes, humming softly as the pestle rose and fell."),
           ]),
        MISTAKE("Telling the reader what to feel",
                "'The market was beautiful and wonderful' tells but does not show. Give the details that make the reader think 'beautiful' themselves."),
        MISTAKE("A list instead of a description",
                "'There were tomatoes, onions, pepper, fish, meat, cloth, shoes...' is a shopping list. Pick a few items and describe them with senses."),
        MISTAKE("No order",
                "Jumping from the gate to the evening to a stall and back to the gate confuses the reader. Choose an organising principle and keep to it."),
        MISTAKE("Too much narrative",
                "If a story takes over, the essay stops being a description. A brief action is fine; the focus must stay on what the subject is like."),
        TIP("Exam link: Descriptive topics are one of the six Section A choices. Write at least 500 words, use the present tense for a place that exists now and the past for a memory, and plan the order of paragraphs before you start."),
        QUIZ("Which sentence uses a sense other than sight?",
             ["The wall was painted white.", "A tall tree stood beside the gate.", "The smell of frying fish drifted over the stalls.", "The road was long and straight."],
             2, "'Smell' is the sense of smell; the others describe only what can be seen.",
             hint="Which sentence mentions smell, sound, touch or taste?",
             feedback=["Sight only.", "Sight only.", "", "Sight only."]),
        QUIZ("Which is the best organising principle for the title 'A walk through my village from the river to the church'?",
             ["Time order", "Spatial order (from place to place)", "A list of unrelated memories", "Order of importance only"],
             1, "The title names a route, so a spatial order from the river to the church is natural.",
             hint="The title gives a start and an end place.",
             feedback=["Time is not the focus of the title.", "", "A random list lacks order.", "Importance is not mentioned in the title."]),
        PQ("Rewrite using exact words and a simile: 'The man walked slowly down the road carrying a heavy load.'",
           "Model: The old man trudged down the dusty road, his sack of cement bent over his shoulders like a second, heavier body. (Any answer with an exact verb, an exact noun and a correct figure.)"),
        PQ("Make a plan for the title 'A thunderstorm in my town'. State your organising principle and give the focus of each paragraph.",
           "Model: Time order, 6 paragraphs. 1: heavy stillness before the storm. 2: wind and first drops. 3: thunder, lightning and the people running. 4: the downpour on roofs and streets. 5: the power cut and the dark. 6: calm after the storm and a conclusion on how the town feels. (Any logical order is accepted.)"),
        PQ("Write a paragraph of about 60 words that describes a classroom at 5 p.m. using at least three senses.",
           "Model: The classroom has been left to dust and silence. A last beam of orange light slants across the empty desks, and the chalky smell of the board hangs in the warm air. Somewhere a window rattles, and the wooden bench feels smooth and cool under my palm. (Any suitable paragraph using three senses.)"),
        PQ("Explain the difference between describing a place and narrating a story about it. Give an example of each in one sentence.",
           "Description shows what a place is like using the senses; narration tells what happened in time order. Description: The market glowed with red tomatoes and green plantains. Narration: I walked into the market, bought a tomato and lost my way."),
        SUM("A descriptive essay shows what something is like using sight, sound, smell, touch and taste.",
            "Choose an organising principle (place, time, sense, feature) and one dominant impression.",
            "Use exact words and figures of speech; avoid vague adjectives and lists.",
            "Marks: content and organisation 10, expression 8, accuracy 2; write at least 500 words; conceal your identity.",
            "Keep the tense steady and proofread for spelling and punctuation."),
    ],
))

# ------------------------------------------------------------------ C3. Expository and discursive essays
LESSONS.append(lesson(
    module=M_C,
    topic=T_EXPO,
    title="Expository and discursive essays: explaining and discussing",
    slug="enl3-expository-discursive-essays",
    minutes=25,
    summary="An expository essay explains a subject clearly; a discursive essay weighs different sides of an issue. Learn the structure, the paragraph pattern (point, explanation, example, link), the language of explanation and balance, and see a full plan and sample paragraphs.",
    objectives=[
        "Distinguish expository, discursive and argumentative writing from the wording of a title",
        "Plan an expository essay (explain) and a discursive essay (weigh both sides)",
        "Write a developed paragraph using point, explanation, example and link",
        "Use linking words, formal register and an impersonal, balanced tone",
    ],
    key_concepts=["Expository essay", "Discursive essay", "Topic sentence", "Linking words", "Balanced discussion"],
    blocks=[
        H("Introduction"),
        T("A teacher in Ngaoundere asks two questions on the board. First: 'Explain why many young people leave villages for towns.' Second: 'Discuss the view that city life is better than village life.' "
          "The first asks you to explain a fact clearly. The second asks you to look at different views and weigh them. These are **expository** and **discursive** writing, the third kind of Section A topic in the Board's syllabus."),
        assess_key(
            "Is the essay relevant to the title? Are the ideas clear, developed and in a logical order, with paragraphs that move from introduction through development to conclusion? Is there a sense of audience?",
            "Clear and coherent writing; adequate, apt vocabulary; the tone of an educated, fair writer; linking words that guide the reader.",
            "Sentences free from lapses, correct spelling of common words, punctuation that helps the sense."),
        H("Reading the title"),
        KEY("Expository, discursive or argumentative?", "The key words in the title tell you what to do.", cards=[
            ["Expository (explain, inform)", "Key words: explain, describe how, outline, what are the causes of, the effects of, the importance of. Aim: make the subject clear to the reader. No need to take a side."],
            ["Discursive (discuss, weigh)", "Key words: discuss, consider, to what extent, examine the view that, advantages and disadvantages. Aim: look at several sides, then give a balanced view, perhaps with your own conclusion."],
            ["Argumentative (persuade)", "Key words: argue, convince, do you agree, write a speech/letter for or against. Aim: take a side and persuade. See the next lessons."],
        ]),
        TIP("Textbooks use these labels differently, and a title may mix them. Read the exact instruction and answer it: if it says 'discuss both sides', do not write a one-sided speech."),
        H("The structure"),
        CODE("Introduction    (60-80 words)  Define the subject or issue; show why it matters; state what the essay will do.\n"
             "Body 1-4       (100-120 words each)  One main point per paragraph, fully developed.\n"
             "Conclusion     (60-80 words)  Sum up the main points; for discursive, give a balanced judgement.\n"
             "Total          about 550 words", "text", title="Plan for about 550 words"),
        D("A developed paragraph follows **P-E-E-L**: **P**oint (topic sentence), **E**xplanation (say more about it), **E**xample (a real or local illustration) and **L**ink (connect to the title or to the next point).", title="Paragraph pattern: PEEL"),
        KEY("Linking words", "Use them to guide the reader, but not in every sentence.", cards=[
            ["Adding", "furthermore, moreover, in addition, also"],
            ["Contrasting", "however, on the other hand, although, whereas, nevertheless"],
            ["Cause and result", "because, since, therefore, consequently, as a result"],
            ["Giving examples", "for example, for instance, such as, in particular"],
            ["Concluding", "in conclusion, to sum up, overall, on balance"],
        ]),
        T("Keep a formal, impersonal tone. Use 'it can be argued that' or 'many people believe that', and avoid slang, text-message forms and sweeping words like 'everybody' or 'always'. "
          "Give examples from Cameroonian life: markets, mobile money, school fees, farming, transport, because specific examples make an explanation clear."),
        T(IDENTITY),
        H("An expository plan with sample paragraphs"),
        T("Title: **Explain the causes of rural-urban migration in Cameroon.** (Examples are general and invented; no statistics are quoted.)"),
        CODE("Introduction  Define rural-urban migration; say it is the movement of people from villages to towns; state that the causes are economic, educational and social.\n"
             "Body 1        Economic: few paid jobs in villages; low prices for farm produce.\n"
             "Body 2        Education: secondary schools, universities and training centres are mostly in towns.\n"
             "Body 3        Services: hospitals, electricity, roads and banking are better in towns.\n"
             "Body 4        Social: influence of relatives and the media; the attraction of city life.\n"
             "Conclusion    Sum up; link to the need to develop rural areas.", "text", title="Plan"),
        T("**Sample introduction:** Every year, thousands of young people leave their villages and move to towns such as Douala, Yaounde and Bamenda. This movement, known as rural-urban migration, is not a sudden decision but the result of several pressures. "
          "This essay explains the main economic, educational and social causes of this movement."),
        T("**Sample body paragraph (PEEL):** The most important cause is the lack of well-paid work in villages (Point). Most village families depend on farming, and a farmer's income can fall sharply when prices drop or when roads are too poor to take crops to market (Explanation). "
          "For example, a cocoa farmer who cannot reach a buyer before the produce spoils may decide that his son will earn more as a motorcycle taxi rider in town (Example). "
          "It is therefore not surprising that many young people believe that their future lies in the town (Link)."),
        T("**Sample conclusion:** In conclusion, rural-urban migration is caused mainly by the search for jobs, education and services, with social influence adding to the pull of the town. "
          "If villages had better roads, schools and markets, fewer young people would feel that they had to leave."),
        H("A discursive plan with sample paragraphs"),
        T("Title: **Discuss the advantages and disadvantages of social media for students.**"),
        CODE("Introduction  Define social media; say students use it daily; state that it has both benefits and risks.\n"
             "Body 1        Advantage: contact and study groups (messages about homework, sharing notes).\n"
             "Body 2        Advantage: access to information and chances to learn new skills.\n"
             "Body 3        Disadvantage: time wasted; poor sleep and weaker concentration.\n"
             "Body 4        Disadvantage: false information, bullying and loss of privacy.\n"
             "Conclusion    Balanced judgement: used with rules and self-control, benefits can outweigh the risks.", "text", title="Plan"),
        T("**Sample body paragraph:** On the one hand, social media helps students to work together (Point). A class can form a group in which pupils share notes, ask questions about a difficult topic and remind each other of deadlines (Explanation). "
          "A pupil who missed a lesson because of illness, for example, can catch up the same evening (Example). Consequently, used well, these platforms can raise the quality of study (Link)."),
        T("**Sample conclusion:** On balance, social media is neither wholly good nor wholly bad for students. It offers real help with study and communication, but it also wastes time and can spread false information. "
          "Students who set limits and check what they read are likely to gain more than they lose."),
        H("Worked examples"),
        EX("Worked example 1: classify the titles",
           intro="Classify each as expository, discursive or argumentative: (a) The importance of mobile money. (b) Discuss the view that school uniforms should be abolished. (c) Convince your school that it needs a library. (d) How to prepare for an examination.",
           steps=[
               S("(a)", text="Expository: explain why it matters."),
               S("(b)", text="Discursive: 'discuss the view' asks you to weigh the arguments."),
               S("(c)", text="Argumentative: 'convince' asks you to persuade."),
               S("(d)", text="Expository: explain a process."),
           ]),
        EX("Worked example 2: build a PEEL paragraph",
           intro="Point: 'Regular exercise improves a student's concentration.' Build a paragraph.",
           steps=[
               S("Explain", text="Exercise sends more blood to the brain and relieves stress, so pupils think more clearly."),
               S("Example", text="A pupil who plays football for thirty minutes after school often finds that evening revision is easier."),
               S("Link", text="Schools should therefore protect games periods."),
               S("Join", text="Regular exercise improves a student's concentration. It sends more blood to the brain and relieves stress, so pupils think more clearly. A pupil who plays football for thirty minutes after school, for example, often finds that evening revision is easier. Schools should therefore protect games periods."),
           ]),
        EX("Worked example 3: from one-sided to balanced",
           intro="Make this discursive sentence balanced: 'Mobile phones are bad for students.'",
           steps=[
               S("Name the problem", text="It is one-sided, absolute and informal in its judgement."),
               S("Add the other side and a qualifier", text="Mobile phones can distract students from their studies; however, they can also give access to useful learning resources."),
           ]),
        MISTAKE("Writing a one-sided speech for a discursive title",
                "If the title says 'discuss', give weight to both sides. A balanced conclusion may still prefer one side, but only after fairly considering the other."),
        MISTAKE("A list of points without development",
                "'First, jobs. Second, schools. Third, hospitals.' is a plan, not an essay. Each point needs explanation and an example."),
        MISTAKE("Memorised introductions that do not fit",
                "Examiners recognise a ready-made opening ('Since the dawn of time...'). Define the actual subject in your own words."),
        TIP("Exam link: Expository and discursive topics are one of the six Section A choices. Spend five minutes on a plan with four body points and an example for each; write about 550 words."),
        QUIZ("Which title is most clearly discursive?",
             ["Describe a crowded bus station.", "Discuss the advantages and disadvantages of boarding schools.", "Tell the story of a journey.", "Write a speech persuading your school to ban plastic bags."],
             1, "'Discuss the advantages and disadvantages' asks for both sides to be weighed.",
             hint="Look for words such as discuss, consider, advantages and disadvantages.",
             feedback=["Descriptive.", "", "Narrative.", "Argumentative (persuasive)."]),
        QUIZ("What does the L in PEEL stand for?",
             ["Language", "Link", "List", "Length"],
             1, "L is for Link: connect the paragraph to the title or to the next point.",
             hint="It joins the paragraph to the essay.",
             feedback=["Not part of the pattern.", "", "Not part of the pattern.", "Not part of the pattern."]),
        PQ("Plan an expository essay on 'The importance of reading'. Give an introduction aim, four body points and a conclusion aim.",
           "Introduction: define reading and say why it matters. Body: (1) widens vocabulary, (2) improves writing and spelling, (3) develops imagination and general knowledge, (4) is cheap entertainment and a lifelong habit. Conclusion: sum up and encourage the habit. Each body point is supported by an example. (Any logical plan is accepted.)"),
        PQ("Write a PEEL paragraph of about 80 words on: 'Fast food has both advantages and disadvantages.'",
           "Model: Fast food saves time, which is its main advantage (Point). Workers who have only a short break can buy a meal in minutes instead of cooking one (Explanation). A trader in a busy market, for example, may eat fried plantain between customers (Example). However, eating it too often can harm health, so convenience must be balanced against nutrition (Link)."),
        PQ("List five linking words and the job each does.",
           "Furthermore (adds a point); however (contrasts); therefore (shows result); for example (gives an illustration); in conclusion (signals the end). Others: moreover, although, consequently, on balance."),
        PQ("Rewrite in a formal, balanced tone: 'Everybody knows that boarding schools are rubbish.'",
           "Model: Boarding schools are often criticised for separating children from their families; however, they can also give pupils a quiet place to study and a regular routine."),
        SUM("Read the title: expository explains, discursive weighs different sides, argumentative persuades.",
            "Plan an introduction, four developed body paragraphs and a conclusion.",
            "Use PEEL for each paragraph and linking words to guide the reader.",
            "Keep a formal, fair tone; give local examples; avoid sweeping statements.",
            "Marks: content and organisation 10, expression 8, accuracy 2; at least 500 words."),
    ],
))

ARG_ESSAY = (
    "Every year, thousands of Cameroonian students leave secondary school with certificates but without a single skill that can earn them a living. A young person may know the date of a treaty and the formula for a circle, yet be unable to repair a bicycle, keep a shop's accounts or plant a profitable garden. For this reason, I strongly support the view that practical skills should be a compulsory subject in every secondary school.\n\n"
    'The first and strongest reason is that practical skills prepare students for the real world of work. The number of graduates is growing much faster than the number of office jobs, and many young people wait years for a post that never comes. A student who has learnt carpentry, tailoring, basic electrical work or farming can begin earning at once, or even employ others. Practical education is therefore not a second-class option; it is a form of insurance against unemployment.\n\n'
    'Secondly, practical lessons make students better learners in every other subject. Measuring a piece of wood teaches fractions more clearly than a blackboard can, and growing beans shows how a plant really grows, which no diagram fully explains. Students who learn by doing are also more active in class and less likely to leave school early through boredom. Schools that already run workshops and school gardens report livelier, more confident pupils.\n\n'
    "Thirdly, practical skills build habits that every employer values: patience, teamwork, honesty with money and pride in good work. A boy who must finish a table before the bell rings learns discipline in a way that a lecture on discipline can never teach. A girl who runs the school canteen's accounts learns responsibility. These habits last long after the facts of an examination are forgotten.\n\n"
    'Some people disagree. They argue that schools exist to teach academic subjects and that adding practical lessons will take time from Mathematics and English. It is true that the timetable is already crowded, and it would be foolish to ignore this concern. However, the answer is not to leave practical skills out but to plan a fair balance, for example two periods a week, and to link them to existing subjects. Others complain that schools lack tools and workshops. This is a real difficulty, yet many skills, such as gardening, sewing, repair work and bookkeeping, need very few tools, and communities and parents are often willing to help.\n\n'
    'A further objection is that practical subjects may be seen as only for weaker students. This belief is mistaken and unfair. Many of the most successful business people in our towns began with a trade, and a clever student who can also build and repair has a great advantage over one who cannot. If every student learns practical skills, no student will be stigmatised.\n\n'
    'In conclusion, a compulsory practical subject would make school more useful, learning more lively and young people more independent. The timetable problems and the shortage of tools can be solved with planning and community support. A country that wants its young people to build its future must teach them how to build. I therefore urge the Ministry and every school to place practical skills at the centre of secondary education.'
)

# ------------------------------------------------------------------ C4. Argumentative essays
LESSONS.append(lesson(
    module=M_C,
    topic=T_ARG,
    title="Argumentative essays: taking a side and persuading the reader",
    slug="enl3-argumentative-essays",
    minutes=25,
    summary="An argumentative essay takes a clear side and persuades the reader with reasons, evidence and an answer to the other side. Learn the structure, persuasive language, the counter-argument and rebuttal, and study a full model essay and a debate-speech version.",
    objectives=[
        "State a clear thesis and support it with reasons and evidence",
        "Include and answer a counter-argument fairly",
        "Use persuasive but reasonable language and avoid unfair arguments",
        "Assess an argumentative essay under content and organisation, expression and accuracy",
    ],
    key_concepts=["Thesis", "Argument", "Evidence", "Counter-argument", "Rebuttal", "Persuasive language"],
    blocks=[
        H("Introduction"),
        T("At a family meeting in Garoua, an uncle says: 'Girls should not travel for university.' A young cousin answers: 'I disagree. A woman with a degree helps her whole family, and many girls already study safely in other cities.' "
          "She has done what an argumentative writer does: she has taken a side and given a reason. An argumentative essay does this at length, in order and with fairness."),
        T("The Board lists 'argumentative' among the Section A kinds of topic. The title may say 'Do you agree?', 'For or against', or ask you to write a speech, a letter to a newspaper or a debate contribution. "
          "Whatever the form, you must take a position and defend it."),
        assess_key(
            "Is your position clear and relevant to the title? Are the arguments logical, well developed and in a good order, with paragraphs? Is there a sense of audience and an appropriate point of view?",
            "Clear, coherent language; apt, persuasive vocabulary; sentences of different shapes; a firm but courteous tone suited to the reader.",
            "Correct sentence structure, spelling and punctuation, so the argument is never hidden by errors."),
        H("The ingredients of an argument"),
        KEY("Five ingredients", "Every strong argumentative essay has all five.", cards=[
            ["1. Thesis", "One sentence stating your position: 'Practical skills should be compulsory in secondary schools.' Put it in the introduction and repeat it in the conclusion."],
            ["2. Reasons", "Three or four separate reasons, each with its own paragraph."],
            ["3. Evidence", "Facts, examples, comparisons and logical explanation. Use local examples. Do not invent statistics."],
            ["4. Counter-argument", "The strongest point the other side would make."],
            ["5. Rebuttal", "Your fair answer to that point: show why it does not defeat your position."],
        ]),
        CODE("Introduction        (70 words)   hook, background, thesis\n"
             "Reason 1           (100 words)  strongest reason: point, explain, example, link\n"
             "Reason 2           (100 words)\n"
             "Reason 3           (100 words)\n"
             "Counter-argument   (100 words)  state the other side fairly, then rebut it\n"
             "Conclusion         (70 words)   restate thesis, sum up, final appeal\n"
             "Total              about 540 words", "text", title="Plan for about 550 words"),
        TIP("Put your strongest reason first or last. The first paragraph catches the reader; the last leaves the final impression. Avoid putting your weakest reason in the middle of the essay by accident."),
        H("Persuasive language"),
        KEY("Ways to persuade fairly", "Persuasion is not shouting.", cards=[
            ["Strong verbs and certain phrases", "It is clear that; there is no doubt that; we must; it is vital that."],
            ["Rhetorical question", "Can a country develop if its young people cannot build?"],
            ["Rule of three", "patience, teamwork and pride in good work."],
            ["Addressing the reader", "We, our country, every parent. (Do not give your own name or address.)"],
            ["Concession", "It is true that...; however... shows fairness."],
        ]),
        KEY("Arguments to avoid", "Weak reasoning loses marks.", cards=[
            ["Personal attack", "Attacking the person instead of the idea: 'Only a fool would think that.'"],
            ["Overgeneralising", "'All teachers are lazy.' A claim about everyone is easily shown false."],
            ["Appeal to majority", "'Everyone agrees, so it is true.'"],
            ["False choice", "'Either we ban phones or students will fail.' (Other options exist.)"],
            ["Unsupported claim", "'Studies show...' without any detail. Use reasoning and honest local examples."],
        ]),
        T(IDENTITY),
        H("A model essay"),
        T("Title: **'Practical skills should be a compulsory subject in secondary schools.' Argue for or against this view.** The model argues for. It is original, about 530 words."),
        T(ARG_ESSAY, title="Model essay: Practical skills for every student"),
        H("How the model essay meets the criteria"),
        KEY("Reading the model", "Check against the three headings.", cards=[
            ["Content and organisation", "The thesis is stated in the first paragraph and restated in the conclusion. Three reasons are in separate paragraphs; the counter-argument (timetable, tools, 'weaker students') is stated fairly and answered. The conclusion sums up and appeals to the reader."],
            ["Expression", "Persuasive phrases ('strongly support', 'it would be foolish to ignore'), the rule of three (patience, teamwork, pride), contrast ('certificates but without a single skill'), a formal and respectful tone."],
            ["Accuracy", "Clear sentences; linking words (Secondly, Thirdly, However, Therefore); consistent present tense; careful punctuation."],
        ]),
        H("The same case as a speech"),
        T("Titles often ask for a speech or a letter. The reasoning stays the same; the form changes. A speech needs a greeting, a direct address to the audience, shorter sentences and a strong closing. "
          "Use the name or title given on your paper; do not use your own name."),
        T("**Opening of a speech (invented):** Honourable guests, teachers and my fellow students, how many of us can mend a broken chair? Please raise your hands. I see very few. That is why I stand before you today to argue that every student in this school must learn a practical skill."),
        T("**Closing of a speech:** I appeal to every member of this assembly to support this motion. Let us leave this hall determined to be a school that produces thinkers and makers. Thank you."),
        H("Worked examples"),
        EX("Worked example 1: a thesis",
           intro="Title: 'Mobile phones should be banned in secondary schools.' Write a thesis sentence against the ban.",
           steps=[
               S("Take a clear side", text="You oppose a total ban."),
               S("Say why in the sentence", text="Mobile phones should not be banned in secondary schools, because with proper rules they help learning and safety."),
           ]),
        EX("Worked example 2: counter-argument and rebuttal",
           intro="Write a counter-argument and rebuttal for the essay opposing the ban.",
           steps=[
               S("State the other side fairly", text="Supporters of a ban argue that phones distract students and disturb lessons."),
               S("Concede what is true", text="This is a serious concern and some students do misuse their phones."),
               S("Rebut", text="However, the answer is better rules, not a total ban: phones can be kept in bags during lessons and used only when a teacher allows, which keeps their benefits and removes the distraction."),
           ]),
        EX("Worked example 3: spot the weak argument",
           intro="What is wrong with: 'Everybody knows that homework is useless, so it should be banned.'",
           steps=[
               S("Identify", text="It overgeneralises ('everybody') and appeals to the majority; it gives no reason."),
               S("Repair", text="Give a reason and an example: Excessive homework can leave students too tired to learn, as a pupil who sleeps four hours each night soon shows."),
           ]),
        MISTAKE("Sitting on the fence",
                "In an argumentative essay you must choose a side. 'Both sides have good points' belongs in a discursive essay."),
        MISTAKE("Ignoring the other side",
                "An essay that never mentions the opposite view looks weak. Name the strongest opposing point, then answer it."),
        MISTAKE("Using anger instead of reasons",
                "Rude or insulting language convinces nobody and may break the rule against obscene language. Be firm but polite."),
        MISTAKE("Repeating one reason three times",
                "Three paragraphs that all say 'it is good for jobs' are one reason, not three. Give different reasons."),
        TIP("Exam link: Argumentative topics are one of the six Section A choices. If the title is a statement ('Prison does more harm than good'), decide your side in the first minute, then list three reasons and one objection before you begin writing."),
        QUIZ("What is a 'rebuttal'?",
             ["The opening of an essay", "Your answer to the opposing argument", "A list of facts", "The title of the essay"],
             1, "A rebuttal answers the counter-argument and shows why it does not defeat your position.",
             hint="It comes after the counter-argument.",
             feedback=["That is the introduction.", "", "A rebuttal is an answer, not a list.", "The title is given."]),
        QUIZ("Which is a weak argument?",
             ["School uniforms reduce competition about clothes, so pupils can concentrate on study.", "Only a fool would oppose school uniforms.", "Uniforms are cheaper than many different outfits for a family with several children.", "Some pupils say uniforms are uncomfortable; however, the fabric can be chosen with care."],
             1, "A personal attack ('only a fool') gives no reason.",
             hint="Which sentence insults instead of reasoning?",
             feedback=["A reason.", "", "A reason with a comparison.", "A counter-argument with an answer."]),
        PQ("Write a thesis sentence for each side of: 'Students should wear school uniform.'",
           "For: Students should wear school uniform, because it creates equality, saves money and builds school pride. Against: Students should not be forced to wear school uniform, because it is costly for poor families and does not improve learning."),
        PQ("Give a counter-argument and a rebuttal for the view that school fees should be abolished in secondary schools.",
           "Counter-argument: Some say that schools need fees to pay for repairs and teaching materials. Rebuttal: This is true, but if the state or the community supports schools directly, children from poor families would not be turned away; fees should not decide who learns."),
        PQ("Name three weak arguments and say why each is weak.",
           "Personal attack (insults the person, not the idea); overgeneralisation (a claim about all people is easily false); appeal to the majority (many people believing something does not make it true). Others: false choice, unsupported claims."),
        PQ("Write a short, persuasive closing paragraph (about 50 words) for a speech on 'Cleaner towns need everybody'.",
           "Model: Fellow citizens, a clean town is not made by the council alone. It is made by the trader who sweeps her stall, the child who uses the bin and the elder who gives example. Let us start today, in our own street. Together we can be proud of our town. Thank you."),
        SUM("Take a clear side. State a thesis in the introduction and restate it in the conclusion.",
            "Give three separate reasons with evidence and local examples; present the opposing view fairly and rebut it.",
            "Persuade with strong, polite language, rhetorical questions and the rule of three; avoid attacks, overgeneralisation and unsupported claims.",
            "For a speech or letter, keep the same reasoning but use the right form and the name/address from the paper.",
            "Marks: content and organisation 10, expression 8, accuracy 2; at least 500 words."),
    ],
))

# ------------------------------------------------------------------ C5. Open-ended titles
LESSONS.append(lesson(
    module=M_C,
    topic=T_OPEN,
    title="Open-ended (one-word) titles: choosing an angle and a form",
    slug="enl3-open-ended-titles",
    minutes=22,
    summary="A one-word title such as 'Bridges' or 'Silence' leaves the form and the angle to you. Learn to brainstorm, choose a focus and a form (story, description, discussion or argument), plan, and stay relevant to the word throughout.",
    objectives=[
        "Brainstorm meanings, images and links for a one-word title",
        "Choose one angle and one form and justify the choice",
        "Plan and write an essay that stays relevant to the word from beginning to end",
        "Use the same assessment criteria to check an open-ended essay",
    ],
    key_concepts=["Open-ended title", "Brainstorming", "Angle", "Form", "Relevance"],
    blocks=[
        H("Introduction"),
        T("The title on the paper is a single word: 'Courage'. A candidate in Maroua panics. 'Which kind of essay must I write?' The answer is: the kind you choose. "
          "The Board lists 'open-ended (one-word)' among the Section A topics. Because the title does not tell you the form, you have freedom, but also a danger: an unfocused essay about 'courage in general' drifts and scores poorly."),
        assess_key(
            "The marks for relevance and organisation depend on a clear angle: does every paragraph connect to the word? Is there a clear introduction, development and conclusion, and a sense of audience?",
            "Range and aptness of vocabulary, imaginative use of figurative language, clear and coherent writing with a tone suited to the form you chose.",
            "Accurate sentence structure, spelling and punctuation, whichever form you choose."),
        H("A four-step method"),
        KEY("From one word to an essay", "Spend about five minutes on steps 1 to 3.", cards=[
            ["1. Brainstorm", "Write everything the word brings to mind in a minute: meanings, pictures, people, places, opposites, proverbs."],
            ["2. Choose an angle", "Pick one idea you can write 500+ words about with real examples. The first idea is often too general; pick a specific one."],
            ["3. Choose a form", "Story (narrative), picture in words (descriptive), explanation or discussion (expository/discursive), or a case (argumentative). Choose the form that matches your angle and your best skill."],
            ["4. Plan and write", "Write a paragraph plan; make every paragraph link back to the word; end by returning to it."],
        ]),
        T("Here is a brainstorm for the word **Bridge**. Notice that the word is a noun, but it can also be a metaphor."),
        CODE("literal      river bridge, footbridge, broken bridge, new road bridge\n"
             "people       a farmer who cannot reach the market; a child going to school\n"
             "metaphor     a bridge between two people, languages, generations\n"
             "opposites    wall, gap, river, distance\n"
             "proverb      cross that bridge when we come to it\n"
             "feelings     fear of crossing, joy of arriving", "text", title="Brainstorm: Bridge"),
        KEY("Four essays from one word", "Each is a valid answer to the title 'Bridge'.", cards=[
            ["Narrative", "A story about the day the village built its first bridge, or the night a child crossed a flooded river."],
            ["Descriptive", "A description of a rope bridge over a river gorge, its sounds, its swaying, the faces of the people crossing."],
            ["Expository or discursive", "How bridges change a community: trade, school, health; or whether money should go to bridges or to schools."],
            ["Argumentative", "A speech arguing that the council must repair the broken bridge now."],
        ]),
        TIP("Choose the form you can handle with the best examples. A fine storyteller may choose narrative; a student who knows a lot about a local issue may prefer an argument. There is no 'best' form."),
        H("Staying relevant"),
        T("The most common weakness in open-ended essays is drifting away from the word. Use a simple check: at the end of each paragraph, ask 'What does this have to do with the word on the paper?' "
          "If you cannot answer in one sentence, change the paragraph. Put the word, or a close link to it, in the introduction and the conclusion."),
        T(IDENTITY),
        H("A sample plan and opening"),
        T("Title: **Bridge.** Form chosen: narrative with a metaphorical ending."),
        CODE("Opening      A village cut in two by a river; the old log bridge washes away (80 words)\n"
             "Complication Children cannot reach school; a mother must cross to the clinic (150)\n"
             "Climax       Villagers build a new bridge together over three weekends; a storm tests it (150)\n"
             "Resolution   The bridge holds; the first crossing is a procession of children (100)\n"
             "Ending       The narrator reflects that the real bridge was the shared work between neighbours (80)", "text",
             title="Plan (about 560 words)"),
        T("**Sample opening paragraph:** For as long as I could remember, our village lived on two sides of the river. On one side were the school, the clinic and the market; on the other, the farms and our house. "
          "A single log lay across the water, slick with moss and older than my grandfather's stories. When the rains of August swept it away in a night, our village was cut in two, and I learnt that a bridge is more than wood."),
        H("Worked examples"),
        EX("Worked example 1: brainstorm and choose",
           intro="Title: 'Silence'. Brainstorm and choose an angle and form.",
           steps=[
               S("Brainstorm", text="library; night in the village; a classroom after bad news; the silence of a mother when you disappoint her; peace after war; silence as protest; silence as fear."),
               S("Choose an angle", text="The silence in a classroom while results are being read."),
               S("Choose a form", text="Narrative with descriptive detail, from the point of view of a pupil waiting for the results."),
           ]),
        EX("Worked example 2: from general to specific",
           intro="Title: 'Courage'. The first idea is 'courage is important'. Make it specific.",
           steps=[
               S("List specific situations", text="a child who speaks up against bullying; a nurse who stays at work during a flood; a farmer who starts again after a fire."),
               S("Choose one", text="A nurse who stays during a flood."),
               S("Choose a form", text="Narrative or discursive: 'What is real courage?' with three examples. Narrative is better if you can tell the story vividly."),
           ]),
        EX("Worked example 3: check relevance",
           intro="A candidate writes on 'Home'. Paragraph 3 describes a football match. Is it relevant?",
           steps=[
               S("Ask the question", text="What does this have to do with home?"),
               S("Decide", text="Not relevant unless the match took place at home or shows what home means. Either connect it (the football in the yard behind the house) or delete it."),
           ]),
        MISTAKE("Writing about the word in general",
                "An essay that defines 'friendship' in five paragraphs but tells no example is vague. Choose a concrete angle with people, places and events."),
        MISTAKE("Using the word once and forgetting it",
                "If the word appears only in the title, the examiner will doubt relevance. Link every paragraph back to it."),
        MISTAKE("Changing the form halfway",
                "Starting a story and finishing as a lecture confuses the reader. Choose a form and keep it."),
        TIP("Exam link: The open-ended title is one of the six Section A choices. If you like freedom, it can be your best option; if you tend to drift, choose a title that tells you the form. Either way, 500 words minimum."),
        QUIZ("What is the first step in writing about an open-ended title?",
             ["Write the conclusion", "Brainstorm ideas about the word", "Count the words", "Copy a model essay"],
             1, "Brainstorming lets you find a specific angle before you choose a form.",
             hint="You need ideas before you can choose.",
             feedback=["You cannot conclude before you start.", "", "Count when you have written.", "Models must not be copied."]),
        QUIZ("A candidate gets the title 'Fire' and writes a descriptive essay about a bonfire in the village. Which sentence shows relevance?",
             ["The kitchen was small and green.", "Flames leapt above the rooftops, and the heat pressed on our faces.", "Next week there is a football match.", "My uncle sells shoes."],
             1, "The second sentence describes the fire, the title word.",
             hint="Which sentence is about fire?",
             feedback=["Not about fire.", "", "Not about fire.", "Not about fire."]),
        PQ("Brainstorm the word 'Journey' for one minute (at least eight items), then choose one angle and one form.",
           "Model: bus; walk to school; a refugee; first flight; life as a journey; a pilgrim; lost luggage; a long road to a degree. Angle: the first journey alone by bus. Form: narrative. (Any sensible brainstorm and choice.)"),
        PQ("Give three different forms of essay a candidate could write for the title 'Water' and one sentence about each.",
           "Narrative: the day the village tap ran dry. Descriptive: a river at sunrise. Expository or argumentative: why every home should have clean water, or a speech urging the council to repair the borehole."),
        PQ("Write a two-sentence introduction for an essay on 'Market' that is clearly relevant and in the descriptive form.",
           "Model: At dawn, the market wakes before the town does, with a clatter of baskets and the smell of woodsmoke. By seven, it is a roaring river of colour, voices and bargaining."),
        PQ("A candidate's essay on 'Courage' drifts into a long description of a city. Explain how to fix it.",
           "Ask of each paragraph how it links to courage. Cut or rewrite paragraphs that do not link. Add examples of courageous action, mention the word or a related idea in the introduction and conclusion, and keep the focus on a few examples."),
        SUM("An open-ended title leaves the angle and the form to you.",
            "Brainstorm, choose a specific angle, choose a form, plan, then write.",
            "Link every paragraph to the word; return to it in the conclusion.",
            "Keep one form throughout; use concrete examples.",
            "Same marks as any composition: content and organisation 10, expression 8, accuracy 2; at least 500 words."),
    ],
))

# ------------------------------------------------------------------ C6. Responding to visual stimuli
LESSONS.append(lesson(
    module=M_C,
    topic=T_VIS,
    title="Responding to visual stimuli: pictures and cartoons",
    slug="enl3-visual-stimuli",
    minutes=22,
    summary="One Section A topic may be a picture or cartoon. Learn to read the image closely (who, where, what, mood, message), choose a form, and write a relevant essay that uses the picture without simply listing what is in it.",
    objectives=[
        "Read an image systematically: setting, people, action, mood, symbols and message",
        "Decide whether to write a story, a description or a discussion from the picture",
        "Use details from the picture accurately while adding your own ideas",
        "Avoid the common mistakes of listing the picture or ignoring it",
    ],
    key_concepts=["Visual stimulus", "Cartoon", "Symbol", "Mood", "Message", "Relevance to the picture"],
    blocks=[
        H("Introduction"),
        T("On the paper, instead of a title, there is a picture: a crowded bus stop, a child at a broken desk, a cartoon of a man carrying a huge pile of paper. "
          "The instruction says: 'Write an essay suggested by the picture.' The Board lists 'reacting to visual stimuli: pictures, cartoons, etc.' among the Section A topics. "
          "The picture is not decoration: it sets the topic, and your essay must clearly come from it."),
        T("Because a book cannot show every picture the Board might use, we describe invented pictures in words, so you can practise reading images. In the examination, look at the actual picture carefully for a full minute before you decide."),
        assess_key(
            "Is the essay relevant to the picture? Does it use details from it accurately and add original ideas? Is it organised in clear paragraphs with an introduction, development and conclusion?",
            "Vocabulary suited to the scene or idea; imaginative language; clear, coherent sentences; a tone suited to the form you chose.",
            "Accurate sentences, spelling and punctuation, as in any composition."),
        H("How to read a picture"),
        KEY("Seven questions to ask", "Take one minute and answer them in your head or in short notes.", cards=[
            ["1. Where?", "Setting: town, village, school, road, market, hospital. What is in the background?"],
            ["2. Who?", "People: how many, age, clothes, expressions, body language."],
            ["3. What?", "Action: what is happening, and what has just happened or is about to happen?"],
            ["4. Mood", "Feeling: busy, peaceful, tense, sad, hopeful. Colour and light can help."],
            ["5. Symbols", "In cartoons, objects often stand for ideas (a mountain of paper means too much work)."],
            ["6. Message", "What does the picture seem to say? Is it a warning, a joke, a protest?"],
            ["7. Words", "Is there a caption or speech bubble? Use it."],
        ]),
        H("Choosing the form"),
        KEY("Picture to essay", "The picture suggests a topic; you choose how to treat it.", cards=[
            ["Picture shows an event or a person in trouble", "A narrative: what happened before and after, or what the people felt."],
            ["Picture shows a place or a crowd", "A descriptive essay, using the senses the picture suggests (sound, smell, heat)."],
            ["Picture shows a social problem (litter, queues, long school fees)", "An expository, discursive or argumentative essay on the issue it raises."],
            ["Cartoon with a message", "Explain the message, then discuss or argue about the issue; do not just describe the drawing."],
        ]),
        TIP("Use details from the picture early, to show the examiner you have read it, but spend most of the essay developing your own ideas. A picture is a starting point."),
        T(IDENTITY),
        H("Two invented pictures and plans"),
        T("**Picture A (described):** A wide road after heavy rain. A minibus stands in brown water up to its doors. A young man is carrying a girl in school uniform on his back through the flood. Behind them, shop owners stack goods on high shelves. The sky is grey, but a thin patch of light shows at the horizon."),
        CODE("Where?   a flooded road in a town\n"
             "Who?     a young man, a schoolgirl, shopkeepers, minibus passengers\n"
             "What?    carrying the girl through the flood; shop-owners saving goods\n"
             "Mood     tense but hopeful (patch of light)\n"
             "Message  floods affect daily life, and people help one another\n"
             "Form     narrative ('The morning the road became a river'), or discursive\n"
             "         ('Floods in our towns: causes and solutions')", "text", title="Reading Picture A"),
        T("**Picture B (a described cartoon):** A very large man in a suit sits behind a desk piled with papers up to the ceiling. A line of people waits at a door marked 'Documents'. The man holds a small stamp and a tiny cup of tea. The caption reads: 'Next week.'"),
        CODE("Symbols  mountain of papers = slow, heavy bureaucracy\n"
             "         tiny stamp, tiny tea = lack of real work\n"
             "         line of people = citizens who suffer delays\n"
             "Message  slow administration wastes the time of ordinary people\n"
             "Form     argumentative: a letter to a newspaper urging faster service; or\n"
             "         expository: causes and effects of delay in offices", "text", title="Reading Picture B"),
        H("Worked examples"),
        EX("Worked example 1: opening from Picture A",
           intro="Write an opening paragraph for a narrative essay suggested by Picture A.",
           steps=[
               S("Choose a point of view", text="The schoolgirl, first person."),
               S("Use picture details", text="Brown water, the minibus, the young man, the shopkeepers."),
               S("Write", text="When I stepped out of the minibus that morning, the road had disappeared. In its place lay a brown river that swallowed my shoes and tugged at my school skirt. A stranger knelt in the water and said, \"Climb on, little sister,\" and that was how my longest school day began."),
           ]),
        EX("Worked example 2: plan from Picture B",
           intro="Plan an argumentative letter suggested by Picture B. The paper gives the name and address to use.",
           steps=[
               S("Thesis", text="Offices should serve citizens faster."),
               S("Reasons", text="1. Delay wastes time and money. 2. Delay encourages bribery. 3. Technology makes faster service possible."),
               S("Counter-argument", text="Offices are understaffed; reply: better organisation and training help."),
               S("Form", text="Formal letter: address, date, salutation, subject line, paragraphs, formal closing signed with the name provided on the paper, not your own."),
           ]),
        EX("Worked example 3: avoiding a list",
           intro="What is wrong with: 'In the picture, I can see a road. I can see a minibus. I can see a girl. I can see a man.'",
           steps=[
               S("Diagnose", text="It only lists the picture; it does not build an essay and it uses the same sentence pattern."),
               S("Repair", text="Turn the details into a story or an idea, with the picture as the setting: 'The minibus stood helplessly in the brown water as the young man waded towards the girl.'"),
           ]),
        MISTAKE("Describing the picture without an essay",
                "A paragraph that lists what you see is not enough. Use the picture to start a story, a description with senses, or a discussion of the issue."),
        MISTAKE("Ignoring the picture",
                "An essay that has nothing to do with the picture will lose marks for relevance, however well written."),
        MISTAKE("Missing the message of a cartoon",
                "A cartoon is often a joke or a protest. If you only describe the characters, you miss the point. Ask what the symbols stand for."),
        MISTAKE("Inventing details that contradict the picture",
                "If the picture shows a flood, do not write about a drought. You may add events before and after, but do not change what is shown."),
        TIP("Exam link: The visual-stimulus topic is one of the six Section A choices. If you can read pictures well, it can be an easy choice; spend one minute reading and two minutes planning."),
        QUIZ("What should you do first when the topic is a picture?",
             ["Start writing immediately", "Study the picture: setting, people, action, mood and message", "Write a letter to the examiner", "Copy the caption only"],
             1, "A careful reading gives you ideas and ensures relevance.",
             hint="You cannot respond to what you have not read.",
             feedback=["You may miss important details.", "", "Not required.", "A caption is only part of the stimulus."]),
        QUIZ("In a cartoon, a huge mountain of papers on a desk most likely stands for",
             ["a large library", "heavy, slow paperwork", "a school bag", "a market stall"],
             1, "In cartoons, objects are symbols. A mountain of papers suggests too much paperwork or slow administration.",
             hint="What do too many papers on one desk suggest?",
             feedback=["Not suggested.", "", "Not suggested.", "Not suggested."]),
        PQ("A picture shows a crowded bus station at sunset: travellers with bags, a driver shouting, a child asleep on a sack. Write a plan for a descriptive essay.",
           "Plan: Introduction (first impression of the station at sunset). Sound paragraph (drivers calling destinations, engines). People paragraph (travellers, hawkers, the sleeping child). Smell and touch paragraph (fumes, grilled fish, heat). Mood paragraph (tiredness and hope as the light fades). Conclusion (what the station says about movement and waiting). About 550 words."),
        PQ("Write an introduction for a discursive essay suggested by a picture of rubbish piled beside a market.",
           "Model: In many of our towns, a mountain of rubbish now stands beside the market where we buy our food. This picture shows an ordinary problem with serious results for health, trade and the town's image. This essay discusses its causes and what can be done."),
        PQ("Explain how to treat a cartoon in which a student carries a bag as large as himself marked 'Homework'. Give the message and one possible form.",
           "Symbol: the giant bag stands for excessive homework. Message: students are overloaded. Form: a discursive or argumentative essay on whether students are given too much homework, using the cartoon as the starting point."),
        PQ("List three mistakes candidates make with picture topics.",
           "Only listing what is in the picture; ignoring the picture or writing something unrelated; missing the message of a cartoon; contradicting the details; being too short."),
        SUM("Study the picture for a full minute: where, who, what, mood, symbols, message, words.",
            "Choose a form: narrative, descriptive, expository, discursive or argumentative.",
            "Use the picture as a starting point and develop your own ideas; do not just list.",
            "For cartoons, find the message in the symbols.",
            "Same marks: content and organisation 10, expression 8, accuracy 2; at least 500 words."),
    ],
))

# ------------------------------------------------------------------ C7. How a composition is assessed
LESSONS.append(lesson(
    module=M_C,
    topic=T_ASSESS,
    title="How a composition is assessed: 20 marks and how to earn them",
    slug="enl3-how-composition-is-assessed",
    minutes=24,
    summary="Section A composition carries 20 marks: content and organisation 10, expression 8, accuracy 2, with at least 500 words, concealed identity and no obscene language. Learn what each heading rewards, how to check your own essay, and how to manage the time.",
    objectives=[
        "State the three assessment headings and their marks",
        "Explain what examiners reward under each heading",
        "Apply a checklist to a sample paragraph and correct its errors",
        "Plan time for choosing a topic, planning, writing and checking",
    ],
    key_concepts=["Content and organisation", "Expression", "Accuracy", "500 words", "Identity concealment", "Proofreading"],
    blocks=[
        H("Introduction"),
        T("Two candidates in Bertoua write on the same title. The first writes 620 words, with a clear plan, careful paragraphs and a few small spelling slips. "
          "The second writes 280 words packed with big words but no plan and many sentence errors. Most teachers would expect the first to earn many more marks. "
          "This lesson explains why, by showing exactly how the Board assesses a composition."),
        T("In Paper 2, Section A (Composition), you choose one of six topics and write an essay of 20 marks. The paper as a whole lasts 2 hours 15 minutes and also contains Section B (Prescribed texts) and Section C (Creative writing), so you must use your time carefully."),
        H("The three headings"),
        KEY("What the Board assesses", "Taken from the Board's syllabus; read it carefully.", cards=[
            ["Content and organisation: 10 marks", "Relevance to the topic; creativity; logical arrangement of ideas and paragraphing; liveliness and freshness of imagination; progression from the introduction through the development to the conclusion; an appropriate point of view; a sense of audience."],
            ["Expression: 8 marks", "A range of skills of expression and an appropriate style; clarity, coherence, adequacy, range and aptness of vocabulary; judicious and imaginative use of figurative language; tone suited to the reader or audience."],
            ["Accuracy: 2 marks", "Writing without lapses in syntax and sentence structure; common words spelt correctly; punctuation that helps the sense instead of blocking it."],
        ]),
        D("Quality is more important than quantity, but the composition **should not be less than 500 words**. There is a **proportionate deduction of marks** if it is shorter. "
          "Candidates must use the **name and address provided** to conceal their identity, must **suit their style and point of view** to the reader and the kind of writing, and **must not use obscene language**.", title="Length and rules"),
        TIP("Notice the weights. Content and organisation together with expression carry 18 of the 20 marks. Accuracy carries only 2 marks, but errors can also make your meaning unclear and reduce your expression and content marks. Do not ignore accuracy."),
        H("What earns marks under each heading"),
        KEY("Content and organisation (10)", "Think of it as: Did you answer the question, and did you build the essay well?", cards=[
            ["Relevance", "Every paragraph connects to the title. Re-read the title before each paragraph."],
            ["Creativity", "Fresh ideas and details; not the same story everybody writes."],
            ["Structure", "An introduction, a body of separate paragraphs, a conclusion, and a logical order."],
            ["Point of view and audience", "A consistent narrator; a style suitable for the reader (a formal speech to officials; an informal story)."],
        ]),
        KEY("Expression (8)", "Think of it as: How well do you use language?", cards=[
            ["Vocabulary", "Exact and varied words; no repetition of 'very', 'nice', 'thing'."],
            ["Sentences", "A mixture of short and long sentences; clear and connected."],
            ["Figurative language", "A few apt similes, metaphors or personification, not a pile of them."],
            ["Tone", "Suits the topic: serious, lively, polite, humorous."],
        ]),
        KEY("Accuracy (2)", "Think of it as: Is the English correct?", cards=[
            ["Syntax", "Complete sentences; correct agreement and tenses; no run-on sentences."],
            ["Spelling", "Common words correct (necessary, government, believe)."],
            ["Punctuation", "Capital letters, full stops, commas, apostrophes, speech marks used to help the reader."],
        ]),
        H("Worked examples"),
        EX("Worked example 1: assess a paragraph",
           intro="A candidate writes in a discursive essay: 'Many peoples thinks that technology is a good thing for student but i dont no. Some students uses phones for play game all the day and dont read book there is many bad effect.' Identify the problems.",
           steps=[
               S("Accuracy", text="'peoples thinks' (people think); 'student' (students); 'i' (I); 'dont' (don't); 'no' (know); 'uses' (use); 'play game' (play games); 'all the day' (all day); 'dont read book' (don't read books); a run-on sentence; 'there is' (there are). Many errors."),
               S("Expression", text="The vocabulary is simple and repeated; no linking words; no variation; the tone is not formal."),
               S("Content and organisation", text="The idea (technology may distract students) is relevant but not developed; there is no example."),
               S("Improved version", text="Many people believe that technology helps students. However, I am not convinced, because some students spend the whole day playing games on their phones instead of reading. The effects on their results can be serious."),
           ]),
        EX("Worked example 2: how many words?",
           intro="A candidate counts ten words per line and writes thirty-eight lines in total. Is this enough?",
           steps=[
               S("Calculate", text="10 words x 38 lines = 380 words."),
               S("Compare", text="The syllabus asks for at least 500 words. A candidate needs about 50 to 55 lines at ten words a line; the number of words per line differs with handwriting, so count a few lines carefully in practice and learn your own average."),
               S("Conclusion", text="380 words is too short; expect a proportionate deduction. Plan for about 550 words to be safe."),
           ]),
        EX("Worked example 3: a time plan",
           intro="Plan the time for Section A if you give it about 50 minutes. (These are KKEVO suggestions, not Board rules.)",
           steps=[
               S("Choose the topic", text="3 minutes: read all six, pick one by form and examples you know."),
               S("Plan", text="5 minutes: angle, form, paragraph plan."),
               S("Write", text="35 minutes: about 550 words."),
               S("Check", text="7 minutes: tenses, spelling, punctuation, paragraphs, word count. Total: 50 minutes."),
           ]),
        H("A checklist for your own essays"),
        CODE("Content and organisation\n"
             "  [ ] My essay answers the title (and the picture, if there is one)\n"
             "  [ ] Introduction, body paragraphs and conclusion\n"
             "  [ ] One main idea in each paragraph; logical order\n"
             "  [ ] My point of view and tone suit the reader and the form\n"
             "Expression\n"
             "  [ ] Varied, exact vocabulary; no repeated 'very' or 'nice'\n"
             "  [ ] Short and long sentences; linking words used well\n"
             "  [ ] A few apt figures of speech\n"
             "Accuracy\n"
             "  [ ] Tenses consistent; subject-verb agreement checked\n"
             "  [ ] Common words spelt correctly\n"
             "  [ ] Capital letters, full stops, apostrophes, speech marks\n"
             "Rules\n"
             "  [ ] At least 500 words\n"
             "  [ ] Identity concealed; only the name/address given on the paper\n"
             "  [ ] No obscene language", "text", title="Self-assessment checklist"),
        T(IDENTITY),
        MISTAKE("Spending all the time writing and none on planning or checking",
                "A five-minute plan saves time later and improves organisation. A five-minute check often finds errors worth several marks."),
        MISTAKE("Padding to reach 500 words",
                "Repeating the same idea in different words does not earn marks. Develop more points or add examples instead."),
        MISTAKE("Writing your own name or school",
                "This breaks the rule on identity. Use only the name and address provided on the paper."),
        MISTAKE("Choosing the topic that sounds easiest without a plan",
                "Choose the topic about which you have the best ideas and examples, not the shortest title."),
        TIP("Exam link: Paper 2 Section A is worth 20 marks. Use the headings to improve your own practice essays: ask a friend or teacher to score yours for content and organisation, expression and accuracy separately."),
        QUIZ("How many marks does the accuracy heading carry?",
             ["2", "8", "10", "20"],
             0, "Accuracy is 2 marks; expression is 8; content and organisation is 10; the total is 20.",
             hint="It is the smallest heading.",
             feedback=["", "That is expression.", "That is content and organisation.", "That is the total."]),
        QUIZ("A candidate writes only 300 words on an otherwise good essay. What does the syllabus say?",
             ["The essay will be marked with no penalty.", "The essay will not be marked.", "There will be a proportionate deduction of marks.", "The accuracy mark is lost."],
             2, "The Board states that the composition should not be less than 500 words and that marks are reduced in proportion if it is shorter.",
             hint="Think about the word 'proportionate'.",
             feedback=["The syllabus states a deduction.", "It is marked, with a deduction.", "", "The deduction applies to the essay's mark."]),
        PQ("State the three headings of the composition assessment and the marks for each.",
           "Content and organisation, 10 marks; expression, 8 marks; accuracy, 2 marks. Total 20."),
        PQ("List four things the Board looks for under content and organisation.",
           "Relevance to the topic; creativity; logical arrangement of ideas and paragraphing; liveliness and freshness of imagination; progression from the introduction through the development to the conclusion; an appropriate point of view and a sense of audience. (Any four.)"),
        PQ("Correct this sentence and name the three errors: 'The goverment have decided to build a new road but the people is not happy'.",
           "'The government has decided to build a new road, but the people are not happy.' Errors: misspelling (goverment); agreement (government is singular here, so 'has'; people is plural, so 'are'); punctuation (a comma before 'but' improves the sentence)."),
        PQ("A candidate writes a strong essay but signs it with his school's name. Explain the rule and what he should have done.",
           "Candidates must conceal their identity by using the name and address provided on the paper. He should not have given any personal or school details; if a name was required, only the one provided should have been used."),
        SUM("The composition is marked out of 20: content and organisation 10, expression 8, accuracy 2.",
            "Write at least 500 words; fewer words mean a proportionate deduction.",
            "Conceal your identity with the name and address provided; do not use obscene language; suit style and point of view to the reader.",
            "Plan, write and check: about 3, 5, 35 and 7 minutes is a suggested KKEVO split for a 50-minute section.",
            "Use the checklist on every practice essay."),
    ],
))

# ------------------------------------------------------------------ X1. Paper 1
LESSONS.append(lesson(
    module=M_X,
    topic=T_P1,
    title="Paper 1: 50 multiple-choice questions in 1 hour 30 minutes",
    slug="enx-paper-1-english-language",
    minutes=24,
    summary="Paper 1 has 50 multiple-choice questions in four sections: Reading comprehension 10, Speech work 10, Grammar 20, Vocabulary 10. Learn the structure, a timing plan, a method for each section and how to use elimination.",
    objectives=[
        "State the structure of Paper 1 and the number of questions in each section",
        "Plan the 90 minutes sensibly across the four sections",
        "Apply a method for each section: reading, speech work, grammar and vocabulary",
        "Use elimination and checking to avoid careless errors",
    ],
    key_concepts=["Paper 1", "Multiple choice", "Elimination", "Timing", "Section A-D"],
    blocks=[
        H("Introduction"),
        T("Paper 1 looks easy because you only have to choose A, B, C or D. In fact, the choices are written to tempt a careless candidate. "
          "Each wrong option is usually a real mistake: a wrong tense, a word that sounds right, a sound that looks right. "
          "Success depends on knowledge of the language and on method."),
        H("The structure of the paper"),
        KEY("Paper 1 (official structure)", "50 multiple-choice questions, 1 hour 30 minutes, 1 mark each.", cards=[
            ["Section A: Reading comprehension", "10 questions on one or more passages (about 750 to 1,000 words in total in our practice paper)."],
            ["Section B: Speech work", "10 questions on consonant and vowel sounds, phonemic transcription, word stress, sentence stress and intonation."],
            ["Section C: Grammar", "20 questions on parts of speech, nouns, verbs, reported speech, clauses, punctuation and other grammar topics."],
            ["Section D: Vocabulary", "10 questions on word choice, connotation and figures of speech, affixes, synonyms and antonyms, confused words, idioms and spelling."],
        ]),
        D("The questions follow the order A, B, C, D. Paper 2 (Composition, Prescribed texts, Creative writing) and Paper 3 (Summary, Text reconstruction, Editing) are separate written papers of 2 hours 15 minutes each.", title="Where Paper 1 fits"),
        H("A timing plan"),
        T("Ninety minutes for fifty questions is an average of 1 minute 48 seconds each. But the sections do not need equal time: reading questions take longer because you must read the passage, while many grammar and vocabulary questions can be answered in under a minute. This is a KKEVO suggestion, not a Board rule."),
        CODE("Section A  Reading        10 questions   about 30 minutes (read once, answer from the text)\n"
             "Section B  Speech work    10 questions   about 12 minutes\n"
             "Section C  Grammar        20 questions   about 22 minutes\n"
             "Section D  Vocabulary     10 questions   about 11 minutes\n"
             "Check                                    about 15 minutes\n"
             "Total                                    90 minutes", "text", title="Suggested timing"),
        TIP("Do the quick sections first if you prefer: some candidates answer Sections B to D before the reading. Be careful to put each answer in the right place on the answer sheet. Follow your paper's instructions about how to mark answers."),
        H("A method for each section"),
        KEY("Section A: reading comprehension", "The answer is always in the passage.", cards=[
            ["Skim, then read", "Read the passage once for the main idea; then read each question and find the lines that answer it."],
            ["Prove it", "Choose the option you can support with words from the passage. Do not use outside knowledge."],
            ["Beware of extremes", "Options with 'all', 'never', 'always' are often wrong. Options that are true in life but not in the passage are wrong."],
            ["Vocabulary in context", "Replace the word with each option and check that the sentence still has the same meaning."],
        ]),
        KEY("Section B: speech work", "Written questions about sounds, so go by sound and rule, not spelling.", cards=[
            ["Say it aloud (quietly)", "Say the word in your head or whisper it. Spelling misleads: 'ough' is pronounced differently in cough, though and through."],
            ["Use the symbols", "Know the main IPA vowel and consonant symbols; transcribe slowly."],
            ["Stress", "Count syllables; use rules for nouns and verbs; check suffixes such as -tion, -ic, -ity."],
            ["Intonation", "Statements and wh-questions usually fall; yes/no questions usually rise; check your textbook for exceptions."],
        ]),
        KEY("Section C: grammar", "Test each option for one clear fault.", cards=[
            ["Find the grammar point", "Is it tense, agreement, voice, reported speech, pronoun, article, punctuation?"],
            ["Read the sentence with each option", "The best option is complete, correct and natural."],
            ["Check for the exact link", "Look at the words around the gap: 'since' or 'for', 'much' or 'many'."],
            ["Watch for two correct-looking options", "The question asks for the BEST one; choose the one that fits the context."],
        ]),
        KEY("Section D: vocabulary", "Meaning, form and use.", cards=[
            ["Meaning in context", "The word may have several meanings; the sentence decides."],
            ["Word class", "A gap after 'the' needs a noun; before a noun it may need an adjective."],
            ["Fixed phrases", "Idioms and collocations do not change: 'make a decision', not 'do a decision'."],
            ["Spelling", "Choose the form you have seen in print; use the rules."],
        ]),
        H("Elimination and checking"),
        EX("Worked example 1: elimination",
           intro="'Neither of the girls ______ present.' A. were B. are C. is D. have been",
           steps=[
               S("Subject", text="'Neither' takes a singular verb in standard English."),
               S("Eliminate", text="A (were), B (are) and D (have been) are plural forms."),
               S("Answer", text="C. is."),
           ]),
        EX("Worked example 2: a speech question",
           intro="Which word has the same vowel sound as 'beat'? A. bit B. seat C. best D. bat",
           steps=[
               S("Identify the sound", text="'Beat' has the long vowel /i:/."),
               S("Compare", text="'Bit' /bɪt/ is short; 'seat' /si:t/ is long /i:/; 'best' /best/ and 'bat' /bæt/ have different vowels."),
               S("Answer", text="B. seat."),
           ]),
        EX("Worked example 3: a vocabulary question",
           intro="The committee decided to ______ the meeting until the chairman returned. A. postpone B. cancel C. finish D. open",
           steps=[
               S("Meaning needed", text="The meeting will happen later, after the chairman returns."),
               S("Test", text="'Cancel' means it will not happen; 'finish' and 'open' do not fit. 'Postpone' means to move to a later time."),
               S("Answer", text="A. postpone."),
           ]),
        MISTAKE("Choosing the first option that seems right",
                "Two options can look right. Read all four before choosing, and check the one you pick against the sentence."),
        MISTAKE("Answering from spelling in speech work",
                "Words like 'one', 'women' and 'ocean' break spelling patterns. Trust the sound."),
        MISTAKE("Spending too long on one hard question",
                "Mark it, move on and come back. A 1-mark question is not worth five minutes."),
        MISTAKE("Leaving questions unanswered",
                "Answer every question. If you must guess, eliminate the options you know are wrong first, then choose. Check your paper's instructions about marking."),
        TIP("Exam link: Use the mock exam on this platform under timed conditions. After marking, look at the results by topic and revise the topics where you lost marks."),
        QUIZ("How many questions are there in Section C (Grammar) of Paper 1?",
             ["10", "20", "30", "50"],
             1, "Section C has 20 questions; A, B and D have 10 each.",
             hint="It is the biggest section.",
             feedback=["That is each of A, B and D.", "", "Not the number of any section.", "That is the total."]),
        QUIZ("What is the best first step on a reading comprehension question?",
             ["Choose from your memory of similar passages", "Find the lines in the passage that answer it", "Pick the longest option", "Choose the option with 'always'"],
             1, "The answer is supported by the passage. Always locate the evidence.",
             hint="Where is the answer?",
             feedback=["Use the passage, not memory.", "", "Length is not a clue.", "Words like 'always' often make an option wrong."]),
        PQ("State the structure of Paper 1: number of questions in each section, total questions and time.",
           "Section A Reading comprehension 10; Section B Speech work 10; Section C Grammar 20; Section D Vocabulary 10; total 50 questions in 1 hour 30 minutes."),
        PQ("A candidate has 90 minutes. Suggest a timing plan for the four sections and a final check.",
           "For example: Section A about 30 minutes; Section B about 12; Section C about 22; Section D about 11; about 15 minutes to check. (KKEVO suggestion; any sensible plan that leaves time for checking is accepted.)"),
        PQ("Explain how elimination works with this question: 'She has lived here ______ 2015.' A. for B. since C. from D. during.",
           "She has lived here (present perfect) from a point in the past to now. 'Since' is used with a starting point (2015). 'For' goes with a length of time (for six years). 'From' and 'during' do not fit the present perfect with a year. Answer: B."),
        PQ("Give three habits that lose marks in a multiple-choice paper and how to avoid each.",
           "Choosing the first option that seems right (read all four); answering speech work from spelling (trust the sound); spending too long on one question (mark it and return); leaving questions blank (eliminate then choose)."),
        SUM("Paper 1: 50 multiple-choice questions in 1 hour 30 minutes: Reading 10, Speech work 10, Grammar 20, Vocabulary 10.",
            "Plan your time: reading takes longest; leave about 15 minutes to check.",
            "Reading: the answer is in the passage. Speech work: trust sound and rule. Grammar: find the point being tested. Vocabulary: meaning, word class and fixed phrases.",
            "Eliminate wrong options by their faults; answer every question.",
            "Take the timed mock and revise by topic."),
    ],
))

