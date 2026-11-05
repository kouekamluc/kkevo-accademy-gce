"""A Level History (0760), Lower Sixth: draft lessons for reviewer checking."""

from .dsl import *  # noqa: F403

COURSE = ("history", "lower-sixth")

LESSONS = []

# ---------------------------------------------------------------------------
# Cameroon 1884–1945 / Treaties and borders
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Cameroon 1884–1945",
    topic="Treaties and borders",
    title="The Germano-Douala Treaty and the making of Cameroon's borders",
    slug="germano-douala-treaty-and-borders",
    minutes=25,
    summary="How the Germano-Douala Treaty of 12 July 1884, the Kings' Memorandum and later Franco-German and Anglo-German conventions created Kamerun and shaped its frontiers.",
    objectives=[
        "Explain why the Duala kings signed the treaty of 12 July 1884",
        "Describe the main conditions in the Kings' Memorandum and assess how far Germany respected them",
        "Outline the Anglo-German and Franco-German conventions that fixed Kamerun's borders",
        "Evaluate the view that Cameroon's borders were drawn without African participation",
    ],
    key_concepts=["Germano-Douala Treaty", "Kings' Memorandum", "Protectorate", "Boundary convention", "Neukamerun"],
    blocks=[
        H("Introduction"),
        T("Every map of Cameroon you have seen is the result of agreements made between 1884 and 1919. "
          "Some were signed with Duala rulers on the Wouri estuary. Most were signed between European "
          "governments in Berlin, London and Paris, often without any Cameroonian present.\n\n"
          "At A Level you must do more than list treaties. You must explain **why** they were signed, "
          "**who** gained from them, and **how far** Africans shaped the outcome."),
        D("A treaty signed on **12 July 1884** by Duala rulers, notably King Bell (Ndumbe Lobe Bell) and King Akwa "
          "(Dika Mpondo Akwa), with representatives of the German trading firms Woermann and Jantzen und Thormählen. "
          "The kings transferred sovereignty over their territory to the German firms, which then passed it to the German Empire.",
          title="Germano-Douala Treaty"),
        D("A list of conditions attached to the treaty by the Duala signatories. It asked, among other things, that "
          "Duala land should not be taken, that existing customs and marriages be respected, and that the Duala "
          "keep their role as middlemen in the trade with the interior.",
          title="Kings' Memorandum"),
        H("Why the Duala kings signed"),
        T("By the 1880s the Duala chiefs faced problems. Their authority over their own people was weakening, "
          "rival houses (Bell, Akwa, Deido and others) competed with each other, and European traders wanted to "
          "trade directly with the interior, which threatened the Duala middleman monopoly."),
        T("For years some Duala rulers had written to Britain asking for British protection. Britain hesitated. "
          "German traders, already active in the estuary, took the opportunity. The German consul-general "
          "Gustav Nachtigal arrived and the German flag was raised on 14 July 1884. The British consul Edward Hewett "
          "arrived a few days later, too late to secure the coast for Britain."),
        KEY("Two ways to read the treaty", "Historians stress different sides of the same event.", cards=[
            ["Eurocentric reading", "Germany, under Bismarck, acquired protectorates in 1884 for reasons of trade, domestic politics and diplomacy. The Duala appear as objects of European rivalry."],
            ["Afrocentric reading", "The Duala kings were active negotiators who chose a protector to serve their own aims and wrote conditions into the Memorandum. Germany later broke those conditions."],
        ], note="A strong essay uses both readings and reaches a judgement."),
        H("Resistance and broken promises"),
        T("Not all Duala accepted the treaty. Lock Priso of Hickory Town (Bonabéri) refused to sign, and in December 1884 "
          "German forces attacked Hickory Town. The treaty divided Duala society from the start."),
        T("Later German policy ignored the Memorandum. German firms pushed into the interior and broke the middleman "
          "trade. In the 1910s the colonial government planned to expropriate Duala land on the Joss plateau. "
          "Rudolf Duala Manga Bell, who led protests against this, was executed by the Germans on 8 August 1914."),
        H("Fixing the borders"),
        T("The coastal treaty gave Germany only a small area. The borders of Kamerun were then extended inland by "
          "conventions with Britain (to the west) and France (to the south and east)."),
        KEY("The main boundary agreements", "Learn these as a chronological chain.", cards=[
            ["Anglo-German agreements (1885–1886, 1893, 1913)", "Fixed the western border with British Nigeria, from the Rio del Rey area on the coast towards Lake Chad. The 1913 agreement placed the Bakassi peninsula on the German side."],
            ["Franco-German conventions (1885, 1894)", "Fixed the southern border with French Gabon (1885) and the eastern border with French territory towards Lake Chad (1894)."],
            ["Franco-German treaty of 4 November 1911", "After the Agadir (second Moroccan) crisis, France ceded large areas of French Equatorial Africa to Germany (Neukamerun) in return for German acceptance of a French protectorate in Morocco."],
        ]),
        T("During the First World War, Kamerun was conquered by British, French and Belgian forces (1914–1916). "
          "Britain and France divided it, first provisionally in 1916 and then by the Milner-Simon declaration of "
          "10 July 1919. Neukamerun returned to French Equatorial Africa. In 1922 the League of Nations confirmed "
          "British and French administration as mandates."),
        EX("Essay plan 1", intro="'The Duala kings signed the Germano-Douala Treaty of 1884 to protect their own interests.' How far do you agree?", steps=[
            S("Introduction and line of argument", text="Define the treaty and its date. State a judgement: the kings acted mainly to protect their trade and authority, but they misjudged German intentions."),
            S("Argument: commercial self-interest", text="Evidence: the Kings' Memorandum demanded protection of the middleman trade and of Duala land. This shows the kings bargained for specific economic aims."),
            S("Argument: political security", text="Evidence: weakening authority and rivalry between the Bell and Akwa houses; earlier requests for British protection show the kings wanted an outside protector."),
            S("Counter-argument: European pressure and division", text="German traders and Nachtigal pushed the deal; Lock Priso's refusal and the attack on Hickory Town show not all Duala agreed, so 'the Duala' did not act as one."),
            S("Judgement", text="The treaty was an African choice made under pressure. Self-interest explains why the kings signed, but the later breach of the Memorandum shows they had little power to enforce their conditions."),
        ]),
        EX("Essay plan 2", intro="Assess the importance of European diplomacy in fixing the borders of Kamerun between 1884 and 1919.", steps=[
            S("Introduction", text="Define the period and the key agreements. Judgement: diplomacy between European powers was decisive; African agency mattered mainly at the coast."),
            S("Anglo-German agreements", text="Evidence: the 1885–1886, 1893 and 1913 agreements set the western border and the position of Bakassi without African consultation."),
            S("Franco-German agreements and 1911", text="Evidence: the 1885 and 1894 conventions; the 1911 exchange linked to Morocco shows borders were bargaining chips in wider European crises."),
            S("Counter-argument: African and military factors", text="Coastal treaties, local resistance and the military conquest of 1914–1916 also shaped the outcome; the partition of 1916–1919 followed the battlefield."),
            S("Judgement", text="Diplomacy drew the lines, but war and conquest decided who ruled inside them after 1916."),
        ]),
        MISTAKE("Confusing the treaty date with the flag-raising", "The treaty was signed on 12 July 1884; the German flag was raised on 14 July. Do not swap them."),
        MISTAKE("Treating 'the Duala' as one group", "Rival houses had different interests and Lock Priso refused to sign. Show the divisions; examiners reward this."),
        MISTAKE("Listing treaties without explaining them", "Every agreement you mention should support an argument about causes, power or consequences."),
        QUIZ("What did France gain from the Franco-German treaty of November 1911?",
             ["The Bakassi peninsula", "German acceptance of a French protectorate in Morocco", "The whole of Kamerun", "Control of Douala port"], 1,
             "The 1911 treaty ended the Agadir crisis: Germany accepted French control of Morocco and received Neukamerun in return.",
             feedback=["Bakassi was placed in Kamerun by the 1913 Anglo-German agreement.", "",
                       "France only gained most of Kamerun after the First World War.", "Douala remained German until 1914."]),
        QUIZ("Which document listed the Duala kings' conditions for accepting German rule?",
             ["The Kings' Memorandum", "The Milner-Simon declaration", "The Berlin Act", "Article 22 of the League Covenant"], 0,
             "The Kings' Memorandum set out Duala conditions such as protection of land and trade.",
             feedback=["", "This 1919 declaration divided Kamerun between Britain and France.",
                       "The Berlin Act (1885) set rules among European powers.", "Article 22 created the mandate system in 1919."]),
        PQ("Explain two reasons why Britain lost the race to annex the Cameroon coast in 1884.",
           "Outline: (1) British hesitation: the government delayed responding to Duala requests for protection, unwilling to take on cost and responsibility. "
           "(2) German speed: German traders already in the estuary negotiated the treaty of 12 July 1884 and the flag was raised on 14 July, before Hewett arrived. "
           "A good answer links these to Bismarck's sudden colonial policy in 1884."),
        PQ("'Germany respected the terms of the Kings' Memorandum.' Discuss.",
           "Outline: Agree only for the early years, when Germany relied on Duala cooperation. Disagree: German firms broke the middleman monopoly by moving inland; "
           "the land expropriation plan on the Joss plateau and the execution of Rudolf Duala Manga Bell in 1914 directly violated the Memorandum's protection of land. "
           "Judgement: the Memorandum had no means of enforcement, so German interests prevailed."),
        PQ("To what extent were Cameroon's borders a product of events outside Africa?",
           "Outline: Outside Africa: the 1911 treaty was a by-product of the Moroccan crisis; the 1919 partition followed the First World War and was confirmed by the League. "
           "Inside Africa: coastal treaties with the Duala, local resistance and the 1914–1916 Kamerun campaign. Judgement: the outlines were mostly decided in European capitals, but African events supplied the starting point and the military facts."),
        SUM("The Germano-Douala Treaty was signed on 12 July 1884; the German flag was raised on 14 July.",
            "The Kings' Memorandum shows the Duala bargained for protection of land, customs and trade.",
            "Germany later broke those conditions, leading to protest and the execution of Rudolf Duala Manga Bell in 1914.",
            "Anglo-German and Franco-German conventions (1885–1913) fixed the borders; the 1911 treaty created Neukamerun.",
            "After 1916 Britain and France divided Kamerun; the League confirmed the mandates in 1922."),
    ],
))

