"""A Level French (0745), Lower Sixth: La Dissertation de Culture Générale (4 lessons), Panorama de la Littérature Française et Francophone
(5 lessons) and Examination (Paper 1, Paper 2, Paper 3).

Taught in English for Anglophone learners; every French example, extract, poem and model answer was written for these lessons (the poem
'Le flamboyant' and all passages are original and invented). Facts about the examination come from the Board's 2023 Advanced Level subject
report (paraphrased; no past-paper content, no mark splits). Literary facts (authors, titles, dates) are limited to well-established ones;
the works named in the Board's report (Baudelaire, Marivaux, Césaire, Hugo, Nkoa Atenga, Bebey) get method and study frameworks, to be
checked against the student's own copy and teacher.
"""

from .dsl import *  # noqa: F403

COURSE = ("french", "lower-sixth")

M_DIS = "La Dissertation de Culture Générale"
M_PAN = "Panorama de la Littérature Française et Francophone"
M_EXAM = "Examination"

T_SUJET = "Analyser le sujet"
T_PROB = "La problématique"
T_PLANS = "Les plans dialectique et thématique"
T_REDIG = "Rédiger la dissertation"
T_CLASS = "Le classicisme"
T_LUM = "Le siècle des Lumières"
T_ROM = "Le romantisme"
T_REAL = "Le réalisme et le naturalisme"
T_NEG = "La négritude et la littérature post-indépendance"

OWNCOPY = ("**Use your own copy and your teacher's notes.** This lesson gives dates and titles that are well established and a method; "
           "any detail you use in an essay must be checked against your own textbook, because syllabus texts and editions differ.")

LESSONS = []

# ------------------------------------------------------------------ 1. Analyser le sujet
LESSONS.append(lesson(
    module=M_DIS, topic=T_SUJET,
    title="Analyser le sujet : mots-clés, consignes et enjeu",
    slug="frl2-analyser-le-sujet",
    minutes=22,
    summary="Before writing a dissertation, read the sujet like a detective: find the key words, define them, spot the trap words (seul, toujours, tout), obey the instruction and name what is at stake (l'enjeu).",
    objectives=[
        "Say what a dissertation de culture générale is and recognise the main kinds of sujet",
        "Underline the key words of a sujet and define each one with its nuances",
        "Spot limiting words and instructions (consignes) that change the question",
        "Rewrite a sujet in your own words and state its enjeu",
    ],
    key_concepts=["Dissertation", "Sujet", "Mots-clés", "Consigne", "Mots-pièges", "Enjeu", "Hors-sujet"],
    blocks=[
        H("Introduction"),
        T("Imagine a debate week in a school in Buea. The topic is shown on the board: « Le livre numérique peut-il remplacer le livre traditionnel ? » One student starts speaking about computers in general. Another talks about the tradition of reading under a mango tree. A third answers the actual question. Only the third will score well. The Board's 2023 report for this subject says the same about essay questions on life situations: many candidates did not understand the question, wrote on a neighbouring subject, or had the ideas but not the French to express them."),
        T("A **dissertation de culture générale** is an argued essay on a general subject (society, technology, education, health, development, culture). You do not simply tell what you know. You answer a question, with arguments and examples, in a clear structure. The first step is always the same: **analyser le sujet**."),
        T("In this course the dissertation method is the backbone of every French essay you write. In the Board's Paper 3 the essay questions are life situations (a debate, a talk, a report), so the same analysis will help you there too. Check the exact format with your teacher."),
        H("What kinds of sujet exist?"),
        KEY("Three common kinds of sujet", "Name the kind first. It tells you what the examiner expects.", cards=[
            ["La question", "« Le numérique peut-il remplacer le livre ? » You answer the question and you must justify the answer."],
            ["La citation ou l'affirmation", "« Seule l'éducation sort un pays du sous-développement. » The sentence is a thesis. You discuss it: is it true, partly true, false?"],
            ["La situation", "« Lors d'une conférence, vous parlez des mesures contre une pandémie. » A role is given (speaker, student, journalist). You answer inside that role."],
        ]),
        D("Le **sujet** is the whole text of the question. Its **mots-clés** are the words that carry the meaning (nouns, verbs, adjectives). The **consigne** is the instruction (Discutez, Expliquez, Êtes-vous pour ou contre ?). L'**enjeu** is what is at stake: the real debate hidden behind the words.", title="Vocabulary of the sujet"),
        H("The four steps of analysis"),
        T("**Step 1: read twice and underline.** Underline the key words and circle the small words that limit the idea (seul, toujours, tout, ne... que, uniquement, jamais). **Step 2: define each key word**, with its nuances: what does it include and what does it leave out? **Step 3: find the relation between the terms** and the consigne: cause, opposition, restriction, comparison. **Step 4: rewrite** the sujet in one clear sentence of your own and state the enjeu."),
        IMG("alfrl2-sujet-plan-flow.svg", alt="Flow of a dissertation: sujet, key words, tension, problématique, plan, conclusion, each step feeding the next.", caption="Figure 1. The path of a dissertation. Analysing the sujet is the first box; every later step depends on it."),
        KEY("Mots-pièges : the small words that change the question", "A limiting word can turn an easy sujet into a very different one.", cards=[
            ["seul, uniquement, ne... que", "They claim there is only one cause. Your answer must test this claim (are there other causes?)."],
            ["toujours, jamais, tout, tous", "They claim a rule without exception. One good counter-example is enough to discuss it."],
            ["peut-il, doit-on, faut-il", "Possibility, duty and necessity are different questions. Do not answer « it exists » when asked « should it? »."],
            ["dans votre pays, de nos jours", "These words limit time and place. Your examples must come from there."],
        ]),
        KEY("Consignes you will meet", "Each consigne asks for a slightly different movement.", cards=[
            ["Discutez / Qu'en pensez-vous ?", "Examine the idea from several sides, then take a reasoned position."],
            ["Expliquez et commentez", "First explain what the idea means, then comment on whether it is valid."],
            ["Dans quelle mesure... ?", "Up to what point? The answer is usually « partly », with conditions."],
            ["Êtes-vous pour ou contre ?", "Choose a side clearly (in a debate), but still answer the other side's best argument."],
        ]),
        EX("Worked example 1 : une question", intro="Sujet (written for practice): « Le livre numérique peut-il remplacer le livre traditionnel ? » Analyse it.", steps=[
            S("Underline the key words", text="livre numérique, peut-il remplacer, livre traditionnel."),
            S("Define", text="Livre numérique: a book read on a screen (tablet, phone, e-reader). Livre traditionnel: the printed paper book. Remplacer: take the place of completely, not only coexist."),
            S("Spot the trap", text="« Remplacer » is strong. The sujet is not « Le numérique est-il utile ? » but « Can it take the place of paper entirely ? »"),
            S("Find the relation", text="There is an opposition (digital against paper) and a degree (replace, not complete)."),
            S("Rewrite", text="Can screens entirely take the place of printed books in reading and education ?"),
            S("State the enjeu", text="Access to books and cost against the quality of reading, culture and equal chances."),
        ]),
        EX("Worked example 2 : une affirmation", intro="Sujet (written for practice): « Seule l'éducation peut sortir l'Afrique du sous-développement. » Analyse it.", steps=[
            S("Underline", text="seule, éducation, sortir, sous-développement. Circle « seule »."),
            S("Define", text="Éducation: schooling and also training and culture. Sous-développement: low income, weak health, poor roads and energy, little industry (several indicators, not only money)."),
            S("The trap", text="« Seule » means education alone. A good essay tests this: do health, roads, energy, good government and trade also matter?"),
            S("Consigne", text="No verb of instruction, so it is an affirmation to discuss: is it true, partly true or false ?"),
            S("Rewrite", text="Is education the only key to development, or one key among several ?"),
            S("Enjeu", text="The place of education among the other conditions of development."),
        ]),
        H("Practical tips"),
        T("Spend about five minutes on the analysis. This is a suggested use of time, not a Board rule. Write on your rough page: the key words with their definitions, the limiting words, the consigne, your rewrite and one sentence for the enjeu. If you cannot rewrite the sujet in your own words, you have not understood it yet."),
        T("Do not copy a lesson you learned. A **récitation de cours** (writing everything you know about the subject) is a form of **hors-sujet**, an answer to a different question."),
        MISTAKE("Answering the topic, not the question", "A candidate sees « numérique » and writes on computers, or sees « pandémie » and describes the history of diseases. Always answer the exact question asked, with its limits."),
        MISTAKE("Ignoring the little words", "« Seul », « toujours », « tout » and « dans votre pays » carry the debate. Underline them before anything else."),
        MISTAKE("Mixing up close words", "The Board's report notes that candidates confused épidémie (a disease spreading in one region) with pandémie (a disease spreading over several continents). Define every technical word exactly."),
        TIP("Exam link: Paper 3 (essay questions are life situations in French; the report says language and understanding of the question decide the mark). The same analysis helps in Paper 2 literature questions that give a statement to discuss with the text. Check the exact format with your teacher."),
        QUIZ("Sujet : « Les réseaux sociaux détruisent toujours les relations humaines. » Which word makes the sujet most easy to challenge?", [
            "réseaux sociaux", "relations humaines", "toujours", "détruisent"], 2,
            "« Toujours » claims no exception. A single example of social media helping people stay in touch shows the claim is too strong, which opens the discussion.",
            hint="Look for the word that says « without exception ».",
            feedback=["It names the topic. It is a key word, but it does not limit the claim.", "It names what is affected. It is not the limiting word.", "", "It is the main verb and an extreme verb, but the absolute word is « toujours »."]),
        QUIZ("Which rewrite keeps the meaning of « Seule l'éducation sort un pays du sous-développement » ?", [
            "L'éducation est utile au développement.", "Sans éducation, aucun pays ne peut se développer, et rien d'autre ne suffit.", "Les pays riches sont éduqués.", "Le sous-développement est un problème."], 1,
            "The rewrite must keep the idea of exclusivity (only education). The first rewrite weakens it, the third and fourth change the subject.",
            hint="Does your rewrite still say « only » ?",
            feedback=["It weakens « seule » to « useful ». That is a different sujet.", "", "It speaks of rich countries, not of the cause of development.", "It states a fact and drops the claim about education."]),
        PQ("Analyse the sujet : « Les nouvelles technologies rendent-elles les jeunes moins cultivés ? » (key words, trap, consigne, rewrite, enjeu).",
           "Key words: nouvelles technologies, rendent... moins, jeunes, cultivés. Define: nouvelles technologies = phones, internet, social media, computers; jeunes = teenagers and young adults; cultivés = having knowledge, taste and critical sense, not only school marks. Trap: « moins » asks for a comparison with before, and « cultivés » is not the same as « informés ». Consigne: a closed question (yes or no) to be discussed. Rewrite: Does the use of new technologies lower young people's culture ? Enjeu: access to knowledge against distraction and shallow reading."),
        PQ("Which kind of sujet is this: « Vous participez à un débat sur la lutte contre la famine. Que proposez-vous ? » What must you do?",
           "It is a **situation** (a debate with a role). You speak as a participant in a debate, so you give clear proposals (causes, solutions, who acts) in a speaking tone, with arguments and examples, and you address the audience. The analysis still asks for the key word (famine), its causes and the limits of your proposals."),
        PQ("Explain the difference between épidémie and pandémie and why it matters in a sujet on a pandemic.",
           "An épidémie spreads quickly within a region or country. A pandémie spreads over several continents or the whole world. If the sujet asks for measures against a pandémie, your examples and measures must be global (borders, international cooperation, vaccines), not only local. Using the wrong word shows a weak understanding of the sujet."),
        SUM("A dissertation answers a question with arguments and examples; analysing the sujet comes first.",
            "Underline key words, define them, and circle limiting words such as seul, toujours, tout and dans votre pays.",
            "Obey the consigne (discutez, expliquez, dans quelle mesure, pour ou contre).",
            "Rewrite the sujet in your own words and state the enjeu before you plan.",
            "Avoid hors-sujet: answer the exact question, not the topic, and do not recite a lesson."),
    ]))

