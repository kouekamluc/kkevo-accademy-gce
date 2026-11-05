"""Form 5 History (GCE O Level): practice sets for African decolonization and the Cold War (one per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("history", "form-5")

MODULE = "World History since 1870"
DECOL = "African decolonization"
COLD = "Cold War"


def Q(prompt, right, wrongs, pos, step, concept, skill, hint, steps=None, feedback=""):
    """Build a 4-option question: `wrongs` is three (text, why) pairs; the right answer goes at index `pos`."""
    choices = [C(t, why=w) for t, w in wrongs]
    choices.insert(pos, C(right, correct=True))
    return MC(prompt, choices, steps or [S("Answer", text=step)], concept=concept, skill=skill, hint=hint, feedback=feedback)


SETS = []

# ---------------------------------------------------------------- 1. Why colonial rule ended
SETS.append(practice_set(
    module=MODULE, topic=DECOL,
    title="Causes of the end of colonial rule", lesson="why-colonial-rule-ended-in-africa",
    questions=[
        Q("Which of these was an external cause of African decolonization after 1945?",
          "The UN Charter's support for self-determination", [
              ("The founding of the OAU", "The OAU was founded in 1963 by states that were already independent."),
              ("The collapse of the USSR", "The USSR was dissolved in 1991, long after most colonies were free."),
              ("The activities of African trade unions", "Trade unions were an internal cause, because they were African organisations."),
          ], 2, "The UN Charter supported self-determination and gave nationalists a principle to quote.",
          "Causes of decolonization", "Reasoning", "An external cause comes from outside Africa and already existed around 1945."),
        Q("Which meeting in 1945 demanded independence for African colonies?",
          "The Pan-African Congress in Manchester", [
              ("The founding meeting of the OAU in Addis Ababa", "The OAU was founded in 1963."),
              ("The launch of the African Union in Durban", "The AU was launched in 2002."),
              ("The Foumban Conference", "Foumban (1961) was about Cameroon's constitution."),
          ], 0, "The Pan-African Congress held in Manchester in 1945 demanded independence for African colonies.",
          "African nationalism and Pan-Africanism", "Recall", "It was held in Britain in the year the Second World War ended."),
        Q("What is Pan-Africanism?",
          "The idea that Africans and people of African descent share interests and should unite", [
              ("A policy of staying out of both Cold War blocs", "That is non-alignment."),
              ("The system by which Europeans ruled colonies", "That is colonialism."),
              ("A trade agreement between neighbouring states", "That describes a regional economic body, not Pan-Africanism."),
          ], 1, "Pan-Africanism is the idea of unity among Africans and people of African descent. It inspired leaders such as Nkrumah.",
          "Pan-Africanism", "Concept", "The word 'Pan' means 'all'."),
        Q("Why did African ex-servicemen help the cause of decolonization?",
          "They returned from the war with new ideas and expectations of freedom", [
              ("They defeated the colonial armies in Africa", "The war was fought mainly abroad, and independence came later through politics and sometimes other wars."),
              ("They were paid by the UN to organise parties", "The UN did not pay ex-servicemen to found parties."),
              ("They formed the OAU", "The OAU was founded in 1963 by heads of independent states."),
          ], 3, "Many Africans served in the Second World War and came home with new ideas and expectations.",
          "Effects of the Second World War", "Reasoning", "Think about what soldiers saw abroad and what they expected when they came home."),
        Q("Which is an example of an economic grievance against colonial rule?",
          "Low prices paid to farmers for cash crops", [
              ("Foreign officials running the government", "This is a political grievance."),
              ("The Manchester Congress of 1945", "This was a political meeting, not an economic grievance."),
              ("India's independence in 1947", "This was an example from Asia that inspired nationalists, not a grievance."),
          ], 0, "Farmers received low prices for cash crops such as cocoa or coffee. Forced labour was another economic grievance.",
          "Economic and political grievances", "Concept", "An economic grievance is about money and work."),
        Q("Why did India's independence in 1947 matter to African nationalists?",
          "It showed that a large colony could win freedom", [
              ("It ended the Second World War", "The war ended in 1945."),
              ("It made Britain give independence to every African colony in 1947", "Most African colonies became independent from 1957 onwards."),
              ("It created the African Union", "The AU was launched in 2002."),
          ], 2, "India's independence showed that a colony could win freedom, and African nationalists took courage from it.",
          "Causes of decolonization", "Reasoning", "Think of it as an example others could follow."),
        Q("How did the attitude of the USA and the USSR after 1945 help decolonization?",
          "Both criticised old-style colonial empires", [
              ("Both gave independence to African colonies", "Neither superpower owned African colonies to give away."),
              ("Both joined the OAU", "The OAU was an African organisation."),
              ("Both wanted Britain and France to keep their empires", "Both superpowers criticised the old empires."),
          ], 1, "The superpowers criticised colonial empires, so Britain and France could not ignore the pressure.",
          "External causes", "Concept", "Were the superpowers in favour of old empires or not?"),
        Q("Which statement best sums up how historians explain the end of colonial rule?",
          "Both African action and the weakness of the colonial powers mattered, in different balance in each colony", [
              ("Only African nationalists caused it", "Many historians also stress the weakness and choices of the colonial powers."),
              ("Only the weakness of Britain and France caused it", "This ignores the work of nationalist leaders, parties and trade unions."),
              ("It was caused only by the OAU", "The OAU came in 1963, after many states were free."),
          ], 3, "Most historians combine internal and external causes and say that the balance differed from colony to colony.",
          "Historical interpretation", "Interpretation", "A balanced answer uses both sides."),
    ]))

# ---------------------------------------------------------------- 2. Peaceful and armed routes
SETS.append(practice_set(
    module=MODULE, topic=DECOL,
    title="Peaceful transfers and armed struggles", lesson="decolonization-peaceful-and-armed-routes",
    questions=[
        Q("Which country was the first colony south of the Sahara to become independent?",
          "Ghana, on 6 March 1957", [
              ("Algeria, in 1962", "Algeria is north of the Sahara and became independent after a war."),
              ("Kenya, in 1963", "Kenya became independent in 1963 after the Mau Mau uprising."),
              ("Nigeria, in 1960", "Nigeria became independent three years later."),
          ], 3, "Ghana (formerly the Gold Coast) became independent on 6 March 1957 under Kwame Nkrumah.",
          "Peaceful transfers", "Recall", "Its first leader was Kwame Nkrumah."),
        Q("Which pair of countries gained independence in 1960 through negotiation?",
          "Nigeria and Senegal", [
              ("Algeria and Kenya", "Both followed armed struggles and became independent in 1962 and 1963."),
              ("Angola and Mozambique", "They won independence in 1974–1975 after long wars."),
              ("Zimbabwe and Namibia", "They became independent in 1980 and 1990."),
          ], 0, "Nigeria and Senegal both became independent in 1960, mainly through negotiation.",
          "Peaceful transfers", "Recall", "Both became independent in the year 17 African countries were freed."),
        Q("Which movement fought France from 1954 until Algeria's independence in 1962?",
          "The FLN", [
              ("The Mau Mau", "The Mau Mau fought in Kenya."),
              ("The MPLA", "The MPLA was a movement in Angola."),
              ("The UPC", "The UPC was a nationalist party in Cameroon."),
          ], 2, "The FLN (National Liberation Front) fought France in Algeria from 1954 to 1962.",
          "Armed struggles", "Recall", "Its initials stand for National Liberation Front."),
        Q("What began in Kenya in 1952, and when did Kenya become independent?",
          "The Mau Mau uprising; independence in 1963", [
              ("The FLN war; independence in 1962", "The FLN fought in Algeria."),
              ("A peaceful transfer; independence in 1957", "1957 was the date of Ghana's independence."),
              ("The Lisbon revolution; independence in 1974", "The revolution was in Portugal and affected the Portuguese colonies."),
          ], 1, "The Mau Mau uprising began in 1952. Kenya became independent in 1963.",
          "Armed struggles", "Recall", "The uprising began eleven years before independence."),
        Q("Why did decolonization in Algeria involve armed struggle rather than a peaceful transfer?",
          "There were many European settlers and the colonial power resisted leaving", [
              ("Algeria was a UN trust territory", "Trusteeship was the status of territories such as Cameroon."),
              ("The OAU ordered armed struggle", "The OAU was founded in 1963, after the war had started in 1954."),
              ("There was no nationalist movement", "The FLN was a strong nationalist movement."),
          ], 0, "Armed struggle was likely where many settlers lived or the colonial power refused to leave.",
          "Peaceful transfer versus armed struggle", "Reasoning", "Compare who lived in Algeria with who lived in Ghana."),
        Q("What event led Portugal to end its colonial rule in Angola, Mozambique and Guinea-Bissau?",
          "A revolution in Lisbon in 1974", [
              ("The creation of the OAU in 1963", "Portugal kept its colonies for another eleven years."),
              ("The end of the Cold War in 1991", "These colonies were free by 1975."),
              ("Ghana's independence in 1957", "Ghana's example inspired nationalists but Portugal still refused to decolonize."),
          ], 3, "Portugal refused to decolonize until a revolution in Lisbon in 1974. Independence followed in 1974–1975.",
          "Portuguese colonies", "Reasoning", "The change came from inside Portugal."),
        NUM("How many African countries became independent in 1960?", 17,
            steps=[S("Recall", text="Seventeen African countries became independent in 1960, including Cameroon.")],
            concept="The year 1960", skill="Recall", hint="This is the number given for the year of independence in Africa.",
            feedback="Seventeen countries were free in 1960."),
        Q("Which statement about Cameroon's road to independence is best?",
          "It combined a constitutional route and the armed struggle of the UPC", [
              ("It was entirely peaceful, with no armed struggle", "The UPC fought an armed struggle."),
              ("It was entirely an armed struggle like Algeria", "A constitutional route led by Ahidjo also took place."),
              ("It happened in 1963, with Kenya", "French Cameroun became independent in 1960."),
          ], 1, "Cameroon's path combined both methods. Cameroonians and historians hold different views about this period.",
          "Cameroon and African decolonization", "Interpretation", "Remember that two different groups took two different methods."),
    ]))

# ---------------------------------------------------------------- 3. OAU to AU
SETS.append(practice_set(
    module=MODULE, topic=DECOL,
    title="The OAU and the African Union", lesson="oau-to-african-union",
    questions=[
        Q("Where and when was the OAU founded?",
          "Addis Ababa, 25 May 1963", [
              ("Durban, 9 July 2002", "This is the launch of the African Union."),
              ("Addis Ababa, 9 July 2002", "The city is right but the date belongs to the AU's launch in Durban."),
              ("Accra, 6 March 1957", "This is Ghana's independence."),
          ], 0, "OAU: Addis Ababa, 25 May 1963. AU: Durban, 9 July 2002.",
          "The OAU", "Recall", "It was founded in Ethiopia, three years after Cameroon's independence."),
        Q("Which was an aim of the OAU?",
          "To defend the sovereignty and territorial integrity of its members", [
              ("To intervene in members in cases of genocide", "This is a power of the AU, not the OAU."),
              ("To create a Pan-African Parliament", "The Pan-African Parliament is an organ of the AU."),
              ("To change all colonial borders", "The OAU accepted the borders inherited from colonial rule."),
          ], 2, "OAU aims: unity, defence of sovereignty and territorial integrity, ending colonialism, cooperation and development.",
          "Aims of the OAU", "Concept", "Think of what newly independent states most wanted to protect."),
        Q("What was the Liberation Committee of the OAU for?",
          "Helping liberation movements fight colonial rule", [
              ("Organising elections in member states", "Elections were a matter for each member state."),
              ("Running the African Union", "The AU was created in 2002."),
              ("Controlling the borders between members", "The Liberation Committee supported liberation movements."),
          ], 3, "The OAU helped liberation movements through its Liberation Committee.",
          "Achievements of the OAU", "Recall", "Think of the OAU's aim to end colonialism."),
        Q("Which was a major weakness of the OAU?",
          "Its policy of non-interference in members' internal affairs", [
              ("It rejected the borders inherited from colonial rule", "The OAU accepted the colonial borders."),
              ("It refused to help liberation movements", "It supported them through its Liberation Committee."),
              ("It supported apartheid in South Africa", "The OAU opposed apartheid."),
          ], 1, "Weak powers, little money and non-interference meant it could not act against abuses inside member states.",
          "Limits of the OAU", "Concept", "What could the OAU not do when abuses happened inside a member state?"),
        Q("Where and when was the African Union launched?",
          "Durban, 9 July 2002", [
              ("Addis Ababa, 25 May 1963", "This is the founding of the OAU."),
              ("Durban, 25 May 1963", "The place is right but the date belongs to the OAU."),
              ("Accra, 9 July 2002", "The AU was launched in Durban."),
          ], 0, "The AU was launched in Durban, South Africa, on 9 July 2002.",
          "The African Union", "Recall", "It was launched in the early 2000s, in South Africa."),
        Q("How does the African Union differ from the OAU?",
          "The AU may intervene in a member state in grave circumstances such as genocide", [
              ("The AU accepts members only from North Africa", "The AU is a continental body, like the OAU."),
              ("The AU has no Parliament", "The AU has a Pan-African Parliament."),
              ("The AU follows strict non-interference", "Strict non-interference was the OAU's policy."),
          ], 2, "The AU's Constitutive Act allows intervention in grave circumstances such as genocide and war crimes.",
          "OAU and AU compared", "Concept", "Leaders created the AU to fix one of the OAU's main weaknesses."),
        Q("Which description fits a regional organisation such as ECOWAS or SADC?",
          "A group of neighbouring states that cooperate on trade, security and development", [
              ("A military alliance of the Cold War", "NATO and the Warsaw Pact were Cold War alliances."),
              ("The body that replaced the AU", "The AU is a continental body and has not been replaced by regional groups."),
              ("A UN trust territory", "A trust territory was a former colony supervised by the UN, not a group of cooperating states."),
          ], 3, "Regional organisations are groups of neighbouring states that work together on trade, security and development.",
          "Regional bodies", "Concept", "Think of 'region' as the part of the continent where the states are neighbours."),
        NUM("How many years passed between the founding of the OAU (1963) and the launch of the AU (2002)?", 39,
            steps=[S("Subtract the years", math=r"2002 - 1963 = 39")],
            concept="Chronology of the OAU and AU", skill="Calculation", hint="Subtract the earlier year from the later year.",
            feedback="39 years separate the two events."),
    ]))

# ---------------------------------------------------------------- 4. Origins of the Cold War
SETS.append(practice_set(
    module=MODULE, topic=COLD,
    title="Origins of the Cold War and containment", lesson="origins-of-the-cold-war",
    questions=[
        Q("Which statement best describes the Cold War?",
          "A rivalry fought by propaganda, arms races and proxy wars rather than direct war", [
              ("A direct war between the USA and the USSR from 1945 to 1991", "The two superpowers never fought each other directly."),
              ("A conflict between European colonial powers over Africa", "The Cold War was a rivalry between the USA and the USSR."),
              ("A war between the USA and Germany", "The USA and the USSR were allies against Nazi Germany."),
          ], 2, "The Cold War was tension and rivalry between the USA and the USSR and their allies, without direct war between them.",
          "Nature of the Cold War", "Concept", "Think about why the word 'cold' is used."),
        Q("In 1946 Winston Churchill described the division of Europe using which phrase?",
          "An iron curtain", [
              ("Glasnost", "Glasnost (openness) was Gorbachev's reform in the 1980s."),
              ("A proxy war", "A proxy war is a conflict in which superpowers back opposing sides."),
              ("Containment", "Containment was the US policy of stopping the spread of communism."),
          ], 0, "After the USSR set up communist governments in Eastern Europe, Churchill said an iron curtain had come down across Europe.",
          "Causes of the Cold War", "Recall", "The phrase suggests a heavy barrier between East and West."),
        Q("What was the policy of containment?",
          "Stopping the spread of communism to new countries", [
              ("Opening the economy of the USSR to private business", "Opening the economy relates to Gorbachev's perestroika, not containment."),
              ("Ending all weapons production", "Containment relied on military power and alliances."),
              ("Dividing Germany into two states", "Germany's division was a consequence of the post-war settlement, not the policy of containment."),
          ], 1, "Containment was the US policy of stopping the spread of communism.",
          "Containment", "Concept", "The word 'contain' means to hold something in."),
        Q("Which pair of alliances and dates is correct?",
          "NATO 1949; Warsaw Pact 1955", [
              ("NATO 1955; Warsaw Pact 1949", "The dates are reversed."),
              ("NATO 1949; Warsaw Pact 1991", "The USSR was dissolved in 1991, and the Warsaw Pact was formed in 1955."),
              ("NATO 1962; Warsaw Pact 1963", "1962 was the Cuban Missile Crisis and 1963 the hotline."),
          ], 0, "The USA and its allies formed NATO in 1949. The USSR and its allies formed the Warsaw Pact in 1955.",
          "Cold War alliances", "Recall", "The Western alliance came first."),
        Q("What happened in the Berlin Blockade of 1948–1949?",
          "The USSR cut land routes to West Berlin and the West supplied the city by air", [
              ("The USA and the USSR fought a war over Berlin", "No direct war was fought."),
              ("The Berlin Wall was opened", "The wall was opened in 1989."),
              ("NATO was dissolved", "NATO continued to exist."),
          ], 3, "The West responded with an airlift. The blockade was the first major Cold War crisis.",
          "Berlin Blockade", "Recall", "Think of how else a city can be supplied if roads are closed."),
        Q("Why did the USSR fear the West after 1945?",
          "It feared a Western attack and the US atomic bomb", [
              ("It feared Africa's independence", "The Soviet fears in 1945 were about Europe and the atomic bomb."),
              ("It feared the OAU", "The OAU was founded in 1963."),
              ("It feared Gorbachev's reforms", "Gorbachev came to power in 1985."),
          ], 2, "The USSR feared Western attack and the US atomic bomb, while the USA feared that communism would spread.",
          "Causes of the Cold War", "Reasoning", "Each side felt threatened by the other."),
        Q("Which pair of ideas correctly describes the main ideological conflict?",
          "Capitalism and democracy against communism and one-party rule", [
              ("Communism and democracy against capitalism and one-party rule", "The ideas are mixed up: the USA stood for capitalism and democracy."),
              ("Colonialism against nationalism", "That was a conflict of the decolonization period."),
              ("Federalism against unitary government", "That was a constitutional question inside Cameroon."),
          ], 0, "The USA stood for capitalism and multi-party democracy. The USSR stood for communism and one-party rule.",
          "Causes of the Cold War", "Concept", "Match each superpower with its own system."),
        Q("Historians disagree about who was to blame for the Cold War. Which view is balanced?",
          "Both superpowers contributed, because each acted from fear and from its own ideas", [
              ("Only the USSR was responsible, because it set up communist governments", "This ignores US policy and the fear felt on both sides."),
              ("Only the USA was responsible, because it had the atomic bomb", "This ignores the Soviet control of Eastern Europe."),
              ("Nobody was responsible, because the Cold War had no causes", "The Cold War had causes: ideas, fear, Eastern Europe and the end of the wartime alliance."),
          ], 1, "Many historians say that both sides contributed, though they weigh the causes differently.",
          "Historical interpretation", "Interpretation", "A balanced view gives some responsibility to both sides."),
    ]))

# ---------------------------------------------------------------- 5. Crises and proxy conflicts
SETS.append(practice_set(
    module=MODULE, topic=COLD,
    title="Cuba, proxy wars and the Cold War in Africa", lesson="cold-war-crises-and-proxy-conflicts",
    questions=[
        NUM("In which year did Fidel Castro's revolution take power in Cuba?", 1959,
            steps=[S("Recall", text="Castro's revolution took power in 1959. Cuba then became an ally of the USSR.")],
            concept="Origins of the Cuban Missile Crisis", skill="Recall", hint="It was three years before the missile crisis.",
            feedback="Castro's revolution was in 1959; the crisis came in October 1962."),
        NUM("For how many days did the world fear nuclear war during the Cuban Missile Crisis?", 13,
            steps=[S("Recall", text="After Kennedy ordered a naval blockade, the world feared nuclear war for thirteen days.")],
            concept="Cuban Missile Crisis", skill="Recall", hint="The crisis is remembered as lasting just under two weeks.",
            feedback="The crisis lasted thirteen days."),
        Q("How did the Cuban Missile Crisis end in October 1962?",
          "Khrushchev agreed to remove the missiles and the USA promised not to invade Cuba", [
              ("The USSR kept its missiles in Cuba", "The Soviet missiles were removed."),
              ("The USA invaded Cuba and removed Castro", "The USA promised not to invade Cuba."),
              ("Gorbachev and Kennedy signed a peace treaty", "Gorbachev led the USSR only from 1985."),
          ], 0, "Each side gave something. The USA later also removed its missiles from Turkey.",
          "Cuban Missile Crisis", "Recall", "Each side gave something to avoid nuclear war."),
        Q("Which was a result of the Cuban Missile Crisis?",
          "A telephone hotline between Washington and Moscow", [
              ("The opening of the Berlin Wall", "The Berlin Wall was opened in 1989."),
              ("The Soviet invasion of Afghanistan", "That began in 1979."),
              ("The formation of NATO", "NATO was formed in 1949."),
          ], 2, "Results: a hotline (1963), the Partial Test Ban Treaty (1963), and more caution about direct confrontation.",
          "Results of the Cuban crisis", "Reasoning", "Both sides wanted a quicker way to talk in a future crisis."),
        Q("What is a proxy war?",
          "A conflict in which superpowers support opposing sides without fighting each other directly", [
              ("A war fought only by the USA and the USSR", "Proxy wars are fought by other states or groups."),
              ("A war between two African states with no outside help", "A proxy war involves superpower support."),
              ("A war that ends with a hotline", "A hotline was a communication link, not a type of war."),
          ], 1, "Korea, Vietnam, Angola and Afghanistan are examples.",
          "Proxy wars", "Concept", "A proxy acts on behalf of someone else."),
        Q("In Angola after 1975, which side did the USSR and Cuba support?",
          "The MPLA government", [
              ("The rivals of the MPLA", "The USA and South Africa backed the MPLA's rivals."),
              ("Portugal", "Portugal had left after the 1974 revolution in Lisbon."),
              ("Neither side", "Angola is the lesson's example of an African proxy war."),
          ], 0, "The USSR and Cuba supported the MPLA government. The USA and South Africa backed its rivals.",
          "Angola and the Cold War", "Recall", "Remember Angola as an example of a proxy war in Africa."),
        Q("How did the USA's war in Vietnam end?",
          "The USA withdrew in 1973 and Vietnam was united under communist rule in 1975", [
              ("The USA won and Vietnam stayed divided", "The USA withdrew and Vietnam was united under communist rule."),
              ("The war ended with the Cuban Missile Crisis", "The Cuban crisis was in 1962."),
              ("The USSR invaded Vietnam in 1979", "The Soviet invasion in 1979 was in Afghanistan."),
          ], 3, "The USA fought communist forces until it withdrew in 1973. Vietnam was united under communist rule in 1975.",
          "Vietnam", "Recall", "Think of the two dates: one for the US withdrawal and one for unification."),
        Q("Which statement about the Cold War in Africa is the most balanced?",
          "It brought aid and weapons, but it also made local wars longer and put pressure on states to take sides", [
              ("It brought only benefits, because it gave Africa aid", "This ignores the costs of foreign weapons and pressure to choose sides."),
              ("It caused every war in Africa", "Local causes also mattered."),
              ("It had no effect on Africa", "Newly independent states had to decide how close to stay to each bloc."),
          ], 0, "A balanced answer gives advantages and disadvantages and does not blame the Cold War for every African war.",
          "Africa as a Cold War arena", "Interpretation", "A balanced answer gives both gains and costs."),
    ]))

# ---------------------------------------------------------------- 6. End of the Cold War
SETS.append(practice_set(
    module=MODULE, topic=COLD,
    title="The end of the Cold War and the Soviet collapse", lesson="end-of-cold-war-and-soviet-collapse",
    questions=[
        Q("Who became Soviet leader in 1985 and introduced reforms?",
          "Mikhail Gorbachev", [
              ("Nikita Khrushchev", "Khrushchev led the USSR during the Cuban Missile Crisis in 1962."),
              ("Joseph Stalin", "Stalin died in 1953."),
              ("Fidel Castro", "Castro led Cuba, not the USSR."),
          ], 0, "Gorbachev led the USSR from 1985.",
          "Gorbachev", "Recall", "He is linked with glasnost and perestroika."),
        Q("What did the term glasnost mean?",
          "Openness", [
              ("Economic restructuring", "That is perestroika."),
              ("Containment", "Containment was a US policy."),
              ("The arms race", "The arms race was the competition in weapons."),
          ], 1, "Glasnost meant openness: more freedom of speech and information.",
          "Glasnost and perestroika", "Recall", "One of Gorbachev's two key words means 'open'."),
        Q("What did the term perestroika mean?",
          "Economic restructuring", [
              ("Openness", "That is glasnost."),
              ("Non-alignment", "Non-alignment means staying out of both blocs."),
              ("Reunification", "Reunification refers to Germany."),
          ], 0, "Perestroika meant changes to make the Soviet economy work better.",
          "Glasnost and perestroika", "Recall", "It is the economic word of the pair."),
        NUM("In which year was the Berlin Wall opened?", 1989,
            steps=[S("Recall", text="The Berlin Wall was opened on 9 November 1989. Germany was reunified on 3 October 1990.")],
            concept="Events of 1989 to 1991", skill="Recall", hint="It happened before Germany was reunified and before the USSR ended.",
            feedback="The wall opened in 1989; the USSR was dissolved in 1991."),
        Q("Which is the correct order of events?",
          "Gorbachev becomes leader, Berlin Wall opens, Germany reunified, USSR dissolved", [
              ("Berlin Wall opens, Gorbachev becomes leader, USSR dissolved, Germany reunified", "Gorbachev came to power in 1985, before the wall opened, and Germany was reunified before the USSR ended."),
              ("USSR dissolved, Germany reunified, Berlin Wall opens, Gorbachev becomes leader", "This reverses the correct order."),
              ("Germany reunified, Gorbachev becomes leader, USSR dissolved, Berlin Wall opens", "Reunification came in 1990, after the wall opened and Gorbachev's rise."),
          ], 2, "1985 Gorbachev; 9 November 1989 Berlin Wall opens; 3 October 1990 reunification; December 1991 USSR dissolved.",
          "Chronology of the collapse", "Reasoning", "Start with the earliest year, 1985."),
        Q("Which was an economic cause of the Soviet collapse?",
          "The huge cost of the arms race and the war in Afghanistan", [
              ("Nationalism in the republics", "This is a political cause."),
              ("The failed coup of August 1991", "This is a political event."),
              ("The founding of the OAU", "The OAU was an African body founded in 1963."),
          ], 0, "Economic causes: a stagnant economy, shortages, and the cost of the arms race and the war in Afghanistan.",
          "Causes of the Soviet collapse", "Concept", "An economic cause is about money and production."),
        Q("Historians weigh the causes of the Soviet collapse differently. Which pair describes the two emphases?",
          "Some stress Western pressure; others stress internal weakness", [
              ("Some stress the Marshall Plan; others stress the Truman Doctrine", "These were 1947 US policies, not the debated causes of the collapse."),
              ("Some stress the Cuban crisis; others stress the Korean War", "These were earlier events."),
              ("Some stress African independence; others stress the OAU", "These are not given as causes of the Soviet collapse."),
          ], 1, "Some historians stress Western pressure, others internal weakness, and most combine the two.",
          "Historical interpretation", "Interpretation", "One view looks outside the USSR, the other looks inside."),
        Q("Which statement about the end of the Cold War in Africa is most balanced?",
          "Superpower aid and interest fell and many states moved towards multi-party politics, but local causes of conflict remained", [
              ("It solved all of Africa's problems", "Gains came together with new difficulties."),
              ("It had no effect in Africa", "Superpower aid and the proxy conflicts changed."),
              ("It ended all wars in Africa at once", "Some wars ended, while others continued from local causes."),
          ], 3, "Namibia became independent in 1990 and many states moved to multi-party politics, but not every problem was solved.",
          "Consequences for Africa", "Interpretation", "A balanced answer gives gains and difficulties."),
    ]))
