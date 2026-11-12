"""A Level Literature in English (0735), Upper Sixth: African & Post-Colonial Prose Fiction (4 lessons) and Geoffrey Chaucer & Canonical English Poetry (5 lessons).

The blueprint does not name the set texts, so the lessons rely on the Board's 2023 subject report, which names (old syllabus / new syllabus):
Nervous Conditions and Anthills of the Savannah, Across the Mongolo and The Lady With a Beard (prose); the General Prologue with the Franklin's
Prologue and Tale (old) or the Merchant's Prologue and Tale (new); Pope's The Rape of the Lock and Keats's Selected Poems (poetry).
Plot, character and theme facts are given only for works the author knows well and that are standard (Nervous Conditions, Anthills of the Savannah and
Things Fall Apart in outline; Chaucer's General Prologue, the Merchant's Tale and the Franklin's Tale in outline); for Across the Mongolo, The Lady With a
Beard and the poem selections the lessons give study frameworks, and the report's own descriptions of what questions asked. Poems and passages used
for analysis are original, written for these lessons. Middle English quotations are a few words of Chaucer (public domain). All paraphrased; check
facts against your own copy.
"""

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

OWNCOPY = ("**Use your own copy.** Every fact you use in an essay must be checked against your own copy of the text. This lesson gives you methods, "
           "frameworks and a few well-known facts written in our own words; editions and teachers' notes differ.")

LESSONS = []

# ------------------------------------------------------------------ 1. Reading African prose fiction
SAMPLE_1 = ("When the rains failed the second year, the old women of Ndu stopped quarrelling over the stream and began to share it. "
            "'A river that is dry,' said Grandmother Efua, 'teaches even enemies to carry water together.' The girls laughed, "
            "but they filled her gourd first.")

LESSONS.append(lesson(
    module=M_PROSE, topic=T_READ,
    title="How to read an African novel: voice, setting, structure and purpose",
    slug="liu1-reading-african-prose",
    minutes=24,
    summary="A reading method for African prose fiction: oral roots, proverbs and storytelling, setting and background, plot and structure, character types, and how to work out the novelist's purpose, with a tracker you can fill in for any set novel.",
    objectives=[
        "Name the features that African novels in English often draw from oral tradition",
        "Track setting, plot, structure, character and theme in a novel using a reading tracker",
        "Explain how background (history, society, place) shapes what a novel means",
        "Identify clues to a novelist's purpose and write a short note on a character, setting or event",
    ],
    key_concepts=["Oral tradition", "Proverb", "Setting and background", "Plot and structure", "Character types", "Novelist's purpose", "Short note"],
    blocks=[
        H("Introduction"),
        T("Before a novel is written down, a story is told. In Cameroonian villages from Bakossi to Bamenda, children grow up listening to tales after the evening meal: tales of the tortoise and other tricksters, tales about why the river runs where it does, tales with a lesson at the end. Many African novelists in English learned storytelling this way, and their books still carry its habits."),
        T("In Upper Sixth, the Board's report shows that the forty text questions in Paper 1 and the essays of Paper 2 come from the same set of things: background, setting, plot, structure, style, themes, characters, mood and the writer's craft. This lesson gives you a reading method that covers all of them, so that you read a novel like an examiner's question paper and not like a bedtime story."),
        T(OWNCOPY),
        H("African prose fiction and oral tradition"),
        D("**Oral tradition** is the body of stories, sayings, songs and history passed on by speaking, from one generation to the next. **Oral prose forms** include the folktale, the myth (a story of origins), the legend (a story about a hero or a past event), the proverb and the riddle.", title="Oral tradition and oral prose forms"),
        T("The Board's report lists 'types of oral prose forms' among the notions tested in Paper 1, so know these terms. Novelists such as Chinua Achebe are well known for bringing oral habits into the English novel: **proverbs** that sum up a community's wisdom, **storytelling** inside the story, **dialogue** that sounds like speech, **proverbs and idioms translated** from a home language, and a narrator who sometimes seems to be addressing a listening audience."),
        KEY("What oral roots can look like on the page", "Look for these signs in your set novel. Each is a 'point' you can later prove with evidence.", cards=[
            ["Proverbs and sayings", "Short sentences that carry a community's wisdom. Ask: who says it, to whom, and what does it show about values?"],
            ["Stories within the story", "A folktale or legend told by a character. Ask: why is it told here, and how does it comment on the main events?"],
            ["Songs, chants and rituals", "Ceremonies such as naming, burial and marriage. Ask: what do they show about community life and belief?"],
            ["Speech-like rhythm", "Repetition, direct address, question and answer. Ask: how does it make the reader feel part of an audience?"],
        ]),
        H("Reading for setting and background"),
        T("**Setting** is the place and time of the action. **Background** is the larger history behind it: the society, the political situation and the ideas of the time. The Board's report keeps reminding teachers to teach 'background issues', and in the new syllabus examples it names colonialism, assimilation, Negritude, the African personality, apartheid and neo-colonialism. A candidate who knows the background can explain *why* a character behaves as they do and not only *what* they do."),
        T("Ask three questions of every setting. Where is it (a village, a mission school, a capital city)? When is it (before colonial rule, during it, after independence)? And what does the place mean (a mission school may stand for new opportunity and for loss of tradition at the same moment)?"),
        H("Plot and structure"),
        D("**Plot** is the chain of events the writer chooses and arranges. **Structure** is how the book is built: its parts, chapters, order of events, turning points and ending. A novel can be told in time order, or can move back and forth with flashback.", title="Plot and structure"),
        T("Mark five points as you read: the **opening situation**, the event that starts the main trouble (the **inciting incident**), the **turning point**, the **climax**, and the **resolution** (or lack of one). Then ask: why did the writer put them in this order? An ending that does not tie everything up is a choice, and examiners reward you for saying what it achieves."),
        H("Character and theme"),
        T("Do not list traits. Show how a writer builds a character through **speech**, **action**, **what other characters say** and **the narrator's comment**. Then place each character in a type: the **protagonist** (the main figure), the **foil** (a character who throws light on another by contrast), the **round character** (complex, able to change) and the **flat character** (simple, represents one idea). A **theme** is an idea the book keeps returning to, such as identity, tradition and change, or power. A theme is not the same as a topic: 'education' is a topic, but 'education can free a person and also change them so much that they no longer fit at home' is a theme."),
        H("Working out the novelist's purpose"),
        T("The report mentions 'clues for identifying a novelist's purpose' as a tested notion. A writer's purpose is what the book as a whole seems designed to do: to entertain, to teach, to criticise a society, to record a lost way of life, to answer another writer's picture of Africa. You cannot see a purpose directly. You collect clues: the **title** (what does it point to?), the **epigraph** or opening lines, the **ending**, the **characters the narrator favours**, repeated images and the **tone** (serious, ironic, tender, angry)."),
        EX("Worked example 1: a reading tracker on an invented passage", intro="Read this invented passage (ours, not from a set text): 'When the rains failed the second year, the old women of Ndu stopped quarrelling over the stream and began to share it. A river that is dry, said Grandmother Efua, teaches even enemies to carry water together. The girls laughed, but they filled her gourd first.' Fill in a short tracker.", steps=[
            S("Setting and background", text="A village, Ndu, in a time of drought. Background: dependence on rain and on community cooperation."),
            S("Oral feature", text="A proverb-like saying spoken by an elder. It sums up the community's wisdom in one sentence."),
            S("Character", text="Grandmother Efua is a source of wisdom; the girls show respect through an action (they fill her gourd first) even while they laugh. Character is shown by speech and by action."),
            S("Theme and tone", text="Theme: hardship can create cooperation. Tone: gentle, warm, lightly humorous."),
            S("Possible purpose clue", text="The small action at the end tells us the community's values are stronger than its quarrels."),
        ]),
        EX("Worked example 2: a short note", intro="Short-note questions ask for a brief, focused account of a character, place or event with illustration and significance. Write a short note on 'the drought' in a novel you know. Here is a model for the invented passage: 'The drought in Ndu.'", steps=[
            S("Identify", text="The drought is the failure of rain for two years, which forces the villagers to rethink how they live together."),
            S("Illustrate (two or more points)", text="The old women stop quarrelling over the stream and begin to share it. Grandmother Efua says the dry river teaches enemies to carry water together."),
            S("Significance", text="The drought tests the community and shows its strength. It also drives the theme of cooperation and gives the passage its mood of hope."),
        ], check=""),
        TIP("The Board's report on a short-notes question warns against two errors: trying all five items instead of the three asked for, and writing a story instead of a note. Identify, illustrate with two or more points, then say why it matters, and keep each note short and numbered."),
        MISTAKE("Retelling the plot", "The report says again and again that weak answers narrate. When a question asks about a theme, a character or a technique, start from that idea and use story events only as evidence."),
        MISTAKE("Not knowing the whole text", "The report asks teachers to make sure the text is finished in class and read in full. If you only know the first half, a question on the ending or on a late episode will defeat you. Finish the book early, then re-read key chapters."),
        MISTAKE("Treating a topic as a theme", "'Marriage' is a topic. 'Marriage can be a trap for a woman whose family has no say' is a theme. Always make a claim."),
        QUIZ("A proverb spoken by an elder in a novel is best described as a feature of", [
            "oral tradition, because it carries a community's wisdom in spoken form", "stage direction, because it tells actors what to do", "the plot twist, because it ends the story", "free verse, because it has no rhyme"], 0,
            "A proverb is an oral prose form: a short saying used in speech that sums up shared wisdom.",
            hint="Think of where proverbs come from in everyday speech.",
            feedback=["", "Stage directions belong to drama, not to a proverb.", "A proverb may comment on events but it does not decide the plot.", "Free verse is a poetry term; proverbs belong to prose and speech."]),
        QUIZ("Which of these is a theme (and not only a topic)?", [
            "Colonialism", "Education that opens doors for a girl but also separates her from her family", "The village of Ndu", "A character named Efua"], 1,
            "A theme is a claim about life that the book keeps developing. The second choice states an idea you can prove with evidence.",
            hint="Which choice says something about life, not just names something?",
            feedback=["That is a topic; it names a subject but makes no claim.", "", "That is a setting.", "That is a character."]),
        PQ("Write a short note (about 60 words) on one setting from a novel you are studying. Use the three steps identify, illustrate, significance.", "Model plan with placeholders (use your own text): Identify: [name the place and say what it is]. Illustrate: [two moments in the book that happen there and what they show]. Significance: [what the place means for the theme or for a character's change]. Keep it short, numbered if the question numbers its parts, and use exact details from your copy."),
        PQ("Give two clues from a novel's opening or ending that could point to the novelist's purpose.", "For example: the title (what it names or alludes to) and the final scene (who survives, who is left speaking, what is unresolved). A good answer names the clue from your own text and says what purpose it suggests, such as criticism of a society or a record of a changing way of life."),
        PQ("Name three oral prose forms and give a one-line description of each.", "Folktale: a short traditional story, often with animals or a trickster and a lesson. Myth: a story of origins or of gods and the world. Legend: a story about a hero or a past event that people believe has some basis in history. (Proverb and riddle are also accepted forms.)"),
        SUM("African novels in English often draw on oral tradition: proverbs, stories inside the story, ceremonies and speech-like rhythm.", "Track setting, background, plot structure, character and theme as you read, and finish the whole book.", "A theme is a claim about life, not only a topic.", "Work out purpose from clues: title, opening, ending, favoured characters, repeated images and tone.", "Short notes: identify, illustrate with two or more points, give significance; do only the number asked."),
    ],
))

# ------------------------------------------------------------------ 2. Narrative perspective
PASS_FIRST = ("I did not tell my aunt about the letter. All that week I carried it folded in my school bag, and each time she smiled at me "
              "across the table I felt it grow heavier. Even now, years later, I cannot say whether I was protecting her or myself.")
PASS_THIRD = ("Mba carried the letter in her school bag all week and told no one. Her aunt, who noticed nothing, smiled at her across the table "
              "each evening. Neither of them knew that the letter would soon change the whole household.")

