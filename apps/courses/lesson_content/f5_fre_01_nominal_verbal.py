"""Form 5 French (O Level 0545), modules "Morphologie et Syntaxe Nominale" and "Système Verbal et Concordance des Temps".
Draft content: explanations in English, examples in French. Check against the official syllabus and your textbook
(à vérifier dans votre manuel)."""

from .dsl import *  # noqa: F403

COURSE = ("french", "form-5")

M1 = "Morphologie et Syntaxe Nominale"
M2 = "Système Verbal et Concordance des Temps"

LESSONS = []


# ---------------------------------------------------------------------- 1. Articles: definite and indefinite
LESSONS += [
    lesson(
        module=M1,
        topic="Articles",
        title="Definite and indefinite articles",
        slug="fr1-articles-definite-indefinite",
        minutes=20,
        summary="French nouns are almost always introduced by an article. Use le, la, l', les for known or general things, and un, une, des for things mentioned for the first time. The article must agree in gender and number with the noun.",
        objectives=[
            "Choose le, la, l' or les according to the gender, number and first letter of the noun",
            "Choose un, une or des to introduce a new person or thing",
            "Decide when French uses a definite article where English uses none (likes, general ideas, days)",
            "Recognise when no article is used (professions after être, most languages after parler)",
        ],
        key_concepts=["Article défini", "Article indéfini", "Élision", "Genre", "Nombre"],
        blocks=[
            H("Introduction"),
            T("At Mokolo Market, Mama Esther says: «J'ai des mangues, une papaye et le meilleur poisson de la ville.» "
              "In French, almost every noun comes with a small word in front of it. That word is the **article**. "
              "In English you can say «I like football» with no article. In French you must say «J'aime le football»."),
            T("The article also tells you the **gender** (masculine or feminine) and the **number** (singular or plural) of the noun. "
              "That is why we learn a noun together with its article: *un taxi*, *une école*, not just *taxi* and *école*."),
            H("The definite article"),
            D("The **definite article** (article défini) points to a particular thing that both speakers know, or to a whole group or idea in general. "
              "It is the equivalent of English *the* (and sometimes of no word at all).", title="Definition"),
            CODE("""            masculin    féminin
singulier   le garçon    la fille
            l'homme     l'école
pluriel     les garçons  les filles""", "text", title="Le, la, l', les"),
            T("**Élision.** Le and la become **l'** in front of a vowel (a, e, i, o, u, é...) or a silent h: *l'élève*, *l'hôpital*, *l'homme*. "
              "Some words begin with an *aspirated* h and do not take élision: *le héros*, *la honte*. "
              "The dictionary shows these words with a mark (often an asterisk or a small sign). Learn them as exceptions."),
            KEY("Use the definite article for", "Three common situations.", cards=[
                ["A known thing", "Le taxi est devant la maison. (We both know which taxi.)"],
                ["A general idea or a liking", "J'adore le manioc. Les Camerounais aiment le football."],
                ["A repeated day", "Le samedi, je vais au marché. (every Saturday). Compare: Samedi, je vais au marché. (this coming Saturday)."],
            ]),
            H("The indefinite article"),
            D("The **indefinite article** (article indéfini) introduces a person or thing for the first time or says 'one of several'. "
              "The forms are **un** (masculine), **une** (feminine) and **des** (plural for both genders).", title="Definition"),
            CODE("""            masculin    féminin
singulier   un cahier    une table
pluriel     des cahiers  des tables""", "text", title="Un, une, des"),
            T("English has no plural of *a*, so *des* is often not translated: *J'ai des amis à Douala* = I have friends in Douala. "
              "Never leave the noun without an article in French just because English has none."),
            EX("Worked example 1: choosing the article", intro="Complete: «___ élève est dans ___ classe.»", steps=[
                S("Find the first noun", text="*Élève* begins with a vowel, so the singular definite article is shortened."),
                S("Choose the first article", text="Here the speaker means a known pupil, so we use l'. The word élève can be masculine or feminine, so l' fits both."),
                S("Find the gender of the second noun", text="*Classe* is feminine, singular. The known class takes la."),
                S("Write the sentence", text="L'élève est dans la classe."),
            ]),
            EX("Worked example 2: first mention, then known", intro="Complete: «Il y a ___ taxi devant le collège. ___ taxi est jaune.»", steps=[
                S("First sentence", text="The taxi is new in the story, so we use the indefinite article. *Taxi* is masculine: un taxi."),
                S("Second sentence", text="Now both speakers know which taxi, so we use the definite article: le taxi."),
                S("Write the text", text="Il y a un taxi devant le collège. Le taxi est jaune."),
            ]),
            H("When French uses no article"),
            T("After **être** (and a few similar verbs), a profession, nationality or religion is used without an article when it comes straight after the verb: "
              "*Mon oncle est professeur.* *Elle est camerounaise.* "
              "With **c'est**, or when an adjective is added, the article returns: *C'est un professeur.* *Mon oncle est un bon professeur.* "
              "After **parler** + a language, there is usually no article (*Je parle français*), but after **aimer**, **adorer**, **détester** we use the definite article (*J'aime le français*)."),
            TIP("For countries, learn the article with the name: le Cameroun, la France, le Nigeria, les États-Unis. "
                "To say 'in' or 'to' a country, French uses en for feminine countries and au for masculine ones: *Je vais en France*, *Je vais au Cameroun*."),
            MISTAKE("Missing élision and wrong gender",
                    "Do not write *le école* or *la hôpital*. Before a vowel or silent h write l': *l'école*, *l'hôpital*. "
                    "A second trap is the plural: *des* is not *les*. Say «J'ai des amis» (some friends) but «J'aime les amis de mon frère» (those particular friends)."),
            MISTAKE("Dropping the article after 'aimer'",
                    "English says «I like music». French says «J'aime la musique». After aimer, adorer, détester and préférer, the noun takes le, la, l' or les when it speaks of things in general."),
            QUIZ("Which article completes «___ hôpital est près du marché»?", ["Le", "La", "L'", "Les"], 2,
                 "Hôpital begins with a silent h, so le becomes l': L'hôpital est près du marché.",
                 hint="Look at the first letter of the noun.",
                 feedback=["Le is the masculine article, but before a vowel or silent h it becomes l'.",
                           "Hôpital is masculine, and la also drops before a vowel.", "",
                           "Les is plural. Hôpital here is singular (est, not sont)."]),
            QUIZ("Which sentence is correct?", ["Mon père est un médecin.", "Mon père est médecin.", "Mon père est le médecin.", "Mon père est des médecin."], 1,
                 "After être a profession needs no article when it comes straight after the verb: Mon père est médecin.",
                 hint="Think of how French gives a profession after être.",
                 feedback=["Un médecin is used with c'est or with an adjective (C'est un médecin), not straight after être.",
                           "", "Le médecin would mean a particular doctor already known, which is not the idea here.",
                           "Des is plural and médecin is singular. This form does not exist."]),
            PQ("Complete with le, la, l', les, un, une or des: «Nous avons ___ nouvelle professeure. ___ professeure parle ___ anglais et ___ français.»",
               "Nous avons une nouvelle professeure. La professeure parle anglais et français. "
               "First mention: une. Known: la. After parler a language needs no article: *elle parle anglais et français*. "
               "(If the language is the subject or object of a liking, the article returns: *elle aime le français*.)"),
            PQ("Write the correct article: (a) ___ héros du film, (b) ___ homme, (c) ___ école, (d) ___ enfants.",
               "(a) le héros (aspirated h, no élision). (b) l'homme. (c) l'école. (d) les enfants."),
            PQ("Write in French: «I love music and I prefer cinema.»",
               "J'adore la musique et je préfère le cinéma. After adorer and préférer the definite article is needed."),
            SUM("French nouns normally come with an article that agrees in gender and number.",
                "Definite: le, la, l' (before a vowel or silent h), les. Use it for known things, general ideas and likes.",
                "Indefinite: un, une, des. Use it for first mention or 'one of several'.",
                "No article: profession, nationality or religion straight after être, and a language after parler.",
                "Learn each noun with its article, and check aspirated h words (le héros)."),
        ],
    ),
]


# ---------------------------------------------------------------------- 2. Partitive articles and contractions
LESSONS += [
    lesson(
        module=M1,
        topic="Articles",
        title="Partitive articles and contracted articles",
        slug="fr1-articles-partitive-contractions",
        minutes=20,
        summary="Du, de la, de l' and des name an unspecified quantity of something. After a negative or an expression of quantity they become de or d'. The prepositions à and de join with le and les to form au, aux, du and des.",
        objectives=[
            "Use du, de la, de l' and des to talk about an unspecified quantity",
            "Change the partitive to de or d' after a negative and after expressions of quantity",
            "Form au, aux, du and des from à/de + le/les",
            "Choose between à and de with common verbs such as jouer",
        ],
        key_concepts=["Article partitif", "Article contracté", "Pas de", "Beaucoup de", "À + le = au"],
        blocks=[
            H("Introduction"),
            T("A mother in Bafoussam asks her son: «Tu veux du riz ou de la banane plantain ?» She does not say how much. "
              "She means 'some rice' or 'some plantain'. For this idea French uses the **partitive article**, a small word that has no single equivalent in English."),
            T("In this lesson you will also meet the **contracted articles** au, aux, du and des. They appear every day, for example in «Je vais au marché» and «Elle revient du collège»."),
            H("The partitive article"),
            D("The **partitive article** (article partitif) is used before nouns that cannot be counted one by one (rice, water, meat, courage) "
              "when we mean 'some' or 'a part of'. The forms are **du** (masculine), **de la** (feminine), **de l'** (before a vowel or silent h) and **des** (plural).",
              title="Definition"),
            CODE("""masculin        du riz, du poisson
féminin         de la viande, de la farine
devant voyelle  de l'eau, de l'huile
pluriel         des haricots, des légumes""", "text", title="Les formes du partitif"),
            T("Compare the articles. «Je mange **le** riz» points to particular rice that both speakers know. «Je mange **du** riz» means that I am eating some rice."),
            KEY("Quand utiliser le partitif ?", "Ask: can I count it one by one?", cards=[
                ["Not countable", "Elle prépare du riz. Il boit de l'eau. J'ai de la chance."],
                ["Countable", "Use un, une or des: Il mange une mangue. Elle achète des bananes."],
                ["General taste", "J'aime le riz (the definite article, because aimer speaks about things in general)."],
            ]),
            H("De after a negative or a quantity"),
            D("After a **negative** (ne ... pas, ne ... jamais, ne ... plus), un, une, du, de la, de l' and des become **de** (or **d'** before a vowel). "
              "After an **expression of quantity** (beaucoup de, trop de, assez de, peu de, un kilo de, une bouteille de) the noun also takes de.",
              title="Rule"),
            CODE("""J'ai du pain.             -> Je n'ai pas de pain.
Il y a des taxis.         -> Il n'y a pas de taxis.
Elle boit de l'eau.       -> Elle ne boit pas d'eau.
Il achète une mangue.     -> Il n'achète pas de mangue.
beaucoup de poissons      trop de bruit
un kilo de tomates        une bouteille d'huile""", "text", title="Pas de, beaucoup de"),
            TIP("There are two exceptions. After **être** the article does not change: «Ce n'est pas du riz, c'est du maïs.» "
                "And when the sentence corrects or contrasts (not X but Y), the article stays: «Je ne bois pas du thé, mais du café.» "
                "Textbooks give slightly different lists of exceptions (à vérifier dans votre manuel / check your textbook)."),
            H("The contracted articles"),
            D("The prepositions **à** (to, at, in) and **de** (of, from) join with le and les. The result is one word: "
              "**à + le = au**, **à + les = aux**, **de + le = du**, **de + les = des**. "
              "With la and l' nothing changes: à la, à l', de la, de l'.", title="Rule"),
            CODE("""à + le   = au    Nous allons au marché.
à + les  = aux   Il parle aux élèves.
à + la   = à la  Elle est à la maison.
à + l'   = à l'  Je suis à l'école.
de + le  = du    Il revient du collège.
de + les = des   Le chef des villageois.
de + la  = de la Le toit de la maison.""", "text", title="Au, aux, du, des"),
            T("Be careful: **du** and **des** are also partitive and indefinite articles. The meaning shows the difference. "
              "«Il vient du marché» means *from the market* (de + le). «Il achète du poisson» means *some fish* (partitive). "
              "With jouer, French uses **à** for games and sports and **de** for instruments: «Il joue **au** football», «Elle joue **du** piano»."),
            EX("Worked example 1: partitive after a negative", intro="Complete: «Tu veux ___ eau ? — Non, merci, je ne bois pas ___ eau froide.»", steps=[
                S("First blank", text="Eau begins with a vowel and cannot be counted one by one. We want 'some water', so the partitive de l' is used: de l'eau."),
                S("Second blank", text="The sentence is negative (ne ... pas), so the partitive becomes d' before a vowel: d'eau."),
                S("Write the text", text="Tu veux de l'eau ? — Non, merci, je ne bois pas d'eau froide."),
            ]),
            EX("Worked example 2: contraction", intro="Complete: «Les élèves reviennent ___ collège et vont ___ marché.»", steps=[
                S("First blank", text="Revenir de means to come back from. Collège is masculine singular: de + le = du."),
                S("Second blank", text="Aller à means to go to. Marché is masculine singular: à + le = au."),
                S("Write the sentence", text="Les élèves reviennent du collège et vont au marché."),
            ]),
            MISTAKE("Writing 'à le', 'de le' and 'de les'",
                    "These forms never exist before a noun. Always write au, du, des. Compare: «Il parle à le professeur» is wrong, «Il parle au professeur» is right."),
            MISTAKE("Keeping the partitive after the negative",
                    "Write «Je n'ai pas de monnaie», not «Je n'ai pas de la monnaie». Remember: pas de, jamais de, plus de."),
            QUIZ("Which sentence is correct?", ["Il n'y a pas des taxis.", "Il n'y a pas de taxis.", "Il n'y a pas du taxis.", "Il n'y a pas les taxis."], 1,
                 "After a negative, des becomes de: Il n'y a pas de taxis.", hint="What happens to du, de la and des after ne ... pas ?",
                 feedback=["Des cannot follow ne ... pas in this sentence.", "", "Du is singular and taxis is plural.",
                           "Les would refer to particular taxis that we already know. The sentence says there are no taxis at all."]),
            QUIZ("Choose the correct form: «Je vais ___ cinéma avec mes amis.»", ["à le", "au", "du", "aux"], 1,
                 "Cinéma is masculine singular: à + le = au.", hint="Combine the preposition à with le.",
                 feedback=["À le never exists in French.", "", "Du is de + le (from the), not to the.", "Aux is for plural nouns."]),
            PQ("Complete with du, de la, de l', des, de or d': (a) Maman achète ___ huile. (b) Il y a beaucoup ___ voitures. (c) Je ne mange pas ___ poisson.",
               "(a) de l'huile (unspecified quantity, vowel start). (b) beaucoup de voitures (after an expression of quantity). (c) je ne mange pas de poisson (negative)."),
            PQ("Complete with au, aux, à la, à l', du, des: (a) Nous allons ___ hôpital. (b) Elle parle ___ voisins. (c) Il revient ___ stade.",
               "(a) à l'hôpital (hôpital has a silent h, so no contraction). (b) aux voisins (à + les). (c) du stade (de + le, since revenir de)."),
            PQ("Write in French: «My brother plays football and my sister plays the piano.»",
               "Mon frère joue au football et ma sœur joue du piano. Games and sports take jouer à (à + le = au). Instruments take jouer de (de + le = du)."),
            SUM("Partitive articles: du, de la, de l', des mean 'some'. Use them with things you do not count one by one.",
                "After a negative (ne ... pas de) and after an expression of quantity (beaucoup de, trop de) the article becomes de or d'.",
                "Contractions: à + le = au, à + les = aux, de + le = du, de + les = des. La and l' do not contract.",
                "Jouer à + a game or sport (au football), jouer de + an instrument (du piano)."),
        ],
    ),
]


