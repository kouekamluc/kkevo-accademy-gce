"""Practice sets for A Level Literature in English, Upper Sixth: Modern African Poetry Anthology (4 sets), Unseen Prose & Poetry Criticism (3 sets) and Examination
(Paper 1, Paper 2, Paper 3: 3 lesson sets), plus 'Paper 1 mock exam A' (50 multiple-choice questions across all four Upper Sixth modules), 'Paper 2 practice paper A'
(about 25 auto-markable parts on planning, choosing and technique) and 'Paper 3 practice paper A' (unseen prose and poem, about 20 parts).

Exam facts follow the Board's 2023 subject report (paraphrased). Facts about the set poems come from that report and are labelled "check your copy". All unseen passages,
poems, extracts and models are original and written for this course. Essays cannot be marked automatically, so the papers test planning, method and technique.
"""

import random

from .dsl import *  # noqa: F403

SETS = []


def K(prompt, right, wrongs, step, concept, skill, hint, feedback="", passage=""):
    """Question spec: the right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80
    return {"prompt": (passage + "\n\n" + prompt) if passage else prompt, "right": right, "wrongs": wrongs,
            "step": step, "concept": concept, "skill": skill, "hint": hint, "feedback": feedback}


def N(prompt, answer, step, concept, skill, hint, unit="", tol=0, passage=""):
    """Numeric question spec."""
    return {"num": True, "prompt": (passage + "\n\n" + prompt) if passage else prompt, "answer": answer, "unit": unit, "tol": tol,
            "step": step, "concept": concept, "skill": skill, "hint": hint}


def build(specs, seed):
    mcs = [sp for sp in specs if not sp.get("num")]
    n = len(mcs)
    pos = [i % 4 for i in range(n)]
    random.Random(seed).shuffle(pos)
    it = iter(pos)
    out = []
    for sp in specs:
        steps = [S("Reasoning", text=s) for s in ([sp["step"]] if isinstance(sp["step"], str) else sp["step"])]
        if sp.get("num"):
            out.append(NUM(sp["prompt"], sp["answer"], steps, tolerance=sp["tol"], unit=sp["unit"], concept=sp["concept"], skill=sp["skill"], hint=sp["hint"]))
            continue
        p = next(it)
        opts = [C(w, why=y) for w, y in sp["wrongs"]]
        opts.insert(p, C(sp["right"], correct=True))
        out.append(MC(sp["prompt"], opts, steps, concept=sp["concept"], skill=sp["skill"], hint=sp["hint"], feedback=sp["feedback"]))
    return out


def SET(module, topic, title, lesson, specs, seed, **kw):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed), **kw))


COURSE = ("literature-in-english", "upper-sixth")

M_POET = "Modern African Poetry Anthology"
M_UNSEEN = "Unseen Prose & Poetry Criticism"
M_EXAM = "Examination"
M_PROSE = "African & Post-Colonial Prose Fiction"
M_CHAUCER = "Geoffrey Chaucer & Canonical English Poetry"

T_READ = "Reading African poetry"
T_ORAL = "Oral tradition and poetic form"
T_SYMB = "Cultural symbolism and theme"
T_WRITE = "Writing about the anthology"
T_UPROSE = "Unseen prose"
T_UPOEM = "Unseen poetry"
T_PRAC = "Practical criticism under exam conditions"
T_P1 = "Paper 1"
T_P2 = "Paper 2"
T_P3 = "Paper 3"

# Topic titles of the other two Upper Sixth modules (used as mock-exam concept tags)
T_PR1 = "Reading African prose fiction"
T_PR2 = "Narrative perspective"
T_PR3 = "Post-colonial themes"
T_PR4 = "Writing about an African novel"
T_CH1 = "Chaucer's language and world"
T_CH2 = "The General Prologue"
T_CH3 = "The prescribed tale"
T_CH4 = "Metaphysical and Romantic poetry"
T_CH5 = "Victorian and Modernist poetry"

OWNCOPY = ("**Use your own copy.** The poems in the anthology and the set texts can change with the syllabus, and editions differ. This lesson gives a method "
           "and a few facts the Board's 2023 report states, written in our own words. Check every fact against your own copy and your teacher's notes before "
           "you use it in an exam.")

# ---- Original practice texts written for KKEVO Academy (invented; not from any anthology or past paper) ----
POEM_MARKET = ("**Evening Market** (an original practice poem written for this course)\n\n"
               "The traders fold their cloths away,\n"
               "And lamps are lit along the lane;\n"
               "The hands that bargained all the day\n"
               "Now count their coins and count their pain.\n\n"
               "A girl sweeps peel and broken stalks\n"
               "Into a pile beside the wall;\n"
               "She hums a tune that no one talks\n"
               "About, and yet it carries all.\n\n"
               "Yet when the final lamp burns low\n"
               "And only stars are left to see,\n"
               "She lifts her basket, turns to go,\n"
               "And hums the tune: it sets her free.")

POEM_QUEUE = ("**Morning Queue at the Tap** (an original practice poem written for this course)\n\n"
              "Before the cocks have finished their argument,\n"
              "the yellow jerrycans are already lined up,\n"
              "a row of small round loyalties\n"
              "waiting for the tap to clear its throat.\n"
              "Nobody speaks of the hour.\n"
              "An old woman counts her breath;\n"
              "a boy kicks a stone, and the stone\n"
              "rolls on into the dark ahead of him.\n"
              "When the water comes it comes like a rumour,\n"
              "thin, then thick, then everywhere,\n"
              "and all the faces lean towards it\n"
              "as towards a late and welcome guest.")

PROSE_RETURN = ("**The Return** (an original practice passage written for this course)\n\n"
                "I came back to the compound after six years and found that the mango tree had grown taller than the roof. My mother met me at the gate with "
                "both hands out, and for a moment neither of us said anything, because the words we had saved were too small for the afternoon. Behind her the "
                "yard was exactly as I had kept it in my mind: the three-legged stool, the blackened pot, the chickens pretending not to notice me. Only I had "
                "changed, and the change made me shy in my own father's house.\n\n"
                "At supper my uncle asked what I had learned in the city. I told him about lectures and libraries and the long, polite silences of strangers. "
                "He nodded slowly, the way he nodded at weather. 'And did the city teach you to sit with your family,' he said, 'or only to visit them?' Nobody "
                "laughed. I looked down at my plate and, for the first time in six years, felt that I had been asked a question worth answering.")

PROSE_PATH = ("**The Path at Mbelu** (an original practice passage written for this course; the village and people are invented)\n\n"
              "The women of Mbelu had carried water along the same path for as long as anyone could remember, so nobody was ready for the morning Pa Ngwa put "
              "a fence across it. He stood beside his new wire, arms folded, and said that the path crossed his land and he wanted it back.\n\n"
              "By noon the whole village had gathered under the mango tree. Voices rose. One young man called the old farmer a thief of the common good, and "
              "Pa Ngwa answered that he was only a man who had kept quiet for forty years. Then Mama Ewane, who had said nothing, raised her hand and waited "
              "until the noise thinned. 'Pa Ngwa,' she said, 'you are right that the path is on your land, and we are right that our mothers walked it. Let "
              "each side say what it fears.'\n\n"
              "Pa Ngwa admitted, with a grudging cough, that his goats had been stolen twice by strangers who used the path in the dark. The women admitted "
              "that the next tap was an hour away. In the end it was the children's idea that settled it: a gate, which the women would close behind them every "
              "evening, and a small stone bench at the wire where anyone could rest.\n\n"
              "When the meeting broke up, nobody looked victorious, but the water still came home before the sun was high.")


# ================================================================== 1. Reading African poetry
SET(M_POET, T_READ, "Reading African poetry: background and method", "liu2-reading-african-poetry", [
    K("Which anthology does the Board's 2023 report name as the poetry text in Paper 2 for both the old and the new syllabus?", "Poems of Black Africa", [
        ("The Penguin Book of Modern African Poetry", "That is a different anthology, not the one the report names."),
        ("Selected Poems of John Keats", "The report lists Keats as a separate Section C text under the new syllabus."),
        ("The Rape of the Lock", "That was an old-syllabus poem by Pope, not the African anthology.")],
      "The report names Poems of Black Africa, edited by Wole Soyinka, in both syllabuses.", "Reading African poetry", "Recall", "Think of the anthology edited by Wole Soyinka."),
    K("What does the report say about how Paper 2 questions on the anthology are usually set?", "They are not tied to particular poems, so candidates choose relevant ones", [
        ("Each question names the one poem to discuss", "The report says the opposite: questions are not tied to particular poems."),
        ("They ask only about the poets' lives", "The questions are about themes, devices and beliefs shown in poems."),
        ("They use unseen poems only", "Unseen poems belong to Paper 3.")],
      "A free choice of poems favours the candidate who knows many poems well.", "Reading African poetry", "Recall", "Why would a free choice help only a well-prepared student?"),
    K("Which set of ideas does the report list as background for the anthology?", "Colonialism, assimilation, Negritude, apartheid, the African personality and neo-colonialism", [
        ("Romanticism, realism, naturalism and modernism", "These are European movements, not the background the report lists."),
        ("Feudalism, chivalry, courtly love and medicine", "The report links these to Chaucer's work."),
        ("The American Dream, class consciousness and identity", "The report links these to a drama text.")],
      "Each of the six ideas affects what the poems say.", "Reading African poetry", "Recall", "Which list refers to African history of the twentieth century?"),
    K("A poem is addressed to a dead grandfather. Which question of the five-question method does this answer?", "To whom?", [
        ("Who speaks?", "That asks about the voice, here the grandchild, not the person addressed."),
        ("How?", "That asks about techniques, such as diction or imagery."),
        ("So what?", "That asks about theme and effect.")],
      "The addressee is the person spoken to.", "Five-question method", "Concept", "Whom is the speaker talking to?"),
    K("In the five-question method, which two questions mainly lead you from meaning to criticism?", "How? and So what?", [
        ("Who speaks? and To whom?", "These identify the voice and the listener."),
        ("About what? and To whom?", "These identify subject and listener."),
        ("Who speaks? and About what?", "These give situation, not technique or effect.")],
      "Criticism asks how the poet does it and why it matters.", "Five-question method", "Concept", "Which questions ask about technique and effect?"),
    K("The report describes Kunene's 'The Bond' as including a grinding stone handed to a successor with a warning of curses if it is defiled. What does this show about the poem's treatment of the ancestors?", "They are still concerned for the living and punish neglect of their legacy", [
        ("They are forgotten once they die", "The poem warns the living not to forget the dead."),
        ("They have no power over the living", "The curses show that they have power."),
        ("They are mocked by the poet", "The tone is solemn and respectful, not mocking.")],
      "The stone and the curse together show a bond of duty between living and dead.", "The Bond: ancestors and duty", "Application", "What does the threat of a curse imply?"),
    K("A student writes a long paragraph retelling the story told in a poem, without linking it to the question. According to the report, what is the main fault?", "Narration that ignores the terms of the question", [
        ("Too many quotations", "The report's complaint is about narration without focus."),
        ("Too much attention to metre", "The report does not say this."),
        ("Poor handwriting only", "Handwriting is a separate concern.")],
      "The report lists vague accounts that ignored the question as a key fault.", "Common faults", "Reasoning", "What does 'ignored the terms of the question' mean?"),
    K("A student knows only two poems well. Why is this risky for the anthology question?", "Neither poem may fit the theme, or the question may ask for three poems", [
        ("The examiner will mark only two poems", "The risk is not about how many are marked but how few fit the question."),
        ("Questions are tied to exactly those two poems", "Questions are not tied to particular poems."),
        ("Two poems are the maximum allowed", "There is no such limit; some questions ask for three poems.")],
      "A free choice only helps a candidate who has a wide choice.", "Common faults", "Application", "What if the question asks for three poems?"),
], 101)

# ================================================================== 2. Oral tradition and poetic form
SET(M_POET, T_ORAL, "Oral tradition and form: features and effects", "liu2-oral-tradition-poetic-form", [
    K("Which of these is an oral prose form?", "A folktale", [
        ("A dirge", "A dirge is a song of mourning, an oral poetic form."),
        ("A praise-song", "That is an oral poetic form."),
        ("An ode", "An ode is a written lyric form.")],
      "Folktales are spoken stories told for entertainment and teaching.", "Oral forms", "Recall", "Which one is a story, not a song or poem?"),
    K("What is call and response?", "A leader's line answered by a chorus or audience", [
        ("The repetition of consonant sounds at the start of words", "That is alliteration."),
        ("A poem addressed to a dead person", "That is apostrophe."),
        ("A line that runs on to the next line", "That is enjambment.")],
      "In performance the audience takes part.", "Oral features", "Recall", "Think of a leader and a crowd."),
    K("A poet writes: 'Grandfather, I still hear your cough in the night.' Which device is used?", "Apostrophe", [
        ("Simile", "No comparison with 'like' or 'as' is used."),
        ("Onomatopoeia", "No sound is imitated by a word."),
        ("Irony", "There is no contrast between what is said and what is meant.")],
      "The speaker addresses a person who is absent or dead.", "Apostrophe", "Application", "Is the person addressed present?"),
    K("What does the Board's report say apostrophe is typically used for?", "Emotional effect", [
        ("Rhyme", "The report links apostrophe to feeling, not rhyme."),
        ("Giving factual information", "Apostrophe expresses emotion."),
        ("Showing the metre", "Metre has no link to apostrophe.")],
      "The report calls it a device often used for emotional effect.", "Apostrophe", "Recall", "What does a speaker gain by calling to the dead?"),
    K("Which feature of oral praise poetry is shown in 'Nkeng of the early hoe, Nkeng of the patient rows'?", "Repetition of the name with praise titles", [
        ("A rhyme scheme of ABAB", "These lines do not rhyme."),
        ("A shift of tone", "The mood stays celebratory."),
        ("A metaphor about money", "The lines contain no money image.")],
      "Praise poems build a portrait through repeated epithets.", "Praise poetry", "Application", "What repeats?"),
    K("Which statement about free verse is correct?", "It has no fixed rhyme or metre but uses line breaks, repetition and sound for rhythm", [
        ("It has no craft", "Line breaks, repetition and sound still shape it."),
        ("It always rhymes ABAB", "Free verse has no fixed rhyme scheme."),
        ("It must have fourteen lines", "That describes a sonnet.")],
      "Free verse is shaped by speech and breath, not by fixed patterns.", "Free verse", "Concept", "What does 'free' mean here?"),
    K("A candidate writes: 'The poet uses repetition.' What must be added to earn marks?", "A quotation and an explanation of the effect", [
        ("The poet's birth date", "Biography does not show effect."),
        ("A longer list of other devices", "A list of names without effects earns little."),
        ("A summary of the plot", "A summary does not explain a device.")],
      "Name, quote, explain the effect.", "Effect of devices", "Reasoning", "What question follows 'The poet uses...'?"),
    K("Why do poets writing in English still use oral features such as repetition and direct address?", "To keep an African voice and rhythm and the spirit of ceremony", [
        ("Because English has no rhythm of its own", "English has its own rhythms; the aim is to carry African voice into it."),
        ("Because oral poems have no meaning", "Oral poems carry deep meaning."),
        ("Because the Board requires it", "It is a matter of poetic choice, not a rule.")],
      "Oral habits help memory, involve listeners and keep the performance feeling.", "Oral tradition in modern poetry", "Reasoning", "What do spoken forms bring into a written poem?"),
], 102)

# ================================================================== 3. Cultural symbolism and theme
SET(M_POET, T_SYMB, "Symbols and themes in the anthology", "liu2-cultural-symbolism-theme", [
    K("What is a symbol?", "An object, creature or action that stands for an idea beyond itself", [
        ("A word that sounds like what it means", "That is onomatopoeia."),
        ("A line repeated at intervals", "That is a refrain."),
        ("A comparison using 'like' or 'as'", "That is a simile.")],
      "A symbol keeps its literal meaning but also stands for an idea.", "Symbolism", "Recall", "What does a symbol carry besides its literal meaning?"),
    K("According to the report, which poem includes a boatman, a bird and a lake of blood?", "'Agony' by Tchicaya U Tam'si", [
        ("'Olokun' by J. P. Clark", "'Olokun' is about a sea goddess and her lovers."),
        ("'The Bond' by Mazisi Kunene", "'The Bond' is about a grinding stone."),
        ("'Cold' by Dennis Brutus", "'Cold' is about prison conditions.")],
      "The report describes the boatman as the poet and the bird as a guide across a lake of blood.", "Poems in the report", "Recall", "Which poet is from Congo?"),
    K("What does the grinding stone in 'The Bond' stand for, according to the report's description?", "The ancestor's legacy and the duty of the living", [
        ("The wealth of the village", "The stone is cherished for its link to the ancestor, not for wealth."),
        ("The cruelty of colonial rulers", "The poem is not about colonial cruelty."),
        ("The speaker's childhood", "The stone is passed in a succession ritual, not recalled from childhood.")],
      "The stone is passed from Masilela to Gumede with a warning.", "Cultural symbols", "Interpretation", "Why must the stone be kept sacred?"),
    K("Which pair of poems does the report link with the idea that 'the dead are not dead'?", "'Breath' and 'Vanity' by Birago Diop", [
        ("'Rulers' and 'Upheaval' by Dipoko", "These are satirical poems about rulers."),
        ("'Cold' and 'The Sounds Begin Again' by Brutus", "These deal with prison and apartheid."),
        ("'Phlora' and 'The Right Road'", "These deal with moral decline and false values.")],
      "The report names Diop's two poems among those about the living dead.", "The living dead", "Recall", "Which poet is from Senegal and writes of ancestors in the wind and trees?"),
    K("What is disillusionment?", "The painful loss of hope and trust after disappointment", [
        ("A celebration of independence", "Disillusionment is the opposite: disappointment."),
        ("A mood of calm acceptance", "It is bitter, not calm."),
        ("A rhyming pattern", "It is a mood, not a form.")],
      "The term describes the poets' disappointed hopes about rulers and society.", "Disillusionment", "Concept", "What happens to hope?"),
    K("The report suggests that a strong answer on poets' dissatisfaction with their societies would also:", "Argue that the poets keep hope and celebrate cultural identity", [
        ("Ignore poems from South Africa", "The report names South African poets among the examples."),
        ("Avoid mentioning any poem", "Poems are the evidence."),
        ("List only poems about sadness", "That would be one-sided.")],
      "The report describes the counter-argument as part of a good answer.", "Balanced argument", "Reasoning", "What does a good candidate add to the case for protest?"),
    K("A candidate says 'In \"Rulers\", Dipoko criticises the rulers' and gives no details. What is missing?", "Evidence from the poem and an explanation of its effect", [
        ("The poet's date of birth", "Biography is not the missing evidence."),
        ("A list of other poets", "More names do not prove this claim."),
        ("An introduction in French", "Language of the introduction is not the issue.")],
      "The report describes rulers who feast, boast and squander funds while the poor suffer; a claim needs such proof.", "Balanced argument", "Application", "What would convince the examiner?"),
    K("Which statement shows respect and exactness when writing about traditional beliefs in poems?", "'The poem presents the belief that the dead protect the living.'", [
        ("'Africans are superstitious.'", "This is a prejudiced generalisation, not literary analysis."),
        ("'The poem is about Africa.'", "It is too vague to earn marks."),
        ("'Ancestors do not exist.'", "An essay reports what the poem presents, not whether beliefs are true.")],
      "Use 'the poem presents' and 'the belief that' to stay accurate and fair.", "Writing about beliefs", "Reasoning", "Which sentence reports what the poem does?"),
], 103)

# ================================================================== 4. Writing about the anthology
SET(M_POET, T_WRITE, "Writing anthology essays: plans and conventions", "liu2-writing-about-anthology", [
    K("Which is the correct way to present the title of a single poem?", "In quotation marks", [
        ("Underlined", "Underlining is for titles of collections, novels and plays."),
        ("In capitals only", "Capitals alone do not mark a title."),
        ("Not marked at all", "The report lists this convention as one to follow.")],
      "Poem titles go in quotation marks.", "Presentation conventions", "Recall", "Compare poem titles with collection titles."),
    K("A question asks: 'Show how the idea that the dead are not dead is sustained in three poems of your choice.' What is the command and focus?", "Show how; the belief sustained in three poems", [
        ("Discuss; the life of the poet", "The focus is the belief, not the poet's life."),
        ("List; any poem you like", "The question asks you to show how, and to link to the belief."),
        ("Compare; two poems", "The number of poems is three.")],
      "Underline the command, the focus and the number of poems.", "Reading the question", "Concept", "What number of poems is asked?"),
    K("Which is the best topic sentence for a paragraph on 'The Bond'?", "In 'The Bond', Kunene makes a grinding stone a symbol of the ancestor's authority over the living.", [
        ("'The Bond' is a poem.", "It makes no claim about the question."),
        ("Kunene was a poet.", "It gives a fact about the poet, not a claim about the poem."),
        ("Stones are hard.", "It is not about the poem.")],
      "A topic sentence makes a claim that the paragraph will prove.", "Paragraph structure", "Application", "Which sentence makes a claim you can prove?"),
    K("According to the report, what do more full and focused illustrations in a paragraph earn?", "A better impression and a higher mark", [
        ("A lower mark because the paragraph is long", "The report says fuller paragraphs score better."),
        ("No change in the mark", "The report says one sketchy illustration earns a skimpy mark."),
        ("A penalty for repetition", "Focused illustration is rewarded, not penalised.")],
      "One sketchy bit of evidence earns a skimpy mark.", "Paragraph structure", "Recall", "What does the report say about one sketchy illustration?"),
    K("A candidate answers five questions when four are required, hoping the best will be chosen. According to the report, what happens?", "The answers are shallow and marks are wasted", [
        ("All five are marked and the best four counted", "The report calls this belief erroneous."),
        ("The paper is disqualified", "The report does not say that."),
        ("The extra answer earns bonus marks", "It does not.")],
      "The report says candidates who do this lose valuable marks.", "Instructions and rubrics", "Application", "Where does the candidate's time go?"),
    K("A question asks for apostrophe in three poems. Which plan fits best?", "Define apostrophe; choose three poems; for each give who is addressed, the words, and the effect", [
        ("Retell three poems in order", "A retelling does not discuss apostrophe."),
        ("Write about the poets' childhood", "Biography is not the focus."),
        ("Discuss rhyme in every poem", "The device asked about is apostrophe.")],
      "The plan must follow the device and the number of poems.", "Planning an answer", "Reasoning", "What three things should each paragraph give?"),
    K("Which conclusion best fits the question 'To what extent do poets present the past as a source of strength?'", "A judgement saying it is largely so, but that the strength depends on the living keeping faith with the past", [
        ("A new topic about modern technology", "A conclusion must not start a new topic."),
        ("A copy of the introduction word for word", "A conclusion should give a judgement, not repeat."),
        ("A list of poems with no comment", "A list does not answer 'to what extent'.")],
      "A conclusion gives a final judgement with a logical close.", "Introductions and conclusions", "Evaluation", "What does 'to what extent' demand?"),
    K("A quotation from a poem runs to six lines. According to the report, how should it be presented?", "Indented or centred", [
        ("Run on in the paragraph", "The report says quotations over four lines should be set off."),
        ("Written in capitals", "Capitals are not required."),
        ("Left out of the essay", "Quotations are allowed but must be presented correctly.")],
      "The report names indentation or centring for quotations longer than four lines.", "Presentation conventions", "Recall", "What does the report say about quotations over four lines?"),
], 104)

# ================================================================== 5. Unseen prose
RADIO = ("**Invented passage (practice only)**\n\n"
         "Atem had repaired radios in the same stall for thirty years. Customers called him slow; he called himself careful. When a boy brought in a broken set "
         "and begged for it by evening, Atem lifted his glasses, studied the boy's anxious face, and said, 'A radio that is hurried will only break again.' The boy "
         "left grumbling, but he returned the next day and found the set singing.")
SET(M_UNSEEN, T_UPROSE, "Unseen prose: context, citation and attitude", "liu2-unseen-prose", [
    K("What does 'meaning in context' require?", "A meaning that fits the passage, in a word or phrase of the same kind", [
        ("Every dictionary meaning of the word", "Only the meaning that fits the passage is wanted."),
        ("The same word repeated", "Repeating the word shows no understanding."),
        ("A translation into another language", "No translation is asked for.")],
      "The meaning must make sense in the lines around it.", "Meaning in context", "Concept", "Why does the term include the word 'context'?"),
    K("In the passage, what does 'anxious' mean in 'the boy's anxious face'?", "Worried and uneasy", [
        ("Calm and relaxed", "That is the opposite of anxious."),
        ("Angry and shouting", "The boy begged, which suggests worry, not anger."),
        ("Sleepy and bored", "Nothing in the passage suggests boredom.")],
      "The boy begged for the repair by evening, which shows he was worried.", "Meaning in context", "Application", "Why would a boy beg for a quick repair?", passage=RADIO),
    K("Which phrase of not more than two words shows the boy's reaction as he left the shop?", "'left grumbling'", [
        ("'the next day'", "This is a time phrase, not an attitude."),
        ("'begged for it'", "This happened earlier and has three words."),
        ("'the set singing'", "This describes the radio, not the boy.")],
      "'Grumbling' shows annoyance; the phrase is exactly two words.", "Citation and attitude", "Application", "Count the words and ask whose attitude is shown.", passage=RADIO),
    K("How should a citation be written?", "The exact words inside quotation marks, as short as the question allows", [
        ("A paraphrase in your own words", "That is not a citation."),
        ("The whole paragraph", "A long chunk breaks the length limit."),
        ("A summary of the passage", "A summary does not answer 'which words?'.")],
      "The report says many candidates lifted chunks without quotation marks.", "Citation and attitude", "Recall", "What does the report say about citing?"),
    K("Which skill does Atem show when he refuses to hurry the repair?", "Patience in keeping a high standard of work", [
        ("Carelessness", "He is called careful, not careless."),
        ("Anger at customers", "He speaks calmly."),
        ("Greed for money", "Nothing suggests he wants more money.")],
      "He explains that a hurried radio will break again.", "Response tasks", "Reasoning", "What does his proverb suggest about quality?", passage=RADIO),
    K("What figure of speech is 'found the set singing'?", "Personification", [
        ("Simile", "No 'like' or 'as' is used."),
        ("Alliteration", "No repeated initial sounds are the point."),
        ("Oxymoron", "No two contradictory words are joined.")],
      "A radio is given a human action: it sings.", "Figures of speech", "Concept", "Does a radio sing literally?", passage=RADIO),
    K("What is the tone of the last sentence?", "Quietly satisfied, with a hint of humour", [
        ("Bitter and angry", "The boy's grumbling is mild and turns to success."),
        ("Fearful", "Nothing frightens the characters."),
        ("Formal and cold", "The ending is warm.")],
      "The boy returns and finds the radio working.", "Attitude and tone", "Interpretation", "How does the story end for the boy?", passage=RADIO),
    K("Before you answer any question on an unseen prose passage, what should you do first?", "Read the passage twice: once for sense, once for feeling words and shifts", [
        ("Start with the last question", "A first reading for sense prevents misreading."),
        ("Copy the opening sentence", "Copying does not answer a question."),
        ("Look for the longest word", "Length of word has no link to meaning.")],
      "Two reads give both the story and the details.", "Reading method", "Concept", "How many reads does the lesson recommend?"),
], 105)

# ================================================================== 6. Unseen poetry
HARMATTAN = ("**Harmattan Morning** (invented for practice)\n\n"
             "Dust hangs above the waking street,\n"
             "The sun a coin of pallid gold;\n"
             "A hawker sings of bread to eat,\n"
             "And children shiver in the cold.")
SET(M_UNSEEN, T_UPOEM, "Unseen poetry: rhyme, metaphor, sound and form", "liu2-unseen-poetry", [
    K("What is the rhyme scheme of 'Harmattan Morning'?", "ABAB", [
        ("AABB", "The first two lines (street, gold) do not rhyme with each other."),
        ("ABBA", "The first and fourth lines (street, cold) do not rhyme."),
        ("ABCB", "The third line (eat) rhymes with the first, so it is not a new sound.")],
      "Street and eat rhyme (A, A); gold and cold rhyme (B, B). In order: A B A B.", "Rhyme scheme", "Calculation", "Give each line-end a letter in order.", passage=HARMATTAN),
    K("What does 'pallid' most likely mean in 'The sun a coin of pallid gold'?", "Pale and dim", [
        ("Bright and blazing", "A dusty sky makes the sun look dim, not blazing."),
        ("Heavy and solid", "Pallid describes colour, not weight."),
        ("Warm and golden red", "The sun is likened to a coin of pale gold.")],
      "Dust in the air makes the sun look faint.", "Words in context", "Application", "What does dust do to sunlight?", passage=HARMATTAN),
    K("The sun is described as 'a coin of pallid gold'. What technique is this?", "Metaphor", [
        ("Simile", "The comparison has no 'like' or 'as'."),
        ("Onomatopoeia", "No sound is imitated."),
        ("Apostrophe", "No one is addressed.")],
      "The sun is said to be a coin, a direct comparison.", "Metaphor", "Concept", "Is there a joining word such as 'like'?", passage=HARMATTAN),
    K("What does the metaphor of a pale gold coin suggest about the sun?", "It is small, flat and weak, like a coin seen through dust", [
        ("It is blazing hot", "A pale coin suggests little warmth."),
        ("It is very large and close", "A coin is small and flat."),
        ("It has disappeared", "The sun is still visible, though weakened.")],
      "A coin is a small, flat, shiny disc.", "Metaphor", "Interpretation", "What are the features of a coin?", passage=HARMATTAN),
    K("How many syllables does each line of 'Harmattan Morning' have?", "Eight", [
        ("Six", "Count 'Dust-hangs-a-bove-the-wak-ing-street': that is eight."),
        ("Ten", "The lines are shorter than ten."),
        ("Seven", "Each line has eight when counted carefully.")],
      "The lines are iambic tetrameter: four feet of two syllables.", "Metre", "Calculation", "Tap out the beats on a line.", passage=HARMATTAN),
    K("A candidate says the rhyme gives the poem 'a song-like, steady feeling that matches a calm morning routine'. What skill does this show?", "Commenting on the effectiveness of the rhyme scheme", [
        ("Identifying the rhyme scheme only", "The comment goes beyond naming the pattern."),
        ("Giving the meaning of a word", "No word is explained."),
        ("Writing a creative stanza", "This is analysis, not creation.")],
      "The report says candidates found schemes but not effects.", "Rhyme scheme", "Reasoning", "What do the rhyme and rhythm do for the mood?"),
    K("Which is the best opening for a six-line poem on a similar situation?", "Six short lines with end rhyme and one clear image, such as a street at dawn", [
        ("A paragraph of prose in six lines", "The report says prose broken into lines is not a poem."),
        ("A list of facts about the weather", "A list lacks image and shape."),
        ("One long sentence with no line breaks", "A poem needs lines and form.")],
      "Choose a form and an image and keep lines roughly equal.", "Creative response", "Application", "What does the report say about prose in six lines?"),
    K("In the lesson poem 'Evening Market', the third stanza begins with 'Yet'. What does this word signal?", "A turn from tiredness to quiet hope", [
        ("A change from poem to prose", "The form does not change."),
        ("The end of the rhyme scheme", "The scheme continues."),
        ("A new speaker", "The same observer speaks.")],
      "'Yet' signals a turn in mood.", "Shifts of tone", "Interpretation", "Think about how the girl's night ends."),
], 106)

# ================================================================== 7. Practical criticism under exam conditions
SET(M_UNSEEN, T_PRAC, "Practical criticism: routine, shifts and unity", "liu2-practical-criticism-exam", [
    K("What is step 3 of the six-step routine?", "Mark the shifts of mood, subject, time or viewpoint", [
        ("Read for sense", "That is step 1."),
        ("Form and voice", "That is step 2."),
        ("Answer each task", "That is step 6.")],
      "The steps are sense, form and voice, shifts, images and sounds, structure and unity, tasks.", "Six-step routine", "Recall", "Count in order."),
    K("Which of these usually signals a shift of tone?", "A connective such as 'but' or 'yet' at the start of a line", [
        ("A full stop", "A full stop ends a sentence but does not turn the mood."),
        ("A long title", "Title length has no link to tone."),
        ("A capital letter", "A capital marks a line or sentence start only.")],
      "Connectives often mark a turn in the thought.", "Shifts", "Concept", "Which word changes direction?"),
    K("What is an imagery pattern?", "A group of related images repeated through a text to build a theme", [
        ("A single simile", "One image is not a pattern."),
        ("A rhyme scheme", "Rhyme is a sound pattern."),
        ("The poem's title", "The title is a part of the poem but not a pattern.")],
      "A pattern is a recurring family of images, such as light or water.", "Imagery patterns", "Concept", "What does 'pattern' imply?"),
    K("A candidate calls the speaker of a poem 'the poet' and says the poet lost a brother. What is the main risk?", "Assuming the speaker is the poet without evidence", [
        ("Using too many adjectives", "That is not the risk here."),
        ("Quoting too much", "The risk is biographical assumption."),
        ("Ignoring the rhyme", "Rhyme is not the issue.")],
      "The speaker is a created voice or persona.", "Form and voice", "Reasoning", "Does the poem say the speaker is the poet?"),
    K("Which evidence best supports the unity of a poem?", "A closing line that returns to the opening image and idea", [
        ("A long first stanza", "Length alone is not unity."),
        ("The poet's reputation", "Reputation is not evidence in the poem."),
        ("The use of capital letters", "Capital letters have no link to unity.")],
      "Return and repetition create the feeling of completeness.", "Structure and unity", "Application", "What shows that the end belongs to the beginning?"),
    K("In 'The Kettle' (lesson poem), which word marks the shift from sound to silence?", "'Then'", [
        ("'sings'", "That belongs to the sound before the shift."),
        ("'saint'", "That belongs to the metaphor in the first part."),
        ("'steam'", "That belongs to the silence after the shift.")],
      "'Then' begins the fourth line, where the mood turns.", "Shifts", "Application", "Where does the noise end?"),
    K("A candidate lists alliteration, assonance and rhyme in a poem and stops. Why does this earn little?", "It names devices without explaining their effect on meaning", [
        ("The devices are not allowed in answers", "They are allowed; the problem is the lack of explanation."),
        ("The list is too short", "The problem is not the length."),
        ("The devices are not in the poem", "The problem is the missing effect.")],
      "Each device must be linked to feeling or meaning.", "Critical comment", "Reasoning", "What question follows every device you name?"),
    K("Why should you never leave the creative six-line task for the last minute?", "It tests form and imagination and needs planning to be poetry rather than prose", [
        ("It is optional and carries no marks", "The report treats it as part of the paper."),
        ("It needs no thought", "The report says most candidates failed because they wrote prose."),
        ("Examiners do not read it", "Examiners read and credit it.")],
      "A short poem needs a form, an image and an ending.", "Time plan", "Evaluation", "What did the report say most scripts did wrong in this task?"),
], 107)

# ================================================================== 8. Paper 1 strategy
SET(M_EXAM, T_P1, "Paper 1 strategy: structure and method", "liu2-paper-1-strategy", [
    K("According to the Board's 2023 report, how many questions are in Paper 1?", "Fifty multiple-choice questions", [
        ("Twenty-five", "Twenty-five is half of the actual number."),
        ("Forty", "Forty is the number of set-text questions only."),
        ("Sixteen", "Sixteen is the number of essay questions in Paper 2 in 2023.")],
      "The paper has fifty questions: ten general and forty on set texts.", "Paper 1 structure", "Recall", "Add the general and the text questions."),
    K("How many of the Paper 1 questions are general literary appreciation questions common to all candidates?", "Ten", [
        ("Four", "Four is the number of questions per text."),
        ("Twenty", "The report says ten."),
        ("Forty", "Forty is the number of text-bound questions.")],
      "The first ten questions are general.", "Paper 1 structure", "Recall", "Fifty minus forty."),
    N("The Board's report says Paper 1 has 40 set-text questions, with exactly four per text. For how many texts are questions set?", 10, "40 divided by 4 gives 10 texts.", "Paper 1 structure", "Calculation", "Divide the number of text questions by the number per text.", tol=0),
    K("Which of these did the report list among the general literary notions tested?", "Types of oral prose forms", [
        ("The date of each author's birth", "Biography was not listed."),
        ("The price of the set texts", "Not a literary notion."),
        ("The names of the examiners", "Not a literary notion.")],
      "The report lists oral prose forms, tone, realism, drama structure and metrical patterns.", "General literary appreciation", "Recall", "Think about the Lower Sixth notions."),
    K("A question stem contains the word 'except'. What should you do?", "Find the one option that is NOT true of the text", [
        ("Choose the first true option", "The word 'except' reverses the task."),
        ("Choose the longest option", "Length does not signal the answer."),
        ("Leave it blank", "There is a single correct answer to find.")],
      "Read the stem fully and note words such as not, except, best.", "Reading options", "Concept", "What does 'except' tell you about the right option?"),
    K("A distractor is:", "A wrong option written to look right, often based on a real fact misplaced or a common misreading", [
        ("The correct answer", "The correct answer is the key."),
        ("A hint in the stem", "A hint is not a distractor."),
        ("An extra option that does not count", "All options are part of the item.")],
      "Distractors are built from real mistakes.", "Reading options", "Concept", "Why do wrong options look attractive?"),
    K("A student scores poorly on questions about the anthology in a mock. What is the most useful next step?", "Revise the anthology lessons and redo their practice sets", [
        ("Re-read the Chaucer text only", "That ignores the weak topic."),
        ("Ignore the result", "A mock is for finding weak topics."),
        ("Memorise the answers to that mock", "That helps only that paper, not the topic.")],
      "Use results by topic to guide revision.", "Revision by topic", "Application", "What does the results page show by topic?"),
    K("Why is relying on summaries of the set texts risky for Paper 1?", "Questions test details such as setting, structure, style, mood and stagecraft, not just plot", [
        ("Summaries are against the rules", "Using summaries is not forbidden; the problem is they omit details."),
        ("Paper 1 has no questions on the texts", "The report says forty questions are on the texts."),
        ("The examiners do not read summaries", "The issue is what the questions test.")],
      "The report lists the assessment objectives for the text questions.", "Text-bound questions", "Reasoning", "What do the forty questions test?"),
], 108)

# ================================================================== 9. Paper 2 strategy
SET(M_EXAM, T_P2, "Paper 2 strategy: choosing and writing essays", "liu2-paper-2-strategy", [
    K("According to the Board's 2023 report, how are the four answers in Paper 2 chosen?", "One from each section and a fourth from any section but a different text", [
        ("Any four from one section", "That breaks the one-from-each-section rule."),
        ("Two from each of two sections", "The rule is one from each section, plus one more."),
        ("All sixteen questions are answered", "Only four are required.")],
      "The sections are drama, prose and poetry.", "Paper 2 structure", "Recall", "Think 'one from each'."),
    K("What do the three sections of Paper 2 correspond to?", "Drama, prose and poetry", [
        ("Past, present and future", "The sections are genres."),
        ("Reading, writing and speaking", "That is a language skills list."),
        ("Old, new and mixed syllabus", "That was a feature of 2023 sets, not the sections.")],
      "Sections A, B and C are the three genres.", "Paper 2 structure", "Recall", "Recall the genres tested."),
    K("A question begins 'To what extent do you agree...'. What should your essay do?", "Give a judgement with a case for and a case against", [
        ("Agree completely without discussion", "The phrase invites a measured judgement."),
        ("Retell the plot", "A retelling does not give a judgement."),
        ("List devices", "A list of devices is not a judgement.")],
      "The command asks for a degree of agreement.", "Command tags", "Concept", "Does 'to what extent' ask for yes or no?"),
    K("The report says some questions blend two elements such as setting and theme. What should a candidate do?", "Answer both parts of the question", [
        ("Choose the easier part only", "That would leave part of the question unanswered."),
        ("Ignore the blended question", "Such questions are normal."),
        ("Write two separate essays", "The parts must be fused in one answer.")],
      "The report says many questions expected candidates to fuse elements.", "Reading the question", "Application", "Underline each part of the question."),
    K("How does the report describe the effect of one sketchy illustration in a paragraph?", "It earns only a skimpy mark", [
        ("It earns full marks", "The report says more full illustrations earn more."),
        ("It is penalised heavily", "The report says it earns little, not a penalty."),
        ("It has no effect", "It limits the mark.")],
      "The more focused illustrations the paragraph has, the higher the mark.", "Paragraphs", "Recall", "What does the report advise for each paragraph?"),
    K("Which opening sentence begins a strong body paragraph on symbolism in a novel?", "Writer X presents the symbol of the river as a sign of continuity with the ancestors.", [
        ("The novel has many chapters.", "It says nothing about symbolism."),
        ("I like the river in the book.", "A personal opinion is not an argument."),
        ("There is a river.", "It is a statement, not a claim about meaning.")],
      "A topic sentence makes a point that the paragraph will prove.", "Paragraphs", "Application", "Which sentence makes an arguable claim?"),
    K("A candidate has 150 minutes in a KKEVO practice paper and four essays. Which time plan is sensible?", "A few minutes to read and choose, then equal planning and writing time for each essay, and a short check", [
        ("Write one very long essay and three short notes", "Each essay should be developed."),
        ("Spend 100 minutes choosing questions", "Choosing should take only a few minutes."),
        ("Skip planning to save time", "The report recommends a plan.")],
      "Planning saves time and structures the answer.", "Time plan", "Evaluation", "Which plan treats all four essays fairly?"),
    K("Why should candidates not answer more than the required number of questions?", "Extra answers are shallow and waste time that would improve the required ones", [
        ("Examiners mark only the first answer", "The report says candidates believe the best are chosen; it calls this erroneous."),
        ("It is impossible to write more", "It is possible but unwise."),
        ("It is encouraged by the Board", "The report discourages it.")],
      "The report warns against the practice.", "Instructions", "Reasoning", "What happens to the depth of each answer?"),
], 109)

# ================================================================== 10. Paper 3 strategy
SET(M_EXAM, T_P3, "Paper 3 strategy: context questions and appreciation", "liu2-paper-3-strategy", [
    K("How many questions in Paper 3 are compulsory, according to the report?", "Four", [
        ("One", "There are four compulsory questions."),
        ("Two", "Two is the number of context questions."),
        ("Three, chosen from six", "There is no choice.")],
      "Two context questions plus unseen prose and poetry make four.", "Paper 3 structure", "Recall", "Count the context and appreciation questions."),
    K("What are the sub-tasks of each Paper 3 question numbered?", "(a) to (e)", [
        ("(i) to (x)", "That is not the numbering the report gives."),
        ("(a) to (c)", "The report describes five sub-tasks."),
        ("1 to 10", "The sub-tasks are lettered.")],
      "Each question has five lettered sub-tasks.", "Paper 3 structure", "Recall", "Think of letters."),
    K("What should you do first in a context question on a play extract?", "Place the extract: who speaks, to whom, where in the play, and what has happened", [
        ("Write a summary of the whole play", "That is not required."),
        ("Quote from a different act", "The focus is the given extract."),
        ("Skip to the creative task", "Each sub-task needs the context.")],
      "Placing the extract guards against mixing characters and scenes.", "Context questions", "Application", "What does the report say about mixing up characters?"),
    K("Which of these is a stagecraft comment?", "A long silence on stage gives the audience time to feel the weight of what has been said", [
        ("The characters are poor", "That is a comment on character."),
        ("The language is formal", "That is a style comment."),
        ("The play is about money", "That is a theme statement.")],
      "Stagecraft concerns what is done on stage and its effect.", "Stagecraft", "Concept", "Which answer names a theatrical element and its effect?"),
    K("The report says some (e) sub-tasks asked for a real-life or creative task. Which is an example it gives?", "Writing a one-stanza poem of six lines", [
        ("Naming the author's birthplace", "That is a fact, not a creative task."),
        ("Copying a quotation", "That is not creative."),
        ("Drawing a map of the author's country", "The report gives no such task.")],
      "Other examples are writing a report and showing conflict-resolution skills.", "Creative tasks", "Recall", "Think of the Competency Based Approach."),
    K("In an unseen prose question, a sub-task asks for two phrases of not more than two words. A candidate copies a whole sentence. Why is this wrong?", "It breaks the length limit and has no quotation marks", [
        ("Sentences are never allowed in Paper 3", "Sentences are allowed when asked for; here the limit is two words."),
        ("It is too short", "It is too long."),
        ("It repeats the question", "The problem is the length and format.")],
      "The report describes candidates copying chunks without quotation marks.", "Citation", "Application", "Count the words."),
    K("Why should you attempt every sub-task in Paper 3, including the creative ones?", "All four questions are compulsory and partial answers still earn marks", [
        ("Creative tasks are optional", "They are part of the compulsory questions."),
        ("Marks are given only for creative tasks", "Other sub-tasks carry marks too."),
        ("Examiners read only the last answer", "All sub-tasks are marked.")],
      "A blank earns nothing; an attempt may earn marks.", "Spreading effort", "Evaluation", "What does a blank earn?"),
    K("The report notes the weakest of the four questions in 2023 was:", "The unseen poetry appreciation question", [
        ("The unseen prose appreciation question", "Prose appreciation performed better than poetry."),
        ("Both context questions equally", "The context questions performed better than the poetry question."),
        ("None; all were equal", "The report singles out poetry.")],
      "The report calls poetry appreciation the 'loadstone' of the poor performance.", "Practice priorities", "Interpretation", "Which unseen part had the lowest success rate?"),
], 110)

# ================================================================== Paper 1 mock exam A (50 multiple-choice questions)
# Proportions by topic count of the four Upper Sixth modules: African prose 12, Chaucer and canonical poetry 16, anthology 12, unseen and general appreciation 10.
P1 = [
    # ---- African & Post-Colonial Prose Fiction (12) ----
    K("In Tsitsi Dangarembga's Nervous Conditions, who tells the story?", "Tambudzai (Tambu), looking back on her girlhood", [
        ("Nyasha, her cousin", "Nyasha is a major character, but Tambu narrates."),
        ("Babamukuru, her uncle", "He is the powerful head of the family, not the narrator."),
        ("An unnamed objective narrator", "The story is told in the first person by Tambu.")],
      "Tambu narrates in the first person.", T_PR1, "Recall", "Think of the girl who wins a place at the mission school."),
    K("Which writer wrote Anthills of the Savannah?", "Chinua Achebe", [
        ("Wole Soyinka", "Soyinka edited the anthology Poems of Black Africa and wrote plays and poems."),
        ("Tsitsi Dangarembga", "She wrote Nervous Conditions."),
        ("Ola Rotimi", "He is a Nigerian dramatist.")],
      "Achebe wrote the novel, set in the imaginary state of Kangan.", T_PR1, "Recall", "Recall the author of Things Fall Apart."),
    K("The Board's report lists clues for identifying a novelist's purpose. Which of these is such a clue?", "What the narrator approves or criticises, and how the ending resolves events", [
        ("The colour of the cover", "Cover design says nothing reliable about purpose."),
        ("The number of pages", "Length is not a clue to purpose."),
        ("The name of the printer", "Printing details do not reveal purpose.")],
      "Purpose appears in title, themes, attitudes and ending.", T_PR1, "Concept", "Which clue comes from inside the story?"),
    K("A story is told by one of its characters, who says 'I'. This point of view is:", "First person", [
        ("Third-person omniscient", "An omniscient narrator is outside the story and knows everything."),
        ("Second person", "Second person addresses 'you'."),
        ("Objective", "An objective narrator reports only what can be seen.")],
      "A character narrating with 'I' uses the first person.", T_PR2, "Concept", "Which pronoun does the narrator use?"),
    K("What is a limitation of a first-person narrator?", "The reader sees only what that narrator knows and chooses to tell", [
        ("The narrator can enter every character's mind", "That is omniscient narration."),
        ("The narrator cannot use dialogue", "First-person narrators can report dialogue."),
        ("The story must be told in the present tense", "Tense is not fixed by person.")],
      "The view is limited to one mind.", T_PR2, "Reasoning", "How much can one person know?"),
    K("Which description of narration in Anthills of the Savannah is most accurate?", "The story moves between several voices and viewpoints, including Beatrice's", [
        ("It has a single narrator throughout", "The novel uses several narrators and viewpoints."),
        ("It is a collection of letters only", "It is not told only in letters."),
        ("It is fully objective with no inner thoughts", "Characters' thoughts are shared.")],
      "Check your copy for which chapters belong to which voice.", T_PR2, "Recall", "Think of the three main friends and Beatrice."),
    K("According to the Board's report, assimilation means:", "Pressure to adopt the colonizer's culture and language", [
        ("Independence from colonial rule", "That is decolonisation."),
        ("The return to ancestral traditions", "That is the opposite of assimilation."),
        ("The division of an empire", "That is not the term's meaning.")],
      "Assimilation asks colonised people to imitate the ruling culture.", T_PR3, "Concept", "Think of 'to make similar'."),
    K("Neo-colonialism is best described as:", "Continued outside control, or new rulers repeating old oppression, after independence", [
        ("The first arrival of colonists", "That is the start of colonialism."),
        ("A return to oral storytelling", "That is a literary choice."),
        ("A peaceful transfer of power with no problems", "Neo-colonialism names a problem after independence.")],
      "The 'neo' means new: a new form of control.", T_PR3, "Concept", "What continues after independence?"),
    K("In Nervous Conditions, what does Nyasha's illness chiefly show?", "The strain of being caught between two cultures and between expectations of obedience and independence", [
        ("A simple dislike of school", "Her illness is far more serious than dislike."),
        ("The success of colonial education", "It shows the costs of that education."),
        ("A happy acceptance of tradition", "She is in conflict, not at ease.")],
      "Check your copy; teachers differ on emphasis.", T_PR3, "Interpretation", "What pressures does Nyasha face at home and at school?"),
    K("How should the title of a novel be shown in handwritten work?", "Underlined", [
        ("In quotation marks", "Quotation marks are for poem titles."),
        ("In capitals only", "Capitals alone do not mark a title."),
        ("Left unmarked", "The report lists titles as a convention to follow.")],
      "The report says novels and collections are underlined.", T_PR4, "Recall", "Compare poem titles with novel titles."),
    K("A candidate answers a question on narrative technique by retelling the plot. What is the main fault?", "The answer does not address the technique asked about", [
        ("It is too short", "Length is not the main problem."),
        ("It uses the present tense", "The present tense is correct."),
        ("It uses a quotation", "A quotation is welcome if used well.")],
      "A retelling is not an analysis.", T_PR4, "Application", "What did the question ask?"),
    K("Which opening sentence is the best topic sentence for a paragraph on a novel's setting?", "The writer uses the mission school to show the cost of colonial education.", [
        ("The book has a school in it.", "It makes no argument."),
        ("Schools are important.", "It is a general statement."),
        ("I enjoyed the school chapter.", "A personal feeling is not a literary claim.")],
      "A topic sentence makes a claim to be proved.", T_PR4, "Application", "Which sentence can be proved with details?"),
    # ---- Chaucer & Canonical English Poetry (16) ----
    K("In which century did Chaucer write The Canterbury Tales?", "The fourteenth century", [
        ("The twelfth century", "That is too early; Middle English was still forming."),
        ("The sixteenth century", "That is the time of Shakespeare's period, later than Chaucer."),
        ("The eighteenth century", "That is the age of Pope.")],
      "Chaucer wrote in the late fourteenth century.", T_CH1, "Recall", "He lived about 1340 to 1400."),
    K("Chaucer's English is called:", "Middle English", [
        ("Old English", "That is the language of Beowulf."),
        ("Modern English", "Spelling, vocabulary and sounds differ from today's English."),
        ("Anglo-Latin", "It is not a Latin text.")],
      "Middle English runs from about 1100 to 1500.", T_CH1, "Recall", "Between Old and Modern English."),
    K("To which shrine are the pilgrims travelling?", "The shrine of Thomas Becket at Canterbury", [
        ("The shrine of St Paul in London", "They set out near London, but Canterbury is the goal."),
        ("The tomb of King Arthur", "That is not the pilgrimage's goal."),
        ("The shrine of St Benedict", "St Benedict wrote the Rule the Monk neglects; he is not the shrine.")],
      "The report names Becket, killed in 1170.", T_CH1, "Recall", "The report mentions the 'holy blissful martyr'."),
    K("Where do the pilgrims meet before setting out?", "The Tabard Inn in Southwark", [
        ("Canterbury Cathedral", "That is the destination."),
        ("Westminster Abbey", "The pilgrims do not meet there."),
        ("The Tower of London", "It is not their meeting place.")],
      "The pilgrims gather at the Tabard Inn, Southwark.", T_CH2, "Recall", "Where do pilgrims lodge before leaving?"),
    K("The opening of the General Prologue mentions Zephyrus. This is an example of:", "A classical allusion", [
        ("A historical allusion", "Historical allusion refers to real events like Becket's death."),
        ("A rhetorical question", "No question is asked."),
        ("An onomatopoeic word", "It is a name, not an imitation of sound.")],
      "Zephyrus is the Greek god of the west wind, an allusion to classical myth.", T_CH2, "Concept", "Is Zephyrus from Greece or from English history?"),
    K("The General Prologue is written in:", "Rhyming couplets of iambic pentameter", [
        ("Blank verse", "Blank verse has no rhyme."),
        ("Free verse", "It has a regular pattern of rhyme and metre."),
        ("Ballad stanzas", "Ballad stanzas are quatrains.")],
      "Pairs of rhyming lines of about ten syllables.", T_CH2, "Concept", "Does it rhyme, and how long are the lines?"),
    K("The Monk is shown hunting and not following the Rule of St Benedict. This mainly shows:", "Chaucer's irony about church figures who fail to live up to their calling", [
        ("Chaucer's admiration for the Monk", "The Monk is gently mocked."),
        ("That monks never hunted", "The text shows that this Monk did."),
        ("The poet's lack of interest in religion", "The satire shows deep interest in the Church.")],
      "The report links the Rule to the Monk's unworthiness.", T_CH2, "Interpretation", "What gap lies between his role and behaviour?"),
    K("Which of these is a key feature of the portrait of the Knight, Parson or Plowman?", "They are presented as largely admirable ideals", [
        ("They are the most corrupt pilgrims", "That would apply to figures like the Pardoner or the Summoner."),
        ("They are mocked for their wealth", "Their portraits are mainly respectful."),
        ("They never speak or act in the General Prologue", "They are described in detail.")],
      "Chaucer includes ideal figures alongside the satirised ones.", T_CH2, "Concept", "Which pilgrims serve as models?"),
    K("In The Merchant's Tale, who is January?", "An old knight who marries a young wife", [
        ("The squire who loves May", "That is Damian."),
        ("January's friend and adviser Justinus", "Justinus is one of January's brothers."),
        ("A god who restores his sight", "The sight-restoring figure is Pluto, who is a different character.")],
      "January is the elderly husband of May.", T_CH3, "Recall", "Which character is the ageing husband?"),
    K("Which character is the young wife in The Merchant's Tale?", "May", [
        ("Dorigen", "Dorigen is in The Franklin's Tale."),
        ("Alisoun", "Alisoun is in The Miller's Tale."),
        ("Griselda", "Griselda is in The Clerk's Tale.")],
      "May deceives January with Damian.", T_CH3, "Recall", "Tale names the wife as a month."),
    K("What is the central irony of The Merchant's Tale?", "A husband who wants a perfect marriage is deceived by his wife", [
        ("A wife who is faithful and rewarded", "May is unfaithful."),
        ("A merchant who is honest and rich", "The tale is about marriage."),
        ("A pilgrim who loses a race", "No race is central.")],
      "Check your copy for how the tale ends.", T_CH3, "Interpretation", "What is January's wish and what happens?"),
    K("A Metaphysical poet is:", "John Donne", [
        ("William Wordsworth", "He is a Romantic poet."),
        ("Robert Browning", "He is a Victorian poet."),
        ("T. S. Eliot", "He is a Modernist poet.")],
      "Donne, Herbert and Marvell are standard examples.", T_CH4, "Recall", "Think seventeenth century."),
    K("A conceit is:", "An elaborate, ingenious and surprising extended comparison", [
        ("A short cry of surprise", "That is an exclamation."),
        ("A pattern of rhyme", "Rhyme is a sound pattern."),
        ("The final line of a poem", "A conceit is not a position in a poem.")],
      "Metaphysical poets used conceits to link thought and feeling.", T_CH4, "Concept", "Think of a comparison that stretches far."),
    K("Which feature is typical of Romantic poetry such as Keats's odes?", "Feeling, imagination and the natural world", [
        ("Strict satire of the court", "That belongs more to Pope's age."),
        ("Interest only in machines and cities", "Romantic poetry values nature."),
        ("Rigid adherence to classical rules", "Romantics valued feeling over rules.")],
      "Romanticism valued feeling and imagination.", T_CH4, "Concept", "Which movement valued 'feeling'?"),
    K("A poem in which a speaker addresses a silent listener and unintentionally reveals his own character is a:", "Dramatic monologue", [
        ("Sonnet", "A sonnet has a fixed fourteen-line form."),
        ("Ode", "An ode is a lyric of praise."),
        ("Elegy", "An elegy mourns the dead.")],
      "Browning's 'My Last Duchess' is a famous example.", T_CH5, "Concept", "One speaker, one silent listener."),
    K("Which is a feature of Modernist poetry?", "Fragmentation and allusion, with a break from regular forms", [
        ("Smooth, regular ballad stanzas always", "Modernists often broke from regular forms."),
        ("An emphasis on perfect rhyme", "Rhyme was not a priority."),
        ("A single clear narrator in every poem", "Modernist poems often use fragments and several voices.")],
      "Eliot's The Waste Land (1922) is a standard example.", T_CH5, "Concept", "Think of fragments and quotations."),
    # ---- Modern African Poetry Anthology (12) ----
    K("Which anthology does the Board's 2023 report name as the set poetry text?", "Poems of Black Africa", [
        ("Songs of Innocence", "That is by Blake."),
        ("Selected Poems of John Keats", "The report lists this as a separate set text."),
        ("The Rape of the Lock", "That is a mock-epic by Pope.")],
      "The report names the anthology for both syllabuses.", T_READ, "Recall", "The anthology edited by Soyinka."),
    K("Negritude is a movement that:", "Celebrates Black cultural identity", [
        ("Rejects all African traditions", "It does the opposite."),
        ("Promotes colonial rule", "It resists colonial culture."),
        ("Studies grammar", "It is a cultural and literary movement.")],
      "It began among French-speaking Black writers in the 1930s.", T_READ, "Concept", "What does the movement affirm?"),
    K("Which poem does the report link to prison conditions?", "'Cold' by Dennis Brutus", [
        ("'Olokun' by J. P. Clark", "That is about a sea goddess."),
        ("'The Bond' by Mazisi Kunene", "That is about a grinding stone."),
        ("'If' by Jared Angira", "That is about omens from animals and dreams.")],
      "The report describes a prison yard in 'Cold'.", T_READ, "Recall", "Which South African poet writes of apartheid prisons?"),
    K("Apostrophe is:", "A direct address to an absent, abstract or dead person or thing", [
        ("A repeated initial consonant", "That is alliteration."),
        ("A comparison using 'like'", "That is a simile."),
        ("A pause in the middle of a line", "That is a caesura.")],
      "The report names it among the poems' devices.", T_ORAL, "Recall", "Who is the speaker talking to?"),
    K("A leader's line answered by a chorus is:", "Call and response", [
        ("Parallelism", "That repeats a sentence shape."),
        ("Enjambment", "That runs a sentence over a line break."),
        ("Refrain", "That repeats a line or phrase, not an answer from a chorus.")],
      "It involves the audience.", T_ORAL, "Recall", "Think of a leader and a crowd."),
    K("Which of these is an oral poetic form?", "A dirge", [
        ("A novel", "A novel is a written prose form."),
        ("A sonnet sequence", "That is a written form."),
        ("A stage direction", "That is a drama term.")],
      "A dirge is sung in mourning.", T_ORAL, "Recall", "Which one is a song of mourning?"),
    K("In 'The Bond', as the report describes it, the grinding stone symbolises:", "The ancestor's legacy and duty to protect it", [
        ("Wealth", "The stone's value is in its link to the ancestor."),
        ("A weapon", "It is a tool, not a weapon."),
        ("The colonial law", "The poem is not about law.")],
      "The stone is passed with a warning of curses.", T_SYMB, "Interpretation", "Why must it be kept sacred?"),
    K("The sea goddess who charms her lovers appears in:", "'Olokun'", [
        ("'Rulers'", "'Rulers' is about corrupt leaders."),
        ("'Cold'", "'Cold' is about prison."),
        ("'Upheaval'", "'Upheaval' is about a tyrant's fall.")],
      "'Olokun' is by J. P. Clark.", T_SYMB, "Recall", "Which poem has a goddess in its title?"),
    K("Disillusionment in the poems refers to:", "The loss of hope and trust in rulers or society", [
        ("A joyful return to tradition", "That is not disillusionment."),
        ("A love of nature", "That is not the term's meaning."),
        ("The use of rhyme", "It is a mood, not a form.")],
      "It is disappointed hope.", T_SYMB, "Concept", "What happens to hope?"),
    K("How should the title of a poem be shown in an essay?", "In quotation marks", [
        ("Underlined", "That is for a collection, novel or play."),
        ("In red ink", "Colour is not a convention."),
        ("Not shown", "The report says to follow conventions.")],
      "The report lists this convention.", T_WRITE, "Recall", "Compare it with a collection title."),
    K("What does the report say candidates should not do with instructions?", "Answer more questions than required", [
        ("Follow them", "Candidates should follow them."),
        ("Read them", "Candidates should read them."),
        ("Underline them", "That is harmless.")],
      "Extra answers are shallow and waste marks.", T_WRITE, "Recall", "What did some candidates do wrongly?"),
    K("Which is the best topic sentence for a paragraph on apostrophe in 'Dedication'?", "In 'Dedication', Soyinka addresses the dead directly, which makes the speaker's respect immediate.", [
        ("'Dedication' is a poem.", "It makes no claim."),
        ("Soyinka was a Nobel Prize winner.", "That is biography, not analysis of the poem."),
        ("Apostrophe is a device.", "It defines but does not analyse the poem.")],
      "Check your copy for the exact words.", T_WRITE, "Application", "Which sentence makes a claim about the poem?"),
    # ---- Unseen Prose & Poetry Criticism (10) ----
    K("Meaning in context means:", "A meaning that fits the passage, in your own words", [
        ("Any dictionary meaning", "Only the fitting meaning counts."),
        ("A translation", "No translation is required."),
        ("The same word repeated", "Repeating shows no understanding.")],
      "The surrounding lines decide the meaning.", T_UPROSE, "Concept", "What does 'context' mean?"),
    K("A question asks you to cite two words. Which is correct?", "Exact words from the passage in quotation marks", [
        ("A paraphrase in your own words", "A paraphrase is not a citation."),
        ("The whole sentence", "It breaks the limit."),
        ("A summary", "A summary does not answer 'which words'.")],
      "The report describes candidates who copied chunks.", T_UPROSE, "Recall", "What goes inside quotation marks?"),
    K("Attitude in a passage is best identified from:", "Words and phrases that carry feeling", [
        ("The length of the passage", "Length does not reveal attitude."),
        ("The author's photograph", "It is not in the passage."),
        ("The number of paragraphs", "Paragraph count does not reveal attitude.")],
      "Diction reveals attitude.", T_UPROSE, "Concept", "Which words carry feeling?"),
    K("The rhyme scheme of a quatrain ending: night, grow, light, slow is:", "ABAB", [
        ("AABB", "Lines 1 and 2 do not rhyme."),
        ("ABBA", "Lines 1 and 4 do not rhyme."),
        ("ABCD", "Two pairs rhyme.")],
      "Night and light rhyme; grow and slow rhyme: A B A B.", T_UPOEM, "Calculation", "Label each end with a letter."),
    K("'Her laughter was a bell' is an example of:", "Metaphor", [
        ("Simile", "No 'like' or 'as'."),
        ("Alliteration", "No repeated initial sound."),
        ("Apostrophe", "No one is addressed.")],
      "Laughter is said to be a bell.", T_UPOEM, "Concept", "Is there a joining word?"),
    K("Which line contains alliteration?", "'Sweet, soft sounds slid by.'", [
        ("'The road is long and wide.'", "No repeated initial consonants."),
        ("'A bird in the hand.'", "No repeated initial consonants dominate."),
        ("'We walked to the sea.'", "No repeated initial consonants dominate.")],
      "The repeated /s/ is alliteration.", T_UPOEM, "Concept", "Which line repeats an initial sound?"),
    K("The report says a candidate must do what after finding a rhyme scheme?", "Comment on its effectiveness", [
        ("Rewrite the poem", "That is not asked."),
        ("Count the words", "Not required."),
        ("Ignore it", "The report says the effect matters.")],
      "Effect links form to meaning.", T_PRAC, "Recall", "What did many candidates fail to do?"),
    K("Tone is:", "The speaker's attitude, shown by word choice and sound", [
        ("The number of stanzas", "That is form."),
        ("The title of the poem", "That is a title."),
        ("The rhyme scheme", "That is a sound pattern.")],
      "The report lists tone among the general literary notions.", T_PRAC, "Concept", "What attitude does the voice reveal?"),
    K("A line has four iambic feet. It is called:", "Iambic tetrameter", [
        ("Iambic pentameter", "Pentameter has five feet."),
        ("Trochaic trimeter", "Trochaic feet and three feet do not match."),
        ("Anapaestic hexameter", "Anapaestic feet and six feet do not match.")],
      "Tetra means four.", T_PRAC, "Concept", "How many feet are there?"),
    K("Which sentence uses a relative pronoun?", "The girl who sang left early.", [
        ("She sang loudly.", "'She' is a personal pronoun."),
        ("They hurt themselves.", "'Themselves' is a reflexive pronoun."),
        ("This is mine.", "'Mine' is a possessive pronoun.")],
      "'Who' relates 'the girl' to the clause that follows.", T_PRAC, "Application", "Which pronoun joins a clause to a noun?"),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(module=M_EXAM, topic=T_P1, title="Paper 1 mock exam A", lesson="liu2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 201)))

# ================================================================== Paper 2 practice paper A (25 auto-markable parts)
P2 = [
    # Question 1: choosing questions
    K("Question 1 (a). According to the Board's 2023 report, which choice of four Paper 2 answers is allowed?", "One question from each of drama, prose and poetry, and a fourth from any section on a different text", [
        ("Four questions from the poetry section", "The rule asks for one from each section first."),
        ("Two from drama and two from prose", "That leaves out poetry."),
        ("Three on the same text and one on another", "Questions from the same text are not allowed as extra answers.")],
      "One from each section, then a fourth on a different text.", T_WRITE, "Recall", "Think 'one from each' plus a different text."),
    N("Question 1 (b). The report says two questions were set on each of eight set texts in Paper 2. How many questions were there in all?", 16, "2 x 8 = 16.", T_WRITE, "Calculation", "Multiply the questions per text by the number of texts.", tol=0),
    K("Question 1 (c). A candidate answers questions 3 and 4 on the same text as two of his four answers. What is wrong?", "Two questions on the same text breaks the rule about a different text for the extra answer", [
        ("Nothing; any four questions are allowed", "The report describes limits on sections and texts."),
        ("He has answered too few questions", "The number is right; the choice is wrong."),
        ("He must answer in pencil", "The pen or pencil issue is not the rule.")],
      "The fourth answer must be from a different text.", T_WRITE, "Application", "Check the text of each answer."),
    # Question 2: command words and focus
    K("Question 2 (a). What does 'examine' ask you to do?", "Look closely at the parts of the matter and weigh them with evidence", [
        ("Retell the plot in order", "Retelling does not examine."),
        ("List every device in the text", "A list is not an examination."),
        ("Write only your opinion", "Opinion needs evidence.")],
      "Command words ask for specific activities.", T_PR4, "Concept", "Is 'examine' about summary or closer study?"),
    K("Question 2 (b). A question says 'To what extent do you agree that the narrator is reliable?' What should the answer include?", "A judgement showing where the narrator can be trusted and where not", [
        ("A statement that the narrator is always reliable", "That ignores the limits."),
        ("A list of the novel's chapters", "That is not an argument."),
        ("A biography of the novelist", "That does not answer the question.")],
      "'To what extent' asks for degree.", T_PR2, "Reasoning", "What does 'extent' suggest?"),
    K("Question 2 (c). A question asks about 'setting and theme' in a novel. What should you do?", "Show how the setting expresses or develops the theme, covering both", [
        ("Write only about setting", "Theme must be covered too."),
        ("Write only about theme", "Setting must be covered too."),
        ("Write about two separate novels", "The question asks for a link between setting and theme.")],
      "The report says many questions blend two elements.", T_PR4, "Application", "Underline both words in the question."),
    # Question 3: anthology
    K("Question 3 (a). Question: 'Comment on the use of apostrophe in three poems of your choice.' Which thesis is best?", "Poets use apostrophe to speak to the dead or to Africa, which makes grief and respect immediate", [
        ("Apostrophe is a device in poetry.", "It defines but does not argue."),
        ("The poets were born in Africa.", "It is a biographical fact, not an argument."),
        ("Poems contain many words.", "It says nothing about apostrophe.")],
      "A thesis states a claim about the device and its effect.", T_SYMB, "Application", "Which sentence explains an effect?"),
    K("Question 3 (b). Which poem does the Board's report name as one where apostrophe appears?", "'Vanity' by Birago Diop", [
        ("'Olokun' by J. P. Clark", "The report links 'Olokun' to the sea goddess and beliefs."),
        ("'Cold' by Dennis Brutus", "The report links 'Cold' to prison conditions."),
        ("'The Bond' by Mazisi Kunene", "The report links 'The Bond' to ancestor protection.")],
      "The report also names 'Dedication', 'Pardon Me', 'Rulers' and others.", T_ORAL, "Recall", "Pick the poem the report lists for apostrophe."),
    K("Question 3 (c). How should a paragraph on one poem be organised?", "Topic sentence, several focused illustrations, comment on effect", [
        ("Retelling, then a quotation, then a retelling", "That produces narration."),
        ("A single long quotation", "It does not argue."),
        ("A biography of the poet followed by a conclusion", "That does not follow the question.")],
      "The report asks for topic sentences, illustrations and comment.", T_WRITE, "Application", "What does a paragraph begin with?"),
    K("Question 3 (d). Which addition strengthens a question on how poets show dissatisfaction with society?", "A counter-point that the poets also keep hope and celebrate their culture", [
        ("A list of poets' birthdays", "It is irrelevant."),
        ("A statement that the poems are all the same", "It is not true and shows no analysis."),
        ("A statement that the poets are not African", "It is false and irrelevant.")],
      "The report says good answers argue both sides.", T_SYMB, "Evaluation", "What does a good answer add to the case for protest?"),
    # Question 4: African prose
    K("Question 4 (a). Question: 'Examine the narrative perspective of a novel you have studied.' Which plan is best?", "Identify the narrator, show what the viewpoint reveals and hides, judge its effect on the theme", [
        ("Retell the novel in order", "That ignores perspective."),
        ("Describe the author's life", "That ignores perspective."),
        ("Count the chapters", "It does not analyse.")],
      "Perspective is a question about who tells and how.", T_PR2, "Application", "What does the question focus on?"),
    K("Question 4 (b). In a first-person retrospective novel, why is it useful to mention the older and younger selves?", "The older self judges events that the younger self lived through", [
        ("They are two different books", "They are two selves of one narrator."),
        ("The older self never speaks", "The older self tells the story."),
        ("It proves the novel is a fable", "It proves nothing about genre.")],
      "Retrospect gives two perspectives in one voice.", T_PR2, "Concept", "Who is telling, and when are the events set?"),
    K("Question 4 (c). 'Assimilation' is a theme in a post-colonial novel. Which sentence best begins a paragraph on it?", "The novelist shows how characters are pressed to copy the colonizer's culture and what this costs them", [
        ("Assimilation is a long word.", "It makes no argument."),
        ("There are many characters.", "It says nothing about theme."),
        ("The setting is Africa.", "It is too vague.")],
      "Name the theme, the pressure and the cost.", T_PR3, "Application", "Which sentence makes a claim about the novel?"),
    K("Question 4 (d). Which is the best evidence in a paragraph on neo-colonialism in Anthills of the Savannah?", "A specific episode or speech showing rulers who repeat old abuses of power, explained", [
        ("The author's name", "It is not evidence of the theme."),
        ("The title only", "The title alone does not prove the point."),
        ("A claim without detail", "A claim needs detail.")],
      "Evidence must be specific and explained; check your copy.", T_PR3, "Application", "What makes a paragraph persuasive?"),
    # Question 5: Chaucer
    K("Question 5 (a). Question: 'Discuss Chaucer's use of irony in the General Prologue.' Which plan is best?", "Define irony, choose several portraits (such as the Monk), show what is said and what is meant, judge the effect", [
        ("List all the pilgrims in order", "A list does not analyse irony."),
        ("Give Chaucer's life story", "Biography does not answer the question."),
        ("Write about the weather in April", "The opening is only one part and does not discuss irony.")],
      "Irony needs explicit examples and explanation.", T_CH2, "Application", "What must each paragraph show?"),
    K("Question 5 (b). In an essay on The Merchant's Tale, which statement is the best claim?", "The tale uses the contrast between January's wish for perfect happiness and May's deceit to criticise a foolish old man's illusion", [
        ("The tale is long.", "It makes no argument."),
        ("January is a month.", "It is a fact, not an argument."),
        ("Chaucer was a poet.", "It says nothing about the tale.")],
      "Check your copy for the details of the tale.", T_CH3, "Application", "Which sentence states a view that can be proved?"),
    K("Question 5 (c). How should you quote Middle English?", "A few exact words only, if you are sure of them", [
        ("A whole page from memory", "A wrong long quotation loses marks."),
        ("Never refer to the text", "Reference to the text is needed."),
        ("Translate it into French", "No translation is required.")],
      "Short exact quotations or references to moments are best.", T_CH1, "Concept", "What is safer: a long quotation or a few words?"),
    # Question 6: canonical poetry
    K("Question 6 (a). For an essay on Donne, which technique should the plan highlight?", "The conceit and its argument", [
        ("The use of dialect", "That is not a Donne feature in this sense."),
        ("The free verse form", "Donne's poems are generally formal."),
        ("The dramatic monologue of the Victorians", "That is a Victorian form.")],
      "Metaphysical poems are known for conceits.", T_CH4, "Concept", "Which device suits Metaphysical poetry?"),
    K("Question 6 (b). In an essay on Keats's odes, which idea is most relevant?", "The Romantic emphasis on feeling, imagination and nature", [
        ("A strict satire of society", "Satire is not the focus."),
        ("Industrial machinery", "It is not typical of Keats."),
        ("Courtly love", "It is a medieval theme.")],
      "The report names Romantic conventions for Keats.", T_CH4, "Concept", "Which movement does Keats belong to?"),
    K("Question 6 (c). Which technique should an essay on a Modernist poem discuss?", "Fragmentation, allusion and free verse", [
        ("Ballad stanzas only", "Those are traditional forms."),
        ("A single clear story told in order", "Modernism often avoids that."),
        ("A strict ABAB rhyme throughout", "Modernists often broke from strict rhyme.")],
      "Check which poem is your set poem.", T_CH5, "Concept", "What breaks with tradition?"),
    # Question 7: time and conventions
    N("Question 7 (a). In a KKEVO practice paper of 150 minutes, a candidate spends 10 minutes reading and choosing and 5 minutes checking, and shares the rest equally among four essays. How many minutes does each essay get? (Give a decimal.)", 33.75, "150 - 10 - 5 = 135; 135 / 4 = 33.75.", T_WRITE, "Calculation", "Subtract the fixed times first, then divide by four.", unit="minutes", tol=0.01),
    K("Question 7 (b). Which conclusion is best?", "A short judgement that answers the question and links back to the thesis", [
        ("A new topic not yet discussed", "A conclusion should not begin a new topic."),
        ("A copy of the introduction", "It should add a judgement, not repeat."),
        ("No conclusion", "The report asks for a logical finish.")],
      "Give a judgement with logical finality.", T_WRITE, "Concept", "What does the report say about a conclusion?"),
    K("Question 7 (c). A candidate crosses out the plan neatly but leaves the essay unfinished. What is the lesson?", "Plan quickly, then manage the time so every essay is finished", [
        ("Never write a plan", "A plan helps, but time must be managed."),
        ("Write only one essay", "Four essays are required."),
        ("Cross out the essay instead", "The essay is what is marked.")],
      "Time management is part of the skill.", T_WRITE, "Evaluation", "What goes wrong if one essay is unfinished?"),
    # Question 8: short notes
    K("Question 8 (a). 'Write short notes on (i) praise poetry and (ii) the dirge.' How many items should you write about?", "Exactly the two items listed, each in a few exact points", [
        ("Every oral form you know", "The report says some candidates answered more than allowed."),
        ("One item in a full essay", "Both items are asked."),
        ("Three items to be safe", "Extra items waste time.")],
      "Short notes are brief and exact.", T_ORAL, "Application", "Count the items asked."),
    K("Question 8 (b). Which is a good first point for short notes on the dirge?", "A song of mourning that may also speak to the dead and comfort the living", [
        ("A long poem about work", "That describes a work song."),
        ("A form of praise for a chief", "That describes praise poetry."),
        ("A funny story with animals", "That describes a folktale.")],
      "A dirge is a funeral song.", T_ORAL, "Recall", "What is a dirge for?"),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=M_EXAM, topic=T_P2, title="Paper 2 practice paper A", lesson="liu2-paper-2-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P2, 202)))

# ================================================================== Paper 3 practice paper A (20 auto-markable parts)
P3 = [
    # ---- Question 1: unseen prose, 'The Path at Mbelu' ----
    K("Question 1 (a)(i). Give the meaning in context of 'a thief of the common good'.", "Someone who takes what belongs to everyone in the community", [
        ("A person who steals money from a bank", "The phrase refers to a shared path, not a bank."),
        ("A person who is good at stealing", "'Good' here means benefit, not skill."),
        ("A criminal who is common in the village", "'Common' means shared.")],
      "The path is used by everyone, so 'common good' means shared benefit.", T_UPROSE, "Application", "What did the young man say Pa Ngwa had taken?", passage=PROSE_PATH),
    K("Question 1 (a)(ii). Give the meaning in context of 'a grudging cough'.", "A reluctant sound made by someone who does not want to admit something", [
        ("A cheerful greeting", "'Grudging' means reluctant."),
        ("A sign of illness", "The cough shows reluctance, not illness."),
        ("An angry shout", "A cough is not a shout.")],
      "He admits his fear unwillingly.", T_UPROSE, "Application", "How does a person speak when admitting something they dislike?", passage=PROSE_PATH),
    K("Question 1 (a)(iii). Give the meaning in context of 'until the noise thinned'.", "Until the shouting became less loud", [
        ("Until the crowd became smaller in body", "'Thinned' describes the noise, not the people."),
        ("Until the noise became thicker", "That is the opposite."),
        ("Until the noise became a song", "No singing is mentioned.")],
      "A thinning noise fades.", T_UPROSE, "Application", "What is the noise doing?", passage=PROSE_PATH),
    K("Question 1 (b). Which quotation best proves that Pa Ngwa had a real reason for his action?", "'his goats had been stolen twice by strangers who used the path in the dark'", [
        ("'the women of Mbelu had carried water'", "This shows the village's custom, not his reason."),
        ("'arms folded'", "This shows his stance, not his reason."),
        ("'the whole village had gathered'", "This shows the size of the meeting.")],
      "His goats were stolen by strangers using the path.", T_UPROSE, "Interpretation", "Which detail explains why he blocked the path?", passage=PROSE_PATH),
    K("Question 1 (c). Which evidence best supports the view that the Mbelu community is admirable?", "Both sides admit their fears and agree a shared solution, a gate and a bench", [
        ("The village has a mango tree", "The tree is only a meeting place."),
        ("The meeting is held at noon", "The time does not show admirable qualities."),
        ("One young man shouts at Pa Ngwa", "The shouting shows conflict, not admirable behaviour.")],
      "They listen, admit fears and compromise.", T_UPROSE, "Evaluation", "What does the community do at the end of the meeting?", passage=PROSE_PATH),
    K("Question 1 (d)(i). Which phrase of not more than two words shows that Pa Ngwa had long held back his complaint?", "'kept quiet'", [
        ("'a fence'", "This shows an object, not his restraint."),
        ("'his land'", "This shows ownership, not restraint."),
        ("'forty years'", "This shows duration, not his attitude.")],
      "He says he had kept quiet for forty years.", T_UPROSE, "Recall", "Which two words show silence?", passage=PROSE_PATH),
    K("Question 1 (d)(ii). What attitude does that phrase reveal?", "A long, patient resentment that has finally come out", [
        ("Cheerful generosity", "He is not generous."),
        ("Complete indifference", "He cares deeply about his land."),
        ("Fear of the villagers", "He stands firm with arms folded.")],
      "He kept quiet for forty years, then acted.", T_UPROSE, "Interpretation", "How does a man feel after silence of forty years?", passage=PROSE_PATH),
    K("Question 1 (e)(i). Which conflict-resolution skill does Mama Ewane show when she says 'Let each side say what it fears'?", "Inviting both sides to state their concerns", [
        ("Punishing the guilty", "She does not punish anyone."),
        ("Taking Pa Ngwa's side", "She states that both sides are right."),
        ("Ending the meeting at once", "She continues the meeting.")],
      "She asks for fears, which are the real interests behind the quarrel.", T_UPROSE, "Application", "Whom does she ask to speak?", passage=PROSE_PATH),
    K("Question 1 (e)(ii). Which outcome shows compromise?", "A gate that the women close each evening, plus a bench for rest", [
        ("The fence stays and nobody may pass", "That is a victory for one side."),
        ("The fence is removed with no change", "That ignores Pa Ngwa's fear."),
        ("The village moves to a new place", "No move is described.")],
      "Each side gets something: safety for goats, water for the women.", T_UPROSE, "Application", "Who gains from the gate?", passage=PROSE_PATH),
    # ---- Question 2: unseen poem, 'Morning Queue at the Tap' ----
    K("Question 2 (a). What is the poem mainly about?", "People patiently waiting for water at dawn and the relief when it comes", [
        ("A farmer selling jerrycans", "No one sells anything."),
        ("A boy who loses a stone", "The stone is a small detail."),
        ("A fight between cocks", "The 'argument' of the cocks is a figure of speech.")],
      "The poem builds from waiting to relief.", T_UPOEM, "Interpretation", "Read the first and last stanza groups.", passage=POEM_QUEUE),
    K("Question 2 (a)(ii). What is the tone of the poem?", "Patient and gently humorous, ending in relief", [
        ("Furious", "The queue is calm."),
        ("Mocking and cruel", "The humour is affectionate."),
        ("Cold and distant", "The poem warms to the people.")],
      "Words such as 'loyalties' and 'welcome guest' are warm.", T_UPOEM, "Interpretation", "How do the speaker's images treat the people?", passage=POEM_QUEUE),
    K("Question 2 (b)(i). In context, 'small round loyalties' means:", "The jerrycans that stand faithfully waiting in line", [
        ("Soldiers", "Jerrycans are being described."),
        ("Little coins", "The row refers to the cans."),
        ("Children's toys", "The cans are described, not toys.")],
      "'Loyalties' suggests faithful waiting.", T_UPOEM, "Application", "What is lined up in the row?", passage=POEM_QUEUE),
    K("Question 2 (b)(ii). In context, 'the tap to clear its throat' means:", "The tap to splutter and start releasing water", [
        ("The tap to be repaired", "It describes the tap starting."),
        ("The tap to be sold", "No sale is mentioned."),
        ("The tap to stop completely", "The tap is about to start.")],
      "A tap often coughs and splutters before water flows.", T_UPOEM, "Application", "What does a tap do before the water comes?", passage=POEM_QUEUE),
    K("Question 2 (c)(i). Which device is used in 'the cocks have finished their argument'?", "Personification", [
        ("Simile", "No 'like' or 'as'."),
        ("Apostrophe", "No one is addressed."),
        ("Onomatopoeia", "No sound is imitated by the word.")],
      "Birds are given human behaviour: arguing.", T_UPOEM, "Concept", "Do cocks really argue?", passage=POEM_QUEUE),
    K("Question 2 (c)(ii). What does the simile 'it comes like a rumour' suggest about the water?", "That it arrives gradually and spreads everywhere, hard to stop", [
        ("That it is false", "The comparison is about spreading, not falsehood."),
        ("That it is dirty", "No dirt is mentioned."),
        ("That it is silent forever", "The line says it grows 'thin, then thick, then everywhere'.")],
      "A rumour starts small and spreads.", T_UPOEM, "Interpretation", "How does a rumour spread?", passage=POEM_QUEUE),
    K("Question 2 (d)(i). Which statement describes the form of the poem?", "Free verse with no regular rhyme or metre", [
        ("Rhyming couplets", "The lines do not rhyme."),
        ("A sonnet", "A sonnet has fourteen lines and a fixed scheme."),
        ("A ballad", "A ballad has a regular stanza and rhyme.")],
      "There is no end-rhyme pattern.", T_UPOEM, "Concept", "Look at the line endings.", passage=POEM_QUEUE),
    K("Question 2 (d)(ii). Where does the mood shift in the poem?", "At 'When the water comes', from patient waiting to relief", [
        ("At the title", "The title only names the scene."),
        ("At 'Nobody speaks of the hour'", "The mood stays patient here."),
        ("There is no shift", "The final lines change the mood.")],
      "A connective 'When' marks the turn.", T_PRAC, "Interpretation", "Where does the waiting end?", passage=POEM_QUEUE),
    K("Question 2 (e). The task asks for a six-line poem about waiting for something important. Which response best fits the requirements?", "Six short lines with a pattern, concrete images and a closing turn", [
        ("A paragraph of prose cut into six lines", "The report says prose in six lines is not a poem."),
        ("A list of six facts", "A list lacks imagery and form."),
        ("A single long sentence", "A poem needs line structure.")],
      "A poem needs form, imagery and an ending.", T_PRAC, "Application", "What did the report say most scripts did wrong?"),
    N("Question 2 (f). How many lines does the poem have?", 12, "Count the lines in the poem: the first line is 'Before the cocks...' and the last is 'as towards a late and welcome guest.'", T_UPOEM, "Calculation", "Count line by line.", tol=0, passage=POEM_QUEUE),
    N("Question 2 (g). How many similes (comparisons with 'like' or 'as') does the poem contain?", 2, "'like a rumour' and 'as towards a late and welcome guest' are the two similes.", T_UPOEM, "Calculation", "Look for 'like' and 'as'.", tol=0, passage=POEM_QUEUE),
]
assert len(P3) == 20, len(P3)
SETS.append(practice_set(module=M_EXAM, topic=T_P3, title="Paper 3 practice paper A", lesson="liu2-paper-3-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P3, 203)))
