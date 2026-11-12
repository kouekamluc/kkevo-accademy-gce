"""A Level Religious Studies (0785), Lower Sixth, modules 1 to 3: Pentateuchal criticism, the monarchy and cult, the intertestamental period and the Synoptic problem (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "lower-sixth")

M1 = "Old Testament: Pentateuchal Criticism & Early Israel"
M2 = "Old Testament: Rise of the Monarchy & Cultic Institutions"
M3 = "New Testament: Intertestamental Period & the Synoptic Problem"

LESSONS = []

# ---------------------------------------------------------------------------
# 1. The Documentary Hypothesis
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The Documentary Hypothesis",
    title="The Documentary Hypothesis: J, E, D and P and their critics",
    slug="rsl1-documentary-hypothesis",
    minutes=24,
    summary="Why many scholars think the first five books were woven from sources called J, E, D and P, what clues they use, what the main rival views say, and how to weigh the theory.",
    objectives=[
        "State what the Documentary Hypothesis claims and who developed it",
        "Describe the four sources J, E, D and P by name, date, setting and style",
        "Explain the clues scholars use: divine names, doublets, contradictions, vocabulary",
        "Evaluate the theory using the objections of its critics and the traditional view",
    ],
    key_concepts=["Pentateuch", "Source criticism", "Documentary Hypothesis", "J E D P", "Doublet", "Redactor"],
    blocks=[
        H("Introduction"),
        T("The **Pentateuch** is the first five books of the Bible: Genesis, Exodus, Leviticus, Numbers and Deuteronomy. "
          "Jews call them the Torah. For many centuries Jewish and Christian tradition said that Moses wrote them. "
          "From the 1700s some scholars began to ask whether the books show signs of several hands.\n\n"
          "This lesson explains one famous answer, the **Documentary Hypothesis**. It is a scholarly theory, not a fact, "
          "and it has many critics. You must be able to explain it fairly and also to judge it."),
        D("The study of a biblical book to find the earlier written documents (sources) that its author or editor may have joined together. "
          "It asks: who wrote this part, when, where, and why?", title="Source criticism"),
        D("The theory that the Pentateuch was made by combining four main written sources, usually called J, E, D and P, "
          "which were later joined by editors. Its classic form was set out by Julius Wellhausen in the 1870s and 1880s.",
          title="Documentary Hypothesis"),
        H("The clues that started the search"),
        T("Scholars noticed patterns in the text that a single author does not obviously explain. Four clues are most often used."),
        KEY("Four clues", "Each clue points to more than one hand, but each can also be explained in other ways.", cards=[
            ["Divine names", "Some passages call God Yahweh (written LORD in many Bibles) and others call him Elohim. Jean Astruc (1753) used this clue first."],
            ["Doublets", "The same story told twice: two accounts of creation (Genesis 1 and 2), and three stories of a patriarch passing off his wife as his sister (Genesis 12, 20 and 26)."],
            ["Contradictions", "In the flood story, one verse says Noah takes two of each animal and another says seven pairs of the clean animals."],
            ["Style and ideas", "Some passages are vivid stories in which God walks and talks with people. Others are formal lists and laws in a solemn, repeated style."],
        ]),
        H("The four sources"),
        KEY("J, E, D and P in the classic theory", "Dates are the classic ones and are debated. Check your textbook.", cards=[
            ["J, the Yahwist", "Uses the name Yahweh from the start. Probably from the southern kingdom, Judah. Dated by many to about the 10th to 9th century BC. Vivid stories; God is described in human terms. Genesis 2 to 4 is the standard example."],
            ["E, the Elohist", "Uses Elohim until the name Yahweh is revealed to Moses. Probably from the northern kingdom. About the 9th to 8th century BC. Interested in prophets and in dreams and angels as God's means of speaking."],
            ["D, the Deuteronomist", "The book of Deuteronomy. Preaching style, 'hear, O Israel', blessing for obedience and curse for disobedience, one place of worship. Often linked to the reform of King Josiah about 621 BC."],
            ["P, the Priestly source", "Interest in worship, priests, dates, genealogies and laws. Genesis 1, much of Exodus 25 to 40, Leviticus and parts of Numbers. Placed by the classic theory late, during or after the exile in Babylon (6th to 5th century BC)."],
        ]),
        T("An editor, called a **redactor**, is thought to have joined the sources into the books we have. Genesis 1:1 to 2:4a is usually given to P, and from 2:4b the story is usually given to J. "
          "This is why the order in the classic theory is often written J, E, D, P."),
        EX("Worked example 1: reading a doublet", intro="Show how the two creation accounts are used as evidence for two sources.", steps=[
            S("Describe account A (Genesis 1:1 to 2:4a)", text="God creates in seven days in a fixed order, by speaking. Humans, male and female, are made last. The style is formal and repeated."),
            S("Describe account B (Genesis 2:4b onward)", text="Yahweh God forms a man from the ground first, then a garden, then the animals, then the woman. God acts like a potter and gardener."),
            S("Compare", text="The order differs (humans last in one, first in the other), the name for God differs, and the style differs."),
            S("Conclusion of the source critic", text="Two traditions, P and J, were placed side by side by an editor."),
            S("Reply of a critic of the theory", text="The accounts can be read as one design: chapter 1 gives the wide view and chapter 2 zooms in on humans. The change of divine name may be deliberate."),
        ]),
        H("How the theory developed"),
        T("Astruc noticed divine names. Later scholars added the other clues. Wellhausen (1878 and after) argued from the history of Israel's religion that the sources were written in the order J, E, D, P "
          "and that the priestly law was the latest layer, not the earliest. This changed how the story of Israel's religion was told. "
          "Many later scholars have kept the idea of sources but changed the dates and the number of sources."),
        H("Criticisms and rival views"),
        KEY("Main objections", "A strong answer names at least two rival positions.", cards=[
            ["Traditional view", "Moses is the author of the core of the Pentateuch, and later editors added small updates such as the account of Moses' death in Deuteronomy 34. Many Jews and Christians still hold this."],
            ["Fragmentary and supplementary views", "Scholars such as R. N. Whybray argued that the books grew from many small units or by supplementing one core text, not from four continuous documents."],
            ["Unity of style and ancient parallels", "Some, such as Umberto Cassuto and Kenneth Kitchen, argued that repetition and variation are normal in ancient Near Eastern writing, so doublets do not need several authors."],
            ["Late dating", "Some scholars, for example John Van Seters, place J much later than the classic theory does, even in the exile. Dating is one of the weakest parts of the classic theory."],
        ]),
        T("Notice what is **not** in dispute. Almost all scholars agree the Pentateuch has a long history and uses older material. They disagree about how many sources, how early they are and who joined them."),
        MISTAKE("Treating J, E, D and P as discovered documents", "No manuscript of J or E has been found. The sources are reconstructed from the text. Write 'scholars argue' and 'the theory suggests', not 'J wrote'."),
        MISTAKE("Saying the theory proves Moses wrote nothing", "The theory is about the final shape of the books. It does not by itself settle whether Moses lived or whether older material goes back to his time."),
        TIP("Exam link: this topic suits essay questions on how the Pentateuch was formed and structured questions that ask for the sources and the evidence. "
            "It supports the Old Testament material in the Board's syllabus, which the Board's report places in Section 1.1 for Paper 2. Check with your teacher exactly where it appears, because the report lists the section only by its title. "
            "It can also appear in Paper 1 multiple choice as a short fact such as the source linked with Deuteronomy."),
        QUIZ("Which source is usually linked with Deuteronomy and the reform of King Josiah?",
             ["J", "E", "D", "P"], 2,
             "D, the Deuteronomist, is the source of Deuteronomy. Many scholars link it to the reform of King Josiah about 621 BC.",
             hint="D stands for the name of the book.",
             feedback=["J is the Yahwist, associated with the southern kingdom and vivid early stories.", "E is the Elohist, usually linked with the northern kingdom.", "", "P is the priestly source, concerned with worship, genealogies and law."]),
        QUIZ("A scholar says that the repeated wife-sister stories can be explained as one author's literary pattern. Which position is this?",
             ["The classic Documentary Hypothesis", "A critic of the Documentary Hypothesis", "The Priestly source", "The theory of Q"], 1,
             "This is a reply to the use of doublets as evidence for separate sources. It is a criticism of the Documentary Hypothesis.",
             feedback=["The classic theory uses doublets as evidence for different sources.", "", "P is a source, not a position about method.", "Q is a theory about the Gospels, not the Pentateuch."]),
        PQ("State four clues that scholars use to argue that the Pentateuch contains more than one source.",
           "Divine names (Yahweh and Elohim); doublets (two accounts of creation; three wife-sister stories); contradictions (the numbers of animals taken into the ark); differences of style and vocabulary (vivid storytelling against formal lists and laws). "
           "One mark-worthy detail for each clue is enough in a structured question."),
        PQ("Describe the main features of the P source and say where scholars find it.",
           "P is the Priestly source. Its interests are worship, priests, sacrifices, dates, genealogies and law. Its style is formal and repeated. "
           "Scholars place Genesis 1, genealogies in Genesis, much of Exodus 25 to 40, Leviticus and parts of Numbers in P. The classic theory dates it late, in or after the exile, though some scholars argue for an earlier date."),
        PQ("'The Documentary Hypothesis is the best explanation of how the Pentateuch was written.' Discuss.",
           "Model plan. Introduction: define the hypothesis and name Wellhausen. For: divine names, doublets, contradictions, style differences, and that sources explain these together. "
           "Against: no manuscript evidence; traditional view of Mosaic authorship; fragmentary and supplementary models; ancient Near Eastern writing repeats stories; wide disagreement about dates. "
           "Evaluation: the idea of several layers is widely accepted, but the classic four-source model with fixed dates is much debated. Conclusion: the hypothesis is a useful tool, not a proven fact."),
        SUM("The Documentary Hypothesis says the Pentateuch combines the sources J, E, D and P, joined by editors.",
            "Clues: divine names, doublets, contradictions and differences of style.",
            "J is southern and vivid, E northern, D is Deuteronomy and Josiah's reform, P is priestly and late in the classic theory.",
            "Critics include the traditional Mosaic view, fragmentary and supplementary models, and scholars who stress ancient writing habits.",
            "Write about it as a scholarly theory with evidence for and against."),
    ],
))

# ---------------------------------------------------------------------------
# 2. Genesis 1 to 11 and the ancient Near East
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="Genesis 1 to 11 and the ancient Near East",
    title="Genesis 1 to 11 beside Babylonian creation and flood stories",
    slug="rsl1-genesis-1-11-ancient-near-east",
    minutes=24,
    summary="Compares Genesis creation, flood and Babel with Mesopotamian texts (Enuma Elish, Atrahasis, Gilgamesh), shows the similarities and the key differences, and weighs borrowing against common heritage.",
    objectives=[
        "Name the main Mesopotamian texts compared with Genesis 1 to 11",
        "Compare the creation and flood stories point by point",
        "Explain the main theological differences in the Genesis versions",
        "Evaluate the explanations: direct borrowing, shared heritage, deliberate reply",
    ],
    key_concepts=["Ancient Near East", "Enuma Elish", "Atrahasis", "Epic of Gilgamesh", "Polemic", "Primeval history"],
    blocks=[
        H("Introduction"),
        T("Genesis 1 to 11 is called the **primeval history**: it covers creation, the Fall, Cain and Abel, the flood and the tower of Babel, before Abraham appears in chapter 12. "
          "Israel was not alone in the ancient world. Its neighbours in Mesopotamia (modern Iraq) and Egypt also told stories about the beginning of the world. "
          "Since the 1800s, when clay tablets were found and read, scholars have compared them with Genesis."),
        D("The lands around the eastern Mediterranean and Mesopotamia in the third to first millennium BC: Egypt, Sumer, Babylon, Assyria, the Hittites, Canaan and their neighbours.",
          title="Ancient Near East"),
        H("The main texts"),
        KEY("Four texts to know", "Dates are approximate. Check your textbook.", cards=[
            ["Enuma Elish", "A Babylonian creation poem. The god Marduk defeats the sea-goddess Tiamat, splits her body to make sky and earth, and humans are made to serve the gods. It was recited at the Babylonian New Year festival."],
            ["Atrahasis", "A Babylonian epic of about 1700 BC. Humans multiply and their noise disturbs the god Enlil, who sends plague, famine and finally a flood. The god Enki warns Atrahasis, who builds a boat."],
            ["Epic of Gilgamesh, tablet 11", "The hero Gilgamesh meets Utnapishtim, who survived a flood in a boat. He sent out a dove, a swallow and a raven, and made a sacrifice afterwards."],
            ["Sumerian King List", "A list of kings that begins with extremely long reigns before a flood and shorter ones after it. Scholars compare it with the long lives in Genesis 5."],
        ]),
        H("Creation: similarities and differences"),
        T("There are some resemblances. Both Genesis 1 and Enuma Elish begin with a watery, dark chaos. Both put the making of light, sky, land and humans in a sequence. "
          "Some scholars link the Hebrew word *tehom* (the deep) with the name Tiamat, but this link is debated. "
          "The differences are more striking, and an exam answer needs both."),
        KEY("Genesis against Enuma Elish", "Compare idea by idea.", cards=[
            ["God and the gods", "Genesis: one God, who has no rival. Enuma Elish: many gods who are born, fight and die."],
            ["How creation happens", "Genesis: God speaks and it is so. Enuma Elish: creation follows a battle and the killing of Tiamat."],
            ["The sea", "Genesis: the deep is part of creation under God's control. Enuma Elish: Tiamat is a goddess and an enemy."],
            ["Humans", "Genesis: humans are made in God's image and given care of the earth. Enuma Elish: humans are made to do the gods' work."],
            ["Sun and moon", "Genesis calls them lights that God made and sets in the sky. In many ancient cultures they were gods."],
        ]),
        H("Flood: similarities and differences"),
        T("The flood stories are closer than the creation stories. The Genesis flood and Gilgamesh tablet 11 share a divine decision to destroy humans, a warning to one man, a boat, animals saved, a landing on a mountain, "
          "birds sent out to test whether the water had gone, and a sacrifice after the flood. Most scholars think there is some historical link between the stories."),
        KEY("Why does the flood happen?", "This is the key difference.", cards=[
            ["Atrahasis", "Humans are too noisy and the god Enlil cannot sleep. The reason is a quarrel among gods."],
            ["Genesis", "The earth is filled with violence and corruption (Genesis 6), so the flood is a moral judgement, and Noah is saved because he is righteous."],
        ]),
        T("Another difference: in Gilgamesh the gods are afraid of the flood and crowd round the sacrifice like flies. In Genesis God makes a covenant with Noah and all living creatures, promising never to flood the whole earth again."),
        H("Babel and the genealogies"),
        T("The tower of Babel (Genesis 11) is often compared with the stepped temple towers of Mesopotamia, called ziggurats, one of which was in Babylon. "
          "'Babel' sounds like the Hebrew for Babylon. The story explains why people speak many languages. The long lives of Genesis 5 are compared with the Sumerian King List, though the numbers and purpose are different."),
        H("Three explanations"),
        KEY("How do scholars explain the similarities?", "Be ready to compare these.", cards=[
            ["Borrowing", "Israel took stories from Mesopotamia, for example during contact with Babylon, and changed them. Some say the exile in Babylon made the contact strong."],
            ["Common heritage", "Israelites and Mesopotamians shared older traditions about a great flood, which each people told in its own way. This suits the idea that Abraham came from Mesopotamia."],
            ["Deliberate reply (polemic)", "Genesis uses familiar story patterns to teach that only one God made everything and that the sun, moon and sea are not gods."],
        ]),
        EX("Worked example 1: compare the flood accounts", intro="Give three similarities and two differences between Genesis 6 to 9 and Gilgamesh tablet 11.", steps=[
            S("Similarity 1", text="A god or gods decide to destroy humans by flood, and one man is warned."),
            S("Similarity 2", text="The man builds a boat and saves his family and animals."),
            S("Similarity 3", text="Birds are sent out to find if the land is dry, and a sacrifice follows."),
            S("Difference 1", text="The reason: Genesis gives moral corruption and violence; the Mesopotamian texts give divine annoyance or the quarrel of gods."),
            S("Difference 2", text="Genesis has one God who acts with purpose and makes a covenant. Gilgamesh has many gods who quarrel and fear the flood."),
        ]),
        EX("Worked example 2: model plan", intro="'Genesis 1 to 11 was borrowed from Babylon.' Discuss.", steps=[
            S("Introduction", text="Define the primeval history and the texts. Say there are real parallels, but 'borrowed' is only one explanation."),
            S("For borrowing", text="Flood story details are close; Babel and ziggurats; Babylonian exile as a point of contact."),
            S("Against borrowing", text="Different theology (one God, moral reason, humans in God's image); the shared material may come from older common tradition."),
            S("Other explanations", text="Common heritage; deliberate polemic against pagan ideas."),
            S("Judgement", text="Contact is likely, but Genesis reworks the material for a different faith. Words like 'copied' hide the difference."),
        ]),
        MISTAKE("Saying that the parallels prove Genesis is false", "Similar stories do not make a text untrue. Believers can say the writer used familiar forms to teach a different message. Scholars discuss the evidence without deciding the faith question."),
        MISTAKE("Listing the stories without comparing", "A list of what Enuma Elish says is not an answer. Pair every similarity with a difference, and add a judgement."),
        TIP("Exam link: expect essay or structured questions on creation, the flood or the nature of God in Genesis, and short Paper 1 facts about the texts. "
            "The Board's report records that candidates often tell the story and do not answer the question that was set, so always finish a paragraph by saying what the comparison shows."),
        QUIZ("Which feature of the Genesis flood most clearly differs from the Atrahasis flood?",
             ["A boat is built", "Animals are saved", "The flood is a moral judgement by one God", "A man is warned"], 2,
             "In Genesis the flood answers human violence and corruption. In Atrahasis the cause is human noise that disturbs a god.",
             feedback=["Both stories have a boat.", "Both stories save animals or living creatures.", "", "Both stories have a warned hero."]),
        QUIZ("Which text has Marduk defeating Tiamat?",
             ["Atrahasis", "Enuma Elish", "Epic of Gilgamesh", "Sumerian King List"], 1,
             "Marduk and Tiamat belong to the Babylonian creation poem Enuma Elish.",
             feedback=["Atrahasis tells of the noisy humans and the flood.", "", "Gilgamesh includes the flood story told by Utnapishtim.", "The King List is a list of rulers."]),
        PQ("State three differences between the Genesis creation account and Enuma Elish.",
           "One God against many gods. Creation by word against creation after battle. Humans made in God's image with responsibility, against humans made to serve the gods. "
           "Other acceptable points: the sea is created and not a goddess; the sun and moon are lights, not gods."),
        PQ("Explain what is meant by the claim that Genesis 1 is a 'polemic' against other ancient views.",
           "A polemic is an argument against another view. The claim is that Genesis 1 uses a familiar story shape but denies pagan ideas: there is one God; the sea, sun and moon are made by him and are not gods; humans, not only kings, carry God's image. "
           "Critics say this reading goes beyond the text, which does not name any rival."),
        PQ("Assess the view that Israel's flood story came from Mesopotamia.",
           "Plan: similarities (boat, birds, sacrifice, mountain). Evidence for contact: older Mesopotamian texts and the exile. Differences: moral reason, one God, covenant. "
           "Alternative: both come from an older shared tradition. Judgement: a historical link is likely, but the theological message in Genesis is its own."),
        SUM("Genesis 1 to 11 is compared with Enuma Elish, Atrahasis, Gilgamesh and the Sumerian King List.",
            "Creation: similar sequence, very different theology (one God, creation by word, humans in God's image).",
            "Flood: very close details, but Genesis gives a moral reason and a covenant.",
            "Explanations: borrowing, common heritage, polemic.",
            "Good answers compare, then judge, and do not treat 'similar' as 'copied'."),
    ],
))

# ---------------------------------------------------------------------------
# 3. The patriarchal covenants
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The patriarchal covenants",
    title="The covenants with Abraham, Isaac and Jacob",
    slug="rsl1-patriarchal-covenants",
    minutes=23,
    summary="Follows God's promises of land, descendants and blessing from Abraham to Jacob, compares them with ancient covenant forms, and assesses the patriarchs as figures of history and faith.",
    objectives=[
        "Describe the covenant passages in Genesis 12, 15 and 17 and the promises they contain",
        "Explain how the promises are renewed with Isaac and Jacob",
        "Compare the patriarchal covenant with ancient Near Eastern treaty and grant forms",
        "Evaluate the debate on whether the patriarchal stories are history",
    ],
    key_concepts=["Covenant", "Promise of land and descendants", "Circumcision", "Faith and righteousness", "Royal grant", "God of the fathers"],
    blocks=[
        H("Introduction"),
        T("The word **patriarch** means 'father-ruler'. The patriarchs of Israel are Abraham, Isaac and Jacob. Their stories fill Genesis 12 to 50. "
          "At the centre of the stories is a **covenant**: a solemn, binding agreement between God and a person or people. "
          "The Board's report notes that candidates are asked about the patriarchs' religious beliefs, their roles, and the way Jacob was both in conflict and chosen. "
          "This lesson gives you the structure to answer such questions."),
        D("A solemn agreement or bond, usually sealed by an oath or a ritual. In the Old Testament, God's covenants with Noah, Abraham, Moses and David set up a relationship with promises and duties.", title="Covenant"),
        H("Abraham: the call and the promises"),
        T("In Genesis 12:1 to 3 God calls Abram to leave his homeland and go to a land God will show him. Three promises are made: a **land**, a great **nation** (many descendants), and **blessing**, including that through him all the families of the earth will be blessed. "
          "Abram goes, even though he is old and his wife Sarai has no child. The story shows faith as trust and obedience."),
        KEY("The three key covenant scenes", "Learn what happens in each.", cards=[
            ["Genesis 15", "God promises a son and descendants as many as the stars. Abram believes, and this is counted to him as righteousness (15:6). A ritual follows with animals cut in two; a smoking fire pot and torch pass between the pieces, which suggests that God alone takes the oath."],
            ["Genesis 17", "God appears again, calls himself El Shaddai, and makes an everlasting covenant. Names change: Abram becomes Abraham, Sarai becomes Sarah. Circumcision is given as the sign of the covenant."],
            ["Genesis 22", "Abraham is tested when told to offer Isaac. The test ends with God providing a ram, and the promises are confirmed. Jewish tradition calls it the Akedah, the binding."],
        ]),
        T("Notice the order. Genesis 12 is the call, 15 shows trust and the promise of a son, 17 gives the sign, 22 tests the faith. A good essay moves through them in order."),
        H("Isaac and Jacob"),
        T("The promises are handed on. God repeats them to **Isaac** in Genesis 26, during a famine, and tells him to stay in the land. "
          "To **Jacob**, who has fled from his brother Esau, the promise is renewed at Bethel in the dream of a ladder (Genesis 28). "
          "Later at the river Jabbok Jacob wrestles with a figure and is given the name **Israel** (Genesis 32). His twelve sons become the ancestors of the twelve tribes."),
        T("In each generation the child who inherits the covenant is not the child one would expect: Isaac rather than Ishmael, Jacob rather than Esau. "
          "This is why the Board's question on Jacob asked about his rejection and his being chosen. The text presents the choice as God's purpose, and Jacob's flawed character, including his deceit of Isaac, is not hidden."),
        H("Covenant forms in the ancient world"),
        T("Scholars compare the covenant with Abraham with documents from the ancient Near East. Two forms are important. A **suzerainty treaty** is made by a great king (the suzerain) with a weaker king (the vassal); the vassal promises loyalty and the king promises protection. "
          "A **royal grant** is a gift from a king to a loyal servant, often land, which is promised without conditions on the king's side. "
          "Moshe Weinfeld argued that the Abrahamic covenant resembles a grant and the Sinai covenant resembles a treaty. Other scholars think the comparison is too neat."),
        KEY("Conditional or unconditional?", "A standard evaluation point.", cards=[
            ["Unconditional features", "God alone passes between the pieces (Genesis 15). The promises are called everlasting (17)."],
            ["Conditional features", "Genesis 17 calls Abraham to walk before God and be blameless, and the sign of circumcision must be kept. Genesis 22:16 to 18 links the blessing to his obedience."],
        ]),
        H("The religion of the patriarchs"),
        T("The patriarchs build altars, call on God's name, and meet him in dreams and visits. They know God by names such as El Shaddai, El Elyon and 'the God of my father'. "
          "The German scholar Albrecht Alt (1929) argued that the patriarchs worshipped a family god, 'the God of the fathers', who guided a wandering family rather than being tied to a holy place. "
          "In Exodus 3 and 6 God makes himself known to Moses by the name Yahweh as the same God as the God of Abraham, Isaac and Jacob."),
        H("Are the patriarchs historical?"),
        T("Scholars are divided. In the early and middle 1900s William Albright and others thought that customs in the stories (such as adoption and inheritance practices) matched texts of the second millennium BC, supporting the stories' setting. "
          "Later scholars such as Thomas Thompson and John Van Seters argued that those parallels are weak and that the stories were shaped much later. "
          "Many believers affirm the stories as history and others treat them as faith traditions. For examination, state both views and the evidence."),
        EX("Worked example 1: the Abrahamic covenant in order", intro="Outline the main stages of God's covenant with Abraham.", steps=[
            S("Call and promise (Genesis 12)", text="God tells Abram to leave and promises land, nation and blessing for all families of the earth."),
            S("Faith and ritual (Genesis 15)", text="Abram believes God's promise of a son; the ritual of the animals confirms it."),
            S("Sign (Genesis 17)", text="The names change and circumcision is the sign of the everlasting covenant."),
            S("Test (Genesis 22)", text="Abraham obeys in the matter of Isaac and the promise is renewed."),
            S("Handed on", text="The promises pass to Isaac and Jacob."),
        ]),
        EX("Worked example 2: model plan on Jacob", intro="'Jacob was both rejected and chosen.' Explain this statement.", steps=[
            S("Rejected", text="He is the younger twin, he deceives his father and takes Esau's blessing, and he flees; his family relations are broken."),
            S("Chosen", text="At Bethel God renews the promise to him. At Jabbok he receives the name Israel."),
            S("Link to the twelve tribes", text="His twelve sons become the tribal ancestors."),
            S("Judgement", text="The story presents God's choice as grace, not as a reward for good behaviour."),
        ]),
        MISTAKE("Confusing the three covenant scenes", "Chapter 15 is the animal ritual and faith, chapter 17 is circumcision and the name changes, chapter 22 is the test. Match each scene to its main feature."),
        MISTAKE("Retelling the whole life of Abraham", "The Board's report says candidates narrate when they should explain significance. Use the stories as evidence for your argument about covenant and religion."),
        TIP("Exam link: the patriarchs belong to the Old Testament material in the report's Section 1.1 and have been the basis of essay questions on their beliefs and on Jacob. "
            "Structured questions ask for promises, signs and names. Always give the chapter if you are certain of it."),
        QUIZ("Which sign is given to Abraham in Genesis 17 as the mark of the covenant?",
             ["The rainbow", "Circumcision", "The Sabbath", "The Passover lamb"], 1,
             "Circumcision is the sign of the covenant with Abraham in Genesis 17.",
             feedback=["The rainbow is the sign of the covenant with Noah.", "", "The Sabbath is linked with the Sinai covenant in Exodus 31.", "The Passover belongs to the Exodus story."]),
        QUIZ("Where did Jacob dream of a ladder and receive the promise?",
             ["Jabbok", "Bethel", "Hebron", "Shechem"], 1,
             "Genesis 28 places the dream at Bethel. At the Jabbok he wrestled and received the name Israel.",
             feedback=["The Jabbok is where he wrestled and was renamed.", "", "Hebron is linked with Abraham and the burial of Sarah.", "Shechem is linked with Abraham's first altar and with Jacob's later dealings, not the ladder."]),
        PQ("List the three main promises made to Abraham in Genesis 12:1 to 3.",
           "Land, a great nation (many descendants), and blessing, including blessing for all the families of the earth through him."),
        PQ("Explain what scholars mean when they compare the Abrahamic covenant with a royal grant.",
           "A royal grant is a king's gift of land or reward to a loyal servant, with the king making the promise and few conditions on him. Scholars such as Weinfeld note that God alone passes between the animal pieces in Genesis 15, so the promise depends on God. "
           "Critics point to the call to obedience in Genesis 17 and 22, so the covenant has conditional features too."),
        PQ("Assess the view that the patriarchs are historical figures.",
           "For: the setting in the second millennium BC and customs that fit some texts of that time (Albright). Against: the stories were written down much later; parallels are not specific (Thompson, Van Seters); no direct evidence for the patriarchs. "
           "Judgement: certainty is impossible. The accounts are best treated as memories shaped by later faith, and believers may affirm them as history by faith."),
        SUM("The covenant with Abraham has three promises: land, nation and blessing (Genesis 12).",
            "Genesis 15 stresses faith and God's own oath, 17 the sign of circumcision and new names, 22 the test.",
            "The promises pass to Isaac and Jacob, who is renamed Israel.",
            "Comparisons with treaties and grants help explain the form, but scholars disagree.",
            "The historicity of the patriarchs is debated, so give both sides."),
    ],
))

# ---------------------------------------------------------------------------
# 4. The Exodus
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The Exodus",
    title="The Exodus: the story, the date, the evidence and the meaning",
    slug="rsl1-exodus",
    minutes=24,
    summary="Tells the Exodus in outline, sets out the early and late dates and the archaeological evidence, and explains why the event became the foundation of Israel's faith and memory.",
    objectives=[
        "Outline the Exodus events from the oppression in Egypt to the crossing of the sea",
        "Explain the early date and late date theories and the evidence for each",
        "Name the extrabiblical evidence and say what it can and cannot show",
        "Explain the religious significance of the Exodus for Israel",
    ],
    key_concepts=["Exodus", "Plagues", "Passover", "Early and late date", "Merneptah Stele", "Redemption"],
    blocks=[
        H("Introduction"),
        T("The **Exodus** is Israel's escape from slavery in Egypt, led by Moses. It is the story the Old Testament refers to most often when it speaks of what God has done for Israel. "
          "The Board's report records that many candidates narrate the story but fail to explain why it was so important. "
          "A good answer needs three things: the events, the historical debate, and the meaning."),
        D("The departure of the Israelites from Egypt under Moses, understood in the Old Testament as Yahweh's act of deliverance. The word comes from the Greek for 'going out'.", title="Exodus"),
        H("The story in outline"),
        T("The book of Exodus describes the Israelites oppressed by a Pharaoh who forces them into hard labour on building projects, including the store cities of Pithom and Raamses (Exodus 1:11). "
          "Moses is born, hidden, adopted into Pharaoh's house, and later flees to Midian after killing an Egyptian. "
          "At the burning bush (Exodus 3) God reveals the name Yahweh and sends Moses back to demand freedom. Pharaoh refuses, and ten plagues fall on Egypt. "
          "The last is the death of the firstborn, from which the Israelites are spared when they mark their doorposts with the blood of a lamb. This is the **Passover**. "
          "Pharaoh lets them go, then pursues them, and the Israelites cross the sea on dry ground while the Egyptian army is drowned (Exodus 14). "
          "They then travel to Mount Sinai."),
        KEY("Four stages", "Use these headings to plan an answer.", cards=[
            ["Oppression", "Forced labour and a command to kill Hebrew baby boys."],
            ["Call of Moses", "The burning bush, the name Yahweh, the signs and Aaron as spokesman."],
            ["Plagues and Passover", "Ten plagues; the Passover meal; the death of the firstborn."],
            ["Escape", "Departure, the sea crossing, the song of victory and the journey to Sinai."],
        ]),
        T("The sea is called *yam suph* in Hebrew. This is often translated 'Red Sea' but literally means 'sea of reeds', and scholars debate which body of water is meant. The route is uncertain."),
        H("When did it happen? Early and late date"),
        T("The Bible does not name the Pharaoh. This makes dating difficult. Two main dates are discussed."),
        KEY("Two dates", "Evidence for each.", cards=[
            ["Early date (about 1446 BC)", "First Kings 6:1 says that Solomon began the Temple 480 years after the Exodus. Solomon's fourth year is usually dated about 966 BC, which gives about 1446 BC. Judges 11:26 mentions 300 years from the conquest to Jephthah. This fits a reading of the numbers as literal."],
            ["Late date (about 1250 to 1200 BC)", "Raamses, the store city (Exodus 1:11), is linked to the city Pi-Ramesses built under Ramesses II in the 13th century BC. The 480 years may be a symbolic number (12 generations of 40 years)."],
        ]),
        T("The numbers differ again in the Bible itself: Exodus 12:40 gives 430 years in Egypt, while the Greek text and some traditions give another count. Many scholars also doubt that the story can be dated at all."),
        H("What does the evidence say?"),
        T("There is no Egyptian record that names Moses or describes the Exodus. Egyptian texts do record Semitic people living in the Delta, working as labourers and herders, and groups leaving and returning. "
          "The **Merneptah Stele** (about 1208 BC) is an Egyptian victory inscription that names 'Israel' among peoples in Canaan. It is the oldest known text outside the Bible that mentions Israel, and it shows that a people called Israel existed in Canaan by that time. It does not mention an exodus."),
        T("Scholars take different positions. Some find the biblical account basically historical, with a smaller group leaving Egypt. "
          "Others say a small group of escapees was the source of a memory later shared by all Israel. Some (often called minimalists) doubt that it happened as described. "
          "Another view is that Israel grew mainly from people already in Canaan. State the range of views, then explain which you find best supported."),
        H("Why the Exodus mattered"),
        KEY("Meaning of the Exodus for Israel", "This is what the Board's report asks candidates to stress.", cards=[
            ["God as redeemer", "Yahweh is known as the God who freed Israel. The Ten Commandments begin with this fact (Exodus 20:2)."],
            ["Birth of a people", "Slaves became a nation with a law, a covenant and a promised land."],
            ["Memory and worship", "The Passover is kept each year and parents tell children what God did. The Exodus is recalled in psalms and by prophets."],
            ["A pattern of hope", "Later exiles and prophets speak of a new exodus, a new deliverance."],
        ]),
        EX("Worked example 1: significance paragraph", intro="Explain why the Exodus was central to Israelite religion.", steps=[
            S("Point", text="It showed that Yahweh acts in history to save his people."),
            S("Evidence", text="The Passover festival and the opening of the Ten Commandments both look back to the deliverance."),
            S("Effect", text="It gave Israel its identity and its hope of the promised land."),
            S("Link back to the question", text="So any later threat, such as exile, is faced with the memory that God had saved them before."),
        ]),
        EX("Worked example 2: dating plan", intro="Compare the early date and the late date of the Exodus.", steps=[
            S("Early date", text="About 1446 BC from 1 Kings 6:1. Weakness: the 480 years may be symbolic, and there is little archaeological match."),
            S("Late date", text="About the 13th century BC, linked with Ramesses II and the store city Raamses. Weakness: the biblical numbers must be read symbolically."),
            S("Evidence outside the Bible", text="The Merneptah Stele shows Israel in Canaan by about 1208 BC. This is more consistent with the later date, but dating remains uncertain."),
            S("Judgement", text="The late date has more support among scholars, but the evidence does not settle it."),
        ]),
        MISTAKE("Saying that archaeology has proved or disproved the Exodus", "Neither has been proved. Archaeology gives context and some limits, such as the Merneptah Stele. Say what the evidence can support."),
        MISTAKE("Giving a long retelling of the plagues", "The report says candidates told the story and missed the significance. Spend at most a short paragraph on events, then explain what they meant."),
        TIP("Exam link: the Exodus has been a Paper 2 essay topic in the report's Section 1.1 and the report singles it out as a question where candidates did not stress importance. "
            "It can also appear as Paper 1 multiple choice (Passover, Moses, Merneptah Stele). Use dates with 'about'."),
        QUIZ("The Merneptah Stele is important because it:",
             ["Describes the plagues of Egypt", "Names Moses", "Is the oldest known text outside the Bible that mentions Israel", "Proves the date of the Exodus was 1446 BC"], 2,
             "It dates to about 1208 BC and names Israel among the peoples in Canaan. It does not mention the Exodus.",
             feedback=["It does not mention plagues.", "It does not name Moses.", "", "It does not give a date for the Exodus; it only shows Israel in Canaan by then."]),
        QUIZ("Which statement best shows the religious importance of the Exodus?",
             ["It proves that Egypt was a weak kingdom", "Yahweh is known as the God who redeemed Israel from slavery", "It explains why the Israelites became shepherds", "It gives the exact date of the Temple"], 1,
             "The Exodus shaped Israel's belief that Yahweh saves his people, which is why it is recalled in the Passover and the Commandments.",
             feedback=["The text gives a religious meaning, not a political history of Egypt.", "", "Israel's family had been shepherds long before.", "The Temple date is a different matter."]),
        PQ("Outline the events of the Passover night in Exodus 12.",
           "The Israelites are told to take a lamb for each household, kill it, put its blood on the doorposts, and eat the meal in haste, with unleavened bread. "
           "God passes over the houses marked with blood and the firstborn of Egypt die. Pharaoh then lets the people go. The festival is to be kept each year as a memorial."),
        PQ("State two arguments for the late date of the Exodus.",
           "The store city Raamses (Exodus 1:11) is linked with Pi-Ramesses built under Ramesses II in the 13th century BC. The Merneptah Stele shows Israel in Canaan by about 1208 BC, which fits a 13th-century setting. "),
        PQ("'The Exodus was the most important event in Israelite history.' Discuss.",
           "Plan: define the event briefly. For: God as redeemer; foundation for the covenant; the Passover; memory in psalms and prophets; hope of a new exodus. "
           "Against or other events: the covenant at Sinai, the monarchy, and the exile also shaped Israel. Historical debate: date and evidence uncertain, but the faith meaning is clear whatever the date. "
           "Judgement: it is the central saving event in the Old Testament memory, with Sinai as its completion."),
        SUM("The Exodus is Israel's liberation from slavery under Moses, with plagues, the Passover and the sea crossing.",
            "The early date is about 1446 BC and the late date about the 13th century BC. The Bible gives no Pharaoh's name.",
            "The Merneptah Stele shows Israel in Canaan about 1208 BC but does not mention the Exodus.",
            "Its meaning: God redeems, a people is born, the Passover is remembered, and later hope uses the pattern.",
            "Explain the significance; do not merely retell."),
    ],
))

# ---------------------------------------------------------------------------
# 5. The Mosaic covenant
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The Mosaic covenant",
    title="The Mosaic covenant at Sinai: law, treaty and community",
    slug="rsl1-mosaic-covenant",
    minutes=23,
    summary="Describes the covenant at Sinai in Exodus 19 to 24 and its renewal, the Decalogue and the Book of the Covenant, the treaty-form theory, and how the covenant shapes Israel's life.",
    objectives=[
        "Outline the making of the covenant in Exodus 19 to 24, and its breaking and renewal in 32 to 34",
        "Describe the Ten Commandments and the Book of the Covenant",
        "Explain the treaty-form comparison and the objections to it",
        "Compare the Mosaic covenant with the covenant with Abraham",
    ],
    key_concepts=["Sinai covenant", "Decalogue", "Book of the Covenant", "Suzerainty treaty", "Apodictic and casuistic law", "Holy nation"],
    blocks=[
        H("Introduction"),
        T("After the Exodus the Israelites reach **Mount Sinai** (also called Horeb in Deuteronomy). There God makes a covenant with the whole people through Moses. "
          "For the Old Testament this is the centre of Israel's religion. The covenant with Abraham was a promise to a family. The covenant at Sinai makes a nation with a law."),
        D("The agreement between Yahweh and Israel made at Sinai through Moses. Yahweh will be Israel's God and Israel will be his people, who must keep his commandments.", title="Mosaic covenant"),
        H("The making of the covenant"),
        T("In Exodus 19 God tells Moses what to say: if Israel obeys his voice and keeps his covenant, they will be his treasured possession, a **kingdom of priests** and a **holy nation** (19:5 to 6). "
          "The people agree. They prepare for three days, and God appears on the mountain with thunder, cloud and trumpet. "
          "Exodus 20 gives the **Ten Commandments**. Exodus 20:22 to 23:33 gives further laws, called the **Book of the Covenant**. "
          "In Exodus 24 the people say again that they will obey, Moses reads the book, sprinkles blood on the altar and the people, and the leaders eat a meal in God's presence."),
        KEY("The Decalogue in two parts", "Different traditions number the commandments differently. Check your textbook.", cards=[
            ["Duties to God", "No other gods; no image of God; do not misuse God's name; keep the Sabbath day holy."],
            ["Duties to people", "Honour father and mother; do not murder; do not commit adultery; do not steal; do not give false evidence; do not covet."],
        ]),
        T("Jews, Catholics and Lutherans, and Reformed Christians divide the commandments slightly differently, so the numbers (for instance which one is 'no other gods') are not the same in every textbook. "
          "The Commandments begin with God's act: 'I am Yahweh your God who brought you out of Egypt' (20:2). Law follows grace."),
        H("The Book of the Covenant"),
        T("This collection includes laws about slaves, injury, property, justice for the poor, protection of strangers and widows, and the annual festivals. "
          "Scholar Albrecht Alt divided Old Testament laws into two types. **Apodictic law** gives commands without conditions: 'You shall not kill.' **Casuistic law** gives cases: 'If a man steals an ox and kills it...' with a set penalty. "
          "The casuistic laws are similar in form to other ancient Near Eastern law codes such as the Code of Hammurabi, while the apodictic commands are more distinctive of Israel. Some scholars argue Alt's contrast is too sharp."),
        H("Covenant and treaty"),
        T("In 1954 George Mendenhall compared the Sinai covenant with the **suzerainty treaties** of the Hittite empire, made between about 1400 and 1200 BC. These treaties had a regular form. Many scholars find the same pattern in Exodus 20 and in Deuteronomy."),
        KEY("Treaty parts and Sinai", "Learn the match.", cards=[
            ["Preamble", "The great king names himself: 'I am Yahweh your God' (Exodus 20:2)."],
            ["Historical prologue", "What the king has done: 'who brought you out of Egypt'."],
            ["Stipulations", "The commands: the Decalogue and the Book of the Covenant."],
            ["Document and witnesses", "The tablets placed in the ark; heaven and earth called as witnesses (clearly in Deuteronomy)."],
            ["Blessings and curses", "Rewards for obedience and punishment for disobedience, set out most fully in Leviticus 26 and Deuteronomy 28."],
        ]),
        T("Objections: the Exodus form is not identical to Hittite treaties; later Assyrian treaties are closer to Deuteronomy, so the model may not prove an early date; and the covenant is more than a legal treaty because it is also a relationship. "
          "Even so, the treaty comparison helps students see why loyalty and exclusive worship are so central."),
        H("Breaking and renewal"),
        T("While Moses is on the mountain the people make a golden calf (Exodus 32). Moses breaks the tablets, intercedes for the people, and God forgives. "
          "In Exodus 34 the covenant is renewed with new tablets, and God describes himself as merciful and gracious, slow to anger and rich in steadfast love. "
          "This shows that the covenant can be broken by Israel and yet is renewed by God's mercy."),
        H("Mosaic and Abrahamic covenants compared"),
        KEY("Compare", "Use this table-style comparison in an essay.", cards=[
            ["Partners", "Abraham: a family and promise. Moses: a whole people at Sinai."],
            ["Main content", "Abraham: promises of land, descendants, blessing. Moses: law and obligations as well as promise."],
            ["Sign", "Abraham: circumcision. Moses: the Sabbath is called a sign (Exodus 31:13 to 17) and the tablets and ark are signs of the relationship."],
            ["Conditions", "Abraham: mostly promise. Moses: 'if you obey' (19:5) with blessings and curses."],
        ]),
        EX("Worked example 1: the covenant scene", intro="Describe the sealing of the covenant in Exodus 24.", steps=[
            S("Reading", text="Moses writes down the words of Yahweh and reads the book of the covenant to the people."),
            S("Response", text="The people say that all that Yahweh has spoken they will do."),
            S("Ritual", text="Moses sprinkles half the blood of the sacrificed animals on the altar and half on the people, binding both sides."),
            S("Meal", text="Moses, Aaron and seventy elders go up, see the God of Israel and eat and drink."),
        ]),
        EX("Worked example 2: model plan", intro="'The Sinai covenant was the most important event in Israel's history.' Discuss.", steps=[
            S("For", text="It gave Israel law and identity; it gave the picture of Israel as a holy nation; the Ten Commandments continue to shape later ethics."),
            S("Against", text="The Exodus came first and caused it; the promise to Abraham gave the land; the Davidic covenant gave hope for the future."),
            S("Evaluate", text="Many Old Testament writers return to Sinai when they speak of sin and repentance, so its place is central."),
            S("Judgement", text="Sinai is the core of Israel's religion, but is best read together with the Exodus before it and the promises to Abraham behind it."),
        ]),
        MISTAKE("Saying the law earned God's favour", "The text puts God's saving act first (Exodus 20:2). Obedience is the response to what God has already done."),
        MISTAKE("Listing the commandments without grouping or comment", "Group them into duties to God and to others and say what each group shows about the covenant community."),
        TIP("Exam link: expect structured questions on the content of the Decalogue and essay questions on covenant ideas, comparing Abraham and Moses. Use 'about' for dates and mention that numbering differs across traditions."),
        QUIZ("Which feature belongs to the treaty form that scholars find in Exodus 20?",
             ["A historical prologue recalling what the king has done", "A list of kings", "A genealogy of the high priests", "A calendar of festivals"], 0,
             "The words 'who brought you out of Egypt' play the part of the historical prologue in a suzerainty treaty.",
             feedback=["", "King lists are a different type of text.", "Genealogies are not a treaty part.", "Festival calendars appear in the laws, but are not part of the treaty pattern."]),
        QUIZ("What does 'apodictic law' mean?",
             ["A law in 'if... then' case form", "A command given without conditions", "A law only about priests", "A Babylonian law code"], 1,
             "Apodictic law is an unconditional command, such as 'You shall not steal'. Case law is called casuistic.",
             feedback=["That is casuistic law.", "", "Apodictic law is a form, not a topic.", "The term describes a form of law, not a particular code."]),
        PQ("State four commandments that deal with duties to other people.",
           "Honour father and mother; do not murder; do not commit adultery; do not steal; do not give false evidence; do not covet. Any four earn the marks."),
        PQ("Explain how the golden calf incident tested the covenant.",
           "While Moses was on Sinai the people made a calf of gold and worshipped it, breaking the first commandments. Moses broke the tablets, interceded, and the people were punished. "
           "God forgave and renewed the covenant (Exodus 34) with new tablets. It shows the covenant could be broken and shows God's mercy."),
        PQ("Compare the Mosaic covenant with the covenant made with Abraham.",
           "Similarities: both start from God's initiative and both involve a people and a land. Differences: Abraham's covenant is mainly promise to a family with circumcision as sign; Moses' covenant is made with a nation and gives law with blessings and curses, with 'if you obey' language. "
           "Evaluation: scholars compare Abraham's with a royal grant and Moses' with a treaty, but both have conditional and unconditional features."),
        SUM("The Sinai covenant (Exodus 19 to 24) makes Israel a holy nation under Yahweh's law.",
            "It includes the Ten Commandments and the Book of the Covenant, sealed with a reading and blood.",
            "Mendenhall compared it with Hittite treaties; there are objections.",
            "The people broke it with the golden calf; God renewed it in Exodus 34.",
            "Compare with Abraham: promise to a family against law for a nation."),
    ],
))

# ---------------------------------------------------------------------------
# 6. The Holiness Code
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M1, topic="The Holiness Code",
    title="The Holiness Code: Leviticus 17 to 26 and what holiness means",
    slug="rsl1-holiness-code",
    minutes=22,
    summary="Introduces the Holiness Code, its contents and its call to be holy as God is holy, shows how ritual and moral laws are joined, and evaluates the debate on its origin and relevance.",
    objectives=[
        "Say what the Holiness Code is, where it is, and how it got its name",
        "Describe its main contents chapter by chapter",
        "Explain the idea of holiness as separation and as ethical living",
        "Evaluate the debate on its date and on how it relates to the Priestly source",
    ],
    key_concepts=["Holiness Code", "Holy", "Clean and unclean", "Sabbatical year and Jubilee", "Love of neighbour", "Blessings and curses"],
    blocks=[
        H("Introduction"),
        T("Leviticus is the third book of the Pentateuch and is mostly about worship and holiness. Within it, chapters 17 to 26 form a block which the German scholar August Klostermann named the **Holiness Code** in 1877. "
          "The name comes from the repeated call: 'Be holy, for I Yahweh your God am holy' (Leviticus 19:2). "
          "This code joins laws about worship, family life, food, farming and social justice in one message: the people of God must be different because their God is different."),
        D("The block of laws in Leviticus 17 to 26 which calls Israel to holiness. It mixes ritual rules with moral and social ones and ends with blessings and curses.", title="Holiness Code"),
        D("To be **holy** is to be set apart for God. In the Old Testament holiness belongs first to God and then to people, places, times and objects that are set apart for him. It includes ritual purity and moral conduct.", title="Holiness"),
        H("Contents"),
        KEY("Main chapters", "Use this map to recall the code.", cards=[
            ["17 and 18", "Sacrifice must be at the sanctuary and blood is not to be eaten, because life is in the blood. Chapter 18 sets out rules on family and sexual relations, forbidding the practices of Egypt and Canaan."],
            ["19", "The heart of the code. A mix of duties: honour parents, keep the Sabbaths, leave part of the harvest for the poor and the foreigner, use honest weights, do not oppress workers, do not slander. Love your neighbour as yourself (19:18). Treat the foreigner as a native and love him (19:33 to 34)."],
            ["20", "Penalties for serious offences listed in earlier chapters."],
            ["21 and 22", "Special rules for priests and for the holy offerings."],
            ["23", "The calendar of festivals: Sabbath, Passover, Weeks, Trumpets, Day of Atonement, Tabernacles."],
            ["24", "Lamp and bread in the sanctuary, and the case of blasphemy."],
            ["25", "The Sabbatical year (every seventh year the land rests) and the Jubilee (the fiftieth year: land returns to the original family and slaves are freed)."],
            ["26", "Blessings for keeping the covenant and curses for breaking it."],
        ]),
        H("Holiness in practice"),
        T("Three ideas run through the code. First, **separation**: Israel must not copy the practices of the nations around it. Second, **purity**: things and people are clean or unclean. "
          "Uncleanness is not the same as sin. It can come from childbirth or contact with a dead body and is removed by washing and waiting. Third, **ethical holiness**: chapter 19 moves between a rule about mixing crops and a rule about justice for the poor without any break, which suggests that ritual and social duty were not separate in the writer's mind."),
        T("The Sabbatical year and the Jubilee express the belief that the land belongs to God (25:23) and that Israelites are tenants. The aim is to protect families from permanent poverty and loss of land. "
          "There is little evidence that the Jubilee was ever fully practised, and scholars debate whether it was a real law or an ideal."),
        H("Origin and date"),
        T("Klostermann saw the code as a separate law-book. Wellhausen included it in the P source, as an older collection later taken into P. "
          "Some modern scholars, such as Israel Knohl and Jacob Milgrom, argue that the Holiness material (called H) is a distinct layer or school close to P but with its own interests, and that it may be later than the main P material or may be its editor. "
          "Others say the dating is too uncertain, and the debate is open. Notice how the Day of Atonement ritual (Leviticus 16) sits just before the code, and the festival calendar in chapter 23 is inside it."),
        KEY("Why does the date matter?", "It affects how you read the book.", cards=[
            ["Early date", "The laws may reflect life before the monarchy, with Moses as the lawgiver."],
            ["Late date", "The code may come from priests in or after the exile, shaping a community without a king."],
        ]),
        EX("Worked example 1: ethical holiness in Leviticus 19", intro="Give three examples from Leviticus 19 that show holiness includes social justice.", steps=[
            S("Gleaning", text="Farmers must leave the edges of their field and the fallen grain for the poor and the foreigner."),
            S("Fair dealing", text="Do not use dishonest scales or weights, do not hold back a worker's wages, do not cheat."),
            S("Neighbour and foreigner", text="Love your neighbour as yourself; treat the stranger as a native and love him as yourself."),
            S("Link", text="Each is justified by the refrain 'I am Yahweh', so ethics are part of holiness."),
        ]),
        EX("Worked example 2: model plan", intro="'The Holiness Code is mainly about ritual, not about morality.' Discuss.", steps=[
            S("For", text="Many laws concern sacrifice, priests, clean and unclean things and festivals."),
            S("Against", text="Chapter 19 mixes ritual and moral commands; chapter 25 deals with poverty, land and slavery; love of neighbour and the foreigner is central."),
            S("Evaluation", text="The writers did not sharply separate religion from daily life. Later prophets and Jesus' sayings also join them, though each does it in its own way."),
            S("Judgement", text="The statement is one-sided. Holiness here means both ritual purity and just behaviour."),
        ]),
        MISTAKE("Treating 'unclean' as 'sinful'", "Many cases of uncleanness, such as childbirth or burial of a relative, were not sins. They were states that required separation and cleansing."),
        MISTAKE("Reading the laws as only about Israel in the past", "Scholars and believers disagree on what applies today, so say 'Jews and Christians differ on how these laws apply' instead of stating one view."),
        TIP("Exam link: this topic suits Paper 1 multiple choice (Sabbatical year, Jubilee, 'Be holy') and structured questions on holiness and social ethics. "
            "Check with your teacher how closely the Board's syllabus examines it, since the report does not list it separately."),
        QUIZ("Which command from the Holiness Code is often called the summary of the neighbour laws?",
             ["Do not boil a kid in its mother's milk", "Love your neighbour as yourself", "Do not make idols", "Observe the Passover"], 1,
             "Leviticus 19:18 is the command to love your neighbour as yourself.",
             feedback=["That law is found elsewhere in the Pentateuch and is not the summary of the neighbour laws.", "", "That belongs to the Decalogue.", "The Passover is part of the festival calendar in chapter 23, but is not the summary of neighbour laws."]),
        QUIZ("What was the purpose of the Jubilee?",
             ["To give priests a holiday", "To change the date of the new year", "To return land to the original families and free slaves", "To end the sacrifices"], 2,
             "In the fiftieth year land returned to the family it was assigned to and Israelite slaves were released, protecting families from permanent loss.",
             feedback=["The Jubilee is a social law, not a priestly holiday.", "The festival calendar is separate.", "", "It did not end sacrifice."]),
        PQ("State three subjects covered in Leviticus 19.",
           "Honour for parents and the Sabbath; leaving part of the harvest for the poor and foreigner; honest weights and measures; justice and fairness; not slandering; love of neighbour; love of the foreigner. Any three."),
        PQ("Explain what the Old Testament means by holiness.",
           "Holiness means being set apart for God. God is holy first; Israel is called to be holy because he is. It includes ritual purity (clean and unclean, offerings, times and places) and moral living (justice, honesty, care for the poor). "
           "The call 'be holy for I am holy' shows the link between God's character and the behaviour of his people."),
        PQ("Assess the view that the Holiness Code is a separate collection from the Priestly source.",
           "For: its own refrain 'I am Yahweh your God', its preaching style, its blessings and curses and its stress on the whole people, not just on priests. Against: it shares vocabulary and interests with P and is placed within Leviticus. "
           "Scholars such as Knohl and Milgrom treat H as a layer of the priestly school. Judgement: it looks like a distinct stage within the priestly tradition, though the exact relationship is debated."),
        SUM("The Holiness Code is Leviticus 17 to 26, named by Klostermann.",
            "Its key text is 'Be holy, for I am holy' (19:2).",
            "It joins ritual and moral law: sacrifice, family rules, festivals, justice, Sabbatical year and Jubilee.",
            "Uncleanness is not the same as sin.",
            "Scholars debate whether it is a separate code, a layer of P, and how early it is."),
    ],
))

# ---------------------------------------------------------------------------
# 7. From the judges to the monarchy
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="From the judges to the monarchy",
    title="From the tribal league and the judges to the monarchy",
    slug="rsl1-judges-to-monarchy",
    minutes=24,
    summary="Describes the tribal confederacy and the judges, the Philistine crisis and the demand for a king, the two attitudes to monarchy in 1 Samuel, and the debate on Noth's amphictyony theory.",
    objectives=[
        "Describe the political and religious roles of the judges",
        "Explain the cycle in the book of Judges and the main judges",
        "Explain why Israel asked for a king and the two views of monarchy in 1 Samuel",
        "Evaluate the amphictyony theory of the tribal league",
    ],
    key_concepts=["Tribal confederacy", "Amphictyony", "Judge", "Charismatic leader", "Philistines", "Kingship"],
    blocks=[
        H("Introduction"),
        T("After the conquest and settlement of Canaan, Israel was not ruled by a king. Twelve tribes lived in their own areas and met in times of danger or worship. This period, roughly 1200 to 1050 BC, is called the **period of the judges**. "
          "The Board's report records that many candidates did not know the judges and failed to bring out their political and religious roles, and that others wrote only about Saul's weakness without explaining how the tribal system worked. "
          "This lesson fills those gaps."),
        D("A leader raised up in the book of Judges to deliver Israel from enemies and to guide the tribes. The word means one who rules, saves and settles disputes. Judges were not kings and did not found dynasties.", title="Judge"),
        D("A leader whose authority rests on a sudden gift of God's spirit and his own personal qualities, not on office or inheritance. Most of the judges are described this way.", title="Charismatic leader"),
        H("The tribal league"),
        T("In 1930 the German scholar Martin Noth argued that early Israel was an **amphictyony**, a sacred league of twelve tribes grouped around a shared sanctuary, as were some leagues in ancient Greece and Italy. "
          "Each tribe took turns to look after the central shrine, and tribes joined for war and worship. The ark and the sanctuary at Shiloh are the centre in this view."),
        KEY("Strengths and weaknesses of the amphictyony theory", "Evaluation points.", cards=[
            ["Support", "Twelve-tribe lists; Shiloh and the ark as a centre; the tribes' common worship of Yahweh; Judges 20 and 21 shows the tribes acting together."],
            ["Criticism", "The Greek and Italian leagues may not be a good model; the twelve tribes are not named identically in all lists; some stories show tribes acting alone or not at all (Judges 5 criticises tribes that stayed away). Many scholars now prefer 'confederacy' or 'tribal society' to 'amphictyony'."],
        ]),
        H("The judges and the cycle"),
        T("The book of Judges is written in a pattern. First Israel does evil by worshipping other gods. Then Yahweh gives them into the power of an enemy. Then Israel cries to Yahweh. Then a judge delivers them and the land has rest. Then the judge dies and the cycle begins again. "
          "This pattern is the work of the Deuteronomistic editors, who used old stories to teach that disobedience leads to disaster."),
        KEY("Judges to know", "Learn name, enemy and a detail.", cards=[
            ["Othniel, Ehud", "Othniel defeats a king from the north; Ehud kills the king of Moab, Eglon, and frees the people."],
            ["Deborah and Barak", "Deborah is a prophetess and judge. Barak leads the army and the Canaanite commander Sisera is killed by Jael (Judges 4 and 5). Judges 5 is a very old poem."],
            ["Gideon", "Defeats the Midianites with three hundred men. He refuses to be king ('Yahweh will rule over you', 8:23), but his son Abimelech later makes himself king at Shechem."],
            ["Jephthah and Samson", "Jephthah defeats the Ammonites and makes a tragic vow. Samson, a Nazirite, fights the Philistines."],
        ]),
        T("The refrain 'in those days there was no king in Israel; everyone did what was right in their own eyes' (Judges 17:6 and 21:25) can be read as supporting monarchy. "
          "Judges also lists minor judges, who are mentioned only briefly, such as Tola and Jair."),
        H("The crisis and the demand for a king"),
        T("The Philistines, a people from the coast with iron weapons and organised armies, pressed on the tribes. At the battle of Aphek, Israel lost, the ark was captured, and the sanctuary at Shiloh was probably destroyed (1 Samuel 4). "
          "Eli's sons were corrupt and Samuel's sons took bribes (1 Samuel 8:3). Samuel was priest, prophet and judge, and was the bridge to the new age. "
          "The elders came to Samuel and asked for a king 'like all the nations' (1 Samuel 8:5)."),
        KEY("Two attitudes to kingship in 1 Samuel", "Many scholars see two strands in the text.", cards=[
            ["Against the king", "1 Samuel 8: asking for a king is a rejection of Yahweh's rule. Samuel warns of conscription, forced labour and taxes. 1 Samuel 12 also warns. Some scholars link these to later critics who had seen what kings did."],
            ["For the king", "1 Samuel 9 and 10:1 to 16: Yahweh himself tells Samuel to anoint Saul to save his people from the Philistines. Chapter 11 shows Saul as a deliverer."],
        ]),
        T("A careful answer does not decide for one strand but notes that the monarchy was both needed (the political and military crisis) and feared (it could replace trust in Yahweh with trust in a human ruler)."),
        EX("Worked example 1: political and religious roles of judges", intro="Describe the roles of the judges in Israel.", steps=[
            S("Military", text="They led the tribes against oppressors: Ehud against Moab, Deborah and Barak against Canaanites, Gideon against Midian."),
            S("Judicial", text="Deborah sat under a palm tree and the people came to her for judgement (Judges 4:5). Samuel travelled to judge in a circuit."),
            S("Religious", text="They called Israel back to Yahweh; Samuel offered sacrifice and spoke as a prophet."),
            S("Limits", text="Their authority was personal and temporary. Most had control over only some tribes and left no successor."),
        ]),
        EX("Worked example 2: model plan", intro="Why did Israel ask for a king?", steps=[
            S("Military pressure", text="The Philistine victories, the loss of the ark, and a need for a permanent army."),
            S("Failure of leadership", text="Eli's sons and Samuel's sons were corrupt; the judges had no successors."),
            S("Wish to be like others", text="The elders wanted a king 'like all the nations'."),
            S("Religious risk", text="Samuel and the text see it as a rejection of Yahweh's kingship unless the king stays under God's law."),
        ]),
        MISTAKE("Mixing up the judges with the kings", "Judges were deliverers and judges with no dynasty. Kings began with Saul. Do not call Samson or Gideon kings."),
        MISTAKE("Describing the confederacy as a government with a capital and laws", "It was a loose bond of tribes held by religion and common danger. Explain how it worked and why it was too weak against the Philistines."),
        TIP("Exam link: the report's Section 1.1 (the Patriarchs to David) includes essay questions on the judges and the confederacy. It says candidates could not name the leaders or explain the political side, so learn names, enemies and roles."),
        QUIZ("Which judge was a prophetess who judged Israel under a palm tree?",
             ["Gideon", "Deborah", "Samson", "Jephthah"], 1,
             "Deborah judged from under a palm tree between Ramah and Bethel (Judges 4:4 to 5).",
             feedback=["Gideon defeated the Midianites.", "", "Samson was a Nazirite who fought the Philistines.", "Jephthah defeated the Ammonites."]),
        QUIZ("What is the 'amphictyony' theory?",
             ["That early Israel was an absolute monarchy", "That the twelve tribes formed a sacred league around a shared sanctuary", "That Israel was ruled by Philistines", "That the judges wrote the Pentateuch"], 1,
             "Martin Noth proposed that the tribes formed a league like some Greek and Italian leagues, centred on a sanctuary such as Shiloh.",
             feedback=["The period before Saul had no king.", "", "The Philistines were enemies, not rulers of Israel.", "It is a theory about political and religious structure."]),
        PQ("Outline the cycle found in the book of Judges.",
           "Israel sins by worshipping other gods; Yahweh allows an enemy to oppress them; the people cry out; Yahweh raises up a judge who delivers them; the land has rest; the judge dies and Israel sins again."),
        PQ("Explain two reasons why the tribal league was weak against the Philistines.",
           "There was no central ruler or standing army, so tribes came together only in crisis. The judges' authority was personal and short, and some tribes did not respond (Judges 5). The Philistines had organised armies and iron weapons. "
           "The loss of the ark at Aphek shook the religious unity."),
        PQ("Assess the view that Israel's monarchy was a rejection of Yahweh.",
           "For: 1 Samuel 8 says the people have rejected Yahweh as their king; Samuel warns of the demands of a king; Gideon's refusal expresses the ideal. Against: 1 Samuel 9 to 11 shows Yahweh choosing Saul to deliver the people; the monarchy was a response to a real threat; David and Solomon are later seen as agents of Yahweh. "
           "Judgement: the text holds both views. Kingship was acceptable if the king obeyed Yahweh and did not become a tyrant."),
        SUM("The period of the judges (about 1200 to 1050 BC) was a time of tribal league and charismatic deliverers.",
            "Noth's amphictyony is a theory with strong criticisms.",
            "Judges follows a cycle: sin, oppression, cry, deliverer, rest.",
            "The Philistine crisis and corruption of Eli's and Samuel's sons led to the demand for a king.",
            "1 Samuel contains both pro-monarchy and anti-monarchy attitudes."),
    ],
))

# ---------------------------------------------------------------------------
# 8. Saul
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Saul",
    title="Saul, the first king: achievements, rejection and assessment",
    slug="rsl1-saul",
    minutes=22,
    summary="Follows Saul from his anointing to his death at Gilboa, weighs his political and military achievements against the reasons given for his rejection, and shows how to assess him fairly.",
    objectives=[
        "Describe how Saul became king and what he achieved",
        "Explain the two stories of Saul's rejection and their reasons",
        "Describe the end of his reign, including his relationship with David and his death at Gilboa",
        "Give a balanced theological and political assessment of Saul",
    ],
    key_concepts=["Anointing", "Charismatic kingship", "Gibeah", "Rejection of Saul", "Holy war", "Gilboa"],
    blocks=[
        H("Introduction"),
        T("**Saul** son of Kish, from the tribe of Benjamin, was Israel's first king, about 1050 to 1010 BC (check your textbook for exact dates). "
          "The books of Samuel tell his story in sympathetic and critical tones. The Board's report notes that many candidates wrote only about Saul's weaknesses and rejection and did not show how the shift from confederacy to monarchy worked. "
          "A balanced answer covers both what Saul did and why the text says he lost his kingdom."),
        D("To pour oil on a person to set him apart for a special task from God. Saul, David and later kings were anointed. The word 'Messiah' means 'anointed one'.", title="Anointing"),
        H("Becoming king"),
        T("Saul was searching for lost donkeys when he met Samuel, who was told by Yahweh that this was the man to rule Israel (1 Samuel 9). Samuel anointed him privately. "
          "At Mizpah the tribes chose the king by lot and the lot fell on Saul (10:17 to 24). He was tall, and hid among the baggage. "
          "The decisive moment came when the Ammonites besieged Jabesh-gilead. The spirit of God came on Saul, he summoned the tribes by sending pieces of a pair of oxen, and he won a victory (chapter 11). "
          "At Gilgal the kingdom was confirmed."),
        H("His reign"),
        T("Saul's court was simple. He ruled from his own town, Gibeah, with a small standing army under his cousin Abner. His son Jonathan was a brave commander. "
          "There was no large palace or tax system. Saul fought the Philistines, Moab, Ammon, Edom, the king of Zobah and the Amalekites (1 Samuel 14:47 to 48). "
          "He broke Philistine control in parts of the hill country but did not defeat them, and the battles continued."),
        KEY("Saul's achievements", "Give these in an assessment before the failures.", cards=[
            ["Unity", "He drew the tribes together in war and made a beginning of national leadership."],
            ["Defence", "He relieved Jabesh-gilead and fought on all borders, keeping the Philistines out of much of the hill country."],
            ["Foundation", "He set up a standing force and a royal centre, which David used and developed."],
        ]),
        H("The rejection of Saul"),
        T("Two stories explain why Yahweh rejected Saul."),
        KEY("Two failures", "Know both stories and the issue in each.", cards=[
            ["Gilgal (1 Samuel 13)", "Saul was to wait seven days for Samuel to offer sacrifice before battle. With his army deserting and Samuel late, Saul offered the burnt offering himself. Samuel told him that his kingdom would not last. The issue: Saul took on a priestly role and did not wait on the word of the prophet."],
            ["Amalek (1 Samuel 15)", "Saul was told to put the Amalekites and their possessions under the ban. He spared their king Agag and kept the best of the animals. Samuel says that obedience is better than sacrifice, and that rebellion is as bad as the sin of divination. Samuel tells him Yahweh has rejected him."],
        ]),
        T("Notice that in both stories the main issue is **obedience to the word of Yahweh given through the prophet**. This tells us how the writers saw kingship: the king must obey Yahweh and does not have absolute power. "
          "Modern readers often find the command about Amalek troubling, and many believers and scholars discuss the ethics of the 'ban' in the ancient setting."),
        H("Saul and David; the end"),
        T("David, anointed in secret by Samuel (chapter 16), came to Saul's court as a musician, and then as a commander after he killed Goliath. Saul's jealousy grew when the women sang that David had killed ten thousands (18:7). "
          "Saul tried to kill David, who fled, and for years Saul pursued him. David twice spared Saul's life (chapters 24 and 26). "
          "Saul's mental state is described as being troubled by an evil spirit. Before his last battle Saul, in fear, visited a medium at Endor (chapter 28), though he had banned such practices. "
          "At Mount Gilboa the Philistines defeated Israel; Jonathan and two other sons were killed and Saul died by falling on his sword (chapter 31). David's lament over Saul and Jonathan (2 Samuel 1) is generous and shows respect for the 'Lord's anointed'."),
        H("Assessing Saul"),
        T("Writers of the books of Samuel set out the events in a way that favours David. A fair assessment weighs two sides."),
        KEY("Two views of Saul", "Balance them.", cards=[
            ["Failed king", "Disobedient, impulsive, jealous and unstable; did not defeat the Philistines; died in defeat; his dynasty did not continue."],
            ["Tragic founder", "Faced a hard political and military situation; started the monarchy; was a genuine deliverer in his early years; his bravery is clear at the end. Some scholars see him as a charismatic leader who was between the judges and a full state."],
        ]),
        EX("Worked example 1: the rejection stories", intro="Compare the two accounts of Saul's rejection.", steps=[
            S("Gilgal", text="Saul offers the sacrifice himself when Samuel is late; the sin is impatience and wrongly taking a priestly role."),
            S("Amalek", text="Saul spares Agag and the best animals; the sin is partial obedience to a divine command."),
            S("Common point", text="In both cases he acts on his own judgement, under pressure from the army, and not on the word through the prophet."),
            S("Result", text="Samuel declares that the kingdom will be taken from him and Saul keeps his throne but loses divine favour."),
        ]),
        EX("Worked example 2: model plan", intro="Assess the achievements and failures of Saul.", steps=[
            S("Introduction", text="Dates, tribe, role as first king; judgement previewed."),
            S("Achievements", text="Jabesh-gilead; wars on all fronts; standing army; Jonathan and Abner; first beginning of unity."),
            S("Failures", text="Gilgal; Amalek; jealousy of David; use of the medium at Endor; death at Gilboa and the Philistine victory."),
            S("Context", text="He ruled in a hard time, with no model of a king; the writers favour David."),
            S("Judgement", text="Saul was a flawed but important founder. His rejection explains why the monarchy needed obedience to God."),
        ]),
        MISTAKE("Describing only Saul's sins", "The report says many answers dwelt on weaknesses only. Include his military successes, his place in the move from confederacy to monarchy, and the political setting."),
        MISTAKE("Confusing Gilgal and Amalek", "Gilgal (chapter 13): the unauthorised sacrifice. Amalek (chapter 15): sparing Agag and the animals. Do not swap them."),
        TIP("Exam link: Saul belongs to Section 1.1 of the report's Old Testament paper (the confederacy, his rise and rejection). Structure an answer as rise, achievements, rejection and assessment."),
        QUIZ("Why did Samuel say Saul would lose his kingdom at Gilgal?",
             ["He refused to fight the Philistines", "He offered the sacrifice himself instead of waiting for Samuel", "He spared Agag", "He married a foreign princess"], 1,
             "In 1 Samuel 13 Saul made the burnt offering before Samuel arrived, which Samuel counted as disobedience.",
             feedback=["Saul did fight the Philistines.", "", "Sparing Agag belongs to the Amalek story in chapter 15.", "This is a charge made against Solomon, not Saul."]),
        QUIZ("Where did Saul and his sons die?",
             ["Mount Carmel", "Mount Gilboa", "Mount Sinai", "Mount Moriah"], 1,
             "The Philistines defeated Israel at Mount Gilboa (1 Samuel 31).",
             feedback=["Mount Carmel is linked with Elijah.", "", "Sinai is where the covenant was made.", "Moriah is linked with Abraham and Isaac, and later with the Temple."]),
        PQ("State three achievements of Saul as king.",
           "He delivered Jabesh-gilead from the Ammonites; he fought the Philistines and other neighbours; he built a standing army with Abner and Jonathan; he began to unify the tribes and was accepted as king. Any three."),
        PQ("Why did Samuel say that 'to obey is better than sacrifice' in the Amalek story?",
           "Saul had spared Agag and the best animals and said they were for sacrifice. Samuel says that Yahweh wants obedience to his word more than offerings. The point is that the king is under God's command and cannot excuse disobedience with religious activity."),
        PQ("Assess the view that Saul failed as Israel's first king.",
           "For: his two disobediences, his jealousy and attempts to kill David, his reliance on a medium, the defeat at Gilboa and the loss of his dynasty. Against: he was chosen in a crisis, he delivered Jabesh-gilead and fought on many fronts, started the standing army, and showed courage at the end; the account is written from David's side. "
           "Judgement: he did fail in the writers' judgement, but his reign was a necessary first stage."),
        SUM("Saul, from Benjamin, was chosen by lot and proved himself at Jabesh-gilead.",
            "He ruled from Gibeah with a small army and fought many enemies.",
            "He was rejected for impatience at Gilgal and partial obedience at Amalek.",
            "Jealousy of David and the visit to Endor mark his decline, and he died at Gilboa.",
            "A good assessment weighs achievement and failure and the bias of the sources."),
    ],
))

# ---------------------------------------------------------------------------
# 9. David and the Davidic covenant
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="David and the Davidic covenant",
    title="David: king, sinner and the promise of an everlasting house",
    slug="rsl1-david-davidic-covenant",
    minutes=25,
    summary="Traces David's rise, his capture of Jerusalem and the ark, the Davidic covenant of 2 Samuel 7, his great sin and its results, and assesses why he is both a flawed man and a model king.",
    objectives=[
        "Outline David's rise from Bethlehem to king of all Israel",
        "Explain why Jerusalem and the ark mattered",
        "Explain the terms of the Davidic covenant in 2 Samuel 7 and later reflection on it",
        "Assess David's weaknesses and why he is still seen as faithful to God",
    ],
    key_concepts=["Davidic covenant", "Nathan's oracle", "Jerusalem", "Ark of the covenant", "Bathsheba and Uriah", "Messianic hope"],
    blocks=[
        H("Introduction"),
        T("**David**, who reigned about 1010 to 970 BC (check your textbook for dates), is the most important king in the Old Testament. "
          "The Board's report describes a question that asked for David's weaknesses and for a justification of the claim that he was still a man after God's heart. "
          "It records that candidates had to explain his restoration and his achievement compared with Saul. "
          "This lesson gives the facts, the covenant and the argument."),
        H("Rise to power"),
        T("David was the youngest son of Jesse of Bethlehem, a shepherd. Samuel anointed him in secret (1 Samuel 16). His victory over Goliath, a Philistine warrior, made him famous (chapter 17). "
          "He married Saul's daughter Michal and was close friends with Jonathan. As Saul's jealousy grew, David fled and lived as an outlaw leader. "
          "For a time he served the Philistine king Achish of Gath and held the town of Ziklag as a vassal. After Saul's death he was made king of Judah at Hebron. Saul's son Ish-bosheth ruled the northern tribes until he was murdered. "
          "The northern elders then came to Hebron and anointed David king over all Israel, as a covenant with them (2 Samuel 5:1 to 3)."),
        H("Jerusalem and the ark"),
        T("David took the Jebusite city of Jerusalem (2 Samuel 5), a fortified town between Judah and the north that belonged to no tribe. He made it his capital, the 'City of David'. "
          "Then he brought the ark of the covenant to Jerusalem with celebration (chapter 6), after an earlier attempt ended in the death of Uzzah. "
          "This made Jerusalem both the political and religious centre. David also won wars against the Philistines, Moab, Ammon, Edom and Aram, and the kingdom grew into a small empire."),
        D("The wooden chest holding the tablets of the law, seen as the throne of God's presence and carried into battle. David's bringing it to Jerusalem linked the king and the capital to Israel's religion.", title="Ark of the covenant"),
        H("The Davidic covenant (2 Samuel 7)"),
        T("David lived in a palace of cedar while the ark was in a tent, and he wished to build God a house. Through the prophet Nathan, God replied: it is not David who will build a house for God. God will build David a **house**, meaning a dynasty. "
          "Key promises: God will make David's name great; give Israel a secure place; raise up David's offspring after him and establish his kingdom; his son will build a house for God's name; God will establish the throne of his kingdom for ever; "
          "God will be a father to him and he will be a son, and if he does wrong God will punish him but not take away his love as he did from Saul (verses 11 to 16)."),
        KEY("Features of the Davidic covenant", "Learn these for any question.", cards=[
            ["Dynasty", "David's descendants will rule; the promise is made to David's 'house'."],
            ["Father and son", "The king has a special relationship with God, described as sonship."],
            ["Discipline but not rejection", "A king who sins is punished but the line is not cut off."],
            ["Temple", "David's son, not David, will build the Temple."],
            ["Zion", "Jerusalem becomes God's chosen city."],
        ]),
        T("Later texts reflect on the covenant. Psalm 89 praises God's promise and then laments that it seems broken after the fall of the dynasty. Psalm 132 links the promise to the ark and Zion. "
          "First Kings 2:4 and 8:25 state a condition: the sons will rule if they walk before God. This gives scholars the question whether the covenant is **unconditional** (2 Samuel 7) or **conditional** (Kings). "
          "After the end of the monarchy in 587 or 586 BC, the promise gave rise to the hope of a future king from David's line, a **messiah** (anointed one)."),
        H("David's sin and its effects"),
        T("In 2 Samuel 11, David stays in Jerusalem while the army fights Ammon. He sees Bathsheba, the wife of Uriah the Hittite, one of his soldiers, and sleeps with her. She becomes pregnant. "
          "David tries to cover it up, and when that fails he arranges for Uriah to be killed in battle. Nathan confronts him with a story of a rich man who took a poor man's only lamb (chapter 12). David confesses: 'I have sinned against Yahweh.' "
          "Nathan tells him that God has forgiven him but that the sword will never leave his house, and the child dies. Psalm 51 is traditionally linked with this repentance."),
        T("The consequences follow: Amnon rapes Tamar, and Absalom kills Amnon; Absalom then revolts and David flees Jerusalem; Absalom is killed by Joab; and another revolt follows under Sheba. "
          "Late in life David also orders a census (chapter 24), which is called a sin, and a plague follows."),
        H("A man after God's own heart?"),
        T("The phrase comes from 1 Samuel 13:14 (a man after his own heart, chosen to replace Saul). Acts 13:22 repeats it. Why is David seen as worthy despite sin?"),
        KEY("Answering the report's question", "Weakness and worth, with evidence.", cards=[
            ["Weaknesses", "Adultery with Bathsheba; murder of Uriah; weak control of his sons (Amnon, Absalom, Adonijah); the census; harshness in war and in some deaths."],
            ["Why still counted worthy", "He repented when confronted (chapter 12 and Psalm 51); he accepted the punishment and did not rule as an absolute tyrant; he spared Saul twice; he kept faith with Yahweh alone, whereas Saul spared Agag and sought a medium; he brought the ark to Jerusalem and received the covenant."],
            ["Compared with Saul", "Saul's rejection followed disobedience and no real change. David's sin was greater in some ways but he turned back, so his kingdom was renewed and surpassed Saul's."],
        ]),
        T("An independent piece of evidence: the Tel Dan inscription, found in northern Israel in the 1990s and dated to the 9th century BC, uses a phrase most scholars read as 'house of David'. It is evidence that David was remembered as the founder of a dynasty soon after his time. "
          "It does not by itself describe his reign."),
        EX("Worked example 1: the Davidic covenant", intro="Explain the main promises made to David in 2 Samuel 7.", steps=[
            S("Setting", text="David wishes to build a house for God. Nathan brings God's reply."),
            S("The promise", text="God will build David a house, meaning a dynasty, and his kingdom will be established for ever."),
            S("Relationship", text="God will be a father to the king and the king a son. Wrong will be punished but love will not be removed."),
            S("Temple", text="David's son will build the Temple."),
        ]),
        EX("Worked example 2: model plan", intro="'David was a great king despite being a great sinner.' Discuss.", steps=[
            S("Achievements", text="United the tribes; took Jerusalem; brought the ark; defeated neighbours; received the covenant."),
            S("Sins", text="Bathsheba and Uriah; failure with his sons; census."),
            S("Response to sin", text="Repentance when Nathan spoke; Psalm 51; acceptance of the consequences."),
            S("Comparison", text="Saul and David both sinned; David repented, Saul made excuses."),
            S("Judgement", text="His greatness lies partly in the achievement and partly in his submission to God's word. The writers do not hide his faults."),
        ]),
        MISTAKE("Telling the Bathsheba story without answering the question", "Say what the sin shows about royal power, repentance and forgiveness, and what it led to."),
        MISTAKE("Saying the Davidic covenant promised that David would build the Temple", "Nathan's oracle says David will not build it. His son Solomon will."),
        TIP("Exam link: David is a Section 1.1 topic in the report and the question on his weakness and worth drew many candidates. Learn his sins, his repentance, and a comparison with Saul."),
        QUIZ("In 2 Samuel 7, the 'house' God promises to build for David means:",
             ["The Temple in Jerusalem", "A palace of cedar", "A dynasty of kings", "The tribe of Judah"], 2,
             "Nathan's oracle plays on the word 'house': David wanted to build a house (temple) for God, but God will build David a house, meaning a dynasty.",
             feedback=["The Temple is the house David's son will build.", "David already lived in a cedar palace.", "", "The promise concerns David's line, not the tribe."]),
        QUIZ("Who confronted David about Bathsheba and Uriah?",
             ["Samuel", "Elijah", "Nathan", "Gad"], 2,
             "The prophet Nathan told David the story of the poor man's lamb (2 Samuel 12).",
             feedback=["Samuel had died before this event.", "Elijah lived much later.", "", "Gad was a prophet in David's time but is linked with the census in chapter 24."]),
        PQ("State three promises made to David through Nathan.",
           "A dynasty or house that will last; a son who will build God's house; a father and son relationship; discipline but not rejection for wrongdoing; David's name made great; a secure place for Israel."),
        PQ("Why did David bring the ark to Jerusalem?",
           "To make Jerusalem the religious as well as the political centre of the kingdom. The ark symbolised God's presence and the covenant. Bringing it to the new capital joined the royal house to Israel's worship and prepared for the Temple."),
        PQ("To what extent was David a man after God's own heart? Discuss.",
           "Plan. Introduction: quote the phrase (1 Samuel 13:14) and say the issue is character. Against: adultery, murder, his sons, the census. For: repentance, Psalm 51, mercy to Saul, loyalty to Yahweh, the ark and Jerusalem, the covenant. "
           "Evaluation: the writers show him as a flawed person whom God forgave; the phrase means that God chose him, not that he was perfect. Judgement: worthy, but because he turned back to God."),
        SUM("David rose from shepherd to king of Judah at Hebron and then of all Israel, and took Jerusalem.",
            "He brought the ark to the new capital, joining politics and religion.",
            "The Davidic covenant (2 Samuel 7) promises an everlasting house, with God as father to the king.",
            "His sin with Bathsheba and Uriah brought punishment, but he repented.",
            "A balanced assessment uses both achievements and failings."),
    ],
))

# ---------------------------------------------------------------------------
# 10. Solomon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="Solomon",
    title="Solomon: wisdom, building, trade and the price of glory",
    slug="rsl1-solomon",
    minutes=22,
    summary="Describes Solomon's accession, wisdom, administration, building and trade, the burdens that fell on the people, and the theological judgement on his foreign alliances, with a fair overall assessment.",
    objectives=[
        "Explain how Solomon became king and secured his throne",
        "Describe his administration, building programme and trade",
        "Explain the social and religious costs of his reign",
        "Assess Solomon's reign as a golden age or the start of decline",
    ],
    key_concepts=["Succession", "Wisdom", "Administrative districts", "Forced labour", "Alliances", "Division of the kingdom"],
    blocks=[
        H("Introduction"),
        T("**Solomon**, son of David and Bathsheba, ruled for about forty years, about 970 to 931 BC (check your textbook). His reign is remembered as a time of peace, wealth, wisdom and the building of the Temple. "
          "Yet the same writers record forced labour, heavy taxes and idolatry, and say the kingdom divided soon after his death. "
          "A good answer weighs both."),
        H("Securing the throne"),
        T("In David's old age his son Adonijah, helped by the commander Joab and the priest Abiathar, claimed the throne. The prophet Nathan and Bathsheba persuaded David to name Solomon, and the priest Zadok anointed him (1 Kings 1). "
          "After David's death Solomon removed his rivals: Adonijah and Joab were put to death, and Abiathar was sent into exile (chapter 2). "
          "This shows that the succession was not automatic and that politics and religion were joined."),
        H("Wisdom"),
        T("At Gibeon Solomon asked God for an understanding mind to judge the people, rather than long life or riches, and God promised wisdom and also wealth (1 Kings 3). "
          "The story of the two women who claimed the same baby shows his judgement. His reputation attracted visitors, including the Queen of Sheba (chapter 10). "
          "Tradition names him as a source of proverbs and songs, and the book of Proverbs has sections linked with his name. Most scholars think those books were collected later."),
        D("Practical skill in living and ruling, rooted in respect for God. Israelite wisdom included proverbs, advice to rulers and observation of nature.", title="Wisdom"),
        H("Administration and building"),
        KEY("How Solomon ran the kingdom", "These details come from 1 Kings 4 and 9.", cards=[
            ["Twelve districts", "He divided the kingdom into twelve districts, each supplying the court for one month a year. The districts did not always follow tribal lines, which weakened old tribal ties."],
            ["Officials and army", "A list of officials (priest, scribes, recorder, army commander); chariot and horse units based in cities such as Hazor, Megiddo and Gezer."],
            ["Forced labour", "Labour gangs from Israelites worked on buildings (1 Kings 5:13 to 14)."],
            ["Building", "The Temple (about seven years), his palace (about thirteen years), the Millo and the walls of Jerusalem, and fortified cities."],
        ]),
        T("Archaeology: in the 20th century Yigael Yadin linked similar six-chambered gates at Hazor, Megiddo and Gezer with Solomon. Other archaeologists, such as Israel Finkelstein, date those layers later (the 'low chronology'), and the dating debate is still open. "
          "Check your textbook; do not state it as settled."),
        H("Trade and foreign relations"),
        T("Solomon made treaties by marriage, most famously with the daughter of a Pharaoh. He had a close relationship with Hiram, king of Tyre, who supplied cedar and skilled craftsmen for the Temple, in return for wheat and oil. "
          "He built a fleet at Ezion-geber on the Red Sea, which traded for gold from Ophir, and he traded in horses and chariots. His wealth became famous."),
        H("The costs"),
        KEY("Problems of the reign", "Link each to the later division.", cards=[
            ["Taxation and forced labour", "The people carried the burden of the court and building. When his son Rehoboam refused to lighten it, the northern tribes revolted (1 Kings 12)."],
            ["Religious compromise", "Solomon married foreign wives and built shrines for their gods. The writer says his heart was turned away from Yahweh (1 Kings 11)."],
            ["Enemies", "Adversaries such as Hadad of Edom and Rezon of Damascus arose, and Jeroboam, a labour overseer, was told by the prophet Ahijah that he would rule ten tribes."],
        ]),
        T("The writer of Kings is a Deuteronomistic editor, who judges the kings by their loyalty to Yahweh and to worship at the Temple. His verdict on Solomon is mixed: glorious beginning, wrong ending."),
        EX("Worked example 1: model plan", intro="'Solomon's reign was a golden age for Israel.' Discuss.", steps=[
            S("For", text="Peace and security; the Temple; trade and wealth; fame for wisdom; skilled administration."),
            S("Against", text="Forced labour and heavy taxes; a divided society; idolatry; borders weakened by rebels; the kingdom splits soon after."),
            S("Evaluation", text="The same buildings and taxes that made it glorious caused the revolt. The writer sees religious failure as the true cause of the split."),
            S("Judgement", text="A golden age for the court and the capital, but at a high cost for many."),
        ]),
        EX("Worked example 2: link to the division", intro="Explain how Solomon's policies led to the division of the kingdom.", steps=[
            S("Burdens", text="Forced labour and taxes weighed most on the northern tribes."),
            S("Districts", text="The new districts weakened tribal loyalties and exposed the north to the court's demands."),
            S("Religion", text="The shrines for foreign gods angered prophets such as Ahijah."),
            S("Result", text="After Solomon's death Rehoboam refused to reduce the burdens, and ten tribes followed Jeroboam."),
        ]),
        MISTAKE("Listing only wealth and wisdom", "The Board expects evaluation. Include the costs and the writer's religious judgement."),
        MISTAKE("Saying Solomon built the first altar in Jerusalem", "David had already set up the ark in a tent and built an altar on the threshing floor of Araunah (2 Samuel 24). Solomon built the Temple."),
        TIP("Exam link: Solomon connects the monarchy topics with the Temple topic and with the later division. Use the Temple lesson that follows for the detail of its design and cult. Check how your teacher links this to the report's Section 1.1."),
        QUIZ("Which king of Tyre supplied cedar for the Temple?",
             ["Ahab", "Hiram", "Hadad", "Nebuchadnezzar"], 1,
             "Hiram of Tyre supplied cedar and craftsmen in exchange for food (1 Kings 5).",
             feedback=["Ahab was a king of Israel in the 9th century.", "", "Hadad of Edom was an adversary of Solomon.", "Nebuchadnezzar of Babylon destroyed the Temple later."]),
        QUIZ("Why did the twelve districts weaken old tribal loyalties?",
             ["They gave all land to the priests", "They did not always follow the tribal boundaries", "They ended the payment of taxes", "They were created by David"], 1,
             "Solomon's districts were organised for supplying the court and often cut across tribal lines.",
             feedback=["They were administrative, not a land gift to priests.", "", "They organised supplies and taxes, not ended them.", "They are credited to Solomon (1 Kings 4)."]),
        PQ("Describe how Solomon became king in 1 Kings 1 and 2.",
           "David was old. His son Adonijah claimed the throne with Joab and Abiathar. Nathan and Bathsheba reminded David of an oath, David named Solomon, and Zadok the priest anointed him. "
           "Solomon later removed Adonijah, Joab and Abiathar."),
        PQ("State three ways in which Solomon organised his kingdom.",
           "Twelve districts supplying the court; officials and a bureaucracy; chariot cities; forced labour; trade by land and sea; treaties by marriage."),
        PQ("Assess the view that Solomon's reign caused the division of the kingdom.",
           "For: forced labour and taxes; the districts; foreign shrines; Jeroboam and the prophecy of Ahijah; Rehoboam's refusal to reduce burdens. Against: tensions between north and south go back to David (Sheba's revolt, the northern anointing of David at Hebron); Rehoboam's actions were the immediate trigger. "
           "Judgement: Solomon's policies laid the ground, but the division also had earlier causes."),
        SUM("Solomon secured the throne with Zadok, Nathan and Bathsheba, removing Adonijah, Joab and Abiathar.",
            "He was known for wisdom, building (Temple, palace, cities), trade and treaties.",
            "He used districts, officials and forced labour.",
            "The costs were taxes, forced labour and idolatry, leading to revolt and division.",
            "Archaeological dating of his buildings is debated."),
    ],
))

# ---------------------------------------------------------------------------
# 11. The Temple, priesthood and festivals
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M2, topic="The Temple, priesthood and festivals",
    title="The Temple, the priesthood, sacrifices and the festivals",
    slug="rsl1-temple-priesthood-festivals",
    minutes=25,
    summary="Describes Solomon's Temple and its furniture, the priests and Levites and their duties, the main sacrifices, and the festivals of the Israelite year, with the main scholarly issues.",
    objectives=[
        "Describe the layout and furniture of Solomon's Temple and its later history",
        "Explain the roles of priests, high priest and Levites",
        "Distinguish the main kinds of sacrifice and what each meant",
        "Describe the main festivals and the religious ideas they express",
    ],
    key_concepts=["Temple", "Holy of Holies", "High priest", "Levites", "Burnt, peace and sin offerings", "Passover, Weeks, Tabernacles, Day of Atonement"],
    blocks=[
        H("Introduction"),
        T("Israelite worship centred on a holy place, a priesthood and a calendar of festivals. Before the monarchy the tent (tabernacle) and the ark were at Shiloh and other sanctuaries. "
          "David brought the ark to Jerusalem and Solomon built the **Temple** there. "
          "This lesson describes the Temple, the people who served in it, the sacrifices they offered and the festivals the nation kept."),
        H("Solomon's Temple"),
        T("According to 1 Kings 6 to 8, Solomon began the Temple in the fourth year of his reign and it took about seven years. It stood on the hill north of the old City of David, on the site of the threshing floor David had bought. "
          "Hiram of Tyre sent cedar and craftsmen."),
        IMG("alrsl1-temple-plan.svg", alt="Plan of Solomon's Temple showing the porch with two pillars, the main hall, and the Holy of Holies, with the altar of burnt offering in the courtyard", caption="Figure 1. Plan of the Temple (schematic, not to scale; details are debated)."),
        KEY("Parts of the Temple", "From the entrance inward.", cards=[
            ["Courtyard", "The great altar of burnt offering, the bronze 'sea' (a large basin) and ten movable bronze stands with basins, for washing."],
            ["Porch", "The entrance hall with two bronze pillars named Jachin and Boaz (1 Kings 7:21)."],
            ["Main hall", "The Holy Place: golden lamp stands, the table for the bread of the presence and the altar of incense."],
            ["Holy of Holies", "The inner room, a cube, with two great winged cherubim. It held the ark. Only the high priest entered, once a year on the Day of Atonement."],
        ]),
        T("At the dedication (1 Kings 8) the ark was placed in the inner room and a cloud filled the house. Solomon's prayer asks God to hear prayers made towards the Temple, even though heaven cannot contain him. "
          "This is important: the Temple was a place of meeting with God, not a box for God."),
        T("History: Shishak of Egypt took treasures from the Temple soon after Solomon (1 Kings 14). Kings such as Hezekiah and Josiah cleansed it. The Babylonians destroyed it in 587 or 586 BC. "
          "A second Temple was completed about 516 BC. King Herod later rebuilt and enlarged it, and the Romans destroyed it in AD 70."),
        H("Priests and Levites"),
        KEY("The ministers of the cult", "Priesthood was hereditary.", cards=[
            ["Priests", "Descendants of Aaron, of the tribe of Levi. They offered sacrifices, kept the lamps and bread, blessed the people, and taught the law."],
            ["High priest", "Head of the priests. Wore special clothing with the breastplate; entered the Holy of Holies on the Day of Atonement. In Solomon's time Zadok held the office, after Abiathar was removed."],
            ["Levites", "Other men of Levi. They helped with the work of the sanctuary, carried the ark, and later served as singers, gatekeepers and teachers."],
        ]),
        T("Priests also decided cases of clean and unclean, and used the Urim and Thummim, objects for seeking God's answer. Many scholars, following Wellhausen, argue that the distinction between priests and Levites became fixed late, and the Pentateuch sources differ about it. "
          "Check your textbook for the history of Zadokites and Levites."),
        H("Sacrifices"),
        KEY("Main offerings (Leviticus 1 to 7)", "Know what each means.", cards=[
            ["Burnt offering", "The whole animal is burned on the altar. A gift to God and a sign of complete dedication."],
            ["Grain offering", "Flour, oil and incense. Thanksgiving and recognition that the harvest comes from God."],
            ["Peace (fellowship) offering", "Part is burned, part is eaten by the worshipper and the priest. A shared meal of thanks or vows, expressing fellowship."],
            ["Sin and guilt offerings", "For unintentional sin and for wrongs needing restitution. Blood is used for cleansing and for restoring the relationship."],
        ]),
        H("Festivals"),
        T("Three festivals were pilgrim festivals, when men were to appear before God at the sanctuary (Deuteronomy 16:16). The calendars are in Exodus 23, Leviticus 23, Numbers 28 and 29 and Deuteronomy 16."),
        KEY("The main festivals", "Remember the season and the meaning.", cards=[
            ["Passover and Unleavened Bread (spring)", "Remembers the Exodus: the lamb, the haste, the unleavened bread. A week of bread without yeast follows."],
            ["Weeks, or Pentecost (early summer)", "Celebrates the wheat harvest, seven weeks after Passover. Later Jewish tradition links it with the giving of the Law."],
            ["Tabernacles, or Booths (autumn)", "Celebrates the final harvest and recalls the years in the wilderness when the people lived in tents. Joyful and long."],
            ["Day of Atonement (autumn)", "A day of fasting and ritual cleansing of the sanctuary and the people (Leviticus 16). The high priest enters the Holy of Holies, and a goat is sent away into the wilderness."],
            ["Sabbath and New Moon", "The weekly day of rest and the monthly offerings. The festival of Trumpets marks the new year of the seventh month."],
        ]),
        T("Festivals joined the agricultural year with Israel's history: a farming feast was given a historical meaning. This is why a festival is a form of teaching as well as celebration."),
        H("Centralisation and criticism"),
        T("Deuteronomy 12 commands worship at the one place Yahweh chooses. Josiah's reform in 621 BC destroyed local shrines (2 Kings 23). Some scholars connect this to the Jerusalem Temple as the only legitimate sanctuary. "
          "The prophets also criticised the cult when it was empty of justice: Amos 5 and Isaiah 1 speak against sacrifices and festivals without right living. They do not reject worship as such. You will see this in the Upper Sixth."),
        EX("Worked example 1: role of the high priest", intro="Describe the duties of the high priest.", steps=[
            S("Cult", text="He led the offerings on the most solemn days."),
            S("Day of Atonement", text="He alone enters the Holy of Holies once a year, with blood, to cleanse the sanctuary and the people."),
            S("Leadership", text="He heads the priests and, after the exile, becomes the chief religious leader of the community."),
            S("Dress", text="He wears special clothing with a breastplate linked to the twelve tribes."),
        ]),
        EX("Worked example 2: model plan", intro="'The Temple was the most important institution in Israelite religion.' Discuss.", steps=[
            S("For", text="It was the one holy place; the sacrifices and festivals centred there; it housed the ark; kings and prophets all refer to it."),
            S("Against", text="Religion also depended on the law, the covenant and the prophets; the exile showed faith could survive without the Temple."),
            S("Evaluation", text="The Temple expressed God's presence but could not guarantee it: Jeremiah warns against trusting in the building."),
            S("Judgement", text="It was central, but not the only support of faith."),
        ]),
        MISTAKE("Saying all Levites were priests", "All priests were Levites in the later tradition, but not all Levites were priests. Levites served in supporting roles."),
        MISTAKE("Describing the festivals as only harvest celebrations", "Each also remembered an event: Passover the Exodus, Tabernacles the wilderness, and Weeks later the giving of the Law."),
        TIP("Exam link: this topic suits structured questions (name three offerings, describe the Holy of Holies) and Paper 1 facts. In essays link the cult to covenant and to the later prophets."),
        QUIZ("Who alone could enter the Holy of Holies?",
             ["Any Levite", "The king", "The high priest, once a year", "The scribes"], 2,
             "The inner room was entered only by the high priest, on the Day of Atonement.",
             feedback=["Levites served in support and could not enter.", "The king had a special place but not entry to the inner room.", "", "Scribes copied and taught the law."]),
        QUIZ("Which offering was burned entirely on the altar?",
             ["Peace offering", "Grain offering", "Burnt offering", "Guilt offering"], 2,
             "The burnt offering was wholly burned and expressed complete dedication.",
             feedback=["Part of the peace offering was eaten by the worshipper.", "Only a portion of the grain offering was burned.", "", "The guilt offering dealt with wrongs needing restitution."]),
        PQ("Describe the Holy of Holies.",
           "The innermost room of the Temple, a cube. It held the ark of the covenant, with two large winged cherubim over it. It was the place of God's presence. Only the high priest entered it, once a year on the Day of Atonement."),
        PQ("State the meaning of three Israelite festivals.",
           "Passover: remembers the Exodus. Weeks (Pentecost): thanks for the wheat harvest. Tabernacles: thanks for the final harvest and remembrance of the wilderness. Day of Atonement: cleansing from sin. Any three."),
        PQ("Assess the role of the priesthood in Israelite religion.",
           "Roles: sacrifice, blessing, teaching, deciding clean and unclean, running the sanctuary. Strengths: preserved worship, law and order. Weaknesses: priests could become corrupt or formal, which the prophets attacked. "
           "Evaluation: priests and prophets worked in tension but also together. Judgement: central for worship, but accountable to the covenant."),
        SUM("The Temple had a porch, a main hall and the Holy of Holies, with the ark and an altar in the courtyard.",
            "Priests were descended from Aaron; the high priest entered the inner room once a year; Levites assisted.",
            "The main offerings were burnt, grain, peace, sin and guilt.",
            "Festivals: Passover, Weeks, Tabernacles and the Day of Atonement, linking harvest and history.",
            "Prophets criticised empty ritual, not worship itself."),
    ],
))

# ---------------------------------------------------------------------------
# 12. The Jewish and Greco-Roman background
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="The Jewish and Greco-Roman background",
    title="From exile to Rome: the world of the New Testament",
    slug="rsl1-jewish-greco-roman-background",
    minutes=24,
    summary="Traces Jewish history from the exile through Persian, Greek and Hasmonean rule to Herod and Roman Judaea, and the Greek language, culture and religions that shaped the setting of the Gospels.",
    objectives=[
        "Place the main events from the exile to Roman rule in order",
        "Explain the Maccabean revolt and its effects on Jewish identity",
        "Describe Roman rule in Palestine, including Herod and the prefects",
        "Explain how Greek language, the Septuagint, the diaspora and Roman peace helped the early Christian mission",
    ],
    key_concepts=["Intertestamental period", "Hellenism", "Maccabean revolt", "Herod the Great", "Septuagint", "Diaspora", "Pax Romana"],
    blocks=[
        H("Introduction"),
        T("The Old Testament ends about the 5th century BC and the New Testament was written in the first century AD. The years in between are called the **intertestamental period**. "
          "They matter because many ideas, groups and institutions that appear in the Gospels, such as the synagogue, the Pharisees, hopes for a messiah and Greek as a common language, began or developed in those centuries."),
        D("The period of about four centuries between the last Old Testament writings and the beginning of the New Testament, when Judaism met Persian, Greek and Roman powers.", title="Intertestamental period"),
        H("Timeline"),
        IMG("alrsl1-intertestamental-timeline.svg", alt="Timeline from 586 BC to AD 70 with the exile, Persian, Greek, Maccabean, Roman and Herodian periods marked", caption="Figure 1. From the exile to the destruction of the Temple (dates approximate)."),
        KEY("Main stages", "Learn the order and a key date for each.", cards=[
            ["Exile and return", "Babylon destroys Jerusalem in 587 or 586 BC. Cyrus of Persia lets the Jews return in 538 BC. The second Temple is finished about 516 BC."],
            ["Persian rule", "Judah is a small province. Ezra and Nehemiah rebuild the community around the law."],
            ["Greek rule", "Alexander the Great conquers the region about 332 BC. After his death, the Ptolemies (Egypt) and Seleucids (Syria) rule Judaea in turn."],
            ["Maccabean revolt and Hasmonean rule", "Antiochus IV Epiphanes forbids Jewish practices and defiles the Temple in 167 BC. Mattathias and his son Judas Maccabeus lead a revolt. The Temple is rededicated in 164 BC (remembered at Hanukkah). The Hasmonean family rules until 63 BC."],
            ["Roman rule", "Pompey takes Jerusalem in 63 BC. Herod the Great rules as king under Rome from 37 BC to 4 BC."],
        ]),
        H("Hellenism and the Maccabees"),
        T("**Hellenism** means the spread of Greek language, ideas and way of life after Alexander. Many Jews adopted parts of it: Greek names, schools and sports. Others resisted what they saw as a threat to the covenant. "
          "When Antiochus IV tried to force the Jews to give up circumcision, the Sabbath and the law, and set up an altar to Zeus in the Temple, the Maccabean revolt began. "
          "The revolt made martyrdom and loyalty to the law very important, and it produced the books of the Maccabees, which are in the Apocrypha. The Hasmonean kings who followed were also priests and later became unpopular with some Jews, which helps explain the rise of the Pharisee and Essene groups."),
        H("Rome, Herod and Palestine"),
        T("Herod the Great was an able but cruel ruler who built the harbour at Caesarea, fortresses such as Masada and Herodium, and a magnificent rebuilding of the Temple in Jerusalem. "
          "Matthew records that he ordered the killing of the baby boys in Bethlehem. After his death in 4 BC his kingdom was divided: Archelaus took Judaea (and was removed in AD 6), Herod Antipas took Galilee and Perea (and ruled during Jesus' ministry), and Philip took the north-east. "
          "From AD 6 Judaea was governed by Roman prefects. Pontius Pilate held the office from about AD 26 to 36. Romans collected taxes through local agents, called tax collectors, who were widely disliked."),
        KEY("Roman rule in Palestine", "Useful for explaining the Gospels' setting.", cards=[
            ["Taxes and census", "Heavy taxes, with tax collectors; a census under Quirinius about AD 6 caused unrest."],
            ["Local rulers", "Herod's sons and the high priest worked with Rome. The high priest was chosen or removed by Roman officials."],
            ["Resistance", "Some groups wanted revolt, some accepted Roman rule and others waited for God to act. The revolt of AD 66 led to the destruction of the Temple in AD 70."],
        ]),
        H("Language, culture and religion"),
        T("Greek was the common language of trade and government in the eastern Mediterranean, called **Koine** ('common') Greek. The New Testament was written in it. "
          "Jews in Alexandria translated the Hebrew scriptures into Greek in the 3rd and 2nd centuries BC. This translation is the **Septuagint** (often abbreviated LXX). Many New Testament writers quote it."),
        T("Jews also lived outside Palestine, in what is called the **diaspora** ('scattering'), in cities like Alexandria, Antioch and Rome. They met for prayer and reading in **synagogues**, which helped the early Christian missionaries find audiences. "
          "Some Gentiles, called God-fearers, admired Jewish faith without becoming full converts. The Roman peace (the **Pax Romana**), good roads and sea routes helped travel."),
        KEY("The religious world of the Roman empire", "Be able to name examples.", cards=[
            ["Emperor and state religion", "Public sacrifices and, in many cities, worship of the emperor. Jews were generally excused from emperor worship."],
            ["Mystery religions", "Groups with secret rites and a god who died and rose, such as the cults of Isis and Mithras."],
            ["Philosophies", "Stoics taught living by reason and nature; Epicureans taught that the gods do not intervene and that pleasure is the aim of life."],
        ]),
        EX("Worked example 1: effects of Greek culture", intro="How did Greek language and culture prepare for the spread of Christianity?", steps=[
            S("Common language", text="Koine Greek could be understood across the empire, so missionaries did not need translators."),
            S("Scriptures", text="The Septuagint gave Greek readers access to the Hebrew scriptures and many New Testament writers quote it."),
            S("Diaspora synagogues", text="Jewish communities across the empire gave early missionaries a first audience, as Acts describes."),
            S("Evaluation", text="Greek culture also challenged Judaism and caused conflict, as the Maccabean revolt shows."),
        ]),
        EX("Worked example 2: model plan", intro="Explain the importance of the Maccabean revolt for Jewish life.", steps=[
            S("Cause", text="Antiochus IV banned Jewish practices and set up a pagan altar in the Temple."),
            S("Course", text="Mattathias and Judas led a revolt; the Temple was rededicated in 164 BC."),
            S("Effects", text="An independent Jewish state under the Hasmoneans; a strong sense of martyrdom and loyalty to the law; new groups reacting to Hasmonean rule."),
            S("Later influence", text="Memory of the revolt fed hopes of a deliverer and some of the resistance to Rome."),
        ]),
        MISTAKE("Confusing the Seleucids and the Ptolemies", "Ptolemies ruled from Egypt (Alexandria). Seleucids ruled from Syria. Antiochus IV was Seleucid."),
        MISTAKE("Saying the New Testament was written in Hebrew", "It was written in Koine Greek. Jesus and his disciples most likely spoke Aramaic in daily life, and a few Aramaic words are kept in the Gospels."),
        TIP("Exam link: this background supports questions on the setting of Jesus' ministry and on the Gospel of Luke in the Board's Paper 3 structure (the report notes candidates must place answers in the Palestinian context). Use dates with 'about' and check your textbook for exact years."),
        QUIZ("Who tried to force Jews to give up their religion in 167 BC?",
             ["Pompey", "Herod the Great", "Antiochus IV Epiphanes", "Cyrus"], 2,
             "Antiochus IV, a Seleucid king, banned Jewish practices and defiled the Temple, which led to the Maccabean revolt.",
             feedback=["Pompey took Jerusalem for Rome in 63 BC.", "Herod ruled much later, from 37 BC.", "", "Cyrus of Persia let the Jews return from exile in 538 BC."]),
        QUIZ("What is the Septuagint?",
             ["The Aramaic version of the Gospels", "A Greek translation of the Hebrew scriptures", "A list of Roman governors", "The Dead Sea community rule"], 1,
             "The Septuagint is the Greek translation of the Hebrew scriptures made in Alexandria.",
             feedback=["The Gospels were written in Greek.", "", "It is not a Roman list.", "The Dead Sea Scrolls are a different collection."]),
        PQ("Name three ruling powers over Palestine between 538 BC and AD 70, in order.",
           "Persians, then the Greeks (first Alexander, then the Ptolemies and Seleucids), then the Hasmoneans (Jewish rule), then the Romans (with Herod as king, then prefects). Any three in the correct order."),
        PQ("Describe Roman rule in Palestine at the time of Jesus.",
           "Herod the Great died in 4 BC; his sons ruled as local princes, with Antipas in Galilee. Judaea was under a Roman prefect, Pilate from about AD 26. Taxes were heavy and collected by local tax collectors. "
           "The high priest worked under Roman supervision. There were tensions and some revolts."),
        PQ("Assess how far the Greco-Roman world helped the spread of early Christianity.",
           "For: a common language, the Septuagint, the diaspora synagogues, Roman roads and peace, a hunger for religious answers. Against: Jewish and Roman persecution, and the conflict over emperor worship; some Greek ideas conflicted with Christian teaching. "
           "Judgement: the setting made the spread easier, but the message also met strong resistance."),
        SUM("The intertestamental period runs from the exile to Rome and shaped the New Testament setting.",
            "The Maccabean revolt (167 to 164 BC) came from Seleucid persecution under Antiochus IV.",
            "Herod the Great ruled 37 to 4 BC and Pilate was prefect about AD 26 to 36.",
            "Koine Greek, the Septuagint and the diaspora helped the Christian mission.",
            "Rome allowed local religion but demanded taxes and order."),
    ],
))

# ---------------------------------------------------------------------------
# 13. Jewish groups and institutions
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Jewish groups and institutions",
    title="Pharisees, Sadducees, Essenes, Zealots, the Sanhedrin and apocalyptic hope",
    slug="rsl1-jewish-groups-institutions",
    minutes=24,
    summary="Compares the main Jewish groups of Jesus' time (Pharisees, Sadducees, Essenes, Zealots), the Sanhedrin, the Temple and the synagogue, and the apocalyptic and messianic hopes of the period.",
    objectives=[
        "Describe the beliefs and practices of the Pharisees, Sadducees, Essenes and Zealots",
        "Explain the roles of the Sanhedrin, the Temple and the synagogue",
        "Explain apocalypticism and messianic hopes",
        "Evaluate how reliable our sources are for each group",
    ],
    key_concepts=["Pharisees", "Sadducees", "Essenes and Qumran", "Zealots", "Sanhedrin", "Synagogue", "Apocalypticism", "Messiah"],
    blocks=[
        H("Introduction"),
        T("When we read the Gospels, we meet groups with names such as Pharisees and Sadducees. To understand why they respond to Jesus as they do, we must know what each believed and how much power each had. "
          "Our evidence is limited. We have the New Testament, the Jewish historian **Josephus** (writing in the 70s to 90s AD), writings of the Jewish thinker Philo, later Jewish rabbinic writings, and the Dead Sea Scrolls. "
          "Each source has its own viewpoint, so scholars debate many details."),
        H("The main groups"),
        KEY("Compare the four groups", "Use this as a revision frame.", cards=[
            ["Pharisees", "Lay teachers with strong support among ordinary people and a link with the synagogues. They accepted the written law and the oral tradition, believed in the resurrection of the dead, angels and divine providence, and stressed careful obedience including tithes, sabbath and purity. They did not make up all the scribes, though the Gospels often link them."],
            ["Sadducees", "Mostly priests and wealthy families, centred on the Temple in Jerusalem. They accepted only the written law, did not believe in the resurrection of the dead (Mark 12:18) or in angels and spirits (Acts 23:8), and were more willing to work with the Romans. They lost their power after AD 70."],
            ["Essenes", "A group who withdrew from Temple worship and lived in disciplined communities with shared property and strict purity. Many scholars link them with the settlement at Qumran and the Dead Sea Scrolls, though this link is debated. They expected a final struggle between good and evil. They are not named in the New Testament."],
            ["Zealots", "A word used by Josephus for revolutionaries who led the revolt against Rome in AD 66. Whether an organised party called Zealots existed in Jesus' time is debated. Simon, one of the Twelve, is called the Zealot (Luke 6:15). Related groups, such as the Sicarii, used assassination."],
        ]),
        T("Other groups: the **scribes** copied and interpreted the law, often with the Pharisees. The **Herodians** supported the family of Herod. The **Samaritans** worshipped at Mount Gerizim, accepted only the first five books and were disliked by many Jews. "
          "Most Jews belonged to no party; they were farmers, fishermen and craftsmen, who kept the law as they understood it."),
        H("The Sanhedrin"),
        T("The **Sanhedrin** was the Jewish council in Jerusalem. The high priest presided, and later tradition counts seventy-one members, including chief priests (mostly Sadducees), elders of leading families and scribes (some of whom were Pharisees). "
          "It judged religious and some civil matters under Roman supervision. The Gospels show it examining Jesus. Whether it could carry out a death sentence is debated; John 18:31 says the Jews could not put anyone to death, while other evidence suggests it could in some cases. Check your textbook."),
        H("Temple and synagogue"),
        KEY("Two centres of Jewish life", "Know the difference.", cards=[
            ["Temple", "Centre of sacrifice and the three pilgrim festivals; run by priests; the only place of sacrifice; destroyed in AD 70."],
            ["Synagogue", "Local meeting place (the word means 'gathering') for prayer, reading and teaching of the law on the Sabbath. Found in Galilee and across the diaspora. Jesus and Paul taught in synagogues. It survived the loss of the Temple."],
        ]),
        H("Apocalyptic hope and the Messiah"),
        D("A type of Jewish writing and belief which expects God to end the present age soon, judge evil and vindicate the faithful. It uses visions, symbols, angels and numbers. The books of Daniel and 1 Enoch are examples.", title="Apocalypticism"),
        T("Features of apocalypticism: a sharp contrast between this age and the age to come; a great struggle between good and evil; a final judgement; resurrection of the dead; and a belief that God will act decisively very soon. "
          "It comforted those who suffered, such as the Jews under Antiochus IV and under Rome. John the Baptist and Jesus' preaching about the kingdom share some of its themes, though scholars debate how far."),
        T("Messianic hopes varied. Some expected a king from David's line, some a priest, some a prophet and some a heavenly figure. There was no single expectation, which helps explain why people in the Gospels answered Jesus differently. Matthew and Luke use these titles in their own ways. See the Christological titles lesson later."),
        EX("Worked example 1: Pharisees and Sadducees on the resurrection", intro="Explain the difference between Pharisees and Sadducees on resurrection and why it matters.", steps=[
            S("Pharisees", text="They accepted the resurrection of the dead as part of God's justice."),
            S("Sadducees", text="They held only to the written law, which they thought did not teach resurrection, so they denied it (Mark 12:18)."),
            S("Why it matters", text="When Jesus teaches about resurrection, the Pharisees find him closer to their view while the Sadducees oppose him. Acts shows Paul using this division before the Sanhedrin (23:6 to 8)."),
        ]),
        EX("Worked example 2: model plan", intro="Why did the Pharisees and Sadducees react differently to Jesus?", steps=[
            S("Pharisees", text="They shared ideas about resurrection and teaching, but they disputed his attitude to the sabbath and purity laws and to sinners."),
            S("Sadducees", text="They feared that a popular movement might provoke Rome and his act in the Temple threatened their authority."),
            S("Common point", text="Both depended on the law and the Temple, so claims of Jesus' authority challenged each."),
            S("Judgement", text="Their opposition had religious and political roots. The Gospels do not show all Pharisees as opponents."),
        ]),
        MISTAKE("Saying that all Pharisees were hypocrites", "The Gospels criticise some Pharisees, but Nicodemus, Gamaliel (Acts 5) and Paul himself were Pharisees. Write 'some Pharisees' or 'Pharisees in the Gospels'."),
        MISTAKE("Saying the Essenes are named in the New Testament", "They are not. Our knowledge comes from Josephus, Philo, Pliny and the Dead Sea Scrolls, if the Qumran link is accepted."),
        TIP("Exam link: expect structured questions on beliefs of Pharisees and Sadducees and on the Sanhedrin, and short Paper 1 facts. Link every group to the Gospels where you can."),
        QUIZ("Which group denied the resurrection of the dead?",
             ["Pharisees", "Sadducees", "Essenes", "Zealots"], 1,
             "The Sadducees, who accepted only the written law, denied resurrection (Mark 12:18; Acts 23:8).",
             feedback=["Pharisees believed in resurrection.", "", "Essenes expected a final judgement and the righteous to be vindicated.", "Zealots are defined by their resistance to Rome, not by this question."]),
        QUIZ("Which statement about the synagogue is correct?",
             ["It was the only place where sacrifice was offered", "It was a local place for prayer and teaching of the law", "It was a Roman court", "It was built only in Jerusalem"], 1,
             "The synagogue was a local assembly for prayer and scripture reading, found in Galilee and across the diaspora.",
             feedback=["Sacrifice was only in the Temple.", "", "Roman courts were separate.", "Synagogues existed in many towns."]),
        PQ("State three beliefs of the Pharisees.",
           "They accepted the oral tradition as well as the written law; believed in the resurrection of the dead; believed in angels and in God's providence; stressed careful keeping of the law, tithes, sabbath and purity; had strong links with the synagogue."),
        PQ("Describe the Essenes and name the source of our knowledge about them.",
           "A group who withdrew from the Temple to live in disciplined communities with shared property and purity rules, expecting a final struggle between good and evil. Sources: Josephus, Philo, Pliny and, if the Qumran link is accepted, the Dead Sea Scrolls. The New Testament does not name them."),
        PQ("Assess the view that Jesus' relationship with the Pharisees was entirely hostile.",
           "For: the Gospels record conflicts over the sabbath, purity, and eating with sinners; woe sayings in Matthew 23. Against: Pharisees invite Jesus to eat (Luke 7, 11, 14), warn him of Herod (Luke 13:31), and Nicodemus and Gamaliel are sympathetic. "
           "Evaluation: the Gospels were written after AD 70, when Pharisaic leaders were the main rivals of the church, which may sharpen the portrayal. Judgement: relationships were mixed, with sharp disputes between teachers of the same tradition."),
        SUM("Pharisees: oral law, resurrection, synagogue, popular. Sadducees: priestly, written law only, no resurrection.",
            "Essenes: withdrawn, purity, Qumran link debated. Zealots: resistance to Rome, whether a party in Jesus' time is debated.",
            "The Sanhedrin was the Jerusalem council under the high priest, with limited powers under Rome.",
            "The Temple was the centre of sacrifice; the synagogue was a local place of prayer and teaching.",
            "Apocalyptic hope expected God to end the age; messianic hopes were varied."),
    ],
))

# ---------------------------------------------------------------------------
# 14. Oral tradition and Form and Redaction criticism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="Oral tradition and Form and Redaction criticism",
    title="From Jesus' words to the Gospels: oral tradition, form criticism and redaction criticism",
    slug="rsl1-oral-form-redaction",
    minutes=24,
    summary="Explains how stories of Jesus were passed on by word of mouth, how form critics classify and trace the units, how redaction critics study each evangelist's editing, and the main criticisms of both.",
    objectives=[
        "Explain the gap between Jesus and the written Gospels and the role of oral tradition",
        "Describe form criticism: its aims, main forms and Sitz im Leben",
        "Describe redaction criticism and use a comparison of parallel passages",
        "Evaluate the strengths and limits of both methods",
    ],
    key_concepts=["Oral tradition", "Form criticism", "Sitz im Leben", "Pronouncement story", "Redaction criticism", "Evangelist as theologian"],
    blocks=[
        H("Introduction"),
        T("Jesus taught and died about AD 30. The earliest Gospel, Mark, is usually dated about AD 65 to 70, Matthew and Luke about the 80s, and John about the 90s. The dates are debated. "
          "For about a generation the stories and sayings of Jesus passed from mouth to mouth. This lesson looks at that stage and at two methods scholars use to study the Gospels: **form criticism** and **redaction criticism**."),
        H("Oral tradition"),
        D("Teaching, stories and sayings passed on by speaking and memory, not in writing, before they were collected in written Gospels.", title="Oral tradition"),
        T("In the Mediterranean world most people could not read, and oral teaching was normal. Jewish teachers trained students to memorise sayings. "
          "The scholar Birger Gerhardsson argued that Jesus' followers passed on his teaching with this kind of careful memory. Kenneth Bailey, from experience of Middle Eastern villages, described an *informal controlled* tradition: the core of a story or saying stays fixed while the telling can vary. "
          "Many African students will recognise this from their own culture, in which proverbs, praise names and community stories are kept alive by speakers and elders, with the community checking the teller."),
        KEY("Why the oral stage matters", "Two sides.", cards=[
            ["For reliability", "Memory training, eyewitnesses still alive (Richard Bauckham argues for this), and the community's concern to keep Jesus' words."],
            ["Against reliability", "The stories were told for teaching and worship, not for history, and they were shaped by the needs of different churches over decades."],
        ]),
        H("Form criticism"),
        D("A method that sorts the Gospel material into small units (pericopes), classifies them by form, and asks what need in the early church shaped each one. It was developed in Germany in the 1910s and 1920s by Martin Dibelius, Rudolf Bultmann and Karl Ludwig Schmidt.", title="Form criticism"),
        T("Schmidt argued that Mark's framework of places and times was the work of the evangelist, who strung separate units like pearls on a string. Form critics then ask the **Sitz im Leben**, the 'setting in life': where in the life of the church, such as preaching, teaching, worship or arguments with Jews, a story was used."),
        KEY("Common forms (names vary by scholar)", "Be able to give an example of each.", cards=[
            ["Pronouncement story", "A short event leading to a saying of Jesus. Example: the question about the tax to Caesar (Mark 12:13 to 17). Dibelius called some of these 'paradigms'."],
            ["Miracle story", "A pattern of need, request, act, result, response. Example: the healing of the leper (Mark 1:40 to 45)."],
            ["Parable and sayings", "Wise sayings and stories such as the sower. Sayings may be collected by theme."],
            ["Legend or story about holy persons", "Stories of birth and infancy, and some scenes at the Temple."],
            ["Passion narrative", "A continuous story from arrest to burial, probably the earliest long unit."],
        ]),
        T("Form critics believe that the tradition was shaped by community needs, and some, like Bultmann, were sceptical about how much can be traced to Jesus. Others, like Vincent Taylor, were more positive."),
        H("Criticisms of form criticism"),
        T("(1) The categories overlap: many units fit more than one form. (2) Scholars cannot show exactly how or why a form arose from a need. (3) The assumption that the stages of a story can be traced by its form is uncertain. "
          "(4) The community may not have created sayings freely, since eyewitnesses were alive. (5) The period of oral transmission was short compared with the long processes of folk tradition in other cultures."),
        H("Redaction criticism"),
        D("A method that studies how each evangelist edited and arranged his material, to find his own theological aims. It treats the evangelists as authors and theologians, not merely collectors. It arose after the Second World War with Willi Marxsen (Mark), Günther Bornkamm (Matthew) and Hans Conzelmann (Luke).", title="Redaction criticism"),
        T("The method needs a theory about sources. If Mark was written first and used by Matthew and Luke, then changes they made to Mark show their own interests. The method compares parallel passages."),
        EX("Worked example 1: the storm on the lake", intro="Compare Mark 4:35 to 41 with Matthew 8:23 to 27 and say what Matthew's changes suggest.", steps=[
            S("Mark's version", text="The disciples wake Jesus with a complaint: 'Teacher, do you not care that we are perishing?' Jesus calms the storm and then asks why they have no faith."),
            S("Matthew's version", text="The disciples call him 'Lord' and ask him to save them. Jesus speaks of their little faith before he calms the storm."),
            S("Changes", text="The disciples' address changes from a complaint to a prayer, and the rebuke comes before the miracle."),
            S("Suggested interest", text="Matthew presents the disciples as people of little faith who still turn to Jesus, which fits his teaching about discipleship in the church."),
        ]),
        EX("Worked example 2: model plan", intro="Assess the value of form criticism for understanding the Gospels.", steps=[
            S("Strengths", text="Shows that Gospel units had a life before being written, and that the Gospels were shaped by the church's needs. Draws attention to the form and purpose of each unit."),
            S("Weaknesses", text="Overlapping categories; speculation about the community's creativity; underestimates eyewitnesses and memory."),
            S("Alternative", text="Gerhardsson and Bailey stress careful transmission."),
            S("Judgement", text="Helpful for classifying and questioning, but weak as a way of deciding which sayings are historical."),
        ]),
        MISTAKE("Treating form criticism and redaction criticism as the same", "Form criticism studies the earlier oral stage and small units. Redaction criticism studies the evangelist's editing in the written Gospel."),
        MISTAKE("Saying that the methods prove the Gospels are not reliable", "They are tools. Some scholars use them to doubt the tradition, others to support it. State what each critic concludes."),
        TIP("Exam link: this topic prepares you for the Synoptic problem and for questions on how the Gospels were written. Always give a worked comparison from a text when you describe redaction criticism."),
        QUIZ("What does 'Sitz im Leben' mean?",
             ["The date of a Gospel", "The author of a Gospel", "The life setting that shaped a unit of tradition", "The Greek text of a manuscript"], 2,
             "It is the setting in the life of the church, such as preaching or worship, in which a story or saying was used.",
             feedback=["It is not a date.", "It is not about authorship.", "", "It is not about manuscripts."]),
        QUIZ("Which is an aim of redaction criticism?",
             ["To recover the exact words of Jesus in Aramaic", "To study how each evangelist edited his sources for his own purposes", "To find forgotten manuscripts", "To prove that Mark is the earliest Gospel"], 1,
             "Redaction critics study the editing of the evangelists, using comparisons of parallel passages, to find their theological aims.",
             feedback=["That is a different aim.", "", "It does not search for manuscripts.", "It usually assumes a theory of sources, and does not prove it."]),
        PQ("Name three forms identified by form critics and give an example of one.",
           "Pronouncement stories, miracle stories, parables, sayings, legends and the passion narrative. Example: the question about paying tax to Caesar (Mark 12:13 to 17) is a pronouncement story."),
        PQ("Explain how redaction criticism uses the comparison of Mark and Matthew.",
           "If Matthew used Mark, then differences between them show Matthew's editing. For example, in the storm story the disciples address Jesus as Lord and ask him to save them, and the rebuke of their little faith comes first. This suggests a concern with discipleship and faith. "
           "The method depends on the theory that Matthew used Mark."),
        PQ("Assess the claim that the Gospels are the products of church needs and not of eyewitness memory.",
           "For: form critics argue that units took shape in preaching, teaching and worship; the evangelists edit and arrange material. Against: eyewitnesses were alive; Jewish methods of memory; Bailey's controlled oral tradition; Bauckham's argument. "
           "Judgement: both memory and later shaping are present. The question is how much of each, which scholars still debate."),
        SUM("Gospel material was passed on orally for a generation before it was written.",
            "Form criticism sorts material into forms and asks about its Sitz im Leben (Dibelius, Bultmann, Schmidt).",
            "Redaction criticism studies each evangelist's editing (Marxsen, Bornkamm, Conzelmann).",
            "Criticisms: overlapping forms, speculation, underestimating memory and eyewitnesses.",
            "Use a worked comparison to show the method."),
    ],
))

# ---------------------------------------------------------------------------
# 15. The Synoptic problem
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M3, topic="The Synoptic problem",
    title="The Synoptic problem: Markan priority, Q and the Four-Source Hypothesis",
    slug="rsl1-synoptic-problem",
    minutes=26,
    summary="Explains why Matthew, Mark and Luke are so alike and so different, sets out the Two-Source and Four-Source hypotheses with the evidence for Markan priority and Q, and compares rival solutions.",
    objectives=[
        "Define the Synoptic problem and the terms triple tradition, double tradition, M and L",
        "Give the main arguments for the priority of Mark",
        "Explain the Q source and the Four-Source Hypothesis",
        "Evaluate the rival solutions: Augustinian, Griesbach and Farrer",
    ],
    key_concepts=["Synoptic problem", "Triple tradition", "Double tradition", "Q", "Two-Source Hypothesis", "Four-Source Hypothesis", "Markan priority"],
    blocks=[
        H("Introduction"),
        T("The Gospels of Matthew, Mark and Luke are called **Synoptic** (from Greek words meaning 'seen together') because they can be laid side by side in columns and compared. "
          "They tell many of the same stories, often in nearly the same words and order, yet they also differ. "
          "The **Synoptic problem** asks how these three Gospels are related. Did one use another? Did they use common sources? "
          "John's Gospel is very different in structure and content, so it is not part of the Synoptic problem. The answers are theories, and each has critics."),
        D("The question of the literary relationship between Matthew, Mark and Luke, given their close similarities and also their differences in wording, order and content.", title="Synoptic problem"),
        H("The evidence"),
        KEY("Four kinds of material", "Learn these names.", cards=[
            ["Triple tradition", "Material found in all three Gospels, such as the baptism of Jesus, the feeding of the five thousand and most of the passion story. Often in similar words and order."],
            ["Double tradition", "About two hundred verses shared by Matthew and Luke but not found in Mark. Mostly sayings, such as much of the Lord's Prayer, parts of the Beatitudes, and John the Baptist's warning."],
            ["Special Matthew (M)", "Found only in Matthew, such as the visit of the Magi and parables such as the weeds and the sheep and goats."],
            ["Special Luke (L)", "Found only in Luke, such as the Good Samaritan, the Prodigal Son and the stories of Zacchaeus and the road to Emmaus."],
        ]),
        T("Most of Mark appears in Matthew and much of it in Luke. Scholars often say that roughly 90 per cent of Mark's content is found in Matthew or Luke or both, but counts depend on how verses are measured. Check your textbook."),
        H("The Two-Source Hypothesis"),
        T("This theory was developed in the 19th century by scholars such as C. H. Weisse and H. J. Holtzmann. It says that **Mark was written first**, and that Matthew and Luke each used Mark. "
          "They also used a second source containing mainly sayings of Jesus, called **Q** (from the German *Quelle*, 'source'), which Mark did not use. "
          "Matthew and Luke wrote independently of each other."),
        KEY("Arguments for Markan priority", "Be ready to give three.", cards=[
            ["Wording", "Mark's Greek is rougher and his accounts are more detailed, while Matthew and Luke smooth the language. It is easier to explain a later writer improving than an earlier one making it rougher."],
            ["Order", "Matthew and Luke follow Mark's order of events, but they never agree with each other against Mark's order. If either had used the other, such agreement would be expected."],
            ["Difficult or embarrassing details", "Mark says Jesus could do no mighty work in Nazareth (6:5), and Matthew softens this. Mark's picture of the disciples' misunderstanding is often reduced in Matthew and Luke."],
            ["Length", "Matthew and Luke often shorten Mark's long stories, such as the Gerasene demoniac, and add teaching material."],
        ]),
        H("The case for Q"),
        T("Matthew and Luke share about two hundred verses not in Mark, often in almost the same Greek, as in John the Baptist's warning (Matthew 3:7 to 10 and Luke 3:7 to 9). "
          "If neither used the other, the best explanation is that both used a common written source. Because the shared material is mostly sayings, Q is thought to have been a collection of sayings, perhaps with some stories such as the temptation and the centurion's servant. "
          "No copy of Q has been found. Scholars reconstruct it from the double tradition."),
        KEY("The Four-Source Hypothesis", "B. H. Streeter, 1924.", cards=[
            ["Mark", "The earliest Gospel, used by Matthew and Luke."],
            ["Q", "The shared sayings of Matthew and Luke, not in Mark."],
            ["M", "Material special to Matthew, from oral or written sources."],
            ["L", "Material special to Luke, from oral or written sources."],
        ]),
        IMG("alrsl1-four-source.svg", alt="Diagram with Mark and Q feeding into Matthew and Luke, and M feeding Matthew and L feeding Luke", caption="Figure 1. The Four-Source Hypothesis (Streeter)."),
        H("Rival solutions"),
        KEY("Other views", "Each has support and difficulties.", cards=[
            ["Augustinian (Matthew first)", "Matthew was written first, Mark abbreviated Matthew and Luke used both. This is the oldest view, and Church tradition (Papias, reported by Eusebius) says Matthew wrote the sayings in Hebrew. Difficulty: why would Mark omit so much, including the Sermon on the Mount and the birth stories?"],
            ["Griesbach (Matthew, Luke, Mark)", "Proposed by J. J. Griesbach in the 18th century. Matthew first, Luke used Matthew, and Mark combined them. Revived by William Farmer. Difficulty: why would Mark leave out so much, and why is his order and wording rougher?"],
            ["Farrer-Goulder (Markan priority without Q)", "Mark first, Matthew used Mark, and Luke used both Mark and Matthew. Defended by Austin Farrer, Michael Goulder and Mark Goodacre. It removes the need for Q. Difficulty: why would Luke take apart Matthew's Sermon on the Mount and spread the sayings across his Gospel?"],
        ]),
        T("A problem for the Two-Source view is the **minor agreements**: places where Matthew and Luke agree against Mark in small details, which is easier to explain if Luke used Matthew. This is a main argument for Farrer-Goulder."),
        EX("Worked example 1: sorting material", intro="Place these stories in the correct category: the Good Samaritan, the baptism of Jesus, the Lord's Prayer, the visit of the Magi.", steps=[
            S("Good Samaritan", text="Only in Luke: special Luke (L)."),
            S("Baptism of Jesus", text="In all three Gospels: triple tradition."),
            S("Lord's Prayer", text="In Matthew and Luke but not in Mark: double tradition (Q), though the wording differs."),
            S("Visit of the Magi", text="Only in Matthew: special Matthew (M)."),
        ]),
        EX("Worked example 2: model plan", intro="'The Two-Source Hypothesis is the best solution to the Synoptic problem.' Discuss.", steps=[
            S("Introduction", text="Define the problem and the hypothesis (Mark and Q, used by Matthew and Luke independently)."),
            S("For", text="Mark's rougher style; agreement in order; double tradition in similar Greek; wide acceptance."),
            S("Against", text="No manuscript of Q; the minor agreements; the unclear content of Q."),
            S("Rivals", text="Farrer-Goulder (no Q), Griesbach and the Augustinian view with their own problems."),
            S("Judgement", text="It explains the most evidence with the fewest difficulties for many scholars, but it remains a hypothesis. A fair answer says so."),
        ]),
        MISTAKE("Writing that Q is a document that was found", "Q is a hypothesis. It is reconstructed from the verses shared by Matthew and Luke."),
        MISTAKE("Saying the Synoptic problem includes John", "John is very different in structure and content. The problem concerns the relationship of Matthew, Mark and Luke."),
        TIP("Exam link: the Synoptic problem connects to the Board's Paper 3 section on Luke, where the report records that candidates were asked about the authorship of Luke and its relation to Acts. State the theories as scholarly proposals and name the main arguments. Check with your teacher how the Board's syllabus treats the Synoptic problem."),
        QUIZ("What is the 'double tradition'?",
             ["Material found in all three Synoptic Gospels", "Material shared by Matthew and Luke but not found in Mark", "Material found only in Luke", "Material found only in John"], 1,
             "The double tradition is the material, mostly sayings, that Matthew and Luke share but Mark lacks. Q is the proposed source.",
             feedback=["That is the triple tradition.", "", "That is special Luke (L).", "John is not part of the Synoptic problem."]),
        QUIZ("Which is an argument for the priority of Mark?",
             ["Mark is the longest Gospel", "Matthew and Luke follow Mark's order but never agree with each other against it", "Mark includes the birth stories", "Mark was written in Hebrew"], 1,
             "If Matthew and Luke each used Mark, they would follow his order. Their never agreeing against Mark's order shows independent use of Mark.",
             feedback=["Mark is the shortest of the three.", "", "Mark has no birth stories.", "Mark was written in Greek."]),
        PQ("Explain the terms triple tradition, double tradition and Q.",
           "Triple tradition: material in Matthew, Mark and Luke. Double tradition: material shared by Matthew and Luke but not in Mark. Q: the hypothetical source (German Quelle, source) used by Matthew and Luke to explain the double tradition, thought to be mainly sayings of Jesus."),
        PQ("Give three arguments for the priority of Mark.",
           "Mark's wording is rougher and more detailed, while Matthew and Luke smooth it; Matthew and Luke follow Mark's order but never agree against it; Mark's difficult details (for example the limits on Jesus' power at Nazareth, or the disciples' misunderstanding) are softened in Matthew and Luke; Matthew and Luke often shorten Mark's stories."),
        PQ("Compare the Two-Source Hypothesis with the Farrer-Goulder hypothesis.",
           "Both accept Markan priority. Two-Source: Matthew and Luke each used Mark and Q, independently. Farrer-Goulder: no Q; Matthew used Mark and Luke used both Mark and Matthew. "
           "Two-Source is supported by the claim that Luke would not have broken up Matthew's discourses, and by the idea that Matthew and Luke wrote independently. Farrer-Goulder is supported by the minor agreements and by the lack of any copy of Q. "
           "Neither is certain; both are theories."),
        SUM("The Synoptic problem asks why Matthew, Mark and Luke are so similar and yet different.",
            "Triple tradition: in all three; double tradition: Matthew and Luke only; M and L are special to each.",
            "The Two-Source Hypothesis: Mark first and Q; Streeter added M and L to make the Four-Source Hypothesis.",
            "Arguments for Markan priority: wording, order, difficult details and length.",
            "Rivals: Augustinian, Griesbach and Farrer-Goulder. All are theories."),
    ],
))
