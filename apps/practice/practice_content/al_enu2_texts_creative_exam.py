"""Practice sets for A Level English Language, Upper Sixth: Prescribed Texts, Creative Writing and Examination (one set per lesson, 13 sets),
plus 'Paper 1 mock exam B' (50 multiple-choice questions, the Board's structure: 10 reading, 10 speech work, 20 grammar, 10 vocabulary) and
'Paper 2 skills check A' (auto-markable multiple-choice parts on planning, linking essays to texts, extract analysis, creative-writing technique and
word limits). All passages, poems, extracts and models are original and invented. Facts about the prescribed texts are limited to well-known
outlines; essays and extracts cannot be marked automatically, so these sets test method and technique. IPA is British Received Pronunciation.
"""

import random

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


def K(prompt, right, wrongs, step, concept, skill, hint, feedback="", passage=""):
    """Question spec: the right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80
    return {"prompt": (passage + "\n\n" + prompt) if passage else prompt, "right": right, "wrongs": wrongs,
            "step": step, "concept": concept, "skill": skill, "hint": hint, "feedback": feedback}


def build(specs, seed):
    n = len(specs)
    pos = [i % 4 for i in range(n)]
    random.Random(seed).shuffle(pos)
    out = []
    for sp, p in zip(specs, pos):
        opts = [C(w, why=y) for w, y in sp["wrongs"]]
        opts.insert(p, C(sp["right"], correct=True))
        steps = [S("Reasoning", text=s) for s in ([sp["step"]] if isinstance(sp["step"], str) else sp["step"])]
        out.append(MC(sp["prompt"], opts, steps, concept=sp["concept"], skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
    return out


def SET(module, topic, title, lesson, specs, seed, **kw):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed), **kw))


SETS = []

# ================================================================== 1. Essay method
SET(M_TEXTS, T_WRITE, "Prescribed-text essay: planning and PEEL", "enu2-prescribed-text-essay", [
    K("How many of the four Section B questions must a candidate answer?", "One", [
        ("All four", "Four is the number set, not the number to answer."), ("Two", "Only one is required."), ("Three", "Three is the number of sections in Paper 2, not the number of Section B questions to answer.")],
      "The syllabus says there will be four questions and candidates answer one.", "Prescribed texts: the question format", "Recall", "Look at the paper structure: four set, how many answered?"),
    K("In the question 'Discuss the theme of endurance in two prescribed texts', which word is the command word?", "Discuss", [
        ("Endurance", "That is the focus (the theme), not the instruction."), ("Two", "That is the number of texts."), ("Prescribed", "That describes the texts; it is not an instruction.")],
      "The command word tells you what to do. Discuss means give a developed, balanced explanation with evidence.", "Reading the question", "Concept", "Which word tells you what to DO?"),
    K("Which is the best Point sentence for a paragraph on endurance in The Old Man and the Sea?", "Hemingway presents Santiago's endurance as the source of his dignity.", [
        ("The Old Man and the Sea is a book.", "It makes no claim about the question."), ("Santiago is an old man who goes fishing.", "It retells the story and does not answer the question."), ("Endurance is important in life.", "It is a general opinion, not a claim about the text.")],
      "A Point makes a claim about the text that answers the question and can be proved.", "Point-Evidence-Explain-Link", "Application", "Which sentence makes a claim you could prove?"),
    K("A question asks for illustrations from three prescribed texts. What does the Board's report say about candidates who use two?", "They did not meet the demand of the question.", [
        ("They gained extra credit for depth.", "The report treats this as a weakness."), ("Nothing; the number of texts is never checked.", "The report notes that three were expected."), ("They automatically lose all marks.", "Marks are lost for incomplete coverage, not removed entirely.")],
      "When a question sets a number of texts, using fewer leaves the demand unmet.", "Number of texts", "Interpretation", "Underline the number of texts in the question."),
    K("Which is the correct way to cite a text in a handwritten essay?", "In The Old Man and the Sea (underlined), Hemingway shows...", [
        ("In the book, the writer shows...", "The text and the author are not named."), ("In Old Man by Steinbeck...", "The title is wrong and the author is wrong."), ("In The Old Man and the Sea, he shows...", "The author is not named and 'he' is unclear.")],
      "Give the full title (underlined) and the author's surname the first time.", "Citing texts", "Application", "Which one names both the title and the author correctly?"),
    K("Which tense should you use to write about events in a text?", "The present tense", [
        ("The past tense, because the events are finished", "The convention is the present tense, for example 'Santiago fights'."), ("The future tense", "Events in a text are not in the future."), ("Any mixture, so long as the meaning is clear", "Mixed tenses are an error.")],
      "Literary essays use the present tense: the writer shows, the speaker urges.", "Writing conventions", "Concept", "Think of 'Hemingway shows'."),
    K("A candidate illustrates an answer with a famous novel that is not on the prescribed list. What is the likely result?", "The example earns no credit for the section.", [
        ("It earns extra credit for wide reading.", "The Board's report criticised this practice."), ("It is accepted if the book is famous.", "Only the prescribed texts count."), ("It is accepted if the candidate names the author.", "Naming the author does not make the book prescribed.")],
      "The Board's report notes candidates citing texts that were not part of the syllabus.", "Using prescribed texts only", "Reasoning", "Which texts are you allowed to use?"),
    K("Which Explain sentence is strongest for the Evidence 'the speaker repeats the word if at the start of many lines'?", "The repetition creates a rhythm like a teacher listing rules and delays the final promise, which gives the advice weight.", [
        ("The poet uses repetition.", "It names the device but does not explain the effect."), ("Repetition is a figure of speech.", "It defines the device only."), ("The speaker likes the word if.", "It gives no meaning or effect.")],
      "Explain means saying what the device does and why it matters for the point.", "Explaining evidence", "Analysis", "Which sentence says what the device does?"),
], 101)

# ================================================================== 2. Extract questions
SET(M_TEXTS, T_WRITE, "Extract questions: meaning, devices and grammar", "enu2-extract-questions", [
    K("What is the first thing to do with an extract?", "Read it twice and place it in the text.", [
        ("Start writing the answer at once.", "Without placing the extract you may misread its meaning."), ("Count the number of lines.", "Length does not help you answer."), ("Find a quotation from another book.", "Only prescribed texts may be used, and not in the first step.")],
      "Placing the extract (who speaks, where in the text) gives the context.", "Extract routine", "Concept", "What gives you the context for the questions?"),
    K("'Meaning in context' means", "what the word or phrase means in this particular passage.", [
        ("its first dictionary meaning only.", "The dictionary meaning may not fit the passage."), ("a synonym chosen at random.", "The meaning must be justified by the context."), ("the word's origin.", "Origin is not the question.")],
      "The meaning must fit the sentence and situation.", "Meaning in context", "Recall", "Where must the meaning fit?"),
    K("In the line 'The market was a silent field of wet sheets', the figure of speech is", "a metaphor", [
        ("a simile", "There is no like or as."), ("an alliteration", "The sound pattern is not the main device."), ("a rhyme", "There is no rhyming ending.")],
      "The market is directly called a field, which is metaphor.", "Figures of speech", "Concept", "Look for 'like' or 'as'."),
    K("Which answer best states the MESSAGE of an extract in which a man hesitates, then goes out into the storm to face his trouble?", "Trouble cannot be escaped, so it must be faced.", [
        ("A man looks at the rain.", "That is a description of events."), ("The weather is bad.", "That is a detail, not a message."), ("Storms last a long time.", "It is not supported as the idea of the passage.")],
      "A message is the idea the passage leads to.", "Message of a passage", "Interpretation", "Which option is an idea and not an event?"),
    K("Change to the simple past: 'He opens the window and sees the rain.'", "He opened the window and saw the rain.", [
        ("He opens the window and saw the rain.", "Only one verb was changed."), ("He has opened the window and seen the rain.", "That is the present perfect."), ("He opened the window and see the rain.", "The second verb was not changed correctly.")],
      "Opens becomes opened and sees becomes saw (irregular).", "Grammar task on an extract", "Calculation", "Find both verbs."),
    K("In an answer on a figure of speech, which three things should you include?", "Name it, quote the words and explain the effect.", [
        ("Name it only.", "That earns very few marks."), ("Quote the whole page.", "Quotations should be short."), ("Retell the story.", "A retelling does not explain the device.")],
      "The three parts together show analysis.", "Answering device questions", "Concept", "Think name, evidence, effect."),
    K("A question asks you to show how sacrifice appears in OTHER prescribed texts. What is the best approach?", "Use two or three other prescribed texts, each with a specific moment and an explanation.", [
        ("Write only about the extract.", "The question asks for other texts."), ("Use any famous novel.", "Only prescribed texts are acceptable."), ("List the word 'sacrifice' ten times.", "The question needs examples and explanation.")],
      "Name the texts and authors, give a moment and explain the link.", "Linking to other texts", "Application", "Which texts may you use?"),
    K("Which answer to 'Explain the phrase carries it on his back' (meaning a man who runs from trouble carries it) is best in context?", "A person who runs away from a problem still has the problem with him, like a heavy load.", [
        ("A man carries a bag on his back.", "It is the literal meaning, which does not fit."), ("Backs are strong.", "It does not explain the phrase."), ("The man is tired.", "It is not the meaning of the phrase.")],
      "The phrase is figurative: the problem is a load that goes wherever he goes.", "Meaning in context", "Reasoning", "Is the phrase literal here?"),
], 102)

# ================================================================== 3. Drama method
SET(M_TEXTS, T_DRAMA, "Reading and writing about a play", "enu2-drama-how-to-write", [
    K("What are the words printed in brackets that tell actors how to speak or move called?", "Stage directions", [
        ("Dialogue", "Dialogue is what characters say."), ("Footnotes", "Footnotes explain words at the bottom of a page."), ("Epilogues", "An epilogue is a closing speech or section.")],
      "Stage directions are the playwright's instructions.", "Drama terms", "Recall", "They direct the stage."),
    K("In an essay about a play you should write", "the playwright shows", [
        ("the narrator says", "A play has no narrator."), ("in chapter two", "Plays have acts and scenes, not chapters."), ("the poet suggests", "A poet writes poems.")],
      "Use the vocabulary of drama.", "Writing about drama", "Concept", "Who writes a play?"),
    K("A character says 'I am not afraid' while his hands shake. This is best described as", "a contrast between words and action that reveals his fear", [
        ("a rhyme", "Rhyme concerns sounds."), ("a flashback", "No earlier time is shown."), ("a change of setting", "The place has not changed.")],
      "The gap between what is said and shown reveals the character.", "Character in drama", "Interpretation", "Compare speech with action."),
    K("Dramatic irony occurs when", "the audience knows something that a character does not.", [
        ("a character tells a joke.", "A joke is not irony."), ("the stage is empty.", "That is a staging choice."), ("the play ends in a happy way.", "The ending is a separate matter.")],
      "The audience's extra knowledge creates tension.", "Dramatic irony", "Concept", "Think about who knows what."),
    K("Which is the best first sentence for a paragraph about conflict?", "The playwright uses the quarrel between the two characters to show the pressure of their situation.", [
        ("There is a quarrel.", "It states a fact but makes no point."), ("Quarrels are bad.", "It is a general opinion."), ("The play has many people.", "It is irrelevant to conflict.")],
      "A strong Point makes a claim about the writer's method.", "Point sentences", "Application", "Which makes a claim about the playwright?"),
    K("Which feature of a play can a novel NOT directly use?", "Actors, movement and lighting seen by an audience", [
        ("Characters", "Novels have characters."), ("Setting", "Novels have settings too."), ("Theme", "Novels have themes.")],
      "A play is written to be performed.", "Nature of drama", "Reasoning", "What happens only on stage?"),
    K("Why is a silence in a play important?", "It can show feelings that the characters do not say.", [
        ("It means the actors forgot their lines.", "Silences in scripts are usually planned."), ("It has no meaning.", "Silence can carry meaning."), ("It means the scene has ended.", "A scene can continue after a pause.")],
      "Subtext and silence tell the audience what words do not.", "Techniques in drama", "Analysis", "Think of what is left unsaid."),
    K("Which is the correct way to write a theme for an essay?", "The play suggests that blind faith can be used by those who control it.", [
        ("Faith.", "One word is not a statement."), ("The play is about a village.", "It names a setting, not a theme."), ("The characters speak a lot.", "It is an observation, not a theme.")],
      "A theme is an idea written as a sentence.", "Themes", "Application", "A theme should be a full idea."),
], 103)

# ================================================================== 4. The Swamp Dwellers
SET(M_TEXTS, T_DRAMA, "The Swamp Dwellers: setting, themes and method", "enu2-swamp-dwellers", [
    K("Who wrote The Swamp Dwellers?", "Wole Soyinka", [
        ("Ernest Hemingway", "Hemingway wrote The Old Man and the Sea."), ("Rudyard Kipling", "Kipling wrote the poem 'If'."), ("Claude McKay", "McKay wrote the poem 'If We Must Die'.")],
      "The Board lists The Swamp Dwellers by Soyinka in Three Short Plays.", "The Swamp Dwellers: author and form", "Recall", "He is a Nigerian playwright."),
    K("What kind of text is The Swamp Dwellers?", "A play", [
        ("A novel", "The Board lists it under drama."), ("A sonnet", "A sonnet is a fourteen-line poem."), ("A newspaper report", "It is a literary text.")],
      "It is the drama text on the prescribed list.", "The Swamp Dwellers: author and form", "Recall", "Which genre does the Board list it under?"),
    K("Where is the play set?", "In a swamp village affected by floods", [
        ("On a ship at sea", "That is the setting of The Old Man and the Sea (a small boat at sea)."), ("In a modern airport", "The play has a village setting."), ("In a university", "A swamp village is the setting.")],
      "The setting is a swamp village, and the water shapes the villagers' lives.", "The Swamp Dwellers: setting", "Recall", "The title names the place."),
    K("Why is setting important in this play?", "The floods and the swamp create the problems and shape what the characters believe and do.", [
        ("It has no effect on the characters.", "The setting is central to the conflict."), ("It is only a decoration on the stage.", "In drama the setting is part of the meaning."), ("It makes the play funny.", "The play treats serious hardship.")],
      "Setting creates the problem and pushes characters towards ritual.", "Setting and theme", "Concept", "Think of the effect of water and failing crops."),
    K("Which of these is a theme usually linked to the Kadiye and the villagers' offerings?", "Faith and its exploitation", [
        ("Winning a football match", "That is not related to the play's main ideas."), ("Learning a foreign language", "It is not a theme of the play."), ("A holiday at the beach", "The play treats hardship, not leisure.")],
      "Check this against your own copy: the priest of the Serpent and the offerings suggest faith and exploitation.", "Themes of the play", "Interpretation", "Who gains from the offerings?"),
    K("Which line of thinking best prepares an essay on 'village and city'?", "Compare how a character who returned from the city sees the village with how those who stayed see it.", [
        ("Count the pages of each scene.", "Page count does not explore a theme."), ("Only discuss the weather.", "The theme needs contrast of outlooks."), ("Ignore the returning character.", "The returning son is central to the contrast.")],
      "The returning son provides the contrast.", "Village and city", "Analysis", "Which characters hold different views?"),
    K("A student is unsure of a detail of the plot. What is the best action in an essay?", "Refer to the moment carefully in general terms and check the detail in the copy beforehand.", [
        ("Invent the detail confidently.", "Wrong details cost marks."), ("Use an event from another play.", "Only the prescribed texts count."), ("Leave the essay unfinished.", "A careful general reference earns credit.")],
      "Accuracy matters; check your copy.", "Using evidence", "Reasoning", "What protects you from errors?"),
    K("Which essay statement is the most balanced?", "The play invites us to question those who profit from belief while still showing sympathy for the villagers.", [
        ("The playwright hates all tradition.", "It is one-sided and unsupported."), ("The villagers are fools.", "It ignores the sympathy shown."), ("The city is perfect.", "The play does not present the city as perfect.")],
      "Balanced answers see complexity.", "Balanced argument", "Application", "Which statement allows two attitudes?"),
], 104)

# ================================================================== 5. Prose method
SET(M_TEXTS, T_PROSE, "Narrator, setting, character and structure in prose", "enu2-prose-how-to-write", [
    K("A narrator who says 'I' and takes part in the story uses", "first-person narration", [
        ("third-person omniscient narration", "An omniscient narrator stands outside the story."), ("dramatic irony", "It is not a type of narrator."), ("stage directions", "Those belong to plays.")],
      "'I' marks first-person narration.", "Point of view", "Recall", "Look at the pronoun."),
    K("Which is an example of indirect characterisation?", "A man gives away his last coins without being asked.", [
        ("The narrator says he is generous.", "That tells us directly."), ("The writer lists his age.", "Facts are not indirect traits."), ("The title names him.", "A name is not a trait.")],
      "Indirect characterisation shows a trait through action or speech.", "Characterisation", "Concept", "Which option shows rather than tells?"),
    K("What does setting include?", "Place, time and atmosphere", [
        ("Only the name of the town", "Setting is more than a name."), ("Only the weather", "Weather is one part."), ("The list of characters", "That is cast, not setting.")],
      "Setting is mood, place and social conditions.", "Setting", "Recall", "It is more than just place."),
    K("An essay should say 'the narrator' rather than 'the writer' when", "referring to the voice telling the story inside the text.", [
        ("referring to the cover of the book.", "That is not the narrator."), ("talking about the publisher.", "That is not the narrator."), ("you cannot remember the name.", "Choose terms for meaning, not memory.")],
      "The narrator and the author are not always the same.", "Narrator and author", "Concept", "Who tells the story inside the book?"),
    K("A passage ends 'She said it would come back, but she did not look at her son.' What does the detail suggest?", "She is not sure, and she hides it.", [
        ("She is angry with the narrator.", "Nothing suggests this."), ("The son is not in the room.", "He is present."), ("She is reading a book.", "No reading is mentioned.")],
      "The avoided glance is indirect evidence of doubt.", "Inference from detail", "Interpretation", "What does not looking at someone suggest?"),
    K("Which is the best use of a notes template for a prose text?", "Fill it in from your own reading with page references.", [
        ("Copy notes from a friend who did not read the text.", "The notes must come from your own reading."), ("Write only the title.", "A template needs details."), ("Use notes from a film.", "A film is not the text.")],
      "Specific notes from the book are the best evidence in an essay.", "Study method", "Application", "Where must the notes come from?"),
    K("Which sentence describes a theme and not a plot event?", "The novel explores how hope can survive hardship.", [
        ("The family sits at the table.", "It is an event."), ("A candle is lit.", "It is a detail."), ("The dogs stop barking.", "It is an event.")],
      "A theme is an idea.", "Themes in prose", "Analysis", "Which one is an idea?"),
    K("For Twilight of Misty Foliage and Unanswered Cries, where must the plot and character facts used in an essay come from?", "Your own reading of your own copy.", [
        ("A single memorised summary from the internet.", "Summaries differ and may be wrong."), ("Guesses from the title.", "Titles do not give facts."), ("The film of another novel.", "It is not the text.")],
      "Facts must be checked against the book.", "Evidence discipline", "Reasoning", "What is the evidence for an essay?"),
], 105)

# ================================================================== 6. The Old Man and the Sea
SET(M_TEXTS, T_PROSE, "The Old Man and the Sea: outline, themes and style", "enu2-old-man-and-the-sea", [
    K("Who is the main character of The Old Man and the Sea?", "Santiago, an old Cuban fisherman", [
        ("Manolin, a captain", "Manolin is the boy who cares for Santiago."), ("A shark", "The sharks are attackers, not the main character."), ("A young American soldier", "That does not describe the novella.")],
      "Santiago is the old fisherman.", "The Old Man and the Sea: characters", "Recall", "Think of the title."),
    K("How many days has Santiago gone without a fish at the start?", "Eighty-four", [
        ("Fourteen", "It is far more than fourteen."), ("Forty", "Forty appears in other stories."), ("A hundred", "The book says eighty-four.")],
      "The novella opens after eighty-four days without a catch.", "The Old Man and the Sea: plot", "Recall", "It is a little over eighty."),
    K("What does Santiago catch far out at sea?", "A huge marlin", [
        ("A shark that he keeps", "The sharks destroy the marlin."), ("A treasure chest", "It is not in the story."), ("A small shoal of sardines", "He catches a giant fish.")],
      "The marlin is his great catch.", "The Old Man and the Sea: plot", "Recall", "A large fish."),
    K("What happens to the marlin on the way home?", "Sharks attack and eat most of it.", [
        ("It escapes at once.", "He kills it first."), ("It is sold in Havana.", "Only the skeleton arrives."), ("Manolin takes it.", "The sharks destroy it.")],
      "Sharks reduce it to a skeleton.", "The Old Man and the Sea: plot", "Recall", "The sea is dangerous."),
    K("Which statement best describes Hemingway's style here?", "Plain, with short sentences and everyday words", [
        ("Elaborate, with long sentences and rare words", "The opposite is true."), ("Written in rhyming verse", "It is prose."), ("Written as letters", "It is a narrative.")],
      "The plain style makes the effort feel real.", "Style", "Concept", "Think of simple, direct language."),
    K("Which theme best fits Santiago's behaviour after the sharks attack?", "Dignity in defeat", [
        ("Winning at all costs", "He loses the fish."), ("Greed for money", "Money is not the main motive."), ("Fear of the sea", "He respects the sea but is not ruled by fear.")],
      "He keeps fighting and keeps his self-respect.", "Themes", "Interpretation", "How does he behave while losing?"),
    K("Why is Manolin included in the story?", "He shows loyalty and the passing on of skill.", [
        ("He is the villain.", "He is loyal."), ("He catches the marlin.", "Santiago does."), ("He has no role.", "He gives the ending its warmth.")],
      "Manolin cares for Santiago and promises to fish with him again.", "Characters", "Analysis", "Think of the ending."),
    K("A student writes 'Santiago is a failure because he returns with a skeleton.' Which is the best correction?", "He is defeated in result but not destroyed in spirit, and the novella values his courage.", [
        ("He is a complete success with no loss.", "He loses the fish."), ("The sharks are evil characters.", "Sharks act by nature."), ("The student is right.", "The essay should see both sides.")],
      "Balanced readings recognise the loss and the dignity.", "Balanced argument", "Reasoning", "Consider results and spirit."),
], 106)

# ================================================================== 7. Poetry method
POEM_Q = ("The Last Bus (an invented poem)\n\nThe last bus leaves without a sound,\nits lamps like tired eyes.\nIt takes the market's noise away\nand leaves the stars to rise.\n\n"
          "I count my coins beside the road\nand think of home, so far,\nyet every step I plan to take\nis lit by one small star.")
SET(M_TEXTS, T_POETRY, "Reading and writing about a poem", "enu2-poetry-how-to-write", [
    K("In the poem, 'its lamps like tired eyes' is", "a simile", [
        ("a metaphor", "A metaphor has no like or as."), ("a rhyme", "It is a comparison, not a rhyme."), ("a stage direction", "Poems do not have stage directions.")],
      "The word like marks a simile.", "Figures of speech", "Concept", "Look for the word like.", passage=POEM_Q),
    K("Which words rhyme in the first stanza?", "eyes and rise", [
        ("sound and away", "These do not rhyme."), ("bus and stars", "These do not rhyme."), ("noise and sound", "These do not rhyme.")],
      "The second and fourth lines rhyme.", "Rhyme", "Recall", "Check the second and fourth lines.", passage=POEM_Q),
    K("What is the tone of the first stanza?", "Quiet and a little lonely", [
        ("Angry and loud", "Nothing in it is loud."), ("Joking", "The mood is quiet, not comic."), ("Proud and boastful", "The speaker does not boast.")],
      "The silent departure and tired lamps suggest loneliness.", "Tone", "Interpretation", "How does the speaker feel at night alone?", passage=POEM_Q),
    K("What effect does 'yet' have in the second stanza?", "It turns the poem from loneliness to hope.", [
        ("It repeats the first stanza.", "It signals a change."), ("It adds a rhyme.", "It is not at a line end."), ("It introduces a new speaker.", "The speaker is the same.")],
      "A word of contrast marks the turn.", "Structure", "Analysis", "Yet signals a contrast.", passage=POEM_Q),
    K("What does the small star most likely symbolise?", "A modest hope that guides the speaker", [
        ("A bus route", "It is a symbol, not a route."), ("A danger", "Light suggests hope here."), ("The market", "The market is mentioned separately.")],
      "Light in the dark is a common symbol of hope.", "Symbols", "Interpretation", "What does light in darkness often suggest?", passage=POEM_Q),
    K("How should you quote from a poem in an essay?", "A few exact words inside your own sentence, followed by an explanation", [
        ("The whole poem", "It wastes time."), ("No quotation at all", "Brief evidence is expected."), ("A paraphrase without naming the poem", "The examiner must know the poem.")],
      "Short quotations keep your argument in front.", "Writing about poetry", "Application", "Be brief and exact."),
    K("'The street was a river of light.' This is", "a metaphor", [
        ("a simile", "It has no like or as."), ("an example of enjambment", "It is a comparison, not a line-break feature."), ("a rhyme", "It has no rhyming end.")],
      "The street is said to be a river.", "Figures of speech", "Concept", "Is there like or as?"),
    K("When comparing two poems, how should you organise your paragraphs?", "By ideas (similarity, difference, form), using both poems in each paragraph.", [
        ("Write all about one poem, then all about the other.", "That makes comparison weak."), ("Write only about the title.", "It is not enough."), ("Skip the second poem.", "A comparison needs both.")],
      "Comparative paragraphs weave the two poems together.", "Comparing poems", "Reasoning", "What is the purpose of a comparison?"),
], 107)

# ================================================================== 8. If and If We Must Die
SET(M_TEXTS, T_POETRY, "'If' and 'If We Must Die' compared", "enu2-if-and-if-we-must-die", [
    K("Who wrote the poem 'If'?", "Rudyard Kipling", [
        ("Claude McKay", "McKay wrote 'If We Must Die'."), ("Wole Soyinka", "Soyinka wrote The Swamp Dwellers."), ("Ernest Hemingway", "Hemingway wrote The Old Man and the Sea.")],
      "'If' is by Kipling.", "'If': author", "Recall", "Think of the British writer."),
    K("Who is addressed in Kipling's 'If'?", "A son", [
        ("A king", "A king is only mentioned among the people the person may meet."), ("A crowd of soldiers", "The speaker addresses one person."), ("The sea", "The sea is not addressed.")],
      "The speaker gives advice to a son.", "'If': voice", "Recall", "It is advice from a parent."),
    K("What is the form of 'If We Must Die'?", "A sonnet of fourteen lines", [
        ("Four stanzas of eight lines", "That is the form of 'If'."), ("A ballad of twenty stanzas", "That is not the form."), ("A play script", "It is a poem.")],
      "McKay's poem is a sonnet.", "'If We Must Die': form", "Recall", "Count fourteen lines."),
    K("What is the tone of 'If We Must Die'?", "Defiant and urgent", [
        ("Calm and gentle", "That fits 'If' better."), ("Humorous", "The subject is serious."), ("Confused", "The speaker is firm.")],
      "The speaker urges his kinsmen to resist.", "'If We Must Die': tone", "Interpretation", "Think of a rallying cry."),
    K("What do the animal images (hogs and dogs) show in McKay's poem?", "How degrading it is to die without resistance", [
        ("A love of animals", "The animals stand for degrading treatment."), ("A farm scene", "The images are metaphors for treatment."), ("A joke about animals", "The poem is serious.")],
      "The speaker rejects dying like hunted animals.", "Imagery", "Analysis", "How does the speaker want them NOT to die?"),
    K("What is the main structural feature of Kipling's 'If'?", "Repeated conditional clauses that lead to a final promise", [
        ("A dialogue between two speakers", "There is only one voice."), ("A rhyming couplet only", "The poem is long and built of stanzas."), ("A list of animals", "That is not the structure.")],
      "The conditions delay the conclusion.", "Structure", "Analysis", "Think of the word if."),
    K("Which is a similarity between the two poems?", "Both treat dignity and courage when facing difficulty.", [
        ("Both are sonnets.", "Only McKay's is."), ("Both were written in the same year.", "They were published in 1910 and 1919."), ("Both are addressed to a son.", "Only 'If' is.")],
      "The theme of dignity under pressure links them.", "Comparing the two poems", "Reasoning", "Think of the ideas, not the form."),
    K("Which is the best way to refer to the poems' lines in an essay?", "Quote a word or two and paraphrase the rest.", [
        ("Copy several lines from memory.", "Memory may be inexact."), ("Do not mention the words at all.", "A few exact words are good evidence."), ("Quote another poem instead.", "Only the poems asked for count.")],
      "Short, exact quotations are safest.", "Using evidence", "Application", "Be brief."),
], 108)

# ================================================================== 9. Short stories and sketches
SET(M_CREATE, T_STORY, "Short stories and sketches", "enu2-short-stories-sketches", [
    K("What is the word limit for the creative writing section?", "200 to 250 words", [
        ("100 to 150 words", "That is too short."), ("300 to 350 words", "That is too long."), ("500 or more", "That is for the composition.")],
      "The syllabus sets a limit of 200 to 250 words.", "Word limit", "Recall", "It is shorter than the composition."),
    K("Which sentence is the best opening for a very short story?", "The generator died just as the first guests arrived.", [
        ("I woke up at six and brushed my teeth.", "It wastes words on routine."), ("Once upon a time there was a long story.", "It is vague."), ("This is a story about a wedding.", "It tells rather than begins the action.")],
      "A good opening starts inside the action.", "Openings", "Application", "Which one starts the trouble?"),
    K("A question gives you the first sentence of a story. You should", "use it exactly and continue from it.", [
        ("change it slightly.", "The words must be used."), ("ignore it.", "That would not answer the question."), ("write only one more sentence.", "The task needs the full word range.")],
      "Given words must be used exactly.", "Given openings", "Concept", "What does the question require?"),
    K("Which is correctly punctuated dialogue?", "'Where are you going?' she asked.", [
        ("'Where are you going.' She asked.", "The question mark and lower case are needed."), ("Where are you going? she asked.", "Quotation marks are missing."), ("'Where are you going' she asked?", "The question mark is outside.")],
      "The question mark goes inside the closing mark.", "Dialogue", "Calculation", "Look at the question mark."),
    K("Which technique does 'His shoulders were bent like an old bridge' use?", "A simile", [
        ("A metaphor", "It uses like."), ("Alliteration", "It is a comparison."), ("A rhetorical question", "It is not a question.")],
      "The word like marks a simile.", "Techniques", "Concept", "Find the word like."),
    K("A sketch differs from a short story because it", "focuses on a person, place or moment, with little or no plot.", [
        ("must have a long plot.", "A sketch needs little plot."), ("is written in verse only.", "A sketch is usually prose."), ("has no description.", "A sketch is full of description.")],
      "The focus is description.", "Sketches", "Recall", "Think about what a sketch shows."),
    K("A story has 18 lines of handwriting, each with about 12 words. Is it inside the 200 to 250 limit?", "Yes: it has about 216 words.", [
        ("No: it has about 150 words.", "18 x 12 = 216."), ("No: it has about 300 words.", "18 x 12 = 216."), ("It cannot be estimated.", "Lines multiplied by words per line gives an estimate.")],
      "18 x 12 = 216, which is within 200 to 250.", "Word count estimate", "Calculation", "Multiply lines by words per line."),
    K("Which ending is best for a 230-word story that began with an envelope arriving?", "A quiet detail that answers the mystery, such as a familiar pen on a shop counter.", [
        ("A long explanation of the moral", "It tells instead of shows."), ("A new character with a new problem", "It leaves the story unfinished."), ("The sentence 'The end'", "It adds nothing.")],
      "An ending should echo the opening or resolve the problem.", "Endings", "Reasoning", "Which one closes the story's question?"),
], 109)

# ================================================================== 10. Poems and plays
SET(M_CREATE, T_POEMPLAY, "Poems and short plays", "enu2-poems-and-plays", [
    K("Which line is correctly laid out in a play script?", "ABENA: (smiling) Good morning.", [
        ("'Good morning,' said Abena.", "That is story style."), ("Abena says, \"Good morning.\"", "That is story style with a verb of saying."), ("Good morning (Abena)", "The speaker's name should come first with a colon.")],
      "A script uses the name, a colon, a bracketed direction and no quotation marks.", "Play layout", "Recall", "Look for name plus colon."),
    K("Stage directions in a script are usually written", "in brackets", [
        ("in quotation marks", "Quotation marks are for stories."), ("in capital letters throughout", "Capitals are for speaker names."), ("at the end of the page", "They are placed where they apply.")],
      "Brackets mark directions.", "Play layout", "Recall", "Think of how directions are separated from speech."),
    K("In an ABCB rhyme scheme which lines rhyme?", "The second and fourth", [
        ("The first and third", "That is the pattern ABAB."), ("The first and second", "That is AABB."), ("All four lines", "That is AAAA.")],
      "In ABCB, lines 2 and 4 rhyme.", "Rhyme schemes", "Concept", "B appears twice."),
    K("A poem has 10 stanzas of 4 lines, each stanza with about 22 words. About how many words does it have?", "220", [
        ("40", "That counts lines, not words."), ("88", "That is 4 x 22."), ("2200", "That multiplies by an extra ten.")],
      "10 x 22 = 220.", "Word count for a poem", "Calculation", "Multiply stanzas by words per stanza."),
    K("What is subtext?", "Feeling or meaning beneath the words that the audience understands", [
        ("Text printed under a picture", "That is a caption."), ("The title of the play", "It is not the title."), ("Words in another language", "It is not translation.")],
      "Characters do not state subtext openly.", "Subtext", "Concept", "Think of what is unsaid."),
    K("Which is the best reason to plan a poem's number of stanzas first?", "So that the poem fits the 200 to 250 word limit.", [
        ("Because poems must always have ten stanzas.", "There is no fixed number."), ("Because rhyme is impossible otherwise.", "It is possible without planning."), ("Because planning is not allowed.", "Planning is advised.")],
      "Stanzas times words per stanza gives the total.", "Planning", "Reasoning", "What limit must you keep?"),
    K("A play scene of 224 words includes 16 speaker labels (one word each). How many words are there without the labels?", "208", [
        ("240", "That adds the labels."), ("224", "That is the total."), ("200", "That is a guess.")],
      "224 - 16 = 208, which is at least 200.", "Counting words in a script", "Calculation", "Subtract the labels."),
    K("Which version of this scene has a bracketed direction in the correct place? KWEDI refuses to lend her pen.", "KWEDI: (holding the pen behind her back) It is the only one I have.", [
        ("(KWEDI) It is the only one I have, holding the pen behind her back.", "The direction is mixed into the speech."), ("It is the only one I have said Kwedi.", "That is story style."), ("'It is the only one I have.' (Kwedi holds the pen)", "Quotation marks do not belong in a script.")],
      "Name, colon, direction in brackets, then speech.", "Play layout", "Application", "Check the layout."),
], 110)

# ================================================================== 11. Reports
SET(M_CREATE, T_REPORT, "Reports of meetings and news reports", "enu2-meeting-and-news-reports", [
    K("In which tense is a report of a meeting mainly written?", "The past tense", [
        ("The present tense", "The meeting is finished."), ("The future tense", "It records what happened."), ("The imperative", "It does not give orders.")],
      "A meeting report records the meeting that has happened.", "Meeting reports", "Recall", "Is the meeting over?"),
    K("The first paragraph of a news report is called", "the lead", [
        ("the footnote", "A footnote is at the bottom."), ("the caption", "A caption describes a picture."), ("the signature", "That ends a report.")],
      "The lead gives the key facts first.", "News reports", "Recall", "It leads the report."),
    K("Which facts belong in the lead?", "Who, what, where and when", [
        ("Only the reporter's opinion", "Opinions are not part of the lead."), ("Only background history", "History comes later."), ("A list of names of readers", "That is not news.")],
      "The most important facts come first.", "News reports", "Concept", "Think of the inverted pyramid."),
    K("Which is correct reported speech? The chairman said, 'We will meet again next week.'", "The chairman said that they would meet again the following week.", [
        ("The chairman said that they will meet again next week.", "Tense and time words were not changed."), ("The chairman said we would meet again next week.", "The time expression was not changed."), ("The chairman said, that we will meet again.", "It mixes direct and reported speech.")],
      "Will becomes would and next week becomes the following week.", "Reported speech", "Application", "Move one step back."),
    K("Which order is correct for a report of a meeting?", "Opening details, previous minutes, main items, other business, closing", [
        ("Closing, main items, opening details", "The order is reversed."), ("Other business first, then opening details", "Other business comes late."), ("Main items, then date and place", "The details of the meeting come first.")],
      "Follow the order of the meeting.", "Meeting reports", "Concept", "Think of a real meeting."),
    K("A headline for a news report should be", "short and focused on the main event", [
        ("a long paragraph", "It should be brief."), ("the writer's real name and address", "Never put your own details."), ("a list of every detail", "It is only a short title.")],
      "A headline captures the main event briefly.", "News reports", "Concept", "How long is a headline?"),
    K("Which sentence has a tense error in a meeting report?", "The principal reports that the roof was finished.", [
        ("The principal reported that the roof had been finished.", "It is correct."), ("The chairman asked members to suggest ideas.", "It is correct."), ("The meeting ended at noon.", "It is correct.")],
      "A meeting report should stay in the past tense: reported, not reports.", "Tense consistency", "Analysis", "Look for the odd one out in tense."),
    K("What should a news report's writer do about personal opinion?", "Leave it out unless the task asks for it.", [
        ("Include it in the lead.", "News is factual."), ("Make it the headline.", "News is factual."), ("Replace facts with opinion.", "Facts are the content.")],
      "News reports are factual.", "News reports", "Reasoning", "Think of the purpose of a news report."),
], 111)

# ================================================================== 12-13. Examination lessons
SET(M_EXAM, "Paper 1", "Paper 1: structure and strategy", "enx2-paper-1-strategy", [
    K("How many questions are there in Paper 1?", "50", [("30", "Too few."), ("40", "Too few."), ("100", "Too many.")],
      "Paper 1 has 50 multiple-choice questions.", "Paper 1 structure", "Recall", "It is a round number of fifty."),
    K("How long is Paper 1?", "1 hour 30 minutes", [("1 hour", "Too short."), ("2 hours 15 minutes", "That is the length of Papers 2 and 3."), ("3 hours", "Too long.")],
      "Paper 1 lasts 90 minutes.", "Paper 1 structure", "Recall", "It is the shortest of the papers."),
    K("Which section of Paper 1 has the most questions?", "Grammar (20)", [("Reading comprehension (10)", "It has 10."), ("Speech work (10)", "It has 10."), ("Vocabulary (10)", "It has 10.")],
      "Grammar has 20 questions.", "Paper 1 structure", "Recall", "It is double the others."),
    K("What is the best first step on a multiple-choice question?", "Read the stem and predict the answer.", [
        ("Read all four options and choose the longest.", "Length is not a clue."), ("Shade the same letter every time.", "It is not a method."), ("Skip all long questions.", "You lose easy marks.")],
      "Predicting protects you from attractive wrong options.", "MC method", "Concept", "Think before looking at options."),
    K("'Neither of the two answers ___ correct.' Which word completes it?", "is", [("are", "Neither takes a singular verb."), ("were", "Plural and past."), ("be", "It is not a finite verb here.")],
      "Neither is singular: neither ... is.", "Elimination in grammar", "Application", "Is neither singular or plural?"),
    K("You have 6 minutes left and 5 unanswered questions. What should you do?", "Answer each using the best guess from elimination, then check the answer sheet.", [
        ("Leave them blank.", "Blanks cannot score."), ("Shade the same letter for all.", "Elimination gives a better chance."), ("Start rereading the passage in detail.", "There is not enough time.")],
      "Every question deserves an answer, and the sheet must be checked.", "Time management", "Application", "Which action can earn marks?"),
    K("Which time allocation matches the Board's guide for Reading comprehension?", "35 minutes", [("15 minutes", "That is the time for Speech work and for Vocabulary."), ("25 minutes", "That is for Grammar."), ("45 minutes", "That is not a Paper 1 time.")],
      "The sections are 35, 15, 25 and 15 minutes.", "Paper 1 timing", "Recall", "It is the longest section."),
    K("A stem says 'Which of the following is NOT stated in the passage?' What should you do?", "Check each option against the passage and choose the one not mentioned.", [
        ("Choose the first option you find in the passage.", "That is the opposite of the task."), ("Ignore the word NOT.", "It changes the task."), ("Choose the longest option.", "Length is not a clue.")],
      "The right answer is the one the passage does not support.", "Reading the stem", "Reasoning", "What does NOT change?"),
], 112)

SET(M_EXAM, "Paper 2", "Paper 2: structure and time plan", "enx2-paper-2-strategy", [
    K("How long is Paper 2?", "2 hours 15 minutes", [("1 hour 30 minutes", "That is Paper 1."), ("2 hours", "Too short."), ("3 hours", "Too long.")],
      "Paper 2 lasts 135 minutes.", "Paper 2 structure", "Recall", "It is the same length as Paper 3."),
    K("How many marks does each section of Paper 2 carry?", "20", [("10", "That is the content mark in composition."), ("15", "That is a Paper 3 section."), ("50", "That is the number of Paper 1 questions.")],
      "Each section carries 20 marks.", "Paper 2 structure", "Recall", "All three are equal."),
    K("In Section A, how many of the six composition topics must you write on?", "One", [("Two", "Only one is required."), ("Three", "Only one is required."), ("All six", "Only one is required.")],
      "You choose one topic.", "Paper 2 structure", "Recall", "The question says one."),
    K("What is the length requirement for the composition?", "At least 500 words", [("200 to 250 words", "That is creative writing."), ("About 100 words", "Far too short."), ("Exactly 1000 words", "That is not the requirement.")],
      "The composition needs at least 500 words.", "Word limits", "Recall", "It is the longest piece."),
    K("A sensible time plan for Paper 2 is", "about 45 minutes for each section, including planning and checking", [
        ("90 minutes for Section A and 15 for the others", "Sections B and C would be rushed."), ("No planning at all", "Planning improves marks."), ("Spend all the time on Section C", "All sections carry equal marks.")],
      "Three equal sections of 20 marks deserve equal time.", "Time plan", "Application", "How many marks per section?"),
    K("What should you do with your plan after you finish writing?", "Cross it out neatly and leave the finished work.", [
        ("Cross out the finished work.", "That loses marks."), ("Hand in only the plan.", "The plan is not marked."), ("Tear out the page.", "It is not needed.")],
      "The Board's report advises candidates to cross out the plan.", "Planning", "Concept", "What is marked?"),
    K("Which name should you write on a creative writing piece that needs a signature?", "The name and address provided in the question", [("Your own name and address", "That reveals your identity."), ("Your friend's name", "Use only the name provided."), ("A famous author's name", "Use only the name provided.")],
      "Candidates must conceal identity with the name and address provided.", "Examination conventions", "Application", "What does the question provide?"),
    K("Which is the best way to choose among the four prescribed-text questions?", "Pick the one for which you can name the clearest moments from your own texts.", [
        ("Pick the one with the shortest title.", "Length does not matter."), ("Pick the most unusual one.", "It may be risky."), ("Pick at random.", "Evidence is what earns marks.")],
      "Strong evidence supports strong essays.", "Choosing a question", "Reasoning", "What do you need for each point?"),
], 113)

# ================================================================== Paper 1 mock exam B (50 questions: 10 + 10 + 20 + 10)
RA = ("**Passage 1: A Radio Class** (invented)\n\n"
      "When schools closed because of the floods, the teachers of a school in Mamfe started a radio class. Every morning at ten, a teacher read a lesson over the "
      "local station, and pupils listened at home with their exercise books open. Parents were asked to sit with the younger children. At first only a few families "
      "took part, because many homes had no radio. Then neighbours began to gather around one set, and soon thirty children were listening together under a mango tree. "
      "The headmaster says that the class is not as good as a real classroom, but that it kept the children learning.")
RB = ("**Passage 2: A letter to the editor** (invented)\n\n"
      "Dear Editor, some people say that school uniforms are a waste of money. I disagree. A uniform means that no child is judged by the clothes he wears, and it saves "
      "parents from buying new outfits every month. However, I do think that the price of uniforms is too high. Schools should allow parents to buy the cloth in the "
      "market and have it sewn by local tailors, which would cost far less. Surely this is a fair compromise.")
RC = ("**Passage 3: Preparing dried cassava** (invented)\n\n"
      "Mama Bih prepares dried cassava in four steps. First she peels and washes the roots. Next she grates them and presses out the water in a cloth. Then she spreads "
      "the paste on a mat in the sun and turns it every hour. Only when it is completely dry does she pack it in clean bags.")

P1 = [
    # ---- Section A: Reading comprehension (10)
    K("Which sentence best states the main idea of Passage 1?", "Teachers used the radio to keep pupils learning when schools were closed.", [
        ("Radio stations in Mamfe were closed by floods.", "The text says schools closed, not radio stations."), ("Parents refused to help younger children.", "Parents were asked to sit with younger children."), ("A mango tree fell on a school.", "The mango tree is only the meeting place.")],
      "The details show that the radio class replaced the closed school.", "Main ideas and supporting details", "Concept", "Which sentence covers the whole passage?", passage=RA),
    K("What can be inferred from 'thirty children were listening together under a mango tree'?", "Children without a radio at home could still take part.", [
        ("Every home had a radio.", "The passage says many homes had no radio."), ("The lessons were held in school.", "The class was on the radio."), ("The teacher was under the tree.", "The teacher read over the radio station.")],
      "Gathering around one set shows that some children had none at home.", "Inference and deduction", "Reasoning", "Why would thirty children share one set?", passage=RA),
    K("The headmaster's attitude to the radio class is", "positive but honest about its limits.", [
        ("angry and dismissive.", "He says it kept the children learning."), ("completely uncritical.", "He admits it is not as good as a classroom."), ("indifferent.", "He gives a considered view.")],
      "He praises the result and admits the weakness.", "Writer's purpose, point of view and attitude", "Interpretation", "Look at what he says about a real classroom.", passage=RA),
    K("In the passage, 'set' (in 'one set') means", "a radio receiver", [
        ("a group of tennis games", "That meaning does not fit a radio class."), ("a stage for a play", "That meaning does not fit."), ("to put something down", "It is used as a noun here.")],
      "'Gather around one set' refers to a radio receiver.", "Words and figures of speech in context", "Application", "What do neighbours gather around to hear a lesson?", passage=RA),
    K("What is the writer's main purpose in Passage 2?", "To argue that uniforms are useful but should be cheaper", [
        ("To describe how uniforms are sewn", "That is only a suggestion."), ("To announce a new school", "No school is announced."), ("To praise tailors", "Tailors are mentioned as part of the solution.")],
      "The writer defends uniforms and proposes a cheaper way.", "Writer's purpose, point of view and attitude", "Concept", "What does the writer want readers to accept?", passage=RB),
    K("The word 'However' in Passage 2 introduces", "a contrast with what has just been said", [
        ("an example of the idea", "However signals contrast."), ("a result of the idea", "However does not show result."), ("a repetition of the idea", "However does not repeat.")],
      "However shows that the writer now makes a point against the price.", "Discourse markers and cohesion", "Concept", "Does the next sentence agree or contrast?", passage=RB),
    K("Which statement is an assumption in the writer's proposal?", "Local tailors would charge less than shops do.", [
        ("Some people say uniforms waste money.", "That is stated in the passage."), ("The writer disagrees with the critics.", "That is stated."), ("Uniforms save parents from buying outfits.", "That is stated as a reason.")],
      "The cost saving depends on tailors being cheaper, which the writer assumes.", "Critical reasoning and evaluation", "Analysis", "Which idea is needed but not proved?", passage=RB),
    K("According to Passage 3, what does Mama Bih do immediately after grating the cassava?", "She presses out the water in a cloth.", [
        ("She packs it in bags.", "That is the last step."), ("She spreads it on a mat.", "That comes after pressing."), ("She peels the roots.", "That is the first step.")],
      "The order is peel and wash, grate, press, spread and turn, pack.", "Facts, opinions and sequence", "Recall", "Find the word Next.", passage=RC),
    K("When does Mama Bih pack the cassava?", "Only when it is completely dry", [
        ("As soon as it is grated", "She presses and dries it first."), ("After the first hour in the sun", "She turns it every hour until dry."), ("Before it is washed", "Washing is the first step.")],
      "The passage says only when it is completely dry.", "Facts, opinions and sequence", "Recall", "Find 'Only when'.", passage=RC),
    K("In Passage 3, 'paste' means", "a soft, wet mixture", [
        ("a kind of glue sold in shops", "That does not fit cooking."), ("to stick paper", "It is used as a noun."), ("a hard dry cake", "The paste is wet before drying.")],
      "Grated, pressed cassava is a soft mixture.", "Words and figures of speech in context", "Application", "What is the cassava like after grating?", passage=RC),
    # ---- Section B: Speech work (10)
    K("Which word has the same vowel sound as 'bird' /bɜːd/?", "heard", [("beard", "It has /ɪə/ (/bɪəd/)."), ("board", "It has /ɔː/ (/bɔːd/)."), ("bared", "It has /eə/ (/beəd/).")],
      "Heard is /hɜːd/ and shares /ɜː/.", "English consonant and vowel sounds", "Recall", "Say each word and compare the vowel."),
    K("Which word begins with the sound /ʃ/?", "sugar", [("sun", "It begins with /s/."), ("chin", "It begins with /tʃ/."), ("zoo", "It begins with /z/.")],
      "Sugar is /ˈʃʊɡə/.", "English consonant and vowel sounds", "Recall", "Think of the sound in 'she'."),
    K("Which word is transcribed /ʃɪp/?", "ship", [("sheep", "That is /ʃiːp/."), ("chip", "That is /tʃɪp/."), ("sip", "That is /sɪp/.")],
      "/ʃ/ + short /ɪ/ + /p/ is ship.", "Phonemic transcription", "Recall", "Is the vowel long or short?"),
    K("Which is the correct transcription of 'cough' in British English?", "/kɒf/", [("/kʌf/", "That is 'cuff' or 'rough' type of vowel."), ("/kəʊf/", "That vowel belongs to 'oaf' type words."), ("/kaʊf/", "That vowel is as in 'cow'.")],
      "Cough is /kɒf/.", "Phonemic transcription", "Recall", "Remember the vowel, not the spelling."),
    K("In which word is the second syllable stressed?", "compete", [("water", "Stress is on the first syllable."), ("happen", "Stress is on the first syllable."), ("garden", "Stress is on the first syllable.")],
      "Compete is /kəmˈpiːt/.", "Word stress", "Recall", "Tap the beat while saying each word."),
    K("In which sentence is the word 'record' stressed on its second syllable?", "We will record the match.", [("She broke the school record.", "A noun, stressed on the first syllable."), ("It is a world record.", "A noun, stressed on the first syllable."), ("The record is on the shelf.", "A noun, stressed on the first syllable.")],
      "As a verb, record is stressed on the second syllable.", "Word stress", "Application", "Is record a noun or verb in each sentence?"),
    K("In 'She wants to go to the market', which words normally carry the main stress?", "wants, go, market", [("she, to, the", "These are function words and are normally weak."), ("to, the, market", "Only market is a content word here."), ("she, to, market", "To is a function word.")],
      "Content words (wants, go, market) carry stress.", "Sentence stress and intonation", "Concept", "Which words carry the meaning?"),
    K("Which question normally has falling intonation?", "Where do you live?", [("Are you coming?", "A yes/no question usually rises."), ("Is this yours?", "A yes/no question usually rises."), ("Really? (showing surprise)", "Surprise usually rises.")],
      "Wh- questions usually fall.", "Sentence stress and intonation", "Concept", "Does the question start with a question word?"),
    K("'Want to' is often pronounced 'wanna' in fast speech. This is an example of", "reduction in connected speech", [("a minimal pair", "A minimal pair differs by one sound."), ("alliteration", "Alliteration repeats initial sounds."), ("word stress shifting", "Stress is not the point.")],
      "Sounds are weakened or joined when words run together.", "Connected speech and spelling of unknown words", "Concept", "How do words change when spoken fast?"),
    K("In which word is the letter k NOT pronounced?", "knife", [("kite", "The k is pronounced /k/."), ("kind", "The k is pronounced /k/."), ("key", "The k is pronounced /k/.")],
      "Knife is /naɪf/ with a silent k.", "Connected speech and spelling of unknown words", "Recall", "Say each word aloud."),
    # ---- Section C: Grammar (20)
    K("In 'She sings beautifully', the word 'beautifully' is a(n)", "adverb", [("adjective", "An adjective describes a noun."), ("noun", "It names nothing."), ("preposition", "It does not link a noun to another word.")],
      "It tells how she sings.", "Parts of speech", "Recall", "What question does the word answer?"),
    K("In 'I stayed home because it rained', which word is a conjunction?", "because", [("stayed", "A verb."), ("home", "Here an adverb or noun."), ("rained", "A verb.")],
      "Because links two clauses.", "Parts of speech", "Recall", "Which word joins the clauses?"),
    K("'There is too ___ noise in the room.'", "much", [("many", "Used with countable nouns."), ("few", "Used with countable nouns."), ("a few", "Used with countable nouns.")],
      "Noise is uncountable, so use much.", "Nouns and quantifiers", "Application", "Can you count noise?"),
    K("Which is the correct plural? 'The ___ are on the table.'", "knives", [("knifes", "Knife changes f to ves."), ("knive", "That is not a word."), ("knifs", "That is not a correct plural.")],
      "The plural of knife is knives.", "Nouns and quantifiers", "Recall", "Remember the f to v pattern."),
    K("'By the time we arrived, the match ___.'", "had started", [("has started", "A present perfect does not fit a past time."), ("starts", "A present tense does not fit."), ("is starting", "A present continuous does not fit.")],
      "The match started before we arrived: past perfect.", "Verbs: tense, mood, modals and voice", "Application", "Which action happened first?"),
    K("'You ___ park here; it is forbidden.'", "mustn't", [("needn't", "It means no need, not forbidden."), ("may", "It would give permission."), ("might", "It would express possibility.")],
      "Mustn't expresses prohibition.", "Verbs: tense, mood, modals and voice", "Application", "Is parking allowed?"),
    K("Which is the passive form of 'The teacher marked the scripts'?", "The scripts were marked by the teacher.", [("The scripts were marking by the teacher.", "The participle is wrong."), ("The scripts was marked by the teacher.", "The verb does not agree with scripts."), ("The scripts have been marked by the teacher.", "The tense changes to present perfect.")],
      "Passive: be (past plural) + past participle.", "Verbs: tense, mood, modals and voice", "Application", "Keep the tense and agree with scripts."),
    K("'I am tired,' said Ako. Which is correct reported speech?", "Ako said that he was tired.", [("Ako said that he is tired.", "In a past reporting, am normally becomes was."), ("Ako said that I was tired.", "The pronoun was not changed."), ("Ako said that he would be tired.", "That changes the meaning.")],
      "Am becomes was and I becomes he.", "Reported speech", "Application", "Change the tense and pronoun."),
    K("She asked, 'Where do you live?' Which is correct reported speech?", "She asked where I lived.", [("She asked where did I live.", "A reported question does not keep the inversion."), ("She asked where do I live.", "The question order and tense are not changed."), ("She asked where I living.", "The verb form is wrong.")],
      "Reported questions use statement order and move the tense back.", "Reported speech", "Application", "Reported questions are not questions."),
    K("'She enjoys ___ novels.'", "reading", [("to read", "Enjoy takes a gerund, not an infinitive."), ("read", "The base form is not correct here."), ("to reading", "To reading is wrong here.")],
      "Enjoy is followed by the -ing form.", "Gerunds, infinitives and participles", "Recall", "Which verbs take -ing?"),
    K("'Between you and ___, the plan will fail.'", "me", [("I", "After a preposition use the object form."), ("mine", "Mine is a possessive."), ("myself", "A reflexive form is not needed.")],
      "Between is a preposition and takes the object pronoun.", "Pronouns and determiners", "Application", "Which pronoun follows a preposition?"),
    K("Which sentence is a complex sentence?", "Although it rained, we played.", [("We played, and it rained.", "That is compound."), ("We played.", "That is simple."), ("Play now!", "That is a simple command.")],
      "It has a main clause and a subordinate clause.", "Sentence types", "Concept", "Look for a clause that cannot stand alone."),
    K("Which is a run-on sentence?", "The bus was late we walked home.", [("The bus was late, so we walked home.", "A conjunction joins the clauses correctly."), ("The bus was late; we walked home.", "A semicolon joins them correctly."), ("The bus was late. We walked home.", "Two separate sentences.")],
      "Two clauses are joined with no punctuation or conjunction.", "Agreement, fragments, run-on sentences and modifiers", "Analysis", "Which one lacks a joining device?"),
    K("Which sentence has a dangling modifier?", "Walking to school, the rain began.", [("Walking to school, Ako felt the rain begin.", "The modifier is clear."), ("As Ako walked to school, the rain began.", "It has a subject."), ("Ako walked to school, and the rain began.", "It is clear.")],
      "The rain is not the one walking.", "Agreement, fragments, run-on sentences and modifiers", "Analysis", "Who is walking?"),
    K("In 'The woman who lives next door is a nurse', 'who lives next door' is a", "relative (adjective) clause", [("noun clause", "It does not act as a noun."), ("adverbial clause", "It does not modify a verb."), ("main clause", "It cannot stand alone.")],
      "It describes the woman.", "Clauses", "Concept", "What does the clause describe?"),
    K("'If I ___ you, I would study harder.'", "were", [("am", "Unreal conditions use were."), ("will be", "Will is not used in an if-clause like this."), ("have been", "It does not fit the unreal condition.")],
      "Second conditional: if + were, would + base form.", "Clauses", "Application", "Is the situation real?"),
    K("'Of the three sisters, Ngum is the ___.'", "tallest", [("taller", "Comparative for two."), ("more tall", "Short adjectives take -er/-est."), ("most tallest", "Double superlative.")],
      "Three or more uses the superlative.", "Comparatives, conjunctions and word order", "Application", "How many are compared?"),
    K("Which sentence has the correct word order?", "She always arrives early.", [("She arrives always early.", "The adverb of frequency comes before the main verb."), ("Always she early arrives.", "The word order is unnatural."), ("She early always arrives.", "The word order is unnatural.")],
      "Adverbs of frequency go before the main verb.", "Comparatives, conjunctions and word order", "Concept", "Where does always go?"),
    K("'He gave a clear ___ of the rules.' (explain)", "explanation", [("explaining", "That is a participle or gerund."), ("explained", "That is a verb form."), ("explainer", "That is not the noun needed.")],
      "The noun form is explanation.", "Word forms", "Application", "A noun is needed after 'a clear'."),
    K("Which sentence is correctly punctuated?", "My brother, who lives in Buea, is a doctor.", [("My brother who lives in Buea, is a doctor.", "An unmatched comma."), ("My brother, who lives in Buea is, a doctor.", "The comma splits the verb."), ("My brother who, lives in Buea is a doctor.", "The comma is misplaced.")],
      "Commas enclose the extra information.", "Punctuation", "Application", "Where does the extra information start and end?"),
    # ---- Section D: Vocabulary (10)
    K("Which phrase is redundant?", "return back", [("return home", "Not redundant."), ("return soon", "Not redundant."), ("return quickly", "Not redundant.")],
      "Return already means come back.", "Word choice, redundancy and malapropism", "Concept", "Does one word repeat the meaning of another?"),
    K("A malapropism is", "the mistaken use of a word that sounds like the intended word but means something different.", [("a word with the same meaning as another.", "That is a synonym."), ("a word that is written the same but has two meanings.", "That is a homonym."), ("a comparison using like.", "That is a simile.")],
      "A malapropism confuses similar-sounding words.", "Word choice, redundancy and malapropism", "Recall", "Think of sound-alike mistakes."),
    K("Which word has the most negative connotation for 'thin'?", "skinny", [("slim", "Often positive."), ("slender", "Often positive."), ("lean", "Neutral or positive.")],
      "Skinny suggests too thin and is often unkind.", "Connotation and figures of speech", "Concept", "Which one sounds least kind?"),
    K("In 'achievement', the suffix -ment turns the verb into a", "noun", [("adjective", "-ment forms nouns."), ("adverb", "-ly forms most adverbs."), ("preposition", "A suffix does not make this.")],
      "Achieve + ment = a noun.", "Affixes and word formation", "Concept", "What does achievement name?"),
    K("Which expression is closest in meaning to 'scarce'?", "in short supply", [("plentiful", "That is the opposite."), ("very loud", "That is not related."), ("easy to see", "That is not related.")],
      "Scarce means hard to find.", "Synonyms, antonyms, homonyms and homophones", "Recall", "Is there a lot or a little?"),
    K("Which word is a homophone of 'knight'?", "night", [("knit", "It sounds different."), ("kite", "It sounds different."), ("knee", "It sounds different.")],
      "Knight and night sound the same.", "Synonyms, antonyms, homonyms and homophones", "Recall", "Say the words."),
    K("'The new rule will ___ all students.'", "affect", [("effect", "Mostly a noun meaning result."), ("infect", "It means to spread disease."), ("defect", "It means a fault.")],
      "Affect is the verb meaning to influence.", "Words often confused", "Application", "Which word means to influence?"),
    K("'To break the ice' means", "to begin a conversation in an awkward situation", [("to smash frozen water", "That is the literal meaning."), ("to break a rule", "It does not mean this."), ("to feel cold", "It does not mean this.")],
      "It is an idiom about easing tension.", "Idioms and figurative expressions", "Concept", "Is it literal?"),
    K("'The exam was a piece of cake.' This means the exam was", "very easy", [("a dessert", "That is literal."), ("a gift", "That is not meant."), ("very hard", "It means the opposite.")],
      "A piece of cake means easy.", "Idioms and figurative expressions", "Concept", "Is it about food?"),
    K("Which word is correctly spelled?", "necessary", [("neccessary", "Too many c's."), ("necesary", "Missing an s."), ("nessesary", "Wrong letters.")],
      "Necessary has one c and two s's.", "Spelling", "Recall", "Remember one collar and two sleeves."),
]
assert len(P1) == 50
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam B", lesson="enx2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 114)))

# ================================================================== Paper 2 skills check A (25 auto-markable parts)
EX_P2 = ("**Invented extract (not from a prescribed text)**\n\n"
         "Nchang stood at the edge of the farm and looked at the river, which had crept across the bean rows overnight. His father had always said that the "
         "river was a patient thief. He took off his shoes, rolled his trousers above the knee and stepped into the brown water to save what he could.")

P2 = [
    K("In Paper 2, how many of the four prescribed-text questions must you answer?", "One", [("Two", "Only one is required."), ("Three", "Only one is required."), ("All four", "Only one is required.")],
      "Four are set and one is answered.", "Writing about prescribed texts", "Recall", "Check the paper structure."),
    K("Which part of a question tells you what to DO?", "The command word", [("The title of the text", "It names the text."), ("The marks", "They tell you the value."), ("The page number", "It does not instruct.")],
      "Command words such as discuss, explain and compare give the task.", "Writing about prescribed texts", "Concept", "Think of verbs like discuss."),
    K("A question asks you to compare how two texts treat sacrifice. Which plan is best?", "Paragraphs by idea (similarity, difference), with both texts in each paragraph", [
        ("All of text one, then all of text two", "The comparison is weak."), ("Only text one", "Two texts are required."), ("A story of your own about sacrifice", "The question is on the texts.")],
      "Comparison paragraphs use both texts together.", "Writing about prescribed texts", "Application", "How do you compare?"),
    K("How long should you plan before writing a 45-minute essay?", "About five minutes", [("Forty minutes", "That leaves no time to write."), ("None", "Planning improves marks."), ("Twenty minutes", "That is too long.")],
      "Five minutes of planning is enough to organise an essay.", "Writing about prescribed texts", "Concept", "It is short but not zero."),
    K("Which is the best Point sentence for a paragraph on courage?", "The writer presents courage as the quality that keeps the character going when he has lost everything.", [
        ("There is a character.", "It makes no claim."), ("Courage is good.", "It is a general opinion."), ("The story is long.", "It is irrelevant.")],
      "A Point makes a claim that the evidence can prove.", "Writing about prescribed texts", "Application", "Which sentence makes a claim?"),
    K("Why must titles and authors be cited correctly?", "The examiner must know exactly which prescribed text you mean.", [
        ("It makes the essay longer.", "Length is not the aim."), ("It is only a spelling test.", "It is about accuracy of evidence."), ("It is optional.", "The Board's report criticised wrong citation.")],
      "Correct citation shows precise knowledge.", "Writing about prescribed texts", "Reasoning", "What does the examiner need to know?"),
    K("Which of these may be used as evidence in the prescribed-text essay?", "A moment from a prescribed text, paraphrased or with a few exact words", [
        ("A scene from a film you saw", "It is not a prescribed text."), ("A line from a famous novel not on the list", "Not prescribed."), ("A long passage from memory", "It may be inaccurate.")],
      "Only the prescribed texts count, quoted briefly.", "Writing about prescribed texts", "Concept", "What must the evidence come from?"),
    K("Read the invented extract. 'a patient thief' describes the river. This is", "a metaphor", [("a simile", "It has no like or as."), ("a rhyme", "It is not a rhyme."), ("an example of dialogue", "It is a description.")],
      "The river is called a thief.", "Prose", "Concept", "Look for like or as.", passage=EX_P2),
    K("In the extract, what does 'patient thief' suggest about the river?", "It takes slowly and quietly what belongs to the farmer.", [
        ("It is very fast.", "Patient suggests slow."), ("It is friendly to the farm.", "A thief is harmful."), ("It is dry.", "The river is flooding.")],
      "The two words combine slow action with loss.", "Prose", "Interpretation", "Combine the meanings of patient and thief.", passage=EX_P2),
    K("Change the first sentence of the extract's verbs to the simple present: 'Nchang stood at the edge of the farm.'", "Nchang stands at the edge of the farm.", [
        ("Nchang stood at the edge of the farm.", "It is unchanged."), ("Nchang standing at the edge of the farm.", "It is not a full sentence."), ("Nchang has stood at the edge of the farm.", "It is present perfect.")],
      "Stood becomes stands.", "Writing about prescribed texts", "Calculation", "Which verb changes?", passage=EX_P2),
    K("What is the best summary of the extract's message?", "Nature can take what people depend on, and they must still act.", [
        ("Rivers are always dangerous.", "It is too general."), ("Farmers should not wear shoes.", "It is a detail."), ("The father is wrong.", "The text does not say so.")],
      "A message is an idea.", "Prose", "Interpretation", "Which option is an idea?", passage=EX_P2),
    K("A play script shows a character saying 'I am fine' while stage directions say he cannot sit still. This reveals", "his real feelings differ from his words", [
        ("his love of dancing", "It does not suggest this."), ("a rhyme scheme", "It is not about rhyme."), ("the end of the play", "It does not signal the end.")],
      "Words and actions can contrast.", "Drama", "Interpretation", "Compare what is said and shown."),
    K("In essays about drama you should refer to", "the playwright and the audience", [("the narrator and the reader", "A play has no narrator."), ("the poet and the stanza", "Those are for poetry."), ("the chapter and the novelist", "Those are for novels.")],
      "Use terms suited to the genre.", "Drama", "Concept", "Who writes a play?"),
    K("A poem's second stanza begins with 'yet' after a sad first stanza. This usually marks", "a turn in thought or mood", [("a new poem", "It is part of the same poem."), ("the title", "It is not the title."), ("a rhyme", "It is a word of contrast.")],
      "Yet signals contrast.", "Poetry", "Analysis", "Yet means despite that."),
    K("Which is the best way to quote from a poem?", "A few exact words within your own sentence", [("Copy the poem", "It wastes time."), ("Quote and say nothing", "Explanation is needed."), ("Never quote", "Evidence is expected.")],
      "Short quotations followed by explanation.", "Poetry", "Application", "Be brief."),
    K("In the creative writing section, what is the required length?", "200 to 250 words", [("50 to 100 words", "Too short."), ("300 to 400 words", "Too long."), ("500 words or more", "That is for the composition.")],
      "The syllabus sets 200 to 250 words.", "Short stories and sketches", "Recall", "It is less than the composition."),
    K("A story of 14 handwritten lines has an average of 15 words a line. About how many words is that?", "210", [("29", "That adds the numbers."), ("150", "That is a guess."), ("300", "That multiplies wrongly.")],
      "14 x 15 = 210.", "Short stories and sketches", "Calculation", "Multiply lines by words."),
    K("Which opening is best for a short story?", "The lights went out the moment the examiner opened the first envelope.", [
        ("My name is Ako and I am writing a story.", "It tells instead of beginning the action."), ("There was once a very nice day.", "It is vague."), ("Many years ago, before anything happened, there was a girl.", "It is slow.")],
      "A good opening starts with action and a hint of trouble.", "Short stories and sketches", "Application", "Which one starts the trouble?"),
    K("Which is the best ending for a very short story that began with a mysterious envelope?", "A small detail that reveals who sent it", [("A paragraph explaining the moral", "It tells instead of shows."), ("A new unrelated mystery", "It leaves the story unfinished."), ("The words 'and so on'", "It is weak.")],
      "An ending should resolve or echo the opening.", "Short stories and sketches", "Reasoning", "Which closes the question?"),
    K("Which poem layout is acceptable for a 200 to 250 word poem?", "About ten four-line stanzas of roughly 22 words each", [("One line of ten words", "It is far too short."), ("A single paragraph of 500 words", "It is too long."), ("Two lines only", "It is too short.")],
      "10 x 22 = 220.", "Poems and plays", "Calculation", "Multiply stanzas by words."),
    K("Which is the correct way to write speech in a play script?", "TABI: (smiling) Then why is it on the table?", [("'Then why is it on the table?' said Tabi.", "That is story style."), ("Tabi says, \"Then why is it on the table?\"", "That is story style."), ("Then why is it on the table (Tabi)", "The speaker comes first.")],
      "Name, colon, direction, speech.", "Poems and plays", "Recall", "Look for name plus colon."),
    K("What should a report of a meeting contain first?", "The kind of meeting, place, date, time, chairperson and attendance", [("The closing time", "That comes at the end."), ("The writer's opinion", "Reports are factual."), ("A joke", "It is a formal document.")],
      "It begins with the details of the meeting.", "Reports of meetings and news reports", "Recall", "Think about the opening of a meeting."),
    K("Which sentence is correct reported speech in a meeting report?", "The chairman said that they would meet again the following week.", [
        ("The chairman said that they will meet again next week.", "Tense and time words not changed."), ("The chairman said, that we will meet.", "It mixes direct and reported speech."), ("The chairman says they met next week.", "It is inconsistent.")],
      "Will becomes would.", "Reports of meetings and news reports", "Application", "Move the tense back."),
    K("The first paragraph of a news report should", "give the main facts: who, what, where and when", [("give the reporter's opinion", "News is factual."), ("give the history of the town", "Background comes later."), ("list names only", "Names alone do not tell the story.")],
      "The most important facts come first.", "Reports of meetings and news reports", "Concept", "Think of the lead."),
    K("A student's creative piece is 280 words. What is the best action?", "Cut details so that it falls within 200 to 250 words.", [("Hand it in as it is.", "It exceeds the limit."), ("Add more to make it 400.", "That moves further from the limit."), ("Delete the title and nothing else.", "That would hardly change the count.")],
      "Edit to the required range.", "Short stories and sketches", "Reasoning", "What is the limit?"),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 skills check A", lesson="enx2-paper-2-strategy",
                         mock=True, time_limit_minutes=135, questions=build(P2, 115)))
