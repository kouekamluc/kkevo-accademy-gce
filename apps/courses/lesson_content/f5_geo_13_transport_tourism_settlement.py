"""Form 5 Geography: Tertiary industries (transport, telecommunication, tourism) and Settlement Geography
(9 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

ECO = "Economic Activities"
TERT = "Tertiary industries"
SET = "Settlement Geography"
GEN = "General concepts of settlement"
MORPH = "Settlement types and their morphology"


def qz(question, right, wrongs, pos, explanation, hint=""):
    """Quiz helper: `wrongs` is a list of (text, feedback); the right answer is placed at index `pos`."""
    choices = [w[0] for w in wrongs]
    feedback = [w[1] for w in wrongs]
    choices.insert(pos, right)
    feedback.insert(pos, "")
    return QUIZ(question, choices, pos, explanation, hint=hint, feedback=feedback)


LESSONS = []

# ------------------------------------------------------------------ 1. Transport systems
LESSONS.append(lesson(
    module=ECO, topic=TERT,
    title="Transport systems: modes, advantages, disadvantages and impacts",
    slug="ts-transport-systems",
    minutes=22,
    summary="What transport is, the five main modes (road, rail, water, air, pipeline), the strengths and weaknesses of each, and how transport development changes the economy and the environment.",
    objectives=[
        "Define transport and identify the main transport systems",
        "Describe the advantages and disadvantages of each mode of transport",
        "Describe the impacts of transport development on the economy",
        "Describe the impacts of transport development on the environment",
    ],
    key_concepts=["Transport", "Road", "Rail", "Water transport", "Air transport", "Pipeline", "Accessibility", "Impact of transport"],
    blocks=[
        H("Introduction"),
        T("A farmer near Bamenda harvests tomatoes at dawn. By evening the tomatoes must reach a market in Douala. A lorry on a "
          "road takes them there. Cocoa from the South-West may leave through Douala port on a ship. Fuel may arrive through a pipe. "
          "A businessperson may fly from Yaoundé to Garoua in a short time."),
        T("Each of these journeys uses a different **mode** of transport. Tertiary industries such as transport do not make goods. "
          "They move people and goods and so link farms, factories, markets and homes."),
        D("**Transport** is the movement of people, goods and services from one place to another.", title="Transport"),
        KEY("The five main modes", "Geographers group transport systems into five main modes.", cards=[
            ["Road", "Lorries, buses, cars, motorbike taxis, bicycles"],
            ["Rail", "Trains on fixed tracks, such as the line from Douala through Yaoundé to Ngaoundéré"],
            ["Water", "Ships, boats, canoes on the sea (ocean) and on rivers and lakes"],
            ["Air", "Aeroplanes and helicopters, using airports"],
            ["Pipeline", "Pipes that carry oil, gas or water, such as the oil pipeline from Chad to the coast near Kribi"],
        ]),
        IMG("f5g-ts-transport-modes.svg", alt="Table of dots comparing road, rail, water, air and pipeline for speed, low cost for bulk goods, load size and door-to-door service",
            caption="Figure 1. A general comparison of the five modes (3 dots is best). Your answers should explain why."),
        H("Road and rail"),
        T("**Road.** Advantages: roads reach almost every village and farm, so goods can go door to door. Vehicles are easy to find, "
          "cheap to start with, and suit short and medium distances. Disadvantages: lorries carry small loads compared with trains and ships, "
          "so long journeys cost more per tonne. Roads in the rainy season can be cut by floods and landslides. Accidents are common, "
          "and vehicles cause air pollution and noise."),
        T("**Rail.** Advantages: a train can carry very heavy and bulky loads, such as timber, cement, fuel and passengers, over long "
          "distances at a fairly low cost per tonne. It is safe and uses less fuel per tonne than road. Disadvantages: rails are very "
          "expensive to build and maintain. Trains run only where there are tracks, so goods often need a lorry at each end. "
          "Timetables are fixed and a rail line cannot easily change route."),
        H("Water, air and pipeline"),
        T("**Water.** Advantages: ships are the cheapest way to move very large and heavy loads over long distances, such as oil, "
          "minerals, cocoa and containers. Sea routes need no roads built. Disadvantages: water transport is slow. It needs ports, which are costly to build "
          "and keep dredged. Rivers may be too shallow in the dry season (the Benue is only open to boats part of the year) and storms and "
          "oil spills are risks."),
        T("**Air.** Advantages: air is the fastest mode, so it is best for people on long journeys and for urgent or high-value goods "
          "such as medicine, fresh flowers and mail. It crosses mountains, forests and seas. Disadvantages: it is the most expensive "
          "mode. Planes carry small loads, and airports need large land areas and costly equipment. Flights burn a great deal of "
          "fuel, release greenhouse gases and cause noise near airports."),
        T("**Pipeline.** Advantages: once built, a pipeline moves liquids and gases day and night at a low running cost, with little "
          "labour and no traffic. It is safe for goods in bulk. Disadvantages: it is very expensive to build and carries only liquids, "
          "gases or slurries. A leak or an attack on the pipe can cause serious pollution and fire, and the route cannot be changed."),
        H("Impacts of transport development"),
        KEY("Impacts on the economy", "Good transport lets an area trade and grow, but it also has costs.", cards=[
            ["Positive", "Farmers sell crops in distant markets, so food loss falls and incomes rise. Industries and shops open and create jobs. Trade, tourism and towns grow. Schools and clinics are easier to reach."],
            ["Negative", "Building is very costly and may mean debt. Towns on the new road may grow while bypassed villages decline. Cheap imports may reach a region and hurt local producers. Maintenance costs are high."],
        ]),
        KEY("Impacts on the environment", "Transport changes land, air, water and wildlife.", cards=[
            ["Negative", "Forest is cleared for roads and opens land to logging, poaching and farming. Vehicles pollute the air. Oil spills harm rivers and the sea. Noise and loss of farmland. Road building can cause erosion and flooding."],
            ["Positive or reduced harm", "Planned railways and public transport cut pollution per person. Good roads can reduce fuel waste from traffic jams. Strict rules, tree planting and drains can reduce damage."],
        ]),
        H("Model answers"),
        EX("Worked example 1: choosing a mode", intro="A company wants to move 500 tonnes of cement from Douala to a town in the north of Cameroon. Which mode of transport would you advise, and why?", steps=[
            S("Name the mode", text="Rail is a strong choice, with road to finish the journey."),
            S("Give a reason about the goods", text="Cement is heavy and bulky and not urgent. Rail carries large loads cheaply over long distances, so the cost per tonne is lower than by lorry."),
            S("Give a reason about the route", text="A railway already links Douala, Yaoundé and Ngaoundéré, so no new line is needed. Trains are also safer and cause less pollution per tonne than many lorries."),
            S("Mention the weakness", text="Rail stops at Ngaoundéré, so lorries must complete the journey, and train timetables are fixed. Air would be far too costly for cement, and a pipeline carries only liquids."),
        ]),
        EX("Worked example 2: impacts on the economy", intro="Describe two ways in which the building of a new tarred road through a farming area can help the economy.", steps=[
            S("Point 1: better markets", text="Farmers can reach distant towns quickly, so fresh food is sold before it rots. Less food is lost, prices are fairer and farm incomes rise."),
            S("Point 2: new jobs and businesses", text="Road workers, drivers, mechanics, shop owners and traders find work along the road. Villages beside it may grow into small towns with new services."),
            S("Link to the question", text="Both points show how better accessibility raises incomes and encourages trade, which helps the whole economy."),
        ]),
        TIP("Exam link: transport appears in Paper 1 as multiple-choice questions on modes, advantages and impacts. In Paper 2 Section C (human geography) it appears as a "
            "'describe' or 'discuss' question. Always give an advantage AND a disadvantage for each mode you name, and add a Cameroon example.", title="Exam link"),
        MISTAKE("Saying one mode is best for everything", "The best mode depends on the load, the distance, the cost and the speed needed. Rail suits heavy goods over land. Air suits urgent goods. Say why."),
        MISTAKE("Writing only about the economy", "Questions on impacts of development often ask for the economy AND the environment. Give at least one point for each, and name the environmental harm (for example forest clearance or pollution)."),
        qz("Which mode of transport is usually the cheapest for moving very large and heavy loads over a long distance?", "Water (ship)", [
            ("Air", "Air is the fastest mode but also the most expensive. It carries small loads."),
            ("Road", "Lorries are flexible but carry small loads, so the cost per tonne is higher over long journeys."),
            ("Pipeline", "A pipeline is cheap to run but carries only liquids and gases, so it cannot move general cargo."),
        ], 2, "Ships carry huge loads at a low cost per tonne, so the sea and rivers are used for oil, minerals and containers.",
           hint="Think of the biggest vessels you know and what they carry."),
        qz("Which is an advantage of road transport over rail?", "Roads give a door-to-door service", [
            ("Roads carry heavier loads", "Trains carry heavier loads than lorries."),
            ("Roads are cheaper for very long journeys", "Rail and water are cheaper per tonne over long distances."),
            ("Roads cause no pollution", "Vehicles give off fumes and noise."),
        ], 0, "Roads reach farms and homes almost everywhere, so goods need not be moved from one vehicle to another.",
           hint="Think about where a train can and cannot go."),
        PQ("Define transport and name the five main modes.", "**Transport** is the movement of people, goods and services from one place to another. The main modes are road, rail, water, air and pipeline."),
        PQ("Describe two advantages and two disadvantages of air transport.", "Advantages: it is the fastest mode, so it suits long journeys and urgent or high-value goods such as medicine; it can cross mountains, forests and seas. Disadvantages: it is the most expensive mode and carries small loads; airports need much land, and aircraft burn a lot of fuel, causing pollution and noise."),
        PQ("Explain two ways in which transport development can harm the environment.", "First, forest is cleared to build roads and railways. This destroys habitats and a new road opens the forest to logging and poaching. Second, vehicles, ships and aircraft burn fuel and release gases and noise, and oil spills pollute rivers and the sea. Both lower the quality of land, air and water."),
        SUM("Transport is the movement of people, goods and services. The main modes are road, rail, water, air and pipeline.",
            "Road is flexible and gives door-to-door service but carries small loads. Rail and water carry heavy loads cheaply but are inflexible or slow.",
            "Air is the fastest but the most costly. Pipelines are cheap to run but carry only liquids and gases.",
            "Transport development boosts trade, jobs and access to services, but it is costly and can damage forests, air and water."),
    ],
))

# ------------------------------------------------------------------ 2. Telecommunication and the internet
LESSONS.append(lesson(
    module=ECO, topic=TERT,
    title="Telecommunication and the internet",
    slug="ts-telecommunication-and-the-internet",
    minutes=20,
    summary="What telecommunication is, the main systems (telephone, radio, television, satellite, mobile phone, internet), how a satellite link works, and the advantages and disadvantages of the internet.",
    objectives=[
        "Define telecommunication",
        "Identify the main telecommunication systems in the world",
        "Describe how a satellite carries a signal between two places",
        "Discuss the advantages and disadvantages of the internet",
    ],
    key_concepts=["Telecommunication", "Telephone", "Radio and television", "Satellite", "Mobile phone", "Internet", "Digital divide"],
    blocks=[
        H("Introduction"),
        T("A trader in a village near Maroua sends money to a supplier through a mobile phone. A student in Limbe watches a lesson on a "
          "phone. A radio programme warns farmers in the North about the first rains. None of these needs the sender and receiver to "
          "be in the same place. This is telecommunication."),
        D("**Telecommunication** is the sending of information (voice, text, pictures, data) over a distance by cable, radio waves or satellite.", title="Telecommunication"),
        T("Transport moves people and goods. Telecommunication moves **information**. It is also a tertiary industry because it is a service."),
        H("Main telecommunication systems"),
        KEY("Six main systems", "Know these systems and one use of each.", cards=[
            ["Telephone (landline)", "Voice over fixed cables. Reliable but tied to a place and costly to extend to villages."],
            ["Radio", "Voice and music by radio waves. Cheap sets run on batteries, so radio reaches remote villages in local languages."],
            ["Television", "Pictures and sound. It needs electricity and a signal or dish, so it is more common in towns."],
            ["Satellite", "A satellite in space relays signals over very long distances, for TV, phone calls and navigation."],
            ["Mobile phone", "Voice, text and data through radio masts. It has spread quickly where there are no landlines."],
            ["Internet", "A world network of computers linked by cables, masts and satellites. It carries email, web pages, video and money transfers."],
        ]),
        IMG("f5g-ts-satellite-link.svg", alt="A signal goes up from a sender to a satellite and comes down to a receiver far away",
            caption="Figure 1. Why satellites are used: Earth is curved, so a straight radio signal cannot reach far. The satellite relays it."),
        T("Land cables and undersea cables also carry much of the world's phone and internet traffic. Cables lie on the sea floor between continents, and "
          "they come ashore at a few coastal points. The signal then travels inland by cable and mast."),
        H("Advantages and disadvantages of the internet"),
        D("The **internet** is a worldwide network of linked computers and devices that share information.", title="The internet"),
        KEY("Advantages", "Why the internet matters for the economy and for people.", cards=[
            ["Fast communication", "Email and calls reach any place in seconds, cheaply."],
            ["Information and learning", "Students, farmers and health workers can look up facts, prices and weather. Online lessons reach people far from schools."],
            ["Business and jobs", "Shops sell online, workers work from home, and mobile money makes payments easy."],
            ["Services", "Banking, government forms, maps and news can be reached from home."],
        ]),
        KEY("Disadvantages", "Why the internet also brings problems.", cards=[
            ["Cost and access", "Phones, data and electricity are costly. Rural areas often have weak networks, so a digital divide appears between the connected and the unconnected."],
            ["Crime and risks", "Fraud, hacking, false information and loss of private data."],
            ["Health and society", "Too much screen time, distraction from study, bullying and harmful content."],
            ["Jobs", "Online shopping and automation may close some shops and jobs, and a power cut or cable fault can stop services."],
        ]),
        H("Model answers"),
        EX("Worked example 1: discuss the internet", intro="Discuss the advantages and disadvantages of the internet for people in Cameroon.", steps=[
            S("Advantage with explanation", text="Learners in towns and villages can study online, read news and get weather and price information. A trader can send money by mobile phone without travelling, which saves time and cost."),
            S("Second advantage", text="Businesses can advertise and sell to customers far away, and families who live apart stay in touch cheaply."),
            S("Disadvantage with explanation", text="Many rural areas have weak signals, and phones, data and electricity cost too much for poor families. This creates a digital divide."),
            S("Second disadvantage and conclusion", text="Fraud, false information and time wasted can harm users. Overall the internet is helpful, but its benefits are greatest where access is good and users are careful."),
        ]),
        EX("Worked example 2: why radio still matters", intro="Give two reasons why radio is still important in rural Cameroon even though the internet is growing.", steps=[
            S("Reason 1: cost and power", text="A cheap radio runs on batteries, so families without grid electricity or data can still use it."),
            S("Reason 2: reach and language", text="One broadcast reaches many villages at once, in French, English or local languages, and carries farming, health and weather messages. It needs no signal for data."),
        ]),
        TIP("Exam link: telecommunication and the internet appear in Paper 1 as short multiple-choice questions (definitions, systems, advantages and disadvantages) and in Paper 2 Section C as 'discuss'. The syllabus now gives extra weight to internet communication as a contemporary issue.", title="Exam link"),
        MISTAKE("Mixing up transport and telecommunication", "Transport moves people and goods. Telecommunication moves information. A letter sent by lorry is transport; an email is telecommunication."),
        MISTAKE("Listing only advantages", "'Discuss' means give both sides. Add at least one disadvantage, such as the digital divide, cost, crime or false information."),
        qz("What is telecommunication?", "Sending information over a distance by cable, radio waves or satellite", [
            ("Moving goods by lorry or ship", "That is transport, not telecommunication."),
            ("Selling goods in a shop", "That is trade or retail, not telecommunication."),
            ("Printing newspapers", "A printing press makes a product. Telecommunication sends information over distance."),
        ], 0, "Telecommunication sends information (voice, text, pictures, data) over a distance without moving the people.",
           hint="Think about what travels, a person or the message?"),
        qz("Why are satellites used to send signals over very long distances?", "A satellite can relay the signal over the curve of the Earth", [
            ("Satellites are cheaper than all cables", "Cables are often cheaper and carry more data. Satellites are useful where cables do not reach."),
            ("Radio signals cannot travel at all on Earth", "They can, but only over a limited straight distance, and Earth curves."),
            ("Satellites make the signal stronger on the ground", "A satellite relays the signal but does not make it stronger on the ground."),
        ], 0, "Earth is curved, so a straight signal cannot reach far. A satellite high above can see both places and relays the signal.",
           hint="Look at the diagram: what blocks a straight signal?"),
        PQ("Define telecommunication and name three telecommunication systems.", "**Telecommunication** is the sending of information over a distance by cable, radio waves or satellite. Systems include the telephone, radio, television, satellite, mobile phone and the internet."),
        PQ("State two advantages and two disadvantages of the internet.", "Advantages: fast and cheap communication and access to information and learning; it supports business, mobile payments and services. Disadvantages: cost and weak access in rural areas (the digital divide); crime, false information and loss of private data."),
        PQ("Explain why mobile phones have spread faster than landline telephones in rural Africa.", "Landlines need long cables and poles to every home, which is very costly. A mobile mast covers a wide area, so one mast can serve many villages. Phones are also portable, can be prepaid in small amounts, and can be used for mobile money, so more people can afford and use them."),
        SUM("Telecommunication is the sending of information over a distance. Main systems are telephone, radio, television, satellite, mobile phone and the internet.",
            "A satellite relays signals over the curve of the Earth, and cables on land and under the sea carry most traffic.",
            "The internet gives fast communication, information, learning, business and services.",
            "Its disadvantages include cost, weak rural access (the digital divide), crime, false information and over-use."),
    ],
))

# ------------------------------------------------------------------ 3. Tourism types and growth
LESSONS.append(lesson(
    module=ECO, topic=TERT,
    title="Tourism: types, destinations and reasons for growth",
    slug="ts-tourism-types-and-growth",
    minutes=22,
    summary="What tourism is, its main types, tourist potentials of a country, major mass-tourism destinations in LEDCs, NICs and MEDCs, and the reasons why tourism has grown so quickly.",
    objectives=[
        "Define tourism and state the types of tourism",
        "Identify tourist potentials and major destinations for mass tourism in LEDCs, NICs and MEDCs",
        "Outline the reasons for the recent growth of tourism",
    ],
    key_concepts=["Tourism", "Domestic and international tourism", "Eco-tourism", "Tourist potential", "Mass tourism", "LEDC, NIC and MEDC", "Package holiday"],
    blocks=[
        H("Introduction"),
        T("On a weekend, families from Douala travel to the beaches at Limbe and Kribi. Visitors from other countries climb Mount Cameroon "
          "or watch wildlife in the north. All these people are tourists, and the businesses that serve them (hotels, guides, taxis, "
          "restaurants, craft sellers) form the tourist industry, a tertiary industry."),
        D("**Tourism** is the travel of people to places outside their usual home or work area, and their stay there, for leisure, business or other purposes, for a limited time.", title="Tourism"),
        T("A **tourist** stays at least one night and then returns home. A person on a day trip is usually called an excursionist."),
        H("Types of tourism"),
        IMG("f5g-ts-tourism-types.svg", alt="Tree diagram of tourism types: domestic and international, and leisure, business, eco-tourism, cultural, religious and health",
            caption="Figure 1. Tourism can be classified by where tourists come from and by why they travel."),
        KEY("Types by origin", "Where the tourists come from.", cards=[
            ["Domestic tourism", "People travel inside their own country, for example a family from Yaoundé visiting Kribi. It is the largest part of tourism in many countries."],
            ["International tourism", "People cross a border, for example visitors from Europe visiting Cameroon. It earns foreign exchange."],
        ]),
        KEY("Types by purpose", "Why people travel.", cards=[
            ["Leisure", "Rest and fun: beaches, sightseeing, sport and entertainment."],
            ["Business", "Meetings, conferences and trade fairs."],
            ["Eco-tourism", "Visits to natural areas that protect nature and help local people, such as national parks."],
            ["Cultural and religious", "Heritage sites, museums, festivals and pilgrimages."],
            ["Health", "Travel for treatment, rest or spa."],
        ]),
        H("Tourist potentials and destinations"),
        D("**Tourist potential** is the set of natural and human attractions of a place that could draw visitors, such as scenery, wildlife, climate, culture and facilities.", title="Tourist potential"),
        T("Cameroon is often called Africa in miniature because it has beaches, mountains, forests, savanna, lakes and many cultures. "
          "Tourist attractions include the beaches of the Atlantic coast at Limbe and Kribi, Mount Cameroon, the Waza National Park and the "
          "Mandara mountains, the western highlands and chiefdoms (such as Foumban), waterfalls near Kribi, and lakes and forests. "
          "Check your textbook for the other attractions your teacher expects."),
        T("**Mass tourism** is the movement of large numbers of tourists, usually on package holidays, to the same few popular places. Syllabus countries are grouped as "
          "**LEDCs** (less economically developed countries, also called LICs), **NICs** (newly industrialising countries) and **MEDCs** "
          "(more economically developed countries, also called AICs). The lists below are examples. Your textbook may name others."),
        CODE("""
