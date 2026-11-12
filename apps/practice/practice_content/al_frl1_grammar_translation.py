"""Practice sets for A Level French, Lower Sixth: Grammaire Avancée et Stylistique Comparée; Méthodologie de la Traduction : Thème et Version
(one set per lesson, 8 questions each, Paper 1 style multiple choice).

All sentences are original and invented. Each question has exactly one correct option.
"""

from .dsl import *  # noqa: F403

COURSE = ("french", "lower-sixth")

M1 = "Grammaire Avancée et Stylistique Comparée"
M2 = "Méthodologie de la Traduction : Thème et Version"

_POS = [1, 3, 0, 2, 2, 0, 3, 1]   # position of the correct option, so each 8-question set has two of each letter
_count = [0]


def Q(prompt, right, wrongs, step, concept, skill, hint, feedback=""):
    """4-option MC. `right` is the correct option text; `wrongs` is 3 (text, why) pairs. The correct option is placed by a
    fixed cycle so that each set of 8 has A, B, C and D twice."""
    pos = _POS[_count[0] % 8]
    _count[0] += 1
    assert len(wrongs) == 3
    choices = []
    w = iter(wrongs)
    for i in range(4):
        if i == pos:
            choices.append(C(right, correct=True))
        else:
            t, why = next(w)
            choices.append(C(t, why=why))
    steps = [S("Reasoning", text=s) for s in ([step] if isinstance(step, str) else step)]
    return MC(prompt, choices, steps, concept=concept, skill=skill, hint=hint, feedback=feedback)


SETS = []

# ================================================================== 1. Le subjonctif
SETS.append(practice_set(
    module=M1, topic="Le subjonctif", title="Le subjonctif : emploi et formes",
    lesson="frl1-subjonctif",
    questions=[
        Q("Complétez : *Il faut que tu ... à l'heure.*",
          "sois", [("es", "Indicative: *il faut que* requires the subjunctive."), ("seras", "Future indicative: wrong mood after *il faut que*."), ("étais", "Imperfect indicative: wrong mood.")],
          "*Il faut que* expresses necessity, so the subjunctive of *être*: *que tu sois*.", "Subjonctif présent d'être", "Recall", "Which mood follows *il faut que* and what is the irregular form of *être* in it?"),
        Q("Complétez : *Je veux que nous ... ce travail ensemble.*",
          "finissions", [("finirons", "Future indicative: *vouloir que* takes the subjunctive."), ("finissons", "Indicative present: the subjunctive of the *nous* form is *finissions*."), ("finissent", "Wrong person: *nous* needs *-ions*.")],
          "*Vouloir que* needs the subjunctive. From *ils finissent*: stem *finiss-* + *-ions*: *finissions*.", "Formation du subjonctif", "Calculation", "Start from *ils finissent*."),
        Q("Complétez : *Bien qu'elle ... peu de temps, elle nous a aidés.*",
          "ait", [("a", "Indicative: *bien que* takes the subjunctive."), ("aie", "*Que j'aie* is the first person; *elle* needs *ait*."), ("avait", "Imperfect indicative: wrong mood.")],
          "*Bien que* is followed by the subjunctive. *Avoir* is irregular: *qu'elle ait*.", "Bien que + subjonctif", "Recall", "What mood does a conjunction of concession take, and which verb form is irregular?"),
        Q("Laquelle de ces phrases est correcte ?",
          "Je ne pense pas qu'il vienne.", [("Je pense qu'il vienne.", "The affirmative *penser que* takes the indicative."), ("J'espère qu'il vienne.", "*Espérer que* takes the indicative (*qu'il viendra*)."), ("Il est certain qu'il vienne.", "*Il est certain que* expresses certainty: indicative.")],
          "A negative *penser que* expresses doubt: subjunctive. Affirmative *penser*, *espérer* and *il est certain* take the indicative.", "Mode après les verbes d'opinion", "Concept", "Which main clause expresses doubt rather than a fact?"),
        Q("Complétez : *Marie travaille dur pour ... l'examen.* (Marie veut elle-même réussir.)",
          "réussir", [("qu'elle réussisse", "Possible only with a different subject; the subject is the same here, so the infinitive is used."), ("que réussir", "*Que* cannot be followed by an infinitive."), ("réussisse", "A subjunctive form cannot stand without *que*.")],
          "When both verbs have the same subject, use the infinitive: *pour réussir*.", "Infinitif ou subjonctif", "Application", "Do the two verbs have the same subject?"),
        Q("Choisissez la forme correcte : *Je suis ravi que vous ... l'examen hier.*",
          "ayez réussi", [("avez réussi", "Indicative: *être ravi que* needs the subjunctive."), ("réussissiez", "Present subjunctive: it does not show that the success came before the joy."), ("réussiriez", "Conditional: wrong mood.")],
          "Feeling: subjunctive. *Hier* shows an earlier action: past subjunctive *ayez réussi*.", "Subjonctif passé", "Application", "Look at *hier*: was the success before or after the feeling?"),
        Q("Complétez : *C'est le plus beau paysage que j'... jamais vu.*",
          "aie", [("ai", "Indicative: after a superlative that gives an opinion, the subjunctive is used."), ("avais", "Imperfect indicative: wrong mood and tense."), ("aurai", "Future: wrong mood.")],
          "After a superlative (*le plus beau*) the subjunctive is used: *que j'aie vu*.", "Subjonctif après un superlatif", "Concept", "What mood follows *le plus beau ... que*?"),
        Q("Dans un texte classique, *Il fallait qu'il parlât* signifie :",
          "He had to speak.", [("He spoke well.", "*Parlât* is not an adverb of manner; it is a verb form."), ("He must speak tomorrow.", "The sentence is in the past (*fallait*)."), ("He was speaking.", "*Parlât* is the imperfect subjunctive after *il fallait que*, not an imperfect of action.")],
          "*Parlât* is the imperfect subjunctive, used after a past main verb in literary French. It translates as an ordinary form: *He had to speak.*", "Subjonctif imparfait (littéraire)", "Interpretation", "Look at the tense of *fallait*: past or present?"),
    ]))

