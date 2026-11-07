"""A Level English Language (0730), Upper Sixth: Prescribed Texts (8 lessons), Creative Writing (3 lessons) and Examination (Paper 1, Paper 2).

Facts about the examination come from the Board's revised 0730 syllabus and its 2023 subject report (paraphrased; no mark splits beyond
those the syllabus gives). The official prescribed texts are Soyinka's The Swamp Dwellers (in Three Short Plays), Ben Jama's Twilight of
Misty Foliage, Osman Conteh's Unanswered Cries, Hemingway's The Old Man and the Sea, and poems from the Board's anthology list.
Plot, character and theme facts are given ONLY for the works the author knows well (The Swamp Dwellers in outline, The Old Man and the Sea,
'If' and 'If We Must Die'), paraphrased, with a reminder to check them against the student's own copy. For Twilight of Misty Foliage,
Unanswered Cries and the other anthology poems the lessons give study prompts only. All extracts, poems, plays, stories and reports
written for these lessons are original and invented (names, places and figures are invented).
"""

from .dsl import *  # noqa: F403

COURSE = ("english-language", "upper-sixth")

M_TEXTS = "Prescribed Texts"
M_CREATE = "Creative Writing"
M_EXAM = "Examination"
T_WRITE = "Writing about prescribed texts"
T_DRAMA = "Drama"
T_PROSE = "Prose"
T_POETRY = "Poetry"
T_STORY = "Short stories and sketches"
T_POEMPLAY = "Poems and plays"
T_REPORT = "Reports of meetings and news reports"

OWNCOPY = ("**Use your own copy.** This lesson gives you a method and a few well-known facts, written in our own words. Every fact you "
           "use in an essay must be checked against your own copy of the text, because editions and teachers' notes differ.")

LESSONS = []

# ------------------------------------------------------------------ 1. Writing about prescribed texts: the essay
LESSONS.append(lesson(
    module=M_TEXTS, topic=T_WRITE,
    title="Planning and writing a prescribed-text essay",
    slug="enu2-prescribed-text-essay",
    minutes=24,
    summary="A reusable method for the prescribed-text essay: read the question, plan in five minutes, write Point-Evidence-Explain-Link paragraphs, cite titles and authors correctly, and keep every example inside the five prescribed texts.",
    objectives=[
        "Say what Paper 2 Section B asks and what the Board's syllabus says it rewards",
        "Break a question into its command word, its focus and the number of texts required",
        "Plan and write a paragraph using Point, Evidence, Explain and Link",
        "Cite titles and authors correctly and avoid the errors the Board's report describes",
    ],
    key_concepts=["Command word", "Focus of a question", "Point-Evidence-Explain-Link", "Citing a text", "Linking an essay to the texts"],
    blocks=[
        H("Introduction"),
        T("Imagine two students in Bamenda, both of whom have read the prescribed texts twice. One writes a long retelling of a story and gets a low mark. The other writes four tight paragraphs that each make a point, prove it from a text and explain why it matters. She gets a high mark. The difference is not reading. It is **method**."),
        T("In Paper 2 Section B you answer **one** of four questions in about 45 minutes. The questions are essays and extracts, and the section carries 20 marks. The questions are set on the five prescribed texts: a play, three prose works and poems from the anthology. This lesson gives you a method that works for any text. The next lessons apply it to drama, prose and poetry."),
        T(OWNCOPY),
        H("What the Board rewards"),
        D("The Board's syllabus says candidates are assessed more on expression, accuracy, clarity, coherence, the range and aptness of vocabulary, careful and imaginative use of figurative language, and the ability to **link the essay with the prescribed texts** appropriately.", title="From the syllabus (paraphrased)"),
        T("Look at that list. 'Retelling the plot' is not on it. Examiners want an argument, in good English, proved from the texts. The Board's 2023 subject report adds what went wrong: shallow answers with little or no illustration, titles and authors cited wrongly, and examples taken from books that are not on the syllabus. In one question candidates used two texts when three were expected."),
        H("Step 1: read the question"),
        T("Underline three things before you write anything. First the **command word** (discuss, explain, illustrate, compare, show how). Second the **focus** (a theme, a character, a technique, a symbol). Third the **number of texts** (one named text, 'two or more' or 'three')."),
        KEY("Four question types", "Most essay questions fall into one of these families. Name the family and you know what to plan.", cards=[
            ["Theme", "Choose a theme such as hope, sacrifice or injustice. Show it in each text asked for and say what each writer thinks about it."],
            ["Character", "Describe what a person is like, then show how the writer builds the person by words, actions and what others say."],
            ["Technique or symbol", "Name the device (symbol, setting, irony, point of view) and explain its effect. Do not only name it."],
            ["Comparison", "Show a similarity and a difference between texts. Use a joining word such as whereas or similarly."],
        ]),
        H("Step 2: plan for five minutes"),
        T("Write a plan on your rough page: a one-sentence answer to the question (your **thesis**), then three or four points, and for each point the text and the moment you will use. Cross the plan out neatly when you finish. The Board's report advises that candidates cross out the plan, not the finished work."),
        IMG("al-enu2-essay-time.svg", alt="A bar divided into time for a 45 minute prescribed text essay: 5 minutes plan, 5 introduction, 25 body, 5 conclusion, 5 check.", caption="Figure 1. A suggested use of the 45 minutes for the prescribed-text question."),
        H("Step 3: write Point, Evidence, Explain, Link"),
        D("Each body paragraph has four parts: **Point** (a clear sentence that answers the question), **Evidence** (a moment, an event or a few exact words from the text), **Explain** (what the evidence shows and how the writer's choice creates that effect) and **Link** (back to the question, or across to another text).", title="Point-Evidence-Explain-Link (PEEL)"),
        T("Keep quotations to a few words copied exactly from your own copy. A short reference to a moment ('when the old man sees the first shark') can be strong evidence too. Never write long passages from memory: wrong quotations lose marks. Write about the text in the **present tense**: 'Hemingway shows', 'the speaker urges'."),
        EX("Worked example 1: planning", intro="Question (written for practice): 'Discuss the theme of endurance in two of the texts you have studied.' Plan an answer using The Old Man and the Sea and Kipling's poem 'If'.", steps=[
            S("Underline the question", text="Command word: discuss. Focus: endurance (carrying on through hardship). Number of texts: two."),
            S("Write the thesis", text="Both writers admire endurance, but Hemingway shows it through action at sea while Kipling teaches it through advice."),
            S("Point 1 (Hemingway)", text="Santiago keeps fighting the huge fish for a long time despite pain. Evidence: the cramped hand and the long struggle."),
            S("Point 2 (Hemingway)", text="He keeps his dignity after the sharks destroy the catch. Evidence: he fights each shark and returns with the skeleton."),
            S("Point 3 (Kipling)", text="The poem lists tests of character and says the person who stays steady is mature. Evidence: the repeated 'if' clauses."),
            S("Link and conclusion", text="Both texts say that worth lies in how a person meets difficulty, not only in the result."),
        ]),
        EX("Worked example 2: one PEEL paragraph", intro="Write one body paragraph for Point 1 of the plan above.", steps=[
            S("Point", text="Hemingway presents endurance as the quality that gives Santiago his dignity."),
            S("Evidence", text="In The Old Man and the Sea, the old fisherman keeps fighting the great marlin for a very long time, even though the line cuts his hands and his body aches."),
            S("Explain", text="The long struggle shows that endurance here is a matter of will, not only of strength. The simple, repeated actions of the fisherman make the effort feel real."),
            S("Link", text="Santiago therefore earns the reader's respect before the result is known, which prepares the main idea that a person's worth lies in effort and courage."),
        ]),
        H("Citing texts correctly"),
        T("Write the full title the first time, with the author's surname: 'In The Old Man and the Sea, Hemingway shows...'. Underline titles of books and plays when you write by hand. Put poem titles in quotation marks, for example 'If' by Kipling. After that you may say 'the novella' or 'the poem'. Spell characters' names exactly as in your copy."),
        MISTAKE("Using books that are not on the syllabus", "The Board's report says some candidates illustrated their answers with famous novels that are not prescribed. These earn no credit for the section. Use only the five prescribed texts, including poems from the Board's anthology list."),
        MISTAKE("Retelling the story", "A paragraph that starts 'First... then... after that...' is a plot summary. Start each paragraph with a point that answers the question, and use only the part of the story that proves it."),
        MISTAKE("Naming a device without explaining it", "'The writer uses a metaphor' earns almost nothing. Write what the metaphor compares, what it makes the reader feel or understand, and why that matters for your point."),
        TIP("Exam link: Paper 2 Section B (essay and extract questions, one to be answered). Practise by planning ten different questions in five minutes each. Planning is the skill that improves marks fastest."),
        QUIZ("A question asks you to discuss a theme 'in three of the prescribed texts'. What is the best way to answer?", [
            "Write about one text in great detail", "Write about two texts because that is enough", "Use three prescribed texts, each with at least one clear example", "Use any three famous books you know"], 2,
            "The question states the number of texts. Using three different prescribed texts meets the demand.",
            hint="Underline the number in the question.",
            feedback=["One text will not meet a question that asks for three.", "The Board's report notes that using two texts when three were expected loses marks.", "", "Texts outside the prescribed list earn no credit."]),
        QUIZ("Which sentence is the strongest topic sentence (the Point) for a paragraph on the theme of hope?", [
            "The story is about a man.", "Hope is shown at the start of the text.", "The writer presents hope as a force that keeps characters alive when everything else seems lost.", "Hope is a good thing."], 2,
            "A strong Point makes a clear claim that the rest of the paragraph can prove.",
            hint="Which one makes a claim you could prove from the text?",
            feedback=["It tells us nothing about the question.", "It says where, not what the writer shows.", "", "It is a general opinion, not a claim about the text."]),
        PQ("Break this question into command word, focus and number of texts: 'Illustrate how writers use setting to reveal character in two prescribed texts.'", "Command word: illustrate (give examples and explain them). Focus: setting used to reveal character, so each paragraph must connect a place to what a person is like. Number of texts: two."),
        PQ("Rewrite this weak sentence as a strong Point: 'In the play there is a priest.'", "A possible answer: 'The playwright presents the priest as a powerful figure who profits from the villagers' fear.' (Check the claim against your own copy before using it.) The new sentence makes a claim about the character that can be proved."),
        PQ("Write the Explain sentence for this Evidence: 'The speaker begins many lines with the word if.'", "A possible answer: 'The repeated if creates a steady rhythm like a teacher listing rules, and it makes the reader wait for the final promise, which gives the advice weight.' Notice that the sentence says what the device does, not only that it exists."),
        SUM("Read the question and mark the command word, the focus and the number of texts.", "Plan for five minutes: thesis, three or four points, text and moment for each.", "Write Point, Evidence, Explain, Link paragraphs in the present tense.", "Cite titles and authors correctly and use only the five prescribed texts.", "Keep quotations to a few exact words from your own copy; refer to moments if you are not sure of the words."),
    ],
))