LESSONS.append(lesson(
    module=M_PROSE, topic=T_NARR,
    title="Narrative perspective: who tells the story and why it matters",
    slug="liu1-narrative-perspective",
    minutes=24,
    summary="The types of narrator and point of view, how narrative distance, reliability and retrospect shape what the reader knows and feels, and how to write about narrative technique in an African novel without retelling the plot.",
    objectives=[
        "Distinguish first-person, third-person limited, omniscient and multiple narration",
        "Explain how a narrator's knowledge, distance and reliability affect the reader",
        "Describe the effect of a retrospective narrator and of several narrators telling one story",
        "Write a paragraph on narrative technique that links technique to effect",
    ],
    key_concepts=["Narrator", "Point of view", "First-person narration", "Omniscient narrator", "Multiple narrators", "Retrospective narration", "Reliability", "Narrative distance"],
    blocks=[
        H("Introduction"),
        T("Two people from the same market can describe the same quarrel in different ways. The trader who was shouted at will say she was insulted. A bystander may say both were tired and hungry. The facts are the same, but the **way of telling** changes what you believe and who you pity. A novelist chooses a way of telling very carefully."),
        T("The Board's syllabus asks candidates to show how writers use narrative techniques, and the 2023 report lists 'effective use of narrative techniques' among the tasks set on the prose texts. The question is never only 'who is the narrator?'. It is 'what does this choice of narrator allow the novel to do?'"),
        T(OWNCOPY),
        H("Author, narrator and point of view"),
        D("The **narrator** is the voice that tells the story. The narrator is not the same as the **author**, who is the real person who wrote the book. **Point of view** is the position from which the story is told: whose eyes and mind the reader sees through.", title="Narrator and point of view"),
        KEY("Main types of narration", "Every novel uses one of these, or a mixture.", cards=[
            ["First-person narrator", "'I' tells the story and takes part in it. We see only what that person sees, knows and chooses to say. Strength: intimacy and voice. Limit: only one view."],
            ["Third-person limited", "The narrator says 'she' or 'he' but stays close to one character's thoughts. We know that character's mind but not the others'."],
            ["Third-person omniscient", "An all-knowing narrator moves between characters, places and times and can comment. Strength: wide view and irony. Limit: the narrator can seem to control the reader."],
            ["Multiple narrators", "Different characters (or a mixture of characters and a third-person voice) tell different parts. Strength: contrasting views of the same events."],
        ]),
        IMG("alliu1-narrators.svg", alt="Three small diagrams: first-person narrator inside the story, third-person limited narrator behind one character, omniscient narrator above all characters.", caption="Figure 1. Where the narrator stands: inside the story, at one character's shoulder, or above everyone."),
        H("Distance, reliability and tone"),
        T("**Narrative distance** is how close the narrator stands to the characters, from deeply inside a mind to far above events. **Reliability** is whether we can trust the narrator's account. A narrator is **unreliable** when we have reasons to doubt what is said: the narrator may be young, biased, ashamed, or may simply not understand what is happening. **Tone** is the narrator's attitude, shown by the choice of words: sympathetic, ironic, angry, detached."),
        H("Retrospective narration"),
        D("In **retrospective narration** an older narrator looks back on earlier events. There are two 'selves' in the telling: the younger self who lived the events and the older self who tells them and can judge them.", title="Retrospective narrator"),
        T("Tsitsi Dangarembga's Nervous Conditions (published 1988) is told in the first person by Tambudzai, called Tambu, who is looking back on her childhood and youth in colonial Rhodesia. The first sentence of the novel is famous for its shock: the narrator says she was not sorry when her brother died. Because an older Tambu is speaking, she can comment on, question and sometimes condemn what her younger self believed. When you write about the novel, ask what the older voice sees that the younger girl could not."),
        H("Several narrators"),
        T("Chinua Achebe's Anthills of the Savannah (published 1987) is told through several voices. Chapters are told in turn by main characters (Chris Oriko, Ikem Osodi and Beatrice Okoh) and by a third-person narrator, so the reader receives contrasting views of the same fictional country and its crisis. No single voice is the full truth. The reader must compare them. Check in your copy which chapters belong to which narrator, and what you learn from each. The effect is a kind of conversation among characters, which fits a book about debate, power and responsibility."),
        EX("Worked example 1: identify and explain the perspective", intro="Read the two invented passages (written for this lesson). Passage A: 'I did not tell my aunt about the letter. All that week I carried it folded in my school bag, and each time she smiled at me across the table I felt it grow heavier. Even now, years later, I cannot say whether I was protecting her or myself.' Passage B: 'Mba carried the letter in her school bag all week and told no one. Her aunt, who noticed nothing, smiled at her across the table each evening. Neither of them knew that the letter would soon change the whole household.'", steps=[
            S("Passage A", text="First-person and retrospective. 'I' and 'even now, years later' show an older narrator looking back."),
            S("Effect of A", text="We feel the girl's guilt from inside. The older voice adds doubt: she cannot judge her own motives, which makes her honest and humanly uncertain."),
            S("Passage B", text="Third-person omniscient. The narrator knows what the aunt does not notice and what neither character knows: the future."),
            S("Effect of B", text="It creates suspense and dramatic irony (the reader knows more than the characters). The narrator stands above them."),
        ]),
        EX("Worked example 2: from technique to effect in one paragraph", intro="Write a PEEL paragraph on 'the effect of a retrospective narrator' using Passage A.", steps=[
            S("Point", text="The older narrator allows the writer to combine a child's feelings with an adult's judgement."),
            S("Evidence", text="In Passage A the girl feels the letter 'grow heavier', but the older voice adds 'even now, years later'."),
            S("Explain", text="The first phrase gives us the young girl's anxiety; the second shows an adult who still cannot decide whether she acted from love or fear. The mixture makes her more truthful and more complex."),
            S("Link", text="Retrospective telling therefore lets the novel judge its own past, which is how a reader trusts and questions a narrator at the same time."),
        ]),
        TIP("Exam link: narrative techniques appear in Paper 2 (essay questions on 'the effective use of narrative techniques') and in the Paper 1 multiple-choice questions on the prose texts. Always finish a technique point with its effect on the reader, on a character or on the theme."),
        MISTAKE("Confusing narrator and author", "Never write 'Dangarembga felt guilty' when you mean the narrator. Write 'Tambu, the narrator, ...'. The author chose the narrator; the narrator is a character in the telling."),
        MISTAKE("Naming the type without the effect", "'The novel uses first-person narration' earns very little. Say what it allows: closeness, a single limited view, a voice you may or may not trust, and why that suits the theme."),
        MISTAKE("Assuming first-person means truthful", "A first-person narrator may be mistaken, biased or ashamed. Look for gaps between what the narrator says and what the other characters or events show."),
        QUIZ("A narrator who stands above all characters and knows their thoughts and the future is", [
            "first-person limited", "third-person omniscient", "unreliable first-person", "retrospective first-person"], 1,
            "All-knowing, above the characters: that is omniscient narration.",
            hint="Which type can enter every mind?",
            feedback=["A first-person narrator cannot enter other minds.", "", "Unreliable narrators are doubted; they do not know everything.", "A retrospective narrator looks back but is still one person."]),
        QUIZ("What is the main advantage of telling a novel through several narrators?", [
            "The story becomes shorter", "The reader gets contrasting views and must compare them", "The author's opinion is always stated clearly", "All characters become equally good"], 1,
            "Different voices give different views of the same events; the reader weighs them.",
            hint="Think about what you gain when two people disagree about the same event.",
            feedback=["Number of narrators does not shorten a novel.", "", "With many voices, the author's view is harder to pin down, not clearer.", "Several narrators say nothing about moral goodness."]),
        PQ("Explain what a retrospective narrator allows a novelist to do.", "The novelist can show a child's or young person's experience as it felt at the time and, through the older voice, comment on it with later understanding, irony or regret. This gives depth and often shows how the narrator has changed."),
        PQ("Give one strength and one limit of first-person narration.", "Strength: closeness to one mind and a distinctive voice. Limit: the reader knows only what the narrator knows or chooses to say, and the narrator may be mistaken or biased. A full answer uses an example from your set novel."),
        PQ("Plan a paragraph on the effect of multiple narrators in a novel you are studying (use placeholders).", "Point: several narrators give contrasting views of [event or situation]. Evidence: [one moment told by narrator 1 and the same issue seen by narrator 2 in your copy]. Explain: the contrast shows [what each character values or fears] and forces the reader to judge. Link: the technique supports the theme of [theme]."),
        SUM("The narrator is not the author; point of view is the position from which the story is told.", "Know first-person, third limited, omniscient and multiple narration, and what each allows.", "Distance, reliability and tone control what the reader trusts and feels.", "A retrospective narrator joins a younger and an older self, as in Nervous Conditions.", "Always link a technique to its effect on the reader, character or theme."),
    ],
))

# ------------------------------------------------------------------ 3. Post-colonial themes
THEMES_TABLE = """Theme                         Question to ask of your novel
----------------------------  -----------------------------------------------
Culture clash                 Where do two ways of life meet, and who pays?
Assimilation / mimicry        Who copies the colonizer, and what is lost?
Language and identity         Which language is spoken, by whom, with what power?
Education                     Does schooling free a person, change them, or both?
Gender and patriarchy         How are women treated by tradition AND by colonial rule?
Neo-colonialism / bad rule    Who rules after independence, and for whose benefit?
Tradition and change          Which old values are worth keeping, which are not?
Memory and storytelling       Who tells the history, and is the telling honest?"""