Group     Examples of mass-tourism destinations
LEDC      Kenya (safari parks, coast), Tanzania (Serengeti, Zanzibar),
          The Gambia (beaches), Nepal (Himalaya trekking)
NIC       Thailand (beaches, temples), Mexico (Cancun), Brazil (Rio),
          South Africa (Cape Town, Kruger), India (Taj Mahal, Goa)
MEDC      Spain (Mediterranean beaches), France (Paris, Alps, Riviera),
          Italy (Rome, Venice), USA (Florida, Orlando), Switzerland (Alps)
""", "text", title="Examples (check your textbook for your list)"),
        H("Reasons for recent growth"),
        KEY("Why tourism has grown quickly", "Learn these as groups of reasons and give one explanation for each.", cards=[
            ["More money and time", "Rising incomes, paid holidays and earlier retirement give more people money and leisure time."],
            ["Better transport", "Jet aircraft, cheaper flights, better roads and railways make travel faster and cheaper."],
            ["Easier booking", "Package holidays, travel agents and the internet make planning and payment simple."],
            ["Promotion and media", "Television, social media and advertising make places known. Governments spend on tourism."],
            ["Facilities and peace", "More hotels, airports and parks, better health care and easier visas, and fewer conflicts."],
        ]),
        H("Model answers"),
        EX("Worked example 1: define and classify", intro="Define tourism and state three types of tourism.", steps=[
            S("Definition", text="Tourism is the travel of people outside their usual home or work area, and their stay there, for leisure, business or other purposes."),
            S("Three types", text="Domestic tourism (within the same country), international tourism (across borders) and eco-tourism (visiting natural areas in a way that protects them). Leisure, business, cultural and health tourism are other types."),
        ]),
        EX("Worked example 2: reasons for growth", intro="Outline three reasons for the rapid growth of tourism in recent years.", steps=[
            S("Reason 1: better transport", text="Fast aircraft and cheaper flights make long journeys quicker and more affordable, so more people can reach distant places."),
            S("Reason 2: higher incomes and leisure time", text="More people earn enough to spend on holidays, and paid leave and retirement give them free time."),
            S("Reason 3: easier booking and promotion", text="Package holidays and online booking make arrangements simple, and media and advertising make destinations famous."),
        ]),
        TIP("Exam link: tourism is tested in Paper 1 (definitions, types, destinations) and in Paper 2 Section C (human geography) as 'outline' or 'discuss' questions. In Section D you may use Cameroon's tourist potential.", title="Exam link"),
        MISTAKE("Defining tourism as only foreign visitors", "Domestic tourists are tourists too. Always mention both domestic and international tourism."),
        MISTAKE("Naming a destination without saying what attracts tourists", "Write the attraction as well, for example 'Kenya: safari parks and coast', so the examiner sees you know why tourists go there."),
        qz("A family from Yaoundé spends a weekend at Kribi beach. What type of tourism is this?", "Domestic leisure tourism", [
            ("International business tourism", "The family stays in its own country and travels for rest, not for work."),
            ("Eco-tourism only", "The trip is for the beach. Eco-tourism is about protecting natural areas."),
            ("Cultural tourism", "The reason for travel is the beach, not heritage or festivals."),
        ], 0, "They travel inside their own country (domestic) and for rest and fun (leisure).",
           hint="Ask two questions: did they cross a border? Why did they go?"),
        qz("Which is a reason for the rapid growth of tourism in recent years?", "Faster and cheaper transport, especially air travel", [
            ("Shorter holidays for workers", "The opposite happened. Paid holidays have increased."),
            ("Fewer destinations are advertised", "Advertising has increased through media and the internet."),
            ("Travel has become slower", "Jet aircraft and better roads have made it faster."),
        ], 0, "Better and cheaper transport, higher incomes, more leisure time and easy booking have all increased tourism.",
           hint="Think about what has changed about how people travel."),
        PQ("Define tourism and name two types.", "**Tourism** is the travel of people outside their usual home or work area, and their stay there, for leisure, business or other purposes. Two types are domestic tourism and international tourism (also leisure, business and eco-tourism)."),
        PQ("Name two major mass-tourism destinations in LEDCs, two in NICs and two in MEDCs, and state one attraction of each.", "LEDCs: Kenya (safari parks) and Tanzania (Serengeti, Zanzibar beaches). NICs: Thailand (beaches and temples) and South Africa (Cape Town and Kruger wildlife). MEDCs: Spain (sunny Mediterranean beaches) and France (Paris, Alps and Riviera). Other examples in your textbook are also correct."),
        PQ("Outline four reasons for the recent growth of tourism.", "Higher incomes mean more people can pay for holidays. More leisure time through paid holidays and retirement. Faster, cheaper transport, especially air travel. Package holidays and online booking make trips easy to arrange, and advertising and media make places known. More hotels, airports and safer, more peaceful destinations also help."),
        SUM("Tourism is travel outside one's usual area for leisure, business or other purposes. Types include domestic and international, leisure, business, eco, cultural and health.",
            "Tourist potential is the natural and human attractions of a place. Cameroon has beaches, mountains, parks, culture and varied landscapes.",
            "Mass tourism goes to a few popular places, for example Kenya (LEDC), Thailand (NIC) and Spain (MEDC).",
            "Growth is due to higher incomes, more leisure time, better transport, easy booking, media promotion and better facilities."),
    ],
))

# ------------------------------------------------------------------ 4. Tourism challenges and impacts
LESSONS.append(lesson(
    module=ECO, topic=TERT,
    title="Tourism: challenges, advantages and disadvantages",
    slug="ts-tourism-challenges-and-impacts",
    minutes=22,
    summary="The obstacles that hold back the tourist industry, and the advantages and disadvantages of tourism for the economy and the environment, including the multiplier effect and leakage.",
    objectives=[
        "Identify the obstacles and challenges facing the tourist industry",
        "Outline the advantages of tourism for the economy and the environment",
        "Outline the disadvantages of tourism for the economy and the environment",
        "Explain the multiplier effect and leakage",
    ],
    key_concepts=["Obstacles to tourism", "Foreign exchange", "Multiplier effect", "Leakage", "Seasonal employment", "Sustainable tourism"],
    blocks=[
        H("Introduction"),
        T("A beach at Limbe or Kribi may be beautiful. Yet tourists will come only if they can reach it, feel safe, find a clean room and "
          "a good meal, and know the place exists. Many countries with great attractions still receive few tourists. This lesson looks at why, "
          "and at what tourism does to a country when it does grow."),
        H("Obstacles facing the tourist industry"),
        D("An **obstacle** (or hindrance) is anything that stops or slows the growth of tourism in a country or region.", title="Obstacles"),
        KEY("Common obstacles", "Group your points so that your answer is clear.", cards=[
            ["Access and transport", "Poor roads, few flights, high air fares and long journeys from main airports to the attractions."],
            ["Facilities and services", "Too few good hotels, poor water and electricity, weak telecommunication and untrained staff."],
            ["Safety and stability", "Insecurity, political unrest, crime, disease risks and fear of poor health care."],
            ["Money and promotion", "Little capital to build hotels, weak advertising, strict visa rules and competition from better-known countries."],
            ["Nature and seasons", "Heavy rains can close roads. Tourist numbers rise and fall with the seasons. Poaching and pollution destroy the very attractions that tourists come to see."],
        ]),
        H("Impacts on the economy"),
        IMG("f5g-ts-tourism-multiplier.svg", alt="Diagram: tourist spending flows to hotels, transport and crafts, then to farmers, builders and workers, whose wages are spent again; some money leaks out of the country",
            caption="Figure 1. The multiplier effect and leakage."),
        D("The **multiplier effect** happens when money spent by tourists is spent again and again in the local economy, creating more income and jobs than the first payment alone.", title="Multiplier effect"),
        D("**Leakage** is money paid by tourists that leaves the local economy, for example profits sent to foreign owners of hotels and payments for imported food and goods.", title="Leakage"),
        KEY("Advantages for the economy", "Tourism can help a country grow.", cards=[
            ["Jobs and incomes", "Hotels, restaurants, transport, guiding, crafts and farming employ many people, including women and young people."],
            ["Foreign exchange and taxes", "International tourists bring foreign money, and governments collect taxes and fees."],
            ["Development", "Roads, airports, water and electricity built for tourists also help local people. Local farmers and craft makers find new markets."],
        ]),
        KEY("Disadvantages for the economy", "The gains are not always shared fairly.", cards=[
            ["Leakage", "When foreign companies own the hotels and tour firms, much of the money leaves the country."],
            ["Seasonal and low-paid jobs", "Workers may have no work in the low season, and many jobs pay little."],
            ["Dependence and rising prices", "If an area depends on tourists, a crisis (disease, insecurity, falling visitors) causes hardship. Land and food prices may rise for local people."],
        ]),
        H("Impacts on the environment"),
        KEY("Advantages for the environment", "Well-managed tourism can protect nature.", cards=[
            ["Money for conservation", "Park fees pay for rangers and reserves."],
            ["Reason to protect", "Local people see that forests, wildlife and clean beaches earn money, and tourists learn to care about nature."],
        ]),
        KEY("Disadvantages for the environment", "Large numbers of visitors can damage the attraction itself.", cards=[
            ["Pollution and litter", "Rubbish on beaches and trails, sewage from hotels, and noise and exhaust from vehicles."],
            ["Damage to land and wildlife", "Footpaths erode, forest is cleared for hotels, wildlife is disturbed or hunted, and coral, dunes and mangroves are damaged."],
            ["Heavy use of resources", "Hotels use large amounts of water and energy, which may leave less for local people."],
        ]),
        T("**Sustainable tourism** means managing tourism so that visitors enjoy a place without using it up, so that local people and nature gain, and so that future visitors can enjoy it as well."),
        H("Model answers"),
        EX("Worked example 1: obstacles", intro="Outline three obstacles facing the tourist industry in a developing country.", steps=[
            S("Obstacle 1: poor transport", text="Many attractions are far from airports and the roads are poor, especially in the rainy season, so journeys are long and costly."),
            S("Obstacle 2: poor facilities", text="There are too few good hotels and the supply of water and electricity is unreliable. Staff may lack training, so visitors are not satisfied."),
            S("Obstacle 3: insecurity and weak promotion", text="Insecurity or disease scares visitors away. With little money for advertising, the country is not known to tourists."),
        ]),
        EX("Worked example 2: balanced discussion", intro="Discuss the advantages and disadvantages of tourism for the economy of a country such as Kenya or Cameroon.", steps=[
            S("Advantage", text="Tourism creates jobs for hotel staff, guides, drivers and traders and earns foreign exchange. Money is spent again in local shops and markets, a multiplier effect."),
            S("Second advantage", text="Roads, airports and utilities built for visitors also serve local people, and farmers gain new customers."),
            S("Disadvantage", text="Where hotels are owned by foreign firms, much money leaks out. Jobs may be seasonal and low paid, and the country is at risk if visitors stop coming."),
            S("Conclusion", text="Tourism can help the economy if local people own businesses, buy local goods and the industry is spread throughout the year."),
        ]),
        TIP("Exam link: tourism impacts appear in Paper 1 and in Paper 2 Section C, often as 'outline the advantages and disadvantages of tourism on the economy and the environment'. Use four headed points: economic advantage, economic disadvantage, environmental advantage, environmental disadvantage.", title="Exam link"),
        MISTAKE("Giving only the benefits", "Many candidates write only about jobs and money. The syllabus asks for both advantages and disadvantages, and for both economy and environment."),
        MISTAKE("Confusing multiplier and leakage", "The multiplier effect keeps money circulating inside the area. Leakage is money that leaves it. Do not swap them."),
        qz("Which of the following is an obstacle to the growth of tourism?", "Poor roads and few good hotels", [
            ("High incomes in tourists' home countries", "Higher incomes make travel easier for tourists; they are not an obstacle."),
            ("A reliable electricity supply", "Reliable utilities help tourism."),
            ("Cheap air fares", "Cheap flights help tourism."),
        ], 0, "Poor access and facilities discourage visitors and reduce the number who come.",
           hint="Which choice makes it harder for tourists to arrive or stay?"),
        qz("What is leakage in tourism?", "Money spent by tourists that leaves the local economy", [
            ("Water spilt in hotels", "Leakage in this topic means money, not water."),
            ("Money that is spent again in local shops", "That is the multiplier effect."),
            ("Tourists who leave early", "Leakage is about money, not about visitors."),
        ], 1, "Leakage includes profits sent abroad and spending on imported goods, so the local area gains less.",
           hint="Look at the brown arrow in Figure 1."),
        PQ("State three obstacles facing the tourist industry in a developing country.", "Poor transport and few flights; too few good hotels and unreliable water and electricity; insecurity or disease; little money for advertising and strict visa rules; untrained staff."),
        PQ("Outline two advantages and two disadvantages of tourism for the economy.", "Advantages: jobs and incomes for local people, and foreign exchange and taxes for the government; also better roads and services. Disadvantages: leakage of money abroad, especially when hotels have foreign owners; seasonal and low-paid jobs; dependence on visitors and rising prices for local people."),
        PQ("Explain two ways in which tourism can damage the environment.", "Large numbers of visitors cause litter, sewage and noise, which pollute beaches, rivers and the air. Footpaths erode and forest, dunes or mangroves are cleared for hotels, and wildlife is disturbed. These changes reduce the beauty and quality of the attraction."),
        PQ("Explain how tourism can help to protect the environment.", "Park entry fees and taxes pay for rangers and reserves, so wildlife and forests are protected. Local people who earn from tourists see a reason to protect nature rather than clear or hunt it, and visitors learn to value nature. This works best when tourism is managed sustainably."),
        SUM("Obstacles include poor transport and facilities, insecurity, disease, lack of money and promotion, and seasonality.",
            "Economic advantages: jobs, foreign exchange, taxes, development and the multiplier effect.",
            "Economic disadvantages: leakage, seasonal low-paid jobs, dependence and rising prices.",
            "Environmental effects: conservation funding can help; pollution, erosion, habitat loss and heavy resource use can harm. Sustainable tourism reduces the harm."),
    ],
))

# ------------------------------------------------------------------ 5. What is settlement
LESSONS.append(lesson(
    module=SET, topic=GEN,
    title="What is a settlement? Types, site, situation and siting factors",
    slug="ts-what-is-settlement-site-and-situation",
    minutes=22,
    summary="What a settlement is, how settlements are classified, the difference between site and situation, the main factors that influence where settlements are sited, and how rural and urban settlements differ.",
    objectives=[
        "Define settlement and identify types of settlement",
        "Differentiate between site and situation",
        "Outline the main factors in siting settlements",
        "Differentiate between rural and urban settlements",
    ],
    key_concepts=["Settlement", "Permanent and temporary settlement", "Site", "Situation", "Siting factors", "Rural settlement", "Urban settlement"],
    blocks=[
        H("Introduction"),
        T("Think of the place where you live: a village near Bamenda, a quarter of Douala, a compound on the road to Maroua. People "
          "built there for reasons. Perhaps a spring was close, the ground was flat and dry, or two roads met."),
        D("A **settlement** is a place where people live and build homes, together with the buildings, roads and land they use.", title="Settlement"),
        H("Types of settlement"),
        KEY("Ways to classify settlements", "Learn one example of each.", cards=[
            ["Permanent", "People live there all year, such as most villages and all towns."],
            ["Temporary", "People stay for a short time, for example seasonal fishing camps on Lake Chad or herders' camps on the Adamawa plateau."],
            ["Rural", "Small, with farming, fishing or herding as the main work: hamlets and villages."],
            ["Urban", "Large, with trade, services, industry and government as the main work: towns and cities."],
            ["By shape (pattern)", "Nucleated (clustered), dispersed (scattered) and linear (in a line). This is the next lesson."],
        ]),
        H("Site and situation"),
        D("The **site** of a settlement is the actual piece of land on which it is built.", title="Site"),
        D("The **situation** of a settlement is its position in relation to the places and features around it: roads, rivers, other towns, hills and resources.", title="Situation"),
        IMG("f5g-ts-site-situation-map.svg", alt="Fictitious map of Ngomo village on dry ground near a river bend, with a stream from Mt Boko and a road 8 km west of Essima market town",
            caption="Figure 1. Site and situation of Ngomo (a fictitious village). The scale bar shows 5 km."),
        T("In Figure 1 the **site** of Ngomo is a patch of dry, raised ground above the marsh and the river, with a stream nearby. "
          "Its **situation** is eight kilometres west of the market town Essima on the main road, south of Mt Boko."),
        H("Factors that influence siting"),
        KEY("Siting factors", "Settlements grow where people can find what they need and stay safe.", cards=[
            ["Water supply", "Springs, rivers and wells for drinking and farming. Many villages grow at a spring or on a river terrace."],
            ["Dry, level site", "A dry point above flood level, with flat or gently sloping ground for building, avoiding marsh and steep slopes."],
            ["Fertile soil and farmland", "Good soil for crops, such as volcanic soils around Mount Cameroon."],
            ["Building materials and fuel", "Stone, clay, timber, thatch and firewood close by."],
            ["Defence and shelter", "Hills or river bends that were safe from attack, and sites sheltered from strong winds and floods. Some villages in the Mandara mountains were built high for defence."],
            ["Resources and jobs", "Minerals, timber, fishing grounds, a harbour or salt, which draw people to a place."],
            ["Accessibility", "Crossroads, bridging points of rivers and sheltered harbours, such as the Wouri estuary at Douala, help trade."],
        ]),
        H("Rural and urban settlements compared"),
        CODE("""
