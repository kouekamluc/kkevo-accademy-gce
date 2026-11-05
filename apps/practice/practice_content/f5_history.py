"""Practice sets for GCE O Level History, Form 5 (draft: check every fact against the lessons and textbooks)."""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

M_TRUST = "Trusteeship & Nationalism in Cameroon (1945–1961)"
M_POST = "Post-Independence Cameroon"
M_WORLD = "World History since 1870"

SETS = []

# ---------------------------------------------------------------------------
# 1. French Cameroun
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_TRUST, topic="French Cameroun",
    title="Nationalism and independence in French Cameroun", lesson="nationalism-in-french-cameroun",
    questions=[
        MC("When and where was the UPC founded?", [
            C("In Kumba in 1957", why="UPC leaders fled to Kumba after the 1955 ban and were expelled in 1957."),
            C("In Yaoundé in July 1955", why="July 1955 is when France banned the UPC, not when it was founded."),
            C("In Douala on 10 April 1948", correct=True),
            C("In Douala in September 1945", why="September 1945 was the date of strikes and riots in Douala, before the UPC existed."),
        ], steps=[S("Recall the founding", text="The UPC was founded in Douala on 10 April 1948, with Ruben Um Nyobè as Secretary-General.")],
           concept="Foundation of the UPC", skill="Recall",
           hint="The party was founded a few years after the Douala strikes, in the same city."),
        MC("Which of these was NOT one of the main demands of the UPC?", [
            C("Gradual change in close partnership with France", correct=True),
            C("Better living standards for Africans", why="This was one of the UPC's three main demands."),
            C("Reunification of French and British Cameroons", why="This was one of the UPC's three main demands."),
            C("A fixed date for independence", why="This was one of the UPC's three main demands."),
        ], steps=[S("List the UPC's demands", text="Reunification, a fixed date for independence and better living standards."),
                  S("Identify the odd one out", text="Gradual change in partnership with France was the position of the BDC, a rival party.")],
           concept="Aims of the UPC", skill="Concept",
           hint="One option describes the policy of a party the French administration favoured."),
        MC("Who founded the Bloc Démocratique Camerounais (BDC) in 1951?", [
            C("Ruben Um Nyobè", why="Um Nyobè was Secretary-General of the UPC, which the BDC opposed."),
            C("André-Marie Mbida", why="Mbida became the first Prime Minister in 1957; he did not found the BDC."),
            C("Ahmadou Ahidjo", why="Ahidjo led the Union Camerounaise, a different party."),
            C("Dr Louis-Paul Aujoulat", correct=True),
        ], steps=[S("Recall the rival parties", text="ESOCAM (1949) and the BDC (1951, Dr Louis-Paul Aujoulat) were favoured by the French against the UPC.")],
           concept="Rival parties: ESOCAM and BDC", skill="Recall",
           hint="The BDC preferred close partnership with France; think of its founder, a doctor."),
        MC("What event came immediately before the French ban on the UPC in July 1955?", [
            C("Um Nyobè was killed in the Sanaga-Maritime", why="Um Nyobè was killed in September 1958, three years after the ban."),
            C("Riots broke out in several towns, including Douala and Yaoundé", correct=True),
            C("Cameroun gained full internal autonomy", why="Internal autonomy came on 1 January 1959."),
            C("The Loi-Cadre gave universal suffrage", why="The Loi-Cadre was passed in June 1956, after the ban."),
        ], steps=[S("Order the events", text="May 1955: riots in several towns, many killed. July 1955: France banned the UPC by decree.")],
           concept="The 1955 ban on the UPC", skill="Reasoning",
           hint="Look for the event in May 1955 that France blamed on the party."),
        MC("What was the maquis?", [
            C("A trade union federation founded in 1944", why="That describes the USCC, the trade union body."),
            C("A party formed by moderates to oppose the UPC", why="That describes ESOCAM or the BDC."),
            C("A French reform law of 1956", why="That was the Loi-Cadre (Defferre framework law)."),
            C("The armed underground resistance of UPC fighters after the ban", correct=True),
        ], steps=[S("Definition", text="The maquis was the armed underground resistance of UPC fighters in the forests of the Sanaga-Maritime and the Bamileke region after the party was banned.")],
           concept="The maquis", skill="Concept",
           hint="Think of what some UPC members did after their party was made illegal."),
        MC("Which statement about the fates of UPC leaders is correct?", [
            C("Um Nyobè died in Geneva in 1960 after being poisoned", why="This was Moumié's fate; Um Nyobè was killed in the Sanaga-Maritime in 1958."),
            C("Ouandié was killed by French-led troops in 1958", why="This was Um Nyobè's fate; Ouandié was executed in 1971."),
            C("Um Nyobè was killed by French-led troops on 13 September 1958", correct=True),
            C("Moumié was executed in Bafoussam in 1971", why="This was Ouandié's fate; Moumié died in Geneva in November 1960."),
        ], steps=[S("Match leader and fate", text="Um Nyobè: killed in the Sanaga-Maritime, 13 September 1958. Moumié: died in Geneva, November 1960. Ouandié: executed in Bafoussam, January 1971.")],
           concept="Fates of the UPC leaders", skill="Recall",
           hint="Learn one place and one year for each of the three leaders."),
        MC("What happened in French Cameroun on 1 January 1959?", [
            C("Full internal autonomy", correct=True),
            C("Mbida became the first Prime Minister", why="Mbida became Prime Minister in 1957."),
            C("The UN voted to end trusteeship", why="The UN General Assembly decided this in March 1959."),
            C("Independence", why="Independence came a year later, on 1 January 1960."),
        ], steps=[S("Separate the two 1 January dates", text="1 January 1959 was full internal autonomy; 1 January 1960 was independence.")],
           concept="Steps to independence", skill="Recall",
           hint="Two important steps both fell on 1 January in consecutive years."),
        MC("Why could the UPC not take part in the elections of December 1956?", [
            C("Its leaders were all in prison in France", why="The leaders were in exile in Kumba and later Cairo, Conakry and Accra, not prison in France."),
            C("It was still banned", correct=True),
            C("The UN had forbidden it", why="The ban was a French government decree, not a UN decision."),
            C("It had merged with the Union Camerounaise", why="The UPC never joined Ahidjo's party; it was a rival."),
        ], steps=[S("Link the events", text="The UPC was banned in July 1955 and was still banned when the Loi-Cadre elections were held in December 1956."),
                  S("Consequence", text="Moderate parties gained power, and Mbida and then Ahidjo led the government towards independence.")],
           concept="Consequences of the 1955 ban", skill="Reasoning",
           hint="Think about the party's legal status after July 1955."),
    ]))