# ---------------------------------------------------------------------- 3. Nouns: gender and number
LESSONS += [
    lesson(
        module=M1,
        topic="Nouns: gender and number",
        title="Gender and number of nouns",
        slug="fr1-noun-gender-number",
        minutes=22,
        summary="Every French noun is masculine or feminine, and singular or plural. Endings help to guess the gender, feminine forms of people follow common patterns, and plurals usually add -s, with important exceptions such as -al to -aux and -eau to -eaux.",
        objectives=[
            "Use common endings to guess the gender of a noun, and know the main exceptions",
            "Form the feminine of nouns that name people (-e, -ière, -euse, -trice, -enne)",
            "Form regular and irregular plurals (-s, -x, -aux, unchanged)",
            "Always learn a noun together with its article",
        ],
        key_concepts=["Genre", "Masculin", "Féminin", "Pluriel", "Terminaison", "Nom invariable"],
        blocks=[
            H("Introduction"),
            T("In a classroom in Yaoundé you may hear «Le professeur donne un livre à l'élève, et la directrice visite les salles.» "
              "In English, a table is simply *it*. In French, a table is *une table* (feminine) and a desk is *un bureau* (masculine). "
              "The gender of a noun is a fact about the word, not about the object."),
            T("Gender and number matter because the article, the adjective, the pronoun and often the verb must agree with the noun. "
              "A wrong gender at the start causes mistakes in every other word of the sentence."),
            H("Gender: masculine or feminine"),
            D("**Gender** (genre) is the class of a noun: **masculin** or **féminin**. For people the gender usually follows sex: *un frère*, *une sœur*. "
              "For things it must be learned. The best habit is to learn *un/une* or *le/la* with each new noun.", title="Definition"),
            T("There is no rule without exceptions, but the endings below are right most of the time. Use them as a guide, not as a guarantee."),
            CODE("""Souvent masculin                    Souvent féminin
-age   le village, le courage       -tion  la nation, la solution
-ment  le moment, le gouvernement   -sion  la décision
-eau   le bureau, le château        -té    la santé, la liberté
-isme  le tourisme                  -ure   la voiture, la nature
-oir   le couloir, le miroir        -ette  la baguette
Exceptions : la page, la plage, l'image, la cage, l'eau, la peau
             le lycée, le musée, l'été, le côté""", "text", title="Gender and endings"),
            TIP("Names of days, months, seasons, languages and most trees are masculine (le lundi, le français). "
                "Most nouns that end in a silent -e are feminine, but many are masculine (le livre, le service, le problème). "
                "When a textbook gives another list of tendencies, trust it (à vérifier dans votre manuel)."),
            H("Feminine of nouns that name people"),
            T("Add -e to the masculine, or change the ending. The patterns are regular enough to learn in groups."),
            CODE("""masculin          féminin
un ami            une amie
un étudiant       une étudiante
un Camerounais    une Camerounaise
un infirmier      une infirmière
un boulanger      une boulangère
un vendeur        une vendeuse
un acteur         une actrice
un instituteur    une institutrice
un lion           une lionne
un musicien       une musicienne
un voisin         une voisine""", "text", title="Masculin et féminin"),
            T("Some nouns do not change in the singular: *un élève / une élève*, *un enfant / une enfant*, *un camarade / une camarade*. The article shows the gender. "
              "Other nouns keep one gender for both sexes: *une personne*, *une victime*, *un médecin*. "
              "For job names such as *professeur*, many speakers use *la professeure*, others *le professeur* for a woman (à vérifier dans votre manuel)."),
            KEY("Same word, two meanings", "A few nouns change meaning with the gender.", cards=[
                ["le tour / la tour", "le tour = a turn, a trip; la tour = a tower"],
                ["le livre / la livre", "le livre = a book; la livre = a pound (money, weight)"],
                ["le poste / la poste", "le poste = a job, a set; la poste = the post office"],
                ["le mode / la mode", "le mode = a way, a mode; la mode = fashion"],
            ]),
            H("Number: singular or plural"),
            D("The regular plural adds **-s** to the singular. The -s is usually not pronounced: only the article and the verb make the difference you hear. "
              "*La fille* and *les filles* sound different because of la/les.", title="Rule"),
            CODE("""Règle                            Exemples
+ s (cas général)                un élève -> des élèves
-s, -x, -z : pas de changement   le pays -> les pays ; la voix -> les voix ; le nez -> les nez
-al -> -aux                      un journal -> des journaux ; un hôpital -> des hôpitaux
-au, -eau, -eu -> + x            un bateau -> des bateaux ; un cheveu -> des cheveux
-ou -> + s                       un trou -> des trous
Cas irréguliers                  un œil -> des yeux ; monsieur -> messieurs ; madame -> mesdames""", "text", title="Le pluriel des noms"),
            T("Exceptions to know: *un bal -> des bals*, *un festival -> des festivals*, *un pneu -> des pneus*, *un bleu -> des bleus*. "
              "A few nouns in -ou take -x: *un bijou -> des bijoux*, *un chou -> des choux*, *un genou -> des genoux*, *un caillou -> des cailloux*. "
              "Lists of exceptions vary slightly between textbooks (à vérifier dans votre manuel)."),
            EX("Worked example 1: the feminine", intro="Give the feminine of: un vendeur, un infirmier, un acteur.", steps=[
                S("Look at the ending", text="Vendeur ends in -eur, infirmier in -ier, acteur in -teur."),
                S("Apply the pattern", text="-eur -> -euse (vendeuse); -ier -> -ière (infirmière); -teur -> -trice (actrice)."),
                S("Write the answers", text="une vendeuse, une infirmière, une actrice."),
            ]),
            EX("Worked example 2: the plural", intro="Write in the plural: «Le journal est sur le bureau, et le bateau est au port.»", steps=[
                S("Change the articles and nouns", text="Journal ends in -al, so it becomes journaux. Bureau and bateau end in -eau, so they add x."),
                S("Change the verbs", text="Est becomes sont, because the subject is now plural."),
                S("Write the sentence", text="Les journaux sont sur les bureaux, et les bateaux sont au port."),
            ]),
            MISTAKE("Adding -s to nouns that end in -s, -x or -z",
                    "A noun that already ends in s, x or z does not change: un pays, des pays; un prix, des prix; un nez, des nez. "
                    "Do not write *des payss*."),
            MISTAKE("Guessing the gender from English or from the object",
                    "The gender of a thing is not logical. *Un stylo* (pen) is masculine, *une plume* (feather) is feminine. "
                    "Learn the noun with its article and check the exceptions (la page, l'eau, le lycée)."),
            QUIZ("What is the plural of «un hôpital» ?", ["des hôpitals", "des hôpitaux", "des hôpitales", "des hôpitauxs"], 1,
                 "Nouns ending in -al form the plural in -aux: des hôpitaux.", hint="Look at the ending -al.",
                 feedback=["Most -al nouns change to -aux, not to -als.", "", "Hôpitales does not exist.", "The plural already ends in x. Do not add another s."]),
            QUIZ("Which noun is feminine?", ["le courage", "le village", "la solution", "le moment"], 2,
                 "The ending -tion is usually feminine: la solution.", hint="Look for the ending -tion.",
                 feedback=["Courage ends in -age and is masculine.", "Village ends in -age and is masculine.", "", "Moment ends in -ment and is masculine."]),
            PQ("Write the feminine: (a) un voisin (b) un instituteur (c) un étudiant (d) un lion.",
               "(a) une voisine (b) une institutrice (-teur -> -trice) (c) une étudiante (d) une lionne (the n doubles before -e)."),
            PQ("Write in the plural: (a) un journal (b) un pays (c) un cheveu (d) un trou.",
               "(a) des journaux (b) des pays (c) des cheveux (d) des trous."),
            PQ("Give the correct article (le, la or l') for each: (a) problème (b) nation (c) plage (d) hôpital.",
               "(a) le problème (b) la nation (-tion) (c) la plage (exception: -age, but feminine) (d) l'hôpital (silent h)."),
            SUM("Every French noun has a gender. Learn it with le/la or un/une.",
                "Endings help: -age, -ment, -eau often masculine; -tion, -sion, -té, -ure often feminine. Know the exceptions.",
                "Feminine of people: add -e, or change the ending (-ier -> -ière, -eur -> -euse, -teur -> -trice, -on -> -onne).",
                "Plurals: add -s; nothing changes after -s, -x, -z; -al -> -aux; -au, -eau, -eu add x.",
                "Textbook lists of exceptions differ slightly: check yours."),
        ],
    ),
]


# ---------------------------------------------------------------------- 4. Qualifying adjectives
LESSONS += [
    lesson(
        module=M1,
        topic="Qualifying adjectives",
        title="Qualifying adjectives: agreement and position",
        slug="fr1-adjectives",
        minutes=22,
        summary="A French adjective agrees in gender and number with the noun it describes. Learn the feminine patterns (-e, -euse, -ive, -elle, -ère), the plural patterns, the irregular beau/nouveau/vieux, and which adjectives usually come before the noun.",
        objectives=[
            "Make adjectives agree in gender and number with the noun or pronoun",
            "Form the feminine of regular and common irregular adjectives",
            "Place adjectives correctly (most after the noun, a few before it)",
            "Use bel, nouvel and vieil before a masculine noun that begins with a vowel",
        ],
        key_concepts=["Adjectif qualificatif", "Accord", "Féminin des adjectifs", "Place de l'adjectif", "Adjectif de couleur"],
        blocks=[
            H("Introduction"),
            T("At the market in Douala you may hear: «Cette belle robe rouge est très chère, mais ces petites chemises blanches sont bon marché.» "
              "Every word in italics describes a noun: **belle**, **rouge**, **chère**, **petites**, **blanches**. These words are **adjectives**."),
            T("In English an adjective never changes: *a red dress*, *red dresses*. In French the adjective changes to match the noun. "
              "This is called **agreement** (l'accord)."),
            H("Agreement of the adjective"),
            D("A **qualifying adjective** (adjectif qualificatif) describes a noun or a pronoun. It agrees in **gender** and **number** with the word it describes, "
              "whether it comes next to the noun or after the verb être.", title="Definition"),
            CODE("""            masculin                   féminin
singulier   un garçon content          une fille contente
pluriel     des garçons contents       des filles contentes""", "text", title="Les quatre formes"),
            T("If the adjective describes **several nouns**, it is plural. If the nouns are of different genders, the **masculine** wins: "
              "«Mon père et ma mère sont contents.»"),
            H("The feminine of adjectives"),
            T("Most adjectives add **-e**. If the masculine already ends in -e, nothing is added: *un enfant poli, une enfant polie*; *un livre facile, une leçon facile*. "
              "Other endings follow patterns:"),
            CODE("""masculin -> féminin
petit    -> petite               (+ e ; the t is now heard)
heureux  -> heureuse             (-eux -> -euse)
actif    -> active               (-if -> -ive)
naturel  -> naturelle            (-el -> -elle)
ancien   -> ancienne             (-en -> -enne)
bon      -> bonne                (-on -> -onne)
premier  -> première             (-er -> -ère)
gentil   -> gentille             (-il -> -ille)
blanc    -> blanche   long -> longue   doux -> douce   frais -> fraîche   faux -> fausse""", "text", title="Féminin des adjectifs"),
            CODE("""masculin   masculin devant voyelle   féminin
beau       bel                       belle
nouveau    nouvel                    nouvelle
vieux      vieil                     vieille
fou        fol                       folle""", "text", title="Adjectifs à trois formes"),
            T("Examples: *un beau garçon*, **un bel** *arbre*, *une belle maison*; *un nouveau livre*, **un nouvel** *élève*, *une nouvelle école*; "
              "*un vieux taxi*, **un vieil** *homme*, *une vieille voiture*."),
            H("The plural of adjectives"),
            T("The plural follows the rules for nouns: add **-s**; no change after -s or -x (*un enfant heureux, des enfants heureux*); -al becomes -aux (*un projet national, des projets nationaux*); "
              "-eau adds x (*un beau village, de beaux villages*)."),
            H("The position of the adjective"),
            KEY("Where does the adjective go ?", "Most adjectives follow the noun. A short group of common adjectives goes before it.", cards=[
                ["After the noun (usual)", "colours, nationalities, shapes: une voiture rouge, un étudiant camerounais, une table ronde."],
                ["Before the noun", "Think BAGS: Beauty (beau, joli), Age (jeune, vieux, nouveau), Goodness (bon, mauvais), Size (grand, petit, gros, long)."],
                ["Meaning changes", "un grand homme (a great man) / un homme grand (a tall man); ma propre chambre (my own room) / ma chambre propre (my clean room)."],
            ]),
            T("Colour adjectives made from nouns do not agree: *des chemises orange*, *des sacs marron*. "
              "Compound colours also stay invariable: *des yeux bleu clair*. Simple colours do agree: *des chemises blanches*."),
            EX("Worked example 1: agreement", intro="Complete: «Les (petit) filles (camerounais) sont très (content).»", steps=[
                S("Noun and number", text="Filles is feminine plural. All three adjectives must be feminine plural."),
                S("Petit", text="Petit -> petites; a pre-noun adjective still agrees with the noun."),
                S("Camerounais", text="Camerounais ends in -s, so the feminine is camerounaise, and the feminine plural is camerounaises."),
                S("Content", text="Content -> contentes."),
                S("Write the sentence", text="Les petites filles camerounaises sont très contentes."),
            ]),
            EX("Worked example 2: position and bel", intro="Put the words in order and make them agree: (a) arbre / beau / un  (b) voiture / noir / nouveau / une.", steps=[
                S("Sort the adjectives", text="Beau and nouveau go before the noun (BAGS). Noir, a colour, goes after it."),
                S("Sentence (a)", text="Arbre is masculine and begins with a vowel, so beau becomes bel: un bel arbre."),
                S("Sentence (b)", text="Voiture is feminine: nouveau becomes nouvelle and goes before; noir becomes noire and goes after: une nouvelle voiture noire."),
            ]),
            MISTAKE("Forgetting to agree the adjective after être",
                    "The adjective agrees with the subject: «Elle est content» is wrong, «Elle est contente» is right. "
                    "Also «Les garçons sont grand» is wrong: «Les garçons sont grands»."),
            MISTAKE("Using beau before a vowel",
                    "Write un bel homme and un nouvel ami, not *un beau homme* or *un nouveau ami*. In the plural the vowel does not change the form: de beaux hommes, de nouveaux amis."),
            QUIZ("Which phrase is correct ?", ["une fille heureux", "une fille heureuse", "une fille heureuxe", "un fille heureuse"], 1,
                 "Heureux becomes heureuse in the feminine.", hint="Fille is feminine. What is the feminine of heureux ?",
                 feedback=["Heureux is masculine. The feminine is heureuse.", "", "Heureuxe does not exist.", "Fille is feminine and takes une, not un."]),
            QUIZ("Choose the correct form: «Mon frère est un ___ homme.»", ["beau", "bel", "belle", "beaux"], 1,
                 "Homme is masculine singular and begins with a vowel sound (silent h): un bel homme.", hint="Which form of beau is used before a vowel ?",
                 feedback=["Beau is used before a consonant sound (un beau garçon).", "", "Belle is feminine.", "Beaux is plural."]),
            PQ("Write the feminine: (a) un ami content (b) un élève sportif (c) un cousin ancien (d) un travail facile.",
               "(a) une amie contente (b) une élève sportive (-if -> -ive) (c) une cousine ancienne (-en -> -enne) (d) un travail facile does not change: une leçon facile."),
            PQ("Make the sentence plural: «Ce vieil arbre est très beau.»",
               "Ces vieux arbres sont très beaux. Vieil becomes vieux, beau becomes beaux, est becomes sont."),
            PQ("Choose the correct sentence: (a) Elle porte une jupe vert. (b) Elle porte une jupe verte. (c) Elle porte une verte jupe.",
               "(b) Elle porte une jupe verte. Colours come after the noun and agree: jupe is feminine, so verte."),
            SUM("Adjectives agree in gender and number with the noun or pronoun they describe, also after être.",
                "Feminine: add -e, or follow the patterns (-eux -> -euse, -if -> -ive, -el -> -elle, -en -> -enne, -er -> -ère).",
                "Beau, nouveau and vieux become bel, nouvel and vieil before a masculine vowel sound.",
                "Most adjectives come after the noun; the BAGS adjectives come before it.",
                "Colours taken from nouns (orange, marron) do not agree."),
        ],
    ),
]