# ================================================================== 2. Le conditionnel
SETS.append(practice_set(
    module=M1, topic="Le conditionnel", title="Le conditionnel : formes et emplois",
    lesson="frl1-conditionnel",
    questions=[
        Q("Complétez : *Si j'avais le temps, je ... te voir.*",
          "viendrais", [("viendrai", "Future: *si* + imparfait needs the conditional."), ("viens", "Present: does not match an imaginary condition."), ("serais venu", "Past conditional: needs *si* + plus-que-parfait.")],
          "*Si* + imparfait gives the conditional présent: *je viendrais*.", "Si + imparfait", "Recall", "What tense follows *si* in an unlikely condition?"),
        Q("Complétez : *Si tu avais étudié, tu ... réussi.*",
          "aurais réussi", [("avais réussi", "Pluperfect in the result clause: it must be the past conditional."), ("réussirais", "Present conditional: the condition belongs to the past."), ("réussiras", "Future: mismatches the pluperfect condition.")],
          "*Si* + plus-que-parfait requires the conditionnel passé: *tu aurais réussi*.", "Si + plus-que-parfait", "Application", "Is the condition possible now or impossible because it is past?"),
        Q("Laquelle de ces phrases est correcte ?",
          "Si tu venais, je serais content.", [("Si tu viendrais, je serais content.", "Never use the conditional after *si*."), ("Si tu viens, je serais content.", "*Si* + présent needs a future, not a conditional."), ("Si tu venais, je serai content.", "*Si* + imparfait needs the conditional, not the future.")],
          "The pair *si* + imparfait, conditionnel présent is correct: *venais ... serais*.", "Phrases hypothétiques", "Concept", "Check the tense after *si*, then the result clause."),
        Q("Quelle phrase montre que le journaliste n'est pas sûr de l'information ?",
          "Le pont serait fermé à cause des pluies.", [("Le pont est fermé à cause des pluies.", "The present states a fact."), ("Le pont sera fermé à cause des pluies.", "The future makes a prediction."), ("Le pont était fermé à cause des pluies.", "The imperfect describes a past state as fact.")],
          "The conditional reports unconfirmed information.", "Conditionnel d'information", "Concept", "Which tense is the one used in rumours in the press?"),
        Q("Complétez : *Elle a dit qu'elle ... le lendemain.*",
          "viendrait", [("viendra", "After a past verb of saying, the future becomes the conditional."), ("vient", "Present: no sequence of tenses."), ("est venue", "Passé composé: changes the meaning.")],
          "Future in the past: conditional. *Elle a dit : Je viendrai* becomes *Elle a dit qu'elle viendrait.*", "Futur dans le passé", "Application", "What happens to the future after a past verb of speaking?"),
        Q("Quelle formule est la plus polie ?",
          "Je voudrais un renseignement.", [("Je veux un renseignement.", "Too blunt: the present of *vouloir* sounds like a demand."), ("Il me faut un renseignement.", "Direct statement of need, not polite."), ("Donne-moi un renseignement.", "An imperative: not polite to a stranger.")],
          "The conditional softens a request: *Je voudrais*.", "Conditionnel de politesse", "Concept", "Which tense softens a request?"),
        Q("Complétez pour exprimer un regret : *J'... dû réviser davantage.*",
          "aurais", [("aurai", "Future: not a regret."), ("avais", "Imperfect: does not express the regret about the past."), ("ai", "Passé composé: states the fact, not the regret.")],
          "Regret about a past action uses the past conditional of *devoir*: *j'aurais dû*.", "Conditionnel passé", "Application", "Which tense means *I should have*?"),
        Q("Quel est le conditionnel présent de *voir* à la première personne ?",
          "je verrais", [("je voirais", "The stem of *voir* in the future and conditional is *verr-*."), ("je voyais", "Imperfect indicative, not the conditional."), ("je verrai", "Future: the endings -ai and -ais differ.")],
          "The conditional is the future stem *verr-* + imperfect endings: *je verrais*.", "Radicaux irréguliers", "Recall", "What is the future stem of *voir*?"),
    ]))