# ---------------------------------------------------------------------------
# Cameroon 1884–1945 / Comparative colonial rule
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Cameroon 1884–1945",
    topic="Comparative colonial rule",
    title="German, British and French rule in Cameroon compared",
    slug="comparative-colonial-rule-in-cameroon",
    minutes=28,
    summary="Compares German imperial policy, British indirect rule and French assimilation and association in Cameroon, and evaluates how different they really were in practice.",
    objectives=[
        "Describe the main features of German rule in Kamerun (1884–1916)",
        "Explain British indirect rule in the British Cameroons and French assimilation and association in French Cameroun",
        "Compare the three systems in theory and in practice",
        "Write a balanced comparative essay with a clear judgement",
    ],
    key_concepts=["Indirect rule", "Assimilation", "Association", "Indigénat", "Mandate", "Native Authority"],
    blocks=[
        H("Introduction"),
        T("Cameroon is unusual: within about forty years it was ruled by three European powers. Germany ruled Kamerun "
          "from 1884 until conquest in 1914–1916. Britain and France then governed their parts as League of Nations "
          "mandates from 1922.\n\nThis gives historians a natural experiment. Did the systems really differ, or were "
          "they different labels for the same colonial domination?"),
        D("A system in which the colonial power governs through existing African rulers and institutions, called "
          "Native Authorities, under the supervision of European officers. It is closely linked to Frederick Lugard in Nigeria.",
          title="Indirect rule"),
        D("The French ideal that colonised people could become French in culture, language and law, and gain the rights "
          "of French citizens. In practice very few Africans achieved this status.",
          title="Assimilation"),
        D("A later, more practical French policy that accepted African societies would stay different and should be "
          "ruled in partnership with chosen chiefs, while France kept firm central control.",
          title="Association"),
        D("The French code of administrative punishments that let officials punish 'subjects' (non-citizens) without "
          "trial, for example by fines or imprisonment.", title="Indigénat"),
        H("German imperial policy, 1884–1916"),
        T("German rule began as a commercial protectorate and became a military and administrative conquest of the "
          "interior. Expeditions such as those of Eugen Zintgraff in the Grassfields met strong resistance, and "
          "Germany fought wars against peoples such as the Bulu and the Nso."),
        T("Governor Jesko von Puttkamer (1895–1907) encouraged large plantation companies around Mount Cameroon, "
          "which took fertile Bakweri land. Buea became the capital. Germany relied heavily on forced labour for "
          "plantations, roads and porterage. Some cooperative chiefs, such as Fon Galega of Bali, were used as allies."),
        T("Germany also built infrastructure: the port of Douala, railways inland from Douala, and roads. Historians "
          "debate whether this was 'development' or simply the means of extraction."),
        H("British indirect rule, 1916–1961"),
        T("Britain administered its two strips of Cameroon as part of Nigeria. The northern part was linked to the "
          "Northern Provinces and the southern part to the Southern (later Eastern) Provinces. Chiefs and councils "
          "became Native Authorities collecting tax and running local courts."),
        T("Historians often describe British rule in the Cameroons as **neglect**: few officials, little investment, "
          "and decisions taken in Lagos or Enugu. German plantations were sold back to German owners in the 1920s and "
          "later became the basis of the Cameroon Development Corporation (1947)."),
        H("French assimilation and association, 1916–1960"),
        T("France governed French Cameroun as a separate mandate with its own commissioner, with the capital at Yaoundé. "
          "French rule was more direct and centralised. Chiefs were often appointed by the administration and acted as "
          "agents of French officials, not as independent rulers."),
        T("Africans were 'subjects' under the indigénat and had to perform compulsory labour (prestation). French rule "
          "invested more than British rule in roads and railways, such as extending the railway from Douala to Yaoundé, "
          "but much of this work used forced labour."),
        KEY("Theory versus practice", "The labels differ more than the experience of ordinary people did.", cards=[
            ["German", "Direct military conquest, plantations and forced labour; used allied chiefs where useful."],
            ["British", "Indirect rule through Native Authorities; low cost, little investment, ruled from Nigeria."],
            ["French", "Assimilation as an ideal, association in practice; centralised, indigénat and labour tax."],
        ], note="Many historians argue all three relied on chiefs, coercion and extraction. Note also that the mandate system added League supervision after 1922, though it was weak."),
        EX("Essay plan 1", intro="Compare and contrast British and French methods of administration in Cameroon between 1916 and 1945.", steps=[
            S("Introduction", text="Define indirect rule, assimilation and association. Judgement: the methods differed in structure but both served colonial control and extraction."),
            S("Similarity: use of chiefs", text="Both used African chiefs to collect tax and keep order; under France chiefs were more clearly administrative agents."),
            S("Difference: centralisation", text="British Cameroons ruled as part of Nigeria with few officials; French Cameroun had its own centralised administration in Yaoundé."),
            S("Difference: law and labour", text="French indigénat and prestation versus British Native Authority courts; both used compulsory labour in some form."),
            S("Difference: investment", text="France invested more in infrastructure (railway to Yaoundé); British rule is often called neglect."),
            S("Judgement", text="The contrast is real in administration and investment, but for most Cameroonians both systems meant taxation, coercion and little political voice."),
        ]),
        EX("Essay plan 2", intro="'German rule in Kamerun was more brutal than British or French rule.' How far do you agree?", steps=[
            S("Introduction", text="Set criteria: violence of conquest, labour, land seizure, political rights. Judgement: German rule was more violent in conquest, but forced labour continued under France."),
            S("Argument for", text="Evidence: wars of conquest in the interior; seizure of Bakweri land for plantations; execution of Rudolf Duala Manga Bell and Martin-Paul Samba in 1914."),
            S("Counter-argument", text="Evidence: French prestation and indigénat; forced labour on the Douala–Yaoundé railway; British neglect left people with few services."),
            S("Context", text="German rule covered the conquest phase, when violence was greatest everywhere; mandates gave some, weak, international oversight."),
            S("Judgement", text="German rule was more openly violent, but the difference is partly one of timing; coercion was common to all three."),
        ]),
        MISTAKE("Describing theory as if it were practice", "Assimilation was rarely applied; say so. Examiners reward the gap between policy and reality."),
        MISTAKE("Forgetting the mandate status", "After 1922 Britain and France ruled as League mandates, not ordinary colonies. Mention it and assess its limited effect."),
        MISTAKE("Writing three separate descriptions", "A comparative question needs point-by-point comparison, not three blocks of narrative."),
        QUIZ("How was the British Cameroons administered between the wars?",
             ["As a separate colony with its own governor", "As part of Nigeria", "Jointly with France", "Directly from Buea by a League commissioner"], 1,
             "Britain ruled its share of Cameroon as part of Nigeria, divided between northern and southern provinces.",
             feedback=["It had no separate governor at this time.", "", "There was no joint Anglo-French administration after 1916.", "The League supervised but did not govern."]),
        QUIZ("Which feature belongs to French rule rather than British rule?",
             ["Native Authorities", "The indigénat", "Rule from Lagos", "Selling plantations back to German owners"], 1,
             "The indigénat was the French code of summary punishments for subjects.",
             feedback=["Native Authorities were the basis of British indirect rule.", "", "Lagos was the British capital of Nigeria.", "This happened in the British Cameroons in the 1920s."]),
        PQ("Explain two features of German colonial administration in Kamerun.",
           "Outline: (1) Military conquest of the interior through expeditions and wars against resisting peoples. (2) A plantation economy around Mount Cameroon under Puttkamer, using land taken from the Bakweri and forced labour. Explain each with one example."),
        PQ("How far did French policy in Cameroun move from assimilation to association?",
           "Outline: Assimilation was the official ideal but few Cameroonians became citizens; in practice France ruled through appointed chiefs and the indigénat, which fits association. "
           "Judgement: the shift was mainly a recognition of what was already happening; both stressed French control."),
        PQ("Assess the view that British rule in the Cameroons was a policy of neglect.",
           "Outline: For: few officials, administered from Nigeria, little investment, plantations returned to German owners. Against: Native Authorities provided some local government; the Cameroon Development Corporation (1947) showed later investment. "
           "Judgement: largely true for 1922–1945, less so after 1945."),
        SUM("Cameroon was ruled by Germany (1884–1916), then by Britain and France as mandates from 1922.",
            "German rule meant conquest, plantations and forced labour.",
            "Britain used indirect rule through Native Authorities and governed the territory from Nigeria.",
            "France preached assimilation but practised centralised association with the indigénat and labour tax.",
            "Strong essays compare point by point and test theory against practice."),
    ],
))

