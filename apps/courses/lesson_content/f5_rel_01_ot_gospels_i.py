"""Form 5 Religious Studies: Old Testament I and II, and Synoptic Gospels I (20 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "form-5")

OT1 = "Old Testament I: Creation to Exodus"
OT2 = "Old Testament II: Monarchy & Prophets"
GOS1 = "Synoptic Gospels I: Birth & Galilean Ministry"

LESSONS = []

# ------------------------------------------------------------------ 1 Creation
LESSONS.append(lesson(
    module=OT1, topic="Creation accounts and the Fall",
    title="The creation accounts in Genesis 1 and 2",
    slug="rel1-creation-accounts", minutes=20,
    summary="What the Bible says about God as Creator in Genesis 1 and 2, the place of human beings, the sabbath rest, and what the accounts teach about stewardship.",
    objectives=[
        "Outline the order of creation in the six days of Genesis 1",
        "Describe the second account in Genesis 2: the man, the garden and the woman",
        "Explain what the accounts teach about God, human beings and the world",
        "Apply the idea of stewardship to the care of land, water and animals",
    ],
    key_concepts=["Creation", "Image of God", "Sabbath", "Stewardship", "Garden of Eden"],
    blocks=[
        H("Introduction"),
        T("A farmer in the Western Highlands clears a field, plants maize and beans, and looks after the soil for the next season. "
          "He knows the land is a gift and a responsibility. The Bible begins with a similar idea on a much larger scale: the world is a gift from God, and human beings are asked to care for it."),
        T("The Old Testament is the first part of the Christian Bible. Its first book is **Genesis**, a word meaning 'beginning'. "
          "The first two chapters of Genesis give two accounts of creation. Christians read these chapters in different ways, and your teacher or church may stress different points. "
          "In this lesson we study what the text itself says and what it teaches about God, people and the world."),
        H("Genesis 1: creation in six days"),
        T("The Bible says that in the beginning God created the heavens and the earth. God speaks, and things come into being. "
          "After each stage of creation the text says that God saw that it was good."),
        CODE("""Day 1  Light, separated from darkness