LESSONS.append(lesson(
    module=M_PROSE, topic=T_POST,
    title="Post-colonial themes in African fiction: culture clash, identity, gender and power",
    slug="liu1-postcolonial-themes",
    minutes=25,
    summary="What post-colonial means, the background ideas the Board's report names (assimilation, Negritude, neo-colonialism and more), the main themes with examples from Nervous Conditions and Anthills of the Savannah, and frameworks for your other set novels.",
    objectives=[
        "Explain post-colonial, assimilation, Negritude, neo-colonialism and related background terms",
        "Identify the main post-colonial themes in an African novel and prove them with evidence",
        "Apply the themes to Nervous Conditions and Anthills of the Savannah (in outline) and to your own set novels",
        "Evaluate a post-colonial reading: what it explains and what it can miss",
    ],
    key_concepts=["Colonialism", "Post-colonial", "Assimilation", "Negritude", "Neo-colonialism", "Hybridity", "Patriarchy", "Culture clash"],
    blocks=[
        H("Introduction"),
        T("Cameroon itself has lived through three colonial histories: German rule before 1916, then British and French administration of different parts of the country under international mandates, and then independence for each part in 1960 and 1961. Cameroonians often speak of their history in terms of two languages and two education systems. That shared experience is one reason why African writers have so much to say about what happens when a country, a language and a school system are shaped by outsiders and then handed back."),
        T("The Board's 2023 report tells teachers to cover the 'background issues' for the prose and poetry texts: it names colonialism, assimilation, Negritude, the African personality, apartheid and neo-colonialism, alongside the themes inside each book. This lesson explains these ideas and shows you how to use them as tools for reading, not as lists to memorise."),
        T(OWNCOPY),
        H("Key terms"),
        D("**Colonialism** is the rule of one people over another by force or by treaty, with the ruler taking political, economic and cultural control. **Post-colonial** has two linked meanings: the period after colonial rule has ended, and a way of reading texts that studies how colonial history shapes identity, language, power and writing itself.", title="Colonialism and post-colonial"),
        KEY("Background ideas named in the Board's report", "Know each in one or two sentences, and know which texts of yours connect to it.", cards=[
            ["Assimilation", "The aim of making colonized people adopt the colonizer's language and culture. It is especially linked with French policy. Novels show it through characters who copy a foreign way of life."],
            ["Negritude", "A cultural and literary movement of black writers in the 1930s and after, associated with Leopold Senghor, Aime Cesaire and Leon Damas, that affirmed the value of black culture against the idea of European superiority."],
            ["African personality", "An idea, associated in the independence era with leaders such as Kwame Nkrumah, that Africans should define their own identity and values and take pride in them."],
            ["Apartheid", "South Africa's system of legal racial separation, which ran from 1948 until the 1990s, ended by the first democratic election in 1994."],
            ["Neo-colonialism", "A term popularised by Nkrumah for continuing outside control, mainly economic, after political independence; in novels it also appears as a local ruling class that copies colonial habits."],
        ]),
        T("Critics also use a few other terms. **Hybridity** (a word associated with Homi Bhabha) means a mixing of cultures so that someone is neither wholly 'traditional' nor wholly 'European'. **Mimicry** means copying the colonizer in a way that is never quite accepted. **Patriarchy** is a system in which men hold the main power in families and society. Frantz Fanon's book The Wretched of the Earth (1961) is a classic study of the mind of colonized people and a source for the title of Nervous Conditions. Check your textbook for how your teacher defines each term."),
        H("Themes and the questions that unlock them"),
        CODE(THEMES_TABLE, "text", title="Post-colonial themes: a checklist"),
        H("Nervous Conditions: education, gender and the colonized mind"),
        T("In outline: Tambu grows up in a poor homestead in colonial Rhodesia and is determined to get an education. Her brother Nhamo is sent to the mission school run under the authority of their uncle, the headmaster Babamukuru. When Nhamo dies, Tambu is given his place. At the mission she meets her cousin Nyasha, who has lived in England and returns questioning both her own culture and her family's rules; Nyasha's struggle, which ends in a serious illness, is one of the book's most powerful strands. Women such as Maiguru (Babamukuru's educated wife), Lucia and Tambu's mother show different relationships to male authority."),
        T("Themes you can prove: **education** as both opportunity and loss of self; **gender**, since the novel shows that girls and women face pressure from African patriarchy *and* from colonial society (a 'double burden'); **identity and hybridity**, in Nyasha's divided self; **colonial assimilation**, in the mission's values. Note the title: it points to a sickness of mind produced by colonial conditions."),
        H("Anthills of the Savannah: power after independence"),
        T("In outline: the fictional West African country of Kangan is ruled by a military head of state called His Excellency (Sam). His old school friends Chris Oriko (Commissioner for Information) and Ikem Osodi (editor of the national newspaper) find themselves on different sides of his growing authoritarian rule; Beatrice Okoh, a senior official, is connected to both. The novel follows their conflict and its consequences. Episodes named in the Board's report include the drought in Abazon, the storming of the presidency by an Abazon delegation, the naming ceremony of Elewa's baby Amaechina, the Abichi Guest House party and the killing of Chris."),
        T("Themes you can prove: **power and its abuse** in a post-independence state (this is the post-colonial theme of internal failure, not only outside blame); the **role of intellectuals and journalists**; **the neglect of the poor** (Abazon); **women's roles and voices** (Beatrice, Elewa); **storytelling** as a way of keeping memory and hope alive; and **community and renewal** in the naming ceremony."),
        H("Your other set novels: use a framework"),
        T("The report describes questions set on Across the Mongolo (love experiences, shown as relieving or destructive; landscape and environment) and on The Lady With a Beard (Bakossi traditional values as a small picture of African traditional society; events in which women's rights are ignored or trampled). Use your own copy and teacher's notes for events and characters. For each novel fill in the checklist above, and for a theme question collect at least three events across the whole book. The Board's report says candidates who fail to cover both sides of a two-sided question, such as two relieving and two destructive love experiences, lose marks."),
        H("Evaluating a post-colonial reading"),
        T("A good essay does not only apply the label. It asks how far the label explains the book. **Strengths:** it connects private lives to history, explains why characters face divided loyalties, and gives a language for power and identity. **Limits:** it can make every problem look like an outside cause. Many African novels, Anthills among them, also show failures that come from within the society, and many books are about love, family, or personal conscience as well. Some critics also warn that 'post-colonial' can flatten very different countries into one story. Mention one limit in your essay's last paragraph to show the Board's 'critical perspective'."),
        EX("Worked example 1: proving a theme", intro="Question (written for practice): 'Show how Nervous Conditions presents education as both a gift and a burden.' Plan the main paragraphs.", steps=[
            S("Thesis", text="Education opens a path for Tambu but separates her from her family and shows the pressure of a colonial system."),
            S("Point 1: the gift", text="Tambu's determination to go to school and her chance to study at the mission after Nhamo's death. Explain: schooling is her way out of the limits of a poor homestead."),
            S("Point 2: the cost", text="The mission school's values and her growing distance from home. Evidence from your copy, and what she feels as she changes."),
            S("Point 3: contrast", text="Nyasha, who is highly educated yet unhappy and in conflict with her father. Explain: education alone does not free a person."),
            S("Evaluation", text="The novel does not reject education; it asks what kind of education and at what price."),
        ]),
        EX("Worked example 2: neo-colonialism in Anthills", intro="Write a PEEL paragraph for: 'Anthills of the Savannah shows that independence did not end the people's suffering.'", steps=[
            S("Point", text="Achebe shows that the ruling class of a free country can fail the poor in much the same way as outside rulers."),
            S("Evidence", text="The Abazon drought and the neglect of its people by those in the capital (check the exact episode in your copy)."),
            S("Explain", text="The suffering is not caused by an outside power but by decisions and silences inside the state. The novel therefore criticizes post-independence leaders."),
            S("Link", text="This supports the wider theme of leadership and responsibility, and shows that the novel looks inward as well as backward."),
        ]),
        TIP("Exam link: background and themes are tested in Paper 1 (4 multiple-choice questions per set text, according to the Board's report) and in Paper 2 essays and short notes. Know your terms and three events per theme."),
        MISTAKE("Using one-word labels", "Writing 'colonialism' or 'neo-colonialism' without an event and an explanation earns little. Each label needs evidence from your text and a line on what it shows."),
        MISTAKE("Mixing up traditions of two places", "The report records candidates who could not separate Bakossi values from wider African tradition. When asked for a microcosm (a small picture of a larger whole), give the local detail first and then say how it represents the wider pattern."),
        MISTAKE("Reading every book only as protest", "A post-colonial reading is a tool. Also read for love, family, humour and personal choice, and for faults that come from within a community."),
        QUIZ("Which pair is correctly matched?", [
            "Assimilation: encouraging colonized people to adopt the colonizer's culture", "Negritude: South Africa's racial separation laws", "Apartheid: a movement of black writers in Paris", "Neo-colonialism: a Cameroonian novel"], 0,
            "Assimilation is the policy of making colonized people adopt the colonizer's culture.",
            hint="Match each term with its meaning, not its sound.",
            feedback=["", "Negritude was a literary and cultural movement; apartheid is the South African system.", "Apartheid was a legal system, not a literary movement.", "Neo-colonialism is a concept about continuing outside control."]),
        QUIZ("Why does Nervous Conditions present gender as part of a colonial theme?", [
            "Because only women lived in colonial Rhodesia", "Because women meet pressure from both African patriarchy and colonial society", "Because men are never shown as colonized", "Because the novel has no male characters"], 1,
            "The novel shows girls and women constrained by family and tradition and by colonial society together.",
            hint="Think of Nyasha, Maiguru and Tambu's mother.",
            feedback=["Colonial Rhodesia had men and women of all kinds.", "", "The novel shows male characters also shaped by colonial pressures.", "The novel has many male characters."]),
        PQ("Define neo-colonialism and say how it can appear in a novel set after independence.", "Neo-colonialism means continuing outside influence or control, usually economic, after political independence; in a novel it may also appear as local rulers who copy colonial attitudes and neglect their own people. A full answer names an episode from your text. For Anthills, the neglect of the poor and the abuse of power by rulers are examples to check in your copy."),
        PQ("Write a thesis sentence for: 'Examine the theme of tradition and change in a post-colonial novel you have studied.'", "Model: In [title], [author] shows that [tradition] is neither simply good nor simply bad, but that [change] brings both loss and opportunity, as seen in [two characters or events]. Replace the brackets with details from your own copy."),
        PQ("Give two strengths and one limit of reading an African novel as a post-colonial text.", "Strengths: it links private lives to history and gives a way to discuss identity, language and power. Limit: it can overlook faults that come from within the society and personal themes such as love and conscience. Use an example from your text."),
        SUM("Post-colonial means after colonial rule and also a way of reading that studies the effects of colonial history.", "Know assimilation, Negritude, African personality, apartheid and neo-colonialism, as the report asks.", "Prove each theme with several events across the whole text and say what each shows.", "Nervous Conditions: education, gender and the colonized mind. Anthills: power and neglect after independence.", "Evaluate: say what a post-colonial reading explains and what it can miss."),
    ],
))

# ------------------------------------------------------------------ 4. Writing about an African novel
QTYPES = """Question type (from the Board's 2023 report)   What it needs
-------------------------------------------------   ------------------------------------------
Three characters and a cause (movement, place)      three named characters, each with evidence
Short notes: do 3 of 5 items                         identify, 2+ illustrations, significance
Three dramatic episodes and their effectiveness     tense, important scenes + what they achieve
Two-sided: relieving and destructive experiences    balance (e.g. two of each), a point per side
Values as a microcosm of a wider society            local detail, then the wider pattern
Events showing a group's rights ignored             events chosen, each with a reason and a result"""

