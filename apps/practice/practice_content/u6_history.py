"""Upper Sixth History practice sets (draft). Facts are taken only from the matching lessons in
apps/courses/lesson_content/u6_history.py. Contested Cameroonian topics are tested as interpretations.
"""

from .dsl import *  # noqa: F403

COURSE = ("history", "upper-sixth")

M_CMR = "Cameroon 1945 to Today"
M_DEC = "Decolonization in Africa"
M_CW = "Cold War & International Governance"

SETS = []

# ---------------------------------------------------------------------------
# 1. Trusteeship and decolonization
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CMR, topic="Trusteeship and decolonization",
    title="French Cameroun under trusteeship, 1946 to 1960", lesson="trusteeship-and-decolonization",
    questions=[
        MC("Which article of the UN Charter required an administering power to promote progress towards "
           "self-government or independence in a trust territory?", [
            C("Article 76", correct=True),
            C("Chapter VII", why="Chapter VII lets the Security Council order sanctions or military action; it is not the trusteeship promise."),
            C("Chapter VI", why="Chapter VI covers the peaceful settlement of disputes, not the duties of an administering power."),
            C("Article 22 of the League Covenant", why="That concerned League mandates; after 1946 Cameroon was a UN trust territory under the Charter."),
        ], steps=[S("Recall the legal basis", text="Article 76 of the UN Charter obliged the administering power to promote progress towards self-government or independence.")],
           concept="Trusteeship: Article 76 of the UN Charter", skill="Recall",
           hint="It is the Charter article the UPC relied on to argue that independence was the goal."),
        MC("Which pair of demands was central to the UPC programme?", [
            C("Reunification of the British and French Cameroons and independence on a fixed timetable", correct=True),
            C("Union with Nigeria and gradual reform", why="Closer ties with Nigeria were associated with the KNC in Southern Cameroons, not the UPC."),
            C("Full integration into the French Union", why="That was closer to the French position, which the UPC rejected."),
            C("Federation with Gabon and a customs union", why="The lesson gives no such aim; the UPC focused on the two Cameroons."),
        ], steps=[S("Recall the UPC aims", text="Founded in Douala in April 1948, the UPC demanded reunification and independence on a fixed timetable.")],
           concept="Aims of the UPC", skill="Recall",
           hint="One demand concerned the two parts of the former German Kamerun; the other concerned timing."),
        MC("Why did the UPC put so much effort into petitions and speeches at the United Nations?", [
            C("Trusteeship gave Cameroonians a voice outside the colonial power and a Charter promise of self-government", correct=True),
            C("The UN governed Cameroun directly from New York", why="The UN supervised; France administered the territory."),
            C("France had already agreed to a fixed date for independence", why="France rejected a fixed timetable; that was exactly what the UPC wanted the UN to impose."),
            C("The UN had the power to force France to hold elections", why="The UN could recommend but not compel; it later accepted independence without new elections."),
        ], steps=[S("Link status and strategy", text="As a trust territory, Cameroun could petition the UN and meet visiting missions, and the Charter promised progress towards self-government.")],
           concept="UN trusteeship as a nationalist platform", skill="Reasoning",
           hint="Think about what made a trust territory legally different from an ordinary colony."),
        MC("How did France interpret Cameroun's status, according to the lesson?", [
            C("As an associated territory linked to the French Union, with gradual reform and no fixed short-term goal of independence", correct=True),
            C("As a trust territory that should be independent on a fixed timetable", why="That was the UPC position, the opposite of the French view."),
            C("As a territory that the UN should govern directly", why="France administered Cameroun and wanted to keep control of the pace of change."),
            C("As part of Nigeria", why="Only British Cameroons was governed with Nigeria."),
        ], steps=[S("Compare the two readings", text="France saw an associated territory of the French Union; the UPC saw a trust territory promised self-government.")],
           concept="French and UPC readings of trusteeship", skill="Interpretation",
           hint="The lesson contrasts two opposite readings of trusteeship. Which one belongs to the administering power?"),
        MC("What was the immediate consequence of the clashes of May 1955 for the UPC?", [
            C("The party was banned by decree in July 1955 and many leaders fled to British Southern Cameroons", correct=True),
            C("The UPC won the December 1956 assembly elections", why="The banned UPC could not take part and called for a boycott."),
            C("Um Nyobè became Prime Minister", why="Mbida became the first Prime Minister in 1957, then Ahidjo in 1958."),
            C("The UN ended trusteeship at once", why="Trusteeship ended only on 1 January 1960, after the UN decision of March 1959."),
        ], steps=[S("Follow the sequence", text="France blamed the UPC for the May 1955 clashes, banned it in July 1955, and many leaders fled to Southern Cameroons and later into exile.")],
           concept="The 1955 ban of the UPC", skill="Reasoning",
           hint="The French authorities blamed the UPC. What legal step followed two months later?"),
        MC("Who replaced André-Marie Mbida as Prime Minister in February 1958?", [
            C("Ahmadou Ahidjo", correct=True),
            C("Ruben Um Nyobè", why="Um Nyobè led the banned UPC and was killed in the Sanaga-Maritime in September 1958."),
            C("Félix-Roland Moumié", why="Moumié was a UPC leader in exile who died in Geneva in 1960."),
            C("John Ngu Foncha", why="Foncha was a Southern Cameroons (KNDP) politician."),
        ], steps=[S("Recall the change of premier", text="Mbida lost French support and resigned; his deputy Ahidjo, a northern politician of the Union Camerounaise, replaced him.")],
           concept="Ahidjo's rise to power", skill="Recall",
           hint="He was Mbida's deputy and a northern politician of the Union Camerounaise."),
        MC("What did the UN General Assembly decide in March 1959, and why did the UPC object?", [
            C("To end trusteeship on 1 January 1960 without first holding new elections under UN supervision", correct=True),
            C("To extend trusteeship for ten more years", why="The UN set an end date of 1 January 1960, not an extension."),
            C("To hold a plebiscite on joining Nigeria", why="Plebiscites concerned British Cameroons in 1961, not French Cameroun."),
            C("To lift the ban on the UPC before independence", why="The lesson records no such decision; the UPC's complaint was about the lack of new elections."),
        ], steps=[S("Recall the decision", text="The UN agreed to independence on 1 January 1960 without the new supervised elections the UPC and its allies had demanded.")],
           concept="The 1959 UN decision on independence", skill="Interpretation",
           hint="The UPC hoped elections would give it a route back into politics. Did the UN require them?"),
        MC("A historian writes that power in 1960 'passed to leaders acceptable to France'. Which interpretation does this "
           "statement belong to?", [
            C("The nationalist and critical view, associated with writers such as Richard Joseph", correct=True),
            C("The official and moderate view", why="That view stresses a peaceful, negotiated independence through the UN, not a transfer to France's chosen partners."),
            C("The social-history view", why="Social historians such as Mbembe and Terretta stress local grievances, memory and networks rather than this verdict on 1960."),
            C("The French administrative view of 'pacification'", why="Pacification was the official French term for the military campaign, not a historians' interpretation of 1960."),
        ], steps=[S("Match the claim to the school", text="The nationalist and critical view sees the UPC as the authentic national movement crushed by a French war, so power passed to leaders acceptable to France.")],
           concept="Historiography of the UPC and 1960", skill="Interpretation",
           hint="Which view sees the UPC as the authentic movement that was defeated by force?"),
    ]))

