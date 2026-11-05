"""Practice sets for Form 5 Geography: Pressure and winds, Basic concepts of climate, Environmental hazards (one per lesson)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Hydrology, Meteorology and Climatology"
PW = "Pressure and winds"
BC = "Basic concepts of climate"
EH = "Environmental hazards"


def Q(prompt, right, wrong, pos, steps, concept, skill, hint, diagram="", alt=""):
    """4-option MC: `wrong` is three (text, why) pairs; the right option goes at index `pos`."""
    ch = [C(t, why=w) for t, w in wrong]
    ch.insert(pos, C(right, correct=True))
    return MC(prompt, ch, steps=[S(a, text=b) for a, b in steps], concept=concept, skill=skill, hint=hint,
              diagram=diagram, diagram_alt=alt)


SETS = []

# ------------------------------------------------------------------ 1. Pressure belts and planetary winds
SETS.append(practice_set(
    module=MODULE, topic=PW,
    title="Pressure belts and planetary winds",
    lesson="clim-pressure-belts-and-planetary-winds",
    questions=[
        Q("Which instrument is used to measure atmospheric pressure?", "Barometer", [
            ("Thermometer", "A thermometer measures temperature, not pressure."),
            ("Rain gauge", "A rain gauge measures the amount of rainfall."),
            ("Anemometer", "An anemometer measures wind speed. Pressure is measured with a barometer."),
        ], 2, [("Recall", "Atmospheric pressure is measured with a barometer, in millibars or hectopascals.")],
          "Measuring atmospheric pressure", "Recall", "Think of the instrument whose name starts with 'baro'."),
        Q("Which pressure belt lies along the equator?", "Equatorial low", [
            ("Equatorial high", "The equator is hot, but hot air rises, so the pressure there is low."),
            ("Subtropical high", "The subtropical highs lie near 30 degrees north and south, not at the equator."),
            ("Polar high", "The polar highs lie at the poles."),
        ], 1, [("Recall", "The sun is overhead at the equator, the air is hot and rises, and pressure is low. This belt is the equatorial low.")],
          "Equatorial low pressure belt", "Recall", "Is air that rises making pressure higher or lower at the ground?"),
        Q("Why is there a low-pressure belt at the equator?", "Hot air rises there", [
            ("Cold air sinks there", "Sinking cold air makes high pressure, as at the poles."),
            ("The ocean is deepest there", "Pressure belts depend on rising and sinking air, not on the depth of the sea."),
            ("The wind blows away from the equator", "The trade winds blow towards the equator, so air is not blown away from it."),
        ], 3, [("Reason", "The overhead sun heats the surface. The warm air rises, so less air presses on the ground and the pressure is low.")],
          "Cause of the equatorial low", "Concept", "What happens to air that is heated strongly?"),
        Q("A wind blows from the south-west towards the north-east. What is it called?", "A south-west wind", [
            ("A north-east wind", "Winds are named after the direction they blow FROM, not the direction they go to."),
            ("A south-east wind", "South-east is a different direction. Check the compass points in the question."),
            ("An easterly wind", "A wind from the east blows towards the west."),
        ], 0, [("Rule", "A wind is named after the direction it blows from. This wind starts in the south-west, so it is a south-west wind.")],
          "Naming winds", "Application", "Name the wind by where it starts, not where it ends."),
        Q("Between which two pressure belts do the trade winds blow?", "From the subtropical highs to the equatorial low", [
            ("From the equatorial low to the subtropical highs", "Wind blows from high to low pressure, so this direction is wrong."),
            ("From the polar highs to the subpolar lows", "These are the polar easterlies."),
            ("From the subtropical highs to the subpolar lows", "These are the westerlies."),
        ], 2, [("Reason", "Wind blows from high to low pressure. The trade winds go from the subtropical highs (about 30 degrees) to the equatorial low.")],
          "Where the trade winds blow", "Concept", "Remember that wind goes from high to low pressure."),
        NUM("Use the map. In January the ITCZ lies at about 5 degrees north and in July at about 20 degrees north. Through how many degrees of latitude does it move north between January and July?", 15,
            steps=[S("Subtract the two latitudes", math=r"20 - 5 = 15", text="The ITCZ moves about 15 degrees of latitude north.")],
            concept="Movement of the ITCZ", skill="Interpretation", hint="Read the two latitudes from the labels on the map and subtract.",
            diagram="f5g-clim-itcz-west-africa.svg",
            diagram_alt="Simplified map of West Africa with the ITCZ about 5 degrees north in January and about 20 degrees north in July, the harmattan arrows from the north-east and the monsoon arrows from the south-west"),
        Q("Look at the map. When the ITCZ is at its July position, which wind reaches Douala?", "The moist south-west monsoon", [
            ("The dry harmattan", "The harmattan reaches the coast only when the ITCZ is in the south, in the northern winter."),
            ("A polar easterly", "Polar easterlies are cold winds from the poles and do not reach West Africa."),
            ("A katabatic wind", "A katabatic wind is a local night wind down a slope."),
        ], 3, [("Read the map", "In July the ITCZ is far north, near 20 degrees north."),
               ("Conclude", "Warm moist air blows in from the Atlantic Ocean from the south-west. This is the south-west monsoon.")],
          "South-west monsoon and ITCZ", "Interpretation", "Where is the ITCZ in July, north or south of Douala?",
          diagram="f5g-clim-itcz-west-africa.svg",
          alt="Simplified map of West Africa with the ITCZ about 5 degrees north in January and about 20 degrees north in July, the harmattan arrows from the north-east and the monsoon arrows from the south-west"),
        Q("Why does the harmattan blow over northern Cameroon in January?", "The ITCZ is in the south, so the north-east trade wind blows from the Sahara", [
            ("The ITCZ is in the north, so the wind blows from the Atlantic", "When the ITCZ is in the north the wind comes from the Atlantic and is moist (the monsoon)."),
            ("The Earth is closest to the sun in January", "Distance to the sun does not explain wind direction. The movement of the ITCZ does."),
            ("A sea breeze blows inland all year", "A sea breeze is a local daytime wind from the sea, not a dry dusty wind."),
        ], 1, [("Cause", "In January the ITCZ is in the south. The north-east trade wind then blows over the Sahara and across West Africa."),
               ("Result", "It carries dry, dusty air. This is the harmattan.")],
          "Cause of the harmattan", "Reasoning", "Where does the north-east trade wind come from over West Africa?"),
    ]))


# ------------------------------------------------------------------ 2. Local winds
SETS.append(practice_set(
    module=MODULE, topic=PW,
    title="Sea and land breezes, slope winds and monsoons",
    lesson="clim-local-winds",
    questions=[
        Q("When does a sea breeze blow?", "During the day", [
            ("At night", "At night the land cools and a land breeze blows from the land to the sea."),
            ("Only in the dry season", "Sea breezes blow on most days, in every season. They are not tied to the dry season."),
            ("Only in winter", "Sea breezes depend on the land being warmer than the sea, which is common on sunny days in any season."),
        ], 0, [("Recall", "By day the land is warmer than the sea. Cool air flows from the sea to the land.")],
          "When a sea breeze blows", "Recall", "Which is warmer during the day, land or sea?"),
        Q("A land breeze blows", "from the land to the sea", [
            ("from the sea to the land", "That is a sea breeze."),
            ("up a mountain slope", "That is an anabatic wind."),
            ("from the Sahara in the dry season", "That is the harmattan, a seasonal wind."),
        ], 1, [("Recall", "Winds are named after where they blow from. A land breeze blows from the land to the sea at night.")],
          "Direction of a land breeze", "Recall", "A wind is named after the place it comes from."),
        Q("Why does the land heat up faster than the sea during the day?", "Water takes in heat to a great depth and warms slowly", [
            ("The land is closer to the sun", "The land and the sea are the same distance from the sun."),
            ("The sea has no heat to give", "The sea holds a lot of heat. It is just slower to warm and slower to cool."),
            ("The wind blows heat onto the land", "Wind does not heat the land. It is the sun that heats the land and the sea differently."),
        ], 2, [("Reason", "Water takes in heat to a great depth and moves heat around by mixing, so it warms and cools slowly. Land heats and cools quickly.")],
          "Unequal heating of land and sea", "Concept", "Compare how fast a stone and a pot of water warm in the sun."),
        Q("In the afternoon, which statement about pressure is correct on a coast?", "Pressure is lower over the land than over the sea", [
            ("Pressure is higher over the land than over the sea", "Warm air over the land rises and pressure falls. This is the opposite of what happens."),
            ("Pressure is the same over land and sea", "Equal pressure would give no wind. The difference in pressure causes the sea breeze."),
            ("Pressure is lower over the sea than over the land", "That is the situation at night, when the land breeze blows."),
        ], 3, [("Reason", "Warm air over the land rises, so pressure there is low. Cooler air over the sea has higher pressure and flows to the land.")],
          "Pressure and the sea breeze", "Concept", "What happens to pressure at the surface where air rises?"),
        Q("Look at the diagram. Which wind is shown in the panel that has a sun?", "A sea breeze", [
            ("A land breeze", "A land breeze is shown in the right-hand panel, which has a moon."),
            ("A katabatic wind", "A katabatic wind flows down a slope, not between sea and land."),
            ("A monsoon", "A monsoon is a seasonal wind. The diagram is headed DAY and NIGHT, so it shows a daily wind."),
        ], 3, [("Read the figure", "The left panel has a sun, so it is daytime. The surface arrow points from the sea to the land."),
                   ("Name it", "A wind from the sea in the day is a sea breeze.")],
          "Reading a sea breeze diagram", "Interpretation", "Look for the sun or the moon in each panel.",
          diagram="f5g-clim-sea-land-breeze.svg",
          alt="Two panels. Left panel DAY: sun, surface arrow from sea to land, rising arrow over land. Right panel NIGHT: moon, surface arrow from land to sea, rising arrow over the sea"),
        Q("Which wind blows down a mountain slope at night?", "Katabatic wind", [
            ("Anabatic wind", "An anabatic wind blows up a slope, in the day."),
            ("Sea breeze", "A sea breeze blows from the sea to the land."),
            ("Trade wind", "A trade wind is a planetary wind between the subtropical highs and the equator."),
        ], 0, [("Reason", "At night the slope cools. The air next to it becomes cold and heavy and flows down into the valley. That is the katabatic wind.")],
          "Katabatic wind", "Recall", "Which name means 'going down'?"),
        Q("Which statement describes a monsoon correctly?", "A wind that changes direction with the season over a large area", [
            ("A wind that changes direction every day and night", "That describes land and sea breezes."),
            ("A wind that blows in one direction all year", "Planetary winds blow in one general direction. A monsoon reverses."),
            ("A wind that blows only up mountain slopes", "That describes an anabatic wind."),
        ], 1, [("Define", "A monsoon is a seasonal reversal of wind direction over a large area, caused by the different heating of a large land mass and the ocean.")],
          "Definition of a monsoon", "Concept", "How long does it take a monsoon to change direction: a day or a season?"),
        Q("Why is the south-west monsoon wet in West Africa?", "It blows from the warm Atlantic Ocean to a hot land, bringing moist air", [
            ("It blows from the Sahara over dry land", "Wind from the Sahara is the dry harmattan."),
            ("It is a cold wind that sinks over the land", "Sinking air is dry. The monsoon is warm, moist and rising over the hot land."),
            ("It is a wind that blows only at night", "The monsoon is a seasonal wind. It blows day and night during the wet season."),
        ], 2, [("Reason", "In the northern summer the land is hot and the pressure is low. Moist air from the Atlantic is pulled in from the south-west."),
               ("Result", "The air rises over the land, cools and brings rain.")],
          "Wet south-west monsoon", "Application", "Where does the south-west monsoon pick up its moisture?"),
    ]))


# ------------------------------------------------------------------ 3. Tropical humid and wet-and-dry climates
SETS.append(practice_set(
    module=MODULE, topic=BC,
    title="The three climatic regions: humid and wet-and-dry",
    lesson="clim-tropical-humid-and-wet-and-dry-climates",
    questions=[
        Q("Which list gives the three tropical climatic regions?", "Tropical humid, tropical wet and dry, tropical dry", [
            ("Tropical humid, polar, Mediterranean", "Polar and Mediterranean climates are not the tropical regions studied here."),
            ("Equatorial, temperate, polar", "These are not the three tropical regions in the syllabus."),
            ("Tropical dry, monsoon, mountain", "Monsoon and mountain are not climatic regions in this list."),
        ], 2, [("Recall", "The three regions are tropical humid, tropical wet and dry, and tropical dry.")],
          "The three climatic regions", "Recall", "All three names start with the word 'tropical'."),
        Q("On the map, the dark green band along the equator shows which climate?", "Tropical humid", [
            ("Tropical dry", "The tropical dry climate is the brown band near the two tropics."),
            ("Tropical wet and dry", "The yellow bands lie on either side of the green band."),
            ("A polar climate", "Polar climates are not shown on this map."),
        ], 0, [("Read the key", "The key says dark green is tropical humid."),
               ("Check", "The green band lies on the equator, where the sun is overhead and rainfall is heavy.")],
          "Locating tropical humid", "Interpretation", "Read the key under the map.",
          diagram="f5g-clim-world-climate-regions.svg",
          alt="Simplified world map with a green band of tropical humid climate along the equator, yellow bands of wet and dry climate on both sides and brown bands of dry climate near the tropics"),
        Q("Which annual temperature range is typical of the tropical humid climate?", "Less than 5°C", [
            ("About 20°C", "A very large range like this belongs to the tropical dry climate."),
            ("About 40°C", "No tropical station has a range as large as 40°C."),
            ("More than 30°C", "This is far too large for any tropical climate."),
        ], 3, [("Recall", "In the tropical humid climate the sun is high all year, so the temperature hardly changes. The range is usually less than 5°C.")],
          "Temperature range in the humid climate", "Recall", "Is the temperature steady or does it change a lot in the humid climate?"),
        Q("Which description fits a tropical wet-and-dry climate?", "About 1200 mm of rain a year, falling mainly in one wet season", [
            ("About 3000 mm of rain spread evenly through the year", "This describes a very wet tropical humid climate with no dry season."),
            ("Less than 100 mm of rain a year", "This describes the tropical dry climate."),
            ("Cool temperatures and snow in winter", "Snow does not fall at low levels in the tropics."),
        ], 0, [("Recall", "The wet-and-dry climate has about 750 mm to 1500 mm of rain a year, falling mainly in a wet season.")],
          "Features of the wet-and-dry climate", "Concept", "Which climate has a clear wet season and a long dry season?"),
        NUM("Use the graph. Add the monthly rainfall of Station A (30, 60, 150, 170, 200, 150, 70, 90, 230, 300, 130 and 40 mm). What is the total annual rainfall, in mm?", 1620,
            steps=[S("Add the twelve values", math=r"30+60+150+170+200+150+70+90+230+300+130+40 = 1620", text="The total is 1620 mm, which is more than 1500 mm.")],
            concept="Annual rainfall total", skill="Calculation", hint="Add all twelve monthly bars.",
            diagram="f5g-clim-graph-humid.svg",
            diagram_alt="Climate graph for Station A with monthly rainfall bars from 30 mm to 300 mm and a temperature line between 23 and 26 degrees Celsius"),
        NUM("Station B has monthly temperatures of 26, 28, 30, 29, 27, 25, 24, 24, 25, 26, 26 and 25°C. What is its mean annual temperature, in °C? (Give the answer to one decimal place.)", 26.3,
            tolerance=0.1,
            steps=[S("Add the twelve values", math=r"26+28+30+29+27+25+24+24+25+26+26+25 = 315"),
                   S("Divide by 12", math=r"315 \div 12 = 26.25", text="This is 26.3°C to one decimal place.")],
            concept="Mean annual temperature", skill="Calculation", hint="Add all the monthly temperatures, then divide by the number of months.",
            diagram="f5g-clim-graph-wetdry.svg",
            diagram_alt="Climate graph for Station B with rainfall bars from 0 to 270 mm and a temperature line from 24 to 30 degrees Celsius"),
        Q("Which statement about the seasons of Station B is correct?", "It has a wet season from May to September and a dry season from November to February", [
            ("It has no dry season", "Rainfall is 0 mm in January and December, so there is a clear dry season."),
            ("It is wettest in January", "January has 0 mm. The wettest month is August with 270 mm."),
            ("It has rain of over 100 mm in every month", "Rainfall is below 100 mm in seven months, and is 0 mm in January and December."),
        ], 2, [("Read the bars", "Bars are above 100 mm from May to September and tiny or zero from November to February."),
               ("Conclude", "This is the pattern of a tropical wet-and-dry climate.")],
          "Describing seasons from a graph", "Interpretation", "Look for months where the bars are tall and months where they are almost zero.",
          diagram="f5g-clim-graph-wetdry.svg",
          alt="Climate graph for Station B with rainfall bars from 0 to 270 mm and a temperature line from 24 to 30 degrees Celsius"),
        Q("Which town in Cameroon has a tropical wet-and-dry climate?", "Garoua", [
            ("Douala", "Douala is on the coast and has a very wet tropical humid climate."),
            ("Ebolowa", "Ebolowa is in the humid south."),
            ("Kribi", "Kribi is on the humid coast."),
        ], 1, [("Locate", "Garoua is the capital of the North Region."),
               ("Conclude", "The north has a long dry season and a shorter wet season: a wet-and-dry climate.")],
          "Wet-and-dry climate in Cameroon", "Application", "Which of these towns is in the north of the country?"),
    ]))


# ------------------------------------------------------------------ 4. Tropical dry climate and climate graphs
SETS.append(practice_set(
    module=MODULE, topic=BC,
    title="The tropical dry climate and climate graphs",
    lesson="clim-tropical-dry-climate-and-climate-graphs",
    questions=[
        Q("Which annual rainfall is typical of the tropical dry climate?", "Less than 250 mm", [
            ("About 1000 mm", "This is in the range of the wet-and-dry climate."),
            ("More than 1500 mm", "This is the humid climate."),
            ("About 2500 mm", "This is a very wet humid climate."),
        ], 1, [("Recall", "A desert climate receives less than about 250 mm of rain a year.")],
          "Rainfall of the dry climate", "Recall", "Think of how little rain falls in the Sahara."),
        Q("Where is the tropical dry climate found?", "Near the tropics of Cancer and Capricorn", [
            ("Along the equator", "The equator has the humid climate."),
            ("Near the North and South Poles", "These are polar regions, not tropical."),
            ("Only on the coast of West Africa", "Most deserts are in continental interiors and on the western sides of continents, and not only in West Africa."),
        ], 3, [("Recall", "The dry climate lies near the two tropics, from about 15 degrees to 30 degrees north and south.")],
          "Location of the dry climate", "Recall", "Look at the brown bands on the world map in the lesson."),
        Q("Why does the Sahara get so little rain?", "Air in the subtropical high-pressure belt is sinking", [
            ("The sun is never overhead", "The sun is high in the Sahara. The problem is the sinking air, not a lack of sun."),
            ("The ITCZ stays there all year", "The ITCZ brings rain. It stays near the Sahara only for a short time and only at its southern edge."),
            ("The Sahara is too close to the equator", "The Sahara is far from the equator. It lies near 30 degrees north."),
        ], 0, [("Reason", "Near 30 degrees north the subtropical high-pressure belt has sinking air. Sinking air warms and dries, so clouds do not form.")],
          "Cause of the dry climate", "Concept", "Is the air rising or sinking in a high-pressure belt?"),
        Q("Which feature is different in the tropical dry climate compared with the tropical humid climate?", "The annual temperature range is much larger", [
            ("It is hot all year", "Both climates are hot all year."),
            ("It lies in the tropics", "Both climates lie in the tropics."),
            ("It has some rain every year", "Both have some rain. The difference is how much."),
        ], 2, [("Compare", "The humid climate has a small range, under 5 degrees. The dry climate has a large range, 15 degrees to 20 degrees or more.")],
          "Compare humid and dry climates", "Concept", "Think about clear skies and cloudy skies."),
        NUM("Use the graph. Add the monthly temperatures of Station C (15, 17, 21, 26, 31, 34, 35, 34, 32, 27, 21 and 16 degrees) and divide by 12. What is the mean annual temperature, in degrees Celsius? (Give the answer to one decimal place.)", 25.8,
            tolerance=0.1,
            steps=[S("Add the twelve values", math=r"15+17+21+26+31+34+35+34+32+27+21+16 = 309"),
                   S("Divide by 12", math=r"309 \div 12 = 25.75", text="To one decimal place this is 25.8 degrees Celsius.")],
            concept="Mean temperature", skill="Calculation", hint="Add the 12 temperatures, then divide by 12.",
            diagram="f5g-clim-graph-dry.svg",
            diagram_alt="Climate graph for Station C: rainfall bars of 0 to 3 millimetres and a temperature line from 15 degrees Celsius in January to 35 degrees Celsius in July"),
        NUM("Use the graph for Station C. What is the annual temperature range, in degrees Celsius?", 20,
            steps=[S("Find the highest and lowest", text="The highest monthly temperature is 35 in July and the lowest is 15 in January."),
                   S("Subtract", math=r"35 - 15 = 20")],
            concept="Temperature range", skill="Calculation", hint="Highest minus lowest.",
            diagram="f5g-clim-graph-dry.svg",
            diagram_alt="Climate graph for Station C: rainfall bars of 0 to 3 millimetres and a temperature line from 15 degrees Celsius in January to 35 degrees Celsius in July"),
        Q("Station X has a temperature range of 7 degrees Celsius, rain of 0 mm in four months and 980 mm in the year. Which climate is it?", "Tropical wet and dry", [
            ("Tropical humid", "The humid climate has no dry months and a range under 5 degrees."),
            ("Tropical dry", "The dry climate has under 250 mm a year. Station X has 980 mm."),
            ("Cold polar", "A polar climate is not tropical and does not have this temperature or rainfall."),
        ], 0, [("Temperature", "A range of 7 degrees is about 5 to 10 degrees, which fits wet and dry."),
               ("Rainfall", "980 mm is between 750 and 1500 mm, and four months are dry. This is a wet-and-dry climate.")],
          "Identify a climate from data", "Application", "Check the dry months first, then the total rainfall."),
        Q("Which pair of words best describes the nights and the days of a desert?", "Cold nights and very hot days", [
            ("Warm nights and cool days", "This is the opposite pattern."),
            ("Cloudy nights and cloudy days", "Desert skies are mostly cloudless."),
            ("Rainy nights and dry days", "Deserts are dry both day and night."),
        ], 1, [("Reason", "The sky is clear, so the ground heats strongly by day and loses its heat quickly at night. That is why the range of temperature is large.")],
          "Daily temperature in a desert", "Reasoning", "Clouds act like a blanket. What happens when there are none?"),
    ]))


# ------------------------------------------------------------------ 5. Factors influencing weather and climate
SETS.append(practice_set(
    module=MODULE, topic=BC,
    title="Factors that influence weather and climate",
    lesson="clim-factors-influencing-weather-and-climate",
    questions=[
        Q("Which factor of climate means the height of a place above sea level?", "Altitude", [
            ("Latitude", "Latitude is distance north or south of the equator."),
            ("Continentality", "Continentality is distance from the sea."),
            ("Relief", "Relief is the shape of the land. Height above sea level is called altitude."),
        ], 2, [("Recall", "Altitude is the height above sea level. Latitude is the distance from the equator.")],
          "Meaning of altitude", "Recall", "Which word sounds like 'altitude' on an aeroplane?"),
        Q("On average, how much does temperature fall for every 1000 m you climb?", "About 6.5°C", [
            ("About 65°C", "This is far too large. A fall of 65°C for each 1000 m would be impossible."),
            ("About 0.65°C", "This is too small. It is ten times less than the true average."),
            ("About 16°C", "This is more than twice the true average."),
        ], 0, [("Recall", "The average fall is about 6.5°C for every 1000 m of height.")],
          "Temperature change with height", "Recall", "It is a number between 5 and 10."),
        NUM("A place at sea level has a mean temperature of 30°C. Using a fall of 6.5°C for every 1000 m, find the temperature at 2500 m, in °C.", 13.75, tolerance=0.05,
            steps=[S("Find the fall", math=r"\dfrac{2500}{1000} \times 6.5 = 16.25", text="The temperature falls by 16.25°C."),
                   S("Subtract", math=r"30 - 16.25 = 13.75", text="The temperature at 2500 m is 13.75°C.")],
            concept="Temperature and altitude", skill="Calculation", hint="Work out how many thousand metres 2500 m is, then multiply by 6.5."),
        Q("What is a rain shadow?", "A dry area on the leeward side of a mountain", [
            ("A very wet area on the windward side of a mountain", "The windward side gets heavy rain. The rain shadow is on the other side."),
            ("A dark cloud over a lake", "A rain shadow is a dry area, not a cloud."),
            ("The area under a rain cloud in the afternoon", "A rain shadow is formed by relief and is not just the area under a cloud."),
        ], 3, [("Explain", "Air rises on the windward side, cools and loses its rain. It sinks on the leeward side, warms and dries, so the leeward side is dry.")],
          "Rain shadow", "Concept", "Is the leeward side the side the wind blows onto or the side it blows away from?"),
        Q("A cold ocean current flows along a coast. What is the most likely effect on that coast?", "The coast is cooler and drier, with fog", [
            ("The coast is warmer and very wet", "A warm current, not a cold one, makes a coast warmer and wetter."),
            ("The coast has more thunderstorms", "Thunderstorms come from rising warm air. A cold current makes the air stable."),
            ("The coast gets heavy rain all year", "Heavy rain comes with warm, moist air. A cold current does the opposite."),
        ], 2, [("Reason", "A cold current cools the air above it and makes it stable. Little water evaporates, so there is little rain and often fog."),
               ("Example", "The Namib coast is dry next to the cold Benguela Current.")],
          "Effect of ocean currents", "Concept", "A cold current cools the air above it. Does cooler air hold more or less moisture?"),
        Q("Why are desert nights colder than nights in a forest at the same latitude?", "The clear sky lets heat escape", [
            ("Clouds trap heat over deserts", "Deserts have few clouds. That is the cause of the cold nights."),
            ("The desert is nearer the sea", "Most deserts are far from the sea, where the range of temperature is large."),
            ("Desert sand is always cold", "Sand is very hot by day. It loses its heat quickly because there are no clouds."),
        ], 1, [("Reason", "Clouds trap heat at night like a blanket. A clear desert sky has no blanket, so heat escapes and nights are cold.")],
          "Cloud cover and temperature", "Reasoning", "What do clouds do to heat at night?"),
        NUM("Look at the figure. By how many degrees Celsius is the temperature range of the inland station greater than that of the coastal station?", 8,
            steps=[S("Read the two ranges", text="The coastal range is 3°C and the inland range is 11°C."),
                   S("Subtract", math=r"11 - 3 = 8")],
            concept="Continentality and range", skill="Interpretation", hint="Read the two ranges written on the graph and subtract.",
            diagram="f5g-clim-continentality.svg",
            diagram_alt="Graph of monthly temperatures for a coastal station with a range of 3 degrees Celsius and an inland station with a range of 11 degrees Celsius"),
        Q("Which air mass produces the dry, dusty harmattan?", "A hot, dry air mass that forms over the Sahara", [
            ("A warm, moist air mass that forms over the Atlantic", "This air mass arrives with the south-west monsoon and brings rain."),
            ("A cold air mass that forms over the poles", "Polar air does not reach West Africa."),
            ("A cool air mass that forms over Lake Chad", "Lake Chad is not big enough to form an air mass that crosses West Africa."),
        ], 0, [("Reason", "An air mass takes the features of the region where it forms. Over the hot, dry Sahara it is hot and dry."),
               ("Result", "When it blows across West Africa it is called the harmattan.")],
          "Air masses of West Africa", "Application", "Where does the harmattan come from?"),
    ]))


# ------------------------------------------------------------------ 6. Global warming
SETS.append(practice_set(
    module=MODULE, topic=EH,
    title="Global warming: causes, effects and responses",
    lesson="clim-global-warming",
    questions=[
        Q("Look at the diagram. What do greenhouse gases do with the heat that leaves the Earth's surface?", "They send some of it back down to the surface", [
            ("They let all of it escape to space", "The diagram shows that only some heat escapes. Greenhouse gases return a part."),
            ("They stop sunlight from reaching the ground", "Sunlight passes through the atmosphere to the ground. It is the outgoing heat that is trapped."),
            ("They cool the surface by sending heat to the sea", "Greenhouse gases return heat to the surface, which keeps it warm."),
        ], 1, [("Read the diagram", "Red arrows show heat. One goes down from the gas layer to the surface."),
               ("Conclude", "Greenhouse gases trap part of the heat and send it back, which keeps the Earth warm.")],
          "The greenhouse effect", "Interpretation", "Follow the red arrows from the surface to the gas layer.",
          diagram="f5g-clim-greenhouse-effect.svg",
          alt="Diagram of the greenhouse effect: sunlight reaches the surface, the surface sends out heat, greenhouse gases send some heat back down and some heat escapes to space"),
        Q("Which of these is a greenhouse gas?", "Carbon dioxide", [
            ("Oxygen", "Oxygen is not a main greenhouse gas."),
            ("Nitrogen", "Nitrogen is most of the air but does not trap heat."),
            ("Argon", "Argon is an inert gas and does not trap heat."),
        ], 3, [("Recall", "The main greenhouse gases are carbon dioxide, methane, nitrous oxide and water vapour.")],
          "Greenhouse gases", "Recall", "It is the gas that plants take in and cars release."),
        Q("Which human activity adds the most carbon dioxide to the air?", "Burning coal, oil and gas", [
            ("Growing food crops on small farms", "Small-scale farming adds little compared with burning fuels."),
            ("Drinking water from wells", "Collecting water does not release carbon dioxide."),
            ("Building schools from local materials", "Building does not release much carbon dioxide compared with burning fuels."),
        ], 0, [("Recall", "Burning fossil fuels in power stations, factories and vehicles releases large amounts of carbon dioxide.")],
          "Causes of global warming", "Recall", "Think of exhaust pipes and factory chimneys."),
        Q("How does deforestation add to global warming?", "Fewer trees take in carbon dioxide, and burned trees release it", [
            ("Trees release methane when they are cut", "Cutting trees does not release methane. It removes a store of carbon dioxide."),
            ("Trees reflect sunlight into space", "Forests are dark and absorb sunlight. They do not reflect it into space."),
            ("Trees make the air wetter and cause floods", "Trees can reduce floods. They are not a main cause of warming."),
        ], 2, [("Reason", "Trees take in carbon dioxide as they grow. When they are cut and burned, this store is lost and the carbon dioxide returns to the air.")],
          "Deforestation and warming", "Concept", "What do trees take in from the air?"),
        Q("Which is a possible positive effect of global warming?", "A longer growing season in some cold regions", [
            ("Rising sea levels", "This is a negative effect. It floods low coasts."),
            ("More droughts in the Sahel", "This is a negative effect. It reduces crops and water."),
            ("Loss of coral reefs", "This is a negative effect on sea life."),
        ], 2, [("Think", "Positive effects are few and occur mainly in cold lands."),
                   ("Conclude", "In some cold regions a warmer climate can lengthen the time in which crops grow.")],
          "Positive effects of warming", "Concept", "Which cold-region benefit comes with warmer weather?"),
        Q("Which of these is an example of mitigation?", "Using solar and hydroelectric power instead of fossil fuels", [
            ("Building a sea wall in a flood-prone town", "A sea wall helps people adapt to rising seas. It does not cut gases."),
            ("Growing drought-resistant crops", "This helps farmers adapt to drought. It does not reduce gases."),
            ("Moving a village away from the coast", "This is adaptation to rising seas."),
        ], 0, [("Define", "Mitigation reduces the causes of global warming by reducing greenhouse gases."),
               ("Apply", "Solar and hydroelectric power release almost no carbon dioxide, so they cut emissions.")],
          "Mitigation measures", "Application", "Which choice cuts the amount of gas that goes into the air?"),
        Q("A farmer in the Far North plants a drought-resistant crop. What kind of response is this?", "Adaptation", [
            ("Mitigation", "Mitigation reduces greenhouse gases, which a change of crop does not do."),
            ("A natural cause of global warming", "A crop choice is not a cause of warming."),
            ("A cause of the greenhouse effect", "Planting a different crop does not add greenhouse gases."),
        ], 3, [("Reason", "The farmer is not cutting gases. The farmer is coping with a hotter, drier climate by changing the crop. That is adaptation.")],
          "Adaptation measures", "Application", "Is the farmer reducing the cause or coping with the effect?"),
        Q("Why is Africa considered vulnerable to global warming even though it has added little of the greenhouse gases?", "Many people depend on rain-fed farming and have few resources to cope with droughts and floods", [
            ("Africa is the largest source of greenhouse gases", "Africa has added very little to the world total."),
            ("Africa has no forests to store carbon", "Africa has large forests, such as the Congo Basin forests."),
            ("Africa is too cold for farming", "Most of Africa is warm. The problem is rain and heat, not cold."),
        ], 1, [("Reason", "Many farmers rely on rain. Droughts, floods and heat can destroy harvests."),
               ("Resources", "Poorer countries often have fewer means to build defences or to buy new technology.")],
          "Vulnerability of Africa", "Reasoning", "Think of farmers who depend on the rains."),
    ]))


# ------------------------------------------------------------------ 7. Floods, droughts and desertification
SETS.append(practice_set(
    module=MODULE, topic=EH,
    title="Floods, droughts and desertification: causes and responses",
    lesson="clim-floods-droughts-and-desertification",
    questions=[
        Q("What is a flood?", "Water covering land that is normally dry", [
            ("A long period with very little rain", "This is a drought."),
            ("The slow change of fertile land into desert-like land", "This is desertification."),
            ("A strong wind that blows from the sea", "This describes a sea breeze, not a flood."),
        ], 2, [("Recall", "A flood happens when water covers land that is normally dry.")],
          "Definition of a flood", "Recall", "Think of what happens when a river overflows."),
        Q("In which region of Cameroon are droughts most common and most serious?", "The Far North, near Lake Chad", [
            ("The South Region", "The south has heavy rain in nearly every month, so droughts are less serious."),
            ("The coast near Limbe", "The coast near Mount Cameroon is one of the wettest places in Africa."),
            ("The South-West forests", "These forests receive heavy rain and drought is rare."),
        ], 0, [("Recall", "The Far North lies in the Sahel, where rain is short and unreliable, so droughts are most serious there.")],
          "Where droughts occur", "Recall", "Which region of Cameroon is in the Sahel?"),
        Q("Look at the diagram. Why does the paved town flood faster than the vegetated land?", "Water cannot soak in, so it runs off quickly and drains block", [
            ("There is more rain in the town than on vegetated land", "The diagram shows the same rain on both. The difference is what happens to the water."),
            ("Water soaks into paved ground faster than into soil", "Paved ground is sealed, so water cannot soak in."),
            ("The vegetation on the left makes rain fall faster", "Plants do not make rain fall faster. They help the soil soak up water."),
        ], 1, [("Compare", "On the left, water soaks into the soil. On the right, the pavement and blocked drain stop it."),
               ("Conclude", "Water runs off quickly along the surface and floods the street.")],
          "Urban flood causes", "Interpretation", "Compare what happens to the rain in the two pictures.",
          diagram="f5g-clim-urban-flood.svg",
          alt="Two panels: heavy rain on vegetated land where water soaks into the soil, and on a paved town where water runs off quickly and a drain is blocked"),
        Q("Which of these is a positive effect of floods on a river floodplain?", "They leave fertile silt that helps farming", [
            ("They destroy roads and bridges", "This is a negative effect."),
            ("They spread cholera", "This is a negative effect."),
            ("They kill animals and crops", "This is a negative effect."),
        ], 3, [("Recall", "Floods deposit fertile silt on the floodplain, which makes the soil rich, and they refill wells and wetlands.")],
          "Positive effects of floods", "Concept", "What does a river leave behind when the flood water goes down?"),
        Q("Look at the diagram. Which stage comes immediately after 'Less plant cover, bare soil'?", "Wind and rain erode the soil", [
            ("Overgrazing, tree cutting and bush fires", "This is where the cycle starts. It comes before the loss of plant cover."),
            ("Crops and grass fail and the land turns to desert", "This is the last stage. It comes after the soil has lost water and nutrients."),
            ("Soil loses water and nutrients", "This comes after erosion, not directly after the loss of plant cover."),
        ], 2, [("Follow the arrows", "Overgrazing leads to less plant cover and bare soil. The next arrow points to 'Wind and rain erode the soil'.")],
          "The desertification cycle", "Interpretation", "Follow the arrow clockwise from 'Less plant cover'.",
          diagram="f5g-clim-desertification-cycle.svg",
          alt="Cycle diagram of desertification: overgrazing, then less plant cover, then wind and rain erode the soil, then soil loses water and nutrients, then crops and grass fail and land turns to desert"),
        Q("What is overgrazing?", "Letting too many animals eat the plants on an area of land", [
            ("Planting too many trees on grazing land", "Planting trees helps to protect the soil."),
            ("Watering the grass with too much water", "Overgrazing is about animals, not about water."),
            ("Letting grass grow too tall", "Overgrazing is the opposite: the grass is eaten too short and too often."),
        ], 1, [("Recall", "Overgrazing means too many animals feed on the land. The plants cannot grow back, so the soil is left bare.")],
          "Overgrazing", "Recall", "Think of too many cattle on a small pasture."),
        Q("Which statement best distinguishes a drought from desertification?", "A drought is temporary, but desertification is a long-term loss of the land's ability to grow plants", [
            ("A drought happens only in forests, and desertification only on the coast", "Droughts and desertification both affect dry and semi-dry regions."),
            ("A drought is caused by floods, and desertification is caused by rain", "Floods do not cause droughts, and desertification is not caused by rain."),
            ("They mean exactly the same thing", "A drought can end when the rains return. Desertification does not simply reverse."),
        ], 3, [("Compare", "A drought is a spell of low rainfall. The land can recover when the rains return."),
               ("Contrast", "In desertification, the land loses its soil and plant cover for a long time.")],
          "Drought and desertification", "Concept", "Which of the two can recover when the rains come back?"),
        Q("Which pair of measures would best reduce flood damage in a town such as Douala?", "Clear drains and stop dumping rubbish, and keep wetlands free of buildings", [
            ("Build on wetlands and block drains", "This would make flooding worse."),
            ("Cut trees along river banks and pave all open ground", "This reduces soaking in, so floods get worse."),
            ("Build houses at the lowest point of the town", "Low ground floods first."),
        ], 0, [("Reason", "Floods are worse when water cannot flow away or soak in. Clear drains let water leave, and wetlands soak up extra water."),
               ("Conclude", "These are mitigation measures that reduce how often floods happen.")],
          "Flood management", "Application", "Which choice helps water to drain away or soak in?"),
    ]))


# ------------------------------------------------------------------ 8. Water scarcity
SETS.append(practice_set(
    module=MODULE, topic=EH,
    title="Water scarcity: causes, effects and solutions",
    lesson="clim-water-scarcity",
    questions=[
        Q("What is water scarcity?", "A shortage of safe fresh water for people, farming and industry", [
            ("Too much water covering the land", "This is a flood, not scarcity."),
            ("The slow change of farmland into desert", "This is desertification, a different hazard."),
            ("Heavy rain in the wet season", "Heavy rain is not scarcity. Scarcity is a shortage of water."),
        ], 1, [("Recall", "Water scarcity means there is not enough safe fresh water to meet people's needs.")],
          "Definition of water scarcity", "Recall", "The word 'scarce' means 'hard to find'."),
        Q("Look at the diagram. Which kind of scarcity is it when water exists but people lack wells, pipes or money to reach it?", "Economic scarcity", [
            ("Physical scarcity", "Physical scarcity means there is not enough water in the region."),
            ("Atmospheric scarcity", "This is not a kind of water scarcity in the syllabus."),
            ("Seasonal flooding", "Flooding is too much water, not too little."),
        ], 0, [("Read the diagram", "The right-hand box says: 'Water exists, but people lack wells, pipes, money or clean sources.'"),
               ("Name it", "This is economic scarcity.")],
          "Physical and economic scarcity", "Interpretation", "Read the two boxes in the diagram.",
          diagram="f5g-clim-water-scarcity-types.svg",
          alt="Two boxes: physical scarcity, where there is not enough water in the region, and economic scarcity, where water exists but people lack wells, pipes or money"),
        Q("Which of these is a human cause of water scarcity?", "Leaking pipes and wasteful irrigation", [
            ("A long drought", "A drought is a natural cause, though human activity can make it worse."),
            ("A year of low rainfall", "Low rainfall is natural, not a human cause."),
            ("A hot dry season", "A hot dry season is a natural event."),
        ], 3, [("Reason", "Pipes that leak and irrigation that wastes water lose water that people could use. These are human causes.")],
          "Causes of water scarcity", "Concept", "Which cause comes from people, not from the weather?"),
        Q("Which disease is often spread by unsafe drinking water?", "Cholera", [
            ("Sunburn", "Sunburn is caused by sunshine, not by drinking water."),
            ("Broken bones", "Broken bones are injuries and not diseases carried by water."),
            ("Hay fever", "Hay fever is caused by pollen in the air."),
        ], 0, [("Recall", "Cholera, typhoid and diarrhoea are spread when people drink water polluted by sewage.")],
          "Health effects of water scarcity", "Recall", "Which of these is a water-borne disease?"),
        NUM("A family of 6 people uses 20 litres of water per person each day. How many litres does the family use in 7 days?", 840,
            steps=[S("Daily use", math=r"6 \times 20 = 120", text="The family uses 120 litres a day."),
                   S("Weekly use", math=r"120 \times 7 = 840", text="In a week they use 840 litres.")],
            concept="Water use calculation", skill="Calculation", hint="Find the family's daily total first, then multiply by 7."),
        Q("Which region is most likely to suffer physical water scarcity?", "The Sahel, including the Far North of Cameroon", [
            ("The wet coast near Mount Cameroon", "This coast has heavy rain, so it is not short of water in the physical sense."),
            ("The humid forests of southern Cameroon", "Forests in the south receive rain in nearly every month."),
            ("The Congo Basin", "The Congo Basin is one of the wettest regions of the world."),
        ], 2, [("Reason", "The Sahel has low and unreliable rainfall, so there is physically little water."),
                   ("Example", "The Far North and the Lake Chad basin are in the Sahel.")],
          "Where water scarcity occurs", "Application", "Which region has a long dry season and little rain?"),
        Q("Which is a conservation measure that helps to protect water supplies?", "Planting trees and protecting forests on river catchments", [
            ("Cutting trees along river banks", "This increases runoff and erosion."),
            ("Pouring waste into streams", "This pollutes the water."),
            ("Draining wetlands for building", "Wetlands store water and drain slowly."),
        ], 1, [("Reason", "Trees on catchments help rain to soak in, refill wells and keep rivers clean. This conserves water.")],
          "Conservation of water", "Application", "Which choice keeps the source of water healthy?"),
        Q("Why does deforestation increase the risk of water scarcity?", "Rain runs off quickly instead of soaking into the ground to refill wells", [
            ("Trees make more rain fall than the ground can hold", "Trees help soak up rain. They do not cause too much rain."),
            ("Cut trees release water into the soil", "Cutting trees does not add water to the soil."),
            ("Without trees the sun cannot reach the ground", "Without trees more sunlight reaches the ground, which dries it faster."),
        ], 3, [("Reason", "Without plant cover, rain runs off the surface quickly."),
               ("Result", "Less water soaks into the ground, so wells and springs are not refilled, and water becomes scarce.")],
          "Deforestation and water supply", "Reasoning", "What do tree roots help the soil to do with rain?"),
    ]))


# ------------------------------------------------------------------ 9. Waste management
SETS.append(practice_set(
    module=MODULE, topic=EH,
    title="Waste management: types, problems and solutions",
    lesson="clim-waste-management",
    questions=[
        Q("Which of these is organic (biodegradable) waste?", "Vegetable leftovers from a market", [
            ("Used batteries", "Batteries are hazardous waste and do not rot."),
            ("Plastic bags", "Plastic does not rot. It stays in the environment for a very long time."),
            ("Broken glass", "Glass is solid waste that does not rot."),
        ], 2, [("Recall", "Organic waste is waste from plants and animals, such as food leftovers. It rots naturally.")],
          "Organic waste", "Recall", "Which item will rot and return to the soil?"),
        NUM("A town produces 40 tonnes of waste a day. The council collects 28 tonnes. What percentage of the waste is not collected?", 30,
            steps=[S("Find the uncollected waste", math=r"40 - 28 = 12", text="12 tonnes are not collected."),
                   S("Find the percentage", math=r"\dfrac{12}{40} \times 100 = 30", text="30% of the waste is not collected.")],
            concept="Waste collection calculation", skill="Calculation", hint="Subtract the collected waste from the total, then divide by the total."),
        Q("Look at the diagram. According to the waste hierarchy, which is the best way to deal with waste?", "Reduce", [
            ("Dispose in a landfill", "This is at the bottom of the hierarchy and is the worst choice."),
            ("Recycle", "Recycling is good, but it comes after reduce and reuse."),
            ("Compost or recover", "These are good ways to treat waste that cannot be avoided, and rank below reduce and reuse."),
        ], 3, [("Read the funnel", "The best choice is at the top and the worst at the bottom."),
               ("Conclude", "Reduce is at the top, so the best choice is not to make the waste at all.")],
          "The waste hierarchy", "Interpretation", "Look at which word is at the top of the funnel.",
          diagram="f5g-clim-waste-hierarchy.svg",
          alt="A funnel diagram of the waste hierarchy: reduce at the top, then reuse, recycle, compost or recover, and dispose at the bottom"),
        Q("How does uncollected rubbish make floods worse in a town?", "It blocks drains, so water cannot flow away", [
            ("It makes the rain fall harder", "Rubbish does not change the amount of rain."),
            ("It absorbs rainwater like soil", "Rubbish in a drain stops water from flowing and does not soak it up."),
            ("It cools the air above the town", "Rubbish does not change the air temperature in a way that causes floods."),
        ], 1, [("Reason", "Water runs along the streets into the drains. If the drains are full of rubbish, the water cannot flow away and spreads into the streets.")],
          "Waste and flooding", "Concept", "Where does the rain go when it enters a drain?"),
        Q("Which of these is an example of recycling?", "Melting old aluminium cans to make new ones", [
            ("Refilling a plastic water bottle many times", "This is reuse, because the same item is used again."),
            ("Carrying a cloth shopping bag", "This is reduce, because it avoids making plastic bag waste."),
            ("Burying rubbish in a landfill", "This is disposal, which is the last choice."),
        ], 0, [("Define", "Recycling means turning waste into new products."),
               ("Apply", "Melting cans to make new cans turns waste into a new product, so it is recycling.")],
          "Recycling", "Application", "Which choice turns waste into something new?"),
        Q("What is compost?", "Rotted organic waste that improves the soil", [
            ("A type of plastic that can be melted", "Compost comes from plants and food, not plastic."),
            ("A chemical that kills rats", "Compost is not a poison."),
            ("A kind of metal waste", "Compost is made from organic waste."),
        ], 2, [("Define", "Compost is the dark, crumbly material made when food and garden waste rot. It adds nutrients to the soil.")],
          "Composting", "Concept", "Think of what a farmer can do with vegetable waste."),
        Q("Why is plastic waste a special environmental hazard?", "It does not rot and stays in the environment for a very long time", [
            ("It rots very quickly and smells", "Plastic does not rot quickly. Food waste rots and smells."),
            ("It is always liquid", "Most plastic waste is solid."),
            ("It turns into soil in a few days", "Plastic does not turn into soil. It breaks into small pieces that last."),
        ], 1, [("Reason", "Plastic is not biodegradable. It breaks into smaller pieces but does not rot, so it blocks drains and harms water life for many years.")],
          "Plastic waste", "Concept", "What happens to plastic that is thrown away, compared with a banana peel?"),
        Q("Which sequence lists ways of dealing with waste from best to worst?", "Reduce, reuse, recycle, then dispose", [
            ("Dispose, recycle, reuse, reduce", "This is the order from worst to best."),
            ("Recycle, dispose, reduce, reuse", "Disposal is the worst choice and should come last."),
            ("Reuse, dispose, recycle, reduce", "Disposal should come last, and reduce comes first."),
        ], 3, [("Recall", "The waste hierarchy puts prevention first (reduce), then reuse, then recycling, and disposal last.")],
          "Order of the waste hierarchy", "Reasoning", "Which choice avoids making waste in the first place?"),
    ]))
