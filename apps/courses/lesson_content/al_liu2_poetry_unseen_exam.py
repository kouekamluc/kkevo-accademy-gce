"""A Level Literature in English (0735), Upper Sixth: Modern African Poetry Anthology (4 lessons), Unseen Prose & Poetry Criticism (3 lessons) and Examination (Paper 1, Paper 2, Paper 3).

Facts about the examination and the set poetry text come from the Board's 2023 Advanced Level subject report (paraphrased). The report names Poems of Black Africa
as the poetry text and mentions the poems used in these lessons; poem summaries follow the report and tell students to check their own copy. Where a poem is not
described by the report, the lessons give study questions only. All unseen passages, poems, models and invented extracts are original and written for this course.
"""

from .dsl import *  # noqa: F403

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

LESSONS = []

# ------------------------------------------------------------------ 1. Reading African poetry
LESSONS.append(lesson(
    module=M_POET, topic=T_READ,
    title="Reading African poetry: background, regions and a method for any poem",
    slug="liu2-reading-african-poetry",
    minutes=24,
    summary="The Board's 2023 report names Poems of Black Africa as the poetry text; this lesson gives the historical background, the regional grouping, the poems the report mentions and a five-question method for reading any poem in the anthology.",
    objectives=[
        "Name the anthology the Board's 2023 report sets for Paper 2 poetry and say how the report describes its range",
        "Explain the background ideas the report asks teachers to teach: colonialism, assimilation, Negritude, apartheid, the African personality and neo-colonialism",
        "Use a five-question method to read a poem you have never discussed in class",
        "Avoid the faults the report lists: poor knowledge of the poems, shallow content and unfocused narration",
    ],
    key_concepts=["Poems of Black Africa", "Negritude", "Colonialism and apartheid", "Speaker and addressee", "Regional classification", "Disillusionment"],
    blocks=[
        H("Introduction"),
        T("Think of a poem that your grandmother could recite at a funeral, a poem a market woman could sing to herself while she sweeps, and a poem that a prisoner could whisper through a wall. African poetry in English has all three voices. It joins very old spoken traditions to the experience of colonial rule, independence, disappointment and hope."),
        T("The Board's 2023 subject report names **Poems of Black Africa** as the poetry text in Paper 2 for both the old and the new syllabus. The anthology was edited by the Nigerian writer Wole Soyinka. The report describes it as offering a wide range of poems from West, East and South Africa, reflecting different themes and styles that bring out African identity and personality. Check with your teacher that this is still your set text, because prescribed texts change."),
        T(OWNCOPY),
        H("What the examiners say about the anthology"),
        D("The report notes that questions on the poetry text are usually 'candidate friendly': they do not tie you to particular poems. Instead you choose the poems that fit the question. Yet performance in this section was weak. The faults it lists are: poor knowledge of the poems (clear signs that candidates had not been taught them), shallow content, vague accounts that ignored the question, and clumsy narration with no purpose.", title="The Board's comment"),
        T("Look at what that means for you. A free choice of poems is an advantage only if you know **many** poems well enough to choose among them. A student who knows two poems has no choice. Aim to know at least eight or ten poems in depth, drawn from different regions and different themes."),
        H("Background you must know"),
        T("The report asks teachers to give 'thorough background' to African literature from Lower Sixth: its history, the forms of oral tradition and how they show up in modern writing, the periods through which African literature has developed, and the themes of African poets. It lists these ideas as needed for the anthology: the African personality, colonialism, assimilation, Negritude, apartheid and neo-colonialism."),
        KEY("Six background ideas", "Use these words precisely.", cards=[
            ["Colonialism", "Rule of African lands by European powers, with its taxes, borders, languages and schools. Many poems mourn loss of land and dignity."],
            ["Assimilation", "A policy or pressure to make Africans adopt the culture and language of the colonizer. Poems criticise people who imitate foreign ways and hide their own."],
            ["Negritude", "A movement begun by French-speaking Black writers in the 1930s, among them Senghor and Cesaire, which celebrates Black cultural identity. Several poets in the anthology are linked with it."],
            ["Apartheid", "The official system of racial separation and white-minority rule in South Africa. Poems by South African poets speak of raids, prison and torture under it."],
            ["The African personality", "The idea that Africans have a distinct cultural identity and values that should be affirmed after colonial rule."],
            ["Neo-colonialism", "The view that independence in name hid continued economic and political control, or that new African rulers copied the oppression of the old masters."],
        ]),
        TIP("Check your textbook for the exact definitions your teacher uses. Negritude in particular has several meanings, and some African writers have criticised it."),
        H("The anthology by region"),
        T("The report says the poems come from West, East and South Africa and advises teachers to analyse them 'according to their regional classification', stressing the poets' backgrounds, themes and styles. Make a three-column table in your notebook: poet, country, region. The countries below are well established, but check your own copy for the regional grouping that your anthology uses."),
        CODE("Poet (as named in the Board's report)   Country (check your copy)\n"
             "Birago Diop                             Senegal\n"
             "David Diop                              Senegal\n"
             "Lenrie Peters                           The Gambia\n"
             "Mbella Sonne Dipoko                     Cameroon\n"
             "Tchicaya U Tam'si                       Congo\n"
             "J. P. Clark                             Nigeria\n"
             "Wole Soyinka                            Nigeria\n"
             "Mazisi Kunene                           South Africa\n"
             "Dennis Brutus                           South Africa\n"
             "Jared Angira                            Kenya\n"
             "Richard Ntiru                           Uganda", "text", title="Poets named in the report"),
        T("Birago Diop and David Diop are different poets, and the report stresses that candidates must identify poems with their rightful authors. Write each poem's title, poet and country on one line, and learn them together."),
        H("Poems the report mentions"),
        T("The report mentions these poems when it explains what answers were expected. The summaries are in our own words and follow the report; check them against the poems in your copy."),
        CODE("'Breath' and 'Vanity' (Birago Diop): ancestors still present; the dead are not dead.\n"
             "'To the Living' (Richard Ntiru): the dead and the living.\n"
             "'Dedication' (Wole Soyinka): speaks to the dead.\n"
             "'Pardon Me' (Ismael Hurreh): speaks to the dead.\n"
             "'The Bond' (Mazisi Kunene): a grinding stone passed on; ancestors protect.\n"
             "'Olokun' (J. P. Clark): a sea goddess whose lovers fall.\n"
             "'If' (Jared Angira): omens from animals and dreams.\n"
             "'Agony' (Tchicaya U Tam'si): a boatman, a bird and a lake of blood.\n"
             "'Rulers' and 'Upheaval' (Mbella Sonne Dipoko): bad rulers and revolt.\n"
             "'The Sounds Begin Again' and 'Cold' (Dennis Brutus): apartheid and prison.\n"
             "'The Right Road' (David Diop): traitor-leaders and false values.\n"
             "'It is time for reckoning, Africa' (Lenrie Peters).\n"
             "'My Mother who art' (Jared Angira).\n"
             "'Phlora': moral decline among young women (check the poet in your copy).", "text", title="Poems named in the report"),
        IMG("alliu2-poem-method.svg", alt="Five boxes in a row: Who speaks, To whom, About what, How, So what. Each has a short prompt beneath it.", caption="Figure 1. The five questions for reading any poem."),
        H("A five-question method for any poem"),
        D("Ask five questions in order: **Who speaks?** (the persona or speaker, which may not be the poet). **To whom?** (the addressee; a dead ancestor, a ruler, the reader, Africa itself). **About what?** (the situation and subject). **How?** (diction, imagery, sound, structure and form). **So what?** (the theme, the attitude and the effect on the reader).", title="Who, to whom, about what, how, so what"),
        T("The first three questions give meaning. The last two give criticism. A weak answer stops at 'about what'. A good answer always reaches 'how' and 'so what'."),
        EX("Worked example 1: the method applied to the Board's description of 'The Bond'", intro="The report describes Kunene's poem as follows: a grinding stone that belonged to Masilela is passed to her successor Gumede in a succession ritual, and he is warned to keep it sacred. If it is carelessly kept or defiled, the ancestor will bring curses on the living. Use the five questions on this description. (Check each point in your copy.)", steps=[
            S("Who speaks?", text="A voice of instruction and warning, speaking with the authority of a family elder."),
            S("To whom?", text="To the successor who receives the stone, here Gumede, so the poem is a kind of address to someone about to inherit a duty."),
            S("About what?", text="Inheriting and guarding a cherished object that links the living with an ancestor."),
            S("How?", text="Objects with meaning (the grinding stone) work as a symbol; the warning of curses gives the poem a solemn, ritual tone. Look in your copy for the actual words and sounds."),
            S("So what?", text="The poem presents the traditional belief that the dead are still concerned for the living and that duty to them is a moral bond. It celebrates a cultural value rather than complaining."),
        ]),
        EX("Worked example 2: choosing poems for a question", intro="A question asks you to show, from poems of your choice, that African poets are troubled by the problems of their societies. Choose and justify three poems using only the report's descriptions.", steps=[
            S("Read the focus", text="Troubled by problems means the poet criticises something in society. You need poems about social or political ills."),
            S("Choose poems from different regions", text="'Rulers' (Dipoko, Cameroon) for greedy rulers; 'Cold' (Brutus, South Africa) for the prison conditions of the apartheid era; 'Phlora' for moral decline (check the poet)."),
            S("Add a counter-point", text="The report suggests that good answers also note that these poets keep hope alive and celebrate African identity, for example in 'Olokun', 'The Bond' and 'If'. That makes the answer balanced."),
        ]),
        MISTAKE("Retelling the poem", "The report says many answers narrated poems without addressing the question. Say what the poem shows about the theme in the question, then give details from the poem as proof. A line-by-line retelling earns little."),
        MISTAKE("Confusing poets and poems", "Never give a poem to the wrong author. Keep a one-page chart of title, poet and theme and test yourself with the title covered."),
        MISTAKE("Studying only your favourite poems", "Questions allow a free choice but ask for a number of poems or a theme. If you know only two poems, you cannot choose well. Spread your revision across regions and themes."),
        QUIZ("According to the Board's 2023 report, how are questions on the poetry text usually set?", [
            "Tied to one named poem each", "Not tied to particular poems, so candidates choose relevant ones", "On unseen poems only", "On the poet's life rather than the poems"], 1,
            "The report calls them candidate friendly because they do not tie candidates to particular poems.",
            hint="Think about why a free choice helps only a student who knows many poems.",
            feedback=["The report says the opposite: questions are not tied to particular poems.", "", "Unseen poems belong to Paper 3.", "The questions are about the poems and their themes, not the poet's biography."]),
        QUIZ("In the five-question method, which question moves your answer from meaning to criticism?", [
            "Who speaks?", "To whom?", "About what?", "How, and so what?"], 3,
            "Meaning comes from who, to whom and about what. Criticism comes from how the poet does it and what effect or theme results.",
            hint="Which questions ask for technique and effect?",
            feedback=["It only identifies the voice.", "It only identifies the addressee.", "It only gives the subject.", ""]),
        PQ("Name three background ideas the Board's report says must be taught for the anthology, and say in a sentence why one of them matters for reading the poems.", "Any three of: the African personality, colonialism, assimilation, Negritude, apartheid, neo-colonialism. Example: apartheid matters because poems such as Brutus's 'Cold' and 'The Sounds Begin Again' (as the report describes them) deal with prison and police raids in South Africa, so readers who do not know the system miss the poems' anger."),
        PQ("Use the five questions on the following invented four-line poem. 'Grandfather, I hold the hoe you held, / the soil still answers when I call. / Forgive the years I said it was shame to dig, / I plant your name in every row.' (Invented for practice.)", "Who: a grandchild. To whom: the dead grandfather (apostrophe, a direct address). About what: regret for having despised farming and a decision to honour the grandfather's work. How: direct address, the image of planting a name in rows, a repeated focus on the hoe. So what: the poem suggests that respect for ancestors can be shown through work and that shame about one's roots can be reversed."),
        PQ("Explain why a student who has learned only two poems in the anthology is at a disadvantage in Paper 2, using the Board's comment.", "The report says questions are not tied to particular poems and that candidates choose. A student who knows only two poems may find that neither fits the theme or that the question asks for three poems. The report also lists poor knowledge of the poems and shallow content as the main reasons for weak answers."),
        SUM("Poems of Black Africa is the poetry text named in the Board's 2023 report for Paper 2; check that it is your current text.",
            "Learn the background ideas: colonialism, assimilation, Negritude, apartheid, the African personality and neo-colonialism.",
            "Group poems by region and keep a poem, poet, country and theme chart.",
            "Use the five questions: who speaks, to whom, about what, how, so what.",
            "Know many poems well, because questions let you choose and weak answers come from poor knowledge of the poems."),
    ],
))