Feature        Rural settlement           Urban settlement
Size           Small (hamlet, village)    Large (town, city)
Main work      Farming, fishing, herding  Trade, services, industry, government
Density        Few people per km2         Many people per km2
Services       Few: primary school,       Many: hospitals, banks, colleges,
               small market, church       shops, offices
Land use       Fields, forest, houses     Buildings, roads, factories, markets
Buildings      Mostly low, spread out     Dense, often tall, close together
""", "text", title="Rural and urban compared"),
        H("Model answers"),
        EX("Worked example 1: site and situation", intro="Differentiate between the site and the situation of a settlement. Use Douala as an example.", steps=[
            S("Define site", text="The site is the actual land on which a settlement stands. Douala is built on low land beside the Wouri estuary, close to the sea."),
            S("Define situation", text="The situation is the position of the settlement in relation to other places. Douala lies on the coast at the point where the Wouri meets the sea, with road and rail links to Yaoundé and the interior."),
            S("State the difference", text="Site describes the local ground. Situation describes the wider location and links, so a place can have a poor site but a good situation."),
        ]),
        EX("Worked example 2: siting factors", intro="Outline three factors that influence the siting of a village.", steps=[
            S("Factor 1: water", text="People need water for drinking, washing and farming, so villages grow near springs, streams or rivers."),
            S("Factor 2: dry, flat land", text="A dry point above flood level on gently sloping ground is good for building and avoids malaria-breeding marsh."),
            S("Factor 3: farmland or defence", text="Fertile soil nearby feeds the village. In times of conflict, a hilltop or river bend gave protection from attack."),
        ]),
        EX("Worked example 3: rural and urban", intro="State three differences between a rural and an urban settlement.", steps=[
            S("Size and density", text="Rural settlements are small with few people per square kilometre. Urban settlements are large and crowded."),
            S("Work", text="Most rural people farm, fish or herd animals. Most urban people work in trade, services, industry or government."),
            S("Services", text="Villages have few services, such as a primary school and a small market. Towns have hospitals, banks, secondary schools and many shops."),
        ]),
        TIP("Exam link: site and situation and siting factors are favourite Paper 1 multiple-choice topics, and Paper 2 Section C asks 'differentiate between' or 'outline factors'. Draw a small annotated sketch map to show a site, with labels for water, dry ground, farmland and roads.", title="Exam link"),
        MISTAKE("Using site and situation as if they meant the same", "Site is the actual spot (ground, slope, water). Situation is the position in relation to other places. Use both words in your answer."),
        MISTAKE("Giving factors without explaining them", "Writing 'water' scores less than 'water, because people need it for drinking and farming, so villages grow beside springs and rivers'."),
        qz("Which statement describes the SITUATION of a settlement?", "It lies 8 km west of a market town on the main road", [
            ("It is built on a dry, raised piece of ground", "That describes the site, the actual ground."),
            ("It stands on gently sloping, fertile land", "That also describes the site."),
            ("It has clay soil and timber nearby", "Soil and materials describe the ground and resources of the site."),
        ], 0, "Situation links the settlement to other places: distance, direction and roads to the surroundings.",
           hint="Look for the choice that compares the place to something else."),
        qz("Why do many villages in wet tropical areas avoid marshy land?", "It floods and spreads disease and is unsuitable for building", [
            ("It is too far from rivers", "Marshy land is usually right beside water."),
            ("It has no soil", "Marsh has plenty of soil, but it is waterlogged."),
            ("It is the best place for defence", "Marsh is not a good defensive site; people avoided it because it floods and breeds mosquitoes."),
        ], 3, "People choose a dry point so that houses stay dry and healthy.",
           hint="Think of what happens to buildings and health in standing water."),
        PQ("Define settlement and name two types of settlement.", "A **settlement** is a place where people live and build homes, together with the buildings and land they use. Types include rural and urban, permanent and temporary settlements."),
        PQ("Differentiate between site and situation.", "The **site** is the actual ground on which a settlement is built, for example a dry raised terrace beside a stream. The **situation** is its position in relation to other places and features, such as 8 km from a market town on the main road."),
        PQ("Outline four factors that influence the siting of a settlement.", "Water supply from springs and rivers; a dry, level site above flood level; fertile soil for farming; building materials and fuel nearby; defence or shelter (hills, river bends); resources such as minerals or a harbour; and accessibility along routes and river crossings."),
        PQ("State three differences between rural and urban settlements.", "Rural settlements are small, have few people per square kilometre and few services, and most people farm. Urban settlements are large, crowded, have many services and most people work in trade, industry and services."),
        SUM("A settlement is a place where people live and build homes. Types include permanent and temporary, and rural and urban.",
            "Site is the actual ground of the settlement. Situation is its position in relation to places around it.",
            "Siting factors include water, dry level land, fertile soil, building materials, defence and shelter, resources and accessibility.",
            "Rural settlements are small and farm-based. Urban settlements are large and based on trade, industry and services."),
    ],
))

# ------------------------------------------------------------------ 6. Rural settlement patterns
LESSONS.append(lesson(
    module=SET, topic=MORPH,
    title="Rural settlement patterns: nucleated, dispersed and linear",
    slug="ts-rural-settlement-patterns",
    minutes=20,
    summary="The three main patterns of rural settlement (nucleated, dispersed and linear), the factors that produce each pattern, how to recognise them on a map, and how to draw and annotate a sketch map.",
    objectives=[
        "Outline the types of rural settlement",
        "Illustrate the patterns of rural settlement with sketch maps",
        "Explain the factors that lead to nucleated, dispersed and linear patterns",
    ],
    key_concepts=["Rural settlement", "Nucleated pattern", "Dispersed pattern", "Linear pattern", "Hamlet and village", "Sketch map"],
    blocks=[
        H("Introduction"),
        T("Fly over the Western Highlands, the forests of the South or the plains near Maroua and you would see very different "
          "arrangements of houses. In one place houses are packed round a market or chief's compound. In another, farms are far apart "
          "with a house in each field. In another, houses line the main road."),
        D("A **rural settlement** is a small settlement, such as a hamlet or village, where the main work is farming, fishing or herding.", title="Rural settlement"),
        D("A **settlement pattern** is the shape formed by the buildings of a settlement when seen on a map or from the air.", title="Settlement pattern"),
        IMG("f5g-ts-rural-patterns.svg", alt="Three sketch maps: nucleated houses clustered round a centre, dispersed farms scattered across the area, and linear houses along a road",
            caption="Figure 1. Three patterns of rural settlement. Squares are houses; dashed shapes show the land they use."),
        H("Nucleated settlement"),
        D("A **nucleated** settlement is one in which houses are close together round a centre, such as a well, market, chief's compound or crossroads, with farmland outside.", title="Nucleated"),
        T("**Factors.** A single water source, such as a spring, a well or a waterhole, so people gather near it. Defence: living together was safer in times of "
          "attack. Shortage of good land or a steep, rugged site, so houses are packed on the flat part. A tradition of living in "
          "kin groups round a chief or religious building. Shared services such as market, school or church."),
        H("Dispersed settlement"),
        D("A **dispersed** (scattered) settlement is one in which farms and houses lie far apart, each in its own land.", title="Dispersed"),
        T("**Factors.** Plenty of land and water everywhere, so no need to cluster. Farms are large or crops need space, for example plantations and cattle ranching. "
          "Safe times, with no need for defence. Individual land ownership. Dense forest or hilly land that makes clearing a large flat area impractical. "
          "Many cocoa farming areas and parts of the highlands have scattered farmsteads. Check your textbook for the examples your teacher uses."),
        H("Linear settlement"),
        D("A **linear** settlement is one in which houses are built in a line, along a road, river, railway, valley or coast.", title="Linear"),
        T("**Factors.** A road or railway gives easy access to transport and trade. A river, stream or spring line gives water along one edge. "
          "A narrow valley, a coast, a dyke or a ridge leaves only a strip of dry land. Many villages in Cameroon have grown as strings of houses beside the main roads."),
        T("Some textbooks add other forms, such as a planned or grid pattern in resettlement schemes, and a mixed pattern in which a village has a nucleus and scattered farms around it. For the exam, concentrate on the three main patterns."),
        H("How to draw and describe a pattern"),
        KEY("Four-step method for a sketch map", "Use this in Paper 2.", cards=[
            ["1. Frame", "Draw a rectangle. Add a title and a north arrow or scale if needed."],
            ["2. Features", "Draw the key features: road, river, hill, well or market."],
            ["3. Houses", "Draw small squares: clustered for nucleated, far apart for dispersed, in a line for linear."],
            ["4. Label", "Name the pattern and write one or two factors on the map."],
        ]),
        H("Model answers"),
        EX("Worked example 1: describe and explain", intro="Describe one pattern of rural settlement and explain why it occurs. Illustrate with a sketch map.", steps=[
            S("Name and describe", text="Nucleated settlement: houses are close together round a centre, such as a spring or market, with fields round the edge."),
            S("Explain", text="People cluster where water is scarce and comes from one spring. In the past it was safer to live together. Shared services such as the market and school also draw houses together."),
            S("Sketch map", text="Draw a circle of small squares round a blue square marked 'spring', with dashed fields outside. Label it 'nucleated: water and defence'."),
        ]),
        TIP("Exam link: patterns of rural settlement are often tested in Paper 1 with a sketch like Figure 1 and in Paper 2 Section C as 'illustrate and explain'. Draw a neat labelled sketch to earn marks; one or two sketches with labels are worth a lot.", title="Exam link"),
        MISTAKE("Drawing houses without a reason", "A sketch map is not decoration. Add the road, river or well that explains the pattern, and label it."),
        qz("A village in which houses stand in a line on both sides of a main road is called", "linear", [
            ("nucleated", "Nucleated houses are clustered round a centre, not stretched along one line."),
            ("dispersed", "Dispersed farms are scattered, far apart."),
            ("planned grid", "A grid has streets crossing at right angles, not one line of houses."),
        ], 2, "Houses strung along a road form a linear pattern.",
           hint="Picture a line of houses on a map."),
        qz("Which factor is most likely to produce a nucleated village?", "A single spring in an area where water is scarce", [
            ("Plenty of land and water everywhere", "That favours scattered farms."),
            ("Large cattle ranches", "Ranches need space, so houses are far apart."),
            ("A peaceful time with no need for defence", "In a peaceful, land-rich area houses can spread out."),
        ], 0, "Scarce water draws houses together round the one source, and defence and shared services act in the same way.",
           hint="Which choice makes people gather in one place?"),
        PQ("Name and describe the three main patterns of rural settlement.", "Nucleated: houses are clustered round a centre such as a spring, market or crossroads. Dispersed: farms and houses are scattered, far apart, each on its own land. Linear: houses are built in a line along a road, river, railway, valley or coast."),
        PQ("Explain two factors that lead to a linear settlement pattern.", "First, a road or railway gives easy transport and trade, so people build beside it and the houses form a line. Second, a river, spring line or narrow valley provides water along one edge, or the dry land is limited to a narrow strip, so the houses are strung out along it."),
        PQ("Explain two factors that lead to a dispersed settlement pattern.", "Land and water are plentiful everywhere, so people need not cluster near one source. Farms are large, for example plantations, so each family lives on its own land. In safe times with no need for defence, and where land is individually owned, farmers prefer to live beside their fields."),
        PQ("Draw a labelled sketch map of a nucleated settlement and explain it.", "Sketch a rectangle with a small square in the middle labelled 'spring and market', ring after ring of small squares round it (houses), a dashed outline for fields outside, and the title 'Nucleated settlement'. Explanation: water is at one place, so houses gather round it, and living together gives safety and shared services."),
        SUM("Rural settlement patterns are nucleated (clustered round a centre), dispersed (scattered) and linear (in a line).",
            "Nucleated: a single water source, defence, scarce land or shared services.",
            "Dispersed: plenty of land and water, large farms, safety and individual ownership.",
            "Linear: a road, railway, river, valley, coast or ridge. In the exam, draw a labelled sketch."),
    ],
))

# ------------------------------------------------------------------ 7. Urbanisation and types of urban settlement
LESSONS.append(lesson(
    module=SET, topic=MORPH,
    title="Urbanisation and types of urban settlement",
    slug="ts-urbanisation-and-types-of-urban-settlement",
    minutes=22,
    summary="What urbanisation is, why towns in Africa and other developing regions are growing so fast (rural push and urban pull), and the types of settlement from hamlet to conurbation, with the functions of towns.",
    objectives=[
        "Define urbanisation",
        "Describe the reasons for rapid urbanisation",
        "Identify the various types of urban settlement",
        "Identify the main functions of towns and cities",
    ],
    key_concepts=["Urbanisation", "Rural-urban migration", "Push and pull factors", "Natural increase", "Hamlet, village, town, city, conurbation", "Urban functions"],
    blocks=[
        H("Introduction"),
        T("Every year more young people leave farms and villages in the Western Highlands, the North and the East and move to Douala, "
          "Yaoundé, Bafoussam and Garoua. Markets grow bigger, new quarters appear at the edge of towns, and "
          "traffic gets heavier. This is happening across Africa and Asia."),
        D("**Urbanisation** is the increase in the proportion (share) of a country's people who live in towns and cities.", title="Urbanisation"),
        T("Do not confuse this with **urban growth**, which is the increase in the number of people living in towns. A country can have urban growth without much "
          "urbanisation if the whole population grows at the same rate."),
        KEY("Measuring urbanisation", "Percentage urban = urban population divided by total population, times 100.", cards=[
            ["Example", "If 4 million of 10 million people live in towns, the country is 40 percent urban."],
            ["Change", "If this rises to 55 percent, urbanisation has increased by 15 percentage points."],
        ]),
        H("Why is urbanisation so rapid?"),
        IMG("f5g-ts-push-pull.svg", alt="Push factors in rural areas (shortage of land, low incomes, few services) and pull factors of towns (jobs, schools, hospitals) with an arrow of migration between them",
            caption="Figure 1. Push factors drive people out of the countryside. Pull factors draw them to towns."),
        KEY("Main reasons", "Learn them as groups.", cards=[
            ["Rural push", "Shortage of farmland, low farm incomes, drought or soil exhaustion, few schools, clinics, electricity and water, few jobs outside farming, and insecurity or conflict in some areas."],
            ["Urban pull", "Jobs and higher wages, schools and colleges, hospitals, electricity, piped water, markets, entertainment, and the hope of a better life."],
            ["Natural increase", "Towns grow because there are more births than deaths, and because young migrants have children in town."],
            ["Other causes", "Industry and government investment concentrate in towns. Better roads and telephones make it easy to move. Nearby villages may be swallowed by the growing town."],
        ]),
        H("Types of settlement from hamlet to conurbation"),
        IMG("f5g-ts-settlement-ladder.svg", alt="Pyramid of settlement types from hamlet at the base through village, town and city to conurbation at the top",
            caption="Figure 2. The settlement hierarchy. The higher the level, the fewer the settlements, and the bigger and more varied the services."),
        KEY("The main types", "Sizes differ from country to country, so describe by function and services too.", cards=[
            ["Hamlet", "A very small rural settlement with a few houses and almost no services."],
            ["Village", "A larger rural settlement with a school, a church or mosque and a small market."],
            ["Town", "An urban settlement with many shops, a market, secondary schools, a health centre and banks. Most people do not farm."],
            ["City", "A very large town with a wide range of services (university, hospital, airport, head offices) and a large sphere of influence."],
            ["Conurbation", "A large urban area formed when several towns and cities grow together, such as Greater Manchester in the United Kingdom or the Ruhr in Germany."],
        ]),
        H("Functions of towns"),
        T("The **function** of a town is the main work it does. Many towns have more than one function."),
        CODE("""