# ================================================================== 3. Les pronoms relatifs composés
SETS.append(practice_set(
    module=M1, topic="Les pronoms relatifs composés", title="Lequel, auquel, duquel, dont : choisir le pronom",
    lesson="frl1-pronoms-relatifs-composes",
    questions=[
        Q("Complétez : *Le stylo ... j'écris est cassé.*",
          "avec lequel", [("avec que", "*Que* cannot follow a preposition."), ("dont", "*Dont* replaces *de* + noun; the verb takes *avec*."), ("avec qui", "*Qui* after a preposition refers to people, not things.")],
          "A preposition + thing needs *lequel*: *avec lequel*.", "Préposition + lequel", "Recall", "Is the antecedent a person or a thing?"),
        Q("Complétez : *La raison pour ... il est parti reste inconnue.*",
          "laquelle", [("lequel", "*Raison* is feminine."), ("qui", "*Qui* after a preposition refers to people."), ("dont", "*Dont* cannot follow a preposition.")],
          "*Raison* is feminine singular, preceded by *pour*: *pour laquelle*.", "Accord de lequel", "Recall", "Check the gender of *raison*."),
        Q("Complétez : *Le projet ... nous pensons est sérieux.*",
          "auquel", [("dont", "*Penser à*, not *de*."), ("duquel", "*Duquel* replaces *de* + masculine noun."), ("lequel", "The preposition *à* must contract with *lequel*.")],
          "*Penser à* gives *à* + *lequel* = *auquel*.", "Contraction auquel", "Application", "Which preposition does *penser* take?"),
        Q("Complétez : *Le film ... tout le monde parle est excellent.*",
          "dont", [("que", "*Parler de* needs *dont*."), ("auquel", "*Auquel* replaces *à*."), ("lequel", "*Lequel* needs a preposition before it.")],
          "*Parler de* gives *dont*: *le film dont tout le monde parle*.", "Dont", "Application", "Which preposition does *parler* take?"),
        Q("Complétez : *Voici le lac au bord ... nous avons campé.*",
          "duquel", [("dont", "*Dont* cannot follow *au bord de*; the compound form is used."), ("lequel", "The *de* of *au bord de* must contract: *duquel*."), ("de qui", "*Qui* is for people.")],
          "After *au bord de*, use *duquel* (masculine singular, with contraction of *de* + *lequel*).", "Duquel après préposition", "Application", "What preposition ends *au bord de*?"),
        Q("Complétez : *Les candidats, parmi ... se trouvait ma sœur, ont réussi.*",
          "lesquels", [("qui", "After *parmi*, *lequel* is required even for people."), ("dont", "*Dont* cannot follow a preposition."), ("lesquelles", "*Candidats* is masculine plural.")],
          "*Parmi* requires *lesquels* (masculine plural).", "Parmi + lesquels", "Concept", "What does *parmi* require after it, even with people?"),
        Q("Complétez : *Je ne comprends pas ... vous voulez dire.*",
          "ce que", [("ce qui", "*Ce qui* is the subject; here *vous* is the subject."), ("ce dont", "*Vouloir dire* does not take *de*."), ("ce à quoi", "*Vouloir dire* does not take *à*.")],
          "The relative clause has *vous* as subject and an object missing: *ce que*.", "Ce que / ce qui / ce dont", "Concept", "What is missing from the clause: a subject or an object?"),
        Q("Complétez : *L'homme ... fille est médecin habite ici.*",
          "dont la", [("dont sa", "Never a possessive after *dont*."), ("que la", "*Que* replaces a direct object, not *de* + noun."), ("dont de la", "Double *de*.")],
          "*Dont* replaces *de l'homme*; the noun follows with its article: *dont la fille*.", "Dont (possession)", "Application", "What follows *dont*: a possessive or an article?"),
    ]))