Day 2  The sky, separating the waters above and below
Day 3  Dry land and seas; plants and trees
Day 4  Sun, moon and stars
Day 5  Fish and sea creatures; birds
Day 6  Land animals; human beings
Day 7  God rests; the seventh day is blessed""", "text", title="The days of creation in Genesis 1"),
        T("Notice the pattern. Days 1 to 3 prepare places (light, sky, land and sea). Days 4 to 6 fill them (sun, moon and stars; fish and birds; animals and people). "
          "Human beings come last, as the high point of the account."),
        D("To be made in the **image of God** (Genesis 1:26-27) means that men and women have a special dignity and relationship with God. "
          "The Bible says God made them male and female and gave them responsibility over the creatures of the earth.", title="Image of God"),
        D("The **sabbath** is the seventh day, when the Bible says God rested from his work and blessed the day as holy. "
          "It became a day of rest and worship for God's people.", title="Sabbath"),
        H("Genesis 2: the man, the garden and the woman"),
        T("Genesis 2 tells the story from closer to the ground. The Lord God forms the man from the dust of the ground and breathes into him the breath of life. "
          "He plants a garden in Eden and puts the man there 'to work it and take care of it'. In the garden are two special trees: the tree of life and the tree of the knowledge of good and evil. "
          "God tells the man he may eat from every tree except the tree of the knowledge of good and evil."),
        T("God then says it is not good for the man to be alone. The man names the animals, but no suitable companion is found among them. "
          "God forms the woman and brings her to the man, who is glad to see her. The text presents marriage as a partnership of two people who belong together."),
        IMG("f5rel-1-creation-frame.svg",
            alt="Two columns showing days 1 to 3 as preparing places and days 4 to 6 as filling them, with the seventh day of rest below",
            caption="Figure 1. The pattern of the six days: preparing and filling, then rest."),
        KEY("What the two accounts teach", "Both accounts agree on the main message.", cards=[
            ["About God", "God is the one Creator. The world is not an accident and it depends on God."],
            ["About the world", "Creation is good. The earth is a gift to be enjoyed and cared for, not wasted."],
            ["About people", "Men and women are made in God's image, equal in dignity, and made for relationship with God and with each other."],
        ], note="Genesis 1 and 2 differ in style and order. Your textbook may explain how Christians understand the difference."),
        D("**Stewardship** means looking after something that belongs to someone else on their behalf. "
          "Genesis speaks of people ruling over and caring for the earth. Many Christians understand this as being God's caretakers, not owners who may destroy.", title="Stewardship"),
        EX("Worked example 1: outlining the six days", intro="State what God created on days 3, 5 and 6 of Genesis 1.", steps=[
            S("Day 3", text="Dry land and seas, then plants and trees."),
            S("Day 5", text="Fish and sea creatures, and birds."),
            S("Day 6", text="Land animals and then human beings, made in God's image."),
        ]),
        EX("Worked example 2: model answer plan", intro="Explain what the creation accounts teach about human beings.", steps=[
            S("Point 1", text="Human beings are made in the image of God and have special dignity."),
            S("Point 2", text="They are made male and female and need each other (the woman is made as a companion)."),
            S("Point 3", text="They are given the work of caring for the garden and ruling the creatures."),
            S("Point 4", text="They are made for relationship with God and are given a rule to obey, which tests trust."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up the order", "In Genesis 1 human beings are made last, on day 6. Plants come on day 3, before the sun, moon and stars of day 4."),
        MISTAKE("Giving the woman's creation to Genesis 1 only", "Genesis 1 says God made them male and female. The story of the woman formed for the man is in Genesis 2."),
        MISTAKE("Saying the sabbath is day 6", "God rested on the seventh day."),
        QUIZ("On which day does Genesis 1 say human beings were created?",
             ["Day 4", "Day 5", "Day 6", "Day 7"], 2,
             "Human beings were made on day 6, after the land animals. Day 7 was the day of rest.",
             hint="They come last in the work of creation, before the rest.",
             feedback=["Day 4 is the sun, moon and stars.", "Day 5 is fish and birds.", "", "Day 7 is the day God rested."]),
        QUIZ("Which idea is a good example of stewardship?",
             ["Cutting down a whole forest for quick money", "Planting trees to replace those cut for timber", "Leaving rubbish in a stream", "Hunting every animal in a reserve"], 1,
             "Stewardship is careful use and care of what we have received. Replanting protects the land for others.",
             hint="Which choice protects the earth for the future?",
             feedback=["This wastes a gift.", "", "This harms the water others use.", "This destroys creatures God called good."]),
        PQ("Name two things that were created on day 1 and day 4 of Genesis 1.", "Day 1: light (separated from darkness). Day 4: the sun, moon and stars."),
        PQ("Give two things the Bible says about the garden of Eden in Genesis 2.", "God planted it and put the man in it to work it and care for it; it had the tree of life and the tree of the knowledge of good and evil."),
        PQ("Explain how a Christian youth group in your town could show stewardship of creation.", "Any two practical ideas with the reason: planting trees, cleaning a stream or market, not wasting water, caring for animals, because the earth is God's gift to be looked after."),
        TIP("Paper 1 asks for facts such as the order of the days and what was made when. Paper 2 essays usually ask what the accounts teach. Cite Genesis 1 and 2 and give a point about God, people and the world."),
        SUM("Genesis 1 tells of creation in six days, with human beings made last and a seventh day of rest.",
            "Genesis 2 tells of the man formed from dust, the garden of Eden, the two special trees and the woman made as a companion.",
            "Both accounts teach that God is the one Creator, that creation is good and that people are made in God's image.",
            "Stewardship means caring for the earth as God's gift."),
    ]))

# ------------------------------------------------------------------ 2 The Fall
LESSONS.append(lesson(
    module=OT1, topic="Creation accounts and the Fall",
    title="The Fall: disobedience in the garden (Genesis 3)",
    slug="rel1-the-fall", minutes=20,
    summary="The story of the serpent, the woman and the man in Genesis 3, the choices made, the consequences, and what Christians learn about obedience, honesty and God's mercy.",
    objectives=[
        "Tell the story of the Fall in the right order",
        "List the consequences of disobedience for the serpent, the woman and the man",
        "Explain what the story teaches about temptation, responsibility and sin",
        "Identify signs of God's care even after the Fall",
    ],
    key_concepts=["Fall", "Temptation", "Sin", "Consequences", "Cain and Abel"],
    blocks=[
        H("Introduction"),
        T("A boy is told by his mother not to touch the money on the table. A friend says, 'Nobody will know.' He takes it. "
          "Later he hides, and when asked, he blames his friend. This ordinary situation helps us understand a famous chapter of the Bible: Genesis 3."),
        D("The **Fall** is the name Christians give to the story in Genesis 3 of how the first man and woman disobeyed God and lost their closeness to him.", title="The Fall"),
        H("The story"),
        T("In the garden, a serpent, described as the most cunning of the wild animals, speaks to the woman. It asks whether God really said they must not eat from any tree. "
          "She answers that they may eat from the trees but not from the tree in the middle, or they will die. "
          "The serpent says they will not die, and that God knows their eyes will be opened and they will be like God. He doubts God's word and suggests that God is keeping something good from them."),
        T("The woman sees that the fruit is good for food and pleasant to look at, and that it is desirable for gaining wisdom. She eats and gives some to her husband, who eats too. "
          "Their eyes are opened and they know they are naked. They sew fig leaves together. They hear God walking in the garden and hide among the trees."),
        T("God calls, 'Where are you?' The man says he was afraid and hid. God asks whether he ate from the forbidden tree. "
          "The man blames the woman (and, in a way, God who gave her). The woman blames the serpent. Nobody simply says, 'I was wrong.'"),
        H("The consequences"),
        KEY("What God says after the disobedience", "Genesis 3 describes consequences for each one.", cards=[
            ["The serpent", "It is cursed above the animals, and there will be enmity between it and the woman's offspring."],
            ["The woman", "Pain in childbirth, and difficulty in the relationship with her husband."],
            ["The man", "The ground is cursed because of him: he will have to toil to grow food, and he will return to the dust."],
            ["Both", "They are sent out of the garden of Eden. Cherubim and a flaming sword guard the way to the tree of life."],
        ], note="Notice that the people are not simply thrown out. The text also says God made clothes of skin for them."),
        T("Many Christians see signs of God's care in the story: God comes looking for the man, God clothes them, and a hopeful promise is made about the offspring of the woman. "
          "Christians often read that promise as an early hint of the coming of Christ. Others stress only the immediate meaning, so check your textbook."),
        IMG("f5rel-1-fall-sequence.svg",
            alt="Flow of five steps: the serpent's question, the eating, the hiding, the questions and blame, the leaving of the garden",
            caption="Figure 1. The sequence of events in Genesis 3."),
        H("After the Fall: Cain and Abel"),
        T("Genesis 4 shows how sin spreads. Cain and Abel bring offerings to God. God accepts Abel's but not Cain's. Cain becomes angry. "
          "God warns him that sin is crouching at the door, but Cain kills his brother. When God asks where Abel is, Cain replies, 'Am I my brother's keeper?' "
          "Cain is sent away to wander. The story teaches that anger, jealousy and refusing responsibility lead to great harm."),
        KEY("Lessons for life", "Use these in application questions.", cards=[
            ["Obedience", "Rules from God and from wise parents protect us. Breaking them damages trust."],
            ["Temptation", "Temptation often begins with doubt and with looking at what we may not have."],
            ["Responsibility", "Blaming others does not remove our own part. Honesty is the first step to repair."],
            ["Mercy", "Even after wrong, God does not abandon people."],
        ]),
        EX("Worked example 1: putting events in order", intro="Put in order: the man and woman hide; the woman eats; God asks 'Where are you?'; the serpent speaks.", steps=[
            S("First", text="The serpent speaks to the woman."),
            S("Second", text="The woman eats and gives some to the man."),
            S("Third", text="They hide when they hear God in the garden."),
            S("Fourth", text="God asks 'Where are you?' and questions them."),
        ]),
        EX("Worked example 2: model answer plan", intro="What does the story of the Fall teach about sin and its results?", steps=[
            S("Point 1", text="Sin begins with doubting God's word and wanting what is forbidden."),
            S("Point 2", text="It spoils relationships: with God (they hide), with each other (blame) and with the earth (toil)."),
            S("Point 3", text="It brings loss: they leave the garden."),
            S("Point 4", text="God still cares: he seeks them out and clothes them."),
        ]),
        H("Common mistakes"),
        MISTAKE("Naming an apple", "The Bible speaks only of the fruit of the tree. It does not name the fruit."),
        MISTAKE("Blaming only the woman in an essay", "The text says she gave to her husband 'who was with her' and he ate as well. Both are held responsible."),
        MISTAKE("Mixing up Genesis 3 and 4", "The Fall is Genesis 3. Cain and Abel is Genesis 4."),
        QUIZ("What did the man do when God asked him about eating the fruit?",
             ["He admitted his fault at once", "He blamed the woman", "He blamed Cain", "He denied that there was any tree"], 1,
             "The man blamed the woman, and the woman blamed the serpent.",
             hint="Think about who was blamed in turn.",
             feedback=["He did not simply admit fault.", "", "Cain is born later.", "He agreed he had eaten."]),
        QUIZ("Which was a consequence for the man in Genesis 3?",
             ["Hard work to get food from the ground", "Pain in childbirth", "Crawling on his belly", "Being sent to Egypt"], 0,
             "The ground was cursed, so the man would toil for his food. Pain in childbirth was for the woman and the belly curse was for the serpent.",
             hint="Match each consequence to the right person.",
             feedback=["", "This was said to the woman.", "This was said to the serpent.", "Egypt belongs to the stories of Joseph."]),
        PQ("Why did the man and woman hide from God?", "They were afraid and ashamed because they had disobeyed him and realised they were naked."),
        PQ("State two ways God showed care after the disobedience.", "He sought them out with a question, he made clothes of skin for them, and he guarded the way to the tree of life so they would not live forever in that state (any two; check your textbook for the last)."),
        PQ("How can the lesson of Cain's question 'Am I my brother's keeper?' be applied in a school?", "We have a duty to care for others: help a classmate being bullied, share, tell the truth about our own mistakes."),
        TIP("Examiners like a clear order of events and the consequences matched to the right person. In application questions, use the words obedience, responsibility and honesty."),
        SUM("Genesis 3 tells how the serpent tempted the woman and both she and the man ate the forbidden fruit.",
            "They hid, then blamed others when God questioned them.",
            "The consequences touched the serpent, the woman and the man, and they were sent out of the garden.",
            "God still cared for them. Genesis 4 shows sin spreading in the story of Cain and Abel."),
    ]))

# ------------------------------------------------------------------ 3 Noah
LESSONS.append(lesson(
    module=OT1, topic="Noah and the Flood",
    title="Noah, the ark and the covenant with creation (Genesis 6 to 9)",
    slug="rel1-noah-and-the-flood", minutes=20,
    summary="The story of Noah in Genesis 6 to 9: human wickedness, Noah's obedience, the ark and the flood, and God's covenant sign of the rainbow.",
    objectives=[
        "Tell the story of Noah in the correct order",
        "Explain why Noah is described as a righteous man",
        "Describe the covenant God made with Noah and its sign",
        "Draw lessons about obedience, faith and care for creation",
    ],
    key_concepts=["Noah", "Ark", "Flood", "Covenant", "Rainbow"],
    blocks=[
        H("Introduction"),
        T("When heavy rains fall in Douala or Limbe, rivers rise and families must decide quickly what to save. "
          "Floods are a serious danger in many places. The Bible tells an ancient story of a great flood and of a man who listened to God and protected his family. Stories of floods are found in the traditions of many peoples. We study here the account in Genesis."),
        H("Why the flood came"),
        T("Genesis 6 says that people on the earth had become very wicked and that violence filled the earth. The text says God was grieved. "
          "But Noah found favour with God. He is described as a righteous man, blameless among the people of his time, who walked with God. He had three sons: Shem, Ham and Japheth."),
        H("The ark and the flood"),
        T("God told Noah to build an ark, a very large wooden boat. The Bible gives its size as 300 cubits long, 50 wide and 30 high (a cubit is roughly the length of a forearm). "
          "Noah was to take his wife, his three sons and their wives, and pairs of the animals and birds so that life would continue. The text says Noah did all that God commanded."),
        T("Then the rain fell for forty days and forty nights and the waters covered the earth. After many days the waters began to go down. "
          "The ark came to rest on the mountains of Ararat. Noah sent out a raven and then a dove. The dove first found nowhere to rest, and later returned with an olive leaf. "
          "Later it did not return at all, and Noah knew the land was dry."),
        T("Noah and his family came out of the ark. Noah built an altar and offered sacrifices to God."),
        D("A **covenant** is a solemn agreement in which God makes promises and often asks for a response from people. "
          "The Bible describes several covenants: with Noah, Abraham, Moses and David.", title="Covenant"),
        H("The covenant with Noah"),
        T("In Genesis 9 God makes a covenant with Noah, with his descendants and with every living creature. God promises never again to destroy the earth by a flood. "
          "The sign of this covenant is the rainbow in the clouds. When God sees it he remembers his promise."),
        IMG("f5rel-1-noah-sequence.svg",
            alt="Sequence from wickedness and Noah's favour, building the ark, forty days of rain, the dove and the olive leaf, the altar and the rainbow",
            caption="Figure 1. The main events of the Noah story."),
        KEY("What Christians learn from Noah", "Useful points for essays.", cards=[
            ["Obedience and faith", "Noah trusted God and built the ark before there was any sign of rain. He acted on God's word."],
            ["Judgement and mercy", "Evil has serious results, but God saves Noah's family and keeps a promise."],
            ["Care for creation", "The animals were saved too. The covenant includes every living creature."],
            ["A promise to rely on", "The rainbow reminds people that God keeps his word."],
        ]),
        EX("Worked example 1: sequence", intro="Arrange: the dove returns with an olive leaf; God promises never again to flood the earth; Noah builds the ark; rain falls for forty days.", steps=[
            S("First", text="Noah builds the ark."),
            S("Second", text="Rain falls for forty days and nights."),
            S("Third", text="The dove returns with an olive leaf."),
            S("Fourth", text="God makes the covenant and gives the rainbow."),
        ]),
        EX("Worked example 2: model answer plan", intro="Describe the covenant God made with Noah.", steps=[
            S("Who", text="God made it with Noah, his sons, their descendants and every living creature."),
            S("Promise", text="Never again would a flood destroy all life on earth."),
            S("Sign", text="The rainbow in the clouds."),
            S("Meaning", text="God is faithful and merciful, and the creation is under his care."),
        ]),
        H("Common mistakes"),
        MISTAKE("Counting the sons wrongly", "Noah had three sons: Shem, Ham and Japheth."),
        MISTAKE("Giving the rainbow as the sign of Abraham's covenant", "The rainbow is the sign of the covenant with Noah. Circumcision is the sign for Abraham."),
        MISTAKE("Saying it rained for forty years", "The rain fell for forty days and forty nights."),
        QUIZ("What was the sign of God's covenant with Noah?",
             ["Circumcision", "The rainbow", "The sabbath", "A burning bush"], 1,
             "The rainbow in the clouds was the sign that God would never again flood the whole earth.",
             hint="Look to the sky.",
             feedback=["That is the sign for Abraham.", "", "The sabbath is linked to creation and to Sinai.", "That is how God met Moses."]),
        QUIZ("Why is Noah remembered as a good example?",
             ["He was a king", "He trusted and obeyed God when others did not", "He built a temple", "He led Israel out of Egypt"], 1,
             "Noah is described as righteous. He did what God commanded.",
             hint="Think about the character of Noah, not an office.",
             feedback=["Noah was not a king.", "", "Solomon built the temple.", "That was Moses."]),
        PQ("Name Noah's three sons.", "Shem, Ham and Japheth."),
        PQ("Which two birds did Noah send out, and what did the second one bring back?", "A raven and a dove; the dove returned with an olive leaf (a sign the waters had gone down)."),
        PQ("A church in your village is asked to help families after a flood. How could the story of Noah encourage them?", "It teaches care for others in danger, trust that God keeps his promises, and responsible care of people and animals; the church can give shelter, food and clothes."),
        TIP("In Paper 1, remember the numbers and names: forty days, three sons, the olive leaf. In essays, link Noah to the idea of covenant, because the same word returns with Abraham, Moses and David."),
        SUM("Genesis says human wickedness grew, but Noah found favour and obeyed God by building the ark.",
            "The flood lasted a long time and Noah's family and the animals were saved.",
            "God made a covenant with Noah and every living creature, with the rainbow as its sign.",
            "The story teaches obedience, faith, judgement with mercy and care for creation."),
    ]))

# ------------------------------------------------------------------ 4 Abraham
LESSONS.append(lesson(
    module=OT1, topic="The Abrahamic covenant",
    title="Abraham: call, covenant and testing of faith",
    slug="rel1-abrahamic-covenant", minutes=22,
    summary="God's call to Abram, the promises of land, descendants and blessing, the covenant sign of circumcision, the birth of Isaac and the test on Mount Moriah.",
    objectives=[
        "Describe the call of Abram and the promises God made to him",
        "Explain the covenant of Genesis 15 and 17 and its sign",
        "Tell the story of the birth of Isaac and the test of Genesis 22",
        "Explain why Abraham is called an example of faith",
    ],
    key_concepts=["Call of Abram", "Promise", "Covenant", "Circumcision", "Faith", "Isaac"],
    blocks=[
        H("Introduction"),
        T("Many Cameroonian families have a story of a grandfather who left the village to settle in a new place, trusting that the family would one day prosper. "
          "The Bible's story of Abraham begins in a similar way: a man leaves his homeland on the word of God without knowing exactly where he is going."),
        H("The call of Abram"),
        T("Abram (later called Abraham) lived with his father Terah's family in Ur of the Chaldeans, in Mesopotamia. The family moved to Haran. "
          "In Genesis 12 God tells Abram to leave his country, his relatives and his father's house and go to the land that God would show him. Abram was seventy-five years old when he left Haran, with his wife Sarai and his nephew Lot."),
        KEY("The promises of Genesis 12", "God made three connected promises.", cards=[
            ["A land", "Abram would be given a land (Canaan)."],
            ["Descendants", "He would become a great nation, though his wife Sarai could not have children."],
            ["Blessing", "God would bless him and, through him, all the families of the earth."],
        ]),
        IMG("f5rel-1-abraham-journey-map.svg",
            alt="Schematic map with arrows from Ur to Haran to Canaan, then a side trip to Egypt and back, with the Mediterranean Sea and the Nile marked",
            caption="Figure 1. Abraham's journey (schematic, not to scale)."),
        T("Abram arrived in Canaan, built altars and lived as a traveller. A famine forced him to go to Egypt for a time. Later he and Lot separated peacefully, because their flocks had grown too large. "
          "Abram let Lot choose first, which shows generosity."),
        H("The covenant"),
        T("In Genesis 15 God appears to Abram and promises a son of his own. God takes him outside and tells him to look at the stars and count them if he can: so numerous will his descendants be. "
          "The text says Abram believed the Lord, and the Lord counted it to him as righteousness. A ritual with animals follows, which was a way of making a solemn covenant in the ancient Near East."),
        D("In the ancient Near East, kings made **covenants** (treaties) with their people or with other kings. The Bible uses this familiar idea to show that God binds himself by promise to his people. "
          "In the covenant with Abraham, the promise comes first, from God's own free choice.", title="Covenant in the ancient world"),
        T("In Genesis 17 God confirms the covenant. Abram's name becomes Abraham ('father of many') and Sarai's becomes Sarah. "
          "The sign of the covenant is circumcision, to be carried out on every male in Abraham's household. God also promises that Sarah will bear a son and that he will be named Isaac."),
        H("Isaac and the test on Moriah"),
        T("Abraham was a hundred years old when Isaac was born (Genesis 21). Earlier Abraham had a son Ishmael with Sarah's servant Hagar. "
          "Genesis 22 tells that God tested Abraham by asking him to offer Isaac as a sacrifice on a mountain in the region of Moriah. "
          "Abraham obeyed and travelled with Isaac, but at the last moment an angel stopped him. Abraham saw a ram caught in a thicket and offered it instead. God renewed the promise."),
        T("Christians and Jews read this story as a lesson about trust in God. The text itself stresses that God did not want the death of the child and that God provided. Teachers may explain the story in slightly different ways, so check your textbook."),
        EX("Worked example 1: promises", intro="State the three promises made to Abram in Genesis 12.", steps=[
            S("Land", text="He would receive a land."),
            S("Descendants", text="He would become a great nation."),
            S("Blessing", text="God would bless him, and all the families of the earth would be blessed through him."),
        ]),
        EX("Worked example 2: model answer plan", intro="Why is Abraham called a man of faith?", steps=[
            S("Point 1", text="He left home at God's word, not knowing where he was going."),
            S("Point 2", text="He believed God's promise of descendants when he and Sarah were old."),
            S("Point 3", text="He was willing to obey God's test on Moriah."),
            S("Conclusion", text="Faith for Abraham meant trust shown in action."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing the signs of the covenants", "Rainbow: Noah. Circumcision: Abraham. The sabbath is linked to Sinai and creation."),
        MISTAKE("Saying Ishmael was Sarah's son", "Ishmael was the son of Abraham and Hagar. Isaac was the son of Abraham and Sarah."),
        MISTAKE("Saying Abraham lived in Egypt for life", "He went to Egypt only for a time because of a famine. He lived mostly in Canaan."),
        QUIZ("What was the sign of the covenant in Genesis 17?",
             ["The rainbow", "Circumcision", "The Passover meal", "The tablets of stone"], 1,
             "Circumcision of every male in the household was the sign of the covenant with Abraham.",
             hint="Abraham's name changes in the same chapter.",
             feedback=["That belongs to Noah.", "", "That belongs to the Exodus.", "That belongs to Sinai."]),
        QUIZ("How did Abraham's journey begin?",
             ["He fled from Pharaoh", "God called him to leave his country for a land God would show", "He was sold by his brothers", "He was sent by Saul"], 1,
             "In Genesis 12 God called Abram to go to the land he would show him.",
             hint="Think of the first words of God to Abram.",
             feedback=["That fits Moses.", "", "That fits Joseph.", "Saul lived much later."]),
        PQ("Name the wife of Abraham and the son she bore to him.", "Sarah, and the son was Isaac."),
        PQ("What happened at the end of the test on Mount Moriah?", "An angel stopped Abraham, he found a ram and offered it instead of Isaac, and God renewed the promise."),
        PQ("Give one way a Christian could show 'faith like Abraham' when moving to a new town for study or work.", "Trust God for guidance and protection, pray, and keep honest and faithful in the new place, while working hard (trust shown in action)."),
        TIP("Paper 1 often asks for the promises or the sign of each covenant. Make a small table in your notes: Noah (rainbow), Abraham (circumcision), Moses (law and sabbath)."),
        SUM("God called Abram to leave his homeland, promising land, descendants and blessing for all families.",
            "God made a covenant with him, changed his name to Abraham and gave circumcision as its sign.",
            "Isaac was born when Abraham was a hundred, and God tested Abraham on Mount Moriah.",
            "Abraham is an example of faith: trust shown in obedience."),
    ]))

# ------------------------------------------------------------------ 5 Jacob
LESSONS.append(lesson(
    module=OT1, topic="Jacob and Joseph",
    title="Jacob: birthright, blessing, Bethel and reconciliation",
    slug="rel1-jacob", minutes=20,
    summary="Jacob and Esau, the birthright and the blessing, the dream at Bethel, Jacob's years with Laban, his new name Israel and his reconciliation with Esau.",
    objectives=[
        "Tell the main events in the life of Jacob in order",
        "Explain the birthright and the blessing and how Jacob gained them",
        "Describe the dream at Bethel and the meeting at Peniel",
        "Draw lessons about deceit, consequences, forgiveness and God's faithfulness",
    ],
    key_concepts=["Esau", "Birthright", "Blessing", "Bethel", "Israel", "Reconciliation"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian families the eldest son carries special responsibilities when the father dies, and property is often discussed with great care. "
          "Rivalry between brothers can cause deep hurt. The story of Jacob and Esau is about two brothers, a family inheritance and the long road to peace."),
        H("Two brothers"),
        T("Isaac and Rebekah had twin sons. Esau was born first and was a hunter and a man of the open country. Jacob was born holding his brother's heel and was a quiet man who stayed among the tents. "
          "The older son had the **birthright**, the special share of the inheritance and family leadership. One day Esau came home hungry and sold his birthright to Jacob for a meal of stew. The Bible says Esau despised his birthright."),
        D("The **blessing** was a father's solemn spoken words, given before death, passing on God's favour and leadership to a chosen son. Once spoken, it could not be taken back.", title="Blessing"),
        T("When Isaac was old and almost blind, he asked Esau to hunt and prepare a meal, so that he could bless him. Rebekah overheard and helped Jacob to deceive his father. "
          "Jacob wore Esau's clothes and covered his arms with goat skins, and received the blessing. Esau was bitter and planned to kill Jacob. Jacob had to flee."),
        H("Bethel and Laban"),
        T("On the way to Haran, where his mother's brother Laban lived, Jacob stopped to sleep at a place that he later called Bethel ('house of God'). "
          "In a dream he saw a stairway between earth and heaven with angels going up and down. God repeated to Jacob the promises made to Abraham and Isaac and said he would be with him. Jacob set up a stone as a pillar."),
        T("Jacob worked for Laban for many years. He loved Rachel and agreed to work seven years for her, but Laban gave him Leah first, so Jacob worked another seven for Rachel. "
          "Jacob had twelve sons by Leah, Rachel and their two servants: Reuben, Simeon, Levi, Judah, Dan, Naphtali, Gad, Asher, Issachar, Zebulun, Joseph and Benjamin. Laban also cheated Jacob over his wages, so Jacob had learned how it feels to be deceived."),
        IMG("f5rel-1-jacob-sequence.svg",
            alt="Sequence of stages: birthright, blessing, flight, Bethel dream, years with Laban, Peniel, meeting Esau",
            caption="Figure 1. The life of Jacob in order."),
        H("Peniel and reconciliation"),
        T("Years later God told Jacob to return home. Jacob was afraid of Esau. He sent gifts ahead and prayed. "
          "The night before the meeting, a man wrestled with him until dawn at the river Jabbok. Jacob refused to let go until he received a blessing. He was given a new name, **Israel**, and he walked with a limp afterwards. He named the place Peniel."),
        T("When Esau arrived with four hundred men, he ran to meet Jacob, embraced him and wept. The two brothers were reconciled. The descendants of Jacob's twelve sons became the twelve tribes of Israel."),
        KEY("Lessons from Jacob", "Use these in application questions.", cards=[
            ["Wrong acts have consequences", "Jacob gained the blessing by deceit, but he lost home and family for many years and was deceived in turn."],
            ["God's faithfulness", "God did not abandon Jacob. The promise continued, even through a flawed person."],
            ["Forgiveness and peace", "Esau's welcome shows the strength of forgiveness. Jacob first prepared humbly to make peace."],
            ["Change", "The man who grasped at heels became Israel, a name for a whole people."],
        ]),
        EX("Worked example 1: facts", intro="Give three facts about Jacob's dream at Bethel.", steps=[
            S("Fact 1", text="He was fleeing from Esau and slept with a stone for a pillow."),
            S("Fact 2", text="He saw a stairway to heaven with angels going up and down."),
            S("Fact 3", text="God promised to be with him and repeated the promises to Abraham; Jacob named the place Bethel."),
        ]),
        EX("Worked example 2: model answer plan", intro="How did Jacob and Esau come to be reconciled?", steps=[
            S("Fear", text="Jacob feared Esau and sent gifts ahead and prayed."),
            S("Peniel", text="He wrestled at Jabbok and became Israel, a changed man."),
            S("Meeting", text="Esau ran to meet him, embraced him and wept."),
            S("Lesson", text="Honesty about wrong and humble gifts opened the way to peace."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing the birthright and the blessing", "The birthright was bought for stew (Genesis 25). The blessing was gained by deceit (Genesis 27)."),
        MISTAKE("Saying Esau was the younger twin", "Esau was born first. Jacob was born second."),
        MISTAKE("Counting Joseph as Leah's son", "Joseph and Benjamin were the sons of Rachel. Reuben to Judah were Leah's first four sons."),
        QUIZ("What did Esau give up for a bowl of stew?",
             ["His blessing", "His birthright", "His tent", "His flock"], 1,
             "Esau sold his birthright to Jacob. The blessing was gained later by deceit.",
             hint="Which of the two things was bought, and which was tricked from Isaac?",
             feedback=["The blessing came through Isaac and Rebekah's plan.", "", "The text does not say this.", "The text does not say this."]),
        QUIZ("What new name was Jacob given at Jabbok?",
             ["Abraham", "Israel", "Isaac", "Judah"], 1,
             "After wrestling through the night he received the name Israel.",
             hint="It became the name of a nation.",
             feedback=["Abraham was the name given to Abram.", "", "Isaac was his father.", "Judah was one of his sons."]),
        PQ("Name the place where Jacob dreamed of the stairway, and say what the name means.", "Bethel, meaning 'house of God'."),
        PQ("Give two ways Rebekah and Jacob deceived Isaac.", "Jacob pretended to be Esau; he wore Esau's clothes and put goat skins on his arms and neck so that he felt hairy; he brought the prepared meal and claimed it was game."),
        PQ("Two cousins in your church quarrel about an inheritance. How could Jacob and Esau's story guide them?", "Be honest about wrongs, offer to make peace, forgive as Esau did, and do not hold anger for years."),
        TIP("Paper 1 likes the names of the twelve sons, the place names Bethel and Peniel, and who got the birthright and blessing. Write the sons in order with their mothers."),
        SUM("Jacob gained Esau's birthright for stew and the blessing by deceit, and fled.",
            "At Bethel God confirmed the promises to him in a dream.",
            "He worked for Laban, married Leah and Rachel and had twelve sons.",
            "At Peniel he became Israel, and he and Esau were reconciled."),
    ]))

# ------------------------------------------------------------------ 6 Joseph
LESSONS.append(lesson(
    module=OT1, topic="Jacob and Joseph",
    title="Joseph in Egypt: from slavery to ruler",
    slug="rel1-joseph-in-egypt", minutes=22,
    summary="Joseph's dreams and betrayal by his brothers, his years in Potiphar's house and in prison, his rise under Pharaoh and his forgiveness of his family.",
    objectives=[
        "Tell the story of Joseph from the dreams to the reunion",
        "Explain how Joseph rose to power and used it",
        "Describe how the family came to live in Egypt",
        "Explain the lesson of Genesis 50 on forgiveness and God's purposes",
    ],
    key_concepts=["Joseph", "Dreams", "Potiphar", "Pharaoh", "Famine", "Forgiveness", "Goshen"],
    blocks=[
        H("Introduction"),
        T("Think of a young person whose own family treats them unfairly, who ends up far from home, works hard and honestly in difficult places, and later has the chance to take revenge but chooses mercy. "
          "That is the shape of the story of Joseph, which fills the last chapters of Genesis (37 to 50)."),
        H("Joseph and his brothers"),
        T("Jacob loved Joseph, the son of his old age, more than his other sons and gave him a special robe (translations describe it as a long robe or a coat of many colours). "
          "Joseph had two dreams in which his brothers' sheaves bowed to his sheaf, and the sun, moon and eleven stars bowed to him. He told them, and his brothers hated him more."),
        T("When the brothers were herding far away, Jacob sent Joseph to check on them. They planned to kill him, but Reuben and Judah argued for another way. "
          "They sold Joseph for twenty pieces of silver to traders on their way to Egypt. They dipped his robe in goat's blood and told their father a wild animal had killed him."),
        H("Egypt: Potiphar, prison and Pharaoh"),
        T("In Egypt, Joseph was bought by Potiphar, an officer of Pharaoh. The Bible says the Lord was with Joseph and he prospered, and Potiphar put him in charge of the house. "
          "Potiphar's wife tried to lead Joseph into wrong. He refused, saying it would be a sin against God and against his master. She accused him falsely, and Joseph was thrown into prison."),
        T("In prison, Joseph again served faithfully and was put in charge of the other prisoners. He explained the dreams of two of Pharaoh's officials, the cupbearer and the baker. His explanations came true, but the cupbearer forgot him for two years."),
        T("Then Pharaoh had two troubling dreams: seven fat cows eaten by seven thin cows, and seven good ears of grain swallowed by seven thin ones. "
          "The cupbearer remembered Joseph. Joseph said that God was giving Pharaoh the answer: seven years of plenty would be followed by seven years of famine. "
          "He advised Pharaoh to store grain during the good years under a wise official. Pharaoh made Joseph governor over Egypt, second only to himself."),
        IMG("f5rel-1-joseph-timeline.svg",
            alt="Timeline: dreams, sold to traders, Potiphar's house, prison, Pharaoh's dreams, governor, famine, reunion, move to Goshen",
            caption="Figure 1. Joseph's story from the dreams to Egypt."),
        H("Famine, reunion and forgiveness"),
        T("The famine spread over the region, and Jacob sent his sons to Egypt to buy grain. They bowed before the governor without recognising him. "
          "Joseph tested them, and Judah offered to remain as a slave in place of Benjamin so their father would not be crushed again. Joseph wept and told them, 'I am Joseph.' "
          "He said that God had sent him ahead of them to save lives. Jacob and his whole family moved to Egypt and settled in the region of Goshen."),
        T("After Jacob died, the brothers feared Joseph would now take revenge. Joseph reassured them. In Genesis 50 he said, in effect, that they had meant evil but God had turned it to good, to save many lives."),
        KEY("What the story teaches", "Use in essays and application questions.", cards=[
            ["Faithfulness in hard times", "Joseph stayed honest as a slave and a prisoner, and the Bible says God was with him."],
            ["Forgiveness", "He chose mercy over revenge and restored his family."],
            ["God's purpose", "God can bring good out of wrong, though the story never excuses the wrongdoing of the brothers."],
            ["Wise leadership", "Planning ahead in good years saved many in the famine."],
        ]),
        EX("Worked example 1: events in order", intro="Put in order: Joseph is made governor; Joseph is sold; Joseph interprets Pharaoh's dreams; Joseph is put in prison.", steps=[
            S("First", text="Joseph is sold to traders by his brothers."),
            S("Second", text="He is put in prison after the false accusation."),
            S("Third", text="He interprets Pharaoh's dreams."),
            S("Fourth", text="He is made governor."),
        ]),
        EX("Worked example 2: model answer plan", intro="Explain what the story of Joseph teaches about forgiveness.", steps=[
            S("The wrong", text="His brothers hated him, sold him and deceived their father."),
            S("The power", text="Years later Joseph could have punished them."),
            S("The choice", text="He wept, forgave them and provided food and land for the family."),
            S("The reason", text="He saw God's hand in events and wanted to save life."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Joseph's brothers sold him to Pharaoh", "They sold him to traders. Potiphar, an officer of Pharaoh, bought him in Egypt."),
        MISTAKE("Mixing up the cupbearer and Pharaoh's dreams", "The cupbearer and the baker had one dream each in prison. Pharaoh's two dreams were about cows and grain."),
        MISTAKE("Saying the seven years of famine came first", "Seven years of plenty came first, then seven years of famine."),
        QUIZ("What advice did Joseph give Pharaoh after the dreams?",
             ["Raise an army", "Store grain in the years of plenty", "Send the Hebrews away", "Build a temple"], 1,
             "Joseph advised storing food during seven good years, to be ready for seven years of famine.",
             hint="Think of what a government does before a famine.",
             feedback=["The dreams were about food, not war.", "", "That is not in the story.", "That is not in the story."]),
        QUIZ("Why did Joseph's brothers hate him?",
             ["He refused to work", "Their father favoured him and he told them dreams in which they bowed to him", "He was older than them", "He had left home"], 1,
             "They hated him for his father's special love and his dreams of ruling over them.",
             hint="Two things are mentioned in Genesis 37.",
             feedback=["The text does not say this.", "", "He was one of the younger sons.", "He had not left home yet."]),
        PQ("Why was Joseph put in prison?", "Potiphar's wife falsely accused him after he refused her."),
        PQ("Where did Jacob's family settle in Egypt?", "In Goshen."),
        PQ("A church member was cheated by a relative and later has the chance to repay them. How can Joseph's example help?", "Be merciful, forgive, trust that God can bring good out of hard times, and use position to help, not to punish."),
        TIP("Paper 1 often asks about the cupbearer, Potiphar, Goshen or the silver price. Keep a one-line timeline of the story in order."),
        SUM("Joseph's brothers hated him, sold him to traders and deceived their father.",
            "In Egypt he served in Potiphar's house, was falsely accused and imprisoned, then explained Pharaoh's dreams and became governor.",
            "Famine brought his brothers to Egypt, and Joseph forgave them.",
            "The family settled in Goshen. The story teaches faithfulness, forgiveness and trust in God's purposes."),
    ]))

# ------------------------------------------------------------------ 7 Call of Moses
LESSONS.append(lesson(
    module=OT1, topic="Moses, the Passover and the Exodus",
    title="Moses: birth, flight to Midian and the call at the burning bush",
    slug="rel1-call-of-moses", minutes=20,
    summary="Israel's oppression in Egypt, the birth and upbringing of Moses, his flight to Midian and God's call at the burning bush (Exodus 1 to 4).",
    objectives=[
        "Explain why the Israelites suffered in Egypt",
        "Tell how Moses was saved and raised in Pharaoh's household",
        "Describe the call of Moses at the burning bush and his objections",
        "Explain what the call teaches about God and about leadership",
    ],
    key_concepts=["Oppression", "Moses", "Midian", "Burning bush", "I AM", "Aaron"],
    blocks=[
        H("Introduction"),
        T("People who have suffered unfair treatment often long for someone to speak up for them. The book of **Exodus**, whose name means 'going out', begins with a people in slavery and with the story of the leader God called to bring them out."),
        H("Oppression in Egypt"),
        T("Joseph's family grew into a large people. Exodus 1 says a new king arose who did not know Joseph. He feared that the Israelites were too many and might join Egypt's enemies. "
          "He forced them into hard labour, building store cities, and made their lives bitter. He then ordered that every Hebrew baby boy be thrown into the Nile."),
        H("The birth and upbringing of Moses"),
        T("A Hebrew woman of the tribe of Levi hid her baby son for three months. When she could hide him no longer, she placed him in a waterproof basket among the reeds at the edge of the Nile. "
          "His sister Miriam watched. Pharaoh's daughter came to bathe, found the child and took pity. Miriam offered to find a nurse, and brought the baby's own mother. "
          "The child grew up in the palace and was named **Moses**, a name the text links to being drawn from the water."),
        T("As a grown man Moses saw an Egyptian beating a Hebrew. He killed the Egyptian and hid the body. When he learned the matter was known, he fled to the land of Midian. "
          "There he married Zipporah, the daughter of the priest Jethro, and spent many years as a shepherd."),
        H("The burning bush"),
        T("While looking after Jethro's flock near Mount Horeb (also called the mountain of God), Moses saw a bush burning but not burned up. "
          "God called him by name from the bush. Moses was told to take off his sandals because the ground was holy. "
          "God said he had seen the suffering of his people, heard their cry and would rescue them, and that he was sending Moses to Pharaoh."),
        D("When Moses asked God's name, he was told, 'I AM WHO I AM'. Christians and Jews understand this name as showing that God is the living God, ever present and faithful, the God of Abraham, Isaac and Jacob.", title="The divine name"),
        KEY("Moses' objections and God's replies", "Moses was a reluctant leader.", cards=[
            ["'Who am I?'", "God said, 'I will be with you.'"],
            ["'What is your name?'", "God gave his name and said he was the God of their ancestors."],
            ["'They will not believe me'", "God gave him signs: the staff that became a snake and the hand that became diseased and was healed."],
            ["'I am slow of speech'", "God said he would help his speaking and allowed Aaron, his brother, to speak for him."],
        ]),
        IMG("f5rel-1-moses-early-life.svg",
            alt="Timeline: Hebrew baby boys ordered killed, Moses in the basket, palace, flight to Midian, burning bush",
            caption="Figure 1. Moses from birth to the burning bush."),
        EX("Worked example 1: facts", intro="Name the people who helped save the baby Moses.", steps=[
            S("Mother", text="She hid him for three months, then placed him in a basket on the Nile."),
            S("Miriam", text="His sister watched and offered to bring a nurse."),
            S("Pharaoh's daughter", text="She found the baby, took pity and adopted him."),
        ]),
        EX("Worked example 2: model answer plan", intro="Explain what the call of Moses teaches about God.", steps=[
            S("Point 1", text="God sees suffering and hears the cry of the oppressed."),
            S("Point 2", text="God is holy; Moses removes his sandals."),
            S("Point 3", text="God keeps his promises to Abraham, Isaac and Jacob."),
            S("Point 4", text="God works through ordinary, even reluctant, people and promises, 'I will be with you.'"),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Moses was born in Midian", "He was born in Egypt, raised in the palace, and fled to Midian as an adult."),
        MISTAKE("Mixing up Aaron and Miriam", "Aaron was the brother who spoke for Moses. Miriam was the sister who watched the basket."),
        MISTAKE("Saying the burning bush was in Egypt", "It was in the wilderness near Mount Horeb in the land of Midian."),
        QUIZ("Why did Moses flee from Egypt?",
             ["He was sent by Pharaoh", "He killed an Egyptian who was beating a Hebrew", "The plagues began", "He wanted to see Jethro"], 1,
             "After killing the Egyptian, Moses feared that the matter was known and ran to Midian.",
             hint="Think of the event that came just before the flight.",
             feedback=["Pharaoh wanted him dead, not sent.", "", "The plagues came later.", "He met Jethro only after he arrived."]),
        QUIZ("Who was appointed to speak for Moses?",
             ["Joshua", "Miriam", "Aaron", "Jethro"], 2,
             "Moses said he was slow of speech, so God allowed his brother Aaron to speak for him.",
             hint="He was Moses' brother.",
             feedback=["Joshua later led Israel into Canaan.", "Miriam was his sister.", "", "Jethro was his father-in-law."]),
        PQ("Why did Moses take off his sandals at the burning bush?", "The ground was holy because God was present there."),
        PQ("State two excuses Moses gave to avoid the task.", "He asked who he was to go to Pharaoh; he said the people would not believe him; he said he was slow of speech (any two)."),
        PQ("How could the call of Moses encourage a young person who feels too weak for a task in their church or community?", "God calls ordinary people and promises to be with them; help from others, like Aaron, shows we need teamwork."),
        TIP("Paper 1 tests the names (Jethro, Zipporah, Aaron, Miriam) and the place (Midian, Horeb). Essays ask what the call teaches about God and about leadership."),
        SUM("Pharaoh oppressed the Israelites and ordered their baby boys killed; Moses was saved in a basket and raised in the palace.",
            "After killing an Egyptian he fled to Midian, married Zipporah and kept sheep.",
            "At the burning bush God called him to lead the people out of Egypt and promised to be with him.",
            "Moses objected, but Aaron was given to help him."),
    ]))

# ------------------------------------------------------------------ 8 Passover and Exodus
LESSONS.append(lesson(
    module=OT1, topic="Moses, the Passover and the Exodus",
    title="The plagues, the Passover and the crossing of the sea",
    slug="rel1-passover-and-exodus", minutes=22,
    summary="The ten plagues, the first Passover night, the escape from Egypt and the crossing of the sea, with the meaning of the Passover for Jews and Christians.",
    objectives=[
        "List the ten plagues in order",
        "Describe the first Passover and its meaning",
        "Tell the story of the Exodus and the crossing of the sea",
        "Explain why the Exodus is central to the faith of Israel",
    ],
    key_concepts=["Ten plagues", "Passover", "Unleavened bread", "Exodus", "Red Sea", "Deliverance"],
    blocks=[
        H("Introduction"),
        T("Every year on Independence Day or Unification Day, Cameroonians remember a founding event. In the same way, the Exodus is the founding event of Israel: the night and the journey in which, the Bible says, God brought his people out of slavery."),
        H("Moses before Pharaoh"),
        T("Moses and Aaron asked Pharaoh to let the people go to worship in the wilderness. Pharaoh refused and made the work harder. "
          "Exodus 7 to 11 describes ten plagues, each one a sign. The Bible says Pharaoh's heart was hard and he refused again and again."),
        CODE("""1  The Nile turned to blood
