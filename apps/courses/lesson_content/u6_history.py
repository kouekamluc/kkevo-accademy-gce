"""Upper Sixth History (A Level 0760, Year 2): draft lessons for reviewer checking.

Contested Cameroonian topics are presented with differing interpretations side by side.
Reviewers: check every date and name against the GCE Board syllabus and standard texts.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "upper-sixth")

M_CMR = "Cameroon 1945 to Today"
M_DEC = "Decolonization in Africa"
M_CW = "Cold War & International Governance"

LESSONS = []

# ---------------------------------------------------------------------------
# 1. Trusteeship and decolonization
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Trusteeship and decolonization",
    title="French Cameroun under UN trusteeship: the UPC, the insurrection and Ahidjo's rise",
    slug="trusteeship-and-decolonization",
    minutes=30,
    summary=("How UN trusteeship shaped decolonization in French Cameroun, 1946 to 1960: visiting missions "
             "and petitions, the UPC, the armed conflict and its repression, and the rise of Ahmadou Ahidjo."),
    objectives=[
        "Explain how the trusteeship system differed from ordinary colonial rule",
        "Describe the aims and methods of the UPC between 1948 and 1960",
        "Outline the causes and course of the insurrection and the French pacification campaign",
        "Explain how Ahmadou Ahidjo came to lead Cameroun to independence in 1960",
        "Compare historians' interpretations of the UPC and of the 1960 independence settlement",
    ],
    key_concepts=["Trusteeship", "UN Visiting Mission", "Petition", "UPC", "Pacification", "Reunification"],
    blocks=[
        H("Introduction"),
        T("After the Second World War, the former German Kamerun was no longer a League of Nations mandate. "
          "In December 1946 the United Nations approved trusteeship agreements that left the larger eastern part "
          "under French administration and the western strip under British administration."),
        T("Trusteeship mattered because it gave Cameroonians a voice outside the colonial power. They could write "
          "petitions to the UN, meet UN visiting missions and even speak in New York. This lesson follows how that "
          "opportunity was used, how a radical nationalist movement was defeated by force, and how a moderate "
          "leader, Ahmadou Ahidjo, took Cameroun to independence on 1 January 1960."),
        D("A **trust territory** was a territory administered by a member state on behalf of the United Nations. "
          "Article 76 of the UN Charter required the administering power to promote progress towards "
          "self-government or independence.", title="Trusteeship"),
        D("The **Union des Populations du Cameroun (UPC)** was founded in Douala in April 1948. Its best-known "
          "leaders were Ruben Um Nyobè, Félix-Roland Moumié, Ernest Ouandié and Abel Kingué. Its two central demands "
          "were the reunification of the British and French Cameroons and independence on a fixed timetable.",
          title="UPC"),
        D("**Pacification** was the official French term for the military and administrative campaign against the "
          "UPC maquis, notably in the Sanaga-Maritime from late 1957 and later in the Bamileke region.",
          title="Pacification"),

        H("Trusteeship machinery: missions and petitions"),
        T("The UN Trusteeship Council sent visiting missions to the Cameroons, generally every three years "
          "(1949, 1952, 1955 and 1958). Missions toured the territory, met chiefs, parties and associations, and "
          "reported back to the Council. Cameroonians sent thousands of petitions to the UN, many of them organised by the UPC. Petitions "
          "complained about forced labour, land, taxation and the slow pace of political reform."),
        T("Ruben Um Nyobè addressed the UN Fourth Committee in New York in December 1952, and again in later "
          "sessions. He argued that France was treating Cameroun as a colony rather than as a trust territory "
          "heading for independence."),
        KEY("Trust territory or colony?", "France and the UPC read trusteeship in opposite ways.", cards=[
            ["French position", "Cameroun was an associated territory linked to the French Union. Reform should be "
             "gradual, and independence was not a fixed goal in the short term."],
            ["UPC position", "The Charter promised self-government or independence. France had no right to fold "
             "Cameroun into the French Union, and a timetable should be set."],
        ], note="This legal disagreement explains why the UPC put so much effort into the UN."),

        H("From ban to insurrection, 1955 to 1958"),
        T("In May 1955 violent clashes broke out in several towns, including Douala and Yaoundé. The French "
          "authorities blamed the UPC, and the party was banned by decree in July 1955. Many leaders fled to "
          "British Southern Cameroons and, after their expulsion from there in 1957, into exile in Africa."),
        T("The 1956 Loi-Cadre reforms led to elections to a new territorial assembly in December 1956. The banned "
          "UPC could not take part and called for a boycott. Armed resistance began in the Sanaga-Maritime around "
          "the same time."),
        T("In 1957 André-Marie Mbida became the first Prime Minister of the autonomous State under Trusteeship, "
          "with Ahmadou Ahidjo as deputy. Mbida lost French support and resigned in February 1958, and Ahidjo, a "
          "northern politician of the Union Camerounaise, replaced him. Um Nyobè was killed by French-led troops in the Sanaga-Maritime forest on 13 September 1958. The "
          "conflict then shifted, with a growing maquis in the Bamileke region and the Mungo, which continued "
          "after independence."),

        H("Independence and the continuing conflict"),
        T("In March 1959 the UN General Assembly agreed to end trusteeship over French Cameroun on 1 January "
          "1960 without first holding new elections under UN supervision, which the UPC and its allies had "
          "demanded. Independence came on that date, with Ahidjo as head of government and, from May 1960, "
          "President. Moumié died in Geneva in November 1960 after being poisoned; the killing is widely attributed to "
          "French secret service agents. Ouandié led the remaining maquis until his capture and execution in "
          "January 1971. The number of people killed in the whole conflict is not known and estimates vary very "
          "widely."),
        KEY("How have historians interpreted the UPC and 1960?", "Read the debate, then weigh the evidence yourself.", cards=[
            ["Nationalist and critical view", "Writers such as Richard Joseph, and later Deltombe, Domergue and "
             "Tatsitsa, see the UPC as the authentic national movement, crushed by a French war, so that power "
             "passed to leaders acceptable to France."],
            ["Official and moderate view", "Ahidjo's supporters stressed that Cameroun gained independence "
             "peacefully through negotiation and the UN, and that order and unity required ending an armed revolt."],
            ["Social-history view", "Historians such as Achille Mbembe and Meredith Terretta stress local "
             "grievances, memory and international networks, not only party leaders."],
        ], note="A strong answer names the view, gives evidence for it, and judges its limits."),

        EX("Essay plan 1", intro=("How far was the UN trusteeship system responsible for the pace of decolonization "
                                   "in French Cameroun between 1946 and 1960?"), steps=[
            S("Argument: trusteeship gave nationalists an international platform",
              text="Charter Article 76 promised self-government; petitions and Um Nyobè's 1952 speech kept Cameroun on the UN agenda."),
            S("Evidence: UN pressure and French reform",
              text="Visiting missions reported regularly; the 1956 Loi-Cadre and 1957 autonomy came partly in response to international scrutiny."),
            S("Counter-argument: French policy and the wider empire mattered more",
              text="Loi-Cadre applied across French Africa; France set the pace and chose which leaders to work with after banning the UPC in 1955."),
            S("Counter-argument: armed conflict and local politics",
              text="The insurrection from 1956 and Ahidjo's alliance with France shaped the timing and the form of independence."),
            S("Judgement",
              text="Trusteeship made independence a fixed legal goal and helped speed it up, but France decided who inherited power; the UN accepted 1 January 1960 without new elections."),
        ]),
        EX("Essay plan 2", intro="Assess the reasons why the UPC failed to take power at independence in 1960.", steps=[
            S("Argument: French repression",
              text="The 1955 ban, exile of leaders and the pacification campaign removed the UPC from legal politics."),
            S("Evidence: loss of leaders",
              text="Um Nyobè killed in 1958; leaders in exile were divided and far from the maquis."),
            S("Argument: strength of rivals",
              text="Ahidjo built a base in the north and won the support of France and of many southern politicians."),
            S("Counter-argument: UPC's own choices",
              text="The boycott of the December 1956 elections left the assembly to its rivals; some historians see this as a tactical error, others as unavoidable."),
            S("Judgement",
              text="Repression was the decisive factor, but UN acceptance of independence without new elections and the UPC's internal divisions sealed the outcome."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling French Cameroun a colony without qualification",
                "Legally it was a UN trust territory. Examiners reward students who explain why that status mattered."),
        MISTAKE("Saying the conflict ended at independence",
                "Fighting continued into the 1960s; Ouandié was executed only in 1971."),
        MISTAKE("Giving casualty figures as facts",
                "Estimates differ greatly. Say that numbers are disputed rather than quoting one figure."),
        QUIZ("Who replaced André-Marie Mbida as Prime Minister in February 1958?",
             ["Ruben Um Nyobè", "Ahmadou Ahidjo", "John Ngu Foncha", "Félix-Roland Moumié"], 1,
             "Ahidjo, Mbida's deputy, became Prime Minister in February 1958 and led Cameroun to independence.",
             hint="He was a northern politician of the Union Camerounaise.",
             feedback=["Um Nyobè led the banned UPC and was in the maquis.", "",
                       "Foncha was a Southern Cameroons politician (KNDP).", "Moumié was a UPC leader in exile."]),
        QUIZ("Why did the UPC take its case to the United Nations?",
             ["Cameroun was a UN trust territory with a Charter promise of self-government",
              "The UN governed Cameroun directly", "France had left Cameroun in 1948",
              "The UN had banned the UPC"], 0,
             "Trusteeship gave petitioners legal standing and a promise of progress towards self-government or independence.",
             feedback=["", "The UN supervised; France administered.", "France administered until 1960.",
                       "France, not the UN, banned the UPC in 1955."]),
        H("Practice questions"),
        PQ("Essay: 'The decolonization of French Cameroun was shaped more by violence than by negotiation.' Discuss.",
           "Outline: for violence, the 1955 ban, maquis from 1956, pacification, death of Um Nyobè 1958; against, "
           "Loi-Cadre, 1957 autonomy, negotiated transfer to Ahidjo, UN vote of 1959. Judgement: both mattered; "
           "violence decided who would rule, negotiation decided the timing and the legal form."),
        PQ("Essay: Assess the role of UN visiting missions and petitions in the Cameroonian nationalist movement.",
           "Outline: missions of 1949, 1952, 1955, 1958; petitions as mass political education; Um Nyobè at the "
           "Fourth Committee; limits: the UN could recommend but not compel, and it accepted independence without "
           "new elections. Judgement: important for publicity and legitimacy, weak as a means of power."),
        PQ("Source-style: A historian argues that independence in 1960 was 'granted to the moderates'. Explain "
           "what this means and how far the evidence supports it.",
           "Explain: power passed to Ahidjo, who cooperated with France, while the radical UPC was banned and "
           "fighting. Support: 1955 ban, 1958 change of premier, 1959 UN decision. Limits: Ahidjo had real "
           "domestic support, especially in the north, and moderates also pushed for independence."),
        SUM("Trusteeship (1946) promised progress towards self-government and let Cameroonians petition the UN.",
            "The UPC (1948) demanded reunification and independence and used the UN intensively.",
            "The UPC was banned in 1955; an armed conflict followed from 1956 and was met with French 'pacification'.",
            "Ahidjo became Prime Minister in 1958 and led Cameroun to independence on 1 January 1960.",
            "Historians disagree about whether 1960 was a genuine liberation or a transfer to France's chosen partners."),
    ],
))

# ---------------------------------------------------------------------------
# 2. Southern Cameroons politics
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="Southern Cameroons politics",
    title="Southern Cameroons politics: parties, conferences, the 1961 plebiscite and Foumban",
    slug="southern-cameroons-politics",
    minutes=30,
    summary=("Party politics in British Southern Cameroons from the 1950s: KNC, KNDP and OK, the road to separate "
             "regional status, the Mamfe conference, the 1961 plebiscite and the Foumban constitutional conference."),
    objectives=[
        "Identify the main Southern Cameroons parties and their leaders and aims",
        "Explain how Southern Cameroons moved from Nigerian administration to its own government",
        "Describe the plebiscite questions of 1961 and the results in the Northern and Southern Cameroons",
        "Assess the Foumban conference and the competing interpretations of it",
    ],
    key_concepts=["KNC", "KNDP", "One Kamerun (OK)", "Plebiscite", "Foumban conference", "Federation"],
    blocks=[
        H("Introduction"),
        T("British Cameroons was governed as part of Nigeria. Its southern part had its own politics, its own "
          "leaders and its own debates about the future: stay with Nigeria, reunite with French-speaking "
          "Cameroun, or seek a separate future. The choices made between 1953 and 1961 still shape debate in "
          "Cameroon today, so this topic needs particular care and balance."),
        D("A **plebiscite** is a direct vote by the people of a territory on a single question about its future, "
          "here organised under United Nations supervision in February 1961.", title="Plebiscite"),
        D("The **Kamerun National Congress (KNC)**, led by Dr E. M. L. Endeley, was formed in 1953. The **Kamerun "
          "National Democratic Party (KNDP)**, led by John Ngu Foncha, broke away in 1955. **One Kamerun (OK)**, "
          "led by Ndeh Ntumazah, was founded in 1957 and was close to the UPC.", title="Main parties"),

        H("From Nigerian region to separate government"),
        T("In 1953 Southern Cameroons members of the Eastern Nigerian House of Assembly, led by Endeley, broke "
          "with the governing party during a regional crisis and demanded separate treatment for the Cameroons."),
        T("The 1954 Nigerian constitution gave Southern Cameroons its own House of Assembly at Buea, with Endeley "
          "as Leader of Government Business. Further constitutional conferences on Nigeria held in London in the "
          "later 1950s, including at Lancaster House in 1957, widened its self-government, and Endeley became "
          "Premier in 1958."),
        T("The KNC came to favour close association with Nigeria. The KNDP favoured separation from Nigeria and, "
          "increasingly, reunification with Cameroun. In the January 1959 elections the KNDP won a narrow "
          "majority and Foncha became Premier. OK campaigned for immediate reunification and independence and "
          "remained a smaller force."),
        KEY("What did the parties want?", "Positions changed over time, so date your claims.", cards=[
            ["KNC / CPNC (Endeley)", "Initially open to reunification, later closer ties with Nigeria; joined "
             "P. M. Kale's KPP to form the CPNC in 1960."],
            ["KNDP (Foncha)", "Secession from Nigeria; reunification with Cameroun, generally imagined as a "
             "loose federation."],
            ["OK (Ntumazah)", "Radical reunification and independence; linked to the UPC."],
        ]),

        H("Mamfe and the plebiscite questions"),
        T("At the Mamfe conference in August 1959 Southern Cameroons leaders failed to agree on the plebiscite "
          "questions or on who should be allowed to vote. The United Nations then decided the matter itself."),
        T("The UN set two options: achieve independence by joining the independent Federation of Nigeria, or by "
          "joining the independent Republic of Cameroun. Separate independence was not offered. Whether it should "
          "have been is still debated."),
        T("Plebiscites were held in February 1961. Northern Cameroons voted to join Nigeria and became part of it "
          "on 1 June 1961. Southern Cameroons voted clearly, by roughly seven votes in ten, to join the Republic of "
          "Cameroun. Cameroun challenged the northern result, and the International Court of Justice declined to "
          "rule on the substance in 1963."),

        H("The Foumban conference and reunification"),
        T("Delegates from Cameroun and Southern Cameroons met at Foumban in July 1961 to discuss a federal "
          "constitution. The Cameroun side, led by President Ahidjo, presented a draft; the Southern Cameroons "
          "delegation, led by Foncha, put forward amendments. The Federal Republic of Cameroon was born on "
          "1 October 1961, with two federated states, East Cameroon and West Cameroon. Ahidjo became Federal "
          "President and Foncha Vice-President."),
        KEY("Interpreting Foumban", "This is one of the most debated events in Cameroonian history.", cards=[
            ["Imposed-settlement view", "Some writers argue the draft was prepared in advance with French advisers, "
             "the Southern Cameroons team was small and under-prepared, and few of its amendments were accepted, "
             "creating a centralised federation."],
            ["Negotiated-settlement view", "Others stress that Southern Cameroons leaders took part, accepted the "
             "outcome, and that a federation with its own West Cameroon institutions was created as promised."],
            ["Contextual view", "Many historians point to unequal bargaining power: a sovereign state facing a "
             "trust territory whose future had already been decided by the plebiscite."],
        ], note="Present each view with its evidence; do not treat one as obvious."),

        EX("Essay plan 1", intro="Why did Southern Cameroons vote to join the Republic of Cameroun in 1961?", steps=[
            S("Argument: fear of Nigerian domination",
              text="Memories of the 1953 Eastern Region crisis and resentment of Nigerian influence in trade and administration pushed many towards Cameroun."),
            S("Argument: KNDP organisation and leadership",
              text="The KNDP had won the 1959 election and campaigned effectively for reunification."),
            S("Argument: historic and cultural ties",
              text="The shared German Kamerun past and the reunification idea long promoted by nationalists."),
            S("Counter-argument: the limited choice",
              text="No independence option was offered; some votes may have been against Nigeria rather than for Cameroun."),
            S("Judgement",
              text="Anti-Nigerian feeling and KNDP organisation were decisive, but the UN's two-option ballot framed the outcome."),
        ]),
        EX("Essay plan 2", intro="'The Foumban conference was a meeting of unequal partners.' How far do you agree?", steps=[
            S("Argument: inequality of status",
              text="Cameroun had been sovereign since 1960; Southern Cameroons was still a trust territory."),
            S("Evidence: preparation and drafting",
              text="The working draft came from the Cameroun side; the Southern Cameroons delegation proposed amendments."),
            S("Counter-argument: real concessions and consent",
              text="A federal structure with a West Cameroon government, House of Assembly and House of Chiefs was kept; Southern leaders accepted the result."),
            S("Counter-argument: Southern Cameroons divisions",
              text="KNDP and CPNC disagreements weakened the Southern position."),
            S("Judgement",
              text="Largely agree on inequality of bargaining power, while recognising that Southern leaders took part and that historians weigh the outcome differently."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying all of British Cameroons joined Cameroun",
                "Only Southern Cameroons did. Northern Cameroons joined Nigeria in June 1961."),
        MISTAKE("Mixing up party positions",
                "The KNDP led the reunification side; the KNC/CPNC leaned towards Nigeria. Date your statements."),
        MISTAKE("Treating the debate on Foumban as settled",
                "Examiners reward balanced use of interpretations, not a one-sided verdict."),
        QUIZ("Which options did the UN place on the 1961 Southern Cameroons plebiscite ballot?",
             ["Independence or union with Nigeria", "Union with Nigeria or union with the Republic of Cameroun",
              "Remaining under British trusteeship or independence", "Union with Cameroun or union with Gabon"], 1,
             "Voters chose between joining Nigeria and joining the Republic of Cameroun; separate independence was not offered.",
             feedback=["Independence was not an option on the ballot.", "",
                       "Trusteeship was ending; continuing it was not offered.", "Gabon was never an option."]),
        H("Practice questions"),
        PQ("Essay: Compare the roles of Endeley and Foncha in Southern Cameroons politics, 1953 to 1961.",
           "Outline: Endeley led the 1953 break with the Eastern Region, became Leader of Government Business and "
           "Premier, later favoured Nigeria; Foncha founded the KNDP in 1955, won in 1959, led the reunification "
           "campaign and the Foumban delegation. Judgement: Endeley won separate status; Foncha shaped the final outcome."),
        PQ("Essay: Was the absence of an independence option in 1961 a decisive factor in the future of Southern Cameroons?",
           "Outline: UN decision after the Mamfe deadlock; arguments about economic viability; supporters of a third "
           "option then and later; counter: strong existing support for reunification. Judgement must weigh both "
           "and note that historians disagree."),
        PQ("Source-style: Explain the significance of the Mamfe conference of August 1959.",
           "Leaders failed to agree on questions and voter eligibility, so the UN set the terms itself, removing "
           "the choice of options from Southern Cameroons politicians."),
        SUM("Southern Cameroons gained its own assembly in 1954 and moved towards full self-government.",
            "KNC (Endeley) leaned to Nigeria, KNDP (Foncha) to reunification, OK (Ntumazah) to radical reunification.",
            "After Mamfe (1959) the UN fixed two plebiscite options, without independence.",
            "In February 1961 the north joined Nigeria and the south voted to join Cameroun.",
            "Foumban (July 1961) led to the federation of 1 October 1961; its fairness is still debated."),
    ],
))

# ---------------------------------------------------------------------------
# 3. The post-colonial state
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR,
    topic="The post-colonial state",
    title="The post-colonial Cameroonian state: from federation to the 1996 constitution",
    slug="the-post-colonial-state",
    minutes=30,
    summary=("Cameroon from 1961 to 1996: the federal system and its replacement by a unitary state, the single "
             "party (CNU, then CPDM), the 1982 transition, the political liberalization of the 1990s and the 1996 constitution."),
    objectives=[
        "Describe how the federal state of 1961 became the unitary state of 1972",
        "Explain the creation of the single party in 1966 and its renaming as the CPDM in 1985",
        "Outline the 1982 transition from Ahidjo to Biya and the crisis that followed",
        "Explain the causes and results of political liberalization in the 1990s",
        "Summarise the main provisions of the 1996 constitution and the federalism versus unitarism debate",
    ],
    key_concepts=["Federalism", "Unitary state", "Single party", "CNU", "CPDM", "Liberalization", "Decentralization"],
    blocks=[
        H("Introduction"),
        T("Reunification in 1961 created a federal state joining two territories with different colonial "
          "languages, laws and administrative traditions. How power should be shared between the centre and "
          "the regions has been a central question ever since. This lesson follows the main constitutional and "
          "political changes up to 1996 and sets out the debates fairly."),
        D("In a **federation**, powers are divided by the constitution between a central government and "
          "regional (federated) governments. In a **unitary state**, sovereignty rests with the central government, "
          "which may delegate powers to local bodies.", title="Federalism and unitarism"),
        D("The **Cameroon National Union (CNU, in French UNC)** was the single party formed in September 1966. "
          "In 1985, at its Bamenda congress, it was renamed the **Cameroon People's Democratic Movement (CPDM, in "
          "French RDPC)**.", title="CNU and CPDM"),

        H("The federal years, 1961 to 1972"),
        T("Under the 1961 constitution the Federal Republic had a federal government in Yaoundé and two federated "
          "states, East Cameroon and West Cameroon, each with its own government and assembly. Important powers "
          "such as defence, foreign affairs, finance and security were federal from the start."),
        T("In 1966 the main parties of both states, including the Union Camerounaise and the KNDP, merged into "
          "the CNU. Cameroon became a de facto one-party state. Supporters said this ended ethnic and regional "
          "division; critics said it removed political competition."),
        T("On 20 May 1972 a referendum approved a new constitution creating the United Republic of Cameroon, a "
          "unitary state. The federated states were abolished. 20 May became the National Day."),

        H("The 1982 transition and its aftermath"),
        T("In November 1982 Ahidjo resigned, and Prime Minister Paul Biya became President as the constitution "
          "provided. Ahidjo kept the chairmanship of the CNU for a time, and tension soon grew between the two men."),
        T("Ahidjo left the country in 1983. In April 1984 an attempted coup in Yaoundé was defeated. In 1984 the "
          "country's name was changed to the Republic of Cameroon, and in 1985 the CNU became the CPDM."),

        H("Liberalization in the 1990s"),
        T("Economic crisis from the late 1980s, the end of the Cold War and pressure for democracy across "
          "Africa all pushed for change. The Social Democratic Front (SDF), led by John Fru Ndi, was launched in "
          "Bamenda in May 1990; several people were killed during the launch."),
        T("Laws on freedom of association and multiparty politics were passed in December 1990. In 1991 "
          "opposition parties organised 'ghost town' (villes mortes) campaigns and demanded a national conference; "
          "the government instead held a tripartite meeting late in 1991."),
        T("Multiparty legislative elections took place in March 1992 and a presidential election in October "
          "1992. Biya was declared the winner; Fru Ndi and other opposition figures disputed the result. In "
          "1993 the All Anglophone Conference in Buea called for a return to federalism."),

        H("The 1996 constitution"),
        T("The constitution of January 1996 kept the unitary state but described it as decentralized. It "
          "provided for regions with elected councils, a Senate and a Constitutional Council, and set a seven-year "
          "presidential term. Many of these institutions were put in place only years later; the constitution "
          "was also amended in 2008."),
        KEY("Federalism versus unitarism", "The debate has deep roots; present both sides.", cards=[
            ["Case for the unitary state", "Supporters argue it strengthened national unity, cut the cost of "
             "duplicated governments, and that the 1972 referendum gave it popular approval."],
            ["Case for federalism", "Critics argue that 1972 ended guarantees given at reunification, that "
             "Anglophone institutions were weakened, and that a federal or strongly decentralized system better "
             "protects diversity."],
            ["Middle positions", "Others see decentralization under the 1996 constitution as a compromise, "
             "debating mainly how fully it has been applied."],
        ], note="Avoid present-day partisan arguments; explain how each view uses historical evidence."),

        EX("Essay plan 1", intro="Why did Cameroon move from a federal to a unitary state between 1961 and 1972?", steps=[
            S("Argument: centralizing design of the 1961 constitution",
              text="Key powers were federal from the start, so the federated states had limited autonomy."),
            S("Argument: the single party after 1966",
              text="The CNU removed separate West Cameroon party competition and channelled politics through Yaoundé."),
            S("Argument: Ahidjo's goal of national unity and security",
              text="The continuing UPC insurgency in the 1960s was used to justify strong central power."),
            S("Counter-argument: popular consent and cost",
              text="The 1972 referendum was approved, and supporters stressed savings and unity; critics question how free the vote was."),
            S("Judgement",
              text="Central leadership and the single party drove the change; the referendum gave it legal form while the debate over its legitimacy continues."),
        ]),
        EX("Essay plan 2", intro="Assess the causes of political liberalization in Cameroon in the early 1990s.", steps=[
            S("Argument: economic crisis",
              text="Falling commodity prices and adjustment programmes from the late 1980s reduced state resources and support."),
            S("Argument: external pressure",
              text="The end of the Cold War, the fall of one-party regimes elsewhere and donor demands for democracy."),
            S("Argument: domestic mobilization",
              text="The SDF launch in 1990, villes mortes in 1991, students, lawyers and the press."),
            S("Counter-argument: limits of change",
              text="The CPDM stayed in power and no sovereign national conference was held, so some historians speak of controlled liberalization."),
            S("Judgement",
              text="Economic and external factors created the opening; domestic pressure forced the 1990 laws; the result was real but limited change."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing 1961, 1972 and 1984",
                "1961 Federal Republic; 1972 United Republic (unitary); 1984 Republic of Cameroon."),
        MISTAKE("Writing about events after 1996 as if they were history in this topic",
                "Keep to the period up to the 1996 constitution, with at most a brief neutral mention of later changes."),
        QUIZ("What was created by the referendum of 20 May 1972?",
             ["The Federal Republic of Cameroon", "The United Republic of Cameroon",
              "The Republic of Cameroon", "The CPDM"], 1,
             "The 1972 referendum created the unitary United Republic of Cameroon.",
             feedback=["The Federal Republic dated from 1961.", "",
                       "That name was adopted in 1984.", "The CPDM was created at the Bamenda congress of 1985."]),
        H("Practice questions"),
        PQ("Essay: How far did the 1982 transition change the nature of the Cameroonian state?",
           "Outline: constitutional succession from Ahidjo to Biya; 1983 to 1984 crisis and failed coup; name change "
           "and CPDM in 1985; continuity: single party, unitary state, strong presidency until 1990. Judgement: "
           "change of leadership more than of system before the 1990s."),
        PQ("Essay: 'The liberalization of the 1990s transformed Cameroonian politics.' Discuss.",
           "Outline: 1990 laws, many parties, 1992 elections, freer press; limits: disputed 1992 result, continued "
           "dominance of the ruling party. Present both supporters' and critics' views."),
        PQ("Short answer: State three provisions of the 1996 constitution.",
           "Decentralized unitary state with regions; a Senate; a Constitutional Council; a seven-year presidential term."),
        SUM("1961 federation had strong federal powers; the single party CNU was formed in 1966.",
            "The 1972 referendum created the unitary United Republic of Cameroon.",
            "In 1982 Biya succeeded Ahidjo; a crisis followed, including the failed coup of 1984.",
            "Liberalization in 1990 brought multiparty politics and contested elections in 1992.",
            "The 1996 constitution created a decentralized unitary state; federalism versus unitarism remains debated."),
    ],
))

# ---------------------------------------------------------------------------
# 4. Constitutional transfers
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="Constitutional transfers",
    title="Constitutional transfers of power: Ghana, Nigeria and French Africa",
    slug="constitutional-transfers",
    minutes=30,
    summary=("How power was transferred by negotiation and constitutional reform: British decolonization in the Gold "
             "Coast (Ghana) and Nigeria, and French reform through the Loi-Cadre and the 1958 referendum, including Guinea's 'No'."),
    objectives=[
        "Explain the stages by which the Gold Coast became independent Ghana in 1957",
        "Explain how Nigeria's regional constitutions led to independence in 1960",
        "Describe the 1956 Loi-Cadre and the 1958 referendum on the French Community",
        "Explain why Guinea voted No in 1958 and what followed",
        "Compare British and French approaches to decolonization",
    ],
    key_concepts=["Constitutional decolonization", "Positive Action", "Federalism in Nigeria", "Loi-Cadre",
                  "French Community", "Balkanization"],
    blocks=[
        H("Introduction"),
        T("Not all of Africa won independence through war. In much of British and French West Africa, power "
          "passed through a series of constitutions, elections and conferences. Cameroonian history is closely "
          "connected to both stories: British Southern Cameroons was administered with Nigeria, and French "
          "reforms like the Loi-Cadre also applied in French Cameroun."),
        D("**Constitutional decolonization** means the gradual transfer of power by legal reforms: new "
          "constitutions, wider voting rights, elected ministers, internal self-government and finally independence.",
          title="Constitutional decolonization"),
        D("The **Loi-Cadre** (framework law) of June 1956, associated with the French minister Gaston Defferre, "
          "introduced universal adult suffrage in a single electoral college and gave territorial assemblies "
          "elected executive councils in each territory.", title="Loi-Cadre"),

        H("The Gold Coast becomes Ghana"),
        T("The United Gold Coast Convention (UGCC) was founded in 1947 and invited Kwame Nkrumah to be its "
          "secretary. After the Accra riots of February 1948, the British appointed the Watson Commission and then "
          "the Coussey Committee to propose reforms."),
        T("Nkrumah broke away to form the Convention People's Party (CPP) in 1949, calling for 'self-government "
          "now'. His Positive Action campaign of strikes and boycotts in January 1950 led to his imprisonment."),
        T("The CPP won the 1951 election. Nkrumah was released to become Leader of Government Business and then "
          "Prime Minister in 1952. After further elections the Gold Coast became independent as Ghana on 6 March "
          "1957, the first sub-Saharan colony to do so."),

        H("Nigeria: regions and federalism"),
        T("Nigeria's constitutions of 1946 (Richards), 1951 (Macpherson) and 1954 (Lyttelton) built up the "
          "regions. The 1954 constitution created a federation of Northern, Western and Eastern regions."),
        T("Politics followed regional lines: the NCNC (Nnamdi Azikiwe) strongest in the East, the Action Group "
          "(Obafemi Awolowo) in the West, and the Northern People's Congress (Ahmadu Bello) in the North. The "
          "Eastern and Western regions gained self-government in 1957 and the North in 1959."),
        T("Nigeria became independent on 1 October 1960, with Abubakar Tafawa Balewa as Prime Minister."),

        H("French Africa: Loi-Cadre and the 1958 referendum"),
        T("After the 1944 Brazzaville conference and the 1946 French Union, French Africans sent deputies to "
          "Paris, and the Rassemblement Démocratique Africain (RDA), led by Félix Houphouët-Boigny, became the "
          "main interterritorial party."),
        T("In 1958 Charles de Gaulle returned to power and held a referendum on 28 September 1958 on the new "
          "constitution and membership of a French Community. A Yes meant joining the Community; a No meant "
          "immediate independence and the loss of French support."),
        T("Guinea, led by Ahmed Sékou Touré, voted No and became independent on 2 October 1958. France withdrew "
          "its officials and aid abruptly. The other territories voted Yes, but by 1960 nearly all of them had "
          "become independent anyway."),
        KEY("British and French approaches compared", "Historians debate how planned each process was.", cards=[
            ["British approach", "Territory-by-territory constitutions; power passed to elected local leaders; "
             "often described as pragmatic, though critics say Britain reacted to pressure rather than planning."],
            ["French approach", "Initially aimed at keeping territories linked to France; the Loi-Cadre shifted "
             "power to individual territories, which Senghor and others criticised as 'balkanization' of the "
             "federations of French West and Equatorial Africa."],
        ], note="Both empires were also influenced by cost, Cold War pressures and events in Algeria and Asia."),

        EX("Essay plan 1", intro="Why did the Gold Coast become the first British colony in sub-Saharan Africa to gain independence?", steps=[
            S("Argument: Nkrumah and the CPP",
              text="Mass party organisation, Positive Action and electoral victory in 1951."),
            S("Argument: favourable conditions",
              text="Relative prosperity from cocoa, an educated elite and no large settler population."),
            S("Argument: British policy",
              text="Watson and Coussey reforms; Britain chose to work with the CPP after 1951."),
            S("Counter-argument: limits of the 'model colony' idea",
              text="Ashanti and northern opposition and the 1948 violence show the process was contested."),
            S("Judgement",
              text="Nkrumah's mobilization was decisive within a context that made Britain willing to concede."),
        ]),
        EX("Essay plan 2", intro="Assess the significance of the 1958 referendum for French Africa.", steps=[
            S("Argument: it offered a formal choice",
              text="Territories could join the Community or take immediate independence."),
            S("Evidence: Guinea's No",
              text="Sékou Touré's Guinea became independent on 2 October 1958; France's harsh response warned others."),
            S("Counter-argument: the Community was short-lived",
              text="By 1960 most territories had gained independence, so the Yes vote delayed rather than prevented it."),
            S("Argument: long-term ties",
              text="Cooperation agreements, the CFA franc and military links kept France influential."),
            S("Judgement",
              text="Important as a turning point, but independence came quickly anyway; its lasting effect was the model of close ties with France."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the Loi-Cadre gave independence",
                "It gave internal autonomy to each territory, not independence."),
        MISTAKE("Confusing Guinea with Guinea-Bissau",
                "Guinea (French) voted No in 1958; Guinea-Bissau (Portuguese) won independence after an armed struggle."),
        QUIZ("Which territory voted No in the 1958 French referendum?",
             ["Senegal", "Côte d'Ivoire", "Guinea", "Gabon"], 2,
             "Guinea, under Sékou Touré, voted No and became independent on 2 October 1958.",
             feedback=["Senegal voted Yes.", "Côte d'Ivoire, Houphouët-Boigny's base, voted Yes.", "", "Gabon voted Yes."]),
        H("Practice questions"),
        PQ("Essay: Compare the decolonization of Ghana and Nigeria.",
           "Outline: Ghana unitary, rapid, dominated by one mass party; Nigeria federal, regional parties, slower and "
           "staged regional self-government. Similarities: British constitutional route, elections, London "
           "conferences. Judgement on why the paths differed: size, regional diversity, party structure."),
        PQ("Essay: 'France decolonized in order to keep its influence in Africa.' Discuss.",
           "Outline: Loi-Cadre, Community, cooperation agreements, CFA franc, military bases; counter: African "
           "pressure, Guinea's No, cost of empire, Algeria. Judgement balancing French aims and African agency."),
        PQ("Short answer: What was Positive Action?",
           "The CPP's campaign of strikes and boycotts launched in January 1950 to press for self-government; it led to Nkrumah's arrest."),
        SUM("Ghana gained independence on 6 March 1957 after CPP victories and staged reforms.",
            "Nigeria became a federation in 1954 and independent on 1 October 1960, with regionally based parties.",
            "The 1956 Loi-Cadre gave each French territory internal autonomy and universal suffrage.",
            "In the 1958 referendum only Guinea voted No; most French territories still became independent in 1960.",
            "British and French approaches differed, but both were shaped by African pressure and international change."),
    ],
))

# ---------------------------------------------------------------------------
# 5. Armed liberation
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="Armed liberation",
    title="Armed liberation struggles: Algeria, Kenya, the Portuguese colonies and Zimbabwe",
    slug="armed-liberation",
    minutes=30,
    summary=("Why some African territories won independence through armed struggle: the Algerian war, Mau Mau in "
             "Kenya, the wars in Angola, Mozambique and Guinea-Bissau, and the Second Chimurenga in Zimbabwe."),
    objectives=[
        "Explain why armed struggle occurred in some territories but not others",
        "Outline the main stages of the Algerian war of independence, 1954 to 1962",
        "Describe the Mau Mau rising and the British response in Kenya",
        "Explain how the Portuguese colonies won independence after 1974",
        "Outline the Second Chimurenga and the Lancaster House settlement in Zimbabwe",
    ],
    key_concepts=["Settler colony", "Guerrilla warfare", "FLN", "Mau Mau", "Carnation Revolution", "UDI", "Chimurenga"],
    blocks=[
        H("Introduction"),
        T("In Ghana or Senegal, power was handed over through elections and negotiation. Elsewhere, Africans "
          "fought long wars. Cameroon itself experienced armed conflict with the UPC, so comparing it with these "
          "cases helps you understand why decolonization was violent in some places."),
        D("A **settler colony** had a large, politically powerful European population that owned land and "
          "resisted majority rule, as in Algeria, Kenya, Southern Rhodesia, Angola and Mozambique.", title="Settler colony"),
        D("**Chimurenga** is a Shona word for revolutionary struggle. The First Chimurenga was the rising of "
          "1896 to 1897; the Second Chimurenga was the liberation war of the 1960s and 1970s.", title="Chimurenga"),
        KEY("Why armed struggle?", "Historians stress several overlapping causes.", cards=[
            ["Settler resistance", "Settlers blocked reform and pressed the colonial power to refuse majority rule."],
            ["Colonial power's attitude", "France saw Algeria as part of France; Portugal under Salazar treated "
             "its colonies as overseas provinces."],
            ["Land and economy", "Loss of land and labour exploitation fuelled rural support for fighters."],
        ]),

        H("Algeria, 1954 to 1962"),
        T("Algeria was legally part of France and had about a million European settlers. The violent repression at "
          "Sétif in May 1945 hardened nationalist opinion."),
        T("The Front de Libération Nationale (FLN) launched its armed struggle on 1 November 1954. The war "
          "included the Battle of Algiers in 1957 and the widespread use of torture by French forces, which "
          "became a scandal in France."),
        T("The crisis of May 1958 brought de Gaulle back to power. He moved towards self-determination, and the "
          "Evian Accords of March 1962 led to a referendum and independence on 5 July 1962. Casualty figures are "
          "disputed and remain politically sensitive."),

        H("Kenya and Mau Mau"),
        T("Mau Mau, also called the Kenya Land and Freedom Army, was rooted mainly among the Kikuyu of central "
          "Kenya and grew out of land grievances in the White Highlands. The British declared a State of "
          "Emergency in October 1952."),
        T("Jomo Kenyatta was arrested and convicted at the Kapenguria trial, although his link to Mau Mau was "
          "disputed. Tens of thousands were detained in camps; the Hola camp killings of 1959 caused outrage in "
          "Britain. Dedan Kimathi was captured in 1956 and executed in 1957."),
        T("The fighting was largely defeated by 1956, but Britain changed course. Lancaster House conferences "
          "in 1960 and 1962 led to majority rule, and Kenya became independent on 12 December 1963 with Kenyatta "
          "as Prime Minister."),

        H("The Portuguese colonies"),
        T("Wars began in Angola in 1961, Guinea-Bissau in 1963 and Mozambique in 1964. Movements included the "
          "MPLA, FNLA and UNITA in Angola, the PAIGC of Amílcar Cabral in Guinea-Bissau, and FRELIMO, led first "
          "by Eduardo Mondlane and later Samora Machel, in Mozambique."),
        T("The cost of the wars helped cause the Carnation Revolution in Lisbon on 25 April 1974. Portugal then "
          "recognised Guinea-Bissau in 1974; Mozambique became independent in June 1975 and Angola in November "
          "1975, where civil war continued with foreign involvement."),

        H("Zimbabwe and the Second Chimurenga"),
        T("Ian Smith's white minority government made a Unilateral Declaration of Independence (UDI) on 11 "
          "November 1965. ZAPU (Joshua Nkomo) and ZANU (Ndabaningi Sithole, later Robert Mugabe) waged guerrilla "
          "war, which intensified in the 1970s after Mozambique's independence gave ZANU bases."),
        T("The Lancaster House Agreement of December 1979 led to elections in February 1980. Zimbabwe became "
          "independent on 18 April 1980 with Mugabe as Prime Minister."),

        EX("Essay plan 1", intro="Compare the reasons for armed struggle in Algeria and Kenya.", steps=[
            S("Argument: settler power in both",
              text="Large settler populations controlled land and resisted reform."),
            S("Argument: different legal status",
              text="Algeria was treated as part of France; Kenya was a colony where Britain could more easily change policy."),
            S("Argument: different social bases",
              text="The FLN built a national movement across Algeria; Mau Mau was concentrated in central Kenya."),
            S("Counter-argument: outcomes differed",
              text="The FLN won a political victory; Mau Mau was defeated militarily, yet both made continued rule too costly."),
            S("Judgement",
              text="Settler resistance was the common cause; the colonial power's view of the territory explains the length and intensity."),
        ]),
        EX("Essay plan 2", intro="'Events in Portugal, not in Africa, ended Portuguese colonial rule.' Discuss.", steps=[
            S("Argument for: the Carnation Revolution",
              text="The April 1974 coup in Lisbon led directly to negotiations and independence in 1974 to 1975."),
            S("Argument against: the wars caused the coup",
              text="Officers turned against the regime because of long, costly wars, especially in Guinea-Bissau."),
            S("Evidence: African movements' gains",
              text="PAIGC controlled much of Guinea-Bissau and declared independence in 1973; FRELIMO advanced in Mozambique."),
            S("Argument: international context",
              text="UN pressure and support for movements from various states added to Portugal's isolation."),
            S("Judgement",
              text="The coup was the trigger, but African armed struggle was the underlying cause."),
        ]),
        MISTAKE("Treating Mau Mau as a simple military victory for Kenyans",
                "Militarily the rising was largely defeated; its significance lies in changing British policy."),
        MISTAKE("Mixing up ZANU and ZAPU",
                "ZAPU was led by Nkomo; ZANU, formed in 1963, came to be led by Mugabe."),
        QUIZ("What event in 1974 opened the way to independence for Portugal's African colonies?",
             ["The Evian Accords", "The Carnation Revolution", "The Lancaster House Agreement", "UDI"], 1,
             "The Carnation Revolution of 25 April 1974 overthrew the dictatorship in Lisbon.",
             feedback=["Evian (1962) ended the Algerian war.", "",
                       "Lancaster House (1979) concerned Zimbabwe.", "UDI (1965) was Rhodesia's rebellion against Britain."]),
        H("Practice questions"),
        PQ("Essay: Why was decolonization in Algeria so violent?",
           "Outline: Algeria legally part of France; settlers; Sétif 1945; FLN strategy; French army and torture; "
           "May 1958 crisis; counter: de Gaulle's eventual negotiation. Judgement: status and settlers."),
        PQ("Essay: Assess the importance of external support in the Zimbabwean liberation struggle.",
           "Outline: Mozambican and Zambian bases, Frontline States, international sanctions; internal: rural "
           "support, ZANLA and ZIPRA; Lancaster House brokered by Britain. Judgement balancing internal and external factors."),
        PQ("Source-style: Explain why the Hola camp killings of 1959 were significant.",
           "Detainees were beaten to death at Hola; the outrage in Britain increased pressure to end the Emergency and move towards majority rule."),
        SUM("Armed struggle was most likely where settlers were powerful and the colonial power refused reform.",
            "Algeria won independence on 5 July 1962 after the 1954 to 1962 war.",
            "Mau Mau was defeated militarily but pushed Britain towards majority rule; Kenya became independent in 1963.",
            "The Carnation Revolution of 1974 followed costly African wars and ended Portuguese rule.",
            "Zimbabwe became independent in 1980 after the Second Chimurenga and Lancaster House."),
    ],
))

# ---------------------------------------------------------------------------
# 6. South Africa
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_DEC,
    topic="South Africa",
    title="Apartheid and the struggle against it in South Africa, 1948 to 1994",
    slug="south-africa-anti-apartheid-struggle",
    minutes=30,
    summary=("The system of apartheid introduced after 1948, the forms of resistance from the Defiance Campaign to the "
             "UDF, international pressure, and the negotiated transition that led to the elections of April 1994."),
    objectives=[
        "Explain what apartheid was and name key apartheid laws",
        "Describe the main phases of resistance from 1948 to 1990",
        "Assess the role of international pressure and sanctions",
        "Explain why apartheid ended through negotiation between 1990 and 1994",
    ],
    key_concepts=["Apartheid", "ANC", "PAC", "Freedom Charter", "Black Consciousness", "Sanctions", "CODESA"],
    blocks=[
        H("Introduction"),
        T("South Africa was already independent and ruled by a white minority when most of Africa decolonized. "
          "The struggle there was not against a distant colonial power but against a domestic system of racial "
          "domination. Africa, including Cameroon, supported the struggle through the OAU and the UN."),
        D("**Apartheid** (Afrikaans for 'separateness') was the system of legal racial segregation and white "
          "minority rule introduced by the National Party government after its election victory in 1948.",
          title="Apartheid"),
        D("The **Freedom Charter**, adopted at the Congress of the People at Kliptown in June 1955, set out the "
          "demands of the ANC and its allies for a non-racial, democratic South Africa.", title="Freedom Charter"),

        H("Building apartheid after 1948"),
        T("The National Party under D. F. Malan won the 1948 election. Key laws followed: the Population "
          "Registration Act and Group Areas Act (1950), the Suppression of Communism Act (1950), the Bantu "
          "Education Act (1953) and the Reservation of Separate Amenities Act (1953)."),
        T("Under H. F. Verwoerd the policy of 'separate development' created homelands (Bantustans), and "
          "Africans were treated as citizens of these territories rather than of South Africa."),

        H("Resistance, 1948 to 1964"),
        T("The ANC, led increasingly by its Youth League generation including Nelson Mandela, Walter Sisulu and "
          "Oliver Tambo, launched the Defiance Campaign in 1952. The Freedom Charter followed in 1955 and the long "
          "Treason Trial from 1956 ended in acquittals in 1961."),
        T("The Pan Africanist Congress (PAC), led by Robert Sobukwe, broke away in 1959. At Sharpeville on 21 "
          "March 1960 police fired on a PAC anti-pass protest, killing 69 people. The government banned the ANC "
          "and PAC."),
        T("The ANC formed an armed wing, Umkhonto we Sizwe, in 1961. After the Rivonia Trial, Mandela and other "
          "leaders were sentenced to life imprisonment in 1964."),

        H("New resistance and international pressure, 1970s to 1980s"),
        T("The Black Consciousness Movement, associated with Steve Biko, inspired a new generation. The Soweto "
          "uprising began on 16 June 1976 when students protested against Afrikaans-medium teaching. Biko died "
          "in police custody in 1977."),
        T("In 1977 the UN Security Council imposed a mandatory arms embargo. In the 1980s the United Democratic "
          "Front (UDF, 1983), trade unions and township protests made the country hard to govern, and many "
          "states and companies imposed sanctions or withdrew investment."),

        H("Negotiated transition, 1990 to 1994"),
        T("On 2 February 1990 President F. W. de Klerk announced the unbanning of the ANC, PAC and other groups. "
          "Mandela was released on 11 February 1990. Negotiations, including CODESA, continued amid serious violence."),
        T("The first non-racial elections were held on 27 April 1994. The ANC won, and Mandela became President "
          "in May 1994. Mandela and de Klerk had jointly received the Nobel Peace Prize in 1993."),
        KEY("Why did apartheid end?", "Historians weigh these factors differently.", cards=[
            ["Internal resistance", "Mass protest, unions and armed struggle made apartheid unworkable."],
            ["International pressure", "Sanctions, sports and cultural boycotts and isolation raised the cost."],
            ["Economic and Cold War change", "Economic decline and the end of the Cold War removed the 'communist "
             "threat' argument and encouraged negotiation."],
            ["Leadership", "De Klerk's reforms and Mandela's commitment to negotiation made a settlement possible."],
        ]),

        EX("Essay plan 1", intro="How far was internal resistance responsible for the end of apartheid?", steps=[
            S("Argument: internal resistance",
              text="Soweto 1976, UDF and unions in the 1980s; ungovernability forced repeated states of emergency."),
            S("Argument: international pressure",
              text="1977 arms embargo, sanctions and disinvestment in the 1980s hurt the economy and morale."),
            S("Argument: end of the Cold War",
              text="After 1989 the government could no longer present itself as a Western bulwark against communism."),
            S("Counter-argument: leadership",
              text="De Klerk's 1990 decisions and Mandela's role were essential to a negotiated rather than violent end."),
            S("Judgement",
              text="Internal resistance was the most important long-term factor, made decisive by international and Cold War change."),
        ]),
        EX("Essay plan 2", intro="Assess the significance of the Sharpeville shootings of 1960.", steps=[
            S("Argument: turning point in methods",
              text="The banning of the ANC and PAC led to the turn to armed struggle in 1961."),
            S("Argument: international impact",
              text="Sharpeville drew worldwide condemnation and strengthened the anti-apartheid movement abroad."),
            S("Counter-argument: apartheid strengthened in the short term",
              text="The government survived, left the Commonwealth and became a republic in 1961, and repression grew."),
            S("Judgement",
              text="Highly significant in the long term, even though it initially strengthened the state's hand."),
        ]),
        MISTAKE("Confusing the ANC and PAC",
                "The PAC broke away from the ANC in 1959 and rejected the multiracial alliance of the Freedom Charter."),
        MISTAKE("Saying apartheid began with colonial rule",
                "Segregation was older, but apartheid as a legal system dates from the National Party victory of 1948."),
        QUIZ("Which event began on 16 June 1976?",
             ["The Sharpeville shootings", "The Soweto uprising", "The Rivonia Trial", "The release of Mandela"], 1,
             "Students in Soweto protested against Afrikaans-medium teaching on 16 June 1976.",
             feedback=["Sharpeville was on 21 March 1960.", "", "The Rivonia Trial took place in 1963 to 1964.",
                       "Mandela was released on 11 February 1990."]),
        H("Practice questions"),
        PQ("Essay: Compare the strategies of the ANC and the Black Consciousness Movement.",
           "Outline: ANC non-racial alliance, Freedom Charter, from non-violence to armed struggle; BCM psychological "
           "liberation and Black self-reliance, influence on Soweto generation. Judgement on their contributions."),
        PQ("Essay: 'Sanctions ended apartheid.' Discuss.",
           "Outline: arms embargo 1977, 1980s sanctions and disinvestment; counter: internal resistance, economic "
           "decline, Cold War, leadership. Judgement: sanctions were important but not sufficient alone."),
        PQ("Short answer: State two apartheid laws and what each did.",
           "Population Registration Act 1950 classified people by race; Group Areas Act 1950 segregated residential areas; "
           "Bantu Education Act 1953 created inferior separate schooling for Africans."),
        SUM("Apartheid was built after the National Party victory of 1948 through laws on race, residence and education.",
            "Peaceful protest in the 1950s led to banning in 1960 and the turn to armed struggle in 1961.",
            "Soweto (1976), the UDF and unions renewed resistance; sanctions increased isolation.",
            "De Klerk unbanned the ANC in 1990; Mandela was freed and negotiations followed.",
            "Elections on 27 April 1994 ended white minority rule."),
    ],
))

# ---------------------------------------------------------------------------
# 7. Cold War geopolitics
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="Cold War geopolitics",
    title="Cold War geopolitics: containment, deterrence and rivalry in the Global South",
    slug="cold-war-geopolitics",
    minutes=30,
    summary=("The origins and development of the Cold War: the Truman Doctrine, the Marshall Plan and containment, "
             "nuclear deterrence, and superpower rivalry in Africa, Asia and Latin America."),
    objectives=[
        "Explain the Truman Doctrine, the Marshall Plan and the policy of containment",
        "Explain nuclear deterrence and key crises such as Cuba in 1962",
        "Describe superpower rivalry in the Global South, including Africa",
        "Compare orthodox, revisionist and post-revisionist interpretations of the Cold War",
    ],
    key_concepts=["Containment", "Truman Doctrine", "Marshall Plan", "Deterrence", "Mutually assured destruction",
                  "Non-Aligned Movement", "Proxy war"],
    blocks=[
        H("Introduction"),
        T("From about 1947 to 1991 the United States and the Soviet Union competed for influence across the "
          "world without fighting each other directly. Newly independent African states, including Cameroon, had "
          "to navigate this rivalry: aid, arms and diplomatic support often came with Cold War strings."),
        D("**Containment** was the US policy of preventing the spread of Soviet influence and communism. It is "
          "associated with the diplomat George Kennan's analysis of 1946 to 1947.", title="Containment"),
        D("**Nuclear deterrence** is the idea that a state will not attack if it expects devastating retaliation. "
          "When both superpowers could destroy each other, this was called **mutually assured destruction (MAD)**.",
          title="Deterrence"),

        H("Origins: 1945 to 1949"),
        T("Wartime allies fell out over Eastern Europe, Germany and the post-war order. Soviet-backed communist "
          "governments were established across Eastern Europe."),
        T("In March 1947 President Truman asked Congress for aid to Greece and Turkey, promising to support "
          "'free peoples' resisting subjugation. This became known as the Truman Doctrine."),
        T("The Marshall Plan, announced in June 1947, provided large-scale US economic aid to rebuild Western "
          "Europe. The USSR refused it and kept Eastern Europe out."),
        T("The Berlin Blockade (1948 to 1949) and Allied airlift, the founding of NATO in April 1949 and the "
          "first Soviet atomic test in August 1949 confirmed the division of Europe."),

        H("Deterrence and crisis"),
        T("The Korean War (1950 to 1953) globalised containment. The Warsaw Pact was formed in 1955. In October "
          "1962 the Cuban Missile Crisis brought the world close to nuclear war before the USSR withdrew its "
          "missiles from Cuba."),
        T("Afterwards a hotline was set up (1963) and treaties followed: the Partial Test Ban Treaty (1963), the "
          "Non-Proliferation Treaty (1968) and SALT I (1972). This period of easing tension is called detente."),

        H("Rivalry in the Global South"),
        T("Many new states sought to avoid choosing sides. The Bandung Conference of 1955 and the founding of the "
          "Non-Aligned Movement at Belgrade in 1961 expressed this aim."),
        T("Africa became an arena of rivalry: the Congo crisis from 1960, the Angolan civil war from 1975 with "
          "Cuban troops and US and South African involvement, and the Ogaden war of 1977 to 1978 between Ethiopia "
          "and Somalia. Ahidjo's Cameroon generally kept close ties with France and the West while describing its "
          "foreign policy as non-aligned."),
        KEY("Who caused the Cold War?", "The historiography has three main schools.", cards=[
            ["Orthodox", "Writing mainly in the early Cold War: Soviet expansionism caused it, and the US responded defensively."],
            ["Revisionist", "From the 1960s: US economic interests and aggressive policy, including the atomic bomb "
             "and the Marshall Plan, share or carry the blame."],
            ["Post-revisionist", "From the 1970s and 1980s, associated with John Lewis Gaddis: mutual misperception and "
             "security fears on both sides; later work using Soviet archives also stresses ideology."],
        ]),

        EX("Essay plan 1", intro="How far was the Marshall Plan an extension of the Truman Doctrine?", steps=[
            S("Argument: same purpose of containment",
              text="Both aimed to stop communist influence; economic recovery reduced the appeal of communist parties."),
            S("Evidence: timing and Soviet reaction",
              text="Both in 1947; the USSR rejected Marshall aid and saw it as a threat."),
            S("Counter-argument: humanitarian and economic aims",
              text="Recovery of European markets served US trade and responded to real hardship."),
            S("Counter-argument: different means",
              text="The Doctrine was military and political; the Plan was economic and open in principle to all."),
            S("Judgement",
              text="Largely an extension: economic containment complementing political commitment."),
        ]),
        EX("Essay plan 2", intro="Assess the impact of the Cold War on post-colonial Africa.", steps=[
            S("Argument: proxy conflicts",
              text="Congo, Angola and the Horn of Africa were prolonged by superpower involvement."),
            S("Argument: support for authoritarian allies",
              text="Both blocs backed friendly regimes regardless of their domestic record."),
            S("Counter-argument: African agency",
              text="Non-alignment, the OAU and leaders who played the blocs against each other to gain aid."),
            S("Counter-argument: former colonial powers",
              text="France and Britain often mattered more than the superpowers in their former territories."),
            S("Judgement",
              text="The Cold War shaped many conflicts and regimes, but local causes and former colonial ties were often equally important."),
        ]),
        MISTAKE("Calling the Cold War a direct war between the superpowers",
                "The US and USSR never fought each other directly; conflict was through proxies, arms races and diplomacy."),
        MISTAKE("Ignoring historiography",
                "Interpretation questions expect you to name and evaluate schools of thought."),
        QUIZ("What did the Truman Doctrine of March 1947 promise?",
             ["Economic aid to all of Europe", "Support for free peoples resisting subjugation, starting with Greece and Turkey",
              "A military alliance with the USSR", "Withdrawal of US troops from Europe"], 1,
             "Truman asked Congress for aid to Greece and Turkey and pledged support for free peoples.",
             feedback=["That describes the Marshall Plan.", "", "The doctrine was directed against Soviet expansion.",
                       "The US increased its commitment to Europe."]),
        H("Practice questions"),
        PQ("Essay: 'Nuclear weapons kept the Cold War cold.' Discuss.",
           "Outline: MAD, Cuba 1962 and caution afterwards, arms control; counter: proxy wars killed many, near-misses, "
           "other factors such as diplomacy and economics. Judgement."),
        PQ("Essay: Evaluate the orthodox and revisionist interpretations of the origins of the Cold War.",
           "Outline: orthodox evidence (Eastern Europe, Berlin Blockade); revisionist evidence (Marshall Plan, "
           "atomic diplomacy); post-revisionist synthesis. Judgement on which is most convincing with reasons."),
        PQ("Short answer: Why did many African states join the Non-Aligned Movement?",
           "To protect newly won sovereignty, avoid being drawn into superpower conflicts and gain aid from both blocs."),
        SUM("The Cold War began after 1945 over Europe and the post-war order.",
            "The Truman Doctrine and the Marshall Plan (1947) put containment into practice.",
            "Nuclear deterrence shaped crises such as Cuba in 1962 and later arms control.",
            "Africa, Asia and Latin America became arenas of proxy rivalry; many states chose non-alignment.",
            "Orthodox, revisionist and post-revisionist historians explain the Cold War differently."),
    ],
))

# ---------------------------------------------------------------------------
# 8. The United Nations
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="The United Nations",
    title="The United Nations: the Charter, the Security Council and peacekeeping",
    slug="the-united-nations",
    minutes=30,
    summary=("The aims and structure of the United Nations under its 1945 Charter, the role and limits of the Security "
             "Council, and the record of peacekeeping in the Congo, the Balkans and Rwanda."),
    objectives=[
        "State the aims of the UN Charter and name the principal organs",
        "Explain the composition and powers of the Security Council, including the veto",
        "Describe UN peacekeeping in the Congo (1960 to 1964), the Balkans and Rwanda",
        "Assess the successes and failures of the UN in maintaining peace",
    ],
    key_concepts=["UN Charter", "Security Council", "Veto", "Peacekeeping", "Chapter VII", "Trusteeship Council"],
    blocks=[
        H("Introduction"),
        T("The United Nations matters directly to Cameroonian history. Its Trusteeship Council supervised both "
          "Cameroons, it organised the 1961 plebiscites, and Cameroon joined it as a member in 1960. This lesson "
          "looks at how the UN was designed and how well it has kept the peace."),
        D("The **UN Charter** was signed at San Francisco on 26 June 1945 and came into force on 24 October 1945. "
          "Its aims include maintaining international peace and security, developing friendly relations based on "
          "self-determination, and promoting human rights and social progress.", title="UN Charter"),
        D("The **veto** is the power of each of the five permanent members of the Security Council (China, "
          "France, the USSR/Russia, the United Kingdom and the United States) to block any substantive resolution.",
          title="Veto"),

        H("Structure of the UN"),
        T("The six principal organs are the General Assembly, the Security Council, the Economic and Social "
          "Council, the Trusteeship Council, the International Court of Justice and the Secretariat, headed by "
          "the Secretary-General."),
        T("The Security Council has primary responsibility for peace and security. It had eleven members at "
          "first and fifteen after an enlargement that took effect in 1965: five permanent and ten elected."),
        T("Chapter VI of the Charter covers peaceful settlement of disputes. Chapter VII allows the Council to "
          "order sanctions or military action against threats to peace."),
        KEY("Strengths and weaknesses of the design", "The structure reflects the world of 1945.", cards=[
            ["Strengths", "Near-universal membership, a forum for new states, legal authority under Chapter VII."],
            ["Weaknesses", "The veto paralysed the Council during much of the Cold War; the UN has no army of "
             "its own and depends on member states for troops and money."],
        ]),

        H("Peacekeeping in the Congo, 1960 to 1964"),
        T("Soon after the Congo's independence in June 1960, an army mutiny, Belgian intervention and the "
          "secession of Katanga led the government to ask for UN help. The UN force (ONUC) was one of the largest "
          "operations of the period."),
        T("ONUC eventually ended the Katanga secession in 1963, but the operation was controversial. Prime "
          "Minister Patrice Lumumba was killed in 1961, and Secretary-General Dag Hammarskjöld died in a plane crash "
          "near Ndola in September 1961. The Soviet Union and others accused the UN of serving Western interests."),

        H("The Balkans and Rwanda in the 1990s"),
        T("After the Cold War the Security Council authorised many more operations. In the former Yugoslavia, "
          "UNPROFOR was deployed from 1992. In July 1995 Bosnian Serb forces overran the UN-declared 'safe area' "
          "of Srebrenica and killed thousands of Bosniak men and boys. NATO air strikes and the Dayton Agreement of "
          "late 1995 ended the Bosnian war."),
        T("In Rwanda a small UN mission (UNAMIR), commanded by General Roméo Dallaire, was present when the "
          "genocide against the Tutsi began in April 1994. The Security Council reduced the force rather than "
          "strengthening it. Hundreds of thousands of people were killed in about one hundred days."),
        KEY("Assessing UN peacekeeping", "Judgements depend on what the UN was asked and allowed to do.", cards=[
            ["Critical view", "Rwanda and Srebrenica show the UN failing to protect civilians, with weak mandates and member states unwilling to act."],
            ["Defensive view", "Failures reflect the choices of powerful member states; many missions, such as later "
             "operations in Mozambique or Namibia, helped end conflicts."],
        ]),

        EX("Essay plan 1", intro="Assess the effectiveness of the UN in the Congo crisis, 1960 to 1964.", steps=[
            S("Argument: success in preserving the state",
              text="ONUC ended Katanga's secession in 1963 and kept the Congo united."),
            S("Argument: failure to protect Lumumba and stability",
              text="The UN could not prevent the central government's collapse or Lumumba's killing in 1961."),
            S("Evidence: Cold War divisions",
              text="Soviet criticism and a financial crisis in the UN over the cost of the operation."),
            S("Counter-argument: limits of the mandate",
              text="The UN was not designed for internal conflicts and depended on members' support."),
            S("Judgement",
              text="Partial success: territorial unity preserved at a high cost to the UN's reputation and finances."),
        ]),
        EX("Essay plan 2", intro="'The failures of the UN in the 1990s were failures of its member states.' Discuss.", steps=[
            S("Argument for: Rwanda",
              text="The Security Council reduced UNAMIR in April 1994 despite warnings from the commander."),
            S("Argument for: Srebrenica",
              text="Safe areas were declared without enough troops to defend them."),
            S("Counter-argument: institutional weaknesses",
              text="Bureaucracy, unclear mandates and rules of engagement within the UN itself."),
            S("Counter-argument: successes",
              text="Missions in Namibia, Mozambique and Cambodia show the UN could work when members were committed."),
            S("Judgement",
              text="Mainly member states, especially permanent members, but the UN system made their reluctance easier to hide."),
        ]),
        MISTAKE("Listing only five members of the Security Council",
                "There are five permanent members, but the Council has fifteen members in total."),
        MISTAKE("Forgetting the Trusteeship Council in Cameroonian questions",
                "It supervised both Cameroons until 1960 to 1961; link it to petitions and visiting missions."),
        QUIZ("Which chapter of the UN Charter allows the Security Council to authorise sanctions or military action?",
             ["Chapter I", "Chapter VI", "Chapter VII", "Chapter XII"], 2,
             "Chapter VII deals with action with respect to threats to the peace and acts of aggression.",
             feedback=["Chapter I sets out purposes and principles.", "Chapter VI covers peaceful settlement.", "",
                       "Chapter XII deals with the trusteeship system."]),
        H("Practice questions"),
        PQ("Essay: How far did the veto limit the effectiveness of the Security Council during the Cold War?",
           "Outline: frequent vetoes by both sides, paralysis on many issues; counter: Korea 1950 (Soviet absence), "
           "Uniting for Peace resolution 1950, UNEF 1956, ONUC. Judgement."),
        PQ("Essay: Assess the role of the UN in the decolonization of Cameroon.",
           "Outline: trusteeship 1946, visiting missions and petitions, decision to end trusteeship in 1959, plebiscites of 1961; "
           "limits: UN accepted French and British choices. Judgement linking this lesson to the Cameroon module."),
        PQ("Short answer: Name the six principal organs of the UN.",
           "General Assembly, Security Council, Economic and Social Council, Trusteeship Council, International Court of Justice, Secretariat."),
        SUM("The UN Charter (1945) aims to maintain peace, promote self-determination and protect human rights.",
            "The Security Council has five permanent members with a veto and ten elected members.",
            "The Congo operation (1960 to 1964) kept the country united but was deeply controversial.",
            "Srebrenica (1995) and Rwanda (1994) exposed the limits of peacekeeping.",
            "The UN shaped Cameroon's history through trusteeship and the 1961 plebiscites."),
    ],
))

# ---------------------------------------------------------------------------
# 9. Regional integration
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CW,
    topic="Regional integration",
    title="Regional integration in Africa: from the OAU to the AU, CEMAC, ECOWAS and SADC",
    slug="regional-integration",
    minutes=30,
    summary=("African continental and regional organisations: the OAU and its replacement by the African Union, "
             "the economic communities CEMAC, ECOWAS and SADC, and the changed world after the end of the Cold War in 1991."),
    objectives=[
        "Explain the aims, principles and record of the OAU from 1963",
        "Explain why the OAU was replaced by the African Union and what changed",
        "Describe the origins and aims of CEMAC, ECOWAS and SADC",
        "Assess how the end of the Cold War changed international and African politics",
    ],
    key_concepts=["Pan-Africanism", "OAU", "African Union", "Non-interference", "CEMAC", "ECOWAS", "SADC", "Unipolarity"],
    blocks=[
        H("Introduction"),
        T("After independence, African leaders debated how far the continent should unite. Cameroon is a member "
          "of the African Union and of CEMAC, whose central bank, the BEAC, has its headquarters in Yaoundé. "
          "Regional organisations therefore affect trade, money and travel for Cameroonians."),
        D("**Pan-Africanism** is the idea that African peoples share common interests and should cooperate or "
          "unite politically and economically.", title="Pan-Africanism"),
        D("**Non-interference** in the internal affairs of member states was a core principle of the OAU, "
          "together with respect for sovereignty and the territorial integrity inherited at independence.",
          title="Non-interference"),

        H("The Organisation of African Unity, 1963 to 2002"),
        T("Before 1963 African states were divided between the more radical Casablanca group, which wanted rapid "
          "political union, and the more gradualist Monrovia group. Cameroon under Ahidjo was among the moderates."),
        T("The OAU was founded at Addis Ababa on 25 May 1963. It adopted the moderate approach: cooperation "
          "between sovereign states rather than a single government. In 1964 members agreed to respect the "
          "borders inherited from colonial rule."),
        T("The OAU's Liberation Committee supported movements fighting colonial and white minority rule in "
          "southern Africa. However, non-interference meant it said little about coups, civil wars and human "
          "rights abuses within member states."),

        H("From OAU to African Union"),
        T("The Sirte Declaration of September 1999 called for a new union. The Constitutive Act was adopted in "
          "Lomé in 2000, and the African Union was launched at Durban in 2002."),
        T("The Constitutive Act gives the AU the right to intervene in a member state in grave circumstances: "
          "war crimes, genocide and crimes against humanity. This shift from non-interference to 'non-indifference' "
          "was influenced by the Rwandan genocide. The AU also created a Peace and Security Council."),
        KEY("OAU and AU compared", "Continuity and change.", cards=[
            ["OAU", "Strict non-interference; main success in supporting liberation and ending apartheid; weak on internal conflicts."],
            ["AU", "Right of intervention in grave circumstances; rejects unconstitutional changes of government; "
             "still limited by funding and member states' will."],
        ]),

        H("Regional economic communities"),
        T("CEMAC grew out of UDEAC (the Central African Customs and Economic Union, created in 1964). The CEMAC "
          "treaty was signed in 1994. Its members are Cameroon, the Central African Republic, Chad, the Congo, "
          "Equatorial Guinea and Gabon, which share the CFA franc issued by the BEAC. The CFA franc was devalued "
          "in January 1994."),
        T("ECOWAS was founded by the Treaty of Lagos in May 1975 to promote economic integration in West Africa. "
          "From 1990 its monitoring group, ECOMOG, intervened in the Liberian civil war, and later in Sierra Leone."),
        T("SADC began as the Southern African Development Coordination Conference in 1980, partly to reduce "
          "dependence on apartheid South Africa. It became the Southern African Development Community in 1992, "
          "and South Africa joined in 1994."),

        H("The post-1991 world"),
        T("The Soviet Union dissolved in December 1991, ending the Cold War. Some described the result as a "
          "unipolar world led by the United States. Western donors increasingly tied aid to democracy and "
          "economic reform, which contributed to political liberalization in Africa, including Cameroon."),

        EX("Essay plan 1", intro="How successful was the OAU in achieving its aims between 1963 and 2002?", steps=[
            S("Argument: success in liberation",
              text="Liberation Committee support for southern African movements; apartheid ended in 1994."),
            S("Argument: preventing border wars",
              text="The 1964 decision to accept colonial borders reduced some territorial disputes."),
            S("Counter-argument: failure on internal conflicts and rights",
              text="Non-interference left civil wars, coups and the Rwandan genocide largely unaddressed."),
            S("Counter-argument: weak economic integration",
              text="Limited resources and divisions between members slowed cooperation."),
            S("Judgement",
              text="Successful in decolonization, weak in governance and peace within states, which led to its replacement."),
        ]),
        EX("Essay plan 2", intro="Assess the impact of the end of the Cold War on Africa.", steps=[
            S("Argument: political liberalization",
              text="End of superpower support for one-party regimes; donor pressure for multiparty elections."),
            S("Argument: end of proxy conflicts",
              text="Namibia independent in 1990; negotiations in South Africa and Mozambique."),
            S("Counter-argument: new conflicts",
              text="Wars in Liberia, Sierra Leone, Somalia and the Great Lakes region in the 1990s."),
            S("Argument: new regional responses",
              text="ECOMOG and later the AU's intervention principle."),
            S("Judgement",
              text="A major turning point that opened space for democracy and regional action, but also exposed weak states to new conflicts."),
        ]),
        MISTAKE("Confusing CEMAC and ECOWAS",
                "Cameroon is in CEMAC (Central Africa) and ECCAS, not ECOWAS (West Africa)."),
        MISTAKE("Saying the AU replaced the OAU in 1999",
                "1999 was the Sirte Declaration; the AU was launched in 2002."),
        QUIZ("Where and when was the OAU founded?",
             ["Accra, 1958", "Addis Ababa, 25 May 1963", "Lagos, 1975", "Durban, 2002"], 1,
             "The OAU was founded at Addis Ababa on 25 May 1963.",
             feedback=["Accra hosted the All-African Peoples' Conference in 1958.", "",
                       "Lagos 1975 was the founding of ECOWAS.", "Durban 2002 was the launch of the AU."]),
        H("Practice questions"),
        PQ("Essay: Why was the OAU replaced by the African Union?",
           "Outline: failures over internal conflicts and Rwanda; end of the Cold War; economic marginalisation; "
           "leaders' initiatives at Sirte 1999; desire for a stronger institution. Judgement."),
        PQ("Essay: Compare the achievements of ECOWAS and CEMAC.",
           "Outline: ECOWAS larger, military role through ECOMOG, free movement protocols; CEMAC monetary union with "
           "the CFA franc and BEAC; both limited by politics and infrastructure. Judgement."),
        PQ("Short answer: Name the six member states of CEMAC.",
           "Cameroon, Central African Republic, Chad, Congo, Equatorial Guinea and Gabon."),
        SUM("The OAU (1963) promoted cooperation between sovereign states and supported liberation movements.",
            "Its non-interference principle limited action on internal conflicts.",
            "The AU (2002) added a right to intervene in grave circumstances.",
            "CEMAC, ECOWAS and SADC pursue regional economic integration; Cameroon belongs to CEMAC.",
            "The end of the Cold War in 1991 encouraged democratization and new regional responses."),
    ],
))
