"""Form 5 French (O Level 0545): Compréhension Écrite et Traduction, Expression Écrite and Examination.

Draft content. Exam facts stated are only those of the Board's 2023 report: Paper 1 = 50 multiple-choice questions, 40% of the
examination, whole syllabus, marked electronically; Paper 2 = Question 1 Translation and Question 2 Essay (140-150 words, one of
three topics); the four marking criteria (pertinence, coherence, correction de la langue, originalite); the penalised errors it names.
Reading passages, translations, model letters and essays are KKEVO originals; names and places are invented.
Timings of the mocks are KKEVO practice settings.
"""

from .dsl import *  # noqa: F403

COURSE = ("french", "form-5")

M_READ = "Compréhension Écrite et Traduction"
M_WRITE = "Expression Écrite"
M_ESSAY = "Expression Écrite"
M_EXAM = "Examination"

LESSONS = [
    # ------------------------------------------------------------------ 1. Reading comprehension strategies
    lesson(
        module=M_READ, topic="Reading comprehension strategies",
        title="Reading a French text: skim, scan and find the answer",
        slug="fr3-reading-strategies",
        minutes=22,
        summary="A step-by-step method for reading a short French text: look at the title, skim for the general idea, "
                "read the questions, scan for the key words, and guess unknown words from the context.",
        objectives=[
            "Use skimming and scanning to find information quickly in a French text",
            "Recognise what each French question word (Qui ? Où ? Quand ? Pourquoi ? Comment ?) asks for",
            "Guess the meaning of an unknown word from the words around it",
            "Tell the difference between an answer found in the text and an answer inferred from it",
        ],
        key_concepts=["Skimming", "Scanning", "Mots interrogatifs", "Inference", "Contexte"],
        blocks=[
            H("Introduction"),
            T("Imagine you are at the gare routière in Bafoussam and you see a notice in French about a change of departure time. "
              "You do not read every word. You look for the town, the hour and the price. That is exactly how a good reader "
              "treats a French text in an examination."),
            T("In this course, explanations are in English, but every French text and question is in French. The skills here help "
              "you with the reading parts of the examination and with the vocabulary and grammar items that depend on a passage. "
              "In 2023 the Board's Paper 1 had 50 multiple-choice questions on the whole Ordinary Level syllabus, so a short "
              "passage followed by questions is a very familiar kind of item."),
            D("**Skimming** means reading quickly to get the general idea (the subject, the people, the place, the mood). "
              "**Scanning** means running your eyes over the text to find one precise piece of information, such as a name, "
              "a number or a place.", title="Two reading skills"),
            H("A method in five steps"),
            KEY("Read in this order", "Do not start translating the text word by word. Follow these steps.", cards=[
                ["1. Titre et contexte", "Look at the title and any first line. What is the text about?"],
                ["2. Lecture rapide", "Skim the whole text once. Who? Where? When? What happens?"],
                ["3. Les questions", "Read each question and underline the question word."],
                ["4. Retour au texte", "Scan for the key words of each question, then read that part carefully."],
                ["5. Vérification", "Check that your answer fits the question and makes sense in the whole text."],
            ]),
            H("Question words tell you what to look for"),
            CODE("""Qui ?        -> une personne        Mireille, sa grand-mère
Où ?         -> un lieu             au marché de Bafoussam
Quand ?      -> un moment           le samedi matin, avant midi
Pourquoi ?   -> une cause           parce que, car, à cause de
Comment ?    -> une manière         doucement, avec patience
Combien ?    -> un nombre, un prix  trois mangues, 500 francs
Que fait... ? -> une action         elle porte le panier""", "text", title="Mots interrogatifs"),
            T("Read the passage below carefully. It was written for KKEVO to practise these skills. First skim it, then answer "
              "the questions that follow."),
            CODE("""Le marché du samedi

Chaque samedi matin, Mireille accompagne sa grand-mère au
marché de Bafoussam. Elles partent très tôt, avant que le soleil
ne soit trop chaud. Grand-mère achète toujours les mêmes choses :
des tomates, des oignons, du poisson fumé et un peu de piment.
Mireille porte le panier. Au marché, les vendeuses connaissent
bien la vieille dame et lui offrent souvent un petit cadeau,
une banane ou une mangue. Aujourd'hui, pourtant, il y a un
problème : les prix ont augmenté parce que la pluie a abîmé
une partie des récoltes. Grand-mère discute longtemps avec la
marchande de tomates et finit par obtenir un prix raisonnable.
En rentrant, Mireille lui dit qu'elle admire sa patience.
Grand-mère sourit et répond que, pour bien acheter, il faut
savoir parler doucement et attendre le bon moment.""", "text", title="Texte 1"),
            EX("Exemple 1 : trouver une information précise", intro="Question : Pourquoi les prix sont-ils plus élevés aujourd'hui ?", steps=[
                S("Underline the question word", text="Pourquoi ? asks for a cause."),
                S("Scan for the key word", text="Look for « prix ». You find « les prix ont augmenté » in the middle of the text."),
                S("Read around it", text="The same sentence continues with « parce que la pluie a abîmé une partie des récoltes »."),
                S("Check the answer", text="The cause is the rain, which damaged part of the harvest."),
            ]),
            EX("Exemple 2 : deviner un mot", intro="Question : Que veut dire « abîmé » dans le texte ?", steps=[
                S("Find the word in its sentence", text="« la pluie a abîmé une partie des récoltes »."),
                S("Ask what rain can do to crops", text="Rain does not usually help a harvest when the prices go up: the sentence explains a problem."),
                S("Decide", text="« Abîmer » means to damage or spoil. The context gives the meaning even without a dictionary."),
            ]),
            TIP("Learn to use clues around a word: the word before it, the word after it, the connector (« parce que », « pourtant ») "
                "and whether the sentence is good news or bad news."),
            H("Found in the text or worked out from the text?"),
            T("Some answers are written plainly in the text (a name, a place, a reason). Others must be worked out. For example, the text "
              "never says that the vendors like Grand-mère, but it says they know her well and offer her small gifts. From these facts you "
              "can infer that they respect her."),
            D("An **inference** is a conclusion you draw from clues in the text when the text does not say it directly. Always be able to "
              "point to the clue in the text.", title="Inférer"),
            MISTAKE("Answering from your own experience", "Do not add what you know about markets in general. The question asks what this "
                    "text says. If you cannot point to a sentence or clue in the passage, your answer is probably not what the examiner wants."),
            MISTAKE("Stopping at the first key word", "The first place where the key word appears may not hold the answer. In Texte 1 the word "
                    "« prix » could also mislead you at « un prix raisonnable ». Read the whole sentence and the one before it."),
            MISTAKE("Translating the whole text first", "Translating every word takes a long time and you may still miss the question. "
                    "Skim, then answer the questions one by one."),
            QUIZ("Dans Texte 1, que fait Mireille pendant les achats ?",
                 ["Elle négocie le prix des tomates.", "Elle porte le panier.", "Elle offre une mangue à la marchande.", "Elle cuisine du poisson fumé."],
                 1, "The text says « Mireille porte le panier ». It is Grand-mère who discusses the price, and the vendors who give gifts.",
                 hint="Scan for the name « Mireille ».",
                 feedback=["It is the grand-mother who discusses the price with the tomato seller.", "",
                           "The vendors offer small gifts to the old lady, not the reverse.", "Cooking is not mentioned in the text."]),
            QUIZ("Dans Texte 1, quel est le sens de « pourtant » dans la phrase « Aujourd'hui, pourtant, il y a un problème » ?",
                 ["Il introduit une cause : à cause de.", "Il introduit une opposition : le jour est différent des autres.", "Il introduit un lieu : à côté de.", "Il introduit une conclusion : donc."],
                 1, "« Pourtant » means however or yet. It shows that today does not follow the usual pattern: there is a problem.",
                 hint="Compare « chaque samedi » (the usual day) and « aujourd'hui ».",
                 feedback=["The cause comes later, after « parce que ».", "", "« Pourtant » has nothing to do with place.", "« Donc » would show a result; « pourtant » shows contrast."]),
            H("Practice"),
            PQ("Dans Texte 1, à quel moment de la journée les deux personnes partent-elles au marché, et pourquoi ?",
               "Elles partent le matin, très tôt, avant que le soleil ne soit trop chaud (pour éviter la chaleur)."),
            PQ("Dans Texte 1, que fait Grand-mère pour obtenir un bon prix ? Répondez avec vos propres mots.",
               "Elle discute longtemps avec la marchande de tomates, avec calme et patience, jusqu'à obtenir un prix raisonnable."),
            PQ("Dans Texte 1, quelle leçon Grand-mère donne-t-elle à Mireille à la fin ? Cette réponse est-elle écrite telle quelle ou faut-il l'inférer ?",
               "Pour bien acheter, il faut parler doucement et savoir attendre le bon moment. Cette idée est donnée par Grand-mère elle-même, donc elle est dans le texte, mais l'élève doit la reformuler."),
            PQ("Dans Texte 1, que pensent les vendeuses de Grand-mère ? Justifiez votre réponse par un indice du texte.",
               "Elles la respectent et l'apprécient : elles la connaissent bien et lui offrent souvent un petit cadeau. Cette réponse est une inférence."),
            SUM("Skim first for the general idea, then read the questions, then scan for key words and read that part carefully.",
                "The question word (Qui ? Où ? Quand ? Pourquoi ? Comment ? Combien ?) tells you what kind of answer to find.",
                "Guess unknown words from the context: the sentence, the connector and the mood of the passage.",
                "Separate what the text says plainly from what you infer, and always keep a clue from the text to support your answer.",
                "Never answer from your own general knowledge only, and never translate the whole text first."),
        ],
    ),
    # ------------------------------------------------------------------ 2. Answering without lifting
    lesson(
        module=M_READ, topic="Answering in French without lifting",
        title="Answering comprehension questions in your own French",
        slug="fr3-answering-in-own-words",
        minutes=24,
        summary="How to answer a French comprehension question in a complete sentence of your own: find the evidence, "
                "change the structure and vocabulary, adjust pronouns and verbs, and avoid copying the text.",
        objectives=[
            "Explain why copying a sentence from the text (lifting) is not a good answer",
            "Rebuild an answer using synonyms, a new sentence structure and correct pronouns",
            "Change the person and tense of a verb when the question changes the point of view",
            "Write short, complete answers in correct French",
        ],
        key_concepts=["Reformulation", "Lifting", "Synonyme", "Phrase complète", "Changement de pronom"],
        blocks=[
            H("Introduction"),
            T("A friend asks you, \"Why was the bus late?\" You do not read the notice aloud; you explain in your own words. A French "
              "comprehension question works the same way: the examiner wants to see that you understood the text, not that you can copy it."),
            D("**Lifting** means copying a sentence or part of a sentence from the text as your answer. **Reformulation** means expressing the "
              "same idea in your own words. Examiners reward understanding and correct French of your own.", title="Reformuler"),
            T("Read this short text. It is original, written for KKEVO."),
            CODE("""Le voyage en car

Samedi dernier, Landry a pris le car pour aller de Douala à
Yaoundé voir son oncle. À la gare routière, il y avait beaucoup
de monde et le départ a été retardé d'une heure parce qu'un
pneu était crevé. Le chauffeur a réparé le pneu sans se
plaindre, puis le car a démarré. Pendant le trajet, un vieil
homme a offert des arachides à tous les voyageurs. Landry a
remercié le vieil homme et a discuté avec lui de la vie au
village. Vers midi, le car s'est arrêté à Édéa pour que les
passagers puissent manger. Landry a acheté du bâton de manioc
et une bouteille d'eau. Il est arrivé à Yaoundé à la fin de
l'après-midi, fatigué mais content. Son oncle l'attendait
devant la gare avec un grand sourire.""", "text", title="Texte 2"),
            H("Four tools for reformulating"),
            KEY("Four ways to change the text", "Use at least two of them in each answer.", cards=[
                ["Synonyme", "Replace a word with another of the same meaning: « fatigué » becomes « épuisé », « content » becomes « heureux »."],
                ["Autre structure", "Turn the verb into a noun: « le départ a été retardé » becomes « le départ a eu du retard »."],
                ["Pronoms", "Replace names by pronouns when the question has already named them."],
                ["Verbe de la question", "Start your answer with the words of the question (but not the text's long phrase), then add the new information."],
            ]),
            EX("Exemple 1 : une cause",
               intro="Question : Pourquoi le départ du car a-t-il été retardé ?",
               steps=[
                   S("Find the evidence", text="« le départ a été retardé d'une heure parce qu'un pneu était crevé »."),
                   S("A lifted answer would be", text="« Parce qu'un pneu était crevé. » This copies the text."),
                   S("Rebuild it", text="Replace the verb with a noun and use a different connector: « à cause d'une crevaison »."),
                   S("Write a complete sentence", text="« Le départ a eu du retard à cause d'une crevaison. »"),
               ]),
            EX("Exemple 2 : une action",
               intro="Question : Qu'a fait le vieil homme pendant le voyage ?",
               steps=[
                   S("Find the evidence", text="« un vieil homme a offert des arachides à tous les voyageurs »."),
                   S("Change the verb", text="« offrir » can become « partager » or « donner »."),
                   S("Change the structure", text="Keep the key fact, the peanuts, but express it differently."),
                   S("Write the answer", text="« Il a partagé ses arachides avec les passagers. »"),
               ]),
            EX("Exemple 3 : un sentiment",
               intro="Question : Dans quel état Landry est-il arrivé à Yaoundé ?",
               steps=[
                   S("Find the evidence", text="« fatigué mais content »."),
                   S("Use synonyms", text="« fatigué » becomes « épuisé »; « content » becomes « heureux »."),
                   S("Write the answer", text="« Il était épuisé, mais heureux. » Note the imperfect: it describes a state."),
               ]),
            H("Pronouns, tenses and complete sentences"),
            T("A good answer is a complete sentence with a subject and a verb. Do not answer « Parce que » alone, unless the question asks for a "
              "short phrase. Use a pronoun when the person has already been named in the question: « Landry » becomes « il », « le vieil homme » "
              "becomes « il », « les passagers » becomes « ils »."),
            T("When the question is in the passé composé (« Qu'a fait... ? »), your answer is also in the passé composé. When the question "
              "describes a state or habit, use the imparfait. Keep the tense of the text unless the question changes it."),
            KEY("A good answer checklist", "Before you move on, ask yourself these questions.", cards=[
                ["Complete ?", "Does it have a subject and a verb?"],
                ["Own words ?", "Have I changed at least some words or the structure?"],
                ["Accurate ?", "Does it match the text, without adding things the text does not say?"],
                ["Correct French ?", "Agreements of adjectives and past participles, accents, verb endings."],
            ]),
            MISTAKE("Changing the meaning while changing the words", "If the text says the delay was one hour, do not write « un jour » or "
                    "forget the cause. Reformulate, but keep the facts the same."),
            MISTAKE("Lifting half a sentence", "Writing « d'une heure parce qu'un pneu était crevé » copies the text and does not fit your "
                    "sentence grammatically. Always build a new, complete sentence."),
            MISTAKE("Forgetting agreements", "In « Ils étaient fatigués », the adjective agrees with the plural subject. In « Elle est "
                    "partie », the past participle agrees with a feminine subject because « partir » uses être."),
            QUIZ("Question : Pourquoi le car s'est-il arrêté à Édéa ? Quelle réponse reformule bien le texte ?",
                 ["Pour que les passagers puissent manger.",
                  "Pour permettre aux voyageurs de se restaurer.",
                  "Parce que les passagers pouvaient manger.",
                  "Le car s'est arrêté à Édéa vers midi."],
                 1, "The second answer keeps the idea (a stop for a meal) with new words: « permettre », « voyageurs », « se restaurer ».",
                 hint="Which answer gives the reason without copying the sentence of the text?",
                 feedback=["It copies the text exactly.", "",
                           "It changes the logic: « parce que » is wrong; the stop is made so that passengers can eat.",
                           "It answers when and where, not why."]),
            QUIZ("Question : Qui attendait Landry devant la gare ? Quelle réponse est la meilleure ?",
                 ["Son oncle l'attendait devant la gare avec un grand sourire.",
                  "Son oncle.",
                  "Son oncle, qui était content de le voir, l'attendait à la gare.",
                  "Il attendait son oncle."],
                 2, "The third answer is a complete sentence with new words. It adds « content de le voir », which is a reasonable inference from « un grand sourire ». The first copies the text, the second is not a sentence, and the fourth reverses the roles.",
                 hint="Who is waiting, and who is arriving?",
                 feedback=["It copies the whole sentence of the text.", "It is correct but it is not a sentence; do not rely on it when full sentences are asked for.",
                           "", "It reverses the roles: Landry is the one who arrives."]),
            H("Practice"),
            PQ("Question : Que fait le chauffeur quand le pneu est crevé ? Répondez avec vos propres mots.",
               "Il répare le pneu calmement, sans protester. On peut aussi écrire : « Il a changé la roue sans se plaindre ». Évitez de copier « a réparé le pneu sans se plaindre »."),
            PQ("Question : Comment Landry a-t-il passé le temps pendant le trajet ?",
               "Il a bavardé avec un vieil homme et lui a parlé de la vie au village. Il a aussi accepté ses arachides."),
            PQ("Question : Quelle est la profession de l'homme qui attendait Landry ? Le texte répond-il à cette question ?",
               "Le texte ne le dit pas. Il dit seulement que l'homme est l'oncle de Landry. Quand le texte ne répond pas, ne l'inventez pas."),
            PQ("Reformulez cette phrase du texte : « Le chauffeur a réparé le pneu sans se plaindre. »",
               "Par exemple : « Le conducteur a remis le pneu en état sans protester. » ou « Le chauffeur a changé le pneu calmement. »"),
            SUM("Lifting is copying from the text; the examiner wants your own French.",
                "Reformulate by changing words (synonyms), structure (verb to noun) and pronouns, but keep the facts the same.",
                "Write a complete sentence with a subject and a verb; match the tense of the question.",
                "Keep checking agreements, accents and verb endings in your own sentence.",
                "If the text does not answer the question, do not invent an answer."),
        ],
    ),
    # ------------------------------------------------------------------ 3. Thème
    lesson(
        module=M_READ, topic="Translation into French (thème)",
        title="Thème: translating a story from English into French",
        slug="fr3-theme-into-french",
        minutes=25,
        summary="How to translate an English narrative into correct French: choose the right past tenses, add the articles English leaves out, "
                "get gender and agreement right, and avoid faux amis and word-for-word translation.",
        objectives=[
            "Follow a method for translating an English passage into French sentence by sentence",
            "Choose between imparfait, passé composé and plus-que-parfait for English past forms",
            "Add the articles that French needs and make adjectives and participles agree",
            "Avoid common faux amis and English-shaped French (calques)",
        ],
        key_concepts=["Thème", "Faux amis", "Imparfait", "Passé composé", "Plus-que-parfait", "Calque"],
        blocks=[
            H("Introduction"),
            T("**Thème** is the French word for translation from English into French. In Paper 2, Question 1 is a translation. In its 2023 report "
              "the Board says the passage was a story told in the past, needing the imperfect (about five times), a main narrative past tense "
              "(passé composé or passé simple), one simple present and four pluperfects. Most candidates translated the vocabulary well; the "
              "marks were lost when they mixed up the tenses, and when a few recopied the text or paraphrased it instead of translating."),
            T("So the skill that matters most is choosing the right tense. Next come articles, gender and agreement, and faux amis."),
            D("A **faux ami** (false friend) is a French word that looks like an English word but means something different. "
              "A **calque** is a phrase translated word for word from English that no French speaker would say.", title="Pièges"),
            H("A method for every sentence"),
            KEY("Five steps for each sentence", "Work sentence by sentence, not word by word.", cards=[
                ["1. Understand", "Read the whole passage first. Who does what, and when?"],
                ["2. Find the tenses", "Underline each verb and ask: background (imparfait), event (passé composé) or earlier event (plus-que-parfait)?"],
                ["3. Translate the meaning", "Say the idea in natural French. Do not follow English word order blindly."],
                ["4. Add what French needs", "Articles, gender, agreements, accents."],
                ["5. Check", "Reread the French only. Does every verb have a subject, and does the tense fit?"],
            ]),
            H("Choosing the tense"),
            CODE("""English                       Idea                  Français
it was raining                background / action   Il pleuvait (imparfait)
in progress or description
she left the house            one finished event    Elle est sortie (passé composé)
she had forgotten             earlier than the      Elle avait oublié (plus-que-parfait)
                              past event
she used to walk              habit in the past     Elle marchait (imparfait)
she is tired                  present state         Elle est fatiguée (présent)""", "text", title="Les temps du passé"),
            T("In the passé composé, verbs of movement and reflexive verbs use être: « elle est sortie », « elle est arrivée », « ils sont partis ». "
              "The past participle agrees with the subject. Most other verbs use avoir: « elle a couru », « elle a attendu », « elle a pris ». "
              "Check the choice of the narrative tense with your teacher, and keep the same one through the whole passage. The passé composé is the "
              "safest choice for everyday narration."),
            KEY("Articles and agreement", "English often drops the article; French does not.", cards=[
                ["General ideas", "Life is hard = La vie est dure. I like rice = J'aime le riz."],
                ["Professions", "She is a teacher = Elle est professeure (no article after être with a profession)."],
                ["Gender", "Learn the noun with its article: le bus, la maison, le parapluie, la rue."],
                ["Adjectives", "Agree with the noun: des chaussures mouillées (feminine plural)."],
            ]),
            EX("Exemple 1 : un passage au passé",
               intro="Traduisez en français : It was raining when Aïcha left the house. She had forgotten her umbrella, so she ran to the bus stop.",
               steps=[
                   S("Find the tenses", text="« was raining » is a background action: imparfait. « left » is a finished event: passé composé. « had forgotten » is earlier: plus-que-parfait. « ran » is a finished event: passé composé."),
                   S("Translate the first sentence", text="« Il pleuvait quand Aïcha est sortie de la maison. » (sortir takes être; Aïcha is feminine, so « sortie »)."),
                   S("Translate the second sentence", text="« Elle avait oublié son parapluie, alors elle a couru jusqu'à l'arrêt de bus. »"),
                   S("Check", text="Imparfait for « pleuvait », plus-que-parfait for « avait oublié », passé composé for « est sortie » and « a couru »."),
               ]),
            EX("Exemple 2 : la suite du passage",
               intro="Traduisez : When she arrived, the bus had already left. She was tired and her shoes were wet, but she did not give up. She waited for an hour, then took a taxi to school.",
               steps=[
                   S("Sentence 1", text="« Quand elle est arrivée, le bus était déjà parti. » The bus had left earlier than she arrived: plus-que-parfait of partir (être). Here « parti » is masculine singular like « le bus »."),
                   S("Sentence 2", text="« Elle était fatiguée et ses chaussures étaient mouillées, mais elle n'a pas abandonné. » States of being are in the imparfait; the decision not to give up is an event."),
                   S("Sentence 3", text="« Elle a attendu une heure, puis elle a pris un taxi pour aller à l'école. »"),
                   S("Check", text="Fatiguée (feminine singular), mouillées (feminine plural, because « chaussures » is feminine plural), and « pour aller » shows purpose."),
               ]),
            H("Faux amis and calques"),
            CODE("""English            Mauvaise traduction     Bonne traduction
actually           actuellement            en fait / en réalité
to attend a class  attendre                assister à un cours
library            librairie (= bookshop)  bibliothèque
to pass an exam    passer (= to sit it)    réussir à un examen
to realise         réaliser                se rendre compte
sensible           sensible (= sensitive)  raisonnable / sensé
I am 15            Je suis 15              J'ai 15 ans
I am cold          Je suis froid           J'ai froid""", "text", title="Pièges fréquents"),
            MISTAKE("Mixing imparfait and passé composé", "A description or a habit is imparfait; a finished event is passé composé. "
                    "The Board's report notes that candidates also confused the plus-que-parfait with the imparfait and the passé composé, "
                    "and these errors were penalised."),
            MISTAKE("Word-for-word translation", "« Je suis 15 ans » is a calque. In French, age is expressed with avoir: « J'ai quinze ans »."),
            MISTAKE("Leaving the passage in English or recopying it", "Examiners can only give marks for French you have written. Translate every sentence."),
            QUIZ("Traduction de « She had already eaten » :",
                 ["Elle a déjà mangé.", "Elle mangeait déjà.", "Elle avait déjà mangé.", "Elle mange déjà."],
                 2, "« Had eaten » is an earlier past action: plus-que-parfait, « avait mangé ».",
                 hint="Is the eating before another past moment?",
                 feedback=["That is a passé composé: it translates « She has already eaten » or « She ate ».", "That would be « She was already eating ».", "", "That is the present."]),
            QUIZ("Traduction de « He is a student » :",
                 ["Il est un étudiant.", "Il est étudiant.", "Il a étudiant.", "Il est des étudiants."],
                 1, "After être, a profession or status is used without article: « Il est étudiant ».",
                 hint="Does French need « un » for a profession after être?",
                 feedback=["With « c'est », you can say « C'est un étudiant », but with « il est » drop the article.", "", "« Avoir » is wrong.", "The plural makes no sense."]),
            H("Practice"),
            PQ("Traduisez : It was hot and the children were playing in the yard. (Use the imparfait.)",
               "Il faisait chaud et les enfants jouaient dans la cour."),
            PQ("Traduisez : My father had bought some fish before we arrived.",
               "Mon père avait acheté du poisson avant que nous arrivions. (Also accepted: avant notre arrivée.) The pluperfect shows an action earlier than « arrivons »."),
            PQ("Traduisez : Actually, I did not go to the library.",
               "En fait, je ne suis pas allé(e) à la bibliothèque. (Do not use « actuellement » or « librairie ».)"),
            PQ("Traduisez : She is 16 years old and she is a nurse.",
               "Elle a seize ans et elle est infirmière."),
            SUM("Thème means English into French: translate meaning sentence by sentence, not word for word.",
                "Choose tenses carefully: imparfait for description and habit, passé composé for finished events, plus-que-parfait for earlier events.",
                "Add the articles French needs, and make adjectives and past participles agree with gender and number.",
                "Learn the faux amis: actually, to attend, library, to pass, to realise, age and cold.",
                "Always translate every sentence in French; never recopy the English."),
        ],
    ),
    # ------------------------------------------------------------------ 4. Version
    lesson(
        module=M_READ, topic="Translation into English (version)",
        title="Version: translating French into natural English",
        slug="fr3-version-into-english",
        minutes=22,
        summary="How to translate a French passage into natural English: understand each tense, translate meaning, not form, "
                "and avoid literal translations of faux amis and idioms.",
        objectives=[
            "Translate French past tenses into natural English past forms",
            "Recognise French structures that have no word-for-word English equivalent (il y a, avoir faim, depuis)",
            "Avoid translating faux amis literally",
            "Check a translation for natural, correct English",
        ],
        key_concepts=["Version", "Passé composé / simple past", "Imparfait / was doing", "Il y a", "Faux amis"],
        blocks=[
            H("Introduction"),
            T("**Version** is the translation from French into English. It looks easier, because English is your language, but there are traps: "
              "French tenses do not map directly onto English ones, and some French phrases sound odd if you translate them word for word. "
              "Translation questions test whether you understood the French and can write good English."),
            T("The Board's report describes the translation as a search for equivalent words and expressions, and for all the grammatical "
              "elements of the source language to be carried into the target language. In plain words: do not skip anything, and do not add anything."),
            KEY("Method", "Follow these steps.", cards=[
                ["1. Read it all", "Get the general meaning before translating anything."],
                ["2. Tenses", "Decide the English tense for each verb from its meaning, not its form."],
                ["3. Meaning", "Rephrase idioms and fixed expressions as an English speaker would say them."],
                ["4. Check", "Reread your English. Does it sound natural? Is anything missing?"],
            ]),
            H("French tenses into English"),
            CODE("""Français                 English
Elle est allée au marché  She went to the market      (passé composé -> simple past)
Elle allait au marché     She was going / used to go  (imparfait -> was doing / used to)
Elle avait acheté du riz  She had bought some rice    (plus-que-parfait -> past perfect)
Elle est partie hier      She left yesterday          (not "has left" with a past time)
Je suis ici depuis 2 ans  I have been here for 2 years (depuis + present)""", "text", title="Les temps"),
            T("The passé composé is often a simple past in English. But with « depuis » (since, for), French uses the present while English uses "
              "the present perfect: « J'habite à Maroua depuis dix ans » is « I have lived in Maroua for ten years »."),
            T("Read this short passage (written for KKEVO)."),
            CODE("""Hier, il faisait très chaud à Maroua. Ma mère est allée au
marché avant midi parce que nous n'avions plus de riz. Quand
elle est revenue, mon petit frère jouait dans la cour avec ses
amis. Elle avait acheté des mangues et du poisson, mais elle
avait oublié le sel. Alors elle m'a demandé d'aller en chercher
chez le voisin.""", "text", title="Texte à traduire"),
            EX("Exemple 1 : traduire le passage",
               intro="Translate the passage into English.",
               steps=[
                   S("Sentence 1", text="« Hier, il faisait très chaud à Maroua. » -> « Yesterday it was very hot in Maroua. » Weather with « il fait » is « it is »."),
                   S("Sentence 2", text="« Ma mère est allée au marché avant midi parce que nous n'avions plus de riz. » -> « My mother went to the market before noon because we had no more rice. »"),
                   S("Sentence 3", text="« Quand elle est revenue, mon petit frère jouait dans la cour avec ses amis. » -> « When she came back, my little brother was playing in the yard with his friends. »"),
                   S("Sentences 4 and 5", text="« She had bought mangoes and fish, but she had forgotten the salt. So she asked me to go and get some from the neighbour. »"),
               ]),
            EX("Exemple 2 : expressions particulières",
               intro="Translate: Il a faim. Elle a dix-sept ans. Il y a un problème. Cela fait deux heures que j'attends.",
               steps=[
                   S("Avoir faim", text="« He is hungry » (not « He has hunger »)."),
                   S("Avoir + age", text="« She is seventeen » or « She is seventeen years old »."),
                   S("Il y a", text="« There is a problem »."),
                   S("Cela fait... que", text="« I have been waiting for two hours »."),
               ]),
            MISTAKE("Translating faux amis literally", "« Il a assisté au match » is « He attended the match », not « He assisted the match ». "
                    "« Une librairie » is a bookshop, not a library. « Actuellement » means « currently », not « actually »."),
            MISTAKE("Using the wrong English tense for the passé composé", "« Elle est partie hier » is « She left yesterday ». "
                    "« She has left yesterday » is wrong in English because a finished past time is given."),
            MISTAKE("Leaving words out", "Missing out « un petit frère » or « avec ses amis » costs marks. Check that every part of the French sentence has an English equivalent."),
            TIP("If you do not know a word, use the context. If the word still blocks you, translate the rest properly and give your best guess; never leave a gap."),
            QUIZ("Translate: « Nous avons fini nos devoirs avant le dîner. »",
                 ["We finish our homework before dinner.", "We have finished our homework yesterday before dinner.",
                  "We finished our homework before dinner.", "We were finishing our homework before dinner."],
                 2, "The passé composé of a finished action in a story is the English simple past.",
                 hint="The action is complete and in the past.",
                 feedback=["That is the present.", "The present perfect does not go with a finished time such as « yesterday »; the French has no « yesterday » either.",
                           "", "The imparfait would suggest the action was in progress."]),
            QUIZ("Translate: « Je suis à Bamenda depuis trois mois. »",
                 ["I am in Bamenda since three months.", "I was in Bamenda for three months.", "I have been in Bamenda for three months.", "I will be in Bamenda for three months."],
                 2, "« Depuis » with the present shows an action that began in the past and continues now: present perfect in English.",
                 hint="The person is still in Bamenda.",
                 feedback=["English does not use « since » with a length of time, and the tense is not the present.", "A simple past would mean the stay is over.", "", "The future is not in the French."]),
            H("Practice"),
            PQ("Translate: « Quand j'étais petit, j'allais à l'école à pied. »",
               "When I was little, I used to walk to school (or: I went to school on foot)."),
            PQ("Translate: « Elle a pris son sac et elle est sortie. »",
               "She took her bag and went out."),
            PQ("Translate: « Il a l'habitude de se lever à six heures. »",
               "He is used to getting up at six o'clock. (He usually gets up at six.)"),
            PQ("Translate: « Nous avions déjà mangé quand les invités sont arrivés. »",
               "We had already eaten when the guests arrived."),
            SUM("Version means French into English: translate meaning and keep every part of the sentence.",
                "Passé composé is usually a simple past in English; imparfait is « was doing » or « used to »; plus-que-parfait is the past perfect.",
                "Some French structures need a different English form: avoir faim, avoir + age, il y a, depuis.",
                "Watch faux amis such as assister à, librairie and actuellement.",
                "Reread your English for naturalness and make sure nothing is missing."),
        ],
    ),
    # ------------------------------------------------------------------ 5. Informal letters
    lesson(
        module=M_WRITE, topic="Informal and formal letters",
        title="The informal letter: writing to a friend or relative",
        slug="fr3-informal-letters",
        minutes=24,
        summary="How to write an informal letter in French: layout, tu and familiar tone, the right tenses, at least three paragraphs, "
                "personal feelings, and the mistakes the Board's examiners penalise.",
        objectives=[
            "Set out an informal letter: place and date, salutation, three or more paragraphs, closing and signature",
            "Use tu, familiar expressions and the right tenses (présent, passé composé, futur simple)",
            "Express feelings and personal opinions",
            "Avoid the penalised errors: passé simple, identity disclosed, essay-style opening",
        ],
        key_concepts=["Lettre amicale", "Tutoiement", "Formule d'ouverture", "Formule de fin", "Passé composé"],
        blocks=[
            H("Introduction"),
            T("In Paper 2, Question 2, candidates write an essay of 140 to 150 words on one of three topics. In 2023 one of the three was an "
              "informal letter to a friend's father, another a narration, and the third an interpretation of pictures. Letters are therefore a "
              "serious possibility, and a lot of marks depend on how well you set one out and how well you write it."),
            T("A letter to someone you know well (a friend, a cousin, a grandparent) is an **informal letter**, or « lettre amicale »."),
            IMG("f5fre-3-letter-layout.svg", alt="Layout of an informal letter: place and date at the top right, salutation, three paragraphs (introduction, body, conclusion), closing phrase and signature",
                caption="Figure 1. Layout of an informal letter in French."),
            H("What the Board's report says"),
            KEY("Points from the 2023 report", "These apply to letters in Paper 2.", cards=[
                ["Tenses", "Past tenses were accepted for narrating what happened. Some candidates used the present throughout, or switched from passé composé to passé simple with no reason."],
                ["No passé simple", "The passé simple is not accepted in letter writing; use the passé composé."],
                ["Identity", "Use the name and address given in the question. Candidates who wrote their own names attracted a penalty."],
                ["Letter, not essay", "Begin as a letter; do not write an essay's opening, and do not begin a narrative essay as a letter."],
            ]),
            T("The marking criteria named in the report are the relevance of your answer to the topic, the coherence of your ideas, the correctness "
              "of your language, and your originality. For a letter, originality includes a clear structure (an introduction, a conclusion and at "
              "least three paragraphs), the expression of your feelings, and no memorised material."),
            H("The parts of an informal letter"),
            CODE("""Douala, le 14 juin 2025                      <- lieu et date

Cher Arnaud,                                 <- appel (formule d'ouverture)

[Paragraphe 1 : introduction]                <- nouvelles, raison de la lettre
[Paragraphe 2 : développement]               <- le sujet : ce qui s'est passé
[Paragraphe 3 : conclusion]                  <- projets, souhaits, invitation

Je t'embrasse très fort,                     <- formule de fin
Nadège                                       <- signature""", "text", title="Mise en page"),
            CODE("""Ouverture                         Fermeture
Cher Arnaud, / Chère Nadège,      Je t'embrasse. / Grosses bises.
Mon cher cousin,                  À bientôt. / À très vite.
Ma chère tante,                   Amicalement. / Affectueusement.

Pour commencer :                  Pour finir :
Comment vas-tu ?                  Écris-moi vite !
J'espère que tu vas bien.         Donne-moi de tes nouvelles.
Je t'écris pour te dire que...    Mes amitiés à ta famille.""", "text", title="Expressions utiles"),
            H("A model letter"),
            T("Here is a model letter, written for KKEVO. Names and places are invented. It tells a friend about a birthday, using the "
              "présent, the passé composé and the futur simple. It has about 115 words, so it is shorter than the examination target of 140 to 150: add details when you write your own. Study how each paragraph has one job. Do not memorise it: examiners "
              "warn against learned texts and expect your own words on the topic you are given."),
            CODE("""Douala, le 14 juin 2025

Cher Arnaud,

Comment vas-tu ? Moi, je vais très bien et toute la famille
te passe le bonjour. Je t'écris pour te raconter mon
anniversaire, car tu n'as pas pu venir.

Samedi dernier, j'ai fêté mes seize ans à la maison. Maman a
préparé du ndolé et du poulet DG, et mes amis sont arrivés vers
quinze heures avec des cadeaux. Nous avons dansé, chanté et
mangé jusqu'au soir. Mon oncle m'a offert un beau dictionnaire,
et j'étais très émue.

J'ai pensé à toi toute la journée et j'espère que tu seras là
l'année prochaine. Pendant les vacances, viens passer une
semaine chez nous : nous irons à la plage de Limbé.

Écris-moi vite !

Je t'embrasse très fort,
Nadège""", "text", title="Lettre modèle"),
            EX("Exemple : analyser la lettre modèle", intro="Identify the job of each paragraph and the tenses used.", steps=[
                S("Paragraph 1", text="Asks for news and gives the reason for writing. Present tense: « je vais », « je t'écris ». The passé composé « tu n'as pas pu venir » explains the missed event."),
                S("Paragraph 2", text="Tells what happened. Passé composé for events (« j'ai fêté », « a préparé », « sont arrivés », « avons dansé »), imparfait for a state (« j'étais très émue »)."),
                S("Paragraph 3", text="Looks to the future: futur simple (« seras », « irons ») and an invitation. Present imperative: « viens »."),
                S("Closing", text="« Écris-moi vite ! » and a warm closing phrase, then the signature."),
            ]),
            TIP("Write 140 to 150 words for a Paper 2 essay-type letter, as the Board's report states for the essay; check the instruction on your paper. "
                "Plan three paragraphs before you write so that the length is right."),
            MISTAKE("Using the passé simple", "Forms such as « il alla » or « nous fûmes » are formal, literary forms. In a letter, write « il est allé » and « nous avons été »."),
            MISTAKE("Writing your own name and address", "If the question gives a name and address, use those. Never write your real name or school; this is penalised."),
            MISTAKE("Switching tense without a reason", "Choose passé composé and imparfait for the past, présent for the present, futur simple for what is coming. Do not drift between them."),
            QUIZ("Quelle formule de fin convient à une lettre amicale ?",
                 ["Veuillez agréer, Monsieur, l'expression de mes salutations distinguées.", "Je t'embrasse très fort.",
                  "Cordialement vôtre, le directeur.", "Veuillez recevoir mes sentiments respectueux."],
                 1, "« Je t'embrasse » is warm and uses tu, as for a friend or cousin.",
                 hint="Which closing uses tu?",
                 feedback=["That is a formal closing for a letter to an official.", "", "A friendly letter has no « le directeur ».", "That is formal and uses vous."]),
            QUIZ("Dans une lettre amicale, laquelle de ces phrases est la meilleure pour raconter la fête d'hier ?",
                 ["Hier, nous dansâmes jusqu'au soir.", "Hier, nous avons dansé jusqu'au soir.", "Hier, nous dansons jusqu'au soir.", "Hier, nous danserons jusqu'au soir."],
                 1, "The passé composé is the usual past tense for letters.",
                 hint="The passé simple is not accepted in letters.",
                 feedback=["The passé simple is not accepted in letter writing.", "", "The present does not fit « hier ».", "The future does not fit « hier »."]),
            H("Practice"),
            PQ("Écrivez la formule d'ouverture et la première phrase d'une lettre à votre cousin Paul pour lui annoncer que vous avez réussi un examen.",
               "Par exemple : « Cher Paul, Comment vas-tu ? Je t'écris pour te dire une bonne nouvelle : j'ai réussi mon examen ! »"),
            PQ("Mettez au passé composé : « Nous allons à Kribi et nous nous baignons. »",
               "« Nous sommes allés à Kribi et nous nous sommes baignés. » Both verbs take être; the participles agree with « nous » (masculine plural here)."),
            PQ("Écrivez une phrase de conclusion pour inviter un ami à votre village pour les vacances.",
               "Par exemple : « Viens passer les vacances chez nous, nous irons au marché et à la rivière ! »"),
            PQ("Pourquoi faut-il éviter le passé simple dans une lettre ?",
               "Because it is a literary tense that is not accepted in letter writing; the passé composé is used instead."),
            SUM("An informal letter has place and date, a salutation, an introduction, a development, a conclusion, a closing phrase and a signature.",
                "Use tu, warm expressions and your feelings; do not memorise a model letter.",
                "Use the passé composé and imparfait to tell what happened, the présent for now, the futur simple for plans.",
                "The passé simple is not accepted in letters, and you must use the identity given in the question.",
                "Aim for the word limit set in the question, with at least three paragraphs."),
        ],
    ),
    # ------------------------------------------------------------------ 6. Formal letters
    lesson(
        module=M_WRITE, topic="Informal and formal letters",
        title="The formal letter: writing to a principal or an official",
        slug="fr3-formal-letters",
        minutes=24,
        summary="How to write a formal letter in French: layout, vous and polite formulas, a clear purpose in each paragraph, "
                "and the fixed opening and closing phrases.",
        objectives=[
            "Lay out a formal letter with sender, recipient, place, date and subject line (objet)",
            "Use vous, polite formulas and the conditional of politeness",
            "Give each paragraph a clear purpose: present yourself, explain, request",
            "Choose the correct closing formula",
        ],
        key_concepts=["Lettre officielle", "Objet", "Vouvoiement", "Formule de politesse", "Conditionnel de politesse"],
        blocks=[
            H("Introduction"),
            T("When a student writes to a school principal, a mayor or an employer, the tone changes: the letter is shorter, more precise and "
              "very polite. French has a precise layout and fixed phrases for this. They are simple to learn and they look professional."),
            D("A **formal letter** (lettre officielle or lettre administrative) is written to a person you do not know well or who has authority. "
              "It uses **vous**, polite expressions and a fixed closing formula.", title="Lettre officielle"),
            H("Layout"),
            CODE("""Nadège Mbarga                              <- expéditeur (en haut à gauche)
Lycée Bilingue de Bonabéri
Douala

                              Monsieur le Directeur   <- destinataire (à droite)
                              du Lycée Bilingue
                              Douala

                              Douala, le 3 mars 2025  <- lieu et date

Objet : demande d'autorisation d'absence              <- objet

Monsieur le Directeur,                                <- appel

[Paragraphe 1 : qui vous êtes et ce que vous demandez]
[Paragraphe 2 : les raisons et les détails]
[Paragraphe 3 : remerciements et formule de politesse]

Veuillez agréer, Monsieur le Directeur, l'expression de mes
salutations distinguées.                              <- formule de fin

Nadège Mbarga                                         <- signature""", "text", title="Mise en page d'une lettre formelle"),
            T("Layouts differ a little between textbooks (some put the sender on the right, or the date on the left). Check your teacher's "
              "preferred layout. What never changes is a clear purpose, polite words and a correct closing formula."),
            KEY("Polite phrases", "Learn these useful forms.", cards=[
                ["Ouvrir", "Je me permets de vous écrire pour... / J'ai l'honneur de solliciter..."],
                ["Demander", "Je voudrais vous demander... / Auriez-vous la possibilité de... ?"],
                ["Expliquer", "En effet, ... / C'est pourquoi... / Je suis dans l'obligation de..."],
                ["Remercier et fermer", "Je vous remercie d'avance. / Veuillez agréer, Monsieur, l'expression de mes salutations distinguées."],
            ]),
            T("The **conditional of politeness** is a softer way to ask: « Je voudrais » (I would like) is more polite than « Je veux »; "
              "« Pourriez-vous » (could you) is more polite than « Pouvez-vous »."),
            H("A model formal letter"),
            CODE("""Nadège Mbarga
Élève de première
Lycée Bilingue de Bonabéri

                              Monsieur le Directeur
                              du Lycée Bilingue de Bonabéri

                              Douala, le 3 mars 2025

Objet : demande d'autorisation d'absence

Monsieur le Directeur,

Je me permets de vous écrire pour vous demander l'autorisation
de m'absenter du lycée du lundi 10 au mercredi 12 mars.

En effet, ma grand-mère est tombée malade au village et ma
famille doit voyager pour lui rendre visite. Mes parents pensent
que ma présence est nécessaire. Je m'engage à rattraper les cours
manqués et à rendre tous mes devoirs dès mon retour.

Je vous remercie d'avance de l'attention que vous porterez à
ma demande.

Veuillez agréer, Monsieur le Directeur, l'expression de mes
salutations distinguées.

Nadège Mbarga""", "text", title="Lettre officielle modèle"),
            EX("Exemple : analyser la lettre", intro="What does each paragraph do, and which polite forms are used?", steps=[
                S("Paragraph 1", text="States who is writing and what is asked: « Je me permets de vous écrire pour vous demander l'autorisation de... ». The request is clear."),
                S("Paragraph 2", text="Gives the reason (« En effet... ») and a promise (« Je m'engage à... »). Facts, not emotions."),
                S("Paragraph 3", text="Thanks in advance with « Je vous remercie d'avance... ». The closing formula repeats the title used in the salutation."),
                S("Language", text="Vous, no slang, no contractions typical of speech, no exclamation marks."),
            ]),
            MISTAKE("Using tu or slang", "A formal letter never says « tu », « salut » or « je t'embrasse ». Use « Monsieur », « Madame » and « vous »."),
            MISTAKE("Wrong closing formula", "In French, the closing formula repeats the title of the salutation: « Veuillez agréer, Monsieur le Directeur, l'expression de mes salutations distinguées. » "
                    "Do not end a formal letter with « À bientôt »."),
            MISTAKE("Forgetting the objet", "In an administrative letter, the objet line tells the reader the purpose before they begin. Keep it short and without a verb."),
            MISTAKE("A request that is not clear", "Say exactly what you ask (the dates, the permission, the information) in the first paragraph."),
            QUIZ("Quelle phrase est la plus polie pour demander un renseignement ?",
                 ["Dis-moi les horaires.", "Donnez-moi les horaires.", "Pourriez-vous m'indiquer les horaires ?", "Je veux connaître les horaires."],
                 2, "The conditional with « vous » is the polite way to ask.",
                 hint="Choose the form with vous and the conditional.",
                 feedback=["It uses tu and the imperative.", "The imperative sounds like an order.", "", "« Je veux » is too direct."]),
            QUIZ("Quelle formule de fin convient pour une lettre à un directeur ?",
                 ["Bisous et à bientôt.", "Veuillez agréer, Monsieur le Directeur, l'expression de mes salutations distinguées.", "Salut et merci.", "Je t'embrasse bien fort."],
                 1, "This is the standard formal closing, repeating the title used in the salutation.",
                 hint="Which closing uses « Veuillez agréer » ?",
                 feedback=["Too familiar.", "", "Too familiar.", "Too familiar and uses tu."]),
            H("Practice"),
            PQ("Écrivez l'objet et la phrase d'ouverture d'une lettre à un directeur pour demander un certificat de scolarité.",
               "Objet : demande de certificat de scolarité. Monsieur le Directeur, Je me permets de vous écrire pour vous demander un certificat de scolarité."),
            PQ("Mettez cette phrase sous une forme plus polie : « Donnez-moi une réponse avant lundi. »",
               "« Pourriez-vous me donner une réponse avant lundi, s'il vous plaît ? »"),
            PQ("Corrigez la fin de cette lettre : « Merci, salut, Nadège. »",
               "« Je vous remercie d'avance. Veuillez agréer, Monsieur le Directeur, l'expression de mes salutations distinguées. Nadège Mbarga »"),
            PQ("Donnez deux différences entre une lettre amicale et une lettre officielle.",
               "A friendly letter uses tu and warm closings (Je t'embrasse); a formal letter uses vous, an objet line and a formal closing formula. A friendly letter may express feelings freely; a formal letter is brief and precise."),
            SUM("A formal letter has sender, recipient, place and date, objet, salutation, clear paragraphs, a closing formula and a signature.",
                "Use vous, polite phrases and the conditional of politeness.",
                "State your request clearly in the first paragraph, give reasons in the second, and thank the reader in the third.",
                "The closing formula repeats the title used in the salutation.",
                "Never use tu or familiar expressions in a formal letter."),
        ],
    ),
    # ------------------------------------------------------------------ 7. Narrative and descriptive
    lesson(
        module=M_WRITE, topic="Narrative and descriptive essays",
        title="Narrative and descriptive essays: telling and describing in French",
        slug="fr3-narrative-descriptive",
        minutes=26,
        summary="How to plan and write a 140 to 150 word narrative or descriptive essay in French: answer every instruction, use "
                "passé composé and imparfait, link ideas with connectors, and give your own reaction at the end.",
        objectives=[
            "Plan a narrative essay that answers every instruction in the question",
            "Use passé composé for events, imparfait for background and description, and connectors to link them",
            "Write a short descriptive paragraph using the senses and well-chosen adjectives",
            "Check an essay against the four criteria: relevance, coherence, language and originality",
        ],
        key_concepts=["Récit", "Description", "Connecteurs", "Passé composé / imparfait", "Pertinence", "Cohérence"],
        blocks=[
            H("Introduction"),
            T("When a Cameroonian grandmother tells a story, she does three things: she sets the scene, she tells what happened, and she "
              "finishes with a lesson. A French narrative essay needs the same three movements."),
            T("The Board's 2023 report says that in Paper 2, Question 2 candidates write 140 to 150 words on one of three topics. One topic was "
              "a narrative or descriptive essay about false news spreading on social media at school, with three precise instructions: "
              "answer the questions where? when? what? who?; develop the story; and end with your own reaction and how it finished. "
              "Many candidates lost marks because they did not read the instructions carefully."),
            KEY("The four criteria in the report", "These are the qualities that examiners look for.", cards=[
                ["Pertinence", "Do you answer exactly what the topic asks? Do you treat all the instructions?"],
                ["Cohérence", "Does the story flow? Paragraphs, linking words, a beginning and an ending."],
                ["Correction de la langue", "Accuracy: grammar, verbs, vocabulary, spelling."],
                ["Originalité", "Your own style and ideas; no memorised essay."],
            ]),
            H("Planning with the instructions"),
            T("Before writing, turn each instruction into a paragraph. Write a plan of key words. A 140 to 150 word essay usually has three or "
              "four short paragraphs."),
            IMG("f5fre-3-essay-plan.svg", alt="Essay plan with three boxes: introduction (who, where, when, what), development (events in order, reactions), conclusion (outcome and own reaction)",
                caption="Figure 1. A three-part plan for a narrative essay."),
            CODE("""Sujet : Racontez une panne d'électricité pendant un examen blanc.
        1. Qui ? Où ? Quand ? (présentez la situation)
        2. Racontez ce qui s'est passé et la réaction des élèves.
        3. Terminez par votre réaction.

Plan :
Introduction : élèves de Terminale, salle 4, vendredi matin, examen de français
Développement : coupure de courant -> noir -> panique -> surveillant calme -> bougie, fenêtres
Conclusion : examen terminé ; ma réaction : fier de rester calme""", "text", title="Plan"),
            H("Tenses and connectors"),
            T("Use the **passé composé** for the main events (what happened one after the other) and the **imparfait** for the background (what "
              "was going on, the weather, how people felt). The Board accepted past tenses as the main narrative tenses; the problem was candidates "
              "who drifted into the present, or who changed from the passé composé to the passé simple without a reason. Choose one main past tense "
              "and keep to it."),
            CODE("""Début           d'abord, au début, ce jour-là, un matin
Suite           ensuite, puis, après cela, quelques minutes plus tard
Surprise        soudain, tout à coup, brusquement
Cause/résultat  parce que, car, alors, c'est pourquoi
Opposition      mais, pourtant, cependant
Fin             enfin, finalement, à la fin, en conclusion""", "text", title="Connecteurs utiles"),
            H("A model narrative"),
            CODE("""Un vendredi matin, nous passions un examen blanc de français
dans la salle quatre quand l'électricité s'est coupée. La
salle est devenue sombre, car les fenêtres étaient petites,
et plusieurs élèves ont crié. Moi, j'avais très peur de ne pas
finir mon devoir.

Soudain, le surveillant s'est levé. Il nous a dit de rester
calmes et il a ouvert toutes les fenêtres. Un élève a apporté
une bougie, puis deux autres. Peu à peu, la peur a disparu et
nous avons continué à écrire. Pendant que nous travaillions, le
directeur est venu voir si tout allait bien.

Finalement, le courant est revenu à la fin de l'épreuve. J'ai
rendu ma copie à temps. Ce jour-là, j'ai compris que le calme est
plus utile que la panique, et j'étais fier de moi.""", "text", title="Récit modèle"),
            T("This model has about 130 words, a little below the 140 to 150 target, so in the examination add one more detail. It answers who, where and when in the first paragraph, develops the events in the second, "
              "and ends with the writer's reaction in the last, just as the instructions asked. Notice the mix: « s'est coupée », « a ouvert » (events, "
              "passé composé) and « étaient », « avais peur », « travaillions » (background, imparfait)."),
            H("Description"),
            T("A **descriptive essay** or paragraph paints a picture of a person, a place or a scene. It uses the présent or the imparfait, "
              "adjectives, comparisons and the five senses (sight, sound, smell, taste, touch)."),
            CODE("""Le marché de mon quartier est toujours très animé. Dès le
matin, les vendeuses installent leurs étals colorés : tomates
rouges, piments verts, bananes jaunes. L'air sent le poisson
fumé et le plantain grillé. On entend des voix fortes qui
annoncent les prix, et la musique d'un haut-parleur couvre
parfois le bruit des moto-taxis. Le soir, la poussière
rouge se pose lentement sur les paniers vides.""", "text", title="Description modèle"),
            EX("Exemple : de la consigne au plan", intro="Sujet : Racontez comment vous avez aidé un voisin le jour de la pluie. Trois consignes : (1) présentez la situation; (2) racontez l'aide apportée; (3) donnez votre réaction.", steps=[
                S("Instruction 1", text="Paragraph 1: who is the neighbour, where, when, what was the rain doing (imparfait)?"),
                S("Instruction 2", text="Paragraph 2: what you did, step by step (passé composé), with connectors: d'abord, ensuite, enfin."),
                S("Instruction 3", text="Paragraph 3: how you felt and what you learned (« J'étais heureux de... » / « J'ai compris que... »)."),
                S("Check", text="Count words (140 to 150). Does each paragraph answer an instruction?"),
            ]),
            MISTAKE("Beginning a narrative as a letter", "The Board noted that some candidates opened a narrative essay with « Cher ami ». If the topic asks for a story, write a story."),
            MISTAKE("Recopying the topic", "Time spent copying the question is lost. Start writing your essay directly."),
            MISTAKE("Drifting between tenses", "Do not move from the passé composé to the présent without reason. Reread to check that the verbs of the story keep the same time frame."),
            MISTAKE("Memorising a model essay", "Examiners notice learned essays that do not fit the topic. Learn tools (connectors, verb forms), not whole texts."),
            QUIZ("Dans « Il pleuvait quand nous sommes partis », quel temps sert à décrire le fond de l'action ?",
                 ["Le présent", "Le passé composé", "L'imparfait", "Le futur simple"],
                 2, "« Il pleuvait » is the background (weather) in the imparfait; « sommes partis » is the event in the passé composé.",
                 hint="Which tense describes what was going on?",
                 feedback=["The present is not the past.", "The passé composé gives the event, not the background.", "", "The future does not fit a past story."]),
            QUIZ("Quel connecteur introduit un événement inattendu ?",
                 ["Finalement", "Soudain", "Parce que", "D'abord"],
                 1, "« Soudain » (suddenly) introduces a surprise.",
                 hint="Think of lights going out.",
                 feedback=["That marks the end.", "", "That gives a cause.", "That marks the start."]),
            H("Practice"),
            PQ("Complétez avec l'imparfait ou le passé composé : « Quand je (arriver) à la gare, le car (partir) déjà. »",
               "Quand je suis arrivé(e) à la gare, le car était déjà parti. (Event, then an earlier event in the plus-que-parfait.)"),
            PQ("Écrivez trois phrases pour décrire un marché à l'aube, avec au moins un sens autre que la vue.",
               "Par exemple : « Le marché s'éveille. Une odeur de poisson fumé flotte dans l'air. Les voix des vendeuses résonnent déjà. »"),
            PQ("Faites un plan en trois parties pour une rédaction sur « une journée de fête dans mon village ».",
               "Introduction: où, quand, quelle fête. Développement: les préparatifs, la cérémonie, les danses. Conclusion: ce que j'ai ressenti."),
            PQ("Réécrivez avec des connecteurs : « Je me suis levé. J'ai mangé. Je suis parti. »",
               "D'abord, je me suis levé; ensuite, j'ai mangé; enfin, je suis parti."),
            SUM("Read every instruction in the topic and turn each into a paragraph of your plan.",
                "Passé composé for events, imparfait for background; keep one main past tense throughout.",
                "Link ideas with connectors (d'abord, puis, soudain, enfin) and end with your own reaction.",
                "A descriptive paragraph uses adjectives, comparisons and the senses.",
                "Judged on relevance, coherence, accuracy of language and originality; do not memorise a model essay."),
        ],
    ),
    # ------------------------------------------------------------------ 8. Argumentative
    lesson(
        module=M_ESSAY, topic="Argumentative and dialogue compositions",
        title="Argumentative essays: giving your opinion with reasons",
        slug="fr3-argumentative-essays",
        minutes=24,
        summary="How to plan and write an argumentative composition in French: a clear thesis, two or three reasons with examples, "
                "the other side acknowledged, and a conclusion.",
        objectives=[
            "Plan an argumentative essay with a thesis, arguments, a counter-argument and a conclusion",
            "Use connectors to add, contrast and conclude",
            "Give an opinion politely in French",
            "Use examples from Cameroonian life to support arguments",
        ],
        key_concepts=["Thèse", "Argument", "Exemple", "Connecteurs logiques", "Conclusion"],
        blocks=[
            H("Introduction"),
            T("At family meetings, at school debates and on the radio, people argue about the same questions: should students use phones at school? "
              "Should girls and boys have the same chances? An argumentative essay puts your side clearly and supports it with reasons."),
            T("The syllabus outline lists argumentative compositions and dialogues together. The Board's 2023 essay topics were a narration, a "
              "letter and a picture interpretation, so an argumentative topic is not guaranteed in a given year; still, the skill of giving reasons "
              "helps every kind of writing, and your teacher may set argumentative work."),
            D("An **argumentative essay** defends an opinion (la thèse) with arguments (reasons) and examples, and answers the strongest "
              "objection. It is written mostly in the présent.", title="Rédaction argumentative"),
            H("The plan"),
            CODE("""Introduction   : présenter le sujet + donner votre opinion (thèse)
Argument 1     : idée + explication + exemple
Argument 2     : idée + explication + exemple
Objection      : « Certains pensent que... mais... »
Conclusion     : rappel de la thèse + ouverture (conseil, souhait)""", "text", title="Plan argumentatif"),
            CODE("""Ajouter         d'abord, de plus, en outre, ensuite
Opposer         mais, cependant, pourtant, en revanche
Expliquer       en effet, c'est-à-dire, par exemple
Conclure        donc, c'est pourquoi, en conclusion, pour finir
Opinion         à mon avis, je pense que, selon moi, il me semble que""", "text", title="Connecteurs de l'argumentation"),
            H("A model essay"),
            T("Sujet : « Les téléphones portables doivent-ils être autorisés à l'école ? » (Model written for KKEVO; the arguments are not the only possible ones.)"),
            CODE("""De nos jours, presque tous les élèves possèdent un téléphone
portable. Faut-il l'autoriser à l'école ? À mon avis, il doit
être interdit en classe, mais permis pendant la récréation.

D'abord, le téléphone distrait les élèves. En effet, un
message ou un jeu peut détourner l'attention pendant le cours.
Par exemple, un élève qui regarde son écran ne comprend plus
l'explication du professeur.

De plus, il peut favoriser la triche pendant les examens.
Un élève peut envoyer ou recevoir des réponses en secret.

Certains pensent pourtant que le téléphone aide à chercher des
informations. C'est vrai, mais l'école peut organiser des
moments précis pour cela, sous le contrôle d'un enseignant.

En conclusion, le téléphone est utile, mais il faut le
réserver aux moments où il ne gêne pas l'apprentissage.""", "text", title="Essai modèle"),
            EX("Exemple : construire un argument", intro="Thèse : Les élèves doivent faire du sport chaque semaine.", steps=[
                S("Idea", text="Le sport est bon pour la santé."),
                S("Explanation", text="En effet, il renforce le corps et aide à mieux dormir."),
                S("Example", text="Par exemple, une heure de football le mercredi donne de l'énergie pour étudier."),
                S("Objection", text="Certains disent qu'il n'y a pas de temps, mais une séance courte suffit."),
            ]),
            TIP("A balanced objection makes your essay look intelligent. Show that you know the other side, then explain why your side is stronger. "
                "Avoid insulting words, and keep examples respectful: no party politics and no remarks about ethnic or religious groups."),
            MISTAKE("Listing opinions with no reasons", "« Je pense que c'est mauvais » is not an argument. Add « parce que... » and an example."),
            MISTAKE("Mixing tenses", "An argumentative essay is in the présent; use the passé composé only for a short example that really happened."),
            MISTAKE("Only one side", "If you ignore the other view, your essay looks one-sided. Mention the objection and reply."),
            QUIZ("Quel connecteur introduit une opposition ?",
                 ["De plus", "Par exemple", "Cependant", "C'est pourquoi"],
                 2, "« Cependant » means however; it contrasts two ideas.",
                 hint="Which connector means « however » ?",
                 feedback=["It adds an idea.", "It introduces an example.", "", "It introduces a consequence."]),
            QUIZ("Quelle phrase est un vrai argument ?",
                 ["Je n'aime pas les devoirs.", "Les devoirs sont mauvais.", "Les devoirs aident à retenir la leçon, car on la répète à la maison.", "Tout le monde déteste les devoirs."],
                 2, "An argument gives a reason and an explanation, not just a feeling.",
                 hint="Look for « car » and a reason.",
                 feedback=["It is a personal taste, not an argument.", "It is an opinion without a reason.", "", "It is a generalisation with no reason."]),
            H("Practice"),
            PQ("Écrivez une phrase de thèse pour le sujet : « Faut-il porter l'uniforme à l'école ? »",
               "Par exemple : « À mon avis, l'uniforme est utile, car il évite les différences entre les élèves. »"),
            PQ("Complétez : « Certains pensent que..., ______ je crois que... » avec un connecteur d'opposition.",
               "mais / pourtant / cependant"),
            PQ("Donnez un exemple pour appuyer l'argument « Lire développe l'imagination ».",
               "Par exemple : « Un élève qui lit des contes invente plus facilement des histoires dans ses rédactions. »"),
            PQ("Rédigez une conclusion de deux phrases pour une rédaction sur les réseaux sociaux.",
               "En conclusion, les réseaux sociaux sont utiles s'ils sont bien utilisés. Il faut donc apprendre aux jeunes à les utiliser avec prudence."),
            SUM("An argumentative essay has a thesis, two or three arguments with examples, an objection and a conclusion.",
                "Use connectors to add, contrast, explain and conclude.",
                "Give reasons with « parce que », « car », « en effet » and examples; opinions alone are not arguments.",
                "Write mainly in the présent and stay respectful to opposing views.",
                "Plan before you write and reread to check tenses and agreements."),
        ],
    ),
    # ------------------------------------------------------------------ 9. Dialogues
    lesson(
        module=M_ESSAY, topic="Argumentative and dialogue compositions",
        title="Dialogue compositions: writing a conversation in French",
        slug="fr3-dialogues",
        minutes=20,
        summary="How to write a short dialogue in French: speaker lines with dashes, tu or vous according to the relationship, natural "
                "questions and answers, and a clear start and finish.",
        objectives=[
            "Set out a dialogue with a dash for each speaker",
            "Choose tu or vous according to the relationship between the speakers",
            "Use natural questions, answers and polite expressions",
            "Plan a dialogue with a beginning, a development and an end",
        ],
        key_concepts=["Dialogue", "Tutoiement / vouvoiement", "Tiret", "Questions et réponses"],
        blocks=[
            H("Introduction"),
            T("A dialogue is a conversation between two or more people. At the pharmacy, at the market, at the school gate, you speak with other people "
              "every day. A written dialogue puts that conversation on paper in a clear form. It tests your ability to use questions, answers, "
              "politeness and the right register (tu or vous)."),
            D("A **dialogue** is a written conversation. Each speaker's words start on a new line, often with a dash. Keep the situation, the "
              "relationship and the register (tu or vous) consistent.", title="Dialogue"),
            KEY("Choosing tu or vous", "The relationship decides.", cards=[
                ["Tu", "Friends, family, children, classmates."],
                ["Vous", "Teachers, principals, shopkeepers, adults you do not know, officials."],
                ["Cohérence", "Do not switch between tu and vous in the same dialogue unless the story says the relationship changes."],
            ]),
            CODE("""Saluer         Bonjour / Bonsoir / Salut (amis) / Comment allez-vous ?
Demander       Pouvez-vous...? / Où est...? / Combien coûte...?
Répondre       Oui, bien sûr. / Non, désolé(e). / Cela dépend.
Remercier      Merci beaucoup. / De rien. / Je vous en prie.
Conclure       À bientôt. / Bonne journée. / À demain.""", "text", title="Expressions utiles"),
            H("A model dialogue"),
            T("Situation : une élève, Clarisse, parle à un pharmacien parce qu'elle a mal à la tête. (Model written for KKEVO.)"),
            CODE("""— Bonjour, Monsieur.
— Bonjour, Mademoiselle. Que puis-je faire pour vous ?
— J'ai mal à la tête depuis ce matin et j'ai aussi un peu de fièvre.
— Avez-vous pris un médicament ?
— Non, pas encore. Que me conseillez-vous ?
— Je vous donne ces comprimés. Prenez-en un deux fois par jour
  après les repas.
— D'accord. Combien coûtent-ils ?
— Ils coûtent huit cents francs.
— Voici l'argent. Merci beaucoup, Monsieur.
— Je vous en prie. Si la fièvre continue demain, allez voir un médecin.
— Oui, j'irai. Au revoir !
— Au revoir, Mademoiselle, et bon rétablissement !""", "text", title="Dialogue modèle"),
            EX("Exemple : analyser le dialogue", intro="What makes this dialogue work?", steps=[
                S("Register", text="Vous throughout, because a pupil speaks to an adult stranger in a shop."),
                S("Structure", text="Greeting, problem, advice, price, thanks, goodbye. A clear start and end."),
                S("Questions and answers", text="Each line answers the previous one: « Avez-vous pris un médicament ? » is followed by « Non, pas encore. »"),
                S("Tenses", text="Présent for the conversation, passé composé for what already happened (« j'ai pris »), futur simple for « j'irai »."),
            ]),
            H("Dialogue inside a story"),
            T("In a narrative, a short piece of dialogue can be set out with guillemets or dashes. Verbs of speech make it clear who is talking: "
              "« dit-il », « répond-elle », « demande Marie », « s'écrie le directeur ». With a question, the verb of speech follows the question mark and begins in small letters."),
            CODE("""— Où vas-tu ? demande Maman.
— Au marché, répond Pascal.
— Reviens avant la nuit, ajoute-t-elle.""", "text", title="Avec verbes de parole"),
            MISTAKE("Mixing tu and vous", "In « Pouvez-vous m'aider ? Merci, tu es gentil », the speaker changes register in one breath. Choose one form."),
            MISTAKE("Writing a story instead of a dialogue", "If the task says dialogue, most of the text must be the characters' words, not a narration."),
            MISTAKE("Answers that do not fit the questions", "Reread each pair: does the second line answer the first?"),
            QUIZ("Quelle phrase convient à un élève qui s'adresse à son directeur ?",
                 ["Tu peux m'aider, s'il te plaît ?", "Pouvez-vous m'aider, s'il vous plaît ?", "Aide-moi !", "Salut, tu m'aides ?"],
                 1, "A pupil uses vous to speak to a principal.",
                 hint="Choose the form with vous.",
                 feedback=["It uses tu.", "", "It is an order with tu.", "Too familiar."]),
            QUIZ("Comment est correctement écrite cette réplique ?",
                 ["— Où vas-tu ? Demande Maman.", "— Où vas-tu ? demande Maman.", "— Où vas-tu, demande Maman ?", "— Où vas tu ? demande Maman."],
                 1, "After the question mark, the verb of speech begins in small letters, and « vas-tu » takes a hyphen.",
                 hint="Check capital letters and hyphens.",
                 feedback=["« demande » should not start with a capital letter after the question mark here.", "", "The question mark belongs after « vas-tu ».", "The hyphen in « vas-tu » is missing."]),
            H("Practice"),
            PQ("Écrivez les trois premières répliques d'un dialogue entre deux amis qui organisent une sortie à la plage.",
               "— Salut Éric ! Tu es libre samedi ? — Oui, pourquoi ? — On pourrait aller à la plage de Limbé. Qu'en penses-tu ?"),
            PQ("Transformez en vouvoiement : « Peux-tu me dire où est la gare ? »",
               "« Pouvez-vous me dire où est la gare ? »"),
            PQ("Écrivez une réponse polie à : « Merci beaucoup pour votre aide. »",
               "« Je vous en prie. » ou « De rien. »"),
            PQ("Imaginez la fin d'un dialogue entre une cliente et un vendeur au marché.",
               "— Voilà trois mille francs. — Merci, Madame, à bientôt. — Au revoir, bonne journée !"),
            SUM("A dialogue is a written conversation; start each speaker's words on a new line with a dash.",
                "Choose tu or vous from the relationship and keep to it.",
                "Questions and answers must match; use polite expressions and a clear greeting and farewell.",
                "Use the présent, passé composé and futur simple naturally.",
                "Verbs of speech (dit-il, répond-elle) help in a dialogue inside a story."),
        ],
    ),
    # ------------------------------------------------------------------ 10. Exam Paper 1
    lesson(
        module=M_EXAM, topic="Paper 1",
        title="Paper 1 strategy: 50 multiple-choice questions in French",
        slug="frx-paper-1-strategy",
        minutes=22,
        summary="How to approach the 50 multiple-choice questions of French Paper 1: what the paper covers, how to read items, "
                "how to eliminate wrong options, and how to manage your time.",
        objectives=[
            "State what the Board's 2023 report says about Paper 1",
            "Recognise the main question types (grammar, verbs, transformations, vocabulary, reading, writing skills)",
            "Use elimination and quick checks (agreement, tense, register) to choose answers",
            "Plan your time and review your answers",
        ],
        key_concepts=["Paper 1", "QCM", "Elimination", "Concordance", "Gestion du temps"],
        blocks=[
            H("Introduction"),
            T("Paper 1 is made of multiple-choice questions, or QCM (questions à choix multiples). The Board's 2023 report says that French "
              "Paper 1 had 50 multiple-choice questions, counted for 40% of the examination, covered the whole Ordinary Level syllabus, and "
              "was marked electronically. That means you shade or choose one option for each question, and nobody reads your reasoning: "
              "only your final choice counts."),
            KEY("What the paper covers", "The six modules of this course are a good map of what you can meet.", cards=[
                ["Grammaire", "Articles, nouns, adjectives, comparatives, pronouns."],
                ["Verbes", "Present, imperative, imparfait, passé composé, plus-que-parfait, passé simple, futur, conditionnel, subjonctif, participle agreement."],
                ["Transformations", "Negative, interrogative, passive, reported speech, connectors."],
                ["Lexique", "Family, school, health, travel, environment, media and ICT."],
                ["Lecture et traduction", "A short passage with questions; choosing a correct translation."],
                ["Expression", "Letters, narratives and dialogues: choosing correct forms, tenses and formulas."],
            ]),
            T("The exact balance between these areas can change from year to year. Practise all six, not only the ones you like."),
            H("A four-step routine for each question"),
            KEY("Routine", "Use it for every item.", cards=[
                ["1. Lire", "Read the stem (the question or sentence) fully, and the instruction."],
                ["2. Prédire", "Before looking at the options, think what the correct answer should be."],
                ["3. Éliminer", "Cross out options with a wrong agreement, tense, preposition or meaning."],
                ["4. Vérifier", "Put your choice back into the sentence and read it aloud in your head."],
            ]),
            H("Quick checks for grammar items"),
            CODE("""Accord            sujet-verbe ? nom-adjectif ? participe passé ?
Temps             le marqueur de temps (hier, déjà, demain, si...) ?
Préposition       à, de, en, dans, chez, par, pour ?
Pronom            COD (le, la, les) ou COI (lui, leur) ? en, y ?
Registre          tu ou vous, langue familière ou soignée ?""", "text", title="Vérifications rapides"),
            EX("Exemple 1 : prédire puis éliminer", intro="Choose the correct word: « Hier, mes cousines ______ au marché. » A. vont  B. sont allées  C. sont allés  D. iront", steps=[
                S("Predict", text="« Hier » means the past. The verb is « aller » (être), the subject is feminine plural."),
                S("Eliminate", text="A is present and D is future. C is masculine plural."),
                S("Answer", text="B. « Hier, mes cousines sont allées au marché. »"),
            ]),
            EX("Exemple 2 : choisir le bon temps", intro="Choose: « Quand il est arrivé, nous ______ déjà mangé. » A. avons  B. avions  C. aurons  D. eûmes", steps=[
                S("Clue", text="« déjà » and « est arrivé » show that the eating came before the arrival."),
                S("Form", text="Plus-que-parfait = imparfait of avoir + participle: « nous avions mangé »."),
                S("Answer", text="B. « avions »."),
            ]),
            T("Reading items give you a passage and ask about it. For these, apply the lesson on reading: skim, read the question, scan, check. "
              "In the mock exams of this course, the passage is repeated in the prompt of each question, so you can practise without turning pages."),
            H("Time and review"),
            T("Our practice settings give 90 minutes for a Paper 1 mock (the Board's own timing: check with your teacher). That is under two "
              "minutes a question. Do the easy items first, mark the difficult ones, and come back. Never leave a question blank: with four options, a "
              "guess after eliminating two options has a fair chance. Whether wrong answers lose marks is a point to check with your teacher; "
              "it is safest to answer every question."),
            MISTAKE("Choosing the first option that sounds right", "Several options may sound right to your ear. Check every option against a rule."),
            MISTAKE("Ignoring the instruction", "Some items ask for the incorrect sentence, or the one that is not correct. Read the instruction twice."),
            MISTAKE("Spending too long on one item", "A difficult question has the same value as an easy one. Move on and return."),
            QUIZ("Which approach is best for a multiple-choice grammar item?",
                 ["Pick the longest option.", "Predict an answer, eliminate wrong options, then check the choice in the sentence.", "Choose the first option.", "Skip it if you are not sure."],
                 1, "Predicting and eliminating uses your grammar knowledge, and checking avoids small slips.",
                 hint="Which answer uses grammar rules?",
                 feedback=["Length has nothing to do with correctness.", "", "The first option is correct only by chance.", "A blank gives no mark; an educated guess may."]),
            QUIZ("An item reads: « Elle est ______ hier soir. » Which clue should you use first?",
                 ["The word « soir ».", "The word « hier »: it shows a past time.", "The word « elle ».", "The capital letter."],
                 1, "« Hier » signals the past, which helps choose a past participle with the correct agreement.",
                 hint="Which word gives the time?",
                 feedback=["« Soir » does not decide the tense.", "", "« Elle » helps with agreement but not with tense.", "A capital letter shows nothing."]),
            H("Practice"),
            PQ("List the four steps of the routine for a multiple-choice item.",
               "Lire, prédire, éliminer, vérifier (read, predict, eliminate, check)."),
            PQ("Why do you check agreement before choosing an option for a verb in the passé composé with être?",
               "Because the past participle agrees with the subject: « elles sont allées », not « elles sont allé »."),
            PQ("A question has an unknown word in the stem. What do you do?",
               "Use the words around it and the options; eliminate impossible choices; do not leave the question blank."),
            PQ("How does the report describe the marking of Paper 1?",
               "It is marked electronically (by machine), so only the chosen option counts."),
            SUM("Paper 1 had 50 multiple-choice questions in 2023, 40% of the examination, covering the whole syllabus, marked by machine.",
                "Use the four-step routine: lire, prédire, éliminer, vérifier.",
                "Check agreement, tense markers, prepositions, pronouns and register.",
                "Manage your time, mark hard items and return to them, and answer every question.",
                "Practise all six modules, not only your favourite."),
        ],
    ),
    # ------------------------------------------------------------------ 11. Exam Paper 2
    lesson(
        module=M_EXAM, topic="Paper 2",
        title="Paper 2 strategy: translation and essay",
        slug="frx-paper-2-strategy",
        minutes=24,
        summary="How to approach French Paper 2: what the Board's report says about Question 1 (translation) and Question 2 (essay), "
                "how to plan your time, and the errors that cost marks.",
        objectives=[
            "State the structure of Paper 2 and the two skills it tests",
            "Plan the translation and the essay with a clear method",
            "Avoid the errors named in the Board's 2023 report",
            "Review your answers with a short checklist",
        ],
        key_concepts=["Paper 2", "Traduction", "Rédaction", "Pertinence", "Cohérence", "Relecture"],
        blocks=[
            H("Introduction"),
            T("Paper 2 asks you to write, not to choose. The Board's 2023 report says it has Question 1 (Translation) and Question 2 (Essay). "
              "Check the exact format with your teacher, because instructions can change."),
            KEY("What the 2023 report says", "Facts from the report, in general terms.", cards=[
                ["Translation", "The passage was a narrative told in the past. It needed the imparfait (about five times), a main narrative tense (passé composé or passé simple), one simple present and four plus-que-parfait."],
                ["Essay", "Candidates wrote 140 to 150 words on one of three topics: a narrative or descriptive essay, an informal letter, or a picture interpretation."],
                ["Criteria", "Pertinence (relevance), cohérence (coherence), correction de la langue (accuracy) and originalité (originality)."],
                ["Marking", "Examiners follow a mark guide with clear criteria; they look for what you can do, not only what you cannot."],
            ]),
            H("Question 1: Translation"),
            KEY("Method", "Follow it every time.", cards=[
                ["Lire", "Read the whole passage once."],
                ["Souligner les verbes", "Underline the verbs and decide the tense of each: imparfait, passé composé, plus-que-parfait, présent."],
                ["Traduire", "Translate sentence by sentence, giving the meaning, not word for word."],
                ["Relire", "Check tenses, agreement, accents and that no sentence is missing."],
            ]),
            T("The Board's report says that most candidates translated the vocabulary well, but some mixed up the tenses (imparfait against "
              "plus-que-parfait, passé composé against passé simple). A few recopied the passage or paraphrased it. Keep to the meaning of the text, "
              "sentence by sentence."),
            H("Question 2: Essay"),
            KEY("Method", "Plan before you write.", cards=[
                ["1. Choisir", "Choose the topic you can write best, not the one that sounds most impressive."],
                ["2. Lire les consignes", "Underline every instruction: who, what, where, when, how you felt."],
                ["3. Planifier", "Write a short plan of key words: introduction, development, conclusion."],
                ["4. Rédiger", "Write 140 to 150 words with the right tense: past for stories, passé composé for letters."],
                ["5. Relire", "Check word count, tenses, agreement, spelling."],
            ]),
            T("Topic types: a narration needs passé composé and imparfait, a letter needs the layout and tone of a letter, and a picture interpretation "
              "needs one tense per instruction, as the question says. In 2023 the first instruction of the picture topic asked for the passé composé."),
            H("Errors the report names"),
            CODE("""Traduction  - confondre imparfait / plus-que-parfait / passé composé
            - recopier le texte anglais sans le traduire
            - paraphraser au lieu de traduire

Rédaction   - ne pas lire les consignes
            - recopier le sujet (perte de temps)
            - écrire en anglais ou mélanger les deux langues
            - utiliser le passé simple dans une lettre
            - donner sa vraie identité au lieu de l'adresse du sujet
            - commencer une narration comme une lettre
            - mémoriser une rédaction modèle""", "text", title="Erreurs fréquentes"),
            EX("Exemple : planifier le temps",
               intro="Our practice paper gives 150 minutes (a KKEVO practice setting; check the real timing with your teacher). How could you split it?",
               steps=[
                   S("Translation", text="About 50 minutes: read, underline verbs, translate, reread."),
                   S("Essay", text="About 80 minutes: choose, plan (10 minutes), write, check."),
                   S("Review", text="Keep about 20 minutes at the end to reread both answers. This is a suggestion; adapt it to your own pace."),
               ]),
            MISTAKE("Writing a learned essay", "The report advises against model essays learned by heart. Use tools, not texts."),
            MISTAKE("Ignoring the word limit", "Far too short loses content; far too long loses accuracy and time. Count your words in the last minutes."),
            MISTAKE("Skipping the review", "A two-minute reread can catch missing agreements and accents."),
            QUIZ("According to the Board's report, which tense is NOT accepted in an informal letter?",
                 ["Passé composé", "Imparfait", "Passé simple", "Futur simple"],
                 2, "The report states that the passé simple is not accepted in letter writing.",
                 hint="Which tense is literary?",
                 feedback=["It is the normal past tense for letters.", "It is fine for description and habit.", "", "It is fine for plans."]),
            QUIZ("You see the instruction « Racontez... » in an essay topic. What do you write?",
                 ["A letter beginning « Cher ami ».", "A story in past tenses.", "A list of arguments.", "A dialogue only."],
                 1, "« Racontez » asks for a narrative. A narrative essay must not begin as a letter.",
                 hint="What does « raconter » mean?",
                 feedback=["The report says some candidates wrongly opened a narrative as a letter.", "", "That is argumentation.", "A dialogue is a different form."]),
            H("Practice"),
            PQ("What are the two questions of French Paper 2 according to the 2023 report?",
               "Question 1: Translation; Question 2: Essay."),
            PQ("Name the four criteria used to assess the essay.",
               "Pertinence, cohérence, correction de la langue and originalité."),
            PQ("Why should you not copy the topic at the start of the essay?",
               "It wastes time and brings no marks; the examiner already knows the topic."),
            PQ("Write a one-line checklist for reviewing your translation.",
               "Tenses (imparfait / passé composé / plus-que-parfait), agreement of adjectives and participles, accents, no missing sentence."),
            SUM("Paper 2 has Question 1 (Translation) and Question 2 (Essay); check the format with your teacher.",
                "Translation: underline the verbs, decide each tense, translate meaning sentence by sentence, reread.",
                "Essay: choose, read every instruction, plan, write 140 to 150 words, reread.",
                "The criteria are pertinence, cohérence, correction de la langue and originalité.",
                "Avoid learned essays, passé simple in letters, English words and copying the English or the topic."),
        ],
    ),
]