# ------------------------------------------------------------------ 2. Oral tradition and poetic form
PRAISE = ("**Praise-song for a farmer** (invented for practice)\n\n"
          "Hail, Nkeng of the early hoe!\n"
          "Hail, Nkeng of the patient rows!\n"
          "Where you walk, the beans stand straight;\n"
          "Where you rest, the rain comes down.\n"
          "Nkeng of the early hoe,\n"
          "who wakes before the cocks have finished,\n"
          "hail, Nkeng of the patient rows,\n"
          "hail, and let the whole hill answer.")

LESSONS.append(lesson(
    module=M_POET, topic=T_ORAL,
    title="Oral tradition and poetic form: how spoken art shapes written African poems",
    slug="liu2-oral-tradition-poetic-form",
    minutes=23,
    summary="Oral forms such as praise poetry, the dirge, the proverb and the folktale shape African poems through repetition, call and response, direct address and speech rhythm; this lesson shows how to spot these features and explain what they do.",
    objectives=[
        "Name the main oral forms (poetic and prose) and the features they pass to written poems",
        "Identify repetition, parallelism, refrain, call and response, ideophone and apostrophe in a poem",
        "Define apostrophe as the Board's report does and say why poets use it",
        "Explain the effect of an oral technique instead of only naming it",
    ],
    key_concepts=["Oral tradition", "Praise poetry", "Dirge", "Call and response", "Repetition and parallelism", "Apostrophe", "Free verse"],
    blocks=[
        H("Introduction"),
        T("Long before African poems were printed, they were spoken, sung, drummed and danced at weddings, funerals, harvests and the courts of chiefs. The Board's 2023 report asks that teachers explain 'forms of the oral tradition and their reflections in modern African Literature'. This is not decoration. Many features of the poems in the anthology, such as repetition, direct address to the dead and a speaking rhythm, come from oral performance."),
        T("The report also says that Paper 1 tested the **types of oral prose forms**. So you need names for oral prose as well as oral poetry."),
        H("Oral forms: prose and poetry"),
        KEY("Oral prose forms", "Spoken stories that are not in verse.", cards=[
            ["Myth", "A traditional story about gods, spirits or the origin of the world and of people."],
            ["Legend", "A story about a real or supposed hero or event of the past, enlarged by retelling."],
            ["Folktale", "A story told for entertainment and teaching, often with animals or a trickster, and often ending with a lesson."],
            ["Proverb and riddle", "A proverb is a short wise saying. A riddle is a puzzle question with a hidden answer. Both are packed with images."],
        ]),
        KEY("Oral poetic forms", "Poems made to be performed.", cards=[
            ["Praise poetry (panegyric)", "Poems that celebrate a person, such as a chief or farmer, by a list of praise names and deeds, often using exaggeration."],
            ["Dirge or elegy", "A song of mourning for the dead, which may also comfort the living and speak to the ancestor."],
            ["Incantation and invocation", "Words said to call on a spirit or god, or to heal or protect."],
            ["Work songs, lullabies and satirical songs", "Songs that keep a rhythm for labour, soothe a child or criticise someone in public."],
        ]),
        TIP("Check your textbook for the names your teacher uses. Terms such as panegyric, dirge and elegy overlap, and some textbooks use different divisions."),
        H("What oral performance leaves in a written poem"),
        T("A performer needs the audience to follow and remember without a page. So oral poems repeat sounds, words and shapes, and they speak to someone. Printed poems that borrow these habits often sound like speech."),
        D("**Repetition** is the return of a word, phrase or line. **Parallelism** is repeating a sentence shape with new content, such as 'Where you walk... Where you rest...'. A **refrain** is a line or phrase repeated at intervals. **Call and response** is a pattern in which a leader's line is answered by a chorus or audience. An **ideophone** is a word that suggests a sound, movement or sight, close to onomatopoeia.", title="Oral features"),
        D("**Apostrophe** is a device in which a speaker suddenly addresses an absent, abstract or dead person, or an object, as if present. Poets use it for emotional effect. The Board's report names apostrophe among the devices for the anthology and mentions Birago Diop's 'Vanity', Wole Soyinka's 'Dedication', Ismael Hurreh's 'Pardon Me', Mbella Sonne Dipoko's 'Rulers', Lenrie Peters's 'It is time for reckoning, Africa' and Jared Angira's 'My Mother who art' as poems where it appears. Check each in your copy.", title="Apostrophe (the report's definition)"),
        IMG("alliu2-oral-features.svg", alt="A central box 'Oral performance' with four arrows to Repetition and refrain, Call and response, Direct address, and Speech rhythm, each with a short effect line.", caption="Figure 1. Oral habits and their effects in a written poem."),
        H("Reading oral features: a worked example"),
        T(PRAISE),
        EX("Worked example 1: identify and explain", intro="List four oral features in the praise-song above and say what each does.", steps=[
            S("Repetition and epithets", text="'Nkeng of the early hoe' and 'Nkeng of the patient rows' repeat the name with a praise title. This is how praise poetry builds up a portrait: each title adds a quality (early rising, patience)."),
            S("Parallelism", text="'Where you walk, the beans stand straight; where you rest, the rain comes down.' The matching shapes make the lines easy to remember and suggest that the whole world answers to the farmer."),
            S("Hyperbole", text="The rain comes down when he rests. Praise poetry exaggerates to show high honour."),
            S("Call and response and direct address", text="'Hail' is a call. 'Let the whole hill answer' invites a chorus reply, so the poem asks the audience to take part."),
        ]),
        EX("Worked example 2: effect of apostrophe", intro="A speaker says to his dead grandmother, 'Grandmother, you are not under this mound.' (Invented for practice.) Explain the effect of the apostrophe.", steps=[
            S("Name it", text="The speaker addresses the dead grandmother directly. This is apostrophe."),
            S("Show the feeling", text="Speaking to her as if she could hear shows love and denies that death has ended the relationship."),
            S("Connect to the theme", text="It supports the belief, reflected in poems the report mentions, that the dead are not dead. Apostrophe lets the poem act out that belief, because the living speak and the dead are treated as listeners."),
        ]),
        H("Form and shape: free verse and regular patterns"),
        T("Many modern African poems are in **free verse**: lines of different lengths with no fixed rhyme or metre, shaped by the speaker's breath and meaning. This echoes the way speech and chant are shaped. Do not think that free verse has no craft. Line breaks, repetition and sound still create rhythm and emphasis."),
        T("When you write about form, ask: Is there a regular stanza, or free verse? Where does the poet repeat? Where do the lines run on (enjambment) and where do they stop? Does the sound make you want to say it aloud? Then say why each choice suits the content."),
        MISTAKE("Naming a technique without effect", "The Board's report says candidates mention devices such as alliteration or apostrophe without showing what they do. Always add: 'This makes the speaker sound... ', 'This suggests... ', 'This reinforces the idea of...'."),
        MISTAKE("Treating oral poetry as primitive", "Oral forms are sophisticated art with strict rules of memory, performance and audience. Write about them with respect and precision."),
        MISTAKE("Quoting from memory", "Quote only a few words, exactly as in your copy. A wrong quotation shows you do not know the poem."),
        QUIZ("A poet writes: 'O my country, when will your children stop crying?' Which device is this?", [
            "Simile", "Apostrophe", "Alliteration", "Pun"], 1,
            "The speaker addresses an absent thing, the country, as if it could hear. That is apostrophe.",
            hint="Who is the speaker talking to, and is that person or thing present?",
            feedback=["A simile compares two things with 'like' or 'as'.", "", "Alliteration repeats initial consonant sounds.", "A pun plays on a word with two meanings."]),
        QUIZ("Which feature of oral performance most directly invites an audience to join in?", [
            "Free verse", "Call and response", "A long stanza", "A sad tone"], 1,
            "In call and response a leader's line is answered by the audience or chorus.",
            hint="Think of a leader and a crowd.",
            feedback=["Free verse is a form without fixed pattern, not a way of involving an audience.", "", "Stanza length does not involve an audience.", "Tone describes mood only."]),
        PQ("Define parallelism and give your own two-line example about a market.", "Parallelism is the repetition of the same sentence shape with different content. Example: 'Where the buyers gather, the prices rise; where the sellers rest, the prices fall.' The repeated 'Where... , the...' pattern is the parallel structure."),
        PQ("Explain why poets who write in English still use oral features such as repetition and direct address.", "These features come from spoken art, which used them to help memory and to involve an audience. Poets use them to keep African voice and rhythm in English, to sound like speech, and to carry the meaning of ceremonies such as praise and mourning."),
        PQ("Write a short paragraph (four sentences) on how one named oral feature works in any one poem of your anthology, with a placeholder for the poem.", "Model: 'In [poem title], [poet] uses [feature]. For example, [a few exact words from your copy]. This makes the speaker sound [effect]. It supports the poem's theme of [theme].' A complete answer replaces each bracket with specific facts from your copy."),
        SUM("Know oral prose forms (myth, legend, folktale, proverb, riddle) and oral poetic forms (praise poetry, dirge, incantation, work song).",
            "Oral habits in written poems: repetition, parallelism, refrain, call and response, ideophone, direct address.",
            "Apostrophe means addressing an absent, abstract or dead person or object as if present; it is used for emotional effect.",
            "Free verse still has craft: line breaks, repetition and sound.",
            "Always explain the effect of a device in the poem, not only its name."),
    ],
))