# ---------------------------------------------------------------------------
# 2. British Southern Cameroons
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_TRUST, topic="British Southern Cameroons",
    title="Southern Cameroons: from the 1953 crisis to reunification",
    lesson="british-southern-cameroons-to-reunification",
    questions=[
        MC("Before 1954, Southern Cameroons was administered as part of which Nigerian region?", [
            C("None: it had its own House of Assembly in Buea", why="The Buea House of Assembly came only with the 1954 constitution."),
            C("The Northern Region", why="Northern Cameroons voted to join Nigeria in 1961, but Southern Cameroons was attached to the Eastern Region."),
            C("The Eastern Region, with its capital at Enugu", correct=True),
            C("The Western Region", why="Southern Cameroons was never part of the Western Region."),
        ], steps=[S("Recall the arrangement", text="Britain governed the trust territory as part of Nigeria; the southern part was attached to the Eastern Region, capital Enugu.")],
           concept="Southern Cameroons under Nigeria", skill="Recall",
           hint="Think of the city where Southern Cameroons members sat before the 1953 crisis."),
        MC("During the 1953 crisis in the Eastern House of Assembly, Endeley's group declared benevolent neutrality. What did this mean?", [
            C("They refused to take sides in the NCNC split", correct=True),
            C("They joined the UPC", why="The UPC was a French Cameroun party; Endeley's group stayed in Southern Cameroons politics."),
            C("They fully supported the NCNC leadership", why="Supporting one side is the opposite of neutrality."),
            C("They demanded immediate reunification with French Cameroun", why="The crisis was about the NCNC split; reunification was not their demand at that moment."),
        ], steps=[S("Context", text="In 1953 a crisis split the ruling NCNC in the Eastern House at Enugu."),
                  S("Meaning", text="The Southern Cameroons members, led by Endeley, refused to take sides and later walked out.")],
           concept="1953 Eastern House of Assembly crisis", skill="Concept",
           hint="Neutral means not choosing either side of a quarrel."),
        MC("What was the main result of the 1953 crisis for Southern Cameroons?", [
            C("It became independent immediately", why="Southern Cameroons gained independence only by joining Cameroun in 1961."),
            C("It was transferred to Northern Nigeria", why="It was separated from the Eastern Region, not attached to the north."),
            C("The UN organised a plebiscite in 1954", why="The plebiscite was held on 11 February 1961."),
            C("The 1954 constitution gave it its own House of Assembly in Buea", correct=True),
        ], steps=[S("Consequence", text="Britain agreed at constitutional talks in 1953. Under the 1954 constitution Southern Cameroons became a quasi-federal territory with a House of Assembly in Buea, and Endeley became Leader of Government Business.")],
           concept="1953 Eastern House of Assembly crisis", skill="Reasoning",
           hint="The crisis convinced members that they needed their own government."),
        MC("Which party and leader are correctly matched?", [
            C("KNDP: Emmanuel Endeley", why="Endeley led the KNC; the KNDP was Foncha's party."),
            C("One Kamerun (OK): Ndeh Ntumazah", correct=True),
            C("KPP: Augustine Ngom Jua", why="The KPP was P. M. Kale's party; Jua was a leading KNDP figure."),
            C("KNC: John Ngu Foncha", why="Foncha left the KNC and founded the KNDP in 1955; Endeley led the KNC."),
        ], steps=[S("Match parties and leaders", text="KNC: Endeley (1953). KNDP: Foncha (1955). OK: Ndeh Ntumazah (1957). KPP: P. M. Kale.")],
           concept="Parties and leaders in Southern Cameroons", skill="Recall",
           hint="One of these parties was close to the banned UPC."),
        MC("How did the aims of the KNC and the KNDP differ?", [
            C("Both wanted Southern Cameroons to become a separate independent state", why="This was not the policy of either; the plebiscite did not even offer separate independence."),
            C("The KNC wanted French rule; the KNDP wanted British rule", why="Neither party had these aims; both wanted self-government and an end to rule from Enugu."),
            C("The KNC wanted reunification; the KNDP wanted to stay with Nigeria", why="This reverses the two parties' positions."),
            C("The KNC came to favour close links with Nigeria; the KNDP wanted separation from Nigeria and reunification", correct=True),
        ], steps=[S("KNC", text="Led by Endeley; talked of reunification at first but came to favour close links with Nigeria."),
                  S("KNDP", text="Founded by Foncha in 1955; wanted separation from Nigeria and, in time, reunification.")],
           concept="KNC versus KNDP", skill="Concept",
           hint="Remember: KNC = Endeley, KNDP = Foncha. Which way did each leader lean?"),
        MC("What options did voters in Southern Cameroons have in the plebiscite of 11 February 1961?", [
            C("A federation or a unitary state", why="This was the question in Cameroon's referendum of 20 May 1972."),
            C("Separate independence or joining Nigeria", why="There was no option of separate independence."),
            C("Joining Nigeria or joining the Republic of Cameroun", correct=True),
            C("Remaining under British rule or independence", why="Continued British rule was not offered; both options meant independence by joining a neighbour."),
        ], steps=[S("Recall the options", text="Voters could only achieve independence by joining Nigeria or by joining the Republic of Cameroun.")],
           concept="The 1961 plebiscite", skill="Recall",
           hint="Both options involved joining an already independent neighbour."),
        MC("What was the result of the 1961 plebiscite in Northern Cameroons?", [
            C("It voted to join Nigeria and became part of Nigeria on 1 June 1961", correct=True),
            C("The vote was cancelled after Cameroun protested", why="Cameroun protested about the northern result, but without success."),
            C("It voted to join Cameroun and joined on 1 October 1961", why="That describes the southern result; the north voted for Nigeria."),
            C("It voted for separate independence", why="Separate independence was not an option."),
        ], steps=[S("Compare north and south", text="Southern Cameroons voted to join Cameroun; Northern Cameroons voted to join Nigeria and became part of it on 1 June 1961.")],
           concept="The 1961 plebiscite", skill="Recall",
           hint="The north and the south did not vote the same way."),
        MC("Some Anglophone critics question the way reunification was achieved in 1961. Which point do they raise?", [
            C("The plebiscite in the south was won by a very narrow margin", why="The south voted clearly, by a large majority, to join Cameroun."),
            C("There was no independence option, the Foumban talks were short, and the two sides were unequal", correct=True),
            C("Reunification took place without any vote", why="A UN plebiscite was held on 11 February 1961."),
            C("The Foumban Conference created a unitary state", why="Foumban agreed on a federation of two states; the unitary state came in 1972."),
        ], steps=[S("One view", text="Many saw reunification as the fulfilment of the nationalist dream, freely chosen by a clear majority."),
                  S("Critical view", text="Critics point to the lack of an independence option, the short Foumban talks and the unequal strength of the two sides, which left weak guarantees.")],
           concept="Differing views of reunification", skill="Interpretation",
           hint="Think about the plebiscite options and the conditions of the Foumban talks."),
    ]))