# ================================================================== 4. La nominalisation
SETS.append(practice_set(
    module=M1, topic="La nominalisation", title="Nominalisation : du verbe au nom",
    lesson="frl1-nominalisation",
    questions=[
        Q("Quel groupe nominal correspond à *Les prix ont augmenté* ?",
          "l'augmentation des prix", [("l'augmenter des prix", "*Augmenter* is a verb; use the noun *augmentation*."), ("augmentation les prix", "*De* + noun is needed to link the nouns."), ("l'augmentation de prix", "The definite article *des* is needed: the prices in question.")],
          "Verb to noun: *l'augmentation*; the subject follows with *de*: *des prix*.", "Nominalisation d'un verbe", "Recall", "Find the noun related to *augmenter*."),
        Q("Quel est le nom correspondant au verbe *décider* ?",
          "la décision", [("le décidement", "No such word."), ("la décidation", "No such word."), ("le décidé", "A past participle, not the noun.")],
          "*Décider* gives *la décision*.", "Paires verbe-nom", "Recall", "Think of *une décision importante*."),
        Q("Quel est le nom correspondant à l'adjectif *rapide* ?",
          "la rapidité", [("la rapideur", "No such word; adjectives in *-ide* give *-idité*."), ("la rapidation", "No such word."), ("le rapidement", "An adverb, not a noun.")],
          "*Rapide* gives *la rapidité*.", "Adjectif vers nom", "Recall", "Compare with *humide / l'humidité*."),
        Q("Transformez : *Quand le ministre est arrivé, ...*",
          "À l'arrivée du ministre, ...", [("À l'arrivé du ministre, ...", "The noun is *l'arrivée*, feminine."), ("Quand l'arrivée du ministre, ...", "The conjunction must be replaced by a preposition."), ("Après arriver du ministre, ...", "*Arriver* is a verb; use the noun.")],
          "Clause to noun phrase: *l'arrivée du ministre*, with *à* for the time.", "Connecteurs en prépositions", "Application", "Which noun comes from *arriver*, and what is its gender?"),
        Q("Transformez : *Parce que les prix ont augmenté, ...*",
          "En raison de l'augmentation des prix, ...", [("Parce que l'augmentation des prix, ...", "*Parce que* needs a clause; a noun phrase needs a preposition."), ("Malgré l'augmentation des prix, ...", "*Malgré* expresses concession, not cause."), ("À cause que les prix augmentent, ...", "*À cause que* is not French; use *à cause de* + noun.")],
          "*En raison de* + noun expresses cause.", "Expression de la cause", "Application", "Which preposition introduces a cause with a noun?"),
        Q("Quelle phrase nominalisée est correcte pour *La police a arrêté le suspect* ?",
          "L'arrestation du suspect par la police", [("L'arrestation de la police du suspect", "It reverses the roles of agent and object."), ("L'arrestation par le suspect de la police", "It means the suspect arrested the police."), ("Arrêter du suspect par la police", "The verb is not turned into a noun.")],
          "The object takes *de* and the agent *par*: *l'arrestation du suspect par la police*.", "Agent et objet", "Application", "Who did the action, who suffered it?"),
        Q("Quelle expression correspond à *Il a réagi rapidement* ?",
          "sa réaction rapide", [("sa réaction rapidement", "An adverb cannot qualify a noun."), ("son réagir rapide", "*Réagir* is a verb, not a noun."), ("sa réagir rapide", "Not French.")],
          "The adverb becomes an adjective: *rapide*, agreeing with *réaction* (feminine).", "Adverbe en adjectif", "Concept", "What becomes of an adverb when the verb becomes a noun?"),
        Q("Quel titre de journal est en style nominal ?",
          "Hausse du prix du carburant", [("Le prix du carburant a augmenté", "A verbal sentence."), ("Le carburant coûte plus cher", "A verbal sentence."), ("Les prix qui augmentent encore", "A relative clause, still verbal.")],
          "A nominal headline has no conjugated verb: *Hausse du prix du carburant*.", "Style nominal", "Interpretation", "Which headline has no verb?"),
    ]))

# ================================================================== 5. L'inversion stylistique
SETS.append(practice_set(
    module=M1, topic="L'inversion stylistique", title="Inversion : formes et déclencheurs",
    lesson="frl1-inversion-stylistique",
    questions=[
        Q("Complétez : *Peut-être ... malade.*",
          "est-il", [("il est", "After *peut-être* we invert in formal French."), ("est il", "The hyphen is missing."), ("est-t-il", "*Est* ends in *t*: no extra *-t-*.")],
          "Inversion: verb, hyphen, pronoun: *est-il*.", "Inversion simple", "Recall", "Where does the subject pronoun go, and how is it joined to the verb?"),
        Q("Complétez : *Sans doute ... raison.*",
          "a-t-elle", [("a-elle", "The *-t-* is needed between a vowel and *elle*."), ("elle a", "No inversion after *sans doute*."), ("à-t-elle", "*À* is a preposition; the verb form is *a*.")],
          "*A* ends in a vowel; before *elle* we add *-t-*: *a-t-elle*.", "Le -t- euphonique", "Calculation", "What is inserted between a verb ending in a vowel and *il/elle/on*?"),
        Q("Complétez : *À peine le professeur ... entré que les élèves se levèrent.*",
          "était-il", [("il était", "Inversion is required after *à peine* (complex inversion)."), ("était", "The pronoun *il* must repeat the noun subject."), ("est-il", "The tense must agree with *se levèrent* (past).")],
          "Complex inversion: noun subject + verb + hyphen + pronoun: *le professeur était-il entré*.", "Inversion complexe", "Application", "How does a noun subject get inverted?"),
        Q("Quelle formule d'incise est correcte ?",
          "« Je pars demain », a-t-il dit.", [("« Je pars demain », a il dit.", "Hyphens and *-t-* are missing."), ("« Je pars demain », a-il dit.", "The *-t-* is missing."), ("« Je pars demain », at-il dit.", "The verb is *a*, not *at*.")],
          "Verb ending in a vowel + *il*: *a-t-il dit*.", "L'incise", "Application", "Which letter must be added between *a* and *il*?"),
        Q("Dans *Il était tard ; aussi avons-nous décidé de rentrer*, *aussi* signifie :",
          "therefore", [("also", "That would be *aussi* without inversion, in the middle of a clause."), ("too", "As an adverb in a sentence, but here it opens the clause."), ("although", "*Bien que* is used for concession.")],
          "*Aussi* at the head of a clause with inversion means *therefore*.", "Aussi = donc", "Interpretation", "Notice the inversion *avons-nous*."),
        Q("Quelle phrase contient une inversion après un complément de lieu ?",
          "Au fond de la cour se dressait un manguier.", [("Au fond de la cour, un manguier se dressait.", "Normal order: subject before the verb."), ("Un manguier au fond de la cour se dressait.", "Normal order."), ("Au fond de la cour il se dressait un manguier.", "*Il* is a dummy subject: not the inversion pattern.")],
          "The subject *un manguier* follows the verb *se dressait*.", "Inversion après complément de lieu", "Concept", "Where is the subject placed?"),
        Q("Complétez : *La lettre qu'a ... le directeur est arrivée.*",
          "écrite", [("écrit", "The participle agrees with the preceding direct object *que* = *la lettre*."), ("écrits", "Feminine singular, not masculine plural."), ("écrites", "*Lettre* is singular.")],
          "The participle agrees with the preceding object (*lettre*, feminine singular): *écrite*.", "Accord du participe", "Application", "What does *que* stand for, and what are its gender and number?"),
        Q("Complétez : *Peut-être le ministre ... demain.*",
          "viendra-t-il", [("vient-il-t", "The *-t-* goes between verb and pronoun."), ("viendra-il", "*Viendra* ends in a vowel: *-t-* is required."), ("il viendra", "Complex inversion requires the pronoun after the verb.")],
          "Complex inversion with a noun subject: *le ministre viendra-t-il*.", "Inversion complexe", "Application", "What repeats the noun subject after the verb?"),
    ]))