LESSONS.append(lesson(
    module=M_PROSE, topic=T_WRITE,
    title="Writing an essay on an African novel: questions, plans and model answers",
    slug="liu1-writing-african-novel",
    minutes=25,
    summary="How to read an A Level prose question, plan it, and write a focused essay or short note on an African novel, built from the question types and weaknesses described in the Board's 2023 report, with model plans for character, episode and theme questions.",
    objectives=[
        "Interpret common A Level question types and the tags in them (examine, to what extent, discuss)",
        "Plan an essay with a thesis, three or four points and several illustrations per point",
        "Write short notes and dramatic-episode answers that stay on the question",
        "Avoid the faults the Board's report describes: retelling, imbalance, thin evidence and weak language",
    ],
    key_concepts=["Question tags", "Thesis", "Topic sentence", "Illustration", "Dramatic episode", "Effectiveness", "Short notes", "Critical perspective"],
    blocks=[
        H("Introduction"),
        T("In the 2023 examination, one question on a Cameroonian novel was answered by 4 499 candidates and about two thirds of them passed it, while a question on the dramatic episodes of another novel had not one candidate in the top band. The difference was not the book. It was whether candidates understood the question and answered it with evidence. This lesson shows you how."),
        T("The Board's report says Paper 2 essays ask candidates to 'initiate and sustain fluent and convincing discussions': to discuss, comment, illustrate, show the extent of a claim, and judge the validity of statements about characters, settings, themes and techniques. Candidates choose four questions in all, one from each section, and a fourth from any section but a different text, according to the report, so you must be able to write a good prose essay quickly."),
        T(OWNCOPY),
        H("Reading the question: tags and types"),
        KEY("Common tags and what they ask", "The report advises teaching these early in the year.", cards=[
            ["Examine, discuss", "Look at the idea from several angles with evidence; weigh points."],
            ["Illustrate, show how", "Give examples from the text and say how they prove the point."],
            ["To what extent, how far, do you agree", "Argue a position: it is partly true, mostly true or false, and say why. Include a counter-point."],
            ["Justify, how true", "Defend the statement with evidence; then show where it has limits."],
            ["Comment on the effectiveness of", "Say what the device or episode achieves for plot, theme, character or mood."],
        ]),
        CODE(QTYPES, "text", title="Question types in the Board's 2023 report (paraphrased)"),
        T("Notice how each type is about a relationship between **a text feature and a result**. 'Dramatic episode' questions want effectiveness. 'Character' questions want how the writer builds the person and what the person shows. 'Two-sided' questions want balance."),
        H("Planning in five minutes"),
        T("Write a one-sentence answer to the question (your **thesis**). List three or four points. Beside each point write two or three pieces of evidence from different parts of the book. Say in a word what each proves. Cross out the plan when you finish; do not cross out the essay. The report notes that planning saves time and improves structure."),
        H("Writing the paragraph"),
        D("A paragraph begins with a **topic sentence** that answers the question, continues with supporting sentences that give **several illustrations** (events, speeches, details), explains each, and ends with a **concluding sentence** that links back to the question.", title="Topic sentence and illustrations"),
        T("The report's strongest message on structure is that one sketchy illustration in a paragraph earns a skimpy mark, while several apt and focused illustrations make the paragraph full and persuasive. Use at least two or three pieces of evidence per point, taken from different parts of the book, and never use the same illustration for two points."),
        H("Dramatic episodes"),
        D("A **dramatic episode** is a scene or incident of high tension and importance: a quarrel, a confrontation, a ceremony, a death, a revelation. It is not any action. Its **effectiveness** is what it achieves: moving the plot, revealing character, developing a theme, creating suspense or mood.", title="Dramatic episode"),
        T("The Board's report says many candidates treated any action as a dramatic episode, and that no one scored in the top band on a question asking for three episodes in Anthills of the Savannah. The better answers chose important scenes, described them briefly, and then spent most of their words on significance."),
        EX("Worked example 1: three dramatic episodes in Anthills", intro="Question (written for practice): 'Select three dramatic episodes in Anthills of the Savannah and comment on their effectiveness.' Use the episodes the report names as possibilities: the Abazon delegation's storming of the presidency; the naming ceremony of Amaechina; the killing of Chris.", steps=[
            S("Thesis", text="Achebe uses these episodes to show a state in crisis and to leave room for hope after loss."),
            S("Episode 1: the Abazon delegation", text="Describe it briefly (check details in your copy). Effectiveness: it brings the neglected poor into the world of the rulers, builds tension, and develops the theme of power and neglect."),
            S("Episode 2: the naming ceremony", text="Describe the ceremony and its setting. Effectiveness: it shows community, tradition and women's roles, and gives the novel an ending of renewal after death."),
            S("Episode 3: the killing of Chris", text="Describe the circumstances. Effectiveness: it is the moment of greatest loss, it shows the cost of resisting a brutal system, and it changes the surviving characters."),
            S("Conclusion", text="The three scenes move from crisis to loss to renewal, which shapes the novel's final message."),
        ]),
        EX("Worked example 2: a three-character question", intro="Question (written for practice): 'Show how the environment affects three characters in Nervous Conditions.'", steps=[
            S("Choose characters with clear evidence", text="For example Tambu (homestead to mission school), Nyasha (England to Rhodesia) and Maiguru (educated woman in a patriarchal home). Check each against your copy."),
            S("Point 1: Tambu", text="Environment of poverty and then of the mission shapes her ambition and her sense of self. Give two or three moments."),
            S("Point 2: Nyasha", text="Years in England and a return to a strict home create conflict and distress. Give two or three moments."),
            S("Point 3: Maiguru", text="A home where her education counts for less than her husband's authority. Give two or three moments."),
            S("Balance", text="Show positive and negative effects on at least one character, as the report notes that better answers do."),
        ]),
        H("Short notes"),
        T("For a 'write short notes on three of five' question, do exactly three, label them with the numbers given, and for each: identify, give two or more illustrations, then state its significance. Do not narrate the whole book. Fifty to a hundred words each is a good target."),
        H("Language"),
        T("Examiners mark your English. Use the present tense for the novel ('Beatrice tells...'), clear topic sentences, linking words (however, moreover, in contrast, as a result), and legible handwriting. Spell titles and names exactly."),
        TIP("Exam link: Paper 2 Section B (prose): the report says there were two questions on each of the eight set texts across the paper, and candidates choose four questions in all. Practise one full prose essay in 40 minutes and one set of short notes in 20."),
        MISTAKE("Retelling the story", "The report records answers that were 'mere or pointless narration'. Begin every paragraph with a point, not with 'then'."),
        MISTAKE("Unbalanced two-sided answers", "A question about relieving and destructive love experiences, or about merits and demerits, wants both sides. The report says many answers were lopsided; aim for the balance the question requests."),
        MISTAKE("Mixing up characters or places", "Confusing characters, places or episodes, or giving no evidence, signals that you did not read the book. Keep a one-page character and event list for each text."),
        QUIZ("A question says 'To what extent do you agree?'. Which is the best approach?", [
            "Agree completely and give three examples", "Take a clear position, support it with evidence and acknowledge a limit", "Write everything you know about the novel", "Disagree without examples"], 1,
            "An 'extent' question wants a position with evidence and a counter-point.",
            hint="Look at the words 'to what extent'.",
            feedback=["That ignores the idea of extent.", "", "That is not focused on the question.", "Without evidence the answer cannot score."]),
        QUIZ("Which is the best test of a 'dramatic episode'?", [
            "Any event in the novel", "A scene of high tension and importance whose effects you can explain", "A character's description", "The first chapter only"], 1,
            "A dramatic episode is important and tense, and you can say what it achieves.",
            hint="Think of scenes that change the plot.",
            feedback=["The report says choosing any action was a common error.", "", "A description is not an episode.", "The episode can come from anywhere in the book."]),
        PQ("Write an introduction (about 60 words) for the question 'Examine the theme of gender inequality in a novel you have studied'. Use placeholders for details.", "Model: In [title], [author] presents gender inequality as [claim], shown through [event 1], [event 2] and [event 3]. The novel also suggests that [limit or complication]. This essay will examine these events and show how they develop the theme. The introduction is focused, names the text and author and gives a route through the essay."),
        PQ("Outline the body of a two-sided answer: 'Show how love is both a relief and a source of suffering in a novel you know.'", "Thesis: love relieves and destroys. Paragraph 1: a relieving experience (event, evidence, effect). Paragraph 2: another relieving experience. Paragraph 3: a destructive experience. Paragraph 4: another destructive experience. Conclusion: what the balance shows about the novel's view. This matches the 'two of each' balance the report describes for a question on Across the Mongolo."),
        PQ("Write short notes (three sentences) on 'The naming ceremony of Amaechina' from Anthills of the Savannah.", "Identify: it is the ceremony in which Elewa's baby is given a name (check the details). Illustrate: describe two details such as who is present and how the child is named. Significance: the ceremony shows tradition, community and hope, and gives the novel a point of renewal after loss."),
        SUM("Read the tags: examine, discuss, illustrate, to what extent, comment on effectiveness.", "Plan a thesis and three or four points with several illustrations each.", "Paragraph: topic sentence, illustrations, explanation, concluding sentence.", "Dramatic episodes are important tense scenes; write on effectiveness.", "Avoid retelling, imbalance, thin evidence and weak language; use the present tense."),
    ],
))

# ------------------------------------------------------------------ 5. Chaucer's language and world
GLOSS = """Middle English        Modern English
-------------------   -------------------------
whan                  when
ful                   very, fully
soote                 sweet
droghte               dryness, drought
hath                  has
wolde                 would
gladly                willingly
lerne / teche         learn / teach
worthy                worthy, of good standing
ther                  there, where
nevere                never"""

LESSONS.append(lesson(
    module=M_CHAUCER, topic=T_LANG,
    title="Chaucer's Middle English, verse form and medieval world",
    slug="liu1-chaucer-language-world",
    minutes=24,
    summary="Who Chaucer was, how Middle English differs from modern English (spelling, sounds, grammar, vocabulary), how his iambic pentameter couplets work, and the medieval background of feudalism, the Church, pilgrimage, chivalry, love and medicine that the Board's report asks you to know.",
    objectives=[
        "Place Chaucer in his time and say what Middle English is",
        "Read Middle English lines using spelling, word-ending and glossary clues",
        "Scan a Chaucer line as iambic pentameter and identify rhyming couplets",
        "Explain the medieval background: feudal society, Church, pilgrimage, chivalry, courtly love and medicine",
    ],
    key_concepts=["Middle English", "Iambic pentameter", "Heroic couplet", "Feudalism", "Estates", "Pilgrimage", "Chivalry", "Courtly love", "Humours"],
    blocks=[
        H("Introduction"),
        T("Imagine a language where 'knight' is spoken with the k and the gh sounds, where 'whan' means 'when', and where one poet in London in the 1380s decides to write a long poem not in French or Latin but in the English spoken by ordinary people. That poet was **Geoffrey Chaucer**, and the poem was The Canterbury Tales."),
        T("The Board's report tells teachers to teach 'background issues' for Chaucer: it names feudalism, religion, chivalry, love, and medieval scholarship and medicine. It also says candidates who stay inside the General Prologue alone cannot do well. This lesson builds the background you need for both the General Prologue and your prescribed tale."),
        T(OWNCOPY),
        H("Chaucer and his time"),
        T("Geoffrey Chaucer was born in London in about 1343 and died in 1400. He was the son of a wine merchant, and he worked as a courtier, a soldier, an official of the king's customs and a diplomat. He wrote The Canterbury Tales mainly in the 1380s and 1390s and left it unfinished. The plan, announced in the General Prologue, was for each pilgrim to tell several tales on the road to Canterbury and back, but only about twenty-four tales survive in whole or in part. Many scholars call him the father of English poetry because he made English a serious literary language."),
        T("His lifetime saw the Black Death (1348 to 1349, which killed a very large share of the population), the long war with France and the Peasants' Revolt of 1381. He was a reader of French, Italian and Latin, and his poems are full of allusions (references) to classical myths, the Bible and earlier writers. The report names such allusions as a tested feature."),
        D("**Middle English** is the stage of the English language spoken and written from about 1100 to about 1500. It grew from Old English with a great influx of French words after the Norman Conquest of 1066. Chaucer wrote in the London dialect of the late fourteenth century.", title="Middle English"),
        H("Reading Chaucer's language"),
        KEY("Five clues for reading Middle English", "You do not need to memorise a grammar. Use these clues.", cards=[
            ["Spelling is not fixed", "Words can be spelled in different ways (nevere/never). Read aloud and the word often appears."],
            ["Say the sounds", "Letters were pronounced that later fell silent: the k in knight, the gh, the l in folk. Vowels were closer to those of French and Italian than to modern English."],
            ["Final -e", "A final e was often pronounced as a short syllable when the metre needed it (not before a word starting with a vowel or h). Chaucer's line needs it to scan."],
            ["Word endings", "-eth for 'he does' (he goeth), -en for plurals and infinitives, y- before past participles. Thou is for one familiar person, ye for several or for a respected person."],
            ["Double negatives", "Two or more negatives strengthen the denial in Middle English; they do not cancel."],
        ]),
        CODE(GLOSS, "text", title="A small glossary of common words"),
        EX("Worked example 1: reading the opening", intro="Read the first two lines of the General Prologue: 'Whan that Aprill with his shoures soote / The droghte of March hath perced to the roote'. Put them into modern English.", steps=[
            S("Glossary", text="whan that = when; shoures soote = sweet showers; droghte = dryness; hath perced = has pierced."),
            S("Word order", text="'his' here means 'its': April with its sweet showers."),
            S("Modern English", text="When April with its sweet showers has pierced the dryness of March to the root."),
            S("Comment", text="The sentence opens the poem with spring, rebirth and growth, and prepares the reader for the pilgrimage setting."),
        ]),
        H("Verse form: iambic pentameter and couplets"),
        D("An **iambic foot** is one weak syllable followed by one strong syllable. **Pentameter** means five feet to the line, so ten syllables (eleven if the line ends on an extra weak syllable). Two rhyming lines in a row are a **couplet**, and the iambic pentameter couplet is often called the **heroic couplet**.", title="Iambic pentameter and couplets"),
        T("Most of the General Prologue and the tales that are in verse use iambic pentameter couplets (rhyme scheme aa bb cc). Two of the tales, Melibee and the Parson's Tale, are in prose. The regular beat and the rhyme help to make the poem easy to remember and to read aloud, and they give a sense of order that Chaucer can then use for comedy when a character does not live up to it."),
        IMG("alliu1-iambic-line.svg", alt="A Chaucer line split into five feet, each with a weak syllable marked x and a strong syllable marked with a slash.", caption="Figure 1. Scansion of a Chaucer line: five feet, ten syllables."),
        EX("Worked example 2: scanning a line", intro="Scan 'A Knyght ther was, and that a worthy man' (the first words of the Knight's portrait).", steps=[
            S("Count syllables", text="A (1) Knyght (2) ther (3) was (4) and (5) that (6) a (7) wor (8) thy (9) man (10). Ten syllables."),
            S("Mark the stresses", text="Read it naturally: a KNYGHT ther WAS and THAT a WOR thy MAN. The strong syllables fall on every second syllable."),
            S("Name the pattern", text="Five iambs: iambic pentameter. This line also ends a couplet with the next line, so check the rhyme in your copy."),
        ], check=""),
        H("The medieval world behind the poem"),
        T("**Feudalism** was the system by which land was held from a lord in return for service. Society was often described in three **estates**: those who fight (knights), those who pray (the clergy) and those who work (peasants). Chaucer's pilgrims include members of all three and many in between, such as merchants, lawyers and guildsmen, which tells us society was already more complex. The pilgrims are a cross-section of society, and that is why the report speaks of the universality of the poem's setting."),
        T("The **Church** was the most powerful institution. Pilgrimage to a holy place such as the shrine of Thomas Becket at Canterbury was a common act of faith and also a holiday. Becket, Archbishop of Canterbury, was murdered in the cathedral in 1170 by knights loyal to King Henry II and was soon honoured as a martyr. The report names this historical allusion. The Church also appears as a target of satire: Chaucer shows members of the clergy who do not live up to their vows."),
        T("**Chivalry** was the code of the ideal knight: courage, loyalty, courtesy and service to the weak. **Courtly love** was a literary convention in which a lover serves his lady with devotion, often secretly. Both appear in the Knight's and the Squire's portraits, and are mocked when practised without sincerity. **Medieval medicine** was based on the theory of four humours (blood, phlegm, yellow bile and black bile) and on astrology, which is why Chaucer says the Doctor of Physic watched the stars for the right hour. Learning and science are named in the report as part of the background."),
        TIP("Exam link: the report says candidates who limit themselves to the General Prologue, or who only narrate vaguely, cannot perform well on the Chaucer questions in Paper 2, and the set text carries four multiple-choice questions in Paper 1. Learn the background in this lesson and be ready to use it in essays and in the Paper 1 multiple-choice questions on the set text."),
        MISTAKE("Pronouncing Middle English like modern English", "If you read 'knight' as 'night' you may miss a rhyme or a beat. When you cannot see why a line does not scan, check final -e and old pronunciation. In an exam you will not be asked to pronounce, but scansion questions depend on it."),
        MISTAKE("Saying Chaucer was a pilgrim in the book", "Chaucer the poet and Chaucer the pilgrim-narrator are different. The narrator pretends to be simple and admiring. Write 'the narrator' for the voice in the poem."),
        MISTAKE("Treating the background as a list", "'Feudalism, chivalry, religion' as a list earns little. For each, name a pilgrim or an episode and say what it shows about the medieval world."),
        QUIZ("What does 'hath perced' mean in 'The droghte of March hath perced to the roote'?", [
            "will pierce", "has pierced", "had been pierced", "is piercing"], 1,
            "Hath is the old form of 'has', and perced is the past participle 'pierced'.",
            hint="Look at the glossary for hath.",
            feedback=["The verb is not in the future tense.", "", "The structure is the present perfect, not the past perfect passive.", "The line expresses completed action, not an action in progress."]),
        QUIZ("Why do we sound the final -e in some Chaucer lines?", [
            "It was never sounded", "It is sounded when the line needs it to make ten syllables with the right beat", "It marks plural nouns", "It marks the Latin words"], 1,
            "Final -e was still pronounced in Chaucer's English; it appears as a short syllable when the metre needs it.",
            hint="Think about the ten-syllable pattern.",
            feedback=["It was sounded in Chaucer's time.", "", "Plural endings are different (-es).", "Latin words are not marked this way."]),
        PQ("Explain 'estates' and name one pilgrim from each of the first two estates.", "The estates are the three traditional groups: those who fight, those who pray, those who work. The Knight belongs to the first estate and the Monk, Prioress or Parson to the second. The third includes the Plowman. Name the pilgrim and say what the portrait shows about the estate."),
        PQ("Scan this invented line and name its metre: 'The river runs beside the road all day'.", "The river RUNS beside the ROAD all DAY would be read as: the RIV | er RUNS | be SIDE | the ROAD | all DAY, five iambs, ten syllables: iambic pentameter."),
        PQ("Give two reasons why the pilgrimage setting suits a poem about a cross-section of society.", "First, a pilgrimage was open to people of all kinds who shared the road. Second, travel placed different estates side by side and made it natural for them to talk and to tell stories, which also lets the poet contrast their characters and attitudes."),
        SUM("Chaucer (c. 1343 to 1400) wrote in London Middle English; The Canterbury Tales is unfinished.", "Use clues to read Middle English: spelling, sounds, final -e, word endings, double negatives.", "Verse is iambic pentameter in rhyming couplets (heroic couplets); two tales are in prose.", "Know feudalism, the three estates, Church and pilgrimage, Becket, chivalry, courtly love and medieval medicine.", "Use background with a specific pilgrim or episode; do not list it."),
    ],
))

