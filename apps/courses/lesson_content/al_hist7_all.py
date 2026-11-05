"""Upper Sixth History (A Level 0760, Year 2): deeper lessons for each topic (KKEVO draft for reviewer checking).

Sensitive topics (the UPC conflict, Southern Cameroons, the post-colonial state, the Anglophone question) are
presented through documents, events and the evidence each interpretation uses. Reviewers: please check every date,
name and figure against the official GCE Board syllabus and standard textbooks.
Any statement marked 'check your textbook' is one KKEVO could not confirm from memory.
Examples labelled 'illustrative source' are invented teaching texts, never real quotations.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "upper-sixth")

M_CMR = "Cameroon 1945 to Today"
M_DEC = "Decolonization in Africa"
M_CW = "Cold War & International Governance"
M_EX = "Examination"

LESSONS = []

# ---------------------------------------------------------------------------
# 1. Trusteeship machinery
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Trusteeship and decolonization",
    title="How trusteeship worked: agreements, visiting missions and petitions",
    slug="h7-cmr-trusteeship-machinery",
    minutes=22,
    summary=("The legal machinery of UN trusteeship in the two Cameroons after 1946: the Charter, the Trusteeship "
             "Council, visiting missions and petitions, and why France and the UPC read the system differently."),
    objectives=[
        "Explain how trusteeship differed from the League of Nations mandate and from ordinary colonial rule",
        "Describe the roles of the Trusteeship Council, visiting missions and petitions",
        "Compare the French and the UPC readings of the trusteeship agreement",
        "Judge the strengths and limits of the UN as a check on the administering power",
    ],
    key_concepts=["Trusteeship Agreement", "Trusteeship Council", "Visiting mission", "Petition", "Article 76", "Mandate"],
    blocks=[
        H("Introduction"),
        T("Imagine a farmer near Nkongsamba in 1950 who wants to complain about forced labour or land. Under ordinary "
          "colonial rule the only people to complain to were the colonial officials. Under UN trusteeship there was "
          "a second address: the United Nations. This lesson explains how that second address worked and where it failed."),
        D("A **trust territory** was a territory placed under the UN trusteeship system, administered by a named "
          "state (the administering authority) under a **Trusteeship Agreement** approved by the UN General Assembly. "
          "For the two Cameroons the agreements were approved in December 1946.", title="Trusteeship"),
        D("The **Trusteeship Council** was the UN organ that supervised trust territories. Its members included the "
          "administering states and an equal number of states that did not administer trust territories.",
          title="Trusteeship Council"),
        D("A **visiting mission** was a small team sent by the Council to tour a territory, meet people and report. "
          "A **petition** was a written complaint or request sent by inhabitants to the UN.", title="Missions and petitions"),
        H("Mandate and trusteeship"),
        T("Kamerun had been a League of Nations mandate under Britain and France after 1919 (in two parts). "
          "When the League ended, the UN created trusteeship to replace mandates, and the two Cameroons were placed "
          "under it. The Charter set out the aims in Article 76, including progress towards self-government or "
          "independence as might be appropriate. Article 87 allowed the General Assembly and the Council to "
          "accept petitions, examine reports and arrange periodic visits."),
        KEY("What changed from mandate to trusteeship?", "The key difference is the stronger link to the inhabitants.", cards=[
            ["Under the League mandate", "The administering state reported to a Commission in Geneva. Petitions had to pass "
             "through the administering state, the Commission could not send visiting missions, and independence was not stated as an aim."],
            ["Under UN trusteeship", "The Charter named self-government or independence as an aim, and gave "
             "inhabitants the right to petition the UN and to meet visiting missions. Check your textbook for the details of both systems."],
        ]),
        IMG("al-h7-trusteeship-flow.svg",
            alt="Diagram: the UN, the administering power and the inhabitants, linked by reports, questions, visits and petitions",
            caption="Figure 1. Trusteeship as a triangle of communication (schematic)."),
        H("Two territories, two administrations"),
        T("The two Cameroons were administered differently. France ran its part as a separate territory attached "
          "to the French Union as an 'associated territory'. Britain ran Southern Cameroons and Northern Cameroons "
          "as parts of its Nigerian administration. The same UN rules applied, but the political results were very different."),
        T("Visiting missions toured the Cameroons in 1949, 1952, 1955 and again later in the 1950s (check your "
          "textbook for exact years and for the separate missions to the British and the French parts). Each time "
          "they met parties and chiefs, listened to complaints and wrote reports with recommendations."),
        H("Two readings of the agreement"),
        KEY("Colony or trust territory?", "The disagreement was about what the agreement allowed.", cards=[
            ["French position", "The territory was associated with the French Union. France stressed gradual "
             "reform and said that the pace of change must suit local conditions."],
            ["UPC position", "The Charter promised self-government or independence. France should set a timetable "
             "and should not tie the territory permanently to the French Union."],
        ], note="Both sides quoted the same texts. A good answer shows how each side read them."),
        H("What the system could and could not do"),
        T("Strengths: trusteeship kept the Cameroons on the world's agenda, created a legal duty to report, and "
          "gave Cameroonian leaders a platform. Limits: the Council could examine and recommend but could not "
          "dismiss the administering authority; the administering states were members of the Council; and Cold War "
          "politics shaped how far the UN would press its allies."),
        EX("Model answer plan 1", intro="How far did trusteeship change the way the Cameroons were governed after 1946?", steps=[
            S("Point 1: a new legal duty", text="Article 76 and the Trusteeship Agreement required progress towards self-government or independence."),
            S("Point 2: new channels", text="Visiting missions and petitions gave Cameroonians access outside the colonial administration."),
            S("Point 3: limits", text="The administering power still ran the territory, and the Council could only recommend."),
            S("Judgement", text="Trusteeship changed the language and the legal framework more than daily government. It mattered most as a platform for nationalists."),
        ]),
        EX("Model answer plan 2", intro="Compare the French and the UPC readings of France's duties under trusteeship.", steps=[
            S("France", text="Associated territory of the French Union; gradual reform; stability first."),
            S("UPC", text="A trust territory is not a colony; the Charter requires a path to independence; reunification of the two Cameroons."),
            S("Evidence each used", text="France: the wording on association and the practical need for training. UPC: Article 76 and the petitions to the UN."),
            S("Judgement", text="The texts allowed both readings, so the argument was political. The balance of power decided which reading prevailed."),
        ]),
        H("Reading a source: a petition"),
        T("Source skill: ask who wrote it, for whom, when, and what it does not say. Below is an **illustrative "
          "source invented for practice**, not a real document."),
        T("Illustrative source (invented): 'We the market women of a southern town write to the Trusteeship Council. "
          "The tax collectors take our goods when we cannot pay. Please ask the administering authority to explain "
          "why we have no representative in the assembly.'", title="Illustrative source"),
        T("What can you infer? It shows that petitioners knew the UN existed and what it was for (provenance and "
          "purpose). It shows one grievance (taxation and representation). It cannot show how many people felt the "
          "same, or whether the administration answered. A historian would look for other petitions and for the administering authority's reply."),
        MISTAKE("Treating trusteeship as UN rule", "The UN supervised. France and Britain administered. Say who held real power."),
        MISTAKE("Saying the UN could force reforms", "The Council could report, question and recommend. It could not compel."),
        QUIZ("Which article of the UN Charter set out the basic objectives of trusteeship?",
             ["Article 2", "Article 51", "Article 76", "Article 99"], 2,
             "Article 76 lists the aims of trusteeship, including progress towards self-government or independence.",
             hint="It is in Chapter XII of the Charter.",
             feedback=["Article 2 sets principles for the whole Organisation, such as not using force.",
                       "Article 51 concerns self-defence.", "", "Article 99 allows the Secretary-General to bring matters to the Security Council."]),
        QUIZ("A visiting mission was",
             ["A force that replaced the colonial army", "A team sent by the Trusteeship Council to see conditions and report",
              "A committee of the administering power", "A meeting of Cameroonian chiefs only"], 1,
             "Missions were UN teams that toured, listened and reported to the Council.",
             feedback=["Missions had no military role.", "",
                       "They were organised by the UN, not by the administering power.", "They met many groups, not only chiefs."]),
        H("Practice questions"),
        PQ("Explain two ways in which trusteeship differed from ordinary colonial rule.",
           "First, the Charter named self-government or independence as an aim. Second, inhabitants could petition the UN and meet "
           "visiting missions. Also acceptable: the administering state had to report to an international body."),
        PQ("Describe two limits on the UN's power over an administering authority in the 1950s.",
           "The Council could only recommend and could not remove the administering authority. The administering states were themselves "
           "members of the Council, and the great powers had their own interests."),
        PQ("Why did Cameroonian nationalists use petitions and visiting missions?",
           "They gave a platform outside the colonial system, publicised grievances internationally, and let parties such as the UPC "
           "argue that the territory was entitled to independence. They were also cheap compared with armed or street politics."),
        PQ("Source question: what can and what can't the invented market women's petition tell a historian?",
           "It can show awareness of the UN and a grievance about tax and representation. It cannot show how widespread the grievance was or "
           "whether the administration responded. Further sources are needed."),
        SUM("Trusteeship replaced the League mandate and named self-government or independence as an aim.",
            "Visiting missions and petitions were the main channels linking inhabitants to the UN.",
            "France and the UPC read the agreement differently: associated territory versus path to independence.",
            "The UN could report and recommend but could not compel the administering power."),
    ],
))

# ---------------------------------------------------------------------------
# 2. UPC to Ahidjo
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Trusteeship and decolonization",
    title="The UPC, the conflict and Ahidjo's rise to independence, 1948 to 1960",
    slug="h7-cmr-upc-conflict-ahidjo-1960",
    minutes=24,
    summary=("A chronology and an evidence-based discussion of the UPC, the 1955 ban, the armed conflict and French "
             "'pacification', and how Ahmadou Ahidjo became head of government and then President in 1960."),
    objectives=[
        "Sequence the main events from the founding of the UPC in 1948 to independence on 1 January 1960",
        "Explain the causes of the 1955 ban and the later conflict from different viewpoints",
        "Describe how Ahidjo replaced Mbida in 1958 and led the state to independence",
        "Present the main interpretations of the UPC and of the 1960 settlement with their evidence",
    ],
    key_concepts=["UPC", "Ban of 1955", "Maquis", "Pacification", "Loi-Cadre", "Union Camerounaise", "1 January 1960"],
    blocks=[
        H("Introduction"),
        T("The years 1948 to 1960 are among the most disputed in Cameroonian history. Historians agree on many "
          "dates but disagree about causes, responsibility and meaning. This lesson gives the sequence first, "
          "then the interpretations. It describes events and the evidence used. It does not judge current politics."),
        IMG("al-h7-cameroon-timeline-1945-1961.svg",
            alt="Timeline of Cameroon from 1946 to 1961 showing the UPC, the ban, independence and reunification",
            caption="Figure 1. Key dates, 1946 to 1961 (not to scale)."),
        H("The sequence"),
        KEY("From party to conflict", "Learn the order of events first.", cards=[
            ["1948 to 1954", "The UPC is founded in Douala (April 1948). Ruben Um Nyobe leads its campaign for "
             "reunification and independence, including petitions and a speech to the UN in 1952."],
            ["1955 to 1957", "Violent clashes in May 1955 are followed by the ban on the UPC in July 1955. Leaders go "
             "into exile or into the forest. Armed resistance grows from 1956 in the Sanaga-Maritime. The Loi-Cadre "
             "elections of December 1956 take place without the UPC."],
            ["1957 to 1960", "A state with an assembly and a Prime Minister is set up in 1957 (Mbida). Ahidjo "
             "replaces Mbida in February 1958. Um Nyobe is killed in September 1958. "
             "The UN agrees in March 1959 to end trusteeship on 1 January 1960."],
        ]),
        T("After independence, fighting continued, especially in the Bamileke region and the Mungo. Felix-Roland "
          "Moumie died in Geneva in November 1960. Ernest Ouandie was captured and executed in January 1971. "
          "Casualty figures for the whole conflict are not known with confidence and estimates differ widely."),
        D("**Pacification** was the French official term for operations against the maquis. Critics argue that the "
          "word hides the scale of violence against civilians. Supporters of the term used it to describe restoring order.",
          title="A contested word"),
        H("Why did Ahidjo rise?"),
        T("Ahmadou Ahidjo came from the north and was a politician of the Union Camerounaise, formed in 1958. He had "
          "been a deputy to Mbida. Mbida lost the confidence of the French High Commissioner and of the assembly "
          "and resigned in February 1958. Ahidjo formed a government and was acceptable to France as a partner for "
          "a transfer of power."),
        T("Reasons given by historians include: his political base in the north, his readiness to cooperate with "
          "France on the date and terms of independence, the removal of the UPC from legal politics, and his "
          "skill in building coalitions in the assembly."),
        T("Independence came on 1 January 1960. A constitution was approved by referendum in February 1960, "
          "legislative elections followed in April, and Ahidjo was elected President in May 1960 "
          "(check your textbook for the exact days)."),
        H("Interpretations and the evidence for each"),
        KEY("Three ways to read 1948 to 1960", "A strong essay names the view, gives its evidence and tests it.", cards=[
            ["A nationalist reading", "The UPC was the authentic national movement. Evidence: its mass support in "
             "the south, its UN petitions, the ban and the military campaign. Limit: it does not explain Ahidjo's real "
             "support or UPC divisions."],
            ["A negotiated-transfer reading", "Independence came through talks with France and the UN, with a "
             "government that had local support. Evidence: the Loi-Cadre, the 1957 statute, the UN vote of 1959. "
             "Limit: the UPC was excluded, and no new elections were held first."],
            ["A social-history reading", "Local grievances, chiefs, churches, migrants and rural conditions "
             "shaped who joined the maquis. Evidence: regional differences between the Sanaga-Maritime, the Bamileke "
             "region and the north. Limit: harder to generalise for the whole country."],
        ], note="Historians such as Richard Joseph, Achille Mbembe, Meredith Terretta and others wrote on these themes. Check your textbook for the titles."),
        EX("Model answer plan 1", intro="Assess the reasons why the UPC was banned in 1955.", steps=[
            S("Argument: the French view", text="The administration blamed the UPC for the violence of May 1955 and said it was a revolutionary threat, linked to communism."),
            S("Argument: the UPC view", text="The party said the ban was political, intended to stop its demand for independence."),
            S("Evidence", text="The riots of May 1955 in Douala, Yaounde and other towns; the decree of July 1955."),
            S("Judgement", text="The ban had a stated security reason, but its timing and effects show a political purpose as well. Historians still debate how far the party planned the violence."),
        ]),
        EX("Model answer plan 2", intro="'Ahidjo came to power because France wanted him.' Discuss.", steps=[
            S("For", text="France influenced Mbida's fall; cooperation with France shaped Ahidjo's terms for independence."),
            S("Against", text="Ahidjo built a real political base, won votes in the assembly and led a party he created."),
            S("Evidence", text="1958 change of Prime Minister; Union Camerounaise; the assembly votes of 1958 and 1959."),
            S("Judgement", text="French support was important, but a purely French explanation ignores local politics. Both mattered."),
        ]),
        H("Source skill: weighing a report"),
        T("Illustrative source (invented for practice): 'The operation in the forest cleared the area of armed "
          "bands. Order has returned to the villages and the people welcome the troops.' (A report written by an officer to his superior.)",
          title="Illustrative source"),
        T("Provenance: written by one side, to a superior, probably to show success. Content: claims success and "
          "welcome, with no figures and no voices from villagers. Use: it shows how the operation was officially "
          "described, not what villagers experienced. Cross-check with other accounts, church records and later testimony."),
        MISTAKE("Giving one casualty figure as fact", "Say that estimates differ and that the exact number is unknown."),
        MISTAKE("Writing as if the UPC was only a violent group or only a heroic one", "Both simplifications skip evidence. Describe its aims, methods, support and the state's response."),
        QUIZ("What happened to the UPC in July 1955?",
             ["It won the Cameroun elections", "It was banned by the French administration", "It merged with the Union Camerounaise",
              "It was dissolved by the UN"], 1,
             "The UPC was banned by decree in July 1955 after the violence of May.",
             feedback=["It could not take part in the December 1956 elections.", "",
                       "The Union Camerounaise was Ahidjo's party, formed in 1958.", "The UN did not ban the UPC."]),
        QUIZ("Who replaced Andre-Marie Mbida as head of government in February 1958?",
             ["Ruben Um Nyobe", "John Ngu Foncha", "Ahmadou Ahidjo", "Ernest Ouandie"], 2,
             "Ahidjo became Prime Minister in February 1958.",
             feedback=["Um Nyobe led the banned UPC and was killed in September 1958.", "Foncha led the KNDP in Southern Cameroons.",
                       "", "Ouandie was a UPC leader."]),
        H("Practice questions"),
        PQ("Give three reasons why the UPC lost the struggle for power by 1960.",
           "The 1955 ban removed it from legal politics; leaders were exiled or killed (Um Nyobe in 1958); the army and administration "
           "attacked the maquis; Ahidjo built a strong rival base; the UN accepted independence without new elections."),
        PQ("Essay plan: 'The UPC was defeated, but its demands were met.' Discuss with reference to independence and reunification.",
           "Independence came on the date and by a route that was close to the UPC demand; reunification of the two Cameroons was achieved "
           "in 1961, but not under UPC leadership or on UPC terms. Judgement: some demands were met by other hands."),
        PQ("Explain why historians disagree about the 1960 independence settlement.",
           "They give different weight to French influence, UPC repression and Ahidjo's local support, and they use different evidence: "
           "official reports, UN records, petitions, local testimony."),
        SUM("The UPC (1948) demanded reunification and independence; it was banned in July 1955.",
            "Armed conflict followed; Um Nyobe was killed in September 1958; fighting continued after 1960.",
            "Ahidjo replaced Mbida in February 1958 and led the state to independence on 1 January 1960.",
            "Historians use different evidence to judge the settlement: describe each view fairly."),
    ],
))

# ---------------------------------------------------------------------------
# 3. Southern Cameroons parties and constitutional steps
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Southern Cameroons politics",
    title="Southern Cameroons parties and constitutional steps, 1953 to 1959",
    slug="h7-sc-parties-and-constitutional-steps",
    minutes=22,
    summary=("How Southern Cameroons moved from the Eastern Region of Nigeria to its own assembly at Buea, and how the "
             "KNC, KNDP, KPP and One Kamerun differed on the future before the plebiscite."),
    objectives=[
        "Explain the 1953 break with the Eastern Region and the 1954 constitutional change",
        "Identify the main parties, their leaders and how their positions changed over time",
        "Describe the 1959 election and its importance for the plebiscite debate",
        "Use dated evidence to compare party positions without oversimplifying",
    ],
    key_concepts=["Eastern Region", "Quasi-federal status", "KNC", "KNDP", "KPP", "One Kamerun", "Premier"],
    blocks=[
        H("Introduction"),
        T("Think of a small region deciding how to be governed while two large neighbours, Nigeria and Cameroun, are "
          "heading towards independence. That was Southern Cameroons in the 1950s. Its politicians argued about "
          "several options, and their positions changed with events. For that reason, always date your claims about a party."),
        D("**Southern Cameroons** was the southern part of the British Cameroons. Before 1954 it was administered as part "
          "of the Eastern Region of Nigeria. A **quasi-federal** status gave it a separate House of Assembly at Buea "
          "and its own government, while still linked to Nigeria.", title="Southern Cameroons"),
        H("The break with the Eastern Region"),
        T("In 1953 a crisis in Eastern Nigerian politics led Southern Cameroons members of the regional House to leave "
          "the Enugu assembly. They said the Cameroons needed separate treatment. Britain agreed to constitutional "
          "change and the 1954 constitution gave Southern Cameroons its own House of Assembly at Buea."),
        T("Dr E. M. L. Endeley led the government in the new House as Leader of Government Business and later as Premier "
          "(1958, check your textbook). Further conferences on Nigeria's constitution held in London in the later 1950s, "
          "including at Lancaster House, widened the powers of the region."),
        H("The parties"),
        KEY("Parties and leaders", "Positions changed. Always attach a date.", cards=[
            ["KNC (Endeley)", "The Kamerun National Congress was led by Endeley. It won early elections and led the "
             "government. Over time it favoured a close link with Nigeria. Check your textbook for the party's founding date."],
            ["KPP (Kale)", "The Kamerun People's Party, led by P. M. Kale, was founded in the early 1950s. It cooperated "
             "with Endeley and later joined him to form the CPNC (about 1960, check your textbook)."],
            ["KNDP (Foncha)", "John Ngu Foncha left the KNC and founded the Kamerun National Democratic Party in 1955. "
             "It argued for separation from Nigeria and later for reunification with Cameroun."],
            ["One Kamerun (Ntumazah)", "Ndeh Ntumazah's party, founded in 1957, called for immediate reunification and "
             "independence and was close to the UPC."],
        ]),
        T("UPC leaders who had taken refuge in Southern Cameroons were expelled in 1957. This affected the reunification "
          "debate, because it linked reunification to the radical politics of French Cameroun."),
        H("The 1959 election"),
        T("In January 1959 elections to the Southern Cameroons House gave the KNDP a narrow majority of seats "
          "(check your textbook for the numbers) and Foncha became Premier. The election is often seen as a sign "
          "that many voters wanted to leave the Nigerian link. Historians remind us that a narrow seat majority "
          "does not show how voters felt about reunification itself."),
        EX("Model answer plan 1", intro="Why did Southern Cameroons obtain separate constitutional status in 1954?", steps=[
            S("Cause 1", text="The 1953 crisis in the Eastern Region led members to walk out of the Enugu House."),
            S("Cause 2", text="Southern Cameroons leaders argued that the Cameroons had a distinct history under trusteeship."),
            S("Response", text="Britain agreed to a separate House of Assembly at Buea under the 1954 constitution."),
            S("Judgement", text="The crisis was the trigger, and trusteeship status gave the argument legal weight."),
        ]),
        EX("Model answer plan 2", intro="Compare the aims of the KNC and the KNDP before 1959.", steps=[
            S("Similarity", text="Both wanted self-government for Southern Cameroons and both opposed domination by the Eastern Region."),
            S("Difference 1", text="The KNC moved towards close association with Nigeria; the KNDP moved towards secession from Nigeria."),
            S("Difference 2", text="The KNDP favoured eventual reunification with Cameroun, often imagined as a loose federation."),
            S("Judgement", text="Their disagreement over Nigeria became the main dividing line in the 1959 campaign."),
        ]),
        H("Source skill: comparing two party statements"),
        T("Two **illustrative statements invented for practice**. Statement A (a party leaflet): 'Our people must not be "
          "a minority in a big country. Let us govern ourselves first, then decide our friends.' Statement B (a rival "
          "leaflet): 'A small country cannot stand alone. Let us keep the ties that bring roads, schools and trade.' "
          "Compare them by purpose, audience and what they leave out."),
        T("Both are campaign leaflets, so both are persuasive and one-sided. A shows fear of domination; B shows "
          "fear of weakness. Neither gives figures. To judge them, a historian would look at election results, budgets and later events."),
        MISTAKE("Giving one fixed position for each party", "KNC and KNDP positions changed between 1953 and 1961. Use dates."),
        MISTAKE("Mixing the two Cameroons", "Southern Cameroons and French Cameroun had different parties, laws and administrations."),
        QUIZ("Where was the Southern Cameroons House of Assembly based after 1954?",
             ["Enugu", "Buea", "Mamfe", "Lagos"], 1,
             "The Southern Cameroons House of Assembly met at Buea.",
             feedback=["Enugu was the capital of the Eastern Region, which Southern Cameroons left.", "",
                       "The Mamfe conference was a meeting in 1959, not the seat of government.", "Lagos was the federal capital of Nigeria."]),
        QUIZ("Which leader founded the KNDP in 1955?",
             ["E. M. L. Endeley", "John Ngu Foncha", "Ndeh Ntumazah", "P. M. Kale"], 1,
             "Foncha founded the KNDP after leaving the KNC.",
             feedback=["Endeley led the KNC.", "", "Ntumazah led One Kamerun.", "Kale led the KPP."]),
        H("Practice questions"),
        PQ("Explain two reasons why Southern Cameroons leaders wanted a separate status from the Eastern Region.",
           "The 1953 crisis showed that Southern Cameroons interests were not safe inside the Eastern Region assembly; and the "
           "Cameroons were a trust territory with a separate legal status and history from Nigeria."),
        PQ("Describe the main difference between Endeley and Foncha in the later 1950s.",
           "Endeley (KNC, later CPNC) leaned towards association with Nigeria. Foncha (KNDP) favoured secession from Nigeria and "
           "then reunification with Cameroun."),
        PQ("Why is it unsafe to treat the January 1959 election result as a vote for reunification?",
           "The result was a narrow majority of seats, and voters may have chosen the KNDP for other reasons, such as dislike of "
           "Nigerian domination or the personalities of the leaders. Further evidence is needed."),
        PQ("Source question: how would you test the claim in an invented leaflet that 'a small country cannot stand alone'?",
           "Check the purpose (a campaign leaflet), then compare it with budgets, trade figures and what visiting missions "
           "reported about the region's resources. It is an opinion, not evidence of fact."),
        SUM("Southern Cameroons left the Eastern Region's assembly in 1953 and had its own House at Buea from 1954.",
            "KNC (Endeley), KNDP (Foncha, 1955), KPP (Kale) and One Kamerun (Ntumazah) differed on the future.",
            "The KNDP won a narrow majority in January 1959 and Foncha became Premier.",
            "Date every claim about party positions, because they changed."),
    ],
))

# ---------------------------------------------------------------------------
# 4. The 1961 plebiscite
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Southern Cameroons politics",
    title="Mamfe, the UN decisions and the 1961 plebiscites",
    slug="h7-sc-mamfe-un-decisions-plebiscites",
    minutes=23,
    summary=("How the UN set the plebiscite options after the Mamfe conference, what the Northern and Southern "
             "Cameroons chose in 1961, and how historians explain the choices and the absence of a third option."),
    objectives=[
        "Explain what happened at the Mamfe conference and why the UN took the decision",
        "State the options offered in the plebiscites and the main results",
        "Explain why Northern and Southern Cameroons chose differently",
        "Evaluate the arguments about whether a third option should have been offered",
    ],
    key_concepts=["Mamfe conference", "UN General Assembly", "Plebiscite", "Northern Cameroons", "Two-option ballot", "ICJ"],
    blocks=[
        H("Introduction"),
        T("A plebiscite looks simple: people vote and the result decides. But the options on the ballot, the date, "
          "the voters and the authority that organises it all shape the result. This lesson looks at those choices for the "
          "British Cameroons in 1959 to 1961, and at how historians argue about them."),
        D("A **plebiscite** is a vote of the people of a territory on a question about its future. In the British "
          "Cameroons the votes were held under the supervision of the United Nations in 1959 and 1961.", title="Plebiscite"),
        H("The Mamfe conference"),
        T("At Mamfe in August 1959, Southern Cameroons leaders tried to agree on the questions to put to the people and on "
          "who should vote. They did not agree. The matter then went to the United Nations General Assembly, "
          "which decided the options and the timetable in 1959 and again in 1960 and 1961 (check your textbook for the "
          "numbers of the resolutions)."),
        H("What the UN decided"),
        T("The UN set two alternatives for the Southern Cameroons: to achieve independence by joining the independent "
          "Federation of Nigeria, or to achieve independence by joining the independent Republic of Cameroun. "
          "Separate independence was not on the ballot. The Northern Cameroons voted on a similar choice, "
          "after an earlier poll in 1959 had deferred the decision."),
        IMG("al-h7-cameroon-timeline-1945-1961.svg",
            alt="Timeline showing the plebiscite in February 1961 and the start of the Federal Republic in October 1961",
            caption="Figure 1. The plebiscite year in the wider timeline (not to scale)."),
        H("The results"),
        KEY("What the two parts chose", "Learn the result and the date of union for each.", cards=[
            ["Southern Cameroons", "Voted in February 1961 to join the Republic of Cameroun by a clear majority, about "
             "seven votes in ten (check your textbook for the exact figures). It became part of the Federal Republic on 1 October 1961."],
            ["Northern Cameroons", "Voted to join Nigeria and became part of the Northern Region on 1 June 1961. "
             "Cameroun challenged the result at the UN and at the International Court of Justice, which in 1963 decided it could not rule on the case."],
        ]),
        H("Why did the two parts choose differently?"),
        T("Historians point to several factors. In the south the KNDP campaign, dislike of Nigerian domination, and "
          "memory of the shared German Kamerun past favoured Cameroun. In the north, links of religion, trade and "
          "administration with the Nigerian Northern Region, and local rulers' views, favoured Nigeria. These are explanations, "
          "not proofs. Votes show the final choice, not each voter's reasons."),
        H("Was a third option needed?"),
        KEY("Arguments about the ballot", "Present each side with its evidence.", cards=[
            ["For a separate-independence option", "Some Southern Cameroons leaders and later writers argue that "
             "people should have been able to choose independence for the territory, as other trust territories did. They point to "
             "the principle of self-determination in the Charter."],
            ["Against a separate-independence option", "Others point to the size, the budget and the "
             "judgement reported at the time that the territory could not survive alone. The UN General Assembly accepted "
             "the two-option plan."],
            ["A cautious view", "Historians note that we cannot know how voters would have chosen with three options. "
             "The question is a counterfactual, so it cannot be settled by documents alone."],
        ]),
        EX("Model answer plan 1", intro="Explain why Southern Cameroons voted to join the Republic of Cameroun in 1961.", steps=[
            S("Factor 1", text="Dislike of domination by Nigeria, remembered from the Eastern Region years."),
            S("Factor 2", text="KNDP organisation and Foncha's leadership after the 1959 election."),
            S("Factor 3", text="The idea of reunification, with a shared German colonial past."),
            S("Qualification", text="The ballot had only two choices, so some votes may have been against Nigeria rather than for Cameroun."),
        ]),
        EX("Model answer plan 2", intro="How far was the UN responsible for the outcome of the plebiscite?", steps=[
            S("For", text="The UN set the options, the timetable and supervision, and the two-option ballot framed the choice."),
            S("Against", text="The voters decided, and the main parties campaigned for their positions."),
            S("Evidence", text="Mamfe failed to agree, so the UN decided; the result was clear in the south."),
            S("Judgement", text="The UN shaped the choices, and the voters made the choice. Responsibility is shared."),
        ]),
        MISTAKE("Saying the whole British Cameroons joined Cameroun", "Only the south did. The north joined Nigeria in June 1961."),
        MISTAKE("Writing that voters chose independence", "The ballot asked them to achieve independence by joining one of two states."),
        MISTAKE("Quoting percentages without a source", "Say 'about seven in ten' and check the figures in your textbook."),
        QUIZ("Which two alternatives were put to Southern Cameroons voters?",
             ["Independence alone or union with Nigeria", "Union with Nigeria or union with the Republic of Cameroun",
              "Continued British rule or independence", "Union with Cameroun or union with Gabon"], 1,
             "The two options were joining Nigeria or joining the Republic of Cameroun.",
             feedback=["Independence alone was not offered.", "", "Continued trusteeship was not offered.", "Gabon was not an option."]),
        QUIZ("What did Northern Cameroons decide in the plebiscite of 1961?",
             ["To join the Republic of Cameroun", "To become a separate state", "To join Nigeria", "To stay under British rule"], 2,
             "It voted to join Nigeria, becoming part of it on 1 June 1961.",
             feedback=["That was the choice of the Southern Cameroons.", "No separate-state option was offered.", "",
                       "Trusteeship was ending in 1961."]),
        H("Practice questions"),
        PQ("State what happened at the Mamfe conference in August 1959 and why it mattered.",
           "Southern Cameroons leaders failed to agree on the plebiscite questions and the voters. As a result the UN decided the "
           "options, so the final choice of alternatives was set outside the Southern Cameroons assembly."),
        PQ("Explain why the north and the south of the British Cameroons voted differently.",
           "Northern links with the Northern Region of Nigeria, in religion, trade and administration, favoured Nigeria. In the south, "
           "KNDP campaigning, dislike of Nigerian domination and ideas of reunification favoured Cameroun."),
        PQ("Give one argument for and one argument against offering a separate-independence option.",
           "For: the Charter's principle of self-determination. Against: reported doubts about the territory's economic viability "
           "and the UN's judgement that two options were realistic."),
        PQ("Why can historians not say how a three-option ballot would have turned out?",
           "It is a counterfactual. No such vote took place, so evidence is limited to opinions at the time, which can be read in different ways."),
        SUM("Mamfe (August 1959) failed to agree, so the UN fixed the plebiscite options.",
            "Only two options were offered: join Nigeria or join the Republic of Cameroun.",
            "Northern Cameroons joined Nigeria (June 1961); Southern Cameroons voted for Cameroun (October 1961 union).",
            "Whether a third option was needed is debated; present both sides and the limits of the evidence."),
    ],
))

# ---------------------------------------------------------------------------
# 5. Foumban: sources and interpretations
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Southern Cameroons politics",
    title="Foumban and the federation: reading the sources and the interpretations",
    slug="h7-sc-foumban-sources-interpretations",
    minutes=24,
    summary=("The Foumban conference of July 1961 and the Federal Republic of 1 October 1961, studied through the types of "
             "source historians use and the competing interpretations of what was agreed."),
    objectives=[
        "Describe the sequence from the plebiscite to the Federal Republic",
        "Outline the main features of the 1961 federal constitution",
        "Evaluate sources on Foumban for provenance, purpose and limits",
        "Present the competing interpretations and the evidence for each",
    ],
    key_concepts=["Foumban", "Federal constitution", "West Cameroon", "Provenance", "Interpretation", "Article 47"],
    blocks=[
        H("Introduction"),
        T("Foumban is often discussed as if everyone already knows what happened there. In fact historians "
          "disagree on important points. This lesson separates what is well documented from what is interpreted, and "
          "shows how to weigh different kinds of sources."),
        D("The **Foumban conference** was a meeting of representatives of the Republic of Cameroun and Southern Cameroons "
          "held in July 1961 (check your textbook for the exact days) to discuss the form of the union. "
          "The Federal Republic of Cameroon began on 1 October 1961.", title="Foumban"),
        H("The sequence"),
        T("After the February 1961 plebiscite the UN endorsed the result. Southern Cameroons leaders prepared their "
          "position, including at an all-party conference in Bamenda in June 1961 (check your textbook for details). "
          "Delegations then met at Foumban in July. A federal constitution was drawn up and the Federal Republic "
          "came into existence on 1 October 1961."),
        H("The 1961 constitution in outline"),
        KEY("Main features (check your textbook for articles)", "Describe them rather than judge them.", cards=[
            ["Structure", "A federation of East Cameroon and West Cameroon, each with its own government and assembly, "
             "and a federal government with powers over matters such as defence and foreign affairs."],
            ["Offices", "A Federal President (Ahidjo) and a Vice-President from West Cameroon (Foncha). "
             "West Cameroon kept its own Prime Minister, House of Assembly and House of Chiefs."],
            ["Language and law", "English and French were official languages. West Cameroon kept its common-law system, "
             "while East Cameroon kept civil law."],
        ]),
        T("A provision on revision of the constitution is often discussed. It set conditions for amending the "
          "constitution and, according to many readers, protected the existence of the federal form. The exact wording and "
          "the way it was later applied are debated, so check your textbook for Article 47 and for the revision procedure."),
        H("Types of source"),
        KEY("Source types for Foumban", "Different sources answer different questions.", cards=[
            ["Official texts", "The constitution, decrees and communiques show what was formally adopted. They do not show how "
             "the talks went or who was persuaded."],
            ["Memoirs and interviews", "Delegates' later accounts give inside detail. They can be selective and shaped by later "
             "events and by self-defence."],
            ["Press and diplomatic reports", "Contemporary and sometimes well informed, but written for newspapers or "
             "governments with their own aims."],
        ]),
        H("Practice with three illustrative sources"),
        T("These three sources are **invented for practice**; they are not real quotations."),
        T("Source A (invented official communique): 'The two delegations met in a spirit of friendship and agreed "
          "on the principles of a federal state, which will be set out in a constitution.'", title="Source A"),
        T("Source B (invented memoir by a delegate, written many years later): 'We had little time. The text was "
          "already prepared and we did our best to make changes in the time we had.'", title="Source B"),
        T("Source C (invented newspaper comment from 1961): 'The union will bring two peoples together, but its "
          "success depends on how the federation is worked in practice.'", title="Source C"),
        EX("Source evaluation: how useful is each source?", intro="Judge the usefulness of Sources A, B and C above for a study of Foumban.", steps=[
            S("Source A", text="Official and public, so it shows the formal story the authorities wanted. It says nothing about disagreements or who drafted the text."),
            S("Source B", text="Inside knowledge but written years later, so memory and later events may shape it. It supports the view that time and preparation were limited, but it is one voice."),
            S("Source C", text="Contemporary and cautious. It shows how an observer saw the future, but not what happened in the room."),
            S("Combined", text="Together they suggest an agreed formal outcome (A), with concerns about process (B) and an open future (C). Further sources are needed to decide."),
        ]),
        H("Interpretations"),
        KEY("Three readings of Foumban", "Each has evidence and limits.", cards=[
            ["An imposed-settlement reading", "Some writers say the draft came from the Cameroun side, the Southern team had little "
             "time, and few amendments were accepted. Evidence: memoirs and the shape of the final text. Limit: the "
             "Southern delegates took part and agreed to the outcome."],
            ["A negotiated-settlement reading", "Others say the talks produced a real federation with West Cameroon institutions "
             "and offices, as promised in the plebiscite campaign. Evidence: the constitution's text. Limit: how the safeguards worked in practice."],
            ["An unequal-partners reading", "Many historians stress the difference of status: Cameroun was independent; Southern "
             "Cameroons was a trust territory facing a deadline. Evidence: the timetable of 1961. Limit: it does not by itself decide whether the final text was fair."],
        ], note="The question whether and how the Southern Cameroons House approved the final text is debated: check your textbook."),
        EX("Model answer plan", intro="'Foumban created a partnership of equals.' How far do you agree?", steps=[
            S("For", text="A federal structure with separate West Cameroon institutions, a Vice-President from West Cameroon and official bilingualism."),
            S("Against", text="Important powers were federal; Cameroun was a sovereign state and the other side a trust territory; the timetable was short."),
            S("Evidence", text="The constitution's text; memoirs; the timetable of 1961."),
            S("Judgement", text="Formal equality in structure, unequal bargaining position. Many historians give weight to both."),
        ]),
        MISTAKE("Describing Foumban as settled history", "State the interpretation and its evidence. Do not claim that all historians agree."),
        MISTAKE("Using a later memoir as if it were a record made on the day", "Mention when it was written and what it might leave out."),
        QUIZ("In which year did the Federal Republic of Cameroon begin?",
             ["1960", "1961", "1972", "1984"], 1,
             "The Federal Republic began on 1 October 1961.",
             feedback=["1960 was the independence of the Republic of Cameroun.", "", "1972 was the year of the unitary state.",
                       "1984 was the year the state was renamed the Republic of Cameroon."]),
        QUIZ("Why is a delegate's memoir written thirty years later a limited source?",
             ["Because it is always false", "Because memory and later events may shape it", "Because memoirs cannot be used in history",
              "Because it is written in a second language"], 1,
             "Memoirs can give inside detail, but memory and later events may shape what is remembered.",
             feedback=["Not always false. It must be checked against other sources.", "",
                       "Historians do use memoirs, with care.", "Language is not the main problem."]),
        H("Practice questions"),
        PQ("Describe two features of the 1961 federal constitution.",
           "A federation of East Cameroon and West Cameroon with their own governments; official languages English and French; "
           "a Federal President and a Vice-President from West Cameroon. Any two correctly stated features."),
        PQ("Explain why historians disagree about Foumban.",
           "Sources are limited (official texts, later memoirs). Historians give different weight to the equality of "
           "the structure and the inequality of the parties' position, and to the speed of the process."),
        PQ("Source question: how would you check the claim in invented Source B that the text was 'already prepared'?",
           "Compare it with other delegates' accounts, with the surviving drafts and with press reports from July 1961. Note the "
           "memoir's date and the author's possible motives."),
        PQ("Essay plan: 'The Federal Republic of 1961 was a fair outcome of the plebiscite.' Discuss.",
           "For: the structure and offices, the plebiscite result, the federal form promised. Against: unequal status, short time and "
           "the later fate of the safeguards. Judgement: weigh the formal fairness against the practical balance of power, and say that views differ."),
        SUM("After the plebiscite, Foumban (July 1961) led to the Federal Republic of 1 October 1961.",
            "The constitution gave two federated states, bilingualism and a Vice-President from West Cameroon.",
            "Official texts, memoirs and press reports each answer different questions; check date and purpose.",
            "Interpretations differ: imposed, negotiated or unequal partners. Use evidence for each."),
    ],
))

# ---------------------------------------------------------------------------
# 6. From federation to the unitary state
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="The post-colonial state",
    title="From federation to the unitary state, 1961 to 1972",
    slug="h7-pcs-federation-to-unitary-state",
    minutes=22,
    summary=("How the federal structure of 1961 worked, how the single party of 1966 changed politics, and the "
             "referendum of 20 May 1972 that created the United Republic, with the arguments and evidence on both sides."),
    objectives=[
        "Describe how the 1961 federation divided powers between the centre and the two states",
        "Explain the formation of the CNU in 1966 and its political effects",
        "Describe the 1972 referendum and the new constitution",
        "Present the arguments for and against the move to a unitary state, with evidence",
    ],
    key_concepts=["Federation", "Unitary state", "CNU", "Referendum", "United Republic", "Centralization"],
    blocks=[
        H("Introduction"),
        T("When you pay a tax, who collects it, a state government or a national one? In a federation both levels have a "
          "role. The 1961 constitution joined East Cameroon and West Cameroon in a federation. In 1972 a referendum replaced "
          "it with a unitary state. This lesson describes the steps and the arguments, and leaves you to weigh the evidence."),
        D("In a **federation** powers are divided by the constitution between a federal government and federated states. "
          "In a **unitary state** the central government holds sovereignty and may delegate powers to local bodies.",
          title="Federal and unitary"),
        IMG("al-h7-cameroon-state-changes.svg",
            alt="Timeline of the Cameroonian state from the federation of 1961 to the constitution of 1996",
            caption="Figure 1. Main constitutional and party changes (not to scale)."),
        H("How the federation worked"),
        T("The 1961 constitution gave the federal government important powers, such as defence, foreign affairs and "
          "much of finance. East and West Cameroon kept their own governments, assemblies and many local matters. "
          "The Federal President was Ahidjo and the Vice-President came from West Cameroon. Over the 1960s "
          "federal institutions and officials had an increasing role in both states (check your textbook for "
          "federal inspectors and the budget arrangements)."),
        H("The single party, 1966"),
        T("In September 1966 the main parties of the two states, including the Union Camerounaise and the KNDP, joined "
          "in a new party, the Cameroon National Union (CNU). Parties that did not join were not able to operate "
          "(check your textbook for how and when other parties ended). Cameroon became a one-party state."),
        KEY("Reading the single party", "Both views existed at the time and later.", cards=[
            ["The official case", "A single party would end ethnic and regional rivalry, speed development and "
             "build one nation after the conflicts of the early 1960s."],
            ["The critical case", "It ended open competition, made it harder for West Cameroon to defend its "
             "separate institutions and concentrated power around the President."],
        ]),
        H("The referendum of 20 May 1972"),
        T("In 1972 President Ahidjo proposed a new constitution creating one state, the United Republic of Cameroon. "
          "A referendum on 20 May 1972 approved it. The federated states and the Vice-President's office were abolished. "
          "20 May became the National Day. The official result was an overwhelming vote in favour, and later critics "
          "question the conditions in which the vote took place."),
        KEY("Arguments about 1972", "Present them fairly.", cards=[
            ["Arguments for the change", "Unity: one government, one national identity. Cost: two sets of "
             "institutions were expensive for a poor country. Popular approval: the referendum result."],
            ["Arguments against", "Guarantees of the 1961 federal form were removed; the revision procedure of the 1961 constitution "
             "was set aside in favour of a referendum; West Cameroon institutions were weakened. Check your textbook for the revision article."],
            ["Points historians raise", "The one-party setting meant no organised campaign against the change. The "
             "official result is hard to read as a measure of opinion."],
        ]),
        EX("Model answer plan 1", intro="Why did Cameroon become a unitary state in 1972?", steps=[
            S("Factor 1: the design of the 1961 federation", text="Key powers were federal from the start."),
            S("Factor 2: the single party", text="The CNU (1966) centralised political life."),
            S("Factor 3: the stated aims", text="National unity and economic development, with lower cost."),
            S("Factor 4: Ahidjo's leadership", text="He proposed the change and controlled the process."),
            S("Judgement", text="Centralising politics from 1961 to 1966 made a unitary state likely. The referendum gave it legal form."),
        ]),
        EX("Model answer plan 2", intro="'The referendum of 1972 expressed the will of the people.' Discuss.", steps=[
            S("For", text="A very high yes vote was recorded and supporters said it showed national unity."),
            S("Against", text="Critics note the single-party setting, no organised opposition and doubts about the procedure."),
            S("Evidence", text="Official results; the CNU's control; the 1961 revision rules (check your textbook)."),
            S("Judgement", text="The vote was formally valid under the new order, but its value as a free measure of opinion is contested."),
        ]),
        H("Source skill: an official statement"),
        T("Illustrative source (invented for practice): 'Two governments for one people are too heavy. One "
          "nation must have one state.' (A speech by a government official.)", title="Illustrative source"),
        T("Provenance: an official speaking for the government. Purpose: to persuade. Content: gives a cost argument and a "
          "unity argument, but no figures. It shows how the change was justified. It does not show how people felt."),
        MISTAKE("Mixing up 1961, 1972 and 1984", "1961 Federal Republic; 1972 United Republic; 1984 Republic of Cameroon."),
        MISTAKE("Giving the 1972 vote as proof of agreement or of fraud", "Give the official result, then discuss its limits."),
        QUIZ("What was abolished by the 20 May 1972 referendum?",
             ["The CNU", "The federal structure", "The UN trusteeship", "The 1996 constitution"], 1,
             "The referendum approved a unitary state, so the federated states were abolished.",
             feedback=["The CNU continued until 1985.", "", "Trusteeship ended in 1960 and 1961.", "The 1996 constitution came later."]),
        QUIZ("Which party formed in September 1966 by merging the main parties of both states?",
             ["SDF", "CPDM", "CNU", "UPC"], 2,
             "The Cameroon National Union was formed in September 1966.",
             feedback=["The SDF was launched in 1990.", "The CPDM was the CNU's new name from 1985.", "", "The UPC was banned in 1955."]),
        H("Practice questions"),
        PQ("State two ways in which power was shared in the 1961 federation.",
           "Federal government in charge of defence and foreign affairs (and more); East and West Cameroon had their own governments and "
           "assemblies; a Vice-President from West Cameroon."),
        PQ("Explain two effects of the formation of the CNU in 1966.",
           "It ended organised party competition, making Cameroon a one-party state; it reduced the independent political base of "
           "the two federated states, making centralisation easier."),
        PQ("Give one argument for and one argument against the creation of a unitary state in 1972.",
           "For: unity and lower cost. Against: the loss of the federal guarantees and of West Cameroon institutions, and doubts about the procedure."),
        PQ("Source question: what is the value and the limit of an official speech that explains the case for a unitary state?",
           "It shows the government's reasons and how it persuaded people. It is one-sided and gives no figures or opposing voices."),
        SUM("The 1961 federation divided powers between a federal government and two federated states.",
            "In September 1966 the CNU made Cameroon a one-party state.",
            "A referendum on 20 May 1972 created the unitary United Republic of Cameroon.",
            "Supporters stress unity and cost; critics stress the loss of federal guarantees. Weigh both with evidence."),
    ],
))

# ---------------------------------------------------------------------------
# 7. Single party, transition and liberalization
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="The post-colonial state",
    title="One-party rule, the 1982 transition and liberalization, 1972 to 1992",
    slug="h7-pcs-one-party-transition-liberalization",
    minutes=24,
    summary=("From the unitary state of 1972 to the multiparty elections of 1992: the 1982 transition from Ahidjo to Biya, the "
             "CPDM of 1985, the economic crisis and the 1990 laws."),
    objectives=[
        "Describe the 1982 transition and the crisis of 1983 to 1984",
        "Explain the change from CNU to CPDM in 1985",
        "Explain internal and external causes of the political opening of 1990",
        "Evaluate how far the early 1990s changed Cameroonian politics",
    ],
    key_concepts=["1982 transition", "CPDM", "Economic crisis", "SDF", "Villes mortes", "Multiparty politics"],
    blocks=[
        H("Introduction"),
        T("Political change often comes when the economy fails and leaders cannot pay for their promises. In Cameroon "
          "the end of Ahidjo's presidency in 1982 and the opening of 1990 both happened in that wider setting. This lesson "
          "describes what happened and the causes historians give, and keeps to events and documents."),
        D("A **transition** is a change of the person or system that holds power. In 1982 it was a change of "
          "President under the constitution. **Liberalization** is the loosening of political controls, such as allowing "
          "parties, a freer press and open elections.", title="Transition and liberalization"),
        H("The 1982 transition"),
        T("Ahmadou Ahidjo resigned as President in November 1982. Paul Biya, who had been Prime Minister since "
          "1975, became President under the constitutional rule of succession. Ahidjo stayed as head of the party for a time, "
          "and tension between the two men grew. In 1983 Ahidjo left the country."),
        T("In April 1984 an attempted coup in Yaounde failed. The events of 1983 and 1984, including trials "
          "(check your textbook for details), ended the period of shared authority. In 1984 the state's name became the "
          "Republic of Cameroon, and in 1985 the CNU became the Cameroon People's Democratic Movement (CPDM)."),
        KEY("Continuity or change?", "Interpretations differ about 1982 and 1985.", cards=[
            ["Emphasis on continuity", "The one-party system, the powerful presidency and the unitary state "
             "remained. The new name did not change how power worked."],
            ["Emphasis on change", "A new President built his own base and policies, new party language of renewal and "
             "'rigour and moralization' was used (check your textbook for the slogans), and new people came to power."],
        ]),
        H("The economic crisis"),
        T("From the mid-1980s, falling prices for main exports and borrowing pressures cut state revenue. Public "
          "salaries were reduced and structural adjustment programmes followed (check your textbook for dates). "
          "Many urban people, civil servants and students suffered, and criticism of the government grew."),
        H("The opening of 1990"),
        T("The Social Democratic Front (SDF), led by John Fru Ndi, was launched in Bamenda on 26 May 1990. Several "
          "people died when security forces confronted the crowd. In December 1990 laws were passed allowing freedom of "
          "association and multiple parties (check your textbook for the numbers of the laws)."),
        T("In 1991 opposition parties organised 'ghost town' (villes mortes) campaigns and demanded a national conference. "
          "The government held a tripartite meeting instead, and agreed to constitutional discussions and elections. "
          "Legislative elections followed in 1992 and a presidential election in October 1992. Biya was declared "
          "the winner, and the opposition disputed the result."),
        KEY("Why did liberalization happen?", "Name internal and external causes.", cards=[
            ["External causes", "The end of the Cold War, the fall of one-party regimes elsewhere in Africa and "
             "demands from donors and foreign governments for reform."],
            ["Internal causes", "The economic crisis, the SDF launch, students, lawyers, churches and the press, and the villes mortes campaigns."],
            ["The government's choices", "The ruling party used legal change to control the pace, and no sovereign national conference was held."],
        ]),
        EX("Model answer plan 1", intro="How far did the 1982 transition change the Cameroonian state?", steps=[
            S("Change", text="A new President, a breach with Ahidjo, new party name in 1985."),
            S("Continuity", text="Single party, strong presidency and the unitary state continued until 1990."),
            S("Evidence", text="The 1983 to 1984 crisis; the 1984 coup attempt; the 1985 Bamenda congress."),
            S("Judgement", text="Large change at the top, limited change in the system before the 1990s."),
        ]),
        EX("Model answer plan 2", intro="Assess the causes of political liberalization in Cameroon in the early 1990s.", steps=[
            S("Argument: economic crisis", text="Falling revenue weakened the government's ability to reward supporters."),
            S("Argument: external pressure", text="The end of the Cold War and donor demands."),
            S("Argument: popular mobilization", text="SDF launch in 1990, villes mortes in 1991, students and the press."),
            S("Counter-argument", text="The government controlled the process; the ruling party stayed in power."),
            S("Judgement", text="Economic crisis and pressure created the opening; the government managed the result. Change was real but limited."),
        ]),
        H("Source skill: a newspaper report"),
        T("Illustrative source (invented for practice): 'Thousands gathered in the town for the launch. The "
          "authorities had refused permission, and the evening ended in confusion and loss of life.' (A foreign press report.)",
          title="Illustrative source"),
        T("Provenance: an outside observer, probably writing quickly. Content: states a refusal of permission "
          "and loss of life but gives no numbers or causes. Use: supports the claim that the launch was contested. "
          "Cross-check with the government's account, party accounts and later inquiries."),
        MISTAKE("Dating the CPDM to 1966", "The CNU was formed in 1966 and renamed the CPDM in 1985."),
        MISTAKE("Using only one cause", "Examiners expect internal and external causes of 1990, with a judgement on which mattered more."),
        QUIZ("In which year did the CNU become the CPDM?",
             ["1966", "1972", "1985", "1992"], 2,
             "The change of name took place at the Bamenda congress in 1985.",
             feedback=["1966 is when the CNU was formed.", "1972 is the unitary state referendum.", "", "1992 saw multiparty elections."]),
        QUIZ("Which was an external cause of the political opening of 1990?",
             ["The villes mortes campaigns", "The end of the Cold War and pressure from donors", "The launch of the SDF in Bamenda",
              "Economic crisis inside Cameroon"], 1,
             "External causes come from outside the country, such as the end of the Cold War and donor pressure.",
             feedback=["Villes mortes were organised inside the country.", "", "The SDF was a Cameroonian party.", "The crisis was mainly a domestic cause, though linked to world prices."]),
        H("Practice questions"),
        PQ("Describe the main events of the 1982 to 1985 period.",
           "Ahidjo resigned in November 1982 and Biya succeeded him; tension and Ahidjo's departure in 1983; failed coup of April 1984; "
           "the 1984 renaming and the CNU becoming the CPDM in 1985."),
        PQ("Explain two internal causes of liberalization in 1990.",
           "Economic crisis and falling state revenue; mobilization by the SDF, students, the press and others, including the villes mortes."),
        PQ("How far had politics changed by the end of 1992? Give two points on each side.",
           "Changed: multiparty elections, many parties, a freer press. Continuity: the same ruling party stayed in power, and the 1992 "
           "presidential result was disputed. Judgement: real change that was limited."),
        PQ("Source question: how reliable is a foreign press report of the SDF launch?",
           "It is an outside view, written quickly, which may lack local knowledge. It can be checked against the government and "
           "party accounts and later inquiries."),
        SUM("Biya succeeded Ahidjo in 1982; the crisis of 1983 to 1984 led to the CPDM in 1985.",
            "Economic crisis and external pressure created the opening of 1990.",
            "The SDF was launched in May 1990; party laws followed in December 1990.",
            "Villes mortes and a tripartite meeting led to the 1992 elections, whose results were disputed."),
    ],
))

# ---------------------------------------------------------------------------
# 8. The 1996 constitution and the historiography
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="The post-colonial state",
    title="The 1996 constitution and the debate on the Anglophone question: historiography",
    slug="h7-pcs-1996-constitution-historiography",
    minutes=24,
    summary=("The Buea and Bamenda conferences of 1993 and 1994, the 1996 constitution, and the ways historians and "
             "commentators interpret federalism, decentralization and the Anglophone question, with the evidence each side uses."),
    objectives=[
        "Describe the Anglophone conferences of 1993 and 1994 and the 1996 constitution",
        "Outline the main positions in the debate and the evidence each uses",
        "Distinguish description, interpretation and opinion in historical writing",
        "Write a balanced paragraph on a contested question",
    ],
    key_concepts=["Anglophone conference", "1996 constitution", "Decentralization", "Historiography", "Interpretation", "Bias"],
    blocks=[
        H("Introduction"),
        T("Some questions in history are still part of public debate. The place of the English-speaking regions in "
          "Cameroon is one of them. This lesson does not take a side. It shows you how to describe the documents and events, "
          "how to present the main interpretations with their evidence, and how to keep your own writing fair."),
        D("**Historiography** is the study of how historians have written about a subject and why their interpretations differ.",
          title="Historiography"),
        H("Documents and events, 1993 to 1996"),
        T("In April 1993 the All Anglophone Conference met in Buea and issued a declaration asking for constitutional "
          "reform, including a return to federalism (check your textbook for the text and the aims). A second conference "
          "in Bamenda in 1994 issued a proclamation which set out a further position and a time limit for talks "
          "(check your textbook for the details)."),
        T("The constitution of 18 January 1996 kept a unitary state and described it as decentralized. It "
          "provides for regions, a Senate, a Constitutional Council and English and French as official languages. "
          "A seven-year presidential term is set. Several institutions were set up many years after 1996. "
          "A constitutional amendment of 2008 changed the rules on presidential terms."),
        IMG("al-h7-cameroon-state-changes.svg",
            alt="Timeline of the Cameroonian state from 1961 to the constitution of 1996",
            caption="Figure 1. The state's main changes, ending with the 1996 constitution (not to scale)."),
        H("The positions in the debate"),
        KEY("Four positions", "Each has a case and a limit. Describe them neutrally.", cards=[
            ["A unitary state with decentralization", "Supporters say it keeps national unity, avoids duplication and "
             "gives powers to elected regions. They point to the 1996 text and to the 1972 referendum. The debate "
             "is then about how fully decentralization is applied."],
            ["A return to federalism", "Supporters say the 1961 agreement set a federal form which was changed in 1972, and "
             "that a federation protects the English-speaking minority's institutions. They point to the 1961 constitution and the conferences of 1993 and 1994."],
            ["A claim about Southern Cameroons' status", "Some argue that the 1961 union was not completed by a "
             "formal agreement or that the territory kept a separate status. Others reject this and point to the UN "
             "decisions, the plebiscite and the Federal Republic. Both sides use legal and historical documents; the claim is disputed."],
            ["A reform-in-practice view", "Some scholars focus on practical grievances, such as law, schooling, "
             "language use in the administration and representation, and argue that these matter more than the "
             "name of the system. They use surveys, court records and administrative data."],
        ], note="Positions held by political groups after the 1990s are part of current debate: describe them and their evidence without taking a side."),
        T("The crisis that began in 2016 in the North-West and South-West regions is very recent and very sensitive. "
          "Use a reliable textbook, record only well-documented facts, and avoid adopting the vocabulary of any one party. "
          "This lesson does not cover those events."),
        H("Description, interpretation, opinion"),
        KEY("Three kinds of statement", "Learn to label them.", cards=[
            ["Description", "A checkable fact: 'The referendum was held on 20 May 1972.'"],
            ["Interpretation", "A reasoned reading of the facts: 'The referendum reflected the dominance of a single party.' It needs evidence and can be challenged."],
            ["Opinion", "A personal preference: 'The system should be federal.' It is not a historical argument unless it is tied to evidence."],
        ]),
        EX("Model answer plan", intro="Why do historians and commentators disagree about the change from federation to unitary state?", steps=[
            S("Different documents", text="Some stress the 1961 constitution and its revision rules; others stress the referendum of 1972."),
            S("Different weight on context", text="Some stress national unity and cost; others stress the loss of guarantees for West Cameroon."),
            S("Different evidence", text="Official results and speeches versus memoirs, party documents and legal analysis."),
            S("Judgement", text="The facts are mostly agreed; the disagreement is about what they mean. A fair answer shows both and says where the evidence is thin."),
        ]),
        EX("Writing a balanced paragraph", intro="Write a fair paragraph on whether the 1996 constitution answered the demands of the 1993 and 1994 conferences.", steps=[
            S("Describe", text="The conferences asked for a return to federalism; the 1996 text kept a unitary state but spoke of decentralization."),
            S("Give each view", text="Some see decentralization as a partial answer; others say it did not meet the demand for a federal form."),
            S("Give the evidence", text="The text of the constitution, the timing of the institutions that followed, and the conference documents."),
            S("Close carefully", text="The answer depends on what one counts as meeting the demand. Avoid words that praise or blame."),
        ]),
        H("Source skill: spotting loaded words"),
        T("Illustrative source (invented for practice): 'The government crushed every request for dialogue.' Compare "
          "with: 'The government did not accept the request for a federal form.' The first uses a charged verb. The second "
          "describes the same event neutrally. In your own writing, prefer the second kind of sentence, and give the date and the document."),
        MISTAKE("Taking a side in a current debate", "Describe each view and the evidence behind it, and let the reader weigh them."),
        MISTAKE("Treating an opinion as a fact", "Ask: could a document or a figure confirm or refute this sentence?"),
        QUIZ("The 1996 constitution described Cameroon as",
             ["A federal republic", "A decentralized unitary state", "A confederation", "A one-party state"], 1,
             "It kept a unitary state and described it as decentralized.",
             feedback=["The federal state ended in 1972.", "", "A confederation was not created.", "Multiparty politics had been allowed since 1990."]),
        QUIZ("Which of these is an interpretation, not a description?",
             ["The All Anglophone Conference met in Buea in April 1993", "The 1996 constitution provides for a Senate",
              "The 1972 referendum shows that the people accepted a unitary state", "The Federal Republic began on 1 October 1961"], 2,
             "The claim about what the referendum shows is a reading of the evidence that can be challenged.",
             feedback=["This is a checkable fact.", "This is a checkable fact about the text.", "", "This is a checkable date."]),
        H("Practice questions"),
        PQ("Describe two features of the 1996 constitution.",
           "A decentralized unitary state with regions; English and French as official languages; provision for a Senate and a "
           "Constitutional Council; a seven-year presidential term. Any two."),
        PQ("Outline two positions in the debate on the form of the state and the evidence each uses.",
           "Unitary state with decentralization: the 1996 text and 1972 referendum. Federalism: the 1961 constitution and the 1993 to 1994 "
           "conference documents. Each is presented without judgement."),
        PQ("Explain the difference between a description and an interpretation, with one example of each.",
           "A description is a checkable fact (the referendum was held on 20 May 1972). An interpretation is a reasoned reading "
           "that needs evidence (the vote showed the weight of the single party)."),
        PQ("Why should a historian avoid charged words when writing on a debated subject?",
           "They show a side and may close discussion. Neutral descriptions with dates and documents allow readers to judge the evidence."),
        SUM("The 1993 Buea and 1994 Bamenda conferences asked for constitutional change; the 1996 constitution kept a decentralized unitary state.",
            "Positions in the debate use legal texts, referendum results and conference documents; present each with its evidence.",
            "Separate description, interpretation and opinion; avoid charged words.",
            "Recent events are very sensitive: use reliable sources and well-documented facts only."),
    ],
))

# ---------------------------------------------------------------------------
# 9. Ghana and Nigeria
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="Constitutional transfers",
    title="British transfers of power: the Gold Coast and Nigeria",
    slug="h7-dec-british-transfers-ghana-nigeria",
    minutes=22,
    summary=("How the Gold Coast became Ghana in 1957 and Nigeria became independent in 1960: the stages of constitutional "
             "change, the leaders and parties, and the different problems of a unitary and a federal transfer."),
    objectives=[
        "Outline the stages by which the Gold Coast moved to independence in 1957",
        "Explain why Nigeria was given a federal constitution and how it reached independence in 1960",
        "Compare the two cases and say why British policy is described as gradual",
        "Evaluate the claim that these were peaceful transfers",
    ],
    key_concepts=["Constitutional decolonization", "CPP", "Positive Action", "Federalism", "Regions", "Self-government"],
    blocks=[
        H("Introduction"),
        T("If you wanted to hand over a house to the tenants, would you do it in one day or room by room? Britain chose "
          "the room-by-room method in West Africa. A series of constitutions gave Africans more seats and more power, until "
          "independence. Ghana and Nigeria show how this worked, and how it could go wrong."),
        D("**Constitutional decolonization** was the transfer of power through a series of constitutions, elections and "
          "conferences, ending in independence on agreed terms, rather than through a war of liberation.",
          title="Constitutional decolonization"),
        IMG("al-h7-decolonization-1957-1980.svg",
            alt="Timeline of independence dates: Ghana 1957, Guinea 1958, Nigeria 1960, Algeria 1962, Kenya 1963, Mozambique and Angola 1975, Zimbabwe 1980",
            caption="Figure 1. Independence dates in this topic (not to scale)."),
        H("The Gold Coast"),
        T("After the Second World War, grievances grew: ex-servicemen without jobs, high prices and anger among cocoa "
          "farmers. In February 1948 riots in Accra followed a protest march. A commission of inquiry and a committee of "
          "Africans (the Coussey Committee) recommended constitutional reform, and a new constitution followed in 1951."),
        T("Kwame Nkrumah left the United Gold Coast Convention and founded the Convention People's Party (CPP) in "
          "June 1949, with a demand for 'self-government now'. In January 1950 he called a campaign of 'positive "
          "action' (strikes and non-cooperation) and was jailed. In the 1951 election the CPP won most seats; "
          "Nkrumah was released to become Leader of Government Business."),
        T("Further elections in 1954 and 1956 confirmed the CPP's lead. The Gold Coast, together with British Togoland "
          "after a plebiscite in 1956, became independent as Ghana on 6 March 1957, with Nkrumah as Prime Minister."),
        H("Nigeria"),
        T("Nigeria was large and divided into three main regions: North, West and East. Constitutions of 1946 (Richards), "
          "1951 (Macpherson) and 1954 (Lyttelton) moved Nigeria towards a federation. Regional parties grew: the "
          "Northern People's Congress, the Action Group in the West and the NCNC in the East and in national politics."),
        T("Fears of domination by one region and the differences in political development between north and south "
          "made the British and many Nigerians favour a federal structure. The Eastern and Western Regions received "
          "self-government in 1957 and the Northern Region in 1959. Nigeria became independent on 1 October 1960, "
          "with Abubakar Tafawa Balewa as Prime Minister (check your textbook for the governor-general arrangement)."),
        KEY("Compare the two transfers", "Use these to structure an essay.", cards=[
            ["Ghana: a unitary route", "One dominant mass party, one leader, strong pressure from below (positive action), "
             "independence for the whole colony in 1957."],
            ["Nigeria: a federal route", "Three regions, three leading parties, slower negotiation among regions, and "
             "independence in 1960 within a federal system."],
            ["Common features", "Elections, conferences in London, African ministers before independence, and no war of liberation."],
        ]),
        T("Why did Britain agree to leave? Historians give several explanations: the pressure of nationalist movements, "
          "Britain's economic weakness after 1945, the cost of resisting in colonies where there was no large settler population, "
          "and a policy of ending colonial rule on British terms while keeping influence. Prime Minister Macmillan's "
          "'wind of change' speech in Cape Town (February 1960) is often cited as a sign of this realism."),
        EX("Model answer plan 1", intro="Why did the Gold Coast become independent in 1957?", steps=[
            S("Internal factors", text="Postwar grievances, the 1948 riots, the CPP's mass organisation and positive action."),
            S("External factors", text="Britain's weakness after 1945, world opinion and the example of India (1947)."),
            S("British policy", text="Constitutional reform after 1948 and the 1951 election, which made independence manageable."),
            S("Judgement", text="African nationalism set the pace, but Britain's choice not to fight a war made peaceful transfer possible."),
        ]),
        EX("Model answer plan 2", intro="'Nigeria's independence in 1960 was a success for British policy.' Discuss.", steps=[
            S("For", text="A peaceful transfer, a working federal constitution and a stable start."),
            S("Against", text="Regional rivalries and fears of domination remained; the first years brought strong tensions, "
              "including the military coups of 1966 and a civil war from 1967 (check your textbook)."),
            S("Evidence", text="The regional party system, the census disputes, the coups of 1966."),
            S("Judgement", text="Independence was peaceful, but the structure it left gave later problems. 'Success' depends on what one measures."),
        ]),
        MISTAKE("Calling the transfers 'handed over freely'", "African organisation and pressure were essential. Britain's choices set the form."),
        MISTAKE("Treating Ghana and Nigeria as identical", "Ghana was a unitary state under one party; Nigeria was a federation of three regions."),
        MISTAKE("Dating Ghana's independence to 1960", "Ghana was independent on 6 March 1957; Nigeria on 1 October 1960."),
        QUIZ("Which leader founded the CPP in 1949?",
             ["Nnamdi Azikiwe", "Kwame Nkrumah", "Obafemi Awolowo", "Ahmadu Bello"], 1,
             "Nkrumah founded the Convention People's Party in June 1949.",
             feedback=["Azikiwe led the NCNC in Nigeria.", "", "Awolowo led the Action Group in Nigeria.", "Bello was a leader of the Northern People's Congress."]),
        QUIZ("Why was a federal constitution chosen for Nigeria?",
             ["There was only one region", "Regional differences and fears of domination", "The USSR required it", "Because Ghana had one"], 1,
             "Differences between the regions and fears of domination by one of them pushed Nigeria towards federation.",
             feedback=["Nigeria had three main regions.", "", "The USSR had no say in Nigeria's constitution.", "Ghana had a unitary structure."]),
        H("Practice questions"),
        PQ("Describe two stages in the Gold Coast's move to independence.",
           "The 1948 riots and the Coussey reforms leading to the 1951 constitution and election; Nkrumah's CPP victory and "
           "government (1951 to 1957), ending with independence on 6 March 1957."),
        PQ("Explain why Nigeria adopted a federal system.",
           "The size and regional differences of Nigeria, regional parties, and fear that one region would dominate. A federation gave each region its own powers."),
        PQ("Compare the routes to independence of Ghana and Nigeria in two respects.",
           "Ghana: one mass party and a unitary state; Nigeria: three regional parties and a federation. Both: elections, conferences "
           "and no war of liberation."),
        PQ("How far was the transfer of power in Ghana a peaceful one? Give evidence on each side.",
           "Peaceful: no war, negotiated constitutions, election-led transition. Not wholly peaceful: riots in 1948 and the strikes of positive "
           "action, with leaders jailed. Judgement: mostly non-violent but not free of conflict."),
        SUM("The Gold Coast moved by constitutions (1951 election) to independence as Ghana on 6 March 1957 under Nkrumah.",
            "Nigeria followed a federal route and became independent on 1 October 1960.",
            "British policy was gradual and constitutional, but African pressure set the pace.",
            "Peaceful transfers still left problems, including regional rivalry in Nigeria."),
    ],
))

# ---------------------------------------------------------------------------
# 10. French Loi-Cadre and Guinea
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="Constitutional transfers",
    title="French Africa: the Loi-Cadre, the 1958 referendum and Guinea's No",
    slug="h7-dec-french-loi-cadre-guinea-1958",
    minutes=22,
    summary=("French decolonization from the Brazzaville Conference to the independence of 1960: the French Union, the Loi-Cadre "
             "of 1956, the referendum of 1958, Guinea's choice and the wave of independence in 1960."),
    objectives=[
        "Outline French policy from Brazzaville (1944) to the Loi-Cadre (1956)",
        "Explain the options offered by the referendum of 28 September 1958",
        "Explain why Guinea voted No and what France did in response",
        "Compare the French route with the British one",
    ],
    key_concepts=["French Union", "Loi-Cadre", "French Community", "Referendum of 1958", "Sekou Toure", "Assimilation"],
    blocks=[
        H("Introduction"),
        T("In September 1958 the people of French West Africa and Equatorial Africa were asked a single question in a "
          "referendum: Yes to a new constitution and the French Community, or No. Only one territory voted No, and "
          "its independence was immediate. This lesson explains why the question was framed in that way, and what happened next."),
        D("The **Loi-Cadre** (framework law) of June 1956, associated with minister Gaston Defferre, gave each territory an "
          "elected assembly and a government council with African ministers, and extended the vote. It left key powers, such as defence "
          "and foreign policy, to France.", title="Loi-Cadre"),
        H("From Brazzaville to the Loi-Cadre"),
        T("At the Brazzaville Conference of 1944, Free French leaders promised reforms but ruled out independence. "
          "The 1946 constitution created the French Union, with African representation in the French parliament. African "
          "politicians such as Felix Houphouet-Boigny worked in Paris, and the RDA, founded in 1946 at Bamako, became the main inter-territorial party."),
        T("By the mid-1950s the war in Indochina was over and the Algerian war had begun. The Loi-Cadre of 1956 was a "
          "response: it gave local governments real roles, but it also divided the large federations of French West Africa "
          "and French Equatorial Africa into smaller territories (a point critics noticed, as it weakened unity)."),
        H("The referendum of 1958"),
        T("After the crisis of 1958 in France, General de Gaulle returned to power and offered a new constitution for "
          "the Fifth Republic. Overseas territories voted on 28 September 1958. A Yes would make them autonomous members of the "
          "French Community, with France controlling foreign policy, defence and some other matters. A No would mean immediate "
          "independence without French aid."),
        T("Every territory except Guinea voted Yes. Guinea, led by Sekou Toure, voted No by a very large majority. Guinea became "
          "independent on 2 October 1958. France withdrew its administrators and aid quickly, and Guinea turned for support to other "
          "states, including the Soviet bloc and Ghana (check your textbook for the details)."),
        KEY("Why did the others vote Yes, and Guinea No?", "Explain with reasons, not just results.", cards=[
            ["Reasons for Yes", "Fear of losing aid and expertise; trust in leaders such as Houphouet-Boigny; the expectation that "
             "the Community could develop into more freedom; local political rivalries."],
            ["Reasons for No in Guinea", "A strong party (the PDG) and trade union organisation, "
             "a leader committed to independence, and a view that the Community kept real power in France."],
        ], note="Historians also note that the Community soon changed, as the 1960 independences showed."),
        H("1960: the year of independence"),
        T("The Community did not last as designed. In 1959 and 1960 most of the territories asked for and received "
          "independence by agreement, including Cameroun on 1 January 1960 (as a trust territory, a separate route). "
          "Togo, Senegal and Mali, Madagascar, Cote d'Ivoire, Niger, Chad, Gabon and others became independent in 1960 "
          "(check your textbook for the exact dates). France kept close links through cooperation agreements, "
          "monetary arrangements such as the CFA franc and military agreements."),
        KEY("British and French routes compared", "A standard essay question.", cards=[
            ["Britain", "Gradual constitutions, elections and conferences, with differences in each colony; Commonwealth link."],
            ["France", "Assimilation and the French Union first; a framework law (1956); a single referendum (1958); independence by agreement in 1960; close ties afterwards."],
            ["Debate", "Some historians stress the sharper break (Guinea) and the continuing French influence, while others stress African agency in negotiating the terms."],
        ]),
        EX("Model answer plan 1", intro="Why did Guinea vote No in 1958?", steps=[
            S("Political organisation", text="The PDG and the trade unions were strong and had mass support."),
            S("Leadership", text="Sekou Toure argued that real freedom required independence."),
            S("The terms of the Community", text="France kept control of key powers, so the Community did not satisfy nationalists."),
            S("Judgement", text="Strong organisation and leadership explain the choice. Others voted Yes for reasons of security and expectation of change."),
        ]),
        EX("Model answer plan 2", intro="Compare the process of decolonization in British and French West Africa.", steps=[
            S("Similarities", text="Elections, African ministers, no long war of liberation in West Africa."),
            S("Differences", text="Britain: step-by-step by colony; France: assimilation, the French Union, the Loi-Cadre, the 1958 referendum and a collective wave in 1960."),
            S("After independence", text="Britain: the Commonwealth; France: closer cooperation, currency and military accords."),
            S("Judgement", text="Both ended in independence on agreed terms, but French ties were tighter. Guinea shows the cost of breaking them."),
        ]),
        MISTAKE("Saying Guinea voted for independence in 1960", "Guinea's vote and independence were in 1958 (28 September and 2 October)."),
        MISTAKE("Forgetting that the Loi-Cadre divided the large federations", "It strengthened territorial governments but weakened the federal units."),
        QUIZ("What was Guinea's choice in the referendum of 28 September 1958?",
             ["Yes, to join the French Community", "No, leading to immediate independence", "It did not vote", "A third option of federation"], 1,
             "Guinea voted No and became independent on 2 October 1958.",
             feedback=["That was the choice of the other territories.", "", "Guinea voted.", "No federation option was offered."]),
        QUIZ("What was the Loi-Cadre of 1956?",
             ["A law giving each territory a government council with African ministers", "A treaty creating the OAU",
              "The constitution of the Fifth Republic", "A UN resolution on Cameroun"], 0,
             "The Loi-Cadre extended self-government within the French system.",
             feedback=["", "The OAU came in 1963.", "The Fifth Republic's constitution was voted on in 1958.", "It was a French law."]),
        H("Practice questions"),
        PQ("State what the Loi-Cadre of 1956 did.",
           "It created territorial assemblies and government councils with African ministers, widened the vote and left defence and foreign policy to France."),
        PQ("Explain two reasons why most French territories voted Yes in 1958.",
           "Fear of losing French aid and expertise; trust in leaders such as Houphouet-Boigny; the hope that the Community "
           "would develop into greater freedom."),
        PQ("Describe what happened to Guinea after its vote.",
           "It became independent on 2 October 1958; France withdrew administrators and aid, and Guinea turned to other partners, "
           "including Ghana and the Soviet bloc (check details)."),
        PQ("Compare the French and the British methods of decolonization in one paragraph.",
           "Britain used step-by-step constitutions and conferences, and the Commonwealth; France used the French Union, the Loi-Cadre "
           "and a 1958 referendum, then agreements in 1960 with close cooperation afterwards. Both avoided war in West Africa."),
        SUM("France moved from assimilation and the French Union to the Loi-Cadre (1956) and the referendum of 1958.",
            "Guinea voted No and was independent on 2 October 1958; others voted Yes.",
            "Most French territories became independent in 1960 by agreement, keeping close French ties.",
            "British and French methods differed, though both avoided war in West Africa."),
    ],
))

# ---------------------------------------------------------------------------
# 11. Algeria and Kenya
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="Armed liberation",
    title="Algeria and Kenya: settlers, war and independence",
    slug="h7-dec-algeria-kenya-armed-struggle",
    minutes=24,
    summary=("Why decolonization turned violent in Algeria and Kenya: settler societies, the FLN and the Algerian war, Mau Mau and "
             "the Emergency, how each ended, and how historians weigh the evidence and the numbers."),
    objectives=[
        "Explain why large settler populations made peaceful transfer harder",
        "Outline the Algerian war from 1954 to the Evian Accords and independence in 1962",
        "Outline the Mau Mau rising, the Emergency and Kenya's independence in 1963",
        "Evaluate the contested evidence on casualties and detention",
    ],
    key_concepts=["Settler colony", "FLN", "Evian Accords", "Mau Mau", "State of Emergency", "Detention"],
    blocks=[
        H("Introduction"),
        T("Where many settlers had made their homes and farms, independence meant more than a change of government: "
          "it meant a question about land, citizenship and who belonged. That is why Algeria and Kenya saw wars, while "
          "Ghana and Nigeria saw negotiations. This lesson looks at both cases and at the difficulty of the evidence."),
        D("A **settler colony** was a colony with a large population of European settlers who held land and "
          "political privileges and resisted majority rule.", title="Settler colony"),
        H("Algeria: the war"),
        T("France conquered Algeria from 1830 and treated it as part of France, with departments. About a million "
          "Europeans (the pieds-noirs) lived there beside a Muslim majority with fewer rights. After peaceful reform "
          "efforts failed, the National Liberation Front (FLN) launched attacks on 1 November 1954."),
        T("The war involved guerrilla actions, urban bombing and French counter-insurgency, including the Battle of Algiers "
          "(1956 to 1957) and the use of torture, which caused a crisis of conscience in France. In May 1958 the crisis in "
          "Algiers helped bring de Gaulle back to power. In 1959 he offered self-determination."),
        T("Opposition from the army and from settlers followed, including a failed generals' putsch in April 1961 and "
          "the violence of the OAS. The Evian Accords of March 1962 ended the war. A referendum in Algeria in July 1962 "
          "voted for independence, and Algeria became independent on 5 July 1962. Most of the settlers left, "
          "and Ahmed Ben Bella became the first leader."),
        H("Kenya: Mau Mau and the Emergency"),
        T("In Kenya, European settlers held the best farmland in the 'White Highlands'. Kikuyu people lost land and "
          "faced pass laws and limited rights. The Kenya African Union (KAU) led by Jomo Kenyatta sought reform by constitutional "
          "means. A militant movement known as Mau Mau, with oaths of unity, took up armed resistance from about 1952."),
        T("The colonial government declared a State of Emergency in October 1952 and arrested Kenyatta and others. He was "
          "tried at Kapenguria and imprisoned. The security forces and the Home Guard fought Mau Mau in the forests; "
          "large numbers of Kikuyu were detained in camps and villages were moved. The Emergency formally ended in 1960. "
          "Constitutional conferences at Lancaster House in 1960 and 1962 led to independence on 12 December 1963 under Kenyatta."),
        KEY("What shaped the outcomes?", "Compare the two cases.", cards=[
            ["Algeria", "Settlers considered Algeria part of France; the FLN won legitimacy abroad; the war's cost and the political crisis in France led "
             "de Gaulle to negotiate."],
            ["Kenya", "Mau Mau was militarily defeated, but the war showed the cost of keeping control, and Britain "
             "negotiated an independence settlement with African leaders who had not led the rising."],
        ]),
        H("Interpreting the evidence"),
        T("Casualty and detention numbers in both wars are disputed. For Algeria, estimates vary widely and "
          "governments, historians and different groups give different figures. For Kenya, some historians argue that detention "
          "and abuse were on a very large scale, while others give lower estimates of deaths and stress the "
          "role of violence by Mau Mau against other Africans as well. In 2013 the British government announced compensation "
          "for a number of surviving victims of abuse in detention. When you write, say that figures are disputed and name "
          "the kind of evidence used: official records, survivor testimony and later research."),
        EX("Model answer plan 1", intro="Why was independence won by war in Algeria?", steps=[
            S("Settlers", text="A large settler population and the status of Algeria as part of France made compromise hard."),
            S("Failure of reform", text="Peaceful demands were blocked, so the FLN chose armed struggle in 1954."),
            S("French politics", text="The war divided France, brought de Gaulle to power and ended with talks."),
            S("Judgement", text="The war was a result of the settler issue; the settlement came when the cost to France was greater than the benefit."),
        ]),
        EX("Model answer plan 2", intro="How far did Mau Mau cause Kenyan independence?", steps=[
            S("For", text="It showed that colonial rule could only be kept by force and at a high political cost."),
            S("Against", text="The movement was defeated militarily; independence came by constitutional talks led by others."),
            S("Evidence", text="The Emergency from 1952; Lancaster House 1960 and 1962; independence 1963."),
            S("Judgement", text="Mau Mau shaped the context and the timing, but its direct role is debated. Present both views."),
        ]),
        MISTAKE("Giving casualty figures as certain", "State that figures are disputed and describe the evidence."),
        MISTAKE("Saying Kenyatta led Mau Mau", "He was arrested and tried; historians disagree about his links with the movement. Do not state it as fact."),
        MISTAKE("Mixing the dates", "Algeria: war from 1954, independence 1962. Kenya: Emergency from 1952, independence 1963."),
        QUIZ("Which agreement ended the Algerian war in 1962?",
             ["The Lancaster House Agreement", "The Evian Accords", "The Brazzaville declaration", "The Treaty of Lagos"], 1,
             "The Evian Accords of March 1962 led to the ceasefire and the referendum on independence.",
             feedback=["Lancaster House was for Kenya and Zimbabwe.", "", "Brazzaville was in 1944.", "The Treaty of Lagos set up ECOWAS in 1975."]),
        QUIZ("What did Britain declare in Kenya in October 1952?",
             ["Independence", "A State of Emergency", "A plebiscite", "A federation"], 1,
             "A State of Emergency was declared in response to Mau Mau.",
             feedback=["Independence was in 1963.", "", "No plebiscite was held.", "A federation was not created."]),
        H("Practice questions"),
        PQ("Explain why settlers made decolonization harder in Algeria and Kenya.",
           "Settlers held land and privileges and resisted majority rule, and in Algeria they regarded the territory as part of France. "
           "Compromise was therefore difficult, and violence resulted."),
        PQ("Outline the main events of the Algerian war from 1954 to 1962.",
           "FLN attacks on 1 November 1954; Battle of Algiers; the 1958 crisis and de Gaulle's return; the 1959 offer of self-determination; "
           "the putsch and the OAS; Evian in March 1962; independence in July 1962."),
        PQ("Describe two features of the British response to Mau Mau.",
           "The State of Emergency of October 1952 and arrests; detention camps and moved villages, with military action. Later, "
           "constitutional conferences led to independence."),
        PQ("Why must a historian be careful with casualty figures in these wars?",
           "Records are incomplete and different groups use different methods and have different purposes; estimates differ widely."),
        SUM("Settler societies made negotiation harder in Algeria and Kenya.",
            "Algeria: FLN from 1954, Evian Accords in March 1962, independence in July 1962.",
            "Kenya: Mau Mau, Emergency from 1952, Lancaster House conferences, independence on 12 December 1963.",
            "Casualty and detention figures are disputed; describe the evidence and say so."),
    ],
))

# ---------------------------------------------------------------------------
# 12. Portuguese colonies and Zimbabwe
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="Armed liberation",
    title="The Portuguese colonies and Zimbabwe: liberation movements and negotiated endings",
    slug="h7-dec-portuguese-colonies-zimbabwe",
    minutes=24,
    summary=("Why Portugal and white-ruled Rhodesia resisted change; the wars in Angola, Mozambique and Guinea-Bissau; the 1974 "
             "coup in Lisbon; and the Rhodesian war, Lancaster House and Zimbabwe's independence in 1980."),
    objectives=[
        "Explain why Portugal refused to decolonize in the 1950s and 1960s",
        "Name the main liberation movements and leaders in Angola, Mozambique and Guinea-Bissau",
        "Explain how the 1974 coup in Portugal changed the situation",
        "Outline the road from UDI (1965) to independence in Zimbabwe in 1980",
    ],
    key_concepts=["Estado Novo", "MPLA", "FRELIMO", "PAIGC", "Carnation Revolution", "UDI", "Chimurenga", "Lancaster House"],
    blocks=[
        H("Introduction"),
        T("By 1965 most of Africa was independent. Yet in the south, Portugal and the white government of Southern Rhodesia "
          "refused to give way. Liberation movements took up arms, and the endings came in 1974 to 1975 and 1980. "
          "This lesson explains the reasons for the long resistance and the way each struggle ended."),
        H("The Portuguese colonies"),
        T("Portugal's government under Salazar (and later Caetano) called its colonies 'overseas provinces' and refused "
          "independence. The economy of Portugal depended partly on its colonies, and the regime used forced labour "
          "and a system that recognised only a small number of Africans as 'assimilated' (check your textbook for details)."),
        KEY("The three wars", "Learn the movements and leaders.", cards=[
            ["Angola", "War began in 1961. Three main movements: the MPLA (Agostinho Neto), the FNLA (Holden Roberto) and UNITA "
             "(Jonas Savimbi, from 1966). They disagreed with one another."],
            ["Mozambique", "FRELIMO, led first by Eduardo Mondlane (killed in 1969) and then Samora Machel, began armed action in 1964 from "
             "bases in Tanzania."],
            ["Guinea-Bissau and Cape Verde", "The PAIGC, led by Amilcar Cabral, began war in 1963. Cabral was assassinated in "
             "January 1973. Independence was declared in 1973 and recognised by Portugal in 1974."],
        ]),
        T("Portugal sent large forces, but the cost in money and lives was heavy. In April 1974 officers of the Armed Forces "
          "Movement overthrew the government in Lisbon, in what is called the Carnation Revolution. The new government "
          "agreed to end the wars. Guinea-Bissau was recognised in 1974; Mozambique became independent in June 1975, Cape Verde "
          "and Sao Tome in July 1975, and Angola in November 1975. In Angola a civil war followed, with foreign "
          "involvement from several states (check your textbook for details)."),
        H("Zimbabwe"),
        T("Southern Rhodesia had a white minority government and land laws that gave most of the best land to Europeans. "
          "The African nationalist parties ZAPU (Joshua Nkomo) and ZANU (formed in 1963, led by Ndabaningi Sithole, with Robert "
          "Mugabe) were banned. In November 1965 Ian Smith's government made a Unilateral Declaration of Independence (UDI) "
          "from Britain, to avoid majority rule. The UN imposed sanctions on Rhodesia."),
        T("Guerrilla war began in 1966 and grew from about 1972, with bases in Zambia and then Mozambique. It is often called "
          "the Second Chimurenga (the first being the risings of 1896 to 1897). Mozambique's independence in 1975 opened a long "
          "new border to guerrilla activity. By 1979 the cost of the war, economic problems and pressure from neighbours "
          "and from Britain and the USA led to talks."),
        T("The Lancaster House conference, held in London in late 1979 under British chairmanship, produced a constitution, "
          "a ceasefire and new elections. In the 1980 elections ZANU-PF won most seats. Zimbabwe became independent on "
          "18 April 1980 with Mugabe as Prime Minister."),
        KEY("What ended white rule in Rhodesia?", "Historians give different weight to different causes.", cards=[
            ["The war", "The guerrilla war raised costs and strained the army, especially after 1975."],
            ["Sanctions and isolation", "Sanctions and the loss of allies in Portuguese Africa made the economy harder to sustain."],
            ["Pressure from neighbours and powers", "South Africa and the United States wished to see a settlement; neighbouring states supported the movements."],
        ], note="A strong answer says that these causes worked together."),
        EX("Model answer plan 1", intro="Why did Portugal's colonies become independent in 1974 and 1975?", steps=[
            S("Wars", text="The colonial wars were costly and long, with no end in sight."),
            S("Politics in Portugal", text="Officers and others in Lisbon turned against the regime in April 1974."),
            S("Liberation movements", text="PAIGC, FRELIMO and the Angolan movements had built bases and international support."),
            S("Judgement", text="The wars made the coup possible, and the coup made independence quick. Neither alone is enough."),
        ]),
        EX("Model answer plan 2", intro="How important was armed struggle in the independence of Zimbabwe?", steps=[
            S("For", text="The war raised the cost for white rule and led to talks."),
            S("Against", text="Sanctions, the change of regime in Mozambique and outside pressure also forced talks."),
            S("Evidence", text="The war from 1966 to 1979; Mozambique 1975; Lancaster House 1979; the 1980 election."),
            S("Judgement", text="Armed struggle was central, but the endgame was negotiated and shaped by regional and international pressure."),
        ]),
        MISTAKE("Saying Angola became independent peacefully in 1975", "Independence was followed by a civil war. Say that, without judging the parties."),
        MISTAKE("Mixing UDI and independence", "UDI (1965) was a white minority declaration. Zimbabwe's independence was in 1980."),
        QUIZ("What event in Lisbon in April 1974 changed the situation in the Portuguese colonies?",
             ["The signing of the Evian Accords", "An officers' coup that overthrew the regime", "The independence of Brazil", "The Lancaster House conference"], 1,
             "The Carnation Revolution ended the old regime and led to the end of the colonial wars.",
             feedback=["The Evian Accords were for Algeria.", "", "Brazil's independence was in the 1820s.", "Lancaster House was about Rhodesia."]),
        QUIZ("Which conference led to Zimbabwean independence?",
             ["Foumban", "Berlin", "Lancaster House", "Bandung"], 2,
             "The Lancaster House conference of late 1979 produced the settlement.",
             feedback=["Foumban was held in 1961 in Cameroon.", "Berlin was in 1884 and 1885.", "", "Bandung was held in 1955."]),
        H("Practice questions"),
        PQ("Name the liberation movement and one leader in each of Mozambique and Guinea-Bissau.",
           "Mozambique: FRELIMO, led by Mondlane then Machel. Guinea-Bissau: PAIGC, led by Amilcar Cabral."),
        PQ("Explain why Portugal resisted decolonization longer than Britain and France.",
           "The regime saw the colonies as part of Portugal and as an economic base, and had no democratic pressure to leave until 1974; "
           "it also had few tools of gradual change in place."),
        PQ("Describe two ways in which the independence of Mozambique in 1975 affected Rhodesia.",
           "It removed a friendly neighbour and opened a long border for guerrillas; it also increased the pressure on Rhodesia's economy "
           "and on South Africa to seek a settlement."),
        PQ("What was UDI and why was it declared?",
           "A Unilateral Declaration of Independence by Ian Smith's government in November 1965, to keep white minority rule and avoid "
           "British demands for majority rule."),
        SUM("Portugal refused decolonization; wars began in Angola (1961), Guinea-Bissau (1963) and Mozambique (1964).",
            "The Carnation Revolution of April 1974 led to independence in 1974 and 1975.",
            "Rhodesia declared UDI in 1965; the Second Chimurenga and sanctions led to Lancaster House (1979).",
            "Zimbabwe became independent on 18 April 1980."),
    ],
))

# ---------------------------------------------------------------------------
# 13. Apartheid
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="South Africa",
    title="Apartheid: laws, aims and early resistance, 1948 to 1960",
    slug="h7-sa-apartheid-system-early-resistance",
    minutes=22,
    summary=("How the National Party built the apartheid system after 1948, the main laws and their effects, and how the ANC and "
             "its allies resisted, from the Defiance Campaign to Sharpeville."),
    objectives=[
        "Define apartheid and explain how the National Party came to power in 1948",
        "Describe the main laws and their effects on daily life",
        "Describe the early resistance: the Defiance Campaign, the Freedom Charter and the Treason Trial",
        "Explain the importance of Sharpeville in 1960",
    ],
    key_concepts=["Apartheid", "Pass laws", "Group Areas", "Bantu Education", "Defiance Campaign", "Freedom Charter", "Sharpeville"],
    blocks=[
        H("Introduction"),
        T("Imagine needing a permit to be in the town where you work, and being told where you may live by law. "
          "Apartheid, meaning 'separateness' in Afrikaans, made this the rule in South Africa. This lesson explains how the system "
          "was built, and how the first generation of resistance responded."),
        D("**Apartheid** was the system of racial segregation and white minority rule built by the National Party government "
          "from 1948. It classified people by race and set separate rights, residence, schools and jobs.", title="Apartheid"),
        IMG("al-h7-south-africa-timeline.svg",
            alt="Timeline of South Africa from 1948 to 1994 with the main events",
            caption="Figure 1. Key events, 1948 to 1994 (not to scale)."),
        H("1948 and the laws"),
        T("In May 1948 the National Party, mainly supported by Afrikaner voters, won the election on a platform of "
          "apartheid. Segregation already existed in South Africa, such as land laws and pass laws, but the new government made "
          "it a complete system."),
        KEY("Main apartheid laws", "Know a few well, with their dates.", cards=[
            ["Population Registration Act (1950)", "Classified every person by race, which decided their rights."],
            ["Group Areas Act (1950)", "Set separate residential and business areas, leading to forced removals."],
            ["Pass laws", "Required Africans to carry passes controlling movement to towns and work."],
            ["Bantu Education Act (1953)", "Created a separate and unequal school system for African children."],
            ["Suppression of Communism Act (1950)", "Gave the state broad powers against opponents, defined widely."],
            ["Homelands policy (1950s onward)", "Assigned Africans to 'homelands' and later gave some of them nominal independence in the 1970s and 1980s."],
        ], note="Check your textbook for exact dates, especially for the homelands."),
        T("Supporters in the government said the laws protected the identity of each group. Critics at home and abroad said "
          "they were a system of racial domination that took land, rights and opportunities from the majority."),
        H("Early resistance"),
        T("The African National Congress (ANC), founded in 1912, was joined by a Youth League in 1944 whose members included "
          "Nelson Mandela, Walter Sisulu and Oliver Tambo. Its 1949 Programme of Action called for strikes and civil "
          "disobedience. In 1952 the ANC and the South African Indian Congress began the Defiance Campaign, in which volunteers "
          "broke apartheid laws peacefully and were arrested."),
        T("In June 1955 a Congress of the People at Kliptown adopted the Freedom Charter, a statement of demands for "
          "a non-racial country. In 1956 leaders were arrested for treason and a long Treason Trial followed. "
          "All accused were finally acquitted by 1961."),
        T("In 1959 the Pan Africanist Congress (PAC) broke away from the ANC. On 21 March 1960 a PAC campaign against the pass laws "
          "led to a protest at Sharpeville, where police opened fire and killed 69 people (the number most books give). "
          "The ANC and PAC were banned in April 1960."),
        KEY("Why was Sharpeville a turning point?", "Explain with two points.", cards=[
            ["For the state", "It banned the movements and a long period of repression followed."],
            ["For the opposition", "Peaceful protest had been met with force, so the ANC formed Umkhonto we Sizwe in 1961 and turned to sabotage as well."],
            ["Abroad", "It drew world attention and stronger criticism of apartheid."],
        ]),
        EX("Model answer plan 1", intro="Explain how the National Party built the apartheid system after 1948.", steps=[
            S("Mandate", text="Won the 1948 election on an apartheid platform."),
            S("Classification", text="Population Registration Act 1950 classified people by race."),
            S("Land and movement", text="Group Areas Act and pass laws controlled where people could live and work."),
            S("Education", text="Bantu Education created separate schooling."),
            S("Judgement", text="A system that was already partly in place was made complete, backed by laws against opponents."),
        ]),
        EX("Model answer plan 2", intro="How effective was peaceful resistance to apartheid between 1950 and 1960?", steps=[
            S("Achievements", text="Mass participation (Defiance Campaign), a statement of aims (the Freedom Charter), world attention."),
            S("Limits", text="Laws were not repealed; leaders were arrested; the movements were banned after Sharpeville."),
            S("Evidence", text="1952, 1955, 1956 Treason Trial, 1960 ban."),
            S("Judgement", text="It built a movement and a programme, but it did not change the laws. Many concluded that new methods were needed."),
        ]),
        MISTAKE("Describing apartheid as starting in 1994 or ending in 1960", "It began as policy in 1948 and ended in the early 1990s with the first all-race election in 1994."),
        MISTAKE("Saying Sharpeville was an ANC protest", "It was organised by the PAC. The ANC was also banned afterwards."),
        QUIZ("Which law classified every South African by race?",
             ["Group Areas Act", "Bantu Education Act", "Population Registration Act", "Pass Law"], 2,
             "The Population Registration Act of 1950 set the racial categories on which other laws relied.",
             feedback=["It set separate residential areas.", "It governed schooling.", "", "Pass laws controlled movement."]),
        QUIZ("What document was adopted at Kliptown in 1955?",
             ["The Freedom Charter", "The Atlantic Charter", "The OAU Charter", "The Constitutive Act"], 0,
             "The Freedom Charter set out the demands of the Congress Alliance.",
             feedback=["", "That was a 1941 wartime statement.", "That is the founding charter of the OAU.", "That is the founding treaty of the AU."]),
        H("Practice questions"),
        PQ("Define apartheid and give two of its laws with dates.",
           "A system of racial segregation and white minority rule from 1948. Population Registration Act (1950); Group Areas Act (1950); Bantu Education Act (1953)."),
        PQ("Describe the Defiance Campaign of 1952.",
           "A campaign by the ANC and the Indian Congress in which volunteers deliberately broke segregation and pass laws "
           "and were arrested, to protest peacefully against unjust laws."),
        PQ("Explain why Sharpeville is regarded as a turning point.",
           "Police killed protesters on 21 March 1960; the ANC and PAC were banned; the ANC formed an armed wing in 1961; and "
           "international criticism grew."),
        PQ("What was the Freedom Charter and why does it matter?",
           "A statement of demands for a democratic, non-racial South Africa adopted at Kliptown in 1955. It gave the movement a "
           "programme and was a basis for later constitutional ideas."),
        SUM("The National Party won in 1948 and built the apartheid system with many laws.",
            "Key laws: Population Registration, Group Areas, pass laws, Bantu Education.",
            "Early resistance: Defiance Campaign (1952), Freedom Charter (1955), Treason Trial (1956 to 1961).",
            "Sharpeville (21 March 1960) led to bans and to armed resistance."),
    ],
))

# ---------------------------------------------------------------------------
# 14. The end of apartheid
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="South Africa",
    title="The end of apartheid: struggle, pressure and negotiation, 1960 to 1994",
    slug="h7-sa-struggle-pressure-negotiation-1994",
    minutes=24,
    summary=("From armed struggle and Rivonia to Soweto, mass resistance and sanctions in the 1980s, and the negotiations "
             "leading to the election of April 1994, with the different explanations historians give for the end of apartheid."),
    objectives=[
        "Outline the main stages of resistance from 1960 to 1990",
        "Explain the roles of internal resistance, international pressure and economic crisis",
        "Describe the negotiated transition from 1990 to 1994",
        "Compare interpretations of why apartheid ended",
    ],
    key_concepts=["Umkhonto we Sizwe", "Rivonia Trial", "Black Consciousness", "Soweto", "UDF", "Sanctions", "CODESA"],
    blocks=[
        H("Introduction"),
        T("Why did a powerful government give up a system it had defended for more than forty years? Many causes worked "
          "together, and historians give them different weights. This lesson follows the stages first and then compares the "
          "explanations."),
        H("1960 to 1976: repression and the armed struggle"),
        T("After the bans of 1960 the ANC formed Umkhonto we Sizwe (MK) in 1961, with Mandela as a leader, and began "
          "sabotage of buildings. In 1963 police arrested leaders at Rivonia. In the Rivonia Trial (1963 to 1964) Mandela "
          "and others were sentenced to life imprisonment in June 1964. Many leaders were jailed or went into exile."),
        T("In the late 1960s Steve Biko and others developed Black Consciousness, which stressed pride and self-reliance. "
          "The South African Students' Organisation was founded in 1968."),
        H("1976 to 1990: uprising and the crisis of the 1980s"),
        T("On 16 June 1976 school pupils in Soweto marched against the use of Afrikaans in teaching and were met "
          "by police fire. Protests spread across the country and many people were killed (figures vary). Biko died in police "
          "custody in September 1977. In November 1977 the UN Security Council imposed a mandatory arms embargo on South Africa."),
        T("The government under P. W. Botha made some reforms, such as a new tricameral parliament in 1984 which "
          "excluded Africans. In 1983 the United Democratic Front (UDF) was formed, uniting hundreds of organisations. Unrest "
          "and states of emergency followed in 1985 and 1986. Trade unions, churches and communities were active, and "
          "international sanctions and disinvestment increased in the mid-1980s."),
        H("1990 to 1994: negotiated transition"),
        T("F. W. de Klerk became President in 1989. On 2 February 1990 he unbanned the ANC, PAC and the Communist Party; "
          "Mandela was released on 11 February 1990 after 27 years. Talks were hard and sometimes violent. The CODESA "
          "negotiations began in December 1991, and violence continued in some places. An interim constitution was agreed, and "
          "the first election open to all adults was held in April 1994. The ANC won and Mandela became President in May 1994."),
        KEY("Why did apartheid end? Four explanations", "Use several and weigh them.", cards=[
            ["Internal resistance", "Strikes, school and township protests, the UDF and trade unions made the country hard to govern and raised the cost of repression."],
            ["International pressure", "Sanctions, sports and cultural boycotts, UN action and loss of foreign finance."],
            ["Economic crisis", "Slow growth, the cost of defence and the need for skilled workers and markets made the system costly."],
            ["Elite negotiation and the end of the Cold War", "Fear of communism had been part of the government's case; its decline and the readiness of leaders such as "
             "de Klerk and Mandela to negotiate made a settlement possible."],
        ], note="Different historians stress different causes. A strong answer links them and gives a judgement."),
        EX("Model answer plan 1", intro="How important was internal resistance in ending apartheid?", steps=[
            S("For", text="Soweto, the UDF, unions and the unrest of the 1980s made the country hard to govern."),
            S("Against", text="The state was militarily strong. The settlement of 1990 to 1994 came by negotiation, helped by outside pressure and economic change."),
            S("Evidence", text="1976, 1983 UDF, 1985 to 1986 emergencies, 1990 unbanning."),
            S("Judgement", text="Resistance changed what the state could do, but other pressures decided its timing."),
        ]),
        EX("Model answer plan 2", intro="Assess the contribution of international pressure to the end of apartheid.", steps=[
            S("Actions", text="UN arms embargo (1977), sanctions and disinvestment in the 1980s, sports boycotts."),
            S("Effects", text="Higher costs, loss of finance and isolation."),
            S("Limits", text="Some major states resisted sanctions; the effect on political decisions is debated."),
            S("Judgement", text="International pressure raised the cost of the system and strengthened the opposition. It was one factor among several."),
        ]),
        H("Source skill: interpreting a source on Soweto"),
        T("Illustrative source (invented for practice): 'The children came out in peace with their books. The police "
          "fired, and the street was full of running children.' (An eyewitness recalled it years later.)", title="Illustrative source"),
        T("Provenance: a later recollection by an eyewitness. Value: gives a personal view of the day. Limit: memory, one "
          "place only, and no figures. Cross-check with police reports, press photographs and later inquiries."),
        MISTAKE("Giving one cause for the end of apartheid", "Examiners want several causes with a judgement on their relative weight."),
        MISTAKE("Dating Mandela's release to 1994", "He was released on 11 February 1990 and became President in May 1994."),
        QUIZ("What began on 16 June 1976?",
             ["The Rivonia Trial", "The Soweto uprising", "The CODESA talks", "The Defiance Campaign"], 1,
             "The Soweto protests began on 16 June 1976.",
             feedback=["That was in 1963 to 1964.", "", "That began in December 1991.", "That was in 1952."]),
        QUIZ("What did the UDF, formed in 1983, do?",
             ["Replaced the ANC in exile", "United many community and other organisations in opposition to apartheid", "Governed the homelands", "Wrote the 1996 constitution"], 1,
             "The United Democratic Front brought together hundreds of organisations.",
             feedback=["The ANC continued in exile.", "", "The homelands had their own governments.", "The 1996 text was written after 1994 by the new parliament."]),
        H("Practice questions"),
        PQ("Describe the Rivonia Trial and its outcome.",
           "Leaders of the ANC and MK, including Mandela, were tried for sabotage in 1963 to 1964 and sentenced to life imprisonment in June 1964."),
        PQ("Explain two effects of the Soweto uprising of 1976.",
           "It showed the anger of young people and spread protests across the country; it led to many deaths, arrests and exile of "
           "youth; it increased international criticism and pressure."),
        PQ("Outline the main events between February 1990 and May 1994.",
           "Unbanning of the ANC and PAC (2 February 1990), Mandela's release (11 February 1990), CODESA talks from December 1991, "
           "interim constitution, elections in April 1994 and Mandela's presidency in May 1994."),
        PQ("Essay plan: 'Apartheid ended mainly because of pressure from outside South Africa.' Discuss.",
           "For: sanctions, the arms embargo, boycotts. Against: internal resistance, economic problems and the decisions of leaders to negotiate. "
           "Judgement: outside pressure was important but worked together with internal causes."),
        SUM("After 1960 the ANC formed MK; Rivonia (1964) sent Mandela and others to prison.",
            "Soweto (1976) and the 1980s uprisings, the UDF and sanctions increased the pressure.",
            "De Klerk unbanned the ANC in February 1990 and Mandela was released; the first all-race vote was in April 1994.",
            "Historians weigh internal resistance, international pressure, economic crisis and negotiation differently."),
    ],
))

# ---------------------------------------------------------------------------
# 15. Containment, Marshall Plan, deterrence
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="Cold War geopolitics",
    title="From the Truman Doctrine to deterrence: how the blocs formed, 1945 to 1962",
    slug="h7-cw-containment-marshall-deterrence",
    minutes=24,
    summary=("The origins of the Cold War in Europe: the Truman Doctrine, the Marshall Plan, containment, the Berlin blockade, NATO "
             "and the Warsaw Pact, and nuclear deterrence up to the Cuban missile crisis, with the debate on who was responsible."),
    objectives=[
        "Explain containment and the Truman Doctrine",
        "Describe the Marshall Plan and the Soviet response",
        "Outline the Berlin blockade, NATO and the Warsaw Pact",
        "Explain nuclear deterrence and the Cuban missile crisis",
        "Compare orthodox, revisionist and post-revisionist interpretations of Cold War origins",
    ],
    key_concepts=["Containment", "Truman Doctrine", "Marshall Plan", "Cominform", "NATO", "Warsaw Pact", "Deterrence", "Historiography"],
    blocks=[
        H("Introduction"),
        T("In 1945 the USA and the USSR were allies who had defeated Germany. Within three years they were rivals with "
          "armies facing each other in Europe. The Cold War was a struggle between them and their allies that stopped short of direct "
          "war between the two great powers. It shaped Africa too, as later lessons show."),
        D("**Containment** was the American policy of preventing the spread of Soviet influence, associated with the diplomat "
          "George Kennan's analysis of 1946 to 1947. **Deterrence** is the idea that the threat of unacceptable retaliation "
          "prevents an attack.", title="Key terms"),
        IMG("al-h7-cold-war-blocs.svg",
            alt="Two columns showing Western and Eastern institutions: Truman Doctrine, Marshall Plan, NATO, and Cominform, Comecon, Warsaw Pact",
            caption="Figure 1. Western and Eastern institutions, 1947 to 1955 (schematic)."),
        H("The formation of the blocs"),
        T("In March 1947 President Truman asked Congress for aid for Greece and Turkey and pledged to support free peoples "
          "resisting pressure. This became the Truman Doctrine. In June 1947 Secretary of State Marshall proposed the European "
          "Recovery Programme (the Marshall Plan), and large American aid flowed to Western Europe from 1948. The Soviet Union "
          "refused the aid for itself and its Eastern European neighbours, created the Cominform in September 1947 and later "
          "Comecon (1949)."),
        T("The division of Germany was the sharpest test. In June 1948 the USSR blockaded the Western sectors of Berlin. "
          "The Western powers supplied the city by air until the blockade ended in May 1949. In April 1949 the "
          "North Atlantic Treaty created NATO, and in 1949 two German states were formed. The Warsaw Pact followed in May 1955, "
          "after West Germany joined NATO."),
        KEY("Two sets of aims", "Use these in essays on origins.", cards=[
            ["Western aims", "Rebuild Western Europe's economies, stop the spread of communism, keep the USA engaged in Europe."],
            ["Soviet aims", "Security after two invasions, control over Eastern Europe, and recovery from huge war damage."],
        ]),
        H("Deterrence and crisis"),
        T("The USSR tested an atomic bomb in 1949 and both sides built much larger nuclear arsenals. Each side relied on the threat "
          "of destruction in return, sometimes called mutually assured destruction. This made direct war between them risky, but wars "
          "took place elsewhere (Korea 1950 to 1953, Vietnam). In October 1962 the discovery of Soviet missiles in Cuba brought "
          "the two powers to the edge of nuclear war. It ended when the USSR agreed to withdraw the missiles, and the USA gave a "
          "pledge not to invade Cuba and, in a private understanding, to remove missiles from Turkey (check your textbook)."),
        H("Who was responsible? Interpretations"),
        KEY("Three schools of thought", "Each uses evidence; none is final.", cards=[
            ["Orthodox (traditional)", "The USSR's expansion in Eastern Europe and its ideology caused the Cold War. Evidence: control "
             "of Eastern Europe, the Berlin blockade."],
            ["Revisionist", "American economic power and the wish for open markets provoked Soviet fears. Evidence: the Marshall Plan's aims, "
             "the atomic bomb diplomacy."],
            ["Post-revisionist", "Both sides misread each other, in a setting of fear and mistrust after the war. "
             "Evidence: Soviet and American documents opened after 1991."],
        ], note="Check your textbook for the historians commonly named for each school."),
        EX("Model answer plan 1", intro="Explain the importance of the Marshall Plan in the origins of the Cold War.", steps=[
            S("What it did", text="Gave large-scale aid to rebuild Western Europe from 1948."),
            S("American view", text="It would stop communism growing in poor, damaged economies."),
            S("Soviet view", text="They saw it as an attempt to draw Eastern Europe into an American sphere, and refused it."),
            S("Result", text="It deepened the division: the Cominform, Comecon, the Berlin crisis."),
            S("Judgement", text="It was a cause and a symptom of the split. It shows how each side's defensive move looked aggressive to the other."),
        ]),
        EX("Model answer plan 2", intro="'Nuclear deterrence kept the peace between 1945 and 1962.' Discuss.", steps=[
            S("For", text="No direct war between the superpowers; both stepped back in Cuba in 1962."),
            S("Against", text="Wars took place by proxy; the Cuban crisis was a near miss, showing luck as well as design."),
            S("Evidence", text="Korea, Berlin, Cuba."),
            S("Judgement", text="Deterrence may have prevented direct war but made crises dangerous. The claim is plausible but cannot be proved."),
        ]),
        MISTAKE("Dating NATO and the Warsaw Pact together", "NATO was formed in April 1949 and the Warsaw Pact in May 1955."),
        MISTAKE("Calling the Marshall Plan a military plan", "It was economic aid. The military alliance was NATO."),
        MISTAKE("Giving one school of historians as proven", "Present at least two and compare their evidence."),
        QUIZ("Which was the first of these to be announced?",
             ["The Warsaw Pact", "The Marshall Plan", "NATO", "The Truman Doctrine"], 3,
             "The Truman Doctrine (March 1947) preceded the Marshall Plan (1947 to 1948), NATO (1949) and the Warsaw Pact (1955).",
             feedback=["Warsaw Pact was in 1955.", "The Marshall Plan was proposed in June 1947, after March.", "NATO was in 1949.", ""]),
        QUIZ("What was the Berlin blockade (1948 to 1949)?",
             ["A Western blockade of East Germany", "A Soviet blockade of the Western sectors of Berlin", "A UN blockade of Cuba", "A strike by German workers"], 1,
             "The USSR closed land access to Western Berlin and the Western powers flew in supplies.",
             feedback=["It was the other way round.", "", "The Cuban crisis was in 1962 and involved a US naval quarantine.", "It was a state action, not a strike."]),
        H("Practice questions"),
        PQ("Explain what the Truman Doctrine was.",
           "A policy announced in March 1947 to support free peoples resisting pressure, beginning with aid to Greece and Turkey. It was "
           "the start of American containment."),
        PQ("Describe the main features of the Berlin blockade and its results.",
           "The USSR blocked road and rail access to the Western sectors of Berlin in June 1948; the West supplied the city by air; the "
           "blockade ended in May 1949; NATO and two German states followed."),
        PQ("Compare the orthodox and revisionist explanations of the Cold War.",
           "Orthodox: Soviet expansion and ideology were the cause. Revisionist: American economic power and the wish for open markets "
           "provoked Soviet fears. Each uses different evidence."),
        PQ("Explain how the Cuban missile crisis showed both the risks and the working of deterrence.",
           "Both sides came close to nuclear war, yet both backed down and found a compromise because each feared the other's retaliation."),
        SUM("The Truman Doctrine (1947), the Marshall Plan (1947 to 1948) and NATO (1949) shaped the Western bloc; Cominform, Comecon and the Warsaw Pact (1955) the Eastern.",
            "Containment aimed to stop Soviet influence spreading; Berlin (1948 to 1949) was an early crisis.",
            "Nuclear deterrence made direct war risky; Cuba (1962) was the closest call.",
            "Historians differ: orthodox, revisionist and post-revisionist explanations."),
    ],
))

# ---------------------------------------------------------------------------
# 16. Global South
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="Cold War geopolitics",
    title="The Cold War in the Global South: non-alignment, Congo, Angola and Cameroon",
    slug="h7-cw-global-south-africa",
    minutes=24,
    summary=("How the superpower rivalry reached Asia, Africa and Latin America: Bandung and non-alignment, the Congo crisis, "
             "Angola in 1975 and the Horn of Africa, and how historians judge the Cold War's impact on African states."),
    objectives=[
        "Explain the aims of the Bandung Conference and the Non-Aligned Movement",
        "Describe the Congo crisis of 1960 to 1965 as a Cold War case",
        "Describe the Angolan conflict of 1975 and the foreign involvement",
        "Evaluate how far the Cold War shaped African politics, including that of Cameroon",
    ],
    key_concepts=["Global South", "Bandung", "Non-alignment", "Proxy war", "Congo crisis", "Angola 1975", "Ideology"],
    blocks=[
        H("Introduction"),
        T("When two elephants fight, it is said, the grass suffers. For many new states the Cold War was the rivalry of "
          "two giants playing out on their territory. Some leaders used the rivalry to win aid, and others were trapped by it. "
          "This lesson looks at both sides."),
        D("The **Global South** is a term for the countries of Africa, Asia and Latin America, many of them former colonies. "
          "A **proxy war** is a conflict in which outside powers support opposing local sides without fighting each other directly.",
          title="Terms"),
        IMG("al-h7-cold-war-timeline.svg",
            alt="Timeline of the Cold War from the Truman Doctrine in 1947 to the end of the USSR in 1991",
            caption="Figure 1. Cold War timeline (not to scale)."),
        H("Non-alignment"),
        T("In April 1955 delegates from 29 Asian and African countries met at Bandung in Indonesia. They called for "
          "independence, economic cooperation and peace, and criticised colonialism. In 1961 leaders including Tito of Yugoslavia, "
          "Nasser, Nehru, Nkrumah and Sukarno helped form the Non-Aligned Movement at Belgrade. Non-alignment meant not joining "
          "either bloc, though in practice states took aid from both."),
        H("The Congo crisis, 1960 to 1965"),
        T("The Belgian Congo became independent on 30 June 1960, with Patrice Lumumba as Prime Minister and Joseph Kasavubu as President. "
          "Within days the army mutinied and Katanga, a rich mining province, announced its secession. Belgium sent troops, "
          "Lumumba asked the UN for help and then sought Soviet help, and the USA and its allies feared a communist foothold. "
          "In September Mobutu intervened and Lumumba was removed. He was killed in January 1961 in Katanga (check "
          "your textbook for details on who was involved). The UN force stayed until 1964. Mobutu took power in 1965 and "
          "became a long-term ally of the West."),
        H("Angola 1975 and the Horn"),
        T("When Portugal left Angola in 1975, the three movements fought for control. The MPLA, with Soviet and Cuban "
          "support, held Luanda and was recognised by many African states. The FNLA and UNITA received support from "
          "the USA, South Africa and others. Cuban troops arrived in large numbers. The war lasted many years. "
          "In 1977 and 1978, in the Horn of Africa, the USSR changed sides, moving from Somalia to Ethiopia in the war over the Ogaden, "
          "which showed how alliances could shift."),
        KEY("Cold War and African politics: two readings", "Weigh the evidence.", cards=[
            ["The Cold War as a major cause", "Superpower aid, arms and ideology prolonged wars and supported rulers who "
             "served their interests (Mobutu, for example). Evidence: Congo and Angola."],
            ["Local causes first", "Ethnic, regional and economic conflicts, colonial borders and leaders' choices "
             "were the main causes of the wars. Outsiders joined existing conflicts. Evidence: the local origins of Katanga's "
             "secession and the pre-existing rivalry of the Angolan movements."],
        ]),
        H("A Cameroon connection"),
        T("In the 1950s the French authorities often described the UPC as linked to communism, and some UPC leaders had contacts "
          "with organisations in the Eastern bloc and China. Historians disagree about how far the Cold War explains the "
          "conflict, compared with local politics. After independence, Ahidjo's government kept close ties with France and the West. "
          "Check your textbook for the evidence on external support."),
        EX("Model answer plan 1", intro="Why did the Congo crisis become part of the Cold War?", steps=[
            S("Local crisis", text="Mutiny, Katanga's secession and a weak new state."),
            S("Outside powers", text="Belgium's troops; Lumumba's requests to the UN and then the USSR; US and Western fears of communism."),
            S("Result", text="Lumumba was removed and killed; Mobutu rose with Western support."),
            S("Judgement", text="The crisis started locally, but superpower fears shaped its course and result."),
        ]),
        EX("Model answer plan 2", intro="How far did the Cold War harm Africa?", steps=[
            S("Harm", text="Arms and proxy wars, support for authoritarian rulers, pressure on economic choices."),
            S("Benefit", text="Some states obtained aid and support for their liberation struggles; non-alignment gave room to bargain."),
            S("Evidence", text="Congo, Angola 1975, Bandung and the Non-Aligned Movement."),
            S("Judgement", text="The impact was mixed. The Cold War raised the stakes of local conflicts, but it was not their only cause."),
        ]),
        MISTAKE("Saying non-aligned states took no aid", "They avoided formal alliances but often accepted aid from both blocs."),
        MISTAKE("Explaining African wars only by the Cold War", "Always give the local causes as well."),
        QUIZ("Which conference of 1955 brought together Asian and African states?",
             ["Yalta", "Bandung", "Potsdam", "Berlin"], 1,
             "The Bandung Conference of April 1955 met in Indonesia.",
             feedback=["Yalta was a wartime conference of the Allies in 1945.", "", "Potsdam was in 1945.", "Berlin (1884 to 1885) divided Africa among colonial powers."]),
        QUIZ("Who was the first Prime Minister of the independent Congo in 1960?",
             ["Joseph Mobutu", "Patrice Lumumba", "Moise Tshombe", "Laurent Kabila"], 1,
             "Lumumba was Prime Minister and Kasavubu was President.",
             feedback=["Mobutu was an army officer who later took power.", "", "Tshombe led the secession of Katanga.", "Kabila came to power in 1997."]),
        H("Practice questions"),
        PQ("State two aims of the Non-Aligned Movement.",
           "To stay outside the two military blocs and to support independence, economic development and peace for new states."),
        PQ("Describe the part played by outside powers in the Congo crisis.",
           "Belgium sent troops, the UN sent a force, and the USA and USSR competed for influence, which affected the removal of Lumumba and the rise of Mobutu."),
        PQ("Explain why Angola's independence in 1975 became a Cold War conflict.",
           "Three rival movements each got different outside backers: the MPLA had Soviet and Cuban support, while the FNLA and UNITA had "
           "support from the USA, South Africa and others."),
        PQ("To what extent did the Cold War cause conflict in Africa? Give two points on each side.",
           "Cause: arms and aid supply, backing of rulers, proxy wars. Not the only cause: local rivalries, colonial borders and leaders' choices. "
           "Judgement: it deepened local conflicts rather than creating them."),
        SUM("Bandung (1955) and the Non-Aligned Movement (1961) aimed at independence from both blocs.",
            "In the Congo (1960 to 1965) a local crisis became a Cold War one.",
            "Angola in 1975 and the Horn showed proxy wars and shifting alliances.",
            "Local causes and Cold War rivalry both mattered; weigh them in essays."),
    ],
))

# ---------------------------------------------------------------------------
# 17. UN Charter and Security Council
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="The United Nations",
    title="The UN Charter and the Security Council: powers, the veto and reform",
    slug="h7-un-charter-security-council-veto",
    minutes=22,
    summary=("The purposes and principles of the UN Charter, how the Security Council is composed and votes, the use of the veto "
             "in the Cold War, and the arguments for reform, including the place of Africa."),
    objectives=[
        "State the main purposes and principles of the UN Charter",
        "Describe the organs of the UN and the composition of the Security Council",
        "Explain how the veto works and its effects in the Cold War",
        "Summarise the arguments for and against reform of the Security Council",
    ],
    key_concepts=["UN Charter", "General Assembly", "Security Council", "Permanent members", "Veto", "Chapter VII", "Reform"],
    blocks=[
        H("Introduction"),
        T("The League of Nations had failed to stop the Second World War. In 1945, delegates from 50 states met in "
          "San Francisco to create a stronger body. The UN Charter was signed on 26 June 1945 and came into force on "
          "24 October 1945. For Cameroon the UN mattered directly, since it supervised trusteeship and the plebiscites. This lesson "
          "explains how the UN's main organs work."),
        D("The **UN Charter** is the founding treaty of the United Nations. Its main purposes are to maintain international peace "
          "and security, develop friendly relations between nations, solve international economic, social and humanitarian "
          "problems, and promote human rights.", title="UN Charter"),
        H("Principles and organs"),
        T("Key principles include the sovereign equality of members, settling disputes peacefully, and refraining from the "
          "threat or use of force against another state's territory (Article 2(4)). Article 2(7) limits UN intervention in matters that "
          "are essentially within a state's domestic jurisdiction, except for enforcement measures under Chapter VII. Article 51 "
          "recognises the right of self-defence."),
        KEY("Main organs", "Know the role of each.", cards=[
            ["General Assembly", "All members, one vote each. Debates and recommends. Cannot give binding orders on peace and security."],
            ["Security Council", "Primary responsibility for peace and security. Its decisions bind members."],
            ["Secretariat", "Led by the Secretary-General, who runs the administration and can bring matters to the Council's attention."],
            ["International Court of Justice", "Settles legal disputes between states that agree to its jurisdiction and gives advisory opinions."],
            ["ECOSOC and the Trusteeship Council", "ECOSOC deals with economic and social work. The Trusteeship Council supervised trust territories and suspended operations in 1994."],
        ]),
        H("The Security Council"),
        T("The Council has fifteen members: five permanent (China, France, Russia (earlier the USSR), the United Kingdom and the "
          "United States) and ten elected for two-year terms. Before 1966 there were eleven members. A substantive decision needs nine votes "
          "and no veto by a permanent member. An abstention is not a veto."),
        T("Chapter VI covers peaceful settlement of disputes. Chapter VII allows the Council to decide on measures including "
          "sanctions and, if necessary, force, when it finds a threat to peace, a breach of peace or an act of aggression."),
        D("The **veto** is the power of each permanent member to block any substantive decision of the Security Council by voting against it.",
          title="Veto"),
        H("The veto and the Cold War"),
        T("During the Cold War the USA and the USSR used the veto often, so that the Council could not act on many disputes. In "
          "1950 the Council authorised help for South Korea because the USSR was boycotting meetings and did not vote. Later that "
          "year the General Assembly adopted the 'Uniting for Peace' resolution, allowing it to recommend action when the Council "
          "is blocked. That is a way round the veto, but the Assembly's resolutions are recommendations."),
        KEY("Reform debates", "Present arguments, not preferences.", cards=[
            ["Arguments for reform", "The Council reflects the world of 1945. Africa has no permanent seat though many of the issues "
             "before the Council concern Africa. The African Union has put forward a common position asking for permanent seats "
             "(the 'Ezulwini Consensus' of 2005, check your textbook)."],
            ["Arguments for caution", "Wider veto powers could make decisions harder; countries disagree on which states should "
             "join; the permanent members must agree to any change of the Charter."],
        ]),
        EX("Model answer plan 1", intro="How far did the veto limit the effectiveness of the UN during the Cold War?", steps=[
            S("For", text="Frequent vetoes blocked action on disputes where the superpowers or their allies were involved."),
            S("Against", text="The UN still did useful work: peacekeeping, decolonization through trusteeship and the Assembly, and humanitarian agencies."),
            S("Evidence", text="Korea 1950 (an exception), Uniting for Peace, the Congo force in 1960."),
            S("Judgement", text="The veto limited action on the main superpower disputes, but the UN found other ways to act."),
        ]),
        EX("Model answer plan 2", intro="Should Africa have permanent representation on the Security Council?", steps=[
            S("For", text="A large share of the Council's agenda concerns Africa, and the Council reflects the power balance of 1945."),
            S("Against", text="Agreement on which African states should be chosen is hard, and wider membership could slow decisions."),
            S("Evidence", text="The Council's agenda and the African Union's stated position."),
            S("Judgement", text="The case for wider representation is widely made. The practical question is how, and the answer depends on a change of the Charter that the permanent members must accept."),
        ]),
        MISTAKE("Saying the General Assembly can order states to act on security matters", "Its resolutions on peace and security are recommendations."),
        MISTAKE("Treating an abstention as a veto", "A substantive resolution passes with nine votes and no negative vote from a permanent member. Abstentions do not block it."),
        QUIZ("How many members does the Security Council have today?",
             ["5", "11", "15", "193"], 2,
             "Five permanent and ten elected members make fifteen.",
             feedback=["That is only the permanent members.", "That was the size before 1966.", "", "193 is about the number of UN member states."]),
        QUIZ("What does Chapter VII of the Charter allow the Security Council to do?",
             ["Only to hold debates", "To decide on enforcement measures including sanctions and force", "To appoint the Secretary-General alone", "To rule in cases between states"], 1,
             "Chapter VII authorises enforcement when there is a threat to the peace, a breach of the peace or aggression.",
             feedback=["Debate is not the limit of its powers.", "", "The Secretary-General is appointed by the Assembly on the Council's recommendation.", "That is the International Court of Justice."]),
        H("Practice questions"),
        PQ("State two purposes of the UN as set out in the Charter.",
           "Maintaining international peace and security; developing friendly relations between nations; solving international economic and "
           "social problems; promoting human rights. Any two."),
        PQ("Explain how the veto works.",
           "A substantive decision needs nine votes of the fifteen members and no negative vote from any of the five permanent members. "
           "A single vote against by a permanent member blocks it."),
        PQ("Describe one way the UN worked round the Cold War veto.",
           "The Uniting for Peace resolution of 1950 let the General Assembly recommend action when the Council was blocked."),
        PQ("Give one argument for and one against Security Council reform.",
           "For: the Council reflects the world of 1945 and Africa lacks a permanent seat. Against: agreement on who should join is hard and "
           "more vetoes could slow decisions."),
        SUM("The UN Charter (signed 26 June 1945) aims at peace, friendly relations, cooperation and human rights.",
            "The Security Council has 15 members, five with a veto; the Assembly can only recommend.",
            "The veto limited action in the Cold War; Uniting for Peace was a partial answer.",
            "Reform proposals include more representation for Africa; the arguments need balanced treatment."),
    ],
))

# ---------------------------------------------------------------------------
# 18. Peacekeeping case studies
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="The United Nations",
    title="UN peacekeeping: Congo, the Balkans and Rwanda compared",
    slug="h7-un-peacekeeping-congo-balkans-rwanda",
    minutes=24,
    summary=("The principles of peacekeeping and three case studies: the UN operation in the Congo (1960 to 1964), UNPROFOR in "
             "Bosnia (1992 to 1995) and UNAMIR in Rwanda (1993 to 1996), with the explanations historians give for success and failure."),
    objectives=[
        "Explain the basic principles of peacekeeping and how it differs from enforcement",
        "Outline the UN operations in the Congo, the Balkans and Rwanda",
        "Explain why the UN failed to prevent mass killing in Srebrenica and Rwanda",
        "Evaluate arguments about what the UN, its members and its commanders could have done",
    ],
    key_concepts=["Peacekeeping", "Consent", "Impartiality", "ONUC", "UNPROFOR", "UNAMIR", "Srebrenica", "Genocide"],
    blocks=[
        H("Introduction"),
        T("Peacekeepers wear blue helmets and carry arms, but their job is not the same as that of an army at war. "
          "The United Nations has used them since 1948, and their record is mixed. This lesson studies three cases that are "
          "often used to test the UN's strengths and limits. They involve mass killing, so the focus is on documents and decisions."),
        D("**Peacekeeping** is the deployment of international personnel, usually with the consent of the parties, to monitor ceasefires "
          "and support peace. Its traditional principles are consent, impartiality and the use of force only in self-defence "
          "or defence of the mandate. **Enforcement** under Chapter VII uses force against a party without its consent.",
          title="Peacekeeping"),
        H("The Congo, 1960 to 1964"),
        T("After the Congo's independence in June 1960 and the mutiny and Katanga's secession, the UN Security Council authorised "
          "a force (ONUC) to help restore order and secure the withdrawal of Belgian troops. It grew to be the UN's largest "
          "operation of its time. In 1961 the mandate was widened to allow the use of force to prevent civil war and to remove foreign "
          "mercenaries. Secretary-General Dag Hammarskjold died in a plane crash in September 1961 on the way to talks; "
          "the cause is still debated. The operation ended in 1964, and Katanga's secession had ended in 1963."),
        H("Bosnia, 1992 to 1995"),
        T("As Yugoslavia broke apart, war began in Bosnia in 1992. A UN Protection Force (UNPROFOR) was sent to protect humanitarian aid "
          "and, in 1993, 'safe areas' were declared, including Srebrenica. The force was lightly armed and had a limited mandate. In July "
          "1995 forces of the Bosnian Serb army took Srebrenica and killed more than eight thousand men and boys. Courts, including the "
          "International Criminal Tribunal for the former Yugoslavia, have described these killings as genocide. NATO air strikes in "
          "1995 and the Dayton agreement later that year ended the war."),
        H("Rwanda, 1993 to 1994"),
        T("The UN Assistance Mission for Rwanda (UNAMIR) was set up in 1993 after the Arusha peace agreement. Its commander, "
          "General Romeo Dallaire, asked for stronger forces and a wider mandate. When the genocide began in April 1994, after the death "
          "of President Habyarimana in a plane crash, ten Belgian peacekeepers were killed and Belgium withdrew. In April "
          "the Security Council reduced UNAMIR to a small force. In June it authorised a French-led operation. The genocide ended in July "
          "1994 when the RPF took control. Estimates of those killed are in the hundreds of thousands, often given as about "
          "800,000 or more."),
        KEY("Why did the UN fail to prevent the killing?", "Historians point to several explanations.", cards=[
            ["Lack of political will", "Powerful members were unwilling to risk troops, and the memory of the failed operation in Somalia in 1993 weighed on decisions."],
            ["Mandate and resources", "Missions had limited mandates, few troops and weak equipment, and could not fight when attacked."],
            ["Structure of the UN", "The UN has no army of its own; it depends on states to send troops, and on the Security Council to agree."],
            ["Information and judgement", "Warnings were available in Rwanda, but they were not acted on. UN inquiries after 1999 criticised both the Secretariat and member states."],
        ]),
        EX("Model answer plan 1", intro="Why did UN peacekeeping fail to stop the genocide in Rwanda?", steps=[
            S("Mandate", text="UNAMIR was a traditional mission with limited force and could not intervene."),
            S("Political will", text="Key members were unwilling to send troops after Somalia. The Council cut the force in April 1994."),
            S("Resources", text="Too few troops and not enough equipment."),
            S("Judgement", text="A failure of decision-making by members and the Council, within a system that depends on them. Historians weigh these causes differently."),
        ]),
        EX("Model answer plan 2", intro="Compare the UN operations in the Congo and in Bosnia.", steps=[
            S("Similarities", text="Both were responses to the collapse of a state and both met difficulties in the use of force."),
            S("Differences", text="ONUC had a widened mandate that allowed force in 1961 and ended Katanga's secession; UNPROFOR's mandate was limited and its safe areas could not be defended."),
            S("Evidence", text="Katanga 1963; Srebrenica 1995."),
            S("Judgement", text="The Congo operation had a clearer, stronger mandate in the end, but both show the dependence of the UN on its members."),
        ]),
        MISTAKE("Saying the UN army killed civilians in Rwanda", "UNAMIR was a small mission that could not stop the genocide. Be accurate about who did what."),
        MISTAKE("Blaming the UN as one actor", "Distinguish the Secretariat, the Security Council and member states."),
        QUIZ("Which of these is a traditional principle of peacekeeping?",
             ["Use of force to defeat one party", "Consent of the parties and impartiality", "Control of the territory by the UN", "Permanent occupation"], 1,
             "Consent, impartiality and minimal use of force are traditional principles.",
             feedback=["That would be enforcement.", "", "Peacekeepers do not take control.", "Missions are temporary."]),
        QUIZ("Which UN mission was commanded by General Romeo Dallaire?",
             ["ONUC", "UNPROFOR", "UNAMIR", "UNEF"], 2,
             "Dallaire commanded UNAMIR in Rwanda.",
             feedback=["ONUC was the Congo operation.", "UNPROFOR operated in the former Yugoslavia.", "", "UNEF was the force of 1956 after Suez."]),
        H("Practice questions"),
        PQ("Explain the difference between peacekeeping and enforcement.",
           "Peacekeeping depends on the consent of the parties and uses force only in self-defence. Enforcement under Chapter VII uses force "
           "against a party without its consent."),
        PQ("Describe the role of the UN in the Congo between 1960 and 1964.",
           "A force (ONUC) was sent to restore order and secure Belgian withdrawal; its mandate was widened in 1961 to allow force; "
           "Katanga's secession ended in 1963; the operation withdrew in 1964. Hammarskjold died in 1961."),
        PQ("Give two reasons why the UN was unable to protect Srebrenica.",
           "UNPROFOR had a limited mandate and few lightly armed troops; the Security Council and members were unwilling to authorise stronger force in time."),
        PQ("Essay plan: 'The UN failed in Rwanda because of its members, not because of its structure.' Discuss.",
           "For: members refused to send troops and the Council cut UNAMIR. Against: structure (no army, dependence on consent and on the Council, "
           "limited mandates). Judgement: the two are linked, since the structure puts decisions in the hands of members."),
        SUM("Peacekeeping rests on consent, impartiality and minimal force; enforcement is under Chapter VII.",
            "ONUC (1960 to 1964), UNPROFOR (1992 to 1995) and UNAMIR (1993 to 1994) are the three cases.",
            "Srebrenica (1995) and Rwanda (1994) showed the limits of mandates, resources and political will.",
            "Distinguish the Secretariat, the Council and member states when assigning responsibility."),
    ],
))

# ---------------------------------------------------------------------------
# 19. Regional integration
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="Regional integration",
    title="From the OAU to the African Union, and the regional communities: ECOWAS, CEMAC and SADC",
    slug="h7-reg-oau-au-ecowas-cemac-sadc",
    minutes=24,
    summary=("The OAU of 1963, its principles and record, the African Union of 2002, and the regional economic communities "
             "ECOWAS, CEMAC and SADC, with the successes, the limits and the world after 1991."),
    objectives=[
        "Describe the founding of the OAU in 1963 and its principles",
        "Explain why the OAU was replaced by the African Union and what changed",
        "Describe the aims and record of ECOWAS, CEMAC and SADC",
        "Evaluate the obstacles to regional integration in Africa",
    ],
    key_concepts=["Pan-Africanism", "OAU", "Non-interference", "African Union", "Peace and Security Council", "ECOWAS", "CEMAC", "SADC"],
    blocks=[
        H("Introduction"),
        T("A trader in Douala who sells goods to Chad or the Central African Republic crosses borders drawn in the colonial "
          "period. Regional bodies try to make such trade easier and to prevent conflict between states. This lesson follows "
          "the continental effort and the regional ones."),
        IMG("al-h7-african-integration.svg",
            alt="Diagram: OAU replaced by the African Union, with the regional communities ECOWAS, CEMAC and SADC below",
            caption="Figure 1. Continental and regional bodies (schematic)."),
        H("The OAU, 1963 to 2002"),
        T("The Organisation of African Unity was founded in Addis Ababa on 25 May 1963 by 32 independent states. "
          "It followed a debate between states that wanted a quick political union (such as Nkrumah's Ghana, in the so-called "
          "Casablanca group) and those that preferred a looser association (the Monrovia group). The Charter chose the loose form."),
        D("The OAU Charter stressed the **sovereign equality** of members, **non-interference** in their internal affairs, respect for existing "
          "borders (confirmed by a resolution of 1964), peaceful settlement of disputes, and support for the liberation of colonies "
          "still under foreign rule.", title="OAU principles"),
        T("The OAU created a Liberation Committee based in Dar es Salaam to support the movements in southern Africa, "
          "and it helped to isolate apartheid South Africa. It mediated some border disputes. Its record on internal "
          "conflicts and abuses was weaker, because the principle of non-interference limited action, as in the Biafran war and the "
          "Rwandan genocide of 1994. The African Charter on Human and Peoples' Rights was adopted in 1981 (in force 1986)."),
        H("The African Union"),
        T("In 1999 leaders at Sirte agreed to create a new body. The Constitutive Act was adopted at Lome in 2000, came into force "
          "in 2001 and the African Union was launched at Durban in July 2002. The Act keeps sovereign equality but also provides for the "
          "Union's right to intervene in a member state in grave circumstances, such as war crimes, genocide and crimes against humanity, "
          "and rejects unconstitutional changes of government. A Peace and Security Council began work in 2004. The AU has "
          "also adopted long-term development plans (check your textbook for NEPAD and Agenda 2063)."),
        KEY("OAU and AU compared", "A standard essay theme.", cards=[
            ["OAU", "Non-interference; priority on decolonization and borders; a small secretariat."],
            ["AU", "Sovereignty with a right of intervention in grave cases; a Peace and Security Council; more attention to economic integration and governance."],
            ["Common problem", "Limited funds and the reluctance of member states to give up powers."],
        ]),
        H("Regional communities"),
        KEY("Three examples", "Know the date of the treaty and one achievement or problem.", cards=[
            ["ECOWAS", "Treaty of Lagos, 1975. West African states. Free movement and trade aims; a military force (ECOMOG) intervened in Liberia from 1990 and "
             "in Sierra Leone. Recent withdrawals of some members are a recent development (check your textbook)."],
            ["CEMAC", "The Economic and Monetary Community of Central Africa, created by a treaty of 1994 and operating from 1999, "
             "succeeding the older customs union UDEAC. Six members: Cameroon, Central African Republic, Chad, Congo, Equatorial Guinea and Gabon. "
             "It has a common currency, the CFA franc, issued by the regional bank, and aims at free movement and trade, although progress is slow."],
            ["SADC", "Began in 1980 as the SADCC to reduce dependence on apartheid South Africa; became SADC by a treaty of 1992; South Africa joined in 1994."],
        ]),
        T("Obstacles include poor transport links, similar export products that do not trade with each other, overlapping "
          "memberships, weak enforcement of agreements, and political conflict. The AfCFTA, an agreement to create a continental "
          "free trade area, was signed in 2018 and began trading in 2021 (check your textbook)."),
        H("After 1991"),
        T("The end of the Cold War reduced superpower support for African rulers and brought pressure for multiparty politics "
          "and economic reform. Apartheid ended in 1994. New conflicts, such as the Rwandan genocide, raised the question of "
          "outside intervention. These changes helped create the AU and give regional bodies a greater role in peace and security."),
        EX("Model answer plan 1", intro="Why was the OAU replaced by the African Union?", steps=[
            S("Success", text="The OAU's main aim of decolonization was largely achieved by 1994."),
            S("Weakness", text="The principle of non-interference limited action on internal conflicts and abuses."),
            S("New conditions", text="The end of the Cold War, globalisation and conflicts such as Rwanda raised new demands."),
            S("Judgement", text="The AU responded with a right of intervention and new organs. How far it changed practice is debated."),
        ]),
        EX("Model answer plan 2", intro="Assess the obstacles to economic integration in CEMAC.", steps=[
            S("Structure", text="Similar export economies based on oil and raw materials, so little trade between members."),
            S("Infrastructure", text="Poor roads and rail links between capitals."),
            S("Implementation", text="Agreements on free movement have not been fully applied."),
            S("Judgement", text="A shared currency exists, but trade and movement remain below the aims. Political will and infrastructure are central."),
        ]),
        MISTAKE("Dating the AU to 1963", "The OAU was founded in 1963. The African Union was launched in 2002."),
        MISTAKE("Listing Cameroon among ECOWAS members", "Cameroon belongs to CEMAC, in Central Africa."),
        QUIZ("Which principle of the OAU Charter limited intervention in members' internal affairs?",
             ["Pan-Africanism", "Non-interference", "Collective security", "Free movement"], 1,
             "Non-interference protected members' sovereignty but limited action on internal conflicts.",
             feedback=["Pan-Africanism was the broad idea of unity.", "", "The OAU had weak collective security arrangements.", "Free movement is an aim of regional communities."]),
        QUIZ("Which regional community has Cameroon as a member?",
             ["ECOWAS", "SADC", "CEMAC", "SADCC"], 2,
             "Cameroon belongs to CEMAC, the community of Central Africa.",
             feedback=["ECOWAS is in West Africa.", "SADC is in southern Africa.", "", "SADCC was the earlier form of SADC."]),
        H("Practice questions"),
        PQ("State two principles of the OAU Charter.",
           "Sovereign equality of members, non-interference in internal affairs, respect for existing borders, peaceful settlement of disputes, "
           "support for decolonization. Any two."),
        PQ("Explain two differences between the OAU and the AU.",
           "The AU allows intervention in grave circumstances while the OAU stressed non-interference; the AU has a Peace and Security Council and "
           "pays more attention to economic integration and governance."),
        PQ("Describe the aims and one problem of CEMAC.",
           "It aims at economic and monetary cooperation with a common currency and free trade and movement among six central African states. Problems "
           "include slow implementation, poor infrastructure and similar economies."),
        PQ("Essay plan: 'Regional integration in Africa has achieved little.' Discuss.",
           "Achieved: ECOWAS peace efforts, SADC's role after apartheid, the AU's new organs, common currency in CEMAC. Little: low trade between members, "
           "overlapping memberships, weak enforcement. Judgement: stronger in peace and politics than in trade."),
        SUM("The OAU (1963) stressed sovereignty, non-interference and decolonization; the AU (2002) allows intervention in grave cases.",
            "ECOWAS (1975), CEMAC (treaty 1994) and SADC (1992) are regional communities; Cameroon is in CEMAC.",
            "Integration faces infrastructure, similar economies, overlapping memberships and political problems.",
            "After 1991 new pressures helped create the AU and enlarged the role of regional bodies."),
    ],
))

# ---------------------------------------------------------------------------
# 20. Exam lesson
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_EX,
    topic="Practice paper",
    title="Approaching the History practice paper: multiple choice, sources and essay planning",
    slug="h7-exam-approaching-practice-paper",
    minutes=20,
    summary=("How to use the KKEVO History practice paper: reading questions, handling source extracts, planning your time (KKEVO "
             "advice) and linking your revision to the topics of the year."),
    objectives=[
        "Read a multiple-choice question and remove wrong options by reasoning",
        "Use a short routine for source-based questions",
        "Plan time for the practice paper and for essays in the real exam",
        "Use the score by topic to plan revision",
    ],
    key_concepts=["Multiple choice", "Source evaluation", "Provenance", "Time planning", "Essay plan", "Revision by topic"],
    blocks=[
        H("Introduction"),
        T("The KKEVO practice paper has 40 multiple-choice questions across all the topics of Upper Sixth History. "
          "It tests knowledge and source interpretation. It cannot mark essays, so it is a supplement and not a replacement for "
          "writing practice. The real paper format and marking should be checked with your teacher. The timings below are KKEVO "
          "practice settings, not official ones."),
        H("Reading a multiple-choice question"),
        KEY("A four-step routine", "Use it every time.", cards=[
            ["1. Read the stem", "Underline dates, names and key words such as 'except' or 'main'."],
            ["2. Predict", "Think of the answer before reading the options."],
            ["3. Remove", "Cross out options with wrong dates, wrong people or wrong places."],
            ["4. Check", "Re-read the stem. Does your option answer this exact question?"],
        ]),
        EX("Worked example", intro="Which body supervised the plebiscites held in the British Cameroons in 1959 to 1961?", steps=[
            S("Stem", text="The key words are 'supervised' and 'British Cameroons'."),
            S("Predict", text="An international body, not a colonial one: the United Nations."),
            S("Remove", text="The OAU did not exist until 1963. The Trusteeship Council is a part of the UN but the General Assembly set the plebiscite terms. The French government had no role in the British Cameroons."),
            S("Answer", text="The United Nations."),
        ]),
        H("Source questions"),
        T("Use PEC: **P**rovenance (who, when, why), **E**vidence (what does it say, and what can you infer), **C**ross-check (what other "
          "sources would help). Remember that the practice paper uses invented illustrative texts, never real quotations."),
        T("Illustrative source (invented for practice): 'The leaders have promised that the rights of our people will be "
          "respected. We hope they will keep their word.' (A newspaper editorial from the period of a constitutional change.)",
          title="Illustrative source"),
        T("P: a newspaper editorial, written to give an opinion, with a possible bias. E: shows hope and some doubt, and no hard facts. "
          "C: compare with the text of the constitution and with later events."),
        H("Planning your time (KKEVO advice)"),
        T("For a 90-minute paper with 40 questions, about two minutes a question leaves about ten minutes to check. If you "
          "are stuck, mark the question and move on. Do not leave blanks if there is no penalty for wrong answers, but check "
          "this with your teacher."),
        T("For essays in the real exam, spend the first few minutes on a plan: a line for each paragraph, with one date or name as "
          "evidence. Write a judgement in the last paragraph. Compare with the model answer plans in the lessons."),
        H("Using your results"),
        T("After the practice paper the results page shows your score by topic. Revise the weakest topic first, using "
          "its lessons and practice sets. Retake the topic set before you try the paper again."),
        MISTAKE("Spending too long on one hard question", "Mark it and return. Easy marks later in the paper are lost if you run out of time."),
        MISTAKE("Choosing an option because it sounds familiar", "Check that it answers this exact question. Wrong options often contain true facts from other topics."),
        QUIZ("In a source question, what does 'provenance' mean?",
             ["The content of the source", "Who produced it, when and why", "The number of words", "Whether you agree with it"], 1,
             "Provenance is the origin and purpose of the source.",
             feedback=["That is the content.", "", "Length is not provenance.", "Agreement is an opinion, not a judgement of the source's origin."]),
        QUIZ("You find a question you cannot answer after a minute. What should you do?",
             ["Stay until you find it", "Mark it, move on and come back", "Guess without reading the options", "Leave the paper"], 1,
             "Marking and moving on saves time for questions you can answer.",
             feedback=["This risks leaving other questions unfinished.", "", "Reading the options may help you eliminate some.", "Never leave the paper unfinished."]),
        H("Practice questions"),
        PQ("Describe the four-step routine for a multiple-choice question.",
           "Read the stem and underline key words; predict an answer; remove wrong options; check that the remaining option answers the exact question."),
        PQ("What three things should you note when evaluating a source?",
           "Provenance (who, when, why), what the evidence says and what can be inferred, and which other sources could be used to cross-check it."),
        PQ("Plan your time for a 40-question, 90-minute practice paper (KKEVO advice).",
           "About 2 minutes a question, which makes about 80 minutes, leaving about 10 minutes to check. Mark hard questions and return."),
        PQ("How should you use the score by topic after a mock?",
           "Identify the weakest topics, revise their lessons, retake the topic practice set, then retry the paper."),
        SUM("Use a four-step routine for multiple choice: read, predict, remove, check.",
            "For sources use provenance, evidence, cross-check.",
            "Plan time (KKEVO advice: about two minutes a question) and check your real format with your teacher.",
            "Use the score by topic to decide what to revise first."),
    ],
))