# ================================================================== 6. Stylistique comparée
SETS.append(practice_set(
    module=M2, topic="Stylistique comparée anglais-français", title="Les procédés de traduction et les faux amis",
    lesson="frl1-stylistique-comparee",
    questions=[
        Q("*As soon as he gets back* devient *Dès son retour*. Quel procédé ?",
          "Transposition", [("Emprunt", "Nothing is borrowed unchanged."), ("Calque", "A calque translates the parts one by one."), ("Adaptation", "No cultural reference is replaced.")],
          "A clause becomes a noun phrase with the same meaning: a change of word class, so transposition.", "Transposition", "Concept", "Does the grammatical class change while the meaning stays?"),
        Q("Le mot *week-end* employé en français est un exemple de :",
          "emprunt", [("calque", "A calque would translate the parts (like *gratte-ciel*)."), ("équivalence", "No different expression is used."), ("adaptation", "No cultural reference is changed.")],
          "The English word is taken over unchanged: borrowing.", "Emprunt", "Recall", "Is the English word kept or translated?"),
        Q("*Wet paint* se traduit par *Peinture fraîche*. Quel procédé ?",
          "Équivalence", [("Calque", "A calque would give *Peinture mouillée*."), ("Traduction littérale", "The words are not translated one by one."), ("Modulation", "The point of view is not reversed; the whole notice is replaced by the usual one.")],
          "A fixed notice is replaced by the French notice for the same situation: equivalence.", "Équivalence", "Concept", "Is the usual French notice built word for word from the English?"),
        Q("Quelle phrase traduit le mieux *He swam across the river* ?",
          "Il a traversé la rivière à la nage.", [("Il a nagé à travers la rivière.", "Understandable but English in style: French prefers the direction verb."), ("Il a nagé la rivière.", "*Nager* does not take this direct object here."), ("Il a traversé nageant la rivière.", "Wrong word order for a participle.")],
          "The English manner verb (*swam*) becomes a direction verb (*traverser*) plus *à la nage*.", "Transposition du verbe de manière", "Application", "Which verb should carry the idea of crossing?"),
        Q("Traduisez : *Actually, I disagree.*",
          "En fait, je ne suis pas d'accord.", [("Actuellement, je ne suis pas d'accord.", "*Actuellement* means *currently*."), ("Éventuellement, je ne suis pas d'accord.", "*Éventuellement* means *possibly*."), ("Finalement, je ne suis pas d'accord.", "*Finalement* means *finally*, not *actually*.")],
          "*Actually* corresponds to *en fait* (or *à vrai dire*); *actuellement* is a false friend.", "Faux amis", "Application", "Is *actuellement* really *actually*?"),
        Q("Traduisez : *I went to the library.*",
          "Je suis allé à la bibliothèque.", [("Je suis allé à la librairie.", "*Librairie* means bookshop."), ("Je suis allé au bibliothèque.", "*Bibliothèque* is feminine."), ("Je suis allé à la librarie.", "Not a French word.")],
          "*Library* = *bibliothèque* (feminine). *Librairie* is a bookshop.", "Faux amis", "Recall", "What does *librairie* really mean?"),
        Q("Traduisez : *a stone wall*.",
          "un mur de pierre", [("un pierre mur", "French does not place the noun before the other, and *pierre* is feminine."), ("une pierre mur", "Same word-order error."), ("un mur pierre", "A link word (*de*) is needed.")],
          "French noun groups use *de*: *un mur de pierre*.", "Groupes nominaux", "Application", "How does French link two nouns that English places side by side?"),
        Q("*Don't forget to lock the door* devient *Pensez à fermer la porte à clé*. Quel procédé ?",
          "Modulation", [("Transposition", "The word class does not change; the viewpoint does."), ("Emprunt", "No word is borrowed."), ("Adaptation", "No cultural reference is replaced.")],
          "A negative instruction becomes a positive one: modulation.", "Modulation", "Concept", "Is there a change of viewpoint?"),
    ]))

