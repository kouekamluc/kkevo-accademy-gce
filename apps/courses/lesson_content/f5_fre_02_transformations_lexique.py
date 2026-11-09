"""Form 5 French (O Level 0545), modules "Transformations Syntaxiques" and "Lexique Thématique et Vie Quotidienne".
Draft content: check against the official syllabus and your textbook."""

from .dsl import *  # noqa: F403

COURSE = ("french", "form-5")

M3 = "Transformations Syntaxiques"
M4 = "Lexique Thématique et Vie Quotidienne"

LESSONS = []


def BANK(title, rows):
    """Aligned word bank. rows = (French, gender or type, English). m = masculine noun, f = feminine noun, mf = same form for both, v = verb, - = phrase."""
    w = max(len(r[0]) for r in rows)
    lines = [f"{fr.ljust(w)}  {g.ljust(2)}  {en}" for fr, g, en in rows]
    return CODE(chr(10).join(lines), "text", title=title)

# ---------------------------------------------------------------------- 1. Negative structures
LESSONS += [
    lesson(
        module=M3, topic="Negative structures",
        title="Negative structures: ne ... pas, jamais, plus, rien, personne, aucun",
        slug="fr2-negative-structures", minutes=24,
        summary="French negation wraps the verb in two parts: ne ... pas, jamais, plus, rien, personne, aucun. Learn where the two parts go in simple and compound tenses, after infinitives, and why un, une, des, du become de.",
        objectives=[
            "Form the negative with ne ... pas, jamais, plus, rien, personne, aucun and ne ... que",
            "Place the two parts correctly in simple tenses, compound tenses and with an infinitive",
            "Change un, une, des, du, de la to de (d') after a negation",
            "Use rien, personne and aucun as subjects and as objects",
        ],
        key_concepts=["Négation", "ne ... pas", "ne ... jamais", "ne ... plus", "rien", "personne", "aucun", "de après la négation"],
        blocks=[
            H("Introduction"),
            T("Awa vend des tomates au marché de Mokolo. Un client lui demande : « Vous avez des tomates ? » "
              "Elle répond : « Non, je n'ai pas de tomates aujourd'hui. » Elle ne dit pas seulement « pas » : "
              "elle entoure le verbe avec deux petits mots, **ne** et **pas**."),
            T("In English we add one word (*do not*, *never*, *nobody*). In French, a negative sentence normally has two parts "
              "that go around the verb. In Paper 1 multiple choice questions you must choose the sentence where both parts are in the right place. "
              "This lesson gives you the pattern."),
            H("The two-part negation"),
            D("The **négation** is formed with **ne** (before a vowel or a mute h: **n'**) placed before the verb, and a second word placed after it. "
              "The second word decides the meaning.", title="Definition"),
            CODE("""ne ... pas       not                  Je ne parle pas anglais.
ne ... jamais    never                Il n'arrive jamais en retard.
ne ... plus      no longer, no more   Elle ne travaille plus à Douala.
ne ... rien      nothing              Je ne vois rien.
ne ... personne  nobody, no one       Nous n'attendons personne.
ne ... aucun(e)  no, not any          Il n'a aucun ami ici.
ne ... pas encore  not yet            Le car n'est pas encore arrivé.
ne ... que       only (not a real negation)   Je n'ai que mille francs.""", "text", title="The main negative pairs"),
            KEY("Pairs of opposites", "Each negative word cancels a positive word. This helps you build the negative of a sentence.", cards=[
                ["toujours, souvent", "→ ne ... jamais"],
                ["encore (still), toujours (still)", "→ ne ... plus"],
                ["déjà (already)", "→ ne ... pas encore"],
                ["quelque chose", "→ ne ... rien"],
                ["quelqu'un", "→ ne ... personne"],
                ["un, une, des, plusieurs, tous", "→ ne ... aucun(e) or ne ... pas de"],
            ]),
            H("Where do the two parts go?"),
            T("In a **simple tense** (présent, imparfait, futur, conditionnel), **ne** goes before the verb and the second word after it. "
              "Object pronouns (le, la, lui, en, y ...) stay between **ne** and the verb: "
              "*Je ne le vois pas. Elle n'en veut plus.*"),
            T("In a **compound tense** (passé composé, plus-que-parfait ...), the two parts go around the **auxiliary**, not around the whole verb: "
              "*Il n'a pas mangé. Nous ne sommes jamais allés à Kribi.* "
              "Exception: **personne** and **aucun** come after the past participle: *Je n'ai vu personne. Elle n'a lu aucun livre.*"),
            T("With an **infinitive**, both parts normally go together before it: *Je préfère ne pas partir. Il a décidé de ne jamais revenir. "
              "Elle promet de ne rien dire.* Again, **personne** comes after: *Je préfère ne voir personne.* "
              "In the **imperative**, the pattern is the same as for a simple tense: *Ne mange pas ! Ne le fais plus !*"),
            CODE("""Présent             Il ne mange pas de viande.
Passé composé       Il n'a pas mangé de viande.
Passé composé       Il n'a rien mangé.        (rien before the participle)
Passé composé       Il n'a vu personne.       (personne after the participle)
Infinitif           Il préfère ne rien manger.
Impératif           Ne mange rien !""", "text", title="Position summary"),
            H("De after a negation"),
            D("After a negation, the indefinite articles **un, une, des** and the partitive articles **du, de la, de l'** become **de** "
              "(**d'** before a vowel). The definite articles **le, la, les** do not change.",
              title="Rule", formula=""),
            CODE("""J'ai un frère.            →  Je n'ai pas de frère.
Elle mange du pain.       →  Elle ne mange pas de pain.
Il y a des élèves.        →  Il n'y a pas d'élèves.
J'aime le manioc.         →  Je n'aime pas le manioc.   (le does not change)
C'est un problème.        →  Ce n'est pas un problème.  (after être: no change)""", "text", title="Articles in the negative"),
            T("Two exceptions: after the verb **être**, un/une/des stay as they are (*Ce n'est pas un problème*), "
              "and with **ne ... que** the article does not change (*Je n'ai que des amis ici*)."),
            H("Rien, personne, aucun as subject"),
            T("**Rien**, **personne** and **aucun** can also be the subject of the sentence. Then they come first and **ne** comes before the verb. "
              "There is no **pas**: *Personne ne vient. Rien ne change. Aucun élève n'est absent.*"),
            EX("Worked example 1: du and des after a negation",
               intro="Make this sentence negative: « Nous avons mangé du poisson hier. »",
               steps=[
                   S("Find the verb group", text="avons mangé is the passé composé. The auxiliary is avons."),
                   S("Put ne ... pas around the auxiliary", text="Nous n'avons pas mangé ... (ne becomes n' before avons)."),
                   S("Change the article", text="After the negation, du becomes de: pas de poisson."),
                   S("Write the sentence", text="Nous n'avons pas mangé de poisson hier."),
               ], check=""),
            EX("Worked example 2: personne after the participle",
               intro="Make this sentence negative: « Quelqu'un a vu le directeur. » and « J'ai vu quelqu'un. »",
               steps=[
                   S("First sentence: quelqu'un is the subject", text="Its opposite as a subject is Personne. Put ne before the verb: Personne n'a vu le directeur."),
                   S("Second sentence: quelqu'un is the object", text="Use ne ... personne. The auxiliary takes ne: Je n'ai ..."),
                   S("Place personne after the participle", text="Je n'ai vu personne."),
               ], check=""),
            EX("Worked example 3: an infinitive",
               intro="Make the verb in the infinitive negative: « Elle décide de répondre à quelqu'un. » (she decides not to answer anyone)",
               steps=[
                   S("Negate the infinitive", text="Both parts go before the infinitive, except personne."),
                   S("Choose the negative word", text="quelqu'un becomes personne, which goes after the infinitive."),
                   S("Write", text="Elle décide de ne répondre à personne."),
               ]),
            MISTAKE("Wrong order: « Je ne pas parle »",
                    "The second word never comes before the verb (except for personne, rien and aucun as subjects). Write: Je ne parle pas. "
                    "In a compound tense, remember it goes after the auxiliary: Je n'ai pas parlé."),
            MISTAKE("Forgetting ne",
                    "In everyday speech, many French speakers say « Je sais pas ». In written French and in exam answers, ne is required: Je ne sais pas."),
            MISTAKE("« Je n'ai pas des amis » or « Je ne vois pas personne »",
                    "After a negation, des becomes de: Je n'ai pas d'amis. Also, rien, personne and aucun already carry the negative meaning: "
                    "do not add pas. Write: Je ne vois personne."),
            QUIZ("Which sentence is the correct negative of « J'ai une voiture » ?",
                 ["Je n'ai pas une voiture.", "Je n'ai pas de voiture.", "Je ne pas ai de voiture.", "Je n'ai de voiture pas."], 1,
                 "After a negation, une becomes de: Je n'ai pas de voiture.",
                 hint="Look at the article after the negation.",
                 feedback=["Une must become de after ne ... pas.", "", "ne and pas go around the auxiliary ai, they do not both come before it.", "pas goes right after the verb ai, before de voiture."]),
            QUIZ("Choose the correct negative of « Il a invité quelqu'un. »",
                 ["Il n'a invité personne.", "Il n'a personne invité.", "Il n'a pas invité personne.", "Il ne personne a invité."], 0,
                 "Personne comes after the past participle, and no pas is added.",
                 hint="Remember that personne goes after the participle in the passé composé.",
                 feedback=["", "Personne goes after the participle: invité personne.", "Personne already carries the negative meaning, so pas is not added.", "Personne cannot stand between ne and the auxiliary here."]),
            TIP("In Paper 1 multiple choice, the wrong options often change the position of the negative words, keep a des or du after the negation, or add pas to personne or rien. "
                "Check these three things in every option. Negation also helps you in the essay: it is part of the language accuracy that the Board's examiners assess.", title="Exam link"),
            PQ("Make this sentence negative: « Mon père boit du café le matin. »", "Mon père ne boit pas de café le matin. (ne ... pas around boit, du becomes de.)"),
            PQ("Make this sentence negative: « Quelqu'un frappe à la porte. »", "Personne ne frappe à la porte. (personne is the subject, with ne before the verb and no pas.)"),
            PQ("Answer in the negative using ne ... plus: « Elle travaille encore à Bafoussam ? »", "Elle ne travaille plus à Bafoussam. (encore becomes ne ... plus.)"),
            PQ("Make the passé composé negative: « Nous sommes allés à Kribi. » (never)", "Nous ne sommes jamais allés à Kribi. (ne ... jamais around the auxiliary sommes.)"),
            SUM("A French negative sentence normally has two parts around the verb: ne + pas, jamais, plus, rien, personne or aucun.",
                "In compound tenses the two parts go around the auxiliary; personne and aucun go after the participle. With an infinitive, both parts come before it.",
                "After a negation, un, une, des, du and de la become de (d'), except after être.",
                "Rien, personne and aucun can be subjects: Personne ne vient. They never take pas."),
        ],
    ),
]

# ---------------------------------------------------------------------- 2. Interrogative forms (yes/no)
LESSONS += [
    lesson(
        module=M3, topic="Interrogative forms",
        title="Yes/no questions: intonation, est-ce que and inversion",
        slug="fr2-yes-no-questions", minutes=22,
        summary="A yes/no question can be asked by intonation, with est-ce que, or by inversion of verb and pronoun. Learn the hyphen, the -t- of liaison, inversion with a noun subject, with compound tenses and with the negative.",
        objectives=[
            "Ask a yes/no question in three ways: intonation, est-ce que and inversion",
            "Form inversion correctly with the hyphen and the -t- (A-t-il, Parle-t-elle)",
            "Invert a noun subject with a pronoun (Paul a-t-il fini ?) and in compound tenses",
            "Answer a negative question with si",
        ],
        key_concepts=["Question totale", "Intonation", "Est-ce que", "Inversion", "-t- de liaison", "Si"],
        blocks=[
            H("Introduction"),
            T("Dans un taxi à Yaoundé, un passager demande : « Est-ce que vous allez à Mvog-Mbi ? » Le chauffeur répond : « Oui, montez ! » "
              "The question can be answered by *oui* or *non*. We call it a **question totale**, a yes/no question."),
            T("In Paper 1 multiple choice, you may have to choose the correct question form or turn a statement into a question. "
              "French has three ways of doing this, and each one has its own register: casual, neutral and formal."),
            H("Three ways to ask"),
            D("A **question totale** is a question whose answer is *oui*, *non* or *si*. It can be formed by (1) **intonation**: "
              "the voice rises at the end, (2) **est-ce que** placed before the statement, (3) **inversion**: the subject pronoun goes after the verb, joined by a hyphen.",
              title="Definition"),
            CODE("""Intonation   Vous parlez anglais ?             (spoken, informal)
Est-ce que   Est-ce que vous parlez anglais ?   (everyday, neutral)
Inversion    Parlez-vous anglais ?              (written, formal)""", "text", title="The same question, three ways"),
            T("In writing, always put the question mark at the end. Note that French puts a space before **?** in careful typing: *Parlez-vous anglais ?*"),
            T("**Est-ce que** becomes **est-ce qu'** before a vowel: *Est-ce qu'il vient ? Est-ce qu'elle a faim ?* "
              "The statement after it keeps its normal word order."),
            H("Inversion step by step"),
            T("In inversion, the **subject pronoun** moves after the verb and is joined to it by a **hyphen**: *Tu as faim ?* becomes *As-tu faim ?* "
              "The pronouns used are: je (rare, only a few verbs), tu, il, elle, on, nous, vous, ils, elles."),
            D("When the verb ends in a vowel (-e or -a) and the pronoun is **il, elle or on**, add a **-t-** between the verb and the pronoun "
              "so that the two vowels are easy to say: *Parle-t-il ? A-t-elle ? Va-t-on ?* "
              "If the verb already ends in -t or -d, do not add another t: *Est-il ? Prend-elle ?*",
              title="The -t- of liaison"),
            CODE("""Il mange du riz.          →  Mange-t-il du riz ?
Elle a un frère.          →  A-t-elle un frère ?
On va au marché.          →  Va-t-on au marché ?
Il est malade.            →  Est-il malade ?
Elle prend le bus.        →  Prend-elle le bus ?
Ils arrivent demain.      →  Arrivent-ils demain ?""", "text", title="Inversion with il, elle, on, ils"),
            H("Noun subjects and compound tenses"),
            T("With a **noun subject**, the noun stays in front and a matching pronoun is added after the verb: "
              "*Paul parle anglais.* becomes *Paul parle-t-il anglais ?* *Les élèves sont partis.* becomes *Les élèves sont-ils partis ?* "
              "Do not invert the noun itself."),
            T("In a **compound tense**, only the auxiliary and the pronoun are inverted. The past participle stays after them: "
              "*Tu as mangé.* becomes *As-tu mangé ?* *Elle est arrivée.* becomes *Est-elle arrivée ?*"),
            T("In the **negative**, ne ... pas goes around the verb-pronoun group: *Ne parle-t-il pas anglais ? N'as-tu pas faim ? "
              "N'est-elle pas venue ?*"),
            KEY("Answering a negative question", "When a question is negative, the answer « yes » is **si**, not oui.", cards=[
                ["Tu n'as pas faim ?", "Si, j'ai faim. (Yes, I am hungry.)"],
                ["Tu n'as pas faim ?", "Non, je n'ai pas faim. (No, I am not hungry.)"],
                ["Tu as faim ?", "Oui, j'ai faim. (positive question: oui)"],
            ]),
            EX("Worked example 1: three forms",
               intro="Write « Vous habitez à Douala. » as a question in the three ways.",
               steps=[
                   S("Intonation", text="Keep the order and add a question mark: Vous habitez à Douala ?"),
                   S("Est-ce que", text="Put it before the statement: Est-ce que vous habitez à Douala ?"),
                   S("Inversion", text="Move vous after the verb with a hyphen: Habitez-vous à Douala ?"),
               ]),
            EX("Worked example 2: a noun subject",
               intro="Make a question with inversion: « Le directeur est arrivé. »",
               steps=[
                   S("Identify the subject", text="le directeur, which is a noun. It stays in front."),
                   S("Choose the pronoun", text="le directeur is masculine singular, so the pronoun is il."),
                   S("Invert the auxiliary and the pronoun", text="est-il: est already ends with t, so no extra -t-."),
                   S("Write the question", text="Le directeur est-il arrivé ?"),
               ]),
            EX("Worked example 3: negative inversion",
               intro="Make a question with inversion: « Elle n'a pas fini. »",
               steps=[
                   S("Invert the auxiliary and the pronoun", text="a-t-elle: a ends with a vowel, and the pronoun is elle, so we add -t-."),
                   S("Put ne ... pas around the group", text="N'a-t-elle pas ..."),
                   S("Add the participle", text="N'a-t-elle pas fini ?"),
               ]),
            MISTAKE("Missing -t- : « Parle-il ? »",
                    "A verb ending in -e or -a followed by il, elle or on needs -t-: Parle-t-il ? A-t-elle ? Aime-t-on ? "
                    "Without it, two vowels meet. For the other persons there is no -t-: Parles-tu ? Parlez-vous ?"),
            MISTAKE("Mixing two question forms: « Est-ce que parles-tu ? »",
                    "Est-ce que already makes a question, so do not invert as well. Write Est-ce que tu parles ? or Parles-tu ?"),
            MISTAKE("Answering a negative question with oui",
                    "To contradict a negative question, say si: « Tu ne viens pas ? » « Si, je viens. »"),
            QUIZ("Which question is correctly formed with inversion?",
                 ["Mange-il du riz ?", "Mange-t-il du riz ?", "Il mange-t-il du riz ?", "Est-ce que mange-t-il du riz ?"], 1,
                 "A verb ending in -e followed by il takes -t-: Mange-t-il du riz ?",
                 hint="Look at the end of the verb mange.",
                 feedback=["Two vowels meet: add -t- between mange and il.", "", "The subject is repeated: il appears twice.", "Do not combine est-ce que with inversion."]),
            QUIZ("« Tu ne viens pas à la fête ? » What is the correct answer meaning « Yes, I am coming » ?",
                 ["Oui, je viens.", "Si, je viens.", "Non, je viens.", "Si, je ne viens pas."], 1,
                 "Si is the answer « yes » to a negative question.",
                 hint="The question is negative.",
                 feedback=["Oui answers a positive question.", "", "Non would mean you are not coming.", "Si contradicts the negative, so the verb is positive."]),
            TIP("In Paper 1 multiple choice, look for the option with the hyphen and the -t- in the right place, and reject options with two question markers "
                "(est-ce que + inversion). In the essay and the translation, inversion is also useful for questions inside dialogue.", title="Exam link"),
            PQ("Turn into a question with est-ce que: « Tu aimes le football. »", "Est-ce que tu aimes le football ?"),
            PQ("Turn into a question with inversion: « Elle a un frère. »", "A-t-elle un frère ? (a ends in a vowel, elle follows: add -t-.)"),
            PQ("Turn into a question with inversion: « Les élèves sont partis. »", "Les élèves sont-ils partis ? (noun kept in front, pronoun ils added after the auxiliary.)"),
            PQ("Write with inversion: « Vous ne venez pas. » and say how you answer « yes ».", "Ne venez-vous pas ? The answer « yes » is Si, je viens."),
            SUM("Yes/no questions: intonation (informal), est-ce que (neutral), inversion (formal).",
                "Inversion joins verb and pronoun with a hyphen; add -t- after a vowel before il, elle, on: Parle-t-il ?",
                "With a noun subject, keep the noun and add the pronoun: Paul parle-t-il ? In compound tenses invert the auxiliary only.",
                "In the negative, wrap the group: N'as-tu pas faim ? The answer « yes » to a negative question is si."),
        ],
    ),
]