# ---------------------------------------------------------------------------
# 2. Southern Cameroons politics
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CMR, topic="Southern Cameroons politics",
    title="Southern Cameroons: parties, plebiscite and Foumban", lesson="southern-cameroons-politics",
    questions=[
        MC("Which party, led by John Ngu Foncha, broke away in 1955 and came to favour reunification with Cameroun?", [
            C("Kamerun National Democratic Party (KNDP)", correct=True),
            C("Kamerun National Congress (KNC)", why="The KNC was Endeley's party, formed in 1953, which came to favour close ties with Nigeria."),
            C("One Kamerun (OK)", why="OK was founded in 1957 by Ndeh Ntumazah and was close to the UPC."),
            C("Union des Populations du Cameroun (UPC)", why="The UPC was founded in Douala in French Cameroun in 1948."),
        ], steps=[S("Match party and leader", text="Foncha led the KNDP, which broke away in 1955 and led the reunification side.")],
           concept="Southern Cameroons parties and leaders", skill="Recall",
           hint="Foncha's party broke away from Endeley's in 1955."),
        MC("Which party was led by Ndeh Ntumazah and was close to the UPC?", [
            C("One Kamerun (OK)", correct=True),
            C("KNDP", why="The KNDP was led by Foncha and generally imagined a loose federation, not the radical UPC line."),
            C("CPNC", why="The CPNC was formed in 1960 by Endeley's KNC and Kale's KPP and leaned towards Nigeria."),
            C("Union Camerounaise", why="That was Ahidjo's northern party in French Cameroun."),
        ], steps=[S("Recall OK", text="One Kamerun, founded in 1957 by Ndeh Ntumazah, campaigned for immediate reunification and independence and was linked to the UPC.")],
           concept="One Kamerun and radical reunification", skill="Recall",
           hint="Its name itself expresses the reunification idea."),
        MC("What did the 1954 Nigerian constitution give Southern Cameroons?", [
            C("Its own House of Assembly at Buea, with Endeley as Leader of Government Business", correct=True),
            C("Full independence from Britain", why="Southern Cameroons remained a trust territory until reunification in 1961."),
            C("Union with French Cameroun", why="Reunification came only in October 1961, after the plebiscite."),
            C("Seats in the Eastern Nigerian House of Assembly for the first time", why="Its members already sat there; their 1953 break with the governing party led to separate treatment."),
        ], steps=[S("Recall the 1954 change", text="After the 1953 crisis in the Eastern Region, the 1954 constitution gave Southern Cameroons its own assembly at Buea.")],
           concept="From Nigerian region to separate government", skill="Recall",
           hint="Think of the town that became the seat of the Southern Cameroons government."),
        MC("Why was the Mamfe conference of August 1959 significant?", [
            C("Leaders failed to agree on the plebiscite questions and voter eligibility, so the UN decided them itself", correct=True),
            C("It drew up the federal constitution of 1961", why="The federal constitution was discussed at Foumban in July 1961."),
            C("It made Foncha Premier", why="Foncha became Premier after the KNDP won the January 1959 elections."),
            C("It agreed to put separate independence on the ballot", why="Separate independence was not offered on the ballot."),
        ], steps=[S("Explain the consequence", text="Deadlock at Mamfe took the choice of options away from Southern Cameroons politicians; the UN fixed the terms.")],
           concept="Mamfe conference and the plebiscite terms", skill="Reasoning",
           hint="Did the leaders at Mamfe reach agreement? If not, who settled the questions?"),
        MC("Which two options did the UN place on the 1961 Southern Cameroons plebiscite ballot?", [
            C("Independence by joining Nigeria, or independence by joining the Republic of Cameroun", correct=True),
            C("Separate independence, or joining Nigeria", why="Separate independence was not offered; whether it should have been is still debated."),
            C("Continued British trusteeship, or independence", why="Trusteeship was ending; continuing it was not an option."),
            C("Joining the French Community, or joining Nigeria", why="The French Community concerned French territories in 1958, not this plebiscite."),
        ], steps=[S("Recall the two options", text="Voters chose between the Federation of Nigeria and the Republic of Cameroun.")],
           concept="The 1961 plebiscite questions", skill="Recall",
           hint="Both options meant gaining independence by joining an already independent neighbour."),
        MC("What were the results of the February 1961 plebiscites?", [
            C("Northern Cameroons voted to join Nigeria; Southern Cameroons voted to join the Republic of Cameroun", correct=True),
            C("Both Northern and Southern Cameroons voted to join Cameroun", why="Only the south joined Cameroun; the north became part of Nigeria on 1 June 1961."),
            C("Both voted to join Nigeria", why="Southern Cameroons voted clearly, by roughly seven votes in ten, for Cameroun."),
            C("Southern Cameroons voted for Nigeria and Northern Cameroons for Cameroun", why="This reverses the two results."),
        ], steps=[S("Separate north and south", text="The north joined Nigeria on 1 June 1961; the south voted by about seven in ten to join Cameroun.")],
           concept="Plebiscite results, north and south", skill="Recall",
           hint="A common mistake is to say that all of British Cameroons joined Cameroun."),
        MC("Which argument is used by writers who see Foumban as an imposed settlement?", [
            C("The draft was prepared in advance, the Southern Cameroons team was small, and few of its amendments were accepted", correct=True),
            C("Southern Cameroons leaders took part and accepted the outcome", why="This is evidence used by the negotiated-settlement view."),
            C("A federation with its own West Cameroon institutions was created as promised", why="This also supports the negotiated-settlement view."),
            C("A sovereign state faced a trust territory whose future the plebiscite had already decided", why="This unequal-bargaining point is the contextual view."),
        ], steps=[S("Sort the evidence by view", text="Imposed view: prepared draft, small team, few amendments accepted. Negotiated view: participation and consent. Contextual view: unequal bargaining power.")],
           concept="Interpretations of the Foumban conference", skill="Interpretation",
           hint="Look for the option that stresses how the draft and the delegations were prepared."),
        MC("Which option correctly describes the Federal Republic of Cameroon born on 1 October 1961?", [
            C("Two federated states, East and West Cameroon, with Ahidjo as Federal President and Foncha as Vice-President", correct=True),
            C("A unitary state with Ahidjo as President", why="The unitary United Republic came only after the 1972 referendum."),
            C("Three federated states including Northern Cameroons", why="Northern Cameroons had joined Nigeria in June 1961."),
            C("Two federated states with Foncha as Federal President", why="Foncha became Vice-President; Ahidjo was Federal President."),
        ], steps=[S("Recall the federal structure", text="East Cameroon and West Cameroon formed the federation; Ahidjo was President and Foncha Vice-President.")],
           concept="The federation of 1 October 1961", skill="Recall",
           hint="Who led the Cameroun delegation at Foumban, and who led the Southern Cameroons one?"),
    ]))