# ---------------------------------------------------------------------- 5. Comparatives and superlatives
LESSONS += [
    lesson(
        module=M1,
        topic="Comparatives and superlatives",
        title="Comparatives and superlatives",
        slug="fr1-comparatives-superlatives",
        minutes=20,
        summary="Compare with plus ... que, moins ... que and aussi ... que. Form the superlative with le/la/les plus or moins. Bon, bien and mauvais have special forms: meilleur, mieux and pire.",
        objectives=[
            "Form comparatives of superiority, inferiority and equality with adjectives, adverbs and nouns",
            "Form the superlative with le, la, les plus/moins and use de after it",
            "Use the irregular forms meilleur (not plus bon) and mieux (not plus bien)",
            "Make the adjective agree in comparisons and superlatives",
        ],
        key_concepts=["Comparatif", "Superlatif", "Plus ... que", "Meilleur / mieux", "Plus de"],
        blocks=[
            H("Introduction"),
            T("Two friends talk about their results at the collège: «Amina est plus rapide que moi en calcul, mais je suis aussi bon qu'elle en anglais. "
              "Et Paul est le meilleur élève de la classe.» "
              "To compare two things, we use a **comparative**. To say that one thing is the highest or lowest of a group, we use a **superlative**."),
            H("The comparative"),
            D("The **comparative** (comparatif) compares two people or things. With an adjective or an adverb, French uses three patterns: "
              "**plus ... que** (more ... than), **moins ... que** (less ... than) and **aussi ... que** (as ... as).", title="Definition"),
            CODE("""supériorité   Paul est plus grand que Marie.
infériorité   Marie est moins grande que Paul.
égalité       Marie est aussi grande que sa sœur.
adverbe       Il court plus vite que moi.
verbe         Elle travaille plus que son frère.
nom           Il y a plus d'élèves dans ma classe que dans ta classe.
              J'ai moins de temps que toi. Il a autant de livres que moi.""", "text", title="Les trois comparatifs"),
            T("With adjectives, the adjective agrees with the first noun: *Marie est plus grande que Paul.* "
              "With **nouns**, use **plus de / moins de / autant de**: *plus de livres*, *moins d'eau*. "
              "For people, use a stress pronoun after que: *plus grand que moi*, *aussi fort que lui* (see the lesson on personal pronouns)."),
            KEY("Three irregular forms", "Do not say plus bon or plus bien.", cards=[
                ["bon -> meilleur", "Ce poisson est meilleur que l'autre. Ces mangues sont meilleures que les bananes. (meilleur agrees: meilleur, meilleure, meilleurs, meilleures)"],
                ["bien -> mieux", "Elle chante mieux que moi. Mieux is an adverb: it never changes."],
                ["mauvais -> pire", "Le résultat est pire que l'année dernière. (plus mauvais is also used; check your textbook)"],
            ]),
            TIP("Negative equality: «Il n'est pas aussi grand que son père» (or «pas si grand que»). "
                "Also, plus de before a number: «Il y a plus de cent élèves.» The 'more than' in numbers is plus de, not plus que."),
            H("The superlative"),
            D("The **superlative** (superlatif) says that something is the most or the least in a group. "
              "Add **le, la** or **les** before plus or moins: **le plus** / **la plus** / **les plus** and **le moins** / **la moins** / **les moins**. "
              "After it, the group is introduced with **de**.", title="Definition"),
            CODE("""Paul est le plus grand de la classe.
Marie est la plus rapide de l'équipe.
Ce sont les élèves les plus sérieux du collège.
Mon frère est le moins bavard de la famille.
C'est le meilleur marché de la ville.
Elle chante le mieux de tous.""", "text", title="Le superlatif"),
            T("If the adjective comes **after** the noun, the article is repeated: *la route la plus longue*, *les élèves les plus sérieux*. "
              "If the adjective goes **before** the noun, it is not repeated: *le plus grand village*, *la plus belle fête*. "
              "In French the group after a superlative is introduced by **de**: «le plus haut sommet **du** Cameroun» (the highest peak in Cameroon), not *dans le Cameroun*."),
            EX("Worked example 1: comparative", intro="Paul is 1.70 m tall and Marie is 1.65 m. Write three sentences in French.", steps=[
                S("Superiority", text="Paul est plus grand que Marie."),
                S("Inferiority", text="Marie est moins grande que Paul. (grande, because Marie is feminine)"),
                S("Equality", text="If both were 1.65 m: Marie est aussi grande que sa cousine."),
            ]),
            EX("Worked example 2: superlative", intro="Say in French: «She is the best pupil in the class» and «These are the most expensive shoes in the shop».", steps=[
                S("Best pupil", text="Bon becomes meilleur. Élève is feminine here, and meilleur goes before the noun: elle est la meilleure élève de la classe."),
                S("Most expensive shoes", text="Chaussures is feminine plural. Chers goes after the noun, so the article is repeated: ce sont les chaussures les plus chères du magasin."),
            ]),
            MISTAKE("Saying plus bon and plus bien",
                    "Write meilleur for bon and mieux for bien: «Ce riz est meilleur», «Il parle mieux». "
                    "Plus bon is only used in a few set phrases. Do not use it in an exam."),
            MISTAKE("Using 'dans' or 'en' after the superlative, and forgetting agreement",
                    "Say «le plus grand de la classe» and «la plus belle ville du pays». The article and the adjective agree with the noun: «les plus grandes villes». "
                    "Also write «plus grand que», not *plus grand que de*."),
            QUIZ("Choose the correct sentence.", ["Ce gâteau est plus bon que l'autre.", "Ce gâteau est meilleur que l'autre.", "Ce gâteau est mieux que l'autre.", "Ce gâteau est plus meilleur que l'autre."], 1,
                 "The comparative of bon is meilleur.", hint="Which special word replaces plus bon ?",
                 feedback=["Plus bon should be replaced by meilleur.", "", "Mieux is the comparative of bien (adverb), not of bon (adjective).", "Meilleur already means more good, so plus is not added."]),
            QUIZ("Choose the correct form: «Ces filles sont ___ plus intelligentes de la classe.»", ["le", "la", "les", "des"], 2,
                 "The article agrees with filles, which is feminine plural: les.", hint="The article of the superlative agrees with the noun.",
                 feedback=["Le is masculine singular.", "La is feminine singular.", "", "Des is an indefinite article and does not form a superlative."]),
            PQ("Complete with plus, moins, aussi or autant: «Il a 18 ans et son frère a 18 ans. Il est ___ âgé que son frère.»",
               "aussi. Equal ages give aussi ... que: il est aussi âgé que son frère."),
            PQ("Write in French: «Yaoundé has more schools than my village.»",
               "Yaoundé a plus d'écoles que mon village. A noun after plus takes de (d' before a vowel): plus d'écoles."),
            PQ("Write in French: «This road is the longest in the region.»",
               "Cette route est la plus longue de la région. The article agrees with route (feminine), and the group is introduced by de."),
            SUM("Comparative: plus / moins / aussi + adjective or adverb + que. With nouns: plus de / moins de / autant de.",
                "Superlative: le, la, les + plus or moins + adjective, then de. Repeat the article when the adjective follows the noun.",
                "Special forms: bon -> meilleur, bien -> mieux, mauvais -> pire (or plus mauvais).",
                "Adjectives agree with their noun; mieux does not change."),
        ],
    ),
]


# ---------------------------------------------------------------------- 6. Personal pronouns
LESSONS += [
    lesson(
        module=M1,
        topic="Personal pronouns",
        title="Personal pronouns: subject, stress, COD, COI, y and en",
        slug="fr1-personal-pronouns",
        minutes=25,
        summary="Personal pronouns replace nouns. Subject pronouns come before the verb, stress pronouns after prepositions, and object pronouns (le, la, les, lui, leur, y, en) go before the verb in a fixed order.",
        objectives=[
            "Use the subject and stress pronouns (je, tu, il ... / moi, toi, lui ...) correctly",
            "Replace a direct object (COD) with le, la, l', les and an indirect object (COI) with lui or leur",
            "Replace a place or a thing introduced by à with y, and a thing introduced by de or a quantity with en",
            "Place one or two object pronouns before the verb in the right order",
        ],
        key_concepts=["Pronom sujet", "Pronom tonique", "COD", "COI", "Y", "En", "Ordre des pronoms"],
        blocks=[
            H("Introduction"),
            T("A mother in Yaoundé asks her daughter: «Tu as acheté le pain ? — Oui, je l'ai acheté. — Tu as donné la monnaie au vendeur ? — Non, je ne la lui ai pas donnée.» "
              "Instead of repeating *le pain*, *la monnaie* and *au vendeur*, the daughter uses small pronouns. "
              "Good speakers use them all the time, and Paper 1 tests them often."),
            H("Subject and stress pronouns"),
            CODE("""Pronoms sujets            Pronoms toniques
je (j')                   moi
tu                        toi
il / elle / on            lui / elle / soi
nous                      nous
vous                      vous
ils / elles               eux / elles""", "text", title="Pronoms sujets et toniques"),
            T("**Tu** is used with a friend, a child or a relative; **vous** with several people or to be polite with one person. "
              "**On** often replaces *nous* in everyday speech (*On va au marché* = we are going to the market) and takes a third-person singular verb. "
              "**Ils** is used for a group of males, or a mixed group."),
            D("A **stress pronoun** (pronom tonique) stands alone or is used after a preposition or after c'est and que: "
              "«avec moi», «chez lui», «C'est toi ?», «plus grand que moi», «Moi, je préfère le thé.»", title="Definition"),
            H("Direct and indirect object pronouns"),
            D("A **direct object (COD)** answers « who ? what ? » directly after the verb: «Je vois **Marie**.» "
              "An **indirect object (COI)** needs the preposition à: «Je parle **à Marie**.» "
              "The direct pronouns are **me, te, le/la (l'), nous, vous, les**. The indirect pronouns are **me, te, lui, nous, vous, leur**.",
              title="Definition"),
            CODE("""COD                           COI
Je le vois. (Paul)            Je lui parle. (à Paul ou à Marie)
Je la vois. (Marie)           Je leur parle. (à mes amis)
Je les vois. (mes amis)       Il me donne le livre. (à moi)
Il m'aime. / Il t'écoute.     Elle nous écrit. / Elle vous répond.""", "text", title="Pronoms COD et COI"),
            T("The object pronoun goes **before the verb**: *Je le vois*, *Je ne le vois pas*, *Je veux le voir* (before the infinitive), *Je l'ai vu* (before the auxiliary). "
              "Common verbs followed by **à + person**: parler à, téléphoner à, répondre à, donner à, écrire à, dire à. "
              "Lui is both masculine and feminine: *Je lui parle* can mean to him or to her."),
            H("Y and en"),
            KEY("Two useful little words", "They replace a thing or a place, never a person after à.", cards=[
                ["Y", "Replaces à, dans, chez + a place or thing. «Nous allons au marché» -> «Nous y allons». «Je pense à mon examen» -> «J'y pense»."],
                ["En (of it, some)", "Replaces de + a thing, or a quantity. «Il parle de son voyage» -> «Il en parle». «J'ai trois frères» -> «J'en ai trois»."],
                ["En with du, de la, des", "«Tu manges du riz ?» -> «Oui, j'en mange.» «Elle revient du marché» -> «Elle en revient.»"],
            ]),
            TIP("With a quantity, keep the number or quantity word after the verb: «Tu as des cousins ? — J'en ai quatre.» «Elle mange du pain ? — Elle en mange beaucoup.» "
                "For a person after à, use lui or leur; for a person after penser à, use a stress pronoun: «Je pense à toi.» "
                "Some textbooks also allow y for a person with certain verbs; check your textbook (à vérifier dans votre manuel)."),
            H("The order of two pronouns"),
            CODE("""me         le
te    ->   la    ->  lui   ->  y  ->  en
nous       les       leur
vous
Je le lui donne.        (le livre à Paul)
Il me les donne.        (les clés)
Il y en a trois.        (y avant en)
Elle m'en parle.""", "text", title="Ordre devant le verbe"),
            T("Short rule: **me, te, nous, vous** come first; then **le, la, les**; then **lui, leur**; then **y**; and **en** is last. "
              "With le, la, les and lui or leur, the order is always le/la/les + lui/leur: *Je le lui donne*, *Je les leur montre*."),
            EX("Worked example 1: replace the underlined word", intro="Replace the nouns with pronouns: (a) Je mange le riz. (b) Elle parle à sa mère. (c) Nous allons au marché. (d) J'ai trois frères.", steps=[
                S("(a) COD", text="Le riz is a direct object (no preposition). Riz is masculine: Je le mange."),
                S("(b) COI", text="À sa mère is an indirect object (person after à): Elle lui parle."),
                S("(c) Place", text="Au marché is a place introduced by à: Nous y allons."),
                S("(d) Quantity", text="Trois frères is a quantity. Replace frères by en and keep the number: J'en ai trois."),
            ]),
            EX("Worked example 2: two pronouns", intro="Replace the nouns: «Il donne le livre à Paul.»", steps=[
                S("Identify the objects", text="Le livre is the COD. À Paul is the COI."),
                S("Choose the pronouns", text="Le livre -> le. À Paul -> lui."),
                S("Apply the order", text="le comes before lui: Il le lui donne."),
            ]),
            MISTAKE("Putting the pronoun after the verb or using lui for things",
                    "Do not write *Je vois le* or *Je parle lui*. The pronoun goes before the verb: Je le vois, Je lui parle. "
                    "Also, lui and leur replace persons only. For a thing introduced by à, use y: «Je réponds à la lettre» -> «J'y réponds.»"),
            MISTAKE("Forgetting en with a quantity",
                    "«Tu as des frères ? — Oui, j'ai deux.» is incomplete. Say «Oui, j'en ai deux.» En stands for the noun, and the number stays."),
            QUIZ("Replace the words: «Je vois Marie.»", ["Je lui vois.", "Je la vois.", "Je le vois.", "Je vois la."], 1,
                 "Marie is a feminine direct object: la.", hint="Is there a preposition between the verb and Marie ?",
                 feedback=["Lui replaces à + person. Here voir takes a direct object.", "", "Le is masculine, but Marie is feminine.", "The pronoun goes before the verb."]),
            QUIZ("Replace the words: «Nous allons au marché.»", ["Nous le allons.", "Nous y allons.", "Nous en allons.", "Nous lui allons."], 1,
                 "Au marché is a place introduced by à, so we use y.", hint="Which pronoun replaces a place after à ?",
                 feedback=["Le replaces a direct object, but au marché is a place.", "", "En replaces de + thing or a quantity.", "Lui replaces a person after à."]),
            PQ("Replace the underlined words with a pronoun: (a) Elle écoute la radio. (b) Tu téléphones à tes amis. (c) Il parle de son voyage.",
               "(a) Elle l'écoute. (la radio, COD, feminine; la becomes l' before a vowel). (b) Tu leur téléphones. (à + persons, plural). (c) Il en parle. (de + thing)."),
            PQ("Answer with a pronoun: «Tu as des cousins à Douala ? — Oui, ...» (four cousins).",
               "Oui, j'en ai quatre. En replaces des cousins; the number quatre stays."),
            PQ("Rewrite with two pronouns: «Elle montre les photos à ses parents.»",
               "Elle les leur montre. The order is le/la/les + lui/leur."),
            SUM("Subject pronouns come before the verb; stress pronouns come after prepositions and c'est.",
                "COD: me, te, le, la, l', nous, vous, les. COI: me, te, lui, nous, vous, leur.",
                "Y replaces à + a place or a thing; en replaces de + a thing and quantities.",
                "Object pronouns go before the verb (or the auxiliary, or the infinitive).",
                "Order: me/te/nous/vous, then le/la/les, then lui/leur, then y, then en."),
        ],
    ),
]


# ---------------------------------------------------------------------- 7. Relative pronouns
LESSONS += [
    lesson(
        module=M1,
        topic="Relative, possessive and demonstrative pronouns",
        title="Relative pronouns: qui, que, dont, où, lequel",
        slug="fr1-relative-pronouns",
        minutes=22,
        summary="A relative pronoun joins two sentences. Qui is the subject, que is the direct object, dont replaces de + noun, où gives a place or a time, and lequel follows a preposition for things. Ce qui, ce que and ce dont are used when there is no noun before them.",
        objectives=[
            "Choose between qui and que by looking at the role of the pronoun in the relative clause",
            "Use dont for de + noun and où for place and time",
            "Use preposition + lequel/laquelle/lesquels/lesquelles for things",
            "Use ce qui, ce que and ce dont when there is no antecedent",
        ],
        key_concepts=["Pronom relatif", "Antécédent", "Qui", "Que", "Dont", "Où", "Lequel", "Ce qui / ce que"],
        blocks=[
            H("Introduction"),
            T("At school a teacher says: «Voici l'élève qui a gagné le concours. C'est le livre que tu cherches. Voici la ville où je suis né.» "
              "Each sentence joins two ideas with a small word: **qui**, **que**, **où**. These words are **relative pronouns**."),
            D("A **relative pronoun** (pronom relatif) replaces a noun already mentioned (the **antecedent**) and introduces a **relative clause**, "
              "which gives more information about that noun. «L'élève **qui** parle» = «L'élève» + «Il parle».", title="Definition"),
            H("Qui and que"),
            KEY("Qui or que ?", "Ask: what is the pronoun doing in the relative clause ?", cards=[
                ["qui = subject", "A verb follows qui. «Le garçon qui joue est mon frère.» (Le garçon joue.) Qui never loses its i."],
                ["que = direct object", "A subject follows que. «Le livre que je lis est intéressant.» (Je lis le livre.) Que becomes qu' before a vowel."],
                ["qui, after a preposition", "For persons only: «la fille avec qui je travaille». For things use a form of lequel."],
            ]),
            TIP("Quick test: if the next word is a **verb**, use **qui**. If it is a **subject** (je, il, Marie, mon père), use **que**. "
                "Remember also that the past participle agrees with the antecedent after que when the auxiliary is avoir (see the lesson on participle agreement)."),
            H("Dont and où"),
            T("**Dont** replaces **de + noun**. It is used with verbs and expressions followed by de: parler de, avoir besoin de, avoir peur de, se souvenir de. "
              "«Voici le professeur dont je t'ai parlé.» (Je t'ai parlé *de ce professeur*.) "
              "«C'est le livre dont j'ai besoin.» "
              "**Où** gives a place or a time: «La ville où j'habite est grande.» «Le jour où nous sommes arrivés, il pleuvait.» Do not use *que* for the time or place here."),
            CODE("""qui    L'homme qui vend les mangues est gentil.
que    Les fruits qu'elle vend sont frais.
dont   Le film dont tu parles est drôle.
où     L'école où j'étudie est près du marché.""", "text", title="Les quatre pronoms de base"),
            H("Preposition + lequel"),
            T("After a preposition (avec, dans, pour, sans, sur, chez ...), a thing is replaced by a form of **lequel**, which agrees with the antecedent: "
              "**lequel, laquelle, lesquels, lesquelles**. «La clé avec **laquelle** j'ouvre la porte est perdue.» "
              "«Les raisons pour **lesquelles** il est parti sont claires.» "
              "With à, the forms contract: auquel, à laquelle, auxquels, auxquelles. With de, use dont for simple cases."),
            H("Ce qui, ce que, ce dont"),
            T("When there is **no noun before** the relative pronoun, French uses **ce** + pronoun: "
              "**ce qui** (subject), **ce que** (object), **ce dont** (de). "
              "«Dis-moi ce qui se passe.» «Je ne comprends pas ce que tu dis.» «Voilà ce dont j'ai besoin.»"),
            EX("Worked example 1: joining two sentences", intro="Join: «J'ai un ami. Il habite à Bafoussam.» and «Voici le livre. Je lis ce livre.»", steps=[
                S("First pair: find the role", text="In the second sentence, il is the subject of habite. The relative pronoun replaces the subject: qui."),
                S("Write the first sentence", text="J'ai un ami qui habite à Bafoussam."),
                S("Second pair: find the role", text="Je lis ce livre. Ce livre is the direct object, so the pronoun is que."),
                S("Write the second sentence", text="Voici le livre que je lis."),
            ]),
            EX("Worked example 2: dont and où", intro="Join: «Voici le film. Nous avons parlé de ce film.» and «C'est le village. Je suis né dans ce village.»", steps=[
                S("First pair", text="Parler de + film: the pronoun replaces de ce film, so dont."),
                S("Write it", text="Voici le film dont nous avons parlé."),
                S("Second pair", text="Dans ce village is a place: où."),
                S("Write it", text="C'est le village où je suis né."),
            ]),
            MISTAKE("Using que for a subject (or qui for an object)",
                    "«L'homme que parle» is wrong: parle needs a subject, so use qui. «Le livre qui je lis» is wrong: je is the subject, so use que."),
            MISTAKE("Using que for time and place",
                    "Say «le jour où» and «la ville où». A common error is *le jour que nous sommes arrivés*. "
                    "Also do not leave out the pronoun: *Voici le professeur je t'ai parlé* is wrong; write dont."),
            QUIZ("Complete: «Les élèves ___ habitent près du collège arrivent tôt.»", ["que", "qui", "dont", "où"], 1,
                 "A verb (habitent) follows the blank, so the pronoun is the subject: qui.", hint="What comes right after the blank: a verb or a subject ?",
                 feedback=["Que is followed by a subject, not by a verb.", "", "Dont replaces de + noun.", "Où gives a place or a time. The pronoun here is the subject of habitent."]),
            QUIZ("Complete: «Le crayon avec ___ j'écris est cassé.»", ["lequel", "laquelle", "qui", "dont"], 0,
                 "Crayon is masculine singular, and the pronoun follows a preposition for a thing: avec lequel.", hint="Is crayon a person or a thing ? Masculine or feminine ?",
                 feedback=["", "Laquelle is feminine, but crayon is masculine.", "Qui after a preposition is used for persons only.", "Dont replaces de + noun, but here the preposition is avec."]),
            PQ("Complete with qui, que, dont or où: (a) La fille ___ chante est ma cousine. (b) Le sac ___ j'ai acheté est cher. (c) Le village ___ nous habitons est calme.",
               "(a) qui (subject of chante). (b) que (j' = subject, sac is the object). (c) où (a place)."),
            PQ("Join: «C'est le professeur. J'ai besoin de ce professeur.»",
               "C'est le professeur dont j'ai besoin. Avoir besoin de takes de, which dont replaces."),
            PQ("Complete: «Je ne sais pas ___ elle veut.» and «Dis-moi ___ se passe.»",
               "«Je ne sais pas ce qu'elle veut» (ce que, shortened to ce qu' before the vowel). «Dis-moi ce qui se passe» (ce qui, because it is the subject of se passe)."),
            SUM("Qui = subject (a verb follows). Que = direct object (a subject follows; qu' before a vowel).",
                "Dont replaces de + noun. Où replaces a place or a time.",
                "After a preposition, a thing is replaced by lequel, laquelle, lesquels or lesquelles; a person by qui.",
                "With no noun before it, use ce qui, ce que or ce dont."),
        ],
    ),
]