# ---------------------------------------------------------------------- 3. Interrogative words
LESSONS += [
    lesson(
        module=M3, topic="Interrogative forms",
        title="Questions with interrogative words: qui, que, où, quand, comment, pourquoi, combien, quel",
        slug="fr2-question-words", minutes=24,
        summary="Question words ask for information: who, what, where, when, how, why, how much, which. Learn qui, que/quoi, où, quand, comment, pourquoi, combien and quel, and build the question with est-ce que or inversion.",
        objectives=[
            "Choose the right question word from the information being asked for",
            "Form questions with qui, que/qu'est-ce que, quoi, où, quand, comment, pourquoi, combien (de)",
            "Make quel agree with its noun (quel, quelle, quels, quelles)",
            "Place a noun subject correctly after a question word",
        ],
        key_concepts=["Mot interrogatif", "Qui", "Que / quoi", "Où, quand, comment, pourquoi", "Combien de", "Quel / quelle / quels / quelles"],
        blocks=[
            H("Introduction"),
            T("À la gare routière de Bafoussam, une voyageuse demande : « À quelle heure part le car pour Douala ? » "
              "Le vendeur répond : « À huit heures. » Elle voulait connaître l'**heure**: she asked for a piece of information, "
              "so she used a question word."),
            T("When the answer is not simply *oui* or *non*, we use an **interrogative word**. "
              "In Paper 1 multiple choice you may have to complete a question with the right word, or find the question that fits an answer."),
            H("The main question words"),
            CODE("""qui              who, whom             Qui est cet homme ?
que / qu'        what                  Que fais-tu ?
quoi             what (after a preposition or informal)   De quoi parles-tu ?
où               where                 Où habites-tu ?
quand            when                  Quand arrive le car ?
comment          how                   Comment vas-tu ?
pourquoi         why                   Pourquoi pleures-tu ?
combien (de)     how much, how many    Combien de frères as-tu ?
quel, quelle     which, what           Quelle heure est-il ?
quels, quelles   which, what (plural)  Quels livres lis-tu ?""", "text", title="Interrogative words"),
            KEY("What does the answer tell you?", "To choose the question word, look at the information in the answer.", cards=[
                ["A person → qui", "Mon frère est venu. → Qui est venu ?"],
                ["A thing → que / qu'est-ce que", "Je mange du riz. → Que manges-tu ?"],
                ["A place → où", "J'habite à Garoua. → Où habites-tu ?"],
                ["A time → quand", "Il part demain. → Quand part-il ?"],
                ["A manner → comment", "Elle voyage en car. → Comment voyage-t-elle ?"],
                ["A reason → pourquoi", "Parce que j'ai faim. → Pourquoi manges-tu ?"],
                ["A number or price → combien", "Il coûte mille francs. → Combien coûte-t-il ?"],
            ]),
            H("Three patterns"),
            T("For most question words you can choose between **est-ce que** and **inversion** (see the previous lesson). "
              "The informal spoken French puts the question word at the end (*Tu habites où ?*), but you should avoid it in writing."),
            CODE("""Est-ce que     Où est-ce que tu habites ?       Quand est-ce que le car part ?
Inversion      Où habites-tu ?                  Quand le car part-il ?
Informal       Tu habites où ?""", "text", title="Same question, three styles"),
            T("With a **noun subject**, there are two safe forms: noun + verb-pronoun (*Quand le car part-il ?*), or noun after the verb with **où, quand, comment, combien**, "
              "if the verb has no object (*Où habite ton oncle ? Quand arrive le car ?*). After **pourquoi**, use the pronoun form: *Pourquoi Paul est-il parti ?*"),
            H("Qui, que and quoi"),
            D("**Qui** asks about a person. As the subject there is no inversion: *Qui chante ?* As an object, you invert or use est-ce que: "
              "*Qui vois-tu ? Qui est-ce que tu vois ?* "
              "**Que** (**qu'**) asks about a thing and is the object: *Que fais-tu ? Qu'est-ce que tu fais ?* "
              "For a thing as the subject, only one long form exists: *Qu'est-ce qui se passe ?*",
              title="Who and what"),
            T("After a **preposition**, que is replaced by **quoi**, and qui stays qui: *De quoi parles-tu ? À quoi penses-tu ? Avec qui travailles-tu ? Pour qui est ce cadeau ?*"),
            H("Quel and combien"),
            D("**Quel** is an adjective meaning *which* or *what*. It agrees with the noun that follows or with the subject after être: "
              "*quel* (masc. sing.), *quelle* (fem. sing.), *quels* (masc. pl.), *quelles* (fem. pl.).",
              title="Quel agrees"),
            CODE("""Quel âge as-tu ?               (âge: masculine singular)
Quelle heure est-il ?          (heure: feminine singular)
Quels livres lis-tu ?          (livres: masculine plural)
Quelles matières préfères-tu ? (matières: feminine plural)
Quelle est ta ville ?          (quelle agrees with ville)""", "text", title="Quel in use"),
            T("**Combien** is followed by **de** and a noun without an article: *Combien de frères as-tu ? Combien d'élèves sont absents ?* "
              "With a verb alone, no de: *Combien coûte ce pain ?*"),
            EX("Worked example 1: find the question",
               intro="The answer is « Je travaille à Limbé. » Write the question with inversion for tu.",
               steps=[
                   S("What information is given?", text="A place: à Limbé. So the question word is où."),
                   S("Write the statement for tu", text="Tu travailles à Limbé."),
                   S("Invert the verb and the pronoun", text="Où travailles-tu ?"),
                   S("Alternative", text="With est-ce que: Où est-ce que tu travailles ?"),
               ]),
            EX("Worked example 2: que, qu'est-ce que or quoi",
               intro="Ask a question about the thing: « Vous cherchez un stylo. » Then ask « about what » with the preposition: « Vous parlez de la fête. »",
               steps=[
                   S("The thing is the object of cherchez", text="Use que: Que cherchez-vous ? or Qu'est-ce que vous cherchez ?"),
                   S("Second sentence has a preposition (de)", text="Que becomes quoi after a preposition."),
                   S("Write", text="De quoi parlez-vous ? (not De que parlez-vous ?)"),
               ]),
            EX("Worked example 3: quel agrees",
               intro="Complete: « ___ matières préfères-tu ? » and « ___ heure est-il ? »",
               steps=[
                   S("Find the noun and its gender and number", text="matières is feminine plural. heure is feminine singular."),
                   S("Choose the form", text="feminine plural: quelles. feminine singular: quelle."),
                   S("Write", text="Quelles matières préfères-tu ? Quelle heure est-il ?"),
               ]),
            MISTAKE("« De que parles-tu ? »",
                    "After a preposition you must use quoi: De quoi parles-tu ? Que is used only without a preposition."),
            MISTAKE("« Qu'est-ce que tu fais-tu ? »",
                    "Qu'est-ce que already makes the question, so there is no inversion: Qu'est-ce que tu fais ? or Que fais-tu ?"),
            MISTAKE("Forgetting to make quel agree",
                    "Quel changes with the noun: quelle heure, quels livres, quelles matières. "
                    "Also, do not confuse pourquoi (the question) with parce que (the answer)."),
            QUIZ("Which question matches the answer « Elle revient demain » ?",
                 ["Où revient-elle ?", "Quand revient-elle ?", "Comment revient-elle ?", "Pourquoi revient-elle ?"], 1,
                 "Demain is a time, so the question word is quand.",
                 hint="What kind of information is « demain » ?",
                 feedback=["Où asks for a place.", "", "Comment asks for the manner.", "Pourquoi asks for a reason."]),
            QUIZ("Complete: « ___ élèves sont absents aujourd'hui ? »",
                 ["Combien", "Combien de", "Quels", "Qui"], 1,
                 "Combien is followed by de and a noun: Combien d'élèves (de + élèves becomes d'élèves).",
                 hint="Combien needs a link before a noun.",
                 feedback=["Combien alone cannot be followed directly by a noun.", "", "Quels needs a noun and means « which ».", "Qui asks about a person and does not count."]),
            TIP("In Paper 1 multiple choice, the question word is often the whole test: choose the word that matches the answer, or the form of quel that agrees with the noun. "
                "Also check whether a preposition forces quoi.", title="Exam link"),
            PQ("Write the question with inversion (tu) that fits the answer: « J'habite à Garoua. »", "Où habites-tu ? (the answer gives a place.)"),
            PQ("Complete with the correct form of quel: « ___ âge a ta sœur ? »", "Quel âge a ta sœur ? (âge is masculine singular.)"),
            PQ("Ask about the thing: « Vous parlez de la fête. » (use the preposition)", "De quoi parlez-vous ? (quoi after the preposition de.)"),
            PQ("Ask why Paul is absent, using the pronoun form: « Paul est absent. »", "Pourquoi Paul est-il absent ? (after pourquoi, keep the noun and add the pronoun il.)"),
            SUM("Choose the question word from the information asked: qui (person), que (thing), où (place), quand (time), comment (manner), pourquoi (reason), combien de (quantity).",
                "Use est-ce que or inversion, but not both. After a preposition, que becomes quoi.",
                "Quel agrees with the noun: quel, quelle, quels, quelles.",
                "Combien is followed by de + noun, without article. Qui as subject needs no inversion."),
        ],
    ),
]