# ================================================================== 7. Traduire les temps et le passif
SETS.append(practice_set(
    module=M2, topic="Traduire les temps et le passif", title="Temps anglais, temps français et passif",
    lesson="frl1-traduire-temps-passif",
    questions=[
        Q("Traduisez : *I have lived here for five years.* (I still live here.)",
          "J'habite ici depuis cinq ans.", [("J'ai habité ici pendant cinq ans.", "That would mean you no longer live here."), ("J'habitais ici depuis cinq ans.", "Imperfect: refers to a past point of view."), ("J'ai habité ici depuis cinq ans.", "*Depuis* does not go with the passé composé in this sense.")],
          "A situation still true: present + *depuis*.", "Depuis + présent", "Application", "Is the situation still true now?"),
        Q("Traduisez : *He has just left.*",
          "Il vient de partir.", [("Il a juste parti.", "Not French."), ("Il venait de partir.", "That means *he had just left*."), ("Il est juste parti.", "That means *he simply left*, not *has just*.")],
          "*Venir de* + infinitive translates *has just*.", "Venir de", "Recall", "Which verb expresses a very recent past?"),
        Q("Traduisez : *When you arrive, call me.*",
          "Quand tu arriveras, appelle-moi.", [("Quand tu arrives, appelle-moi.", "English uses the present, French the future after *quand*."), ("Quand tu arrivais, appelle-moi.", "Imperfect: wrong time."), ("Quand tu arriverais, appelle-moi.", "Conditional: wrong mood.")],
          "After *quand*, French keeps the future: *Quand tu arriveras*.", "Futur après quand", "Concept", "In French, what tense follows *quand* when the action is in the future?"),
        Q("Traduisez : *Every Sunday he would visit his aunt.*",
          "Chaque dimanche, il rendait visite à sa tante.", [("Chaque dimanche, il rendrait visite à sa tante.", "Conditional: here *would* expresses a habit, not a hypothesis."), ("Chaque dimanche, il a rendu visite à sa tante.", "Passé composé: a single occasion."), ("Chaque dimanche, il rendra visite à sa tante.", "Future: wrong time.")],
          "*Would* of repeated habit = imperfect.", "Would d'habitude", "Application", "Is the action a hypothesis or a repeated habit?"),
        Q("Traduisez : *English is spoken here.*",
          "Ici, on parle anglais.", [("Ici est parlé anglais.", "Not French word order or form."), ("Ici l'anglais parle.", "The language does not speak."), ("Ici anglais est parler.", "Wrong form of the verb.")],
          "Use *on* for the unspecified agent: *on parle anglais*.", "Éviter le passif", "Application", "Which pronoun replaces an unspecified agent?"),
        Q("Traduisez : *He was given a prize.*",
          "On lui a remis un prix.", [("Il a été donné un prix.", "The indirect object cannot be the subject of a French passive."), ("Il a été remis un prix.", "Same error."), ("Il a donné un prix.", "Active: changes the meaning (he gave).")],
          "The person is an indirect object (*lui*), so French uses *on*.", "Passif avec objet indirect", "Concept", "Is the person the direct or the indirect object?"),
        Q("Traduisez : *He could not open the door* (on one occasion).",
          "Il n'a pas pu ouvrir la porte.", [("Il ne savait pas ouvrir la porte.", "*Savoir* describes a learnt skill."), ("Il ne peut pas ouvrir la porte.", "Present: wrong time."), ("Il ne pourrait pas ouvrir la porte.", "Conditional: hypothetical.")],
          "Failure on one occasion in the past: passé composé of *pouvoir*.", "Could / pouvoir", "Application", "Is *could* about a single event or a skill?"),
        Q("Traduisez : *She had been waiting for an hour when I arrived.*",
          "Elle attendait depuis une heure quand je suis arrivé.", [("Elle avait attendu depuis une heure quand j'arrivais.", "Wrong tenses: imperfect with *depuis* is needed."), ("Elle a attendu depuis une heure quand j'étais arrivé.", "Tenses reversed."), ("Elle attend depuis une heure quand je suis arrivé.", "Present: wrong time.")],
          "Situation continuing up to a past moment: imperfect + *depuis*; the interrupting event: passé composé.", "Depuis + imparfait", "Application", "Which tense describes a situation that was in progress when something happened?"),
    ]))

