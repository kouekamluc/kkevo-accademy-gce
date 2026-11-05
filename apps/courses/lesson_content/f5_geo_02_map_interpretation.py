"""Form 5 Geography: Map interpretation (5 lessons, one practice set each).

All maps in these lessons show KUMA DISTRICT, a fictitious place drawn for teaching.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "Map Reading and Interpretation"
TOPIC = "Map interpretation"

LESSONS = []

# ------------------------------------------------------------------ 1. Relief and contour lines
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Relief and contour lines",
    slug="mapint-relief-and-contour-lines",
    minutes=24,
    summary="How maps show the shape of the land with contours, spot heights, trig stations and bench marks, how to read slopes and landforms from contour patterns, and how to describe the relief of an area.",
    objectives=[
        "Identify the ways of representing relief on a map: contours, spot heights, trigonometrical stations, bench marks, hachures and layer tinting",
        "Interpret contour lines and the contour interval to find the height of a place",
        "Identify and describe hills, valleys, spurs, ridges, plateaus, saddles and escarpments from contour patterns",
        "Describe the gradient of a slope as steep or gentle from the spacing of contours",
    ],
    key_concepts=["Relief", "Contour line", "Contour interval", "Spot height", "Trigonometrical station", "Bench mark",
                  "Steep and gentle slope", "Spur", "Saddle", "Escarpment"],
    blocks=[
        H("Introduction"),
        T("A student in Bamenda lives on high land in the western highlands. A student in Douala lives on a low coastal plain, "
          "close to sea level. Between them are hills, valleys and plateaus. The shape of the land, with its heights and slopes, "
          "is called **relief**."),
        T("A map is flat. So how can it show a mountain like Mount Cameroon, or the flat floor of the Benue lowlands? "
          "Mapmakers use special signs for height. In this lesson you learn to read those signs and to describe relief in words. "
          "That is the first step of every map interpretation answer. The Board has removed gradient calculation and cross-sections, so you "
          "will **describe** slopes as steep or gentle. You will not calculate them."),
                H("Ways of showing relief"),
        IMG("f5g-mapint-relief-symbols.svg",
            alt="Six ways relief is shown: contour line, spot height, trig station, bench mark, hachures and layer tinting",
            caption="Figure 1. Six ways of showing relief on a map."),
        D("A **contour line** is a line on a map that joins places of equal height above sea level. Every point on one contour "
          "has the same height.", title="Contour line"),
        D("The **contour interval** is the difference in height between two neighbouring contour lines. On the map in this "
          "lesson the interval is 50 metres. Every second line is thicker and has its height written on it (400, 500, 600).",
          title="Contour interval"),
        KEY("Other height signs", "Contours show the shape of the land. These signs give exact heights at single points.", cards=[
            ["Spot height", "A dot with a number. It gives the exact height of one point, for example 431 metres."],
            ["Trigonometrical station", "A triangle with a dot and a height. It is a fixed survey point, usually on a hilltop."],
            ["Bench mark", "A cross marked BM with a height. It is a cut mark on a bridge, building or rock used by surveyors."],
            ["Hachures", "Short lines drawn down a slope. They are thick and close where the slope is steep and thin where it is gentle."],
            ["Layer tinting", "Colours between contour heights. Low land may be green, higher land yellow and brown."],
        ], note="Contours and spot heights are the signs you meet most often."),
        H("Reading contour lines"),
        T("Two rules do most of the work. First, **contour spacing shows steepness**. Second, **the numbers show which way "
          "the land rises**. A contour line never crosses another contour line, because one place cannot have two heights."),
        KEY("Gradient: steep or gentle?", "You describe gradient. You do not calculate it.", cards=[
            ["Steep slope", "Contours are close together. The land rises quickly over a short distance."],
            ["Gentle slope", "Contours are far apart. The land rises slowly over a long distance."],
            ["Flat land", "Very few contours, or none, over a wide area."],
            ["Changing slope", "Close at the top and wide at the bottom means steep, then gentle."],
        ]),
        IMG("f5g-mapint-contour-shapes.svg",
            alt="Eight contour patterns: hill, ridge, valley, spur, saddle, plateau, escarpment, and steep and gentle slopes",
            caption="Figure 2. Eight contour patterns. Heights are in metres and the interval is 50 m."),
        KEY("Landforms from contour patterns", "Look at Figure 2 as you read.", cards=[
            ["Hill", "Closed rings. The numbers get higher towards the middle."],
            ["Ridge", "Long, narrow closed rings. A line of high ground with lower land on both sides."],
            ["Valley", "V-shaped bends. The V points UPHILL, towards higher numbers. A river usually runs along it."],
            ["Spur", "V-shaped bends. The V points DOWNHILL. It is high ground sticking out from a hill."],
            ["Saddle", "A dip in the high ground between two hills. It is a natural pass for a road or path."],
            ["Plateau", "A wide, flat top with steep sides. Contours are close at the edge and absent on top."],
            ["Escarpment", "A long steep slope: many contours very close, with a gentle slope behind it."],
        ]),
        H("Reading the relief of Kuma District"),
        T("Kuma District is a fictitious area drawn for teaching. Study Figure 3. The scale is 1 : 50 000 and the contour interval is "
          "50 metres. The highest point is the trig station on Kuma Hill, 706 metres above sea level. The lowest land is the "
          "surface of Lake Bimbi, 300 metres."),
        IMG("f5g-mapint-kuma-relief.svg",
            alt="Relief map of Kuma District with contours at 50 metre interval, spot heights, two trig stations, a bench mark, a lake and lettered points A, D, E, F and G",
            caption="Figure 3. Relief of Kuma District (fictitious). Letters A, D, E, F and G mark places used in the examples."),
        EX("Model answer 1: describe the relief of Kuma District", intro="Describe the relief of the area shown in Figure 3.", steps=[
            S("Point: the overall pattern", text="The land is highest in the north-west and north-east and falls towards the south-east, where the lake is. "
              "Heights range from 300 metres at Lake Bimbi to 706 metres on Kuma Hill, a range of 406 metres."),
            S("Point: the highland in the north-west", text="Kuma Hill rises to a trig station at 706 metres. Ekwe Hill to its east reaches 644 metres. "
              "Between the two hills there is a saddle (A) of 564 metres, which is a low point on the high ground."),
            S("Point: the plateau and escarpment in the north-east", text="Land over 550 metres is flat on top, with a trig station at 586 metres, so it is a plateau (G). "
              "Its south-west edge is an escarpment (D) with many contours very close together."),
            S("Point: the lowland in the south", text="South of the 350 metre contour the land is gentle. There are few contours. A spot height reads 319 metres and the bench mark near Tabeng reads 330 metres. "
              "This is low flat land."),
            S("Point: the slopes", text="Slopes are steepest on the west side of Kuma Hill (F) and on the escarpment, where contours are close. They are gentlest on the plateau top and in the lowland, "
              "where contours are far apart or missing."),
        ]),
        EX("Model answer 2: identify features from letters", intro="Using Figure 3, name the relief feature at each letter and give the evidence from the contours.", steps=[
            S("A: saddle", text="A lies between two hills. The ground dips from 564 metres at A, with higher ground on two sides and lower ground on the other two."),
            S("D: escarpment", text="At D many contours run close together in a long line. This is a steep slope along the edge of the plateau."),
            S("E: gentle slope or lowland", text="At E there are no contours for a long distance. The land is almost flat, about 320 metres high."),
            S("F: steep slope", text="At F the contours are close together on the west side of Kuma Hill, so the slope is steep."),
            S("G: plateau", text="At G the land is high (over 550 metres) but there are no contours on top. It is a flat-topped area with steep edges."),
        ]),
        TIP("Exam link: relief is the first part of Paper 2 Section A (map reading and interpretation, compulsory) and appears in Paper 1 "
            "multiple-choice questions on map skills. Questions ask you to identify a feature, describe slope or relief, or give a height.",
            title="Exam link"),
        MISTAKE("Saying that close contours mean high land",
                "Close contours mean a STEEP slope, not high land. A steep slope can be at 300 metres or at 700 metres. Read the numbers to find the height."),
        MISTAKE("Calculating gradient",
                "The Board has removed gradient calculation. Write 'steep' or 'gentle' and give the evidence: 'the contours are close together'. Do not write a ratio."),
        QUIZ("On a contour map, closely spaced contour lines show:", [
            "a gentle slope", "a steep slope", "a flat plateau top", "the bottom of a valley"], 1,
            "Contours close together mean the land rises quickly over a short distance, so the slope is steep.",
            hint="Think about how far you walk to climb 50 metres.",
            feedback=["A gentle slope has contours far apart.", "", "A plateau top has very few contours.",
                      "A valley is shown by V-shaped bends, not by close spacing alone."]),
        H("Practice questions"),
        PQ("Define a contour line and the contour interval. State the contour interval of Figure 3.",
           "A contour line joins places of equal height above sea level. The contour interval is the difference in height between two neighbouring contours. "
           "In Figure 3 the interval is 50 metres. The thick lines are 400 and 500 metres, and there is one thin line between them at 450 metres."),
        PQ("In Figure 3, state the height and the name of the feature at the highest point, and explain how the map shows it.",
           "The highest point is the trig station on Kuma Hill at 706 metres. A trig station is shown by a triangle with a dot. "
           "The contours form closed rings and the heights increase towards the middle, which shows a hill."),
        PQ("Compare the slope at F with the slope at E in Figure 3. Give the reason for the difference.",
           "The slope at F is steep and the slope at E is gentle. At F the contours on the west side of Kuma Hill are close together, so the land rises quickly. "
           "At E there are no contours over a wide area, so the land is almost flat (about 320 metres)."),
        PQ("Explain how you would tell a valley from a spur on a contour map.",
           "Both are shown by V-shaped bends in the contours. In a valley the V points uphill, towards higher numbers, and a river often runs along it. "
           "In a spur the V points downhill, towards lower numbers. Read the heights on the lines to decide."),
        SUM("Relief is the shape of the land. Maps show it with contours, spot heights, trig stations, bench marks, hachures and layer tinting.",
            "The contour interval is the height difference between neighbouring contours. Heights go up or down by the interval each time you cross a line.",
            "Close contours mean a steep slope. Wide contours mean a gentle slope. You describe gradient, you do not calculate it.",
            "Closed rings show a hill, V-bends pointing uphill a valley, V-bends pointing downhill a spur. A saddle, plateau and escarpment have their own patterns.",
            "To describe relief, give the highest and lowest land with heights, name the main landforms and say where the slopes are steep and gentle."),
    ],
))

# ------------------------------------------------------------------ 2. Drainage on maps
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Drainage on maps: rivers, lakes and patterns",
    slug="mapint-drainage-on-maps",
    minutes=22,
    summary="How to read rivers, tributaries, confluences, lakes, swamps and seasonal streams on a map, how to work out the direction of flow from contours, and how to recognise dendritic, trellised and radial drainage patterns.",
    objectives=[
        "Identify the source, mouth, tributaries and confluences of a river on a map",
        "Describe the direction of flow of a river from the contour lines and the heights",
        "Identify lakes, swamps and seasonal streams and describe their distribution",
        "Identify and describe dendritic, trellised and radial drainage patterns",
    ],
    key_concepts=["Drainage", "Source", "Mouth", "Tributary", "Confluence", "Direction of flow", "Seasonal stream", "Swamp",
                  "Dendritic pattern", "Trellised pattern", "Radial pattern"],
    blocks=[
        H("Introduction"),
        T("Cameroon has many rivers. The Sanaga, the Wouri and the Nyong flow towards the Atlantic coast. The Benue and the Logone "
          "flow through the north, and the Logone drains towards Lake Chad. Where rivers flow, farmers, fishers and towns follow."),
        T("On a map, rivers, lakes and swamps are usually drawn in blue. Together they are called the **drainage** of an area. "
          "To interpret a map you must find the rivers, say where they start and end, say which way they flow and describe the "
          "pattern that they make."),
        H("The parts of a river"),
        IMG("f5g-mapint-river-terms.svg",
            alt="A river system with the source in highland, two tributaries, two confluences, the main river and the mouth at a lake or sea",
            caption="Figure 1. The parts of a river system."),
        D("The **source** is the place where a river begins, usually in higher land. The **mouth** is the place where it ends, where it enters the sea, a lake or a larger river.", title="Source and mouth"),
        D("A **tributary** is a smaller stream or river that flows into a larger one. A **confluence** is the place where they join.",
          title="Tributary and confluence"),
        H("Direction of flow"),
        T("Rivers flow downhill. On a map the river does not have an arrow, so you work out the direction from the heights."),
        KEY("Three ways to find the direction of flow", "Use at least one, and give the evidence.", cards=[
            ["Heights at both ends", "Find the contour or spot height near the source and near the mouth. The river flows from the higher number to the lower number."],
            ["V-shaped contours", "Contours bend into a V where they cross a river. The V points upstream, towards higher land."],
            ["Tributaries", "A tributary joins a main river in a Y shape. The two open arms of the Y are upstream and the stem is downstream."],
        ]),
        H("Lakes, swamps and seasonal streams"),
        KEY("Other water features", "Learn the symbols in the key of every map.", cards=[
            ["Lake", "A large area of water on land. It is shown in blue, and its height can be read from the contour or spot height at its edge."],
            ["Swamp", "Low, flat land that is wet. It is shown by blue lines and grass tufts. It is usually found near river mouths and lakes."],
            ["Seasonal stream", "A broken blue line. It carries water only in the rainy season and is dry in the dry season."],
        ]),
        H("Drainage patterns"),
        IMG("f5g-mapint-drainage-patterns.svg",
            alt="Three drainage patterns: dendritic like a tree, trellised with right-angle joins, and radial from a hill",
            caption="Figure 2. The three drainage patterns."),
        KEY("The three patterns", "Look at Figure 2.", cards=[
            ["Dendritic", "Like the branches of a tree. Tributaries join the main river at acute angles. It is common on gently sloping land of uniform rock."],
            ["Trellised", "Main streams run in parallel and tributaries join them at right angles. It is found where long ridges and valleys alternate."],
            ["Radial", "Streams flow outwards in all directions from a high point, like the spokes of a wheel. It forms around a dome-shaped hill or a volcano."],
        ], note="Mount Cameroon is a volcano. Check your textbook for the streams on its slopes."),
        H("Reading the drainage of Kuma District"),
        IMG("f5g-mapint-kuma-drainage.svg",
            alt="Drainage map of Kuma District showing R. Kuma with its tributaries R. Njuni, R. Ngom, R. Ewe and R. Ebo, a seasonal stream, Lake Bimbi and a swamp, and lettered points P, Q, R, S and V",
            caption="Figure 3. Drainage of Kuma District (fictitious). Contours are drawn faintly."),
        EX("Model answer 1: describe the drainage of Kuma District", intro="Describe the drainage shown in Figure 3.", steps=[
            S("Point: the main river", text="The main river is the R. Kuma. Its source (Q) is at about 480 metres at the foot of the plateau in the north. "
              "It flows south and then south-east, and its mouth (R) is at Lake Bimbi, 300 metres above sea level."),
            S("Point: the tributaries", text="Four tributaries join the R. Kuma. From north to south they are the R. Njuni, the R. Ngom, the R. Ewe and the R. Ebo. "
              "The confluence of the R. Ewe and the R. Kuma is marked P."),
            S("Point: lake, swamp and seasonal stream", text="Lake Bimbi lies in the south-east, in the lowest land. A swamp surrounds the lake and the lower course of the river, where the land is flat. "
              "A seasonal stream (S) in the south-west carries water only in the wet season and joins the R. Ewe."),
            S("Point: the pattern", text="The R. Kuma and its tributaries form a dendritic pattern, like the branches of a tree. Around Kuma Hill a few short streams flow outwards in different directions, a radial pattern."),
        ]),
        EX("Model answer 2: show the direction of flow", intro="Explain how you can tell that the R. Kuma flows from north to south-east.", steps=[
            S("Evidence: heights", text="The source is at about 480 metres. The mouth is in Lake Bimbi at 300 metres. A river flows downhill, so it flows from the source towards the lake."),
            S("Evidence: contours", text="The contour lines cross the river in V-shapes that point upstream, towards the north. Higher land lies to the north."),
            S("Evidence: tributaries", text="The tributaries join the main river in Y shapes whose stems point downstream, towards the south-east."),
        ]),
        TIP("Exam link: drainage questions are part of Paper 2 Section A (map reading and interpretation) and appear as multiple-choice "
            "questions in Paper 1. You may be asked to name a pattern, say where a river flows or describe the drainage of an area.",
            title="Exam link"),
        MISTAKE("Mixing up source, mouth and confluence",
                "A source is where a river BEGINS. A confluence is where two rivers JOIN. A mouth is where a river ENDS. Say which one you mean."),
        MISTAKE("Saying a river flows uphill",
                "Always compare the heights at the two ends. If the source is 480 metres and the mouth is 300 metres, the flow is from source to mouth."),
        QUIZ("On a map, a river flows from a place with a height of 480 metres to a place with a height of 300 metres. The place at 300 metres is the:", [
            "source", "confluence", "tributary", "mouth"], 3,
            "The river ends at the lower height. The end of a river is its mouth.",
            hint="Rivers flow downhill. Which end is the end of the river?",
            feedback=["The source is where the river begins, at the higher height.",
                      "A confluence is where two streams join.", "A tributary is a smaller stream that joins a larger one.", ""]),
        H("Practice questions"),
        PQ("In Figure 3, name the lake into which the R. Kuma flows and state its height. Which letter marks the mouth?",
           "The R. Kuma flows into Lake Bimbi. The lake is at 300 metres above sea level. The mouth is marked R."),
        PQ("Explain how the contours help you to find the direction of flow of a river.",
           "Where contours cross a river they bend into a V. The V points upstream, towards higher land. The river flows away from the point of the V, "
           "towards lower numbers. You can also compare the heights at the source and the mouth."),
        PQ("Name the three drainage patterns and describe radial drainage.",
           "The three patterns are dendritic, trellised and radial. In radial drainage streams flow outwards in all directions from a high point, such as a dome-shaped hill or a volcano, "
           "like the spokes of a wheel."),
        SUM("Drainage is made up of rivers, lakes and swamps, usually drawn in blue. A river has a source, a mouth, tributaries and confluences.",
            "Rivers flow downhill. Find the direction by comparing heights at the ends, by the V-shapes in the contours, or by the Y-shaped joins of tributaries.",
            "A swamp is wet, flat land near lakes and river mouths. A seasonal stream is shown by a broken line and flows only in the rainy season.",
            "The three patterns are dendritic (tree-like), trellised (right-angle joins) and radial (outwards from a high point).",
            "When you describe drainage, name the main river, its source and mouth, the tributaries, the lake and swamp, and the pattern."),
    ],
))

# ------------------------------------------------------------------ 3. Vegetation and land use
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Vegetation and land use on maps",
    slug="mapint-vegetation-and-land-use",
    minutes=22,
    summary="How to identify the types of vegetation and land use shown on a map, describe where they are found, and explain their distribution using relief, drainage and access.",
    objectives=[
        "Identify the types of vegetation and land use shown on a map",
        "Describe the distribution of vegetation and land uses using compass directions and place names",
        "Explain the distribution of vegetation and land use using relief, drainage and transport",
        "Outline how people use the land for farming, plantations, grazing, forestry and settlement",
    ],
    key_concepts=["Vegetation", "Land use", "Forest", "Grassland", "Plantation", "Farmland", "Swamp vegetation", "Built-up area", "Distribution"],
    blocks=[
        H("Introduction"),
        T("Travel from the south of Cameroon to the north and the plants change. Dense forest in the south gives way to tall grass and "
          "scattered trees in the Adamawa plateau and to drier grass in the far north. On the Adamawa plateau cattle are reared on the grass. "
          "Near the coast, large plantations cover flat land. In each place people use the land in the way that suits it best."),
        T("A topographic map records both. **Vegetation** is the plant cover of an area. **Land use** is what people do with the land. "
          "In map interpretation you must name each type, say where it is found and then **explain why it is there**."),
        D("**Distribution** means how something is spread out over an area. You can say it is concentrated in one part, scattered, or "
          "spread along a line such as a road or a river.", title="Distribution"),
        H("Types of vegetation and land use"),
        KEY("What you can find on a map", "Learn the colours and symbols in each map key.", cards=[
            ["Forest", "Dense trees. Shown in green with tree signs. It is usually on high, steep or wet land that is hard to farm."],
            ["Grassland", "Open grass with few trees. It is shown by tufts or pale green. It is used for grazing."],
            ["Swamp vegetation", "Reeds and grasses on wet ground, shown by blue lines with grass tufts."],
            ["Plantation", "Rows of one tree crop, such as oil palm or rubber, in neat dots. It is a large commercial farm."],
            ["Farmland", "Cultivated land with food crops, shown in yellow with crop signs."],
            ["Built-up area", "Land covered by a town or village. It is shown in black squares."],
        ]),
        D("**Land use** is the way in which people use the land: for example farming, grazing, forestry, plantations, settlement and transport.",
          title="Land use"),
        T("Some land is left in its natural state. Other land is changed for farming. On the map, the key tells you which symbol "
          "is which. Always check it before you write."),
        H("Describing distribution"),
        T("A good description follows a simple order. Name the feature. Say where it is, using compass directions and place names. "
          "Then say how it is arranged. For example: 'Forest covers the high land in the north-west, around Kuma Hill and Ekwe Hill.'"),
        TIP("Use compass points (north-west, south-east), place names (around Tabeng, near Ekum) and words like 'concentrated', 'scattered', "
            "'along' and 'beside'. 'It is in the middle' is too weak.", title="Words to use"),
        IMG("f5g-mapint-kuma-map.svg",
            alt="Topographic map of Kuma District with contours, rivers, forest, plantation, farmland, grassland, swamp, roads, railway, a market town and villages",
            caption="Figure 1. Kuma District (fictitious). Study the key before you answer."),
        EX("Model answer 1: describe the distribution of vegetation", intro="Describe the distribution of vegetation shown in Figure 1.", steps=[
            S("Forest", text="Forest is concentrated on the high land in the north-west. It covers Kuma Hill and Ekwe Hill above about 450 metres."),
            S("Grassland", text="Grassland covers the plateau in the north-east, in a compact block of high, flat land."),
            S("Swamp vegetation", text="Swamp vegetation is found in the south-east, around Lake Bimbi and the lower course of the R. Kuma."),
            S("Summary", text="So vegetation changes with height: forest on the hills, grass on the plateau and swamp plants on the low land beside the lake."),
        ]),
        EX("Model answer 2: describe land use", intro="Describe the land use in Figure 1.", steps=[
            S("Farming", text="Farmland is found in small patches on gentle slopes near villages: around Ekum in the west, near Tabeng in the centre and near Bimbi in the east."),
            S("Plantation", text="One large oil palm plantation lies on the flat land in the south-west, close to the railway."),
            S("Grazing", text="The grass of the plateau in the north-east is used for grazing. The hamlets of Fundi are small and scattered."),
            S("Built-up land", text="Tabeng is the only town. It is in the centre, at the meeting point of roads and the railway. Villages are smaller and more scattered."),
        ]),
        H("Explaining the distribution"),
        T("Describing is not enough in Section A. The question word 'explain' asks for reasons. On a map most reasons come from the "
          "physical environment and from access."),
        KEY("Four main reasons", "Link each land use to at least one reason.", cards=[
            ["Relief", "Steep slopes are hard to plough and soil is washed away, so they stay forested. Gentle slopes and flat land suit farms and plantations."],
            ["Drainage and water", "Farms like to be near rivers for water. Very wet land such as a swamp is too wet to farm and keeps its natural vegetation."],
            ["Height and climate", "High land is usually cooler and wetter. Forest grows well there. Grass grows on flat tops with thin soil."],
            ["Access", "Plantations need roads or railways to take crops to market. Farms are close to villages and towns where people live and sell."],
        ]),
        EX("Model answer 3: explain the distribution", intro="Suggest reasons for the location of the forest, the plantation and the farmland in Figure 1.", steps=[
            S("Forest on the hills", text="The slopes of Kuma Hill are steep (the contours are close together) and high, so they are hard to farm. They are left under forest."),
            S("Plantation in the south-west", text="The land is flat and low (about 330 metres), so machines and workers can use it easily. It is also near the railway, which carries the crop to market."),
            S("Farmland near villages", text="The farms are on gentle slopes close to settlements and streams. Farmers have water and do not have to carry crops far."),
            S("Swamp left alone", text="The land beside the lake is wet and flat, so it is too wet for crops. It keeps its swamp vegetation."),
        ]),
        TIP("Exam link: vegetation and land use are part of Paper 2 Section A (map reading and interpretation). Questions ask you to name, "
            "describe the distribution of, and explain land uses. Paper 1 may also test them with a map extract.", title="Exam link"),
        MISTAKE("Describing without the key",
                "Do not guess the symbol. Check the key. Forest, plantation and farmland look alike if you rush, and a wrong name loses the mark."),
        MISTAKE("Listing land uses without saying where",
                "Writing 'there is forest and farmland' gives one mark at best. Add place names and compass directions."),
        QUIZ("On the map of Kuma District the forest covers the highest hills. The best reason is that:", [
            "the land there is flat and wet", "the slopes are steep and hard to farm",
            "the hills are close to the railway", "swamps cannot grow on hills"], 1,
            "Steep slopes are hard to plough and lose soil quickly, so they are usually left under forest.",
            hint="Think about the contour spacing on the hills.",
            feedback=["The hills are steep, not flat.", "",
                      "The railway is on the low land in the south.", "This does not explain the forest, only a swamp."]),
        H("Practice questions"),
        PQ("Define land use and name three land uses shown in Figure 1.",
           "Land use is the way in which people use the land. Three land uses in Figure 1 are farming (farmland), plantation agriculture (the oil palm estate) "
           "and settlement (the town of Tabeng). Grazing on the plateau is another."),
        PQ("Describe the distribution of forest in Figure 1.",
           "Forest is concentrated in the north-west on the high land. It covers Kuma Hill and Ekwe Hill above about 450 metres. There is no forest in the south or the east."),
        PQ("Explain why the plateau in the north-east is used for grazing and not for plantations.",
           "The plateau is high and its soil is thin, with grass as the natural cover, so it suits cattle. It has few roads and no railway, "
           "so it is hard to carry plantation crops to market. Its edge is a steep escarpment, which makes access difficult."),
        PQ("Why is there no farming in the swamp beside Lake Bimbi?",
           "The swamp is low, flat and always wet because water cannot drain away. Most crops cannot grow in waterlogged soil, so the land keeps its swamp vegetation."),
        SUM("Vegetation is the plant cover. Land use is what people do with the land. On a map you find both from the key.",
            "Describe distribution with compass directions, place names and words such as concentrated or scattered.",
            "Forest is usually on high, steep land. Grassland suits plateaus and grazing. Plantations need flat land and transport.",
            "Farmland lies on gentle slopes near rivers and villages. Swamps are too wet for crops.",
            "To explain, link each land use to relief, drainage, climate or access, and use evidence from the map."),
    ],
))

# ------------------------------------------------------------------ 4. Settlement, communication, economic activity
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Settlement, communication and economic activity on maps",
    slug="mapint-settlement-communication-and-economic-activity",
    minutes=25,
    summary="How to describe the type, size, pattern, site, situation and function of settlements on a map, the distribution of roads, railways and paths, and why economic activities are found where they are.",
    objectives=[
        "Identify and describe the type, pattern, size, site, situation and function of settlements on a map",
        "Identify and describe the types and distribution of communication: roads, railways, rivers and paths",
        "Explain how relief and drainage influence the routes of roads and railways and the location of settlements",
        "Describe and explain the location of economic activities shown on a map",
    ],
    key_concepts=["Settlement", "Nucleated, linear and dispersed", "Site", "Situation", "Function", "Route centre", "Communication", "Bridging point", "Economic activity"],
    blocks=[
        H("Introduction"),
        T("Douala grew where the Wouri River meets the sea, with a port, a railway and roads that reach the rest of the country. "
          "Bamenda grew in the highlands, among farms and markets. A map does not tell us a town's story in words. "
          "But the site, the roads and the land around it let us work out why it is there."),
        T("This lesson has three linked parts: **settlement** (where people live), **communication** (the routes that join places) "
          "and **economic activity** (how people earn a living). The Board says the lesson must stress the links between the physical "
          "environment and human activities, so we keep asking: why here?"),
        H("Settlement: type, size, pattern, site, situation and function"),
        KEY("Describing a settlement", "Use these headings in every answer.", cards=[
            ["Type and size", "Rural settlements are hamlets and villages. Urban settlements are towns and cities. On a map, size shows in the number of buildings and the area they cover."],
            ["Pattern", "Nucleated: buildings are close together around a centre. Linear: buildings are in a line along a road or river. Dispersed: buildings are scattered far apart."],
            ["Site", "The actual land on which the settlement is built, for example flat land above a river, or a hilltop."],
            ["Situation", "Where the settlement lies in relation to its surroundings: hills, rivers, roads and other settlements."],
            ["Function", "The main job of the settlement, for example market town, route centre, administrative town, port or farming village."],
        ]),
        IMG("f5g-mapint-site-situation.svg",
            alt="A town on a dry terrace beside a river bridge, with roads to farming villages and a port, and forested hills to the north",
            caption="Figure 1. Site and situation of a town."),
        D("**Site** is the actual ground on which a settlement stands. **Situation** is its position in relation to the land and the routes around it.",
          title="Site and situation"),
        D("A **function** is the main activity that a settlement serves. A **route centre** is a settlement where many roads or railways meet.",
          title="Function and route centre"),
        H("Communication: roads, railways, rivers and paths"),
        KEY("Types of communication", "Check the key for the symbols.", cards=[
            ["Roads", "Tarred roads (thick line) carry the most traffic. Earth roads (thin line) join smaller places."],
            ["Railways", "A black line with cross marks. Railways need a gentle gradient, so they follow flat land."],
            ["Rivers", "Large rivers carry boats where they are wide and deep. Small rivers are crossed by bridges or fords."],
            ["Paths", "Footpaths (dotted lines) join farms and small villages. They may climb steep slopes that vehicles cannot use."],
        ]),
        T("Look at the **distribution** of communication. Are there many routes in one part and few in another? Where do routes meet? "
          "Where do they cross rivers? Where do they avoid hills?"),
        H("Economic activity: where and why"),
        T("An **economic activity** is something people do to earn a living. On a map you can see farming, plantation agriculture, grazing, "
          "forestry, fishing and trading. Each is placed where the land and the routes suit it."),
        KEY("Activity and reason", "Say where the activity is and why it is placed there.", cards=[
            ["Farming", "On gentle slopes near water and villages, with markets close by."],
            ["Plantation", "On large flat land close to a railway or road, so the crop can be moved."],
            ["Grazing", "On open grass, such as a plateau, where the land is poor for crops."],
            ["Fishing", "By a lake or river. The map may show a village beside the water, but it does not prove fishing."],
            ["Trade", "In a market town at the meeting point of roads and railways."],
        ]),
        TIP("Exam link: settlement, communication and economic activity are the human part of Paper 2 Section A (map reading and "
            "interpretation). Paper 1 may test a symbol or a pattern. Examiners reward answers that link the human features to relief and drainage.",
            title="Exam link"),
        IMG("f5g-mapint-kuma-map.svg",
            alt="Topographic map of Kuma District with roads, railway, market town, villages, farmland, plantation, grassland, forest and lake",
            caption="Figure 2. Kuma District (fictitious)."),
        EX("Model answer 1: describe the settlements", intro="Describe the settlements shown in Figure 2.", steps=[
            S("The town", text="Tabeng is the only town. It is large and nucleated, with its buildings close together, and it has a market and a railway station."),
            S("Villages and patterns", text="Njomi is a linear village, with houses in a line along the main road. Ekum is a small nucleated village in the west. "
              "Mbolo is a small village on the saddle between the two hills. Bimbi is a scattered village beside the lake. Fundi is a set of dispersed hamlets on the plateau."),
            S("Distribution", text="Most settlements lie on gentle land in the centre and south. Settlements are few on the steep hills and none are in the forest."),
        ]),
        EX("Model answer 2: site, situation and function of Tabeng", intro="Describe the site, situation and function of Tabeng.", steps=[
            S("Site", text="Tabeng stands on flat land about 333 metres above sea level, where there are no steep slopes. It is on the side of the R. Kuma and is close to the bridge."),
            S("Situation", text="It is in the centre of the district. Highland lies to the north, the plateau to the north-east and farmland and a plantation to the south. The lake is to the south-east."),
            S("Function", text="Tabeng is a market town and a route centre. The tarred road, the earth roads and the railway all meet there, and it has a station and a market."),
        ]),
        EX("Model answer 3: communication and economic activity", intro="Describe and explain the pattern of routes and the location of the plantation in Figure 2.", steps=[
            S("Railway", text="The railway runs from west to east across the flat southern lowland. It has to be level, so it avoids the hills and crosses the R. Kuma by a bridge east of Tabeng."),
            S("Roads", text="The tarred road comes from the north through the saddle between Kuma Hill and Ekwe Hill, the lowest point on the high ground. It then runs down gentle land to Tabeng. "
              "Earth roads join Tabeng to Ekum in the west and to Bimbi in the east."),
            S("Paths", text="A footpath climbs the escarpment to the plateau. Vehicles cannot use it because it is too steep."),
            S("Plantation", text="The oil palm plantation is in the flat south-west, near the railway. It is on land that is easy to work and has an easy route to market."),
        ]),
        MISTAKE("Mixing up site and situation",
                "Site is the exact ground (flat, dry, beside a river). Situation is the position in relation to other things (between hills, at a road junction). Use both words in an answer."),
        MISTAKE("Saying a village is 'nucleated' with no evidence",
                "Give the evidence: 'the buildings are close together around a centre'. For linear, say 'in a line along the road'."),
        QUIZ("A village has its houses in a line along a main road. Its pattern is:", [
            "nucleated", "dispersed", "linear", "radial"], 2,
            "Houses in a line along a road form a linear settlement.",
            hint="What is the shape of the line of buildings?",
            feedback=["Nucleated means closely grouped around a centre.", "Dispersed means scattered far apart.", "",
                      "Radial is a drainage pattern, not a settlement pattern here."]),
        H("Practice questions"),
        PQ("Distinguish between the site and the situation of a settlement.",
           "The site is the actual ground on which the settlement stands, for example flat, dry land beside a river. "
           "The situation is its position in relation to the land and routes around it, for example between hills and at a road junction."),
        PQ("Name the three patterns of rural settlement and describe linear settlement.",
           "The patterns are nucleated, linear and dispersed. In a linear settlement the houses are built in a line along a road, a river or the foot of a hill, "
           "like Njomi in Figure 2."),
        PQ("Explain why the railway in Figure 2 runs across the southern lowland and not over the hills.",
           "A railway needs a very gentle gradient because trains cannot climb steep slopes. The southern lowland is almost flat, so the railway can be built there easily. "
           "The hills in the north are steep and would need tunnels or long detours."),
        PQ("Give two reasons why Tabeng has grown into the main market town.",
           "It stands on flat land near a bridge over the R. Kuma, so it has good site conditions. It lies at the meeting point of the road and the railway, "
           "so traders and farmers from the whole district can reach its market."),
        SUM("Describe a settlement by its type, size, pattern (nucleated, linear, dispersed), site, situation and function.",
            "Site is the actual ground. Situation is the position in relation to land and routes. Function is the main job of the place.",
            "Roads and railways follow gentle land, valleys and saddles and cross rivers by bridges. They avoid steep slopes.",
            "Economic activities are located where land, water and routes suit them, for example plantations on flat land near a railway.",
            "Always link human features to relief and drainage, and use map evidence."),
    ],
))

# ------------------------------------------------------------------ 5. Sketch maps and linking features
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Sketch maps and linking physical and human features",
    slug="mapint-sketch-maps-and-linking-features",
    minutes=25,
    summary="How to draw a clear sketch map with a frame, title, north arrow, scale and key, and how to write a full Section A answer that links relief and drainage to settlement, communication and economic activity.",
    objectives=[
        "Draw a sketch map to illustrate the distribution of physical and human features, with frame, title, key, north and scale",
        "Show only the features that the question asks for, in their correct positions",
        "Explain how relief and drainage influence settlement, communication, vegetation and land use",
        "Write a structured Section A answer using point, evidence and explanation",
    ],
    key_concepts=["Sketch map", "Frame", "Key", "Scale", "Distribution", "Link between features", "Point, evidence, explanation"],
    blocks=[
        H("Introduction"),
        T("Section A of Paper 2 is the map reading and interpretation question. It is compulsory, and it carries about a quarter of "
          "all the marks in the whole examination. That makes it one of the best places to gain marks."),
        T("The question often asks you to **draw a sketch map** of part of the map and then to **link** the physical environment to "
          "human activities. This lesson shows you how to do both, using the fictitious Kuma District."),
        H("What is a sketch map?"),
        D("A **sketch map** is a simple drawing of part of a map. It shows only the features that the question asks for, in their "
          "correct positions, with a frame, a title, a north arrow, a scale and a key.", title="Sketch map"),
        T("A sketch map is not a copy of the whole map. It is not a work of art. The examiner looks for correct positions, clear lines "
          "and a complete key. Extra features that were not asked for waste your time and can lose marks."),
        H("Six steps to a good sketch map"),
        KEY("Draw it in this order", "Use a pencil first, then ink the lines you want to keep.", cards=[
            ["1. Frame", "Draw a rectangle with the same shape as the area you are asked to draw. Use a simple proportion such as 8 cm by 6 cm."],
            ["2. Title", "Write a short title above the frame that says what the sketch shows."],
            ["3. North and scale", "Draw a north arrow. Give a scale line or a statement such as 'about 1 : 50 000'."],
            ["4. Features", "Draw only the features asked for, starting with the biggest: highland, river, lake, then roads and settlements."],
            ["5. Key", "Make a box with a symbol and a name for every feature you drew."],
            ["6. Labels", "Name the main features directly on the sketch. Write horizontally and keep labels short."],
        ]),
        IMG("f5g-mapint-sketch-example.svg",
            alt="A model sketch map of Kuma District with frame, title, north arrow, scale, key and labels numbered one to six",
            caption="Figure 1. A model sketch map of Kuma District: relief, river, lake, town and railway."),
        TIP("Copy positions with light grid lines. Divide your frame into squares that match the grid on the map. Then place each feature in the same square.",
            title="Placing features correctly"),
        H("Linking the physical environment to human activity"),
        T("The Board says the lessons must stress the links between the physical environment and human activities. In an answer, "
          "a link has three parts: the **point**, the **evidence** from the map and the **explanation**."),
        KEY("Common links", "Use these as starting points. Always add map evidence.", cards=[
            ["Steep slopes", "Forest or grassland, not farms. Roads wind around them or use saddles."],
            ["Flat land", "Plantations, farms, towns and railways."],
            ["Rivers", "Water for farms and villages. Bridges and bridging-point towns. Rivers also divide land and need bridges."],
            ["Swamps", "Few buildings and no crops, because the ground is wet."],
            ["Plateaus", "Grazing on grass. Few roads, and steep edges to climb."],
            ["Lakes", "Fishing villages and water supply."],
        ]),
        T("Write each link as a short chain: 'The land is flat (evidence), so a railway is easy to build (explanation).' "
          "Use linking words such as because, so, therefore and as a result."),
        EX("Model answer plan 1: describe and link", intro="Describe the relief and drainage of Kuma District and explain how they affect settlement and communication.", steps=[
            S("Paragraph 1: relief", text="High land in the north-west (Kuma Hill 706 metres) and north-east (plateau, trig 586 metres). The land falls south-east to Lake Bimbi at 300 metres. The south is low and gentle."),
            S("Paragraph 2: drainage", text="The R. Kuma flows from a source at about 480 metres south-east to Lake Bimbi. Its tributaries (R. Njuni, R. Ngom, R. Ewe, R. Ebo) join it in a dendritic pattern. A swamp lies around the lake."),
            S("Paragraph 3: link to settlement", text="Settlements lie on the gentle land of the centre and south, not on the steep hills or in the swamp. Tabeng is on flat land near a bridge over the R. Kuma, so it grew into the market town."),
            S("Paragraph 4: link to communication", text="The tarred road uses the saddle between Kuma Hill and Ekwe Hill and runs down to Tabeng. The railway crosses the flat lowland. Rivers are crossed by bridges. Paths climb the steep escarpment to the plateau."),
            S("Conclusion", text="The pattern of settlement and routes follows the relief and drainage: people live and build on the gentle, dry land and avoid the steep and wet land."),
        ]),
        EX("Model answer plan 2: sketch map and comment", intro="Draw a sketch map of Kuma District to show the land above 500 metres, the R. Kuma, Lake Bimbi, the railway and Tabeng. Then comment on the distribution of economic activities.", steps=[
            S("Draw the frame and title", text="Draw a rectangle in the proportion of the map (about 9 by 6). Write 'Kuma District: relief, river and town' above it. Add a north arrow and a scale line."),
            S("Draw the features asked", text="Shade the land above 500 metres in the north-west and north-east. Draw the R. Kuma from the north to the lake in the south-east. Draw the lake, the railway from west to east and a square for Tabeng."),
            S("Add key and labels", text="Make a key for the shading, river, lake, railway and town. Label Kuma Hill, the plateau, the R. Kuma and Lake Bimbi."),
            S("Comment on activities", text="Farming and the plantation are concentrated on the flat south and centre, near Tabeng and the railway. Grazing is on the plateau in the north-east. "
              "The steep hills in the north-west are left under forest. The activities are placed where the relief allows and where there is access."),
        ]),
        TIP("Exam link: this is the whole of Paper 2 Section A. The question may start with short parts (heights, features, drainage) and "
            "end with a sketch map or a longer 'describe and explain' part. Paper 1 map-skills questions test the same ideas in short form.",
            title="Exam link"),
        MISTAKE("Drawing every feature on the map",
                "A sketch map shows only what the question asks. If you add extra features, you waste time and the sketch becomes crowded."),
        MISTAKE("Forgetting the key, the title or north",
                "Each missing part costs marks. Draw the frame, then add the title, north arrow, scale and key before you draw the features."),
        MISTAKE("Describing without explaining",
                "'There is forest in the north-west' is a description. 'The slopes are steep, so they are hard to farm and stay forested' is an explanation. Do both."),
        QUIZ("Which of these is NOT needed on a sketch map?", [
            "A title", "A key", "Every feature shown on the original map", "A north arrow"], 2,
            "A sketch map shows only the features that the question asks for.",
            hint="Think about the word 'only' in the definition of a sketch map.",
            feedback=["A title is needed.", "A key is needed.", "", "A north arrow is needed."]),
        QUIZ("Which sentence links a physical feature to a human activity?", [
            "The R. Kuma flows south-east.",
            "Kuma Hill is 706 metres high.",
            "The railway crosses the flat lowland because trains need gentle slopes.",
            "There is a lake in the south-east."], 2,
            "This sentence gives a physical feature (flat lowland), a human feature (railway) and a reason (trains need gentle slopes).",
            hint="Look for a reason that joins a human feature to the land.",
            feedback=["This describes only a physical feature.", "This describes only a physical feature.", "",
                      "This describes only a physical feature."],
            title="Quick check 2"),
        H("Practice questions"),
        PQ("List the six parts of a good sketch map in the order you would draw them.",
           "Frame, title, north arrow and scale, the features asked for, the key, and the labels."),
        PQ("Why should a sketch map show only the features asked for in the question?",
           "The examiner is testing whether you can pick out and place the features named in the question. Extra features waste time, crowd the sketch "
           "and make the important ones hard to see."),
        PQ("Write one sentence linking a swamp to human activity, using the form: feature, evidence, explanation.",
           "The land around Lake Bimbi is low and flat with swamp symbols (evidence), so it is too wet for buildings and crops (explanation) and few people live on it."),
        PQ("Explain why the main road in Kuma District runs through the saddle between Kuma Hill and Ekwe Hill.",
           "The saddle is the lowest point on the line of high ground (about 564 metres), so a road climbs less there than over either hill. "
           "It is a natural pass that gives the shortest and easiest route to the north."),
        SUM("A sketch map is a simple drawing of part of a map. It shows only the features asked for, in their correct positions.",
            "Draw the frame first. Add the title, north arrow, scale, features, key and labels.",
            "Link physical features to human activities in three parts: point, evidence from the map, explanation.",
            "Steep land stays forested or grassed, flat land is used for farms, plantations and railways, rivers need bridges and swamps stay empty.",
            "Section A is compulsory and carries about a quarter of the marks, so practise describing and explaining with maps."),
    ],
))