# ------------------------------------------------------------------ 3. Cultural symbolism and theme
LESSONS.append(lesson(
    module=M_POET, topic=T_SYMB,
    title="Cultural symbolism and theme: ancestors, disillusionment, protest and pride",
    slug="liu2-cultural-symbolism-theme",
    minutes=24,
    summary="Anthology poems turn objects, animals, spirits and places into symbols and gather around themes such as the living dead, disillusionment with rulers, apartheid and prison, and cultural pride; this lesson uses the report's descriptions to teach theme-based selection and balanced argument.",
    objectives=[
        "Distinguish a symbol from a plain image and explain what a cultural symbol stands for",
        "Group poems under the themes the Board's report names: the living dead, African beliefs, disillusionment and satire, and cultural identity",
        "Select and justify poems for a theme using the report's descriptions as a guide",
        "Argue both sides of a question, as the report recommends for the disillusionment question",
    ],
    key_concepts=["Symbol", "Cultural symbolism", "The living dead", "Disillusionment", "Satire", "Protest and hope", "Cultural identity"],
    blocks=[
        H("Introduction"),
        T("In many African communities a grinding stone is more than a tool. It can hold the memory of the woman who used it every day. A squirrel crossing the path can be a message. A sea can be a goddess. When a poet uses such things, the reader must know the culture behind them, or the poem seems to say less than it means."),
        T("The Board's 2023 report asks candidates to link poems to themes and to know the 'philosophies or conventions' behind them. For the anthology it names the African personality, colonialism, assimilation, Negritude, apartheid and neo-colonialism as background. This lesson shows how to turn that background into theme-based answers."),
        T(OWNCOPY),
        H("Symbol and cultural symbol"),
        D("An **image** is a picture in words. A **symbol** is an image, object, creature or action that stands for an idea beyond itself, and keeps its literal meaning as well. A **cultural symbol** gets its meaning from the beliefs and customs of a community.", title="Symbol"),
        T("To explain a symbol, give three things: what it is in the poem, what it stands for and what that adds to the theme. Never say only 'it symbolises hope'. Say why, with a detail from the poem."),
        CODE("Poem (poet)          Symbol (as the report describes it)       What it stands for (check your copy)\n"
             "The Bond (Kunene)   Masilela's grinding stone                 Ancestral legacy and the bond of duty\n"
             "Olokun (Clark)      The sea goddess who charms her lovers      The power of gods; mortals who rival gods fall\n"
             "If (Angira)         A squirrel or a cheetah crossing the path   Omens: good or bad luck\n"
             "Agony (Tchicaya)    The boatman, the bird, the lake of blood    Suffering of a people and a search for identity\n"
             "Upheaval (Dipoko)   A ruler on a sinking throne                A tyrant's fall\n"
             "Rulers (Dipoko)     Palace feasts and dances                   Greed that ignores the poor", "text", title="Symbols named in the Board's report"),
        H("Theme 1: the dead are not dead"),
        T("The report says an old-syllabus question asked how the belief that 'the dead are not dead' is sustained in three poems of the candidate's choice. It suggested poems such as Birago Diop's 'Breath' and 'Vanity', Richard Ntiru's 'To the Living', Wole Soyinka's 'Dedication' and Ismael Hurreh's 'Pardon Me'. This belief means that the dead remain present, give blessings and protection, and may punish neglect."),
        T("A new-syllabus question asked for poems reflecting the traditional African mind-set about the natural and supernatural worlds. The report names 'The Bond', 'Olokun', 'If' and 'Agony'. Notice that 'Olokun' is about gods and 'If' about omens, so this theme is wider than ancestors: it is about a world in which the visible and the invisible are connected."),
        T("Be careful about how you write. These poems present beliefs. Say 'the poem presents the belief that', 'traditional African thought holds that', not 'Africans are superstitious'. Respect and exactness earn marks."),
        H("Theme 2: disillusionment and satire"),
        D("**Disillusionment** is the painful loss of hopes and trust, here the disappointment that followed independence or colonial promises. **Satire** is a way of criticising faults in people or society by ridicule, anger or irony, in order to correct them.", title="Two key terms"),
        T("The report says a new-syllabus question asked for poems showing that Black African poets are dissatisfied with the ills of their societies and respond with satire. It described: poor government and extravagant rulers in Dipoko's 'Rulers', rulers who prefer civil war to handing over power in Dipoko's 'Upheaval', torture and police raids under apartheid in Brutus's 'The Sounds Begin Again', cruel prison conditions in Brutus's 'Cold', suffering under colonialism and racism in Tchicaya U Tam'si's 'Agony', moral decline in 'Phlora', and traitor-leaders and false values in David Diop's 'The Right Road'. The report said candidates struggled with the word 'disillusionment' and wrote about irrelevant poems."),
        IMG("alliu2-theme-map.svg", alt="Three theme boxes (The living dead and beliefs; Disillusionment and satire; Cultural identity and hope) each listing poems named in the Board's report.", caption="Figure 1. Three themes and the poems the report links to them."),
        H("Theme 3: hope and cultural identity"),
        T("The report adds that good answers would argue the other side as well: despite the disillusionment, these poets keep hope in the suffering masses and celebrate their cultural identity, beliefs and vitality. It names 'Olokun', 'The Bond' and 'If' as poems that celebrate the authenticity of African cultural identity, and it notes that Dipoko hopes in 'Upheaval' for a revolution that removes a tyrant, while David Diop's 'The Right Road' both condemns false leaders and urges youth towards truth, beauty and love."),
        KEY("Balanced argument", "A question that says 'show that poets are...' still rewards a counter-point.", cards=[
            ["Claim", "State the main idea of the question in your own words."],
            ["Proof", "Give poems and exact details that prove it."],
            ["Complication", "Show that the poets also celebrate, hope or resist. This is what the report calls the good candidate's extra step."],
            ["Judgement", "End with a short verdict: which idea is stronger across the poems, and why."],
        ]),
        EX("Worked example 1: explaining a symbol", intro="Explain the symbolism of the grinding stone in 'The Bond', using the report's description. (Check each point in your copy.)", steps=[
            S("What it is", text="A grinding stone that belonged to Masilela and is handed to Gumede in a succession ritual."),
            S("What it stands for", text="The legacy of the ancestor and the duty of the living to keep it sacred."),
            S("What it adds", text="The warning that curses follow if it is defiled turns an ordinary tool into a test of loyalty, and supports the theme that the ancestors protect the living when respected."),
        ]),
        EX("Worked example 2: planning an essay", intro="Question (written for practice): 'Poets in the anthology criticise the ills of their societies, but they never lose hope.' Discuss with reference to three poems.", steps=[
            S("Introduction", text="Define disillusionment and say that the poets both protest and hope."),
            S("Paragraph 1: protest", text="'Rulers': greedy rulers feasting while the poor cry (Dipoko, Cameroon). Name the satire and its target."),
            S("Paragraph 2: protest in a second region", text="'Cold' or 'The Sounds Begin Again' (Brutus, South Africa): apartheid prison and raids. Link the anger to colonial and racial oppression."),
            S("Paragraph 3: hope", text="'Upheaval' (revolt follows the tyrant's fall) or 'The Right Road' (urging youth towards truth). Show that protest carries hope."),
            S("Conclusion", text="Judge: the anger is strong, but it grows from love for the community, so hope does not disappear."),
        ]),
        MISTAKE("Misreading disillusionment", "The report says candidates did not grasp the word and chose irrelevant poems. It means disappointed hope about rulers, independence or society, not any sad poem."),
        MISTAKE("Saying a symbol 'just represents Africa'", "Name the symbol, the idea it carries and the evidence. 'Africa' alone is too vague to earn marks."),
        MISTAKE("Using a poem for a theme it does not support", "Before you use a poem, say in one sentence how it shows the theme. If you cannot, choose another."),
        QUIZ("According to the Board's report, which poem is described as showing a boatman, a bird and a lake of blood?", [
            "'Olokun'", "'The Bond'", "'Agony'", "'Cold'"], 2,
            "The report describes Tchicaya U Tam'si's 'Agony' with a boatman, a bird that directs him across a lake of blood, and a suffering people.",
            hint="Think of the Congolese poet in the list.",
            feedback=["'Olokun' is about a sea goddess.", "'The Bond' is about a grinding stone.", "", "'Cold' is Brutus's prison poem."]),
        QUIZ("Which approach does the report suggest earns higher marks on a question about the poets' dissatisfaction with society?", [
            "Listing only the sad poems", "Arguing that the poets also keep hope and celebrate their culture", "Retelling every poem", "Avoiding named poems"], 1,
            "The report says good candidates would argue the other side: the poets still hold hope and celebrate identity.",
            hint="What does the report say a good candidate adds?",
            feedback=["That is one-sided.", "", "Retelling does not answer the question.", "Named poems are the evidence."]),
        PQ("Choose three poems for the theme 'the dead are not dead' and give one sentence of reason for each, using the report.", "Any three of: 'Breath' or 'Vanity' (Diop), 'To the Living' (Ntiru), 'Dedication' (Soyinka), 'Pardon Me' (Hurreh), 'The Bond' (Kunene). Reason model for 'The Bond': the ancestor's grinding stone must be kept sacred or she will curse, which shows that the dead still care about the living."),
        PQ("Explain the difference between an image and a symbol, with the report's grinding stone as an example.", "An image is a picture in words. A symbol also stands for an idea. In 'The Bond' the grinding stone is a real object and also stands for the ancestor's legacy and the duty of the living to protect it."),
        PQ("Write a thesis sentence for a question on satire in the anthology.", "Model: 'African poets use satire to attack greedy rulers, apartheid brutality and moral decay, yet their anger is a form of hope because it calls for change.' (A thesis answers the question and previews the argument.)"),
        SUM("A symbol is a thing that also stands for an idea; cultural symbols draw meaning from community beliefs.",
            "The report links the living dead and African beliefs to 'Breath', 'Vanity', 'To the Living', 'Dedication', 'Pardon Me', 'The Bond', 'Olokun', 'If' and 'Agony'.",
            "Disillusionment and satire appear in 'Rulers', 'Upheaval', 'The Sounds Begin Again', 'Cold', 'Agony', 'Phlora' and 'The Right Road' as the report describes them.",
            "Good answers argue both sides: protest and hope, criticism and cultural pride.",
            "Say how each poem proves your point; avoid vague words such as 'Africa' or 'sad'."),
    ],
))