# ------------------------------------------------------------------ 2. Extract questions
EXTRACT_A = ("Ngwa sat beside the window and watched the rain fall on the zinc roofs. The market, which had been a loud river of voices at noon, "
             "had become a silent field of wet plastic sheets. He felt as though the whole town had swallowed its tongue. His mother's warning came "
             "back to him: a man who runs from trouble carries it on his back. He picked up his bag, hesitated, and then walked into the storm.")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_WRITE,
    title="Answering extract questions",
    slug="enu2-extract-questions",
    minutes=22,
    summary="How to answer extract questions on a prescribed text: place the extract, then deal with meaning in context, main message, figures of speech, grammar tasks and links to other texts, using a short model for each.",
    objectives=[
        "Place an extract in the text before answering any question",
        "Give the meaning of a word or phrase in context, not its dictionary meaning alone",
        "Identify a figure of speech, quote it and explain its effect",
        "Handle a grammar task and a link-to-another-text task on an extract",
    ],
    key_concepts=["Extract", "Meaning in context", "Message of a passage", "Figure of speech", "Linking to another text"],
    blocks=[
        H("Introduction"),
        T("Some Section B questions give you a short **extract**, a passage taken from one of the prescribed texts, followed by several small questions. They look easier than an essay, but the Board's 2023 report says extract questions were poorly done: candidates could not give the meaning of words and expressions in context, could not state the message of the passage, did not know comparative devices well, and could not change simple present verbs to the simple past. Some could not illustrate an idea in other prescribed texts."),
        T("This lesson gives you a routine for every type of small question. We practise on an **invented** extract that is not from any prescribed text, so that you learn the method without needing a particular book."),
        H("A routine for any extract"),
        KEY("Read, place, answer", "Do these in order.", cards=[
            ["1. Read twice", "First for the story, then for the details. Underline unusual words and comparisons."],
            ["2. Place it", "Ask: who is speaking or thinking, where are we in the text, and what has just happened?"],
            ["3. Read each question word by word", "Meaning, message, device, grammar or link? Each needs a different answer."],
            ["4. Answer in full sentences", "Use your own words, quote a few exact words when asked, and give a reason."],
        ]),
        T("Here is the invented extract. Read it twice."),
        CODE(EXTRACT_A, "text", title="Invented extract (not from a prescribed text)"),
        H("Meaning in context"),
        D("**Meaning in context** is what a word or phrase means in this particular place. A dictionary gives general meanings; the question wants the one that fits the sentence.", title="Definition"),
        EX("Worked example 1: meaning, message and device", intro="Using the invented extract: (a) Explain 'swallowed its tongue'. (b) State the message of the passage. (c) Identify and explain the figure of speech in 'a loud river of voices'.", steps=[
            S("(a) Meaning in context", text="The phrase does not mean that anyone swallowed anything. It means the town had become completely silent, as if no one dared to speak."),
            S("(b) Message", text="Running away from trouble does not solve it, because the trouble goes with you. Ngwa decides, after hesitating, to face his problem."),
            S("(c) Name the device", text="It is a metaphor, because the market is said to be a river without using 'like' or 'as'."),
            S("(c) Quote and explain", text="The market at noon is full of voices that flow without stopping, as a river does. The comparison makes the noise feel powerful and constant, which makes the later silence more striking."),
        ]),
        H("Grammar tasks on an extract"),
        T("The report mentions a task in which candidates had to find verbs in the simple present and change them to the simple past. Another version may do the opposite. Read the sentence, circle every verb, and change **only** the verbs. Do not change nouns, and remember that irregular verbs change their form."),
        EX("Worked example 2: changing the tense", intro="The sentence is in the simple past: 'Ngwa sat beside the window and watched the rain.' Rewrite it in the simple present.", steps=[
            S("Find the verbs", text="Sat and watched."),
            S("Change each to the simple present for a singular subject", text="Sat becomes sits. Watched becomes watches, with es because the verb ends in ch."),
            S("Write the whole sentence", text="Ngwa sits beside the window and watches the rain."),
        ]),
        H("Linking to another text"),
        T("Some questions ask you to show the same idea (for example sacrifice or injustice) in **other** prescribed texts. Use the extract only to name the idea, then move to the other texts. Name each text and author, say what happens or is said, and explain how it connects. Two clear examples from two different texts beat five vague ones."),
        MISTAKE("Giving the dictionary meaning", "The meaning 'to take food into the stomach' is correct in a dictionary but useless here. Always ask what the phrase means in the situation described."),
        MISTAKE("Retelling the extract", "When asked for the message, do not repeat the passage in other words. State the lesson or idea the writer wants the reader to see, in one or two sentences."),
        MISTAKE("Naming the device but not quoting it", "Write the device, copy the words that contain it, and then say what the comparison or sound does. All three parts are needed."),
        TIP("Exam link: extract questions in Paper 2 Section B. Practise the same routine on a short paragraph from your own prescribed texts. Time yourself: about two minutes per small question."),
        QUIZ("In the invented extract, 'a silent field of wet plastic sheets' is best described as", [
            "a simile because it uses like", "a metaphor because the market is said to be a field", "personification because the market is a person", "a rhyme"], 1,
            "The market is directly called a field without 'like' or 'as', which is the pattern of a metaphor.",
            hint="Look for the words 'like' or 'as'.",
            feedback=["There is no 'like' or 'as' in the phrase.", "", "The phrase does not give the market human actions.", "Rhyme is a sound pattern, not a comparison."]),
        QUIZ("Which answer to 'State the message of the passage' is best?", [
            "Ngwa watches the rain from a window.", "Running away from a problem does not remove it, so Ngwa chooses to face his trouble.", "The market is wet.", "Ngwa's mother is wise."], 1,
            "A message states the idea the passage leads to, not the events.",
            hint="Which answer could be a lesson for a reader?",
            feedback=["That only describes what Ngwa does.", "", "That is a detail of the setting.", "It is partly true but does not say what the passage means."]),
        PQ("Change this sentence to the simple past: 'The market becomes silent and the rain beats on the roofs.'", "The market became silent and the rain beat on the roofs. (Becomes changes to became and beats to beat, because beat has the same form in the past tense. Check each irregular verb.)"),
        PQ("Explain the meaning in context of 'carries it on his back' in the invented extract.", "It means that a person who runs away from a problem still has the problem with him wherever he goes, as if it were a heavy load on his back. The mother is warning Ngwa that escape is not a solution."),
        PQ("A question says: 'Show how the idea of sacrifice appears in other prescribed texts.' Describe how you would structure the answer, without naming events you are not sure of.", "Name two or three other prescribed texts by title and author. For each, give one specific moment from your own copy where a character gives up something important for others, then explain what the writer shows about the cost or the value of the sacrifice. Finish with a sentence that links the texts. Do not use books outside the prescribed list."),
        SUM("Place the extract first: who speaks, where, and what has happened.", "Meaning in context means the meaning that fits this passage.", "A message is an idea, not a retelling.", "Name a figure of speech, quote it, and explain its effect.", "For grammar tasks, change only the verbs; for link questions, use other prescribed texts correctly cited."),
    ],
))

# ------------------------------------------------------------------ 3. Drama: how to read and write about a play
SCENE_A = ("SCENE: A roadside bench outside a bus park at dusk. MAMA ADA, a fruit seller, is counting coins. ENOW, a driver, hurries in.\n\n"
           "ENOW: (not looking at her) Mama, the bus leaves in five minutes.\n"
           "ADA: (still counting) Then it will leave in four.\n"
           "ENOW: (laughing, then stopping) You have been counting that money since morning.\n"
           "ADA: (closing her hand) It has been counting me.\n"
           "(A horn sounds. ENOW does not move.)")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_DRAMA,
    title="Reading and writing about a play",
    slug="enu2-drama-how-to-write",
    minutes=22,
    summary="A framework for writing about drama: the play as something performed, stage directions, dialogue, conflict, character, setting, structure and theme, with a worked analysis of a short invented scene.",
    objectives=[
        "Explain how a play differs from a novel and why that changes how we write about it",
        "Use the terms stage direction, dialogue, conflict, setting, climax and dramatic irony correctly",
        "Show how character is revealed through speech, action and what others say",
        "Write a Point-Evidence-Explain-Link paragraph about a dramatic technique",
    ],
    key_concepts=["Stage direction", "Dialogue", "Conflict", "Setting", "Dramatic irony", "Plot structure"],
    blocks=[
        H("Introduction"),
        T("A novel is read alone, but a play is written to be **performed**. When a company of actors in Buea or Bamenda prepares a play, they have only the words on the page to decide how to stand, how to speak and how to move. That is why a good essay on drama talks about what the audience sees and hears, not only about what the characters say."),
        T("The Board's syllabus asks you to identify themes, character traits and literary techniques, and to show how the writer's choices of language, form and structure create meaning. This lesson gives you a framework for the play on your list, The Swamp Dwellers, and for any other play."),
        T(OWNCOPY),
        H("The parts of a play"),
        KEY("What a playwright controls", "Look for each of these in a scene.", cards=[
            ["Dialogue", "What characters say to each other. Notice who speaks most, who interrupts and who stays silent."],
            ["Stage directions", "The playwright's instructions about setting, movement, tone and silence. They are often printed in brackets or italics."],
            ["Setting", "The place and time. In a play the setting is a real space on stage that actors must live in."],
            ["Structure", "How the story is arranged in acts and scenes: introduction, rising tension, climax and resolution."],
        ]),
        D("**Conflict** is the struggle that drives a play. It can be between people, between a person and a group, between a person and nature or between ideas inside a person.", title="Definition"),
        D("**Dramatic irony** happens when the audience knows something that a character does not. It creates tension or pity because we see the danger the character cannot.", title="Definition"),
        H("How character is revealed"),
        T("A novel can tell us what a person thinks. A play must **show** it. So ask four questions about every important character: What does the person say? What does the person do? What do other characters say about them? What do the stage directions tell us about their tone and movement? A character who says one thing and does another is usually being shown as weak, afraid or dishonest."),
        T("Read this short **invented** scene (not from a prescribed play) and then watch the method at work."),
        CODE(SCENE_A, "text", title="Invented scene"),
        EX("Worked example 1: analysing a scene", intro="How does the playwright reveal Mama Ada's character in this scene?", steps=[
            S("Point", text="The playwright presents Mama Ada as careful with money but also quick-witted."),
            S("Evidence from dialogue", text="Her reply that the bus will leave in four minutes turns the driver's warning into a joke. Her last line suggests that the money is holding her, not the other way round."),
            S("Evidence from stage directions", text="She keeps counting while she talks, and she closes her hand when the driver mentions the money. These actions show that she guards what she has."),
            S("Explain and link", text="Together, speech and action show a woman who has learned to survive by watching every coin. The silence at the end, when the driver does not move, suggests that he cares about her more than he admits. The scene therefore links money with worry and with human concern."),
        ]),
        H("Structure and theme"),
        T("Most plays follow a pattern: an **opening** that shows the situation, **rising action** in which tension grows, a **climax** at the highest point of conflict and a **resolution** that shows what has changed. Some plays, including short ones, end with a question rather than an answer. When you write about structure, say what each part does for the audience and why the playwright put it there."),
        T("A **theme** is an idea the play explores, such as faith, injustice, family loyalty or the pull between village and city. Never say a theme in one word only. Write it as a sentence: 'The play suggests that people who depend on blind faith can be used by those who control it.' Then prove it with scenes and dialogue."),
        EX("Worked example 2: from observation to theme", intro="Turn the observation 'The characters wait a lot' into a themed Point for an essay on any play.", steps=[
            S("State the observation", text="Characters spend long periods waiting, and silences interrupt their conversation."),
            S("Ask what waiting suggests", text="It may suggest helplessness, hope, or dependence on something outside their control."),
            S("Write the Point", text="The playwright uses waiting and silence to show how helpless the characters feel in the face of forces they cannot control."),
            S("Choose evidence", text="Pick one moment of waiting from your own copy and one stage direction about silence, and explain each."),
        ]),
        MISTAKE("Writing as if it were a novel", "Do not write 'the narrator says'. A play has no narrator. Write 'the playwright shows', 'the audience sees' or 'the actor would need to'."),
        MISTAKE("Ignoring the stage directions", "Many students quote only speech. Stage directions are part of the writer's language. A direction such as a silence or a gesture can carry as much meaning as a whole speech."),
        MISTAKE("Calling a character good or bad without proof", "Say what the character does and why it matters. Characters in strong plays are mixed, and examiners reward answers that see both sides."),
        TIP("Exam link: drama appears in Paper 2 Section B as essay or extract questions. In an extract question, read the stage directions twice: they usually answer the question about tone or attitude."),
        QUIZ("A character in a play says 'I am not afraid' while the stage direction says his hands are shaking. What does this create?", [
            "A rhyme", "Dramatic irony or a contrast between words and action", "A change of setting", "A flashback"], 1,
            "The audience sees the truth (fear) that the words deny, which reveals the character's real feeling.",
            hint="Compare what is said with what is shown.",
            feedback=["Rhyme is about sound patterns.", "", "The place does not change.", "No earlier time is shown."]),
        QUIZ("Which sentence uses the correct vocabulary for writing about a play?", [
            "The narrator describes the village.", "The playwright uses a stage direction to show the villagers' silence.", "The author tells us in chapter two.", "The poet repeats the word."], 1,
            "A play has a playwright, stage directions and scenes or acts, not a narrator or chapters.",
            hint="Which one fits a play and not a novel or a poem?",
            feedback=["A play has no narrator.", "", "Plays are divided into acts and scenes, not chapters.", "A poet writes poems, not plays."]),
        PQ("Define dramatic irony and say why it is useful to a playwright.", "Dramatic irony is when the audience knows something that a character does not. It is useful because it creates tension, pity or humour: we watch the character move towards a danger or a mistake that we already understand."),
        PQ("Write a Point and an Explain sentence about how a playwright might use a flooded or crowded setting to affect the audience. Do not refer to a specific play.", "Point: The playwright uses a cramped, flooded setting to make the audience feel the characters' lack of choice. Explain: Because the actors must share a small, wet space, every movement feels difficult, and this physical pressure matches the pressure of the conflict between them."),
        PQ("In the invented scene, what is the effect of the final stage direction, 'A horn sounds. ENOW does not move'?", "The horn reminds us that time is running out, but the driver stays. The silence shows that he cares about the woman more than his duty or his words suggest, and it leaves the audience with an unspoken feeling instead of a speech."),
        SUM("A play is written for performance, so write about what the audience sees and hears.", "Use the playwright's tools: dialogue, stage directions, setting and structure.", "Character is shown by speech, action and what others say.", "A theme is a sentence about an idea, proved from scenes.", "Write 'the playwright' and 'the audience', never 'the narrator' or 'chapter'."),
    ],
))