# ---------------------------------------------------------------------- 4. Active and passive voice
LESSONS += [
    lesson(
        module=M3, topic="Active and passive voice",
        title="Active and passive voice: être + past participle",
        slug="fr2-active-passive", minutes=24,
        summary="In the passive, the object of the active sentence becomes the subject: être in the same tense + the past participle (agreeing with the new subject) + par or de + the agent. Only verbs with a direct object can be made passive.",
        objectives=[
            "Turn an active sentence into the passive and back, keeping the same tense",
            "Form the passive in the présent, imparfait, passé composé, futur, plus-que-parfait and conditionnel",
            "Make the past participle agree with the new subject",
            "Choose par or de for the agent, and rewrite sentences with on",
        ],
        key_concepts=["Voix active", "Voix passive", "Complément d'agent", "être + participe passé", "Accord du participe", "par / de"],
        blocks=[
            H("Introduction"),
            T("Lisez ces deux phrases : « Le directeur félicite les élèves. » et « Les élèves sont félicités par le directeur. » "
              "They tell the same story, but the focus changes. In the first, the director acts. In the second, we look at the pupils who receive the action."),
            T("In Paper 1 multiple choice you may have to find the correct passive of a sentence. "
              "The test is almost always the same: the right tense of **être** and the right agreement of the participle."),
            H("Active and passive"),
            D("In the **active voice** the subject does the action: *La directrice félicite les élèves.* "
              "In the **passive voice** the subject receives the action: *Les élèves sont félicités par la directrice.* "
              "The person who does the action is the **complément d'agent**, introduced by **par** (or sometimes **de**).",
              title="Definition"),
            KEY("How to build the passive", "Follow these four steps.", cards=[
                ["1. New subject", "The direct object of the active sentence becomes the subject."],
                ["2. être", "Use être in the SAME tense as the active verb."],
                ["3. Participle", "Add the past participle of the active verb. It agrees in gender and number with the new subject."],
                ["4. Agent", "The old subject becomes the agent with par (or de). It can be left out."],
            ]),
            IMG("f5fre-2-passive.svg", alt="The active sentence La directrice félicite les élèves and its passive Les élèves sont félicités par la directrice, with crossing arrows showing that subject and object swap places",
                caption="Figure 1. In the passive, subject and object swap places."),
            H("The tense stays the same"),
            T("The tense of the active verb becomes the tense of **être**. Here is the same sentence in six tenses, "
              "with the active sentence *La directrice félicite les élèves* as the starting point."),
            CODE("""Tense              Passive form
présent            Les élèves sont félicités par la directrice.
imparfait          Les élèves étaient félicités par la directrice.
passé composé      Les élèves ont été félicités par la directrice.
plus-que-parfait   Les élèves avaient été félicités par la directrice.
futur simple       Les élèves seront félicités par la directrice.
conditionnel       Les élèves seraient félicités par la directrice.""", "text", title="One passive, six tenses"),
            T("A quick way to find the tense of a passive: look only at **être**. *Sont* is présent, *étaient* is imparfait, *ont été* is passé composé, "
              "*seront* is futur. In the passé composé, **été** never changes, but the participle that follows does: "
              "*Les élèves ont été félicités. La lettre a été écrite.*"),
            H("Which verbs can be passive?"),
            T("Only verbs that can have a **direct object** (COD) have a passive: *Le chauffeur conduit le car.* → *Le car est conduit par le chauffeur.* "
              "Verbs such as *aller, arriver, partir, dormir* have no direct object, so they have no passive. "
              "Do not confuse the passive with a compound tense of a motion verb: *Elle est arrivée* is an active passé composé, not a passive."),
            D("Use **par** with an action done by someone: *La route a été construite par une entreprise.* "
              "Use **de** with verbs of feeling or state such as *aimer, respecter, entourer, couvrir*: *Il est aimé de tous. La colline est couverte de brouillard.* "
              "When the active subject is **on**, the passive usually has no agent: *On a volé mon téléphone.* → *Mon téléphone a été volé.*",
              title="Par, de and on"),
            EX("Worked example 1: présent",
               intro="Turn into the passive: « Le chauffeur conduit le car. »",
               steps=[
                   S("Find the object", text="le car (masculine singular) becomes the subject."),
                   S("être in the same tense", text="conduit is présent, so est."),
                   S("Participle of conduire, agreeing with le car", text="conduit (masculine singular)."),
                   S("Agent", text="par le chauffeur."),
                   S("Write", text="Le car est conduit par le chauffeur."),
               ]),
            EX("Worked example 2: passé composé with agreement",
               intro="Turn into the passive: « Le maire a inauguré l'école. »",
               steps=[
                   S("New subject", text="l'école, feminine singular."),
                   S("être in the passé composé", text="a été (the auxiliary avoir + été)."),
                   S("Participle with feminine agreement", text="inauguré + e = inaugurée."),
                   S("Write", text="L'école a été inaugurée par le maire."),
               ]),
            EX("Worked example 3: futur and imparfait",
               intro="Turn into the passive: « Les voisins aidaient la vieille dame. » and « Marie écrira la lettre. »",
               steps=[
                   S("First sentence: imparfait", text="aidaient → était. New subject la vieille dame (feminine singular): aidée."),
                   S("Write the first", text="La vieille dame était aidée par les voisins."),
                   S("Second sentence: futur", text="écrira → sera. New subject la lettre (feminine): écrite."),
                   S("Write the second", text="La lettre sera écrite par Marie."),
               ]),
            EX("Worked example 4: back to the active, with on",
               intro="Rewrite as an active sentence: « La lettre sera écrite par Marie. » Then rewrite « Mon téléphone a été volé » with on.",
               steps=[
                   S("Agent becomes subject", text="Marie."),
                   S("Subject becomes object, être becomes the verb in the same tense", text="sera écrite (futur) → écrira."),
                   S("Write the active", text="Marie écrira la lettre."),
                   S("With on", text="a été volé (passé composé) → on a volé. Mon téléphone becomes the object: On a volé mon téléphone."),
               ]),
            MISTAKE("Wrong tense of être",
                    "« Les élèves sont félicités » is présent. For « La directrice a félicité les élèves » (passé composé), write « Les élèves ont été félicités ». "
                    "Always copy the tense of the active verb onto être."),
            MISTAKE("Forgetting agreement",
                    "The participle behaves like an adjective: La lettre est écrite. Les lettres sont écrites. Les voleurs ont été arrêtés. "
                    "Check the gender and number of the NEW subject."),
            MISTAKE("Using avoir instead of être, or passive with an intransitive verb",
                    "« Les copies ont corrigées » is wrong. Write « Les copies sont corrigées » (présent) or « ont été corrigées » (passé composé). "
                    "Verbs like arriver or aller have no passive."),
            QUIZ("Which is the correct passive of « Le professeur a corrigé les copies » ?",
                 ["Les copies sont corrigées par le professeur.", "Les copies ont été corrigées par le professeur.", "Les copies ont été corrigé par le professeur.", "Les copies ont corrigées par le professeur."], 1,
                 "The active verb is in the passé composé, so être must be a été / ont été, and the participle agrees (féminin pluriel): corrigées.",
                 hint="Copy the tense, then agree the participle.",
                 feedback=["That is the présent passive.", "", "The participle must agree with les copies.", "Ont corrigées uses avoir, but the passive needs être."]),
            QUIZ("« Les élèves étaient félicités. » In which tense is this passive?",
                 ["présent", "passé composé", "imparfait", "futur"], 2,
                 "Étaient is the imparfait of être, so the passive is in the imparfait.",
                 hint="Look at the form of être only.",
                 feedback=["The présent would be sont.", "The passé composé would be ont été.", "", "The futur would be seront."]),
            TIP("In Paper 1 multiple choice, the wrong options often copy the right tense but forget the agreement, or agree correctly but change the tense. "
                "Check the form of être first, then the participle. Passive sentences also appear in translation work, where English has the same structure.", title="Exam link"),
            PQ("Turn into the passive: « Awa prépare les beignets. »", "Les beignets sont préparés par Awa. (présent; beignets masculine plural.)"),
            PQ("Turn into the passive: « Le préfet a ouvert la foire. »", "La foire a été ouverte par le préfet. (passé composé; foire feminine: ouverte.)"),
            PQ("Turn into the passive: « Les habitants nettoieront le quartier. »", "Le quartier sera nettoyé par les habitants. (futur → sera; quartier masculine singular.)"),
            PQ("Rewrite in the active: « Les voleurs ont été arrêtés par la police. »", "La police a arrêté les voleurs. (a été → a: passé composé; the agent becomes the subject.)"),
            SUM("Passive = être (same tense as the active verb) + past participle + par/de agent.",
                "The object of the active sentence becomes the subject; the participle agrees with it.",
                "Only verbs with a direct object have a passive. Avoid mistakes such as ont corrigées.",
                "Use par for actions, de for feelings or states; with on, the passive often has no agent."),
        ],
    ),
]

# ---------------------------------------------------------------------- 5. Direct and indirect speech: statements
LESSONS += [
    lesson(
        module=M3, topic="Direct and indirect speech",
        title="Reporting statements: tenses, pronouns and time words",
        slug="fr2-reported-statements", minutes=25,
        summary="To report a statement, drop the quotation marks and add que. When the reporting verb is in the past, the tense moves back (présent to imparfait, passé composé to plus-que-parfait, futur to conditionnel), pronouns change person, and time words change (hier to la veille).",
        objectives=[
            "Turn a direct statement into indirect speech with que",
            "Apply the tense shifts after a reporting verb in the past",
            "Change pronouns and possessives to match the new speaker",
            "Replace time and place words (aujourd'hui, hier, demain, ici)",
        ],
        key_concepts=["Discours direct", "Discours indirect", "Verbe introducteur", "Concordance des temps", "Changement de pronoms", "Indicateurs de temps"],
        blocks=[
            H("Introduction"),
            T("Un élève de Form 5 à Bamenda dit à son père : « Mon professeur a dit qu'il corrigerait les copies le lendemain. » "
              "Il ne répète pas les mots exacts du professeur (« Je corrigerai les copies demain. »). "
              "In everyday life we often report what somebody said instead of quoting it exactly. That change is called **indirect speech**."),
            D("In **direct speech** (*discours direct*) we repeat the exact words of a speaker, between quotation marks: *Paul dit : « J'ai faim. »* "
              "In **indirect speech** (*discours indirect*) we report the meaning, without quotation marks, with **que** (**qu'** before a vowel): *Paul dit qu'il a faim.*",
              title="Definition"),
            H("Step 1: the reporting verb"),
            T("The **reporting verb** (*verbe introducteur*) is the verb that introduces the words: *dit, déclare, explique, annonce, répond, affirme*. "
              "Its tense decides what happens next."),
            KEY("Present or future reporting verb: no tense change", "If the reporting verb is in the présent or the futur, the tense of the statement stays the same. Only the pronouns change.", cards=[
                ["Marie dit : « Je suis fatiguée. »", "Marie dit qu'elle est fatiguée."],
                ["Il dira : « Je viendrai. »", "Il dira qu'il viendra."],
            ]),
            KEY("Past reporting verb: the tense moves back", "If the reporting verb is in the passé composé, imparfait or passé simple, the tense of the statement changes.", cards=[
                ["Paul a dit : « J'habite à Douala. »", "Paul a dit qu'il habitait à Douala."],
                ["Paul a dit : « J'ai fini. »", "Paul a dit qu'il avait fini."],
            ]),
            H("Tense changes after a past reporting verb"),
            CODE("""Direct speech               Indirect speech (past reporting verb)
présent                     →  imparfait
passé composé               →  plus-que-parfait
futur simple                →  conditionnel présent
futur antérieur             →  conditionnel passé
imparfait                   →  imparfait  (no change)
plus-que-parfait            →  plus-que-parfait  (no change)
conditionnel                →  conditionnel  (no change)""", "text", title="The tense chain"),
            IMG("f5fre-2-tense-shift.svg", alt="Four arrows: présent to imparfait, passé composé to plus-que-parfait, futur simple to conditionnel présent, futur antérieur to conditionnel passé",
                caption="Figure 1. The tense moves back after a past reporting verb."),
            CODE("""« J'étudie. »        Elle a dit qu'elle étudiait.
« J'ai étudié. »     Elle a dit qu'elle avait étudié.
« J'étudierai. »     Elle a dit qu'elle étudierait.
« J'aurai fini. »    Elle a dit qu'elle aurait fini.
« J'étudiais. »      Elle a dit qu'elle étudiait.
« J'avais fini. »    Elle a dit qu'elle avait fini.""", "text", title="Examples with a past reporting verb"),
            H("Step 2: pronouns and possessives"),
            T("Pronouns and possessives change so that they fit the person who is speaking in the report. "
              "The most common changes are: **je → il / elle**, **tu → je / il / elle**, **mon, ma, mes → son, sa, ses**, **nous → ils / elles**, **notre → leur**. "
              "Example: *Ma mère a dit : « Tu as fini tes devoirs. »* becomes *Ma mère a dit que j'avais fini mes devoirs* (tu → je, tes → mes). "
              "Ask yourself each time: who spoke, to whom, and who is reporting?"),
            T("Notice also that an exclamation or a question in the original disappears: the quotation marks and the exclamation mark are not kept."),
            H("Step 3: time and place words"),
            T("When the reporting verb is in the past, words that depend on the moment of speaking change, because the report is made later."),
            CODE("""aujourd'hui            →  ce jour-là
hier                   →  la veille
demain                 →  le lendemain
ce soir                →  ce soir-là
maintenant             →  alors
la semaine prochaine   →  la semaine suivante
la semaine dernière    →  la semaine précédente
ici                    →  là""", "text", title="Time and place words (past reporting verb)"),
            EX("Worked example 1: pronouns only",
               intro="Report: « Marie dit : “Je suis fatiguée.” »",
               steps=[
                   S("Reporting verb", text="dit is in the présent: the tense does not change."),
                   S("Add que", text="Marie dit que ..."),
                   S("Change the pronoun", text="je becomes elle (Marie is a woman)."),
                   S("Write", text="Marie dit qu'elle est fatiguée. (que becomes qu' before elle)"),
               ]),
            EX("Worked example 2: tense and pronoun",
               intro="Report: Paul a dit : « J'habite à Douala. »",
               steps=[
                   S("Reporting verb", text="a dit is in the passé composé: the tense will shift."),
                   S("présent becomes imparfait", text="j'habite → il habitait."),
                   S("Pronoun", text="je → il."),
                   S("Write", text="Paul a dit qu'il habitait à Douala."),
               ]),
            EX("Worked example 3: time word and futur",
               intro="Report: Le directeur a annoncé : « La réunion aura lieu demain. »",
               steps=[
                   S("Tense", text="aura lieu is futur simple, so after a past reporting verb it becomes the conditionnel: aurait lieu."),
                   S("Time word", text="demain becomes le lendemain."),
                   S("Write", text="Le directeur a annoncé que la réunion aurait lieu le lendemain."),
               ]),
            EX("Worked example 4: several changes",
               intro="Report: Awa a dit : « Hier, j'ai vendu mes tomates. »",
               steps=[
                   S("Tense", text="passé composé → plus-que-parfait: j'ai vendu → elle avait vendu."),
                   S("Pronoun and possessive", text="je → elle, mes → ses."),
                   S("Time word", text="hier → la veille."),
                   S("Write", text="Awa a dit que la veille elle avait vendu ses tomates."),
               ]),
            MISTAKE("Forgetting the tense shift",
                    "« Paul a dit qu'il habite à Douala » is wrong after a past reporting verb. Write « qu'il habitait ». "
                    "Similarly, « Elle a dit qu'elle viendra » becomes « qu'elle viendrait »."),
            MISTAKE("Keeping the original time words",
                    "After a past reporting verb, hier, demain and aujourd'hui must change: la veille, le lendemain, ce jour-là."),
            MISTAKE("Keeping the original pronouns",
                    "« Paul a dit qu'il habitait à Douala » and not « que j'habitais ». Check who speaks and who reports."),
            QUIZ("Paul a dit : « J'ai faim. » Choose the correct indirect speech.",
                 ["Paul a dit qu'il a faim.", "Paul a dit qu'il avait faim.", "Paul a dit que j'avais faim.", "Paul a dit qu'il aurait faim."], 1,
                 "J'ai faim is in the présent, so it becomes the imparfait avait. J' becomes il.",
                 hint="Reporting verb in the past: move the tense back.",
                 feedback=["The présent was kept, but the reporting verb is in the past.", "", "The pronoun j' must change to il.", "The conditionnel would be for a futur."]),
            QUIZ("Awa a dit : « Je partirai demain. » Choose the correct indirect speech.",
                 ["Awa a dit qu'elle partirait demain.", "Awa a dit qu'elle partira le lendemain.", "Awa a dit qu'elle partirait le lendemain.", "Awa a dit qu'elle était partie le lendemain."], 2,
                 "Futur → conditionnel (partirait) and demain → le lendemain.",
                 hint="Two changes: the tense and the time word.",
                 feedback=["Demain must become le lendemain.", "The futur must become the conditionnel.", "", "Futur does not become passé composé or plus-que-parfait."]),
            TIP("Paper 1 multiple choice often gives one correct report and three options that make one error each: the tense, the pronoun or the time word. "
                "Check the three in turn. Indirect speech also gives you the narrative skill needed in the essay, where you report what people said.", title="Exam link"),
            PQ("Report: Marie dit : « Je suis fatiguée. »", "Marie dit qu'elle est fatiguée."),
            PQ("Report: Le professeur a dit : « Je corrigerai les copies demain. »", "Le professeur a dit qu'il corrigerait les copies le lendemain."),
            PQ("Report: Ma mère a dit : « Tu as fini tes devoirs. »", "Ma mère a dit que j'avais fini mes devoirs. (tu → je, tes → mes, passé composé → plus-que-parfait.)"),
            PQ("Report: Elle a expliqué : « Hier, j'ai visité Kribi. »", "Elle a expliqué que la veille, elle avait visité Kribi. (je → elle; passé composé → plus-que-parfait; hier → la veille.)"),
            SUM("Indirect speech has no quotation marks and uses que (qu').",
                "If the reporting verb is in the past: présent → imparfait, passé composé → plus-que-parfait, futur → conditionnel.",
                "Pronouns and possessives change with the speaker; time words change: hier → la veille, demain → le lendemain, aujourd'hui → ce jour-là.",
                "Imparfait, plus-que-parfait and conditionnel do not change."),
        ],
    ),
]

