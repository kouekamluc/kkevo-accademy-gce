"""Practice sets for A Level French (0745), Upper Sixth: Compréhension Auditive et Expression Orale (3 sets) and Examination (Paper 1, Paper 2,
Paper 3 sets), plus 'Paper 1 mock exam A' (50 multiple-choice questions across the four modules), 'Paper 2 practice paper A' (25 auto-markable
parts on planning, evidence and the unseen poem) and 'Paper 3 practice paper A' (20 translation and language parts).

Explanations are in English; French examples are original. Listening passages are WRITTEN TRANSCRIPTS (invented), not audio. All poems, extracts
and passages are invented for practice. Facts about set texts are limited to the works the Board's 2023 report names and to well-known outlines;
students must check them against their own copy.
"""

import random

from .dsl import *  # noqa: F403

COURSE = ("french", "upper-sixth")

M_FR = "Étude des Œuvres Françaises au Programme"
M_AF = "Étude des Œuvres Francophones Africaines au Programme"
M_DI = "Dissertation Littéraire et Commentaire Composé"
M_ORAL = "Compréhension Auditive et Expression Orale"
M_EXAM = "Examination"

FR1 = "Lire l'œuvre française au programme"
FR2 = "Thèmes et personnages"
FR3 = "Structure et style"
AF1 = "Lire l'œuvre africaine au programme"
AF2 = "Thèmes et contexte"
AF3 = "Narration et style"
DI1 = "La dissertation littéraire"
DI2 = "Intégrer les citations"
DI3 = "Le commentaire composé"
T_LISTEN = "La compréhension auditive"
T_EXPOSE = "L'exposé oral"
T_DEBAT = "Le débat spontané"


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

# ================================================================== 1. Listening
SET(M_ORAL, T_LISTEN, "Listening strategies and sound traps", "fru2-listening-comprehension", [
    K("What is the best thing to do BEFORE the listening starts?", "Read all the questions and predict the kind of answer needed", [
        ("Close your eyes and wait", "You lose the chance to know what to listen for."),
        ("Write the whole question paper again", "This wastes time; you only need to underline the question words."),
        ("Decide the answers from the title only", "Predict the type of answer, but wait for the speaker to give the facts.")],
      "Reading the questions first tells you what to listen for: place, number, reason, opinion.", "La compréhension auditive", "Recall", "Think about what you can do while the recording has not started."),
    K("The question is « Combien de centres de vaccination y a-t-il ? ». What type of answer do you listen for?", "A number", [
        ("A place name", "That would answer où ?"), ("A reason", "That would answer pourquoi ?"), ("A person", "That would answer qui ?")],
      "Combien asks for a quantity.", "La compréhension auditive", "Concept", "What does « combien » ask for?"),
    K("A speaker says: « Les prix ont baissé. Cependant, les salaires n'ont pas augmenté. » What does « cependant » signal?", "A contrast: the next idea is often the important one", [
        ("A reason", "A reason is signalled by parce que or car."), ("A conclusion", "A conclusion is signalled by donc or en conclusion."), ("An example", "An example is signalled by par exemple.")],
      "Cependant, mais and pourtant introduce a contrast.", "La compréhension auditive", "Concept", "Is the second sentence going with the first or against it?"),
    K("You hear « quatre-vingt-quinze ». Which number do you write?", "95", [
        ("45", "Quatre-vingt is 80, not 40."), ("415", "You put the digits together instead of adding 80 + 15."), ("75", "Soixante-quinze is 75.")],
      "Quatre-vingt = 4 x 20 = 80; 80 + 15 = 95.", "La compréhension auditive", "Calculation", "Count in twenties: quatre-vingt = 4 x 20."),
    K("You hear [ilzɔ̃ fini] with a z sound before the vowel. Which verb is it?", "ils ont fini (avoir)", [
        ("ils sont fini (être)", "Sont is heard with an s sound: [ilsɔ̃]."), ("il est fini", "Est is singular and has no z link."), ("ils ont finir", "A past participle, not an infinitive, follows avoir here.")],
      "A z sound links ils to a vowel: ils ont. With être it is ils sont, heard with an s.", "La compréhension auditive", "Concept", "Which verb makes a z sound with ils?"),
    K("Why do the prices rise at ten o'clock?", "Because demand increases", [
        ("Because merchants arrive early", "Merchants arrive first, before the prices rise."),
        ("Because the market closes", "The text does not say the market closes."),
        ("Because vegetables are fresher", "Freshness is not mentioned.")],
      "The speaker links the rise in prices to « parce que la demande augmente ».", "La compréhension auditive", "Application", "Find the word that gives a reason: parce que, car.",
      passage="**Transcript (invented; read aloud twice):** « Le marché du quartier ouvre à six heures. Les commerçants arrivent d'abord avec leurs légumes. Mais à dix heures, les prix montent parce que la demande augmente. »"),
    K("Which set of notes is best for « Les autorités conseillent de ne pas traverser les cours d'eau » ?", "autorités : conseil -> pas traverser cours d'eau", [
        ("Les autorités conseillent de ne pas traverser les cours d'eau", "A full copy is too slow while listening."),
        ("autorités", "Too short: the advice itself is missing."), ("cours d'eau, rivière, pluie, orage, nuit", "These are ideas you invented, not what was said.")],
      "Notes keep key words and a symbol; they do not copy the sentence.", "La compréhension auditive", "Application", "Which notes are short but still contain the advice?"),
    K("Choose the correct word: « Elle va ___ Limbé. »", "à", [("a", "A without accent is the verb avoir."), ("ah", "That is an exclamation."), ("as", "That is the verb avoir (tu as).")],
      "Homophones: a (avoir) and à (preposition). Here the preposition is needed.", "La compréhension auditive", "Application", "Is there a verb or a preposition before the place name?"),
], 701)

# ================================================================== 2. Oral presentation
SET(M_ORAL, T_EXPOSE, "Structuring and delivering an exposé", "fru2-oral-presentation", [
    K("What is an « accroche » in an exposé?", "A first sentence meant to catch the listener's attention", [
        ("The final sentence", "That is the conclusion or ouverture."), ("A list of sources", "An exposé does not begin with sources."), ("A repetition of the title", "The hook adds interest; it does not repeat the title.")],
      "The accroche is the hook at the start: a question, a short fact or a situation.", "L'exposé oral", "Recall", "It starts the talk; what is it meant to do?"),
    K("Where does the « annonce du plan » belong?", "At the end of the introduction", [
        ("In the middle of part 2", "The plan is announced before the parts."), ("After the conclusion", "It would come too late."), ("Nowhere: the plan stays secret", "The listener needs the plan to follow by ear.")],
      "Announce the plan at the end of the introduction.", "L'exposé oral", "Recall", "The listener needs the plan before the parts begin."),
    K("About how many words should a five-minute talk contain for a learner who speaks clearly?", "About 550 to 650", [
        ("About 100", "That is under a minute of speech."), ("About 2 000", "That would need very fast speech."), ("It does not matter", "Time and pace matter: plan your length.")],
      "Around 110 to 130 words a minute, so five minutes is about 550 to 650 words.", "L'exposé oral", "Calculation", "Multiply 120 words by 5 minutes."),
    K("Why is it better to speak from cards of key words than from a full script?", "Your voice stays natural and you can keep eye contact", [
        ("Because a script is forbidden by law", "There is no such law: it is a question of quality."), ("Because key words are longer", "Key words are short."), ("Because notes remove the need to practise", "You must still practise aloud.")],
      "Notes make you think and speak, so your delivery sounds natural.", "L'exposé oral", "Concept", "Think about a person reading aloud versus talking."),
    K("Which phrase announces a plan?", "« Je vais d'abord décrire les causes, ensuite les conséquences, enfin les solutions. »", [
        ("« Euh, voilà, c'est tout. »", "This ends the talk without a structure."), ("« Je ne sais pas quoi dire. »", "A plan is not announced."), ("« En conclusion, tout va bien. »", "This is a conclusion phrase.")],
      "An announced plan has d'abord, ensuite and enfin with the content of each part.", "L'exposé oral", "Application", "Which one lists the parts in order?"),
    K("What belongs in a conclusion?", "A short answer to the problématique and an ouverture", [
        ("A brand-new argument", "It cannot be developed any more."), ("A long apology", "It lowers the impression."), ("A copy of the whole talk", "Repetition adds nothing.")],
      "Answer the question you asked and open the topic wider.", "L'exposé oral", "Concept", "What did you ask in the introduction?"),
    K("The listener asks a question you did not expect. Which reply is best?", "« C'est une bonne question. Si je comprends bien, vous me demandez pourquoi... »", [
        ("« Je ne sais pas. » and silence", "Reformulate to gain time and show engagement."), ("« Cette question est idiote. »", "Impolite."), ("A change of subject without an answer", "The listener notices and trusts you less.")],
      "Reformulating buys time and shows that you listen.", "L'exposé oral", "Application", "Which reply buys time politely?"),
    K("For an exposé on a set novel, which is most important in each part?", "A precise example taken from the book", [
        ("A general opinion about literature", "The Board's report says candidates lose marks for general answers."), ("A long quotation from memory", "A short, exact reference is better."), ("The author's life story only", "It does not prove the point about the text.")],
      "Each part needs a precise reference to the text, checked against your own copy.", "L'exposé oral", "Reasoning", "What does the Board say candidates forget?"),
], 702)

