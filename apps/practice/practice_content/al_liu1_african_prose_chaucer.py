"""Practice sets for A Level Literature in English (0735), Upper Sixth: African & Post-Colonial Prose Fiction and Geoffrey Chaucer & Canonical English Poetry
(one set per lesson, 9 sets of 8 questions). Facts about set texts are limited to well-known outlines and the Board's 2023 report; passages and poems
used in questions are original, written for these sets. Essays cannot be marked automatically, so the sets test method, technique and knowledge.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("literature-in-english", "upper-sixth")

M_PROSE = "African & Post-Colonial Prose Fiction"
M_CHAUCER = "Geoffrey Chaucer & Canonical English Poetry"
T_READ = "Reading African prose fiction"
T_NARR = "Narrative perspective"
T_POST = "Post-colonial themes"
T_WRITE = "Writing about an African novel"
T_LANG = "Chaucer's language and world"
T_GP = "The General Prologue"
T_TALE = "The prescribed tale"
T_MR = "Metaphysical and Romantic poetry"
T_VM = "Victorian and Modernist poetry"


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

# ================================================================== 1. Reading African prose fiction
P1_PASSAGE = ("When the rains failed the second year, the old women of Ndu stopped quarrelling over the stream and began to share it. "
              "'A river that is dry,' said Grandmother Efua, 'teaches even enemies to carry water together.' The girls laughed, "
              "but they filled her gourd first.")

SET(M_PROSE, T_READ, "Reading an African novel: oral roots, setting, structure and purpose", "liu1-reading-african-prose", [
    K("Which of these is an oral prose form?", "A folktale told after the evening meal", [
        ("A sonnet in fourteen lines", "A sonnet is a written poetic form, not an oral prose form."),
        ("A stage direction", "Stage directions belong to written drama."),
        ("A footnote", "A footnote is a written academic device.")],
      "Oral prose forms include the folktale, myth, legend, proverb and riddle, all passed on by speaking.", "Oral prose forms", "Recall", "Which choice is spoken and in prose?"),
    K("In the passage, what is the best description of Grandmother Efua's remark about the dry river?", "A proverb-like saying that sums up a community's wisdom", [
        ("A stage direction", "Stage directions instruct actors; this is a character's speech."),
        ("A description of the plot's climax", "The remark comments on the situation; it is not the climax."),
        ("The narrator's own opinion", "The words belong to a character, though the narrator chose them.")],
      "The remark is short, memorable and general, like a proverb, and it is spoken by an elder.", "Proverbs in a novel", "Application", "Who speaks, and is the sentence general or specific?", passage=P1_PASSAGE),
    K("What does the girls' action of filling Grandmother's gourd first show?", "Respect for an elder, shown by action as well as speech", [
        ("That the girls are selfish", "They serve the elder first, which shows consideration."),
        ("That the drought has ended", "The passage says the rain has failed, not that it has returned."),
        ("That the narrator disapproves", "Nothing in the passage suggests disapproval.")],
      "Character is shown by action; their laughter is mild and the gourd shows respect.", "Characterisation by action", "Interpretation", "What do they do, rather than say?", passage=P1_PASSAGE),
    K("Which statement is a theme and not only a topic?", "Hardship can teach a community to cooperate", [
        ("Drought", "This names a subject only."),
        ("The village of Ndu", "That is a setting."),
        ("Grandmother Efua", "That is a character.")],
      "A theme makes a claim about life. Only the first option does so.", "Theme versus topic", "Concept", "Which option makes a claim?", passage=P1_PASSAGE),
    K("Which is the best example of reading for background?", "Asking when the story is set (before, during or after colonial rule) and what that history means for the characters", [
        ("Counting how many chapters the book has", "That is structure, not background."),
        ("Listing the characters in alphabetical order", "A list does not explain meaning."),
        ("Deciding whether you like the cover", "Personal reaction to the cover is not background.")],
      "Background is the history and society behind the setting; it explains why characters act as they do.", "Setting and background", "Concept", "Think of history and society."),
    K("Which sequence best lists the main points of plot structure?", "Opening situation, inciting incident, turning point, climax, resolution", [
        ("Title, author, publisher, price, date", "These are publishing details, not plot structure."),
        ("Climax, title, proverb, resolution, cover", "Title and proverb are not plot stages."),
        ("Setting, proverb, theme, tone, style", "These are literary features, not plot points.")],
      "A plot develops from a starting situation, through the event that begins the trouble, to a turning point, a climax and an ending.", "Plot and structure", "Recall", "Think of the shape of a story."),
    K("A short-notes question asks for three of five items. A candidate writes on all five. According to the Board's report, what is the likely result?", "Sketchy, thin notes that lose marks", [
        ("Extra marks for doing more", "The report says doing all five led to sketchy answers."),
        ("The marker reads only the best three", "Do not assume this; follow the instructions."),
        ("The paper is cancelled", "This is not what happens.")],
      "The report says some candidates attempted all five items and were bound to be sketchy; follow the number asked.", "Short-notes technique", "Application", "What does the report say about attempting all five?"),
    K("Which clue is most useful for working out a novelist's purpose?", "The ending of the novel and who is left speaking or surviving", [
        ("The price of the book", "Price says nothing about purpose."),
        ("The number of pages", "Length does not reveal purpose."),
        ("The colour of the cover", "Cover colour is not a literary clue.")],
      "Purpose appears in title, ending, favoured characters, images and tone. The ending is a strong clue.", "Novelist's purpose", "Reasoning", "Look inside the text."),
], seed=11)

# ================================================================== 2. Narrative perspective
N2_A = ("I did not tell my aunt about the letter. All that week I carried it folded in my school bag, and each time she smiled at me "
        "across the table I felt it grow heavier. Even now, years later, I cannot say whether I was protecting her or myself.")
N2_B = ("Mba carried the letter in her school bag all week and told no one. Her aunt, who noticed nothing, smiled at her across the table "
        "each evening. Neither of them knew that the letter would soon change the whole household.")

SET(M_PROSE, T_NARR, "Narrators, point of view and the effect of telling", "liu1-narrative-perspective", [
    K("Which statement about narrator and author is correct?", "The narrator is the voice that tells the story, and may differ from the author", [
        ("The narrator and the author are always the same person", "The narrator is a created voice; the author is the real writer."),
        ("The author is a character in every novel", "Not unless the writer makes the author a character."),
        ("The narrator only exists in poetry", "Narrators exist in prose fiction too.")],
      "The author writes the book; the narrator is the voice of the telling.", "Narrator and author", "Recall", "Who is real and who is created?"),
    K("Passage A is told by", "A first-person retrospective narrator", [
        ("A third-person omniscient narrator", "Passage A uses 'I' and looks back; it is not omniscient."),
        ("A third-person limited narrator", "Passage A is in the first person."),
        ("Several narrators", "Only one voice speaks in Passage A.")],
      "'I' shows first person; 'even now, years later' shows an older narrator looking back.", "Types of narration", "Application", "Look for the pronoun and the time marker.", passage=N2_A),
    K("What does 'Even now, years later' add to Passage A?", "An older voice that judges the younger self and admits doubt", [
        ("Suspense about the future of the household", "That is more like Passage B's last sentence."),
        ("Proof that the narrator is lying", "Nothing shows lying; the narrator expresses honest doubt."),
        ("A stage direction for actors", "Stage directions are for plays.")],
      "The phrase shows retrospective telling, where the older self comments on the past.", "Retrospective narration", "Interpretation", "Whose voice is speaking now?", passage=N2_A),
    K("In Passage B, 'Neither of them knew that the letter would soon change the whole household' is possible because the narrator is", "Omniscient, knowing more than the characters and the future", [
        ("First person", "Passage B uses 'she', not 'I'."),
        ("Unreliable", "Nothing suggests the narrator is untrustworthy."),
        ("A character in the story", "The narrator is outside the events.")],
      "Only an all-knowing narrator can tell what neither character knows.", "Omniscient narration", "Application", "Who can know the future?", passage=N2_B),
    K("The reader knows the letter will change the household, but Mba and her aunt do not. This effect is", "Dramatic irony, creating suspense", [
        ("Alliteration", "That is a sound device."),
        ("A simile", "No comparison is made with like or as."),
        ("A refrain", "Nothing is repeated.")],
      "When the reader knows more than the characters, the effect is dramatic irony.", "Dramatic irony", "Concept", "Who knows more, the characters or the reader?", passage=N2_B),
    K("Why can a first-person narrator be unreliable?", "Because the reader sees only what that narrator knows, remembers or chooses to say", [
        ("Because first-person narrators always lie", "They do not always lie; they may be honest but limited."),
        ("Because the author is absent", "The author is not the issue."),
        ("Because the novel has no plot", "Plot is not the cause.")],
      "Reliability depends on knowledge, bias and honesty, which may be limited in one voice.", "Reliability", "Reasoning", "What are the limits of one mind?"),
    K("What is a main advantage of several narrators in a novel such as Anthills of the Savannah?", "The reader gets contrasting views and must compare them", [
        ("The book becomes shorter", "The number of narrators does not shorten a book."),
        ("The author's opinion becomes obvious", "With many voices it is harder, not easier, to find one view."),
        ("Every narrator tells the same truth", "They offer different views, which is the point.")],
      "Different voices give different perspectives, and the reader weighs them.", "Multiple narrators", "Reasoning", "What do you gain when different people tell the story?"),
    K("Which sentence is the best Point for a paragraph on narrative technique?", "The retrospective narrator allows the novel to combine a young person's feeling with an adult's judgement", [
        ("The narrator uses the word 'I'", "That only names the feature."),
        ("The story is told in the past tense", "That is true of many novels and shows no effect."),
        ("The novel is about a girl", "That describes the topic, not the technique's effect.")],
      "A good Point links technique and effect.", "Writing about technique", "Application", "Which one links technique to its effect?"),
], seed=12)

# ================================================================== 3. Post-colonial themes
SET(M_PROSE, T_POST, "Colonialism, assimilation, identity and power in African fiction", "liu1-postcolonial-themes", [
    K("Which description best fits assimilation?", "Encouraging colonized people to adopt the colonizer's language and culture", [
        ("A movement of black writers in Paris", "That describes Negritude."),
        ("South Africa's legal system of racial separation", "That describes apartheid."),
        ("Continuing economic control after independence", "That describes neo-colonialism.")],
      "Assimilation is the aim of making colonized people adopt the colonizer's culture.", "Assimilation", "Recall", "Which term is about copying a culture?"),
    K("Negritude is best described as", "A movement that affirmed the value of black culture, associated with Senghor, Cesaire and Damas", [
        ("A system of laws in South Africa", "That is apartheid."),
        ("A policy of French rule", "That is closer to assimilation."),
        ("A modern African political party", "Negritude is a cultural and literary movement.")],
      "Negritude arose among black writers in the 1930s and after, and affirmed black identity.", "Negritude", "Recall", "Think of Senghor."),
    K("Which of these is the most precise meaning of neo-colonialism?", "Continuing outside control, mainly economic, after political independence", [
        ("The first period of colonial rule", "That is colonialism itself."),
        ("A kind of oral tale", "That is unrelated."),
        ("A school subject taught in missions", "That is unrelated.")],
      "Neo-colonialism, popularised by Nkrumah, means new forms of control after independence.", "Neo-colonialism", "Concept", "Neo means new."),
    K("In Nervous Conditions, why is Nyasha's story important to the theme of identity?", "She is a young woman divided between her family's rules and her experience of life in England", [
        ("She is the only educated character", "Others are educated too, such as Maiguru."),
        ("She is never in conflict with her father", "The novel shows serious conflict with her father."),
        ("She plays no role in the plot", "She is a central figure.")],
      "Nyasha's divided self illustrates hybridity and the pressure of colonial education.", "Identity in Nervous Conditions", "Reasoning", "Where has Nyasha lived, and what does she return to?"),
    K("Which reading of Anthills of the Savannah best shows that the novel is not only about outside causes?", "It shows rulers of a free country neglecting the poor and abusing power", [
        ("It says independence solved every problem", "The novel does not claim this."),
        ("It is only a love story", "Love is present, but the novel's power and politics matter."),
        ("It has no link to politics", "It has a clear link to power and its abuse.")],
      "The Abazon drought and abuse of power show internal failure after independence.", "Power in Anthills", "Reasoning", "Think of the Abazon drought."),
    K("A student writes 'The novel is about colonialism' and gives no evidence. What is the main weakness?", "A one-word label with no event and no explanation", [
        ("The sentence is too long", "It is short."),
        ("It uses the present tense", "That is correct usage."),
        ("It names the novel", "Naming the novel is not a fault.")],
      "Labels need evidence and explanation; the Board's report warns against vague narration.", "Using evidence", "Application", "What does the claim lack?"),
    K("For a question on The Lady With a Beard asking for Bakossi traditional values as a microcosm of African traditional society, the best approach is to", "Give local Bakossi details first, then show how they represent wider African tradition", [
        ("Write only about general African history", "The question asks for the local details to be shown first."),
        ("Ignore the text and write about colonialism", "The question is about traditional values."),
        ("Narrate the whole story", "The report warns against narration.")],
      "A microcosm is a small picture of a larger whole; the local details must come first.", "Microcosm", "Application", "What is a microcosm?"),
    K("Which sentence best evaluates a post-colonial reading?", "It links private lives to history but can overlook faults that come from within a society", [
        ("It is always completely correct", "No reading explains everything."),
        ("It has nothing to say about identity", "It has much to say about identity."),
        ("It applies only to poetry", "It applies to prose, drama and poetry.")],
      "A balanced evaluation names a strength and a limit.", "Evaluating a reading", "Reasoning", "Which answer gives both a strength and a limit?"),
], seed=13)

# ================================================================== 4. Writing about an African novel
SET(M_PROSE, T_WRITE, "Planning and writing prose essays and short notes", "liu1-writing-african-novel", [
    K("In the question 'To what extent do you agree?', what should a good answer do?", "Take a position, support it with evidence and acknowledge a limit", [
        ("Agree completely without examples", "Without evidence the answer cannot score."),
        ("Narrate the whole story", "The report criticises narration."),
        ("Avoid giving an opinion", "'To what extent' wants a position.")],
      "An extent question wants a position, evidence and a counter-point.", "Question tags", "Recall", "What does 'extent' ask for?"),
    K("Which is the best description of a dramatic episode?", "A scene of high tension and importance whose effects you can explain", [
        ("Any action in the book", "The report says candidates lost marks by treating any action as a dramatic episode."),
        ("A character description", "A description is not an episode."),
        ("The author's biography", "That is background, not an episode.")],
      "A dramatic episode is important and tense; effectiveness is what it achieves.", "Dramatic episode", "Concept", "Is the event tense and important?"),
    K("In a question on three dramatic episodes, a candidate spends most of the answer retelling each scene and only one line on its effect. This is weak because", "The question asks for effectiveness, not retelling", [
        ("Retelling is never allowed", "Brief description is needed, but significance matters most."),
        ("Three episodes are too many", "The question asked for three."),
        ("Episodes cannot be discussed", "They can, and must be.")],
      "The better answers describe briefly and then explain significance.", "Effectiveness", "Reasoning", "What does the question ask for?"),
    K("A short-note question numbers the items 1 to 5 and asks for three. How should you answer?", "Choose three, keep the numbers, and for each identify, illustrate and give significance", [
        ("Answer all five briefly", "That risks sketchy answers and wastes time."),
        ("Write one long paragraph on the whole novel", "The question asks for separate numbered notes."),
        ("Answer only one in detail", "Three notes are required.")],
      "Follow the instruction and use the three-step pattern.", "Short notes", "Application", "How many items are asked for?"),
    K("A question asks for two relieving and two destructive love experiences. A candidate writes about three relieving experiences only. What is the main fault?", "The answer is lopsided and does not balance both sides", [
        ("Love cannot be discussed", "It can be discussed."),
        ("Three experiences is too many", "The fault is the missing second side."),
        ("The candidate used the present tense", "The present tense is correct.")],
      "Two-sided questions need balance; the report notes many lopsided answers.", "Two-sided questions", "Reasoning", "What does 'both' require?"),
    K("Which opening sentence of a paragraph is the best topic sentence for a question on the theme of gender inequality?", "The novelist shows that women's rights are ignored in key events of the community", [
        ("In the novel there are many people", "It says nothing about the question."),
        ("First, then, after that", "This begins a retelling."),
        ("I liked the book", "A personal reaction is not a point.")],
      "A topic sentence answers the question and can be proved.", "Topic sentences", "Application", "Which one makes a claim?"),
    K("The Board's report says one sketchy illustration in a paragraph earns", "A skimpy mark, while several apt illustrations make the paragraph fuller and better", [
        ("Full marks", "A single sketchy illustration does not earn full marks."),
        ("No marks at all", "It earns some marks, but only a little."),
        ("The same as three illustrations", "More focused illustrations earn more.")],
      "The report says the more focused illustrations a paragraph has, the better.", "Illustrations", "Recall", "What does the report advise?"),
    K("Which habit best helps a candidate on a three-character question to avoid mixing up characters?", "Keeping a one-page list of characters with two or three events for each", [
        ("Memorising the cover", "The cover does not help."),
        ("Reading only the first chapter", "Late events would be missed."),
        ("Writing the answer without a plan", "Planning prevents confusion.")],
      "A character-and-event list gives quick, correct evidence.", "Revision method", "Application", "What helps you recall characters and events?"),
], seed=14)

# ================================================================== 5. Chaucer's language and world
SET(M_CHAUCER, T_LANG, "Middle English, verse form and the medieval background", "liu1-chaucer-language-world", [
    K("In which century did Chaucer write The Canterbury Tales?", "The fourteenth", [
        ("The twelfth", "That is the era of early Middle English, before Chaucer's time."),
        ("The sixteenth", "That is Shakespeare's era."),
        ("The nineteenth", "That is the Victorian era.")],
      "Chaucer lived from about 1343 to 1400 and wrote the Tales in the 1380s and 1390s.", "Chaucer's date", "Recall", "He died in 1400."),
    K("What is Middle English?", "The English of about 1100 to 1500, shaped by Old English and by French after the Norman Conquest", [
        ("The English of Shakespeare", "That is early modern English."),
        ("A dialect of French", "It is English, though it borrowed French words."),
        ("A modern slang", "Middle English is a medieval stage of the language.")],
      "Middle English came after Old English and before modern English.", "Middle English", "Concept", "Think of the Norman Conquest of 1066."),
    K("What does 'The droghte of March hath perced to the roote' mean?", "The dryness of March has pierced to the root", [
        ("March will soon become dry", "The verb is perfect: 'has pierced'."),
        ("The roots of March are dead", "March is a month, not a plant."),
        ("A drought will end the spring", "The line describes spring's rain reaching the dry ground.")],
      "Hath perced = has pierced; droghte = dryness.", "Reading Middle English", "Application", "Use the glossary: hath = has."),
    K("A line has ten syllables with a weak-strong pattern five times. It is in", "Iambic pentameter", [
        ("Trochaic tetrameter", "Trochaic means strong-weak, and tetrameter means four feet."),
        ("Anapestic trimeter", "Anapests have three syllables each."),
        ("Free verse", "Free verse has no fixed pattern.")],
      "Five iambs make iambic pentameter.", "Iambic pentameter", "Recall", "Count the beats."),
    K("Two rhyming lines of iambic pentameter in a row are called", "A heroic couplet", [
        ("A refrain", "A refrain is a repeated line."),
        ("A sestet", "A sestet is six lines."),
        ("A quatrain", "A quatrain is four lines.")],
      "Pairs of rhyming iambic pentameter lines are heroic couplets.", "Couplet", "Recall", "How many lines in the pair?"),
    K("Which describes the three estates?", "Those who fight, those who pray and those who work", [
        ("Rich, middle and poor merchants only", "That is not the standard division."),
        ("King, queen and prince", "That is not the three estates."),
        ("Poets, painters and musicians", "That is not the medieval division.")],
      "The medieval three estates were knights, clergy and workers.", "Three estates", "Recall", "Think of Knight, Monk and Plowman."),
    K("Why is the pilgrimage a good frame for a poem about many kinds of people?", "A pilgrimage brought people of different estates together on one road", [
        ("Only kings made pilgrimages", "Pilgrims came from all estates."),
        ("Pilgrims did not speak to each other", "The poem depends on their talking and storytelling."),
        ("Pilgrimage was a legal punishment only", "It was also an act of faith and a holiday.")],
      "The shared journey allows a cross-section of society to meet.", "Pilgrimage frame", "Reasoning", "Who could take part in a pilgrimage?"),
    K("Which background idea does the Board's report name for Chaucer?", "Feudalism, religion, chivalry, love, and medieval scholarship and medicine", [
        ("Industrial capitalism", "That belongs to a later period."),
        ("Space travel", "Unrelated."),
        ("Modern democracy", "Unrelated to the medieval setting.")],
      "The report names these background areas for the General Prologue and the tale.", "Background issues", "Recall", "Which choice fits the Middle Ages?"),
], seed=15)

# ================================================================== 6. The General Prologue
SET(M_CHAUCER, T_GP, "The General Prologue: frame, portraits and satire", "liu1-general-prologue", [
    K("Where do the pilgrims gather before the journey?", "The Tabard Inn in Southwark", [
        ("Canterbury Cathedral", "That is their destination, not the starting place."),
        ("A palace in London", "They meet at an inn."),
        ("A ship at the harbour", "The journey is by road.")],
      "The narrator meets the company at the Tabard Inn, Southwark.", "The frame", "Recall", "It is an inn."),
    K("What does the Host propose?", "A storytelling contest on the road, with a supper as the prize", [
        ("A race to Canterbury", "The contest is about stories."),
        ("A debate about religion", "The proposal is for tales."),
        ("A lottery for the pilgrims' money", "The prize is a supper paid by the others.")],
      "Harry Bailly proposes tales as entertainment and offers to judge.", "The Host", "Recall", "What do the pilgrims do to pass the time?"),
    K("The narrator praises the Monk and agrees with him that studying in a cloister is pointless. The main effect of this is", "Irony that exposes the Monk's neglect of his vows", [
        ("Praise that Chaucer sincerely holds", "The facts contradict the praise."),
        ("A rhyme scheme", "The effect is about meaning, not sound."),
        ("A stage direction", "Stage directions belong to plays.")],
      "The narrator pretends to agree; the reader sees the failing.", "Irony", "Application", "Does the praise fit the facts?"),
    K("Which pair of pilgrims does the report treat as models of virtue?", "The Knight and the Parson (with the Plowman)", [
        ("The Pardoner and the Summoner", "Both are shown as corrupt."),
        ("The Miller and the Reeve", "Both are shown with faults."),
        ("The Friar and the Monk", "Both are satirised.")],
      "The report says Chaucer praises the Knight, Parson and Plowman as models.", "Praise and satire", "Recall", "Which pilgrims are not mocked?"),
    K("The Doctor of Physic is compared to Hippocrates and other famous physicians, though he loves gold. This is mainly", "A classical allusion used with hyperbole", [
        ("Alliteration", "The device is about reference and exaggeration."),
        ("A pun on the Doctor's name", "No pun is intended."),
        ("A biblical allusion to Judith", "Judith belongs to the Merchant's Tale and is a biblical figure.")],
      "The report names Hippocrates (and Rufus) as classical allusions that exaggerate the Doctor's status.", "Allusion", "Application", "Who is Hippocrates?"),
    K("Which best explains verisimilitude in the General Prologue?", "Real places and concrete detail make the pilgrims and the setting seem true", [
        ("The poem is written in Latin", "It is in English."),
        ("The pilgrims are all kings", "They are ordinary and varied."),
        ("The poem has no narrator", "The narrator is a key device.")],
      "Verisimilitude is the appearance of truth, made by detail and real settings.", "Verisimilitude", "Concept", "What makes the scene seem real?"),
    K("Which answer to 'Chaucer is a social critic' is strongest?", "It names several areas (Church, trade, marriage), gives examples from several pilgrims, and names the tools of satire", [
        ("It describes only the Knight", "The Knight is a model, not a target."),
        ("It retells each portrait without a point", "The report criticises narration."),
        ("It uses only one pilgrim", "The report asks for at least four areas.")],
      "The report asks for at least four areas of criticism with tools and examples.", "Satire essay", "Reasoning", "What does the report want in a social-critic answer?"),
    K("A candidate repeats the Friar example to support three different points. The report would say this", "Does not score well, because repeated illustration for different points is weak", [
        ("Shows excellent range", "The report says repeated illustration does not score well."),
        ("Earns top marks", "It does not."),
        ("Is the only way to write about the Friar", "Different points need different examples.")],
      "The report warns against repeating similar illustrations for different points.", "Using evidence", "Reasoning", "Does the report praise repetition?"),
], seed=16)

# ================================================================== 7. The prescribed tale
SET(M_CHAUCER, T_TALE, "The Merchant's and Franklin's tales: outline, theme and allusion", "liu1-prescribed-tale", [
    K("Which tales does the Board's 2023 report name for the General Prologue questions?", "The Merchant's Prologue and Tale (new syllabus) and the Franklin's Prologue and Tale (old syllabus)", [
        ("The Miller's Tale and the Reeve's Tale", "The report does not name these."),
        ("The Knight's Tale only", "The Knight's Tale is not named for the Section C questions."),
        ("The Pardoner's Tale and the Nun's Priest's Tale", "The report does not name these.")],
      "The report names the Merchant's and the Franklin's Prologue and Tale, one for each syllabus.", "Prescribed tales", "Recall", "Which two names appear in the report?"),
    K("In the Merchant's Tale, which character is the elderly knight who marries a young wife?", "January", [
        ("Justinus", "Justinus is the cautious counsellor."),
        ("Damian", "Damian is the squire who loves May."),
        ("Pluto", "Pluto is the king of the fairies.")],
      "January marries May; Justinus advises caution and Damian loves May.", "Characters (Merchant's Tale)", "Recall", "He is the husband."),
    K("In the Merchant's Tale, what is the setting of the central deceit?", "A walled garden with a pear tree", [
        ("A ship at sea", "The deceit takes place in the garden."),
        ("A cathedral", "The tale's key scene is in a garden."),
        ("A battlefield", "It is not a war tale.")],
      "January's enclosed garden is the setting of the pear-tree scene.", "Setting (Merchant's Tale)", "Recall", "Where does January keep the key?"),
    K("Which of these is classical allusion in the Merchant's Tale?", "Pluto and Proserpina, the gods who watch the pear-tree scene", [
        ("The Tabard Inn", "That is a real place in the General Prologue."),
        ("Thomas Becket", "That is a historical allusion in the General Prologue."),
        ("The Rule of St Benet", "That is a literary or religious text alluded to in the General Prologue.")],
      "Pluto and Proserpina come from classical myth.", "Allusion types", "Application", "Which names are from myth?"),
    K("In the Franklin's Tale, what promise does Dorigen make to Aurelius?", "To love him if he removes the rocks from the coast", [
        ("To give him gold", "She promises love, not gold."),
        ("To go to England with him", "Her husband goes to England."),
        ("To tell her husband nothing", "She does tell her husband.")],
      "She makes the promise half in jest, thinking it impossible.", "Plot (Franklin's Tale)", "Recall", "It involves dangerous rocks."),
    K("What is the main idea behind the Franklin's closing question?", "Which of the three, Arveragus, Aurelius or the clerk, acted most generously", [
        ("Which of them is the richest", "The question is about generosity."),
        ("Which of them is the oldest", "Age is not the issue."),
        ("Which of them is the best traveller", "Travel is not the issue.")],
      "The Franklin asks his hearers to judge generosity, a theme of gentilesse.", "Theme (Franklin's Tale)", "Concept", "What does the tale end with?"),
    K("Why is the Merchant's own prologue important for his tale?", "It shows his bitterness about marriage, which colours the story of January and May", [
        ("It tells us the plot in full", "It does not narrate the tale."),
        ("It has no link to the tale", "The teller's mood shapes the tale."),
        ("It praises marriage without irony", "The Merchant speaks bitterly.")],
      "Tale and teller are linked: the Merchant's bitter view shapes the story.", "Tale and teller", "Reasoning", "What does the Merchant say about his marriage?"),
    K("A student answers a question on both texts using only the General Prologue. The report would say this answer", "Cannot perform well, because it limits itself to one of the two texts", [
        ("Earns top marks", "The report says limiting to the General Prologue cannot perform well."),
        ("Is acceptable if it is long", "Length does not fix the missing text."),
        ("Is better than using the tale", "Both are expected.")],
      "The report says those who limit themselves to the General Prologue cannot perform well.", "Linking the texts", "Application", "What does the report say about speculation and limiting?"),
], seed=17)

# ================================================================== 8. Metaphysical and Romantic poetry
MR_POEM1 = ("Though road and river keep us far apart,\nWe are two clocks wound by one single hand;\n"
            "Each tick of mine is echoed in your heart,\nAnd time itself must learn to understand.")
MR_POEM2 = ("The rain has gone; each leaf is hung with light,\nThe red road steams beneath the climbing sun,\n"
            "And one small bird I cannot name takes flight\nTo sing the day that has not yet begun.")

SET(M_CHAUCER, T_MR, "Wit, conceit, nature, imagination and symbol", "liu1-metaphysical-romantic", [
    K("Which poet is associated with Metaphysical poetry?", "John Donne", [
        ("John Keats", "Keats is a Romantic poet."),
        ("Alexander Pope", "Pope belongs to the earlier eighteenth century."),
        ("T. S. Eliot", "Eliot is a Modernist poet.")],
      "Donne, Herbert and Marvell are the best-known Metaphysical poets.", "Metaphysical poets", "Recall", "Seventeenth century."),
    K("What is a conceit?", "An extended, surprising comparison worked out like an argument", [
        ("A short simile with 'like'", "A conceit is extended, not short."),
        ("A line that repeats", "That is a refrain."),
        ("A stanza of four lines", "That is a quatrain.")],
      "A conceit is the signature device of Metaphysical poetry.", "Conceit", "Recall", "It is clever and extended."),
    K("In the four lines above, the comparison is", "A conceit: the lovers are compared to two clocks wound by one hand", [
        ("Personification of a river", "The river is part of the separation, not the main comparison."),
        ("A refrain", "No line is repeated."),
        ("An onomatopoeia", "There is no sound word.")],
      "The lovers become two clocks wound by one hand: an extended comparison.", "Identifying a conceit", "Application", "What two things are compared?", passage=MR_POEM1),
    K("Why does the conceit suit the poem's idea?", "Clocks that share a spring share a fate, which supports the idea that the lovers are linked", [
        ("Clocks are always broken", "That is not the poem's idea."),
        ("Clocks are noisy", "Noise is not the point."),
        ("Clocks are expensive", "Cost is not the point.")],
      "The mechanical image argues that what happens to one affects the other.", "Effect of conceit", "Reasoning", "Think about what a shared spring means.", passage=MR_POEM1),
    K("Which feature of the four lines above is most typical of Romantic poetry?", "The link between nature and feeling: the landscape brightens and the speaker's mood lifts", [
        ("A strict logical argument with 'if... then...'", "That is more typical of Metaphysical poetry."),
        ("A mock-epic style", "That is Pope's style."),
        ("A formal address to a monarch", "That is not Romantic.")],
      "The poem links nature and emotion.", "Romantic features", "Application", "What changes with the weather?", passage=MR_POEM2),
    K("Which element is an appeal to the sense of sight in these lines?", "'each leaf is hung with light'", [
        ("'one small bird I cannot name'", "That refers to a bird, and later sound, not sight of light."),
        ("'To sing the day'", "That is a sound image."),
        ("'has not yet begun'", "That is about time, not sight.")],
      "The leaf hung with light is a visual image.", "Imagery", "Application", "Which line gives something you can see?", passage=MR_POEM2),
    K("The Rape of the Lock by Alexander Pope is best described as", "A mock-epic that treats a trivial event in the grand style of epic poetry", [
        ("A Romantic ode about a nightingale", "That is Keats's world."),
        ("A Metaphysical love poem", "It is eighteenth-century satire."),
        ("A Modernist fragment", "It uses regular heroic couplets.")],
      "Pope uses epic conventions to laugh at fashionable vanity.", "Mock-epic", "Concept", "Pope wrote in heroic couplets."),
    K("The Board's report mentions the idea that symbolism is a hallmark of Keats's poetry. A good answer would", "Show how objects, characters or setting act as symbols in at least three poems from the selection", [
        ("Retell the biography of Keats", "The report warns against background without focus."),
        ("Use one poem only", "The question asked for any three poems."),
        ("Describe Pope's poem", "Pope is not Keats.")],
      "A symbolism answer uses objects, characters and settings in several poems.", "Keats and symbolism", "Reasoning", "How many poems were asked for?"),
], seed=18)

# ================================================================== 9. Victorian and Modernist poetry
VM_POEM1 = ("You ask me, sir, why I still keep the clock\nWound and the lamps all trimmed, when no one comes?\n"
            "The railway left this valley years ago.")
VM_POEM2 = ("Plastic sheets. The long light\nslides off the zinc.\nA radio says rain, says price, says\nsomewhere a war.")

SET(M_CHAUCER, T_VM, "Victorian and Modernist poetry: forms, voices and effects", "liu1-victorian-modernist", [
    K("A dramatic monologue is", "A poem in which a character speaks to a silent listener and reveals himself or herself", [
        ("A poem with no speaker", "A dramatic monologue has a clear speaker."),
        ("A poem written by two poets", "It is about voice, not authorship."),
        ("A poem in free verse only", "Form varies; many use blank verse.")],
      "The speaker is a character who reveals personality.", "Dramatic monologue", "Recall", "Think of Browning."),
    K("In the lines above, which phrase shows that the speaker has a listener?", "'You ask me, sir'", [
        ("'The railway left'", "That states a fact."),
        ("'all trimmed'", "That describes lamps."),
        ("'years ago'", "That marks time.")],
      "'You ask me, sir' addresses a listener.", "Dramatic monologue features", "Application", "Who is 'you'?", passage=VM_POEM1),
    K("The lines above are unrhymed with ten syllables and a weak-strong beat. They are written in", "Blank verse", [
        ("Free verse", "Free verse has no fixed beat."),
        ("Heroic couplets", "Couplets rhyme."),
        ("A sonnet", "A sonnet is fourteen lines with rhyme.")],
      "Unrhymed iambic pentameter is blank verse.", "Blank verse", "Concept", "Is there rhyme?", passage=VM_POEM1),
    K("Which context most helps to explain Victorian poems of doubt?", "Scientific discoveries such as Darwin's challenged older ideas about creation", [
        ("The invention of the telephone only", "That is not the main context for doubt."),
        ("The end of the First World War", "That belongs to Modernism."),
        ("The Norman Conquest", "That belongs to the Middle Ages.")],
      "Darwin's work (1859) challenged older beliefs and fed doubt.", "Victorian context", "Concept", "Think of the 1850s."),
    K("The lines above use short lines, fragments and no rhyme. This is", "Free verse with fragmentation", [
        ("Blank verse", "Blank verse is regular iambic pentameter."),
        ("A heroic couplet", "Couplets rhyme."),
        ("A ballad", "A ballad has a regular rhyme and stanza.")],
      "Free verse has no fixed pattern; fragments are typical of Modernism.", "Free verse", "Application", "Does it rhyme or have a regular beat?", passage=VM_POEM2),
    K("The radio news is placed next to the market scene with no comment. This technique is", "Juxtaposition", [
        ("Alliteration", "That is repeated consonant sound."),
        ("A refrain", "Nothing repeats."),
        ("A mock-epic", "That is Pope's style.")],
      "Placing two things side by side lets the reader supply the link.", "Juxtaposition", "Concept", "What is next to what?", passage=VM_POEM2),
    K("Which sentence best compares the two poems?", "Both show people facing change, but the first states its case in order while the second implies meaning through fragments", [
        ("Both are written in rhyming couplets", "Neither is in rhyming couplets."),
        ("Neither has a theme", "Both have themes."),
        ("The first is free verse and the second is blank verse", "It is the other way round.")],
      "A comparison names a similarity and a difference.", "Comparison", "Reasoning", "Check the forms."),
    K("A student writes 'the poet is proud' about a dramatic monologue's speaker. What is wrong?", "The speaker is a created character, not the poet", [
        ("Nothing: speaker and poet are always the same", "They are usually different in a dramatic monologue."),
        ("The student used the present tense", "The present tense is correct."),
        ("Pride cannot be discussed", "It can, but it belongs to the speaker.")],
      "Write 'the speaker' for the voice and avoid confusing it with the author.", "Speaker and poet", "Application", "Who speaks in a monologue?"),
], seed=19)