# ---------------------------------------------------------------------------
# 3. Federal to unitary state
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_POST, topic="Federal to unitary state",
    title="From the Federal Republic to the United Republic", lesson="federal-to-unitary-state",
    questions=[
        MC("What were the two federated states of the Federal Republic of Cameroon and their capitals?", [
            C("East Cameroon (Yaoundé) and West Cameroon (Enugu)", why="Enugu was the capital of Nigeria's Eastern Region, not of West Cameroon."),
            C("East Cameroon (Douala) and West Cameroon (Bamenda)", why="The capitals were Yaoundé and Buea, not Douala and Bamenda."),
            C("East Cameroon (Yaoundé) and West Cameroon (Buea)", correct=True),
            C("North Cameroon (Garoua) and South Cameroon (Yaoundé)", why="The two states were East and West Cameroon."),
        ], steps=[S("Recall the structure", text="East Cameroon had its capital at Yaoundé, which was also the federal capital; West Cameroon had its capital at Buea.")],
           concept="Structure of the Federal Republic", skill="Recall",
           hint="West Cameroon's capital was where the Southern Cameroons House of Assembly had sat since 1954."),
        MC("Which list gives the Prime Ministers of West Cameroon in the correct order?", [
            C("Foncha, Jua, Muna", correct=True),
            C("Endeley, Foncha, Jua", why="Endeley was replaced by Foncha as Premier in 1959, before the federation existed."),
            C("Jua, Foncha, Muna", why="Foncha came first (1961–1965), then Jua."),
            C("Foncha, Muna, Jua", why="Muna was the last Prime Minister (1968–1972), after Jua."),
        ], steps=[S("Order", text="Foncha (1961–1965), Augustine Ngom Jua (1965–1968), Solomon Tandeng Muna (1968–1972).")],
           concept="Prime Ministers of West Cameroon", skill="Recall",
           hint="The first one was also federal Vice-President in 1961."),
        MC("Why was Ahidjo's appointment of Muna as Prime Minister of West Cameroon in 1968 significant?", [
            C("It ended the federation", why="The federation ended after the referendum of 20 May 1972."),
            C("It created the single party", why="The CNU was formed on 1 September 1966."),
            C("It made Muna federal President", why="Muna led West Cameroon; Ahidjo remained federal President."),
            C("It showed how much influence the federal President had over the states", correct=True),
        ], steps=[S("Interpret", text="The federal President, not West Cameroon alone, decided who led the state government, showing power moving to the centre.")],
           concept="Centralisation of power", skill="Interpretation",
           hint="Ask who chose the leader of a federated state."),
        MC("When was the Cameroon National Union (CNU) formed?", [
            C("1985", why="In 1985 the CNU was renamed the CPDM."),
            C("1 September 1966", correct=True),
            C("1 October 1961", why="This was the date of reunification and the federal constitution."),
            C("20 May 1972", why="This was the referendum that created the unitary state."),
        ], steps=[S("Recall", text="On 1 September 1966 the main parties merged to form the CNU.")],
           concept="Formation of the CNU", skill="Recall",
           hint="It came between reunification and the unitary state."),
        MC("Which parties merged to form the CNU?", [
            C("KNC, KPP and BDC", why="The KNC and KPP had already merged into the CPNC; the BDC was a 1950s French Cameroun party."),
            C("CPDM and SDF", why="The CPDM dates from 1985 and the SDF from 1990."),
            C("UPC, KNDP and OK", why="Remaining UPC activists refused to join and faced repression."),
            C("Union Camerounaise, KNDP, CPNC and CUC", correct=True),
        ], steps=[S("Recall the merger", text="Ahidjo's Union Camerounaise joined the three West Cameroon parties: KNDP, CPNC and CUC.")],
           concept="Formation of the CNU", skill="Recall",
           hint="One party from East Cameroon joined three from West Cameroon."),
        MC("Which was one of the official reasons given for replacing the federation with a unitary state in 1972?", [
            C("The 1961 plebiscite required it after ten years", why="The plebiscite only decided which country Southern Cameroons would join."),
            C("The UN demanded it", why="The UN played no part; the change came through a national referendum."),
            C("The high cost of running three governments", correct=True),
            C("West Cameroon had voted to leave the federation", why="There was no such vote; the 1972 referendum was national."),
        ], steps=[S("Official reasons", text="High cost of three governments; national unity; faster economic development; the single party had already united political life.")],
           concept="Causes of the 1972 change", skill="Reasoning",
           hint="Count the governments and assemblies a federation of two states needed."),
        MC("What name did the country take after the 1972 referendum?", [
            C("United Republic of Cameroon", correct=True),
            C("Republic of Cameroun", why="This was the name of the Francophone state before reunification."),
            C("Federal Republic of Cameroon", why="That was the name from 1961 to 1972."),
            C("Republic of Cameroon", why="This name came in 1984."),
        ], steps=[S("Recall", text="A new constitution in June 1972 created the United Republic of Cameroon, with provinces replacing the two states.")],
           concept="Effects of the 1972 referendum", skill="Recall",
           hint="The new name stressed unity."),
        MC("How do many Anglophone critics view the 1972 change?", [
            C("As the free completion of national unity", why="That is the government's view, not the critics'."),
            C("As the loss of the Foumban guarantees, made in a way the federal constitution did not allow", correct=True),
            C("As a change forced on Cameroon by the UN", why="Neither view blames the UN."),
            C("As a return to rule from Nigeria", why="Nigeria had no role in 1972."),
        ], steps=[S("Government view", text="The completion of national unity, freely approved by the people."),
                  S("Critical view", text="The federal constitution did not allow changes that harmed the federation, and West Cameroon lost the guarantees agreed at Foumban.")],
           concept="Views on the end of federalism", skill="Interpretation",
           hint="Think about what West Cameroon had been promised in 1961."),
    ]))