# ================================================================== 3. Spontaneous debate
SET(M_ORAL, T_DEBAT, "Arguing, conceding and replying in a debate", "fru2-spontaneous-debate", [
    K("Which order gives a good 30-second intervention?", "Position, reason, example, link", [
        ("Example, link, reason, position", "The listener will not know your point."), ("Link, link, link, link", "There is no content."), ("Reason, position, silence", "There is no example.")],
      "State your position, give a reason, add an example and link back.", "Le débat spontané", "Recall", "Start with what you think."),
    K("Which sentence contains a concession?", "« Certes, le numérique est pratique, mais il coûte cher. »", [
        ("« Le numérique coûte cher. »", "There is no admission of the other side's point."), ("« Vous avez tort. »", "An attack, not a concession."), ("« Je ne sais pas. »", "No argument.")],
      "Certes... mais... admits a point and then replies.", "Le débat spontané", "Application", "Which sentence first admits something?"),
    K("Complete: « Je ne pense pas que ce ___ une bonne idée. »", "soit", [("est", "The indicative is not used after a negated opinion verb."), ("sera", "The future is not a subjunctive."), ("serait", "The conditional is not a subjunctive.")],
      "Je ne pense pas que + subjunctive: que ce soit.", "Le débat spontané", "Application", "After a negated opinion verb, which mood?"),
    K("Complete: « Bien que les prix ___ bas, les clients hésitent. »", "soient", [("sont", "Bien que takes the subjunctive."), ("seront", "Bien que takes the subjunctive, not the future."), ("étaient", "Bien que takes the present subjunctive here.")],
      "Bien que + subjunctive. Être gives qu'ils soient.", "Le débat spontané", "Application", "Which conjunction forces the subjunctive?"),
    K("Which is the politest way to interrupt?", "« Excusez-moi de vous interrompre, mais... »", [("« Taisez-vous. »", "Rude."), ("« Vous dites n'importe quoi. »", "An attack on the person."), ("« Non, non, non ! »", "No polite phrase.")],
      "Use a polite phrase and keep the interruption short.", "Le débat spontané", "Application", "Which phrase begins with an apology?"),
    K("Which word describes a disease that spreads across several continents?", "une pandémie", [("une épidémie", "That spreads in a region or a country."), ("une endémie", "That is a disease constantly present in one area."), ("une allergie", "That is not an infectious disease.")],
      "A pandémie is worldwide; an épidémie is local or national.", "Le débat spontané", "Concept", "Think of the Board's report on epidemic and pandemic."),
    K("According to the Board's report, in group discussion students should speak in:", "French or English, not pidgin", [
        ("Pidgin only", "The report says not pidgin."), ("Only their home language", "The report names French or English."), ("Silence", "The report encourages group discussion.")],
      "The report recommends discussions in French or English, not pidgin.", "Le débat spontané", "Recall", "Check the recommendation for students."),
    K("You freeze in a debate. Which is the best way out?", "Reformulate the previous speaker's point and add an example", [
        ("Say nothing until the end", "You lose your turn."), ("Change the topic to something easier", "It breaks the debate."), ("Speak in a language the others do not know", "It defeats the purpose.")],
      "Reformulating buys time and keeps you in the discussion.", "Le débat spontané", "Application", "How can you gain time and still be useful?"),
], 703)

# ================================================================== 4. Paper 1 strategy
SET(M_EXAM, "Paper 1", "Paper 1 strategy: grammar, vocabulary and literary notions", "fru2-paper-1-strategy", [
    K("According to the Board's 2023 report, Paper 1 is made up of:", "50 multiple-choice questions on grammar, vocabulary, expressions and literary notions", [
        ("Two long essays", "Essays are in Papers 2 and 3."), ("A translation and a poem", "Translation belongs to Paper 3."), ("An oral test", "The report does not describe an oral test.")],
      "Paper 1 is the multiple-choice paper.", "Paper 1", "Recall", "Which paper is the multiple-choice one?"),
    K("Complete: « Les fleurs qu'elle a ___ sont belles. » (cueillir)", "cueillies", [
        ("cueilli", "The direct object « que » (= les fleurs) is before the verb, so the participle agrees."), ("cueillit", "That is a passé simple form."), ("cueillie", "The object is plural.")],
      "Que stands for les fleurs, feminine plural, placed before avoir: cueillies.", "Paper 1", "Application", "Is the direct object before the verb?"),
    K("Complete: « Bien qu'il ___ fatigué, il travaille. »", "soit", [("est", "Bien que takes the subjunctive."), ("sera", "Bien que takes the subjunctive."), ("serait", "Bien que takes the present subjunctive here.")],
      "Bien que + subjunctive; être gives qu'il soit.", "Paper 1", "Application", "Which mood follows bien que?"),
    K("Complete: « La raison ___ il est parti reste inconnue. »", "pour laquelle", [("dont", "Dont replaces de + noun; here the preposition is pour."), ("que", "Que is a direct object, but pour is needed."), ("qui", "Qui is a subject; il is already the subject.")],
      "Partir pour une raison: pour laquelle.", "Paper 1", "Application", "Which preposition goes with « raison » here?"),
    K("Complete: « Si nous avions de l'argent, nous ___ . »", "voyagerions", [("voyagerons", "Si + imparfait goes with the conditional, not the future."), ("voyageons", "The present does not fit si + imparfait."), ("avons voyagé", "The passé composé does not fit.")],
      "Si + imparfait -> conditional present.", "Paper 1", "Application", "Which tense follows si + imparfait?"),
    K("« Je t'ai dit mille fois de ne pas le faire. » Which figure of style is it?", "Hyperbole", [("Litote", "A litote says less."), ("Oxymore", "No contradiction of terms."), ("Antithèse", "No contrast of two ideas.")],
      "Mille fois exaggerates: hyperbole.", "Paper 1", "Concept", "Is the statement exaggerated?"),
    K("« Actuellement » in French means:", "at present", [("actually", "Actually is en fait."), ("in the past", "It refers to now."), ("in the future", "It refers to now.")],
      "Faux ami: actuellement = at present.", "Paper 1", "Recall", "Think of the false-friend list."),
    K("An alexandrin is a line with:", "12 syllables", [("8 syllables", "That is an octosyllable."), ("10 syllables", "That is a décasyllabe."), ("14 syllables", "That is not a standard French line.")],
      "Alexandrin = 12 syllables.", "Paper 1", "Recall", "The name suggests twelve."),
], 704)