# ------------------------------------------------------------------ 4. Writing about the anthology
LESSONS.append(lesson(
    module=M_POET, topic=T_WRITE,
    title="Writing about the anthology: question types, plans and paragraphs that earn marks",
    slug="liu2-writing-about-anthology",
    minutes=24,
    summary="How to read a Paper 2 poetry question, choose poems, plan an essay and write paragraphs with topic sentence, exact illustration and critical comment, avoiding the errors the Board's 2023 report lists.",
    objectives=[
        "Recognise the main kinds of anthology question: theme, belief or background, device, poet or attitude, and the 'short notes' question",
        "Plan an essay with a thesis, poem choices and a counter-point in five minutes",
        "Write a paragraph with a topic sentence, several illustrations and a closing comment",
        "Follow the Board's presentation rules: titles, authors, quotations, instructions and the number of answers",
    ],
    key_concepts=["Command word", "Thesis", "Topic sentence", "Illustration", "Critical perspective", "Presentation conventions"],
    blocks=[
        H("Introduction"),
        T("Two students in Buea know the same ten poems. One scores 7 out of 10 and the other 3. The difference is not memory. The first student answers the exact question, picks poems that fit, proves each point with details and writes clean English. The second narrates poems and hopes the examiner finds the relevant parts."),
        T("The Board's 2023 report describes the structure of Paper 2: it has Sections A, B and C for drama, prose and poetry; two questions are set on each of the eight set texts; candidates answer four, one from each section and a fourth from any section but a different text. The anthology is one of the Section C poetry texts. Check the instructions on your own paper and with your teacher."),
        T(OWNCOPY),
        H("Four question families"),
        KEY("What the question asks", "Name the family, then plan.", cards=[
            ["Belief or background", "Example from the report: show how the idea that the dead are not dead is sustained in three poems of your choice. Choose three poems and tie each to the belief."],
            ["Theme and attitude", "Example: poets are dissatisfied with the ills of their societies and use satire. Show the ills, the satire and, in a good answer, the counter-hope."],
            ["Device", "Example: comment on the use of apostrophe in three poems. Name the device, quote its words, explain its effect on feeling or theme."],
            ["Short notes", "A question that asks for short notes on listed aspects wants a few exact points on each, not an essay. The report says some candidates answered more items than allowed."],
        ]),
        T("The report also says many anthology questions mix two things, such as setting and theme or plot and style. Read both parts and answer both."),
        H("Command words"),
        D("**Discuss**: give a developed, balanced view. **Examine**: look closely at the parts. **How far / to what extent do you agree?**: give a judgement with reasons on both sides. **Illustrate**: give examples and explain them. **Justify**: give reasons for a claim. The report advises teaching learners the meaning of these tags early in the year.", title="Common tags"),
        H("A planning routine"),
        EX("Worked example 1: a five-minute plan", intro="Question (written for practice): 'Examine how poets in the anthology use symbolism to present traditional African beliefs, with reference to three poems.'", steps=[
            S("Underline", text="Command word: examine. Focus: symbolism presenting traditional beliefs. Number of poems: three."),
            S("Thesis", text="Poets use objects, creatures and spirits as symbols to show that the natural and supernatural worlds are one, and to respect that view."),
            S("Choose poems", text="'The Bond' (the grinding stone), 'Olokun' (the sea goddess), 'If' (animal omens), all of which the Board's report links to African beliefs."),
            S("Points", text="For each: what the symbol is, what it stands for, what that shows about belief. Add a different region if you wish, for variety."),
            S("Counter-point and verdict", text="Some poems may use belief to criticise rather than only celebrate. Judge which is stronger."),
        ]),
        EX("Worked example 2: one model paragraph", intro="Write the paragraph on 'The Bond' for the plan above, using the report's description. Replace the bracket with exact words from your own copy.", steps=[
            S("Topic sentence", text="In 'The Bond', Kunene makes a grinding stone a symbol of the ancestor's authority over the living."),
            S("Illustration 1", text="The stone belonged to Masilela and is handed to Gumede in a succession ritual, so the object carries the family's history."),
            S("Illustration 2", text="The warning that the ancestor will curse the living if the stone is defiled shows that duty to the dead is a serious bond. [Add a few exact words from your copy.]"),
            S("Critical comment", text="Because an everyday tool is raised into a sacred symbol, the poem presents ancestor respect as part of ordinary life, which suits its solemn tone."),
        ]),
        T("Notice the structure: topic sentence, at least two illustrations, a comment on effect. The Board's report says one sketchy illustration in a paragraph earns only a skimpy mark; more full and focused illustrations raise the mark."),
        H("Presentation rules from the report"),
        D("The Board's report asks candidates to: put the titles of poems in quotation marks; underline titles of collections, novels and plays; indent or centre quotations longer than four lines; identify each poem with its rightful author; follow the instructions on the number of questions and items; and write clearly, in acceptable English, with correct spelling and subject-verb agreement. It also says candidates should not answer more questions than required, should not answer two questions from the same section where the paper forbids it, and should not choose two questions on the same text.", title="Presentation"),
        IMG("alliu2-essay-plan.svg", alt="A vertical flow: Introduction (answer the question), Body paragraphs (topic sentence, illustrations, comment), Counter-point, Conclusion (judgement).", caption="Figure 1. The shape of an anthology essay."),
        H("Introductions and conclusions"),
        T("A good introduction is three or four sentences: define the key word of the question, give your thesis and name the poems. Do not retell the poet's life. A good conclusion gives the judgement and links back to the question. The report asks for a conclusion 'with an air of logical finality'."),
        MISTAKE("Answering more questions than allowed", "The report says some candidates wrongly believe that all answers will be marked and the best chosen. Extra answers are shallow and the marks are wasted. Answer exactly the number asked."),
        MISTAKE("Using a poem without proof", "Writing that 'Dipoko criticises rulers' is a claim. Add what the rulers do in the poem (according to the report, feast, boast and squander funds) and what that shows."),
        MISTAKE("Poor language and handwriting", "The report says feeble language prevents good ideas from scoring. Plan, write in short clear sentences and re-read. Use ink, not pencil, where the paper requires it."),
        MISTAKE("Ignoring a second part of the question", "A question that blends setting and theme, or plot and style, must be answered in both parts. Underline each part."),
        QUIZ("Which is the correct way to present the title of a single poem in handwritten work?", [
            "Underline it", "Put it in quotation marks", "Write it in capitals only", "Leave it unmarked"], 1,
            "The report says poem titles go in quotation marks, while titles of collections, novels and plays are underlined.",
            hint="Compare a poem title with the title of the whole anthology.",
            feedback=["That is for the title of a collection, novel or play.", "", "Capitals alone do not signal a title.", "The report lists this as a convention to follow."]),
        QUIZ("A candidate writes five short, thin paragraphs each with one illustration. According to the report, how could the answer be improved?", [
            "Add more paragraphs with one illustration", "Make fewer, fuller paragraphs with several focused illustrations each", "Remove all illustrations", "Write the same point five times"], 1,
            "The report says that more full and focused illustrations in each paragraph earn more.",
            hint="What does the report say about 'one sketchy bit of evidence'?",
            feedback=["More thin paragraphs do not solve the thin evidence.", "", "Illustration is the proof; without it the claim is weak.", "Repeating a point wastes time."]),
        PQ("Write a thesis for: 'To what extent do poets in the anthology present the past as a source of strength?'", "Model: 'The poets present ancestors, rituals and inherited objects as a real source of strength, though some poems warn that the past can be neglected or defiled, so the strength depends on the living keeping faith with it.' The thesis answers 'to what extent' with a qualified yes."),
        PQ("List three things a candidate must do to follow the Board's presentation rules in a poetry answer.", "Any three of: poem titles in quotation marks; collections, novels and plays underlined; quotations longer than four lines indented or centred; each poem given with its right author; answering the required number of questions; correct spelling and grammar."),
        PQ("A question asks for the use of apostrophe in three poems. Plan the answer.", "Define apostrophe (addressing an absent, abstract or dead person or thing). Choose three poems the report names, such as Diop's 'Vanity', Soyinka's 'Dedication', Hurreh's 'Pardon Me'. For each: who is addressed, a few exact words, the effect (grief, respect, accusation). Add a short comment on what apostrophe does for the African idea of ancestor presence. Conclude with a judgement of its overall effect."),
        SUM("Name the question family (belief, theme, device, short notes) and underline the command word and the number of poems.",
            "Plan in five minutes: thesis, poems, points and a counter-point.",
            "Write paragraphs with a topic sentence, several focused illustrations and a closing comment.",
            "Follow the Board's presentation rules: quotation marks for poem titles, underlining for collections, correct authors, and the number of questions required.",
            "Use clear English and a conclusion that gives a judgement."),
    ],
))

# ------------------------------------------------------------------ 5. Unseen prose
LESSONS.append(lesson(
    module=M_UNSEEN, topic=T_UPROSE,
    title="Unseen prose: meaning in context, citation, attitude and response",
    slug="liu2-unseen-prose",
    minutes=24,
    summary="A method for the unseen prose question: read for meaning and voice, give meaning in context, cite exact words in quotation marks, identify attitude from short phrases and respond to the passage with a practical solution or personal reply.",
    objectives=[
        "Read an unseen prose passage for situation, voice, tone and structure in two reads",
        "Give the meaning of a word or phrase in context, using a word or phrase of the same kind",
        "Cite exact words in quotation marks and keep a citation as short as the question asks",
        "Identify attitude from diction and answer a response task such as conflict resolution",
    ],
    key_concepts=["Unseen passage", "Meaning in context", "Citation", "Attitude and tone", "Diction", "Substantiation"],
    blocks=[
        H("Introduction"),
        T("In the unseen prose question you meet a passage nobody has taught you. That sounds frightening, but the Board's 2023 report says this is exactly where candidates lost easy marks: they gave the dictionary meaning of words and not the meaning in context, they copied whole sentences when asked to cite, they could not state attitude and they could not suggest a practical solution from the passage."),
        T("The report describes the prose question as having sub-tasks of these kinds: the meaning in context of several words and expressions; citing evidence from the passage to defend an argument; substantiating a view about the community or characters; picking out short phrases that reveal attitude and describing the attitude; and identifying skills, such as conflict-resolution skills, shown in the passage. We practise each on invented passages written for this course."),
        T("**The Return** below is invented for practice. Read it twice before you continue."),
        T(PROSE_RETURN),
        H("Step 1: two reads"),
        T("First read: what is happening, who is speaking, to whom, where and when? Second read: underline words that show feeling, images and comparisons, and note where the mood changes. In this passage the narrator is a young man returning home after six years in a city. The first paragraph is warm and nostalgic. In the second, an uncle's question turns the mood thoughtful and slightly embarrassed."),
        H("Step 2: meaning in context"),
        D("**Meaning in context** means what a word or phrase means in the passage, not every meaning it has. Give a word or phrase of the same grammatical kind, in your own words, that could replace it. Do not repeat the word.", title="Meaning in context"),
        EX("Worked example 1: meaning in context", intro="Give the meaning in context of: (i) 'too small for the afternoon'; (ii) 'long, polite silences of strangers'; (iii) 'pretending not to notice me'.", steps=[
            S("(i)", text="Too weak or too ordinary to express the strength of the feeling at that moment. The speaker and his mother felt more than their prepared words could carry."),
            S("(ii)", text="Quiet, correct but cold distance between people who did not know or care for one another. 'Polite' means well-mannered but not warm."),
            S("(iii)", text="Acting as though they had not seen him, in a humorous way, as if the chickens were behaving with good manners or shyness. The phrase gives the chickens human behaviour (personification)."),
        ]),
        H("Step 3: citing evidence"),
        D("To **cite** is to pick out the exact words from the passage and put them inside quotation marks. A citation answers 'which words?'. If the question limits the length, for example 'two words', obey the limit. After a citation you may add a short comment if the question asks you to explain.", title="Cite"),
        MISTAKE("Copying a whole sentence", "The report says many candidates lifted chunks of the passage without quotation marks when asked for short phrases. This loses the mark. Read the limit ('not more than two words') and give exactly that."),
        EX("Worked example 2: cite and substantiate", intro="(a) Cite two phrases that show the narrator felt out of place. (b) Substantiate the view that the uncle's question is a challenge.", steps=[
            S("(a) Choose the words", text="'made me shy' and 'Only I had changed'. Both show he feels different from the home he remembers."),
            S("(a) Check", text="Both are exact words from the passage, in quotation marks."),
            S("(b) Claim", text="The uncle questions whether the narrator has learned to belong, not only to achieve."),
            S("(b) Proof", text="He asks if the city taught him 'to sit with your family' or 'only to visit them', which suggests that the narrator may have become a visitor in his own home. The narrator's response, looking at his plate, shows the challenge has hit home."),
        ]),
        H("Step 4: attitude and tone"),
        T("**Attitude** is what a character or writer feels about something. **Tone** is how this is shown in the voice of the passage. To find attitude, pick out words and phrases that carry feeling (diction), say what feeling they show and give the reason. Words like 'slowly', 'grudging' or 'proudly' are strong clues."),
        CODE("Phrase from the passage      Attitude shown\n"
             "'nodded slowly'            The uncle: serious, patient, not impressed.\n"
             "'polite silences'          The narrator: found the city distant and unfriendly.\n"
             "'worth answering'          The narrator: respect and humility.", "text", title="Phrases of two words or fewer and the attitude they show"),
        EX("Worked example 3: a tone question", intro="Describe the tone of the second paragraph of 'The Return' and say how it differs from the first.", steps=[
            S("First paragraph", text="Warm, nostalgic and humorous: the mother with 'both hands out', the chickens 'pretending'."),
            S("Second paragraph", text="Quieter, serious and reflective: the uncle's question and the long silence."),
            S("The change", text="The mood moves from the joy of arrival to the harder question of belonging."),
        ]),
        H("Step 5: response tasks"),
        T("The Board's report says some tasks ask you to go beyond the lines: to react as a character, to suggest a solution or to state a skill shown in the passage. In the report's example, candidates had to name efficient conflict-resolution skills found in the passage and most rambled. The rule is: **name the skill first, then prove it with the passage**."),
        KEY("A response routine", "Use this to avoid rambling.", cards=[
            ["Name it", "Write the skill or point in a few words (for example, listening before judging)."],
            ["Prove it", "Say what a character does in the passage that shows it."],
            ["Link it", "Say why it helps, in one sentence."],
        ]),
        EX("Worked example 4: a response task", intro="Invented mini-passage: 'Two neighbours quarrelled over a drain that flooded both yards. The older woman asked the younger one to describe the flood first, repeated it in her own words to be sure she understood, and only then said what she had seen. Together they dug a shallow channel.' Name two skills the older woman shows.", steps=[
            S("Skill 1: active listening", text="She lets the younger woman speak first and repeats the account, which shows she has understood."),
            S("Skill 2: shared problem-solving", text="She states what she has seen and then they dig a channel together, so the solution comes from both sides."),
            S("Link", text="Both skills lower anger and focus on the flood, not on blame."),
        ]),
        MISTAKE("Dictionary meaning only", "The word 'draught' has several meanings. The report notes a poem where candidates chose the wrong meaning and misread the whole poem. Always test the meaning against the surrounding lines."),
        MISTAKE("Rambling instead of naming", "If the question asks for a skill, state it in a clear phrase before explaining. Examiners cannot award marks for implied relevance."),
        MISTAKE("Retelling the passage", "Every question wants a specific task done. A summary of the passage rarely answers it."),
        QUIZ("A question asks you to cite two phrases of not more than two words each. Which is the best answer?", [
            "'Only I had changed', because it is short", "'polite silences' and 'nodded slowly'", "The whole sentence containing 'polite silences'", "Any two words that seem important"], 1,
            "Both phrases are two words and in quotation marks.",
            hint="Count the words and look for quotation marks.",
            feedback=["It has four words and breaks the limit.", "", "A sentence breaks the length limit.", "Without checking the words and the limit, the citation may be wrong."]),
        QUIZ("What does 'meaning in context' require?", [
            "Any dictionary meaning", "A meaning that fits the passage, stated in your own words", "A copy of the original word", "A translation into French"], 1,
            "It means the meaning that fits the passage, expressed in a word or phrase of the same kind.",
            hint="Why does the word 'context' appear in the term?",
            feedback=["A dictionary has many meanings; only one fits.", "", "Repeating the word shows no understanding.", "No translation is needed."]),
        PQ("Give the meaning in context of 'a question worth answering' in the last sentence of 'The Return'.", "A question serious and important enough to deserve a thoughtful reply. The narrator feels that the uncle's question is not casual but challenges him to think about where he belongs."),
        PQ("Cite one phrase of not more than three words that shows the narrator's humility and explain the attitude it reveals.", "'made me shy' (three words) or 'worth answering' (two words). 'made me shy' shows that he feels uncomfortable and small in his own home; 'worth answering' shows he respects his uncle's challenge."),
        PQ("Substantiate the view that the family in 'The Return' is warm in welcome but frank in speech.", "Warm: the mother meets him 'with both hands out'; frank: the uncle asks whether the city taught him 'to sit with your family' or 'only to visit them'. Together these show affection that does not avoid hard truths."),
        SUM("Read twice: first for situation and voice, second for feeling words and shifts of mood.",
            "Meaning in context: a word or phrase of the same kind that fits the passage, not any dictionary sense.",
            "Cite: exact words in quotation marks, as short as the question allows.",
            "Attitude comes from diction: name the feeling and give the reason.",
            "For response tasks, name the skill or answer first, then prove it from the passage."),
    ],
))