2  Frogs
3  Gnats (or lice)
4  Flies
5  Disease on the livestock
6  Boils
7  Hail
8  Locusts
9  Darkness
10 Death of the firstborn""", "text", title="The ten plagues in order"),
        T("Translations differ slightly on the third and fourth plagues. Check your Bible. The order of the ten is the same."),
        H("The Passover"),
        T("Before the tenth plague, God told Moses what each Israelite family must do (Exodus 12). On the tenth day of the month each household chose a lamb without defect. "
          "On the fourteenth evening they killed it and put some of the blood on the two doorposts and the lintel of the house. They roasted the lamb and ate it with bitter herbs and bread without yeast, dressed to travel, in haste. "
          "God said that at midnight he would pass through Egypt and strike the firstborn, but would **pass over** every house marked with the blood."),
        D("The **Passover** is the festival that remembers the night the Lord passed over the houses of the Israelites. **Unleavened bread** (bread made without yeast) recalls the haste of the departure. "
          "Jews still keep the Passover each year. The Bible commands that the story be told to the children.", title="Passover"),
        T("That night there was a great cry in Egypt. Pharaoh called Moses and Aaron and told them to leave. The Egyptians urged the people to hurry."),
        H("The Exodus and the crossing"),
        T("The Israelites left, with their flocks and herds, led by a pillar of cloud by day and a pillar of fire by night. "
          "Pharaoh changed his mind and pursued them with chariots. The people were trapped between the army and the sea and were afraid. "
          "Moses told them not to be afraid. He stretched out his hand over the sea, and a strong wind drove the waters back, so the people crossed on dry ground. "
          "When the Egyptians followed, the waters returned and covered them. Hebrew calls this the 'sea of reeds'; many Bibles say 'Red Sea'."),
        T("In Exodus 15, Moses and the people sang a song of praise, and Miriam took a tambourine and led the women in singing and dancing."),
        IMG("f5rel-1-exodus-route-map.svg",
            alt="Schematic map with Egypt on the left, an arrow across the sea, the wilderness and Mount Sinai in the middle, and Canaan on the right",
            caption="Figure 1. The route of the Exodus (schematic; scholars differ on the exact places)."),
        KEY("Why the Exodus matters", "For Israel and for Christians.", cards=[
            ["For Israel", "It is the great act of deliverance, the reason Israel worships God who saves. Many later writers look back to it."],
            ["For Christians", "Christians see a link between the Passover lamb and Christ, who died around the time of Passover, and between Passover and the Lord's Supper."],
            ["For all", "God cares about the oppressed and calls people to act for freedom and justice."],
        ]),
        EX("Worked example 1: the tenth night", intro="State three things Israelite families did on the Passover night.", steps=[
            S("Step 1", text="Killed a lamb and put its blood on the doorposts and lintel."),
            S("Step 2", text="Ate the roasted lamb with unleavened bread and bitter herbs."),
            S("Step 3", text="Ate in haste, dressed ready to leave, and stayed indoors."),
        ]),
        EX("Worked example 2: model answer plan", intro="Why is the Passover important to Jews and Christians?", steps=[
            S("Meaning for Jews", text="It remembers God's rescue from slavery and is kept every year, with the story told to children."),
            S("Meaning for Christians", text="Christians read the Passover lamb as a sign pointing to Christ's sacrifice and link it to the Last Supper."),
            S("Lesson", text="God saves his people and people should remember his goodness."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing the order of plagues", "The first is blood, the last is the death of the firstborn. Learn the list as a chant."),
        MISTAKE("Saying Pharaoh agreed after the first plague", "The Bible says Pharaoh hardened his heart through many plagues, and let the people go only after the tenth."),
        MISTAKE("Saying the Red Sea crossing was before the Passover", "The Passover night came first. The crossing of the sea came after Pharaoh pursued the people."),
        QUIZ("Which was the tenth plague?",
             ["Darkness", "Locusts", "Death of the firstborn", "Hail"], 2,
             "The tenth plague was the death of the firstborn of Egypt. Darkness was the ninth.",
             hint="It is the plague that led Pharaoh to let the people go.",
             feedback=["Darkness was the ninth.", "Locusts were the eighth.", "", "Hail was the seventh."]),
        QUIZ("What did the Israelites put on their doorposts at Passover?",
             ["Oil", "Blood of the lamb", "Water from the Nile", "Flour"], 1,
             "The blood of the lamb marked their houses, and the Lord passed over them.",
             hint="It is the origin of the name 'Passover'.",
             feedback=["Oil is not part of the Passover instructions.", "", "The Nile was turned to blood in the first plague, not used on doors.", "Flour belongs to bread, not the doorpost."]),
        PQ("Name the first three plagues.", "The Nile turned to blood, frogs, gnats (or lice)."),
        PQ("Why did the Israelites eat unleavened bread at the first Passover?", "They were leaving in haste and had no time for bread to rise."),
        PQ("How could a church community act on the lesson that God cares for the oppressed?", "Support people being treated unfairly or kept in poverty, help the sick and the poor, speak against injustice."),
        TIP("The ten plagues and the Passover details are common Paper 1 items. Learn the list. Essays link Passover to deliverance and to the Lord's Supper in the Gospels."),
        SUM("Pharaoh refused to free Israel, and ten plagues followed, ending with the death of the firstborn.",
            "At the first Passover, families marked their doors with the blood of a lamb and ate in haste.",
            "Israel left Egypt and God brought them through the sea while Pharaoh's army was overcome.",
            "The Exodus is the central saving act of Israel; Christians link it with Christ and the Lord's Supper."),
    ]))

# ------------------------------------------------------------------ 9 Sinai
LESSONS.append(lesson(
    module=OT1, topic="The Sinai covenant",
    title="Sinai: the covenant, the Ten Commandments and the golden calf",
    slug="rel1-sinai-covenant", minutes=22,
    summary="God's covenant with Israel at Mount Sinai, the Ten Commandments, the sealing of the covenant, the golden calf and what the law teaches about love of God and neighbour.",
    objectives=[
        "Describe the events at Mount Sinai (Exodus 19 to 24)",
        "State the Ten Commandments in your own words",
        "Explain the story of the golden calf",
        "Apply the commandments to honesty, family life and justice today",
    ],
    key_concepts=["Sinai covenant", "Ten Commandments", "Law", "Golden calf", "Sabbath", "Tablets"],
    blocks=[
        H("Introduction"),
        T("A school has rules, and a good school explains why: to protect everyone and help each student learn. Three months after leaving Egypt, the Israelites came to Mount Sinai. The Bible says God gave them a covenant and a law, to shape them as a people."),
        H("Arrival at Sinai"),
        T("In Exodus 19, God reminded the people that he had carried them out of Egypt like an eagle carries its young, and he called them to be his special possession, a kingdom of priests and a holy nation if they would obey him. "
          "The people answered that they would do all that the Lord had said. The mountain was covered in cloud, with thunder, lightning, trumpet sound and smoke."),
        D("The **Sinai covenant** is the agreement in which God, who had rescued Israel, promised to be their God and they promised to keep his law. It was grounded in what God had already done: the rescue from Egypt.", title="Sinai covenant"),
        H("The Ten Commandments"),
        T("In Exodus 20 God spoke the Ten Commandments. The text begins by recalling that God brought them out of slavery. Numbering differs among traditions, so check your textbook. The ten are, in short:"),
        CODE("""1  You shall have no other gods before me
