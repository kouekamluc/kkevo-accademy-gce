"""Upper Sixth History (A Level 0760): practice sets for the deeper lessons (KKEVO draft for reviewer checking).

One set per lesson in al_hist7_all.py, plus the practice paper mock (40 multiple-choice questions).
Source extracts are invented illustrative texts, never real quotations or past-paper items.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "upper-sixth")

M_CMR = "Cameroon 1945 to Today"
M_DEC = "Decolonization in Africa"
M_CW = "Cold War & International Governance"
M_EX = "Examination"

_n = [0]


def Q(prompt, right, wrongs, step, concept, skill, hint, feedback=""):
    """Four-option question. `wrongs` is three (text, why) pairs. The correct option rotates through A-D."""
    pos = _n[0] % 4
    _n[0] += 1
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(right, correct=True))
    return MC(prompt, choices, [S("Answer", text=step)], concept=concept, skill=skill, hint=hint, feedback=feedback)


def N(prompt, answer, step, concept, skill, hint, unit=""):
    return NUM(prompt, answer, [S("Answer", text=step)], unit=unit, concept=concept, skill=skill, hint=hint)


SETS = []

# ---------------------------------------------------------------- 1. Trusteeship machinery
SETS.append(practice_set(
    module=M_CMR, topic="Trusteeship and decolonization",
    title="Trusteeship agreements, missions and petitions", lesson="h7-cmr-trusteeship-machinery",
    questions=[
        Q("Which UN organ supervised trust territories such as the two Cameroons?",
          "The Trusteeship Council", [
              ("The International Court of Justice", "The Court settles legal disputes between states; it did not supervise the territories."),
              ("The Economic and Social Council", "ECOSOC deals with economic and social work, not trusteeship."),
              ("The Secretariat", "The Secretariat runs the administration of the UN but does not supervise trusteeship."),
          ], "The Trusteeship Council examined reports, received petitions and sent visiting missions.",
          "Trusteeship Council", "Recall", "Think of the UN organ named after the system itself."),
        Q("What was a petition under the trusteeship system?",
          "A written complaint or request sent by inhabitants to the UN", [
              ("An order from the UN to the administering power", "Petitions came from the inhabitants, and the UN could only recommend."),
              ("A tax paid by the inhabitants to the UN", "Petitions were not taxes."),
              ("A treaty between France and Britain", "A treaty is an agreement between states, not a petition."),
          ], "Article 87 allowed the Assembly and Council to accept petitions from inhabitants.",
          "Petitions", "Recall", "Who wrote petitions, and to whom?"),
        Q("Which aim did Article 76 of the Charter set for trusteeship?",
          "Progress towards self-government or independence as appropriate", [
              ("Permanent union with the administering state", "Article 76 pointed to self-government or independence, not permanent integration."),
              ("Immediate independence for every territory on 1 January 1946", "No such fixed date was set by the Charter."),
              ("Control of the territories by UN troops", "The UN did not govern the territories; an administering authority did."),
          ], "Article 76 named progress towards self-government or independence as appropriate to each territory.",
          "Article 76", "Recall", "The aim looks forward to a change in political status."),
        Q("Who administered French Cameroun under the trusteeship agreement?",
          "France", [
              ("The United Nations directly", "The UN supervised; it did not administer."),
              ("Britain", "Britain administered the western strip, the British Cameroons."),
              ("The League of Nations", "The League had ended and its mandates were replaced by trusteeship."),
          ], "France was the administering authority for the larger eastern part.",
          "Administering authority", "Recall", "The UN supervised, but a state ran the territory."),
        Q("Which statement gives the UPC reading of France's duties under the agreement?",
          "The Charter promised a path to independence, so France should set a timetable", [
              ("Cameroun was a permanent part of the French Union", "That is closer to the French reading of association."),
              ("The UN should govern Cameroun directly", "The UPC did not ask for UN governance; it asked for independence."),
              ("Trusteeship gave France the right to ban all petitions", "Petitions were a right of inhabitants under the Charter."),
          ], "The UPC stressed Article 76 and asked for a timetable and for reunification.",
          "French and UPC readings", "Concept", "Which side quoted the Charter's promise of independence?"),
        Q("Which of these was a limit on the UN's power over an administering authority?",
          "The Council could recommend but could not compel", [
              ("The Council could dismiss the administering authority at any vote", "It had no such power."),
              ("The Council governed through its own officials", "Governing was done by the administering authority."),
              ("The General Assembly could cancel France's membership of the UN", "Trusteeship supervision did not include such a power."),
          ], "Recommendation without enforcement was the key limit; administering states also sat on the Council.",
          "Limits of trusteeship", "Reasoning", "What could the Council do with its findings?"),
        N("In which year did the UN approve the trusteeship agreements for the two Cameroons?", 1946,
          "The General Assembly approved them in December 1946.", "Trusteeship agreements", "Recall",
          "It was the year after the UN was founded."),
        Q("An invented petition from market women complains about tax and the lack of a representative in the assembly. What can a historian NOT learn from it alone?",
          "How many people shared the grievance", [
              ("That the petitioners knew of the UN", "The act of petitioning shows this."),
              ("That tax was one grievance", "The text states this."),
              ("That representation was a concern", "The text states this."),
          ], "One petition cannot show how widespread the grievance was. Further sources are needed.",
          "Source evaluation", "Interpretation", "Think about what one document can and cannot represent."),
    ]))

# ---------------------------------------------------------------- 2. UPC to Ahidjo
SETS.append(practice_set(
    module=M_CMR, topic="Trusteeship and decolonization",
    title="The UPC, the conflict and Ahidjo's rise", lesson="h7-cmr-upc-conflict-ahidjo-1960",
    questions=[
        Q("In which town was the UPC founded in April 1948?",
          "Douala", [
              ("Buea", "Buea became the seat of the Southern Cameroons House of Assembly."),
              ("Foumban", "Foumban hosted the 1961 conference."),
              ("Garoua", "Garoua is in the north, Ahidjo's home region."),
          ], "The UPC was founded in Douala.", "UPC", "Recall", "It is the main port city."),
        Q("What happened to the UPC in July 1955?",
          "It was banned by the French administration", [
              ("It won a majority in the territorial assembly", "It could not take part in the December 1956 elections."),
              ("It was merged with the Union Camerounaise", "The Union Camerounaise was formed by Ahidjo in 1958."),
              ("It was dissolved by the Trusteeship Council", "The ban was a French administrative act."),
          ], "A decree banned the UPC in July 1955 after the clashes of May 1955.",
          "Ban of 1955", "Recall", "Think of the administering authority."),
        Q("Who replaced Andre-Marie Mbida as head of government in February 1958?",
          "Ahmadou Ahidjo", [
              ("Ruben Um Nyobe", "Um Nyobe led the banned UPC."),
              ("Ernest Ouandie", "Ouandie was a UPC leader."),
              ("John Ngu Foncha", "Foncha was Premier of Southern Cameroons."),
          ], "Ahidjo became Prime Minister in February 1958.", "Ahidjo's rise", "Recall", "He was Mbida's deputy."),
        Q("What does the word 'pacification' show about the French campaign against the maquis?",
          "It was the official French term, which critics say hides the violence", [
              ("It proves that no violence took place", "The word does not prove this; critics argue the opposite."),
              ("It was the UPC's own name for its movement", "It was an official French term."),
              ("It describes the 1960 UN vote", "The UN vote of 1959 is a different matter."),
          ], "Terms in sources carry a viewpoint. Describe the word and who used it.",
          "Pacification", "Interpretation", "Whose word was it?"),
        Q("Which reading of 1960 stresses that independence came by negotiation with France and the UN?",
          "A negotiated-transfer reading", [
              ("A nationalist reading", "That reading stresses the UPC as the authentic movement and the effect of repression."),
              ("A social-history reading", "That reading stresses local grievances and regional differences."),
              ("A reading based only on numbers of deaths", "No such school exists, and casualty figures are uncertain."),
          ], "The negotiated-transfer reading uses the Loi-Cadre, the 1957 statute and the 1959 UN vote.",
          "Interpretations of 1960", "Concept", "Which reading talks about negotiation?"),
        N("How many years passed between the founding of the UPC in 1948 and independence on 1 January 1960?", 12,
          "1960 minus 1948 is 12 years.", "Chronology", "Calculation", "Subtract the founding year from the independence year."),
        Q("Why is a French officer's report that 'the people welcome the troops' of limited use on its own?",
          "It was written by one side to a superior and may exaggerate success", [
              ("Because officers never write reports", "Officers did write reports; the issue is their purpose."),
              ("Because it is too long", "Length is not the problem."),
              ("Because it is a UN document", "It is a French military report."),
          ], "Provenance and purpose limit its value. Cross-check with other accounts.",
          "Source evaluation", "Interpretation", "Ask who wrote it, to whom and why."),
        Q("Which statement about the conflict's casualties is the safest to write in an essay?",
          "Estimates differ widely and the exact number is not known", [
              ("Exactly 100,000 died", "No single figure is certain, so stating one as fact is unsafe."),
              ("No one died after independence", "Fighting continued after 1960; Ouandie was executed in 1971."),
              ("Only soldiers were killed", "Civilians were affected in the conflict."),
          ], "Figures are disputed, so say so and describe the types of evidence.",
          "Casualty evidence", "Reasoning", "A cautious sentence avoids claiming precise numbers."),
    ]))

# ---------------------------------------------------------------- 3. Southern Cameroons parties
SETS.append(practice_set(
    module=M_CMR, topic="Southern Cameroons politics",
    title="Southern Cameroons parties and constitutional steps", lesson="h7-sc-parties-and-constitutional-steps",
    questions=[
        Q("Where did the Southern Cameroons House of Assembly meet after 1954?",
          "Buea", [
              ("Enugu", "Enugu was the Eastern Region capital, which Southern Cameroons left."),
              ("Yaounde", "Yaounde was the capital of the Republic of Cameroun."),
              ("Lagos", "Lagos was the federal capital of Nigeria."),
          ], "The House met at Buea.", "Southern Cameroons assembly", "Recall", "It lies at the foot of Mount Cameroon."),
        Q("Who founded the KNDP in 1955?",
          "John Ngu Foncha", [
              ("E. M. L. Endeley", "Endeley led the KNC."),
              ("Ndeh Ntumazah", "Ntumazah led One Kamerun."),
              ("Ahmadou Ahidjo", "Ahidjo was a leader in the Republic of Cameroun."),
          ], "Foncha left the KNC and founded the KNDP.", "KNDP", "Recall", "He later became Premier."),
        Q("Which party was close to the UPC and called for immediate reunification?",
          "One Kamerun", [
              ("KNC", "The KNC leaned towards Nigeria."),
              ("KPP", "The KPP cooperated with Endeley."),
              ("CPNC", "The CPNC was formed by Endeley and Kale around 1960."),
          ], "One Kamerun, led by Ntumazah, was linked to the UPC.", "One Kamerun", "Recall", "The name itself suggests the aim."),
        Q("What triggered Southern Cameroons members to leave the Enugu assembly in 1953?",
          "A crisis in Eastern Region politics", [
              ("The plebiscite", "The plebiscite took place in 1961."),
              ("The Foumban conference", "Foumban was held in 1961."),
              ("The UPC ban in French Cameroun", "The 1955 ban was a different event."),
          ], "A crisis in the Eastern Region led to the walkout and a demand for separate status.",
          "1953 crisis", "Concept", "It happened inside the Eastern Region."),
        Q("What did the 1954 constitution give Southern Cameroons?",
          "A separate House of Assembly at Buea within a quasi-federal arrangement", [
              ("Full independence", "Independence was not given in 1954."),
              ("Membership of the French Union", "It was part of the British side."),
              ("A seat in the Security Council", "Southern Cameroons had no such seat."),
          ], "The 1954 constitution gave a separate House and government with a link to Nigeria.",
          "1954 constitution", "Concept", "Think of the new place where the House met."),
        Q("Why is a narrow seat majority for the KNDP in January 1959 not proof that voters wanted reunification?",
          "Voters may have chosen the party for other reasons, such as dislike of Nigerian domination", [
              ("Because the KNDP did not contest the election", "The KNDP did contest and won."),
              ("Because the election was held in 1961", "It was held in January 1959."),
              ("Because seat counts are never recorded", "Seat counts are recorded."),
          ], "Election results show party support, not the reasons of each voter.",
          "1959 election", "Reasoning", "Ask what a vote for a party actually measures."),
        N("In which year did Foncha found the KNDP?", 1955,
          "The KNDP was founded in 1955.", "KNDP", "Recall", "It was founded after the Eastern Region crisis of 1953."),
        Q("Which description of a campaign leaflet is the most accurate for a historian?",
          "It is persuasive and one-sided, so it shows what a party wanted voters to believe", [
              ("It is a neutral record of the election result", "Leaflets argue for a side and are not neutral records."),
              ("It is a UN report", "Leaflets come from parties."),
              ("It gives the exact number of voters", "Leaflets rarely give such figures."),
          ], "Campaign material is evidence of a party's message and its audience.",
          "Source evaluation", "Interpretation", "Think about the purpose of a leaflet."),
    ]))

# ---------------------------------------------------------------- 4. Plebiscite
SETS.append(practice_set(
    module=M_CMR, topic="Southern Cameroons politics",
    title="Mamfe, the UN decisions and the plebiscites", lesson="h7-sc-mamfe-un-decisions-plebiscites",
    questions=[
        Q("What was the main result of the Mamfe conference of August 1959?",
          "Leaders failed to agree on the plebiscite questions, so the UN decided", [
              ("The conference set the date of independence", "Independence terms were not set at Mamfe."),
              ("It created the Federal Republic", "The federation began in October 1961."),
              ("It banned the KNDP", "No such ban took place."),
          ], "The disagreement at Mamfe led the UN to fix the options.", "Mamfe conference", "Recall", "Who decided after the leaders disagreed?"),
        Q("Which two options were put to Southern Cameroons voters in 1961?",
          "Join Nigeria or join the Republic of Cameroun", [
              ("Independence alone or union with Nigeria", "Independence alone was not offered."),
              ("Union with Gabon or union with Chad", "These states were not options."),
              ("Continued British rule or union with Cameroun", "Continued trusteeship was not offered."),
          ], "Both options were forms of independence by joining an independent state.",
          "Two-option ballot", "Recall", "Neither option was a separate state."),
        Q("What did Northern Cameroons decide in 1961?",
          "To join Nigeria", [
              ("To join the Republic of Cameroun", "That was the choice of the south."),
              ("To become a separate state", "A separate state was not on the ballot."),
              ("To remain a British colony", "Trusteeship was ending."),
          ], "The north voted for Nigeria and joined it on 1 June 1961.",
          "Northern Cameroons", "Recall", "It is the opposite of the south's choice."),
        Q("On what date did Southern Cameroons become part of the Federal Republic?",
          "1 October 1961", [
              ("1 January 1960", "That is the independence of the Republic of Cameroun."),
              ("1 June 1961", "That is when Northern Cameroons joined Nigeria."),
              ("20 May 1972", "That is the date of the referendum creating a unitary state."),
          ], "The Federal Republic began on 1 October 1961.", "Date of union", "Recall", "It was after Foumban in July."),
        Q("Which court gave a decision in 1963 on Cameroun's challenge about Northern Cameroons?",
          "The International Court of Justice", [
              ("The European Court of Human Rights", "This court is not connected with the case."),
              ("The Supreme Court of Nigeria", "The challenge was between states at the world court."),
              ("The Security Council", "The Council is not a court."),
          ], "The ICJ decided in 1963 that it could not rule on the case.", "ICJ", "Recall", "Which UN court settles disputes between states?"),
        Q("Which argument is used AGAINST offering a separate-independence option?",
          "Doubts about the territory's economic viability", [
              ("The principle of self-determination in the Charter", "This is used by those who FAVOUR a third option."),
              ("The results of the Foumban conference", "Foumban was after the plebiscite."),
              ("The Treaty of Lagos", "This created ECOWAS in 1975."),
          ], "Reports at the time raised doubts about the territory's viability as a separate state.",
          "Third option debate", "Reasoning", "Which argument is about money and size?"),
        N("Roughly what percentage (to the nearest ten) of Southern Cameroons voters chose to join Cameroun if the vote was about seven in ten?", 70,
          "Seven in ten is 70 percent. Check your textbook for the exact figures.", "Plebiscite results", "Calculation",
          "Convert seven out of ten to a percentage.", unit="percent"),
        Q("Why can historians not say how voters would have chosen if a third option had been offered?",
          "It is a counterfactual and no such vote took place", [
              ("Because all records were destroyed", "The problem is logical, not only about records."),
              ("Because voters were not allowed to vote", "Voters did vote in 1961."),
              ("Because the UN did not keep any record", "The UN kept records of the process."),
          ], "A counterfactual cannot be settled by documents alone.", "Counterfactuals", "Reasoning",
          "Think about what a vote that never happened can tell us."),
    ]))

# ---------------------------------------------------------------- 5. Foumban
SETS.append(practice_set(
    module=M_CMR, topic="Southern Cameroons politics",
    title="Foumban: sources and interpretations", lesson="h7-sc-foumban-sources-interpretations",
    questions=[
        Q("In which month and year was the Foumban conference held?",
          "July 1961", [
              ("February 1961", "February 1961 was the month of the plebiscites."),
              ("October 1961", "The Federal Republic began in October 1961."),
              ("January 1960", "January 1960 was the independence of the Republic of Cameroun."),
          ], "Foumban took place in July 1961 (check the exact days).", "Foumban", "Recall", "It was between the plebiscite and the start of the federation."),
        Q("Who became Vice-President of the Federal Republic in 1961?",
          "John Ngu Foncha", [
              ("Ahmadou Ahidjo", "Ahidjo was Federal President."),
              ("E. M. L. Endeley", "Endeley led the CPNC opposition in West Cameroon."),
              ("Paul Biya", "Biya became President in 1982."),
          ], "Foncha, from West Cameroon, was Vice-President.", "Federal offices", "Recall", "The post went to someone from West Cameroon."),
        Q("Which feature did West Cameroon keep under the 1961 constitution?",
          "A House of Assembly, a House of Chiefs and a common-law system", [
              ("Its own army", "Defence was a federal matter."),
              ("Its own foreign policy", "Foreign affairs were federal."),
              ("Its own currency", "No separate currency was issued."),
          ], "West Cameroon kept its own government, legislature and legal tradition.",
          "Federal constitution", "Recall", "Think of the state's own institutions and its law."),
        Q("Which source would be the BEST evidence of what was formally adopted at Foumban?",
          "The text of the constitution", [
              ("A memoir written thirty years later", "Memoirs may be shaped by memory and later events."),
              ("A campaign leaflet from the plebiscite", "Leaflets show a party's message, not the final text."),
              ("A rumour recorded in a letter", "Rumours are not reliable records of a formal outcome."),
          ], "Official texts show what was adopted, though not how the talks went.",
          "Source types", "Reasoning", "Which source is a formal record?"),
        Q("Which reading says that the structure created two federated states with real institutions?",
          "A negotiated-settlement reading", [
              ("An imposed-settlement reading", "That reading says the draft was prepared in advance and few amendments were accepted."),
              ("An unequal-partners reading", "That reading stresses the difference of status."),
              ("A plebiscite-only reading", "No such school exists."),
          ], "The negotiated reading points to the structure and offices.", "Interpretations of Foumban", "Concept",
          "Which reading stresses what was agreed?"),
        Q("What does the term 'provenance' ask you to consider?",
          "Who produced the source, when and why", [
              ("Only how long the source is", "Length is not provenance."),
              ("Whether you agree with the source", "Agreement is not provenance."),
              ("Only the title", "The title is one small part."),
          ], "Provenance covers author, date and purpose.", "Provenance", "Recall", "It is about the origin of the source."),
        N("In which year did the Federal Republic of Cameroon begin?", 1961,
          "The Federal Republic began on 1 October 1961.", "Federal Republic", "Recall", "It followed the plebiscite and Foumban."),
        Q("An invented memoir says 'the text was already prepared'. What is a sensible way to test this?",
          "Compare with other accounts, drafts and press reports, and note when it was written", [
              ("Accept it because it is a memoir", "A memoir is one voice and may be selective."),
              ("Reject it because memoirs are always false", "Memoirs can contain valuable detail if checked."),
              ("Ignore the date", "The date matters, since memory and later events may shape an account."),
          ], "Cross-checking with other sources is the standard method.", "Source evaluation", "Interpretation",
          "A single source is rarely enough."),
    ]))

# ---------------------------------------------------------------- 6. Federation to unitary state
SETS.append(practice_set(
    module=M_CMR, topic="The post-colonial state",
    title="From federation to the unitary state", lesson="h7-pcs-federation-to-unitary-state",
    questions=[
        Q("What is a federation?",
          "A state in which powers are divided by the constitution between a central and regional governments", [
              ("A state in which all powers belong to one central government", "That describes a unitary state."),
              ("A union of independent states with no central government", "A federation has a central government."),
              ("A state ruled by a single party", "A single party is a political arrangement, not a federal structure."),
          ], "In a federation the constitution divides powers between levels of government.",
          "Federalism", "Recall", "Think of two levels of government."),
        Q("When was the Cameroon National Union (CNU) formed?",
          "September 1966", [
              ("October 1961", "That is when the Federal Republic began."),
              ("May 1972", "That is the month of the referendum."),
              ("March 1985", "In 1985 the CNU was renamed CPDM."),
          ], "The main parties of both states merged into the CNU in September 1966.", "CNU", "Recall", "It came five years after reunification."),
        Q("What did the referendum of 20 May 1972 create?",
          "The United Republic of Cameroon, a unitary state", [
              ("The Federal Republic of Cameroon", "That was created in 1961."),
              ("The Republic of Cameroon", "That name came in 1984."),
              ("The Southern Cameroons House of Assembly", "That was created in 1954."),
          ], "The referendum approved a unitary state and ended the federation.", "1972 referendum", "Recall", "Look at the words 'United Republic'."),
        Q("Which of these was federal under the 1961 constitution?",
          "Defence and foreign affairs", [
              ("The West Cameroon House of Chiefs", "This was a West Cameroon institution."),
              ("The common-law courts of West Cameroon", "These were state-level."),
              ("The East Cameroon assembly's local rules", "These were state-level."),
          ], "Defence and foreign affairs were federal powers.", "Federal powers", "Concept", "Which powers must a single country keep at the centre?"),
        Q("Which argument was used by supporters of the unitary state in 1972?",
          "One government would strengthen unity and reduce cost", [
              ("The federal form had been guaranteed for ever", "That is an argument used by critics of the change."),
              ("West Cameroon had asked for abolition", "Supporters did not rely on such a request; critics noted the loss of West Cameroon institutions."),
              ("The UN had ordered the change", "The UN made no such order."),
          ], "The official arguments were unity and cost.", "Arguments for 1972", "Concept", "Which arguments appear in the official speeches?"),
        Q("Which argument is used by critics of the 1972 change?",
          "It set aside the 1961 revision procedure and weakened West Cameroon institutions", [
              ("It increased the number of governments", "The change reduced the number of governments."),
              ("It created a multiparty system", "A single party remained until 1990."),
              ("It had no official result", "An official result was announced."),
          ], "Critics point to the revision procedure and to the loss of federal guarantees (check your textbook).",
          "Arguments against 1972", "Concept", "Which argument concerns the 1961 guarantees?"),
        N("How many years passed between the start of the Federal Republic in 1961 and the referendum of 1972?", 11,
          "1972 minus 1961 is 11 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("What can an official speech on the cost of two governments tell a historian?",
          "How the change was justified, but not how people felt", [
              ("The exact opinion of every voter", "A speech cannot show individual opinions."),
              ("That the referendum was fair", "A speech does not prove fairness."),
              ("Nothing at all", "It is useful evidence of the official case."),
          ], "Purpose and provenance show its value and limits.", "Source evaluation", "Interpretation", "Who is speaking, and to persuade whom?"),
    ]))

# ---------------------------------------------------------------- 7. One-party, transition, liberalization
SETS.append(practice_set(
    module=M_CMR, topic="The post-colonial state",
    title="One-party rule, the 1982 transition and liberalization", lesson="h7-pcs-one-party-transition-liberalization",
    questions=[
        Q("Who succeeded Ahmadou Ahidjo as President in November 1982?",
          "Paul Biya", [
              ("John Fru Ndi", "Fru Ndi led the SDF, an opposition party."),
              ("John Ngu Foncha", "Foncha was Vice-President in 1961."),
              ("Andre-Marie Mbida", "Mbida was Prime Minister in 1957 to 1958."),
          ], "Biya, the Prime Minister, became President under the constitution.", "1982 transition", "Recall", "He had been Prime Minister since 1975."),
        Q("In which year did the CNU become the CPDM?",
          "1985", [
              ("1982", "In 1982 Biya succeeded Ahidjo."),
              ("1990", "In 1990 the SDF was launched and party laws passed."),
              ("1996", "In 1996 a new constitution was adopted."),
          ], "The change of name came at the Bamenda congress of 1985.", "CPDM", "Recall", "It came one year after the state was renamed."),
        Q("Where and when was the SDF launched?",
          "Bamenda, May 1990", [
              ("Douala, April 1948", "That is the UPC's founding."),
              ("Buea, April 1993", "That was the All Anglophone Conference."),
              ("Yaounde, December 1991", "That is not the launch of the SDF."),
          ], "The SDF, led by John Fru Ndi, was launched in Bamenda on 26 May 1990.", "SDF", "Recall", "It was the first major opposition party of the 1990s."),
        Q("Which is an EXTERNAL cause of the political opening of 1990?",
          "The end of the Cold War and donor pressure", [
              ("The villes mortes campaigns", "They were organised inside the country."),
              ("The SDF launch", "The SDF was a Cameroonian party."),
              ("Falling export revenues inside the country", "This was mainly a domestic economic cause, though linked to world prices."),
          ], "External causes come from outside the country.", "Causes of liberalization", "Concept", "Which cause is international?"),
        Q("What were the 'villes mortes' of 1991?",
          "Campaigns of stay-at-home and shop closures to press for reform", [
              ("Military operations in towns", "They were civil protest actions."),
              ("New cities built by the government", "The phrase means 'ghost towns'."),
              ("A UN peace mission", "The UN was not involved."),
          ], "Villes mortes were a form of civil disobedience.", "Villes mortes", "Concept", "Think of what a ghost town looks like."),
        Q("Which statement best expresses a 'continuity' reading of 1982 to 1985?",
          "The one-party system, strong presidency and unitary state continued despite the new name", [
              ("Everything changed, including the constitution", "This overstates change."),
              ("The state was federal again", "The unitary state remained."),
              ("Multiparty politics began in 1985", "Multiparty politics came in 1990."),
          ], "Continuity readings stress what did not change.", "Interpretations", "Reasoning", "Which option says nothing important changed?"),
        N("How many years passed between the formation of the CNU in 1966 and its renaming in 1985?", 19,
          "1985 minus 1966 is 19 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("A foreign press report of the SDF launch says the evening 'ended in confusion and loss of life'. What is a reasonable use of it?",
          "As evidence the launch was contested, to be cross-checked with other accounts", [
              ("As proof of the exact number killed", "It gives no number."),
              ("As the final official account", "It is a press report and not an official account."),
              ("As proof of who was responsible", "It does not say who was responsible."),
          ], "A quick press report is useful but limited. Cross-checking is needed.", "Source evaluation", "Interpretation", "What does the report actually say?"),
    ]))

# ---------------------------------------------------------------- 8. 1996 constitution & historiography
SETS.append(practice_set(
    module=M_CMR, topic="The post-colonial state",
    title="The 1996 constitution and the historiography of the Anglophone question",
    lesson="h7-pcs-1996-constitution-historiography",
    questions=[
        Q("How did the 1996 constitution describe the state?",
          "A decentralized unitary state", [
              ("A federation of two states", "The federation ended in 1972."),
              ("A one-party republic", "Multiparty politics had been allowed since 1990."),
              ("A confederation of regions", "A confederation was not created."),
          ], "The text kept a unitary state described as decentralized.", "1996 constitution", "Recall", "It combines two ideas."),
        Q("Where did the All Anglophone Conference of April 1993 meet?",
          "Buea", [
              ("Foumban", "Foumban hosted the 1961 conference."),
              ("Mamfe", "Mamfe hosted the 1959 conference."),
              ("Yaounde", "It was not held in the capital."),
          ], "The first All Anglophone Conference was held in Buea.", "Anglophone conferences", "Recall", "It is a town at the foot of Mount Cameroon."),
        Q("Which of these is a DESCRIPTION rather than an interpretation?",
          "The 1996 constitution provides for English and French as official languages", [
              ("The 1972 referendum proves that all people wanted a unitary state", "This is an interpretation that can be challenged."),
              ("The 1996 text answered every demand of the conferences", "This is an interpretation."),
              ("The Anglophone question is only a matter of language", "This is an interpretation."),
          ], "A description is a checkable fact about a text or an event.", "Description and interpretation", "Concept",
          "Which sentence could be checked in a document?"),
        Q("Which wording is the more neutral way to describe a government decision?",
          "'did not accept the request'", [
              ("'crushed the request'", "This is a charged verb."),
              ("'betrayed the request'", "This is a charged verb that judges motives."),
              ("'killed the request'", "This is figurative and loaded."),
          ], "Neutral wording describes the event and its date.", "Neutral language", "Application", "Choose the plain description."),
        Q("Which kind of evidence do supporters of a federal form mainly use?",
          "The 1961 constitution and the 1993 and 1994 conference documents", [
              ("Only the results of the 1992 elections", "The 1992 elections are not the main evidence for this position."),
              ("The OAU Charter", "The OAU Charter is not about Cameroon's internal structure."),
              ("The Treaty of Lagos", "This is about ECOWAS."),
          ], "They point to the 1961 text and the conference documents.", "Positions in the debate", "Concept", "Which documents concern federalism?"),
        Q("What is historiography?",
          "The study of how historians have written about a subject and why they differ", [
              ("The study of ancient writing", "That is palaeography."),
              ("A list of dates", "A list of dates is a chronology."),
              ("The history of the printing press", "That is a different subject."),
          ], "Historiography compares interpretations and the evidence for each.", "Historiography", "Recall", "It is the history of writing about history."),
        N("What is the length in years of the presidential term set in the 1996 constitution?", 7,
          "The 1996 constitution set a seven-year term. Check your textbook for later amendments.", "1996 constitution", "Recall",
          "It is longer than five years.", unit="years"),
        Q("How should a student treat very recent events in the North-West and South-West regions in an essay?",
          "Use reliable sources, record well-documented facts and avoid the vocabulary of any one party", [
              ("State the strongest claim of one side as a fact", "This is not balanced."),
              ("Leave out all dates", "Dates are essential for accuracy."),
              ("Use rumours if they sound convincing", "Rumours are not reliable evidence."),
          ], "Sensitive and recent topics need careful use of evidence and neutral wording.", "Balanced writing", "Reasoning",
          "Which choice respects both accuracy and fairness?"),
    ]))

# ---------------------------------------------------------------- 9. Ghana and Nigeria
SETS.append(practice_set(
    module=M_DEC, topic="Constitutional transfers",
    title="British transfers: the Gold Coast and Nigeria", lesson="h7-dec-british-transfers-ghana-nigeria",
    questions=[
        Q("On what date did Ghana become independent?",
          "6 March 1957", [
              ("1 October 1960", "That is Nigeria's independence."),
              ("1 January 1960", "That is Cameroun's independence."),
              ("12 December 1963", "That is Kenya's independence."),
          ], "Ghana was independent on 6 March 1957.", "Ghana's independence", "Recall", "It was the first of the group in this topic."),
        Q("Who founded the Convention People's Party (CPP) in 1949?",
          "Kwame Nkrumah", [
              ("Nnamdi Azikiwe", "Azikiwe led the NCNC in Nigeria."),
              ("Obafemi Awolowo", "Awolowo led the Action Group in Nigeria."),
              ("Ahmadu Bello", "Bello was a Northern Nigerian leader."),
          ], "Nkrumah founded the CPP in June 1949.", "CPP", "Recall", "He called for 'self-government now'."),
        Q("Why did Nigeria adopt a federal system?",
          "Regional differences and fears of domination by one region", [
              ("It had only one region", "Nigeria had three main regions."),
              ("The USSR required a federation", "The USSR had no such role."),
              ("Britain had no other option", "Britain had a choice and chose a federation because of regional differences."),
          ], "Federation fitted Nigeria's size and regional parties.", "Nigerian federation", "Concept", "Think of the three regions."),
        Q("What was the effect of the 1951 election in the Gold Coast?",
          "The CPP won most seats and Nkrumah became Leader of Government Business", [
              ("Independence was declared at once", "Independence came in 1957."),
              ("The CPP was banned", "The CPP won."),
              ("British rule ended in Nigeria too", "Nigeria's independence came in 1960."),
          ], "The 1951 election began the transfer of power under CPP leadership.", "1951 election", "Concept", "He had been in jail before the vote."),
        Q("Which of these is a feature of 'constitutional decolonization'?",
          "A series of constitutions, elections and conferences leading to independence", [
              ("A long war of liberation", "That is armed liberation."),
              ("Immediate independence without any preparation", "This is not the model described."),
              ("Permanent rule by the colonial power", "This is the opposite of decolonization."),
          ], "Constitutional change in stages was the British approach.", "Constitutional decolonization", "Concept", "It is the opposite of armed struggle."),
        Q("Which speech of February 1960 is often cited as a sign of British realism about colonial rule?",
          "Harold Macmillan's 'wind of change' speech in Cape Town", [
              ("De Gaulle's Brazzaville speech", "That was in 1944."),
              ("Nkrumah's independence speech", "That was in 1957 in Ghana."),
              ("Truman's address on Greece and Turkey", "That was in 1947."),
          ], "Macmillan spoke in Cape Town in February 1960.", "Wind of change", "Recall", "He was the British Prime Minister."),
        N("How many years passed between Ghana's independence (1957) and Nigeria's (1960)?", 3,
          "1960 minus 1957 is 3 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("Which statement best qualifies the claim that Nigeria's transfer was a success?",
          "The transfer was peaceful but left regional rivalries that caused later crises", [
              ("The transfer failed immediately in 1960", "Independence was achieved peacefully."),
              ("There were no problems after independence", "Later coups and a civil war show problems."),
              ("The federation was abolished in 1960", "The federation continued."),
          ], "A balanced judgement notes both the peaceful transfer and later problems.", "Evaluating the transfer", "Reasoning",
          "Look for the answer that gives both sides."),
    ]))

# ---------------------------------------------------------------- 10. French Loi-Cadre & Guinea
SETS.append(practice_set(
    module=M_DEC, topic="Constitutional transfers",
    title="French Africa: the Loi-Cadre, the 1958 referendum and Guinea", lesson="h7-dec-french-loi-cadre-guinea-1958",
    questions=[
        Q("What was the Loi-Cadre of 1956?",
          "A law giving territories elected assemblies and councils with African ministers", [
              ("The constitution of the Fifth Republic", "That was voted on in 1958."),
              ("A treaty creating the OAU", "The OAU was founded in 1963."),
              ("A UN resolution on trusteeship", "It was a French law."),
          ], "The Loi-Cadre extended self-government within the French system.", "Loi-Cadre", "Recall", "'Cadre' means framework."),
        Q("Which territory voted No in the referendum of 28 September 1958?",
          "Guinea", [
              ("Senegal", "Senegal voted Yes."),
              ("Cote d'Ivoire", "Cote d'Ivoire voted Yes."),
              ("Cameroun", "Cameroun was a trust territory and did not vote in that referendum."),
          ], "Guinea voted No and became independent on 2 October 1958.", "Guinea's No", "Recall", "Its leader was Sekou Toure."),
        Q("What would a Yes vote in 1958 have meant?",
          "Membership of the French Community with France controlling key areas", [
              ("Immediate full independence", "Immediate independence was the result of a No."),
              ("Union with Britain", "No such union was offered."),
              ("Membership of the OAU", "The OAU did not exist."),
          ], "A Yes meant autonomy within the Community, with France keeping defence and foreign policy.",
          "Referendum options", "Concept", "A No meant independence."),
        Q("Which conference in 1944 promised reforms but ruled out independence?",
          "The Brazzaville Conference", [
              ("The Bandung Conference", "That was in 1955."),
              ("The Lancaster House conference", "That was a British conference."),
              ("The Evian conference", "Evian was about Algeria in 1962."),
          ], "Brazzaville set French wartime policy.", "Brazzaville", "Recall", "It was held in French Equatorial Africa."),
        Q("What did France do after Guinea's No vote?",
          "It withdrew administrators and aid quickly", [
              ("It sent a UN force", "No UN force was sent."),
              ("It increased aid immediately", "The opposite occurred."),
              ("It annexed Guinea", "France recognised Guinea's independence."),
          ], "France cut ties sharply, and Guinea turned to other partners.", "Guinea after 1958", "Concept", "Think about what was done to discourage others."),
        Q("Which factor helps explain why most territories voted Yes?",
          "Fear of losing French aid and trust in leaders such as Houphouet-Boigny", [
              ("A ban on all political parties", "Parties were active."),
              ("An order from the UN", "The vote was a French referendum."),
              ("A lack of any African leaders", "Many African leaders campaigned."),
          ], "Security and local leaders' influence favoured Yes.", "Reasons for Yes", "Reasoning", "Which factor is about caution and trust?"),
        N("How many years passed between Guinea's independence (1958) and the main wave of independences in 1960?", 2,
          "1960 minus 1958 is 2 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("How did the Loi-Cadre affect the large federations of French West and Equatorial Africa?",
          "It strengthened individual territories and weakened the federal units", [
              ("It strengthened the federations", "It divided powers among smaller territories."),
              ("It abolished all territorial assemblies", "It created them."),
              ("It made the federations independent", "They stayed under French rule."),
          ], "The reform gave powers to the territories rather than to the federations.", "Loi-Cadre effects", "Reasoning",
          "Critics said it 'Balkanised' the federations (check your textbook)."),
    ]))

# ---------------------------------------------------------------- 11. Algeria and Kenya
SETS.append(practice_set(
    module=M_DEC, topic="Armed liberation",
    title="Algeria and Kenya: settlers, war and independence", lesson="h7-dec-algeria-kenya-armed-struggle",
    questions=[
        Q("What is a settler colony?",
          "A colony with a large population of settlers who held land and privileges", [
              ("A colony without any foreign population", "That would not be a settler colony."),
              ("A colony ruled by the UN", "That is a trust territory."),
              ("A colony that is a military base only", "A settler colony has permanent settlers."),
          ], "Settlers resisted majority rule, making compromise hard.", "Settler colony", "Recall", "Think of where they lived and farmed."),
        Q("When did the FLN begin its armed struggle in Algeria?",
          "1 November 1954", [
              ("1 January 1960", "That is Cameroun's independence."),
              ("5 July 1962", "That is Algeria's independence."),
              ("15 August 1945", "No such start date for the FLN."),
          ], "FLN attacks began on 1 November 1954.", "Algerian war", "Recall", "It began in the same decade as Bandung."),
        Q("Which agreement of 1962 ended the Algerian war?",
          "The Evian Accords", [
              ("The Lancaster House Agreement", "That relates to Kenya and Zimbabwe."),
              ("The Dayton Agreement", "That ended the Bosnian war in 1995."),
              ("The Arusha Accords", "That relates to Rwanda in 1993."),
          ], "The Evian Accords of March 1962 led to a ceasefire and a referendum.", "Evian Accords", "Recall", "It is named after a French town."),
        Q("What did the British declare in Kenya in October 1952?",
          "A State of Emergency", [
              ("Independence", "Independence came in 1963."),
              ("A federation", "No federation was created."),
              ("A plebiscite", "No plebiscite was held."),
          ], "The Emergency followed the rise of Mau Mau.", "Kenyan Emergency", "Recall", "It allowed arrests and detention."),
        Q("Who became the leader of Kenya at independence in December 1963?",
          "Jomo Kenyatta", [
              ("Dedan Kimathi", "Kimathi was a Mau Mau leader who was executed in 1957."),
              ("Ahmed Ben Bella", "Ben Bella led Algeria."),
              ("Robert Mugabe", "Mugabe led Zimbabwe."),
          ], "Kenyatta, released from detention in 1961, led Kenya to independence.", "Kenyatta", "Recall", "He had been tried at Kapenguria."),
        Q("Which sentence about casualty figures is the safest?",
          "Figures are disputed and depend on the sources and methods used", [
              ("All historians accept one exact figure", "Figures differ widely."),
              ("No one was killed", "Many people were killed."),
              ("Only soldiers died", "Civilians were also affected."),
          ], "Good history says what is uncertain.", "Casualty figures", "Reasoning", "Which wording avoids a false certainty?"),
        N("How many years passed between the start of the FLN war (1954) and Algerian independence (1962)?", 8,
          "1962 minus 1954 is 8 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("Which factor made peaceful transfer harder in both Algeria and Kenya?",
          "A significant settler population with land and privileges", [
              ("A lack of any nationalist movement", "Both had nationalist movements."),
              ("A UN trusteeship agreement", "Neither was a trust territory."),
              ("A shortage of European settlers", "The problem was the presence of many settlers."),
          ], "Settlers resisted majority rule and the colonial power was influenced by them.", "Settlers and violence", "Reasoning",
          "What did these two countries have that Ghana did not?"),
    ]))

# ---------------------------------------------------------------- 12. Portuguese colonies & Zimbabwe
SETS.append(practice_set(
    module=M_DEC, topic="Armed liberation",
    title="The Portuguese colonies and Zimbabwe", lesson="h7-dec-portuguese-colonies-zimbabwe",
    questions=[
        Q("Which movement was led by Amilcar Cabral?",
          "PAIGC", [
              ("FRELIMO", "FRELIMO was led by Mondlane and then Machel."),
              ("MPLA", "The MPLA's leader was Agostinho Neto."),
              ("ZANU", "ZANU was a Zimbabwean party."),
          ], "The PAIGC fought for Guinea-Bissau and Cape Verde.", "PAIGC", "Recall", "It began its war in 1963."),
        Q("Which event of April 1974 changed the situation in the Portuguese colonies?",
          "An officers' coup in Lisbon", [
              ("The Evian Accords", "That was 1962 and about Algeria."),
              ("The Lancaster House conference", "That was in 1979."),
              ("The independence of Ghana", "That was in 1957."),
          ], "The Carnation Revolution led Portugal to end the colonial wars.", "Carnation Revolution", "Recall", "It took place in Portugal."),
        Q("In which year did Mozambique become independent?",
          "1975", [
              ("1960", "1960 was the wave of independence in French Africa."),
              ("1980", "That is Zimbabwe's independence."),
              ("1963", "That is Kenya's independence."),
          ], "Mozambique became independent in June 1975.", "Mozambique", "Recall", "It is the same year as Angola."),
        Q("What was UDI?",
          "A Unilateral Declaration of Independence by Rhodesia's white minority government in 1965", [
              ("A UN resolution on Rhodesia", "UDI was a declaration by Smith's government."),
              ("A peace treaty of 1979", "The 1979 settlement was reached at Lancaster House."),
              ("A union of Rhodesia and Mozambique", "No such union existed."),
          ], "UDI was declared in November 1965 by Ian Smith's government.", "UDI", "Recall", "Think about who was declaring independence from whom."),
        Q("Which conference led to Zimbabwe's independence?",
          "Lancaster House", [
              ("Foumban", "Foumban was in Cameroon, 1961."),
              ("Mamfe", "Mamfe was in 1959."),
              ("Bandung", "Bandung was held in 1955."),
          ], "Lancaster House (1979) agreed a ceasefire, constitution and elections.", "Lancaster House", "Recall", "It was held in London."),
        Q("Which factor helped force Rhodesia's government to negotiate?",
          "The war, sanctions and the loss of Portuguese-ruled neighbours", [
              ("A UN military occupation", "There was no UN occupation."),
              ("The success of apartheid", "Rhodesia's position weakened."),
              ("A vote of the UN Trusteeship Council", "Rhodesia was not a trust territory."),
          ], "Several pressures worked together.", "Rhodesia's end", "Reasoning", "Which option lists several pressures?"),
        N("How many years passed between UDI (1965) and Zimbabwe's independence (1980)?", 15,
          "1980 minus 1965 is 15 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("Why is it unsafe to say that Angola became independent peacefully in 1975?",
          "A civil war between the movements, with foreign involvement, followed", [
              ("Angola did not become independent", "It became independent in November 1975."),
              ("Portugal remained in control", "Portugal left in 1975."),
              ("The UN governed it", "The UN did not govern Angola."),
          ], "Independence was followed by conflict between the three movements.", "Angola after 1975", "Reasoning",
          "Think about what happened after the Portuguese left."),
    ]))

# ---------------------------------------------------------------- 13. Apartheid
SETS.append(practice_set(
    module=M_DEC, topic="South Africa",
    title="Apartheid: laws and early resistance", lesson="h7-sa-apartheid-system-early-resistance",
    questions=[
        Q("In which year did the National Party win the election that began the apartheid era?",
          "1948", [
              ("1960", "1960 was the year of Sharpeville."),
              ("1912", "1912 was the founding of the ANC."),
              ("1994", "1994 was the first all-race election."),
          ], "The National Party won in May 1948.", "1948 election", "Recall", "It is the date that begins the timeline."),
        Q("Which law classified every person by race?",
          "The Population Registration Act", [
              ("The Group Areas Act", "It set residential areas."),
              ("The Bantu Education Act", "It governed schooling."),
              ("The Suppression of Communism Act", "It gave the state powers against opponents."),
          ], "The 1950 Act set the categories on which other laws relied.", "Population Registration Act", "Recall", "Registration means listing people."),
        Q("What did the Group Areas Act lead to?",
          "Separate residential areas and forced removals", [
              ("Equal schools for all", "It was not an education law."),
              ("The end of pass laws", "Pass laws continued."),
              ("A multiparty constitution", "The vote was not extended."),
          ], "People were moved to areas set by their racial category.", "Group Areas Act", "Concept", "Think about where people could live."),
        Q("What was the Freedom Charter?",
          "A statement of demands for a non-racial, democratic South Africa adopted at Kliptown in 1955", [
              ("The founding treaty of the AU", "That is the Constitutive Act."),
              ("A law passed by the National Party", "It was an opposition document."),
              ("A UN resolution on sanctions", "It was not a UN text."),
          ], "The Congress of the People adopted it in June 1955.", "Freedom Charter", "Recall", "It was adopted by the opposition."),
        Q("Who organised the protest at Sharpeville on 21 March 1960?",
          "The Pan Africanist Congress", [
              ("The ANC", "The ANC was also banned afterwards, but the protest was a PAC campaign."),
              ("The National Party", "The National Party was the government."),
              ("The United Democratic Front", "The UDF was formed in 1983."),
          ], "The PAC called a campaign against pass laws.", "Sharpeville", "Recall", "The PAC broke away from the ANC in 1959."),
        Q("Which was a result of Sharpeville?",
          "The ANC and PAC were banned and the ANC later formed an armed wing", [
              ("Apartheid laws were repealed", "They were not repealed."),
              ("Mandela became President", "That came in 1994."),
              ("The UN ended all sanctions", "Sanctions were not yet in place on this scale."),
          ], "The bans and the turn to armed struggle followed.", "Effects of Sharpeville", "Concept", "What happened to the movements in April 1960?"),
        N("How many people, according to the figure most textbooks give, were killed at Sharpeville?", 69,
          "Most books give 69. Check your textbook.", "Sharpeville", "Recall", "The figure is in the high sixties."),
        Q("Which view of peaceful resistance in the 1950s best weighs the evidence?",
          "It built a movement and a programme but did not change the laws", [
              ("It repealed all apartheid laws by 1960", "The laws remained."),
              ("It had no support", "The Defiance Campaign had mass participation."),
              ("It was never banned", "The movements were banned in 1960."),
          ], "A balanced view notes achievements and limits.", "Evaluating resistance", "Reasoning", "Choose the answer that gives both sides."),
    ]))

# ---------------------------------------------------------------- 14. End of apartheid
SETS.append(practice_set(
    module=M_DEC, topic="South Africa",
    title="The end of apartheid: struggle, pressure and negotiation", lesson="h7-sa-struggle-pressure-negotiation-1994",
    questions=[
        Q("What was the Rivonia Trial?",
          "A trial of ANC and MK leaders, including Mandela, ending in life sentences in 1964", [
              ("A trial of the National Party leaders", "The accused were opposition leaders."),
              ("A UN trial of South Africa", "It was held in a South African court."),
              ("A trial that freed Mandela in 1964", "He was sentenced to life imprisonment."),
          ], "The Rivonia accused were sentenced in June 1964.", "Rivonia Trial", "Recall", "It followed arrests in 1963."),
        Q("What began on 16 June 1976?",
          "The Soweto uprising", [
              ("The Defiance Campaign", "That was in 1952."),
              ("The CODESA talks", "They began in December 1991."),
              ("The Treason Trial", "It began in 1956."),
          ], "School pupils marched in Soweto.", "Soweto", "Recall", "It began with a student protest."),
        Q("Which body was formed in 1983 to unite hundreds of anti-apartheid organisations?",
          "The United Democratic Front", [
              ("The Pan Africanist Congress", "The PAC was formed in 1959."),
              ("The African Union", "The AU was created in 2002."),
              ("The Congress of the People", "That met in 1955."),
          ], "The UDF was an umbrella for community and other groups.", "UDF", "Recall", "Its name includes 'United'."),
        Q("On what date was Nelson Mandela released from prison?",
          "11 February 1990", [
              ("2 February 1990", "This is the date of the unbanning speech."),
              ("27 April 1994", "This is the election period."),
              ("16 June 1976", "This is Soweto Day."),
          ], "Mandela was released nine days after the unbanning.", "Mandela's release", "Recall", "It followed the unbanning of the ANC."),
        Q("Which is an example of INTERNATIONAL pressure on South Africa?",
          "The UN arms embargo of 1977 and sanctions in the 1980s", [
              ("The Soweto uprising", "This was internal resistance."),
              ("The formation of the UDF", "This was internal organisation."),
              ("The Freedom Charter", "This was an internal document."),
          ], "The Security Council imposed a mandatory arms embargo in November 1977.", "International pressure", "Concept", "Which action came from outside the country?"),
        Q("Which explanation says apartheid ended because of its high economic and political cost?",
          "The economic-crisis explanation", [
              ("The unbanning explanation", "Unbanning was an event, not an explanation of the causes."),
              ("The Freedom Charter explanation", "The Charter was a statement of aims."),
              ("The Defiance Campaign explanation", "This was an early protest."),
          ], "Slow growth and the cost of defence weakened the system.", "Explanations", "Concept", "Which explanation is about money?"),
        N("For how many years was Mandela in prison before his release in 1990, according to most accounts?", 27,
          "Most accounts give 27 years (1962 to 1990).", "Mandela's imprisonment", "Recall", "He was jailed in 1962.", unit="years"),
        Q("A recollection of the Soweto protests written years later is useful mainly because it",
          "gives a personal view but is limited by memory and one viewpoint", [
              ("is a perfect record of the exact numbers killed", "Recollections rarely give exact numbers."),
              ("was written on the day of the events", "It was written years later."),
              ("comes from the police", "It is an eyewitness account."),
          ], "Eyewitness accounts show experience but need cross-checking.", "Source evaluation", "Interpretation", "Check when it was written."),
    ]))

# ---------------------------------------------------------------- 15. Containment, Marshall, deterrence
SETS.append(practice_set(
    module=M_CW, topic="Cold War geopolitics",
    title="Containment, the Marshall Plan and deterrence", lesson="h7-cw-containment-marshall-deterrence",
    questions=[
        Q("Which policy aimed to prevent the spread of Soviet influence?",
          "Containment", [
              ("Non-alignment", "Non-alignment was the policy of not joining either bloc."),
              ("Decolonization", "This is the end of colonial rule."),
              ("Appeasement", "Appeasement was the policy before the Second World War."),
          ], "Containment guided American policy from 1947.", "Containment", "Recall", "It is also called 'holding in'."),
        Q("What was the Truman Doctrine of March 1947?",
          "A pledge to support free peoples resisting pressure, beginning with aid to Greece and Turkey", [
              ("The founding of NATO", "NATO was founded in 1949."),
              ("A programme of aid to rebuild Western Europe", "That describes the Marshall Plan."),
              ("A Soviet plan for Eastern Europe", "The Truman Doctrine was American."),
          ], "It began American containment.", "Truman Doctrine", "Recall", "It is named after an American President."),
        Q("What was the Marshall Plan?",
          "American economic aid to rebuild Western Europe from 1948", [
              ("A military alliance of 1949", "That describes NATO."),
              ("A Soviet scheme for trade", "That describes Comecon."),
              ("An agreement ending the Berlin blockade", "The blockade ended in May 1949 after a Western air supply."),
          ], "The plan was economic, not military.", "Marshall Plan", "Recall", "It aimed at recovery."),
        Q("Which pair of dates is correct for NATO and the Warsaw Pact?",
          "NATO 1949, Warsaw Pact 1955", [
              ("NATO 1955, Warsaw Pact 1949", "These are reversed."),
              ("NATO 1945, Warsaw Pact 1947", "Both dates are wrong."),
              ("NATO 1961, Warsaw Pact 1962", "These dates are those of the Berlin Wall and the Cuban crisis."),
          ], "NATO was formed in April 1949, and the Warsaw Pact in May 1955.", "NATO and Warsaw Pact", "Recall", "The Pact followed West Germany's entry into NATO."),
        Q("What happened in the Berlin blockade?",
          "The USSR closed land access to West Berlin and the West supplied the city by air", [
              ("The West closed access to East Berlin", "The blockade was Soviet."),
              ("A nuclear war began", "There was no nuclear war."),
              ("Berlin was unified", "Berlin stayed divided."),
          ], "The blockade lasted from June 1948 to May 1949.", "Berlin blockade", "Concept", "The airlift is the key feature."),
        Q("Which description of deterrence is correct?",
          "The threat of unacceptable retaliation prevents an attack", [
              ("A policy of attacking first", "That is a pre-emptive policy."),
              ("A policy of disarming at once", "Deterrence depended on keeping weapons."),
              ("A policy of avoiding all alliances", "That is non-alignment."),
          ], "Both sides held nuclear arsenals to deter the other.", "Deterrence", "Concept", "Think about what stops an attacker."),
        N("How many years passed between the Truman Doctrine (1947) and the creation of the Warsaw Pact (1955)?", 8,
          "1955 minus 1947 is 8 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("Which school of historians argues that American economic power provoked Soviet fears?",
          "Revisionist", [
              ("Orthodox", "The orthodox school blames Soviet expansion."),
              ("Post-revisionist", "Post-revisionists stress mutual misperception."),
              ("Imperial", "This is not one of the three schools in this lesson."),
          ], "Revisionists stress American aims and power.", "Historiography of the Cold War", "Concept", "Which school challenges the traditional view?"),
    ]))

# ---------------------------------------------------------------- 16. Global South
SETS.append(practice_set(
    module=M_CW, topic="Cold War geopolitics",
    title="The Cold War in the Global South", lesson="h7-cw-global-south-africa",
    questions=[
        Q("In which country was the Bandung Conference of April 1955 held?",
          "Indonesia", [
              ("India", "India was a participant, not the host."),
              ("Egypt", "Egypt was a participant."),
              ("Yugoslavia", "The 1961 Non-Aligned Movement meeting was held at Belgrade."),
          ], "The Bandung Conference met in Indonesia.", "Bandung", "Recall", "The conference is named after the city."),
        Q("What does 'non-alignment' mean?",
          "Not joining either of the two military blocs", [
              ("Joining the Warsaw Pact only", "That would be alignment."),
              ("Accepting no aid from anyone", "Non-aligned states often took aid from both sides."),
              ("Being a member of NATO", "That would be alignment."),
          ], "Non-aligned states stayed outside the blocs and took aid from both.", "Non-alignment", "Concept", "It is about the blocs."),
        Q("Who was the first Prime Minister of the independent Congo?",
          "Patrice Lumumba", [
              ("Joseph Mobutu", "Mobutu was an army officer who took power in 1965."),
              ("Moise Tshombe", "Tshombe led the secession of Katanga."),
              ("Dag Hammarskjold", "He was UN Secretary-General."),
          ], "Lumumba became Prime Minister in June 1960.", "Congo crisis", "Recall", "Kasavubu was President."),
        Q("Which province tried to secede from the Congo in 1960?",
          "Katanga", [
              ("Leopoldville", "This was the capital region, which did not secede."),
              ("Equateur", "Equateur did not announce a secession in 1960."),
              ("Kivu", "Kivu was not the province that announced secession in July 1960."),
          ], "Katanga was rich in minerals.", "Katanga", "Recall", "It is the province of the copper mines."),
        Q("Which movement did the USSR and Cuba support in Angola in 1975?",
          "The MPLA", [
              ("The FNLA", "The FNLA received support from the USA and others."),
              ("UNITA", "UNITA received support from South Africa and the USA."),
              ("The PAIGC", "The PAIGC fought in Guinea-Bissau."),
          ], "The MPLA, led by Agostinho Neto, held Luanda.", "Angola 1975", "Recall", "Neto was its leader."),
        Q("Which statement best expresses a 'local causes first' reading of Africa's conflicts?",
          "Outside powers joined conflicts that already had local roots", [
              ("The Cold War was the only cause of every African war", "This ignores local causes."),
              ("African states were not involved in any conflict", "They were involved."),
              ("The Cold War had no effect on Africa", "This ignores the supply of arms and aid."),
          ], "Local grievances and borders were the starting points in this reading.", "Local and external causes", "Reasoning", "Which option places outside powers second?"),
        N("In which year was the Non-Aligned Movement formed at Belgrade?", 1961,
          "It was formed in 1961.", "Non-Aligned Movement", "Recall", "It is the year of the Berlin Wall."),
        Q("What can be said about the Cold War and the UPC conflict in Cameroun?",
          "French authorities presented the UPC as linked to communism and historians debate how far the Cold War explains the conflict", [
              ("The USSR governed French Cameroun", "France administered the territory."),
              ("The conflict had no local causes", "Local politics and grievances were important."),
              ("NATO fought in Cameroun in 1955", "No such force fought in Cameroun."),
          ], "Historians weigh the Cold War framing against local causes (check your textbook for evidence).", "Cold War and Cameroon", "Reasoning",
          "Look for the answer that includes a debate."),
    ]))

# ---------------------------------------------------------------- 17. UN Charter and Security Council
SETS.append(practice_set(
    module=M_CW, topic="The United Nations",
    title="The Charter, the Security Council and the veto", lesson="h7-un-charter-security-council-veto",
    questions=[
        Q("When was the UN Charter signed?",
          "26 June 1945", [
              ("24 October 1945", "This is the date it came into force."),
              ("10 December 1948", "That is the date of the Universal Declaration of Human Rights."),
              ("1 January 1946", "No such Charter date."),
          ], "The Charter was signed at San Francisco on 26 June 1945.", "UN Charter", "Recall", "It was signed before it came into force."),
        Q("Which of these is a permanent member of the Security Council?",
          "France", [
              ("Germany", "Germany is not a permanent member."),
              ("Brazil", "Brazil is not a permanent member."),
              ("Cameroon", "Cameroon has been an elected member at times, not a permanent one."),
          ], "The five permanent members are China, France, Russia, the UK and the USA.", "Permanent members", "Recall", "It administered Cameroun."),
        Q("What can a permanent member do with a veto?",
          "Block a substantive decision by voting against it", [
              ("Remove another permanent member", "The veto does not do this."),
              ("Overrule the General Assembly's debates", "The veto applies to Council decisions."),
              ("Change the Charter alone", "Charter changes need wide agreement."),
          ], "One negative vote from a permanent member blocks a substantive resolution.", "Veto", "Concept", "It works by voting against."),
        Q("How many affirmative votes does a substantive Security Council decision need today?",
          "Nine, with no veto", [
              ("Five", "Five is the number of permanent members."),
              ("Seven", "Seven of eleven was the rule before the Council was enlarged in 1966."),
              ("Fifteen", "Fifteen is the total membership."),
          ], "Nine of the fifteen members, including no negative vote of a permanent member.", "Voting", "Recall", "It is a majority of fifteen plus."),
        Q("What does Chapter VII of the Charter allow?",
          "Enforcement measures including sanctions and force", [
              ("Only debates in the Assembly", "Chapter VII concerns the Council's enforcement powers."),
              ("The creation of the ICJ", "The ICJ is set up under other provisions."),
              ("The admission of new members", "That is a different matter."),
          ], "Chapter VII applies to threats to peace, breaches of the peace and aggression.", "Chapter VII", "Concept", "It is about enforcement."),
        Q("What was the 'Uniting for Peace' resolution (1950) designed to do?",
          "Let the General Assembly recommend action when the Council is blocked by a veto", [
              ("Abolish the veto", "It did not abolish the veto."),
              ("Create a UN army", "It did not create an army."),
              ("End the Korean war", "It was a procedural measure."),
          ], "It is a way round a blocked Council, though the Assembly can only recommend.", "Uniting for Peace", "Concept", "It was adopted in the year of the Korean war."),
        N("How many members does the Security Council have today?", 15,
          "Five permanent and ten elected members make fifteen.", "Security Council", "Recall", "Add the permanent and elected members."),
        Q("Which argument for reform is often made about the Security Council?",
          "It reflects the world of 1945 and Africa has no permanent seat", [
              ("It has too many permanent members from Africa", "Africa has none."),
              ("It was created in 1990", "It was created in 1945."),
              ("It has no power to bind members", "Its decisions under Chapter VII bind members."),
          ], "Reform arguments stress the changed world and wider representation.", "Reform", "Reasoning", "Which argument mentions Africa?"),
    ]))

# ---------------------------------------------------------------- 18. Peacekeeping
SETS.append(practice_set(
    module=M_CW, topic="The United Nations",
    title="Peacekeeping in the Congo, the Balkans and Rwanda", lesson="h7-un-peacekeeping-congo-balkans-rwanda",
    questions=[
        Q("Which is a traditional principle of peacekeeping?",
          "Consent of the parties", [
              ("Use of force to defeat one party", "That is enforcement."),
              ("Control of the territory by the UN", "Peacekeepers do not take control."),
              ("Permanent occupation", "Missions are temporary."),
          ], "Consent, impartiality and minimal force are the traditional principles.", "Peacekeeping principles", "Recall", "It is about agreement."),
        Q("What was ONUC?",
          "The UN operation in the Congo, 1960 to 1964", [
              ("The UN force in Rwanda", "That was UNAMIR."),
              ("The UN force in Bosnia", "That was UNPROFOR."),
              ("The African Union's force in Darfur", "That was an AU mission."),
          ], "ONUC was the UN's Congo operation.", "ONUC", "Recall", "Its initials come from the French name."),
        Q("Which UN Secretary-General died in a plane crash in September 1961?",
          "Dag Hammarskjold", [
              ("Kofi Annan", "Annan served 1997 to 2006."),
              ("U Thant", "U Thant succeeded Hammarskjold."),
              ("Boutros Boutros-Ghali", "He served 1992 to 1996."),
          ], "The cause of the crash is still debated.", "Hammarskjold", "Recall", "He was on his way to talks about the Congo."),
        Q("Which town was a 'safe area' where more than eight thousand men and boys were killed in July 1995?",
          "Srebrenica", [
              ("Sarajevo", "Sarajevo was besieged but is not the place of this massacre."),
              ("Kigali", "Kigali is in Rwanda."),
              ("Katanga", "Katanga is in the Congo."),
          ], "Srebrenica was declared a safe area in 1993 and taken in July 1995.", "Srebrenica", "Recall", "It is in Bosnia."),
        Q("Who commanded UNAMIR in Rwanda?",
          "General Romeo Dallaire", [
              ("General Philippe Morillon", "Morillon served in Bosnia."),
              ("Lord Carrington", "Carrington was a diplomat linked to Rhodesia."),
              ("Dag Hammarskjold", "He was Secretary-General, not a commander."),
          ], "Dallaire asked for more troops and a wider mandate.", "UNAMIR", "Recall", "He later wrote about his experience."),
        Q("Which is a reason given for the UN's failure to prevent the killing in Rwanda?",
          "Members were unwilling to send troops and the mandate was limited", [
              ("The UN had no members", "The UN had many members."),
              ("The UN army was too large", "The UN has no army of its own."),
              ("There was no information", "Warnings existed."),
          ], "Political will and mandate are the main explanations.", "Rwanda", "Reasoning", "Which answer mentions members' decisions?"),
        N("How many years passed between the start of UNPROFOR in 1992 and the Srebrenica killings in 1995?", 3,
          "1995 minus 1992 is 3 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("Why should an essay distinguish the Secretariat, the Security Council and member states?",
          "Responsibility for decisions is shared among them", [
              ("They are the same body", "They are different bodies."),
              ("Only member states exist", "The Secretariat and Council are separate organs."),
              ("The UN is always blameless", "That is not an analysis."),
          ], "Accurate attribution of responsibility is a mark of a careful answer.", "Attributing responsibility", "Reasoning",
          "Think of who votes and who runs missions."),
    ]))

# ---------------------------------------------------------------- 19. Regional integration
SETS.append(practice_set(
    module=M_CW, topic="Regional integration",
    title="The OAU, the AU, ECOWAS, CEMAC and SADC", lesson="h7-reg-oau-au-ecowas-cemac-sadc",
    questions=[
        Q("When was the OAU founded?",
          "25 May 1963", [
              ("9 July 2002", "That is the launch of the AU."),
              ("28 May 1975", "That is the Treaty of Lagos creating ECOWAS."),
              ("1 January 1960", "That is Cameroun's independence."),
          ], "The OAU was founded in Addis Ababa in 1963.", "OAU", "Recall", "It was after 1960's wave of independence."),
        Q("Which principle limited OAU action on internal conflicts?",
          "Non-interference", [
              ("Sovereign inequality", "The OAU stressed sovereign equality."),
              ("Collective punishment", "No such principle."),
              ("Federalism", "The OAU was not a federation."),
          ], "Non-interference protected members' sovereignty.", "Non-interference", "Concept", "It is about keeping out."),
        Q("Where was the African Union launched in 2002?",
          "Durban", [
              ("Lome", "The Constitutive Act was adopted at Lome in 2000."),
              ("Addis Ababa", "The OAU was founded in Addis Ababa."),
              ("Lagos", "The Treaty of Lagos created ECOWAS."),
          ], "The AU was launched at Durban in July 2002.", "African Union", "Recall", "It is a South African port city."),
        Q("Which regional community has Cameroon as a member?",
          "CEMAC", [
              ("ECOWAS", "ECOWAS is in West Africa."),
              ("SADC", "SADC is in southern Africa."),
              ("The Arab Maghreb Union", "This is in North Africa."),
          ], "Cameroon belongs to CEMAC.", "CEMAC", "Recall", "It is in Central Africa."),
        Q("Why was SADC's predecessor, the SADCC (1980), created?",
          "To reduce the dependence of southern African states on apartheid South Africa", [
              ("To protect apartheid", "It aimed to reduce dependence."),
              ("To create a common army", "It aimed at economic cooperation."),
              ("To replace the OAU", "The OAU was not replaced until 2002."),
          ], "The frontline states sought economic independence.", "SADC", "Concept", "Which answer is about dependence?"),
        Q("Which is a difference between the AU and the OAU?",
          "The AU provides for intervention in grave circumstances", [
              ("The AU forbids all intervention", "The AU provides for intervention in grave cases."),
              ("The OAU had a Peace and Security Council", "That was created under the AU."),
              ("The AU was founded in 1963", "That is the OAU."),
          ], "The Constitutive Act includes a right of intervention in grave circumstances.", "OAU and AU", "Concept", "Which answer is about a new power?"),
        N("How many years passed between the foundation of the OAU (1963) and the launch of the AU (2002)?", 39,
          "2002 minus 1963 is 39 years.", "Chronology", "Calculation", "Subtract the earlier year from the later one."),
        Q("Which obstacle to integration is most relevant to CEMAC?",
          "Poor transport links and similar export economies", [
              ("Too much trade between members", "Trade between members is low."),
              ("A lack of any shared currency", "CEMAC has a shared currency."),
              ("The absence of any treaty", "A treaty exists."),
          ], "Infrastructure and similar economies limit trade.", "Obstacles to integration", "Reasoning", "Which obstacle limits trade?"),
    ]))

# ---------------------------------------------------------------- 20. Exam lesson
SETS.append(practice_set(
    module=M_EX, topic="Practice paper",
    title="Approaching the History practice paper", lesson="h7-exam-approaching-practice-paper",
    questions=[
        Q("What is the FIRST step of the multiple-choice routine?",
          "Read the stem and underline key words", [
              ("Pick the longest option", "Length is not a reason."),
              ("Look at the last option first", "The routine starts with the stem."),
              ("Skip the question", "Skipping is for time-saving, after a first read."),
          ], "Read the stem, predict, remove, then check.", "Multiple-choice routine", "Recall", "It starts with reading."),
        Q("What does 'provenance' mean in source work?",
          "Who produced the source, when and why", [
              ("What the source says", "That is its content."),
              ("How many pages it has", "Length is not provenance."),
              ("Whether you like it", "Opinion is not provenance."),
          ], "Provenance covers author, date and purpose.", "Provenance", "Recall", "It is about origin."),
        Q("A question stem says 'Which was NOT a cause'. What should you do?",
          "Look for the one option that is not a cause", [
              ("Choose the first cause you recognise", "You need the exception."),
              ("Choose the longest option", "Length is not a clue."),
              ("Ignore the word NOT", "Ignoring NOT changes the question."),
          ], "Read the stem carefully for words such as NOT, EXCEPT and MAIN.", "Reading the stem", "Application", "The key word changes the task."),
        Q("In the PEC routine, what does the 'C' stand for?",
          "Cross-check with other sources", [
              ("Copy from the source", "Copying is not evaluation."),
              ("Conclude without evidence", "Conclusions need evidence."),
              ("Count the words", "Word count is not the point."),
          ], "PEC stands for provenance, evidence and cross-check.", "PEC routine", "Recall", "It is about comparing."),
        Q("For a 40-question, 90-minute practice paper, what is a sensible KKEVO plan?",
          "About two minutes a question and about ten minutes to check", [
              ("Ten minutes a question", "That would not finish the paper."),
              ("Answer the first ten and leave the rest", "Leaving questions blank wastes marks."),
              ("Check each answer for ten minutes", "Checking should be brief."),
          ], "Mark hard questions and return to them.", "Time planning", "Application", "Divide the time by the number of questions."),
        Q("Why does the practice paper not mark essays?",
          "Essays cannot be marked automatically, so write and check them with a teacher", [
              ("Essays are not part of History", "Essays are an important skill."),
              ("The paper is only for teachers", "It is for students."),
              ("Essays are always optional", "Check the real format with your teacher."),
          ], "Use the model answer plans and ask a teacher to review your writing.", "Essay practice", "Reasoning", "What is missing from an automatic check?"),
        N("About how many minutes per question (rounded down to a whole number) does a 90-minute, 40-question paper give?", 2,
          "90 divided by 40 is 2.25, so about 2 minutes a question.", "Time planning", "Calculation", "Divide 90 by 40."),
        Q("What should you do first with the score by topic after the mock?",
          "Revise the weakest topic using its lessons and practice sets", [
              ("Ignore the lowest topic", "The lowest topic needs most attention."),
              ("Retake the mock at once without revising", "Revision should come first."),
              ("Only revise your best topic", "That gives the least gain."),
          ], "Use the results to plan revision.", "Using results", "Application", "Think about where you can gain most."),
    ]))

# ---------------------------------------------------------------- Mock: practice paper
_n[0] = 0  # the 40 mock questions are all MC, so the correct option cycles A-D exactly ten times each

T1 = "Trusteeship and decolonization"
T2 = "Southern Cameroons politics"
T3 = "The post-colonial state"
T4 = "Constitutional transfers"
T5 = "Armed liberation"
T6 = "South Africa"
T7 = "Cold War geopolitics"
T8 = "The United Nations"
T9 = "Regional integration"

MOCK_QUESTIONS = [
    # ---- Trusteeship and decolonization (5)
    Q("Which article of the UN Charter sets out the basic objectives of trusteeship, including progress towards self-government or independence?",
      "Article 76", [
          ("Article 2", "Article 2 lists principles of the Organisation, such as refraining from the use of force."),
          ("Article 51", "Article 51 concerns the right of self-defence."),
          ("Article 99", "Article 99 allows the Secretary-General to bring matters to the Council."),
      ], "Article 76 sets the objectives of trusteeship.", T1, "Recall", "It is in the chapter on the international trusteeship system."),
    Q("Why did the UPC take its case to the UN?",
      "Cameroun was a trust territory with a Charter promise of progress towards self-government or independence", [
          ("The UN governed Cameroun directly", "France administered under UN supervision."),
          ("France had left Cameroun in 1948", "France administered until 1960."),
          ("The UN had banned the UPC", "The UPC was banned by the French administration in 1955."),
      ], "Trusteeship gave petitioners a legal standing outside the colonial administration.", T1, "Concept", "Think of what trusteeship offered."),
    Q("Who replaced Andre-Marie Mbida as head of government in February 1958?",
      "Ahmadou Ahidjo", [
          ("Ruben Um Nyobe", "Um Nyobe led the banned UPC."),
          ("Ernest Ouandie", "Ouandie was a UPC leader."),
          ("Paul Biya", "Biya became President in 1982."),
      ], "Ahidjo became Prime Minister in February 1958.", T1, "Recall", "He was Mbida's deputy."),
    Q("An invented report from a French officer says 'order has returned and the people welcome the troops'. What is its main limit as evidence?",
      "It was written by one side to a superior and gives no independent voices", [
          ("It is too short to read", "Length is not the issue."),
          ("It was written by the UN", "It was written by an officer."),
          ("It proves that no violence occurred", "A claim of order does not prove the absence of violence."),
      ], "Provenance and purpose limit the value of the report.", T1, "Interpretation", "Ask who wrote it and why."),
    Q("Which statement about casualties in the conflict is the safest to write?",
      "Estimates differ widely and the exact number is not known", [
          ("Exactly 100,000 people died", "No exact figure is established."),
          ("No civilians were affected", "Civilians were affected in the conflict."),
          ("The fighting ended on 1 January 1960", "Fighting continued after independence."),
      ], "Good history states uncertainty.", T1, "Reasoning", "Which sentence avoids false precision?"),
    # ---- Southern Cameroons politics (5)
    Q("Where did the Southern Cameroons House of Assembly meet after 1954?",
      "Buea", [
          ("Enugu", "Enugu was the Eastern Region capital."),
          ("Foumban", "Foumban hosted the conference of 1961."),
          ("Lagos", "Lagos was the federal capital of Nigeria."),
      ], "The House met at Buea.", T2, "Recall", "It lies at the foot of Mount Cameroon."),
    Q("Which party was led by John Ngu Foncha?",
      "KNDP", [
          ("KNC", "The KNC was led by Endeley."),
          ("One Kamerun", "One Kamerun was led by Ntumazah."),
          ("UPC", "The UPC was based in French Cameroun."),
      ], "Foncha founded the KNDP in 1955.", T2, "Recall", "He left the KNC to found it."),
    Q("Which two options were on the 1961 Southern Cameroons ballot?",
      "Joining Nigeria or joining the Republic of Cameroun", [
          ("Independence alone or joining Nigeria", "Independence alone was not offered."),
          ("Joining Gabon or joining Chad", "These were not options."),
          ("Staying under British rule or joining Cameroun", "Continued trusteeship was not an option."),
      ], "The UN set two options after the Mamfe deadlock.", T2, "Recall", "Both options were forms of union."),
    Q("What was decided at the Foumban conference of July 1961?",
      "The form of a federal union, leading to the Federal Republic of 1 October 1961", [
          ("The date of Cameroun's independence", "Cameroun was independent from 1 January 1960."),
          ("The result of the plebiscite", "The plebiscite was held in February 1961."),
          ("The abolition of the federation", "The federation was abolished in 1972."),
      ], "Foumban discussed the federal constitution.", T2, "Concept", "Think of what followed on 1 October 1961."),
    Q("An invented memoir written long after 1961 says the text at Foumban 'was already prepared'. How should a historian treat it?",
      "As one voice to be cross-checked, noting that memory and later events may shape it", [
          ("As a perfect record of the talks", "Memoirs are shaped by memory."),
          ("As worthless because it is a memoir", "Memoirs can offer valuable detail when checked."),
          ("As the official text of the constitution", "A memoir is not an official text."),
      ], "Cross-checking is the standard method.", T2, "Interpretation", "What should you do with a single account?"),
    # ---- The post-colonial state (5)
    Q("What did the referendum of 20 May 1972 create?",
      "The United Republic of Cameroon, a unitary state", [
          ("The Federal Republic of Cameroon", "That was created in 1961."),
          ("The Republic of Cameroon", "That name was adopted in 1984."),
          ("The CPDM", "The CPDM came in 1985."),
      ], "The referendum ended the federation.", T3, "Recall", "Look at the name."),
    Q("Which of these was an external cause of the political opening of 1990?",
      "The end of the Cold War and pressure from donors", [
          ("The villes mortes campaigns", "They were organised inside the country."),
          ("The launch of the SDF", "The SDF was a Cameroonian party."),
          ("The tripartite meeting", "It was a domestic meeting."),
      ], "External causes come from outside the country.", T3, "Concept", "Which cause is international?"),
    Q("What does a 'decentralized unitary state' mean?",
      "The central government keeps sovereignty but delegates powers to regions", [
          ("Sovereignty is divided between a centre and federated states", "That describes a federation."),
          ("There is no central government", "A unitary state has a central government."),
          ("Several independent states share a currency", "That is not a unitary state."),
      ], "A unitary state keeps sovereignty at the centre.", T3, "Concept", "Compare it with a federation."),
    Q("Which sentence is an interpretation, not a description?",
      "The 1972 referendum shows that all citizens accepted a unitary state", [
          ("The referendum was held on 20 May 1972", "This is a checkable date."),
          ("The 1996 constitution provides for regions", "This is a checkable fact about the text."),
          ("The CNU became the CPDM in 1985", "This is a checkable fact."),
      ], "An interpretation needs evidence and can be challenged.", T3, "Reasoning", "Which sentence could be argued against?"),
    Q("An invented official speech says 'one nation must have one state'. What does it show a historian?",
      "How the change to a unitary state was justified, not how people felt", [
          ("The exact opinion of each voter", "A speech cannot show this."),
          ("That the referendum was unfair", "A speech does not prove unfairness."),
          ("The text of the 1961 constitution", "A speech is not the text."),
      ], "A speech gives reasons and purpose.", T3, "Interpretation", "What is a speech for?"),
    # ---- Constitutional transfers (4)
    Q("Which leader founded the Convention People's Party in 1949?",
      "Kwame Nkrumah", [
          ("Nnamdi Azikiwe", "Azikiwe led the NCNC in Nigeria."),
          ("Jomo Kenyatta", "Kenyatta led Kenya's KAU."),
          ("Sekou Toure", "Toure led Guinea."),
      ], "Nkrumah founded the CPP.", T4, "Recall", "Ghana's first leader."),
    Q("Why did Nigeria adopt a federal constitution?",
      "Regional differences and fears of domination by one region", [
          ("It had one region only", "Nigeria had three main regions."),
          ("The Soviet Union required it", "The USSR had no such role."),
          ("Ghana had a federal system", "Ghana was unitary."),
      ], "Federation fitted Nigeria's regional structure.", T4, "Concept", "Think of the three regions."),
    Q("What was the result of the referendum of 28 September 1958 in Guinea?",
      "A No vote, followed by immediate independence", [
          ("A Yes vote and membership of the Community", "That was the choice of the other territories."),
          ("A postponed vote", "Guinea voted on the day."),
          ("A vote for union with Ghana", "No such option was on the ballot."),
      ], "Guinea voted No and became independent on 2 October 1958.", T4, "Recall", "Its leader was Sekou Toure."),
    Q("Which statement best compares British and French methods in West Africa?",
      "Britain used step-by-step constitutions; France used the Loi-Cadre and the 1958 referendum before independence by agreement in 1960", [
          ("Both fought long wars of liberation", "Neither did in West Africa."),
          ("Britain held a referendum in 1958; France held none", "The 1958 referendum was a French one."),
          ("France gave independence in 1947", "French territories became independent mainly in 1960."),
      ], "The two approaches differed but both avoided war in West Africa.", T4, "Reasoning", "Choose the answer with both sides."),
    # ---- Armed liberation (4)
    Q("Which agreement ended the Algerian war in 1962?",
      "The Evian Accords", [
          ("The Lancaster House Agreement", "That was about Kenya and Zimbabwe."),
          ("The Arusha Accords", "That concerned Rwanda."),
          ("The Dayton Agreement", "That concerned Bosnia."),
      ], "The Evian Accords were signed in March 1962.", T5, "Recall", "It is named after a French town."),
    Q("What did Britain declare in Kenya in October 1952?",
      "A State of Emergency", [
          ("Independence", "Kenya became independent in 1963."),
          ("A federation", "No federation was created."),
          ("A plebiscite", "No plebiscite was held."),
      ], "The Emergency was a response to Mau Mau.", T5, "Recall", "It allowed detention."),
    Q("Which event of April 1974 changed the situation in the Portuguese colonies?",
      "An officers' coup in Lisbon", [
          ("The independence of Ghana", "That was in 1957."),
          ("The Evian Accords", "That was in 1962."),
          ("The Lancaster House conference", "That was in 1979."),
      ], "The Carnation Revolution led to the end of the colonial wars.", T5, "Recall", "It took place in Portugal."),
    Q("What was UDI in Rhodesia?",
      "A Unilateral Declaration of Independence by the white minority government in 1965", [
          ("A UN peace plan of 1979", "The settlement of 1979 was reached at Lancaster House."),
          ("A union with Mozambique", "No such union existed."),
          ("The name of the guerrilla army", "UDI was a declaration, not an army."),
      ], "UDI was declared in November 1965.", T5, "Recall", "It was a declaration."),
    # ---- South Africa (4)
    Q("Which law classified every South African by race?",
      "The Population Registration Act of 1950", [
          ("The Bantu Education Act", "It governed schooling."),
          ("The Group Areas Act", "It set residential areas."),
          ("The Freedom Charter", "It was a statement of demands, not a law."),
      ], "The Act set the categories on which other laws relied.", T6, "Recall", "Registration lists people."),
    Q("What happened at Sharpeville on 21 March 1960?",
      "Police killed protesters in a pass-law protest, and the ANC and PAC were banned afterwards", [
          ("Mandela was released", "He was released in 1990."),
          ("The first all-race election was held", "That was in 1994."),
          ("The Freedom Charter was adopted", "That was in 1955."),
      ], "Sharpeville led to bans and a turn to armed struggle.", T6, "Recall", "It was a turning point."),
    Q("Which of these is an example of INTERNAL pressure on the apartheid government in the 1980s?",
      "The United Democratic Front and trade union action", [
          ("The UN arms embargo of 1977", "This was an external measure."),
          ("Sanctions imposed by other countries", "These were external."),
          ("The end of the Berlin blockade", "This was a Cold War event of 1949."),
      ], "The UDF and unions mobilised inside South Africa.", T6, "Concept", "Which pressure came from within?"),
    Q("An invented eyewitness recalled the 1976 protests many years later. What is the main limit of that account?",
      "It depends on memory and one viewpoint", [
          ("It was written by the police on the day", "It was a later recollection."),
          ("It is a government statistic", "It is personal testimony."),
          ("It is the text of a law", "It is not a legal text."),
      ], "Eyewitness accounts show experience but need cross-checking.", T6, "Interpretation", "Check when it was written."),
    # ---- Cold War geopolitics (5)
    Q("What did the Truman Doctrine of March 1947 promise?",
      "Support for free peoples resisting pressure, beginning with aid to Greece and Turkey", [
          ("The creation of NATO", "NATO was created in 1949."),
          ("Aid to rebuild Western Europe", "That describes the Marshall Plan."),
          ("A Soviet plan for Eastern Europe", "The Truman Doctrine was an American policy."),
      ], "The Doctrine began American containment.", T7, "Recall", "It is named after a President."),
    Q("Which pair of dates is correct?",
      "NATO 1949, Warsaw Pact 1955", [
          ("NATO 1955, Warsaw Pact 1949", "The dates are reversed."),
          ("NATO 1947, Warsaw Pact 1949", "Both dates are wrong."),
          ("NATO 1961, Warsaw Pact 1962", "These are the dates of other events."),
      ], "NATO was formed in April 1949 and the Warsaw Pact in May 1955.", T7, "Recall", "The Pact came after West Germany joined NATO."),
    Q("What was the main aim of non-alignment?",
      "Staying outside the two military blocs", [
          ("Joining the stronger bloc", "That is alignment."),
          ("Refusing all aid", "Many non-aligned states accepted aid from both blocs."),
          ("Creating a world government", "That was not the aim."),
      ], "The Non-Aligned Movement was formed at Belgrade in 1961.", T7, "Concept", "It is about the blocs."),
    Q("Why did the Congo crisis of 1960 become part of the Cold War?",
      "A local crisis drew in Belgium, the UN and the superpowers, who feared losing influence", [
          ("The Congo was a NATO member", "It was not."),
          ("The Congo was a Soviet republic", "It was an independent state."),
          ("The crisis had no outside involvement", "Outside powers were deeply involved."),
      ], "The crisis began locally, but superpower fears shaped it.", T7, "Reasoning", "Which answer mentions both local and outside factors?"),
    Q("Which school of historians says American economic power provoked Soviet fears?",
      "Revisionist", [
          ("Orthodox", "Orthodox historians blame Soviet expansion."),
          ("Post-revisionist", "Post-revisionists stress mutual misperceptions."),
          ("Nationalist", "This is not one of the Cold War schools discussed in the lesson."),
      ], "Revisionists stress American aims and power.", T7, "Concept", "It challenges the traditional view."),
    # ---- The United Nations (4)
    Q("How many members does the Security Council have?",
      "Fifteen", [
          ("Five", "That is the number of permanent members."),
          ("Eleven", "That was the number before 1966."),
          ("Fifty-one", "That was the number of original UN members."),
      ], "Five permanent and ten elected members.", T8, "Recall", "Add the two groups."),
    Q("What is the effect of a veto by a permanent member?",
      "It blocks a substantive decision of the Council", [
          ("It removes the member from the Council", "A veto does not remove anyone."),
          ("It is overruled by the Assembly's vote", "The Assembly cannot overrule the Council's decisions in this way."),
          ("It has no effect if nine members vote yes", "A veto blocks the decision even if nine vote yes."),
      ], "One negative vote blocks a substantive resolution.", T8, "Concept", "Think of what a veto stops."),
    Q("Which statement about the Rwanda mission is accurate?",
      "UNAMIR was a small mission with a limited mandate which was reduced in April 1994", [
          ("UNAMIR was a large force that won the war", "It was a small force."),
          ("UNAMIR was commanded by Dag Hammarskjold", "Dallaire commanded it."),
          ("UNAMIR was created in 1960", "It was created in 1993."),
      ], "The Council reduced UNAMIR during the genocide.", T8, "Recall", "Think of the year 1994."),
    Q("Which peacekeeping principle separates peacekeeping from enforcement?",
      "Consent of the parties", [
          ("Use of force to defeat a party", "That is enforcement."),
          ("Occupation of the territory", "That is not peacekeeping."),
          ("Permanent presence", "Missions are temporary."),
      ], "Peacekeeping rests on consent, impartiality and minimal force.", T8, "Concept", "It begins with agreement."),
    # ---- Regional integration (4)
    Q("Which organisation was launched at Durban in 2002?",
      "The African Union", [
          ("The OAU", "The OAU was founded in 1963."),
          ("ECOWAS", "ECOWAS was created in 1975."),
          ("SADC", "SADC's treaty is of 1992."),
      ], "The AU replaced the OAU.", T9, "Recall", "It replaced the OAU."),
    Q("Which principle of the OAU Charter limited intervention in members' internal affairs?",
      "Non-interference", [
          ("Pan-Africanism", "It was a broad idea of unity."),
          ("Collective security", "The OAU had weak collective security arrangements."),
          ("Free movement", "That is a regional community aim."),
      ], "Non-interference protected sovereignty.", T9, "Concept", "It means staying out of others' affairs."),
    Q("Which of these is a member of CEMAC?",
      "Cameroon", [
          ("Nigeria", "Nigeria is a member of ECOWAS."),
          ("South Africa", "South Africa is a member of SADC."),
          ("Kenya", "Kenya belongs to the East African Community."),
      ], "CEMAC has six members, including Cameroon.", T9, "Recall", "It is in Central Africa."),
    Q("Which obstacle to economic integration in Africa is most commonly cited?",
      "Poor transport links and similar export economies that do not trade with each other", [
          ("Too many trade routes between all members", "Links are generally poor."),
          ("A single currency for all of Africa", "No such currency exists."),
          ("The absence of any regional bodies", "Several regional bodies exist."),
      ], "Infrastructure and similar economies limit trade.", T9, "Reasoning", "Which obstacle limits trade?"),
]

assert len(MOCK_QUESTIONS) == 40

SETS.append(practice_set(
    module=M_EX, topic="Practice paper",
    title="Practice paper: multiple choice across all topics", lesson="h7-exam-approaching-practice-paper",
    mock=True, time_limit_minutes=90, questions=MOCK_QUESTIONS))