Function            Example in Cameroon (check your textbook)
Capital and         Yaounde (national capital); regional capitals such as
administration      Bamenda, Buea, Maroua, Garoua, Bertoua
Port and trade      Douala (main port), Kribi, Limbe
Market and trade    Bafoussam, Maroua
Industry            Douala; Edea (aluminium)
Tourism and resort  Limbe and Kribi (beaches)
Route centre        Ngaoundere (rail terminus)
""", "text", title="Functions of towns"),
        H("Model answers"),
        EX("Worked example 1: calculate urbanisation", intro="In a country of 20 million people, 9 million live in towns. Calculate the percentage urban population.", steps=[
            S("Write the formula", text="Percentage urban = urban population divided by total population, times 100."),
            S("Substitute", math=r"\frac{9}{20} \times 100"),
            S("Answer", math=r"= 45\%", text="The country is 45 percent urban."),
        ]),
        EX("Worked example 2: reasons for rapid urbanisation", intro="Describe three reasons for rapid urbanisation in developing countries.", steps=[
            S("Rural push", text="Farmland is short and farm incomes are low, and villages lack schools, clinics and electricity, so many young people leave."),
            S("Urban pull", text="Towns offer jobs, better wages and services such as hospitals and colleges, so people move in the hope of a better life."),
            S("Natural increase", text="Towns also grow because more people are born than die there, and migrants have children in town."),
        ]),
        EX("Worked example 3: types and functions", intro="Name three types of urban settlement and state one function of a town.", steps=[
            S("Types", text="Town, city and conurbation. A town is smaller, a city is larger with more services, and a conurbation is formed when towns and cities join together."),
            S("Function", text="Douala is a port and commercial centre, because goods enter and leave the country through its port."),
        ]),
        TIP("Exam link: urbanisation is tested in Paper 1 (definitions, push and pull, types of settlement, percentage calculations) and in Paper 2 Section C as 'describe the reasons for rapid urbanisation'. In Section D use Douala and Yaoundé as Cameroon examples.", title="Exam link"),
        MISTAKE("Defining urbanisation as 'growth of towns'", "It is the increase in the proportion of people living in towns. Growth of town population is urban growth."),
        MISTAKE("Writing only pull factors", "A full answer gives both push (why people leave the countryside) and pull (why towns attract them)."),
        qz("Which of the following is a PUSH factor causing rural-urban migration?", "Shortage of farmland and low farm incomes", [
            ("Good hospitals in towns", "Services in towns are a pull factor."),
            ("Many jobs in factories", "Jobs in towns are a pull factor."),
            ("Electricity and piped water in cities", "These attract people to towns, so they are pull factors."),
        ], 0, "Push factors are the problems of the rural area that drive people out.",
           hint="Push factors are about the place people leave."),
        qz("A very large urban area formed when several towns have grown together is called a", "conurbation", [
            ("hamlet", "A hamlet is a few houses in the countryside."),
            ("village", "A village is a small rural settlement."),
            ("market town", "A market town is a single town and not a merged urban area."),
        ], 1, "A conurbation is a continuous built-up area made of towns and cities that have joined.",
           hint="Think of the top of the settlement pyramid."),
        PQ("Define urbanisation and give its measure.", "**Urbanisation** is the increase in the proportion of a country's people who live in towns and cities. It is measured as a percentage: urban population divided by total population, times 100."),
        PQ("Describe two push factors and two pull factors that cause rural-urban migration.", "Push: shortage of farmland and low farm incomes; few schools, clinics and electricity in villages. Pull: jobs and higher wages in towns; better schools, hospitals and amenities."),
        PQ("In a region of 8 million people, 3.2 million live in towns. What percentage is urban?", "3.2 divided by 8 gives 0.4, and 0.4 times 100 is 40. The region is 40 percent urban."),
        PQ("Name five types of settlement in order of size, starting with the smallest, and state one function of a town.", "Hamlet, village, town, city and conurbation. A town may have a function such as a market centre, a port, an administrative centre or an industrial centre; for example, Douala is a port."),
        SUM("Urbanisation is the increase in the proportion of people living in towns and cities.",
            "Rural push factors are land shortage, low incomes and few services. Urban pull factors are jobs, services and a better life. Natural increase also adds to town growth.",
            "Settlement types by size are hamlet, village, town, city and conurbation. A town's function is its main work.",
            "Percentage urban = urban population divided by total population, times 100."),
    ],
))

# ------------------------------------------------------------------ 8. Urban problems and solutions
LESSONS.append(lesson(
    module=SET, topic=MORPH,
    title="Urban problems and possible solutions",
    slug="ts-urban-problems-and-solutions",
    minutes=22,
    summary="The main problems of fast-growing towns (housing shortage and slums, traffic, unemployment, waste and pollution, crime and pressure on services) and the solutions that governments, communities and planners can use.",
    objectives=[
        "Outline the main problems of urban areas",
        "Explain the causes of these problems",
        "Outline possible solutions to urban problems",
    ],
    key_concepts=["Informal settlement", "Traffic congestion", "Unemployment", "Informal sector", "Waste management", "Urban planning"],
    blocks=[
        H("Introduction"),
        T("Visit a big town at rush hour and you may see crowded streets, traders on every pavement, rubbish by the road, and houses "
          "packed on the edge of marsh or hillside. People come to town for opportunity. Yet when too many arrive too fast, the town cannot "
          "build houses, roads and services quickly enough."),
        IMG("f5g-ts-urban-cycle.svg", alt="Cycle: rapid growth causes shortage of houses and jobs, then slums and traffic jams, then overloaded water, waste and health services, then poverty, crime, pollution and disease",
            caption="Figure 1. How unplanned growth produces a cycle of problems."),
        H("The main problems"),
        KEY("Housing and slums", "The most visible problem.", cards=[
            ["Cause", "Migrants arrive faster than houses are built, and rents and land are costly for poor families."],
            ["Effect", "People build informal settlements (slums) with weak materials, often on marsh, steep slopes or along drains. They lack water, toilets and electricity, and risk floods, landslides, fire and disease."],
        ]),
        KEY("Traffic congestion", "Roads are too few and too narrow.", cards=[
            ["Cause", "Too many vehicles for old roads, little public transport and street trading on the road edge."],
            ["Effect", "Long journeys, lost working time, accidents and air pollution."],
        ]),
        KEY("Unemployment and underemployment", "Not enough jobs.", cards=[
            ["Cause", "More people arrive than formal jobs can be created. Many migrants have few skills."],
            ["Effect", "Many work in the informal sector, for example street trade or motorbike taxi, with low and uncertain pay. Poverty, begging and crime may follow."],
        ]),
        KEY("Waste and pollution", "Rubbish and dirty water.", cards=[
            ["Cause", "Too few bins, trucks and dumps, no sewers in slums, and many vehicles and small industries."],
            ["Effect", "Blocked drains cause floods and mosquito breeding, rivers and the air are polluted, and diseases such as cholera and typhoid spread."],
        ]),
        KEY("Crime and pressure on services", "The town is overloaded.", cards=[
            ["Crime", "Unemployment, poverty, poor street lighting and overcrowding raise theft and violence."],
            ["Pressure on services", "Schools, clinics, water and electricity supplies, and police are too few for the growing population, so classes and hospitals are crowded and power and water supplies are cut."],
        ]),
        H("Possible solutions"),
        CODE("""