2  You shall not make or worship idols
3  You shall not misuse the name of the Lord
4  Keep the sabbath day holy
5  Honour your father and your mother
6  You shall not murder
7  You shall not commit adultery
8  You shall not steal
9  You shall not give false evidence against your neighbour
10 You shall not covet what belongs to your neighbour""", "text", title="The Ten Commandments (summary)"),
        T("The first four concern the relationship with God. The last six concern relationships with other people. Later, Jesus summed up the law as love of God and love of neighbour."),
        T("The chapters after Exodus 20 give more laws, often called the Book of the Covenant. They deal with slaves, injuries, property and the weak: the foreigner, the widow and the orphan are to be protected. "
          "In Exodus 24 Moses read the book to the people, who said again that they would obey. Moses sprinkled blood on the altar and the people, sealing the covenant. He then went up the mountain for forty days."),
        H("The golden calf"),
        T("While Moses was away, the people grew impatient. They asked Aaron to make gods for them. Aaron collected their gold earrings and made a golden calf, and the people held a festival before it. "
          "God told Moses what was happening. Moses came down, saw the calf and threw down the tablets, which broke. He ground the calf to powder. "
          "Moses pleaded with God for the people, and God did not abandon them. In Exodus 34 the covenant was renewed and Moses received new tablets."),
        IMG("f5rel-1-sinai-sequence.svg",
            alt="Sequence from arrival at Sinai, the Ten Commandments, the covenant sealed, the golden calf and the renewal of the covenant",
            caption="Figure 1. The main events at Sinai."),
        KEY("What the Sinai covenant teaches", "Use in essays.", cards=[
            ["God first", "The law begins with God's grace: he rescued Israel before he gave the law."],
            ["Worship of one God", "The first commandments forbid other gods and idols."],
            ["Justice in daily life", "The commandments protect life, marriage, property, truth and family."],
            ["Mercy", "After the calf, God forgave and renewed the covenant."],
        ]),
        EX("Worked example 1: the commandments", intro="Divide the Ten Commandments into duties to God and duties to people.", steps=[
            S("Duties to God", text="No other gods; no idols; respect God's name; keep the sabbath."),
            S("Duties to people", text="Honour parents; do not murder, commit adultery, steal, lie in court or covet."),
        ]),
        EX("Worked example 2: model answer plan", intro="Explain what happened when Moses was on the mountain and what this teaches.", steps=[
            S("The event", text="The people asked Aaron for gods and made a golden calf."),
            S("Moses' response", text="He broke the tablets, destroyed the calf and prayed for the people."),
            S("The result", text="The covenant was renewed with new tablets."),
            S("Lesson", text="People are tempted to put other things in God's place, and God is merciful."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying God gave the law before the Exodus", "The Ten Commandments were given at Sinai after the Exodus."),
        MISTAKE("Blaming only Moses or only Aaron", "Moses was away. Aaron made the calf at the people's request. The people worshipped it."),
        MISTAKE("Saying the commandments were given to the Egyptians", "They were given to Israel as part of their covenant with God."),
        QUIZ("Which commandment concerns the seventh day?",
             ["The first", "The second", "The fourth", "The sixth"], 2,
             "The fourth commandment (in the usual Protestant numbering) is to keep the sabbath day holy.",
             hint="It is the last of the commands about God.",
             feedback=["The first forbids other gods.", "The second forbids idols.", "", "The sixth forbids murder."]),
        QUIZ("Why did Aaron make the golden calf?",
             ["God told him to", "The people were impatient while Moses was away and asked for gods", "Pharaoh commanded it", "To celebrate Passover"], 1,
             "The people grew impatient when Moses was gone for a long time.",
             hint="Think about Moses' absence.",
             feedback=["God was angry about it.", "", "Pharaoh was no longer involved.", "It was a different event."]),
        PQ("Name the mountain where the Ten Commandments were given and the leader who received them.", "Mount Sinai; Moses."),
        PQ("State two of the commandments about relationships between people.", "Honour father and mother; do not murder, commit adultery, steal, bear false witness or covet (any two)."),
        PQ("Which commandment would a market trader break by using a false scale, and how?", "'You shall not steal' (and the one against false witness): cheating customers takes what is not theirs."),
        TIP("In Paper 1, expect questions on the commandments and on the golden calf. For essays, include both the commandments and the idea of the covenant: God's promise and Israel's response."),
        SUM("At Sinai God made a covenant with Israel, who promised to obey his law.",
            "The Ten Commandments cover duty to God and to other people.",
            "While Moses was on the mountain the people made a golden calf, and Moses broke the tablets.",
            "God forgave, renewed the covenant, and the law calls people to love, justice and loyalty to God."),
    ]))

# ------------------------------------------------------------------ 10 Samuel and Saul
LESSONS.append(lesson(
    module=OT2, topic="Samuel and Saul",
    title="Samuel and Saul: the first king of Israel",
    slug="rel1-samuel-and-saul", minutes=20,
    summary="Hannah's prayer and the call of Samuel, Israel's request for a king, the anointing of Saul, Saul's disobedience and his rejection and death.",
    objectives=[
        "Tell how Samuel was born, dedicated and called",
        "Explain why Israel asked for a king and what Samuel warned",
        "Describe Saul's rise and the two acts of disobedience that cost him the kingdom",
        "Draw lessons about prayer, obedience and leadership",
    ],
    key_concepts=["Hannah", "Eli", "Samuel", "Prophet and judge", "Monarchy", "Saul", "Obedience"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian communities, a chief or fon is chosen according to custom and has duties to the people, not only privileges. "
          "Israel was first led by judges, men and women raised up in times of need. The books of Samuel tell how the nation moved from judges to kings, and how hard it was to choose a good king."),
        H("Hannah and the call of Samuel"),
        T("Hannah, wife of Elkanah, had no child and prayed in great distress at the sanctuary at Shiloh. The priest Eli at first thought she was drunk, but when he heard her prayer he blessed her. "
          "She promised that if she had a son, she would give him to the Lord. Her son Samuel was born, and when he was weaned she brought him to serve in the sanctuary under Eli (1 Samuel 1 and 2)."),
        T("One night, as the boy lay down, he heard a voice call his name. He thought Eli had called him. After the third time, Eli understood that it was the Lord and told him to answer, 'Speak, Lord, for your servant is listening.' "
          "God told him that Eli's family would be judged because Eli's sons had done wrong and Eli had not stopped them (1 Samuel 3). Samuel grew up and all Israel knew he was a prophet of the Lord."),
        H("Israel asks for a king"),
        T("When Samuel was old, his sons did not follow his ways, and took bribes. The elders came to Samuel and asked for a king 'such as all the other nations have' (1 Samuel 8). "
          "Samuel was displeased and prayed. God said the people had rejected him as their king. Samuel warned them that a king would take their sons for his army, their daughters for his service, their fields and a tenth of their produce. The people insisted."),
        D("The **monarchy** is rule by a king. In Israel the king was meant to rule under God's law as a servant of the Lord, not as an absolute master.", title="Monarchy"),
        H("Saul"),
        T("Saul, son of Kish of the tribe of Benjamin, was a tall and handsome young man who was looking for lost donkeys when he met Samuel. "
          "Samuel anointed him with oil as ruler over Israel in private (1 Samuel 9 and 10), and later he was publicly acknowledged at Mizpah. Saul was humble at first. He won a victory over the Ammonites and the people confirmed him as king."),
        T("Two acts of disobedience are remembered. At Gilgal, Saul grew impatient waiting for Samuel and offered the sacrifice himself, which was not his place (1 Samuel 13). "
          "Later, ordered to destroy the Amalekites completely, Saul kept the best of the animals and spared the king. Samuel told him that to obey is better than sacrifice and that God had rejected him as king (1 Samuel 15). Check your textbook for details of each."),
        T("Saul was troubled and jealous of David. At the end, in battle with the Philistines at Mount Gilboa, Saul and his son Jonathan died (1 Samuel 31)."),
        IMG("f5rel-1-kingdom-timeline.svg",
            alt="Timeline of the united kingdom: Samuel and Saul, David, Solomon, then the division of the kingdom, with approximate dates",
            caption="Figure 1. The united monarchy and its division (dates are approximate; check your textbook)."),
        KEY("Lessons from Samuel and Saul", "For application questions.", cards=[
            ["Prayer", "Hannah brought her trouble to God and kept her promise."],
            ["Listening", "Samuel learned to listen to God when called; a good leader listens."],
            ["Obedience", "Saul lost the kingdom through impatience and partial obedience."],
            ["Responsible leadership", "Eli's failure to correct his sons and Samuel's warning show that leaders answer for how they use power."],
        ]),
        EX("Worked example 1: facts", intro="Why did the elders of Israel ask for a king?", steps=[
            S("Reason 1", text="Samuel was old and his sons were corrupt."),
            S("Reason 2", text="They wanted to be like other nations, with a king to lead them in war."),
            S("Samuel's warning", text="A king would take their sons, daughters, land and a tenth of their produce."),
        ]),
        EX("Worked example 2: model answer plan", intro="Why did God reject Saul as king?", steps=[
            S("Gilgal", text="Saul offered the sacrifice himself instead of waiting for Samuel."),
            S("Amalek", text="He did not carry out God's command fully, sparing the best animals."),
            S("Samuel's verdict", text="To obey is better than sacrifice."),
            S("Lesson", text="Leaders must obey God and not use religion to excuse disobedience."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying David was the first king", "Saul was the first king of Israel. David was the second."),
        MISTAKE("Confusing Eli and Samuel", "Eli was the priest at Shiloh who raised Samuel. Samuel was the prophet and judge who anointed Saul and David."),
        MISTAKE("Saying Samuel was Hannah's husband", "Hannah was Samuel's mother. Her husband was Elkanah."),
        QUIZ("Who anointed Saul as king?",
             ["Eli", "Samuel", "Nathan", "Elijah"], 1,
             "Samuel anointed Saul, and later David.",
             hint="He was the prophet and judge of the time.",
             feedback=["Eli had died before this.", "", "Nathan was David's prophet.", "Elijah lived much later."]),
        QUIZ("What happened when Samuel was a boy at Shiloh?",
             ["He killed a giant", "He heard the Lord calling his name at night", "He built a temple", "He was made king"], 1,
             "He heard a voice call him three times, and Eli told him to answer, 'Speak, Lord, for your servant is listening.'",
             hint="It happened at night.",
             feedback=["That is David.", "", "Solomon did that.", "Samuel was never king."]),
        PQ("Why did Hannah take her son to Shiloh?", "She had promised God that if he gave her a son she would give him to the Lord's service."),
        PQ("State one warning Samuel gave about having a king.", "A king would take sons and daughters into his service, take fields and a tenth of the crops, and the people would become his servants."),
        PQ("A young church leader in your town is tempted to use church money for personal use because 'God knows I am doing good work.' What does Saul's story warn?", "Partial or self-serving obedience is still disobedience; honest, accountable leadership is better than good-sounding excuses."),
        TIP("Know the order of Israel's early leaders: judges, Samuel, Saul, David, Solomon. Paper 1 often asks 'who was the first king?'"),
        SUM("Samuel was born in answer to Hannah's prayer, dedicated at Shiloh and called as a boy.",
            "Israel asked for a king, and Samuel warned them what a king would cost.",
            "Saul was anointed first king but disobeyed at Gilgal and over the Amalekites.",
            "He died at Gilboa. The story teaches obedience and responsible leadership."),
    ]))

# ------------------------------------------------------------------ 11 David
LESSONS.append(lesson(
    module=OT2, topic="David",
    title="David: shepherd, king, sinner and the promise to his house",
    slug="rel1-david", minutes=24,
    summary="David's anointing, the victory over Goliath, his years as Saul's rival, his reign in Jerusalem, God's promise to his house, his sin with Bathsheba and his repentance.",
    objectives=[
        "Tell the story of David's anointing and victory over Goliath",
        "Explain how David became king and made Jerusalem his capital",
        "Describe God's promise to David in 2 Samuel 7",
        "Explain David's sin against Uriah and what his repentance teaches",
    ],
    key_concepts=["David", "Goliath", "Jonathan", "Jerusalem", "Davidic covenant", "Bathsheba", "Repentance"],
    blocks=[
        H("Introduction"),
        T("In a family of many brothers, the youngest is sometimes overlooked. David, the youngest of Jesse's sons, was minding sheep when God chose him. His story is a mixture of faith, courage and failure, and it shows how a great person can fall and how repentance makes a way back."),
        H("The shepherd boy chosen"),
        T("After God rejected Saul, Samuel went to Bethlehem to the house of Jesse. Jesse brought seven sons, and God did not choose any of them. Samuel asked if there was another. David was brought in from the fields and Samuel anointed him. "
          "God had told Samuel that people look at outward appearance but the Lord looks at the heart (1 Samuel 16). David was brought to Saul's court to play the lyre when Saul was troubled."),
        H("David and Goliath"),
        T("The Philistines gathered against Israel, and their champion, Goliath of Gath, a giant, challenged Israel to send a man to fight him. For forty days no one dared. "
          "David, who had brought food for his brothers, heard the challenge. He said the Philistine had insulted the armies of the living God. Saul tried to give him armour, but David refused it. "
          "He took his staff, five smooth stones and his sling. He told Goliath that he came in the name of the Lord. One stone struck Goliath, who fell, and David cut off his head (1 Samuel 17)."),
        H("Years as Saul's rival"),
        T("David became famous. Saul grew jealous and tried to kill him. Saul's son Jonathan loved David as himself and made a covenant of friendship with him, protecting him. "
          "David fled and lived in the wilderness with a band of men. Twice he had the chance to kill Saul, once in a cave, and he refused to harm 'the Lord's anointed' (1 Samuel 24 and 26). "
          "After Saul and Jonathan died, David mourned them."),
        H("King in Jerusalem"),
        T("David was first anointed king over Judah at Hebron. After some years, the northern tribes also accepted him. David reigned forty years: seven at Hebron and thirty-three at Jerusalem (2 Samuel 5). "
          "He captured Jerusalem from the Jebusites and made it his capital, a city belonging to no single tribe. He brought the ark of the covenant to Jerusalem with rejoicing. It became both the political and religious centre of Israel."),
        D("In 2 Samuel 7, David wanted to build a house (temple) for God. Through the prophet Nathan, God said David's son would build it, and that God would establish David's house and throne for ever. This is often called the **Davidic covenant**. "
          "Christians believe it points to Jesus, who is called Son of David in the Gospels.", title="The promise to David"),
        H("Bathsheba and Uriah"),
        T("One spring, when the army was at war, David stayed in Jerusalem. From his roof he saw Bathsheba, the wife of Uriah the Hittite, one of his soldiers. David took her, and she conceived. "
          "David tried to hide his sin by calling Uriah home, and when that failed, he arranged for Uriah to be placed where the fighting was fiercest, and Uriah was killed. David then married Bathsheba (2 Samuel 11)."),
        T("The Lord sent Nathan, who told David a story of a rich man who took a poor man's only lamb. David was angry and said the man deserved to die. Nathan said, 'You are the man.' "
          "David confessed, 'I have sinned against the Lord.' Nathan said God had forgiven him, though the child would die and troubles would follow in his family. Psalm 51 is linked by its heading to this event: a prayer for a clean heart (2 Samuel 12)."),
        KEY("Lessons from David", "For application questions.", cards=[
            ["Courage and trust", "David faced Goliath trusting God, not weapons."],
            ["Respect and loyalty", "He refused to harm Saul and kept faith with Jonathan."],
            ["Abuse of power", "A king is not above the law; Nathan confronted him."],
            ["Repentance", "David admitted his wrong. Forgiveness did not remove every consequence."],
        ]),
        EX("Worked example 1: facts", intro="State four facts about David's kingship.", steps=[
            S("Fact 1", text="Anointed first at Hebron over Judah, then king over all Israel."),
            S("Fact 2", text="Reigned forty years."),
            S("Fact 3", text="Captured Jerusalem and made it his capital."),
            S("Fact 4", text="Brought the ark there; God promised to establish his house."),
        ]),
        EX("Worked example 2: model answer plan", intro="What does David's sin and repentance teach?", steps=[
            S("The sin", text="Adultery, deceit and arranging Uriah's death."),
            S("The prophet", text="Nathan's story made David judge himself."),
            S("The response", text="He confessed and prayed for mercy."),
            S("Lessons", text="Leaders must be accountable; honest confession is the way back; sin has consequences."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving Solomon the credit for Goliath or for Jerusalem", "David defeated Goliath and made Jerusalem the capital. Solomon built the temple."),
        MISTAKE("Saying Nathan took part in the killing of Uriah", "Nathan was the prophet who confronted David. Uriah was killed in battle on David's orders."),
        MISTAKE("Dating Goliath to David's old age", "David was a young man or boy when he fought Goliath."),
        QUIZ("Who was David's close friend and Saul's son?",
             ["Absalom", "Jonathan", "Uriah", "Joab"], 1,
             "Jonathan, Saul's son, made a covenant of friendship with David.",
             hint="Think of the son of the king who wanted to kill David.",
             feedback=["Absalom was David's son.", "", "Uriah was Bathsheba's husband.", "Joab was David's army commander."]),
        QUIZ("Which prophet confronted David about Bathsheba?",
             ["Samuel", "Nathan", "Elijah", "Amos"], 1,
             "Nathan told the story of the poor man's lamb and said 'You are the man.'",
             hint="He is the prophet who also brought God's promise about David's house.",
             feedback=["Samuel had died.", "", "Elijah lived much later.", "Amos lived much later."]),
        PQ("What weapons did David use against Goliath?", "A sling and five smooth stones (he refused Saul's armour)."),
        PQ("State two things David did when he became king in Jerusalem.", "Captured Jerusalem and made it his capital; brought the ark of the covenant there."),
        PQ("A public official in Cameroon is tempted to hide a wrong. What does David's story teach?", "Hiding wrong makes things worse; honest confession, accepting responsibility and making amends are better; no one is above accountability."),
        TIP("David is a favourite for Paper 2: expect both 'describe how David became king' and 'what lessons can we learn from his sin?' Always mention Nathan and Psalm 51 (check your Bible for the heading)."),
        SUM("David, youngest son of Jesse, was anointed by Samuel and defeated Goliath.",
            "He was Saul's rival, spared Saul's life, and became king over all Israel, reigning forty years.",
            "He made Jerusalem his capital and received God's promise about his house.",
            "He sinned with Bathsheba and against Uriah, was confronted by Nathan and repented."),
    ]))

# ------------------------------------------------------------------ 12 Solomon
LESSONS.append(lesson(
    module=OT2, topic="Solomon",
    title="Solomon: wisdom, the temple and the decline",
    slug="rel1-solomon", minutes=20,
    summary="Solomon's request for wisdom at Gibeon, his judgement between two women, the building of the temple, his wealth and the foreign wives who drew his heart away.",
    objectives=[
        "Describe Solomon's request for wisdom (1 Kings 3)",
        "Outline the building and dedication of the temple",
        "Explain the burdens of Solomon's reign",
        "Explain what Solomon's life teaches about wisdom and faithfulness",
    ],
    key_concepts=["Solomon", "Wisdom", "Temple", "Queen of Sheba", "Forced labour", "Idolatry"],
    blocks=[
        H("Introduction"),
        T("A new head teacher or mayor takes office and many people watch to see what he will do first. Solomon, the son of David and Bathsheba, came to the throne as a young man. The Bible says his reign began well, with a prayer for wisdom."),
        H("The request for wisdom"),
        T("Solomon went to Gibeon to offer sacrifices. That night God appeared in a dream and said, 'Ask for whatever you want.' Solomon replied that he was a young man and did not know how to lead such a great people. "
          "He asked for a discerning heart to govern the people and to know right from wrong. God was pleased that he did not ask for long life, riches or the death of his enemies. "
          "God gave him wisdom and promised riches and honour as well, and long life if he walked in God's ways (1 Kings 3)."),
        T("A well-known example of his wisdom: two women came with one living baby, each claiming it was hers. Solomon called for a sword to divide the child in two. "
          "One woman said, 'Give her the baby, do not kill him.' Solomon saw that she was the true mother and gave her the child. All Israel heard and stood in awe of the king's wisdom."),
        H("The temple"),
        T("David had wanted to build a house for God, but his son was to do it. In the fourth year of his reign Solomon began to build the temple in Jerusalem, and it took seven years (1 Kings 6). "
          "He made an agreement with King Hiram of Tyre for cedar timber, and he used skilled workers. The temple was built of stone and cedar, overlaid with gold, and the ark of the covenant was placed in the inner room."),
        T("At the dedication, Solomon stood before the altar and prayed (1 Kings 8). He said that heaven and the highest heaven could not contain God, how much less this house. He asked God to hear the prayers of his people in the temple, and of foreigners who came to pray. "
          "The glory of the Lord filled the temple."),
        D("The **temple** in Jerusalem was the centre of Israel's worship. It was the place where sacrifices were offered and where people believed God's name dwelt.", title="Temple"),
        H("Wealth, fame and the cost"),
        T("Solomon's fame spread. The queen of Sheba came with gifts to test him with hard questions. She was amazed at his wisdom and wealth (1 Kings 10). "
          "He built cities, a palace and fortifications, had many horses and chariots, and traded widely."),
        T("This glory came at a price. He used forced labour for building, and heavy taxes. He married many foreign women, partly for treaties. "
          "In his old age, the Bible says, his wives turned his heart to other gods, and he built places of worship for them. The Lord told him that because of this the kingdom would be torn from his son (1 Kings 11). Solomon reigned forty years."),
        IMG("f5rel-1-solomon-reign.svg",
            alt="Flow showing the start of Solomon's reign with wisdom, the temple, wealth and fame, then burdens and foreign gods, then the loss of the kingdom",
            caption="Figure 1. Solomon's reign: from wisdom to decline."),
        KEY("Lessons from Solomon", "For application questions.", cards=[
            ["Humility and wisdom", "Solomon asked for a heart to serve rather than wealth for himself."],
            ["Worship", "The temple teaches that God is to be honoured and prayer is welcome from all."],
            ["Justice", "Great buildings and wealth do not excuse heavy burdens on the people."],
            ["Faithfulness to the end", "A good beginning is not enough; Solomon's heart turned away."],
        ]),
        EX("Worked example 1: facts", intro="Give four facts about Solomon's temple.", steps=[
            S("Fact 1", text="It was in Jerusalem and took seven years to build."),
            S("Fact 2", text="King Hiram of Tyre supplied cedar timber."),
            S("Fact 3", text="The ark of the covenant was placed inside."),
            S("Fact 4", text="Solomon prayed at the dedication and God's glory filled it."),
        ]),
        EX("Worked example 2: model answer plan", intro="Why did the kingdom decline in Solomon's later years?", steps=[
            S("Heavy burdens", text="Forced labour and taxes."),
            S("Foreign gods", text="Wives drew him to their gods."),
            S("Divine judgement", text="The Lord said the kingdom would be torn from his son."),
            S("Lesson", text="Success can lead to pride and to neglect of duty and God."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving David credit for the temple", "David planned and prepared, but Solomon built the temple."),
        MISTAKE("Saying Solomon asked for riches", "He asked for wisdom. Riches were added as a gift."),
        MISTAKE("Confusing Sheba and Tyre", "The queen of Sheba visited Solomon. Hiram was king of Tyre and supplied timber."),
        QUIZ("What did Solomon ask God for at Gibeon?",
             ["Long life", "Wealth", "An understanding heart to govern wisely", "Victory over enemies"], 2,
             "He asked for a discerning heart to govern God's people and tell right from wrong.",
             hint="The request was linked to his duty as king.",
             feedback=["God noted that he did not ask for this.", "God noted that he did not ask for this.", "", "God noted that he did not ask for this."]),
        QUIZ("What turned Solomon's heart away from God in old age?",
             ["Wars with Egypt", "His foreign wives and their gods", "The building of the temple", "The visit of the queen of Sheba"], 1,
             "His many foreign wives led him to worship other gods.",
             hint="It is connected with his marriages.",
             feedback=["The text points to another cause.", "", "The temple was a good work.", "She visited and praised him."]),
        PQ("Name the king of Tyre who helped Solomon.", "Hiram."),
        PQ("Describe Solomon's judgement between the two women.", "He ordered the child to be divided; the real mother pleaded to give it to the other; Solomon gave the baby to her."),
        PQ("A church in your town plans an expensive new building while some members cannot pay school fees. How does Solomon's story help in the discussion?", "Great projects must not be built on heavy burdens for the people; leaders should combine worship with justice and care for the poor."),
        TIP("Paper 1 asks for the temple (Hiram, seven years) and for the request for wisdom. In essays, include the decline: examiners expect the whole reign, not only the good beginning."),
        SUM("Solomon asked God for wisdom and became famous for his judgements.",
            "He built the temple in Jerusalem and prayed at its dedication.",
            "His reign brought wealth but also forced labour and heavy taxes.",
            "His foreign wives led him to worship other gods, and the kingdom was later divided."),
    ]))

# ------------------------------------------------------------------ 13 Divided kingdom
LESSONS.append(lesson(
    module=OT2, topic="The divided kingdom",
    title="The division of the kingdom: Rehoboam, Jeroboam and the two nations",
    slug="rel1-divided-kingdom", minutes=20,
    summary="Why the united kingdom split after Solomon, how Israel in the north and Judah in the south developed, and how each kingdom came to an end.",
    objectives=[
        "Explain the causes of the division of the kingdom (1 Kings 12)",
        "Name the two kingdoms, their capitals and their first kings",
        "Describe Jeroboam's religious policy and the Bible's judgement on it",
        "State how and when each kingdom ended (approximate dates)",
    ],
    key_concepts=["Rehoboam", "Jeroboam", "Israel (north)", "Judah (south)", "Golden calves", "Assyria", "Babylon"],
    blocks=[
        H("Introduction"),
        T("Imagine a country in which one region feels it pays high taxes and provides labour, but receives little. If a new leader refuses to listen, people may break away. "
          "Something like this happened in Israel after Solomon died, about 930 BC (dates are approximate; check your textbook)."),
        H("The split"),
        T("Solomon's son Rehoboam went to Shechem to be made king. The northern tribes sent Jeroboam, a former official of Solomon who had been in Egypt, to ask Rehoboam to lighten the heavy burdens placed on them. "
          "The old men who had advised Solomon told Rehoboam to listen and serve the people. The young men he grew up with told him to be harsher still. Rehoboam followed the young men and answered roughly. "
          "The northern tribes said they had no share in David's family and went home. Jeroboam was made king over the north (1 Kings 12)."),
        KEY("The two kingdoms", "The Bible calls the northern kingdom Israel and the southern kingdom Judah.", cards=[
            ["Israel (north)", "Ten tribes. First king: Jeroboam. Early capital Shechem; later Samaria, built under Omri."],
            ["Judah (south)", "Judah and Benjamin. First king: Rehoboam. Capital Jerusalem, with the temple. Kings were all from David's family."],
        ]),
        IMG("f5rel-1-divided-kingdom-map.svg",
            alt="Schematic map of the northern kingdom of Israel with Samaria, the southern kingdom of Judah with Jerusalem, and Assyria to the north-east and Babylon to the east",
            caption="Figure 1. Israel and Judah after the division (schematic, not to scale)."),
        H("Jeroboam's worship"),
        T("Jeroboam feared that if his people kept going to Jerusalem to worship, they would return to Rehoboam. So he set up two golden calves, one at Bethel and one at Dan, and said, 'Here are your gods who brought you up out of Egypt.' "
          "He appointed his own priests and a festival. The Bible repeatedly condemns this as 'the sin of Jeroboam', which later kings of Israel followed."),
        T("There was fighting between the two kingdoms for years, and sometimes alliances. Judah had kings who were faithful and kings who were not."),
        H("The end of the two kingdoms"),
        T("Israel had many changes of dynasty and a series of weak or violent kings. Prophets such as Elijah, Elisha, Amos and Hosea spoke against their sins. "
          "Assyria, a powerful empire, grew to the north-east. Samaria fell to the Assyrians in about 722 BC, and many people were taken away. The northern kingdom never came back."),
        T("Judah lasted longer, partly because of faithful kings such as Hezekiah and Josiah. But Babylon replaced Assyria as the great power. "
          "Jerusalem and the temple were destroyed by the Babylonians in 586 BC and many people were taken to Babylon. This period is called the exile."),
        KEY("Lessons from the division", "Use these in essays.", cards=[
            ["Listening to wise advice", "Rehoboam ignored the experienced elders, and lost most of his kingdom."],
            ["Justice for the people", "Heavy burdens without fairness provoke revolt."],
            ["True worship", "Setting up rival shrines and golden calves led people from the true worship of God."],
            ["Prophets speak", "The prophets warned both kingdoms that disloyalty to God and injustice would have consequences."],
        ]),
        EX("Worked example 1: facts", intro="Compare Israel and Judah in one sentence each: first king, capital and end.", steps=[
            S("Israel", text="First king Jeroboam; capital later Samaria; fell to Assyria in about 722 BC."),
            S("Judah", text="First king Rehoboam; capital Jerusalem; fell to Babylon in 586 BC."),
        ]),
        EX("Worked example 2: model answer plan", intro="Explain two causes of the division of the kingdom.", steps=[
            S("Cause 1", text="Solomon's heavy taxes and forced labour built resentment in the north."),
            S("Cause 2", text="Rehoboam refused the request to ease the burden and took the advice of the young men."),
            S("Background", text="Old rivalry between the north and Judah, and Solomon's sins, also played a part."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up Israel and Judah", "Israel is the northern kingdom (ten tribes); Judah the southern (capital Jerusalem)."),
        MISTAKE("Saying the exile began with Assyria", "Assyria ended the northern kingdom. Babylon destroyed Jerusalem in 586 BC and exiled Judah."),
        MISTAKE("Saying Jeroboam built the temple", "Solomon built the temple in Jerusalem. Jeroboam set up golden calves at Bethel and Dan."),
        QUIZ("Which kingdom had Jerusalem as its capital?",
             ["Israel", "Judah", "Assyria", "Samaria"], 1,
             "Judah, the southern kingdom, kept Jerusalem.",
             hint="It was ruled by David's family.",
             feedback=["The northern kingdom first used Shechem and later Samaria.", "", "Assyria was an empire.", "Samaria was the later capital of Israel."]),
        QUIZ("What did Jeroboam set up at Bethel and Dan?",
             ["Two temples to Baal", "Two golden calves", "Two altars to Asherah", "Two palaces"], 1,
             "He set up golden calves so that the northern tribes did not need to go to Jerusalem.",
             hint="The same type of object was made at Sinai.",
             feedback=["The golden calves are the recorded objects.", "", "These are other forms of worship.", "He built shrines, not palaces."]),
        PQ("Give two reasons why the northern tribes rejected Rehoboam.", "He refused to lighten the heavy burdens, and he spoke harshly to them following the advice of the young men; the north also felt it had no share in David's family."),
        PQ("Which empire destroyed Samaria and about when?", "Assyria, about 722 BC."),
        PQ("A school committee ignores the suggestions of the elderly teachers and students and imposes new fees suddenly. What does the story of Rehoboam warn?", "Leaders who ignore wise advice and the needs of the people provoke anger and division; they should listen and consult."),
        TIP("Dates are approximate in textbooks. Use 'about 930 BC' for the division, 'about 722 BC' for Samaria and '586 BC' for Jerusalem unless your teacher gives different figures."),
        SUM("After Solomon died, Rehoboam refused to lighten the burdens and the ten northern tribes made Jeroboam king.",
            "Israel (north) and Judah (south, with Jerusalem) became separate kingdoms.",
            "Jeroboam set up golden calves at Bethel and Dan.",
            "Assyria ended Israel about 722 BC and Babylon ended Judah in 586 BC."),
    ]))

# ------------------------------------------------------------------ 14 Elijah and Ahab
LESSONS.append(lesson(
    module=OT2, topic="Elijah and Ahab",
    title="Elijah and Ahab: Baal, Carmel and Naboth's vineyard",
    slug="rel1-elijah-and-ahab", minutes=22,
    summary="The prophet Elijah and King Ahab: the drought, the contest on Mount Carmel, Naboth's vineyard and what the stories say about true worship and justice.",
    objectives=[
        "Describe the religious situation under Ahab and Jezebel",
        "Tell the story of the contest on Mount Carmel",
        "Explain the injustice done to Naboth and Elijah's judgement",
        "Explain what Elijah's ministry teaches about courage, worship and justice",
    ],
    key_concepts=["Elijah", "Ahab", "Jezebel", "Baal", "Mount Carmel", "Naboth", "Justice"],
    blocks=[
        H("Introduction"),
        T("Imagine a powerful person who takes land from a poor family because he wants it, and a village elder who dares to say, 'This is wrong.' "
          "Elijah the Tishbite was such a person. He lived in the northern kingdom in the ninth century BC, when Ahab was king."),
        H("Ahab, Jezebel and Baal"),
        T("Ahab, son of Omri, married Jezebel, daughter of the king of Sidon (1 Kings 16). She brought the worship of Baal, a Canaanite god thought to control rain and crops. "
          "Ahab built a temple and altar for Baal in Samaria. Jezebel supported hundreds of prophets of Baal and attacked the prophets of the Lord. The Bible says Ahab did more evil than any king before him."),
        H("Drought and Carmel"),
        T("Elijah told Ahab that there would be no rain except at his word. During the drought, he was fed by ravens at the brook Cherith, and then lived with a widow at Zarephath whose flour and oil did not run out. He also restored her son to life (1 Kings 17)."),
        T("In the third year Elijah met Ahab and asked him to gather the people and the prophets of Baal on Mount Carmel (1 Kings 18). He asked the people how long they would waver between two opinions: if the Lord is God, follow him, and if Baal, follow him. "
          "Four hundred and fifty prophets of Baal prepared a bull and called on Baal from morning until evening, but there was no answer. Elijah mocked them. "
          "Elijah then repaired the altar of the Lord, arranged twelve stones, dug a trench, drenched the sacrifice with water, and prayed a short prayer. Fire fell from heaven and consumed the offering, the wood, stones and water. "
          "The people fell on their faces and said, 'The Lord, he is God.' Afterwards, Elijah prayed and rain came."),
        D("**Baal** was a god of the Canaanites, linked with rain and fertility. The story of Carmel presents a contest to show who really controls rain and life. The Bible teaches that the Lord alone is God.", title="Baal"),
        H("Despair and a quiet voice"),
        T("Jezebel threatened to kill Elijah, and he ran away to the wilderness, and then to Mount Horeb. He felt alone and wished to die. "
          "God did not come in the wind, earthquake or fire, but in a gentle whisper (a still small voice). God sent him back with tasks, including the call of Elisha as his successor (1 Kings 19). "
          "He also told him that seven thousand in Israel had not bowed to Baal."),
        H("Naboth's vineyard"),
        T("Naboth owned a vineyard next to Ahab's palace at Jezreel. Ahab wanted it for a vegetable garden and offered to buy it or exchange it. Naboth refused because it was his family inheritance. "
          "Ahab sulked, and Jezebel arranged false witnesses to accuse Naboth of cursing God and the king. Naboth was stoned, and Ahab took the vineyard (1 Kings 21)."),
        T("The Lord sent Elijah to Ahab in the vineyard. Elijah said, 'Have you murdered a man and also taken his property?' and announced judgement on Ahab and Jezebel. "
          "When Ahab humbled himself, the judgement on his house was delayed. Ahab died later in battle (1 Kings 22)."),
        IMG("f5rel-1-elijah-sequence.svg",
            alt="Sequence: Ahab and Jezebel promote Baal, drought and Cherith, Zarephath, Mount Carmel, Horeb, Naboth's vineyard",
            caption="Figure 1. The story of Elijah in order."),
        KEY("Lessons from Elijah and Ahab", "For application questions.", cards=[
            ["Loyalty to God", "Elijah called people to choose between the Lord and Baal and not to waver."],
            ["Courage", "Elijah stood alone against king and priests, yet needed rest and encouragement himself."],
            ["Justice", "God cares about the rights of the weak; rulers must not seize the property of the poor."],
            ["Humility", "Ahab's partial humbling was met with mercy."],
        ]),
        EX("Worked example 1: the contest at Carmel", intro="Describe what happened on Mount Carmel.", steps=[
            S("The challenge", text="Elijah challenged the people to choose between the Lord and Baal."),
            S("The prophets of Baal", text="They prayed all day but received no answer."),
            S("Elijah's altar", text="He drenched the sacrifice with water and prayed."),
            S("Result", text="Fire fell and consumed everything; the people said the Lord is God; later rain came."),
        ]),
        EX("Worked example 2: model answer plan", intro="What does the story of Naboth teach about justice?", steps=[
            S("The wrong", text="Ahab and Jezebel used false witnesses to take a poor man's land and life."),
            S("The prophet", text="Elijah condemned both murder and theft."),
            S("The principle", text="God is on the side of the weak, and no ruler is above the law."),
            S("Application", text="Land grabbing and corruption today are condemned in the same way."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing Elijah and Elisha", "Elijah confronted Ahab. Elisha was his successor."),
        MISTAKE("Giving the wrong number of prophets", "Four hundred and fifty prophets of Baal were at Carmel."),
        MISTAKE("Saying Jezebel was an Israelite", "She was a princess of Sidon who brought Baal worship to Israel."),
        QUIZ("Where did the contest between Elijah and the prophets of Baal take place?",
             ["Mount Sinai", "Mount Carmel", "Mount Zion", "Mount Ararat"], 1,
             "The contest was on Mount Carmel.",
             hint="It is the mountain of 1 Kings 18.",
             feedback=["Sinai is where Moses received the law.", "", "Zion is Jerusalem.", "Ararat is where Noah's ark rested."]),
        QUIZ("Why did Naboth refuse to sell his vineyard?",
             ["He disliked Ahab", "It was his family inheritance", "He wanted more money", "He was afraid of Jezebel"], 1,
             "Land was a family inheritance from God and was not to be sold lightly.",
             hint="Think of what land meant for an Israelite family.",
             feedback=["The story does not say this.", "", "He refused any price.", "He did not act out of fear."]),
        PQ("Who was Elijah's successor?", "Elisha."),
        PQ("What did God show Elijah at Horeb?", "A gentle whisper, a still small voice, after wind, earthquake and fire."),
        PQ("A local official takes land from a poor widow by pretending the papers are false. Which story gives a Christian a guide for speaking out, and why?", "Naboth's vineyard: Elijah condemned Ahab for taking land by false accusation; Christians are called to speak for the powerless and justice."),
        TIP("Paper 1: Carmel, 450 prophets, Naboth, Jezreel, Cherith, Zarephath. Essays: always give both stories, true worship and justice."),
        SUM("Under Ahab and Jezebel, Baal worship spread in Israel.",
            "Elijah announced a drought and called people to choose between the Lord and Baal on Mount Carmel.",
            "At Horeb God spoke in a gentle whisper and Elijah was sent to anoint his successor.",
            "Naboth's vineyard shows that God opposes injustice by rulers."),
    ]))

# ------------------------------------------------------------------ 15 Prophets
LESSONS.append(lesson(
    module=OT2, topic="The eighth-century prophets",
    title="Amos, Hosea and Isaiah: justice, faithfulness and hope",
    slug="rel1-eighth-century-prophets", minutes=24,
    summary="The message of Amos (justice), Hosea (God's faithful love) and Isaiah (holiness, call and hope) in the eighth century BC.",
    objectives=[
        "Explain what a prophet was and why the prophets spoke",
        "State the main message of Amos, Hosea and Isaiah",
        "Describe Isaiah's call in the temple",
        "Apply the prophets' message on justice and love to modern life",
    ],
    key_concepts=["Prophet", "Amos", "Hosea", "Isaiah", "Justice", "Steadfast love", "Remnant"],
    blocks=[
        H("Introduction"),
        T("When a community is facing something wrong, a person with courage may stand up and say what others are afraid to say. The Bible's prophets did this. In the eighth century BC (700s), Amos, Hosea and Isaiah spoke to Israel and Judah in a time of trade, wealth for some, and poverty for others."),
        D("A **prophet** is a person who speaks for God. Biblical prophets did more than predict the future. They called people back to faithful worship and just living, warned of the results of ignoring God, and gave hope.", title="Prophet"),
        H("Background: prosperity and injustice"),
        T("In the north, King Jeroboam II ruled during a time of peace and wealth. The rich built fine houses and held feasts, while the poor were pushed aside. Worship went on at shrines, but daily life was unjust. "
          "Assyria was a growing threat. Judah, ruled in turn by Uzziah, Jotham, Ahaz and Hezekiah, also faced danger."),
        H("Amos: the voice for justice"),
        T("Amos was a shepherd and a grower of figs from Tekoa in Judah. He said he was no professional prophet, but God had taken him from following the flock and sent him to Israel (Amos 7). "
          "He spoke at Bethel. He warned about the nations around Israel, then Israel itself."),
        T("His charges: the rich sold the poor for a pair of sandals, cheated with false scales, trampled on the needy and took bribes. "
          "He said God hated their festivals and offerings when there was no justice. In a famous line (Amos 5:24) he said, 'Let justice roll on like a river, righteousness like a never-failing stream.' "
          "He also spoke of 'the day of the Lord' as a day of judgement, not simply of light for Israel."),
        H("Hosea: God's faithful love"),
        T("Hosea lived in the northern kingdom. God told him to marry Gomer, who was unfaithful. This became a picture of Israel's unfaithfulness to the Lord, who had loved Israel from its youth. "
          "Hosea's children were given names that carried messages. Hosea's message is that Israel had gone after Baal, forgotten God's goodness and given no real knowledge of God. "
          "But God's love is faithful, and he would not give up. In Hosea 6:6 God says he desires steadfast love (mercy), not sacrifice, and the knowledge of God rather than burnt offerings. Hosea 11 describes God as a parent teaching a child to walk."),
        H("Isaiah: holiness and hope"),
        T("Isaiah lived in Jerusalem and served as a prophet during the reigns of several kings of Judah. In the year King Uzziah died, he saw a vision of the Lord on a throne in the temple, with seraphs calling 'Holy, holy, holy' (Isaiah 6). "
          "He felt unclean and sinful, but a burning coal touched his lips and his guilt was taken away. He heard God ask, 'Whom shall I send?' and answered, 'Here am I. Send me.'"),
        T("Isaiah condemned injustice, empty worship and reliance on alliances rather than God. He told Judah to trust God in danger. He spoke of a faithful remnant, a small group who would be saved. "
          "He also looked forward to a coming ruler, sometimes read by Christians as pointing to Jesus (Isaiah 7, 9 and 11), and to a time when nations would beat swords into ploughshares (Isaiah 2). Different books and teachers explain these passages in different ways, so check your textbook."),
        IMG("f5rel-1-prophets-timeline.svg",
            alt="Timeline of the eighth century BC showing Amos and Hosea in the north, Isaiah in Judah, and the fall of Samaria about 722 BC",
            caption="Figure 1. The eighth-century prophets (dates approximate)."),
        KEY("The three messages", "Learn this table.", cards=[
            ["Amos", "From Judah to Israel. Justice for the poor; worship without justice is empty."],
            ["Hosea", "In Israel. God's faithful love for an unfaithful people; return to him."],
            ["Isaiah", "In Judah. The holy God; trust him, not alliances; hope of a righteous ruler and a remnant."],
        ]),
        EX("Worked example 1: facts", intro="Give three facts about Isaiah's call.", steps=[
            S("When", text="In the year King Uzziah died."),
            S("Where", text="In a vision in the temple, with seraphs saying 'Holy, holy, holy'."),
            S("Response", text="He admitted his sin, a coal touched his lips, and he said 'Here am I; send me.'"),
        ]),
        EX("Worked example 2: model answer plan", intro="What did Amos teach about worship and justice?", steps=[
            S("The setting", text="Wealthy people in Israel offered sacrifices but cheated the poor."),
            S("The charge", text="False scales, bribes, selling people for small debts."),
            S("The message", text="God hates worship that is separated from justice."),
            S("Application", text="Honest business, fair wages and care for the poor are part of true religion."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Amos was a priest or a professional prophet", "He was a shepherd and fig-grower from Tekoa."),
        MISTAKE("Mixing up Hosea's picture", "Hosea's wife Gomer is the picture of unfaithful Israel; God's patient love is the main message."),
        MISTAKE("Saying Isaiah worked in the north", "Isaiah lived and served in Jerusalem in Judah."),
        QUIZ("Which prophet was a shepherd from Tekoa?",
             ["Isaiah", "Hosea", "Amos", "Elijah"], 2,
             "Amos was a shepherd and fig-grower from Tekoa.",
             hint="His message was strongly about justice.",
             feedback=["Isaiah lived in Jerusalem.", "Hosea is known for his marriage to Gomer.", "", "Elijah lived earlier."]),
        QUIZ("What was Hosea's main message about God?",
             ["God demands only sacrifices", "God's love is faithful even when Israel is unfaithful", "God has abandoned his people forever", "God cares only for Judah"], 1,
             "Hosea shows God's steadfast love for an unfaithful people and his call to return.",
             hint="Think of his marriage as a picture.",
             feedback=["He said God desires mercy, not sacrifice.", "", "The book ends with hope of restoration.", "He spoke in the north."]),
        PQ("How did Isaiah answer God's question 'Whom shall I send?'", "'Here am I. Send me.'"),
        PQ("State two injustices that Amos condemned.", "Selling the poor for small debts; cheating with false weights; taking bribes; trampling the needy (any two)."),
        PQ("A Christian youth leader sees dishonesty in a local market. How can the message of Amos guide them?", "Speak up respectfully for honest trade and fair treatment; worship and church attendance must go with justice."),
        TIP("The 'three prophets' question appears often: remember Amos = justice, Hosea = love, Isaiah = holiness. Add the kingdom (Israel or Judah) and one text."),
        SUM("Prophets spoke for God, calling people to faithfulness and justice.",
            "Amos, a shepherd from Judah, condemned injustice and empty worship in Israel.",
            "Hosea showed God's faithful love through his marriage to Gomer.",
            "Isaiah, called in the temple vision, taught trust in the holy God and hope for a righteous ruler."),
    ]))

# ------------------------------------------------------------------ 16 Annunciation and birth
LESSONS.append(lesson(
    module=GOS1, topic="The Annunciation and the birth of John and Jesus",
    title="The Annunciation and the birth of John the Baptist and Jesus",
    slug="rel1-annunciation-and-birth", minutes=24,
    summary="The synoptic Gospels, the announcements to Zechariah and Mary, the birth of John and of Jesus in Bethlehem, and the events of the infancy in Matthew and Luke.",
    objectives=[
        "Explain what the synoptic Gospels are",
        "Describe the announcements of the births of John and Jesus",
        "Tell the story of the birth of Jesus in Luke 2 and the visit of the magi in Matthew 2",
        "Explain what the stories teach about humility, trust and God's care for the poor",
    ],
    key_concepts=["Synoptic Gospels", "Gabriel", "Zechariah and Elizabeth", "Mary", "Magnificat", "Bethlehem", "Magi"],
    blocks=[
        H("Introduction"),
        T("In many Cameroonian homes the birth of a child is celebrated with joy, family gathers and songs. The Gospels begin the story of Jesus with birth stories full of joy, wonder and trust in God."),
        D("The **synoptic Gospels** are Matthew, Mark and Luke. 'Synoptic' means 'seeing together', because they follow a similar outline and share much material. "
          "The Gospel of John is different in style and content. Only Matthew and Luke tell of Jesus' birth.", title="Synoptic Gospels"),
        H("The announcement to Zechariah"),
        T("Luke 1 begins with Zechariah, a priest, and his wife Elizabeth, who were old and had no child. While Zechariah was serving in the temple, the angel Gabriel appeared and said Elizabeth would bear a son. "
          "The child was to be named John, would be great before the Lord, filled with the Holy Spirit and would prepare the people for the Lord. Zechariah doubted because of their age, and was unable to speak until the child was born."),
        H("The announcement to Mary"),
        T("In the sixth month, Gabriel was sent to Nazareth in Galilee to Mary, a young woman engaged to Joseph, a descendant of David. The angel greeted her and told her not to be afraid. "
          "She would conceive and bear a son and call him Jesus. He would be great and be called Son of the Most High, and God would give him the throne of David. "
          "Mary asked how this could be. The angel said the Holy Spirit would come on her. Mary answered, 'I am the Lord's servant. May your word to me be fulfilled' (Luke 1:26-38)."),
        T("Mary went to visit Elizabeth, her relative. Elizabeth greeted her as the mother of her Lord, and Mary sang a song of praise known as the **Magnificat**, in which she rejoices that God lifts up the lowly and fills the hungry with good things. "
          "Elizabeth's son John was born; Zechariah wrote 'His name is John', his speech returned, and he praised God."),
        H("The birth of Jesus"),
        T("In Matthew 1, Joseph discovers Mary is expecting a child and is troubled. An angel tells him in a dream not to be afraid to take Mary as his wife, for the child is from the Holy Spirit, and to name him Jesus, for he will save his people from their sins."),
        T("Luke 2 says that Emperor Augustus ordered a census. Joseph and Mary travelled from Nazareth to Bethlehem, the town of David. There Mary gave birth to her firstborn son, wrapped him in cloths and laid him in a manger, because there was no room for them in the inn. "
          "Angels appeared to shepherds in the fields, telling them of a Saviour, Christ the Lord, and the shepherds went to see the child and told others what they had heard."),
        T("Jesus was circumcised, and in the temple Simeon and the prophetess Anna recognised him as the one God had promised (Luke 2)."),
        H("Matthew's account: the magi"),
        T("In Matthew 2, wise men (magi) from the east followed a star to Jerusalem and asked where the king of the Jews was born. King Herod was troubled and sent them to Bethlehem. "
          "They worshipped the child and gave gifts of gold, frankincense and myrrh. Warned in a dream, they returned home by another way. Joseph was warned to take the child and his mother to Egypt, as Herod ordered the killing of boys in Bethlehem. "
          "After Herod's death the family returned and settled in Nazareth."),
        IMG("f5rel-1-nativity-timeline.svg",
            alt="Timeline from the announcement to Zechariah, the announcement to Mary, the birth of John, the birth in Bethlehem, the magi, the flight to Egypt and Nazareth",
            caption="Figure 1. The birth stories of John and Jesus."),
        KEY("What the stories teach", "For essays and application.", cards=[
            ["Trust and humility", "Mary accepted God's word as his servant."],
            ["God's care for the lowly", "Shepherds, a manger, a poor family: the good news comes to ordinary people."],
            ["Preparation", "John's birth points forward to his task of preparing the way."],
            ["Rejoicing", "The stories are full of praise: the Magnificat, the angels, the shepherds."],
        ], note="Christians believe Jesus is the Son of God and Saviour. In the Gospels, 'Jesus' means 'the Lord saves'."),
        EX("Worked example 1: facts", intro="Give four facts about the birth of Jesus in Luke 2.", steps=[
            S("Fact 1", text="Joseph and Mary went from Nazareth to Bethlehem for the census."),
            S("Fact 2", text="Jesus was born and laid in a manger."),
            S("Fact 3", text="Angels announced the birth to shepherds."),
            S("Fact 4", text="Simeon and Anna recognised him in the temple."),
        ]),
        EX("Worked example 2: model answer plan", intro="Compare the announcements to Zechariah and to Mary.", steps=[
            S("Similarity", text="Both were announced by Gabriel and both children were to have special tasks."),
            S("Zechariah", text="He doubted and was made unable to speak."),
            S("Mary", text="She asked how it could happen, then accepted: 'I am the Lord's servant.'"),
            S("Difference of role", text="John would prepare the way; Jesus would be Son of the Most High and receive David's throne."),
        ]),
        H("Common mistakes"),
        MISTAKE("Attributing the shepherds to Matthew", "The shepherds are in Luke. The magi and the flight to Egypt are in Matthew."),
        MISTAKE("Saying there were three named wise men", "Matthew does not give their number or names; the three gifts are listed."),
        MISTAKE("Confusing John the Baptist's parents with Jesus' parents", "John: Zechariah and Elizabeth. Jesus: Mary and Joseph."),
        QUIZ("Which angel announced the births of both John and Jesus?",
             ["Michael", "Gabriel", "Raphael", "Uriel"], 1,
             "Gabriel appeared to Zechariah and to Mary in Luke 1.",
             hint="He is the angel named in Luke 1.",
             feedback=["Michael is not named in Luke 1.", "", "Raphael is not named in the Gospels.", "Uriel is not named in the Gospels."]),
        QUIZ("Which Gospel tells of the visit of the magi?",
             ["Mark", "Luke", "Matthew", "John"], 2,
             "The magi are in Matthew 2. Luke has the shepherds.",
             hint="Think about which two Gospels have birth stories.",
             feedback=["Mark begins with John the Baptist.", "Luke has shepherds, not magi.", "", "John begins with the Word."]),
        PQ("Why did Joseph and Mary go to Bethlehem?", "For the census ordered by Emperor Augustus; Joseph was of David's family and Bethlehem was David's town."),
        PQ("State two gifts brought by the magi.", "Gold, frankincense and myrrh (any two)."),
        PQ("How can Mary's response 'I am the Lord's servant' guide a young person who is asked to take on an unexpected responsibility?", "Accept humbly and trust God, asking questions honestly as Mary did, and be ready to serve."),
        TIP("In Paper 1, always ask: Matthew or Luke? Luke: Gabriel, Mary, shepherds, manger, Simeon, Anna. Matthew: Joseph's dream, magi, Herod, Egypt."),
        SUM("Matthew, Mark and Luke are the synoptic Gospels; only Matthew and Luke tell of Jesus' birth.",
            "Gabriel announced John's birth to Zechariah and Jesus' birth to Mary.",
            "Jesus was born in Bethlehem, the shepherds visited, and in Matthew the magi came and the family fled to Egypt.",
            "The stories teach humility, trust and God's care for ordinary people."),
    ]))

# ------------------------------------------------------------------ 17 Baptism and temptation
LESSONS.append(lesson(
    module=GOS1, topic="The Baptism and the Temptation",
    title="The Baptism of Jesus and the Temptation in the wilderness",
    slug="rel1-baptism-and-temptation", minutes=22,
    summary="The preaching of John the Baptist, the baptism of Jesus, the voice from heaven, and the three temptations in the wilderness and Jesus' replies.",
    objectives=[
        "Describe the ministry and message of John the Baptist",
        "Tell the story of the baptism of Jesus and what happened",
        "List the three temptations and Jesus' answers",
        "Apply the lessons about temptation to daily life",
    ],
    key_concepts=["John the Baptist", "Repentance", "Baptism", "Holy Spirit", "Temptation", "Wilderness"],
    blocks=[
        H("Introduction"),
        T("Before an important job or an examination, a person often needs a time of preparation. Jesus' public work begins with two events: his baptism by John and forty days of testing in the wilderness."),
        H("John the Baptist"),
        T("John lived in the wilderness of Judea, wore clothing of camel hair with a leather belt and ate locusts and wild honey. He preached a baptism of repentance for the forgiveness of sins, in the Jordan river. "
          "Crowds from Jerusalem and Judea came to him. He told them to produce fruit that shows repentance, and not to rely on being Abraham's descendants (Luke 3:7-14 has his advice to crowds, tax collectors and soldiers: share, be honest, do not abuse power)."),
        T("John said that one who was more powerful than he would come after him. John was not worthy to untie his sandals. That coming one would baptise with the Holy Spirit."),
        D("**Repentance** means turning away from wrong and returning to God, with a real change of life. **Baptism** is a washing with water, a sign of repentance and new life.", title="Repentance and baptism"),
        H("The baptism of Jesus"),
        T("Jesus came from Galilee to the Jordan to be baptised by John. John hesitated, saying that he needed to be baptised by Jesus, but Jesus said it was proper to fulfil all righteousness (Matthew 3). "
          "As Jesus came up out of the water, the heavens opened, the Spirit of God descended like a dove, and a voice from heaven said, 'This is my beloved Son, with whom I am well pleased' (in Mark and Luke the voice speaks to Jesus: 'You are my beloved Son')."),
        KEY("Meaning of the baptism", "Christians understand it this way.", cards=[
            ["Identification", "Jesus shared in the life of the people he came to save."],
            ["Approval", "The Father declares Jesus to be his beloved Son."],
            ["Empowerment", "The Holy Spirit comes on Jesus for his ministry."],
            ["A model", "Christians are baptised in his name as a sign of new life."],
        ]),
        H("The Temptation"),
        T("Straight after, the Spirit led Jesus into the wilderness. He fasted for forty days and nights and was tempted by the devil. Mark mentions the temptation briefly. Matthew and Luke give three temptations and Jesus' replies from the book of Deuteronomy. "
          "Matthew's order is below. Luke gives the second and third in the opposite order."),
        CODE("""1  Stones into bread
   Satan: 'If you are the Son of God, tell these stones to become bread.'
   Jesus: People do not live on bread alone, but on every word from God.