# ------------------------------------------------------------------ 4. The Swamp Dwellers
SD_MAP = ("Setting      A swamp village; floods and failing harvests\n"
          "Cast         Makuri and Alu (an older couple); Igwezu (their son)\n"
          "             the Beggar; the Kadiye (priest of the Serpent of the Swamp)\n"
          "             Awuchike and Desala (linked to Igwezu's story)\n"
          "Conflict     Faith and ritual versus hard facts; villagers versus a\n"
          "             powerful priest; village versus city; hope versus despair\n"
          "Themes       Exploitation, faith, survival, family, rural and urban life")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_DRAMA,
    title="The Swamp Dwellers: a study guide",
    slug="enu2-swamp-dwellers",
    minutes=22,
    summary="A study guide to Wole Soyinka's The Swamp Dwellers, the African play on the list: what is certain about the play, a map of setting, cast, conflict and themes, and prompts that send you back to your own copy for evidence.",
    objectives=[
        "State the author, the form and the setting of The Swamp Dwellers",
        "Name the main characters and the conflicts around them, to be checked against your own copy",
        "Link the setting, the priest and the returning son to the themes of faith and exploitation",
        "Write a Point-Evidence-Explain-Link paragraph on the play with evidence from your own copy",
    ],
    key_concepts=["Wole Soyinka", "Swamp village", "The Kadiye and the Serpent", "Faith and exploitation", "Village and city"],
    blocks=[
        H("Introduction"),
        T("Floods are not a distant idea for many Cameroonians. Farmers on low ground near rivers know what water can do to a harvest in a single week. *The Swamp Dwellers* is a short play about people whose land lies in a swamp, where the water, the failing crops and the village's religion shape every choice they make."),
        T("The play was written by **Wole Soyinka**, a Nigerian writer who was awarded the Nobel Prize in Literature in 1986. It is a short play in the collection *Three Short Plays*, which the Board names as the African text for drama. The Board's list uses the spelling of Soyinka's name given there; use the spelling on your own copy."),
        T(OWNCOPY),
        T("We keep the outline below short on purpose. Your own copy, and your teacher's notes, are the evidence for the essay. If something here does not match your copy, trust your copy and tell your teacher."),
        H("A map of the play"),
        CODE(SD_MAP, "text", title="Study map: The Swamp Dwellers (check each item in your copy)"),
        T("Notice how the map joins things together. The setting (a swamp, with its floods) creates the problem. The problem pushes the characters towards the priest of the Serpent of the Swamp and his rituals. A son who has been to the city comes back with a different view of the world. The conflict is therefore both **outer** (people against a powerful priest, people against the water) and **inner** (belief against doubt)."),
        H("Themes to be ready to discuss"),
        KEY("Four themes for essays", "For each, find at least two moments in your copy.", cards=[
            ["Faith and its limits", "The villagers depend on the Serpent. Ask what the play suggests about trusting a power that does not change their suffering."],
            ["Exploitation", "Ask who gains from the villagers' offerings and who loses. Notice how the priest speaks about duty and sacrifice."],
            ["Village and city", "A son returns from the city. Ask what the city has given or taken from him and how his view of the village changes."],
            ["Survival and hope", "Ask what keeps the older couple going and how they respond to visitors who bring news or demands."],
        ]),
        H("Language and technique"),
        T("Ask these questions as you reread: What images of **water** and **decay** recur in the dialogue? How do the stage directions create atmosphere (light, sound, weather)? How does the speech of the older characters differ from the speech of the one who has returned? Where does the conversation turn into argument, and who has the last word?"),
        EX("Worked example 1: building an essay on setting", intro="Question (written for practice): 'How does Soyinka use the setting of the swamp village to develop the themes of the play?'", steps=[
            S("Thesis", text="Soyinka uses the flooded village as more than a background: it makes the characters' poverty, their dependence on ritual and their conflicts visible to the audience."),
            S("Point 1: setting creates the problem", text="Find in your copy two references to flooding or failing crops and explain how each makes the characters' situation desperate."),
            S("Point 2: setting shapes belief", text="Find a moment where a character explains the trouble by speaking about the Serpent and explain what this shows about how people make sense of disaster."),
            S("Point 3: setting is contrasted", text="Find a moment where the city, or a character from outside, is described. Explain how the contrast makes the village feel more trapped."),
            S("Link", text="End by saying what the setting finally tells us about the playwright's attitude to the villagers: sympathy, criticism or both."),
        ]),
        EX("Worked example 2: a model paragraph, ready for your evidence", intro="Write a paragraph on exploitation in the play. The wording below is a frame; replace the bracketed items with details from your own copy.", steps=[
            S("Point", text="Soyinka presents the Kadiye as a figure who gains from the villagers' fear, while they suffer."),
            S("Evidence", text="[One moment from your copy in which the villagers give or promise offerings, or in which the priest speaks of what is owed.]"),
            S("Explain", text="Because the audience sees the villagers' poverty beside the priest's authority, we ask who is really being served by the ritual."),
            S("Link", text="This links to the theme of faith: the play invites us to question beliefs that keep people powerless, while still feeling for those who hold them."),
        ]),
        MISTAKE("Treating the play as a simple attack on religion", "Do not write that the playwright simply 'hates tradition'. Look at how kindly or sadly the older characters are treated, and at how the city is also shown as a place of loss. Good essays see the complexity."),
        MISTAKE("Using a plot summary instead of evidence", "A list of everything that happens is not an essay. Choose the two or three moments that prove your point and explain them."),
        MISTAKE("Using facts you have not checked", "If you are not sure of a name or an event, refer to the moment carefully ('when the son returns') instead of guessing. A wrong detail costs more than a careful general reference."),
        TIP("Exam link: The Swamp Dwellers is the drama text for Paper 2 Section B. Question families are theme, character, symbol or technique, and comparison with other prescribed texts. For a comparison question, pair it with a text that also deals with power, hardship or survival, and check each example in your copy."),
        QUIZ("Which statement about The Swamp Dwellers is certain from the Board's list and from Soyinka's career?", [
            "It is a novel by Ernest Hemingway.", "It is a play by Wole Soyinka in the collection Three Short Plays.", "It is a poem in the Board's anthology.", "It is a Cameroonian novel."], 1,
            "The Board names The Swamp Dwellers by Wole Soyinka in Three Short Plays as the African drama text.",
            hint="Think of the form and the author.",
            feedback=["Hemingway wrote The Old Man and the Sea.", "", "It is a play, not a poem.", "It is by a Nigerian playwright and it is a play."]),
        QUIZ("Which line of thinking best fits the theme 'village and city'?", [
            "Compare how characters who stayed and a character who left see the swamp.", "Count the number of words in each scene.", "List the colours mentioned in the play.", "Ignore the returning character."], 0,
            "The theme is explored through contrast between those who stayed and one who has seen the city.",
            hint="A theme question wants a comparison of viewpoints.",
            feedback=["", "Word counts do not explore a theme.", "Colours may matter but do not answer the question.", "The returning character is a main source of the contrast."]),
        PQ("Using your own copy, choose one stage direction or description of the setting and explain what atmosphere it creates.", "A good answer names the moment, says what the audience sees or hears, and explains the atmosphere (for example gloom, dampness or tension) and how it supports the conflict. Stay with details that are in your copy."),
        PQ("Write a thesis sentence for the question: 'Discuss the theme of exploitation in The Swamp Dwellers.'", "A possible thesis: 'Soyinka shows that the people who have the least are asked to give the most, and he invites the audience to question those who benefit from their fear.' Support it with evidence from your own copy."),
        PQ("Explain why the returning son is a useful character for the playwright's themes.", "A character who has seen the city can compare the village with another world, so he can question accepted beliefs and make the audience see them differently. His return also creates conflict with those who stayed. Use details from your own copy to show how he speaks and what he challenges."),
        SUM("The Swamp Dwellers is a play by Wole Soyinka in Three Short Plays, set in a swamp village.", "Setting, the priest of the Serpent and a returning son create faith, exploitation and village versus city themes.", "Write about what the audience sees and hears: dialogue, stage directions and setting.", "Check every fact against your own copy and use short evidence, not a plot summary.", "Aim for balanced views: sympathy for the villagers and questions about those who profit."),
    ],
))

# ------------------------------------------------------------------ 5. Prose: how to read and write about a novel or novella
PROSE_A = ("The generator coughed twice and died. In the sudden dark, Mama Teku lit a candle and set it on the table between the two beds. "
           "Outside, the dogs stopped barking, as though they too were waiting. 'It will come back,' she said, but she did not look at her son, "
           "and he knew that she was not speaking only about the light.")

NOTES_TEMPLATE = ("TEXT: title, author, form\n"
                  "SETTING: where and when; how it changes\n"
                  "CHARACTERS: name, role, 3 traits, 1 key moment each\n"
                  "VOICE: who tells the story; how close to the thoughts?\n"
                  "STRUCTURE: opening, turning points, ending\n"
                  "THEMES: 3 ideas, 2 moments for each\n"
                  "LANGUAGE: 3 images or symbols, 3 effects\n"
                  "LINKS: one idea that also appears in another text")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_PROSE,
    title="Reading and writing about a novel or novella",
    slug="enu2-prose-how-to-write",
    minutes=24,
    summary="A framework for prose texts: narrator and point of view, setting, character, structure, theme and language, a notes template for each text, and study prompts for the novels where only your own copy can supply the facts.",
    objectives=[
        "Distinguish first-person, third-person limited and omniscient narration",
        "Explain how setting, character and structure support a theme",
        "Analyse a short passage for narrator, atmosphere and language",
        "Build a notes template for each prose text on your list",
    ],
    key_concepts=["Narrator", "Point of view", "Setting and atmosphere", "Characterisation", "Plot and structure", "Symbol", "Theme"],
    blocks=[
        H("Introduction"),
        T("Three of the five prescribed texts are prose: a Cameroonian novel (*Twilight of Misty Foliage* by Ben Jama), an African-European novel (*Unanswered Cries* by Osman Conteh) and an American novella (*The Old Man and the Sea* by Ernest Hemingway). A novel can have hundreds of pages, so students often panic. The cure is a **method**: the same six questions asked of every prose text."),
        T(OWNCOPY),
        T("For *Twilight of Misty Foliage* and *Unanswered Cries* this course does not tell you the plot, the characters or the ending. Those must come from your own reading. What we give you is a way of reading that makes your own notes sharp, and a template you can fill in."),
        H("Six questions for any prose text"),
        KEY("The six questions", "Write the answers in your notes as you read.", cards=[
            ["1. Who tells it?", "First person ('I'), third person close to one character, or an all-knowing narrator. This decides what we know and how far we can trust it."],
            ["2. Where and when?", "The setting is not only a place. It is mood, social conditions and time, and it often changes as the story moves."],
            ["3. Who are the people?", "Note traits, desires, flaws and how they change. Writers show character by action, speech, thoughts and what others say."],
            ["4. How is it built?", "Look at the opening, the turning points, the climax, the ending and any flashbacks or time jumps."],
            ["5. What is it about?", "Themes are ideas such as loss, justice, power, endurance or loyalty. Link each theme to specific moments."],
            ["6. How is it written?", "Sentence length, word choice, images, symbols, repetition, dialogue and irony."],
        ]),
        H("Narrator and point of view"),
        D("**Point of view** is the position from which the story is told. In **first person** the narrator is a character who says 'I'. In **third person limited** the narrator stays close to one character's thoughts. An **omniscient** narrator knows everything about everyone.", title="Definition"),
        T("Ask what the choice does. A first-person narrator makes the story personal but may be biased. A close third-person narrator can share a character's feelings while keeping a little distance. An omniscient narrator can show a whole community and its history. In an essay, never say 'the writer' when you mean 'the narrator'. They are not always the same."),
        H("Setting, character and structure"),
        T("Setting creates atmosphere and meaning: a village after a storm, a city street at night or the open sea each suggest different feelings and limits. Character is built by **direct** description (the narrator tells us) and **indirect** description (we judge from words and actions). Structure is the order of events. Ask why the writer begins where they do and why they end where they end."),
        T("Now read an **invented** passage (not from a prescribed text) and see how the questions work."),
        CODE(PROSE_A, "text", title="Invented passage"),
        EX("Worked example 1: narrator, setting and language", intro="Analyse the invented passage.", steps=[
            S("Narrator", text="The narrator is outside the characters (third person). The narrator describes Mama Teku's actions and also tells us what her son knows, so we see through the son's understanding."),
            S("Setting and atmosphere", text="A power cut in the dark creates tension. The candle on the table between the beds gives a small circle of light, which suggests a small family surrounded by uncertainty. The dogs falling silent adds to the stillness."),
            S("Language", text="'As though they too were waiting' is a simile-like comparison (it uses as though) that makes the animals share the family's anxious waiting."),
            S("Theme", text="Her sentence about the light returning has a second meaning: she is also talking about hope for something else, and her refusal to look at her son shows she is not sure. The passage hints at the theme of hope under pressure."),
        ]),
        H("A notes template"),
        T("Copy this template for each prose text and fill it in as you read. Short, specific notes with page references are worth more than long summaries."),
        CODE(NOTES_TEMPLATE, "text", title="Notes template (fill in from your own copy)"),
        EX("Worked example 2: using the template for an essay question", intro="Question (written for practice): 'Show how setting contributes to the themes of a prose text you have studied.'", steps=[
            S("Choose the text", text="Pick the text where you have the clearest notes on setting."),
            S("Select two or three settings", text="From your notes on SETTING, choose places or times that change or contrast."),
            S("Match each setting to a theme", text="For each place, state the theme it supports. Use the THEMES section of your notes for moments."),
            S("Add language", text="From your LANGUAGE notes choose one image that makes the setting vivid, and explain it."),
            S("Link", text="Finish with a sentence that shows what the settings together say about the writer's view of people and their world."),
        ]),
        MISTAKE("Mixing up the author and the narrator", "Write 'the narrator tells us' for events inside the story and 'Hemingway shows' for the writer's overall choices. Do not assume the narrator's opinions are the author's."),
        MISTAKE("Describing characters only by adjectives", "'He is brave' is not enough. Write what he does that proves it, and what the writer wants us to think about that bravery."),
        MISTAKE("Writing about the film or the summary instead of the book", "Examiners can tell when you rely on summaries. Refer to scenes, chapters and details only the book provides."),
        TIP("Exam link: prose appears in Paper 2 Section B as essay or extract questions. In extract questions, always begin by saying who is telling the story, where we are in the text and what has just happened."),
        QUIZ("A story is told by a character who says 'I' and takes part in the events. This is", [
            "third-person omniscient", "first-person narration", "dramatic irony", "free verse"], 1,
            "A narrator who says 'I' and takes part is a first-person narrator.",
            hint="Think of the pronoun used.",
            feedback=["An omniscient narrator stands outside the story.", "", "Dramatic irony is a gap in knowledge, not a narrator type.", "Free verse is a poetry form."]),
        QUIZ("Which is an example of indirect characterisation?", [
            "The narrator says that a man is generous.", "A man gives away his last coins without being asked.", "A list of the character's age and height.", "The title of the chapter."], 1,
            "Indirect characterisation shows a trait through action or speech, which the reader interprets.",
            hint="Which option shows rather than tells?",
            feedback=["That is direct characterisation: the narrator tells us.", "", "A fact list tells us basic details only.", "A chapter title does not show character."]),
        PQ("Explain the difference between direct and indirect characterisation, with one example of each.", "Direct characterisation: the narrator tells us what a person is like, for example 'she was a patient woman'. Indirect characterisation: we infer from what the person does or says, for example she waits three hours for a slow bus without complaint. Indirect methods are usually stronger evidence in an essay."),
        PQ("Complete the notes template headings for one of your own prose texts in two lines each. Which heading was hardest and why?", "There is no single answer. A good response fills each heading with specific details from the student's own copy, then identifies the heading with the fewest notes (often language or structure) as the next area to reread."),
        PQ("In the invented passage, why does Mama Teku not look at her son?", "She says the light will come back but does not look at him because she is not sure, or because the sentence is about something larger than the generator. The detail shows indirectly that she is anxious and perhaps trying to hide it."),
        SUM("Ask six questions of every prose text: narrator, setting, characters, structure, theme, language.", "Point of view controls what we know and how much we trust it.", "Characterisation can be direct (told) or indirect (shown); indirect evidence is stronger.", "Keep notes with page references in a template for each text.", "For Twilight of Misty Foliage and Unanswered Cries, all facts must come from your own reading."),
    ],
))