Problem          Solutions
Housing          Build low-cost houses; site-and-service schemes (plots with
                 water and drains); upgrade slums instead of demolishing them
Traffic          Better public transport (buses, trains); ring roads and
                 bypasses; one-way streets; safe markets away from main roads
Unemployment     Industrial zones; training and loans for small businesses;
                 develop rural areas so fewer people leave
Waste            Regular collection, recycling and composting; drains and
                 sewers; fines for dumping; community clean-up days
Crime            Street lighting, community policing, jobs and youth
                 programmes
Services         Plan ahead: build schools, clinics, water and power in new
                 districts; develop new towns (satellite towns) to take
                 pressure off the big city
""", "text", title="Problems and solutions"),
        T("The best long-term answer is **urban planning**: deciding in advance where houses, roads, industry and services will go. Decentralisation, which means "
          "developing other towns and rural areas with jobs and services, reduces the pressure on the biggest city."),
        H("Model answers"),
        EX("Worked example 1: a problem, its cause and a solution", intro="Describe one problem of a fast-growing city. Explain its causes and suggest one solution.", steps=[
            S("The problem", text="A shortage of housing leads to informal settlements (slums) on marshy or steep land."),
            S("Causes", text="Migrants arrive faster than houses are built, and poor families cannot afford rents or land in planned areas, so they build with weak materials where land is cheap."),
            S("Effects", text="Slums lack water, toilets and drains, so floods, landslides and diseases such as cholera are common."),
            S("Solution", text="Build low-cost housing and site-and-service plots with water and drains, and upgrade existing slums."),
        ]),
        EX("Worked example 2: traffic", intro="Explain why traffic congestion is a problem in many African cities and suggest two ways to reduce it.", steps=[
            S("Why", text="Roads were built for a smaller town. Vehicles have increased, there are few buses, and traders and parked vehicles crowd the road, so traffic moves slowly."),
            S("Effects", text="Workers lose time, goods are delayed, accidents rise and exhaust fumes pollute the air."),
            S("Solutions", text="Provide more buses or trains so fewer people need cars and taxis. Build ring roads and bypasses and move markets away from main roads."),
        ]),
        TIP("Exam link: urban problems and solutions appear in Paper 1 and as a common Paper 2 Section C essay: 'outline the problems of urban areas and suggest solutions'. Use the pattern problem, cause, effect, solution. Keep a balanced and factual tone.", title="Exam link"),
        MISTAKE("Listing problems without solutions", "The syllabus objective says 'problems and possible solutions'. Give at least one solution for each problem you describe."),
        MISTAKE("Blaming the migrants", "Problems come from rapid growth that planning and investment did not keep up with. Explain the cause, not who is to blame."),
        qz("Which is a possible solution to a shortage of houses in a growing city?", "Site-and-service schemes with water and drains", [
            ("Stop all roads being built", "Stopping roads does not provide housing."),
            ("Close schools to save money", "That would worsen pressure on services and does not help housing."),
            ("Encourage everyone to move to the capital", "More migration would increase pressure on housing."),
        ], 0, "Providing plots and basic services (and low-cost homes) helps poor families build safe homes.",
           hint="Which choice actually adds safe housing?"),
        qz("Why do informal settlements often have more disease than planned districts?", "They lack clean water, toilets and drains", [
            ("The houses are too large", "Informal houses are usually small and crowded."),
            ("They are too near to hospitals", "Many slums are far from good clinics."),
            ("They have too much electricity", "Informal areas often lack electricity."),
        ], 0, "Without clean water, toilets and drains, diseases such as cholera spread quickly.",
           hint="Think about water and sanitation."),
        PQ("State four problems of urban areas in developing countries.", "Shortage of housing and slums; traffic congestion; unemployment and low pay; waste and pollution; crime; pressure on schools, hospitals, water and electricity."),
        PQ("Explain two causes of traffic congestion in a large town.", "Roads are too few and too narrow for the growing number of vehicles. There is little public transport, so many people use cars and taxis. Traders and parked vehicles also take up road space."),
        PQ("Outline two solutions to the problem of unemployment in towns.", "Create jobs by setting up industrial zones and supporting small businesses with training and loans. Develop rural areas and other towns so that fewer people migrate to the big city."),
        PQ("Describe how poor waste management harms a town.", "When rubbish is not collected it blocks drains and causes floods. It attracts mosquitoes and flies and spreads diseases such as cholera. Rivers and the air are polluted and the town looks and smells bad."),
        SUM("Fast, unplanned urban growth causes housing shortages, slums, traffic jams, unemployment, waste, crime and pressure on services.",
            "Slums lack water and sanitation, so disease spreads. Traffic wastes time and causes pollution.",
            "Solutions include low-cost housing, site-and-service schemes, public transport, job creation, waste collection and recycling.",
            "Planning ahead and developing rural areas and other towns reduce pressure on the big city."),
    ],
))

# ------------------------------------------------------------------ 9. Urban fields
LESSONS.append(lesson(
    module=SET, topic=MORPH,
    title="Urban fields and functional relationships between town and country",
    slug="ts-urban-fields-and-functional-relationships",
    minutes=20,
    summary="The urban field (sphere of influence) of a town, why bigger towns have larger fields, and the two-way functional relationships between a town and the villages around it, shown on a diagram.",
    objectives=[
        "Define urban field (sphere of influence) and range of a service",
        "Illustrate the urban field of a town with a diagram",
        "Describe the functional relationships between a town and its surrounding area",
        "Explain the factors that affect the size of an urban field",
    ],
    key_concepts=["Urban field", "Sphere of influence", "Hinterland", "Range", "Threshold", "Functional relationship"],
    blocks=[
        H("Introduction"),
        T("Every Saturday farmers from the villages around Bamenda carry plantains, maize and vegetables to the market. Others come to the "
          "hospital, the bank or the secondary school. Some travel to work. People travel from the countryside to the town because the town "
          "offers things the village does not. In return, the town depends on the farms for food."),
        D("The **urban field** (or **sphere of influence**) of a town is the area around it that depends on it for goods, services and jobs, and that supplies it with food, raw materials and labour.", title="Urban field"),
        D("The **range** of a service is the greatest distance people will travel to use it. The **threshold** is the minimum number of customers a service needs to stay in business.", title="Range and threshold"),
        H("The urban field diagram"),
        IMG("f5g-ts-urban-field.svg", alt="Fictitious map of Town T with dashed circles at 5, 12 and 19 km and six villages A to F; F is outside the largest circle",
            caption="Figure 1. The urban field of Town T (fictitious). Scale: 10 km equals the length of the scale bar. Rings show the range of three services."),
        T("In Figure 1 the inner ring (5 km) shows the range of everyday services such as a daily shop and a primary school. The middle ring "
          "(12 km) shows the range of a weekly market and a secondary school. The outer ring (19 km) shows the range of rarer, higher-order services "
          "such as a hospital, bank or college."),
        T("The more specialised the service, the larger its range and the greater the number of customers needed. Because only large towns have "
          "enough customers, specialised services are found in a few big places and many people must travel far to reach them."),
        T("Village A (3 km) is inside all three rings. Villages B (8 km) and C (10 km) lie between the 5 km and 12 km rings. Villages D (15 km) and E (17 km) lie between the 12 km and 19 km rings. Village F (22 km) is "
          "outside the outer ring, so it is not in the field of Town T and must depend on another town for higher-order services."),
        H("Functional relationships"),
        KEY("A two-way link", "Town and country depend on each other.", cards=[
            ["Town to country", "Shops and markets, manufactured goods, schools and colleges, hospitals and clinics, banks, government offices, jobs, transport, news and entertainment."],
            ["Country to town", "Food and raw materials, such as vegetables and cocoa. Labour for factories and shops, daily commuters, and customers for urban shops and services."],
        ]),
        H("What decides the size of an urban field?"),
        KEY("Factors", "Learn four.", cards=[
            ["Size and functions of the town", "A large city with many services has a larger field than a small market town."],
            ["Transport", "Good roads and cheap fares increase the area people can reach. Rain-damaged roads reduce it."],
            ["Competition", "If another town is close, the two fields meet and the boundary lies between them, nearer to the smaller town."],
            ["Population density and relief", "Densely populated areas give more customers. Mountains, rivers and forests make travel harder, so fields are smaller."],
        ]),
        T("Douala is an example of a very large field. Its port serves not only Cameroon but also landlocked neighbours such as Chad and the Central African Republic."),
        H("Model answers"),
        EX("Worked example 1: reading the diagram", intro="Use Figure 1. State which village is outside the urban field of Town T and give its distance. Name two villages inside the 12 km ring.", steps=[
            S("Find the outer ring", text="The largest ring has a radius of 19 km. Any village farther than 19 km from Town T is outside the field."),
            S("Compare each village", text="Village F is 22 km from Town T, which is more than 19 km, so it lies outside the field."),
            S("Inside the 12 km ring", text="Villages A (3 km), B (8 km) and C (10 km) are all within 12 km of Town T, so they are inside the 12 km ring. Any two of them answer the question."),
        ]),
        EX("Worked example 2: functional relationships", intro="Describe the functional relationships between a town and the villages around it.", steps=[
            S("From town to village", text="The town provides a market for farm produce, shops selling manufactured goods, schools, hospitals, banks and jobs."),
            S("From village to town", text="Villages supply food and raw materials, workers for factories and shops, and customers for town businesses."),
            S("Conclusion", text="Both depend on each other, linked by roads and communications. Better roads strengthen these links."),
        ]),
        EX("Worked example 3: factors affecting size", intro="Explain why a large city has a bigger urban field than a small market town.", steps=[
            S("More services", text="A city has more and rarer services (university, specialist hospital, airport), which draw people from farther away."),
            S("More customers and transport", text="It has more people and better transport links, so higher-order services can find enough customers and people can reach them."),
        ]),
        TIP("Exam link: urban fields are tested in Paper 1 (reading a diagram like Figure 1) and in Paper 2 Section C ('illustrate and describe functional relationships'). Always draw a labelled diagram with a town in the centre, rings, villages and arrows both ways.", title="Exam link"),
        MISTAKE("Showing arrows in one direction only", "Functional relationships are two-way: services and goods go from town to country; food, labour and customers go from country to town."),
        MISTAKE("Drawing the field as an exact circle in the answer", "Real fields are uneven because of roads, relief and competing towns. Say that circles are a simplification."),
        qz("What is the sphere of influence (urban field) of a town?", "The area around it that depends on it for goods, services and jobs", [
            ("The area inside the town's boundary only", "The field includes the surrounding villages that depend on the town."),
            ("The area where the town gets its rainfall", "Rainfall is a climate matter, not a settlement relationship."),
            ("A list of all roads in the town", "A list of roads does not describe the area served by the town."),
        ], 0, "It is the area linked to the town by trade, services, jobs and flows of food and labour.",
           hint="Think of who uses the town's market, school and hospital."),
        qz("Which flow goes from the countryside to the town?", "Food and labour", [
            ("Manufactured goods", "These flow from the town to the countryside."),
            ("Hospital services", "Services flow from town to country, and the people travel to use them."),
            ("Bank loans", "Bank services are provided by the town to its field."),
        ], 0, "Villages supply food, raw materials, workers and customers to the town.",
           hint="What does a town not produce for itself?"),
        PQ("Define urban field (sphere of influence).", "The urban field of a town is the area around it that depends on it for goods, services and jobs, and which supplies the town with food, raw materials and labour."),
        PQ("Describe two flows from a town to its surrounding villages and two from the villages to the town.", "Town to villages: manufactured goods from shops and services such as schools and hospitals. Villages to town: food (for example vegetables and fruit) and labour or daily commuters."),
        PQ("Explain two factors that affect the size of a town's urban field.", "The size and functions of the town: a large city with many specialised services draws people from farther away. Transport: good roads and cheap fares extend the field, while poor roads or mountains and rivers shrink it. Competition from nearby towns can also limit it."),
        PQ("Draw and label a diagram of the urban field of a town.", "Draw a square for the town at the centre. Draw three dashed circles round it, labelled with services of low, medium and high order (daily shop, weekly market, hospital). Add small circles for villages inside and outside the rings, and arrows both ways between the villages and the town marked 'food, labour' and 'goods, services'. Add a scale bar and title."),
        SUM("An urban field (sphere of influence) is the area that depends on a town for goods, services and jobs and supplies it with food and labour.",
            "Range is how far people will travel for a service. Threshold is the number of customers needed. Rarer services have larger ranges.",
            "Functional relationships are two-way: goods and services go out; food, labour and customers come in.",
            "The size of a field depends on the size and functions of the town, transport, competition and relief."),
    ],
))
