"""A Level History (0760), Lower Sixth: deeper lessons (KKEVO draft, for reviewer checking against the syllabus and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("history", "lower-sixth")

M_CAM = "Cameroon 1884–1945"
M_EUR = "European Revolutions & Unifications"
M_IMP = "Imperialism & the First World War"
M_INT = "The Interwar Crises"
M_EXAM = "Examination"

LESSONS = []

# ---------------------------------------------------------------------------
# Cameroon 1884-1945 / Treaties and borders
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CAM, topic="Treaties and borders",
    title="The Duala kings, the treaty and the Memorandum in detail",
    slug="h6-duala-kings-and-the-memorandum",
    minutes=22,
    summary="Who the Duala rulers were, what each side wanted in July 1884, how the treaty was made and divided Duala society, and how to judge whose interests it served.",
    objectives=[
        "Describe the Duala trading world and the pressures on the Duala rulers by 1884",
        "Explain what Germany wanted and how the treaty was made in July 1884",
        "Explain the divisions among the Duala, including the case of Hickory Town",
        "Judge how far the treaty served Duala and German interests",
    ],
    key_concepts=["Middleman trade", "Sovereignty", "Protectorate", "Kings' Memorandum", "Agency"],
    blocks=[
        H("Introduction"),
        T("Before 1884 the Duala of the Wouri estuary lived by trade. They bought goods from European ships on the coast "
          "and sold them to peoples of the interior, and they sold palm oil, ivory and other products back to the ships. "
          "This is called the **middleman trade**. It made the Duala house heads rich and powerful.\n\n"
          "This lesson looks closely at one event: the treaty of 12 July 1884. The existing overview lesson on treaties and "
          "borders gives the outline. Here we ask who wanted what, and why the treaty caused so much argument."),
        D("Supreme political authority over a territory and its people. In 1884 the Duala rulers transferred rights of "
          "government to German firms, and the firms passed these rights to the German state. Historians still debate how "
          "much the signatories understood about what they were giving up.", title="Sovereignty"),
        D("A relationship in which a stronger state takes responsibility for the defence and foreign relations of a weaker "
          "one. In practice a protectorate often became full colonial rule. This is exactly what happened in Kamerun.",
          title="Protectorate"),
        H("The Duala world in 1884"),
        T("Duala society was divided into several rival 'houses' or lineages, each led by a chief. Two of the best known were "
          "the house of Bell (King Bell, also called Ndumbe Lobe Bell) and the house of Akwa (King Akwa, Dika Mpondo). "
          "Other chiefs, such as Deido, ruled other quarters. The houses competed for control of trade.\n\n"
          "Europeans had traded on the coast for a long time. Missionaries such as the English Baptist Alfred Saker lived "
          "in the area. The kings sometimes asked the British government to take over, but no answer came that satisfied them. "
          "Check your textbook for the exact dates of these appeals."),
        H("What each side wanted"),
        KEY("Interests in July 1884", "A good answer separates the interests of each group.", cards=[
            ["Duala rulers", "To keep the middleman trade, to keep their land and customs, and to gain a strong protector against rivals and against traders who wanted to go inland themselves."],
            ["German firms", "Woermann and Jantzen und Thormaehlen wanted safe trade, protection from British competition and a chance to push inland. They wanted the German state to take on the cost of government."],
            ["German state", "Under Bismarck, Germany took a protectorate in 1884 cautiously and mainly to protect trade. The government wanted colonies that paid for themselves."],
        ]),
        H("How the treaty was made"),
        T("Gustav Nachtigal, German consul-general, arrived on the coast in July 1884. Kings Bell and Akwa signed the treaty "
          "with the German firms' representatives on **12 July 1884**. The German flag was raised on **14 July**. "
          "The British consul Edward Hewett arrived a few days later and found that Germany had acted first."),
        T("The treaty was written in a European language, and the Duala rulers also attached the Kings' Memorandum with their "
          "conditions. Historians ask how well the kings could read what they signed, and what the word 'sovereignty' meant "
          "to them. These are questions of interpretation, not fully settled facts."),
        H("A divided Duala community"),
        T("The Duala did not act as one. Some chiefs signed. Lock Priso of Hickory Town (near present-day Bonaberi) did not sign "
          "and fought German authority. German forces attacked Hickory Town in December 1884. The treaty therefore brought "
          "violence from the very start of German rule."),
        TIP("When you discuss the treaty, show the disagreement among the Duala. Writing 'the Duala accepted German rule' without "
            "qualification is a weaker answer."),
        EX("Model essay plan 1", intro="'The Germano-Douala Treaty benefited the Germans more than the Duala.' Discuss.", steps=[
            S("Introduction", text="State the date and signatories. Judgement: Germany gained most, but the Duala kings made a reasoned choice with some short-term gains."),
            S("Benefits to Germany", text="A coastal base won ahead of Britain; legal claim to authority from African signatures; firms protected at the state's cost."),
            S("Benefits to the Duala", text="Short-term protection of trade and of the kings' position; the Memorandum set out conditions."),
            S("Costs to the Duala", text="Division of the community, the attack on Hickory Town, and later broken promises over trade and land."),
            S("Judgement", text="The treaty served Germany better in the long run. The kings had a plan, but they could not enforce it."),
        ]),
        EX("Model essay plan 2", intro="Explain why the Duala rulers were not united over the German treaty.", steps=[
            S("Point 1: rival houses", text="Bell, Akwa and others competed for trade and status, so each house judged the German offer by its own interests."),
            S("Point 2: different views of risk", text="Some thought a protector would strengthen their position; Lock Priso refused and kept his independence."),
            S("Point 3: the pace of events", text="Nachtigal and the German firms acted quickly in July 1884, leaving little time for the Duala to agree a common position."),
            S("Link to the question", text="Disunity helped Germany: it could deal with the chiefs who signed and attack the one who did not."),
        ]),
        MISTAKE("Swapping 12 July and 14 July", "12 July: treaty signed. 14 July: German flag raised. Use the order: sign first, flag two days later."),
        MISTAKE("Calling the treaty either a 'free African choice' or a 'trick'", "Both labels are too simple. Explain the pressures on the kings and the choices they made, then give a judgement."),
        QUIZ("Which Duala ruler refused to accept the German treaty and was attacked in December 1884?",
             ["King Bell", "King Akwa", "Lock Priso of Hickory Town", "Rudolf Duala Manga Bell"], 2,
             "Lock Priso of Hickory Town (Bonaberi) did not sign, and German forces attacked his town in December 1884.",
             feedback=["King Bell signed the treaty.", "King Akwa signed the treaty.", "", "Rudolf Duala Manga Bell was a later leader, executed in 1914."]),
        QUIZ("Why is it misleading to write 'the Duala accepted German rule'?",
             ["Because no Duala ruler ever signed anything", "Because the Duala were divided and one important ruler refused", "Because the treaty was signed by Britain", "Because the treaty was signed in 1914"], 1,
             "The Duala were divided into rival houses, and Lock Priso of Hickory Town refused to sign.",
             feedback=["Kings Bell and Akwa did sign.", "", "The treaty was with German firms.", "It was signed in 1884."]),
        PQ("Explain two reasons why the Duala rulers wanted a European protector in 1884.",
           "Outline: (1) To protect their middleman trade against European traders who wanted to deal directly with the interior. (2) To strengthen the position of their house against rivals such as other Duala chiefs. "
           "Support each with a detail: the Memorandum asked for protection of trade; the houses of Bell and Akwa competed with each other."),
        PQ("How far did German firms and the German government want the same things in 1884?",
           "Outline: Similar: both wanted secure trade and to keep out British competition. Different: the firms wanted the state to carry the cost of government; Bismarck wanted protectorates that would pay for themselves and avoid heavy spending. "
           "Judgement: broadly shared aims, with a difference over who would pay."),
        PQ("'The treaty of 1884 shows that Africans were active makers of their own history.' How far do you agree?",
           "Outline: For: the kings negotiated, chose Germany over a hesitant Britain and wrote conditions into the Memorandum; Lock Priso resisted. "
           "Against: the German firms and Nachtigal set the pace; the Memorandum could not be enforced; German power grew. "
           "Judgement: the Duala had agency in the decision, but little power over the results."),
        SUM("The Duala were middlemen divided into rival houses, with Bell and Akwa the best-known kings.",
            "Treaty signed 12 July 1884; German flag raised 14 July; Hewett arrived too late for Britain.",
            "The Duala wanted protection of trade, land and position; the German firms wanted safe trade at the state's cost.",
            "Lock Priso refused to sign and Hickory Town was attacked in December 1884.",
            "Judge the treaty by asking who gained, who had power, and how united the Duala were."),
    ],
))

LESSONS.append(lesson(
    module=M_CAM, topic="Treaties and borders",
    title="From coast to frontier: how Kamerun's borders were fixed, 1884-1922",
    slug="h6-making-kamerun-borders-1884-1922",
    minutes=24,
    summary="A step-by-step chronology of the boundary agreements, the 1911 Moroccan exchange, the First World War partition and the mandates, with a way to judge how African or European the borders were.",
    objectives=[
        "Place the main Anglo-German and Franco-German agreements in order",
        "Explain how the 1911 treaty created Neukamerun and why it was later undone",
        "Describe the partition of 1916 to 1919 and the mandates of 1922",
        "Judge the claim that Cameroon's borders were made in Europe",
    ],
    key_concepts=["Boundary convention", "Neukamerun", "Hinterland", "Milner-Simon declaration", "Mandate"],
    blocks=[
        H("Introduction"),
        T("The coastal treaty of 1884 gave Germany a small area. The Kamerun on the map grew inland over thirty years through "
          "agreements between European governments, and in 1919 it was divided. Today's Cameroon is the result of both stages.\n\n"
          "This lesson gives you a clear chronology and teaches you how to argue about it."),
        IMG("al-h6-kamerun-timeline.svg", alt="Timeline of the making of Cameroon's borders from 1884 to 1922",
            caption="Figure 1. Key stages in the making of Kamerun and its division. Events are evenly spaced, not to scale."),
        D("An agreement between two states fixing the line between their territories. In this period such lines were often "
          "drawn on maps by officials who had not visited the area. Many were later adjusted on the ground.", title="Boundary convention"),
        D("The part of Kamerun added in 1911 from French Equatorial Africa, in exchange for German acceptance of French control "
          "in Morocco. The name means 'New Cameroon'. It was returned to French Equatorial Africa in 1919.", title="Neukamerun"),
        H("Stage 1: the western and southern frontiers"),
        T("With Britain, Germany made agreements in 1885 and 1886 and again in 1893 fixing the line between Kamerun and British "
          "territory in the Niger region. A further Anglo-German agreement of 1913 dealt with the line from the Yola area to the "
          "sea. It placed the Bakassi area on the German side. Treat the Bakassi question with care: it was later the subject of "
          "legal decisions, and your textbook will explain the modern dispute."),
        T("With France, Germany agreed the southern border with the French Congo and Gabon area in the 1880s, and a convention of "
          "1894 dealt with the east towards Lake Chad. Check the exact dates and names of these conventions in your textbook."),
        H("Stage 2: 1911 and Neukamerun"),
        T("In 1911 France and Germany quarrelled over Morocco (the second Moroccan, or Agadir, crisis). A treaty signed on "
          "4 November 1911 settled it. Germany accepted French control of Morocco. France gave Germany large strips of French "
          "Equatorial Africa, which gave Kamerun access to the Congo and Ubangi rivers. The people who lived there were not asked."),
        H("Stage 3: war and partition, 1914 to 1922"),
        T("In 1914 Britain, France and Belgium attacked Kamerun. German resistance ended in February 1916. In 1916 Britain and "
          "France made a provisional division. The Milner-Simon declaration of **10 July 1919** fixed the main line: France received "
          "the larger share and Britain two strips on the western side. Neukamerun went back to France. In 1922 the League of "
          "Nations confirmed the arrangement as two mandates."),
        IMG("al-h6-kamerun-partition.svg", alt="Schematic boxes showing Kamerun, Neukamerun and the 1916 to 1919 division into British and French shares",
            caption="Figure 2. A schematic of the changes, not a map."),
        EX("Model essay plan 1", intro="Assess the importance of the First World War in determining the borders of Cameroon.", steps=[
            S("Introduction", text="Before 1914 the frontier was German; after 1919 it was British and French. Judgement: the war was decisive for the internal division, but the outer frontiers owed more to earlier agreements."),
            S("Before the war", text="Anglo-German and Franco-German conventions from 1885 to 1913 fixed the outer limits of Kamerun."),
            S("The war itself", text="Military conquest in 1914 to 1916 removed German rule and led to the 1916 provisional division."),
            S("After the war", text="Milner-Simon (10 July 1919) and the 1922 mandates made the division permanent and returned Neukamerun to France."),
            S("Judgement", text="Pre-war agreements fixed where the lines ran, war decided who ruled on each side."),
        ]),
        EX("Model essay plan 2", intro="'Cameroon's borders were made without African participation.' How far is this true?", steps=[
            S("Introduction", text="Define the time (1884 to 1922). Judgement: largely true for the frontier lines, but African action shaped the starting point and the war."),
            S("For the claim", text="The conventions with Britain and France, the 1911 exchange and the 1919 declaration were negotiated by Europeans. No African delegations are recorded."),
            S("Against the claim", text="The coastal treaty of 1884 was signed by Duala kings who attached conditions; resistance to German expansion slowed and shaped the extension of control."),
            S("Evaluation", text="African participation was strongest at the start and weakest when the lines were drawn."),
            S("Judgement", text="The lines were European-made; the existence of a colony to draw lines around began with African decisions in 1884."),
        ]),
        MISTAKE("Mixing up Neukamerun and the 1919 split", "Neukamerun was added in 1911. The British and French shares were created in 1916 to 1919. Keep both on your timeline."),
        MISTAKE("Giving only dates", "An agreement in your essay must be linked to a cause, such as the Moroccan crisis, and a result, such as a larger Kamerun."),
        QUIZ("What did Germany gain by the treaty of 4 November 1911?",
             ["Control of Morocco", "Large parts of French Equatorial Africa added to Kamerun", "The Bakassi area", "The mandate over Togo"], 1,
             "France gave Germany territory in Equatorial Africa (Neukamerun); Germany accepted French control of Morocco.",
             feedback=["Germany accepted French control of Morocco.", "", "The Anglo-German agreement of 1913 dealt with this area.", "Togo is not part of this treaty."]),
        QUIZ("Which document in 1919 fixed the main division of Kamerun between Britain and France?",
             ["The Berlin Act", "The Milner-Simon declaration", "The Kings' Memorandum", "The Atlantic Charter"], 1,
             "The Milner-Simon declaration of 10 July 1919 divided Kamerun between Britain and France.",
             feedback=["The Berlin Act dates from 1885 and concerned the Scramble.", "", "The Memorandum dates from 1884.", "The Atlantic Charter dates from 1941."]),
        PQ("Explain why France gave part of its Equatorial African territory to Germany in 1911.",
           "Outline: The second Moroccan crisis had brought France and Germany close to war. France wanted Germany to accept its control of Morocco. In exchange it ceded strips of the French Congo, which became Neukamerun. The territory was used as a bargaining chip, with no consultation of its people."),
        PQ("Describe how Kamerun was divided between 1916 and 1922.",
           "Outline: 1916 provisional Anglo-French division after the German defeat; Milner-Simon declaration (10 July 1919) giving France the larger share and Britain two strips in the west; return of Neukamerun to France; League mandates confirmed in 1922."),
        PQ("To what extent were the borders of Cameroon decided in Europe?",
           "Outline: Yes: European conventions (1885 to 1913), the 1911 treaty and the 1919 declaration, all made in European capitals. No: Duala treaty of 1884, resistance, and military facts on the ground. Judgement: lines were drawn in Europe, but they followed African events and were lived in by Africans."),
        SUM("Anglo-German and Franco-German conventions fixed Kamerun's outer lines from the 1880s to 1913.",
            "The treaty of 4 November 1911 added Neukamerun in exchange for German acceptance of French control in Morocco.",
            "After the 1914-1916 conquest Britain and France divided Kamerun; Milner-Simon dates from 10 July 1919.",
            "The League confirmed the mandates in 1922.",
            "Borders were largely European-made, with African action shaping the context."),
    ],
))

LESSONS.append(lesson(
    module=M_CAM, topic="Treaties and borders",
    title="Source skills: how to evaluate a historical source",
    slug="h6-source-skills-evaluating-a-source",
    minutes=24,
    summary="A five-step method (origin, purpose, content, value, limits) for judging a source, practised on two invented illustrative sources about colonial Cameroon that are clearly labelled as not real documents.",
    objectives=[
        "Use origin, purpose and content to describe a source",
        "Judge a source's value and limitations for a specific question",
        "Compare two sources and reach a supported conclusion",
        "Avoid common errors such as dismissing a source because it is biased",
    ],
    key_concepts=["Primary source", "Secondary source", "Provenance", "Purpose", "Reliability", "Utility"],
    blocks=[
        H("Introduction"),
        T("History is built from sources: treaties, letters, petitions, photographs, newspapers, and the books written later by historians. "
          "An A Level examiner does not ask only 'what does the source say?'. It asks 'how far can we trust it?' and 'how useful is it for this question?'.\n\n"
          "This lesson gives a method. **The sources in this lesson are invented by KKEVO for practice. They are not real documents and must never be quoted as evidence in an essay.**"),
        D("A source made at the time of the events by someone who was there or took part: a treaty, a diary, a petition, a newspaper report. "
          "A **secondary source** is written later by someone who studies the past, such as a textbook or a historian's article.", title="Primary and secondary sources"),
        D("The facts about where a source comes from: author, date, place, and the kind of document. Also called **provenance**.", title="Origin"),
        IMG("al-h6-opcvl.svg", alt="Five boxes labelled Origin, Purpose, Content, Value and Limits", caption="Figure 1. The OPCVL method."),
        H("The method: O P C V L"),
        T("**Origin**: Who made it, when, where, and what kind of document is it? **Purpose**: Why was it made and for whom? A private diary and a report to a "
          "government have different purposes. **Content**: What does it actually say, and what does it leave out?"),
        T("**Value**: What can it tell us about the question asked? **Limits**: What can it not tell us? A source has value even if it is "
          "biased, because bias is itself evidence of an attitude. Never write 'this source is biased so it is useless'."),
        KEY("Reliability and utility", "Two different questions.", cards=[
            ["Reliability", "Can we believe what the source says? This depends on the author's knowledge, honesty and purpose."],
            ["Utility", "Is the source useful for this question? A biased or one-sided source can still be very useful, for example for showing how colonial officials thought."],
        ]),
        H("Illustrative Source A (invented by KKEVO, not a real document)"),
        T("*Invented practice text.* A letter written in 1885 by an imaginary agent of a trading company on the Cameroon coast to his manager in Hamburg: "
          "'The local chiefs are friendly and sign what is put before them. If the company wants the interior, the chiefs must be kept happy. "
          "Our competitors speak of British protection, but I think we have acted in time.'"),
        EX("Worked example 1: evaluating Source A", intro="How useful is Illustrative Source A for a historian studying why German traders wanted a treaty in 1884 and 1885?", steps=[
            S("Origin", text="An imaginary company agent writing to his manager, in 1885, soon after the events. A private business letter."),
            S("Purpose", text="To report to the employer. It is not meant for publication, which suggests the writer may speak frankly about the company's aims."),
            S("Content", text="Says the chiefs 'sign what is put before them'; stresses keeping chiefs happy to reach the interior; mentions competitors and British protection."),
            S("Value", text="Shows a trader's view that the interior was the aim and that British competition mattered. It supports the idea that commerce drove the German firms."),
            S("Limits", text="One agent's opinion. It says nothing about the Duala view, the German state's reasons, or whether the chiefs understood the treaty. The claim that chiefs 'sign what is put before them' is the writer's judgement, not proof."),
            S("Judgement", text="Useful for trader motives; limited for African views and for state policy."),
        ]),
        H("Illustrative Source B (invented by KKEVO, not a real document)"),
        T("*Invented practice text.* A petition sent in the 1930s by an imaginary group of Duala traders to the League of Nations: "
          "'Our fathers accepted protection, not the loss of their land. We ask that the promises made in the past be remembered.'"),
        EX("Worked example 2: comparing A and B", intro="How far do Sources A and B agree about the relationship between Africans and Europeans?", steps=[
            S("Points of agreement", text="Both suggest a bargain was made in the 1880s and that European promises mattered."),
            S("Points of disagreement", text="A treats the chiefs as easy to manage and the treaty as a commercial tool. B treats the treaty as a limited protection that was later broken."),
            S("Provenance explains the difference", text="A is a private business letter from a trader who gained from the treaty. B is a public petition from people who lost land, written to win support from the League. Each author selects what suits their purpose."),
            S("Conclusion", text="They do not contradict each other as much as they look: they show two sides of one bargain, seen by those who gained and by those who lost."),
        ]),
        MISTAKE("Dismissing a source because it is biased", "Say what the bias is, why it exists, and what the source still shows. Bias is evidence."),
        MISTAKE("Judging by the type of source alone", "A government report is not automatically reliable and a private letter is not automatically honest. Check purpose and knowledge."),
        MISTAKE("Using outside knowledge instead of the source", "Use your own knowledge to test and explain the source, but always start from what the source says."),
        TIP("The Board's paper formats are to be checked with your teacher. As good practice, label every quote and say which source you mean (Source A, Source B)."),
        QUIZ("Which of these best describes a primary source for a historian studying the 1884 treaty?",
             ["A modern textbook chapter on the Scramble", "A letter written by a trader in 1885", "A film made in 2010", "An encyclopaedia entry written in 1990"], 1,
             "A primary source comes from the time of the events. A letter written in 1885 is an example; the others were written later.",
             feedback=["Written long after the events: secondary.", "", "Made long after: not a primary source for 1884.", "Written long after: secondary."]),
        QUIZ("A source is written by a colonial officer who wanted to show that his policy was a success. What is the best comment?",
             ["It is useless because it is biased", "It is reliable because officers saw events", "Its purpose may lead the writer to select what looks good, but it is useful evidence of how officials justified policy", "It cannot be used because it is a primary source"], 2,
             "Purpose affects selection. The source is still useful, especially for officials' attitudes and justifications.",
             feedback=["Bias does not make a source useless.", "Being there does not guarantee honesty or full knowledge.", "", "Primary sources are exactly what historians use."]),
        PQ("Using Illustrative Source A, explain one way in which it is useful and one way in which it is limited for a study of the 1884 treaty.",
           "Outline: Useful: it shows a trader's view that the interior and British competition were key concerns, supporting a commercial explanation. Limited: it is one agent's view, from the German side, with no information on Duala aims or on the German government. Make a short judgement."),
        PQ("What can a historian learn from Illustrative Source B even though it comes from people with a grievance?",
           "Outline: It shows how some Africans remembered the bargain and how they used the League's petition system. The grievance is part of the evidence; it must be tested against other sources, such as the actual treaty and Memorandum."),
        PQ("Explain the difference between 'how reliable is this source?' and 'how useful is this source?'.",
           "Outline: Reliability concerns trust in its claims (knowledge, honesty, purpose). Utility concerns its value for the question asked; an unreliable or biased source can be useful, for example for showing attitudes. Give one example."),
        SUM("Use OPCVL: origin, purpose, content, value, limits.",
            "Reliability and utility are different questions.",
            "A biased source is evidence of attitudes, not a useless source.",
            "Compare sources by explaining differences through provenance and purpose.",
            "Sources in this course that are marked invented must not be quoted as real evidence."),
    ],
))

# ---------------------------------------------------------------------------
# Cameroon 1884-1945 / Comparative colonial rule
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CAM, topic="Comparative colonial rule",
    title="German rule in Kamerun: conquest, plantations and chiefs",
    slug="h6-german-rule-conquest-plantations-chiefs",
    minutes=22,
    summary="How Germany extended control inland, how it used force, plantations and cooperating rulers such as Fon Galega I and King Njoya, and how to judge German rule fairly.",
    objectives=[
        "Describe how German control spread from the coast to the interior",
        "Explain the plantation economy and its effect on the Bakweri and on labour",
        "Explain how Germany used African rulers as allies",
        "Weigh violence and development in an evaluation of German rule",
    ],
    key_concepts=["Schutztruppe", "Plantation", "Crown land", "Ally and collaboration", "Forced labour"],
    blocks=[
        H("Introduction"),
        T("German rule in Kamerun lasted about thirty years. It began with a coastal treaty and, after 1884, spread inland by "
          "expeditions, treaties and wars. The German state wanted trade and revenue. It used a small colonial force called the "
          "**Schutztruppe**, made up of a few German officers and many African soldiers, and it relied on African rulers.\n\n"
          "This lesson covers what German rule did. It is a topic where violence must be described honestly, without exaggeration and without excuse."),
        D("A large farm that grows one or two crops for export, using hired or forced workers. In Kamerun the main plantation crops "
          "were cocoa, bananas, rubber and palm products.", title="Plantation"),
        D("Land the colonial state declared to be its own. A German law of 1896 treated land not clearly in use as crown land and "
          "opened it to companies. Check the exact title and date of the law in your textbook.", title="Crown land"),
        H("Conquest of the interior"),
        T("German explorers and officers such as Eugen Zintgraff led expeditions into the Grassfields and the forest. "
          "Some peoples were defeated by force. Others signed agreements with the Germans and kept much of their local authority. "
          "In the Beti area, German posts were set up in the 1880s and 1890s and the forest peoples fought and negotiated."),
        T("Resistance was widespread, from the Bakweri on the slopes of Mount Cameroon to peoples of the forest and grassland. "
          "German rule was therefore a long process of conquest and settlement, not a single event of 1884. "
          "The names and dates of individual campaigns should be checked in your textbook."),
        H("Plantations and labour"),
        T("From the mid-1890s the governor, Jesko von Puttkamer, encouraged plantation companies on the fertile volcanic soils near "
          "Mount Cameroon. Land was taken from the Bakweri. Later, reserves were created for the Bakweri, but much of the best land went to the companies. "
          "The plantations needed workers, and recruitment was often by pressure or force. Check the dates of the governors in your textbook."),
        T("German officials also built the port and railway lines. The Northern railway went from Douala towards Nkongsamba, and a Central railway was begun towards Yaoundé. "
          "Roads and railways helped trade and administration, but they were built with African labour that was often forced and in poor conditions."),
        H("Chiefs as allies"),
        T("Germany rarely had enough officers to rule alone. It worked with chiefs who accepted its authority. Fon Galega I of Bali is a well-known ally who "
          "helped German expeditions in the Grassfields. King Njoya of Bamum cooperated with the Germans and kept control of his kingdom, "
          "and is known for creating a writing system for the Bamum language."),
        KEY("Two ways to read the German period", "Both can be supported by evidence.", cards=[
            ["Exploitation", "Land seizure, forced labour and violent conquest show a regime built on force and extraction."],
            ["Development and cooperation", "Ports, railways, plantations, mission schools and agreements with rulers show a more complex picture. Developments mainly served export trade."],
        ], note="A strong essay says who benefited and who paid the cost."),
        EX("Model essay plan 1", intro="'German rule in Kamerun depended more on force than on cooperation.' How far do you agree?", steps=[
            S("Introduction", text="Define force and cooperation. Judgement: force was essential to conquest, but day-to-day rule needed African allies."),
            S("Force", text="Expeditions and wars in the interior; Schutztruppe; recruitment of labour by pressure; land taken for plantations."),
            S("Cooperation", text="Alliances with rulers such as Fon Galega I and King Njoya; African soldiers and clerks; local chiefs as intermediaries."),
            S("Link", text="Chiefs cooperated partly because of the threat of force, so the two are connected."),
            S("Judgement", text="Force opened the door and cooperation ran the system; the balance changed over time and place."),
        ]),
        EX("Model essay plan 2", intro="Explain the effects of the plantation economy on the Bakweri.", steps=[
            S("Point 1: loss of land", text="Land near Mount Cameroon was taken for German companies; reserves were made but were limited."),
            S("Point 2: labour", text="Plantations needed workers; many were brought from other regions, and the Bakweri were pressed to work or pushed to the margins."),
            S("Point 3: later memory", text="The land question lasted into the British and later periods and remained a political issue."),
            S("Link to the question", text="The plantation economy changed who owned the best land and shaped later disputes."),
        ]),
        MISTAKE("Saying Germany 'developed' Kamerun without saying for whom", "Name the purpose: export trade and revenue. Then name who gained and who bore the costs."),
        MISTAKE("Making German rule the 'worst' by assertion", "Compare with specific evidence on violence, labour and land under later rulers. Use balanced language."),
        QUIZ("Which governor encouraged large plantations near Mount Cameroon from the mid-1890s?",
             ["Gustav Nachtigal", "Jesko von Puttkamer", "Edward Hewett", "Frederick Lugard"], 1,
             "Jesko von Puttkamer served as governor of Kamerun and encouraged plantation companies.",
             feedback=["Nachtigal was consul-general in 1884.", "", "Hewett was a British consul.", "Lugard is linked with British Nigeria."]),
        QUIZ("Why did Germany need African allies such as Fon Galega I?",
             ["It had no soldiers at all", "It had few officials and needed local rulers to help control the interior", "The League of Nations required it", "Britain ordered it"], 1,
             "Germany had a small number of officials and relied on local rulers.",
             feedback=["It had the Schutztruppe, though small.", "", "The League did not exist yet.", "Britain did not control Germany's policy."]),
        PQ("Explain two ways in which Germany extended its control inland after 1884.",
           "Outline: (1) Expeditions and military campaigns by the Schutztruppe, with defeat of resisting peoples. (2) Agreements and alliances with rulers such as Fon Galega I of Bali and King Njoya of Bamum. Support each with a name."),
        PQ("Describe the plantation economy in Kamerun before 1914.",
           "Outline: Plantations of cocoa, bananas, rubber and palm products on land near Mount Cameroon taken from the Bakweri, run by companies, with labour that was often recruited by pressure. Add the purpose: export to Germany."),
        PQ("To what extent was German rule in Kamerun a period of development?",
           "Outline: For: the port of Douala, railways, roads, plantations, mission schools. Against: these served export and administration; the work used forced labour; land was taken; conquest was violent. Judgement: some infrastructure was built, but not mainly for the benefit of Cameroonians."),
        SUM("Germany extended control inland by expeditions, wars, agreements and alliances.",
            "Plantations near Mount Cameroon took land from the Bakweri and needed labour that was often forced.",
            "German rule used allies such as Fon Galega I and King Njoya to control a large territory with few officials.",
            "Historians weigh violence and extraction against infrastructure and cooperation.",
            "Always name who gained and who paid."),
    ],
))

LESSONS.append(lesson(
    module=M_CAM, topic="Comparative colonial rule",
    title="British indirect rule in the Cameroons",
    slug="h6-british-indirect-rule-in-the-cameroons",
    minutes=22,
    summary="What indirect rule was in theory, how Britain applied it to the Northern and Southern Cameroons from Nigeria, its strengths and weaknesses, and why historians speak of neglect.",
    objectives=[
        "Define indirect rule and name its link with Lugard",
        "Describe how the British Cameroons were administered from Nigeria",
        "Explain how Native Authorities worked and where they succeeded or struggled",
        "Assess the view that British rule was a policy of neglect",
    ],
    key_concepts=["Indirect rule", "Native Authority", "Dual Mandate", "Mandate", "Cameroons Development Corporation"],
    blocks=[
        H("Introduction"),
        T("After 1916 Britain governed two narrow strips of former Kamerun on the border with Nigeria. After 1922 it ruled them under a League of Nations mandate, "
          "not as an ordinary colony. In practice Britain administered the territory as part of Nigeria.\n\n"
          "To understand the system, start with indirect rule, an idea Britain used in many places."),
        D("A system in which a colonial power governs through existing local rulers and institutions, under the supervision of European officers. "
          "In British West Africa it is closely linked with Frederick Lugard, who set out his ideas in *The Dual Mandate in British Tropical Africa* (1922).", title="Indirect rule"),
        D("A local ruler or council recognised by the colonial government to collect taxes, run a native court and keep order. "
          "Its powers were set by the colonial government.", title="Native Authority"),
        H("How the Cameroons were run"),
        T("Northern Cameroons were administered with the Northern Provinces of Nigeria and Southern Cameroons with the Southern (later Eastern) Provinces. "
          "Officials in Lagos and in the regional capitals took the main decisions. There were few British officers on the spot. "
          "Check in your textbook how the divisions were organised and how they changed over time."),
        T("In the northern areas, which had emirates and well-organised chiefdoms, indirect rule fitted easily. In parts of the south, where "
          "societies were smaller and chiefs had less power, officials sometimes had to appoint or strengthen chiefs, and this could cause trouble. "
          "In the grassland of Bamenda, Fons with real authority made indirect rule easier to apply."),
        H("What Native Authorities did"),
        T("Native Authorities collected taxes, ran native courts and paid small local services from the money they raised. "
          "Britain argued that this respected local custom and cost little. Critics argued that it kept ordinary people under chiefs who answered to the government "
          "and that it did not prepare Cameroonians for a wider political life."),
        H("Neglect or sound economy?"),
        T("Many historians describe the British Cameroons as neglected: few officers, little investment, and decisions taken far away. "
          "The plantations of the former German period were sold by auction in the early 1920s, and many returned to German owners. "
          "The Cameroons Development Corporation was set up in the 1940s to run lands that had come into public hands. Check the exact dates in your textbook."),
        T("Other historians point to the limits of the budget and to the mandate's expectation that the territory should pay its own way. "
          "They argue that Britain's low cost model was a policy choice, not simple forgetfulness."),
        KEY("Judging British rule", "Use the criteria before you decide.", cards=[
            ["Administration", "Light, cheap, run through Native Authorities from Nigeria."],
            ["Development", "Limited investment in roads, schools and health; missions provided much education."],
            ["Politics", "Few chances for educated Cameroonians; politics in the Cameroons was tied to Nigeria."],
        ]),
        EX("Model essay plan 1", intro="Assess how far indirect rule was suitable for the Cameroons.", steps=[
            S("Introduction", text="Define indirect rule. Judgement: it worked where strong chiefs existed, and less well where they did not."),
            S("Where it suited", text="Societies with Fons or emirs; Native Authorities collected tax and kept order cheaply."),
            S("Where it did not", text="Societies without strong chiefs; appointed chiefs lacked support; tension between the chiefs and educated people."),
            S("Wider effects", text="Administration from Nigeria meant the Cameroons had little separate attention."),
            S("Judgement", text="Suitable in some areas for the colonial government, but it limited development and political change."),
        ]),
        EX("Model essay plan 2", intro="'British rule in the Cameroons between the wars was a policy of neglect.' Discuss.", steps=[
            S("Introduction", text="Define neglect as low investment and little attention. Judgement: largely accurate, with some qualifications."),
            S("Evidence for neglect", text="Few British officers; rule through Nigeria; plantations returned to former owners; little spending on services."),
            S("Evidence against", text="Native Authority courts and tax system provided order; missions and local councils supplied services."),
            S("Explanation", text="The mandate did not require Britain to spend heavily, and the Cameroons were small and distant for Nigeria's administrators."),
            S("Judgement", text="Neglect is a fair summary of investment, but not of administration, which was cheap by design."),
        ]),
        MISTAKE("Saying Britain had no system", "Britain had a system: indirect rule. The question is how well it worked."),
        MISTAKE("Forgetting that the territory was a mandate", "Britain reported to the League's Permanent Mandates Commission. Mention it and say how effective it was."),
        QUIZ("Which British colonial official is most closely linked with indirect rule?",
             ["Cecil Rhodes", "Frederick Lugard", "Edward Hewett", "Lord Milner"], 1,
             "Lugard developed indirect rule in Nigeria and wrote about it in The Dual Mandate (1922).",
             feedback=["Rhodes is linked with southern Africa.", "", "Hewett was a consul in 1884.", "Milner signed the 1919 declaration."]),
        QUIZ("How did Britain mainly govern the British Cameroons between the wars?",
             ["As a separate colony with its own governor", "As part of Nigeria, through Native Authorities", "Through French officials", "Directly from London with no local rulers"], 1,
             "The territory was administered from Nigeria, using Native Authorities.",
             feedback=["It was not a separate colony.", "", "France ruled its own share.", "Britain used local rulers under indirect rule."]),
        PQ("Explain what a Native Authority was.",
           "Outline: A local ruler or council recognised by the colonial government to collect taxes, run a native court and keep order, under the supervision of British officers. Add one example, such as a Fon in Bamenda."),
        PQ("Why did indirect rule work better in some parts of the Cameroons than in others?",
           "Outline: It worked where strong chiefs and clear authority existed, such as the grassland Fons or northern chiefdoms. It worked less well where societies had no strong chiefs and officials had to appoint them. Give a short judgement."),
        PQ("Assess the view that British rule in the Cameroons was neglectful.",
           "Outline: For: rule from Nigeria, few officers, little investment, plantations returned to German owners. Against: Native Authorities supplied basic order; missions gave education; the later Corporation shows later investment. Judgement: largely neglect in 1922 to 1945."),
        SUM("Indirect rule means ruling through existing local rulers under European supervision (Lugard).",
            "The British Cameroons were governed as part of Nigeria through Native Authorities.",
            "It worked best where strong chiefs existed and less well elsewhere.",
            "Many historians describe the period as neglect, though the system was cheap by design.",
            "The mandate meant League supervision, but it was weak."),
    ],
))

LESSONS.append(lesson(
    module=M_CAM, topic="Comparative colonial rule",
    title="French rule in Cameroun: assimilation, association and the indigenat",
    slug="h6-french-rule-assimilation-association",
    minutes=24,
    summary="The French ideals of assimilation and association, the legal categories of citizen and subject, the indigenat and labour tax, French investment and how to compare French rule with British rule.",
    objectives=[
        "Define assimilation and association and explain the gap between them",
        "Describe the indigenat, the status of subject and compulsory labour",
        "Explain the role of chiefs and investment in French Cameroun",
        "Compare French and British rule using clear criteria",
    ],
    key_concepts=["Assimilation", "Association", "Indigenat", "Subject and citizen", "Prestation", "Mise en valeur"],
    blocks=[
        H("Introduction"),
        T("France received the larger part of Kamerun. It governed French Cameroun as a mandate from Yaounde, with its own commissioner, "
          "separate from French Equatorial Africa. France's official ideas about colonies were assimilation and association, and "
          "this lesson asks how they worked in practice."),
        D("The French ideal that colonised peoples could become French in language, culture and law and receive the rights of French citizens. "
          "Very few Africans reached full citizenship before 1945.", title="Assimilation"),
        D("A more practical policy that accepted that colonised societies would remain different and should be ruled with chosen local leaders, "
          "while France kept firm control.", title="Association"),
        D("The French system of special legal rules for 'subjects' (non-citizens), allowing officials to punish minor offences without trial. "
          "In Cameroun it was applied from the 1920s. Check exact dates in your textbook.", title="Indigenat"),
        D("A labour obligation that required subjects to give a number of days of unpaid work each year to the administration, for example on roads.", title="Prestation"),
        H("Citizen and subject"),
        T("Most Cameroonians were 'subjects'. They paid a head tax, had to perform labour, and could be punished under the indigenat. "
          "Only a small educated minority could become citizens. This is why historians say assimilation was an ideal, not a reality."),
        H("Chiefs and the administration"),
        T("French officials appointed and removed chiefs, who acted as agents of the administration: collecting taxes, recruiting labour and passing on orders. "
          "A chief who did not obey could be dismissed. So chiefs held less independent power than under classic British indirect rule."),
        H("Investment and forced labour"),
        T("France invested more than Britain in infrastructure. The Douala to Yaounde railway was completed in the 1920s and the port of Douala was developed. "
          "The plan for 'mise en valeur' (economic development), linked with minister Albert Sarraut, aimed to make colonies productive. Check the date. "
          "Much of this work depended on forced labour, with high death rates on the railway. Cocoa, coffee and other cash crops grew, and France also ran health campaigns "
          "against sleeping sickness, linked to Eugene Jamot."),
        KEY("French and British rule compared", "Use criteria: control, chiefs, law, investment.", cards=[
            ["Control", "France: direct and centralised, separate administration at Yaounde. Britain: indirect, administered from Nigeria."],
            ["Chiefs", "France: agents appointed and dismissed by officials. Britain: Native Authorities with set powers."],
            ["Law and labour", "France: indigenat and prestation. Britain: native courts and taxes; compulsory labour was also used in some forms."],
            ["Investment", "France: more infrastructure. Britain: less, often called neglect."],
        ]),
        EX("Model essay plan 1", intro="'Assimilation was the main feature of French rule in Cameroun.' How far do you agree?", steps=[
            S("Introduction", text="Define assimilation. Judgement: it was an ideal in speeches and schools, but association describes the practice."),
            S("Evidence for assimilation", text="Teaching French; a small group of educated Cameroonians with citizen rights; the idea of a civilising mission."),
            S("Evidence against", text="Most were subjects under the indigenat; chiefs were used as agents; compulsory labour."),
            S("Explanation", text="Citizenship for all would have meant equal rights and costs that France would not accept."),
            S("Judgement", text="In practice France ruled by association and control. Assimilation was mainly a theory."),
        ]),
        EX("Model essay plan 2", intro="Compare the role of chiefs in British and French Cameroons.", steps=[
            S("Similarity", text="Both used chiefs to collect taxes and keep order, since neither had enough officers."),
            S("Difference: powers", text="British Native Authorities had recognised powers and courts; French chiefs were agents who could be dismissed."),
            S("Difference: structure", text="Britain ruled from Nigeria through Native Authorities; France ran a more centralised administration."),
            S("Link", text="Both systems changed the position of chiefs by making them depend on colonial support."),
            S("Judgement", text="Chiefs were more of a partner under British theory, more of an agent under French practice, but in both they served the colonial state."),
        ]),
        MISTAKE("Equating assimilation with equality", "Assimilation promised French identity and rights in theory. In practice most people were subjects."),
        MISTAKE("Quoting numbers of deaths without a source", "Describe the railway labour as costly in lives, but do not give a figure unless your textbook does."),
        QUIZ("Which French legal system allowed officials to punish subjects without trial?",
             ["The mandate", "The indigenat", "The Dual Mandate", "The Berlin Act"], 1,
             "The indigenat was a code of summary punishments for subjects.",
             feedback=["The mandate was a League system.", "", "The Dual Mandate is Lugard's book.", "The Berlin Act dates from 1885."]),
        QUIZ("What was the main difference between assimilation and association?",
             ["Assimilation aimed to make colonised people French; association accepted differences but kept French control", "Association was British, assimilation French", "Assimilation applied only to Britain", "There was no difference"], 0,
             "Assimilation aimed at French identity and rights, association accepted lasting differences.",
             feedback=["", "Both were French policies.", "Assimilation was a French idea.", "They are distinct ideas."]),
        PQ("Explain what is meant by the indigenat.",
           "Outline: A set of special rules for subjects, not citizens, letting officials punish minor offences by fines or imprisonment without trial. It symbolised the gap between the ideal of assimilation and reality."),
        PQ("Why did France invest more than Britain in infrastructure in its share of Cameroon?",
           "Outline: France ruled a larger, more populous and more productive part, with the port of Douala and the Douala-Yaounde railway; the policy of mise en valeur aimed to develop colonies; and France's centralised administration could direct labour. Mention that the work used forced labour."),
        PQ("Compare French and British rule in Cameroon between the wars.",
           "Outline: Similar: use of chiefs, taxation, labour demands, League mandate. Different: France more direct, with the indigenat and more investment; Britain indirect and administered from Nigeria, with less investment. Judgement: different methods with similar outcomes for most Cameroonians."),
        SUM("Assimilation aimed to make colonised people French; association accepted difference but kept French control.",
            "Most Cameroonians were subjects under the indigenat and the labour obligation.",
            "French officials appointed and dismissed chiefs, who acted as agents of the administration.",
            "France invested more than Britain, but with forced labour.",
            "Compare with criteria: control, chiefs, law and labour, investment."),
    ],
))

# ---------------------------------------------------------------------------
# Cameroon 1884-1945 / Social and economic change
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CAM, topic="Social and economic change",
    title="Cash crops, taxes and forced labour in colonial Cameroon",
    slug="h6-forced-labour-and-the-colonial-economy",
    minutes=22,
    summary="How colonial economies drew Cameroonians into cash crops and wage work through taxes and compulsion, the role of the Great Depression and how to weigh costs and benefits.",
    objectives=[
        "Describe the main export crops and plantation work",
        "Explain how taxes and compulsion forced people into the colonial economy",
        "Describe the effects of the 1930s depression on farmers and workers",
        "Weigh costs and benefits of the colonial economy in a balanced judgement",
    ],
    key_concepts=["Cash crop", "Head tax", "Forced labour", "Migrant labour", "Great Depression"],
    blocks=[
        H("Introduction"),
        T("Before colonial rule, Cameroonian households grew food, traded locally and made goods for use. Colonial rule linked them to world markets. "
          "Governments wanted exports and revenue. This lesson asks how people were drawn in, what it cost them and who gained."),
        D("A crop grown mainly to be sold rather than eaten, such as cocoa, palm products, rubber, bananas or coffee.", title="Cash crop"),
        D("A tax charged on each adult regardless of income. It had to be paid in money, so people needed to sell crops or work for wages.", title="Head tax"),
        D("Work that a person is made to perform under threat of punishment, for example porterage, road work or plantation work.", title="Forced labour"),
        H("Ways of drawing people into the economy"),
        T("There were three main methods. First, **taxation**: a head tax in cash pushed people to grow crops for sale or take wage work. "
          "Second, **direct compulsion**: recruitment of workers for plantations and porterage, and, under France, the labour obligation known as prestation. "
          "Third, **incentive**: the chance to earn money from cocoa, palm oil or trade."),
        H("Plantations and migrant labour"),
        T("Plantations near Mount Cameroon grew bananas, rubber, cocoa and palm products. They drew workers from other parts of Cameroon and from Nigeria. "
          "Housing and food were often poor, and hours were long. Workers sometimes left their families for many months."),
        H("Railways, roads and porterage"),
        T("Before roads and railways, goods were carried on the heads of porters. Railways reduced porterage over time, but building them required large work gangs. "
          "Under France the Douala to Yaounde railway was built in the 1920s using forced labour with heavy mortality. Do not use a death figure unless your textbook gives it."),
        H("Farmers and the Great Depression"),
        T("From 1929 world prices for tropical crops fell sharply in the Great Depression. Farmers who sold cocoa or palm products earned less, while taxes were still due. "
          "Many people were forced to work more for the same money. Colonial governments cut spending. The depression showed how exposed Cameroonians were to events far away."),
        KEY("Who gained and who paid?", "Divide the colonial economy by groups.", cards=[
            ["Colonial governments and companies", "Revenue, exports, cheap labour and raw materials."],
            ["Cameroonian farmers and traders", "Some gained income from cocoa and trade; they also faced falling prices, taxes and unfair buying terms."],
            ["Workers", "Wages for some; but heavy labour, poor conditions and family disruption."],
        ]),
        EX("Model essay plan 1", intro="'Taxation was more important than direct force in drawing Cameroonians into the colonial economy.' Discuss.", steps=[
            S("Introduction", text="Define the methods. Judgement: tax was the most widespread tool, but force was decisive in plantations and railways."),
            S("Tax", text="A cash head tax applied to most adults; forced the sale of crops or labour."),
            S("Force", text="Recruited labour for plantations; prestation; railway building."),
            S("Incentives", text="Cocoa and trade offered income, so some people joined voluntarily."),
            S("Judgement", text="Tax created the need for cash; force supplied labour where incentives were not enough."),
        ]),
        EX("Model essay plan 2", intro="Assess the impact of the Great Depression on Cameroon in the 1930s.", steps=[
            S("Introduction", text="Define the depression and the dependence on exports. Judgement: it brought hardship and showed the weakness of an export economy."),
            S("Prices and incomes", text="World prices for crops fell; farmers earned less."),
            S("Taxes and labour", text="Taxes stayed, so people worked more or borrowed."),
            S("Government response", text="Public spending was reduced; less investment."),
            S("Judgement", text="Hardship was widespread; the lesson of dependence on world markets was learned."),
        ]),
        MISTAKE("Using dramatic statistics from memory", "Do not invent figures for deaths or workers. Describe scale carefully."),
        MISTAKE("Ignoring Cameroonian choices", "Many farmers chose to grow cocoa because it paid. Explain choice and pressure together."),
        QUIZ("Why did a cash head tax push people into the colonial economy?",
             ["It had to be paid in money, so people needed to sell crops or work for wages", "It was paid in food", "It was paid only by chiefs", "It was abolished in the 1920s"], 0,
             "A tax payable in money meant people needed cash.",
             feedback=["", "The tax was in money.", "It applied to ordinary adults.", "It was a long-lasting feature of colonial rule."]),
        QUIZ("What effect did the Great Depression have on Cameroonian farmers?",
             ["World prices for their crops fell while taxes stayed", "Prices rose", "Taxes were abolished", "Plantations closed everywhere"], 0,
             "Falling prices and constant taxes squeezed farmers.",
             feedback=["", "Prices fell.", "Taxes continued.", "Plantations continued."]),
        PQ("Explain two ways in which colonial governments forced Cameroonians to work.",
           "Outline: (1) Recruitment for plantations and porterage under pressure. (2) Compulsory labour obligations such as prestation under France, used for roads and railways. Mention that tax created further pressure."),
        PQ("How did the Great Depression affect colonial Cameroon?",
           "Outline: Crop prices fell, incomes dropped, taxes continued, public spending was cut. Farmers and workers faced hardship; the export economy showed its weakness."),
        PQ("To what extent did Cameroonians benefit from the colonial economy before 1945?",
           "Outline: Benefits: cash income from cocoa and trade; roads, railways and ports; wage work. Costs: taxes, forced labour, land loss, low prices. Judgement: benefits were uneven and mostly served colonial interests."),
        SUM("Colonial governments drew Cameroonians into the economy by taxes, compulsion and incentives.",
            "Plantations used migrant and recruited labour; railways relied on forced labour.",
            "The Great Depression cut crop prices while taxes continued.",
            "Weigh benefits and costs by group: governments, farmers, workers.",
            "Do not invent statistics."),
    ],
))

LESSONS.append(lesson(
    module=M_CAM, topic="Social and economic change",
    title="Schools, the press and the first associations",
    slug="h6-schools-press-and-first-associations",
    minutes=22,
    summary="How mission and government schools, the early press, petitions and associations such as Jeucafra created an educated elite and a political voice before 1945.",
    objectives=[
        "Describe the missions and schools active in Cameroon before 1945",
        "Explain how language policy differed under German, British and French rule",
        "Explain the role of the press and petitions",
        "Explain why Jeucafra was founded and how it later mattered",
    ],
    key_concepts=["Mission school", "Evolue", "Petition", "Press", "Jeucafra", "Unikamerun"],
    blocks=[
        H("Introduction"),
        T("Colonial rule created a small group of Cameroonians who could read, write and work in European languages. "
          "They were teachers, clerks, interpreters, traders and pastors. After 1945 many of them led political movements. This lesson asks how that group formed and what it did before 1945."),
        D("A school run by a Christian mission, teaching reading, writing, counting and religion, and often a trade or farm work.", title="Mission school"),
        D("A formal request or complaint signed by a person or group and sent to an authority. Under the mandate system, inhabitants could petition the League of Nations.", title="Petition"),
        H("Missions and schools"),
        T("Missionaries ran most schools. The English Baptist Alfred Saker worked in Douala and founded Victoria in 1858. "
          "The Basel Mission took over Baptist work in the 1880s and the Catholic Pallottine Fathers arrived in 1890. American Presbyterians worked in the south. "
          "Under France, other Catholic and Protestant missions worked. Check your textbook for dates and places."),
        T("Schools brought literacy and Christianity. They also changed how young people saw local customs and authority. "
          "Some missions criticised local practices; this caused tension. Many students came from families near mission stations or towns."),
        H("Language policy"),
        T("Under Germany, German was promoted, with mission schools often teaching in African languages as well. "
          "Under France, French was the required language of instruction and mission schools had to teach it. "
          "In the British Cameroons, English and local languages were used. These choices shaped the later divide between English-speaking and French-speaking Cameroon."),
        H("Press and petitions"),
        T("Literate people in towns such as Douala began to produce and read newspapers, circulars and petitions. "
          "During the mandate period, Cameroonians sent petitions to the League of Nations about land, taxes and labour. "
          "The petitions gave a public voice to educated and urban Cameroonians. Check names of petitioners and newspapers in your textbook."),
        H("Associations: Jeucafra and Unikamerun"),
        T("In 1938 the French authorities encouraged the creation of Jeucafra (Jeunesse camerounaise francaise), partly to counter German claims "
          "for the return of its former colonies. Educated Cameroonians such as Paul Soppo Priso were involved. "
          "Though sponsored by the French, it gave members experience of organisation. Unikamerun is named in the outline as an early movement; check its founding date, founders and aims in your textbook before you use details."),
        KEY("Why associations mattered", "Three effects to remember.", cards=[
            ["Training", "Members learned committee work, debate and political organisation."],
            ["Networks", "Educated Cameroonians from different towns met and exchanged ideas."],
            ["Link to 1945", "After the Second World War many members joined or founded political parties."],
        ]),
        EX("Model essay plan 1", intro="Assess the importance of mission education in the political awakening of Cameroonians before 1945.", steps=[
            S("Introduction", text="Define mission education and political awakening. Judgement: schools created the people able to organise, but political change also needed other factors."),
            S("Skills and ideas", text="Literacy, new languages, Christian ideas of equality, access to newspapers and petitions."),
            S("Elite formation", text="Teachers, clerks and pastors formed a small educated class."),
            S("Other factors", text="Urban growth, forced labour and taxes, and the experience of the mandate system."),
            S("Judgement", text="Education supplied the leaders; grievances supplied the reasons."),
        ]),
        EX("Model essay plan 2", intro="Explain why Jeucafra was founded in 1938 and how far it was a nationalist body.", steps=[
            S("Introduction", text="Context: German colonial demands in the late 1930s. Judgement: founded by France to show loyalty, but it later provided experience for nationalists."),
            S("Why founded", text="France wanted to show that Cameroonians preferred France over Germany."),
            S("Who joined", text="Educated urban Cameroonians who saw a chance for a voice."),
            S("Nationalism", text="It was not nationalist at the start; it did not call for independence."),
            S("Judgement", text="A step towards organised politics, not yet nationalism."),
        ]),
        MISTAKE("Calling Jeucafra anti-colonial", "It began as a pro-French body under French encouragement. Explain the later importance."),
        MISTAKE("Listing missions without effects", "Link each mission to schools and to the type of person it trained."),
        QUIZ("Why did France encourage Jeucafra in 1938?",
             ["To prepare independence", "To show Cameroonian support for France against German claims", "To unite British and French Cameroons", "To abolish the indigenat"], 1,
             "Jeucafra was meant to show loyalty to France when Germany claimed its old colonies.",
             feedback=["France had no independence plan.", "", "France did not seek reunification.", "The indigenat was not abolished by Jeucafra."]),
        QUIZ("Which was one effect of language policy in schools?",
             ["It created a later divide between English-speaking and French-speaking areas", "It made one language official everywhere", "It banned mission schools", "It ended petitions"], 0,
             "Different policies in the British and French parts shaped later divisions.",
             feedback=["", "Languages differed by zone.", "Missions continued.", "Petitions continued."]),
        PQ("Explain two ways in which mission schools changed Cameroonian society.",
           "Outline: (1) They produced literate people who became teachers, clerks and pastors. (2) They spread Christianity and European languages, which sometimes weakened local customs. Give a named mission."),
        PQ("Why were petitions to the League of Nations important?",
           "Outline: They allowed Cameroonians to protest about land, taxes and labour to an international body. They showed an educated political voice and set a precedent for later appeals to the United Nations."),
        PQ("To what extent was Jeucafra a step towards nationalism?",
           "Outline: Against: founded under French encouragement, pro-French. For: gave educated Cameroonians organisational experience and public roles; many later nationalists came from similar groups. Judgement: a step towards politics but not nationalism in itself."),
        SUM("Missions ran most schools and trained teachers, clerks and pastors.",
            "Language policy differed under German, British and French rule.",
            "Petitions to the League and the early press gave educated people a public voice.",
            "Jeucafra (1938) began as a pro-French body; check Unikamerun details in your textbook.",
            "Associations trained people for the politics that followed 1945."),
    ],
))

# ---------------------------------------------------------------------------
# European Revolutions & Unifications / 1848 revolutions
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_EUR, topic="1848 revolutions",
    title="Why 1848? Causes, ideas and the three ideologies",
    slug="h6-1848-causes-and-ideologies",
    minutes=22,
    summary="The long-term and short-term causes of the 1848 revolutions, with liberalism, nationalism and socialism explained, and a method for ranking causes in an essay.",
    objectives=[
        "Explain the political order set up in 1815 and why many people resented it",
        "Explain the economic crisis of 1845 to 1848",
        "Distinguish liberalism, nationalism and socialism",
        "Rank causes and justify the ranking",
    ],
    key_concepts=["Congress of Vienna", "Metternich system", "Liberalism", "Nationalism", "Socialism", "Trigger"],
    blocks=[
        H("Introduction"),
        T("In early 1848 revolts broke out in Paris, Vienna, Berlin, Milan, Budapest and other cities. Why did so many happen within a few weeks? "
          "Historians separate **long-term causes** (conditions that built up over years) from **triggers** (events that set off the explosion).\n\n"
          "This lesson covers causes. The next lesson covers events and failure."),
        D("The peace settlement of 1814 to 1815 after the Napoleonic wars. The great powers restored monarchs, set up a balance of power and tried to prevent new revolutions. "
          "Prince Metternich of Austria was its leading defender.", title="Congress of Vienna"),
        H("The old order and its critics"),
        T("After 1815 the rulers of Austria, Prussia and Russia tried to stop liberal and national ideas by censorship, police and control of universities. "
          "In the German states and Italy this was called the Metternich system. It kept many people from forming parties, writing freely or voting."),
        KEY("Three ideas that challenged the old order", "Learn the difference between them.", cards=[
            ["Liberalism", "Constitutions, elected parliaments, rule of law, freedom of speech and press, protection of property. Supported mainly by the educated middle classes."],
            ["Nationalism", "Each nation, defined by language, culture and history, should govern itself. Inspired Germans, Italians, Hungarians, Czechs and others."],
            ["Socialism", "Society and the economy should be organised for the benefit of working people. Ideas ranged from state workshops to Marx and Engels, who published the Communist Manifesto in early 1848."],
        ], note="Liberals and nationalists often worked together; many liberals feared socialism."),
        T("Nationalism could unite or divide. In the German states it argued for a united Germany. In the Austrian Empire, where Germans, Hungarians, Czechs, Italians, Croats and others lived together, "
          "nationalism threatened to break the empire apart."),
        H("Economic and social pressures"),
        T("A population rise and the growth of towns left many people without work. In 1845 to 1847 poor harvests and the potato disease raised food prices sharply. "
          "A commercial and industrial slump followed in 1846 to 1847, which brought unemployment in towns. Hungry workers and frustrated middle classes had a common enemy: the government."),
        H("Triggers"),
        T("In France the government of Louis-Philippe banned a reform banquet in Paris in February 1848, and protests turned into revolution. "
          "News of the fall of the French king spread quickly by newspaper and telegraph and sparked revolts in Vienna, Berlin and the Italian states in March. "
          "Check the exact dates in your textbook."),
        EX("Model essay plan 1", intro="Assess the relative importance of economic and political causes in producing the revolutions of 1848.", steps=[
            S("Introduction", text="Define the two types. Judgement: economic distress explains the timing and the crowds; political ideas explain the aims."),
            S("Economic causes", text="Harvest failure 1845 to 1847; food prices; slump and unemployment; poor living conditions in towns."),
            S("Political causes", text="Resentment of the Metternich system; liberal demands for constitutions; nationalism in Germany, Italy and Hungary."),
            S("Link", text="Hunger gave liberals a mass audience; liberal ideas gave the hungry a programme."),
            S("Judgement", text="Both were needed; economic crisis was the trigger and politics the direction."),
        ]),
        EX("Model essay plan 2", intro="Explain why nationalism was a threat to the Austrian Empire.", steps=[
            S("Point 1: many nationalities", text="The empire included Germans, Hungarians, Czechs, Italians, Croats and others. Each national movement could demand self-government."),
            S("Point 2: Habsburg weakness", text="The ruler depended on a loyal army and a small group of officials. Fiscal and political reforms were resisted."),
            S("Point 3: example", text="Hungarian demands in 1848 and Italian revolts in Lombardy and Venice show nationalism challenging the empire."),
            S("Link", text="The empire's survival depended on dividing national movements."),
        ]),
        MISTAKE("Listing causes without ranking", "A Level essays need a judgement: which cause mattered most, and why? Use 'more important because'."),
        MISTAKE("Treating all liberals as radicals", "Most liberals wanted constitutions under monarchs, not republics, and many feared workers' demands."),
        QUIZ("Which statement best defines liberalism in 1848?",
             ["Belief in absolute rule by a monarch", "Belief in constitutional government, an elected parliament and the rule of law", "Belief that workers should own all property", "Belief in a single language for Europe"], 1,
             "Liberalism supported constitutions, elected parliaments, law and freedoms.",
             feedback=["That is absolutism.", "", "That is closer to socialism.", "That is not liberalism."]),
        QUIZ("Which event is best described as a trigger rather than a long-term cause?",
             ["The Congress of Vienna", "The ban on a reform banquet in Paris in February 1848", "The growth of the middle classes", "The spread of nationalism"], 1,
             "The banquet ban set off the Paris revolution.",
             feedback=["A long-term settlement of 1815.", "", "A long-term development.", "A long-term idea."]),
        PQ("Explain two ways in which economic conditions helped cause the revolutions of 1848.",
           "Outline: (1) Poor harvests and potato disease in 1845 to 1847 raised food prices and caused hunger. (2) A slump in trade and industry caused unemployment in towns. Link both to crowds in the streets."),
        PQ("Distinguish between liberalism and nationalism.",
           "Outline: Liberalism is about the form of government (constitution, rights). Nationalism is about who governs whom (a nation's right to its own state). They overlap in Germany and Italy, but could conflict in the Austrian Empire."),
        PQ("Which was more important in causing the 1848 revolutions: ideas or economic hardship? Explain.",
           "Outline: Hardship brought people into the streets and explains the timing; ideas gave direction and leaders. Judgement: neither alone would have produced a European wave."),
        SUM("The Congress of Vienna order and the Metternich system angered liberals and nationalists.",
            "Liberalism sought constitutions; nationalism sought national states; socialism sought social change.",
            "Harvest failure and slump in 1845 to 1848 caused hardship.",
            "In France, a banned banquet triggered revolution in February 1848.",
            "Rank causes and justify your ranking."),
    ],
))

LESSONS.append(lesson(
    module=M_EUR, topic="1848 revolutions",
    title="The course of 1848 in France, the German states and the Austrian Empire",
    slug="h6-1848-course-and-failure",
    minutes=26,
    summary="A step-by-step account of the revolutions in France, the German states, the Austrian Empire and Italy, and the reasons for failure, with a balanced view of what survived.",
    objectives=[
        "Outline the events in France, the German states and the Austrian Empire",
        "Explain the role of the Frankfurt Parliament and its failure",
        "Explain how the Habsburgs recovered",
        "Judge the reasons for failure and the lasting results",
    ],
    key_concepts=["Second Republic", "June Days", "Frankfurt Parliament", "Counter-revolution", "Serfdom"],
    blocks=[
        H("Introduction"),
        T("The revolutions of 1848 spread fast, and by 1849 most had been defeated. This lesson follows the main stages and asks why the revolutionaries lost, "
          "and what survived."),
        H("France"),
        T("In February 1848 (22 to 24 February) Louis-Philippe abdicated and a republic was declared. The new government introduced universal male suffrage and set up National Workshops to give work to the unemployed. "
          "In April, elections returned a moderate majority. In June the government closed the Workshops. Workers rose in the **June Days** (23 to 26 June) and were crushed by the army."),
        T("In December 1848 Louis-Napoleon Bonaparte, nephew of Napoleon I, won the presidential election. In December 1851 he seized power, and in 1852 he became Emperor Napoleon III."),
        H("The German states"),
        T("In March 1848 rulers in several German states gave concessions, and the king of Prussia, Frederick William IV, promised reforms after street fighting in Berlin. "
          "An assembly met at Frankfurt from May 1848 (the Frankfurt Parliament) to draft a constitution for a united Germany."),
        T("The deputies argued over the shape of the new Germany: a 'big German' solution including Austria, or a 'little German' one led by Prussia without Austria. "
          "In April 1849 the Parliament offered the imperial crown to Frederick William IV, who refused it, saying that it came from an assembly, not from princes. "
          "Without a ruler's support and army the Parliament collapsed."),
        H("The Austrian Empire and Italy"),
        T("In March 1848 Metternich resigned and left Vienna. Revolts broke out in Vienna, Budapest, Prague and Milan. The Habsburgs recovered step by step. "
          "In June, Prague was bombarded; in autumn, Vienna was retaken; in December, the young Franz Joseph became emperor. "
          "Hungary's revolution under Lajos Kossuth was crushed in 1849 with Russian help."),
        T("In Italy, the king of Piedmont-Sardinia, Charles Albert, fought Austria in 1848 and 1849 and was defeated. A Roman Republic led by Mazzini and defended by Garibaldi was ended by French troops in 1849. "
          "Check the dates in your textbook."),
        H("Why did the revolutions fail?"),
        KEY("Four explanations", "Link them rather than list them.", cards=[
            ["Divisions", "Middle-class liberals were afraid of workers; nationalities fought each other; Frankfurt could not agree on its boundaries."],
            ["The army", "Most armies stayed loyal to rulers and were used to recover control."],
            ["Foreign help and weak revolutionary armies", "Russian troops in Hungary; French troops in Rome."],
            ["Economic recovery", "Better harvests from 1848 reduced hunger and anger."],
        ]),
        H("What survived?"),
        T("Not everything was lost. Serfdom was ended in the Austrian Empire. French men kept the vote for some years. In Prussia, the king issued a constitution in 1848 to 1849 with an unequal voting system. "
          "The idea of national unity and constitutional government remained, and later leaders achieved unification by different means."),
        EX("Model essay plan 1", intro="'The revolutions of 1848 failed because the revolutionaries could not agree.' How far do you agree?", steps=[
            S("Introduction", text="Define the failure. Judgement: division was the main internal weakness, but loyal armies decided the outcome."),
            S("Division", text="June Days in France; Frankfurt debates; national conflicts in the Austrian Empire."),
            S("Armies", text="Armies stayed loyal and were used to recover control in Vienna, Prague, Berlin and Hungary."),
            S("Other factors", text="Russian aid; French intervention in Rome; economic recovery."),
            S("Judgement", text="Division gave rulers the time to recover; the army made recovery possible."),
        ]),
        EX("Model essay plan 2", intro="Compare the outcomes of the 1848 revolutions in France and the Austrian Empire.", steps=[
            S("Similarity", text="Initial success followed by a conservative recovery; both ended under strong rulers (Napoleon III and Franz Joseph)."),
            S("Difference: regime", text="France ended a monarchy and created a republic that became an empire; Austria kept its dynasty."),
            S("Difference: lasting change", text="Austria ended serfdom; France kept universal male suffrage for a time."),
            S("Difference: foreign factors", text="Russian troops helped the Habsburgs in Hungary."),
            S("Judgement", text="Both returned to authority, but in different forms."),
        ]),
        MISTAKE("Saying that Frankfurt failed because it was too radical", "Most of its members were moderate. It failed for lack of a ruler's support and army."),
        MISTAKE("Mixing up the date of the Frankfurt crown refusal", "The offer and refusal were in April 1849, almost a year after the Parliament opened."),
        QUIZ("Why did the Frankfurt Parliament collapse?",
             ["Russia invaded Frankfurt", "Frederick William IV refused the crown and the rulers kept their armies", "Bismarck dissolved it", "Napoleon III forced it to close"], 1,
             "Without a ruler's support and army the Parliament could not enforce its plans.",
             feedback=["Russia helped the Habsburgs in Hungary.", "", "Bismarck was not yet in power.", "Napoleon III was not emperor in 1849."]),
        QUIZ("Which was a lasting result of 1848 in the Austrian Empire?",
             ["The end of serfdom", "The end of the Habsburg dynasty", "The creation of a republic", "The independence of Hungary"], 0,
             "Serfdom was ended; the dynasty survived.",
             feedback=["", "The Habsburgs survived.", "No republic was created.", "Hungary was defeated in 1849."]),
        PQ("Explain two reasons why the revolution in France became more radical and then failed in 1848.",
           "Outline: (1) The closing of the National Workshops led to the June Days. (2) Fear of social revolution turned moderate republicans and the middle classes towards order, helping Louis-Napoleon win the December election."),
        PQ("Describe the work of the Frankfurt Parliament.",
           "Outline: Met from May 1848 to draft a constitution for a united Germany; debated whether to include Austria; offered the crown to Frederick William IV in April 1849; collapsed after his refusal."),
        PQ("How far had the revolutions of 1848 achieved nothing by 1850?",
           "Outline: Failure: most governments restored, nationalists defeated. Achievements: serfdom ended in Austria; constitutions in some states; ideas remained for the future. Judgement: failed in their main aims but left lasting changes."),
        SUM("France: Second Republic, June Days, Louis-Napoleon president in December 1848 and emperor in 1852.",
            "Germany: Frankfurt Parliament opened in May 1848; the crown was refused in April 1849.",
            "Austria: Metternich fell, but the Habsburgs recovered by force, with Russian help in Hungary.",
            "Failure came from division, loyal armies, foreign help and economic recovery.",
            "Some changes lasted, such as the end of serfdom in Austria."),
    ],
))

# ---------------------------------------------------------------------------
# European Revolutions & Unifications / Italian and German unification
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_EUR, topic="Italian and German unification",
    title="Italian unification step by step, 1859-1870",
    slug="h6-italian-unification-stages",
    minutes=24,
    summary="The stages of Italian unification: Cavour's diplomacy, the war of 1859, Garibaldi's expedition of 1860, the Kingdom of Italy in 1861 and the later gains of Venetia and Rome, with the roles of foreign help.",
    objectives=[
        "Outline the stages of unification in order",
        "Explain Cavour's aims and methods",
        "Explain the role of Garibaldi and his relationship with Cavour",
        "Judge the importance of foreign help",
    ],
    key_concepts=["Piedmont-Sardinia", "Plombieres", "Villafranca", "Garibaldi and the Thousand", "Plebiscite", "Risorgimento"],
    blocks=[
        H("Introduction"),
        T("Italy in the 1850s was divided into several states, with Austria strong in the north and the Pope ruling Rome. After the failures of 1848 and 1849, "
          "the kingdom of Piedmont-Sardinia became the main hope of nationalists. Between 1859 and 1870 Italy was united. "
          "This lesson goes through the stages in order, so that you can place every event in a chain of cause and effect."),
        IMG("al-h6-unification-timeline.svg", alt="Timeline from 1859 to 1871 showing stages of Italian and German unification", caption="Figure 1. Italian and German unification on one line. Not to scale."),
        D("The movement and period of Italian national revival, leading to unification. The word means 'resurgence' or 'rising again'.", title="Risorgimento"),
        D("A vote by the people of a territory on a question such as joining another state. In 1860 plebiscites were held in central Italy and in Sicily and Naples.", title="Plebiscite"),
        H("Cavour and the road to war, 1852-1859"),
        T("Count Camillo di Cavour became prime minister of Piedmont in 1852. He improved the economy and army. He sent troops to the Crimean War (1855) to win a place at the peace conference and the goodwill of Britain and France. "
          "In July 1858 he met Napoleon III at Plombieres and made a secret agreement: France would help Piedmont against Austria; in return Piedmont would give Nice and Savoy."),
        T("In 1859 war began. French and Piedmontese forces won at Magenta and Solferino. Then Napoleon III made a separate peace at Villafranca (July 1859). Piedmont gained Lombardy, but not Venetia."),
        H("1860: Garibaldi and the south"),
        T("In 1860 the central Italian states voted in plebiscites to join Piedmont. In May Giuseppe Garibaldi sailed from near Genoa with about a thousand volunteers, known as the Thousand, and landed in Sicily. "
          "He conquered Sicily and then crossed to the mainland and took Naples. Cavour feared that Garibaldi would attack Rome and bring in the French, so he sent the Piedmontese army south through the Papal States. "
          "Garibaldi handed over his conquests to King Victor Emmanuel II. In March 1861 the Kingdom of Italy was proclaimed. Cavour died in June 1861."),
        H("Venetia and Rome"),
        T("Italy won Venetia in 1866 by allying with Prussia against Austria. It occupied Rome in 1870 after French troops left to fight the Franco-Prussian War. "
          "Rome became the capital in 1871. The unification therefore took about twelve years and relied heavily on other powers' actions."),
        KEY("Who made Italy?", "Different historians stress different people.", cards=[
            ["Cavour", "Diplomacy, alliance with France, the 1859 war and annexations. Some historians say he did not plan a united Italy from the start."],
            ["Garibaldi", "A volunteer army that conquered the south, creating a united Italy larger than Cavour planned."],
            ["Foreign powers", "France in 1859, Prussia in 1866, the Franco-Prussian War in 1870."],
        ]),
        EX("Model essay plan 1", intro="'Italian unification was achieved mainly by foreign help.' How far do you agree?", steps=[
            S("Introduction", text="Define unification and foreign help. Judgement: foreign help was essential at every stage, but Italian leaders used it skilfully."),
            S("Foreign help", text="France in 1859; Prussia in 1866; French withdrawal from Rome in 1870."),
            S("Italian action", text="Cavour's diplomacy and reforms; Garibaldi's expedition; plebiscites showing popular support."),
            S("Evaluation", text="Foreign help created openings, but Italians had to exploit them."),
            S("Judgement", text="Italy was made by Italians in a favourable international situation."),
        ]),
        EX("Model essay plan 2", intro="Compare the contributions of Cavour and Garibaldi to Italian unification.", steps=[
            S("Cavour", text="Diplomacy; Plombieres; war of 1859; annexation of central states; sending the army south."),
            S("Garibaldi", text="Expedition of the Thousand; conquest of Sicily and Naples; popular appeal."),
            S("Relationship", text="They disagreed, but their actions combined; Garibaldi handed over to Victor Emmanuel."),
            S("Judgement", text="Neither could have achieved unity alone."),
        ]),
        MISTAKE("Saying Italy was complete in 1861", "Venetia joined in 1866 and Rome in 1870. Keep each stage separate."),
        MISTAKE("Calling Cavour a nationalist who planned a united Italy from the start", "Historians debate this. Say that Cavour's aims changed with events."),
        QUIZ("What did Piedmont promise France at Plombieres?",
             ["Venetia", "Nice and Savoy", "Rome", "Sicily"], 1,
             "In return for French help against Austria, Piedmont agreed to give Nice and Savoy.",
             feedback=["Venetia was Austrian until 1866.", "", "Rome was the Pope's.", "Sicily was taken by Garibaldi."]),
        QUIZ("Why did Cavour send the Piedmontese army through the Papal States in 1860?",
             ["To attack Naples directly", "To stop Garibaldi attacking Rome and to take control of the south", "To help Austria", "To defend Venice"], 1,
             "He wanted to stop Garibaldi and prevent French intervention.",
             feedback=["The aim was control and prevention.", "", "Austria was Piedmont's enemy.", "Venetia was still Austrian."]),
        PQ("Explain two reasons why Piedmont was able to take the lead in Italian unification.",
           "Outline: (1) It had a constitution, a modernising economy and army, and the leadership of Cavour. (2) It had the support of France in 1859 and the sympathy of nationalists after 1848."),
        PQ("Describe the main stages of unification between 1859 and 1870.",
           "Outline: 1859 war and Lombardy; 1860 plebiscites and Garibaldi's expedition; 1861 Kingdom of Italy; 1866 Venetia; 1870 Rome."),
        PQ("Assess the importance of Garibaldi to Italian unification.",
           "Outline: He conquered the south and created a larger Italy than Cavour planned; his expedition showed popular support. But the Piedmontese army took control and French and Prussian actions mattered. Judgement: very important, but not alone."),
        SUM("Cavour built Piedmont and made the Plombieres agreement with Napoleon III in 1858.",
            "The 1859 war gave Lombardy; plebiscites in 1860 added central Italy.",
            "Garibaldi's expedition of 1860 added Sicily and Naples; the Kingdom of Italy was proclaimed in 1861.",
            "Venetia came in 1866 and Rome in 1870, both through other powers' wars.",
            "Foreign help was essential at every stage."),
    ],
))

LESSONS.append(lesson(
    module=M_EUR, topic="Italian and German unification",
    title="German unification: Bismarck's three wars, 1862-1871",
    slug="h6-german-unification-three-wars",
    minutes=26,
    summary="The stages of German unification from the Zollverein and Bismarck's appointment through the wars of 1864, 1866 and 1870 to the proclamation of the empire in 1871, and the effects on Europe.",
    objectives=[
        "Explain Prussia's economic and military advantages before 1862",
        "Outline the wars of 1864, 1866 and 1870 and their results",
        "Explain the role of diplomacy, including the Ems telegram",
        "Explain the effects of unification on the balance of power",
    ],
    key_concepts=["Zollverein", "Realpolitik", "Schleswig-Holstein", "Konigsgratz", "Ems telegram", "North German Confederation"],
    blocks=[
        H("Introduction"),
        T("After the failure of 1848 and 1849, Prussia and Austria competed for leadership of the German states. In twenty years Prussia defeated Austria and France and created a German Empire. "
          "This lesson follows the three wars and asks how much came from planning and how much from chance."),
        D("A customs union of German states set up in 1834 under Prussian leadership. It excluded Austria and tied the economies of many states to Prussia.", title="Zollverein"),
        D("Politics based on practical power and interest rather than moral ideals. It is often linked with Bismarck.", title="Realpolitik"),
        H("Prussia before Bismarck"),
        T("By 1860 Prussia was the strongest economy in the German states, with coal, iron and railways. King William I wanted a larger army, and the Prussian parliament refused the money. "
          "In 1862 the king appointed Otto von Bismarck as minister-president. Bismarck ran the government without parliament's budget and said that great questions would be decided by 'iron and blood'. "
          "This is a paraphrase; check the exact words and context in your textbook."),
        H("The war with Denmark, 1864"),
        T("Prussia and Austria together defeated Denmark in 1864 over Schleswig and Holstein. Disputes over how to run the duchies then led to tension, and the Convention of Gastein (1865) postponed a solution."),
        H("The war with Austria, 1866"),
        T("Bismarck made sure that Austria was isolated: France stayed neutral, Russia was friendly, and Italy allied with Prussia. In June 1866 war began. "
          "At Konigsgratz (Sadowa) on 3 July 1866 Prussia won a decisive victory. Prussia's generals (Moltke) used railways and modern rifles. "
          "Peace was made quickly and mildly: Austria lost no territory to Prussia but was excluded from German affairs. In 1867 the North German Confederation was formed under Prussian leadership."),
        H("The war with France, 1870-1871"),
        T("In 1870 a crisis arose over a possible Hohenzollern candidate for the Spanish throne. Bismarck edited a telegram from the king's resort town of Ems so that it looked like an insult to France. "
          "France declared war on 19 July 1870. The southern German states joined Prussia. Napoleon III was defeated and captured at Sedan in September. Paris was besieged. "
          "On 18 January 1871 the German Empire was proclaimed at Versailles, with William I as emperor. Germany took Alsace and part of Lorraine and demanded an indemnity."),
        KEY("Effects on Europe", "Unification changed the balance of power.", cards=[
            ["Germany", "The strongest power on the continent, with a fast-growing industry."],
            ["France", "Humiliated, resentful, wanting Alsace and Lorraine back."],
            ["Austria", "Excluded from Germany and turned towards the Balkans."],
            ["The system of alliances", "Bismarck built alliances to keep France isolated, shaping European diplomacy until 1890."],
        ]),
        EX("Model essay plan 1", intro="Assess the importance of Bismarck in the unification of Germany.", steps=[
            S("Introduction", text="Define the period. Judgement: Bismarck was skilful and decisive, but Prussian economic and military power gave him the means."),
            S("Bismarck's role", text="Appointed in 1862; isolated Austria and France; used the Ems telegram; kept the wars short and limited."),
            S("Other factors", text="Zollverein and industry; Moltke and Roon's army; mistakes by Austria and France; nationalism in the south."),
            S("Evaluation", text="Bismarck exploited opportunities; he did not create all of them."),
            S("Judgement", text="Bismarck was the architect of the timing and method, not the sole cause."),
        ]),
        EX("Model essay plan 2", intro="Explain why Prussia defeated Austria in 1866.", steps=[
            S("Point 1: military", text="Reformed army, railways, modern rifles and Moltke's planning."),
            S("Point 2: diplomacy", text="Austria isolated: Italy allied with Prussia, France stayed neutral."),
            S("Point 3: economic", text="Prussian industry and the Zollverein."),
            S("Link", text="Prussia combined strength and diplomacy."),
        ]),
        MISTAKE("Dating unification as 1866", "1866 made the North German Confederation. The empire was proclaimed on 18 January 1871."),
        MISTAKE("Writing about Bismarck as if he controlled every event", "He reacted to events and used them. Use words like 'exploited' and give evidence."),
        QUIZ("Where was the German Empire proclaimed on 18 January 1871?",
             ["Berlin", "Versailles", "Vienna", "Frankfurt"], 1,
             "It was proclaimed at the Palace of Versailles, near Paris.",
             feedback=["Berlin was the Prussian capital.", "", "Vienna was the Austrian capital.", "Frankfurt hosted the 1848 Parliament."]),
        QUIZ("What was the main result of the war of 1866?",
             ["Prussia took over Austria", "Austria was excluded from German affairs and the North German Confederation was formed", "Denmark gained the duchies", "France gained Alsace"], 1,
             "Austria was excluded and Prussia led the Confederation.",
             feedback=["Austria remained independent.", "", "Denmark lost the duchies in 1864.", "Germany took Alsace in 1871."]),
        PQ("Explain two ways in which Bismarck used diplomacy in the unification of Germany.",
           "Outline: (1) Isolating Austria in 1866 by securing Italian alliance and French neutrality. (2) In 1870 using the Ems telegram to make France appear the aggressor and bringing the southern states to Prussia's side."),
        PQ("Describe the stages of German unification between 1862 and 1871.",
           "Outline: 1862 Bismarck; 1864 Denmark; 1866 Austria and Konigsgratz; 1867 North German Confederation; 1870 France and Sedan; 1871 empire proclaimed at Versailles."),
        PQ("How far did German unification change the balance of power in Europe?",
           "Outline: Germany became the leading continental power; France was hostile; Austria turned to the Balkans; alliance system developed. Judgement: a major change that shaped European politics until 1914."),
        SUM("The Zollverein and Prussian industry gave Prussia economic strength.",
            "Bismarck became minister-president in 1862 and fought wars in 1864, 1866 and 1870.",
            "Konigsgratz (3 July 1866) led to the North German Confederation in 1867.",
            "The empire was proclaimed at Versailles on 18 January 1871.",
            "Unification made Germany dominant and left France hostile."),
    ],
))

LESSONS.append(lesson(
    module=M_EUR, topic="Italian and German unification",
    title="Source skills: comparing historians on Bismarck",
    slug="h6-comparing-historians-on-bismarck",
    minutes=24,
    summary="How to compare historians' interpretations of Bismarck (master planner, opportunist, structural forces), how to explain why they differ and how to use them in an essay.",
    objectives=[
        "Distinguish three broad interpretations of Bismarck",
        "Explain why historians differ (evidence, period, purpose, approach)",
        "Compare two invented interpretation extracts using a clear method",
        "Use historiography in an essay without name-dropping",
    ],
    key_concepts=["Historiography", "Interpretation", "Master plan", "Opportunist", "Structural factors"],
    blocks=[
        H("Introduction"),
        T("Historians do not just tell the same story. They ask different questions, use different evidence and live in different times. "
          "Comparing historians' interpretations is a major A Level skill. In this lesson we use Bismarck because the debate about him is a classic example.\n\n"
          "The extracts in this lesson are **invented by KKEVO to illustrate views. They are not quotations from any real historian.**"),
        D("The study of how history has been written: the different interpretations that historians have given and why they differ.", title="Historiography"),
        D("An explanation of events that is argued from evidence. Two historians can use the same facts and reach different interpretations.", title="Interpretation"),
        H("Three broad views of Bismarck"),
        KEY("Master planner, opportunist, structures", "Learn the idea of each, not just the names.", cards=[
            ["Master planner", "Bismarck knew where he was going from the start and planned the three wars. This view was common in German national writing after 1871, and Bismarck's own memoirs presented his career this way."],
            ["Opportunist", "Bismarck responded to events and kept options open. A.J.P. Taylor is often linked with a view of Bismarck as a flexible improviser. Check the books in your textbook."],
            ["Structural forces", "Long-term economic and social forces, such as industrial growth and the Zollverein, made Prussian leadership likely; Bismarck steered within them. This view is associated with some later German historians; check names in your textbook."],
        ], note="Be careful: do not give a historian a view unless your teacher or textbook confirms it."),
        H("Why do historians differ?"),
        T("Reasons include: **evidence** (new documents, or reading the same documents differently); **period** (a nationalist historian in the 1900s and a historian after the Second World War ask different questions); "
          "**approach** (focus on individuals, or on economics and society); **purpose** (some wrote to praise or to warn)."),
        H("A method for comparison"),
        T("Step 1: say in one line what each extract argues. Step 2: find the points of agreement. Step 3: find the points of disagreement. Step 4: explain the difference by approach, evidence or period. Step 5: reach a judgement that uses your own knowledge."),
        H("Illustrative Extract 1 (invented by KKEVO, not a real historian)"),
        T("*Invented practice text.* 'Bismarck saw clearly from 1862 that Austria would have to be defeated and France provoked. Each war was a step in a sequence he controlled.'"),
        H("Illustrative Extract 2 (invented by KKEVO, not a real historian)"),
        T("*Invented practice text.* 'Prussia's coal, iron and railways made it the natural leader. Bismarck was a gifted politician who worked within forces larger than any one man.'"),
        EX("Worked example: comparing the extracts", intro="How far do Extracts 1 and 2 agree about Bismarck's role?", steps=[
            S("Argument of each", text="Extract 1: Bismarck controlled a planned sequence. Extract 2: Prussian economic strength shaped what he could do."),
            S("Agreement", text="Both accept that Bismarck was important and that Austria and France were the main obstacles."),
            S("Disagreement", text="Extract 1 treats Bismarck as the cause; Extract 2 treats him as a skilled actor within larger forces."),
            S("Explaining the difference", text="Extract 1 focuses on a person and diplomacy; Extract 2 focuses on economic structures. They ask different questions."),
            S("Judgement with own knowledge", text="Evidence for planning: the isolation of Austria in 1866. Evidence for structures: the Zollverein and Prussian industry. Evidence against a fixed plan: Bismarck's flexibility, such as using the Ems telegram when a chance appeared. The best view combines skill and structure."),
        ]),
        EX("Model essay plan", intro="'Bismarck planned the unification of Germany.' How far do you agree?", steps=[
            S("Introduction", text="State both views briefly. Judgement: Bismarck had clear aims but adapted to events."),
            S("For planning", text="Isolation of Austria; limiting the war; use of diplomacy to bring France to declare war."),
            S("Against planning", text="Events like the Spanish succession crisis; Bismarck's flexibility; his statements after the event were self-serving."),
            S("Structures", text="Industrial strength and the Zollverein created conditions for Prussian leadership."),
            S("Judgement", text="Bismarck was a skilful opportunist who worked within favourable structures."),
        ]),
        MISTAKE("Naming historians without explaining their arguments", "Say what the view is first. A name alone earns nothing."),
        MISTAKE("Treating one historian as the final truth", "Compare views and test them against evidence."),
        QUIZ("What is historiography?",
             ["A list of dates", "The study of how history has been written and why interpretations differ", "A type of primary source", "A treaty"], 1,
             "It is the study of changing interpretations.",
             feedback=["It is not a list of dates.", "", "It concerns writing about the past.", "It is not a treaty."]),
        QUIZ("Which is a good reason why two historians may disagree about Bismarck?",
             ["They live in the same period and read the same books", "They ask different questions and focus on different kinds of evidence", "One of them has made a spelling error", "They must always disagree"], 1,
             "Different approaches and questions produce different interpretations.",
             feedback=["That would reduce disagreement.", "", "Disagreement is about interpretation.", "Historians can agree."]),
        PQ("Explain two reasons why historians' interpretations of Bismarck have changed over time.",
           "Outline: (1) New evidence and documents, and a more critical reading of Bismarck's own memoirs. (2) Changing questions: after the Second World War historians were less likely to praise national heroes and more likely to examine structures and consequences."),
        PQ("Using the invented extracts, explain one similarity and one difference.",
           "Outline: Similarity: both treat Bismarck as important. Difference: Extract 1 sees a planner; Extract 2 sees him acting inside economic structures. Explain by approach."),
        PQ("Why should a historian be cautious about using Bismarck's memoirs?",
           "Outline: Written later, with a purpose of shaping his reputation; he may exaggerate planning and play down chance. Use them with other sources."),
        SUM("Historiography studies how history is written and why views differ.",
            "Three views of Bismarck: master planner, opportunist, and one who worked within structures.",
            "Compare extracts by argument, agreement, disagreement and explanation.",
            "Use names only with an explanation of their view.",
            "Invented extracts are for practice only."),
    ],
))

# ---------------------------------------------------------------------------
# Imperialism & the First World War / The Scramble for Africa
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IMP, topic="The Scramble for Africa",
    title="The Scramble for Africa: events, the Berlin Conference and African responses",
    slug="h6-scramble-events-berlin-and-african-responses",
    minutes=26,
    summary="The main events of the partition of Africa from 1880 to 1914, what the Berlin Conference did and did not do, the tools that made conquest easier and the range of African responses.",
    objectives=[
        "Place the main events of the Scramble in order",
        "State accurately what the Berlin Conference decided",
        "Explain the means that made European conquest possible",
        "Describe African responses: resistance, negotiation and collaboration",
    ],
    key_concepts=["Scramble for Africa", "Berlin Conference", "Effective occupation", "Congo Free State", "Resistance", "Collaboration"],
    blocks=[
        H("Introduction"),
        T("Around 1880, European powers controlled only parts of the African coast, plus areas such as Algeria and the Cape. By 1914 only Ethiopia and Liberia were not under European rule. "
          "Cameroon's colonial history began in the middle of this process, in 1884.\n\n"
          "The existing overview lesson explains the main schools of interpretation. This lesson gives the events, the Berlin Conference and the African side. "
          "The next lesson shows how to turn this knowledge into an essay plan."),
        D("The rapid partition and conquest of Africa by European powers, roughly from 1880 to 1914.", title="Scramble for Africa"),
        D("A meeting in Berlin from November 1884 to February 1885, hosted by Bismarck and attended by European states and the United States. No African ruler took part. "
          "Its General Act set rules for claims on the African coast and for free trade on the Congo and Niger, and it recognised Leopold II's Congo association.", title="Berlin Conference"),
        H("Key events in order"),
        T("1881: France takes control of Tunisia. 1882: Britain occupies Egypt. 1884: Germany declares protectorates, including Togo and Kamerun, and South West Africa. "
          "1884 to 1885: Berlin Conference. 1890: Britain and Germany agree spheres in East Africa. 1896: Ethiopia defeats Italy at Adwa. 1898: Fashoda crisis between Britain and France; British victory over the Mahdist state at Omdurman. "
          "1899 to 1902: South African War. 1911 to 1912: Morocco becomes a French protectorate after the Agadir crisis. Check each date in your textbook before using it in an essay."),
        H("What the Berlin Conference did"),
        KEY("Accurate and inaccurate statements", "A common error is to say that the conference divided Africa.", cards=[
            ["What it did", "Set rules for claiming coastal territory (notification and effective occupation); declared free trade in the Congo basin; recognised the Congo Free State under Leopold II; stated opposition to the slave trade."],
            ["What it did not do", "It did not draw the map. Most frontiers were fixed later by agreements between European powers, such as the Anglo-German and Franco-German conventions for Cameroon."],
        ]),
        H("Means of conquest"),
        T("European forces had several advantages: steamships on rivers, quinine to reduce death from malaria, rapid-fire guns such as the Maxim gun, telegraph links and the support of African soldiers and allies. "
          "But these advantages were not enough alone. European forces also depended on African soldiers, porters and local alliances, and on divisions among African states."),
        H("African responses"),
        T("Responses varied. Some states fought: Samori Toure resisted French forces in West Africa until his capture in 1898. In German East Africa, the Maji Maji rising of 1905 to 1907 was put down with great violence. "
          "In German South West Africa, the Herero and Nama people were attacked in 1904 to 1908, in killings now widely described as genocide. Check the wording and evidence in your textbook."),
        T("Some rulers negotiated or signed treaties to protect their interests, as the Duala kings did in 1884. Emperor Menelik II of Ethiopia used diplomacy, modern weapons and a strong army to defeat Italy at Adwa in 1896 and stay independent. "
          "Other rulers collaborated, hoping to keep power under colonial protection. Choices were rarely simple, and many rulers changed approach over time."),
        TIP("Do not describe all Africans as passive or all as resisters. Use specific examples to show the range."),
        EX("Model essay plan 1", intro="Assess the importance of the Berlin Conference in the partition of Africa.", steps=[
            S("Introduction", text="State what the conference did. Judgement: it was important as a set of rules and a sign of cooperation, but it did not itself divide Africa."),
            S("Its effects", text="Effective occupation encouraged powers to claim and occupy coasts quickly; the Congo Free State was recognised."),
            S("Its limits", text="No map was drawn; borders came from later agreements; Africans were not present; conquest of the interior continued after 1885."),
            S("Other factors", text="Egypt in 1882, rivalry among powers, new technology and African alliances."),
            S("Judgement", text="The conference regulated and speeded the Scramble; it did not cause it."),
        ]),
        EX("Model essay plan 2", intro="To what extent did African states and peoples resist the Scramble?", steps=[
            S("Introduction", text="Define resistance. Judgement: resistance was widespread, but it was one of several responses, and it often failed against superior arms."),
            S("Resistance", text="Samori Toure; Maji Maji; Herero and Nama; Ethiopia at Adwa."),
            S("Negotiation and collaboration", text="Duala kings in 1884; Fon Galega I of Bali; King Njoya of Bamum."),
            S("Why resistance often failed", text="Technology, divisions among Africans, shortage of weapons, disease and famine."),
            S("Judgement", text="Resistance shaped the pace and the terms of conquest; it rarely stopped it."),
        ]),
        MISTAKE("Saying 'the Berlin Conference divided Africa'", "It set rules. Say 'it set rules for claiming territory'."),
        MISTAKE("Naming African resistance without outcomes", "For each example say what happened and what it shows about the scale or limits of resistance."),
        QUIZ("Which African state defeated Italy at Adwa in 1896?",
             ["Liberia", "Ethiopia", "Egypt", "Morocco"], 1,
             "Ethiopia under Menelik II defeated Italy.",
             feedback=["Liberia did not fight Italy.", "", "Egypt was occupied by Britain in 1882.", "Morocco became a French protectorate in 1912."]),
        QUIZ("Which statement about the Berlin Conference is accurate?",
             ["It drew the map of Africa", "African rulers took part", "It set rules for claiming coastal territory and recognised the Congo Free State", "It ended in 1914"], 2,
             "The conference set rules; it did not draw the map or include African rulers.",
             feedback=["Frontiers were fixed later.", "No African ruler attended.", "", "It ended in February 1885."]),
        PQ("Explain two reasons why European powers were able to conquer most of Africa by 1914.",
           "Outline: (1) Technology: Maxim guns, steamships, quinine and telegraphs. (2) African divisions and alliances: European forces used African soldiers and allies and exploited rivalries. Add that resistance was often hindered by shortage of modern weapons."),
        PQ("Describe the main decisions of the Berlin Conference.",
           "Outline: Rules for notifying and effectively occupying coastal claims; free trade in the Congo and Niger basins; recognition of the Congo Free State; statement against the slave trade. No African participation."),
        PQ("How far did African leaders shape the course of the Scramble?",
           "Outline: Shaping: treaties such as the Duala treaty; Menelik II's victory at Adwa; resistance delaying conquest; use of alliances. Limits: European arms and diplomacy; rules set at Berlin without Africans. Judgement: Africans shaped terms and timing but not the overall outcome."),
        SUM("Between 1880 and 1914 almost all Africa came under European rule, except Ethiopia and Liberia.",
            "The Berlin Conference (1884 to 1885) set rules and recognised the Congo Free State; it did not draw the map.",
            "Technology and African allies helped European conquest.",
            "African responses included resistance, negotiation and collaboration.",
            "Use specific examples and avoid blanket claims."),
    ],
))

LESSONS.append(lesson(
    module=M_IMP, topic="The Scramble for Africa",
    title="Essay skills: planning an essay on the Scramble for Africa",
    slug="h6-essay-planning-the-scramble",
    minutes=24,
    summary="A step-by-step method for planning a history essay (read the question, plan in five minutes, argue with a judgement) practised on the four schools of interpretation of the Scramble.",
    objectives=[
        "Break down an essay question into command word, topic, time frame and focus",
        "Write a five-minute plan with a clear line of argument",
        "Structure paragraphs with point, evidence, explanation and link",
        "Use interpretations to support an argument, not as a list",
    ],
    key_concepts=["Command word", "Line of argument", "Judgement", "Counter-argument", "PEEL"],
    blocks=[
        H("Introduction"),
        T("Many students know a lot of history but lose marks because they describe instead of arguing. At A Level an essay answers a question with a clear judgement, supported by evidence and balanced against counter-arguments. "
          "Planning is the skill that makes this possible.\n\n"
          "Check the real paper format and timing with your teacher. The timings below are KKEVO advice, not official instructions."),
        D("The instruction word at the start of the question, such as *explain*, *assess*, *compare* or *to what extent*. It tells you what kind of answer is needed.", title="Command word"),
        D("The main answer to the question, stated in the introduction and kept in view throughout the essay.", title="Line of argument"),
        H("Step 1: read the question (about one minute)"),
        T("Underline four things: the **command word**, the **topic**, the **time frame** and the **focus** (the cause, result, person or idea being tested). "
          "In 'To what extent was the Scramble for Africa caused by economic factors?' the command words are *to what extent*, the topic is the Scramble, the time frame is roughly 1880 to 1914 and the focus is economic factors."),
        H("Step 2: plan (about five minutes)"),
        T("Write a short plan: your judgement in one sentence; three or four paragraph points with one piece of evidence each; one counter-argument; the conclusion. "
          "Number the paragraphs in the order you will write them."),
        IMG("al-h6-opcvl.svg", alt="OPCVL: origin, purpose, content, value, limits", caption="Figure 1. For source questions, use OPCVL; for essays, use a plan like the one below."),
        H("Step 3: write with structure"),
        KEY("Essay structure", "A simple model.", cards=[
            ["Introduction", "Define key terms, set the time frame, state your judgement in a sentence."],
            ["Paragraphs (PEEL)", "Point (answers the question), Evidence (names, dates, examples), Explanation (why it matters), Link (back to the question)."],
            ["Counter-argument", "A paragraph on the other side, showing why you still hold your judgement."],
            ["Conclusion", "Answer the question, rank the factors, and do not introduce new evidence."],
        ]),
        H("Using interpretations well"),
        T("Do not list the four schools. Choose the ones that help your argument. For an economic question, use Hobson and Lenin as the case for the economic view and Fieldhouse as critic. "
          "For a question about Africans, use African agency and Hopkins on West Africa. Always say what the interpretation argues and test it against evidence."),
        EX("Worked plan 1", intro="'The Scramble for Africa was caused mainly by economic factors.' How far do you agree?", steps=[
            S("Underline", text="Command words: how far do you agree. Topic: the Scramble. Time: about 1880 to 1914. Focus: economic causes."),
            S("Judgement", text="Economic motives were important background, but political rivalry and crises in Africa explain the timing."),
            S("Paragraph 1: economic case", text="Hobson, Lenin; trade interests of firms, as in Kamerun."),
            S("Paragraph 2: economic critique", text="Fieldhouse: little investment in tropical Africa before 1900."),
            S("Paragraph 3: political and strategic", text="Prestige, rivalry, Bismarck's moves in 1884."),
            S("Paragraph 4: peripheral and African factors", text="Egypt 1882 (Robinson and Gallagher); African treaties and resistance."),
            S("Conclusion", text="Rank the factors and state the judgement."),
        ]),
        EX("Worked plan 2", intro="Compare two interpretations of the Scramble for Africa.", steps=[
            S("Choose two", text="For example economic (Hobson and Lenin) and peripheral (Robinson and Gallagher)."),
            S("State each argument", text="Economic: capitalism needed markets and investment. Peripheral: crises in Africa, especially Egypt in 1882, drew Europeans in."),
            S("Compare", text="Agreement: both stress forces beyond diplomacy. Disagreement: where the cause lies (Europe's economy or African crises)."),
            S("Evaluate", text="Test with evidence: Egypt supports peripheral; the Congo supports economic."),
            S("Judgement", text="Neither explains everything. Combine them."),
        ]),
        MISTAKE("Writing everything you know", "Include only material that answers the question. Cut the rest."),
        MISTAKE("Having no judgement until the last line", "State your judgement in the introduction and use it in each paragraph link."),
        MISTAKE("Ignoring the time frame", "Check dates. Writing about 1900 to 1914 when the question says 1880 to 1900 loses focus."),
        QUIZ("What is the purpose of the plan?",
             ["To use up exam time", "To organise a line of argument and evidence before writing", "To make the essay longer", "To replace the introduction"], 1,
             "A plan helps you argue clearly.",
             feedback=["A short plan saves time overall.", "", "Quality matters more than length.", "The introduction is still needed."]),
        QUIZ("Which is the best use of an interpretation in an essay?",
             ["List the names of four historians", "Explain what the interpretation argues and test it against evidence", "Quote a historian at length", "Avoid mentioning any interpretation"], 1,
             "Interpretations are tools for argument.",
             feedback=["A list earns little.", "", "Long quotation takes up time.", "Interpretations help the argument."]),
        PQ("Underline and name the command word, topic, time frame and focus in: 'Assess the importance of African resistance in the Scramble for Africa.'",
           "Command word: assess (weigh importance). Topic: African resistance. Time frame: the Scramble, roughly 1880 to 1914. Focus: its importance (effect on the outcome)."),
        PQ("Write a one-sentence judgement for: 'To what extent was the Berlin Conference responsible for the partition of Africa?'",
           "Sample: The Berlin Conference set rules that speeded the Scramble, but it did not cause or complete it; rivalry, technology and African events were more important."),
        PQ("Explain how to structure one paragraph using PEEL.",
           "Outline: Point answers the question; Evidence gives a name, date or example; Explanation says why it supports the point; Link ties it back to the question and judgement."),
        SUM("Read the question and underline command word, topic, time frame and focus.",
            "Plan for about five minutes: judgement, paragraph points, counter-argument.",
            "Use PEEL: point, evidence, explanation, link.",
            "Use interpretations to build the argument, not as a list.",
            "Check the real paper format and timing with your teacher."),
    ],
))

# ---------------------------------------------------------------------------
# Imperialism & the First World War / The First World War
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_IMP, topic="The First World War",
    title="The July Crisis of 1914 and the question of responsibility",
    slug="h6-july-crisis-and-responsibility",
    minutes=26,
    summary="A day-by-day account of the July Crisis, the roles of Austria-Hungary, Germany, Russia, France and Britain, and a method for judging responsibility in a balanced way.",
    objectives=[
        "Place the events of the July Crisis in order",
        "Explain the decisions of each power",
        "Explain the Fischer thesis and other interpretations",
        "Write a balanced judgement on responsibility",
    ],
    key_concepts=["July Crisis", "Blank cheque", "Ultimatum", "Mobilisation", "Schlieffen Plan", "Fischer thesis"],
    blocks=[
        H("Introduction"),
        T("The First World War began after a month of crisis. Many factors made war possible, but in July 1914 leaders took decisions that turned a Balkan crisis into a European war. "
          "This lesson tracks those decisions and asks who bore most responsibility. Treat the question with care: historians still disagree."),
        IMG("al-h6-july-crisis.svg", alt="Timeline of the July Crisis from the assassination on 28 June to Britain's declaration of war on 4 August 1914", caption="Figure 1. The July Crisis. Events are evenly spaced, not to scale."),
        D("A promise of German support to Austria-Hungary in early July 1914, given without conditions. The term 'blank cheque' is a later label.", title="Blank cheque"),
        D("Calling up the army and reserves for war. Mobilisation plans were complex, so starting them was seen as a step close to war.", title="Mobilisation"),
        H("Background"),
        T("The long-term causes (alliances, naval and arms races, imperial rivalry, Balkan nationalism, a series of crises such as Morocco and Bosnia) made Europe tense. "
          "Italy was in the Triple Alliance but stayed neutral in 1914. Britain's links with France and Russia were ententes, not binding alliances."),
        H("The crisis day by day"),
        T("28 June: Archduke Franz Ferdinand is shot in Sarajevo by Gavrilo Princip, a Bosnian Serb. Early July: Germany assures Austria-Hungary of support (the blank cheque). "
          "23 July: Austria-Hungary sends Serbia a harsh ultimatum. 25 July: Serbia accepts most demands but not all. 28 July: Austria-Hungary declares war on Serbia. "
          "Russia mobilises, first partly and then generally (30 July). 1 August: Germany declares war on Russia. 3 August: Germany declares war on France and invades Belgium. "
          "4 August: Britain declares war on Germany. Check each date in your textbook."),
        H("Decisions that mattered"),
        KEY("Who decided what", "A responsibility essay needs specific decisions.", cards=[
            ["Austria-Hungary", "Chose a hard ultimatum and war against Serbia, believing it had to act to protect its position."],
            ["Germany", "Gave unconditional support; had a war plan (Schlieffen Plan) that required a quick attack on France through Belgium."],
            ["Russia", "Mobilised in support of Serbia, which German leaders saw as a threat."],
            ["France", "Supported Russia and did not restrain it."],
            ["Britain", "Hoped to remain a mediator; entered the war after the invasion of Belgium."],
            ["Serbia", "Its officials and nationalist groups were linked to the assassination plot; the exact degree of official involvement is debated."],
        ]),
        H("Interpretations"),
        T("After 1919, the Versailles treaty blamed Germany. In the 1920s and 1930s many historians argued that all powers slid into war. In 1961 Fritz Fischer argued that Germany's leaders had aims of European dominance and took risks that made war likely. "
          "His thesis caused a strong debate in Germany. Later writers such as Christopher Clark stressed shared responsibility and the complex decisions of several governments. "
          "A.J.P. Taylor stressed the pressure of railway timetables and military plans. Check titles and dates of these works in your textbook."),
        EX("Model essay plan 1", intro="'Germany was mainly responsible for the outbreak of the First World War.' How far do you agree?", steps=[
            S("Introduction", text="Outline the debate. Judgement: Germany bore a large share but not sole responsibility."),
            S("For German responsibility", text="The blank cheque; the Schlieffen Plan; the declaration of war on Russia and France; the invasion of Belgium; Fischer's argument."),
            S("Against", text="Austria-Hungary issued the ultimatum and declared war; Russia mobilised first; Serbia's role; Britain's ambiguity."),
            S("Structure", text="Alliances and mobilisation timetables limited choices."),
            S("Judgement", text="Germany's decisions in July were decisive, but the crisis grew out of conditions that other powers helped to create."),
        ]),
        EX("Model essay plan 2", intro="Explain why a local crisis in the Balkans became a European war in 1914.", steps=[
            S("Point 1: alliances", text="Austria-Hungary was backed by Germany; Serbia by Russia; Russia by France."),
            S("Point 2: war plans", text="The Schlieffen Plan meant Germany had to attack France quickly, including through Belgium."),
            S("Point 3: decisions", text="Austria's ultimatum, German blank cheque, Russian mobilisation."),
            S("Link", text="Each decision limited the options of the next."),
        ]),
        MISTAKE("Saying the assassination alone caused the war", "It was the trigger. Explain the underlying causes and the decisions after it."),
        MISTAKE("Ranking powers without evidence", "For each power name one decision and its effect."),
        QUIZ("What was the 'blank cheque'?",
             ["A payment to Serbia", "Unconditional German support for Austria-Hungary in July 1914", "A British loan to France", "A Russian promise to Serbia"], 1,
             "Germany gave unconditional backing.",
             feedback=["It was not a payment to Serbia.", "", "It was not a British loan.", "It was a German promise."]),
        QUIZ("Which event led Britain to declare war on 4 August 1914?",
             ["The assassination at Sarajevo", "The German invasion of Belgium", "The Austrian ultimatum", "The Russian mobilisation"], 1,
             "The invasion of Belgium brought Britain in.",
             feedback=["It was the trigger of the crisis, not Britain's reason.", "", "Britain was not a party to this.", "Britain was not bound to Russia."]),
        PQ("Explain two ways in which the Schlieffen Plan contributed to the outbreak of war.",
           "Outline: (1) It required a quick attack on France before Russia was ready, so a Russo-German war meant a Franco-German war. (2) It involved invading Belgium, which brought Britain into the war."),
        PQ("Summarise the Fischer thesis and one criticism of it.",
           "Outline: Fischer argued German leaders deliberately pursued dominance and accepted war in 1914. Critics say it underplays the decisions of other powers and the pressures of the alliance system, as in Clark's account."),
        PQ("How far was Austria-Hungary responsible for the outbreak of the war?",
           "Outline: Responsible: harsh ultimatum, declaration of war on Serbia, rejection of mediation. Not alone: Germany's support, Russian mobilisation. Judgement: a major share, but dependent on German backing."),
        SUM("The assassination on 28 June 1914 triggered a crisis in which several governments made decisions that led to war.",
            "Key steps: blank cheque, 23 July ultimatum, 28 July war on Serbia, mobilisations, 1 to 4 August declarations.",
            "Germany's role was large, but Austria-Hungary, Russia, Serbia and others also played a part.",
            "Interpretations range from Versailles blame to Fischer and Clark.",
            "Support every judgement with named decisions."),
    ],
))

LESSONS.append(lesson(
    module=M_IMP, topic="The First World War",
    title="Versailles, the other treaties and the mandates, including Cameroon",
    slug="h6-versailles-and-the-mandates",
    minutes=26,
    summary="The aims of the Big Three at Paris, the main terms of the Treaty of Versailles and the debate on its fairness, the mandate system and its application to Cameroon.",
    objectives=[
        "Explain the aims of Wilson, Clemenceau and Lloyd George",
        "State the main terms of the Treaty of Versailles",
        "Evaluate how harsh or fair the treaty was",
        "Explain the mandate system and the position of Cameroon",
    ],
    key_concepts=["Fourteen Points", "Big Three", "Article 231", "Reparations", "Diktat", "Mandate system"],
    blocks=[
        H("Introduction"),
        T("The war ended with an armistice on 11 November 1918. The peace conference opened in Paris in January 1919. Its decisions shaped Europe and also Cameroon, which was removed from German rule. "
          "This lesson covers the aims, the terms, the debate and the mandates."),
        D("The principles for peace announced by US President Woodrow Wilson in January 1918, including self-determination for peoples and a League of Nations.", title="Fourteen Points"),
        D("Article 231 of the Treaty of Versailles, which stated that Germany and its allies accepted responsibility for the loss and damage caused by the war. It was the legal basis for reparations.", title="War guilt clause"),
        H("The Big Three"),
        KEY("Different aims", "The leaders wanted different things.", cards=[
            ["Wilson (United States)", "A fair peace based on self-determination and a League of Nations to keep the peace."],
            ["Clemenceau (France)", "Security against Germany: weaken it, take back Alsace-Lorraine, secure reparations."],
            ["Lloyd George (Britain)", "A peace that kept British security and trade, with a settlement that would not be impossible to keep; he also faced public demands to punish Germany."],
        ]),
        H("Terms of the Treaty of Versailles, signed 28 June 1919"),
        T("Germany lost Alsace-Lorraine to France and other territory, including land to Poland, and the port of Danzig became a free city under League supervision. "
          "The Rhineland was demilitarised. The German army was limited to 100,000 men and the navy and air force were severely limited. Germany lost all its colonies. "
          "Article 231 made Germany responsible, and in 1921 reparations were fixed at 132 billion gold marks. Union with Austria was forbidden."),
        T("Separate treaties dealt with Austria, Hungary, Bulgaria and the Ottoman Empire. Austria-Hungary was broken up and new states were created or enlarged in central Europe."),
        H("Harsh or fair?"),
        T("Germans called the treaty a **Diktat** (dictated peace). John Maynard Keynes, in a book of 1919, argued that the treaty's economic terms were unwise. "
          "Later historians, among them Margaret MacMillan, argue that the treaty was less harsh than Germans claimed and that Germany remained united and strong. "
          "Others stress that the real problem was a treaty that was too weak to contain Germany but too hard for Germans to accept. Check these views in your textbook."),
        H("The mandate system and Cameroon"),
        T("Germany's colonies were not simply handed to the victors. Article 22 of the League Covenant said they would be administered as mandates by 'advanced nations' on behalf of the League, supervised by the Permanent Mandates Commission. "
          "Mandates were classed A, B and C. Cameroon and Togo were class B."),
        IMG("al-h6-kamerun-partition.svg", alt="Schematic of Kamerun being divided into British and French shares", caption="Figure 1. Kamerun after 1916: schematic only, not a map."),
        T("The Kamerun campaign of 1914 to 1916 ended German rule. The Milner-Simon declaration of 10 July 1919 divided the territory. The League confirmed the mandates in 1922. "
          "Critics said the mandates were colonies under another name. Defenders said they carried duties to the inhabitants and international reporting that could be used by petitioners. After 1945 the territories became United Nations trust territories."),
        EX("Model essay plan 1", intro="'The Treaty of Versailles was a harsh treaty.' How far do you agree?", steps=[
            S("Introduction", text="Define harsh. Judgement: harsh in its symbolism and reparations, less so in its territorial effect."),
            S("Harsh features", text="Loss of land and colonies; army limits; Article 231; reparations."),
            S("Less harsh features", text="Germany remained a united state with industry; the Rhineland occupation was limited; reparations were later reduced."),
            S("Historians", text="Keynes versus MacMillan."),
            S("Judgement", text="The treaty was seen as harsh by Germans and was used by extremists, whether or not it was objectively harsh."),
        ]),
        EX("Model essay plan 2", intro="Assess the impact of the mandate system on Cameroon.", steps=[
            S("Introduction", text="Define the mandate. Judgement: day-to-day rule was colonial, but the legal status mattered later."),
            S("Colonial reality", text="Britain and France administered the zones with the methods already studied."),
            S("Legal framework", text="Annual reports, the Permanent Mandates Commission and petitions."),
            S("After 1945", text="UN trusteeship, visiting missions and the path to independence."),
            S("Judgement", text="A limited protection in the interwar years that helped later claims."),
        ]),
        MISTAKE("Saying Germany lost all territory", "Germany lost land and colonies but remained a large state."),
        MISTAKE("Mixing up the date of the armistice and the treaty", "Armistice 11 November 1918. Treaty of Versailles 28 June 1919."),
        QUIZ("What did Article 231 say?",
             ["Germany must give up its colonies", "Germany accepted responsibility for the loss and damage caused by the war", "The League would govern Cameroon", "Austria could join Germany"], 1,
             "Article 231 was the war guilt clause.",
             feedback=["That is Article 119.", "", "That belongs to Article 22 of the Covenant.", "Union with Austria was forbidden."]),
        QUIZ("What class of mandate was Cameroon?",
             ["Class A", "Class B", "Class C", "No mandate"], 1,
             "Cameroon and Togo were class B mandates.",
             feedback=["Class A covered former Ottoman territories.", "", "Class C included South West Africa.", "Cameroon was a mandate from 1922."]),
        PQ("Explain two reasons why Germans resented the Treaty of Versailles.",
           "Outline: (1) Article 231 placed responsibility on Germany. (2) Reparations, territorial losses and army limits were imposed with no German negotiation."),
        PQ("Describe the mandate system.",
           "Outline: Article 22 of the League Covenant: former German and Ottoman territories administered by advanced nations on behalf of the League, supervised by the Permanent Mandates Commission, in classes A, B and C."),
        PQ("To what extent did the peace settlement of 1919 meet the aims of the Big Three?",
           "Outline: Clemenceau gained Alsace-Lorraine and reparations but not the Rhine frontier. Lloyd George gained colonies and naval security but wanted moderation. Wilson achieved the League but not all his points. Judgement: each leader was partly satisfied."),
        SUM("The war ended with an armistice on 11 November 1918; Versailles was signed on 28 June 1919.",
            "The Big Three had different aims: Wilson idealism, Clemenceau security, Lloyd George compromise.",
            "Terms included loss of land and colonies, army limits, Article 231 and reparations.",
            "Historians debate how harsh it was.",
            "Cameroon became a class B mandate, divided between France and Britain and confirmed in 1922."),
    ],
))

# ---------------------------------------------------------------------------
# The Interwar Crises / Fascism and Nazism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_INT, topic="Fascism and Nazism",
    title="How Mussolini came to power and built a Fascist state, 1919-1929",
    slug="h6-mussolini-rise-and-fascist-state",
    minutes=24,
    summary="Why Italy's liberal government failed after 1918, how the Fascists used violence and politics to gain power by 1922, and how Mussolini made a dictatorship between 1922 and 1929.",
    objectives=[
        "Explain the problems of Italy after the First World War",
        "Describe the March on Rome and the way Mussolini became prime minister",
        "Explain how Mussolini turned his government into a dictatorship",
        "Judge the reasons for Fascist success",
    ],
    key_concepts=["Fascism", "Squadristi", "March on Rome", "Matteotti crisis", "Lateran Treaties", "Dictatorship"],
    blocks=[
        H("Introduction"),
        T("Fascism was a new political movement, born in Italy in 1919. It rejected democracy and socialism, praised the nation and the leader, and accepted violence as a political tool. "
          "This lesson asks how Mussolini came to power without a revolution and how he then built a dictatorship."),
        D("A political movement of the early twentieth century that stressed extreme nationalism, a single party, a powerful leader, state control and the use of force against opponents. "
          "The word comes from *fasces*, a bundle of rods used as a symbol of authority in ancient Rome.", title="Fascism"),
        D("Squads of armed Fascist supporters who attacked socialist and trade union offices and members in 1920 to 1922.", title="Squadristi"),
        H("Italy after 1918"),
        T("Italy was on the winning side of the war, but many Italians felt cheated by the peace settlement, which they called a 'mutilated victory'. "
          "There were strikes, factory occupations and fear of communism in 1919 to 1920. Unemployment and inflation were serious problems. "
          "The liberal governments of the time were divided and weak, and they had trouble forming lasting coalitions."),
        H("The rise of the Fascists, 1919-1922"),
        T("Benito Mussolini, a former socialist journalist, founded the Fasci di Combattimento in March 1919. The movement had little success at first. "
          "From 1920 it grew rapidly when squads of Fascists attacked socialists and trade unionists, especially in northern and central Italy. Landowners, businessmen and some police and army officers tolerated or helped them. "
          "In 1921 Mussolini turned the movement into a party, the National Fascist Party, and Fascists won seats in parliament."),
        H("The March on Rome, October 1922"),
        T("In late October 1922 Fascist columns gathered around Rome while Mussolini stayed in Milan. The government asked the king, Victor Emmanuel III, to declare martial law. The king refused. "
          "He invited Mussolini to form a government, and Mussolini travelled to Rome by train. The 'March' was more a show of strength than a battle; the king's decision was decisive. Check the dates in your textbook."),
        H("From prime minister to dictator"),
        T("At first Mussolini led a coalition. In 1923 the Acerbo Law gave the largest party two thirds of the seats if it won a quarter of the votes. In the 1924 elections, held amid violence and intimidation, the Fascists won a large majority. "
          "The socialist deputy Giacomo Matteotti, who criticised the elections, was kidnapped and murdered in June 1924 by Fascists. Opposition deputies withdrew from parliament. "
          "On 3 January 1925 Mussolini accepted responsibility for what had happened and began to build a dictatorship. In 1925 to 1926 opposition parties were banned, the press was controlled and a secret police was created."),
        H("Securing the regime"),
        KEY("Tools of control", "The regime used both force and consent.", cards=[
            ["Force", "Secret police, special courts, exile for opponents, control of local government."],
            ["Propaganda", "Control of the press and radio, the cult of the leader (Il Duce), youth organisations."],
            ["Deals with institutions", "The Lateran Treaties of February 1929 settled the long dispute with the Papacy and created Vatican City."],
            ["Economy", "The 'corporate state' aimed to control labour and industry under state direction."],
        ]),
        EX("Model essay plan 1", intro="Explain why the Fascists came to power in Italy in 1922.", steps=[
            S("Introduction", text="Define the question. Judgement: Fascists gained power through the weakness of liberal Italy and the choices of the elite, as well as their own violence."),
            S("Weak liberal governments", text="Divided coalitions, strikes, fear of communism, economic problems."),
            S("Fascist methods", text="Squadristi violence; Mussolini's political skill in making deals; the threat of the March on Rome."),
            S("Elite support", text="Landowners, industrialists, police and the king allowed or supported the Fascists."),
            S("Judgement", text="The Fascists could not have succeeded without the failure of others to oppose them."),
        ]),
        EX("Model essay plan 2", intro="'The Matteotti crisis was the turning point in the creation of the Fascist dictatorship.' Discuss.", steps=[
            S("Introduction", text="Define the crisis (June 1924). Judgement: it was a turning point because Mussolini survived it and chose repression, but earlier laws had already prepared the ground."),
            S("For", text="Public outrage; opposition withdrew; Mussolini then took full responsibility in January 1925 and passed laws against opponents."),
            S("Against", text="The Acerbo Law (1923) and violence in 1924 had already weakened democracy."),
            S("Why Mussolini survived", text="The king and elites did not act; the opposition was divided."),
            S("Judgement", text="A key moment, within a longer process."),
        ]),
        MISTAKE("Saying Mussolini seized power by force alone", "The king appointed him as prime minister. Explain why the elite accepted him."),
        MISTAKE("Mixing 1922 and 1925", "1922 is the March on Rome; 1925 to 1926 marks the creation of the dictatorship."),
        QUIZ("Who invited Mussolini to form a government in October 1922?",
             ["The Pope", "King Victor Emmanuel III", "The army", "Parliament by a vote"], 1,
             "The king chose Mussolini as prime minister.",
             feedback=["The Pope did not appoint governments.", "", "The army did not appoint him.", "It was the king's decision."]),
        QUIZ("What did the Lateran Treaties of 1929 settle?",
             ["The status of the Vatican and relations with the Papacy", "Italy's borders with Austria", "The end of reparations", "The alliance with Germany"], 0,
             "They settled the Roman Question.",
             feedback=["", "Borders were settled in 1919 to 1920.", "Italy was not a reparations payer.", "The alliance came later."]),
        PQ("Explain two reasons why liberal governments in Italy were unable to stop the Fascists.",
           "Outline: (1) They were weak and divided coalitions. (2) Many officials, police and elites sympathised with the Fascists because they feared socialism."),
        PQ("Describe the stages by which Mussolini created a dictatorship between 1922 and 1926.",
           "Outline: 1922 prime minister; 1923 Acerbo Law; 1924 elections and Matteotti murder; January 1925 speech; 1925 to 1926 laws banning opposition and controlling the press."),
        PQ("How far was Mussolini's rise to power due to the weakness of his opponents?",
           "Outline: Weak opponents: divided liberals, socialists and Catholic party; failure of the king to resist. Fascist strength: violence, organisation, propaganda. Judgement: both, with the weakness of opponents essential."),
        SUM("Italy after 1918 faced disappointment with the peace, strikes and weak governments.",
            "Fascists used violence from 1920; Mussolini became prime minister in October 1922 after the March on Rome.",
            "The Acerbo Law, the 1924 election and the Matteotti murder prepared a dictatorship from 1925.",
            "The regime used force, propaganda and deals such as the Lateran Treaties (1929).",
            "The failure of the elite to resist was essential."),
    ],
))

LESSONS.append(lesson(
    module=M_INT, topic="Fascism and Nazism",
    title="From the Weimar Republic to Hitler's dictatorship, 1919-1934",
    slug="h6-weimar-republic-to-nazi-dictatorship",
    minutes=28,
    summary="The problems and successes of the Weimar Republic, the effect of the Great Depression, how Hitler became chancellor in 1933, and how Nazi rule became a dictatorship by 1934.",
    objectives=[
        "Explain the problems of the Weimar Republic and the recovery of 1924 to 1929",
        "Explain how the Great Depression helped the Nazis",
        "Explain how Hitler became chancellor and consolidated power",
        "Evaluate the causes of the fall of Weimar",
    ],
    key_concepts=["Weimar Republic", "Article 48", "Hyperinflation", "Great Depression", "Enabling Act", "Gleichschaltung"],
    blocks=[
        H("Introduction"),
        T("Germany became a republic in November 1918, after the Kaiser abdicated. In 1933 Hitler became chancellor, and within two years Germany was a dictatorship. "
          "This lesson looks at both the weaknesses of the Weimar Republic and the actions of the Nazis. Nazi ideology was extremely racist and antisemitic, and these beliefs led to persecution. "
          "This topic should be studied with seriousness and respect for the victims."),
        D("The German republic from 1919 to 1933, named after the city of Weimar where its constitution was drawn up.", title="Weimar Republic"),
        D("A clause of the Weimar constitution that let the president rule by emergency decree in a crisis. In the early 1930s it was used to govern without a majority in the Reichstag.", title="Article 48"),
        H("Weimar's problems, 1919-1923"),
        T("Many Germans blamed the republic for the defeat and the Treaty of Versailles. Early years brought left-wing risings (the Spartacist rising, January 1919) and right-wing attempts such as the Kapp Putsch (1920). "
          "In 1923 France and Belgium occupied the Ruhr when Germany fell behind on reparations. Printing money led to hyperinflation, which destroyed the savings of many middle-class families. "
          "In November 1923 Hitler's attempted Munich Putsch failed and he was imprisoned."),
        H("Recovery, 1924-1929"),
        T("Under Gustav Stresemann, Germany introduced a new currency, accepted the Dawes Plan (1924) for reparations with American loans, and signed the Locarno agreements (1925). "
          "The economy recovered. The Nazis received very few votes in elections in the late 1920s."),
        H("The Great Depression and the Nazi breakthrough"),
        T("After the Wall Street Crash of October 1929, American loans were withdrawn and German unemployment soared. Governments used emergency decrees under Article 48. "
          "The Nazis offered simple answers, strong leadership and attacks on scapegoats. Their share of the vote rose from about 2.6 per cent in May 1928 to about 18.3 per cent in September 1930, and about 37.3 per cent in July 1932."),
        IMG("al-h6-nazi-votes.svg", alt="Bar chart of Nazi vote shares: 2.6 in 1928, 18.3 in 1930, 37.3 in July 1932, 33.1 in November 1932, 43.9 in March 1933", caption="Figure 1. Nazi share of the vote in Reichstag elections (rounded). Check figures in your textbook."),
        H("Becoming chancellor, January 1933"),
        T("No party had a majority. Conservative politicians, including Franz von Papen, believed they could control Hitler. President Hindenburg appointed Hitler chancellor on 30 January 1933 at the head of a coalition. "
          "This was a political decision by a small circle, not the result of a majority vote for the Nazis."),
        H("Consolidating power, 1933-1934"),
        T("After the Reichstag fire on 27 February 1933, an emergency decree suspended civil rights. In the March 1933 election, the Nazis won about 43.9 per cent. "
          "The Enabling Act of 23 March 1933, passed with the support of other parties under pressure, let Hitler's government pass laws without the Reichstag. "
          "In 1933 trade unions were abolished and other parties were banned. On 30 June 1934 the 'Night of the Long Knives' removed the SA leadership and other opponents. "
          "When Hindenburg died on 2 August 1934, Hitler combined the offices of president and chancellor and became Fuhrer."),
        KEY("Why did Weimar fall?", "Structure your answer by type of cause.", cards=[
            ["Long-term weaknesses", "Association with Versailles; political division; Article 48; elite hostility to the republic."],
            ["Economic crisis", "Hyperinflation in 1923 and, above all, the Depression after 1929."],
            ["Nazi methods", "Propaganda, the SA, and Hitler's skill in presenting himself as a saviour."],
            ["Political decisions", "The choices of Hindenburg, Papen and others in 1932 to 1933."],
        ]),
        EX("Model essay plan 1", intro="'The Great Depression was the main reason for the Nazis' rise to power.' How far do you agree?", steps=[
            S("Introduction", text="Define the question. Judgement: the Depression was the main trigger, but political decisions and Nazi methods were also essential."),
            S("The Depression", text="Mass unemployment and the collapse of the coalition; the vote rise from 1930."),
            S("Nazi appeal", text="Propaganda, the SA, promises to different groups, the Fuhrer image."),
            S("Elite decisions", text="Papen and Hindenburg appointed Hitler in January 1933, believing he could be controlled."),
            S("Judgement", text="Without the Depression the Nazis would likely have remained marginal; without elite decisions they might not have gained office."),
        ]),
        EX("Model essay plan 2", intro="Explain how Hitler consolidated power between January 1933 and August 1934.", steps=[
            S("Step 1: emergency powers", text="Reichstag fire decree, 28 February 1933."),
            S("Step 2: law-making power", text="The Enabling Act, 23 March 1933."),
            S("Step 3: removing opposition", text="Trade unions and parties banned; Gleichschaltung (bringing institutions into line)."),
            S("Step 4: removing rivals and the army question", text="Night of the Long Knives, 30 June 1934; the army oath after Hindenburg's death."),
            S("Link", text="Each step used legal forms and violence together."),
        ]),
        MISTAKE("Saying Hitler won a majority in 1933", "Hitler was appointed chancellor. His best result in a free election was about 37 per cent in July 1932."),
        MISTAKE("Blaming only the Treaty of Versailles", "The Depression and political decisions were also decisive."),
        QUIZ("On what date was Hitler appointed chancellor?",
             ["9 November 1923", "30 January 1933", "27 February 1933", "2 August 1934"], 1,
             "President Hindenburg appointed him on 30 January 1933.",
             feedback=["That was the Munich Putsch.", "", "That was the Reichstag fire.", "That was Hindenburg's death."]),
        QUIZ("What did the Enabling Act of March 1933 allow?",
             ["Hitler's government to pass laws without the Reichstag", "Women to vote", "The end of reparations", "The union of Germany and Austria"], 0,
             "It gave the government law-making power.",
             feedback=["", "Women voted from 1919.", "Reparations were reduced earlier.", "Union with Austria was forbidden."]),
        PQ("Explain two reasons why hyperinflation in 1923 damaged support for the Weimar Republic.",
           "Outline: (1) Savings of the middle classes were destroyed, causing resentment. (2) It was blamed on the republic and reparations, adding to the sense of national humiliation."),
        PQ("Describe how Hitler became chancellor in January 1933.",
           "Outline: Nazis the largest party but without a majority; Papen and other conservatives persuaded Hindenburg to appoint Hitler as head of a coalition, thinking they could control him."),
        PQ("To what extent did the fall of the Weimar Republic result from weaknesses in its constitution?",
           "Outline: Weaknesses: Article 48, proportional representation, hostile elites. Other causes: Depression, Nazi methods, decisions in 1932 to 1933. Judgement: the constitution allowed a crisis; events and decisions turned it into a collapse."),
        SUM("Weimar faced political violence and the 1923 crisis, then recovered under Stresemann.",
            "The Depression after 1929 raised Nazi support to about 37 per cent in July 1932.",
            "Hitler was appointed chancellor on 30 January 1933 by a political decision.",
            "The Reichstag fire decree, the Enabling Act and the ban on rival organisations created a dictatorship.",
            "In August 1934 Hitler combined the offices of president and chancellor."),
    ],
))

# ---------------------------------------------------------------------------
# The Interwar Crises / Appeasement
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_INT, topic="Appeasement",
    title="Crises and concessions: Manchuria to the Anschluss, 1931-1938",
    slug="h6-appeasement-crises-1931-1938",
    minutes=24,
    summary="The chain of crises from Manchuria to the Anschluss, the choices of Britain and France in each, and the reasons given for appeasement.",
    objectives=[
        "Place the crises of 1931 to 1938 in order",
        "Describe the British and French response to each",
        "Explain the reasons for appeasement",
        "Judge whether appeasement was a policy or a series of reactions",
    ],
    key_concepts=["Appeasement", "League of Nations", "Remilitarisation", "Anschluss", "Collective security", "Rearmament"],
    blocks=[
        H("Introduction"),
        T("Before 1939 the word appeasement meant settling disputes by negotiation and concessions. It became an insult after the Second World War broke out. "
          "This lesson covers the crises up to the Anschluss. The next lesson covers Munich and the debate about the policy."),
        IMG("al-h6-appeasement-timeline.svg", alt="Timeline of crises from Manchuria in 1931 to the outbreak of war in September 1939", caption="Figure 1. Crises and appeasement, 1931 to 1939. Not to scale."),
        D("A policy of making concessions to dissatisfied powers in order to avoid war. In the 1930s it is mainly linked to British policy under Baldwin and Chamberlain and to French policy.", title="Appeasement"),
        H("The League tested: Manchuria and Abyssinia"),
        T("In 1931 Japanese forces took over Manchuria. The League of Nations condemned Japan, but it took no military action, and Japan left the League. "
          "In 1935 Mussolini invaded Abyssinia (Ethiopia). The League imposed limited sanctions that did not include oil. A British-French plan, the Hoare-Laval proposal, was leaked, caused anger, and was dropped. "
          "Many people lost confidence in the League as a way to stop aggression."),
        H("Germany under Hitler"),
        T("In 1933 Hitler left the Disarmament Conference and the League. In 1935 he announced conscription, breaking Versailles; Britain signed the Anglo-German Naval Agreement that year, "
          "which weakened the common front with France. On 7 March 1936 German troops entered the demilitarised Rhineland. France did not act without British support, and Britain did not want war. "
          "In 1936 Italy and Germany drew closer (the Rome-Berlin Axis), and both intervened in the Spanish Civil War, while Britain and France followed a policy of non-intervention."),
        H("The Anschluss, March 1938"),
        T("In March 1938 Germany forced the Austrian government to accept German troops, and Austria was joined to Germany (Anschluss). This broke the Treaty of Versailles. "
          "Britain and France protested but took no military action. Many in Austria welcomed the union, which complicated international responses."),
        H("Why appeasement?"),
        KEY("Reasons given at the time", "Weigh them rather than listing them.", cards=[
            ["Memory of the First World War", "Casualties of 1914 to 1918 made war seem the worst outcome; public opinion in Britain and France was strongly in favour of peace."],
            ["Economic limits", "The Depression restricted spending, and rearmament was slow."],
            ["Belief that Versailles was too harsh", "Many thought some German demands were reasonable."],
            ["Military fears", "Fear of bombing of cities; the British empire was far-flung and its defences stretched."],
            ["Fear of communism", "Some saw Germany as a barrier to the Soviet Union."],
            ["Isolated Britain and France", "The United States was isolationist; the Soviet Union was distrusted."],
        ]),
        EX("Model essay plan 1", intro="Explain why Britain and France did not oppose German remilitarisation of the Rhineland in March 1936.", steps=[
            S("Introduction", text="State the event. Judgement: lack of will and capacity, and doubts about whether the move was a threat."),
            S("Political reasons", text="France was divided and unwilling to act without British support; Britain saw the Rhineland as German territory in any case."),
            S("Military reasons", text="Neither country was ready for war."),
            S("Wider context", text="Attention on Abyssinia; belief that Versailles had been harsh."),
            S("Judgement", text="A chance to stop Hitler was lost, but it was not obvious at the time."),
        ]),
        EX("Model essay plan 2", intro="Assess the importance of the failure of the League of Nations in the rise of appeasement.", steps=[
            S("Introduction", text="Define collective security. Judgement: the League's failures made appeasement more likely but were not the only reason."),
            S("The League's failures", text="Manchuria and Abyssinia showed it could not stop aggression."),
            S("Other factors", text="Public opinion, economic limits, fear of war."),
            S("Link", text="Without a credible League, direct negotiation seemed the only option."),
            S("Judgement", text="The League's failure was important, but it interacted with domestic and economic factors."),
        ]),
        MISTAKE("Using hindsight", "Explain what leaders knew at the time, not what we know now."),
        MISTAKE("Blaming one person", "Many British and French politicians supported appeasement for different reasons."),
        QUIZ("Which event of 1936 broke the Treaty of Versailles and the Locarno agreements?",
             ["The Anschluss", "The remilitarisation of the Rhineland", "The invasion of Poland", "The Munich Agreement"], 1,
             "German troops entered the Rhineland on 7 March 1936.",
             feedback=["That was 1938.", "", "That was 1939.", "That was September 1938."]),
        QUIZ("Why did the Hoare-Laval plan of 1935 cause anger?",
             ["It proposed giving Italy large parts of Abyssinia", "It ended the League of Nations", "It banned the German army", "It gave Austria to Germany"], 0,
             "Many saw it as rewarding aggression.",
             feedback=["", "The League continued.", "It was unrelated to Germany.", "The Anschluss was in 1938."]),
        PQ("Explain two reasons why Britain was reluctant to go to war with Germany in the 1930s.",
           "Outline: (1) Memory of the human cost of the First World War and strong public opposition to war. (2) Economic difficulties and the slow state of rearmament, with fears about air attack."),
        PQ("Describe the response of Britain and France to the Anschluss.",
           "Outline: They protested but did not use force; the union was accepted in practice; many Austrians welcomed it."),
        PQ("How far was appeasement a consequence of the League's failures in Manchuria and Abyssinia?",
           "Outline: League failures showed collective security was weak. But appeasement also reflected public opinion, economics, and a belief in revising Versailles. Judgement: an important factor, within several."),
        SUM("Appeasement meant negotiating concessions to avoid war.",
            "The League failed to stop Japan in Manchuria (1931) and Italy in Abyssinia (1935).",
            "Hitler broke Versailles by conscription (1935), the Rhineland (1936) and the Anschluss (1938).",
            "Britain and France were influenced by memories of war, economic limits and military fears.",
            "Judge decisions by what was known at the time."),
    ],
))

LESSONS.append(lesson(
    module=M_INT, topic="Appeasement",
    title="Munich, the end of appeasement and the historians' debate",
    slug="h6-munich-and-the-appeasement-debate",
    minutes=26,
    summary="The Sudeten crisis and Munich Agreement of September 1938, the collapse of appeasement in 1939, and the changing interpretations from the 'Guilty Men' view to later reassessments.",
    objectives=[
        "Explain the Sudeten crisis and the Munich Agreement",
        "Explain how appeasement ended in 1939",
        "Describe the main interpretations of appeasement",
        "Write a balanced judgement on whether appeasement was justified",
    ],
    key_concepts=["Sudetenland", "Munich Agreement", "Guarantee to Poland", "Nazi-Soviet Pact", "Revisionist historians"],
    blocks=[
        H("Introduction"),
        T("Munich is the best-known moment of appeasement. In September 1938 Britain and France agreed to Germany taking the Sudetenland from Czechoslovakia. "
          "Within a year the policy had collapsed and a new world war began. This lesson asks why Munich happened, how appeasement ended and how historians judge it."),
        D("A border region of Czechoslovakia with a large German-speaking population. Hitler demanded its transfer to Germany in 1938.", title="Sudetenland"),
        H("The Sudeten crisis, 1938"),
        T("After the Anschluss Hitler pressed the Sudeten German party, led by Konrad Henlein, to make demands. Czechoslovakia was a democracy with a strong army and an alliance with France and the Soviet Union. "
          "In September 1938 British Prime Minister Neville Chamberlain flew to Germany three times. At Munich on 29 to 30 September, Britain, France, Italy and Germany agreed that Germany would take the Sudetenland. "
          "Czechoslovakia and the Soviet Union were not invited. Chamberlain returned claiming peace. Check the details and dates of the three visits in your textbook."),
        H("The collapse of appeasement, 1939"),
        T("In March 1939 German troops occupied the rest of Czechoslovakia, breaking the promises made at Munich. Britain and France then gave a guarantee to Poland (31 March 1939) and sped up rearmament. "
          "On 23 August 1939 Germany and the Soviet Union signed a non-aggression pact. On 1 September Germany invaded Poland, and on 3 September Britain and France declared war."),
        H("The debate"),
        KEY("Interpretations of appeasement", "Learn how views changed.", cards=[
            ["The 'Guilty Men' view (1940s)", "Appeasers were weak and foolish; war could have been prevented by firmness. Winston Churchill's later writing supported this view."],
            ["Revisionist view (1960s onwards)", "Historians with access to government papers, released after thirty years, argued that appeasers faced real limits: weak armed forces, divided public opinion and an uncertain empire."],
            ["Later views", "Some argue appeasement bought time for rearmament; others say it strengthened Germany and lost the support of Czechoslovakia and the Soviet Union."],
        ], note="The Czechs paid the main price at Munich; do not ignore their perspective."),
        T("A.J.P. Taylor in 1961 argued that Hitler was an opportunist and that appeasers responded to the circumstances. His book caused a major debate. Check authors and arguments in your textbook."),
        EX("Model essay plan 1", intro="'Appeasement was a wise policy that failed.' Discuss.", steps=[
            S("Introduction", text="Define appeasement. Judgement: understandable in context but unwise at Munich."),
            S("For", text="Public opinion; limited armed forces; hope to avoid a second world war; time for rearmament."),
            S("Against", text="Hitler's demands grew; Czechoslovakia was strong and had allies; Soviet Union excluded; moral cost."),
            S("Context", text="Hindsight versus knowledge at the time."),
            S("Judgement", text="A rational response to weakness in earlier years but a mistake in 1938 when stronger options existed."),
        ]),
        EX("Model essay plan 2", intro="Explain why the Munich Agreement was reached in September 1938.", steps=[
            S("Point 1: fear of war", text="Chamberlain and Daladier wanted to avoid a general war."),
            S("Point 2: military weakness", text="British and French armed forces were not ready."),
            S("Point 3: belief in Hitler's aims", text="They believed Hitler's claim that the Sudetenland was his last demand."),
            S("Link", text="The decision came from fear and misjudgement, not agreement among equals."),
        ]),
        MISTAKE("Saying Czechoslovakia agreed at Munich", "Czechoslovakia was not invited. Its government was told to accept."),
        MISTAKE("Judging by hindsight only", "Show what leaders knew in 1938 and then compare with later events."),
        QUIZ("Which countries signed the Munich Agreement?",
             ["Britain, France, Italy and Germany", "Britain, France and Czechoslovakia", "Germany and the Soviet Union", "Britain and the United States"], 0,
             "Four powers signed; Czechoslovakia was not present.",
             feedback=["", "Czechoslovakia was excluded.", "That was the 1939 pact.", "The US did not take part."]),
        QUIZ("What event ended appeasement in March 1939?",
             ["The Anschluss", "German occupation of the rest of Czechoslovakia", "The Rhineland", "Munich"], 1,
             "It showed that Hitler's aims went beyond German-speaking areas.",
             feedback=["That was 1938.", "", "That was 1936.", "That was September 1938."]),
        PQ("Explain two reasons why Chamberlain signed the Munich Agreement.",
           "Outline: (1) He wished to avoid a war for which Britain was not ready and which public opinion opposed. (2) He believed that Hitler's demands were limited and that concessions could preserve peace."),
        PQ("Describe how the policy of appeasement came to an end in 1939.",
           "Outline: March 1939 occupation of Prague; guarantee to Poland on 31 March; rearmament; Nazi-Soviet Pact in August; invasion of Poland on 1 September; war declared on 3 September."),
        PQ("Assess the view that appeasement was justified.",
           "Outline: Justified: public opinion, weak forces, empire concerns, time to rearm. Not justified: gave Hitler victories without war, lost Czech strength and Soviet cooperation. Judgement: understandable in context, but Munich was a serious mistake."),
        SUM("At Munich (29 to 30 September 1938) Britain, France, Italy and Germany agreed the transfer of the Sudetenland.",
            "Czechoslovakia and the Soviet Union were not present.",
            "In March 1939 Germany occupied Prague; Britain and France guaranteed Poland.",
            "War began on 1 September 1939, with British and French declarations on 3 September.",
            "Historians range from the 'Guilty Men' view to revisionist views."),
    ],
))

# ---------------------------------------------------------------------------
# Examination / Practice paper
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_EXAM, topic="Practice paper",
    title="Approaching the Lower Sixth History practice paper",
    slug="h6-exam-approaching-the-practice-paper",
    minutes=20,
    summary="How to approach a mixed History practice paper that tests knowledge and short source questions, with a revision plan by topic, a time plan labelled as KKEVO advice, and a reminder to check the real paper format.",
    objectives=[
        "Use a two-pass method on a multiple-choice paper",
        "Recognise dates and names that are easy to confuse",
        "Handle short quoted sources in multiple-choice questions",
        "Plan revision across all four modules of the year",
    ],
    key_concepts=["Practice paper", "Two-pass method", "Distractor", "Time planning", "Revision plan"],
    blocks=[
        H("Introduction"),
        T("The KKEVO practice paper for Lower Sixth History has 40 multiple-choice questions on the whole year: Cameroon 1884 to 1945, European revolutions and unifications, imperialism and the First World War, and the interwar crises. "
          "Some questions test knowledge of dates, names and events. Some ask you to interpret a short source that KKEVO has written or paraphrased. They are KKEVO practice questions, not copies of any past paper."),
        D("The real A Level History papers are usually written essays and source questions. **Check the real paper format, number of questions and timing with your teacher.** "
          "The multiple-choice practice paper and its 90-minute time limit are KKEVO practice settings, not official instructions.", title="Check the real format"),
        H("A two-pass method"),
        KEY("Using time sensibly", "This is KKEVO advice.", cards=[
            ["Pass 1", "Answer every question you can do quickly. Mark the others and move on."],
            ["Pass 2", "Return to marked questions and eliminate wrong options."],
            ["Final minutes", "Make sure every question has an answer and check any 'NOT' or 'EXCEPT' questions again."],
        ], note="With 40 questions in 90 minutes, KKEVO's practice setting gives just over two minutes per question."),
        H("Spotting traps"),
        T("Distractors are often real facts from another date or place. For example, 12 July 1884 and 14 July 1884 are both real dates; one is the treaty and one is the flag. "
          "Konigsgratz (1866) and Sedan (1870) are real battles. Milner-Simon (1919) and Versailles (1919) are both from 1919. Make a list of such pairs as you revise."),
        EX("Worked example 1: eliminate by date", intro="Which event happened in 1919? A. The Anglo-German agreement on Yola and the sea. B. The Milner-Simon declaration. C. The Franco-German treaty about Morocco. D. The Berlin Conference opened.", steps=[
            S("Link each option to a date", text="A is 1913. C is 1911. D is 1884."),
            S("Cross out", text="A, C and D are real events with different dates."),
            S("Answer", text="B, the Milner-Simon declaration, 10 July 1919."),
        ]),
        EX("Worked example 2: short source question", intro="Invented practice source: 'The assembly offered the crown, but the king would not take what the people had made.' Which event does this fit? A. Frankfurt crown offer in 1849. B. Plombieres. C. The Munich Agreement. D. The Berlin Conference.", steps=[
            S("Underline clues", text="Assembly, crown, king refusing."),
            S("Match", text="This matches the Frankfurt Parliament offering the crown to Frederick William IV in April 1849."),
            S("Answer", text="A. The other events involve no assembly offering a crown."),
        ]),
        H("A revision plan by module"),
        T("Cameroon 1884 to 1945: treaty, borders, three colonial systems, economy and education. Europe: causes and failure of 1848; steps of Italian and German unification. "
          "Imperialism and the First World War: Scramble events and interpretations; July Crisis; Versailles and mandates. Interwar: Mussolini, Weimar and Hitler, appeasement. "
          "Take the practice paper once, look at your topic scores, and revise the weakest topics first."),
        MISTAKE("Guessing from familiar words", "A name or date that you recognise may belong to another event. Check what the question asks."),
        MISTAKE("Spending too long on one question", "Mark it and return."),
        QUIZ("Why is a two-pass method helpful?",
             ["It guarantees every answer is right", "It secures easy marks first and leaves time for harder questions", "It avoids reading the questions", "It makes the paper shorter"], 1,
             "You collect easy marks first and then think harder about difficult questions.",
             feedback=["No method guarantees this.", "", "You must read every question.", "The paper length is fixed."]),
        QUIZ("Which statement about the KKEVO practice paper is correct?",
             ["It is a past paper", "It uses KKEVO practice settings and the real format should be checked with the teacher", "It is set by the Board", "It has no time limit"], 1,
             "The practice paper is KKEVO's own.",
             feedback=["It is not a past paper.", "", "It is not set by the Board.", "It has a 90-minute practice limit."]),
        PQ("List the pairs of similar dates or events that you find hardest to separate.",
           "Sample answer: 12 July and 14 July 1884; Versailles (28 June 1919) and Milner-Simon (10 July 1919); Konigsgratz and Sedan; Plombieres and Villafranca; 1922 March on Rome and 1925 dictatorship. Add your own."),
        PQ("Why should a source in a question be read before looking at the options?",
           "Reading the source first helps you find clues without being led by the options. Underline the key words and then compare with each option."),
        PQ("Make a three-line revision plan for the week before the practice paper.",
           "Sample: Day 1 to 2: Cameroon. Day 3: Europe. Day 4: Imperialism and the First World War. Day 5: Interwar. Day 6: attempt the practice paper. Day 7: revise the weakest topic scores."),
        SUM("Check the real paper format and timing with your teacher.",
            "Use a two-pass method and eliminate wrong options.",
            "Beware of real dates and names that belong to other events.",
            "Read short sources for clues before looking at options.",
            "Revise the weakest topics first."),
    ],
))
