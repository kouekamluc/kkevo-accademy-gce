"""Practice sets for A Level Literature in English (0735), Lower Sixth: Modern British/American & African Drama, Canonical English & American Prose
Fiction and Examination (one set per lesson, 11 sets), plus 'Paper 1 mock exam A' (50 multiple-choice questions across all four Lower Sixth
modules), 'Paper 2 practice paper A' (25 auto-markable parts on planning, question types and technique) and 'Paper 3 practice paper A' (20 parts on
invented unseen passages and an invented drama extract). All passages, extracts and poems are original and invented; facts about set texts are
limited to well-known outlines and the points the Board's 2023 report mentions. Essays cannot be marked automatically, so these sets test method
and understanding.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("literature-in-english", "lower-sixth")

M_DRAMA = "Modern British/American & African Drama"
M_PROSE = "Canonical English & American Prose Fiction"
M_EXAM = "Examination"

T_ARI = "Aristotle's Poetics and tragedy"
T_PRO = "Prosody and scansion"
T_NAR = "Narrative theory"
T_CRI = "Critical approaches"
T_READ = "Reading Shakespeare's plays"
T_TRA = "Tragedy in Shakespeare"
T_COM = "Comedy and history in Shakespeare"
T_WSH = "Writing about a Shakespeare play"
T_MOD = "Modern drama and stagecraft"
T_CHD = "Characterization in modern drama"
T_AFR = "African drama and social themes"
T_CMP = "Comparing plays"
T_NOV = "Reading the 19th and 20th century novel"
T_NVO = "Narrative voice and structure"
T_CTN = "Character and theme in the prescribed novels"
T_WNV = "Writing about a novel"


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


SETS = []


def SET(module, topic, title, lesson, specs, seed, **kw):
    assert len(specs) == 8, title
    SETS.append(practice_set(module=module, topic=topic, title=title, lesson=lesson, questions=build(specs, seed), **kw))

# ================================================================== 1. Modern drama and stagecraft
SET(M_DRAMA, T_MOD, "Stagecraft: set, props, directions and production", "lil2-modern-drama-stagecraft", [
    K("Which of these is a stage direction?", "(She puts the letter down and does not look at him.)", [
        ("You promised to come before dark.", "That is dialogue, something a character says."),
        ("ACT TWO", "That is a division of the play, not a direction about action."),
        ("The play was first performed in a hall.", "That is information about the production, not a direction inside the script.")],
      "Stage directions describe action, sound, light or manner and are normally in brackets.", "Stage directions", "Recall", "Look for the words describing what a character does, not says."),
    K("In stage terms, which area is nearest the audience?", "Downstage", [
        ("Upstage", "Upstage is at the back of the stage, farthest from the audience."),
        ("Stage left", "Stage left is a side, not the front or back."),
        ("Backstage", "Backstage is the area behind and out of view of the audience.")],
      "Downstage is the front of the stage, near the audience; upstage is the back.", "Stage areas", "Recall", "Think of the stage sloping down to the audience."),
    K("In A Raisin in the Sun, the plant that Mama cares for is best understood as", "a small prop that stands for hope and growth", [
        ("a costume that shows her wealth", "A plant is not a costume, and the family is not wealthy."),
        ("a lighting effect", "A plant is a physical prop, not light."),
        ("a stage direction about music", "It is an object on the set, not a sound direction.")],
      "Props can carry symbolic meaning; the plant stands for Mama's hopes for her family's growth.", "Props and symbols", "Concept", "Is it an object actors handle?"),
    K("A producer notes that a play needs only everyday clothes, a table and two chairs. She is describing", "production facilities", [
        ("audience appeal", "Audience appeal is about interest and enjoyment."),
        ("a production difficulty", "These items are easy to find, so they are not a difficulty."),
        ("the theme of the play", "A theme is an idea, not a list of items.")],
      "Simple and cheap props and costume are production facilities.", "Production facilities", "Application", "Is she describing what is easy or what is hard?"),
    K("Which feature of a production of And Palm-Wine Will Flow does the Board's report call a difficulty?", "Showing a ritual of women at twin streams and the loss of farmland on stage", [
        ("The costumes, which are very expensive", "The report says costumes are familiar and affordable."),
        ("The large cast, which is hard to manage", "The report says the cast is limited."),
        ("The night lighting needed for every scene", "The report says daylight performance removes the need for complicated lights.")],
      "The report says costumes, props, cast and settings are easy; the ritual and the farmland are hard to realise.", "Production difficulties", "Interpretation", "Which scenes are about water and land?"),
    K("Death of a Salesman lets Willy step into scenes from the past without changing the scene. Which stagecraft makes this possible?", "A set that treats walls as if they were not there, with changes of light and music", [
        ("A narrator who tells the audience about the past", "The play shows the past through staging, not a narrator's telling."),
        ("A curtain closing between every memory", "The point is that memory flows into the present without breaks."),
        ("A chorus of villagers", "A chorus belongs to other forms of drama; it is not how Salesman presents memory.")],
      "Light, music and a set without solid walls allow past and present to move into each other.", "Realism and memory", "Concept", "How does the stage show Willy's mind?"),
    K("A candidate is asked about production difficulties and writes only about how much the audience would enjoy the play. What is wrong?", "The answer addresses audience appeal and not the practical difficulties asked for", [
        ("Nothing, because audience appeal is the same as production", "The report separates the two sides."),
        ("The candidate used too many props", "The problem is the focus, not the number of props."),
        ("The candidate wrote in the future tense", "Tense is not the issue.")],
      "The report warns candidates against answering audience appeal when production facilities and difficulties are asked for.", "Answering the question", "Reasoning", "What did the question ask for?"),
    K("(She enters, shaking rain from her coat, and does not look at him.) What does this direction mainly suggest?", "Tension: she is hiding something", [
        ("That she is cheerful", "Avoiding his eyes suggests the opposite."),
        ("That it is morning", "Rain and a coat suggest weather, not the time of day."),
        ("That the play is a comedy", "The direction alone does not tell the genre; it suggests unease.")],
      "Not looking at someone is a sign of guilt or tension.", "Effect of stage directions", "Interpretation", "What does avoiding someone's eyes usually suggest?"),
], 1)

# ================================================================== 2. Characterization
SET(M_DRAMA, T_CHD, "Characterization: methods, roles and the playwright's attitude", "lil2-characterization-drama", [
    K("Which is NOT a method of characterization in drama?", "The number of acts in the play", [
        ("What other characters say about the person", "This is a standard method."),
        ("What the character does", "Action reveals character."),
        ("The character's own speech", "Speech reveals character.")],
      "The number of acts is a structural feature, not a way of building character.", "Methods of characterization", "Recall", "Which choice is not about the person?"),
    K("A character whose qualities contrast with another's, making both clearer, is called a", "foil", [
        ("protagonist", "The protagonist is the main character."),
        ("chorus", "A chorus is a group that comments on the action."),
        ("narrator", "A narrator tells the story, which is not a role in a play like this.")],
      "A foil is a contrasting character.", "Foil", "Recall", "Think of a character set against another."),
    K("In A Raisin in the Sun, which character is a foil to Asagai?", "George Murchison", [
        ("Travis", "Travis is a child, not a suitor."),
        ("Mama", "Mama is a parent figure, not a contrast in values for Beneatha's suitors."),
        ("Ruth", "Ruth is Walter's wife.")],
      "George wants to fit into the white world; Asagai looks to Africa.", "Foil in Raisin", "Application", "Which suitor has opposite values?"),
    K("The Board's report says a candidate wrote that Mama and Ruth conform to the white world because they work for white people. What is the error?", "Working in a white household is an economic fact and does not show acceptance of white values", [
        ("Mama and Ruth are not in the play", "They are both in the play."),
        ("They do not work", "The report's wording says they are servants to rich whites."),
        ("The candidate used the wrong play", "The text is the one the question asked about.")],
      "The report says candidates confused being employed with conforming. Beneatha's ambition was also misread.", "Reading characters", "Reasoning", "Is working for someone the same as accepting their values?"),
    K("'Butake's attitude towards the women is one of admiration.' This sentence correctly states", "the playwright's attitude", [
        ("a character's role", "A role would say what the women do."),
        ("the plot", "It does not narrate events."),
        ("the setting", "It names no place or time.")],
      "Attitude means the writer's feeling about the characters; admiration is an attitude.", "Role and attitude", "Concept", "Is it about what the women do or how the writer sees them?"),
    K("According to the Board's report, a full answer about Willy Loman's failure should also consider", "the contributions of other characters and outside forces", [
        ("only Willy's own illusions", "That is the one-sided answer the report criticises."),
        ("the writer's biography", "The report does not require this."),
        ("the cost of the production", "This is stagecraft and not the question.")],
      "The report says good answers give a critical perspective: how others and external forces pushed Willy.", "Critical perspective", "Interpretation", "Is Willy alone responsible?"),
    K("'Willy is self-deceiving: he tells Linda sales are going well when they are not.' This sentence is a good character point because it", "gives an adjective and supports it with evidence", [
        ("only retells the plot", "It also states a quality."),
        ("gives the writer's biography", "It names no biography."),
        ("lists stage directions", "It contains no stage directions.")],
      "Strong character points give an adjective and evidence.", "Adjective plus evidence", "Application", "What two parts does the sentence have?"),
    K("A candidate writes only: 'Walter is a good man.' What is the best improvement?", "Add specific moments that show his strengths and weaknesses and say what they show", [
        ("Say he is a bad man instead", "A one-word verdict is still a verdict without evidence."),
        ("Add the date the play was written", "A date does not describe the character."),
        ("Quote a long passage from memory", "Long quotations from memory risk mistakes and do not explain anything.")],
      "Evidence and explanation turn an opinion into an argument.", "Evidence", "Application", "What is missing from the sentence?"),
], 2)

# ================================================================== 3. African drama and social themes
SET(M_DRAMA, T_AFR, "African drama: oral tradition, satire and social themes", "lil2-african-drama-social-themes", [
    K("Which is an element of oral tradition that appears in many African plays?", "Song and proverbs", [
        ("Printed footnotes", "Footnotes belong to print, not oral performance."),
        ("Silent reading", "Oral tradition is performed and heard."),
        ("A written preface", "A preface is a written feature.")],
      "Oral tradition appears as song, dance, proverb, praise-name and ritual.", "Oral tradition", "Recall", "Which choice is spoken or sung?"),
    K("Satire is best defined as", "humour and irony used to criticise wrongdoing or foolishness", [
        ("praise of a ruler", "Satire criticises."),
        ("a history of a people", "That is history, not satire."),
        ("a sad song at a funeral", "That is a dirge, not satire.")],
      "Satire exposes faults through humour.", "Satire", "Recall", "Does satire praise or criticise?"),
    K("According to the Board's report, the social ill linked to the extract of A Dance of the Forests that mentions the seventy is", "bribery and corruption", [
        ("drought", "The report does not mention drought."),
        ("illiteracy", "The report does not mention illiteracy."),
        ("war", "The report does not link the extract to war.")],
      "The report says candidates were expected to identify bribery and corruption.", "Social themes", "Recall", "What did someone take to allow an unsafe journey?"),
    K("In the report's description of the same extract, Adenebi is shown as", "sensitive to accusation and hypocritical", [
        ("brave and honest", "The report's wording points to hypocrisy and defensiveness."),
        ("a child", "He is an official, not a child."),
        ("a spirit of the forest", "The report discusses the character in the human world of the extract.")],
      "The report says his words show sensitivity to accusation and a pretentious nature.", "Impression of a character", "Interpretation", "How does he react when blamed?"),
    K("The Board's report says Butake's portrayal of women is mainly", "admiring and sympathetic, with criticism of the fon who takes their land", [
        ("contemptuous of the women", "The report describes admiration, not contempt."),
        ("neutral, with no attitude", "The report says attitude is expected to be expressed with adjectives."),
        ("in support of the fon", "The fon is the cause of the injustice.")],
      "Butake admires the women's resilience and courage and sympathises with their treatment.", "Playwright's attitude", "Interpretation", "Whose side does the writer take?"),
    K("A task says: 'As a reporter, write one paragraph with four reasons why bribe-takers should be punished.' Which feature must the answer have?", "A caption and one paragraph with four reasons", [
        ("A poem of six lines", "That is a different task."),
        ("A long essay of five paragraphs", "The task asks for one paragraph."),
        ("Only a list of names", "The task asks for reasons.")],
      "The report notes some candidates lost marks for failing to give a caption or keep to one paragraph.", "Creative task", "Application", "What form is a report?"),
    K("Why is And Palm-Wine Will Flow described as easy to stage in the report?", "Small cast, familiar costumes, simple settings and daylight performance", [
        ("It needs real water on stage", "Real water is a difficulty."),
        ("It needs a large crowd of extras", "The cast is limited."),
        ("It has no characters", "It has characters."),],
      "The report lists costumes, props, cast, settings and daylight as facilitating production.", "Production", "Recall", "Which choices make production cheap and simple?"),
    K("An answer says 'Soyinka uses songs.' with no further comment. What is missing?", "What the songs do for theme, mood or character", [
        ("A plot summary of the play", "The answer needs effect, not narration."),
        ("The date of the play", "A date does not explain effect."),
        ("The writer's biography", "Biography does not explain effect.")],
      "Naming a device earns little; say what it does.", "Effect of devices", "Reasoning", "Which word do the report's comments stress: effectiveness?"),
], 3)

# ================================================================== 4. Comparing plays
SET(M_DRAMA, T_CMP, "Comparing plays: points, grids and joining words", "lil2-comparing-plays", [
    K("Which is the best order for a comparison essay?", "Point by point, with both plays discussed in each paragraph", [
        ("All of one play, then all of the other", "That leaves the comparing to the examiner."),
        ("Only the similarities", "Differences are needed too."),
        ("Only the differences", "Similarities are needed too.")],
      "Compare inside each paragraph.", "Comparison method", "Recall", "Where should the comparing happen?"),
    K("Which word signals a contrast?", "whereas", [
        ("similarly", "It signals similarity."),
        ("likewise", "It signals similarity."),
        ("moreover", "It adds a point; it does not contrast.")],
      "Whereas, while, in contrast and however signal difference.", "Joining words", "Recall", "Which word means 'on the other hand'?"),
    K("Which is a good point of comparison for two plays?", "How each ends and what hope or defeat it leaves", [
        ("The colour of the cover", "A cover is not part of the play."),
        ("The price of the book", "Price is not literary."),
        ("The number of pages", "Length is a weak point.")],
      "Endings, themes, conflict, setting, stagecraft and attitude are productive points.", "Choosing points", "Concept", "Which choice concerns meaning?"),
    K("Which sentence compares properly?", "Whereas Willy's dream is false and private, Walter's grows into a dream the family shares.", [
        ("Willy dreams. Walter dreams.", "It lists but does not compare."),
        ("Both plays are interesting.", "It says nothing about the texts."),
        ("Willy has a son called Biff.", "It describes one play only.")],
      "A comparison names both plays and uses a joining word with a judgment.", "A comparison sentence", "Application", "Which has a joining word and both characters?"),
    K("A question demands examples from three texts. A candidate uses two. According to the Board's report on essay demands, this", "leaves part of the question unanswered", [
        ("earns extra credit for depth", "It is treated as a weakness."),
        ("is acceptable if the two texts are long", "Length does not change the demand."),
        ("is penalised only in poetry", "The demand applies to any such question.")],
      "Using fewer texts than demanded leaves the question partly answered.", "Number of texts", "Interpretation", "Count the texts asked for."),
    K("Both A Raisin in the Sun and Death of a Salesman centre on money from insurance. Which statement is accurate?", "In Raisin the cheque follows a death and gives the family a chance; in Salesman Willy's insurance is part of his thinking about his own death", [
        ("Neither play involves insurance", "Both involve insurance."),
        ("Only Raisin involves a death", "Salesman also involves a death."),
        ("Insurance plays no role in either", "It is central in both.")],
      "Both plays link money from insurance to a dream, in very different ways.", "Similarity of theme", "Concept", "How does money appear in each?"),
    K("In a grid comparing two plays, each row should be", "one point of comparison such as dream, ending or stage", [
        ("one page of the book", "Page numbers are not points of comparison."),
        ("one actor's name", "Actors are not the point."),
        ("one character's whole life story", "A row is a point, not a summary.")],
      "Rows are points; columns are plays.", "Comparison grid", "Concept", "What does a row represent?"),
    K("Which conclusion shows balanced judgment?", "Both writers admire people who refuse to be pushed around, but they place the struggle in different settings.", [
        ("Both plays are the same.", "It ignores differences."),
        ("One play is better because it is longer.", "Length is not a literary judgment."),
        ("There is nothing to compare.", "It gives up the task.")],
      "A conclusion states a similarity and a difference.", "Conclusion", "Reasoning", "Which sentence has both?"),
], 4)

# ================================================================== 5. Reading the novel
SET(M_PROSE, T_NOV, "Reading the novel: background, setting, description and coincidence", "lil2-reading-the-novel", [
    K("Hard Times first appeared in", "1854, in weekly instalments in a magazine", [
        ("1949, as a single volume", "1949 is the publication date of Nineteen Eighty-Four."),
        ("1960, to mark independence", "That is the date of A Dance of the Forests."),
        ("1600, as a play", "Hard Times is a Victorian novel, not an early play.")],
      "Dickens published Hard Times in 1854 in instalments.", "Background", "Recall", "Think of the Victorian novel in parts."),
    K("Which type of setting does the Board's report assign to Mrs Sparsit's staircase in Hard Times?", "Psychological setting", [
        ("Physical setting only", "The report presents it as a mental picture rooted in her spite."),
        ("Social setting", "It reflects a person's mind more than a social group."),
        ("Historical setting", "It is not an era.")],
      "The report calls it a psychological setting in Mrs Sparsit's cynical mind.", "Kinds of setting", "Recall", "Is it a place in the story or in her thoughts?"),
    K("A descriptive detail is best defined as", "a vivid piece of description that appeals to the senses and does work in the story", [
        ("an event in the plot", "An event is plot, not description."),
        ("the writer's name", "It is a technique, not a name."),
        ("a summary of a chapter", "A summary is not a detail.")],
      "Descriptive details are exact, sensory pieces of description that show theme, character or mood.", "Descriptive detail", "Concept", "Is it an event or a piece of description?"),
    K("The smell of boiled cabbage in the hallway of Victory Mansions mainly suggests", "poverty and decay under the Party", [
        ("wealth and comfort", "The detail suggests the opposite."),
        ("a festival", "Nothing suggests a festival."),
        ("a friendly neighbourhood", "The setting is gloomy.")],
      "The detail builds a picture of shabbiness and deprivation.", "Descriptive detail", "Interpretation", "What does a bad smell in a hallway suggest?"),
    K("Coincidence in a novel is", "events that seem like chance but serve the plot", [
        ("an error by the writer", "It is a deliberate device."),
        ("a long description", "That is description."),
        ("the end of the book", "It can occur anywhere.")],
      "The Board's report describes coincidence as incidents that seem naturally planned.", "Coincidence", "Recall", "Does it look like chance or like planning?"),
    K("The Board's report says many candidates identified coincidences in Hard Times but did not", "show how the coincidences develop the plot", [
        ("name the author", "The complaint was about development of plot."),
        ("write in the past tense", "Tense is not the point."),
        ("mention the weather", "Weather is not the point.")],
      "The question was about coincidence and plot development.", "Coincidence and plot", "Interpretation", "What was the thrust of the question?"),
    K("The Old Hell Shaft in Hard Times is expected, in the report, to be discussed as", "a symbol of the dangers left by industrial life, as well as a physical place", [
        ("a harmless pond", "It is a danger."),
        ("a home for the Gradgrinds", "It is a mine shaft."),
        ("a classroom", "It is not a school.")],
      "The report says candidates did not discuss its symbolic meaning.", "Symbolic setting", "Concept", "Is it safe or dangerous?"),
    K("In a question asking for three settings in a novel, which answer earns most credit?", "Naming each setting and saying what it adds to plot, character or theme", [
        ("Listing ten places with no comment", "The report says naming without literary use is sketchy."),
        ("Retelling the whole novel", "Retelling is not what was asked."),
        ("Giving the writer's life story", "Biography is not relevant here.")],
      "Candidates were expected to show the literariness of the settings.", "Setting and its use", "Reasoning", "What must follow the name of a setting?"),
], 5)

# ================================================================== 6. Narrative voice and structure
SET(M_PROSE, T_NVO, "Narrative voice and structure in the two novels", "lil2-narrative-voice-structure", [
    K("A narrator who follows one character closely and tells only what that person knows is", "third person limited", [
        ("first person", "First person says 'I'."),
        ("omniscient", "Omniscient narrators know everything."),
        ("a chorus", "A chorus is a group in a play.")],
      "Third person limited stays with one character's view.", "Point of view", "Recall", "He says 'he' but knows only one mind."),
    K("The narration in Nineteen Eighty-Four stays close to", "Winston Smith", [
        ("O'Brien", "We learn about O'Brien through Winston."),
        ("Big Brother", "Big Brother is a symbol, not the viewpoint."),
        ("Julia", "Winston is the viewpoint character.")],
      "The narrator follows Winston's thoughts and fears.", "Limited point of view", "Recall", "Whose diary starts the story?"),
    K("The narrator of Hard Times is best described as", "omniscient and commenting, using irony", [
        ("first person, a child", "The narration is third person."),
        ("limited to one character", "The narrator moves between characters and comments."),
        ("silent, with no opinions", "The narrator is openly critical.")],
      "Dickens's narrator comments and uses irony.", "Narrator of Hard Times", "Concept", "Does the narrator share opinions?"),
    K("The three books of Hard Times are called", "Sowing, Reaping and Garnering", [
        ("Hope, Fear and Peace", "These are not the titles."),
        ("Coketown, London and Paris", "They are not place names."),
        ("Facts, Fancy and Feeling", "They are not the titles.")],
      "The farming terms suggest a cycle of cause and consequence.", "Structure", "Recall", "Think of a farming year."),
    K("The farming titles of the books of Hard Times suggest that", "what is planted early bears fruit later", [
        ("the novel is about agriculture", "The setting is an industrial town."),
        ("the story has no order", "The titles show a clear order."),
        ("the characters are farmers", "The characters are mill people, teachers and circus people.")],
      "Sowing, reaping and garnering show cause and effect.", "Structure and theme", "Interpretation", "What does a plant do after sowing?"),
    K("Why does limited point of view help Orwell's novel?", "It builds suspense and sympathy because we know only what Winston knows", [
        ("It tells us everything the Party plans", "That would be omniscient narration."),
        ("It removes all emotion", "Limited narration gives close access to emotion."),
        ("It shortens the novel", "Length is not the point.")],
      "We share Winston's fear and discovery, so his defeat is more painful.", "Effect of narration", "Reasoning", "What do we not know that Winston does not know?"),
    K("Which sentence is in the third person omniscient?", "Ama thought the bus would never come, while in the next street a man mended his net, unaware she was near.", [
        ("I thought the bus would never come.", "It is first person."),
        ("Ama thought the bus would never come, and her feet ached.", "It is limited to Ama."),
        ("You must wait for the bus.", "It is second person.")],
      "The narrator moves beyond Ama to another person's situation.", "Identify narration", "Application", "Which sentence goes beyond one mind?"),
    K("Which statement about structure is best?", "The three-part structure of each novel moves from a beginning through deepening trouble to a consequence", [
        ("Structure means the chapter numbers only", "Structure is the shape of the story."),
        ("Structure is the font of the book", "Typography is not structure."),
        ("A novel has no structure", "Novels are built in parts.")],
      "Structure is the shaping of events into parts with a purpose.", "Structure", "Concept", "What does the shape of the story do?"),
], 6)

# ================================================================== 7. Character and theme
SET(M_PROSE, T_CTN, "Characters and themes in Hard Times and Nineteen Eighty-Four", "lil2-character-theme-novels", [
    K("In Hard Times, who believes that facts alone should be taught to children?", "Thomas Gradgrind", [
        ("Sissy Jupe", "Sissy comes from the circus and stands for imagination."),
        ("Mr Sleary", "Sleary is the circus master."),
        ("Stephen Blackpool", "Stephen is a mill worker.")],
      "Gradgrind runs a school based on facts.", "Gradgrind", "Recall", "Who owns the school?"),
    K("Sissy Jupe in Hard Times mainly represents", "warmth, loyalty and imagination", [
        ("pride in being self-made", "That is Bounderby."),
        ("jealousy and spite", "That is Mrs Sparsit."),
        ("selfishness", "That is Tom.")],
      "Sissy contrasts with the facts-only system.", "Sissy", "Concept", "Which character comes from the circus?"),
    K("Which pair matches character and role in Nineteen Eighty-Four?", "O'Brien: a member of the Inner Party who turns out to be an agent of the system", [
        ("Julia: the head of the Party", "Julia is a young woman who rebels in her own way."),
        ("Mr Parsons: Winston's secret ally", "Parsons is a loyal and unthinking Party neighbour."),
        ("Big Brother: Winston's neighbour", "Big Brother is the figure on the posters.")],
      "Winston thinks O'Brien is a friend, but O'Brien is part of the Party's power.", "Characters", "Recall", "Which character first seems a friend?"),
    K("Newspeak is", "the Party's language designed to narrow thought", [
        ("a secret code of the rebels", "It is the state's language."),
        ("Winston's diary", "The diary is private writing."),
        ("a poster slogan only", "It is a language, not only a slogan.")],
      "Newspeak reduces the range of words so that thoughts become harder to think.", "Theme of language", "Recall", "Who invented it and why?"),
    K("Which theme best matches Stephen Blackpool's part in Hard Times?", "The harsh treatment of workers", [
        ("The joys of a circus", "That is Sissy and Sleary."),
        ("Pride in a self-made fortune", "That is Bounderby."),
        ("Fashionable society", "It is not Stephen's theme.")],
      "Stephen's life shows the conditions of mill workers.", "Theme and character", "Application", "Which character is a mill hand?"),
    K("Which sentence best links character to theme?", "Louisa, raised on facts alone and unable to say what she feels, shows that Dickens attacks a system without feeling.", [
        ("Louisa is a character in the book.", "It does not state a theme."),
        ("The book is long.", "It says nothing about character or theme."),
        ("Dickens lived in London.", "It gives biography only.")],
      "A link names a character, evidence, theme and effect.", "Linking", "Application", "Which sentence has all of these?"),
    K("The Board's report complains that candidates often", "mixed up characters and gave sketchy evidence", [
        ("wrote answers that were too well organised", "The complaint was the opposite."),
        ("named too many themes", "Not the complaint."),
        ("used too many linking words", "Linking words were encouraged.")],
      "The report says candidates confuse characters and give sketchy evidence.", "Report on candidates", "Interpretation", "What are the sketchy answers like?"),
    K("Winston's love for Julia can be read as a theme of", "private love set against total state control", [
        ("fashion", "Fashion is not a theme in the novel."),
        ("farming", "Farming is not the theme."),
        ("sport", "Sport is not the theme.")],
      "The love affair is the one private feeling the Party tries to destroy.", "Theme", "Concept", "What does the Party want to control?"),
], 7)

# ================================================================== 8. Writing about a novel
SET(M_PROSE, T_WNV, "Writing about a novel: question tags, plans and short notes", "lil2-writing-about-a-novel", [
    K("'To what extent' asks you to", "give a reasoned judgment on how far something is true", [
        ("retell the story", "Retelling is not a judgment."),
        ("answer yes or no only", "The tag needs reasons and evidence."),
        ("list characters", "A list does not answer the question.")],
      "Tags such as to what extent and how far ask for a degree of agreement with reasons.", "Question tags", "Recall", "Does it ask for a degree?"),
    K("A short-notes question asks you to choose three of five aspects. You should", "write on three, with several focused sentences each", [
        ("write on all five", "The report notes some candidates did this; it wastes time."),
        ("write on one at great length", "The number is three."),
        ("skip the question", "It is accessible.")],
      "Follow the number set by the question.", "Short notes", "Application", "How many were asked for?"),
    K("A strong body paragraph in a literature essay includes", "a topic sentence, several illustrations with their effect, and a closing sentence", [
        ("one detail only", "The report says one sketchy bit of evidence earns a skimpy mark."),
        ("only the writer's opinion", "Evidence is needed."),
        ("a long quotation with no comment", "Comment is needed.")],
      "The report asks for topic sentences, illustrations and concluding sentences.", "Paragraph structure", "Concept", "How many illustrations does the report want?"),
    K("The critical perspective in a literature answer means", "showing how a technique or detail develops other elements of the work", [
        ("criticising the writer harshly", "It means analysing effect, not blaming."),
        ("listing facts only", "Facts alone are descriptive."),
        ("writing about the weather", "The weather is irrelevant.")],
      "The report says answers score better when they show how elements are enhanced.", "Critical perspective", "Concept", "What comes after naming a device?"),
    K("Which is the best thesis sentence for 'Discuss the importance of setting in Nineteen Eighty-Four'?", "Setting is central because the shabby flats, the watching eyes and Room 101 develop plot, show character and carry the novel's warning.", [
        ("Nineteen Eighty-Four has many places.", "It does not answer how or why."),
        ("George Orwell wrote the book.", "It gives a fact, not a thesis."),
        ("The book is about a man.", "It does not address setting.")],
      "A thesis answers the question in one sentence.", "Thesis", "Application", "Which sentence answers the question?"),
    K("A candidate writes 'the novel shows control' with nothing more. What is missing?", "Specific evidence and an explanation of how it shows control", [
        ("A date", "A date is not required."),
        ("A longer title", "Titles are not the problem."),
        ("A drawing", "A drawing is not required.")],
      "Evidence and explanation are required.", "Evidence", "Reasoning", "What proves the claim?"),
    K("Which is an advised use of the first five minutes of an essay?", "Plan a thesis, points and evidence", [
        ("Copy the question twice", "That does not help the answer."),
        ("Write the conclusion first without a plan", "A plan comes before drafting."),
        ("Draw the cover of the book", "Drawing is not planning.")],
      "The report says a plan helps to structure the answer and saves time.", "Planning", "Application", "What does the plan contain?"),
    K("In a question 'Justify the claim that Bounderby is a satirical figure', 'justify' means", "defend the claim with evidence", [
        ("deny the claim", "It asks you to support it."),
        ("ignore the claim", "You must address it."),
        ("make a joke", "Satire is a technique, not a request to joke.")],
      "Justify means defend with evidence.", "Command word", "Concept", "Is it asking for support or rejection?"),
], 8)

# ================================================================== 9-11. Exam lesson sets
SET(M_EXAM, "Paper 1", "Paper 1: structure and multiple-choice method", "lil2-paper-1-strategy", [
    K("How many questions are on general literary appreciation in the Board's 2023 description of Paper 1?", "10", [
        ("5", "Five is not the number the report gives."), ("25", "Twenty-five would be half the paper."), ("40", "Forty are on the set texts.")],
      "Ten general questions and forty on the set texts, four per text.", "Paper 1 structure", "Recall", "There are 50 in all."),
    K("How many questions on each set text does the report say Paper 1 contains?", "Four", [
        ("One", "There are four per text."), ("Ten", "Ten is the number of general questions."), ("Fifty", "Fifty is the total in the paper.")],
      "Forty text questions across ten texts gives four per text.", "Paper 1 structure", "Recall", "Divide forty by the ten texts."),
    K("Which is a general literary notion the report says was tested?", "Tone", [
        ("The date of the Globe fire", "That is not listed."), ("The cost of a ticket", "Not a literary notion."), ("The author's address", "Not a literary notion.")],
      "The report lists tone, metrical patterns, realism and oral prose forms among others.", "General appreciation", "Recall", "Look at the list the report gives."),
    K("A stem asks what a symbol stands for. The best first step is to", "read the stem and predict the answer before reading the options", [
        ("pick the longest option", "Length is not a clue."), ("pick option C", "No letter is favoured."), ("skip all stems", "The stem asks the question.")],
      "Predicting protects you from tempting options.", "Method", "Application", "Think before looking."),
    K("Four options are given. Two are clearly wrong. What next?", "Compare the remaining two against the stem and choose the one that answers it exactly", [
        ("Choose at random without reading", "Compare them first."), ("Choose the first option", "Order does not decide."), ("Leave the question blank without reading", "Elimination makes a good answer more likely.")],
      "Elimination narrows the choice.", "Elimination", "Application", "What do you do after eliminating?"),
    K("Which is a text-based area the report says Paper 1 tests?", "Setting", [
        ("The publisher's profit", "Not an area listed."), ("The weight of the book", "Not an area listed."), ("The cover design", "Not an area listed.")],
      "Background, setting, plot, structure, style, themes, characterisation, stagecraft and mood are listed.", "Text-based areas", "Recall", "Which choice is a literary feature?"),
    K("Why is revising only the plot of a text risky?", "Paper 1 also tests style, structure, mood, stagecraft and background", [
        ("Paper 1 never asks about the plot", "Plot is included."), ("Plot is not in the book", "Plot is the story."), ("Teachers forbid it", "That is not the reason.")],
      "The report lists many areas besides plot.", "Revision", "Reasoning", "Read the list of areas."),
    K("A one-page revision sheet for a text should contain", "setting and background, characters, key events, themes and techniques", [
        ("only the author's address", "Not useful."), ("only quotations", "Quotations alone are not enough."), ("nothing: just reread the text", "A sheet helps recall under time pressure.")],
      "A compact sheet covers the areas that questions come from.", "Revision plan", "Application", "What do four questions per text come from?"),
], 9)

SET(M_EXAM, "Paper 2", "Paper 2: choosing, planning and answering", "lil2-paper-2-strategy", [
    K("According to the Board's 2023 report, how many questions do candidates answer in Paper 2?", "Four", [
        ("Two", "Two is too few."), ("Three", "Three is the number of sections."), ("Sixteen", "Sixteen is the number set.")],
      "They answer four of the sixteen.", "Paper 2 structure", "Recall", "One from each section plus another."),
    K("In the report's rule, the fourth question must be", "from any section but on a different text", [
        ("from the same text as another answer", "It must be a different text."), ("a repeat of the first", "It must be a different question."), ("from Section C only", "Any section is allowed.")],
      "One from each section, then a fourth from any section but a different text.", "Choosing", "Recall", "Look at the rule in the lesson."),
    K("Which sections does the report name in Paper 2?", "Drama, prose and poetry", [
        ("Grammar, spelling and handwriting", "These are not the sections."), ("Reading, writing and speaking", "These are not the sections."), ("Past, present and future", "These are not the sections.")],
      "Sections A, B and C: drama, prose, poetry.", "Paper 2 sections", "Recall", "Think of the three genres."),
    K("A question on the symbolic use of settings is answered with a general essay on symbolism. According to the report, this", "ignores the terms of the question", [
        ("is the ideal answer", "The focus was settings."), ("earns full marks", "It does not address settings."), ("is a better answer than one on settings", "It misses the focus.")],
      "The report describes this fault in a Death of a Salesman answer.", "Question focus", "Reasoning", "What was the question about?"),
    K("Which routine is best for each essay?", "Read, underline the tag and focus, plan, write, check", [
        ("Write at once, plan later", "Planning comes first."), ("Plan after writing the conclusion", "A plan comes before drafting."), ("Skip the introduction", "A focused introduction is advised.")],
      "A short plan saves time and gives structure.", "Routine", "Application", "What comes before writing?"),
    K("A candidate retells the plot in answer to 'Comment on the effect of suspense in a play'. The likely result is", "a low mark because the effect of suspense is not discussed", [
        ("a high mark for completeness", "The report says narration scored low."), ("full marks for length", "Length is not the criterion."), ("a bonus for a good memory", "There is no such bonus.")],
      "The report describes candidates narrating the plot and scoring low.", "Avoiding narration", "Interpretation", "What did the question ask for?"),
    K("Which paragraph is strongest?", "A topic sentence, three focused illustrations each explained, and a concluding sentence", [
        ("A single sentence of opinion", "It lacks evidence."), ("A long quotation with no comment", "Comment is needed."), ("A list of names", "A list has no argument.")],
      "The report wants full and focused illustrations.", "Paragraph quality", "Concept", "How many illustrations?"),
    K("What should a candidate do if an essay question concerns something she cannot support with three or four pieces of evidence?", "Choose another question she can support", [
        ("Write anyway and hope", "A weak answer scores low."), ("Invent facts", "Invented facts are marked wrong."), ("Leave all questions blank", "She should choose one she can answer.")],
      "Choosing well is part of exam technique.", "Choosing", "Reasoning", "What can you prove?"),
], 10)

SET(M_EXAM, "Paper 3", "Paper 3: context, unseen prose and poetry", "lil2-paper-3-strategy", [
    K("How are the questions of Paper 3 described in the Board's 2023 report?", "Four compulsory questions with sub-tasks a to e", [
        ("Ten optional questions", "They are compulsory and four in number."), ("Two essays of 40 lines", "They are structural, not essays."), ("Fifty multiple-choice items", "That is Paper 1.")],
      "Four compulsory questions of sub-tasks a to e.", "Paper 3 structure", "Recall", "Count the questions."),
    K("In a meaning-in-context task, the best answer is", "a word or phrase that can replace the original in the sentence, in your own words", [
        ("the original word copied out", "The report says recopying is a common fault."), ("a long sentence of explanation", "A replacement phrase is needed."), ("an unrelated word", "It must fit the sentence.")],
      "The replacement should fit the context.", "Meaning in context", "Application", "Can your word replace the original?"),
    K("'Cite two phrases of not more than two words each.' Which answer follows the instruction?", "\"cruel laughter\" and \"empty street\" in quotation marks", [
        ("A whole sentence from the passage", "It is too long."), ("Your own summary", "Citing needs exact words."), ("Two paragraphs", "It is far too long.")],
      "Cite means exact words in quotation marks, within the limit.", "Citing", "Application", "Count the words."),
    K("How should stage directions be written in an answer?", "In brackets, followed by a comment on what they show", [
        ("In capital letters only", "Brackets are the convention."), ("Without any comment", "Comment earns the marks."), ("As part of the dialogue", "They are not spoken.")],
      "The report expects brackets and a comment on use and significance.", "Stage directions", "Recall", "How do playwrights mark them?"),
    K("A question asks for the 'most significant stage prop' in a killing scene. The best answer is", "one prop, the one most important to the action", [
        ("a list of every prop in the play", "The question asks for the most significant one."), ("no prop at all", "A prop is expected."), ("the name of the playwright", "Not a prop.")],
      "The report notes candidates lost marks by listing other props.", "Stagecraft", "Application", "Is it one or many?"),
    K("A creative task asks for a report of one paragraph. What must the answer have?", "A caption and a single paragraph", [
        ("Six lines of verse", "That is a poem."), ("Three pages", "It must be one paragraph."), ("No caption", "A caption is expected.")],
      "The report says candidates lost marks for ignoring the caption and paragraph limits.", "Creative form", "Application", "What does a report need?"),
    K("A modern-English task requires", "direct speech, grammatical accuracy and no change of person or voice", [
        ("reported speech with the person changed", "The report says direct speech only."), ("a copy of the original line", "The task is to render it in modern English."), ("an essay", "It is a short rendering.")],
      "The report lists the rubric: direct speech only, accuracy, no switching of person or voice.", "Modern English prose", "Concept", "Direct or reported speech?"),
    K("A poetry question asks you to find the rhyme scheme. You label a four-line stanza whose lines end in sounds A, B, A, B. The scheme is", "ABAB", [
        ("AABB", "That would mean lines 1 and 2 rhyme."), ("ABBA", "That would mean lines 1 and 4 rhyme."), ("AAAA", "That would mean all four rhyme.")],
      "Alternate rhyme is ABAB.", "Rhyme scheme", "Application", "Which lines end alike?"),
], 11)

# ================================================================== Paper 1 mock exam A (50 questions, four Lower Sixth modules)
P1 = [
    # ---- Aristotle's Poetics and tragedy (3)
    K("In Aristotle's Poetics, the word hamartia is usually explained as", "a mistake or error of judgment that begins the hero's fall", [
        ("a reversal of fortune", "That is peripeteia."), ("a change from ignorance to knowledge", "That is anagnorisis."), ("the cleansing effect on the audience", "That is catharsis.")],
      "Hamartia is the error that starts the fall.", T_ARI, "Recall", "Match each Greek term to its meaning."),
    K("Aristotle says tragedy arouses pity and fear so as to bring about", "catharsis", [
        ("peripeteia", "That is a reversal in the plot."), ("hamartia", "That is the hero's error."), ("anagnorisis", "That is recognition.")],
      "Catharsis is the effect of pity and fear on the audience.", T_ARI, "Recall", "Which word names the effect on the audience?"),
    K("In the Poetics, which element does Aristotle place first in importance in tragedy?", "Plot", [
        ("Spectacle", "He ranks spectacle low."), ("Song", "Song is not first."), ("Costume", "Costume is not one of his main elements.")],
      "He calls the plot the soul of tragedy and says tragedy imitates action.", T_ARI, "Concept", "Which element is the chain of events?"),
    # ---- Prosody and scansion (4)
    K("An iambic pentameter line has", "five iambs, ten syllables in all", [
        ("four trochees, eight syllables", "That is trochaic tetrameter."), ("three anapests, nine syllables", "That is anapestic trimeter."), ("six dactyls, eighteen syllables", "That is dactylic hexameter.")],
      "Iamb = unstressed then stressed; five feet gives ten syllables.", T_PRO, "Recall", "Penta means five."),
    K("A foot with the pattern stressed, unstressed is a", "trochee", [
        ("iamb", "An iamb is unstressed then stressed."), ("anapest", "An anapest has two unstressed then one stressed."), ("spondee", "A spondee is two stressed syllables; it is a possible but different foot.")],
      "Trochee: / u.", T_PRO, "Recall", "Reverse the iamb."),
    K("A poem of fourteen lines on a single theme is usually a", "sonnet", [
        ("ballad", "A ballad is a story song in quatrains."), ("elegy", "An elegy mourns."), ("limerick", "A limerick has five lines.")],
      "The sonnet has fourteen lines.", T_PRO, "Recall", "Count the lines."),
    K("The rhyme scheme of the stanza 'day / one / gay / sun' (end words in order) is", "ABAB", [
        ("AABB", "The first two lines do not rhyme."), ("ABBA", "The first and fourth lines do not rhyme."), ("ABCD", "Lines one and three rhyme.")],
      "Day rhymes with gay and one rhymes with sun.", T_PRO, "Application", "Which lines rhyme?"),
    # ---- Narrative theory (3)
    K("In narrative theory, plot differs from story because plot", "arranges events with links of cause and effect", [
        ("is shorter than story", "Length is not the difference."), ("contains no characters", "A plot includes characters."), ("is always told in the first person", "Plot can be told in any person.")],
      "Story is events in time order; plot is their arrangement with causes.", T_NAR, "Concept", "What does a writer do to events?"),
    K("Freytag's pyramid names the turning point of a story as the", "climax", [
        ("exposition", "That is the opening."), ("denouement", "That is the tying up of loose ends."), ("rising action", "That builds towards the turning point.")],
      "The climax is the high point and turning point.", T_NAR, "Recall", "Where is the peak of the pyramid?"),
    K("A narrator who uses 'I' and tells his own experience is", "a first-person narrator", [
        ("an omniscient narrator", "Omniscient narrators know everything in the third person."), ("a limited third-person narrator", "That is third person."), ("a chorus", "A chorus belongs to drama.")],
      "First person uses I.", T_NAR, "Recall", "Which word does the narrator use?"),
    # ---- Critical approaches (3)
    K("A critic who focuses on class and economic power in a text is using a", "Marxist approach", [
        ("formalist approach", "Formalists study form and language."), ("psychoanalytic approach", "That studies the mind and the unconscious."), ("feminist approach", "That studies gender.")],
      "Marxist criticism studies class, wealth and power.", T_CRI, "Concept", "Which approach follows class?"),
    K("A critic who studies the relation between a text and colonial rule and its aftermath uses a", "post-colonial approach", [
        ("formalist approach", "That studies form."), ("psychoanalytic approach", "That studies the unconscious."), ("Marxist approach only", "It centres on class, not empire.")],
      "Post-colonial criticism examines empire, identity and resistance.", T_CRI, "Concept", "Which approach looks at empire?"),
    K("A critic who studies the unconscious desires and fears of characters is using a", "psychoanalytic approach", [
        ("feminist approach", "That studies gender."), ("formalist approach", "That studies form."), ("post-colonial approach", "That studies empire.")],
      "Psychoanalytic criticism draws on ideas about the mind.", T_CRI, "Concept", "What is hidden in the mind?"),
    # ---- Reading Shakespeare's plays (3)
    K("A soliloquy is", "a speech in which a character, alone or as if alone, speaks thoughts aloud to the audience", [
        ("a short remark that others on stage cannot hear", "That is an aside."), ("a group of speakers who comment on the action", "That is a chorus."), ("a direction to exit", "That is a stage direction.")],
      "Soliloquy: a character's thoughts spoken aloud.", T_READ, "Recall", "Think of Hamlet alone on stage."),
    K("Shakespeare's plays are mostly written in", "blank verse, which is unrhymed iambic pentameter", [
        ("rhymed couplets only", "Couplets appear but are not the main form."), ("prose only", "Verse is the main form with some prose."), ("free verse", "Free verse is modern.")],
      "Blank verse is his usual line.", T_READ, "Recall", "Ten syllables, no rhyme."),
    K("The Globe theatre in London, associated with Shakespeare's company, opened in", "1599", [
        ("1066", "That is the date of the Norman conquest."), ("1800", "Too late."), ("1949", "That is a twentieth-century date.")],
      "The company built the Globe in 1599.", T_READ, "Recall", "Late sixteenth century."),
    # ---- Tragedy in Shakespeare (3)
    K("In Coriolanus, the Board's report says the title character is killed by", "Tullus Aufidius", [
        ("Brutus", "Brutus is a tribune who opposes him."), ("Menenius", "Menenius is his friend."), ("Volumnia", "She is his mother.")],
      "The report's description of the extract names Aufidius.", T_TRA, "Recall", "Who is his enemy?"),
    K("In Hamlet, the play within the play is used by Hamlet to", "test the guilt of the king", [
        ("entertain the court only", "The play has a purpose."), ("arrange a marriage", "It is not about marriage."), ("announce a war", "It is not about war.")],
      "Hamlet stages a play to watch the king's reaction.", T_TRA, "Concept", "What does Hamlet want to learn?"),
    K("A tragic loss in a play is felt when", "a person of great ability or goodness is destroyed, so the audience feels waste as well as pity", [
        ("a villain is punished", "That is justice, not tragic loss."), ("a comedy ends in marriage", "That is comedy."), ("the actors forget their lines", "That is a production error.")],
      "Tragic loss emphasises the hero's good qualities as well as the death.", T_TRA, "Concept", "Is it about waste of great qualities?"),
    # ---- Comedy and history in Shakespeare (3)
    K("A Shakespearean comedy usually ends with", "reconciliation and marriages", [
        ("the hero's death", "That is tragedy."), ("a battle", "That belongs to history plays and tragedies."), ("a long silence", "It is not a convention.")],
      "Comedy moves from confusion to a happy ending.", T_COM, "Recall", "Think of how comedies end."),
    K("Shakespeare's English history plays drew mainly on", "chronicles by historians such as Holinshed", [
        ("modern newspapers", "They did not exist."), ("scientific journals", "They are not sources."), ("films", "Films did not exist.")],
      "He used chronicles and altered events to make better plays.", T_COM, "Recall", "Which written sources did he use?"),
    K("A history play differs from a tragedy because it", "dramatises events from a nation's past, drawn from a chronicle", [
        ("has no characters", "It has many."), ("is always funny", "It is not defined by humour."), ("is performed only in churches", "It was performed in public theatres.")],
      "History plays dramatise English history.", T_COM, "Concept", "What does the word history suggest?"),
    # ---- Writing about a Shakespeare play (3)
    K("A context question asks you to put lines into modern English prose. The Board's report says to use", "direct speech, with the same person and correct grammar", [
        ("reported speech", "The report says direct speech only."), ("a copy of the original lines", "The task is a rendering in modern English."), ("a poem", "Prose is required.")],
      "The report states the rubric.", T_WSH, "Recall", "Direct or reported speech?"),
    K("A stagecraft question asks for the most significant prop in a killing scene. The report notes most candidates named", "the sword (or dagger)", [
        ("a chair", "It is not the most significant prop."), ("a mask", "It is not the answer in the report."), ("a flag", "It is not the answer in the report.")],
      "More than 90 per cent identified the sword or its synonym.", T_WSH, "Recall", "What is used to kill?"),
    K("Which is the best paragraph in an essay on a Shakespeare play?", "A topic sentence, several focused illustrations with their effect, and a closing sentence", [
        ("A single quotation with no comment", "It lacks explanation."), ("A plot summary", "Narration scores low."), ("A list of characters", "A list has no argument.")],
      "The report advises full and focused illustrations.", T_WSH, "Concept", "How many illustrations?"),
    # ---- Modern drama and stagecraft (3)
    K("Stage directions in a printed play are normally shown", "in brackets or italics", [
        ("in the title", "They are inside the play."), ("only in the foreword", "They are inside the scene."), ("as footnotes", "They are not footnotes.")],
      "Brackets and italics separate them from speech.", T_MOD, "Recall", "How do you tell action from speech?"),
    K("A producer says a scene is easy to stage because it needs only simple props and everyday clothes. This is a point about", "production facilities", [
        ("audience appeal", "That concerns interest."), ("a production difficulty", "It describes ease."), ("theme", "It is not an idea.")],
      "Simple, cheap items are facilities.", T_MOD, "Application", "Is it easy or hard?"),
    K("The set of Death of a Salesman lets Willy move between present and past because", "the walls are treated as if they were not there, with lighting and music marking the change", [
        ("the play is told by a narrator", "Staging shows the past."), ("there is no set", "There is a house on stage."), ("the actors speak to the audience in each scene", "The device is the staging of memory.")],
      "Light, music and a set without solid walls show Willy's mind.", T_MOD, "Concept", "How is memory staged?"),
    # ---- Characterization in modern drama (3)
    K("A foil is a character who", "contrasts with another so that both are clearer", [
        ("tells the story", "That is a narrator."), ("always wins", "A foil does not always win."), ("never speaks", "A foil speaks.")],
      "A foil is a contrast.", T_CHD, "Recall", "Think of a character set against another."),
    K("In A Raisin in the Sun, Beneatha's wish to become a doctor is best read as", "a form of ambition and protest, not a surrender to white values", [
        ("a wish to please white employers", "The report says candidates wrongly read it as giving in."), ("a joke in the play", "It is a serious ambition."), ("a sign she wants to leave her family", "It is not that.")],
      "The report says candidates confused her ambition with accepting white values.", T_CHD, "Interpretation", "What does the ambition challenge?"),
    K("The Board's report says a full answer on Willy Loman's failure needs", "a critical perspective that includes other characters and outside forces", [
        ("only his illusions", "That is the one-sided answer."), ("only the date of the play", "Dates do not answer the question."), ("only the ending", "The ending alone is not enough.")],
      "The report asks for the contributions of others and external forces.", T_CHD, "Interpretation", "Is Willy alone to blame?"),
    # ---- African drama and social themes (3)
    K("Oral tradition in African drama appears as", "song, dance, proverb and ritual", [
        ("only printed footnotes", "Footnotes are written."), ("only silent reading", "Oral means spoken."), ("only stage lighting", "Lighting is a stage element, not oral tradition.")],
      "Song, dance, proverb and ritual are oral forms.", T_AFR, "Recall", "Which are spoken or performed?"),
    K("Which social ill does the Board's report link to the extract of A Dance of the Forests that mentions the seventy?", "Bribery and corruption", [
        ("Drought", "Not named."), ("Illiteracy", "Not named."), ("War", "Not named.")],
      "The report says bribery and corruption.", T_AFR, "Recall", "What allowed an unsafe journey?"),
    K("According to the report, Butake's attitude to the women in And Palm-Wine Will Flow is", "admiring and sympathetic", [
        ("contemptuous", "The report says otherwise."), ("indifferent", "The report expects an attitude."), ("hostile", "The report says otherwise.")],
      "He admires their courage and resilience.", T_AFR, "Interpretation", "Whose side is the writer on?"),
    # ---- Comparing plays (3)
    K("The best way to organise a comparison essay is", "to discuss both plays together in each paragraph", [
        ("to write about one play and then the other", "That leaves the comparing to the examiner."), ("to write only similarities", "Differences are needed too."), ("to write only a plot summary", "A summary is not a comparison.")],
      "Compare inside the paragraph.", T_CMP, "Concept", "Where does the comparing happen?"),
    K("Which word introduces a contrast?", "whereas", [
        ("likewise", "Similarity."), ("similarly", "Similarity."), ("also", "Addition.")],
      "Whereas signals difference.", T_CMP, "Recall", "Which means on the other hand?"),
    K("A question demands examples from three texts. Using two", "leaves the question partly unanswered", [
        ("earns extra credit", "It is a weakness."), ("is always acceptable", "The count matters."), ("is only a problem in poetry", "It applies everywhere.")],
      "Count the texts demanded.", T_CMP, "Application", "How many were asked?"),
    # ---- Reading the 19th and 20th century novel (3)
    K("Hard Times was first published in", "1854, in weekly instalments", [
        ("1949", "That is Nineteen Eighty-Four."), ("1960", "That is A Dance of the Forests."), ("1600", "It is a Victorian novel.")],
      "Dickens published it in 1854.", T_NOV, "Recall", "Victorian era."),
    K("Mrs Sparsit's staircase in Hard Times is, according to the Board's report, an example of", "psychological setting", [
        ("physical setting only", "The report stresses the mind."), ("historical setting", "It is not an era."), ("a stage direction", "Hard Times is a novel.")],
      "It reflects her spite.", T_NOV, "Recall", "Is it a place in her mind?"),
    K("Coincidence in a novel is", "events that seem like chance but serve the plot", [
        ("a mistake by the writer", "It is deliberate."), ("a long description", "That is description."), ("the ending only", "It can be anywhere.")],
      "The Board's report defines it so.", T_NOV, "Concept", "Does it look like chance?"),
    # ---- Narrative voice and structure (3)
    K("The narrator of Nineteen Eighty-Four stays close to", "Winston Smith", [
        ("O'Brien", "We learn about him through Winston."), ("Big Brother", "Big Brother is a symbol."), ("Mr Charrington", "Winston is the viewpoint.")],
      "Third person limited on Winston.", T_NVO, "Recall", "Whose diary?"),
    K("The titles Sowing, Reaping and Garnering belong to", "the three books of Hard Times", [
        ("Nineteen Eighty-Four", "Its parts are numbered."), ("A Raisin in the Sun", "It is a play in acts."), ("Death of a Salesman", "It is a play in acts and a requiem.")],
      "The farming cycle suggests cause and effect.", T_NVO, "Recall", "Which novel by Dickens?"),
    K("A narrator who knows the thoughts of many characters and also comments on the story is", "omniscient", [
        ("first person", "First person says I."), ("limited", "Limited stays with one."), ("a chorus", "A chorus belongs to drama.")],
      "That is Dickens's narrator.", T_NVO, "Concept", "Does the narrator know everything?"),
    # ---- Character and theme in the prescribed novels (3)
    K("Who in Hard Times believes in facts alone?", "Thomas Gradgrind", [
        ("Sissy Jupe", "She stands for imagination."), ("Mr Sleary", "He is the circus master."), ("Stephen Blackpool", "He is a mill hand.")],
      "Gradgrind runs the school of facts.", T_CTN, "Recall", "Who owns the school?"),
    K("Newspeak in Nineteen Eighty-Four is", "the Party's language designed to narrow thought", [
        ("a code of rebels", "It is the state's."), ("Winston's diary", "That is his private writing."), ("a type of poster", "It is a language.")],
      "Newspeak limits words and thoughts.", T_CTN, "Recall", "Whose language?"),
    K("The theme of Room 101 in Nineteen Eighty-Four is best described as", "fear and betrayal under total control", [
        ("peaceful family life", "It is not peaceful."), ("a village festival", "It is not a festival."), ("harvest", "Not the theme.")],
      "In Room 101 Winston is broken.", T_CTN, "Interpretation", "What happens to Winston there?"),
    # ---- Writing about a novel (4)
    K("A question beginning 'To what extent' requires", "a reasoned judgment on how far something is true", [
        ("a retelling", "Retelling is not an answer."), ("a one-word reply", "Reasons are needed."), ("a list", "A list is not enough.")],
      "It asks for a degree of agreement.", T_WNV, "Concept", "How far?"),
    K("In a short-notes question that says 'choose three', you should", "write on three, each with focused sentences", [
        ("write on all of them", "It wastes time."), ("write on one", "The number is three."), ("skip it", "It is accessible.")],
      "Follow the number set.", T_WNV, "Application", "How many?"),
    K("One piece of evidence in a paragraph, according to the Board's report, earns", "a skimpy mark", [
        ("full marks", "More evidence earns more."), ("a bonus", "There is no bonus."), ("no mark in any case", "It earns a small mark.")],
      "More focused illustrations earn more.", T_WNV, "Interpretation", "What does the report say about single evidence?"),
    K("The critical perspective in a literature answer means", "showing how a device develops other elements", [
        ("criticising the writer harshly", "It is analysis."), ("giving the plot only", "That is narration."), ("listing characters", "A list is not analysis.")],
      "Show effect on plot, theme or character.", T_WNV, "Concept", "What comes after naming?"),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="lil2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 201)))

# ================================================================== Paper 2 practice paper A (25 auto-markable parts)
P2 = [
    # Question 1: Structure and choice (5)
    K("Question 1(a). How many questions does a candidate answer in Paper 2, according to the Board's 2023 report?", "Four", [
        ("Two", "Two is too few."), ("Three", "There are three sections but four answers."), ("Sixteen", "Sixteen is the number set.")],
      "Four of sixteen.", T_WSH, "Recall", "One from each section plus another."),
    K("Question 1(b). Which rule applies to the fourth question?", "It may be from any section but must be on a different text", [
        ("It must be from the same text as another answer", "It must be a different text."), ("It must be a repeat", "It must be a different question."), ("It must be poetry", "Any section is allowed.")],
      "The report states the rule.", T_WNV, "Recall", "Different text."),
    K("Question 1(c). A candidate sees a question she cannot support with three or four pieces of evidence. What should she do?", "Choose another question she can support", [
        ("Invent evidence", "Invented evidence is wrong."), ("Write in general terms", "That scores low."), ("Leave the paper", "She should choose another question.")],
      "Choice is part of technique.", T_WNV, "Reasoning", "What can you prove?"),
    K("Question 1(d). In 'Comment on the symbolic use of settings', the focus is", "the settings", [
        ("symbolism in general", "That is the faulty reading the report describes."), ("the writer's life", "Not the focus."), ("the cost of production", "Not the focus.")],
      "Underline the focus.", T_NOV, "Concept", "What is the topic?"),
    K("Question 1(e). Which command tag asks for a degree of agreement?", "To what extent", [
        ("Illustrate", "It asks for examples."), ("Short notes", "It asks for brief paragraphs."), ("Comment on", "It asks for effect.")],
      "To what extent means how far.", T_WNV, "Concept", "Which tag has a degree?"),
    # Question 2: Drama (5)
    K("Question 2(a). A question asks whether Willy Loman's problems come from his illusions. A good plan includes", "his illusions and the roles of others and outside forces", [
        ("only his illusions", "That is one-sided."), ("only other characters", "Willy's illusions also matter."), ("only the ending", "Not enough.")],
      "The report asks for the critical perspective.", T_CHD, "Application", "Is it one cause or several?"),
    K("Question 2(b). A question on the merits and demerits of And Palm-Wine Will Flow as a stage play requires attention to", "production facilities and production difficulties", [
        ("only audience appeal", "The report says this was the common error."), ("only the date of writing", "Not relevant."), ("only the title", "Not relevant.")],
      "Candidates were expected to cover facilities and hurdles.", T_MOD, "Application", "What does the report say candidates missed?"),
    K("Question 2(c). Which is a production difficulty named in the report for And Palm-Wine Will Flow?", "Showing women's ritual at twin streams or the loss of farmland", [
        ("Familiar costumes", "That is a facility."), ("A small cast", "That is a facility."), ("Daylight performance", "That is a facility.")],
      "The ritual and the farmland are hard to stage.", T_AFR, "Recall", "Which is hard to show?"),
    K("Question 2(d). 'Butake's attitude to the women is one of admiration.' This states", "the playwright's attitude", [
        ("a role", "A role says what they do."), ("a stage direction", "Not a direction."), ("a plot point", "Not a plot point.")],
      "Attitude is the writer's view.", T_CHD, "Concept", "Is it a view or a function?"),
    K("Question 2(e). Which is the strongest point for an essay on suspense in A Raisin in the Sun?", "A moment of waiting for the money, what it builds and its effect on plot", [
        ("A list of the characters' names", "A list is not a point."), ("The date of the play", "A date is not a point."), ("A retelling of the whole play", "Narration scores low.")],
      "The report says candidates narrated the plot instead of discussing suspense.", T_MOD, "Reasoning", "What does the question ask for?"),
    # Question 3: Prose (5)
    K("Question 3(a). In an essay on setting in Nineteen Eighty-Four, each setting should be", "named and linked to plot, character, theme or style", [
        ("only named", "The report says candidates stopped at naming."), ("only described in a sentence", "The use must be explained."), ("left out", "The question asks for them.")],
      "Show the literariness of each setting.", T_NOV, "Application", "What must follow the name?"),
    K("Question 3(b). A descriptive detail in Nineteen Eighty-Four could be", "the smell of boiled cabbage in the hallway of Victory Mansions", [
        ("the whole plot", "A plot is not a detail."), ("the writer's name", "A name is not a detail."), ("the date of publication", "A date is not a detail.")],
      "The report names the hallway as a descriptive detail.", T_NOV, "Recall", "Which is a sensory detail?"),
    K("Question 3(c). The Board's report says candidates identified coincidences in Hard Times but did not", "show how they develop the plot", [
        ("name any", "They identified them."), ("write at all", "They wrote answers."), ("mention Dickens", "The weakness was in plot development.")],
      "The thrust was coincidence and plot development.", T_NOV, "Interpretation", "What was missing?"),
    K("Question 3(d). In short notes on the Old Hell Shaft, the report expects discussion of", "its symbolic significance as a leftover danger of the Industrial Revolution", [
        ("its price", "Not relevant."), ("its colour only", "Not enough."), ("the author's address", "Not relevant.")],
      "Candidates did not delve into the symbolic significance.", T_WNV, "Recall", "What does it stand for?"),
    K("Question 3(e). The best thesis for 'Discuss the importance of the setting in Hard Times' is", "Coketown, the shaft and the staircase show how industry harms people and develop plot and theme.", [
        ("Hard Times has a setting.", "It says nothing of importance."), ("Dickens was born in 1812.", "It is biography."), ("The novel is about a town.", "It gives no argument.")],
      "A thesis answers the question.", T_WNV, "Application", "Which sentence argues?"),
    # Question 4: Technique and expression (5)
    K("Question 4(a). A paragraph that has one sketchy illustration will, according to the report, earn", "a skimpy mark", [
        ("full marks", "More illustrations earn more."), ("a bonus", "There is no bonus."), ("no marks at all", "It earns a small mark.")],
      "The report stresses several focused illustrations.", T_WNV, "Recall", "How many illustrations?"),
    K("Question 4(b). A candidate names a device but does not say what it does. This lacks", "the critical perspective (effect)", [
        ("a title", "A title is not the issue."), ("a date", "A date is not the issue."), ("a drawing", "Not needed.")],
      "Say how it develops other elements.", T_WNV, "Reasoning", "What follows the name?"),
    K("Question 4(c). Which linking word signals contrast?", "however", [
        ("moreover", "Addition."), ("similarly", "Similarity."), ("in addition", "Addition.")],
      "However signals contrast.", T_CMP, "Recall", "Which means but?"),
    K("Question 4(d). When writing about a text, which tense is the convention?", "Present tense", [
        ("Past tense", "The convention is present."), ("Future tense", "Not used for events in the text."), ("A mixture", "Mixed tenses are an error.")],
      "Literary essays use the present tense.", T_WNV, "Recall", "Hemingway shows."),
    K("Question 4(e). Which is the best use of the first five minutes?", "Plan a thesis, points and evidence", [
        ("Copy the question twice", "That does not help."), ("Write the conclusion first", "Plan first."), ("Draw a picture", "Not useful.")],
      "A plan structures the answer.", T_WNV, "Application", "What does the plan hold?"),
    # Question 5: Comparing and timing (5)
    K("Question 5(a). In a comparison essay, the best structure is", "point by point with both texts in each paragraph", [
        ("all of text one, then all of text two", "That does not compare."), ("only similarities", "Differences are needed."), ("only differences", "Similarities are needed.")],
      "Compare within paragraphs.", T_CMP, "Concept", "Where does the comparing happen?"),
    K("Question 5(b). Which pair of points is a good basis for comparing two plays?", "ending and the playwright's attitude", [
        ("page count and font", "Not literary."), ("price and cover", "Not literary."), ("publisher and year of printing", "Not about meaning.")],
      "Endings and attitudes concern meaning.", T_CMP, "Application", "Which concern meaning?"),
    K("Question 5(c). A candidate runs out of time and leaves the fourth essay unfinished. The best lesson is to", "plan time so that all four essays are finished", [
        ("write longer introductions", "That uses more time."), ("skip planning", "Planning saves time."), ("write only one essay", "Four are required.")],
      "Keep to a steady pace.", T_WNV, "Reasoning", "What was the problem?"),
    K("Question 5(d). A question asks for illustrations from three texts. A candidate uses two. This", "leaves part of the question unanswered", [
        ("earns extra credit", "It does not."), ("is perfect", "It is incomplete."), ("is only a problem in poetry", "It applies throughout.")],
      "Count the texts.", T_CMP, "Application", "How many were asked?"),
    K("Question 5(e). Which concluding sentence shows balanced judgment?", "Both writers admire people who resist injustice, but they place the struggle in different settings.", [
        ("Both writers are the same.", "It ignores difference."), ("The better play is the longer one.", "Length is not a literary criterion."), ("There is nothing to compare.", "It gives up the task.")],
      "A balanced conclusion has a similarity and a difference.", T_CMP, "Reasoning", "Which has both?"),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="lil2-paper-2-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P2, 202)))

# ================================================================== Paper 3 practice paper A (20 parts on invented passages)
EX_A = ("**Invented extract A (not from a set text): a scene in a village health centre**\n\n"
        "ATEM, a nurse, checks a long list. BANJOH, a messenger, stands by the door.\n\n"
        "ATEM: (She checks the list, not looking up.) The medicine has not come.\n\n"
        "BANJOH: (He turns his cap in his hands.) The chief says it must come by Friday.\n\n"
        "ATEM: (She puts the list down at last. A child coughs off stage.) He said that last month. Every day I tell the mothers to wait one more day.\n\n"
        "BANJOH: I do not make the roads.\n\n"
        "ATEM: No. You only carry the excuses.")
EX_B = ("**Invented passage B (not from a set text)**\n\n"
        "By the time the market bell rang, Mama Ndi had sold half of her tomatoes. She did not shout like the others. She built her tomatoes into neat red towers and let their colour call the buyers. "
        "A young man, hurrying, knocked over the smallest tower. For a moment the market held its breath. Mama Ndi bent, picked up each tomato, wiped it on her cloth and set it back. "
        "\"The ground has had its share,\" she said gently. The young man, who had expected anger, left a note far larger than the cost of the damage, and walked away more slowly than he had come.")
EX_C = ("**Invented poem C (written for practice)**\n\n"
        "The Well at Dusk\n\n"
        "The well keeps watch till end of day,\nWhen women gather, one by one;\nTheir pots are full, their words are gay,\nAnd evening wraps the dying sun.\n\n"
        "The rope is old, the stone is worn,\nYet water rises cool and clear;\nIt serves each child that has been born\nAnd answers every thirsty year.")
P3 = [
    K("Question 1(a). Which words in extract A are stage directions that show Banjoh's nervousness?", "(He turns his cap in his hands.)", [
        ("The chief says it must come by Friday.", "That is dialogue."), ("I do not make the roads.", "That is dialogue."), ("ATEM, a nurse, checks a long list.", "That introduces the scene; it is not the direction that shows Banjoh's nerves.")],
      "The bracketed action shows his nerves.", "Modern drama and stagecraft", "Application", "Find the bracketed words about Banjoh.", passage=EX_A),
    K("Question 1(b). In the extract, 'excuses' means", "false or weak reasons given for failing to do something", [
        ("gifts", "Excuses are not gifts."), ("medicines", "Medicines are the subject, not the meaning."), ("apologies for rudeness", "It means reasons for failure, said with bitterness.")],
      "Meaning in context: reasons offered for failure.", "Modern drama and stagecraft", "Concept", "Atem is angry that the medicine has not come.", passage=EX_A),
    K("Question 1(c). Which adjective best describes Atem's attitude in the extract?", "Bitter and frustrated", [
        ("Cheerful and relaxed", "Her words are sharp."), ("Frightened of the chief", "Her last line attacks the messenger, not fear."), ("Indifferent", "She cares about the mothers.")],
      "Her final line and her tired words show bitterness.", "Characterization in modern drama", "Interpretation", "Look at her last line.", passage=EX_A),
    K("Question 1(d). What is the effect of the child's cough off stage?", "It is a sound effect that adds urgency and shows the cost of delay", [
        ("It shows the child is the messenger", "Nothing suggests this."), ("It shows the scene is a comedy", "The cough signals the problem."), ("It has no effect", "Sound effects do work on stage.")],
      "Off-stage sound is a stagecraft device.", "Modern drama and stagecraft", "Interpretation", "What does a cough in a health centre suggest?", passage=EX_A),
    K("Question 1(e). Which prop most helps to show that Atem avoids Banjoh at the start?", "The list she studies without looking up", [
        ("The door", "The door is not what she holds."), ("The fan", "No fan is mentioned in the extract."), ("The chief's cap", "The cap belongs to Banjoh.")],
      "She does not look up from the list.", "Modern drama and stagecraft", "Application", "What does she hold in the first line?", passage=EX_A),
    K("Question 1(f). Atem's last line, put into modern English prose in direct speech, could best be", "\"No, you only bring us reasons for failure.\"", [
        ("She said that he only brought excuses.", "The task requires direct speech."), ("\"No. You only carry the excuses.\"", "It copies the original."), ("\"No, you were not carrying anything.\"", "It changes the meaning.")],
      "A rendering keeps the meaning, direct speech and person.", "Writing about a Shakespeare play", "Application", "Which one is direct speech in new words?", passage=EX_A),
    K("Question 2(a). In passage B, 'held its breath' is an example of", "personification", [
        ("simile", "A simile uses like or as."), ("alliteration", "It is not a repeated sound."), ("onomatopoeia", "It is not a sound word.")],
      "A market cannot breathe, so the market is given a human action.", "Narrative voice and structure", "Concept", "Can a market hold its breath?", passage=EX_B),
    K("Question 2(b). 'She built her tomatoes into neat red towers' uses", "a metaphor that suggests order and skill", [
        ("a simile", "No 'like' or 'as'."), ("a rhyme", "There is no rhyme."), ("a sound word", "It is not onomatopoeia.")],
      "The towers compare piles of tomatoes to buildings.", "Reading the 19th and 20th century novel", "Concept", "Is there a like or as?", passage=EX_B),
    K("Question 2(c). Which two-word phrase best shows how Mama Ndi speaks to the young man?", "\"said gently\"", [
        ("\"neat red\"", "It describes the tomatoes."), ("\"market bell\"", "It describes the setting."), ("\"large note\"", "It describes the young man's payment.")],
      "Gently shows her calm manner.", "Reading the 19th and 20th century novel", "Application", "Which words describe her manner of speech?", passage=EX_B),
    K("Question 2(d). The narrator's attitude to Mama Ndi is", "admiring", [
        ("mocking", "The passage praises her."), ("angry", "The tone is calm."), ("indifferent", "The details show admiration.")],
      "Neat towers, gentle speech and calm response show admiration.", "Narrative voice and structure", "Interpretation", "Does the narrator praise or criticise?", passage=EX_B),
    K("Question 2(e). Which conflict-resolution skill does Mama Ndi show?", "She responds with calm kindness instead of anger", [
        ("She shouts at the young man", "She does not shout."), ("She calls the police", "Not in the passage."), ("She ignores the accident", "She picks up the tomatoes.")],
      "Her calm words defuse the situation.", "Character and theme in the prescribed novels", "Application", "What does she do after the tower falls?", passage=EX_B),
    K("Question 2(f). The young man's behaviour at the end shows that he", "felt ashamed and respected her response", [
        ("wanted to steal", "He pays more than the cost."), ("was angry", "He walks away more slowly."), ("did not notice", "He expected anger and is changed by gentleness.")],
      "He leaves more than the damage and walks slowly.", "Character and theme in the prescribed novels", "Interpretation", "Why does he leave a large note?", passage=EX_B),
    K("Question 2(g). The tone of passage B is", "warm and admiring", [
        ("bitter and angry", "No anger in the passage."), ("fearful", "No fear is shown."), ("bored", "The tone is interested.")],
      "The details are warm.", "Writing about a novel", "Concept", "How would you read it aloud?", passage=EX_B),
    K("Question 3(a). The rhyme scheme of the first stanza of poem C is", "ABAB", [
        ("AABB", "Lines one and two do not rhyme."), ("ABBA", "Lines one and four do not rhyme."), ("ABCD", "Lines one and three rhyme.")],
      "Day, one, gay, sun: A B A B.", "Prosody and scansion", "Application", "Match the line endings.", passage=EX_C),
    K("Question 3(b). 'The well keeps watch' is an example of", "personification", [
        ("simile", "No like or as."), ("hyperbole", "It is not exaggeration."), ("onomatopoeia", "No sound word.")],
      "A well cannot watch; human action is given to it.", "Prosody and scansion", "Concept", "Can a well watch?", passage=EX_C),
    K("Question 3(c). The metre of 'The rope is old, the stone is worn' is", "iambic tetrameter", [
        ("iambic pentameter", "That would have five feet."), ("trochaic tetrameter", "The stress falls on the second syllable of each foot, not the first."), ("anapestic trimeter", "The feet have two syllables, not three.")],
      "Eight syllables in four iambs: the ROPE is OLD the STONE is WORN.", "Prosody and scansion", "Application", "Count the stresses.", passage=EX_C),
    K("Question 3(d). The mood of the poem is", "calm and warm", [
        ("tense and angry", "No anger appears."), ("fearful", "No fear appears."), ("comic", "It is not comic.")],
      "Evening, gathering and gay words give calm.", "Critical approaches", "Interpretation", "How do the women speak?", passage=EX_C),
    K("Question 3(e). 'Answers every thirsty year' most likely means that the well", "gives water in every dry season", [
        ("speaks to the farmers", "It is a metaphor for giving water."), ("is only used in rainy seasons", "It answers dry years."), ("has no water", "It supplies water.")],
      "A thirsty year is a dry season; the well answers it with water.", "Critical approaches", "Interpretation", "What is a thirsty year?", passage=EX_C),
    K("Question 3(f). The repeated w sound in 'well', 'watch', 'women', 'wraps' and 'words' is", "alliteration", [
        ("assonance of the vowel a", "The repeated sound is a consonant."), ("onomatopoeia", "No sound is imitated."), ("rhyme", "The sound is at the start of words, not the end.")],
      "Repeated initial consonant sound is alliteration.", "Prosody and scansion", "Concept", "Which part of the words repeats?", passage=EX_C),
    K("Question 3(g). A central idea of the poem is that", "a well serves a community across generations", [
        ("wells are dangerous", "The tone is gentle."), ("old things should be thrown away", "The old rope still serves."), ("women should not talk", "Their words are gay.")],
      "The well serves 'each child that has been born'.", "Critical approaches", "Interpretation", "Who does the well serve?", passage=EX_C),
]
assert len(P3) == 20, len(P3)
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="lil2-paper-3-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P3, 203)))