# ------------------------------------------------------------------ 6. The Old Man and the Sea
OMS_MAP = ("PART 1  Santiago, an old Cuban fisherman, has gone 84 days without\n"
           "        a catch. The boy Manolin, who was his helper, now fishes in\n"
           "        another boat on his parents' orders, but still cares for him.\n"
           "PART 2  On the 85th day Santiago sails far out alone, hooks a huge\n"
           "        marlin and is pulled for a very long time. His hands are\n"
           "        hurt, but he does not give up. He kills the fish.\n"
           "PART 3  He lashes the marlin to his skiff, but sharks attack and\n"
           "        eat it. He fights them as long as he can and comes home\n"
           "        with only the skeleton. Manolin cares for him, and the old\n"
           "        man sleeps, dreaming of lions.")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_PROSE,
    title="The Old Man and the Sea: a study guide",
    slug="enu2-old-man-and-the-sea",
    minutes=24,
    summary="A study guide to Hemingway's The Old Man and the Sea: the three-part outline, Santiago and Manolin, the marlin and the sharks, the themes of endurance, dignity and respect for nature, the plain style, and model paragraphs.",
    objectives=[
        "Outline the three parts of the novella in your own words",
        "Describe Santiago and Manolin and the relationship between them",
        "Explain the themes of endurance, dignity in defeat, pride and respect for nature, with evidence",
        "Comment on Hemingway's plain style and on the symbols of the marlin, the sharks and the lions",
    ],
    key_concepts=["Santiago", "Manolin", "The marlin", "The sharks", "The lions", "Endurance", "Dignity in defeat", "Plain style"],
    blocks=[
        H("Introduction"),
        T("Many fishing families in Limbe, Kribi and Douala know what it means to go out before dawn and come back with nothing. *The Old Man and the Sea* is about an old fisherman who has a long run of bad luck and who goes far out to sea to end it. It is short, and its language is simple, but the questions it raises about courage, pride and loss are large."),
        T("The novella was written by the American writer **Ernest Hemingway** and published in 1952. It won the Pulitzer Prize for Fiction in 1953, and Hemingway was awarded the Nobel Prize in Literature in 1954. The Board lists it as the American novella."),
        T(OWNCOPY),
        H("Outline"),
        CODE(OMS_MAP, "text", title="Outline in three parts (in our own words)"),
        T("The setting is the coast of Cuba near Havana and the Gulf Stream, where Santiago fishes from a small skiff, a little rowing and sailing boat. Almost the whole middle of the book happens on the water, far from any other person. The narration is in the **third person**, staying close to Santiago's thoughts. When he is alone, the old man often speaks aloud, so we hear his thoughts as dialogue."),
        H("Characters"),
        KEY("Santiago and Manolin", "Find at least two moments in your copy for each point.", cards=[
            ["Santiago", "Old, thin, experienced and proud. He is a skilled fisherman, he respects the sea and its creatures and he talks about baseball and about his own past strength. Weakness in age does not stop his will."],
            ["Manolin", "A boy who learned to fish from Santiago and still loves him. He brings food and bait, and the book ends with his promise to fish with the old man again. He represents loyalty and the passing on of skill."],
            ["The marlin", "A huge fish that Santiago respects as a worthy opponent and almost as a brother. He admires its strength and feels sorrow as he kills it."],
            ["The sharks", "Hungry predators that destroy the marlin's body. They stand for the forces that wear down even a great effort."],
        ]),
        H("Themes"),
        T("**Endurance.** Santiago keeps fighting through hunger, pain and tiredness. **Dignity in defeat.** He loses the fish but not his self-respect, and the book suggests that effort and courage matter as much as results. **Pride and humility.** He admits that he went out too far, partly out of pride, yet the novella treats his pride with respect. **Man and nature.** He fights the fish but respects it, and he sees himself as part of the same natural world. **Friendship.** Manolin's care for Santiago gives the ending warmth."),
        H("Symbols and style"),
        T("The **lions** that Santiago dreams of on an African beach seem to stand for youth, strength and peace. The **marlin** can be seen as a noble opponent and the **sharks** as destructive forces; some readers also see religious meaning in the way the old man carries the mast home, but critics differ, so say 'some readers see' in an essay. Hemingway's style is plain: short sentences, common words and repetition, often joined by the word 'and'. That simple style makes the effort feel real and quiet."),
        EX("Worked example 1: a paragraph on dignity in defeat", intro="Write a PEEL paragraph for the question: 'Santiago is defeated but not destroyed. Discuss.'", steps=[
            S("Point", text="Hemingway shows that Santiago loses the fish but keeps his dignity."),
            S("Evidence", text="When the sharks attack, the old man fights them with whatever he has, even though he knows the marlin may be lost."),
            S("Explain", text="Because he fights to the end and never blames anyone, the reader admires his courage. Defeat takes away the marlin's flesh, but not the old man's self-respect."),
            S("Link", text="The ending, with Manolin's promise to fish with him again, confirms that Santiago is respected by those who matter to him."),
        ]),
        EX("Worked example 2: a paragraph on style", intro="Comment on Hemingway's plain style and its effect.", steps=[
            S("Point", text="Hemingway uses short, simple sentences to make Santiago's struggle feel direct and honest."),
            S("Evidence", text="Many sentences describe one action at a time, joined by 'and', as in a list of tasks that the fisherman must do."),
            S("Explain", text="The plain language slows the pace to the rhythm of rowing and waiting, and it avoids decoration so that the reader's attention stays on the effort and the pain."),
            S("Link", text="This style supports the theme of endurance, because the sentences themselves seem to keep going, step by step."),
        ]),
        MISTAKE("Calling Santiago a failure", "He returns with only a skeleton, but the novella invites us to judge him by courage and skill as well as results. Use 'defeated but not destroyed' as a starting point and show both sides."),
        MISTAKE("Saying the sharks are 'evil'", "Sharks act by nature, as the marlin did. Write that they represent destructive forces and explain why."),
        MISTAKE("Muddling the characters", "'The boy' is Manolin and 'the fish' is the marlin. Name characters and creatures clearly in your essay so that the examiner can follow your evidence."),
        TIP("Exam link: The Old Man and the Sea is one of the three prose texts for Paper 2 Section B. It pairs well with 'If' for endurance and dignity, and with The Swamp Dwellers for struggle against forces beyond a person's control. Check each pair in your own copy."),
        QUIZ("How many days has Santiago gone without a fish when the novella begins?", [
            "14", "40", "84", "100"], 2,
            "The book opens after 84 days without a catch; on the 85th day he goes far out.",
            hint="The count is more than eighty.",
            feedback=["Far too few.", "Forty is a number from other stories.", "", "It is lower than that."]),
        QUIZ("Which is the best description of Hemingway's style in this novella?", [
            "Long, complex sentences with many difficult words", "Short, simple sentences and everyday words", "Rhyming couplets", "Letters between characters"], 1,
            "The plain style is one of the book's most noticed features.",
            hint="Think of the simple, direct language.",
            feedback=["The opposite is true.", "", "It is prose, not verse.", "It is a narrative, not an exchange of letters."]),
        PQ("Explain the role of Manolin in the novella.", "Manolin shows loyalty and love. He was taught by Santiago, still cares for him, brings him food and supplies and, at the end, promises to learn more from him and fish with him again. He also reminds us that Santiago's skill will pass to a new generation."),
        PQ("Discuss the importance of the sharks in the story.", "The sharks destroy the marlin and show that Santiago's great effort can be undone by forces beyond his control. They give the book its test of endurance and dignity: the old man fights them anyway. Some readers also see them as symbols of the harsh side of nature and of loss."),
        PQ("In what way does the setting at sea help to develop the theme of endurance?", "Far out at sea, Santiago is alone, with no one to help, and the water and weather test his strength. The isolation makes his struggle with the marlin and the sharks purely a test of his will, so the setting concentrates the theme of endurance."),
        SUM("Hemingway's The Old Man and the Sea (1952) follows Santiago, an old Cuban fisherman, his 84 days without a catch, the big marlin and the sharks.", "Manolin shows loyalty and the passing on of skill.", "Key themes: endurance, dignity in defeat, pride, respect for nature and friendship.", "Symbols such as the lions, the marlin and the sharks may be read in more than one way: say 'some readers see'.", "The plain style supports the themes; support every point with moments from your own copy."),
    ],
))

# ------------------------------------------------------------------ 7. Poetry: how to read and write about a poem
POEM_A = ("The Last Bus (an invented poem)\n\n"
          "The last bus leaves without a sound,\n"
          "its lamps like tired eyes.\n"
          "It takes the market's noise away\n"
          "and leaves the stars to rise.\n\n"
          "I count my coins beside the road\n"
          "and think of home, so far,\n"
          "yet every step I plan to take\n"
          "is lit by one small star.")