# ---------------------------------------------------------------------------
# Cameroon 1884–1945 / Social and economic change
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Cameroon 1884–1945",
    topic="Social and economic change",
    title="Social and economic change in colonial Cameroon, 1884–1945",
    slug="social-and-economic-change-colonial-cameroon",
    minutes=26,
    summary="Urbanization, forced labour, mission education, the early press and early associations such as Jeucafra and Unikamerun, and how they prepared the ground for nationalism.",
    objectives=[
        "Explain the causes and effects of urban growth in Douala, Victoria and Yaoundé",
        "Assess the role of forced labour in the colonial economy",
        "Evaluate the impact of mission education and the early press",
        "Explain why associations such as Jeucafra emerged in the late 1930s",
    ],
    key_concepts=["Urbanization", "Forced labour", "Mission education", "Évolué", "Jeucafra", "Unikamerun"],
    blocks=[
        H("Introduction"),
        T("Colonial rule changed where Cameroonians lived, how they worked, what they learned and how they spoke "
          "about politics. These changes are the background to the nationalist movements after 1945.\n\n"
          "A Level questions ask you to weigh **benefits** against **costs**, and to judge who gained."),
        D("The growth of towns as a share of the population. In Cameroon it was driven by ports, railways, "
          "administration and plantations.", title="Urbanization"),
        D("Labour that people were obliged to perform for the colonial state or for companies, often for little or "
          "no pay. It included porterage, road and railway building, and plantation work.", title="Forced labour"),
        D("A term used in French territories for Western-educated Africans, such as clerks, teachers and catechists, "
          "who were seen as having adopted French ways.", title="Évolué"),
        H("Urbanization"),
        T("Douala grew as the main port and the start of the railways. Victoria (now Limbe) grew with the plantations "
          "around Mount Cameroon. Buea became the German capital, and Yaoundé became the French capital after the war."),
        T("Towns attracted migrants seeking wages, schools and trade. They also brought overcrowding, segregation "
          "between European and African quarters, and new social groups such as clerks, artisans and dock workers."),
        H("Forced labour and the colonial economy"),
        T("The colonial economy was built on cash crops (cocoa, palm products, bananas, rubber, timber) and on the "
          "transport needed to export them. All three colonial powers relied on compulsory labour."),
        T("Under Germany, workers were recruited, often by force, for plantations and porterage. Under France, "
          "the prestation required subjects to work for the administration each year, and the extension of the railway "
          "from Douala to Yaoundé used forced labour with high mortality. Under Britain, plantation labour drew "
          "migrants from the Grassfields and from Nigeria."),
        TIP("Avoid quoting death tolls or labour figures unless your textbook gives a reliable source. Describe the scale in words instead."),
        H("Mission education"),
        T("Schools were run mostly by missions. The English Baptist Alfred Saker had worked in Douala and founded "
          "Victoria in 1858, before German rule. Under Germany, the Basel Mission (Protestant) took over Baptist work "
          "from 1886 and the Catholic Pallottine Fathers arrived in 1890. American Presbyterians worked in the south."),
        T("Mission schools taught literacy, Christianity and practical skills, and trained catechists, teachers and "
          "clerks. They also spread European languages and attitudes, and could weaken local religions and customs. "
          "Mission-educated Cameroonians later formed much of the nationalist leadership."),
        H("The early press and early associations"),
        T("Literate townspeople, especially in Douala, began to read and produce newspapers and petitions. "
          "Petitions to the League of Nations from Duala leaders in the 1920s and 1930s protested land seizures and "
          "French policies. The press and petitions gave educated Cameroonians a public voice."),
        T("In the late 1930s Nazi Germany demanded the return of its former colonies, including Cameroon. In response, "
          "the French encouraged the founding of **Jeucafra** (Jeunesse camerounaise française) in 1938 to show that "
          "Cameroonians preferred France. Paul Soppo Priso was among its leading figures. Although sponsored by France, "
          "it gave Cameroonians experience of organisation and debate, and after 1945 it was reorganised as Unicafra."),
        T("**Unikamerun** is named in the syllabus among early movements that promoted the idea of a single, united "
          "Kamerun across the British and French zones. Check its exact founding date, founders and aims in your class "
          "notes or textbook before using details in an essay."),
        KEY("Interpreting change", "Historians weigh colonial change differently.", cards=[
            ["Modernisation view", "Towns, schools, railways and cash crops brought new opportunities and created the educated class that led independence."],
            ["Exploitation view", "Change served colonial extraction; forced labour, land seizure and low wages meant most Cameroonians bore the costs."],
            ["Agency view", "Cameroonians used schools, towns and the press for their own ends, turning colonial tools into weapons of protest."],
        ]),
        EX("Essay plan 1", intro="'Colonial rule brought more benefits than costs to the people of Cameroon between 1884 and 1945.' Discuss.", steps=[
            S("Introduction", text="Define benefits and costs and for whom. Judgement: costs outweighed benefits for most people, though a small educated group gained."),
            S("Benefits: infrastructure and education", text="Railways and the port of Douala; mission schools training teachers and clerks."),
            S("Costs: labour and land", text="Forced labour under all three powers; Bakweri land loss; Duala land expropriation."),
            S("Unequal distribution", text="Gains concentrated in towns and among évolués; rural people carried most burdens."),
            S("Judgement", text="Infrastructure was built for export, not welfare; the main lasting benefit, education, also created the leaders who challenged colonial rule."),
        ]),
        EX("Essay plan 2", intro="Explain why educated Cameroonians formed associations such as Jeucafra in the late 1930s.", steps=[
            S("Introduction", text="Context: mission education and urban growth produced an educated class. Judgement: the immediate cause was the German colonial claim, but deeper causes were social change."),
            S("Immediate cause", text="Nazi Germany's demand for colonies; French sponsorship of Jeucafra in 1938 to show loyalty to France."),
            S("Long-term causes", text="Schools, towns and the press created people able and wanting to organise."),
            S("Cameroonian aims", text="Members used the association to press for reforms and a greater voice, not only to serve France."),
            S("Judgement", text="France supplied the occasion, but social change supplied the members; Jeucafra was a step towards post-1945 politics."),
        ]),
        MISTAKE("Inventing statistics", "Do not invent numbers of workers or deaths. Describe scale carefully and cite only figures you can support."),
        MISTAKE("Seeing Jeucafra as nationalist from the start", "It was founded with French encouragement as a pro-French body. Explain how it later became a training ground for nationalists."),
        QUIZ("Why did the French encourage the founding of Jeucafra in 1938?",
             ["To prepare Cameroon for independence", "To counter German demands for the return of Cameroon", "To organise forced labour", "To unite the British and French zones"], 1,
             "Jeucafra was meant to show that Cameroonians preferred France when Nazi Germany claimed its former colonies.",
             feedback=["France had no independence plan in 1938.", "", "Forced labour was organised through the administration and chiefs.", "French policy did not seek reunification."]),
        PQ("Explain two effects of mission education in colonial Cameroon.",
           "Outline: (1) It created a literate group of teachers, clerks and catechists who later led political movements. (2) It spread Christianity and European languages, sometimes weakening local beliefs and customs. Give a named mission for each."),
        PQ("How important was forced labour to the colonial economy of Cameroon?",
           "Outline: Very important: plantations, porterage, roads and the Douala–Yaoundé railway relied on it under Germany and France. Other factors: cash-crop farming by Cameroonians (cocoa), migrant wage labour and trade. Judgement: forced labour was central to building the export infrastructure."),
        PQ("Assess the impact of urbanization on Cameroonian society before 1945.",
           "Outline: New social groups and wage work; schools and the press concentrated in towns; overcrowding and segregation; towns as centres of protest such as Duala petitions. Judgement: towns were where colonial change was most intense and where political awareness grew."),
        SUM("Douala, Victoria, Buea and Yaoundé grew as ports, plantation centres and capitals.",
            "All three colonial powers used forced labour for plantations, porterage and railways.",
            "Missions (Baptist, Basel, Pallottine, Presbyterian) provided most schooling and shaped the future elite.",
            "Petitions and the press gave educated Cameroonians a voice; Jeucafra (1938) began as a pro-French body.",
            "Weigh benefits against costs and show who gained from change."),
    ],
))