# ------------------------------------------------------------------ 2. La problématique
LESSONS.append(lesson(
    module=M_DIS, topic=T_PROB,
    title="La problématique : trouver la tension et poser la question",
    slug="frl2-problematique",
    minutes=22,
    summary="A problématique is the central question of your essay, born from a tension in the sujet. Learn to find the tension, phrase the question in French, test it, and make the plan answer it.",
    objectives=[
        "Define the problématique and say how it differs from the sujet and from the plan",
        "Find the tension (paradox, opposition, limit) inside a sujet",
        "Write a clear problématique in one or two sentences, with the usual French formulas",
        "Test a problématique and correct the four most common faults",
    ],
    key_concepts=["Problématique", "Tension", "Question ouverte", "Formules de problématisation", "Lien avec le plan"],
    blocks=[
        H("Introduction"),
        T("A good doctor does not treat « the whole body ». The doctor asks a precise question: where does it hurt, and why? A good essay does the same. After analysing the sujet you must decide **what exact question your essay will answer**. That question is the **problématique**. It is the engine of the dissertation: the plan answers it, and the conclusion returns to it."),
        D("La **problématique** is the central question, or small group of linked questions, that a sujet raises and that the whole essay tries to answer. It comes from a **tension**: two ideas that both seem true but pull in different directions.", title="Definition"),
        T("Do not confuse three things. The **sujet** is what the examiner gives you. The **problématique** is the question you build from it. The **plan** is the path of arguments that answers it."),
        H("Finding the tension"),
        T("Most sujets contain a tension. Look for one of these: an **opposition** (advantages against dangers), a **paradox** (something useful that also harms), a **limit** (true in some cases, false in others) or a **condition** (possible only if something else exists). Ask yourself two questions: « Why would someone say yes ? » and « Why would someone say no ? » The space between the two answers is your problématique."),
        EX("Worked example 1 : trouver la tension", intro="Sujet (written for practice): « Le livre numérique peut-il remplacer le livre traditionnel ? »", steps=[
            S("Why yes?", text="Cheaper to share, light to carry, thousands of titles on one phone, useful where bookshops are rare."),
            S("Why no?", text="Not everyone has a device or electricity or data; paper is easier on the eyes and on memory; a printed library is a shared cultural heritage."),
            S("Name the tension", text="Wider access through screens against the loss of the qualities of paper and unequal access to devices."),
            S("Phrase the question", text="Dans quelle mesure le livre numérique peut-il remplacer le livre traditionnel sans appauvrir la lecture ni creuser les inégalités d'accès ?"),
        ]),
        KEY("Formulas for the problématique", "Choose one that fits the sujet. They all invite a nuanced answer.", cards=[
            ["Dans quelle mesure... ?", "Up to what point is the claim true? Ideal for strong affirmations."],
            ["Peut-on... ? / Faut-il... ?", "Possibility or duty, followed by the conditions or limits."],
            ["Comment concilier... et... ?", "How to reconcile two aims that seem opposed (progress and tradition)."],
            ["Est-il vrai que..., ou... ?", "True, or the opposite? Often used to test a popular belief."],
        ]),
        H("Four tests of a good problématique"),
        T("**1. It is open.** It cannot be answered only by « oui » or « non »: it needs a reasoned answer. **2. It uses the terms of the sujet**, not a different subject. **3. It is short**: one or two sentences. **4. It leads to the plan**: you should be able to see two or three parts that answer it."),
        EX("Worked example 2 : une affirmation", intro="Sujet (written for practice): « Seule l'éducation peut sortir l'Afrique du sous-développement. » Build the problématique.", steps=[
            S("Why yes?", text="Education gives skills, health knowledge, good citizens and innovation."),
            S("Why no?", text="Schools cannot work without roads, energy, health, stable institutions and fair trade; some educated people leave the country (brain drain)."),
            S("Tension", text="Education seems essential, yet it cannot act alone."),
            S("Problématique", text="L'éducation est-elle la seule condition du développement de l'Afrique, ou doit-elle s'accompagner d'autres changements ?"),
            S("Check the plan", text="Part 1: role of education. Part 2: its limits and other conditions. Part 3: how they work together. The question announces this path."),
        ]),
        EX("Worked example 3 : rejeter une mauvaise problématique", intro="For the sujet « Les réseaux sociaux détruisent toujours les relations humaines », a student writes: « Qu'est-ce que les réseaux sociaux ? » Correct it.", steps=[
            S("Diagnose", text="The question is a definition. It does not use « détruisent » or « toujours » and it has no tension."),
            S("Find the tension", text="Social media connect distant people, yet they may replace real conversation with screens."),
            S("Rewrite", text="Les réseaux sociaux rapprochent-ils vraiment les gens, ou remplacent-ils la conversation réelle par une présence apparente ?"),
        ]),
        H("Common faults"),
        MISTAKE("Turning the sujet into a question and stopping", "« Le livre numérique peut-il remplacer le livre ? » is only the sujet again. Add the tension: dans quelle mesure, à quelles conditions, au prix de quoi ?"),
        MISTAKE("A closed or too large question", "« Le numérique est-il bon ? » can be answered in one word, and « Qu'est-ce que la technologie ? » is far too large. Keep the limits of the sujet."),
        MISTAKE("A list of five questions", "A problématique is one main question, with at most one or two linked sub-questions. A long list hides the argument."),
        MISTAKE("A problématique that the plan does not answer", "If your problématique asks about « conditions » but your plan only lists advantages, the examiner sees a break. Write the plan to answer the question word for word."),
        TIP("Exam link: in the Board's Paper 3 essay on a life situation (debate, talk, report), the problématique may be short or implicit, but the idea is the same: you decide the exact question and answer it. Check the exact format with your teacher."),
        QUIZ("Which of these is the best problématique for « Les réseaux sociaux détruisent toujours les relations humaines » ?", [
            "Les réseaux sociaux sont-ils bons ?", "Qu'est-ce qu'un réseau social ?",
            "Dans quelle mesure les réseaux sociaux rapprochent-ils les gens sans appauvrir leurs relations réelles ?",
            "Les réseaux sociaux ont été inventés quand ?"], 2,
            "It is open, uses the terms of the sujet, expresses the tension (rapprocher against appauvrir) and suggests a plan.",
            hint="Which question contains both sides of the debate?",
            feedback=["Closed and vague: « bons » has no clear meaning.", "It is a definition question and has no tension.", "", "It is a factual history question, not an argument."]),
        QUIZ("A problématique must be...", [
            "a statement of your opinion", "a list of all the arguments", "an open question born from a tension", "the title of the essay"], 2,
            "It is a question born from a tension and answered by the plan.",
            hint="Think of the engine of the essay.",
            feedback=["Your opinion appears in the conclusion, not here.", "The arguments belong to the plan.", "", "A title is not a question to be answered."]),
        PQ("Build a problématique for the sujet : « La pandémie a-t-elle changé notre façon de vivre ? »",
           "Tension: real changes (hygiene, remote work and school, health systems) against habits that quickly returned, and changes that differ between rich and poor. Possible problématique: Dans quelle mesure la pandémie a-t-elle transformé durablement nos modes de vie, au-delà des mesures d'urgence ? Check: open, uses the terms (pandémie, façon de vivre), one sentence, and it leads to a plan (what changed / what did not last / what should remain)."),
        PQ("Correct this problématique for « Faut-il remplacer les livres papier par des tablettes à l'école ? » : « Les tablettes sont-elles bonnes ? »",
           "Faults: it is vague (« bonnes »), it ignores « remplacer » and « à l'école », and it has no tension. Better: Faut-il remplacer entièrement les livres papier par des tablettes à l'école, ou les deux supports peuvent-ils se compléter ? The tension is modern tools against the quality of learning and the cost of equipment."),
        PQ("For the sujet « Les dirigeants africains doivent agir pour sortir leurs pays du sous-développement », give a problématique and a three-part idea of the plan.",
           "Problématique: Quelles mesures les dirigeants africains doivent-ils prendre en priorité pour réduire le sous-développement, et à quelles conditions seront-elles efficaces ? Plan (thematic): 1. mesures politiques et institutionnelles (gouvernance, lutte contre la corruption); 2. mesures économiques et d'infrastructures (routes, énergie, agriculture); 3. mesures sociales et culturelles, d'abord l'éducation et la santé. The conclusion answers which priority comes first and what the leaders cannot do alone."),
        SUM("The problématique is the central question of the essay, born from a tension in the sujet.",
            "Find the tension by asking why someone would say yes and why someone would say no.",
            "Use a formula such as dans quelle mesure, peut-on, faut-il, comment concilier.",
            "Test it: open, uses the sujet's terms, short, and it leads to the plan.",
            "Avoid copying the sujet, closed questions, long lists and plans that do not answer the question."),
    ]))

# ------------------------------------------------------------------ 3. Les plans dialectique et thématique
LESSONS.append(lesson(
    module=M_DIS, topic=T_PLANS,
    title="Les plans dialectique et thématique : choisir et construire",
    slug="frl2-plans",
    minutes=24,
    summary="Build the skeleton of a dissertation: the dialectical plan (thèse, antithèse, synthèse) for debates and claims, the thematic plan for subjects with several aspects, and how to fill each part with arguments, examples and transitions.",
    objectives=[
        "Describe the dialectical plan and the real role of the synthèse",
        "Describe the thematic plan and when to prefer it (also the analytical plan)",
        "Choose the right plan for a given sujet and problématique",
        "Fill a plan with arguments and examples and link the parts with transitions",
    ],
    key_concepts=["Plan dialectique", "Thèse, antithèse, synthèse", "Plan thématique", "Plan analytique", "Argument et exemple", "Transition"],
    blocks=[
        H("Introduction"),
        T("A house needs a plan before the walls go up. A dissertation is the same. The problématique is the question; the **plan** is the path of arguments that answers it, part by part. In French writing two plans are used most: the **plan dialectique** and the **plan thématique**."),
        D("Le **plan dialectique** moves in three steps: la **thèse** (the idea is true, with arguments), l'**antithèse** (the idea has limits or is false, with arguments) and la **synthèse** (a reasoned answer that goes beyond both, with conditions and nuances).", title="Plan dialectique"),
        IMG("alfrl2-plan-dialectique.svg", alt="Three boxes in a row: thèse (yes, arguments and examples), antithèse (but, limits and objections), synthèse (answer with conditions), joined by arrows labelled transitions.", caption="Figure 1. The dialectical plan. Each box holds two or three arguments, and each argument has an example."),
        T("The **synthèse** is the most misunderstood part. It is not a repetition of the thesis and not a weak compromise like « both are good ». It is a **higher answer** that explains when the thesis is true and when the antithesis is true, or what condition reconciles them."),
        D("Le **plan thématique** groups the ideas by **themes or fields** (political, economic, social, cultural, educational, environmental...). Each part treats one aspect of the sujet. It suits sujets that ask what to do, what the causes are, what the consequences are, or any question that has several areas.", title="Plan thématique"),
        T("A close cousin is the **plan analytique**: causes, then consequences, then solutions. It is natural for a sujet such as « les conséquences du changement climatique » or « prévention et traitement d'une pandémie ». Check which names your teacher uses; the logic is the same: each part has one clear idea."),
        H("Which plan for which sujet?"),
        KEY("Choosing the plan", "Let the sujet decide. Do not force every essay into the same mould.", cards=[
            ["Affirmation or question with a yes-or-no tension", "Plan dialectique. Example: « Le livre numérique peut-il remplacer le livre ? »"],
            ["What should be done? Which measures?", "Plan thématique by fields. Example: « Que doivent faire les dirigeants pour réduire le sous-développement ? »"],
            ["Causes, effects, remedies", "Plan analytique (a kind of thematic plan). Example: « Le changement climatique : conséquences et réponses. »"],
            ["Debate role (for or against)", "A position-first plan: take your side, give strong arguments, then refute the best opposing argument (concession and rebuttal)."],
        ]),
        H("Filling the plan"),
        T("Each part contains **two or three arguments**. Each argument has the same small structure: **idée directrice** (one sentence), **explication** (why it is true), **exemple** (a fact, a case from Cameroon, Africa or the world, or a literary reference). An argument without an example is only an opinion; an example without an argument is only a story."),
        T("Between the parts, write a **transition**: one or two sentences that close the previous part and open the next. For example: « Si l'éducation joue un rôle essentiel, elle ne suffit pourtant pas à elle seule : il faut examiner les autres conditions. »"),
        EX("Worked example 1 : plan dialectique", intro="Sujet (written for practice): « Le livre numérique peut-il remplacer le livre traditionnel ? » Build a dialectical plan.", steps=[
            S("Partie 1 (thèse) : oui, le numérique offre des avantages décisifs", text="Argument 1: accès à beaucoup de titres à faible coût (example: a student with one phone can carry a library). Argument 2: facilité pour l'éducation à distance (example: lessons sent when schools are closed)."),
            S("Partie 2 (antithèse) : mais il ne peut pas tout remplacer", text="Argument 1: inégalités d'accès (appareils, électricité, connexion). Argument 2: qualité de la lecture (fatigue des yeux, distraction, mémoire). Argument 3: valeur culturelle du livre imprimé (bibliothèques, héritage)."),
            S("Partie 3 (synthèse) : vers une complémentarité", text="The two supports can live together if the conditions exist: numérique for access and quick reference, papier for deep reading and equal access; schools and libraries must keep both."),
            S("Transitions", text="Between 1 and 2: « Pourtant, ces avantages ne doivent pas faire oublier les limites du numérique. » Between 2 and 3: « Dès lors, le débat ne doit pas opposer, mais articuler les deux supports. »"),
        ]),
        EX("Worked example 2 : plan thématique", intro="Sujet (written for practice): « Que doivent faire les dirigeants africains pour sortir leurs pays du sous-développement ? » Build a thematic plan.", steps=[
            S("Partie 1 : sur le plan politique", text="Argument 1: gouvernance et institutions stables. Argument 2: lutte contre la corruption (example: contrôle transparent des budgets)."),
            S("Partie 2 : sur le plan économique", text="Argument 1: routes et énergie pour relier les marchés. Argument 2: soutien à l'agriculture et à la transformation locale des produits."),
            S("Partie 3 : sur le plan social et culturel", text="Argument 1: éducation pour tous, formation technique. Argument 2: santé et protection des plus pauvres."),
            S("Link and answer", text="Each part answers the same question (what must leaders do?); the conclusion ranks the priorities and notes that citizens, business and partners also act."),
        ]),
        H("Quality checks"),
        T("Before writing, test the plan: Are the parts balanced in size? Do the parts answer the problématique? Is each part different from the others (no overlap)? Does every argument have an example? Do you have transitions? In an exam, a plan of **two or three parts** is enough; a plan with five weak parts is worse than three strong ones."),
        MISTAKE("A synthèse that only repeats", "Writing « En conclusion, le numérique a des avantages et des inconvénients » is not a synthèse. Give a precise answer: under which conditions, for which group, up to which point."),
        MISTAKE("Unbalanced parts", "A very long thesis, a short antithesis and a one-line synthèse look like a one-sided essay. Aim for similar weight, with the synthèse the most refined."),
        MISTAKE("A list instead of a plan", "Writing « d'abord... ensuite... enfin... » with no link between the ideas gives a list. Each part must answer the problématique and each transition must say why we move on."),
        MISTAKE("Arguments without examples", "« L'éducation est importante » is an opinion. Add a fact, a case or a reference: a school programme, a country, a book. Keep examples accurate and do not invent statistics."),
        TIP("Exam link: use the dialectical plan for a for-or-against question and the thematic or analytical plan for « what should be done » and « consequences » questions, which the Board used in Paper 3 life situations. In a debate or speech, commit to a side early and still answer the best objection. Check the exact format with your teacher."),
        QUIZ("Sujet : « Quelles mesures prendre pour prévenir une pandémie et soigner les malades ? » Which plan fits best?", [
            "Un plan dialectique (thèse, antithèse, synthèse)", "Un plan analytique ou thématique (prévention, puis traitement)",
            "Un seul paragraphe sans parties", "Un plan chronologique de l'histoire des maladies"], 1,
            "The sujet asks for measures in two fields (prevention and care). A thematic or analytical plan by field is the natural answer.",
            hint="Is there a yes-or-no debate, or a question about what to do in several areas?",
            feedback=["The sujet has no yes-or-no tension to resolve.", "", "A dissertation needs a visible structure.", "History of diseases is not the question."]),
        QUIZ("What is the best description of a good synthèse?", [
            "It repeats the thèse in other words.", "It says that both sides are good.",
            "It answers the problématique with conditions and nuances that go beyond thèse and antithèse.", "It introduces a new, unrelated subject."], 2,
            "The synthèse is a reasoned answer: when the thèse holds, when the antithèse holds, under what conditions.",
            hint="Think of an answer you could defend.",
            feedback=["That is a repetition, not a synthèse.", "It is a weak compromise that answers nothing.", "", "It would leave the sujet unanswered."]),
        PQ("Give a dialectical plan (three part titles in French) for « La technologie rend-elle l'homme plus libre ? »",
           "1. La technologie libère l'homme (travail plus facile, information, mobilité). 2. Mais elle crée de nouvelles dépendances (écrans, surveillance, perte d'autonomie). 3. La liberté dépend de l'usage que l'homme en fait: éducation, règles, choix conscient. Each part needs two arguments with an example, and a transition before the next part."),
        PQ("Why is a thematic plan better than a dialectical plan for « Quelles solutions face au changement climatique ? »",
           "The sujet asks for solutions in several fields, not for a yes-or-no debate. A thematic plan by field (political and international, economic and technical, individual and educational) lets you give distinct measures. A dialectical plan would force an artificial for-and-against."),
        PQ("Write a transition between the thèse « le numérique facilite l'éducation » and the antithèse « le numérique creuse les inégalités ».",
           "« Si le numérique ouvre de grandes possibilités à ceux qui y ont accès, il laisse pourtant de côté tous ceux qui n'ont ni appareil, ni électricité, ni connexion : voyons maintenant ses limites. » A good transition summarises the first part and announces the problem that opens the next."),
        SUM("The plan dialectique has three moves: thèse, antithèse, synthèse; the synthèse is a reasoned answer, not a repetition.",
            "The plan thématique (or analytique) groups ideas by field; it suits « what to do », causes and consequences.",
            "Choose the plan the sujet and problématique require; in a debate, take a side and answer the best objection.",
            "Two or three balanced parts, each with two arguments and an example.",
            "Link the parts with transitions that summarise and announce."),
    ]))