ANTHOLOGY = ("1  Corruption in the Country        Adebayo Oluwatobi\n"
             "2  Exploitation                     Amos Brazzoli\n"
             "3  Faceless                         Anichebe Chinenye\n"
             "4  If We Must Die                   Claude McKay\n"
             "5  Human Degration                  Daljit Khankhana\n"
             "6  Cruel Megalomaniacal Leaders     Francis Duggan\n"
             "7  Keep Peggin' Along               James Conway Jackson\n"
             "8  Deceit                           Jayme Chapin\n"
             "9  You Can't Buy Me                 John Chizoba Vincent\n"
             "10 Moral Decay of Society           Margaret Bailey\n"
             "11 How Can I Sing                   Odia Ofeimun\n"
             "12 Africa's Plea                    Roland Tombekai Dempster\n"
             "13 If                               Rudyard Kipling\n"
             "14 Just a Word                      Shiekha A. El-Miskery\n"
             "15 Power of Corruption              Surenda Deo (S. D.) Tiwari\n"
             "16 Time to Stop Struggling          Tanya\n"
             "17 Corruption                       Theophilus Katon Chidonku\n"
             "18 I Am an African                  Wayne Visser")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_POETRY,
    title="Reading and writing about a poem",
    slug="enu2-poetry-how-to-write",
    minutes=24,
    summary="A method for any poem on the Board's list: voice, subject and tone, then form, language and sound, with a worked analysis of a short invented poem, the list of anthology titles and prompts for reading poems you have not met in this course.",
    objectives=[
        "Identify the speaker, subject, audience and tone of a poem",
        "Describe form (stanza, line, rhyme, rhythm) and say what it contributes",
        "Name and explain imagery, figures of speech and sound devices",
        "Plan a comparison of two poems using the prescribed list",
    ],
    key_concepts=["Speaker", "Tone", "Imagery", "Simile and metaphor", "Rhyme and rhythm", "Stanza", "Volta (turn)", "Comparison of poems"],
    blocks=[
        H("Introduction"),
        T("Poetry says a lot in few words. A poem is not a story with the details removed. It is a small, carefully built object in which every word, line break and sound has been chosen. The Board's list for poetry is a set of poems from the anthology *Cosmic Anthology to Poetry*, edited by Vainer and Kaby. Eighteen poems are listed, and you should be able to write about any of them."),
        T(OWNCOPY),
        CODE(ANTHOLOGY, "text", title="The Board's list of poems (spelling as in the syllabus; check your anthology)"),
        T("This course explains two of these poems, 'If' by Kipling and 'If We Must Die' by Claude McKay, in the next lesson. For the other sixteen, you need to read the poem itself. The titles suggest subjects (corruption, exploitation, moral decay, identity, hope) but a title is only a hint, so read each poem and form your own judgement."),
        H("A four-part method"),
        KEY("Voice, form, language, sound", "Ask these questions of every poem. Write short answers in the margin.", cards=[
            ["Voice", "Who is speaking? To whom? About what? What is the tone: angry, sad, ironic, hopeful, calm?"],
            ["Form", "How many stanzas and lines? Is there a pattern of rhyme or a regular rhythm? Where does the poem turn?"],
            ["Language", "Which images, comparisons and key words stand out? What do they make you see or feel?"],
            ["Sound", "Which sounds repeat (rhyme, alliteration, assonance)? How do punctuation and line endings affect the pace?"],
        ]),
        D("**Tone** is the speaker's attitude to the subject and the reader, shown by word choice and rhythm. **Imagery** is language that creates pictures or sensations. A **simile** compares using 'like' or 'as'; a **metaphor** says one thing is another; **personification** gives human qualities to things. **Enjambment** is when a sentence runs on past the end of a line.", title="Terms to know"),
        T("Read this short **invented** poem (not from the list) and then see the method at work."),
        CODE(POEM_A, "text", title="Invented poem"),
        EX("Worked example 1: analysing the invented poem", intro="Write a short analysis of 'The Last Bus' using voice, form, language and sound.", steps=[
            S("Voice", text="The speaker is a person alone at a bus stop at night, counting coins and thinking of home. The tone begins as lonely and tired, and ends hopeful."),
            S("Form", text="There are two stanzas of four lines. The second and fourth lines of each stanza rhyme (eyes with rise, far with star), a pattern often called abcb. The third line of the second stanza begins with 'yet', which turns the poem from loneliness to hope."),
            S("Language", text="The simile 'like tired eyes' makes the bus lamps seem human and weary, matching the speaker's mood. The small star at the end is a symbol of hope that is modest but real."),
            S("Sound", text="Short, steady lines and simple words make the poem sound calm, like quiet thoughts at night. The rhyme of far and star links the distance of home with the light that guides the speaker."),
        ]),
        H("Writing about poetry"),
        T("Use the same Point-Evidence-Explain-Link pattern as for any text, but quote **briefly**: a word or short phrase set inside your own sentence. 'The simile in the second line makes the lamps seem tired' is better than copying a whole line. Write 'the speaker', not 'I', and 'the poet' only when you mean the real writer's choices."),
        EX("Worked example 2: planning a comparison", intro="Question (written for practice): 'Compare how two poems on your list present the idea of struggle or hardship.'", steps=[
            S("Choose two poems", text="Pick poems you know well whose subjects overlap, for example two that deal with courage or with corruption."),
            S("Find similarities", text="Note shared ideas, for example both speakers urge their readers to act, with evidence from each poem."),
            S("Find differences", text="Compare tone (angry versus calm), form (regular pattern versus free), and attitude to the future."),
            S("Structure the answer", text="Use paragraphs by theme, not by poem: Point on similarity (both poems), Point on difference, Point on form or language, then a conclusion about the poets' attitudes."),
        ]),
        MISTAKE("Paraphrasing instead of analysing", "Explaining what each line means in other words is only the first step. Examiners want you to explain why the poet chose those words and what effect they have."),
        MISTAKE("Saying 'the poet uses alliteration' and stopping", "Name the sounds, say what they sound like (hard, soft, hissing) and say how this supports the meaning."),
        MISTAKE("Forgetting that the speaker may not be the poet", "Use 'the speaker' for the voice in the poem unless you have good reason to refer to the poet's own life."),
        TIP("Exam link: poetry appears in Paper 2 Section B as an essay on a theme across several poems, or as an extract-style question on one poem. Learn at least five poems well enough to compare, including the two in the next lesson."),
        QUIZ("What is the best way to quote from a poem in an essay?", [
            "Copy the whole stanza", "Quote a few exact words inside your own sentence and explain them", "Never quote", "Paraphrase without naming the poem"], 1,
            "Brief quotations woven into your argument show that you are close to the text without wasting time.",
            hint="Think about being brief and exact.",
            feedback=["It uses up time and does not show analysis.", "", "Short quotations are expected as evidence.", "The examiner must know which poem you mean."]),
        QUIZ("'The street was a river of light.' This is", [
            "a simile", "a metaphor", "an alliteration only", "a rhyme"], 1,
            "The street is called a river directly, without like or as, so it is a metaphor.",
            hint="Look for the words like or as.",
            feedback=["A simile would use like or as.", "", "There is no repeated first sound that carries the effect.", "Rhyme needs two matching line endings."]),
        PQ("List the four headings of the method for reading a poem and give one question for each.", "Voice (who is speaking, and in what tone?), form (how many stanzas, is there a rhyme pattern, where is the turn?), language (what images and comparisons are used?), sound (what sounds and pauses shape the effect?)."),
        PQ("In the invented poem, explain the effect of 'yet' at the start of the second stanza's third line.", "'Yet' is a word of contrast. It changes the poem from the speaker's loneliness and distance from home to a hopeful decision. It marks the turn (volta) of the poem."),
        PQ("Write two sentences comparing the tone of two poems of your choice from the list. Do not describe a poem you have not read.", "A good answer names two poems, states a tone for each (for example angry, calm, sad or urgent), and supports each with a word or phrase from the poem. It then says which one is more direct and why."),
        SUM("Use four questions for every poem: voice, form, language, sound.", "Tone is the speaker's attitude; the speaker is not always the poet.", "Quote a few exact words, and explain the effect.", "For comparison, organise by ideas, not by poem.", "The Board's list has eighteen poems: read each one yourself."),
    ],
))

# ------------------------------------------------------------------ 8. 'If' and 'If We Must Die'
POEM_FACTS = ("                'If'                     'If We Must Die'\n"
              "Poet            Rudyard Kipling          Claude McKay\n"
              "Published       1910                     1919\n"
              "Form            4 stanzas of 8 lines     A sonnet: 14 lines\n"
              "Rhyme           Regular, alternate       Alternate rhymes, then\n"
              "                lines rhyme              a closing couplet\n"
              "Speaker         A calm adviser           A defiant leader\n"
              "Addressed to    A son                    Fellow sufferers (kinsmen)\n"
              "Core idea       Self-control and         Dignity and courage when\n"
              "                steadiness               facing violence")

LESSONS.append(lesson(
    module=M_TEXTS, topic=T_POETRY,
    title="Two poems studied closely: 'If' and 'If We Must Die'",
    slug="enu2-if-and-if-we-must-die",
    minutes=24,
    summary="Close study of two poems from the Board's list, Kipling's 'If' and Claude McKay's 'If We Must Die': form, voice, tone, imagery and message in our own words, and how to compare them in an essay.",
    objectives=[
        "State the poet, date, form and central idea of each poem",
        "Describe the voice and tone of each poem and how the form supports them",
        "Explain the imagery of McKay's poem and the structure of Kipling's, with brief evidence",
        "Write a comparison paragraph that uses both poems",
    ],
    key_concepts=["Conditional structure", "Advice poem", "Sonnet", "Closing couplet", "Animal imagery", "Dignity under pressure", "Comparison"],
    blocks=[
        H("Introduction"),
        T("Think of the moment when a footballer in Yaounde misses a penalty in a final, or a trader loses a day's stock in a market fire. How a person behaves in that moment says something about character. Two poems on the Board's list ask the same question in very different voices: Kipling's 'If' gives patient advice, and McKay's 'If We Must Die' gives a rallying cry."),
        T("Both poems are well known, so we can say a number of things about them with confidence. We paraphrase them and quote only single words, because your essay must use your own wording and a few exact words from your own copy."),
        T(OWNCOPY),
        CODE(POEM_FACTS, "text", title="The two poems at a glance"),
        H("'If' by Rudyard Kipling"),
        T("Kipling was a British writer born in India, and he received the Nobel Prize in Literature in 1907. 'If' was published in 1910. It is addressed to a **son**, and the speaker gives a list of qualities that a mature person should show. Each stanza is made of a chain of 'if' clauses (conditions), and the poem's final lines deliver the promise that a person who can do all this will be a true adult."),
        KEY("Reading 'If'", "Look for these features in your copy.", cards=[
            ["Structure", "A very long conditional sentence builds across the stanzas and only ends in the last two lines. The reader has to wait for the reward, which makes the final promise strong."],
            ["Balance", "The poem pairs opposites: success and failure, being doubted and trusting yourself, crowds and kings. The advice is to stay steady, without becoming proud in success or crushed by loss."],
            ["Integrity", "The speaker values honesty, patience, humility and the courage to start again after seeing a life's work destroyed."],
            ["Voice", "A calm, firm adviser who speaks to 'you'. The direct address makes the reader feel the advice is personal."],
        ]),
        EX("Worked example 1: a paragraph on structure in 'If'", intro="How does Kipling's use of repeated 'if' clauses help to communicate his message?", steps=[
            S("Point", text="Kipling uses repeated 'if' clauses to make self-control feel like a long, demanding discipline."),
            S("Evidence", text="Line after line begins with 'if' and names another test, so the reader must keep listening before reaching the conclusion."),
            S("Explain", text="The repetition has the rhythm of a teacher listing rules. Because the main promise is delayed until the end, the reader feels that the reward has to be earned."),
            S("Link", text="This structure supports the poem's message: steadiness is built slowly, one test at a time."),
        ]),
        H("'If We Must Die' by Claude McKay"),
        T("Claude McKay was born in Jamaica and became a leading writer in the United States. This sonnet was published in 1919, a year of terrible racial violence against Black Americans in several American cities. The speaker is a leader who speaks to his own people (his 'kinsmen'). The poem says that if they must die, they should not die like hunted animals in a trap but in a way that earns respect: nobly, fighting back."),
        KEY("Reading 'If We Must Die'", "Look for these features in your copy.", cards=[
            ["Form", "A sonnet of fourteen lines, with alternate rhymes and a closing rhyming couplet. The compact form matches the speaker's disciplined courage."],
            ["Animal imagery", "The speaker rejects dying like hogs or like dogs and calls the enemy a pack. The images show how dehumanising violence is and make dignity the main point."],
            ["Military language", "Words such as foe, blow and wall turn the speaker's call into a battle cry and give the poem a marching pace."],
            ["Tone", "Defiant, urgent and proud. The speaker does not plead; he commands."],
        ]),
        EX("Worked example 2: comparing the two poems", intro="Write one comparison paragraph: 'Compare how the poets present courage under pressure.'", steps=[
            S("Point", text="Both poets admire courage and dignity under pressure, but Kipling presents it as quiet self-control while McKay presents it as open resistance."),
            S("Evidence from Kipling", text="The adviser speaks calmly to a son and lists tests of patience and honesty."),
            S("Evidence from McKay", text="The speaker calls his kinsmen to face the enemy together and to strike back, using the images of hogs and dogs to show what they must not become."),
            S("Explain", text="Kipling's long conditional sentence teaches slowly, while McKay's sonnet drives forward with commands. The first poem builds private character; the second builds public courage."),
            S("Link", text="Both conclude that a person's worth lies in how they meet difficulty, not in whether they escape it."),
        ]),
        MISTAKE("Saying 'If' is only about being a man", "The poem's idea is wider: steady character, honesty and humility. Write about the qualities, and note that it addresses a son in the language of its time."),
        MISTAKE("Ignoring the historical background of the McKay poem", "A sentence about the 1919 violence helps to explain the urgency, but do not guess details. Keep to what you can state with certainty."),
        MISTAKE("Quoting long lines from memory", "Your memory of the lines may be inexact. Quote a word or two, and write the rest in your own words."),
        TIP("Exam link: these poems are on the Board's anthology list for Paper 2 Section B. They are a good pair for questions on courage, dignity, endurance or the voice of a speaker. They also pair well with The Old Man and the Sea. Check the pairing in your own copy."),
        QUIZ("Which poem is a sonnet?", [
            "'If'", "'If We Must Die'", "Both of them", "Neither of them"], 1,
            "McKay's poem has fourteen lines and a closing couplet, which is the sonnet form. Kipling's has four stanzas of eight lines.",
            hint="Count the lines of each poem in your copy.",
            feedback=["It has 32 lines in four stanzas.", "", "Only McKay's poem is a sonnet.", "McKay's poem is a sonnet."]),
        QUIZ("Which statement best describes the tone of McKay's poem?", [
            "Calm and gentle advice", "Defiant and urgent", "Light and humorous", "Confused and uncertain"], 1,
            "The speaker commands his kinsmen to resist with dignity, so the tone is defiant and urgent.",
            hint="Think of a leader rallying people.",
            feedback=["That fits Kipling's poem better.", "", "The subject is serious.", "The speaker is clear and firm."]),
        PQ("State two ways in which the voices of the two poems differ.", "Kipling's speaker is a calm adviser who speaks to a single young person (a son) in long conditional sentences. McKay's speaker is a defiant leader who speaks to a group of fellow sufferers and uses commands and strong images. One is private and patient; the other is public and urgent."),
        PQ("Explain the effect of the animal images in 'If We Must Die' without quoting more than a word or two.", "The speaker refuses to let his people die like hunted animals, such as hogs, and calls the enemy a pack. The images show the degrading treatment they face and make dignity the main issue: if they fight back, they die as human beings who matter."),
        PQ("Write a conclusion for an essay comparing the two poems.", "A possible conclusion: 'Both poets present dignity as the true test of character, but they imagine it in different ways. Kipling teaches steadiness through patient conditions, while McKay summons courage through defiance. Together they show that the way a person meets hardship may matter as much as the outcome.'"),
        SUM("'If' (1910) is Kipling's advice to a son in four stanzas of eight lines, built from repeated 'if' clauses.", "'If We Must Die' (1919) is McKay's sonnet of defiance, with animal and military imagery.", "Both admire dignity under pressure; they differ in voice, tone and form.", "Quote only a word or two; paraphrase the rest.", "Check every detail against your own copy before using it."),
    ],
))