# ------------------------------------------------------------------ 6. The General Prologue
PILGRIMS = """Pilgrim            Estate / group     What the portrait stresses
----------------   ----------------   ---------------------------------------------
Knight             fighters           ideal: truth, honour, courtesy, humble
Squire, Yeoman     fighters/servants  youth and love; skill and service
Prioress           clergy             refined manners, sentiment; worldly touches
Monk               clergy             hunting and fine living, not the Rule
Friar              clergy             friendly but gains money; taverns not the poor
Clerk              clergy/scholar     poor, thin, loves learning
Parson             clergy             poor but rich in goodness; practises what he preaches
Plowman            workers            honest labour, love of God and neighbour
Merchant           trade              solemn talk of profit; hides debt
Franklin           landowner          hospitality and feasting
Shipman, Miller    trade/workers      dishonest dealing; coarse, strong
Doctor of Physic   learned            learning in stars and humours; loves gold
Wife of Bath       cloth trade        five husbands, travel, confident, deaf
Reeve, Summoner    officials          cunning steward; corrupt Church-court officer
Pardoner           clergy             sells relics and pardons; false"""

LESSONS.append(lesson(
    module=M_CHAUCER, topic=T_GP,
    title="The General Prologue: frame, portraits, irony and satire",
    slug="liu1-general-prologue",
    minutes=26,
    summary="The structure and purpose of the General Prologue, the pilgrim-narrator, the main portraits and what each shows, the tools of satire (irony, hyperbole, understatement, incongruity, juxtaposition) and the praise for ideal figures, with the Board's report on how candidates went wrong.",
    objectives=[
        "Describe the frame of the General Prologue: spring, the Tabard Inn, the pilgrims and the Host's contest",
        "Analyse a portrait for what it shows and how it is written",
        "Name and illustrate the tools of satire and the targets Chaucer criticises and praises",
        "Plan an essay on the General Prologue using at least four examples and the critical perspective",
    ],
    key_concepts=["Frame narrative", "Pilgrim-narrator", "Estates satire", "Irony", "Hyperbole", "Incongruity", "Juxtaposition", "Verisimilitude", "Ideal figure"],
    blocks=[
        H("Introduction"),
        T("Think of a Cameroonian motor park at the start of a long journey, where traders, a priest, a student, a driver, a doctor and a market woman are all sitting together waiting for the bus to fill. In the General Prologue, Chaucer does the same with English medieval society. He puts about thirty people in an inn in Southwark (south of London) on an April evening, all about to leave for Canterbury, and he describes them one by one."),
        T("According to the Board's 2023 report, Chaucer questions were set on allusion, on Chaucer as a social critic and on techniques that give the poem a believable, universal setting. They did not go well: candidates used vague narration, limited themselves to the General Prologue, or could name no tool of satire. This lesson gives you the content and the tools."),
        T(OWNCOPY),
        H("The frame"),
        D("A **frame narrative** is a story that contains other stories. In The Canterbury Tales the frame is the pilgrimage: the General Prologue sets it up, the links between the tales continue it, and each pilgrim's tale is told inside it.", title="Frame narrative"),
        KEY("The General Prologue in four movements", "Know them in order.", cards=[
            ["1 Spring and pilgrimage", "The opening picture of April rain, the west wind (Zephyrus, a classical allusion), growth and birdsong. People long to go on pilgrimage, especially to the shrine of Thomas Becket at Canterbury."],
            ["2 The Tabard Inn", "The narrator stays at the Tabard, meets a company of about thirty, and promises to describe them in the order of their rank and kind."],
            ["3 The portraits", "A series of descriptions, from the Knight to the Pardoner, mixing ideal figures with figures who fall short."],
            ["4 The Host and the contest", "The innkeeper, Harry Bailly, proposes a storytelling game on the road, with a supper at the others' cost as the prize for the best tale, and offers himself as judge and guide."],
        ]),
        T("The narrator calls himself one of the company, and speaks as an admiring, rather simple observer who agrees with everything he sees. This is the **pilgrim-narrator**, a mask the poet wears. The gap between what the narrator says and what the details show is the main source of **irony**."),
        H("Portraits and what they show"),
        CODE(PILGRIMS, "text", title="Main pilgrims, their group and the stress of the portrait"),
        T("Chaucer describes people in four ways: by **appearance** (clothes, face, body), by **habits and skills**, by **moral qualities** (stated or implied) and by **what they do for a living**. Appearance is a clue to character: the Pardoner's thin voice and long hair, the Wife of Bath's gap teeth and red stockings, the Miller's wart and bagpipes."),
        T("The **Knight** is the first portrait and the ideal of chivalry: brave in many battles, but gentle and humble in manner. The **Parson** is a poor priest who gives to the poor, practises what he preaches and is a model shepherd for his flock; his brother, the **Plowman**, honest and devout, is another model. These figures show that Chaucer praises as well as criticises, as the report notes."),
        T("The **Monk** loves hunting and fine horses and says the old monastic rule (the Rule of St Benet, an allusion the report names) is out of date. The **Friar** is cheerful and well liked but easy on sins when he is paid, and prefers taverns and rich people to the poor. The **Pardoner** sells pardons and false relics. The **Merchant** talks all the time about profit and hides his debts. The **Doctor of Physic** is learned in astrology and the humours and compared to great medical names such as Hippocrates (a classical allusion), but he loves gold. The **Wife of Bath** has had five husbands and travelled to many shrines."),
        H("Tools of satire"),
        D("**Satire** is writing that exposes the faults of people or institutions by making them seem ridiculous, in order to criticise and, often, to improve them. **Irony** says one thing and means another; **hyperbole** is exaggeration; **understatement** makes something seem smaller; **incongruity** puts together things that do not fit; **juxtaposition** places two things side by side so that the contrast speaks.", title="Satire and its tools"),
        IMG("alliu1-satire-chain.svg", alt="Four boxes joined by arrows: target, method, effect, aim.", caption="Figure 1. How satire works: a target, a method, an effect on the reader and an aim."),
        T("The report calls satire the heart of a question on Chaucer as a social critic and says candidates failed when they could not name its tools. It gave four areas for the answer: the **Church** (Monk, Prioress, Friar, Pardoner and others: corruption and hypocrisy), the **business world** (dishonest dealings of figures such as the Shipman and the Miller), **marriage and love** (money and not love as motive, as in the Wife of Bath) and **particular vices** such as the Franklin's excess in feasting. It also asks you to show praise: the Knight, Parson and Plowman as models. Always give the target, the method and the effect."),
        EX("Worked example 1: analysing a portrait", intro="Analyse how Chaucer presents the Monk (check the details in your copy).", steps=[
            S("What the portrait shows", text="A monk who loves hunting, fine horses and rich food, and who dismisses the old rule of his order as not worth reading."),
            S("Technique: irony", text="The narrator praises him as a manly man fit to be an abbot and says he agrees that studying in a cloister is pointless. The praise exposes the Monk's neglect of his vows."),
            S("Technique: contrast", text="His life is set against the ideal monk of the Rule of St Benet, the allusion the report names. The contrast shows the failure of the Church to keep its own standards."),
            S("Effect", text="The reader laughs at the Monk but also sees a serious fault: a church leader who lives for pleasure. This is satire with a moral aim."),
        ]),
        EX("Worked example 2: a PEEL paragraph on the Church", intro="Write a paragraph for: 'Chaucer is a critic of the Church in the General Prologue. Discuss.'", steps=[
            S("Point", text="Chaucer uses the portraits of several clergy to show corruption and worldliness in the Church."),
            S("Evidence (at least two)", text="The Monk who loves hunting; the Friar who gives easy penance for gifts; the Pardoner who sells false relics (check each in your copy)."),
            S("Explain", text="In each case the narrator speaks with approval, but the facts say the opposite. This irony makes the reader see what the narrator pretends not to see."),
            S("Link", text="This is balanced by the Parson, who shows what a priest should be, so the target is bad priests, not the Church itself."),
        ]),
        H("Verisimilitude and universality"),
        T("For the old-syllabus questions the report mentions, two ideas matter. **Verisimilitude** (the appearance of truth) comes from real places (Southwark, Canterbury), concrete detail, direct description of dress, speech and habits, a believable narrator and a clear time (April). **Universality** means that the poem's setting and people speak beyond fourteenth-century England: the pilgrims are types that exist in every society, such as the hypocrite, the cheat and the honest worker. These are the 'contrasting types' the report expects to see discussed."),
        TIP("Exam link: General Prologue questions appear in Paper 2 (Section C, poetry), where the report says candidates were weak on allusion and satire, and in the Paper 1 text-based multiple-choice questions. Always use evidence from at least four portraits and, when your prescribed tale is on the syllabus, from the tale too."),
        MISTAKE("Limiting the answer to the General Prologue", "The report says this was the most common weakness in the 2023 Chaucer answers. Where a question names both texts, use both."),
        MISTAKE("Vague narration of pilgrims", "Writing a few lines about each pilgrim without a point about satire, praise or technique is narration. Group the pilgrims under points and give each point a target, a method and an effect."),
        MISTAKE("Repeating the same illustration", "The report warns that repeating similar illustrations for different points does not score. Choose different pilgrims for different points."),
        QUIZ("The narrator praises the Monk as a manly man fit to be an abbot and agrees that studying is pointless. This is mainly an example of", [
            "hyperbole", "irony", "personification", "alliteration"], 1,
            "The narrator's praise means the opposite of what the facts suggest: this is irony.",
            hint="Does the praise fit the Monk's real behaviour?",
            feedback=["There is no exaggeration meant to amuse; the point is the gap between praise and fact.", "", "No object is given human qualities.", "This is not about repeated sounds."]),
        QUIZ("Which pair gives two of the ideal figures Chaucer praises?", [
            "Monk and Friar", "Knight and Parson", "Pardoner and Summoner", "Miller and Reeve"], 1,
            "The Knight (chivalry) and the Parson (a true shepherd of his flock) are model figures.",
            hint="Which pilgrims are shown without any irony?",
            feedback=["Both are shown as falling short of their vows.", "", "Both are shown as corrupt.", "Both are shown as rough or dishonest."]),
        PQ("Name three tools of satire and give one example of each from the General Prologue.", "For instance: irony (the narrator praises the Monk's fine living), hyperbole (the Doctor's exaggerated learning and rank, compared to great medical names), incongruity (the Prioress's tender manners combined with worldly interests; the Merchant's solemn tone about profit). Use examples checked in your copy."),
        PQ("Plan an essay: 'Chaucer both criticises and praises his contemporaries in the General Prologue. Discuss.'", "Thesis: Chaucer criticises vice in several estates but also offers models. Point 1: the Church (Monk, Friar, Pardoner) with method and effect. Point 2: business and law (Merchant, Shipman). Point 3: marriage and love (Wife of Bath). Point 4: the models (Knight, Parson, Plowman). Evaluation: the praise makes the satire purposeful, not merely mocking."),
        PQ("Explain verisimilitude and give two ways Chaucer creates it.", "Verisimilitude is the appearance of truth. Chaucer uses concrete details of dress, appearance and habit (the Wife of Bath's gap teeth and hat), real places (the Tabard Inn, Southwark, Canterbury) and a believable narrator who speaks as an ordinary pilgrim."),
        SUM("The General Prologue is the frame: spring, the Tabard Inn, about thirty pilgrims and the Host's contest.", "Portraits mix praise (Knight, Parson, Plowman) with satire (Monk, Friar, Pardoner, Merchant, Doctor).", "Satire needs a target, a method (irony, hyperbole, incongruity, juxtaposition) and an effect.", "Verisimilitude and universality make the pilgrims real and typical.", "Use evidence from many portraits, and from the tale too, and never narrate without a point."),
    ],
))