# ---------------------------------------------------------------------- 8. Possessives and demonstratives
LESSONS += [
    lesson(
        module=M1,
        topic="Relative, possessive and demonstrative pronouns",
        title="Possessive and demonstrative words and pronouns",
        slug="fr1-possessives-demonstratives",
        minutes=22,
        summary="Possessive adjectives (mon, ma, mes ...) agree with the thing owned, not with the owner. Possessive pronouns are le mien, la tienne and so on. Demonstratives are ce, cet, cette, ces and celui, celle, ceux, celles.",
        objectives=[
            "Choose the possessive adjective that agrees with the noun owned (mon/ma/mes, son/sa/ses ...)",
            "Use mon, ton, son before a feminine noun that begins with a vowel",
            "Form and use possessive pronouns (le mien, la tienne, les nôtres ...)",
            "Use ce, cet, cette, ces and celui, celle, ceux, celles with -ci, -là, de and relative pronouns",
        ],
        key_concepts=["Adjectif possessif", "Pronom possessif", "Adjectif démonstratif", "Pronom démonstratif", "Celui / celle"],
        blocks=[
            H("Introduction"),
            T("In a taxi in Douala: «Ce sac est à toi ? — Non, c'est celui de ma sœur. Le mien est dans la voiture.» "
              "To show who owns a thing we use **possessive** words. To point to a thing we use **demonstrative** words. "
              "In French both kinds agree with the noun, so you need to know its gender and number."),
            H("Possessive adjectives"),
            D("A **possessive adjective** (adjectif possessif) shows who owns a noun. It agrees in gender and number with the noun that is owned, **not** with the owner.", title="Definition"),
            CODE("""             masc. sing.   fém. sing.   pluriel
je           mon           ma           mes
tu           ton           ta           tes
il / elle    son           sa           ses
nous         notre         notre        nos
vous         votre         votre        vos
ils / elles  leur          leur         leurs""", "text", title="Adjectifs possessifs"),
            T("Son, sa and ses mean *his*, *her* or *its*. The form depends on the noun that is owned: "
              "«Paul aime **sa** sœur» and «Marie aime **sa** sœur» both use sa because sœur is feminine. The context shows whether it is his or her sister."),
            TIP("Before a feminine noun that begins with a vowel or a silent h, use **mon, ton, son**, not ma, ta, sa: "
                "*mon amie*, *ton école*, *son histoire*. This avoids two vowel sounds meeting."),
            H("Possessive pronouns"),
            D("A **possessive pronoun** (pronom possessif) replaces a possessive adjective + noun: «mon sac» -> «le mien». "
              "It is preceded by le, la, les and agrees with the noun that is replaced.", title="Definition"),
            CODE("""            masc. sing.  fém. sing.   masc. pl.  fém. pl.
à moi       le mien      la mienne    les miens   les miennes
à toi       le tien      la tienne    les tiens   les tiennes
à lui/elle  le sien      la sienne    les siens   les siennes
à nous      le nôtre     la nôtre     les nôtres  les nôtres
à vous      le vôtre     la vôtre     les vôtres  les vôtres
à eux/elles le leur      la leur      les leurs   les leurs""", "text", title="Pronoms possessifs"),
            T("Examples: «Mon cahier est ici. **Le tien** est là-bas.» «Ma mère travaille à Douala, **la sienne** à Garoua.» "
              "After à and de, the article contracts: «Je pense **aux miens**» (to my family), «Il parle **des siens**»."),
            H("Demonstrative adjectives"),
            CODE("""            masculin    féminin     pluriel
singulier   ce garçon    cette fille
            cet élève   cette élève
pluriel                             ces garçons, ces filles""", "text", title="Ce, cet, cette, ces"),
            T("**Cet** is used before a masculine singular noun that begins with a vowel or a silent h: *cet élève*, *cet hôpital*. "
              "To distinguish between near and far, add **-ci** or **-là** after the noun: *ce livre-ci* (this book), *ce livre-là* (that book)."),
            H("Demonstrative pronouns"),
            T("The demonstrative pronoun replaces a demonstrative adjective + noun. The forms are **celui** (masc. sing.), **celle** (fem. sing.), **ceux** (masc. pl.) and **celles** (fem. pl.). "
              "They are never used alone: they are followed by **-ci / -là**, by **de + noun** or by a relative pronoun (**qui, que, dont**)."),
            CODE("""Quel livre ? Celui-ci ou celui-là ?
Mon sac est lourd. Celui de ma sœur est léger.
Quelle robe ? Celle que tu portes aujourd'hui ?
Ces élèves sont sérieux, mais ceux qui arrivent en retard le sont moins.
Ceci est nouveau. Cela / Ça ne me regarde pas.""", "text", title="Celui, celle, ceux, celles"),
            T("**Ceci, cela** and the everyday **ça** are neutral: they mean *this* or *that* when no gender is involved (an idea or a situation). "
              "**C'est** and **ce sont** are used before a noun or pronoun: *C'est mon frère*, *Ce sont mes amis*."),
            EX("Worked example 1: possessive adjectives", intro="Complete (everything belongs to Marie): «Marie et ___ amie vont chez ___ oncle avec ___ parents.»", steps=[
                S("First blank", text="Amie is feminine but begins with a vowel, so we use son: son amie."),
                S("Second blank", text="Oncle is masculine singular: son oncle."),
                S("Third blank", text="Parents is plural: ses parents."),
                S("Write the sentence", text="Marie et son amie vont chez son oncle avec ses parents."),
            ]),
            EX("Worked example 2: possessive and demonstrative pronouns", intro="Replace the nouns: (a) «Ton cahier est ouvert, mon cahier est fermé.» (b) «Ce livre est intéressant, mais le livre de Paul est ennuyeux.»", steps=[
                S("(a) possessive pronoun", text="Mon cahier is masculine singular: le mien. So: Ton cahier est ouvert, le mien est fermé."),
                S("(b) demonstrative pronoun", text="Le livre de Paul is masculine singular with de: celui de Paul. So: Ce livre est intéressant, mais celui de Paul est ennuyeux."),
            ]),
            MISTAKE("Agreeing the possessive with the owner",
                    "In English *his* and *her* depend on the owner. In French they depend on the noun owned. "
                    "«Paul et sa mère» and «Marie et sa mère» both use sa, because mère is feminine. Do not write *Paul aime son sœur*."),
            MISTAKE("Using ma/ta/sa before a vowel, and ce before a vowel",
                    "Write mon amie, not *ma amie*, and cet ami, not *ce ami*. Also remember the circumflex on nôtre and vôtre (le nôtre, le vôtre), but not on the adjectives notre and votre."),
            QUIZ("Complete: «Paul aime ___ sœur.»", ["son", "sa", "ses", "leur"], 1,
                 "Sœur is feminine singular, so the possessive is sa. It agrees with the noun owned, not with Paul.", hint="Which word shows the gender: Paul or sœur ?",
                 feedback=["Son is masculine, but sœur is feminine.", "", "Ses is plural, but sœur is singular.", "Leur would mean that several people own her."]),
            QUIZ("Complete: «___ élève est très sérieux.»", ["Ce", "Cet", "Cette", "Ces"], 1,
                 "Élève is masculine singular and begins with a vowel: cet élève.", hint="Which form is used before a vowel for a masculine noun ?",
                 feedback=["Ce is used before a consonant.", "", "Cette is feminine.", "Ces is plural."]),
            PQ("Complete with the French for 'my': (a) ___ école (b) ___ amie (c) ___ parents (d) ___ voiture.",
               "(a) mon école (feminine noun that begins with a vowel). (b) mon amie (same reason). (c) mes parents (plural). (d) ma voiture (feminine, begins with a consonant)."),
            PQ("Replace the nouns by a pronoun: «Mes notes sont meilleures que les notes de Paul.»",
               "Mes notes sont meilleures que celles de Paul. Notes is feminine plural, so celles + de."),
            PQ("Write in French: «Their house is bigger than ours.»",
               "Leur maison est plus grande que la nôtre. Maison is feminine, and ours (la nôtre) keeps the circumflex."),
            SUM("Possessive adjectives agree with the noun owned: mon/ma/mes, ton/ta/tes, son/sa/ses, notre/nos, votre/vos, leur/leurs.",
                "Use mon, ton, son before a feminine noun that begins with a vowel (mon amie).",
                "Possessive pronouns: le mien, la tienne, les siens, le nôtre, la vôtre, les leurs (with a circumflex on nôtre and vôtre).",
                "Demonstrative adjectives: ce, cet (before a vowel), cette, ces. Add -ci or -là to distinguish.",
                "Demonstrative pronouns: celui, celle, ceux, celles, followed by -ci/-là, de + noun or qui/que/dont."),
        ],
    ),
]


# ---------------------------------------------------------------------- 9. Present tense: regular verbs
LESSONS += [
    lesson(
        module=M2,
        topic="Present tense",
        title="The present tense of regular verbs",
        slug="fr1-present-regular",
        minutes=22,
        summary="Regular verbs follow three patterns in the présent: -er (parler), -ir (finir) and -re (vendre). Learn the endings, the spelling changes (mangeons, commençons, appelle, achète) and the main uses of the present, including depuis, aller + infinitive and venir de + infinitive.",
        objectives=[
            "Conjugate regular -er, -ir (finir type) and -re verbs in the présent",
            "Apply the spelling changes of manger, commencer, appeler, acheter and préférer",
            "Use the present for actions now, habits, general truths and with depuis",
            "Form the near future (aller + infinitive) and the recent past (venir de + infinitive)",
        ],
        key_concepts=["Présent", "Radical", "Terminaison", "Verbe en -er", "Verbe en -ir", "Verbe en -re", "Futur proche"],
        blocks=[
            H("Introduction"),
            T("Every morning a trader in Bamenda says: «Je vends des légumes, ma fille choisit les plus beaux et nous finissons avant midi.» "
              "The verbs are in the **présent**. To conjugate a verb, we take the **stem** (le radical, the infinitive without its ending) and add the **ending** (la terminaison) that matches the subject."),
            H("The three regular patterns"),
            D("French verbs are grouped by their infinitive ending. The regular groups are **-er** (parler, the largest group), **-ir** with -iss- (finir) and **-re** (vendre).", title="Definition"),
            CODE("""            parler        finir          vendre
je          parle         finis          vends
tu          parles        finis          vends
il / elle   parle         finit          vend
nous        parlons       finissons      vendons
vous        parlez        finissez       vendez
ils / elles parlent       finissent      vendent""", "text", title="Le présent : trois modèles"),
            T("Notice the endings. For -er verbs: **-e, -es, -e, -ons, -ez, -ent**. For -ir verbs: **-is, -is, -it, -issons, -issez, -issent**. For -re verbs: **-s, -s, (nothing), -ons, -ez, -ent**. "
              "With **je**, a verb starting with a vowel or silent h takes **j'**: *j'aime*, *j'habite*. "
              "Other regular verbs: -er: aimer, chanter, étudier, travailler, habiter; -ir: choisir, réussir, grandir, obéir; -re: attendre, répondre, perdre, entendre, descendre."),
            TIP("In speech, parle, parles and parlent sound the same. The silent endings -e, -es and -ent still matter in writing, so check the subject carefully: «Les élèves parlent» (ent) but «L'élève parle» (e)."),
            H("Spelling changes in -er verbs"),
            CODE("""manger      je mange        nous mangeons     (e after g before -ons)
commencer   je commence     nous commençons   (ç before -ons)
appeler     j'appelle       nous appelons     ils appellent
acheter     j'achète        nous achetons     ils achètent
préférer    je préfère      nous préférons    ils préfèrent""", "text", title="Particularités"),
            T("The change in **manger** and **commencer** keeps the soft sound of g and c before the ending -ons. "
              "In **appeler** the l doubles, and in **acheter** and **préférer** an accent appears, whenever the ending is silent (je, tu, il, ils). "
              "In the nous and vous forms the stem stays unchanged. A few verbs (payer: je paie or je paye) have two accepted spellings; check your textbook (à vérifier dans votre manuel)."),
            H("The uses of the present"),
            KEY("What the present can express", "One tense, several meanings.", cards=[
                ["Now", "En ce moment, je lis un livre. (Also: je suis en train de lire.)"],
                ["Habit and general truth", "Le samedi, nous allons au marché. L'eau bout à 100 degrés."],
                ["Since: depuis", "J'habite à Douala depuis trois ans. (I have lived ... and I still do.)"],
                ["Near future and recent past", "Je vais partir. (aller + infinitive) Il vient d'arriver. (venir de + infinitive)"],
            ]),
            EX("Worked example 1: conjugating", intro="Conjugate the verbs in the present: (a) nous (manger) du riz. (b) elles (finir) leur travail. (c) tu (répondre) au professeur.", steps=[
                S("(a) manger, nous", text="Stem mang-. Before -ons keep the e: mangeons. Nous mangeons du riz."),
                S("(b) finir, elles", text="-ir model: -issent. Elles finissent leur travail."),
                S("(c) répondre, tu", text="-re model with tu: -s. Tu réponds au professeur."),
            ]),
            EX("Worked example 2: aller + infinitive and venir de", intro="Say in French: «We are going to buy bread» and «She has just arrived».", steps=[
                S("Near future", text="Aller in the present (nous allons) + infinitive (acheter): Nous allons acheter du pain."),
                S("Recent past", text="Venir in the present (elle vient) + de + infinitive (arriver): Elle vient d'arriver."),
            ]),
            MISTAKE("Using the passé composé with depuis",
                    "English says «I have lived here for three years». French uses the present: «J'habite ici depuis trois ans». "
                    "Writing *J'ai habité ici depuis trois ans* is a common mistake."),
            MISTAKE("Forgetting the stem change or the endings of -ir verbs",
                    "Write nous mangeons (not *mangons*) and nous commençons (with the cedilla, not *commencons*). "
                    "For finir, remember -iss- in the plural: nous finissons, ils finissent, not *nous finons*."),
            QUIZ("Which form is correct ?  «Nous ___ (manger) au restaurant.»", ["mangons", "mangeons", "mangeont", "mangez"], 1,
                 "Before -ons a g keeps its soft sound with an e: mangeons.", hint="What letter keeps the sound of g before o ?",
                 feedback=["Without the e, the g would sound hard.", "", "Mangeont does not exist.", "Mangez is the vous form."]),
            QUIZ("Which sentence is correct ?", ["Ils finit leurs devoirs.", "Ils finissent leurs devoirs.", "Ils finient leurs devoirs.", "Ils finisent leurs devoirs."], 1,
                 "Finir takes -iss- in the plural: ils finissent.", hint="Remember the -iss- of the plural.",
                 feedback=["Finit is the singular (il finit).", "", "Finient does not exist: finir is not an -er verb.", "Finisent has one s too few. It is finissent."]),
            PQ("Conjugate in the present: (a) je (choisir) (b) vous (vendre) (c) ils (parler) (d) nous (commencer).",
               "(a) je choisis. (b) vous vendez. (c) ils parlent. (d) nous commençons (cedilla before o)."),
            PQ("Write in French: «We have lived in Yaoundé for five years.»",
               "Nous habitons à Yaoundé depuis cinq ans. The present is used with depuis for an action that continues."),
            PQ("Rewrite with aller + infinitive: «Je finis mes devoirs.»",
               "Je vais finir mes devoirs. Aller in the present + the infinitive."),
            SUM("-er verbs: -e, -es, -e, -ons, -ez, -ent. -ir (finir): -is, -is, -it, -issons, -issez, -issent. -re: -s, -s, (nothing), -ons, -ez, -ent.",
                "Spelling: nous mangeons, nous commençons, j'appelle, j'achète, je préfère.",
                "The present expresses now, habits, truths, and an action that continues with depuis.",
                "Near future: aller + infinitive. Recent past: venir de + infinitive."),
        ],
    ),
]