# ------------------------------------------------------------------ 6. Unseen poetry
SUMMARY_MARKET = ("The poem describes the end of a market day. In the first stanza the traders pack up and the tired sellers count both their money and "
                  "their suffering, so the day's profit is mixed with pain. In the second stanza a girl sweeps the rubbish and hums a tune that nobody speaks "
                  "about, though it carries everything she feels. In the third stanza the lamps go out, only the stars remain, and she lifts her basket and goes "
                  "home humming; the tune frees her. The mood moves from weariness, through quiet dignity, to a gentle hope. The poet suggests that ordinary "
                  "people bear hardship with a private song, and that the song gives them the strength to continue. The regular rhyme and steady rhythm echo the "
                  "calm routine of the day's end, while the final line, with its word free, closes the poem on freedom of spirit.")

LESSONS.append(lesson(
    module=M_UNSEEN, topic=T_UPOEM,
    title="Unseen poetry: meaning, words, sound, metaphor, rhyme and writing a stanza",
    slug="liu2-unseen-poetry",
    minutes=25,
    summary="A step-by-step method for the unseen poem: summarise the meaning and tone, test word meanings in context, identify and explain sound devices and metaphors, plot the rhyme scheme and its effect, and write a six-line stanza of your own.",
    objectives=[
        "Write a meaning-and-tone summary of a poem in about 150 words",
        "Choose the meaning of a word that fits the poem, not the first meaning you know",
        "Identify a sound device or metaphor, quote it and explain its effect",
        "Plot a rhyme scheme and comment on its effectiveness, and write six lines in a chosen form",
    ],
    key_concepts=["Meaning and tone", "Words in context", "Sound devices", "Metaphor", "Rhyme scheme", "Scansion", "Creative response"],
    blocks=[
        H("Introduction"),
        T("The Board's 2023 report calls the unseen poem the weakest part of Paper 3: most scripts scored very low. It describes the sub-tasks: give the meaning of the poem in about 150 words and show how the tone contributes; give the meanings of words and expressions; comment on a sound device and explain a metaphor; establish the rhyme scheme and comment on its effectiveness; and write a six-line poem expressing your thoughts about a similar situation."),
        T("The report adds the reasons: candidates misread a key word (one thought a word meant dryness and wrote about drought, when the poem was about a patient before surgery); they named sound devices vaguely without quoting; they found a rhyme scheme but could not say what it did; and they wrote prose in six lines instead of poetry. This lesson answers each problem on an invented poem."),
        T(POEM_MARKET),
        H("Step 1: meaning and tone"),
        T("Read the title, then the whole poem, then ask: who speaks, what happens, where is the turning point and how does the mood change? **Tone** is the speaker's attitude, shown by word choice and sound. Here the tone is tired but dignified in stanza 2, then quietly hopeful in stanza 3, marked by the word **yet** at the start of the last stanza."),
        EX("Worked example 1: meaning in about 150 words", intro="Write a summary of the meaning of 'Evening Market' and show how the tone contributes.", steps=[
            S("Plan", text="Stanza 1: end of the day and tired sellers. Stanza 2: the girl and the unspoken tune. Stanza 3: the lamp burns low, the tune frees her. Tone: weary, then hopeful."),
            S("Model summary (147 words)", text=SUMMARY_MARKET),
            S("Check", text="The model covers all three stanzas, states the theme, names the tone change and comments on form. Count your words and stay near the limit."),
        ]),
        H("Step 2: words in context"),
        T("Test every unknown word with its neighbours. 'Bargained' is clear: haggled over prices. 'Stalks' are the dry stems of vegetables and plants left in a market. 'Peel' means skin of fruit. Always ask whether the meaning you chose makes the whole sentence and poem sensible. If it does not, try another."),
        H("Step 3: sound devices"),
        D("**Alliteration** repeats the same consonant sound at the start of nearby words. **Assonance** repeats a vowel sound. **Consonance** repeats consonant sounds inside or at the end of words. **Onomatopoeia** is a word that imitates a sound. **Repetition** returns a word to build emphasis.", title="Sound devices"),
        EX("Worked example 2: comment on a sound device", intro="Comment on the sound device in 'Now count their coins and count their pain'.", steps=[
            S("Name and quote", text="Repetition of the word 'count' and the repeated /k/ sound in 'count', 'coins' (hard c sounds)."),
            S("Explain the effect", text="The beat of the repeated word imitates the steady counting of coins; it links money and pain in the same action."),
            S("Link to meaning", text="The sound makes the line feel mechanical and weary, which supports the tired tone."),
        ]),
        H("Step 4: metaphor"),
        D("A **metaphor** says one thing is another, or speaks of one thing as if it were another, without 'like' or 'as'. To explain it: say what is compared to what, what they share and what the comparison suggests.", title="Metaphor"),
        EX("Worked example 3: explain a metaphor", intro="Explain 'count their pain' and 'it carries all' in the poem.", steps=[
            S("'count their pain'", text="Pain is treated as money that can be counted. It shows that the traders add up their suffering as well as their earnings, and suggests that the day's work costs them physically and emotionally."),
            S("'it carries all'", text="The tune is spoken of as a bearer, a person carrying a load. It means the humming holds everything the girl feels but never says: tiredness, hope and courage."),
        ]),
        H("Step 5: rhyme scheme and effect"),
        T("Write a letter for each line end. Same sound, same letter. Stanza 1 ends: away, lane, day, pain, giving A B A B. Stanza 2: stalks, wall, talks, all, giving C D C D. Stanza 3: low, see, go, free, giving E F E F. The scheme is **ABAB CDCD EFEF**, an alternating rhyme in three quatrains."),
        IMG("alliu2-feet-patterns.svg", alt="Four metrical feet shown with stress marks: iamb (unstressed, stressed), trochee (stressed, unstressed), anapaest (two unstressed, stressed), dactyl (stressed, two unstressed), and the line 'Into a pile beside the wall' marked as four iambs.", caption="Figure 1. The four common feet and a line of iambic tetrameter."),
        T("Each line has eight syllables in a pattern of weak and strong beats: for example, 'in-TO a PILE be-SIDE the WALL'. That is four iambs, or **iambic tetrameter**. Metre is the pattern of stressed and unstressed syllables, and a **foot** is one unit of that pattern."),
        T("**Effect of the form.** The regular rhyme and steady metre give the poem a calm, song-like feeling that matches the humming girl and the routine of closing the market. The pattern stays regular even in the third stanza, so the hope is quiet and controlled, not a sudden burst. A comment on effect is a **must**: the report says candidates found the scheme but could not say what it did."),
        H("Step 6: writing six lines"),
        T("The report describes a task to write a six-line poem expressing your thoughts about a similar situation. It says many scripts were continuous prose, and only a few respected form, structure, poetic effect and style. A poem is not a paragraph cut up into lines. Choose a form (for example AABBCC couplets or ABABCC), choose images from your own experience, keep lines roughly equal and read it aloud."),
        EX("Worked example 4: a six-line response", intro="Write six lines (rhyme AABBCC) about a student walking home after a long exam day. (Invented model.)", steps=[
            S("Model", text="The sun goes down, the road is long, / My head is full of dust and song. / The pencils tapped, the minutes flew, / And now I walk with all I knew. / No answer sheet can hold me fast; / I breathe the evening, free at last."),
            S("Why it works", text="Rhyming couplets (long/song, flew/knew, fast/last), a steady rhythm, concrete images (dust, pencils, evening) and a shift from tiredness to relief."),
        ]),
        MISTAKE("Choosing the wrong meaning of a word", "Test the meaning against the line, the stanza and the title. The report's example shows how one wrong guess destroys the whole interpretation."),
        MISTAKE("Naming a device you cannot quote", "Write the device, then the exact words in quotation marks, then the effect. Without a quotation, the mark is lost."),
        MISTAKE("Finding the rhyme scheme but not the effect", "Always add one sentence: the rhyme gives what mood, links which ideas, or helps which theme."),
        QUIZ("What is the rhyme scheme of a quatrain that ends: day, sea, way, free?", [
            "AABB", "ABAB", "ABBA", "AAAA"], 1,
            "Day and way rhyme (A, A); sea and free rhyme (B, B). In order the lines are A B A B.",
            hint="Label each line end with a letter in order, giving matching sounds the same letter.",
            feedback=["That would need the first two lines to rhyme with each other.", "", "That would need the first and fourth lines to rhyme.", "Not all four rhyme."]),
        QUIZ("Which comment explains the effect of repeated /s/ sounds in 'the silent streets slept'?", [
            "It is alliteration", "It is alliteration that creates a soft, hushing sound like quiet night", "It is a metaphor", "It rhymes"], 1,
            "A complete comment names the device and explains the effect on sound and meaning.",
            hint="Which answer gives both a name and an effect?",
            feedback=["It names the device but not the effect.", "", "Nothing here is compared.", "Rhyme needs matching line endings."]),
        PQ("State the rhyme scheme of this quatrain and its metre. 'The rain begins, the roofs resound, / A thousand drums in endless sound, / The children laugh and chase the flood, / And sink their feet in singing mud.' (Invented.)", "Scheme AABB (resound/sound and flood/mud, both true rhymes). The lines have eight syllables with a rising iambic beat, mostly iambic tetrameter. Effect: the quick rhyming couplets suit the lively rain and the children's joy."),
        PQ("Explain the metaphor in: 'The old truck is a tired ox on the hill.' (Invented.)", "The truck is compared to an ox: both are heavy, slow and tired but keep pulling. The comparison suggests that the truck struggles and carries its load with effort, and gives it a patient, almost living character."),
        PQ("Write a four-line alternating (ABAB) quatrain about waiting for a bus, with four beats in each line.", "Model: 'The bus is late; the sun climbs high, / We shade our faces with our hands; / The road is empty to the sky, / And patience wears like shifting sands.' The ends are high/hands/sky/sands, giving ABAB."),
        SUM("Summarise the poem stanza by stanza and name the tone change before you write the final 150 words.",
            "Test word meanings against the whole line and poem.",
            "Name a sound device, quote it and explain its effect.",
            "Explain a metaphor by saying what is compared, what they share and what it suggests.",
            "Plot rhyme with letters, name the metre if asked and always comment on effect.",
            "For a six-line poem, keep a form, a pattern and concrete images, not prose in lines."),
    ],
))

