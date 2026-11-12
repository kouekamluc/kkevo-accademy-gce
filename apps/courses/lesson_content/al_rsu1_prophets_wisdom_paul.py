"""A Level Religious Studies (0785), Upper Sixth: prophets, wisdom and Paul (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("religious-studies", "upper-sixth")

M1 = "Old Testament: Prophecy in Israel & the Eighth-Century Prophets"
M2 = "Old Testament: Exilic Prophecy & Wisdom Literature"
M3 = "New Testament: Apostolic History & the Pauline Epistles"

LESSONS = []

LESSONS.append(lesson(
    module=M1, topic="Hebrew prophecy",
    title="Hebrew prophecy: origins, types and the test of a true prophet",
    slug="rsu1-hebrew-prophecy",
    minutes=22,
    summary="What a Hebrew prophet was, how prophecy developed from seers and ecstatic bands to the classical prophets, and how Israel tried to tell true prophets from false ones.",
    objectives=[
        "Define a prophet and explain the words nabi, roeh and hozeh",
        "Compare ecstatic, court, cultic and classical prophecy",
        "Describe the call, message and methods of the classical prophets",
        "Evaluate the Old Testament tests of a true prophet and their difficulties",
    ],
    key_concepts=["Nabi", "Seer", "Ecstatic prophecy", "Classical prophets", "Forthtelling and foretelling", "True and false prophets"],
    blocks=[
        H("Introduction"),
        T("In many societies people believe that some individuals speak for a higher power. In ancient Israel such a person was called a "
          "**prophet**. Prophets advised kings, warned the rich, comforted the broken and sometimes paid for their words with their lives.\n\n"
          "This lesson looks at the origins and nature of Hebrew prophecy. It prepares you for the individual prophets in the next lessons. "
          "Religious Studies at A Level asks you to describe, compare and evaluate: scholars hold different views on many points here, so we say 'scholars argue' where they do."),
        IMG("alrsu1-prophets-timeline.svg", alt="Timeline bars showing when Elijah, Amos, Hosea, Isaiah, Jeremiah, Ezekiel and Deutero-Isaiah prophesied, with the falls of Samaria and Jerusalem and the capture of Babylon marked.", caption="Figure 1. The prophets of this course in time (dates approximate; check your textbook)."),
        D("A person who, according to the Old Testament, was called by Yahweh to speak his word to the people. The usual Hebrew word is **nabi**, "
          "often explained as 'one who is called' or 'one who announces'. Scholars debate the exact root, so check your textbook.", title="Prophet"),
        D("Early Israel also used the words **roeh** and **hozeh**, both meaning 'seer'. A seer was consulted for guidance on lost property, journeys or "
          "decisions. First Samuel 9 explains that the person now called a prophet was formerly called a seer. Samuel is the best-known example.", title="Seer"),
        H("Foretelling or forthtelling?"),
        T("Many people think a prophet mainly predicts the future. Scholars stress that the main task was **forthtelling**: speaking Yahweh's message "
          "to the present situation. **Foretelling** (predicting) was part of it, but usually as a warning or promise tied to the people's conduct: "
          "'if you continue, this will follow'. A prophecy of judgement could be cancelled by repentance, as the book of Jonah illustrates."),
        H("Stages in the history of prophecy"),
        KEY("Four main types", "Scholars distinguish types of prophet, but the types overlap and the evidence is thin.", cards=[
            ["Ecstatic prophets", "Bands of prophets who used music and dance and fell into trance-like states (1 Samuel 10 and 19). Saul joined such a band. Some scholars compare similar groups in neighbouring cultures."],
            ["Court prophets", "Prophets attached to a king, such as Nathan and Gad under David. They gave advice and sometimes rebuked the king (2 Samuel 12)."],
            ["Cultic prophets", "Some scholars (for example Sigmund Mowinckel) argued that many prophets served in the Temple worship. Others doubt that this was common. Check your textbook."],
            ["Classical (writing) prophets", "From the eighth century BC: Amos, Hosea, Isaiah, Micah, then Jeremiah, Ezekiel and others. Books are linked to their names. Most spoke against the existing order."],
        ]),
        T("Outside Israel, written texts from the city of Mari (on the Euphrates, in the eighteenth century BC) record messages from gods delivered through "
          "human intermediaries. This shows that prophecy was not unique to Israel, though scholars debate how close the parallels are."),
        H("How a classical prophet worked"),
        T("The classical prophets share some features. Most describe a **call**: a moment of encounter with Yahweh that gave a mission (Isaiah 6, Jeremiah 1, "
          "Ezekiel 1 to 3, Amos 7). They used the **messenger formula**, 'Thus says Yahweh', like a royal messenger carrying a king's words. "
          "They used speech, poetry, parables and symbolic actions (Jeremiah's yoke, Ezekiel's model of Jerusalem). Their main concerns were loyalty to Yahweh alone, "
          "justice in society and the meaning of political events such as the rise of Assyria and Babylon."),
        TIP("In an essay, name the feature and then give a biblical example in a few words. 'Symbolic action: Jeremiah wore a yoke' is stronger than 'prophets did strange things'."),
        H("True and false prophets"),
        T("Israel faced a hard problem. Many people claimed to speak for Yahweh and they disagreed. The book of Deuteronomy offers tests. "
          "Deuteronomy 13 says a prophet who calls people to follow other gods is false, even if a sign comes true. "
          "Deuteronomy 18 says that if a prophet speaks in Yahweh's name and the word does not come true, Yahweh did not send it. Other texts add more ideas."),
        KEY("Possible tests of a true prophet", "Each test has a weakness that students should be able to state.", cards=[
            ["Loyalty to Yahweh", "A true prophet leads the people to Yahweh alone. Weakness: a false prophet could use Yahweh's name while telling the king only what he wished to hear."],
            ["Fulfilment of the word", "A true prophecy comes to pass. Weakness: the test works only after the event, when the people already had to decide. A warning may also be withdrawn when people repent."],
            ["Moral life and message", "True prophets condemn injustice, false ones promise peace without change (Jeremiah 23, Micah 3). Weakness: moral failings are hard to judge from outside."],
            ["Unpopular message", "A message against the king's wish is often a mark of truth (1 Kings 22: Micaiah against the four hundred). Weakness: not every unpopular person is a prophet."],
        ]),
        T("The clearest conflict is Jeremiah 28. Hananiah said in Yahweh's name that Babylon's power would be broken within two years. Jeremiah said the yoke would "
          "not be removed so soon. Both claimed to speak for Yahweh. The text shows that Jeremiah first said 'Amen, may it be so' and waited. "
          "The reader is told that Hananiah died the same year. Many students miss this point: the story shows how hard it was to decide in the moment."),
        TIP("Exam link: the Board's 2023 report names the Old Testament as a section of Paper 2 (essays; four questions from one section) and Paper 1 tests concepts of all the religions in the syllabus by multiple choice. "
            "Prophecy may be set in either. The report's named OT section was the Patriarchs to David, so check which OT sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="'Hebrew prophets were mainly predictors of the future.' Discuss.", steps=[
            S("Introduction", text="Define prophet (nabi) and forthtelling versus foretelling. Thesis: prediction was real but secondary."),
            S("For the view", text="Prophets announced coming judgement or restoration (Amos on exile, Isaiah on the Assyrian threat). Deuteronomy 18 tests prophets by whether the word came true."),
            S("Against the view", text="The main task was to apply Yahweh's demands to the present: Amos on social injustice, Hosea on worship of Baal. Predictions were conditional and tied to behaviour."),
            S("Conclusion", text="Prophets were messengers of Yahweh to their own time. Future prediction served that message."),
        ]),
        EX("Model essay plan 2", intro="Explain the development of prophecy in Israel from the seers to the classical prophets.", steps=[
            S("Early stage", text="Seers (roeh, hozeh), such as Samuel, and ecstatic bands (1 Samuel 10 and 19)."),
            S("Monarchy", text="Court prophets (Nathan, Gad) advised and rebuked kings. Elijah and Elisha opposed rulers and Baal worship."),
            S("Classical stage", text="From the eighth century, prophets whose speeches were collected and written: Amos, Hosea, Isaiah. Their concerns were justice, covenant loyalty and the fate of the nation."),
            S("Comment", text="The stages overlap. Scholars disagree about how far there was a clear break."),
        ]),
        MISTAKE("Treating all prophets as the same", "Candidates often describe 'the prophets' as one group. Name the type (seer, ecstatic, court, classical) and use the right example."),
        MISTAKE("Writing only a story", "The Board's 2023 report repeatedly says that candidates narrate Bible stories instead of answering the question. State the point first, then support it with a short example."),
        QUIZ("Which word describes the main task of most classical prophets?",
             ["Foretelling only", "Forthtelling Yahweh's word to the present situation", "Offering sacrifices in the Temple", "Advising kings on war"], 1,
             "Prediction was part of the message, but the prophets mostly addressed the present conduct of the people and leaders.",
             hint="Think about what Amos said about the courts and the poor.",
             feedback=["Prediction was important but not the main task.", "", "Priests, not prophets, were responsible for sacrifices.", "Court prophets sometimes did this, but classical prophets often opposed royal policy."]),
        QUIZ("Which text gives a test that a prophecy which does not come true was not spoken by Yahweh?",
             ["Genesis 1", "Deuteronomy 18", "Psalm 23", "Amos 1"], 1,
             "Deuteronomy 18 gives this test, alongside Deuteronomy 13 on loyalty to Yahweh.",
             hint="It is one of the law books.",
             feedback=["Genesis 1 is a creation account.", "", "A psalm is a prayer, not a test of prophecy.", "Amos 1 begins his oracles against nations."]),
        PQ("Distinguish between a seer and a classical prophet. (Paper 3 style structural question)",
           "A seer (roeh or hozeh), such as Samuel in 1 Samuel 9, was consulted privately for guidance about practical matters, often for a fee or gift. "
           "A classical prophet, such as Amos or Isaiah, spoke publicly against the nation's sins, was called by a vision, and left a collection of speeches in a book that bears his name. "
           "The seer answered questions put to him; the classical prophet brought an unwelcome message that nobody had asked for."),
        PQ("Explain two difficulties in using fulfilment as the test of a true prophet.",
           "First, a prophecy can be tested only after the event, but the people had to decide whether to listen before it. Second, many prophecies were warnings that depended on repentance: "
           "if people changed, the disaster might not come (as in Jonah), yet the prophet was still true. A third point is that some false prophets may by chance be proved right. "
           "Deuteronomy therefore also tests loyalty to Yahweh (Deuteronomy 13), so fulfilment alone is not enough."),
        PQ("Briefly compare Jeremiah and Hananiah (Jeremiah 28).",
           "Both claimed to speak in Yahweh's name. Hananiah promised that Babylon's yoke would be broken within two years and broke Jeremiah's wooden yoke as a sign. "
           "Jeremiah said the exile would last longer and that Hananiah's message gave false hope. The story shows the problem of testing prophets: both sounded confident. "
           "The narrative says Hananiah died that year, which in the Old Testament view confirmed Jeremiah. Scholars note that the people of the time had no such confirmation."),
        SUM("A prophet (nabi) spoke Yahweh's word; the seer (roeh, hozeh) was an earlier figure who gave guidance.",
            "Forthtelling (speaking to the present) was the main task; foretelling was usually conditional.",
            "Types overlap: ecstatic bands, court prophets, possibly cultic prophets, and the classical writing prophets from the eighth century.",
            "Classical prophets had a call, used the messenger formula and attacked injustice and idolatry.",
            "Tests of a true prophet (loyalty to Yahweh, fulfilment, moral message, unpopularity) each have limits."),
    ],
))

LESSONS.append(lesson(
    module=M1, topic="Elijah",
    title="Elijah: Yahweh against Baal in the northern kingdom",
    slug="rsu1-elijah",
    minutes=22,
    summary="The religious and political crisis of Ahab's reign, Elijah's confrontations (drought, Carmel, Naboth, Horeb) and what they teach about covenant loyalty and justice.",
    objectives=[
        "Describe the political and religious crisis in the northern kingdom under Ahab and Jezebel",
        "Explain the events on Mount Carmel and their meaning",
        "Explain the Naboth incident and the prophet's role against royal power",
        "Assess Elijah's importance for later prophecy",
    ],
    key_concepts=["Divided kingdom", "Baal worship", "Syncretism", "Mount Carmel", "Naboth's vineyard", "Horeb"],
    blocks=[
        H("Introduction"),
        T("After the death of Solomon the kingdom split into two: Israel in the north and Judah in the south. The northern kingdom had no Temple in Jerusalem "
          "and its kings needed alliances. Under King **Ahab** (reigned about 874 to 853 BC; check your textbook for exact dates) the north was strong and rich, "
          "but its worship of Yahweh was under serious threat. The prophet **Elijah**, from Tishbe in Gilead, stood against the king.\n\n"
          "The stories of Elijah are in 1 Kings 17 to 19 and 21, and 2 Kings 1 to 2. They belong to the period of the **early or pre-classical** prophets: "
          "no book bears Elijah's name, but his actions shaped later prophecy."),
        D("The mixing of the worship of Yahweh with the worship of other gods. In the northern kingdom this meant that Yahweh's people might honour Baal, a Canaanite god of storm, rain and fertility, "
          "alongside or instead of Yahweh. The prophets treated this as a breach of the covenant.", title="Syncretism"),
        H("The crisis under Ahab"),
        KEY("Why the crisis was serious", "Political, economic and religious pressures combined.", cards=[
            ["Politics", "Ahab's father Omri founded a strong dynasty and built the capital, Samaria. Ahab kept peace with Phoenicia by marrying Jezebel, daughter of the king of Sidon."],
            ["Religion", "Jezebel brought the worship of Baal (the texts link her with the Baal of Tyre) and supported hundreds of his prophets. Ahab built a temple and altar for Baal in Samaria (1 Kings 16)."],
            ["Society", "Royal power over land and justice grew. The story of Naboth shows a king and queen taking land by false accusation."],
        ]),
        T("Baal was thought to give rain and good harvests. Farmers in a land that depends on rain were tempted to turn to him. "
          "Elijah's first act is to announce a drought in the name of Yahweh (1 Kings 17). This challenged Baal in his own area of power."),
        H("Drought and the widow of Zarephath"),
        T("During the drought Elijah is fed by ravens and then stays with a widow in Zarephath, a town in Sidon, Jezebel's own country. "
          "Her jar of flour and jug of oil do not run out, and her son is restored to life. The story presents Yahweh as the one who gives food and life, and shows his care for a foreigner and a poor woman."),
        H("Mount Carmel (1 Kings 18)"),
        T("After about three years Elijah meets Ahab and calls the people to Mount Carmel with the prophets of Baal. The test is simple: each side prepares a bull for sacrifice, "
          "but lights no fire. The god who answers by fire is God. The prophets of Baal call on him from morning until evening with no result. "
          "Elijah repairs the altar of Yahweh, uses twelve stones (one for each tribe), pours water over the offering, and prays briefly. Fire falls and the people cry that Yahweh is God. "
          "The prophets of Baal are killed, and rain returns."),
        KEY("Meaning of Carmel", "Examiners want the significance, not only the story.", cards=[
            ["Monotheistic loyalty", "Elijah asks how long the people will limp between two opinions: the issue is exclusive loyalty to Yahweh (the first commandment)."],
            ["Yahweh controls nature", "Fire and rain, both claimed by Baal, answer to Yahweh."],
            ["Unity of Israel", "The twelve stones show Elijah calling all Israel back to the covenant."],
        ]),
        TIP("Exam link: the Old Testament forms a section of Paper 2 (essays) in the Board's 2023 report. The report notes that many candidates narrate stories without stating the significance. "
            "Open each Elijah answer with the meaning, then support it with the event. Check which OT sections your school teaches.", title="Exam link"),
        H("Naboth's vineyard (1 Kings 21)"),
        T("Ahab wanted the vineyard of Naboth, next to the palace. Naboth refused because the land was his family inheritance, and Israelite tradition did not allow land to be sold away from the family. "
          "Jezebel arranged false witnesses to accuse Naboth of cursing God and the king. Naboth was stoned and Ahab took the vineyard. "
          "Elijah met Ahab there and announced judgement on his house.\n\n"
          "This story shows that the king is under the law of Yahweh. It is often seen as a model for the later social criticism of Amos and Isaiah."),
        H("Horeb (1 Kings 19)"),
        T("After Carmel, Jezebel threatened Elijah's life and he fled south to Mount Horeb (another name for Sinai in some traditions), exhausted and discouraged. "
          "There Yahweh was not in the wind, the earthquake or the fire, but in a 'still small voice' (the exact translation varies, check your Bible). "
          "Elijah was told to anoint Hazael, Jehu and Elisha, and that seven thousand in Israel had not bowed to Baal. The prophet learns that Yahweh works quietly as well as dramatically, and that he is not alone. "
          "Many scholars note the links to Moses at Sinai: Elijah is presented as a new Moses calling Israel back to the covenant."),
        EX("Model essay plan 1", intro="Explain the significance of the contest on Mount Carmel.", steps=[
            S("Setting", text="Ahab and Jezebel promote Baal; the people are divided; three years of drought."),
            S("The contest", text="Fire from heaven as the test. Baal's prophets fail; Elijah's simple prayer is answered."),
            S("Meaning", text="Yahweh alone is God; he controls fire and rain; the people must choose; twelve stones show the covenant of all Israel."),
            S("Result and limits", text="The people confess Yahweh, but Jezebel's anger shows that the struggle continued. Horeb follows."),
        ]),
        EX("Model essay plan 2", intro="'Elijah was concerned with social justice as much as with worship.' Discuss.", steps=[
            S("For worship", text="Carmel, the drought as a challenge to Baal, and Horeb's call to loyalty."),
            S("For social justice", text="Naboth's vineyard: a king may not use false law to take a poor man's inheritance; Yahweh judges the royal house."),
            S("Link", text="In the covenant, loyalty to Yahweh and justice among his people belong together. Baal worship also supported royal power over land."),
            S("Judgement", text="Both concerns were equal. Elijah's work points forward to Amos and Hosea."),
        ]),
        MISTAKE("Calling Elijah a writing prophet", "No book of Elijah exists. He belongs to the earlier tradition and is known from 1 and 2 Kings."),
        MISTAKE("Retelling the whole story", "A question on 'the significance' asks for meaning. A long summary of the drought, the widow and the bulls will not earn the marks."),
        QUIZ("Who was the queen who promoted Baal worship in Israel?",
             ["Athaliah", "Jezebel", "Bathsheba", "Michal"], 1,
             "Jezebel, from Sidon, married Ahab and supported the worship of Baal.",
             hint="She came from Sidon.",
             feedback=["Athaliah was a queen of Judah, linked to the house of Ahab, but she is not the one in the Elijah stories.", "", "Bathsheba was David's wife and Solomon's mother.", "Michal was Saul's daughter and David's wife."]),
        QUIZ("What does the story of Naboth's vineyard mainly show?",
             ["Baal could not give rain", "A king is not above Yahweh's law and cannot take a family's land by false accusation", "The Temple must be rebuilt", "Elijah escaped to Horeb"], 1,
             "Elijah condemns Ahab's seizure of Naboth's land: even the king answers to the covenant.",
             hint="Think about why Naboth refused.",
             feedback=["That is the issue at Carmel and in the drought.", "", "The Temple is not part of this story.", "Horeb is in 1 Kings 19, a different story."]),
        PQ("Why did Elijah's confrontation with Baal's prophets matter in the political situation of Israel? (structural question)",
           "Baal worship came with Jezebel and had royal backing, so it was both political (alliance with Phoenicia) and religious. Elijah's challenge insisted that loyalty to Yahweh could not be shared. "
           "Because Baal was believed to control rain, the drought and then the return of rain showed Yahweh's power over the area claimed by Baal. "
           "The contest therefore defended the covenant against a royal policy of syncretism."),
        PQ("What lessons does Horeb teach about Elijah and about God?",
           "Elijah is discouraged and in danger, so Horeb shows his human weakness. Yahweh meets him in a quiet voice rather than in the wind, earthquake or fire, "
           "showing that God does not only work in spectacular signs. Elijah is given tasks (to anoint Hazael, Jehu and Elisha) and is told that seven thousand remain faithful, which corrects his belief that he was alone. "
           "Scholars see links with Moses and Sinai, presenting Elijah as a renewer of the covenant."),
        PQ("Compare the prophet Nathan's rebuke of David with Elijah's rebuke of Ahab.",
           "Both prophets confront a king who has abused power over a man (Uriah for David, Naboth for Ahab) and announce judgement in Yahweh's name. "
           "Both show that kings are under the covenant. A difference is that David repented (2 Samuel 12), while Ahab's response was brief humility followed by continued failure (1 Kings 21 and 22). "
           "Nathan acted as a court prophet in David's house; Elijah acted as an independent opponent of a royal house that supported another god."),
        SUM("Under Ahab and Jezebel the northern kingdom was threatened by Baal worship with royal support.",
            "Elijah, a pre-classical prophet from Gilead, announced the drought and met the prophets of Baal on Carmel.",
            "Carmel was about exclusive loyalty to Yahweh, who controls fire and rain.",
            "Naboth's vineyard shows that prophets defended justice and the limits of royal power.",
            "Horeb shows Elijah's weakness, Yahweh's quiet presence and the call to continue the work through Elisha."),
    ],
))

LESSONS.append(lesson(
    module=M1, topic="Amos",
    title="Amos: social justice, empty worship and the Day of the Lord",
    slug="rsu1-amos",
    minutes=23,
    summary="Amos of Tekoa, the prosperity and injustice of Israel under Jeroboam II, his attack on ritual without justice, his reversal of the Day of the Lord and the debated hope at the end.",
    objectives=[
        "Describe Amos's background, call and historical setting",
        "Explain his condemnation of social injustice and of religious hypocrisy",
        "Explain how he reversed the popular idea of the Day of the Lord",
        "Evaluate the place of election and hope in his message",
    ],
    key_concepts=["Tekoa", "Jeroboam II", "Social justice", "Election and responsibility", "Day of the Lord", "Bethel"],
    blocks=[
        H("Introduction"),
        T("Amos is usually seen as the first of the classical prophets whose words were collected in a book. "
          "He lived in the middle of the eighth century BC, when Israel under **Jeroboam II** (reigned about 793 to 753 BC; check your textbook) enjoyed peace, expansion and wealth. "
          "Amos came from **Tekoa** in Judah, in the south, but his message was addressed to the northern kingdom, especially the shrine at **Bethel**.\n\n"
          "The book describes him as a herdsman and a dresser of sycamore figs (1:1 and 7:14). He says he was not a prophet by profession or from a prophetic guild: Yahweh took him from his flock and told him to prophesy. "
          "Scholars debate whether he was a poor shepherd or an owner of flocks, so check your textbook."),
        H("The world Amos entered"),
        T("Israel was strong. Trade was growing and there were fine houses, ivory furniture and feasts. But the wealth was uneven: Amos accuses the rich of crushing the poor. "
          "Farmers could fall into debt and lose their land or freedom. Courts at the city gate, where cases were heard, were open to bribes. Meanwhile the shrines were busy with sacrifices and pilgrimage. "
          "Many Israelites believed that Yahweh was on their side and would defend them, because they were his chosen people."),
        D("The prophetic demand that Yahweh's people practise fairness in courts, business and daily life. In Amos it is the test of true religion. The Hebrew words are often given as *mishpat* (justice) and *tsedaqah* (righteousness). Check how your textbook translates them.", title="Social justice"),
        H("Structure of the book"),
        KEY("A simple outline", "Examiners expect you to know the main parts.", cards=[
            ["Chapters 1 and 2", "Oracles against the nations (Damascus, Gaza, Tyre, Edom, Ammon, Moab, Judah) and then Israel. The pattern 'for three transgressions, and for four' leads the audience in, then turns on Israel."],
            ["Chapters 3 to 6", "Speeches against Israel: election and responsibility (3:2), the wealthy women and the oppression of the poor (4:1), false worship (5:21 to 24), woe to the complacent (6)."],
            ["Chapters 7 to 9", "Five visions (locusts, fire, plumb line, basket of summer fruit, the Lord at the altar), the clash with Amaziah (7:10 to 17), and a promise of restoration (9:11 to 15)."],
        ]),
        H("Judgement on the nations and on Israel"),
        T("In chapters 1 and 2 Amos condemns crimes of cruelty and war among the neighbours. The listeners would agree. Then he reaches Judah and finally Israel itself. "
          "His point is that Yahweh judges by moral standards that apply to all, and Israel will not be excused. "
          "Israel is condemned for selling the needy for a pair of sandals, trampling the heads of the poor, using the same woman in sexual abuse and taking garments in pledge (2:6 to 8)."),
        H("Election means responsibility"),
        T("Amos 3:2 says that Yahweh has known only Israel among all the families of the earth, 'therefore' he will punish them for their sins. Election was a belief that Yahweh had chosen Israel in the Exodus. "
          "Most people took this as a guarantee of safety. Amos turns it around: being chosen brings greater responsibility, not a privilege to do wrong."),
        H("Worship without justice"),
        T("In chapters 4 and 5 Amos mocks the shrines of Bethel and Gilgal, whose pilgrims offer many sacrifices. In 5:21 to 24 Yahweh says he hates and despises their festivals and will not accept their offerings. "
          "Instead, justice should roll on like water and righteousness like a never-failing stream. "
          "Scholars discuss whether Amos rejects all sacrifice or only worship cut off from justice. Most take the second view: the book attacks hypocrisy and does not propose to abolish worship."),
        TIP("Do not say that Amos was against religion. State carefully that he was against worship that was not joined to justice.", title="Careful wording"),
        H("The Day of the Lord"),
        T("Many Israelites looked forward to a 'Day of the Lord', a day when Yahweh would act to defeat Israel's enemies and bring light and victory to his people. "
          "Amos 5:18 to 20 says: woe to those who long for it, for it will be darkness and not light. The popular hope is reversed: the day will fall on Israel. "
          "Scholars debate the origin of the idea (a holy war tradition, a festival of Yahweh's kingship or something else). What is clear is the reversal."),
        H("Amos and Amaziah"),
        T("In 7:10 to 17 Amaziah, the priest of Bethel, reports Amos to King Jeroboam for conspiracy and tells him to go home to Judah and earn his bread there. "
          "Amos answers that he is no professional prophet, that Yahweh took him from the flock, and that Amaziah's family will suffer when Israel is exiled. "
          "The incident shows the tension between official religion and a prophet's independent call, and the claim that the exile of Israel was coming."),
        H("Hope at the end?"),
        T("The book ends in 9:11 to 15 with the promise that Yahweh will restore David's fallen shelter and the land will overflow with harvest. "
          "Many scholars think these verses were added after the fall of the kingdom or after the exile, because the rest of the book speaks only of judgement. "
          "Others think they could be authentic and show that judgement is not the final word. Both views are in textbooks, so check yours."),
        TIP("Exam link: prophets belong to the Old Testament options (Paper 2 essays) and their central ideas can appear in Paper 1 multiple choice. The Board's 2023 report warns against narration; "
            "when asked about Amos, state the idea (justice, election, hypocrisy) and then give one verse-based example. Check which OT sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="Explain the social teaching of Amos.", steps=[
            S("Setting", text="Prosperity under Jeroboam II, but an uneven distribution: debt, bribes, slavery."),
            S("Examples", text="The poor sold for silver and sandals (2:6), the rich women of Samaria (4:1), bribery at the gate (5:10 to 12)."),
            S("Theology", text="Yahweh is the God of justice; election brings responsibility (3:2)."),
            S("Link to worship", text="Festivals are rejected where justice is missing (5:21 to 24)."),
        ]),
        EX("Model essay plan 2", intro="'Amos taught that worship without justice is worthless.' Discuss.", steps=[
            S("For", text="Yahweh hates festivals and rejects sacrifices (5:21 to 24); the rich who oppress the poor still go to Bethel."),
            S("Against or qualified", text="The book does not tell people to give up worship; it attacks hypocrisy. Some scholars compare it with other prophets who show similar attitudes (Hosea 6:6, Isaiah 1)."),
            S("Judgement", text="The statement is broadly correct if 'worship' means worship alone. Amos wants both justice and sincere worship."),
        ]),
        MISTAKE("Saying that Amos was a priest or professional prophet", "Amos denies this (7:14). He is described as a herdsman and fig-dresser from Judah."),
        MISTAKE("Explaining the Day of the Lord as a day of joy", "Amos reverses the popular expectation: for a sinful Israel it will be darkness."),
        QUIZ("Where was Amos from?",
             ["Samaria", "Tekoa in Judah", "Bethel", "Anathoth"], 1,
             "Amos came from Tekoa in the south but prophesied in the northern kingdom.",
             hint="He was not a northerner.",
             feedback=["Samaria was the northern capital.", "", "Bethel was the northern shrine where he spoke.", "Anathoth was the home of Jeremiah."]),
        QUIZ("How did Amos change the popular idea of the Day of the Lord?",
             ["He said it would never come", "He said it would be a day of darkness for sinful Israel", "He said it would restore the monarchy", "He said it was a festival at Bethel"], 1,
             "In 5:18 to 20 the day Israel longs for is a day of judgement on them.",
             hint="Compare light and darkness.",
             feedback=["He says it will come.", "", "That idea belongs to other passages.", "The text does not describe it as a festival."]),
        PQ("Why did Amos have difficulties with the authorities at Bethel? (structural question)",
           "Amos announced that the royal house of Jeroboam would fall and that Israel would go into exile. Amaziah, priest of the royal shrine, reported this to the king as conspiracy "
           "and told Amos to return to Judah. Amos replied that he had been called by Yahweh and repeated the judgement. The conflict shows the clash between an official sanctuary that served the king "
           "and a prophet who spoke from an independent call."),
        PQ("Explain what Amos meant by 'You only have I known' (3:2).",
           "It refers to Israel's election: Yahweh chose Israel in the Exodus and made a covenant with them. Israel took this as protection. Amos says that election means closer accountability: "
           "because Israel knows Yahweh's will, its sins are punished. The statement removes the assumption that Israel's status makes it safe and prepares the judgement speeches."),
        PQ("To what extent is Amos a prophet of hope?",
           "Most of the book is judgement: oracles of doom, visions of destruction and the reversal of the Day of the Lord. The call to seek good and not evil (5:14 to 15) allows that Yahweh might be gracious to a remnant. "
           "The final promise of restoration (9:11 to 15) is the clearest hope, but many scholars think it was added later. A balanced answer says that Amos is mainly a prophet of judgement, with a possible hope in the book as we have it."),
        SUM("Amos, a herdsman from Tekoa in Judah, prophesied at Bethel about 760 BC under Jeroboam II (check dates).",
            "He condemned the oppression of the poor and bribery in the courts, and the hypocrisy of rich worshippers.",
            "Election brings responsibility: 'you only have I known' leads to punishment for sin.",
            "The Day of the Lord is reversed into darkness for Israel.",
            "Amaziah's challenge shows the conflict between the official shrine and the prophet; the closing hope is debated."),
    ],
))

LESSONS.append(lesson(
    module=M1, topic="Hosea",
    title="Hosea: covenant love (hesed), unfaithful Israel and the knowledge of God",
    slug="rsu1-hosea",
    minutes=22,
    summary="Hosea's marriage and children as signs, the charge of Baal worship and political folly, the meaning of hesed and knowledge of God, and Yahweh's costly love.",
    objectives=[
        "Describe Hosea's setting in the last years of the northern kingdom",
        "Explain the marriage to Gomer and the names of the children, and the ways scholars read them",
        "Explain hesed and the knowledge of God in Hosea",
        "Evaluate the picture of Yahweh as faithful husband and loving parent",
    ],
    key_concepts=["Hesed", "Knowledge of God", "Marriage metaphor", "Baalism", "Ephraim", "Repentance"],
    blocks=[
        H("Introduction"),
        T("Hosea was a prophet of the northern kingdom, a younger contemporary of Amos. His ministry stretched over the last decades before the fall of Samaria to Assyria in 722 BC (check your textbook for dates). "
          "These years saw violent change: after Jeroboam II died, kings were murdered and replaced in quick succession, and Israel turned for safety first to Assyria, then to Egypt. "
          "Hosea speaks as a man whose own family life has become a message.\n\n"
          "Where Amos stresses justice, Hosea stresses **love and loyalty** within the covenant. Together they show two sides of the prophetic message."),
        D("A Hebrew word for steadfast love, loyalty and faithfulness within a relationship, especially the covenant. It is translated 'steadfast love', 'loyal love', 'mercy' or 'kindness'. "
          "Hosea 6:6 says Yahweh desires hesed and not sacrifice. The word is often used of Yahweh's love for Israel and of the love Israel should return.", title="Hesed"),
        D("In Hosea this is not only information. To 'know' God (da'at Elohim) means to be in a relationship of loyalty, obedience and trust. "
          "Hosea 4:1 to 6 says there is no knowledge of God in the land and that the people perish for lack of knowledge.", title="Knowledge of God"),
        H("Hosea's marriage (chapters 1 to 3)"),
        T("Yahweh tells Hosea to take 'a wife of whoredom' and have children by her. The woman is called Gomer. The children are given names that act as messages:"),
        KEY("The children's names", "Each name carries a warning, and the book later reverses each.", cards=[
            ["Jezreel", "Recalls the bloodshed linked to Jehu's dynasty at Jezreel; 'God sows'. It announces the end of the dynasty. Later the name is a promise: God will sow Israel in the land."],
            ["Lo-ruhamah", "'Not pitied' or 'not shown mercy'. Yahweh will no longer show mercy to Israel. Later reversed to 'pitied'."],
            ["Lo-ammi", "'Not my people'. The covenant bond is broken. Later reversed to 'my people'."],
        ]),
        T("In chapter 3 Hosea is told to love a woman who is loved by another man and who is an adulteress, as Yahweh loves Israel though they turn to other gods. He buys her back and she must wait many days before he lives with her again. "
          "It is not certain whether this is Gomer or another woman. Scholars disagree."),
        KEY("Ways of reading the marriage", "Check which approach your textbook prefers.", cards=[
            ["Literal", "A real marriage, with real unfaithfulness. Hosea learned through his own pain what Yahweh feels. Weakness: it raises moral questions about why Yahweh would command it."],
            ["Allegory or vision", "An account in words only, which stands for Yahweh and Israel. Weakness: the details such as the children's names look like real events."],
            ["Two stages", "Gomer was a bride from a cult of Baal that included sexual rites, so the 'harlotry' reflects Israel's setting. This view is debated, since the evidence for such rites is itself disputed."],
        ]),
        H("The charges against Israel"),
        T("Hosea accuses Israel of forgetting Yahweh. He attacks:"),
        KEY("Main charges", "Use these headings in exam answers.", cards=[
            ["Baal worship", "The people thought grain, wine and oil came from Baal and not from Yahweh (2:5 and 2:8). They worshipped at hilltop shrines. For Hosea, going after Baal was like a wife chasing lovers."],
            ["Political unfaithfulness", "Kings made and unmade by violence (7:7, 8:4) and alliances with Assyria and Egypt (7:11, 12:1) in place of trust in Yahweh."],
            ["Failure of leaders", "Priests did not teach and shared in the profit from sacrifices (4:6 to 8). Hosea says there is no faithfulness, no hesed and no knowledge of God in the land (4:1)."],
            ["Empty ritual and quick repentance", "Their love is like morning mist (6:4). Yahweh wants hesed and the knowledge of God more than burnt offerings (6:6)."],
        ]),
        H("The love of Yahweh"),
        T("Hosea 11 is one of the most moving chapters in the Old Testament. Yahweh is pictured as a parent who loved Israel as a child, taught him to walk and took him in his arms, but the child went on turning away. "
          "Yahweh asks how he can give Israel up. The text says his heart recoils within him and he will not carry out his fierce anger, 'for I am God and not a human being'. "
          "Hosea also pictures Yahweh as a husband who will allure Israel again into the wilderness and betroth her in righteousness and hesed (2:14 to 20)."),
        TIP("Exam link: for Paper 2 (Old Testament essays) and for the multiple-choice questions on key terms, learn hesed with its translations, Hosea's family, and the two images (husband and parent). "
            "The Board's 2023 report asks candidates for significance rather than narration. Check which OT sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="Explain how Hosea's family life was used to teach his message.", steps=[
            S("Setting", text="Last years of Israel; Baal worship and political chaos."),
            S("Marriage", text="The marriage to Gomer is a sign of Yahweh's marriage to Israel: faithful love met with unfaithfulness."),
            S("Children", text="Jezreel, Lo-ruhamah and Lo-ammi announce judgement; the reversals announce restoration."),
            S("Evaluation", text="Debate whether the marriage was literal or symbolic; either way, it makes the covenant a relationship of love."),
        ]),
        EX("Model essay plan 2", intro="'Hosea is a prophet of love and not of judgement.' Discuss.", steps=[
            S("Love", text="Hosea 11 and 2:14 to 20: Yahweh's compassion, forgiveness and new betrothal."),
            S("Judgement", text="Lo-ammi, exile and the fall of Israel (for example 9:3 and 10:6) are announced because the people reject Yahweh."),
            S("Link", text="Judgement is the other side of love: a husband or parent who loves is hurt by betrayal. The book moves from judgement to hope."),
            S("Judgement", text="Both belong together, so the statement is half true."),
        ]),
        MISTAKE("Defining hesed as 'sacrifice'", "Hosea sets hesed against sacrifice (6:6). It is loyal love, not a ritual offering."),
        MISTAKE("Writing that Hosea condemns 'the poor'", "Hosea accuses Israel's leaders and the people at large of idolatry and political unfaithfulness. His social concern is shared with Amos, but his main theme is covenant love."),
        QUIZ("What is the meaning of the name of Hosea's child 'Lo-ammi'?",
             ["God sows", "Not pitied", "Not my people", "Peace of God"], 2,
             "Lo-ammi means 'not my people', announcing a break in the covenant relationship.",
             hint="Ammi means 'my people'.",
             feedback=["That is the meaning of Jezreel.", "That is Lo-ruhamah.", "", "That name is not used for one of the children."]),
        QUIZ("Which of these best describes hesed in Hosea?",
             ["A temple tax", "Loyal, steadfast covenant love", "A military oath", "A feast of Baal"], 1,
             "Hesed means loyalty and steadfast love within a relationship, which Yahweh asks of Israel.",
             hint="Think of Hosea 6:6.",
             feedback=["It is not a payment.", "", "It is not a military term in Hosea.", "Baal feasts are the object of Hosea's attack."]),
        PQ("Explain the importance of hesed in Hosea. (structural question)",
           "Hesed means steadfast covenant love. Hosea says the land lacks it (4:1) and that Yahweh desires it more than sacrifice (6:6). "
           "The people's hesed is 'like the morning mist' because it disappears quickly. Yahweh's own hesed is shown in the picture of the faithful husband and the loving parent. "
           "It therefore defines both what Yahweh is like and what Israel should be."),
        PQ("Describe how Hosea portrays Israel's unfaithfulness and the reasons for it.",
           "Israel is a wife who goes after lovers: the Baals, whom the people credit with grain, wine and oil (2:5 to 8). The people forget Yahweh because their leaders, priests and kings have failed to teach and to lead. "
           "Political choices show the same lack of trust: the kings make alliances with Assyria and Egypt, and the kingdom suffers violence and conspiracy. "
           "The result is a lack of knowledge of God (4:1 to 6), which Hosea treats as the root problem."),
        PQ("Compare the messages of Amos and Hosea.",
           "Both prophesied to the northern kingdom in the eighth century and both announced judgement. Amos concentrated on social justice, the hypocrisy of worship and the Day of the Lord; "
           "Hosea concentrated on covenant faithfulness, Baal worship and the love of Yahweh. Amos is a southerner who came to Israel; Hosea is a northerner. "
           "The two complement each other: justice and love are both requirements of the covenant."),
        SUM("Hosea prophesied in the northern kingdom in the years before the fall of Samaria (722 BC), a time of coups and foreign alliances.",
            "His marriage to Gomer and the children's names (Jezreel, Lo-ruhamah, Lo-ammi) teach Yahweh's relationship with Israel.",
            "Hesed means loyal covenant love; knowledge of God means trusting relationship, not just information.",
            "He attacks Baal worship, political unfaithfulness and failing leaders.",
            "Yahweh is shown as a faithful husband and loving parent whose love is costly and who promises a new beginning."),
    ],
))

LESSONS.append(lesson(
    module=M1, topic="Isaiah of Jerusalem",
    title="Isaiah of Jerusalem: holiness, Immanuel and the remnant",
    slug="rsu1-isaiah-of-jerusalem",
    minutes=24,
    summary="Isaiah's vision of the holy Yahweh, his advice to Ahaz and the Immanuel sign, the idea of the remnant, trust in Yahweh and the hope of an ideal king.",
    objectives=[
        "Place Isaiah of Jerusalem in the history of Judah and Assyria",
        "Explain the call vision of chapter 6 and the meaning of holiness",
        "Explain the Immanuel sign and the debate about Isaiah 7:14",
        "Explain the remnant, faith and the hope of a righteous king",
    ],
    key_concepts=["Holiness of Yahweh", "Call vision", "Immanuel", "Remnant", "Faith and trust", "Zion", "Messianic hope"],
    blocks=[
        H("Introduction"),
        T("Isaiah lived in Jerusalem in the southern kingdom of Judah in the second half of the eighth century BC. "
          "Unlike Amos and Hosea, who spoke to the north, he spoke to the royal court of Judah and to the city. He prophesied under the kings Uzziah, Jotham, Ahaz and Hezekiah (Isaiah 1:1; check your textbook for the span).\n\n"
          "The book of Isaiah has 66 chapters. Most scholars attribute chapters 1 to 39 mainly to Isaiah of Jerusalem and chapters 40 to 55 and 56 to 66 to later writers (we study Deutero-Isaiah in a later lesson). "
          "This lesson uses the chapters that scholars link with Isaiah himself."),
        H("Historical setting"),
        T("Assyria was the great power. In about 734 to 732 BC the kings Pekah of Israel and Rezin of Damascus tried to force Judah's King Ahaz to join a coalition against Assyria. "
          "When Ahaz refused they threatened Jerusalem (the Syro-Ephraimite war, Isaiah 7). Ahaz appealed to Assyria for help, which made Judah a vassal. "
          "In 722 BC Samaria fell. In 701 BC the Assyrian king Sennacherib invaded Judah in Hezekiah's time and besieged Jerusalem. Isaiah advised trust in Yahweh and not in foreign alliances."),
        H("The call: Isaiah 6"),
        T("The call came 'in the year that King Uzziah died' (about 740 BC, check your textbook). Isaiah saw Yahweh seated on a high throne, the hem of his robe filling the Temple, and seraphim calling to one another: "
          "'Holy, holy, holy is Yahweh of hosts; the whole earth is full of his glory.' The doorposts shook and the house filled with smoke. "
          "Isaiah cried that he was lost, a man of unclean lips living among a people of unclean lips. One of the seraphim touched his lips with a live coal from the altar and declared his guilt removed. "
          "When Yahweh asked 'Whom shall I send?', Isaiah answered 'Here am I; send me.'"),
        D("In Isaiah, Yahweh's holiness means that he is utterly different from humans and from created things, awesome in power and pure in moral character. "
          "Isaiah's favourite title for Yahweh is 'the Holy One of Israel'. Holiness is both transcendence (otherness) and moral purity, so it demands justice from the people.", title="Holiness of Yahweh"),
        T("The commission was hard. Isaiah was told to speak to a people who would hear but not understand. Scholars debate whether this describes Yahweh's purpose or the result Isaiah would meet. "
          "He asks 'How long?' and is told: until cities are ruined. But a 'holy seed', a stump, remains (6:13)."),
        KEY("Effects of the call on Isaiah's message", "Link each theme to chapter 6 in an exam.", cards=[
            ["Holiness and sin", "Because Yahweh is holy, injustice and pride among his people are unbearable (chapter 1, chapter 5)."],
            ["Judgement", "Human pride will be brought low (2:12 to 17). Judgement comes through Assyria."],
            ["Remnant", "A stump remains (6:13). The faithful will survive."],
            ["Sovereignty", "Yahweh rules history, including the empires. He is the real king."],
        ]),
        H("Social criticism"),
        T("Isaiah shares Amos's concern for justice. The Song of the Vineyard (5:1 to 7) says Yahweh looked for justice (mishpat) and found bloodshed, for righteousness and found a cry. "
          "He attacks landowners who join house to house and field to field (5:8), those who call evil good, and leaders who deny justice to widows and orphans (10:1 to 2). "
          "In chapter 1 he says Yahweh is tired of sacrifices and incense and tells the people to wash, learn to do good and seek justice. Like Amos, he does not reject worship but worship divorced from justice."),
        H("Faith and politics: Isaiah 7"),
        T("When Ahaz faced the threat of Pekah and Rezin, Isaiah met him at the end of the conduit of the upper pool, with his son Shear-jashub (the name means 'a remnant will return'). "
          "He told Ahaz to be calm and not afraid, adding 'If you do not stand firm in faith, you will not stand at all' (7:9; translations differ). "
          "Ahaz was told to ask for a sign. He refused, saying he would not test Yahweh. Isaiah answered that Yahweh himself would give a sign: a young woman is or will be with child and will give birth to a son and call him **Immanuel**, 'God with us' (7:14)."),
        KEY("The Immanuel debate", "State the debate fairly. Do not present one view as proven.", cards=[
            ["Meaning in Isaiah's time", "Many scholars see a child born in the near future, perhaps a royal child, whose growth marks the time before the two enemy kings fall (7:16). The name expresses confidence in Yahweh's presence."],
            ["The word almah", "The Hebrew almah means 'young woman'. The Greek Septuagint used parthenos (virgin). Scholars disagree over the force of the Hebrew."],
            ["Christian reading", "Matthew 1:23 quotes the verse in the account of Jesus's birth. Christians read the sign as fulfilled in Jesus; historians also ask what the prophet meant for his own day."],
        ]),
        H("The remnant and the king"),
        D("The idea that after judgement a small faithful group will survive and form the basis of a new future. In Isaiah it appears in the child's name Shear-jashub, the stump of chapter 6 and the 'remnant of Jacob' who will return (10:20 to 23).", title="Remnant"),
        T("Isaiah also hopes for a righteous king from David's line. Chapters 9 and 11 describe a child given to the people on whom government rests, who is called by wonderful titles, and a shoot from the stump of Jesse who judges with righteousness and brings peace in which the wolf lives with the lamb. "
          "Scholars debate whether these poems refer to Hezekiah or another king of Isaiah's day, or to a future ideal king. The passages helped shape later messianic hope."),
        H("Isaiah and Hezekiah in 701 BC"),
        T("When Sennacherib besieged Jerusalem, Isaiah advised Hezekiah to trust Yahweh (Isaiah 36 to 37; 2 Kings 18 to 19). The city was not taken, although Judah suffered badly. "
          "Isaiah believed in the safety of Zion, the city of Yahweh. This belief was challenged after 587 BC, as we see with Jeremiah. Check your textbook for the debate about what exactly saved Jerusalem."),
        TIP("Exam link: Isaiah is part of the Old Testament prophets that may be set in Paper 2 (essays) and Paper 1 (key terms such as remnant, holiness, Immanuel). "
            "The Board's 2023 report repeatedly criticises narration without significance. Give each idea its meaning first. Check which OT sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="Explain the significance of Isaiah's vision in chapter 6.", steps=[
            S("Setting", text="The year Uzziah died; a Temple scene with Yahweh as king."),
            S("The vision", text="Holy, holy, holy; the seraphim; the shaking house; Isaiah's guilt and cleansing."),
            S("Meaning", text="God's holiness and glory; the need for cleansing before a mission; Isaiah's willing answer."),
            S("Effects", text="It shapes his message: holiness and justice, judgement, the remnant, and Yahweh's rule over nations."),
        ]),
        EX("Model essay plan 2", intro="Discuss the view that the Immanuel prophecy was about a child of Isaiah's own time.", steps=[
            S("For", text="The sign was given to Ahaz in a crisis and the child's growth is tied to events within a few years (7:16)."),
            S("Against", text="The Greek translation reads parthenos; Matthew applies the verse to Jesus; some argue that the prophecy has a further meaning."),
            S("Evaluation", text="Historical readers ask what the first hearers would have understood; Christian readers add a later fulfilment. State both without claiming that one is proved."),
        ]),
        MISTAKE("Making Isaiah a northern prophet", "Isaiah lived in Jerusalem and addressed kings of Judah."),
        MISTAKE("Giving only one view of Immanuel", "Say that scholars debate the meaning of 7:14 and describe both the original setting and the later Christian use."),
        QUIZ("What is the main emphasis of Isaiah's vision in chapter 6?",
             ["The kingship of Hezekiah", "The holiness of Yahweh", "The fall of Samaria", "The return from exile"], 1,
             "The seraphim's threefold 'holy' is the centre of the vision.",
             hint="What do the seraphim cry?",
             feedback=["Hezekiah is not named in chapter 6.", "", "Samaria's fall is not the subject of the vision.", "The return from exile belongs to later chapters."]),
        QUIZ("What does the name Shear-jashub mean?",
             ["God with us", "A remnant will return", "The Lord is salvation", "Not my people"], 1,
             "Isaiah's son carried a name that was a message about the remnant.",
             hint="It is linked to the idea of a small survivor group.",
             feedback=["That is Immanuel.", "", "That is the meaning of Isaiah's own name.", "That is Hosea's child Lo-ammi."]),
        PQ("Explain the Immanuel sign in its historical setting. (structural question)",
           "During the Syro-Ephraimite crisis, Ahaz feared Pekah and Rezin. Isaiah told him to trust Yahweh and offered a sign. A young woman would bear a son named Immanuel, 'God with us', "
           "and before the child was old enough to know right from wrong the land of the two kings would be abandoned (7:14 to 16). The sign promised Yahweh's presence and the end of the threat, but also warned that Ahaz's reliance on Assyria would bring Assyria upon Judah."),
        PQ("What did Isaiah mean by the remnant?",
           "He taught that judgement would be severe but not total. A small group would survive and be the basis of a new beginning. The idea is seen in his son's name Shear-jashub, in the stump left when the tree is cut down (6:13), "
           "and in the promise that a remnant of Jacob will return to the mighty God (10:21). The remnant is the faithful minority who trust in Yahweh, not a guarantee for everyone."),
        PQ("Compare Isaiah's social message with that of Amos.",
           "Both attack injustice, such as the rich taking land and denying justice to the poor, and both say that worship without justice is unacceptable (Amos 5, Isaiah 1). "
           "Amos was a southerner who spoke to the north and used the reversal of the Day of the Lord. Isaiah was a Jerusalemite of the court who stressed Yahweh's holiness, faith in political crisis, the remnant and the future king. "
           "Isaiah is also more concerned with the fate of Zion."),
        SUM("Isaiah of Jerusalem prophesied under Uzziah, Jotham, Ahaz and Hezekiah during the Assyrian threat.",
            "The call vision stresses the holiness of Yahweh, and Isaiah's cleansing and willingness.",
            "Isaiah attacked injustice and pride, and told kings to trust Yahweh, not alliances.",
            "Immanuel (7:14) was a sign to Ahaz; scholars and Christians read it in different ways.",
            "The remnant and the hope of a righteous king point beyond judgement."),
    ],
))

LESSONS.append(lesson(
    module=M2, topic="Jeremiah",
    title="Jeremiah: the Temple Sermon, the Confessions and the New Covenant",
    slug="rsu1-jeremiah",
    minutes=24,
    summary="Jeremiah's call and times, his Temple Sermon, his personal Confessions, his advice to the exiles and the promise of a new covenant written on the heart.",
    objectives=[
        "Describe Jeremiah's background, call and the political crisis from Josiah to the fall of Jerusalem",
        "Explain the Temple Sermon and why it provoked opposition",
        "Explain the Confessions and what they show about the prophet",
        "Explain the New Covenant of chapter 31 and how it differs from the Sinai covenant",
    ],
    key_concepts=["Temple Sermon", "Confessions", "New Covenant", "Fall of Jerusalem", "Letter to the exiles", "Baruch"],
    blocks=[
        H("Introduction"),
        T("Jeremiah was a priest from Anathoth, a village near Jerusalem. He was called to be a prophet in the thirteenth year of King Josiah (about 627 BC; check your textbook) and prophesied through the reigns of Josiah, Jehoahaz, Jehoiakim, Jehoiachin and Zedekiah until the fall of Jerusalem in 587 or 586 BC and beyond. "
          "He is the prophet we know best as a person, because his book contains prayers and complaints that show his inner struggles.\n\n"
          "Jeremiah's age was one of crisis: the Assyrian empire declined, Babylon rose, Josiah's religious reform (about 622 BC) raised hope, and then Judah was drawn into wars between Egypt and Babylon. "
          "Babylon took Jerusalem in 597 BC and deported King Jehoiachin and the leading citizens. After a rebellion it destroyed the city and the Temple in 587 or 586 BC."),
        H("The call (chapter 1)"),
        T("Yahweh says he knew Jeremiah before he was formed in the womb. Jeremiah answers that he is only a boy and cannot speak. Yahweh touches his mouth and says he is putting his words there. "
          "Jeremiah's task is 'to pluck up and to pull down, to destroy and to overthrow, to build and to plant'. Visions of an almond branch and a boiling pot from the north explain the task: Yahweh is watching over his word and disaster is coming from the north."),
        H("The Temple Sermon (chapters 7 and 26)"),
        T("At the gate of the Temple Jeremiah told the worshippers not to trust in deceptive words: 'This is the temple of the Lord'. "
          "Many believed that Yahweh would never allow Jerusalem or the Temple to be destroyed, as Isaiah's teaching on Zion had been understood. "
          "Jeremiah said that the Temple would be safe only if they truly changed their ways: acting justly, not oppressing the stranger, the orphan or the widow, not shedding innocent blood and not following other gods. "
          "Otherwise Yahweh would do to the Temple what he had done to Shiloh, the earlier sanctuary that had been destroyed."),
        KEY("Why the sermon caused trouble", "Chapter 26 tells what followed.", cards=[
            ["Challenge to a popular belief", "People relied on the Temple like a lucky charm. Jeremiah said the building could not protect people who broke the covenant."],
            ["Reaction", "Priests and prophets demanded the death penalty. The officials and elders, remembering the case of the prophet Micah, let him go (26:17 to 19)."],
            ["Link to earlier prophets", "Like Amos and Isaiah, he said that worship without justice is useless. His new element is the claim that even the Temple may be destroyed."],
        ]),
        H("The Confessions"),
        D("A group of personal laments in the book (usually listed as 11:18 to 12:6, 15:10 to 21, 17:14 to 18, 18:18 to 23 and 20:7 to 18) in which Jeremiah complains to Yahweh about opposition, loneliness and the pain of being a prophet. "
          "Scholars debate whether they record his own experience or are shaped by later editors. Many take them as a window into his inner life.", title="The Confessions"),
        T("In them Jeremiah says that people plot against him, that his message brings him only mockery, and that he has been deceived or overpowered by Yahweh (20:7). "
          "He curses the day he was born (20:14). Yet he also says that if he tries to hold back the word, it burns in his heart like fire (20:9). "
          "Yahweh does not give him comfort at once; in 15:19 he is told to return and then he will be allowed to stand before Yahweh. "
          "The Confessions show the cost of the prophetic office and a close, honest relationship with God that includes protest."),
        H("Conflict with kings and false prophets"),
        T("Under Jehoiakim, Jeremiah's scroll was read to the king, who cut it up and burned it piece by piece; Baruch the scribe then wrote it again (chapter 36). "
          "Jeremiah wore a yoke to show that nations should submit to Babylon, and clashed with the prophet Hananiah (chapter 28). "
          "During the siege he was imprisoned and thrown into a cistern for 'weakening the morale' of the soldiers (chapters 37 and 38). "
          "He was freed and stayed in the land under the governor Gedaliah, but after Gedaliah was murdered, he was taken to Egypt by people who feared Babylon."),
        H("Letter to the exiles and a field at Anathoth"),
        T("After 597 BC Jeremiah wrote to the exiles in Babylon (chapter 29). He told them to build houses, plant gardens, marry and seek the welfare of the city, because in its welfare they would find theirs. "
          "The exile would be long (the text speaks of seventy years, a round number whose meaning scholars debate). The message was to live faithfully in a foreign land and not to expect a quick return. "
          "In chapter 32, while Jerusalem was under siege, Jeremiah bought a field from his cousin at Anathoth as a sign that houses, fields and vineyards would again be bought in the land."),
        H("The New Covenant (31:31 to 34)"),
        T("The words come in the 'Book of Consolation' (chapters 30 to 33). Yahweh says that days are coming when he will make a **new covenant** with the house of Israel and the house of Judah. "
          "It will not be like the covenant made at the Exodus, which they broke. This time the law will be put within them and written on their hearts. "
          "He will be their God and they will be his people. No one will need to teach their neighbour 'Know the Lord', for all will know him, and he will forgive their wrongdoing and remember their sin no more."),
        KEY("Old and new covenant compared", "A useful table-style plan for an exam answer.", cards=[
            ["Sinai covenant", "Law written on stone tablets, an external demand. The people broke it and the nation fell."],
            ["New covenant", "Law written on the heart: inner change and personal knowledge of God."],
            ["What stays the same", "The same Yahweh, the same people, the same law. The change is in how the people receive and keep it."],
            ["Forgiveness", "A fresh start that rests on God's gift of forgiveness."],
        ]),
        T("Christians later saw the text as fulfilled in Jesus: Luke 22:20 and 1 Corinthians 11:25 speak of the cup as the new covenant in his blood, and Hebrews 8 quotes the passage. "
          "Jewish readers understand the promise within the history of Israel. When you write about the passage, say who is reading it."),
        TIP("Exam link: Jeremiah belongs to the Old Testament prophets that may be set in Paper 2 (essays) or tested by key terms in Paper 1. The Board's 2023 report says many candidates narrate instead of showing significance. "
            "Check which OT sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="Explain the message of Jeremiah's Temple Sermon.", steps=[
            S("Setting", text="The Temple in Jerusalem; popular trust that Yahweh would protect it."),
            S("Message", text="True security depends on justice and loyalty to Yahweh, not on the building. The example of Shiloh."),
            S("Response", text="Priests and prophets demanded his death; officials freed him (chapter 26)."),
            S("Significance", text="It linked the survival of the nation with its conduct and prepared people to understand the destruction of 587 BC."),
        ]),
        EX("Model essay plan 2", intro="Discuss the view that the New Covenant was a complete break with the past.", steps=[
            S("For", text="It is described as 'not like' the covenant at the Exodus; law inside the person; forgiveness; no need for teachers."),
            S("Against", text="The law is the same; the same two parties; the change is in motivation and heart. 'Renewal' is as good a word as 'break'."),
            S("Evaluation", text="Christian readers add Jesus as the one who inaugurates it. The promise does not announce a new religion in Jeremiah but a transformed relationship."),
        ]),
        MISTAKE("Giving Jeremiah as the author of Lamentations and Kings", "Tradition links him with Lamentations but scholars debate this. Say 'tradition' and 'check your textbook'."),
        MISTAKE("Saying the new covenant abolished the law", "In Jeremiah the law is written on the heart. The text does not say that the law is cancelled."),
        QUIZ("Where did Jeremiah deliver his Temple Sermon?",
             ["In Babylon", "At the gate of the Temple in Jerusalem", "At Bethel", "In Egypt"], 1,
             "The sermon was spoken at the Temple gate and its consequences appear in chapters 7 and 26.",
             hint="It is called the Temple Sermon.",
             feedback=["He never went to Babylon.", "", "Bethel is Amos's setting.", "He ended in Egypt but not for this sermon."]),
        QUIZ("According to Jeremiah 31, the New Covenant is different because the law will be",
             ["Written on tablets of stone", "Put within people and written on their hearts", "Taught only by priests", "Given to the Gentiles only"], 1,
             "The change is from an external law to one internalised in the heart.",
             hint="Think about 'heart'.",
             feedback=["That describes the Sinai covenant.", "", "The passage says no one will need to teach their neighbour.", "The text speaks of Israel and Judah."]),
        PQ("What do the Confessions reveal about Jeremiah's ministry? (structural question)",
           "They show his loneliness and suffering: people plot against him, he is mocked, and he feels Yahweh has overpowered him (20:7). They show that he was honest with God and complained to him (15:18), "
           "and that he could not stop speaking because the word burned inside him (20:9). They also show that Yahweh did not remove the pain but called him to continue (15:19 to 21). "
           "They give a rare picture of a prophet as a human being."),
        PQ("Explain Jeremiah's advice to the exiles in chapter 29.",
           "Jeremiah wrote that the exile would last a long time, against false prophets who promised an early return. He told the exiles to build houses, plant gardens, marry, have children and seek the welfare of the city where they lived. "
           "It meant that they could remain faithful to Yahweh in a foreign land and that the future of Israel lay with the exiles. The text also promises that after the period Yahweh will bring them back (29:10 to 14)."),
        PQ("Why was Jeremiah unpopular with the leaders of Judah?",
           "He said that the Temple would not protect Jerusalem (chapters 7 and 26), that Babylon was Yahweh's instrument and that submission was better than revolt (chapters 27 and 38). "
           "He opposed prophets who promised peace, such as Hananiah, and condemned the injustice of kings, such as Jehoiakim. Leaders therefore saw him as unpatriotic and a danger to morale, so he was beaten, imprisoned and threatened with death."),
        SUM("Jeremiah, a priest of Anathoth, prophesied from about 627 BC until after Jerusalem fell in 587 or 586 BC.",
            "His Temple Sermon warned that the building would not save a disobedient people.",
            "The Confessions reveal his pain and his honest dialogue with God.",
            "His letter told the exiles to settle in Babylon and seek its welfare.",
            "The New Covenant promises law on the heart, personal knowledge of God and forgiveness."),
    ],
))

LESSONS.append(lesson(
    module=M2, topic="Ezekiel",
    title="Ezekiel: priest in exile, individual responsibility and the dry bones",
    slug="rsu1-ezekiel",
    minutes=23,
    summary="Ezekiel's call by the river Chebar, his sign acts, the departure of God's glory, individual responsibility in chapter 18, the vision of the dry bones and the hope of a new temple.",
    objectives=[
        "Describe Ezekiel's background, call and setting among the exiles",
        "Explain the sign acts and the role of the watchman",
        "Explain the teaching on individual responsibility in chapter 18",
        "Explain the vision of the dry bones and the hope of restoration",
    ],
    key_concepts=["Exile", "Throne-chariot vision", "Watchman", "Sign acts", "Individual responsibility", "Dry bones", "New temple"],
    blocks=[
        H("Introduction"),
        T("Ezekiel was a priest, the son of Buzi. He was taken to Babylon in the first deportation of 597 BC with King Jehoiachin and lived among the exiles by the river Chebar at a place called Tel Abib. "
          "His call came in the fifth year of the exile (about 593 BC), when he was about thirty, the age at which a priest would begin to serve. Since he was far from the Temple, he could not serve as a priest; Yahweh made him a prophet instead.\n\n"
          "Jeremiah spoke in Judah, while Ezekiel spoke among the exiles. Both lived through the same crisis, the fall of Jerusalem in 587 or 586 BC. "
          "The book has three broad parts: oracles of judgement before the fall (chapters 1 to 24), oracles against nations (25 to 32), and oracles of hope after it (33 to 48)."),
        H("The call: chapters 1 to 3"),
        T("Ezekiel saw a stormy wind from the north, a great cloud with fire, and four living creatures, each with four faces, beside wheels full of eyes. "
          "Above them was a throne and on it a figure like a human form, which is described as the appearance of the likeness of the glory of Yahweh. "
          "The vision showed that Yahweh was not confined to the Temple in Jerusalem: his glory could be seen in Babylon, a foreign land, and his throne could move. "
          "Ezekiel ate a scroll with writing on both sides and was told to speak to Israel, a rebellious house, whether they listened or not."),
        D("A guard who warns a city of danger. In 3:16 to 21 and chapter 33, Ezekiel is made a watchman for Israel. If the watchman sees danger and does not warn, he is responsible for the loss of life. "
          "If he warns and the people ignore it, he has saved himself. The image defines the prophet's duty to speak, not to be successful.", title="Watchman"),
        H("Sign acts and messages of judgement"),
        T("Ezekiel is known for dramatic symbolic actions. He drew a siege of Jerusalem on a clay brick, lay on his side for many days to carry the guilt of Israel and Judah, ate measured food and water, shaved his head and divided the hair (chapters 4 and 5), and packed baggage like an exile (chapter 12). "
          "When his wife died he was told not to mourn publicly, as a sign that the people would not be able to mourn when the Temple fell (chapter 24). "
          "Some scholars have suggested that he had a psychological illness, while others see the actions as deliberate teaching. Check your textbook."),
        H("The glory leaves the Temple (chapters 8 to 11)"),
        T("In a vision Ezekiel is taken to Jerusalem and shown the idolatry practised in the Temple precincts: images on the walls, elders offering incense, women weeping for Tammuz and men worshipping the sun. "
          "Then the glory of Yahweh leaves the Temple, moves to the threshold, the east gate and finally the mountain east of the city. "
          "The Temple had been seen as Yahweh's home and the guarantee of safety. Ezekiel says Yahweh himself abandons the Temple because of the people's sin. This prepares the people for the fall of Jerusalem."),
        H("Individual responsibility (chapter 18)"),
        T("The exiles had a saying: 'The parents have eaten sour grapes, and the children's teeth are set on edge.' It meant that they were suffering for the sins of earlier generations (such as Manasseh), and that nothing they did could change it. "
          "Ezekiel 18 says that Yahweh rejects the proverb. The one who sins shall die, but a person who does what is right and just shall live. "
          "Three cases are given: a righteous father, his violent son and that man's righteous son. Each is judged by their own conduct. "
          "Even the wicked person who turns away from sin shall live, because Yahweh takes no pleasure in anyone's death."),
        KEY("What chapter 18 teaches", "Be ready to explain the context and the limits.", cards=[
            ["Context", "Exiles believed they were doomed by past sins and Yahweh was unfair. The chapter answers fatalism and complaint."],
            ["Teaching", "Each person is responsible for their own conduct. Repentance is always possible and life is offered."],
            ["Limits", "Other parts of the Old Testament speak of family and communal consequences, and Ezekiel himself says the nation shares guilt. Scholars see a shift in emphasis rather than the discovery of the individual."],
            ["Link", "Compare Jeremiah 31:29 to 30, which uses the same proverb."],
        ]),
        TIP("Exam link: Ezekiel belongs to the Old Testament prophets that may appear in Paper 2 (essays) and in key-term items in Paper 1. The Board's 2023 report calls for significance, not retelling. Check which OT sections your school teaches.", title="Exam link"),
        H("The valley of dry bones (chapter 37)"),
        T("Ezekiel is brought to a valley full of very dry bones. Yahweh asks if the bones can live. Ezekiel answers that only Yahweh knows. "
          "He is told to prophesy to the bones and they come together, sinews and flesh appear, but there is no breath. He prophesies to the breath (the Hebrew word ruach can mean breath, wind or spirit), and the bodies stand as a vast army. "
          "Yahweh explains that the bones are the whole house of Israel, who say 'our bones are dried up and our hope is lost'. Yahweh will open their graves and bring them to the land of Israel.\n\n"
          "The vision is mainly about the national restoration of Israel after exile. Later Jewish and Christian readers have also used it for the hope of resurrection. Be clear about the original meaning."),
        H("Shepherds, new heart and the new temple"),
        T("Chapter 34 condemns the shepherds (leaders) who fed themselves and not the flock; Yahweh will himself be the shepherd and set up one shepherd from David's line. "
          "Chapter 36 promises that Yahweh will give a new heart and put a new spirit within the people, taking away the heart of stone. "
          "Chapters 40 to 48 describe a visionary new temple, with a detailed plan and a river flowing from it; at the end the city is named 'Yahweh is there'. "
          "Priests and the glory of Yahweh return to the temple (43:1 to 5)."),
        EX("Model essay plan 1", intro="Explain Ezekiel's teaching on individual responsibility.", steps=[
            S("Context", text="The sour grapes proverb among the exiles: they felt punished for earlier sins."),
            S("Teaching", text="Each person is judged by their own actions (chapter 18); the wicked who repent will live."),
            S("Purpose", text="To end fatalism and give hope; to call the exiles to repentance."),
            S("Limits", text="The nation still shares guilt in other chapters; the idea is a shift of emphasis."),
        ]),
        EX("Model essay plan 2", intro="What is the meaning of the vision of the dry bones?", steps=[
            S("Setting", text="The exiles despair: 'our bones are dried up'."),
            S("Vision", text="Bones come together, receive flesh and breath (ruach) and live."),
            S("Original meaning", text="National restoration: Israel will be brought back from the exile by Yahweh's power."),
            S("Later reading", text="Some Jewish and Christian readers use it for resurrection hope, but the text itself speaks of the restoration of a nation."),
        ]),
        MISTAKE("Dating Ezekiel to Jerusalem", "Ezekiel prophesied among the exiles in Babylon, not in Jerusalem."),
        MISTAKE("Reading chapter 37 as only about the resurrection of the dead", "Yahweh explains that the bones are the house of Israel, so the primary meaning is national restoration."),
        QUIZ("What did the exiles mean by the proverb of the sour grapes?",
             ["That the vineyards of Judah were destroyed", "That they were suffering for the sins of earlier generations", "That Ezekiel was a false prophet", "That they should return to Egypt"], 1,
             "The proverb says that the parents' sin left the children suffering, a complaint of fatalism.",
             hint="Whose teeth are set on edge?",
             feedback=["The saying is about guilt, not farms.", "", "It is not about Ezekiel's authority.", "Egypt is not mentioned in the proverb."]),
        QUIZ("What does Yahweh explain the dry bones to be?",
             ["The soldiers of Babylon", "The whole house of Israel", "The priests of the Temple", "The kings of Judah"], 1,
             "Ezekiel 37:11 says that the bones are the whole house of Israel.",
             hint="Read the explanation in verse 11.",
             feedback=["Babylon's soldiers are not the subject.", "", "The priests are not mentioned here.", "The kings are not the subject."]),
        PQ("Explain the significance of Ezekiel's vision of the glory of Yahweh leaving the Temple. (structural question)",
           "The Temple was believed to be Yahweh's house and the guarantee of Jerusalem's safety. In chapters 8 to 11 Ezekiel sees idolatry in the Temple and then the glory of Yahweh leaving. "
           "It shows that Yahweh was free to leave, and that the destruction of the city was Yahweh's judgement and not his defeat by Babylon's gods. "
           "It also meant that Yahweh could be with the exiles in Babylon, as shown in the first vision, and could return in the future (chapter 43)."),
        PQ("What was Ezekiel's duty as a watchman?",
           "In chapters 3 and 33 Ezekiel is a watchman for Israel. He must warn the people when he hears a word of judgement from Yahweh. If he fails to warn the wicked, he is responsible for the consequences; if he warns and they ignore him, the guilt is theirs. "
           "The role means that the prophet's task is to speak faithfully, not to ensure that people listen, and that people have a chance to turn and live (33:11)."),
        PQ("Compare the messages of Jeremiah and Ezekiel.",
           "Both warned of the fall of Jerusalem and promised renewal through a new relationship with God: the new covenant in Jeremiah, and the new heart and spirit in Ezekiel (36:26 to 27). "
           "Jeremiah spoke in Judah and Ezekiel among the exiles. Jeremiah was a priest's son whose book shows personal struggle and the Confessions; "
           "Ezekiel, a priest in exile, focused on the Temple, the glory and the new temple, with dramatic visions and sign acts. Both used the sour grapes proverb in teaching personal responsibility."),
        SUM("Ezekiel, a priest among the exiles of 597 BC, was called about 593 BC by the river Chebar.",
            "His first vision showed that Yahweh's glory is not tied to the Temple.",
            "Sign acts, the watchman and the departure of the glory prepare for the fall of Jerusalem.",
            "Chapter 18 teaches individual responsibility and the possibility of repentance.",
            "The dry bones and the new temple promise the restoration of Israel under Yahweh."),
    ],
))

LESSONS.append(lesson(
    module=M2, topic="Deutero-Isaiah and the Suffering Servant",
    title="Deutero-Isaiah: comfort for the exiles and the Servant Songs",
    slug="rsu1-deutero-isaiah-servant",
    minutes=24,
    summary="Why scholars separate Isaiah 40 to 55 from earlier chapters, its message of comfort, one God and a new exodus, and the Servant Songs with the debate about who the Servant is.",
    objectives=[
        "Explain why most scholars date Isaiah 40 to 55 to the late exile and attribute it to an anonymous prophet",
        "Describe its themes: comfort, monotheism, creation, the new exodus and Cyrus",
        "Outline the four Servant Songs",
        "Evaluate the main identifications of the Servant, including the Christian use",
    ],
    key_concepts=["Deutero-Isaiah", "Exile", "Cyrus", "Monotheism", "New exodus", "Servant Songs", "Vicarious suffering"],
    blocks=[
        H("Introduction"),
        T("In the last lesson on Isaiah we used chapters that scholars link with Isaiah of Jerusalem in the eighth century BC. "
          "From chapter 40 the setting seems to change. The city of Jerusalem is already destroyed, the people are in exile, and the Persian king Cyrus is named. "
          "Most scholars therefore think that chapters 40 to 55 come from an unnamed prophet of the exile, about 550 to 539 BC, whom they call **Deutero-Isaiah** ('Second Isaiah'). "
          "Chapters 56 to 66 are usually assigned to later prophets of the return, sometimes called Trito-Isaiah.\n\n"
          "This is a scholarly theory and not a statement of faith. Some readers hold that the whole book is by Isaiah. In your exam answer, give the reasons for the theory and note that it is debated."),
        KEY("Why scholars separate chapters 40 to 55", "Four lines of argument.", cards=[
            ["Historical setting", "The audience is in exile, Jerusalem is in ruins, and Cyrus of Persia is named (44:28, 45:1), about 150 years after Isaiah of Jerusalem."],
            ["Style and vocabulary", "Long, flowing poems, in a different style from the shorter oracles of chapters 1 to 39."],
            ["Theology", "A stronger emphasis on creation, the uniqueness of Yahweh and comfort instead of judgement."],
            ["Authors named?", "No name is given. The theory is an inference from the text, and some scholars still defend the unity of the book."],
        ]),
        H("The message of comfort"),
        T("Chapter 40 begins: 'Comfort, comfort my people.' The prophet announces that Israel's penalty has been paid and a highway will be made in the wilderness for Yahweh's return. "
          "The grass withers and flowers fade but the word of God stands for ever. The exiles fear that Yahweh has forgotten them (40:27). The prophet answers that Yahweh does not grow faint or weary and gives strength to those who wait for him."),
        H("One God, creator of all"),
        D("The belief that only one God exists. Deutero-Isaiah is often counted as the clearest expression of this in the Old Testament: 'I am Yahweh, and there is no other' (45:5). "
          "He ridicules the making of idols (44:9 to 20) and says Yahweh is the creator of the ends of the earth and the Lord of history. "
          "Scholars debate whether earlier writers already held this view; check your textbook.", title="Monotheism"),
        T("Why did this matter? In exile, the Babylonian gods seemed to have won. Deutero-Isaiah says the fall of Jerusalem was not a defeat of Yahweh, but the act of the one God, who can now bring his people home. "
          "Creation language is used to support this: the one who made the world can renew his people."),
        H("A new exodus and Cyrus"),
        T("The prophet describes the return in the language of the Exodus: a way through the wilderness, water in the desert, and Yahweh as a shepherd leading his people. "
          "Surprisingly, Cyrus, a Persian king, is called Yahweh's shepherd and his 'anointed' (45:1), the one who will let the exiles go. "
          "Cyrus conquered Babylon in 539 BC, and an edict allowed exiles to return (Ezra 1; check your textbook for the debate about the wording of the edict). "
          "The idea that Yahweh used a foreign ruler for his plan stretches earlier thinking."),
        H("The Servant Songs"),
        D("Four poems about Yahweh's 'servant' in chapters 42, 49, 50 and 52 to 53. Bernhard Duhm, in 1892, was the scholar who singled them out as separate poems. Not all scholars agree that they form a distinct group.", title="Servant Songs"),
        KEY("The four songs", "Know the content of each.", cards=[
            ["Song 1 (42:1 to 4)", "Yahweh's chosen servant, with his spirit, will bring justice to the nations, gently, not breaking a bruised reed."],
            ["Song 2 (49:1 to 6)", "The servant speaks: called from the womb, he was first told he would restore Israel, and now is made a light to the nations so that salvation reaches the ends of the earth."],
            ["Song 3 (50:4 to 9)", "The servant is a disciple who listens, speaks to the weary and accepts insults and blows without turning back. He trusts Yahweh to help him."],
            ["Song 4 (52:13 to 53:12)", "The servant is exalted, but first disfigured, despised and rejected. He bears our griefs, is wounded for our transgressions, dies as one counted with sinners, and the many are healed by his wounds."],
        ]),
        H("Who is the Servant?"),
        KEY("Main identifications", "Give at least two and evaluate them.", cards=[
            ["Israel as a whole", "Isaiah 49:3 says 'You are my servant, Israel'. The suffering of the exile is seen as vicarious (on behalf of others) for the nations. Weakness: 49:5 appears to distinguish the servant from Israel."],
            ["A faithful remnant", "A righteous group within Israel suffers and serves the nation."],
            ["An individual of the time", "Suggestions include the prophet himself, Moses, Jehoiachin or Cyrus. The evidence is slight and there is no agreement."],
            ["A future individual", "Christians have understood the fourth song as fulfilled in Jesus, who suffered and died for others. The New Testament refers to Isaiah 53 several times (for example Acts 8:32 to 35 and 1 Peter 2:22 to 25). Historians ask what the passage meant in its own time, while believers add the Christian reading."],
        ]),
        T("A central idea in the fourth song is **vicarious suffering**: the servant suffers not for his own sin but for the sins of others. "
          "The speakers (probably the nations and kings, 52:15) realise that they had thought him punished by God, but he was bearing their guilt. "
          "This is a striking idea in a time when most people thought suffering was a punishment for one's own sins; we meet that question again in Job."),
        TIP("Exam link: Deutero-Isaiah and the Servant Songs belong to the Old Testament prophets and may be set in Paper 2 (essays) or Paper 1 (key terms). The Board's 2023 report asks for explanation and not only retelling. "
            "State clearly which view of the Servant you are describing and keep a balanced tone. Check which OT sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="Discuss the identity of the Suffering Servant.", steps=[
            S("Introduction", text="Define the Servant Songs (Duhm) and the debate."),
            S("Israel", text="49:3 names Israel; Israel suffered in exile. Problem: the servant in 49:5 has a mission to Israel."),
            S("An individual", text="The prophet, Moses and others are proposed, but the evidence is thin."),
            S("Christian reading", text="The New Testament applies the fourth song to Jesus. Historical study and Christian faith ask different questions."),
            S("Judgement", text="No single answer satisfies all the passages; the figure may blend a community and an individual."),
        ]),
        EX("Model essay plan 2", intro="Explain the main teachings of Deutero-Isaiah.", steps=[
            S("Comfort", text="The exile is nearly over (40:1 to 2)."),
            S("One God", text="Yahweh is creator and there is no other; idols are nothing."),
            S("New exodus", text="Return through the desert, with Cyrus as Yahweh's instrument."),
            S("Servant", text="Yahweh's servant brings justice and suffers for others."),
        ]),
        MISTAKE("Saying that 'Isaiah' wrote chapters 40 to 55 without comment", "State that the book is traditionally attributed to Isaiah, but most scholars date chapters 40 to 55 to the exile and an anonymous prophet."),
        MISTAKE("Presenting the Christian interpretation as the only one", "Note the original setting and the Jewish and historical readings, and then explain how the New Testament uses the song."),
        QUIZ("Which Persian king is named in Deutero-Isaiah as Yahweh's anointed?",
             ["Nebuchadnezzar", "Cyrus", "Darius", "Sennacherib"], 1,
             "Isaiah 44:28 and 45:1 name Cyrus.",
             hint="He conquered Babylon in 539 BC.",
             feedback=["Nebuchadnezzar was a Babylonian king.", "", "Darius was a later Persian king.", "Sennacherib was Assyrian."]),
        QUIZ("Which of these is an argument for dating Isaiah 40 to 55 to the exile?",
             ["It is written in the first person by Isaiah", "It addresses exiles and names Cyrus", "It mentions the Temple Sermon", "It describes the call of Isaiah in the year Uzziah died"], 1,
             "The audience and the named Persian king point to the late exile, long after the eighth century.",
             hint="Think about setting.",
             feedback=["The chapters do not claim to be Isaiah's speech about his own call.", "", "The Temple Sermon is in Jeremiah.", "That is in chapter 6."]),
        PQ("What is vicarious suffering, and how does the fourth Servant Song express it? (structural question)",
           "Vicarious suffering is suffering endured on behalf of others. In Isaiah 52:13 to 53:12 the servant is despised, wounded and killed, but the speakers realise that he bore their griefs and was wounded for their transgressions, "
           "and that by his wounds the many are healed. The poem presents a righteous sufferer whose suffering has a saving effect, which was unusual because suffering was often taken as punishment for one's own sin."),
        PQ("Explain the theological importance of Cyrus in Deutero-Isaiah.",
           "Cyrus is called Yahweh's shepherd and anointed (44:28 and 45:1). A foreign king who did not know Yahweh is used for Yahweh's purposes, showing that Yahweh is the Lord of history and not tied to Israel's borders. "
           "It also gave the exiles hope that the empire could end and that they could go home. The language broadens ideas of the 'anointed one', which earlier referred to Israel's kings."),
        PQ("To what extent was the Suffering Servant Israel?",
           "For: the second song says 'You are my servant, Israel' (49:3), and Israel had suffered in exile. The nation's mission as a 'light to the nations' fits the Servant's task. "
           "Against: in 49:5 the servant has a task towards Israel, and in the fourth song the servant is described as an individual who dies innocently. Some scholars argue that the Servant is a person, others that he is a corporate figure who may include both. "
           "A balanced answer concludes that Israel is the best-supported single identification, but that the evidence does not settle the matter."),
        SUM("Most scholars assign Isaiah 40 to 55 to an anonymous prophet of the exile (about 550 to 539 BC), called Deutero-Isaiah.",
            "His message is comfort, one God as creator, and a new exodus.",
            "Cyrus of Persia is described as Yahweh's anointed.",
            "The four Servant Songs describe a servant who brings justice and, in the fourth, suffers for others.",
            "The Servant has been identified as Israel, a remnant, an individual or, for Christians, Jesus; no single view is universally accepted."),
    ],
))

LESSONS.append(lesson(
    module=M2, topic="Job and the problem of theodicy",
    title="Job and the problem of theodicy: why do the innocent suffer?",
    slug="rsu1-job-theodicy",
    minutes=25,
    summary="The structure of Job, the retribution theology of the friends, Job's protest, God's answer from the whirlwind, and the responses to suffering in Job and the lament psalms.",
    objectives=[
        "Define theodicy and explain the traditional doctrine of retribution",
        "Outline the structure and main speakers of Job",
        "Explain the arguments of the friends and of Job",
        "Evaluate God's answer and compare Job with Psalms 37, 73 and 88",
    ],
    key_concepts=["Theodicy", "Retribution", "Wisdom literature", "Satan (the accuser)", "Lament", "Divine speeches"],
    blocks=[
        H("Introduction"),
        T("Why does a good person suffer? Most societies ask this question. In Cameroon families may ask it after illness, a death or a failed harvest; in the Old Testament the question is put with unusual honesty. "
          "The book of Job belongs to the **wisdom literature** with Proverbs and Ecclesiastes. It tells of a righteous man who loses everything and argues with God and with his friends."),
        D("A word made from the Greek for 'God' and 'justice'. It means the attempt to defend the goodness and justice of God in the face of evil and suffering. "
          "The word was coined by the philosopher Leibniz in the early eighteenth century, but the problem is much older.", title="Theodicy"),
        D("The view, strong in much of the Old Testament, especially Deuteronomy and Proverbs, that God rewards the righteous with prosperity and punishes the wicked with misfortune. "
          "If this rule were exact, every sufferer would be a sinner.", title="Retribution (doctrine of rewards and punishments)"),
        IMG("alrsu1-job-structure.svg", alt="Diagram showing the structure of the book of Job: prologue, three cycles of dialogue, Job's final speech, Elihu, God's speeches, Job's reply and the epilogue.", caption="Figure 1. The structure of Job."),
        H("Structure and story"),
        KEY("Outline of the book", "Know the order of the sections.", cards=[
            ["Prologue (chapters 1 and 2)", "Job, a blameless man in the land of Uz, is rich and has a large family. In the heavenly court 'the satan' (the accuser, not yet the devil of later thought) challenges whether Job fears God for nothing. Yahweh allows testing. Job loses property, children and health but does not curse God."],
            ["Dialogues (3 to 27)", "Three friends, Eliphaz, Bildad and Zophar, come to comfort him and then argue with him in three cycles. Job answers each."],
            ["Job's final words (29 to 31)", "Job recalls his former life, describes his suffering and swears an oath of innocence."],
            ["Elihu (32 to 37)", "A young man claims the friends failed and says suffering can teach. Many scholars think these chapters were added later."],
            ["God's answer (38 to 42:6)", "Yahweh speaks out of a whirlwind. Job responds."],
            ["Epilogue (42:7 to 17)", "Yahweh says the friends have not spoken rightly of him, as Job has. Job's fortunes are restored."],
        ]),
        H("The friends: retribution theology"),
        T("The friends are not villains. They sit silent with Job for seven days. But once they speak they defend the traditional doctrine. Eliphaz says that no innocent person ever perishes (4:7). "
          "Bildad says that God does not pervert justice (8:3) and suggests that Job's children died because of their sin. Zophar says Job deserves less than he receives (11:6). "
          "The friends move from suggestion to accusation: if Job suffers, he must have sinned and he should repent. They protect their view of God by blaming the sufferer."),
        H("Job's protest"),
        T("Job refuses the explanation. He knows he is not guilty. He says God treats the righteous and wicked alike (9:22), asks why the wicked prosper (21:7), and wants to bring his case before God as in a law court (13:3 and 23:3 to 7). "
          "At the same time, he longs for someone to speak for him, an arbiter or a 'redeemer' (9:33, 16:19, 19:25; the translation and meaning of 19:25 to 27 are disputed, so check your textbook). "
          "Job does not give up faith in God; he insists that God must answer for his actions."),
        H("The voice from the whirlwind"),
        T("In chapters 38 to 41 Yahweh speaks. He does not explain Job's suffering or mention the heavenly wager. He asks Job a series of questions: where was Job when the earth's foundations were laid? "
          "Can he command the dawn, the rain, the stars? Who feeds the lion, the raven, the wild ox? He describes two huge creatures, Behemoth and Leviathan. "
          "Job answers that he spoke of things he did not understand, and that now his eye sees God; he repents 'in dust and ashes' (42:1 to 6; the exact meaning of the verb 'repent' is debated)."),
        KEY("How scholars read God's answer", "None is certain; weigh them.", cards=[
            ["Divine mystery", "God's wisdom is beyond human grasp; humans cannot judge the order of creation."],
            ["God's care beyond humans", "The questions show a world with wild and untamed creatures that God loves, and in which humans are not the centre."],
            ["Encounter over explanation", "What matters is that God appears and speaks to Job: the relationship is restored, even if the question 'why?' is not answered."],
            ["Criticism", "Some readers feel that the speeches evade the moral question. Others say the book exposes the limits of the retribution doctrine."],
        ]),
        T("In the epilogue God says that the friends did not speak rightly of him but Job did (42:7). Job has to pray for the friends. "
          "This shows that the book rejects the simple rule that the sufferer is a sinner. The restoration of Job's wealth is sometimes seen as a return to the old pattern, and some readers think it weakens the book. Check which view your textbook gives."),
        H("Psalms of suffering"),
        T("The Psalms also face the problem. Psalm 37 gives a traditional answer: do not envy the wicked, for they will wither, and the righteous will inherit the land. "
          "Psalm 73 is more honest: the psalmist almost lost faith because the wicked prosper. He found an answer when he entered the sanctuary and saw their end, and he concluded that to be near God is his good. "
          "Psalm 88 has no answer: it is a lament that ends in darkness. Psalm 22 begins with the cry 'My God, my God, why have you forsaken me?' but ends in praise. "
          "Lament is a legitimate part of worship in the Old Testament."),
        TIP("Exam link: Job and the problem of theodicy may be set among the Old Testament topics in Paper 2 (essays) and linked to Philosophy of Religion (Paper 3). The Board's report names Philosophy of Religion and Ethics and Morality sections, including questions on evil and suffering. "
            "Use Job as an example, and check which sections your school teaches.", title="Exam link"),
        EX("Model essay plan 1", intro="Examine the arguments of Job's friends and Job's response.", steps=[
            S("Friends", text="Retribution doctrine: suffering follows sin; Job must repent (Eliphaz 4:7, Bildad 8:3)."),
            S("Job's reply", text="He knows he is innocent; the wicked prosper; God appears unjust; he wants a hearing."),
            S("God's verdict", text="In the epilogue the friends have not spoken rightly."),
            S("Evaluation", text="The book rejects a simple rule but does not give a full explanation."),
        ]),
        EX("Model essay plan 2", intro="'God's answer to Job does not solve the problem of suffering.' Discuss.", steps=[
            S("For", text="God never explains why Job suffers or mentions the wager; Job's question 'why?' remains."),
            S("Against", text="The speeches reframe the question: God's wisdom is wider than human views, and meeting God matters more than an explanation."),
            S("Other texts", text="Psalm 73 finds comfort in God's presence; Psalm 88 gives no answer."),
            S("Judgement", text="It is not a complete theodicy, but it does rule out the claim that all suffering is deserved."),
        ]),
        MISTAKE("Calling 'the satan' the devil", "In Job the Hebrew word means an accuser in God's court. The later idea of Satan as God's enemy is a development. Say this."),
        MISTAKE("Saying that Job's friends were wicked", "They were sincere and held the traditional view. Their error was applying it as a rule to Job's case."),
        QUIZ("What is theodicy?",
             ["A study of the Temple", "The defence of God's justice in the face of evil", "The order of the Psalms", "A prophecy about the return from exile"], 1,
             "Theodicy asks how a good and just God can allow suffering.",
             hint="It comes from Greek words for 'God' and 'justice'.",
             feedback=["It is not about architecture.", "", "It is not about the arrangement of books.", "It is not a prophecy."]),
        QUIZ("Who, according to the epilogue of Job, spoke rightly of God?",
             ["Eliphaz", "Job", "Elihu", "Zophar"], 1,
             "Yahweh says that the friends did not speak rightly of him as Job did (42:7).",
             hint="It is the sufferer.",
             feedback=["Eliphaz is one of the friends criticised.", "", "Elihu is not mentioned in the epilogue.", "Zophar is one of the friends criticised."]),
        PQ("Explain the doctrine of retribution and how the book of Job challenges it. (structural question)",
           "Retribution is the belief that God rewards the righteous with prosperity and punishes the wicked with disaster. The friends defend it and infer that Job is a sinner. "
           "The prologue tells readers that Job is blameless, so the doctrine fails for Job. Job complains that the wicked prosper and the innocent suffer. "
           "At the end God condemns the friends' speech, showing that the book rejects a mechanical link between sin and suffering."),
        PQ("What do the divine speeches (chapters 38 to 41) say to Job?",
           "God does not give reasons for Job's suffering. He asks Job about creation: its foundations, the sea, the stars, the animals. The questions show the limits of human knowledge and the wide scope of God's care. "
           "Job concedes that he spoke without understanding and says he now sees God (42:1 to 6). Interpreters differ: some say the speeches show divine mystery, some that they show the relationship matters more than an explanation, others that they avoid the moral question."),
        PQ("Compare the treatment of suffering in Job and in Psalm 73.",
           "Both face the problem that the wicked prosper while the righteous suffer. Job argues with God and his friends and is answered by an encounter with God in a whirlwind. "
           "The psalmist almost loses faith, then enters the sanctuary and understands that the prosperity of the wicked is temporary and that nearness to God is the real good. "
           "Both accept that the traditional rule fails in individual cases, and both find the answer in relationship with God, but Job's book is longer and more radical in its protest."),
        SUM("Theodicy is the defence of God's goodness in the face of evil; retribution is the traditional rule of reward and punishment.",
            "Job has a prose prologue and epilogue and a poetic centre of dialogues, Job's final speech, Elihu and God's speeches.",
            "The friends defend retribution and accuse Job; Job insists on his innocence and demands an answer.",
            "God's answer stresses wisdom, creation and presence rather than an explanation; the epilogue says the friends spoke wrongly.",
            "Psalms 37, 73, 88 and 22 show other responses: confidence, struggle, darkness and lament leading to praise."),
    ],
))

LESSONS.append(lesson(
    module=M3, topic="The Acts of the Apostles",
    title="The Acts of the Apostles: author, aims and historical reliability",
    slug="rsu1-acts-reliability",
    minutes=24,
    summary="Who wrote Acts and why, its structure and themes, and how scholars weigh its historical reliability using external evidence, Paul's own letters and the speeches.",
    objectives=[
        "Outline the structure and main themes of Acts",
        "Discuss the authorship, date and purposes of Acts",
        "Evaluate the evidence for and against its historical reliability",
        "Explain the importance of Pentecost, the persecution of the Jerusalem church and the Council of Jerusalem",
    ],
    key_concepts=["Luke-Acts", "Theophilus", "We passages", "Speeches in Acts", "Historical reliability", "Universalism", "Council of Jerusalem"],
    blocks=[
        H("Introduction"),
        T("Acts is the only surviving early account of the first generation of Christians. It is the second volume of a two-volume work by the author of the Gospel of Luke: both are addressed to Theophilus (Luke 1:3 and Acts 1:1). "
          "Acts tells how the message of Jesus spread from Jerusalem to Rome, through Peter, Stephen, Philip and above all Paul.\n\n"
          "A key question for A Level students is how far Acts can be trusted as history. Examiners want you to weigh evidence, not simply to defend or attack the book."),
        KEY("Outline of Acts", "Acts 1:8 gives a programme: 'in Jerusalem, in all Judea and Samaria, and to the ends of the earth'.", cards=[
            ["Chapters 1 to 7: Jerusalem", "Ascension, Pentecost (chapter 2), life of the early church, persecution, the death of Stephen."],
            ["Chapters 8 to 12: Judea, Samaria and beyond", "Philip in Samaria, the conversion of Saul (chapter 9), Peter and Cornelius (chapter 10), the church at Antioch."],
            ["Chapters 13 to 28: to the ends of the earth", "Paul's three journeys, the Council of Jerusalem (chapter 15), arrest in Jerusalem, trials and the journey to Rome."],
        ]),
        H("Author and date"),
        T("The book does not name its author. Church tradition from the second century says he was Luke, the physician and companion of Paul (Colossians 4:14, Philemon 24). "
          "The evidence for this is the shared prologue with the Gospel and the 'we' passages: in parts of Acts (16:10 to 17, 20:5 to 21:18, 27:1 to 28:16) the narrative changes from 'they' to 'we', as if the writer was present. "
          "Scholars argue about this. Some accept that the writer was a travelling companion of Paul. Others say 'we' is a literary device or the use of a source. Check your textbook."),
        T("The date is uncertain too. Acts ends with Paul under house arrest in Rome, about AD 60 to 62, without mentioning his trial or death. Some scholars say this shows it was written about then. "
          "Others date it to AD 80 to 90, because Luke's Gospel uses Mark, written about AD 65 to 70, and because the book does not clearly use Paul's letters. The ending may be explained by Luke's aim: the message reaches Rome unhindered."),
        H("Aims of Acts"),
        KEY("Likely purposes", "Scholars suggest several, and they are not exclusive.", cards=[
            ["Historical record", "To tell Theophilus the history of the early church (Luke 1:1 to 4)."],
            ["Theological: the Holy Spirit", "The Spirit guides every step: Pentecost, Samaria, Cornelius, Antioch, the missions."],
            ["Universal mission", "The gospel is for Jews and Gentiles. The church moves outward from Jerusalem to Rome."],
            ["Political apologetic", "Roman officials often find the Christians innocent (Gallio, Felix, Festus, Agrippa). Some scholars think Luke wanted to show that Christianity was not a threat to Rome."],
            ["Church unity", "Peter and Paul preach the same gospel; disputes (such as chapter 15) are settled by agreement."],
        ]),
        H("The speeches"),
        T("About a quarter of Acts consists of speeches, by Peter, Stephen, Paul and others. The writer was in no position to record these word for word. "
          "Ancient historians, such as Thucydides, said they tried to give what a speaker would say in the situation while keeping to the general sense. Scholars debate whether Luke's speeches follow the real content or are mostly his own composition. "
          "Many see common patterns: for example, the early sermons repeat a simple outline (Jesus's ministry, death, resurrection, a call to repent), which may reflect early preaching."),
        H("Evidence for reliability"),
        KEY("Points supporting Acts", "These are the commonly cited arguments.", cards=[
            ["Local and official knowledge", "Acts uses correct titles for officials in various places, such as the 'politarchs' at Thessalonica (an inscription confirms the word) and a proconsul in Cyprus and in Achaia. Sir William Ramsay argued strongly for such accuracy."],
            ["Gallio", "An inscription from Delphi mentions the proconsul Gallio in Achaia, which helps date Paul's stay in Corinth (Acts 18:12) to about AD 51 to 52. Check your textbook."],
            ["Travel and sea voyage", "The details of the voyage to Rome (chapter 27) are widely thought to show first-hand knowledge of ancient sailing."],
            ["Agreement with Paul's letters", "Both give the picture of Paul as a travelling missionary who worked in cities, such as Corinth, Philippi and Thessalonica, and met opposition."],
        ]),
        KEY("Points that raise questions", "Do not only defend Acts.", cards=[
            ["Differences from Paul's letters", "Paul, in Galatians 1 and 2, mentions fewer visits to Jerusalem than Acts and does not mention the decree of Acts 15 in his letters. Scholars discuss whether the two accounts can be harmonised."],
            ["Portrait of Paul", "Acts presents Paul as a gifted speaker who keeps the law; his letters show him sometimes less impressive in speech (2 Corinthians 10:10) and more critical of the law. His letters do not mention that he was a Roman citizen."],
            ["Selective narrative", "Acts leaves out much (for example the founding of the church in Rome, Paul's death). Theology shapes what is told."],
            ["Tendency (the Tübingen school)", "F. C. Baur in the nineteenth century argued that Acts smoothed over a conflict between Peter and Paul. Most scholars today think this was overstated, though differences are acknowledged."],
        ]),
        T("A fair conclusion is that Acts is a work of history with a purpose, like other ancient histories. It is reliable on many details of setting and travel, while its selection and the shaping of speeches and conflicts reflect Luke's aims. "
          "Scholars hold different views on how much weight to give it when it differs from Paul."),
        TIP("Exam link: the Board's 2023 report names the Early Church as reflected in Acts and 1 Corinthians (section 2.3 of Paper 3, structural questions; four from a section of choice). "
            "It records questions on Pentecost, the leadership of Peter and Paul, the Jerusalem Council and the persecution at Jerusalem as a blessing to the church's growth. Use these as models for your own revision.", title="Exam link"),
        H("Three key events"),
        KEY("Pentecost, persecution, Jerusalem Council", "The Board's report names these as exam areas.", cards=[
            ["Pentecost (chapter 2)", "The Spirit comes on the disciples at the feast of Pentecost with wind, fire and speaking in other languages. Peter preaches and about three thousand are added. It marks the birth of the church's public mission."],
            ["Persecution (chapters 7 and 8)", "After Stephen's death, believers (other than the apostles) scattered through Judea and Samaria, taking the message with them. The persecution thus helped to spread it."],
            ["Council of Jerusalem (chapter 15)", "The question was whether Gentile converts must be circumcised and keep the law of Moses. After debate, led by Peter and James with Paul and Barnabas giving witness, the council did not require circumcision and asked Gentiles to keep a few rules (abstain from food offered to idols, blood, strangled animals and sexual immorality; manuscripts vary). It opened the way for the Gentile mission."],
        ]),
        EX("Model essay plan 1", intro="How reliable is Acts as a historical source?", steps=[
            S("Introduction", text="Acts is Luke's second volume. Define reliability and note the purpose of the author."),
            S("For", text="Titles of officials, Gallio inscription, the voyage, the 'we' passages."),
            S("Against", text="Differences with Galatians, shaped speeches, gaps, theological aims, doubts about the Roman citizenship detail."),
            S("Judgement", text="Reliable in setting and general outline, with shaped detail. Use with Paul's letters."),
        ]),
        EX("Model essay plan 2", intro="Explain the importance of the Council of Jerusalem.", steps=[
            S("Problem", text="Must Gentiles be circumcised? The church risked splitting into Jewish and Gentile groups."),
            S("Debate and decision", text="Peter and James speak; Paul and Barnabas report; no circumcision, a few rules."),
            S("Effects", text="It freed the Gentile mission; the missionary journeys follow."),
            S("Comment", text="Galatians 2 reports a meeting in Jerusalem and scholars debate whether it is the same event."),
        ]),
        MISTAKE("Treating Luke's authorship as proved", "Say that church tradition and the 'we' passages point to Luke but that scholars debate it."),
        MISTAKE("Listing events without evaluation", "A question on reliability needs evidence for and against and a judgement."),
        QUIZ("What does Acts 1:8 provide?",
             ["The names of the twelve apostles", "A programme for the spread from Jerusalem to the ends of the earth", "The date of Pentecost", "Rules for the Gentile converts"], 1,
             "The verse is often treated as the outline of the book.",
             hint="Think of the places named in the verse.",
             feedback=["The names are in Acts 1:13.", "", "Pentecost is dated in chapter 2.", "The rules are in Acts 15."]),
        QUIZ("Which feature of Acts is mostly cited as evidence of first-hand knowledge?",
             ["The speeches word for word", "The 'we' passages and the detail of the sea voyage", "The account of the Last Supper", "The genealogy of Jesus"], 1,
             "Many scholars see the voyage detail and the 'we' sections as signs that the author, or a source, was present.",
             hint="The narrative switches from 'they' to 'we'.",
             feedback=["The speeches are the most debated part.", "", "That belongs to the Gospels.", "The genealogy is in Luke's Gospel."]),
        PQ("Explain how the persecution of the Jerusalem church helped the growth of Christianity. (structural question)",
           "After Stephen's death a great persecution began and the believers, apart from the apostles, were scattered through Judea and Samaria (8:1). "
           "As they moved they preached the message wherever they went. Philip took it to Samaria, and others went to Phoenicia, Cyprus and Antioch (11:19). "
           "The church that had been concentrated in Jerusalem now became a movement with new centres, and Antioch became the base for Paul's work. The suffering therefore served the mission in Acts 1:8."),
        PQ("What were the results of the Council of Jerusalem?",
           "The council decided that Gentile converts did not need to be circumcised or keep the whole law of Moses to be saved. They were asked to avoid food offered to idols, blood, meat of strangled animals and sexual immorality (15:20 and 15:29). "
           "A letter was sent to the churches at Antioch, Syria and Cilicia. The decision protected the unity of the church and allowed the Gentile mission to continue, as in Paul's journeys."),
        PQ("Compare the leadership of Peter and Paul in Acts.",
           "Peter leads in the early chapters: he preaches at Pentecost, heals, speaks before the council and opens the door to the Gentiles in the house of Cornelius. "
           "Paul becomes the leading figure from chapter 13: he starts new churches among Gentiles, speaks in synagogues and before governors, and writes letters. "
           "Acts shows them in agreement: Peter supports the Gentile mission at the council of Jerusalem (15:7 to 11). Galatians 2:11 to 14 shows a disagreement between them in Antioch, which Acts does not report."),
        SUM("Acts is the second volume of Luke-Acts, addressed to Theophilus, and tells the spread of the church from Jerusalem to Rome.",
            "Tradition names Luke as the author; the 'we' passages are debated; the date lies between about AD 62 and 90.",
            "Its aims include history, the work of the Spirit, the universal mission and the innocence of Christians before Rome.",
            "Arguments for reliability: official titles, the Gallio inscription, the voyage; against: differences from Paul, shaped speeches, gaps.",
            "Pentecost, the persecution and the Jerusalem Council are key events for the exam."),
    ],
))

LESSONS.append(lesson(
    module=M3, topic="Paul's missionary strategy",
    title="Paul's missionary strategy: cities, synagogues, teams and letters",
    slug="rsu1-pauls-missionary-strategy",
    minutes=23,
    summary="Paul's three journeys and voyage to Rome, and the methods behind them: urban centres, the synagogue first, Gentile adaptation, co-workers, self-support, house churches, letters and the collection.",
    objectives=[
        "Outline Paul's three missionary journeys and the voyage to Rome",
        "Identify the main features of Paul's missionary strategy",
        "Explain how he adapted his message to Jewish and Gentile audiences",
        "Evaluate how far Acts and Paul's letters show a planned strategy",
    ],
    key_concepts=["Missionary journeys", "Synagogue first", "Gentile mission", "Co-workers", "Self-support", "House churches", "Collection"],
    blocks=[
        H("Introduction"),
        T("Paul (also called Saul) was a Pharisee from Tarsus, a Roman citizen according to Acts, who persecuted the church until the risen Jesus appeared to him on the road to Damascus. "
          "He then became the leading missionary to the Gentiles (non-Jews). Within about twenty years he had helped found churches across Asia Minor and Greece.\n\n"
          "Was this the result of a plan? Scholars disagree. Some say Paul followed a deliberate strategy; others say he responded to opportunities and opposition. "
          "This lesson describes the pattern that can be seen in Acts and in his letters, and asks you to evaluate it."),
        IMG("alrsu1-paul-journeys.svg", alt="Schematic route map of Paul's three missionary journeys and the voyage to Rome, showing the order of the main cities.", caption="Figure 1. Schematic order of Paul's journeys (not to scale; dates approximate)."),
        H("The journeys at a glance"),
        KEY("Journeys in Acts", "Dates are approximate; check your textbook.", cards=[
            ["First journey (Acts 13 and 14, about AD 46 to 48)", "With Barnabas and John Mark from Antioch in Syria to Cyprus, then Pisidian Antioch, Iconium, Lystra and Derbe in Asia Minor and back. Many Gentiles believe; Jews oppose."],
            ["Jerusalem Council (Acts 15, about AD 49)", "The decision on circumcision of Gentiles."],
            ["Second journey (Acts 15:36 to 18:22, about AD 49 to 52)", "With Silas, later Timothy. Through Asia Minor to Troas, then Philippi, Thessalonica, Berea, Athens and Corinth (about eighteen months)."],
            ["Third journey (Acts 18:23 to 21:17, about AD 52 to 57)", "Based at Ephesus for two to three years. Then Macedonia and Greece, collecting money for Jerusalem."],
            ["Arrest and voyage to Rome (Acts 21 to 28)", "Arrest in Jerusalem, imprisonment in Caesarea, appeal to Caesar, shipwreck on Malta and arrival in Rome."],
        ]),
        H("Features of his strategy"),
        T("**Cities.** Paul worked in important towns along Roman roads and sea routes: Antioch, Ephesus, Corinth, Philippi, Thessalonica. These were centres of trade and communication, so the message could spread from them into the surrounding region. "
          "Romans had built roads and kept order, and Greek was widely spoken."),
        T("**The synagogue first.** In many cities Acts shows Paul going first to the synagogue (13:5, 14:1, 17:2, 18:4). There he found Jews and 'God-fearers' (Gentiles attracted to Judaism) who knew the scriptures. "
          "Romans 1:16 says the gospel is 'to the Jew first and also to the Greek'. When opposed, he turned to Gentiles, though Acts does not suggest that he gave up on Jewish hearers."),
        T("**Teams of co-workers.** Paul rarely worked alone. Barnabas, Silas, Timothy, Titus, Luke, Priscilla and Aquila, Apollos and many others are named. "
          "The team shared the work of teaching, travelling and caring for the new churches. Women such as Lydia in Philippi (Acts 16) and Phoebe, who carried the letter to Rome (Romans 16:1), played roles."),
        T("**Self-support.** Paul worked as a tentmaker or leatherworker, with Priscilla and Aquila in Corinth (Acts 18:3). In 1 Corinthians 9 and 1 Thessalonians 2 he explains that he did not burden the new churches with his upkeep, though he defends the right of workers to be supported. "
          "He did accept gifts, such as those from Philippi."),
        T("**House churches.** Churches met in homes (Romans 16:5, 1 Corinthians 16:19, Philemon 2). A home could hold a small group, and heads of households such as Lydia, Crispus or Gaius could host and lead."),
        T("**Care after founding.** Paul revisited churches, sent Timothy and Titus and wrote letters. According to Acts 14:23 he and Barnabas appointed elders. He treated the letter as a way to be present while absent."),
        T("**The collection.** Paul organised a gift from Gentile churches for the poor among believers at Jerusalem (1 Corinthians 16, 2 Corinthians 8 and 9, Romans 15). "
          "It helped the poor, and it was a sign of unity between Gentile and Jewish believers."),
        H("Adapting the message"),
        KEY("Two audiences", "Compare Pisidian Antioch with Athens.", cards=[
            ["To Jews and God-fearers (Acts 13:16 to 41)", "Paul retells Israel's story from the Exodus to David and shows Jesus as the promised saviour, using the scriptures and the resurrection."],
            ["To Gentile philosophers (Acts 17:22 to 31)", "At the Areopagus in Athens he begins with an altar 'to an unknown god', quotes Greek poets and speaks of one creator God, a coming judgement and the resurrection. Few responded."],
            ["To a rural audience (Acts 14:15 to 17)", "At Lystra he speaks of the God who gives rain and harvests, because the crowd took him for a god."],
        ]),
        T("Paul's own words in 1 Corinthians 9:19 to 23 say that he became 'all things to all people' to win some. It is a principle of adapting the manner of presentation without changing the message of Christ crucified and raised."),
        TIP("Exam link: the Board's 2023 report names the Early Church as reflected in Acts and 1 Corinthians (Paper 3, section 2.3), with questions on the Jerusalem Council and the missionary journeys as evidence of its effects. "
            "Use the order of the journeys and a few named features of Paul's method.", title="Exam link"),
        H("Evaluation: plan or response?"),
        T("In favour of a plan: he chose cities, a pattern of synagogue and then Gentiles, teams and follow-up. Romans 15:19 to 24 shows him thinking of Spain and of Rome as a base. "
          "Against: Acts shows changes made by the Spirit (16:6 to 10), by opposition and by arrest. Paul says he preached where Christ was not already named (Romans 15:20). "
          "A fair conclusion is that Paul had clear aims and methods but remained flexible. Dates and exact routes vary between scholars, and the 'South Galatia' and 'North Galatia' debate concerns where the Galatian churches were. Check your textbook."),
        EX("Model essay plan 1", intro="Describe Paul's missionary methods.", steps=[
            S("Cities", text="Roman roads and trade centres: Corinth, Ephesus, Philippi."),
            S("Synagogue then Gentiles", text="Acts 13 to 19; Romans 1:16; God-fearers."),
            S("Teams and self-support", text="Barnabas, Silas, Timothy, Priscilla and Aquila; tentmaking in Corinth."),
            S("Follow-up", text="Letters, return visits, elders, house churches, the collection."),
        ]),
        EX("Model essay plan 2", intro="Compare Paul's speeches at Pisidian Antioch and at Athens.", steps=[
            S("Audience", text="Jews and God-fearers in a synagogue versus Greek philosophers on the Areopagus."),
            S("Content", text="Antioch: Israel's history and the scriptures. Athens: creation, an unknown god, Greek poets."),
            S("Common ground", text="Both end with the resurrection and a call to respond."),
            S("Result", text="Many believed in Antioch though opposition grew; in Athens a few believed, including Dionysius and Damaris."),
        ]),
        MISTAKE("Giving journeys without cities in order", "A list of places in the correct order is the simplest way to show knowledge. Use the figure."),
        MISTAKE("Stating exact dates as certain", "Dates are approximate and differ between scholars. Use 'about' and the Gallio date as an anchor."),
        QUIZ("Which Roman proconsul inscription helps date Paul's stay in Corinth?",
             ["Felix", "Gallio", "Festus", "Sergius Paulus"], 1,
             "Gallio, proconsul of Achaia, is the anchor point (Acts 18:12).",
             hint="His name is linked to Delphi.",
             feedback=["Felix was governor of Judea.", "", "Festus was governor of Judea after Felix.", "Sergius Paulus was proconsul of Cyprus (Acts 13)."]),
        QUIZ("Why did Paul work as a tentmaker in Corinth?",
             ["Because he was not allowed to preach", "To support himself and not burden the new church", "Because Gentiles paid him to", "Because the synagogue demanded it"], 1,
             "He earned his own living, as he explains in 1 Corinthians 9 and 1 Thessalonians 2.",
             hint="He worked with Priscilla and Aquila.",
             feedback=["He preached every Sabbath.", "", "He refused payment from the Corinthians for his preaching.", "No such demand is recorded."]),
        PQ("Why did Paul normally begin his work in a new city at the synagogue? (structural question)",
           "The synagogue gave him an audience of Jews and God-fearers who already knew the scriptures and believed in one God, so he could argue that Jesus was the Messiah from texts they respected. "
           "It also reflected his conviction that the gospel is for the Jew first (Romans 1:16). It was a convenient base for contacts and a link with Jewish communities across the empire. "
           "When opposed, as in Corinth (Acts 18:6), he turned to Gentiles."),
        PQ("Explain the importance of Paul's co-workers.",
           "Paul worked with Barnabas, Silas, Timothy, Titus, Luke, and Priscilla and Aquila, among others. They shared teaching, travelled on his behalf, delivered letters and led churches in his absence. "
           "The team spread the workload and trained leaders, so that the churches could continue when Paul moved on. Their names in Romans 16 show that women and men from many backgrounds took part."),
        PQ("To what extent did Paul follow a planned strategy?",
           "For: he concentrated on cities on trade routes, started in synagogues, worked with teams, revisited churches and organised the collection. Romans 15 shows a wider plan including Spain. "
           "Against: Acts says the Spirit sometimes redirected him (16:6 to 10), and arrests, riots and expulsions often decided his movements. He also appears to have responded to invitations and crises, such as Corinth. "
           "He combined clear aims with flexibility, so the best conclusion is 'a strategy, but a flexible one'."),
        SUM("Paul made three journeys, then travelled to Rome as a prisoner; dates are approximate.",
            "His strategy used cities on trade routes, started with the synagogue, then turned to Gentiles.",
            "He worked with teams, supported himself by a trade and used house churches.",
            "He kept contact by letters, visits, appointment of elders and the collection for Jerusalem.",
            "He adapted his message to the audience while keeping the central message of Christ crucified and risen."),
    ],
))

LESSONS.append(lesson(
    module=M3, topic="1 Corinthians",
    title="1 Corinthians: a church with problems and Paul's answers",
    slug="rsu1-1-corinthians",
    minutes=28,
    summary="Corinth and its church, and Paul's replies on divisions, immorality, lawsuits, marriage, food offered to idols, the Lord's Supper, spiritual gifts and the resurrection.",
    objectives=[
        "Describe Corinth and the occasion of the letter",
        "Explain Paul's teaching on divisions, litigation, marriage and food offered to idols, linking each to the Corinthian situation",
        "Explain his teaching on the Lord's Supper and spiritual gifts (charismata)",
        "Explain the argument of chapter 15 on bodily resurrection",
    ],
    key_concepts=["Corinth", "Divisions", "Litigation", "Marriage and celibacy", "Idol meat", "Lord's Supper", "Charismata", "Resurrection body"],
    blocks=[
        H("Introduction"),
        T("Corinth was a wealthy port city in Greece, with harbours on two seas. Julius Caesar refounded it as a Roman colony in 44 BC, so its people were a mix of Romans, Greeks, Jews and others. "
          "It held the Isthmian Games and was known for trade and for a loose moral reputation, although scholars warn against exaggerating this. Paul founded the church there on his second journey, staying about eighteen months (Acts 18).\n\n"
          "He wrote 1 Corinthians from Ephesus, probably about AD 53 to 55 (check your textbook). He had heard of problems from 'Chloe's people' (1:11) and received a letter from the Corinthians (7:1). "
          "Most of the letter is Paul's answer to concrete questions. The Board's 2023 report named 1 Corinthians as part of Paper 3 section 2.3, and asked about marriage and food offered to idols, noting that candidates must link Paul's teaching to the actual situation in Corinth. "
          "Always begin with the problem, then give Paul's answer."),
        KEY("Outline of the letter", "A map of the main sections.", cards=[
            ["Chapters 1 to 4", "Divisions and the wisdom of the world versus the cross."],
            ["Chapters 5 and 6", "Immorality in the church and lawsuits before pagan courts; sexual ethics."],
            ["Chapter 7", "Marriage, divorce and singleness."],
            ["Chapters 8 to 10", "Food offered to idols, Paul's rights and warnings from Israel's history."],
            ["Chapters 11 to 14", "Worship: head coverings, the Lord's Supper, spiritual gifts and love."],
            ["Chapter 15 and 16", "Resurrection, the collection and greetings."],
        ]),
        H("Divisions (chapters 1 to 4)"),
        T("Some members said 'I belong to Paul', others 'to Apollos', 'to Cephas' (Peter) or 'to Christ' (1:12). They boasted of wisdom and preferred skilled speakers, in a city that valued rhetoric. "
          "Paul replies that Christ is not divided. He did not come with eloquent wisdom but preached Christ crucified, which seems foolish to the world but is God's power (1:18 to 25). "
          "Apollos watered and Paul planted, but God gave the growth (3:6). Leaders are servants and stewards, and members should not boast."),
        H("Immorality and lawsuits (chapters 5 and 6)"),
        T("A man was living with his father's wife and the church was proud, instead of mourning. Paul tells them to remove him from fellowship so that his spirit may be saved (5:1 to 5), and to avoid claiming to be believers while ignoring serious wrongs. "
          "In 6:1 to 8 he rebukes members who took each other to court before unbelieving judges. He asks whether the saints will judge the world, so why can they not settle small cases among themselves; better to suffer wrong than to wrong a fellow believer. "
          "In 6:12 to 20 he rejects the slogan 'all things are lawful for me' and says the body is a temple of the Holy Spirit and is not for immorality. "
          "Court cases between wealthy, high-status members and poorer ones may also have reflected the class tension in the church. Check your textbook."),
        H("Marriage and singleness (chapter 7)"),
        T("The Corinthians had written asking about sex and marriage. Some seem to have claimed 'it is good for a man not to touch a woman' (7:1, which scholars see as a Corinthian slogan or as Paul's view, a point of debate). "
          "Paul answers with a balanced teaching:"),
        KEY("Paul's guidance on marriage", "Link each point to the Corinthian situation.", cards=[
            ["Within marriage", "Because of immorality, each man should have his own wife and each woman her own husband. Husband and wife owe each other marital rights, and neither should refuse the other except by agreement for a time of prayer (7:2 to 5). The teaching is mutual."],
            ["The unmarried and widowed", "Paul wishes all were as he was (unmarried), but each has their own gift from God. If they cannot control themselves, they should marry (7:7 to 9)."],
            ["Divorce", "He cites a command from the Lord: the wife should not separate and the husband should not divorce (7:10 to 11). In the case of a believer married to an unbeliever, if the unbeliever is willing to stay, the believer should not leave; if the unbeliever leaves, the believer is not bound (7:12 to 16)."],
            ["Singleness and 'the present distress'", "Because of the 'present distress' (the exact meaning is debated, perhaps hardship or expectation of the end), Paul advises people to stay as they are, but marrying is not sin (7:25 to 38). He wants them free from anxiety."],
        ]),
        T("Paul's advice is a response to specific questions in a mixed church. It should not be reduced to a universal rule for all time, and scholars disagree about how far it does so. Be careful with this point in exams."),
        H("Food offered to idols (chapters 8 to 10)"),
        T("In Corinth, meat from pagan temples was often sold in the market or served at banquets in temple dining rooms. Some believers said 'an idol is nothing' and ate; others, converted from idol worship, felt it was a betrayal. "
          "Paul agrees that an idol is nothing and that there is one God (8:4 to 6), but says that 'knowledge puffs up, but love builds up' (8:1). "
          "Believers must not use freedom in a way that makes a weaker brother or sister fall (8:9 to 13). He gives himself as an example: he gave up his right to support (9). "
          "In chapter 10 he warns from the wilderness story of Israel that those who think they stand must take care, and he forbids sharing in the table of demons, that is joining in temple meals as worship. "
          "Practical rule: eat what is sold in the market without asking questions, but if someone says 'this has been offered in sacrifice', do not eat it for the sake of that person's conscience (10:25 to 29). 'Whatever you do, do it all for the glory of God' (10:31)."),
        H("The Lord's Supper (11:17 to 34)"),
        T("When the church gathered for a common meal and the Supper, the rich ate and drank too much, while the poor went hungry. Paul says that what they eat is not the Lord's Supper because they despise the church of God and humiliate those who have nothing. "
          "He reminds them of the words Jesus spoke on the night he was betrayed: 'This is my body... this cup is the new covenant in my blood', and says that whenever they eat and drink they proclaim the Lord's death until he comes. "
          "To eat or drink 'in an unworthy manner' (that is, without discerning the body, the community) brings judgement. Each must examine themselves."),
        H("Spiritual gifts (chapters 12 to 14)"),
        D("Gifts of grace given by the Holy Spirit to members of the church for the common good (from the Greek charisma). Paul lists wisdom, knowledge, faith, healing, miracles, prophecy, discernment, tongues and interpretation of tongues (12:8 to 10).", title="Charismata"),
        T("In Corinth, some boasted of gifts such as speaking in tongues and despised others. Paul uses the image of the **body**: one body with many parts, each needed, so the eye cannot say to the hand 'I do not need you' (12:12 to 26). "
          "Chapter 13, the hymn to love, says that without love the greatest gifts are nothing, and that love is patient and kind, and outlasts prophecy and tongues. "
          "In chapter 14 he prefers prophecy (clear speech that builds the church) to tongues unless there is interpretation, and says that all should be done decently and in order."),
        H("Resurrection (chapter 15)"),
        T("Some in Corinth said there is no resurrection of the dead. Paul answers in steps: (1) he reminds them of the tradition he received: Christ died for our sins, was buried, was raised on the third day and appeared to Cephas, the Twelve, more than five hundred, James, all the apostles and finally to Paul (15:3 to 8). "
          "(2) If there is no resurrection, then Christ has not been raised and the preaching and faith are in vain (15:12 to 19). "
          "(3) Christ has been raised as the 'first fruits' of those who have died, as Adam brought death and Christ brings life (15:20 to 28). "
          "(4) On the question 'with what kind of body?', he uses the image of a seed and says the body sown is perishable and raised imperishable, sown a physical body and raised a spiritual body (15:35 to 49). "
          "(5) At the last trumpet the dead will be raised and all changed (15:50 to 57)."),
        T("The 'spiritual body' (soma pneumatikon) is debated: it does not mean a ghost or a non-physical existence, since the word 'body' is used, but a body transformed and animated by the Spirit. Check your textbook."),
        TIP("Exam link: this is a Paper 3 section (the Early Church in Acts and 1 Corinthians, four questions chosen from six). Answer in this order: the situation in Corinth, Paul's teaching with verses, the application. "
            "The Board's report says candidates who list what is wrong in marriage without linking it to Corinth lose marks.", title="Exam link"),
        EX("Model answer plan 1", intro="Explain Paul's teaching on marriage in 1 Corinthians 7.", steps=[
            S("Situation", text="Corinth: immorality, an ascetic group saying 'not to touch', mixed marriages."),
            S("Teaching", text="Mutual duty in marriage; the unmarried may stay single if gifted; no divorce among believers; the believer with an unbelieving partner."),
            S("Reasons", text="Fidelity, peace, freedom from anxiety, 'the present distress'."),
            S("Comment", text="Paul answers questions, so his advice is partly contextual; scholars disagree about 7:1 and the 'distress'."),
        ]),
        EX("Model answer plan 2", intro="What problem about food offered to idols did Paul address and how?", steps=[
            S("Problem", text="Meat from temple sacrifices sold in the market and served at temple feasts; strong and weak consciences divided the church."),
            S("Principle", text="An idol is nothing, but knowledge must be ruled by love (chapter 8)."),
            S("Example and warning", text="Paul gives up his rights (chapter 9); Israel in the wilderness (chapter 10)."),
            S("Practice", text="Eat in the market without question; do not eat if it is pointed out as sacrificed; do not share in temple feasts."),
        ]),
        MISTAKE("Listing the ills of marriage in general", "The Board's report says that answers which do not tie the teaching to the Corinthian situation lose marks."),
        MISTAKE("Saying that Paul forbids eating all meat", "Paul says an idol is nothing and allows meat from the market, but not temple feasts or acts that harm a weaker conscience."),
        QUIZ("What was the main problem in the Lord's Supper in Corinth?",
             ["The meal was held on the wrong day", "The rich ate and drank while the poor went hungry", "Gentiles were not allowed", "Wine was forbidden"], 1,
             "Paul says they humiliate those who have nothing and fail to discern the body.",
             hint="Look at 11:21 to 22.",
             feedback=["The day is not the issue.", "", "No such ban is mentioned.", "Wine is part of the Supper."]),
        QUIZ("Why does Paul prefer prophecy to tongues in the church?",
             ["Tongues are evil", "Prophecy builds up the church by clear speech", "Tongues are only for Jews", "Prophecy is easier"], 1,
             "Chapter 14 says that what is understood builds up the church.",
             hint="Compare 'understood' and 'not understood'.",
             feedback=["He does not call tongues evil.", "", "Tongues are not limited by origin.", "He is not talking about ease."]),
        PQ("Explain the problems at Corinth and Paul's answers on marriage. (structural question)",
           "The church had members who thought sexual relations should be avoided, some who were immoral and some who were married to unbelievers. Paul teaches that each man and woman should have their own spouse, "
           "that husband and wife owe each other marital rights, that the unmarried and widowed may remain single if they are able, and that believers should not divorce. "
           "A believer married to a willing unbeliever should stay, but if the unbeliever leaves, the believer is not bound. He gives some advice because of 'the present distress' and because marriage brings concerns, but he says marriage is not sin."),
        PQ("Discuss Paul's response to the question of food offered to idols.",
           "Paul agreed with the 'strong' that an idol is nothing and there is one God, but he refused to let knowledge rule. Love requires that a believer should not cause a weaker brother or sister to fall. "
           "He used his own example of giving up rights and warned from Israel's history against overconfidence. "
           "In practice: meat bought at the market may be eaten without asking questions; if told that it was offered to an idol, do not eat it for the sake of the conscience of the one who told you; do not take part in feasts at temples, which is fellowship with demons."),
        PQ("What does Paul say about the resurrection body in chapter 15?",
           "Paul argues that Christ was raised and is the first fruits, so believers will be raised. When asked what kind of body, he uses the seed image: what is sown dies, and God gives it a new body. "
           "The body sown is perishable and weak and is raised imperishable and powerful; it is a 'spiritual body', not a mere spirit but a body transformed by the Spirit. "
           "At the last trumpet the dead will be raised and the living changed. Without the resurrection, he says, faith is futile."),
        SUM("Corinth was a wealthy, mixed Roman colony; Paul wrote about AD 53 to 55 in reply to reports and a letter.",
            "He rebukes divisions around leaders, teaches that the cross is God's wisdom, and rejects lawsuits and immorality.",
            "On marriage he teaches mutual duty, allows singleness, and addresses divorce and mixed marriages.",
            "On idol meat the rule is love: eat in the market, avoid temple feasts, do not harm a weaker conscience.",
            "At the Lord's Supper the community must be honoured; gifts are for the body, with love supreme; the resurrection is central."),
    ],
))

LESSONS.append(lesson(
    module=M3, topic="Galatians and Romans",
    title="Galatians and Romans: justification by faith, law and life in the Spirit",
    slug="rsu1-galatians-romans",
    minutes=27,
    summary="Why Paul wrote Galatians and Romans, his argument that people are put right with God by faith and not by works of the law, the role of the law, and life in the Spirit.",
    objectives=[
        "Describe the occasion and purpose of Galatians and of Romans",
        "Explain justification by faith and the argument from Abraham",
        "Explain Paul's view of the law and of grace",
        "Explain life in the Spirit and evaluate the main scholarly readings of justification",
    ],
    key_concepts=["Judaisers", "Justification", "Faith and works of the law", "Grace", "Abraham", "Life in the Spirit", "Fruit of the Spirit"],
    blocks=[
        H("Introduction"),
        T("These two letters are Paul's most sustained arguments on how a person comes to be right with God. Galatians is a passionate letter written to meet a crisis. Romans, written later to a church Paul had not founded, sets out the same ideas more calmly.\n\n"
          "Both letters answer the question that the Council of Jerusalem opened: must Gentile believers keep the Jewish law, above all circumcision, to belong fully to God's people? Paul says no, and he gives theological reasons."),
        D("In Paul, to be 'justified' is to be declared right with God, acquitted and accepted as a member of God's people. It is a legal image (a court verdict) used for a relationship. "
          "Paul says this happens through faith in Jesus Christ and not by 'works of the law'. How exactly to understand these phrases is debated, as shown below.", title="Justification"),
        H("Galatians: the occasion"),
        T("Paul founded churches in Galatia (scholars debate whether this means the northern region or the southern towns visited on the first journey, so check your textbook). "
          "After he left, other teachers arrived, often called **Judaisers**, saying that Gentile believers must be circumcised and keep the law of Moses to be saved. They also attacked Paul's authority as an apostle. "
          "Paul writes with no thanksgiving, and opens in anger: 'I am astonished that you are so quickly deserting the one who called you.'"),
        KEY("Outline of Galatians", "Three movements.", cards=[
            ["Chapters 1 and 2: Paul's authority", "His gospel came by revelation, not from humans. He tells how he met the Jerusalem leaders and how they accepted the Gentile mission without circumcision. At Antioch he opposed Peter for withdrawing from table fellowship with Gentiles (2:11 to 14)."],
            ["Chapters 3 and 4: the argument", "Justification by faith, the example of Abraham, the purpose of the law, sons and heirs."],
            ["Chapters 5 and 6: freedom and the Spirit", "Do not return to slavery; live by the Spirit and show its fruit."],
        ]),
        T("The heart is 2:16: a person is not justified by works of the law but through faith in Jesus Christ. In 2:20 Paul says he has been crucified with Christ and that Christ lives in him."),
        H("Abraham and the law (Galatians 3)"),
        T("Paul argues from scripture. Abraham 'believed God and it was reckoned to him as righteousness' (Genesis 15:6). That happened before circumcision (Genesis 17) and before the law of Moses, so those who have faith are Abraham's children, including Gentiles (3:7 to 9). "
          "The promise came 430 years before the law, and the law cannot cancel it (3:17). Why then the law? It was added because of transgressions, until the offspring came; it was like a **guardian** (paidagogos, a household slave who supervised a child) until Christ came (3:19 to 25). "
          "Now 'there is no longer Jew or Greek, there is no longer slave or free, there is no longer male and female; for all of you are one in Christ Jesus' (3:28)."),
        H("Freedom and the Spirit (Galatians 5 and 6)"),
        T("Paul warns that if they accept circumcision, Christ will be of no benefit to them; what counts is faith working through love (5:2 to 6). "
          "Freedom is not licence for selfish living. The flesh (human nature turned from God) and the Spirit are in conflict. The works of the flesh include immorality, idolatry, enmity, jealousy and drunkenness. "
          "The **fruit of the Spirit** is love, joy, peace, patience, kindness, goodness, faithfulness, gentleness and self-control (5:22 to 23). Those who belong to Christ walk by the Spirit and bear one another's burdens (6:2)."),
        H("Romans: occasion and purpose"),
        T("Paul wrote Romans from Corinth, probably about AD 56 to 57, as he prepared to take the collection to Jerusalem (15:25 to 26) and wanted to visit Rome on the way to Spain. "
          "The Roman church was not founded by him. It included Jews and Gentiles, and there were tensions between them (chapters 14 and 15). "
          "Scholars suggest several purposes: to introduce himself and his gospel and ask for support for Spain; to prepare for a possible hostile reception in Jerusalem; to heal tensions between Jewish and Gentile believers. They are not exclusive."),
        KEY("Outline of Romans", "The main sections.", cards=[
            ["1:1 to 17", "Greeting and theme: the gospel is the power of God for salvation, to the Jew first and also to the Greek; the righteousness of God is revealed through faith."],
            ["1:18 to 3:20", "All are under sin: Gentiles and Jews. 'No one will be justified by works of the law.'"],
            ["3:21 to 5:21", "Justification by faith in Christ. All have sinned, and are justified by grace through the redemption in Christ Jesus (3:23 to 24). Abraham (chapter 4). Peace with God. Adam and Christ (5:12 to 21)."],
            ["Chapters 6 to 8", "Dying and rising with Christ in baptism (6), the law and the struggle with sin (7), life in the Spirit and no condemnation (8)."],
            ["Chapters 9 to 11", "The place of Israel in God's plan."],
            ["Chapters 12 to 16", "Practical ethics: a living sacrifice, love, the state (13), the weak and the strong (14 and 15), greetings (16)."],
        ]),
        H("Justification in Romans"),
        T("Romans 3:21 to 26 is the centre. God's righteousness has been shown apart from the law through faith in Jesus Christ for all who believe. All have sinned and fall short of God's glory and are justified freely by his grace through the redemption in Christ, "
          "whom God put forward as an atoning sacrifice (the Greek word hilasterion is translated in different ways, so check your Bible). In Romans 4 Abraham is again the example: faith counted as righteousness, and the promise for all who share his faith, Jews or Gentiles."),
        D("Unearned favour: God's generous gift to people who do not deserve it. In Paul, grace is the basis of justification and of life in Christ, and it is opposed to the idea of earning right standing by achievement.", title="Grace"),
        H("The law"),
        T("Paul's view of the law has several sides. The law is holy and good (Romans 7:12), reveals sin (3:20, 7:7), and cannot give life because human weakness prevents keeping it (8:3). "
          "Christ is the end (or goal) of the law for righteousness for everyone who believes (10:4); the word 'end' can mean termination or goal, which is debated. "
          "Those who live by the Spirit fulfil the just requirement of the law (8:4) and love fulfils the law (13:8 to 10)."),
        H("Life in the Spirit (Romans 8)"),
        T("Chapter 8 opens: 'There is therefore now no condemnation for those who are in Christ Jesus.' The Spirit of life has set believers free from the law of sin and death. "
          "Those led by the Spirit are children of God and cry 'Abba, Father'. Creation itself groans in hope. Nothing can separate believers from the love of God in Christ (8:38 to 39)."),
        H("How do scholars read justification?"),
        KEY("Two main readings", "Know the debate; do not treat either as settled.", cards=[
            ["Traditional (Reformation) reading", "Paul opposes a religion of earning salvation by good works. People are sinners who cannot meet God's standard, and God declares the believer righteous through faith, by grace. Martin Luther made this reading famous."],
            ["'New perspective' reading", "E. P. Sanders (1977) argued that Judaism of Paul's time was based on God's covenant grace and not on earning salvation. Scholars such as James Dunn then argued that 'works of the law' meant boundary markers (circumcision, food laws, Sabbath) that separated Jews from Gentiles, so Paul's main point was that Gentiles belong to God's people by faith. N. T. Wright developed a related view."],
            ["Common ground", "Both agree that Paul says faith in Christ, not the law, is the way into God's people, and that this is God's gift. They differ on what Paul was arguing against."],
        ]),
        TIP("Exam link: Galatians and Romans belong to Pauline studies in the New Testament options. The Board's 2023 report names Acts and 1 Corinthians in Paper 3 section 2.3; check with your teacher whether your school's section also includes Galatians and Romans. "
            "Where they are set, link each teaching to the problem it answers.", title="Exam link"),
        EX("Model essay plan 1", intro="Explain what Paul meant by justification by faith.", steps=[
            S("Definition", text="Declared right with God, through faith in Christ, as a gift of grace."),
            S("Galatians", text="Written against Judaisers who demanded circumcision; Abraham believed and was counted righteous (3:6)."),
            S("Romans", text="All are under sin (1:18 to 3:20); justified freely by grace through redemption (3:24); Abraham (chapter 4)."),
            S("Evaluation", text="Traditional and 'new perspective' readings: what were 'works of the law'?"),
        ]),
        EX("Model essay plan 2", intro="Why did Paul teach that the law could not save?", steps=[
            S("Purpose of the law", text="It shows sin (Romans 3:20, 7:7), acts as a guardian until Christ (Galatians 3:24)."),
            S("Weakness", text="Human sinfulness prevents anyone from keeping it (Romans 8:3)."),
            S("Abraham", text="The promise preceded the law, and faith came before circumcision."),
            S("Balance", text="The law is holy and good; the Spirit enables believers to fulfil its requirement; love fulfils the law."),
        ]),
        MISTAKE("Saying that Paul thought the law was evil", "He says it is holy, righteous and good (Romans 7:12) but unable to give life."),
        MISTAKE("Treating one reading of 'works of the law' as the only one", "Present the traditional and the new perspective readings, with their main supporters, and say they are debated."),
        QUIZ("Who were the Judaisers in Galatians?",
             ["Roman officials who persecuted the church", "Teachers who said Gentile believers must be circumcised and keep the law", "Followers of Apollos", "Jewish priests in Jerusalem"], 1,
             "They insisted that Gentile converts adopt the law, especially circumcision.",
             hint="Think about the dispute that began in Acts 15.",
             feedback=["They were not Roman officials.", "", "The Apollos party is in 1 Corinthians.", "The letter does not describe them as the priests."]),
        QUIZ("Which of the following is part of the fruit of the Spirit (Galatians 5:22 to 23)?",
             ["Prophecy", "Love", "Circumcision", "Speaking in tongues"], 1,
             "Love, joy, peace, patience, kindness, goodness, faithfulness, gentleness and self-control.",
             hint="Look for a quality of character.",
             feedback=["Prophecy is a gift (charisma), not part of this list.", "", "It is the issue in Galatians, not a fruit.", "That is a gift in 1 Corinthians 12."]),
        PQ("Explain Paul's argument from Abraham in Galatians 3 and Romans 4. (structural question)",
           "Paul says Abraham believed God and it was counted to him as righteousness (Genesis 15:6). This happened before he was circumcised and long before the law was given, so righteousness comes through faith and not through the law or circumcision. "
           "Therefore all who share Abraham's faith, Jews and Gentiles, are his children and heirs of the promise. The argument takes the opponents' own scripture and shows that Gentiles do not need to become Jews to belong to God's people."),
        PQ("Why did Paul say that the law was a 'guardian'? (Galatians 3:24)",
           "The word paidagogos referred to a household slave who supervised a child until adulthood. The law's role was to guard and discipline God's people until Christ came. "
           "It was temporary and under the promise, not the final way to God. Now that faith in Christ has come, believers are no longer under the guardian but are children of God and heirs (3:25 to 4:7)."),
        PQ("Outline Paul's teaching about life in the Spirit in Romans 8 and Galatians 5.",
           "The Spirit sets believers free from the power of sin and death and from condemnation (Romans 8:1 to 2). Those led by the Spirit are children of God who can call him 'Abba, Father', and the Spirit helps in weakness and prayer. "
           "In Galatians 5, life by the Spirit contrasts with the works of the flesh and produces fruit: love, joy, peace, patience, kindness, goodness, faithfulness, gentleness and self-control. "
           "The Christian life is therefore freedom from the law as a way of earning right standing, and freedom for love and service."),
        SUM("Galatians answers Judaisers who demanded circumcision; Romans sets out the same gospel to a church Paul had not founded.",
            "Justification means being declared right with God, through faith in Christ and by grace, not by works of the law.",
            "Abraham's faith before circumcision and the law shows that Gentiles belong to God's people by faith.",
            "The law is holy and good but cannot give life; it was a guardian until Christ.",
            "Life in the Spirit brings freedom from condemnation and the fruit of the Spirit; scholars debate how to read 'works of the law'."),
    ],
))