# ================================================================== 8. Traduire les expressions idiomatiques
SETS.append(practice_set(
    module=M2, topic="Traduire les expressions idiomatiques", title="Idiomes, proverbes et collocations",
    lesson="frl1-expressions-idiomatiques",
    questions=[
        Q("Quelle traduction anglaise convient à *Il pleut des cordes* ?",
          "It is pouring with rain.", [("It is raining ropes.", "Word for word: not English."), ("Ropes are raining.", "Not English."), ("It is raining a little.", "The opposite meaning.")],
          "It is an idiom for very heavy rain; translate the meaning.", "Idiomes", "Concept", "Do not translate the image."),
        Q("Quel équivalent anglais convient à *faire d'une pierre deux coups* ?",
          "to kill two birds with one stone", [("to hit two stones", "Word for word."), ("to throw a stone twice", "Word for word."), ("to break two stones with one blow", "Word for word.")],
          "Equivalent expression with a different image: *to kill two birds with one stone*.", "Image différente", "Recall", "Is the English image the same?"),
        Q("Que signifie *vendre la mèche* ?",
          "to let the cat out of the bag", [("to sell the wick", "Word for word."), ("to sell a secret for money", "*Vendre* is part of the idiom: no money is involved."), ("to light a candle", "No connection with lighting.")],
          "*Vendre la mèche* means to reveal a secret by accident.", "Idiomes", "Concept", "What happens to a secret in this idiom?"),
        Q("Traduisez en français : *to cost an arm and a leg.*",
          "coûter les yeux de la tête", [("coûter un bras et une jambe", "Word for word: French uses another image."), ("coûter la main et le pied", "Not the French idiom."), ("coûter cher comme un œil", "Not an idiom.")],
          "The French idiom uses eyes: *coûter les yeux de la tête*.", "Équivalents idiomatiques", "Recall", "Which part of the body is used in French?"),
        Q("Traduisez en français : *Better late than never.*",
          "Mieux vaut tard que jamais.", [("Meilleur tard que jamais.", "*Meilleur* cannot replace *mieux vaut*."), ("Plus vaut tard que jamais.", "The proverb uses *mieux*."), ("Mieux vaut jamais que tard.", "The meaning is reversed.")],
          "The standard proverb uses *mieux vaut ... que*.", "Proverbes", "Recall", "Which verb is in the structure *mieux vaut prévenir que guérir*?"),
        Q("Que signifie *poser un lapin à quelqu'un* ?",
          "to stand someone up", [("to give someone a rabbit", "Word for word."), ("to ask someone a question", "*Poser* is part of the idiom, not *ask*."), ("to put someone in a cage", "No connection.")],
          "The idiom means to fail to meet someone as arranged.", "Idiomes", "Concept", "Think of a missed appointment."),
        Q("Traduisez : *to take an exam.*",
          "passer un examen", [("prendre un examen", "A literal collocation error."), ("porter un examen", "Not French."), ("tenir un examen", "Not the usual collocation.")],
          "French collocation: *passer un examen*.", "Collocations", "Recall", "Which verb does French use with exams?"),
        Q("Traduisez : *He has a frog in his throat.*",
          "Il a un chat dans la gorge.", [("Il a une grenouille dans la gorge.", "Word for word: not the French idiom."), ("Il a un chien dans la gorge.", "Not an idiom."), ("Il a un chat sur la gorge.", "Wrong preposition and not the idiom.")],
          "The French idiom uses a cat: *avoir un chat dans la gorge*.", "Équivalents idiomatiques", "Application", "Which animal does the French idiom use?"),
    ]))

# ================================================================== 9. Le thème
SETS.append(practice_set(
    module=M2, topic="Le thème", title="Thème : pièges de l'anglais vers le français",
    lesson="frl1-theme",
    questions=[
        Q("Traduisez : *He is a doctor.*",
          "Il est médecin.", [("Il est un médecin.", "No article before a profession after *être* (in this neutral statement)."), ("Il a médecin.", "Wrong verb."), ("Il fait médecin.", "Not French here.")],
          "Profession after *être* takes no article: *Il est médecin.*", "Articles et professions", "Recall", "Does French use an article after *être* with a profession?"),
        Q("Traduisez : *She is thirty.*",
          "Elle a trente ans.", [("Elle est trente ans.", "Age uses *avoir*, not *être*."), ("Elle a trente années.", "*Ans* is the word used for age."), ("Elle a trente.", "The noun *ans* is required.")],
          "Age uses *avoir* + *ans*.", "Âge avec avoir", "Recall", "Which verb gives age in French?"),
        Q("Traduisez : *I am cold.*",
          "J'ai froid.", [("Je suis froid.", "That would mean you are a cold person."), ("Je fais froid.", "*Faire froid* is for the weather."), ("Il fait froid.", "That says the weather is cold.")],
          "Feelings use *avoir*: *J'ai froid.*", "Sensations avec avoir", "Concept", "Is the cold in you or in the weather?"),
        Q("Traduisez : *Most people prefer to travel by road.*",
          "La plupart des gens préfèrent voyager par la route.", [("Plupart gens préfère voyager sur route.", "Article and plural verb missing."), ("Les plus gens préfèrent voyager par la route.", "*Les plus gens* is not French for *most people*."), ("La plupart des gens préfère voyager par la route.", "After *la plupart des* the verb is plural: *préfèrent*.")],
          "*La plupart des* + plural noun takes a plural verb.", "La plupart des", "Application", "What is the fixed French expression for *most*?"),
        Q("Traduisez : *I live in Cameroon.*",
          "J'habite au Cameroun.", [("J'habite en Cameroun.", "*Cameroun* is masculine: *au*."), ("J'habite à Cameroun.", "*À* is for towns."), ("J'habite dans Cameroun.", "Wrong preposition without an article.")],
          "Masculine country: *au Cameroun*; feminine: *en France*; town: *à Douala*.", "Prépositions de lieu", "Recall", "Is *Cameroun* masculine or feminine?"),
        Q("Traduisez : *On Mondays we go to the market.*",
          "Le lundi, nous allons au marché.", [("Lundi, nous allons au marché.", "Without article it means one particular Monday."), ("Aux lundis, nous allons au marché.", "Not French."), ("Le lundis, nous allons au marché.", "Days do not take an *-s* in this use.")],
          "A habit on a day: *le lundi*.", "Jours de la semaine", "Application", "Is the habit repeated (every Monday) or a single Monday?"),
        Q("Traduisez : *We have been studying French for three years.*",
          "Nous étudions le français depuis trois ans.", [("Nous avons étudié le français pour trois ans.", "*Pour* does not give the duration of a continuing action."), ("Nous étudiions le français depuis trois ans.", "Imperfect: wrong time."), ("Nous étudions le français pour trois ans.", "Wrong preposition.")],
          "Present + *depuis* for an action continuing now.", "Depuis + présent", "Application", "Is the study still going on?"),
        Q("Traduisez : *If prices fell, families would buy more.*",
          "Si les prix baissaient, les familles achèteraient davantage.", [("Si les prix baisseraient, les familles achèteraient davantage.", "Never a conditional after *si*."), ("Si les prix baissent, les familles achèteraient davantage.", "Mismatch: *si* + présent needs the future."), ("Si les prix baisseraient, les familles achetaient davantage.", "Wrong tenses in both clauses.")],
          "Imaginary condition: *si* + imparfait, conditionnel présent.", "Si + imparfait", "Application", "What tense follows *si* when the condition is imaginary?"),
    ]))