# ---------------------------------------------------------------------- 10. Present tense: irregular verbs
LESSONS += [
    lesson(
        module=M2,
        topic="Present tense",
        title="The present tense of irregular verbs",
        slug="fr1-present-irregular",
        minutes=24,
        summary="The most useful French verbs are irregular: être, avoir, aller, faire, dire, venir, pouvoir, vouloir, savoir, prendre, voir, devoir and others. Learn them in families, and watch the nous, vous and ils forms, which often change the stem.",
        objectives=[
            "Conjugate être, avoir, aller and faire in the présent from memory",
            "Conjugate venir, prendre, pouvoir, vouloir, devoir, savoir, voir, dire and boire",
            "Recognise families of verbs (prendre, venir, partir, mettre, connaître) and conjugate their relatives",
            "Use these verbs correctly in short sentences",
        ],
        key_concepts=["Verbe irrégulier", "Être", "Avoir", "Aller", "Faire", "Famille de verbes"],
        blocks=[
            H("Introduction"),
            T("Each day at the collège you say or hear: «Je suis en retard. Tu as ton cahier ? Nous allons au laboratoire. Vous faites un exposé. Ils veulent sortir.» "
              "Those verbs (être, avoir, aller, faire, vouloir) are **irregular**: their forms do not follow the three regular patterns. "
              "They are also the verbs used most often, so you must know them by heart."),
            H("The four essential verbs"),
            CODE("""            être      avoir     aller     faire
je          suis      ai        vais      fais
tu          es        as        vas       fais
il / elle   est       a         va        fait
nous        sommes    avons     allons    faisons
vous        êtes      avez      allez     faites
ils / elles sont      ont       vont      font""", "text", title="Être, avoir, aller, faire"),
            T("Notice: **vous êtes**, **vous faites** (and **vous dites**) are the only vous forms that do not end in -ez. "
              "Aller is the only -er verb with an irregular present: je vais, tu vas, il va, ils vont."),
            H("Verbs with a stem change"),
            CODE("""            venir      pouvoir     vouloir     savoir
je          viens      peux        veux        sais
tu          viens      peux        veux        sais
il / elle   vient      peut        veut        sait
nous        venons     pouvons     voulons     savons
vous        venez      pouvez      voulez      savez
ils / elles viennent   peuvent     veulent     savent""", "text", title="Venir, pouvoir, vouloir, savoir"),
            CODE("""            prendre     voir        devoir      dire        boire
je          prends      vois        dois        dis         bois
tu          prends      vois        dois        dis         bois
il / elle   prend       voit        doit        dit         boit
nous        prenons     voyons      devons      disons      buvons
vous        prenez      voyez       devez       dites       buvez
ils / elles prennent    voient      doivent     disent      boivent""", "text", title="Prendre, voir, devoir, dire, boire"),
            H("Families of verbs"),
            KEY("Learn one, get several", "Verbs built on the same base are conjugated alike.", cards=[
                ["prendre", "apprendre, comprendre, surprendre: j'apprends, nous comprenons, ils comprennent"],
                ["venir", "devenir, revenir, tenir (je tiens), obtenir: il devient, elles reviennent"],
                ["mettre", "permettre, promettre, remettre: je mets, nous permettons"],
                ["partir / sortir / dormir", "je pars, je sors, je dors (the final consonant of the stem is dropped in the singular): nous partons, ils sortent"],
                ["connaître", "reconnaître, paraître: je connais, il connaît (with an accent), nous connaissons"],
            ]),
            T("More irregular verbs you need: **lire** (je lis, nous lisons), **écrire** (j'écris, nous écrivons), **ouvrir** (j'ouvre, like an -er verb), "
              "**croire** (je crois, nous croyons, ils croient), **vivre** (je vis, nous vivons), **mettre**, **recevoir** (je reçois, nous recevons, ils reçoivent), **courir** (je cours, nous courons)."),
            EX("Worked example 1: conjugating", intro="Complete: (a) Vous (faire) un exposé. (b) Les élèves (prendre) le bus. (c) Nous (vouloir) sortir.", steps=[
                S("(a) faire, vous", text="Faire has an irregular vous form: vous faites."),
                S("(b) prendre, ils", text="The ils form doubles the n: ils prennent. Les élèves prennent le bus."),
                S("(c) vouloir, nous", text="The nous form keeps the stem voul-: nous voulons."),
            ]),
            EX("Worked example 2: choosing the verb", intro="Complete with the right verb in the present: «Mon père ___ (venir) du marché. Il ___ (avoir) deux sacs, mais il ne ___ (pouvoir) pas les porter seul.»", steps=[
                S("Venir, il", text="Il vient du marché."),
                S("Avoir, il", text="Il a deux sacs."),
                S("Pouvoir, il, negative", text="Il ne peut pas les porter seul."),
                S("Write it", text="Mon père vient du marché. Il a deux sacs, mais il ne peut pas les porter seul."),
            ]),
            MISTAKE("Regularising irregular verbs",
                    "Avoid *vous disez*, *vous faisez*, *ils vonts* and *il peux*. Write vous dites, vous faites, ils vont and il peut. "
                    "A good habit: learn each verb as a row of six forms, not as a stem and an ending."),
            MISTAKE("Mixing je veux with il veut, and je peux with il peut",
                    "Vouloir and pouvoir end in -x in the first and second person (je veux, tu veux, je peux, tu peux) but in -t in the third (il veut, il peut). "
                    "Savoir does not: je sais, tu sais, il sait."),
            QUIZ("Vous ___ (faire) du sport.", ["faisez", "faites", "faisent", "faisons"], 1,
                 "Faire has an irregular vous form: faites.", hint="Which three vous forms do not end in -ez ?",
                 feedback=["Faisez does not exist.", "", "Faisent does not exist (the ils form is font).", "Faisons is the nous form."]),
            QUIZ("Ils ___ (prendre) le taxi.", ["prend", "prenent", "prennent", "prendent"], 2,
                 "The ils form of prendre doubles the n: ils prennent.", hint="Compare nous prenons and ils ___.",
                 feedback=["Prend is the singular.", "The n must double.", "", "Prendent does not exist; the d disappears and the n doubles."]),
            PQ("Conjugate in the present: (a) je (aller) (b) elles (être) (c) tu (pouvoir) (d) nous (dire).",
               "(a) je vais (b) elles sont (c) tu peux (d) nous disons."),
            PQ("Complete: «Mes parents ___ (venir) me voir et ils ___ (apprendre) que je ___ (savoir) conduire.»",
               "viennent (ils, venir), apprennent (ils, apprendre follows prendre), sais (je, savoir): Mes parents viennent me voir et ils apprennent que je sais conduire."),
            PQ("Write in French: «We are going to the market, but my sister wants to stay at home.»",
               "Nous allons au marché, mais ma sœur veut rester à la maison. (nous allons; elle veut)"),
            SUM("Être, avoir, aller, faire: learn all six forms: suis/es/est/sommes/êtes/sont; ai/as/a/avons/avez/ont; vais/vas/va/allons/allez/vont; fais/fais/fait/faisons/faites/font.",
                "Pouvoir, vouloir, savoir, venir, prendre, voir, devoir, dire, boire change their stem in the nous or ils forms.",
                "Verbs of the same family are conjugated alike (prendre / comprendre; venir / revenir).",
                "Learn each irregular verb as a row of six forms."),
        ],
    ),
]


# ---------------------------------------------------------------------- 11. Imperative
LESSONS += [
    lesson(
        module=M2,
        topic="Imperative",
        title="The imperative: orders, advice and requests",
        slug="fr1-imperative",
        minutes=20,
        summary="The imperative gives an order, advice or an invitation, with only three forms (tu, nous, vous) and no subject pronoun. Watch the missing -s of -er verbs, the irregular verbs être, avoir and savoir, and the place of pronouns after the verb.",
        objectives=[
            "Form the imperative of regular and irregular verbs for tu, nous and vous",
            "Drop the -s of the tu form of -er verbs (and aller), except before y and en",
            "Make the imperative negative with ne ... pas around the verb",
            "Place pronouns after the affirmative imperative and before the negative one (Donne-le-moi / Ne me le donne pas)",
        ],
        key_concepts=["Impératif", "Tu, nous, vous", "Être / avoir / savoir", "Pronoms après le verbe", "Impératif négatif"],
        blocks=[
            H("Introduction"),
            T("The teacher says: «Ouvrez vos cahiers, écoutez bien et ne parlez pas.» A mother says: «Va au marché, achète du pain et reviens vite.» A friend says: «Allons jouer !» "
              "These are orders, advice or invitations. They use the **imperative** (l'impératif)."),
            D("The **imperative** is the mood used to give an order, advice, a request or an invitation. It has only **three forms**: **tu**, **nous** and **vous**. "
              "The subject pronoun is **never** written.", title="Definition"),
            H("Forming the imperative"),
            T("Take the present tense and drop the subject pronoun: *tu finis* -> **Finis !**, *nous finissons* -> **Finissons !**, *vous finissez* -> **Finissez !** "
              "There is one change: -er verbs (and **aller**, and verbs like **ouvrir** and **offrir**) lose the **-s** of the tu form."),
            CODE("""            parler      finir       vendre      prendre     aller
tu          Parle !     Finis !     Vends !     Prends !    Va !
nous        Parlons !   Finissons ! Vendons !   Prenons !   Allons !
vous        Parlez !    Finissez !  Vendez !    Prenez !    Allez !""", "text", title="Impératif régulier"),
            CODE("""            être      avoir     savoir     vouloir
tu          Sois !    Aie !     Sache !    Veuille !
nous        Soyons !  Ayons !   Sachons !  Veuillons !
vous        Soyez !   Ayez !    Sachez !   Veuillez !""", "text", title="Quatre verbes irréguliers"),
            T("Examples: **Sois** patient ! **Aie** du courage ! **Soyez** à l'heure demain. **Veuillez** patienter (a polite formula used in writing). "
              "The tu form of an -er verb takes its **-s back** before **y** or **en**, so that the sounds join: *Vas-y !* *Manges-en !* *Parles-en à ton père.*"),
            H("The negative imperative"),
            T("Put **ne** before the verb and **pas** (or jamais, plus) after it: *Ne parle pas !* *Ne courez pas dans la classe !* *N'oublie pas ton cahier.* "
              "With pronouns, the pronouns stay **before** the verb: *Ne le fais pas !* *Ne lui dis rien.*"),
            H("Pronouns with the imperative"),
            D("In the **affirmative** imperative, the pronouns come **after** the verb and are joined to it by hyphens: **Donne-le-moi !** "
              "In the **negative** imperative, they come **before** the verb, in the usual order: **Ne me le donne pas !**", title="Rule"),
            CODE("""Affirmatif                   Négatif
Prends-le !                  Ne le prends pas !
Donne-moi ton numéro.        Ne me donne pas ton numéro.
Dites-lui la vérité.         Ne lui dites pas la vérité.
Donne-le-moi !               Ne me le donne pas !
Lève-toi !                   Ne te lève pas !
Vas-y !  Parles-en !         N'y va pas !  N'en parle pas !""", "text", title="Pronoms et impératif"),
            T("After the verb, **me** and **te** become **moi** and **toi** (*Donne-moi*, *Lève-toi*). Before **en** and **y** they become **m'** and **t'** (*Donne-m'en*, *Va-t'en*). "
              "The order after the verb is: le/la/les, then moi/toi/lui/nous/vous/leur, then y, then en."),
            EX("Worked example 1: forming the imperative", intro="Give the order for each person: (a) tu: manger (b) vous: finir (c) nous: aller (d) tu: être gentil.", steps=[
                S("(a) tu, manger", text="Present: tu manges. Drop the s: Mange !"),
                S("(b) vous, finir", text="Present: vous finissez. Finissez !"),
                S("(c) nous, aller", text="Present: nous allons. Allons !"),
                S("(d) tu, être", text="Être is irregular: Sois gentil !"),
            ]),
            EX("Worked example 2: with pronouns", intro="Replace the nouns with pronouns: «Donne le livre à Paul.» then make it negative.", steps=[
                S("Find the pronouns", text="Le livre is the COD: le. À Paul is the COI: lui."),
                S("Affirmative", text="After the verb, the order is COD then COI, with hyphens: Donne-le-lui !"),
                S("Negative", text="The pronouns go before the verb, with the usual order: Ne le lui donne pas !"),
            ]),
            MISTAKE("Writing the subject, or keeping the -s of the tu form",
                    "Do not write *Tu parle !* or *Parles !* as an order. Say **Parle !** (no tu, no s). "
                    "The only exception is before y or en: Parles-en ! Vas-y !"),
            MISTAKE("Putting pronouns before the affirmative imperative",
                    "Write **Prends-le !**, not *Le prends !*. And in the negative, the pronoun goes back before the verb: **Ne le prends pas !** "
                    "Also: Donne-moi, not *Donne-me*."),
            QUIZ("Complete: «___ au marché, Paul !» (aller, tu)", ["Vas", "Va", "Allez", "Aller"], 1,
                 "Aller loses the -s in the tu form of the imperative: Va !", hint="Which -er verbs lose the -s of the tu form ?",
                 feedback=["Vas keeps the s of the present. In the imperative the s drops, except before y.", "", "Allez is the vous form.", "Aller is the infinitive."]),
            QUIZ("Which sentence is correct ?", ["Donne-me le livre !", "Donne-moi le livre !", "Me donne le livre !", "Donne-moi-le !"], 1,
                 "After the verb, me becomes moi: Donne-moi le livre !", hint="What happens to me after an affirmative imperative ?",
                 feedback=["Me becomes moi after the verb.", "", "In the affirmative, the pronoun comes after the verb.", "With two pronouns, le comes before moi: Donne-le-moi."]),
            PQ("Write the imperative for the form indicated: (a) tu: ouvrir la fenêtre (b) vous: être à l'heure (c) nous: partir tout de suite.",
               "(a) Ouvre la fenêtre ! (ouvrir loses the s like an -er verb). (b) Soyez à l'heure ! (c) Partons tout de suite !"),
            PQ("Make the sentence negative: «Prends-le !» and «Dites-lui la vérité !»",
               "Ne le prends pas ! Ne lui dites pas la vérité ! The pronouns go before the verb."),
            PQ("Replace the nouns by pronouns: «Donne ces fruits à ta sœur.» (affirmative)",
               "Donne-les-lui ! Les fruits is the COD (les) and à ta sœur the COI (lui); COD first, hyphens between."),
            SUM("Three forms only: tu, nous, vous, with no subject pronoun.",
                "Take the present tense; -er verbs and aller lose the -s in the tu form (Parle !, Va !), except before y or en (Vas-y !).",
                "Irregular: sois/soyons/soyez, aie/ayons/ayez, sache/sachons/sachez.",
                "Negative: ne + verb + pas. Affirmative: pronouns after the verb with hyphens (Donne-le-moi); negative: before the verb (Ne me le donne pas)."),
        ],
    ),
]


