"""Form 5 History: Post-Independence Cameroon (5 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

MODULE = "Post-Independence Cameroon"
FED = "Federal to unitary state"
MOD = "Modern transitions"

LESSONS = []

# ------------------------------------------------------------------ 1. The Federal Republic
LESSONS.append(lesson(
    module=MODULE,
    topic=FED,
    title="The Federal Republic of Cameroon, 1961–1972",
    slug="federal-republic-of-cameroon-1961-1972",
    minutes=20,
    summary="How the Federal Republic of Cameroon was organised from 1 October 1961, who led East and West Cameroon, how federal inspectors worked, and how power moved towards the centre.",
    objectives=[
        "Describe the structure of the Federal Republic of Cameroon (1961–1972)",
        "Name the main leaders of the federation and of West Cameroon",
        "Explain the role of the federal inspectors of administration",
        "Give balanced reasons why power moved towards the centre",
    ],
    key_concepts=["Federation", "Federal constitution", "East Cameroon", "West Cameroon", "Federal inspectors", "Centralization"],
    blocks=[
        H("Introduction"),
        T("When a student in Buea or Bamenda today hears the words 'the federal period', they are talking about eleven years of "
          "Cameroon's history, from 1961 to 1972. In those years the country had two federated states with two capitals, "
          "two governments and two assemblies, as well as a federal government above them."),
        T("This lesson is about how that system was built and how it worked in practice. The next lesson explains how it ended."),
        D("A **federation** is a state in which power is shared between a central (federal) government and regional (state) "
          "governments. Each level has its own institutions.", title="Federation"),
        D("A **constitution** is the set of basic rules that says how a country is governed and who holds power.", title="Constitution"),
        H("The federal constitution"),
        T("The federal constitution came into force on **1 October 1961**, the date of reunification. Southern Cameroons joined "
          "the Republic of Cameroon, and the two parts became **East Cameroon** and **West Cameroon**."),
        T("East Cameroon had its capital at **Yaoundé**. West Cameroon had its capital at **Buea**. Yaoundé was also the federal capital."),
        T("Each state had its own Prime Minister, its own government and its own legislature. The federal level had a President "
          "and a federal government."),
        KEY("Who led the federation?", "The two top posts at the federal level in 1961.", cards=[
            ["Federal President", "Ahmadou Ahidjo"],
            ["Federal Vice-President", "John Ngu Foncha"],
        ], note="Foncha was also the first Prime Minister of West Cameroon."),
        T("The federal government controlled key matters such as defence, foreign affairs, finance and higher education. "
          "The states handled the other matters. For the full list of federal and state powers, check your textbook."),
        IMG("f5h-federal-timeline.svg", alt="Timeline of the federation: 1 October 1961 start, Jua as West Cameroon Prime Minister in 1965, Muna in 1968, end of the federation in 1972",
            caption="Figure 1. The federal period and the three Prime Ministers of West Cameroon."),
        H("The leaders of West Cameroon"),
        T("West Cameroon had three Prime Ministers during the federation. They were John Ngu Foncha (1961–1965), "
          "Augustine Ngom Jua (1965–1968) and Solomon Tandeng Muna (1968–1972)."),
        T("The change in 1968 matters for exam answers. Ahidjo appointed Muna as Prime Minister of West Cameroon. "
          "This showed how much influence the federal President had over the states."),
        H("Federal inspectors and centralization"),
        T("**Federal Inspectors of Administration** were officials appointed by the President. They supervised administration "
          "in each state. This was one way in which the federal government kept an eye on the work of the states."),
        D("**Centralization** is the movement of decision-making power towards the central government and away from regions.",
          title="Centralization"),
        T("Historians agree that, over the years of the federation, real power moved towards the centre. Two signs were the "
          "role of the federal inspectors and the President's influence over who led West Cameroon."),
        KEY("Two views on the federal years", "A good answer gives both and does not take a side without evidence.", cards=[
            ["Supporters of the centre", "A strong centre was needed to unite two parts that had been ruled differently in the past, and to run a young and poor state."],
            ["Critics", "The states lost real power. Many Anglophones feel the guarantees given at reunification were slowly weakened."],
        ], note="Both views are part of the debate in Cameroon today."),
        EX("Model answer plan 1", intro="Describe the structure of the Federal Republic of Cameroon between 1961 and 1972.", steps=[
            S("Introduction", text="Say that the federal constitution came into force on 1 October 1961 and created two federated states."),
            S("The two states", text="East Cameroon (capital Yaoundé) and West Cameroon (capital Buea), each with its own Prime Minister, government and legislature."),
            S("The federal level", text="A federal President (Ahidjo) and Vice-President (Foncha), with Yaoundé as federal capital."),
            S("Federal powers", text="The federal government controlled matters such as defence, foreign affairs, finance and higher education."),
            S("Conclusion", text="The system lasted until 1972, but over time power moved towards the centre."),
        ]),
        EX("Model answer plan 2", intro="Explain how power moved towards the centre during the federal period.", steps=[
            S("Introduction", text="Define centralization and say that the federation (1961–1972) became more centralized over time."),
            S("Federal inspectors", text="Inspectors of administration, appointed by the President, supervised administration in each state."),
            S("The Prime Minister of West Cameroon", text="In 1968 Ahidjo appointed Muna, which showed the President's influence over the states."),
            S("Federal control of key matters", text="Defence, foreign affairs, finance and higher education were federal matters."),
            S("Balance", text="Supporters say a strong centre helped unity; critics say the states lost the guarantees given in 1961."),
            S("Conclusion", text="By 1972 the centre was already far stronger than the two states."),
        ]),
        H("Common mistakes"),
        MISTAKE("Giving the wrong capitals", "East Cameroon: Yaoundé. West Cameroon: Buea. Yaoundé was also the federal capital. Douala and Bamenda were not state capitals."),
        MISTAKE("Mixing up the posts", "Ahidjo was the federal President and Foncha the federal Vice-President. The Prime Ministers of West Cameroon were Foncha, Jua and Muna, in that order."),
        MISTAKE("One-sided answers", "Do not write only that the federation was good or only that it was bad. Give both views, with evidence for each."),
        QUIZ("Which list gives the Prime Ministers of West Cameroon in the correct order?",
             ["Jua, Foncha, Muna", "Foncha, Jua, Muna", "Foncha, Muna, Jua", "Muna, Jua, Foncha"], 1,
             "Foncha (1961–1965), then Jua (1965–1968), then Muna (1968–1972).",
             hint="The first one was also the federal Vice-President.",
             feedback=["Foncha came first, not Jua.", "", "Muna was the last Prime Minister, after Jua.", "This is the reverse order."]),
        QUIZ("What was the job of the federal inspectors of administration?",
             ["To command the army", "To supervise administration in each state", "To judge court cases", "To count votes in the 1961 plebiscite"], 1,
             "They were appointed by the President to supervise administration in each state.",
             feedback=["Defence was a federal matter, but the inspectors were not army commanders.", "",
                       "Judging cases was the work of the courts.", "The plebiscite was in 1961, before the federation started."]),
        H("Practice questions"),
        PQ("Name the two federated states of the Federal Republic of Cameroon and give the capital of each.",
           "East Cameroon, with its capital at Yaoundé, and West Cameroon, with its capital at Buea. Yaoundé was also the federal capital."),
        PQ("State two matters that were controlled by the federal government.",
           "Any two of: defence, foreign affairs, finance, higher education."),
        PQ("Who were the Prime Ministers of West Cameroon from 1961 to 1972?",
           "John Ngu Foncha (1961–1965), Augustine Ngom Jua (1965–1968) and Solomon Tandeng Muna (1968–1972)."),
        PQ("Give two signs that power moved towards the centre during the federal period.",
           "Federal inspectors of administration, appointed by the President, supervised the states; Ahidjo appointed Muna as Prime Minister of West Cameroon in 1968, showing the President's influence."),
        SUM("The federal constitution came into force on 1 October 1961, creating East Cameroon (Yaoundé) and West Cameroon (Buea).",
            "Ahidjo was federal President and Foncha federal Vice-President; the federal government controlled matters such as defence, foreign affairs, finance and higher education.",
            "West Cameroon's Prime Ministers were Foncha, Jua and Muna.",
            "Federal inspectors and the President's influence over the states show how power moved towards the centre.",
            "Supporters and critics of the federal system give different views; give both in an essay."),
    ],
))

# ------------------------------------------------------------------ 2. Single party and 1972
LESSONS.append(lesson(
    module=MODULE,
    topic=FED,
    title="The CNU, the 1972 referendum and the unitary state",
    slug="cnu-single-party-and-the-1972-referendum",
    minutes=22,
    summary="Why the CNU single party was formed on 1 September 1966, what happened in the referendum of 20 May 1972, and how supporters and critics explain the change to a unitary state.",
    objectives=[
        "Explain how and why the CNU was formed in 1966",
        "Describe the referendum of 20 May 1972 and the United Republic of Cameroon",
        "Give the reasons offered for the change to a unitary state",
        "Present the criticisms and the different views fairly",
    ],
    key_concepts=["Single party", "CNU", "Referendum", "Unitary state", "United Republic of Cameroon", "Province"],
    blocks=[
        H("Introduction"),
        T("Every year on 20 May, Cameroonians march past in Yaoundé, Bamenda, Garoua and every town for National Day. "
          "The date recalls the referendum of 20 May 1972, which ended the federation."),
        T("In the previous lesson you saw how the federal system worked and how power moved towards the centre. "
          "This lesson looks at two big steps: the single party of 1966 and the unitary state of 1972."),
        D("A **single party** system is one in which only one political party is allowed or has real power.", title="Single party"),
        D("A **unitary state** has one central government that holds sovereign power. Regions only have the powers the centre gives them.", title="Unitary state"),
        D("A **referendum** is a vote in which all voters accept or reject a proposal, such as a new constitution.", title="Referendum"),
        H("The CNU (1966)"),
        T("President Ahidjo called for one national party to build unity. On **1 September 1966** the main parties merged "
          "to form the **Cameroon National Union (CNU)**."),
        T("The parties that merged were Ahidjo's Union Camerounaise (UC) from East Cameroon and, from West Cameroon, the KNDP, "
          "the CPNC and the CUC."),
        KEY("Two ways of seeing the CNU", "Both views are used in exam answers.", cards=[
            ["Supporters said", "One party reduced ethnic and regional division and helped to build a national identity."],
            ["Critics said", "It ended open political competition. People who refused to join, including remaining UPC activists, faced repression."],
        ]),
        IMG("f5h-unitary-timeline.svg", alt="Timeline: federal constitution 1 October 1961, CNU formed 1 September 1966, referendum 20 May 1972, new constitution June 1972",
            caption="Figure 1. From federation to unitary state."),
        H("The referendum of 20 May 1972"),
        T("In May 1972 President Ahidjo announced a referendum on replacing the federation with a unitary state. "
          "It was held on **20 May 1972**. The official result was an overwhelming vote in favour. "
          "The exact figures are not needed here; check your textbook if your teacher asks for them."),
        T("A new constitution followed in June 1972. The country became the **United Republic of Cameroon**. "
          "The two federated states were abolished and replaced by provinces governed from Yaoundé."),
        H("Reasons and criticisms"),
        T("The government gave several reasons for the change. People in Cameroon still discuss all of them, "
          "so in an exam you should present them as the reasons that were given, not as unquestioned facts."),
        KEY("Reasons given and later criticisms", "Use both columns in a balanced answer.", cards=[
            ["Reasons given", "The high cost of running three governments; the need for national unity; faster economic development; the single party had already united political life."],
            ["Criticisms", "Many Anglophone critics argue that the federal constitution did not allow changes that harmed the federation, and that West Cameroon lost the guarantees agreed at Foumban."],
        ], note="Some writers also link the timing to economic factors such as oil discoveries. This is debated."),
        T("The government presented the referendum as the completion of national unity, freely approved by the people. "
          "A good answer explains both positions and does not decide for the reader."),
        T("What changed in practice? Provinces replaced the two states. More power went to the Presidency. "
          "20 May became National Day. The debate among Anglophones about lost autonomy has continued."),
        EX("Model answer plan 1", intro="Why did Cameroon change from a federal to a unitary state in 1972?", steps=[
            S("Introduction", text="State that the 20 May 1972 referendum replaced the Federal Republic with the United Republic of Cameroon."),
            S("Cost of federalism", text="Three governments were expensive for a poor country. This was one of the official reasons."),
            S("National unity", text="The government said one state would reduce divisions between Anglophones and Francophones."),
            S("The single party was already in place", text="The CNU (1966) had ended party competition, making the change easier."),
            S("Centralization already under way", text="Federal inspectors and presidential influence in West Cameroon had weakened the states."),
            S("Economic development", text="A single administration was presented as better for planning and development."),
            S("Conclusion", text="The official and critical views differ. The change is still debated, especially among Anglophones."),
        ]),
        EX("Model answer plan 2", intro="Discuss different views on the 1972 referendum.", steps=[
            S("Introduction", text="Say that the referendum of 20 May 1972 created a unitary state and that historians and citizens disagree about it."),
            S("Government view", text="It completed national unity and was freely approved by the people. The official result was an overwhelming vote in favour."),
            S("Critical view", text="Many Anglophone critics say the federal constitution did not allow changes that harmed the federation."),
            S("Foumban guarantees", text="Critics add that West Cameroon lost the guarantees agreed at Foumban."),
            S("Consequences", text="Provinces replaced the two states, the Presidency became stronger, and the Anglophone debate continued."),
            S("Conclusion", text="Present both positions with evidence and avoid picking a side without proof."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing 1961, 1966 and 1972", "1961: the federation. 1966: the CNU single party. 1972: the unitary state after the 20 May referendum."),
        MISTAKE("Writing 'Republic of Cameroon' for the 1972 name", "1972 gave the United Republic of Cameroon. The name Republic of Cameroon came later, in 1984."),
        MISTAKE("Taking sides", "Do not write 'Ahidjo cheated the people' or 'the Anglophones were wrong'. Say who holds each view and give their reasons."),
        QUIZ("Which parties merged to form the CNU on 1 September 1966?",
             ["UPC and SDF", "UC, KNDP, CPNC and CUC", "CPDM and UNDP", "KNC and OK only"], 1,
             "The CNU came from Ahidjo's Union Camerounaise and the three West Cameroon parties KNDP, CPNC and CUC.",
             hint="One East Cameroon party joined three from West Cameroon.",
             feedback=["The UPC stayed outside, and the SDF was founded only in 1990.", "",
                       "The CPDM dates from 1985; it was the CNU renamed.", "These did not form the CNU."]),
        QUIZ("What was the 1972 change in the country's form of government?",
             ["From a unitary state to a federation", "From a federation to a unitary state", "From one party to many parties", "From a republic to a kingdom"], 1,
             "The referendum of 20 May 1972 replaced the federation with a unitary state.",
             feedback=["This is the reverse of what happened.", "",
                       "Many parties returned only in 1990.", "Cameroon remained a republic."]),
        H("Practice questions"),
        PQ("Give the date and the full name of the party formed in 1966.",
           "The Cameroon National Union (CNU) was formed on 1 September 1966."),
        PQ("State three effects of the referendum of 20 May 1972.",
           "Creation of the United Republic of Cameroon; abolition of the two federated states and their replacement by provinces; more power in the Presidency. Also: 20 May became National Day and the Anglophone debate about lost autonomy continued."),
        PQ("Give two reasons that were offered for replacing the federation with a unitary state.",
           "Any two of: the high cost of running three governments; the need for national unity; faster economic development; the single party had already united political life."),
        PQ("Explain one criticism of the 1972 change.",
           "Many Anglophone critics say the federal constitution did not allow changes that harmed the federation, and that West Cameroon lost the guarantees agreed at Foumban."),
        SUM("The CNU single party was formed on 1 September 1966 from the UC, KNDP, CPNC and CUC.",
            "The referendum of 20 May 1972 replaced the federation with a unitary state; the official result was an overwhelming vote in favour.",
            "The country became the United Republic of Cameroon, with provinces replacing the two states.",
            "Reasons given: cost, unity, development, and an existing single party.",
            "Critics, especially many Anglophones, say the federal guarantees were lost; present both views fairly."),
    ],
))

# ------------------------------------------------------------------ 3. 1982 transition
LESSONS.append(lesson(
    module=MODULE,
    topic=MOD,
    title="The 1982 transition and the changes of the 1980s",
    slug="ahidjo-to-biya-transition-1982-and-the-1980s",
    minutes=20,
    summary="How Paul Biya succeeded Ahmadou Ahidjo in November 1982, why relations broke down, the failed coup of 6 April 1984, the 1984 name change and the birth of the CPDM in 1985.",
    objectives=[
        "Describe how power passed from Ahidjo to Biya in 1982",
        "Outline the breakdown between the two men and the coup attempt of April 1984",
        "State the 1984 change of name and explain why some people objected",
        "Explain how the CNU became the CPDM in 1985",
    ],
    key_concepts=["Constitutional succession", "Resignation", "Coup attempt", "Republic of Cameroon", "CPDM"],
    blocks=[
        H("Introduction"),
        T("From independence to 1982, Cameroon had only one President: Ahmadou Ahidjo. A whole generation of students grew up "
          "knowing no other head of state. Then, in 1982, the presidency changed hands without an election and without a war."),
        T("In the earlier lessons you studied the federal period and the unitary state of 1972. This lesson covers what happened "
          "next, in the 1980s: a change of President, a change of name, and a change of party name."),
        D("A **constitutional succession** is a change of leader that follows the rules written in the constitution.", title="Constitutional succession"),
        D("A **coup attempt** is an effort, often by soldiers, to remove a government by force and outside the constitution.", title="Coup attempt"),
        H("The transfer of power in November 1982"),
        T("On **4 November 1982** President Ahidjo announced his resignation."),
        T("Under the constitution, the Prime Minister, **Paul Biya**, became President. He was sworn in on **6 November 1982**. "
          "Ahidjo remained chairman of the CNU, the single party."),
        KEY("Why 'constitutional succession'?", "Check these points in an exam answer.", cards=[
            ["What happened", "Ahidjo resigned. The Prime Minister took over, as the constitution said."],
            ["What did not happen", "Biya did not seize power. There was no coup in 1982."],
        ]),
        H("The break between the two men"),
        T("Relations between Ahidjo and Biya soon broke down. In 1983 Ahidjo left the country and later resigned from the party."),
        T("On **6 April 1984** an attempted coup failed in Yaoundé. Ahidjo, accused of links to it, lived in exile until his death in 1989."),
        T("Note the order of events. The coup attempt came in 1984, after Biya had already been President for more than a year."),
        IMG("f5h-transition-timeline.svg", alt="Timeline: Ahidjo resigns and Biya is sworn in in November 1982, name change in February 1984, failed coup on 6 April 1984, CNU becomes the CPDM in 1985",
            caption="Figure 1. From the transfer of power to the birth of the CPDM."),
        H("A new name and a new party"),
        T("In **February 1984** a law changed the country's name from the United Republic of Cameroon to the "
          "**Republic of Cameroon**."),
        T("In **1985**, at a congress in Bamenda, the CNU became the **CPDM** (Cameroon People's Democratic Movement)."),
        KEY("Two views on the 1984 name", "Use both in a balanced answer.", cards=[
            ["Government view", "The change was a sign of national unity."],
            ["Objection", "Many Anglophones objected, because Republic of Cameroun had been the name of the Francophone state before reunification."],
        ]),
        EX("Model answer plan 1", intro="Describe how Paul Biya became President of Cameroon in 1982 and state two events that followed in the 1980s.", steps=[
            S("Introduction", text="Say that Ahidjo had been President since independence and resigned in 1982."),
            S("Resignation", text="On 4 November 1982 Ahidjo announced his resignation."),
            S("Succession", text="As Prime Minister, Biya was the constitutional successor. He was sworn in on 6 November 1982."),
            S("Event 1", text="The coup attempt of 6 April 1984 failed in Yaoundé. Ahidjo, accused of links to it, lived in exile until his death in 1989."),
            S("Event 2", text="In 1985 the CNU became the CPDM at a congress in Bamenda. In 1984 the country's name had become the Republic of Cameroon."),
        ]),
        EX("Model answer plan 2", intro="Explain why the change of name in 1984 was controversial.", steps=[
            S("Introduction", text="State that in February 1984 a law changed the name from the United Republic of Cameroon to the Republic of Cameroon."),
            S("Government view", text="It was presented as a sign of national unity."),
            S("Objection", text="Many Anglophones objected because Republic of Cameroun had been the name of the Francophone state before reunification."),
            S("Meaning behind the objection", text="For these critics the name seemed to ignore the union of two parts of the country."),
            S("Conclusion", text="The views differ. Explain both and give the reason each side offers."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Biya seized power in 1982", "Ahidjo resigned and Biya took over as constitutional successor. The failed coup was in April 1984."),
        MISTAKE("Mixing up the CNU and the CPDM", "The CNU was founded in 1966. It was renamed the CPDM at a congress in Bamenda in 1985."),
        MISTAKE("Mixing up the two names", "1972: United Republic of Cameroon. 1984: Republic of Cameroon."),
        QUIZ("What happened on 6 April 1984?",
             ["Biya was sworn in as President", "An attempted coup failed in Yaoundé", "The SDF was launched", "The CNU became the CPDM"], 1,
             "On 6 April 1984 an attempted coup failed in Yaoundé.",
             hint="This event came after Biya had been President for more than a year.",
             feedback=["Biya was sworn in on 6 November 1982.", "", "The SDF was launched in Bamenda on 26 May 1990.",
                       "The CNU became the CPDM in 1985."]),
        QUIZ("Which is the correct order of events?",
             ["CPDM formed, Ahidjo resigns, name change", "Ahidjo resigns, name change, CPDM formed", "Name change, CPDM formed, Ahidjo resigns", "Ahidjo resigns, CPDM formed, name change"], 1,
             "Ahidjo resigned in November 1982, the name changed in February 1984, and the CPDM was formed in 1985.",
             feedback=["The CPDM came last, in 1985.", "", "Ahidjo resigned first, in 1982.", "The name change came in 1984, before the CPDM in 1985."]),
        H("Practice questions"),
        PQ("How did Paul Biya become President in 1982?",
           "Ahidjo announced his resignation on 4 November 1982. As Prime Minister, Biya was his constitutional successor and was sworn in on 6 November 1982."),
        PQ("What happened on 6 April 1984, and what was the effect on Ahidjo?",
           "An attempted coup failed in Yaoundé. Ahidjo, accused of links to it, lived in exile until his death in 1989."),
        PQ("Give the name of the country before and after February 1984.",
           "Before: United Republic of Cameroon. After: Republic of Cameroon."),
        PQ("Why did many Anglophones object to the 1984 change of name?",
           "Republic of Cameroun had been the name of the Francophone state before reunification, so they saw the new name as ignoring the union of the two parts."),
        SUM("Ahidjo announced his resignation on 4 November 1982; Prime Minister Biya succeeded him and was sworn in on 6 November 1982.",
            "Relations between the two men broke down, and a coup attempt failed in Yaoundé on 6 April 1984.",
            "In February 1984 the country became the Republic of Cameroon; many Anglophones objected, while the government saw the name as a sign of unity.",
            "In 1985, at a congress in Bamenda, the CNU became the CPDM."),
    ],
))

# ------------------------------------------------------------------ 4. Liberalization 1990-1992
LESSONS.append(lesson(
    module=MODULE,
    topic=MOD,
    title="Political liberalization, 1990–1992",
    slug="political-liberalization-sdf-ghost-towns-tripartite",
    minutes=24,
    summary="Why multiparty politics returned: the launch of the SDF in May 1990, the liberty laws of December 1990, the ghost towns campaign, the Tripartite Conference of 1991 and the elections of 1992.",
    objectives=[
        "Explain the causes of the return to multiparty politics in 1990",
        "Describe the launch of the SDF and the liberty laws",
        "Explain the ghost towns campaign and the Tripartite Conference",
        "Present the 1992 elections and the different views of the reforms fairly",
    ],
    key_concepts=["Multipartism", "SDF", "Liberty laws", "Ghost towns", "Sovereign national conference", "Tripartite Conference"],
    blocks=[
        H("Introduction"),
        T("In the 1980s there was one legal party in Cameroon. A few years later a student in Douala could read many party "
          "newspapers and see many party flags. This lesson explains how that change came about between 1990 and 1992."),
        T("In the previous lesson the CNU became the CPDM in 1985. You will now see how that single-party system came under pressure."),
        D("**Multipartism** is a political system in which several parties may legally exist and compete in elections.", title="Multipartism"),
        D("The **liberty laws** were laws passed in December 1990 that allowed political parties and associations and eased controls on the press and public meetings.", title="Liberty laws"),
        D("The **ghost towns** (villes mortes) campaign of 1991 was an opposition strategy in which shops, markets and transport stayed closed on working days to pressure the government.", title="Ghost towns"),
        H("Why change came"),
        T("By 1990 the end of the Cold War and an economic crisis were pushing many African states towards democracy. "
          "Pressure came from inside and outside the country."),
        KEY("Causes of the 1990 change", "Use these as paragraph headings.", cards=[
            ["External", "The end of the Cold War, the fall of the Berlin Wall (1989) and the collapse of one-party regimes in Eastern Europe. Western donors linked aid to democratic reform."],
            ["Internal", "Economic crisis and structural adjustment, with falling commodity prices and hardship. Demands from students, lawyers and the press, and the launch of the SDF."],
        ]),
        H("The SDF and the liberty laws"),
        T("On **26 May 1990** the **Social Democratic Front (SDF)** was launched in Bamenda by John Fru Ndi. "
          "Several people were killed when security forces dispersed the launch."),
        T("In **December 1990** the National Assembly passed the liberty laws. They allowed the creation of political parties "
          "and associations and eased controls on the press and public meetings. Multiparty politics was legal again."),
        H("Ghost towns and the Tripartite Conference"),
        T("In 1991 opposition parties demanded a **sovereign national conference**, as in some other African countries. "
          "The government refused."),
        T("The opposition then organised the **ghost towns** campaign. It hit trade in Douala, Bamenda and other towns. "
          "The government responded with military command in several provinces."),
        T("To end the crisis, the government called a **Tripartite Conference** in Yaoundé. It met from late October to November 1991. "
          "It brought together three groups: the government, opposition parties and members of civil society."),
        T("The conference agreed on steps to restore calm. It also set up a committee to draft constitutional reforms. "
          "Some opposition leaders refused to sign."),
        IMG("f5h-liberalization-timeline.svg", alt="Timeline: SDF launched 26 May 1990, liberty laws December 1990, ghost towns 1991, Tripartite Conference October to November 1991, multiparty elections 1992",
            caption="Figure 1. The road to multiparty elections."),
        H("The elections of 1992"),
        T("Multiparty legislative and presidential elections followed in 1992. Biya won the presidential election of October 1992. "
          "The opposition, especially the SDF, contested the result."),
        KEY("Two views of the reforms", "Give both in an essay.", cards=[
            ["Supporters", "They see a peaceful, gradual transition that brought back several parties without a collapse of the state."],
            ["Critics", "They say reforms were limited and slow. Some opposition leaders refused to sign the Tripartite agreement."],
        ]),
        EX("Model answer plan 1", intro="Explain the factors that led to the return of multiparty politics in Cameroon in 1990.", steps=[
            S("Introduction", text="From 1966 the CNU, then the CPDM, was the only legal party. In December 1990 the liberty laws restored multipartism."),
            S("End of the Cold War", text="The fall of the Berlin Wall (1989) and the collapse of one-party regimes in Eastern Europe encouraged change."),
            S("Economic crisis", text="Falling commodity prices and structural adjustment caused hardship and discontent."),
            S("Internal pressure", text="Lawyers, students and journalists demanded reform, and the SDF was launched on 26 May 1990 in Bamenda."),
            S("External pressure", text="Western donors linked aid to democratic reform."),
            S("Conclusion", text="Internal and external factors together led to the liberty laws of December 1990."),
        ]),
        EX("Model answer plan 2", intro="(a) What was the Tripartite Conference? (b) State its results.", steps=[
            S("(a) Definition", text="A meeting in Yaoundé (October–November 1991) of the government, opposition parties and civil society."),
            S("(a) Why it was called", text="To end the ghost towns crisis and answer the opposition's demand for a sovereign national conference, which the government had refused."),
            S("(b) Return of calm", text="It agreed steps to restore calm and reduce unrest."),
            S("(b) Constitutional reform", text="A committee was set up to draft constitutional reforms."),
            S("(b) Limits", text="Some opposition leaders refused to sign, so divisions remained."),
        ]),
        H("Common mistakes"),
        MISTAKE("Dating the liberty laws to 1991", "The liberty laws were passed in December 1990. 1991 was the year of the ghost towns and the Tripartite Conference."),
        MISTAKE("Thinking the Tripartite Conference was a sovereign national conference", "The opposition demanded a sovereign national conference and the government refused. The Tripartite Conference was a different meeting called by the government."),
        MISTAKE("One-sided accounts", "Do not write that the transition was either perfect or a failure. Give the view of supporters and of critics."),
        QUIZ("When was the Social Democratic Front (SDF) launched?",
             ["4 November 1982", "6 April 1984", "26 May 1990", "18 January 1996"], 2,
             "The SDF was launched in Bamenda on 26 May 1990.",
             hint="The year is the same as that of the liberty laws.",
             feedback=["This is when Ahidjo announced his resignation.", "This was the failed coup attempt.", "",
                       "This is the date of the 1996 constitution."]),
        QUIZ("Which groups met at the Tripartite Conference?",
             ["Only the government and the army", "The government, opposition parties and civil society", "Cameroon, Nigeria and the UN", "Only opposition parties"], 1,
             "It brought together the government, opposition parties and members of civil society.",
             feedback=["The conference included the opposition and civil society.", "",
                       "It was a national meeting, not an international one.", "The government was also present."]),
        H("Practice questions"),
        PQ("Who launched the SDF, where and when?",
           "John Fru Ndi launched the Social Democratic Front in Bamenda on 26 May 1990."),
        PQ("What did the liberty laws of December 1990 allow?",
           "They allowed the creation of political parties and associations and eased controls on the press and public meetings."),
        PQ("Give two reasons for the ghost towns campaign of 1991.",
           "The government refused the opposition's demand for a sovereign national conference; the opposition wanted faster political reform."),
        PQ("State two results of the Tripartite Conference.",
           "It agreed steps to restore calm and set up a committee to draft constitutional reforms. Some opposition leaders refused to sign."),
        SUM("The end of the Cold War, economic crisis and internal pressure pushed Cameroon towards multipartism.",
            "The SDF was launched in Bamenda on 26 May 1990, and the liberty laws were passed in December 1990.",
            "In 1991 the government refused a sovereign national conference; the opposition organised ghost towns.",
            "The Tripartite Conference (October–November 1991) brought together the government, opposition and civil society.",
            "Multiparty elections followed in 1992; supporters and critics judge the reforms differently."),
    ],
))

# ------------------------------------------------------------------ 5. 1996 constitution
LESSONS.append(lesson(
    module=MODULE,
    topic=MOD,
    title="The 1996 constitution and decentralization",
    slug="constitution-of-1996-and-decentralization",
    minutes=20,
    summary="The All Anglophone Conference of 1993 and the constitution of 18 January 1996: the presidential term, the Senate, the Constitutional Council, regions and decentralization, and the 2008 amendment.",
    objectives=[
        "State the date of the 1996 constitution and the text it amended",
        "List the main provisions of the 1996 constitution",
        "Explain decentralization in a unitary state",
        "Present supporters' and critics' views fairly",
    ],
    key_concepts=["Constitution of 1996", "Senate", "Constitutional Council", "Region", "Decentralization", "All Anglophone Conference"],
    blocks=[
        H("Introduction"),
        T("The Tripartite Conference of 1991 set up a committee to draft constitutional reforms. The result came in 1996. "
          "This lesson looks at the constitution that followed and at the idea of decentralization."),
        T("In the previous lesson you studied the liberty laws, the ghost towns and the 1992 elections. "
          "Here the story turns from street politics to the rules of the state."),
        D("**Decentralization** means giving some powers and resources to regional or local bodies while the country keeps one central government.", title="Decentralization"),
        D("A **Senate** is a second chamber of the legislature, in addition to the National Assembly.", title="Senate"),
        H("The All Anglophone Conference, 1993"),
        T("Anglophone groups met at the **All Anglophone Conference** in Buea in 1993 to state their grievances."),
        T("This meeting shows that constitutional reform was also tied to the Anglophone question. "
          "For the details of what the conference declared, check your textbook. "
          "Different groups in Cameroon describe its meaning in different ways."),
        H("The constitution of 18 January 1996"),
        T("The constitution of **18 January 1996** amended the 1972 constitution."),
        IMG("f5h-constitution-timeline.svg", alt="Timeline: All Anglophone Conference in Buea 1993, constitution of 18 January 1996, 2008 amendment removing the limit on presidential terms",
            caption="Figure 1. From the 1993 conference to the 2008 amendment."),
        KEY("Main provisions", "These are the points the syllabus expects you to know.", cards=[
            ["The President", "A seven-year presidential term, renewable once."],
            ["New institutions", "A Senate and a Constitutional Council."],
            ["Regions", "Regions with elected councils: decentralization."],
            ["The state", "Cameroon is confirmed as a decentralized unitary state."],
        ], note="For the powers of each institution, check your textbook."),
        T("Many of these institutions were set up only years later. A 2008 amendment removed the limit on presidential terms."),
        H("Decentralization and the unitary state"),
        T("Compare three systems you have met. In the federation of 1961–1972, the states had their own governments and legislatures. "
          "In a unitary state, the centre holds the sovereign power. In a decentralized unitary state, some powers go to regions, "
          "but the state is still one."),
        KEY("Two views of the 1996 constitution", "Give both and take no side without evidence.", cards=[
            ["Supporters", "They see a peaceful, gradual reform that brought in new institutions and regions."],
            ["Critics", "They say reforms were limited and slow, and that many institutions took years to appear."],
        ]),
        EX("Model answer plan 1", intro="State four provisions of the constitution of 18 January 1996.", steps=[
            S("Introduction", text="Say that the constitution of 18 January 1996 amended the 1972 constitution."),
            S("Presidential term", text="A seven-year term, renewable once."),
            S("Senate", text="A Senate was created."),
            S("Constitutional Council", text="A Constitutional Council was created."),
            S("Regions", text="Regions with elected councils (decentralization). Cameroon was confirmed as a decentralized unitary state."),
            S("Later change", text="A 2008 amendment removed the limit on presidential terms."),
        ]),
        EX("Model answer plan 2", intro="Discuss how far the 1996 constitution answered the demands made in the early 1990s.", steps=[
            S("Introduction", text="Link the 1996 constitution to the Tripartite Conference (1991), which set up a committee for reforms, and to the All Anglophone Conference (1993)."),
            S("Supporters' view", text="New institutions and regions with elected councils were created; the reform was peaceful and gradual."),
            S("Critics' view", text="Reforms were limited and slow. Many institutions were set up only years later."),
            S("The unitary state", text="Cameroon was confirmed as a decentralized unitary state. For the Anglophone grievances, check your textbook for what each group wanted."),
            S("2008", text="The 2008 amendment removed the limit on presidential terms."),
            S("Conclusion", text="Give both views and state your judgement with evidence."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the 1996 constitution brought back the federation", "It confirmed a decentralized unitary state. Federalism ended in 1972."),
        MISTAKE("Mixing 1996 and 2008", "The seven-year term, renewable once, is from 1996. The removal of the limit on terms came with the 2008 amendment."),
        MISTAKE("Claiming details that are not in the syllabus", "If you do not remember the powers of the Senate or of the regions, do not guess. Check your textbook."),
        QUIZ("Which of these was created by the 1996 constitution?",
             ["The CNU", "A Senate", "The federal system", "The plebiscite"], 1,
             "The 1996 constitution created a Senate, a Constitutional Council and regions.",
             hint="Think of a second chamber of the legislature.",
             feedback=["The CNU was formed in 1966.", "", "Federalism ended in 1972.", "The plebiscite was in 1961."]),
        QUIZ("What does decentralization mean?",
             ["Giving all power to one person", "Moving some powers to regional or local bodies within one state", "Splitting a country into two", "Banning political parties"], 1,
             "Decentralization gives some powers to regions or local bodies while the country keeps one central government.",
             feedback=["That is closer to centralization.", "", "That describes a division of a country, not decentralization.", "That would be a single-party system."]),
        H("Practice questions"),
        PQ("On what date was the constitution that amended the 1972 text adopted?",
           "18 January 1996."),
        PQ("State three provisions of the 1996 constitution.",
           "Any three of: a seven-year presidential term, renewable once; a Senate; a Constitutional Council; regions with elected councils (decentralization); a decentralized unitary state."),
        PQ("What was the All Anglophone Conference and where was it held in 1993?",
           "A meeting of Anglophone groups in Buea in 1993 to state their grievances. For its declarations, check your textbook."),
        PQ("What change did the 2008 amendment make to the presidential term?",
           "It removed the limit on presidential terms."),
        SUM("The constitution of 18 January 1996 amended the 1972 constitution.",
            "It set a seven-year term renewable once, and created a Senate, a Constitutional Council and regions with elected councils.",
            "Cameroon was confirmed as a decentralized unitary state; many institutions were set up only years later.",
            "The All Anglophone Conference of 1993 in Buea voiced Anglophone grievances; for details, check your textbook.",
            "A 2008 amendment removed the limit on presidential terms."),
    ],
))