# ------------------------------------------------------------------ 7. The prescribed tale
MERCH_PLOT = """Stage                      What happens (outline: check your copy)
-------------------------  ------------------------------------------------------
Prologue                   The Merchant complains that his own marriage is unhappy
January decides to marry   An elderly knight of Pavia wants a young, obedient wife
Two counsellors            Placebo flatters him; Justinus warns him (cites Seneca)
The marriage               He marries young May; Damian, a squire, loves her
The garden                 He builds a walled garden and keeps the key
Blindness                  January goes blind and clings to May
The pear tree              May and Damian meet in a pear tree
Pluto and Proserpina       The gods watch; Pluto restores his sight
May's answer               Proserpina gives May a quick excuse; January believes her"""

FRANK_PLOT = """Stage                      What happens (outline: check your copy)
-------------------------  ------------------------------------------------------
Marriage on equal terms    Dorigen and Arveragus marry in Brittany
Arveragus goes away        He leaves for England; Dorigen fears the coastal rocks
Aurelius                   A young squire loves her; she makes a rash promise
The magician               A clerk of Orleans makes the rocks seem to vanish
Dorigen's trouble          She is bound to keep her word; Arveragus returns
Generosity                 Arveragus, Aurelius and the clerk each act generously
The Franklin's question    Which of them was the most generous?"""

LESSONS.append(lesson(
    module=M_CHAUCER, topic=T_TALE,
    title="The prescribed tale: Prologue, plot, themes and allusion (Merchant's or Franklin's)",
    slug="liu1-prescribed-tale",
    minutes=26,
    summary="How to study the prescribed Chaucer tale: the Board's 2023 report names the Merchant's Prologue and Tale (new syllabus) and the Franklin's Prologue and Tale (old syllabus). Outline, themes, allusions and satire for both, with a framework to adapt to your own copy.",
    objectives=[
        "State which tales the Board's 2023 report names, and check which one your school teaches",
        "Give a reliable outline of the Merchant's Tale and of the Franklin's Tale",
        "Identify the main themes, allusions and techniques in the tale you study",
        "Link the tale to the General Prologue in an essay, as the report requires",
    ],
    key_concepts=["Tale and teller", "Fabliau and romance", "Marriage theme", "Allusion", "Irony", "Trouthe and gentilesse", "Link between tale and Prologue"],
    blocks=[
        H("Introduction"),
        T("A Canterbury tale is told by a person, and the tale is partly a portrait of that person. When the Merchant tells his tale, we hear a man who is unhappy in marriage. When the Franklin tells his, we hear a country gentleman who loves hospitality and fair dealing. So you must always ask two questions: what happens in the tale, and what does the telling show about the teller?"),
        T("The Board's 2023 report names two prescribed tales: the **General Prologue with the Merchant's Prologue and Tale** (for the new syllabus) and the **General Prologue with the Franklin's Prologue and Tale** (for the old syllabus). **Check which one your school teaches.** The outlines below are for both, so you can use the right one. Because details differ between editions and classroom notes, check every fact against your own copy."),
        T(OWNCOPY),
        H("The Merchant's Prologue and Tale: outline"),
        CODE(MERCH_PLOT, "text", title="The Merchant's Tale in nine stages"),
        T("**Prologue.** The Merchant, after the Clerk's tale about a patient wife, says he has been married for only a short time and that his wife is a terrible shrew. This sets the bitter tone of the tale. **Tale.** January, an old and wealthy knight of Pavia in Lombardy, has lived for pleasure and now wishes to marry, believing that marriage is a state of happiness. He asks advice from two friends. Placebo flatters him, as his name suggests. Justinus warns that he may be making a mistake and uses an allusion to the Roman writer Seneca to say that marriage should not be taken lightly. January marries the young May. Damian, his squire, falls in love with May and sends her a letter. January builds a walled garden and keeps the only key. Then he goes blind, and clings even more to May. Damian and May use the garden to meet and, with May standing on January's back, climb into a pear tree. In the garden Pluto, king of the fairies, and his queen Proserpina see it all. Pluto restores January's sight just as the pair are together in the tree. Proserpina gives May an answer so quick that January accepts it and believes her. The Merchant ends on a bitterly ironic note."),
        H("The Franklin's Prologue and Tale: outline"),
        CODE(FRANK_PLOT, "text", title="The Franklin's Tale in seven stages"),
        T("**Prologue.** The Franklin, who has just heard the Squire's tale, politely praises the Squire's gifts and says he cannot match such fine speech. **Tale.** In Brittany, the knight Arveragus and the lady Dorigen marry after he promises to honour her freely and she promises to be a true and humble wife; their agreement is a picture of marriage based on trust. When Arveragus goes to England to win honour, Dorigen waits in sorrow and fears the dangerous black rocks along the coast. A squire, Aurelius, who loves her, hears her speak of the rocks. Half in jest she promises to love him if he removes them. With the help of a clerk who works illusions, Aurelius makes the rocks seem to vanish. Dorigen, in despair, confesses to Arveragus, who tells her she must keep her word, though it breaks his heart. Aurelius, moved by this nobility, releases her from her promise. The clerk, seeing this, releases Aurelius from his debt. The Franklin ends by asking his hearers which of the three acted most generously."),
        H("Themes, allusion and techniques"),
        KEY("What to track in the tale you study", "Use the same questions for either tale.", cards=[
            ["Marriage and love", "What does the tale say about the true basis of marriage: money, lust, trust, freedom? Compare with the Wife of Bath's presence in the Prologue."],
            ["Appearance and reality", "Merchant: January's blindness is literal and moral; May's excuse; the garden as a false paradise. Franklin: the rocks that only seem to vanish."],
            ["Satire and irony", "Merchant: January's self-deception, the praise of marriage that the story contradicts, the pear tree. Franklin: gentle irony about the Franklin's own taste for rhetoric and fine manners."],
            ["Allusion", "Classical, biblical, historical and literary references, each with an effect on meaning."],
            ["Gender", "How are women treated and described? How do men use proverbs, authorities and power? Who speaks for women?"],
        ]),
        T("The report lists the allusions that the best candidates found in the Merchant's tale and the General Prologue together. In the General Prologue: Zephyrus (classical, hope and spring), Thomas Becket (historical, the pilgrimage's goal), the Rule of St Benet (a literary or religious text, the Monk's failure) and Rufus and Hippocrates (classical, the Doctor's learning, hyperbole). In the Merchant's Tale: Pluto and Proserpina (classical myth, with the Rape of Proserpina as the background to judges who are not neutral); Solomon (biblical wisdom, used by Pluto to say that there is no good woman); Judith (a biblical woman who helped her people, cited as an example of a good woman, which answers the claim that none exists; check in your copy who speaks); Seneca, cited by Justinus (a classical authority warning about marriage). The report asks candidates to explore any four, to explain each and to say what each adds to the poem."),
        EX("Worked example 1: a question on allusion (Merchant's Tale)", intro="Question (written for practice): 'Discuss Chaucer's use of allusion in the General Prologue and the Merchant's Tale.' Plan the answer using the types the report lists.", steps=[
            S("Thesis", text="Chaucer uses classical, biblical, historical and literary allusion to give depth, irony and authority to his satire."),
            S("Classical", text="Zephyrus in the opening gives hope and spring; Pluto and Proserpina in the garden bring myth into the comic scene and ironise the idea of fair judges."),
            S("Biblical", text="Solomon is used by Pluto to condemn women; Judith is cited as an example of a good woman (check who speaks in your copy). The two references set up a debate and show Pluto's patriarchal bias."),
            S("Historical and literary", text="Becket gives the pilgrimage its purpose; the Rule of St Benet exposes the Monk."),
            S("Effectiveness", text="Each allusion adds irony, character or theme, which is what the question asks for."),
        ]),
        EX("Worked example 2: a PEEL paragraph on marriage in the Franklin's Tale", intro="Write a paragraph for: 'The Franklin's Tale presents trust as the basis of a good marriage.'", steps=[
            S("Point", text="Chaucer presents trust and freedom as the foundation of the marriage of Dorigen and Arveragus."),
            S("Evidence", text="They agree to a marriage without lordship over each other, and when Dorigen confesses, Arveragus tells her she must keep her word even though it hurts him (check the exact lines in your copy)."),
            S("Explain", text="Arveragus puts trouthe (loyalty to one's word) above his own pride, which suggests that a marriage rests on honour, not on control."),
            S("Link", text="This contrasts with the Merchant's marriage of January and May, which rests on possession and deceit."),
        ]),
        H("Linking the tale to the General Prologue"),
        T("The report says candidates who limit themselves to the General Prologue cannot succeed, and that good answers drew examples from both texts. Make four links before the exam: the **teller** (how the Merchant's or Franklin's portrait fits his tale), the **theme** (marriage, authority, honour), the **technique** (irony, allusion, satire) and the **target** (the Church, business, marriage, vice). If your question names both texts, use at least two examples from each."),
        TIP("Exam link: the Chaucer questions in Paper 2 (Section C, poetry), the Paper 1 multiple-choice questions on the set text (four per text, according to the report) and Paper 3 context-style tasks if your school's text is set there. Write down at least four allusions, four examples of satire and four examples of marriage, each with line or section references from your copy."),
        MISTAKE("Mixing up the tales", "The Merchant's Tale (January, May, Damian, pear tree) and the Franklin's Tale (Dorigen, Arveragus, Aurelius, rocks) are different. Make sure you study the tale your school teaches and do not use the other's events as evidence."),
        MISTAKE("Retelling the plot", "Even the best outline does not answer a question. Write about what the events show, and use them as evidence."),
        MISTAKE("Forgetting the teller", "The tale reveals the teller. A good paragraph can show how the Merchant's bitterness shapes the portrait of January, or how the Franklin's values shape the theme of generosity."),
        QUIZ("In the Merchant's Tale, who restores January's sight?", [
            "Damian", "Pluto", "Justinus", "The Host"], 1,
            "Pluto, king of the fairies, restores January's sight; Proserpina then helps May with her excuse.",
            hint="Think of the gods who watch the garden.",
            feedback=["Damian is May's lover.", "", "Justinus is January's cautious counsellor.", "The Host is the guide of the pilgrimage, not a character in the tale."]),
        QUIZ("In the Franklin's Tale, what does Dorigen promise Aurelius?", [
            "To pay him gold", "To love him if he removes the rocks", "To leave her husband", "To go to England"], 1,
            "She says, half in jest, that she will love him if he makes the rocks vanish; the promise then binds her.",
            hint="The promise is tied to the dangerous rocks.",
            feedback=["She promises love, not money.", "", "She does not offer to leave her husband.", "Her husband goes to England, not she."]),
        PQ("State which tales the Board's 2023 report names and say how you would check which applies to you.", "The report names the Merchant's Prologue and Tale (new syllabus) and the Franklin's Prologue and Tale (old syllabus), each studied with the General Prologue. Check with your teacher and the school's syllabus and your edition which one applies to you."),
        PQ("Give four allusions mentioned in this lesson and say what each adds.", "Examples: Zephyrus (classical: hope and spring); Thomas Becket (historical: the pilgrimage's goal); the Rule of St Benet (literary/religious: exposes the Monk); Solomon and Judith (biblical: set up the debate about women); Pluto and Proserpina (classical: myth in the garden scene); Seneca (classical authority: warning about marriage). Choose four and give an effect for each."),
        PQ("Plan an answer: 'Compare how love and marriage are presented in the General Prologue and your prescribed tale.'", "Thesis: both show that marriage is presented as shaped by money and vanity, but the tale also asks what true marriage might be. Para 1: the Wife of Bath and other portraits in the General Prologue (love shaped by money and experience). Para 2: the tale's central couples (Merchant: January and May; Franklin: Dorigen and Arveragus). Para 3: the contrast with the models and what Chaucer suggests. Evaluation: whether Chaucer's view is serious, comic or both."),
        SUM("The report names the Merchant's Prologue and Tale (new) and the Franklin's Prologue and Tale (old): check which your school teaches.", "Know the outline of your tale in stages and the characters by name.", "Track marriage, appearance and reality, satire, allusion and gender.", "Know and explain at least four allusions with their effects.", "Always link the tale to the General Prologue and to its teller."),
    ],
))