# ================================================================== 5. Paper 2 strategy
SET(M_EXAM, "Paper 2", "Paper 2 strategy: literature essays and the unseen poem", "fru2-paper-2-strategy", [
    K("What did the Board's report say was the main weakness in many literature answers?", "Candidates did not support their points with facts and examples from the text", [
        ("Their handwriting", "The report does not mention it."), ("Too many correct quotations", "The report says the opposite."), ("Writing in the wrong language", "Language is not the main point here.")],
      "The report says candidates gave general answers and could not substantiate with the text.", "Paper 2", "Recall", "Which skill do essays need to prove a point?"),
    K("In which order should you analyse an unseen poem?", "Structure, tenses, lexical field, message", [
        ("Message, signature, title, date", "These are not the points the report expects."), ("Only the title", "The title is not enough."), ("Only the last line", "You need the whole poem.")],
      "The report expects structure (external and internal), tenses, lexical field and message.", "Paper 2", "Application", "Start from the external appearance."),
    K("Which sentence is a problématique?", "« Comment l'autorité des parents influence-t-elle les choix des enfants dans le roman ? »", [
        ("« Le roman parle de parents. »", "A statement, not a question."), ("« Les parents ont de l'autorité. »", "A statement."), ("« Voici mon plan. »", "A plan announcement, not a problem.")],
      "A problématique is a real question that the essay will answer.", "Paper 2", "Concept", "Which one is a question to be answered?"),
    K("A question on parents' authority in a novel: what does the Board's report say about the word « parents »?", "It can extend to elders of the village", [
        ("It can only mean the father and the mother", "The report says candidates were too narrow."), ("It never includes uncles", "The report refers to elders."), ("It is not important", "Understanding key words is essential.")],
      "Think of the wider social meaning of key words.", "Paper 2", "Interpretation", "Think of African extended society."),
    K("Which paragraph structure is best in a literature essay?", "Argument, example from the text, analysis, link with the question", [
        ("Opinion, opinion, opinion", "No proof."), ("Retelling of the plot only", "A retelling is not an argument."), ("Quotation only", "A quotation without analysis proves nothing.")],
      "Argument + precise example + analysis + link.", "Paper 2", "Concept", "What is needed after an example?"),
    K("A question says: « Aucune mère ne peut être contre sa fille. » Which line of argument fits the Board's expectations about a play where a mother defends her daughter's interests?", "A mother may disagree about means but works for her daughter's happiness", [
        ("The mother is totally against her daughter", "The report notes that candidates wrongly claimed this."), ("Mothers never disagree", "The report allows divergent opinions and approaches."), ("Only fathers matter", "The question is about mothers.")],
      "The report expects mothers to be shown protecting their children even when approaches differ.", "Paper 2", "Reasoning", "Think of mothers' aims versus methods."),
    K("Why did the Board's report advise teachers to teach selected Baudelaire poems?", "Many teachers avoid them and focus only on the unseen poem", [
        ("Because Baudelaire is easy", "The report does not say so."), ("Because the unseen poem is never set", "It was the most popular question in 2023."), ("Because poems are not examined", "Poetry is a section of Paper 2.")],
      "The report says teachers avoid prescribed poems and concentrate on the unseen one.", "Paper 2", "Recall", "Look at the teachers' recommendations."),
    K("A question asks you to use your society AND the text. What should you do?", "Use examples from both", [
        ("Use only your society", "The text is also asked for."), ("Use only the text", "Your society is also asked for."), ("Use neither, only your opinion", "Evidence is required.")],
      "The 2023 questions often combined real life and the text.", "Paper 2", "Application", "Check what the question demands."),
], 705)

# ================================================================== 6. Paper 3 strategy
SET(M_EXAM, "Paper 3", "Paper 3 strategy: essay writing and translation", "fru2-paper-3-strategy", [
    K("In 2023 the Board's report says candidates in Paper 3 essays had to:", "Choose one of four life situations", [
        ("Write all four essays", "Only one was chosen."), ("Write a poem commentary", "That is Paper 2."), ("Write only a translation", "Translation is a separate question.")],
      "Four life situations were offered and one chosen.", "Paper 3", "Recall", "How many essays were offered and how many answered?"),
    K("A debate question says « Êtes-vous pour ou contre ? ». What must the introduction contain?", "Your position", [
        ("Only a quotation", "A position is required."), ("A neutral list of both sides without choice", "The question asks for a stand."), ("A translation", "Not relevant.")],
      "State your position early and defend it.", "Paper 3", "Application", "The question is a choice between two sides."),
    K("Which word is correct for a disease that spreads in several countries around the world?", "une pandémie", [("une épidémie", "Local or national."), ("une allergie", "Not contagious."), ("une famine", "Lack of food, not a disease.")],
      "Pandémie = worldwide.", "Paper 3", "Concept", "Local or worldwide?"),
    K("Translate: « He is attending a meeting. »", "Il assiste à une réunion.", [("Il assiste une réunion.", "Assister takes à."), ("Il attend une réunion.", "Attendre = to wait for."), ("Il aide une réunion.", "Aider = to help.")],
      "Assister à = to attend.", "Paper 3", "Application", "Which verb means to attend?"),
    K("Translate: « I have lived here for ten years. »", "J'habite ici depuis dix ans.", [("J'ai habité ici pour dix ans.", "Depuis + present is used for an action still going on."), ("J'habiterai ici depuis dix ans.", "The future does not fit."), ("Je suis habité ici il y a dix ans.", "Ungrammatical.")],
      "Present perfect + for -> present + depuis in French.", "Paper 3", "Application", "Is the action still going on?"),
    K("Translate: « Many houses were destroyed by the floods. »", "De nombreuses maisons ont été détruites par les inondations.", [("De nombreuses maisons ont été détruit par les inondations.", "The participle agrees: détruites."), ("De nombreuses maisons étaient détruire par les inondations.", "Wrong verb form."), ("Beaucoup de maisons détruisaient les inondations.", "Meaning reversed.")],
      "Passive: ont été + participle agreeing with maisons: détruites.", "Paper 3", "Application", "Check the agreement of the participle."),
    K("« Actually » translates into French as:", "en fait", [("actuellement", "This is at present."), ("récemment", "This is recently."), ("autrefois", "This is formerly.")],
      "Actually = en fait, à vrai dire.", "Paper 3", "Recall", "Think of the false friend."),
    K("The question says: « Faites-nous part de votre rapport. » What is the text type?", "A report or talk presenting your findings and measures", [
        ("A poem", "No poetic form."), ("A dialogue", "No dialogue requested."), ("A dictionary entry", "Not appropriate.")],
      "A report presents information and recommendations in an organised way.", "Paper 3", "Concept", "What is a rapport?"),
], 706)