# ---------------------------------------------------------------------------
# 3. The post-colonial state
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CMR, topic="The post-colonial state",
    title="From federation to the 1996 constitution", lesson="the-post-colonial-state",
    questions=[
        MC("What distinguishes a federation from a unitary state?", [
            C("In a federation the constitution divides powers between central and regional governments; in a unitary state sovereignty rests with the centre", correct=True),
            C("A federation has a president; a unitary state has a prime minister", why="The form of the executive does not define federalism; the division of powers does."),
            C("A unitary state cannot delegate any powers to local bodies", why="A unitary state may delegate powers to local bodies, as the 1996 decentralized state shows."),
            C("A federation always has a single party", why="Party systems are separate from state structure; the 1961 federation had several parties until 1966."),
        ], steps=[S("Apply the definitions", text="Federation: powers divided by the constitution. Unitary state: sovereignty with the central government, which may delegate.")],
           concept="Federalism and unitarism", skill="Concept",
           hint="Ask who holds sovereignty and whether the constitution guarantees regional powers."),
        MC("Which powers were federal from the start under the 1961 constitution?", [
            C("Defence, foreign affairs, finance and security", correct=True),
            C("Only the running of schools and markets", why="The lesson stresses that major powers such as defence and finance were federal from the start."),
            C("None: all powers belonged to the two federated states", why="Important powers were held by the federal government in Yaoundé."),
            C("Customary courts and chieftaincy only", why="These are not the powers the lesson names as federal."),
        ], steps=[S("Recall the 1961 design", text="Defence, foreign affairs, finance and security were federal, which limited the autonomy of the federated states.")],
           concept="Centralizing design of the 1961 federation", skill="Recall",
           hint="Think of the powers any national government would keep for itself."),
        MC("What was created in September 1966?", [
            C("The Cameroon National Union (CNU), making Cameroon a de facto one-party state", correct=True),
            C("The Cameroon People's Democratic Movement (CPDM)", why="The CNU was renamed the CPDM at the Bamenda congress of 1985."),
            C("The Social Democratic Front (SDF)", why="The SDF was launched in Bamenda in May 1990."),
            C("The United Republic of Cameroon", why="That came from the referendum of 20 May 1972."),
        ], steps=[S("Recall the single party", text="In 1966 the main parties of both states, including the Union Camerounaise and the KNDP, merged into the CNU.")],
           concept="The single party (CNU), 1966", skill="Recall",
           hint="Its French initials were UNC."),
        MC("Put these names of the state in the correct order.", [
            C("Federal Republic (1961), United Republic (1972), Republic of Cameroon (1984)", correct=True),
            C("United Republic (1961), Federal Republic (1972), Republic of Cameroon (1984)", why="The federation came first in 1961; the United Republic was the unitary state of 1972."),
            C("Federal Republic (1961), Republic of Cameroon (1972), United Republic (1984)", why="The 1972 referendum created the United Republic; the name Republic of Cameroon came in 1984."),
            C("Republic of Cameroon (1961), Federal Republic (1972), United Republic (1984)", why="This mixes up all three dates."),
        ], steps=[S("Fix the three dates", text="1961 Federal Republic; 1972 United Republic (unitary); 1984 Republic of Cameroon.")],
           concept="Constitutional names of the state", skill="Recall",
           hint="The lesson lists confusing 1961, 1972 and 1984 as a common mistake. Which change came with the referendum?"),
        MC("Which statement best explains why Cameroon moved from a federal to a unitary state by 1972, according to the essay plan in the lesson?", [
            C("Central leadership and the single party drove the change, and the referendum gave it legal form", correct=True),
            C("The federated states asked to be abolished because they were bankrupt", why="The lesson mentions cost savings as an argument of supporters, not a request by the states."),
            C("The UN ordered Cameroon to become unitary", why="The UN had no such role after 1961; the change came through a national referendum."),
            C("The 1990 multiparty laws required a unitary state", why="The 1990 laws came eighteen years after the 1972 change."),
        ], steps=[S("Weigh the causes", text="A centralizing 1961 design, the single party from 1966 and Ahidjo's aim of unity drove the change; the 1972 referendum gave it legal form, though its legitimacy is still debated.")],
           concept="Causes of the 1972 unitary state", skill="Reasoning",
           hint="Consider who held power after 1966 and what the 1972 vote added."),
        MC("What happened in November 1982?", [
            C("Ahidjo resigned and Prime Minister Paul Biya became President as the constitution provided", correct=True),
            C("Biya won a contested multiparty presidential election", why="The first multiparty presidential election was in October 1992."),
            C("An attempted coup removed Ahidjo", why="Ahidjo resigned; the failed coup attempt came in April 1984."),
            C("The CNU was renamed the CPDM", why="That happened at the Bamenda congress of 1985."),
        ], steps=[S("Recall the transition", text="Ahidjo resigned in November 1982 and Biya succeeded him constitutionally; Ahidjo kept the CNU chairmanship for a time.")],
           concept="The 1982 transition", skill="Recall",
           hint="Biya was Prime Minister at the time. How does a constitution normally handle a resignation?"),
        MC("Which combination of factors does the lesson give for political liberalization in the early 1990s?", [
            C("Economic crisis, the end of the Cold War, external pressure for democracy and domestic mobilization", correct=True),
            C("A sovereign national conference that removed the ruling party", why="No sovereign national conference was held; the government held a tripartite meeting instead."),
            C("The 1996 constitution", why="The 1996 constitution came after liberalization, not before it."),
            C("The 1972 referendum", why="The 1972 referendum created the unitary state; it is not a cause of 1990s liberalization."),
        ], steps=[S("List the causes", text="Economic crisis from the late 1980s and external pressure opened the way; the SDF launch and villes mortes added domestic pressure.")],
           concept="Causes of 1990s liberalization", skill="Reasoning",
           hint="The lesson's essay plan groups the causes into economic, external and domestic."),
        MC("Which provision belongs to the constitution of January 1996?", [
            C("A decentralized unitary state with regions, a Senate, a Constitutional Council and a seven-year presidential term", correct=True),
            C("A return to two federated states", why="The 1996 constitution kept the unitary state; the All Anglophone Conference of 1993 had called for federalism."),
            C("The creation of the single party", why="The single party was formed in 1966; multiparty politics had returned in 1990."),
            C("Abolition of the presidency in favour of a prime minister", why="The constitution set a seven-year presidential term."),
        ], steps=[S("Recall the main provisions", text="The 1996 constitution kept the unitary state but called it decentralized, with regions, a Senate, a Constitutional Council and a seven-year term.")],
           concept="The 1996 constitution", skill="Recall",
           hint="It kept the unitary state but described it in a new way."),
    ]))