# ------------------------------------------------------------------ 7. Practical criticism under exam conditions
POEM_KETTLE = ("**The Kettle** (invented for practice)\n\n"
               "The kettle sings before it boils,\n"
               "a small, impatient saint,\n"
               "and the whole kitchen leans to listen.\n"
               "Then silence, and the steam,\n"
               "which says everything the song could not.")

LESSONS.append(lesson(
    module=M_UNSEEN, topic=T_PRAC,
    title="Practical criticism under exam conditions: form, voice, shifts, imagery and unity",
    slug="liu2-practical-criticism-exam",
    minutes=24,
    summary="A timed routine for unseen prose and poetry: identify form and voice, mark shifts of tone, track image patterns, judge structural unity and write controlled critical paragraphs; plus how to use your time and avoid the faults the Board's report describes.",
    objectives=[
        "Apply a six-step routine to any unseen text in a fixed time",
        "Mark shifts of tone and say how the poet or writer signals them",
        "Track a pattern of imagery and explain how it unifies a text",
        "Write a short critical paragraph that links technique, effect and meaning",
    ],
    key_concepts=["Form", "Voice", "Shift in tone", "Imagery pattern", "Structural unity", "Critical paragraph", "Time plan"],
    blocks=[
        H("Introduction"),
        T("Practical criticism means reading a piece you have never seen and writing about it closely, using only the words on the page. The Board's 2023 report states the overall problem frankly: performance in the unseen sections, and in poetry appreciation especially, was far below expectation, and the report asks teachers to give pupils 'as many unseen prose passages and poems as possible', beginning in Lower Sixth. The report's own figures show success rates of about a third for the prose appreciation question and under ten percent for the poetry appreciation question."),
        T("You cannot memorise your way through an unseen text. You can learn a routine and practise it until it is automatic. That is the aim of this lesson."),
        IMG("alliu2-unseen-routine.svg", alt="Six steps in a column: Read for sense, Form and voice, Shifts, Images and sounds, Structure and unity, Answer each task.", caption="Figure 1. A six-step routine for any unseen text."),
        H("The six-step routine"),
        KEY("Six steps", "Use them in order on every unseen text.", cards=[
            ["1. Read for sense", "Read once through without stopping. Ask: what is happening? Who is speaking? To whom? When and where?"],
            ["2. Form and voice", "Poem or prose? Narrator in first or third person? Stanzas and rhyme or free verse? A calm, angry or playful voice?"],
            ["3. Shifts", "Mark places where the mood, subject, time or speaker changes. Look for signal words: but, yet, then, however."],
            ["4. Images and sounds", "Underline the images and sound patterns. Group them: nature, body, light, money, home."],
            ["5. Structure and unity", "How do beginning, middle and end fit? Does the ending return to the opening? How does the title relate to the text?"],
            ["6. Answer each task", "Re-read each question and give the exact skill it asks for: meaning, citation, device, effect, creative response."],
        ]),
        H("Form and voice"),
        D("**Form** is the shape and structure of a text: stanzas, rhyme, metre, line length, paragraphs, sentence types. **Voice** is the personality we hear: who is speaking and how they feel. **Persona** is the speaker created by the writer, who may not be the writer. Note whether the speaker is the writer's persona, an observer or a character.", title="Form and voice"),
        T("Do not assume that 'I' is the poet. Say 'the speaker' or 'the narrator'. This habit avoids silly mistakes about biography."),
        H("Shifts of tone"),
        D("A **shift** is a turn in mood, subject, time or viewpoint inside a text. It is often marked by a connective ('but', 'yet', 'then'), a change of tense, a change of image, a new stanza or paragraph, or a sudden short line.", title="Shifts"),
        T(POEM_KETTLE),
        EX("Worked example 1: a full critical reading", intro="Read 'The Kettle'. Describe its form, voice, shift, image pattern and unity in about 120 words.", steps=[
            S("Form and voice", text="Five lines of free verse, no rhyme, with short and long lines. The speaker is an observer in a kitchen who speaks with affectionate humour."),
            S("Shift", text="The word 'Then' at the start of line 4 marks the shift from noise ('sings', 'listen') to silence ('silence', 'steam'). The mood changes from playful to quietly thoughtful."),
            S("Images", text="Sound images in the first three lines (sings, listen) contrast with silence and steam. The kettle is a 'small, impatient saint', a metaphor that gives it human, comic holiness."),
            S("Unity", text="The title names the subject. The first line speaks of song, the last line returns to the song and says that silence and steam 'say' more. The ending completes the sound-and-silence pattern, so the poem feels whole."),
            S("Critical comment", text="The poem suggests that what is unspoken can say more than what is said: a small domestic event becomes a meditation on silence."),
        ]),
        H("Image patterns and unity"),
        T("A single image is a detail. A **pattern** of images is a design. When several images belong to the same family (light, water, money, hands) they build a theme. To find a pattern, list all concrete nouns and verbs, then group them. In 'The Kettle' sounds and silence form the pattern. In 'Evening Market' (the previous lesson), money, light and carrying form patterns."),
        T("**Unity** means that the parts of the text fit together. You can argue for it by pointing to repeated images, a return to the opening, a title that gains meaning at the end, or a steady tone with a purposeful shift."),
        H("Using your time"),
        T("The report does not give the paper's timing here, so check the time with your teacher. A sensible plan is to divide time in proportion to marks and always leave time to re-read. In KKEVO practice papers we use a practice setting of about 5 minutes for the six-step read, then time for each sub-task, with a final few minutes for checking spelling and quotation marks. Never leave a creative task such as a six-line poem for the last minute."),
        EX("Worked example 2: paragraph shape", intro="Write a critical paragraph on the shift in 'The Kettle'.", steps=[
            S("Point", text="The poem turns at 'Then' from lively sound to a hush."),
            S("Evidence", text="Before the turn the kettle 'sings' and the kitchen 'leans to listen'; after it there is 'silence' and 'steam'."),
            S("Effect", text="The change slows the rhythm and shifts the mood from comic to reflective."),
            S("Link to meaning", text="It leads to the last line's idea that silence can say more than song."),
        ]),
        MISTAKE("Spotting techniques without a point", "Listing alliteration, metaphor and rhyme is not criticism. Link each device to the effect and meaning."),
        MISTAKE("Assuming 'I' is the poet", "Say 'the speaker' or 'the narrator'. The speaker is a created voice."),
        MISTAKE("Writing prose when asked for poetry", "The report says many six-line poems were prose. Use line breaks, a pattern and compressed language."),
        MISTAKE("Ignoring the title", "A title is part of the text. Ask what it names, hints or ironises."),
        QUIZ("Which of these is most likely to signal a shift of tone in a poem?", [
            "A comma", "The word 'Yet' at the start of a stanza", "The poet's name", "A long line"], 1,
            "Connectives such as 'yet' and 'but' often signal a turn in mood or argument.",
            hint="Which of these changes the direction of the sentence?",
            feedback=["A comma only marks a pause.", "", "The poet's name is not part of the poem's meaning.", "Line length alone does not mark a shift."]),
        QUIZ("What is an imagery pattern?", [
            "A single metaphor", "A group of related images repeated through a text", "A rhyme scheme", "A change of narrator"], 1,
            "A pattern is a set of images belonging to one family that recur and build a theme.",
            hint="The word 'pattern' suggests something that recurs.",
            feedback=["One metaphor is a single image.", "", "Rhyme is a sound pattern, not an image pattern.", "That is a change of voice."]),
        PQ("Read 'The Kettle' again. Name two pieces of evidence for the unity of the poem.", "(1) The title names the subject that the poem follows from start to finish. (2) The poem begins with the kettle's song and ends by saying that silence and steam say more than the song, a return to the opening idea."),
        PQ("Explain the metaphor 'a small, impatient saint' in 'The Kettle'.", "The kettle is compared to a holy person who cannot wait. This gives the kettle a human, slightly comic dignity: it sings with a kind of devotion yet hurries to boil. The comparison makes an ordinary object seem charming and important."),
        PQ("List the six steps of the routine from memory.", "Read for sense; form and voice; shifts; images and sounds; structure and unity; answer each task."),
        SUM("Use the six-step routine every time: sense, form and voice, shifts, images and sounds, structure and unity, then the tasks.",
            "A shift is a turn of mood, subject, time or viewpoint; look for signal words and changes of image.",
            "An image pattern builds a theme; unity comes from repetition, return and a purposeful ending.",
            "Say 'the speaker', not 'the poet', and always link technique to effect and meaning.",
            "Plan your time with your teacher's paper timing and never leave creative tasks to the last minute."),
    ],
))