2  Jump from the temple
   Satan: 'Throw yourself down; God will send angels to catch you.'
   Jesus: Do not put the Lord your God to the test.
3  The kingdoms of the world
   Satan: 'All this I will give you if you bow down and worship me.'
   Jesus: Worship the Lord your God and serve him only.""", "text", title="The three temptations (Matthew 4)"),
        IMG("f5rel-1-baptism-temptation-flow.svg",
            alt="Flow from John in the wilderness to the baptism, the Spirit leading Jesus into the wilderness, the three temptations and the beginning of Galilean ministry",
            caption="Figure 1. From John's preaching to the start of the ministry in Galilee."),
        T("After the temptation, the Gospels say angels came and served Jesus (in Matthew and Mark). Jesus then went to Galilee and began to preach: 'Repent, for the kingdom of heaven is near' (Matthew 4:17)."),
        KEY("What the temptations mean", "Use in essays.", cards=[
            ["Bread", "Not to use power for himself or put physical needs above God. Obeying God matters more than food."],
            ["Temple", "Not to test God or seek a spectacular show of power."],
            ["Kingdoms", "Not to take a shortcut to power by giving up loyalty to God."],
            ["For us", "Jesus resisted by knowing and trusting scripture. We face similar pressures: money, show-off, power."],
        ]),
        EX("Worked example 1: facts", intro="State three things that happened at the baptism of Jesus.", steps=[
            S("Fact 1", text="John baptised him in the river Jordan."),
            S("Fact 2", text="The Spirit came down like a dove."),
            S("Fact 3", text="A voice from heaven called Jesus the beloved Son."),
        ]),
        EX("Worked example 2: model answer plan", intro="How can Jesus' temptation help students resisting wrong pressure?", steps=[
            S("Preparation", text="Jesus knew the scriptures; students can build values through study and prayer."),
            S("Resistance", text="He replied calmly, with scripture, not argument."),
            S("Priorities", text="Obedience to God before comfort, show or power."),
            S("Support", text="He was strengthened by angels; we can seek support from family, church and friends."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying John baptised Jesus in the Nile", "The baptism was in the Jordan river."),
        MISTAKE("Calling John the Baptist a disciple of Jesus", "John was the forerunner who prepared the way; he had his own disciples."),
        MISTAKE("Saying the temptation lasted forty years", "It lasted forty days and nights."),
        QUIZ("In which river did John baptise Jesus?",
             ["Nile", "Jordan", "Euphrates", "Jabbok"], 1,
             "The Jordan.",
             hint="It flows into the Dead Sea.",
             feedback=["The Nile is in Egypt.", "", "The Euphrates is in Mesopotamia.", "The Jabbok is where Jacob wrestled."]),
        QUIZ("How did Jesus reply to the temptation to turn stones into bread?",
             ["He turned them into bread", "He quoted that people live not on bread alone but on God's word", "He ignored the devil", "He asked John for help"], 1,
             "He quoted Deuteronomy 8:3.",
             hint="He answered with scripture.",
             feedback=["He refused.", "", "He answered him.", "John was not there."]),
        PQ("What did John the Baptist wear and eat?", "Camel-hair clothing with a leather belt; locusts and wild honey."),
        PQ("List the three temptations in Matthew's order.", "Turning stones into bread; throwing himself down from the temple; receiving the kingdoms of the world in return for worship."),
        PQ("A student is offered money to help someone cheat in the GCE examination. How does Jesus' reply to the third temptation guide the student's answer?", "Keep loyalty to what is right and refuse shortcuts to gain, even if they look attractive; serve God only."),
        TIP("Paper 1: the three temptations in order, the quotation from Deuteronomy and the meaning of repentance. Mention that Luke changes the order."),
        SUM("John the Baptist preached repentance and baptised in the Jordan.",
            "Jesus was baptised, the Spirit came like a dove and the voice from heaven called him the beloved Son.",
            "In the wilderness he fasted forty days and resisted three temptations with scripture.",
            "He then began to preach in Galilee."),
    ]))

# ------------------------------------------------------------------ 18 Twelve and Sermon
LESSONS.append(lesson(
    module=GOS1, topic="The Twelve and the Sermon on the Mount",
    title="The call of the Twelve and the Sermon on the Mount",
    slug="rel1-twelve-and-sermon-on-the-mount", minutes=25,
    summary="How Jesus called the first disciples and the Twelve, who they were, and the main teachings of the Sermon on the Mount (Matthew 5 to 7).",
    objectives=[
        "Describe the call of the first disciples at the lake of Galilee",
        "Name the Twelve and say what kind of people they were",
        "Outline the Beatitudes and the main teaching of the Sermon on the Mount",
        "Apply the teaching on love, forgiveness and honesty to daily life",
    ],
    key_concepts=["Disciple", "Apostle", "Beatitudes", "Salt and light", "Lord's Prayer", "Golden Rule", "Two builders"],
    blocks=[
        H("Introduction"),
        T("A teacher cannot teach a whole nation alone, so he needs helpers. Jesus gathered a group of followers to learn from him, to share his work and to carry on after him. He then taught them and the crowd on a hillside. The teaching is called the Sermon on the Mount."),
        H("The call of the first disciples"),
        T("By the lake of Galilee, Jesus saw two brothers, Simon (called Peter) and Andrew, casting a net. He said, 'Follow me, and I will make you fishers of people.' They left their nets and followed. "
          "He called James and John, sons of Zebedee, who were mending nets in their boat with their father. They too left and followed (Matthew 4:18-22; Mark 1:16-20). In Luke 5, the call follows a great catch of fish. "
          "Jesus also called Levi (Matthew), a tax collector at his booth, who left his work and gave a feast for Jesus (Mark 2)."),
        D("A **disciple** is a learner and follower. **Apostle** means 'one who is sent'. The Gospels use these words of the Twelve: those Jesus chose, from a larger group of disciples, to be with him and to be sent out.", title="Disciple and apostle"),
        H("The Twelve"),
        T("Mark 3, Matthew 10 and Luke 6 list the Twelve. The lists differ slightly in one name, so check your Bible. They are:"),
        CODE("""Simon Peter           Andrew