# ---------------------------------------------------------------------------
# 4. Constitutional transfers
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_DEC, topic="Constitutional transfers",
    title="Ghana, Nigeria and French Africa", lesson="constitutional-transfers",
    questions=[
        MC("What does 'constitutional decolonization' mean?", [
            C("The gradual transfer of power through new constitutions, wider voting rights, elected ministers and finally independence", correct=True),
            C("Independence won mainly through guerrilla war", why="That describes armed liberation, as in Algeria or Kenya, not constitutional transfer."),
            C("The immediate grant of independence without any elections", why="Constitutional decolonization worked through staged elections and reforms."),
            C("Direct UN government of a colony", why="The UN supervised trust territories but did not govern colonies directly."),
        ], steps=[S("Recall the definition", text="Power passes step by step through legal reforms: constitutions, suffrage, elected ministers, self-government, independence.")],
           concept="Constitutional decolonization", skill="Concept",
           hint="The key word is gradual: think of a series of legal steps."),
        MC("What was 'Positive Action' in the Gold Coast?", [
            C("The CPP's campaign of strikes and boycotts launched in January 1950", correct=True),
            C("The British reform plan drawn up by the Coussey Committee", why="Coussey proposed reforms for Britain; Positive Action was the CPP's campaign of pressure."),
            C("The armed rising of the Kenya Land and Freedom Army", why="That was Mau Mau in Kenya."),
            C("The 1948 founding of the UGCC", why="The UGCC was founded in 1947; Positive Action came in 1950 from Nkrumah's breakaway CPP."),
        ], steps=[S("Recall Positive Action", text="Nkrumah's CPP launched strikes and boycotts in January 1950 to press for self-government; Nkrumah was imprisoned.")],
           concept="Nkrumah, the CPP and Positive Action", skill="Recall",
           hint="It was a non-violent campaign by the party that demanded 'self-government now'."),
        MC("Why was Nkrumah released from prison and made Leader of Government Business?", [
            C("His CPP won the 1951 election", correct=True),
            C("The Accra riots forced Britain to grant immediate independence", why="The 1948 riots led to the Watson Commission and the Coussey Committee, not immediate independence."),
            C("The UGCC chose him as its leader", why="Nkrumah had broken away from the UGCC to form the CPP in 1949."),
            C("Ghana had already become independent", why="Independence came later, on 6 March 1957."),
        ], steps=[S("Link election and office", text="After the CPP's 1951 election victory Britain chose to work with it, releasing Nkrumah; he became Prime Minister in 1952.")],
           concept="Gold Coast route to independence", skill="Reasoning",
           hint="What event in 1951 showed Britain where popular support lay?"),
        MC("Which leader and party were strongest in Nigeria's Western Region?", [
            C("Obafemi Awolowo and the Action Group", correct=True),
            C("Nnamdi Azikiwe and the NCNC", why="The NCNC was strongest in the East."),
            C("Ahmadu Bello and the Northern People's Congress", why="The NPC dominated the North."),
            C("Abubakar Tafawa Balewa and the CPP", why="Balewa became federal Prime Minister in 1960; the CPP was Nkrumah's party in the Gold Coast."),
        ], steps=[S("Match region, party and leader", text="East: NCNC (Azikiwe). West: Action Group (Awolowo). North: NPC (Ahmadu Bello).")],
           concept="Regional parties in Nigeria", skill="Recall",
           hint="Each region had its own dominant party. Eliminate the East and the North first."),
        MC("Why was Nigeria's road to independence slower and more staged than Ghana's?", [
            C("Regional diversity and regionally based parties led to a federation with regional self-government at different dates", correct=True),
            C("Nigeria fought a long armed war against Britain", why="Nigeria's transfer was constitutional, through conferences and elections."),
            C("Britain refused to hold any elections in Nigeria", why="Elections and constitutions (1946, 1951, 1954) built up the regions."),
            C("Nigeria joined the French Community in 1958", why="The French Community was for French territories only."),
        ], steps=[S("Compare structures", text="Ghana was unitary with one mass party; Nigeria's 1954 federation and regional parties meant the East and West gained self-government in 1957 and the North in 1959.")],
           concept="Comparing Ghana and Nigeria", skill="Reasoning",
           hint="Think about size, regions and how many dominant parties there were."),
        MC("What did the Loi-Cadre of June 1956 do?", [
            C("Introduced universal adult suffrage in a single electoral college and gave each territory an elected executive council", correct=True),
            C("Gave the French African territories independence", why="A common mistake: it gave internal autonomy, not independence."),
            C("Created the French Community by referendum", why="The Community came from the 1958 referendum under de Gaulle."),
            C("Strengthened the federations of French West and Equatorial Africa", why="Critics such as Senghor said it shifted power to individual territories and 'balkanized' the federations."),
        ], steps=[S("Recall the Loi-Cadre", text="Associated with Gaston Defferre, it brought universal suffrage and territorial executive councils, giving internal autonomy.")],
           concept="The 1956 Loi-Cadre", skill="Recall",
           hint="It reformed voting and territorial government, but stopped short of the final step."),
        MC("What were the consequences of Guinea's No vote in the 1958 referendum?", [
            C("Immediate independence on 2 October 1958 and an abrupt withdrawal of French officials and aid", correct=True),
            C("Guinea became a founding member of the French Community", why="A Yes vote meant joining the Community; Guinea voted No."),
            C("France sent troops to reverse the result", why="The lesson describes France withdrawing officials and aid, not a military intervention."),
            C("Guinea had to wait until 1960 for independence like the others", why="Guinea became independent at once; the Yes territories became independent around 1960."),
        ], steps=[S("Follow the referendum terms", text="A No meant immediate independence and the loss of French support; Guinea under Sékou Touré became independent on 2 October 1958.")],
           concept="Guinea's No in 1958", skill="Reasoning",
           hint="Recall what a No vote meant under the terms de Gaulle set."),
        MC("Senghor and others criticised the Loi-Cadre as 'balkanization'. What did they mean?", [
            C("It shifted power to individual territories and weakened the federations of French West and Equatorial Africa", correct=True),
            C("It caused war between territories, as in the Balkans", why="The criticism concerned political fragmentation of the federations, not war."),
            C("It united all French territories into one state", why="It did the opposite, strengthening each territory separately."),
            C("It handed territories to Britain", why="The Loi-Cadre was a French reform within French Africa."),
        ], steps=[S("Interpret the term", text="Balkanization means breaking a larger unit into small separate units; the Loi-Cadre gave power to territories rather than the federations.")],
           concept="Balkanization critique of French policy", skill="Interpretation",
           hint="Think of the federations of French West and Equatorial Africa. Did the reform strengthen them or the individual territories?"),
    ]))