# ---------------------------------------------------------------------------
# 4. Modern transitions
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_POST, topic="Modern transitions",
    title="Cameroon 1982–1996: Biya, multipartism and the new constitution",
    lesson="cameroon-modern-transitions-1982-1996",
    questions=[
        MC("How did Paul Biya become President in 1982?", [
            C("He won a multiparty presidential election", why="Multiparty presidential elections were first held in 1992."),
            C("He led a coup against Ahidjo", why="Ahidjo resigned; the failed coup attempt was in April 1984, after Biya was already President."),
            C("As Prime Minister, he was Ahidjo's constitutional successor after Ahidjo resigned", correct=True),
            C("He was chosen at the Tripartite Conference", why="The Tripartite Conference took place in 1991."),
        ], steps=[S("Ahidjo resigns", text="Ahidjo announced his resignation on 4 November 1982."),
                  S("Constitutional succession", text="Under the constitution the Prime Minister, Paul Biya, became President and was sworn in on 6 November 1982.")],
           concept="The 1982 transition", skill="Recall",
           hint="Think about what office Biya held just before November 1982."),
        MC("What happened in Yaoundé on 6 April 1984?", [
            C("An attempted coup failed", correct=True),
            C("Biya was sworn in as President", why="Biya was sworn in on 6 November 1982."),
            C("The SDF was launched", why="The SDF was launched in Bamenda on 26 May 1990."),
            C("The CNU became the CPDM", why="This happened at a congress in Bamenda in 1985."),
        ], steps=[S("Recall", text="On 6 April 1984 an attempted coup failed in Yaoundé. Ahidjo, accused of links to it, lived in exile until his death in 1989.")],
           concept="The 1982 transition and its aftermath", skill="Recall",
           hint="This event worsened the break between Biya and Ahidjo."),
        MC("Why did many Anglophones object to the 1984 change of the country's name to Republic of Cameroon?", [
            C("It restored the federal system", why="The name change did not restore federalism, which had ended in 1972."),
            C("It was chosen by a referendum they boycotted", why="The name was changed by a law in February 1984, not a referendum."),
            C("It removed French as an official language", why="The name change was not about languages."),
            C("It was the name of the Francophone state before reunification", correct=True),
        ], steps=[S("Two views", text="The government presented the name change as a sign of national unity. Many Anglophones objected because Republic of Cameroun had been the Francophone state's name before 1961.")],
           concept="The 1984 name change", skill="Interpretation",
           hint="Recall what the French-speaking state was called at independence in 1960."),
        MC("Who launched the Social Democratic Front (SDF), and where?", [
            C("John Fru Ndi, in Yaoundé", why="The leader is right but the launch took place in Bamenda."),
            C("John Fru Ndi, in Bamenda", correct=True),
            C("John Ngu Foncha, in Buea", why="Foncha founded the KNDP in 1955, not the SDF."),
            C("Ndeh Ntumazah, in Kumba", why="Ntumazah founded One Kamerun in 1957."),
        ], steps=[S("Recall", text="On 26 May 1990 the SDF was launched in Bamenda by John Fru Ndi. Several people were killed when security forces dispersed the launch.")],
           concept="Return of multipartism", skill="Recall",
           hint="The same town hosted the 1985 CNU congress."),
        MC("What did the liberty laws of December 1990 do?", [
            C("Ended the ghost towns campaign", why="The ghost towns campaign came in 1991, after the liberty laws."),
            C("Set a seven-year presidential term", why="This was in the 1996 constitution."),
            C("Created a Senate and a Constitutional Council", why="These were created by the 1996 constitution."),
            C("Allowed the creation of political parties and associations and eased press controls", correct=True),
        ], steps=[S("Recall", text="The National Assembly passed the liberty laws in December 1990, restoring multipartism and easing controls on the press and public meetings.")],
           concept="The liberty laws", skill="Recall",
           hint="These laws ended the one-party system."),
        MC("Why did the opposition organise the ghost towns campaign in 1991?", [
            C("Because Biya had resigned", why="Biya did not resign; he won the 1992 presidential election."),
            C("To protest against the 1972 referendum", why="The 1972 referendum was almost twenty years earlier."),
            C("Because the government refused their demand for a sovereign national conference", correct=True),
            C("To celebrate the passing of the liberty laws", why="Ghost towns were a protest that closed shops and transport, not a celebration."),
        ], steps=[S("Cause", text="Opposition parties demanded a sovereign national conference; the government refused."),
                  S("Method", text="Shops, markets and transport stayed closed on working days, hitting trade in Douala, Bamenda and other towns.")],
           concept="Ghost towns campaign", skill="Reasoning",
           hint="Think about what the opposition demanded that other African countries had held."),
        MC("Who took part in the Tripartite Conference of October–November 1991?", [
            C("The government, opposition parties and civil society", correct=True),
            C("Ahidjo, Biya and Fru Ndi", why="Ahidjo died in exile in 1989."),
            C("Cameroon, Nigeria and the UN", why="It was a national meeting, not an international one."),
            C("The CNU, the KNDP and the UPC", why="These parties belong to the 1960s; the CNU had become the CPDM in 1985."),
        ], steps=[S("Recall", text="The Tripartite Conference in Yaoundé brought together the government, opposition parties and civil society to end the crisis."),
                  S("Results", text="It agreed steps to restore calm and set up a committee to draft constitutional reforms; some opposition leaders refused to sign.")],
           concept="Tripartite Conference", skill="Recall",
           hint="The name tells you how many groups took part."),
        MC("Which of these was a provision of the constitution of 18 January 1996?", [
            C("A return to a federation of two states", why="It confirmed Cameroon as a decentralised unitary state."),
            C("A seven-year presidential term, renewable once", correct=True),
            C("The creation of the CNU as the only party", why="The CNU dates from 1966, and multipartism was restored in 1990."),
            C("A five-year presidential term with no limit", why="It set a seven-year term, renewable once; the limit was removed in 2008."),
        ], steps=[S("Provisions", text="Seven-year term renewable once; a Senate; a Constitutional Council; regions with elected councils; a decentralised unitary state."),
                  S("Later change", text="A 2008 amendment removed the limit on presidential terms.")],
           concept="The 1996 constitution", skill="Recall",
           hint="The term limit in this constitution was later removed in 2008."),
    ]))

