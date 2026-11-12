"""Practice sets for A Level French (0745), Lower Sixth: La Dissertation de Culture Générale (4 sets), Panorama de la Littérature Française et
Francophone (5 sets) and Examination (3 exam-lesson sets), plus 'Paper 1 mock exam A' (50 multiple-choice questions across all four Lower
Sixth modules), 'Paper 2 practice paper A' (25 auto-markable parts on literature and essay method) and 'Paper 3 practice paper A'
(20 auto-markable parts: essay planning, translation and language items). Every French sentence, passage and poem is original and written
for these sets (the poem 'Le flamboyant' is invented). Literary facts are limited to well-established titles and dates; essays cannot be
auto-marked, so these sets test method, knowledge and language.
"""

import random

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
T_SUBJ = "Le subjonctif"
T_COND = "Le conditionnel"
T_REL = "Les pronoms relatifs composés"
T_NOM = "La nominalisation"
T_INV = "L'inversion stylistique"
T_STYL = "Stylistique comparée anglais-français"
T_TEMPS = "Traduire les temps et le passif"
T_IDIOM = "Traduire les expressions idiomatiques"
T_THEME = "Le thème"
T_VERS = "La version"

POEM = ("**Poème (original, écrit pour ces exercices)**\n\n"
        "LE FLAMBOYANT\n\n"
        "Le soir descend sur le village,\nEt l'arbre rouge brûle encore ;\nLes chants s'éteignent sous l'ombrage,\nLes braises rêvent de l'aurore.\n\n"
        "Demain la pluie viendra, mon frère,\nEt les pétales tomberont ;\nViens danser sur la terre claire,\nCueille la joie : les jours s'en vont.\n\n"
        "Je chanterai tant que la braise\nGardera un peu de chaleur ;\nEt quand la nuit sera mauvaise,\nTu garderas mon chant au cœur.")


def K(prompt, right, wrongs, step, concept, skill, hint, feedback="", passage=""):
    """Question spec: the right option first, then three (text, why) wrong options. Positions are assigned by build()."""
    assert len(wrongs) == 3, prompt
    assert len(concept) <= 80, concept
    assert all(w[1] for w in wrongs), prompt
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

# ================================================================== 1. Analyser le sujet
SET(M_DIS, T_SUJET, "Analyser le sujet : mots-clés, consignes, enjeu", "frl2-analyser-le-sujet", [
    K("What is the first step of a dissertation?", "Analyse the sujet: key words, consigne and enjeu", [
        ("Write the introduction at once", "You cannot introduce a sujet you have not analysed."),
        ("Recite everything you know about the topic", "This is a récitation de cours, a form of hors-sujet."),
        ("Write the conclusion first", "The conclusion answers the problématique, which comes after the analysis.")],
      "Understanding the sujet comes before everything else.", "Analyser le sujet", "Recall", "What must happen before you plan?"),
    K("In « Seule l'éducation sort un pays du sous-développement », which word is the limiting word that must be tested?", "seule", [
        ("éducation", "It is a key word but not the word that limits the claim."),
        ("pays", "It names who is concerned; it does not limit the claim."),
        ("sort", "It is the verb; the limiting word is the one that says « alone ».")],
      "« Seule » says education alone is enough. The essay has to test this.", "Analyser le sujet", "Concept", "Which word means « only » ?"),
    K("The sujet is « Les téléphones nuisent toujours à la concentration. » What does « toujours » force you to do?", "Test whether the rule has exceptions", [
        ("Ignore the word and write about phones in general", "Ignoring limiting words leads to hors-sujet."),
        ("Answer only « oui »", "A claim without exception is exactly what you must test."),
        ("Write about the history of telephones", "The sujet asks about concentration, not history.")],
      "An absolute word invites you to look for counter-examples and to nuance.", "Analyser le sujet", "Reasoning", "What does « always » ask you to check?"),
    K("A consigne begins with « Dans quelle mesure... ». What kind of answer is expected?", "A nuanced answer: partly true, under certain conditions", [
        ("Only « oui » or « non »", "The phrase asks for degree, not a one-word answer."),
        ("A definition of each key word only", "Definitions help but do not answer the question of degree."),
        ("A story about the topic", "A dissertation argues; it does not narrate.")],
      "Dans quelle mesure means up to what point.", "Analyser le sujet", "Concept", "Think of « to what extent ».", "A good answer shows where the claim is true and where it is not."),
    K("A sujet is about the measures against a pandémie. Which examples are best?", "Measures at world level: cooperation between countries, vaccines, border information", [
        ("Only a small outbreak in one neighbourhood", "That is a local épidémie, not a pandémie."),
        ("A list of old diseases in history", "History of diseases is not the question about measures."),
        ("Only the price of medicines in one shop", "It is too narrow for a global problem.")],
      "A pandémie spreads over several continents, so measures must be global too.", "Analyser le sujet", "Application", "Which word, épidémie or pandémie, sets the scale?"),
    K("A student answers « Le livre numérique peut-il remplacer le livre traditionnel ? » by narrating the history of printing. What is this?", "A hors-sujet (récitation de cours)", [
        ("A perfect plan", "It does not answer the question."),
        ("A problématique", "A problématique is a question, not a story."),
        ("A synthèse", "A synthèse is the third part of a dialectical plan.")],
      "The essay must answer the exact question, not a nearby topic.", "Analyser le sujet", "Concept", "Does the story answer « peut-il remplacer » ?"),
    K("Which of the following sujets is a situation?", "« Lors d'un débat dans votre lycée, vous donnez votre avis sur l'usage du téléphone en classe. »", [
        ("« Le téléphone est-il utile à l'école ? »", "It is a plain question."),
        ("« Seul le travail mène à la réussite. »", "It is an affirmation to discuss."),
        ("« Téléphone et école »", "It is a theme, not a complete sujet.")],
      "A situation gives a role and a context (debate, talk, report).", "Analyser le sujet", "Recall", "Which sujet gives you a role?"),
    K("What is the enjeu of « Les réseaux sociaux rapprochent-ils les gens ? »", "Easy contact against the quality of real relationships", [
        ("The date when social networks began", "That is a fact, not the stake of the debate."),
        ("The price of mobile data", "It is a different subject."),
        ("The rules of French spelling", "It is unrelated to the sujet.")],
      "The enjeu is the real debate behind the words.", "Analyser le sujet", "Reasoning", "What are the two sides of the debate?"),
], 301)

# ================================================================== 2. La problématique
SET(M_DIS, T_PROB, "La problématique : tension et question", "frl2-problematique", [
    K("What is a problématique?", "The central open question of the essay, born from a tension in the sujet", [
        ("A summary of the whole essay", "A summary comes in the conclusion."),
        ("The title of the essay", "A title is not a question to be answered."),
        ("A list of the arguments", "The arguments belong to the plan.")],
      "It is a question that the plan answers.", "La problématique", "Recall", "What does the plan answer?"),
    K("What is a tension in a sujet?", "Two ideas that both seem true but pull in different directions", [
        ("A spelling difficulty", "Tension is about ideas."),
        ("A long sentence", "Length is not tension."),
        ("A date in the sujet", "A date is a fact, not a tension.")],
      "Look for oppositions, paradoxes, limits or conditions.", "La problématique", "Concept", "Think of yes and no at once."),
    K("Which is the best problématique for « La télévision rend-elle les enfants moins cultivés ? »", "« Dans quelle mesure la télévision peut-elle enrichir ou appauvrir la culture des enfants ? »", [
        ("« Qu'est-ce que la télévision ? »", "It is a definition question without tension."),
        ("« La télévision est mauvaise. »", "It is an opinion, not an open question."),
        ("« Les enfants regardent-ils la télévision ? »", "It is a factual question that needs only yes or no.")],
      "A problématique is open and uses both sides of the sujet.", "La problématique", "Application", "Which question contains both enrichir and appauvrir?"),
    K("Which formula suits a strong claim such as « Seule l'éducation sort un pays du sous-développement » ?", "« Dans quelle mesure... ? »", [
        ("« Quelle est la date de... ? »", "It asks for a fact."),
        ("« Qui a écrit... ? »", "It asks for an author."),
        ("« Combien de... ? »", "It asks for a number.")],
      "Dans quelle mesure tests how far the claim is true.", "La problématique", "Application", "Which formula asks how far ?"),
    K("« Le numérique est-il bon ? » is a weak problématique because it is...", "closed and vague, without tension", [
        ("too long", "It is short."),
        ("a perfect problématique", "It lacks tension and precision."),
        ("a conclusion", "It is a question, not a conclusion.")],
      "Good means open, precise and tied to the sujet.", "La problématique", "Reasoning", "Can it be answered in one word ?"),
    K("How should the plan relate to the problématique?", "The plan answers the problématique", [
        ("The plan is unrelated to it", "A plan that ignores the problématique breaks the essay."),
        ("The plan repeats the sujet", "It must answer, not repeat."),
        ("The plan comes before it", "The problématique is built first.")],
      "The problématique is the engine; the plan is the path.", "La problématique", "Concept", "What does the plan do to the question ?"),
    K("How many questions should a problématique contain?", "One main question, with at most one or two linked sub-questions", [
        ("Five or six questions", "A long list hides the argument."),
        ("No question at all", "A problématique is a question."),
        ("A different question for each part", "Each part answers the same central question.")],
      "Keep it short and clear.", "La problématique", "Recall", "Short and clear."),
    K("What is the tension in « Faut-il interdire le téléphone à l'école ? »", "A tool for learning and information against distraction and inequality", [
        ("The colour of the phone", "It has nothing to do with the debate."),
        ("The weight of the school bag", "It is unrelated to the debate."),
        ("The age of the teacher", "It is unrelated to the debate.")],
      "Both sides must be real arguments.", "La problématique", "Reasoning", "Why yes? Why no?"),
], 302)