# ---------------------------------------------------------------------------
# 5. Armed liberation
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_DEC, topic="Armed liberation",
    title="Algeria, Kenya, the Portuguese colonies and Zimbabwe", lesson="armed-liberation",
    questions=[
        MC("Which feature, common to Algeria, Kenya, Southern Rhodesia, Angola and Mozambique, helps explain why decolonization there was violent?", [
            C("A large, politically powerful European settler population that resisted majority rule", correct=True),
            C("The absence of any nationalist movement", why="Each had strong nationalist movements, such as the FLN, Mau Mau, ZANU and FRELIMO."),
            C("Early agreement by the colonial power to independence", why="In these cases the colonial power or settlers refused reform for a long time."),
            C("Membership of the French Community", why="Only Algeria was French, and it was treated as part of France, not a Community member."),
        ], steps=[S("Recall the definition", text="A settler colony had a powerful European population that owned land and blocked majority rule.")],
           concept="Settler colonies and armed struggle", skill="Concept",
           hint="Think about who owned the land and resisted reform in these territories."),
        MC("Why did France resist Algerian independence so strongly?", [
            C("Algeria was legally part of France and had about a million European settlers", correct=True),
            C("Algeria was a UN trust territory", why="Algeria was legally part of France, not a trust territory."),
            C("Algeria had voted Yes in the 1958 referendum", why="The lesson links French resistance to Algeria's legal status and settlers, not to the referendum."),
            C("The FLN had accepted French rule after Sétif", why="The 1945 Sétif repression hardened nationalist opinion; the FLN launched war in 1954."),
        ], steps=[S("Identify the status and settlers", text="Because Algeria was treated as part of France with a large settler population, France saw it differently from colonies it could leave.")],
           concept="Algeria's status and the war of 1954 to 1962", skill="Reasoning",
           hint="Compare how France viewed Algeria with how it viewed its other African territories."),
        MC("Which agreement led to a referendum and Algerian independence on 5 July 1962?", [
            C("The Evian Accords", correct=True),
            C("The Lancaster House Agreement", why="Lancaster House (1979) led to Zimbabwe's independence."),
            C("The Loi-Cadre", why="The Loi-Cadre of 1956 reformed territorial government in French black Africa."),
            C("The Dayton Agreement", why="Dayton (1995) ended the Bosnian war."),
        ], steps=[S("Recall the settlement", text="De Gaulle moved towards self-determination; the Evian Accords of March 1962 led to a referendum and independence.")],
           concept="Evian Accords and Algerian independence", skill="Recall",
           hint="The agreement is named after a French spa town."),
        MC("Mau Mau was largely defeated militarily by 1956, yet Kenya became independent in 1963. How does the lesson explain this?", [
            C("Its significance lay in changing British policy, helped by outrage at events such as the Hola camp killings", correct=True),
            C("Mau Mau won a final military victory in 1962", why="A common mistake: the rising was largely defeated by 1956."),
            C("Kenya was handed to the UN Trusteeship Council", why="Kenya was a British colony; Lancaster House conferences led to majority rule."),
            C("Kenyatta led the Mau Mau army to Nairobi", why="Kenyatta was imprisoned after the Kapenguria trial, and his link to Mau Mau was disputed."),
        ], steps=[S("Separate military and political outcomes", text="Militarily defeated, Mau Mau and the abuses of the Emergency made continued rule costly; Lancaster House conferences in 1960 and 1962 led to majority rule.")],
           concept="Mau Mau and the change in British policy", skill="Interpretation",
           hint="Distinguish winning battles from changing a government's mind."),
        MC("Which movement was led by Amílcar Cabral?", [
            C("PAIGC in Guinea-Bissau", correct=True),
            C("FRELIMO in Mozambique", why="FRELIMO was led first by Eduardo Mondlane and later by Samora Machel."),
            C("MPLA in Angola", why="The lesson names the MPLA as an Angolan movement but not Cabral as its leader; Cabral led the PAIGC."),
            C("ZANU in Rhodesia", why="ZANU was led by Sithole and later Mugabe."),
        ], steps=[S("Match leader and movement", text="Cabral led the PAIGC in Guinea-Bissau.")],
           concept="Movements in the Portuguese colonies", skill="Recall",
           hint="Guinea-Bissau's war began in 1963."),
        MC("'Events in Portugal, not in Africa, ended Portuguese rule.' Which judgement does the lesson reach on this claim?", [
            C("The 1974 coup was the trigger, but African armed struggle was the underlying cause", correct=True),
            C("The coup had nothing to do with Africa", why="Officers turned against the regime because of long, costly African wars."),
            C("Portugal gave independence in 1961 before the wars began", why="Wars began in 1961 to 1964; independence came in 1974 to 1975."),
            C("The UN forced Portugal out by military action", why="UN pressure added to isolation, but the lesson does not describe UN military action."),
        ], steps=[S("Weigh trigger and cause", text="The Carnation Revolution of 25 April 1974 led directly to independence, but the cost of the wars helped cause the coup.")],
           concept="The Carnation Revolution and Portuguese decolonization", skill="Interpretation",
           hint="Why did Portuguese officers turn against their own government?"),
        MC("What was UDI in Southern Rhodesia?", [
            C("The Unilateral Declaration of Independence by Ian Smith's white minority government on 11 November 1965", correct=True),
            C("The union of ZANU and ZAPU", why="ZAPU and ZANU were separate movements; UDI was the settlers' rebellion."),
            C("A British grant of majority rule", why="UDI was made against Britain to avoid majority rule."),
            C("The 1979 peace settlement", why="That was the Lancaster House Agreement."),
        ], steps=[S("Recall UDI", text="Smith's minority government declared independence unilaterally in 1965, triggering the guerrilla war of the Second Chimurenga.")],
           concept="UDI and the Second Chimurenga", skill="Recall",
           hint="The letters stand for something done by one side alone."),
        MC("Why did the guerrilla war in Rhodesia intensify in the 1970s?", [
            C("Mozambique's independence gave ZANU bases", correct=True),
            C("Britain sent troops to support ZANU", why="The lesson gives no such intervention; Britain later brokered Lancaster House."),
            C("The Smith government accepted majority rule", why="Majority rule came only after Lancaster House and the 1980 elections."),
            C("ZAPU and ZANU stopped fighting", why="Both waged guerrilla war; the war intensified rather than eased."),
        ], steps=[S("Link regional change", text="After Mozambique became independent in June 1975, ZANU could operate from bases there.")],
           concept="External bases in the Zimbabwean struggle", skill="Reasoning",
           hint="Which neighbouring country became independent in 1975?"),
    ]))