# ------------------------------------------------------------------ 8. Paper 1
LESSONS.append(lesson(
    module=M_EXAM, topic=T_P1,
    title="Paper 1 strategy: 50 multiple-choice questions on literary notions and set texts",
    slug="liu2-paper-1-strategy",
    minutes=22,
    summary="What the Board's 2023 report says Paper 1 contains (ten general literary appreciation questions and forty set-text questions), how to prepare for each, how to read options and how to use a mock paper to find weak topics.",
    objectives=[
        "State the structure of Paper 1 as the Board's 2023 report describes it",
        "Name the literary notions and language points the report says were tested",
        "Use a four-step method for text-bound multiple-choice questions",
        "Turn a mock result into a revision plan by topic",
    ],
    key_concepts=["Paper 1 structure", "General literary appreciation", "Text-bound questions", "Distractor", "Revision by topic"],
    blocks=[
        H("Introduction"),
        T("Paper 1 looks easy: you only choose A, B, C or D. In reality it tests whether you really know your texts and basic literary ideas, because a wrong option is written to match a common mistake. The student who has only read summaries is caught by the details."),
        T("The Board's 2023 report says this about the paper. It had **fifty multiple-choice questions**. The first ten were tagged **general literary appreciation** and were common to all candidates. The other forty were on the set texts, with **exactly four questions per text**. Because 2023 was a threshold year with an old and a new syllabus, there were separate sets of text questions for each, but the paper has the same standard structure. Check the number of set texts and the format with your teacher, because they change."),
        IMG("alliu2-paper-map.svg", alt="Three columns summarising Paper 1 (50 multiple-choice questions: 10 general appreciation and 40 on set texts), Paper 2 (essays in three sections, four answered) and Paper 3 (four compulsory questions with parts a to e).", caption="Figure 1. The three papers at a glance, from the Board's 2023 report."),
        H("The ten general questions"),
        T("The report says these tested basic literary notions on the major genres and sub-genres, and essential language awareness. It lists the topics: the purpose of literary criticism, realism in art, the structure and type of a drama, clues for identifying a novelist's purpose, types of oral prose forms, tone and related ideas, and metrical patterns. The two language questions were on grammar: the type and function of a pronoun, and the function of parts of a sentence."),
        KEY("Prepare these ten", "They are the same whatever your set texts are.", cards=[
            ["Genres", "Know drama, prose and poetry and their sub-genres: tragedy, comedy, novel, short story, ballad, elegy, ode."],
            ["Devices and tone", "Know common devices, tone and mood words, narrative point of view and the main metres (iamb, trochee, anapaest, dactyl)."],
            ["Oral prose", "Myth, legend, folktale, fable, proverb, riddle."],
            ["Grammar", "Pronoun types (personal, relative, reflexive) and sentence parts (subject, object, clause)."],
        ]),
        H("The forty text questions"),
        T("The report says the forty text-bound questions followed the assessment objectives: relevant background information, setting, plot, structure, style, thematic concerns, characterisation, stagecraft, mood and basics of creativity. So you must know the **facts** about each text, such as who says what to whom, where a scene is set, which event follows which, and what a device does."),
        D("A **distractor** is a wrong option written to look right. It usually matches a real fact from the text but in the wrong place, a character confusion, a common misreading, or a half-true statement.", title="Distractor"),
        H("A four-step method for a text question"),
        EX("Worked example 1: a method on a general question", intro="Question (written for practice): 'A narrator who tells the story using the pronoun I and who is a character in the events is called:' A) omniscient narrator B) first-person narrator C) third-person limited narrator D) objective narrator.", steps=[
            S("Cover the options and answer in your head", text="A character who says 'I' tells the story from the first person."),
            S("Match to an option", text="Option B."),
            S("Test the others", text="Omniscient and third-person limited both use third person; objective reports only what can be seen. None uses 'I'."),
            S("Choose and move on", text="B. If you were unsure, mark it and return."),
        ]),
        EX("Worked example 2: a text question where a distractor is tempting", intro="Question (written for practice): 'In The Canterbury Tales General Prologue, the pilgrims set out from:' A) Canterbury B) the Tabard Inn in Southwark C) Westminster Abbey D) Windsor Castle.", steps=[
            S("Cover the options", text="The pilgrims meet at an inn in Southwark, near London, before setting out for Canterbury."),
            S("Match", text="B."),
            S("Why A is a distractor", text="Canterbury is the destination, not the start. This is the classic confusion between origin and destination."),
        ]),
        TIP("Exam link: Paper 1 is a Board paper of 50 multiple-choice questions. Do the KKEVO Paper 1 mock exam A under timed conditions (the 90 minutes is a KKEVO practice setting) and then read the explanation for every wrong answer."),
        H("Reading options"),
        T("Read the stem fully, watch for words such as **not**, **except**, **best** and **most likely**, and check names: the report notes that candidates mix up characters. Eliminate options that are clearly wrong, then pick the one that matches the text best. The report does not say whether wrong answers lose marks, so check the rule with your teacher; in any case, never leave a question unanswered in a practice mock without thinking about it."),
        H("Turning a mock into a plan"),
        T("After a mock, make a table with four rows: African prose, Chaucer and canonical poetry, the poetry anthology, and unseen and general appreciation. Count your wrong answers in each row. Revise the row with the most errors first. The KKEVO mock tags each question with a topic so the results page shows your score by topic."),
        MISTAKE("Studying only plots", "The report says the text questions test setting, structure, style, mood and stagecraft as well as plot. Revise how each text is built and how each device works."),
        MISTAKE("Mixing up characters and texts", "Make a one-line card for each character: who, relation, key action. Test by covering the names."),
        MISTAKE("Ignoring the general ten", "These ten questions are the same for every candidate. They are the easiest to prepare for because the notions are fixed."),
        QUIZ("How many general literary appreciation questions does the Board's report say are in Paper 1?", [
            "Four", "Ten", "Twenty", "Forty"], 1,
            "The first ten of the fifty questions are general literary appreciation; the other forty are on the set texts.",
            hint="The paper has 50 questions in total, 40 of them on set texts.",
            feedback=["Four is the number of questions per text.", "", "That is not the structure the report gives.", "Forty is the number of set-text questions."]),
        QUIZ("What does the report say about the number of questions on each set text?", [
            "One", "Four", "Eight", "It varies widely"], 1,
            "The report says exactly four questions were set per text.",
            hint="Forty text questions divided by the number of texts.",
            feedback=["One would make too few questions.", "", "Eight is the number of Paper 2 set texts in the report.", "The report says exactly four."]),
        PQ("List four literary notions that the report says were tested in the ten general questions.", "Any four of: the purpose of literary criticism, realism in art, the structure and type of a drama, clues to a novelist's purpose, types of oral prose forms, tone and its related ideas, metrical patterns. (Grammar was also tested: pronoun type and function of sentence parts.)"),
        PQ("Explain why a student who has read only summaries of the set texts may lose marks in Paper 1.", "Distractors are built from real facts placed wrongly or from common misreadings, and the text questions cover setting, structure, style, mood and stagecraft, not only plot. A summary may not give such details."),
        PQ("Describe how you would use a mock paper score to plan revision for the next week.", "Group wrong answers by topic (the KKEVO results page does this), choose the weakest topic, re-read the relevant lesson, redo the practice set of that lesson, and retake only those questions in a few days. Repeat the cycle with the next weakest topic."),
        SUM("Paper 1 has 50 multiple-choice questions: 10 general literary appreciation and 40 on set texts, four per text (Board's 2023 report).",
            "The ten general questions cover literary notions, tone, metre, oral prose forms and basic grammar.",
            "The text questions cover background, setting, plot, structure, style, themes, character, stagecraft and mood.",
            "Use the four-step method: answer in your head, match, test the other options, choose.",
            "Use mock results by topic to plan revision."),
    ],
))

# ------------------------------------------------------------------ 9. Paper 2
LESSONS.append(lesson(
    module=M_EXAM, topic=T_P2,
    title="Paper 2 strategy: choosing questions and writing essays on the set texts",
    slug="liu2-paper-2-strategy",
    minutes=24,
    summary="How Paper 2 works (sections on drama, prose and poetry, four essays), how to read command words, choose questions, plan, write focused paragraphs and avoid the faults the Board's 2023 report lists, with a model plan and timing advice.",
    objectives=[
        "State the structure of Paper 2 as the Board's 2023 report describes it",
        "Choose four questions that obey the section and text rules",
        "Interpret command words and the blended focus of a question",
        "Plan and write an essay with a focused introduction, developed body and logical conclusion",
    ],
    key_concepts=["Sections A, B and C", "Choosing questions", "Command word", "Topic sentence and illustration", "Critical perspective", "Instruction errors"],
    blocks=[
        H("Introduction"),
        T("In Paper 2 you write, so everything depends on how well you choose, plan and develop. The Board's 2023 report says Paper 2 is based on the set books and is divided into **Section A (drama), Section B (prose) and Section C (poetry)**. Two questions were set on each text, giving sixteen questions in 2023, and candidates chose **four: one from each section and a fourth from any section, on a different text**. Check the current instructions with your teacher and on your question paper."),
        T("The African prose and poetry texts and the Chaucer or canonical poetry text you study in Upper Sixth appear here. So do the drama texts you studied in Lower Sixth. Your revision must cover all your set texts."),
        H("How the report describes the questions"),
        T("The report describes many tasks. Some ask you to discuss characters and their conflicts; some ask for the effectiveness of a device such as suspense, symbolism, allusion, apostrophe or an episode; some ask about a theme with a belief or a philosophy behind it; some ask about background, such as the historical or cultural setting; and some ask for short notes on listed items. It also notes that many questions blend two things, such as setting with theme or plot with style, and that one-, two- and three-star questions are set in a fixed ratio, so the paper includes easier and harder items."),
        KEY("Question types you will meet", "Know what each wants.", cards=[
            ["Character or conflict", "Judge a character's role, strengths or causes of failure, giving proofs and other characters' influence."],
            ["Theme or philosophy", "Discuss a theme and the ideas behind it, such as colonialism, assimilation or the American Dream, using several texts or scenes."],
            ["Technique", "Discuss the effectiveness of a device: what it is, where it appears, how it affects the plot, character or theme."],
            ["Background and context", "Show how the setting, history and culture shape the text."],
            ["Short notes", "Write brief, exact notes on listed items. Do not write more items than the question allows."],
        ]),
        H("Reading the question"),
        D("**Command tags** such as examine, how far, do you agree, to what extent, how true, justify and discuss tell you what to do. The report advises teaching candidates their meanings early in the course. 'Do you agree' or 'to what extent' demands a judgement with a case for and a case against.", title="Command tags"),
        T("The report's most common complaint is that candidates 'misinterpret' the question, narrate irrelevant material or ignore the terms of the question. In one example about suspense in a play, many candidates simply told the story and did not show how suspense developed other literary elements. In another, candidates mistook characters who serve rich whites for characters who conform to the white world, because they did not read the focus."),
        H("Choosing four questions"),
        T("Spend about five minutes at the start choosing. For each question that interests you, underline the command tag and the focus and ask: Do I know enough texts, poems or scenes for this? Do I obey the section and text rules? Which four give me the best proof? The report warns that some candidates answer more than the stipulated number of questions or choose two questions from the same section or the same text against the rules. Doing so wastes marks."),
        H("A planning and writing routine"),
        EX("Worked example 1: a plan for a technique question", intro="Question (written for practice): 'Examine the use of symbolism in a prose text you have studied.' Make a plan using an invented text placeholder.", steps=[
            S("Underline", text="Command tag: examine. Focus: symbolism. One text."),
            S("Thesis", text="[Writer] uses symbols such as [symbol 1] and [symbol 2] to express [theme], and the symbols develop with the plot."),
            S("Paragraph 1", text="Symbol 1: where it appears, what it stands for, how it affects the theme or a character."),
            S("Paragraph 2", text="Symbol 2: the same three questions."),
            S("Paragraph 3", text="Symbol 3 or a change of the symbol across the text, showing development."),
            S("Evaluation and conclusion", text="Judge the symbolism's effectiveness: what does the text gain? Does one symbol matter most?"),
        ]),
        EX("Worked example 2: a paragraph that earns marks", intro="Show the structure of one body paragraph with placeholders.", steps=[
            S("Topic sentence", text="[Writer] presents [symbol] as a sign of [idea]."),
            S("Illustration 1", text="In [scene], [short exact detail from your copy]."),
            S("Illustration 2", text="Later, when [event], the symbol [changes or returns]."),
            S("Illustration 3", text="[Another detail if available.]"),
            S("Comment and link", text="This shows [effect on theme or character], which answers the question because [link]."),
        ]),
        T("The report stresses that one sketchy illustration in a paragraph earns a skimpy mark: the more full and focused illustrations a paragraph has, the better the impression and mark. Develop each point."),
        H("Essay structure and language"),
        T("The report asks for a focused introduction, a body that fully develops the terms of the question, and a conclusion with logical finality. It adds: use linking words to keep the flow, write a clear plan and cross it out neatly, write in clear handwriting and acceptable English, put titles correctly, indent long quotations, and give the right author for each work."),
        T("The report also says the genres are not hermetic: drama, prose and poetry share techniques such as symbolism, irony and characterisation. When you revise, ask how a technique in one genre helps you understand another."),
        TIP("Exam link: Paper 2 is the essay paper on the set texts in three sections. The KKEVO Paper 2 practice paper A tests planning, key points and technique through auto-marked questions, because essays cannot be machine-marked. Use it to practise planning, then write real essays and have your teacher mark them."),
        MISTAKE("Narrating instead of answering", "The report calls this the weakest answer type. Every paragraph should begin with a point that answers the question."),
        MISTAKE("Answering too many questions", "Extra answers are thin. Answer the number asked and make each one strong."),
        MISTAKE("Forgetting the critical perspective", "A good answer shows how a technique or character affects other elements of the text, such as theme or plot. The report calls this the critical perspective."),
        MISTAKE("Leaving the text half-studied", "The report warns that texts not completed in class leave candidates with too few facts. Finish every text, including the poems."),
        QUIZ("Which choice of four questions obeys the section rule described in the Board's report?", [
            "Two from Section A, two from Section B", "One from each section and a fourth from any section but a different text", "All four from Section C", "Four on the same text"], 1,
            "The report says: one question from each section and a fourth from any section, but from a different text.",
            hint="Think 'one from each' first.",
            feedback=["That leaves out Section C.", "", "That breaks the one-from-each-section rule.", "The fourth must be on a different text."]),
        QUIZ("A question says 'To what extent do you agree?' What must your essay contain?", [
            "Only agreement", "A judgement with reasons on both sides", "A summary of the plot", "A list of devices"], 1,
            "'To what extent' calls for a judgement that considers both agreement and limits.",
            hint="The phrase asks for degree, not yes or no.",
            feedback=["It would ignore the limits.", "", "A summary does not answer the question.", "A list of devices lacks argument."]),
        PQ("Write a thesis sentence for: 'Discuss the importance of setting in a text you have studied.' Use placeholders.", "Model: 'In [text], [writer] makes [place] more than a background: it shapes [character] and expresses [theme], as [two examples] show.'"),
        PQ("Explain why a paragraph with one illustration earns fewer marks than one with three, according to the report.", "The report says that a sketchy illustration earns a skimpy mark and that fuller, more focused illustrations improve the impression and the mark. Several apt details prove the point more convincingly."),
        PQ("List four faults the Board's report notes in weak Paper 2 answers.", "Any four of: misunderstanding the question; narrating the plot; irrelevant material; no illustrations or thin ones; poor knowledge of the text; weak structure and no conclusion; poor language; answering more than the required number; choosing two questions from the same section or text; failing to discuss effectiveness."),
        SUM("Paper 2: sections on drama, prose and poetry; four essays, one from each section and a fourth from a different text (Board's 2023 report; check your paper).",
            "Read the command tag and focus; many questions blend two elements, so answer both.",
            "Plan with a thesis, three or four points and a judgement.",
            "Write paragraphs with a topic sentence, several illustrations and a comment.",
            "Use clear language, obey instructions and finish all your texts in revision."),
    ],
))