# ------------------------------------------------------------------ 8. Metaphysical and Romantic poetry
POEM_TWO_CLOCKS = """Two Clocks (invented for this lesson, in the metaphysical manner)

Though road and river keep us far apart,
We are two clocks wound by one single hand;
Each tick of mine is echoed in your heart,
And time itself must learn to understand.
If one should stop, the other cannot run,
For clocks that share a spring must share a fate;
So when your hour is dark, I lose my sun,
And when you wake, my morning is not late."""

POEM_RAIN = """After the Rain (invented for this lesson, in the Romantic manner)

The rain has gone; each leaf is hung with light,
The red road steams beneath the climbing sun,
And one small bird I cannot name takes flight
To sing the day that has not yet begun.
I stand, and all my cares seem far and small,
As if the hills had listened and grown wise;
The earth is wide, and kind, and over all
A quiet joy is rising with the skies."""

MR_TABLE = """                 Metaphysical (c. 1600-1680)      Romantic (c. 1798-1832)
---------------  -------------------------------  ----------------------------
Main idea        wit, argument, intellect         feeling, imagination, nature
Typical themes   love, death, faith, time         nature, beauty, memory, freedom
Voice            dramatic, speaks as if arguing   personal, reflective, lyrical
Imagery          the conceit: surprising,         sensuous, natural, symbolic
                 extended comparison
Language         conversational, logical          rich and musical, from
                                                  everyday life (Wordsworth)
Examples         Donne, Herbert, Marvell          Wordsworth, Coleridge, Keats"""

LESSONS.append(lesson(
    module=M_CHAUCER, topic=T_MR,
    title="Metaphysical and Romantic poetry: wit, feeling, imagery and form",
    slug="liu1-metaphysical-romantic",
    minutes=26,
    summary="What Metaphysical and Romantic poetry are, how to recognise their features (the conceit, argument, nature, imagination, symbolism, the ode), a note on Pope and Keats from the Board's report, and a method for reading both kinds of poem with two original practice poems.",
    objectives=[
        "Define Metaphysical and Romantic poetry and list the features of each",
        "Identify a conceit and explain how it argues an idea",
        "Explain Romantic features: nature, imagination, emotion, sensuous imagery and symbol",
        "Analyse a poem for theme, imagery, sound and form, and write about its effectiveness",
    ],
    key_concepts=["Metaphysical poetry", "Conceit", "Paradox", "Romanticism", "Imagination", "Symbol", "Ode", "Sensuous imagery", "Mock-epic"],
    blocks=[
        H("Introduction"),
        T("Poetry is a conversation across centuries. A Cameroonian student reading a poem written in 1600 and another written in 1819 is meeting two different ways of thinking: one that loves a clever argument, and one that trusts feeling and nature. Knowing the period helps you explain why a poem sounds the way it does."),
        T("The blueprint for this module names Metaphysical, Romantic, Victorian and Modernist poetry, and your school will teach a selection. The Board's 2023 report names, in its poetry section, Alexander Pope's The Rape of the Lock and John Keats's Selected Poems. **Use your own copy and your teacher's list of poems.** This lesson gives the method and the features, and uses short poems written for this lesson (not by any poet on the syllabus)."),
        T(OWNCOPY),
        IMG("alliu1-periods.svg", alt="A timeline from 1300 to 1950 with bars for Chaucer, Metaphysical, Romantic, Victorian and Modernist periods.", caption="Figure 1. Approximate periods of the poetry in this module."),
        H("Metaphysical poetry"),
        D("**Metaphysical poetry** is the work of a group of seventeenth-century English poets, notably John Donne, George Herbert and Andrew Marvell, who joined intellect and emotion. The name was applied later by critics, among them John Dryden and Samuel Johnson, who thought their comparisons strained and learned.", title="Metaphysical poetry"),
        KEY("Main features", "Look for these in a poem from the seventeenth century.", cards=[
            ["The conceit", "An extended, surprising comparison between two very different things, worked out in detail like an argument. It is the signature of the style."],
            ["Argument and logic", "The poem reasons: 'if... then...', 'therefore'. The speaker tries to persuade a lover, God or the reader."],
            ["Dramatic voice", "Poems often open abruptly and speak in a natural, conversational tone, as if in mid-conversation."],
            ["Paradox and wit", "Statements that seem to contradict themselves but contain a truth; intellectual play."],
            ["Themes", "Love, death, religious faith, time, the soul and the body."],
        ]),
        CODE(POEM_TWO_CLOCKS, "text", title="An invented poem for analysis"),
        EX("Worked example 1: analysing 'Two Clocks'", intro="Analyse the poem as a metaphysical-style poem: theme, conceit, argument, form and effect.", steps=[
            S("Theme", text="The bond between two lovers who are separated by distance."),
            S("Conceit", text="The lovers are two clocks wound by one hand. A clock is mechanical and exact, yet it stands for the lovers' feeling. The unusual comparison makes love seem both precise and unbreakable."),
            S("Argument", text="Stanza 2 reasons: if clocks share one spring they share one fate, so what happens to one happens to the other. 'If... then...' is typical of metaphysical reasoning."),
            S("Form", text="Two quatrains in iambic pentameter, rhyming abab cdcd (apart, hand, heart, understand; run, fate, sun, late). The regular rhyme supports the steady ticking of the clock image."),
            S("Effect", text="The poem persuades by wit rather than by direct emotion, and the final line returns to the clock image, giving a sense of order and completeness."),
        ]),
        H("Romantic poetry"),
        D("**Romanticism** was a movement in literature and the arts in Europe, strong in English poetry from about 1798 (the publication of Wordsworth and Coleridge's Lyrical Ballads) to about 1830. It valued feeling, imagination, the individual and nature over reason, order and tradition. Major English Romantic poets are Wordsworth, Coleridge, Byron, Shelley and Keats.", title="Romanticism"),
        KEY("Main features", "Keats, named in the Board's report, is a Romantic poet; use these features for him.", cards=[
            ["Nature", "Nature is a source of beauty, healing and truth, and often a mirror of the poet's mood."],
            ["Imagination and emotion", "The poet trusts the imagination, and poems begin in strong feeling. Wordsworth called poetry an overflow of powerful feeling."],
            ["The individual", "The speaker is often a thoughtful, lonely person; poems explore the self and its changes."],
            ["Sensuous imagery", "Rich appeal to the five senses: Keats is known for taste, touch, scent and sound in his images."],
            ["Symbol and myth", "Objects stand for larger ideas: the nightingale for immortal song, the urn for art that outlasts time (check your selection for the poems you study)."],
            ["Mortality and beauty", "Joy and sadness are close: beauty is made more precious by the knowledge that it fades."],
        ]),
        T("Keats (1795 to 1821) died young. His best-known poems include odes such as 'Ode to a Nightingale', 'Ode on a Grecian Urn' and 'To Autumn', and a sonnet whose first line says that the poetry of earth is never dead ('On the Grasshopper and Cricket'). An **ode** is a long lyric poem in a high, serious style addressed to a person or thing. The Board's 2023 report names two ideas for the Keats questions: that **symbolism** is a hallmark of his poetry, and that the poetry of earth never dies. For the first, show how he uses symbols at the level of objects, characters and setting; for the second, show how nature's life keeps going and comforts the speaker. Use any three poems from your selection and ground every point in them."),
        CODE(POEM_RAIN, "text", title="A second invented poem for analysis"),
        EX("Worked example 2: analysing 'After the Rain'", intro="Analyse the poem as a Romantic-style poem.", steps=[
            S("Theme", text="Joy and renewal in nature after rain; the calming of the speaker's cares."),
            S("Imagery (senses)", text="'Each leaf is hung with light' (sight), 'the red road steams' (sight and touch of warmth), a bird's singing (sound). The images are sensuous and concrete."),
            S("Nature and feeling", text="The speaker's mood changes with the landscape: from cares to quiet joy. This is the Romantic pattern of nature healing the mind."),
            S("Symbol", text="The rain's end and the new day can be read as a symbol of renewal; the unnamed bird may suggest song that is greater than the speaker."),
            S("Form", text="Two quatrains of iambic pentameter, rhyming abab cdcd, with a movement from description (stanza 1) to reflection (stanza 2). That turn is a typical Romantic shape."),
        ]),
        H("A word on Pope"),
        T("Alexander Pope (1688 to 1744) belongs to the earlier eighteenth century, the age of order and wit, which Romantic writers later reacted against. The Rape of the Lock is a **mock-epic**: it tells a trivial event (a young man cuts a lock of a lady's hair) in the grand style of epic poetry, with heroic couplets, supernatural helpers and a descent into a cave of spleen, to laugh at the vanity of fashionable society. The report mentions the descent into the cave of spleen as a journey episode. Contrast: Pope uses wit, balance and satire; Keats uses feeling, imagery and symbol."),
        CODE(MR_TABLE, "text", title="Metaphysical and Romantic poetry compared"),
        TIP("Exam link: poetry set texts in Paper 2 (Section C), four multiple-choice questions per set text in Paper 1, and unseen poetry in Paper 3. The report asks for a critical perspective: say what each device achieves, not only that it exists."),
        MISTAKE("Naming a conceit without working it out", "Saying 'the poet uses a conceit' earns little. State the two things compared, the points of similarity the poet develops, and what the comparison makes you feel or believe."),
        MISTAKE("Calling every nature poem Romantic", "A poem is Romantic when nature is linked to feeling, imagination or the self. A list of nature images alone is not enough."),
        MISTAKE("Using only one poem when three are asked for", "The report's Keats questions asked for any three poems. Check how many poems the question wants, and use each with evidence."),
        QUIZ("A comparison between two very different things, developed at length like an argument, is a", [
            "simile", "conceit", "sonnet", "refrain"], 1,
            "A conceit is an extended, surprising comparison; it is the typical device of metaphysical poetry.",
            hint="Which term describes an extended, clever comparison?",
            feedback=["A simile is a short comparison with like or as; a conceit is extended and worked out.", "", "A sonnet is a form of fourteen lines.", "A refrain is a repeated line."]),
        QUIZ("Which feature is most typical of Romantic poetry?", [
            "A strict logical argument", "The link between nature, feeling and imagination", "The mock-epic style", "A formal address to the king"], 1,
            "Romantic poets show nature, emotion and imagination working together.",
            hint="Think of Keats and nature.",
            feedback=["That is more typical of Metaphysical poetry.", "", "Mock-epic is Pope's eighteenth-century style.", "Romantic poetry is not about court or public address."]),
        PQ("Explain the conceit in 'Two Clocks' and say what it adds to the poem.", "The lovers are compared to two clocks wound by one hand. It adds precision and exactness to love and gives the idea that their lives are linked even when they are apart; the comparison also supports the poem's argument that they share one fate."),
        PQ("Give three features of Romantic poetry and illustrate one from 'After the Rain'.", "Nature, imagination and emotion, sensuous imagery, symbol, the individual. Illustration: 'each leaf is hung with light' appeals to sight and shows nature's beauty; the speaker's cares are lifted as the landscape brightens, linking nature and feeling."),
        PQ("Plan a paragraph on symbolism in poems from a Keats selection (use placeholders).", "Point: Keats uses [object, character or setting] as a symbol of [idea]. Evidence: [poem title and a short phrase from your copy]. Explain: what the symbol suggests, and how it connects with the poem's theme. Link: the symbol shows [Romantic idea: beauty, mortality, imagination]. Repeat with two more poems."),
        SUM("Metaphysical poetry uses wit, argument, dramatic voice, paradox and the conceit.", "Romantic poetry values nature, feeling, imagination, sensuous imagery and symbol.", "Keats: odes, symbol, beauty and mortality; Pope: mock-epic wit in heroic couplets.", "Analyse theme, imagery, sound and form, and say what each achieves.", "Use the poems in your own selection and the number of poems the question asks for."),
    ],
))