# ---------------------------------------------------------------------- 6. Direct and indirect speech: questions and commands
LESSONS += [
    lesson(
        module=M3, topic="Direct and indirect speech",
        title="Reporting questions and commands",
        slug="fr2-reported-questions-commands", minutes=24,
        summary="A reported yes/no question uses si, a reported question word keeps its word (qu'est-ce que becomes ce que) with normal word order and no question mark, and a reported command becomes de + infinitive. Tense and pronoun changes follow the previous lesson.",
        objectives=[
            "Report a yes/no question with si, and a question with an interrogative word",
            "Change qu'est-ce que, qu'est-ce qui and que into ce que and ce qui",
            "Report a positive and a negative command with de + infinitive",
            "Combine these with the tense, pronoun and time changes",
        ],
        key_concepts=["Question indirecte", "si", "ce que / ce qui", "Ordre des mots", "de + infinitif", "Ordre indirect"],
        blocks=[
            H("Introduction"),
            T("Au lycée de Bonabéri, la surveillante a demandé à Aïcha : « Pourquoi es-tu en retard ? » Plus tard, Aïcha raconte à sa mère : "
              "« La surveillante m'a demandé pourquoi j'étais en retard. » Notice what has disappeared: the quotation marks, the question mark, and the inversion."),
            T("In the previous lesson you reported statements. This lesson covers the two other sentence types: **questions** and **commands**. "
              "Every change from the previous lesson (tense after a past reporting verb, pronouns, time words) still applies."),
            H("Reported yes/no questions"),
            D("A yes/no question becomes a clause introduced by **si**. **Si** becomes **s'** only before **il** or **ils**: *s'il, s'ils*, but *si elle, si on, si nous*. "
              "The word order is the normal order (subject, verb), with no est-ce que, no inversion and no question mark.",
              title="Rule"),
            CODE("""« Est-ce que tu viens ? »   Il a demandé si je venais.
« Viens-tu ? »             Il a demandé si je venais.
« Tu vas au marché ? »     Awa a demandé à Paul s'il allait au marché.
« Elle a mangé ? »         Il a demandé si elle avait mangé.""", "text", title="With si"),
            H("Reported questions with a question word"),
            T("The question word stays (où, quand, comment, pourquoi, combien, quel ...). The order is subject + verb, with no inversion, no est-ce que and no question mark. "
              "Only the forms with **que** change."),
            CODE("""Direct                               Indirect
Où vas-tu ?                          ... où j'allais.
Quand viendras-tu ?                  ... quand je viendrais.
Pourquoi pleures-tu ?                ... pourquoi je pleurais.
Combien coûte ce pain ?              ... combien coûtait ce pain.
Quelle heure est-il ?                ... quelle heure il était.
Qui est venu ?                       ... qui était venu.
Qu'est-ce que tu fais ? / Que fais-tu ?   ... ce que je faisais.
Qu'est-ce qui se passe ?             ... ce qui se passait.
De quoi parles-tu ?                  ... de quoi je parlais.""", "text", title="Question words in the report (past reporting verb)"),
            KEY("The que family", "Remember these three changes.", cards=[
                ["qu'est-ce que / que", "→ ce que"],
                ["qu'est-ce qui", "→ ce qui"],
                ["qui, quoi (after a preposition)", "stay the same"],
            ]),
            H("Reported commands"),
            T("A command (imperative) becomes **de + infinitive**. The reporting verb is often *dire (à quelqu'un) de, demander (à quelqu'un) de, ordonner de, conseiller de*. "
              "A negative command becomes **de ne pas + infinitive**. Possessives follow the usual rule: *ta chambre* becomes *ma chambre* if I am the person who was told."),
            CODE("""« Range ta chambre ! »        Ma mère m'a dit de ranger ma chambre.
« Fermez la porte ! »         Elle nous a demandé de fermer la porte.
« Ne mange pas trop de sucre ! »   Le médecin lui a dit de ne pas manger trop de sucre.
« Ne sortez jamais seuls ! »  Il leur a conseillé de ne jamais sortir seuls.""", "text", title="Command to de + infinitive"),
            EX("Worked example 1: a yes/no question",
               intro="Report: Awa a demandé à Paul : « Tu vas au marché ? »",
               steps=[
                   S("Type", text="A yes/no question: introduce it with si."),
                   S("Pronoun and tense", text="tu → il. vas (présent) → allait (imparfait), because the reporting verb is in the past."),
                   S("Elision", text="si + il = s'il."),
                   S("Write", text="Awa a demandé à Paul s'il allait au marché."),
               ]),
            EX("Worked example 2: qu'est-ce que",
               intro="Report: Le professeur a demandé aux élèves : « Qu'est-ce que vous avez fait hier ? »",
               steps=[
                   S("Question word", text="qu'est-ce que becomes ce que."),
                   S("Pronoun", text="vous → ils (the pupils)."),
                   S("Tense and time", text="avez fait (passé composé) → avaient fait. hier → la veille."),
                   S("Write", text="Le professeur a demandé aux élèves ce qu'ils avaient fait la veille."),
               ]),
            EX("Worked example 3: a question with où",
               intro="Report: Elle m'a demandé : « Où habitez-vous ? »",
               steps=[
                   S("Keep the question word", text="où."),
                   S("Remove the inversion", text="habitez-vous becomes subject + verb."),
                   S("Pronoun and tense", text="vous → je (it is me she asked). habitez → habitais."),
                   S("Write", text="Elle m'a demandé où j'habitais."),
               ]),
            EX("Worked example 4: negative command",
               intro="Report: Le médecin lui a dit : « Ne mangez pas trop de sucre ! »",
               steps=[
                   S("Command type", text="negative imperative: use de ne pas + infinitive."),
                   S("Infinitive", text="manger."),
                   S("Write", text="Le médecin lui a dit de ne pas manger trop de sucre."),
               ]),
            MISTAKE("Keeping the inversion or the question mark",
                    "« Il a demandé où habitais-tu ? » is wrong. A reported question is a statement in form: « Il a demandé où j'habitais. » No inversion, no question mark."),
            MISTAKE("Using qu'est-ce que in the report",
                    "« Elle a demandé qu'est-ce que je faisais » is wrong. Write « Elle a demandé ce que je faisais. » Also: « ce qui » for qu'est-ce qui."),
            MISTAKE("Keeping the imperative in the report",
                    "« Il m'a dit : mange » cannot be reported as « Il m'a dit que mange ». Use de + infinitive: Il m'a dit de manger."),
            QUIZ("Elle a demandé à Paul : « Pourquoi pleures-tu ? » Choose the correct report.",
                 ["Elle a demandé à Paul pourquoi il pleurait.", "Elle a demandé à Paul pourquoi pleurait-il.", "Elle a demandé à Paul pourquoi il pleure.", "Elle a demandé à Paul s'il pleurait pourquoi."], 0,
                 "Keep pourquoi, use normal order, tu → il, présent → imparfait.",
                 hint="Normal word order, imparfait.",
                 feedback=["", "There is no inversion in a reported question.", "The présent should become the imparfait after a past reporting verb.", "Si is for yes/no questions, not for pourquoi."]),
            QUIZ("Ma mère m'a dit : « Range ta chambre ! » Choose the correct report.",
                 ["Ma mère m'a dit que je range ma chambre.", "Ma mère m'a dit de ranger ma chambre.", "Ma mère m'a dit de ranger ta chambre.", "Ma mère m'a dit si je rangeais ma chambre."], 1,
                 "A command becomes de + infinitive, and ta becomes ma.",
                 hint="Commands use an infinitive in the report.",
                 feedback=["A command is not reported as a statement with que.", "", "The possessive must change from ta to ma.", "Si introduces a question, not a command."]),
            TIP("In Paper 1 multiple choice, check three things in a reported question: the question word (ce que, not qu'est-ce que), the word order (no inversion) and the tense. "
                "For commands, check for de + infinitive. These skills are also used when you write dialogue in your essay.", title="Exam link"),
            PQ("Report: Il a demandé à Marie : « Tu aimes le football ? »", "Il a demandé à Marie si elle aimait le football. (si, tu → elle, présent → imparfait.)"),
            PQ("Report: La directrice a demandé aux élèves : « Qu'est-ce que vous voulez ? »", "La directrice a demandé aux élèves ce qu'ils voulaient. (qu'est-ce que → ce que; vous → ils; voulez → voulaient.)"),
            PQ("Report: Le chauffeur nous a dit : « Ne parlez pas pendant le voyage ! »", "Le chauffeur nous a dit de ne pas parler pendant le voyage. (de ne pas + infinitive.)"),
            PQ("Report: Elle m'a demandé : « Quand arriveras-tu ? »", "Elle m'a demandé quand j'arriverais. (quand kept, no inversion, tu → je, futur → conditionnel.)"),
            SUM("Reported yes/no questions use si (s' before il/ils). Reported questions have normal word order and no question mark.",
                "Question words stay, but qu'est-ce que / que becomes ce que and qu'est-ce qui becomes ce qui.",
                "Commands become de + infinitive; negative commands become de ne pas + infinitive.",
                "Tense, pronoun and time-word changes from the previous lesson still apply after a past reporting verb."),
        ],
    ),
]

# ---------------------------------------------------------------------- 7. Logical connectors: cause, consequence, purpose
LESSONS += [
    lesson(
        module=M3, topic="Logical connectors",
        title="Logical connectors 1: cause, consequence and purpose",
        slug="fr2-connectors-cause-consequence-purpose", minutes=24,
        summary="Connectors link ideas. Cause (parce que, puisque, comme, car, grâce à, à cause de) and consequence (donc, alors, c'est pourquoi, si bien que, si ... que) use the indicative; purpose (pour que, afin que) uses the subjunctive, or pour / afin de + infinitive when the subject is the same.",
        objectives=[
            "Link ideas with connectors of cause, consequence and purpose",
            "Use the mood each connector requires (indicative or subjunctive)",
            "Choose between pour que + subjunctive and pour + infinitive",
            "Distinguish grâce à, à cause de and parce que",
        ],
        key_concepts=["Connecteur logique", "Cause", "Conséquence", "But", "Indicatif", "Subjonctif", "pour que / pour + infinitif"],
        blocks=[
            H("Introduction"),
            T("Une élève de Bertoua écrit : « Je suis arrivée en retard **parce que** le car est tombé en panne. **Donc** j'ai manqué le premier cours. "
              "Le lendemain, je suis partie plus tôt **afin d'**être à l'heure. » The three bold words connect ideas: a cause, a result and an aim."),
            T("A **connector** (*connecteur logique*) shows the logical link between two ideas. "
              "They are very important in the French essay, where the Board's marking looks at whether the ideas follow each other logically. They also appear in Paper 1 multiple choice, "
              "where you must choose the connector that fits, or the correct mood of the verb after it."),
            D("Each connector has a meaning and, for many, requires a **mood**. The **indicative** states facts: *Il pleut.* "
              "The **subjunctive** is used after certain connectors (here, those of purpose): *pour que tu réussisses*. "
              "The mood is decided by the connector, not by your wish.",
              title="Connector and mood"),
            H("Cause"),
            T("**Cause** answers the question *Pourquoi ?* The main connectors of cause are followed by the **indicative**."),
            CODE("""parce que        because (the real reason)     Il est absent parce qu'il est malade.
car              for, because (written)        Il est absent, car il est malade.
puisque          since (reason already known)  Puisque tu es là, aide-moi.
comme            as (starts the sentence)      Comme il pleuvait, nous sommes restés.
étant donné que  given that                    Étant donné que le car est en retard, ...
grâce à          thanks to + noun (good result)   Grâce à la bourse, il a pu étudier.
à cause de       because of + noun (bad result)   À cause de la grève, les cours ont été suspendus.""", "text", title="Cause connectors"),
            T("**Grâce à** and **à cause de** are followed by a **noun**, not a verb: *grâce à ton aide*, *à cause de la pluie*. "
              "Use **grâce à** for a positive result and **à cause de** for a negative one. **Comme** always starts the sentence. "
              "**Car** joins two clauses and is preceded by a comma; it does not start a sentence in a careful text."),
            H("Consequence"),
            T("**Consequence** answers the question *Quel est le résultat ?* The connectors are followed by the **indicative**."),
            CODE("""donc            therefore            La route est mauvaise, donc le voyage est long.
alors           so                   Il pleut, alors nous restons ici.
c'est pourquoi  that is why          C'est pourquoi je suis venu.
par conséquent  consequently         Par conséquent, la réunion est reportée.
si bien que     so that, with the result that   Il a beaucoup étudié, si bien qu'il a réussi.
si / tellement ... que   so ... that   Il pleuvait si fort que les rues ont été inondées.""", "text", title="Consequence connectors"),
            H("Purpose"),
            D("**Purpose** (*le but*) answers *Dans quel but ?* (for what aim?). **Pour que** and **afin que** are followed by the **subjunctive**. "
              "When the subject of both parts is the **same**, do not use que: use **pour** or **afin de** with an **infinitive**.",
              title="Purpose and the subjunctive"),
            CODE("""Different subjects:
Elle travaille pour que ses enfants réussissent.     (subjunctive)
Il explique afin que tout le monde comprenne.        (subjunctive)

Same subject:
Elle travaille pour réussir.                          (infinitive)
Il a économisé afin d'acheter un ordinateur.         (infinitive)""", "text", title="Pour que or pour"),
            KEY("Mood summary for this lesson", "Remember the pattern.", cards=[
                ["Cause", "parce que, car, puisque, comme + indicative"],
                ["Consequence", "donc, alors, si bien que, si ... que + indicative"],
                ["Purpose", "pour que, afin que + subjunctive"],
                ["Same subject", "pour / afin de + infinitive"],
            ]),
            EX("Worked example 1: cause and consequence",
               intro="Join the ideas in two ways: « Le car est tombé en panne. Nous sommes arrivés en retard. »",
               steps=[
                   S("Cause (parce que)", text="Nous sommes arrivés en retard parce que le car est tombé en panne."),
                   S("Consequence (donc)", text="Le car est tombé en panne, donc nous sommes arrivés en retard."),
                   S("Mood", text="Both connectors take the indicative: est tombé, sommes arrivés."),
               ]),
            EX("Worked example 2: pour que or pour",
               intro="Complete: « Il travaille dur pour que ses enfants (avoir) un bel avenir. » and « Il travaille dur pour (réussir) son examen. »",
               steps=[
                   S("First sentence", text="Subjects differ (il / ses enfants): pour que + subjunctive."),
                   S("Subjunctive of avoir for ils", text="qu'ils aient."),
                   S("Second sentence", text="Same subject (il): pour + infinitive."),
                   S("Write", text="Il travaille dur pour que ses enfants aient un bel avenir. Il travaille dur pour réussir son examen."),
               ]),
            EX("Worked example 3: grâce à or à cause de",
               intro="Choose and complete: « ___ la grève, les cours ont été suspendus. » and « ___ ton aide, j'ai réussi. »",
               steps=[
                   S("First sentence", text="The result is bad (classes suspended): à cause de la grève."),
                   S("Second sentence", text="The result is good (success): grâce à ton aide."),
                   S("Check", text="Both are followed by a noun (la grève, ton aide)."),
               ]),
            MISTAKE("Subjunctive after parce que",
                    "« Il est absent parce qu'il soit malade » is wrong. Parce que takes the indicative: parce qu'il est malade."),
            MISTAKE("Indicative after pour que",
                    "« Il travaille pour que ses enfants ont un avenir » is wrong. Pour que and afin que need the subjunctive: pour que ses enfants aient un avenir. "
                    "Learn the irregular forms: que j'aie, que tu aies, qu'il soit, qu'il vienne, qu'ils fassent."),
            MISTAKE("Using pour que with the same subject",
                    "« Je travaille pour que je réussisse » is incorrect. Use « Je travaille pour réussir »."),
            MISTAKE("Mixing à cause de and grâce à",
                    "Do not say « grâce à la grève » for a bad result. Use à cause de for negative results, grâce à for positive ones, and always a noun after them."),
            QUIZ("Choose the correct sentence.",
                 ["Il est absent parce qu'il soit malade.", "Il est absent parce qu'il est malade.", "Il est absent à cause qu'il est malade.", "Il est absent grâce à qu'il est malade."], 1,
                 "Parce que takes the indicative.",
                 hint="Which connector is followed by a clause in the indicative?",
                 feedback=["Parce que is never followed by the subjunctive.", "", "À cause de needs a noun.", "Grâce à needs a noun."]),
            QUIZ("Choose the correct completion: « Elle explique afin que tout le monde ___. »",
                 ["comprend", "comprenne", "comprendre", "comprenait"], 1,
                 "Afin que takes the subjunctive: que tout le monde comprenne.",
                 hint="Afin que expresses purpose.",
                 feedback=["That is the indicative.", "", "The infinitive is used with afin de, not afin que.", "The imparfait is indicative."]),
            TIP("For Paper 1 multiple choice, many questions ask you to match a connector with its mood: parce que (indicative), pour que (subjunctive). "
                "In the essay, use varied connectors (donc, c'est pourquoi, afin de) to make your story or argument flow.", title="Exam link"),
            PQ("Complete with parce que or donc: « Je suis fatigué, ___ je me couche. »", "donc. (donc introduces the consequence.)"),
            PQ("Put the verb in the right form: « Je t'explique afin que tu (comprendre). »", "comprennes. (afin que + subjunctive: que tu comprennes.)"),
            PQ("Choose pour or pour que: « Elle étudie ___ réussir son examen. »", "pour. (the subject is the same, so use pour + infinitive.)"),
            PQ("Choose grâce à or à cause de: « ___ la pluie, le match a été annulé. »", "À cause de. (a negative result, followed by a noun.)"),
            SUM("Cause connectors (parce que, car, puisque, comme) and consequence connectors (donc, alors, si bien que) are followed by the indicative.",
                "Purpose connectors pour que and afin que take the subjunctive; with the same subject use pour or afin de + infinitive.",
                "Grâce à (good result) and à cause de (bad result) are followed by a noun.",
                "Use connectors to make your French essay logical and coherent."),
        ],
    ),
]