# ================================================================== 3. Plans
SET(M_DIS, T_PLANS, "Plans dialectique et thématique", "frl2-plans", [
    K("What is the order of the dialectical plan?", "Thèse, antithèse, synthèse", [
        ("Synthèse, thèse, antithèse", "The synthèse comes last, after both sides."),
        ("Antithèse, antithèse, thèse", "There is one of each."),
        ("Introduction, thèse, thèse", "The plan has three different movements.")],
      "Affirm, challenge, go beyond.", "Plans dialectique et thématique", "Recall", "Which part goes beyond the two others ?"),
    K("What is a good synthèse?", "A reasoned answer with conditions and nuances that goes beyond thèse and antithèse", [
        ("A repetition of the thèse", "It adds nothing."),
        ("A vague sentence saying both sides are good", "A weak compromise answers nothing."),
        ("A new unrelated subject", "It must answer the problématique.")],
      "It says when, for whom and under what condition.", "Plans dialectique et thématique", "Concept", "Think of a defendable answer."),
    K("Which sujet needs a thematic plan?", "« Quelles mesures prendre contre la famine ? »", [
        ("« Le livre numérique peut-il remplacer le livre ? »", "It has a clear yes-or-no tension, which suits a dialectical plan."),
        ("« Seule l'éducation fait le développement. »", "It is an affirmation to discuss, suited to a dialectical plan."),
        ("« Le téléphone rend-il plus libre ? »", "It has a yes-or-no tension.")],
      "« What to do » questions suit fields: politique, économique, social.", "Plans dialectique et thématique", "Application", "Which sujet asks what to do ?"),
    K("In a debate, where you must be for or against, what should you do?", "Take a clear side and still answer the best opposing argument", [
        ("Avoid taking a side", "A debate requires a position."),
        ("Ignore the opposing arguments", "A strong speaker answers the best objection."),
        ("Write only a definition", "A definition is not an argument.")],
      "Commit, then refute.", "Plans dialectique et thématique", "Application", "What does a debater do with the other side ?"),
    K("Every argument in a part should contain...", "an idea, an explanation and an example", [
        ("only an opinion", "An opinion without proof is weak."),
        ("only a story", "An example without an argument is only a story."),
        ("only a quotation", "A quotation without comment proves nothing.")],
      "Idea, explanation, example.", "Plans dialectique et thématique", "Recall", "What proves an idea ?"),
    K("What is wrong with an essay with a very long thèse, a short antithèse and a one-line synthèse?", "The parts are unbalanced and the essay looks one-sided", [
        ("Nothing, it is ideal", "Balance matters."),
        ("It is too balanced", "It is not balanced."),
        ("It has no synthèse", "It has one, but it is too short.")],
      "Give each part similar weight; the synthèse should be refined.", "Plans dialectique et thématique", "Reasoning", "Compare the sizes of the parts."),
    K("What is the role of a transition?", "To close the previous part and announce the next", [
        ("To repeat the introduction", "It does not repeat it."),
        ("To end the essay", "That is the conclusion."),
        ("To add a new example", "Examples belong inside the arguments.")],
      "It links the parts of the plan.", "Plans dialectique et thématique", "Concept", "Think of a bridge."),
    K("Which thematic plan fits « Les conséquences du changement climatique » ?", "Conséquences environnementales, économiques, sociales", [
        ("Thèse, antithèse, synthèse", "There is no yes-or-no tension in the sujet."),
        ("Biographie, bibliographie, index", "These are not parts of an essay."),
        ("Passé, présent, passé", "The idea of time is repeated and does not answer the question.")],
      "Group by fields of consequence.", "Plans dialectique et thématique", "Application", "Which fields suffer ?"),
], 303)

# ================================================================== 4. Rédiger
SET(M_DIS, T_REDIG, "Rédiger : introduction, développement, conclusion", "frl2-rediger", [
    K("What is the order of the four moves of the introduction?", "Amorce, présentation du sujet, problématique, annonce du plan", [
        ("Problématique, amorce, plan, sujet", "The amorce comes first; the problématique comes after the sujet."),
        ("Plan, conclusion, amorce, sujet", "The conclusion is not part of the introduction."),
        ("Sujet, plan, amorce, problématique", "The amorce comes first and the plan last.")],
      "Hook, topic, question, path.", "Rédiger la dissertation", "Recall", "What do you start with ?"),
    K("What are the two moves of a conclusion?", "Bilan and ouverture", [
        ("Amorce and annonce", "These belong to the introduction."),
        ("A new argument and a new plan", "A conclusion does not add arguments."),
        ("Thèse and antithèse", "These are parts of the plan.")],
      "Answer the problématique, then widen.", "Rédiger la dissertation", "Recall", "Think of an answer and a wider view."),
    K("Which is the best amorce for an essay on the digital book?", "« Depuis quelques années, il n'est plus rare de voir un élève lire un roman sur son téléphone. »", [
        ("« De tout temps, l'homme a lu des livres. »", "It is too general and leads nowhere."),
        ("« Ma tablette est neuve. »", "It is a personal remark, not an introduction to the sujet."),
        ("« Voici mon plan. »", "The plan comes at the end of the introduction.")],
      "A good amorce is precise and leads to the sujet.", "Rédiger la dissertation", "Application", "Which one is specific and connected ?"),
    K("Complete: « Il n'y a pas d'électricité ; ___, les tablettes sont inutilisables. »", "par conséquent", [
        ("de plus", "It adds a point; it does not show a consequence."),
        ("pourtant", "It shows opposition."),
        ("car", "It shows cause and would reverse the logic.")],
      "The second fact is the result of the first.", "Rédiger la dissertation", "Application", "Is it a result, an addition or an opposition ?"),
    K("The French word « actuellement » means...", "currently", [
        ("actually", "That is a faux ami; « actually » is en fait."),
        ("in the past", "It refers to the present."),
        ("eventually", "« Eventually » is finalement.")],
      "Learn faux amis in pairs.", "Rédiger la dissertation", "Recall", "Is it present or contrast ?"),
    K("Which sentence is correct?", "Une pandémie touche plusieurs continents.", [
        ("Une épidémie touche plusieurs continents.", "An épidémie is regional; the word needed is pandémie."),
        ("Une pandémie touche un seul village.", "A single village is a local outbreak."),
        ("Une pandémie est une chanson.", "It is meaningless.")],
      "Scale decides the word.", "Rédiger la dissertation", "Concept", "Which word means worldwide ?"),
    K("A paragraph has an idée directrice, an explication, an exemple and...", "a mini-bilan", [
        ("a second introduction", "The introduction is only at the start."),
        ("a new problématique", "There is one problématique."),
        ("an index", "An index is not part of an essay.")],
      "Close each paragraph by linking to the question.", "Rédiger la dissertation", "Recall", "What closes a paragraph ?"),
    K("Which of these does NOT belong in a conclusion?", "A new argument not developed in the essay", [
        ("A bilan answering the problématique", "It belongs there."),
        ("An ouverture to a wider question", "It belongs there."),
        ("A final nuance", "It belongs there if it answers the question.")],
      "A new argument belongs in the développement.", "Rédiger la dissertation", "Reasoning", "What is the conclusion for ?"),
], 304)

# ================================================================== 5. Le classicisme
SET(M_PAN, T_CLASS, "Le classicisme : règles et grands auteurs", "frl2-classicisme", [
    K("Which are the three classical unités?", "Action, lieu, temps", [
        ("Action, style, personnage", "Style and personnage are not unités."),
        ("Lieu, rime, temps", "Rime is not an unité."),
        ("Temps, genre, titre", "Genre and titre are not unités.")],
      "One action, one place, about one day.", "Le classicisme", "Recall", "Think of a play on one stage in one day."),
    K("What does bienséance require?", "Nothing shocking on stage: violence is reported, not shown", [
        ("Violence shown in full on stage", "That is the opposite."),
        ("Mixing tragedy and comedy", "Classicism separates the genres."),
        ("A play lasting several years", "The unité de temps asks for about a day.")],
      "Propriety on stage.", "Le classicisme", "Concept", "What may the audience not see ?"),
    K("Who wrote L'Art poétique (1674), which gave the rules of classical poetry their classic form?", "Boileau", [
        ("Molière", "Molière wrote comedies."),
        ("Racine", "Racine wrote tragedies."),
        ("La Fontaine", "La Fontaine wrote fables.")],
      "Boileau is the theorist of classicism.", "Le classicisme", "Recall", "Which writer was a theorist ?"),
    K("What is an alexandrin?", "A line of twelve syllables, usually with a césure in the middle", [
        ("A line of eight syllables", "That is an octosyllabe."),
        ("A line of ten syllables", "That is a décasyllabe."),
        ("A line without rhyme or rhythm", "The alexandrin has a strict rhythm.")],
      "Twelve syllables, six plus six.", "Le classicisme", "Recall", "How many syllables ?"),
    K("A « héros cornélien » is a character who...", "faces a choice between duty and passion", [
        ("only laughs at others", "That is a comic character."),
        ("never makes choices", "Corneille's heroes choose."),
        ("is destroyed without any struggle", "That is closer to Racine's fatal passion, and even there the struggle matters.")],
      "Corneille is the poet of the dilemma.", "Le classicisme", "Concept", "Think of Le Cid."),
    K("Racine's tragic characters are often...", "overcome by a fatal passion", [
        ("masters of every feeling", "Racine's heroes lose control."),
        ("comic servants", "That describes comedy."),
        ("free from any destiny", "Fate and passion weigh on them.")],
      "Phèdre is the classic example.", "Le classicisme", "Concept", "Think of Phèdre."),
    K("Which sentence best describes Molière's idea of comedy?", "To correct customs through laughter by showing vices such as hypocrisy and greed", [
        ("To make the audience cry", "That belongs to tragedy."),
        ("To avoid social criticism", "Molière's comedy criticises society."),
        ("To tell the history of kings", "That is not the aim of his comedy.")],
      "Comedy corrects by laughter.", "Le classicisme", "Concept", "What does laughter do here ?"),
    K("La Fontaine is known for...", "Fables in verse with a morale", [
        ("Tragedies in alexandrins", "Those are Corneille's and Racine's."),
        ("Realist novels", "The realist novel is a 19th-century genre."),
        ("Philosophical dictionaries", "That is closer to the Encyclopédie of the 18th century.")],
      "Animals, short stories, a lesson.", "Le classicisme", "Recall", "Which genre has a morale ?"),
], 305)