# ------------------------------------------------------------------ 9. Victorian and Modernist poetry
POEM_STATION = """The Station-Master (invented for this lesson, in the Victorian manner)

You ask me, sir, why I still keep the clock
Wound and the lamps all trimmed, when no one comes?
The railway left this valley years ago.
I keep it, as a man keeps faith, because
A place that has been loved should not go dark.
You smile. I know. The world has gone ahead
And left me with my brass and my small flame;
Yet I have never felt a poorer man
Than those who ride the fast trains and arrive."""

POEM_MARKET = """Market, Evening (invented for this lesson, in the Modernist manner)

Plastic sheets. The long light
slides off the zinc.
A radio says rain, says price, says
somewhere a war.
Someone is counting
what he cannot sell.
Tomatoes bruise.
Children carry the evening home
in empty basins."""

VM_TABLE = """                 Victorian (1837-1901)            Modernist (c. 1910-1945)
---------------  -------------------------------  -------------------------------
Context          industry, empire, science,       the First World War, cities,
                 doubt about faith                breakdown of old certainties
Form             regular metre and rhyme,         free verse, fragments, broken
                 stanzas, blank verse             syntax, irregular lines
Voice            often a clear speaker;           many voices; speaker may be
                 the dramatic monologue           uncertain or split
Method           story, argument, moral view      images side by side (juxtaposition),
                                                  allusion, hints not statements
Reader's job     follow the argument and feeling  piece the meaning together
Examples         Tennyson, Browning, Arnold,      Eliot, Pound, Yeats (later work),
                 C. Rossetti, Hopkins, Hardy      Owen (war poetry)"""

LESSONS.append(lesson(
    module=M_CHAUCER, topic=T_VM,
    title="Victorian and Modernist poetry: doubt, change, fragments and form",
    slug="liu1-victorian-modernist",
    minutes=26,
    summary="The contexts and features of Victorian and Modernist poetry (the dramatic monologue, doubt and change; free verse, fragmentation, allusion and juxtaposition), with two original poems to analyse and a method for comparing poems of different periods.",
    objectives=[
        "Describe the contexts behind Victorian and Modernist poetry",
        "Recognise a dramatic monologue and explain how it reveals a speaker",
        "Recognise free verse, fragmentation, allusion and juxtaposition and say what they achieve",
        "Compare a Victorian and a Modernist poem for theme, form and effect",
    ],
    key_concepts=["Victorian poetry", "Dramatic monologue", "Blank verse", "Modernism", "Free verse", "Fragmentation", "Juxtaposition", "Allusion"],
    blocks=[
        H("Introduction"),
        T("Compare two ways of telling someone you are lost. One person says, calmly and in order, 'I have taken the wrong road, and I regret it.' Another says only: 'Dust. Road. A sign with no name. No one.' Both give the same message, but the second makes the reader piece it together. The first is typical of Victorian poetry, the second of Modernist poetry."),
        T("Your school may study poems from these periods, and unseen poems in Paper 3 may come from any period. The Board's 2023 report names poets in other sections of its poetry paper, so use your own list. This lesson teaches the periods, the features and a method, with two poems written for this lesson."),
        T(OWNCOPY),
        H("Victorian poetry (1837 to 1901)"),
        T("Queen Victoria reigned from 1837 to 1901. Britain became an industrial and imperial power, with railways, factories, growing cities and an empire that included parts of Africa. Science gave new confidence but also doubt: Charles Darwin's On the Origin of Species (1859) challenged older beliefs about creation, and many writers wrote about a loss of religious certainty. Social questions such as poverty, women's roles and the cost of progress also fill the poetry."),
        D("A **dramatic monologue** is a poem in which one speaker, who is not the poet, addresses a silent listener, and reveals his or her character, often without intending to. Robert Browning is its best-known Victorian master.", title="Dramatic monologue"),
        KEY("Main features of Victorian poetry", "Check which of these appear in the poems you study.", cards=[
            ["Regular form", "Metre, rhyme and stanza patterns; also blank verse (unrhymed iambic pentameter)."],
            ["Moral and social concern", "Poems ask what duty, progress, love and faith mean in a changing world."],
            ["Doubt and loss", "Tennyson's elegy In Memoriam and Matthew Arnold's 'Dover Beach' are well-known poems of grief and lost faith."],
            ["The dramatic monologue", "A speaker reveals himself or herself to a listener; the reader sees more than the speaker does."],
            ["Music and imagery", "Rich sound effects, as in Tennyson; unusual rhythm and strong word-music in Gerard Manley Hopkins."],
        ]),
        CODE(POEM_STATION, "text", title="An invented poem for analysis"),
        EX("Worked example 1: 'The Station-Master' as a dramatic monologue", intro="Analyse the poem's speaker, theme, form and effect.", steps=[
            S("Speaker and listener", text="A railway station-master speaks to a visitor ('You ask me, sir'). The listener is silent, but we sense his smile: 'You smile. I know.'"),
            S("What the speaker reveals", text="He is loyal, proud and lonely. He keeps the lamps trimmed though no trains come. The poem shows his character through what he chooses to say."),
            S("Theme", text="Faithfulness to a place and a duty against the pressure of progress; the railway has left, and he has not."),
            S("Form", text="Blank verse: unrhymed lines of ten syllables, five iambs. It sounds like natural speech but with dignity, which suits a speaker who is humble yet proud."),
            S("Effect and irony", text="He says he is not poorer than those who 'arrive'. The reader senses both his pride and his loneliness, and may question whether he is right. This is the dramatic monologue's gap between what the speaker says and what the reader understands."),
        ]),
        H("Modernist poetry (about 1910 to 1945)"),
        D("**Modernism** was a movement in the arts that broke with traditional forms to express a changed world. In poetry it is linked with T. S. Eliot (The Waste Land, 1922; 'The Love Song of J. Alfred Prufrock'), Ezra Pound and others, and with the shock of the First World War (1914 to 1918), growing cities and the loss of older certainties.", title="Modernism"),
        KEY("Main features of Modernist poetry", "Learn the terms and what each does.", cards=[
            ["Free verse", "No fixed metre or rhyme; the line break and rhythm are shaped by meaning."],
            ["Fragmentation", "Broken syntax, abrupt shifts and gaps. The form mirrors a broken world."],
            ["Juxtaposition", "Images or voices placed side by side without explanation; the reader supplies the link."],
            ["Allusion", "Quiet references to myth, literature and religion, sometimes in other languages, adding depth and irony."],
            ["Objective, hard images", "Concrete pictures instead of statements of feeling (Pound's Imagist ideas); a tone that can be cool or ironic."],
            ["Alienation", "A sense of isolation in modern life."],
        ]),
        T("Modernist ideas also reached African poetry. Critics often connect the work of poets such as Wole Soyinka and Christopher Okigbo with Modernist techniques of allusion and compression, though they also draw heavily on African oral tradition and myth. Check this in your textbook before using it in an essay."),
        CODE(POEM_MARKET, "text", title="A second invented poem for analysis"),
        EX("Worked example 2: 'Market, Evening' as a Modernist poem", intro="Analyse its form, images and effect.", steps=[
            S("Form", text="Free verse: short, irregular lines, no rhyme, little punctuation of the usual kind, sentences in fragments ('Plastic sheets.')."),
            S("Juxtaposition", text="The radio's news of rain, price and war is placed beside the ordinary market scene. The reader senses how distant events press on local life, with no explanation given."),
            S("Imagery", text="Concrete and cool: 'zinc', 'tomatoes bruise', 'empty basins'. The tone is flat and observing, so the sadness comes from what is left unsaid."),
            S("Theme", text="The fragility of ordinary livelihood and the weight of a world beyond one's control."),
            S("Effect", text="The poem asks the reader to complete the meaning, which is typical of Modernist writing."),
        ]),
        CODE(VM_TABLE, "text", title="Victorian and Modernist poetry compared"),
        H("Comparing poems from different periods"),
        T("Use four lenses for any comparison: **theme** (what is each poem about?), **voice** (who speaks, and how reliably?), **form and sound** (metre, rhyme, line length, free verse) and **effect** (what does the form do to the reader?). Link each point with a comparing word (whereas, in contrast, similarly). For 'The Station-Master' and 'Market, Evening': both show people facing change; the first speaks directly, with order and pride; the second implies, with fragments and silence."),
        TIP("Exam link: periods and poets appear in Paper 1 (general literary appreciation and set-text multiple-choice questions), in Paper 2 Section C essays on the poetry set texts and in the unseen poetry question of Paper 3. Practise saying what a technique does, not only what it is."),
        MISTAKE("Saying free verse has no form", "Free verse has form: line breaks, rhythm, repetition, shape on the page. Always say what the line breaks and gaps do."),
        MISTAKE("Confusing the poet and the speaker", "In a dramatic monologue, the speaker is a character. Write 'the speaker reveals...' not 'the poet is proud'."),
        MISTAKE("Dating poems carelessly", "A poem written in 1930 is not Victorian because it rhymes. Judge by features and context, and say 'typical of' rather than 'always'."),
        QUIZ("In a dramatic monologue, the speaker", [
            "is always the poet", "reveals his or her character to a silent listener", "must write in rhymed couplets", "speaks only about nature"], 1,
            "A dramatic monologue lets a character speak to a listener and reveal personality, often unintentionally.",
            hint="Think of how Browning's poems work.",
            feedback=["The speaker is usually a created character.", "", "Form varies; many use blank verse.", "Themes are not limited to nature."]),
        QUIZ("Which feature most clearly marks a Modernist poem?", [
            "Strict rhyming couplets", "A clear moral lesson at the end", "Fragments and images set side by side without explanation", "A formal address to a monarch"], 2,
            "Fragmentation and juxtaposition are typical of Modernism: the reader makes the link.",
            hint="Look for what the poem leaves unsaid.",
            feedback=["Strict couplets suggest earlier styles such as Pope's.", "Modernist poems seldom state a moral.", "", "That is not a Modernist feature."]),
        PQ("Define blank verse and say why a dramatic monologue might use it.", "Blank verse is unrhymed iambic pentameter. It sounds like natural speech but has dignity, which suits a speaker who tells his own thoughts in a serious, controlled way."),
        PQ("Give two differences between Victorian and Modernist poetry and illustrate one.", "Victorian poems usually have regular form, a clear speaker and a moral or emotional argument; Modernist poems use free verse, fragments, allusion and juxtaposition. Illustration: 'Market, Evening' places radio news beside the market scene without comment, while 'The Station-Master' states his case in full sentences."),
        PQ("Plan a comparison essay on one Victorian and one Modernist poem of your choice (placeholders).", "Introduction: name both poems and a shared idea such as change. Para 1: theme in each. Para 2: voice and form (Victorian: regular, spoken; Modernist: free verse, fragments). Para 3: imagery and effect. Para 4: evaluation, which poem engages you more and why. Always quote a few words from each and say what they do."),
        SUM("Victorian poetry reflects industry, empire, science and doubt, in regular form and often through a dramatic monologue.", "Modernist poetry breaks with form after the First World War: free verse, fragments, juxtaposition and allusion.", "A speaker in a monologue is a character, not the poet.", "Free verse has form; ask what line breaks and gaps do.", "Compare poems through theme, voice, form and effect."),
    ],
))

