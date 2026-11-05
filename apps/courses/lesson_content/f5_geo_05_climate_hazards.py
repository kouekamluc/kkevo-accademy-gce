"""Form 5 Geography: Pressure and winds, Basic concepts of climate, Environmental hazards (9 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Hydrology, Meteorology and Climatology"
PW = "Pressure and winds"
BC = "Basic concepts of climate"
EH = "Environmental hazards"


def _merge_text(blocks):
    """Join neighbouring plain text blocks into one block (paragraphs separated by a blank line)."""
    out = []
    for b in blocks:
        if out and b["block_type"] == "text" and out[-1]["block_type"] == "text" and not b["title"] and not out[-1]["title"]:
            out[-1] = dict(out[-1], body=out[-1]["body"] + "\n\n" + b["body"])
        else:
            out.append(b)
    return out


LESSONS = []

# ------------------------------------------------------------------ 1. Pressure belts and planetary winds
LESSONS.append(lesson(
    module=MODULE,
    topic=PW,
    title="Atmospheric pressure, pressure belts and planetary winds",
    slug="clim-pressure-belts-and-planetary-winds",
    minutes=24,
    summary="What atmospheric pressure is and how it is measured, where the four pressure belts lie, how they drive the trade winds, westerlies and polar easterlies, and how the ITCZ brings the harmattan and the south-west monsoon to West Africa.",
    objectives=[
        "Define atmospheric pressure and pressure belts",
        "Represent the planetary pressure belts and the main planetary winds in a diagram",
        "Describe the main planetary winds: trade winds, westerlies and polar easterlies",
        "Explain how the shifting ITCZ gives West Africa the harmattan and the south-west monsoon",
    ],
    key_concepts=["Atmospheric pressure", "Barometer", "Pressure belts", "Trade winds", "Westerlies", "Polar easterlies", "ITCZ", "Harmattan"],
    blocks=[
        H("Introduction"),
        T("In Maroua in January, the air is dry and a fine dust hangs over the town. In Douala in July, the air is warm and wet, "
          "and the rain falls almost every day. The same country has two very different kinds of air at two times of the year. "
          "The reason is wind, and wind starts with pressure."),
        T("In this lesson you will learn what pressure is, where the great belts of high and low pressure lie, and which winds "
          "blow between them. At the end you will see how these winds explain the seasons of West Africa."),
        H("Atmospheric pressure"),
        D("**Atmospheric pressure** is the force that the weight of the air presses on a surface. It is also called air pressure.",
          title="Atmospheric pressure"),
        T("Air is a gas, but it has weight. The air above you is a tall column that presses down on the ground. "
          "At sea level the average pressure is about 1013 millibars (mb). Pressure becomes lower as you climb, "
          "because there is less air above you. This is why the air feels thin on the top of Mount Cameroon."),
        D("A **barometer** is the instrument used to measure atmospheric pressure. There are two common types: the mercury barometer "
          "and the aneroid barometer. Pressure is measured in millibars (mb) or hectopascals (hPa).", title="Measuring pressure"),
        T("On a weather map, lines called **isobars** join places that have the same pressure. Lines that are close together "
          "mean a big change in pressure over a short distance, and so a strong wind."),
        H("The planetary pressure belts"),
        D("A **pressure belt** is a wide band of high or low pressure that stretches around the Earth along lines of latitude.",
          title="Pressure belts"),
        T("There are four pressure belts in each half of the Earth. Two are low-pressure belts and two are high-pressure belts. "
          "Study the diagram. Notice that high and low belts follow each other: low, high, low, high."),
        IMG("f5g-clim-pressure-belts.svg", alt="A diagram of latitudes from 90 degrees north to 90 degrees south showing the equatorial low at the equator, subtropical highs at 30 degrees, subpolar lows at 60 degrees and polar highs at the poles, with arrows for the winds between them",
            caption="Figure 1. The pressure belts and the planetary winds. L = low pressure, H = high pressure."),
        KEY("The four pressure belts", "Learn them from the equator to the pole.", cards=[
            ["Equatorial low (about 0°)", "The sun is overhead, so the air is hot. It rises and pressure is low. This is also called the doldrums."],
            ["Subtropical highs (about 30°)", "Air that rose at the equator cools and sinks here. Sinking air makes high pressure and dry weather."],
            ["Subpolar lows (about 60°)", "Warm air from the south meets cold air from the pole. The lighter warm air is forced up, so pressure is low."],
            ["Polar highs (about 90°)", "The poles are very cold. Cold air is heavy, so it sinks and pressure is high."],
        ]),
        H("The planetary winds"),
        D("**Wind** is air that moves sideways. It blows from an area of high pressure to an area of low pressure. "
          "A bigger difference in pressure gives a stronger wind.", title="Wind"),
        T("The Earth also spins. Because of this spin, moving air is pushed to the right in the northern half of the Earth "
          "and to the left in the southern half. So winds do not blow straight north or south. They bend."),
        T("Winds are named by the direction they blow **from**. A north-east wind blows from the north-east towards the south-west."),
        KEY("The three planetary winds", "Each one blows from a high-pressure belt to a low-pressure belt.", cards=[
            ["Trade winds", "Blow from the subtropical highs to the equatorial low. North-east trades in the north, south-east trades in the south."],
            ["Westerlies", "Blow from the subtropical highs to the subpolar lows. South-westerly in the north, north-westerly in the south."],
            ["Polar easterlies", "Blow from the polar highs to the subpolar lows. Cold winds from the north-east in the north and from the south-east in the south."],
        ]),
        H("The ITCZ and West Africa"),
        D("The **ITCZ** (Inter-Tropical Convergence Zone) is the belt near the equator where the north-east and south-east trade winds meet. "
          "The air there is hot, so it rises and brings clouds and heavy rain.", title="ITCZ"),
        T("The ITCZ does not stay in one place. It follows the overhead sun, but a little later. It moves north in the northern summer "
          "and south in the northern winter. Over West Africa it lies near the Guinea coast in January and far to the north, "
          "near the southern edge of the Sahara, in July. The positions in the map are only approximate."),
        IMG("f5g-clim-itcz-west-africa.svg", alt="A simplified map of West Africa showing the ITCZ near 5 degrees north in January and near 20 degrees north in July, with the dry harmattan arrows from the north-east and the moist south-west monsoon arrows from the Atlantic Ocean",
            caption="Figure 2. How the shifting ITCZ gives West Africa two kinds of wind. Simplified sketch, not to scale."),
        T("When the ITCZ is in the south (about December to February), the dry north-east trade wind blows over the Sahara and then "
          "across West Africa. This wind is the **harmattan**. It is dry and dusty, the sky is hazy, the days are hot and the nights "
          "can be cool. The harmattan is strongest in the northern part of the region."),
        T("When the ITCZ moves north (about April to October), air from the Atlantic Ocean blows towards the land from the "
          "south-west. This is the **south-west monsoon**. The air is warm and moist, so it brings the rainy season."),
        TIP("In Paper 1, expect questions on the name of a belt or wind, or on where the ITCZ is in January and July. In Paper 2 Section B, "
            "a sketch of the pressure belts with wind arrows earns marks. In Section D (Cameroon), the harmattan and the monsoon explain the "
            "seasons of the north and the south.", title="Exam link"),
        EX("Model answer 1", intro="With the help of a diagram, describe the planetary pressure belts and the main planetary winds.", steps=[
            S("Introduction", text="Define atmospheric pressure and a pressure belt, then say there are four belts in each half of the Earth."),
            S("Draw", text="Draw a latitude strip from 90°N to 90°S. Mark the equatorial low (0°), the subtropical highs (30°), the subpolar lows (60°) and the polar highs (90°)."),
            S("Add the winds", text="Draw arrows from each high to the next low: the trade winds (to the equator), the westerlies (from 30° to 60°) and the polar easterlies (from the pole to 60°). Bend them to the right in the north and to the left in the south."),
            S("Name them", text="Label the north-east and south-east trades, the westerlies and the polar easterlies."),
            S("Explain", text="Say that wind blows from high to low pressure and is turned by the Earth's spin."),
        ]),
        EX("Model answer 2", intro="Explain how the position of the ITCZ affects the weather of West Africa.", steps=[
            S("Define", text="The ITCZ is the belt where the trade winds meet. The air rises and there is cloud and heavy rain."),
            S("It moves", text="It follows the overhead sun: north in the northern summer, south in the northern winter."),
            S("January", text="The ITCZ is near the Guinea coast. The north-east trade wind blows from the Sahara. This is the dry, dusty harmattan."),
            S("July", text="The ITCZ is far north. Moist south-west monsoon winds blow in from the Atlantic Ocean and bring the rainy season."),
            S("Example", text="Places near the coast such as Douala get a long wet season. The Far North has a short wet season and a long dry season with the harmattan."),
        ]),
        H("Common mistakes"),
        MISTAKE("Naming a wind by where it goes", "A westerly wind blows from the west. A north-east trade wind blows from the north-east towards the south-west."),
        MISTAKE("Mixing up pressure and temperature", "The equator is hot but has LOW pressure because warm air rises. The poles are cold but have HIGH pressure because cold air sinks."),
        MISTAKE("Saying the harmattan brings rain", "The harmattan comes from the Sahara and is dry. The south-west monsoon is the wet wind."),
        QUIZ("Which wind blows from the subtropical high to the equatorial low in the northern half of the Earth?",
             ["South-west monsoon", "North-east trade wind", "Westerly wind", "Polar easterly"], 1,
             "The trade winds blow from the subtropical highs to the equator. In the north they come from the north-east.",
             hint="It blows towards the equator.",
             feedback=["The south-west monsoon is a seasonal wind from the ocean. It is not one of the three planetary winds.", "",
                       "The westerlies blow from the subtropical highs to the subpolar lows, not to the equator.", "Polar easterlies blow away from the poles."]),
        QUIZ("In July the ITCZ is over the southern edge of the Sahara. What wind reaches the Guinea coast?",
             ["The dry harmattan", "The moist south-west monsoon", "The polar easterlies", "A land breeze"], 1,
             "When the ITCZ is far north, warm moist air from the Atlantic blows in from the south-west.",
             hint="Think about which direction the sea is from Douala.",
             feedback=["The harmattan blows when the ITCZ is in the south, in about December to February.", "",
                       "Polar easterlies never reach West Africa.", "A land breeze is a local night wind, not a seasonal wind."]),
        H("Practice questions"),
        PQ("Define atmospheric pressure and name the instrument used to measure it.",
           "Atmospheric pressure is the force that the weight of the air presses on a surface. It is measured with a barometer (mercury or aneroid), in millibars or hectopascals."),
        PQ("Name the four pressure belts of the Northern Hemisphere and give the approximate latitude of each.",
           "The equatorial low (about 0°), the subtropical high (about 30°N), the subpolar low (about 60°N) and the polar high (about 90°N)."),
        PQ("Why do winds blow from high pressure to low pressure, and why do they not blow in a straight line?",
           "Air moves from where the pressure is high to where it is low, so as to even out the difference. The spin of the Earth turns moving air to the right in the northern half and to the left in the southern half, so winds are bent."),
        PQ("Describe the harmattan and explain why it blows in the dry season.",
           "The harmattan is a dry, dusty north-east wind from the Sahara. It blows from about December to February because the ITCZ is then in the south, so the north-east trade wind blows over West Africa from the desert. It has no moisture, so there is no rain."),
        SUM("Atmospheric pressure is the weight of air pressing on a surface. It is measured with a barometer in millibars.",
            "There are four pressure belts: equatorial low, subtropical highs, subpolar lows and polar highs.",
            "Wind blows from high to low pressure and is bent by the Earth's spin.",
            "The planetary winds are the trade winds, the westerlies and the polar easterlies.",
            "The ITCZ moves with the sun. It brings the dry harmattan in the northern winter and the moist south-west monsoon in the northern summer."),
    ],
))

# ------------------------------------------------------------------ 2. Local winds
LESSONS.append(lesson(
    module=MODULE,
    topic=PW,
    title="Local winds: sea and land breezes, mountain and valley winds, monsoons",
    slug="clim-local-winds",
    minutes=22,
    summary="How land and sea breezes, anabatic and katabatic winds and monsoons form, with a labelled diagram for each, and how to tell a daily local wind from a seasonal one.",
    objectives=[
        "Define local winds, land and sea breezes, anabatic and katabatic winds, and monsoons",
        "Illustrate each local wind with a labelled diagram",
        "Describe how each local wind forms and when it blows",
        "Distinguish a daily local wind from a seasonal wind",
    ],
    key_concepts=["Local wind", "Sea breeze", "Land breeze", "Anabatic wind", "Katabatic wind", "Monsoon", "Differential heating"],
    blocks=[
        H("Introduction"),
        T("Visitors to Limbe or Kribi often notice that the afternoon feels cooler near the beach. A breeze arrives from the sea, "
          "and in the evening it fades. In the highlands around Bamenda, a farmer on a hill may feel the air move up the slope "
          "on a sunny afternoon and down it after dark."),
        T("These winds are small and local. They are different from the big planetary winds you studied in the last lesson. "
          "In this lesson you will learn how each one forms. The idea is always the same: **unequal heating**."),
        D("A **local wind** is a wind that blows over a small area and is caused by local differences in heating and pressure. "
          "Most local winds change between day and night.", title="Local winds"),
        H("Land and sea breezes"),
        T("Land heats up quickly in the sun and cools quickly at night. The sea heats up and cools slowly, because water "
          "takes in heat to a great depth and keeps it for longer. So during the day the land is warmer than the sea, and "
          "at night the land is cooler than the sea."),
        D("A **sea breeze** is a cool wind that blows from the sea to the land during the day.", title="Sea breeze"),
        D("A **land breeze** is a wind that blows from the land to the sea at night.", title="Land breeze"),
        IMG("f5g-clim-sea-land-breeze.svg", alt="Two cross-section diagrams. By day, air rises over warm land, low pressure forms, and a cool sea breeze blows from the sea to the land at the surface. By night, air rises over the warmer sea and a land breeze blows from the land to the sea",
            caption="Figure 1. A sea breeze by day (left) and a land breeze by night (right)."),
        KEY("How a sea breeze forms", "Follow the steps in the left-hand diagram.", cards=[
            ["1. The land heats", "The sun warms the land more than the sea."],
            ["2. Air rises over land", "Warm air rises, so pressure is low over the land."],
            ["3. Wind blows in", "Cooler air over the sea has higher pressure. It blows to the land as a sea breeze."],
            ["4. The air circulates", "The rising air spreads out high up, flows back over the sea and sinks. This completes a cell."],
        ]),
        T("At night everything is reversed. The land cools quickly and the sea stays warmer. Air rises over the sea, "
          "so pressure is lower there. Air flows from the land to the sea as a land breeze. The land breeze is usually weaker than the sea breeze."),
        H("Mountain and valley winds"),
        D("An **anabatic wind** is a wind that blows UP a mountain slope during the day. Warm air rises along the sunny slope.",
          title="Anabatic wind (valley wind)"),
        D("A **katabatic wind** is a wind that blows DOWN a mountain slope at night. Cold, heavy air flows down into the valley.",
          title="Katabatic wind (mountain wind)"),
        IMG("f5g-clim-mountain-valley-winds.svg", alt="Two diagrams of a mountain slope. By day the sun heats the slope and warm air flows up it (anabatic wind). At night the slope cools and cold air flows down into the valley (katabatic wind)",
            caption="Figure 2. The anabatic wind by day (left) and the katabatic wind by night (right)."),
        T("By day, the sun heats the mountain slope. The air touching the slope becomes warm and light, so it rises up the slope. "
          "This is the anabatic wind. It often brings clouds and afternoon showers to the upper slopes."),
        T("At night, the slope loses heat quickly. The air touching it becomes cold and heavy, so it sinks and flows down into the valley. "
          "This is the katabatic wind. Cold air collects on the valley floor, so valleys can be colder than the hillsides at night."),
        H("Monsoons"),
        D("A **monsoon** is a wind that changes direction with the season. It is caused by the different heating of a very large "
          "land area and the nearby ocean. The word comes from an Arabic word for 'season'.", title="Monsoon"),
        IMG("f5g-clim-monsoon.svg", alt="Two cross-section diagrams of land and ocean. In the summer the land is very hot, pressure is low over the land and a moist wind blows from the Atlantic to the land. In the winter the land is cooler, pressure is high and a dry wind blows from the land to the sea",
            caption="Figure 3. A monsoon in summer (left) and winter (right). The idea is the same as a sea breeze, but over a whole season."),
        T("In summer the land becomes much hotter than the ocean. Air rises over the land, pressure falls, and moist air is pulled in "
          "from the ocean. This wind brings heavy rain. In winter the land is cooler than the ocean. Pressure is high over the land and "
          "the wind blows out to sea. This wind is dry."),
        T("West Africa has a monsoon. The wet wind is the south-west monsoon and the dry wind is the harmattan. "
          "The monsoon of South Asia is even more famous: its summer rains are vital to farmers in India."),
        KEY("Breeze or monsoon?", "Both come from unequal heating of land and sea. They differ in size and timing.", cards=[
            ["Land and sea breezes", "Small area. Change every day and night."],
            ["Monsoons", "Very large area. Change with the seasons."],
        ]),
        TIP("In Paper 1, you may be given a diagram and asked to name the wind or say whether it is day or night. In Paper 2 Section B, "
            "a labelled sketch with arrows, plus a short explanation, gains most of the marks.", title="Exam link"),
        EX("Model answer 1", intro="With the help of a diagram, explain how a sea breeze forms.", steps=[
            S("Define", text="A sea breeze is a wind that blows from the sea to the land during the day."),
            S("Draw", text="Draw sea on the left and land on the right. Label low pressure (L) over the land and high pressure (H) over the sea."),
            S("Add arrows", text="Draw a surface arrow from sea to land (the sea breeze), a rising arrow over the land, an arrow aloft from land to sea, and a sinking arrow over the sea."),
            S("Explain", text="The land heats faster than the sea. Air over the land is warmed and rises, so pressure is low. Cooler air from the sea flows in to replace it."),
        ]),
        EX("Model answer 2", intro="Explain the difference between an anabatic wind and a katabatic wind.", steps=[
            S("Anabatic", text="It blows up a slope by day. The sun heats the slope, the air above it warms and rises."),
            S("Katabatic", text="It blows down a slope at night. The slope cools, the air above it becomes cold and heavy and sinks into the valley."),
            S("Difference", text="One goes up and one goes down. One happens in the day and the other at night. Warm air drives the first and cold air the second."),
        ]),
        EX("Model answer 3", intro="Explain why the monsoon is a seasonal wind and not a daily wind.", steps=[
            S("Size", text="A monsoon covers a huge area, such as the whole of South Asia or West Africa."),
            S("Why it changes", text="A large land mass and the ocean heat and cool by different amounts over the year, not only over a day."),
            S("Summer", text="Land is hot, pressure is low, moist air blows in from the ocean and brings rain."),
            S("Winter", text="Land is cooler, pressure is high, dry air blows out to sea."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the sea breeze blows at night", "A sea breeze blows by day, when the land is warmer. At night the land breeze blows."),
        MISTAKE("Naming the wind by where it goes", "A sea breeze comes FROM the sea. A land breeze comes FROM the land."),
        MISTAKE("Mixing up anabatic and katabatic", "Anabatic = up (A for 'ascend'). Katabatic = down (K for 'keeps going down')."),
        QUIZ("It is 3 pm in Limbe. A cool wind blows from the sea to the land. Which wind is it?",
             ["Land breeze", "Sea breeze", "Katabatic wind", "Harmattan"], 1,
             "In the afternoon the land is warmer than the sea. Cool air flows from the sea to the land: a sea breeze.",
             hint="Which is warmer in the afternoon, land or sea?",
             feedback=["A land breeze blows from the land to the sea at night.", "",
                       "A katabatic wind flows down a mountain slope at night.", "The harmattan is a dry seasonal wind from the Sahara."]),
        QUIZ("Which wind flows down a valley at night as cold air sinks off the slopes?",
             ["Anabatic wind", "Sea breeze", "Katabatic wind", "South-west monsoon"], 2,
             "Cold, dense air sinks down the slope at night. This is a katabatic wind.",
             hint="Think of cold air flowing downhill.",
             feedback=["An anabatic wind blows up the slope in the day.", "A sea breeze comes from the sea, not from the hills.", "",
                       "The monsoon is a seasonal wind and is not tied to one slope."]),
        H("Practice questions"),
        PQ("Define a local wind and give two examples.",
           "A local wind is a wind that blows over a small area because of local differences in heating and pressure. Examples: sea and land breezes, anabatic and katabatic winds."),
        PQ("Explain why a land breeze blows at night.",
           "At night the land cools faster than the sea. The air over the warmer sea rises and pressure is lower there. Air flows from the cooler land, where pressure is higher, to the sea. This is the land breeze."),
        PQ("Draw a simple diagram to show a katabatic wind and label it.",
           "Draw a slope going down into a valley. Add arrows along the slope pointing down. Label 'cold air sinks', 'katabatic wind' and 'night', and mark the valley floor where cold air collects."),
        PQ("State two differences between a sea breeze and a monsoon.",
           "A sea breeze blows over a small coastal area and changes between day and night. A monsoon blows over a very large area and changes with the season."),
        SUM("Local winds are caused by unequal heating and blow over small areas.",
            "A sea breeze blows from sea to land by day. A land breeze blows from land to sea at night.",
            "An anabatic wind blows up a slope by day. A katabatic wind blows down a slope at night.",
            "A monsoon is a seasonal wind caused by the heating of a large land mass and the nearby ocean. West Africa has the wet south-west monsoon and the dry harmattan.",
            "Always draw and label your diagram, and use L and H for low and high pressure."),
    ],
))


# ------------------------------------------------------------------ 3. Tropical humid and wet-and-dry climates
LESSONS.append(lesson(
    module=MODULE,
    topic=BC,
    title="The three climatic regions: tropical humid and tropical wet-and-dry",
    slug="clim-tropical-humid-and-wet-and-dry-climates",
    minutes=24,
    summary="Where the three tropical climatic regions lie on a world map, and the temperature, rainfall and seasons of the tropical humid and tropical wet-and-dry climates, with practice in reading climate graphs.",
    objectives=[
        "Locate the three climatic regions of the world on a map",
        "Identify the major characteristics of the tropical humid climate",
        "Identify the major characteristics of the tropical wet-and-dry climate",
        "Read temperature and rainfall from a climate graph and describe the pattern",
    ],
    key_concepts=["Climate", "Climatic region", "Tropical humid climate", "Tropical wet-and-dry climate", "Climate graph", "Wet season", "Dry season"],
    blocks=[
        H("Introduction"),
        T("Compare two towns in Cameroon. In Douala it rains in nearly every month, and the air is always warm and damp. "
          "In Garoua the rains fall for only a few months, and then the land is dry and dusty for the rest of the year. "
          "Both towns are hot, but their rainfall and seasons are very different."),
        T("Geographers group places with a similar climate into **climatic regions**. The syllabus asks you to know three regions "
          "found in the tropics. This lesson teaches the first two. The next lesson teaches the third."),
        D("**Climate** is the average weather of a place over a long time, usually 30 years or more.", title="Climate"),
        D("A **climatic region** is a large area of the world that has a similar climate.", title="Climatic region"),
        H("Where are the three regions?"),
        T("The three regions are tropical humid, tropical wet and dry, and tropical dry. They lie one after another as you move away "
          "from the equator, in both hemispheres. Look at the map."),
        IMG("f5g-clim-world-climate-regions.svg", alt="A simplified world map with bands of colour on the land: tropical humid near the equator, tropical wet and dry on both sides of it, and tropical dry near the tropics of Cancer and Capricorn, with Cameroon marked",
            caption="Figure 1. The three tropical climatic regions (simplified). Real boundaries are irregular."),
        KEY("Where to find them", "A good way to remember: humid at the equator, dry near the tropics, and wet-and-dry between the two.", cards=[
            ["Tropical humid", "Near the equator, up to about 10° north and south. Examples: the Congo Basin, the Amazon Basin and the islands of Southeast Asia."],
            ["Tropical wet and dry", "Between about 10° and 20° north and south of the equator, on the outer side of the humid region. Examples: the savanna of West Africa and East Africa, and northern Australia."],
            ["Tropical dry", "Near the tropics, from about 15° to 30° north and south. Examples: the Sahara, the Namib and Kalahari, Arabia and the Australian desert."],
        ]),
        T("Cameroon crosses two of the regions. The south has a tropical humid climate. The Adamawa plateau and the north have "
          "a tropical wet-and-dry climate. The far north, near Lake Chad, is drier, and it borders the dry Sahel. "
          "For exact boundaries, check your textbook."),
        H("The tropical humid climate"),
        D("The **tropical humid climate** is hot and wet in every month. It is found near the equator, where the sun is high all year.",
          title="Tropical humid climate"),
        T("**Temperature.** Every month is hot. The mean monthly temperature is about 24°C to 27°C. The temperature range through the "
          "year is small, usually less than 5°C. Days and nights are warm and the air feels sticky."),
        T("**Rainfall.** Rainfall is heavy, usually more than 1500 mm in a year, and it falls in every month. "
          "Most of it is convectional rain. The hot ground heats the air, which rises, cools, and makes tall clouds. "
          "Heavy afternoon showers and thunderstorms follow."),
        T("**Seasons.** There is no true dry season. Some places have two rainier periods, after the two times the sun is overhead "
          "(about March to May, and September to November). The periods between them are a little drier."),
        IMG("f5g-clim-graph-humid.svg", alt="A climate graph with bars for monthly rainfall and a line for temperature. Rainfall is above 30 millimetres in every month with peaks of 200 millimetres in May and 300 millimetres in October. Temperature stays between 23 and 26 degrees Celsius",
            caption="Figure 2. Station A, a tropical humid climate (a fictitious station, built to show the pattern)."),
        H("The tropical wet-and-dry climate"),
        D("The **tropical wet-and-dry climate** is hot all year and has a clear wet season and a clear dry season. It lies between the "
          "humid region and the deserts. It is also called the savanna climate.", title="Tropical wet-and-dry climate"),
        T("**Temperature.** It is hot all year. The mean monthly temperature is usually above 24°C. The range through the year is a little "
          "larger than in the humid climate, about 5°C to 10°C. The hottest months come just before the rains, when the sky is clear."),
        T("**Rainfall.** Total rainfall is lower than in the humid climate, about 750 mm to 1500 mm a year. It falls mainly in the wet season. "
          "The amount and the start of the rains can change from year to year."),
        T("**Seasons.** There are two seasons. The wet season comes when the ITCZ is overhead, in the high-sun months. "
          "The dry season comes when the ITCZ has moved away, and the dry harmattan can blow in West Africa. The nearer to the desert, "
          "the shorter the wet season."),
        IMG("f5g-clim-graph-wetdry.svg", alt="A climate graph with bars for monthly rainfall and a line for temperature. Rainfall is zero in January and December, rises to 270 millimetres in August and falls again. Temperature peaks at 30 degrees Celsius in March",
            caption="Figure 3. Station B, a tropical wet-and-dry climate (a fictitious station)."),
        CODE("""Feature          Tropical humid        Tropical wet and dry