# ================================================================== 6. Lumières
SET(M_PAN, T_LUM, "Le siècle des Lumières : idées et genres", "frl2-lumieres", [
    K("Who wrote Du contrat social (1762)?", "Rousseau", [
        ("Voltaire", "Voltaire wrote Candide and the Traité sur la tolérance."),
        ("Montesquieu", "Montesquieu wrote De l'esprit des lois."),
        ("Molière", "Molière lived in the 17th century and wrote comedies.")],
      "Rousseau and the social contract.", "Le siècle des Lumières", "Recall", "Think of the general will."),
    K("Which philosophe developed the idea of the separation of powers?", "Montesquieu", [
        ("Diderot", "Diderot directed the Encyclopédie."),
        ("Rousseau", "Rousseau wrote on the social contract."),
        ("Beaumarchais", "Beaumarchais was a dramatist.")],
      "De l'esprit des lois (1748).", "Le siècle des Lumières", "Recall", "Législatif, exécutif, judiciaire."),
    K("The Encyclopédie was directed by...", "Diderot (with d'Alembert)", [
        ("Racine", "Racine was a classical tragedian."),
        ("Hugo", "Hugo is a romantic writer."),
        ("Zola", "Zola is a naturalist.")],
      "A huge dictionary of knowledge, 1751 to 1772.", "Le siècle des Lumières", "Recall", "Which philosophe worked with d'Alembert ?"),
    K("Candide (1759) is an example of...", "a conte philosophique", [
        ("a classical tragedy", "Candide is a tale, not a tragedy."),
        ("a realist novel of the 19th century", "It belongs to the 18th century."),
        ("a lyric poem", "It is in prose.")],
      "A short tale that carries an idea.", "Le siècle des Lumières", "Concept", "Voltaire used tales."),
    K("Why did the philosophes often use argumentation indirecte?", "Censorship made direct criticism dangerous, and stories persuade by themselves", [
        ("They did not know how to write essays", "They wrote many essays."),
        ("Because indirect argument is shorter", "Length was not the reason."),
        ("Because the Revolution had already happened", "The Revolution came in 1789, after most of these works.")],
      "Hide the thesis in a tale or a letter.", "Le siècle des Lumières", "Reasoning", "What risk did they face ?"),
    K("What is the effect of ironie in a work of the Lumières?", "It says the opposite of what is meant, so the reader sees the criticism", [
        ("It states the criticism openly", "That is direct argument."),
        ("It tells the exact truth", "Irony says the opposite."),
        ("It describes the author's family", "It has nothing to do with biography.")],
      "The reader becomes an ally of the author.", "Le siècle des Lumières", "Concept", "Think of saying the opposite."),
    K("In Lettres persanes (1721), what is the effect of Persian travellers describing France?", "Familiar customs seem strange, which invites criticism", [
        ("It makes the customs more normal", "The foreign eye makes them look strange."),
        ("It proves that France is perfect", "The aim is critical."),
        ("It avoids all criticism", "It allows criticism indirectly.")],
      "Regard éloigné: a foreigner's view.", "Le siècle des Lumières", "Application", "How does a stranger see our customs ?"),
    K("Which century is « le siècle des Lumières » ?", "The 18th century", [
        ("The 17th century", "That is the classical century."),
        ("The 19th century", "That is romanticism and realism."),
        ("The 20th century", "That is the century of négritude and the post-independence novel.")],
      "1715 to 1789 roughly.", "Le siècle des Lumières", "Recall", "Between Louis XIV and the Revolution."),
], 306)

# ================================================================== 7. Romantisme
SET(M_PAN, T_ROM, "Le romantisme : le moi, la nature, la liberté", "frl2-romantisme", [
    K("What is the mal du siècle?", "The sadness and disillusion of the young generation of the early 19th century", [
        ("A disease of the lungs", "It is a state of mind, not an illness."),
        ("A rule of classical drama", "Classical rules are different."),
        ("A kind of rhyme", "It is not a rhyme.")],
      "Solitude and melancholy after great upheavals.", "Le romantisme", "Concept", "Think of René."),
    K("Which text is the manifesto of the romantic theatre?", "Hugo's preface to Cromwell (1827)", [
        ("Boileau's L'Art poétique", "That is the classical text."),
        ("Zola's Le Roman expérimental", "That is a naturalist text."),
        ("Voltaire's Candide", "That is an 18th-century tale.")],
      "Hugo defends the mélange des genres.", "Le romantisme", "Recall", "Which preface attacked the rules ?"),
    K("Lamartine's Méditations poétiques (1820) is an example of...", "romantic lyric poetry", [
        ("a naturalist novel", "It is poetry from the first half of the century."),
        ("a classical tragedy", "It is poetry, not tragedy."),
        ("a comedy of manners", "It is not a comedy.")],
      "Personal feelings in verse.", "Le romantisme", "Recall", "Which genre expresses the moi ?"),
    K("What is lyrisme?", "Expression of personal feelings, often in the first person", [
        ("A precise description of society", "That is realism."),
        ("A neutral report of facts", "Lyricism is personal."),
        ("A lesson without emotion", "Lyricism expresses emotion.")],
      "Joy, love, grief: the moi speaks.", "Le romantisme", "Concept", "Who speaks ?"),
    K("An enjambement is...", "a sentence that runs from one line of verse to the next", [
        ("a rhyme at the end of each line", "That is rime."),
        ("a pause after six syllables", "That is the césure."),
        ("the repetition of a word at the start of lines", "That is anaphore.")],
      "The sense overflows the line.", "Le romantisme", "Concept", "Does the sentence end with the line ?"),
    K("In « Ô soir, tu viens poser ta main sur mon cœur », the words « Ô soir » are...", "an apostrophe", [
        ("an anaphore", "There is no repetition."),
        ("a litote", "There is no understatement."),
        ("a comparaison", "There is no comme.")],
      "The speaker addresses the evening.", "Le romantisme", "Application", "Who is being addressed ?"),
    K("« La nature miroir de l'âme » means that...", "the landscape reflects the poet's feelings", [
        ("nature is described as a mirror in a shop", "It is figurative."),
        ("the poet ignores nature", "Nature is central."),
        ("the poet describes a map", "It is not about maps.")],
      "The setting matches the mood.", "Le romantisme", "Concept", "What does the landscape show ?"),
    K("Baudelaire's Les Fleurs du mal appeared in...", "1857", [
        ("1657", "That is classical times."),
        ("1757", "That is the 18th century."),
        ("1957", "That is the 20th century.")],
      "The same year as Madame Bovary.", "Le romantisme", "Recall", "Mid 19th century."),
], 307)

# ================================================================== 8. Réalisme et naturalisme
SET(M_PAN, T_REAL, "Le réalisme et le naturalisme", "frl2-realisme-naturalisme", [
    K("Who wrote Les Rougon-Macquart?", "Zola", [
        ("Balzac", "Balzac wrote La Comédie humaine."),
        ("Flaubert", "Flaubert wrote Madame Bovary."),
        ("Stendhal", "Stendhal wrote Le Rouge et le Noir.")],
      "Twenty novels about one family.", "Le réalisme et le naturalisme", "Recall", "Which author is the naturalist leader ?"),
    K("Madame Bovary (1857) is by...", "Flaubert", [
        ("Zola", "Zola wrote Germinal."),
        ("Maupassant", "Maupassant wrote Bel-Ami."),
        ("Hugo", "Hugo wrote Les Misérables.")],
      "Flaubert's famous provincial novel.", "Le réalisme et le naturalisme", "Recall", "A woman and her disappointed dreams."),
    K("What distinguishes naturalism from realism?", "Naturalism uses a scientific approach and determinism: heredity and milieu", [
        ("It rejects all observation", "Naturalism observes closely."),
        ("It is a form of classical tragedy", "It is a novelistic movement."),
        ("It only describes dreams", "Naturalism describes real life.")],
      "Zola compared the novelist to an experimenter.", "Le réalisme et le naturalisme", "Concept", "What does the scientist add ?"),
    K("What is « focalisation interne » ?", "The story is told through what one character perceives and thinks", [
        ("The narrator knows everything", "That is omniscient (zero) focalisation."),
        ("The narrator describes only what can be seen from outside", "That is external focalisation."),
        ("The story is told only in dialogue", "That is not focalisation.")],
      "We are inside the character.", "Le réalisme et le naturalisme", "Concept", "Whose mind do we enter ?"),
    K("Which of these is an example of style indirect libre?", "« Elle fermait son cahier. Qu'importait, après tout, cette note ? »", [
        ("« Elle dit : je ferme mon cahier. »", "That is direct speech."),
        ("« Elle dit qu'elle fermait son cahier. »", "That is ordinary indirect speech."),
        ("« Fermez vos cahiers ! »", "That is a command.")],
      "Thoughts without quotation marks or introducing verb.", "Le réalisme et le naturalisme", "Application", "Which sentence has no verb like dit ?"),
    K("What are the two roles of a description in a realist novel?", "It creates the illusion of reality and it reveals meaning about characters or society", [
        ("It only fills space", "A description has functions."),
        ("It only advertises products", "It is not advertising."),
        ("It only copies reality exactly", "It is a selection and an organisation of details.")],
      "Credibility and meaning.", "Le réalisme et le naturalisme", "Concept", "Why describe a room ?"),
    K("La Comédie humaine is the cycle of novels by...", "Balzac", [
        ("Zola", "Zola's series is Les Rougon-Macquart."),
        ("Maupassant", "Maupassant is known for short stories."),
        ("Flaubert", "Flaubert wrote a few novels, not a cycle.")],
      "Returning characters across many novels.", "Le réalisme et le naturalisme", "Recall", "Eugénie Grandet, Le Père Goriot."),
    K("Why should you not say « realism copies reality exactly » ?", "The author selects and organises details to create an illusion of reality", [
        ("Because realists never describe anything", "Realists describe a lot."),
        ("Because novels are always poems", "Novels are prose."),
        ("Because realism does not exist", "It is a real movement.")],
      "It creates the illusion of reality.", "Le réalisme et le naturalisme", "Reasoning", "Does the author choose the details ?"),
], 308)