# ---------------------------------------------------------------------------
# 5. African decolonization
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_WORLD, topic="African decolonization",
    title="African decolonization, the OAU and the AU", lesson="african-decolonization-oau-au",
    questions=[
        MC("Which of these was an external cause of African decolonization after 1945?", [
            C("The founding of the OAU", why="The OAU was founded in 1963 by states that were already independent."),
            C("The launch of the African Union", why="The AU was launched in 2002, long after most colonies were free."),
            C("The UN Charter's support for self-determination", correct=True),
            C("The Lisbon revolution of 1945", why="The revolution in Lisbon came in 1974 and affected only the Portuguese colonies."),
        ], steps=[S("External causes", text="The weakening of Britain and France in the Second World War, the UN Charter's support for self-determination, superpower criticism of empires and India's independence in 1947.")],
           concept="Causes of decolonization", skill="Reasoning",
           hint="Look for a cause that existed in 1945, before most colonies were free."),
        MC("Which meeting in 1945 demanded independence for African colonies?", [
            C("The Pan-African Congress in Manchester", correct=True),
            C("The founding meeting of the OAU in Addis Ababa", why="The OAU was founded in 1963."),
            C("The Foumban Conference", why="Foumban (1961) was about Cameroon's federal constitution."),
            C("The Durban summit", why="The AU was launched in Durban in 2002."),
        ], steps=[S("Recall", text="The Pan-African Congress held in Manchester in 1945 demanded independence.")],
           concept="African nationalism and Pan-Africanism", skill="Recall",
           hint="It was held in Britain in the year the Second World War ended."),
        MC("Which country was the first colony south of the Sahara to become independent?", [
            C("Algeria, in 1962", why="Algeria is north of the Sahara and became independent after a war in 1962."),
            C("Kenya, in 1963", why="Kenya became independent in 1963 after the Mau Mau uprising."),
            C("Nigeria, in 1960", why="Nigeria became independent in 1960, three years later."),
            C("Ghana, on 6 March 1957", correct=True),
        ], steps=[S("Recall", text="Ghana (formerly the Gold Coast) became independent on 6 March 1957 under Kwame Nkrumah.")],
           concept="Peaceful transfers of power", skill="Recall",
           hint="Its first leader was Kwame Nkrumah."),
        MC("Why did decolonization in Algeria and Kenya involve armed struggle rather than a peaceful transfer?", [
            C("They were UN trust territories", why="Trusteeship was the status of territories like Cameroon, not Algeria or Kenya."),
            C("There were many European settlers and the colonial power resisted leaving", correct=True),
            C("The OAU ordered armed struggle", why="The OAU was founded in 1963, after the Algerian war had started in 1954 and the Mau Mau rising in 1952."),
            C("They had no nationalist parties", why="Both had nationalist movements, such as the FLN in Algeria."),
        ], steps=[S("Pattern", text="Armed struggle was common where there were many settlers or where the colonial power refused to leave."),
                  S("Examples", text="Algeria: FLN against France, 1954–1962. Kenya: Mau Mau from 1952, independence 1963.")],
           concept="Peaceful transfer versus armed struggle", skill="Reasoning",
           hint="Compare who lived in these colonies with Ghana or Senegal."),
        MC("What event led Portugal to end its colonial rule in Angola, Mozambique and Guinea-Bissau?", [
            C("The creation of the OAU in 1963", why="The OAU opposed colonialism but Portugal kept its colonies until 1974."),
            C("The end of the Cold War in 1991", why="These colonies were already independent by 1975."),
            C("India's independence in 1947", why="That inspired nationalists, but Portugal still refused to decolonize for decades."),
            C("A revolution in Lisbon in 1974", correct=True),
        ], steps=[S("Recall", text="Portugal refused to decolonize until a revolution in Lisbon in 1974; Angola, Mozambique and Guinea-Bissau won independence in 1974–1975 after long wars.")],
           concept="Armed struggles in Portuguese Africa", skill="Reasoning",
           hint="The change came from inside Portugal itself."),
        MC("Where and when was the OAU founded?", [
            C("Addis Ababa, 9 July 2002", why="The city is right for the OAU, but this date belongs to the AU's launch in Durban."),
            C("Durban, 9 July 2002", why="This is the launch of the African Union."),
            C("Addis Ababa, 25 May 1963", correct=True),
            C("Accra, 6 March 1957", why="This is the date of Ghana's independence."),
        ], steps=[S("Recall", text="OAU: Addis Ababa, 25 May 1963. AU: Durban, 9 July 2002.")],
           concept="The OAU", skill="Recall",
           hint="It was founded in Ethiopia, three years after Cameroon's independence."),
        MC("Which was a major weakness of the OAU?", [
            C("Its policy of non-interference in members' internal affairs", correct=True),
            C("It rejected the borders inherited from colonial rule", why="The OAU accepted the colonial borders."),
            C("It refused to help liberation movements", why="It helped liberation movements through its Liberation Committee."),
            C("It supported apartheid in South Africa", why="The OAU opposed apartheid."),
        ], steps=[S("Weaknesses", text="Weak powers, lack of money and non-interference in members' internal affairs meant it could not act against abuses inside member states.")],
           concept="Achievements and weaknesses of the OAU", skill="Concept",
           hint="Think about what the OAU could not do when abuses happened inside a member state."),
        MC("How does the African Union differ from the OAU?", [
            C("The AU accepts members only from North Africa", why="The AU is a continental body like the OAU."),
            C("The AU may intervene in a member state in grave circumstances such as genocide", correct=True),
            C("The AU has no Parliament", why="The AU has a Pan-African Parliament."),
            C("The AU follows strict non-interference", why="Strict non-interference was the OAU's policy; the AU's Constitutive Act allows intervention."),
        ], steps=[S("Key difference", text="The AU's Constitutive Act allows intervention in grave circumstances such as genocide and war crimes; it has organs such as the Pan-African Parliament and the Peace and Security Council.")],
           concept="OAU and AU compared", skill="Concept",
           hint="Leaders created the AU to fix one of the OAU's main weaknesses."),
    ]))