# ---------------------------------------------------------------------------
# European Revolutions & Unifications / 1848 revolutions
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="European Revolutions & Unifications",
    topic="1848 revolutions",
    title="The revolutions of 1848: causes, course and failure",
    slug="revolutions-of-1848",
    minutes=28,
    summary="Why revolutions broke out across Europe in 1848, the roles of liberalism, socialism and nationalism, events in France, Germany and Austria, and why they failed.",
    objectives=[
        "Explain the long-term and short-term causes of the 1848 revolutions",
        "Distinguish liberal, socialist and nationalist aims",
        "Outline the course of revolution in France, the German states and the Austrian Empire",
        "Evaluate the reasons for the failure of the revolutions",
    ],
    key_concepts=["Liberalism", "Socialism", "Nationalism", "Frankfurt Parliament", "Counter-revolution"],
    blocks=[
        H("Introduction"),
        T("In 1848 revolutions broke out in Paris, Vienna, Berlin, Milan, Budapest and many other cities within a few "
          "weeks. Historians call it the 'springtime of the peoples'. By 1849 almost all of them had been defeated.\n\n"
          "The key A Level questions are: why did so many revolutions happen at once, and why did they fail?"),
        D("The belief in constitutional government, elected parliaments, the rule of law, and freedoms of speech, press "
          "and property. Its main supporters were the educated middle classes.", title="Liberalism"),
        D("Ideas that society and the economy should be organised for the benefit of workers, for example through the "
          "right to work. In 1848 Marx and Engels published the Communist Manifesto, though it had little immediate influence.",
          title="Socialism"),
        D("The belief that each nation, defined by language and culture, should have its own state. It inspired Germans, "
          "Italians, Hungarians, Czechs and others.", title="Nationalism"),
        H("Causes"),
        T("Long-term causes included resentment of the conservative order created at the Congress of Vienna (1815) and "
          "defended by the Austrian chancellor Metternich, the growth of the middle classes, and the spread of liberal and "
          "nationalist ideas among students and intellectuals."),
        T("Short-term causes were economic. Poor harvests and the potato blight of 1845–1847 caused food shortages and "
          "high prices. A commercial and industrial slump followed, bringing unemployment in the towns. Hungry workers "
          "and frustrated liberals came together on the streets."),
        H("France"),
        T("In February 1848 protests in Paris forced King Louis-Philippe to abdicate. The Second Republic was declared, "
          "with universal male suffrage. National Workshops were created to give work to the unemployed."),
        T("Conflict grew between moderate republicans and workers. When the National Workshops were closed, Paris workers "
          "rose in the June Days and were crushed by the army. In December 1848 Louis-Napoleon Bonaparte was elected president; "
          "in 1851 he seized power and in 1852 became Emperor Napoleon III."),
        H("The German states and the Austrian Empire"),
        T("In March 1848 Metternich fled Vienna and the Prussian king Frederick William IV made concessions in Berlin. "
          "A German National Assembly, the Frankfurt Parliament, met from May 1848 to draft a constitution for a united Germany."),
        T("The Parliament argued over whether Germany should include Austria (greater Germany) or exclude it (lesser Germany). "
          "In April 1849 it offered the crown of a united Germany to Frederick William IV, who refused it. The Parliament collapsed."),
        T("In the Austrian Empire the Habsburgs recovered by playing nationalities against each other. Prague was bombarded "
          "in June 1848, Vienna was retaken in October, and the Hungarian revolution led by Kossuth was crushed in 1849 "
          "with the help of Russian troops."),
        KEY("Why the revolutions failed", "Historians combine several explanations.", cards=[
            ["Divided revolutionaries", "Liberals feared the radicalism of workers more than they disliked kings; nationalities clashed with each other."],
            ["Survival of old power", "Monarchs kept control of their armies, which stayed loyal and were used to crush revolt."],
            ["Economic recovery", "Better harvests from 1848 reduced the hunger that had driven protest."],
            ["Foreign help", "Russia intervened in Hungary; France crushed the Roman Republic in 1849."],
        ]),
        T("Historiography: Lewis Namier described 1848 as a 'revolution of the intellectuals', stressing the weakness and "
          "idealism of middle-class leaders. A.J.P. Taylor called 1848 a turning point at which German history 'failed to turn', "
          "meaning Germany missed the chance of a liberal path. Other historians stress that the revolutions left lasting "
          "changes, such as the end of serfdom in the Austrian Empire and universal male suffrage in France."),
        EX("Essay plan 1", intro="'The revolutions of 1848 failed mainly because the revolutionaries were divided.' How far do you agree?", steps=[
            S("Introduction", text="Define the revolutions and their aims. Judgement: division was the most important internal cause, but failure was completed by loyal armies."),
            S("Division of classes", text="France: the June Days split middle-class republicans from workers. Germany: Frankfurt liberals feared radicals."),
            S("Division of nations", text="Austrian Empire: Czechs, Hungarians, Croats and Germans had conflicting aims; the Habsburgs exploited this."),
            S("Counter-argument: armies and foreign help", text="Monarchs kept their armies; Russian troops crushed Hungary; Frederick William IV refused the crown."),
            S("Counter-argument: economic recovery", text="Improved harvests reduced popular anger and support."),
            S("Judgement", text="Division allowed the old rulers to recover; their armies then delivered the final blow. Both factors were linked."),
        ]),
        EX("Essay plan 2", intro="Assess the importance of economic factors in causing the revolutions of 1848.", steps=[
            S("Introduction", text="Distinguish long-term and short-term causes. Judgement: economic crisis was the trigger, ideas gave the revolutions their aims."),
            S("Economic crisis", text="Harvest failures and potato blight 1845–1847, high food prices, industrial slump and unemployment."),
            S("Political and ideological causes", text="Opposition to Metternich's system, liberal demands for constitutions, nationalism in Germany, Italy and Hungary."),
            S("Social change", text="Growth of the middle class and of towns created the people who led and joined the revolts."),
            S("Judgement", text="Economic distress explains the timing and the crowds; liberalism and nationalism explain what the revolutionaries wanted."),
        ]),
        MISTAKE("Treating 1848 as one revolution", "Each country had different causes and outcomes. Compare at least France, Germany and Austria."),
        MISTAKE("Saying 1848 achieved nothing", "Serfdom was ended in the Austrian Empire and French men kept universal suffrage. Balance failure against lasting change."),
        QUIZ("Why did the Frankfurt Parliament fail to create a united Germany in 1849?",
             ["Napoleon III invaded Germany", "Frederick William IV refused the crown it offered him", "Bismarck dissolved it", "The Communist Manifesto turned workers against it"], 1,
             "Without the Prussian king's acceptance and army, the Parliament had no power to enforce its constitution.",
             feedback=["Napoleon III was not yet emperor and did not invade.", "", "Bismarck only came to power in 1862.", "The Manifesto had little immediate influence."]),
        PQ("Explain two reasons why revolution broke out in France in February 1848.",
           "Outline: (1) Economic distress: poor harvests, high prices and unemployment after 1846. (2) Political frustration: a very narrow electorate under Louis-Philippe and the banning of reform banquets. Link each to the February protests in Paris."),
        PQ("Compare the outcomes of the 1848 revolutions in France and in the Austrian Empire.",
           "Outline: France: monarchy ended, Second Republic, but conservatives won and Louis-Napoleon later became emperor. Austria: Metternich fell and serfdom ended, but the Habsburgs restored control by force with Russian help. Both ended in authoritarian rule, but France kept universal male suffrage."),
        PQ("'The revolutions of 1848 were a revolution of the intellectuals.' Discuss this view.",
           "Outline: Supporting: middle-class lawyers, professors and students led Frankfurt and other assemblies; idealism and lack of force (Namier's view). Against: workers and peasants filled the streets; economic hunger drove the crowds; nationalism had wide appeal. Judgement: intellectuals led, but popular distress gave the revolutions their force."),
        SUM("1848 saw revolutions across Europe, caused by economic crisis together with liberal and nationalist ideas.",
            "In France the monarchy fell, the June Days split the revolution and Louis-Napoleon rose to power.",
            "The Frankfurt Parliament failed when Frederick William IV refused the crown in 1849.",
            "The Habsburgs recovered by dividing nationalities and with Russian help in Hungary.",
            "Failure came from divided revolutionaries, loyal armies and economic recovery; some changes lasted."),
    ],
))