# ================================================================== 9. Négritude
SET(M_PAN, T_NEG, "La négritude et la littérature post-indépendance", "frl2-negritude-post-independance", [
    K("Who are the three main founders of négritude?", "Césaire, Senghor and Damas", [
        ("Oyono, Beti and Bebey", "They are Cameroonian novelists of a later period."),
        ("Kourouma, Kane and Laye", "They are novelists."),
        ("Baudelaire, Hugo and Zola", "They are French writers of the 19th century.")],
      "Martinique, Senegal, Guyane.", "La négritude et la littérature post-indépendance", "Recall", "Think of L'Étudiant noir."),
    K("The Cahier d'un retour au pays natal is a poem by...", "Aimé Césaire", [
        ("Léopold Sédar Senghor", "Senghor wrote Chants d'ombre and Éthiopiques."),
        ("Ferdinand Oyono", "Oyono wrote Une vie de boy."),
        ("Camara Laye", "Laye wrote L'Enfant noir.")],
      "Césaire's major poem.", "La négritude et la littérature post-indépendance", "Recall", "Which poet is from Martinique ?"),
    K("Which review founded in 1947 by Alioune Diop became a forum for Black writers?", "Présence africaine", [
        ("L'Encyclopédie", "That is an 18th-century work."),
        ("Le Figaro", "It is a newspaper, not the Black writers' forum."),
        ("La Gazette de Hugo", "It does not exist.")],
      "A review and later a publishing house.", "La négritude et la littérature post-indépendance", "Recall", "Which name includes Africa ?"),
    K("Une vie de boy (1956) by Ferdinand Oyono is mainly...", "a satire of colonial society", [
        ("a classical tragedy", "It is a modern novel."),
        ("a romantic ode to nature", "It criticises colonial life."),
        ("a treatise on the separation of powers", "That is Montesquieu.")],
      "Irony and observation.", "La négritude et la littérature post-indépendance", "Concept", "Think of the servant's diary."),
    K("Les Soleils des indépendances (1968) by Ahmadou Kourouma is typical of...", "disillusion after independence", [
        ("the praise of colonial rule", "It does not praise colonial rule."),
        ("the classical rules", "It is a modern novel."),
        ("the Parnasse school", "It is not French poetry of that school.")],
      "Writers criticise their own societies.", "La négritude et la littérature post-indépendance", "Concept", "What happens to the hope of independence ?"),
    K("Which is a main theme of post-independence literature?", "Tension between tradition and modernity, corruption and family authority", [
        ("The unity of place of classical theatre", "That is a classical rule."),
        ("The ideal of the royal court", "That is classical."),
        ("The invention of the printing press", "That is a historical fact, not a literary theme of this movement.")],
      "African societies after independence.", "La négritude et la littérature post-indépendance", "Concept", "Think of Kane, Kourouma, Bebey."),
    K("Léopold Sédar Senghor was also...", "the first president of Senegal", [
        ("a classical dramatist", "He was a poet of the 20th century."),
        ("a naturalist novelist", "He was a poet."),
        ("the founder of the Académie française", "It was founded in 1635.")],
      "Poet and statesman.", "La négritude et la littérature post-indépendance", "Recall", "He governed from 1960."),
    K("Le Fils d'Agatha Moudio (1967) is by...", "Francis Bebey, a Cameroonian writer", [
        ("Mongo Beti", "Beti wrote Le Pauvre Christ de Bomba."),
        ("Aimé Césaire", "Césaire is a Martinican poet."),
        ("Voltaire", "Voltaire is an 18th-century writer.")],
      "A gentle, humorous novel about tradition and love.", "La négritude et la littérature post-indépendance", "Recall", "Cameroonian novel of the 1960s."),
], 309)

# ================================================================== 10. Paper 1 strategy
SET(M_EXAM, "Paper 1", "Paper 1 : méthode pour les choix multiples", "frl2-paper-1-strategy", [
    K("According to the Board's 2023 report, how many questions does Paper 1 have?", "50 multiple-choice questions", [
        ("20 essay questions", "Paper 1 is multiple choice."),
        ("5 translation texts", "Translation is in Paper 3."),
        ("10 poems to analyse", "Poem analysis is in Paper 2.")],
      "Paper 1 is the MCQ.", "Paper 1", "Recall", "Look at the paper structure."),
    K("Which is the right four-step method?", "Read, decide what is tested, predict, test and eliminate", [
        ("Guess, guess, guess, guess", "Guessing wastes marks."),
        ("Choose the longest option", "Length does not decide."),
        ("Read only the options", "The stem gives the question.")],
      "A fixed method prevents impulse errors.", "Paper 1", "Concept", "What do you do before choosing ?"),
    K("A question asks: « Quelle phrase est INCORRECTE ? » What do you look for?", "The one sentence with an error", [
        ("The sentence with the best style", "It asks for an error."),
        ("The shortest sentence", "Length is irrelevant."),
        ("The only correct sentence", "Three are correct; the question asks for the wrong one.")],
      "Underline the keyword INCORRECTE.", "Paper 1", "Application", "What does the capital word change ?"),
    K("« Il pleure comme une fontaine. » is a...", "comparaison", [
        ("métaphore", "A métaphore has no tool word."),
        ("litote", "There is no understatement."),
        ("antithèse", "There are no opposites.")],
      "There is the tool word comme.", "Paper 1", "Application", "Look for comme."),
    K("« Un silence assourdissant » is a...", "oxymore", [
        ("comparaison", "There is no tool word."),
        ("anaphore", "There is no repetition."),
        ("personnification", "No human trait is given to a thing.")],
      "Two contradictory words are joined.", "Paper 1", "Application", "Silence and deafening contradict each other."),
    K("The mock gives 90 minutes for 50 questions. About how long per question?", "About 1.8 minutes", [
        ("About 5 minutes", "That would take 250 minutes."),
        ("About 10 seconds", "That is far too short."),
        ("About 30 minutes", "That is far too long.")],
      "90 divided by 50.", "Paper 1", "Calculation", "Divide the time by the number of questions."),
    K("Which is a faux ami trap?", "« assister à » means to attend, not to help", [
        ("« aider » means to help", "That is correct and not a trap."),
        ("« livre » means book", "That is correct."),
        ("« école » means school", "That is correct.")],
      "Learn faux amis in pairs.", "Paper 1", "Concept", "Which word looks like an English one ?"),
    K("What is the difference between a litote and an euphémisme?", "A litote says less to suggest more; an euphémisme softens a harsh idea", [
        ("They are exactly the same", "They differ in purpose."),
        ("A litote exaggerates, an euphémisme understates", "A litote understates to suggest more; exaggeration is hyperbole."),
        ("A litote is a rhyme", "It is a figure of speech.")],
      "Suggest more against soften.", "Paper 1", "Concept", "Compare « ce n'est pas bête » and « il nous a quittés ».", "Learn each pair together."),
], 310)

# ================================================================== 11. Paper 2 strategy
SET(M_EXAM, "Paper 2", "Paper 2 : la littérature et l'analyse de texte", "frl2-paper-2-strategy", [
    K("According to the Board's report, what is a common weakness in Paper 2?", "General answers without facts from the text", [
        ("Using too many examples from the text", "The report says candidates failed to use the text."),
        ("Writing too short an introduction", "That is not the weakness named."),
        ("Writing in capital letters", "That is not mentioned.")],
      "Evidence from the text is vital.", "Paper 2", "Recall", "What proves a point ?"),
    K("In the unseen poem « Le flamboyant », how many syllables does each line have?", "8", [
        ("12", "That is the alexandrin."),
        ("10", "That is the décasyllabe."),
        ("6", "That is half an alexandrin.")],
      "Count: Le soir descend sur le village (8).", "Paper 2", "Calculation", "Count each sounded syllable; the final mute e is not counted.", passage=POEM),
    K("What is the rhyme scheme of each strophe of the poem?", "ABAB (rimes croisées)", [
        ("AABB (rimes plates)", "Lines 1 and 3 rhyme and lines 2 and 4 rhyme."),
        ("ABBA (rimes embrassées)", "Line 1 does not rhyme with line 4."),
        ("There is no rhyme", "Each strophe rhymes.")],
      "Village / ombrage; encore / aurore.", "Paper 2", "Analyse", "Which lines rhyme in strophe 1 ?", passage=POEM),
    K("What is the role of the future tense in the second strophe?", "It announces a coming loss and supports the advice to enjoy the present", [
        ("It tells a past memory", "The future cannot tell the past."),
        ("It describes the present scene", "The present tense does that in strophe 1."),
        ("It has no role", "Tenses carry meaning.")],
      "Viendra, tomberont: loss to come.", "Paper 2", "Analyse", "What do viendra and tomberont predict ?", passage=POEM),
    K("Which lexical field dominates the poem?", "Fire and light against night and ending", [
        ("War and weapons", "There is no war vocabulary."),
        ("Money and trade", "There is no commerce vocabulary."),
        ("School and exams", "There is no school vocabulary.")],
      "Brûle, braise, aurore, chaleur; nuit, s'éteignent.", "Paper 2", "Analyse", "Underline the words that belong together.", passage=POEM),
    K("What advice does the poem give?", "To enjoy life now because time passes", [
        ("To avoid all joy", "The poem says the opposite."),
        ("To wait for tomorrow", "Tomorrow brings the rain."),
        ("To forget the village", "The village is the setting of the poem.")],
      "« Cueille la joie » is the advice.", "Paper 2", "Interpretation", "Look at the imperative verbs.", passage=POEM),
    K("To show that a technique is effective, which sequence is best?", "Define it, give an example, explain the effect, evaluate", [
        ("Name it only", "Naming it is not enough."),
        ("Retell the story", "Retelling the story shows nothing."),
        ("Give three technical words", "Listing is not analysis.")],
      "The report says candidates listed techniques without showing effects.", "Paper 2", "Application", "What is missing in a list ?"),
    K("In a question on « parents », what does the Board's report say about the word?", "It can include elders and the wider family, not only father and mother", [
        ("It only means mother", "The report says it is wider."),
        ("It only means father", "The report says it is wider."),
        ("It never includes elders", "The report says it includes elders.")],
      "Define the key words of the question.", "Paper 2", "Interpretation", "Whose authority counts in a village ?"),
], 311)

# ================================================================== 12. Paper 3 strategy
SET(M_EXAM, "Paper 3", "Paper 3 : expression écrite et traduction", "frl2-paper-3-strategy", [
    K("According to the Board's 2023 report, what must a candidate do in the essay part of Paper 3?", "Choose one of four life situations and write on it", [
        ("Answer all four situations", "Only one is chosen."),
        ("Write a poem", "The essay part is about life situations."),
        ("Answer only multiple-choice questions", "That is Paper 1.")],
      "Four situations, one essay.", "Paper 3", "Recall", "Read the structure of the paper."),
    K("In a debate situation, what should the first paragraph do?", "State a clear position, say why the question matters and announce the arguments", [
        ("Tell the history of the world", "Too general."),
        ("Say nothing about your opinion", "A debate needs a position."),
        ("Copy the question word for word and stop", "That does not start the argument.")],
      "Commit, justify, announce.", "Paper 3", "Application", "What does a debater say first ?"),
    K("Why should you choose the essay topic by vocabulary?", "Language, more than understanding, was the main difficulty on several topics", [
        ("Because easy topics have no vocabulary", "Every topic needs words."),
        ("Because vocabulary is not marked", "Language accuracy matters."),
        ("Because topics are chosen by the examiner", "The candidate chooses.")],
      "The report says candidates lacked the words.", "Paper 3", "Reasoning", "Which topic can you write about accurately ?"),
    K("How do you translate « Cela fait deux ans que j'habite ici » into English?", "I have been living here for two years.", [
        ("It makes two years that I live here.", "That is a word-for-word calque."),
        ("I lived here two years.", "It suggests that the stay has ended."),
        ("It does two years I live here.", "That is a word-for-word calque.")],
      "Present with « cela fait... que » = present perfect continuous.", "Paper 3", "Application", "The action continues now."),
    K("What is « Il y a trois jours » in English?", "Three days ago", [
        ("It has three days", "That is a literal calque."),
        ("There are three days", "It changes the meaning."),
        ("Three days from now", "It points to the future.")],
      "Il y a + time = ago.", "Paper 3", "Application", "Is it past or future ?"),
    K("Which sentence uses the correct word for a disease affecting several continents?", "Une pandémie a touché plusieurs continents.", [
        ("Une épidémie mondiale touche un seul village.", "It contradicts itself."),
        ("Une pandémie est une chanson.", "It is meaningless."),
        ("Une épidémie touche toujours plusieurs continents.", "Épidémie is regional.")],
      "Pandémie is worldwide.", "Paper 3", "Concept", "Which word is global ?"),
    K("What is the best first step in a translation?", "Read the whole text and then cut it into units of meaning", [
        ("Translate word by word from the first line", "A literal approach often gives wrong sentences."),
        ("Use the first dictionary meaning for each word", "Words have several meanings."),
        ("Skip hard words", "A translation must be complete.")],
      "Understand first, translate units of meaning.", "Paper 3", "Concept", "Which step comes first ?"),
    K("Why must you proofread an essay?", "To correct agreements, verb forms, accents and connectors", [
        ("To make it longer", "Length is not the aim."),
        ("To change your opinion", "Proofreading is about language accuracy."),
        ("To add new arguments at the last minute", "It is not for adding.")],
      "Accuracy of language is marked.", "Paper 3", "Application", "What errors remain at the end ?"),
], 312)