# ---------------------------------------------------------------------- 12. Imparfait
LESSONS += [
    lesson(
        module=M2,
        topic="Imparfait and passé composé",
        title="The imparfait: formation and uses",
        slug="fr1-imparfait",
        minutes=20,
        summary="The imparfait describes the past: habits, scenes, states and actions in progress. Form it from the nous form of the present without -ons, then add -ais, -ais, -ait, -ions, -iez, -aient. Être is the only irregular stem: ét-.",
        objectives=[
            "Form the imparfait of regular and irregular verbs from the nous form of the present",
            "Apply the spelling changes of manger, commencer and étudier",
            "Use the imparfait for habits, descriptions, background and actions in progress",
            "Recognise time words that point to the imparfait (souvent, chaque jour, autrefois ...)",
        ],
        key_concepts=["Imparfait", "Radical de nous", "Habitude passée", "Description", "Action en cours"],
        blocks=[
            H("Introduction"),
            T("A grandmother in Bafoussam remembers: «Quand j'étais petite, nous habitions dans un petit village. Chaque matin, je me levais à cinq heures, j'allais à la rivière et mon père travaillait au champ.» "
              "All these verbs are in the **imparfait**. The imparfait paints a picture of the past: what used to happen, what things were like. "
              "It does not say that something started or finished."),
            H("Forming the imparfait"),
            D("To form the **imparfait**: take the **nous** form of the present, remove **-ons**, and add the endings **-ais, -ais, -ait, -ions, -iez, -aient**.", title="Rule"),
            CODE("""parler (nous parlons)       finir (nous finissons)      vendre (nous vendons)
je parlais                  je finissais                je vendais
tu parlais                  tu finissais                tu vendais
il parlait                  il finissait                il vendait
nous parlions               nous finissions             nous vendions
vous parliez                vous finissiez              vous vendiez
ils parlaient               ils finissaient             ils vendaient""", "text", title="L'imparfait régulier"),
            CODE("""aller (nous allons)     -> j'allais
faire (nous faisons)    -> je faisais
prendre (nous prenons)  -> je prenais
venir (nous venons)     -> je venais
avoir (nous avons)      -> j'avais
pouvoir (nous pouvons)  -> je pouvais
être                    -> j'étais, tu étais, il était, nous étions, vous étiez, ils étaient""", "text", title="Verbes irréguliers"),
            T("Être is the only verb whose imparfait does not come from nous: the stem is **ét-**. "
              "The endings -ais, -ais, -ait and -aient sound the same, so you must remember the spelling. "
              "The nous and vous forms have an **-i-**: *nous parlions*, *vous parliez*."),
            KEY("Spelling points", "Keep the sound of the stem.", cards=[
                ["manger", "je mangeais, il mangeait, ils mangeaient (e kept before a); nous mangions, vous mangiez"],
                ["commencer", "je commençais, il commençait (ç before a); nous commencions, vous commenciez"],
                ["étudier", "Two i's in the nous and vous forms: nous étudiions, vous étudiiez"],
            ]),
            H("The uses of the imparfait"),
            KEY("When to use the imparfait", "Think of a picture, not of a photograph.", cards=[
                ["Habit in the past", "Quand j'étais petit, j'allais au marché tous les samedis."],
                ["Description and state", "La maison était grande. Il faisait chaud. Elle avait quinze ans."],
                ["Action in progress", "Je lisais quand tu as téléphoné. (The reading was going on.)"],
                ["Background, with another action", "Il pleuvait quand nous sommes sortis. (The rain is the setting.)"],
            ]),
            T("Time words that often go with the imparfait: **souvent, toujours, d'habitude, chaque jour, tous les jours, le samedi, autrefois, à cette époque, pendant que**. "
              "Also **si + imparfait** suggests or imagines: «Si on allait au marché ?» (What if we went to the market ?), «Si j'avais de l'argent, ...» (see the lesson on the conditionnel)."),
            EX("Worked example 1: forming", intro="Put the verbs in the imparfait: (a) nous (habiter) (b) ils (finir) (c) je (être) (d) elle (commencer) (e) nous (manger).", steps=[
                S("(a) nous habitions", text="Present nous habitons -> remove -ons -> habit- + ions."),
                S("(b) ils finissaient", text="Nous finissons -> finiss- + aient."),
                S("(c) j'étais", text="Être has the stem ét-: j'étais."),
                S("(d) elle commençait", text="Nous commençons -> commenç-; keep the ç before the a of -ait."),
                S("(e) nous mangions", text="Nous mangeons -> mang- + ions. The e is not needed before i."),
            ]),
            EX("Worked example 2: choosing a tense", intro="Put the verbs in the right tense: «Autrefois, mon père (travailler) à la gare. Chaque matin, il (prendre) le train à six heures.»", steps=[
                S("Look at the time words", text="Autrefois and chaque matin show a habit in the past: imparfait."),
                S("Conjugate", text="Mon père travaillait (travaill- + ait). Il prenait (nous prenons -> pren- + ait)."),
                S("Write it", text="Autrefois, mon père travaillait à la gare. Chaque matin, il prenait le train à six heures."),
            ]),
            MISTAKE("Using the stem of the infinitive instead of nous",
                    "Write nous finissions and il finissait (from finissons), not *nous finions*. And write j'allais, not *j'irais* (that is the conditionnel). "
                    "A reliable method: say the nous form, remove -ons, add the ending."),
            MISTAKE("Forgetting the mark that keeps the sound",
                    "Before a, French writes mangeait, commençait. Before i it does not need the extra letter: mangions, commencions. "
                    "Also keep the -i- of étudiions and the ét- stem of être."),
            QUIZ("Nous ___ (habiter) à Bafoussam quand j'étais petit.", ["habitons", "habitions", "habitiez", "habitaient"], 1,
                 "Imparfait, nous: habit- + ions.", hint="Which ending goes with nous in the imparfait ?",
                 feedback=["Habitons is the present.", "", "Habitiez goes with vous.", "Habitaient goes with ils/elles."]),
            QUIZ("Il ___ (faire) très chaud ce jour-là.", ["fait", "faisait", "ferait", "a fait"], 1,
                 "A description of the weather in the past: faisait (nous faisons -> fais- + ait).", hint="Is it a description in the past ?",
                 feedback=["Fait is the present.", "", "Ferait is the conditionnel.", "A fait is the passé composé: it announces an event, not a description."]),
            PQ("Put in the imparfait: (a) tu (avoir) (b) vous (finir) (c) ils (aller) (d) nous (commencer).",
               "(a) tu avais (b) vous finissiez (c) ils allaient (d) nous commencions."),
            PQ("Rewrite in the past (imparfait): «Chaque samedi, j'achète des légumes et ma mère prépare le repas.»",
               "Chaque samedi, j'achetais des légumes et ma mère préparait le repas. (Habit in the past: nous achetons -> achet- + ais; nous préparons -> préparait.)"),
            PQ("Write in French: «When I was a child, we lived in Douala and I went to school by taxi.»",
               "Quand j'étais enfant, nous habitions à Douala et j'allais à l'école en taxi. All the verbs describe a past situation or habit."),
            SUM("Imparfait stem = nous form of the present minus -ons. Endings: -ais, -ais, -ait, -ions, -iez, -aient.",
                "Être is irregular: j'étais. Spelling: je mangeais, nous mangions; je commençais, nous commencions.",
                "Use the imparfait for habits, descriptions, states and actions in progress or in the background.",
                "Time words: souvent, chaque jour, autrefois, d'habitude, pendant que."),
        ],
    ),
]


# ---------------------------------------------------------------------- 13. Passé composé and imparfait
LESSONS += [
    lesson(
        module=M2,
        topic="Imparfait and passé composé",
        title="The passé composé, and choosing between passé composé and imparfait",
        slug="fr1-passe-compose",
        minutes=25,
        summary="The passé composé is made with avoir or être in the present plus a past participle. Most verbs take avoir; a short list of verbs of movement and all reflexive verbs take être. The passé composé tells what happened; the imparfait describes the scene.",
        objectives=[
            "Form the past participle of -er, -ir, -re verbs and of common irregular verbs",
            "Choose between avoir and être as the auxiliary",
            "Make the passé composé negative and place pronouns correctly",
            "Choose between the passé composé (event) and the imparfait (background or habit) in a short text",
        ],
        key_concepts=["Passé composé", "Auxiliaire", "Participe passé", "Verbes avec être", "Verbes pronominaux", "Passé composé et imparfait"],
        blocks=[
            H("Introduction"),
            T("Ama tells a friend about her day: «Hier, je me suis levée à six heures, j'ai pris le taxi et je suis arrivée au collège à sept heures. Il pleuvait, mais j'ai couru jusqu'à la classe.» "
              "The verbs *me suis levée, ai pris, suis arrivée, ai couru* are in the **passé composé**. They tell what happened. The verb *pleuvait* is in the imparfait: it describes the weather."),
            H("Forming the passé composé"),
            D("The **passé composé** is made of an **auxiliary** (avoir or être in the present) and a **past participle**: j'**ai mangé**, elle **est partie**.", title="Definition"),
            CODE("""-er  ->  é      parler -> parlé      manger -> mangé
-ir  ->  i      finir -> fini        choisir -> choisi
-re  ->  u      vendre -> vendu      attendre -> attendu

Irréguliers :
avoir eu        être été        faire fait      dire dit
prendre pris    apprendre appris   comprendre compris
mettre mis      voir vu         pouvoir pu      vouloir voulu
savoir su       devoir dû       boire bu        lire lu
écrire écrit    ouvrir ouvert   venir venu      naître né
mourir mort     connaître connu   recevoir reçu   vivre vécu""", "text", title="Le participe passé"),
            H("Avoir or être ?"),
            T("**Most verbs** use **avoir**: j'ai parlé, tu as fini, nous avons vendu. "
              "A short list of verbs of movement or change use **être**, and so do all **reflexive** verbs (se lever, se laver, se promener)."),
            CODE("""aller (allé)      venir (venu)       arriver (arrivé)    partir (parti)
entrer (entré)    sortir (sorti)     monter (monté)      descendre (descendu)
rester (resté)    tomber (tombé)     naître (né)         mourir (mort)
retourner (retourné)   devenir (devenu)   revenir (revenu)   rentrer (rentré)
+ tous les verbes pronominaux : je me suis levé(e), elle s'est lavée""", "text", title="Verbes conjugués avec être"),
            CODE("""avoir                         être
j'ai mangé                    je suis parti(e)
tu as mangé                   tu es parti(e)
il / elle a mangé             il est parti / elle est partie
nous avons mangé              nous sommes parti(e)s
vous avez mangé               vous êtes parti(e)(s)
ils / elles ont mangé         ils sont partis / elles sont parties""", "text", title="Passé composé de manger et de partir"),
            TIP("Memory aid for the être verbs: think of a house. You **enter** (entrer), **go up** (monter), **stay** (rester), **go down** (descendre), **go out** (sortir), **leave** (partir) and **come back** (revenir, rentrer). "
                "Be careful: a few of these verbs take avoir when they have a direct object: «J'ai sorti la voiture», «Elle a monté les valises», «Il a descendu l'escalier». "
                "Textbooks differ on the details (à vérifier dans votre manuel)."),
            T("The agreement of the participle is the subject of a separate lesson. For now remember: with **être** the participle agrees with the subject (*elle est partie*, *ils sont arrivés*); with **avoir** it does not agree with the subject."),
            T("**Negative:** ne ... pas surrounds the auxiliary: *Je n'ai pas mangé.* *Elle n'est pas venue.* "
              "**Pronouns** come before the auxiliary: *Je l'ai vu.* *Nous leur avons parlé.* *Il n'y est pas allé.*"),
            H("Passé composé or imparfait ?"),
            KEY("Two tenses, two jobs", "Together they tell a story.", cards=[
                ["Passé composé", "An event, finished and counted: Hier, j'ai pris le taxi. Il est arrivé à huit heures. Elle a ouvert la porte."],
                ["Imparfait", "The scene, the habit, the action in progress: Il pleuvait. Je lisais. Nous allions souvent au marché."],
                ["Both together", "Je lisais quand tu as téléphoné. Il faisait nuit quand nous sommes arrivés."],
            ]),
            T("Ask yourself: is this the **frame** of the story (weather, time, feelings, habits, what was going on) or an **event** that moves the story forward (what happened) ? "
              "Words that point to the passé composé: **hier, un jour, soudain, tout à coup, ce matin, à huit heures**. "
              "Words that point to the imparfait: **souvent, toujours, d'habitude, chaque jour, pendant que**."),
            EX("Worked example 1: forming the passé composé", intro="Put in the passé composé: (a) nous (finir) (b) elle (partir) (c) j' (prendre) (d) ils (vendre).", steps=[
                S("(a) finir, nous", text="Avoir: nous avons + fini = nous avons fini."),
                S("(b) partir, elle", text="Partir takes être, and elle is feminine: elle est partie."),
                S("(c) prendre, je", text="Irregular participle pris: j'ai pris."),
                S("(d) vendre, ils", text="Participle vendu: ils ont vendu."),
            ]),
            EX("Worked example 2: telling a story", intro="Put the verbs in the right tense: «Ce matin, il (faire) beau. Je (prendre) le taxi, et je (arriver) au collège à sept heures. Mes amis (attendre) devant la porte.»", steps=[
                S("Weather: description", text="Imparfait: il faisait beau."),
                S("Event", text="Passé composé: j'ai pris le taxi."),
                S("Event", text="Arriver takes être: je suis arrivé(e) au collège."),
                S("Action in progress", text="Imparfait: mes amis attendaient devant la porte."),
            ]),
            MISTAKE("Using avoir with a verb that needs être",
                    "Write elle est partie, not *elle a parti*. And write il est tombé, not *il a tombé*. "
                    "If you are unsure, check whether the verb is on the list of movement verbs or is reflexive."),
            MISTAKE("Using the passé composé for a description or habit",
                    "Write «Quand j'étais petit, j'allais au marché», not *quand j'étais petit, je suis allé au marché* when you mean every week. "
                    "The imparfait is for habits and scenes."),
            QUIZ("Which sentence is correct ?", ["Elle a arrivé hier.", "Elle est arrivée hier.", "Elle est arrivé hier.", "Elle a arrivée hier."], 1,
                 "Arriver takes être, and the participle agrees with the feminine subject: arrivée.", hint="Is arriver a verb of movement ?",
                 feedback=["Arriver takes être, not avoir.", "", "Elle is feminine, so the participle needs an e.", "Arriver takes être, not avoir."]),
            QUIZ("Choose the right tense: «Hier soir, pendant que je faisais mes devoirs, ma sœur ___ du piano.»", ["a joué", "jouait", "jouera", "jouerait"], 1,
                 "Pendant que shows two actions going on at the same time: imparfait.", hint="Are both actions in progress together ?",
                 feedback=["A joué would present a finished event.", "", "Jouera is the future.", "Jouerait is the conditionnel."]),
            PQ("Put in the passé composé: (a) Je (voir) un accident. (b) Nous (aller) au marché. (c) Elles (se lever) tôt.",
               "(a) J'ai vu un accident. (b) Nous sommes allés au marché (or allées, if only girls). (c) Elles se sont levées tôt."),
            PQ("Make negative: «Il a fini ses devoirs.» and «Elles sont arrivées.»",
               "Il n'a pas fini ses devoirs. Elles ne sont pas arrivées. Ne and pas surround the auxiliary."),
            PQ("Choose the tense: «Quand je (rentrer) à la maison, ma mère (préparer) le dîner.»",
               "Quand je suis rentré(e) à la maison, ma mère préparait le dîner. The entry is an event (passé composé); the cooking was in progress (imparfait)."),
            SUM("Passé composé = avoir or être in the present + past participle. Participles: -é, -i, -u, plus irregulars (pris, fait, vu, dit, mis).",
                "Être: about 17 verbs of movement or change (aller, venir, arriver, partir ...) and all reflexive verbs. Avoir: all the others.",
                "Negative: ne + auxiliary + pas + participle. Pronouns go before the auxiliary.",
                "Passé composé = events; imparfait = scenes, habits, actions in progress."),
        ],
    ),
]