# ---------------------------------------------------------------------------
# European Revolutions & Unifications / Italian and German unification
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="European Revolutions & Unifications",
    topic="Italian and German unification",
    title="Cavour, Bismarck and the unification of Italy and Germany",
    slug="italian-and-german-unification",
    minutes=30,
    summary="How Italy (1859–1870) and Germany (1864–1871) were unified, the roles of Cavour, Garibaldi and Bismarck, Realpolitik, and the effects on the European balance of power.",
    objectives=[
        "Outline the main stages of Italian and German unification",
        "Explain Realpolitik and assess the roles of Cavour and Bismarck",
        "Evaluate the debate on whether Bismarck followed a master plan",
        "Explain the effects of unification on the balance of power",
    ],
    key_concepts=["Realpolitik", "Risorgimento", "Zollverein", "Balance of power", "North German Confederation"],
    blocks=[
        H("Introduction"),
        T("In 1848 nationalists failed to unite Italy or Germany. Twenty years later both countries were united, "
          "not by revolutions from below but by war and diplomacy led by the states of Piedmont-Sardinia and Prussia.\n\n"
          "This lesson asks: who or what was responsible, and how did unification change Europe?"),
        D("Politics based on practical calculation of power and interest rather than on ideals or principles. "
          "The term is closely associated with Bismarck and Cavour.", title="Realpolitik"),
        D("The German customs union, set up under Prussian leadership in 1834. It excluded Austria and tied the economies "
          "of many German states to Prussia.", title="Zollverein"),
        H("Italy: Cavour and Garibaldi"),
        T("Count Camillo di Cavour became prime minister of Piedmont-Sardinia in 1852. He modernised its economy and army "
          "and sent troops to the Crimean War to gain a seat at the peace conference and the goodwill of Britain and France."),
        T("At Plombières in 1858 Cavour secretly agreed with Napoleon III that France would help Piedmont against Austria. "
          "In the war of 1859, French and Piedmontese forces won at Magenta and Solferino. Napoleon III then made a separate "
          "peace at Villafranca, and Piedmont gained Lombardy but not Venetia."),
        T("In 1860 the central Italian states voted to join Piedmont. Giuseppe Garibaldi and his Thousand conquered Sicily "
          "and Naples. Cavour sent the Piedmontese army through the Papal States to control the south, and Garibaldi handed "
          "his conquests to King Victor Emmanuel II. The Kingdom of Italy was proclaimed in March 1861. Cavour died in June 1861."),
        T("Italy gained Venetia in 1866 by allying with Prussia against Austria, and Rome in 1870 when French troops "
          "withdrew during the Franco-Prussian War."),
        H("Germany: Bismarck and three wars"),
        T("Otto von Bismarck became minister-president of Prussia in 1862 during a conflict over army reform. He declared "
          "that the great questions of the day would be decided by 'iron and blood', not by speeches and majority votes."),
        T("Prussia and Austria defeated Denmark in 1864 over Schleswig and Holstein. In 1866 Prussia defeated Austria at "
          "Königgrätz (Sadowa) in a short war. Austria was excluded from German affairs, and the North German Confederation "
          "was formed in 1867 under Prussia."),
        T("In 1870 a dispute over a Hohenzollern candidate for the Spanish throne, and Bismarck's edited Ems telegram, led "
          "France to declare war. The southern German states joined Prussia. France was defeated at Sedan, and the German "
          "Empire was proclaimed at Versailles on 18 January 1871. Germany took Alsace and Lorraine."),
        KEY("Did Bismarck have a master plan?", "One of the classic debates of the topic.", cards=[
            ["Master planner", "Older German nationalist historians, and Bismarck's own memoirs, presented unification as a carefully planned sequence of three wars."],
            ["Opportunist", "A.J.P. Taylor and many later historians argue Bismarck reacted to events and exploited opportunities, keeping several options open."],
            ["Structural forces", "Economic historians stress Prussian industry and the Zollverein; J.M. Keynes argued the Empire was built more on coal and iron than on blood and iron."],
        ], note="A similar debate exists for Italy: Denis Mack Smith presented Cavour as an opportunist who did not originally aim at full unification."),
        H("Effects on the balance of power"),
        T("A united Germany became the strongest power in continental Europe, with a large army and fast-growing industry. "
          "France was humiliated and wanted Alsace-Lorraine back. Austria turned towards the Balkans, where it competed with Russia."),
        T("Italy became a new but weaker great power. The 1815 balance of power was replaced by a system dominated by Germany. "
          "Bismarck then tried to keep France isolated through alliances, a policy that helps explain the alliance system before 1914."),
        EX("Essay plan 1", intro="'Bismarck was the architect of German unification.' How far do you agree?", steps=[
            S("Introduction", text="Define the period 1862–1871. Judgement: Bismarck's diplomacy was decisive, but it rested on Prussian economic and military strength."),
            S("Bismarck's diplomacy", text="Isolation of Austria in 1866 and France in 1870; the Ems telegram; quick, limited wars."),
            S("Economic strength", text="Zollverein, coal, iron and railways gave Prussia the means to win (Keynes, economic historians)."),
            S("Military reform and international context", text="Roon and Moltke's army; Russian goodwill and French miscalculation; Austrian weakness after 1859."),
            S("Historiography", text="Master-plan view versus Taylor's opportunist Bismarck."),
            S("Judgement", text="Bismarck was the skilful builder, but Prussian power supplied the materials; he exploited rather than created the opportunities."),
        ]),
        EX("Essay plan 2", intro="Compare the contributions of Cavour and Garibaldi to Italian unification.", steps=[
            S("Introduction", text="Judgement: Cavour's diplomacy made unification possible; Garibaldi's campaign made it larger and faster than Cavour planned."),
            S("Cavour", text="Crimean War, Plombières, French alliance and the war of 1859; annexation of the central states."),
            S("Garibaldi", text="The Thousand in 1860; conquest of Sicily and Naples; popular nationalism."),
            S("Interaction", text="Cavour feared Garibaldi's radicalism and sent the army south; Garibaldi accepted Victor Emmanuel."),
            S("Other factors", text="French help, Austrian defeat, Prussian wars of 1866 and 1870."),
            S("Judgement", text="Neither could have succeeded alone; foreign help was essential to both."),
        ]),
        MISTAKE("Saying Italy was complete in 1861", "Venetia joined in 1866 and Rome in 1870. Keep the stages clear."),
        MISTAKE("Presenting Bismarck's memoirs as fact", "His later account exaggerates planning. Use the historiographical debate."),
        QUIZ("Which event ended Austrian influence in German affairs?",
             ["The Danish war of 1864", "The battle of Königgrätz in 1866", "The battle of Sedan in 1870", "The Zollverein of 1834"], 1,
             "Prussia's victory at Königgrätz led to Austria's exclusion and the North German Confederation.",
             feedback=["In 1864 Austria fought alongside Prussia.", "", "Sedan was a defeat of France, not Austria.", "The Zollverein excluded Austria economically but not politically."]),
        QUIZ("What did Napoleon III promise Cavour at Plombières in 1858?",
             ["Rome", "Military help against Austria", "Venetia immediately", "Recognition of Garibaldi"], 1,
             "France agreed to help Piedmont in a war against Austria, in return for Nice and Savoy.",
             feedback=["France protected the Pope in Rome.", "", "Venetia stayed Austrian until 1866.", "Garibaldi's expedition came later, in 1860."]),
        PQ("Explain two reasons why Prussia defeated Austria in 1866.",
           "Outline: (1) Military superiority: army reforms, the needle gun and efficient use of railways under Moltke. (2) Diplomacy: Bismarck secured French neutrality and an alliance with Italy, so Austria fought on two fronts."),
        PQ("How far was Italian unification achieved by foreign help?",
           "Outline: Foreign help: French armies in 1859; Venetia via Prussia in 1866; Rome after French withdrawal in 1870. Italian factors: Cavour's diplomacy, Garibaldi's campaign, plebiscites. Judgement: foreign help was essential at every stage, but Italians used it skilfully."),
        PQ("Assess the effects of German unification on the European balance of power to 1890.",
           "Outline: Germany became the dominant continental power; France hostile over Alsace-Lorraine; Austria turned to the Balkans; Bismarck's alliances (Dual Alliance 1879, Three Emperors' League) kept France isolated. Judgement: stability under Bismarck, but new rivalries were created."),
        SUM("Realpolitik means politics based on power and interest; Cavour and Bismarck both practised it.",
            "Italy was unified through the war of 1859, Garibaldi's campaign of 1860, and gains in 1866 and 1870.",
            "Germany was unified through wars against Denmark (1864), Austria (1866) and France (1870–1871).",
            "Historians debate whether Bismarck planned unification or exploited opportunities.",
            "Unification made Germany the dominant continental power and left France hostile."),
    ],
))

# ---------------------------------------------------------------------------
# Imperialism & the First World War / The Scramble for Africa
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Imperialism & the First World War",
    topic="The Scramble for Africa",
    title="The Scramble for Africa: four schools of interpretation",
    slug="scramble-for-africa-interpretations",
    minutes=30,
    summary="The partition of Africa from about 1880 to 1914 and the Eurocentric, Afrocentric, peripheral and Marxist (economic) interpretations of why it happened.",
    objectives=[
        "Outline the main events of the Scramble, including the Berlin Conference",
        "Explain the Eurocentric, Afrocentric, peripheral and Marxist interpretations",
        "Name the main historians linked to each school",
        "Evaluate the interpretations in a balanced essay",
    ],
    key_concepts=["Scramble for Africa", "Berlin Conference", "Effective occupation", "Peripheral theory", "Economic imperialism", "African agency"],
    blocks=[
        H("Introduction"),
        T("Around 1880 European powers controlled only small parts of Africa, mostly on the coasts. By 1914 almost the "
          "whole continent was under European rule; only Ethiopia and Liberia stayed independent. Cameroon became German in 1884, "
          "in the middle of this process.\n\nThere is no single accepted explanation. At A Level you must know the main schools "
          "and judge between them."),
        D("The rapid partition and conquest of Africa by European powers, roughly between 1880 and 1914.", title="Scramble for Africa"),
        D("A meeting in Berlin (November 1884 to February 1885), chaired by Bismarck, that set rules for claiming African coasts "
          "and recognised Leopold II's Congo Free State. No Africans were present.", title="Berlin Conference"),
        D("The principle in the Berlin Act that a power claiming African coastline must notify others and establish authority "
          "there. It encouraged powers to occupy territory quickly.", title="Effective occupation"),
        H("Key events"),
        T("Important moments include the British occupation of Egypt in 1882, German protectorates in 1884 (including Kamerun "
          "and Togo), the Berlin Conference, Italy's defeat by Ethiopia at Adwa in 1896, the Fashoda crisis between Britain "
          "and France in 1898, and the South African War of 1899–1902."),
        H("The economic and Marxist interpretation"),
        T("J.A. Hobson, in Imperialism: A Study (1902), argued that surplus capital and the interests of financiers drove "
          "imperial expansion, against the interests of the nation as a whole. Lenin, in Imperialism, the Highest Stage of "
          "Capitalism (written in 1916), argued that imperialism was a necessary stage of monopoly capitalism, as capitalists "
          "competed for markets, raw materials and places to invest."),
        T("Critics such as D.K. Fieldhouse pointed out that relatively little European investment went to tropical Africa, "
          "and that much of the Scramble came before the period Lenin described. Supporters reply that hopes of future profit, "
          "not actual investment, mattered."),
        H("The Eurocentric (political and strategic) interpretation"),
        T("This school stresses events in Europe: national prestige, rivalry between great powers, domestic politics and "
          "the diplomacy of Bismarck after 1871. For example, Bismarck's colonial moves in 1884 have been linked to German "
          "domestic politics and to relations with Britain and France."),
        H("The peripheral interpretation"),
        T("Ronald Robinson and John Gallagher, in Africa and the Victorians (1961), argued that the causes lay in crises on "
          "the periphery, in Africa itself. They saw Britain's occupation of Egypt in 1882, to protect the route to India via "
          "the Suez Canal, as the trigger that set off the Scramble. Europeans were drawn in by local crises and the collapse "
          "of collaboration with African rulers."),
        H("The Afrocentric interpretation"),
        T("African historians such as J.F. Ade Ajayi and the authors of the UNESCO General History of Africa stressed African "
          "agency: African rulers negotiated, collaborated, traded and resisted, and their choices shaped how and when partition "
          "happened. A.G. Hopkins linked the Scramble in West Africa to a crisis in the trade relationship between Africans and "
          "Europeans after the end of the slave trade."),
        KEY("The four schools at a glance", "Each answers the question 'where did the Scramble start?' differently.", cards=[
            ["Economic / Marxist", "In European capitalism: Hobson, Lenin."],
            ["Eurocentric", "In European politics and diplomacy: prestige, rivalry, Bismarck."],
            ["Peripheral", "In crises in Africa that drew Europeans in: Robinson and Gallagher."],
            ["Afrocentric", "In African societies, their choices and their resistance: Ajayi, UNESCO history."],
        ], note="Most modern historians combine several explanations."),
        EX("Essay plan 1", intro="'The Scramble for Africa was caused mainly by economic factors.' How far do you agree?", steps=[
            S("Introduction", text="Define the Scramble and the economic thesis. Judgement: economic motives mattered, but political and peripheral factors explain the timing better."),
            S("Economic case", text="Hobson and Lenin; trade interests of firms such as Woermann in Kamerun; search for raw materials and markets."),
            S("Critique of the economic case", text="Fieldhouse: little capital went to tropical Africa; much of the partition came before monopoly capitalism."),
            S("Political and peripheral factors", text="Prestige and great-power rivalry; Robinson and Gallagher on Egypt 1882 as the trigger."),
            S("African agency", text="African rulers' treaties and resistance, such as the Duala in 1884 and Ethiopia at Adwa, shaped the process."),
            S("Judgement", text="Economic interest was a constant background, but political rivalry and local crises explain why partition happened so fast after 1880."),
        ]),
        EX("Essay plan 2", intro="Assess the strengths and weaknesses of the peripheral interpretation of the Scramble for Africa.", steps=[
            S("Introduction", text="State the theory of Robinson and Gallagher. Judgement: it explains British actions well but is less convincing for Germany and France."),
            S("Strengths", text="Explains Egypt 1882 and British concern for the route to India; takes events in Africa seriously."),
            S("Weaknesses: Eurocentric critique", text="German protectorates in 1884 are better explained by Bismarck's European calculations."),
            S("Weaknesses: economic and Afrocentric critiques", text="Underplays business interests and gives Africans a reactive role rather than real agency."),
            S("Judgement", text="A valuable corrective to purely economic theories, but best combined with other explanations."),
        ]),
        MISTAKE("Saying the Berlin Conference divided Africa", "It set rules for claiming territory and recognised the Congo Free State; most borders were fixed later by bilateral agreements."),
        MISTAKE("Naming historians you are unsure of", "Attribute arguments only where you are certain. A clear explanation of a school earns more than a wrong name."),
        QUIZ("Which historians developed the peripheral (excentric) interpretation of the Scramble?",
             ["Hobson and Lenin", "Robinson and Gallagher", "Fischer and Ritter", "Taylor and Namier"], 1,
             "Robinson and Gallagher's Africa and the Victorians (1961) stressed crises on the African periphery, especially Egypt.",
             feedback=["They put forward economic explanations.", "", "They debated the causes of the First World War.", "They are known for other debates, such as appeasement and 1848."]),
        PQ("Explain two decisions taken at the Berlin Conference of 1884–1885.",
           "Outline: (1) Effective occupation: claims to coastal territory had to be notified and backed by real authority. (2) Recognition of Leopold II's Congo Free State, with free trade and navigation on the Congo and Niger rivers. Note that no Africans attended."),
        PQ("Compare the economic interpretations of Hobson and Lenin.",
           "Outline: Similarity: both linked imperialism to surplus capital and capitalist interests. Difference: Hobson, a liberal, saw imperialism as a distortion that reform could cure; Lenin, a Marxist, saw it as an inevitable highest stage of capitalism leading to war."),
        PQ("'Africans were not passive victims of the Scramble.' Discuss.",
           "Outline: For: treaties negotiated by African rulers (Duala 1884), collaboration and resistance, victory at Adwa 1896, Samori Touré's long resistance. Against: European military technology and the Berlin rules meant Africans had limited power to stop partition. Judgement: Africans shaped the timing and form of partition but not its overall outcome."),
        SUM("Between about 1880 and 1914 Europe partitioned almost all of Africa; Ethiopia and Liberia stayed independent.",
            "The Berlin Conference (1884–1885) set rules such as effective occupation; no Africans attended.",
            "Economic theory: Hobson (1902) and Lenin (1916); criticised by Fieldhouse and others.",
            "Peripheral theory: Robinson and Gallagher, with Egypt in 1882 as the trigger.",
            "Eurocentric and Afrocentric views stress European politics and African agency; good essays combine and judge."),
    ],
))

