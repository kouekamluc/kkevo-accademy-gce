"""Form 5 History (GCE O Level): World History since 1870 - African decolonization and the Cold War.

Draft content: every date, name and figure must be checked by a reviewer against the official
syllabus and standard textbooks before publishing.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

MODULE = "World History since 1870"
DECOL = "African decolonization"
COLD = "Cold War"

LESSONS = []

# ---------------------------------------------------------------------------
# 1. Why colonial rule ended
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MODULE, topic=DECOL,
    title="Why colonial rule in Africa came to an end",
    slug="why-colonial-rule-ended-in-africa",
    minutes=20,
    summary="The causes of African decolonization after 1945: the effects of the Second World War, the UN and the "
            "superpowers, Pan-Africanism and nationalism, and economic and political grievances.",
    objectives=[
        "Define decolonization and Pan-Africanism",
        "Explain how the Second World War weakened colonial rule",
        "Explain the roles of the UN, the superpowers and the Manchester Congress of 1945",
        "Group causes into external and internal, and into economic and political",
    ],
    key_concepts=["Decolonization", "Pan-Africanism", "Nationalism", "Self-determination", "Ex-servicemen", "Cash crops"],
    blocks=[
        H("Introduction"),
        T("In 1945 only a few African states were independent, such as Ethiopia, Liberia and Egypt. Thirty years later "
          "most of the continent was free.\n\nCameroon was part of this change. In 1960 alone, 17 African countries became "
          "independent, and French Cameroun was one of them."),
        T("This lesson asks one question: why did colonial rule end? The next lessons show how it ended, and what "
          "African states did after independence."),
        D("**Decolonization** is the process by which colonies gained independence from European colonial powers.",
          title="Decolonization"),
        D("**Nationalism** is the wish of a people to rule themselves in their own state. **Self-determination** is the "
          "right of a people to choose their own government.", title="Nationalism and self-determination"),
        H("Effects of the Second World War"),
        T("The Second World War (1939–1945) left Britain and France weak. They were short of money and busy rebuilding "
          "their own countries. Ruling large empires became harder and more expensive."),
        T("The war also damaged the idea that Europeans could not be defeated. Colonial subjects saw European armies "
          "beaten and European cities in ruins."),
        T("Many Africans served as soldiers or workers in the war. These **ex-servicemen** returned home with new ideas "
          "and new expectations. They had seen other countries and fought for freedom abroad. Many asked why they "
          "should not enjoy freedom at home."),
        H("The UN and the superpowers"),
        T("The Charter of the United Nations supported self-determination. This gave African nationalists a principle "
          "to quote in their demands. The UN also watched over trust territories, such as Cameroon."),
        T("The USA and the USSR became the two new superpowers after 1945. Both criticised old-style colonial empires. "
          "Britain and France could not ignore this pressure."),
        T("India became independent in 1947. This showed that a large colony could win freedom. African nationalists "
          "took courage from the example."),
        H("African action: Pan-Africanism and nationalism"),
        D("**Pan-Africanism** is the idea that all Africans and people of African descent share common interests and "
          "should unite. It inspired leaders such as Kwame Nkrumah.", title="Pan-Africanism"),
        T("A Pan-African Congress was held in Manchester, England, in 1945. It demanded independence for African "
          "colonies. Future leaders such as Nkrumah took part in the Pan-African movement."),
        T("Inside Africa, educated elites, trade unions and political parties organised. They held meetings, wrote in "
          "newspapers and won support from ordinary people."),
        H("Economic and political grievances"),
        T("**Economic grievances.** Farmers received low prices for cash crops. A cash crop is a crop grown to sell, "
          "such as cocoa or coffee. Forced labour was also used in many colonies. These problems turned ordinary people "
          "against colonial rule."),
        T("**Political grievances.** Africans had little say in the government that ruled them. Colonial rule was "
          "run by foreign officials. Educated Africans wanted a share of power, and nationalist parties grew out of "
          "this demand."),
        KEY("Sorting the causes", "Examiners like answers that group causes. Use two simple groupings.", cards=[
            ["External causes", "Weakened Britain and France; the UN Charter; pressure from the USA and the USSR; India's independence in 1947."],
            ["Internal causes", "Ex-servicemen; educated elites, parties and trade unions; the Manchester Congress; economic and political grievances."],
        ], note="Historians disagree about the balance. Some stress African action, others stress the weakness and choices "
                "of the colonial powers. Most combine both."),
        EX("Model answer plan 1", intro="Explain five factors that led to the decolonization of Africa after 1945.", steps=[
            S("Introduction", text="Define decolonization. Say that most of Africa became free between the late 1950s and 1975."),
            S("Effects of the Second World War", text="Britain and France were weakened; ex-servicemen returned with new ideas."),
            S("Role of the UN", text="The UN Charter supported self-determination and gave nationalists a principle to quote."),
            S("Superpower attitudes", text="The USA and the USSR both criticised old colonial empires."),
            S("Nationalist movements", text="Educated leaders, parties and trade unions organised the people; the Manchester Congress of 1945 demanded independence."),
            S("Example of Asia", text="India's independence in 1947 inspired African nationalists."),
            S("Conclusion", text="Internal and external factors worked together. Their balance differed from colony to colony."),
        ]),
        EX("Model answer plan 2", intro="Explain why economic and political grievances led ordinary Africans to support the nationalists.", steps=[
            S("Introduction", text="Explain that nationalists needed mass support, and grievances gave it to them."),
            S("Economic point 1", text="Low prices for cash crops left farmers poor, and the colonial system seemed to benefit foreigners."),
            S("Economic point 2", text="Forced labour was hated because it took people away from their own farms and families."),
            S("Political point", text="Africans had little say in government and educated Africans wanted a share of power."),
            S("Link to leaders", text="Parties and trade unions turned these complaints into demands for self-government and independence."),
            S("Conclusion", text="Grievances were the fuel, and organised nationalism was the fire. Without both, independence would have come later."),
        ]),
        H("Common mistakes"),
        MISTAKE("Writing a list instead of an explanation", "Do not only write 'the war, the UN, nationalism'. For each cause, say how it made colonial rule harder to keep."),
        MISTAKE("Giving only one side", "Many students write only about African nationalists, or only about Europe's weakness. Good answers use both."),
        MISTAKE("Mixing up the dates", "The Manchester Congress was in 1945. India became independent in 1947. The OAU came later, in 1963."),
        QUIZ("Which of these was an internal (African) cause of decolonization?",
             ["India's independence in 1947", "Pressure from the USA and the USSR", "Educated elites, parties and trade unions organising the people", "The weakness of Britain and France after the war"], 2,
             "Organised African nationalism is an internal cause. The other three come from outside Africa.",
             hint="An internal cause starts inside Africa.",
             feedback=["India is in Asia, so this is an external example.", "The superpowers were outside Africa.", "",
                       "The weakening of Britain and France is an external cause."]),
        QUIZ("What did the Pan-African Congress held in Manchester in 1945 demand?",
             ["Independence for African colonies", "The creation of the OAU", "The end of the Cold War", "The launch of the African Union"], 0,
             "The Manchester Congress of 1945 demanded independence for African colonies.",
             hint="Think of the year it was held and what nationalists wanted then.",
             feedback=["", "The OAU was founded in 1963.", "The Cold War began after 1945 and ended in 1991.", "The AU was launched in 2002."]),
        H("Practice questions"),
        PQ("Define decolonization and name two African states that were independent in 1945.",
           "Decolonization is the process by which colonies gained independence from European colonial powers. Ethiopia, Liberia and Egypt were independent in 1945."),
        PQ("State three ways in which the Second World War made it harder for Britain and France to keep their African colonies.",
           "It left them short of money and busy rebuilding; it damaged the idea that Europeans could not be defeated; "
           "African ex-servicemen returned with new ideas and expectations."),
        PQ("Explain the importance of Pan-Africanism and the Manchester Congress of 1945.",
           "Pan-Africanism taught that Africans share common interests and should unite. The Manchester Congress of 1945 "
           "demanded independence for African colonies. Together they gave nationalist leaders such as Nkrumah ideas and a platform."),
        PQ("Why were low prices for cash crops a cause of nationalism?",
           "Farmers earned little for crops such as cocoa or coffee, so they felt that the colonial system did not serve them. "
           "This made them ready to support parties that promised self-government."),
        SUM("Decolonization is the process by which colonies gained independence; most of Africa was free by 1975.",
            "The Second World War weakened Britain and France, and ex-servicemen returned with new ideas.",
            "The UN Charter and the pressure of the USA and the USSR supported self-determination.",
            "Pan-Africanism, the Manchester Congress of 1945 and organised nationalist movements drove the demand for independence.",
            "Economic grievances (low cash crop prices, forced labour) and political grievances turned ordinary people against colonial rule.",
            "Good answers explain both external and internal causes."),
    ],
))

# ---------------------------------------------------------------------------
# 2. Peaceful transfers and armed struggles
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MODULE, topic=DECOL,
    title="Two roads to independence: negotiation and armed struggle",
    slug="decolonization-peaceful-and-armed-routes",
    minutes=22,
    summary="How colonies became independent in different ways: negotiated transfers in Ghana, Nigeria and Senegal, "
            "and armed struggles in Algeria, Kenya, the Portuguese colonies and Zimbabwe.",
    objectives=[
        "Describe a peaceful transfer of power, with Ghana, Nigeria and Senegal as examples",
        "Describe armed liberation struggles in Algeria, Kenya, the Portuguese colonies and Zimbabwe",
        "Explain why some colonies followed one road and some the other",
        "Compare the two roads in a balanced answer",
    ],
    key_concepts=["Peaceful transfer", "Armed struggle", "Settlers", "Liberation movement", "Self-government", "Independence date"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you studied why colonial rule ended. Now we ask how it ended.\n\n"
          "There was no single road to independence. In some colonies leaders negotiated with the colonial power. "
          "In others, people took up arms."),
        IMG("f5h-decolonization-timeline.svg",
            alt="A timeline from 1945 to 1990 with eight dates: Manchester Congress, Ghana, 17 states in 1960, Algeria, Kenya and the OAU, the Portuguese colonies, Zimbabwe and Namibia",
            caption="Figure 1. Key dates of decolonization in this lesson (spaced evenly, not by scale)."),
        D("In a **peaceful transfer**, independence is won mainly by negotiation, elections and reforms, and power is "
          "handed over on a fixed date.", title="Peaceful transfer"),
        D("An **armed struggle** is a war of liberation, fought by a nationalist movement against the colonial power.",
          title="Armed struggle"),
        H("The peaceful road"),
        T("In many colonies, nationalist parties won elections. The colonial power then introduced reforms step by step "
          "and handed over power at an agreed date.\n\nPeaceful does not mean easy. Strikes, protests, party organising "
          "and hard bargaining all put pressure on the colonial government."),
        T("**Ghana.** The Gold Coast became independent as Ghana on 6 March 1957, under Kwame Nkrumah. It was the first "
          "colony south of the Sahara to win independence."),
        T("**Nigeria and Senegal.** Nigeria became independent in 1960. Senegal also became independent in 1960. Most French "
          "West African territories gained independence through negotiation as well."),
        T("**1960.** This is often called the year of independence in Africa. Seventeen African countries became "
          "independent in that year. Cameroon (French Cameroun) was one of them."),
        KEY("Why some colonies took the peaceful road", "Peaceful transfers were more likely when:", cards=[
            ["Few settlers", "There were few European families who had settled for life and wanted to keep power."],
            ["Willing colonial power", "The colonial power decided that negotiating was better than fighting."],
            ["Strong parties", "Nationalist parties could win elections and speak for the majority."],
        ]),
        H("The armed road"),
        T("Where there were many European settlers, or where the colonial power refused to leave, Africans often turned "
          "to armed struggle."),
        T("**Algeria.** The FLN (National Liberation Front) fought France from 1954. Algeria became independent in 1962."),
        T("**Kenya.** The Mau Mau uprising began in 1952. Kenya became independent in 1963."),
        T("**The Portuguese colonies.** Portugal refused to decolonize. This changed after a revolution in Lisbon in 1974. "
          "Angola, Mozambique and Guinea-Bissau won independence in 1974–1975 after long wars."),
        T("**Zimbabwe.** Zimbabwe became independent in 1980, after a struggle against a government run by the white "
          "minority. Namibia followed in 1990."),
        T("**Cameroon.** Cameroon's story combined both methods: the constitutional route led by Ahidjo, and the armed "
          "struggle of the UPC. Historians and Cameroonians still hold different views about this period."),
        KEY("Comparing the two roads", "Compare, do not just list.", cards=[
            ["Peaceful transfer", "Negotiation, elections and reforms. Few settlers. Ghana 1957, Nigeria 1960, Senegal 1960."],
            ["Armed struggle", "Many settlers or a colonial power that refused to leave. Algeria 1954–1962, Kenya from 1952, Angola, Mozambique, Zimbabwe 1980."],
        ], note="The two roads are not always separate. In many places pressure from nationalists and the threat of "
                "violence made negotiation possible."),
        EX("Model answer plan 1", intro="Compare peaceful and armed routes to independence in Africa, using examples.", steps=[
            S("Introduction", text="Say that independence came in different ways, and that the settlers and the attitude of the colonial power explain much of the difference."),
            S("Paragraph 1: peaceful route", text="Ghana 1957 under Nkrumah; Nigeria and Senegal 1960; negotiation, elections and step-by-step reform."),
            S("Paragraph 2: armed route", text="Algeria (FLN, 1954–1962) and Kenya (Mau Mau from 1952, independence 1963); the Portuguese colonies in 1974–1975."),
            S("Paragraph 3: reasons for the difference", text="Many settlers or a colonial power that refused to leave led to war; few settlers and a willing power led to talks."),
            S("Paragraph 4: similarity", text="In both cases nationalist movements, popular support and the weakening of colonial powers were the real drivers."),
            S("Conclusion", text="Give a balanced judgement: the roads differed in method, not in the African demand for freedom."),
        ]),
        EX("Model answer plan 2", intro="Why did the Portuguese colonies become independent later than most of Africa?", steps=[
            S("Introduction", text="Most colonies were free by 1960–1963, but Angola, Mozambique and Guinea-Bissau were free only in 1974–1975."),
            S("Portuguese refusal", text="Portugal refused to decolonize."),
            S("Long wars", text="Liberation movements fought long wars against Portugal."),
            S("The turning point", text="A revolution in Lisbon in 1974 changed Portugal's policy."),
            S("Result", text="Independence followed in 1974–1975. Link forward: the new states then faced Cold War rivalries (next topic)."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the peaceful road meant no struggle", "Peaceful transfers still needed pressure from parties, strikes and elections. Say 'mainly by negotiation'."),
        MISTAKE("Mixing up the dates", "Ghana 1957, Nigeria and Senegal 1960, Algeria 1962, Kenya 1963. Learn them as a short chain."),
        MISTAKE("Placing Algeria south of the Sahara", "Algeria is in North Africa. Ghana was the first colony south of the Sahara to win independence."),
        QUIZ("Which country became independent on 6 March 1957 under Kwame Nkrumah?",
             ["Nigeria", "Kenya", "Ghana", "Algeria"], 2,
             "Ghana, formerly the Gold Coast, became independent on 6 March 1957.",
             hint="It was the first colony south of the Sahara to be free.",
             feedback=["Nigeria became independent in 1960.", "Kenya became independent in 1963.", "", "Algeria became independent in 1962."]),
        QUIZ("Which situation made an armed struggle more likely?",
             ["Few settlers and a willing colonial power", "Many settlers and a colonial power that refused to leave", "A strong party winning every election", "Independence already promised for a fixed date"], 1,
             "Where many settlers lived or the colonial power refused to leave, negotiation failed and war often followed.",
             hint="Think of Algeria and the Portuguese colonies.",
             feedback=["That points to a peaceful transfer.", "", "Winning elections is part of the peaceful road.", "A promised date is a feature of a peaceful transfer."]),
        H("Practice questions"),
        PQ("Give two examples of countries that gained independence through armed struggle, with dates.",
           "Algeria (war from 1954, independence 1962) and Kenya (Mau Mau uprising from 1952, independence 1963). Also Angola and Mozambique (1975) or Zimbabwe (1980)."),
        PQ("Give two examples of peaceful transfers of power and say what made them peaceful.",
           "Ghana (6 March 1957) and Nigeria (1960). Nationalist parties won elections and the colonial power negotiated and handed over power on an agreed date."),
        PQ("Why did the Portuguese colonies win independence in 1974–1975?",
           "Portugal refused to decolonize and long wars were fought. A revolution in Lisbon in 1974 changed Portugal's policy, so Angola, Mozambique and Guinea-Bissau won independence."),
        PQ("Explain why 1960 is called the year of independence in Africa.",
           "Seventeen African countries became independent in that year, including Cameroon, Nigeria and Senegal."),
        SUM("Colonies gained independence by two main roads: negotiation and armed struggle.",
            "Peaceful transfers: Ghana (1957), Nigeria and Senegal (1960). Seventeen countries were free in 1960.",
            "Armed struggles: Algeria (1954–1962), Kenya (Mau Mau from 1952), the Portuguese colonies (1974–1975) and Zimbabwe (1980).",
            "Settlers and the colonial power's attitude help to explain which road a colony followed.",
            "Cameroon's road combined constitutional politics and armed struggle.",
            "In a good answer you compare the roads and explain the reasons for the differences."),
    ],
))

# ---------------------------------------------------------------------------
# 3. From the OAU to the African Union
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MODULE, topic=DECOL,
    title="From the OAU to the African Union",
    slug="oau-to-african-union",
    minutes=20,
    summary="The founding, aims, achievements and limits of the Organisation of African Unity (1963), and why the "
            "African Union replaced it in 2002.",
    objectives=[
        "State where and when the OAU and the AU were founded",
        "Describe the aims, achievements and limits of the OAU",
        "Explain why the OAU was replaced by the African Union",
        "Explain in general terms what regional bodies do",
    ],
    key_concepts=["OAU", "African Union", "Non-interference", "Liberation Committee", "Sovereignty", "Regional organisation"],
    blocks=[
        H("Introduction"),
        T("By 1963 many African states were independent, but most were new, poor and small. Their leaders asked how "
          "they could work together.\n\nIn the previous lessons you saw how colonies became free. This lesson shows how "
          "African states tried to cooperate after independence."),
        D("The **Organisation of African Unity (OAU)** was founded in Addis Ababa, Ethiopia, on 25 May 1963.",
          title="The OAU"),
        IMG("f5h-oau-au-compare.svg",
            alt="Two boxes compare the OAU (Addis Ababa, 25 May 1963, non-interference) with the African Union (Durban, 9 July 2002, intervention in grave circumstances, Pan-African Parliament)",
            caption="Figure 1. The OAU and the African Union compared."),
        H("Aims of the OAU"),
        T("The OAU wanted to promote unity among African states. It wanted to defend their sovereignty and territorial "
          "integrity. **Sovereignty** means a state's right to rule itself. **Territorial integrity** means keeping "
          "the borders of the state."),
        T("It also wanted to end colonialism in Africa and to promote cooperation and development. Its members "
          "accepted the borders they had inherited from colonial rule."),
        H("What the OAU achieved"),
        T("The OAU helped liberation movements through its Liberation Committee. It opposed apartheid, the system of "
          "racial separation in South Africa. It gave African states a place to discuss problems and a united voice "
          "in world politics."),
        T("Independence for Zimbabwe (1980) and Namibia (1990) happened while the OAU existed. Historians credit the "
          "liberation movements first, and see the OAU's support as one helpful factor."),
        H("Limits of the OAU"),
        T("The OAU had weak powers and little money. It could not enforce its decisions."),
        T("It followed a policy of **non-interference** in the internal affairs of members. This meant it could not "
          "act when governments abused their own people."),
        KEY("Judging the OAU", "A balanced answer weighs both sides.", cards=[
            ["Successes", "Unity and a common voice; support for liberation movements; opposition to apartheid; accepting inherited borders helped to avoid border wars."],
            ["Weaknesses", "Weak powers and little money; non-interference; some say that keeping colonial borders left old problems unsolved."],
        ], note="Historians disagree on whether accepting colonial borders was wise or a weakness. Give both views."),
        H("The African Union"),
        T("African leaders decided to create a stronger body. The **African Union (AU)** was launched in Durban, South "
          "Africa, on 9 July 2002."),
        T("The AU's Constitutive Act allows it to intervene in a member state in grave circumstances such as genocide "
          "and war crimes. It has new organs, such as the Pan-African Parliament and the Peace and Security Council."),
        T("New challenges also explain the change: civil wars, economic problems and globalisation. These needed "
          "stronger cooperation than the OAU could give."),
        H("Regional bodies"),
        T("Many African states also belong to **regional organisations**. These are groups of neighbouring states that "
          "cooperate on trade, security and development. Examples include ECOWAS in West Africa and SADC in southern Africa."),
        T("Regional bodies and the AU work at different levels. The AU deals with the whole continent. Regional bodies "
          "deal with the problems of one region."),
        EX("Model answer plan 1", intro="(a) State three aims of the OAU. (b) Why was the OAU replaced by the AU in 2002?", steps=[
            S("(a) Aims", text="Promote African unity; defend sovereignty and territorial integrity; end colonialism; promote cooperation and development."),
            S("(b) Weak powers", text="The OAU could not enforce its decisions and had little money."),
            S("(b) Non-interference", text="It could not act against abuses inside member states."),
            S("(b) New challenges", text="Civil wars, economic problems and globalisation needed stronger cooperation."),
            S("(b) Result", text="The AU, launched in Durban on 9 July 2002, has more powers, including the right to intervene in grave circumstances."),
        ]),
        EX("Model answer plan 2", intro="Assess how successful the OAU was between 1963 and 2002.", steps=[
            S("Introduction", text="State the OAU's aims and say you will weigh successes against failures."),
            S("Success 1", text="It supported liberation movements through its Liberation Committee."),
            S("Success 2", text="It opposed apartheid and gave Africa a united voice."),
            S("Failure 1", text="Weak powers and little money."),
            S("Failure 2", text="Non-interference left it unable to act against abuses."),
            S("Conclusion", text="A fair judgement: strong on ending colonial rule, weak on problems inside independent states. This is why the AU was created."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing OAU and AU dates and places", "OAU: Addis Ababa, 25 May 1963. AU: Durban, 9 July 2002."),
        MISTAKE("Saying the OAU had no successes", "It helped the liberation movements and opposed apartheid. Always give successes and failures."),
        MISTAKE("Saying the AU always intervenes", "The Constitutive Act allows intervention in grave circumstances. Say 'allows', not 'always does'."),
        QUIZ("Which policy limited the OAU most?",
             ["Support for liberation movements", "Non-interference in members' internal affairs", "Opposition to apartheid", "Promoting African unity"], 1,
             "Non-interference meant the OAU could not act against abuses inside member states.",
             hint="Look for a rule that stopped action, not one that allowed it.",
             feedback=["This was an achievement.", "", "This was an achievement.", "This was one of its aims."]),
        QUIZ("Where and when was the African Union launched?",
             ["Addis Ababa, 25 May 1963", "Durban, 9 July 2002", "Accra, 6 March 1957", "Algiers, 1962"], 1,
             "The AU was launched in Durban, South Africa, on 9 July 2002.",
             hint="It was launched in the early 2000s.",
             feedback=["That is the OAU's founding.", "", "That is Ghana's independence.", "Algeria's independence was in 1962, not an AU event."]),
        H("Practice questions"),
        PQ("Where and when was the OAU founded?", "In Addis Ababa, Ethiopia, on 25 May 1963."),
        PQ("State two achievements and two weaknesses of the OAU.",
           "Achievements: support for liberation movements through the Liberation Committee; opposition to apartheid. "
           "Weaknesses: weak powers and little money; non-interference in members' internal affairs."),
        PQ("State two differences between the OAU and the AU.",
           "The OAU followed strict non-interference, while the AU's Constitutive Act allows intervention in grave circumstances such as genocide. "
           "The AU has new organs, such as the Pan-African Parliament and the Peace and Security Council."),
        PQ("What is a regional organisation? Give one example.",
           "A group of neighbouring states that cooperate on trade, security and development, for example ECOWAS in West Africa or SADC in southern Africa."),
        SUM("The OAU was founded in Addis Ababa on 25 May 1963.",
            "Its aims: unity, defence of sovereignty and territorial integrity, an end to colonialism, cooperation and development.",
            "Achievements: support for liberation movements and opposition to apartheid. Limits: weak powers, little money and non-interference.",
            "The African Union was launched in Durban on 9 July 2002, with powers to intervene in grave circumstances and new organs.",
            "Regional bodies are groups of neighbouring states that work together on trade, security and development."),
    ],
))

# ---------------------------------------------------------------------------
# 4. Origins of the Cold War
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MODULE, topic=COLD,
    title="Origins of the Cold War: two superpowers, two blocs",
    slug="origins-of-the-cold-war",
    minutes=20,
    summary="Why the USA and the USSR, allies in the Second World War, became rivals after 1945: ideas, fear, "
            "Eastern Europe, the policy of containment, the Berlin Blockade and the two alliances.",
    objectives=[
        "Define the Cold War, superpower, capitalism, communism and containment",
        "Explain the causes of the rivalry between the USA and the USSR",
        "Describe the Berlin Blockade (1948–1949) and the formation of NATO and the Warsaw Pact",
        "Give a balanced view of who was responsible for the Cold War",
    ],
    key_concepts=["Cold War", "Superpower", "Iron curtain", "Containment", "NATO", "Warsaw Pact", "Arms race"],
    blocks=[
        H("Introduction"),
        T("From 1945 to 1991 the world was divided between two superpowers: the capitalist USA and the communist USSR. "
          "They never fought each other directly. But their rivalry shaped wars, alliances and even African politics.\n\n"
          "During this period many African governments, including Cameroon's, had to decide how close to stay to each bloc."),
        D("The **Cold War** was the state of tension and rivalry between the USA and its allies and the USSR and its allies "
          "from 1945 to 1991. It was fought by propaganda, arms races and proxy wars rather than direct war.",
          title="Cold War"),
        D("A **superpower** is a state so strong, in armies, weapons and wealth, that it can influence events across the world. "
          "After 1945 there were two: the USA and the USSR.", title="Superpower"),
        IMG("f5h-two-blocs.svg",
            alt="Two boxes: the Western bloc led by the USA with NATO (1949) and the Eastern bloc led by the USSR with the Warsaw Pact (1955), joined by a dashed line marked rivalry with no direct war",
            caption="Figure 1. The two blocs of the Cold War."),
        H("Causes of the rivalry"),
        T("**Opposing ideas.** The USA stood for **capitalism** (private business and profit) and democracy with several "
          "parties. The USSR stood for **communism** (the state controls the economy) and one-party rule. Each side "
          "thought the other's system was a danger."),
        T("**An alliance of convenience.** The two had been allies only to defeat Nazi Germany. When that aim was achieved, "
          "the main reason for cooperation disappeared."),
        T("**Eastern Europe.** After 1945 the USSR set up communist governments in Eastern Europe. In 1946 Winston Churchill "
          "said that an **iron curtain** had come down across Europe. The phrase meant the line dividing the communist East from the West."),
        T("**Fear on both sides.** The USA feared that communism would spread further. The USSR feared a Western attack. "
          "It also feared the US atomic bomb."),
        KEY("Causes in short", "Use these four headings in an essay.", cards=[
            ["Ideas", "Capitalism and democracy against communism and one-party rule."],
            ["Security", "The USA feared the spread of communism; the USSR feared the West and the atomic bomb."],
            ["Eastern Europe", "Communist governments in the East; the iron curtain."],
            ["Wartime alliance", "Allies against Nazi Germany only; the common enemy was gone."],
        ], note="Historians disagree about blame. Some stress Soviet expansion in Europe. Others stress US policy and "
                "fear on both sides. Many say both superpowers contributed."),
        H("Containment"),
        D("**Containment** was the US policy of stopping the spread of communism to new countries.", title="Containment"),
        T("The USA used economic, political and military methods. It gave economic aid to rebuild Western Europe, so that "
          "poverty would not help communism. It promised support to governments that resisted communism. And it built "
          "military alliances. (At A Level you study two of these policies by name, the Truman Doctrine and the Marshall Plan.)"),
        H("Berlin and the two alliances"),
        T("Germany and its capital, Berlin, were divided between the victors. The **Berlin Blockade** (1948–1949) was the "
          "first major crisis. The USSR cut the land routes to West Berlin. The West responded with an airlift, "
          "supplying the city by air."),
        T("In 1949 the USA and its allies formed **NATO**, a military alliance. The USSR and its allies formed the "
          "**Warsaw Pact** in 1955. Europe was now divided into two armed blocs."),
        T("Both sides built up weapons in an **arms race**: a competition to have more and better weapons."),
        EX("Model answer plan 1", intro="Explain why the Cold War began after 1945.", steps=[
            S("Introduction", text="Define the Cold War and say it was a rivalry, not a direct war."),
            S("Ideas", text="Capitalism and democracy against communism; each saw the other as a danger."),
            S("The end of the alliance", text="The USA and the USSR had been allies only against Nazi Germany."),
            S("Eastern Europe", text="The USSR set up communist governments; Churchill's iron curtain speech in 1946."),
            S("Fear", text="The USA feared communism would spread; the USSR feared the West and the atomic bomb."),
            S("Conclusion", text="Give a balanced judgement: both superpowers contributed, and historians stress different causes."),
        ]),
        EX("Model answer plan 2", intro="Describe the Berlin Blockade (1948–1949) and explain its importance.", steps=[
            S("The blockade", text="The USSR cut land routes to West Berlin in 1948."),
            S("The Western response", text="The West supplied the city by air, the Berlin Airlift, instead of giving it up."),
            S("Outcome", text="The blockade lasted until 1949."),
            S("Importance 1", text="It was the first major Cold War crisis."),
            S("Importance 2", text="In 1949 the USA and its allies formed NATO, and the USSR and its allies formed the Warsaw Pact in 1955."),
            S("Conclusion", text="It hardened the division of Europe into two blocs."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling the Cold War a direct war", "The USA and the USSR never fought each other directly. Use the words tension, rivalry and proxy war."),
        MISTAKE("Mixing up NATO and the Warsaw Pact", "NATO (1949) is the Western alliance led by the USA. The Warsaw Pact (1955) is the Eastern alliance led by the USSR."),
        MISTAKE("Blaming only one side", "Say that historians disagree and use evidence about both superpowers."),
        QUIZ("Which phrase did Winston Churchill use in 1946 to describe the division of Europe?",
             ["Containment", "An iron curtain", "Glasnost", "A proxy war"], 1,
             "Churchill said that an iron curtain had come down across Europe.",
             hint="The phrase suggests a heavy barrier between East and West.",
             feedback=["Containment was the name of the US policy.", "", "Glasnost was a Soviet reform of the 1980s.", "A proxy war is a conflict in which superpowers back opposing sides."]),
        QUIZ("What was the Berlin Blockade (1948–1949)?",
             ["The USSR cut land routes to West Berlin and the West supplied it by air", "A war between the USA and the USSR", "The building of NATO headquarters", "The opening of the Berlin Wall"], 0,
             "The USSR cut the land routes to West Berlin and the West responded with an airlift.",
             hint="The Berlin Wall opened in 1989, much later.",
             feedback=["", "There was no direct war between the two superpowers.", "NATO was formed in 1949 but this is not what the blockade was.", "The Berlin Wall opened in 1989."]),
        H("Practice questions"),
        PQ("Define the Cold War and containment.",
           "The Cold War was the state of tension and rivalry between the USA and its allies and the USSR and its allies from 1945 to 1991, "
           "without direct war between the superpowers. Containment was the US policy of stopping the spread of communism to new countries."),
        PQ("Name the two military alliances of the Cold War and the years they were formed.",
           "NATO (1949), led by the USA; the Warsaw Pact (1955), led by the USSR."),
        PQ("Give three causes of the Cold War.",
           "Opposing ideas (capitalism and democracy against communism); communist governments set up in Eastern Europe, the iron curtain; "
           "fear on both sides, of the spread of communism and of Western attack and the atomic bomb; the wartime alliance ended."),
        PQ("Why do historians disagree about who was to blame for the Cold War?",
           "Some stress Soviet control of Eastern Europe, others stress US policy and the fear felt on both sides. "
           "Both superpowers acted from fear and ideas, so many historians give both some responsibility."),
        SUM("The Cold War (1945–1991) was a rivalry between the capitalist USA and the communist USSR, fought without direct war.",
            "Causes: opposing ideas, the end of the wartime alliance, communist governments in Eastern Europe, and fear on both sides.",
            "Churchill spoke of an iron curtain across Europe in 1946.",
            "Containment was the US policy of stopping the spread of communism.",
            "The Berlin Blockade (1948–1949) was the first major crisis. NATO was formed in 1949 and the Warsaw Pact in 1955.",
            "Historians disagree about blame, so give a balanced answer."),
    ],
))

# ---------------------------------------------------------------------------
# 5. Crises and proxy conflicts
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MODULE, topic=COLD,
    title="Crises and proxy conflicts: Cuba, Vietnam and Africa",
    slug="cold-war-crises-and-proxy-conflicts",
    minutes=24,
    summary="The Cuban Missile Crisis of 1962 and its results, proxy wars in Korea and Vietnam, and Africa as a Cold War "
            "arena, with Angola as the main example.",
    objectives=[
        "Explain the causes, events and results of the Cuban Missile Crisis (1962)",
        "Define a proxy war and give examples from Asia and Africa",
        "Describe how the Cold War affected Africa, with advantages and disadvantages",
        "Write balanced answers on crises and proxy conflicts",
    ],
    key_concepts=["Cuban Missile Crisis", "Blockade", "Hotline", "Proxy war", "Non-alignment", "MPLA"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you learned how the Cold War began. This lesson looks at the moments when it came "
          "close to real war, and at the places where the superpowers fought through others."),
        D("A **proxy war** is a conflict in which the superpowers support opposing sides without fighting each other directly.",
          title="Proxy war"),
        H("The Cuban Missile Crisis (1962)"),
        T("After Fidel Castro's revolution in 1959, Cuba became an ally of the USSR. In 1961 a US-backed invasion at the Bay of "
          "Pigs failed. Cuba then looked to the USSR for protection."),
        T("In October 1962, US spy planes found Soviet nuclear missile sites in Cuba, about 150 km from Florida. The "
          "Soviet leader Khrushchev may have wanted to protect Cuba and to balance US missiles in Turkey."),
        T("President Kennedy ordered a naval blockade, called a quarantine, of Cuba. For thirteen days the world feared "
          "nuclear war."),
        T("Khrushchev agreed to remove the missiles. The USA promised not to invade Cuba. It later removed its own "
          "missiles from Turkey."),
        T("A telephone **hotline** between Washington and Moscow was set up in 1963. A Partial Test Ban Treaty was also "
          "signed in 1963. Both sides became more careful about direct confrontation."),
        KEY("Who gained from the crisis?", "A balanced answer looks at both sides.", cards=[
            ["For the USA", "The missiles left Cuba and the USA showed firmness."],
            ["For the USSR", "Cuba was safe from invasion and the missiles in Turkey were later removed."],
        ], note="Both leaders avoided war. Historians disagree on who gained more, so avoid saying that one side simply won."),
        H("Proxy wars in Asia"),
        T("**Korea (1950–1953).** UN forces led by the USA fought North Korea and China. North Korea was supported by "
          "communist powers. Neither superpower fought the other directly."),
        T("**Vietnam.** The USA fought communist forces until it withdrew in 1973. Vietnam was united under communist rule "
          "in 1975. The war divided opinion in the USA itself."),
        H("Africa as a Cold War arena"),
        T("Newly independent African states were poor and wanted aid, weapons and allies. The superpowers wanted friends "
          "and influence. Some governments joined a bloc. Others chose **non-alignment**, which means staying "
          "out of both blocs."),
        T("**Angola.** After independence in 1975, the USSR and Cuba supported the MPLA government. The USA and South "
          "Africa backed its rivals. A local struggle for power became part of the Cold War."),
        T("**Afghanistan (1979–1989).** This is not in Africa, but it matters for the end of the Cold War. Soviet troops "
          "fought rebels supported by the USA."),
        KEY("Effects of the Cold War on Africa", "Give advantages and disadvantages.", cards=[
            ["Possible gains", "Aid, training and weapons for liberation movements and governments; superpower attention to African causes."],
            ["Costs", "Local wars made longer and deadlier by foreign weapons; pressure to choose a side; debt and dependence."],
        ], note="Historians stress different effects. Many say that local causes started African conflicts, and that the "
                "Cold War made them worse."),
        EX("Model answer plan 1", intro="Explain the causes and results of the Cuban Missile Crisis of 1962.", steps=[
            S("Cause: Cuban revolution", text="Castro took power in 1959 and moved close to the USSR."),
            S("Cause: Bay of Pigs (1961)", text="A failed US-backed invasion made Cuba seek Soviet protection."),
            S("Cause: Soviet strategy", text="Khrushchev wanted to protect Cuba and balance US missiles in Turkey."),
            S("Event", text="October 1962: missiles found, US blockade, thirteen days of tension, deal to remove them."),
            S("Result: hotline and test ban", text="A Washington–Moscow hotline and the 1963 Partial Test Ban Treaty."),
            S("Result: caution", text="Both superpowers avoided direct confrontation afterwards."),
        ]),
        EX("Model answer plan 2", intro="Explain how the Cold War affected Africa.", steps=[
            S("Introduction", text="Define the Cold War and say that newly independent states had to decide how close to stay to each bloc."),
            S("Advantages", text="Aid, weapons and training; liberation movements found support."),
            S("Angola", text="After 1975 the USSR and Cuba supported the MPLA, and the USA and South Africa backed its rivals."),
            S("Disadvantages", text="Foreign weapons made wars longer; states were pressed to take sides."),
            S("Non-alignment", text="Some governments tried to stay out of both blocs."),
            S("Conclusion", text="Give a balanced judgement: the Cold War did not cause every African conflict, but it shaped many."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the USA and the USSR fought each other in Cuba", "Neither fired on the other. The crisis ended with a deal. Describe it as a standoff."),
        MISTAKE("Saying one side simply won", "Both gave something. Show what each side gained and gave up."),
        MISTAKE("Blaming the Cold War for every African war", "Local causes also mattered. Say that the Cold War made them worse or longer."),
        QUIZ("How did the Cuban Missile Crisis end?",
             ["The USA invaded Cuba", "Khrushchev agreed to remove the missiles and the USA promised not to invade Cuba", "The USSR attacked Florida", "NATO and the Warsaw Pact fought a war"], 1,
             "Khrushchev removed the missiles. The USA promised not to invade Cuba and later removed its missiles from Turkey.",
             hint="Each side gave something to avoid nuclear war.",
             feedback=["The USA promised not to invade.", "", "The USSR did not attack.", "The two alliances never fought each other directly."]),
        QUIZ("In Angola after 1975, which government did the USSR and Cuba support?",
             ["The MPLA", "Portugal", "South Africa", "The OAU"], 0,
             "The USSR and Cuba supported the MPLA. The USA and South Africa backed its rivals.",
             hint="Angola is the lesson's example of a proxy war in Africa.",
             feedback=["", "Portugal left after the 1974 revolution.", "South Africa backed the MPLA's rivals.", "The OAU is an African organisation, not a side in the war."]),
        H("Practice questions"),
        PQ("Give two results of the Cuban Missile Crisis.",
           "A telephone hotline between Washington and Moscow and the Partial Test Ban Treaty (both 1963). Both sides also became more cautious about direct confrontation."),
        PQ("Give two examples of proxy wars and say which superpower supported which side.",
           "Korea (1950–1953): the USA led UN forces against North Korea, which communist powers supported. Angola (from 1975): the USSR and Cuba "
           "supported the MPLA, and the USA and South Africa backed its rivals. Vietnam and Afghanistan are other examples."),
        PQ("Why did some African states choose non-alignment?",
           "They wanted aid and independence of action without being controlled by either bloc, and did not wish to be drawn into the superpowers' rivalry."),
        PQ("Give one advantage and one disadvantage of the Cold War for Africa.",
           "Advantage: aid, weapons and training for governments and liberation movements. Disadvantage: foreign weapons and superpower rivalry made local wars longer and deadlier."),
        SUM("The Cuban Missile Crisis (October 1962) followed Castro's revolution and the Bay of Pigs. For thirteen days the world feared nuclear war.",
            "It ended when Khrushchev removed the missiles and the USA promised not to invade Cuba.",
            "Results: a hotline and the Partial Test Ban Treaty in 1963, and more caution on both sides.",
            "Proxy wars: Korea (1950–1953), Vietnam (US withdrawal in 1973, unity under communist rule in 1975), Angola (from 1975).",
            "In Africa the Cold War brought aid and weapons but also longer, deadlier local wars.",
            "Give balanced answers: avoid saying that one superpower simply won."),
    ],
))

# ---------------------------------------------------------------------------
# 6. End of the Cold War
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=MODULE, topic=COLD,
    title="The end of the Cold War and the collapse of the USSR",
    slug="end-of-cold-war-and-soviet-collapse",
    minutes=22,
    summary="Gorbachev's reforms, the revolutions of 1989, the fall of the Berlin Wall, the dissolution of the USSR in "
            "December 1991 and the consequences for Africa and the world.",
    objectives=[
        "Define glasnost and perestroika",
        "Describe the events of 1985 to 1991 in the right order",
        "Explain the economic and political causes of the Soviet collapse",
        "Explain consequences for Africa and the world, with balance",
    ],
    key_concepts=["Gorbachev", "Glasnost", "Perestroika", "Berlin Wall", "Reunification", "Dissolution of the USSR", "Multi-party politics"],
    blocks=[
        H("Introduction"),
        T("The Cold War ended without a battle between the superpowers. Between 1985 and 1991 the Soviet Union weakened "
          "and then disappeared.\n\nIn the previous lesson you studied crises and proxy wars. This lesson shows how "
          "the rivalry finally ended, and what it meant for Africa."),
        IMG("f5h-cold-war-timeline.svg",
            alt="A timeline of eight Cold War dates: iron curtain 1946, Berlin Blockade 1948-49, NATO 1949, Warsaw Pact 1955, Cuban Missiles 1962, Gorbachev 1985, Berlin Wall opens 1989, USSR ends 1991",
            caption="Figure 1. Key dates of the Cold War (spaced evenly, not by scale)."),
        H("Gorbachev's reforms"),
        T("Mikhail Gorbachev became Soviet leader in 1985. The Soviet economy was weak, and he tried to save it."),
        D("**Glasnost** means openness: more freedom of speech and information.", title="Glasnost"),
        D("**Perestroika** means economic restructuring: changes to make the economy work better.", title="Perestroika"),
        T("Gorbachev also reduced arms spending. The reforms let people criticise the system, and criticism grew."),
        H("From 1989 to 1991"),
        T("In 1989 communist governments fell across Eastern Europe. The Berlin Wall was opened on 9 November 1989. "
          "Germany was reunified on 3 October 1990."),
        T("In August 1991 there was a failed coup against Gorbachev. After it, Soviet republics declared independence. "
          "The USSR was dissolved in December 1991."),
        KEY("Why the USSR collapsed", "Combine several causes in your answer.", cards=[
            ["Economic", "A stagnant economy, shortages, and the huge cost of the arms race and the war in Afghanistan."],
            ["Political", "Gorbachev's reforms allowed criticism; nationalism in the republics; the failed 1991 coup."],
        ], note="Historians weigh these differently: some stress Western pressure, others internal weakness."),
        EX("Model answer plan 1", intro="Explain why the USSR collapsed in 1991.", steps=[
            S("Introduction", text="Say that the USSR was dissolved in December 1991 after years of decline."),
            S("Economic weakness", text="A stagnant economy and shortages made life hard."),
            S("Cost of rivalry", text="The arms race and the war in Afghanistan were very expensive."),
            S("Gorbachev's reforms", text="Glasnost and perestroika meant criticism and change, but the economy did not improve fast enough."),
            S("Nationalism and the coup", text="Nationalism in the republics and the failed coup of August 1991 led republics to declare independence."),
            S("Conclusion", text="Weigh the views: some historians stress Western pressure, others internal weakness; most combine them."),
        ]),
        H("Consequences for the world"),
        T("The Cold War's two-bloc order ended. The USA became the sole superpower. Germany was reunified, and the "
          "Warsaw Pact ended. The republics of the USSR became independent states."),
        T("Many people hoped for a calmer world. Others pointed to new conflicts and new rivalries. The next topic in "
          "this module, the post-Cold War world, looks at this."),
        H("Consequences for Africa"),
        T("**Less superpower interest.** Aid and attention from the superpowers fell. Some proxy conflicts, such as "
          "Angola's, lost foreign backing. Historians note that some wars ended while others continued from local causes."),
        T("**Pressure for change inside Africa.** In the early 1990s many African states moved towards multi-party politics. "
          "Historians link this to the end of the Cold War, to economic crisis and to demands from African citizens. "
          "Cameroon's 1990 'liberty laws' and democratic revival belong to this period."),
        T("**Southern Africa.** Namibia became independent in 1990. South Africa's apartheid system also came to an end "
          "in the early 1990s. The causes were mainly inside South Africa, but historians also note the changing world."),
        KEY("Consequences in short", "Balance gains and losses.", cards=[
            ["For the world", "End of the two-bloc order; USA as sole superpower; German reunification; new independent states."],
            ["For Africa", "Less superpower aid and weapons; pressure for multi-party politics; end of some proxy wars; independence for Namibia."],
        ], note="Do not say that the Cold War's end solved Africa's problems. Gains and new difficulties came together."),
        EX("Model answer plan 2", intro="Explain two consequences of the end of the Cold War for Africa.", steps=[
            S("Introduction", text="Say that the Cold War had shaped African politics, so its end changed them."),
            S("Consequence 1: aid and rivalry", text="Superpower interest and aid fell; some proxy conflicts lost foreign backing, while others continued from local causes."),
            S("Consequence 2: politics", text="Many states moved to multi-party politics in the early 1990s, helped by the changed world, economic crisis and local demands."),
            S("Example", text="Cameroon's democratic revival and 1990 liberty laws; Namibia's independence in 1990."),
            S("Conclusion", text="Give a balanced judgement: change brought hope and new difficulties."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up 1989 and 1991", "1989: the Berlin Wall opened and Eastern Europe was freed. 1991: the USSR itself was dissolved."),
        MISTAKE("Mixing up glasnost and perestroika", "Glasnost means openness. Perestroika means economic restructuring."),
        MISTAKE("Saying one cause explains everything", "Name economic and political causes and say that historians weigh them differently."),
        QUIZ("What did the term glasnost mean?",
             ["Economic restructuring", "Openness", "The arms race", "Containment"], 1,
             "Glasnost meant openness: more freedom of speech and information.",
             hint="Perestroika is the other Gorbachev word.",
             feedback=["That is perestroika.", "", "The arms race was the competition in weapons.", "Containment was a US policy."]),
        QUIZ("When was the Berlin Wall opened, and when was the USSR dissolved?",
             ["1961 and 1985", "9 November 1989 and December 1991", "1991 and 1989", "3 October 1990 and 1962"], 1,
             "The Berlin Wall was opened on 9 November 1989. The USSR was dissolved in December 1991.",
             hint="The wall came first.",
             feedback=["The dates do not match these events.", "", "The two dates are in the wrong order.", "3 October 1990 was German reunification; 1962 was the Cuban crisis."]),
        H("Practice questions"),
        PQ("State three reasons for the collapse of the USSR.",
           "Economic weakness and shortages; the cost of the arms race and the war in Afghanistan; Gorbachev's reforms "
           "(glasnost and perestroika) that allowed criticism; nationalism in the republics; the failed coup of August 1991."),
        PQ("Put these in order: dissolution of the USSR, Gorbachev becomes leader, Berlin Wall opens, German reunification.",
           "Gorbachev becomes leader (1985); Berlin Wall opens (9 November 1989); German reunification (3 October 1990); dissolution of the USSR (December 1991)."),
        PQ("Give two consequences of the end of the Cold War for the world.",
           "The USA became the sole superpower; Germany was reunified; the Warsaw Pact ended; the republics of the USSR became independent states."),
        PQ("Explain one way in which the end of the Cold War affected Africa.",
           "Superpower aid and interest fell and some proxy conflicts lost foreign backing. Also, many African states moved towards multi-party politics in the early 1990s, helped by the changed world, economic crisis and demands from citizens."),
        SUM("Gorbachev became Soviet leader in 1985 and introduced glasnost (openness) and perestroika (economic restructuring).",
            "In 1989 communist governments fell across Eastern Europe; the Berlin Wall was opened on 9 November 1989; Germany was reunified on 3 October 1990.",
            "After the failed coup of August 1991, republics declared independence and the USSR was dissolved in December 1991.",
            "Causes: economic weakness, the cost of the arms race and Afghanistan, reforms that allowed criticism, and nationalism.",
            "Consequences for the world: the USA became the sole superpower and the two-bloc order ended.",
            "Consequences for Africa: less superpower interest, pressure for multi-party politics and independence for Namibia in 1990."),
    ],
))


def _merge_short_texts(lessons):
    """Join runs of plain text blocks into short multi-paragraph blocks to keep lessons compact on phones."""
    for les in lessons:
        out = []
        run = 0
        for b in les["blocks"]:
            plain = b["block_type"] == "text" and not b["title"]
            if plain and out and out[-1]["block_type"] == "text" and not out[-1]["title"] and run < 3:
                out[-1]["body"] += "\n\n" + b["body"]
                run += 1
            else:
                out.append(b)
                run = 1 if plain else 0
        les["blocks"] = out


_merge_short_texts(LESSONS)