# ================================================================== Paper 1 mock exam A (50 questions)
P1 = [
    # --- Étude des Œuvres Françaises au Programme: Lire l'œuvre (5)
    K("*Les Fausses Confidences* de Marivaux est :", "une comédie", [("une tragédie", "A tragedy ends in death or ruin; this is a comedy."), ("un recueil de poèmes", "Poems are in Baudelaire's collection."), ("un roman à la première personne", "It is a play.")],
      "Les Fausses Confidences is a comedy for the theatre (check your own copy).", FR1, "Recall", "Is it a play or a novel, a comedy or a tragedy?"),
    K("Baudelaire est surtout connu pour le recueil :", "Les Fleurs du mal", [("Le Dernier Jour d'un condamné", "That is a work by Victor Hugo."), ("La Tragédie du Roi Christophe", "That is a play by Césaire."), ("Les Fausses Confidences", "That is a play by Marivaux.")],
      "Les Fleurs du mal is Baudelaire's best-known collection of poems.", FR1, "Recall", "Think of the poet of the Board's poetry section."),
    K("Dans *Le Dernier Jour d'un condamné*, Victor Hugo fait raconter l'histoire par :", "un condamné à mort, à la première personne", [("un narrateur omniscient extérieur", "The story is told by the condemned man himself."), ("le juge", "The judge is not the narrator."), ("un enfant témoin", "The narrator is the condemned man.")],
      "The novel is narrated in the first person by the condemned man (check your copy).", FR1, "Recall", "Who says « je » in the novel?"),
    K("*Le Dernier Jour d'un condamné* est :", "un roman (récit)", [("une comédie", "It is prose fiction, not a play."), ("un poème lyrique", "It is not in verse."), ("un essai de grammaire", "It is a work of fiction.")],
      "It is a prose narrative, a short novel.", FR1, "Recall", "Is it in verse or prose?"),
    K("Selon le rapport 2023 du Board, que conseille-t-on aux élèves pour les textes au programme ?", "Les lire attentivement pour répondre avec précision", [("Ne lire que les résumés", "The report advises intensive reading."), ("Lire seulement le poème inconnu", "The set texts must be read."), ("Ne pas les lire, car on peut réussir les Papers 1 et 3", "The report criticises this belief.")],
      "The report recommends intensive reading of the set texts.", FR1, "Recall", "Check the students' recommendations."),
    # --- Thèmes et personnages (4)
    K("Dans *Les Fausses Confidences*, Dorante est :", "un jeune homme amoureux d'Araminte", [("la mère d'Araminte", "Argante is Araminte's mother."), ("un roi haïtien", "That is Christophe in Césaire's play."), ("le condamné de Hugo", "That is a different work.")],
      "Dorante loves Araminte (check your copy for the details).", FR2, "Recall", "He is a character who loves."),
    K("Dans la même pièce, Argante est :", "la mère d'Araminte, qui défend les intérêts de sa fille", [("la servante de Dorante", "Argante is Araminte's mother."), ("une amie du roi", "Not in this play."), ("le narrateur", "A play has no narrator.")],
      "The Board's report says Argante defends her daughter's interests.", FR2, "Recall", "Think of the question on mothers."),
    K("Le thème central du *Dernier Jour d'un condamné* est :", "la peine de mort et l'angoisse du condamné", [("la fortune du roi", "That is not the theme."), ("le mariage de Fanny", "That is Bebey's novel."), ("la vie à la campagne", "Not the central subject.")],
      "Hugo's work is known as an argument against the death penalty (check your edition).", FR2, "Recall", "What is the condemned man facing?"),
    K("Le protagoniste d'une œuvre est :", "le personnage principal", [("le narrateur obligatoire", "A protagonist is not necessarily the narrator."), ("l'auteur", "The author is not a character."), ("l'adversaire du héros", "That is the antagoniste.")],
      "Protagoniste = main character.", FR2, "Recall", "Think of the prefix proto-: first."),
    # --- Structure et style (4)
    K("« Cette salle est un four. » est :", "une métaphore", [("une comparaison", "No comparison word."), ("une litote", "No understatement."), ("un oxymore", "No contradictory pair.")],
      "Identification without a comparison word: metaphor.", FR3, "Concept", "Is there a word like comme?"),
    K("Quel schéma de rimes : soir, jour, espoir, amour ?", "ABAB (croisées)", [("AABB (plates)", "Plates would be soir, espoir, jour, amour."), ("ABBA (embrassées)", "Embrassées would be soir, jour, amour, espoir."), ("ABCD (sans rime)", "There are rhymes: soir/espoir and jour/amour.")],
      "Soir (A), jour (B), espoir (A), amour (B): crossed rhymes ABAB.", FR3, "Application", "Label each line-ending with the same letter if it rhymes."),
    K("Un alexandrin est un vers de :", "12 syllabes", [("8 syllabes", "That is an octosyllable."), ("10 syllabes", "That is a décasyllabe."), ("6 syllabes", "That is a hexasyllable.")],
      "The alexandrine has twelve syllables.", FR3, "Recall", "The name comes from a twelve-syllable verse."),
    K("Un retour en arrière dans un récit s'appelle :", "une analepse (flashback)", [("une ellipse", "An ellipse skips time."), ("une didascalie", "That is a stage direction."), ("une tirade", "That is a long speech.")],
      "A flashback = analepse.", FR3, "Recall", "Look back in time."),
    # --- Lire l'œuvre africaine (4)
    K("Qui a écrit *Le Fils d'Agatha Moudio* ?", "Francis Bebey", [("Victor Hugo", "Hugo wrote Le Dernier Jour d'un condamné."), ("Marivaux", "Marivaux wrote comedies."), ("Aimé Césaire", "Césaire wrote La Tragédie du Roi Christophe.")],
      "The Board's report names Francis Bebey as its author.", AF1, "Recall", "Check the prose section of the report."),
    K("*Le Fils d'Agatha Moudio* est :", "un roman", [("un recueil de poèmes", "It is prose fiction."), ("une comédie en cinq actes", "It is a novel."), ("un essai politique", "It is fiction.")],
      "It is a novel (check your edition).", AF1, "Recall", "Is it a play, a poem or a novel?"),
    K("*La Tragédie du Roi Christophe* est :", "une pièce de théâtre", [("un roman", "It is a play."), ("un recueil de nouvelles", "It is a play."), ("un journal intime", "It is a play.")],
      "The Board's report places it in the drama section.", AF1, "Recall", "Look at the drama section of the report."),
    K("Une question parle des « parents » dans un roman africain. Que faut-il comprendre ?", "Le mot peut inclure les aînés et la famille élargie", [("Uniquement le père et la mère", "The report says this is too narrow."), ("Uniquement les voisins", "Not correct."), ("Aucune personne âgée", "Elders are often included.")],
      "The Board's report notes that « parents » can include elders in the village.", AF1, "Interpretation", "Think of the extended family."),
    # --- Thèmes et contexte (4)
    K("Dans *Le Fils d'Agatha Moudio*, un thème discuté par le Board est :", "la pression des parents sur les enfants", [("la peine de mort", "That is Hugo's theme."), ("les voyages dans l'espace", "Not relevant."), ("la gloire des rois", "That is Christophe's play.")],
      "The Board's report names parental pressure (Fanny, Mbenda).", AF2, "Recall", "Check the prose questions of the report."),
    K("Dans *L'Enfant de la révolte muette*, la question du Board sur l'égalité compare :", "le couple Nathalie et Jean-Marie", [("Dorante et Araminte", "That is Marivaux's play."), ("Fanny et Mbenda", "That is Bebey's novel."), ("Baudelaire et Hugo", "These are authors.")],
      "The report asks to apply gender equality to Nathalie and Jean-Marie.", AF2, "Recall", "Look at question 6 of the report."),
    K("*La Tragédie du Roi Christophe* a pour contexte :", "Haïti après l'indépendance", [("la France de Louis XIV", "The context is Haitian."), ("le Cameroun d'aujourd'hui", "Not the setting."), ("la Grèce antique", "Not the setting.")],
      "The play shows Henri Christophe, king in Haiti after independence (check your copy).", AF2, "Recall", "Where did a King Christophe rule?"),
    K("Le « contexte » d'une œuvre désigne :", "le cadre historique et social dans lequel elle a été écrite ou se déroule", [("sa couverture", "That is not context."), ("le nombre de pages", "That is not context."), ("le nom de l'éditeur", "That is not context.")],
      "Context = historical and social setting.", AF2, "Concept", "Think history and society."),
    # --- Narration et style (4)
    K("Dans un récit à la première personne, on trouve surtout :", "le pronom « je »", [("le pronom « on » seulement", "Je is the mark of first person."), ("le pronom « ils » seulement", "That is third person."), ("aucun pronom", "There are pronouns.")],
      "First-person narration uses je (and nous).", AF3, "Concept", "Who speaks?"),
    K("Un narrateur omniscient :", "sait tout sur les personnages et leurs pensées", [("ne sait rien", "That is not omniscient."), ("est toujours un personnage", "Not necessarily."), ("n'utilise jamais le passé", "Unrelated.")],
      "Omniscient = knows everything.", AF3, "Concept", "Omni = all."),
    K("Selon le rapport, la description et le flashback aident à :", "faciliter la compréhension, révéler les personnages et susciter l'intérêt", [("remplir le livre", "The report stresses function."), ("remplacer l'histoire", "They support the story."), ("cacher le sens", "They help understanding.")],
      "The report lists understanding, character revelation and reader interest.", AF3, "Interpretation", "Check question 5 of the report."),
    K("Pour un retour en arrière dans un récit au passé, on emploie souvent :", "le plus-que-parfait", [("le futur simple", "Future is forward in time."), ("le présent de l'impératif", "Not used for flashbacks."), ("le subjonctif présent", "Not the narrative tense.")],
      "The pluperfect marks an action before the main past action.", AF3, "Application", "Which tense goes before the past?"),
    # --- La dissertation littéraire (5)
    K("Une problématique est :", "la question centrale à laquelle l'essai répond", [("une conclusion", "The conclusion answers it."), ("un titre", "A title is not necessarily a question."), ("une citation", "A quotation is evidence.")],
      "The problématique is the central question.", DI1, "Concept", "What does the essay answer?"),
    K("Un plan dialectique suit l'ordre :", "thèse, antithèse, synthèse", [("synthèse, thèse, antithèse", "The order is thesis first."), ("exemple, exemple, exemple", "No argument structure."), ("introduction, introduction, conclusion", "Not a plan.")],
      "Dialectical plan: thesis, antithesis, synthesis.", DI1, "Recall", "Hegel's triad (thesis...)."),
    K("Quel est l'ordre de l'introduction d'une dissertation ?", "Amener le sujet, poser le sujet, problématique, annonce du plan", [("Annonce du plan, conclusion, titre", "Wrong order."), ("Problématique, amorce, exemple", "Incorrect order."), ("Conclusion, plan, sujet", "Incorrect order.")],
      "Introduction: amorce, subject, problématique, plan.", DI1, "Recall", "Start with the hook."),
    K("La conclusion d'une dissertation doit :", "répondre à la problématique", [("ajouter un nouvel argument", "It cannot be developed."), ("répéter l'introduction mot pour mot", "Repetition adds nothing."), ("s'excuser", "It lowers the impression.")],
      "Conclusion = answer + opening.", DI1, "Concept", "What did you ask?"),
    K("Quel connecteur marque l'opposition ?", "cependant", [("de plus", "That adds."), ("par conséquent", "That marks consequence."), ("par exemple", "That introduces an example.")],
      "Cependant introduces a contrast.", DI1, "Recall", "Which connector opposes?"),
    # --- Intégrer les citations (4)
    K("Une citation est placée entre :", "guillemets français « »", [("accolades", "Not for quotations."), ("crochets uniquement", "Brackets are for changes."), ("deux points", "A colon introduces it.")],
      "Quotations use guillemets.", DI2, "Recall", "French quotation marks."),
    K("Pour intégrer une citation, il faut :", "l'introduire puis l'analyser", [("la copier sans commentaire", "A quotation needs analysis."), ("la remplacer par un résumé sans source", "Evidence is needed."), ("la mettre à la fin sans lien", "It must be linked.")],
      "Introduce, quote, analyse.", DI2, "Concept", "What comes after the quote?"),
    K("Les points de suspension entre parenthèses ou crochets (...) ou […] indiquent :", "une coupure dans la citation", [("une erreur", "They mark an omission."), ("une question", "No."), ("un titre", "No.")],
      "(...) shows that words have been omitted.", DI2, "Recall", "What does the omission mark show?"),
    K("Quelle phrase intègre le mieux une citation ?", "Hugo souligne l'angoisse du condamné lorsqu'il écrit que [citation courte], ce qui montre sa peur.", [("« Citation seule. »", "No introduction or analysis."), ("Citation, citation, citation.", "No analysis."), ("Le texte est bien.", "No evidence.")],
      "A good integration has an introduction, a short quotation and an analysis.", DI2, "Application", "Which one introduces and explains?"),
    # --- Le commentaire composé (4)
    K("Un commentaire composé est :", "l'analyse organisée d'un texte en axes, avec des citations", [("un résumé du livre", "It analyses a passage."), ("une traduction", "It is not a translation."), ("une liste de mots", "It is organised analysis.")],
      "The commentaire composé groups observations by axes, with evidence.", DI3, "Concept", "Analysis or summary?"),
    K("Dans un commentaire composé, chaque axe comprend :", "des procédés (techniques) et leurs effets", [("des dates seulement", "Dates do not analyse style."), ("des opinions sans preuve", "Evidence is needed."), ("la biographie de l'auteur", "Not the main content.")],
      "Each axis links a technique to its effect.", DI3, "Concept", "Technique plus what?"),
    K("Quelle première étape pour un commentaire ?", "Lire le texte, repérer le thème et les procédés", [("Écrire la conclusion", "Too early."), ("Recopier le texte", "Wastes time."), ("Ignorer le texte", "You must read it.")],
      "Read, identify the theme, techniques, then plan the axes.", DI3, "Application", "What do you do first with any text?"),
    K("Pour un poème inconnu, le rapport attend l'analyse de :", "la structure, des temps, du champ lexical et du message", [("la date de publication seulement", "Not enough."), ("le nom du poète seulement", "Not enough."), ("la longueur du livre", "Not relevant.")],
      "The report lists structure, tenses, lexical field and message.", DI3, "Recall", "Check question 2 in the report."),
    # --- La compréhension auditive (4)
    K("« Quatre-vingt-douze » s'écrit :", "92", [("42", "Quatre-vingt is 80, not 40."), ("412", "You put digits together."), ("82", "Quatre-vingt-douze is 80 + 12.")],
      "4 x 20 + 12 = 92.", T_LISTEN, "Calculation", "Count in twenties."),
    K("Le mot « mais » dans un discours signale :", "un contraste", [("un exemple", "Par exemple does."), ("une conclusion", "En conclusion does."), ("une répétition", "No.")],
      "Mais introduces a contrast.", T_LISTEN, "Concept", "Does it add or oppose?"),
    K("Avant d'écouter un document, il faut :", "lire les questions", [("fermer les yeux", "It wastes the chance to prepare."), ("écrire la conclusion", "Too early."), ("dormir", "No.")],
      "Read the questions to know what to hear.", T_LISTEN, "Recall", "What do you do before the sound?"),
    K("On entend [ilsɔ̃] (avec le son s). Quelle phrase ?", "ils sont partis", [("ils ont partis", "Ont has a z liaison."), ("ils son partis", "Son is a noun determiner."), ("il est partis", "Not the form heard.")],
      "The s sound gives ils sont.", T_LISTEN, "Concept", "Which verb is heard with s?"),
    # --- L'exposé oral (4)
    K("Un exposé commence par :", "une accroche suivie du sujet et du plan", [("la conclusion", "Wrong place."), ("la bibliographie", "Not at the start."), ("un long silence", "No.")],
      "Hook, subject, problem, plan.", T_EXPOSE, "Recall", "How does the introduction begin?"),
    K("Pour parler cinq minutes, il vaut mieux utiliser :", "des fiches de mots-clés", [("un texte entièrement écrit à lire", "Reading kills natural delivery."), ("aucune préparation", "Preparation is needed."), ("du pidgin", "Standard French is required.")],
      "Notes on cards keep delivery natural.", T_EXPOSE, "Application", "Notes or script?"),
    K("La transition « Passons maintenant à... » sert à :", "annoncer une nouvelle partie", [("conclure", "That would be en conclusion."), ("s'excuser", "No."), ("poser une question au jury", "No.")],
      "It is a signpost between parts.", T_EXPOSE, "Concept", "Moving on."),
    K("Après l'exposé, une question inattendue : que faire ?", "Reformuler la question puis répondre avec un exemple", [("Quitter la salle", "No."), ("Répondre à côté", "No."), ("Rire", "No.")],
      "Reformulate to gain time and answer.", T_EXPOSE, "Application", "How do you gain time?"),
    # --- Le débat spontané (4)
    K("Complète : « Il faut que nous ___ à choisir. » (apprendre)", "apprenions", [("apprenons", "Il faut que takes the subjunctive."), ("apprendrons", "Not a subjunctive."), ("apprenez", "Wrong person.")],
      "Subjunctive of apprendre: que nous apprenions.", T_DEBAT, "Application", "Which mood follows il faut que?"),
    K("« Certes, c'est pratique, mais c'est cher. » C'est :", "une concession suivie d'une réplique", [("une conclusion", "No."), ("une question", "No."), ("une insulte", "No.")],
      "Certes... mais admits then replies.", T_DEBAT, "Concept", "What does certes admit?"),
    K("Quelle formule demande poliment la parole ?", "Puis-je dire un mot ?", [("Taisez-vous !", "Rude."), ("Moi d'abord !", "Impolite."), ("Vous avez tort !", "Attack.")],
      "A polite request for the floor.", T_DEBAT, "Application", "Which one is a polite request?"),
    K("Une maladie qui touche plusieurs continents est :", "une pandémie", [("une épidémie", "Local or national."), ("une endémie", "Constantly present in one area."), ("une allergie", "Not contagious.")],
      "Pandémie = worldwide.", T_DEBAT, "Concept", "Local or worldwide?"),
]
assert len(P1) == 50, len(P1)
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="fru2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 710)))