# ---------------------------------------------------------------------------
# 6. South Africa
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_DEC, topic="South Africa",
    title="Apartheid and resistance, 1948 to 1994", lesson="south-africa-anti-apartheid-struggle",
    questions=[
        MC("Which statement about the origins of apartheid is correct?", [
            C("Segregation was older, but apartheid as a legal system dates from the National Party victory of 1948", correct=True),
            C("Apartheid began with the first colonial settlement", why="A common mistake: segregation was older, but apartheid as a legal system began in 1948."),
            C("Apartheid was introduced by Britain in 1910", why="The lesson links apartheid to the National Party government elected in 1948."),
            C("Apartheid was introduced after Sharpeville in 1960", why="Key apartheid laws had already been passed in 1950 and 1953."),
        ], steps=[S("Date the system", text="The National Party under D. F. Malan won in 1948 and passed the key apartheid laws from 1950.")],
           concept="Definition and origins of apartheid", skill="Concept",
           hint="Which party's election victory began the legal system?"),
        MC("Which apartheid law segregated residential areas?", [
            C("Group Areas Act (1950)", correct=True),
            C("Population Registration Act (1950)", why="This classified people by race; the Group Areas Act decided where they could live."),
            C("Bantu Education Act (1953)", why="This created separate, inferior schooling for Africans."),
            C("Suppression of Communism Act (1950)", why="This was used against political opponents, not to divide residential areas."),
        ], steps=[S("Match law and purpose", text="The Group Areas Act of 1950 segregated where people of each race could live.")],
           concept="Key apartheid laws", skill="Recall",
           hint="The name of the law refers to areas."),
        MC("Under Verwoerd's policy of 'separate development', how were Africans treated?", [
            C("As citizens of homelands (Bantustans) rather than of South Africa", correct=True),
            C("As full citizens of South Africa with equal votes", why="Separate development denied Africans South African citizenship rights."),
            C("As citizens of neighbouring independent states", why="The homelands were created inside South Africa's system, not neighbouring states."),
            C("As members of the Commonwealth with British passports", why="The lesson does not connect separate development with Commonwealth status."),
        ], steps=[S("Recall separate development", text="Homelands were created and Africans were treated as their citizens, not as citizens of South Africa.")],
           concept="Separate development and the homelands", skill="Recall",
           hint="Think of the territories also called Bantustans."),
        MC("What was the most important consequence of the Sharpeville shootings of 21 March 1960 for the ANC's methods?", [
            C("The banning of the ANC and PAC led to the turn to armed struggle with Umkhonto we Sizwe in 1961", correct=True),
            C("The ANC adopted the Freedom Charter", why="The Freedom Charter was adopted at Kliptown in 1955, before Sharpeville."),
            C("Mandela was immediately released", why="Mandela was sentenced to life imprisonment in 1964 and released only in 1990."),
            C("The government ended the pass laws", why="The government responded with repression and banned the ANC and PAC."),
        ], steps=[S("Follow the sequence", text="Police killed 69 people at a PAC anti-pass protest; the ANC and PAC were banned; the ANC formed an armed wing in 1961.")],
           concept="Sharpeville and the turn to armed struggle", skill="Reasoning",
           hint="Once peaceful legal organisations were banned, what alternative was left?"),
        MC("How did the PAC differ from the ANC?", [
            C("It broke away in 1959 and rejected the multiracial alliance of the Freedom Charter", correct=True),
            C("It was the ANC's armed wing", why="The ANC's armed wing was Umkhonto we Sizwe, formed in 1961."),
            C("It was founded by Steve Biko in the 1970s", why="Biko is associated with the Black Consciousness Movement; the PAC was led by Robert Sobukwe."),
            C("It supported the National Party", why="The PAC opposed apartheid; it organised the Sharpeville anti-pass protest."),
        ], steps=[S("Recall the split", text="Robert Sobukwe's PAC broke away from the ANC in 1959, rejecting the Freedom Charter's multiracial alliance.")],
           concept="ANC and PAC compared", skill="Concept",
           hint="The split was about the Freedom Charter's alliance with other groups."),
        MC("What sparked the Soweto uprising of 16 June 1976?", [
            C("Student protest against Afrikaans-medium teaching", correct=True),
            C("Police shooting at an anti-pass protest", why="That describes Sharpeville in 1960."),
            C("The death of Steve Biko", why="Biko died in police custody in 1977, after the uprising began."),
            C("The release of Nelson Mandela", why="Mandela was released on 11 February 1990."),
        ], steps=[S("Recall Soweto", text="Students inspired by Black Consciousness protested against teaching in Afrikaans.")],
           concept="Soweto 1976 and Black Consciousness", skill="Recall",
           hint="The protesters were school students. What were they objecting to in their lessons?"),
        MC("Which international measure was imposed by the UN Security Council in 1977?", [
            C("A mandatory arms embargo", correct=True),
            C("Full trade sanctions by all members", why="In the 1980s many states and companies imposed sanctions or withdrew investment; the 1977 measure was an arms embargo."),
            C("Expulsion of South Africa from the UN", why="The lesson does not describe an expulsion; the 1977 measure was an arms embargo."),
            C("A peacekeeping force in Soweto", why="No UN force was sent; the measure was an arms embargo."),
        ], steps=[S("Recall international pressure", text="The Security Council imposed a mandatory arms embargo in 1977; wider sanctions and disinvestment followed in the 1980s.")],
           concept="International pressure and sanctions", skill="Recall",
           hint="It concerned the supply of weapons."),
        MC("A historian argues that the end of the Cold War was a key reason apartheid ended through negotiation. What is the argument?", [
            C("The government could no longer present itself as a Western bulwark against the 'communist threat'", correct=True),
            C("The USSR invaded South Africa in 1989", why="No such invasion happened; the point is about the loss of an argument used by the government."),
            C("The Cold War ended because of the Soweto uprising", why="This reverses cause and effect and is not in the lesson."),
            C("The ANC stopped all resistance in 1989", why="Internal resistance continued; negotiations went on amid serious violence."),
        ], steps=[S("Explain the link", text="After 1989 the 'communist threat' argument lost force, encouraging negotiation; de Klerk unbanned the ANC on 2 February 1990.")],
           concept="Why apartheid ended: Cold War change", skill="Interpretation",
           hint="What justification had the apartheid government used to win Western support?"),
    ]))

# ---------------------------------------------------------------------------
# 7. Cold War geopolitics
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CW, topic="Cold War geopolitics",
    title="Containment, deterrence and the Global South", lesson="cold-war-geopolitics",
    questions=[
        MC("What was containment?", [
            C("The US policy of preventing the spread of Soviet influence and communism", correct=True),
            C("The Soviet policy of keeping Eastern Europe out of the Marshall Plan", why="The USSR did refuse Marshall aid, but containment was a US policy."),
            C("The idea that neither side would attack because of certain retaliation", why="That is nuclear deterrence."),
            C("The policy of new states avoiding both blocs", why="That is non-alignment."),
        ], steps=[S("Recall the definition", text="Containment, associated with George Kennan's analysis of 1946 to 1947, aimed to stop Soviet influence spreading.")],
           concept="Containment", skill="Concept",
           hint="It is associated with the US diplomat George Kennan."),
        MC("What did the Truman Doctrine of March 1947 promise?", [
            C("Support for 'free peoples' resisting subjugation, starting with aid to Greece and Turkey", correct=True),
            C("Large-scale economic aid to rebuild all of Western Europe", why="That describes the Marshall Plan of June 1947."),
            C("A military alliance, NATO", why="NATO was founded in April 1949."),
            C("Withdrawal of US forces from Europe", why="The doctrine increased US commitment abroad."),
        ], steps=[S("Recall the doctrine", text="Truman asked Congress for aid to Greece and Turkey and pledged support for free peoples.")],
           concept="Truman Doctrine", skill="Recall",
           hint="Two Mediterranean countries were named in Truman's request to Congress."),
        MC("How did the Marshall Plan differ from the Truman Doctrine, according to the lesson's essay plan?", [
            C("The Doctrine was military and political; the Plan was economic and open in principle to all", correct=True),
            C("The Plan was military; the Doctrine was purely economic", why="This reverses the two."),
            C("The Plan was Soviet; the Doctrine was American", why="Both were US policies; the USSR refused Marshall aid."),
            C("They had opposite aims, one for and one against communism", why="Both aimed to contain communist influence."),
        ], steps=[S("Compare means and aims", text="Same purpose of containment; different means: political and military commitment versus economic recovery.")],
           concept="Marshall Plan and Truman Doctrine compared", skill="Reasoning",
           hint="Ask what each one actually provided: promises of support, or money for recovery?"),
        MC("Which events of 1948 to 1949 confirmed the division of Europe?", [
            C("The Berlin Blockade and airlift, the founding of NATO and the first Soviet atomic test", correct=True),
            C("The Cuban Missile Crisis and the hotline", why="These came in 1962 and 1963."),
            C("The Korean War and the Warsaw Pact", why="The Korean War began in 1950 and the Warsaw Pact formed in 1955."),
            C("The Bandung Conference and the Non-Aligned Movement", why="These came in 1955 and 1961 and concerned new states avoiding the blocs."),
        ], steps=[S("Recall the sequence", text="Berlin Blockade (1948 to 1949), NATO (April 1949) and the Soviet atomic test (August 1949).")],
           concept="Origins of the Cold War, 1945 to 1949", skill="Recall",
           hint="Look for the option in which every event falls in 1948 or 1949."),
        MC("Why is mutually assured destruction (MAD) said to have deterred direct war between the superpowers?", [
            C("Each side expected devastating retaliation if it attacked, because both could destroy each other", correct=True),
            C("Neither side had nuclear weapons", why="Both had them; the USSR tested its first atomic bomb in 1949."),
            C("The UN had banned war between permanent members", why="Deterrence rested on fear of retaliation, not on a UN rule."),
            C("Both sides had agreed to share their weapons", why="There was an arms race, later limited by treaties such as SALT I."),
        ], steps=[S("Apply the definition", text="Deterrence: no attack if devastating retaliation is expected. When both could destroy each other, this was MAD.")],
           concept="Nuclear deterrence and MAD", skill="Concept",
           hint="Think about what would happen to the attacker."),
        MC("Which measures followed the Cuban Missile Crisis and formed part of detente?", [
            C("The hotline and Partial Test Ban Treaty (1963), the Non-Proliferation Treaty (1968) and SALT I (1972)", correct=True),
            C("The Marshall Plan and the Truman Doctrine", why="These came in 1947, at the start of the Cold War."),
            C("The founding of NATO and the Warsaw Pact", why="These alliances deepened the division rather than easing tension."),
            C("The Berlin Blockade and airlift", why="This was a crisis of 1948 to 1949, not an easing of tension."),
        ], steps=[S("Recall detente", text="After Cuba in 1962, a hotline (1963) and treaties in 1963, 1968 and 1972 marked a period of easing tension.")],
           concept="Detente and arms control", skill="Recall",
           hint="Detente means easing of tension. Which option lists agreements rather than crises?"),
        MC("Which example shows superpower rivalry in Africa, according to the lesson?", [
            C("The Angolan civil war from 1975, with Cuban troops and US and South African involvement", correct=True),
            C("The Berlin Blockade", why="That crisis was in Europe."),
            C("The Bandung Conference", why="Bandung expressed new states' wish to avoid choosing sides."),
            C("The Korean War", why="That was in Asia."),
        ], steps=[S("Recall African arenas", text="The Congo crisis, the Angolan civil war and the Ogaden war of 1977 to 1978 were African arenas of rivalry.")],
           concept="Cold War rivalry in Africa", skill="Application",
           hint="Look for the conflict located on the African continent with foreign troops involved."),
        MC("Which school of historians blames US economic interests and aggressive policy, including the atomic bomb and the Marshall Plan, for the Cold War?", [
            C("Revisionist", correct=True),
            C("Orthodox", why="Orthodox historians blamed Soviet expansionism and saw the US as defensive."),
            C("Post-revisionist", why="Post-revisionists, associated with Gaddis, stress mutual misperception and security fears."),
            C("Non-aligned", why="Non-alignment was a foreign-policy stance of new states, not a school of historians."),
        ], steps=[S("Match the view to the school", text="Orthodox: Soviet expansionism. Revisionist (from the 1960s): US economic interests and aggression. Post-revisionist: mutual misperception.")],
           concept="Historiography of the Cold War", skill="Interpretation",
           hint="This school revised the earlier view that the US was only reacting defensively."),
    ]))