# ---------------------------------------------------------------------------
# Imperialism & the First World War / The First World War
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="Imperialism & the First World War",
    topic="The First World War",
    title="The First World War: causes, peace settlement and mandates",
    slug="first-world-war-causes-and-peace",
    minutes=30,
    summary="The long-term and short-term causes of the First World War, the debate on responsibility including the Fischer thesis, the Paris peace settlement and the mandate system that placed Cameroon under Britain and France.",
    objectives=[
        "Explain the long-term causes: alliances, militarism, imperial rivalry and nationalism",
        "Describe the July Crisis of 1914",
        "Evaluate the Fischer thesis and other interpretations of responsibility",
        "Explain the Paris peace settlement and the mandate system, including its effect on Cameroon",
    ],
    key_concepts=["Alliance system", "July Crisis", "Fischer thesis", "Treaty of Versailles", "War guilt clause", "Mandate system"],
    blocks=[
        H("Introduction"),
        T("The First World War (1914–1918) changed Cameroon directly. German Kamerun was invaded by British, French and "
          "Belgian forces, and after the war it was divided and placed under the League of Nations mandate system.\n\n"
          "This lesson covers why the war started, who was responsible, and how the peace was made."),
        H("Long-term causes"),
        T("Europe was divided into two blocs. The Triple Alliance (1882) linked Germany, Austria-Hungary and Italy. "
          "France and Russia allied in 1894. Britain settled colonial disputes with France in the Entente Cordiale (1904) "
          "and with Russia in 1907, forming the Triple Entente."),
        T("Other pressures included the Anglo-German naval race after 1898, large conscript armies and rigid war plans "
          "such as Germany's Schlieffen Plan, imperial rivalry, and nationalism in the Balkans, where Serbia challenged "
          "Austria-Hungary."),
        T("A series of crises raised tension: the Moroccan crises of 1905–1906 and 1911, the Bosnian crisis of 1908–1909, "
          "and the Balkan Wars of 1912–1913."),
        H("The July Crisis, 1914"),
        T("On 28 June 1914 Archduke Franz Ferdinand, heir to the Austro-Hungarian throne, was assassinated in Sarajevo by "
          "Gavrilo Princip, a Bosnian Serb. Germany promised Austria-Hungary its full support (the so-called blank cheque)."),
        T("Austria-Hungary sent Serbia an ultimatum on 23 July and declared war on 28 July. Russia mobilised. Germany declared "
          "war on Russia on 1 August and on France on 3 August, and invaded Belgium. Britain declared war on Germany on 4 August."),
        D("Article 231 of the Treaty of Versailles, in which Germany accepted responsibility for causing the loss and damage of "
          "the war. It became the legal basis for reparations.", title="War guilt clause"),
        KEY("Who was responsible?", "The debate on responsibility has changed over time.", cards=[
            ["Versailles verdict", "Article 231 placed responsibility on Germany and its allies."],
            ["Shared responsibility (1920s–1950s)", "Many historians argued that all powers slid into war together, trapped by alliances and military plans."],
            ["Fischer thesis (1961)", "Fritz Fischer, in Griff nach der Weltmacht, argued that Germany's leaders deliberately sought European and world power and bore the main responsibility."],
            ["Recent views", "Christopher Clark (The Sleepwalkers, 2012) spread responsibility across several governments; others still stress German and Austrian decisions in July 1914."],
        ], note="The Fischer controversy was intense in West Germany in the 1960s. A.J.P. Taylor stressed mobilisation timetables."),
        H("The Kamerun campaign"),
        T("British, French and Belgian forces invaded Kamerun in 1914. Douala fell in September 1914. The last German forces "
          "withdrew into Spanish Guinea (Río Muni) early in 1916, and the northern fort at Mora surrendered in February 1916."),
        H("The Paris peace settlement"),
        T("The Paris Peace Conference opened in January 1919, dominated by Wilson (United States), Lloyd George (Britain) and "
          "Clemenceau (France). Wilson's Fourteen Points (January 1918) had called for self-determination and a League of Nations."),
        T("The Treaty of Versailles was signed on 28 June 1919. Germany lost Alsace-Lorraine and other territory, its army was "
          "limited to 100,000 men, the Rhineland was demilitarised, Germany accepted Article 231, and it lost all its colonies. "
          "Reparations were fixed in 1921 at 132 billion gold marks. Other treaties dealt with Austria, Hungary, Bulgaria and Turkey."),
        D("Article 22 of the League Covenant placed former German colonies and Ottoman territories under 'advanced nations' as "
          "mandates, supervised by the Permanent Mandates Commission. Class A were Middle Eastern territories, class B were "
          "most of German Central Africa, including Cameroon and Togo, and class C included South West Africa and Pacific islands.",
          title="The mandate system"),
        T("Cameroon became a class B mandate, divided between France (the larger share) and Britain, confirmed by the League "
          "in 1922. Critics argue the system was annexation in disguise; defenders note it created the international "
          "supervision and petition rights that later helped Cameroonian nationalists after 1945."),
        EX("Essay plan 1", intro="'Germany was mainly responsible for the outbreak of the First World War.' How far do you agree?", steps=[
            S("Introduction", text="Outline the debate. Judgement: Germany bears a large share, but Austria-Hungary and Russia also made decisive choices."),
            S("Case for German responsibility", text="Fischer thesis; the blank cheque; Schlieffen Plan forcing war on France and invasion of Belgium; Weltpolitik and naval race."),
            S("Austria-Hungary and Serbia", text="Austria's harsh ultimatum and decision for war; Serbian nationalist networks behind the assassination."),
            S("Russia, France and Britain", text="Russian general mobilisation; French support for Russia; Britain's ambiguous commitments (Clark's argument)."),
            S("Structural causes", text="Alliances and mobilisation timetables (Taylor) narrowed choices."),
            S("Judgement", text="Germany's decisions made a local war general; structural factors explain why the crisis was so dangerous."),
        ]),
        EX("Essay plan 2", intro="Assess the view that the mandate system was simply colonialism under another name, with reference to Cameroon.", steps=[
            S("Introduction", text="Define Article 22 and the B mandates. Judgement: in practice largely colonial, but its legal framework mattered later."),
            S("Colonial reality", text="Britain ruled its share as part of Nigeria; France used the indigénat and forced labour; borders followed the 1916–1919 partition."),
            S("International supervision", text="Annual reports to the Permanent Mandates Commission; petitions from Duala leaders."),
            S("Long-term significance", text="Mandate status became UN trusteeship in 1946, giving Cameroon a path to independence and reunification debates."),
            S("Judgement", text="Colonialism in daily life, but not in law; the difference proved important after 1945."),
        ]),
        MISTAKE("Treating the alliance system as automatic", "Alliances did not force everyone into war: Italy stayed neutral in 1914, and Britain's entente was not a binding alliance."),
        MISTAKE("Overstating the reparations figure's impact without evidence", "Give the 1921 figure accurately and note that historians still debate how burdensome reparations really were."),
        QUIZ("What was the argument of the Fischer thesis?",
             ["All powers slid into war by accident", "Germany's leaders deliberately pursued aims that led to war", "Britain caused the war through naval rivalry", "Serbia alone was responsible"], 1,
             "Fischer argued that German leaders aimed at European and world power and accepted, even sought, war in 1914.",
             feedback=["This is the shared-responsibility view he challenged.", "", "Fischer focused on German, not British, policy.", "Fischer did not blame Serbia."]),
        QUIZ("What type of League mandate was Cameroon?",
             ["Class A", "Class B", "Class C", "It was not a mandate"], 1,
             "Cameroon and Togo were class B mandates, divided between Britain and France.",
             feedback=["Class A applied to former Ottoman territories such as Syria and Iraq.", "", "Class C included South West Africa and Pacific islands.", "Cameroon was confirmed as a mandate in 1922."]),
        PQ("Explain two long-term causes of the First World War.",
           "Outline: (1) The alliance system: two armed blocs meant a local conflict could become general. (2) Militarism and the naval race: arms competition and rigid war plans such as the Schlieffen Plan increased fear and reduced time for diplomacy."),
        PQ("How far was the Treaty of Versailles a harsh peace?",
           "Outline: Harsh: territorial losses, loss of colonies, military limits, Article 231 and reparations; Keynes criticised it. Not so harsh: Germany remained united with its industry largely intact; Margaret MacMillan and others argue it was a compromise. Judgement: harsh enough to anger Germans, not harsh enough to stop German recovery."),
        PQ("Assess the importance of the First World War in shaping Cameroon's history.",
           "Outline: Conquest 1914–1916 ended German rule; partition into British and French zones; mandate status from 1922 led to trusteeship and later reunification debates. Judgement: the war created the two Cameroons whose relationship dominated politics until 1961 and after."),
        SUM("Long-term causes: alliances, militarism, imperial rivalry, Balkan nationalism and a series of crises.",
            "The July Crisis followed the Sarajevo assassination of 28 June 1914; Britain entered on 4 August.",
            "Interpretations range from Versailles war guilt to shared responsibility, the Fischer thesis and Clark's Sleepwalkers.",
            "Versailles (28 June 1919) took Germany's colonies; reparations were fixed at 132 billion gold marks in 1921.",
            "Cameroon became a class B League mandate divided between France and Britain, confirmed in 1922."),
    ],
))