James (son of Zebedee) John
Philip                Bartholomew
Matthew               Thomas
James (son of Alphaeus)  Thaddaeus / Judas son of James
Simon the Zealot      Judas Iscariot""", "text", title="The Twelve (names vary slightly in the lists)"),
        T("They were ordinary people: fishermen, a tax collector, a political activist (Simon the Zealot). Twelve is a symbolic number, recalling the twelve tribes of Israel."),
        H("The Sermon on the Mount"),
        T("In Matthew 5 to 7, Jesus goes up a mountainside, sits down and teaches. Luke 6 gives a shorter version on level ground. The sermon begins with the **Beatitudes**, sayings that start with 'Blessed are...'."),
        CODE("""Blessed are the poor in spirit
Blessed are those who mourn
Blessed are the meek
Blessed are those who hunger and thirst for righteousness
Blessed are the merciful
Blessed are the pure in heart
Blessed are the peacemakers
Blessed are those persecuted for righteousness""", "text", title="The Beatitudes in outline (Matthew 5)"),
        T("Jesus says his followers are the salt of the earth and the light of the world. They should let their good deeds shine so that people give glory to God. "
          "He did not come to abolish the law but to fulfil it. Then he gives examples ('You have heard it said... but I say to you...'): anger as well as murder is wrong; lust as well as adultery; keep promises without making oaths; do not take revenge; love your enemies and pray for those who persecute you."),
        T("He teaches about giving, praying and fasting without showing off. He gives the Lord's Prayer as a model. He tells his hearers not to store up treasures on earth, to serve God rather than money, and not to worry, for God cares for the birds and the flowers. "
          "He says, 'Do not judge, or you too will be judged.' He gives the Golden Rule: do to others what you would have them do to you. He ends with the story of two builders, one on rock and one on sand: those who hear and do his words are like the wise builder."),
        IMG("f5rel-1-sermon-outline.svg",
            alt="Outline of the Sermon on the Mount in five blocks: Beatitudes, salt and light, fulfilling the law, religion without show, trust and treasure, with the builders at the end",
            caption="Figure 1. A map of the Sermon on the Mount."),
        KEY("Key themes", "For essays and application.", cards=[
            ["Love", "Love for enemies and neighbours, not only friends."],
            ["Humility and mercy", "The Beatitudes honour the humble and merciful."],
            ["Honesty", "Let your 'Yes' be yes; do not show off; keep promises."],
            ["Trust in God", "Do not be anxious; seek God's kingdom first."],
            ["Doing", "Hearing is not enough; the wise builder acts."],
        ]),
        EX("Worked example 1: facts", intro="Name four of the Twelve and give the occupation of two.", steps=[
            S("Names", text="Peter, Andrew, James and John."),
            S("Occupations", text="Peter and Andrew were fishermen; Matthew (Levi) was a tax collector."),
        ]),
        EX("Worked example 2: model answer plan", intro="Explain what Jesus taught about love in the Sermon on the Mount.", steps=[
            S("Enemies", text="Love your enemies and pray for those who persecute you."),
            S("Revenge", text="Do not take revenge; turn the other cheek."),
            S("Golden Rule", text="Treat others as you want to be treated."),
            S("Reason", text="God's love extends to good and bad; his followers should imitate him."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Peter was a tax collector", "Peter was a fisherman. Matthew (Levi) was the tax collector."),
        MISTAKE("Confusing the Beatitudes with the Ten Commandments", "The Ten Commandments were given at Sinai. The Beatitudes begin the Sermon on the Mount."),
        MISTAKE("Saying the Sermon is in Mark", "The full Sermon on the Mount is in Matthew 5 to 7. Luke has a shorter sermon (Luke 6)."),
        QUIZ("Which of the Twelve was a tax collector?",
             ["Peter", "Matthew (Levi)", "Andrew", "Thomas"], 1,
             "Matthew, also called Levi, was a tax collector.",
             hint="He gave a feast for Jesus and his friends.",
             feedback=["Peter was a fisherman.", "", "Andrew was a fisherman.", "The Gospels do not say Thomas was a tax collector."]),
        QUIZ("What does the Golden Rule say?",
             ["Love only your friends", "Do to others what you would want them to do to you", "Give a tenth of your income", "Keep the sabbath"], 1,
             "It is found in Matthew 7:12.",
             hint="It is about how we treat others.",
             feedback=["Jesus taught the opposite.", "", "That is a different teaching.", "That is one of the Ten Commandments."]),
        PQ("Which two brothers were called first at the lake?", "Simon Peter and Andrew."),
        PQ("Give two things the Sermon on the Mount says about prayer.", "Pray in private, not to be seen; do not use many empty words; use the Lord's Prayer as a model (any two)."),
        PQ("A neighbour keeps insulting a church member. How might the teaching on enemies guide the response?", "Respond without revenge, pray for them, and show kindness; try for peace."),
        TIP("Know the names of the Twelve and the Beatitudes. For essays, group the Sermon into themes: love, honesty, humility, trust, action."),
        SUM("Jesus called fishermen, a tax collector and others to follow him; twelve became apostles.",
            "The Sermon on the Mount (Matthew 5 to 7) begins with the Beatitudes.",
            "It teaches love for enemies, honesty, humility, trust in God and the Golden Rule.",
            "Jesus ends by calling hearers to do his words, like the wise builder."),
    ]))

# ------------------------------------------------------------------ 19 Miracles
LESSONS.append(lesson(
    module=GOS1, topic="Miracles of Jesus",
    title="Nature and healing miracles of Jesus",
    slug="rel1-miracles-of-jesus", minutes=24,
    summary="The main kinds of miracle in the synoptic Gospels, with examples such as the calming of the storm, the feeding of the five thousand, the paralysed man and Jairus' daughter, and their meaning.",
    objectives=[
        "Name different kinds of miracles in the synoptic Gospels",
        "Tell four miracle stories accurately",
        "Explain what the miracles show about Jesus and the kingdom of God",
        "Explain the importance of faith and compassion in the stories",
    ],
    key_concepts=["Miracle", "Nature miracle", "Healing", "Faith", "Compassion", "Kingdom of God"],
    blocks=[
        H("Introduction"),
        T("In a village, when someone is sick, family and friends gather around, pray and take the person for help. The Gospels tell many stories of Jesus meeting people in need. They call them signs or mighty works. This lesson looks at the synoptic accounts."),
        D("A **miracle** is an event that Christians believe shows God's power at work in a special way. The Gospels use the miracles as signs that the kingdom of God is near.", title="Miracle"),
        H("Kinds of miracle"),
        KEY("Four groups", "A way of remembering the miracles.", cards=[
            ["Nature miracles", "Calming the storm; feeding the five thousand; walking on the water."],
            ["Healing miracles", "The leper; the paralysed man; the woman with bleeding; blind Bartimaeus."],
            ["Casting out evil spirits", "The man in the synagogue at Capernaum; the Gerasene man."],
            ["Raising the dead", "Jairus' daughter; the widow's son at Nain (Luke only)."],
        ]),
        H("Four stories"),
        T("**The calming of the storm** (Mark 4:35-41). Jesus and the disciples were crossing the lake of Galilee in a boat when a great windstorm came. Jesus was asleep in the stern. The disciples woke him and said, 'Teacher, don't you care if we drown?' "
          "He rebuked the wind and said to the waves, 'Quiet! Be still!' There was calm. He asked them why they were afraid and had no faith. They were amazed and asked who he was that even the wind and waves obey him."),
        T("**The feeding of the five thousand** (Mark 6:30-44). A large crowd followed Jesus to a lonely place. He had compassion on them because they were like sheep without a shepherd. Late in the day, the disciples wanted to send the people away to buy food. "
          "Jesus said, 'You give them something to eat.' They had five loaves and two fish. Jesus gave thanks, broke the bread and gave it to the disciples to distribute. All ate and were satisfied, and twelve baskets of pieces were left."),
        T("**The paralysed man** (Mark 2:1-12). Jesus was teaching in a house at Capernaum, and the house was so full there was no room. Four friends carried a paralysed man on a mat. Unable to get through the crowd, they dug through the roof and lowered him down. "
          "Jesus saw their faith and said, 'Son, your sins are forgiven.' Some teachers of the law thought this was blasphemy, because only God can forgive sins. Jesus said, 'Get up, take your mat and go home.' The man got up and walked out, and the people were amazed."),
        T("**Jairus' daughter and the woman with bleeding** (Mark 5:21-43). Jairus, a synagogue leader, begged Jesus to come and heal his dying daughter. On the way, a woman who had been bleeding for twelve years, and had spent all her money on doctors, touched Jesus' cloak, believing she would be healed. "
          "She was healed. Jesus asked who touched him, and she came forward trembling. He said, 'Daughter, your faith has healed you. Go in peace.' Messengers then said the girl had died, but Jesus said, 'Don't be afraid; just believe.' He took her by the hand and said, 'Little girl, get up!' and she got up and walked."),
        IMG("f5rel-1-galilee-map.svg",
            alt="Schematic map of the lake of Galilee showing Nazareth, Cana, Capernaum, Bethsaida and the region of the Gerasenes, with the Jordan river",
            caption="Figure 1. Places around the lake of Galilee (schematic, not to scale)."),
        KEY("What the miracles show", "Use in essays.", cards=[
            ["Power", "Jesus has authority over nature, illness, evil and death."],
            ["Compassion", "He healed the outcast and the poor, and touched those thought unclean."],
            ["Faith", "In several stories faith is the setting for healing, and the faith of friends mattered."],
            ["The kingdom", "The miracles are signs that God's rule has begun."],
        ]),
        EX("Worked example 1: facts", intro="Give three details of the story of the paralysed man.", steps=[
            S("Detail 1", text="Four friends carried him to the house at Capernaum."),
            S("Detail 2", text="They made an opening in the roof and lowered him."),
            S("Detail 3", text="Jesus forgave his sins and then healed him."),
        ]),
        EX("Worked example 2: model answer plan", intro="What do the miracles teach about faith?", steps=[
            S("Friends", text="Jesus saw the faith of the four friends."),
            S("The woman", text="Her trust led her to touch his cloak; he said her faith had healed her."),
            S("Jairus", text="He was told to keep believing."),
            S("Disciples", text="In the storm, they were asked why they had little faith."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing the numbers", "Five thousand were fed with five loaves and two fish; twelve baskets remained."),
        MISTAKE("Confusing Jairus' daughter with the widow's son", "Jairus' daughter is in Mark, Matthew and Luke. The widow's son at Nain is in Luke only."),
        MISTAKE("Saying the paralysed man was healed before his sins were forgiven", "Jesus first forgave his sins, then told him to rise and walk."),
        QUIZ("How many loaves and fish did the disciples have at the feeding of the five thousand?",
             ["Seven loaves and a few fish", "Five loaves and two fish", "Two loaves and five fish", "Twelve loaves and no fish"], 1,
             "Five loaves and two fish. The feeding of the four thousand has seven loaves.",
             hint="The numbers match the title 'five thousand'.",
             feedback=["That is the feeding of the four thousand.", "", "The numbers are reversed.", "Twelve is the number of baskets collected."]),
        QUIZ("In the story of the paralysed man, why was he lowered through the roof?",
             ["He wanted to surprise Jesus", "The crowd blocked the door", "The door was locked", "Jesus asked them to"], 1,
             "The house was so crowded that the friends could not get near Jesus.",
             hint="Think about the crowd.",
             feedback=["The text points to a practical reason.", "", "The door was not locked.", "Jesus did not ask this."]),
        PQ("State two nature miracles of Jesus.", "Calming the storm; feeding the five thousand; walking on the water (any two)."),
        PQ("Which Gospel alone tells of the raising of the widow's son at Nain?", "Luke."),
        PQ("A church group visits a hospital in your area. How do the healing miracles of Jesus guide what they do?", "Show compassion and care, including to people others avoid; pray and help practically; support the sick and their families."),
        TIP("Paper 1 may ask for the Gospel, place and people in each story. Make a card for each miracle: who, where, what Jesus said, what it teaches."),
        SUM("Miracles of Jesus include nature miracles, healings, driving out evil spirits and raising the dead.",
            "Four key stories are the storm, the feeding of the five thousand, the paralysed man and Jairus' daughter.",
            "They show Jesus' power, compassion and the importance of faith.",
            "The Gospels present them as signs that the kingdom of God has come near."),
    ]))

# ------------------------------------------------------------------ 20 Parables
LESSONS.append(lesson(
    module=GOS1, topic="Parables of the Kingdom",
    title="The parables of the kingdom of God",
    slug="rel1-parables-of-the-kingdom", minutes=24,
    summary="What a parable is, what Jesus meant by the kingdom of God, and the meaning of the sower, the weeds, the mustard seed, the yeast, the hidden treasure, the pearl and the net.",
    objectives=[
        "Define parable and kingdom of God",
        "Tell the parable of the sower and explain its four soils",
        "Explain the parables of the mustard seed, yeast, treasure and pearl",
        "Apply the parables to everyday faith and life",
    ],
    key_concepts=["Parable", "Kingdom of God", "Sower", "Weeds", "Mustard seed", "Treasure and pearl"],
    blocks=[
        H("Introduction"),
        T("In a Cameroonian village, an elder may teach a lesson with a story about a tortoise or a farmer, because a story is easier to remember than a lecture. Jesus often taught in stories called parables."),
        D("A **parable** is a short story from everyday life that teaches a spiritual lesson. The **kingdom of God** (or kingdom of heaven) means God's rule, which Jesus said was coming near in his own ministry and which people can enter by trusting and obeying him.", title="Parable and kingdom"),
        H("The sower (Mark 4:1-20; Matthew 13:1-23)"),
        T("A farmer scatters seed. Some falls on the path and birds eat it. Some falls on rocky ground with little soil; it springs up quickly but the sun scorches it because it has no root. "
          "Some falls among thorns, which choke it. Some falls on good soil and produces a crop, thirty, sixty or even a hundred times what was sown."),
        T("Jesus explains: the seed is the word of God. The path stands for people who hear but lose the message. The rocky ground is those who receive it with joy but fall away in trouble. "
          "The thorns are those who are choked by the worries of life and the love of wealth. The good soil are those who hear the word, accept it and bear fruit."),
        KEY("The four soils", "Remember this table.", cards=[
            ["Path", "Hears but does not understand. The evil one takes the word away."],
            ["Rocky ground", "Quick joy, no root. Falls away under trouble."],
            ["Thorns", "Worries and the lure of wealth choke the word."],
            ["Good soil", "Hears, understands and bears fruit."],
        ]),
        H("Parables of growth and value"),
        T("**The weeds** (Matthew 13:24-30, 36-43). A farmer sowed good seed, but an enemy sowed weeds among the wheat. The servants wished to pull them up but the farmer said to wait until harvest, lest wheat be uprooted. "
          "It teaches patience and that final judgement belongs to God."),
        T("**The mustard seed and the yeast** (Matthew 13:31-33). The kingdom is like a mustard seed, the smallest of seeds that grows into a large plant where birds make nests. It is like yeast that a woman mixes into a large amount of flour until it works through all the dough. "
          "Small beginnings can lead to great results."),
        T("**The hidden treasure and the pearl** (Matthew 13:44-46). A man finds treasure hidden in a field and sells everything to buy the field. A merchant finds a pearl of great value and sells all he has to buy it. The kingdom is worth more than everything else."),
        T("**The net** (Matthew 13:47-50). A net caught fish of every kind; the good were kept and the bad thrown away. It is also about a final separation at the end of time."),
        IMG("f5rel-1-parables-chart.svg",
            alt="Chart linking each parable to its main lesson: sower, weeds, mustard seed, yeast, treasure and pearl, net",
            caption="Figure 1. Parables of the kingdom and their main lessons."),
        H("Why parables?"),
        T("Parables made people think. Those willing to listen could understand; those who did not wish to listen might not. Jesus sometimes explained them privately to his disciples (Mark 4:10-12, 33-34)."),
        EX("Worked example 1: the sower", intro="Match each soil to the person it describes.", steps=[
            S("Path", text="A person who hears and does not understand."),
            S("Rocky ground", text="A person who is joyful at first but gives up when trouble comes."),
            S("Thorns", text="A person distracted by worry and the love of money."),
            S("Good soil", text="A person who hears, understands and bears fruit."),
        ]),
        EX("Worked example 2: model answer plan", intro="What do the parables of the treasure and the pearl teach?", steps=[
            S("Story", text="A man sells everything for a field with treasure; a merchant sells all for a pearl."),
            S("Meaning", text="The kingdom of God is worth more than anything else."),
            S("Response", text="Joyful, wholehearted commitment, even at a cost."),
            S("Application", text="Putting faith above money, fame or success."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling the kingdom a country", "In the parables the kingdom of God means God's rule over lives, not a state with borders."),
        MISTAKE("Saying the mustard seed is the largest seed", "It is described as the smallest seed that grows into a large plant."),
        MISTAKE("Mixing the sower with the weeds", "In the sower, the seed is the word. In the weeds, the good seed is people of the kingdom and the weeds are people of the evil one."),
        QUIZ("In the parable of the sower, what does the seed stand for?",
             ["Money", "The word of God", "The disciples", "The temple"], 1,
             "Jesus explained that the seed is the word.",
             hint="Look at Jesus' own explanation.",
             feedback=["Money is the thorn that chokes it.", "", "The disciples are among the hearers.", "The temple is not part of this parable."]),
        QUIZ("What is the main point of the mustard seed and the yeast?",
             ["Gardens need weeding", "The kingdom starts small and grows great", "Bread is better than seed", "Women should bake"], 1,
             "Both stories show small beginnings with great results.",
             hint="Compare the size at the start with the size at the end.",
             feedback=["Not the point of this parable.", "", "Not the point.", "Not the point."]),
        PQ("Name the four kinds of ground in the parable of the sower.", "The path, rocky ground, thorns, good soil."),
        PQ("What does the parable of the weeds teach about judgement?", "Judgement is left to God at the end; people must be patient and not uproot others hastily."),
        PQ("A church youth group in a rural area starts a small project with few members. How can the mustard seed encourage them?", "Small beginnings can grow; keep faithful, work steadily and trust that results may be large later."),
        TIP("Learn the sower in detail: it is the parable most often set. For others, remember one image and one lesson."),
        SUM("A parable is a short story with a spiritual meaning. The kingdom of God is God's rule.",
            "The sower shows four responses to God's word.",
            "The mustard seed and yeast show small beginnings with great results; the treasure and pearl show the kingdom's worth.",
            "The weeds and the net speak of patience and the final judgement."),
    ]))

