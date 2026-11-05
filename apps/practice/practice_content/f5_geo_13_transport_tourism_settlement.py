"""Practice sets for Form 5 Geography: Tertiary industries and Settlement Geography (one set per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

ECO = "Economic Activities"
TERT = "Tertiary industries"
SET = "Settlement Geography"
GEN = "General concepts of settlement"
MORPH = "Settlement types and their morphology"


def Q(prompt, right, wrongs, pos, step, concept, skill, hint, feedback="", diagram="", diagram_alt=""):
    """Multiple choice helper: `wrongs` is a list of three (text, why); the right answer goes at index `pos`."""
    ch = [C(t, why=w) for t, w in wrongs]
    ch.insert(pos, C(right, correct=True))
    return MC(prompt, ch, steps=[S("Reason it out", text=step)], concept=concept, skill=skill, hint=hint,
              feedback=feedback or step, diagram=diagram, diagram_alt=diagram_alt)


SETS = []

# ------------------------------------------------------------------ 1. Transport
SETS.append(practice_set(
    module=ECO, topic=TERT, title="Transport systems: modes and impacts", lesson="ts-transport-systems",
    questions=[
        Q("What is transport?", "The movement of people, goods and services from one place to another", [
            ("The sending of information over a distance", "That is telecommunication."),
            ("The buying and selling of goods", "That is trade."),
            ("The making of goods in factories", "That is manufacturing, a secondary industry."),
        ], 2, "Transport is the movement of people, goods and services from one place to another.",
          "Transport definition", "Recall", "Think about what is being moved."),
        Q("Which mode of transport is the fastest?", "Air", [
            ("Rail", "Trains are faster than lorries over long distances but slower than aircraft."),
            ("Road", "Road transport is flexible but slower than air."),
            ("Water", "Water transport is the slowest of the main modes."),
        ], 1, "Aircraft cover long distances in the shortest time, although air transport is also the most expensive mode.",
          "Speed of modes", "Recall", "Think about which mode can cross an ocean in hours."),
        Q("A pipeline can be used to carry", "oil, gas or water", [
            ("passengers going to work", "Pipes cannot carry people."),
            ("bags of cement", "Cement in bags is solid cargo; pipelines carry liquids, gases and slurries."),
            ("fresh fruit and vegetables", "Fresh food needs vehicles that can carry solid goods."),
        ], 0, "A pipeline carries liquids and gases, such as crude oil, natural gas and water.",
          "Pipeline use", "Recall", "What kinds of goods can flow through a pipe?"),
        Q("Which is an advantage of road transport?", "It provides a door-to-door service", [
            ("It carries heavier loads than trains", "Trains and ships carry heavier loads than lorries."),
            ("It is cheapest for very long journeys", "Rail and water cost less per tonne over long distances."),
            ("It causes no pollution", "Vehicles give off fumes and noise."),
        ], 3, "Roads reach farms, markets and homes, so goods need not be moved from one vehicle to another.",
          "Advantages of road transport", "Concept", "Where can a lorry go that a train cannot?"),
        NUM("A lorry carries 20 tonnes of maize from a farm to a town. The cost of the journey is 120,000 FCFA. What is the cost per tonne, in FCFA?", 6000,
            steps=[S("Divide the cost by the tonnes", math=r"120000 \div 20 = 6000", text="The cost is 6000 FCFA for each tonne.")],
            unit="FCFA", concept="Cost per tonne", skill="Calculation", hint="Divide the total cost by the number of tonnes carried."),
        Q("A company wants to export thousands of tonnes of cocoa to another continent. Which mode of transport is usually the cheapest for this?", "Water (ship)", [
            ("Air", "Air freight is the most expensive way to move heavy loads."),
            ("Road", "A lorry cannot cross the sea."),
            ("Pipeline", "A pipeline carries only liquids and gases."),
        ], 1, "Ships carry very large loads at the lowest cost per tonne over long distances.",
          "Choosing a mode of transport", "Application", "The goods are bulky, heavy and not urgent."),
        Q("What is the most likely environmental impact of building a new road through a rainforest?", "The forest is opened to logging, farming and poaching", [
            ("The air becomes cleaner", "Vehicles and clearing add pollution and remove trees."),
            ("Wildlife numbers increase", "Habitats are cut and hunting becomes easier, so wildlife usually suffers."),
            ("Soil erosion stops", "Cleared slopes and road cuttings usually increase erosion."),
        ], 3, "A road in a forest breaks habitats and gives access to loggers, farmers and hunters, so more forest is lost.",
          "Environmental impacts of transport", "Reasoning", "Ask who can now reach the forest."),
        Q("A tarred road now links a farming area to a city market. Which economic effect is most likely?", "Less food spoils and farm incomes rise", [
            ("Fewer jobs for drivers and traders", "Roads usually create jobs in driving, trade and repair."),
            ("Farmers sell crops only in the village", "The road widens the market, so farmers can sell farther away."),
            ("Villages become harder to reach", "A road makes places easier to reach."),
        ], 2, "Fast, reliable transport gets crops to market before they spoil, so farmers sell more and earn more.",
          "Economic impacts of transport", "Reasoning", "Think about how quickly the crops reach buyers."),
    ]))

# ------------------------------------------------------------------ 2. Telecommunication and the internet
SETS.append(practice_set(
    module=ECO, topic=TERT, title="Telecommunication systems and the internet", lesson="ts-telecommunication-and-the-internet",
    questions=[
        Q("Telecommunication is best defined as", "the sending of information over a distance by cable, radio waves or satellite", [
            ("the movement of goods by road, rail or sea", "That is transport."),
            ("the setting up of shops in towns", "That is retail trade."),
            ("the printing of books and newspapers", "Printing makes a product. It does not send information over a distance."),
        ], 1, "Telecommunication moves information, such as voice, text, pictures and data, over a distance.",
          "Telecommunication definition", "Recall", "Think about what is being sent and what is not."),
        Q("Which of the following is a telecommunication system?", "A mobile phone network", [
            ("A railway", "A railway is a transport system."),
            ("An oil pipeline", "A pipeline carries oil, which is a physical product."),
            ("A cargo ship", "A ship is a transport vehicle."),
        ], 0, "A mobile phone network sends voice and data through masts and cables.",
          "Telecommunication systems", "Recall", "Look for a system that carries information, not goods."),
        Q("Why are communication satellites used to send signals between distant continents?", "They relay the signal over the curve of the Earth", [
            ("Radio signals cannot be sent on the ground at all", "Signals can be sent on the ground, but only over a limited straight distance."),
            ("Satellites are always cheaper than cables", "Cables are often cheaper and carry more data. Satellites help where cables do not reach."),
            ("Satellites make the signal travel faster than light", "Nothing travels faster than light. The satellite simply relays the signal around the curve."),
        ], 2, "The Earth is curved, so a straight signal cannot reach far. A satellite high above can send the signal on.",
          "How satellites work", "Concept", "Think about the shape of the Earth."),
        Q("Why is radio still important in many remote villages?", "Cheap battery radios work without electricity or internet", [
            ("Radio gives faster downloads than the internet", "Radio does not download files."),
            ("Radio needs no transmitter", "A broadcast needs a transmitter."),
            ("Radio can only be heard in cities", "Radio waves reach rural areas as well."),
        ], 3, "A small battery radio is cheap and needs no grid power or data, and a broadcast reaches many people in local languages.",
          "Role of radio", "Application", "Think about cost and power supply."),
        NUM("A school has 120 students. Only 30 of them can use the internet at home. What percentage can use the internet at home?", 25,
            steps=[S("Fraction times 100", math=r"\frac{30}{120} \times 100 = 25", text="So 25 percent of the students can use the internet at home.")],
            unit="%", concept="Percentage with internet access", skill="Calculation", hint="Divide the part by the whole, then multiply by 100."),
        Q("Which is an advantage of the internet?", "Fast and cheap communication with people far away", [
            ("It never needs electricity", "Computers, phones and masts all need power."),
            ("It stops fraud", "Fraud and hacking are risks of the internet."),
            ("It is equally available in all areas", "Access is much weaker in many rural areas."),
        ], 1, "Email, calls and messages reach distant people in seconds at low cost.",
          "Advantages of the internet", "Concept", "Think about what the internet does for communication."),
        Q("The 'digital divide' means", "the gap between people who have access to the internet and those who do not", [
            ("the splitting of a file into two parts", "It is a social and economic gap, not a computer file task."),
            ("the difference between radio and television", "It concerns access to internet technology."),
            ("a break in an undersea cable", "A cable fault is a technical problem, not the digital divide."),
        ], 2, "The digital divide is the gap between connected and unconnected people, often along lines of income and location.",
          "Digital divide", "Concept", "Think about who can and cannot get online."),
        Q("A trader in a village pays a supplier in another town by mobile money. What advantage of telecommunication does this show?", "It saves time and travel cost", [
            ("It removes the need for any phone network", "Mobile money needs a phone network."),
            ("It makes the supplier's goods cheaper to make", "The payment does not change how goods are made."),
            ("It increases the weight of the goods", "Payment by phone does not change the goods."),
        ], 0, "The trader makes the payment at once without a journey, which saves time and travel costs.",
          "Benefits of mobile payments", "Application", "What would the trader have to do without a phone?"),
    ]))

# ------------------------------------------------------------------ 3. Tourism: types and growth
SETS.append(practice_set(
    module=ECO, topic=TERT, title="Tourism: types, potentials and growth", lesson="ts-tourism-types-and-growth",
    questions=[
        Q("Tourism is best defined as", "travel to and stay in places outside one's usual area for leisure, business or other purposes", [
            ("the transport of goods across a border", "That is trade and transport."),
            ("moving permanently to a new country", "A tourist returns home, but a migrant moves for good."),
            ("working in a hotel", "That is a job in the tourist industry, not tourism itself."),
        ], 3, "A tourist travels outside the usual home or work area for a limited time and then returns.",
          "Definition of tourism", "Recall", "A tourist visits and then goes home."),
        Q("A family from Yaounde spends a weekend at a beach in Cameroon. What type of tourism is this?", "Domestic tourism", [
            ("International tourism", "The family does not cross a border."),
            ("Business tourism", "The trip is for rest, not for work."),
            ("Health tourism", "The trip is for rest and fun, not for medical treatment."),
        ], 0, "They stay inside their own country, so it is domestic tourism.",
          "Domestic and international tourism", "Application", "Ask whether the family crosses a border."),
        NUM("A national park received 80,000 visitors in one year and 100,000 in the next year. By what percentage did the number of visitors increase?", 25,
            steps=[S("Find the increase", math=r"100000 - 80000 = 20000"), S("Divide by the original and multiply by 100", math=r"\frac{20000}{80000} \times 100 = 25", text="Visitors increased by 25 percent.")],
            unit="%", concept="Percentage change in visitors", skill="Calculation", hint="Find the increase first, then divide by the starting number."),
        Q("Eco-tourism means", "visiting natural areas in a way that protects nature and helps local people", [
            ("taking cheap package holidays to the coast", "Package holidays are not necessarily eco-tourism."),
            ("travelling only for business meetings", "That is business tourism."),
            ("visiting a hospital in another country", "That is health tourism."),
        ], 2, "Eco-tourism aims to enjoy and protect natural areas and benefit local communities.",
          "Eco-tourism", "Concept", "Think of 'eco' as ecology, nature."),
        Q("Which of these is a natural tourist attraction of Cameroon?", "The beaches near Limbe and Kribi", [
            ("A shopping mall with imported goods", "A mall is a human-made facility, not a natural attraction."),
            ("A foreign hotel chain", "A hotel is a facility, not an attraction."),
            ("An international airport", "An airport helps access but is not an attraction."),
        ], 1, "Coastal beaches are a natural attraction. Mount Cameroon, waterfalls and parks are others.",
          "Tourist potential of Cameroon", "Recall", "Choose the attraction made by nature."),
        Q("Mass tourism refers to", "large numbers of tourists, often on package holidays, visiting the same popular places", [
            ("one wealthy person visiting a remote village", "That describes individual tourism."),
            ("people visiting a place only once in ten years", "Mass tourism is about numbers, not the rarity of a visit."),
            ("tourists who stay for a whole year", "Mass tourism is about large numbers of visitors."),
        ], 0, "Mass tourism involves large groups visiting a few popular places such as beach resorts.",
          "Mass tourism", "Concept", "Think about the word 'mass'."),
        Q("Which development has most helped tourism to grow quickly?", "Package holidays and online booking", [
            ("Fewer paid holidays for workers", "Paid holidays have increased, which has helped tourism."),
            ("Higher air fares", "Cheaper air travel has helped tourism grow."),
            ("Less advertising of destinations", "Advertising and social media have increased."),
        ], 3, "Package holidays and online booking make travel easy and affordable, so more people travel.",
          "Reasons for the growth of tourism", "Concept", "Which change makes planning a trip easier?"),
        Q("A country starts low-cost direct flights from several cities. What is the most likely effect on tourism?", "More tourists arrive because travel is cheaper and quicker", [
            ("Fewer tourists arrive because travel is easier", "Easier and cheaper travel usually raises numbers."),
            ("Only domestic tourism increases", "Direct flights mainly increase international arrivals."),
            ("Tourist numbers do not change", "Better access is a major factor in tourist numbers."),
        ], 2, "Cheaper and quicker access removes one of the main obstacles, so more tourists come.",
          "Transport and tourism growth", "Reasoning", "Think about what flights change for travellers."),
    ]))

# ------------------------------------------------------------------ 4. Tourism: challenges and impacts
SETS.append(practice_set(
    module=ECO, topic=TERT, title="Tourism: obstacles, advantages and disadvantages", lesson="ts-tourism-challenges-and-impacts",
    questions=[
        Q("Which of the following is an obstacle to the growth of tourism in a developing country?", "Poor roads and few good hotels", [
            ("Reliable electricity and water", "Reliable utilities help tourism."),
            ("Cheap air fares", "Cheap flights help tourism."),
            ("Well-known attractions", "Well-known attractions help to draw tourists."),
        ], 2, "Poor access and weak facilities discourage visitors and reduce the numbers who come.",
          "Obstacles to tourism", "Recall", "Which choice makes visiting harder?"),
        Q("The multiplier effect in tourism means that", "money spent by tourists is spent again and again in the local economy", [
            ("tourist numbers double every year", "That describes growth in numbers."),
            ("hotel prices are multiplied by the number of guests", "The multiplier effect is not about prices."),
            ("profits are sent abroad", "That is leakage."),
        ], 0, "Hotels, guides and shops spend their income on local wages and supplies, creating more income and jobs.",
          "Multiplier effect", "Concept", "Think of money passing from hand to hand."),
        Q("What is leakage in tourism?", "Money paid by tourists that leaves the local economy", [
            ("Rainwater entering hotel rooms", "Leakage here means money, not water."),
            ("Tourists who leave before the end of their stay", "Leakage is about money."),
            ("Money spent again in local markets", "That is the multiplier effect."),
        ], 3, "Profits sent to foreign owners and payments for imported goods leave the area.",
          "Leakage", "Concept", "Where does the money go?"),
        NUM("A tourist spends 100,000 FCFA on a trip. Of this, 60 percent leaks out of the local economy. How many FCFA stay in the local economy?", 40000,
            steps=[S("Percentage that stays", math=r"100 - 60 = 40\%"), S("Find 40 percent of 100,000", math=r"\frac{40}{100} \times 100000 = 40000", text="So 40,000 FCFA stays in the local economy.")],
            unit="FCFA", concept="Leakage calculation", skill="Calculation", hint="First work out what percentage stays."),
        Q("Which is an economic advantage of tourism?", "It creates jobs and earns foreign exchange", [
            ("It always lowers prices for local people", "Prices may rise near tourist areas."),
            ("It removes all seasonal unemployment", "Many tourism jobs are seasonal."),
            ("It makes the country independent of other sectors", "Overdependence on tourism is a risk."),
        ], 1, "Tourism provides jobs in hotels, transport, guiding and crafts, and international visitors bring foreign money.",
          "Economic advantages of tourism", "Concept", "Think about who earns money from visitors."),
        Q("Which is an environmental disadvantage of tourism?", "Litter and footpath erosion at popular sites", [
            ("Money for rangers", "Money for rangers is an advantage."),
            ("Local people value nature more", "Valuing nature is an advantage."),
            ("More jobs in guiding", "Jobs are an economic effect, not an environmental harm."),
        ], 0, "Large numbers of visitors drop litter and wear away paths and soil.",
          "Environmental disadvantages of tourism", "Concept", "Look for the choice that harms the place."),
        Q("How can tourism help to protect the environment?", "Park fees can pay for rangers and reserves", [
            ("Hotels can use more water", "More water use is a pressure on resources."),
            ("Beaches can be left untidy", "That would damage the environment."),
            ("More forest can be cleared for roads", "Clearance harms habitats."),
        ], 2, "Entrance fees and taxes fund conservation, and local people have a reason to protect nature that earns money.",
          "Environmental advantages of tourism", "Reasoning", "Think about where conservation money can come from."),
        Q("Most hotels in a resort are owned by foreign companies and import their food. What is the most likely effect?", "More money leaks out and the local area gains less", [
            ("The multiplier effect becomes larger", "Imported food and foreign profits reduce local spending."),
            ("All jobs become better paid", "Foreign ownership does not guarantee better pay."),
            ("Tourist numbers fall to zero", "There is no reason for numbers to fall to zero."),
        ], 3, "Profits and import payments leave the country, so less money is spent again locally.",
          "Leakage and ownership", "Application", "Where do foreign owners send their profits?"),
    ]))

# ------------------------------------------------------------------ 5. Settlement, site and situation
SIT = "f5g-ts-site-situation-map.svg"
SIT_ALT = "Fictitious map of Ngomo village on dry ground near a marsh and river, with a stream from Mt Boko, a main road 8 km to Essima market town and a 5 km scale bar"
SETS.append(practice_set(
    module=SET, topic=GEN, title="Settlement: types, site, situation and siting factors", lesson="ts-what-is-settlement-site-and-situation",
    questions=[
        Q("A settlement is best defined as", "a place where people live and build homes", [
            ("a place where goods are made", "That describes an industrial site."),
            ("a farm without any houses", "A settlement includes the homes of the people."),
            ("a place where tourists stay for a day", "A settlement is where people live, not where they visit."),
        ], 1, "A settlement is a place where people live and build homes, with the buildings and land they use.",
          "Definition of settlement", "Recall", "Think about the word 'live'."),
        Q("The site of a settlement is", "the actual ground on which the settlement is built", [
            ("its position in relation to other places", "That is the situation."),
            ("the number of people who live there", "That is population size."),
            ("the main job of its people", "That is the function."),
        ], 3, "Site is the actual spot: the ground, slope and nearby water.",
          "Site of a settlement", "Recall", "Site is about the ground itself."),
        Q("Look at the map. Which statement describes the SITUATION of Ngomo?", "It lies 8 km west of Essima market town, south of Mt Boko", [
            ("It stands on dry, raised ground above the marsh", "That describes the site, the ground itself."),
            ("It is built on a gently sloping area near a stream", "That is also about the site."),
            ("It has fertile farmland close to its houses", "That describes the resources of the site."),
        ], 0, "Situation compares the settlement with other places: distance, direction and routes.",
          "Situation from a map", "Interpretation", "Choose the statement that links Ngomo to other places.",
          diagram=SIT, diagram_alt=SIT_ALT),
        NUM("On the map, the scale bar of 5 km is a given length. The road from Ngomo to Essima is exactly 1.6 times as long as this scale bar. What is the distance from Ngomo to Essima, in km?", 8,
            steps=[S("Multiply the scale length by 1.6", math=r"5 \times 1.6 = 8", text="The road is 8 km long.")],
            unit="km", concept="Distance from a scale bar", skill="Calculation", hint="Multiply 5 km by the number of scale bar lengths.",
            diagram=SIT, diagram_alt=SIT_ALT),
        Q("Which is the best reason for villagers to build on a dry point beside a marsh instead of in the marsh?", "The ground stays dry and healthy for houses and floods are less likely", [
            ("Marsh has no water", "A marsh is full of water."),
            ("Marsh is the best place for defence", "Marsh is not a good defensive site, and it breeds mosquitoes."),
            ("Marsh soil is too fertile for crops", "Waterlogged soil is difficult to farm and build on."),
        ], 2, "A dry point keeps buildings safe and healthy, while marsh floods and breeds disease.",
          "Siting factors: dry site", "Reasoning", "Think about floods and health."),
        Q("Which is a feature of a rural settlement?", "Most people work in farming, fishing or herding", [
            ("Most people work in banks and offices", "That describes urban work."),
            ("It has a university and an airport", "These are services of a city."),
            ("It has very high population density", "Rural settlements have few people per square kilometre."),
        ], 1, "Rural settlements are small and based on primary work such as farming.",
          "Rural settlement features", "Concept", "Think about what villagers do for a living."),
        Q("Douala is on the Wouri estuary near the sea. Which statement is about its situation?", "It lies where the Wouri meets the sea, linked by road and rail to the interior", [
            ("It is built on low, flat ground", "That describes the site."),
            ("The soil under the houses is sandy and wet", "That describes the ground, the site."),
            ("Mangroves grow on the river banks", "That is about the vegetation of the site."),
        ], 3, "Situation describes position in relation to the sea and routes: the estuary and the links inland.",
          "Site and situation: Douala", "Application", "Which choice links Douala to places and routes around it?"),
        Q("Look at the map. Why is Ngomo built on the raised ground rather than next to the river?", "The ground near the river is marsh that floods, while the raised ground is dry and has a stream", [
            ("The river has no water in it", "The map shows the river with a floodplain and marsh along it."),
            ("The hill makes the river flow backwards", "The hill is not related to the river's direction."),
            ("Villages never use rivers or streams", "Water is vital, and the village uses a stream that is on dry ground."),
        ], 2, "The marsh and floodplain are wet and risky. The dry raised ground with a nearby stream is the better site.",
          "Interpreting a site on a map", "Interpretation", "Compare the ground next to the river with the ground where the houses stand.",
          diagram=SIT, diagram_alt=SIT_ALT),
    ]))

# ------------------------------------------------------------------ 6. Rural patterns
PAT = "f5g-ts-rural-patterns-quiz.svg"
PAT_ALT = "Three sketch maps labelled A, B and C: A has twelve houses in two lines along a road; B has houses clustered round a central square; C has farms scattered with space between them"
SETS.append(practice_set(
    module=SET, topic=MORPH, title="Rural settlement patterns", lesson="ts-rural-settlement-patterns",
    questions=[
        Q("A nucleated settlement is one in which", "houses are grouped closely round a centre", [
            ("houses are scattered far apart", "That is a dispersed settlement."),
            ("houses are built in a line", "That is a linear settlement."),
            ("there are no houses, only farms", "A settlement has houses."),
        ], 0, "A nucleated settlement is a cluster of houses round a focus such as a well, market or crossroads.",
          "Nucleated settlement", "Recall", "Think of the word 'nucleus' meaning centre."),
        Q("Look at the three sketch maps. Which letter shows a nucleated pattern?", "B", [
            ("A", "A shows houses in a line, a linear pattern."),
            ("C", "C shows scattered farms, a dispersed pattern."),
            ("A and C", "Neither A nor C shows houses grouped round a centre."),
        ], 1, "In B, houses are clustered round a central feature, so it is nucleated.",
          "Recognising nucleated pattern", "Interpretation", "Look for a centre with houses round it.",
          diagram=PAT, diagram_alt=PAT_ALT),
        Q("Look at the sketch maps. The pattern shown in C is called", "dispersed", [
            ("nucleated", "A nucleated pattern has houses packed round a centre."),
            ("linear", "A linear pattern has houses along a line."),
            ("star-shaped", "No star shape is shown. The farms are scattered."),
        ], 3, "In C, farms and houses are scattered with open land between them, a dispersed pattern.",
          "Recognising dispersed pattern", "Interpretation", "Look at the distance between houses in C.",
          diagram=PAT, diagram_alt=PAT_ALT),
        NUM("Look at sketch map A. It has the same number of houses on each side of the road, with 6 houses on the upper side. How many houses are there altogether in A?", 12,
            steps=[S("Count both sides", math=r"6 + 6 = 12", text="There are 12 houses in A.")],
            unit="houses", concept="Counting houses in a linear pattern", skill="Interpretation", hint="Add the houses on both sides of the road.",
            diagram=PAT, diagram_alt=PAT_ALT),
        Q("Which factor is most likely to produce a LINEAR settlement?", "A main road or a river with land only along its edge", [
            ("A wide flat plain with water everywhere", "That favours scattered houses."),
            ("A single spring in a dry area", "That favours a nucleated village."),
            ("Large farms owned by single families", "That favours a dispersed pattern."),
        ], 2, "Roads and rivers give access and water along a line, so houses are built in a line.",
          "Factors of linear settlement", "Concept", "Think about the one line that attracts houses."),
        Q("Which factor is most likely to produce a NUCLEATED village?", "One spring in a dry area, and the need for defence", [
            ("Plenty of land and water in every place", "That allows people to spread out."),
            ("A very safe time with no conflicts", "In safe times people can spread out."),
            ("Large plantations needing wide space", "Plantations lead to scattered homes."),
        ], 0, "A single water source and the need for defence draw people together.",
          "Factors of nucleated settlement", "Concept", "Think about reasons to live close together."),
        Q("Which is a reason why farmers may build a DISPERSED pattern of houses?", "Each family lives on its own large farm", [
            ("There is only one well in the whole area", "That would draw people together."),
            ("The area is under attack", "Attack encourages people to gather for defence."),
            ("A road is the only dry land", "That would produce a line of houses."),
        ], 3, "On large individual farms, people live beside their fields, so houses are far apart.",
          "Factors of dispersed settlement", "Concept", "Think about where farmers want to live if their farms are big."),
        Q("A village lies in a narrow valley between steep hills with a stream along the valley floor. Which pattern is it most likely to have?", "Linear", [
            ("Dispersed", "There is little flat land for scattered farms."),
            ("Nucleated", "The valley is a narrow strip, so houses stretch along it."),
            ("Grid", "A grid needs wide level ground."),
        ], 0, "A narrow valley floor with a stream leaves only a strip of land, so houses form a line along it.",
          "Applying pattern factors", "Application", "Picture the shape of the available flat land."),
    ]))

# ------------------------------------------------------------------ 7. Urbanisation and urban types
SETS.append(practice_set(
    module=SET, topic=MORPH, title="Urbanisation and types of urban settlement", lesson="ts-urbanisation-and-types-of-urban-settlement",
    questions=[
        Q("Urbanisation is the", "increase in the proportion of people living in towns and cities", [
            ("increase in the number of farms", "That is agricultural expansion."),
            ("movement of people from towns to villages", "That is counter-urbanisation."),
            ("building of one new town", "Urbanisation is about the share of people living in towns."),
        ], 2, "Urbanisation is a rise in the percentage of a country's people living in urban areas.",
          "Definition of urbanisation", "Recall", "Look for the word 'proportion'."),
        NUM("In a country of 9 million people, 3.6 million live in towns. What percentage of the population is urban?", 40,
            steps=[S("Divide and multiply by 100", math=r"\frac{3.6}{9} \times 100 = 40", text="The country is 40 percent urban.")],
            unit="%", concept="Percentage urban", skill="Calculation", hint="Divide the urban population by the total population."),
        Q("Which is a PUSH factor in rural-urban migration?", "A shortage of farmland and low farm incomes", [
            ("Many jobs in factories", "Jobs in towns are a pull factor."),
            ("Hospitals and colleges in cities", "Services in towns are pull factors."),
            ("Electricity and piped water in towns", "These attract people to towns."),
        ], 0, "Push factors are problems in the countryside that drive people out.",
          "Push factors", "Concept", "Push is about the place people leave."),
        Q("Which is a PULL factor of towns?", "Jobs, schools and hospitals", [
            ("Drought in farming areas", "Drought pushes people out of rural areas."),
            ("Lack of electricity in villages", "That is a push factor."),
            ("Too little farmland per family", "That pushes people away from villages."),
        ], 3, "Pull factors are attractions of the destination town.",
          "Pull factors", "Concept", "Pull is about what attracts people to the town."),
        NUM("In 2000 a country was 32 percent urban. In 2020 it was 47 percent urban. By how many percentage points did the urban share rise?", 15,
            steps=[S("Subtract", math=r"47 - 32 = 15", text="The urban share rose by 15 percentage points.")],
            unit="percentage points", concept="Change in urban share", skill="Calculation", hint="Subtract the earlier percentage from the later one."),
        Q("Which is the smallest type of settlement in the usual settlement hierarchy?", "Hamlet", [
            ("Village", "A village is larger than a hamlet."),
            ("Town", "A town is larger than a village."),
            ("Conurbation", "A conurbation is the largest of these types."),
        ], 1, "In order of size: hamlet, village, town, city, conurbation.",
          "Settlement hierarchy", "Recall", "Order the types from smallest to largest."),
        Q("A conurbation is", "a large urban area formed when several towns and cities grow together", [
            ("a group of farms around one well", "That is a rural cluster."),
            ("a village with a school", "That is a small rural settlement."),
            ("a temporary herders' camp", "That is a temporary rural settlement."),
        ], 2, "A conurbation is a continuous built-up area made by the merging of towns and cities.",
          "Conurbation", "Concept", "Think of the top of the settlement pyramid."),
        Q("Douala handles most of the country's sea trade. Which main function does this show?", "Port and commercial centre", [
            ("Mining centre", "Douala's trade is based on its port."),
            ("Farming village", "Douala is a large city, not a village."),
            ("Religious pilgrimage centre", "The port is a trade function."),
        ], 0, "A port handles imports and exports and so is a port and trade centre.",
          "Functions of towns", "Application", "Which function matches trade by sea?"),
    ]))

# ------------------------------------------------------------------ 8. Urban problems
SETS.append(practice_set(
    module=SET, topic=MORPH, title="Urban problems and possible solutions", lesson="ts-urban-problems-and-solutions",
    questions=[
        Q("What is the main cause of slum growth in fast-growing cities?", "Migrants arrive faster than houses are built, and many cannot afford rent", [
            ("There are too many empty houses", "Slums grow because houses are too few and too costly."),
            ("The government builds too many roads", "Roads do not cause slums."),
            ("Farmers prefer to live in the city centre", "Most poor migrants cannot afford central housing."),
        ], 1, "Housing is too scarce and costly, so poor families build their own homes on cheap, risky land.",
          "Causes of slums", "Concept", "Think about how fast migrants arrive compared with houses."),
        Q("An informal settlement (slum) is", "a settlement built without planning or services such as water and drains", [
            ("a planned estate with good services", "That is a planned housing estate."),
            ("a village of farmers", "That is a rural settlement."),
            ("a new town with factories", "That is a planned industrial town."),
        ], 3, "Informal settlements are built quickly with weak materials and lack basic services.",
          "Informal settlement", "Recall", "Think about 'informal' meaning not planned."),
        Q("Which is a main cause of traffic congestion in a growing town?", "Too many vehicles on narrow roads with little public transport", [
            ("Too few people in the town", "Congestion comes from too many people and vehicles."),
            ("Too many wide roads", "Roads are usually too narrow, not too wide."),
            ("Too many buses and trains", "Too few public transport vehicles encourages more cars."),
        ], 0, "Roads built for a smaller town cannot carry the many vehicles of a larger one.",
          "Traffic congestion", "Concept", "Compare the number of vehicles with the road space."),
        NUM("A family of 12 people shares a house with 3 rooms. How many people share each room on average?", 4,
            steps=[S("Divide people by rooms", math=r"12 \div 3 = 4", text="There are on average 4 people to each room.")],
            unit="persons per room", concept="Overcrowding calculation", skill="Calculation", hint="Divide the number of people by the number of rooms."),
        Q("What is a likely effect of uncollected rubbish in a town?", "Blocked drains, floods and the spread of disease", [
            ("Cleaner rivers", "Rubbish pollutes rivers."),
            ("Fewer mosquitoes", "Rubbish and stagnant water breed mosquitoes."),
            ("Better health", "Poor waste management causes disease."),
        ], 2, "Rubbish blocks drains, which flood, and standing water and waste carry diseases such as cholera.",
          "Effects of waste", "Concept", "Follow what happens to rubbish in drains."),
        Q("Which is a sensible solution to a shortage of housing?", "Build low-cost houses and provide serviced plots", [
            ("Demolish all slums without replacement", "People would be left with nowhere to live."),
            ("Stop schools being built", "That worsens pressure on services."),
            ("Close all clinics", "That would make health problems worse."),
        ], 3, "Low-cost housing and plots with water and drains give poor families safe homes.",
          "Solutions to the housing shortage", "Application", "Which choice adds safe housing?"),
        Q("Which action would best reduce unemployment in towns?", "Support small businesses with training and loans", [
            ("Close small businesses", "That would raise unemployment."),
            ("Encourage more people to leave villages", "More migration adds to the problem."),
            ("Reduce the number of schools", "Less education reduces skills and job chances."),
        ], 1, "Training and loans help people to start work and create jobs.",
          "Solutions to unemployment", "Application", "Which choice creates jobs?"),
        Q("Why can developing other towns and rural areas help the biggest city?", "It reduces the number of people moving to the biggest city", [
            ("It makes the big city grow faster", "Jobs and services elsewhere reduce migration to the big city."),
            ("It removes all traffic from the city at once", "It cuts pressure over time but does not remove traffic at once."),
            ("It stops rural schools being built", "Developing rural areas includes building such services."),
        ], 0, "When other places offer jobs and services, fewer people migrate to the big city, so pressure there falls.",
          "Decentralisation", "Reasoning", "Think about the push and pull factors for migration."),
    ]))

# ------------------------------------------------------------------ 9. Urban fields
FLD = "f5g-ts-urban-field.svg"
FLD_ALT = "Fictitious map of Town T with dashed rings at 5, 12 and 19 km and six villages A to F; the scale bar shows 10 km"
SETS.append(practice_set(
    module=SET, topic=MORPH, title="Urban fields and functional relationships", lesson="ts-urban-fields-and-functional-relationships",
    questions=[
        Q("The urban field (sphere of influence) of a town is", "the area around it that depends on it for goods, services and jobs", [
            ("the area inside the town centre only", "The field includes the surrounding villages."),
            ("the area where the town gets rain", "Rain is a climate matter."),
            ("the largest road in the town", "A road is not an area of influence."),
        ], 0, "The field is the area served by the town and linked to it.",
          "Definition of urban field", "Recall", "Think of the people who use the town's services."),
        Q("Look at the map. Which village lies outside the largest ring around Town T?", "F", [
            ("A", "A is 3 km from the town, inside every ring."),
            ("C", "C is 10 km from the town, inside the 12 km ring."),
            ("E", "E is 17 km from the town, inside the 19 km ring."),
        ], 3, "The largest ring has a radius of 19 km. Village F is 22 km away, so it is outside.",
          "Reading an urban field map", "Interpretation", "Compare each village's distance with the largest ring.",
          diagram=FLD, diagram_alt=FLD_ALT),
        NUM("Look at the map. The outer ring has a radius of 19 km. What is the distance across the whole ring, from one edge to the opposite edge, in km?", 38,
            steps=[S("Diameter is twice the radius", math=r"19 \times 2 = 38", text="The ring is 38 km across.")],
            unit="km", concept="Diameter of an urban field", skill="Calculation", hint="The distance across a circle is twice its radius.",
            diagram=FLD, diagram_alt=FLD_ALT),
        Q("Look at the map. Village E is 17 km from Town T. Where does E lie?", "Inside the 19 km ring but outside the 12 km ring", [
            ("Inside the 5 km ring", "5 km is much less than 17 km."),
            ("Outside the 19 km ring", "17 km is less than 19 km."),
            ("Inside the 12 km ring", "17 km is more than 12 km."),
        ], 1, "17 km is more than 12 km and less than 19 km, so E is between those two rings.",
          "Reading rings on a map", "Interpretation", "Compare 17 with the three ring distances.",
          diagram=FLD, diagram_alt=FLD_ALT),
        Q("Which of these flows goes from the countryside to the town?", "Food, labour and customers", [
            ("Manufactured goods", "They flow from the town to the countryside."),
            ("Hospital and bank services", "The town supplies these services."),
            ("School lessons", "Schools are provided by the town."),
        ], 2, "Villages supply food, workers and customers. The town supplies goods and services.",
          "Functional relationships", "Concept", "What does a town depend on the country for?"),
        Q("Which factor is most likely to make a town's urban field larger?", "Good roads and cheap transport", [
            ("Few services in the town", "A town with few services draws people from a small area."),
            ("Another large town nearby", "A rival town limits the field."),
            ("Steep mountains all around", "Mountains make travel harder, so the field is smaller."),
        ], 3, "Good transport lets more people reach the town's services, so the field widens.",
          "Factors affecting the field", "Concept", "Think about how easy it is to travel to the town."),
        Q("On the map, which service has the greatest range?", "The hospital, bank and college (19 km)", [
            ("The daily shop and primary school (5 km)", "These have the smallest range."),
            ("The weekly market and secondary school (12 km)", "Their range is less than that of the hospital, bank and college."),
            ("All three services have the same range", "The rings show different ranges."),
        ], 0, "The outer ring is the biggest, so its services (hospital, bank, college) are used from farthest away.",
          "Range of a service", "Interpretation", "Look for the biggest ring.",
          diagram=FLD, diagram_alt=FLD_ALT),
        Q("Look at the map. Why is village A more likely than village E to use the daily shop in Town T?", "A is only 3 km away, inside the 5 km range of daily services, while E is 17 km away", [
            ("A is bigger than Town T", "Distance is the key idea, not the size of the village."),
            ("E has no road to any town", "The question is about distance from the town, not about roads."),
            ("Daily shops only serve villages that are far away", "Everyday services have a short range, so near villages use them."),
        ], 1, "Everyday services have a small range. A (3 km) is inside it. E (17 km) is far beyond it.",
          "Range of everyday services", "Reasoning", "Compare each village's distance with the 5 km ring.",
          diagram=FLD, diagram_alt=FLD_ALT),
    ]))