# ---------------------------------------------------------------------------
# The Interwar Crises / Fascism and Nazism
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="The Interwar Crises",
    topic="Fascism and Nazism",
    title="The rise of Italian Fascism and Nazism and the fall of Weimar",
    slug="rise-of-fascism-and-nazism",
    minutes=30,
    summary="Why Mussolini came to power in Italy in 1922, why the Weimar Republic collapsed, and how Hitler became chancellor in 1933 and built a dictatorship.",
    objectives=[
        "Explain the rise of Mussolini and the Fascists to 1926",
        "Analyse the weaknesses and collapse of the Weimar Republic",
        "Explain how Hitler came to power and consolidated it in 1933–1934",
        "Compare the rise of Fascism and Nazism and evaluate the role of elites",
    ],
    key_concepts=["Fascism", "Nazism", "Weimar Republic", "Article 48", "Enabling Act", "Mutilated victory"],
    blocks=[
        H("Introduction"),
        T("Between the wars, democracy collapsed in much of Europe. In Italy and Germany, new mass movements led by Mussolini "
          "and Hitler took power and created dictatorships. Their policies led to the crises of the 1930s and to the Second World War.\n\n"
          "A key A Level question is whether these men seized power or were handed it."),
        D("A nationalist, anti-democratic and anti-communist ideology that glorified the state, violence and a single leader. "
          "It began with Mussolini's movement in Italy in 1919.", title="Fascism"),
        D("The ideology of Hitler's National Socialist German Workers' Party (NSDAP): extreme nationalism, racism and "
          "antisemitism, the leader principle, and expansion in the east.", title="Nazism"),
        H("Italy: the rise of Mussolini"),
        T("Italy was on the winning side in 1918 but did not gain all the territory it had been promised. Nationalists called "
          "this a 'mutilated victory'. Inflation, unemployment and the strikes and land occupations of 1919–1920 (the 'two red years') "
          "frightened landowners, industrialists and the middle classes."),
        T("Mussolini founded the Fasci di Combattimento in 1919. Fascist squads attacked socialists and trade unions, often with "
          "the tolerance of the police. In October 1922, during the March on Rome, King Victor Emmanuel III refused to declare "
          "martial law and appointed Mussolini prime minister."),
        T("Mussolini consolidated power through the Acerbo Law (1923), which gave a large bonus of seats to the leading party, "
          "and survived the crisis caused by the murder of the socialist deputy Giacomo Matteotti in 1924. By 1925–1926 Italy was a dictatorship."),
        H("Germany: the weaknesses of Weimar"),
        T("The Weimar Republic was born in defeat in 1918–1919. Many Germans associated it with the Treaty of Versailles. "
          "Proportional representation produced unstable coalitions, and Article 48 of the constitution allowed the president "
          "to rule by emergency decree."),
        T("The early years saw the Spartacist rising (1919), the Kapp Putsch (1920), the French occupation of the Ruhr and "
          "hyperinflation (1923), and Hitler's failed Munich (Beer Hall) Putsch in November 1923. Under Stresemann the Republic "
          "recovered, helped by the Dawes Plan (1924)."),
        H("Depression and the Nazi breakthrough"),
        T("The Wall Street Crash of 1929 and the Depression caused mass unemployment in Germany, reaching around six million in "
          "early 1932. From 1930 chancellors ruled by presidential decree under Article 48. The Nazi vote rose from 18 percent in "
          "September 1930 to about 37 percent in July 1932, making them the largest party; it fell to about 33 percent in November 1932."),
        T("Conservative politicians around President Hindenburg, including Franz von Papen, believed they could control Hitler. "
          "Hitler was appointed chancellor on 30 January 1933 at the head of a coalition."),
        T("He then built a dictatorship: the Reichstag fire (February 1933) was used to suspend civil rights, the Enabling Act "
          "(March 1933) let the government make laws without the Reichstag, other parties were banned, the SA leadership was "
          "killed in the Night of the Long Knives (June 1934), and after Hindenburg's death in August 1934 Hitler became Führer."),
        KEY("Seized or handed power?", "Historians weigh long-term, short-term and personal factors.", cards=[
            ["Long-term weaknesses", "Some historians argue Germany followed a special path (Sonderweg) with weak democratic traditions; others reject this."],
            ["Economic crisis", "The Depression turned the Nazis from a fringe party into a mass movement."],
            ["Elite intrigue", "Ian Kershaw and others stress that Hitler was brought to power by conservative elites, not by a majority vote."],
            ["Appeal and propaganda", "Nazi propaganda, organisation and Hitler's leadership attracted voters from many social groups."],
        ], note="In Italy too, the king, landowners and industrialists helped Mussolini into office."),
        EX("Essay plan 1", intro="'The Great Depression was the main reason for the collapse of the Weimar Republic.' How far do you agree?", steps=[
            S("Introduction", text="Judgement: the Depression was the decisive trigger, but Weimar was already weakened and its end was decided by elites."),
            S("The Depression", text="Mass unemployment; collapse of the Grand Coalition in 1930; Nazi vote rising from 18 to 37 percent."),
            S("Long-term weaknesses", text="Association with Versailles; proportional representation; Article 48; hostility of the army, judges and civil service."),
            S("Elite decisions", text="Hindenburg, Papen and Schleicher governed by decree and appointed Hitler in January 1933."),
            S("Nazi appeal", text="Propaganda, organisation, use of SA violence; broad social support."),
            S("Judgement", text="Without the Depression the Nazis would probably have stayed marginal; without elite intrigue Hitler might not have become chancellor."),
        ]),
        EX("Essay plan 2", intro="Compare the ways in which Mussolini and Hitler came to power.", steps=[
            S("Introduction", text="Judgement: both were legally appointed with elite help after using violence and exploiting crisis; Hitler had greater electoral support."),
            S("Similarities: crisis and fear of communism", text="Post-war unrest in Italy; Depression in Germany; both exploited fear of the left."),
            S("Similarities: elite help", text="Victor Emmanuel III in 1922; Hindenburg and Papen in 1933."),
            S("Differences: elections and speed", text="Fascists were a small parliamentary group in 1922; the Nazis were the largest party in 1932. Hitler consolidated power within 18 months, Mussolini over several years."),
            S("Judgement", text="Both were handed power by elites, but Hitler had a mass base and moved faster to dictatorship."),
        ]),
        MISTAKE("Saying Hitler was elected dictator", "He was appointed chancellor by Hindenburg; the Nazis never won a majority in a free election."),
        MISTAKE("Mixing up the dates of the putsches", "The Kapp Putsch was 1920, the Munich Putsch 1923, the March on Rome 1922."),
        QUIZ("Which law allowed Hitler's government to make laws without the Reichstag?",
             ["Article 48", "The Enabling Act", "The Acerbo Law", "The Dawes Plan"], 1,
             "The Enabling Act of March 1933 gave the government power to pass laws without the Reichstag.",
             feedback=["Article 48 gave emergency powers to the president, not the chancellor.", "", "The Acerbo Law was an Italian electoral law of 1923.", "The Dawes Plan (1924) rescheduled reparations."]),
        PQ("Explain two reasons why Mussolini was appointed prime minister in 1922.",
           "Outline: (1) Fear of socialism after the two red years made elites and the middle classes support the Fascists. (2) The king refused to use the army against the March on Rome and appointed Mussolini to avoid conflict."),
        PQ("How important was Article 48 in the collapse of the Weimar Republic?",
           "Outline: Important: from 1930 Brüning, Papen and Schleicher governed by decree, weakening parliament and getting Germans used to rule without the Reichstag. Other factors: Depression, Nazi appeal, elite intrigue. Judgement: a necessary tool, but used by people who chose not to defend democracy."),
        PQ("'Hitler came to power through backstairs intrigue rather than popular support.' Discuss.",
           "Outline: Intrigue: Papen and Hindenburg's deal in January 1933; Nazi vote fell in November 1932. Popular support: largest party in July 1932 with about 37 percent; mass membership and SA. Judgement: popular support made Hitler impossible to ignore, intrigue put him in office."),
        SUM("Post-war crisis and fear of socialism helped Mussolini, who was appointed prime minister in October 1922.",
            "Weimar was weakened by Versailles, unstable coalitions, Article 48 and early crises such as 1923.",
            "The Depression made the Nazis the largest party in July 1932.",
            "Conservative elites made Hitler chancellor on 30 January 1933; the Enabling Act and 1934 events created dictatorship.",
            "Both dictators exploited crisis and violence and were helped into power by elites."),
    ],
))

