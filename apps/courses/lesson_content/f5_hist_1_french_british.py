"""Form 5 History: Trusteeship & Nationalism in Cameroon (1945-1961), 6 lessons, one practice set each."""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

MODULE = "Trusteeship & Nationalism in Cameroon (1945–1961)"
FRENCH = "French Cameroun"
BRITISH = "British Southern Cameroons"

LESSONS = []

# ------------------------------------------------------------------ French Cameroun 1
LESSONS.append(lesson(
    module=MODULE,
    topic=FRENCH,
    title="The United Nations trusteeship and the rise of nationalism in French Cameroun",
    slug="french-cameroun-trusteeship-and-early-nationalism",
    minutes=22,
    summary="What trusteeship meant for French Cameroun after 1946, how trade unions and the first parties (UPC, ESOCAM, BDC) appeared, and why nationalism grew after 1945.",
    objectives=[
        "Explain what a trust territory was and what France had to do as administering power",
        "Describe the role of trade unions such as the USCC in the early protest movement",
        "Distinguish the UPC from its rivals ESOCAM and the BDC",
        "Explain the causes of nationalism in French Cameroun after 1945",
    ],
    key_concepts=["Trusteeship", "Nationalism", "Indigénat", "USCC", "UPC", "ESOCAM", "BDC"],
    blocks=[
        H("Introduction"),
        T("In 1945 the eastern part of Cameroon was ruled by France. Fifteen years later, on 1 January 1960, it became an independent state. "
          "This is the first of three lessons on French Cameroun. It explains the starting point: the trusteeship system and the first "
          "organised protests."),
        T("Picture a dockworker in Douala in 1945. He works long hours for low pay. He has no vote and no union that the "
          "administration respects. Many workers like him began to ask: why should Africans have no say in how they are governed?"),
        H("What was trusteeship?"),
        D("A **trust territory** was a former League of Nations mandate placed under the United Nations after 1946. "
          "The administering power (here France) had to prepare the people for self-government or independence "
          "and report to the UN Trusteeship Council.", title="Trusteeship"),
        T("The Trusteeship Agreement of 1946 made France answerable to the United Nations for French Cameroun. "
          "This was a real change from the mandate period. Cameroonians could now send petitions to the UN, "
          "and UN visiting missions could come to see conditions for themselves."),
        T("In practice France ruled French Cameroun in a way similar to its other African territories. "
          "That gap between the promise of trusteeship and daily life was one source of anger."),
        D("**Nationalism** is the desire of a people to govern themselves. In Cameroon it meant demands for "
          "independence and, for many, reunification of the French and British territories.", title="Nationalism"),
        H("Grievances under French rule"),
        T("Africans had many complaints. There was forced labour on roads and plantations. There was low pay and "
          "racial discrimination at work and in public life."),
        D("The **indigénat** was a system of punishments that officials could give to Africans without a trial.", title="Indigénat"),
        T("Educated Cameroonians, ex-servicemen and workers felt these injustices most. They wanted change, and they began to organise."),
        H("Trade unions: the first organised voice"),
        T("Trade unions were the first organised voice of protest. The **USCC** (Union des Syndicats Confédérés du Cameroun) "
          "grew from 1944 onwards. Strikes and riots in Douala in September 1945 showed the anger of workers."),
        T("Unions mattered for a second reason. They trained leaders. Many future UPC leaders, including Ruben Um Nyobè, were trade unionists."),
        IMG("f5h-french-nationalism-timeline.svg",
            alt="Timeline from 1944 to December 1952 showing the USCC, the Douala strikes, the Trusteeship Agreement, the founding of the UPC, ESOCAM and the BDC, and Um Nyobè at the UN",
            caption="Figure 1. From trade unions to political parties in French Cameroun."),
        H("The first political parties"),
        T("The **Union des Populations du Cameroun (UPC)** was founded in Douala on 10 April 1948. "
          "Ruben Um Nyobè became its Secretary-General. The next lesson studies the UPC in detail."),
        T("The French administration saw the UPC as dangerous and favoured rival parties. **ESOCAM** "
          "(Évolution Sociale Camerounaise, 1949) opposed the UPC. The **BDC** (Bloc Démocratique Camerounais), "
          "founded by Dr Louis-Paul Aujoulat in 1951, preferred gradual change in close partnership with France."),
        KEY("Causes of nationalism after 1945", "Use these as paragraph points in essays.", cards=[
            ["Outside events", "The Second World War weakened France and spread ideas of freedom. The UN Charter (1945) and the "
                               "Trusteeship Agreement (1946) promised progress towards self-government."],
            ["Local grievances", "Forced labour, the indigénat, low wages and racial discrimination."],
            ["Organisation", "Trade unions such as the USCC, then parties, above all the UPC (1948) and its petitions to the UN."],
        ], note="A strong answer links these causes: grievances gave anger, trusteeship gave hope, and organisations gave direction."),
        EX("Model answer plan 1", intro="Explain five reasons for the rise of nationalism in French Cameroun after 1945.", steps=[
            S("Introduction", text="Define nationalism; say that after 1945 Cameroonians increasingly demanded self-rule."),
            S("Effects of the Second World War", text="France was weakened; ideas of freedom spread among soldiers and workers."),
            S("UN trusteeship", text="The UN Charter and the 1946 Trusteeship Agreement promised self-government; nationalists could petition the UN."),
            S("Colonial grievances", text="Forced labour, the indigénat, low wages and racial discrimination caused anger."),
            S("Trade unions", text="The USCC organised workers; strikes in Douala in September 1945; unions trained future leaders such as Um Nyobè."),
            S("Formation and work of the UPC", text="Founded in 1948 with clear aims; Um Nyobè's petitions to the UN from December 1952."),
            S("Conclusion", text="Several causes worked together; the UPC turned discontent into an organised movement."),
        ]),
        EX("Model answer plan 2", intro="(a) What was a trust territory? (b) Explain how trusteeship helped Cameroonian nationalists.", steps=[
            S("(a) Definition", text="A former League of Nations mandate placed under the United Nations after 1946."),
            S("(a) Duty of France", text="France had to prepare the people for self-government or independence and report to the UN Trusteeship Council."),
            S("(b) A new forum", text="Nationalists could send petitions to the UN and speak there, as Um Nyobè did from December 1952."),
            S("(b) A standard to quote", text="The promise of progress towards self-government let nationalists say France was not keeping its duty."),
            S("(b) Limits", text="France still controlled the administration, and favoured moderate parties such as ESOCAM and the BDC."),
        ]),
        H("Common mistakes"),
        MISTAKE("Dating the UPC to 1945", "The Douala strikes were in September 1945. The UPC was founded later, on 10 April 1948."),
        MISTAKE("Mixing up the rival parties", "ESOCAM (1949) and the BDC (1951) were moderate parties favoured by France. "
                "The UPC (1948) demanded far-reaching change."),
        MISTAKE("Saying trusteeship meant independence", "Trusteeship was a UN system that required France to prepare the territory for self-government. "
                "Independence only came in 1960."),
        QUIZ("Which body was a trade union federation that grew from 1944 in French Cameroun?",
             ["BDC", "ESOCAM", "USCC", "KNC"], 2,
             "The USCC (Union des Syndicats Confédérés du Cameroun) grew from 1944 and organised workers.",
             hint="Its name includes the word for unions (syndicats).",
             feedback=["The BDC was a political party founded in 1951.", "ESOCAM was a political party founded in 1949.", "",
                       "The KNC was a party in British Southern Cameroons."]),
        QUIZ("Which statement about the BDC is correct?",
             ["It was founded by Um Nyobè in 1948", "It preferred gradual change in close partnership with France",
              "It was banned in July 1955", "It demanded a fixed date for independence"], 1,
             "The BDC, founded by Dr Louis-Paul Aujoulat in 1951, preferred gradual change in close partnership with France.",
             hint="Which parties did the French administration favour?",
             feedback=["Um Nyobè led the UPC, not the BDC.", "",
                       "The UPC was banned in July 1955.", "A fixed date for independence was a UPC demand."]),
        H("Practice questions"),
        PQ("What was the Trusteeship Agreement of 1946?",
           "An agreement under which France administered French Cameroun for the United Nations. France had to prepare the people for "
           "self-government or independence and report to the UN Trusteeship Council."),
        PQ("State three grievances of Cameroonians under French rule.",
           "Any three of: forced labour; the indigénat (punishments without trial); low wages; racial discrimination."),
        PQ("Why were trade unions important in the rise of nationalism?",
           "They were the first organised voice of workers (the USCC grew from 1944); strikes in Douala in September 1945 showed "
           "the strength of feeling; and they trained leaders, including Ruben Um Nyobè, who later led the UPC."),
        PQ("Name two parties favoured by the French administration against the UPC and say what one of them wanted.",
           "ESOCAM (1949) and the BDC (1951). The BDC, founded by Dr Louis-Paul Aujoulat, preferred gradual change in close partnership with France."),
        SUM("Trusteeship (from 1946) made France answerable to the UN for preparing Cameroonians for self-government.",
            "Forced labour, the indigénat, low wages and discrimination caused anger.",
            "Trade unions such as the USCC (from 1944) were the first organised voice; the Douala strikes were in September 1945.",
            "The UPC was founded on 10 April 1948; ESOCAM (1949) and the BDC (1951) were moderate rivals favoured by France.",
            "Nationalism grew from outside events, local grievances and organisation working together."),
    ],
))