# ================================================================== 10. La version
SETS.append(practice_set(
    module=M2, topic="La version", title="Version : du français à l'anglais naturel",
    lesson="frl1-version",
    questions=[
        Q("Traduisez en anglais : *Il a failli tomber.*",
          "He nearly fell.", [("He failed to fall.", "*Faillir* does not mean *fail to*."), ("He fell.", "He did not fall."), ("He had to fall.", "It does not express obligation.")],
          "*Faillir* + infinitive means *nearly*.", "Faillir", "Concept", "Did he fall?"),
        Q("Traduisez en anglais : *Cela fait deux ans qu'elle habite ici.*",
          "She has lived here for two years.", [("She lived here two years ago.", "That would be *il y a deux ans*."), ("It makes two years that she lives here.", "Word for word."), ("She will live here for two years.", "The French is in the present.")],
          "*Cela fait ... que* + present = *for* with a perfect tense.", "Cela fait... que", "Application", "Is the situation continuing?"),
        Q("Traduisez en anglais : *Il est parti il y a trois jours.*",
          "He left three days ago.", [("He leaves in three days.", "The French is in the past."), ("He has left for three days.", "*Il y a* + time means *ago*."), ("There are three days that he left.", "Word for word.")],
          "*Il y a* with a time expression means *ago*.", "Il y a = ago", "Recall", "What does *il y a trois jours* mean?"),
        Q("Traduisez en anglais : *Elle ouvrit la porte et vit un étranger.*",
          "She opened the door and saw a stranger.", [("She opens the door and sees a stranger.", "The French is in the past (passé simple)."), ("She was opening the door and was seeing a stranger.", "The passé simple is a completed action."), ("She had opened the door and had seen a stranger.", "The passé simple is not a pluperfect.")],
          "Passé simple = simple past in English.", "Passé simple", "Recall", "Which English tense matches the passé simple?"),
        Q("Traduisez en anglais : *Il doit être malade.*",
          "He must be ill.", [("He has to be ill.", "Not natural English for a deduction."), ("He was supposed to be ill.", "That is *Il devait être malade*."), ("He owes illness.", "Word for word.")],
          "*Devoir* + *être* expresses deduction: *must be*.", "Devoir", "Concept", "Is it an obligation or a guess?"),
        Q("Traduisez en anglais : *Actuellement, il étudie à Douala.*",
          "Currently, he is studying in Douala.", [("Actually, he studies in Douala.", "*Actuellement* is not *actually*."), ("Eventually, he studies in Douala.", "False friend."), ("Possibly, he studies in Douala.", "Not the meaning.")],
          "*Actuellement* = *currently*.", "Faux amis", "Recall", "Does *actuellement* mean *really*?"),
        Q("Traduisez en anglais : *Il ne reste que deux jours.*",
          "Only two days remain.", [("Two days do not remain.", "*Ne ... que* is not a plain negation."), ("Not even two days remain.", "Opposite emphasis."), ("There remain no two days.", "Not English.")],
          "*Ne ... que* means *only*.", "Ne ... que", "Concept", "Does *que* here restrict or deny?"),
        Q("Traduisez en anglais : *Il s'est fait voler son téléphone.*",
          "He had his phone stolen.", [("He stole his phone.", "He is the victim."), ("He made himself steal the phone.", "Word for word."), ("He did his phone steal.", "Not English.")],
          "*Se faire* + infinitive here is a passive of misfortune: *he had his phone stolen*.", "Se faire + infinitif", "Application", "Who is the victim?"),
    ]))