# ---------------------------------------------------------------------- 14. Plus-que-parfait and passé simple
LESSONS += [
    lesson(
        module=M2,
        topic="Plus-que-parfait and passé simple",
        title="The plus-que-parfait and the passé simple",
        slug="fr1-plus-que-parfait-passe-simple",
        minutes=22,
        summary="The plus-que-parfait (imparfait of avoir or être + participle) shows an action that happened before another past action. The passé simple is the tense of written narrative; at this level you must recognise its forms, especially the third person.",
        objectives=[
            "Form the plus-que-parfait with avoir and être, with the right agreement",
            "Use the plus-que-parfait for an action completed before another past action",
            "Recognise the passé simple of regular verbs and of être, avoir, faire, venir, voir, dire, prendre, pouvoir, vouloir",
            "Change a passé simple sentence into the passé composé",
        ],
        key_concepts=["Plus-que-parfait", "Antériorité", "Passé simple", "Récit écrit", "Troisième personne"],
        blocks=[
            H("Introduction"),
            T("Paul arrived at the bus station in Bafoussam. He says: «Quand je suis arrivé, le bus était déjà parti.» "
              "Two things happened in the past, but one came **before** the other. The bus left first, then Paul arrived. "
              "To show the earlier action, French uses the **plus-que-parfait**."),
            H("The plus-que-parfait"),
            D("The **plus-que-parfait** (pluperfect) is formed with the **imparfait** of avoir or être and the **past participle**. "
              "The choice of auxiliary and the agreement of the participle are the same as in the passé composé.", title="Definition"),
            CODE("""avoir                         être
j'avais mangé                 j'étais parti(e)
tu avais mangé                tu étais parti(e)
il avait mangé                il était parti / elle était partie
nous avions mangé             nous étions parti(e)s
vous aviez mangé              vous étiez parti(e)(s)
ils avaient mangé             ils étaient partis / elles étaient parties""", "text", title="Le plus-que-parfait"),
            KEY("Uses of the plus-que-parfait", "It always looks back from a point in the past.", cards=[
                ["Earlier action", "Quand je suis arrivé, le bus était parti. Elle avait déjà fini quand nous sommes entrés."],
                ["Reported past", "Il m'a dit qu'il avait perdu son stylo. (He had lost it before he spoke.)"],
                ["Regret or unreal past", "Si j'avais étudié, j'aurais réussi. (see the conditionnel)"],
            ]),
            TIP("Typical time words: **déjà** (already), **ne ... pas encore** (not yet), **avant**, **après que**, **quand**. "
                "Compare: «Il pleuvait quand je suis sorti» (the rain was going on) and «Il avait plu quand je suis sorti» (the rain had stopped before I went out)."),
            H("The passé simple"),
            D("The **passé simple** is a past tense used in **written narrative**: novels, stories, history texts and the set texts you may meet in an exam. "
              "In everyday speech and in letters, French uses the passé composé instead. At this level you must **recognise** the passé simple, especially the third person (il, elle, ils, elles).", title="Definition"),
            CODE("""            parler      finir       vendre      être       avoir
je          parlai      finis       vendis      fus        eus
tu          parlas      finis       vendis      fus        eus
il / elle   parla       finit       vendit      fut        eut
nous        parlâmes    finîmes     vendîmes    fûmes      eûmes
vous        parlâtes    finîtes     vendîtes    fûtes      eûtes
ils / elles parlèrent   finirent    vendirent   furent     eurent""", "text", title="Le passé simple"),
            CODE("""faire    il fit        ils firent
venir    il vint       ils vinrent
voir     il vit        ils virent
dire     il dit        ils dirent
prendre  il prit       ils prirent
pouvoir  il put        ils purent
vouloir  il voulut     ils voulurent
aller    il alla       ils allèrent""", "text", title="Troisième personne : quelques verbes irréguliers"),
            T("Recognition tips: -er verbs show **-a** (il parla) or **-èrent** (ils parlèrent); most other verbs show **-it / -irent** (il finit, ils finirent; il prit, ils prirent) or **-ut / -urent** (il voulut, ils voulurent). "
              "Be careful: **il finit** can be the present or the passé simple. The context tells which. Textbooks do not always list the same irregular verbs (à vérifier dans votre manuel)."),
            EX("Worked example 1: plus-que-parfait", intro="Put the verb in brackets in the correct tense: «Quand nous (arriver) au marché, les vendeurs (partir) déjà.»", steps=[
                S("Find the order of events", text="The sellers left first, then we arrived. So partir is the earlier action: plus-que-parfait."),
                S("First verb", text="Arriver, nous, passé composé with être: nous sommes arrivés."),
                S("Second verb", text="Partir with être in the imparfait: les vendeurs étaient partis."),
                S("Write it", text="Quand nous sommes arrivés au marché, les vendeurs étaient déjà partis."),
            ]),
            EX("Worked example 2: passé simple to passé composé", intro="Rewrite in the passé composé: «Le roi ouvrit la porte et vit un étranger. Il prit son sac et partit.»", steps=[
                S("Identify the forms", text="ouvrit (ouvrir), vit (voir), prit (prendre), partit (partir)."),
                S("Change each verb", text="ouvrit -> a ouvert; vit -> a vu; prit -> a pris; partit -> est parti."),
                S("Write it", text="Le roi a ouvert la porte et a vu un étranger. Il a pris son sac et est parti."),
            ]),
            MISTAKE("Using the passé composé for the earlier action",
                    "When two past actions are linked, put the earlier one in the plus-que-parfait. "
                    "«Quand j'ai fini, il est parti» means he left after I finished. «Quand j'ai fini, il était parti» means he had already left."),
            MISTAKE("Confusing the passé simple with the imparfait",
                    "Il parla (a single event) is not il parlait (an habit or scene). "
                    "Also remember the circumflex on the nous and vous forms (nous parlâmes, vous finîtes). You will rarely need to write them."),
            QUIZ("Choose the correct form: «Quand je suis arrivé, elle ___ déjà ___ .» (partir)", ["est ... parti", "était ... partie", "avait ... parti", "était ... parti"], 1,
                 "Partir takes être, the earlier action needs the imparfait of être, and elle needs the feminine participle: était partie.", hint="Which tense is needed for the earlier action, and is the subject feminine ?",
                 feedback=["Est partie would be the passé composé, and partie needs an e.", "", "Partir takes être, not avoir.", "Elle is feminine, so the participle needs an e: partie."]),
            QUIZ("What is the infinitive of «ils furent» ?", ["fuir", "être", "faire", "avoir"], 1,
                 "Furent is the passé simple, third person plural, of être.", hint="Compare il fut (he was).",
                 feedback=["The passé simple of fuir would be ils fuirent.", "", "Faire has ils firent.", "Avoir has ils eurent."]),
            PQ("Put in the plus-que-parfait: (a) j'(finir) (b) nous (voir) (c) elles (partir).",
               "(a) j'avais fini (b) nous avions vu (c) elles étaient parties."),
            PQ("Complete: «Il m'a dit qu'il (perdre) son téléphone.»",
               "Il m'a dit qu'il avait perdu son téléphone. The loss happened before he spoke."),
            PQ("Give the infinitive and the passé composé of: «Elle dit», «Ils prirent», «Il fut» (passé simple).",
               "Dire -> elle a dit. Prendre -> ils ont pris. Être -> il a été."),
            SUM("Plus-que-parfait = imparfait of avoir or être + past participle. It shows an action earlier than another past action.",
                "Typical words: déjà, pas encore, avant, après que. The agreement rules are the same as for the passé composé.",
                "Passé simple = tense of written narrative; learn to recognise il/elle/ils/elles forms (parla, finit, prit, fut, firent, vinrent).",
                "In speech and in letters, replace the passé simple with the passé composé."),
        ],
    ),
]


# ---------------------------------------------------------------------- 15. Futur simple and futur antérieur
LESSONS += [
    lesson(
        module=M2,
        topic="Futur simple and futur antérieur",
        title="The futur simple and the futur antérieur",
        slug="fr1-futur-simple-anterieur",
        minutes=22,
        summary="The futur simple is formed from the infinitive (or an irregular stem) plus -ai, -as, -a, -ons, -ez, -ont. The futur antérieur (auxiliary in the futur + participle) shows an action that will be finished before another future action.",
        objectives=[
            "Form the futur simple of regular verbs and of common irregular verbs",
            "Use the futur simple after quand, dès que and si + présent",
            "Form the futur antérieur and use it for an action completed before another future action",
            "Distinguish the futur simple from the futur proche (aller + infinitive)",
        ],
        key_concepts=["Futur simple", "Radical du futur", "Futur antérieur", "Futur proche", "Si + présent"],
        blocks=[
            H("Introduction"),
            T("A student in Maroua plans her year: «L'année prochaine, j'irai au lycée, je travaillerai beaucoup et je passerai l'examen. Quand j'aurai réussi, je ferai un grand voyage.» "
              "The verbs *irai, travaillerai, passerai, ferai* are in the **futur simple**. The verb *aurai réussi* is in the **futur antérieur**."),
            H("The futur simple"),
            D("The **futur simple** is formed from the **infinitive** (for -re verbs, drop the final e) followed by the endings **-ai, -as, -a, -ons, -ez, -ont**. "
              "These endings are the present tense of avoir.", title="Rule"),
            CODE("""parler        finir         vendre (vendr-)
je parlerai   je finirai    je vendrai
tu parleras   tu finiras    tu vendras
il parlera    il finira     il vendra
nous parlerons nous finirons nous vendrons
vous parlerez vous finirez  vous vendrez
ils parleront ils finiront  ils vendront""", "text", title="Futur simple régulier"),
            CODE("""être       ser-      je serai
avoir      aur-      j'aurai
aller      ir-       j'irai
faire      fer-      je ferai
venir      viendr-   je viendrai
pouvoir    pourr-    je pourrai
vouloir    voudr-    je voudrai
savoir     saur-     je saurai
voir       verr-     je verrai
devoir     devr-     je devrai
envoyer    enverr-   j'enverrai
courir     courr-    je courrai""", "text", title="Radicaux irréguliers"),
            T("Spelling: **appeler -> j'appellerai**, **acheter -> j'achèterai**, **payer -> je paierai** (or je payerai), **jeter -> je jetterai**. "
              "Note that all stems end in **-r**, so the sound r is heard before every ending. The endings are the same for every verb."),
            H("Uses of the futur simple"),
            KEY("When to use it", "For what will happen.", cards=[
                ["Future events", "Demain, il fera chaud. Mon frère arrivera la semaine prochaine."],
                ["After quand, dès que, lorsque", "French uses the future where English uses the present: «Je te téléphonerai quand j'arriverai.» (English: when I arrive)"],
                ["Si + présent", "Si tu étudies, tu réussiras. (If + present -> future.) Never put the future after si."],
            ]),
            TIP("The **futur proche** (aller + infinitive) also speaks about the future, but it is closer and more certain: «Je vais partir» (I am about to leave). "
                "The futur simple is more formal and for distant events: «Je partirai en 2030.»"),
            H("The futur antérieur"),
            D("The **futur antérieur** is formed with the **futur simple** of avoir or être and the **past participle**. "
              "It shows an action that will be **finished before** another future action.", title="Definition"),
            CODE("""j'aurai fini           je serai parti(e)
tu auras fini          tu seras parti(e)
il aura fini           il sera parti / elle sera partie
nous aurons fini       nous serons parti(e)s
vous aurez fini        vous serez parti(e)(s)
ils auront fini        ils seront partis / elles seront parties""", "text", title="Futur antérieur"),
            T("«Quand j'aurai fini mes devoirs, je regarderai la télévision.» (First I will finish, then I will watch.) "
              "«Dès qu'ils seront arrivés, nous mangerons.» "
              "It is often used after **quand, lorsque, dès que, aussitôt que, après que**, together with a futur simple in the main clause. "
              "The agreement of the participle follows the passé composé rules."),
            EX("Worked example 1: forming the futur simple", intro="Put in the futur simple: (a) nous (parler) (b) tu (faire) (c) ils (aller) (d) vous (vendre).", steps=[
                S("(a) parler, nous", text="Infinitive + ons: nous parlerons."),
                S("(b) faire, tu", text="Irregular stem fer-: tu feras."),
                S("(c) aller, ils", text="Irregular stem ir-: ils iront."),
                S("(d) vendre, vous", text="Drop the final e: vendr- + ez = vous vendrez."),
            ]),
            EX("Worked example 2: futur antérieur", intro="Complete: «Quand tu (finir) tes études, tu (chercher) un travail.»", steps=[
                S("Order of events", text="First you will finish your studies, then you will look for a job."),
                S("First verb", text="Futur antérieur: tu auras fini."),
                S("Second verb", text="Futur simple: tu chercheras."),
                S("Write it", text="Quand tu auras fini tes études, tu chercheras un travail."),
            ]),
            MISTAKE("Using the present after quand, or the future after si",
                    "Say «Quand il viendra, nous mangerons» (not *quand il vient* for a future). But after si, use the present: «Si tu viens, nous mangerons», never *si tu viendras*."),
            MISTAKE("Wrong stems of irregular verbs",
                    "Write j'irai, not *j'allerai*; je ferai, not *je faiserai*; il faudra, il pourra, ils seront. "
                    "Also keep the double r of courrai, verrai and pourrai: the stems are courr-, verr- and pourr-."),
            QUIZ("Demain, nous ___ (aller) au marché.", ["allerons", "irons", "irions", "allons"], 1,
                 "Aller has the irregular stem ir-: nous irons.", hint="What is the stem of aller in the future ?",
                 feedback=["Aller has an irregular stem.", "", "Irions is the conditionnel.", "Allons is the present."]),
            QUIZ("Which sentence is correct ?", ["Si tu viendras, nous mangerons.", "Si tu viens, nous mangerons.", "Si tu viennes, nous mangerons.", "Si tu viendrais, nous mangerons."], 1,
                 "After si, French uses the present: Si tu viens, nous mangerons.", hint="Which tense follows si when the main verb is in the future ?",
                 feedback=["The future never follows si in this structure.", "", "Viennes is the subjunctive.", "Viendrais is the conditionnel."]),
            PQ("Put in the futur simple: (a) je (être) (b) elle (avoir) (c) vous (pouvoir) (d) ils (voir).",
               "(a) je serai (b) elle aura (c) vous pourrez (d) ils verront."),
            PQ("Complete: «Dès que nous (arriver), nous (téléphoner) à nos parents.» (use the futur antérieur for the first verb)",
               "Dès que nous serons arrivés, nous téléphonerons à nos parents. Arriver takes être; arrivés agrees with nous."),
            PQ("Write in French: «If it rains tomorrow, we will stay at home.»",
               "S'il pleut demain, nous resterons à la maison. Si + il becomes s'il; present after si, futur in the main clause."),
            SUM("Futur simple = infinitive (or irregular stem) + -ai, -as, -a, -ons, -ez, -ont. Irregular stems: ser-, aur-, ir-, fer-, viendr-, pourr-, voudr-, saur-, verr-, devr-.",
                "After quand, dès que, lorsque French uses the future. After si, use the present, never the future.",
                "Futur antérieur = auxiliary in the futur simple + participle: an action finished before another future action.",
                "Futur proche (aller + infinitive) is for an event that is near or certain."),
        ],
    ),
]


# ---------------------------------------------------------------------- 16. Conditionnel
LESSONS += [
    lesson(
        module=M2,
        topic="Conditionnel",
        title="The conditionnel: politeness, wishes and conditions",
        slug="fr1-conditionnel",
        minutes=22,
        summary="The conditionnel présent uses the future stem with the imparfait endings (je parlerais). It expresses politeness, wishes and the result of an unlikely condition: si + imparfait, conditionnel. The conditionnel passé (j'aurais parlé) speaks of an unreal past.",
        objectives=[
            "Form the conditionnel présent from the future stem and the imparfait endings",
            "Use the conditionnel for polite requests, wishes and advice",
            "Build conditional sentences: si + imparfait, conditionnel présent",
            "Recognise the conditionnel passé and the future in the past in reported speech",
        ],
        key_concepts=["Conditionnel présent", "Politesse", "Si + imparfait", "Conditionnel passé", "Futur dans le passé"],
        blocks=[
            H("Introduction"),
            T("At the market a customer says politely: «Bonjour madame, je voudrais un kilo de tomates, s'il vous plaît. Pourriez-vous me faire un petit prix ?» "
              "The seller dreams aloud: «Si j'avais plus d'argent, j'ouvrirais un deuxième magasin.» "
              "The verbs *voudrais, pourriez, ouvrirais* are in the **conditionnel**."),
            H("Forming the conditionnel présent"),
            D("The **conditionnel présent** is formed with the **future stem** (the same as the futur simple) and the **imparfait endings**: **-ais, -ais, -ait, -ions, -iez, -aient**.", title="Rule"),
            CODE("""            parler        finir         être       avoir      aller
je          parlerais     finirais      serais     aurais     irais
tu          parlerais     finirais      serais     aurais     irais
il / elle   parlerait     finirait      serait     aurait     irait
nous        parlerions    finirions     serions    aurions    irions
vous        parleriez     finiriez      seriez     auriez     iriez
ils / elles parleraient   finiraient    seraient   auraient   iraient""", "text", title="Le conditionnel présent"),
            CODE("""faire     ferais       venir     viendrais
pouvoir   pourrais     vouloir   voudrais
savoir    saurais      voir      verrais
devoir    devrais      envoyer   enverrais""", "text", title="Autres radicaux irréguliers"),
            TIP("Compare: futur **parlerai** (-ai) and conditionnel **parlerais** (-ais). In writing the difference is the s; in speech the difference is small, so be careful in dictations and Paper 1 questions. "
                "Remember: future ending = avoir (ai, as, a ...); conditional ending = imparfait (ais, ais, ait ...)."),
            H("Uses of the conditionnel"),
            KEY("Four common uses", "It softens, wishes and imagines.", cards=[
                ["Politeness", "Je voudrais un café. Pourriez-vous m'aider ? Tu devrais te reposer."],
                ["Wish or advice", "J'aimerais voyager. À ta place, je parlerais à ton professeur."],
                ["Condition", "Si j'avais le temps, je viendrais. (si + imparfait, conditionnel)"],
                ["Future in the past", "Il a dit qu'il viendrait demain. (reported speech after a past tense)"],
            ]),
            H("Conditional sentences"),
            CODE("""Condition possible     si + présent,   futur            Si tu viens, nous mangerons.
Condition improbable   si + imparfait, conditionnel     Si tu venais, nous mangerions.
Condition irréelle     si + plus-que-parfait, conditionnel passé
                                              Si tu étais venu, nous aurions mangé.""", "text", title="Les trois systèmes avec si"),
            D("The **conditionnel passé** is formed with the conditionnel présent of avoir or être and the past participle: **j'aurais fini**, **elle serait partie**. "
              "It speaks about something that did not happen in the past, or a regret.", title="Conditionnel passé"),
            T("Never put the conditionnel after **si** in these structures. The error *si j'aurais le temps* is very common. "
              "Say: «Si j'avais le temps, je viendrais.» The conditionnel is in the result clause, not in the clause with si."),
            EX("Worked example 1: forming", intro="Put in the conditionnel présent: (a) je (parler) (b) nous (finir) (c) ils (être) (d) tu (avoir).", steps=[
                S("(a) parler, je", text="Future stem parler- + ais: je parlerais."),
                S("(b) finir, nous", text="Stem finir- + ions: nous finirions."),
                S("(c) être, ils", text="Stem ser- + aient: ils seraient."),
                S("(d) avoir, tu", text="Stem aur- + ais: tu aurais."),
            ]),
            EX("Worked example 2: a conditional sentence", intro="Complete: «Si j'(avoir) de l'argent, je (voyager) en Europe.»", steps=[
                S("Identify the structure", text="The condition is unlikely or imaginary: si + imparfait, conditionnel."),
                S("First verb", text="Imparfait of avoir, j': si j'avais."),
                S("Second verb", text="Conditionnel of voyager, je: je voyagerais."),
                S("Write it", text="Si j'avais de l'argent, je voyagerais en Europe."),
            ]),
            MISTAKE("Using the conditionnel after si",
                    "Wrong: *Si j'aurais de l'argent, j'achèterais une voiture.* Right: Si j'avais de l'argent, j'achèterais une voiture. "
                    "After si, use the present, the imparfait or the plus-que-parfait. Never the futur or the conditionnel."),
            MISTAKE("Mixing up the future and the conditionnel",
                    "«Si tu viens, nous mangerons» (future, possible) is not the same as «Si tu venais, nous mangerions» (imaginary). "
                    "Check which tense follows si, and match the result clause."),
            QUIZ("Which sentence is correct ?", ["Si j'aurais le temps, je viendrais.", "Si j'avais le temps, je viendrais.", "Si j'ai eu le temps, je viendrais.", "Si j'aurai le temps, je viendrais."], 1,
                 "After si, use the imparfait (si j'avais) and put the conditionnel in the result clause.", hint="Which tense follows si in this structure ?",
                 feedback=["The conditionnel never follows si here.", "", "The passé composé does not fit this structure.", "The future never follows si."]),
            QUIZ("«Je voudrais un café.» The conditionnel expresses here:", ["an order", "politeness", "a past habit", "a future certainty"], 1,
                 "Je voudrais is more polite than je veux.", hint="Compare je veux and je voudrais.",
                 feedback=["An order would use the imperative or je veux.", "", "A past habit uses the imparfait.", "A future certainty uses the futur simple."]),
            PQ("Put in the conditionnel présent: (a) il (pouvoir) (b) vous (faire) (c) elles (venir) (d) je (vouloir).",
               "(a) il pourrait (b) vous feriez (c) elles viendraient (d) je voudrais."),
            PQ("Complete: «Si nous (avoir) le temps, nous (aller) à la plage.»",
               "Si nous avions le temps, nous irions à la plage. Si + imparfait, conditionnel présent."),
            PQ("Write in French, using the conditionnel passé: «If I had studied, I would have succeeded.»",
               "Si j'avais étudié, j'aurais réussi. Si + plus-que-parfait, conditionnel passé."),
            SUM("Conditionnel présent = future stem + -ais, -ais, -ait, -ions, -iez, -aient.",
                "Uses: politeness (je voudrais), wishes and advice (j'aimerais, tu devrais), result of an unlikely condition, future in the past (il a dit qu'il viendrait).",
                "Structures: si + présent, futur; si + imparfait, conditionnel présent; si + plus-que-parfait, conditionnel passé.",
                "Never put the future or the conditionnel after si in these structures."),
        ],
    ),
]