# ---------------------------------------------------------------------- 8. Logical connectors: opposition and concession
LESSONS += [
    lesson(
        module=M3, topic="Logical connectors",
        title="Logical connectors 2: opposition and concession",
        slug="fr2-connectors-opposition-concession", minutes=24,
        summary="Opposition contrasts two facts (mais, alors que, tandis que, en revanche). Concession admits a fact that does not stop the result (bien que and quoique with the subjunctive, même si with the indicative, malgré + noun, pourtant, cependant).",
        objectives=[
            "Express opposition with mais, alors que, tandis que, en revanche, par contre",
            "Express concession with bien que, quoique, même si, malgré, pourtant, cependant",
            "Use the subjunctive after bien que and quoique, and the indicative after même si and alors que",
            "Compare all the connectors of the module and their moods",
        ],
        key_concepts=["Opposition", "Concession", "bien que + subjonctif", "même si + indicatif", "malgré + nom", "alors que"],
        blocks=[
            H("Introduction"),
            T("À Garoua, il fait très chaud en avril, **alors qu'**à Buéa il pleut souvent. Mon cousin habite à Garoua **mais** il aime le froid. "
              "**Bien qu'**il fasse chaud, il porte un pull le soir. Dans ces phrases, chaque connecteur montre une difficulté, un contraste ou une surprise."),
            D("**Opposition** (*opposition*) puts two facts in contrast: they differ. **Concession** (*concession*) admits a fact that could have prevented another, "
              "but did not: the result is surprising. *Il est malade, mais il travaille* is a contrast. *Bien qu'il soit malade, il est venu* is a concession.",
              title="Definition"),
            H("Opposition"),
            CODE("""mais          but                  Il est petit, mais il est fort.
alors que     while, whereas       Il pleut à Buéa, alors qu'il fait sec à Garoua.
tandis que    while, whereas       Elle aime lire, tandis que son frère préfère le sport.
en revanche   on the other hand    Le prix est élevé ; en revanche, la qualité est bonne.
par contre    on the other hand (informal)   Il est lent ; par contre, il est précis.
au contraire  on the contrary      Il n'est pas triste, au contraire, il est joyeux.
au lieu de    instead of + infinitive/noun   Au lieu de dormir, il regarde la télévision.""", "text", title="Opposition connectors"),
            T("**Alors que** and **tandis que** are followed by the **indicative**: *Il travaille alors que les autres dorment.* "
              "**Mais** joins two ideas and needs no mood change. **Au lieu de** is followed by an infinitive or a noun, not by a clause."),
            H("Concession"),
            CODE("""bien que         although      + subjunctive   Bien qu'il soit malade, il est venu.
quoique          although      + subjunctive   Quoiqu'elle ait peur, elle chante.
même si          even if       + indicative    Même s'il pleut, nous sortirons.
malgré           despite       + noun          Malgré la pluie, nous sommes sortis.
en dépit de      despite       + noun          En dépit de la fatigue, il continue.
pourtant         yet, however  (adverb)        Il est fatigué ; pourtant, il travaille.
cependant        however       (adverb)        Le plan est bon ; cependant, il coûte cher.
néanmoins        nevertheless  (adverb)        Le prix a baissé ; néanmoins, c'est cher.""", "text", title="Concession connectors"),
            KEY("Mood and structure after concession words", "Remember this pattern.", cards=[
                ["bien que, quoique", "+ subjunctive (Bien qu'il soit ..., Quoiqu'elle ait ...)"],
                ["même si", "+ indicative (Même s'il pleut ... : never the subjunctive and never the conditionnel)"],
                ["malgré, en dépit de", "+ noun (Malgré la pluie)"],
                ["pourtant, cependant, néanmoins", "adverbs: a full sentence follows, often after a comma or semicolon"],
            ]),
            T("Subjunctive forms that you need after **bien que**: être → *qu'il soit*, *qu'ils soient*; avoir → *qu'il ait*, *qu'ils aient*; "
              "faire → *qu'il fasse*, *qu'ils fassent*; aller → *qu'il aille*; pouvoir → *qu'il puisse*; savoir → *qu'il sache*; "
              "regular verbs: *qu'il finisse*, *qu'il parle*."),
            KEY("Mood chart: all connectors of the module", "Cause and consequence from the previous lesson, plus opposition and concession.", cards=[
                ["Indicative", "parce que, puisque, comme, car, donc, alors, si bien que, alors que, tandis que, même si"],
                ["Subjunctive", "pour que, afin que, bien que, quoique"],
                ["Noun after", "grâce à, à cause de, malgré, en dépit de"],
                ["Infinitive after", "pour, afin de, au lieu de"],
            ]),
            EX("Worked example 1: bien que",
               intro="Join with bien que: « Il est malade. Il va à l'école. »",
               steps=[
                   S("Meaning", text="Being ill could have stopped him, but did not: a concession."),
                   S("Connector and mood", text="bien que + subjunctive. Subjunctive of être for il: qu'il soit."),
                   S("Elision", text="bien que + il = bien qu'il."),
                   S("Write", text="Bien qu'il soit malade, il va à l'école."),
               ]),
            EX("Worked example 2: même si or bien que",
               intro="Complete: « ___ il pleut, nous sortirons. » and « ___ il pleuve, nous sortons. » (même si / bien que)",
               steps=[
                   S("First sentence", text="il pleut is the indicative: même s'il pleut."),
                   S("Second sentence", text="il pleuve is the subjunctive: bien qu'il pleuve."),
                   S("Write", text="Même s'il pleut, nous sortirons. Bien qu'il pleuve, nous sortons."),
               ]),
            EX("Worked example 3: malgré",
               intro="Rewrite with malgré: « Bien qu'il fasse chaud, il porte un pull. »",
               steps=[
                   S("Malgré needs a noun", text="Replace il fasse chaud by the noun phrase la chaleur."),
                   S("Write", text="Malgré la chaleur, il porte un pull."),
               ]),
            EX("Worked example 4: alors que",
               intro="Join with alors que (contrast): « Awa aime le football. Sa sœur préfère le basket. »",
               steps=[
                   S("Meaning", text="Two different things, side by side: opposition."),
                   S("Connector", text="alors que + indicative: préfère."),
                   S("Write", text="Awa aime le football alors que sa sœur préfère le basket."),
               ]),
            MISTAKE("Indicative after bien que",
                    "« Bien qu'il est malade » is wrong. Write « Bien qu'il soit malade ». Bien que and quoique always take the subjunctive."),
            MISTAKE("Subjunctive after même si",
                    "« Même s'il pleuve » is wrong. Même si takes the indicative: « Même s'il pleut ». "
                    "Also never use the conditionnel after si: not « même s'il pleuvrait »."),
            MISTAKE("Malgré followed by a verb",
                    "Malgré is followed by a noun: malgré la pluie, malgré ton aide. If you have a clause, use bien que: Bien qu'il pleuve."),
            MISTAKE("Confusing mais and pourtant",
                    "Mais joins two clauses: Il est fatigué, mais il travaille. Pourtant is an adverb and can start a second sentence: Il est fatigué. Pourtant, il travaille."),
            QUIZ("Choose the correct sentence.",
                 ["Bien qu'il est malade, il travaille.", "Bien qu'il soit malade, il travaille.", "Bien qu'il sera malade, il travaille.", "Bien qu'il serait malade, il travaille."], 1,
                 "Bien que takes the subjunctive: qu'il soit.",
                 hint="Which mood follows bien que?",
                 feedback=["That is the indicative.", "", "That is the futur.", "That is the conditionnel."]),
            QUIZ("Which connector is followed by the indicative?",
                 ["bien que", "quoique", "même si", "afin que"], 2,
                 "Même si is followed by the indicative: même s'il pleut.",
                 hint="Three of them need the subjunctive.",
                 feedback=["Bien que needs the subjunctive.", "Quoique needs the subjunctive.", "", "Afin que needs the subjunctive."]),
            TIP("Paper 1 multiple choice likes to test the mood after bien que and the choice between malgré (noun) and bien que (verb). "
                "In the essay, concession and opposition connectors help you present both sides in an argumentative text and show logical coherence.", title="Exam link"),
            PQ("Join with bien que: « Il pleut. Nous sortons. »", "Bien qu'il pleuve, nous sortons. (subjunctive of pleuvoir: qu'il pleuve.)"),
            PQ("Choose même si or bien que: « ___ tu es fatigué, viens à la réunion. »", "Même si. (tu es is the indicative.)"),
            PQ("Rewrite with malgré: « Bien qu'il ait peur, il parle. »", "Malgré sa peur, il parle. (malgré + noun.)"),
            PQ("Join with alors que: « Il fait sec à Garoua. Il pleut à Buéa. »", "Il fait sec à Garoua alors qu'il pleut à Buéa. (alors que + indicative.)"),
            SUM("Opposition contrasts two facts: mais, alors que, tandis que, en revanche. Concession admits a fact that does not stop the result.",
                "Bien que and quoique take the subjunctive; même si and alors que take the indicative.",
                "Malgré and en dépit de take a noun; pourtant, cependant and néanmoins are adverbs.",
                "Use the mood chart to check any connector in Paper 1."),
        ],
    ),
]

# ---------------------------------------------------------------------- 9. Family and social relationships
LESSONS += [
    lesson(
        module=M4, topic="Family and social relationships",
        title="Family and social relationships",
        slug="fr2-lex-family-social", minutes=22,
        summary="Words for the family, friends, neighbours and community life, with their gender, the verbs for family events (se marier, naître, rendre visite), a model dialogue and common traps such as ma amie and les parents.",
        objectives=[
            "Name family members, including extended and in-law relatives, with the right gender",
            "Talk about friends, neighbours and community life (entraide, tontine, fête)",
            "Use verbs for family events and relationships (se marier, s'entendre bien, se disputer)",
            "Use possessives correctly with family words (mon amie, ma tante)",
        ],
        key_concepts=["La famille", "Les relations sociales", "Genre des noms", "Les adjectifs possessifs", "Les événements familiaux"],
        blocks=[
            H("Introduction"),
            T("Au Cameroun, la famille est souvent très grande : les parents, les enfants, les grands-parents, les oncles, les tantes, les cousins. "
              "On dit « la famille élargie » (the extended family). Les voisins et les amis font aussi partie de la vie sociale."),
            T("Paper 1 multiple choice tests vocabulary in context: you read a sentence with a gap and choose the right word. "
              "The best way to learn is to group words by theme, to note the **gender** of each noun (m = masculine, f = feminine), and to learn each word in a short sentence."),
            D("The **gender** of a French noun is masculine or feminine. Always learn the noun with its article: *le père*, *la mère*. "
              "Nouns for people often have two forms (*le cousin, la cousine*), but some have one form for both (*un enfant, une enfant*).",
              title="Learn nouns with their gender"),
            H("The family"),
            BANK("Close family", [
                ("le père", "m", "father"), ("la mère", "f", "mother"), ("les parents", "m", "parents (also: relatives)"),
                ("le fils", "m", "son"), ("la fille", "f", "daughter, girl"), ("l'enfant", "mf", "child"),
                ("le frère", "m", "brother"), ("la sœur", "f", "sister"), ("l'aîné, l'aînée", "mf", "eldest child"),
                ("le cadet, la cadette", "mf", "younger or youngest child"), ("les jumeaux", "m", "twins (boys, or mixed)"),
                ("le mari", "m", "husband"), ("la femme", "f", "wife, woman"),
            ]),
            BANK("Extended family", [
                ("le grand-père", "m", "grandfather"), ("la grand-mère", "f", "grandmother"), ("les grands-parents", "m", "grandparents"),
                ("le petit-fils, la petite-fille", "mf", "grandson, granddaughter"),
                ("l'oncle", "m", "uncle"), ("la tante", "f", "aunt"), ("le neveu", "m", "nephew"), ("la nièce", "f", "niece"),
                ("le cousin, la cousine", "mf", "cousin"), ("le beau-père", "m", "father-in-law, stepfather"),
                ("la belle-mère", "f", "mother-in-law, stepmother"), ("le beau-frère", "m", "brother-in-law"),
                ("la famille nombreuse", "f", "large family"),
            ]),
            H("Friends, neighbours and community"),
            BANK("Social relationships", [
                ("l'ami, l'amie", "mf", "friend"), ("le camarade de classe", "m", "classmate"), ("le voisin, la voisine", "mf", "neighbour"),
                ("le collègue", "mf", "colleague"), ("le quartier", "m", "neighbourhood"), ("le chef du village", "m", "village chief"),
                ("la tontine", "f", "rotating savings group of friends or neighbours"),
                ("l'entraide", "f", "mutual help"), ("la solidarité", "f", "solidarity"), ("le respect", "m", "respect"),
                ("le mariage", "m", "wedding, marriage"), ("la naissance", "f", "birth"), ("l'anniversaire", "m", "birthday"),
                ("le baptême", "m", "baptism"), ("la fête", "f", "party, celebration"), ("la réunion de famille", "f", "family gathering"),
            ]),
            BANK("Verbs and phrases", [
                ("se marier (avec)", "v", "to get married (to)"), ("épouser", "v", "to marry (someone)"), ("naître", "v", "to be born"),
                ("grandir", "v", "to grow up"), ("élever un enfant", "v", "to bring up a child"),
                ("rendre visite à", "v", "to visit (a person)"), ("s'entendre bien avec", "v", "to get on well with"),
                ("se disputer", "v", "to quarrel"), ("se réconcilier", "v", "to make up"), ("fêter", "v", "to celebrate"),
                ("inviter", "v", "to invite"), ("respecter les aînés", "-", "to respect one's elders"),
            ]),
            KEY("Three useful rules", "These small rules prevent common mistakes.", cards=[
                ["Mon, ma, mes", "Before a vowel, use mon even for a feminine noun: mon amie, mon école, mon oncle."],
                ["Careful: parents", "Les parents means mother and father, and sometimes relatives in general. To be clear about relatives, say les membres de la famille."],
                ["Same form, two genders", "un enfant / une enfant, un collègue / une collègue, un camarade / une camarade."],
            ]),
            H("A short dialogue"),
            CODE("""Amina : Salut Brice ! Comment va ta famille ?
Brice : Bien, merci. Mon grand frère vient de se marier et toute la famille est venue à Bafoussam pour la fête.
Amina : Félicitations ! Tu as combien de frères et sœurs ?
Brice : J'ai deux frères et une sœur. Je suis le cadet.
Amina : Moi, je suis l'aînée. J'aide ma mère à la maison et nos voisins nous rendent souvent visite.
Brice : Chez nous aussi, l'entraide est très importante.""", "text", title="Dialogue : à la sortie de l'école"),
            T("**In English:** Amina asks how Brice's family is. His older brother has just got married, and the whole family came to Bafoussam for the party. "
              "Brice has two brothers and one sister, and he is the youngest. Amina is the eldest and helps her mother. Both say that mutual help is important in their neighbourhood."),
            EX("Worked example 1: describing a family",
               intro="Write four sentences about the family of Brice, using the vocabulary.",
               steps=[
                   S("Introduce the speaker and the home", text="Je m'appelle Brice. J'habite à Bafoussam avec mes parents, mes deux frères et ma sœur."),
                   S("Jobs of parents (preview)", text="Mon père est enseignant et ma mère est commerçante."),
                   S("Extended family", text="Mon grand-père vit au village. Pendant les vacances, nous rendons visite à notre oncle à Douala."),
                   S("Check the gender and the possessives", text="mes parents (plural), ma sœur (f), mon père (m), ma mère (f), mon grand-père, notre oncle."),
               ]),
            EX("Worked example 2: translation",
               intro="Translate into French: (a) My cousin is getting married next month. (b) She gets on well with her neighbours.",
               steps=[
                   S("(a) Vocabulary", text="my cousin = mon cousin (or ma cousine); to get married = se marier; next month = le mois prochain."),
                   S("(a) Write", text="Mon cousin se marie le mois prochain."),
                   S("(b) Vocabulary", text="to get on well with = s'entendre bien avec; her neighbours = ses voisins."),
                   S("(b) Write", text="Elle s'entend bien avec ses voisins."),
               ]),
            MISTAKE("« ma amie » and « ma école »",
                    "Feminine nouns beginning with a vowel take mon, ton, son: mon amie, ton école, son erreur. The noun stays feminine."),
            MISTAKE("« le femme » or « la fils »",
                    "Check the gender: la femme (f), le fils (m). Learn the article with the noun. Note that grand-mère has no extra e: not « grande-mère »."),
            MISTAKE("Using visiter for a person",
                    "To visit a person is rendre visite à (not visiter). Visiter is for places: visiter Kribi, but rendre visite à ma tante."),
            QUIZ("La sœur de ma mère est ma ___.",
                 ["nièce", "tante", "cousine", "belle-mère"], 1,
                 "The sister of your mother is your aunt: ma tante.",
                 hint="Think of the parent's sister.",
                 feedback=["A nièce is the daughter of your brother or sister.", "", "A cousin is the child of your uncle or aunt.", "A belle-mère is a mother-in-law or stepmother."]),
            QUIZ("Which sentence is correct?",
                 ["Ma amie habite à Douala.", "Mon amie habite à Douala.", "Mes amie habite à Douala.", "Son amie habitent à Douala."], 1,
                 "Before a vowel, the feminine possessive is mon: mon amie.",
                 hint="Amie begins with a vowel.",
                 feedback=["Ma cannot be used before a vowel.", "", "Mes is plural but amie is singular.", "The verb must agree: son amie habite."]),
            TIP("In Paper 1 multiple choice, vocabulary questions often give three words from the right theme and one that fits the grammar of the sentence. "
                "Check the gender, the article and the meaning. Family vocabulary is also essential for the informal letter and the narrative essay in Paper 2.", title="Exam link"),
            PQ("Complete: « Le fils de mon oncle est mon ___. »", "cousin. (the son of an uncle is a male cousin.)"),
            PQ("Write in French: « We visit our grandmother every Sunday. »", "Nous rendons visite à notre grand-mère tous les dimanches. (rendre visite à, not visiter.)"),
            PQ("Choose the correct possessive: « ___ amie s'appelle Aïcha. » (my)", "Mon amie s'appelle Aïcha. (before a vowel, mon.)"),
            PQ("Write a two-sentence description of your neighbourhood using voisin and entraide.", "Model: Dans mon quartier, les voisins s'entendent bien. Chez nous, l'entraide est très importante."),
            SUM("Learn family and social words with their gender (m/f) and in short sentences.",
                "Verbs for events: se marier, naître, rendre visite à, s'entendre bien avec, se disputer.",
                "Use mon, ton, son before a vowel, even for feminine nouns: mon amie.",
                "Beware of traps: parents means parents (and relatives), rendre visite à a person, visiter a place."),
        ],
    ),
]