# ================================================================== Paper 1 mock exam A (50 questions)
def Q(prompt, right, wrongs, step, concept, hint="Name the rule or idea being tested first.", skill="Application", passage=""):
    return K(prompt, right, wrongs, step, concept, skill, hint, passage=passage)


P1 = [
    # --- Le subjonctif (3)
    Q("« Il faut que tu ___ ton travail avant midi. » (finir)", "finisses", [
        ("finis", "« Il faut que » requires the subjunctive; « finis » is indicative."),
        ("finiras", "The future is not used after « il faut que »."),
        ("finirais", "The conditional is not used after « il faut que ».")],
      "Il faut que + subjunctive: que tu finisses.", T_SUBJ),
    Q("« Je suis content que vous ___ venus. »", "soyez", [
        ("êtes", "Verbs of emotion + que take the subjunctive; « êtes » is indicative."),
        ("serez", "The future is not used here."),
        ("seriez", "The conditional is not used here.")],
      "Emotion + que + subjonctif passé: que vous soyez venus.", T_SUBJ),
    Q("« Je ne pense pas qu'il ___ raison. »", "ait", [
        ("a", "After a negated « penser », standard French uses the subjunctive."),
        ("avait", "The imperfect is not used after a negated « penser »."),
        ("aura", "The future is not used here.")],
      "Ne pas penser que + subjonctif: qu'il ait.", T_SUBJ),
    # --- Le conditionnel (3)
    Q("« Si j'avais assez d'argent, je ___ un vélo. »", "m'achèterais", [
        ("m'achèterai", "The future does not follow « si + imparfait »."),
        ("m'achetais", "« Si » clause and main clause cannot both be imperfect here."),
        ("m'achète", "The present does not express the hypothesis.")],
      "Si + imparfait, conditionnel présent.", T_COND),
    Q("« Si tu étais venu, nous ___ ensemble. »", "aurions mangé", [
        ("mangerions", "Si + plus-que-parfait requires the conditional past."),
        ("avons mangé", "The passé composé states a real fact, not a hypothesis."),
        ("mangions", "The imperfect does not fit the unreal past.")],
      "Si + plus-que-parfait, conditionnel passé.", T_COND),
    Q("« Selon la radio, le ministre ___ démissionné. » (information not confirmed)", "aurait", [
        ("a", "The passé composé would present the fact as certain."),
        ("avait", "The plus-que-parfait does not express unconfirmed news."),
        ("aura", "The future is not the right tense.")],
      "The conditional of unconfirmed information: aurait démissionné.", T_COND),
    # --- Les pronoms relatifs composés (3)
    Q("« La table sur ___ j'ai posé mon sac est cassée. »", "laquelle", [
        ("lequel", "« Table » is feminine singular."),
        ("lesquelles", "The antecedent is singular."),
        ("dont", "« Poser sur » needs a preposition plus lequel, not « dont ».")],
      "sur + laquelle (feminine singular).", T_REL),
    Q("« Voici le problème ___ nous réfléchissons. »", "auquel", [
        ("lequel", "The verb « réfléchir à » needs à + lequel = auquel."),
        ("dont", "« Réfléchir de » is not used; the preposition is « à »."),
        ("que", "« Que » is a direct-object pronoun.")],
      "réfléchir à: à + lequel = auquel.", T_REL),
    Q("« Les raisons pour ___ il a refusé sont claires. »", "lesquelles", [
        ("lequel", "« Raisons » is plural."),
        ("lesquels", "« Raisons » is feminine."),
        ("laquelle", "« Raisons » is plural.")],
      "pour + lesquelles (feminine plural).", T_REL),
    # --- La nominalisation (2)
    Q("Nominalise: « Il est arrivé en retard. »", "Son arrivée tardive", [
        ("Son arrivant tardif", "« Arrivant » is not the noun of « arriver »."),
        ("Il arrivée en retard", "A noun cannot be a verb."),
        ("Son arriver tardif", "The infinitive is not used this way.")],
      "arriver → l'arrivée; en retard → tardive.", T_NOM),
    Q("« Quand la ville a détruit le vieux marché, ... » Which nominal version is correct?", "Après la destruction du vieux marché", [
        ("Après détruire le vieux marché", "After « après » a past infinitive is needed: après avoir détruit."),
        ("Après le détruit du vieux marché", "« Détruit » is a participle, not a noun."),
        ("Après détruisant le vieux marché", "The present participle is not used after « après ».")],
      "détruire → la destruction.", T_NOM),
    # --- L'inversion stylistique (3)
    Q("« À peine ___ parti que la pluie commença. »", "était-il", [
        ("il était", "After « à peine » at the start of a sentence, literary style inverts subject and verb."),
        ("il fut-il", "The subject is repeated."),
        ("était-t-il", "No « -t- » is needed after « était »: the verb ends with a consonant sound.")],
      "À peine + inversion: était-il parti.", T_INV),
    Q("« Peut-être ___ demain. » (venir, futur)", "viendra-t-il", [
        ("viendra-il", "The euphonic « -t- » is required between two vowels: viendra-t-il."),
        ("il viendra-t-il", "The subject is repeated."),
        ("viendra t'il", "Hyphens and « -t- » are written as viendra-t-il.")],
      "Peut-être + inversion with the euphonic -t-.", T_INV),
    Q("What is the effect of stylistic inversion in a literary sentence?", "It gives a more formal, literary tone and can emphasise a word", [
        ("It turns the sentence into a question", "Stylistic inversion does not always ask a question."),
        ("It turns the sentence negative", "It does not change the polarity."),
        ("It changes the tense", "It changes word order, not the tense.")],
      "A matter of style and emphasis.", T_INV, skill="Concept"),
    # --- Stylistique comparée anglais-français (3)
    Q("Best translation of « He swam across the river. »", "Il a traversé la rivière à la nage.", [
        ("Il a nagé à travers la rivière.", "It copies the English structure; French puts the main movement in the verb and the manner in a complement."),
        ("Il nageait la rivière à travers.", "The word order is a calque and unnatural."),
        ("Il est nagé la rivière.", "« Nager » does not take this auxiliary and structure.")],
      "French verb of movement + manner complement.", T_STYL),
    Q("The English word « actually » is best translated by...", "en fait", [
        ("actuellement", "That is a faux ami: « actuellement » means currently."),
        ("maintenant", "It means now."),
        ("aujourd'hui", "It means today.")],
      "Faux ami: actuellement ≠ actually.", T_STYL, skill="Recall"),
    Q("Translating « No smoking » by « Défense de fumer » is an example of...", "équivalence", [
        ("calque", "A calque copies the structure literally."),
        ("emprunt", "An emprunt borrows the word itself."),
        ("traduction littérale", "A literal translation would not be a fixed French sign.")],
      "A fixed expression with the same function in the other language.", T_STYL, skill="Concept"),
    # --- Traduire les temps et le passif (3)
    Q("Best translation of « I have lived in Douala for ten years. »", "J'habite à Douala depuis dix ans.", [
        ("J'ai habité à Douala pour dix ans.", "« Pour » and the passé composé suggest a completed period."),
        ("J'habiterai à Douala depuis dix ans.", "The future cannot be used with « depuis »."),
        ("J'habitais à Douala depuis dix ans.", "The imperfect puts the situation in the past.")],
      "Present + depuis for a situation that continues.", T_TEMPS),
    Q("Most natural translation of « English is spoken here. »", "Ici, on parle anglais.", [
        ("L'anglais est parlé ici.", "It is possible but heavy: French prefers « on » to a literal passive."),
        ("Ici est parlé anglais.", "The word order is wrong."),
        ("Ici, on est parlé anglais.", "« On » cannot take a passive verb here.")],
      "French often replaces the English passive by « on ».", T_TEMPS),
    Q("Best translation of « He had been waiting for an hour when she arrived. »", "Il attendait depuis une heure quand elle est arrivée.", [
        ("Il a attendu pendant une heure quand elle est arrivée.", "The passé composé does not give the background of a continuing action."),
        ("Il attendra depuis une heure quand elle est arrivée.", "The future does not fit."),
        ("Il avait été en attendant depuis une heure.", "The structure is ungrammatical.")],
      "Imparfait + depuis for a continuing background action.", T_TEMPS),
    # --- Traduire les expressions idiomatiques (2)
    Q("The French equivalent of « to kill two birds with one stone » is...", "faire d'une pierre deux coups", [
        ("tuer deux oiseaux avec une pierre", "That is word for word; the idiom in French is different."),
        ("casser deux pierres d'un coup", "It is not the idiom."),
        ("lancer deux pierres", "It is not the idiom.")],
      "Translate the idiom as an idiom.", T_IDIOM),
    Q("« Il pleut des cordes » means...", "It is raining heavily", [
        ("He is selling ropes", "It is an idiom about rain."),
        ("It is windy", "It speaks of rain, not wind."),
        ("It is raining ropes of water literally", "It is figurative.")],
      "Idiom for heavy rain.", T_IDIOM, skill="Recall"),
    # --- Le thème (2)
    Q("Translate into French: « I like swimming. »", "J'aime nager.", [
        ("J'aime nageant.", "The infinitive follows « aimer », not the present participle."),
        ("Je suis aimant nager.", "It copies an English structure."),
        ("Je aime nager.", "« Je » is elided before a vowel: j'aime.")],
      "aimer + infinitive; je → j'.", T_THEME),
    Q("Translate into French: « She asked me to come. »", "Elle m'a demandé de venir.", [
        ("Elle m'a demandé venir.", "« Demander » needs « de » before the infinitive."),
        ("Elle m'a demandé que je viens.", "After « demander que » the subjunctive is required, and the infinitive is simpler."),
        ("Elle a demandé moi de venir.", "The pronoun « me » goes before the verb: m'a demandé.")],
      "demander à quelqu'un de + infinitive.", T_THEME),
    # --- La version (2)
    Q("Translate into English: « Il vient de partir. »", "He has just left.", [
        ("He comes to leave.", "It is a literal calque."),
        ("He will leave.", "« Venir de » expresses the recent past."),
        ("He is leaving from.", "It is ungrammatical.")],
      "venir de + infinitive = has just.", T_VERS),
    Q("Translate into English: « Malgré la fatigue, elle a continué. »", "In spite of her tiredness, she carried on.", [
        ("Because of the tiredness, she continued.", "« Malgré » expresses opposition, not cause."),
        ("Thanks to the tiredness, she continued.", "« Malgré » does not mean thanks to."),
        ("Before the tiredness, she continued.", "« Malgré » does not express time.")],
      "malgré = in spite of.", T_VERS),
    # --- Analyser le sujet (3)
    Q("In « Seul le travail mène à la réussite », which word must be tested?", "seul", [
        ("travail", "It is a key word but not the limiting word."),
        ("mène", "It is the verb."),
        ("réussite", "It is a key word but not the limiting word.")],
      "« Seul » claims there is only one cause.", T_SUJET),
    Q("A student answers a sujet on the digital book by writing the history of printing. This is...", "a hors-sujet", [
        ("a problématique", "A problématique is a question."),
        ("a synthèse", "A synthèse is part of a plan."),
        ("a conclusion", "A conclusion answers the question.")],
      "The essay must answer the exact question.", T_SUJET, skill="Concept"),
    Q("What does the consigne « Dans quelle mesure... ? » ask for?", "A nuanced answer showing how far the idea is true", [
        ("Only « oui » or « non »", "It asks for degree."),
        ("A definition only", "A definition does not give the degree."),
        ("A list of authors", "It is not a request for authors.")],
      "Dans quelle mesure = up to what point.", T_SUJET, skill="Concept"),
    # --- La problématique (3)
    Q("Which is a good problématique for « Le téléphone aide-t-il à étudier ? »", "« Dans quelle mesure le téléphone aide-t-il à étudier sans distraire l'élève ? »", [
        ("« Qu'est-ce qu'un téléphone ? »", "It is a definition without tension."),
        ("« Le téléphone est utile. »", "It is a statement, not a question."),
        ("« Qui a inventé le téléphone ? »", "It asks for a fact.")],
      "Open, with tension.", T_PROB),
    Q("A problématique is born from...", "a tension in the sujet", [
        ("a date in the sujet", "A date is a fact."),
        ("the length of the sujet", "Length is irrelevant."),
        ("the title of the book", "It comes from the sujet.")],
      "Look for two ideas pulling in different directions.", T_PROB, skill="Concept"),
    Q("What is wrong with « Le numérique est-il bon ? » as a problématique?", "It is closed and vague, without tension", [
        ("It is too long", "It is short."),
        ("It uses the subjunctive", "It does not."),
        ("It is in the past tense", "It is in the present.")],
      "Good means open, precise, tied to the sujet.", T_PROB, skill="Reasoning"),
    # --- Les plans dialectique et thématique (3)
    Q("What is the order of a dialectical plan?", "Thèse, antithèse, synthèse", [
        ("Synthèse, thèse, antithèse", "The synthèse comes last."),
        ("Thèse, thèse, thèse", "There are three different movements."),
        ("Antithèse, antithèse, synthèse", "There is one of each.")],
      "Affirm, challenge, go beyond.", T_PLANS, skill="Recall"),
    Q("Which sujet suits a thematic plan?", "« Quelles mesures contre la famine ? »", [
        ("« Le livre numérique peut-il remplacer le livre ? »", "It has a yes-or-no tension, which suits a dialectical plan."),
        ("« Seule l'éducation développe un pays. »", "It is an affirmation to discuss."),
        ("« Le téléphone est-il toujours utile ? »", "It has a yes-or-no tension.")],
      "« What to do » questions suit fields.", T_PLANS),
    Q("A good synthèse is...", "a reasoned answer with conditions and nuances", [
        ("a repetition of the thèse", "It adds nothing."),
        ("an unrelated subject", "It must answer the problématique."),
        ("a statement that both sides are good", "That is a weak compromise.")],
      "It goes beyond thèse and antithèse.", T_PLANS, skill="Concept"),
    # --- Rédiger la dissertation (2)
    Q("The four moves of the introduction are...", "amorce, sujet, problématique, annonce du plan", [
        ("conclusion, amorce, plan, sujet", "The conclusion is not part of the introduction."),
        ("plan, plan, plan, plan", "They are different moves."),
        ("sujet, conclusion, amorce, plan", "The conclusion is not part of the introduction.")],
      "Hook, topic, question, path.", T_REDIG, skill="Recall"),
    Q("« Il n'y a pas de courant ; ___, les tablettes ne servent à rien. »", "par conséquent", [
        ("de plus", "It adds a point; it does not show a result."),
        ("pourtant", "It shows opposition."),
        ("car", "It shows cause and reverses the logic.")],
      "The second fact is the result of the first.", T_REDIG),
    # --- Le classicisme (3)
    Q("Which are the three classical unités?", "Action, lieu, temps", [
        ("Action, style, rime", "Style and rime are not unités."),
        ("Lieu, genre, titre", "Genre and titre are not unités."),
        ("Temps, ton, personnage", "Ton and personnage are not unités.")],
      "One action, one place, about one day.", T_CLASS, skill="Recall"),
    Q("Racine is above all the author of...", "tragedies such as Phèdre", [
        ("fables", "Fables are by La Fontaine."),
        ("realist novels", "Realist novels are of the 19th century."),
        ("a dictionary of the Lumières", "That is the Encyclopédie.")],
      "Phèdre (1677).", T_CLASS, skill="Recall"),
    Q("L'alexandrin has...", "twelve syllables", [
        ("eight syllables", "That is the octosyllabe."),
        ("ten syllables", "That is the décasyllabe."),
        ("six syllables only", "That is half a line.")],
      "Twelve syllables with a césure.", T_CLASS, skill="Recall"),
    # --- Le siècle des Lumières (3)
    Q("Who directed the Encyclopédie with d'Alembert?", "Diderot", [
        ("Voltaire", "Voltaire wrote Candide."),
        ("Rousseau", "Rousseau wrote Du contrat social."),
        ("Racine", "Racine lived in the 17th century.")],
      "Diderot directed it.", T_LUM, skill="Recall"),
    Q("Candide is an example of...", "a conte philosophique", [
        ("a tragedy", "It is a tale in prose."),
        ("a naturalist novel", "Naturalism is 19th century."),
        ("a lyric poem", "It is in prose.")],
      "A tale that carries an idea.", T_LUM, skill="Recall"),
    Q("Irony in the Lumières means...", "saying the opposite of what is meant so the reader sees the criticism", [
        ("telling the plain truth", "That is the opposite."),
        ("listing facts", "It is a figure of speech."),
        ("describing nature", "It is not a description.")],
      "The reader becomes an ally.", T_LUM, skill="Concept"),
    # --- Le romantisme (2)
    Q("The mal du siècle is...", "the sadness and disillusion of the young generation of the early 19th century", [
        ("a classical rule", "It is a feeling, not a rule."),
        ("a type of verse", "It is not about verse."),
        ("a naturalist method", "Naturalism is later.")],
      "Solitude and melancholy.", T_ROM, skill="Concept"),
    Q("Hugo's preface to Cromwell defends...", "the mélange des genres and a free drama", [
        ("the three unités", "That is classical."),
        ("bienséance in all plays", "That is classical."),
        ("scientific determinism", "That is naturalist.")],
      "The sublime and the grotesque together.", T_ROM),
    # --- Le réalisme et le naturalisme (2)
    Q("Zola is the leader of...", "naturalism", [
        ("classicism", "Classicism is of the 17th century."),
        ("romanticism", "Zola is later."),
        ("négritude", "Négritude is of the 20th century.")],
      "Les Rougon-Macquart.", T_REAL, skill="Recall"),
    Q("What is « style indirect libre » ?", "Reporting a character's thoughts without quotation marks or introducing verb", [
        ("A form of rhyme", "It is a narrative technique."),
        ("A pure description of a place", "It reports thoughts."),
        ("A type of title", "It is not a title.")],
      "Thoughts told by the narrator.", T_REAL, skill="Concept"),
    # --- La négritude et la littérature post-indépendance (3)
    Q("The three founders of négritude are...", "Césaire, Senghor and Damas", [
        ("Oyono, Beti and Kane", "They are novelists."),
        ("Zola, Flaubert and Balzac", "They are French realist writers."),
        ("Hugo, Lamartine and Vigny", "They are French romantic writers.")],
      "Martinique, Senegal, Guyane.", T_NEG, skill="Recall"),
    Q("Une vie de boy is by...", "Ferdinand Oyono, a Cameroonian writer", [
        ("Aimé Césaire", "Césaire wrote the Cahier."),
        ("Léopold Senghor", "Senghor wrote Chants d'ombre."),
        ("Voltaire", "Voltaire wrote Candide.")],
      "A satire of colonial life (1956).", T_NEG, skill="Recall"),
    Q("A major theme of post-independence novels is...", "disillusion with the new state and tension between tradition and modernity", [
        ("praise of the royal court", "That is classical."),
        ("the rules of the three unités", "That is classical."),
        ("the mal du siècle of 1830", "That is romantic.")],
      "Kourouma, Kane, Bebey.", T_NEG, skill="Concept"),
]
assert len(P1) == 50, len(P1)
_topics = [T_SUBJ, T_COND, T_REL, T_NOM, T_INV, T_STYL, T_TEMPS, T_IDIOM, T_THEME, T_VERS, T_SUJET, T_PROB, T_PLANS, T_REDIG,
           T_CLASS, T_LUM, T_ROM, T_REAL, T_NEG]
