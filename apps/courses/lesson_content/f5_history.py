"""GCE O Level History (0560), Form 5: Cameroon 1945 to the present and world history since 1870.

Draft content: every date, name and figure must be checked by a reviewer against the
official syllabus and standard textbooks before publishing.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

M_TRUST = "Trusteeship & Nationalism in Cameroon (1945–1961)"
M_POST = "Post-Independence Cameroon"
M_WORLD = "World History since 1870"

LESSONS = []

# ---------------------------------------------------------------------------
# 1. French Cameroun
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_TRUST,
    topic="French Cameroun",
    title="Nationalism and independence in French Cameroun (1945–1960)",
    slug="nationalism-in-french-cameroun",
    minutes=25,
    summary="How trade unions, the UPC and rival parties shaped nationalism in French Cameroun, "
            "from the 1955 ban and the maquis to the Loi-Cadre and independence on 1 January 1960.",
    objectives=[
        "Explain the rise of nationalism in French Cameroun after 1945",
        "Describe the aims and methods of the UPC and its rivals (BDC, ESOCAM)",
        "Explain the causes and results of the 1955 ban on the UPC",
        "Outline the steps from the Loi-Cadre (1956) to independence on 1 January 1960",
    ],
    key_concepts=["Trusteeship", "Nationalism", "UPC", "Maquis", "Loi-Cadre", "Internal autonomy"],
    blocks=[
        H("Introduction"),
        T("In 1945 the eastern part of Cameroon was ruled by France. Fifteen years later, on 1 January 1960, "
          "it became the independent Republic of Cameroun. This lesson explains how that happened.\n\n"
          "The story has two sides. One side is peaceful politics: elections, assemblies and talks with France. "
          "The other side is armed conflict: after the UPC was banned in 1955, some of its members took up arms. "
          "Both sides matter for the GCE examination."),
        D("A **trust territory** was a former League of Nations mandate placed under the United Nations after 1946. "
          "The administering power (here France) had to prepare the people for self-government or independence "
          "and report to the UN Trusteeship Council.", title="Trusteeship"),
        D("**Nationalism** is the desire of a people to govern themselves. In Cameroon it meant demands for "
          "independence and, for many, reunification of the French and British territories.", title="Nationalism"),
        D("The **maquis** was the armed underground resistance of UPC fighters in the forests of the "
          "Sanaga-Maritime and the Bamileke region after the party was banned.", title="Maquis"),
        H("Causes of nationalism after 1945"),
        T("The Second World War weakened France and spread ideas of freedom. The UN Charter (1945) and the "
          "Trusteeship Agreement (1946) promised progress towards self-government.\n\n"
          "Africans also had local grievances: forced labour, the indigénat (a system of punishments without trial), "
          "low wages and racial discrimination. Educated Cameroonians, ex-servicemen and workers wanted change."),
        T("Trade unions were the first organised voice. The USCC (Union des Syndicats Confédérés du Cameroun) "
          "grew from 1944 onwards. Strikes and riots in Douala in September 1945 showed the anger of workers. "
          "Many future UPC leaders, including Ruben Um Nyobè, were trade unionists."),
        H("The UPC and its rivals"),
        T("The **Union des Populations du Cameroun (UPC)** was founded in Douala on 10 April 1948. "
          "Ruben Um Nyobè became its Secretary-General. Félix-Roland Moumié and Ernest Ouandié were other key leaders.\n\n"
          "The UPC had three main demands: reunification of French and British Cameroons, a fixed date for independence, "
          "and better living standards for Africans. Um Nyobè presented these demands at the UN in New York, "
          "first in December 1952."),
        T("The French administration saw the UPC as dangerous and favoured rival parties. **ESOCAM** "
          "(Évolution Sociale Camerounaise, 1949) opposed the UPC. The **BDC** (Bloc Démocratique Camerounais), "
          "founded by Dr Louis-Paul Aujoulat in 1951, preferred gradual change in close partnership with France."),
        H("The 1955 ban and the maquis"),
        T("Tension grew between the UPC and the authorities. In May 1955 riots broke out in several towns, "
          "including Douala and Yaoundé, and many people were killed. The French government banned the UPC "
          "by decree in July 1955.\n\n"
          "UPC leaders fled to British Southern Cameroons (Kumba), but were expelled from there in 1957. "
          "They then worked in exile from Cairo, Conakry and Accra. Um Nyobè stayed in the Sanaga-Maritime "
          "forest and led the maquis. He was killed by French-led troops on 13 September 1958.\n\n"
          "The armed struggle continued after independence. Moumié died in Geneva in November 1960, "
          "after being poisoned. Ouandié led the remaining fighters until his capture; he was executed in "
          "Bafoussam in January 1971."),
        H("From the Loi-Cadre to independence"),
        T("The **Loi-Cadre** (Defferre framework law) of June 1956 gave French territories universal suffrage and "
          "elected territorial assemblies with more powers. Elections in Cameroun were held in December 1956; "
          "the UPC, still banned, could not take part.\n\n"
          "In 1957 Cameroun became a self-governing trust state. André-Marie Mbida became the first Prime Minister. "
          "In February 1958 he was replaced by Ahmadou Ahidjo of the Union Camerounaise. Cameroun gained full "
          "internal autonomy on 1 January 1959."),
        T("In March 1959 the UN General Assembly agreed to end trusteeship on 1 January 1960, without holding new "
          "elections first. Cameroun became independent on that date with Ahidjo as leader; he was elected President in May 1960."),
        KEY("Causes and effects at a glance", "Use these as paragraph points in essays.", cards=[
            ["Causes", "Effects of the Second World War; UN trusteeship promises; forced labour and discrimination; "
                       "trade unions; the work of the UPC at the UN."],
            ["Effects", "Ban of the UPC (1955) and armed conflict; French reforms (Loi-Cadre 1956); internal autonomy "
                        "(1959); independence on 1 January 1960 under Ahidjo."],
        ], note="Historians still debate how far the UPC's struggle sped up independence, and how to judge the "
                "French repression. Mention more than one view."),
        EX("Model answer plan 1", intro="Explain five reasons for the rise of nationalism in French Cameroun after 1945.", steps=[
            S("Introduction", text="Define nationalism; say that after 1945 Cameroonians increasingly demanded self-rule."),
            S("Effects of the Second World War", text="France was weakened; Cameroonian soldiers and workers saw that Europeans could be defeated."),
            S("UN trusteeship", text="The UN Charter and the 1946 Trusteeship Agreement promised self-government; nationalists could petition the UN."),
            S("Colonial grievances", text="Forced labour, the indigénat, low wages and racial discrimination caused anger."),
            S("Trade unions", text="The USCC organised workers; strikes in Douala in 1945; unions trained future leaders such as Um Nyobè."),
            S("Formation and work of the UPC", text="Founded in 1948 with clear aims (reunification, independence date); Um Nyobè's petitions to the UN."),
            S("Conclusion", text="Several causes worked together; the UPC turned discontent into an organised movement."),
        ]),
        EX("Model answer plan 2", intro="(a) Why was the UPC banned in 1955? (b) What were the consequences of the ban?", steps=[
            S("(a) Radical demands", text="The UPC demanded reunification and a fixed date for independence, which France rejected."),
            S("(a) French hostility and rival parties", text="The administration favoured ESOCAM and the BDC and saw the UPC as a threat to French interests."),
            S("(a) The May 1955 riots", text="Violent clashes in Douala, Yaoundé and other towns; France blamed the UPC and banned it in July 1955."),
            S("(b) Exile of leaders", text="Leaders fled to Southern Cameroons, then were expelled in 1957 to other African countries."),
            S("(b) Armed struggle", text="The maquis in the Sanaga-Maritime and Bamileke region; heavy loss of life; Um Nyobè killed in 1958."),
            S("(b) Moderate parties gain power", text="With the UPC excluded from the 1956 elections, Mbida and then Ahidjo led the government to independence."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up the UPC leaders' fates", "Um Nyobè was killed in the Sanaga-Maritime in 1958; Moumié died in Geneva in 1960; "
                "Ouandié was executed in 1971. Learn one fact for each."),
        MISTAKE("Saying Ahidjo led the UPC", "Ahidjo led the Union Camerounaise, a rival party. The UPC was founded in 1948 and led by Um Nyobè."),
        MISTAKE("Confusing 1 January 1959 and 1 January 1960", "1959 was full internal autonomy; 1960 was independence."),
        QUIZ("Which party was favoured by the French administration to oppose the UPC?",
             ["KNDP", "ESOCAM", "One Kamerun", "SDF"], 1,
             "ESOCAM (1949) was encouraged by the French administration to counter the UPC.",
             hint="Think of a party in French Cameroun before 1955.",
             feedback=["The KNDP was a party in British Southern Cameroons.", "",
                       "One Kamerun was a party in British Southern Cameroons linked to the UPC.",
                       "The SDF was founded in 1990."]),
        QUIZ("What did the Loi-Cadre of 1956 introduce in French Cameroun?",
             ["Immediate independence", "Universal suffrage and a more powerful elected assembly",
              "The ban of the UPC", "Reunification with Southern Cameroons"], 1,
             "The Loi-Cadre gave universal suffrage and more powers to elected territorial assemblies.",
             feedback=["Independence came in 1960, not 1956.", "",
                       "The UPC was banned in 1955, before the Loi-Cadre.",
                       "Reunification came on 1 October 1961."]),
        H("Practice questions"),
        PQ("When and where was the UPC founded, and who became its Secretary-General?",
           "In Douala on 10 April 1948. Ruben Um Nyobè became Secretary-General."),
        PQ("State three aims of the UPC.",
           "Reunification of the British and French Cameroons; independence with a fixed timetable; "
           "improved living and working conditions for Cameroonians."),
        PQ("Outline the main steps by which French Cameroun moved from trusteeship to independence between 1956 and 1960.",
           "Loi-Cadre of June 1956 and elections in December 1956; self-governing trust state with Mbida as Prime Minister in 1957; "
           "Ahidjo replaces Mbida in February 1958; full internal autonomy on 1 January 1959; UN resolution in March 1959 "
           "ending trusteeship; independence on 1 January 1960; Ahidjo elected President in May 1960."),
        SUM("After 1945, war, UN trusteeship and colonial grievances fuelled nationalism in French Cameroun.",
            "Trade unions and the UPC (1948, Um Nyobè) led the demand for reunification and independence.",
            "France favoured moderate rivals (ESOCAM, BDC) and banned the UPC in July 1955, leading to the maquis.",
            "The Loi-Cadre (1956), internal autonomy (1959) and a UN resolution led to independence on 1 January 1960 under Ahidjo.",
            "Views differ on the UPC's role: present both the armed struggle and the constitutional path."),
    ],
))

# ---------------------------------------------------------------------------
# 2. British Southern Cameroons
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_TRUST,
    topic="British Southern Cameroons",
    title="British Southern Cameroons: from the 1953 crisis to reunification",
    slug="british-southern-cameroons-to-reunification",
    minutes=25,
    summary="How Southern Cameroons separated from Nigeria's Eastern Region, the rivalry of the KNC, KNDP and OK, "
            "the UN plebiscite of 11 February 1961, the Foumban Conference and reunification on 1 October 1961.",
    objectives=[
        "Explain the causes and results of the 1953 Eastern House of Assembly crisis",
        "Compare the aims of the KNC, KNDP and OK and their leaders",
        "Describe the 1961 plebiscite and its results",
        "Explain the role of the Foumban Conference in reunification",
    ],
    key_concepts=["Eastern House crisis", "Benevolent neutrality", "KNC", "KNDP", "Plebiscite", "Foumban Conference", "Reunification"],
    blocks=[
        H("Introduction"),
        T("After the First World War, Britain ruled a strip of Kamerun along the Nigerian border. From 1946 it was a "
          "UN trust territory, but Britain governed it as part of Nigeria. The southern part, the **Southern Cameroons**, "
          "was attached to Nigeria's Eastern Region, with its capital at Enugu.\n\n"
          "Many people in towns such as Buea, Bamenda, Kumba and Mamfe felt neglected under this system. This lesson follows "
          "their path from protest in Enugu to reunification with the Republic of Cameroun in 1961."),
        D("A **plebiscite** is a direct vote by the people on one important question, such as which country to join.", title="Plebiscite"),
        D("**Reunification** is the joining together, on 1 October 1961, of the former British Southern Cameroons and the "
          "former French Cameroun into the Federal Republic of Cameroon.", title="Reunification"),
        H("The 1953 Eastern House of Assembly crisis"),
        T("In 1953 a political crisis split the ruling NCNC party in the Eastern House of Assembly at Enugu. "
          "The Southern Cameroons members, led by Dr Emmanuel Endeley, refused to take sides. They declared "
          "**benevolent neutrality** and later walked out.\n\n"
          "The crisis convinced them that Southern Cameroons needed its own government. At constitutional talks in 1953, "
          "Britain agreed. Under the 1954 constitution, Southern Cameroons became a quasi-federal territory with its own "
          "House of Assembly in Buea, and Endeley became Leader of Government Business."),
        H("The political parties and their leaders"),
        T("The **KNC** (Kamerun National Congress) was formed in 1953 and led by Endeley. At first it talked of "
          "reunification, but it came to favour close links with Nigeria. Later it merged with P. M. Kale's KPP "
          "to form the CPNC.\n\n"
          "The **KNDP** (Kamerun National Democratic Party) was founded in 1955 by John Ngu Foncha after he left the KNC. "
          "It wanted separation from Nigeria and, in time, reunification with French Cameroun. Augustine Ngom Jua and "
          "Solomon Tandeng Muna were leading KNDP figures."),
        T("The **OK** (One Kamerun), founded in 1957 by Ndeh Ntumazah, was close to the banned UPC and demanded "
          "immediate reunification and independence.\n\n"
          "The KNDP won the January 1959 elections and Foncha replaced Endeley as Premier. Talks between Foncha and "
          "Endeley at the Mamfe Conference (1959) failed to agree on the plebiscite questions, so the UN decided them."),
        H("The plebiscite of 11 February 1961"),
        T("The UN organised separate plebiscites in Southern and Northern Cameroons on 11 February 1961. Voters had only "
          "two choices: independence by joining Nigeria, or independence by joining the Republic of Cameroun. "
          "There was no option of separate independence.\n\n"
          "Southern Cameroons voted clearly to join the Republic of Cameroun. Northern Cameroons voted to join Nigeria, "
          "and became part of Nigeria on 1 June 1961. Cameroun protested about the northern result, without success."),
        TIP("Commonly cited results (check against your textbook): Southern Cameroons about 233,571 votes for Cameroun "
            "and 97,741 for Nigeria; Northern Cameroons about 146,296 for Nigeria and 97,659 for Cameroun.",
            title="Plebiscite figures"),
        H("Foumban and reunification"),
        T("Delegations led by Ahidjo and Foncha met at the **Foumban Conference** in July 1961 to discuss a constitution. "
          "They agreed on a federation of two states, East Cameroon and West Cameroon.\n\n"
          "Reunification took place on 1 October 1961. Ahidjo became President of the Federal Republic and Foncha became "
          "Vice-President and Prime Minister of West Cameroon."),
        KEY("Differing views of 1961", "Present these views fairly in essays.", cards=[
            ["Reunification as success", "Many saw it as the fulfilment of the nationalist dream of one Kamerun, "
                                         "freely chosen by a clear majority in the plebiscite."],
            ["Anglophone concerns", "Others argue that the lack of an independence option, the short Foumban talks and "
                                    "the unequal strength of the two sides left Anglophones with weak guarantees."],
        ], note="Historians and Cameroonians still debate these points; a good answer shows awareness of both."),
        EX("Model answer plan 1", intro="Explain the causes and consequences of the 1953 Eastern House of Assembly crisis.", steps=[
            S("Background", text="Southern Cameroons was ruled as part of Nigeria's Eastern Region; its members sat in the Enugu House."),
            S("Cause: neglect", text="Few schools, roads and jobs; people felt the region was ignored by the Eastern government."),
            S("Cause: NCNC split", text="A quarrel within the NCNC in 1953 forced members to take sides; Endeley's group chose benevolent neutrality."),
            S("Consequence: walk-out", text="The Southern Cameroons members withdrew and demanded a separate region."),
            S("Consequence: new constitution", text="The 1954 constitution gave Southern Cameroons its own House of Assembly in Buea, with Endeley as leader."),
            S("Consequence: rise of parties", text="The KNC was formed (1953) and the debate on Nigeria or reunification began, leading to the KNDP in 1955."),
        ]),
        EX("Model answer plan 2", intro="Compare the aims of the KNC and the KNDP between 1955 and 1961.", steps=[
            S("Leaders", text="KNC led by Endeley; KNDP led by Foncha, with Jua and Muna."),
            S("Attitude to Nigeria", text="The KNC came to favour association with Nigeria; the KNDP wanted secession from Nigeria."),
            S("Attitude to reunification", text="The KNDP supported reunification with French Cameroun; the KNC opposed rapid reunification."),
            S("Similarity", text="Both wanted self-government for Southern Cameroons and an end to rule from Enugu."),
            S("Outcome", text="The KNDP won in 1959 and its choice won the 1961 plebiscite in the south."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing KNC and KNDP", "KNC = Endeley = closer to Nigeria. KNDP = Foncha = reunification. The D in KNDP "
                "can remind you of the party that broke away (1955)."),
        MISTAKE("Saying the plebiscite offered independence alone", "There were only two options: join Nigeria or join the Republic of Cameroun."),
        MISTAKE("Mixing up plebiscite and reunification dates", "Plebiscite: 11 February 1961. Foumban: July 1961. Reunification: 1 October 1961."),
        QUIZ("Who founded the KNDP in 1955?",
             ["Emmanuel Endeley", "John Ngu Foncha", "Ndeh Ntumazah", "Ahmadou Ahidjo"], 1,
             "Foncha founded the KNDP after leaving Endeley's KNC.",
             feedback=["Endeley led the KNC.", "", "Ntumazah founded One Kamerun (OK).", "Ahidjo led French Cameroun."]),
        H("Practice questions"),
        PQ("What were the two options offered in the 1961 plebiscite?",
           "Achieving independence by joining the Federation of Nigeria, or by joining the independent Republic of Cameroun."),
        PQ("State two results of the Foumban Conference of July 1961.",
           "Agreement on a federal system with two states, East and West Cameroon; preparation of the federal constitution "
           "that came into force on 1 October 1961."),
        PQ("Why did Northern and Southern Cameroons vote differently in 1961? Give two reasons.",
           "The north had long been administered with Northern Nigeria and had close religious and ethnic ties there; "
           "in the south, the KNDP campaign for reunification and dissatisfaction with Eastern Nigeria favoured Cameroun."),
        SUM("Southern Cameroons was ruled as part of Nigeria's Eastern Region until the 1953 crisis.",
            "The 1954 constitution gave it its own House of Assembly in Buea under Endeley.",
            "KNC (Endeley) leaned to Nigeria; KNDP (Foncha) and OK (Ntumazah) wanted reunification.",
            "On 11 February 1961 the south voted to join Cameroun; the north joined Nigeria.",
            "After the Foumban Conference, reunification took place on 1 October 1961."),
    ],
))

# ---------------------------------------------------------------------------
# 3. Federal to unitary state
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_POST,
    topic="Federal to unitary state",
    title="From the Federal Republic to the United Republic (1961–1972)",
    slug="federal-to-unitary-state",
    minutes=25,
    summary="How the Federal Republic of Cameroon worked from 1961, why the CNU single party was formed in 1966, "
            "and why the 20 May 1972 referendum created a unitary state.",
    objectives=[
        "Describe the structure of the Federal Republic of Cameroon (1961–1972)",
        "Explain how and why the CNU single party was formed in 1966",
        "Give reasons for the 20 May 1972 referendum and describe its results",
        "Present different views on the end of federalism",
    ],
    key_concepts=["Federation", "Unitary state", "Single party", "CNU", "Referendum"],
    blocks=[
        H("Introduction"),
        T("Every year on 20 May, Cameroonians march past in Yaoundé, Bamenda, Garoua and every town for National Day. "
          "The date recalls the referendum of 20 May 1972, which ended the federation created at reunification.\n\n"
          "In this lesson you will see how the federation worked, how political power became concentrated, "
          "and why the country became a unitary state."),
        D("A **federation** is a state in which power is shared between a central government and regional (state) "
          "governments, each with its own institutions.", title="Federation"),
        D("A **unitary state** has one central government that holds sovereign power; regions only have the powers "
          "the centre gives them.", title="Unitary state"),
        D("A **referendum** is a vote in which all voters accept or reject a proposal, such as a new constitution.", title="Referendum"),
        H("The Federal Republic (1961–1972)"),
        T("The federal constitution came into force on 1 October 1961. There were two federated states: **East Cameroon** "
          "(capital Yaoundé) and **West Cameroon** (capital Buea). Each had its own Prime Minister, government and "
          "legislature. Yaoundé was also the federal capital.\n\n"
          "Ahmadou Ahidjo was federal President and John Ngu Foncha was Vice-President. The federal government controlled "
          "key matters such as defence, foreign affairs, finance and higher education."),
        T("West Cameroon had three Prime Ministers: Foncha (1961–1965), Augustine Ngom Jua (1965–1968) and "
          "Solomon Tandeng Muna (1968–1972). Ahidjo appointed Muna in 1968, which showed how much influence the "
          "federal President had over the states.\n\n"
          "Federal Inspectors of Administration, appointed by the President, also supervised administration in each "
          "state. Over time, real power moved towards the centre."),
        H("The single party: CNU (1966)"),
        T("Ahidjo called for one national party to build unity. On 1 September 1966 the main parties merged to form the "
          "**Cameroon National Union (CNU)**: Ahidjo's Union Camerounaise and, from West Cameroon, the KNDP, the CPNC "
          "and the CUC.\n\n"
          "Supporters said one party reduced ethnic and regional division. Critics said it ended open political "
          "competition. Opponents who refused to join, including remaining UPC activists, faced repression."),
        H("The 20 May 1972 referendum"),
        T("In May 1972 Ahidjo announced a referendum on replacing the federation with a unitary state. It was held on "
          "20 May 1972 and the official result was an overwhelming vote in favour.\n\n"
          "A new constitution followed in June 1972. The country became the **United Republic of Cameroon**. The two "
          "federated states were abolished and replaced by provinces governed from Yaoundé."),
        KEY("Causes and effects of the 1972 change", "Official reasons and later consequences.", cards=[
            ["Reasons given", "High cost of running three governments; the need for national unity; faster economic "
                              "development; the single party had already united political life."],
            ["Effects", "United Republic of Cameroon; provinces replaced the two states; more power in the Presidency; "
                        "20 May became National Day; lasting Anglophone debate about lost autonomy."],
        ], note="Some writers also link the timing to economic factors such as oil discoveries; this is debated."),
        T("Views on 1972 differ. The government presented it as the completion of national unity, freely approved by the "
          "people. Many Anglophone critics argue that the federal constitution did not allow changes that harmed the "
          "federation, and that West Cameroon lost the guarantees agreed at Foumban. A good answer explains both positions."),
        EX("Model answer plan 1", intro="Why did Cameroon change from a federal to a unitary state in 1972?", steps=[
            S("Introduction", text="State that the 20 May 1972 referendum replaced the Federal Republic with the United Republic of Cameroon."),
            S("Cost of federalism", text="Three governments and assemblies were expensive for a poor country."),
            S("National unity", text="Ahidjo argued that one state would reduce divisions between Anglophones and Francophones."),
            S("Single party already in place", text="The CNU (1966) had removed party competition, making change easier."),
            S("Centralisation of power", text="Federal inspectors and presidential control of West Cameroon had already weakened the states."),
            S("Economic development", text="A single administration was presented as better for planning and development."),
            S("Conclusion", text="Official and critical views differ; the change remains debated, especially among Anglophones."),
        ]),
        EX("Model answer plan 2", intro="Describe the formation of the CNU and explain its effects on politics in Cameroon.", steps=[
            S("Formation", text="1 September 1966: UC, KNDP, CPNC and CUC merged into the Cameroon National Union."),
            S("Effect: one-party state", text="Other parties disappeared; elections offered a single list."),
            S("Effect: national integration", text="Party structures covered both states and promoted a national identity."),
            S("Effect: stronger Presidency", text="Ahidjo controlled the party and the state, preparing the way for 1972."),
            S("Effect: limited freedom", text="Opposition and criticism were restricted until the 1990 liberty laws."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing 1961, 1966 and 1972", "1961: federation. 1966: CNU single party. 1972: unitary state after the 20 May referendum."),
        MISTAKE("Writing that the 1972 name was 'Republic of Cameroon'", "1972 gave the United Republic of Cameroon. The name Republic of Cameroon came in 1984."),
        QUIZ("Which parties merged to form the CNU in 1966?",
             ["UPC and SDF", "UC, KNDP, CPNC and CUC", "KNC and OK only", "CPDM and UNDP"], 1,
             "The CNU was formed from the Union Camerounaise and the three West Cameroon parties KNDP, CPNC and CUC.",
             feedback=["The UPC stayed outside and the SDF was founded only in 1990.", "",
                       "The KNC had already become part of the CPNC, and OK was not part of the merger.",
                       "The CPDM (1985) and UNDP (1990s) came much later."]),
        H("Practice questions"),
        PQ("Name the two federated states of the Federal Republic of Cameroon and their capitals.",
           "East Cameroon (Yaoundé) and West Cameroon (Buea)."),
        PQ("List the three Prime Ministers of West Cameroon in order.",
           "John Ngu Foncha (1961–1965), Augustine Ngom Jua (1965–1968), Solomon Tandeng Muna (1968–1972)."),
        PQ("State three effects of the 1972 referendum.",
           "Creation of the United Republic of Cameroon; abolition of the two federated states and creation of provinces; "
           "greater concentration of power in the Presidency (also: 20 May became National Day; continuing Anglophone debate)."),
        SUM("The Federal Republic (1961–1972) had two states, East and West Cameroon, under President Ahidjo.",
            "Power gradually moved to the centre, through federal inspectors and presidential influence.",
            "The CNU single party was formed on 1 September 1966.",
            "The 20 May 1972 referendum created the United Republic of Cameroon.",
            "The government saw 1972 as unity; many Anglophones saw a loss of the federal guarantees."),
    ],
))

# ---------------------------------------------------------------------------
# 4. Modern transitions
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_POST,
    topic="Modern transitions",
    title="Cameroon from 1982 to 1996: Biya, multipartism and the new constitution",
    slug="cameroon-modern-transitions-1982-1996",
    minutes=25,
    summary="The 1982 Ahidjo–Biya transition, the 1984 name change, the 1990 liberty laws, the ghost towns campaign, "
            "the Tripartite Conference of 1991 and the constitution of 18 January 1996.",
    objectives=[
        "Describe the 1982 transfer of power from Ahidjo to Biya and its aftermath",
        "Explain the return of multiparty politics in 1990",
        "Explain the ghost towns campaign and the Tripartite Conference",
        "State the main provisions of the 1996 constitution",
    ],
    key_concepts=["Constitutional succession", "Multipartism", "Liberty laws", "Ghost towns", "Tripartite Conference", "Decentralisation"],
    blocks=[
        H("Introduction"),
        T("In 1982 Cameroon had known only one President since independence. By 1996 it had many political parties, "
          "a new constitution and a very different political climate.\n\n"
          "This lesson explains these changes in order: a change of President, a change of name, a return to multiparty "
          "politics, a period of crisis and a negotiated constitutional reform."),
        D("**Multipartism** is a political system in which several parties may legally exist and compete in elections.", title="Multipartism"),
        D("The **ghost towns** (villes mortes) campaign of 1991 was an opposition strategy in which shops, markets and "
          "transport stayed closed on working days to pressure the government.", title="Ghost towns"),
        H("The 1982 transition"),
        T("On 4 November 1982 President Ahidjo announced his resignation. Under the constitution, the Prime Minister, "
          "**Paul Biya**, became President and was sworn in on 6 November 1982. Ahidjo remained chairman of the CNU.\n\n"
          "Relations between the two men soon broke down. In 1983 Ahidjo left the country and later resigned from the party. "
          "On 6 April 1984 an attempted coup failed in Yaoundé. Ahidjo, accused of links to it, lived in exile until his death in 1989."),
        T("In February 1984 a law changed the country's name from the United Republic of Cameroon to the "
          "**Republic of Cameroon**. In 1985, at a congress in Bamenda, the CNU became the **CPDM** "
          "(Cameroon People's Democratic Movement).\n\n"
          "Many Anglophones objected to the name change, because Republic of Cameroun had been the name of the "
          "Francophone state before reunification. The government presented it as a sign of national unity."),
        H("The return of multipartism (1990)"),
        T("By 1990 the end of the Cold War and economic crisis were pushing many African states towards democracy. "
          "On 26 May 1990 the **Social Democratic Front (SDF)** was launched in Bamenda by John Fru Ndi. Several people "
          "were killed when security forces dispersed the launch.\n\n"
          "In December 1990 the National Assembly passed the **liberty laws**. They allowed the creation of political "
          "parties and associations and eased controls on the press and public meetings."),
        H("Ghost towns and the Tripartite Conference (1991)"),
        T("In 1991 opposition parties demanded a sovereign national conference, as in some other African countries. "
          "The government refused. The opposition then organised the **ghost towns** campaign, which hit trade in Douala, "
          "Bamenda and other towns. The government responded with military command in several provinces.\n\n"
          "To end the crisis, the government called a **Tripartite Conference** in Yaoundé from late October to November 1991. "
          "It brought together the government, opposition parties and members of civil society. It agreed on steps to "
          "restore calm and set up a committee to draft constitutional reforms. Some opposition leaders refused to sign."),
        T("Multiparty legislative and presidential elections followed in 1992. Biya won the presidential election of "
          "October 1992; the opposition, especially the SDF, contested the result. Anglophone groups also met at the "
          "All Anglophone Conference in Buea in 1993 to state their grievances."),
        H("The 1996 constitution"),
        T("The constitution of **18 January 1996** amended the 1972 constitution. It set a seven-year presidential term, "
          "renewable once. It created a Senate, a Constitutional Council and regions with elected councils "
          "(decentralisation), and it confirmed the Republic of Cameroon as a decentralised unitary state.\n\n"
          "Many of these institutions were set up only years later. A 2008 amendment removed the limit on presidential terms."),
        KEY("Causes and effects of the 1990s changes", "Paragraph points for essays.", cards=[
            ["Causes", "End of the Cold War and global pressure for democracy; economic crisis and structural adjustment; "
                       "the SDF launch; demands from students, lawyers and the press."],
            ["Effects", "Liberty laws (1990); many new parties; ghost towns and unrest (1991); Tripartite Conference; "
                        "multiparty elections (1992); the 1996 constitution."],
        ], note="Supporters see a peaceful, gradual transition; critics say reforms were limited and slow. Give both views."),
        EX("Model answer plan 1", intro="Explain the factors that led to the return of multiparty politics in Cameroon in 1990.", steps=[
            S("Introduction", text="From 1966 the CNU, then CPDM, was the only legal party; in December 1990 the liberty laws restored multipartism."),
            S("End of the Cold War", text="The fall of the Berlin Wall (1989) and the collapse of one-party regimes in Eastern Europe encouraged change."),
            S("Economic crisis", text="Falling commodity prices and structural adjustment caused hardship and discontent."),
            S("Internal pressure", text="Lawyers, students, journalists and the launch of the SDF on 26 May 1990 in Bamenda."),
            S("External pressure", text="Western donors linked aid to democratic reform."),
            S("Conclusion", text="Internal and external factors together led to the liberty laws of December 1990."),
        ]),
        EX("Model answer plan 2", intro="(a) What was the Tripartite Conference? (b) State its results.", steps=[
            S("(a) Definition", text="A meeting in Yaoundé (October–November 1991) of government, opposition parties and civil society."),
            S("(a) Why it was called", text="To end the ghost towns crisis and opposition demands for a sovereign national conference."),
            S("(b) Return of calm", text="Agreement to lift some emergency measures and reduce unrest."),
            S("(b) Constitutional reform", text="A committee was set up to propose changes, which led to the 1996 constitution."),
            S("(b) Limits", text="Some opposition leaders rejected the agreement, so divisions remained."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Biya seized power in 1982", "Ahidjo resigned and Biya took over as constitutional successor. The failed coup was in April 1984."),
        MISTAKE("Mixing up the CNU and CPDM", "The CNU was founded in 1966; it was renamed CPDM in Bamenda in 1985."),
        MISTAKE("Dating the liberty laws to 1991", "The liberty laws were passed in December 1990. 1991 was the year of ghost towns and the Tripartite Conference."),
        QUIZ("When was the Social Democratic Front (SDF) launched?",
             ["4 November 1982", "6 April 1984", "26 May 1990", "18 January 1996"], 2,
             "The SDF was launched in Bamenda on 26 May 1990.",
             feedback=["This is when Ahidjo announced his resignation.", "This was the failed coup attempt.", "",
                       "This is the date of the 1996 constitution."]),
        QUIZ("Which of these was created by the 1996 constitution?",
             ["The CNU", "A Senate", "The federal system", "The plebiscite"], 1,
             "The 1996 constitution created a Senate, a Constitutional Council and regions.",
             feedback=["The CNU was formed in 1966.", "", "Federalism ended in 1972.", "The plebiscite was in 1961."]),
        H("Practice questions"),
        PQ("How did Paul Biya become President in 1982?",
           "Ahidjo resigned on 4 November 1982; as Prime Minister, Biya was his constitutional successor and was sworn in on 6 November 1982."),
        PQ("State three provisions of the 1996 constitution.",
           "Seven-year presidential term renewable once (changed in 2008); creation of a Senate; creation of a Constitutional Council; "
           "regions and decentralisation."),
        PQ("Give two reasons for the ghost towns campaign of 1991.",
           "The government refused the opposition's demand for a sovereign national conference; the opposition wanted faster "
           "political reform and fair elections."),
        SUM("Ahidjo resigned on 4 November 1982 and Biya succeeded him; a coup attempt failed on 6 April 1984.",
            "In 1984 the country became the Republic of Cameroon; in 1985 the CNU became the CPDM.",
            "The SDF launch (May 1990) and the liberty laws (December 1990) restored multipartism.",
            "Ghost towns (1991) led to the Tripartite Conference and multiparty elections in 1992.",
            "The 18 January 1996 constitution created a Senate, a Constitutional Council and regions."),
    ],
))

# ---------------------------------------------------------------------------
# 5. African decolonization
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_WORLD,
    topic="African decolonization",
    title="African decolonization, the OAU and the AU",
    slug="african-decolonization-oau-au",
    minutes=25,
    summary="Why African colonies won independence after 1945, the difference between peaceful transfers and armed "
            "struggles, and the work of the OAU (1963) and the African Union (2002).",
    objectives=[
        "Explain the causes of African decolonization after 1945",
        "Compare peaceful transfers of power with armed liberation struggles, using examples",
        "Describe the aims, achievements and weaknesses of the OAU",
        "Explain why the OAU was replaced by the African Union in 2002",
    ],
    key_concepts=["Decolonization", "Peaceful transfer", "Armed struggle", "Pan-Africanism", "OAU", "African Union"],
    blocks=[
        H("Introduction"),
        T("In 1945 only a few African states were independent, such as Ethiopia, Liberia and Egypt. By 1975 most of the "
          "continent was free. Cameroon was part of this wave in 1960, the year in which 17 African countries became independent.\n\n"
          "This lesson explains why decolonization happened, how it happened in different places, and how independent "
          "states tried to cooperate."),
        D("**Decolonization** is the process by which colonies gained independence from European colonial powers.", title="Decolonization"),
        D("**Pan-Africanism** is the idea that all Africans and people of African descent share common interests and "
          "should unite. It inspired leaders such as Kwame Nkrumah.", title="Pan-Africanism"),
        H("Causes of decolonization"),
        T("The Second World War weakened Britain and France and damaged the idea that Europeans could not be defeated. "
          "African soldiers who served abroad returned with new ideas and expectations.\n\n"
          "The UN Charter supported self-determination. The USA and USSR, the new superpowers, both criticised "
          "old-style colonial empires. India's independence in 1947 showed that a colony could win freedom."),
        T("Inside Africa, educated elites, trade unions and political parties organised. The Pan-African Congress held in "
          "Manchester in 1945 demanded independence. Economic grievances, such as low prices for cash crops and forced "
          "labour, also turned ordinary people against colonial rule."),
        H("Peaceful transfers of power"),
        T("In many colonies, independence was negotiated. Nationalist parties won elections, colonial powers introduced "
          "reforms step by step, and power was handed over at a fixed date.\n\n"
          "Ghana (formerly the Gold Coast) became independent on 6 March 1957 under Kwame Nkrumah, the first colony south of "
          "the Sahara to do so. Nigeria (1960), Senegal (1960) and most French West African territories also gained "
          "independence through negotiation."),
        H("Armed struggles"),
        T("Where there were many European settlers, or where the colonial power refused to leave, Africans often turned to "
          "armed struggle. In Algeria the FLN fought France from 1954 until independence in 1962. In Kenya the Mau Mau "
          "uprising began in 1952; Kenya became independent in 1963.\n\n"
          "Portugal refused to decolonize until a revolution in Lisbon in 1974. Angola, Mozambique and Guinea-Bissau "
          "won independence in 1974–1975 after long wars. Zimbabwe became independent in 1980 and Namibia in 1990."),
        T("Cameroon's path combined both methods: the constitutional route led by Ahidjo, and the armed struggle of the UPC."),
        H("The OAU and the African Union"),
        T("The **Organisation of African Unity (OAU)** was founded in Addis Ababa on 25 May 1963. Its aims included "
          "promoting unity among African states, defending their sovereignty and territorial integrity, and ending "
          "colonialism in Africa. It accepted the borders inherited from colonial rule.\n\n"
          "The OAU helped liberation movements through its Liberation Committee and opposed apartheid in South Africa. "
          "But it was criticised for weak powers, lack of money, and its policy of non-interference in members' internal affairs."),
        T("African leaders decided to create a stronger body. The **African Union (AU)** was launched in Durban, South Africa, "
          "on 9 July 2002. Unlike the OAU, the AU's Constitutive Act allows it to intervene in a member state in grave "
          "circumstances such as genocide and war crimes. It has organs such as the Pan-African Parliament and the "
          "Peace and Security Council."),
        KEY("Peaceful versus armed decolonization", "Compare, do not just list.", cards=[
            ["Peaceful transfer", "Negotiation, elections and reforms; few settlers; examples: Ghana 1957, Nigeria 1960, Senegal 1960."],
            ["Armed struggle", "Many settlers or a colonial power that refused to leave; examples: Algeria, Kenya, Angola, Mozambique, Zimbabwe."],
        ], note="Some historians stress African action; others stress the weakness and choices of the colonial powers. Most combine both."),
        EX("Model answer plan 1", intro="Explain five factors that led to the decolonization of Africa after 1945.", steps=[
            S("Introduction", text="Define decolonization; most of Africa became independent between 1956 and 1975."),
            S("Effects of the Second World War", text="Colonial powers weakened; African ex-servicemen returned with new ideas."),
            S("Role of the UN", text="The UN Charter supported self-determination; trusteeship territories had a timetable to self-rule."),
            S("Superpower attitudes", text="The USA and USSR opposed old colonial empires."),
            S("Nationalist movements", text="Educated leaders, parties and trade unions mobilised the people; Manchester Congress (1945)."),
            S("Example of Asia", text="Indian independence in 1947 inspired African nationalists."),
            S("Conclusion", text="Internal and external factors combined; the balance differed from colony to colony."),
        ]),
        EX("Model answer plan 2", intro="(a) State three aims of the OAU. (b) Why was the OAU replaced by the AU in 2002?", steps=[
            S("(a) Aims", text="Promote African unity; defend sovereignty and territorial integrity; eradicate colonialism; promote cooperation and development."),
            S("(b) Weak powers", text="The OAU could not enforce its decisions and had little money."),
            S("(b) Non-interference", text="It could not act against abuses inside member states."),
            S("(b) New challenges", text="Civil wars, economic problems and globalisation needed stronger cooperation."),
            S("(b) Result", text="The AU, launched in Durban in July 2002, has more powers, including intervention in grave circumstances."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing OAU and AU dates", "OAU: Addis Ababa, 25 May 1963. AU: Durban, 9 July 2002."),
        MISTAKE("Listing examples without explaining", "Do not just name countries. Say why each one followed a peaceful or armed route."),
        QUIZ("Which country was the first colony south of the Sahara to become independent, in 1957?",
             ["Nigeria", "Kenya", "Ghana", "Algeria"], 2,
             "Ghana became independent on 6 March 1957 under Kwame Nkrumah.",
             feedback=["Nigeria became independent in 1960.", "Kenya became independent in 1963.", "",
                       "Algeria is north of the Sahara and became independent in 1962."]),
        H("Practice questions"),
        PQ("Give two examples of countries that gained independence through armed struggle, with dates.",
           "Algeria (war from 1954, independence 1962); Kenya (Mau Mau from 1952, independence 1963); also Angola and Mozambique (1975) or Zimbabwe (1980)."),
        PQ("Where and when was the OAU founded?", "In Addis Ababa, Ethiopia, on 25 May 1963."),
        PQ("State two differences between the OAU and the AU.",
           "The OAU followed strict non-interference, while the AU may intervene in grave circumstances such as genocide; "
           "the AU has new organs such as the Pan-African Parliament and the Peace and Security Council."),
        SUM("The Second World War, the UN, the superpowers and African nationalism drove decolonization after 1945.",
            "Peaceful transfers took place where negotiation was possible, such as Ghana in 1957.",
            "Armed struggles took place where settlers or colonial powers resisted, such as Algeria, Kenya and the Portuguese colonies.",
            "The OAU (1963) fought colonialism but was limited by weak powers and non-interference.",
            "The African Union (2002) replaced it with stronger institutions."),
    ],
))

# ---------------------------------------------------------------------------
# 6. Cold War
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_WORLD,
    topic="Cold War",
    title="The Cold War: containment, crises and the collapse of the USSR",
    slug="the-cold-war",
    minutes=25,
    summary="The rivalry between the USA and the USSR from 1945 to 1991: containment, the Cuban Missile Crisis, "
            "proxy wars in Asia and Africa, and the collapse of the Soviet Union.",
    objectives=[
        "Explain the causes of the Cold War",
        "Describe the policy of containment and its main instruments",
        "Explain the causes and results of the Cuban Missile Crisis (1962)",
        "Explain why the USSR collapsed in 1991",
    ],
    key_concepts=["Cold War", "Containment", "Iron Curtain", "Proxy war", "Arms race", "Glasnost and perestroika"],
    blocks=[
        H("Introduction"),
        T("From 1945 to 1991 the world was divided between two superpowers: the capitalist USA and the communist USSR. "
          "They never fought each other directly, but their rivalry shaped wars, alliances and even African politics.\n\n"
          "During this period many African governments, including Cameroon's, had to decide how close to stay to each bloc."),
        D("The **Cold War** was the state of tension and rivalry between the USA and its allies and the USSR and its allies "
          "from 1945 to 1991, fought by propaganda, arms races and proxy wars rather than direct war.", title="Cold War"),
        D("**Containment** was the US policy of stopping the spread of communism to new countries.", title="Containment"),
        D("A **proxy war** is a conflict in which the superpowers support opposing sides without fighting each other directly.", title="Proxy war"),
        H("Causes of the Cold War"),
        T("The USA and USSR had opposing ideologies: capitalism and democracy against communism and one-party rule. "
          "They had been allies only to defeat Nazi Germany.\n\n"
          "After 1945 the USSR set up communist governments in Eastern Europe. Winston Churchill said in 1946 that an "
          "**iron curtain** had come down across Europe. The USA feared communism would spread further; the USSR feared "
          "Western attack and the US atomic bomb."),
        H("Containment in action"),
        T("In 1947 the **Truman Doctrine** promised US support to countries resisting communism. The **Marshall Plan** "
          "(1947) gave economic aid to rebuild Western Europe.\n\n"
          "The **Berlin Blockade** (1948–1949) was the first major crisis: the USSR cut land routes to West Berlin and the "
          "West responded with an airlift. In 1949 the USA and its allies formed **NATO**. The USSR and its allies "
          "formed the **Warsaw Pact** in 1955."),
        H("The Cuban Missile Crisis (1962)"),
        T("After Fidel Castro's revolution (1959), Cuba became an ally of the USSR. In October 1962 US spy planes found "
          "Soviet nuclear missile sites in Cuba, about 150 km from Florida.\n\n"
          "President Kennedy ordered a naval blockade (quarantine) of Cuba. For thirteen days the world feared nuclear war. "
          "Khrushchev agreed to remove the missiles; the USA promised not to invade Cuba and later removed its missiles from Turkey."),
        T("Results: a telephone hotline was set up between Washington and Moscow (1963), and a Partial Test Ban Treaty was "
          "signed in 1963. Both sides became more careful about direct confrontation."),
        H("Proxy wars"),
        T("The superpowers fought through others. In **Korea** (1950–1953) UN forces led by the USA fought North Korea and "
          "China. In **Vietnam** the USA fought communist forces until it withdrew in 1973; Vietnam was united under "
          "communist rule in 1975.\n\n"
          "In **Angola**, after independence in 1975, the USSR and Cuba supported the MPLA government while the USA and "
          "South Africa backed its rivals. In **Afghanistan** (1979–1989) Soviet troops fought rebels supported by the USA."),
        H("The collapse of the USSR"),
        T("Mikhail Gorbachev became Soviet leader in 1985. He introduced **glasnost** (openness) and **perestroika** "
          "(economic restructuring) to save a weak economy, and he reduced arms spending.\n\n"
          "In 1989 communist governments fell across Eastern Europe. The Berlin Wall was opened on 9 November 1989 and "
          "Germany reunified on 3 October 1990. After a failed coup in August 1991, Soviet republics declared independence. "
          "The USSR was dissolved in December 1991."),
        KEY("Why the USSR collapsed", "Combine several causes in your answer.", cards=[
            ["Economic", "Stagnant economy, shortages and the huge cost of the arms race and the war in Afghanistan."],
            ["Political", "Gorbachev's reforms allowed criticism; nationalism in the republics; the failed 1991 coup."],
        ], note="Historians weigh these differently: some stress Western pressure, others internal weakness."),
        EX("Model answer plan 1", intro="Explain the causes and results of the Cuban Missile Crisis of 1962.", steps=[
            S("Cause: Cuban revolution", text="Castro took power in 1959 and moved close to the USSR."),
            S("Cause: Bay of Pigs (1961)", text="A failed US-backed invasion made Cuba seek Soviet protection."),
            S("Cause: Soviet strategy", text="Khrushchev wanted to balance US missiles in Turkey and protect Cuba."),
            S("Event", text="October 1962: missiles discovered, US blockade, thirteen days of tension, deal to remove them."),
            S("Result: hotline and test ban", text="A Washington–Moscow hotline and the 1963 Partial Test Ban Treaty."),
            S("Result: caution", text="Both superpowers avoided direct confrontation afterwards; Cuba stayed communist."),
        ]),
        EX("Model answer plan 2", intro="Describe the methods used by the USA to contain communism between 1947 and 1962.", steps=[
            S("Truman Doctrine (1947)", text="Promise of aid to governments resisting communism, starting with Greece and Turkey."),
            S("Marshall Plan (1947)", text="Economic aid to Western Europe so poverty would not encourage communism."),
            S("Berlin Airlift (1948–1949)", text="Supplying West Berlin by air instead of giving it up."),
            S("Military alliances", text="NATO (1949) and other alliances surrounding the communist bloc."),
            S("War in Korea (1950–1953)", text="US-led UN forces stopped North Korea from taking the whole peninsula."),
            S("Cuba (1962)", text="Blockade to force removal of Soviet missiles."),
        ]),
        H("Common mistakes"),
        MISTAKE("Calling the Cold War a direct war", "The USA and USSR never fought each other directly. Use the words tension, rivalry and proxy war."),
        MISTAKE("Mixing up 1989 and 1991", "1989: Berlin Wall opened and Eastern Europe freed. 1991: the USSR itself dissolved."),
        QUIZ("Which Soviet leader agreed to remove missiles from Cuba in 1962?",
             ["Stalin", "Khrushchev", "Brezhnev", "Gorbachev"], 1,
             "Nikita Khrushchev led the USSR during the Cuban Missile Crisis.",
             feedback=["Stalin died in 1953.", "", "Brezhnev became leader in 1964.", "Gorbachev led the USSR from 1985."]),
        QUIZ("What did the term glasnost mean?",
             ["Economic restructuring", "Openness", "Arms race", "Containment"], 1,
             "Glasnost meant openness: more freedom of speech and information.",
             feedback=["That is perestroika.", "", "The arms race was the competition in weapons.", "Containment was a US policy."]),
        H("Practice questions"),
        PQ("Name the two military alliances of the Cold War and the years they were formed.",
           "NATO (1949), led by the USA; the Warsaw Pact (1955), led by the USSR."),
        PQ("Give two examples of proxy wars and the superpower involvement in each.",
           "Korea (1950–1953): USA and UN against North Korea, supported by China and the USSR. Angola (from 1975): USSR and Cuba "
           "supported the MPLA; USA and South Africa supported its rivals. (Also Vietnam, Afghanistan.)"),
        PQ("State three reasons for the collapse of the USSR.",
           "Economic weakness and shortages; the cost of the arms race and the war in Afghanistan; Gorbachev's reforms "
           "(glasnost and perestroika) that allowed criticism; nationalism in the republics; the failed coup of August 1991."),
        SUM("The Cold War (1945–1991) was a rivalry between the capitalist USA and the communist USSR.",
            "The USA used containment: the Truman Doctrine, the Marshall Plan, NATO and the Berlin Airlift.",
            "The Cuban Missile Crisis (October 1962) brought the world close to nuclear war.",
            "Proxy wars were fought in Korea, Vietnam, Angola and Afghanistan.",
            "Economic weakness and Gorbachev's reforms led to the collapse of the USSR in December 1991."),
    ],
))

# ---------------------------------------------------------------------------
# 7. Post-Cold War world
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_WORLD,
    topic="Post-Cold War world",
    title="The Arab–Israeli conflict and the post-Cold War world",
    slug="arab-israeli-conflict-post-cold-war",
    minutes=25,
    summary="The origins and main wars of the Arab–Israeli conflict, attempts at peace from Camp David to Oslo, "
            "and the new world order after 1991.",
    objectives=[
        "Explain the origins of the Arab–Israeli conflict",
        "Describe the main Arab–Israeli wars between 1948 and 1973",
        "Describe peace efforts from Camp David (1978) to the Oslo Accords (1993)",
        "Describe the main features of the world order after the Cold War",
    ],
    key_concepts=["Zionism", "Partition", "Intifada", "Peace process", "Unipolar world", "Globalisation"],
    blocks=[
        H("Introduction"),
        T("The Arab–Israeli conflict is one of the longest conflicts of the modern world. It is about land, security, "
          "refugees and national identity for two peoples, Israelis and Palestinians, and it has drawn in neighbouring states.\n\n"
          "The end of the Cold War in 1991 changed the world in which this conflict, and many others, took place. "
          "This lesson covers both subjects. It is a sensitive topic: aim to explain each side's view accurately."),
        D("**Zionism** is the movement, begun in the late nineteenth century, for a Jewish national homeland in Palestine.", title="Zionism"),
        D("An **intifada** (Arabic for uprising or shaking off) is a Palestinian popular uprising against Israeli occupation. "
          "The first began in 1987 and the second in 2000.", title="Intifada"),
        H("Origins of the conflict"),
        T("After the First World War, Britain governed Palestine under a League of Nations mandate. In the **Balfour Declaration** "
          "(1917) Britain had supported a national home for the Jewish people in Palestine, while also promising to respect the "
          "rights of the existing non-Jewish communities. Jewish immigration grew, and so did conflict with the Arab population.\n\n"
          "After the Holocaust, pressure for a Jewish state increased. In November 1947 the UN voted to partition Palestine into "
          "a Jewish state and an Arab state. Jewish leaders accepted the plan; Arab leaders rejected it."),
        H("The wars of 1948–1973"),
        T("Israel declared independence on 14 May 1948. Neighbouring Arab states attacked, and Israel won the war of 1948–1949. "
          "Hundreds of thousands of Palestinians fled or were expelled, creating a refugee problem that remains unresolved.\n\n"
          "In the **Suez Crisis** (1956) Israel, Britain and France attacked Egypt after Nasser nationalised the Suez Canal; "
          "pressure from the USA and USSR forced them to withdraw."),
        T("In the **Six-Day War** (June 1967) Israel defeated Egypt, Jordan and Syria. It occupied the Sinai, Gaza, the West Bank, "
          "East Jerusalem and the Golan Heights. In the **Yom Kippur War** (October 1973) Egypt and Syria attacked Israel. "
          "Arab oil producers then raised prices and cut supplies to countries that supported Israel."),
        H("The search for peace"),
        T("Through the **Camp David Accords** (1978), mediated by US President Carter, Egypt and Israel agreed to make peace. "
          "Their peace treaty of 1979 returned Sinai to Egypt. Egypt's President Sadat was assassinated in 1981.\n\n"
          "In the **Oslo Accords** (1993) Israel and the Palestine Liberation Organization (PLO) recognised each other, and a "
          "Palestinian Authority was created with limited self-rule. Jordan signed a peace treaty with Israel in 1994."),
        T("Key issues remained unsolved: borders, Jewish settlements in occupied territory, the status of Jerusalem, the return "
          "of refugees and security. The Second Intifada (2000) and later wars in Gaza showed that the conflict continued."),
        H("The post-Cold War order"),
        T("After the USSR collapsed in 1991, the USA was the only superpower. Some people described this as a **unipolar** world. "
          "In the Gulf War (1991) a US-led coalition, authorised by the UN, drove Iraq out of Kuwait.\n\n"
          "Other features followed: rapid **globalisation** of trade and communication; the spread of multiparty democracy, "
          "including in Africa; the growth of the European Union; the attacks of 11 September 2001 and the US-led 'war on terror'; "
          "and the economic rise of China, which led many to speak of a multipolar world."),
        KEY("Causes and effects at a glance", "Two topics, one pattern: rivalry and attempts at order.", cards=[
            ["Arab–Israeli conflict", "Causes: competing national claims, the 1947 partition, refugees, occupation. "
                                      "Effects: repeated wars, refugees, oil crisis (1973), peace treaties with Egypt and Jordan."],
            ["Post-Cold War order", "Causes: collapse of the USSR. Effects: US dominance, globalisation, democratisation in Africa, "
                                    "new threats such as terrorism, later multipolarity."],
        ], note="Israelis and Palestinians describe 1948 very differently. Present both narratives without taking sides."),
        EX("Model answer plan 1", intro="Explain the causes of the Arab–Israeli war of 1948–1949.", steps=[
            S("Competing claims", text="Zionists and Palestinian Arabs both claimed the same land."),
            S("British policy", text="The Balfour Declaration (1917) and the mandate encouraged Jewish immigration while also promising Arab rights."),
            S("Effect of the Holocaust", text="Increased international support for a Jewish state."),
            S("UN partition plan (1947)", text="Accepted by Jewish leaders, rejected by Arab leaders; violence grew."),
            S("British withdrawal and declaration of Israel", text="Britain left in May 1948; Israel declared independence on 14 May; Arab states attacked."),
        ]),
        EX("Model answer plan 2", intro="Describe the main features of the world after the end of the Cold War.", steps=[
            S("Introduction", text="The Cold War ended with the collapse of the USSR in December 1991."),
            S("US dominance", text="The USA became the only superpower; the Gulf War of 1991 showed its power."),
            S("Globalisation", text="Growth of world trade, the internet and multinational companies."),
            S("Democratisation", text="One-party states, including many in Africa, moved to multiparty politics in the early 1990s."),
            S("New conflicts and terrorism", text="Ethnic wars (Rwanda, former Yugoslavia) and the attacks of 11 September 2001."),
            S("Rise of new powers", text="China's economic growth and regional blocs such as the EU and AU point to a multipolar world."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up the 1967 and 1973 wars", "1967: Six-Day War, Israel occupied large territories. 1973: Yom Kippur War, Egypt and Syria attacked, followed by the oil crisis."),
        MISTAKE("Confusing Camp David and Oslo", "Camp David (1978): Egypt and Israel. Oslo (1993): Israel and the PLO."),
        QUIZ("Which agreement led to mutual recognition between Israel and the PLO?",
             ["Balfour Declaration", "Camp David Accords", "Oslo Accords", "UN partition plan"], 2,
             "The Oslo Accords of 1993 led to mutual recognition and the Palestinian Authority.",
             feedback=["The Balfour Declaration (1917) was a British statement of support for a Jewish national home.",
                       "Camp David (1978) led to peace between Egypt and Israel.", "",
                       "The 1947 partition plan proposed two states; the PLO did not yet exist."]),
        H("Practice questions"),
        PQ("Name three territories occupied by Israel in the Six-Day War of 1967.",
           "Any three of: Sinai Peninsula, Gaza Strip, West Bank, East Jerusalem, Golan Heights."),
        PQ("State two results of the Camp David Accords.",
           "Egypt and Israel signed a peace treaty in 1979; Israel returned Sinai to Egypt (also: Egypt was suspended from the Arab League for a time)."),
        PQ("Give three features of the post-Cold War world order.",
           "US dominance as the only superpower; globalisation; spread of multiparty democracy; growth of terrorism; rise of China and regional blocs."),
        SUM("The Arab–Israeli conflict grew from competing claims to Palestine under the British mandate.",
            "Israel was declared on 14 May 1948; wars followed in 1948–1949, 1956, 1967 and 1973.",
            "Camp David (1978) brought peace with Egypt; Oslo (1993) brought Israel–PLO recognition, but key issues remain.",
            "After 1991 the USA was the only superpower in a more globalised world.",
            "New challenges such as terrorism and the rise of China shaped the post-Cold War order."),
    ],
))