# ---------------------------------------------------------------------------
# The Interwar Crises / Appeasement
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module="The Interwar Crises",
    topic="Appeasement",
    title="Anglo-French appeasement, 1931–1939",
    slug="anglo-french-appeasement",
    minutes=28,
    summary="Why Britain and France followed a policy of appeasement towards the dictators in the 1930s, the key crises from Manchuria to Munich, and the historiographical debate from Guilty Men to the revisionists.",
    objectives=[
        "Define appeasement and outline the main crises of the 1930s",
        "Explain British and French motives for appeasement",
        "Evaluate the orthodox, revisionist and post-revisionist interpretations",
        "Reach a judgement on whether appeasement was a mistake",
    ],
    key_concepts=["Appeasement", "Munich Agreement", "Remilitarisation of the Rhineland", "Anschluss", "Nazi-Soviet Pact", "Revisionism"],
    blocks=[
        H("Introduction"),
        T("In the 1930s Britain and France repeatedly made concessions to Germany and Italy in the hope of avoiding another war. "
          "The policy is linked above all to the British prime minister Neville Chamberlain (1937–1940). It ended when Germany "
          "invaded Poland in September 1939.\n\nIt is one of the most debated policies of the twentieth century."),
        D("A policy of settling international disputes by making reasonable concessions to a dissatisfied power, in order to "
          "avoid war. Before 1939 the word was not necessarily negative.", title="Appeasement"),
        H("The crises of the 1930s"),
        T("Japan invaded Manchuria in 1931 and the League of Nations failed to act effectively. Germany left the League and the "
          "Disarmament Conference in 1933, and announced rearmament and conscription in 1935. The Anglo-German Naval Agreement (1935) "
          "accepted German naval expansion."),
        T("Italy invaded Abyssinia (Ethiopia) in 1935. The League imposed limited sanctions that did not include oil. The "
          "Hoare-Laval Pact, a British and French plan to give Italy much of Abyssinia, caused public outrage when it leaked in December 1935."),
        T("In March 1936 German troops reoccupied the demilitarised Rhineland, breaking Versailles and Locarno; Britain and France "
          "did not respond with force. In the Spanish Civil War (1936–1939) they followed non-intervention, while Germany and Italy helped Franco."),
        T("In March 1938 Germany annexed Austria (the Anschluss). Hitler then demanded the Sudetenland from Czechoslovakia. At Munich "
          "on 29–30 September 1938 Chamberlain, Daladier, Hitler and Mussolini agreed that Germany would take the Sudetenland. "
          "Czechoslovakia was not invited."),
        T("In March 1939 Germany occupied the rest of Czech territory. Britain and France guaranteed Poland on 31 March 1939. "
          "The Nazi-Soviet Pact was signed on 23 August 1939. Germany invaded Poland on 1 September, and Britain and France declared war on 3 September."),
        H("Why Britain and France appeased"),
        KEY("British motives", "Several pressures pointed the same way.", cards=[
            ["Public opinion and memory of 1914–1918", "Fear of another mass war and of bombing of cities."],
            ["Military and economic weakness", "Rearmament was slow and costly; military chiefs warned against fighting several enemies at once."],
            ["Empire and dominions", "Global commitments, threats from Japan and Italy; dominions reluctant to fight over Central Europe."],
            ["Views of Versailles", "Many British leaders thought some German grievances were fair."],
        ]),
        T("France had the larger army but relied on the defensive Maginot Line, was politically divided (for example under the "
          "Popular Front of 1936–1938), faced economic difficulties, and was unwilling to act without Britain. French appeasement "
          "therefore often followed British policy, even though France had treaty links with Czechoslovakia."),
        H("The historiographical debate"),
        KEY("Three schools", "Interpretations have changed with access to records and with politics.", cards=[
            ["Orthodox", "Guilty Men (1940), written under the pen-name Cato, and later Churchill's memoirs, condemned appeasers as weak and foolish."],
            ["Revisionist", "From the 1960s, when government records opened, historians stressed the real constraints on Chamberlain; John Charmley later defended him strongly."],
            ["Post-revisionist", "R.A.C. Parker (1993) argued Chamberlain did have alternatives, such as a closer alliance with France and the USSR, but chose not to pursue them."],
        ], note="A.J.P. Taylor's Origins of the Second World War (1961) controversially presented Hitler as an opportunist and argued the war arose from mistakes on all sides."),
        EX("Essay plan 1", intro="'Appeasement was a sensible policy in the circumstances of the 1930s.' How far do you agree?", steps=[
            S("Introduction", text="Define appeasement. Judgement: understandable until Munich, but a mistake once Hitler broke the Munich agreement in March 1939, if not earlier."),
            S("Sensible: constraints", text="Public opinion, military weakness, imperial commitments and dominion views (revisionist case)."),
            S("Sensible: buying time", text="Rearmament, especially of the air force, continued between 1938 and 1939."),
            S("Mistaken: missed chances", text="Rhineland 1936 and Czechoslovakia 1938 (strong defences, French treaty); failure to work with the USSR (Parker)."),
            S("Mistaken: misreading Hitler", text="Chamberlain treated Hitler as a normal statesman with limited aims."),
            S("Judgement", text="Rational in motive, flawed in execution; the post-revisionist view is the most convincing."),
        ]),
        EX("Essay plan 2", intro="Compare the reasons why Britain and France followed appeasement.", steps=[
            S("Introduction", text="Judgement: shared fear of war, but France was more dependent and Britain more confident in its own policy."),
            S("Shared reasons", text="Memory of the First World War, economic problems after the Depression, fear of air attack."),
            S("British reasons", text="Empire and dominions, sympathy for some German grievances, Chamberlain's personal diplomacy."),
            S("French reasons", text="Defensive military doctrine, political division, dependence on Britain despite alliances in Eastern Europe."),
            S("Judgement", text="Britain led and France followed; this shows France's weakness more than its agreement with British views."),
        ]),
        MISTAKE("Judging with hindsight only", "Explain what leaders knew at the time. Examiners reward explanation of constraints before criticism."),
        MISTAKE("Presenting Taylor as defending appeasement", "Taylor's book is mainly about Hitler as an opportunist; do not confuse it with revisionist defences of Chamberlain."),
        QUIZ("What was agreed at Munich in September 1938?",
             ["Germany would annex Austria", "Germany would take the Sudetenland", "Britain would guarantee Poland", "Germany and the USSR would not attack each other"], 1,
             "Britain, France, Germany and Italy agreed that Germany would take the Sudetenland, without Czechoslovak participation.",
             feedback=["The Anschluss happened in March 1938, without an agreement.", "", "The guarantee to Poland came on 31 March 1939.", "That was the Nazi-Soviet Pact of August 1939."]),
        QUIZ("Which historian is associated with the post-revisionist view that Chamberlain had alternatives?",
             ["R.A.C. Parker", "J.A. Hobson", "Fritz Fischer", "Lewis Namier"], 0,
             "Parker's Chamberlain and Appeasement (1993) argued Chamberlain chose appeasement when other options existed.",
             feedback=["", "Hobson wrote on imperialism in 1902.", "Fischer wrote on the causes of the First World War.", "Namier is best known here for his view of 1848."]),
        PQ("Explain two reasons why Britain did not oppose the remilitarisation of the Rhineland in 1936.",
           "Outline: (1) Many British people felt Germany was only moving into its own territory. (2) Britain was not ready militarily and was distracted by the Abyssinian crisis; France would not act alone."),
        PQ("How far was the Munich Agreement a triumph for Hitler?",
           "Outline: Triumph: gained the Sudetenland and its defences without war; Czechoslovakia weakened; Western powers shown to be unwilling to fight. Limits: Hitler had wanted a short war; Britain gained time to rearm; British opinion hardened after March 1939. Judgement: a major gain, but it helped turn Britain towards resistance."),
        PQ("'Guilty Men' or men with no choice? Assess interpretations of Chamberlain's policy.",
           "Outline: Orthodox (Cato 1940, Churchill): weak and blind. Revisionist: constrained by economy, military advice, empire and opinion. Post-revisionist (Parker): constraints real, but alternatives existed. Judgement: support a reasoned position using evidence of the options in 1938–1939."),
        SUM("Appeasement meant concessions to avoid war; it is linked above all to Chamberlain.",
            "Key crises: Manchuria, Abyssinia, Rhineland, Spain, Anschluss, Munich, Prague and Poland.",
            "Motives: memory of 1914–1918, military and economic weakness, empire and dominions, views of Versailles.",
            "France depended on Britain and on the defensive Maginot Line.",
            "Debate: orthodox Guilty Men, revisionists on constraints, post-revisionists such as Parker; Taylor on Hitler as opportunist."),
    ],
))