assert {s["concept"] for s in P1} == set(_topics)
SETS.append(practice_set(module=M_EXAM, topic="Paper 1", title="Paper 1 mock exam A", lesson="frl2-paper-1-strategy",
                         mock=True, time_limit_minutes=90, questions=build(P1, 320)))

# ================================================================== Paper 2 practice paper A (25 parts)
def R(label, prompt, right, wrongs, step, concept, hint, skill="Analyse", passage=""):
    return K(label + " " + prompt, right, wrongs, step, concept, skill, hint, passage=passage)


P2 = [
    # Question 1: the unseen poem (8 parts)
    R("Question 1(a).", "What is the rhyme scheme of each strophe?", "ABAB (rimes croisées)", [
        ("AABB (rimes plates)", "Lines 1 and 2 do not rhyme with each other."),
        ("ABBA (rimes embrassées)", "Lines 1 and 4 do not rhyme."),
        ("No rhyme", "Every strophe is rhymed.")],
      "Strophe 1: village / encore / ombrage / aurore: A B A B.", T_ROM, "Mark the end sounds of each line.", passage=POEM),
    R("Question 1(b).", "How many syllables has each line (the final mute e is not counted)?", "8", [
        ("12", "That is the alexandrin."), ("10", "That is the décasyllabe."), ("6", "That is half an alexandrin.")],
      "Le soir descend sur le village: 8 syllables; the other lines also have 8.", T_ROM, "Count each sounded syllable.", "Calculation", POEM),
    R("Question 1(c).", "« Les braises rêvent de l'aurore. » Which figure of speech?", "personnification", [
        ("comparaison", "There is no tool word such as comme."),
        ("litote", "Nothing is understated."),
        ("oxymore", "There are no contradictory words.")],
      "Embers are given a human act: dreaming.", T_ROM, "Can embers dream ?", "Application", POEM),
    R("Question 1(d).", "« L'arbre rouge brûle encore » says that the red flowers look like fire. Which figure?", "métaphore", [
        ("comparaison", "There is no comme."),
        ("anaphore", "No word is repeated at the start of lines."),
        ("euphémisme", "Nothing is softened.")],
      "The tree is said to burn: an implicit comparison.", T_ROM, "Is there a tool word ?", "Application", POEM),
    R("Question 1(e).", "Which tense dominates strophe 3?", "The future", [
        ("The passé simple", "No passé simple appears."),
        ("The imperfect", "No imperfect appears."),
        ("The plus-que-parfait", "No plus-que-parfait appears.")],
      "Chanterai, gardera, sera, garderas.", T_ROM, "Underline the verbs.", "Analyse", POEM),
    R("Question 1(f).", "What is the register of the poem?", "Lyrique", [
        ("Satirique", "There is no mockery."),
        ("Épique", "There is no heroic action."),
        ("Polémique", "There is no attack.")],
      "The first person expresses feeling, in a melancholy and tender tone.", T_ROM, "Who speaks and what does he feel ?", "Analyse", POEM),
    R("Question 1(g).", "What is the main theme?", "The passing of time and the call to enjoy the present", [
        ("The history of a war", "No war is mentioned."),
        ("A political election", "Politics is absent."),
        ("A school exam", "School is absent.")],
      "« Cueille la joie : les jours s'en vont. »", T_ROM, "Look at the imperatives.", "Interpretation", POEM),
    R("Question 1(h).", "What is notable about the rhymes of strophe 1?", "All four end with a mute e (rimes féminines)", [
        ("All four are masculine rhymes", "Village, encore, ombrage and aurore end with a mute e."),
        ("They alternate masculine and feminine", "Strophe 1 has only feminine rhymes; the alternation appears in strophes 2 and 3."),
        ("They do not rhyme", "They do rhyme (ABAB).")],
      "A feminine rhyme ends with a mute e.", T_ROM, "Check the last letter of each line.", "Analyse", POEM),
    # Question 2: classicisme
    R("Question 2(a).", "Which of the following is NOT a classical rule?", "Mixing the sublime and the grotesque", [
        ("Respect for the unité de lieu", "It is a classical rule."),
        ("Bienséance", "It is a classical rule."),
        ("Vraisemblance", "It is a classical rule.")],
      "The mélange des genres belongs to romantic drama.", T_CLASS, "Which rule did Hugo attack?", "Concept"),
    R("Question 2(b).", "L'Avare is best described as...", "a comédie de caractère built on a ruling fault, avarice", [
        ("a tragedy of fatal passion", "That describes Racine."),
        ("a naturalist novel", "It is a 17th-century play."),
        ("a lyric poem", "It is a play.")],
      "Molière's comedies of character expose a vice.", T_CLASS, "Which fault drives the main character ?", "Recall"),
    R("Question 2(c).", "Which thesis best contrasts Corneille and Racine?", "Corneille shows will mastering passion; Racine shows passion overwhelming will", [
        ("Corneille wrote comedies, Racine wrote novels", "Both wrote tragedies."),
        ("Both show characters free of all passion", "Passion is central in both."),
        ("Racine shows only duty", "Duty against passion is Corneille's dilemma.")],
      "A balanced thesis names a difference with a reason.", T_CLASS, "What does each hero do with passion ?", "Synthesis"),
    R("Question 2(d).", "For « En quoi le classicisme est-il un art de la raison ? », which part title is best?", "Les règles au service de la clarté et de la vraisemblance", [
        ("La vie privée de Louis XIV", "It is off the subject."),
        ("Les débuts du roman réaliste", "That belongs to the 19th century."),
        ("La poésie des mal-aimés", "It is not about classical reason.")],
      "A part title must answer the sujet.", T_CLASS, "Which title links rules and reason ?", "Application"),
    # Question 3: Lumières
    R("Question 3(a).", "For « En quoi la littérature des Lumières est-elle un instrument de combat ? », the best three-part plan is...", "les combats, les moyens, les limites", [
        ("la vie de Voltaire, la vie de Rousseau, la vie de Diderot", "It tells biographies rather than answering the question."),
        ("le théâtre, le théâtre, le théâtre", "It repeats one idea."),
        ("les dates, les lieux, les noms", "It is a list without argument.")],
      "A plan answers the question: what, how, and with what limits.", T_LUM, "Which plan answers « En quoi » ?", "Application"),
    R("Question 3(b).", "What does the conte Candide mainly criticise?", "A naïve optimism, war and intolerance", [
        ("The invention of the telephone", "It was not invented in the 18th century."),
        ("The rules of classical tragedy", "That is not the target."),
        ("The industrial novel", "It is of the 19th century.")],
      "Voltaire uses adventures to criticise ideas.", T_LUM, "What does the hero learn ?", "Interpretation"),
    R("Question 3(c).", "Which nuance is correct about the Lumières and the Revolution?", "They helped prepare the Revolution, which also had financial, social and political causes", [
        ("They alone caused it", "The Revolution had many causes."),
        ("They had no influence at all", "Their ideas spread widely."),
        ("They wrote after it began and had no effect", "Most of the major works are earlier.")],
      "Use « ont contribué à préparer ».", T_LUM, "Is one cause enough ?", "Evaluation"),
    # Question 4: romantisme et réalisme
    R("Question 4(a).", "Which feature belongs to the drame romantique defended by Hugo?", "Mixture of the sublime and the grotesque", [
        ("Strict respect of the three unités", "It is classical."),
        ("All violence off stage", "That is bienséance, a classical rule."),
        ("Only noble characters", "Romantic drama accepts all ranks.")],
      "The preface to Cromwell.", T_ROM, "Which rule is broken ?", "Recall"),
    R("Question 4(b).", "Which thesis best answers « Montrez que le retour en arrière est un procédé efficace dans le roman » ?", "Le retour en arrière éclaire le passé du personnage, explique ses actes présents et maintient l'intérêt du lecteur.", [
        ("Il y a un retour en arrière dans le roman.", "It only states the presence of the technique."),
        ("Le retour en arrière est un procédé.", "It defines but does not argue."),
        ("Le roman est long.", "It is irrelevant.")],
      "A thesis states the effects that you will prove.", T_ROM, "Which sentence explains the effect ?", "Application"),
    R("Question 4(c).", "Which plan best fits « Le milieu détermine-t-il les personnages dans le roman naturaliste ? »", "Le milieu décrit, les personnages déterminés, les limites du déterminisme", [
        ("Biographie de l'auteur, date de naissance, mort", "It does not answer the question."),
        ("Rime, strophe, vers", "That is for poems."),
        ("Théâtre, comédie, tragédie", "That is for drama.")],
      "A plan builds on key words: milieu, déterminés, limites.", T_REAL, "Which plan follows the sujet ?", "Application"),
    R("Question 4(d).", "« Mariama regardait la rue. Combien de temps durerait encore cette attente ? » Which technique appears in the second sentence?", "Style indirect libre", [
        ("Discours direct", "There are no quotation marks and no introducing verb."),
        ("Anaphore", "No repetition at the start of sentences."),
        ("Litote", "There is no understatement.")],
      "Thoughts reported without a verb like pensa.", T_REAL, "Who asks the question ?", "Application"),
    # Question 5: négritude et post-indépendance
    R("Question 5(a).", "A sujet says that parents have too much authority over children. What is the best first step?", "Define « parents » (it may include elders and the wider family) and the word « trop »", [
        ("Retell the whole book", "A retelling does not answer the question."),
        ("Write only about your own family", "The text must be used."),
        ("Skip the definition", "The key words need defining.")],
      "The Board's report notes that parents can include elders.", T_NEG, "Whose authority counts ?", "Application"),
    R("Question 5(b).", "Which plan best uses the text for a statement about gender equality?", "Where equality exists in the text, its limits in the text, then your society", [
        ("A list of unrelated proverbs", "It does not use the text."),
        ("Only a definition of equality", "It does not use the text."),
        ("A biography of the author", "It does not answer the question.")],
      "Evidence from the text, then application.", T_NEG, "Which plan names the text ?", "Application"),
    R("Question 5(c).", "Which theme best fits Kourouma's Les Soleils des indépendances?", "Disillusion after independence", [
        ("Praise of colonial rule", "The novel does not praise colonial rule."),
        ("The rules of classical tragedy", "That is a different period."),
        ("The ideal of the philosopher-king", "It is not the theme.")],
      "A prince's decline in the new state.", T_NEG, "What happens to the hope ?", "Interpretation"),
    R("Question 5(d).", "Which is the best synthèse for « La littérature africaine a-t-elle trahi l'espoir de liberté ? »", "It records disappointment but keeps freedom alive by criticism and new forms", [
        ("It only praises all governments", "That is not what the writers did."),
        ("It never mentions independence", "It often does."),
        ("It stopped being written", "It continued to grow.")],
      "A synthèse nuances with conditions.", T_NEG, "What does criticism do to hope ?", "Evaluation"),
    # Question 6: method
    R("Question 6(a).", "Why must every point in a literary essay be supported by a precise moment of the text?", "Because general answers cannot prove an interpretation and were criticised in the Board's report", [
        ("Because examiners like long quotations", "Precision matters more than length."),
        ("Because the plot is the only subject", "The plot is evidence, not the subject."),
        ("Because quotations replace analysis", "Analysis is still needed.")],
      "Evidence makes the argument credible.", T_NEG, "What did the report criticise ?", "Reasoning"),
    R("Question 6(b).", "Which order is best for a poem commentary?", "Structure externe, structure interne, tenses, lexical field, theme", [
        ("Theme, then random lines", "It is not a method."),
        ("Biography only", "The text must be analysed."),
        ("Quote every line without comment", "It is not an analysis.")],
      "A fixed method keeps the commentary complete.", T_ROM, "What does the report expect ?", "Application"),
]
assert len(P2) == 25, len(P2)
SETS.append(practice_set(module=M_EXAM, topic="Paper 2", title="Paper 2 practice paper A", lesson="frl2-paper-2-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P2, 330)))

# ================================================================== Paper 3 practice paper A (20 parts)
P3 = [
    R("Question 1(a).", "Situation: « Lors d'une conférence dans votre quartier, vous parlez de la prévention des maladies contagieuses. » What is your role?", "A speaker addressing residents", [
        ("A judge reading a law", "No judge is mentioned."),
        ("A poet reading to a king", "No such role is given."),
        ("A translator", "Translation is a different task.")],
      "Identify the role before you plan.", T_SUJET, "Who speaks and to whom ?", "Application"),
    R("Question 1(b).", "Which plan fits « Quelles mesures contre la famine ? »", "Mesures politiques, économiques et sociales", [
        ("Thèse, antithèse, synthèse for a yes-or-no debate", "There is no yes-or-no tension."),
        ("The history of the alphabet", "It is off the subject."),
        ("A list of poems", "It is off the subject.")],
      "A « what to do » question suits a thematic plan.", T_PLANS, "Is it a yes-or-no question ?", "Application"),
    R("Question 1(c).", "In a debate for or against the digital book at school, the first paragraph should...", "state a clear position, say why the question matters and announce the arguments", [
        ("tell the story of paper", "It does not take a position."),
        ("avoid taking a side", "A debate needs a position."),
        ("only quote an author", "It does not state your position.")],
      "A debater commits early.", T_REDIG, "What does a debater say first ?", "Application"),
    R("Question 1(d).", "Which problématique fits « Le numérique peut-il remplacer le livre ? »", "Dans quelle mesure l'écran peut-il prendre la place du papier sans appauvrir la lecture ?", [
        ("Qu'est-ce qu'un écran ?", "A definition without tension."),
        ("Le numérique est-il bon ?", "Closed and vague."),
        ("Qui a inventé l'écran ?", "A factual question.")],
      "Open and tied to the sujet.", T_PROB, "Which question has both sides ?", "Application"),
    R("Question 1(e).", "« Actuellement » means...", "currently", [
        ("actually", "A faux ami; « actually » is en fait."),
        ("eventually", "« Eventually » is finalement."),
        ("in the past", "It refers to the present.")],
      "Faux ami.", T_REDIG, "Present or contrast ?", "Recall"),
    R("Question 1(f).", "Which sentence uses the right word for a disease that spreads across several continents?", "Cette pandémie a touché plusieurs continents.", [
        ("Cette épidémie a touché plusieurs continents.", "An épidémie is regional."),
        ("Cette épidémie mondiale reste dans un seul quartier.", "It contradicts itself."),
        ("Cette pandémie est un village.", "It is meaningless.")],
      "Pandémie means worldwide.", T_SUJET, "Which word is global ?", "Concept"),
    R("Question 2(a).", "Translate into French: « I have been learning French for two years. »", "J'apprends le français depuis deux ans.", [
        ("J'ai appris le français pour deux ans.", "« Pour » and the passé composé suggest a finished period."),
        ("J'apprenais le français depuis deux ans.", "The imperfect puts the situation in the past."),
        ("J'apprendrai le français depuis deux ans.", "The future does not fit with « depuis ».")],
      "Present + depuis.", T_THEME, "The action continues now.", "Application"),
    R("Question 2(b).", "Translate into French: « The more you read, the more you learn. »", "Plus on lit, plus on apprend.", [
        ("Le plus on lit, le plus on apprend.", "The English structure is not copied; French uses « plus..., plus... »."),
        ("Plus lire, plus apprendre.", "Verbs must be conjugated."),
        ("La lecture plus, l'apprentissage plus.", "It is ungrammatical.")],
      "Plus... plus... without « le ».", T_STYL, "Which structure is French ?", "Application"),
    R("Question 2(c).", "Translate into French: « Many young people are looking for work in the cities. »", "De nombreux jeunes cherchent du travail dans les villes.", [
        ("Beaucoup jeunes sont cherchant du travail dans les villes.", "French does not use the English progressive form."),
        ("Des nombreux jeunes cherchent travail dans les villes.", "« De nombreux » is used without « des », and « du travail » is needed."),
        ("Les jeunes beaucoup cherchent des travails.", "The word order and « travails » are wrong.")],
      "Present simple; de nombreux + noun.", T_THEME, "Do not copy are looking.", "Application"),
    R("Question 2(d).", "Translate into French: « He told me that he was tired. »", "Il m'a dit qu'il était fatigué.", [
        ("Il m'a dit qu'il est fatigué.", "After a past main verb, the verb of the subordinate agrees in the past: était."),
        ("Il a dit moi qu'il était fatigué.", "The pronoun goes before the verb: m'a dit."),
        ("Il m'a dit qu'il serait fatigué.", "It changes the meaning to the future.")],
      "Sequence of tenses: m'a dit que + imparfait.", T_THEME, "Match the tense of the main verb.", "Application"),
    R("Question 2(e).", "Translate into French: « A new hospital will be built here next year. »", "Un nouvel hôpital sera construit ici l'année prochaine.", [
        ("Un nouvel hôpital construira ici l'année prochaine.", "The hospital does not build; it is built."),
        ("Un nouvel hôpital est construit ici l'année dernière.", "« Dernière » means last, and the tense is not future."),
        ("Un nouvel hôpital serait construit ici hier.", "« Hier » is the past."),],
      "The English passive future: sera construit.", T_TEMPS, "Who builds the hospital ?", "Application"),
    R("Question 3(a).", "Translate into English: « Depuis plusieurs années, la sécheresse oblige de nombreuses familles à quitter leur village. »", "For several years, drought has been forcing many families to leave their villages.", [
        ("Since several years, drought forces many families to leave their village.", "English uses « for » with a period and the present perfect."),
        ("For several years, drought forced many families to leave.", "The simple past suggests it has ended."),
        ("Several years ago, drought obliged many families.", "It changes the meaning.")],
      "Depuis + present = present perfect continuous.", T_VERS, "The situation continues.", "Application"),
    R("Question 3(b).", "Translate into English: « Il y a dix ans, ma sœur a quitté le village. »", "Ten years ago, my sister left the village.", [
        ("There are ten years, my sister left the village.", "It is a literal calque."),
        ("It has ten years that my sister leaves the village.", "It is a literal calque."),
        ("In ten years, my sister will leave the village.", "It changes the time.")],
      "Il y a + time = ago.", T_VERS, "Past or future ?", "Application"),
    R("Question 3(c).", "Translate into English: « Cela fait trois jours qu'il pleut. »", "It has been raining for three days.", [
        ("It makes three days that it rains.", "It is a literal calque."),
        ("It rained three days.", "The rain is continuing."),
        ("It will rain for three days.", "It changes the time.")],
      "Cela fait... que = for + present perfect continuous.", T_TEMPS, "The rain continues.", "Application"),
    R("Question 3(d).", "Translate into English: « Il faut que nous agissions maintenant. »", "We must act now.", [
        ("It is necessary that we acted now.", "The subjunctive does not mean the past."),
        ("We acted now.", "It misses the obligation."),
        ("It fails that we act.", "It is a literal calque.")],
      "Il faut que + subjunctive = must.", T_VERS, "Obligation, present.", "Application"),
    R("Question 3(e).", "Translate into English: « Elle a failli tomber. »", "She nearly fell.", [
        ("She failed to fall.", "« Faillir + infinitive » means almost."),
        ("She fell.", "She did not fall."),
        ("She will fall.", "It is the past.")],
      "faillir + infinitive = nearly.", T_IDIOM, "Did she fall?", "Application"),
    R("Question 4(a).", "Which sentence is correct?", "Ils ont assisté à la réunion.", [
        ("Ils ont aidé à la réunion pour dire qu'ils étaient présents.", "« Aider » means to help, not to attend."),
        ("Ils ont assisté la réunion.", "« Assister » needs « à » to mean attend."),
        ("Ils ont attendu à la réunion à la fin.", "It does not express attending.")],
      "assister à = to attend.", T_REDIG, "Which verb means attend ?", "Concept"),
    R("Question 4(b).", "Which form completes « Bien que la pluie ___ forte, nous sommes sortis » ?", "soit", [
        ("est", "« Bien que » takes the subjunctive."),
        ("sera", "The future is not used."),
        ("serait", "The conditional is not used.")],
      "bien que + subjunctive.", T_SUBJ, "Which mood follows bien que ?", "Application"),
    R("Question 4(c).", "« Éventuellement » is best translated as...", "possibly", [
        ("eventually", "That is a faux ami; « eventually » is finalement."),
        ("always", "It is toujours."),
        ("never", "It is jamais.")],
      "Faux ami.", T_STYL, "Possibility, not time.", "Recall"),
    R("Question 4(d).", "Which sentence is correct?", "Si j'avais le temps, je lirais davantage.", [
        ("Si j'aurais le temps, je lirais davantage.", "« Si » is not followed by the conditional."),
        ("Si j'ai eu le temps, je lis davantage.", "The tenses do not express the hypothesis."),
        ("Si j'avais le temps, je lirai davantage.", "The future does not follow « si + imparfait ».")],
      "Si + imparfait, conditionnel.", T_COND, "Which tense follows si ?", "Application"),
]
assert len(P3) == 20, len(P3)
SETS.append(practice_set(module=M_EXAM, topic="Paper 3", title="Paper 3 practice paper A", lesson="frl2-paper-3-strategy",
                         mock=True, time_limit_minutes=150, questions=build(P3, 340)))