# ---------------------------------------------------------------------------
# 6. Cold War
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_WORLD, topic="Cold War",
    title="The Cold War", lesson="the-cold-war",
    questions=[
        MC("Which statement best describes the Cold War?", [
            C("A conflict between European colonial powers over Africa", why="The Cold War was a rivalry between the capitalist USA and the communist USSR."),
            C("A direct war between the USA and the USSR from 1945 to 1991", why="The two superpowers never fought each other directly."),
            C("A rivalry fought by propaganda, arms races and proxy wars rather than direct war", correct=True),
            C("A war between the USA and Germany", why="The USA and USSR were allies against Nazi Germany before the Cold War."),
        ], steps=[S("Definition", text="The Cold War was tension and rivalry between the USA and the USSR and their allies from 1945 to 1991, without direct war between them.")],
           concept="Nature of the Cold War", skill="Concept",
           hint="Think about why the word cold is used."),
        MC("In 1946 Winston Churchill described the division of Europe using which phrase?", [
            C("An iron curtain", correct=True),
            C("Glasnost", why="Glasnost (openness) was Gorbachev's reform in the 1980s."),
            C("A proxy war", why="A proxy war is a conflict in which superpowers back opposing sides."),
            C("Containment", why="Containment was the US policy of stopping the spread of communism."),
        ], steps=[S("Recall", text="After the USSR set up communist governments in Eastern Europe, Churchill said in 1946 that an iron curtain had come down across Europe.")],
           concept="Causes of the Cold War", skill="Recall",
           hint="The phrase suggests a heavy barrier dividing east from west."),
        MC("What was the aim of the Marshall Plan (1947)?", [
            C("To form a military alliance against the USSR", why="That was NATO, formed in 1949."),
            C("To supply West Berlin by air", why="That was the Berlin Airlift of 1948–1949."),
            C("To remove Soviet missiles from Cuba", why="That was the outcome of the 1962 crisis."),
            C("To give economic aid to rebuild Western Europe", correct=True),
        ], steps=[S("Recall", text="The Marshall Plan gave economic aid to Western Europe so that poverty would not encourage communism.")],
           concept="Containment", skill="Recall",
           hint="It was the economic partner of the Truman Doctrine."),
        MC("Which pair of alliances and dates is correct?", [
            C("NATO 1947; Warsaw Pact 1962", why="1947 was the Truman Doctrine and Marshall Plan; 1962 was the Cuban Missile Crisis."),
            C("NATO 1949; Warsaw Pact 1955", correct=True),
            C("NATO 1949; Warsaw Pact 1991", why="The USSR was dissolved in 1991; the Warsaw Pact was formed in 1955."),
            C("NATO 1955; Warsaw Pact 1949", why="The dates are reversed."),
        ], steps=[S("Recall", text="The USA and its allies formed NATO in 1949; the USSR and its allies formed the Warsaw Pact in 1955.")],
           concept="Cold War alliances", skill="Recall",
           hint="The Western alliance came first, soon after the Berlin Blockade began."),
        MC("How did the Cuban Missile Crisis end in October 1962?", [
            C("The USSR kept its missiles in Cuba in exchange for leaving Berlin", why="The Soviet missiles were removed; Berlin was not part of the deal."),
            C("Gorbachev and Kennedy signed a peace treaty", why="Gorbachev led the USSR only from 1985."),
            C("The USA invaded Cuba and removed Castro", why="The USA promised not to invade Cuba, and Cuba stayed communist."),
            C("Khrushchev agreed to remove the missiles; the USA promised not to invade Cuba", correct=True),
        ], steps=[S("The crisis", text="US spy planes found Soviet missile sites; Kennedy ordered a naval blockade; thirteen days of tension followed."),
                  S("The deal", text="Khrushchev removed the missiles; the USA promised not to invade Cuba and later removed its missiles from Turkey.")],
           concept="Cuban Missile Crisis", skill="Recall",
           hint="Each side gave something to avoid nuclear war."),
        MC("Which was a result of the Cuban Missile Crisis?", [
            C("The opening of the Berlin Wall", why="The Berlin Wall was opened in 1989."),
            C("The Soviet invasion of Afghanistan", why="That began in 1979 and was not a result of the crisis."),
            C("A telephone hotline between Washington and Moscow", correct=True),
            C("The formation of NATO", why="NATO was formed in 1949, long before 1962."),
        ], steps=[S("Results", text="A hotline (1963), the Partial Test Ban Treaty (1963), and more caution about direct confrontation.")],
           concept="Cuban Missile Crisis", skill="Reasoning",
           hint="Both sides wanted a quicker way to talk in a future crisis."),
        MC("In Angola after 1975, which side did the USSR and Cuba support?", [
            C("The MPLA government", correct=True),
            C("Portugal", why="Portugal had already left after the 1974 revolution in Lisbon."),
            C("Neither side: Angola was not a Cold War conflict", why="Angola is one of the lesson's examples of a proxy war."),
            C("The rivals of the MPLA", why="The USA and South Africa backed the MPLA's rivals."),
        ], steps=[S("Proxy war", text="The USSR and Cuba supported the MPLA government while the USA and South Africa backed its rivals.")],
           concept="Proxy wars", skill="Recall",
           hint="Remember Angola as an example of a proxy war in Africa."),
        MC("Historians weigh the causes of the Soviet collapse differently. Which pair describes the two emphases in the lesson?", [
            C("Some stress the Marshall Plan; others stress the Truman Doctrine", why="These were 1947 US policies, not the debated causes of the 1991 collapse."),
            C("Some stress Western pressure; others stress internal weakness", correct=True),
            C("Some stress the Cuban crisis; others stress the Korean War", why="These were earlier events and are not the factors the lesson gives for 1991."),
            C("Some stress African independence; others stress the OAU", why="These are not given as causes of the Soviet collapse."),
        ], steps=[S("Causes", text="Economic: stagnant economy, shortages, the cost of the arms race and Afghanistan. Political: Gorbachev's reforms, nationalism in the republics, the failed 1991 coup."),
                  S("Debate", text="Some historians stress Western pressure, others internal weakness.")],
           concept="Collapse of the USSR", skill="Interpretation",
           hint="One view looks outside the USSR, the other looks inside."),
    ]))