# ---------------------------------------------------------------------- 10. School and career
LESSONS += [
    lesson(
        module=M4, topic="School and career",
        title="School and career",
        slug="fr2-lex-school-career", minutes=22,
        summary="Vocabulary for school life, subjects, exams, jobs and the world of work, with gender, useful verbs, a dialogue about a future career and the traps réussir, passer un examen and assister à.",
        objectives=[
            "Name people, places, objects and subjects in school life",
            "Talk about exams and results with the right verbs (réussir, échouer, passer un examen)",
            "Name common jobs and workplace words, with the right gender",
            "Avoid false friends such as assister à, collège and étudiant",
        ],
        key_concepts=["L'école", "Les matières", "Les examens", "Les métiers", "Le monde du travail", "Faux amis"],
        blocks=[
            H("Introduction"),
            T("Chaque matin, des milliers d'élèves camerounais prennent le chemin du collège ou du lycée avec leur cartable. "
              "Ils étudient pour réussir leurs examens, puis pour trouver un métier : médecin, infirmière, ingénieur, enseignant, commerçant. "
              "Le vocabulaire de l'école et du travail revient souvent dans les exercices de Paper 1 et dans les essais de Paper 2."),
            D("A **false friend** (*faux ami*) is a French word that looks like an English word but has a different meaning. "
              "For example, a *collège* is a lower secondary school, not a university, and *assister à* means to attend, not to assist.",
              title="Watch for false friends"),
            H("School life"),
            BANK("People and places", [
                ("l'école", "f", "school"), ("le collège", "m", "lower secondary school"), ("le lycée", "m", "upper secondary school"),
                ("l'élève", "mf", "pupil, student at school"), ("l'étudiant, l'étudiante", "mf", "university student"),
                ("le professeur", "m", "teacher (also for a woman)"), ("l'enseignant, l'enseignante", "mf", "teacher"),
                ("le proviseur", "m", "head of a lycée"), ("le directeur, la directrice", "mf", "head, principal"),
                ("la classe", "f", "class, classroom"), ("la salle de classe", "f", "classroom"), ("la bibliothèque", "f", "library"),
                ("la cour", "f", "playground, courtyard"),
            ]),
            BANK("Objects and subjects", [
                ("le cahier", "m", "exercise book"), ("le livre", "m", "book"), ("le stylo", "m", "pen"), ("le cartable", "m", "school bag"),
                ("la règle", "f", "ruler"), ("la calculatrice", "f", "calculator"), ("le tableau", "m", "board"),
                ("l'emploi du temps", "m", "timetable"), ("la matière", "f", "school subject"),
                ("les mathématiques", "f", "mathematics"), ("l'histoire", "f", "history"), ("la géographie", "f", "geography"),
                ("la physique", "f", "physics"), ("l'informatique", "f", "ICT, computing"), ("l'anglais", "m", "English"),
            ]),
            BANK("Exams and study verbs", [
                ("l'examen", "m", "exam"), ("le devoir", "m", "assignment, written test"), ("la note", "f", "mark"),
                ("le bulletin", "m", "report card"), ("le diplôme", "m", "diploma, certificate"), ("la bourse", "f", "scholarship"),
                ("étudier", "v", "to study"), ("apprendre", "v", "to learn"), ("réviser", "v", "to revise"),
                ("passer un examen", "v", "to sit an exam (not: to pass)"), ("réussir à un examen", "v", "to pass an exam"),
                ("échouer à un examen", "v", "to fail an exam"), ("redoubler", "v", "to repeat a year"),
                ("s'inscrire", "v", "to enrol"), ("faire des progrès", "v", "to make progress"),
            ]),
            H("Jobs and the world of work"),
            BANK("Jobs", [
                ("le médecin", "m", "doctor (also for a woman)"), ("l'infirmier, l'infirmière", "mf", "nurse"),
                ("l'ingénieur", "m", "engineer"), ("l'avocat, l'avocate", "mf", "lawyer"), ("le comptable, la comptable", "mf", "accountant"),
                ("l'agriculteur, l'agricultrice", "mf", "farmer"), ("le commerçant, la commerçante", "mf", "trader"),
                ("le mécanicien, la mécanicienne", "mf", "mechanic"), ("le couturier, la couturière", "mf", "tailor, dressmaker"),
                ("le chauffeur", "m", "driver"), ("le journaliste, la journaliste", "mf", "journalist"),
                ("l'informaticien, l'informaticienne", "mf", "computer specialist"),
            ]),
            BANK("Work words", [
                ("le métier", "m", "job, trade"), ("la profession", "f", "profession"), ("l'emploi", "m", "job, employment"),
                ("le salaire", "m", "salary"), ("le chômage", "m", "unemployment"), ("le patron, la patronne", "mf", "boss, owner"),
                ("la formation", "f", "training"), ("le stage", "m", "internship, work placement"),
                ("l'entretien d'embauche", "m", "job interview"), ("le CV", "m", "CV"),
                ("chercher un emploi", "v", "to look for a job"), ("gagner sa vie", "v", "to earn a living"),
                ("embaucher", "v", "to hire"), ("postuler", "v", "to apply for a job"),
            ]),
            T("For the professions *médecin, professeur, ingénieur*, careful French normally keeps the masculine noun for a woman: *Ma mère est médecin.* "
              "Feminine forms such as *une ingénieure* or *une professeure* are used more and more; check your textbook and your teacher's preference. "
              "For the other jobs the feminine is usually formed in the normal way: *infirmier → infirmière, couturier → couturière, agriculteur → agricultrice*."),
            KEY("False friends in this theme", "Learn these pairs for Paper 1.", cards=[
                ["assister à", "to attend (a class, a meeting), not to assist. J'assiste au cours."],
                ["le collège / le lycée", "lower and upper secondary school, not a university."],
                ["passer un examen", "to sit an exam. To pass it: réussir à un examen."],
                ["la lecture", "reading (not a lecture). A lecture is un cours magistral or une conférence."],
            ]),
            H("A short dialogue"),
            CODE("""Mme Fouda : Que voulez-vous faire plus tard, Ngono ?
Ngono : Je veux devenir infirmière, madame. J'aime aider les malades.
Mme Fouda : C'est un beau métier. Il faut réussir à l'examen et suivre une bonne formation.
Ngono : Je révise tous les soirs. Et vous, pourquoi avez-vous choisi l'enseignement ?
Mme Fouda : Parce que j'aime transmettre ce que j'ai appris.""", "text", title="Dialogue : au lycée"),
            T("**In English:** Mrs Fouda asks Ngono what she wants to do later. Ngono wants to become a nurse because she likes helping the sick. "
              "The teacher says she must pass her exam and do good training. Ngono revises every evening, and Mrs Fouda explains that she became a teacher because she likes passing on what she has learned."),
            EX("Worked example 1: exam verbs",
               intro="Complete with passer or réussir (passé composé): « Awa a ___ son examen en juin et elle a ___ . Elle est très contente. »",
               steps=[
                   S("First gap", text="She sat the exam: the participle of passer is passé."),
                   S("Second gap", text="She is happy because she passed: the participle of réussir is réussi."),
                   S("Write", text="Awa a passé son examen en juin et elle a réussi. Elle est très contente."),
               ]),
            EX("Worked example 2: describing a job",
               intro="Write three sentences about a future job using the vocabulary.",
               steps=[
                   S("Say what you want", text="Plus tard, je veux devenir ingénieur."),
                   S("Say what you must do", text="Pour cela, je dois bien réviser et réussir à mes examens."),
                   S("Say why", text="Je veux gagner ma vie et aider mon pays. J'ai déjà fait un stage dans une entreprise."),
               ]),
            MISTAKE("« Il a passé son examen » to mean he passed",
                    "Passer un examen means to sit or take an exam. To say that you passed, use réussir à un examen or être reçu à un examen: Elle a réussi à son examen."),
            MISTAKE("« Je vais assister mon ami » for « I attend class »",
                    "Assister à means to be present at: J'assiste au cours d'anglais. To help someone, say aider quelqu'un."),
            MISTAKE("Wrong gender of school words",
                    "L'école, la matière, la note, la classe are feminine. Le cahier, le stylo, le livre, le métier, le salaire are masculine. Learn each with its article."),
            QUIZ("Which verb means « to pass an exam » ?",
                 ["passer un examen", "réussir à un examen", "échouer à un examen", "redoubler un examen"], 1,
                 "Réussir à un examen means to pass. Passer un examen means to take it.",
                 hint="False friend alert.",
                 feedback=["Passer means to sit the exam.", "", "Échouer means to fail.", "Redoubler means to repeat a year."]),
            QUIZ("Complete: « Il ___ au cours d'histoire tous les lundis. »",
                 ["assiste", "aide", "assistera", "écoute à"], 0,
                 "Assister à = to attend. Il assiste au cours.",
                 hint="Which verb means « to attend » ?",
                 feedback=["", "Aider means to help.", "The sentence is in the présent, not the futur.", "Écouter is not used with à in this way."]),
            TIP("School and career vocabulary appears in Paper 1 multiple choice and is useful in the essay (a letter to a friend about school, a narrative about an exam). "
                "False friends are especially popular in multiple choice because they test whether you know the real French meaning.", title="Exam link"),
            PQ("Complete: « Ma mère est ___ ; elle soigne les malades à l'hôpital. » (profession)", "médecin (or infirmière). A doctor or a nurse who looks after patients."),
            PQ("Write in French: « I revise every evening to pass my exam. »", "Je révise tous les soirs pour réussir à mon examen."),
            PQ("Explain the difference between passer un examen and réussir à un examen.", "Passer un examen = to sit or take the exam. Réussir à un examen = to pass it."),
            PQ("Give the feminine of « le couturier » and of « l'infirmier ».", "la couturière, l'infirmière."),
            SUM("Group school words (people, objects, subjects, exams) and job words, and learn each noun with its article.",
                "Exam verbs: étudier, réviser, passer un examen (sit), réussir à (pass), échouer à (fail).",
                "Many job nouns change in the feminine (infirmier, infirmière); médecin and professeur are often kept in the masculine.",
                "False friends: assister à, collège, étudiant, lecture, passer un examen."),
        ],
    ),
]

