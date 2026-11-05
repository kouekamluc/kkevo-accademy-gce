"""Form 5 Logic: Terms (simple apprehension) and Definitions and Logical Division (9 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("logic", "form-5")

M_TERMS = "First Operation of the Mind: Simple Apprehension (Ideas, Words and Terms)"
M_DEFS = "Definitions and Logical Division"
T_PROPS = "Properties of ideas and terms"
T_QQ = "Classification of terms according to quantity and quality"
T_DEF = "Classification of terms according to definiteness of meaning and relation"
T_FUNC = "The basic functions of language"
T_NOTIONS = "Basic notions of definition"
T_KINDS = "Kinds of definition"
T_RULES = "Rules and fallacies of definition"
T_DIV = "Structure and rules of logical division"

LESSONS = []

# ------------------------------------------------------------------ 1. Ideas, words and terms
LESSONS.append(lesson(
    module=M_TERMS,
    topic=T_PROPS,
    title="Ideas, words and terms",
    slug="term-ideas-words-and-terms",
    minutes=18,
    summary="Logic starts with simple apprehension: forming an idea. This lesson separates the idea in the mind, the word that expresses it, and the term, a word or phrase that can be the subject or predicate of a statement.",
    objectives=[
        "Explain what simple apprehension is and what an idea is",
        "Distinguish an idea, a word and a term",
        "Show that one idea can have many words and one word can carry many ideas",
        "Recognise a term, including a term made of several words",
    ],
    key_concepts=["Simple apprehension", "Idea (concept)", "Word", "Term", "Categorematic and syncategorematic words"],
    blocks=[
        H("Introduction"),
        T("A trader in Mokolo says the word 'tomato'. At once her customer thinks of a red, soft fruit. Nobody has shown the customer a tomato. "
          "The customer has an **idea** of one in the mind. The word only called up the idea."),
        T("Logic studies how we think. Traditional logic says the mind does three things: it forms ideas, it makes judgements and it reasons. "
          "This module is about the first one. Later modules are about the other two."),
        D("**Simple apprehension** is the first operation of the mind. It is the act of grasping what something is, without yet saying "
          "anything true or false about it. When you understand 'mango', 'justice' or 'taxi', you perform simple apprehension.",
          title="Simple apprehension"),
        D("An **idea** (also called a **concept**) is what the mind holds when it understands something. It is a thought, not a sound "
          "and not a picture. You can have an idea of 'honesty' even though you cannot draw it.", title="Idea"),
        D("A **word** is a sound or a written sign that stands for an idea. Words belong to a language. English, French and "
          "Cameroon Pidgin use different words for the same thing.", title="Word"),
        D("A **term** is a word or a group of words that stands for an idea and can be the **subject** (what we speak about) or the "
          "**predicate** (what we say about it) of a statement.", title="Term"),
        H("Idea, word and term compared"),
        KEY("Three things, not one", "Each one is at a different level.", cards=[
            ["Idea", "In the mind. The same for everyone who understands it, whatever the language."],
            ["Word", "A sound or written sign. It changes from language to language."],
            ["Term", "A word or phrase doing a job in a statement: subject or predicate."],
        ], note="Logic mostly works with terms, because arguments are built from statements and statements are built from terms."),
        T("**One idea, many words.** The idea of the clear liquid we drink is expressed by 'water' in English, 'eau' in French and 'wata' in "
          "Cameroon Pidgin. The idea is one. The words are three."),
        T("**One word, many ideas.** The word 'bank' can mean a place where money is kept or the side of a river. The word is one. The "
          "ideas are two. We come back to this in the lesson on equivocal terms."),
        H("What counts as a term"),
        T("A term is not always a single word. In the statement 'Cameroonian students are hard-working', the phrase **Cameroonian students** "
          "is one term, and **hard-working** is another. A phrase such as 'the capital of Cameroon' is also one term."),
        T("Some small words are not terms. Words like 'and', 'but', 'if', 'very' and 'of' cannot be the subject or predicate of a "
          "statement alone. Traditional logic calls them **syncategorematic** words: they help to link terms but do not stand for an idea "
          "by themselves. Words that can be terms are **categorematic** ('student', 'river', 'honest')."),
        EX("Worked example 1: find the terms", intro="Find the two terms in the statement 'Cocoa is a cash crop'.", steps=[
            S("Find what the statement is about", text="It speaks about cocoa. So 'cocoa' is the subject term."),
            S("Find what is said about it", text="It says cocoa is 'a cash crop'. The words 'a cash crop' together form the predicate term."),
            S("Check the linking word", text="The word 'is' links the two terms. It is not a term itself."),
            S("Answer", text="The subject term is 'cocoa'. The predicate term is 'cash crop'."),
        ]),
        EX("Worked example 2: idea, word or term?", intro="A mother in Bafoussam says 'maison' to her child, and a boy in Kumba says 'haus'. "
           "Both mean the place where a family lives. Say what is the same and what is different.", steps=[
            S("The idea", text="Both have the same idea in mind: a home for a family. The idea is the same."),
            S("The words", text="'Maison' (French) and 'haus' (Pidgin) are different words, two signs for one idea."),
            S("The term", text="In a statement such as 'The house is old', the words 'the house' work as a term (the subject)."),
            S("Answer", text="One idea, two words. A word becomes a term when it is used as subject or predicate."),
        ]),
        MISTAKE("Thinking the word and the idea are the same", "If someone does not know the English word 'cassava', they can still have the idea of the food. "
                "Do not say 'no word, no idea'. Words express ideas. They do not create them."),
        MISTAKE("Thinking a term is always one word", "'Mount Cameroon', 'the head of the family' and 'a very tall man' are terms made of "
                "several words. Look for the part of the statement that names what we speak about or what we say about it."),
        QUIZ("The French word 'eau' and the English word 'water' are two different ____ for the same ____.",
             ["terms; word", "words; idea", "ideas; word", "ideas; term"], 1,
             "A word is a sign and an idea is what the mind understands. Two languages give two words for one idea.",
             hint="Which of the three is in the mind, and which is a sound or a written sign?",
             feedback=["Terms are words doing a job in a statement. Here we only compare two signs for one thing.", "",
                       "The ideas are not different: both languages express the same thought.",
                       "The two signs are words, not ideas."]),
        QUIZ("In the statement 'Some farmers are generous', which is a term?",
             ["Some farmers", "are", "Both 'Some farmers' and 'generous' are terms", "Only 'generous'"], 2,
             "'Some farmers' is the subject term and 'generous' is the predicate term. The word 'are' only links them.",
             hint="Look for what we speak about and what we say about it.",
             feedback=["That is the subject term, but 'generous' is a term too.", "'Are' is a linking word, not a term.", "",
                       "'Some farmers' is also a term (the subject)."]),
        TIP("This topic appears in Paper 1 as short multiple-choice questions on simple apprehension, ideas, words and terms. "
            "It also helps in Paper 2 Section A when you are asked to define idea, word and term and to show how they differ.",
            title="Exam link"),
        PQ("In your own words, state the difference between an idea and a word.",
           "An idea is a thought in the mind that grasps what something is. A word is a sound or written sign that stands for an idea. "
           "The same idea can be expressed by different words in different languages."),
        PQ("Give one example of one idea with two words, and one example of one word with two ideas.",
           "One idea, two words: 'water' (English) and 'eau' (French). One word, two ideas: 'bank' (a place for money / the side of a river)."),
        PQ("Pick out the terms in the statement: 'The school bell is loud'.",
           "The terms are 'the school bell' (subject) and 'loud' (predicate). The word 'is' links them and is not a term."),
        SUM("Simple apprehension is the first operation of the mind: grasping what something is without saying yet that it is true or false.",
            "An idea is a thought in the mind. A word is a sign for an idea. A term is a word or phrase that can be the subject or predicate of a statement.",
            "One idea can have many words, and one word can carry many ideas.",
            "A term can be several words long. Words like 'and', 'if' and 'of' are linking words, not terms."),
    ],
))

# ------------------------------------------------------------------ 2. Comprehension and extension
LESSONS.append(lesson(
    module=M_TERMS,
    topic=T_PROPS,
    title="Comprehension and extension of a term",
    slug="term-comprehension-and-extension",
    minutes=20,
    summary="Every term has a comprehension (the attributes it includes) and an extension (the things it applies to). When one term is a narrower kind of another, adding attributes shrinks the extension.",
    objectives=[
        "Define comprehension (intension) and extension of a term",
        "Give the comprehension and extension of a simple term",
        "State the inverse relationship between comprehension and extension",
        "Arrange terms in order of increasing comprehension and decreasing extension",
    ],
    key_concepts=["Comprehension (intension)", "Extension", "Inverse relationship", "Genus and species", "Attributes"],
    blocks=[
        H("Introduction"),
        T("A school asks for 'a student' to read the notice at assembly. Many students can do it. Then it asks for 'a Form 5 student from Bamenda "
          "who has a loud voice'. Now far fewer students qualify. We added conditions, and the group got smaller."),
        T("Logic has two words for this. Every term has two sides: what it **means** and what it **covers**."),
        D("The **comprehension** of a term (also called **intension** or **connotation**) is the set of attributes, or qualities, that the "
          "term includes. The comprehension of 'triangle' includes: closed figure, flat, three straight sides, three angles.",
          title="Comprehension (intension)"),
        D("The **extension** of a term (also called **denotation**) is the set of all things to which the term applies. The extension of "
          "'region of Cameroon' is the ten regions.", title="Extension"),
        KEY("Two sides of every term", "Ask two different questions of a term.", cards=[
            ["Comprehension", "What does the term mean? Which attributes must a thing have?"],
            ["Extension", "Which things does the term cover? How many are there in the class?"],
        ], note="Comprehension is about attributes. Extension is about individuals."),
        H("The inverse relationship"),
        T("Look at three terms: **animal**, **mammal**, **dog**. A mammal is an animal that is warm-blooded and feeds its young with milk. "
          "A dog is a mammal that also has its own special features. Each step has more attributes than the one before."),
        IMG("f5l-term-comprehension-extension.svg", alt="Three nested circles: animal contains mammal, which contains dog; the inner circles have more attributes and fewer individuals",
            caption="Figure 1. Animal, mammal and dog: as the comprehension grows, the extension shrinks."),
        T("Every dog is a mammal and every mammal is an animal. So there are more animals than mammals, and more mammals than dogs. "
          "The extension gets smaller as we move from animal to dog. The comprehension gets larger."),
        D("For terms in a series where each is a narrower kind of the one before, the more attributes a term "
          "includes (greater comprehension), the fewer things it applies to (smaller extension), and the other way round.",
          title="Inverse relationship"),
        T("Where does the rule apply? Only when the terms are in one line, each a kind of the one before: animal, mammal, dog. The rule does not "
          "compare unrelated terms. A bicycle is not a kind of teacher, so the rule says nothing about whether 'bicycle' or 'teacher' has the larger extension. "
          "Some books state the rule with extra conditions. If your teacher's book does, follow it."),
        T("In traditional logic the broader term is the **genus** (the wider class) and the narrower term is the **species** (a kind within it). "
          "Mammal is a genus of dog; dog is a species of mammal. A term can be a genus in one pair and a species in another."),
        EX("Worked example 1: order the terms", intro="Arrange in order of increasing comprehension: goalkeeper, person, Cameroonian goalkeeper, footballer, athlete.", steps=[
            S("Find the widest class", text="'Person' covers the most. Not every person is an athlete."),
            S("Narrow step by step", text="An athlete is a kind of person. A footballer is a kind of athlete. A goalkeeper is a kind of footballer. A Cameroonian goalkeeper is a kind of goalkeeper."),
            S("Write the order", text="person, athlete, footballer, goalkeeper, Cameroonian goalkeeper."),
            S("Extension", text="The extension runs the other way. 'Person' has the largest extension and 'Cameroonian goalkeeper' the smallest."),
        ]),
        EX("Worked example 2: attributes of a term", intro="Give part of the comprehension and part of the extension of 'region of Cameroon'.", steps=[
            S("Comprehension", text="A large administrative area of Cameroon, headed by a governor, made up of divisions."),
            S("Extension", text="The things it covers: Adamawa, Centre, East, Far North, Littoral, North, North-West, West, South, South-West."),
            S("Check", text="The comprehension tells us what a region is. The extension lists the regions. They are different questions."),
        ]),
        MISTAKE("Mixing up the two", "Do not give a list of examples when asked for the comprehension. Examples belong to the extension. "
                "Qualities and characteristics belong to the comprehension."),
        MISTAKE("Thinking more attributes means more things", "Adding conditions narrows the class: 'a student' covers more people than "
                "'a student from Bamenda'. In a series of narrower kinds, more attributes means a smaller extension."),
        QUIZ("Which term has the SMALLEST extension?",
             ["Vehicle", "Motor vehicle", "Taxi", "Yellow taxi in Douala"], 3,
             "Each term is a narrower kind of the one before. 'Yellow taxi in Douala' has the most attributes, so it covers the fewest things.",
             hint="Which term adds the most conditions?",
             feedback=["'Vehicle' has the fewest attributes and the largest extension.", "A motor vehicle is wider than a taxi.",
                       "A taxi is wider than a yellow taxi in Douala.", ""]),
        QUIZ("The set of all attributes a term includes is its",
             ["extension", "comprehension", "denotation", "classification"], 1,
             "Comprehension (also called intension or connotation) is the set of attributes.",
             hint="One of these words is about 'what the term means', the other about 'what it covers'.",
             feedback=["Extension is the set of things the term applies to.", "",
                       "Denotation is another name for extension.", "Classification is not a name for either side of a term."]),
        TIP("Paper 1 often asks how extension changes when comprehension increases (it decreases), or asks you to rank terms. "
            "In Paper 2 Section A you may be asked to define both and give an example.", title="Exam link"),
        PQ("Define the comprehension and the extension of the term 'bicycle' with one example each.",
           "Comprehension: the attributes of a bicycle, such as two wheels, a frame, pedals and a seat. Extension: the bicycles themselves, for example "
           "the bicycle of a farmer in Foumban and the bicycle in the school store."),
        PQ("Put in order of increasing extension: crop, cocoa, cash crop.",
           "Cocoa is a kind of cash crop, and a cash crop is a kind of crop. Increasing extension: cocoa, cash crop, crop."),
        PQ("Why does the rule 'more comprehension, less extension' not compare 'bicycle' and 'teacher'?",
           "The rule only works for a series where each term is a narrower kind of the one before. A bicycle is not a kind of teacher, so the rule does not apply."),
        SUM("The comprehension of a term is the set of attributes it includes. The extension is the set of things it applies to.",
            "Comprehension answers 'what does it mean?'. Extension answers 'what does it cover?'.",
            "In a series of narrower and narrower kinds, the more attributes, the fewer things: they vary inversely.",
            "The genus is the wider class and the species is a narrower kind inside it."),
    ],
))

# ------------------------------------------------------------------ 3. Quantity and quality
LESSONS.append(lesson(
    module=M_TERMS,
    topic=T_QQ,
    title="Classifying terms by quantity and quality",
    slug="term-classifying-terms-by-quantity-and-quality",
    minutes=20,
    summary="Terms are classified by quantity (extension) as singular, particular or universal, and by quality as positive, negative or privative. The lesson shows how to tell them apart and notes where textbooks differ.",
    objectives=[
        "Classify a term as singular, particular or universal",
        "Classify a term as positive, negative or privative",
        "Explain the difference between a negative and a privative term",
        "Name two further classifications and say where to check your textbook",
    ],
    key_concepts=["Singular term", "Particular term", "Universal term", "Positive term", "Negative term", "Privative term"],
    blocks=[
        H("Introduction"),
        T("A market woman in Limbe says: 'Yaoundé is far. Some buyers are late. Every seller wants a good place.' Each sentence "
          "speaks about a different amount: one place, a part of the buyers, all the sellers. Logic notes that terms differ in how much "
          "they cover. It also notes that terms differ in what kind of thing they say."),
        T("This lesson sorts terms in two ways: by **quantity** (how much of the class the term covers) and by **quality** (whether the term states "
          "something, denies something, or points to something missing)."),
        H("Classification by quantity"),
        T("Quantity is about extension. Here the question is: how many things does the term stand for in this use?"),
        D("A **singular term** stands for one definite individual: 'Douala', 'Mount Cameroon', 'this student', 'the capital of Cameroon'.",
          title="Singular term"),
        D("A **particular term** stands for some members of a class, but not all of them or not a named one: 'some students', 'a few farmers', 'certain drivers'.",
          title="Particular term"),
        D("A **universal term** stands for every member of a class: 'all students', 'every farmer', 'each driver'.",
          title="Universal term"),
        KEY("Quick test for quantity", "Ask how many it covers.", cards=[
            ["Singular", "One definite person, place or thing."],
            ["Particular", "Some, at least one, not all."],
            ["Universal", "All, every, each."],
        ], note="Textbooks may use slightly different names. Some call a general word like 'student' a common or universal term and then look at the sentence to see how much it covers. Follow your teacher's book."),
        H("Classification by quality"),
        T("Quality is about what the term says about the thing."),
        D("A **positive term** names something that is there: 'healthy', 'farmer', 'literate', 'present'.", title="Positive term"),
        D("A **negative term** denies something. It says a thing is not of a certain kind and has no other meaning: 'non-smoker', 'non-voter', 'not red'.",
          title="Negative term"),
        D("A **privative term** points to the absence of something that should be there. It says a being lacks a quality it ought to have: "
          "'blind' (a person without sight), 'deaf', 'illiterate'.", title="Privative term"),
        T("A stone is not blind. We simply say it has no sight. We call a person or an animal blind because eyes belong to them. "
          "That is the difference: a negative term only denies, and a privative term points to a loss."),
        T("Compare three pairs. 'Voter' is positive and 'non-voter' is negative. 'Sighted' is positive and 'blind' is privative. "
          "'Teacher' is positive and 'non-teacher' is negative."),
        H("Two more classifications (check your textbook)"),
        T("Many textbooks also sort terms as **concrete** or **abstract**, and as **collective** or **distributive**. "
          "Books place these differently. Some put them with this topic and some do not. Check your textbook for where your teacher teaches them. "
          "Here is the usual meaning, so that you can recognise them."),
        KEY("Other classifications you may meet", "Short definitions.", cards=[
            ["Concrete term", "Names a thing: 'bridge', 'mother', 'cocoa tree'."],
            ["Abstract term", "Names a quality taken alone: 'honesty', 'motherhood', 'speed'."],
            ["Collective term", "Names a group as one whole: 'a herd', 'a football team', 'the jury'."],
        ], note="A collective term does not apply to each member alone: a herd is not one cow."),
        EX("Worked example 1: classify by quantity", intro="Classify each term by quantity: (a) Mount Cameroon, (b) some farmers, (c) every driver.", steps=[
            S("(a) Mount Cameroon", text="It stands for one definite mountain. It is a singular term."),
            S("(b) some farmers", text="It stands for part of the farmers. It is a particular term."),
            S("(c) every driver", text="It stands for all drivers. It is a universal term."),
        ]),
        EX("Worked example 2: classify by quality", intro="Classify each term by quality: (a) deaf, (b) non-voter, (c) healthy.", steps=[
            S("(a) deaf", text="A person who should hear but cannot. Something good is missing. It is a privative term."),
            S("(b) non-voter", text="It only says the person is not a voter. It is a negative term."),
            S("(c) healthy", text="It says something is present: good health. It is a positive term."),
        ]),
        MISTAKE("Confusing the words 'not' and 'privative'", "Not every word that sounds negative is a negative term, and not every negative sounding word "
                "is privative. Ask: does it only deny (negative), or does it say that something that should be there is missing (privative)?"),
        MISTAKE("Classifying a single word without the sentence", "The same word can be taken for all or for some, depending on the statement. "
                "'Students' in 'All students must wear uniform' covers all. In 'Some students are late' it covers some. Read the whole statement."),
        QUIZ("The term 'every nurse' is",
             ["singular", "particular", "universal", "privative"], 2,
             "'Every' means all, so the term stands for every member of the class. It is universal in quantity.",
             hint="Does the term cover one thing, some, or all of them?",
             feedback=["A singular term names one definite individual.", "'Particular' means some, but 'every' means all.", "",
                       "'Privative' is a classification by quality, not by quantity."]),
        QUIZ("Which term is PRIVATIVE?",
             ["Teacher", "Non-teacher", "Blind", "Tall"], 2,
             "'Blind' means a being that should see lacks sight. 'Non-teacher' only denies.",
             hint="Look for a lack of something that ought to be present.",
             feedback=["'Teacher' is positive.", "It only denies being a teacher; that is a negative term.", "", "'Tall' is positive."]),
        TIP("In Paper 1 expect questions such as 'The term all students is ...' or 'A term that denotes the absence of a quality that should be present is ...'. "
            "In Paper 2 Section A you may have to classify a list of terms and say why.", title="Exam link"),
        PQ("Classify by quantity: 'the President of the school club', 'some parents', 'all examiners'.",
           "'The President of the school club' stands for one definite person: singular. 'Some parents': particular. 'All examiners': universal."),
        PQ("Give one example of a positive, a negative and a privative term.",
           "Positive: 'healthy'. Negative: 'non-smoker'. Privative: 'deaf'."),
        PQ("What is the difference between a negative term and a privative term?",
           "A negative term only denies that a thing is of a certain kind, for example 'non-voter'. A privative term says that something that should be there is missing, for example 'blind' said of a person."),
        SUM("By quantity (extension), terms are singular (one individual), particular (some) or universal (all).",
            "By quality, terms are positive (something present), negative (a denial) or privative (something missing that should be there).",
            "A negative term only denies; a privative term points to a loss.",
            "Concrete/abstract and collective/distributive are further classifications. Check your textbook for where they belong."),
    ],
))

# ------------------------------------------------------------------ 4. Definiteness of meaning and relation
LESSONS.append(lesson(
    module=M_TERMS,
    topic=T_DEF,
    title="Terms by definiteness of meaning and by relation",
    slug="term-definiteness-of-meaning-and-relation",
    minutes=22,
    summary="Terms may have one meaning (univocal), unrelated meanings (equivocal) or related meanings (analogous). Terms may also stand in relation as correlative, contrary or contradictory terms.",
    objectives=[
        "Distinguish univocal, equivocal and analogous terms",
        "Give examples of each",
        "Distinguish correlative, contrary and contradictory terms",
        "Tell a contrary pair from a contradictory pair using the 'middle' test",
    ],
    key_concepts=["Univocal term", "Equivocal term", "Analogous term", "Correlative terms", "Contrary terms", "Contradictory terms"],
    blocks=[
        H("Introduction"),
        T("A man tells a friend in Bafoussam: 'Let us meet at the bank.' One friend goes to the bank on Avenue Ahidjo. The other goes to the riverside. "
          "They never meet. The word 'bank' carries two meanings, and the confusion is a real problem."),
        T("Logic notes that terms differ in how definite their meaning is. It also notes that some pairs of terms are connected by a relationship. "
          "This lesson explains both."),
        H("Definiteness of meaning"),
        D("A **univocal term** has one meaning, always the same: 'triangle', 'Douala', 'Wednesday'.", title="Univocal term"),
        D("An **equivocal term** has two or more meanings that have nothing to do with each other: 'bank' (where money is kept; the side of a river), "
          "'bark' (of a tree; of a dog), 'light' (not heavy; not dark).", title="Equivocal term"),
        D("An **analogous term** has meanings that are partly the same and partly different, because they are linked by a connection. "
          "'Healthy' is said of a person, of food and of a climate. A healthy person has good health, healthy food helps to cause good health and a healthy "
          "climate is good for health. The meanings are related.", title="Analogous term"),
        KEY("How to tell them apart", "Compare the meanings.", cards=[
            ["Univocal", "One meaning only."],
            ["Equivocal", "Different meanings with no link between them."],
            ["Analogous", "Different meanings, but linked by a real connection."],
        ], note="An equivocal word is used by accident. An analogous word is used on purpose, because of a link. The fallacy of equivocation is studied in Module Nine."),
        EX("Worked example 1: classify the term", intro="Classify 'pen' in these two uses: (a) a pen for writing, (b) a pen for pigs.", steps=[
            S("Compare the meanings", text="One is an instrument for writing. The other is an enclosure for animals."),
            S("Test for a link", text="There is no real link. They are two different things that happen to share one word."),
            S("Answer", text="'Pen' is an equivocal term here."),
        ]),
        EX("Worked example 2: classify the term", intro="Classify 'healthy' in: (a) a healthy child, (b) healthy food.", steps=[
            S("Compare the meanings", text="The child has good health. The food helps a person to keep good health."),
            S("Test for a link", text="Both uses point to health. One has it; the other helps to cause it."),
            S("Answer", text="'Healthy' is an analogous term."),
        ]),
        H("Terms by relation"),
        T("Some terms stand in a relation to each other. Traditional logic names three main kinds."),
        D("**Correlative terms** are pairs that need each other. You cannot understand one without the other: parent and child, teacher and student, buyer and seller, employer and employee.",
          title="Correlative terms"),
        D("**Contrary terms** are opposite extremes with a middle ground between them. They cannot both be true of the same thing, at the same time and in the same respect, but they can both be false: hot and cold, tall and short, rich and poor.",
          title="Contrary terms"),
        D("**Contradictory terms** are opposites with no middle ground. One of them must apply and the other must not: even and not even, citizen and non-citizen.",
          title="Contradictory terms"),
        IMG("f5l-term-contrary-contradictory.svg", alt="Two bars. The first shows contrary terms hot and cold with a middle area between. The second shows contradictory terms even number and not even with no middle.",
            caption="Figure 1. Contrary terms leave a middle; contradictory terms split everything."),
        T("**The middle test.** Ask: can the thing be neither? Water can be neither hot nor cold (it can be warm), so hot and cold are contrary. "
          "A whole number cannot be neither even nor not even, so even and not even are contradictory."),
        T("Note: textbooks sometimes list further relations between terms. If your textbook does, learn them. These three are the ones the topic names."),
        EX("Worked example 3: contrary or contradictory?", intro="Classify the pairs: (a) tall and short, (b) voter and non-voter.", steps=[
            S("(a) tall and short", text="A person can be neither: of medium height. There is a middle. The pair is contrary."),
            S("(b) voter and non-voter", text="A person is one or the other. There is no middle. The pair is contradictory."),
        ]),
        MISTAKE("Calling every opposite 'contradictory'", "Many opposites have a middle. 'Rich' and 'poor' are contrary, because a person can be neither. "
                "Check with the middle test."),
        MISTAKE("Calling an analogous word equivocal", "If the meanings are linked, as with 'healthy', the term is analogous. Only call it equivocal when the meanings have nothing to do with each other."),
        QUIZ("'Husband' and 'wife' are",
             ["contrary terms", "contradictory terms", "correlative terms", "equivocal terms"], 2,
             "You cannot understand 'husband' without 'wife'. They are correlative.",
             hint="Does each term need the other to make sense?",
             feedback=["Contrary terms are opposite extremes with a middle.", "Contradictory terms exclude each other with no middle.", "",
                       "'Equivocal' describes one word with several unrelated meanings."]),
        QUIZ("The word 'bark' (of a tree, of a dog) is",
             ["univocal", "analogous", "equivocal", "correlative"], 2,
             "The two meanings are unrelated. The term is equivocal.",
             hint="Is there a link between the two meanings?",
             feedback=["It has two meanings, so it is not univocal.", "Analogous terms have related meanings.", "",
                       "Correlative terms are pairs that need each other."]),
        TIP("In Paper 1 expect 'Which of the following pairs are contradictory terms?' or 'A word with several unrelated meanings is called ...'. "
            "In Paper 2 Section A you may be asked to define the types and give an example of each.", title="Exam link"),
        PQ("Give one example each of a univocal, an equivocal and an analogous term.",
           "Univocal: 'triangle'. Equivocal: 'bank' (money / river). Analogous: 'healthy' (a person / food / a climate)."),
        PQ("Are 'rich' and 'poor' contrary or contradictory terms? Use the middle test.",
           "They are contrary. A person can be neither rich nor poor, so there is a middle ground. Both cannot be true of the same person at the same time, but both can be false."),
        PQ("Why are 'seller' and 'buyer' called correlative terms?",
           "Each needs the other. There is no seller unless there is a buyer."),
        SUM("Terms may be univocal (one meaning), equivocal (unrelated meanings) or analogous (related meanings).",
            "Correlative terms are pairs that need each other, such as parent and child.",
            "Contrary terms are opposite extremes with a middle ground; both cannot be true but both can be false.",
            "Contradictory terms have no middle: one must be true and the other false."),
    ],
))

# ------------------------------------------------------------------ 5. Functions of language
LESSONS.append(lesson(
    module=M_DEFS,
    topic=T_FUNC,
    title="The basic functions of language",
    slug="def-the-basic-functions-of-language",
    minutes=20,
    summary="Language is used to inform, to express feelings, to direct action and, in special cases, to perform an act by speaking. Many sentences mix these uses, and knowing which is in play helps us judge an argument.",
    objectives=[
        "Name and explain the informative, expressive and directive functions of language",
        "Explain the performative (ceremonial) function",
        "Recognise sentences that mix several functions",
        "Explain why only some uses of language can be true or false and why this matters in argument",
    ],
    key_concepts=["Informative use", "Expressive use", "Directive use", "Performative use", "Mixed use", "True and false"],
    blocks=[
        H("Introduction"),
        T("Think of one morning at a school gate in Ngaoundéré. The teacher says: 'The exam starts at eight.' A pupil shouts: 'Hurray, no more holidays!' "
          "The principal says: 'Line up now.' And a visitor says: 'I declare this new classroom block open.' Four sentences, four different jobs."),
        T("Language does more than pass on facts. Before we can judge an argument or a definition, we must see what job the words are doing. "
          "Textbooks such as Copi and Hurley list three basic functions, and many add a fourth."),
        H("Four functions"),
        D("The **informative function** gives or asks for information: it states facts or claims about the world. Such statements can be true or false. "
          "Example: 'Yaoundé is the political capital of Cameroon.'", title="Informative function"),
        D("The **expressive function** shows feelings or attitudes: joy, anger, sorrow, praise, blame. Such sentences are not true or false in the same way. "
          "Example: 'What a wonderful goal!' or 'I am so tired of this noise.'", title="Expressive function"),
        D("The **directive function** tries to make someone do something, or not do it: commands, requests, advice, instructions. "
          "Commands are not true or false. They are followed or not followed. Example: 'Switch off your phones.' Questions are usually counted here, "
          "because they ask the hearer to supply information (check your textbook).", title="Directive function"),
        D("The **performative function** (which some books call the **ceremonial** use) is the use of words to perform an act, so that by saying them "
          "something is done. Example: 'I promise to pay you tomorrow.' 'I declare the meeting open.' 'I name this child Mary.' The sentence is not "
          "mainly a report: it does the act.", title="Performative function"),
        KEY("Four functions at a glance", "Match the sentence to its job.", cards=[
            ["Informative", "States or asks for facts. True or false."],
            ["Expressive", "Shows feeling. Not true or false in the same way."],
            ["Directive", "Tries to get action. Followed or not followed."],
            ["Performative", "Does an act by speaking. The act is valid or not."],
        ], note="Some textbooks keep only three functions and treat the performative as a special case. Follow your teacher's book."),
        H("Mixed uses"),
        T("Real sentences often do several jobs at once. Take the sentence: 'Our school is the best in town, so you must join us!' It informs (the claim "
          "that the school is the best), it expresses pride, and it directs (an invitation to join)."),
        T("To classify such a sentence, ask which job is **main**, and which jobs are present. If your question asks you to classify, say 'mainly directive, with an informative element'."),
        H("Why this matters for argument"),
        T("An argument is made of statements that can be true or false. Only informative uses can be premises that give evidence. "
          "If a speaker says 'Only a fool would buy from that shop', the sentence looks like a claim, but its main job is to express contempt "
          "and to push the hearer. It is not evidence about the shop."),
        T("Three consequences follow. First, do not ask 'is it true?' of a command. Ask 'should I obey?'. Second, do not treat a "
          "strong feeling as proof. Third, when two people 'disagree', check whether they disagree about facts or only about attitudes. "
          "Facts can be tested. Attitudes cannot be tested in the same way."),
        EX("Worked example 1: classify the sentences", intro="Name the main function of each sentence: (a) 'The market opens at six.' (b) 'Ouch, that hurts!' (c) 'Please sit down.' (d) 'I promise to return your book on Monday.'", steps=[
            S("(a) The market opens at six", text="It states a fact that can be checked. It is informative."),
            S("(b) Ouch, that hurts!", text="It shows pain or feeling. It is expressive."),
            S("(c) Please sit down", text="It asks someone to act. It is directive."),
            S("(d) I promise to return your book on Monday", text="By saying it, the speaker makes a promise. It is performative."),
        ]),
        EX("Worked example 2: a mixed sentence", intro="Classify: 'Stop shouting in the corridor, because the exam is on and it is very disturbing!'", steps=[
            S("Find the command", text="'Stop shouting in the corridor' tells someone to act. It is directive."),
            S("Find the claim", text="'The exam is on' states a fact. It is informative."),
            S("Find the feeling", text="'It is very disturbing' shows annoyance. It is expressive."),
            S("Answer", text="Mainly directive, with informative and expressive elements."),
        ]),
        MISTAKE("Calling every sentence informative", "A sentence with a strong feeling is not always a report. 'That match was a disgrace!' mainly expresses anger. "
                "Ask what the words are trying to do."),
        MISTAKE("Asking whether a command is true", "'Close the door' is neither true nor false. It is a directive. Only informative statements are true or false."),
        QUIZ("'Let us all pray for peace.' The main function is",
             ["informative", "directive", "expressive", "performative"], 1,
             "It invites people to do something: pray. That is directive.",
             hint="Is the speaker reporting a fact, or inviting people to act?",
             feedback=["No fact is being reported.", "", "There is feeling behind it, but the main job is to get people to act.",
                       "A performative act needs words that themselves do the act, such as 'I declare'."]),
        QUIZ("Which of these is MAINLY informative?",
             ["'How awful!'", "'Come here.'", "'The river is five kilometres wide.'", "'I now declare you winner.'"], 2,
             "It states something that can be true or false.",
             hint="Which sentence can be checked by measuring?",
             feedback=["It shows feeling.", "It is a command.", "", "It does an act by saying it; it is performative."]),
        TIP("Paper 1 asks you to name the function of a sentence, and Paper 2 Section A asks you to define the functions with examples. "
            "Link the lesson to arguments: only informative statements can be premises.", title="Exam link"),
        PQ("State the four functions of language and give one example of each.",
           "Informative: 'The school has four hundred pupils.' Expressive: 'What a lovely song!' Directive: 'Open your books.' Performative: 'I declare the meeting open.'"),
        PQ("Classify mainly: 'Buy fresh fish here, the best price in town!'",
           "Mainly directive (it urges the hearer to buy), with an informative claim (best price) and a persuasive feeling."),
        PQ("Why should we not call a command true or false?",
           "A command does not say how things are. It tells someone what to do. It can be obeyed or disobeyed, but not true or false."),
        SUM("Language is used to inform, to express feelings, to direct action and, in special cases, to perform an act by speaking.",
            "Informative statements can be true or false. Expressive and directive sentences are not true or false in the same way.",
            "Many sentences mix functions. Name the main job and the others.",
            "In argument, only informative statements give evidence. Feelings and commands are not proof."),
    ],
))

# ------------------------------------------------------------------ 6. Basic notions of definition
LESSONS.append(lesson(
    module=M_DEFS,
    topic=T_NOTIONS,
    title="Basic notions of definition",
    slug="def-basic-notions-of-definition",
    minutes=20,
    summary="A definition explains the meaning of a term. It has a definiendum (the term) and a definiens (the words that explain it). It serves several purposes and may work by extension or by intension.",
    objectives=[
        "Define a definition, the definiendum and the definiens",
        "Identify the definiendum and the definiens in a given definition",
        "State the main purposes of a definition",
        "Distinguish a definition by extension from a definition by intension",
    ],
    key_concepts=["Definition", "Definiendum", "Definiens", "Purposes of definition", "Extensional definition", "Intensional definition"],
    blocks=[
        H("Introduction"),
        T("A girl moves from Douala to a village near Bamenda. At a family meeting someone says: 'We will start the njangi.' She asks: 'What is a njangi?' "
          "Her cousin answers: 'A group of people who each pay a fixed sum at regular times, and take turns to receive the whole amount.' "
          "That answer is a **definition**."),
        D("A **definition** is a statement that gives the meaning of a term.", title="Definition"),
        D("The **definiendum** is the term being defined. In 'A njangi is a group of people who each pay a fixed sum at regular times and take turns to receive the whole amount', the definiendum is 'njangi'.",
          title="Definiendum"),
        D("The **definiens** is the group of words that does the defining. In the same example it is 'a group of people who each pay a fixed sum at regular times and take turns to receive the whole amount'.",
          title="Definiens"),
        KEY("The two parts", "Remember the order: the thing to be defined, then the words that define it.", cards=[
            ["Definiendum", "The term to be defined. 'What is being explained'."],
            ["Definiens", "The words that explain it. 'What does the explaining'."],
        ], note="The Latin ending '-dum' hints at 'to be defined'. The ending '-ens' hints at the one that is doing it."),
        H("Purposes of definition"),
        T("People define terms for several reasons. Copi and Hurley list these main purposes."),
        KEY("Why we define", "Five common purposes.", cards=[
            ["To increase vocabulary", "A child or a learner meets a new word."],
            ["To remove ambiguity", "A word has two meanings. A definition shows which one is meant."],
            ["To reduce vagueness", "A word has no sharp edge. A rule is set, for example 'adult means 18 and over'."],
            ["To explain theoretically", "A term is explained by a theory, such as 'light' in physics."],
            ["To influence attitudes", "Words are chosen to win approval or disapproval."],
        ], note="You will meet the matching kinds of definition in the lesson 'Kinds of definition'."),
        H("Extension and intension in definition"),
        T("A definition can work in two ways, depending on whether we point to the things or state the attributes. "
          "This links back to comprehension and extension in the lesson on terms."),
        D("A definition by **extension** (also called **denotative**) shows the term by pointing to or listing the things it applies to. "
          "Example: 'A region of Cameroon is Centre, Littoral, West, ...'", title="Extensional definition"),
        D("A definition by **intension** (also called **connotative**) states the attributes that a thing must have to be called by the term. "
          "Example: 'A triangle is a closed plane figure with three straight sides.'", title="Intensional definition"),
        T("Extensional definitions are quick but often incomplete. A list cannot decide a new case. Intensional definitions can decide new cases, "
          "because they give a test. The next lessons show how to build intensional definitions well."),
        EX("Worked example 1: find the two parts", intro="'An orphan is a child whose parents are both dead.' Find the definiendum and the definiens.", steps=[
            S("Find the term that is being explained", text="The sentence is about 'orphan'. That is the definiendum."),
            S("Find the explaining words", text="'A child whose parents are both dead' explains it. That is the definiens."),
            S("Type", text="It states attributes, so it is an intensional definition."),
        ]),
        EX("Worked example 2: extension or intension?", intro="Classify: (a) 'Primary colours are red, yellow and blue.' (b) 'A mammal is a warm-blooded animal that feeds its young with milk.'", steps=[
            S("(a)", text="It lists the members. It is a definition by extension."),
            S("(b)", text="It states attributes. It is a definition by intension."),
        ]),
        MISTAKE("Swapping the two parts", "The definiendum is the term; the definiens is the explanation. Do not write them the wrong way round in an answer."),
        MISTAKE("Thinking a definition proves something", "A definition explains a word. It does not prove that the thing exists or that a claim about it is true."),
        QUIZ("In 'A pharmacist is a person trained to prepare and give out medicines', the definiens is",
             ["pharmacist", "A pharmacist is", "a person trained to prepare and give out medicines", "medicines"], 2,
             "The definiens is the group of words that does the defining.",
             hint="Which part tells us what a pharmacist is?",
             feedback=["That is the term to be defined, the definiendum.", "That includes the term and the linking word.", "",
                       "One word only; the definiens is the whole explaining phrase."]),
        QUIZ("A definition that lists the members of a class is a definition by",
             ["intension", "extension", "connotation", "comprehension"], 1,
             "Listing or pointing to members works through the extension.",
             hint="Which word means 'the set of things'?",
             feedback=["Intension means the attributes.", "", "Connotation is another word for intension.", "Comprehension is another word for intension."]),
        TIP("In Paper 1, expect questions that give a definition and ask for the definiendum or definiens, or ask which purpose a definition serves. "
            "In Paper 2 you may be asked to define 'definition' and name its parts and purposes.", title="Exam link"),
        PQ("Identify the definiendum and the definiens: 'A farmer is a person who grows crops or keeps animals for a living.'",
           "Definiendum: 'farmer'. Definiens: 'a person who grows crops or keeps animals for a living'."),
        PQ("State three purposes of definition with an example for each.",
           "To increase vocabulary: teach a new word such as 'njangi'. To remove ambiguity: say which meaning of 'bank' is meant. To reduce vagueness: say 'adult means 18 years and over'."),
        PQ("Is 'The days of the school week are Monday, Tuesday, Wednesday, Thursday and Friday' a definition by extension or by intension?",
           "By extension. It lists the members."),
        SUM("A definition is a statement of the meaning of a term. The term is the definiendum; the explaining words are the definiens.",
            "Definitions serve several purposes: to increase vocabulary, to remove ambiguity, to reduce vagueness, to explain theoretically and to influence attitudes.",
            "A definition by extension lists or points to members. A definition by intension states the attributes.",
            "A definition explains a word; it does not prove a claim."),
    ],
))

# ------------------------------------------------------------------ 7. Kinds of definition
LESSONS.append(lesson(
    module=M_DEFS,
    topic=T_KINDS,
    title="Kinds of definition",
    slug="def-kinds-of-definition",
    minutes=24,
    summary="Definitions differ by what they describe (real and nominal), by purpose (lexical, stipulative, precising, theoretical, persuasive) and by technique (synonym, example, pointing, genus and difference).",
    objectives=[
        "Distinguish real and nominal definitions",
        "Name and illustrate the five kinds of definition by purpose",
        "Name and illustrate definition by synonym, enumeration, ostension and genus and difference",
        "Say which kinds of definition can be true or false",
    ],
    key_concepts=["Real definition", "Nominal definition", "Lexical", "Stipulative", "Precising", "Theoretical", "Persuasive", "Genus and difference"],
    blocks=[
        H("Introduction"),
        T("At a village football tournament, three people explain 'offside'. The referee gives the rule. The coach shows with a drawing on the ground. "
          "A boy says 'it is when the striker stands too far forward'. All three are defining, but in different ways. "
          "Logic sorts definitions into kinds, so that we can use and judge each kind properly."),
        H("Real and nominal definitions"),
        T("Traditional (Aristotelian) logic has an old and simple division."),
        D("A **nominal definition** explains the meaning of a **word** (from the Latin word nomen, 'name'): how a word is used, where it comes from, or another word that means the same. "
          "Example: 'Philosophy' comes from Greek words meaning 'love of wisdom'.", title="Nominal definition"),
        D("A **real definition** explains the nature of the **thing** itself, by saying what it is. It is usually given by genus and difference. "
          "Example: 'Man is a rational animal.'", title="Real definition"),
        T("Copi and Hurley do not use these two names as their main division. They sort definitions by purpose. We now learn both. If your teacher prefers one scheme, use it."),
        H("Kinds of definition by purpose"),
        D("A **lexical definition** reports the meaning a word already has in the language. It is what a dictionary does. It can be right or wrong. "
          "Example: 'A njangi is a rotating savings group.'", title="Lexical definition"),
        D("A **stipulative definition** gives a meaning to a new term, or a new meaning to an old term, by agreement. It is not true or false. It is a decision. "
          "Example: 'In this exam, a late candidate means anyone who arrives after 8:15.'", title="Stipulative definition"),
        D("A **precising definition** takes a word that already has a meaning but is vague, and makes it sharper for some purpose. "
          "Example: 'For this scholarship, a youth means a person between 15 and 25.'", title="Precising definition"),
        D("A **theoretical definition** explains a term by fitting it into a scientific, philosophical or other theory. "
          "Example: 'Heat is the energy of moving particles of matter.'", title="Theoretical definition"),
        D("A **persuasive definition** tries to change the hearer's attitude or feelings by the way a word is defined. It uses emotional meaning and often stands in for an argument. "
          "Example: 'A school uniform is a badge of pride.'", title="Persuasive definition"),
        KEY("Match purpose to kind", "Ask what the definer is trying to do.", cards=[
            ["Report the usual meaning", "Lexical"],
            ["Give a meaning by agreement", "Stipulative"],
            ["Remove vagueness", "Precising"],
            ["Explain by a theory", "Theoretical"],
            ["Win approval or dislike", "Persuasive"],
        ], note="Only the lexical definition is true or false in the ordinary sense. The stipulative one is a decision and the persuasive one is a way of pushing a view."),
        H("Kinds of definition by technique"),
        T("The same word can be defined in several ways. Here are the usual techniques."),
        D("**By synonym:** use another word with the same meaning. 'Rapid' means 'fast'. It works only if the listener knows the second word.", title="Definition by synonym"),
        D("**By enumeration (by examples):** list members of the class. 'Neighbours of Cameroon are Nigeria, Chad, the Central African Republic, the Republic of Congo, Gabon and Equatorial Guinea.' "
          "A list can leave out items.", title="Definition by enumeration"),
        D("**By ostension (pointing):** show an example. Point to a mango tree and say 'That is a mango tree.' It is useful for things we can see.", title="Ostensive definition"),
        D("**By genus and difference:** name the larger class (the genus) and then what sets the term apart (the difference). "
          "'A triangle (the term) is a plane figure (the genus) with three straight sides (the difference).'", title="Definition by genus and difference"),
        T("Some books also list the **etymological** definition (by the origin of the word) and the **operational** definition (by the test or operation that shows the thing: 'a substance is "
          "soluble in water if it dissolves when placed in water'). Check your textbook for the full list."),
        EX("Worked example 1: name the kind by purpose", intro="Name the kind: 'In our school, Green Day means the last Friday of each month, when we plant trees.'", steps=[
            S("Is a usual meaning being reported?", text="No. 'Green Day' has no meaning in the language except the one given here."),
            S("Is the speaker setting a meaning by agreement?", text="Yes. A new term is given a meaning for use in this school."),
            S("Answer", text="It is a stipulative definition. It is a decision, so it is neither true nor false."),
        ]),
        EX("Worked example 2: name the technique", intro="Name the technique: 'An orphan is a child (the genus) whose parents are both dead (the difference).'", steps=[
            S("Is there a larger class?", text="Yes: 'child'."),
            S("Is there a distinguishing feature?", text="Yes: 'whose parents are both dead'."),
            S("Answer", text="Definition by genus and difference. It is also a real definition in the traditional scheme."),
        ]),
        MISTAKE("Calling every definition 'true or false'", "A stipulative definition is a decision, so it cannot be true or false. Only a lexical definition can be checked against usage."),
        MISTAKE("Using a persuasive definition as if it were a neutral one", "'A school uniform is a badge of pride' is meant to win approval. A neutral definition would state the meaning. "
                "In an argument, treat a persuasive definition as a view to examine, not as a fact."),
        QUIZ("A teacher says: 'In this class, plagiarism means copying anything without naming the source.' This is",
             ["a lexical definition", "a stipulative definition", "a theoretical definition", "a persuasive definition"], 1,
             "The teacher is setting a meaning for use in her class. It is a stipulative definition.",
             hint="Is the teacher reporting a dictionary meaning or setting a rule?",
             feedback=["A lexical definition reports ordinary usage.", "", "No scientific theory is being used.", "The aim is not to influence feelings."]),
        QUIZ("'An odd number is a whole number that is not divisible by two.' The technique is",
             ["ostension", "synonym", "genus and difference", "enumeration"], 2,
             "The genus is 'whole number' and the difference is 'not divisible by two'.",
             hint="Look for a larger class and a special feature.",
             feedback=["Nobody is pointing at anything.", "No other word with the same meaning is given.", "", "No list of members is given."]),
        TIP("Paper 1 often gives a short definition and asks for its kind: lexical, stipulative, precising, theoretical or persuasive. "
            "Paper 2 Section A asks you to define each kind with an example.", title="Exam link"),
        PQ("Explain the difference between a real and a nominal definition with one example each.",
           "A nominal definition explains a word, for example 'Philosophy' from Greek words for love of wisdom. A real definition explains the nature of the thing, for example 'Man is a rational animal'."),
        PQ("Give one example of a stipulative definition from school life and say why it is not true or false.",
           "'In this school, a punctual pupil means one who arrives before 7:30.' It sets a meaning by agreement. It is a decision, so it is neither true nor false."),
        PQ("Name the five kinds of definition by purpose.",
           "Lexical, stipulative, precising, theoretical and persuasive."),
        SUM("A nominal definition explains a word; a real definition explains the nature of a thing, usually by genus and difference.",
            "By purpose, definitions are lexical, stipulative, precising, theoretical or persuasive.",
            "By technique, a definition can use a synonym, examples, pointing, or genus and difference.",
            "Only lexical definitions can be true or false. Treat persuasive definitions with care."),
    ],
))

# ------------------------------------------------------------------ 8. Rules and fallacies of definition
LESSONS.append(lesson(
    module=M_DEFS,
    topic=T_RULES,
    title="Rules and fallacies of definition",
    slug="def-rules-and-fallacies-of-definition",
    minutes=24,
    summary="A good definition states the essential attributes, is not circular, is neither too wide nor too narrow, avoids obscure or figurative language and avoids negatives where a positive will do. Breaking a rule creates a fault.",
    objectives=[
        "State the five rules of a good definition",
        "Name the fault created when each rule is broken",
        "Test whether a definition is too wide, too narrow, or both",
        "Correct a faulty definition",
    ],
    key_concepts=["Essential attributes", "Circular definition", "Too wide", "Too narrow", "Obscure definition", "Figurative definition", "Negative definition"],
    blocks=[
        H("Introduction"),
        T("A shopkeeper in Garoua says: 'A customer is someone who is a customer of my shop.' A student answers: 'That goes round in a circle.' "
          "Another offers: 'A customer is a person with money.' That is too wide: many people with money are not customers."),
        T("Logic gives a short list of rules for a good definition. Copi lists five, which most textbooks follow. Some textbooks add or reword rules. "
          "Learn these five and check your textbook for others."),
        H("The five rules"),
        D("**Rule 1. A definition should state the essential attributes of the thing.** The essential attributes are those without which the thing would not be what it is. "
          "Accidental features (things that could change while the thing stays the same) do not define.", title="Essential attributes"),
        T("Faulty: 'A student is a person who carries a school bag.' Many students do not carry one, and many carriers are not students."),
        D("**Rule 2. A definition should not be circular.** The definiens must not contain the definiendum, or a word that depends on it, or send us round in a circle between two terms. "
          "The fault is called **circular definition**.", title="Not circular"),
        T("Faulty: 'Justice is the quality of being just.' It uses 'just' to explain 'justice'. We learn nothing new."),
        D("**Rule 3. A definition should be neither too wide nor too narrow.** It should apply to all the things the term applies to and to nothing else. "
          "If it applies to some things that are not the term, it is **too wide**. If it leaves out some things that are the term, it is **too narrow**. It can be both.",
          title="Not too wide, not too narrow"),
        IMG("f5l-term-too-wide-too-narrow.svg", alt="Two overlapping circles. Birds on the left and animals that fly on the right. Ostrich and penguin only in birds, bat and bee only in animals that fly, sparrow and eagle in both.",
            caption="Figure 1. 'A bird is an animal that flies' is both too narrow (it leaves out ostriches) and too wide (it lets in bats)."),
        T("Too wide: 'A school is a building.' Hospitals and churches are buildings too. Too narrow: 'A teacher is a person who teaches mathematics.' "
          "It leaves out teachers of other subjects."),
        D("**Rule 4. A definition should not be ambiguous, obscure or figurative.** The words of the definiens must be clearer than the word being defined. "
          "Avoid words with double meanings, hard words and metaphors. The faults are called **obscure** or **figurative** definition.", title="Clear, literal language"),
        T("Obscure: 'A school is an institution for the dissemination of pedagogic instruction.' Harder than the word it explains. "
          "Figurative: 'A teacher is a candle that burns itself to light the way for others.' It is a metaphor. It is a poem, not a definition."),
        D("**Rule 5. A definition should not be negative when it can be positive.** Saying what a thing is not rarely tells us what it is. "
          "The fault is called **negative definition**. A negative definition is fine when the term itself names an absence.", title="Not negative where avoidable"),
        T("Faulty: 'A farmer is not a trader.' Acceptable: 'Blind means without sight.' The term 'blind' itself names a lack."),
        KEY("Rules and faults", "A quick table to learn.", cards=[
            ["Essential attributes", "Fault: states only accidental features."],
            ["Not circular", "Fault: circular definition."],
            ["Not too wide or too narrow", "Faults: too wide; too narrow; or both."],
            ["Clear and literal", "Faults: obscure; ambiguous; figurative."],
            ["Not negative", "Fault: negative definition (where a positive one is possible)."],
        ], note="Other books may list more rules (for example about grammar or context). Learn the list your teacher uses."),
        EX("Worked example 1: find the fault", intro="'A fruit is something sweet to eat.' Is it too wide, too narrow, or both?", steps=[
            S("Test for too wide", text="Sweets, honey and cake are sweet and good to eat, but they are not fruit. The definition lets in too much: too wide."),
            S("Test for too narrow", text="A lemon, an avocado and a tomato are fruit, but they are not sweet. The definition leaves out some fruit: too narrow."),
            S("Answer", text="Both too wide and too narrow."),
        ]),
        EX("Worked example 2: correct a definition", intro="Improve 'A taxi is not a private car.'", steps=[
            S("Find the fault", text="It is negative. It says what a taxi is not. A bus and a bicycle are also 'not a private car'."),
            S("Find the genus", text="A taxi is a kind of motor vehicle."),
            S("Find the difference", text="It carries passengers for a fare, and the passenger chooses the destination."),
            S("Write it", text="A taxi is a motor vehicle that carries passengers to a chosen destination for a fare."),
        ]),
        MISTAKE("Thinking 'too wide' and 'too narrow' are opposites that exclude each other", "A definition can be both at once, as with 'a bird is an animal that flies'. Test both ways."),
        MISTAKE("Calling any use of the same root a circle", "Rule 2 is broken when the definiens depends on the definiendum. 'Justice is being just' is circular. 'A farmer is a person who grows crops' is not: 'grows crops' does not use the word 'farmer'."),
        QUIZ("'A mother is a mother who has a child.' The fault is",
             ["too wide", "circular definition", "figurative definition", "negative definition"], 1,
             "The definiens uses the word being defined, so it sends us round in a circle.",
             hint="Does the definiens contain the term to be defined?",
             feedback=["Width is not the point: the word 'mother' is repeated.", "", "There is no metaphor.", "Nothing is denied."]),
        QUIZ("'A chair is something you can sit on.' This definition is",
             ["too narrow only", "too wide only", "both too wide and too narrow", "perfect"], 1,
             "Benches, rocks and beds can be sat on but are not chairs, so it is too wide. No chair is left out, because every chair can be sat on.",
             hint="Are there things you can sit on that are not chairs? Is there a chair you cannot sit on?",
             feedback=["No chair is left out by 'can be sat on'.", "", "No chair is left out, so it is not too narrow as well.", "It lets in benches and rocks."]),
        TIP("Paper 1 usually gives a faulty definition and asks you to name the fault. In Paper 2 Section A you may be asked to state the rules and correct examples.", title="Exam link"),
        PQ("State the five rules of definition.",
           "1. State the essential attributes. 2. Be not circular. 3. Be neither too wide nor too narrow. 4. Avoid ambiguous, obscure or figurative language. 5. Avoid the negative where a positive can be given."),
        PQ("Name the fault in: 'A doctor is a person who wears a white coat.'",
           "It names an accidental feature, not the essential attributes. It is also both too wide (laboratory workers, chemists) and too narrow (doctors in other clothes)."),
        PQ("When is a negative definition acceptable? Give an example.",
           "When the term itself names an absence. Example: 'Blind means without sight.'"),
        SUM("A good definition states the essential attributes of the thing.",
            "It is not circular, and it is neither too wide nor too narrow (it can be both).",
            "It uses clear, literal words, not obscure or figurative ones.",
            "It is positive wherever possible. A negative definition is fine for a term that names an absence."),
    ],
))

# ------------------------------------------------------------------ 9. Logical division
LESSONS.append(lesson(
    module=M_DEFS,
    topic=T_DIV,
    title="Structure and rules of logical division",
    slug="def-structure-and-rules-of-logical-division",
    minutes=24,
    summary="Logical division separates a class (the whole) into its kinds (the members) using one basis. A good division has one basis, covers the whole, has no overlaps and proceeds step by step. Division differs from partition.",
    objectives=[
        "Define logical division and name its three parts: the whole, the members and the basis",
        "State the rules of logical division",
        "Name the fault when each rule is broken",
        "Distinguish logical division from partition",
    ],
    key_concepts=["Logical division", "Whole (totum)", "Members", "Basis of division", "Cross-division", "Partition"],
    blocks=[
        H("Introduction"),
        T("A school secretary in Kumba has a list of all the pupils and wants to arrange them. She can sort them by class, by age, by sex or by home town. "
          "Each choice gives a different set of groups. But she must choose one way at a time, or her lists will be a muddle."),
        T("Logic names this act. When we separate a class into its kinds, we **divide** it."),
        D("**Logical division** is the act of separating a class (a whole) into the kinds (members) that make it up, according to a chosen basis.", title="Logical division"),
        D("The **whole** (Latin totum) is the class being divided. The **members** (the dividing members) are the kinds it is divided into. The **basis** (the principle, or fundamentum divisionis) is the feature used to divide.",
          title="Whole, members and basis"),
        IMG("f5l-term-division-tree.svg", alt="A tree. Triangles at the top, basis: size of the angles, three members below: acute-angled, right-angled and obtuse-angled.",
            caption="Figure 1. A good division: the whole is triangles, the basis is the angles, the members are three kinds."),
        T("In Figure 1 the whole is 'triangle'. The basis is 'the size of the angles'. The members are acute-angled, right-angled and obtuse-angled triangles. "
          "Every triangle falls in one member, and only one."),
        H("The rules of division"),
        D("**Rule 1. Use one basis only.** At each step, divide by one principle. Mixing bases makes the members overlap. "
          "The fault is called **cross-division**.", title="One basis"),
        D("**Rule 2. The division must be complete (exhaustive).** The members together must make up the whole. Nothing may be left out. "
          "The fault is an **incomplete division**.", title="Exhaustive"),
        D("**Rule 3. The members must be mutually exclusive.** No thing may belong to two members. If the members overlap, the division is faulty.", title="Mutually exclusive"),
        D("**Rule 4. The division must proceed step by step.** The members must be the nearest kinds of the whole. Do not jump over a level. "
          "The fault is **jumping** (division by leaps).", title="No jumping"),
        IMG("f5l-term-division-faults.svg", alt="Two faulty division trees. Students divided into boys, girls and footballers, where members overlap. Plants divided into trees and shrubs, where herbs and others are left out.",
            caption="Figure 2. Two faults: overlapping members (cross-division) and a missing member (not exhaustive)."),
        T("In Figure 2, the first tree mixes two bases: sex (boys, girls) and sport (footballers). A girl who plays football is in two members. "
          "The second tree is not exhaustive: plants such as herbs and grasses are not shown."),
        T("Jumping: 'Animals are divided into lions, birds, reptiles and fish.' Lions are a kind of mammal, so the member 'mammals' has been skipped. "
          "The correct step is 'mammals, birds, reptiles, amphibians, fish', and then divide mammals into lions, and so on."),
        KEY("Dichotomy", "A simple way to be complete and exclusive.", cards=[
            ["What it is", "Dividing into 'A' and 'not-A'. Example: motorised vehicles and non-motorised vehicles."],
            ["Why it works", "Every vehicle is in exactly one member."],
        ], note="Dichotomy is always exhaustive and exclusive, but the 'not-A' member is often too broad to be useful."),
        H("Division and partition"),
        T("Some books separate two things. **Logical division** splits a class into **kinds** (each member is a kind of the whole): 'Vehicles are cars, buses, motorbikes...'. "
          "**Partition** splits a thing into its **parts** (each member is a part of the whole, not a kind): 'A car has an engine, wheels, a body...'. "
          "The test: is each member an X? (division). Or is each member a part of X? (partition)."),
        T("An engine is not a car, so splitting a car into an engine and wheels is a partition. Dividing Cameroon into ten regions is also a partition: a region is a part of Cameroon, not a kind of Cameroon. "
          "Not every book makes this distinction. Check your textbook."),
        EX("Worked example 1: test a division", intro="Test: 'Students are divided into boys, girls and footballers.'", steps=[
            S("Whole and members", text="The whole is 'students'. The members are boys, girls and footballers."),
            S("Test rule 1", text="Boys and girls use sex as the basis. Footballers use sport. That is two bases."),
            S("Test rule 3", text="A girl can be a footballer, so she is in two members. The members overlap."),
            S("Answer", text="Cross-division. Fix: divide by sex (boys, girls) and then divide each by sport if needed."),
        ]),
        EX("Worked example 2: test a division by counting", intro="A class has 40 students: 22 boys and 18 girls. A teacher divides them into boys (22), girls (18) and footballers (12). How many students are counted twice?", steps=[
            S("Add the members", math=r"22 + 18 + 12 = 52", text="The members add up to 52."),
            S("Compare with the whole", text="The class has only 40 students."),
            S("Subtract", math=r"52 - 40 = 12", text="So 12 students are counted twice: the footballers, who are also boys or girls."),
        ]),
        MISTAKE("Confusing 'division' with the fallacy of division", "Logical division is a method of sorting a class. The 'fallacy of division' is a faulty argument that what is true of a whole must be true of its parts. They are different topics."),
        MISTAKE("Dividing by an accidental feature that is not exhaustive", "'People are tall or short' leaves out people of middle height. When in doubt, use a dichotomy or check that every member of the whole fits one group."),
        QUIZ("'Vehicles are divided into cars, buses, motorbikes and fast ones.' The main fault is",
             ["it is not exhaustive", "cross-division", "it is a partition", "it has too few members"], 1,
             "'Fast ones' uses speed as a basis, while the others use the type of vehicle. A fast car is in two members.",
             hint="Are the members chosen using the same principle?",
             feedback=["That is not the main fault here.", "", "A partition would list parts of one vehicle.", "The number of members is not the fault."]),
        QUIZ("Dividing a bicycle into frame, wheels and pedals is",
             ["logical division", "a partition", "cross-division", "a dichotomy"], 1,
             "A wheel is a part of a bicycle, not a kind of bicycle. It is a partition.",
             hint="Is each member a kind of bicycle or a part of one?",
             feedback=["In logical division each member is a kind of the whole.", "", "No overlap or mixed basis is shown.", "A dichotomy would be A and not-A."]),
        TIP("In Paper 1, expect questions like 'The principle used to divide a class is called ...' (the basis) or 'Which rule is broken?'. In Paper 2 you may have to test a division and correct it.", title="Exam link"),
        PQ("Name the three parts of a logical division and give an example.",
           "The whole (for example 'triangles'), the members (acute-angled, right-angled, obtuse-angled) and the basis (the size of the angles)."),
        PQ("State the rules of division and name the fault for each.",
           "One basis (cross-division); exhaustive (incomplete division); mutually exclusive (overlap); step by step (jumping)."),
        PQ("Is 'Cameroon is divided into ten regions' a logical division or a partition? Explain.",
           "It is a partition. Each region is a part of Cameroon, not a kind of Cameroon."),
        SUM("Logical division separates a whole into members using a basis.",
            "The rules: one basis, exhaustive, mutually exclusive, step by step (no jumping).",
            "The faults are cross-division, incomplete division, overlap and jumping.",
            "Logical division splits a class into kinds. Partition splits a thing into parts. Not every book makes this distinction."),
    ],
))