# ------------------------------------------------------------------ 9. Short stories and sketches
STORY_A = (
    "The envelope arrived on the morning of the examination. Nkeng found it under the door, thin and white, with his name written in a hand he did not know. "
    "His heart began to race, for he had not slept, and the fees for the examination were still unpaid.\n\n"
    "He opened it with shaking fingers. Inside lay a single receipt and a note: 'Paid in full. Study well. A friend.'\n\n"
    "'Who would do this?' he whispered. He looked at the handwriting again. The loops of the letters seemed familiar, but he could not place them.\n\n"
    "There was no time to wonder. He grabbed his pen and ran, past the bakery, past the chapel, across the muddy field where the school bus had once stuck in the rain. "
    "At the gate, the supervisor checked his name and smiled. 'You are on the list,' she said.\n\n"
    "For three hours, Nkeng wrote with a steady hand. When the bell rang, he felt tired but light, as though a stone had rolled off his back.\n\n"
    "That evening, he walked to Mama Ruth's shop, where she sold soap and sugar by the roadside. She was tying a small bundle of notes in a cloth. "
    "On the counter lay a pen with a loop he recognised.\n\n"
    "'Mama,' he said softly.\n\n"
    "She did not look up. 'Eat first,' she said. 'Then we can talk about the results.'"
)

SKETCH_A = (
    "At six in the morning, the Mile Four motor park is already awake. Drivers stretch beside their buses, calling the names of towns as if they were songs: "
    "'Bamenda, Bamenda, one seat!' The smell of roasting corn drifts over the diesel, and a boy weaves between the wheels with a tray of boiled eggs balanced on his head.\n\n"
    "Near the ticket kiosk sits Pa Lukong, the oldest porter in the park. His shoulders are bent like an old bridge, but his hands are quick. "
    "He lifts a traveller's bag, tests its weight with a grunt, and ties it to the roof with one smooth loop of rope.\n\n"
    "'Too many things,' he says to the owner, smiling. 'But heavy bags mean people are going home.'\n\n"
    "Beside the kiosk, a woman in a bright wrapper argues over the price of a sack of plantains, waving her hand like a flag, until the seller laughs and lowers it by a hundred francs.\n\n"
    "By seven, the buses begin to leave, one after another, horns blaring. The crowd thins. Pa Lukong counts his small coins, folds them into a cloth and tucks the cloth into his belt. "
    "Then he sits down on an upturned crate, closes his eyes and waits for the next bus to arrive."
)

OPENING_B = ("The generator died just as the first guests arrived at the wedding. For a moment, nobody spoke. "
             "Then, from the back of the hall, a small voice began to sing.")

LESSONS.append(lesson(
    module=M_CREATE, topic=T_STORY,
    title="Writing short stories and sketches in 200 to 250 words",
    slug="enu2-short-stories-sketches",
    minutes=24,
    summary="How to write a complete short story or a descriptive sketch of 200 to 250 words: one incident, a clear shape, a strong opening and ending, correct dialogue and one tense, with two original models and a word-count method.",
    objectives=[
        "Tell a short story and a sketch apart and choose the right shape for each",
        "Plan a story with five beats inside the 200 to 250 word limit",
        "Write an opening, an ending and correctly punctuated dialogue",
        "Check the word count and the tense before handing in",
    ],
    key_concepts=["Short story", "Sketch", "Word limit", "Opening and ending", "Dialogue", "Show, don't tell", "Tense consistency"],
    blocks=[
        H("Introduction"),
        T("Paper 2 Section C offers two creative writing questions, and you write **one** in 200 to 250 words. The syllabus says candidates should be able to produce sketches, poems, short stories and plays, and to imagine the beginning or the ending of a story. In 200 to 250 words there is no room for a long journey. A short story has space for **one** event and one or two characters."),
        T("The Board also reminds candidates to use the name and address provided to conceal their identity, to suit style and point of view to the reader and the kind of writing, and never to use obscene language."),
        D("A **short story** tells one incident with a beginning, a middle and an end, and usually a change in a character. A **sketch** is a short descriptive piece that shows a person, a place or a moment, with little or no plot.", title="Definitions"),
        H("The five beats of a very short story"),
        KEY("Plan before you write", "Use roughly these word counts for a 230-word story.", cards=[
            ["1. Opening (20-30 words)", "Start inside the action: a place, a person and a hint of trouble. Skip long introductions."],
            ["2. Situation (40-50 words)", "What does the character want or fear? Give one or two concrete details."],
            ["3. Complication (70-80 words)", "Something goes wrong or surprises the character. Show it through action and dialogue."],
            ["4. Turning point (40-50 words)", "The character makes a choice or learns something."],
            ["5. Ending (30-40 words)", "Close with an image, a quiet line of dialogue or a twist that echoes the opening."],
        ]),
        T("Read the original story below and notice how it follows the beats."),
        T(STORY_A, title="Model story: 'The Envelope' (invented)"),
        EX("Worked example 1: the beats in the model", intro="Mark the five beats in 'The Envelope'.", steps=[
            S("Opening", text="The first sentence gives the time and the object: an envelope on the morning of an examination. It starts the problem at once."),
            S("Situation", text="Nkeng is anxious and the fees are unpaid, so we know what he wants."),
            S("Complication", text="The receipt and the unknown friend create a mystery. He has little time, so he runs."),
            S("Turning point", text="He writes the examination with a steady hand. The anxiety is gone."),
            S("Ending", text="The pen with the familiar loop reveals who helped him, and Mama Ruth's quiet reply shows love without long speeches. The ending answers the mystery without explaining it."),
        ]),
        H("Writing a sketch"),
        T("A sketch needs no plot, but it needs a **focus**: one person, place or moment. Use the five senses, strong verbs, and small details that suggest a larger picture. Include one simple comparison, and end with an image rather than a lesson. Read the original sketch below."),
        T(SKETCH_A, title="Model sketch: 'The Motor Park at Dawn' (invented)"),
        EX("Worked example 2: what makes the sketch work", intro="Identify three techniques in 'The Motor Park at Dawn'.", steps=[
            S("Sensory detail", text="Roasting corn and diesel (smell), calling drivers (sound) and the boy with eggs (sight) put the reader in the scene."),
            S("Simile", text="Shoulders are bent 'like an old bridge', a comparison that shows age and strength together."),
            S("Focus and ending", text="The sketch centres on Pa Lukong. The final image of him waiting, with his eyes closed, suggests patience and a life of work without a speech."),
        ]),
        H("Openings, endings and dialogue"),
        T("Some questions give you a beginning or an ending and ask you to imagine the rest. Always **use the given words exactly** and continue from them. If you are given an opening, plan an ending that connects to it. If you are given an ending, start with a situation that leads to it."),
        T("Punctuate dialogue correctly: put the speaker's exact words in quotation marks, begin a new line for each new speaker, put punctuation inside the marks, and use a capital letter for the first word of the speech. Keep the tense of the narration consistent; if the story is in the past tense, everything outside speech stays in the past."),
        H("Counting words"),
        T("Count every word, including small words such as *a* and *the*. A hyphenated word usually counts as one word and a number written in digits counts as one. Methods differ, so ask your teacher how to count, and aim for **215 to 240** words so that you are safe either way. Count one full line of your handwriting, then multiply by the number of lines, and check the total against the limit."),
        MISTAKE("Starting too early", "Beginning with the character waking up and brushing teeth wastes forty words. Start where the trouble starts."),
        MISTAKE("Trying to tell a whole life", "A weekend story does not fit in 250 words. Choose one event and one turning point."),
        MISTAKE("Going over or under the limit", "Under 200 words, you may not have developed the idea; over 250, you waste time and may lose marks. Count before you copy out."),
        TIP("Exam link: Paper 2 Section C, creative writing (one of two questions, 200 to 250 words). Keep five minutes at the end to check the word count, the spelling and the tense."),
        QUIZ("A question gives you the first sentence of a story. What should you do?", [
            "Change the sentence slightly to suit your idea", "Use the given sentence exactly and continue from it", "Ignore it and write your own story", "Write only one more sentence"], 1,
            "The given words must be used, because the examiners test whether you can continue a story.",
            hint="The question has given you the words.",
            feedback=["Changing the sentence may mean you have not answered the question.", "", "That would not answer the question.", "The task needs a full story of 200 to 250 words."]),
        QUIZ("Which is correctly punctuated dialogue?", [
            "\"Where are you going\" she asked.", "'Where are you going?' she asked.", "'Where are you going.' She asked.", "Where are you going? she asked."], 1,
            "A question mark goes inside the closing quotation mark, and 'she asked' continues with a lower-case letter.",
            hint="Look at the question mark and the next word.",
            feedback=["The question mark is missing inside the marks.", "", "A full stop after a question and a capital for 'She' are wrong.", "Quotation marks are missing."]),
        PQ(f"Plan a story that begins: {OPENING_B!r} Give a one-line note for each of the five beats.", "A possible plan: 1. Opening: the generator dies at the wedding; silence. 2. Situation: the families are nervous because the guests have come from far. 3. Complication: no music, no light, and the bride's father is embarrassed. 4. Turning point: the child sings; guests join and the sound fills the hall. 5. Ending: the lights return, but nobody notices until the song ends. Other plans are fine if they use the given sentences and follow the five beats."),
        PQ("Write the first two sentences of a sketch of a school canteen at lunchtime, using at least two senses.", "A possible answer: 'The canteen smells of hot rice and woodsmoke, and the clatter of plates rises to the roof. A line of students in green uniforms leans forward, each waiting for the cook's ladle.' It uses smell, sound and sight."),
        PQ("A student's story is 180 words. Name two ways to lengthen it to the required range without adding unneeded details.", "Add a sentence of concrete detail to the situation or complication (what the character sees or feels), and expand the turning point with a line of dialogue or a short reaction. Do not add long explanations or a new character."),
        SUM("Write one incident, one or two characters and five beats in 200 to 250 words.", "A sketch needs a focus, sensory detail and an ending image, not a plot.", "Use given openings or endings exactly.", "Punctuate dialogue correctly and keep one tense.", "Count words and aim for 215 to 240."),
    ],
))

# ------------------------------------------------------------------ 10. Poems and plays
POEM_B = ("Before the Market Wakes (invented)\n\n"
          "Before the cocks have found their song,\n"
          "before the sun is high,\n"
          "my mother ties her wrapper tight\n"
          "and watches the grey sky.\n\n"
          "She lifts the basket to her head,\n"
          "a hill of yams and greens,\n"
          "and walks the red road, step by step,\n"
          "past fields of maize and beans.\n\n"
          "The trucks go by and fill the air\n"
          "with dust and horns and noise,\n"
          "but she walks on, her shoulders straight,\n"
          "with quiet, steady poise.\n\n"
          "At market, in her little space,\n"
          "she spreads a faded sheet\n"
          "and lines the yams in tidy rows\n"
          "to make the stall look neat.\n\n"
          "The buyers come and bargain hard;\n"
          "she laughs, then shakes her head,\n"
          "for every coin she earns today\n"
          "will pay for books and bread.\n\n"
          "At noon the sun beats on the roofs,\n"
          "the dust clings to her feet,\n"
          "yet still she calls her friendly words\n"
          "to everyone she meets.\n\n"
          "At dusk she counts the day's small coins\n"
          "and ties them in a cloth,\n"
          "then hums a song beneath her breath\n"
          "that flutters like a moth.\n\n"
          "I watch her walk back down the road,\n"
          "her basket light at last,\n"
          "and wonder how her tired arms\n"
          "have held our house so fast.\n\n"
          "One day I'll build her a wide stall\n"
          "beneath a tin roof high,\n"
          "and she will sit and rest her feet\n"
          "and watch the traders by.\n\n"
          "Until that day I'll study hard\n"
          "by lamplight in the night,\n"
          "for every page I turn is hers,\n"
          "and every line I write.")

PLAY_A = ("THE LAST MANGO (invented)\n\n"
          "Characters: ABENA, a young market seller; MR TABI, a customer.\n"
          "Setting: A market stall at midday. One mango sits on a plate.\n\n"
          "(ABENA straightens the plate. MR TABI approaches, fanning himself.)\n\n"
          "TABI: Good afternoon. How much for the mango?\n"
          "ABENA: It is not for sale, sir.\n"
          "TABI: (surprised) A seller who will not sell?\n"
          "ABENA: It is the last one from my grandmother's tree. (She touches it gently.)\n"
          "TABI: (smiling) Then why is it on the table?\n"
          "ABENA: So that everyone can see what the tree gave us.\n"
          "TABI: Mangoes bruise easily, you know. Someone will knock it over.\n"
          "ABENA: (firmly) Then I will sit beside it all day.\n"
          "TABI: For how many days?\n"
          "ABENA: For as long as it stays sweet. My grandmother always said that a good fruit should be admired before it is eaten.\n"
          "TABI: (laughing softly) Your grandmother sounds like a wise woman.\n"
          "TABI: (after a pause) I once had a tree like that. The storm took it, and I did not see it fall.\n"
          "(Silence. ABENA lifts the mango and holds it out.)\n"
          "ABENA: Take it, sir.\n"
          "TABI: But you said...\n"
          "ABENA: (gently) I said it was not for sale. I did not say it was not for sharing.\n"
          "TABI: (taking it) Then let us cut it. Half for you, half for me.\n"
          "(They smile. The lights fade slowly.)")