# ---------------------------------------------------------------------------
# 8. The United Nations
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CW, topic="The United Nations",
    title="The UN Charter, Security Council and peacekeeping", lesson="the-united-nations",
    questions=[
        MC("Which is NOT one of the six principal organs of the United Nations?", [
            C("The Peace and Security Council", correct=True),
            C("The Trusteeship Council", why="The Trusteeship Council is a principal organ; it supervised both Cameroons."),
            C("The International Court of Justice", why="The ICJ is a principal organ."),
            C("The Economic and Social Council", why="ECOSOC is a principal organ."),
        ], steps=[S("List the six organs", text="General Assembly, Security Council, Economic and Social Council, Trusteeship Council, International Court of Justice and Secretariat. The Peace and Security Council belongs to the African Union.")],
           concept="Principal organs of the UN", skill="Recall",
           hint="One of these bodies belongs to a regional African organisation, not the UN."),
        NUM("How many members has the UN Security Council had since the enlargement that took effect in 1965?", 15,
            steps=[S("Add permanent and elected members", text="Five permanent members plus ten elected members gives fifteen.")],
            concept="Composition of the Security Council", skill="Recall",
            hint="Add the permanent members to the elected members."),
        MC("What is the veto in the Security Council?", [
            C("The power of each of the five permanent members to block any substantive resolution", correct=True),
            C("The power of the General Assembly to overrule the Security Council", why="The veto belongs to the permanent members of the Council, not the Assembly."),
            C("The power of any of the fifteen members to block a resolution", why="Only the five permanent members hold a veto."),
            C("The Secretary-General's power to stop a peacekeeping mission", why="The veto is held by states, not by the Secretary-General."),
        ], steps=[S("Recall the definition", text="China, France, the USSR/Russia, the United Kingdom and the United States can each block substantive resolutions.")],
           concept="The veto", skill="Concept",
           hint="It is a privilege of a small group of members."),
        MC("Which chapter of the UN Charter allows the Security Council to order sanctions or military action?", [
            C("Chapter VII", correct=True),
            C("Chapter VI", why="Chapter VI covers the peaceful settlement of disputes."),
            C("Chapter XII", why="Chapter XII deals with the trusteeship system."),
            C("Chapter I", why="Chapter I sets out purposes and principles."),
        ], steps=[S("Distinguish VI and VII", text="Chapter VI: peaceful settlement. Chapter VII: sanctions or military action against threats to peace.")],
           concept="Chapters VI and VII of the Charter", skill="Recall",
           hint="It is the chapter after the one on peaceful settlement."),
        MC("Why was the Security Council often paralysed during the Cold War?", [
            C("Permanent members on opposing sides used the veto to block action", correct=True),
            C("It had no permanent members until 1965", why="The five permanent members existed from 1945; 1965 enlarged the elected seats."),
            C("The General Assembly could veto its decisions", why="The Assembly has no veto over the Council."),
            C("The UN had its own army that refused to act", why="The UN has no army of its own and depends on member states for troops."),
        ], steps=[S("Link structure to outcome", text="With the US and USSR both holding vetoes, resolutions opposed by either side were blocked.")],
           concept="Cold War limits on the Security Council", skill="Reasoning",
           hint="Both superpowers were permanent members. What could each do to the other's proposals?"),
        MC("Which statement best sums up the lesson's judgement on the UN operation in the Congo (ONUC), 1960 to 1964?", [
            C("Partial success: it ended Katanga's secession and kept the Congo united, at a high cost to the UN's reputation and finances", correct=True),
            C("Complete success: it protected Lumumba and stabilised the government", why="Lumumba was killed in 1961 and the operation was deeply controversial."),
            C("Complete failure: Katanga became independent", why="ONUC ended the Katanga secession in 1963."),
            C("It was a NATO operation, not a UN one", why="ONUC was a UN force requested by the Congolese government."),
        ], steps=[S("Weigh success and failure", text="Territorial unity was preserved, but Lumumba's killing, Hammarskjöld's death and Soviet accusations damaged the UN.")],
           concept="UN peacekeeping in the Congo", skill="Interpretation",
           hint="Consider both what happened to Katanga and what happened to Lumumba."),
        MC("What did the Security Council do when the genocide against the Tutsi began in Rwanda in April 1994?", [
            C("It reduced the UNAMIR force rather than strengthening it", correct=True),
            C("It sent a large Chapter VII force within days", why="The Council reduced the small mission instead."),
            C("It ordered NATO air strikes", why="NATO air strikes are linked in the lesson to Bosnia in 1995."),
            C("It declared Kigali a safe area defended by UNPROFOR", why="UNPROFOR and safe areas belong to the former Yugoslavia."),
        ], steps=[S("Recall Rwanda", text="UNAMIR, under General Dallaire, was small; the Council cut it, and hundreds of thousands were killed in about one hundred days.")],
           concept="UN failure in Rwanda", skill="Recall",
           hint="Did the Council respond by adding troops or removing them?"),
        MC("Which argument supports the 'defensive view' of UN peacekeeping?", [
            C("Failures reflect the choices of powerful member states, and missions in Mozambique or Namibia helped end conflicts", correct=True),
            C("Srebrenica shows the UN failing to protect civilians", why="This is evidence for the critical view."),
            C("The Security Council reduced UNAMIR in 1994", why="This also supports the critical view, though defenders blame member states for it."),
            C("The UN accepted French and British choices in Cameroon", why="This is a criticism of the UN's role in decolonization, not a defence of peacekeeping."),
        ], steps=[S("Sort the evidence", text="Critical view: Rwanda and Srebrenica. Defensive view: member states made the choices, and some missions succeeded.")],
           concept="Assessing UN peacekeeping", skill="Interpretation",
           hint="A defence either shifts the blame or points to successes."),
    ]))