# ------------------------------------------------------------------ 4. Rédiger la dissertation
LESSONS.append(lesson(
    module=M_DIS, topic=T_REDIG,
    title="Rédiger la dissertation : introduction, développement, conclusion",
    slug="frl2-rediger",
    minutes=25,
    summary="Write the finished essay: a four-move introduction (amorce, sujet, problématique, annonce), well-built paragraphs with connectors, a conclusion with bilan and ouverture, and clean French (faux amis, épidémie and pandémie, reread).",
    objectives=[
        "Write a four-move introduction in correct French",
        "Build a paragraph with idée directrice, explication, exemple and mini-conclusion",
        "Use connectors of addition, opposition, cause, consequence and concession correctly",
        "Write a conclusion with a bilan and an ouverture, and proofread for common errors",
    ],
    key_concepts=["Introduction en quatre temps", "Amorce", "Paragraphe argumentatif", "Connecteurs logiques", "Conclusion : bilan et ouverture", "Faux amis"],
    blocks=[
        H("Introduction"),
        T("You have analysed the sujet, built a problématique and chosen a plan. Now you must **write**, and here the Board's report makes a clear point about Paper 3: many candidates understood the topic but lacked the vocabulary and the control of grammar and sentence structure to say it well. A good essay therefore needs both a clear structure and clean French."),
        T("A dissertation has three visible parts: l'**introduction**, le **développement** (the plan) and la **conclusion**. Leave a blank line between the parts and start each new part of the plan on a new paragraph."),
        H("The introduction in four moves"),
        D("The introduction has four moves in this order: **l'amorce** (a short opening idea that leads to the topic), **la présentation du sujet** (quote or rephrase it), **la problématique** (the central question) and **l'annonce du plan** (the path you will follow).", title="Introduction en quatre temps"),
        EX("Worked example 1 : une introduction complète", intro="Sujet (written for practice): « Le livre numérique peut-il remplacer le livre traditionnel ? »", steps=[
            S("1. Amorce", text="« Depuis quelques années, il n'est plus rare de voir un élève lire un roman sur son téléphone plutôt que dans un livre imprimé. » Start from a real observation, not from « de tout temps ». Keep it to one or two sentences."),
            S("2. Présentation du sujet", text="« Cette évolution pose la question suivante : le livre numérique peut-il remplacer entièrement le livre traditionnel ? » Keep the key words."),
            S("3. Problématique", text="« Dans quelle mesure l'écran peut-il prendre la place du papier sans appauvrir la lecture ni creuser les inégalités d'accès ? »"),
            S("4. Annonce du plan", text="« Nous verrons d'abord les avantages décisifs du numérique, puis ses limites, avant de montrer que les deux supports peuvent se compléter. »"),
        ]),
        T("Write the introduction as **one paragraph** or four short sentences in one block. Do not number the moves. Do not give your whole answer yet: the conclusion will do that."),
        H("The development: paragraphs that argue"),
        D("A **paragraphe argumentatif** has four elements: **l'idée directrice** (the main point, usually in the first sentence), **l'explication** (why it is true), **l'exemple** (a fact or case) and **le mini-bilan** (a closing sentence that links to the problématique).", title="Paragraphe argumentatif"),
        EX("Worked example 2 : un paragraphe", intro="Write one paragraph for the argument « le numérique ne profite pas à tous » (partie 2).", steps=[
            S("Idée directrice", text="« D'abord, le numérique ne profite pas à tous. »"),
            S("Explication", text="« En effet, lire sur écran suppose un appareil, de l'électricité et une connexion, trois conditions qui manquent encore dans de nombreuses familles et dans certaines zones rurales. »"),
            S("Exemple", text="« Ainsi, dans un village où le courant est irrégulier, une tablette devient vite inutilisable alors qu'un livre imprimé se lit à la lumière du jour. »"),
            S("Mini-bilan", text="« Par conséquent, remplacer le papier par l'écran risquerait d'exclure ceux qui ont déjà le moins accès à la lecture. »"),
        ]),
        KEY("Connecteurs logiques à retenir", "Use them to show the logic, but vary them and use each one with its exact meaning.", cards=[
            ["Addition", "de plus, en outre, par ailleurs"],
            ["Opposition", "pourtant, cependant, en revanche, or (but, in fact), mais"],
            ["Cause", "car, en effet, puisque, parce que"],
            ["Conséquence", "donc, ainsi, par conséquent, c'est pourquoi"],
            ["Illustration", "par exemple, ainsi, notamment"],
            ["Concession", "certes... mais, bien que + subjonctif, même si"],
        ]),
        H("The conclusion: bilan and ouverture"),
        D("The conclusion has two moves: **le bilan** (a short answer to the problématique, following the plan) and **l'ouverture** (a wider question or idea that goes beyond the sujet without starting a new essay).", title="Conclusion"),
        EX("Worked example 3 : une conclusion", intro="Conclude the essay on the livre numérique.", steps=[
            S("Bilan", text="« Au terme de cette réflexion, il apparaît que le livre numérique ne peut pas remplacer entièrement le livre traditionnel : il élargit l'accès aux textes, mais il ne garantit ni l'égalité d'accès ni la qualité de la lecture approfondie. »"),
            S("Ouverture", text="« La vraie question est peut-être moins celle du support que celle de l'éducation à la lecture : comment donner à chaque jeune le goût et les moyens de lire, sur papier comme sur écran ? »"),
            S("Check", text="No new argument in the bilan. The ouverture links to a wider idea without proving it."),
        ]),
        H("Clean French: the traps"),
        KEY("Faux amis and close words", "These confusions appear every year in essays. Learn them in pairs.", cards=[
            ["actuellement", "means « currently », not « actually ». « Actually » is en fait or en réalité."],
            ["assister à", "means « to attend », not « to help ». « To help » is aider."],
            ["librairie", "is a bookshop. A library is une bibliothèque."],
            ["épidémie, pandémie", "An épidémie spreads in a region; une pandémie spreads over several continents."],
            ["éventuellement", "means « possibly », not « eventually » (finalement, à la fin)."],
            ["sensible", "means « sensitive ». « Sensible » is raisonnable."],
        ]),
        T("Write in standard French: no pidgin, no text-message spelling, no English word order. Prefer short clear sentences to long unclear ones. Do not use a word you are not sure of: a simple correct word scores better than a rare wrong one."),
        T("A suggested use of your time (a KKEVO suggestion, not a Board rule): about one fifth for the analysis and plan, about seven tenths for writing, and the rest to reread. When rereading, check in this order: agreements (gender, number), verb endings, accents, connectors, and then the sense of each paragraph."),
        MISTAKE("A very long or general amorce", "Opening with « De tout temps, l'homme... » wastes time and does not lead to the sujet. Start with a precise observation linked to the key words."),
        MISTAKE("Giving the answer in the introduction", "The introduction states the question and the path. The reader should still be curious. The answer comes in the conclusion."),
        MISTAKE("A conclusion that adds a new argument", "The conclusion answers the problématique and opens a wider view. A new argument belongs in the développement."),
        MISTAKE("Connectors used with the wrong logic", "« Donc » shows a consequence, not an addition; « or » introduces a turning point, not a cause. Check the logic before writing the connector."),
        TIP("Exam link: Paper 3 essay questions on life situations (a debate, a talk, a report) need the same skills: a clear opening, organised arguments with examples, a closing sentence, and accurate French. Adapt the form to the situation (a speaker addresses an audience; a report is more factual). Check the exact format with your teacher."),
        QUIZ("Which sentence is the best amorce for an essay on the digital book?", [
            "De tout temps, l'homme a lu des livres.", "Les livres sont en papier et les tablettes sont en plastique.",
            "Depuis quelques années, il n'est plus rare de voir un élève lire un roman sur son téléphone.", "Ma tablette est neuve et très chère."], 2,
            "A good amorce is a precise, relevant observation that leads naturally to the sujet.",
            hint="Which opening is both specific and connected to the sujet?",
            feedback=["« De tout temps » is too general and does not lead to the sujet.", "It lists facts without leading to the question.", "", "It is a personal anecdote, not an introduction to the sujet."]),
        QUIZ("A student writes « Actuellement, j'étais à l'école, mais actually ma tante est venue. » What is the main language problem?", [
            "Nothing, it is correct French.", "The student mixed English and French and used actuellement as if it meant actually.",
            "The student used the wrong tense only.", "The student should use the subjunctive."], 1,
            "Actuellement means currently, and « actually » is English. In French, « en fait » is the correct equivalent.",
            hint="Which word is a faux ami and which is English?",
            feedback=["The sentence mixes languages and a faux ami.", "", "The tense is secondary here; the main problem is the mixture and the faux ami.", "The subjunctive is not involved."]),
        PQ("Write the introduction (four moves) for the sujet « La technologie rend-elle l'homme plus libre ? » in 4 or 5 sentences.",
           "Possible answer: « Aujourd'hui, un téléphone suffit pour payer, apprendre ou communiquer avec le monde entier. Cette puissance de la technologie permet de se demander si elle rend l'homme plus libre. Dans quelle mesure les techniques modernes libèrent-elles l'homme sans le rendre dépendant d'elles ? Nous verrons d'abord comment la technologie élargit nos libertés, puis les nouvelles dépendances qu'elle crée, avant de montrer que la liberté dépend de l'usage que l'on en fait. » The answer uses the four moves in order and a problématique with tension."),
        PQ("Rewrite using a good connector: « Il y a des routes goudronnées. Les marchandises arrivent plus vite. » Explain the logic.",
           "« Il y a des routes goudronnées ; par conséquent, les marchandises arrivent plus vite. » (or « Grâce aux routes goudronnées, les marchandises arrivent plus vite. ») The second fact is the result of the first, so a connector of consequence (par conséquent, donc, c'est pourquoi) is right. « De plus » would wrongly make them two separate points."),
        PQ("Write a two-sentence conclusion (bilan and ouverture) for an essay on the question : « Faut-il remplacer les livres papier par des tablettes à l'école ? »",
           "Possible answer: « Les tablettes offrent des ressources précieuses, mais elles ne remplacent pas toujours le plaisir et la concentration du livre imprimé, surtout là où l'équipement manque. Plus largement, la question est de savoir comment l'école peut apprendre à chaque élève à lire avec esprit critique sur n'importe quel support. » The first sentence is the bilan (answers the question with a nuance), the second the ouverture."),
        SUM("Introduction in four moves: amorce, sujet, problématique, annonce du plan.",
            "Each paragraph: idée directrice, explication, exemple, mini-bilan; use connectors with their exact logic.",
            "Conclusion: bilan (answer) and ouverture (wider question), without a new argument.",
            "Watch the faux amis (actuellement, assister, librairie, éventuellement) and épidémie against pandémie.",
            "Reread in order: agreements, verb endings, accents, connectors, sense."),
    ]))