LESSONS.append(lesson(
    module=M_CREATE, topic=T_POEMPLAY,
    title="Writing poems and short plays",
    slug="enu2-poems-and-plays",
    minutes=24,
    summary="How to write a poem and a short play that fit a word limit of 200 to 250 words: choosing a form, building images and sound, laying out a play script correctly, and checking length, with an original poem and an original scene.",
    objectives=[
        "Plan a poem with a clear subject, speaker, form, images and ending",
        "Use rhyme, rhythm and imagery on purpose",
        "Lay out a play script correctly, with cast, setting, speakers and stage directions",
        "Decide how to count words in each form and keep to the limit",
    ],
    key_concepts=["Quatrain", "Rhyme scheme", "Imagery", "Play script layout", "Stage direction", "Subtext", "Word limit"],
    blocks=[
        H("Introduction"),
        T("The syllabus asks candidates to produce poems and plays as well as stories and sketches. Tasks may read, for example, 'Write a poem about a person who has taught you something' or 'Write the scene of a play in which two people disagree about a gift'. The word limit of 200 to 250 words applies to every form, so the work has to be compact."),
        H("Writing a poem"),
        KEY("Four decisions", "Make these before writing the first line.", cards=[
            ["Subject and speaker", "Choose one subject you know well. Decide who is speaking: you, a child, a parent, an object."],
            ["Form", "Quatrains (four-line stanzas) with a pattern such as ABCB or AABB are easiest to control. Free verse is allowed, but it still needs clear images and a firm shape."],
            ["Images", "Pick three concrete images from the five senses. A single strong picture is better than five weak ones."],
            ["Ending", "End with a turn, a promise or an image that completes the thought."],
        ]),
        T("A poem of 200 to 250 words is long: about ten quatrains. Count your words by stanzas. If a stanza has about 22 words, ten stanzas give about 220. Plan the number of stanzas before writing so that you do not run out of time."),
        T(POEM_B, title="Model poem (invented)"),
        EX("Worked example 1: what makes the poem work", intro="Identify the form, the images and the ending of 'Before the Market Wakes'.", steps=[
            S("Form", text="Ten quatrains (248 words). The second and fourth lines of each rhyme (high/sky, greens/beans, noise/poise). The rhythm is steady, like footsteps on a road."),
            S("Images", text="The basket as a 'hill of yams and greens' (metaphor), the song that flutters 'like a moth' (simile), and the sun beating on the roofs (personification-like action)."),
            S("Voice and journey", text="The speaker, a child, follows the mother through the day from dawn to dusk. The day gives the poem its structure."),
            S("Ending", text="The final stanza turns from observation to promise: the child will study in honour of the mother, which gives the poem a purpose."),
        ]),
        H("Writing a short play"),
        T("A play is made of dialogue and stage directions. In a scene of 200 to 250 words you can have two or three characters and one clear conflict, and you must show the conflict through speech and action. Use **subtext**, meaning feelings that characters do not state but that the audience understands."),
        D("**Script layout:** a title; a list of characters with a few words about each; a line for the setting; each speech begins with the speaker's name followed by a colon; stage directions go in brackets and in the present tense; there are no quotation marks around speech.", title="Layout rules"),
        T(PLAY_A, title="Model play scene (invented)"),
        EX("Worked example 2: how the scene works", intro="Explain how the scene shows a change in feeling without a long speech.", steps=[
            S("Opening conflict", text="Abena refuses to sell. The customer is surprised, so the audience asks why."),
            S("Revealed through dialogue", text="Abena explains the mango's meaning in one line. Tabi answers with a short, painful memory of his own tree."),
            S("Stage directions carry feeling", text="'Silence' and the gesture of holding out the mango show her decision before she says it."),
            S("Resolution", text="The final line, about sharing, solves the opening problem with kindness. The lights fade, which gives a clear ending."),
        ]),
        H("Counting words"),
        T("The Board says candidates write 200 to 250 words. For a play, ask your teacher whether speakers' names and stage directions count. To be safe, make sure your total including names is **at most 250** and that your words **without the speakers' names** are still at least 200. The model scene is written to satisfy both ways of counting. For a poem, count every word in every line, not including the title unless your teacher says to."),
        MISTAKE("Rhyming at any cost", "Do not make a sentence odd just to find a rhyme. A near-rhyme or an unrhymed line is better than nonsense."),
        MISTAKE("Using quotation marks in a play", "A script marks speech with the speaker's name and a colon. Quotation marks belong to stories."),
        MISTAKE("Writing a speech instead of a scene", "A play needs conflict and movement between at least two characters. One long speech is not a scene."),
        TIP("Exam link: Paper 2 Section C, creative writing. If you choose a poem or a play, spend five minutes planning (stanzas or beats), and keep two minutes to count words."),
        QUIZ("Which line is correctly laid out in a play script?", [
            "'Good morning,' said Abena.", "ABENA: (smiling) Good morning.", "Abena says, \"Good morning.\"", "Good morning (Abena)"], 1,
            "A script uses the speaker's name, a colon, a bracketed direction and the speech with no quotation marks.",
            hint="Look for the name followed by a colon.",
            feedback=["That is story style.", "", "That is story style with a verb of saying.", "The speaker should come first with a colon."]),
        QUIZ("A poem has ten quatrains with about 22 words in each. What is the approximate word count?", [
            "100", "150", "220", "300"], 2,
            "10 x 22 = 220, which is within the 200 to 250 limit.",
            hint="Multiply the number of stanzas by the words in each.",
            feedback=["That would be too short.", "Still too short for the limit.", "", "That would go over the limit."]),
        PQ("Write a first stanza (four lines, ABCB) for a poem about a school bell.", "A possible answer: The bell begins to ring at eight / and shakes the morning air; / it calls the sleepy children in / from every corner stair. Lines 2 and 4 rhyme (air and stair), which is the ABCB pattern."),
        PQ("Write two lines of dialogue with a bracketed stage direction for a scene in which a student refuses to lend a pen.", "A possible answer: 'KWEDI: (holding the pen behind her back) It is the only one I have. / SAMA: (quietly) Then we will both fail.' The direction shows her protectiveness and the second line shows the conflict."),
        PQ("Explain what subtext is and give a brief example.", "Subtext is the meaning beneath the words: feelings the characters do not say but the audience understands. For example, a man says 'I am fine' while he looks at the door and does not sit down. The audience senses he wishes to leave or is worried."),
        SUM("A poem needs a subject, a speaker, a form, three strong images and a turning ending.", "Ten quatrains of about 22 words give about 220 words.", "A play script has a title, cast, setting, speaker names with colons and bracketed directions.", "Subtext lets feeling show without long speeches.", "Count so that your work is within 200 to 250 words by any sensible method."),
    ],
))

# ------------------------------------------------------------------ 11. Reports of meetings and news reports
MEET_A = (
    "Report of the Monthly Meeting of the Parents' Association, Government Secondary School, Fontem\n\n"
    "A meeting of the Parents' Association of Government Secondary School, Fontem, was held in the school hall on Saturday, 14 March, at 10 a.m. "
    "Mr Ayuk Tabe, the chairman, presided. Twenty-six members attended and three sent apologies.\n\n"
    "The secretary, Mrs Neba, read the minutes of the last meeting, and they were adopted without change.\n\n"
    "The principal reported that the new classroom block had been roofed. However, he said that the windows and doors were still missing and that the school lacked the funds to buy them. "
    "He added that the contractor had promised to finish the walls by April. The chairman asked members to suggest ways of raising money.\n\n"
    "Several members spoke. Mrs Fon proposed a fund-raising dance, but Mr Che objected that the date was too close to the examinations. "
    "After a long discussion, members agreed that each family would contribute 2,000 francs and that a committee of five would collect the money and report back.\n\n"
    "Under any other business, a parent complained about the muddy path to the school. The chairman promised to ask the council for help.\n\n"
    "The meeting ended at 12:15 p.m. The next meeting was fixed for 11 April.\n\n"
    "Signed: Mrs Neba, Secretary"
)

NEWS_A = (
    "FLOOD CLOSES MARKET ROAD IN LIMBE\n\n"
    "By Staff Reporter, Limbe, 3 June\n\n"
    "A sudden downpour on Tuesday night flooded the main market road in Limbe, forcing traders to abandon their stalls and leaving dozens of families without goods worth thousands of francs.\n\n"
    "Residents said that the water began to rise at about 9 p.m. and reached knee height within an hour. 'We saved only what we could carry,' said Mrs Ekema, who sells vegetables near the bridge. Several traders said that the same drain had flooded their stalls last year, and they asked the council to repair it properly this time.\n\n"
    "The mayor, Mr Ndive, visited the site yesterday morning. He told reporters that a blocked drain near the bus stop was the main cause. "
    "He promised that council workers would clear the drain within a week and that traders would be told when it was safe to return.\n\n"
    "Meanwhile, a local youth group has offered to help the traders carry their remaining goods to higher ground. The group's leader said that about thirty volunteers were ready to work.\n\n"
    "The police have asked drivers to avoid the area until further notice. The council will also hold a meeting with traders on Friday to discuss help for those who lost goods."
)

LESSONS.append(lesson(
    module=M_CREATE, topic=T_REPORT,
    title="Writing reports of meetings and news reports",
    slug="enu2-meeting-and-news-reports",
    minutes=24,
    summary="How to write a report of a meeting and a news report in 200 to 250 words: layout, past tense and reported speech, order of information, headline and lead, with two original models and the slips that lose marks.",
    objectives=[
        "Write a report of a meeting with the correct heading, order, tense and sign-off",
        "Write a news report with a headline, byline, strong first paragraph and inverted pyramid order",
        "Use reported speech and a few direct quotations correctly",
        "Keep each report within 200 to 250 words",
    ],
    key_concepts=["Report of a meeting", "Agenda items", "Resolutions", "Headline and byline", "Lead paragraph", "Inverted pyramid", "Reported speech"],
    blocks=[
        H("Introduction"),
        T("The syllabus says candidates should be able to report on the proceedings of meetings, seminars, workshops and conferences, and to write news reports. In daily life this is a useful skill: the secretary of a village development association, a school press club reporter and a church committee member all do it. In the examination you do it in 200 to 250 words."),
        T("Both kinds of report are **factual** and **formal**. They are written in the third person and mostly in the past tense (a meeting report) or in the past and present perfect (a news report). Leave out your opinions unless the task asks for them. Use invented names only, and the identity details the question provides, never your own."),
        H("A report of a meeting"),
        KEY("Parts and order", "Follow this order.", cards=[
            ["1. Opening", "What meeting, where, when, who presided, how many attended, who sent apologies."],
            ["2. Minutes and matters arising", "A line on the previous minutes if the question mentions them."],
            ["3. Main items", "One short paragraph for each item: who raised it, what was said (in reported speech) and what was decided."],
            ["4. Any other business", "Small items raised at the end."],
            ["5. Closing", "Time the meeting ended, date of the next meeting and the writer's name and title."],
        ]),
        T(MEET_A, title="Model: report of a meeting (invented, about 210 words)"),
        EX("Worked example 1: studying the meeting report", intro="Note three features that make the model a good report.", steps=[
            S("Order", text="It follows the order of the meeting: opening, minutes, the principal's report, discussion, other business, closing."),
            S("Tense and voice", text="Everything is in the past tense and the third person. Speeches are reported ('the principal reported that...') rather than quoted."),
            S("Decisions are clear", text="The paragraph on the funds names the decision (2,000 francs per family), who will collect it and what happens next."),
        ]),
        H("A news report"),
        D("A **news report** gives the facts of a recent event for the public. The first paragraph (the **lead**) answers who, what, where and when; later paragraphs give how and why, then less important details. This order is called the **inverted pyramid** because the most important facts come first.", title="Definition"),
        T("Give your report a **headline** (short, in the present tense or with the verb omitted) and a **byline** such as 'By Staff Reporter'. Use quotations sparingly, and always say who spoke. Do not include your opinions."),
        T(NEWS_A, title="Model: news report 'Flood Closes Market Road in Limbe' (invented, about 210 words)"),
        EX("Worked example 2: the lead and the pyramid", intro="Check that the lead paragraph of the news report contains the key facts.", steps=[
            S("Who", text="Traders and families in the market area."),
            S("What", text="A sudden downpour flooded the main market road."),
            S("Where and when", text="Limbe, on Tuesday night."),
            S("What follows", text="Residents' account, then the mayor's explanation and promise, then the volunteers and the police notice. Each later paragraph is less urgent than the one before."),
        ]),
        H("Reported speech in reports"),
        T("Reports mostly use reported speech, so the tenses move one step back: 'We will collect the money' becomes 'the chairman said that they would collect the money'. Use reporting verbs such as *said*, *explained*, *proposed*, *objected*, *promised* and *agreed*, and vary them. In a news report a short direct quotation adds life, but use only one or two."),
        MISTAKE("Writing minutes in note form when a report is asked for", "A report is written in connected paragraphs. Do not use bullet points or one-line notes unless the question asks for minutes."),
        MISTAKE("Mixing tenses", "A meeting report is in the past tense from start to finish. Check every verb before handing in."),
        MISTAKE("Burying the main fact", "If the flood or the decision is in the last paragraph, the report is badly built. Put the key fact first."),
        TIP("Exam link: Paper 2 Section C, creative writing, includes tasks on reports of meetings and news reports (200 to 250 words). Practise with a real event from your school or quarter, using invented names. Reports of meetings and minutes also appear in the editing and reconstruction work of Paper 3."),
        QUIZ("Which sentence is in correct reported speech?", [
            "The chairman said, 'We will meet again.'", "The chairman said that they will meet again next week.", "The chairman said that they would meet again the following week.", "The chairman said that they are meeting again."], 2,
            "In reported speech 'will' becomes 'would' and 'next week' becomes 'the following week' when the report is in the past.",
            hint="Move the tense one step back.",
            feedback=["That is direct speech.", "The tense and time expression have not been changed.", "", "The tense has not been moved back."]),
        QUIZ("In a news report, which should come first?", [
            "Background history", "The most important facts: who, what, where, when", "The reporter's opinion", "A list of names"], 1,
            "The inverted pyramid puts the key facts first.",
            hint="Think of the lead.",
            feedback=["Background comes later.", "", "Opinions do not belong in news reports.", "Names support the facts but do not lead."]),
        PQ("Write the lead paragraph for a news report about a school opening a new library (invented details).", "A possible answer: 'Government Bilingual High School, Ekona, opened a new library on Monday, giving its 800 students their first reading room in thirty years. The headmistress, Mrs Mbella, cut the ribbon before parents, teachers and council officials.' It answers who, what, where and when in the first paragraph."),
        PQ("Turn this into reported speech: 'We shall plant fifty trees on Saturday,' said the club president.", "The club president said that they would plant fifty trees on the following Saturday (or: on Saturday). Shall changes to would."),
        PQ("List the parts of a report of a meeting, in order.", "Opening (meeting, place, date, time, chair, attendance, apologies); minutes of the previous meeting; main items with discussion and decisions; any other business; closing (time ended, next meeting, writer's name and title)."),
        SUM("A meeting report follows the order of the meeting, in the past tense and the third person.", "A news report has a headline, byline and a lead that answers who, what, where and when.", "Put the most important facts first and the details after.", "Use reported speech, with one or two short quotations in news reports.", "Keep to 200 to 250 words and use invented names."),
    ],
))