# ---------------------------------------------------------------------- 17. Subjonctif présent
LESSONS += [
    lesson(
        module=M2,
        topic="Subjonctif présent",
        title="The subjonctif présent",
        slug="fr1-subjonctif-present",
        minutes=25,
        summary="The subjunctive is used after expressions of necessity, wish, emotion, doubt and after certain conjunctions (pour que, avant que, bien que). Form it from the ils stem of the present plus -e, -es, -e, -ions, -iez, -ent; learn the irregular verbs être, avoir, aller, faire, pouvoir, savoir, vouloir.",
        objectives=[
            "Form the subjonctif présent of regular verbs from the ils form of the present",
            "Conjugate the irregular verbs être, avoir, aller, faire, pouvoir, savoir and vouloir",
            "Recognise the expressions and conjunctions that require the subjunctive",
            "Use an infinitive when the subject of both verbs is the same",
        ],
        key_concepts=["Subjonctif", "Il faut que", "Vouloir que", "Bien que", "Pour que", "Infinitif ou subjonctif"],
        blocks=[
            H("Introduction"),
            T("The teacher says: «Il faut que vous fassiez vos devoirs. Je veux que tout le monde soit à l'heure. Bien que vous soyez fatigués, vous devez finir.» "
              "In each sentence, the verb after **que** is in the **subjonctif**. The indicative states facts. The subjunctive is used after expressions of necessity, wish, feeling, doubt and some conjunctions."),
            H("Forming the subjonctif présent"),
            D("For most verbs, take the **ils** form of the present, remove **-ent**, and add the endings **-e, -es, -e, -ions, -iez, -ent**. "
              "The nous and vous forms are then the same as in the imparfait.", title="Rule"),
            CODE("""            parler      finir        vendre       partir
que je      parle       finisse      vende        parte
que tu      parles      finisses     vendes       partes
qu'il       parle       finisse      vende        parte
que nous    parlions    finissions   vendions     partions
que vous    parliez     finissiez    vendiez      partiez
qu'ils      parlent     finissent    vendent      partent""", "text", title="Subjonctif régulier"),
            CODE("""            être      avoir     aller      faire
que je      sois      aie       aille      fasse
que tu      sois      aies      ailles     fasses
qu'il       soit      ait       aille      fasse
que nous    soyons    ayons     allions    fassions
que vous    soyez     ayez      alliez     fassiez
qu'ils      soient    aient     aillent    fassent""", "text", title="Quatre verbes irréguliers"),
            CODE("""            pouvoir     savoir      vouloir     venir      prendre
que je      puisse      sache       veuille     vienne     prenne
que tu      puisses     saches      veuilles    viennes    prennes
qu'il       puisse      sache       veuille     vienne     prenne
que nous    puissions   sachions    voulions    venions    prenions
que vous    puissiez    sachiez     vouliez     veniez     preniez
qu'ils      puissent    sachent     veuillent   viennent   prennent""", "text", title="Autres verbes irréguliers"),
            T("Other verbs with a stem change: **boire** (que je boive, que nous buvions), **voir** (que je voie, que nous voyions), **devoir** (que je doive, que nous devions). "
              "Verbs like prendre, venir and boire have a different stem in nous and vous (que nous prenions, que vous veniez)."),
            H("When to use the subjunctive"),
            KEY("Triggers", "The subjunctive follows que after these.", cards=[
                ["Necessity", "il faut que, il est nécessaire que, il est important que, il vaut mieux que"],
                ["Wish and order", "vouloir que, souhaiter que, désirer que, aimer que, préférer que, exiger que"],
                ["Feeling", "être content que, avoir peur que, regretter que, être triste que, craindre que"],
                ["Doubt", "douter que, ne pas penser que, il est possible que, il est peu probable que"],
                ["Conjunctions", "pour que, afin que, avant que, jusqu'à ce que, bien que, quoique, sans que, à condition que"],
            ]),
            TIP("The subjunctive is **not** used after verbs of certainty or opinion in the affirmative: «Je pense qu'il vient», «Je sais qu'il est là», «Il est certain qu'il a raison» (indicative). "
                "But in the negative or the question, many verbs take the subjunctive: «Je ne pense pas qu'il vienne.» "
                "Textbooks differ on a few cases, such as après que (à vérifier dans votre manuel)."),
            T("**Same subject: use the infinitive.** When both verbs have the same subject, French uses an infinitive, not the subjunctive: "
              "«Je veux partir» (not *je veux que je parte*). «Je suis content de partir.» "
              "Use the subjunctive only when the subjects are different: «Je veux que tu partes.» Before that, always ask: is the subject of the second verb the same as the first ?"),
            EX("Worked example 1: forming the subjunctive", intro="Complete: (a) Il faut que tu (finir) tes devoirs. (b) Je veux que vous (venir). (c) Il faut que nous (être) à l'heure.", steps=[
                S("(a) finir, tu", text="Ils finissent -> finiss- + es: que tu finisses."),
                S("(b) venir, vous", text="The vous form of venir uses the nous stem: que vous veniez."),
                S("(c) être, nous", text="Être is irregular: que nous soyons."),
            ]),
            EX("Worked example 2: subjunctive or indicative ?", intro="Choose: «Je pense que Paul (être) malade. Je ne pense pas qu'il (aller) à l'école.»", steps=[
                S("First verb", text="Penser que in the affirmative takes the indicative: Paul est malade."),
                S("Second verb", text="Ne pas penser que takes the subjunctive: il aille."),
                S("Write it", text="Je pense que Paul est malade. Je ne pense pas qu'il aille à l'école."),
            ]),
            MISTAKE("Using the indicative after il faut que",
                    "Write «Il faut que tu viennes», not *il faut que tu viens*. And «Il faut qu'elle fasse», not *il faut qu'elle fait*. "
                    "After il faut que, vouloir que and bien que, always check the subjunctive."),
            MISTAKE("Using the subjunctive when the subject is the same",
                    "«Je veux que je vienne» is wrong. Say «Je veux venir.» Use the subjunctive only when the two verbs have different subjects: «Je veux que tu viennes.» "
                    "Also remember that espérer que is followed by the indicative in standard French (J'espère qu'il viendra)."),
            QUIZ("Il faut que tu ___ (finir) tes devoirs.", ["finis", "finisses", "finiras", "finirais"], 1,
                 "Il faut que is followed by the subjunctive: que tu finisses.", hint="Which mood follows il faut que ?",
                 feedback=["Finis is the indicative present.", "", "Finiras is the futur simple.", "Finirais is the conditionnel."]),
            QUIZ("Which sentence is correct ?", ["Je veux que tu viens.", "Je veux que tu viennes.", "Je veux que tu viendras.", "Je veux que tu venais."], 1,
                 "Vouloir que takes the subjunctive: que tu viennes.", hint="Which mood follows vouloir que ?",
                 feedback=["Viens is the indicative.", "", "Viendras is the future.", "Venais is the imparfait."]),
            PQ("Put in the subjunctive: (a) Il faut que je (faire) mes devoirs. (b) Bien qu'elle (être) fatiguée, elle travaille. (c) Je veux que vous (avoir) du courage.",
               "(a) que je fasse (b) bien qu'elle soit fatiguée (c) que vous ayez du courage."),
            PQ("Choose the right mood: «Je sais qu'il (être) à Douala.» / «Je doute qu'il (être) à Douala.»",
               "Je sais qu'il est à Douala (certainty: indicative). Je doute qu'il soit à Douala (doubt: subjunctive)."),
            PQ("Write in French: «I want to leave» and «I want you to leave.»",
               "Je veux partir. Je veux que tu partes (or que vous partiez). Same subject: infinitive. Different subjects: subjunctive."),
            SUM("Subjunctive = que + the ils stem of the present + -e, -es, -e, -ions, -iez, -ent.",
                "Irregular: être (sois), avoir (aie), aller (aille), faire (fasse), pouvoir (puisse), savoir (sache), vouloir (veuille).",
                "Use it after il faut que, vouloir que, expressions of feeling and doubt, and pour que, avant que, bien que, jusqu'à ce que, sans que.",
                "Same subject: infinitive. Certainty (je sais que, je pense que): indicative."),
        ],
    ),
]


# ---------------------------------------------------------------------- 18. Past participle agreement
LESSONS += [
    lesson(
        module=M2,
        topic="Past participle agreement",
        title="Agreement of the past participle",
        slug="fr1-participle-agreement",
        minutes=25,
        summary="With être, the past participle agrees with the subject. With avoir, it agrees with a direct object placed before the verb (la lettre que j'ai écrite) and never with the subject. Reflexive verbs follow the direct object rule.",
        objectives=[
            "Agree the participle with the subject after être",
            "Agree the participle with a direct object placed before the verb after avoir",
            "Leave the participle unchanged when the direct object follows or when en is used",
            "Apply the rule to reflexive verbs (elle s'est lavée / elles se sont parlé)",
        ],
        key_concepts=["Accord du participe passé", "Auxiliaire être", "COD placé avant", "Verbes pronominaux", "Participe invariable"],
        blocks=[
            H("Introduction"),
            T("Compare these sentences: «Marie est partie.» «Les mangues que j'ai achetées sont mûres.» «Marie a acheté des mangues.» "
              "The first participle has an -e, the second has -ées, the third has none. The rule behind it is one of the most tested points of French grammar, and Paper 1 questions often ask about it."),
            H("Participles with être"),
            D("With the auxiliary **être**, the past participle **agrees in gender and number with the subject**, like an adjective: add **-e** for feminine, **-s** for plural, **-es** for feminine plural.", title="Rule 1"),
            CODE("""Il est parti.         Elle est partie.
Ils sont partis.      Elles sont parties.
Paul est arrivé.      Marie est arrivée.
Nous sommes allés.    (nous = garçons ou groupe mixte)
Nous sommes allées.   (nous = filles seulement)""", "text", title="Accord avec être"),
            T("With **on**, the participle can stay masculine singular or agree with the people meant: «On est allé au marché» or «On est allées au marché» (if the speakers are girls). "
              "With **vous**, it agrees with the number of people: «Vous êtes arrivée» (one woman) / «Vous êtes arrivés» (several people)."),
            H("Participles with avoir"),
            D("With the auxiliary **avoir**, the past participle **never agrees with the subject**. It agrees with the **direct object (COD) only if the COD comes before the verb**. "
              "If the COD comes after the verb, or if there is no COD, the participle stays in the masculine singular.", title="Rule 2"),
            CODE("""COD après le verbe  (pas d'accord)   Marie a acheté des mangues.
                                     Nous avons vu ces élèves.
COD avant le verbe  (accord)         Les mangues que Marie a achetées sont mûres.
                                     Ces élèves, nous les avons vus.
                                     La lettre, je l'ai écrite hier.
                                     Quelle robe as-tu choisie ?
Pas de COD          (pas d'accord)   Elles ont mangé. Ils ont parlé.""", "text", title="Accord avec avoir"),
            T("The COD can be placed before the verb as: a **personal pronoun** (me, te, le, la, l', nous, vous, les), the relative pronoun **que**, or the question words **quel(le)(s) + noun** or **combien de**. "
              "The participle then agrees with that word's gender and number. For example *Je l'ai vue* means l' = a woman. "
              "**En** is the exception: «J'ai acheté des mangues → J'en ai acheté» (no agreement)."),
            TIP("Quick method: (1) Is the auxiliary être or avoir ? (2) If être, agree with the subject. (3) If avoir, find the COD by asking « who ? what ? » after the verb. (4) If the COD is before the verb, agree with it. Otherwise nothing changes."),
            H("Reflexive verbs"),
            T("Reflexive (pronominal) verbs use **être**, but the participle agrees with the **reflexive pronoun** (se, me, nous...) only if that pronoun is a **direct object**. "
              "«Elle s'est lavée» (she washed herself: se = COD, agreement). «Elle s'est lavé les mains» (the COD *les mains* comes after: no agreement). "
              "«Elles se sont parlé» (parler à quelqu'un: se = COI, no agreement). «Elles se sont téléphoné.» "
              "Textbooks give slightly different lists of special cases such as the participle fait before an infinitive (à vérifier dans votre manuel)."),
            CODE("""-é   -> -ée, -és, -ées       arrivé, arrivée, arrivés, arrivées
-i   -> -ie, -is, -ies       fini, finie, finis, finies
-u   -> -ue, -us, -ues       vu, vue, vus, vues
pris -> prise, prises        mis -> mise, mises
fait -> faite, faites        écrit -> écrite, écrites
dit  -> dite, dites          ouvert -> ouverte, ouvertes""", "text", title="Formes du participe"),
            EX("Worked example 1: avoir with a preceding COD", intro="Make the participle agree: «Les lettres que j'ai (écrire) sont sur la table.»", steps=[
                S("Find the auxiliary", text="J'ai: the auxiliary is avoir."),
                S("Find the COD", text="What did I write ? Les lettres, replaced here by que, which comes before the verb."),
                S("Agree", text="Lettres is feminine plural: écrites."),
                S("Write it", text="Les lettres que j'ai écrites sont sur la table."),
            ]),
            EX("Worked example 2: être and reflexive verbs", intro="Make the participles agree: (a) Marie et Ama sont (arriver) à midi. (b) Elles se sont (laver). (c) Elle s'est (laver) les mains.", steps=[
                S("(a) être, subject", text="Marie et Ama = feminine plural: arrivées."),
                S("(b) reflexive, COD", text="Se = COD (they washed themselves), feminine plural: lavées."),
                S("(c) reflexive, COD after", text="The COD is les mains, after the verb: no agreement: lavé. (Elle s'est lavé les mains.)"),
            ]),
            MISTAKE("Agreeing with the subject after avoir",
                    "Do not write *Marie a acheté des mangues* with acheté changed to *achetée*. With avoir, the subject never decides the agreement. "
                    "Only the COD before the verb matters."),
            MISTAKE("Forgetting the agreement after que or a pronoun",
                    "«Les fruits qu'elle a acheté» is wrong. Que stands for les fruits (masculine plural) and comes before the verb: «Les fruits qu'elle a achetés». "
                    "Likewise «Je les ai vu» is wrong: write «Je les ai vus»."),
            QUIZ("Which sentence is correct ?", ["Elle est parti.", "Elle est partie.", "Elle a partie.", "Elle est partis."], 1,
                 "With être, the participle agrees with the subject: elle est partie.", hint="The subject is feminine singular.",
                 feedback=["The participle needs an e to agree with elle.", "", "Partir takes être.", "Partis is masculine plural."]),
            QUIZ("Which sentence is correct ?", ["Les mangues que j'ai acheté sont mûres.", "Les mangues que j'ai achetées sont mûres.", "Les mangues que j'ai achetés sont mûres.", "Les mangues que j'ai achetée sont mûres."], 1,
                 "Que (= les mangues, feminine plural) is the COD placed before the verb: achetées.", hint="What does que stand for ? Masculine or feminine ?",
                 feedback=["The COD (que) is before the verb, so the participle must agree.", "", "Mangues is feminine, not masculine.", "Mangues is plural, so the participle needs an s."]),
            PQ("Make the participle agree: (a) Elles sont (venir). (b) Les films que nous avons (voir) étaient longs. (c) Ils ont (finir) leur travail.",
               "(a) venues (être, feminine plural subject). (b) vus (que = les films, masculine plural, before the verb). (c) fini (leur travail comes after the verb: no agreement)."),
            PQ("Rewrite with a pronoun and make the participle agree: «J'ai vu Marie hier.»",
               "Je l'ai vue hier. L' = Marie (feminine), placed before the verb, so the participle takes an e."),
            PQ("Choose: «Elle s'est (lever) tôt.» and «Elles se sont (téléphoner).»",
               "Elle s'est levée tôt (se = COD, agreement). Elles se sont téléphoné (téléphoner à: se = COI, no agreement)."),
            SUM("With être (not reflexive), the participle agrees with the subject: elle est partie, ils sont arrivés.",
                "With avoir, it agrees only with a COD placed before the verb: la lettre que j'ai écrite; je les ai vus.",
                "No agreement if the COD comes after, if there is no COD, or with en: j'en ai acheté.",
                "Reflexive verbs: agree with the reflexive pronoun when it is a direct object (elle s'est lavée), not when it is an indirect object (elles se sont parlé)."),
        ],
    ),
]