Temperature      24-27 C all year      Above 24 C, hottest before rains
Annual range     Under 5 C             About 5-10 C
Rainfall         Over 1500 mm          About 750-1500 mm
Dry season       None                  Clear, several months
Wet season       All year (peaks)      One main wet season""", "text", title="Summary table (typical values)"),
        H("Reading a climate graph"),
        D("A **climate graph** shows the average monthly rainfall as bars and the average monthly temperature as a line, for one place "
          "over the year.", title="Climate graph"),
        T("Follow these steps. First read the left scale for rainfall and the right scale for temperature. Then look at the shape: "
          "are the bars high in every month, or only in some? Is the temperature line flat or does it curve?"),
        TIP("Every climate graph question can be answered in three parts: temperature (highest, lowest, range), rainfall (total, wettest and driest months) "
            "and seasons (when it is wet and dry). Always quote numbers with their units. The climates also appear in Paper 1 multiple-choice "
            "questions, and in Paper 2 Section B and Section D (the climates of Cameroon).", title="Exam link"),
        EX("Model answer 1", intro="Describe the climate shown by the graph for Station A (Figure 2).", steps=[
            S("Temperature", text="It is hot all year. The highest monthly temperature is 26°C and the lowest is 23°C. The range is only 3°C."),
            S("Rainfall", text="Rainfall is heavy. The total is 1620 mm. Every month has at least 30 mm. The wettest month is October with 300 mm."),
            S("Seasons", text="There is no dry season. There are two rainier periods, with peaks in May (200 mm) and October (300 mm)."),
            S("Conclusion", text="This is a tropical humid climate."),
        ]),
        EX("Model answer 2", intro="Describe the climate shown by the graph for Station B (Figure 3).", steps=[
            S("Temperature", text="It is hot all year. The highest monthly temperature is 30°C in March and the lowest is 24°C in July and August. The range is 6°C."),
            S("Rainfall", text="The total is 1225 mm. The wettest month is August with 270 mm. Rainfall is 0 mm in January and December."),
            S("Seasons", text="There is a wet season from May to September, when each month has more than 100 mm, and a long dry season from November to February."),
            S("Conclusion", text="This is a tropical wet-and-dry climate."),
        ]),
        EX("Model answer 3", intro="Locate the tropical humid and the tropical wet-and-dry regions on a world map.", steps=[
            S("Draw", text="Draw an outline of the world with the equator and the two tropics."),
            S("Humid", text="Shade the area close to the equator, up to about 10° north and south. Name the Congo Basin and the Amazon Basin."),
            S("Wet and dry", text="Shade the areas on either side of the humid region, between about 10° and 20°. Name the savanna of West Africa."),
            S("Key", text="Add a key. Say that the real boundaries are irregular."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the tropical humid climate is cool", "All the tropical climates are hot. The humid climate has a mean monthly temperature of about 24°C to 27°C."),
        MISTAKE("Forgetting the units", "Write 26°C and 300 mm, not just 26 and 300."),
        MISTAKE("Mixing the two scales", "The bars use the rainfall scale in mm. The line uses the temperature scale in °C. Check which axis you are reading."),
        QUIZ("Which climate has a clear dry season and a clear wet season?",
             ["Tropical humid", "Tropical wet and dry", "Tropical dry", "Cold polar"], 1,
             "The wet-and-dry climate has a wet season when the ITCZ is overhead and a dry season when it moves away.",
             hint="The name tells you the answer.",
             feedback=["The humid climate is wet in every month.", "", "The dry climate has very little rain in any month.", "Polar climates are not tropical and are not studied in this lesson."]),
        QUIZ("A station has a temperature range of 3°C and rain in every month, with a total of over 1500 mm. Which climate is it?",
             ["Tropical wet and dry", "Tropical dry", "Tropical humid", "Mediterranean"], 2,
             "A small range, heavy rain all year and no dry season are the marks of the tropical humid climate.",
             hint="Which climate has no dry season?",
             feedback=["The wet-and-dry climate has a long dry season.", "The dry climate has under 250 mm a year.", "", "A Mediterranean climate has wet winters and dry summers and is not a tropical climate."]),
        H("Practice questions"),
        PQ("Name the three tropical climatic regions of the world.",
           "Tropical humid, tropical wet and dry, and tropical dry."),
        PQ("State three characteristics of the tropical humid climate.",
           "It is hot all year (about 24°C to 27°C) with a small annual range under 5°C; it has heavy rainfall, usually over 1500 mm, in every month; there is no dry season."),
        PQ("Describe the seasons of the tropical wet-and-dry climate.",
           "There is a wet season in the high-sun months, when the ITCZ is overhead, and a clear dry season when it moves away. The dry season can last several months. Total rainfall is about 750 mm to 1500 mm."),
        PQ("Station B (Figure 3) has monthly temperatures of 26, 28, 30, 29, 27, 25, 24, 24, 25, 26, 26 and 25°C. Calculate its mean annual temperature and its temperature range.",
           "Total = 315. Mean = 315 divided by 12 = 26.25°C (about 26.3°C). Range = 30 - 24 = 6°C."),
        SUM("The three tropical climatic regions are humid (near the equator), wet and dry (on either side) and dry (near the tropics).",
            "The tropical humid climate is hot all year, with a small range and heavy rain in every month. It has no dry season.",
            "The tropical wet-and-dry climate is hot all year, with a wet season and a long dry season and less rain than the humid climate.",
            "Describe a climate graph in three parts: temperature, rainfall and seasons. Quote numbers with units.",
            "Cameroon has a humid climate in the south and a wet-and-dry climate in the north."),
    ],
))


# ------------------------------------------------------------------ 4. Tropical dry climate and climate graphs
LESSONS.append(lesson(
    module=MODULE,
    topic=BC,
    title="The tropical dry climate and describing climate graphs",
    slug="clim-tropical-dry-climate-and-climate-graphs",
    minutes=24,
    summary="The temperature, rainfall and seasons of the tropical dry (desert) climate, a comparison of all three tropical climates, and how to calculate and describe the mean, range, total and seasons from a climate graph.",
    objectives=[
        "Identify the major characteristics of the tropical dry climate and locate it on the map",
        "Compare the tropical humid, wet-and-dry and dry climates",
        "Calculate the mean temperature, the range and the annual rainfall from climate data",
        "Describe a climate graph, naming the wet and dry seasons",
    ],
    key_concepts=["Tropical dry climate", "Desert", "Mean temperature", "Temperature range", "Annual rainfall", "Wet season", "Dry season"],
    blocks=[
        H("Introduction"),
        T("Travel north from Maroua towards Lake Chad and the land becomes drier. The trees get smaller, the grass thins, and in some "
          "years the rains hardly come. Go further north, into the Sahara, and the land becomes desert: sand and rock, with almost no rain."),
        T("This is the **tropical dry climate**. It is the third tropical climate in the syllabus. In this lesson you will learn its features, "
          "compare the three climates, and practise calculating and describing the figures on a climate graph."),
        H("The tropical dry climate"),
        D("The **tropical dry climate** (desert climate) has very little rainfall, very hot days, and a large range of temperature. "
          "It is found near the tropics of Cancer and Capricorn, mostly on the western sides and in the middle of the continents.",
          title="Tropical dry climate"),
        T("**Where.** The Sahara, Arabia, the Namib and Kalahari, the Atacama and the Australian desert are in this region. "
          "Look again at the world map of the last lesson: the dry climate is the brown band near the two tropics."),
        T("**Why it is dry.** Near 30° north and south the air in the subtropical high-pressure belt is sinking. "
          "Sinking air warms and dries, so clouds do not form. There are few clouds and little rain."),
        T("**Rainfall.** The total is usually less than 250 mm in a year. The rain is very unreliable. Some years have none, "
          "and then a single storm may bring more rain than the whole of an average year."),
        T("**Temperature.** The days are very hot, often above 40°C in the hottest months. The sky is clear, so the ground gains a lot "
          "of heat by day and loses it quickly at night. Nights can be cold. The daily range is large. The annual range is also large, "
          "often 15°C to 20°C or more."),
        T("**Seasons.** There is no real wet season. There is a hot season and a cooler season."),
        IMG("f5g-clim-graph-dry.svg", alt="A climate graph with almost invisible rainfall bars of 0 to 3 millimetres a month and a temperature line rising from 15 degrees Celsius in January to 35 degrees Celsius in July and falling again",
            caption="Figure 1. Station C, a tropical dry climate (a fictitious station). Notice how small the rainfall bars are."),
        H("Comparing the three tropical climates"),
        CODE("""Feature          Humid           Wet and dry         Dry
