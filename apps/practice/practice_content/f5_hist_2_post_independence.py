"""Practice sets for Form 5 History: Post-Independence Cameroon (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

MODULE = "Post-Independence Cameroon"
FED = "Federal to unitary state"
MOD = "Modern transitions"

SETS = []

# ------------------------------------------------------------------ 1. The Federal Republic
SETS.append(practice_set(
    module=MODULE, topic=FED,
    title="The Federal Republic, 1961–1972: structure and leaders",
    lesson="federal-republic-of-cameroon-1961-1972",
    questions=[
        MC("On what date did the federal constitution come into force?", [
            C("20 May 1972", why="This is the date of the referendum that ended the federation."),
            C("1 September 1966", why="This is the date on which the CNU was formed."),
            C("1 October 1961", correct=True),
            C("11 February 1961", why="This is the date of the UN plebiscite, before reunification."),
        ], steps=[S("Recall", text="The federal constitution came into force on 1 October 1961, the date of reunification.")],
           concept="Start of the federation", skill="Recall",
           hint="It is the date of reunification."),
        NUM("Counting from the year 1961 to the year 1972, how many years did the federal period last?", 11,
            steps=[S("Subtract the years", math=r"1972 - 1961 = 11")],
            concept="Length of the federal period", skill="Calculation",
            hint="Subtract the year the federation began from the year it ended."),
        MC("What was the capital of West Cameroon?", [
            C("Bamenda", why="Bamenda was an important town but not the state capital."),
            C("Douala", why="Douala was not a state capital."),
            C("Yaoundé", why="Yaoundé was the capital of East Cameroon and the federal capital."),
            C("Buea", correct=True),
        ], steps=[S("Recall", text="West Cameroon had its capital at Buea.")],
           concept="Structure of the Federal Republic", skill="Recall",
           hint="Think of the town at the foot of Mount Cameroon."),
        MC("Who was the federal Vice-President in 1961?", [
            C("Solomon Tandeng Muna", why="Muna became Prime Minister of West Cameroon in 1968."),
            C("John Ngu Foncha", correct=True),
            C("Augustine Ngom Jua", why="Jua was Prime Minister of West Cameroon from 1965 to 1968."),
            C("Ahmadou Ahidjo", why="Ahidjo was the federal President."),
        ], steps=[S("Recall", text="Ahidjo was federal President and Foncha federal Vice-President. Foncha was also the first Prime Minister of West Cameroon.")],
           concept="Leaders of the federation", skill="Recall",
           hint="He was also West Cameroon's first Prime Minister."),
        MC("Who was Prime Minister of West Cameroon from 1965 to 1968?", [
            C("Augustine Ngom Jua", correct=True),
            C("John Ngu Foncha", why="Foncha held the post from 1961 to 1965."),
            C("Solomon Tandeng Muna", why="Muna held the post from 1968 to 1972."),
            C("Ahmadou Ahidjo", why="Ahidjo was federal President, not a Prime Minister of West Cameroon."),
        ], steps=[S("Order of Prime Ministers", text="Foncha (1961–1965), Jua (1965–1968), Muna (1968–1972).")],
           concept="Prime Ministers of West Cameroon", skill="Recall",
           hint="He came between the first and the last Prime Minister."),
        MC("What was the position of Yaoundé in the Federal Republic?", [
            C("Capital of East Cameroon only", why="Yaoundé was also the federal capital."),
            C("Capital of West Cameroon", why="West Cameroon's capital was Buea."),
            C("Capital of East Cameroon and federal capital", correct=True),
            C("A town with no special role", why="It was both a state capital and the federal capital."),
        ], steps=[S("Recall", text="Yaoundé was the capital of East Cameroon and also the federal capital.")],
           concept="Structure of the Federal Republic", skill="Recall",
           hint="One town had two roles."),
        MC("Who were the Federal Inspectors of Administration?", [
            C("Officials elected by the people of each state", why="They were appointed by the President, not elected."),
            C("Officials appointed by the President to supervise administration in each state", correct=True),
            C("Judges of the West Cameroon courts", why="Judging cases was the work of the courts."),
            C("Soldiers in charge of defence", why="Defence was a federal matter, but the inspectors supervised administration."),
        ], steps=[S("Role", text="They were appointed by the President and supervised administration in each state, which is one sign of centralization.")],
           concept="Federal inspectors", skill="Concept",
           hint="Think about who appointed them."),
        MC("Which approach gives the best answer to an essay on the federal period?", [
            C("Say the federation was perfect", why="This ignores the criticisms and the centralization."),
            C("Say the federation completely failed", why="This ignores the supporters' arguments about unity."),
            C("Give only Ahidjo's view", why="One view is not enough on a debated topic."),
            C("Give the views of supporters and critics, each with evidence", correct=True),
        ], steps=[S("Balance", text="Supporters say a strong centre helped unity; critics say the states lost power and the guarantees of 1961. Give both and support each with evidence.")],
           concept="Balanced views", skill="Reasoning",
           hint="History questions on debated topics ask for more than one view."),
    ]))

# ------------------------------------------------------------------ 2. CNU and 1972
SETS.append(practice_set(
    module=MODULE, topic=FED,
    title="The CNU and the 1972 referendum: causes, results and views",
    lesson="cnu-single-party-and-the-1972-referendum",
    questions=[
        MC("What is a referendum?", [
            C("A meeting of party leaders", why="A referendum is a vote of voters, not a meeting of leaders."),
            C("A court judgement", why="A referendum is not decided by courts."),
            C("A vote in which voters accept or reject a proposal", correct=True),
            C("A change of Prime Minister", why="That is an appointment, not a vote on a proposal."),
        ], steps=[S("Definition", text="A referendum is a vote in which all voters accept or reject a proposal, such as a new constitution.")],
           concept="Referendum", skill="Recall",
           hint="Think of voters answering yes or no."),
        MC("When was the Cameroon National Union (CNU) formed?", [
            C("1 September 1966", correct=True),
            C("1 October 1961", why="This is the date of the federal constitution."),
            C("20 May 1972", why="This is the date of the referendum."),
            C("1985", why="In 1985 the CNU became the CPDM."),
        ], steps=[S("Recall", text="The CNU was formed on 1 September 1966.")],
           concept="Formation of the CNU", skill="Recall",
           hint="It came between 1961 and 1972."),
        MC("Which parties merged to form the CNU?", [
            C("UPC, SDF and CPDM", why="The UPC stayed outside, the SDF came in 1990 and the CPDM in 1985."),
            C("Only Ahidjo's Union Camerounaise", why="The West Cameroon parties also merged into it."),
            C("KNDP and the SDF", why="The SDF did not exist in 1966."),
            C("UC, KNDP, CPNC and CUC", correct=True),
        ], steps=[S("Recall", text="Ahidjo's Union Camerounaise joined the KNDP, CPNC and CUC from West Cameroon.")],
           concept="Formation of the CNU", skill="Recall",
           hint="One East Cameroon party and three West Cameroon parties."),
        MC("Which was an argument made by supporters of the single party?", [
            C("It increased party competition", why="A single party ended open competition."),
            C("It reduced ethnic and regional division", correct=True),
            C("It restored the federation", why="The federation ended in 1972."),
            C("It allowed the UPC to win elections", why="Remaining UPC activists who refused to join faced repression."),
        ], steps=[S("Two views", text="Supporters said one party reduced ethnic and regional division. Critics said it ended open political competition.")],
           concept="Views on the CNU", skill="Concept",
           hint="Think of the word 'unity'."),
        MC("On what date was the referendum that replaced the federation held?", [
            C("11 February 1961", why="This is the date of the UN plebiscite."),
            C("20 May 1972", correct=True),
            C("18 January 1996", why="This is the date of the 1996 constitution."),
            C("26 May 1990", why="This is the date of the launch of the SDF."),
        ], steps=[S("Recall", text="The referendum was held on 20 May 1972. The date is now National Day.")],
           concept="The 1972 referendum", skill="Recall",
           hint="It is the date of National Day."),
        MC("What name did the country take after the referendum of 1972?", [
            C("Federal Republic of Cameroon", why="This was the name from 1961 to 1972."),
            C("Republic of Cameroon", why="This name came in 1984."),
            C("United Republic of Cameroon", correct=True),
            C("Republic of Cameroun", why="This was the name of the Francophone state before reunification."),
        ], steps=[S("Recall", text="A new constitution in June 1972 created the United Republic of Cameroon.")],
           concept="Effects of the 1972 referendum", skill="Recall",
           hint="The new name stressed unity."),
        MC("Which was one of the official reasons for the change to a unitary state?", [
            C("The UN ordered it", why="The change came through a national referendum, not a UN order."),
            C("The high cost of running three governments", correct=True),
            C("A vote of the West Cameroon assembly to leave the country", why="No such vote is part of the account."),
            C("The end of the Cold War", why="The Cold War ended much later, around 1989–1991."),
        ], steps=[S("Official reasons", text="High cost of three governments, national unity, faster economic development, and a single party that had already united political life.")],
           concept="Causes of the 1972 change", skill="Reasoning",
           hint="Count the governments in a federation of two states."),
        MC("How do many Anglophone critics view the 1972 change?", [
            C("As the free completion of national unity", why="That is the government's view."),
            C("As an event caused by Nigeria", why="Nigeria had no role in this debate."),
            C("As a change ordered by the UN", why="Neither side in the debate blames the UN."),
            C("As a loss of the guarantees agreed at Foumban, made in a way the federal constitution did not allow", correct=True),
        ], steps=[S("Government view", text="The referendum completed national unity and was freely approved by the people."),
                  S("Critical view", text="Many Anglophone critics argue that the federal constitution did not allow changes that harmed the federation, and that West Cameroon lost the guarantees agreed at Foumban.")],
           concept="Views on the end of federalism", skill="Interpretation",
           hint="Think about what West Cameroon had been promised in 1961."),
    ]))

# ------------------------------------------------------------------ 3. 1982 transition
SETS.append(practice_set(
    module=MODULE, topic=MOD,
    title="From Ahidjo to Biya: the transition of 1982 and the 1980s",
    lesson="ahidjo-to-biya-transition-1982-and-the-1980s",
    questions=[
        MC("On what date did Ahidjo announce his resignation?", [
            C("6 April 1984", why="This is the date of the failed coup attempt."),
            C("4 November 1982", correct=True),
            C("26 May 1990", why="This is the date of the launch of the SDF."),
            C("20 May 1972", why="This is the date of the referendum."),
        ], steps=[S("Recall", text="Ahidjo announced his resignation on 4 November 1982.")],
           concept="The 1982 transition", skill="Recall",
           hint="It was in 1982, in the month of Biya's swearing-in."),
        MC("How did Paul Biya become President in 1982?", [
            C("He won a multiparty election", why="Multiparty presidential elections were first held in 1992."),
            C("He led a coup", why="Ahidjo resigned; the failed coup was in 1984."),
            C("As Prime Minister, he was the constitutional successor of Ahidjo", correct=True),
            C("He was chosen at the Tripartite Conference", why="The Tripartite Conference took place in 1991."),
        ], steps=[S("Succession", text="As Prime Minister, Biya was the constitutional successor and was sworn in on 6 November 1982.")],
           concept="Constitutional succession", skill="Concept",
           hint="What post did Biya hold just before November 1982?"),
        MC("What post did Ahidjo keep after resigning as President?", [
            C("Prime Minister", why="Biya was Prime Minister before becoming President."),
            C("Chairman of the CNU", correct=True),
            C("President of the Senate", why="There was no Senate until the 1996 constitution."),
            C("Leader of the SDF", why="The SDF was launched only in 1990."),
        ], steps=[S("Recall", text="Ahidjo remained chairman of the CNU.")],
           concept="The 1982 transition", skill="Recall",
           hint="Think of the single party."),
        MC("What happened in Yaoundé on 6 April 1984?", [
            C("Biya was sworn in as President", why="Biya was sworn in on 6 November 1982."),
            C("The SDF was launched", why="The SDF was launched in Bamenda on 26 May 1990."),
            C("The CNU became the CPDM", why="This happened in 1985 at a congress in Bamenda."),
            C("An attempted coup failed", correct=True),
        ], steps=[S("Recall", text="On 6 April 1984 an attempted coup failed in Yaoundé. Ahidjo, accused of links to it, lived in exile until his death in 1989.")],
           concept="The coup attempt of 1984", skill="Recall",
           hint="It came after Biya had been President for more than a year."),
        MC("What did a law of February 1984 change?", [
            C("The country's name to Republic of Cameroon", correct=True),
            C("The country to a federation", why="Federalism ended in 1972."),
            C("The name of the CNU to CPDM", why="This came in 1985."),
            C("The capital from Yaoundé to Buea", why="The capital did not change."),
        ], steps=[S("Recall", text="In February 1984 a law changed the name from the United Republic of Cameroon to the Republic of Cameroon.")],
           concept="The 1984 name change", skill="Recall",
           hint="The name before 1984 was United Republic of Cameroon."),
        MC("Why did many Anglophones object to the 1984 name?", [
            C("It restored the federal system", why="The name change did not restore federalism."),
            C("It was the name of the Francophone state before reunification", correct=True),
            C("It removed the CPDM", why="The CPDM was created in 1985."),
            C("It was decided by a referendum they lost", why="The name was changed by a law, not a referendum."),
        ], steps=[S("Two views", text="The government presented the change as a sign of national unity. Many Anglophones objected because Republic of Cameroun had been the name of the Francophone state before reunification.")],
           concept="The 1984 name change", skill="Interpretation",
           hint="Think about what the Francophone state was called before 1961."),
        MC("Where was the CNU renamed the CPDM, and in which year?", [
            C("Yaoundé, 1982", why="The 1982 date belongs to the transfer of power."),
            C("Buea, 1961", why="1961 was the year of reunification."),
            C("Bamenda, 1985", correct=True),
            C("Bamenda, 1990", why="1990 is the year of the SDF launch and the liberty laws."),
        ], steps=[S("Recall", text="In 1985, at a congress in Bamenda, the CNU became the CPDM.")],
           concept="CNU becomes the CPDM", skill="Recall",
           hint="The SDF was launched in the same town five years later."),
        MC("Which order of events is correct?", [
            C("Coup attempt, Ahidjo resigns, CPDM formed", why="Ahidjo resigned in 1982, before the coup attempt in 1984."),
            C("CPDM formed, name change, Ahidjo resigns", why="The CPDM came last, in 1985."),
            C("Name change, Ahidjo resigns, coup attempt", why="Ahidjo resigned in 1982, before the 1984 name change."),
            C("Ahidjo resigns, name change, coup attempt, CPDM formed", correct=True),
        ], steps=[S("Order", text="4 November 1982: resignation. February 1984: new name. 6 April 1984: failed coup. 1985: CNU becomes the CPDM.")],
           concept="Chronology of the 1980s", skill="Reasoning",
           hint="Place the dates 1982, 1984 and 1985 in order."),
    ]))

# ------------------------------------------------------------------ 4. Liberalization
SETS.append(practice_set(
    module=MODULE, topic=MOD,
    title="Liberalization 1990–1992: SDF, ghost towns and the Tripartite Conference",
    lesson="political-liberalization-sdf-ghost-towns-tripartite",
    questions=[
        MC("What does multipartism mean?", [
            C("A system where only one party is legal", why="That is a single-party system."),
            C("A system without elections", why="Multipartism involves competing in elections."),
            C("A system where several parties may legally exist and compete in elections", correct=True),
            C("A system with two states", why="That describes a federation of two states."),
        ], steps=[S("Definition", text="Multipartism is a system in which several parties may legally exist and compete in elections.")],
           concept="Multipartism", skill="Recall",
           hint="'Multi' means many."),
        MC("Which was an external cause of the return to multiparty politics?", [
            C("The 1972 referendum", why="This was an internal event, almost twenty years earlier."),
            C("The creation of the CNU", why="The CNU was formed in 1966."),
            C("The coup attempt of 1984", why="This was an internal event in 1984."),
            C("The end of the Cold War", correct=True),
        ], steps=[S("External causes", text="The end of the Cold War, the fall of the Berlin Wall (1989) and the collapse of one-party regimes in Eastern Europe, plus donor pressure.")],
           concept="Causes of liberalization", skill="Reasoning",
           hint="Think of events outside Cameroon around 1989."),
        MC("Who launched the SDF, and where?", [
            C("John Fru Ndi, in Yaoundé", why="The launch took place in Bamenda."),
            C("John Ngu Foncha, in Buea", why="Foncha is linked to the KNDP and the federation."),
            C("John Fru Ndi, in Bamenda", correct=True),
            C("Paul Biya, in Bamenda", why="Biya was President and CPDM leader, not the founder of the SDF."),
        ], steps=[S("Recall", text="On 26 May 1990 the SDF was launched in Bamenda by John Fru Ndi. Several people were killed when security forces dispersed the launch.")],
           concept="Launch of the SDF", skill="Recall",
           hint="The same town hosted the 1985 congress that created the CPDM."),
        MC("What did the liberty laws of December 1990 do?", [
            C("They ended the ghost towns", why="The ghost towns campaign came in 1991."),
            C("They created the CNU", why="The CNU dates from 1966."),
            C("They created the Senate", why="The Senate was created by the 1996 constitution."),
            C("They allowed political parties and associations and eased controls on the press", correct=True),
        ], steps=[S("Recall", text="The liberty laws allowed political parties and associations and eased controls on the press and public meetings.")],
           concept="The liberty laws", skill="Recall",
           hint="They restored what the single party had ended."),
        MC("Why did the opposition organise the ghost towns campaign?", [
            C("Because the government refused a sovereign national conference", correct=True),
            C("Because Biya resigned", why="Biya did not resign."),
            C("To celebrate the liberty laws", why="Ghost towns were a protest, not a celebration."),
            C("To oppose the 1972 referendum", why="That referendum was almost twenty years earlier."),
        ], steps=[S("Cause", text="Opposition parties demanded a sovereign national conference; the government refused."),
                  S("Method", text="Shops, markets and transport stayed closed on working days.")],
           concept="Ghost towns", skill="Reasoning",
           hint="Think of what the opposition asked for and was refused."),
        MC("What was the ghost towns method?", [
            C("Citizens left their towns for the villages permanently", why="The campaign closed economic activity in towns on working days."),
            C("Shops, markets and transport stayed closed on working days", correct=True),
            C("Soldiers took control of markets", why="The government responded with military command in several provinces; the campaign itself was the opposition's."),
            C("Candidates withdrew from elections", why="That is a boycott, not ghost towns."),
        ], steps=[S("Definition", text="Ghost towns (villes mortes) were an opposition strategy of closing shops, markets and transport on working days to pressure the government.")],
           concept="Ghost towns", skill="Concept",
           hint="Think of an empty town on a market day."),
        MC("Who took part in the Tripartite Conference of October–November 1991?", [
            C("The government, opposition parties and civil society", correct=True),
            C("Ahidjo, Biya and Foncha", why="The conference was a national meeting of groups, not three people."),
            C("Cameroon, Nigeria and the UN", why="It was a national, not an international, meeting."),
            C("Only CPDM members", why="It included the opposition and civil society."),
        ], steps=[S("Recall", text="It brought together the government, opposition parties and members of civil society, and set up a committee to draft constitutional reforms. Some opposition leaders refused to sign.")],
           concept="Tripartite Conference", skill="Recall",
           hint="The name tells you how many groups took part."),
        MC("Which statement about the 1992 elections is correct?", [
            C("The SDF won and Biya left office", why="Biya won the presidential election, and the SDF contested the result."),
            C("They were held under the single-party system", why="They were multiparty elections."),
            C("Biya won the presidential election of October 1992 and the opposition, especially the SDF, contested the result", correct=True),
            C("They were held in 1982", why="1982 was the year Biya succeeded Ahidjo."),
        ], steps=[S("Recall", text="Multiparty legislative and presidential elections followed in 1992. Biya won in October 1992; the opposition, especially the SDF, contested the result.")],
           concept="The 1992 elections", skill="Recall",
           hint="Look for the answer that mentions both the winner and the dispute."),
    ]))

# ------------------------------------------------------------------ 5. 1996 constitution
SETS.append(practice_set(
    module=MODULE, topic=MOD,
    title="The 1996 constitution and decentralization",
    lesson="constitution-of-1996-and-decentralization",
    questions=[
        MC("On what date was the constitution amending the 1972 text adopted?", [
            C("1 October 1961", why="This is the date of the federal constitution."),
            C("20 May 1972", why="This is the date of the referendum."),
            C("26 May 1990", why="This is the date of the SDF launch."),
            C("18 January 1996", correct=True),
        ], steps=[S("Recall", text="The constitution of 18 January 1996 amended the 1972 constitution.")],
           concept="The 1996 constitution", skill="Recall",
           hint="It came after the 1992 elections."),
        MC("Where did Anglophone groups meet in 1993 to state their grievances?", [
            C("Buea", correct=True),
            C("Yaoundé", why="The Tripartite Conference of 1991 was held in Yaoundé."),
            C("Foumban", why="Foumban is linked to the 1961 talks, not to 1993."),
            C("Douala", why="Douala was affected by the ghost towns, but the conference was not held there."),
        ], steps=[S("Recall", text="The All Anglophone Conference was held in Buea in 1993. For what it declared, check your textbook.")],
           concept="All Anglophone Conference", skill="Recall",
           hint="This town was the capital of West Cameroon."),
        MC("What was the length of the presidential term in the 1996 constitution?", [
            C("Five years, with no limit", why="The term was seven years, renewable once."),
            C("Four years, not renewable", why="The term was seven years."),
            C("Seven years, renewable once", correct=True),
            C("Seven years, with no limit", why="The limit was removed only by the 2008 amendment."),
        ], steps=[S("Recall", text="The 1996 constitution set a seven-year term, renewable once. A 2008 amendment removed the limit.")],
           concept="Provisions of the 1996 constitution", skill="Recall",
           hint="The limit was removed later, in 2008."),
        MC("Which institutions were provided for by the 1996 constitution?", [
            C("A Senate and a Constitutional Council", correct=True),
            C("The CNU and the KNDP", why="These are parties of the 1960s."),
            C("The Tripartite Conference", why="That was a meeting in 1991, not an institution created in 1996."),
            C("The Federal Inspectors", why="Federal inspectors belonged to the federal period of 1961–1972."),
        ], steps=[S("Recall", text="The 1996 constitution created a Senate, a Constitutional Council and regions with elected councils.")],
           concept="Provisions of the 1996 constitution", skill="Recall",
           hint="One of them is a second chamber of the legislature."),
        MC("What is decentralization?", [
            C("Giving all power to the President", why="That is closer to centralization."),
            C("Dividing the country into two independent states", why="Decentralization keeps one state."),
            C("Moving some powers to regional or local bodies while keeping one central government", correct=True),
            C("Banning elections", why="Decentralization does not mean banning elections."),
        ], steps=[S("Definition", text="Decentralization gives some powers and resources to regional or local bodies while the country keeps one central government.")],
           concept="Decentralization", skill="Concept",
           hint="Think of the word 'centre' and moving something away from it."),
        MC("What did a 2008 amendment change?", [
            C("It created the Senate", why="The Senate comes from the 1996 constitution."),
            C("It ended the federation", why="The federation ended in 1972."),
            C("It removed the limit on presidential terms", correct=True),
            C("It created the SDF", why="The SDF was launched in 1990."),
        ], steps=[S("Recall", text="A 2008 amendment removed the limit on presidential terms.")],
           concept="The 2008 amendment", skill="Recall",
           hint="It concerns the seven-year term."),
        MC("Which statement about the 1996 constitution is correct?", [
            C("It returned Cameroon to a federation", why="It confirmed a decentralized unitary state."),
            C("It confirmed Cameroon as a decentralized unitary state", correct=True),
            C("It made the CNU the only legal party", why="Multipartism returned in 1990."),
            C("It ended elections", why="It provided for regions with elected councils."),
        ], steps=[S("Recall", text="It confirmed the Republic of Cameroon as a decentralized unitary state.")],
           concept="The decentralized unitary state", skill="Concept",
           hint="Federalism ended in 1972."),
        MC("Which answer presents the 1996 reforms fairly?", [
            C("Supporters see a peaceful, gradual reform; critics say reforms were limited and slow", correct=True),
            C("Everyone agrees the reforms were perfect", why="Many people disagree; critics call them limited and slow."),
            C("Everyone agrees the reforms were a failure", why="Supporters see a peaceful, gradual reform."),
            C("Only the government's view needs to be given", why="A fair answer gives both views."),
        ], steps=[S("Balance", text="Present the view of supporters (peaceful, gradual reform) and critics (limited, slow) with evidence for each. For details beyond the lesson, check your textbook.")],
           concept="Balanced views", skill="Reasoning",
           hint="Look for the answer that has two sides."),
    ]))