# ------------------------------------------------------------------ 5. Le classicisme
LESSONS.append(lesson(
    module=M_PAN, topic=T_CLASS,
    title="Le classicisme : raison, règles et perfection au XVIIe siècle",
    slug="frl2-classicisme",
    minutes=24,
    summary="French classicism (17th century): context under Louis XIV, its rules (trois unités, bienséance, vraisemblance), the great names (Corneille, Racine, Molière, La Fontaine, Boileau) and how to talk about them in an exam.",
    objectives=[
        "Place classicism in time and in its political and cultural context",
        "State the classical rules and values (raison, ordre, plaire et instruire, trois unités, bienséance, vraisemblance)",
        "Name the main authors and works of the period and their genres",
        "Distinguish tragedy, comedy and fable and use the right literary notions",
    ],
    key_concepts=["Classicisme", "Règle des trois unités", "Bienséance", "Vraisemblance", "Tragédie, comédie", "Alexandrin", "Plaire et instruire"],
    blocks=[
        H("Introduction"),
        T("Walk into a classical French theatre and you will see tidy gardens, strict rules and noble characters speaking in perfect verse. This is the world of **classicisme**, the literature of the 17th century, when France was ruled by Louis XIV (reign from 1643, and personal rule from 1661 to 1715). Writers wanted order, clarity and reason, and they wanted to be both pleasing and useful: **plaire et instruire**."),
        T("In the Board's Paper 1 you must recognise literary notions and movements; in Paper 2 you write about literary texts using the right technique words. This lesson gives you the map. For any detail (date, title) you plan to use in an exam, check your own textbook."),
        IMG("alfrl2-timeline-mouvements.svg", alt="Timeline from the 17th to the 20th century with five movements: classicisme (about 1630 to 1715), Lumières (1715 to 1789), romantisme (about 1800 to 1850), réalisme et naturalisme (about 1850 to 1890), négritude and post-independence (1930s onward).", caption="Figure 1. The five movements of this course (dates are approximate; movements overlap)."),
        H("The context"),
        T("Three facts explain classicism. **A strong state:** Louis XIV and his court at Versailles set the model of taste. **A language to organise:** the Académie française, founded in 1635, was given the task of fixing and polishing the French language. **A faith in reason:** the philosopher Descartes (Discours de la méthode, 1637) made clear thinking the guide of knowledge."),
        D("**Le classicisme** is the French literary movement of the 17th century (roughly the 1630s to the early 1700s) that sought order, clarity, balance and imitation of ancient models (Greek and Latin), with the aim of pleasing and instructing the honnête homme (the cultured, balanced person).", title="Definition"),
        KEY("The classical rules", "Learn each rule with its reason.", cards=[
            ["Règle des trois unités", "Unité d'action (one main plot), de lieu (one place) and de temps (about one day, twenty-four hours). The aim: clarity and credibility on the stage."],
            ["Vraisemblance", "What happens must seem believable to the audience, even if it is not true in history."],
            ["Bienséance", "Nothing shocking on stage: violence and death happen off-stage and are reported; language stays proper."],
            ["Séparation des genres", "Tragedy (noble characters, serious tone) and comedy (ordinary characters, laughter) are not mixed."],
        ]),
        T("The theorist who gave the rules their classic form is **Boileau**, in his poem *L'Art poétique* (1674). Its spirit: nature, reason and clarity. Classical verse is the **alexandrin**: a line of twelve syllables, usually cut in two halves of six by the **césure** (the pause in the middle). In theatre, rhymes are usually **rimes plates** (AABB) with alternating **masculine** and **feminine** rhymes (feminine rhymes end with a mute e)."),
        H("Tragedy: Corneille and Racine"),
        T("**Pierre Corneille** (1606 to 1684) wrote Le Cid (1637), Horace, Cinna and Polyeucte. His heroes face a **dilemma** (devoir against passion) and win by will: this gave the adjective « cornélien » to any choice between duty and love. Le Cid caused a great debate (la querelle du Cid) about the rules."),
        T("**Jean Racine** (1639 to 1699) wrote Andromaque (1667), Britannicus (1669) and Phèdre (1677). His heroes are caught in the grip of a **fatal passion** that reason cannot control. The audience feels **pitié et crainte** (pity and fear), the effect that tragedy has since Aristotle. The language is simple, harmonious and very precise."),
        H("Comedy: Molière"),
        T("**Molière** (Jean-Baptiste Poquelin, 1622 to 1673) followed the classical idea of comedy, « corriger les mœurs par le rire » (correct customs by laughter), to attack hypocrisy, greed and vanity. His main plays include Tartuffe (1664, banned and then allowed in 1669), Le Misanthrope (1666), L'Avare (1668) and Le Bourgeois gentilhomme (1670). He mixes **comédie de caractère** (a character with a ruling fault: the miser, the hypocrite) and **comédie de mœurs** (a portrait of society) with farce."),
        H("Other classical writers"),
        KEY("Beyond the theatre", "The same ideals appear in other genres.", cards=[
            ["La Fontaine (1621 to 1695)", "Fables, in verse (1668 to 1694): short stories with animals, a **morale** (lesson) and a satire of court and society."],
            ["La Rochefoucauld and La Bruyère", "Maximes (La Rochefoucauld) and Les Caractères (La Bruyère, 1688): short moral portraits and sayings that study human nature."],
            ["Madame de La Fayette", "La Princesse de Clèves (1678), often called the first great French psychological novel."],
            ["Pascal and Bossuet", "Pascal's Pensées (thoughts on human weakness and faith); Bossuet's funeral orations: prose of reason and faith."],
        ]),
        EX("Worked example 1 : relier une œuvre à l'esthétique classique", intro="Question: « Montrez que Phèdre de Racine respecte les règles du classicisme. » Plan the answer.", steps=[
            S("Name the movement", text="Phèdre (1677) is a classical tragedy in alexandrins."),
            S("Unités", text="One main action (the passion of Phèdre and its consequences), one place (a palace), about one day. Check these details against your own copy."),
            S("Bienséance", text="Violent deaths are not shown: they are reported by a character."),
            S("Aim", text="Pity and fear: the audience sees how a passion destroys a person who knows it is wrong."),
            S("Evaluate", text="The rules are not a prison: Racine uses them to concentrate tension on the characters' inner struggle."),
        ]),
        EX("Worked example 2 : analyser un effet comique", intro="In a classical comedy, a miser refuses to spend money even for his children's happiness. Which literary notions do you use?", steps=[
            S("Genre", text="Comédie de caractère: the ruling fault of the character is avarice."),
            S("Technique", text="Exaggeration (**hyperbole**) and repetition create the **comique de caractère**; the character's contradictions create **comique de situation**."),
            S("Register", text="Satire: the aim is to criticise a fault through laughter."),
            S("Aim", text="To make the audience recognise the fault and correct it: « plaire et instruire »."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing movements and dates", "Classicism is the 17th century; the Lumières are the 18th; romanticism the early 19th. Match each author to the century and the century to its mood."),
        MISTAKE("Listing rules without examples", "Writing « il y a trois unités » earns little. Say what the unités are, why they exist and show them in a play you studied."),
        MISTAKE("Thinking classical art is cold", "Racine's plays are full of violent feeling; the form is calm because the passion inside is strong. Show this tension."),
        TIP("Exam link: Paper 1 asks about literary notions and movements (rules, alexandrin, tragedy and comedy). In Paper 2 the Board recommends covering characters, techniques, setting, themes and plot, and using the text as evidence; classical drama gives you vocabulary for that. Check which texts your school studies."),
        QUIZ("Which of these is NOT one of the three classical unités?", ["Unité d'action", "Unité de lieu", "Unité de style", "Unité de temps"], 2,
             "The three unités are action, lieu and temps. « Style » is not an unité.",
             hint="Name the three and see which does not belong.",
             feedback=["It is one of the three.", "It is one of the three.", "", "It is one of the three."]),
        QUIZ("What does bienséance require in classical theatre?", [
            "Shocking scenes are shown on stage", "Scenes that offend good taste, such as violent deaths, are not shown and are reported",
            "Comedy and tragedy are mixed", "The play must last several years"], 1,
            "Bienséance means propriety: nothing shocking on stage; violence is reported.",
            hint="Think of what the audience may and may not see.",
            feedback=["It is the opposite of bienséance.", "", "That is mixing of genres, a romantic idea.", "Unité de temps asks for about one day."]),
        PQ("Define l'alexandrin and the césure, and give one example of a fact about classical rhyme.",
           "L'alexandrin is a line of twelve syllables; the césure is the pause in the middle, usually after the sixth syllable, which divides the line into two hémistiches. In classical theatre rhymes are mostly rimes plates (AABB) and masculine and feminine rhymes alternate (a feminine rhyme ends with a mute e, such as « terre » or « fable »)."),
        PQ("Explain the term « héros cornélien » and say why Racine's characters are different.",
           "A héros cornélien faces a dilemma between duty (honour, state, family) and personal passion, and wins through willpower and reason. Racine's characters are often overcome by a fatal passion they cannot master, so their tragedy is more inner and more fatal. Contrast: Corneille shows will winning over passion, Racine shows passion that destroys."),
        PQ("Write a short paragraph answering: « En quoi la comédie de Molière est-elle à la fois divertissante et critique ? »",
           "Plan: (1) Divertissement: farce, exaggeration, quick dialogue, characters with obvious faults. (2) Critique: the plays attack hypocrisy, greed and vanity (a miser, a false devout person), which the audience recognises in its own society. (3) Link: the laughter makes the lesson acceptable (« corriger les mœurs par le rire »). Support the points with a play you have studied."),
        SUM("Classicisme is the 17th-century movement of order, reason and imitation of the ancients: plaire et instruire.",
            "Rules: unité d'action, de lieu et de temps, vraisemblance, bienséance, séparation des genres.",
            "Corneille (devoir against passion), Racine (fatal passion), Molière (comedy of character and manners), La Fontaine (fables).",
            "Verse: the alexandrin (twelve syllables, césure), rimes plates, alternating gender.",
            "Link every work to its movement, its genre and its literary notions."),
    ]))

# ------------------------------------------------------------------ 6. Le siècle des Lumières
LESSONS.append(lesson(
    module=M_PAN, topic=T_LUM,
    title="Le siècle des Lumières : raison, critique et tolérance",
    slug="frl2-lumieres",
    minutes=24,
    summary="The French Enlightenment (18th century): its ideas (raison, progrès, liberté, tolérance), the main philosophes (Montesquieu, Voltaire, Rousseau, Diderot), the genres they used (conte philosophique, essai, Encyclopédie, théâtre) and their weapons: irony and satire.",
    objectives=[
        "Explain the ideas of the Lumières and the context of the 18th century",
        "Name the main authors and works with their genres",
        "Define the conte philosophique, ironie, satire and argumentation indirecte",
        "Answer a question on how the Lumières used literature to fight for ideas",
    ],
    key_concepts=["Les Lumières", "Philosophe", "Encyclopédie", "Conte philosophique", "Ironie et satire", "Argumentation directe et indirecte", "Tolérance"],
    blocks=[
        H("Introduction"),
        T("Think of a student who asks « why? » about everything and refuses to accept an answer only because someone powerful gave it. In the 18th century many French writers did exactly this: they questioned authority, superstition and injustice in the name of reason. We call the century **le siècle des Lumières** because they wanted to bring the « light » of reason into a world they thought was dark with ignorance."),
        D("**Les Lumières** (the Enlightenment) is the intellectual movement of the 18th century that trusted reason, experience and freedom of thought, defended **tolérance**, **liberté**, **progrès** and **égalité** before the law, and criticised absolute power, religious intolerance and injustice. Its writers are called the **philosophes**.", title="Definition"),
        T("These ideas did not stay in books. They spread in the salons, in the press and in the Encyclopédie, and they helped prepare the French Revolution of 1789, which produced the Déclaration des droits de l'homme et du citoyen. Historians debate how direct this influence was, so say that the Lumières **helped prepare** the Revolution, not that they alone caused it."),
        H("The main philosophes"),
        KEY("Four great names", "Know one major work for each with its genre.", cards=[
            ["Montesquieu (1689 to 1755)", "Lettres persanes (1721): two Persian visitors criticise French society with humour (roman épistolaire). De l'esprit des lois (1748): the separation of the powers (législatif, exécutif, judiciaire)."],
            ["Voltaire (1694 to 1778)", "Lettres philosophiques (1734), Candide (1759), Traité sur la tolérance (1763). He fought fanaticism and injustice with wit."],
            ["Rousseau (1712 to 1778)", "Discours sur l'inégalité (1755), Du contrat social (1762), Émile (1762). He placed nature, feeling and the people's will at the centre."],
            ["Diderot (1713 to 1784)", "With d'Alembert he directed the Encyclopédie (published 1751 to 1772), a huge dictionary of knowledge and techniques. Also Jacques le fataliste."],
        ]),
        T("Other voices: **Marivaux** (1688 to 1763) wrote comedies such as Le Jeu de l'amour et du hasard (1730) and Les Fausses Confidences (1737), where the language of love, class and money meets. **Beaumarchais** wrote Le Barbier de Séville (1775) and Le Mariage de Figaro (written 1778, staged 1784), in which a servant answers his master. **L'abbé Prévost** wrote Manon Lescaut (1731). Olympe de Gouges wrote a Déclaration des droits de la femme et de la citoyenne (1791). Les Fausses Confidences is named in the Board's report among the set texts of the literature paper; check what your syllabus requires."),
        H("How did they write?"),
        T("The philosophes could not always speak openly, because censorship and prison were real risks. They therefore invented ways to argue while looking innocent. **Argumentation directe** states a thesis openly (an essay or a treatise). **Argumentation indirecte** hides the thesis in a story, a play or a letter (a conte, a roman épistolaire, a comedy) so that the reader draws the conclusion."),
        KEY("Tools of the philosophes", "Name the tool, then say its effect.", cards=[
            ["Ironie", "Saying the opposite of what you mean so that the reader sees the criticism. Effect: complicity with the reader."],
            ["Satire", "Attacking a person, a group or an institution by ridicule. Effect: laughter that exposes a vice."],
            ["Conte philosophique", "A short, lively tale with a simple plot that carries an idea (Voltaire's Candide, Zadig, Micromégas). Effect: ideas made easy and memorable."],
            ["Regard éloigné", "Seeing one's own society through foreign eyes (the Persians of Montesquieu). Effect: customs seem strange and are questioned."],
        ]),
        EX("Worked example 1 : lire une critique indirecte", intro="Candide (1759) ends with the idea of cultivating one's own garden (« cultiver notre jardin »). Explain what the final lesson could mean.", steps=[
            S("Place the work", text="Candide is a conte philosophique by Voltaire, which follows a young man across a series of disasters."),
            S("What is criticised?", text="The conte mocks a naïve optimism (« tout est pour le mieux »), war, religious intolerance and slavery."),
            S("What does the garden suggest?", text="Readers have discussed it: practical work, modest but useful effort, rather than empty theories. Check your textbook for the reading your teacher gives."),
            S("Evaluate", text="The conclusion is not a call to give up the world: it is a call to action that is realistic and useful."),
        ]),
        EX("Worked example 2 : plan d'une réponse", intro="Question: « En quoi la littérature des Lumières est-elle un instrument de combat ? »", steps=[
            S("Partie 1 : des combats", text="Against absolute power, intolerance, slavery, privilege. Examples: Voltaire (tolérance), Montesquieu (séparation des pouvoirs)."),
            S("Partie 2 : des moyens", text="Ironie, satire, conte, Encyclopédie for the spread of knowledge, theatre for a wide audience."),
            S("Partie 3 : des limites", text="Censorship forced indirect forms; the philosophes were not all democrats; their ideas were put into practice slowly and unevenly."),
            S("Conclusion", text="The literature of the Lumières made ideas public, and prepared the language of rights that the Revolution later used."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the Lumières caused the Revolution alone", "Their ideas prepared opinion, but the Revolution had financial, social and political causes too. Use « ont contribué à préparer »."),
        MISTAKE("Confusing Voltaire and Rousseau", "Voltaire stands for reason, wit and tolerance; Rousseau stresses nature, feeling and the general will. They disagreed about many things, including the effects of civilisation."),
        MISTAKE("Thinking all the 18th century is philosophical", "The century also has comedy (Marivaux), novel (Prévost) and theatre of love. Do not call every 18th-century author a philosophe."),
        TIP("Exam link: Paper 1 may test authors, works, genres and notions (ironie, satire, conte). In Paper 2 the Board's report asks candidates to analyse, to illustrate with the text and to judge; Marivaux appears among the questions, so learn how a comedy of love and class works. Check which works are on your syllabus."),
        QUIZ("Which author wrote Du contrat social?", ["Voltaire", "Montesquieu", "Rousseau", "Diderot"], 2,
             "Rousseau wrote Du contrat social (1762).",
             hint="Which philosophe wrote about the general will?",
             feedback=["Voltaire wrote Candide and the Traité sur la tolérance.", "Montesquieu wrote Lettres persanes and De l'esprit des lois.", "", "Diderot directed the Encyclopédie."]),
        QUIZ("What is the effect of ironie in a work of the Lumières?", [
            "It states the criticism openly and without ornament", "It says the opposite of what is meant so the reader sees the criticism",
            "It tells an exact historical story", "It describes the author's private life"], 1,
            "Irony says the opposite of what is meant. The reader understands the criticism and becomes the author's ally.",
            hint="Think of saying « Quelle belle journée ! » in a storm.",
            feedback=["That describes argumentation directe.", "", "That is historical narrative, not irony.", "Irony has nothing to do with biography."]),
        PQ("Define « conte philosophique » and give one example with an author.",
           "A conte philosophique is a short, lively story with a simple plot and often exotic or imaginary settings that carries an idea or a criticism. Example: Voltaire's Candide (1759), which uses the adventures of a naïve young man to criticise optimism, war and intolerance."),
        PQ("Explain the difference between argumentation directe and indirecte and say why the philosophes used the second.",
           "Argumentation directe states a thesis openly (an essay, a treatise, a speech). Argumentation indirecte hides it in a tale, a play, a letter or a dialogue so that the reader draws the conclusion. The philosophes often used the second because censorship made open criticism dangerous, and because stories are more entertaining and persuasive."),
        PQ("Write a short paragraph on « Marivaux et la comédie des sentiments » to show you understand the genre.",
           "Marivaux writes comedies about love, where characters hide or misunderstand their feelings, which creates a delicate game of language (marivaudage). Social rank and money often shape the choices of the characters. The tone is light but not shallow: the comedy shows how fragile and subtle feelings are. For a precise answer on Les Fausses Confidences or another play, use your own copy and your teacher's notes."),
        SUM("The Lumières (18th century) trusted reason and defended tolérance, liberté and progrès against absolutism and fanaticism.",
            "Montesquieu, Voltaire, Rousseau and Diderot are the main philosophes; the Encyclopédie spreads knowledge.",
            "Direct argument states a thesis; indirect argument hides it in a conte, a letter or a play.",
            "Ironie and satire are the main tools; the conte philosophique makes ideas memorable.",
            "Say the Lumières helped prepare the Revolution, not that they alone caused it."),
    ]))

# ------------------------------------------------------------------ 7. Le romantisme
LESSONS.append(lesson(
    module=M_PAN, topic=T_ROM,
    title="Le romantisme : le moi, la nature et la liberté en art",
    slug="frl2-romantisme",
    minutes=24,
    summary="French romanticism (early 19th century): the mal du siècle, lyrical poetry, the romantic drama and Hugo's manifesto, the great names (Chateaubriand, Lamartine, Hugo, Vigny, Musset) and how poetry and prose express the self; Baudelaire as a bridge to modernity.",
    objectives=[
        "Explain what romanticism is and what it reacted against",
        "Name the main romantic authors and works and the themes they share",
        "Define the lyric register, the mal du siècle, the drame romantique and the mélange des genres",
        "Use the vocabulary of romantic poetry (lyrisme, enjambement, rejet, personnification, nature-miroir)",
    ],
    key_concepts=["Romantisme", "Mal du siècle", "Lyrisme", "Nature miroir de l'âme", "Drame romantique", "Mélange des genres", "Enjambement et rejet"],
    blocks=[
        H("Introduction"),
        T("You are alone at night and look at the sky. The stars make you feel small, your sadness gets bigger and you wish to write it down. If you did, you would write like a romantic. The **romantisme** is the movement in which writers made their own feelings the centre of literature, and wanted to be free from the rules of classicism."),
        D("**Le romantisme** is the literary and artistic movement of the early 19th century (about 1800 to 1850 in France) that put the **moi** (the self), emotion, imagination and nature at the centre, rejected strict classical rules and claimed freedom in art. It reacted against the primacy of reason and rules.", title="Definition"),
        T("The context: the French Revolution (1789) and the Empire had shaken old certainties. Many young people of the new century felt disillusioned, lonely and anxious about the future. This feeling is called the **mal du siècle** (the sickness of the century)."),
        H("Main themes"),
        KEY("What romantic writers write about", "Link each theme to the feeling behind it.", cards=[
            ["Le moi et le lyrisme", "The poet speaks of personal feelings: love, sadness, regret, hope (poésie lyrique). The pronoun « je » is central."],
            ["La nature miroir de l'âme", "Landscapes reflect the poet's mood: a lake at evening shows melancholy, a storm shows revolt."],
            ["Le temps, la mort, le souvenir", "Everything passes; poetry tries to keep what is lost."],
            ["La liberté et l'engagement", "Freedom in art, and also in society: Hugo fights against the death penalty and poverty."],
        ]),
        H("The great names"),
        KEY("Authors and works", "Learn one or two works for each.", cards=[
            ["Chateaubriand (1768 to 1848)", "René (1802): a young man torn by boredom and melancholy; one of the first expressions of the mal du siècle in prose."],
            ["Lamartine (1790 to 1869)", "Méditations poétiques (1820), including the poem « Le Lac » : a meditation on time and love. Lyric poetry."],
            ["Victor Hugo (1802 to 1885)", "Preface to Cromwell (1827), Hernani (1830), Notre-Dame de Paris (1831), Les Contemplations (1856), Les Misérables (1862). Poet, dramatist and novelist."],
            ["Vigny and Musset", "Vigny (1797 to 1863): philosophical poetry and the proud solitude of the poet. Musset (1810 to 1857): Lorenzaccio (1834), a drama of disillusion; Les Nuits poems."],
        ]),
        T("Women writers also mattered: **Madame de Staël** helped introduce the ideas of romanticism, and **George Sand** (1804 to 1876) wrote novels about love and social questions. Check your textbook for the authors your teacher stresses."),
        H("The romantic theatre and the preface to Cromwell"),
        T("In his preface to Cromwell (1827) Hugo attacked the classical rules and defended a free drama. He claimed the **mélange des genres**: the **sublime** (noble, beautiful) and the **grotesque** (ugly, comic) can appear side by side, as in life. In the famous première of Hernani (1830) supporters of the old and the new theatre clashed: we call this « la bataille d'Hernani »."),
        KEY("Classical drama against romantic drama", "Compare the two to prepare essays.", cards=[
            ["Classical", "Three unités, bienséance, tragedy and comedy kept apart, alexandrin respected strictly, noble characters."],
            ["Romantic", "No strict unités, scenes and events on stage, mixture of tragic and comic, freer verse and prose, characters of all ranks."],
        ]),
        H("The language of romantic poetry"),
        T("Romantic poets keep the alexandrin but make it more flexible. They use the **enjambement** (a sentence runs over to the next line) and the **rejet** (a word of the first line that completes the sense is thrown to the next line). They use images of nature, **personification** (giving human features to a thing) and **apostrophe** (addressing a person or thing: « ô lac ! »). The dominant register is **lyrique** (feelings expressed in the first person)."),
        EX("Worked example 1 : analyser un trait romantique", intro="Invented lines for practice: « Ô soir, tu viens poser ta main sur mon cœur lourd ; / Le vent qui passe emporte mon souvenir ». Which romantic features can you identify?", steps=[
            S("Apostrophe", text="« Ô soir » addresses the evening as if it were a person."),
            S("Personification", text="The evening « pose sa main » (human gesture)."),
            S("Lyrisme", text="The first person (« mon cœur », « mon souvenir ») expresses personal emotion."),
            S("Nature miroir de l'âme", text="The evening and the wind reflect the speaker's sadness."),
        ]),
        EX("Worked example 2 : plan d'une réponse", intro="Question: « En quoi Victor Hugo est-il à la fois un poète lyrique et un écrivain engagé ? »", steps=[
            S("Partie 1 : le poète lyrique", text="He writes of family, love, mourning and nature with the first person (for example in Les Contemplations)."),
            S("Partie 2 : l'écrivain engagé", text="He uses his writing against the death penalty and for the poor (Les Misérables, 1862; the Dernier Jour d'un condamné, 1829)."),
            S("Partie 3 : l'unité", text="The same compassion drives both: the pain of the individual becomes the pain of humanity."),
            S("Check", text="Support each point with a text you have studied."),
        ]),
        T("A bridge to modernity: after the high romantic years, **Charles Baudelaire** (1821 to 1867) published Les Fleurs du mal (1857). He keeps the lyric voice but speaks of the city, of spleen (heavy boredom) and of the ideal (idéal). Because the Board's report asks students to study selected poems of Baudelaire, learn the main sections of the collection from your textbook (the first, « Spleen et Idéal », is the largest) and prepare a theme such as love and inspiration."),
        MISTAKE("Calling every sad poem romantic", "Romantic poems join emotion with nature, imagination and freedom of form. Do not label a poem romantic only because it is sad."),
        MISTAKE("Mixing up Hugo's roles", "Hugo is a poet, a dramatist and a novelist, and a political voice. In an answer say which role the work shows."),
        MISTAKE("Defining lyrisme as « sadness »", "Lyrisme is the expression of personal feeling in the first person: joy, love, admiration or grief."),
        TIP("Exam link: Paper 1 asks about literary notions (lyrisme, enjambement, personnification); the Board's Paper 2 includes questions on poetry and on a novel by Hugo, where candidates must show how techniques (narration, description, flashback) are used effectively, not only list them. Check which texts your school studies."),
        QUIZ("What is the mal du siècle?", [
            "A disease that spread in 1800", "The sadness and disillusion of the young generation after the Revolution and the Empire",
            "A classical rule of tragedy", "A style of verse with twelve syllables"], 1,
            "The mal du siècle is a feeling of boredom, solitude and disillusion typical of the early 19th century.",
            hint="Think of the mood after great historical shocks.",
            feedback=["It is a feeling, not an illness.", "", "Classical rules are different.", "That is the alexandrin."]),
        QUIZ("Which of the following is a feature of the drame romantique?", [
            "Strict respect for the three unités", "Mixture of the grotesque and the sublime", "Violence always hidden from the stage", "Only noble characters"], 1,
            "Hugo's preface to Cromwell defends the mélange des genres: the sublime and the grotesque together.",
            hint="Remember the preface to Cromwell.",
            feedback=["That is classical.", "", "Bienséance is classical; romantic drama shows action on stage.", "Romantic drama accepts characters of every rank."]),
        PQ("Define enjambement and rejet and say why romantic poets liked them.",
           "L'enjambement: the sense of a sentence does not stop at the end of the line but continues into the next. Le rejet: a word (or a short group) that completes the sense is placed at the start of the next line, which emphasises it. Romantic poets liked them because they break the rigid rhythm of the classical alexandrin, create surprise and imitate the natural movement of speech and feeling."),
        PQ("Compare in four points the classical and the romantic conception of theatre.",
           "1. Rules: classical respects the three unités; romantic rejects them. 2. Genres: classical keeps tragedy and comedy apart; romantic mixes sublime and grotesque. 3. Bienséance: classical hides violence; romantic shows action on stage. 4. Characters and language: classical uses noble characters and strict alexandrins; romantic uses characters of all ranks and freer verse or prose."),
        PQ("Explain « la nature miroir de l'âme » with an example you invent.",
           "The expression means the landscape reflects the poet's state of mind. Invented example: « Le ciel gris pèse comme mon chagrin ; l'arbre mort dit ma solitude. » The grey sky and the dead tree are described in words that match the poet's grief, so the nature seen is also the heart shown."),
        SUM("Romanticism (early 19th century) puts the moi, emotion, imagination and nature at the centre and claims freedom against rules.",
            "The mal du siècle is the disillusion of the generation after the Revolution and the Empire.",
            "Main names: Chateaubriand, Lamartine, Hugo, Vigny, Musset; Hugo's preface to Cromwell (1827) defends the drame romantique.",
            "Features: lyrisme, nature miroir de l'âme, enjambement and rejet, apostrophe, personification, mélange des genres.",
            "Baudelaire's Les Fleurs du mal (1857) is a bridge to modern poetry."),
    ]))

# ------------------------------------------------------------------ 8. Le réalisme et le naturalisme
LESSONS.append(lesson(
    module=M_PAN, topic=T_REAL,
    title="Le réalisme et le naturalisme : observer et peindre la société",
    slug="frl2-realisme-naturalisme",
    minutes=24,
    summary="Realism and naturalism (mid to late 19th century): the novel as a mirror of society, Balzac, Stendhal, Flaubert, Maupassant and Zola, the ideas of observation, milieu and heredity, and the techniques of narration, description and point of view.",
    objectives=[
        "Explain what realism and naturalism aim to do and how they differ",
        "Name the main authors and works of each movement",
        "Define narrateur, point de vue (focalisation), description and style indirect libre",
        "Analyse how a realist or naturalist writer builds the illusion of reality",
    ],
    key_concepts=["Réalisme", "Naturalisme", "Observation et documentation", "Milieu et hérédité", "Focalisation", "Description", "Style indirect libre"],
    blocks=[
        H("Introduction"),
        T("Look at the market of your town and ask a camera to record it: the noise, the smells, the prices, the faces. A novelist can do the same with words. In the middle of the 19th century many French writers decided that literature should not dream of the past or of faraway lands but should look at the real society of their own time, with all its money, work, ambition and misery. This is the **réalisme**."),
        D("**Le réalisme** is the literary movement (especially the novel) of about 1830 to 1880 that tries to represent contemporary society as it really is, through observation, documentation and precise detail. **Le naturalisme** (about 1870 to 1890) pushes this further: the writer works like a scientist, showing how **heredity** and **environment (milieu)** shape the characters.", title="Definition"),
        T("The context: the Industrial Revolution, the growth of cities, the rise of the middle class, the press and the sciences (medicine, biology, sociology). The novel became the main literary genre because it could describe all these changes."),
        H("The realist novel"),
        KEY("Four great realist novelists", "Learn one major work for each.", cards=[
            ["Balzac (1799 to 1850)", "La Comédie humaine: a huge cycle of novels about French society, with returning characters. Eugénie Grandet (1833), Le Père Goriot (1835)."],
            ["Stendhal (1783 to 1842)", "Le Rouge et le Noir (1830): a young ambitious man from a small town faces the social order of his time."],
            ["Flaubert (1821 to 1880)", "Madame Bovary (1857): a woman's disappointed dreams in the provinces. Famous for its precise style and its impersonal narration."],
            ["Maupassant (1850 to 1893)", "Short stories and novels: Boule de Suif (1880), Une vie (1883), Bel-Ami (1885). Clear, ironic, economical writing."],
        ]),
        T("In addition, Hugo's Les Misérables (1862) combines romantic and realist features; this reminds us that movements overlap."),
        H("The naturalist novel and Zola"),
        T("**Émile Zola** (1840 to 1902) is the leader of naturalism. In Le Roman expérimental (1880) he argued that the novelist is like an experimenter: he places characters in a milieu and observes the effects. His series **Les Rougon-Macquart** (twenty novels, 1871 to 1893) follows one family across several generations to show the effects of heredity and environment. Major titles: L'Assommoir (1877) on alcoholism and poverty among workers, and **Germinal** (1885) on a miners' strike. Zola's open letter « J'accuse…! » (1898) shows that his idea of truth also reached political life, in the Dreyfus affair."),
        KEY("Réalisme against naturalisme", "A useful comparison for essay questions.", cards=[
            ["Réalisme", "Observe and represent society. Detail makes the story credible. The author may judge or not. Focus on social types and individuals."],
            ["Naturalisme", "Apply the scientific method. Determinism: heredity and milieu explain behaviour. Often the lowest classes and strong social criticism. Documentation and fieldwork."],
        ]),
        H("Techniques"),
        T("Realists and naturalists create the **illusion of reality** with several techniques. **The description** gives precise details of places, objects, clothes and bodies, which also reveal the character or the society. **The narrator** may be **omniscient** (knows everything, zero focalisation), may see through one character (**internal focalisation**) or may only describe what could be seen from outside (**external focalisation**). **Le style indirect libre** (free indirect speech) reports a character's thoughts without quotation marks or introducing verbs (« Elle se demanda si tout cela valait la peine. Non, certainement pas. ») and is associated with Flaubert."),
        EX("Worked example 1 : repérer la focalisation", intro="Invented sentence: « Mariama regardait la rue. Combien de temps durerait encore cette attente ? Il fallait pourtant tenir. » Which technique is used in the last two sentences?", steps=[
            S("Read the second sentence", text="« Combien de temps durerait encore cette attente ? » is a question in the character's mind, without a verb like « elle se demanda »."),
            S("Name the technique", text="Style indirect libre: the narrator reports the thoughts without quotation marks."),
            S("Focalisation", text="Internal: we are inside Mariama's mind."),
            S("Effect", text="The reader shares her anxiety and the narration feels alive."),
        ]),
        EX("Worked example 2 : plan d'un commentaire", intro="Question: « Montrez comment le roman naturaliste présente le milieu comme une force qui détermine les personnages. »", steps=[
            S("Define", text="Naturalism says that heredity and milieu shape people, in the manner of a scientific experiment."),
            S("Partie 1 : le milieu décrit", text="Housing, work, money and health are described in detail (for example the mine in Germinal or the neighbourhood in L'Assommoir)."),
            S("Partie 2 : les personnages déterminés", text="Characters repeat family traits and cannot escape: use the idea of the Rougon-Macquart series."),
            S("Partie 3 : limites", text="Some critics say the characters have little freedom and that the author's moral message is clear. Evaluate."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying realism copies reality exactly", "Realist novels are constructions: the author chooses details and organises them. Say « crée l'illusion du réel », not « copie la réalité »."),
        MISTAKE("Using naturalisme and réalisme as synonyms", "Naturalism is a more systematic, scientific and often more pessimistic movement that follows realism. Say what each adds."),
        MISTAKE("Listing techniques without effect", "The Board's report for Paper 2 stresses effectiveness: do not only say « il y a une description ». Say what the description reveals about the character or society."),
        TIP("Exam link: Paper 1 may ask for authors, titles and notions (narrateur, description, style indirect libre). In Paper 2 the Board's report warns that candidates list narration, description and flashback without showing how effective they are: always link a technique to its effect, with a precise example from the text."),
        QUIZ("Which author is associated with Les Rougon-Macquart?", ["Balzac", "Flaubert", "Zola", "Maupassant"], 2,
             "Zola wrote the twenty novels of Les Rougon-Macquart (1871 to 1893).",
             hint="It is the naturalist family saga.",
             feedback=["Balzac wrote La Comédie humaine.", "Flaubert wrote Madame Bovary.", "", "Maupassant is known for short stories and Bel-Ami."]),
        QUIZ("What does « focalisation interne » mean?", [
            "The narrator knows everything", "The story is told through what one character perceives and thinks",
            "The narrator only describes what can be seen from outside", "The story is told in the future"], 1,
            "In focalisation interne we perceive events through one character's eyes and mind.",
            hint="Think of the word « inside ».",
            feedback=["That is omniscient narration (zero focalisation).", "", "That is external focalisation.", "Tense is not the question."]),
        PQ("Define « description » in a realist novel and explain its two main roles.",
           "A description presents a place, an object, a person or a scene with detail. Roles: (1) it creates the illusion of reality (the reader believes in the world of the novel); (2) it reveals meaning: the details show the character, the social class or the mood (for example a poor house shows poverty, a luxury room shows ambition). In some novels it also announces events."),
        PQ("Distinguish realism and naturalism in three points.",
           "1. Method: realism observes and represents; naturalism uses a scientific approach (experiment, documentation). 2. Idea: naturalism insists on determinism (heredity and milieu). 3. Subjects and tone: naturalism often shows the poorest classes and strong social criticism, with a darker tone. Examples: Balzac and Flaubert for realism, Zola for naturalism."),
        PQ("Explain « style indirect libre » with an invented example.",
           "Style indirect libre reports a character's words or thoughts in the third person and the past tense without quotation marks or a verb such as « dit » or « pensa ». Example: « Fatou fermait son cahier. Qu'importait, après tout, cette note ? Elle ferait mieux la prochaine fois. » The questions and exclamations belong to Fatou's mind but are told by the narrator. The effect is to give inner life without breaking the flow."),
        SUM("Realism (about 1830 to 1880) shows contemporary society through observation and precise detail.",
            "Naturalism (about 1870 to 1890) adds the scientific method and determinism: heredity and milieu; Zola is its leader.",
            "Main names: Balzac, Stendhal, Flaubert, Maupassant, Zola; Les Rougon-Macquart is Zola's series.",
            "Techniques: description, narrator and focalisation, style indirect libre.",
            "Always explain the effect of a technique and support it with a precise example."),
    ]))

# ------------------------------------------------------------------ 9. La négritude et la littérature post-indépendance
LESSONS.append(lesson(
    module=M_PAN, topic=T_NEG,
    title="La négritude et la littérature post-indépendance",
    slug="frl2-negritude-post-independance",
    minutes=25,
    summary="From the négritude of Césaire, Senghor and Damas to the French-language African novel and theatre after independence: colonial criticism, identity, disillusion, tradition against modernity, with Cameroonian writers (Oyono, Beti, Bebey, Oyono-Mbia).",
    objectives=[
        "Explain négritude, its origins and its main figures",
        "Describe how African writers in French moved from protest to a critique of post-independence society",
        "Name key works and authors, including Cameroonian ones, with accurate titles and dates",
        "Use the common themes (colonialism, identity, tradition and modernity, family authority, gender) in an essay",
    ],
    key_concepts=["Négritude", "Colonialisme", "Identité et assimilation", "Roman africain de langue française", "Désillusion post-indépendance", "Tradition et modernité"],
    blocks=[
        H("Introduction"),
        T("Imagine you are a young African student in Paris in 1934. You study the culture of your teachers, but they speak of your own continent as if it had no history and no civilisation. You and your friends answer: « We have a culture, a past and a voice; we will write it ourselves. » This is the starting point of the **négritude**, and of modern literature in French from Africa and the Caribbean."),
        D("**La négritude** is a movement of Black writers in French that began in Paris in the 1930s. It asserted the value of Black cultures, history and identity against colonial racism and assimilation, using poetry, essays and journals. Its main founders are the Martinican **Aimé Césaire**, the Senegalese **Léopold Sédar Senghor** and the Guianese **Léon-Gontran Damas**.", title="Definition"),
        T("Before them, the Paris salon of the Nardal sisters and their review La Revue du monde noir (1931) had brought Black thinkers together. The journal **L'Étudiant noir** (1934) is usually linked with the group of Césaire, Senghor and Damas. After the Second World War, the review **Présence africaine** (founded in 1947 by Alioune Diop) gave Black writers a public forum. Césaire is usually credited with the word « négritude » in his writing of the 1930s."),
        H("The great works of négritude"),
        KEY("Authors and works", "Know one or two titles for each.", cards=[
            ["Aimé Césaire (1913 to 2008)", "Cahier d'un retour au pays natal (a poem first published in a review in 1939 and as a book in 1947); Discours sur le colonialisme (1950); the play La Tragédie du roi Christophe (1963), about King Henri Christophe of Haiti."],
            ["Léopold Sédar Senghor (1906 to 2001)", "Chants d'ombre (1945), Hosties noires (1948), Éthiopiques (1956). Poet and first president of Senegal (1960 to 1980); member of the Académie française (1983)."],
            ["Léon-Gontran Damas (1912 to 1978)", "Pigments (1937): short, sharp, rhythmic poems that denounce racism."],
            ["An anthology", "Senghor's Anthologie de la nouvelle poésie nègre et malgache (1948) with a preface by Jean-Paul Sartre, « Orphée noir »."],
        ]),
        T("Négritude was also criticised. Some African writers said that an identity based on race risked becoming a new stereotype; others said it was too focused on the past and not enough on the real struggles for independence. Check your textbook for the critics your syllabus names."),
        H("The novel of protest and the Cameroonian voices"),
        T("In the 1950s, in the final years of colonial rule, African novelists in French used the novel to describe the injustice of colonisation. **Camara Laye** (Guinea) wrote L'Enfant noir (1953), a memory of childhood. The Cameroonians are especially important. **Ferdinand Oyono** wrote Une vie de boy (1956) and Le Vieux Nègre et la médaille (1956), two satires of colonial life. **Mongo Beti** wrote Le Pauvre Christ de Bomba (1956), a critical look at a missionary, and Mission terminée (1957), about a young man's return to his village. They use irony, a lively narrative voice and sharp observation."),
        H("After independence: disillusion and new questions"),
        T("Cameroon and many African countries became independent around 1960. The great hopes of liberation were then tested by **corruption, authoritarian rule, poverty and cultural conflict**. Writers changed their target: from the colonial master to their own societies. Key works include **Cheikh Hamidou Kane**'s L'Aventure ambiguë (1961), on the clash between African and Western ways of knowing, and **Ahmadou Kourouma**'s Les Soleils des indépendances (1968), on a prince's loss in the new state, written in a French that is strongly marked by Malinké speech. **Sembène Ousmane** wrote Les Bouts de bois de Dieu (1960) about a railway strike."),
        T("In Cameroon, **Guillaume Oyono-Mbia** wrote the comedy Trois prétendants... un mari (1964), a theatre of laughter that treats the marriage dowry, and **Francis Bebey** wrote Le Fils d'Agatha Moudio (1967), a gentle, humorous novel about love, family pressure and tradition. **Mariama Bâ** (Senegal) wrote Une si longue lettre (1979), a woman's letter about marriage and polygamy. Later, **Calixthe Beyala** (Cameroon) wrote novels about women and migration. Note that Bebey's novel and Nkoa Atenga's L'Enfant de la révolte muette are named in the Board's report as set texts; use your own copy for any detail."),
        KEY("Main themes of post-independence literature", "Link each theme to an example you have studied.", cards=[
            ["Critique of colonisation", "Racism, forced labour, the missionary and the administrator (Oyono, Beti)."],
            ["Identity and cultural conflict", "Tradition against modernity, the African and the West (Kane)."],
            ["Disillusion with independence", "Corruption, dictatorship, poverty (Kourouma)."],
            ["Family, parents and gender", "Authority of parents and elders, marriage, women's place (Bebey, Bâ, Nkoa Atenga)."],
        ]),
        EX("Worked example 1 : relier une œuvre à son contexte", intro="Question: « Dans quelle mesure la littérature africaine d'expression française reflète-t-elle les changements politiques de l'époque ? »", steps=[
            S("Partie 1 : avant les indépendances", text="Négritude and the novel of protest: identity and denunciation of colonisation (Césaire, Senghor, Oyono, Beti)."),
            S("Partie 2 : après les indépendances", text="New themes: disillusion, the state, family and tradition (Kourouma, Bebey)."),
            S("Partie 3 : limites", text="Literature does not only mirror politics: it also invents forms (a new use of French, humour, theatre) and personal stories. Evaluate."),
        ]),
        EX("Worked example 2 : appliquer à un sujet de société", intro="Question (as the Board's report encourages): « Les parents exercent-ils trop d'autorité sur les enfants dans votre société ? Appuyez-vous sur un texte étudié. »", steps=[
            S("Define the key word", text="The report notes that « parents » may include elders and the wider family, not only father and mother."),
            S("Partie 1 : le poids de l'autorité", text="Parents and elders choose or influence marriage, careers and behaviour (cite a precise moment from the text you have studied)."),
            S("Partie 2 : les effets", text="Respect, security and tradition, but also frustration and conflict between generations."),
            S("Partie 3 : nuance", text="Authority differs between families and times; dialogue may reconcile respect and personal choice."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving general ideas without the text", "The Board's report for Paper 2 says many candidates wrote general answers without facts from the text and scored very low. Always support each point with a precise event, a character or a line from the work you have studied."),
        MISTAKE("Confusing négritude and the post-independence novel", "Négritude (1930s onward) is mainly poetic and affirms identity. Post-independence writing (after about 1960) is often realistic, ironic and critical of African societies."),
        MISTAKE("Giving wrong dates or countries", "Césaire is from Martinique, Senghor from Senegal, Oyono and Beti from Cameroon, Kourouma from Côte d'Ivoire. Check your textbook before the exam."),
        TIP("Exam link: Paper 1 may test authors, movements and notions; Paper 2 (the Board's report) uses statements about society (gender equality, parental authority, the influence of the environment on politicians) to be discussed with set texts; Paper 3 essays on development also profit from this knowledge. Check which African texts your syllabus prescribes."),
        QUIZ("Who are the three founders usually associated with négritude?", [
            "Senghor, Kourouma and Oyono", "Césaire, Senghor and Damas", "Beti, Laye and Kane", "Bâ, Bebey and Beyala"], 1,
            "Césaire (Martinique), Senghor (Senegal) and Damas (Guyane) are the three most often named.",
            hint="Remember the Paris student journal of 1934.",
            feedback=["Kourouma and Oyono belong to later novelistic traditions.", "", "These are novelists of the 1950s and 1960s.", "These are later writers."]),
        QUIZ("Which statement best describes post-independence African writing in French?", [
            "It only praised the new states", "It often criticised corruption, authoritarian rule and the tension between tradition and modernity",
            "It was written only in poetry", "It ignored colonial history"], 1,
            "After 1960 many writers criticised their own societies as well as the colonial past.",
            hint="Think of Kourouma's title: Les Soleils des indépendances.",
            feedback=["Many writers expressed disappointment.", "", "The novel and theatre were central.", "Colonial history remained an important theme."]),
        PQ("Define négritude in two sentences and name its three founders.",
           "Négritude is a movement of Black writers in French, begun in Paris in the 1930s, which affirms the value of Black cultures and identity against colonial racism and assimilation. Its founders are Aimé Césaire, Léopold Sédar Senghor and Léon-Gontran Damas."),
        PQ("Explain the difference between the aims of Oyono's Une vie de boy and Senghor's poetry.",
           "Oyono's novel is a satire of colonial society: through the diary of a servant it shows the injustices and absurdities of colonial life, with irony. Senghor's poetry affirms African values, memory and beauty with a lyric voice and a musical rhythm. Both resist colonial views, one by satire and observation, the other by celebration and identity."),
        PQ("Discuss in one paragraph: « La littérature africaine après les indépendances a-t-elle trahi l'espoir de liberté ? »",
           "Plan: (1) Disillusion: writers such as Kourouma show the failure of the new state (corruption, authoritarianism); (2) But literature does not betray hope: criticism is a form of faith in change; (3) New forms (humour, theatre, women's voices) show the creative energy of independence. Conclusion: literature records disappointment and keeps the idea of freedom alive. Support with a work you have studied."),
        SUM("Négritude (1930s onward): Césaire, Senghor, Damas affirm Black identity and denounce colonialism; Présence africaine gives it a forum.",
            "Protest novels of the 1950s (Laye, Oyono, Beti) criticise colonial society.",
            "After independence (about 1960) writers such as Kane, Kourouma, Bebey and Bâ examine disillusion, tradition and modernity, family and gender.",
            "Cameroonian voices: Oyono, Beti, Oyono-Mbia, Bebey, Beyala.",
            "Always support an opinion with a precise fact from the text; avoid general answers."),
    ]))

# ------------------------------------------------------------------ 10. Paper 1 strategy
LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 1",
    title="Paper 1 : stratégie pour les 50 questions à choix multiples",
    slug="frl2-paper-1-strategy",
    minutes=22,
    summary="Paper 1 is 50 multiple-choice questions on grammar, vocabulary, expressions and literary notions. Learn the question types, a four-step method (read, decide, test, eliminate), the traps examiners use and a quick reference of literary notions.",
    objectives=[
        "State what Paper 1 tests, according to the Board's 2023 report",
        "Recognise the main question types (grammar, vocabulary, expressions, literary notions) and answer each with a method",
        "Eliminate wrong options by testing them in the sentence",
        "Use a reference list of literary notions (figures, registers, verse, genres) and manage time",
    ],
    key_concepts=["Paper 1", "Question à choix multiples", "Méthode de test", "Pièges", "Notions littéraires", "Gestion du temps"],
    blocks=[
        H("Introduction"),
        T("Imagine a Lower Sixth student in Yaoundé who knows the rules of the subjunctive and the movements of French literature but loses marks because of a rushed reading of a question. Paper 1 rewards both **knowledge** and **careful reading**."),
        D("According to the Board's 2023 subject report, Paper 1 is made of **50 multiple-choice questions** on **grammar, vocabulary, expressions and literary concepts and notions**. It tests the ability to recall, apply, analyse, synthesise and assess. The report says that the paper is not marked by the examination panel (so it gives no success rate). Check with your teacher the number of marks per question and whether wrong answers lose marks.", title="What the Board says"),
        T("Paper 1 covers the whole course. In your Lower Sixth year this includes advanced grammar and stylistics (subjonctif, conditionnel, pronoms relatifs composés, nominalisation, inversion), translation method (stylistique comparée, tenses and passive, idioms, thème and version), the dissertation method and the panorama of literature."),
        H("The four-step method"),
        KEY("Read, decide, test, eliminate", "Use the same four steps on every item.", cards=[
            ["1. Read the whole question", "Read the stem and the options before choosing. Look for words like NOT, EXCEPT, best, incorrect."],
            ["2. Decide what is tested", "Grammar rule? A word's meaning? An expression? A literary notion? Name it quickly."],
            ["3. Predict the answer", "Cover the options and think of the answer first; then look for it."],
            ["4. Test and eliminate", "Put each option in the sentence. Reject options that break the rule, then compare the remaining ones."],
        ]),
        EX("Worked example 1 : un item de grammaire", intro="Written for practice: « Bien qu'il ___ très fatigué, il a terminé le travail. » (a) est (b) soit (c) sera (d) serait", steps=[
            S("What is tested?", text="The mood after a conjunction: bien que."),
            S("Rule", text="Bien que is followed by the subjunctive."),
            S("Test", text="Only « soit » is the present subjunctive of être (il soit)."),
            S("Eliminate", text="« est » is indicative, « sera » future, « serait » conditional."),
            S("Answer", text="(b) soit."),
        ]),
        EX("Worked example 2 : un item sur une notion littéraire", intro="Written for practice: « Le silence est assourdissant. » Which figure of speech?", steps=[
            S("What is tested?", text="A figure of speech: two contradictory words are joined."),
            S("Test", text="Silence and assourdissant (deafening) contradict each other."),
            S("Name", text="Oxymore."),
            S("Eliminate", text="A comparison would use comme; a personification would give human traits to a thing; an anaphore repeats words at the start of sentences."),
        ]),
        H("A quick reference of literary notions"),
        CODE("""FIGURES
comparaison   deux éléments + outil (comme, tel) : « fort comme un lion »
métaphore     comparaison sans outil : « cet homme est un lion »
personnification   traits humains à une chose
antithèse     deux idées opposées rapprochées : « la vie et la mort »
oxymore       deux mots contradictoires : « un silence assourdissant »
hyperbole     exagération : « mort de faim »
litote        dire moins pour suggérer plus : « Ce n'est pas bête »
euphémisme    adoucir : « il nous a quittés »
anaphore      répétition en début de phrases ou de vers
gradation     suite croissante ou décroissante : « il marche, il court, il vole »
métonymie     le contenant pour le contenu : « boire un verre »
ironie        dire le contraire de ce que l'on pense

REGISTRES
lyrique (sentiments personnels)   tragique (destin fatal)   comique (rire)
satirique (critiquer en moquant)  épique (héroïsme)   pathétique (pitié)
polémique (attaquer)   didactique (instruire)   fantastique, réaliste

VERS ET FORMES
alexandrin 12 syllabes (césure 6/6)   octosyllabe 8   décasyllabe 10
rimes plates AABB, croisées ABAB, embrassées ABBA
rime masculine (sans e muet), féminine (e muet)
quatrain 4 vers, tercet 3 vers, sonnet = 2 quatrains + 2 tercets
enjambement, rejet, césure, hémistiche, strophe

GENRES
tragédie, comédie, drame, fable, conte, nouvelle, roman, essai, poème""", "text", title="Aide-mémoire", caption="Learn the terms and one example of each."),
        H("Typical traps"),
        MISTAKE("Choosing the first option that sounds right", "Some distractors are correct French in another context. Test every option in the sentence before deciding."),
        MISTAKE("Missing NOT, EXCEPT or INCORRECT", "A question may ask for the wrong sentence. Underline these words before reading the options."),
        MISTAKE("Confusing similar notions", "Métaphore against comparaison (is there a tool word?), litote against euphémisme (suggest more against soften), enjambement against rejet. Learn each pair together."),
        MISTAKE("Falling for faux amis", "In vocabulary questions, English-looking words trap you: actuellement, assister, librairie, éventuellement, sensible. Say the English meaning, then ask whether the French really means the same."),
        H("Managing time"),
        T("As a KKEVO practice setting, our mock gives 90 minutes for 50 questions, which is about 1.8 minutes per question. This is not a Board timing; check the real timing with your teacher. Answer the easy items first, mark the hard ones and come back, and never leave a question blank unless you know that wrong answers lose marks."),
        TIP("Exam link: Paper 1 is the only paper that covers all four Lower Sixth modules (grammar and stylistics, translation method, dissertation method and literary panorama). Revise by topic, then take a full timed mock. Check your results by topic to find weak areas."),
        QUIZ("A question asks: « Quelle phrase est INCORRECTE ? » What should you do?", [
            "Choose the correct sentence", "Underline INCORRECTE and look for the one wrong sentence",
            "Skip the question", "Choose the longest sentence"], 1,
            "A question can ask for the wrong sentence. Mark the word and look for the error.",
            hint="What does the capital word tell you?",
            feedback=["That would answer the opposite question.", "", "It is a normal question; do not skip it.", "Length does not decide correctness."]),
        QUIZ("« Il pleure comme une fontaine. » Which figure of speech is this?", [
            "Métaphore", "Comparaison", "Antithèse", "Litote"], 1,
            "There is a tool word (comme), so it is a comparaison. A métaphore would say « Il est une fontaine ».",
            hint="Look for comme.",
            feedback=["A métaphore has no tool word.", "", "There is no pair of opposites.", "A litote says less to suggest more."]),
        PQ("List the four types of item in Paper 1 and give one tip for each.",
           "Grammar: name the rule (mood, agreement, tense) and test each option in the sentence. Vocabulary: check the exact meaning and beware of faux amis. Expressions: learn idioms by their meaning, not word for word. Literary notions: memorise the definition with an example (comme = comparaison; opposites = antithèse)."),
        PQ("Why is a systematic elimination method useful in multiple-choice questions?",
           "It reduces the number of options with a reason each time, even if you do not know the answer at once. Rejecting options that break a rule makes the right one clearer and prevents you from choosing a plausible but wrong answer by impulse."),
        PQ("Explain how to answer: « Laquelle de ces phrases contient un enjambement ? »",
           "An enjambement is a sentence that continues from one line of verse to the next. So look for the option where the sense does not end at the end of the first line (the syntax overflows to the next line). A sentence that ends exactly with the line has no enjambement."),
        SUM("Paper 1 is 50 multiple-choice questions on grammar, vocabulary, expressions and literary notions (Board's 2023 report).",
            "Use the four steps: read, decide what is tested, predict, test and eliminate.",
            "Watch the traps: NOT and EXCEPT, faux amis, look-alike notions.",
            "Keep an aide-mémoire of figures, registers, verse forms and genres.",
            "Revise by topic and use timed mocks (90 minutes is a KKEVO setting)."),
    ]))

# ------------------------------------------------------------------ 11. Paper 2 strategy
LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 2",
    title="Paper 2 : la littérature (poésie, théâtre, prose) et l'analyse de texte",
    slug="frl2-paper-2-strategy",
    minutes=25,
    summary="Paper 2 is the literature paper (poetry, drama, prose). Learn the method for an unseen poem (structure externe and interne, tenses, lexical field, tone), how to answer a statement with evidence from the text, and the faults the Board's 2023 report names.",
    objectives=[
        "State what Paper 2 tests and the faults the Board's 2023 report lists",
        "Analyse an unseen poem with a fixed method",
        "Answer a question that gives a statement to discuss with evidence from a set text",
        "Plan a literary answer in French with a thesis, arguments, evidence and a conclusion",
    ],
    key_concepts=["Paper 2", "Poème à analyser", "Structure externe et interne", "Champ lexical", "Preuves tirées du texte", "Évaluer l'efficacité d'une technique"],
    blocks=[
        H("Introduction"),
        T("In the Board's 2023 report, the success rate in the sampled Paper 2 (literature) scripts was very low, about 9 percent. Candidates chose popular questions but did not use the text: they wrote general ideas that could apply to any book. This lesson shows how to avoid this."),
        D("The Board's report says Paper 2 is the **literature paper**, with sections for **poetry, drama and prose**. It tests recall and application, analysis, synthesis and judgement of literary techniques, concepts, themes and perspectives, points of view, characters and their portrayal, setting and the organisation of ideas. Check with your teacher how many questions you answer and which texts are prescribed.", title="What the Board says"),
        H("What went wrong (from the report)"),
        KEY("Faults the Board names", "Turn each fault into a rule for yourself.", cards=[
            ["No evidence from the text", "Candidates gave generalised answers not related to the work. Rule: every point needs a precise moment, character or line."],
            ["Listing techniques only", "They named narration, description and flashbacks but did not show how effective they are. Rule: technique, then effect."],
            ["Misreading the keyword", "Some did not see that « parents » could include elders in the village. Rule: define the key words of the question."],
            ["Not reading the books", "Many do not own or read the set texts. Rule: read each prescribed work fully, and take notes on characters, themes, techniques and setting."],
        ]),
        H("Method 1: the unseen poem"),
        T("The report says the unseen poem question was the most popular, yet most candidates failed it. The report expects the candidate to study the **structure externe**, the **structure interne**, the role of the verb **tenses**, the **lexical field** that shows an optimistic or pessimistic tone, the **advice** hidden in the poem and the **theme**. Here is a poem written for practice (original and invented)."),
        CODE("""LE FLAMBOYANT

Le soir descend sur le village,
Et l'arbre rouge brûle encore ;
Les chants s'éteignent sous l'ombrage,
Les braises rêvent de l'aurore.

Demain la pluie viendra, mon frère,
Et les pétales tomberont ;
Viens danser sur la terre claire,
Cueille la joie : les jours s'en vont.

Je chanterai tant que la braise
Gardera un peu de chaleur ;
Et quand la nuit sera mauvaise,
Tu garderas mon chant au cœur.""", "text", title="Poème pour l'analyse (original, écrit pour ce cours)"),
        EX("Worked example 1 : analyser le poème", intro="Analyse « Le flamboyant » with the method.", steps=[
            S("Structure externe", text="Three quatrains (twelve lines) of octosyllabes (8 syllables). Rimes croisées ABAB. Masculine and feminine rhymes alternate in strophes 2 and 3 (strophe 1 has only feminine rhymes)."),
            S("Structure interne", text="Strophe 1: the evening in a village, an image of the fire-coloured tree. Strophe 2: a warning about tomorrow and an invitation to live now. Strophe 3: the poet promises to sing while the fire lasts and asks his friend to keep the song."),
            S("Les temps", text="Present in strophe 1 (the scene), future and imperative in strophe 2 (announcement of loss, advice), future in strophe 3 (promise). The future announces a loss and a duty to keep a memory."),
            S("Champ lexical", text="Fire and light (brûle, braises, aurore, chaleur) against night, ending and loss (s'éteignent, tomberont, nuit, les jours s'en vont). The tone is melancholy but not hopeless."),
            S("Conseil du poème", text="« Cueille la joie »: enjoy the present because time passes (the idea of carpe diem)."),
            S("Thème et conclusion", text="The fleeting nature of time and the power of song and memory to resist it."),
        ]),
        H("Method 2: a statement to discuss with the text"),
        T("The report's themed questions give a statement and ask you to use a set text. Use a plan with placeholders that you fill from your own reading. Do not invent events: use only what you know from your own copy."),
        EX("Worked example 2 : plan avec preuves", intro="Question type (written for practice): « Les parents exercent trop d'autorité sur leurs enfants. Est-ce vrai dans l'œuvre que vous avez étudiée et dans votre société ? »", steps=[
            S("Define the key words", text="Parents (including elders and family), autorité (power to decide), trop (excess)."),
            S("Introduction", text="Amorce, the statement, a problématique such as: Dans quelle mesure l'autorité parentale aide-t-elle ou limite-t-elle la liberté des enfants ?"),
            S("Partie 1 : l'autorité dans le texte", text="Name the character, the decision and the event in your text [placeholder: moment of the work], and show the effect on the child."),
            S("Partie 2 : nuances", text="Show motives (protection, tradition) and moments of dialogue or resistance in the text [placeholder]."),
            S("Partie 3 : votre société", text="Give examples from your environment: education, marriage, career choices; discuss when authority protects and when it blocks."),
            S("Conclusion", text="A balanced answer and a wider idea."),
        ]),
        H("Method 3: evaluating a technique"),
        T("When asked to show that a technique (narration, description, flashback, point of view) is effective, follow four steps: **define it**, **find a precise example**, **explain what it does** (reveals a character, creates suspense, helps understanding) and **evaluate its importance** for the work. For example: « Le retour en arrière révèle le passé du personnage et explique ses réactions présentes. »"),
        MISTAKE("Retelling the story", "The examiner knows the story. Use the plot only to prove a point."),
        MISTAKE("Mixing up characters or inventing facts", "A wrong name or event shows you have not read the work. Use only what you can check in your own copy."),
        MISTAKE("An unseen poem answer made of a list", "Naming the number of lines and the rhymes is only the start. Link form, tenses and vocabulary to the meaning."),
        MISTAKE("Neglecting the prescribed poems", "The report advises teachers to teach the selected poems of Baudelaire and not only the unseen poem. Prepare both types."),
        TIP("Exam link: Paper 2 questions in the Board's 2023 report ask for analysis (themes, characters, setting), evaluation (effect of techniques) and discussion of statements, in sections on poetry, drama and prose. Practise one unseen poem per week and one themed essay plan per text. Check with your teacher the exact format."),
        QUIZ("In the poem « Le flamboyant », what is the function of the future tense in strophe 2?", [
            "It describes the present scene", "It announces a coming loss and supports the advice to enjoy the present",
            "It tells a past memory", "It expresses a wish for the past"], 1,
            "The future (viendra, tomberont) announces rain and the fall of the petals, which explains the invitation to live now.",
            hint="What do viendra and tomberont predict?",
            feedback=["The present tense describes the scene in strophe 1.", "", "A past memory would use a past tense.", "No wish for the past is expressed."]),
        QUIZ("According to the Board's report, what is a frequent weakness in the essays on set texts?", [
            "Writing too many quotations", "Giving general answers without facts from the text", "Writing in English", "Writing too neatly"], 1,
            "The report says candidates could not use facts from the text and gave generalised answers.",
            hint="Think of evidence.",
            feedback=["Too many quotations is not the main weakness named.", "", "Language was not the main issue named for the literature paper.", "Neatness is not discussed."]),
        PQ("Give the five steps of the method for an unseen poem.",
           "1. Structure externe (strophes, vers, syllables, rimes). 2. Structure interne (meaning strophe by strophe). 3. Temps verbaux and their role. 4. Champ lexical and tone (optimistic or pessimistic). 5. Theme, advice or message, and a conclusion linking form and meaning."),
        PQ("Write a thesis sentence in French for an essay on the effectiveness of flashback in a novel you have studied.",
           "Possible answer: « Le retour en arrière est un procédé efficace parce qu'il éclaire le passé du personnage, explique ses actes présents et maintient l'intérêt du lecteur. » Then prove each of the three ideas with a precise moment of your text."),
        PQ("A statement (written for practice) says: « Une femme peut accomplir tout ce qu'accomplit un homme. » Give a plan using a set text with placeholders.",
           "Intro: define the statement (équité entre l'homme et la femme) and ask: dans quelle mesure est-elle vraie dans l'œuvre et dans votre localité ? Part 1: areas of equality (education, work, responsibility) in the text [placeholder events]. Part 2: limits (traditions, expectations, unequal duties) in the text [placeholder]. Part 3: your society, with examples. Conclusion: a nuanced judgement. Fill the placeholders with facts from your own copy."),
        SUM("Paper 2 is the literature paper; the Board's report notes low success because answers lacked evidence from the text.",
            "Unseen poem: structure externe, structure interne, temps, champ lexical and tone, advice or theme.",
            "Statement questions: define the key words, use a plan with precise events from the text, then relate to your society.",
            "For a technique: define, give an example, explain the effect, evaluate.",
            "Read the set texts and the selected poems fully; do not retell the story and do not invent facts."),
    ]))

# ------------------------------------------------------------------ 12. Paper 3 strategy
LESSONS.append(lesson(
    module=M_EXAM, topic="Paper 3",
    title="Paper 3 : l'expression écrite et la traduction",
    slug="frl2-paper-3-strategy",
    minutes=24,
    summary="Paper 3 combines an essay on a life situation (choose one of four) and a translation. Learn how to read the situation, choose the topic, plan, write with the right register, avoid the language faults the Board names, and translate by units of meaning.",
    objectives=[
        "State the structure of Paper 3 and the lessons of the Board's 2023 report",
        "Choose an essay topic by vocabulary and plan it by the situation (debate, talk, report)",
        "Write with the right register and avoid the faux amis and vocabulary gaps the Board notes",
        "Translate a short text by units of meaning and proofread the result",
    ],
    key_concepts=["Paper 3", "Situation de communication", "Choisir son sujet", "Registre et format", "Vocabulaire thématique", "Traduction par unités de sens"],
    blocks=[
        H("Introduction"),
        T("Paper 3 tests whether you can **communicate in writing**. In the Board's 2023 report, performance in Paper 3 was better than in the literature paper, which the report links to essay topics drawn from life situations and to a general awareness of the French language. The two main difficulties it names are **language** (vocabulary, grammar, sentence construction) and **misreading the question**."),
        D("According to the Board's 2023 report, Paper 3 is **Essay Writing and Translation**. It offers **four life situations** from which the candidate chooses **one** essay, and a **translation** task. The 2023 essay subjects included the choice between textbooks and digital books, the consequences of climate change, prevention and treatment of pandemics, and what leaders can do against underdevelopment. The translation texts were on migration, birth control, electrical equipment in households and famine; the report notes that translating from French into English helped candidates. Check with your teacher the exact format for your year.", title="What the Board says"),
        H("Part A: the essay on a life situation"),
        KEY("Read the situation", "The sujet is often a role: a debate, a talk, a report. Identify the role.", cards=[
            ["Un débat (pour ou contre)", "Take a clear side at once, give arguments with examples, and answer the best opposing argument. Address the audience (« Mesdames et Messieurs », « chers camarades »)."],
            ["Une conférence ou une sensibilisation", "Explain the problem briefly, then give practical measures (prevention first, then what to do if the problem happens). Speak to the audience."],
            ["Un rapport", "Be organised and factual: introduction, findings in ordered parts, recommendations, conclusion."],
            ["Un texte à partir duquel on discute", "Use the ideas of the text as a starting point, then add your own arguments."],
        ]),
        T("**Choosing the topic.** Pick the subject for which you know the **vocabulary**, not the one that looks easiest. The report says candidates understood questions on climate change and underdevelopment but lacked words. List ten key words in French for each topic when you revise: climate (réchauffement, sécheresse, inondation), health (prévention, dépistage, vaccin, hygiène), development (infrastructures, gouvernance, éducation, pauvreté)."),
        EX("Worked example 1 : planifier un essai sur une situation", intro="Situation (written for practice): « Lors d'une conférence dans votre quartier, vous parlez de la prévention des maladies contagieuses. Présentez votre exposé. »", steps=[
            S("Analyse", text="Role: speaker at a community conference. Key words: prévention, maladies contagieuses. Audience: residents."),
            S("Introduction", text="Greet the audience, explain why the subject matters (health and economy) and announce the plan."),
            S("Partie 1 : comprendre le risque", text="What is a contagious disease; how it spreads; difference between épidémie and pandémie."),
            S("Partie 2 : mesures de prévention", text="Hygiene (lavage des mains), eau potable, vaccination, information, surveillance."),
            S("Partie 3 : que faire si l'on est malade ?", text="Consult a health centre, isolate if advised, follow treatment, do not self-medicate. Real treatment depends on the disease and a qualified health worker."),
            S("Conclusion", text="A call to act together."),
        ]),
        H("Part B: the translation"),
        T("Translation is not word for word. Use these steps. **1. Read the whole text** and grasp the subject. **2. Cut into units of meaning** (not individual words). **3. Translate each unit** into natural target language, checking tenses, articles and faux amis. **4. Reread** the whole translation as if it were an original text. **5. Check** that nothing is missing or added."),
        EX("Worked example 2 : traduire par unités de sens", intro="Translate into English (written for practice): « Depuis plusieurs années, la sécheresse oblige de nombreuses familles à quitter leur village. »", steps=[
            S("Units", text="Depuis plusieurs années | la sécheresse | oblige | de nombreuses familles | à quitter leur village."),
            S("Tense", text="« Depuis » with a present means an action that began in the past and continues: English uses the present perfect (has been forcing)."),
            S("Translate", text="« For several years, drought has been forcing many families to leave their villages. »"),
            S("Check", text="« Their village » becomes « their villages » in English because many families have many villages; « de nombreuses » is « many »."),
        ]),
        H("Common language faults"),
        MISTAKE("Poor vocabulary for the topic", "The report states that language was the main difficulty. Learn lists of key words for the likely themes (environment, health, education, development, technology)."),
        MISTAKE("Confusing similar words", "The report notes that candidates did not distinguish épidémie from pandémie. Learn pairs like this."),
        MISTAKE("Answering the topic, not the question", "On the textbooks question some candidates wrote about tradition or about technology in general. Link every paragraph to the question."),
        MISTAKE("Word-for-word translation", "A literal translation often gives a wrong or odd sentence. Translate the meaning: « Il y a trois jours » is « three days ago », not « it has three days »."),
        TIP("Exam link: Paper 3 (essay and translation) uses everything from the dissertation lessons (analyse, problématique, plan, introduction and conclusion) and from the translation module. Practise one essay plan per day and one short translation per day. Check the exact format with your teacher."),
        QUIZ("A situation says: « Vous participez à un débat : pour ou contre le livre numérique à l'école ? » What should the first paragraph include?", [
            "A long history of printing", "A clear position (for or against), the reason for the debate and the plan", "A poem", "A translation in English"], 1,
            "In a debate you announce your position clearly, say why the issue matters and announce your arguments.",
            hint="Think of a speaker beginning a debate.",
            feedback=["It is not the question.", "", "It is not relevant.", "Not relevant to the task."]),
        QUIZ("How do you translate « Cela fait deux ans que j'habite ici » ?", [
            "It makes two years that I live here", "I have been living here for two years", "I lived here two years", "It does two years I live here"], 1,
            "A present tense with « cela fait... que » describes a situation continuing from the past: present perfect continuous in English.",
            hint="The action started two years ago and continues now.",
            feedback=["A word-for-word calque; not English.", "", "That suggests it ended.", "A word-for-word calque; not English."]),
        PQ("Choose one of these topics and give a three-part plan in French: (a) the consequences of climate change; (b) what leaders should do against underdevelopment.",
           "Possible plan for (a): 1. Conséquences sur l'environnement (sécheresse, inondations). 2. Conséquences économiques et sociales (agriculture, famine, migrations). 3. Réponses possibles (reboisement, énergies propres, éducation, coopération internationale). Possible plan for (b): 1. Mesures politiques (gouvernance, lutte contre la corruption). 2. Mesures économiques (routes, énergie, agriculture). 3. Mesures sociales (éducation, santé). Each part with two arguments and an example."),
        PQ("Translate into French: « Many young people are looking for work in the cities. »",
           "« De nombreux jeunes cherchent du travail dans les villes. » or « Beaucoup de jeunes cherchent un emploi en ville. » Check: « are looking for » is a present tense (cherchent), not « sont cherchant »; « work » is travail or emploi (uncountable); and « young people » is « jeunes » (often with « de nombreux »)."),
        PQ("Explain why a student should choose the essay topic by vocabulary.",
           "The Board's report says that language, not understanding, was the main difficulty on several topics. A student who knows the words for a topic can write precise, varied sentences and avoids repeating a few words. Choosing by vocabulary raises accuracy and clarity, which examiners reward."),
        SUM("Paper 3 (Board's 2023 report): four life situations (choose one essay) and a translation.",
            "Read the situation: debate, talk or report; adapt the form and register.",
            "Choose the topic you have words for; prepare lists of key vocabulary by theme.",
            "Translate by units of meaning, checking tenses and faux amis; avoid word-for-word.",
            "Plan, write, then proofread: agreements, verb forms, accents, connectors."),
    ]))