# ------------------------------------------------------------------ French Cameroun 2
LESSONS.append(lesson(
    module=MODULE,
    topic=FRENCH,
    title="The UPC, repression and the maquis",
    slug="french-cameroun-upc-ban-and-maquis",
    minutes=22,
    summary="The aims of the UPC under Um Nyobè, the riots and ban of 1955, the armed struggle in the maquis, French counter-insurgency, and the fates of Um Nyobè, Moumié and Ouandié.",
    objectives=[
        "State the aims and methods of the UPC",
        "Explain why France banned the UPC in July 1955",
        "Describe the maquis and the French response to it",
        "Present the differing views on the UPC struggle and its repression fairly",
    ],
    key_concepts=["UPC", "Um Nyobè", "1955 ban", "Maquis", "Counter-insurgency", "Moumié", "Ouandié"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you met the first unions and parties of French Cameroun. This lesson follows the party that "
          "became the centre of the story: the UPC."),
        T("The UPC's story has two parts. The first is a peaceful campaign of petitions, meetings and speeches. "
          "The second begins after 1955, when the party was banned and some members took up arms. "
          "It is a sensitive topic, and Cameroonians still disagree about it. A good answer shows more than one view."),
        H("The aims of the UPC"),
        T("The **Union des Populations du Cameroun (UPC)** was founded in Douala on 10 April 1948. "
          "Ruben Um Nyobè was its Secretary-General. Félix-Roland Moumié and Ernest Ouandié were other key leaders."),
        T("The UPC had three main demands:"),
        KEY("The three main demands of the UPC", "Learn these three points.", cards=[
            ["Reunification", "Joining French and British Cameroons into one country."],
            ["Independence", "A fixed date for independence."],
            ["Living standards", "Better living standards for Africans."],
        ]),
        T("Um Nyobè took these demands to the United Nations in New York, first in December 1952. "
          "This was a peaceful, constitutional method. The UPC also held meetings and built local branches."),
        H("Why France banned the UPC"),
        T("France rejected the UPC's central demands. The administration favoured ESOCAM and the BDC and saw the UPC as a threat "
          "to French interests. Tension grew."),
        T("In May 1955 riots broke out in several towns, including Douala and Yaoundé, and many people were killed. "
          "France blamed the UPC. The French government banned the party by decree in July 1955."),
        D("The **maquis** was the armed underground resistance of UPC fighters in the forests of the "
          "Sanaga-Maritime and the Bamileke region after the party was banned.", title="Maquis"),
        H("Exile and the armed struggle"),
        T("After the ban, UPC leaders fled to British Southern Cameroons (Kumba), but were expelled from there in 1957. "
          "They then worked in exile from Cairo, Conakry and Accra."),
        T("Um Nyobè stayed in the Sanaga-Maritime forest and led the maquis. He was killed by French-led troops on 13 September 1958."),
        T("The armed struggle continued after independence. Moumié died in Geneva in November 1960, after being poisoned. "
          "Ouandié led the remaining fighters until his capture; he was executed in Bafoussam in January 1971."),
        H("French counter-insurgency"),
        D("**Counter-insurgency** means the military and police methods used by a government to defeat an armed rebellion. "
          "The French authorities called their campaign pacification.", title="Counter-insurgency"),
        T("French-led troops hunted the maquis in the forests of the Sanaga-Maritime and the Bamileke region. "
          "The fighting cost many lives. Historians disagree about how many, so this lesson gives no figures. "
          "Check your textbook for what your teacher expects."),
        KEY("Differing views of the UPC struggle", "A balanced answer presents more than one view.", cards=[
            ["Supporters of the UPC", "They see its leaders as patriots who demanded real independence and reunification, and who were "
                                      "repressed for it. They point to the heavy loss of life in the maquis regions."],
            ["Supporters of the authorities", "They say the armed struggle threatened order, and that the army's task was to restore peace "
                                              "and allow the state to move to independence."],
        ], note="Historians still debate how far the UPC's struggle sped up independence, and how to judge the French repression."),
        EX("Model answer plan 1", intro="(a) Why was the UPC banned in 1955? (b) What were the consequences of the ban?", steps=[
            S("(a) Radical demands", text="The UPC demanded reunification and a fixed date for independence, which France rejected."),
            S("(a) French hostility and rival parties", text="The administration favoured ESOCAM and the BDC and saw the UPC as a threat to French interests."),
            S("(a) The May 1955 riots", text="Violent clashes in Douala, Yaoundé and other towns; France blamed the UPC and banned it in July 1955."),
            S("(b) Exile of leaders", text="Leaders fled to Southern Cameroons, then were expelled in 1957 to other African countries."),
            S("(b) Armed struggle", text="The maquis in the Sanaga-Maritime and Bamileke region; heavy loss of life; Um Nyobè killed in 1958."),
            S("(b) Moderate parties gain power", text="With the UPC excluded from the 1956 elections, Mbida and then Ahidjo led the government to independence."),
        ]),
        EX("Model answer plan 2", intro="Discuss the role of Ruben Um Nyobè in the nationalist movement in French Cameroun.", steps=[
            S("Introduction", text="Um Nyobè was a trade unionist who became Secretary-General of the UPC when it was founded in Douala on 10 April 1948."),
            S("Peaceful methods", text="He presented the UPC's demands to the UN in New York, first in December 1952."),
            S("Aims", text="Reunification, a fixed date for independence and better living standards."),
            S("After the ban", text="He stayed in the Sanaga-Maritime forest and led the maquis."),
            S("His death", text="Killed by French-led troops on 13 September 1958."),
            S("Differing views", text="Supporters honour him as a patriot; others criticise the armed struggle. Give both views and a short conclusion."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up the UPC leaders' fates", "Um Nyobè was killed in the Sanaga-Maritime in 1958; Moumié died in Geneva in 1960; "
                "Ouandié was executed in 1971. Learn one fact for each."),
        MISTAKE("Taking one side", "Do not write only that the UPC were heroes or only that they were rebels. Show that people disagree "
                "and give the reason for each view."),
        MISTAKE("Giving invented numbers of dead", "Do not quote casualty figures you are not sure of. Say that many people died and that historians disagree on numbers."),
        QUIZ("When was the UPC banned?",
             ["April 1948", "May 1955", "July 1955", "September 1958"], 2,
             "France banned the UPC by decree in July 1955, after the May 1955 riots.",
             hint="It was after the riots, not at the same time.",
             feedback=["April 1948 is when the UPC was founded.", "The riots were in May 1955; the ban came two months later.", "",
                       "September 1958 is when Um Nyobè was killed."]),
        QUIZ("Which leader died in Geneva in November 1960 after being poisoned?",
             ["Ruben Um Nyobè", "Félix-Roland Moumié", "Ernest Ouandié", "Ahmadou Ahidjo"], 1,
             "Moumié died in Geneva in November 1960, after being poisoned.",
             hint="Think of the leader in exile abroad.",
             feedback=["Um Nyobè was killed in the Sanaga-Maritime in 1958.", "",
                       "Ouandié was executed in Bafoussam in January 1971.", "Ahidjo became head of government and then President."]),
        H("Practice questions"),
        PQ("When and where was the UPC founded, and who became its Secretary-General?",
           "In Douala on 10 April 1948. Ruben Um Nyobè became Secretary-General."),
        PQ("State three aims of the UPC.",
           "Reunification of the British and French Cameroons; independence with a fixed date; better living standards for Africans."),
        PQ("What was the maquis, and where was it fought?",
           "The armed underground resistance of UPC fighters after the party was banned. It was fought in the forests of the Sanaga-Maritime and the Bamileke region."),
        PQ("Give two different views about the UPC struggle.",
           "One view: the UPC leaders were patriots who demanded real independence and reunification and were repressed for it. "
           "Another view: the armed struggle threatened order and the army had to restore peace. Historians still debate these views."),
        SUM("The UPC was founded on 10 April 1948 under Um Nyobè, demanding reunification, a fixed date for independence and better living standards.",
            "After the riots of May 1955 France banned it in July 1955.",
            "Some members formed the maquis; leaders went into exile; French-led troops fought a campaign of pacification.",
            "Um Nyobè was killed in 1958, Moumié died in Geneva in 1960 and Ouandié was executed in 1971.",
            "Views differ on the UPC and on the repression: present both fairly."),
    ],
))

# ------------------------------------------------------------------ French Cameroun 3
LESSONS.append(lesson(
    module=MODULE,
    topic=FRENCH,
    title="The road to independence in French Cameroun",
    slug="french-cameroun-loi-cadre-to-independence",
    minutes=20,
    summary="How the Loi-Cadre of 1956, the governments of Mbida and Ahidjo and internal autonomy led to independence on 1 January 1960 under President Ahidjo.",
    objectives=[
        "Explain what the Loi-Cadre of June 1956 changed",
        "Name the first two heads of government and the party of Ahidjo",
        "Distinguish internal autonomy (1959) from independence (1960)",
        "Outline the steps from 1956 to the election of Ahidjo as President",
    ],
    key_concepts=["Loi-Cadre", "Universal suffrage", "Internal autonomy", "Mbida", "Ahidjo", "Independence"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson the UPC was banned and some of its members were fighting in the maquis. "
          "At the same time France was changing the way it ruled its territories. This lesson follows those political steps "
          "from 1956 to independence on 1 January 1960."),
        T("Many steps fall close together, and two important ones fall on 1 January of different years. Learn them in order. "
          "The timeline in Figure 1 helps."),
        H("The Loi-Cadre of 1956"),
        D("The **Loi-Cadre** (Defferre framework law) of June 1956 gave French territories universal suffrage and "
          "elected territorial assemblies with more powers.", title="Loi-Cadre"),
        D("**Universal suffrage** means that all adults have the right to vote.", title="Universal suffrage"),
        T("Elections in Cameroun were held in December 1956. The UPC was still banned, so it could not take part. "
          "This is a key point: the new assembly was chosen without the party that had made the loudest demands for independence."),
        H("Self-government and two Prime Ministers"),
        T("In 1957 Cameroun became a self-governing trust state. André-Marie Mbida became the first Prime Minister."),
        T("In February 1958 Mbida was replaced by Ahmadou Ahidjo of the Union Camerounaise. "
          "Textbooks give different accounts of why the change happened, so check what your teacher expects."),
        D("**Internal autonomy** means that a territory runs its own internal affairs, while a foreign power keeps some "
          "powers, such as defence and foreign policy. Cameroun gained full internal autonomy on 1 January 1959.",
          title="Internal autonomy",
          note="Do not confuse internal autonomy (1 January 1959) with independence (1 January 1960)."),
        IMG("f5h-french-road-to-independence.svg",
            alt="Timeline from the Loi-Cadre in June 1956 to Ahidjo's election as President in May 1960",
            caption="Figure 1. The road to independence, 1956 to 1960."),
        H("The end of trusteeship"),
        T("In March 1959 the UN General Assembly agreed to end trusteeship on 1 January 1960, without holding new "
          "elections first."),
        T("Cameroun became independent on that date with Ahidjo as leader. He was elected President in May 1960."),
        T("Independence did not end the conflict. The armed struggle of the maquis went on after independence, as you saw in the last lesson."),
        KEY("Causes and steps at a glance", "Use these as paragraph points in essays.", cards=[
            ["Causes of independence", "Effects of the Second World War; UN trusteeship; the pressure of the UPC and other nationalists; "
                                       "French reforms such as the Loi-Cadre."],
            ["Steps", "Loi-Cadre (1956); self-government (1957); internal autonomy (1 January 1959); UN decision (March 1959); independence (1 January 1960)."],
        ], note="Historians still debate how far the UPC's struggle sped up independence, and how far moderates and French reforms did. "
                "Mention more than one view."),
        EX("Model answer plan 1", intro="Outline the main steps by which French Cameroun moved from trusteeship to independence between 1956 and 1960.", steps=[
            S("Introduction", text="Say that France reformed its rule after 1955 and that moderate leaders took over."),
            S("Loi-Cadre, 1956", text="Universal suffrage and a more powerful elected assembly; elections in December 1956 without the banned UPC."),
            S("Self-government, 1957", text="Cameroun became a self-governing trust state; Mbida was the first Prime Minister."),
            S("Ahidjo, 1958", text="In February 1958 Ahidjo of the Union Camerounaise replaced Mbida."),
            S("Autonomy and UN decision, 1959", text="Full internal autonomy on 1 January 1959; in March 1959 the UN agreed to end trusteeship."),
            S("Independence, 1960", text="1 January 1960; Ahidjo elected President in May 1960. Conclude."),
        ]),
        EX("Model answer plan 2", intro="Explain why the Loi-Cadre of 1956 was important for the political history of French Cameroun.", steps=[
            S("What it was", text="A French framework law (the Defferre law) of June 1956 for French territories."),
            S("Political change", text="It gave universal suffrage and elected assemblies with more powers."),
            S("Results in Cameroun", text="Elections in December 1956; the next steps led to self-government in 1957."),
            S("The UPC", text="The UPC was banned and could not take part, so moderate parties led the new institutions."),
            S("Conclusion", text="It started the transfer of power that ended in independence, but it also divided opinion because of the exclusion of the UPC."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing 1 January 1959 and 1 January 1960", "1959 was full internal autonomy; 1960 was independence."),
        MISTAKE("Saying Ahidjo led the UPC", "Ahidjo led the Union Camerounaise, a rival party. The UPC was led by Um Nyobè and, later, Moumié and Ouandié."),
        MISTAKE("Putting the Loi-Cadre before the ban", "The ban was in July 1955. The Loi-Cadre came in June 1956, so the UPC could not take part in the first elections."),
        QUIZ("Who was the first Prime Minister of the self-governing trust state of Cameroun in 1957?",
             ["Ahmadou Ahidjo", "Ruben Um Nyobè", "André-Marie Mbida", "Louis-Paul Aujoulat"], 2,
             "André-Marie Mbida became the first Prime Minister in 1957. Ahidjo replaced him in February 1958.",
             hint="Ahidjo was his successor.",
             feedback=["Ahidjo became Prime Minister in February 1958.", "Um Nyobè led the UPC and was never a Prime Minister.", "",
                       "Aujoulat founded the BDC."]),
        QUIZ("What happened on 1 January 1959?",
             ["Independence", "The ban of the UPC", "Full internal autonomy", "Ahidjo was elected President"], 2,
             "Cameroun gained full internal autonomy on 1 January 1959.",
             hint="Independence followed exactly one year later.",
             feedback=["Independence was on 1 January 1960.", "The UPC was banned in July 1955.", "",
                       "Ahidjo was elected President in May 1960."]),
        H("Practice questions"),
        PQ("What did the Loi-Cadre of June 1956 introduce?",
           "Universal suffrage and elected territorial assemblies with more powers."),
        PQ("Why could the UPC not take part in the elections of December 1956?",
           "It was still banned, as it had been since July 1955."),
        PQ("State two differences between internal autonomy and independence.",
           "Internal autonomy (1 January 1959): the territory ran its internal affairs but France kept some powers, and the territory was still under UN "
           "trusteeship. Independence (1 January 1960): trusteeship ended and Cameroun became a fully independent state."),
        PQ("Write the following in the correct order: independence; Mbida becomes Prime Minister; the Loi-Cadre; Ahidjo replaces Mbida.",
           "The Loi-Cadre (1956); Mbida becomes Prime Minister (1957); Ahidjo replaces Mbida (February 1958); independence (1 January 1960)."),
        SUM("The Loi-Cadre (June 1956) brought universal suffrage and a more powerful elected assembly; elections followed in December 1956 without the banned UPC.",
            "Mbida was Prime Minister in 1957; Ahidjo of the Union Camerounaise replaced him in February 1958.",
            "Full internal autonomy came on 1 January 1959; the UN agreed in March 1959 to end trusteeship.",
            "Cameroun became independent on 1 January 1960; Ahidjo was elected President in May 1960.",
            "Views differ on how far the UPC struggle, moderates and French reforms each brought independence."),
    ],
))

# ------------------------------------------------------------------ British Southern Cameroons 1
LESSONS.append(lesson(
    module=MODULE,
    topic=BRITISH,
    title="British rule and the 1953 Eastern House of Assembly crisis",
    slug="southern-cameroons-nigeria-rule-and-1953-crisis",
    minutes=20,
    summary="How Britain ruled Southern Cameroons as part of Nigeria's Eastern Region, why the 1953 crisis in Enugu changed this, and how the 1954 constitution created a House of Assembly in Buea.",
    objectives=[
        "Describe how Southern Cameroons was administered with Nigeria",
        "Explain the causes of the 1953 Eastern House of Assembly crisis",
        "Explain the meaning of benevolent neutrality",
        "Describe the 1954 constitution and the Buea assembly",
    ],
    key_concepts=["Trust territory", "Eastern Region", "Enugu", "Benevolent neutrality", "1954 constitution", "House of Assembly"],
    blocks=[
        H("Introduction"),
        T("Now we turn to the other side of Cameroon. After the First World War, Britain ruled a strip of Kamerun along the Nigerian border. "
          "From 1946 it was a UN trust territory, as French Cameroun was."),
        T("But Britain governed it as part of Nigeria. The southern part, the **Southern Cameroons**, "
          "was attached to Nigeria's Eastern Region, with its capital at Enugu."),
        T("Many people in towns such as Buea, Bamenda, Kumba and Mamfe felt neglected under this system. "
          "This lesson explains how the crisis of 1953 led to a government of their own."),
        H("Southern Cameroons inside Nigeria"),
        T("Southern Cameroons had no capital of its own. Its representatives sat in the Eastern House of Assembly at Enugu, "
          "far from the Cameroons, together with members from Nigeria."),
        T("People complained that the region received little attention. There were few schools, roads and jobs compared with their needs. "
          "They felt that decisions were taken by others, a long way away."),
        D("A **trust territory** under British administration was governed by Britain for the United Nations. "
          "Britain had to prepare the people for self-government and report to the UN.", title="British trusteeship"),
        H("The 1953 crisis"),
        T("In 1953 a political crisis split the ruling NCNC party in the Eastern House of Assembly at Enugu. "
          "The Southern Cameroons members, led by Dr Emmanuel Endeley, refused to take sides."),
        D("**Benevolent neutrality** was the position of Endeley's group: they refused to take sides in the NCNC split. "
          "They later walked out of the Eastern House.", title="Benevolent neutrality"),
        T("The crisis convinced them that Southern Cameroons needed its own government. At constitutional talks in 1953, Britain agreed."),
        IMG("f5h-southern-cameroons-1946-1954.svg",
            alt="Timeline: 1946 trust territory, 1953 crisis in Enugu, 1953 constitutional talks, 1954 new constitution with a Buea assembly",
            caption="Figure 1. From trust territory to the Buea assembly."),
        H("The 1954 constitution and the Buea assembly"),
        T("Under the 1954 constitution, Southern Cameroons became a quasi-federal territory with its own "
          "House of Assembly in Buea. Endeley became Leader of Government Business."),
        D("**Quasi-federal** means partly federal: Southern Cameroons had its own assembly for local matters, but was still linked "
          "to Nigeria.", title="Quasi-federal"),
        T("This was a real step forward, but it was not independence. Southern Cameroons was still tied to Nigeria. "
          "The debate now turned to the next question: should it join Nigeria or join Cameroun? That is the subject of the next lesson."),
        KEY("Causes and consequences of the 1953 crisis", "Use these as paragraph points.", cards=[
            ["Causes", "Neglect inside the Eastern Region; the NCNC split in Enugu; the wish for a government of their own."],
            ["Consequences", "Benevolent neutrality and the walk-out; constitutional talks in 1953; the 1954 constitution; "
                             "a House of Assembly in Buea; Endeley as Leader of Government Business."],
        ]),
        EX("Model answer plan 1", intro="Explain the causes and consequences of the 1953 Eastern House of Assembly crisis.", steps=[
            S("Background", text="Southern Cameroons was ruled as part of Nigeria's Eastern Region; its members sat in the Enugu House."),
            S("Cause: neglect", text="Few schools, roads and jobs; people felt the region was ignored by the Eastern government."),
            S("Cause: NCNC split", text="A quarrel within the NCNC in 1953 forced members to take sides; Endeley's group chose benevolent neutrality."),
            S("Consequence: walk-out", text="The Southern Cameroons members withdrew and wanted a government of their own."),
            S("Consequence: new constitution", text="The 1954 constitution gave Southern Cameroons its own House of Assembly in Buea, with Endeley as leader."),
            S("Conclusion", text="The crisis separated Southern Cameroons from the Eastern Region and opened the debate on its future."),
        ]),
        EX("Model answer plan 2", intro="Describe how Southern Cameroons was governed between 1946 and 1954.", steps=[
            S("1946", text="Became a UN trust territory under Britain."),
            S("Administration with Nigeria", text="Governed as part of Nigeria; the southern part belonged to the Eastern Region, capital Enugu."),
            S("Representation", text="Its members sat in the Eastern House of Assembly in Enugu."),
            S("Complaints", text="Neglect and distance from decision making."),
            S("After 1954", text="Quasi-federal status, own House of Assembly in Buea, Endeley Leader of Government Business."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying Southern Cameroons became independent in 1954", "The 1954 constitution gave it its own assembly in Buea. It remained linked to Nigeria."),
        MISTAKE("Thinking benevolent neutrality means support", "Endeley's group refused to take sides in the NCNC split; they did not support either side."),
        MISTAKE("Mixing up the regions", "The southern part was attached to the Eastern Region (Enugu), not to Northern Nigeria."),
        QUIZ("Before 1954, in which city did Southern Cameroons members sit?",
             ["Buea", "Enugu", "Yaoundé", "Douala"], 1,
             "They sat in the Eastern House of Assembly at Enugu, capital of Nigeria's Eastern Region.",
             hint="It is the capital of the Eastern Region.",
             feedback=["Buea became the seat of the Southern Cameroons House of Assembly only after 1954.", "",
                       "Yaoundé was in French Cameroun.", "Douala was in French Cameroun."]),
        QUIZ("What did the 1954 constitution give Southern Cameroons?",
             ["Independence", "Membership of the French Union", "Its own House of Assembly in Buea", "A plebiscite"], 2,
             "Southern Cameroons became quasi-federal, with its own House of Assembly in Buea.",
             hint="Think of the town named in the lesson.",
             feedback=["Independence came only through the 1961 plebiscite.", "The French Union concerned French territories.", "",
                       "The plebiscite was held on 11 February 1961."]),
        H("Practice questions"),
        PQ("Under which Nigerian region was Southern Cameroons administered, and what was its capital?",
           "The Eastern Region, with its capital at Enugu."),
        PQ("What was benevolent neutrality?",
           "Endeley's group in the Eastern House refused to take sides in the 1953 NCNC split. They later walked out."),
        PQ("State two results of the 1953 crisis.",
           "Any two of: Britain agreed at constitutional talks in 1953; under the 1954 constitution Southern Cameroons became quasi-federal; "
           "it gained its own House of Assembly in Buea; Endeley became Leader of Government Business."),
        PQ("Why did many Southern Cameroonians feel neglected in the Eastern Region?",
           "Decisions were taken in Enugu, far away; there were few schools, roads and jobs for Southern Cameroons; the territory had little control of its own affairs."),
        SUM("From 1946 Southern Cameroons was a UN trust territory, but Britain governed it with Nigeria's Eastern Region (capital Enugu).",
            "Many felt neglected: few schools, roads and jobs.",
            "In 1953 a split in the NCNC led Endeley's group to declare benevolent neutrality and walk out.",
            "The 1954 constitution gave a quasi-federal status, a House of Assembly in Buea, and Endeley as Leader of Government Business.",
            "This was not independence; the question of the future remained open."),
    ],
))

# ------------------------------------------------------------------ British Southern Cameroons 2
LESSONS.append(lesson(
    module=MODULE,
    topic=BRITISH,
    title="Political parties and the road to the plebiscite",
    slug="southern-cameroons-parties-and-plebiscite-options",
    minutes=22,
    summary="The KNC, KNDP and One Kamerun, their leaders and aims, the KNDP victory of January 1959, the Mamfe Conference and the two options of the UN plebiscite.",
    objectives=[
        "Name the main parties of Southern Cameroons and their leaders",
        "Compare the aims of the KNC, the KNDP and One Kamerun",
        "Explain the outcome of the January 1959 election and the Mamfe Conference",
        "State the two options offered in the plebiscite",
    ],
    key_concepts=["KNC", "KNDP", "One Kamerun", "Endeley", "Foncha", "Plebiscite", "Mamfe Conference"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson Southern Cameroons won its own House of Assembly in Buea. "
          "The big question was then: what next? Join Nigeria, join the Republic of Cameroun, or something else?"),
        T("Political parties gave different answers. Their rivalry shaped the road to the plebiscite, the vote that decided the future "
          "of the territory."),
        D("A **plebiscite** is a direct vote by the people on one important question, such as which country to join.", title="Plebiscite"),
        H("The KNC and Endeley"),
        T("The **KNC** (Kamerun National Congress) was formed in 1953 and led by Dr Emmanuel Endeley. At first it talked of "
          "reunification, but it came to favour close links with Nigeria."),
        T("Later the KNC merged with P. M. Kale's KPP to form the CPNC."),
        H("The KNDP and Foncha"),
        T("The **KNDP** (Kamerun National Democratic Party) was founded in 1955 by John Ngu Foncha after he left the KNC. "
          "It wanted separation from Nigeria and, in time, reunification with French Cameroun."),
        T("Augustine Ngom Jua and Solomon Tandeng Muna were leading KNDP figures."),
        H("One Kamerun"),
        T("The **OK** (One Kamerun) was founded in 1957 by Ndeh Ntumazah. It was close to the banned UPC and demanded "
          "immediate reunification and independence."),
        IMG("f5h-southern-cameroons-parties.svg",
            alt="Timeline: KNC 1953, KNDP 1955, OK 1957, KNDP wins election January 1959, Mamfe Conference 1959, plebiscite 11 February 1961",
            caption="Figure 1. Parties and events on the road to the plebiscite."),
        KEY("Three parties compared", "Match each party with its leader and aim.", cards=[
            ["KNC (1953)", "Leader: Endeley. Came to favour close links with Nigeria."],
            ["KNDP (1955)", "Leader: Foncha, with Jua and Muna. Wanted separation from Nigeria and, in time, reunification."],
            ["OK (1957)", "Leader: Ntumazah. Close to the UPC; wanted immediate reunification and independence."],
        ]),
        H("The 1959 election and the Mamfe Conference"),
        T("The KNDP won the January 1959 elections and Foncha replaced Endeley as Premier. "
          "The new leaders and the old now had to agree on what question to put to voters."),
        T("Talks between Foncha and Endeley at the Mamfe Conference (1959) failed to agree on the plebiscite questions, so the UN decided them."),
        H("The options in the plebiscite"),
        T("The UN organised plebiscites in Southern and Northern Cameroons on 11 February 1961. Voters had only "
          "two choices: independence by joining Nigeria, or independence by joining the Republic of Cameroun. "
          "There was no option of separate independence."),
        T("Look at the parties again. The KNC leaned towards the first choice. The KNDP and OK leaned towards the second. "
          "The results, and what followed, are the subject of the next lesson."),
        EX("Model answer plan 1", intro="Compare the aims of the KNC and the KNDP between 1955 and 1961.", steps=[
            S("Leaders", text="KNC led by Endeley; KNDP led by Foncha, with Jua and Muna."),
            S("Attitude to Nigeria", text="The KNC came to favour association with Nigeria; the KNDP wanted separation from Nigeria."),
            S("Attitude to reunification", text="The KNDP supported reunification with French Cameroun; the KNC favoured close links with Nigeria instead."),
            S("Similarity", text="Both wanted self-government for Southern Cameroons and an end to rule from Enugu."),
            S("Outcome", text="The KNDP won the January 1959 election and Foncha replaced Endeley as Premier."),
        ]),
        EX("Model answer plan 2", intro="Describe the political developments in Southern Cameroons between 1953 and 1959.", steps=[
            S("1953", text="Endeley's group declared benevolent neutrality in Enugu; the KNC was formed."),
            S("1954", text="The new constitution created a House of Assembly in Buea; Endeley was Leader of Government Business."),
            S("1955", text="Foncha left the KNC and founded the KNDP."),
            S("1957", text="Ndeh Ntumazah founded One Kamerun, close to the banned UPC."),
            S("January 1959", text="The KNDP won the elections and Foncha replaced Endeley as Premier."),
            S("1959", text="The Mamfe Conference failed to agree on the plebiscite questions, so the UN decided them."),
        ]),
        H("Common mistakes"),
        MISTAKE("Confusing KNC and KNDP", "KNC = Endeley = closer to Nigeria. KNDP = Foncha = separation from Nigeria. The D in KNDP "
                "can remind you of the party that broke away (1955)."),
        MISTAKE("Saying Ahidjo led a Southern Cameroons party", "Ahidjo led French Cameroun. The Southern Cameroons leaders were Endeley, Foncha and Ntumazah."),
        MISTAKE("Saying the plebiscite offered independence alone", "There were only two options: join Nigeria or join the Republic of Cameroun."),
        QUIZ("Who founded the KNDP in 1955?",
             ["Emmanuel Endeley", "John Ngu Foncha", "Ndeh Ntumazah", "Ahmadou Ahidjo"], 1,
             "Foncha founded the KNDP after leaving Endeley's KNC.",
             hint="He replaced Endeley as Premier in 1959.",
             feedback=["Endeley led the KNC.", "", "Ntumazah founded One Kamerun (OK).", "Ahidjo led French Cameroun."]),
        QUIZ("What happened at the Mamfe Conference of 1959?",
             ["Foncha and Endeley agreed the plebiscite questions", "They failed to agree, so the UN decided the questions",
              "Southern Cameroons was declared independent", "The UPC was unbanned"], 1,
             "Talks between Foncha and Endeley failed to agree on the plebiscite questions, so the UN decided them.",
             hint="The word failed is in the lesson.",
             feedback=["They did not agree.", "", "Southern Cameroons did not become independent on its own.",
                       "The UPC was a French Cameroun party; Mamfe did not concern it."]),
        H("Practice questions"),
        PQ("Name the leaders of the KNC, the KNDP and One Kamerun.",
           "KNC: Emmanuel Endeley. KNDP: John Ngu Foncha. One Kamerun: Ndeh Ntumazah."),
        PQ("What did the KNDP want?",
           "Separation from Nigeria and, in time, reunification with French Cameroun."),
        PQ("What were the two options in the plebiscite?",
           "Achieving independence by joining the Federation of Nigeria, or by joining the independent Republic of Cameroun."),
        PQ("Why was the January 1959 election important?",
           "The KNDP won and Foncha replaced Endeley as Premier, so the party that wanted separation from Nigeria and reunification led the territory into the plebiscite."),
        SUM("The KNC (1953, Endeley) came to favour close links with Nigeria.",
            "The KNDP (1955, Foncha, with Jua and Muna) wanted separation from Nigeria and, in time, reunification.",
            "One Kamerun (1957, Ntumazah) was close to the UPC and wanted immediate reunification and independence.",
            "The KNDP won in January 1959; the Mamfe Conference failed to agree, so the UN set the plebiscite questions.",
            "The plebiscite of 11 February 1961 gave two options: join Nigeria or join the Republic of Cameroun."),
    ],
))

# ------------------------------------------------------------------ British Southern Cameroons 3
LESSONS.append(lesson(
    module=MODULE,
    topic=BRITISH,
    title="The plebiscite, the Foumban Conference and reunification",
    slug="southern-cameroons-plebiscite-foumban-reunification",
    minutes=24,
    summary="The outcomes of the plebiscite of 11 February 1961 in Northern and Southern Cameroons, the Foumban Conference of July 1961, reunification on 1 October 1961 and the differing views on these events.",
    objectives=[
        "State the outcome of the plebiscite in Northern and in Southern Cameroons",
        "Describe the Foumban Conference and its main result",
        "Explain what happened on 1 October 1961",
        "Present Anglophone and Francophone views of reunification fairly",
    ],
    key_concepts=["Plebiscite", "Foumban Conference", "Federation", "East Cameroon", "West Cameroon", "Reunification"],
    blocks=[
        H("Introduction"),
        T("In the previous lesson you saw the parties and the two options of the plebiscite. This lesson follows the vote, the talks at Foumban "
          "and the creation of the Federal Republic of Cameroon."),
        T("Historians and Cameroonians still discuss these events. This lesson shows the facts first and then the different views."),
        D("**Reunification** is the joining together, on 1 October 1961, of the former British Southern Cameroons and the "
          "former French Cameroun into the Federal Republic of Cameroon.", title="Reunification"),
        H("The plebiscite of 11 February 1961"),
        T("The UN organised separate plebiscites in Southern and Northern Cameroons on 11 February 1961. "
          "Voters could only choose between joining Nigeria or joining the Republic of Cameroun."),
        T("**Southern Cameroons** voted clearly to join the Republic of Cameroun."),
        T("**Northern Cameroons** voted to join Nigeria, and became part of Nigeria on 1 June 1961. "
          "Cameroun protested about the northern result, without success."),
        T("This lesson gives the results in general terms. For exact vote counts, check your textbook or your teacher's notes."),
        IMG("f5h-plebiscite-to-reunification.svg",
            alt="Timeline: plebiscites on 11 February 1961, Northern Cameroons joins Nigeria on 1 June, Foumban Conference in July, reunification on 1 October 1961",
            caption="Figure 1. From the plebiscite to reunification, 1961."),
        H("The Foumban Conference"),
        T("Delegations led by Ahidjo and Foncha met at the **Foumban Conference** in July 1961 to discuss a constitution. "
          "They agreed on a federation of two states, East Cameroon and West Cameroon."),
        D("A **federation** is a state made of two or more parts, each with its own government for some matters, "
          "under a central government for others.", title="Federation"),
        H("Reunification on 1 October 1961"),
        T("Reunification took place on 1 October 1961. Ahidjo became President of the Federal Republic and Foncha became "
          "Vice-President and Prime Minister of West Cameroon."),
        T("The federal constitution came into force on that day. The story of how the federation changed after 1961 belongs to the next module."),
        KEY("Differing views of 1961", "Present these views fairly in essays.", cards=[
            ["Reunification as success", "Many saw it as the fulfilment of the nationalist dream of one Kamerun, "
                                         "freely chosen by a clear majority in the plebiscite organised by the UN. "
                                         "West Cameroon kept its own Prime Minister."],
            ["Anglophone concerns", "Others argue that the lack of an independence option, the short Foumban talks and "
                                    "the unequal strength of the two sides left Anglophones with weak guarantees."],
        ], note="Historians and Cameroonians still debate these points; a good answer shows awareness of both."),
        EX("Model answer plan 1", intro="Describe the plebiscite of 11 February 1961 and its results.", steps=[
            S("Organisation", text="The UN organised separate plebiscites in Southern and Northern Cameroons on 11 February 1961."),
            S("The choice", text="Voters could only join Nigeria or join the Republic of Cameroun; there was no option of separate independence."),
            S("Southern result", text="Southern Cameroons voted clearly to join the Republic of Cameroun."),
            S("Northern result", text="Northern Cameroons voted to join Nigeria and became part of it on 1 June 1961."),
            S("Reactions", text="Cameroun protested about the northern result without success."),
            S("Conclusion", text="The different results led to different paths for the two parts of the trust territory."),
        ]),
        EX("Model answer plan 2", intro="Discuss the view that reunification in 1961 benefited both Southern Cameroons and the Republic of Cameroun.", steps=[
            S("Introduction", text="Say that views differ and that you will weigh both sides."),
            S("Arguments for", text="A clear majority in the south chose Cameroun; the nationalist dream of one Kamerun was fulfilled; West Cameroon kept its own Prime Minister (Foncha)."),
            S("Arguments against", text="No option of separate independence; the Foumban Conference was short; the two sides were unequal in strength, so Anglophone guarantees were weak."),
            S("Evidence from the facts", text="Foumban in July 1961 agreed a federation of East and West Cameroon; reunification on 1 October 1961."),
            S("Conclusion", text="Give a reasoned judgment that recognises both views. Do not claim that one side is simply right."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying both parts voted for Cameroun", "The south voted for Cameroun. The north voted for Nigeria and joined it on 1 June 1961."),
        MISTAKE("Mixing up the dates", "Plebiscite: 11 February 1961. Foumban: July 1961. Reunification: 1 October 1961."),
        MISTAKE("Taking sides", "Do not write only that reunification was perfect or only that it was a mistake. Present both views and explain why people hold them."),
        QUIZ("What was the result of the plebiscite in Northern Cameroons?",
             ["It voted to join Cameroun", "It voted to join Nigeria", "It voted for separate independence", "The vote was cancelled"], 1,
             "Northern Cameroons voted to join Nigeria and became part of Nigeria on 1 June 1961.",
             hint="The north and south did not vote alike.",
             feedback=["That was the southern result.", "", "Separate independence was not an option.",
                       "Cameroun protested about the result, but the vote was not cancelled."]),
        QUIZ("Which statement about the Foumban Conference is correct?",
             ["It created a unitary state", "It was held in July 1961 and agreed a federation of East and West Cameroon",
              "It organised the plebiscite", "It took place before the plebiscite"], 1,
             "Delegations led by Ahidjo and Foncha met in July 1961 and agreed a federation of two states.",
             hint="Place it between the plebiscite and reunification.",
             feedback=["The unitary state came later, in the next module's period.", "",
                       "The UN organised the plebiscite.", "The plebiscite was in February; Foumban was in July."]),
        H("Practice questions"),
        PQ("State the date of the plebiscite and the date of reunification.",
           "The plebiscite: 11 February 1961. Reunification: 1 October 1961."),
        PQ("State two results of the Foumban Conference of July 1961.",
           "Any two of: agreement on a federation of two states, East Cameroon and West Cameroon; preparation of the federal constitution; "
           "Ahidjo as President and Foncha as Vice-President (on 1 October)."),
        PQ("Why did Northern and Southern Cameroons vote differently in 1961? Give two reasons.",
           "The north had long been administered with Northern Nigeria and had close religious and ethnic ties there; "
           "in the south, the KNDP campaign for reunification and dissatisfaction with Eastern Nigeria favoured Cameroun."),
        PQ("Give one Anglophone concern and one other view about reunification.",
           "Anglophone concern: no independence option, short Foumban talks and unequal strength left weak guarantees. "
           "Other view: reunification fulfilled the nationalist dream and was chosen by a clear majority in a UN plebiscite."),
        SUM("The UN plebiscites of 11 February 1961 offered two options: join Nigeria or join the Republic of Cameroun.",
            "Southern Cameroons voted for Cameroun; Northern Cameroons voted for Nigeria and joined it on 1 June 1961.",
            "The Foumban Conference (July 1961) agreed a federation of East and West Cameroon.",
            "Reunification took place on 1 October 1961: Ahidjo became President, Foncha Vice-President and West Cameroon Prime Minister.",
            "Anglophone and other views differ; present both fairly."),
    ],
))