# ---------------------------------------------------------------------- 11. Health and sports
LESSONS += [
    lesson(
        module=M4, topic="Health and sports",
        title="Health and sports",
        slug="fr2-lex-health-sports", minutes=22,
        summary="Vocabulary for the body, illness and care, and for sports and matches, with avoir mal à + au/à la/aux, jouer à and faire de, a doctor's-visit dialogue and common traps.",
        objectives=[
            "Name parts of the body and common illnesses and treatments",
            "Say where it hurts with avoir mal à + au, à la, à l', aux",
            "Talk about sports and matches, using jouer à and faire de correctly",
            "Use the vocabulary in a short dialogue at a health centre",
        ],
        key_concepts=["Le corps", "La santé et la maladie", "avoir mal à", "jouer à / faire de", "Le sport"],
        blocks=[
            H("Introduction"),
            T("Au centre de santé de Mbouda, un jeune homme explique : « J'ai de la fièvre et j'ai mal à la tête. » "
              "Le week-end, il joue au football avec ses amis. La santé et le sport sont deux sujets très fréquents dans les textes et les exercices de français."),
            T("This lesson is a language lesson. It teaches you the words to describe health and sport. It is not medical advice: if you are ill, see a health worker."),
            H("The body and health"),
            BANK("The body", [
                ("la tête", "f", "head"), ("le visage", "m", "face"), ("l'œil (pl. les yeux)", "m", "eye"), ("l'oreille", "f", "ear"),
                ("le nez", "m", "nose"), ("la bouche", "f", "mouth"), ("la dent", "f", "tooth"), ("la gorge", "f", "throat"),
                ("le dos", "m", "back"), ("le ventre", "m", "stomach, belly"), ("le bras", "m", "arm"), ("la main", "f", "hand"),
                ("la jambe", "f", "leg"), ("le genou", "m", "knee"), ("le pied", "m", "foot"), ("le cœur", "m", "heart"),
            ]),
            BANK("Illness and care", [
                ("la santé", "f", "health"), ("la maladie", "f", "illness"), ("le malade, la malade", "mf", "sick person, patient"),
                ("le médecin", "m", "doctor"), ("l'infirmier, l'infirmière", "mf", "nurse"), ("l'hôpital", "m", "hospital"),
                ("le centre de santé", "m", "health centre"), ("la pharmacie", "f", "pharmacy"), ("l'ordonnance", "f", "prescription"),
                ("le médicament", "m", "medicine"), ("le vaccin", "m", "vaccine"), ("la fièvre", "f", "fever"),
                ("la toux", "f", "cough"), ("le rhume", "m", "cold"), ("le paludisme", "m", "malaria"),
                ("la douleur", "f", "pain"), ("la blessure", "f", "injury"), ("la moustiquaire", "f", "mosquito net"),
            ]),
            BANK("Verbs and phrases", [
                ("tousser", "v", "to cough"), ("se sentir fatigué", "v", "to feel tired"), ("se soigner", "v", "to look after oneself, to get treated"),
                ("guérir", "v", "to recover, to cure"), ("prendre un médicament", "v", "to take medicine"),
                ("se reposer", "v", "to rest"), ("se faire vacciner", "v", "to get vaccinated"), ("être en bonne santé", "-", "to be in good health"),
                ("avoir de la fièvre", "-", "to have a fever"), ("avoir mal à", "-", "to have a pain in"),
            ]),
            H("Avoir mal à"),
            D("To say that a part of the body hurts, use **avoir mal à** + the part. The word **à** joins with the article: "
              "**à + le = au**, **à + les = aux**, **à la** and **à l'** do not change.",
              title="Avoir mal à + body part"),
            CODE("""J'ai mal à la tête.      (la tête)
J'ai mal au ventre.      (le ventre)
J'ai mal aux dents.      (les dents)
J'ai mal à l'oreille.    (l'oreille)
Il a mal au dos.
Elle a mal aux jambes.""", "text", title="Where does it hurt?"),
            H("Sports"),
            BANK("Sports and matches", [
                ("le sport", "m", "sport"), ("le football", "m", "football"), ("le basket-ball", "m", "basketball"),
                ("le handball", "m", "handball"), ("le volley-ball", "m", "volleyball"), ("l'athlétisme", "m", "athletics"),
                ("la course", "f", "race, running"), ("la natation", "f", "swimming"), ("le match", "m", "match"),
                ("l'équipe", "f", "team"), ("le joueur, la joueuse", "mf", "player"), ("l'entraîneur", "m", "coach"),
                ("l'arbitre", "mf", "referee"), ("le stade", "m", "stadium"), ("le terrain", "m", "pitch, field"),
                ("le ballon", "m", "ball"), ("le but", "m", "goal"),
            ]),
            BANK("Sport verbs", [
                ("jouer au football", "v", "to play football"), ("faire du sport", "v", "to do sport"), ("s'entraîner", "v", "to train"),
                ("marquer un but", "v", "to score a goal"), ("gagner", "v", "to win"), ("perdre", "v", "to lose"),
                ("faire match nul", "v", "to draw"), ("courir", "v", "to run"), ("nager", "v", "to swim"),
            ]),
            KEY("Jouer à or faire de ?", "Two patterns for sport.", cards=[
                ["jouer à + team or ball game", "jouer au football, jouer au basket, jouer au volley. In everyday speech you also hear faire du foot, but jouer au is the safe form."],
                ["faire de + individual sport", "faire de la natation, faire de l'athlétisme, faire du vélo"],
                ["Note", "Les Lions Indomptables is the name of the Cameroon national football team."],
            ]),
            H("Dialogue"),
            CODE("""Le médecin : Bonjour, qu'est-ce qui ne va pas ?
Le patient : J'ai de la fièvre et j'ai mal à la tête depuis hier.
Le médecin : Avez-vous de la toux ?
Le patient : Non, mais je me sens très fatigué.
Le médecin : Je vous prescris des médicaments. Reposez-vous et buvez beaucoup d'eau. Dormez sous une moustiquaire.
Le patient : Merci, docteur.""", "text", title="Dialogue : au centre de santé"),
            T("**In English:** The doctor asks what is wrong. The patient has had a fever and a headache since yesterday and feels very tired. "
              "The doctor gives him medicine and tells him to rest, drink plenty of water and sleep under a mosquito net."),
            EX("Worked example 1: avoir mal à",
               intro="Say in French: (a) She has a stomach ache. (b) I have toothache. (c) He has a pain in the ear.",
               steps=[
                   S("(a) le ventre", text="à + le = au: Elle a mal au ventre."),
                   S("(b) les dents", text="à + les = aux: J'ai mal aux dents."),
                   S("(c) l'oreille", text="à l' does not change: Il a mal à l'oreille."),
               ]),
            EX("Worked example 2: jouer à or faire de",
               intro="Complete: « Mon frère joue ___ basket et ma sœur fait ___ natation. »",
               steps=[
                   S("Basketball is a ball game", text="jouer au basket (à + le = au)."),
                   S("Swimming is an individual sport", text="faire de la natation."),
                   S("Write", text="Mon frère joue au basket et ma sœur fait de la natation."),
               ]),
            MISTAKE("« J'ai mal à le ventre »",
                    "Always contract à + le = au and à + les = aux: J'ai mal au ventre, j'ai mal aux dents."),
            MISTAKE("« J'ai le mal à la tête » or « je suis mal à la tête »",
                    "Say J'ai mal à la tête, with no article before mal. Je suis malade means I am ill; Je me sens mal means I feel unwell."),
            MISTAKE("« jouer le football » or « faire le football »",
                    "For ball games and team sports, use jouer à: jouer au football. For other sports, use faire de: faire de l'athlétisme."),
            QUIZ("Which sentence is correct?",
                 ["Il a mal à le dos.", "Il a mal au dos.", "Il a mal à dos.", "Il a mal du dos."], 1,
                 "À + le = au: il a mal au dos.",
                 hint="Contract à with le.",
                 feedback=["À le must become au.", "", "The article is missing.", "Avoir mal is followed by à, not de."]),
            QUIZ("Complete: « Les garçons ___ au football le samedi. »",
                 ["font", "jouent", "sont", "ont"], 1,
                 "A team ball game takes jouer à: jouent au football.",
                 hint="Football is a team sport.",
                 feedback=["Faire is followed by du or de, not au.", "", "Être does not fit the meaning.", "Avoir does not fit the meaning."]),
            TIP("In Paper 1, health and sports vocabulary may appear in a gap sentence (choose avoir mal au/à la/aux) or a context question. "
                "In Paper 2, you may need these words in a narrative about an accident or a malaise, or a match.", title="Exam link"),
            PQ("Write in French: « I have a headache and a fever. »", "J'ai mal à la tête et j'ai de la fièvre."),
            PQ("Complete: « Il a mal ___ jambes. »", "aux. (à + les = aux.)"),
            PQ("Complete: « Elle ___ de la natation tous les mercredis. »", "fait. (faire de + individual sport.)"),
            PQ("Write two sentences about a football match using joueur, but and gagner.", "Model: Le joueur marque un but. Notre équipe gagne le match."),
            SUM("Learn body parts, illnesses and care words with their gender.",
                "Avoir mal à + body part: au, aux, à la, à l'.",
                "Sports: jouer à for team or ball games, faire de for other sports.",
                "Use the vocabulary in dialogues at the health centre and in sports reports."),
        ],
    ),
]

# ---------------------------------------------------------------------- 12. Travel and transport
LESSONS += [
    lesson(
        module=M4, topic="Travel and transport",
        title="Travel and transport",
        slug="fr2-lex-travel-transport", minutes=22,
        summary="Vocabulary for vehicles, stations, roads, tickets and journeys, the prepositions en and à with transport (en car, à pied), il faut + infinitive, and a dialogue at a bus station.",
        objectives=[
            "Name vehicles, places, documents and problems on a journey",
            "Use en and à correctly with means of transport (en car, à moto, à pied)",
            "Buy a ticket and ask for information in a short dialogue",
            "Use il faut, venir de and aller to talk about journeys",
        ],
        key_concepts=["Les moyens de transport", "La gare routière", "En / à + transport", "Il faut + infinitif", "Le voyage"],
        blocks=[
            H("Introduction"),
            T("Pour aller de Yaoundé à Douala, on peut prendre le car ou le train. Pour aller à Kribi ou à Limbé, on voyage souvent en car. "
              "En ville, on prend un taxi ou une moto-taxi, et beaucoup d'élèves vont à l'école à pied. "
              "Le thème « voyage et transport » est très fréquent dans les textes et les rédactions."),
            H("Vehicles and places"),
            BANK("Means of transport", [
                ("le moyen de transport", "m", "means of transport"), ("la voiture", "f", "car"), ("le car", "m", "coach, intercity bus"),
                ("le bus", "m", "bus"), ("le taxi", "m", "taxi"), ("la moto", "f", "motorcycle"), ("le vélo", "m", "bicycle"),
                ("le camion", "m", "lorry, truck"), ("le train", "m", "train"), ("l'avion", "m", "aeroplane"),
                ("le bateau", "m", "boat"), ("la pirogue", "f", "dugout canoe"),
            ]),
            BANK("Places and roads", [
                ("la gare", "f", "railway station"), ("la gare routière", "f", "bus or coach station"), ("l'aéroport", "m", "airport"),
                ("le port", "m", "port"), ("l'arrêt de bus", "m", "bus stop"), ("la route", "f", "road"), ("la rue", "f", "street"),
                ("le carrefour", "m", "crossroads, junction"), ("le rond-point", "m", "roundabout"), ("le pont", "m", "bridge"),
                ("le feu rouge", "m", "red light"), ("la frontière", "f", "border"), ("la douane", "f", "customs"),
            ]),
            BANK("Journey words", [
                ("le voyage", "m", "journey, trip"), ("le trajet", "m", "journey, route (distance covered)"), ("le voyageur, la voyageuse", "mf", "traveller"),
                ("le passager, la passagère", "mf", "passenger"), ("le chauffeur", "m", "driver"), ("le billet", "m", "ticket"),
                ("le guichet", "m", "ticket window"), ("l'horaire", "m", "timetable"), ("le départ", "m", "departure"),
                ("l'arrivée", "f", "arrival"), ("le retard", "m", "delay"), ("la panne", "f", "breakdown"),
                ("l'embouteillage", "m", "traffic jam"), ("l'accident", "m", "accident"), ("le bagage, la valise", "m / f", "luggage, suitcase"),
                ("le passeport", "m", "passport"), ("la ceinture de sécurité", "f", "seat belt"), ("le casque", "m", "helmet"),
            ]),
            BANK("Verbs", [
                ("voyager", "v", "to travel"), ("partir", "v", "to leave"), ("arriver", "v", "to arrive"), ("prendre le car", "v", "to take the coach"),
                ("monter dans", "v", "to get into / on"), ("descendre de", "v", "to get off / out of"), ("réserver", "v", "to book"),
                ("acheter un billet", "v", "to buy a ticket"), ("rater le car", "v", "to miss the coach"), ("conduire", "v", "to drive"),
                ("traverser", "v", "to cross"), ("attendre", "v", "to wait"), ("décoller", "v", "to take off"), ("atterrir", "v", "to land"),
            ]),
            KEY("En or à with transport?", "Learn this contrast.", cards=[
                ["en + vehicle you get into", "en voiture, en car, en train, en avion, en bateau, en taxi"],
                ["à + open or personal transport", "à pied, à vélo, à moto"],
                ["Il faut + infinitive", "Il faut arriver tôt. (You must arrive early.)"],
            ]),
            H("Dialogue"),
            CODE("""Le voyageur : Bonjour, je voudrais un billet pour Douala, s'il vous plaît.
La vendeuse : C'est pour quand ?
Le voyageur : Pour demain matin. À quelle heure part le car ?
La vendeuse : À sept heures. Il faut arriver trente minutes avant.
Le voyageur : Puis-je mettre mon sac dans la soute ?
La vendeuse : Oui, mais gardez votre pièce d'identité avec vous.""", "text", title="Dialogue : à la gare routière"),
            T("**In English:** A traveller asks for a ticket to Douala for tomorrow morning. The seller says the coach leaves at seven, and that he must arrive thirty minutes early. "
              "He asks if he can put his bag in the luggage hold, and she tells him to keep his identity document with him."),
            EX("Worked example 1: en or à",
               intro="Complete: (a) Je vais à Kribi ___ car. (b) Les élèves vont à l'école ___ pied. (c) Mon oncle voyage ___ avion.",
               steps=[
                   S("(a) car", text="en car."),
                   S("(b) pied", text="à pied."),
                   S("(c) avion", text="en avion."),
                   S("Write", text="(a) en (b) à (c) en."),
               ]),
            EX("Worked example 2: buying a ticket",
               intro="Write the question: you want to know the departure time of the coach to Garoua.",
               steps=[
                   S("Question word", text="à quelle heure (at what time)."),
                   S("Verb and subject", text="partir, le car pour Garoua."),
                   S("Write", text="À quelle heure part le car pour Garoua ?"),
               ]),
            MISTAKE("« Je vais à Douala à car »",
                    "With a vehicle you sit in, use en: en car, en voiture, en train. Use à for à pied, à vélo, à moto."),
            MISTAKE("Using voyager for a short trip",
                    "Voyager is for a trip to another town or country. For going to school or to the market, say aller or prendre le taxi."),
            MISTAKE("« Je rate le car » for « I take the coach »",
                    "Rater means to miss: J'ai raté le car. To take it, say prendre le car."),
            QUIZ("Complete: « Pour aller au marché, ma mère prend le taxi et mon frère y va ___ . »",
                 ["à pied", "en pied", "en pieds", "à pieds"], 0,
                 "The expression is à pied.",
                 hint="Walking is a fixed expression.",
                 feedback=["", "En is not used with pied.", "Pied does not take a plural or en.", "The expression is singular: à pied."]),
            QUIZ("Which word means « a delay » ?",
                 ["une panne", "un retard", "un trajet", "un bagage"], 1,
                 "Un retard is a delay. Une panne is a breakdown.",
                 hint="The coach arrives later than planned.",
                 feedback=["Une panne is a breakdown.", "", "Un trajet is a journey.", "Un bagage is luggage."]),
            TIP("Travel vocabulary is common in Paper 1 gap questions (en or à, the right noun) and in essay topics about a journey, an accident or a holiday. "
                "Learn a few words for breakdowns and delays, because narrative essays often include a problem on the way.", title="Exam link"),
            PQ("Complete: « Nous allons à Garoua ___ train. »", "en. (en train.)"),
            PQ("Translate: « The coach left late because of a breakdown. »", "Le car est parti en retard à cause d'une panne."),
            PQ("Write in French: « You must arrive early. »", "Il faut arriver tôt."),
            PQ("Write a question to buy a ticket for Bamenda.", "Je voudrais un billet pour Bamenda, s'il vous plaît. (or: Combien coûte un billet pour Bamenda ?)"),
            SUM("Learn vehicles, places, journey words and verbs with their gender.",
                "Use en with vehicles (en car, en avion) and à for à pied, à vélo, à moto.",
                "Il faut + infinitive expresses necessity.",
                "Rater = to miss; prendre = to take; descendre de and monter dans for getting off and on."),
        ],
    ),
]

