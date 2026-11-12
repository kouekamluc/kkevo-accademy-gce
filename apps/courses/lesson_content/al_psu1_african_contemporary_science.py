"""A Level Philosophy (0790), Upper Sixth, Modules 1 to 3: African Philosophy, 19th and 20th Century Contemporary Philosophy, Epistemology and Philosophy of Science (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("philosophy", "upper-sixth")

M_AFR = "African Philosophy"
M_CON = "19th & 20th Century Contemporary Philosophy"
M_EPI = "Epistemology & Philosophy of Science"


def ex(title, intro, steps):
    """Model essay plan: question in intro, one step per paragraph."""
    return EX(title, intro=intro, steps=[S(a, text=b) for a, b in steps])


def qz(question, right, wrongs, expl, pos, hint=""):
    """Quick check: `wrongs` = three (text, feedback) pairs; `pos` = index of the correct choice."""
    choices = [w[0] for w in wrongs]
    fb = [w[1] for w in wrongs]
    choices.insert(pos, right)
    fb.insert(pos, "")
    return QUIZ(question, choices, pos, expl, hint=hint, feedback=fb)


LESSONS = []

# ---------------------------------------------------------------------------
# African Philosophy
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_AFR, topic="The debate on African philosophy",
    title="Is there an African philosophy? The great debate",
    slug="psu1-the-debate-on-african-philosophy",
    minutes=22,
    summary="Why some Western thinkers denied that Africans had philosophy, how Africans answered, and the main questions of the debate: what philosophy is, whether it can be communal and oral, and the myth of unanimity.",
    objectives=[
        "Explain why the existence of African philosophy was questioned and in what historical setting",
        "State the main arguments for and against an African philosophy",
        "Explain the four classic criticisms: communal status, oral status, uniqueness and the myth of unanimity",
        "Evaluate the debate with objections and replies",
    ],
    key_concepts=["African philosophy", "Colonial setting", "Orality", "Unanimism", "Pan-Africanism"],
    blocks=[
        H("Introduction"),
        T("In a market in Yaounde an old woman settles a quarrel between two traders. She gives reasons, weighs what is fair, and "
          "refers to what the elders have always taught. Is she doing philosophy? Is the proverb she quotes a philosophical thesis? "
          "Questions like these lie at the heart of what is called **the great debate on African philosophy**.\n\n"
          "The debate is not only about Africa. It forces us to ask what philosophy itself is: a universal activity of critical "
          "reasoning, or a particular tradition that began in Greece and written down in books?"),
        D("The **debate on African philosophy** is the long discussion, in the 20th century, about whether there is a philosophy that "
          "is African, what it consists of, and by what method it should be studied. It is the entry point to every other lesson in "
          "this module.", title="Definition"),
        H("The setting: colonialism and denial"),
        T("The debate began in a colonial setting. Some European writers claimed that African peoples lived by custom and feeling and "
          "had no developed thought. Georg Hegel, in his lectures on the philosophy of history, is often cited by African authors as a "
          "leading example of such denial. Lucien Levy-Bruhl, a French anthropologist, described a supposed 'prelogical' mentality of "
          "'primitive' peoples. Later scholars rejected this claim, and Levy-Bruhl himself revised it late in his life. Check your "
          "textbook for how it is presented."),
        T("A turning point came in 1945, when the Belgian missionary Placide Tempels published *Bantu Philosophy*. He argued that Bantu "
          "peoples have a coherent philosophy of being. The book set the pace of the whole debate: it was admired by some for taking "
          "African thought seriously, and strongly criticised by others (see the lesson on Ethnophilosophy). The Board's 2023 report "
          "notes that this book shifted the focus of the discourse on philosophy in Africa."),
        KEY("Three pressures behind the debate", "Students often forget the historical pressures. Name them in your essays.", cards=[
            ["Colonial denial", "European claims that Africans lacked reason and philosophy, used to justify rule."],
            ["Nationalist and Pan-African movements", "Writers such as W. E. B. Du Bois and Kwame Nkrumah linked the recovery of African dignity to political liberation."],
            ["Decolonisation of knowledge", "After independence, universities asked what an African curriculum and an African thinking should be."],
        ]),
        H("The questions in the debate"),
        T("The debate can be reduced to four questions. First: **what is philosophy?** If philosophy means systematic, critical, reasoned "
          "inquiry by individuals, the answer will differ from the case where it means any worldview of a people. Second: **can "
          "philosophy be oral?** Third: **can philosophy be communal?** Fourth: **must it be unique, different from the rest of "
          "philosophy, to count as African?**"),
        D("**Unanimism** is the claim, criticised by Paulin Hountondji, that all members of a traditional society share one set of "
          "beliefs. The criticism of unanimism is sometimes called the criticism of the **myth of unanimity**.", title="Unanimism"),
        KEY("The four classic criticisms (as listed in the Board's report)", "These are the points a good answer on the debate should reach.", cards=[
            ["Communal status", "Philosophy is thought by individuals who argue. A body of beliefs shared by a whole people looks more like a culture or a worldview."],
            ["Oral status", "Without written texts, thought cannot be checked, debated and improved over time. Critics ask whether oral thought can be systematic."],
            ["Uniqueness", "If African philosophy only repeats what is 'different', it risks exoticism. If it uses universal reason, what makes it African?"],
            ["Myth of unanimity", "Traditional societies also had disagreement and individual thinkers. Treating a whole people as one mind hides this."],
        ]),
        H("Replies and positions"),
        T("Defenders of African philosophy make four replies. First, philosophy exists wherever people reason critically about "
          "knowledge, existence and conduct; Greek philosophy began in speech too (Socrates wrote nothing). Second, written texts are one "
          "form of preservation, not the only one: oral cultures kept proverbs, tales and the reflections of wise individuals. "
          "Third, what makes philosophy African is the problems, the starting points and the experience from which it reasons, not a "
          "different logic. Fourth, individual thinkers did exist in Africa, as Odera Oruka's work on sages was to show."),
        T("Many scholars today say the debate produced **trends** (ethnophilosophy, philosophic sagacity, nationalist-ideological "
          "philosophy, professional philosophy). The Board's report advises approaching the debate through the conditions of its emergence "
          "and through an examination of these trends, and speaking of Africa from within, in the first person."),
        TIP("Pan-Africanism may appear in Paper 1. The ideas of W. E. B. Du Bois and Kwame Nkrumah are both linked to it. Marcus Garvey is also "
            "usually linked to it. Do not confuse them with Paulin Hountondji, who is known for criticising ethnophilosophy."),
        ex("Model essay plan 1", "'There can be no philosophy without writing.' Discuss with reference to African philosophy.", [
            ("Introduction", "Define philosophy as critical, reasoned inquiry. State the problem: is writing necessary for it? Thesis: writing helps, but is not essential."),
            ("The case for the claim", "Texts allow criticism across time and a tradition of replies. Critics of ethnophilosophy argue that without written argument, tradition remains collected beliefs."),
            ("The case against", "Socrates taught orally; Africa had oral specialists who reasoned about ethics and nature. The mark of philosophy is argument, not the medium."),
            ("Evaluation", "Writing helps philosophy to become cumulative; oral thought can be philosophical but must be recorded and argued to be discussed academically. Hence the role of professional philosophers who write."),
            ("Conclusion", "Give a balanced judgement and link to the trends."),
        ]),
        ex("Model essay plan 2", "Explain two criticisms commonly made against the idea of an African philosophy.", [
            ("Criticism 1: the communal status", "Philosophy needs individual argument; a body of shared beliefs is a worldview. Reply: individual sages such as those studied by Oruka reasoned critically."),
            ("Criticism 2: the myth of unanimity", "Not all members of a society think alike; to speak of 'the African' mind hides debate. Reply: debate within traditions can be recovered and studied."),
            ("Link", "Both criticisms push African philosophy toward individual, critical and argued work."),
        ]),
        MISTAKE("Treating the debate as 'Africans against Europeans'", "Many of the strongest critics of ethnophilosophy were African philosophers. The disagreement is also inside Africa."),
        MISTAKE("Narrating history instead of philosophising", "The Board's report says broad questions invite narration. Take a position, give an argument, and then evaluate."),
        qz("What is meant by the 'myth of unanimity'?",
           "The false idea that all members of a traditional society share the same beliefs",
           [("The claim that all African societies speak one language", "The criticism concerns shared belief, not language."),
            ("The claim that philosophers always agree with each other", "It concerns traditional communities, not philosophers."),
            ("The claim that colonial governments were united", "This has nothing to do with the debate on philosophy.")],
           "Unanimism treats a whole people as thinking with one mind. Critics say this hides individual disagreement.", 0,
           hint="Think of the word 'unanimous'."),
        qz("Which book is said to have shifted the focus of the philosophical discussion about Africa after 1945?",
           "Bantu Philosophy by Placide Tempels",
           [("Philosophy of History by Hegel", "Hegel's work is often cited as an example of the denial that the debate answered."),
            ("Consciencism by Kwame Nkrumah", "It was published in 1964, long after the debate began."),
            ("Ujamaa by Julius Nyerere", "It is a political essay, not the book that opened the debate.")],
           "Tempels' book, published in 1945, set the pace for the debate on the foundation and nature of African philosophy.", 2,
           hint="The author was a Belgian missionary."),
        PQ("Explain why the debate on African philosophy is also a debate about the meaning of philosophy.",
           "Whether African philosophy exists depends on what philosophy is. If philosophy means critical, argued, individual inquiry, then a communal and oral body of beliefs may not qualify. "
           "If philosophy means reflection on being, knowledge and conduct in any form, African thought qualifies. So the argument about Africa forces a definition of philosophy. A good answer gives both definitions and shows how each leads to a different verdict."),
        PQ("Give two replies that defenders of African philosophy make to the claim that oral thought cannot be philosophy.",
           "(1) Socrates, a founder of Western philosophy, wrote nothing: the argument, not the medium, makes philosophy. (2) Oral cultures preserved reasoned reflection in proverbs, tales and the thought of wise individuals, which scholars can study and record. "
           "A strong answer also notes that writing helps criticism to accumulate over time."),
        PQ("'African philosophy must be unique to be African.' Evaluate this claim.",
           "For: it must differ from other traditions in problems and starting points, or it is only imitation. Against: philosophy uses universal reason, so what is African is the experience and the questions, not a different logic; demanding uniqueness may exoticise Africans. "
           "Judgement: African philosophy is African by its context and concerns, while its method is open to critical reason everywhere."),
        SUM("The debate on African philosophy began in a colonial setting that denied Africans philosophy, and was reshaped by Tempels in 1945.",
            "It turns on four questions: what philosophy is, and whether it can be oral, communal and unique.",
            "Critics raise the communal status, the oral status, the question of uniqueness and the myth of unanimity.",
            "Defenders reply that argument, not writing, defines philosophy, and that individual African thinkers existed.",
            "In essays take a position, argue, and evaluate; do not just narrate the history."),
    ],
))

LESSONS.append(lesson(
    module=M_AFR, topic="Odera Oruka's four trends",
    title="Odera Oruka's four trends in African philosophy",
    slug="psu1-oruka-four-trends",
    minutes=22,
    summary="Oruka's classification of African philosophy into ethnophilosophy, philosophic sagacity, nationalist-ideological philosophy and professional philosophy, with the folk sage and the philosophic sage.",
    objectives=[
        "Name and define the four trends",
        "Distinguish the folk sage from the philosophic sage",
        "Match thinkers to trends and explain each trend's strength and weakness",
        "Evaluate Oruka's classification",
    ],
    key_concepts=["Ethnophilosophy", "Philosophic sagacity", "Nationalist-ideological philosophy", "Professional philosophy", "Folk sage", "Philosophic sage"],
    blocks=[
        H("Introduction"),
        T("When a debate has many voices, a map helps. Henry Odera Oruka, a Kenyan philosopher, produced the best-known map of African "
          "philosophy in the twentieth century. He sorted the work done into **four trends**. Examiners often ask students to name the "
          "trends, to match a thinker to a trend, or to judge the classification. This lesson gives you all three."),
        IMG("alpsu1-oruka-trends.svg", alt="Four boxes: ethnophilosophy (Tempels, Mbiti), philosophic sagacity (Oruka), nationalist-ideological philosophy (Nkrumah, Senghor, Nyerere), professional philosophy (Towa, Hountondji).",
            caption="Figure 1. Oruka's four trends with the thinkers usually placed in each. Check your textbook for variations."),
        H("The four trends"),
        D("**Ethnophilosophy** presents the collective worldview of a people, found in their myths, proverbs, rituals and language, as their philosophy. "
          "Thinkers usually placed here: Placide Tempels, John Mbiti.", title="Trend 1: ethnophilosophy"),
        D("**Philosophic sagacity** studies individual wise men and women in traditional communities who reason critically about their culture. Oruka "
          "carried out interviews with such sages, especially in Kenya, to show that individual critical thinking exists in oral culture.", title="Trend 2: philosophic sagacity"),
        D("**Nationalist-ideological philosophy** uses philosophy to support liberation, unity and development: it reflects on the political and social "
          "future of Africa. Thinkers usually placed here: Kwame Nkrumah, Leopold Senghor, Julius Nyerere.", title="Trend 3: nationalist-ideological philosophy"),
        D("**Professional philosophy** is philosophy done by trained academic philosophers, in universities, using critical and often written argument, "
          "and open to the world philosophical tradition. Thinkers usually placed here: Marcien Towa, Paulin Hountondji, Fabien Eboussi Boulaga, Ebenezer Njoh-Mouelle.", title="Trend 4: professional philosophy"),
        H("Folk sage and philosophic sage"),
        T("Within the second trend Oruka made a further distinction, which the Board's report treats as examinable. A **folk sage** knows and "
          "repeats the wisdom of the community, and is often admired for exemplary morals. A **philosophic sage** goes beyond this: he or she "
          "questions, tests and improves community wisdom and produces individual, critical thinking. Oruka's purpose was to show that, "
          "although African culture is communal, there are individual African sages who think critically."),
        KEY("Folk sage versus philosophic sage", "The difference is critical reflection.", cards=[
            ["Folk sage", "Carries and teaches community wisdom; exemplary but not necessarily critical."],
            ["Philosophic sage", "Questions community wisdom and gives reasoned, individual views."],
        ]),
        H("Strengths and weaknesses of each trend"),
        T("Ethnophilosophy takes African thought seriously and preserves worldviews, but is accused of unanimism and of confusing culture "
          "with philosophy. Sage philosophy shows individual critical thought, but critics ask who selects the sages and whether the "
          "recorded interviews are shaped by the researcher. Nationalist-ideological philosophy gave direction to liberation, but is "
          "accused of being ideology rather than philosophy, tied to a political project. Professional philosophy offers rigour and criticism, "
          "but is accused of being detached from ordinary African life and too dependent on Western methods."),
        TIP("The Board's report advises evaluating individual philosophers, not groups. When you meet a trend in an essay, name the specific "
            "thinker and the specific claim, and do not say only 'the ethnophilosophers believe'."),
        ex("Model essay plan 1", "Describe and evaluate Oruka's four trends.", [
            ("Introduction", "Oruka sorted African philosophy into four trends. State the question: does the classification help?"),
            ("Describe", "One short paragraph per trend, each with a thinker and a main idea."),
            ("Evaluate", "Useful as a map; but thinkers can belong to more than one trend (Nkrumah and Nyerere were also philosophers in a professional sense; Senghor was a poet and a politician)."),
            ("Evaluation 2", "The classification itself is part of the debate: it was proposed by one participant, and some trends are named by their critics. Check your textbook."),
            ("Conclusion", "Useful but not absolute; a starting point for study."),
        ]),
        ex("Model essay plan 2", "Distinguish the folk sage from the philosophic sage and explain why the distinction matters.", [
            ("Folk sage", "Repeats community wisdom, shows exemplary morals."),
            ("Philosophic sage", "Reflects critically and produces individual thinking."),
            ("Why it matters", "It answers the claim that African thought is only communal: critical individual thinking exists inside oral culture."),
            ("Objection and reply", "Objection: the researcher chooses the sages. Reply: the aim is to show that critical individuals exist, not to say every elder is a philosopher."),
        ]),
        MISTAKE("Placing Oruka in ethnophilosophy", "Oruka is associated with philosophic sagacity and in fact criticised pure ethnophilosophy."),
        MISTAKE("Treating the trends as rigid boxes", "Real thinkers cross the lines. Say 'usually placed in' and give the reason."),
        qz("In Oruka's classification, which trend is concerned with the political emergence and liberation of Africa?",
           "Nationalist-ideological philosophy",
           [("Ethnophilosophy", "It presents the collective worldview of peoples."),
            ("Philosophic sagacity", "It studies critical individual sages."),
            ("Professional philosophy", "It is academic philosophy, though it can address politics.")],
           "Nationalist-ideological philosophy uses thought for liberation, unity and development, with thinkers such as Nkrumah, Senghor and Nyerere.", 3,
           hint="The name of the trend includes a word for liberation movements."),
        qz("Which sage goes beyond community wisdom and produces individual, critical thinking?",
           "The philosophic sage",
           [("The folk sage", "The folk sage embodies communal wisdom and is exemplary in morals."),
            ("The cultural sage", "This is not one of Oruka's two named types."),
            ("The ethnic sage", "This is not one of Oruka's two named types.")],
           "The philosophic sage questions and reasons critically; the folk sage repeats and embodies communal wisdom.", 1,
           hint="Which sage 'philosophises'?"),
        PQ("Name Oruka's four trends and one thinker usually placed in each.",
           "Ethnophilosophy (Tempels or Mbiti); philosophic sagacity (Oruka's own sage interviews); nationalist-ideological philosophy (Nkrumah, Senghor or Nyerere); professional philosophy (Towa or Hountondji). Check your textbook for variations."),
        PQ("Why did Oruka introduce the idea of the philosophic sage?",
           "To answer the charge that African thought is only communal and uncritical. By showing that individuals in traditional communities reason critically about their culture, Oruka tried to show that philosophy exists in oral Africa and is not just shared belief."),
        PQ("Evaluate the claim that nationalist-ideological philosophy is ideology and not philosophy.",
           "For: it serves a political programme and may not question its own assumptions. Against: all philosophy has a context; Nkrumah and Nyerere argue for their views with reasons and respond to objections. "
           "Judgement: it is philosophy to the degree that it argues and can be criticised, ideology to the degree that it only mobilises."),
        SUM("Oruka's four trends are ethnophilosophy, philosophic sagacity, nationalist-ideological philosophy and professional philosophy.",
            "Philosophic sagacity separates the folk sage (carries communal wisdom) from the philosophic sage (thinks critically).",
            "Each trend has strengths and a standard criticism that you should be able to state.",
            "Thinkers can overlap trends: say 'usually placed in'.",
            "Evaluate named thinkers, not whole groups."),
    ],
))

LESSONS.append(lesson(
    module=M_AFR, topic="Ethnophilosophy: Tempels and Mbiti",
    title="Ethnophilosophy: Tempels' vital force and Mbiti's religion and time",
    slug="psu1-ethnophilosophy-tempels-mbiti",
    minutes=24,
    summary="Tempels' theory that being is force, Mbiti's account of African religion, community and time, and the criticisms of ethnophilosophy by African philosophers.",
    objectives=[
        "Explain Tempels' idea of being as force and the hierarchy of vital force",
        "Describe Mbiti's views on religion, community and time (Sasa and Zamani)",
        "Explain why ethnophilosophy has been criticised",
        "Evaluate ethnophilosophy with objections and replies",
    ],
    key_concepts=["Vital force", "Chain of being", "Sasa and Zamani", "Living-dead", "Ethnophilosophy"],
    blocks=[
        H("Introduction"),
        T("Many African families keep ties with ancestors: a libation is poured, a name is given in memory of a grandparent, a "
          "decision is delayed until elders have been consulted. Tempels and Mbiti ask what worldview lies behind such practices. "
          "They are the two best-known writers of the first of Oruka's trends, **ethnophilosophy**. The Board's report gives special "
          "attention to Tempels' vital force; students who treated it as a question about witchcraft missed the point."),
        H("Tempels: being is force"),
        T("Placide Tempels, a Belgian Franciscan missionary who worked among the Luba of the present Democratic Republic of Congo, published "
          "*Bantu Philosophy* in 1945. His central thesis is that, for the Bantu peoples he studied, **being is force**. In "
          "his reading, Western thought defines a being as something that is (static), while the Bantu define a being as "
          "a force or something that has force (dynamic)."),
        D("**Vital force** is, in Tempels' account, the dynamic, life-giving energy that animates every being. All beings are forces in "
          "relationship, and the aim of human life is to preserve and strengthen one's vital force and that of one's community.", title="Vital force"),
        KEY("The hierarchy of forces", "In the account the Board's report summarises, force flows in a hierarchy, and all of nature takes part in one chain of being.", cards=[
            ["God", "The origin of all force."],
            ["Ancestors and spirits", "Intermediaries who hold and pass on force to the living."],
            ["Living humans", "Elders first, then adults, then children; force can be increased or reduced."],
            ["Animals, plants, minerals", "Lower forces, still part of the same dynamic order."],
        ]),
        T("Tempels used the idea to explain Bantu ethics (to do good is to increase the force of the community and oneself) and "
          "social life (the roles of elders, of names and of rites). He wrote with missionaries and colonial administrators in "
          "mind and argued that they should respect Bantu thought when they governed or taught."),
        H("Mbiti: religion, community and time"),
        T("John Mbiti, a Kenyan scholar and theologian, wrote *African Religions and Philosophy* (1969). Two of his claims are famous. First, "
          "Africans are deeply religious: religion pervades every part of life, from birth and farming to politics, so that it "
          "cannot be separated from the rest of culture. Second, community comes before the individual: the individual exists in the "
          "community, which is often summarised in the sentence 'I am because we are, and since we are, therefore I am'."),
        D("In Mbiti's study of the languages of several East African peoples, **Sasa** is the 'micro-time' of the present and recent past "
          "that people experience, and **Zamani** is the 'macro-time' of the deep past into which events and people go. Time is "
          "measured by events (a birth, a harvest) and is directed backwards rather than towards a long future. Mbiti also describes "
          "the **living-dead**: the recently deceased who are remembered by name and still take part in family life.", title="Sasa, Zamani and the living-dead"),
        H("Criticisms of ethnophilosophy"),
        KEY("Four standard objections", "Many are made by African philosophers.", cards=[
            ["Unanimism", "It assumes that a whole people shares a single worldview. Hountondji calls this a myth."],
            ["Culture is not philosophy", "Collecting beliefs, even skilfully, is ethnography; philosophy needs argument and criticism."],
            ["Hidden audience", "Tempels wrote for Europeans. Critics say his book speaks about Africans, and not with them, and that an outsider's system was presented as African thought."],
            ["Overgeneralisation", "Studying a few peoples is used to speak for 'the Africans' or 'the Bantu'. Mbiti's time thesis has been challenged by later scholars: check your textbook."],
        ]),
        T("Defenders of ethnophilosophy reply that Tempels was among the first to take African thought seriously in the colonial era, and that "
          "the worldview of a people is a legitimate object of philosophy, as the Presocratic myths and the Hindu Upanishads are for "
          "others. Mbiti's attempt to draw out the structure of concepts such as time and community has been influential even among "
          "his critics. The dispute then becomes whether ethnophilosophy is a first step or a dead end."),
        TIP("Link your answer to the vital force: God, then ancestors, then humans, then nature. Do not turn the question into a discussion "
            "of witchcraft: witchcraft at most is one way that force can be misused."),
        ex("Model essay plan 1", "Explain Tempels' theory of vital force.", [
            ("Introduction", "Tempels, Bantu Philosophy, 1945: being is force, in contrast to the static Western being."),
            ("Hierarchy", "God as origin, ancestors, humans, rest of nature: one dynamic chain of being."),
            ("Application", "Ethics: increase force. Society: roles of elders, ancestors and rites."),
            ("Evaluation", "Strength: a coherent metaphysics. Weakness: a Belgian missionary's synthesis of many peoples; does it show what the people themselves thought?"),
        ]),
        ex("Model essay plan 2", "'Ethnophilosophy is not philosophy.' Discuss.", [
            ("For", "It describes shared belief and does not argue (Hountondji, Towa). It assumes unanimity."),
            ("Against", "Worldviews contain metaphysics, ethics and a theory of knowledge that can be analysed critically; it opened the debate."),
            ("Judgement", "Ethnophilosophy is useful raw material for philosophy but, unless the analysis is critical, it remains description."),
        ]),
        MISTAKE("Reducing Tempels to witchcraft", "The Board's report says the focus must be on vital force, the force that animates all being. Witchcraft is peripheral."),
        MISTAKE("Saying Mbiti proved that Africans have no idea of the future", "Mbiti's claim about time is a thesis based on some languages. Later scholars dispute it. State it as his thesis, then evaluate."),
        qz("In Tempels' account, which order of the hierarchy of force is correct?",
           "God, ancestors, living humans, the rest of nature",
           [("Ancestors, God, nature, humans", "God is the source of force in this account, so God comes first."),
            ("Humans, ancestors, God, nature", "Humans are not the origin of force."),
            ("Nature, humans, ancestors, God", "This reverses the hierarchy.")],
           "God is the origin of force, which flows down through ancestors to living humans and the rest of nature.", 2,
           hint="Start from the origin of force."),
        qz("What is the main point of Hountondji's criticism of ethnophilosophy?",
           "It assumes that a whole people shares a single philosophy",
           [("It writes in the wrong language", "The issue is not language but unanimity."),
            ("It denies that Africans have religion", "Ethnophilosophy stresses religion."),
            ("It rejects the idea of the community", "The criticism is of treating the community as one mind.")],
           "Hountondji criticises unanimism, the belief that traditional peoples share one collective philosophy.", 1,
           hint="Remember the 'myth of unanimity'."),
        PQ("Explain what Mbiti means by Sasa and Zamani.",
           "Sasa is the present and recent experienced time, the 'now' of people's lives. Zamani is the deep past into which events pass. Time is measured by events and extends mostly backwards. "
           "Evaluation: the thesis is drawn from some East African languages, so critics ask if it applies to all of Africa; check your textbook."),
        PQ("Why do critics say Tempels' book is not African philosophy?",
           "They argue that it was written by a European missionary for European readers, that it presents a single system for many peoples, and that it describes beliefs without the critical argument that makes philosophy. "
           "Defenders reply that it took African thought seriously and opened the field."),
        PQ("Discuss whether the idea of vital force gives a coherent account of ethics.",
           "Coherent: good is whatever increases life and force in the community; bad is whatever diminishes it, which gives a clear criterion. Problems: the criterion may justify anything that benefits the group; it is not clear how conflicts between forces are resolved. "
           "Judgement: it offers a community-centred ethics of life that needs supplementing with an account of rights and justice."),
        SUM("Tempels (1945) argued that, for the Bantu he studied, being is force: a dynamic hierarchy from God through ancestors and humans to nature.",
            "Mbiti (1969) described African religion as pervasive, the community as prior, and time as Sasa and Zamani, with the living-dead.",
            "Critics (Towa, Hountondji and others) charge ethnophilosophy with unanimism, with confusing culture and philosophy, and with overgeneralising.",
            "Defenders see it as an early, valuable attempt to take African thought seriously.",
            "Answer on the vital force itself, not on witchcraft."),
    ],
))

LESSONS.append(lesson(
    module=M_AFR, topic="Nationalist-ideological philosophy",
    title="Nationalist-ideological philosophy: Senghor, Nkrumah and Nyerere",
    slug="psu1-nationalist-ideological-philosophy",
    minutes=23,
    summary="How Negritude, Consciencism and Ujamaa used philosophy for liberation and development, and how critics judge them.",
    objectives=[
        "Explain Senghor's Negritude and the criticisms made against it",
        "Explain Nkrumah's Consciencism and the idea of three segments of African society",
        "Explain Nyerere's Ujamaa and its link to the African family",
        "Judge whether nationalist-ideological writing is philosophy or ideology",
    ],
    key_concepts=["Negritude", "Consciencism", "Ujamaa", "African socialism", "Ideology"],
    blocks=[
        H("Introduction"),
        T("When African countries moved towards independence, leaders did not only ask how to win power. They asked what an independent African "
          "society should be. Some of them were philosophers or poets as well as politicians. The writers studied here belong to Oruka's "
          "third trend, **nationalist-ideological philosophy**. Their philosophy is tied to liberation, unity and development. "
          "This lesson presents each position fairly. Whether one agrees with a leader's politics is not the question; we study the "
          "arguments."),
        H("Senghor and Negritude"),
        T("Leopold Senghor, poet and the first president of Senegal, with Aime Cesaire of Martinique and Leon Damas of Guiana, developed "
          "**Negritude**, a movement of the 1930s onward. It started among black students in Paris who rejected the idea that "
          "assimilation to French culture was the only way forward. Negritude asserts the value of black history, culture and "
          "ways of knowing."),
        D("**Negritude** is the movement and philosophy that affirms the identity, culture and values of black peoples against colonial denial. "
          "In Senghor's version, black culture is described as based on intuitive participation, rhythm and emotion, "
          "while European culture is described as based on analytic reason. Senghor presented the two as complementary and "
          "called for a meeting of cultures.", title="Negritude"),
        T("Critics, especially Marcien Towa, argued that Negritude accepted a European picture of Africans as people of feeling "
          "rather than of reason and made it a virtue. Wole Soyinka's well-known remark that a tiger does not proclaim its "
          "tigritude is usually quoted in this connection; check your textbook for the wording. Defenders reply that Negritude "
          "was a necessary act of self-assertion and that it also drew Africans into conversation with the world."),
        H("Nkrumah and Consciencism"),
        T("Kwame Nkrumah, the first leader of independent Ghana and a leading advocate of Pan-Africanism, wrote *Consciencism* (1964). He "
          "argues that African society has been shaped by three segments: the **traditional** African, the **Islamic** and the "
          "**Euro-Christian**. **Philosophical consciencism** is the map of the intellectual forces that would let African society "
          "digest these three segments and develop them according to its own humanist principles, which he links to egalitarian ideas "
          "of the traditional society."),
        KEY("Consciencism in brief", "Key ideas to be able to state.", cards=[
            ["Three segments", "Traditional, Islamic and Euro-Christian influences exist side by side and must be harmonised."],
            ["Materialism", "Nkrumah defends a philosophical materialism and links it with the egalitarianism he sees in traditional societies."],
            ["Pan-African aim", "Philosophy serves the political and economic unity of Africa."],
        ]),
        T("Critics say Consciencism is more a political programme than a philosophical argument, and question whether the claimed "
          "traditional egalitarianism is historically accurate. Defenders say it is a genuine philosophical reflection on the conditions of "
          "decolonisation."),
        H("Nyerere and Ujamaa"),
        T("Julius Nyerere, the first president of Tanzania, developed **Ujamaa** (a Swahili word often translated as 'familyhood'). In 1962 he "
          "described it as the basis of African socialism. The idea is that traditional African society was built on the "
          "extended family: people shared land and care, and no one was a labourer without a family. Ujamaa sought to "
          "keep this spirit while building a modern state, and was developed in the Arusha Declaration of 1967."),
        D("**Ujamaa** is Nyerere's idea of socialism based on the family community: equality of respect, a duty to work, "
          "and common ownership of the main means of production. It is a view of society, not only a policy.", title="Ujamaa"),
        T("Supporters see Ujamaa as an African form of social solidarity that influenced education and national unity in Tanzania. "
          "Critics argue that some policies carried out in its name, especially the movement of rural people into villages, caused "
          "hardship and low production. Historians continue to debate the results; check your textbook."),
        H("Is this philosophy or ideology?"),
        T("The main philosophical question is whether these writings are **philosophy** (open to criticism and reasoned) or **ideology** (a set of "
          "ideas used to mobilise people). The Board's report notes that critics of this trend say it restricts African thought to the "
          "political world view. A balanced answer reasons that these writers advance arguments, but their arguments serve a political "
          "project, so they should be examined critically like any other."),
        ex("Model essay plan 1", "Explain the main ideas of nationalist-ideological philosophy in Africa.", [
            ("Introduction", "Define the trend: philosophy tied to liberation, unity and development."),
            ("Three thinkers", "Senghor: Negritude; Nkrumah: Consciencism and Pan-Africanism; Nyerere: Ujamaa."),
            ("Common ground", "Defence of African dignity; a search for a path to development that is neither copy nor rejection."),
            ("Evaluation", "A criticism: ideology rather than philosophy; reply: reasoned argument inside a political context."),
        ]),
        ex("Model essay plan 2", "'Negritude accepted the stereotypes of the colonisers.' Discuss.", [
            ("For", "Reason versus emotion contrast risks repeating the colonial image (Towa)."),
            ("Against", "It reversed the value judgement; it was a cultural defence and Senghor called for complementarity."),
            ("Judgement", "A debatable claim: Negritude was useful as a rallying idea but weak as philosophy of reason."),
        ]),
        MISTAKE("Mixing up the three thinkers' key words", "Senghor: Negritude. Nkrumah: Consciencism. Nyerere: Ujamaa. Learn each pair as one unit."),
        MISTAKE("Taking sides in a political quarrel", "Philosophy answers explain and evaluate arguments. Do not praise or condemn a leader or party."),
        qz("Which pair is correctly matched?",
           "Nkrumah and Consciencism",
           [("Nyerere and Negritude", "Nyerere is linked to Ujamaa; Negritude is Senghor's movement."),
            ("Senghor and Ujamaa", "Ujamaa is Nyerere's idea."),
            ("Tempels and Consciencism", "Tempels wrote Bantu Philosophy.")],
           "Consciencism (1964) is the book of Kwame Nkrumah.", 1,
           hint="Recall the key word of each thinker."),
        qz("What does Ujamaa mean in Nyerere's thought?",
           "Familyhood: a socialism built on the extended-family spirit",
           [("Freedom from all government", "Nyerere did not argue for no government."),
            ("The superiority of black culture", "That is closer to some readings of Negritude."),
            ("A return to colonial law", "Ujamaa was meant to build a new society, not restore colonial law.")],
           "Ujamaa, often translated as familyhood, was Nyerere's basis of African socialism.", 3,
           hint="Think of the Swahili word for family."),
        PQ("State what Nkrumah means by the three segments of African society.",
           "The traditional African, the Islamic and the Euro-Christian: three streams of influence in African society. Consciencism aims to harmonise them within a humanist, egalitarian framework."),
        PQ("Explain one criticism of Negritude and one reply.",
           "Criticism (Towa, others): by describing the African as intuitive and the European as rational, Negritude accepted and valued a colonial stereotype. Reply: it reversed the colonial evaluation, was a necessary assertion of dignity, and Senghor presented the two as complementary."),
        PQ("Is Nyerere's Ujamaa best described as philosophy or as policy? Give a reasoned answer.",
           "As philosophy: it offers a view of human relationships (community before property), grounded in African family life. As policy: it was implemented through programmes whose results are debated. "
           "Judgement: the underlying ideas can be studied philosophically, but evaluating the policies requires history and economics as well."),
        SUM("Nationalist-ideological philosophy ties philosophy to African liberation, unity and development.",
            "Senghor: Negritude. Nkrumah: Consciencism and Pan-Africanism. Nyerere: Ujamaa.",
            "Critics ask whether this is ideology and not philosophy; defenders point to its reasoned argument.",
            "Present the thinkers fairly and do not take a party-political side.",
            "Check your textbook for the details of each thinker's works."),
    ],
))

LESSONS.append(lesson(
    module=M_AFR, topic="Professional philosophy",
    title="Professional philosophy: Towa, Hountondji, Eboussi Boulaga and Njoh-Mouelle",
    slug="psu1-professional-philosophy",
    minutes=24,
    summary="The critical, academic trend in African philosophy: the criticism of ethnophilosophy by Towa and Hountondji, the crisis of the Muntu in Eboussi Boulaga, and Njoh-Mouelle's call for transformation.",
    objectives=[
        "Define professional philosophy and state what its supporters demand",
        "Explain Towa's and Hountondji's criticisms of ethnophilosophy",
        "Describe the main ideas of Eboussi Boulaga and Njoh-Mouelle",
        "Evaluate the claim that philosophy in Africa must be critical and written",
    ],
    key_concepts=["Professional philosophy", "Critical discourse", "Unanimism", "Crisis of the Muntu", "Transformation"],
    blocks=[
        H("Introduction"),
        T("Three of the four thinkers in this lesson are from the Francophone world and two of them are from Cameroon. This is "
          "important for you: the Board's report says that Marcien Towa's book on the philosophical problem of present-day Africa helped to set the "
          "foundation of the professional trend in Cameroonian philosophy. Professional philosophers hold that philosophy must be "
          "a critical, argued discourse done by trained thinkers, and not merely a description of what a people believes."),
        D("**Professional philosophy** is African philosophy done as critical, rigorous, usually written work by trained philosophers, in "
          "dialogue with the world tradition. Its proponents say philosophy is defined by argument and criticism, not by the ethnic or "
          "cultural origin of the ideas.", title="Professional philosophy"),
        H("Marcien Towa"),
        T("Marcien Towa, a Cameroonian philosopher, published *Essai sur la problematique philosophique dans l'Afrique actuelle* "
          "(1971). He argues against ethnophilosophy: describing the beliefs of the past, he says, does not give Africa the "
          "critical thinking it needs to face its present. For Towa, philosophy is critical and self-critical, and Africa must "
          "take the ideas of other traditions into its own thinking and master them so that it can think for itself and act in "
          "history. He also criticised Negritude as too dependent on the image the colonisers drew of Africans."),
        H("Paulin Hountondji"),
        T("Paulin Hountondji, from Benin, argued in his book often translated as *African Philosophy: Myth and Reality* (check the "
          "title in your textbook) that ethnophilosophy is not African philosophy but a European project: it was written for Europeans "
          "by Europeans and some Africans, and it assumes **unanimism**. For Hountondji, African philosophy should be defined as the "
          "set of philosophical texts written by Africans, a body of critical discourse that is open to debate. This is "
          "sometimes called a 'geographical' definition, because it is based on who writes, not on a mythical collective thought."),
        KEY("Two critics, one claim", "Towa and Hountondji agree that philosophy must be critical, but they differ in emphasis.", cards=[
            ["Towa", "Philosophy must free Africa from imitation and help it to act; study the world tradition critically to build an own thought."],
            ["Hountondji", "Philosophy is a written discourse, open to criticism; collective worldviews are not philosophy."],
        ]),
        H("Fabien Eboussi Boulaga"),
        T("Fabien Eboussi Boulaga, a Cameroonian philosopher and former Jesuit, wrote *La crise du Muntu* (1977). The Muntu (a Bantu word for "
          "person) is in crisis because colonisation and its ideas broke older certainties. He criticised both the "
          "idealisation of tradition found in some ethnophilosophy and the simple imitation of the West. His works call "
          "for authenticity understood as the freedom of the African to think and decide for himself or herself. He wrote also on "
          "religion and on the political conditions of freedom; check your textbook for the details of his books."),
        H("Ebenezer Njoh-Mouelle"),
        T("Ebenezer Njoh-Mouelle, a Cameroonian philosopher, wrote *De la mediocrite a l'excellence* (1970). He argues that the human "
          "being is a being who must continually transform himself or herself, and that African development begins with a change "
          "of mentality, from mediocrity to excellence. He therefore stresses action, work and the production of the self, "
          "and sees philosophy as an aid to that transformation rather than as a defence of the past."),
        H("Strengths and limits of the professional trend"),
        T("Strengths: rigour; openness to the world's philosophy; an account of philosophy as argument open to correction. "
          "Limits: critics say it can seem a copy of Western academic philosophy and distant from ordinary people's questions; "
          "that a definition by authorship ('whatever Africans write') is too loose; and that written philosophy leaves out the "
          "thinking of oral cultures that Oruka's sages show. Professional philosophers answer that criticism is "
          "universal and that an African can use any tradition's tools."),
        TIP("The Board's report asks for evaluation of individual philosophers, not of groups. In an answer say 'Towa argues that ...' and give "
            "his reason. Name the Cameroonian thinkers: Towa, Eboussi Boulaga and Njoh-Mouelle."),
        ex("Model essay plan 1", "Explain Marcien Towa's criticism of ethnophilosophy.", [
            ("Introduction", "Towa, Essai sur la problematique philosophique dans l'Afrique actuelle (1971)."),
            ("Criticism", "Description of past beliefs is not critical philosophy; it keeps Africa looking backwards."),
            ("Positive view", "Philosophy as critical, self-critical thinking that masters the world's ideas to allow Africa to act in history."),
            ("Evaluation", "Strength: calls for rigour. Weakness: does it neglect the value of oral thought? Reply: it asks that oral thought be studied critically."),
        ]),
        ex("Model essay plan 2", "Compare Hountondji and Njoh-Mouelle.", [
            ("Hountondji", "Philosophy is critical discourse in written form; attacks unanimism."),
            ("Njoh-Mouelle", "Human beings must transform themselves; development begins with a change of mentality."),
            ("Similarity", "Both want critical, forward-looking thought and reject uncritical admiration of the past."),
            ("Difference", "Hountondji defines what counts as philosophy; Njoh-Mouelle describes the tasks of philosophy in development."),
        ]),
        MISTAKE("Calling Hountondji an ethnophilosopher", "He is the main critic of ethnophilosophy."),
        MISTAKE("Dismissing oral wisdom as worthless", "Professional philosophers demand criticism, not the destruction of oral knowledge. Say how oral material can be examined critically."),
        qz("Which Cameroonian philosopher's 1971 essay is cited in the Board's report as setting the bases of the professional trend in Cameroonian philosophy?",
           "Marcien Towa",
           [("Fabien Eboussi Boulaga", "He is a Cameroonian philosopher, but the report names Towa for this."),
            ("Ebenezer Njoh-Mouelle", "He is known for the philosophy of transformation."),
            ("Juleat Fouda", "He was a Cameroonian philosopher but not the one the report links to this point.")],
           "The report says Towa's book builds arguments against ethnophilosophy and sets the basis for the professional trend in Cameroon.", 0,
           hint="Recall the critic of ethnophilosophy."),
        qz("What is Hountondji's central criticism of ethnophilosophy?",
           "It assumes unanimity and replaces critical discourse by a supposed collective philosophy",
           [("It is too critical of tradition", "Hountondji's complaint is the reverse."),
            ("It was written in an African language", "Language is not the issue."),
            ("It is too modern", "The criticism is about uncritical description of the past.")],
           "Hountondji argues ethnophilosophy is based on a myth of unanimity and so is not critical philosophy.", 2,
           hint="Remember the myth of unanimity."),
        PQ("Define professional philosophy.",
           "Professional philosophy is critical, rigorous philosophy by trained philosophers, usually in written form, taking part in the world philosophical conversation. It claims that philosophy is defined by argument and criticism."),
        PQ("Explain the idea of the 'crisis of the Muntu' in Eboussi Boulaga's thought.",
           "The Muntu, the person in Bantu thought, is in crisis after colonisation shook inherited certainties. Eboussi Boulaga warns against both idealising tradition and imitating the West, and calls for authenticity as the free decision of Africans about their own future."),
        PQ("Does an African philosophy have to be written to be critical? Discuss.",
           "Yes: writing allows precise argument, reply and accumulation (Hountondji). No: oral sages can reason critically (Oruka), and writing can be uncritical. Judgement: writing is a powerful tool for criticism but not the only place where it occurs; oral thought can be recorded and examined."),
        SUM("Professional philosophy is critical, argued, usually written philosophy by trained thinkers, open to the world tradition.",
            "Towa and Hountondji criticise ethnophilosophy; Hountondji attacks unanimism.",
            "Eboussi Boulaga writes of the crisis of the Muntu; Njoh-Mouelle of the move from mediocrity to excellence.",
            "Strength: rigour. Limit: distance from oral thought and from ordinary life.",
            "Check your textbook for exact titles and dates."),
    ],
))

# ---------------------------------------------------------------------------
# 19th & 20th Century Contemporary Philosophy
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CON, topic="Hegel",
    title="Hegel: Spirit, dialectic and the movement of history",
    slug="psu1-hegel",
    minutes=23,
    summary="Hegel's absolute idealism: reality as Spirit developing through contradiction, the dialectic and Aufhebung, the master-slave relation and history as the growth of freedom, with the main criticisms.",
    objectives=[
        "Explain Hegel's idealism and the idea of Spirit (Geist)",
        "Explain the dialectic and Aufhebung with an example",
        "Describe the master-slave relation and history as the progress of freedom",
        "Evaluate Hegel with objections (Marx, Kierkegaard, critics of Eurocentrism)",
    ],
    key_concepts=["Spirit (Geist)", "Dialectic", "Aufhebung", "Master-slave dialectic", "Absolute idealism"],
    blocks=[
        H("Introduction"),
        T("Think of a child who grows up. The child is not simply replaced by an adult; the child's life is kept, changed and "
          "carried into the adult. Georg Wilhelm Friedrich Hegel (1770-1831), a German philosopher, thought that all of reality, and "
          "especially human history and thought, grows in this way, through conflict that is overcome and kept at a higher level. "
          "His philosophy is the starting point of the 19th century tradition that Marx, Kierkegaard and others reacted to."),
        D("**Absolute idealism** is Hegel's view that reality is, at bottom, rational and spiritual: **Spirit (Geist)**, the "
          "self-developing mind or reason, comes to know itself through nature, history, art, religion and philosophy.", title="Absolute idealism and Spirit"),
        H("The dialectic"),
        T("For Hegel a concept or a form of life is never complete. It contains a one-sidedness that produces its own opposite. "
          "The two then conflict and are overcome in a richer unity. This movement is the **dialectic**. Textbooks describe it as thesis, antithesis, "
          "synthesis. Hegel himself seldom used these three words; the triad was popularised by later writers, so use it as a teaching summary "
          "and check your textbook."),
        D("**Aufhebung** (often translated as 'sublation') is the German word Hegel uses for the step in which a conflict is both "
          "cancelled, kept and lifted to a higher level. The earlier stages are not thrown away: they are preserved in the later.", title="Aufhebung"),
        KEY("A simple example of dialectical movement", "Any example is a teaching device, not Hegel's text.", cards=[
            ["Thesis", "A society where only family bonds matter: loyalty, but no individual freedom."],
            ["Antithesis", "A market society of free individuals: freedom, but loneliness and rivalry."],
            ["Synthesis", "A state that respects individual rights while keeping a shared life (Hegel's idea of the ethical state)."],
        ]),
        H("The master-slave dialectic"),
        T("In the *Phenomenology of Spirit* (1807) Hegel describes two self-consciousnesses who meet. Each wants to be recognised by the other. "
          "One risks life and becomes the master; the other yields and becomes the servant. But the master depends on the servant's work and "
          "so has a poor, dependent recognition, while the servant, who works on nature and shapes things, gains a sense of own power and "
          "skill. The relation therefore turns round. Hegel's point is that self-consciousness needs **mutual recognition** between free "
          "equals. This passage influenced Marx and later Sartre."),
        H("History as the growth of freedom"),
        T("In his lectures on the philosophy of history Hegel presents world history as the progress of the consciousness of freedom: one "
          "is free in the ancient East, some are free in the Greek and Roman world, and all are free in the modern, Christian-Germanic "
          "world, as he saw it. History, in his view, has reason in it, and individuals and nations serve ends larger than their own, "
          "a thought sometimes called the 'cunning of reason'."),
        TIP("African students must know that Hegel's lectures on history also placed Africa outside 'world history', a view that African and many "
            "other philosophers reject as ignorant and Eurocentric. This is the passage cited in the debate on African philosophy (see that lesson)."),
        H("Objections and replies"),
        KEY("Main criticisms", "A good essay states objections and gives Hegel's likely reply.", cards=[
            ["Marx", "Hegel puts ideas first. Marx says the material conditions of life come first and that Hegel's dialectic 'stood on its head' must be turned over."],
            ["Kierkegaard", "A system that explains everything leaves no place for the single existing individual and for the choice of faith."],
            ["Eurocentrism and determinism", "The account of history ranks peoples and treats a European present as the goal; critics also say it makes history too neat."],
            ["Obscurity", "The vocabulary is very hard. A reply: concepts such as recognition and freedom as social achievements remain powerful."],
        ]),
        T("Defenders reply that Hegel's emphasis on the social and historical character of reason, freedom and the self, which "
          "cannot be separated from a community, remains highly influential. The objection that he is merely idealist "
          "meets the reply that he never denied the material world; he held that its full truth is rational and spiritual."),
        ex("Model essay plan 1", "Explain Hegel's dialectic.", [
            ("Introduction", "Reality and thought develop through contradiction; the dialectic is the logic of this movement."),
            ("Stages", "Thesis, antithesis, synthesis as a teaching summary; Aufhebung: cancel, keep, raise."),
            ("Example", "Family, civil society, state, or master and servant."),
            ("Evaluation", "Strength: explains change and conflict. Weakness: unclear, may force history into a pattern."),
        ]),
        ex("Model essay plan 2", "'Hegel's philosophy of history is Eurocentric.' Discuss.", [
            ("For", "Hegel ranked peoples by their consciousness of freedom and placed Africa outside history."),
            ("Against", "His central claim is that freedom develops in history, an idea that can be used without his ranking."),
            ("Judgement", "The conclusions about Africa are untenable and show how a philosophy can be shaped by its time; the method and the idea of recognition survive."),
        ]),
        MISTAKE("Presenting 'thesis, antithesis, synthesis' as Hegel's own phrase", "It is a later summary; Hegel's own language is of Aufhebung and of the movement of the concept. Say so."),
        MISTAKE("Saying Hegel denied the material world", "He held that reality is spirit-like or rational in structure, not that tables do not exist."),
        qz("What does Aufhebung mean in Hegel's dialectic?",
           "Overcoming a contradiction by cancelling, keeping and raising the earlier stages",
           [("Complete destruction of the earlier stage", "The earlier stage is preserved as well as cancelled."),
            ("Choosing one side of a contradiction and ignoring the other", "Both sides are taken up."),
            ("A return to the starting point", "The movement goes to a higher level.")],
           "Aufhebung is the single German word that means to cancel, to preserve and to lift up.", 0,
           hint="Hegel's word contains three senses at once."),
        qz("In the master-slave relation, why does the master's recognition fail to satisfy him?",
           "It comes from a dependent servant and not from a free equal",
           [("The servant always rebels at once", "The point is not rebellion but the quality of recognition."),
            ("The master fears the law", "Law is not the issue here."),
            ("The servant is richer than the master", "Wealth is not the point.")],
           "Real recognition must come from someone who is free; the servant's recognition is given under constraint.", 3,
           hint="Whose approval counts?"),
        PQ("State two differences between Hegel's and Marx's views of history.",
           "(1) For Hegel, history is the development of Spirit and of ideas; for Marx, history is driven by material production and class conflict. (2) Hegel sees the state as the realisation of freedom; Marx sees the state as an instrument of the ruling class."),
        PQ("What does Hegel mean by saying that history is the progress of the consciousness of freedom?",
           "He means that over time more people come to know that human beings as such are free and embody this in laws and institutions: from one free (ruler), to some free (citizens), to all free. History therefore has direction and meaning."),
        PQ("Evaluate the claim that Hegel's dialectic is only a trick to make history look rational.",
           "For: it can fit any events; later opposites are found after the event. Against: the model describes real patterns of conflict and development in social life; it need not predict. Judgement: it is a helpful interpretation of change but not an exact law."),
        SUM("Hegel holds that reality is rational Spirit that develops through contradiction.",
            "The dialectic moves through opposition to a higher unity; Aufhebung cancels, keeps and raises.",
            "The master-slave passage argues that self-consciousness needs mutual recognition.",
            "History is the progress of the consciousness of freedom, but Hegel's ranking of peoples is rejected today.",
            "Main critics: Marx (matter first), Kierkegaard (the individual) and critics of Eurocentrism."),
    ],
))

LESSONS.append(lesson(
    module=M_CON, topic="Marx",
    title="Marx: historical materialism, class struggle and alienation",
    slug="psu1-marx",
    minutes=24,
    summary="Marx's materialist view of history, the base and superstructure, class struggle, alienation and ideology, and the strongest objections to them.",
    objectives=[
        "Explain historical materialism, the base and the superstructure",
        "Describe class struggle and surplus value in outline",
        "Describe the four forms of alienation in the early writings",
        "Evaluate Marx's claims with objections and replies, without taking a political side",
    ],
    key_concepts=["Historical materialism", "Base and superstructure", "Class struggle", "Alienation", "Ideology"],
    blocks=[
        H("Introduction"),
        T("A farm worker on a large plantation grows crops he will never own, for a wage he cannot negotiate. Karl Marx (1818-1883), a German "
          "thinker who lived mostly in England, asked a philosophical question about such a situation: how do the ways in which people produce "
          "their living shape their ideas, their politics and their sense of being themselves? This lesson studies his answers as philosophy. "
          "We explain and evaluate them. We do not recommend or condemn any political party."),
        H("Historical materialism"),
        D("**Historical materialism** is Marx's theory that the way a society produces its material life (its mode of production) shapes "
          "its social relations, institutions and ideas, and that history changes as conflicts arise inside the mode of production.", title="Historical materialism"),
        T("In his view, a **mode of production** has two parts: the **forces of production** (tools, skills, land, technology) and the "
          "**relations of production** (who owns what, who works for whom). When the forces grow beyond the old relations, "
          "conflict appears and society changes. Marx listed, among others, ancient, feudal and capitalist modes."),
        KEY("Base and superstructure", "Marx's famous picture of a society.", cards=[
            ["Base (economic structure)", "Forces and relations of production: the economy."],
            ["Superstructure", "Law, politics, religion, morality, art and ideas that stand on the base."],
            ["Relationship", "The base conditions the superstructure. How strongly it does so is debated: check your textbook."],
        ]),
        H("Class struggle and surplus value"),
        T("In capitalist society Marx saw two main classes: the **bourgeoisie**, who own the means of production, and the **proletariat**, who must sell "
          "their labour. In his analysis, the worker produces more value than he or she is paid for; the difference, **surplus value**, goes to the owner. "
          "The conflict of interest between the classes is the engine of change. Marx expected the contradictions of capitalism to produce a "
          "revolution leading to a classless society."),
        H("Alienation"),
        T("In his early *Economic and Philosophical Manuscripts* (written in 1844) Marx describes four forms of **alienation** (estrangement) of the worker "
          "under capitalism."),
        KEY("Four forms of alienation", "Learn the four in this order.", cards=[
            ["From the product", "The product of labour belongs to another and stands over the worker as a foreign thing."],
            ["From the activity", "Work is forced and a means to a wage, not a free expression of the self."],
            ["From species-being", "Humans are by nature creative and social producers; wage labour reduces this to survival."],
            ["From other people", "Competition sets workers and owners against each other and against themselves."],
        ]),
        T("The idea is that work, which could be the way humans develop themselves, becomes a loss of self. Hegel's master-slave "
          "passage and his view of work lie behind it."),
        D("**Ideology** in Marx's thought is a set of ideas that present the interests of the ruling class as natural and universal, so "
          "that the arrangement of society appears fair and unchangeable.", title="Ideology"),
        H("Objections and replies"),
        KEY("Main criticisms", "Marx's followers and critics debate each.", cards=[
            ["Economic determinism", "Ideas and politics also shape the economy. Reply: later Marxists accepted a two-way influence; the base is only 'in the last instance' decisive."],
            ["Failed predictions", "Revolution did not come first in the most industrialised countries; workers' conditions improved in many. Reply: capitalism adapted; analysis of exploitation remains valid."],
            ["Human nature", "Is there a creative 'species-being'? Critics say Marx assumes a human nature he cannot prove."],
            ["Political outcomes", "States that claimed Marx's name often became authoritarian. Reply: this is a question of how the ideas were applied, which is itself debated."],
        ]),
        TIP("A strong essay separates three things: Marx's analysis of capitalism, his prediction of revolution, and later political movements that used his name. Judge each separately."),
        ex("Model essay plan 1", "Explain Marx's idea of alienation.", [
            ("Introduction", "Alienation: work under capitalism separates the worker from what he or she should be."),
            ("Four forms", "Product, activity, species-being, other people, one sentence each with an example such as plantation or factory wage work."),
            ("Link", "Alienation prepares the critique of capitalism and the call for a society in which work is free."),
            ("Evaluation", "Strength: describes meaningless work and loss of control. Weakness: assumes a human nature; some workers find meaning in wage work."),
        ]),
        ex("Model essay plan 2", "'The economy determines everything.' Is this Marx's view?", [
            ("Claim", "Base conditions superstructure: law, religion and ideas reflect the interests of the ruling class."),
            ("Qualification", "Marx and Engels allowed the superstructure to influence the base; the economy is decisive in the long run."),
            ("Objection", "Max Weber argued that religious ideas also influenced the rise of capitalism; reply: Marx might call this an interaction."),
            ("Judgement", "A strict determinism is a simplification; Marx's view is better called a strong claim about economic conditions."),
        ]),
        MISTAKE("Confusing Marx with the regimes that used his name", "Judge Marx's arguments on their merits and treat the later history as a separate evidence for or against."),
        MISTAKE("Defining alienation only as 'unhappiness'", "It is a technical idea with four forms, linked to the ownership of the product and to loss of free creative activity."),
        qz("In Marx's picture, what does the 'base' consist of?",
           "The forces and relations of production",
           [("Law, politics and religion", "These belong to the superstructure."),
            ("The ideas of the ruling class", "These are part of the ideology of the superstructure."),
            ("The state alone", "The state is part of the superstructure for Marx.")],
           "The base is the economic structure: forces and relations of production.", 2,
           hint="Which part is 'material'?"),
        qz("Which is NOT one of the four forms of alienation in Marx's 1844 manuscripts?",
           "Alienation from God",
           [("Alienation from the product of labour", "This is the first form."),
            ("Alienation from species-being", "This is the third form."),
            ("Alienation from other people", "This is the fourth form.")],
           "The four are: from the product, from the activity, from species-being and from other people.", 3,
           hint="Marx's list is economic and social."),
        PQ("Distinguish the forces of production from the relations of production.",
           "Forces of production are the productive capacities of a society: tools, technology, skills and resources. Relations of production are the social relations through which production happens: who owns the means of production and who works for whom."),
        PQ("Explain what Marx means by ideology.",
           "Ideology is a body of ideas, typically produced within the ruling class's world, that present the existing social order as natural, just or inevitable, so that the interests of the dominant class seem to be the interests of everyone."),
        PQ("Evaluate the claim that Marx's predictions about capitalism were refuted.",
           "For: revolution did not occur where he expected, and workers' conditions improved in many countries. Against: his analysis of inequality, crises and the power of capital still helps explain features of modern economies, and he offered an analysis as well as a prediction. Judgement: parts of the prediction failed; parts of the analysis remain used."),
        SUM("Historical materialism: the mode of production shapes social life and ideas, and history moves by conflict inside it.",
            "Base (forces and relations of production) conditions the superstructure (law, politics, religion, ideas).",
            "Class struggle and surplus value express exploitation; ideology hides it.",
            "Alienation has four forms: from the product, the activity, species-being and other people.",
            "Evaluate the analysis, the prediction and later movements separately."),
    ],
))

LESSONS.append(lesson(
    module=M_CON, topic="Nietzsche",
    title="Nietzsche: the death of God, will to power and the revaluation of values",
    slug="psu1-nietzsche",
    minutes=23,
    summary="Nietzsche's diagnosis of nihilism after the death of God, master and slave morality, will to power, the overman and eternal recurrence, perspectivism, and the main objections.",
    objectives=[
        "Explain the death of God and nihilism",
        "Distinguish master morality from slave morality",
        "Explain will to power, the overman, eternal recurrence and perspectivism",
        "Evaluate Nietzsche, including common misreadings",
    ],
    key_concepts=["Death of God", "Nihilism", "Master and slave morality", "Will to power", "Overman", "Perspectivism"],
    blocks=[
        H("Introduction"),
        T("Suppose a whole society grew up believing that life has a meaning because a God gave it one, and then slowly stopped believing. "
          "What would replace the meaning? Friedrich Nietzsche (1844-1900), a German philosopher and former professor of classical philology, "
          "thought this was the greatest problem of modern Europe. He wrote in a bold, aphoristic style, and he is easily misread, so "
          "we must be careful."),
        H("The death of God and nihilism"),
        D("The **death of God** is Nietzsche's phrase for the fact that belief in the Christian God no longer supports the values of European culture. "
          "It is a statement about culture, not a boast: he feared what would follow.", title="Death of God"),
        D("**Nihilism** is the condition in which the highest values lose their value and life seems to have no meaning or goal. "
          "Nietzsche thought it would follow if nothing replaced the old foundation.", title="Nihilism"),
        H("Master and slave morality"),
        T("In *On the Genealogy of Morality* (1887) Nietzsche gives a historical account of how moral ideas arose. He distinguishes two "
          "types. **Master morality** is the ethics of the strong: it calls 'good' what is noble, powerful and life-affirming, and 'bad' what is "
          "weak and common. **Slave morality** arises among the oppressed: it calls 'good' what is humble, patient and kind, and 'evil' the "
          "powerful who hurt them. He suggested that Christian morality has roots in slave morality, with a feeling of resentment (**ressentiment**) behind it."),
        KEY("Master versus slave morality", "Nietzsche's historical thesis, to be explained and then criticised.", cards=[
            ["Master morality", "Good = noble, strong, self-affirming. Bad = base, weak."],
            ["Slave morality", "Good = humble, kind, safe. Evil = the powerful and cruel. Driven by ressentiment."],
        ]),
        H("Will to power, overman, eternal recurrence"),
        T("**Will to power** is Nietzsche's name for a basic drive in living things to grow, overcome resistance and shape their world. It is not "
          "only the wish to dominate others; it includes self-overcoming and creativity. The **overman** (Ubermensch) is the figure in "
          "*Thus Spoke Zarathustra* who creates new values and gives meaning to the earth after the death of God. "
          "**Eternal recurrence** is a test: imagine that you must live this same life again, in every detail, an infinite number of times. "
          "Could you say yes to it? Whoever can affirms life fully."),
        H("Perspectivism"),
        T("Nietzsche argues that there is no knowledge from nowhere: every view is held from a perspective shaped by drives and interests. "
          "Truth is knowledge from many perspectives, and the more perspectives we can use, the fuller our understanding. This is "
          "**perspectivism**."),
        H("Objections and replies"),
        KEY("Common objections", "A good essay answers each.", cards=[
            ["Self-refutation", "If every view is only a perspective, so is perspectivism. Reply: Nietzsche need not claim that all views are equal, only that none is perspective-free."],
            ["Elitism", "Master morality seems to despise the weak. Reply: he attacks a certain moral outlook, and his target is the weakness of resentment more than people."],
            ["Misuse", "His ideas were distorted by later political movements, partly through edited writings. Reply: scholars reject these readings; read his texts for their own claims."],
            ["No alternative", "He criticises Christian values but offers no clear guide. Reply: his point is that each person must create values."],
        ]),
        TIP("The overman is not a race or a 'superior people'. Nietzsche's overman is an individual who creates values and overcomes himself. Say so; it is a common error."),
        ex("Model essay plan 1", "Explain Nietzsche's idea of the death of God.", [
            ("Introduction", "A cultural claim: belief in the Christian God no longer supports European values."),
            ("Consequence", "Nihilism: the loss of the highest values and of the meaning they gave."),
            ("Response", "Nietzsche's answer: create new values; the overman; affirm life, test it with eternal recurrence."),
            ("Evaluation", "Strength: a vivid diagnosis of meaning-loss. Weakness: values created by individuals may be arbitrary."),
        ]),
        ex("Model essay plan 2", "'Nietzsche's master morality is a justification of cruelty.' Discuss.", [
            ("Claim", "Master morality praises strength and despises weakness."),
            ("Objection", "It seems to excuse the strong against the weak."),
            ("Reply", "Nietzsche's good is also nobility and self-mastery; he criticises resentment more than he praises domination."),
            ("Judgement", "The text can be read both ways; the passage is a reason to read him carefully and not as a slogan."),
        ]),
        MISTAKE("Reading 'God is dead' as 'there is no God' written triumphantly", "It describes a cultural event, with grave consequences, and is not an announcement for or against belief."),
        MISTAKE("Equating will to power with bullying", "It includes creative self-overcoming as well as domination."),
        qz("What does Nietzsche mean by nihilism?",
           "The collapse of the highest values and of the sense of meaning",
           [("The belief that science is false", "Nihilism is about values and meaning."),
            ("The view that only the state has authority", "That is a political position."),
            ("The wish to destroy society", "Nietzsche diagnoses it; he does not recommend destruction.")],
           "Nihilism is the loss of faith in the highest values so that nothing seems to matter.", 1,
           hint="Think of what happens after the old foundations of value fall."),
        qz("What is the purpose of the thought experiment of eternal recurrence?",
           "To test whether one can affirm one's life completely",
           [("To prove that time is circular in physics", "It is a test of attitude, not a physical claim."),
            ("To prove the soul is immortal", "It is not an argument for the soul."),
            ("To show that history repeats politically", "It is a personal test.")],
           "If you could will your life to recur forever, you affirm it; the test measures life-affirmation.", 0,
           hint="It is a question you ask yourself."),
        PQ("Distinguish master morality from slave morality.",
           "Master morality starts from the noble self and calls good what is strong and life-affirming; its opposite is bad. Slave morality starts from the suffering of the weak: it calls the powerful evil and calls good what is humble and kind, with ressentiment as its source."),
        PQ("Explain Nietzsche's perspectivism and one objection to it.",
           "Perspectivism: all knowing is from a particular perspective, shaped by drives and interests; more perspectives give fuller knowledge. Objection: it refutes itself if it claims to be true for all perspectives. Reply: it states only that no view is perspective-free, not that all are equal."),
        PQ("To what extent does Nietzsche offer a satisfactory answer to nihilism?",
           "For: he calls for creating values and affirming life, which gives a task instead of despair. Against: individual value creation may be arbitrary, and the figure of the overman is vague. Judgement: a powerful diagnosis and a suggestive but incomplete answer."),
        SUM("The death of God is the cultural fact that the Christian foundation of European values has collapsed; nihilism is the danger.",
            "Master morality affirms noble strength; slave morality, born of ressentiment, reverses the values.",
            "Will to power, the overman and eternal recurrence are Nietzsche's answers about creating values and affirming life.",
            "Perspectivism: all knowledge is from a perspective.",
            "Read him carefully: do not equate the overman with a race or domination."),
    ],
))

LESSONS.append(lesson(
    module=M_CON, topic="Freud",
    title="Freud: the unconscious and the structure of the mind",
    slug="psu1-freud",
    minutes=22,
    summary="Freud's theory of the unconscious, id, ego and superego, repression, dreams and drives, why it matters for philosophy of mind and freedom, and the objections to it.",
    objectives=[
        "Explain the unconscious and repression",
        "Describe the id, ego and superego",
        "Explain dream interpretation and the role of drives",
        "Evaluate Freud's theory, including the question whether it is scientific",
    ],
    key_concepts=["Unconscious", "Repression", "Id, ego, superego", "Dream work", "Defence mechanism"],
    blocks=[
        H("Introduction"),
        T("You are sure you chose to be late for an appointment because of traffic. A friend suggests that you did not want to go. "
          "Could he be right, even if you never noticed such a wish? Sigmund Freud (1856-1939), an Austrian doctor and the founder of "
          "psychoanalysis, said yes: much of our mental life is hidden from us. This challenges an old philosophical assumption, found in "
          "Descartes, that the mind is transparent to itself."),
        D("The **unconscious** is the part of the mind that contains wishes, memories and feelings of which a person is not aware, "
          "but that influence thought and behaviour. Freud considered it the larger part of mental life.", title="The unconscious"),
        D("**Repression** is the mental process by which painful or forbidden wishes and memories are pushed out of consciousness. What "
          "is repressed does not disappear: it returns in disguised forms such as slips, dreams and symptoms.", title="Repression"),
        H("The structure of the mind"),
        KEY("Id, ego and superego", "In his later model Freud divides the mind into three agencies.", cards=[
            ["Id", "Instinctual drives and wishes; driven by pleasure; entirely unconscious."],
            ["Ego", "The organising self that deals with reality and balances demands; partly conscious."],
            ["Superego", "Internalised parental and social rules, the source of conscience and guilt; partly unconscious."],
        ]),
        T("The ego is under pressure from three sides: the drives of the id, the demands of the superego and the limits of the "
          "real world. Anxiety arises when it is overwhelmed. To protect itself the ego uses **defence mechanisms** such as repression, denial, "
          "projection (seeing in others what one cannot accept in oneself) and rationalisation (giving a respectable reason for an unworthy motive)."),
        H("Dreams and drives"),
        T("In *The Interpretation of Dreams* (1899) Freud argues that dreams are disguised fulfilments of repressed wishes. The "
          "**manifest content** is what the dreamer remembers; the **latent content** is the hidden wish. The **dream work** (condensation, "
          "displacement, symbolisation) disguises the latent content. Freud also held that drives, especially sexual and later aggressive drives, "
          "are central to development, and described stages of childhood development and the Oedipus complex. Many of these claims are "
          "disputed, so treat them as Freud's theory."),
        H("Philosophical significance"),
        T("Freud's theory affects questions in philosophy: if motives can be unconscious, how free and how responsible are we? Is "
          "self-knowledge possible? Is a person divided? Some philosophers say the theory deepens our understanding of freedom: "
          "we become freer as we understand our hidden motives. Others say it threatens responsibility. Nietzsche had already suggested "
          "that drives lie behind conscious reasoning."),
        H("Objections and replies"),
        KEY("Main criticisms", "A complete answer gives at least two.", cards=[
            ["Not scientific", "Karl Popper argued that psychoanalysis can explain any behaviour, so no behaviour could refute it. Reply: some parts of the theory do make testable claims, and later therapies use testing."],
            ["Weak evidence", "Case studies were few and the therapist may shape what the patient reports. Reply: clinical experience gave insights that later research partly supports."],
            ["Overemphasis on sex", "Critics, including some followers such as Jung and Adler, said sexual drives were over-stressed. Reply: Freud later added a drive of aggression and death."],
            ["Cultural bias", "Developed in 19th-century Vienna; its universality is doubted. Reply: later anthropologists tested some claims in other cultures with mixed results."],
        ]),
        TIP("Link Freud to other topics: Popper's demarcation (Bachelard, Popper and Kuhn lesson), Nietzsche (hidden drives), Sartre (bad faith as an alternative to the unconscious) and freedom and determinism."),
        ex("Model essay plan 1", "Explain Freud's theory of the structure of the mind.", [
            ("Introduction", "The mind is not transparent: the unconscious shapes behaviour."),
            ("Three agencies", "Id (drives), ego (reality), superego (conscience); example of a conflict."),
            ("Defences", "Repression, denial, projection, rationalisation."),
            ("Evaluation", "Insightful but difficult to test; contested in its details."),
        ]),
        ex("Model essay plan 2", "'Freud's theory is not scientific.' Discuss.", [
            ("For", "Popper: unfalsifiable. Any behaviour can be explained after the fact."),
            ("Against", "Some claims are testable (e.g. about memory and repression); the theory led to research."),
            ("Judgement", "Parts of the theory are untestable and parts are testable; its value is partly a philosophical and interpretive one."),
        ]),
        MISTAKE("Saying 'Freud said everything is about sex'", "Freud gave a large role to sexual drives, but later added aggression, and his model has structure (id, ego, superego)."),
        MISTAKE("Treating the unconscious as a second hidden person", "It is a theory of mental processes outside awareness, not a separate being."),
        qz("Which agency of the mind, in Freud's later model, is the source of conscience and guilt?",
           "The superego",
           [("The id", "The id is the source of instinctual drives."),
            ("The ego", "The ego manages reality and conflict."),
            ("The manifest content", "That is a term from dream interpretation.")],
           "The superego contains internalised rules and moral demands.", 2,
           hint="It is formed from the rules of parents and society."),
        qz("What did Karl Popper say about psychoanalysis?",
           "It is not falsifiable because it can explain every possible behaviour",
           [("It is the most testable theory in psychology", "Popper argued the reverse."),
            ("It was disproved by one experiment", "His point was that no experiment could disprove it."),
            ("It is a branch of physics", "Not relevant.")],
           "Popper used psychoanalysis as an example of a theory that is never refuted, which he took as a weakness.", 1,
           hint="Remember falsification."),
        PQ("Explain what Freud means by repression and give an example.",
           "Repression is the pushing of unacceptable wishes or memories out of awareness. Example: a person forgets the name of someone he resents; Freud would say that the name is repressed and appears in a slip or a dream."),
        PQ("Distinguish manifest and latent content in a dream.",
           "Manifest content is the story the dreamer remembers. Latent content is the hidden wish or meaning, which the dream work (condensation, displacement) disguises."),
        PQ("Does the theory of the unconscious make human freedom impossible? Discuss.",
           "Yes: if our motives are hidden, our choices may not be our own. No: understanding unconscious motives increases self-control; therapy aims at greater freedom. Judgement: it limits naive ideas of freedom but supports a richer one based on self-knowledge."),
        SUM("Freud's unconscious is the part of the mind, outside awareness, that influences thought and behaviour.",
            "Id (drives), ego (reality) and superego (conscience) conflict, and the ego uses defence mechanisms.",
            "Dreams are disguised wish fulfilments with manifest and latent content.",
            "Objections: unfalsifiable (Popper), weak evidence, over-emphasis on sex, cultural bias.",
            "Philosophically it questions self-transparency, responsibility and freedom."),
    ],
))

LESSONS.append(lesson(
    module=M_CON, topic="Husserl's phenomenology",
    title="Husserl's phenomenology: back to the things themselves",
    slug="psu1-husserl-phenomenology",
    minutes=22,
    summary="Husserl's method of describing experience as it appears: intentionality, the epoche, the phenomenological and eidetic reductions, transcendental consciousness and the lifeworld, with objections.",
    objectives=[
        "Explain intentionality and the aim of phenomenology",
        "Describe the epoche (bracketing) and the reductions",
        "Explain the lifeworld and the problem of other minds",
        "Evaluate phenomenology, including objections from Heidegger and from scientists",
    ],
    key_concepts=["Phenomenology", "Intentionality", "Epoche", "Reduction", "Essence", "Lifeworld"],
    blocks=[
        H("Introduction"),
        T("Look at a mango on a table. You see it as ripe, yellow, near and edible. You do not first receive colour patches and then add "
          "meaning. Edmund Husserl (1859-1938), a German philosopher and mathematician by training, asked: can we describe how things "
          "appear to consciousness, without first assuming theories about them? His answer started **phenomenology**, a method and a movement "
          "that shaped existentialism."),
        D("**Phenomenology** is the careful study of the structures of experience as they appear to consciousness, with the slogan 'to "
          "the things themselves': return to what is given in experience, before theories and prejudices.", title="Phenomenology"),
        H("Intentionality"),
        D("**Intentionality** is the 'aboutness' of consciousness: every act of consciousness is directed to something. To see is to see something; "
          "to fear is to fear something; to judge is to judge something. The idea comes from Franz Brentano and is central for Husserl.", title="Intentionality"),
        T("Husserl distinguishes the **act** (seeing, remembering, imagining) from the **object as intended** (the mango as seen, the "
          "mango as remembered). Consciousness is therefore not a closed box with ideas inside; it is always already outside itself, "
          "directed towards the world. This answers a worry from Descartes: how can the mind reach the world?"),
        H("The epoche and the reductions"),
        D("The **epoche** (Greek for 'suspension') is the act of **bracketing** or putting out of play our natural belief that the world exists "
          "independently, so as to attend purely to how things appear. It does not deny the world; it suspends judgement about it as a "
          "method.", title="Epoche"),
        KEY("Steps of the method", "Phenomenological description follows a disciplined sequence.", cards=[
            ["1. Epoche", "Suspend assumptions, theories and the natural attitude."],
            ["2. Phenomenological reduction", "Turn to the way things are given in consciousness."],
            ["3. Eidetic reduction", "Vary the example in imagination to find what is essential (the eidos) and what is accidental."],
            ["4. Description", "Describe the essential structures without explaining them by causes."],
        ]),
        EX("Worked example: the essence of a die", intro="Use the eidetic reduction on a die (a cube).", steps=[
            S("Choose an example", text="Imagine a red wooden die."),
            S("Vary it freely", text="Change the colour, the material, the size: it is still a cube-like die."),
            S("Test the shape", text="Change the number of faces to five: it is no longer a cube. Shape is essential; colour is accidental."),
            S("Result", text="The essence of a cube is revealed by what cannot be removed in imagination without destroying the thing."),
        ]),
        H("Transcendental consciousness and the lifeworld"),
        T("In his middle period Husserl described a **transcendental ego**, the source of the meaning of the world, which the reduction reveals. "
          "In his last work (*The Crisis of the European Sciences*) he introduced the **lifeworld** (Lebenswelt): the shared everyday world of "
          "experience that is the ground of all science. Science, he said, forgets that it grows out of this lifeworld and mistakes its "
          "abstract models for reality."),
        T("In the *Cartesian Meditations* he faces the problem of **other minds**: if the world is constituted by my consciousness, how do "
          "other subjects exist for me? His answer is that I recognise others through empathy, as beings like me, so the world is "
          "**intersubjective**. Many readers find the answer incomplete."),
        H("Objections and replies"),
        KEY("Main criticisms", "A good essay uses at least two.", cards=[
            ["Heidegger", "We are always already in the world with practical concerns; a detached bracketing is impossible. Reply: the method is a discipline, not a claim to be neutral forever."],
            ["Idealism and solipsism", "The transcendental ego risks locking us inside consciousness. Reply: intentionality is always about the world, and the intersubjective turn addresses it."],
            ["Science", "Cognitive scientists say experience must be explained by brain processes. Reply: phenomenology describes experience first and cannot be replaced by explanations that must start from it."],
            ["Introspective method", "Descriptions differ from person to person. Reply: the eidetic method tests descriptions by imaginative variation, and results can be discussed."],
        ]),
        ex("Model essay plan 1", "Explain Husserl's method of phenomenological reduction.", [
            ("Introduction", "Aim: describe experience as it appears, with no presuppositions; slogan: to the things themselves."),
            ("Epoche", "Bracket the natural attitude and assumptions."),
            ("Reductions", "Phenomenological reduction (to what is given) and eidetic reduction (to the essence by free variation)."),
            ("Evaluation", "Strength: careful description. Weakness: can we really suspend all assumptions? (Heidegger)."),
        ]),
        ex("Model essay plan 2", "Why did Husserl think science needs phenomenology?", [
            ("Claim", "Science rests on the lifeworld of ordinary experience."),
            ("Problem", "Science forgets this foundation, treating mathematical models as the only reality."),
            ("Remedy", "Phenomenology returns to experience to ground the meaning of science."),
            ("Objection and reply", "Objection: science corrects experience. Reply: it corrects it by using experience as evidence."),
        ]),
        MISTAKE("Saying the epoche denies the existence of the world", "It suspends the belief in order to study how things appear; it is a method, not scepticism."),
        MISTAKE("Using 'phenomenology' to mean any description of events", "Husserl's method is specific: epoche, reductions and description of essences."),
        qz("What does intentionality mean in Husserl's phenomenology?",
           "Consciousness is always directed at an object",
           [("People always act with a purpose", "That is the everyday meaning of 'intention'."),
            ("The mind creates all physical objects", "Intentionality is about directedness, not creation of matter."),
            ("Knowledge depends on moral intentions", "Not what the term means.")],
           "Every conscious act is of or about something.", 1,
           hint="It is about 'aboutness'."),
        qz("What is the purpose of the epoche?",
           "To suspend assumptions about the world so that its appearing can be described",
           [("To prove that the world does not exist", "It is not a denial."),
            ("To measure brain activity", "It is a philosophical method, not a laboratory measure."),
            ("To define the rules of logic", "That is a different task.")],
           "The epoche brackets the natural attitude so that experience can be studied as it is given.", 0,
           hint="Think of putting something in brackets."),
        PQ("Describe the eidetic reduction with an example.",
           "The eidetic reduction seeks the essence (eidos) of a thing by imagining it varied freely: whatever can be changed without the thing ceasing to be what it is is accidental; what cannot be changed is essential. Example: changing the colour of a cube leaves it a cube; changing its faces does not."),
        PQ("What is the lifeworld, and why does Husserl think it is important?",
           "The lifeworld is the shared, pre-theoretical world of everyday experience. It is important because science grows out of it and depends on it; forgetting this leads to the 'crisis' of treating abstract models as the only reality."),
        PQ("Evaluate Heidegger's criticism that Husserl's method is too detached.",
           "Heidegger says that human beings are first involved practically in the world, so a neutral, detached viewing is already a special attitude. Husserl's defenders say that bracketing is a method to describe even practical involvement. Judgement: the objection shows limits of detachment but does not remove the value of careful description."),
        SUM("Phenomenology studies experience as it appears, 'to the things themselves'.",
            "Intentionality: consciousness is always of something.",
            "Epoche brackets the natural attitude; the reductions lead to essences by free variation.",
            "The lifeworld is the ground of science; others are known by empathy.",
            "Objections: Heidegger (always in the world), solipsism, and scientific explanation."),
    ],
))

LESSONS.append(lesson(
    module=M_CON, topic="Existentialism",
    title="Existentialism: Kierkegaard, Heidegger and Sartre",
    slug="psu1-existentialism",
    minutes=24,
    summary="The existentialist emphasis on individual existence, choice and responsibility in Kierkegaard, Heidegger and Sartre, with anxiety, authenticity, bad faith and the main objections.",
    objectives=[
        "Explain what unites existentialist thinkers",
        "Describe Kierkegaard's individual, anxiety and leap of faith",
        "Describe Heidegger's Dasein, being-towards-death and authenticity",
        "Explain Sartre's 'existence precedes essence', freedom, bad faith and responsibility, and evaluate them",
    ],
    key_concepts=["Existence precedes essence", "Anxiety", "Authenticity", "Dasein", "Bad faith"],
    blocks=[
        H("Introduction"),
        T("A student must choose a course of study. Family expects one thing, a teacher another, friends something else. Whatever he chooses, "
          "he alone must live with the choice. Existentialism puts this experience at the centre of philosophy: the single, existing "
          "person who must decide how to live without a guaranteed answer. The thinkers in this lesson are very different. Kierkegaard was "
          "a Christian, Sartre an atheist, and Heidegger disliked the label 'existentialist'. Together they ask what it means to exist."),
        KEY("Themes shared by many existentialists", "Use as an introduction, then name the differences.", cards=[
            ["Existence and the individual", "Philosophy starts from the concrete individual, not from abstract systems."],
            ["Freedom and responsibility", "We must choose and cannot hand over responsibility."],
            ["Anxiety and absurdity", "The lack of fixed meaning produces anxiety and, for some, a sense of the absurd."],
            ["Authenticity", "To live one's own life honestly and not as a crowd or a role dictates."],
        ]),
        H("Kierkegaard"),
        T("Soren Kierkegaard (1813-1855), a Danish thinker, reacted against Hegel's system. A system explains everything, he said, but "
          "cannot tell me how to live. He stressed **subjective truth**: some truths, such as how to live and what to believe, must "
          "be taken up with personal commitment. He described **anxiety** (or dread) as the dizziness of freedom when one faces possibilities, "
          "and described three **stages** of life: the aesthetic (pleasure), the ethical (duty) and the religious (faith). In the "
          "religious stage the individual makes a **leap of faith** that cannot be proved by reason."),
        H("Heidegger"),
        T("Martin Heidegger (1889-1976), a German philosopher and student of Husserl, asks in *Being and Time* (1927) what it means to be. "
          "He starts from **Dasein** (German for 'being-there'), the human way of being, which is always in a world, concerned with "
          "things and with others, and aware that it will die. He argues that most of the time we live as 'they' (das Man) do, following "
          "the public way of being. Facing one's own death, **being-towards-death**, can free us to take over our existence as our own: "
          "this is **authenticity**."),
        T("Heidegger refused to be called an existentialist, and his political involvement with the Nazi party in 1933 is a serious "
          "and much discussed matter in the evaluation of his person. Philosophers disagree about how it relates to his work."),
        H("Sartre"),
        T("Jean-Paul Sartre (1905-1980), a French philosopher and writer, developed atheistic existentialism in *Being and Nothingness* (1943) "
          "and the lecture *Existentialism Is a Humanism* (1946). His central statement is that **existence precedes essence**."),
        D("**Existence precedes essence** means that a human being first exists, and then defines what he or she is through choices and actions. "
          "A paper knife has an essence (a purpose) before it exists, because a maker designed it. If there is no God who designed us, "
          "no fixed human nature gives us a purpose in advance.", title="Existence precedes essence"),
        D("**Bad faith** (mauvaise foi) is self-deception in which a person denies his or her freedom, for example by saying "
          "'I had no choice, that is just how I am' or by acting as if only a role (waiter, student) defined him or her. Bad faith "
          "treats a person as a thing.", title="Bad faith"),
        T("Because we are condemned to be free, we are responsible for what we choose and, in choosing, we 'choose for all humanity' by "
          "implying a model of what a person should be. Sartre also describes the **look** of the other, who makes me an object, "
          "which leads to conflict in relations with others. In his later work he tried to unite existentialism and Marxism."),
        H("Objections and replies"),
        KEY("Main criticisms", "Use at least two with replies.", cards=[
            ["Too much freedom", "People are strongly shaped by circumstances. Reply: Sartre admits situations but says we still decide what they mean."],
            ["Subjectivism", "If I create my values, any choice is as good as another. Reply: Sartre argues that choices imply universal responsibility, and that bad faith is a failure."],
            ["Individualism", "It neglects community. Reply: later Sartre and others such as Heidegger stress being-with-others."],
            ["Pessimism", "It is gloomy. Reply: it calls for action, and Sartre called it a doctrine of optimism of action."],
        ]),
        TIP("Link existentialism with Nietzsche (creating values), Husserl (the method), Hegel (the individual versus the system) and freedom and determinism."),
        ex("Model essay plan 1", "Explain Sartre's claim that existence precedes essence.", [
            ("Introduction", "Existentialism begins from existence; Sartre: atheistic version."),
            ("The paper knife", "Objects have a purpose before they exist; humans do not."),
            ("Consequences", "Freedom, responsibility, anxiety and rejection of fixed human nature as an excuse."),
            ("Evaluation", "Strength: stresses responsibility. Weakness: underestimates the effect of conditions."),
        ]),
        ex("Model essay plan 2", "Compare Kierkegaard and Sartre.", [
            ("Similarity", "Both start from the individual's choice, anxiety and responsibility, and both oppose abstract systems."),
            ("Difference", "Kierkegaard ends in faith in God; Sartre rejects God and stresses a freedom that creates its own values."),
            ("Judgement", "They share a method of describing existence but differ about whether the leap ends in God or in the human project."),
        ]),
        MISTAKE("Calling all existentialists atheists", "Kierkegaard was a Christian thinker; Sartre was an atheist. Heidegger refused the label."),
        MISTAKE("Reading 'condemned to be free' as 'free to do anything without consequences'", "For Sartre freedom brings full responsibility."),
        qz("Which thinker is associated with the 'leap of faith'?",
           "Kierkegaard",
           [("Sartre", "Sartre is the philosopher of bad faith and existence preceding essence."),
            ("Husserl", "Husserl is the founder of phenomenology."),
            ("Hegel", "Hegel built a system that Kierkegaard criticised.")],
           "Kierkegaard held that the move to religious faith cannot be proved by reason and is a leap.", 3,
           hint="He was Danish, and a Christian."),
        qz("What does Sartre mean by 'bad faith'?",
           "Self-deception that denies one's freedom and responsibility",
           [("Lack of religious belief", "Bad faith is about self-deception."),
            ("Dishonesty towards others only", "It is a lie to oneself."),
            ("Anxiety about death", "That is closer to Heidegger's themes.")],
           "In bad faith a person pretends he or she has no choice or is merely a role.", 1,
           hint="It is a lie told to oneself."),
        PQ("Explain Heidegger's idea of authenticity.",
           "Authenticity is to take over one's existence as one's own instead of living as 'they' do. Facing the certainty of death shows life as finite and one's own, which frees one from mere conformity. Inauthenticity is drifting with the crowd."),
        PQ("Why does Sartre say we are 'condemned to be free'?",
           "We did not choose to be free: there is no God or human nature to give us a ready-made purpose, so we must choose and are responsible for our choices. Even refusing to choose is a choice."),
        PQ("Is Sartre's picture of freedom realistic? Discuss.",
           "Yes: in the end we decide how to respond to circumstances; blaming one's character is an excuse. No: social, economic and psychological conditions limit real choice. Judgement: Sartre is right that responsibility remains, but he underplays how situation limits the options available."),
        SUM("Existentialists start from individual existence, freedom, anxiety and authenticity.",
            "Kierkegaard: subjective truth, anxiety, three stages and the leap of faith.",
            "Heidegger: Dasein, being-towards-death and authenticity (he rejected the label).",
            "Sartre: existence precedes essence, radical freedom, bad faith and responsibility.",
            "Objections: too much freedom, subjectivism, individualism."),
    ],
))

# ---------------------------------------------------------------------------
# Epistemology & Philosophy of Science
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_EPI, topic="Knowledge, truth and justification",
    title="Knowledge, truth and justification: the analysis of knowing",
    slug="psu1-knowledge-truth-justification",
    minutes=24,
    summary="Types of knowledge, the justified true belief analysis, Gettier's challenge and replies, foundationalism and coherentism, and the correspondence, coherence and pragmatic theories of truth.",
    objectives=[
        "Distinguish propositional knowledge, know-how and acquaintance",
        "Explain the justified true belief (JTB) analysis and Gettier's counterexamples",
        "Compare foundationalism and coherentism, internalism and externalism",
        "Compare the correspondence, coherence and pragmatic theories of truth",
    ],
    key_concepts=["Propositional knowledge", "Justified true belief", "Gettier problem", "Foundationalism", "Coherentism", "Theories of truth"],
    blocks=[
        H("Introduction"),
        T("A student says, 'I know the result is on the board.' Does he know it, or does he only believe it? Epistemology asks what knowledge is, "
          "how we can have it and where its limits lie. You met rationalism and empiricism in the Lower Sixth. This lesson looks at the "
          "analysis of knowledge itself, and at truth."),
        H("Kinds of knowledge"),
        KEY("Three uses of 'know'", "Epistemologists mostly study the first.", cards=[
            ["Propositional knowledge (knowing that)", "I know that Yaounde is the capital of Cameroon. It is true or false."],
            ["Know-how (knowing how)", "I know how to ride a bicycle or to cook ndole: a skill."],
            ["Acquaintance (knowing a person or place)", "I know my cousin or I know Douala."],
        ]),
        H("The JTB analysis"),
        D("The **justified true belief (JTB) analysis**, traced to Plato's *Theaetetus*, says that a person S knows a proposition p if and only if (1) p is true, "
          "(2) S believes p, and (3) S is justified in believing p.", title="JTB analysis"),
        T("Each condition does work. If p is false, S cannot know it, only think so. If S does not believe p, S does not know it. And if S "
          "believes a true proposition by luck, such as guessing the winning number, S does not know it; justification is needed."),
        H("Gettier's challenge"),
        T("In 1963 Edmund Gettier published a short article with cases in which a person has a justified true belief that "
          "seems not to be knowledge. The idea of such cases is older: Bertrand Russell's stopped clock is a simple version."),
        EX("Worked example: the stopped clock", intro="Amina looks at the clock in the school hall and reads 10:00. It is in fact 10:00. But the clock stopped exactly 24 hours earlier.", steps=[
            S("Is her belief true?", text="Yes: it is 10:00."),
            S("Does she believe it?", text="Yes, she reads the clock."),
            S("Is she justified?", text="Yes: a working clock is a normal good reason, and she has no sign of a fault."),
            S("Does she know?", text="Most people say no. The clock gives the right time by luck."),
            S("Conclusion", text="She has justified true belief without knowledge, so JTB is not sufficient for knowledge."),
        ]),
        T("Replies: some add a fourth condition, for instance that the justification must not depend on any false belief (here, "
          "'the clock is working'). Others say knowledge needs a causal link between the fact and the belief, or that the belief must come "
          "from a **reliable** process (**reliabilism**), or that knowledge is a basic state that cannot be analysed. No reply has "
          "won universal agreement."),
        H("The structure of justification"),
        KEY("Foundationalism and coherentism", "Two pictures of how justified beliefs fit together.", cards=[
            ["Foundationalism", "Some beliefs are basic (for example immediate sense experience or self-evident truths) and the rest are justified by resting on them. Problem: what justifies the foundations?"],
            ["Coherentism", "A belief is justified by fitting with a large coherent set of beliefs, like planks of a raft. Problem: a coherent story could still be false."],
        ]),
        T("A related dispute: **internalism** says that justification depends on what the believer can reflect on and access; **externalism** says it may depend on facts "
          "outside the believer's view, such as whether the process that formed the belief is reliable."),
        H("Theories of truth"),
        KEY("Three classic theories", "Truth is one of the hardest concepts.", cards=[
            ["Correspondence", "A proposition is true when it corresponds to the facts. 'It is raining' is true if it is raining. Problem: what is the relation of corresponding, and how to check it?"],
            ["Coherence", "A proposition is true when it coheres with a system of beliefs. Strong in mathematics; problem: two coherent systems can conflict."],
            ["Pragmatic", "A proposition is true when it works in practice (William James): a belief is true if it is useful in guiding us. Problem: false beliefs can be useful."],
        ]),
        TIP("Do not say the theories of truth are the same as theories of justification. Justification asks when we are entitled to believe; truth asks what makes a belief correct."),
        ex("Model essay plan 1", "Is justified true belief sufficient for knowledge?", [
            ("Introduction", "State the JTB analysis and its history."),
            ("Case for", "Each condition is plausible, and ordinary cases fit."),
            ("Gettier cases", "Stopped clock: justified true belief by luck."),
            ("Replies", "No false lemmas; causal or reliabilist conditions; assess each."),
            ("Judgement", "JTB is necessary but not sufficient; no fix is accepted by all."),
        ]),
        ex("Model essay plan 2", "Compare the correspondence and coherence theories of truth.", [
            ("Correspondence", "Truth is agreement with facts; fits common sense and science."),
            ("Coherence", "Truth is fit within a system; fits mathematics and abstract thought."),
            ("Objection to each", "Correspondence: how to compare beliefs with facts? Coherence: coherent fictions."),
            ("Judgement", "Correspondence is the best account of what truth means; coherence is useful as a test of beliefs."),
        ]),
        MISTAKE("Saying Gettier showed that JTB is false", "He showed that justified true belief is not enough (not sufficient); it may still be necessary."),
        MISTAKE("Confusing belief with knowledge", "A person may believe falsely; knowledge needs truth and justification as well."),
        qz("What do Gettier-type cases show about the JTB analysis?",
           "That justified true belief can exist without knowledge",
           [("That knowledge does not need truth", "Gettier cases keep truth as a condition."),
            ("That belief is not necessary for knowledge", "Belief is untouched."),
            ("That justification is impossible", "Gettier did not attack the possibility of justification.")],
           "In Gettier cases the three JTB conditions are satisfied and yet it looks like luck, not knowledge.", 0,
           hint="Is JTB sufficient?"),
        qz("According to foundationalism, how are justified beliefs structured?",
           "Some basic beliefs support the others",
           [("Every belief supports every other in a circle", "That is coherentism."),
            ("No belief needs justification", "Foundationalism requires justification, with basic beliefs as the base."),
            ("Beliefs are justified by authority alone", "That is not the foundationalist claim.")],
           "Foundationalism: a structure like a building resting on basic beliefs.", 2,
           hint="Think of foundations."),
        PQ("State the three conditions of the JTB analysis.",
           "(1) The proposition is true; (2) the person believes it; (3) the person is justified in believing it."),
        PQ("Give a Gettier-style case and explain why it is a problem.",
           "A person reads a stopped clock that happens to show the right time: his belief about the time is true and justified but accidental, so it does not look like knowledge. It shows that justification plus truth plus belief can still be luck."),
        PQ("Evaluate the pragmatic theory of truth.",
           "Strength: ties truth to practice and the success of science. Weakness: false beliefs may be useful (a comforting falsehood), and a true belief may be useless. Judgement: usefulness is a sign of truth in many cases, but it cannot be the meaning of truth."),
        SUM("Epistemology studies knowledge: knowing that, know-how and acquaintance.",
            "JTB analysis: true, believed, justified; Gettier cases show it is not sufficient.",
            "Replies include no false lemmas, causal links and reliabilism.",
            "Foundationalism and coherentism disagree on how justification is structured.",
            "Truth: correspondence, coherence, pragmatic; each has strengths and objections."),
    ],
))

LESSONS.append(lesson(
    module=M_EPI, topic="The scientific method and induction",
    title="The scientific method and the problem of induction",
    slug="psu1-scientific-method-and-induction",
    minutes=24,
    summary="Steps of the scientific method, induction and deduction, Hume's problem of induction and the main replies, and why valid and invalid argument forms matter for testing hypotheses.",
    objectives=[
        "Describe the steps of the scientific method and the roles of induction and deduction",
        "Explain Hume's problem of induction",
        "Evaluate the main replies to the problem",
        "Use valid and invalid argument forms in testing a hypothesis",
    ],
    key_concepts=["Induction", "Deduction", "Hypothetico-deductive method", "Problem of induction", "Uniformity of nature"],
    blocks=[
        H("Introduction"),
        T("A farmer in the West Region has seen the sun rise every morning of her life. She believes it will rise tomorrow. A health worker has "
          "seen a drug cure malaria in thousands of patients and believes it will cure the next patient. In both cases we move from "
          "past experience to a claim about the future. Is this move rational? This lesson asks how science works and why the "
          "question is hard."),
        H("Steps of the scientific method"),
        KEY("A common outline", "Not every science follows the steps in order.", cards=[
            ["1. Observation", "Notice facts or a puzzle."],
            ["2. Hypothesis", "Propose an explanation."],
            ["3. Prediction", "Deduce what should happen if the hypothesis is true."],
            ["4. Test", "Experiment or observe to see whether the prediction holds."],
            ["5. Revision", "Keep, change or reject the hypothesis; repeat."],
        ]),
        D("**Induction** is reasoning from particular observations to a general claim or to a claim about unobserved cases: 'every swan I have seen is white, so all swans are white'. "
          "The conclusion goes beyond the premises, so it is probable at best, not certain.", title="Induction"),
        D("**Deduction** is reasoning in which the conclusion follows necessarily from the premises: if the premises are true, the conclusion must be true.", title="Deduction"),
        T("Francis Bacon (1561-1626) argued for gathering many observations and reasoning upwards from them, the **inductive method**. "
          "Later thinkers described the **hypothetico-deductive method**: a hypothesis is proposed (by any source), predictions are deduced "
          "from it, and the predictions are tested."),
        H("Hume's problem of induction"),
        T("David Hume (1711-1776) asked what justifies the belief that the future will resemble the past. His argument runs in four steps."),
        EX("Hume's argument in steps", intro="Why can we not justify induction?", steps=[
            S("The claim needed", text="To trust induction we need the principle that nature is uniform: unobserved cases will resemble observed ones."),
            S("A priori?", text="We cannot prove it by pure reason, since the opposite (the sun not rising) is not a contradiction."),
            S("By experience?", text="We could appeal to past success of induction. But that argues from the past to the future, which is induction itself."),
            S("Conclusion", text="Induction cannot be justified without circular reasoning. We follow it from habit or custom, as Hume put it."),
        ]),
        H("Replies to Hume"),
        KEY("Main replies and their problems", "A strong essay evaluates these.", cards=[
            ["Pragmatic reply", "Induction is the best method we have; if any method works, induction will. Problem: it does not show that induction is likely to work."],
            ["Probabilistic reply", "Evidence makes conclusions more probable. Problem: the justification for using probability seems also to rest on a pattern holding."],
            ["Popper's reply", "Science does not use induction; it conjectures and tries to refute (see the next lesson). Problem: we still rely on past tests when we use a theory to predict."],
            ["Ordinary-language reply", "To call a belief 'rational' just means it follows inductive standards, so asking for justification of induction is confused. Problem: it looks like avoiding the question."],
        ]),
        T("Nelson Goodman added a 'new riddle of induction': define 'grue' as 'green if observed before a fixed future date and blue "
          "afterwards'. Every emerald observed so far is both green and grue. So the evidence supports both predictions, though we prefer one. Which "
          "properties may be projected into the future is not settled by evidence alone."),
        H("Argument forms used to test hypotheses"),
        T("Hypothesis testing uses deductive forms. If hypothesis H predicts observation O, then: if O fails, H is refuted (**modus tollens**, valid). "
          "If O succeeds, H is not proved (**affirming the consequent**, invalid), because another hypothesis might also predict O."),
        CODE("Valid:    If H then O.  Not O.  Therefore not H.   (modus tollens)\n"
             "Invalid:  If H then O.  O.      Therefore H.       (affirming the consequent)",
             "text", title="Testing a hypothesis"),
        TIP("This asymmetry (a failed prediction can refute; a successful one cannot prove) is the key to Popper's falsificationism in the next lesson."),
        ex("Model essay plan 1", "Explain Hume's problem of induction.", [
            ("Introduction", "Define induction and its role in science."),
            ("The argument", "Uniformity cannot be proved a priori nor by experience without circularity."),
            ("Consequence", "Induction rests on habit, not demonstration; science's claims are never certain."),
            ("Evaluation", "State a reply (pragmatic or probabilistic) and its weakness."),
        ]),
        ex("Model essay plan 2", "'Scientific laws can be proved by experiment.' Discuss.", [
            ("Claim", "Experiments seem to confirm laws."),
            ("Objection", "Confirming instances never prove a universal claim; one counterexample can refute it."),
            ("Reply", "Scientists use probability and the accumulation of evidence; laws are best-supported, not proved."),
            ("Judgement", "Experiments give good grounds, not proof."),
        ]),
        MISTAKE("Saying induction is 'wrong'", "Hume's point is that it cannot be justified without circularity, not that we should stop using it."),
        MISTAKE("Calling every observation-based argument inductive", "Deduction from a hypothesis to a prediction is part of the method as well."),
        qz("What is the central claim of Hume's problem of induction?",
           "No non-circular argument justifies the belief that the future will resemble the past",
           [("Experience is always misleading", "Hume does not say experience is always wrong."),
            ("Scientific laws are false", "He says we cannot justify them without circularity."),
            ("Deduction is impossible", "Deduction is not the issue.")],
           "Justifying induction by its past success is itself an inductive argument.", 1,
           hint="Why is the appeal to past success a problem?"),
        qz("A hypothesis H predicts observation O. O is observed. What follows?",
           "H is supported, but not proved, since other hypotheses might also predict O",
           [("H is proved true", "That is the fallacy of affirming the consequent."),
            ("H is refuted", "Refutation requires that O fails."),
            ("Nothing at all can be said", "The evidence gives some support.")],
           "From 'if H then O' and O, we cannot validly infer H.", 3,
           hint="Which form is valid: tollens or affirming the consequent?"),
        PQ("Distinguish induction from deduction with an example of each.",
           "Deduction: All humans are mortal; Ngo is human; so Ngo is mortal (the conclusion is necessary). Induction: every raven I have seen is black; so all ravens are black (the conclusion is probable only)."),
        PQ("Explain why a failed prediction can refute a hypothesis but a successful prediction cannot prove it.",
           "From 'if H then O' and 'not O' we can validly infer 'not H' (modus tollens). From 'if H then O' and 'O' we cannot validly infer H (affirming the consequent), since other hypotheses may predict O. (An auxiliary assumption might also be at fault: check your textbook on the Duhem-Quine point.)"),
        PQ("Evaluate one reply to the problem of induction.",
           "Pragmatic reply: induction is the best policy available; if nature is regular it works, and nothing else would. Weakness: it does not show that nature will remain regular. Judgement: the reply explains why we may as well use induction but does not remove Hume's challenge."),
        SUM("The scientific method moves from observation to hypothesis, prediction, test and revision.",
            "Induction goes beyond its premises; deduction preserves truth.",
            "Hume: induction cannot be justified without circularity.",
            "Replies (pragmatic, probabilistic, Popper's) each have problems; Goodman's grue adds another.",
            "Modus tollens is valid and affirming the consequent is invalid: refutation is easier than proof."),
    ],
))

LESSONS.append(lesson(
    module=M_EPI, topic="Bachelard, Popper and Kuhn",
    title="Bachelard, Popper and Kuhn: how science progresses",
    slug="psu1-bachelard-popper-kuhn",
    minutes=25,
    summary="Bachelard's epistemological obstacle and rupture, Popper's falsificationism and demarcation, Kuhn's paradigms and scientific revolutions, compared and evaluated.",
    objectives=[
        "Explain Bachelard's epistemological obstacle and epistemological rupture",
        "Explain Popper's falsificationism and the demarcation of science",
        "Explain Kuhn's normal science, paradigm, anomaly, crisis and revolution",
        "Compare and evaluate the three views",
    ],
    key_concepts=["Epistemological obstacle", "Falsifiability", "Demarcation", "Paradigm", "Scientific revolution", "Incommensurability"],
    blocks=[
        H("Introduction"),
        T("Why did people believe for centuries that the sun goes round the Earth, and why did they change? Three thinkers answer in different "
          "ways. Gaston Bachelard (French, 1884-1962) looks at the mental obstacles inside the scientist. Karl Popper (1902-1994, Austrian-born, "
          "later British) looks at the logic of testing. Thomas Kuhn (American, 1922-1996) looks at the history and community of science."),
        IMG("alpsu1-kuhn-cycle.svg", alt="A cycle: normal science, anomalies, crisis, revolution, new normal science.", caption="Figure 1. Kuhn's pattern of scientific change."),
        H("Bachelard: epistemological obstacles"),
        D("An **epistemological obstacle** (obstacle epistemologique) is a habit of mind, found in the scientist and in common sense, that blocks the growth of "
          "scientific knowledge. Bachelard described them in *The Formation of the Scientific Mind* (1938).", title="Epistemological obstacle"),
        KEY("Examples of obstacles", "Bachelard discusses many; know at least three.", cards=[
            ["First experience", "Trusting immediate impressions: the sun seems to move across the sky."],
            ["Substantialism", "Explaining properties by hidden substances: 'it burns because it contains fire'."],
            ["Verbal obstacle", "A familiar image or word seems to explain more than it does, such as 'bad air' for malaria (the word malaria comes from 'bad air')."],
            ["General knowledge", "Premature generalisations accepted without testing."],
        ]),
        T("Progress needs an **epistemological rupture** (break): science does not continue common sense but breaks with it, forming new concepts "
          "and new methods. For Bachelard, the scientific mind must constantly criticise and correct itself and its own past."),
        H("Popper: falsification and demarcation"),
        D("The **problem of demarcation** is the problem of drawing a line between science and non-science. Popper's answer is **falsifiability**: "
          "a theory is scientific if it forbids some possible observations and so could be shown false by experience.", title="Falsifiability"),
        T("Popper argued that science does not proceed by inductive proof. Scientists make bold **conjectures** and try to **refute** them. A theory that "
          "survives severe tests is **corroborated**, but never proved. He used Einstein's prediction of the bending of starlight as an example of a bold, risky "
          "prediction, and contrasted it with theories that, in his view, can explain any event, citing certain versions of Marxism and "
          "psychoanalysis as examples. Those judgements are disputed."),
        KEY("Objections to Popper", "A fair essay includes at least two.", cards=[
            ["Duhem-Quine problem", "A test checks a theory together with auxiliary assumptions, so a failed prediction does not show which part is wrong."],
            ["Scientists rarely drop a theory at once", "Real science keeps theories despite anomalies. Reply: Popper allowed that scientists may reasonably defend a theory for a while."],
            ["Probabilistic theories", "Statistical claims cannot be strictly refuted."],
            ["Too narrow", "Some well-regarded fields (history of the earth, parts of evolutionary theory) are not easily tested by simple prediction."],
        ]),
        H("Kuhn: paradigms and revolutions"),
        T("Thomas Kuhn argued in *The Structure of Scientific Revolutions* (1962) that real science works in phases."),
        KEY("Kuhn's cycle", "Memorise the sequence.", cards=[
            ["Normal science", "Scientists work within a shared **paradigm**: accepted theories, methods and standard examples. They solve puzzles."],
            ["Anomalies", "Results that do not fit begin to pile up."],
            ["Crisis", "Confidence in the paradigm weakens; rival ideas appear."],
            ["Revolution", "A new paradigm replaces the old, as in the shift from the Earth-centred to the Sun-centred view."],
        ]),
        T("Kuhn also argued that rival paradigms may be **incommensurable**: they use different concepts and standards, so comparison is hard and "
          "choice is not decided by evidence and logic alone. He described this as partly a matter of persuasion within the community, which led "
          "critics to charge him with relativism. Kuhn himself rejected that charge, listing shared values such as accuracy and simplicity."),
        H("Comparing the three"),
        KEY("Who explains what", "One-sentence summaries.", cards=[
            ["Bachelard", "Progress needs a break with common sense and the removal of obstacles in the mind."],
            ["Popper", "Progress needs bold theories and attempts to refute them; science is marked by falsifiability."],
            ["Kuhn", "Progress is mostly puzzle-solving within a paradigm, interrupted by revolutions; the community matters."],
        ]),
        TIP("Evaluate each philosopher separately and compare only at the end. The Board's report advises students to evaluate individual philosophers."),
        ex("Model essay plan 1", "Explain Popper's falsificationism and one objection to it.", [
            ("Introduction", "Problem of demarcation, and Popper's answer."),
            ("Argument", "Induction cannot prove laws; bold conjectures, severe tests, corroboration."),
            ("Example", "Starlight prediction versus a theory that explains everything."),
            ("Objection", "Duhem-Quine: auxiliary assumptions. Reply: methodological rules about not rescuing a theory with ad hoc moves."),
        ]),
        ex("Model essay plan 2", "Discuss the claim that Kuhn made science irrational.", [
            ("Claim", "Paradigm choice is not fixed by logic and evidence alone."),
            ("For", "Incommensurability and the role of persuasion."),
            ("Against", "Kuhn appealed to shared values; paradigms are replaced because they solve problems better."),
            ("Judgement", "Kuhn describes the psychology and sociology of science more than he denies rationality."),
        ]),
        MISTAKE("Saying Popper claims that theories are proved false for good", "Even refutation depends on auxiliary assumptions and accepted observations."),
        MISTAKE("Using 'paradigm' to mean any idea", "In Kuhn it is a shared framework of theories, methods and exemplars that guides a community."),
        qz("What is Bachelard's 'epistemological obstacle'?",
           "A habit of thought that blocks the growth of scientific knowledge",
           [("A physical limit to what instruments can measure", "It is a mental obstacle."),
            ("A law that forbids some experiments", "It is not a legal or moral rule."),
            ("A lack of money for research", "It is about thinking, not funding.")],
           "Bachelard's obstacles include first experience, substantialism and verbal images.", 2,
           hint="The obstacle is in the mind."),
        qz("In Kuhn's account, what typically comes after the accumulation of anomalies?",
           "Crisis",
           [("Normal science becomes stronger", "Anomalies make the paradigm weaker."),
            ("Immediate falsification of all theories", "Kuhn describes a gradual crisis."),
            ("The end of science", "Crisis may lead to a new paradigm.")],
           "Anomalies lead to crisis; a revolution may then replace the paradigm.", 0,
           hint="Follow the cycle."),
        PQ("Explain Popper's criterion of demarcation.",
           "A theory is scientific if it is falsifiable: it makes claims that observation could show to be false. Theories that are compatible with every possible observation are not scientific by this criterion."),
        PQ("Describe Kuhn's concept of normal science.",
           "Normal science is the period when a community works within an accepted paradigm, solving puzzles that the paradigm defines, without questioning its foundations."),
        PQ("Compare Popper and Kuhn on how science progresses.",
           "Popper: science progresses through bold conjectures and attempts to refute them; falsification is the key. Kuhn: science usually proceeds by puzzle-solving within a paradigm and changes through revolutions. Popper is mainly prescriptive (what science should do); Kuhn is more descriptive (what historians find). Judgement: each captures part of science; Kuhn shows why scientists do not drop theories at the first anomaly."),
        SUM("Bachelard: epistemological obstacles and rupture; science breaks with common sense.",
            "Popper: demarcation by falsifiability; conjecture, refutation, corroboration.",
            "Kuhn: normal science, anomalies, crisis, revolution; incommensurable paradigms.",
            "Objections: Duhem-Quine (Popper), charge of relativism (Kuhn).",
            "Evaluate individual thinkers before comparing them."),
    ],
))

LESSONS.append(lesson(
    module=M_EPI, topic="The philosophy of mathematics",
    title="The philosophy of mathematics: what are numbers and proofs?",
    slug="psu1-philosophy-of-mathematics",
    minutes=23,
    summary="Platonism, logicism, formalism, intuitionism and empiricism about mathematics, Russell's paradox and Godel's incompleteness theorems in outline, and the puzzle of why mathematics applies to the world.",
    objectives=[
        "Distinguish Platonism, logicism, formalism, intuitionism and empiricism",
        "Explain how a mathematical proof gives certainty, using Euclid's argument about primes",
        "State Russell's paradox and the outline of Godel's incompleteness results",
        "Evaluate the schools and the question of how mathematics applies to the world",
    ],
    key_concepts=["Platonism", "Logicism", "Formalism", "Intuitionism", "Russell's paradox", "Incompleteness"],
    blocks=[
        H("Introduction"),
        T("2 + 3 = 5 in Yaounde, in Tokyo and, we believe, on the other side of the galaxy. Nobody can open a market stall and find that "
          "2 + 3 is sometimes 6. What kind of truth is this? Is the number 5 a thing somewhere, a human invention or a rule of "
          "a game? The philosophy of mathematics asks about the nature of mathematical objects, the source of mathematical knowledge and "
          "the reason why mathematics describes the physical world so well."),
        H("Mathematical knowledge: proof"),
        T("Mathematical truths seem to be known by proof from axioms, not by observation. A famous example is Euclid's argument that there is no "
          "largest prime number."),
        EX("Worked example: there are infinitely many primes", intro="Show that no finite list of primes contains all primes.", steps=[
            S("Assume the opposite", text="Suppose the primes are p1, p2, ..., pn, a complete finite list."),
            S("Build a number", text="Let N be the product of all of them plus 1."),
            S("Look at its divisors", text="Dividing N by any pi leaves remainder 1, so no prime on the list divides N."),
            S("Contradiction", text="But N has a prime factor (or is itself prime), which is not on the list. So the list was not complete."),
            S("Check with a small case", text="2 x 3 x 5 x 7 x 11 x 13 + 1 = 30031 is not prime: it equals 59 x 509. Both 59 and 509 are new primes, not on the list. The proof does not claim that N is prime, only that it has a prime factor outside the list."),
        ]),
        T("This proof gives certainty because it follows from premises by valid steps. It does not depend on observation, which is why "
          "Kant spoke of the **a priori**. The question is what the premises (axioms) are and why they hold."),
        H("The main philosophies of mathematics"),
        KEY("Five views", "Learn one sentence and one objection for each.", cards=[
            ["Platonism", "Mathematical objects (numbers, sets) exist independently of us, in an abstract realm, and are discovered. Objection: how can we know abstract objects that have no causal link with us?"],
            ["Logicism (Frege, Russell)", "Mathematics reduces to logic: its truths follow from logical definitions. Objection: the logic needed seems to carry set-theoretic assumptions, and paradoxes appeared."],
            ["Formalism (Hilbert)", "Mathematics is the manipulation of symbols by rules; proofs are formal derivations. Objection: why does the game matter, and Godel limited the programme."],
            ["Intuitionism (Brouwer)", "Mathematics is a construction of the human mind; a statement is true only if it can be constructed or proved. Rejects the law of excluded middle for infinite cases. Objection: it discards a great deal of classical mathematics."],
            ["Empiricism (Mill)", "Mathematical truths are very general truths learned from experience. Objection: they seem necessary and certain, not just well confirmed."],
        ]),
        H("Paradox and incompleteness"),
        D("**Russell's paradox** (1901): consider the set R of all sets that are not members of themselves. Is R a member of itself? If it is, "
          "it is not; if it is not, it is. This contradiction showed that naive set theory, which was used in logicism, is "
          "inconsistent, and led to more careful axioms.", title="Russell's paradox"),
        D("**Godel's incompleteness theorems** (1931), stated informally: in any consistent formal system strong enough to express basic arithmetic "
          "there are statements that are true but cannot be proved within the system (first theorem), and such a system cannot prove "
          "its own consistency (second theorem). They limited Hilbert's hope of a complete formal foundation. Check your textbook for the "
          "exact conditions.", title="Godel's incompleteness"),
        H("Why does mathematics apply to the world?"),
        T("Physics uses mathematics with astonishing success. Platonists say that the physical world participates in mathematical structure; "
          "empiricists say mathematics arises from abstractions of experience; formalists and others say we choose tools that suit "
          "us. The question remains open. It links to the philosophy of science: mathematical models are tested by observation."),
        TIP("Do not mix logic and mathematics: this lesson is about the nature of mathematical knowledge. Truth tables and syllogisms belong to the logic lessons."),
        ex("Model essay plan 1", "Compare Platonism and intuitionism in the philosophy of mathematics.", [
            ("Platonism", "Mathematical objects exist independently; mathematics discovers; classical logic holds."),
            ("Intuitionism", "Mathematics is constructed by the mind; truth means provability; excluded middle fails for infinite domains."),
            ("Objections", "Platonism: epistemic access. Intuitionism: loses much classical mathematics."),
            ("Judgement", "Platonism explains objectivity; intuitionism explains knowledge; neither is complete."),
        ]),
        ex("Model essay plan 2", "What do Godel's theorems show about mathematics?", [
            ("Statement", "Consistent formal systems capable of arithmetic have true but unprovable statements."),
            ("Impact", "Hilbert's formalist aim of complete formal systems cannot be reached."),
            ("Limits", "They do not show that mathematics is unreliable or that truth is relative."),
            ("Judgement", "Mathematical truth goes beyond any single formal system."),
        ]),
        MISTAKE("Saying Godel proved that nothing can be known for certain", "His theorems concern formal systems and provability, not all knowledge."),
        MISTAKE("Thinking Euclid's number N must be prime", "The proof only shows N has a prime factor outside the list: 30031 = 59 x 509."),
        qz("Which school holds that mathematical objects exist independently of the human mind?",
           "Platonism",
           [("Intuitionism", "It says mathematics is a mental construction."),
            ("Formalism", "It treats mathematics as symbol manipulation."),
            ("Empiricism", "It bases mathematics on experience.")],
           "Platonism: numbers and sets exist in an abstract realm and are discovered.", 1,
           hint="Think of Plato's Forms."),
        qz("What did Russell's paradox show?",
           "That naive set theory, as used in the logicist programme, is inconsistent",
           [("That arithmetic is false", "It affected set theory, not arithmetic directly."),
            ("That proofs are impossible", "Proofs remained possible in revised systems."),
            ("That numbers do not exist", "It does not show that.")],
           "The set of all sets that are not members of themselves cannot consistently exist.", 3,
           hint="It concerns sets that contain themselves."),
        PQ("Outline Euclid's proof that there are infinitely many primes.",
           "Assume a finite list of all primes; multiply them and add 1 to get N. No prime on the list divides N (remainder 1). But N has a prime factor, which must lie outside the list. So the list is incomplete, a contradiction. Hence the primes are infinite."),
        PQ("Explain the formalist view of mathematics and one objection.",
           "Formalism (Hilbert) treats mathematics as a system of symbols manipulated by formal rules, with truth as derivability. Objection: it does not explain why the symbol-game applies to the world, and Godel's theorems showed that no consistent formal system captures all arithmetic truth."),
        PQ("Discuss whether mathematics is discovered or invented.",
           "Discovered: mathematical truths seem objective, independent of belief, and often surprising (Platonism). Invented: mathematics is made by humans with chosen axioms (formalism, intuitionism). Judgement: the choice of axioms is invented, while consequences are discovered; the debate shows the limits of each simple view."),
        SUM("Mathematical knowledge is mostly by proof from axioms, as in Euclid's argument about primes.",
            "Platonism, logicism, formalism, intuitionism and empiricism give five views of what mathematics is.",
            "Russell's paradox troubled logicism; Godel's theorems limited formalism.",
            "How mathematics applies to the world remains an open question.",
            "Be careful to state what each result shows and what it does not."),
    ],
))

LESSONS.append(lesson(
    module=M_EPI, topic="Philosophy of biology and bioethics",
    title="Philosophy of biology and bioethics",
    slug="psu1-philosophy-of-biology-and-bioethics",
    minutes=24,
    summary="Mechanism, vitalism and teleology, explanation by natural selection, the question of what life is, and the principles and main cases of bioethics.",
    objectives=[
        "Contrast mechanism and vitalism and explain teleological language in biology",
        "Explain why natural selection explains function and what philosophers ask about it",
        "State the four principles of bioethics and apply them to cases",
        "Evaluate arguments in bioethics fairly",
    ],
    key_concepts=["Mechanism", "Vitalism", "Teleology", "Natural selection", "Autonomy", "Beneficence", "Non-maleficence", "Justice"],
    blocks=[
        H("Introduction"),
        T("Two questions meet in this lesson. First, a question about biological knowledge: what is life, and can biology be explained like physics? "
          "Second, a question about action: what should we do when biology gives us power over birth, health and death, from "
          "vaccination campaigns to organ transplants? The first is philosophy of biology; the second is **bioethics**."),
        H("Is life explained by physics and chemistry?"),
        KEY("Mechanism and vitalism", "An old debate with modern versions.", cards=[
            ["Mechanism", "Living things are complex machines, explained fully by physical and chemical processes (Descartes held this for animals)."],
            ["Vitalism", "Life has a special vital principle that is not reducible to physics and chemistry. It is now rejected by most scientists because biochemistry has explained many life processes."],
            ["Modern middle view", "Organisms are physical systems, but organisation, information and evolution give biology explanations of its own (emergence versus reductionism)."],
        ]),
        D("**Teleology** is explanation in terms of purpose or goal ('the heart is for pumping blood'). Philosophers ask whether such language "
          "is legitimate or only a shorthand.", title="Teleology"),
        H("Natural selection and function"),
        T("Charles Darwin's theory of evolution by natural selection (*On the Origin of Species*, 1859) gives a way of understanding purpose "
          "without a designer: traits that helped ancestors survive and reproduce were passed on, so the heart 'is for' pumping blood because "
          "pumping blood is what it was selected for. This is a **selected-effects** account of function, and it makes teleological talk "
          "respectable. Philosophers also discuss whether all traits are adaptations, how to define a **species** (several competing definitions exist, "
          "such as the group that can interbreed), and the level at which selection acts: genes, organisms or groups."),
        T("Some people object that evolution conflicts with their religious beliefs. Philosophy distinguishes the scientific question (what explains "
          "the diversity of life) from questions of ultimate meaning. Many religious thinkers accept evolution. A student should state "
          "the scientific theory accurately and treat other views with respect."),
        H("Bioethics: four principles"),
        D("The most used framework in bioethics is the four principles of Beauchamp and Childress: **autonomy** (respect a person's right to decide), "
          "**beneficence** (do good), **non-maleficence** (do no harm) and **justice** (fairness in the distribution of benefits and burdens). "
          "They can conflict, and judgement is needed.", title="Four principles"),
        KEY("Applying the principles", "Typical cases (general principles for study, not medical or legal advice).", cards=[
            ["Informed consent", "A patient should receive understandable information and decide freely. Autonomy against beneficence when a doctor believes the choice will harm."],
            ["Organ transplantation", "Many lives could be saved, but who gets scarce organs (justice), and may organs be taken without consent?"],
            ["End of life", "Refusing treatment, palliative care and euthanasia raise autonomy, non-maleficence and the sanctity of life. Laws differ by country: check the local law."],
            ["Genetic technology and GMOs", "Possible benefits (health, food) against risks, ownership and fairness; the precautionary principle is often discussed."],
            ["Research and animals", "Experiments on humans need consent and oversight; the use of animals raises questions of their moral status."],
        ]),
        T("In the African context, discussions stress the community as well as the individual: a family may take part in decisions about care, "
          "and the idea of the person as defined by relations affects how consent is understood. Medical research in poorer countries "
          "raises questions of justice and exploitation. Real patients and real cases need qualified professionals; this lesson teaches "
          "how to reason about them."),
        H("Objections and replies"),
        KEY("Three typical debates", "Present both sides.", cards=[
            ["Reductionism", "Objection: explaining life by molecules loses the organism. Reply: reduction explains how parts work; higher-level explanations still matter."],
            ["Principlism", "Objection: four principles are too abstract and Western. Reply: they are a checklist that other traditions can supplement; many cultures recognise them."],
            ["Moral status", "Objection: some deny that embryos or animals have rights. Reply: views differ on when moral status begins and on its grounds."],
        ]),
        ex("Model essay plan 1", "Discuss whether biology can be reduced to physics and chemistry.", [
            ("Mechanism", "Biochemistry explains many life processes (digestion, heredity at the molecular level)."),
            ("Against", "Function and organisation, natural selection and ecology need explanations at the level of organisms and populations."),
            ("Vitalism", "No special life force has been found; it is rejected."),
            ("Judgement", "Living things are physical, but biology is not simply physics; explanations work at several levels."),
        ]),
        ex("Model essay plan 2", "Apply the four principles to a case of a patient refusing treatment.", [
            ("Autonomy", "Competent adults may refuse treatment after being informed."),
            ("Beneficence and non-maleficence", "The doctor wants to help but must not force harm; weigh risks of treatment and refusal."),
            ("Justice", "Resources and fairness; the effect on other patients."),
            ("Judgement", "In most accounts a competent, informed refusal is respected, with support and counselling; the law of the country applies."),
        ]),
        MISTAKE("Saying evolution means 'man comes from monkeys'", "Humans and other apes share common ancestors; no living species is the ancestor of another."),
        MISTAKE("Giving an opinion instead of an argument in bioethics", "State the principles, apply them to the case, weigh conflicts and then reach a reasoned judgement."),
        qz("Which statement best describes vitalism?",
           "Life depends on a special vital force not reducible to physics and chemistry",
           [("Living things are machines", "That is mechanism."),
            ("Species never change", "That is not vitalism."),
            ("Life began from other planets", "It is unrelated.")],
           "Vitalism posits a non-physical principle of life; modern biology rejects it because of molecular explanations.", 2,
           hint="Which view adds an extra principle?"),
        qz("A doctor wants to treat a competent adult who, fully informed, refuses. Which principle supports the patient's refusal?",
           "Autonomy",
           [("Beneficence", "Beneficence supports doing good for the patient, which may favour treatment."),
            ("Justice", "Justice concerns fair distribution of benefits."),
            ("Teleology", "Teleology is explanation by purpose, not a bioethical principle.")],
           "Autonomy is respect for a person's right to decide about his or her own body and life.", 0,
           hint="Whose decision is it?"),
        PQ("What is teleology and why does natural selection make it respectable in biology?",
           "Teleology explains by purpose ('the heart is for pumping blood'). Natural selection explains purpose naturally: traits exist because of the effects for which they were selected in past generations, so function talk refers to selection history, not to a conscious designer."),
        PQ("List the four principles of bioethics and give one conflict between two of them.",
           "Autonomy, beneficence, non-maleficence, justice. Conflict: autonomy versus beneficence when a patient refuses a treatment that would help him."),
        PQ("Discuss whether organs for transplant should be taken from a deceased person unless he or she has opted out.",
           "For (presumed consent): saves lives; justice for those on waiting lists. Against: may violate autonomy and family wishes, and public trust. Judgement: depends on strong safeguards, public information and local values; the law of each country applies."),
        SUM("Mechanism explains life by physics and chemistry; vitalism adds a special force and is rejected; biology also needs higher-level explanations.",
            "Natural selection explains function and so makes teleological language respectable.",
            "Bioethics uses four principles: autonomy, beneficence, non-maleficence, justice.",
            "Apply them to cases, weigh conflicts and give a reasoned judgement; laws differ by country.",
            "Respect different views and state the science accurately."),
    ],
))
