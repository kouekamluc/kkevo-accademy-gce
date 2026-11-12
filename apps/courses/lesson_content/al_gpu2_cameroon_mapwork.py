"""A Level Geography (0750), Upper Sixth: Comprehensive Geography of Cameroon and Practical Geography I (Map Work).

KKEVO draft for reviewer checking against the Board syllabus and textbooks. The map extracts (Map A: Kemo area,
Map B: R. Mewa basin) are invented; every height, distance, gradient, vertical exaggeration, stream order,
bifurcation ratio, drainage density and sinuosity value was computed by script from the same data that drew the maps.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "upper-sixth")

M_CMR = "Comprehensive Geography of Cameroon"
M_MAP = "Practical Geography I: Map Work"

MAP_A = "algpu2-map-a.svg"
MAP_A_ALT = ("Invented 1:50 000 map of the Kemo area (eastings 30-37, northings 60-65, contours every 50 m): western plateau with "
             "summit A (1298) and col C, escarpment near easting 33 with point E and a waterfall, R. Kemo meandering east past Kemo "
             "village and swamp, hill D (955), point B (817), section line X-Y.")

LESSONS = []

# ---------------------------------------------------------------------------
# 1. Relief and structure of Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Relief and structure of Cameroon",
    title="Relief and structure: the morphostructural regions of Cameroon",
    slug="gpu2-relief-and-structure-of-cameroon",
    minutes=24,
    summary="How the old crystalline basement, the sedimentary basins and the Cameroon Volcanic Line explain the main relief regions of Cameroon, and how to describe each region by height, gradient and landforms.",
    objectives=[
        "Explain the three main structural units of Cameroon: basement, sedimentary basins and volcanic rocks",
        "Describe each morphostructural region by height, slope, landforms and rock type",
        "Explain the origin and features of the Cameroon Volcanic Line, including its hazards",
        "Write a structured Paper 3 answer that links relief to structure with named examples",
    ],
    key_concepts=["Structure", "Morphostructural region", "Precambrian basement", "Sedimentary basin", "Cameroon Volcanic Line", "Escarpment", "Inselberg"],
    blocks=[
        H("Introduction"),
        T("At O Level you learned the names and positions of Cameroon's relief units. At A Level the question is **why** "
          "the land has this shape. The answer lies in the rocks underneath (the **structure**) and in the long history of "
          "uplift, faulting, volcanic activity and erosion that shaped them."),
        T("The 2023 Board report on Paper 3 noted that many candidates could name the relief regions crossed by the "
          "Cameroon Volcanic Line but could not describe their characteristics: height, gradient and landforms. This lesson "
          "trains exactly that skill."),
        D("**Structure** is the type, age and arrangement of the rocks under an area: whether they are old crystalline rocks, "
          "layered sediments or volcanic rocks, and whether they are folded, faulted or flat.", title="Structure"),
        D("A **morphostructural region** is an area whose relief (morphology) is explained by one dominant structure, for "
          "example a high plateau of old crystalline rocks, or a lowland floored by young sediments.", title="Morphostructural region"),
        H("The three structural building blocks"),
        KEY("Structure of Cameroon", "Most of the country rests on very old rocks; younger rocks lie on top in a few places.", cards=[
            ["Precambrian basement", "Very old crystalline rocks (granite, gneiss, schist), more than about 540 million years old. They underlie most of the country: the South Cameroon plateau, much of the Adamawa and the western highlands."],
            ["Sedimentary basins", "Younger layered rocks in hollows of the basement: the coastal basins (Douala, Kribi-Campo, Rio del Rey), the Benue trough around Garoua (Cretaceous) and the Chad basin (mostly recent sands and clays)."],
            ["Volcanic rocks", "Basalts and related lavas of the Cameroon Volcanic Line and the Adamawa, mostly much younger (Tertiary to present). They build Mount Cameroon, the Manengouba, Bamboutos and Oku mountains and the basalt cover around Ngaoundéré."],
        ]),
        IMG("algpu2-cmr-profile.svg",
            alt="Schematic south to north profile of Cameroon: coastal plain on sediments at Douala, South Cameroon plateau on basement at Yaoundé, high Adamawa plateau with basalt cap at Ngaoundéré between escarpments, Benue lowland on sediments at Garoua, Chad plain on sediments",
            caption="Figure 1. A schematic south to north profile. Plateaus stand on hard basement; lowlands sit on softer sedimentary basins. Not to scale."),
        H("The morphostructural regions"),
        KEY("Southern and central regions", "Describe each with height, slope, landforms and rock.", cards=[
            ["Coastal lowlands", "Low (mostly below about 200 m), flat to gently sloping, with estuaries, creeks and mangrove swamps (Wouri, Rio del Rey). Floored by sediments of the coastal basins."],
            ["South Cameroon plateau", "The largest region; an undulating surface at roughly 600 to 900 m (check your textbook), on basement rocks. Isolated rocky hills (inselbergs) rise above it, for example around Yaoundé. Rivers form rapids and falls where they drop off its edges."],
            ["Adamawa plateau", "A high plateau at roughly 1,000 to 1,500 m (check your textbook) crossing the country near 6 to 8° N. Basement rocks with a basalt cover; bounded by steep escarpments, especially on the north side facing the Benue lowland. It is the main water divide."],
        ]),
        KEY("Western and northern regions", "These are the regions most often confused in answers.", cards=[
            ["Western highlands", "A belt of high plateaus and volcanic mountains (Bamileke and Bamenda plateaus; Manengouba, Bamboutos and Oku mountains, Oku being close to 3,000 m). Granite basement with volcanic rocks on top; deep valleys, crater lakes, steep slopes."],
            ["Mount Cameroon", "An active volcano on the coast, about 4,100 m high (textbook figures differ slightly): the highest point in Cameroon. Basaltic lava flows; fertile volcanic soils on its lower slopes."],
            ["Northern lowlands and Mandara", "The Benue lowland (roughly 200 to 400 m) and the Chad plain (around 300 m) are flat sedimentary lowlands. The Mandara mountains on the Nigerian border are granite and volcanic hills with many inselbergs and volcanic necks."],
        ]),
        H("The Cameroon Volcanic Line"),
        T("The **Cameroon Volcanic Line** is a straight chain of volcanoes running south-west to north-east. It begins with the "
          "islands of the Gulf of Guinea (Annobón, São Tomé, Príncipe and Bioko), reaches the mainland at Mount Cameroon and "
          "continues through the Manengouba, Bamboutos and Oku mountains towards the Adamawa. Because it crosses both ocean and "
          "continent, geologists use it to study how volcanoes form inside a plate, far from a plate boundary."),
        IMG("algpu2-cmr-cvl.svg",
            alt="Schematic of the Cameroon Volcanic Line: volcanic islands Annobón, São Tomé, Príncipe and Bioko in the Gulf of Guinea, then Mount Cameroon on the coast and Manengouba, Bamboutos, Oku and the Adamawa volcanoes inland, along a south-west to north-east line",
            caption="Figure 2. The Cameroon Volcanic Line has an oceanic sector and a continental sector. Schematic, not to scale."),
        T("Its origin is still debated. Explanations include a mantle **hot spot**, melting along old lines of weakness (shear "
          "zones) in the crust, and small-scale movements in the upper mantle. Notice that there is no clear age order along "
          "the line, which is a problem for the simple hot-spot idea. Say that the origin is debated; do not present one theory "
          "as proven."),
        KEY("Effects of the Volcanic Line on people", "A balanced answer gives resources and hazards.", cards=[
            ["Resources", "Fertile volcanic soils (plantations around Mount Cameroon, intensive farming in the western highlands); cool healthy climate; crater lakes and scenery for tourism (Mount Cameroon race, Lake Barombi Mbo, Manengouba twin lakes); building stone."],
            ["Hazards", "Lava flows (Mount Cameroon erupted in 1999 and 2000, among other dates); landslides on steep slopes; dangerous gas releases from crater lakes: the Lake Nyos disaster of August 1986 killed about 1,700 people when carbon dioxide escaped from the lake."],
        ]),
        EX("Worked example 1: describe a region the way examiners want", intro="Describe the relief of the Adamawa plateau.", steps=[
            S("Location", text="A high plateau across the centre of Cameroon, roughly between 6° and 8° N, from the western highlands to the eastern border; Ngaoundéré lies on it."),
            S("Height", text="Mostly about 1,000 to 1,500 m, much higher than the South Cameroon plateau to the south and the Benue lowland to the north."),
            S("Gradient and edges", text="The surface is gently undulating, but the edges are steep escarpments, especially the northern edge that drops sharply to the Benue lowland."),
            S("Landforms and rock", text="Basalt-covered surfaces, volcanic cones and crater lakes on old basement rocks; many rivers rise here and flow outwards in all directions, so it is the main water divide."),
        ]),
        EX("Worked example 2: link relief to structure", intro="Explain why the Benue lowland is low and flat while the Adamawa plateau to its south is high.", steps=[
            S("Structure of the Benue lowland", text="It lies in the Benue trough, a long hollow in the basement that sank (rift-like subsidence) and was filled with Cretaceous sediments."),
            S("Erosion", text="These sediments are softer than the basement and have been worn down to a low, flat plain drained by the Benue."),
            S("Structure of the Adamawa", text="The Adamawa is made of resistant basement rocks, uplifted and partly capped by hard basalt that protects the surface from erosion."),
            S("Conclusion", text="So the contrast is structural: hard, uplifted rocks form the plateau; a down-faulted basin of softer rocks forms the lowland. The escarpment marks the boundary."),
        ]),
        TIP("In the 2023 Board report, Paper 3 was described as having a compulsory map work question (Section A), fieldwork and "
            "techniques (Section B) and four questions on the geography of Cameroon (Section C). Relief and structure can appear "
            "in Section C, often joined with another theme such as farming. It can also appear in Paper 1 multiple-choice questions.",
            title="Exam link"),
        MISTAKE("Naming regions without describing them", "The report says candidates gave 'bare knowledge'. For every region give height, gradient (gentle, steep, escarpment), landforms (inselbergs, craters, plains) and rock type."),
        MISTAKE("Calling the Volcanic Line a plate boundary", "The Cameroon Volcanic Line lies inside the African plate. Its origin is debated (hot spot, shear zones); it is not a subduction zone or a mid-ocean ridge."),
        MISTAKE("Mixing up Mount Cameroon and Mount Oku", "Mount Cameroon is the active volcano on the coast (about 4,100 m). Oku is the high massif in the North-West highlands (close to 3,000 m)."),
        QUIZ("Which region of Cameroon is mainly floored by Cretaceous sedimentary rocks in a down-faulted hollow?",
             ["The South Cameroon plateau", "The Benue lowland", "The western highlands", "The Adamawa plateau"], 1,
             "The Benue lowland lies in the Benue trough, a sunken basin filled with Cretaceous sediments.",
             hint="Think of the region named after a trough.",
             feedback=["The South Cameroon plateau is on old basement rocks.", "", "The western highlands are basement and volcanic rocks.", "The Adamawa is uplifted basement with basalt."]),
        QUIZ("Why is it wrong to call the Cameroon Volcanic Line a plate boundary?",
             ["It has no active volcanoes", "It lies inside the African plate, away from plate margins", "It runs north to south", "It is made of sedimentary rocks"], 1,
             "The line crosses the interior of the African plate; that is why its origin is debated.",
             feedback=["Mount Cameroon is active.", "", "It runs south-west to north-east.", "It is made of volcanic rocks such as basalt."]),
        PQ("Identify one highland and one lowland crossed by or next to the Cameroon Volcanic Line and describe the characteristics of the lowland.",
           "Highland: the western highlands (Bamboutos, Oku) or Mount Cameroon. Lowland: the coastal lowland around Douala and the Rio del Rey area. "
           "Characteristics: low (mostly below about 200 m), flat or gently sloping; estuaries, creeks and mangrove swamps; floored by sediments of the coastal basins; "
           "poorly drained in places and subject to flooding; rivers such as the Wouri and Mungo reach the sea here."),
        PQ("Explain how structure influences relief in Cameroon. Use three examples.",
           "Model plan. (1) Resistant basement uplifted forms plateaus: the South Cameroon plateau with inselbergs of granite. "
           "(2) Down-faulted basins filled with softer sediments form lowlands: the Benue lowland and the Chad plain. "
           "(3) Volcanic activity builds mountains and plateaus: Mount Cameroon, the Bamboutos and Oku, and basalt-capped surfaces of the Adamawa. "
           "Evaluation: structure is not the only control; climate and long periods of erosion have also shaped the surfaces (for example inselbergs left above planed surfaces)."),
        PQ("Assess the advantages and disadvantages of the Cameroon Volcanic Line for human activities.",
           "Model plan. Advantages: fertile volcanic soils (plantations of banana, oil palm, rubber and tea around Mount Cameroon; dense farming in the western highlands); "
           "cool climate; tourism (mountain race, crater lakes); building materials. Disadvantages: eruptions (1999, 2000 on Mount Cameroon), landslides on steep slopes, "
           "gas disasters (Lake Nyos 1986), difficult road building. Judgement: the benefits are felt every year, the hazards are rare but severe, so monitoring and planning are essential."),
        SUM("Cameroon's relief reflects three structures: Precambrian basement, younger sedimentary basins and volcanic rocks.",
            "Plateaus (South Cameroon, Adamawa) stand on resistant basement; lowlands (coast, Benue, Chad) sit on sedimentary basins.",
            "The Cameroon Volcanic Line runs SW to NE from the Gulf of Guinea islands through Mount Cameroon to the Adamawa; its origin is debated.",
            "Describe every region with height, gradient, landforms and rock type, not just its name.",
            "Volcanic areas bring fertile soils and tourism but also eruptions, landslides and gas disasters."),
    ],
))

# ---------------------------------------------------------------------------
# 2. Climate, vegetation and soils of Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Climate, vegetation and soils of Cameroon",
    title="Climate, vegetation and soils: controls, sub-climates and zonal patterns",
    slug="gpu2-climate-vegetation-and-soils-of-cameroon",
    minutes=25,
    summary="Why Cameroon's climate changes from wet equatorial in the south to semi-arid in the far north, how altitude creates highland sub-climates, and how vegetation and soils follow these climatic zones.",
    objectives=[
        "Explain the controls of Cameroon's climate: latitude, the ITCZ, the monsoon and harmattan air masses, relief and the ocean",
        "Contrast the main climatic types and sub-climates, including the South Cameroon plateau and the Adamawa",
        "Relate the vegetation zones to climate and human use",
        "Describe the main zonal and azonal soils, including the ferrallitic soils of the south",
    ],
    key_concepts=["ITCZ", "Monsoon", "Harmattan", "Sub-climate", "Orographic rainfall", "Ferrallitic soil", "Zonal soil", "Azonal soil"],
    blocks=[
        H("Introduction"),
        T("Douala may receive rain in most months, while Kousseri near Lake Chad has a short rainy season and a long, hot, dusty "
          "dry season. A single country stretching from about 2° N to 13° N contains almost every tropical climate. At A Level "
          "you must explain the **controls** of these climates, describe **sub-climates** precisely, and link climate to "
          "vegetation and soils."),
        D("The **Inter-Tropical Convergence Zone (ITCZ)** is the belt near the equator where the north-east and south-east trade "
          "winds meet. Air rises there, so it brings cloud and rain. It moves north and south with the overhead sun.", title="ITCZ"),
        D("Over Cameroon two air masses meet at the ITCZ: the **monsoon** (moist south-westerly air from the Atlantic, rainy) "
          "and the **harmattan** (dry north-easterly trade wind from the Sahara, dusty).", title="Monsoon and harmattan"),
        H("The controls of Cameroon's climate"),
        IMG("algpu2-cmr-itcz.svg",
            alt="Two panels. January: the ITCZ lies near the coast, dry north-easterly harmattan covers most of Cameroon, moist air only in the far south. July: the ITCZ lies north of Cameroon and moist south-westerly monsoon air covers the whole country.",
            caption="Figure 1. The seasonal shift of the ITCZ. Positions are approximate (check your textbook)."),
        KEY("Five controls", "Use these to explain any climate pattern in Cameroon.", cards=[
            ["Latitude", "Close to the equator in the south: high sun all year, high temperatures and two rain maxima. Further north the sun's seasonal swing gives one rainy season."],
            ["ITCZ and air masses", "When the ITCZ is north (about June to September) monsoon air covers the country and it rains. When it moves south (about December to February) the harmattan brings the dry season, longest in the north."],
            ["Relief", "Altitude lowers temperature (the average environmental lapse rate is about 6.5 °C per 1,000 m). Windward slopes facing the monsoon receive orographic rain; leeward areas are drier."],
            ["Ocean and distance from the sea", "Coastal areas are humid with a small temperature range. The interior north has a larger daily and annual range."],
            ["Local factors", "Forest cover, lakes and towns modify local climates: for example cities such as Douala and Yaoundé are warmer than their surroundings (urban heat island)."],
        ]),
        H("Climatic types and sub-climates"),
        KEY("From south to north", "Rainfall decreases and the dry season lengthens northwards; highlands are cooler.", cards=[
            ["Equatorial (Guinean) type", "South Cameroon plateau (Yaoundé, Ebolowa, Bertoua): rain in most months with two rainy and two drier seasons; about 1,500 to 2,000 mm; temperatures about 23 to 26 °C with a small annual range."],
            ["Cameroon (coastal monsoon) type", "Coast and Mount Cameroon (Douala, Limbe, Debundscha): one very long rainy season and very high totals; Debundscha on the windward foot of Mount Cameroon is often quoted among the wettest places on Earth (check the figure in your textbook)."],
            ["Highland (mountain) type", "Western highlands and Adamawa (Bamenda, Dschang, Ngaoundéré): rainfall pattern of the latitude, but cooler (often below 20 °C on average) because of altitude."],
            ["Sudan (tropical) type", "Benue lowland (Garoua): one rainy season of about five to six months; hot, especially before the rains; about 1,000 mm (check your textbook)."],
            ["Sahel (semi-arid) type", "Far North (Maroua, Kousseri): short rainy season of about three to four months; under about 800 mm; very hot; large temperature range; frequent drought."],
        ]),
        EX("Worked example 1: contrast two sub-climates", intro="Contrast the climate of the South Cameroon plateau with that of the Adamawa plateau.", steps=[
            S("Rainfall regime", text="South Cameroon plateau: two rainy seasons separated by a short dry season, because the ITCZ passes over twice a year. Adamawa: one rainy season, roughly April to October, and one dry season, because it lies further north."),
            S("Rainfall totals", text="Both are fairly wet (roughly 1,500 mm or more), but the dry season is longer and drier on the Adamawa because the harmattan reaches it for several months."),
            S("Temperature", text="The South Cameroon plateau (about 600 to 900 m) is warm all year, about 24 °C. The Adamawa (about 1,000 to 1,500 m) is cooler, especially at night in the dry season, because of altitude."),
            S("Range and humidity", text="Small annual range and high humidity in the south; larger daily range and lower humidity on the Adamawa in the dry season."),
            S("Explain, then conclude", text="Latitude explains the rainfall regime; altitude explains the lower temperatures. This is the precise contrast the 2023 report said many candidates failed to give."),
        ]),
        H("Vegetation zones"),
        KEY("Climate and vegetation", "Each zone reflects rainfall, the length of the dry season, altitude and human use.", cards=[
            ["Dense rainforest", "South and East: tall evergreen trees in layers, great biodiversity (Dja reserve, a UNESCO World Heritage Site). Mangroves along creeks and estuaries of the coast."],
            ["Forest-savanna mosaic", "A transition zone on the northern edge of the forest (roughly the Centre and East around 4 to 6° N) where fire and farming push savanna into the forest."],
            ["Guinea and Sudan savanna", "Adamawa and Benue: tall grasses with scattered trees that resist fire and drought; grazed by cattle."],
            ["Sahel savanna (steppe)", "Far North: short grasses, thorny trees such as acacias; very sensitive to overgrazing and drought."],
            ["Montane vegetation", "Western highlands and Mount Cameroon: montane forest (for example Kilum-Ijim on Oku) and highland grassland, much of it cleared for farming and grazing."],
        ]),
        H("Soils"),
        D("A **zonal soil** reflects the climate and vegetation of its zone. An **azonal** (or intrazonal) soil is controlled mainly by "
          "parent rock or drainage, so it can occur in any climate zone.", title="Zonal and azonal soils"),
        KEY("Main soils of Cameroon", "Name the soil, its process and its use.", cards=[
            ["Ferrallitic soils (zonal, south)", "Deep red or yellow soils of the South Cameroon plateau. Heavy rain and high temperatures cause intense chemical weathering and leaching: silica and bases are removed, iron and aluminium oxides remain. Acidic and poor in nutrients once the forest is cleared."],
            ["Tropical ferruginous soils (zonal, north)", "Savanna soils of the Benue and Adamawa margins: less leached, with a dry-season crust; moderately fertile but easily eroded."],
            ["Volcanic soils (azonal)", "Young, dark, fertile soils on basalt and ash around Mount Cameroon and in the western highlands; support plantations and intensive food farming."],
            ["Hydromorphic and vertisol soils (azonal)", "Waterlogged soils of swamps and flood plains (Logone flood plain, Ndop plain). Black cracking clays (vertisols, locally called karal) in the Far North are used for dry-season sorghum (muskwari)."],
        ]),
        EX("Worked example 2: explain a zonal soil", intro="Examine the characteristics of the zonal soil of the South Cameroon plateau.", steps=[
            S("Name it", text="Ferrallitic (lateritic) soil, the zonal soil of the humid equatorial south."),
            S("Process", text="High temperatures and heavy rain all year cause deep chemical weathering of the basement rocks and strong leaching (ferrallitisation)."),
            S("Characteristics", text="Very deep profile; red or yellow colour from iron oxides; clay-rich but with low nutrient content; acidic; thin humus layer under forest; can harden into laterite crusts if exposed."),
            S("Use and management", text="Fertile only while the forest cycles nutrients; after clearing, yields fall within a few years, which explains bush fallowing and the use of tree crops such as cocoa."),
        ]),
        MISTAKE("Describing 'the climate of Cameroon' in general", "The 2023 report criticised answers that generalised about major climates when a question named two sub-regions. Give the regime, totals, temperatures and range for each named region."),
        MISTAKE("Explaining highland coolness by latitude", "The western highlands and the Adamawa are cool because of altitude (lapse rate), not because they are further north."),
        MISTAKE("Calling all red soils 'laterite'", "Laterite is a hardened crust of iron oxides. Ferrallitic soil is the whole leached soil; it may contain a laterite layer."),
        QUIZ("What mainly causes the dry season in northern Cameroon?",
             ["The cool Benguela current reaching the coast", "The harmattan, as the ITCZ moves south", "Heavy orographic rain on the Adamawa", "Leaching of ferrallitic soils"], 1,
             "When the ITCZ moves south, dry north-easterly harmattan air from the Sahara covers the north for many months.",
             feedback=["This affects the coast, not the dry season of the north.", "", "Orographic rain makes places wetter, not drier.", "Leaching is a soil process, not a cause of climate."]),
        QUIZ("Why are volcanic soils around Mount Cameroon called azonal?",
             ["They are found only in the Sahel zone", "They are controlled mainly by parent rock rather than by climate", "They are the most leached soils", "They are always waterlogged"], 1,
             "Their character comes from young basalt and ash parent material, so they can occur in different climatic zones.",
             feedback=["They are found in the humid south-west.", "", "Young volcanic soils are less leached and more fertile.", "That describes hydromorphic soils."]),
        PQ("Contrast the climatic characteristics of the South Cameroon plateau and the Adamawa plateau.",
           "South Cameroon plateau: two rainy seasons; about 1,500 to 2,000 mm; warm all year (about 24 °C); small range; humid. "
           "Adamawa: one rainy season (about April to October) and a long dry season under the harmattan; cooler because of altitude; larger daily range. "
           "Explanation: latitude controls the regime; altitude controls temperature."),
        PQ("Explain why Debundscha, at the foot of Mount Cameroon, receives much more rain than Garoua.",
           "Debundscha is on the coast, facing the moist south-west monsoon, which is forced to rise up Mount Cameroon (orographic uplift): heavy rain for most of the year. "
           "Garoua is far inland in the north, reached by monsoon air for only about five to six months, and lies in a lowland without strong uplift; the harmattan dominates the rest of the year."),
        PQ("Examine the relationship between climate, vegetation and soils from the south to the north of Cameroon.",
           "Model plan. South: hot and wet all year, dense rainforest, deep leached ferrallitic soils (nutrients held in the vegetation). "
           "Centre: longer dry season, forest-savanna mosaic, ferrallitic to ferruginous soils. North: one short rainy season, Sudan then Sahel savanna, ferruginous soils, vertisols in hollows. "
           "Evaluation: relief (highlands) and human activity (burning, grazing, farming) modify the pattern, so the zones are not perfectly regular."),
        SUM("The ITCZ, the monsoon and the harmattan control the rainy and dry seasons; latitude and relief modify them.",
            "Rainfall decreases and the dry season lengthens from the south (two rainy seasons) to the north (one short rainy season).",
            "Highlands are cooler because of altitude; windward slopes such as Mount Cameroon are among the wettest places on Earth.",
            "Vegetation changes from rainforest and mangroves to savanna and Sahel steppe, with montane vegetation on highlands.",
            "Ferrallitic soils dominate the south; volcanic, hydromorphic and vertisol soils are azonal, set by rock or drainage."),
    ],
))

# ---------------------------------------------------------------------------
# 3. Drainage of Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Drainage of Cameroon",
    title="Drainage of Cameroon: basins, regimes and river use",
    slug="gpu2-drainage-of-cameroon",
    minutes=22,
    summary="The four drainage basins of Cameroon, how the Adamawa plateau acts as the main water divide, how river regimes differ between south and north, and how rivers are used and managed, including flood control.",
    objectives=[
        "Name and locate the four drainage basins and their main rivers",
        "Explain why the Adamawa plateau is the main water divide",
        "Contrast the regime of a southern river with that of a northern river",
        "Evaluate the benefits and problems of river use, including dams and floods",
    ],
    key_concepts=["Drainage basin", "Water divide", "River regime", "Hydroelectric power", "Flood plain", "Inland drainage"],
    blocks=[
        H("Introduction"),
        T("Rain that falls on the Adamawa plateau can end up in four different places: the Atlantic Ocean, the River Niger, "
          "Lake Chad or the River Congo. This is one reason why Cameroon is sometimes called the 'water tower' of the region. "
          "Understanding the drainage of Cameroon helps you explain where electricity, irrigation water and floods come from."),
        D("A **drainage basin** is the whole area drained by a river and its tributaries. A **water divide** (watershed) is the high ground "
          "separating one drainage basin from another.", title="Drainage basin and water divide"),
        H("The four drainage basins"),
        IMG("algpu2-cmr-basins.svg",
            alt="Schematic of the four drainage basins of Cameroon: Niger basin (Benue, Faro, Mayo Kebi), Lake Chad basin (Logone, Chari), Atlantic basin (Sanaga, Nyong, Ntem, Wouri, Mungo) and Congo basin (Dja, Boumba, Kadei, Ngoko to the Sangha), arranged around the Adamawa water divide",
            caption="Figure 1. The four drainage basins. The boxes show direction of flow, not exact areas. Schematic."),
        KEY("Basins and main rivers", "Learn at least two rivers for each basin.", cards=[
            ["Atlantic basin", "The largest and most important. Rivers flow south-west or west to the sea: Sanaga (the longest river wholly within Cameroon, about 900 km: check your textbook), Nyong, Ntem, Wouri, Mungo and, in the south-west, the Manyu (Cross River system)."],
            ["Niger basin", "In the north, the Benue (rising in the Adamawa) with its tributaries the Faro and the Mayo Kébi flows west into Nigeria and joins the Niger."],
            ["Lake Chad basin", "In the far north, the Logone (with the Vina and Mbéré from the Adamawa) and the Chari flow to Lake Chad, an inland lake with no outlet to the sea. The Mayo Tsanaga and other seasonal streams of the Mandara join it."],
            ["Congo basin", "In the south-east, rivers such as the Dja, Boumba, Kadéï and Ngoko flow to the Sangha, which joins the Congo."],
        ]),
        T("The Adamawa plateau is the main water divide because it is the highest continuous ground in the centre of the country. "
          "Streams that rise on its southern slopes feed the Sanaga and the Congo basin; those on its northern slopes feed the Benue and the Logone. "
          "The western highlands divide the Atlantic rivers from the upper Benue and Cross River systems."),
        H("River regimes"),
        D("A **river regime** is the pattern of a river's discharge through the year. It depends on rainfall, relief, vegetation and rock type.", title="River regime"),
        KEY("North and south compared", "Regime follows climate.", cards=[
            ["Southern rivers (Nyong, Ntem, Wouri)", "Equatorial rainfall in most months and dense forest give high discharge for most of the year, with two peaks in step with the two rainy seasons and no dry-season stoppage."],
            ["Sanaga", "Its basin covers both the equatorial south and the Adamawa, so it has a mixed regime: a main flood after the rains and a low-water period in the dry season."],
            ["Northern rivers (Benue, Logone, mayos)", "One rainy season gives one flood peak (about August to October) and very low flow, or none for seasonal streams called mayos, in the long dry season."],
        ]),
        H("Using the rivers"),
        KEY("Benefits", "Link each use to a named place.", cards=[
            ["Hydroelectric power", "Sanaga: Edéa and Song Loulou, with reservoirs on its tributaries (Mbakaou on the Djerem, Bamendjin on the Noun) regulating flow. Benue: Lagdo dam. Other schemes: Lom Pangar, Memve'ele and Nachtigal (check their current status)."],
            ["Irrigation and farming", "Lagdo and the Logone plain (rice and dry-season sorghum); flood-recession farming on the Logone flood plain."],
            ["Fishing and transport", "Fishing at Lake Chad, Lagdo and the Logone; limited river transport (the Wouri estuary carries port traffic to Douala)."],
            ["Water supply", "Towns draw water from rivers and boreholes; many rural areas lack safe water."],
        ]),
        KEY("Problems", "A balanced answer includes both.", cards=[
            ["Floods", "The Logone flood plain floods each rainy season; releases from the Lagdo dam have added to floods downstream on the Benue (check the details in your textbook); coastal floods in Douala's low-lying districts."],
            ["Shrinking Lake Chad", "The lake has shrunk greatly since the 1960s because of drought and water withdrawal (check recent estimates). Fishing and farming livelihoods are affected."],
            ["Seasonal flow and pollution", "Dry-season low flow limits hydroelectric output in some years; sediment, waste and chemicals pollute rivers near towns and farms."],
        ]),
        EX("Worked example 1: describe the drainage", intro="Describe the drainage of Cameroon. (Illustrate with a sketch map.)", steps=[
            S("Water divide", text="The Adamawa plateau is the main divide; from it rivers flow north, south, east and west."),
            S("Four basins", text="Atlantic (Sanaga, Nyong, Wouri), Niger (Benue, Faro), Lake Chad (Logone, Chari) and Congo (Dja, Ngoko)."),
            S("Pattern and direction", text="Many rivers radiate from the highlands (radial pattern); the Atlantic rivers flow short distances over plateau edges, forming rapids and falls (for example Sanaga at Edéa) that suit hydroelectric power."),
            S("Sketch map", text="Draw the outline, mark the Adamawa divide with a dotted line, draw and label the main rivers with arrows for direction, add a key and 'not to scale'."),
        ]),
        EX("Worked example 2: explain a flood problem and measures", intro="Explain the causes of flooding on the Logone plain and suggest measures to reduce its effects.", steps=[
            S("Causes", text="Very flat land with a gentle gradient; one heavy rainy season; rivers such as the Logone overflow their banks onto the wide plain; clay soils drain slowly."),
            S("Human factors", text="Settlement and farming on the flood plain increase the damage; embankments and rice schemes can disturb natural drainage."),
            S("Measures", text="Early-warning systems and flood forecasting; raised villages and houses; embankments and drainage channels; planning controls that keep new settlements off the flood plain; careful dam operation."),
            S("Evaluation", text="No single measure is enough. The flood plain is also valuable for fishing and farming, so complete exclusion is not desirable; adapting to seasonal flooding is the realistic aim."),
        ]),
        TIP("In the 2023 Board report, the Paper 3 Cameroon questions included a case in which candidates were to discuss floods and the measures taken. Drainage appears in Paper 3 Section C and in Paper 1; always name rivers and places.",
            title="Exam link"),
        MISTAKE("Confusing the Benue and the Logone", "The Benue flows west to the Niger; the Logone flows north to the Lake Chad basin. Both rise on the Adamawa but on different sides of the divide."),
        MISTAKE("Saying all Cameroon's rivers flow to the Atlantic", "Four basins exist. The Benue reaches the Atlantic only after the Niger, and the Lake Chad basin has inland drainage with no outlet to the sea."),
        QUIZ("Which river basin has inland drainage, with no outlet to the sea?",
             ["Atlantic basin", "Niger basin", "Lake Chad basin", "Congo basin"], 2,
             "Rivers of the Lake Chad basin (Logone, Chari) end in Lake Chad, which has no outlet to the sea.",
             feedback=["Atlantic rivers flow straight to the sea.", "The Niger reaches the Atlantic in Nigeria.", "", "The Congo reaches the Atlantic."]),
        QUIZ("Why does a river such as the Benue show a much stronger seasonal variation in flow than the Nyong?",
             ["It is shorter", "The north has one short rainy season, the south rain in most months", "It crosses more forest", "It flows over granite only"], 1,
             "Regime follows climate: one rainy season in the north means one flood and very low dry-season flow; equatorial rain in the south keeps flow high.",
             feedback=["Length is not the reason.", "", "The north has savanna, not more forest.", "Rock type matters less than rainfall."]),
        PQ("Name the four drainage basins of Cameroon and give one river for each.",
           "Atlantic basin: Sanaga (or Nyong, Ntem, Wouri). Niger basin: Benue (or Faro). Lake Chad basin: Logone (or Chari). Congo basin: Dja (or Ngoko, Kadéï)."),
        PQ("Explain why the Adamawa plateau is the main water divide of Cameroon.",
           "It is the highest continuous high ground across the centre of the country; it receives good rainfall and many rivers rise on it; the slope of the land falls away from it to the south (Atlantic, Congo) and to the north (Benue, Logone), so water drains in different directions."),
        PQ("Discuss the advantages and problems of building dams on Cameroon's rivers.",
           "Advantages: hydroelectric power (Lagdo, Song Loulou, Edéa), water for irrigation and for towns, regulation of flow, fishing in reservoirs. Problems: displacement of people, loss of farmland and habitats, changes to downstream flooding and silting, high construction costs, risk of low output in dry years. Judgement: dams are essential for Cameroon's electricity but their benefits depend on good management and care for affected communities."),
        SUM("Cameroon has four drainage basins: Atlantic, Niger, Lake Chad and Congo; the Adamawa plateau is the main divide.",
            "River regimes follow climate: long high flow in the south, a single flood and low dry-season flow in the north.",
            "Rivers provide power (Sanaga, Lagdo), irrigation, fish and water supply, but also floods and pollution.",
            "Lake Chad has no outlet to the sea and has shrunk since the 1960s.",
            "Always name rivers, places and projects, and give both benefits and problems."),
    ],
))

# ---------------------------------------------------------------------------
# 4. Population of Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Population of Cameroon",
    title="Population of Cameroon: growth, distribution and structure",
    slug="gpu2-population-of-cameroon",
    minutes=24,
    summary="How to calculate and interpret population growth, density and age structure for Cameroon, why people are unevenly distributed, and what population change means for development.",
    objectives=[
        "Calculate an annual growth rate and a doubling time from census totals",
        "Calculate and interpret population density",
        "Explain the uneven distribution of population using physical, economic and historical factors",
        "Describe the age structure and migration and assess their effects on development",
    ],
    key_concepts=["Natural increase", "Growth rate", "Doubling time", "Population density", "Dependency", "Rural-urban migration", "Urbanisation"],
    blocks=[
        H("Introduction"),
        T("Cameroon's population has grown quickly for decades. Many more people now live in Douala and Yaoundé than a generation ago, "
          "while some forest and savanna areas remain thinly settled. At A Level you must be able to **calculate** change, "
          "**describe** the pattern and **explain** it. Paper 3 Cameroon questions also link population to other themes, such as soils and floods."),
        D("**Natural increase** is the birth rate minus the death rate. Population change also depends on migration. "
          "**Population density** is the number of people per square kilometre: total population divided by area.", title="Natural increase and density"),
        H("Growth: census totals and calculations"),
        T("Cameroon has held three modern censuses: 1976, 1987 and 2005. The totals below are the figures usually quoted in textbooks "
          "(check your textbook for the exact values). Later totals are estimates, not census counts."),
        CODE("Year   Total population\n1976      7 663 246\n1987     10 493 655\n2005     17 463 836", "text", title="Table 1. Census totals (as usually quoted; check your textbook)"),
        F(r"r = \left(\frac{P_{\text{end}}}{P_{\text{start}}}\right)^{1/n} - 1", title="Compound annual growth rate"),
        EX("Worked example 1: growth rate and doubling time", intro="Use Table 1 to find the average annual growth rate between 1987 and 2005 and the time the population would take to double at that rate.", steps=[
            S("Number of years", math=r"n = 2005 - 1987 = 18"),
            S("Ratio", math=r"\frac{17\,463\,836}{10\,493\,655} = 1.6642"),
            S("Take the 18th root", math=r"1.6642^{1/18} = 1.0287"),
            S("Growth rate", math=r"r = 2.87\% \text{ per year}"),
            S("Doubling time, rule of 70", math=r"\frac{70}{2.87} \approx 24.4 \text{ years}", text="The exact calculation with logarithms gives the same, 24.4 years."),
        ]),
        EX("Worked example 2: density", intro="Cameroon has an area of about 475 000 square kilometres (check your textbook). Calculate the density in 2005 and 1987.", steps=[
            S("Formula", math=r"\text{density} = \frac{\text{population}}{\text{area}}"),
            S("2005", math=r"\frac{17\,463\,836}{475\,000} \approx 36.8 \approx 37 \text{ people per km}^2"),
            S("1987", math=r"\frac{10\,493\,655}{475\,000} \approx 22.1 \approx 22 \text{ people per km}^2"),
            S("Interpret", text="The national average hides huge differences: some highland and coastal areas have several hundred per km2, parts of the east have only a few."),
        ]),
        TIP("A national density is an average. In an essay, say what it hides, then give regional contrasts."),
        H("Distribution of population"),
        KEY("Dense areas", "Give a physical reason, an economic reason and a historical or social reason.", cards=[
            ["Western and north-western highlands", "Fertile volcanic soils, cool healthy climate with reliable rain, intensive farming (maize, coffee, vegetables), a long history of settlement and strong chiefdoms with high land pressure."],
            ["Coast and large cities", "Douala (port and industry) and Yaoundé (capital) attract migrants for jobs; plantation areas around Mount Cameroon support workers."],
            ["Mandara foothills and parts of the Far North", "Locally very dense because of old settlement and terraced farming, despite a harsh climate."],
        ]),
        KEY("Sparse areas", "These are usually forest or very dry or remote areas.", cards=[
            ["East and South forests", "Dense forest, poor soils after clearing, long distances and poor roads, some protected areas."],
            ["Adamawa and Benue margins", "Pastoral land use needs space; tsetse fly and past disease limited settlement; long dry season."],
            ["Flood-prone and swampy areas", "Parts of the coast and the Logone plain are avoided or used only seasonally."],
        ]),
        H("Structure and migration"),
        T("Cameroon has a **young population**: a large share are children, so its population pyramid has a wide base and narrows quickly. "
          "Fertility is high and falling slowly, and life expectancy has improved but remains below that of richer countries (use current figures from your textbook or national sources; the exact values change). "
          "In terms of the Demographic Transition Model, Cameroon is usually placed in stage 2 or early stage 3: falling death rates, birth rates still high."),
        KEY("Consequences of a young population", "Weigh costs against opportunities.", cards=[
            ["Pressures", "Heavy demand for schools, clinics and jobs; a high dependency ratio; youth unemployment; pressure on land and on cities."],
            ["Opportunities", "A large future labour force and market; a possible 'demographic dividend' if jobs and skills are created."],
        ]),
        T("**Migration** is a major force. Rural-urban migration feeds the growth of Douala and Yaoundé. People also move between regions "
          "for plantation or farm work, from the north and west towards the forest and coast, and across borders as refugees or traders. "
          "More than half of Cameroonians now live in towns (check the latest estimate)."),
        EX("Worked example 3: dependency ratio", intro="An invented population for practice: 42 per cent are aged under 15, 54 per cent aged 15 to 64 and 4 per cent aged 65 and over. Calculate the total dependency ratio.", steps=[
            S("Formula", math=r"\text{dependency ratio} = \frac{\text{young} + \text{old}}{\text{working age}} \times 100"),
            S("Substitute", math=r"\frac{42 + 4}{54} \times 100"),
            S("Calculate", math=r"= 85.2"),
            S("Interpret", text="There are about 85 dependants for every 100 people of working age. That is high; most dependants are children."),
        ]),
        MISTAKE("Using the simple percentage change as the annual rate", "From 1987 to 2005 the population grew by about 66 per cent in total. That is not 66 per cent a year. Use the compound formula or divide carefully, and state the years."),
        MISTAKE("Describing the distribution without figures or places", "Say 'densities are highest in the West and North-West highlands and around Douala and Yaoundé and lowest in the East'. Add figures or contrasts where the question gives data."),
        MISTAKE("Giving only physical reasons", "Examiners expect physical, economic and historical or social factors, for example soils and climate, jobs and ports, long-settled areas."),
        QUIZ("A population grows from 10.0 million to 12.1 million in 10 years. Its average annual growth rate is closest to",
             ["2.1%", "1.9%", "2.0%", "21%"], 1,
             "Ratio 1.21, tenth root 1.019, so about 1.9 per cent a year (about 2 per cent is also common; 2.1 would give 12.3 million).",
             hint="Use r = (P_end divided by P_start) to the power 1 over n, minus 1.",
             feedback=["2.1 per cent a year would give about 12.3 million.", "", "Close, but 2.0 per cent a year would give 12.19 million.", "That is the total change over 10 years, not the annual rate."]),
        QUIZ("Which is the best explanation for dense population in the western highlands?",
             ["Very dry climate", "Fertile volcanic soils and reliable rain supporting intensive farming", "Dense equatorial forest", "Absence of roads"], 1,
             "Rich volcanic soils, cool wet climate and a long farming history support many people per km2.",
             feedback=["The climate is not very dry.", "", "Dense forest is more typical of the south-east, with low densities.", "Remote areas have low densities."]),
        PQ("Describe and explain the distribution of population in Cameroon.",
           "Describe: dense in the West and North-West highlands, the coast around Douala and Yaoundé, and some parts of the Far North; sparse in the East and South forests and parts of the Adamawa. "
           "Explain: fertile volcanic soils and a cool wet climate; jobs, ports and services in Douala and Yaoundé; long settlement history; in contrast dense forest, poor roads, tsetse fly and thin soils limit settlement elsewhere. "
           "Evaluate: physical, economic and historical factors operate together."),
        PQ("Population totals for a region (invented for practice) were 2.4 million in 1987 and 3.6 million in 2005. Calculate the average annual growth rate.",
           "Ratio 3.6 divided by 2.4 = 1.5. n = 18. 1.5 to the power 1/18 = 1.0228, so about 2.3 per cent a year."),
        PQ("Assess the effects of a young population on the development of Cameroon.",
           "Pressures: schools, health care and jobs for many young people; high dependency; unemployment; pressure on land and cities. Opportunities: a large future workforce and market. Judgement: it depends on investment in education, health and job creation; without these the youth bulge is a burden, with them it can be an advantage."),
        SUM("Growth rate: r = (end divided by start) to the power 1 over n, minus 1. For 1987 to 2005 it is about 2.9 per cent a year; doubling time is about 24 years.",
            "Density = people divided by area; the national figure (about 37 per km2 in 2005) hides large regional differences.",
            "Dense areas: highlands, coast and big cities. Sparse areas: eastern and southern forest, parts of the Adamawa.",
            "Cameroon has a young population (DTM stage 2 or early 3), bringing pressure and opportunity.",
            "Explain distribution with physical, economic and historical factors and always use places and figures."),
    ],
))

# ---------------------------------------------------------------------------
# 5. Agriculture, forestry and fishing in Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Agriculture, forestry and fishing in Cameroon",
    title="Agriculture, forestry and fishing: zones, systems, problems and policy",
    slug="gpu2-agriculture-forestry-fishing-cameroon",
    minutes=25,
    summary="How physical conditions shape the agro-ecological zones and farming systems of Cameroon, how plantation and smallholder farming differ, and the problems and management of forests and fisheries.",
    objectives=[
        "Relate the main crops and farming systems to the five agro-ecological zones",
        "Contrast plantation farming with smallholder farming in Cameroon",
        "Explain the problems of agriculture and the measures taken, with examples",
        "Assess the exploitation and management of forest and fish resources",
    ],
    key_concepts=["Agro-ecological zone", "Plantation", "Smallholder", "Cash crop", "Food crop", "Deforestation", "Sustainable management", "Artisanal fishing"],
    blocks=[
        H("Introduction"),
        T("Most Cameroonians still earn part of their living from the land, the forest or the water. The country grows crops from the "
          "banana and oil palm of the coast to the cotton and sorghum of the north. The 2023 Board report noted that candidates could "
          "name crops but often could not link them to a **farming system** or to the physical environment. This lesson builds that link."),
        D("An **agro-ecological zone** is an area where climate, relief and soils are similar enough that the same crops and farming systems are suitable.", title="Agro-ecological zone"),
        D("A **plantation** is a large estate growing one cash crop for sale, using hired labour and often owning its own processing plant. A **smallholder** farms a small plot, mainly with family labour, often growing food crops and some cash crops.", title="Plantation and smallholder"),
        H("Agro-ecological zones and crops"),
        T("Cameroon is usually divided into five agro-ecological zones. Names and boundaries differ slightly between sources, so check your textbook."),
        KEY("The five zones", "Learn the zone, its climate and its crops.", cards=[
            ["Sudano-Sahelian (Far North, North)", "Hot, one short rainy season. Cotton (SODECOTON), sorghum and millet, groundnuts, onions; irrigated rice at Maga; cattle and goats; dry-season sorghum (muskwari) on clay soils."],
            ["High Guinea savanna (Adamawa)", "Cooler plateau with a long rainy season. Cattle rearing (the Mbororo tradition), maize, cassava, groundnuts, tea and vegetables on the plateau edges."],
            ["Western highlands (West, North-West)", "Cool, fertile volcanic soils, high densities. Arabica coffee, maize, beans, potatoes, vegetables, tea (for example Ndu), oil palm at lower levels; very intensive smallholder farming."],
            ["Humid forest, bimodal rainfall (Centre, South, East)", "Two rainy seasons. Cocoa (the main region), plantain, cassava, yams, groundnuts, robusta coffee; shifting cultivation and bush fallow; forestry."],
            ["Humid forest, monomodal rainfall (Littoral, South-West)", "One very long rainy season; volcanic soils. Banana, oil palm, rubber, tea, plantains, robusta coffee; large plantations (CDC and private companies) plus smallholders; fishing on the coast."],
        ]),
        H("Farming systems"),
        KEY("Main systems", "Name the system, say where, say why.", cards=[
            ["Shifting cultivation and bush fallow", "Forest and savanna margins; farmers clear and burn plots, crop for a few years, then leave land fallow so that fertility recovers. Works only if population density is low."],
            ["Permanent smallholder farming", "Western highlands and the Mandara; intensive use of small plots with manure, mixed cropping and terraces."],
            ["Plantation farming", "Coastal lowlands and the slopes of Mount Cameroon (banana, oil palm, rubber, tea); large estates, hired labour, processing on site."],
            ["Pastoralism", "Adamawa and the north; cattle herding, sometimes seasonal movement (transhumance) between wet- and dry-season pastures."],
            ["Irrigated farming", "Rice schemes on the Logone plain, small-scale vegetable growing in dry-season valleys."],
        ]),
        EX("Worked example 1: link the farming system to the physical environment", intro="Illustrate how the physical environment has influenced the pattern of food crop farming in Cameroon.", steps=[
            S("Humid south", text="Rain in most months and acid forest soils favour root crops and plantain (cassava, yams, plantain, cocoyam), grown by shifting cultivation and bush fallow."),
            S("Highlands", text="Cool climate and fertile volcanic soils at 1,000 to 2,000 m suit maize, beans, potatoes and vegetables, grown intensively on permanent plots."),
            S("Savanna and north", text="One short rainy season and drought risk favour drought-tolerant sorghum and millet, with groundnuts and cattle; irrigation allows rice and dry-season crops."),
            S("Link back", text="So rainfall total and season length, temperature (altitude) and soil type together control which food crop is grown where."),
        ]),
        H("Problems and efforts"),
        KEY("Problems of agriculture", "Do not list problems only: say what they cause and give an example.", cards=[
            ["Physical", "Drought and irregular rainfall in the north; soil exhaustion and erosion on steep slopes; pests and diseases (for example black pod disease of cocoa)."],
            ["Economic and technical", "Small plots, simple tools, limited credit, expensive fertiliser, falling or unstable world prices for cash crops, post-harvest losses."],
            ["Infrastructure and social", "Poor feeder roads to farms and markets, so food rots or sells cheaply; land tenure insecurity; ageing farmers and youth leaving farms; insecurity in some areas disrupting farming."],
        ]),
        KEY("Efforts to improve agriculture", "Name the effort and the result, with caution on details.", cards=[
            ["Institutions and research", "Ministries of agriculture; research by IRAD; cotton company SODECOTON; plantation companies such as CDC (check current status)."],
            ["Inputs and training", "Improved seed, fertiliser and extension advice; farmer cooperatives and credit schemes; irrigation at Maga and Lagdo."],
            ["Processing and markets", "Agro-processing (sugar, palm oil, rubber, cotton ginning); feeder-road rehabilitation; efforts to increase local value added on cocoa and coffee."],
        ]),
        H("Forestry"),
        T("Cameroon has large tropical forests in the south and east, among the largest in Central Africa. They provide timber (for example ayous, sapele and iroko), "
          "fuel wood, food and medicines, and they shelter biodiversity and store carbon. The 1994 forestry law created a framework of forest management units and "
          "community forests and set aside protected areas (check the current rules). Threats include **deforestation** for farms and plantations, "
          "logging (legal and illegal), fuel wood collection and mining."),
        KEY("Managing forests sustainably", "Link each measure to a problem.", cards=[
            ["Regulation", "Management plans, annual cutting limits, forest certification, controls on log exports and processing in Cameroon (check current rules)."],
            ["Community involvement", "Community forests and benefit sharing so that local people gain from keeping forests."],
            ["Protection and restoration", "National parks and reserves (for example Dja Faunal Reserve), reforestation and agroforestry."],
        ]),
        H("Fishing"),
        T("Cameroon's fish come from the Atlantic coast (Douala, Limbe, Kribi), from rivers and lakes (Lake Chad, Lagdo, Bamendjin) and from fish farms (aquaculture). "
          "Most fish are caught by **artisanal** fishers using canoes and nets; a smaller **industrial** fleet uses trawlers. Cameroon imports a large quantity of "
          "frozen fish to meet demand (check current figures). Problems include overfishing, small-mesh nets, illegal fishing by foreign vessels, pollution, poor storage and roads, "
          "and falling water levels in Lake Chad. Measures include fishing-season and mesh-size rules, aquaculture projects, cold-storage and landing sites, and patrols."),
        EX("Worked example 2: model essay plan", intro="Discuss the view that Cameroon's forests should be protected rather than used.", steps=[
            S("Case for protection", text="Biodiversity (Dja reserve), carbon storage, protection of soils and rivers, livelihoods of forest peoples, tourism."),
            S("Case for use", text="Timber exports and jobs; land for cocoa, plantations and food; fuel wood; revenue for development."),
            S("Evaluation", text="The two are not opposites: sustainable management with limited cutting, replanting and community benefit can serve both. The risk is that weak enforcement turns 'use' into deforestation."),
            S("Judgement", text="A balanced policy: strictly protect core areas and manage the rest sustainably, with enforcement and benefits for local people."),
        ]),
        TIP("In the 2023 Board report the Paper 3 Cameroon section had questions on agriculture (food crop farming systems, socio-economic obstacles and measures), tourism and vegetation. "
            "Examiners wanted **concrete examples** such as a named crop, scheme or region. Agriculture also appears in Paper 1.",
            title="Exam link"),
        MISTAKE("Listing crops without a system", "Say whether the crop is grown by plantation, smallholder shifting cultivation, permanent farming or irrigation, and in which zone."),
        MISTAKE("Stopping at 'poor roads' or 'lack of capital'", "Explain the effect (food spoils, farmers sell cheaply) and give a measure with an example (feeder road rehabilitation, cooperatives)."),
        QUIZ("Which agro-ecological zone is the main region for cocoa production in Cameroon?",
             ["Sudano-Sahelian", "Humid forest zone with two rainy seasons", "High Guinea savanna", "Western highlands"], 1,
             "Cocoa needs heat, humidity and shade; it is grown mainly in the Centre, South and East.",
             feedback=["Too dry for cocoa.", "", "Too cool and with a long dry season for large-scale cocoa.", "Arabica coffee and food crops dominate here."]),
        QUIZ("Which statement correctly contrasts a plantation with smallholder farming?",
             ["Plantations use mainly family labour", "Plantations are large estates with hired labour growing one cash crop", "Smallholders always grow export crops only", "Plantations never process their products"], 1,
             "Plantations are large, specialised and commercial, often with on-site processing.",
             feedback=["That describes smallholders.", "", "Smallholders mostly grow food crops, with some cash crops.", "Many plantations process on site (oil palm mills, rubber)."]),
        PQ("Discuss two socio-economic factors that hinder agricultural development in Cameroon and state a measure to solve each.",
           "(1) Poor feeder roads: food and cash crops spoil or cannot reach markets, so prices to farmers are low. Measure: rehabilitation of rural roads and storage. "
           "(2) Limited credit and inputs: farmers cannot buy fertiliser and improved seeds, so yields are low. Measure: cooperatives, microcredit and subsidised inputs. "
           "Use examples such as cocoa farmers in the Centre or maize farmers in the West."),
        PQ("Explain why shifting cultivation is common in the forest zone but permanent farming is common in the western highlands.",
           "In the forest zone population density is low and soils are quickly exhausted once cleared, so fallow is possible and necessary. In the western highlands high population density, "
           "fertile volcanic soils and little spare land mean farmers cannot leave land fallow; they use manure, mixed cropping and terraces on permanent plots."),
        PQ("Assess the success of efforts to manage Cameroon's forests sustainably.",
           "Successes: forestry law of 1994 and management plans, community forests, protected areas such as Dja. Limits: illegal logging, weak enforcement, clearing for farms and plantations, "
           "limited benefits for local people. Judgement: the framework exists but results depend on enforcement and on giving communities a reason to protect forests."),
        SUM("Cameroon has five agro-ecological zones; crops follow rainfall, altitude and soil, from cotton and sorghum in the north to cocoa, banana and oil palm in the south.",
            "Systems: shifting cultivation, permanent smallholder farming, plantations, pastoralism and irrigated farming.",
            "Problems include drought, poor roads, low inputs and unstable prices; efforts include research, cooperatives, irrigation and processing.",
            "Forests give timber, food and biodiversity but are threatened by clearing and illegal logging; management combines regulation, communities and protection.",
            "Fishing is mostly artisanal; overfishing and imports show the need for management and aquaculture. Always use examples."),
    ],
))

# ---------------------------------------------------------------------------
# 6. Energy, minerals and industry in Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Energy, minerals and industry in Cameroon",
    title="Energy, minerals and industry: resources as bases for industrialisation",
    slug="gpu2-energy-minerals-industry-cameroon",
    minutes=24,
    summary="Cameroon's energy and mineral resources, where industries are located and why, and how far agriculture, energy and minerals form a base for industrial growth, with the obstacles and measures.",
    objectives=[
        "Describe the main sources of energy and minerals in Cameroon and where they are found",
        "Explain the location of the main industrial centres",
        "Discuss agricultural and energy resources as bases for industrialisation",
        "Explain the problems of industrial growth and the efforts made to promote it",
    ],
    key_concepts=["Hydroelectric power", "Hydrocarbons", "Mineral reserves", "Agro-processing", "Industrial location", "Value added", "Free zone"],
    blocks=[
        H("Introduction"),
        T("The 2023 Board report on Paper 3 noted that candidates could say that Cameroon's industries use agricultural and energy resources "
          "but gave **few concrete examples**: which raw material, which industry, in which town. At A Level, a resource is only useful if you can say "
          "where it is, how it is used and what limits its use."),
        D("**Industrialisation** is the growth of manufacturing in an economy. **Value added** is the extra value created when raw materials are processed, for example when cocoa beans become chocolate or logs become furniture.", title="Industrialisation and value added"),
        H("Energy resources"),
        KEY("Main sources", "Give the source, a place and a use.", cards=[
            ["Hydroelectricity", "The main source of electricity. Plants on the Sanaga (Edéa, Song Loulou), Lagdo on the Benue, and newer schemes such as Memve'ele, Lom Pangar and Nachtigal (check their current status). Much of the output serves the aluminium smelter at Edéa and the cities."],
            ["Oil", "Mainly offshore in the Rio del Rey basin near the Bakassi coast and off the south-west coast; crude oil is refined at Limbe (SONARA). The Chad-Cameroon pipeline carries Chad's oil from the Doba fields to a floating terminal off Kribi."],
            ["Natural gas", "Used in the Kribi power station and in Douala (Logbaba field)."],
            ["Biomass", "Fuel wood and charcoal are the main household fuels for many families, which adds to forest clearing."],
            ["Solar and other", "Solar power is promising, especially in the sunny north, but still small."],
        ]),
        T("Cameroon has great hydroelectric potential, but production depends on rainfall and reservoirs, and power cuts still happen. Large dams need heavy investment. "
          "Many rural areas have no grid electricity."),
        H("Mineral resources"),
        T("Cameroon has many mineral deposits but few are exploited on a large scale. For several, check the current status in your textbook, because projects change."),
        KEY("Minerals and their situation", "Separate what is mined from what is only a deposit.", cards=[
            ["Bauxite (aluminium ore)", "Large deposits in the Adamawa (Minim-Martap, Ngaoundal) and the western highlands; large-scale mining has long been planned. The Edéa smelter uses imported alumina."],
            ["Iron ore", "Mbalam-Nabeba in the south-east (near the Congo border); a major project that depends on a railway link."],
            ["Cobalt, nickel, manganese", "Around Lomié in the East (Nkamouna): a development project."],
            ["Gold, diamonds and rutile", "Gold and diamonds are mostly extracted by small-scale or artisanal miners in the East; rutile in the Akonolinga area."],
            ["Limestone and sand", "Limestone at Figuil in the north and in the Douala area for cement; sand and gravel for construction near cities."],
        ]),
        H("Industry and where it is located"),
        KEY("Main industrial centres", "Link each centre to the factors that attract industry.", cards=[
            ["Douala (and Bonabéri)", "Largest industrial centre: port, airport, rail and road links, a large labour force and consumer market, banks and electricity. Brewing, soft drinks, soap, cement, metal goods, timber processing, printing."],
            ["Edéa", "Hydroelectric power from the Sanaga: aluminium smelting (ALUCAM) and wood processing."],
            ["Limbe and the South-West", "The oil refinery, rubber and palm oil processing, banana packing near the plantations."],
            ["Yaoundé", "Capital city market: food, beverages and construction materials."],
            ["Mbandjock, Maroua and Garoua", "Sugar (Mbandjock) and cotton ginning and textiles in the north near the cotton fields."],
            ["Kribi", "The deep-sea port and industrial zone, the gas power plant and the pipeline terminal (check the current projects)."],
        ]),
        EX("Worked example 1: agricultural raw materials as a base for industry", intro="Discuss agricultural resources as a base for industrialisation in Cameroon.", steps=[
            S("Link raw material to industry", text="Cotton in the north supplies ginneries and textiles; sugar cane at Mbandjock supplies the sugar factory; oil palm and rubber supply mills in the Littoral and South-West; timber supplies sawmills; cocoa and coffee can supply local processing."),
            S("Advantages", text="Raw materials are local, so costs of imports are saved; processing adds value and creates jobs; farmers gain a market."),
            S("Limits", text="Much cocoa, coffee and timber is still exported with little processing; quality and supply vary; transport and electricity costs are high; foreign competition."),
            S("Judgement", text="Agriculture is a strong base, but the full benefit needs more local processing."),
        ]),
        EX("Worked example 2: energy as a base for industry", intro="Examine how energy resources support industrial development in Cameroon.", steps=[
            S("Hydro power", text="Cheap electricity at Edéa attracted the aluminium smelter, which is a very large electricity user; power also supports factories in Douala."),
            S("Oil and gas", text="Oil provides export income and fuel through the Limbe refinery; gas now fuels power plants at Kribi and Douala."),
            S("Constraints", text="Power cuts, high tariffs for small factories, limited rural grid, dependence on rainfall."),
            S("Judgement", text="Energy is a major advantage, but reliable and affordable supply, not just potential, is what firms need."),
        ]),
        H("Problems and efforts"),
        KEY("Obstacles to industrial growth", "Give effects and examples.", cards=[
            ["Market and capital", "A small national market and limited local capital; competition from imported goods."],
            ["Infrastructure", "Unreliable electricity, poor roads and rail, congestion at the port of Douala."],
            ["Skills and finance", "Shortage of technical skills; difficult access to credit."],
            ["Informal sector", "Many small firms are informal, with low productivity and no access to support."],
        ]),
        KEY("Efforts to promote industry", "Name the measure and, where possible, a result.", cards=[
            ["Investment and zones", "Investment codes and an industrial free zone system with tax advantages; the industrial park at Bonabéri; Kribi port and industrial zone."],
            ["Infrastructure", "New dams and gas plants, road and rail upgrades, the deep-sea port of Kribi."],
            ["Policy", "National development strategies that aim at emergence by 2035 (check the current plan) and support for processing of raw materials in Cameroon."],
        ]),
        TIP("This topic matches the Section C question type in Paper 3 (Cameroon) of the 2023 Board report, which asked about agricultural and energy resources as bases for industry and about efforts to promote industrial growth. Always give a named raw material, a named industry and a named town.",
            title="Exam link"),
        MISTAKE("Saying 'Cameroon has many minerals so it is rich'", "A deposit is not a mine. Distinguish deposits from exploited minerals and give reasons: distance, lack of railways, finance, world prices."),
        MISTAKE("Only naming HEP as the energy source", "The report said that candidates mostly gave HEP without concrete examples. Add oil (Limbe refinery, pipeline), gas (Kribi) and biomass, and name plants."),
        QUIZ("Why is aluminium smelting located at Edéa?",
             ["It is near bauxite mines", "Cheap hydroelectric power from the Sanaga is available", "It is the capital", "It has a large oil field"], 1,
             "Smelting uses very large amounts of electricity, and the Sanaga provides it. The ore is not mined there.",
             feedback=["Bauxite is mostly in the Adamawa and the alumina is imported.", "", "The capital is Yaoundé.", "Oil is offshore, in the Rio del Rey basin."]),
        QUIZ("Which statement about minerals in Cameroon is most accurate?",
             ["All major deposits are in large-scale production", "Large deposits such as bauxite and iron ore exist but most are not yet exploited on a large scale", "Cameroon has no minerals", "Gold is mined only by multinational companies"], 1,
             "Many large deposits await development because of infrastructure and finance needs.",
             feedback=["Most are not in large-scale production.", "", "Cameroon has many minerals.", "A lot of gold is mined by artisanal miners."]),
        PQ("Name two agricultural raw materials used in manufacturing in Cameroon and the industry and town for each.",
           "Cotton: ginning and textile industry at Garoua and Maroua region (Sodecoton gins). Sugar cane: sugar factory at Mbandjock. Also oil palm (mills in the Littoral and South-West) and timber (sawmills in the East and Douala)."),
        PQ("Explain why Douala is the main industrial centre of Cameroon.",
           "Port with links to the world; airport and road and rail links to Yaoundé, the north and the west; the biggest market and labour supply; electricity from Edéa and Song Loulou; banks and services; a concentration of existing industry attracts more (agglomeration)."),
        PQ("Discuss the problems of industrial development in Cameroon and efforts to solve them.",
           "Problems: power cuts, high costs, small market, poor roads and port congestion, skills and finance shortage, competition from imports, informal sector. Efforts: new dams and gas plants, Kribi port, Bonabéri industrial park, free zone incentives, development plans. Judgement: progress is real, but reliable power and infrastructure remain the decisive tests."),
        SUM("Cameroon's energy comes mainly from hydroelectricity, with oil, gas and biomass; many mineral deposits exist but few are exploited at large scale.",
            "Industries locate at Douala (market, port), Edéa (power), Limbe (oil), Mbandjock (sugar) and in the north (cotton).",
            "Agricultural, energy and mineral resources are potential bases for industry, but processing and infrastructure limit the benefits.",
            "Obstacles: unreliable power, poor transport, small market, skills and finance; efforts include dams, Kribi port and free zones.",
            "Always give a named resource, industry and town."),
    ],
))

# ---------------------------------------------------------------------------
# 7. Transport and regional inequalities in Cameroon
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_CMR, topic="Transport and regional inequalities in Cameroon",
    title="Transport corridors and regional inequalities in Cameroon",
    slug="gpu2-transport-and-regional-inequalities-cameroon",
    minutes=23,
    summary="The main transport corridors and ports of Cameroon, how relief and distance shape them, and how differences in access and wealth between regions arise and are addressed.",
    objectives=[
        "Describe the main road, rail, air and sea transport corridors and the role of the ports",
        "Explain how physical and human factors shape transport development",
        "Describe regional inequalities in development and explain their causes",
        "Evaluate strategies to reduce inequalities",
    ],
    key_concepts=["Transport corridor", "Transit trade", "Core and periphery", "Regional inequality", "Enclaved region", "Decentralisation", "Growth pole"],
    blocks=[
        H("Introduction"),
        T("A truck leaving the port of Douala for N'Djamena travels well over a thousand kilometres, crossing forest, the Adamawa escarpment and the savanna. "
          "Chad and the Central African Republic have no coast: Cameroon's ports and roads are their lifelines. "
          "Within Cameroon, regions near the ports and the capital are generally better served and richer than remote regions. "
          "This lesson connects **transport** to **regional inequality**."),
        D("A **transport corridor** is a main route, usually combining road, rail or river links, along which goods and people flow between major centres and ports.", title="Transport corridor"),
        D("**Regional inequality** is the difference between regions in income, services, jobs and infrastructure. In a **core-periphery** pattern, one or two core regions are richer and the outlying regions poorer.", title="Regional inequality"),
        H("The main corridors"),
        IMG("algpu2-cmr-corridors.svg",
            alt="Schematic of transport corridors: railway Douala-Edea-Yaounde-Belabo-Ngaoundere; roads Ngaoundere-Garoua-Maroua-N'Djamena, Yaounde-Bertoua-Garoua-Boulai-Bangui, Douala-Bafoussam-Bamenda; Kribi port linked to Edea",
            caption="Figure 1. The main corridors. Schematic, not to scale; routes and links are simplified."),
        KEY("Corridors and ports", "Learn the corridor, what it links and what it carries.", cards=[
            ["Douala-Yaoundé-Ngaoundéré", "The railway (run by Camrail) links the port of Douala to Yaoundé and Ngaoundéré, where goods transfer to road for northern Cameroon and Chad. Fuel, containers, cement, timber, cattle and food move along it."],
            ["Douala-Bafoussam-Bamenda", "Roads from the port to the western highlands: farm produce and manufactured goods in both directions."],
            ["Douala-Bertoua-Garoua-Boulaï", "The road corridor to the Central African Republic (Bangui). Timber trucks and imports use it."],
            ["Ngaoundéré-Garoua-Maroua-N'Djamena", "The northern corridor linking the railhead to the Far North and Chad."],
            ["Sea and air", "Douala is the main seaport (the Wouri estuary needs dredging); Kribi has a new deep-sea port (check current status); Limbe is a smaller port. Douala, Yaoundé-Nsimalen and Garoua have the main international airports."],
        ]),
        H("Why transport develops as it does"),
        KEY("Physical and human influences", "A good answer uses both.", cards=[
            ["Relief", "The Adamawa escarpment, western mountains and forest make roads and railways costly to build; steep gradients slow vehicles (compare the road climbing an escarpment in the map-work lessons)."],
            ["Climate and drainage", "Heavy rain damages earth roads and washes out bridges; flood plains in the north cut roads each rainy season; rivers need bridges."],
            ["Economic", "Roads follow the flow of exports (cocoa, timber, cotton) and imports to the ports and the main markets."],
            ["Political and financial", "Cost of building and maintenance, priorities of investment, regional balance, regional agreements for transit routes."],
        ]),
        KEY("Problems of transport", "Name the problem and its effect.", cards=[
            ["Roads", "Many rural and some main roads are in poor condition; long travel times raise costs and spoil perishable food."],
            ["Rail", "A single main line with limited capacity and few links; delays in freight."],
            ["Port and border", "Congestion at Douala; slow customs and many checks along corridors."],
            ["Road safety and cost", "High accident rates on busy routes; high fuel and vehicle costs."],
        ]),
        H("Regional inequalities"),
        T("Cameroon's regions differ strongly in income and services. In national surveys, poverty is usually highest in the northern regions "
          "(Far North, North, Adamawa) and in parts of the East, and lower in the Littoral and Centre regions where Douala and Yaoundé lie (check the latest survey before quoting figures). "
          "School attendance, health care access and electricity also differ. Insecurity in some areas in recent years has added to the difficulties."),
        KEY("Causes of inequality", "Link them to the map: relief, climate, distance, history, policy.", cards=[
            ["Physical", "Drought-prone north; remote forest and escarpments; poor soils in some areas."],
            ["Location and accessibility", "Regions far from the ports and capital have higher transport costs and fewer investors (the periphery); Douala and Yaoundé form the core."],
            ["Economic and historical", "Industry, banks and services concentrated in a few cities; colonial-period investment concentrated on plantations and ports; migration drains young workers from poorer regions."],
            ["Policy", "Past investment priorities and uneven provision of services; limited local budgets."],
        ]),
        EX("Worked example 1: explain a core-periphery pattern", intro="Explain why the Far North region is less developed than the Littoral region.", steps=[
            S("Physical", text="The Far North has a semi-arid climate with frequent drought and flooding on the Logone plain; farming is risky. The Littoral has reliable rain and fertile volcanic soils."),
            S("Accessibility", text="The Far North is well over a thousand kilometres by road from the port of Douala, so goods are costly. The Littoral has the port, airport and rail."),
            S("Economic", text="Industry and services concentrate at Douala; the Far North depends on cotton, livestock and small trade."),
            S("Social and security", text="Lower school attendance, fewer clinics, and insecurity in some areas reduce investment."),
            S("Conclusion", text="Physical limits, distance and the concentration of investment reinforce one another in a cumulative cycle."),
        ]),
        H("Reducing inequality"),
        KEY("Strategies", "For each, give a possible benefit and a limit.", cards=[
            ["Infrastructure", "Roads, rail and electricity to remote regions; Kribi port and corridors. Benefit: lowers costs and opens markets. Limit: expensive and slow to complete."],
            ["Decentralisation", "Transferring powers and funds to regions and councils. Benefit: local priorities. Limit: capacity and money are unequal."],
            ["Growth poles and zones", "Developing secondary centres such as Garoua, Bafoussam or Kribi. Benefit: jobs outside Douala and Yaoundé. Limit: may not spread to rural areas."],
            ["Targeted programmes", "Irrigation, schools and health in the poorest regions. Benefit: direct help. Limit: depends on funding and security."],
        ]),
        EX("Worked example 2: evaluation", intro="Assess the success of measures to reduce regional inequalities in Cameroon.", steps=[
            S("Evidence of progress", text="New roads and the railway have opened access; Kribi port and gas power add capacity; decentralisation has given councils more responsibilities."),
            S("Limits", text="Inequalities remain large; remote regions still lack roads and power; funding and capacity differ widely; insecurity disrupts programmes."),
            S("Judgement", text="Some progress, but not enough to close the gap. The most effective measures combine transport, services and local jobs, and they need stable funding and security."),
        ]),
        TIP("Transport and regional inequalities connect to the Cameroon questions of Paper 3 Section C and to the regional development ideas of the Upper Sixth (core and periphery, cumulative causation). Name corridors, ports and regions. Do not make political judgements: describe causes and measures.", title="Exam link"),
        MISTAKE("Listing roads without explaining", "Link transport to relief, rainfall, trade flows and finance, and give an effect on people."),
        MISTAKE("Saying inequality is only about the north", "Inequality also exists within regions (for example between rural villages and cities) and between neighbourhoods of Douala and Yaoundé."),
        QUIZ("Why is the Ngaoundéré railhead important to Chad?",
             ["It is Chad's capital", "Goods from Douala are transferred there to road for northern Cameroon and Chad", "It has the main airport of Chad", "It is the end of the Benue river route"], 1,
             "Rail takes goods from the port of Douala to Ngaoundéré; road trucks carry them on to the north and to Chad.",
             feedback=["Chad's capital is N'Djamena.", "", "Not in Chad.", "Not a river route."]),
        QUIZ("Which is the best explanation of a core-periphery pattern?",
             ["Wealth is evenly spread", "Development concentrates in one or two core regions while remote regions stay poorer", "The periphery is richer", "All regions have a port"], 1,
             "Investment, services and migration favour the core, which draws resources away from the periphery.",
             feedback=["That is the opposite.", "", "The periphery is usually poorer.", "Many regions have no port."]),
        PQ("Describe the main transport links between the port of Douala and northern Cameroon.",
           "Rail from Douala through Edéa and Yaoundé to Ngaoundéré; road from Ngaoundéré north through Garoua to Maroua and on to N'Djamena; the climb of the Adamawa escarpment; Ngaoundéré is the transfer point between rail and road."),
        PQ("Explain two reasons why road construction is difficult in the Far North and in the forest zone of the East.",
           "Far North: seasonal flooding of flat plains and mayos washes out roads; long distances and a small population make roads costly per user. East: heavy rain and dense forest make earth roads impassable and costly to maintain; low population density limits traffic."),
        PQ("Discuss the causes of regional inequalities in Cameroon and measures to reduce them.",
           "Causes: physical (drought, remoteness), location (distance from ports and capital), concentration of industry and services in Douala and Yaoundé, history of investment, migration. Measures: infrastructure (roads, power, Kribi port), decentralisation, growth poles and targeted programmes. Judgement: effective only when transport, services and jobs are developed together and funding and security are stable."),
        SUM("Main corridors: Douala-Yaoundé-Ngaoundéré (rail), Ngaoundéré-Maroua-N'Djamena, Yaoundé-Bertoua-Garoua-Boulaï, Douala-Bafoussam-Bamenda; ports at Douala and Kribi.",
            "Relief, rainfall, flooding, trade flows and finance shape transport; roads and port congestion are key problems.",
            "Regional inequalities form a core-periphery pattern: wealth and services concentrate around Douala and Yaoundé.",
            "Causes: physical limits, distance, concentration of investment and migration; measures: infrastructure, decentralisation, growth poles.",
            "Name places and give both progress and limits when evaluating."),
    ],
))

# ---------------------------------------------------------------------------
# 8. Topographic map reading and relief
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_MAP, topic="Topographic map reading and relief",
    title="Topographic map reading: scale, grid references, distance and relief description",
    slug="gpu2-topographic-map-reading-and-relief",
    minutes=24,
    summary="Reading a 1:50 000 topographic map with confidence: scale, six-figure references, bearings, distances, contour interpretation and a structured description of relief, using an invented map of the Kemo area.",
    objectives=[
        "Convert map distances to ground distances and give six-figure grid references and bearings",
        "Read heights from contours and spot heights and find relative relief",
        "Identify relief features (summit, spur, col, escarpment, valley, plateau) from contour patterns",
        "Describe the relief of a map area in sections, using grid lines and figures",
    ],
    key_concepts=["Representative fraction", "Six-figure reference", "Grid bearing", "Contour interval", "Spot height", "Relative relief", "Col", "Escarpment"],
    blocks=[
        H("Introduction"),
        T("Map work (Section A of Paper 3 in the 2023 Board report) is compulsory and is the most popular paper 3 question. The report said candidates "
          "could identify highland and lowland but often could not say **where** they were: west or east of a named grid line. Many described 'close contours' "
          "without saying what that meant for the slope. This lesson trains the skills that avoid those losses."),
        T("The map used in this and the next three lessons, **Map A**, is **invented** for teaching (an imaginary Kemo area). The heights, positions and "
          "calculations were checked by script. On a real exam map the skills are the same."),
        IMG(MAP_A, alt=MAP_A_ALT, caption="Figure 1. Map A (invented). Scale 1:50 000, grid squares 1 km, contour interval 50 m. Points A to E and the section line X-Y are used in the worked examples."),
        H("Scale and distance"),
        D("A **representative fraction** (RF) such as 1:50 000 means that 1 unit on the map is 50 000 of the same unit on the ground. On a 1:50 000 map, 1 cm on the map is 50 000 cm = 500 m = 0.5 km on the ground, so a 1 km grid square is 2 cm wide.", title="Scale"),
        EX("Worked example 1: straight-line and ground distance", intro="Find the straight-line distance from A (308 611) to B (336 616) on Map A.", steps=[
            S("Difference in eastings", math=r"336 - 308 = 28 \text{ hundreds of metres} = 2.8 \text{ km}"),
            S("Difference in northings", math=r"616 - 611 = 5 \text{ hundreds of metres} = 0.5 \text{ km}"),
            S("Pythagoras", math=r"d = \sqrt{2.8^2 + 0.5^2} = \sqrt{8.09} = 2.84 \text{ km}"),
            S("On the map", math=r"2.84 \text{ km} \div 0.5 \text{ km per cm} = 5.7 \text{ cm}", text="Measuring with a ruler should give about 5.7 cm. Give the ground distance with its unit."),
        ]),
        T("For a winding road or river, lay a thread or the edge of a paper strip along the route, mark the straight pieces, then measure the total against the scale bar."),
        H("Grid references and bearings"),
        D("A **six-figure grid reference** gives the easting first, then the northing. Each is three digits: the grid line number of the square's left (or lower) edge, followed by the tenths of the square. A point 8 tenths of the way from line 30 to line 31 gives 308.", title="Six-figure reference"),
        T("The summit A has a spot height of 1298 m and lies 8 tenths east of line 30 and 1 tenth north of line 61: its reference is **308 611**. "
          "Hill D (955 m) is at **359 607**. Always give eastings before northings: 'along the corridor, then up the stairs'."),
        D("A **grid bearing** is the angle measured clockwise from grid north (the north-south grid lines) to the line joining two points, written with three figures such as 080.", title="Grid bearing"),
        EX("Worked example 2: bearing", intro="Find the grid bearing of B from A.", steps=[
            S("Eastings and northings", text="B is 2.8 km east and 0.5 km north of A."),
            S("Angle from north", math=r"\tan\theta = \frac{\text{east}}{\text{north}} = \frac{2.8}{0.5} = 5.6 \Rightarrow \theta = 79.9^\circ"),
            S("Write it", text="The grid bearing of B from A is about 080 degrees (nearly due east). With a protractor you will read 080 within a degree or two."),
        ]),
        H("Reading heights and slopes"),
        KEY("Contour rules", "These make height reading reliable.", cards=[
            ["Heights", "A contour joins points of equal height. Here the interval is 50 m; every fifth contour (250 m) is drawn thicker. Spot heights give exact heights at points."],
            ["Between contours", "A point between the 1000 and 1050 contours has a height between those values; estimate from its position. Point E (330 613) lies between them, so about 1010 m."],
            ["Steepness", "Close contours mean a steep slope; wide spacing means a gentle slope. Even spacing means a uniform slope."],
            ["Direction of slope", "Height numbers show which way the land falls. Rivers cross contours at right angles, forming V shapes that point uphill."],
        ]),
        D("**Relative relief** is the difference in height between the highest and lowest points in an area. On Map A the highest point is A (1298 m) and the lowest is where the River Kemo leaves the map in the east (about 751 m): relative relief about 547 m.", title="Relative relief"),
        H("Relief features"),
        KEY("Features seen on Map A", "Give the grid reference of each feature you name.", cards=[
            ["Summit", "A (308 611, 1298 m): closed rings of contours around the highest ground."],
            ["Col", "C (about 315 607, about 1180 m): the low point on the ridge between summit A and the hill at about 320 604, where the contours of the two hills almost meet."],
            ["Escarpment", "The steep slope near easting 33 where contours are very close together, dropping from about 1100 m to about 850 m."],
            ["Plateau", "West of easting 33: a broad area at about 1100 to 1250 m with wide contour spacing."],
            ["Valley and flood plain", "The R. Kemo valley in the east: wide, low (about 750 to 800 m), with meanders, swamp and rice fields."],
            ["Hill", "D (359 607, 955 m): a rounded isolated hill rising above the lowland."],
        ]),
        EX("Worked example 3: describe the relief in sections", intro="Describe the relief of Map A.", steps=[
            S("Divide the map", text="Use the grid line at easting 33. West of it the land is a high plateau; east of it a low plain. State this first."),
            S("West of easting 33", text="Heights mostly between 1100 and 1300 m. The highest point is A (1298 m at 308 611). Contours are widely spaced on the plateau top, so slopes are gentle, but steep on the margin of summit A."),
            S("The boundary", text="Between eastings 32.7 and 33.3 the contours are very close; the land falls about 250 m in roughly 600 m: a steep escarpment (gradient about 1 in 2.5)."),
            S("East of easting 33", text="Low, mostly 750 to 850 m, gently sloping eastwards; the R. Kemo flows across it in a wide, meandering valley; isolated hill D reaches 955 m."),
            S("Compare", text="The plateau is about 400 m higher than the plain; the contrast is sharp because of the escarpment."),
        ]),
        TIP("Report on Paper 3 section A: marks were lost when candidates 'simply talked of close contours'. Say **what close contours mean** (steep slope), give **numbers** (heights, distances) and **locate** each statement with a grid line or reference.", title="Exam link"),
        MISTAKE("Giving the northing first", "Eastings (along the bottom) come before northings (up the side): 308 611, not 611 308."),
        MISTAKE("Calling every high area a hill", "A plateau is broad and fairly flat on top, a ridge is long and narrow, a summit is a point. Describe the shape using the contour pattern."),
        MISTAKE("Forgetting to convert distance", "Measuring 5.7 cm and answering '5.7' is incomplete. Convert with the scale and write km."),
        QUIZ("On Map A the distance between two points is 7.2 cm. The ground distance is",
             ["1.44 km", "3.6 km", "7.2 km", "36 km"], 1,
             "1 cm = 0.5 km, so 7.2 cm = 3.6 km.",
             feedback=["That divides by 5, not multiplies by 0.5.", "", "That ignores the scale.", "That uses 5 km per cm."]),
        QUIZ("Which statement best describes a col?",
             ["The highest point of a hill", "The lowest point on a ridge between two higher summits", "A very steep slope", "The meeting point of two rivers"], 1,
             "A col is a saddle: low ground between two peaks on a ridge.",
             feedback=["That is a summit.", "", "That is an escarpment or cliff.", "That is a confluence."]),
        PQ("Hill D lies 9 tenths of a square east of grid line 35 and 7 tenths north of grid line 60. Give its six-figure grid reference and state its height from the map.",
           "Easting 359 (35 then 9 tenths), northing 607 (60 then 7 tenths): 359 607. Its spot height is 955 m."),
        PQ("Two points are 4.6 cm apart on a 1:50 000 map. Find the ground distance in kilometres, and the map distance if the scale were 1:25 000 for the same ground distance.",
           "4.6 x 0.5 = 2.3 km. At 1:25 000, 1 cm = 0.25 km, so 2.3 km = 9.2 cm."),
        PQ("Describe the relief east and west of easting 33 on Map A and explain what the contour pattern between 32 and 34 shows.",
           "West: plateau at about 1100 to 1300 m, with the highest point A (1298 m); gentle slopes on the plateau top. East: lowland at 750 to 850 m, with the River Kemo, and hill D (955 m). Between eastings 32.7 and 33.3 the contours are tightly packed: a steep escarpment dropping about 250 m in about 600 m, a gradient of about 1 in 2.5."),
        SUM("On a 1:50 000 map, 1 cm = 0.5 km; always convert and give units.",
            "Six-figure reference: easting then northing, each with tenths of a square. Bearings are measured clockwise from grid north.",
            "Read heights from contours and spot heights; close contours mean steep slopes, wide spacing gentle slopes.",
            "Identify features by contour pattern: summit, col, escarpment, plateau, valley.",
            "Describe relief in sections with figures and grid lines, and compare the sections."),
    ],
))

# ---------------------------------------------------------------------------
# 9. Cross-sections, gradient and intervisibility
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_MAP, topic="Cross-sections, gradient and intervisibility",
    title="Cross-sections, gradient, vertical exaggeration and intervisibility",
    slug="gpu2-cross-sections-gradient-intervisibility",
    minutes=25,
    summary="How to draw a relief cross-section, calculate gradient in three forms, work out vertical exaggeration, and test intervisibility and dead ground, using the section X-Y on Map A.",
    objectives=[
        "Draw a cross-section from contours using the paper-strip method with a sensible vertical scale",
        "Calculate gradient as 1 in n, a percentage and an angle",
        "Calculate vertical exaggeration and explain its effect on the shape of a section",
        "Decide whether two points are intervisible and identify dead ground",
    ],
    key_concepts=["Cross-section", "Vertical scale", "Vertical exaggeration", "Gradient", "Intervisibility", "Dead ground", "Line of sight"],
    blocks=[
        H("Introduction"),
        T("A map is a view from above. A **cross-section** shows the land as if sliced along a line, so you can see slope, valleys and escarpments. "
          "The same slice lets you test whether one place can be seen from another (**intervisibility**). Practical questions on this lesson often ask for "
          "a gradient or a vertical exaggeration; the 2023 report reminded teachers to give plenty of practice with calculations in map work."),
        IMG("algpu2-map-a.svg", alt=MAP_A_ALT, caption="Figure 1. Map A again. The section line X-Y runs from 302 611 to 368 607 and passes over summit A and hill D."),
        H("Drawing a cross-section"),
        KEY("The paper-strip method", "Follow the steps in order.", cards=[
            ["1. Prepare the strip", "Lay the straight edge of a strip of paper along the line X-Y. Mark X and Y."],
            ["2. Mark the crossings", "At each place where a contour (or river or spot height) touches the strip, mark it and write its height."],
            ["3. Set up the graph", "Draw a baseline the same length as the strip (the horizontal scale is the map scale). Draw a vertical axis with a scale that spans the range of heights."],
            ["4. Plot and join", "Place the strip on the baseline, mark the heights above each point, then join the dots with a smooth line (not straight segments). Label X, Y and features."],
            ["5. Finish", "Add titles, scales, the vertical exaggeration and labels for the river, escarpment, summits."],
        ]),
        CODE("Distance from X (km)   Height (m)\n0.00                  1198  (X)\n0.34                  1250\n0.60                  1298  (A)\n0.84                  1250\n1.13                  1200\n2.23                  1150\n2.61                  1100\n2.74                  1050\n2.83                  1000\n2.91                   950\n3.02                   900\n3.22                   850\n5.07                   850\n5.33                   900\n5.60                   950\n5.71                   955  (D)\n5.81                   950\n6.07                   900\n6.29                   850\n6.61                   807  (Y)",
             "text", title="Table 1. Readings along X-Y on Map A (distances to 0.01 km)"),
        EX("Worked example 1: choose scales and draw", intro="The section X-Y is 6.61 km long. Heights range from 807 m to 1298 m. Choose scales for a section on a page 14 cm wide.", steps=[
            S("Horizontal scale", text="Keep the map scale: 1:50 000, so 1 cm = 0.5 km. The line is 6.61 km = 13.2 cm: it fits."),
            S("Vertical range", math=r"1298 - 807 = 491 \text{ m}"),
            S("Vertical scale", text="Choose 1 cm = 100 m. The section is then 4.9 cm high: a convenient size, with the baseline at 700 m."),
            S("Plot", text="Mark each height from Table 1 above its distance, join with a smooth line, label A, D, the escarpment and the lowland, and write the scales and the vertical exaggeration."),
        ]),
        IMG("algpu2-section-xy.svg", alt="Cross-section along X-Y: height from 1298 m at summit A falling to a plateau near 1150 m, then dropping steeply at the escarpment near 3 km to a lowland near 830 m, rising to hill D at 955 m near 5.7 km; a dashed line of sight from A to D clears the ground, with dead ground marked below it",
            caption="Figure 2. The completed section with a line of sight from A to D. Vertical exaggeration x5."),
        H("Vertical exaggeration"),
        D("**Vertical exaggeration** (VE) shows how much the heights have been stretched compared with distances. It equals the horizontal scale divided by the vertical scale, using the same units. If it equals 1, the section is true to scale.", title="Vertical exaggeration", formula=r"\text{VE} = \frac{\text{vertical scale}}{\text{horizontal scale}}"),
        EX("Worked example 2: calculate VE", intro="Horizontal scale 1:50 000. Vertical scale 1 cm = 100 m. Find the vertical exaggeration.", steps=[
            S("Convert the vertical scale", math=r"1 \text{ cm} : 100 \text{ m} = 1 \text{ cm} : 10\,000 \text{ cm} = 1 : 10\,000"),
            S("Divide", math=r"\text{VE} = \frac{1/10\,000}{1/50\,000} = \frac{50\,000}{10\,000} = 5"),
            S("Write it", text="The section has a vertical exaggeration of x5 (five times): every slope looks steeper than it is."),
        ]),
        T("Exaggeration helps the eye see low relief, but it distorts steepness. A real slope of 1 in 2.45 (22 degrees, the escarpment) has tan 22.2 = 0.408. "
          "On a section with VE 5 the apparent slope has tan = 5 x 0.408 = 2.04, so it looks like about 64 degrees. Always state the VE next to a section."),
        H("Gradient"),
        D("**Gradient** is the steepness of a slope: vertical interval (VI) divided by horizontal equivalent (HE). It can be given as a ratio (1 in n), a percentage or an angle.", title="Gradient",
          formula=r"\text{gradient} = \frac{\text{VI}}{\text{HE}}, \quad 1 \text{ in } n \text{ with } n = \frac{\text{HE}}{\text{VI}}"),
        EX("Worked example 3: gradient from A to B", intro="Find the average gradient from the summit A (1298 m, 308 611) to the spot height B (817 m, 336 616).", steps=[
            S("Vertical interval", math=r"\text{VI} = 1298 - 817 = 481 \text{ m}"),
            S("Horizontal equivalent", math=r"\text{HE} = 2.84 \text{ km} = 2844 \text{ m}"),
            S("Ratio", math=r"n = \frac{2844}{481} = 5.9 \Rightarrow 1 \text{ in } 5.9"),
            S("Percentage", math=r"\frac{481}{2844} \times 100 = 16.9\%"),
            S("Angle", math=r"\theta = \tan^{-1}\left(\frac{481}{2844}\right) = 9.6^\circ"),
            S("Say what it means", text="This is a steep average slope, mostly because of the escarpment between the two points."),
        ]),
        EX("Worked example 4: compare slopes", intro="The escarpment: the ground falls from 1100 m to 850 m between 2.61 km and 3.22 km on the section. Compare it with the river gradient.", steps=[
            S("HE and VI", math=r"\text{HE} = (3.22 - 2.61) \times 1000 = 610 \text{ m}, \quad \text{VI} = 250 \text{ m}"),
            S("Escarpment gradient", math=r"610 \div 250 = 2.44 \Rightarrow 1 \text{ in } 2.4"),
            S("River on the lowland", text="The R. Kemo falls from 777 m to 751 m over about 4.06 km of channel."),
            S("Gradient of the river", math=r"4060 \div 26 = 156 \Rightarrow 1 \text{ in } 156"),
            S("Compare", text="The escarpment is about 60 times steeper than the river on the plain, so the river forms a waterfall and rapids at the escarpment and meanders slowly on the plain."),
        ]),
        H("Intervisibility and dead ground"),
        D("Two points are **intervisible** if you can see one from the other: no ground lies above the straight line joining them. **Dead ground** is land that cannot be seen from a given viewpoint because higher ground hides it.", title="Intervisibility"),
        KEY("How to test intervisibility", "Do it on the section, not on the map.", cards=[
            ["1", "Draw a cross-section along the line joining the two points (to the same scale)."],
            ["2", "Mark the two points on the section. Add the height of the observer's eye (about 1.5 m) if the question says so; it hardly shows at this scale."],
            ["3", "Join the points with a straight line: the line of sight."],
            ["4", "If the ground profile rises above the line anywhere between them, they are not intervisible. Land that falls below the line extended beyond that obstacle is dead ground."],
        ]),
        EX("Worked example 5: intervisibility on Map A", intro="Is hill D visible from summit A?", steps=[
            S("Section", text="Use Figure 2: A is at 1298 m at 0.60 km and D at 955 m at 5.71 km."),
            S("Line of sight", text="Join them. The line falls steadily from 1298 to 955 m."),
            S("Check the ground", text="Between them the profile is below the line everywhere: the plateau falls away at the escarpment and the lowland is far below. The ground falls away from A so quickly that no point rises above the line."),
            S("Conclusion", text="D is visible from A. The lowland between about 2.4 km and 5.2 km from X is dead ground as seen from A, hidden by the plateau edge."),
        ]),
        T("By contrast, point B (817 m, at the foot of the escarpment) is not visible from A. Along the line A to B, the ground at the escarpment brow is about 150 m above the line of sight, so the escarpment blocks the view."),
        TIP("The 2023 Board report described the compulsory map question in Paper 3 as covering relief, drainage and human activity, with calculations such as sinuosity, and asked for more practical exercises in teaching. Cross-sections, gradients and intervisibility are standard map-work techniques. Show formula, substitution, answer and unit.", title="Exam link"),
        MISTAKE("Joining the section points with straight lines", "Use a smooth curve; a ruler-drawn zigzag misrepresents landforms and loses marks for accuracy."),
        MISTAKE("Mixing units in VE or gradient", "Convert metres and kilometres to the same unit before dividing. 481 m over 2.84 km is not 481 over 2.84."),
        MISTAKE("Checking intervisibility on the map", "Close contours between two points do not prove they are hidden. Draw the section and the line of sight."),
        QUIZ("A section has a horizontal scale of 1:25 000 and a vertical scale of 1 cm = 50 m. The vertical exaggeration is",
             ["x2", "x5", "x10", "x0.5"], 1,
             "1 cm = 50 m = 5 000 cm, so the vertical scale is 1:5 000. VE = 25 000 / 5 000 = 5.",
             hint="Convert 1 cm to 50 m into a ratio first.",
             feedback=["That divides 50 by 25.", "", "That would need a vertical scale of 1:2 500.", "That inverts the ratio."]),
        QUIZ("Which statement about intervisibility is correct?",
             ["Two points are intervisible if the contours between them are widely spaced", "Two points are intervisible if no ground rises above the straight line joining them", "Two points at the same height are always intervisible", "Intervisibility is tested by measuring the bearing between points"], 1,
             "Draw the section and the line of sight; ground above the line blocks the view.",
             feedback=["Contour spacing does not decide it.", "", "A ridge between them can still block the view.", "Bearings give direction, not visibility."]),
        PQ("A road climbs 150 m over a horizontal distance of 1.2 km. Give the gradient as 1 in n, a percentage and an angle.",
           "n = 1200 / 150 = 8, so 1 in 8; percentage 150 / 1200 x 100 = 12.5 per cent; angle = tan inverse of 0.125 = 7.1 degrees."),
        PQ("Explain what is meant by vertical exaggeration and why it is used.",
           "VE is the ratio of the vertical scale to the horizontal scale. It stretches heights so that small differences in relief are visible, but it makes slopes look steeper than they are, so the VE must be stated."),
        PQ("On a section the line of sight from point P (900 m) to point Q (850 m) passes over a ridge 910 m high between them. Are P and Q intervisible? Explain.",
           "No. The ridge top at 910 m is higher than the line of sight, which lies between 900 and 850 m. The ridge blocks the view, and the ground just beyond it is dead ground."),
        SUM("Draw a section with the paper strip: mark crossings, choose a vertical scale, plot and join with a smooth line.",
            "VE = horizontal scale divided by vertical scale in the same units; state it on the section.",
            "Gradient = VI / HE, given as 1 in n, a percentage or an angle; always convert to the same units first.",
            "Intervisibility: draw the line of sight on a section; any ground above the line blocks the view and creates dead ground.",
            "Show working: formula, substitution, answer and units."),
    ],
))

# ---------------------------------------------------------------------------
# 10. Drainage analysis
# ---------------------------------------------------------------------------
MAP_B_ALT = ("Invented 1:50 000 map of the R. Mewa basin (eastings 50-57, northings 20-25): dashed watershed, 15 streams of orders 1 to 3 "
             "flowing from NW, N and E to the outlet Q at 558 200; P at 532 223 marks the start of the third-order channel.")

LESSONS.append(lesson(
    module=M_MAP, topic="Drainage analysis",
    title="Drainage analysis: stream order, bifurcation ratio, density and sinuosity",
    slug="gpu2-drainage-analysis-map-work",
    minutes=25,
    summary="Quantitative drainage analysis from a map: Strahler stream ordering, bifurcation ratio, drainage density, stream frequency, sinuosity and channel gradient, with interpretation, using an invented drainage basin.",
    objectives=[
        "Order the streams of a drainage basin using Strahler's method",
        "Calculate bifurcation ratios, drainage density, stream frequency and sinuosity",
        "Interpret each value in terms of rock, rainfall, slope and flood behaviour",
        "Describe a drainage pattern and the shape of a drainage basin",
    ],
    key_concepts=["Strahler order", "Bifurcation ratio", "Drainage density", "Stream frequency", "Sinuosity", "Drainage pattern", "Watershed"],
    blocks=[
        H("Introduction"),
        T("Rivers on a map are more than blue lines. Counting and measuring them tells you how fast water leaves a basin, how easily rock lets water soak in, and how likely floods are. "
          "In the 2023 Board report the compulsory map question included a **calculation of the sinuosity** of a named river between two points and the **meaning of the value**. "
          "The report said that the calculation was usually done well but that many candidates could not interpret the result. This lesson covers both."),
        T("Map B is an **invented** drainage basin for teaching. Lengths, areas and ratios were measured by script from the same data that drew the map."),
        IMG("algpu2-map-b.svg", alt=MAP_B_ALT, caption="Figure 1. Map B (invented): the R. Mewa basin. Scale 1:50 000, grid squares 1 km, contour interval 50 m. Circled numbers give the Strahler order of each stream."),
        H("Strahler stream ordering"),
        KEY("The rules", "Apply them from the smallest streams downstream.", cards=[
            ["Order 1", "Every stream with no tributaries (starts at a source) is first order."],
            ["When streams meet", "Where two streams of the same order meet, the stream below the confluence has the next order up (two order 1 make order 2)."],
            ["No change", "Where streams of different orders meet, the larger order continues unchanged (order 1 joining order 2 gives order 2)."],
            ["Highest order", "The order of the basin is the order of the main stream at the outlet."],
        ]),
        T("On Map B there are 11 first-order streams, 3 second-order streams and one third-order channel, 15 streams in all. The third-order channel runs from the "
          "junction of the two main western and northern second-order branches (point P at 532 223) to the outlet Q at 558 200."),
        CODE("Order   Number   Total length (km)   Mean length (km)\n1         11        14.06              1.28\n2          3         4.32              1.44\n3          1         4.12              4.12\nAll       15        22.49", "text", title="Table 1. Stream data for Map B (measured by script)"),
        H("Bifurcation ratio"),
        D("The **bifurcation ratio** (Rb) is the number of streams of one order divided by the number of the next higher order. A mean value for the basin is the average of the ratios.", title="Bifurcation ratio", formula=r"R_b = \frac{N_u}{N_{u+1}}"),
        EX("Worked example 1: bifurcation ratios for Map B", intro="Use Table 1 to find Rb for orders 1 to 2 and 2 to 3, and the mean.", steps=[
            S("Order 1 to 2", math=r"R_{b(1:2)} = \frac{11}{3} = 3.67"),
            S("Order 2 to 3", math=r"R_{b(2:3)} = \frac{3}{1} = 3.0"),
            S("Mean", math=r"\bar{R}_b = \frac{3.67 + 3.0}{2} = 3.33"),
            S("Interpret", text="Values of about 3 to 5 are typical of basins in which geology does not strongly control the drainage (check your textbook). A mean of 3.3 suggests a normal, branching dendritic pattern with no unusual structural control."),
        ]),
        H("Drainage density and stream frequency"),
        D("**Drainage density** (Dd) is the total length of all streams in a basin divided by the basin area. **Stream frequency** is the number of streams divided by the area.", title="Drainage density and stream frequency", formula=r"D_d = \frac{\sum L}{A}, \quad F = \frac{N}{A}"),
        EX("Worked example 2: Dd and frequency", intro="Map B has total stream length 22.49 km and a basin area of 24.5 km squared (measured from the watershed). Find Dd and the stream frequency.", steps=[
            S("Drainage density", math=r"D_d = \frac{22.49}{24.5} = 0.92 \text{ km/km}^2"),
            S("Stream frequency", math=r"F = \frac{15}{24.5} = 0.61 \text{ streams per km}^2"),
            S("Interpret", text="This is a moderate-to-low density. Low values often go with permeable rock, dense vegetation, gentle slopes or low rainfall; high values (above about 2 km/km2) with impermeable rock, steep slopes or intense rainfall (check your textbook for classes)."),
            S("Link to flooding", text="Water is shed more slowly than in a basin with high Dd, so peak flows after rain are lower and later: a lower flood risk."),
        ]),
        TIP("When asked for area, count whole squares and parts of squares inside the watershed (each square here is 1 km squared). Your answer may differ slightly from the exact value, so state your method and give the result to 1 decimal place."),
        H("Sinuosity and gradient of a channel"),
        D("**Sinuosity** is the length of the river channel divided by the straight-line distance between the same two points. A value of 1 means a straight channel. Values of about 1.05 to 1.5 are called sinuous and above about 1.5 meandering (check your textbook).", title="Sinuosity", formula=r"\text{sinuosity} = \frac{\text{channel length}}{\text{straight-line distance}}"),
        EX("Worked example 3: sinuosity and gradient from P to Q", intro="P (532 223) is at 415 m and Q (558 200) is at 300 m. The channel from P to Q measures 4.12 km along its bends, and the straight line from P to Q measures 3.47 km. Find the sinuosity and the average gradient.", steps=[
            S("Sinuosity", math=r"\frac{4.12}{3.47} = 1.19"),
            S("Meaning", text="1.19 means the channel is 19 per cent longer than a straight line: it is moderately sinuous, with gentle bends rather than strong meanders."),
            S("Vertical interval", math=r"415 - 300 = 115 \text{ m}"),
            S("Gradient", math=r"\frac{4120}{115} = 35.8 \Rightarrow 1 \text{ in } 36 \text{ (2.8 per cent)}"),
            S("Interpret", text="This is a moderate gradient. A fairly steep, only moderately bendy channel suggests energy used mainly for downcutting rather than lateral erosion and meander growth."),
        ]),
        H("Drainage patterns and basin shape"),
        KEY("Common patterns", "Name the pattern and link it to geology.", cards=[
            ["Dendritic", "Tree-like branching; uniform rock and gentle slopes. Map B is mostly dendritic."],
            ["Radial", "Streams flow outwards from a high point such as a volcano or dome."],
            ["Trellis", "Parallel main streams with short tributaries at right angles; folded alternating hard and soft rocks."],
            ["Rectangular and parallel", "Streams follow joints and faults; or flow down uniform steep slopes."],
        ]),
        T("A **drainage basin** is the area drained by one river system; its boundary is the **watershed**, drawn along the highest ground. "
          "A rounded basin brings tributaries to the outlet at about the same time (a sharp flood peak); an elongated basin spreads the arrival of water (a flatter peak). "
          "Map B is moderately elongated, with the outlet on the southern edge."),
        EX("Worked example 4: describe the drainage of Map B", intro="Describe the drainage and drainage pattern shown on Map B.", steps=[
            S("Pattern", text="Mostly dendritic: tributaries join the main streams at acute angles, suggesting uniform rock."),
            S("Direction", text="Streams rise on the high ground in the north-west, north and east (about 500 m at the watershed) and flow towards the outlet Q at 558 200 (300 m)."),
            S("Structure of the network", text="The western and northern second-order streams meet at P to form the third-order channel; the eastern second-order stream and three first-order streams join it further downstream."),
            S("Numbers", text="Mean bifurcation ratio 3.3, drainage density 0.92 km per km squared; the channel from P to Q has a sinuosity of 1.19."),
        ]),
        MISTAKE("Counting orders from the mouth", "Start at the headwaters: first-order streams are the tiny ones at the sources."),
        MISTAKE("Raising the order when different orders meet", "Order 1 joining order 2 leaves order 2. Only two streams of equal order raise the order."),
        MISTAKE("Giving a sinuosity and stopping", "The 2023 report said candidates could not interpret the value. Say what it means: how bendy the channel is, how fast the river flows, what that suggests about gradient and erosion."),
        QUIZ("At a confluence, an order 2 stream meets an order 1 stream. The stream below the confluence is",
             ["Order 1", "Order 2", "Order 3", "Order 1.5"], 1,
             "Only two streams of the same order make the next higher order. Here order 2 continues.",
             feedback=["The order cannot go down.", "", "That needs two order 2 streams.", "Orders are whole numbers."]),
        QUIZ("A river channel is 8.4 km long and the straight-line distance between its ends is 6.0 km. Its sinuosity is",
             ["0.71", "1.4", "2.4", "14.4"], 1,
             "8.4 divided by 6.0 = 1.4: a sinuous channel.",
             feedback=["That inverts the fraction.", "", "That subtracts.", "That adds."]),
        PQ("A basin has 24 first-order, 6 second-order, 2 third-order and 1 fourth-order streams. Calculate the bifurcation ratios and the mean.",
           "24/6 = 4.0; 6/2 = 3.0; 2/1 = 2.0. Mean = (4 + 3 + 2) / 3 = 3.0."),
        PQ("A basin of 32 km squared has streams with a total length of 60 km. Calculate the drainage density and interpret it.",
           "60 / 32 = 1.9 km per km squared. This is a moderately high density: suggests fairly impermeable rock or steep slopes or a rainy climate; the basin sheds water quickly, so floods are more likely than in a low-density basin."),
        PQ("For Map B, explain what a sinuosity of 1.19 and a gradient of 1 in 36 tell you about the channel from P to Q.",
           "1.19: channel 19 per cent longer than a straight line, so moderately sinuous, with gentle bends, not true meanders. 1 in 36 (2.8 per cent): a moderate gradient, so the river has considerable energy and flows fairly quickly; erosion is mainly downwards, which limits bend development. Together they suggest a youthful to middle-course channel."),
        SUM("Strahler order: order 1 is a stream with no tributaries; only equal orders meeting raise the order.",
            "Bifurcation ratio = N(u) / N(u+1); mean values of 3 to 5 are typical. Map B: 3.67, 3.0, mean 3.33.",
            "Drainage density = total stream length / area (Map B 0.92 km per km squared); stream frequency = streams / area (0.61).",
            "Sinuosity = channel length / straight distance (Map B P to Q: 1.19); gradient = VI / HE (1 in 36).",
            "Always interpret values: rock, slope, rainfall, flood speed."),
    ],
))

# ---------------------------------------------------------------------------
# 11. Interpreting physical and human relationships on maps
# ---------------------------------------------------------------------------
LESSONS.append(lesson(
    module=M_MAP, topic="Interpreting physical and human relationships on maps",
    title="Interpreting physical and human relationships on a topographic map",
    slug="gpu2-physical-human-relationships-on-maps",
    minutes=25,
    summary="How to use map evidence to explain why settlements, roads, farming and possible development projects are where they are, and to suggest strategies and judge potential, using Map A.",
    objectives=[
        "Explain the siting and pattern of settlements using relief, drainage and routes",
        "Explain the course of a road and the difficulties of road building from map evidence",
        "Judge the potential for irrigation, farming and hydroelectric power from map evidence only",
        "Write a structured answer: evidence, physical reason, human response, evaluation",
    ],
    key_concepts=["Site", "Situation", "Nucleated settlement", "Dispersed settlement", "Route", "Map evidence", "Potential"],
    blocks=[
        H("Introduction"),
        T("The last part of a map question usually asks you to link physical and human features: why the village is where it is, why the road bends, whether a dam or irrigation scheme is possible. "
          "The 2023 Board report said the compulsory map question covered relief, drainage, road network development, irrigation and hydroelectric power and the problems of rice farmers. "
          "It also said that many candidates drifted into general problems (poor roads, lack of capital) instead of using **map evidence only**, and could not show the relationship between mapped features. This lesson shows how to avoid that."),
        IMG(MAP_A, alt=MAP_A_ALT, caption="Figure 1. Map A (invented) again. Scale 1:50 000, contour interval 50 m."),
        KEY("A four-part method", "Use it for every 'explain why' question on a map.", cards=[
            ["1. Evidence", "Say what the map shows with a grid reference or figure (for example 'the road climbs 281 m in 1.8 km near 326 643')."],
            ["2. Physical reason", "Name the relief, drainage or soil factor that explains it."],
            ["3. Human response", "State how people have responded: sited, routed or adapted."],
            ["4. Evaluation", "Say whether it works, what limits it, or what could be improved."],
        ]),
        H("Settlements"),
        T("Map A shows three kinds of settlement. **Kemo** (about 347 to 351, 629 to 632) is a compact, **nucleated** village beside the main road, on the lowland about 25 m above the swamps "
          "and river. **Bafu** (about 304 to 323, 634 to 640) is a **dispersed** group of buildings spread over the plateau. **Ndu** (about 350 611) is a small hamlet beside a track, on gentle ground."),
        EX("Worked example 1: explain the site of Kemo", intro="Explain the site and growth of the village of Kemo.", steps=[
            S("Evidence", text="Kemo lies at about 786 m, on gently sloping land next to the main road, just north of the R. Kemo and near the junction with a track at 349 630."),
            S("Physical reasons", text="Flat or gently sloping land for building; water from the R. Kemo and R. Tolo within a kilometre; land above the swamp (about 760 m) and so above the usual flood level; the road reaches it along level ground."),
            S("Human response", text="A nucleated village grew at the road junction (a route centre), where traders and farmers meet; farmland on the flood plain and rice fields lie to the south-east."),
            S("Evaluation", text="Good site for water and access, but flooding in the swamp area limits expansion southwards."),
        ]),
        EX("Worked example 2: contrast two patterns", intro="Contrast the settlement pattern of the plateau with that of the lowland.", steps=[
            S("Plateau (Bafu)", text="Buildings are scattered at about 1180 m among farms; gentle slopes and fairly even terrain allow people to live near their fields; the map shows no water source nearby, so say 'probably springs or wells'."),
            S("Lowland (Kemo)", text="Compact village at a junction; low land with only limited dry ground, so people cluster on the dry ground away from the swamp and near the road."),
            S("Reason for difference", text="Dispersed settlement suits even land with scattered farming; nucleation develops where a route, water or dry sites attract people to one spot."),
        ]),
        H("Roads and routes"),
        T("The main road enters at the east edge near 370 634, passes through Kemo, crosses the R. Tolo near 345 632 by a bridge and then turns up the escarpment in a series of **hairpin bends** to the plateau, reaching Bafu and leaving the map at the west edge at about 300 638."),
        EX("Worked example 3: why the road zigzags", intro="Explain why the road has hairpin bends between about 335 635 and 326 643, and calculate the gradient it achieves.", steps=[
            S("Evidence", text="The road climbs from about 807 m to about 1088 m: 281 m, with a road length of about 1.82 km, between points only about 1.10 km apart in a straight line."),
            S("Gradient with bends", math=r"\frac{1823}{281} = 6.5 \Rightarrow 1 \text{ in } 6.5 \; (15.4\%)"),
            S("Gradient if straight", math=r"\frac{1097}{281} = 3.9 \Rightarrow 1 \text{ in } 3.9 \; (25.6\%)"),
            S("Reason", text="A straight road up the escarpment would be much too steep for lorries and buses; hairpins spread the climb over a longer route, lowering the gradient."),
            S("Cost", text="The road is about 66 per cent longer than a straight road: higher costs of building and maintenance, slower journeys, landslide and erosion risks on the escarpment."),
        ]),
        KEY("Difficulties for road building on Map A", "All of them can be proved from the map.", cards=[
            ["Relief", "The escarpment at easting 33 (gradient about 1 in 2.4) forces hairpins; deep cuttings and embankments."],
            ["Drainage", "Rivers need bridges (R. Tolo near 345 632) and the swamp near 352 to 368, 618 to 625 would need raised roads and drainage."],
            ["Other", "Forest along the escarpment near easting 328 must be cleared; heavy rain would increase erosion on steep slopes (general knowledge, not map evidence)."],
        ]),
        H("Farming and development potential"),
        KEY("Evidence for farming", "Use the key and the contours.", cards=[
            ["Rice", "The rice fields (355 to 363, 616 to 618) lie on flat, low land beside the swamp and R. Kemo; there is a water supply and level ground."],
            ["Plateau farming", "The plateau is gently sloping and about 1150 m high, so cooler; farmland around Bafu on gentle slopes."],
            ["Limits", "Steep escarpment slopes and swampy ground are unsuitable for most crops; flooding and waterlogging are problems for rice farmers; the map cannot tell us soil quality."],
        ]),
        EX("Worked example 4: potential for hydroelectric power", intro="Using map evidence only, describe the possibility of generating hydroelectric power (HEP) on the R. Kemo.", steps=[
            S("Head of water", text="The river falls from about 1060 m to about 820 m between easting 32.5 and 33.0, a drop of about 240 m in about 0.56 km: a gradient of about 1 in 2.3, with a waterfall at 329 628."),
            S("Flow", text="The Kemo is the main river and is joined by the R. Tolo; the map does not show discharge, so we cannot tell how much water flows in the dry season."),
            S("Site and access", text="The falls are close to the main road and about 2 km from Kemo, so equipment and electricity could reach the village; the plateau side has space for a reservoir."),
            S("Evaluation", text="The high, concentrated head makes the site attractive for HEP, but discharge data, flood risk and cost need study. The map shows potential, not certainty."),
        ]),
        EX("Worked example 5: irrigation", intro="Describe the possibility of irrigating farmland in the area east of the escarpment.", steps=[
            S("Water source", text="The R. Kemo and R. Tolo flow across the lowland, and the swamp shows that the water table is high."),
            S("Land", text="The land is flat or gently sloping (the river falls only about 1 in 156), so water can be spread by gravity canals and fields can be levelled."),
            S("Existing use", text="Rice fields beside the swamp near 355 to 363, 616 to 618 show that rice is already grown."),
            S("Limits", text="Flooding, waterlogging and the need for drainage; the map does not show soil or rainfall; canals and pumps cost money."),
        ]),
        TIP("In your answer, use only map evidence when the question says so, even if you know more. Avoid general statements such as 'lack of capital'. Write grid references, heights, distances and gradients. The report said answers that drifted into other problems scored poorly.", title="Exam link"),
        MISTAKE("Naming problems that are not on the map", "If the question says 'from map evidence', cite grid references and features, not poor roads or lack of money."),
        MISTAKE("Saying 'because of relief' without detail", "Explain how: gentle slopes, flat sites, water, level routes, steep slopes avoided."),
        MISTAKE("Describing without linking", "State the relationship: 'the road follows the valley because the gradient is gentle', not just 'the road is in the valley'."),
        QUIZ("Which map evidence best supports hydroelectric power potential at 329 628?",
             ["A wide meandering river on flat land", "A waterfall with a large drop in height over a short distance", "Rice fields beside the river", "A main road crossing the river"], 1,
             "A large drop concentrated in a short distance gives a high head of water, which drives turbines.",
             feedback=["That shows slow flow and low head.", "", "That shows irrigation potential.", "That shows access, not head."]),
        QUIZ("Why are hairpin bends used where the road climbs the escarpment?",
             ["To make the journey faster", "To reduce the gradient by lengthening the route", "To avoid the R. Tolo", "Because the land is flat"], 1,
             "A longer, winding route spreads the climb, so the gradient is lower and vehicles can climb.",
             feedback=["They make the route longer and slower.", "", "The river is crossed elsewhere.", "The escarpment is steep."]),
        PQ("Suggest two physical difficulties of building a road network in the area shown on Map A, using map evidence only.",
           "(1) The steep escarpment near easting 33, where the land falls about 250 m in about 600 m (gradient about 1 in 2.4), needs hairpin bends and costly cuttings. (2) The swamp around 352 to 368, 618 to 625 and the rivers (R. Tolo near 345 632) need raised embankments and bridges."),
        PQ("Describe the possibility of irrigation and HEP generation in the area of Map A using map evidence only.",
           "Irrigation: rivers Kemo and Tolo and a swamp on a flat lowland, existing rice fields at 355 to 363, 616 to 618; gentle river gradient of about 1 in 156 allows gravity canals. HEP: a drop of about 240 m over about 0.56 km at the waterfall at 329 628 gives a high head; the main road is near for access. Limits: discharge unknown."),
        PQ("Explain why Kemo is a nucleated village and Bafu a dispersed settlement.",
           "Kemo: at a road junction beside rivers on dry ground above the swamp; routes and dry land attract people into one place. Bafu: on the plateau with gentle even slopes and scattered farmland, so houses are spread near fields; no single site is better than others."),
        SUM("Use evidence, physical reason, human response and evaluation in every 'explain' answer.",
            "Settlements follow dry sites, water and routes: nucleated at junctions, dispersed on even farmland.",
            "Roads avoid steep slopes: hairpins turn 1 in 3.9 into 1 in 6.5 at the cost of 66 per cent more length.",
            "Potential: HEP needs head and flow (the falls, 240 m in 0.56 km); irrigation needs water, level land and drainage.",
            "When asked for map evidence only, give grid references and figures, not general knowledge."),
    ],
))

# ---- end of lessons ----