# ---------------------------------------------------------------------- 13. Environment and climate
LESSONS += [
    lesson(
        module=M4, topic="Environment and climate",
        title="Environment and climate",
        slug="fr2-lex-environment-climate", minutes=22,
        summary="Vocabulary for nature, weather, seasons, environmental problems and solutions, with weather expressions (il pleut, il fait chaud), a dialogue about a clean-up, and the false friend le temps.",
        objectives=[
            "Name features of nature, the seasons and the weather",
            "Describe environmental problems (pollution, déchets, déforestation, inondations)",
            "Propose solutions using verbs such as protéger, planter, trier, économiser",
            "Use weather expressions correctly (il pleut, il fait chaud, il y a du vent)",
        ],
        key_concepts=["La nature", "Le climat et le temps", "Les problèmes de l'environnement", "Les solutions", "Expressions météo"],
        blocks=[
            H("Introduction"),
            T("Le Cameroun est un pays de contrastes : la forêt équatoriale du Sud, les savanes de l'Adamaoua, le mont Cameroun près de la côte et le climat plus sec du Nord. "
              "Mais la déforestation, les déchets plastiques et les inondations inquiètent les habitants. Dans les examens, le thème de l'environnement revient souvent."),
            H("Nature and landscape"),
            BANK("Nature", [
                ("l'environnement", "m", "environment"), ("la nature", "f", "nature"), ("la forêt", "f", "forest"),
                ("la savane", "f", "savannah"), ("la montagne", "f", "mountain"), ("le volcan", "m", "volcano"),
                ("le fleuve", "m", "large river flowing to the sea"), ("la rivière", "f", "river"), ("le lac", "m", "lake"),
                ("la mer", "f", "sea"), ("la plage", "f", "beach"), ("la côte", "f", "coast"), ("le sol", "m", "soil, ground"),
                ("l'arbre", "m", "tree"), ("la plante", "f", "plant"), ("l'animal", "m", "animal"), ("le parc national", "m", "national park"),
            ]),
            H("Climate and weather"),
            BANK("Climate and weather", [
                ("le climat", "m", "climate"), ("le temps", "m", "weather (and time)"), ("la saison", "f", "season"),
                ("la saison des pluies", "f", "rainy season"), ("la saison sèche", "f", "dry season"), ("la pluie", "f", "rain"),
                ("le soleil", "m", "sun"), ("la chaleur", "f", "heat"), ("le vent", "m", "wind"), ("l'orage", "m", "storm"),
                ("le brouillard", "m", "fog"), ("la température", "f", "temperature"), ("la sécheresse", "f", "drought"),
                ("l'inondation", "f", "flood"), ("le réchauffement climatique", "m", "global warming"),
            ]),
            CODE("""Il pleut.                 It is raining.
Il fait chaud.            It is hot.
Il fait froid.            It is cold.
Il fait beau.             The weather is fine.
Il fait du vent.          It is windy.  (also: Il y a du vent.)
Il y a de l'orage.        There is a storm.
Il y a du brouillard.     It is foggy.
Quel temps fait-il ?      What is the weather like?""", "text", title="Weather expressions"),
            H("Problems and solutions"),
            BANK("Problems", [
                ("la pollution", "f", "pollution"), ("les déchets", "m", "waste"), ("les ordures", "f", "rubbish"),
                ("le plastique", "m", "plastic"), ("le sachet plastique", "m", "plastic bag"), ("la déforestation", "f", "deforestation"),
                ("l'érosion", "f", "erosion"), ("la catastrophe naturelle", "f", "natural disaster"),
                ("le glissement de terrain", "m", "landslide"), ("l'espèce en voie de disparition", "f", "endangered species"),
            ]),
            BANK("Solutions", [
                ("protéger", "v", "to protect"), ("préserver", "v", "to preserve"), ("planter des arbres", "v", "to plant trees"),
                ("reboiser", "v", "to replant forest"), ("trier les déchets", "v", "to sort waste"), ("recycler", "v", "to recycle"),
                ("économiser l'eau", "v", "to save water"), ("nettoyer le quartier", "v", "to clean the neighbourhood"),
                ("sensibiliser", "v", "to raise awareness"), ("l'énergie solaire", "f", "solar energy"),
            ]),
            KEY("Faux ami and agreement", "Two points for Paper 1.", cards=[
                ["le temps", "means both weather and time. Quel temps fait-il ? = What is the weather like? Je n'ai pas le temps = I have no time."],
                ["il faut / on doit", "Il faut protéger la forêt. On doit trier les déchets. (necessity)"],
                ["Plural nouns", "les déchets and les ordures are normally used in the plural in French: Les déchets sont dangereux."],
            ]),
            H("Dialogue"),
            CODE("""Léa : Ce samedi, le club de l'environnement nettoie le quartier.
Marc : Super idée ! Il y a trop de sachets plastiques dans la rue.
Léa : Oui, et après la pluie, ils bouchent les caniveaux. Les inondations arrivent plus vite.
Marc : Nous pouvons aussi planter des arbres devant l'école.
Léa : Bonne idée. Les arbres donnent de l'ombre et protègent le sol.""", "text", title="Dialogue : le club de l'environnement"),
            T("**In English:** Léa tells Marc that the environment club will clean the neighbourhood on Saturday. Marc notes that there are too many plastic bags on the street. "
              "Léa says that after the rain they block the drains, so floods come faster. They also decide to plant trees in front of the school, because trees give shade and protect the soil."),
            EX("Worked example 1: weather",
               intro="Say in French: (a) It is raining. (b) It is very hot in Garoua in April. (c) What is the weather like?",
               steps=[
                   S("(a)", text="Il pleut."),
                   S("(b)", text="Il fait très chaud à Garoua en avril. (Use fait, not est, with chaud.)"),
                   S("(c)", text="Quel temps fait-il ?"),
               ]),
            EX("Worked example 2: a problem and a solution",
               intro="Write two sentences about a problem in your area and one solution.",
               steps=[
                   S("The problem", text="Dans notre quartier, il y a beaucoup de déchets dans la rue."),
                   S("The consequence", text="Après la pluie, les déchets bouchent les caniveaux et l'eau inonde les maisons."),
                   S("The solution", text="Il faut trier les déchets et nettoyer le quartier chaque mois."),
               ]),
            MISTAKE("« Il est chaud » for « It is hot »",
                    "For the weather say il fait chaud (faire). Il est chaud would describe an object, such as a cup of tea."),
            MISTAKE("Confusing le fleuve and la rivière",
                    "A fleuve flows to the sea (le Wouri flows to the Atlantic near Douala). A rivière flows into another river. Check your textbook for the examples it uses."),
            MISTAKE("Wrong article",
                    "Le sol, le climat, le plastique are masculine; la pollution, la forêt, la sécheresse are feminine. Learn the article with each noun."),
            QUIZ("Which sentence means « It is cold » ?",
                 ["Il est froid.", "Il fait froid.", "Il a froid.", "Il pleut froid."], 1,
                 "For weather, use il fait froid. Il a froid means he feels cold.",
                 hint="The weather uses faire.",
                 feedback=["Il est froid describes an object.", "", "Il a froid: a person feels cold.", "Not a French expression."]),
            QUIZ("Which verb best completes: « Il faut ___ les déchets pour protéger l'environnement » ?",
                 ["polluer", "trier", "oublier", "gaspiller"], 1,
                 "Trier les déchets means to sort waste, which protects the environment.",
                 hint="Which action is a solution?",
                 feedback=["Polluer is the problem.", "", "Oublier means to forget.", "Gaspiller means to waste."]),
            TIP("Environment and climate vocabulary is useful for Paper 1 gap questions and for the essay (a letter to a friend about a flood, an argumentative piece on plastic bags). "
                "The Board's 2023 report links its essay topics to themes such as ICT and health and the environment, so build a list of words for causes, consequences and solutions.", title="Exam link"),
            PQ("Write in French: « It is windy and it is going to rain. »", "Il fait du vent et il va pleuvoir."),
            PQ("Complete: « Les ___ plastiques bouchent les caniveaux. » (sachets / sachet)", "sachets. (plural: les sachets.)"),
            PQ("Give two solutions to the problem of waste in a neighbourhood.", "Model: trier les déchets; nettoyer le quartier; planter des arbres; sensibiliser les habitants."),
            PQ("What is the difference between le temps and la saison?", "Le temps is the weather (or time); la saison is a season of the year (saison sèche, saison des pluies)."),
            SUM("Learn nature, weather, problems and solutions with the article of each noun.",
                "Weather expressions: il pleut, il fait chaud, il fait froid, il y a du vent.",
                "Solutions use verbs such as protéger, planter, trier, recycler, sensibiliser.",
                "Le temps means both weather and time."),
        ],
    ),
]

# ---------------------------------------------------------------------- 14. Media and ICT
LESSONS += [
    lesson(
        module=M4, topic="Media and ICT",
        title="Media and ICT",
        slug="fr2-lex-media-ict", minutes=22,
        summary="Vocabulary for the press, radio, television, computers, phones and the Internet, with verbs (télécharger, se connecter), advice on fake news and passwords, a cybercafé dialogue and the false friend les nouvelles.",
        objectives=[
            "Name the main media and the people who work in them",
            "Name devices, software and Internet words (ordinateur, application, réseau social)",
            "Use common ICT verbs (télécharger, envoyer, se connecter, partager)",
            "Talk about advantages and dangers of the Internet, including fausses informations",
        ],
        key_concepts=["Les médias", "Les TIC", "Les verbes du numérique", "Les réseaux sociaux", "Les fausses informations"],
        blocks=[
            H("Introduction"),
            T("Au Cameroun, beaucoup de jeunes écoutent la radio, regardent la télévision et utilisent le téléphone portable pour aller sur Internet. "
              "Les TIC (technologies de l'information et de la communication) changent la vie de tous les jours : écrire un message, chercher un renseignement, payer ou apprendre à distance."),
            T("The Board's 2023 report mentions an essay topic about fake news spread on social media, so this theme can be useful both for vocabulary and for composition."),
            H("The media"),
            BANK("Media", [
                ("les médias", "m", "the media"), ("la télévision, la télé", "f", "television"), ("la radio", "f", "radio"),
                ("le journal (pl. les journaux)", "m", "newspaper"), ("le magazine", "m", "magazine"), ("l'article", "m", "article"),
                ("l'émission", "f", "programme"), ("le reportage", "m", "report"), ("l'information, les informations", "f", "piece of news, the news"),
                ("l'actualité", "f", "current events"), ("la chaîne", "f", "channel"), ("la publicité", "f", "advertisement"),
                ("le journaliste, la journaliste", "mf", "journalist"), ("le présentateur, la présentatrice", "mf", "presenter"),
                ("le téléspectateur", "m", "television viewer"), ("l'auditeur, l'auditrice", "mf", "radio listener"),
            ]),
            H("Devices and the Internet"),
            BANK("Devices", [
                ("l'ordinateur (portable)", "m", "computer (laptop)"), ("la tablette", "f", "tablet"),
                ("le téléphone portable, le portable", "m", "mobile phone"), ("l'écran", "m", "screen"), ("le clavier", "m", "keyboard"),
                ("la souris", "f", "mouse"), ("l'imprimante", "f", "printer"), ("la clé USB", "f", "USB stick"),
                ("la batterie", "f", "battery"), ("le chargeur", "m", "charger"),
            ]),
            BANK("Internet words", [
                ("Internet", "-", "the Internet"), ("le site web", "m", "website"), ("la page", "f", "page"),
                ("le réseau social (pl. les réseaux sociaux)", "m", "social network"), ("l'application", "f", "app"),
                ("le logiciel", "m", "software"), ("le fichier", "m", "file"), ("le mot de passe", "m", "password"),
                ("la connexion", "f", "connection"), ("les données mobiles", "f", "mobile data"), ("le forfait", "m", "data or airtime bundle"),
                ("le message, le SMS", "m", "message, text"), ("l'e-mail, le courriel", "m", "e-mail"),
                ("la fausse information, l'infox", "f", "fake news"),
            ]),
            BANK("Verbs", [
                ("allumer / éteindre", "v", "to switch on / off"), ("cliquer", "v", "to click"), ("taper", "v", "to type"),
                ("télécharger", "v", "to download"), ("envoyer / recevoir", "v", "to send / receive"), ("se connecter", "v", "to log in, to connect"),
                ("se déconnecter", "v", "to log out"), ("naviguer", "v", "to browse"), ("chercher sur Internet", "v", "to search the Internet"),
                ("partager", "v", "to share"), ("publier", "v", "to post, to publish"), ("sauvegarder", "v", "to save"),
                ("imprimer", "v", "to print"), ("recharger", "v", "to recharge"), ("vérifier", "v", "to check"),
            ]),
            KEY("False friends and advice", "Points to remember.", cards=[
                ["les nouvelles / les informations", "Les nouvelles = news that someone gives you (Donne-moi de tes nouvelles). Les informations = the news on radio or television."],
                ["Internet", "is used without an article after sur: sur Internet, un site Internet."],
                ["Safe use", "Ne partagez jamais votre mot de passe. Vérifiez la source avant de partager une information."],
            ]),
            H("Dialogue"),
            CODE("""Paul : Je voudrais imprimer mon devoir, mais ma clé USB ne marche pas.
L'employée : Essayez de vous connecter à votre messagerie et d'envoyer le fichier par e-mail.
Paul : Bonne idée. Je tape mon mot de passe... Voilà.
L'employée : Attention, ne partagez jamais votre mot de passe.
Paul : Vous avez raison. Merci, madame.""", "text", title="Dialogue : au cybercafé"),
            T("**In English:** Paul wants to print his homework, but his USB stick does not work. The employee suggests logging in to his e-mail and sending the file. "
              "Paul types his password, and the employee reminds him never to share it."),
            EX("Worked example 1: matching words",
               intro="Which word fits? (a) On l'utilise pour écrire sur l'ordinateur. (b) On le lit chaque matin pour avoir les actualités. (c) On l'écoute à la maison.",
               steps=[
                   S("(a) keyboard", text="le clavier."),
                   S("(b) newspaper", text="le journal."),
                   S("(c) radio", text="la radio."),
               ]),
            EX("Worked example 2: advantages and dangers",
               intro="Write three sentences on Internet use by teenagers.",
               steps=[
                   S("Advantage", text="Internet permet de chercher des informations et de rester en contact avec ses amis."),
                   S("Danger", text="Mais on peut aussi y trouver de fausses informations, il faut donc vérifier la source."),
                   S("Advice", text="Il ne faut jamais partager son mot de passe."),
               ]),
            MISTAKE("Wrong gender of ICT words",
                    "Le clavier, le logiciel, le fichier, l'écran, l'e-mail are masculine; la souris, la clé USB, l'application, l'imprimante, la page are feminine. Learn the article."),
            MISTAKE("« télécharger » for « to upload »",
                    "Télécharger means to download. To upload, say téléverser or mettre en ligne, which is useful to know but less common in simple texts."),
            MISTAKE("« les nouvelles » for « the news on TV »",
                    "For news on television or radio, say les informations (or le journal télévisé). Les nouvelles are news you receive from a person."),
            QUIZ("Which word means « password » ?",
                 ["le logiciel", "le fichier", "le mot de passe", "le forfait"], 2,
                 "Le mot de passe is the password.",
                 hint="Think of a secret word.",
                 feedback=["Le logiciel is software.", "Le fichier is a file.", "", "Le forfait is a data or airtime bundle."]),
            QUIZ("Complete: « Je ___ une photo sur les réseaux sociaux. »",
                 ["publie", "imprime", "télécharge", "éteins"], 0,
                 "Publier means to post, so it fits with réseaux sociaux.",
                 hint="You put the photo online.",
                 feedback=["", "Imprimer means to print.", "Télécharger means to download.", "Éteindre means to switch off."]),
            TIP("ICT and media vocabulary appears in Paper 1 gap questions and in the essay. A good argumentative essay on social media can use connectors from the previous lessons, "
                "such as bien que, parce que, c'est pourquoi and afin de.", title="Exam link"),
            PQ("Complete: « Pour envoyer un e-mail, il faut d'abord se ___ à sa messagerie. »", "connecter. (se connecter = to log in.)"),
            PQ("Translate: « I download the file and I print it. »", "Je télécharge le fichier et je l'imprime."),
            PQ("Write in French: « Never share your password. »", "Ne partagez jamais votre mot de passe. (or: Ne partage jamais ton mot de passe.)"),
            PQ("Give one advantage and one danger of social networks.", "Model: Les réseaux sociaux permettent de communiquer avec ses amis. Mais on peut y rencontrer de fausses informations."),
            SUM("Learn media, device, Internet and verb words with the gender of each noun.",
                "Verbs: télécharger (download), se connecter, envoyer, publier, partager, sauvegarder.",
                "Les informations = news on TV or radio; les nouvelles = news from a person.",
                "Be careful online: protect your password and check sources before sharing."),
        ],
    ),
]