Temperature      24-27 C         Over 24 C           Very hot, cool nights
Annual range     Under 5 C       About 5-10 C        15-20 C or more
Annual rainfall  Over 1500 mm    About 750-1500 mm   Under 250 mm
Seasons          No dry season   Wet and dry         No wet season
Where            Equator         Either side         Near the tropics""", "text", title="Comparing the three climates (typical values)"),
        T("The main differences are rainfall and seasons. All three are hot. The range of temperature becomes larger as the "
          "rainfall becomes smaller, because clouds and moist air keep temperatures steady."),
        H("Calculating from climate data"),
        D("The **mean** (average) is found by adding all the values and dividing by the number of values. For a mean annual temperature, "
          "add the 12 monthly temperatures and divide by 12.", title="Mean", formula=r"\text{mean} = \dfrac{\text{sum of values}}{\text{number of values}}"),
        D("The **range** is the highest value minus the lowest value. The **annual rainfall** is the sum of the 12 monthly totals.",
          title="Range and total", formula=r"\text{range} = \text{highest} - \text{lowest}"),
        TIP("Check your arithmetic by estimating. If all twelve temperatures lie between 23°C and 26°C, the mean must also lie between 23°C and 26°C.", title="Check"),
        EX("Worked example 1: Station C", intro="The monthly temperatures of Station C (Figure 1) are 15, 17, 21, 26, 31, 34, 35, 34, 32, 27, 21 and 16°C. Calculate the mean and the range.", steps=[
            S("Add", math=r"15+17+21+26+31+34+35+34+32+27+21+16 = 309"),
            S("Mean", math=r"309 \div 12 = 25.75", text="The mean annual temperature is about 25.8°C."),
            S("Range", math=r"35 - 15 = 20", text="The highest is 35°C (July) and the lowest is 15°C (January). The range is 20°C."),
        ]),
        EX("Worked example 2: describing a graph", intro="Describe the climate shown by Station C (Figure 1).", steps=[
            S("Temperature", text="It is very hot in summer: the highest is 35°C in July. January is the coolest month at 15°C. The range is large, 20°C."),
            S("Rainfall", text="Rainfall is tiny. The annual total is only 19 mm. No month has more than 3 mm."),
            S("Seasons", text="There is no wet season. There is a hot season from May to September and a cooler season from November to February."),
            S("Conclusion", text="This is a tropical dry (desert) climate."),
        ]),
        EX("Worked example 3: which climate?", intro="Station X has a temperature range of 7°C. Its rainfall is 0 mm in four months, 230 mm in August and 980 mm for the year. Which climate is it?", steps=[
            S("Temperature", text="A range of 7°C is within the wet-and-dry band of about 5°C to 10°C. It is not under 5°C (humid) and not 15°C or more (dry)."),
            S("Rainfall", text="980 mm is between 750 mm and 1500 mm. Four months have no rain, so there is a dry season."),
            S("Conclusion", text="Station X has a tropical wet-and-dry climate."),
        ]),
        TIP("Climate-graph questions appear in Paper 1 and in Paper 2 Section B. In Section D you may be asked to describe the climates "
            "of Cameroon. Use the pattern: temperature (with highest, lowest and range), rainfall (with total and months), seasons (wet and dry months).",
            title="Exam link"),
        H("Common mistakes"),
        MISTAKE("Calling the dry climate cold", "The days are very hot. The nights can be cold, but the mean is still high."),
        MISTAKE("Dividing by the wrong number", "A mean annual temperature uses 12 months, so divide by 12."),
        MISTAKE("Mixing up range and mean", "The range is highest minus lowest. The mean is the average of all the values."),
        QUIZ("Which feature best identifies the tropical dry climate?",
             ["Rainfall of over 1500 mm", "Rainfall of under 250 mm and a large temperature range", "Rain in every month", "A temperature range of 3°C"], 1,
             "Very low rainfall and a large temperature range are the marks of the desert climate.",
             hint="Think of the Sahara.",
             feedback=["This belongs to the tropical humid climate.", "", "A desert has very few rainy months.", "A very small range belongs to the humid climate."]),
        QUIZ("The highest monthly temperature of a station is 31°C and the lowest is 24°C. What is the range?",
             ["7°C", "55°C", "27.5°C", "24°C"], 0,
             "Range = highest minus lowest = 31 - 24 = 7°C.",
             hint="Subtract.",
             feedback=["", "55 is the sum of the two values. The range uses subtraction.", "27.5 is the mean of the two values, not the range.", "24 is the lowest value, not the range."]),
        H("Practice questions"),
        PQ("State four characteristics of the tropical dry climate.",
           "Very little rain (under about 250 mm a year); very hot days; a large temperature range; cloudless skies and unreliable rainfall. It lies near the tropics, for example in the Sahara."),
        PQ("Explain why the Sahara has so little rain.",
           "It lies near 30°N, under the subtropical high-pressure belt. The air there sinks, so it warms and dries. Clouds do not form and rain rarely falls."),
        PQ("The monthly rainfall of Station C is 3, 2, 1, 0, 1, 0, 2, 3, 1, 1, 2 and 3 mm. Calculate the annual rainfall.",
           "3+2+1+0+1+0+2+3+1+1+2+3 = 19 mm."),
        PQ("Give three differences between the tropical humid climate and the tropical dry climate.",
           "Humid: over 1500 mm of rain, small temperature range (under 5°C), no dry season. Dry: under 250 mm of rain, large temperature range (15°C to 20°C or more), no wet season."),
        SUM("The tropical dry climate has very little, unreliable rain (under about 250 mm), very hot days and a large range.",
            "It lies near the tropics, where air in the subtropical highs is sinking.",
            "All three tropical climates are hot. They differ in rainfall, seasons and temperature range.",
            "Mean = sum divided by the number of values. Range = highest minus lowest. Annual rainfall = the sum of the monthly values.",
            "When you describe a graph, give temperature, rainfall and seasons, with figures and units."),
    ],
))


# ------------------------------------------------------------------ 5. Factors influencing weather and climate
LESSONS.append(lesson(
    module=MODULE,
    topic=BC,
    title="Factors that influence weather and climate",
    slug="clim-factors-influencing-weather-and-climate",
    minutes=26,
    summary="How latitude, altitude, relief, ocean currents, water bodies, continentality, cloud cover, air masses and human activities change the weather and climate of a place, with examples from Mount Cameroon, Lake Chad and the Guinea coast.",
    objectives=[
        "Illustrate how altitude, relief and continentality affect temperature and rainfall",
        "Describe the effect of latitude, ocean currents, water bodies and cloud cover on climate",
        "Describe how air masses and human activities influence weather and climate",
        "Use examples from Cameroon to explain why places at the same latitude can have different climates",
    ],
    key_concepts=["Latitude", "Altitude", "Relief", "Ocean current", "Water body", "Cloud cover", "Continentality", "Air mass", "Human activities"],
    blocks=[
        H("Introduction"),
        T("Douala and Bamenda are both in Cameroon, only a few hundred kilometres apart. Yet in Douala the days are hot and sticky, while "
          "in Bamenda the evenings can feel cool. Mount Cameroon rises beside the sea, and its summit can be much colder than the beach at its foot."),
        T("Why do places so close together have such different weather? The answer is a group of **factors** that shape climate. "
          "The syllabus names nine of them. We study them in this lesson, with examples from Cameroon."),
        KEY("The nine factors", "Learn the list first. Each one is explained below.", cards=[
            ["Latitude", "How far north or south of the equator a place is."],
            ["Altitude", "How high a place is above sea level."],
            ["Relief", "The shape of the land: mountains, slopes and valleys."],
            ["Ocean currents", "Warm or cold streams of water in the oceans."],
            ["Water bodies", "Seas, lakes and large rivers near a place."],
            ["Continentality", "Distance from the sea."],
            ["Cloud cover", "How much of the sky is covered by cloud."],
            ["Air masses", "Large bodies of air that move across the land."],
            ["Human activities", "What people do to the land and the air."],
        ]),
        H("Latitude"),
        T("Near the equator the sun is high in the sky all year. Its rays strike the ground almost straight down, so heat is "
          "concentrated on a small area. Far from the equator the rays strike at a low angle, so the same heat is spread over a bigger "
          "area and each place is cooler. So temperatures fall from the equator towards the poles."),
        T("Latitude also affects rainfall, because it decides where the ITCZ and the pressure belts lie. "
          "This is why Cameroon is humid in the south and drier in the north."),
        H("Altitude"),
        D("**Altitude** is the height of a place above sea level.", title="Altitude"),
        T("Temperature falls as you go up. On average it falls by about 6.5°C for every 1000 m. The air is thinner on high ground "
          "and holds less heat, and the ground is further from the warm surface below."),
        IMG("f5g-clim-altitude-relief.svg", alt="Cross-section of a 3000 metre mountain beside the ocean with typical temperatures of 27 degrees at sea level, 20.5 at 1000 metres, 14 at 2000 metres and 7.5 at 3000 metres, with a wet windward slope and a drier leeward slope",
            caption="Figure 1. Altitude and relief on a mountain near the coast (illustrative, not to scale)."),
        T("**Example: Mount Cameroon.** The mountain is the highest in the country and stands right beside the coast. "
          "The foot of the mountain is hot. The upper slopes are much cooler, and the summit area is cold. In the same way, Bamenda, "
          "which stands on the Western Highlands more than 1000 m above sea level, is cooler than Douala."),
        H("Relief"),
        D("**Relief** is the shape and height of the land. Mountains force air to rise and change where rain falls.", title="Relief"),
        T("Moist air from the sea meets a mountain. It is forced to rise up the windward slope. As it rises it cools, "
          "its water vapour condenses, and heavy rain falls. After crossing the top, the air sinks down the leeward slope. "
          "It warms and dries, so rainfall is low. This dry side is called a **rain shadow**."),
        T("**Example: the Guinea coast.** The slopes of Mount Cameroon that face the Atlantic receive very heavy rain from the "
          "south-west monsoon. The coast near the mountain is one of the wettest parts of Africa (check your textbook for the figures)."),
        H("Ocean currents and water bodies"),
        D("An **ocean current** is a large stream of water that moves through the ocean in a regular path. It may be warm or cold.", title="Ocean current"),
        T("A warm current warms the air above it and brings moist air, so it makes the coast it passes warmer and wetter. "
          "A cold current cools the air and makes it stable, so there is little rain and often fog. The cold Benguela Current "
          "flows along the south-west coast of Africa and helps to make the Namib Desert dry. The warm Guinea Current flows along the "
          "Gulf of Guinea coast and helps to keep it warm and moist."),
        T("Water bodies such as seas and big lakes have a cooling effect in hot weather and a warming effect in cool weather, "
          "because water heats and cools slowly. They also give moisture to the air. **Example: Lake Chad.** The lake adds some moisture "
          "and a little cooling to the dry Sahelian region around it. In recent decades the lake has shrunk a lot, because of low rainfall "
          "and heavy use of its water. As it shrinks, this local effect weakens."),
        H("Continentality"),
        D("**Continentality** is the effect of distance from the sea. Places far from the sea have a continental climate.", title="Continentality"),
        T("Near the sea, temperatures change little, because the sea warms and cools slowly. This is called a maritime climate. "
          "Far inland, temperatures change more, and rainfall is usually lower, because the winds have lost their moisture on the way. "
          "The Far North of Cameroon is a long way from the Atlantic, so it has a bigger temperature range and less rain than Douala."),
        IMG("f5g-clim-continentality.svg", alt="A graph of monthly temperature for two fictitious stations. The coastal station has a range of 3 degrees Celsius and the inland station has a range of 11 degrees Celsius",
            caption="Figure 2. Coastal and inland stations at the same latitude (fictitious data). The inland range is much bigger."),
        H("Cloud cover"),
        T("Clouds act like a blanket. By day they reflect sunlight, so cloudy days are cooler. At night they trap heat, so cloudy nights are warmer. "
          "Under a clear sky, days are hotter and nights are colder. This is why deserts, which have few clouds, have a big daily range of temperature."),
        H("Air masses"),
        D("An **air mass** is a very large body of air that has the same temperature and humidity throughout. It takes its features from the "
          "region where it formed.", title="Air mass"),
        T("Two air masses affect West Africa. A hot, dry air mass forms over the Sahara and blows as the harmattan. "
          "A warm, moist air mass forms over the Atlantic and arrives with the south-west monsoon. The weather depends on which one is over you."),
        H("Human activities"),
        T("People can change climate, mostly in small ways. Cutting forests removes trees that give moisture to the air, so local "
          "rainfall may fall and the ground becomes hotter. Towns are warmer than the countryside, because concrete and tarmac store heat. "
          "Burning fuels and forests adds greenhouse gases, which strengthens the greenhouse effect. In dry regions, big irrigation schemes can "
          "reduce the water in lakes and rivers."),
        TIP("In Paper 1, expect a question on one factor and an example. In Paper 2 Section B, explain two or three factors with named places. "
            "In Section D, use Mount Cameroon, Bamenda, Lake Chad and the Guinea coast as your examples.", title="Exam link"),
        EX("Worked example: calculating temperature with height", intro="The temperature at the foot of a mountain at sea level is 27°C. Use a fall of 6.5°C for every 1000 m. Find the temperature at 2000 m.", steps=[
            S("Find the fall", math=r"\dfrac{2000}{1000} \times 6.5 = 13", text="The temperature falls by 13°C."),
            S("Subtract", math=r"27 - 13 = 14", text="The temperature at 2000 m is about 14°C."),
        ], check=r"1000\text{ m: } 27 - 6.5 = 20.5; \quad 2000\text{ m: } 20.5 - 6.5 = 14"),
        EX("Model answer 1", intro="Explain why Bamenda is cooler than Douala.", steps=[
            S("Point", text="Bamenda is much higher above sea level than Douala."),
            S("Evidence", text="Bamenda lies on the Western Highlands at more than 1000 m. Douala is on the coast, near sea level."),
            S("Explanation", text="Temperature falls by about 6.5°C for every 1000 m. So Bamenda is several degrees cooler than Douala."),
        ]),
        EX("Model answer 2", intro="Explain how relief affects the rainfall of the coast near Mount Cameroon.", steps=[
            S("Point", text="The mountain forces the moist monsoon air to rise."),
            S("Explanation", text="The air blows in from the Atlantic, rises up the windward slope, cools, condenses and gives heavy rain."),
            S("Contrast", text="After crossing the top the air sinks, warms and dries, so the leeward side is drier. This is the rain shadow."),
        ]),
        H("Common mistakes"),
        MISTAKE("Mixing up altitude and latitude", "Altitude is height above the sea. Latitude is distance north or south of the equator."),
        MISTAKE("Saying temperature rises with height", "Temperature falls with height, by about 6.5°C for every 1000 m."),
        MISTAKE("Listing factors without examples", "Name a place for each factor, for example Mount Cameroon for altitude and relief, and Lake Chad for a water body."),
        QUIZ("Which factor best explains why the summit of Mount Cameroon is colder than the coast at its foot?",
             ["Latitude", "Altitude", "Continentality", "Cloud cover only"], 1,
             "The summit is much higher than the coast. Temperature falls as height increases.",
             hint="Which factor is about height?",
             feedback=["The summit and the foot of the mountain are at almost the same latitude.", "",
                       "Both places are close to the sea, so continentality is not the reason.", "Cloud can lower the temperature a little, but height is the main cause."]),
        QUIZ("Which factor explains why the Far North of Cameroon has a larger annual temperature range than Douala?",
             ["It is near the sea", "It is far from the sea", "It is on a warm current", "It is covered in forest"], 1,
             "Places far from the sea heat up and cool down more, so the range is larger. This is continentality.",
             hint="Think about the sea's effect on temperature.",
             feedback=["Nearness to the sea reduces the range, as at Douala.", "", "A warm current affects coasts, not inland places.", "Forest keeps temperatures more even, so it would reduce the range."]),
        H("Practice questions"),
        PQ("Name five factors that influence the climate of a place.",
           "Any five of: latitude, altitude, relief, ocean currents, water bodies, cloud cover, continentality, air masses and human activities."),
        PQ("The temperature at sea level is 28°C. Calculate the temperature at 1500 m, using a fall of 6.5°C per 1000 m.",
           "Fall = 1.5 x 6.5 = 9.75°C. Temperature = 28 - 9.75 = 18.25°C, about 18°C."),
        PQ("Explain the effect of a cold ocean current on the climate of a coast.",
           "The cold current cools the air above it. The air becomes stable and holds little moisture, so there is little rain and often fog. The coast may be a desert, as the Namib coast is next to the cold Benguela Current."),
        PQ("Describe two ways in which human activities can change the climate.",
           "Cutting forests reduces moisture and can lower local rainfall and raise ground temperature. Burning fuels and forests adds greenhouse gases and raises temperatures. Towns are warmer than the countryside because of tarmac and concrete."),
        SUM("Nine factors influence weather and climate: latitude, altitude, relief, ocean currents, water bodies, cloud cover, continentality, air masses and human activities.",
            "Temperature falls with latitude (away from the equator) and with altitude, at about 6.5°C for every 1000 m.",
            "Relief gives heavy rain on windward slopes and a rain shadow on the leeward side.",
            "The sea reduces temperature range. Far inland the range is larger and rain is less.",
            "Use named places: Mount Cameroon, Bamenda, Lake Chad, the Guinea coast and Douala."),
    ],
))


# ------------------------------------------------------------------ 6. Global warming
LESSONS.append(lesson(
    module=MODULE,
    topic=EH,
    title="Global warming as an environmental hazard",
    slug="clim-global-warming",
    minutes=24,
    summary="What the greenhouse effect and global warming are, where their effects are felt, their causes and their positive and negative effects, and the adaptation, mitigation and conservation measures that respond to them.",
    objectives=[
        "Define global warming and the greenhouse effect, and illustrate the greenhouse effect",
        "Identify the areas where the effects of global warming are found",
        "Outline the causes and the positive and negative effects of global warming",
        "Outline adaptation, mitigation and conservation measures",
    ],
    key_concepts=["Greenhouse effect", "Greenhouse gases", "Global warming", "Fossil fuels", "Deforestation", "Adaptation", "Mitigation", "Conservation"],
    blocks=[
        H("Introduction"),
        T("Farmers in the Far North say that the rains come later and stop earlier than in their grandparents' time. Fishers around Limbe "
          "and Douala worry about higher seas. Many scientists link changes like these to **global warming**. "
          "In this lesson we look at global warming as an environmental hazard. For each hazard in the syllabus you will "
          "define it, say where it occurs, give its causes and effects, and outline how people respond."),
        H("Definitions"),
        D("The **greenhouse effect** is a natural process. Some gases in the air let sunlight pass through to the ground, but trap part of the heat "
          "that the ground sends back. This keeps the Earth warm enough for life.", title="Greenhouse effect"),
        D("**Global warming** is the rise in the average temperature of the Earth's surface and lower atmosphere over a long period. "
          "Most scientists agree that it is mainly caused by human activities that add extra greenhouse gases to the air.", title="Global warming"),
        IMG("f5g-clim-greenhouse-effect.svg", alt="Diagram of the greenhouse effect: sunlight passes through the atmosphere to the Earth's surface, the surface sends out heat, greenhouse gases send some heat back to the surface, and some heat escapes to space",
            caption="Figure 1. The greenhouse effect. More greenhouse gases send more heat back to the surface."),
        T("The main **greenhouse gases** are carbon dioxide, methane, nitrous oxide and water vapour. The greenhouse effect is not bad in itself. "
          "Without it the Earth would be far too cold. The problem is that human activities are adding more gases. This is sometimes called "
          "the enhanced greenhouse effect."),
        H("Where does it occur?"),
        T("Global warming is a world-wide hazard. The extra greenhouse gases spread through the whole atmosphere. But its effects are not the same everywhere. "
          "The places most at risk include the polar regions, where ice is melting, low-lying coasts and small islands, which face rising seas, and "
          "dry regions such as the Sahel, where droughts may become more severe."),
        T("In Cameroon, the Lake Chad basin and the Far North are at risk from heat and drought. The low coast near Douala and Limbe is at risk from "
          "rising seas and heavier storms. Africa has added very little of the world's greenhouse gases, but it is one of the regions most "
          "exposed to the effects."),
        H("Causes"),
        KEY("Human causes of global warming", "Most of them add carbon dioxide or methane to the air.", cards=[
            ["Burning fossil fuels", "Coal, oil and gas are burned in power stations, factories, cars and trucks. This releases carbon dioxide."],
            ["Deforestation", "Trees take in carbon dioxide. When forests are cut and burned, this store is lost and more carbon dioxide goes into the air."],
            ["Farming", "Cattle and rice fields release methane. Fertilisers release nitrous oxide. Bush burning adds carbon dioxide."],
            ["Waste", "Rubbish dumps and landfills produce methane as the waste rots."],
        ]),
        T("Natural causes also exist, such as volcanic eruptions and changes in the sun's energy. But the fast rise in temperature "
          "since the 1800s is mainly linked to human activities."),
        H("Effects"),
        IMG("f5g-clim-warming-chain.svg", alt="A diagram linking causes (burning fossil fuels, cutting forests, farming) to more greenhouse gases and a stronger greenhouse effect, and then to effects (hotter climate, melting ice and rising seas, changing rainfall), with mitigation and adaptation as responses",
            caption="Figure 2. From causes to effects, and the two kinds of response."),
        T("**Negative effects.** Temperatures rise and heat waves become more common. Ice melts and the sea expands as it warms, so the sea level rises and "
          "low coasts flood. Rainfall patterns change, with more floods in some places and more droughts in others. Crops and fish stocks may suffer, "
          "which can lead to hunger. Coral reefs, forests and many wild species are put under stress. Some diseases may spread to new areas."),
        T("**Positive effects.** These are fewer, and they occur mainly in cold regions. In very cold lands the growing season may become longer. "
          "Melting Arctic ice may open new shipping routes. Warmer winters reduce the cost of heating. But experts agree that the negative effects "
          "are greater, especially for poor countries."),
        H("Responses: adaptation, mitigation and conservation"),
        D("**Mitigation** means reducing the causes of global warming, by cutting the greenhouse gases that go into the air.", title="Mitigation"),
        D("**Adaptation** means changing the way we live so as to cope with the effects of warming that cannot be avoided.", title="Adaptation"),
        D("**Conservation** means protecting and using natural resources wisely, such as forests and mangroves, which store carbon and shield the coast.", title="Conservation"),
        KEY("Examples of each response", "Notice that mitigation tackles the cause, and adaptation tackles the effect.", cards=[
            ["Mitigation", "Use solar, hydro and wind power instead of fossil fuels; save energy; use cleaner stoves and cars; plant trees; reduce waste. Countries sign agreements, such as the Paris Agreement of 2015, to cut emissions."],
            ["Adaptation", "Grow drought-resistant crops and change planting dates; harvest rainwater; build sea walls and drainage; set up early warning for floods and storms; move settlements away from the most exposed coasts."],
            ["Conservation", "Protect forests, including the rainforest of southern and eastern Cameroon; protect mangroves on the coast; plant trees on bare land."],
        ]),
        TIP("This topic is in Paper 1 (definitions, causes and effects) and in Paper 2 Section B and Section D (Cameroon). Keep the claims general and "
            "qualitative. Do not quote exact temperatures or dates unless you are sure of them.", title="Exam link"),
        EX("Model answer 1", intro="Explain the greenhouse effect with the help of a diagram.", steps=[
            S("Define", text="The greenhouse effect is a natural process in which gases in the air trap some of the heat that leaves the Earth."),
            S("Draw", text="Draw the sun, the atmosphere with greenhouse gases and the Earth's surface. Add arrows for sunlight coming down, heat going up, some heat sent back down, and some heat escaping to space."),
            S("Explain", text="Sunlight passes through the air and warms the surface. The surface sends out heat. Greenhouse gases absorb some of it and send it back, which keeps the Earth warm."),
            S("Link", text="More gases means more heat sent back, so the surface warms. This is global warming."),
        ]),
        EX("Model answer 2", intro="Outline the causes and the effects of global warming.", steps=[
            S("Define", text="Global warming is the rise in the average temperature of the Earth's surface and lower atmosphere."),
            S("Causes", text="Burning fossil fuels, cutting forests, farming (cattle, rice, fertilisers) and rubbish dumps add greenhouse gases."),
            S("Negative effects", text="Heat waves, melting ice and rising seas that flood coasts, changing rainfall with floods and droughts, and lower crop and fish yields."),
            S("Positive effects", text="Longer growing seasons in cold lands and new Arctic shipping routes. These are fewer and local."),
            S("Conclusion", text="The negative effects are greater, especially for poor and low-lying countries."),
        ]),
        EX("Model answer 3", intro="Distinguish between adaptation and mitigation, with an example of each from Cameroon.", steps=[
            S("Mitigation", text="Mitigation reduces the causes. Example: using hydroelectric power instead of burning wood or oil, and protecting forests."),
            S("Adaptation", text="Adaptation reduces the harm from the effects. Example: farmers in the Far North planting drought-resistant crops, or building drains to cope with floods in a coastal town."),
            S("Difference", text="Mitigation acts on the cause. Adaptation acts on the effect."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying the greenhouse effect is always harmful", "The natural greenhouse effect keeps the Earth warm. The hazard is the extra warming from more gases."),
        MISTAKE("Mixing up adaptation and mitigation", "Mitigation = reduce the cause (fewer gases). Adaptation = cope with the effect (sea walls, new crops)."),
        MISTAKE("Mixing global warming with the ozone hole", "The ozone layer protects us from ultraviolet rays. It is a different problem from global warming."),
        QUIZ("Which gas is released when coal, oil and gas are burned?",
             ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"], 2,
             "Burning fossil fuels releases carbon dioxide, the main greenhouse gas added by human activity.",
             hint="Which gas do the exhaust pipes of cars release?",
             feedback=["Oxygen is used up in burning, not released.", "Nitrogen makes up most of the air and is not a greenhouse gas.", "", "Helium is a light gas and is not released by burning fuels."]),
        QUIZ("A coastal town builds a sea wall because of rising seas. This is an example of",
             ["Mitigation", "Adaptation", "Conservation of forests", "A cause of global warming"], 1,
             "A sea wall helps people cope with an effect that is already happening. This is adaptation.",
             hint="Does the wall reduce the greenhouse gases or only protect the town?",
             feedback=["Mitigation would reduce the gases, which a sea wall does not do.", "", "Conservation protects natural resources such as forests.", "A sea wall does not release greenhouse gases."]),
        H("Practice questions"),
        PQ("Define global warming.",
           "Global warming is the rise in the average temperature of the Earth's surface and lower atmosphere over a long period, mainly caused by the extra greenhouse gases that human activities add to the air."),
        PQ("State three causes of global warming.",
           "Any three of: burning fossil fuels, deforestation, cattle and rice farming, fertilisers, bush burning, rubbish dumps and industry."),
        PQ("Describe two negative effects and one positive effect of global warming.",
           "Negative: rising seas flood low coasts; changing rainfall causes floods and droughts that reduce crop yields. Positive: longer growing seasons in cold regions."),
        PQ("Outline two mitigation measures and two adaptation measures.",
           "Mitigation: use solar, hydro and wind energy; protect forests and plant trees. Adaptation: grow drought-resistant crops; build sea walls and drains."),
        SUM("The greenhouse effect is natural. Global warming is the rise in average temperature caused mainly by extra greenhouse gases.",
            "It is a world-wide hazard. Polar regions, low coasts, small islands and dry regions such as the Sahel are most at risk.",
            "The main causes are burning fossil fuels, deforestation, farming and waste.",
            "The effects are mainly negative: heat, rising seas, floods and droughts. A few positive effects occur in cold lands.",
            "Mitigation reduces the causes. Adaptation copes with the effects. Conservation protects forests and mangroves."),
    ],
))


# ------------------------------------------------------------------ 7. Floods, droughts and desertification
LESSONS.append(lesson(
    module=MODULE,
    topic=EH,
    title="Floods, droughts and desertification",
    slug="clim-floods-droughts-and-desertification",
    minutes=26,
    summary="The meaning, location, causes, positive and negative effects of floods, droughts and desertification, with examples from the Far North, the Lake Chad basin and Douala, and the adaptation, mitigation and conservation measures that respond to them.",
    objectives=[
        "Define floods, droughts and desertification",
        "Identify the typical areas where each hazard occurs, with examples from Cameroon",
        "Outline the causes and the positive and negative effects of each hazard",
        "Outline adaptation, mitigation and conservation measures for each hazard",
    ],
    key_concepts=["Flood", "Drought", "Desertification", "Overgrazing", "Sahel", "Floodplain", "Drainage", "Afforestation"],
    blocks=[
        H("Introduction"),
        T("In the rainy season, streets in parts of Douala can fill with brown water and people wade to work. In the dry season in the Far North, "
          "ponds dry up and herders walk long distances to find water for their animals. Both are hazards linked to rainfall: too much in one place, too little in another. "
          "A third hazard, desertification, slowly turns dry farmland into desert."),
        T("In this lesson we study the three together. For each one we answer the same questions: What is it? Where does it occur? "
          "What causes it? What are its effects? What can be done?"),
        H("Floods"),
        D("A **flood** happens when water covers land that is normally dry. It may be caused by a river overflowing, by heavy rain, or by the sea.", title="Flood"),
        T("**Where.** Floods occur on the floodplains of rivers, such as the floodplains of the Logone and the Benue, and in low coastal and urban areas "
          "such as parts of Douala. They also occur in many other countries with heavy seasonal rain."),
        T("**Causes.** The natural cause is very heavy rain, which makes rivers overflow. Human activities make floods worse. "
          "Cutting trees means less water is held in the soil. Paved roads and buildings stop water from soaking in. Rubbish blocks drains. "
          "Building in wetlands and on river banks puts people in the path of the water. Dam releases can add to the flow of a river downstream."),
        IMG("f5g-clim-urban-flood.svg", alt="Two diagrams comparing heavy rain on vegetated land, where water soaks into the soil, with a paved town with blocked drains, where water runs off quickly and floods the streets",
            caption="Figure 1. Why floods are worse in a built-up area."),
        T("**Negative effects.** People may be drowned or injured, and homes, roads and bridges are damaged. Crops and animals are lost. "
          "Dirty water spreads diseases such as cholera. Schools and markets close."),
        T("**Positive effects.** Floods leave behind fertile silt, so floodplain farms can be very productive. They refill wells and wetlands, and "
          "they help fish to breed."),
        H("Droughts"),
        D("A **drought** is a long period with much less rainfall than normal. It causes a shortage of water for people, crops and animals.", title="Drought"),
        T("**Where.** Droughts are most common and most serious in dry and semi-dry regions. The Sahel, including the Far North of Cameroon and the Lake Chad basin, "
          "is a well-known drought region. Droughts also affect the wetter regions, but less often."),
        T("**Causes.** The main cause is rainfall that comes late, stops early, or fails. Natural changes in the ocean and atmosphere play a part. "
          "Global warming may make droughts more frequent in some areas. Human activities can make the effects worse, for example by cutting vegetation "
          "so that the ground dries faster, and by using too much water."),
        T("**Negative effects.** Crops fail and animals die, so there is hunger and loss of income. Rivers, ponds and wells dry up, "
          "and women and children walk further for water. People and herds migrate. Bush fires become more common."),
        T("**Positive effects.** These are few and local. Dry weather can help in harvesting and drying crops, and in salt production. Overall, droughts do far more harm than good."),
        H("Desertification"),
        D("**Desertification** is the process by which fertile or semi-dry land slowly turns into desert-like land. It is caused by a mix of "
          "climate change and human activities.", title="Desertification"),
        T("**Where.** It occurs on the edges of deserts, in dry and semi-dry regions. In Africa the southern edge of the Sahara, the Sahel, "
          "is the best-known area. In Cameroon it threatens the Far North and the Lake Chad basin."),
        IMG("f5g-clim-desertification-cycle.svg", alt="A cycle diagram: overgrazing, tree cutting and bush fires lead to less plant cover and bare soil, then to soil erosion by wind and rain, then to loss of water and nutrients, then to failed crops and grass and desert-like land, which makes the ground hotter and drier",
            caption="Figure 2. The desertification cycle."),
        T("**Causes.** Natural: long droughts and a drier climate. Human: **overgrazing** (too many animals eat the grass), cutting trees for firewood and charcoal, "
          "bush burning, and over-cultivation, which wears out the soil. When plant cover is lost, wind and rain carry the soil away, and the land cannot grow plants again."),
        T("**Negative effects.** Crop yields fall, and grazing land shrinks. People face hunger and poverty and may migrate to towns or to other regions. "
          "Competition for land and water can lead to conflict. **Positive effects.** There are almost none. Some people argue that the abandoned land lets "
          "wildlife return, but this does not make up for the loss of farmland."),
        H("Responses: adaptation, mitigation and conservation"),
        KEY("Responses to each hazard", "Adaptation copes with the hazard. Mitigation reduces its causes or its size. Conservation protects the land and water.", cards=[
            ["Floods", "Adaptation: build on higher ground, raise houses, set up early warnings, use floodplain farming only in the dry season. Mitigation: clear and build drains, build embankments, stop dumping rubbish in gutters, leave wetlands unbuilt. Conservation: plant trees and keep forest cover on slopes and river banks."],
            ["Droughts", "Adaptation: grow drought-resistant and quick-growing crops, store water and fodder, dig wells and boreholes, and use small-scale irrigation. Mitigation: harvest rainwater, build small dams and ponds. Conservation: protect catchments and plant trees."],
            ["Desertification", "Adaptation: plant crops that suit dry land, and rotate crops. Mitigation: control grazing, use fuel-efficient stoves, plant shelter belts of trees. Conservation: afforestation, soil conservation, and international projects such as the Great Green Wall across the Sahel."],
        ]),
        TIP("This topic is a likely Paper 2 Section B or Section D question: 'Describe the causes and effects of desertification in the Far North' or 'Explain how floods can be managed'. "
            "Use a named place, a cause and an effect in every paragraph.", title="Exam link"),
        EX("Model answer 1", intro="Explain the causes and effects of flooding in a town such as Douala.", steps=[
            S("Define", text="A flood is water covering land that is normally dry."),
            S("Natural cause", text="Douala is low-lying and has heavy rain for many months, so rivers and streams overflow."),
            S("Human causes", text="Roads and buildings stop water from soaking in, rubbish blocks the drains, and houses are built on wetlands and river banks."),
            S("Effects", text="Homes and goods are damaged, roads are blocked, schools and markets close, and dirty water spreads cholera. A small positive effect is that floods refill wells and leave silt on farm land."),
            S("Responses", text="Build and clear drains, stop dumping rubbish, keep wetlands free of buildings, and set up early warnings."),
        ]),
        EX("Model answer 2", intro="Describe how desertification happens in the Far North of Cameroon.", steps=[
            S("Define", text="Desertification is the slow change of fertile or semi-dry land into desert-like land."),
            S("Starting point", text="The region has a short rainy season and is at risk of droughts."),
            S("Human pressure", text="Too many animals graze the land, trees are cut for firewood, and bush fires clear the grass."),
            S("Result", text="Bare soil is blown and washed away. The soil loses water and nutrients, crops and grass fail, and the land becomes desert-like."),
            S("Effects and responses", text="Hunger, poverty and migration follow. Planting trees, controlling grazing and conserving soil can slow the process."),
        ]),
        EX("Model answer 3", intro="Distinguish between a drought and desertification.", steps=[
            S("Drought", text="A drought is a temporary period of unusually low rainfall. The land can recover when the rains return."),
            S("Desertification", text="Desertification is a long-term loss of the land's ability to support plants. It does not reverse when the rains return."),
            S("Link", text="Droughts can make desertification worse, especially where people overgraze and cut trees."),
        ]),
        H("Common mistakes"),
        MISTAKE("Saying desertification is the spread of existing deserts by sand blowing", "The main problem is that land loses its plants and soil because of drought and human pressure. It can happen far from the desert."),
        MISTAKE("Saying a drought and desertification are the same", "A drought is temporary. Desertification is long-lasting."),
        MISTAKE("Listing only negative effects", "The syllabus asks for positive and negative effects. Floods leave fertile silt. Say so, but also say the harm is greater."),
        QUIZ("Which of these is a human cause of floods in towns?",
             ["Heavy rain", "Rubbish blocking drains", "A long drought", "The north-east trade wind"], 1,
             "Rubbish blocks drains, so water cannot flow away. Heavy rain is a natural cause.",
             hint="Which cause can people change?",
             feedback=["Heavy rain is natural, not a human cause.", "", "A drought is a lack of rain and does not cause floods.", "The north-east trade wind is a planetary wind and is not a cause of floods."]),
        QUIZ("Which action best helps to reduce desertification in the Far North?",
             ["Cutting more trees for firewood", "Letting more cattle graze", "Planting trees and controlling grazing", "Burning the bush after harvest"], 2,
             "Trees and controlled grazing protect the soil and keep plant cover.",
             hint="Which action keeps plants on the ground?",
             feedback=["Cutting trees removes plant cover.", "More cattle means overgrazing.", "", "Burning clears plants and exposes the soil."]),
        H("Practice questions"),
        PQ("Define a flood, a drought and desertification.",
           "A flood is water covering land that is normally dry. A drought is a long period with much less rainfall than normal. Desertification is the slow change of fertile or semi-dry land into desert-like land."),
        PQ("Name one area in Cameroon at risk from drought and one at risk from flooding.",
           "Drought: the Far North, including the Lake Chad basin. Flooding: the floodplains of the Logone and the Benue, or low-lying parts of Douala."),
        PQ("Describe two natural causes and two human causes of desertification.",
           "Natural: long droughts and a drier climate. Human: overgrazing, cutting trees for firewood and charcoal, bush burning, over-cultivation."),
        PQ("Outline three ways of controlling the effects of droughts.",
           "Grow drought-resistant crops; harvest rainwater and build small dams and ponds; dig wells and boreholes; store food and fodder; plant trees to protect catchments."),
        SUM("A flood covers dry land with water. A drought is a long spell with little rain. Desertification turns fertile or semi-dry land into desert-like land.",
            "Floods occur on floodplains and in low towns such as parts of Douala. Droughts and desertification affect the Sahel, including the Far North and Lake Chad basin.",
            "Floods are caused by heavy rain and made worse by paving, blocked drains and tree cutting. Overgrazing, tree cutting and bush burning cause desertification.",
            "Floods leave fertile silt but cause much damage. Droughts and desertification have very few benefits.",
            "Responses include early warning, drains, drought-resistant crops, rainwater harvesting, tree planting and soil conservation."),
    ],
))


# ------------------------------------------------------------------ 8. Water scarcity
LESSONS.append(lesson(
    module=MODULE,
    topic=EH,
    title="Water scarcity as an environmental hazard",
    slug="clim-water-scarcity",
    minutes=22,
    summary="What water scarcity is, where it occurs (in dry regions, rural areas and growing cities), its causes, its negative and positive effects, and the adaptation, mitigation and conservation measures that can reduce it.",
    objectives=[
        "Define water scarcity and distinguish physical from economic scarcity",
        "Identify areas where water scarcity occurs, in Cameroon and elsewhere",
        "Outline the causes and the effects (positive and negative) of water scarcity",
        "Outline adaptation, mitigation and conservation measures",
    ],
    key_concepts=["Water scarcity", "Physical scarcity", "Economic scarcity", "Water stress", "Borehole", "Rainwater harvesting", "Water conservation"],
    blocks=[
        H("Introduction"),
        T("In a village in the Far North, a girl walks for an hour each morning to a well. In a fast-growing district of a big city, a family "
          "waits for the tap to run and buys water from a vendor when it does not. Both families live with the same problem: not enough "
          "safe water for their needs."),
        T("The Board treats water scarcity as an **environmental hazard**, not only as an urban problem. It affects villages, farms and towns, in dry "
          "regions and in wetter ones. In this lesson you will define it and study its causes, its effects and what can be done."),
        H("Definition"),
        D("**Water scarcity** is a situation in which there is not enough safe fresh water to meet the needs of people, farming, industry and nature in a "
          "place or region.", title="Water scarcity"),
        IMG("f5g-clim-water-scarcity-types.svg", alt="A diagram of two kinds of water scarcity: physical scarcity, where there is not enough water in the region, and economic scarcity, where water exists but people lack wells, pipes or money",
            caption="Figure 1. Two kinds of water scarcity."),
        T("**Physical scarcity** means there is not enough water in the region, because rainfall is low or unreliable. "
          "**Economic scarcity** means that water is there, but people cannot reach it, because there are no wells, pipes or treatment plants, or because "
          "they cannot pay for it. Many places have a mix of both."),
        H("Where does it occur?"),
        T("Water scarcity is found in dry regions such as the Sahel (including the Far North and the Lake Chad basin), North Africa and the Horn of Africa. "
          "It is also found in the wetter regions where water is polluted or the supply system is weak. Many rural villages "
          "depend on a single well or stream, and some fast-growing cities cannot lay pipes as quickly as new homes are built."),
        H("Causes"),
        KEY("Causes of water scarcity", "Some are natural, some are human.", cards=[
            ["Low and unreliable rainfall", "Dry climates and droughts leave rivers, ponds and wells empty."],
            ["Climate change", "Changes in rainfall and higher temperatures increase evaporation and may reduce supplies in some regions."],
            ["Growing demand", "More people, more farms and more industry use more water."],
            ["Pollution", "Sewage, waste and chemicals make water unsafe, so there is less usable water."],
            ["Waste and poor management", "Leaking pipes, open taps and wasteful irrigation lose a lot of water."],
            ["Poor infrastructure and poverty", "Few wells, pipes and treatment plants, and not enough money to build or repair them."],
        ]),
        T("Deforestation can also play a part. Without trees and plant cover, rain runs off quickly instead of soaking into the ground to refill wells. "
          "Over-use of a lake or river, for example for irrigation, can leave less for people downstream. Lake Chad has lost much of its water in recent decades "
          "because of low rainfall and heavy use."),
        H("Effects"),
        T("**Negative effects.** People drink unsafe water and get diseases such as cholera, typhoid and diarrhoea. "
          "Women and children spend hours fetching water, so children miss school and women lose time for work. Crops fail and animals die, which "
          "leads to hunger and loss of income. Hygiene is poor, and clinics and schools struggle without clean water. Industry cannot grow. "
          "People migrate, and competition for water can lead to quarrels and conflict."),
        T("**Positive effects.** These are few. Scarcity can push communities to save water, to build wells and storage tanks, to use rainwater, and to try new "
          "ideas such as drip irrigation. It can also lead to new rules and cooperation to share water fairly. But the harm is much greater than the benefit."),
        H("Responses: adaptation, mitigation and conservation"),
        KEY("What can be done?", "Combine measures: increase supply, reduce demand and protect sources.", cards=[
            ["Adaptation", "Dig wells and boreholes; store water in tanks and ponds; grow drought-resistant crops; use drip irrigation; treat or boil drinking water."],
            ["Mitigation", "Repair leaking pipes; build small dams and water treatment plants; stop polluting rivers; reduce waste of water; harvest rainwater from roofs."],
            ["Conservation", "Protect water catchments and forests; plant trees along rivers; reuse waste water for farming; teach people to save water; manage lakes and rivers fairly."],
        ]),
        TIP("Water scarcity is a new item in the revised syllabus. Expect a short Paper 1 question on its definition or a cause, and a Paper 2 question asking for causes, effects and solutions in the Far North or in a town. "
            "Always give causes, effects and solutions in separate paragraphs.", title="Exam link"),
        EX("Model answer 1", intro="Outline the causes of water scarcity in the Far North of Cameroon.", steps=[
            S("Define", text="Water scarcity is a lack of enough safe fresh water for people, farming and industry."),
            S("Natural cause", text="The Far North lies in the Sahel. Rainfall is low and unreliable, and droughts leave wells and ponds dry."),
            S("Human causes", text="A growing population and herds use more water. Trees are cut, so rain runs off quickly. Lake Chad has lost much of its water."),
            S("Other causes", text="There are few wells and boreholes, and poor families cannot pay for treated water."),
        ]),
        EX("Model answer 2", intro="Describe the effects of water scarcity on a rural community.", steps=[
            S("Health", text="People drink unsafe water and get diseases such as cholera and diarrhoea."),
            S("Time and education", text="Children, especially girls, spend hours fetching water and miss school."),
            S("Farming", text="Crops and animals die, so there is hunger and loss of income."),
            S("Wider effects", text="People migrate or quarrel over water. A small positive effect is that the community may start saving water or building wells."),
        ]),
        EX("Model answer 3", intro="Suggest how water scarcity can be reduced in a village and in a town.", steps=[
            S("Village", text="Dig boreholes and protect wells; build small dams and ponds; harvest rainwater; plant trees to protect the source."),
            S("Town", text="Repair leaking pipes; build treatment plants and more taps; stop pollution of rivers; teach people to save water."),
            S("Both", text="Combine measures that raise supply, reduce waste and protect the water source."),
        ]),
        H("Common mistakes"),
        MISTAKE("Thinking water scarcity is only a city problem", "The syllabus treats it as a hazard that also affects villages and farms."),
        MISTAKE("Thinking scarcity means no rain at all", "Scarcity can also be economic: the water is there, but people cannot reach it or afford it."),
        MISTAKE("Giving effects without a cause or solution", "Give causes, effects and solutions in separate paragraphs, with an example."),
        QUIZ("A river runs through a district, but families there have no pipes or wells and must walk far to fetch water. This is an example of",
             ["Physical scarcity", "Economic scarcity", "A flood", "Desertification"], 1,
             "Water exists, but people cannot reach it because there is no infrastructure. This is economic scarcity.",
             hint="Is the water absent, or only out of reach?",
             feedback=["Physical scarcity means there is not enough water in the region.", "", "A flood is too much water, not too little.", "Desertification is the loss of fertile land."]),
        QUIZ("Which is a conservation measure for water?",
             ["Draining wetlands", "Protecting forests on a river catchment", "Cutting trees along a river", "Dumping waste in a stream"], 1,
             "Forests on catchments help rain to soak into the ground and keep rivers clean.",
             hint="Which choice protects a water source?",
             feedback=["Wetlands store water. Draining them reduces water.", "", "Cutting trees increases runoff.", "Dumping waste pollutes the water."]),
        H("Practice questions"),
        PQ("Define water scarcity.",
           "Water scarcity is a situation in which there is not enough safe fresh water to meet the needs of people, farming and industry."),
        PQ("Distinguish between physical and economic water scarcity.",
           "Physical scarcity means there is not enough water in the region, for example because rainfall is low. Economic scarcity means water exists but people cannot reach or afford it because of poor infrastructure or poverty."),
        PQ("State three causes of water scarcity.",
           "Any three of: low and unreliable rainfall, drought or climate change, growing demand, pollution, waste and leaks, poor infrastructure, deforestation."),
        PQ("Describe three effects of water scarcity on a community.",
           "People drink unsafe water and fall ill; children miss school fetching water; crops and animals die, so there is hunger and lost income; people may migrate or quarrel over water."),
        SUM("Water scarcity is a shortage of safe fresh water. It can be physical (not enough water) or economic (water out of reach).",
            "It occurs in dry regions such as the Sahel and also in villages and fast-growing towns.",
            "Causes include low rainfall, climate change, growing demand, pollution, waste and poor infrastructure.",
            "Effects are mostly negative: disease, lost schooling, hunger, migration and conflict. Positive effects are few.",
            "Responses: wells and boreholes, rainwater harvesting, repairing leaks, treating water, and protecting catchments and forests."),
    ],
))


# ------------------------------------------------------------------ 9. Waste management
LESSONS.append(lesson(
    module=MODULE,
    topic=EH,
    title="Waste management as an environmental hazard",
    slug="clim-waste-management",
    minutes=22,
    summary="The types of waste, the problems and effects of poor waste management, and the solutions: reduce, reuse, recycle, compost and organised collection and disposal, treated as an environmental hazard for towns, villages and farms.",
    objectives=[
        "Define waste and waste management, and classify the main types of waste",
        "Identify where waste problems occur, in towns, villages and industries",
        "Outline the causes, the problems and the effects (positive and negative) of poor waste management",
        "Outline adaptation, mitigation and conservation measures: reduce, reuse, recycle, compost and collect",
    ],
    key_concepts=["Waste", "Solid waste", "Liquid waste", "Hazardous waste", "Biodegradable", "Recycling", "Composting", "Landfill"],
    blocks=[
        H("Introduction"),
        T("Walk through a busy market in any Cameroonian town and you will see them: plastic bags, bottles, vegetable leftovers and sachets "
          "blown against the drains. When the rain comes, the rubbish blocks the gutters and the water spreads into the street. "
          "A heap of rubbish by the road smells, attracts flies and rats, and sometimes it is burnt, so smoke fills the air."),
        T("The Board treats waste management as an **environmental hazard**, not just a town problem. Waste appears in villages, on farms, in "
          "hospitals and in factories too. In this lesson you will learn what waste is, why it becomes a hazard, and what can be done."),
        H("Meaning and types of waste"),
        D("**Waste** is any material that people throw away because they no longer need it. **Waste management** is the collection, treatment and "
          "disposal of waste so that it does not harm people or the environment.", title="Waste and waste management"),
        KEY("Main types of waste", "Waste can be grouped by its form and by what it can do.", cards=[
            ["Solid waste", "Household rubbish, packaging, plastics, paper, glass, metal, broken goods, market waste, building waste."],
            ["Liquid waste", "Sewage, waste water from homes and factories, used oil and chemicals."],
            ["Organic (biodegradable) waste", "Food waste, leaves, crop remains and animal dung. It rots naturally."],
            ["Hazardous waste", "Medical waste, batteries, chemicals, old electronics (e-waste). It can poison people and the environment."],
        ]),
        T("Waste also comes from different **sources**: homes, markets and shops, farms, hospitals, factories and building sites. "
          "Plastic is a special problem because it does not rot. It breaks into smaller and smaller pieces that remain for a very long time."),
        H("Where and why does it occur?"),
        T("Waste problems are worst where many people live close together and collection is weak. Fast-growing towns and cities, such as Douala and "
          "Yaounde, produce large amounts of waste. Markets, bus stations and slums are hot spots. Villages have waste problems too, as plastics "
          "reach the countryside. Industrial areas and farms produce waste of their own."),
        KEY("Causes of the waste problem", "Mostly people and systems, not nature.", cards=[
            ["More people and more goods", "More packaging and cheap plastics are used and thrown away."],
            ["Weak collection", "Not enough bins, trucks and workers, and poor roads in some districts."],
            ["Lack of money and land", "Councils cannot afford enough collection and safe landfills."],
            ["Poor habits", "Dumping in drains, rivers and open land; burning rubbish."],
        ]),
        H("Problems and effects"),
        T("**Negative effects.** Rubbish blocks drains, which makes floods worse. Heaps of waste smell and attract rats, flies and mosquitoes, "
          "which spread diseases such as cholera and malaria. Burning waste releases smoke and harmful gases that harm health and add to global warming. "
          "Liquid from rotting waste, called leachate, can soak into the ground and pollute wells and rivers. Plastics choke rivers and the sea and can "
          "kill fish and animals. Dirty towns lower the quality of life and put off visitors and investors."),
        T("**Positive effects.** Waste can become a resource. Organic waste can be made into compost for farms. Some waste can be recycled or sold, "
          "which creates jobs for collectors and small businesses. Waste can also produce energy, for example biogas from rotting waste. "
          "These benefits only occur when waste is managed well."),
        IMG("f5g-clim-waste-hierarchy.svg", alt="A funnel diagram of the waste hierarchy from best to worst: reduce, reuse, recycle, compost or recover, and dispose in a landfill",
            caption="Figure 1. The waste hierarchy: prevent waste first, and dispose of it last."),
        H("Solutions: reduce, reuse, recycle, compost and collect"),
        D("The **waste hierarchy** ranks the ways of dealing with waste. The best choice is to avoid making waste. The worst is to dump it.", title="Waste hierarchy"),
        KEY("The main solutions", "Move up the hierarchy wherever you can.", cards=[
            ["Reduce", "Make less waste. Buy only what you need, avoid single-use plastic and carry a cloth bag."],
            ["Reuse", "Use things again. Refill bottles, repair goods, give away old clothes."],
            ["Recycle", "Turn waste into new products, for example paper, glass, metal and some plastics."],
            ["Compost", "Rot food and garden waste into a rich soil for gardens and farms."],
            ["Collect and dispose safely", "Provide bins and regular collection, sorting, and sanitary landfills, away from water sources."],
        ]),
        T("**Adaptation** includes household sorting, storing waste safely and using drains that are protected from rubbish. "
          "**Mitigation** includes better laws, bans on some plastic bags (rules of this kind exist in Cameroon and other countries: check your textbook), fines "
          "for dumping, and waste-to-energy plants. **Conservation** includes keeping rivers, wetlands and forests clean and protecting them from dumping, and "
          "teaching people to care for the environment."),
        TIP("This is a new item in the revised syllabus. Expect a Paper 1 question on the types of waste or the meaning of reduce, reuse and recycle. In Paper 2, "
            "link waste to floods, disease and pollution, and give solutions in order of the waste hierarchy. For details of waste collection in Douala and Yaounde, check your textbook.", title="Exam link"),
        EX("Model answer 1", intro="Describe the problems caused by poor waste management in a town such as Douala.", steps=[
            S("Define", text="Waste is material people throw away. Poor management means it is not collected or disposed of safely."),
            S("Floods", text="Rubbish blocks the drains, so rainwater cannot flow away and floods occur in the streets."),
            S("Health", text="Heaps of waste attract rats and mosquitoes and spread diseases such as cholera and malaria."),
            S("Pollution", text="Burning waste pollutes the air. Liquid from rotting waste pollutes wells and rivers. Plastic chokes drains and streams."),
        ]),
        EX("Model answer 2", intro="Explain how reduce, reuse and recycle can help to solve the waste problem.", steps=[
            S("Reduce", text="Making less waste is the best choice. For example, a market trader can use a cloth bag instead of many plastic bags."),
            S("Reuse", text="Using things again keeps them out of the waste stream. For example, refill bottles."),
            S("Recycle", text="Turning waste into new goods saves resources and gives work to collectors. For example, metal, paper and glass are recycled."),
            S("Conclusion", text="Together they reduce the amount that must be collected and buried."),
        ]),
        EX("Model answer 3", intro="Suggest how organic waste from a market can be used.", steps=[
            S("Separate", text="Keep vegetable leftovers and leaves apart from plastic and metal."),
            S("Compost", text="Pile the organic waste so that it rots into compost."),
            S("Use", text="Sell or use the compost on farms and gardens to improve the soil."),
            S("Benefits", text="This cuts the amount of rubbish, lowers the smell, and returns nutrients to the soil."),
        ]),
        H("Common mistakes"),
        MISTAKE("Treating waste as only an urban problem", "The syllabus covers villages, farms, hospitals and industry too. Plastic reaches the countryside."),
        MISTAKE("Saying the answer is 'burn it'", "Burning pollutes the air and adds greenhouse gases. It is not a good solution for most waste."),
        MISTAKE("Mixing up reuse and recycle", "Reuse means using the same item again. Recycle means turning it into something new."),
        QUIZ("Which of these is an example of hazardous waste?",
             ["Banana peels", "Used batteries", "Paper", "Garden leaves"], 1,
             "Batteries contain harmful chemicals, so they are hazardous waste.",
             hint="Which item can poison water and soil?",
             feedback=["Banana peels are organic waste that rots naturally.", "", "Paper is solid waste that can be recycled.", "Garden leaves are organic waste."]),
        QUIZ("A trader refills a plastic bottle many times instead of throwing it away. This is",
             ["Recycling", "Reducing", "Reusing", "Landfilling"], 2,
             "Using the same item again is reuse. Recycling turns the item into something new.",
             hint="Is the bottle used again as it is, or turned into something else?",
             feedback=["Recycling would mean melting the plastic to make a new product.", "Reducing means making less waste in the first place.", "", "Landfilling is dumping waste in the ground."]),
        H("Practice questions"),
        PQ("Define waste and name three types of waste.",
           "Waste is any material that people throw away because they no longer need it. Types: solid waste, liquid waste, organic waste and hazardous waste."),
        PQ("Give three problems caused by uncollected waste in a market town.",
           "It blocks drains and causes floods; it attracts rats and flies that spread diseases; burning it pollutes the air; liquid from rotting waste pollutes water."),
        PQ("Explain what is meant by reduce, reuse and recycle, with an example of each.",
           "Reduce: make less waste, such as using a cloth bag. Reuse: use the item again, such as refilling a bottle. Recycle: turn waste into new products, such as making new metal goods from scrap."),
        PQ("Outline four measures that can improve waste management in a town.",
           "Provide bins and regular collection; build sanitary landfills away from water; sort waste and compost organic waste; encourage recycling; make laws and fines against dumping; teach people to reduce waste."),
        SUM("Waste is material that is thrown away. The main types are solid, liquid, organic and hazardous waste.",
            "Waste is worst where many people live and collection is weak, but it also affects villages, farms and industry.",
            "Poor waste management blocks drains and causes floods, spreads diseases and pollutes air, water and soil. Well-managed waste can be a resource.",
            "The waste hierarchy: reduce first, then reuse, recycle, compost, and dispose safely as the last choice.",
            "Solutions need laws, collection systems and changes in everyone's habits."),
    ],
))


for _lesson in LESSONS:
    _lesson["blocks"] = _merge_text(_lesson["blocks"])