# ------------------------------------------------------------------ 12. Paper 1 strategy
LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1: the multiple-choice paper and how to manage it",
    slug="enx2-paper-1-strategy",
    minutes=20,
    summary="The structure of the 50-question multiple-choice paper (reading, speech work, grammar, vocabulary), the time the Board gives to each section, and a method for choosing answers and managing time.",
    objectives=[
        "State the four sections of Paper 1, their number of questions and their timings",
        "Use a time plan that leaves a few minutes for checking",
        "Apply elimination and context checking to multiple-choice questions",
        "Avoid the common slips on speech work, grammar and vocabulary items",
    ],
    key_concepts=["Paper 1 structure", "Time per section", "Elimination", "Reading the stem", "Checking"],
    blocks=[
        H("Introduction"),
        T("Paper 1 is the only paper marked by machine. It has **50 multiple-choice questions** to answer in **1 hour 30 minutes**, and each question carries one mark. Because the marking is automatic, clear shading matters as much as the right idea. Follow the instructions on your answer sheet exactly."),
        H("The structure"),
        CODE("Section A  Reading comprehension   10 questions   35 minutes\nSection B  Speech work             10 questions   15 minutes\nSection C  Grammar                 20 questions   25 minutes\nSection D  Vocabulary              10 questions   15 minutes\nTotal                              50 questions   90 minutes", "text", title="Paper 1 (from the Board's syllabus)"),
        T("The times above are the Board's guide for each section and they add up to the full 90 minutes. Reading takes longest because you must read passages. Grammar has the most questions, so you must be quick and accurate."),
        KEY("A method for every question", "Use these steps on all sections.", cards=[
            ["1. Read the stem", "Read the question or the sentence with its gap before you look at the options."],
            ["2. Predict", "Decide what the answer should be, then look for it."],
            ["3. Eliminate", "Cross out options that are clearly wrong. Often two go quickly."],
            ["4. Check in context", "Put your choice back in the sentence or passage and read it aloud in your head."],
        ]),
        H("Section by section"),
        T("**Reading comprehension.** Skim the questions first, then read the passage once for the main idea and again for details. Base every answer on the text, not on what you know. Words such as *not*, *except* and *best* change the task."),
        T("**Speech work.** Check the symbol or the word carefully. For stress, say the word quietly and tap the beat. For intonation, say the sentence naturally. Remember that this course teaches sounds by description, so practise with a dictionary that has audio and with confident speakers."),
        T("**Grammar.** Find the grammar point first: tense, agreement, reported speech, modals, clauses, punctuation. Then test each option. Grammar has 20 questions, so do not spend more than a minute on any one."),
        T("**Vocabulary.** Read the whole sentence. Think of the meaning the sentence needs, then match it. Watch for words that look alike (affect/effect, principal/principle) and for idioms whose meaning is not literal."),
        EX("Worked example 1: a time plan", intro="Plan the 90 minutes with a five-minute check at the end.", steps=[
            S("Allocate by section", text="A 33 minutes, B 14 minutes, C 24 minutes, D 14 minutes. That is 85 minutes."),
            S("Add the check", text="The last 5 minutes are for the answer sheet: make sure every question has exactly one shaded answer."),
            S("Mark and skip", text="If a question takes more than a minute, mark it with a light dot in the question paper, choose your best guess, and return if time allows."),
        ]),
        EX("Worked example 2: elimination", intro="'Neither of the two answers ___ correct.' Options: A. are, B. were, C. is, D. be.", steps=[
            S("Find the grammar point", text="Subject-verb agreement. 'Neither' is the subject, and it takes a singular verb."),
            S("Eliminate", text="'Are' and 'were' are plural, so they go. 'Be' is not a finite form that can follow this subject."),
            S("Check in context", text="'Neither of the two answers is correct' reads well, so the answer is C."),
        ]),
        MISTAKE("Answering from memory of the passage", "Go back to the lines in the passage. The first answer that comes to mind is often a detail from a different paragraph."),
        MISTAKE("Shading two options or skipping a number", "A machine cannot read two shaded options. If you skip a question, shade the next answer in the right place."),
        MISTAKE("Spending too long on one question", "One difficult question costs the time of three easy ones. Move on and come back."),
        TIP("Exam link: Paper 1 is made up of Reading comprehension, Speech work, Grammar and Vocabulary, each question worth one mark. Practise with timed sections: 35, 15, 25 and 15 minutes."),
        QUIZ("How many questions are in Section C (Grammar)?", ["10", "20", "30", "50"], 1,
             "Grammar has 20 questions, the largest section.", hint="It is the biggest section.",
             feedback=["That is the size of reading, speech work and vocabulary.", "", "There are 50 in the whole paper.", "That is the total for the paper."]),
        QUIZ("Which is the best first step for a multiple-choice question?", ["Read all four options and pick the longest", "Read the stem and predict the answer", "Shade A for every unknown question", "Skip every question with a long stem"], 1,
             "Predicting before looking at options protects you from attractive wrong answers.", hint="Think before you look at the options.",
             feedback=["The longest option is not always right.", "", "Guessing the same letter is not a method.", "Skipping long stems loses easy marks."]),
        PQ("List the four sections of Paper 1 with the number of questions in each.", "Reading comprehension 10, Speech work 10, Grammar 20, Vocabulary 10: 50 in all."),
        PQ("You have 6 minutes left and 5 unanswered questions. What should you do?", "Answer every remaining question, using elimination for the best guess, and then use the last minute to check that every question has one shaded answer."),
        PQ("Explain how to deal with a question that contains the word NOT.", "Underline the word NOT, then decide for each option whether it is true or false. The correct answer is the one that is false or not mentioned, so read each option against the passage or rule before choosing."),
        SUM("Paper 1 has 50 multiple-choice questions in 1 hour 30 minutes, worth one mark each.", "Sections: Reading 10, Speech work 10, Grammar 20, Vocabulary 10.", "Predict the answer, eliminate wrong options and check in context.", "Watch for NOT, EXCEPT and BEST in stems.", "Keep time for a final check of the answer sheet."),
    ],
))

# ------------------------------------------------------------------ 13. Paper 2 strategy
LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2: composition, prescribed texts and creative writing",
    slug="enx2-paper-2-strategy",
    minutes=22,
    summary="How to manage the 2 hours 15 minute writing paper: three sections of 20 marks each, a time plan, the word limits, planning, hiding your identity and checking your work.",
    objectives=[
        "State the three sections of Paper 2, the choices and the marks",
        "Plan 135 minutes across the three sections",
        "Meet the word requirements and writing conventions for each section",
        "Check each answer for relevance, accuracy and word count",
    ],
    key_concepts=["Paper 2 structure", "Time plan", "Word limits", "Identity concealment", "Planning", "Checking"],
    blocks=[
        H("Introduction"),
        T("Paper 2 lasts **2 hours 15 minutes** (135 minutes) and has three sections, each worth 20 marks. Because each section is answered in about 45 minutes, the paper is a test of planning and control as much as of writing. Candidates who run out of time in the last section lose marks they could have won."),
        CODE("Section A  Composition        6 topics, write ONE     20 marks\n           (content and organisation 10, expression 8, accuracy 2)\nSection B  Prescribed texts   4 questions, answer ONE 20 marks\n           (essay and extract questions)\nSection C  Creative writing   2 questions, answer ONE 20 marks\n           (200 to 250 words)", "text", title="Paper 2 (from the Board's syllabus)"),
        IMG("al-enu2-paper2-time.svg", alt="A bar of 135 minutes divided into three equal sections of 45 minutes: Composition, Prescribed texts and Creative writing.", caption="Figure 1. A suggested time plan: about 45 minutes for each section."),
        H("Section A: Composition"),
        T("You choose one of six topics (narrative, descriptive, expository or discursive, argumentative, open-ended or a visual stimulus). The composition should be at least 500 words. Marks are for content and organisation, expression and accuracy. The Board's report notes that some candidates described the pictures instead of being inspired by them when they chose the visual topic. Plan the type of writing, the reader and the point of view before you begin."),
        H("Section B: Prescribed texts"),
        T("You answer one of four essay or extract questions in about 45 minutes. Use only the five prescribed texts and the anthology poems, cite titles and authors correctly, and answer the question that is asked. Use the Point-Evidence-Explain-Link method."),
        H("Section C: Creative writing"),
        T("You answer one of two questions in 200 to 250 words: a story, sketch, poem, play, meeting report or news report. Count your words. The Board also reminds candidates to use the name and address provided to hide their identity, to suit style and point of view to the reader and the type of writing, and not to use obscene language."),
        EX("Worked example 1: a 135-minute plan", intro="Plan the paper so that each section gets equal time and a check.", steps=[
            S("Section A: 45 minutes", text="5 minutes to choose and plan, 35 minutes to write 500 or more words, 5 minutes to check."),
            S("Section B: 45 minutes", text="5 minutes to plan, 35 minutes to write, 5 minutes to check."),
            S("Section C: 45 minutes", text="5 minutes to plan, 30 minutes to write 200 to 250 words, 5 minutes to count, 5 minutes to check."),
            S("Order", text="You may do the sections in a different order, but note the time at which you start each and keep to it."),
        ]),
        EX("Worked example 2: choosing a question", intro="You have a minute to choose among the four prescribed-text questions. How do you decide?", steps=[
            S("Scan each question", text="Mark the command word, the focus and the number of texts."),
            S("Test yourself", text="Can you name two or three moments from your own texts for each point? If not, the question is too risky."),
            S("Choose", text="Pick the question for which you have the clearest evidence, even if another looks more interesting."),
        ]),
        MISTAKE("Spending 70 minutes on the composition", "The composition is only one of three equal sections. Keep to your time plan."),
        MISTAKE("Writing your real name or address", "Use only the name and address given in the question. Writing your own identity can disqualify the work."),
        MISTAKE("Ignoring the word limit in Section C", "Under 200 or over 250 words is outside the instruction. Count before you stop."),
        TIP("Exam link: Paper 2 has Composition, Prescribed texts and Creative writing, one question from each and 20 marks each. Rehearse the whole paper once under timed conditions before the examination."),
        QUIZ("How long is Paper 2?", ["1 hour 30 minutes", "2 hours", "2 hours 15 minutes", "3 hours"], 2,
             "Paper 2 lasts 2 hours 15 minutes.", hint="It is the same length as Paper 3.",
             feedback=["That is the length of Paper 1.", "Paper 2 is longer than that.", "", "That is too long."]),
        QUIZ("What is the word limit for the creative writing section?", ["50 to 100", "200 to 250", "300 to 400", "500 or more"], 1,
             "Creative writing must be between 200 and 250 words.", hint="It is much shorter than the composition.",
             feedback=["That is too short.", "", "That is outside the range.", "That is the minimum for the composition."]),
        PQ("Give the number of choices and the marks in each section of Paper 2.", "Section A: six topics, write one, 20 marks. Section B: four questions, answer one, 20 marks. Section C: two questions, answer one, 20 marks."),
        PQ("You finish Section A with 10 minutes left over your plan. How should you use them?", "Reread the composition for spelling, punctuation, tense and relevance to the topic, and count that the length is at least 500 words. Do not start a new section early without keeping time for the others."),
        PQ("Why should you cross out your plan instead of the finished work?", "The plan is rough work. The finished work is what is marked, and crossing it out loses marks. The Board's report advises candidates to cross out the plan neatly."),
        SUM("Paper 2 lasts 2 hours 15 minutes and has three 20-mark sections.", "Plan about 45 minutes for each section, including planning and checking.", "Write at least 500 words for the composition and 200 to 250 for creative writing.", "Use only prescribed texts and cite them correctly.", "Conceal your identity with the name and address provided."),
    ],
))
