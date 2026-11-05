"""Practice sets for Form 5 Geography: The Geography of Cameroon (Background and Physical characteristics)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
BACK = "Background of Cameroon"
PHYS = "Physical characteristics"

SETS = []

# ------------------------------------------------------------------ 1. Location and administrative map
ADMIN_ALT = ("Sketch map of Cameroon with seven regional headquarters marked by dots and the letters A to G: A in the far north, B in the middle, "
             "C in the west, D on the coast, E in the south-centre, F in the east and G in the south")
SETS.append(practice_set(
    module=MODULE, topic=BACK,
    title="Location of Cameroon and regional headquarters",
    lesson="cmr-location-and-administrative-map",
    questions=[
        MC("Which of these gives the approximate latitude and longitude of Cameroon?", [
            C("About 2°S to 13°S and 8.5°W to 16°W", why="Cameroon is north of the Equator and east of Greenwich, so the letters would be N and E."),
            C("About 2°N to 13°N and 8.5°E to 16°E", correct=True),
            C("About 12°N to 23°N and 8.5°E to 16°E", why="This latitude is much too far north. It is the latitude of the Sahara, not of Cameroon."),
            C("About 2°N to 13°N and 18°E to 28°E", why="These longitudes are too far east. They lie in the Central African Republic and beyond."),
        ], steps=[S("Recall", text="Cameroon is north of the Equator (about 2°N to 13°N) and east of Greenwich (about 8.5°E to 16°E).")],
           concept="Latitude and longitude of Cameroon", skill="Recall",
           hint="Decide first whether Cameroon is north or south of the Equator, and east or west of Greenwich."),
        MC("Which of these countries does NOT share a border with Cameroon?", [
            C("Chad", why="Chad lies to the north-east of Cameroon and shares a border with it."),
            C("Gabon", why="Gabon lies to the south of Cameroon and shares a border with it."),
            C("Ghana", correct=True),
            C("Congo", why="Congo lies to the south-east of Cameroon and shares a border with it."),
        ], steps=[S("Recall the neighbours", text="Cameroon borders Nigeria, Chad, the Central African Republic, Congo, Gabon and Equatorial Guinea. Ghana is further west, beyond Nigeria.")],
           concept="Neighbours of Cameroon", skill="Recall",
           hint="Ghana is on the Gulf of Guinea coast, but is it next to Cameroon?"),
        MC("On the map, which letter marks the regional headquarters of the Far North Region?", [
            C("A", correct=True),
            C("B", why="B is in the middle of the country. It marks the headquarters of Adamawa."),
            C("C", why="C is in the west. It marks the headquarters of North-West."),
            C("F", why="F is in the east. It marks the headquarters of the East Region."),
        ], steps=[S("Find the far north", text="The Far North is the thin tip of the country near Lake Chad. The dot nearest the north tip is A, which is Maroua.")],
           concept="Regional headquarters on a map", skill="Interpretation",
           hint="Look at the thin tip of the country pointing towards Lake Chad.",
           diagram="f5g-cmr-admin-quiz.svg", diagram_alt=ADMIN_ALT),
        MC("On the same map, letter C marks a regional headquarters in the west of Cameroon, in the highlands. Which town is it?", [
            C("Buea", why="Buea is on the coast, at the foot of Mount Cameroon. The coastal dot on the map is D."),
            C("Bafoussam", why="Bafoussam is in the West Region, a little south-east of Bamenda. It is not marked on this map."),
            C("Bertoua", why="Bertoua is in the east. On this map the east is marked F."),
            C("Bamenda", correct=True),
        ], steps=[S("Locate it", text="C is in the north-west highlands, above the coast. The headquarters of the North-West Region is Bamenda.")],
           concept="Bamenda, North-West", skill="Interpretation",
           hint="C is inland in the west, well north of the coast.",
           diagram="f5g-cmr-admin-quiz.svg", diagram_alt=ADMIN_ALT),
        MC("On the same map, letter D marks the largest city and main port of Cameroon, on the coast. Of which region is it the headquarters?", [
            C("South-West", why="South-West's headquarters is Buea, a smaller town on the slopes of Mount Cameroon."),
            C("Littoral", correct=True),
            C("West", why="The West Region is inland. Its headquarters is Bafoussam."),
            C("Centre", why="The Centre Region is inland. Its headquarters is Yaoundé, the political capital."),
        ], steps=[S("Identify the town", text="The largest city and main port is Douala."),
                  S("Match the region", text="Douala is the headquarters of the Littoral Region.")],
           concept="Douala, Littoral", skill="Interpretation",
           hint="Think of the city with Cameroon's main sea port.",
           diagram="f5g-cmr-admin-quiz.svg", diagram_alt=ADMIN_ALT),
        NUM("Take 1° of latitude as 111 km. Cameroon extends from about 2°N to 13°N. Calculate its length from north to south in km.", 1221, tolerance=25, unit="km",
            steps=[S("Difference in latitude", math=r"13° - 2° = 11°"),
                   S("Convert to kilometres", math=r"11 \times 111 = 1\,221 \text{ km}")],
            concept="Distance from latitude", skill="Calculation",
            hint="First subtract the two latitudes to find how many degrees apart they are."),
        MC("The figure shows Cameroon in Africa. Which statement about its position is correct?", [
            C("It is south of the Equator and west of Greenwich.", why="The figure shows Cameroon above the Equator line and to the right of the Greenwich line."),
            C("It is on the Equator and on the Greenwich Meridian.", why="Neither line passes through Cameroon. The Equator is south of it and Greenwich is west of it."),
            C("It is north of the Equator and east of Greenwich.", correct=True),
            C("It is north of the Equator and west of Greenwich.", why="Cameroon is to the right (east) of the Greenwich line on the figure."),
        ], steps=[S("Read the figure", text="Cameroon is above the dashed Equator line (north) and to the right of the dashed Greenwich line (east).")],
           concept="Hemisphere position of Cameroon", skill="Interpretation",
           hint="Find the two dashed lines, then see on which side of each line the green shape lies.",
           diagram="f5g-cmr-africa-location.svg", diagram_alt="Sketch map of Africa with Cameroon in dark green, a dashed Equator line and a dashed Greenwich Meridian line"),
        MC("Which is the best way to begin an exam answer on the location of Cameroon?", [
            C("Cameroon is a rich country with many tribes and two official languages.", why="This is not about location. Location needs latitude, longitude and neighbours."),
            C("Cameroon is a hot country near the sea.", why="This is too vague. It gives no figures and no neighbours."),
            C("Cameroon is in Africa, next to Nigeria.", why="This is correct but too short. A full answer also gives latitude and longitude."),
            C("Cameroon lies in West-Central Africa between about 2°N and 13°N and 8.5°E and 16°E, on the Gulf of Guinea.", correct=True),
        ], steps=[S("Check the command word", text="'Locate' or 'describe the location' needs latitude, longitude and areal (neighbouring) location."),
                  S("Choose", text="Only the last statement gives latitude, longitude, the part of Africa and the sea.")],
           concept="Describing location", skill="Application",
           hint="Which statement contains numbers for latitude and longitude as well as a place in Africa?"),
    ]))

# ------------------------------------------------------------------ 2. Relief units
RELIEF_ALT = ("Sketch map of Cameroon with relief regions shaded and lettered A to G: A on the north-west border in the far north, B in the west, "
              "C in the centre, D along the south-west coast, E in the far north, F in the south and east, G in the north below E")
SETS.append(practice_set(
    module=MODULE, topic=PHYS,
    title="Relief units and Mount Cameroon",
    lesson="cmr-relief-units",
    questions=[
        MC("Which is the highest mountain in Cameroon?", [
            C("Mount Oku", why="Mount Oku is high (about 3,000 m) and is in the western highlands, but it is lower than Mount Cameroon."),
            C("Mount Cameroon", correct=True),
            C("Mount Manengouba", why="Mount Manengouba is a volcano in the western highlands, but it is much lower than Mount Cameroon."),
            C("Mount Mandara", why="The Mandara are a range of rocky hills in the north, much lower than Mount Cameroon."),
        ], steps=[S("Recall", text="Mount Cameroon, an active volcano on the coast, is more than 4,000 m high. It is the highest peak in Cameroon.")],
           concept="Highest mountain", skill="Recall",
           hint="It stands next to the Atlantic coast near Buea and Limbe."),
        MC("On the map, which letter marks the Adamawa plateau?", [
            C("A", why="A is the Mandara mountains, on the north-western border of the Far North."),
            C("B", why="B is the western highlands, in the west of the country."),
            C("C", correct=True),
            C("F", why="F is the southern plateau, in the south and east."),
        ], steps=[S("Locate", text="The Adamawa plateau lies across the centre of the country, at about 6°N to 8°N. Letter C is in the centre.")],
           concept="Adamawa plateau on a map", skill="Interpretation",
           hint="The Adamawa plateau lies across the middle of the country.",
           diagram="f5g-cmr-relief-quiz.svg", diagram_alt=RELIEF_ALT),
        MC("On the same map, which relief unit is marked by letter D, a low strip along the Atlantic coast?", [
            C("Chad lowlands", why="The Chad lowlands are in the far north, not on the coast."),
            C("Benue lowlands", why="The Benue lowlands lie in the north, along the Benue River."),
            C("Western highlands", why="The western highlands are high land inland, not a low coastal strip."),
            C("Coastal plain", correct=True),
        ], steps=[S("Read the map", text="D is a low strip along the south-west coast. This is the coastal plain.")],
           concept="Coastal plain on a map", skill="Interpretation",
           hint="Which unit is low and lies beside the sea?",
           diagram="f5g-cmr-relief-quiz.svg", diagram_alt=RELIEF_ALT),
        MC("Which list shows the relief units in order as you travel from the south-west coast northwards to the far north (through the centre)?", [
            C("Chad lowlands, Benue lowlands, Adamawa plateau, southern plateau, coastal plain", why="This is the order from north to south, the reverse of the question."),
            C("Coastal plain, Adamawa plateau, southern plateau, Benue lowlands, Chad lowlands", why="The southern plateau comes before the Adamawa plateau as you go north."),
            C("Coastal plain, southern plateau, Adamawa plateau, Benue lowlands, Chad lowlands", correct=True),
            C("Southern plateau, coastal plain, Adamawa plateau, Chad lowlands, Benue lowlands", why="The coastal plain is at the sea, so it comes first, and the Benue lowlands come before the Chad lowlands."),
        ], steps=[S("Follow the route", text="From the coast the land rises to the southern plateau, then to the Adamawa plateau, and falls to the Benue lowlands and then the Chad lowlands.")],
           concept="Order of relief units", skill="Reasoning",
           hint="Begin at the coast and go inland, then north."),
        MC("On the map, letter A marks hills on the north-western border near Mokolo, where steep slopes are terraced for farming. What are they?", [
            C("Mandara mountains", correct=True),
            C("Southern plateau", why="The southern plateau is in the south and east, not in the Far North."),
            C("Adamawa plateau", why="The Adamawa plateau is in the centre, not on the border in the Far North."),
            C("Coastal plain", why="The coastal plain is low land on the coast."),
        ], steps=[S("Match the clues", text="Rocky hills, the Far North and terraces describe the Mandara mountains, near Mokolo and Mora.")],
           concept="Mandara mountains", skill="Interpretation",
           hint="Which unit of the Far North is made of rocky hills?",
           diagram="f5g-cmr-relief-quiz.svg", diagram_alt=RELIEF_ALT),
        MC("Which statement describes the Chad lowlands best?", [
            C("High rocky mountains with terraced slopes", why="This describes the Mandara mountains, not the lowlands."),
            C("A high plateau with grassland and cool weather", why="This describes the Adamawa plateau."),
            C("A flat, low-lying plain in the far north, part of which floods in the rainy season", correct=True),
            C("A narrow strip of mangroves along the Atlantic coast", why="This describes the coastal plain."),
        ], steps=[S("Match", text="The Chad lowlands are flat, low and hot, near the Logone River and Lake Chad, and parts flood each rainy season.")],
           concept="Chad lowlands", skill="Concept",
           hint="'Lowlands' tells you the height. The unit is in the far north."),
        MC("Which statement about Mount Cameroon is correct?", [
            C("It is an extinct volcano with no recent eruption.", why="Mount Cameroon is active and has erupted several times in recent decades."),
            C("It is an active volcano on the coast whose lava has made fertile soils.", correct=True),
            C("It is a plateau in the Adamawa Region.", why="A plateau is flat; Mount Cameroon is a volcanic cone, and it is not in Adamawa."),
            C("It is a hill in the Mandara mountains.", why="It is much higher than the Mandara and is on the coast."),
        ], steps=[S("Recall", text="Mount Cameroon is an active volcano near the coast in the South-West. Its lava and ash make fertile volcanic soils.")],
           concept="Mount Cameroon", skill="Recall",
           hint="Think about the soils and plantations around Buea and Limbe."),
        MC("Why is the population density in the western highlands higher than in the Benue lowlands?", [
            C("The highlands are flatter than the lowlands.", why="The highlands are steep, not flatter. Flatness is not the reason."),
            C("The lowlands have no rivers.", why="The Benue lowlands have the Benue River and its tributaries."),
            C("The lowlands are nearer the Equator.", why="The lowlands are further from the Equator than the highlands."),
            C("The highlands have fertile volcanic soils and a cooler, wetter climate that support farming.", correct=True),
        ], steps=[S("Reason", text="Volcanic soils are rich, and height gives a cooler, wetter climate. Both help farming and support more people.")],
           concept="Relief and population", skill="Reasoning",
           hint="Think about soil and temperature in the highlands compared with the hot, dry north."),
    ]))

# ------------------------------------------------------------------ 3. Drainage systems and watersheds
DRAIN_ALT = ("Sketch map of Cameroon with blue rivers lettered A to F: A a long river in the south-centre flowing west, B a river in the north flowing north then west, "
             "C a river along the north-east border, D a short river near Douala, E a river in the south, F a river in the west near the Nigerian border")
SETS.append(practice_set(
    module=MODULE, topic=PHYS,
    title="Rivers, drainage systems and watersheds",
    lesson="cmr-drainage-systems-and-watersheds",
    questions=[
        MC("What is a watershed?", [
            C("A river that joins a larger river", why="This is a tributary, not a watershed."),
            C("The whole area drained by a river and its tributaries", why="This is the drainage basin, not the watershed."),
            C("The place where a river meets the sea", why="This is the river mouth."),
            C("A line of high ground separating two drainage basins", correct=True),
        ], steps=[S("Recall", text="A watershed is the high ground that divides one drainage basin from the next.")],
           concept="Definition of watershed", skill="Recall",
           hint="It separates the areas drained by two different river systems."),
        MC("On the map, river A is the longest river wholly inside Cameroon and has hydroelectric dams at Edéa. Which river is it?", [
            C("Benue", why="The Benue is in the north. It is lettered B on the map."),
            C("Sanaga", correct=True),
            C("Logone", why="The Logone is on the north-east border. It is lettered C on the map."),
            C("Cross River", why="The Cross River is in the west, lettered F, and has no dams at Edéa."),
        ], steps=[S("Identify", text="The Sanaga flows west across the south-centre to the Atlantic. Dams at Edéa and Song Loulou produce electricity.")],
           concept="Sanaga River", skill="Interpretation",
           hint="Which river flows west across the middle of southern Cameroon and has dams near Edéa?",
           diagram="f5g-cmr-drainage-quiz.svg", diagram_alt=DRAIN_ALT),
        MC("On the same map, river B rises on the Adamawa plateau near Ngaoundéré, flows north past Garoua and then leaves for Nigeria. Which river is it?", [
            C("Benue", correct=True),
            C("Nyong", why="The Nyong is in the south and flows to the Atlantic."),
            C("Wouri", why="The Wouri is a short river near Douala."),
            C("Mungo", why="The Mungo is a short river near Mount Manengouba and the coast."),
        ], steps=[S("Match the clues", text="Rising near Ngaoundéré, passing Garoua and leaving for Nigeria are the course of the Benue.")],
           concept="Benue River", skill="Interpretation",
           hint="Think of the river on which the Lagdo Dam is built.",
           diagram="f5g-cmr-drainage-quiz.svg", diagram_alt=DRAIN_ALT),
        MC("River C forms part of the border with Chad in the Far North. Where does its water end?", [
            C("In the Atlantic Ocean", why="This is where the Sanaga, Wouri and Nyong end, not the northern rivers."),
            C("In the Congo River", why="Only the rivers of the south-east flow to the Congo."),
            C("In Lake Chad", correct=True),
            C("In the Niger River", why="The Niger is reached by the Benue, not by the Logone."),
        ], steps=[S("Follow the river", text="The Logone flows north along the border, joins the Chari and ends in Lake Chad, which has no outlet to the sea.")],
           concept="Logone and Lake Chad", skill="Interpretation",
           hint="Lake Chad is in the corner at the north tip.",
           diagram="f5g-cmr-drainage-quiz.svg", diagram_alt=DRAIN_ALT),
        MC("Which river flows into the Atlantic Ocean through an estuary at Douala?", [
            C("Logone", why="The Logone is in the far north and flows to Lake Chad."),
            C("Wouri", correct=True),
            C("Benue", why="The Benue flows north and west into Nigeria."),
            C("Dja", why="The Dja flows south-east towards the Congo basin."),
        ], steps=[S("Recall", text="Douala's port is on the Wouri estuary.")],
           concept="Wouri estuary", skill="Recall",
           hint="The estuary has the same name as the river."),
        MC("The Lagdo Dam is on which river?", [
            C("Sanaga", why="The Sanaga has dams at Edéa and Song Loulou, not Lagdo."),
            C("Logone", why="The Logone has no dam called Lagdo. Lagdo is near Garoua on another river."),
            C("Benue", correct=True),
            C("Nyong", why="The Nyong is in the south, far from Garoua."),
        ], steps=[S("Recall", text="The Lagdo Dam is on the Benue near Garoua. It produces electricity and stores water for irrigation.")],
           concept="Lagdo Dam", skill="Recall",
           hint="Lagdo is near Garoua, in the north."),
        MC("Why do the Adamawa plateau and its watershed matter for the whole country?", [
            C("It is the coldest place in the country.", why="It is cool, but this is not why it matters as a watershed."),
            C("It is next to the sea, so ships can reach it.", why="The plateau is in the centre, far from the sea."),
            C("It is the lowest land in the country, so all rivers meet there.", why="The plateau is high. Rivers flow away from high ground, not to it."),
            C("Rivers rising there flow north and south to different basins and serve many regions.", correct=True),
        ], steps=[S("Reason", text="A watershed sends water to different basins. Rivers from the Adamawa plateau serve the south (Atlantic and Congo) and the north (Benue and Lake Chad).")],
           concept="Adamawa watershed", skill="Reasoning",
           hint="Rivers flow downhill, away from high ground."),
        MC("Why do many rivers in the Far North flow only in the rainy season?", [
            C("The Far North is a high plateau so rivers cannot flow there.", why="The Far North is mostly low plains and hills, and height is not the reason."),
            C("There is a short rainy season, a long dry season and high evaporation.", correct=True),
            C("The rivers are blocked by Mount Cameroon.", why="Mount Cameroon is on the south-west coast, far from the Far North."),
            C("All northern rivers have been dammed.", why="Dams exist, but most northern rivers are seasonal because of the climate."),
        ], steps=[S("Reason", text="Rain falls for only a few months. During the long dry season there is little rain and much evaporation, so seasonal rivers (mayos) dry up.")],
           concept="Seasonal rivers", skill="Reasoning",
           hint="Think about how long the dry season lasts in the north."),
    ]))

# ------------------------------------------------------------------ 4. Climate zones and vegetation
SETS.append(practice_set(
    module=MODULE, topic=PHYS,
    title="Climatic types, climate graphs and vegetation",
    lesson="cmr-climate-zones-and-vegetation",
    questions=[
        MC("Square B on the map is in the far north of Cameroon. Which climatic type is found there?", [
            C("Equatorial (Guinean)", why="The equatorial climate is in the south and east, near the Equator."),
            C("Cameroonian type", why="The Cameroonian type is on the coast and in the western highlands."),
            C("Sudanian", why="The Sudanian climate covers the Adamawa plateau and the North Region, south of the Far North."),
            C("Sahelian", correct=True),
        ], steps=[S("Read the map", text="Square B is in the thin northern tip. This is the Far North, which has the Sahelian climate.")],
           concept="Sahelian climate location", skill="Interpretation",
           hint="Find the Far North on the map and read the zone it lies in.",
           diagram="f5g-cmr-climate-zones.svg", diagram_alt="Sketch map of Cameroon with four shaded climate zones and two squares marked A and B, A in the south and B in the far north"),
        MC("The graph shows constructed exercise data for station A: two rainfall peaks (May and October), more than 1,800 mm of rain a year and a temperature range of 2 °C. Which climatic type does it most resemble?", [
            C("Sahelian", why="The Sahelian climate has one short rainy season, less than about 900 mm and a large range."),
            C("Equatorial (Guinean)", correct=True),
            C("Sudanian", why="The Sudanian climate has one rainy season and a large temperature range."),
            C("Cameroonian type", why="The Cameroonian type has one long rainy season, not two peaks."),
        ], steps=[S("Match the clues", text="Two rainy seasons, high rainfall and a very small temperature range describe the equatorial (Guinean) climate.")],
           concept="Identify climate from a graph", skill="Interpretation",
           hint="Count the rainy seasons first, then look at the range of the line.",
           diagram="f5g-cmr-climate-graph-a.svg", diagram_alt="Climate graph for exercise station A with rainfall bars peaking in May and October and a nearly flat temperature line"),
        NUM("The monthly rainfall for station A (exercise data) from January to December is 50, 90, 190, 200, 220, 160, 70, 90, 250, 300, 150 and 40 mm. Calculate the annual rainfall total in mm.", 1810, tolerance=0, unit="mm",
            steps=[S("Add all 12 months", math=r"50 + 90 + 190 + 200 + 220 + 160 + 70 + 90 + 250 + 300 + 150 + 40 = 1\,810")],
            concept="Annual rainfall total", skill="Calculation",
            hint="Add all twelve monthly values."),
        MC("Why is rainfall so heavy on the Cameroon coast and in the highlands (Cameroonian-type climate)?", [
            C("The harmattan wind brings rain from the Sahara.", why="The harmattan is a dry wind. It brings dust, not rain."),
            C("The area is nearer to the North Pole.", why="Cameroon is in the tropics. Distance from the pole is not the cause."),
            C("Moist monsoon winds from the Atlantic are forced to rise over Mount Cameroon and the highlands.", correct=True),
            C("There are no mountains to stop the clouds.", why="Mountains are the cause: they force the air to rise and form rain."),
        ], steps=[S("Explain", text="South-west monsoon winds carry moisture from the sea. When they rise over the mountains the air cools, clouds form and relief rainfall falls.")],
           concept="Cause of heavy rain on the coast", skill="Concept",
           hint="Think about what happens to moist air when it meets high land."),
        NUM("Station B (exercise data) has a hottest month of 34 °C and a coolest month of 24 °C. Calculate its annual temperature range in °C.", 10, tolerance=0, unit="°C",
            steps=[S("Subtract", math=r"34 - 24 = 10")],
            concept="Temperature range", skill="Calculation",
            hint="Range is the highest value minus the lowest value.",
            diagram="f5g-cmr-climate-graph-b.svg", diagram_alt="Climate graph for exercise station B with rainfall bars peaking in August and a temperature line from 24 to 34 degrees"),
        MC("Which statement about station B is correct?", [
            C("It has one short rainy season and a large temperature range, so it resembles the Sahelian climate.", correct=True),
            C("It has two long rainy seasons, so it resembles the equatorial climate.", why="The graph has one peak, in August, not two."),
            C("It has no dry season, so it resembles the Cameroonian-type climate.", why="Station B has about six months with almost no rain."),
            C("Its rainfall is highest in January.", why="Rainfall is almost nothing in January. The highest is in August."),
        ], steps=[S("Read the graph", text="Only June to September have more than 100 mm. The total is 725 mm and the range is 10 °C. These are Sahelian features.")],
           concept="Describe a Sahelian climate graph", skill="Interpretation",
           hint="Count how many months have clear rainfall bars.",
           diagram="f5g-cmr-climate-graph-b.svg", diagram_alt="Climate graph for exercise station B with rainfall bars peaking in August and a temperature line from 24 to 34 degrees"),
        MC("Which vegetation has stilt roots and grows in the salty mud of the coast and estuaries?", [
            C("Equatorial rainforest", why="Rainforest grows on dry land inland, not in salty mud."),
            C("Sahel steppe", why="Sahel steppe is in the far north, far from the coast."),
            C("Mangrove", correct=True),
            C("Guinea savanna", why="Guinea savanna is tall grass on the Adamawa plateau, far from the coast."),
        ], steps=[S("Recall", text="Mangroves grow in salty coastal mud, for example near Douala, and have stilt roots.")],
           concept="Mangrove vegetation", skill="Recall",
           hint="Think of the Wouri estuary."),
        MC("Which vegetation type is correctly matched with its description?", [
            C("Sahel steppe: tall evergreen trees in layers", why="This describes the rainforest. The Sahel has short grass and thorn bushes."),
            C("Equatorial rainforest: tall evergreen trees in layers with little undergrowth", correct=True),
            C("Mangrove: tall grass and scattered fire-resistant trees", why="This describes Guinea savanna, not mangrove."),
            C("Guinea savanna: thorny bushes and short tufted grass", why="This describes the Sahel steppe. Guinea savanna has tall grass."),
        ], steps=[S("Match each type", text="Rainforest has tall evergreen trees in layers. Sahel steppe has thorny bushes and short grass. Guinea savanna has tall grass with scattered trees. Mangrove has stilt roots in salty mud.")],
           concept="Vegetation characteristics", skill="Concept",
           hint="Match the plant description to the amount of rain each zone gets."),
    ]))

# ------------------------------------------------------------------ 5. Soil types
SOIL_ALT = ("Sketch map of Cameroon with soil zones labelled: ferralitic in the south and east, volcanic in the western highlands, tropical ferruginous across the centre and north, "
            "Sahelian in the far north and alluvial patches on river plains and the coast")
SETS.append(practice_set(
    module=MODULE, topic=PHYS,
    title="Soil types of Cameroon and farming",
    lesson="cmr-soil-types-and-characteristics",
    questions=[
        MC("Which soil type is deep, red or yellow and found under the rainforest of southern Cameroon?", [
            C("Volcanic", why="Volcanic soils are dark and found near Mount Cameroon and in the western highlands."),
            C("Ferralitic", correct=True),
            C("Alluvial", why="Alluvial soils are deposited by rivers on flood plains."),
            C("Tropical ferruginous", why="Tropical ferruginous soils are found under savanna in the north and Adamawa."),
        ], steps=[S("Recall", text="Ferralitic soils are red or yellow and cover the south and east under the forest.")],
           concept="Ferralitic soils", skill="Recall",
           hint="Think of heavy rain and forest in the south."),
        MC("On the map, which soil type is shown covering the south and east of Cameroon?", [
            C("Volcanic soils", why="Volcanic soils are only in the western highlands and around Mount Cameroon on the map."),
            C("Alluvial soils", why="Alluvial soils are shown only in small patches on river plains and estuaries."),
            C("Sahelian soils", why="Sahelian soils are in the far north on the map."),
            C("Ferralitic soils", correct=True),
        ], steps=[S("Read the map", text="The largest zone in the south and east is ferralitic soils.")],
           concept="Soil map reading", skill="Interpretation",
           hint="Find the large area in the south and east, then read its label.",
           diagram="f5g-cmr-soils.svg", diagram_alt=SOIL_ALT),
        MC("Why are volcanic soils fertile?", [
            C("They are formed from lava and ash that are rich in minerals.", correct=True),
            C("They are always flooded by rivers.", why="Flooding makes alluvial soils fertile, not volcanic soils."),
            C("They are covered by thick rainforest.", why="Forest cover does not make soil fertile, and many volcanic areas have farmland."),
            C("They are the same as ferralitic soils.", why="Ferralitic soils are red and leached, while volcanic soils are dark and rich."),
        ], steps=[S("Explain", text="Lava and ash break down to release minerals. This makes the soil rich and fertile.")],
           concept="Fertility of volcanic soils", skill="Concept",
           hint="Think about what lava and ash are made of."),
        MC("Which crop-and-soil match is most suitable?", [
            C("Cotton in the Sahel desert sand", why="Cotton grows in the north's savanna soils, not in poor desert sand."),
            C("Tea and banana on volcanic soils near Mount Cameroon", correct=True),
            C("Rice on dry hilltops in the Mandara", why="Rice needs water. Alluvial plains or irrigated land suit it better than hilltops."),
            C("Cocoa on bare hard crusts in the north", why="Cocoa needs forest soils in the south, not bare crusts."),
        ], steps=[S("Match", text="Tea and banana plantations thrive on the fertile volcanic soils near Mount Cameroon.")],
           concept="Crops and soils", skill="Application",
           hint="Think about the plantations on the slopes of Mount Cameroon."),
        MC("Why are alluvial soils fertile?", [
            C("They are washed free of nutrients by heavy rain.", why="This describes leaching, which makes soils poor."),
            C("They are formed from lava and ash.", why="This describes volcanic soils."),
            C("They are renewed each year when rivers deposit fresh silt.", correct=True),
            C("They are very sandy and dry.", why="Sandy dry soils are poor. Alluvial soils are fine, silty and moist."),
        ], steps=[S("Explain", text="When rivers flood they deposit silt that contains minerals and humus. This renews the soil.")],
           concept="Fertility of alluvial soils", skill="Concept",
           hint="What do rivers leave behind after a flood?"),
        MC("Why does the fertility of ferralitic soils fall quickly after the forest is cleared?", [
            C("Rain stops falling in the south.", why="Rain continues. The problem is that rain washes the nutrients out."),
            C("Most nutrients are held in the trees and a thin humus layer, and rain washes the rest out.", correct=True),
            C("Volcanic ash covers the soil.", why="Ash falls only near volcanoes such as Mount Cameroon, not on the southern plateau."),
            C("The soil is made of silt from rivers.", why="Silt is alluvial soil. Ferralitic soils are deep, leached soils."),
        ], steps=[S("Reason", text="The nutrient store is the forest, not the soil. After clearing, crops use the nutrients and rain washes them down.")],
           concept="Fertility after clearing", skill="Reasoning",
           hint="Where are the nutrients kept in a rainforest?"),
        MC("Which method best helps farmers keep ferralitic soils productive?", [
            C("Burning the same plot and planting the same crop every year", why="This uses up nutrients and humus and lowers yields."),
            C("Clearing all trees from steep slopes", why="This increases erosion and loses topsoil."),
            C("Leaving plots to rest (bush fallow) and adding manure and compost", correct=True),
            C("Removing the humus layer", why="Humus holds nutrients and water. Removing it harms the soil."),
        ], steps=[S("Choose", text="Fallow and manure restore humus and nutrients, so they keep soil productive.")],
           concept="Soil management", skill="Application",
           hint="Which method gives back humus and nutrients to the soil?"),
        MC("Why is the population density of the western highlands higher than that of much of the southern forest?", [
            C("Volcanic soils are fertile and the climate is cool, which support farming.", correct=True),
            C("The highlands have no rain.", why="The highlands have plenty of rain."),
            C("The highlands have ferralitic soils.", why="The highlands have mainly volcanic soils."),
            C("The highlands are at sea level.", why="The highlands are high, not at sea level."),
        ], steps=[S("Link soil to population", text="Fertile volcanic soils and a cool climate support intensive farming and many people.")],
           concept="Soil and population density", skill="Reasoning",
           hint="Think about soil fertility and temperature in the highlands."),
    ]))