# ---------------------------------------------------------------------------
# 7. Post-Cold War world
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_WORLD, topic="Post-Cold War world",
    title="The Arab–Israeli conflict and the post-Cold War world", lesson="arab-israeli-conflict-post-cold-war",
    questions=[
        MC("What did Britain state in the Balfour Declaration of 1917?", [
            C("Recognition of the PLO", why="Israel and the PLO recognised each other in the Oslo Accords of 1993."),
            C("Independence for Palestine under Arab rule", why="The declaration supported a Jewish national home; it did not grant independence."),
            C("Support for a national home for the Jewish people in Palestine, while respecting the rights of existing non-Jewish communities", correct=True),
            C("A plan to partition Palestine into two states", why="Partition was proposed by the UN in November 1947."),
        ], steps=[S("Recall", text="In 1917 Britain supported a national home for the Jewish people in Palestine while promising to respect the rights of the existing non-Jewish communities.")],
           concept="Origins of the Arab–Israeli conflict", skill="Recall",
           hint="The declaration made promises to two communities at once."),
        MC("How did Jewish and Arab leaders respond to the UN partition plan of November 1947?", [
            C("Jewish leaders accepted it; Arab leaders rejected it", correct=True),
            C("Arab leaders accepted it; Jewish leaders rejected it", why="This reverses the two responses."),
            C("Both rejected it", why="Jewish leaders accepted the plan."),
            C("Both accepted it", why="Arab leaders rejected the plan."),
        ], steps=[S("Recall", text="The UN voted to partition Palestine into a Jewish state and an Arab state. Jewish leaders accepted; Arab leaders rejected it.")],
           concept="The 1947 partition plan", skill="Recall",
           hint="The two sides did not respond in the same way."),
        MC("When did Israel declare independence?", [
            C("June 1967", why="This was the Six-Day War."),
            C("1917", why="This was the Balfour Declaration."),
            C("November 1947", why="This was the UN vote on partition."),
            C("14 May 1948", correct=True),
        ], steps=[S("Recall", text="Israel declared independence on 14 May 1948, as Britain left; neighbouring Arab states attacked.")],
           concept="The 1948–1949 war", skill="Recall",
           hint="It came a few months after the UN partition vote."),
        MC("Which territories did Israel occupy in the Six-Day War of June 1967?", [
            C("None: Israel lost the war", why="Israel defeated Egypt, Jordan and Syria in 1967."),
            C("Sinai, Gaza, the West Bank, East Jerusalem and the Golan Heights", correct=True),
            C("Kuwait and southern Iraq", why="Kuwait was involved in the Gulf War of 1991, when a coalition drove Iraq out."),
            C("Only the Suez Canal zone", why="In 1956 Israel attacked Egypt over Suez but withdrew under superpower pressure."),
        ], steps=[S("Recall", text="Israel defeated Egypt, Jordan and Syria and occupied the Sinai, Gaza, the West Bank, East Jerusalem and the Golan Heights.")],
           concept="The Six-Day War", skill="Recall",
           hint="Israel fought Egypt, Jordan and Syria; think of land taken from each."),
        MC("What followed the Yom Kippur War of October 1973?", [
            C("Egypt nationalised the Suez Canal", why="Nasser nationalised the canal before the 1956 Suez Crisis."),
            C("Israel declared independence", why="Israel declared independence in 1948."),
            C("The Oslo Accords", why="Oslo came twenty years later, in 1993."),
            C("Arab oil producers raised prices and cut supplies to countries that supported Israel", correct=True),
        ], steps=[S("Recall", text="Egypt and Syria attacked Israel in October 1973; Arab oil producers then raised prices and cut supplies, causing an oil crisis.")],
           concept="The Yom Kippur War", skill="Reasoning",
           hint="Arab states used an economic weapon."),
        MC("Which agreements are correctly matched with the parties involved?", [
            C("Camp David (1978): Israel and the PLO", why="Camp David was between Egypt and Israel; Oslo involved the PLO."),
            C("Oslo (1993): Egypt and Israel", why="Oslo involved Israel and the PLO; Egypt made peace at Camp David."),
            C("Camp David (1978): Egypt and Israel; Oslo (1993): Israel and the PLO", correct=True),
            C("Oslo (1993): Jordan and Israel", why="Jordan signed a separate peace treaty with Israel in 1994."),
        ], steps=[S("Camp David", text="Mediated by President Carter; Egypt and Israel agreed peace; the 1979 treaty returned Sinai to Egypt."),
                  S("Oslo", text="Israel and the PLO recognised each other; a Palestinian Authority with limited self-rule was created.")],
           concept="The search for peace", skill="Recall",
           hint="One agreement involved a state, the other an organisation."),
        MC("Why is the year 1948 a sensitive subject when studying this conflict?", [
            C("Israelis and Palestinians describe 1948 very differently, so both narratives should be presented", correct=True),
            C("Historians agree on every detail, so there is nothing to discuss", why="The lesson stresses that the two peoples describe 1948 very differently."),
            C("Nothing important happened in 1948", why="Israel was declared and a war followed, creating a refugee problem."),
            C("Only the Palestinian view is accepted by historians", why="A good answer presents both narratives without taking sides."),
        ], steps=[S("What happened", text="Israel was declared and won the 1948–1949 war; hundreds of thousands of Palestinians fled or were expelled."),
                  S("Approach", text="Israelis and Palestinians describe these events very differently; present both without taking sides.")],
           concept="Differing narratives of 1948", skill="Interpretation",
           hint="Think about how each people remembers the creation of Israel and the refugee problem."),
        MC("Which feature of the world after 1991 led some to describe it as unipolar?", [
            C("The rise of China", why="China's economic rise led many to speak of a multipolar world, the opposite idea."),
            C("The USA was the only remaining superpower", correct=True),
            C("The growth of the African Union", why="Regional blocs point towards a multipolar world, not a unipolar one."),
            C("The formation of the Warsaw Pact", why="The Warsaw Pact was formed in 1955 and belongs to the Cold War."),
        ], steps=[S("Unipolar", text="After the USSR collapsed in 1991 the USA was the only superpower; the 1991 Gulf War showed its power."),
                  S("Later", text="Globalisation, the rise of China and regional blocs led many to speak of a multipolar world.")],
           concept="The post-Cold War order", skill="Concept",
           hint="Uni means one: one what?"),
    ]))