# ---------------------------------------------------------------------------
# 9. Regional integration
# ---------------------------------------------------------------------------
SETS.append(practice_set(
    module=M_CW, topic="Regional integration",
    title="OAU, AU and regional economic communities", lesson="regional-integration",
    questions=[
        MC("Where and when was the OAU founded?", [
            C("Addis Ababa, 25 May 1963", correct=True),
            C("Durban, 2002", why="Durban 2002 was the launch of the African Union."),
            C("Lagos, May 1975", why="The Treaty of Lagos of 1975 founded ECOWAS."),
            C("Sirte, September 1999", why="The Sirte Declaration of 1999 called for the new African Union."),
        ], steps=[S("Recall the founding", text="The OAU was founded at Addis Ababa on 25 May 1963.")],
           concept="Founding of the OAU", skill="Recall",
           hint="The city is the capital of Ethiopia."),
        MC("Which approach did the OAU adopt in 1963?", [
            C("Cooperation between sovereign states rather than a single government, the moderate approach", correct=True),
            C("Rapid political union under one continental government", why="That was the aim of the more radical Casablanca group, which the OAU did not adopt."),
            C("A right to intervene in member states in cases of genocide", why="That right came with the AU's Constitutive Act."),
            C("A single currency for the whole continent", why="The lesson describes no such OAU policy; the CFA franc is shared only by certain states."),
        ], steps=[S("Compare the groups", text="The Casablanca group wanted rapid union; the Monrovia group was gradualist. The OAU adopted the moderate approach.")],
           concept="Casablanca and Monrovia groups; OAU approach", skill="Concept",
           hint="Cameroon under Ahidjo was among the moderates, and the moderate view prevailed."),
        MC("What was the main consequence of the OAU's principle of non-interference?", [
            C("It said little about coups, civil wars and human rights abuses within member states", correct=True),
            C("It refused to support liberation movements in southern Africa", why="Its Liberation Committee did support movements against colonial and white minority rule."),
            C("It redrew colonial borders", why="In 1964 members agreed to respect the borders inherited from colonial rule."),
            C("It intervened militarily in Rwanda in 1994", why="Non-interference meant inaction on internal conflicts such as Rwanda."),
        ], steps=[S("Link principle and record", text="Non-interference protected sovereignty but left internal conflicts and abuses largely unaddressed.")],
           concept="Non-interference and the OAU's record", skill="Reasoning",
           hint="If you may not interfere in a state's internal affairs, what can you not respond to?"),
        MC("What is the main difference between the OAU and the African Union?", [
            C("The AU's Constitutive Act gives a right to intervene in grave circumstances such as genocide, war crimes and crimes against humanity", correct=True),
            C("The AU abolished the borders inherited from colonial rule", why="The lesson describes no such change; the shift was from non-interference to 'non-indifference'."),
            C("The AU has no member states, only regional communities", why="The AU, like the OAU, is made up of member states."),
            C("The OAU had a Peace and Security Council, which the AU abolished", why="The AU created a Peace and Security Council."),
        ], steps=[S("Compare the two", text="The OAU kept strict non-interference; the AU added a right of intervention in grave circumstances and a Peace and Security Council.")],
           concept="From OAU to AU: non-indifference", skill="Concept",
           hint="The change is summed up as moving from non-interference to 'non-indifference'."),
        MC("Which event influenced the AU's shift towards a right of intervention?", [
            C("The Rwandan genocide", correct=True),
            C("The Sharpeville shootings", why="Sharpeville in 1960 belongs to the South African struggle, decades earlier."),
            C("The Cuban Missile Crisis", why="That was a superpower crisis of 1962 unrelated to the AU's founding."),
            C("The devaluation of the CFA franc", why="That was a monetary event of January 1994, not a cause of the intervention principle."),
        ], steps=[S("Identify the influence", text="The OAU's inaction during the Rwandan genocide pushed African leaders towards 'non-indifference'.")],
           concept="Causes of the AU intervention principle", skill="Reasoning",
           hint="Think of the 1994 catastrophe that the OAU and the UN failed to stop."),
        MC("Which list gives the members of CEMAC?", [
            C("Cameroon, Central African Republic, Chad, Congo, Equatorial Guinea and Gabon", correct=True),
            C("Cameroon, Nigeria, Ghana, Senegal, Chad and Gabon", why="Nigeria, Ghana and Senegal are West African states, not members of the Central African CEMAC."),
            C("Cameroon, South Africa, Angola, Mozambique, Chad and Gabon", why="South Africa, Angola and Mozambique are southern African states, not members of the Central African CEMAC."),
            C("Cameroon, Central African Republic, Chad, Congo and Gabon only", why="This leaves out Equatorial Guinea; CEMAC has six members."),
        ], steps=[S("Recall CEMAC", text="Six members share the CFA franc issued by the BEAC, whose headquarters is in Yaoundé.")],
           concept="CEMAC membership", skill="Recall",
           hint="CEMAC is a Central African community with six members."),
        MC("Why was SADC's forerunner, the Southern African Development Coordination Conference, set up in 1980?", [
            C("Partly to reduce dependence on apartheid South Africa", correct=True),
            C("To share the CFA franc", why="The CFA franc in Central Africa is issued by the BEAC for CEMAC members."),
            C("To send ECOMOG troops into Liberia", why="ECOMOG was the ECOWAS monitoring group in West Africa."),
            C("To include South Africa as its founding leader", why="South Africa joined only in 1994, after apartheid ended."),
        ], steps=[S("Recall SADC's origins", text="The 1980 conference aimed partly to reduce dependence on apartheid South Africa; it became the Community in 1992 and South Africa joined in 1994.")],
           concept="Origins of SADC", skill="Reasoning",
           hint="Consider who ruled the region's most powerful economy in 1980."),
        MC("How did the end of the Cold War in 1991 affect African politics, according to the lesson?", [
            C("Western donors increasingly tied aid to democracy and economic reform, contributing to liberalization, including in Cameroon", correct=True),
            C("It ended all conflicts in Africa", why="The 1990s saw new wars in Liberia, Sierra Leone, Somalia and the Great Lakes region."),
            C("It led directly to the founding of the OAU", why="The OAU dated from 1963."),
            C("It made African states join the Warsaw Pact", why="The Soviet Union dissolved in December 1991; the lesson gives no such outcome."),
        ], steps=[S("Explain the change", text="With the Soviet Union gone, donors tied aid to democracy and reform, encouraging multiparty politics, though new conflicts also arose.")],
           concept="Africa after the Cold War", skill="Interpretation",
           hint="Think about the conditions attached to Western aid after 1991."),
    ]))