# ================================================================== Paper 2 practice paper A (25 auto-markable parts)
POEM = ("**Poème inventé pour s'exercer (ne vient d'aucun examen)**\n\n"
        "Le fleuve passe sous le pont,\nIl chante un air toujours pareil ;\nLes jours s'en vont, les jours s'en vont,\nEt moi, j'attends le grand soleil.")

P2 = [
    # Question 1: unseen poem (6 parts)
    K("**Question 1(a).** Combien de strophes compte ce poème ?", "Une seule strophe (un quatrain)", [("Deux strophes", "There are four lines in one block."), ("Quatre strophes", "Each line is not a stanza."), ("Aucune strophe", "A stanza is a block of lines, and this is one.")],
      "Four lines form one quatrain.", DI3, "Recall", "Count the blocks of lines.", passage=POEM),
    K("**Question 1(b).** Quel est le schéma des rimes ?", "ABAB (rimes croisées)", [("AABB (plates)", "Pont/pareil are not neighbours that rhyme."), ("ABBA (embrassées)", "The second and third lines do not rhyme."), ("Aucune rime", "Pont/vont and pareil/soleil rhyme.")],
      "Pont (A), pareil (B), vont (A), soleil (B).", DI3, "Application", "Label the endings pont, pareil, vont, soleil.", passage=POEM),
    K("**Question 1(c).** Combien de syllabes comptent les vers (e muet en fin de vers non compté) ?", "8 syllabes (octosyllabes)", [("12 syllabes", "That would be alexandrines."), ("10 syllabes", "That would be décasyllabes."), ("6 syllabes", "That is too short.")],
      "Le-fleu-ve-pas-se-sous-le-pont: 8 syllables, the e of « fleuve » and « passe » counting before a consonant.", DI3, "Application", "Count one line slowly: Le (1) fleu (2)...", passage=POEM),
    K("**Question 1(d).** Quel effet produit la répétition « les jours s'en vont, les jours s'en vont » ?", "Elle insiste sur le passage monotone du temps", [("Elle exprime la colère", "The tone is calm."), ("Elle annonce un changement joyeux", "It stresses repetition, not change."), ("Elle prouve que le poème est un dialogue", "There is one speaker.")],
      "Repetition imitates the flow of time and boredom.", DI3, "Interpretation", "What does repeating the same phrase suggest?", passage=POEM),
    K("**Question 1(e).** Quel temps domine dans le poème ?", "Le présent", [("Le futur", "The only future-like idea is « j'attends » in the present."), ("Le passé composé", "No past verbs."), ("Le plus-que-parfait", "No pluperfect.")],
      "Passe, chante, vont, attends are all present.", DI3, "Recall", "Look at the verbs.", passage=POEM),
    K("**Question 1(f).** Quel est le ton du poème ?", "Une attente mélancolique mais pleine d'espoir", [("Une colère violente", "No angry words."), ("Une joie bruyante", "The tone is quiet."), ("Une ironie amère", "No irony.")],
      "Les jours s'en vont (melancholy) and j'attends le grand soleil (hope).", DI3, "Interpretation", "Compare « s'en vont » and « le grand soleil ».", passage=POEM),
    # Question 2: essay planning (5 parts)
    K("**Question 2(a).** Sujet inventé : « Une mère ne désire que le bonheur de sa fille. Discutez à partir de *Les Fausses Confidences*. » Que signifie « Discutez » ?", "Examiner plusieurs points de vue, puis conclure par une opinion argumentée", [("Raconter l'intrigue", "A retelling does not discuss."), ("Recopier une scène", "That is not an analysis."), ("Répondre seulement par oui ou non", "A discussion needs argument.")],
      "Discuter = weigh arguments and reach a reasoned view.", DI1, "Concept", "Think of the verb discuter.", ),
    K("**Question 2(b).** Quelle est la meilleure problématique ?", "Dans quelle mesure l'attitude d'Argante montre-t-elle le souci du bonheur de sa fille ?", [("Argante est la mère d'Araminte.", "A fact, not a question."), ("Marivaux est un auteur du XVIIIe siècle.", "Not linked to the subject."), ("Le théâtre est un genre littéraire.", "Too general.")],
      "A problématique is a question that guides the essay.", DI1, "Application", "Which one is a question about the subject?"),
    K("**Question 2(c).** Pour le Board, quelle idée centrale convient à une partie sur Argante ?", "Une mère peut avoir une autre approche, mais elle protège les intérêts de sa fille", [("Argante est totalement contre sa fille", "The report notes this error."), ("Argante n'apparaît jamais dans la pièce", "She is a character."), ("Les mères n'ont aucune influence", "The question concerns the influence of mothers.")],
      "The report expects mothers to be shown protecting their children even when approaches differ.", DI1, "Reasoning", "What did the report say about the mother's limits?"),
    K("**Question 2(d).** Quel paragraphe est le plus solide ?", "Argante veut influencer le choix de sa fille (scène à citer de votre édition), ce qui montre qu'elle pense à son avenir, même si leurs idées diffèrent.", [("Argante est un personnage qui apparaît dans la pièce.", "No argument or analysis."), ("Marivaux a très bien écrit.", "An opinion without proof."), ("Voir le livre pour la réponse.", "No work done.")],
      "Argument + example + analysis + link.", DI1, "Application", "Which one has argument, example and analysis?"),
    K("**Question 2(e).** Quelle conclusion est la plus adaptée ?", "Ainsi, malgré leurs désaccords, mère et fille visent le même but : le bonheur d'Araminte.", [("En conclusion, je n'ai rien à dire.", "No answer."), ("Marivaux est né en 1688.", "Not an answer to the problem."), ("Voici une nouvelle idée : les valets décident de tout.", "A new, undeveloped idea.")],
      "A conclusion answers the question.", DI1, "Application", "Which one answers the problématique?"),
    # Question 3: narrative techniques (4 parts)
    K("**Question 3(a).** Sujet inventé : « Montrez que la narration à la première personne est efficace dans *Le Dernier Jour d'un condamné*. » Quel est l'effet principal de ce choix ?", "Le lecteur partage directement les pensées et la peur du condamné", [("Il éloigne le lecteur du personnage", "First person brings the reader closer."), ("Il supprime toute émotion", "The reverse is true."), ("Il rend le récit objectif", "It makes it subjective.")],
      "First-person narration brings the reader into the character's mind.", FR3, "Interpretation", "Who speaks, and how close does it bring the reader?"),
    K("**Question 3(b).** Le rapport critique les candidats qui « donnent des exemples » de narration. Que doit-on faire de plus ?", "Montrer comment la technique est efficace", [("Compter les pages", "Not a literary analysis."), ("Résumer toute l'histoire", "A summary does not evaluate."), ("Donner la biographie de l'auteur", "Not asked.")],
      "The report says candidates must show effectiveness, not only list examples.", FR3, "Reasoning", "Examples are not enough: what else?"),
    K("**Question 3(c).** Quelle phrase évalue le mieux l'effet d'un flashback ?", "Le souvenir révèle ce que le condamné a perdu, ce qui accroît l'émotion du lecteur", [("Il y a un flashback au chapitre 3.", "It identifies only."), ("Le flashback est un souvenir.", "It defines only."), ("Le flashback est long.", "It does not evaluate.")],
      "Evaluation links a technique to its effect.", FR3, "Application", "Which sentence explains an effect?"),
    K("**Question 3(d).** À quoi sert une description dans un roman, selon le rapport ?", "À faciliter la compréhension, révéler les personnages et susciter l'intérêt", [("À remplir les pages", "The report stresses function."), ("À remplacer l'histoire", "It supports the story."), ("À cacher les personnages", "It reveals them.")],
      "The report lists understanding, character revelation and interest.", FR3, "Recall", "Check question 5 of the report."),
    # Question 4: real life and text (4 parts)
    K("**Question 4(a).** Sujet inventé : « Les parents exercent trop d'autorité sur leurs enfants. Discutez à partir de *Le Fils d'Agatha Moudio*. » Le mot « parents » inclut :", "les parents, mais aussi les aînés de la famille et du village", [("seulement le père", "Too narrow."), ("seulement la mère", "Too narrow."), ("aucun adulte", "Parents are adults.")],
      "The Board's report notes that « parents » can extend to elders.", AF2, "Interpretation", "Think of the extended family."),
    K("**Question 4(b).** Que faut-il montrer pour réussir ce type de question selon le rapport ?", "Le lien parents-enfants, l'influence sur les actes et des exemples du texte avec leurs effets", [("Seulement l'opinion personnelle", "The text is needed."), ("Seulement le titre", "Not enough."), ("Seulement l'histoire de l'auteur", "Not asked.")],
      "The report expects the bond, the influence and text examples with their effects.", AF2, "Reasoning", "What three things does the report list?"),
    K("**Question 4(c).** Pour une question liant votre société et le texte, il faut :", "donner un exemple de la vie réelle et un exemple du texte", [("donner seulement un exemple de la vie réelle", "The text is also needed."), ("donner seulement un exemple du texte", "Real life is also needed."), ("ne donner aucun exemple", "Evidence is needed.")],
      "Combine real-life and textual evidence.", AF2, "Application", "Read the question words: votre pays + le texte."),
    K("**Question 4(d).** Pour *L'Enfant de la révolte muette*, quel domaine n'est PAS mentionné par le rapport pour comparer Nathalie et Jean-Marie ?", "Le sport professionnel", [("L'éducation", "The report lists education."), ("La vie professionnelle (le travail)", "The report lists work."), ("La responsabilité envers la famille", "The report lists family responsibility.")],
      "The report lists education, work, family responsibility and infidelity.", AF2, "Recall", "Check question 6 of the report."),
    # Question 5: quotations and commentary (4 parts)
    K("**Question 5(a).** Quelle intégration de citation est la meilleure ?", "Le narrateur dit qu'il [courte citation], ce qui révèle son angoisse.", [("« Citation de cinq lignes recopiée »", "Too long and not analysed."), ("Citation entre guillemets sans commentaire", "No analysis."), ("Aucune citation et aucun exemple", "No evidence.")],
      "Short quotation inside your own sentence, followed by analysis.", DI2, "Application", "Which one blends the quotation with analysis?"),
    K("**Question 5(b).** Que signifie (...) dans une citation ?", "Une partie du texte a été omise", [("Une faute d'orthographe", "It marks an omission."), ("Une question", "No."), ("Un titre", "No.")],
      "(...) shows that words have been left out.", DI2, "Recall", "What do suspension points show?"),
    K("**Question 5(c).** Pour un commentaire composé, un axe doit contenir :", "un procédé, une citation et son effet", [("une date de naissance", "Not an analysis."), ("un résumé du chapitre", "Not an analysis."), ("une opinion sans preuve", "No evidence.")],
      "Technique + quotation + effect.", DI3, "Concept", "What does an axis combine?"),
    K("**Question 5(d).** Quelle est la meilleure première étape pour un texte inconnu ?", "Lire attentivement, repérer le thème, les temps et le vocabulaire", [("Écrire la conclusion", "Too early."), ("Compter les lignes", "Not useful."), ("Ignorer les verbes", "Tenses matter.")],
      "Read and spot theme, tenses and vocabulary before planning.", DI3, "Application", "What must you understand before writing?"),
]
assert len(P2) == 23, len(P2)
P2_NUM = [
    NUM("**Question 6(a).** Dans ce paper d'entraînement KKEVO, vous avez 150 minutes pour 3 questions. Vous gardez 10 minutes par question pour planifier. Combien de minutes pour rédiger chaque réponse (le temps est partagé également) ?", 40,
        [S("Time per question", math=r"150 \div 3 = 50"), S("Remove planning time", math=r"50 - 10 = 40")],
        unit="minutes", concept=DI1, skill="Calculation", hint="Divide the total time by 3, then remove the planning time."),
    NUM("**Question 6(b).** Une dissertation a une introduction de 80 mots, trois paragraphes de 120 mots et une conclusion de 60 mots. Combien de mots en tout ?", 500,
        [S("Paragraphs", math=r"3 \times 120 = 360"), S("Add the rest", math=r"80 + 360 + 60 = 500")],
        unit="mots", concept=DI1, skill="Calculation", hint="Multiply, then add the three parts."),
]
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="fru2-paper-2-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P2, 720) + P2_NUM))