# ------------------------------------------------------------------ 10. Paper 3
CONTEXT_EXTRACT = ("**Invented extract (not from any set text)**\n\n"
                   "MAMA ABENG: (setting down the water pot) You have counted the money three times, and it has not grown.\n"
                   "TAKU: (not looking up) It will grow if I count it a fourth time.\n"
                   "MAMA ABENG: Money is like a goat, my son. It does not come to the one who shouts at it.\n"
                   "(A long silence. A radio plays faintly offstage.)\n"
                   "TAKU: Then what must I do, Mama?")

LESSONS.append(lesson(
    module=M_EXAM, topic=T_P3,
    title="Paper 3 strategy: context questions, unseen prose and poetry, and the (a) to (e) tasks",
    slug="liu2-paper-3-strategy",
    minutes=24,
    summary="Paper 3 has four compulsory questions each divided into sub-tasks (a) to (e): two context questions on drama texts and two appreciation questions on unseen prose and poetry; this lesson gives a method for each kind of sub-task and a plan for the creative and real-life tasks.",
    objectives=[
        "State the structure of Paper 3 as the Board's 2023 report describes it",
        "Answer a context question: place the extract, then deal with language, content, style and stagecraft",
        "Recognise the types of (a) to (e) sub-tasks, including creative and real-life ones",
        "Spread your effort across four compulsory questions",
    ],
    key_concepts=["Compulsory questions", "Sub-tasks (a) to (e)", "Context question", "Stagecraft", "Creative task", "Competency Based Approach"],
    blocks=[
        H("Introduction"),
        T("Paper 3 is the practical paper, and all four questions are compulsory. The Board's 2023 report says it had two context questions on drama texts and two literary appreciation questions on unseen prose and poetry. Each of the four was divided into sub-tasks lettered (a) to (e), some with sub-parts, to cover critical concepts, techniques, language skills, stagecraft and creativity. Because every question must be attempted, a weak area costs you directly."),
        T("The report gives a sobering picture: performance in Paper 3 was low overall, and poetry appreciation was the weakest question. It adds that questions in this paper need a combination of all six cognitive skills, from knowledge to evaluation. This lesson shows how to prepare."),
        H("The four questions"),
        CODE("Question 1 and 2: context questions on two prescribed drama texts (the texts depend on the syllabus).\n"
             "Question 3: unseen prose appreciation, sub-tasks (a) to (e).\n"
             "Question 4: unseen poetry appreciation, sub-tasks (a) to (e).", "text", title="Structure according to the 2023 report (check with your teacher)"),
        T("The report says the first sub-task in the questions was often a language skill, such as the meaning of words in context or a grammar point. Sub-tasks (b), (c) and (d) in the context questions covered content, style, plot or plot development, character, the ethos of an era, mood, attitude or tone, and stagecraft. Sub-task (e) was based on stagecraft (production, gestures, realism of action) or on a real-life or creative task reflecting the Competency Based Approach: for example writing a report, showing efficient conflict-resolution skills, or writing a six-line poem."),
        H("Context questions"),
        D("A **context question** gives a short extract from a play and asks about it. First place the extract: who is speaking, to whom, where in the play, and what has just happened or is about to happen. Then answer the tasks: meaning, content, style, character, tone, stagecraft and significance.", title="Context question"),
        T(CONTEXT_EXTRACT),
        EX("Worked example 1: a context question on the invented extract", intro="(a) Give the meaning in context of 'does not come to the one who shouts at it'. (b) What do we learn about Taku? (c) How do the stage directions help the scene? (d) What is the tone of the exchange? (e) In two or three sentences, advise Taku as a friend.", steps=[
            S("(a)", text="Money (like a goat) cannot be forced or frightened to come; gaining it needs calm, patient and wise action, not anger."),
            S("(b)", text="He is anxious and stubborn about money. He keeps counting it, answers his mother sharply, and finally asks for help, which shows that he is willing to learn."),
            S("(c)", text="'Not looking up' shows his unwillingness to face her; 'setting down the water pot' shows the mother's calm authority; 'a long silence' and the faint radio create a pause in which the point sinks in."),
            S("(d)", text="At first tense and sharp; then gentle and reflective, ending in humble questioning."),
            S("(e)", text="'Taku, count less and plan more. Save a little each week, ask your mother how she managed in hard seasons, and give the money time to grow.'"),
        ]),
        H("Stagecraft"),
        D("**Stagecraft** is the practical art of making a play work on stage: the set, props, lighting, sound, costume, movement, gesture, entrances and exits, pauses and silences. A stagecraft answer says what is done and what effect it has on the audience.", title="Stagecraft"),
        T("The report says sub-task (e) often tested stagecraft or real-life tasks. Prepare by imagining your set plays in performance: How would you stage the key scene? What would a pause or a gesture add? In an exam, name the element (a prop, a silence), say where it occurs and explain its effect."),
        H("Unseen prose and poetry in Paper 3"),
        T("The earlier lessons of this module teach the skills for Questions 3 and 4. The report describes prose tasks such as meaning in context, citing evidence, substantiating a view, attitude from short phrases and identifying skills; and poetry tasks such as a meaning in about 150 words with tone, words in context, a sound device and a metaphor, the rhyme scheme and effect, and a six-line creative response."),
        H("Spreading effort"),
        T("All four questions are compulsory, so a blank earns nothing. The report's figures showed prose appreciation doing better than poetry, but both were weak. Give each question the time its marks deserve and do not spend half the paper on your favourite. Always attempt the creative sub-task: even a modest, correct six-line poem scores something, and examiners reward form."),
        MISTAKE("Skipping the place-the-extract step", "Many wrong answers come from forgetting who speaks, to whom and when. Write one line placing the extract before anything else."),
        MISTAKE("Naming stagecraft without effect", "'There is a pause' scores nothing. Say what the pause does for the audience."),
        MISTAKE("Leaving creative tasks blank", "They are part of the paper and test the skills the Board calls competencies. Plan a short poem or report quickly and attempt it."),
        MISTAKE("Writing outside the task", "A sub-task asking for tone does not ask for the plot. Answer the question that is asked."),
        QUIZ("According to the Board's report, how many questions are compulsory in Paper 3?", [
            "One", "Two", "Four", "Choose any three"], 2,
            "The report says Paper 3 has four compulsory questions, each divided into sub-tasks (a) to (e).",
            hint="The paper has two context questions and two appreciation questions.",
            feedback=["One would not cover context and appreciation.", "Two is the number of context questions.", "", "There is no choice in Paper 3."]),
        QUIZ("Which of these is a stagecraft comment on the invented extract?", [
            "Taku is stubborn", "The long silence and the faint radio give the audience time to feel the weight of the mother's advice", "The language is simple", "Mama Abeng is a good character"], 1,
            "A stagecraft comment names a theatrical element and its effect on the audience.",
            hint="Which answer names something done on stage and its effect?",
            feedback=["That is a character comment.", "", "That is a style comment.", "It is a character opinion without evidence."]),
        PQ("Place the invented extract: say who speaks, to whom, and what the scene is about.", "Mama Abeng speaks to her son Taku in a family home. The scene is about Taku's worry over money and his mother's calm advice that patience, not anger, brings success."),
        PQ("Write a short (about 40-word) reply for the (e) task of the invented extract: 'Write a brief note from Taku to a friend about what he learned.'", "Model: 'Dear friend, today my mother showed me that anxiety does not make money grow. I will plan, save weekly and ask for advice. I am grateful she spoke plainly. I hope you find a calm way to handle your own worries too.'"),
        PQ("List the kinds of sub-task that the report says appear in Paper 3 as (a) to (e).", "Language skills (meaning in context, grammar), content, style, plot and character, ethos of an era, mood, attitude and tone, stagecraft, and real-life or creative tasks such as a report, conflict-resolution skills or a six-line poem."),
        SUM("Paper 3: four compulsory questions; two context questions on drama and two unseen appreciation questions, each with sub-tasks (a) to (e) (Board's 2023 report).",
            "For context questions, place the extract first, then answer each sub-task precisely.",
            "Stagecraft answers name the element, where it occurs and its effect on the audience.",
            "Practise creative and real-life tasks: they reflect the Competency Based Approach.",
            "Spread your time: all four questions are compulsory."),
    ],
))