# ================================================================== Paper 3 practice paper A (20 auto-markable parts)
TX = ("**Texte inventé pour s'exercer :** « La famine reste un problème majeur dans plusieurs régions du monde. Les causes sont multiples : les sécheresses, "
      "la guerre et la pauvreté. »")

P3 = [
    K("**Part 1.** Traduisez en anglais : « La famine reste un problème majeur. »", "Famine remains a major problem.", [("The famine rests a majority problem.", "Majeur means major, not majority; rester means to remain."), ("Famine is a rest problem.", "Rester does not mean rest here."), ("The hunger stays a main majority.", "Unnatural and inaccurate.")],
      "La famine = famine; reste = remains; un problème majeur = a major problem.", "Paper 3", "Application", "Which one keeps the meaning?", passage=TX),
    K("**Part 2.** « plusieurs régions » se traduit par :", "several regions", [("pluralistic regions", "False friend: pluralistic is a different word."), ("more regions", "Plusieurs means several, not more."), ("some many regions", "Ungrammatical.")],
      "Plusieurs = several.", "Paper 3", "Recall", "Several, not plural.", passage=TX),
    K("**Part 3.** « les sécheresses » se traduit par :", "droughts", [("dry shirts", "A joke translation, not the word."), ("dryness of the sea", "Not the meaning."), ("secrets", "Mistaken by sound.")],
      "Une sécheresse = a drought.", "Paper 3", "Recall", "Think of lack of rain.", passage=TX),
    K("**Part 4.** Traduisez en français : « Famine affects children first. »", "La famine touche d'abord les enfants.", [("La famine affecte premier les enfants.", "Use d'abord (adverb), not premier."), ("Les enfants touchent la famine d'abord.", "The subject and the object are reversed."), ("La faim est touchée par les enfants.", "The meaning is reversed.")],
      "Affects = touche (or affecte); first = d'abord.", "Paper 3", "Application", "First (adverb) = d'abord."),
    K("**Part 5.** Traduisez : « Birth control is a delicate subject. »", "Le contrôle des naissances est un sujet délicat.", [("Le contrôle des naissances est un sujet délicieux.", "Délicieux means delicious."), ("Le contrôle des naissances est une sujet délicat.", "Sujet is masculine."), ("Le contrôle des naissances est sujet délicat.", "The article is missing.")],
      "Délicat is delicate; délicieux is a false friend; sujet is masculine.", "Paper 3", "Application", "Check gender and false friends."),
    K("**Part 6.** Traduisez : « The number of immigrants has increased. »", "Le nombre d'immigrés a augmenté.", [("Le nombre d'immigrés a augmentés.", "The participle after avoir stays masculine singular."), ("Le nombre d'immigrés a été augmenter.", "Wrong verb form."), ("Le nombre d'immigrés augmente depuis.", "Incomplete and awkward.")],
      "Has increased = a augmenté (passé composé).", "Paper 3", "Application", "Which tense translates the present perfect here?"),
    K("**Part 7.** Complétez : « Beaucoup de personnes migrent ___ l'Europe. »", "vers", [("à", "With the continent: en or vers; à is for towns."), ("pour", "Pour is not used for direction with migrate."), ("sur", "Sur means on.")],
      "Migrer vers l'Europe (or en Europe).", "Paper 3", "Application", "Which preposition expresses direction?"),
    K("**Part 8.** Traduisez : « Electrical appliances are used in almost every home. »", "Les appareils électriques sont utilisés dans presque tous les foyers.", [("Les appareils électriques sont utilisé dans presque chaque foyers.", "The participle agrees (utilisés) and chaque takes singular."), ("Les appareils électriques utilisent presque tous les foyers.", "The passive meaning is lost."), ("Les appareils électriques sont utilisés presque dans les foyers chaque.", "Unnatural order.")],
      "Passive: sont + participle agreeing with appareils: utilisés.", "Paper 3", "Application", "Check the agreement and the quantifier."),
    K("**Part 9.** « In recent years » se traduit par :", "Ces dernières années", [("Dans récent années", "Wrong form."), ("Les dernier années", "Agreement missing."), ("Pendant récemment", "Not French.")],
      "Ces dernières années = in recent years.", "Paper 3", "Recall", "Dernier agrees with années."),
    K("**Part 10.** Traduisez : « If the government invested in roads, farmers would earn more. »", "Si le gouvernement investissait dans les routes, les agriculteurs gagneraient plus.", [("Si le gouvernement investira..., les agriculteurs gagneraient plus.", "No future after si."), ("Si le gouvernement investirait..., les agriculteurs gagnent plus.", "No conditional after si."), ("Si le gouvernement a investi..., les agriculteurs gagneraient plus.", "The passé composé does not fit si + imparfait.")],
      "Si + imparfait + conditional.", "Paper 3", "Application", "Which tense follows si in an unreal condition?"),
    K("**Part 11.** Complétez : « Les mesures que le gouvernement a ___ ont aidé. » (prendre)", "prises", [("pris", "The object « que » = les mesures comes before: agreement."), ("prise", "The object is plural."), ("prendre", "Wrong form.")],
      "Feminine plural agreement: prises.", "Paper 3", "Application", "Is the direct object before avoir?"),
    K("**Part 12.** Complétez : « Il est essentiel que les dirigeants ___ des mesures. » (prendre)", "prennent", [("prenent", "Spelling error."), ("prendront", "Not the subjunctive."), ("prennaient", "Not the subjunctive.")],
      "Il est essentiel que + subjunctive: qu'ils prennent.", "Paper 3", "Application", "Which mood after il est essentiel que?"),
    K("**Part 13.** Complétez : « Le problème ___ nous parlons est grave. »", "dont", [("que", "Parler de requires dont."), ("qui", "Qui is a subject."), ("où", "Où is place or time.")],
      "Parler de quelque chose: dont.", "Paper 3", "Application", "Which preposition goes with parler?"),
    K("**Part 14.** Complétez : « Les routes sont mauvaises ; ___, les produits arrivent tard. »", "par conséquent", [("cependant", "That opposes; here we need a consequence."), ("par exemple", "That gives an example."), ("bien que", "A conjunction needing a verb after it.")],
      "Cause then consequence: par conséquent.", "Paper 3", "Application", "Is the second idea a result?"),
    K("**Part 15.** « Sensibiliser la population » signifie :", "to raise the population's awareness", [("to make the population ill", "Sensibiliser is not about illness."), ("to tax the population", "Not the meaning."), ("to make the population sensible", "False friend: sensible means raisonnable.")],
      "Sensibiliser = to raise awareness.", "Paper 3", "Concept", "Think of a public campaign."),
    K("**Part 16.** Dans une question de débat (« Êtes-vous pour ou contre ? »), l'introduction doit :", "indiquer votre position", [("éviter de choisir", "The question asks for a position."), ("raconter votre vie", "Not relevant."), ("citer seulement un proverbe", "Not enough.")],
      "State your position early and defend it.", T_DEBAT, "Application", "The question gives two options: choose."),
    K("**Part 17.** Quelle phrase est une bonne conclusion d'un essai sur le changement climatique ?", "En somme, agir tôt reste le meilleur moyen de limiter ses conséquences.", [("Voilà, j'ai fini.", "No content."), ("Le climat est un mot français.", "Irrelevant."), ("Voici un nouveau problème : la musique.", "A new idea.")],
      "A conclusion gives a final view that answers the problem.", DI1, "Application", "Which one answers the problem?"),
    K("**Part 18.** Dans une question avec un texte (« En vous inspirant du texte... »), il faut :", "utiliser le texte puis développer vos propres idées", [("ignorer le texte", "The text is a source."), ("recopier le texte entier", "Copying is not an essay."), ("traduire le texte", "Not the task.")],
      "Use the text as a starting point, then add ideas.", DI1, "Application", "What does « en vous inspirant du texte » ask?"),
    K("**Part 19.** Une pandémie se distingue d'une épidémie parce qu'elle :", "touche plusieurs continents ou le monde entier", [("dure toujours un mois", "Duration is not the difference."), ("est moins dangereuse", "Danger is not the difference."), ("ne touche que des animaux", "It affects humans.")],
      "Pandémie = worldwide spread.", T_DEBAT, "Concept", "Local or worldwide?"),
    K("**Part 20.** Que faire dans les dernières minutes d'une épreuve d'essai ?", "Relire pour corriger les accords, les temps et la ponctuation", [("Écrire un nouveau paragraphe sans relire", "Errors remain."), ("Effacer toute l'introduction", "Not useful."), ("Quitter la salle", "You lose marks.")],
      "Check agreement, tense and punctuation.", DI1, "Application", "What improves accuracy at the end?"),
]
assert len(P3) == 20, len(P3)
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="fru2-paper-3-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P3, 730)))
