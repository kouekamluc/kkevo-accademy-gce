"""Form 5 Geography: The Geography of Cameroon (Background and Physical characteristics), 5 lessons."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
BACK = "Background of Cameroon"
PHYS = "Physical characteristics"

LESSONS = []

# ------------------------------------------------------------------ 1. Location and administrative map
LESSONS.append(lesson(
    module=MODULE,
    topic=BACK,
    title="Location of Cameroon and the administrative map",
    slug="cmr-location-and-administrative-map",
    minutes=22,
    summary="Locate Cameroon in Africa by latitude, longitude and neighbours, and learn the ten regions and their headquarters so you can sketch the administrative map.",
    objectives=[
        "Locate Cameroon in Africa using latitude, longitude and areal (neighbouring) location",
        "Identify the countries and the ocean that border Cameroon",
        "Name the ten regions of Cameroon and their regional headquarters",
        "Draw a sketch map of Cameroon showing the regional headquarters",
    ],
    key_concepts=["Latitude", "Longitude", "Areal location", "Region", "Regional headquarters", "Sketch map"],
    blocks=[
        H("Introduction"),
        T("A traveller who leaves Douala by road for Maroua passes through forest, hills, savanna and finally dry Sahel country. "
          "The journey is more than a thousand kilometres by road, yet it stays inside one country. "
          "This is why Cameroon is often called 'Africa in miniature'."),
        T("Before you study the land, climate and people of Cameroon, you must know **where** Cameroon is. "
          "A geography examiner expects you to locate a country in three ways: by latitude, by longitude and by the places around it."),
        H("Locating Cameroon in Africa"),
        D("**Latitude** is the distance of a place north or south of the Equator, measured in degrees. "
          "The Equator is 0°. Lines of latitude run east to west.", title="Latitude"),
        D("**Longitude** is the distance of a place east or west of the Greenwich (Prime) Meridian, measured in degrees. "
          "The Greenwich Meridian is 0°. Lines of longitude run from the North Pole to the South Pole.", title="Longitude"),
        D("**Areal location** (also called relative location) says which area a place is in and what lies around it: "
          "neighbouring countries, seas and oceans.", title="Areal location"),
        IMG("f5g-cmr-africa-location.svg",
            alt="Sketch map of Africa with Cameroon in dark green, north of the Equator and east of the Greenwich Meridian at the head of the Gulf of Guinea",
            caption="Figure 1. Cameroon in Africa: north of the Equator, east of Greenwich, at the inner corner of the Gulf of Guinea. Simplified sketch map, not to scale."),
        KEY("Cameroon's latitude and longitude", "Use these figures in your answers. They are approximate.", cards=[
            ["Latitude", "From about 2°N in the south to about 13°N in the far north. The whole country is north of the Equator."],
            ["Longitude", "From about 8.5°E in the west to about 16°E in the east. The whole country is east of Greenwich."],
            ["Position in Africa", "West-Central Africa, at the inner corner of the Gulf of Guinea (part of the Atlantic Ocean)."],
        ]),
        T("Because Cameroon lies between about 2°N and 13°N, it is inside the **tropics** (the zone between the Tropic of Cancer and the Tropic of Capricorn). "
          "It is close to the Equator in the south and nearer to the edge of the Sahara in the north. This explains why the south is hot and wet and the north is hot and dry."),
        EX("Worked example 1: size from latitude", intro="Take 1° of latitude as about 111 km. About how far is it from the southern tip of Cameroon (2°N) to the northern tip (13°N)?", steps=[
            S("Find the difference in latitude", math=r"13° - 2° = 11°"),
            S("Multiply by the length of one degree", math=r"11 \times 111 = 1\,221 \text{ km}"),
            S("Give a sensible answer", text="Cameroon is about 1,200 km long from north to south. This is an estimate in a straight line, not the road distance."),
        ]),
        H("The neighbours of Cameroon"),
        IMG("f5g-cmr-neighbours.svg",
            alt="Sketch map of Cameroon with latitude and longitude lines and its neighbours: Nigeria to the west, Chad to the north-east, Central African Republic to the east, Congo to the south-east, Gabon and Equatorial Guinea to the south, and the Atlantic Ocean to the south-west",
            caption="Figure 2. Cameroon and its neighbours, with lines of latitude and longitude. Simplified sketch map, not to scale."),
        KEY("Where Cameroon's neighbours are", "Learn them by direction.", cards=[
            ["West and north-west", "Nigeria (the long border runs from the coast to Lake Chad)"],
            ["North-east", "Chad (the Logone River and Lake Chad are on this side)"],
            ["East", "Central African Republic"],
            ["South-east", "Congo"],
            ["South", "Gabon and Equatorial Guinea"],
            ["South-west", "The Atlantic Ocean (Gulf of Guinea): Cameroon's only coast"],
        ]),
        T("Cameroon has one coast. Its sea ports, Douala and Kribi, are on the Atlantic coast in the south-west. "
          "Chad and the Central African Republic have no sea coast, so goods for them often pass through Cameroon."),
        EX("Model answer: describe the location of Cameroon in Africa", intro="Describe the location of Cameroon in Africa. (A good answer uses latitude, longitude and neighbours.)", steps=[
            S("Latitude", text="Cameroon lies north of the Equator, between about 2°N and 13°N, so it is entirely in the tropics."),
            S("Longitude", text="It lies east of the Greenwich Meridian, between about 8.5°E and 16°E."),
            S("Position in Africa", text="It is in West-Central Africa, at the inner corner of the Gulf of Guinea."),
            S("Neighbours", text="Nigeria is to the west, Chad to the north-east, the Central African Republic to the east, Congo to the south-east, Gabon and Equatorial Guinea to the south, and the Atlantic Ocean to the south-west."),
        ]),
        H("The administrative map: ten regions"),
        T("For government, Cameroon is divided into **regions**. Each region has a town where the regional government has its offices. "
          "This town is the **regional headquarters** (also called the regional capital)."),
        D("A **region** is a large administrative area of a country. The **regional headquarters** is the main town where the offices of the region are based.", title="Region and headquarters"),
        CODE("""
Region        Regional headquarters
-----------   ---------------------
Far North     Maroua
North         Garoua
Adamawa       Ngaoundéré
North-West    Bamenda
West          Bafoussam
South-West    Buea
Littoral      Douala
Centre        Yaoundé
East          Bertoua
South         Ebolowa
""", "text", title="The ten regions and their headquarters"),
        IMG("f5g-cmr-admin-map.svg",
            alt="Sketch map of Cameroon with dots and names for the ten regional headquarters from Maroua in the far north to Ebolowa in the south",
            caption="Figure 3. The ten regional headquarters. The boundaries between regions are not drawn here: copy them from your atlas. Simplified sketch map, not to scale."),
        TIP("Learn the regions in groups by position. **Three northern regions**: Far North, North, Adamawa. **Four western regions**: North-West, West, South-West, Littoral. "
            "**Three southern and eastern regions**: Centre, South, East. Then learn one headquarters for each group member.",
            title="A memory aid"),
        T("Yaoundé, the headquarters of the Centre Region, is also the political capital of Cameroon. Douala, the headquarters of the Littoral Region, is the largest city and the main port."),
        H("Sketching the administrative map"),
        T("Paper 2 may ask you to **draw** the administrative map. You do not need to trace perfectly. You need a recognisable shape, correct positions and clear labels."),
        EX("Model answer: how to sketch the map", intro="Draw a sketch map of Cameroon and mark the regional headquarters.", steps=[
            S("Frame and title", text="Draw a tall rectangle, taller than it is wide. Write a title above it: 'Cameroon: regional headquarters'."),
            S("Outline", text="Draw the shape like a triangle with a long thin tip. The tip points north to Lake Chad. The wide base is in the south and the coast is on the west side."),
            S("Neighbours and sea", text="Write NIGERIA on the west, CHAD in the north-east, CAR on the east, GABON and EQ. GUINEA in the south, and ATLANTIC OCEAN in the south-west."),
            S("Headquarters", text="Mark each headquarters with a dot in its correct position: Maroua and Garoua in the north, Ngaoundéré in the middle, Bamenda and Bafoussam in the west, Douala and Buea on the coast, Yaoundé, Ebolowa and Bertoua in the south and centre-east."),
            S("Names and key", text="Write the town name beside each dot and the region name beneath it. Add a key (dot = regional headquarters), a north arrow and the words 'not to scale'."),
        ]),
        TIP("This topic appears in **Paper 2, Section D (Geography of Cameroon)** as a sketch map or a description, and in **Paper 1** as multiple-choice questions on location, neighbours and regional headquarters. "
            "Multiple-choice questions on case studies are allowed on Cameroon, so facts about Cameroon can be tested directly.",
            title="Exam link"),
        MISTAKE("Mixing up regions and headquarters", "Do not write 'Bamenda Region'. The region is North-West and Bamenda is its headquarters. Buea is the headquarters of South-West, not of Littoral."),
        MISTAKE("Wrong neighbours", "Ghana and Niger do not border Cameroon, and Togo and Benin do not either. Only Nigeria, Chad, the Central African Republic, Congo, Gabon and Equatorial Guinea do. (Lake Chad is shared, but it is not a country.)"),
        QUIZ("Which pair gives the correct latitude and longitude of Cameroon?",
             ["About 2°N to 13°N and 8.5°E to 16°E", "About 2°S to 13°S and 8.5°E to 16°E", "About 2°N to 13°N and 8.5°W to 16°W", "About 22°N to 33°N and 8.5°E to 16°E"], 0,
             "Cameroon is north of the Equator and east of Greenwich, so the letters are N and E. Its range is about 2° to 13° north and 8.5° to 16° east.",
             hint="Is Cameroon above or below the Equator? East or west of Greenwich?",
             feedback=["", "South latitude would put Cameroon below the Equator, in the southern hemisphere.", "West longitude would put it in the Atlantic Ocean.", "22°N to 33°N is the latitude of the Sahara and North Africa, far north of Cameroon."]),
        QUIZ("Which regional headquarters is correctly matched with its region?",
             ["Buea: Littoral", "Bafoussam: West", "Garoua: Far North", "Bertoua: Centre"], 1,
             "Bafoussam is the headquarters of the West Region. Buea is South-West, Garoua is North and Bertoua is East.",
             hint="Take each town in turn and recall its region.",
             feedback=["Buea is the headquarters of the South-West Region. Douala is the headquarters of Littoral.", "", "Garoua is the headquarters of the North Region. Maroua is the headquarters of the Far North.", "Bertoua is the headquarters of the East Region. Yaoundé is the headquarters of Centre."]),
        PQ("Name the country that borders Cameroon (a) to the west and (b) to the east, and the ocean on the south-west.",
           "(a) Nigeria. (b) The Central African Republic. The ocean is the Atlantic Ocean (Gulf of Guinea)."),
        PQ("State the headquarters of the following regions: Far North, Adamawa, South-West and South.",
           "Far North: Maroua. Adamawa: Ngaoundéré. South-West: Buea. South: Ebolowa."),
        PQ("Cameroon extends from about 2°N to 13°N. Using 1° of latitude = 111 km, calculate its approximate length from north to south.",
           "13° - 2° = 11°. 11 × 111 = 1,221 km, so about 1,200 km."),
        PQ("Explain why Cameroon is described as 'Africa in miniature'.",
           "Cameroon stretches from near the Equator to the edge of the Sahel, over about 11° of latitude. It therefore has the coast and rainforest in the south, mountains and plateaus in the middle and west, and savanna and semi-desert in the north. Many of the main natural environments of Africa are found within one country."),
        SUM("Cameroon lies in West-Central Africa, north of the Equator (about 2°N to 13°N) and east of Greenwich (about 8.5°E to 16°E).",
            "Its neighbours are Nigeria (west), Chad (north-east), the Central African Republic (east), Congo (south-east), Gabon and Equatorial Guinea (south) and the Atlantic Ocean (south-west).",
            "Cameroon has ten regions. Their headquarters are Maroua, Garoua, Ngaoundéré, Bamenda, Bafoussam, Buea, Douala, Yaoundé, Bertoua and Ebolowa.",
            "To sketch the map, draw a frame and title, a tall triangle-like outline with the thin tip at Lake Chad, neighbours, dots and names, a key and a north arrow."),
    ],
))

# ------------------------------------------------------------------ 2. Relief units
LESSONS.append(lesson(
    module=MODULE,
    topic=PHYS,
    title="Relief units of Cameroon and Mount Cameroon",
    slug="cmr-relief-units",
    minutes=24,
    summary="Locate and describe the main relief units of Cameroon, from the coastal plain to the Chad lowlands, and describe Mount Cameroon.",
    objectives=[
        "Illustrate the distribution of the main relief units of Cameroon on a sketch map",
        "Describe the coastal plain, southern plateau, Adamawa plateau, western highlands, Benue and Chad lowlands and Mandara mountains",
        "Describe Mount Cameroon and its importance",
        "Explain how relief affects settlement and farming in Cameroon",
    ],
    key_concepts=["Relief", "Plain", "Plateau", "Highlands", "Lowlands", "Mount Cameroon", "Inselberg"],
    blocks=[
        H("Introduction"),
        T("Travel from Limbe to Maroua and you climb and descend several times. You start at sea level on the beach, climb to the cool highlands near Bamenda or "
          "Bafoussam, pass over the high Adamawa plateau near Ngaoundéré, and then come down to the hot plains of the north. "
          "The shape of the land has a strong effect on climate, rivers, farming and where people live."),
        D("**Relief** is the shape of the land surface: its height above sea level and its slopes. Mountains, plateaus and plains are types of relief.", title="Relief"),
        D("A **plain** is a large area of low, flat or gently sloping land. A **plateau** is a high area of fairly flat land, often with steep edges. "
          "**Highlands** are areas of high land with hills and mountains. **Lowlands** are broad areas of low-lying land.", title="Plain, plateau, highlands, lowlands"),
        H("The relief units and where they are"),
        T("Cameroon has six main relief units. Their positions are shown in the figure. Notice the pattern: the land is lowest at the coast and in the far north, "
          "and highest in the west and in the centre."),
        IMG("f5g-cmr-relief.svg",
            alt="Sketch map of Cameroon with relief units labelled: coastal plain, southern plateau, western highlands, Adamawa plateau, Benue lowlands, Chad lowlands, Mandara mountains and Mount Cameroon on the coast",
            caption="Figure 1. The main relief units of Cameroon. Darker brown means higher land. Boundaries are gradual and approximate. Simplified sketch map, not to scale."),
        T("Going from the Atlantic coast to the far north, the main steps are: coastal plain, southern plateau, Adamawa plateau, Benue lowlands, then the Chad lowlands. "
          "The western highlands and Mount Cameroon lie to the west of this line, and the Mandara mountains lie on the north-western border."),
        H("Description of each unit"),
        KEY("1. The coastal plain", "A low plain along the Atlantic coast.", cards=[
            ["Where", "Along the coast from the Nigerian border to the border with Equatorial Guinea, with the Wouri estuary and Douala near its middle."],
            ["Description", "Low and mostly flat, with sandy beaches, creeks, estuaries and mangrove swamps. The Wouri estuary and Douala port are here."],
            ["Height", "Low, mostly below about 200 m (check your textbook)."],
        ]),
        KEY("2. The southern plateau", "The largest relief unit by area, covering the Centre, South and East regions.", cards=[
            ["Where", "Inland from the coastal plain, in the south and east, up to the foot of the Adamawa plateau."],
            ["Description", "A gently rolling plateau cut by many rivers, with scattered hills (for example the hills around Yaoundé). Rivers form rapids and waterfalls where they leave the plateau."],
            ["Height", "Mostly about 500 to 1,000 m (check your textbook)."],
        ]),
        KEY("3. The Adamawa plateau", "A high plateau across the centre of the country.", cards=[
            ["Where", "Between about 6°N and 8°N, from the western highlands to the eastern border. Ngaoundéré lies on it."],
            ["Description", "Wide, high, grass-covered plateau with steep edges (escarpments) to the south and north. Many rivers rise here and flow north and south."],
            ["Height", "About 1,000 to 1,500 m, higher than the southern plateau (check your textbook)."],
        ]),
        KEY("4. The western highlands", "A belt of high land in the west and north-west.", cards=[
            ["Where", "The North-West and West regions, running south-west towards Mount Cameroon. Bamenda and Bafoussam are in it."],
            ["Description", "High volcanic and granite mountains, plateaus and crater lakes, such as the Bamenda and Bamileke plateaus and Mount Oku. Slopes are steep, valleys deep."],
            ["Height", "Often 1,000 to 2,000 m, with peaks near 3,000 m (check your textbook)."],
        ]),
        KEY("5. The Benue and Chad lowlands", "Two broad lowlands in the north.", cards=[
            ["Where", "The Benue lowlands lie along the Benue River around Garoua. The Chad lowlands lie further north, near the Logone River and Lake Chad."],
            ["Description", "Flat or gently undulating plains, low-lying and hot. Parts of the Logone plain flood each rainy season."],
            ["Height", "Low, mostly below about 500 m (check your textbook)."],
        ]),
        KEY("6. The Mandara mountains", "Rocky mountains on the Nigerian border in the Far North.", cards=[
            ["Where", "Near Mokolo and Mora, on the north-west border with Nigeria."],
            ["Description", "A line of rocky hills and peaks that rise above the plains. Some are isolated rocks called inselbergs. Steep slopes are terraced for farming."],
            ["Height", "About 1,000 m and above (check your textbook)."],
        ]),
        D("An **inselberg** is an isolated rocky hill that rises sharply above a flat plain. The word comes from German and means 'island mountain'.", title="Inselberg"),
        H("Mount Cameroon"),
        T("Mount Cameroon (also called Fako) stands beside the Atlantic coast near Buea and Limbe. It is the highest mountain in Cameroon, more than 4,000 m high. "
          "It is an **active volcano**: it has erupted several times in recent decades, for example in 1999, 2000 and 2012 (check the dates in your textbook)."),
        KEY("Mount Cameroon: key facts", "Learn these for descriptions.", cards=[
            ["Position", "On the coast, in the South-West Region, about 4°N and 9°E."],
            ["Height", "More than 4,000 m: the highest peak in Cameroon."],
            ["Origin", "A volcano. Lava and ash have built a huge cone with fertile soils."],
            ["Importance", "Fertile volcanic soils for plantations (banana, oil palm, rubber, tea); very heavy rain on the windward slopes; tourism and the annual mountain race from Buea."],
        ]),
        T("Beyond the usual features, Mount Cameroon is also a risk. Lava flows and ash can damage farms and roads, and steep slopes cause landslides in heavy rain. "
          "People near the mountain farm the rich soils but must prepare for eruptions."),
        EX("Model answer: describe the distribution of relief units", intro="Describe the distribution of the main relief units of Cameroon. (Illustrate with a sketch map.)", steps=[
            S("Coast and south", text="A low coastal plain runs along the Atlantic coast in the south-west. Inland, the southern plateau covers the Centre, South and East regions."),
            S("Centre", text="The high Adamawa plateau lies across the centre of the country, between about 6°N and 8°N."),
            S("West", text="The western highlands, a belt of high volcanic mountains, lie in the west. Mount Cameroon, an active volcano, is on the coast at their south-west end."),
            S("North", text="North of the Adamawa plateau the land falls to the Benue lowlands and then to the Chad lowlands. The Mandara mountains rise on the north-western border near Mokolo."),
            S("Sketch map", text="Draw the outline of Cameroon, shade or label each unit in its position, put a triangle for Mount Cameroon and add a key and the words 'not to scale'."),
        ]),
        EX("Model answer: effects of relief on people", intro="Explain why the western highlands are more densely populated than the Benue lowlands.", steps=[
            S("Point: fertile soils", text="Volcanic soils in the western highlands are rich and support intensive farming of coffee, maize, beans and vegetables."),
            S("Point: cool, wet climate", text="Height makes the highlands cooler, which is pleasant to live in and gives reliable rain for crops."),
            S("Contrast", text="The Benue lowlands are hotter and drier, with a long dry season, so farming is harder and fewer people can be supported."),
            S("Concluding link", text="So relief affects climate and soil, and these affect how many people an area can support."),
        ]),
        TIP("This topic appears in **Paper 2, Section D (Geography of Cameroon)** as a request to **illustrate and describe** the distribution of relief units, often with a sketch map. "
            "In **Paper 1** you may meet multiple-choice questions on the position of a unit, on Mount Cameroon, or on the lowlands.",
            title="Exam link"),
        MISTAKE("Calling every highland a plateau", "A plateau is high but fairly flat. The Adamawa and the southern plateaus are plateaus. The western highlands and the Mandara are mountains and hills."),
        MISTAKE("Putting Mount Cameroon inland", "Mount Cameroon is on the coast, in the South-West. Mount Oku and the Bamenda highlands are further inland. Always place the triangle for Mount Cameroon at the coast."),
        QUIZ("Which relief unit is found across the centre of Cameroon, between about 6°N and 8°N, and has Ngaoundéré on it?",
             ["Southern plateau", "Adamawa plateau", "Chad lowlands", "Coastal plain"], 1,
             "The Adamawa plateau is the high plateau across the centre. Ngaoundéré lies on it.",
             hint="Which unit is named after the region whose headquarters is Ngaoundéré?",
             feedback=["The southern plateau lies further south, covering the Centre, South and East regions.", "", "The Chad lowlands are in the far north, far from Ngaoundéré.", "The coastal plain is a strip along the Atlantic coast in the south-west."]),
        QUIZ("Which statement about Mount Cameroon is correct?",
             ["It is an extinct volcano in the Far North.", "It is a plateau in the Adamawa Region.", "It is the highest mountain in Cameroon and an active volcano near the coast.", "It is a rocky hill in the Mandara mountains."], 2,
             "Mount Cameroon is an active volcano in the South-West Region, near the Atlantic coast, and is the highest mountain in the country.",
             hint="Think of Buea and Limbe.",
             feedback=["Mount Cameroon is not in the Far North, and it is active, not extinct.", "A plateau is flat land. Mount Cameroon is a volcanic cone and is not in Adamawa.", "", "The Mandara mountains are in the north. Mount Cameroon is on the south-west coast."]),
        PQ("Name the six main relief units of Cameroon.",
           "The coastal plain, the southern plateau, the Adamawa plateau, the western highlands, the Benue and Chad lowlands, and the Mandara mountains."),
        PQ("Describe the coastal plain of Cameroon.",
           "It is a low plain along the Atlantic coast in the south-west. It is mostly flat, with sandy beaches, creeks, estuaries and mangrove swamps. The Wouri estuary and the port of Douala are on it. Its height is mostly below about 200 m."),
        PQ("Describe Mount Cameroon and give two ways it is important to people.",
           "Mount Cameroon is the highest mountain in Cameroon, more than 4,000 m high. It is an active volcano on the coast in the South-West Region, near Buea and Limbe. It is important because its volcanic soils are fertile for plantations of banana, oil palm, rubber and tea, and because it attracts tourists and climbers, for example in the annual mountain race."),
        PQ("Explain why people in the Mandara mountains build terraces.",
           "The slopes are steep, so soil and water run off quickly and erosion is a danger. Terraces make flat steps that hold soil and water, so crops can be grown. They are important where land is scarce and many people depend on the hills."),
        SUM("Cameroon has six main relief units: the coastal plain, the southern plateau, the Adamawa plateau, the western highlands, the Benue and Chad lowlands, and the Mandara mountains.",
            "Land is low on the coast and in the north, and high in the centre (Adamawa plateau, about 1,000 m or more) and in the west (western highlands).",
            "The coastal plain has creeks and mangroves; the southern plateau is rolling and forested; the lowlands are flat and hot; the Mandara mountains have rocky peaks and terraces.",
            "Mount Cameroon is an active volcano on the coast and the highest mountain in the country, with fertile volcanic soils.",
            "In an exam, illustrate with a labelled sketch map and describe each unit by position, shape and height."),
    ],
))

# ------------------------------------------------------------------ 3. Drainage systems and watersheds
LESSONS.append(lesson(
    module=MODULE,
    topic=PHYS,
    title="Drainage systems and watersheds of Cameroon",
    slug="cmr-drainage-systems-and-watersheds",
    minutes=22,
    summary="The main river systems of Cameroon (Atlantic, Benue-Niger, Logone-Lake Chad, Cross River and Congo basin tributaries) and the watersheds that separate them.",
    objectives=[
        "Define drainage basin, river system and watershed",
        "Describe the main drainage systems of Cameroon and name their main rivers",
        "Illustrate the main drainage systems and watersheds on a sketch map",
        "Explain why the Adamawa plateau and the western highlands are important watersheds",
    ],
    key_concepts=["Drainage basin", "River system", "Watershed", "Mouth and source", "Seasonal river (mayo)", "Lake Chad basin"],
    blocks=[
        H("Introduction"),
        T("At Douala, the Wouri River widens into an estuary where ships from all over the world dock. In Garoua, the Benue River crosses the north before it leaves for Nigeria. "
          "In the Far North, many rivers flow only in the rainy season and dry up in the dry season. "
          "Cameroon's rivers do not all flow to the same place. Some reach the Atlantic Ocean, some reach Lake Chad, some join the Niger and some join the Congo."),
        D("A **river system** is a main river with all its tributaries. A **tributary** is a smaller river that joins a larger one.", title="River system"),
        D("A **drainage basin** (catchment area) is the whole area of land drained by a river system. All the rain that falls in it flows to the same river.", title="Drainage basin"),
        D("A **watershed** (drainage divide) is the line of high ground that separates two drainage basins. Rain that falls on one side flows to one river system. Rain that falls on the other side flows to another.", title="Watershed"),
        H("The main drainage systems"),
        IMG("f5g-cmr-drainage.svg",
            alt="Sketch map of Cameroon with the main rivers in blue (Cross River, Mungo, Wouri, Sanaga, Nyong, Benue, Logone, Dja and Boumba) and the main watersheds as brown dashed lines across the Adamawa plateau and the south-east",
            caption="Figure 1. The main rivers (blue) and watersheds (brown dashes) of Cameroon. Dotted rivers have approximate courses. Simplified sketch map, not to scale."),
        T("Cameroon can be divided into five main drainage systems. Learn each by its rivers, its direction and where its water ends."),
        KEY("1. The Atlantic (Gulf of Guinea) system", "Rivers that flow south or west into the Atlantic Ocean.", cards=[
            ["Main rivers", "Sanaga, Wouri, Nyong, Mungo (and others such as the Ntem and the Dibamba)."],
            ["Description", "These rivers rise on the Adamawa plateau and in the western highlands and flow across the southern plateau and the coastal plain. Heavy rain keeps them flowing all year. They have rapids and waterfalls where they leave the plateau."],
            ["Examples", "The Sanaga is the longest river wholly inside Cameroon. The Wouri forms the estuary at Douala. The Mungo rises on Mount Manengouba. There are hydroelectric dams on the Sanaga, for example at Edéa and Song Loulou."],
        ]),
        KEY("2. The Benue-Niger system", "Rivers that flow north then west into Nigeria.", cards=[
            ["Main river", "The Benue, with tributaries such as the Faro and the Mayo Louti."],
            ["Description", "The Benue rises on the Adamawa plateau near Ngaoundéré, flows north through the Benue lowlands past Garoua and leaves Cameroon for Nigeria, where it joins the Niger River."],
            ["Examples", "The Lagdo Dam on the Benue, near Garoua, makes electricity and gives water for irrigation. Some rivers in the north are seasonal rivers (called mayos)."],
        ]),
        KEY("3. The Logone and Lake Chad system", "Rivers that flow north into the inland basin of Lake Chad.", cards=[
            ["Main river", "The Logone River, which flows along the border with Chad and joins the Chari before reaching Lake Chad."],
            ["Description", "The Logone flows across the flat Chad lowlands. In the rainy season it floods the plains around it. Lake Chad has no outlet to the sea."],
            ["Examples", "Lake Chad has shrunk a great deal since the 1960s, because of long droughts and because people take more water for farming (check your textbook)."],
        ]),
        KEY("4. The Cross River system", "A small system on the western edge.", cards=[
            ["Main river", "The Manyu River, which becomes the Cross River."],
            ["Description", "It drains the south-western part of the western highlands around Mamfe and flows west into Nigeria and then to the Atlantic Ocean."],
        ]),
        KEY("5. The Congo basin tributaries", "Rivers in the south-east.", cards=[
            ["Main rivers", "The Dja, Boumba and Ngoko, which flow to the Sangha River."],
            ["Description", "The Sangha joins the Congo River, which reaches the Atlantic Ocean far to the south. These rivers flow slowly through the rainforest of the East Region."],
        ]),
        H("The main watersheds"),
        T("Each drainage system is separated from the next by a watershed. The main watersheds of Cameroon are on high ground."),
        KEY("Where the main watersheds lie", "Check exact lines in your atlas or textbook.", cards=[
            ["The Adamawa plateau", "The main watershed of the country. Rivers on its south side flow to the Atlantic (the Sanaga and its tributaries) or to the Congo. Rivers on its north side flow to the Benue and to the Logone and Lake Chad."],
            ["The western highlands", "Separate the Atlantic rivers (Wouri, Mungo, upper Sanaga) from the Cross River and the Benue system."],
            ["The south-east", "A watershed on the southern plateau separates the Nyong and the Sanaga, which flow to the Atlantic, from the Dja and Boumba, which flow to the Congo."],
        ]),
        T("For this reason the Adamawa plateau is sometimes called the 'water tower' of Cameroon. Many rivers that serve people in the south and in the north begin there."),
        EX("Model answer: describe the main drainage systems", intro="Describe the main drainage systems of Cameroon and show them on a sketch map.", steps=[
            S("Atlantic system", text="The Sanaga, Wouri, Nyong and Mungo flow south or west to the Atlantic Ocean. They flow all year because the south is wet."),
            S("Benue-Niger system", text="The Benue rises on the Adamawa plateau and flows north and west into Nigeria and the Niger. The Lagdo Dam is on it."),
            S("Chad system", text="The Logone flows north along the border with Chad into Lake Chad, an inland basin with no outlet to the sea."),
            S("Other systems", text="The Cross River drains the west towards Nigeria. The Dja, Boumba and Ngoko flow south-east to the Sangha and the Congo."),
            S("Sketch map", text="Draw the outline, mark the Adamawa plateau as a dashed watershed line, draw the main rivers with arrows for the direction of flow, and label them."),
        ]),
        EX("Model answer: explain the importance of the Adamawa watershed", intro="Explain why the Adamawa plateau is an important watershed.", steps=[
            S("Point: high ground", text="The Adamawa plateau is the highest broad land in the centre of the country, so water flows away from it in all directions."),
            S("Point: sends water to different basins", text="South of it rivers flow to the Atlantic and the Congo. North of it, rivers flow to the Benue and to Lake Chad."),
            S("Point: importance to people", text="The same rivers provide water, fish and electricity (for example the Lagdo Dam and the Sanaga dams) to the south and the north."),
            S("Link", text="If forests or grassland on the plateau are damaged, water supplies in several regions could change, so its protection matters."),
        ]),
        TIP("This topic appears in **Paper 2, Section D (Geography of Cameroon)**, often as a sketch map of rivers and watersheds, and in **Paper 1** as multiple-choice questions, for example on the river that flows to Lake Chad or on the Lagdo Dam.",
            title="Exam link"),
        MISTAKE("Showing the Benue flowing to the Atlantic in Cameroon", "The Benue rises on the Adamawa plateau and flows north, then west into Nigeria. It is part of the Niger system. It does not reach the Atlantic in Cameroon."),
        MISTAKE("Confusing a watershed with a river", "A watershed is a line of high ground, not water. In a sketch map draw it as a dashed line along the high ground, and draw rivers as blue lines with arrows."),
        QUIZ("Which river forms the estuary at Douala?",
             ["Sanaga", "Wouri", "Benue", "Logone"], 1,
             "The Wouri River enters the Atlantic through an estuary at Douala, where the port is.",
             hint="Think of the port city on the Atlantic coast and the estuary beside it.",
             feedback=["The Sanaga reaches the sea further south, near Edéa.", "", "The Benue flows north and west to Nigeria.", "The Logone is in the north and flows to Lake Chad."]),
        QUIZ("Which river system carries water from Cameroon into Lake Chad?",
             ["Sanaga", "Cross River", "Logone", "Nyong"], 2,
             "The Logone flows north along the border with Chad and joins the Chari before reaching Lake Chad.",
             hint="It forms part of the Cameroon-Chad border.",
             feedback=["The Sanaga flows to the Atlantic Ocean.", "The Cross River drains the west into Nigeria and the Atlantic.", "", "The Nyong flows west across the southern plateau to the Atlantic."]),
        PQ("Define the term watershed.",
           "A watershed is a line of high ground that separates two drainage basins. Rain falling on opposite sides of it flows into different river systems."),
        PQ("Name two rivers that flow to the Atlantic Ocean and the river that flows from Cameroon into the Niger system.",
           "Any two of the Sanaga, Wouri, Nyong or Mungo flow to the Atlantic Ocean. The river that flows into the Niger system is the Benue."),
        PQ("State two uses of the Lagdo Dam on the Benue.",
           "The dam produces hydroelectric power and stores water for irrigation. It also helps to control flooding along the river."),
        PQ("Explain why rivers in southern Cameroon flow all year, but many rivers in the Far North flow only in the rainy season.",
           "The south has heavy rain in most months, so rivers are always fed with water. The Far North has a short rainy season and a long dry season with high evaporation. Seasonal rivers (mayos) fill after rain and dry up when the rains stop."),
        SUM("A drainage basin is the land drained by a river system, and a watershed is the high ground that separates two basins.",
            "Cameroon has five main drainage systems: the Atlantic system (Sanaga, Wouri, Nyong, Mungo), the Benue-Niger system, the Logone and Lake Chad system, the Cross River and the Congo basin tributaries (Dja, Boumba, Ngoko).",
            "The Adamawa plateau is the main watershed. Rivers flow south to the Atlantic and Congo and north to the Benue and Lake Chad.",
            "Southern rivers flow all year; northern rivers (mayos) are seasonal. The Lagdo Dam on the Benue and the Sanaga dams make electricity.",
            "In an exam, draw the outline, the main rivers with arrows and the watersheds as dashed lines, then label them."),
    ],
))

# ------------------------------------------------------------------ 4. Climate zones and vegetation
LESSONS.append(lesson(
    module=MODULE,
    topic=PHYS,
    title="Climatic types and vegetation of Cameroon",
    slug="cmr-climate-zones-and-vegetation",
    minutes=26,
    summary="The four climatic types of Cameroon, how to read a climate graph, and the main vegetation types from mangrove and rainforest to savanna and Sahel.",
    objectives=[
        "Describe the main climatic types of Cameroon and where they are found",
        "Describe the characteristics of equatorial, Cameroonian-type, Sudanian and Sahelian climates",
        "Interpret a climate graph by naming the rainfall pattern, total and temperature range",
        "Describe the main vegetation types of Cameroon and their characteristics",
    ],
    key_concepts=["Equatorial (Guinean) climate", "Cameroonian-type climate", "Sudanian climate", "Sahelian climate", "Climate graph", "Rainforest", "Savanna", "Mangrove"],
    blocks=[
        H("Introduction"),
        T("In Douala, it rains for most of the year and umbrellas are used all through the rainy season. In Yaoundé there are two rainy seasons. "
          "In Ngaoundéré the rains stop for several months, and in Maroua the dry season is long and the sun is very hot. "
          "This is one country, but it has four different climates."),
        T("Climate decides which plants grow naturally. So the vegetation changes from forest in the south to grassland in the middle and thorn bush in the far north."),
        D("**Climate** is the average weather of a place over many years (usually 30 years or more): its temperature, rainfall, winds and humidity.", title="Climate"),
        H("Why Cameroon has different climates"),
        T("Two air masses meet over West and Central Africa. A moist wind, the **south-west monsoon**, blows from the Atlantic Ocean and brings rain. A dry, dusty wind, the **harmattan**, blows from the Sahara. "
          "The meeting zone of these two winds moves north in the northern summer (about June to September) and south in the northern winter (about December to February)."),
        T("Places near the Equator are crossed by this zone twice a year, so they have two rainy seasons. Places far to the north are reached only once and for a shorter time, so they have one short rainy season. "
          "Height and nearness to the sea also change the climate."),
        H("The four climatic types"),
        IMG("f5g-cmr-climate-zones.svg",
            alt="Sketch map of Cameroon showing climate zones: Equatorial (Guinean) in the south and east, Cameroonian type on the coast and in the west, Sudanian across the Adamawa plateau and north, Sahelian in the far north; squares A and B show where two exercise stations could belong",
            caption="Figure 1. The climatic types of Cameroon. Limits are approximate. Squares A and B are used in the climate-graph exercises below. Simplified sketch map, not to scale."),
        KEY("1. Equatorial (Guinean) climate", "South, Centre and East regions.", cards=[
            ["Rainfall", "Rain in most months. Two rainy seasons (about March to June and September to November) and two shorter dry spells. About 1,500 to 2,000 mm a year."],
            ["Temperature", "Hot all year: about 24 to 26 °C. The annual range is small (about 2 to 3 °C)."],
            ["Other features", "High humidity and cloud. Day and night temperatures are similar."],
        ]),
        KEY("2. Cameroonian-type climate (monsoon)", "The coast and the western highlands (Littoral, South-West, West and North-West).", cards=[
            ["Rainfall", "One long rainy season (about March to October) and a short dry season. Very heavy rain: often 2,000 to 4,000 mm or more, and more on the slopes of Mount Cameroon."],
            ["Cause", "The moist south-west monsoon winds from the Atlantic are forced to rise over Mount Cameroon and the highlands. The air cools, clouds form and heavy relief rain falls."],
            ["Temperature", "Hot on the coast (about 25 to 27 °C) but cooler in the highlands because of height (for example Bamenda and Bafoussam)."],
        ]),
        KEY("3. Sudanian climate", "The Adamawa plateau and the North Region.", cards=[
            ["Rainfall", "One rainy season of about five to seven months (about April to October) and a longer, dry season. About 900 to 1,500 mm a year."],
            ["Temperature", "Hot, with a larger yearly range than in the south. Cooler on the Adamawa plateau because of height."],
            ["Other features", "The dry harmattan wind blows between about December and February, bringing dust and cool nights."],
        ]),
        KEY("4. Sahelian climate", "The Far North Region.", cards=[
            ["Rainfall", "One short rainy season of three to four months (about June to September). Less than about 900 mm a year, and less further north. Rain is unreliable and droughts are common."],
            ["Temperature", "Very hot, especially before the rains (March to May, above 40 °C on some days). The yearly range and the day-night range are large."],
            ["Other features", "A long dry season with the dusty harmattan, high evaporation and strong sunshine."],
        ]),
        CODE("""
Type          Rainy season(s)         Rain a year (mm)
-----------   ---------------------   ----------------
Equatorial    2 (Mar-Jun, Sep-Nov)    1,500 to 2,000
Cameroonian   1 long (Mar-Oct)        2,000 to 4,000+
Sudanian      1 (Apr-Oct)             900 to 1,500
Sahelian      1 short (Jun-Sep)       under 900
""", "text", title="Summary table (months and totals are approximate: check your textbook)"),
        H("Reading a climate graph"),
        T("A **climate graph** shows monthly rainfall as bars and monthly temperature as a line. The first step in any question is to read four things: "
          "the **annual rainfall total**, the **temperature range** (highest minus lowest monthly temperature), the **pattern of rainy and dry months**, and the **hottest and coolest months**."),
        D("**Annual temperature range** = highest monthly mean temperature minus lowest monthly mean temperature.", title="Temperature range", formula=r"\text{range} = T_{\max} - T_{\min}"),
        T("The two graphs below use **constructed exercise data**. They are not real station records. Use them only to practise the method."),
        IMG("f5g-cmr-climate-graph-a.svg",
            alt="Climate graph for exercise station A: rainfall bars with peaks in May (220 mm) and October (300 mm), temperature line between about 24 and 26 degrees Celsius",
            caption="Figure 2. Station A: constructed exercise data (not a real station)."),
        EX("Worked example 1: read station A", intro="Describe the climate shown for station A (rainfall in mm: 50, 90, 190, 200, 220, 160, 70, 90, 250, 300, 150, 40 from January to December).", steps=[
            S("Annual rainfall total", math=r"50 + 90 + 190 + 200 + 220 + 160 + 70 + 90 + 250 + 300 + 150 + 40 = 1\,810 \text{ mm}"),
            S("Rainfall pattern", text="There are two peaks: about 220 mm in May and 300 mm in October. There is a short drier spell in July and August and a longer dry spell from December to February."),
            S("Temperature", math=r"\text{range} = 25.8 - 23.8 = 2.0\,^{\circ}\text{C}", text="The warmest month is February (25.8 °C) and the coolest are July and August (23.8 °C)."),
            S("Conclusion", text="Two rainy seasons, high rainfall and a very small temperature range are typical of the equatorial (Guinean) climate of the south."),
        ]),
        IMG("f5g-cmr-climate-graph-b.svg",
            alt="Climate graph for exercise station B: rainfall bars from almost nothing in January to 220 mm in August, temperature line from 24 to 34 degrees Celsius",
            caption="Figure 3. Station B: constructed exercise data (not a real station)."),
        EX("Worked example 2: read station B", intro="Describe the climate shown for station B (rainfall in mm: 0, 0, 5, 25, 60, 110, 170, 220, 110, 25, 0, 0 from January to December; hottest month April 34 °C, coolest January 24 °C).", steps=[
            S("Annual rainfall total", math=r"0 + 0 + 5 + 25 + 60 + 110 + 170 + 220 + 110 + 25 + 0 + 0 = 725 \text{ mm}"),
            S("Rainfall pattern", text="There is one peak, in August (220 mm). Only four months (June to September) have more than 100 mm. Six months have almost no rain."),
            S("Temperature", math=r"\text{range} = 34 - 24 = 10\,^{\circ}\text{C}", text="April is hottest, just before the rains. August is cooler because of cloud and rain."),
            S("Conclusion", text="One short rainy season, a total below about 900 mm and a large temperature range are typical of the Sahelian climate of the Far North."),
        ]),
        H("Vegetation types"),
        D("**Natural vegetation** is the plant cover that grows in a place without human planting. It depends mainly on climate (temperature and rainfall) and also on soil and height.", title="Natural vegetation"),
        IMG("f5g-cmr-vegetation.svg",
            alt="Sketch map of Cameroon showing vegetation zones: mangrove on the coast, montane forest in the western highlands, equatorial rainforest in the south and east, Guinea savanna in the centre, Sudan savanna and Sahel steppe in the north",
            caption="Figure 4. The main vegetation zones of Cameroon. Boundaries are gradual and approximate. Simplified sketch map, not to scale."),
        KEY("Mangrove (coastal swamp)", "Along the coast and in estuaries, such as the Wouri estuary and the area near Rio del Rey.", cards=[
            ["Features", "Short trees growing in salty mud. Stilt (prop) roots hold the trees up. Leaves are leathery. Breathing roots stick out of the mud."],
            ["Uses", "Fish nurseries, fuelwood for smoking fish, protection of the coast from waves."],
        ]),
        KEY("Equatorial rainforest", "South, Centre, East and the south-west lowlands.", cards=[
            ["Features", "Tall, evergreen broadleaf trees, some over 40 m high. Layers: a high canopy, a lower layer of smaller trees and shrubs, and a dark floor with little undergrowth. Buttress roots, climbers (lianas) and a great variety of species."],
            ["Uses", "Hardwood timber (for example iroko, sapele and ayous), cocoa farms, food crops, wildlife."],
        ]),
        KEY("Montane vegetation", "The western highlands, Mount Cameroon and Mount Oku.", cards=[
            ["Features", "Cooler and wetter than the plains. Forests of shorter trees covered in moss and ferns at middle heights, and grassland on the highest slopes."],
            ["Uses", "Water supply, grazing, tourism. Much of the forest has been cleared for farming."],
        ]),
        KEY("Guinea savanna", "The Adamawa plateau and the south of the North Region.", cards=[
            ["Features", "Tall grass (2 to 3 m) with scattered trees that lose leaves in the dry season. The trees have thick bark that resists fire."],
            ["Uses", "Cattle grazing on the Adamawa plateau and farming. Grass fires are common in the dry season."],
        ]),
        KEY("Sudan savanna", "The North Region.", cards=[
            ["Features", "Shorter, thinner grass and fewer, more widely spaced trees (acacia, baobab, shea). The land is green in the rainy season and brown in the dry season."],
            ["Uses", "Cotton, groundnuts, millet and sorghum farming; grazing."],
        ]),
        KEY("Sahel steppe", "The Far North.", cards=[
            ["Features", "Short, tufted grass, thorny bushes and a few acacia trees. Plants have deep roots, small leaves and thorns to save water. The ground is bare in places."],
            ["Uses", "Grazing for goats, sheep and cattle. Overgrazing and tree-cutting can lead to desertification (the spread of desert-like conditions)."],
        ]),
        EX("Model answer: link climate and vegetation", intro="Explain why the vegetation of the far north is different from the vegetation of the south.", steps=[
            S("Point: rainfall", text="The south receives heavy rain in most months, which supports tall evergreen trees. The far north has a short rainy season, so only drought-resistant plants survive."),
            S("Point: temperature and evaporation", text="The far north is very hot and has high evaporation, so soils dry out quickly."),
            S("Evidence", text="Rainforest in the south has layers and evergreen leaves. The Sahel has short grass and thorn bushes with small leaves and long roots."),
            S("Link", text="So vegetation changes as rainfall decreases from south to north."),
        ]),
        TIP("This topic appears in **Paper 2, Section D (Geography of Cameroon)** as 'describe the climatic types' or 'describe the vegetation' and in **Paper 1** as multiple-choice questions, often with a climate graph. "
            "Always quote figures from the graph: the total, the range and the months.",
            title="Exam link"),
        MISTAKE("Mixing up rainfall total and temperature range", "The range is the highest minus the lowest temperature, not the total rainfall. Add up the 12 rainfall values for the total, and subtract two temperatures for the range."),
        MISTAKE("Saying 'Cameroon has two climates'", "Cameroon has four climatic types. Do not forget the Cameroonian-type climate of the coast and highlands, with its very heavy rainfall."),
        QUIZ("Which climatic type has two rainy seasons and a very small annual temperature range?",
             ["Sahelian", "Sudanian", "Equatorial (Guinean)", "Cameroonian type"], 2,
             "The equatorial (Guinean) climate of the south has two rainy seasons and a small range, about 2 to 3 °C.",
             hint="Think of Yaoundé and the south.",
             feedback=["The Sahelian climate has one short rainy season and a large range.", "The Sudanian climate has one rainy season and a longer dry season.", "", "The Cameroonian type has one long rainy season and very heavy rain."]),
        QUIZ("Which vegetation has stilt roots and grows in salty mud on the coast?",
             ["Sahel steppe", "Mangrove", "Montane forest", "Guinea savanna"], 1,
             "Mangrove trees grow in salty coastal mud and have stilt roots to hold them up.",
             hint="It grows around the Wouri estuary.",
             feedback=["Sahel steppe is short grass and thorn bush in the far north.", "", "Montane forest is on the cool wet highlands.", "Guinea savanna is tall grass with scattered trees on the Adamawa plateau."]),
        PQ("State the four climatic types of Cameroon.",
           "Equatorial (Guinean), Cameroonian type (monsoon), Sudanian and Sahelian."),
        PQ("Describe the rainfall of the Cameroonian-type climate and explain why it is so heavy.",
           "It has one long rainy season (about March to October) and a short dry season. Rainfall is very heavy, often 2,000 to 4,000 mm or more. It is heavy because moist south-west monsoon winds from the Atlantic are forced up Mount Cameroon and the highlands. The air cools, clouds form and relief rain falls."),
        PQ("Describe two characteristics of the equatorial rainforest.",
           "Tall evergreen broadleaf trees, some over 40 m high, grow in layers with a dense canopy that shades the ground. It has a great variety of species, buttress roots and lianas."),
        PQ("A station has monthly mean temperatures from 24 °C to 34 °C. Calculate its annual temperature range and say what this suggests about its climate.",
           "Range = 34 - 24 = 10 °C. A large range suggests a place far from the Equator and away from the sea, such as the Sahelian or Sudanian climates, not the equatorial climate."),
        SUM("Cameroon has four climatic types: equatorial (Guinean) in the south and east, Cameroonian type on the coast and highlands, Sudanian in the Adamawa and north, and Sahelian in the far north.",
            "Rainfall decreases from south to north and the dry season gets longer. The Cameroonian type has the heaviest rain because of relief rainfall on Mount Cameroon and the highlands.",
            "On a climate graph read the annual total, the temperature range, the rainy and dry months and the hottest and coolest months.",
            "Vegetation follows climate: mangrove on the coast, rainforest in the south and east, montane forest on the highlands, Guinea and Sudan savanna in the centre and north, and Sahel steppe in the far north.",
            "Describe each type by position, rainfall, temperature and plant features."),
    ],
))

# ------------------------------------------------------------------ 5. Soil types
LESSONS.append(lesson(
    module=MODULE,
    topic=PHYS,
    title="Main soil types of Cameroon and farming",
    slug="cmr-soil-types-and-characteristics",
    minutes=20,
    summary="The main soil types of Cameroon (ferralitic, volcanic, alluvial and tropical ferruginous), their characteristics, where they are found and what they mean for farming.",
    objectives=[
        "Name the main soil types of Cameroon and locate them on a sketch map",
        "Describe the characteristics of ferralitic, volcanic, alluvial and tropical ferruginous soils",
        "Explain how soil type affects farming in different parts of Cameroon",
        "Outline ways of keeping soils fertile",
    ],
    key_concepts=["Soil", "Fertility", "Leaching", "Ferralitic soil", "Volcanic soil", "Alluvial soil", "Tropical ferruginous soil"],
    blocks=[
        H("Introduction"),
        T("A farmer near Buea grows bananas and oil palm on dark soil beside Mount Cameroon. A cocoa farmer near Ebolowa works on red soil under forest trees. "
          "In the Benue plain near Garoua, farmers grow rice and sorghum after the floods. "
          "All of them depend on soil, but the soils are very different."),
        D("**Soil** is the thin layer of loose material on the land surface made of broken rock, dead plants (humus), water and air. Plants grow in it and get water and nutrients from it.", title="Soil"),
        D("**Soil fertility** is the ability of a soil to supply the nutrients that crops need. A **fertile** soil gives good crops. **Humus** is the dark material made from rotting plants and animals.", title="Fertility and humus"),
        H("The main soil types"),
        IMG("f5g-cmr-soils.svg",
            alt="Sketch map of Cameroon showing soil zones: ferralitic soils in the south and east, volcanic soils in the western highlands and around Mount Cameroon, tropical ferruginous soils across the Adamawa and the north, Sahelian soils in the far north, and alluvial soils on river plains and estuaries",
            caption="Figure 1. The main soil zones of Cameroon. They are general: soils vary locally. Simplified sketch map, not to scale."),
        T("Cameroon has four main soil types, with some others in particular places. The soil in each region depends on its rocks, climate, vegetation and relief."),
        KEY("1. Ferralitic soils", "The most widespread soil of the south and east (Centre, South, East and the coastal lowlands).", cards=[
            ["Appearance", "Red or yellow, deep, sometimes clayey. The colour comes from iron and aluminium in the soil."],
            ["Characteristics", "Formed under heat and heavy rain. Rain washes the nutrients down below the roots of crops (leaching). The soil is acid and poor in nutrients. Nutrients are mostly in the plants and in a thin layer of humus under the forest."],
            ["Farming", "Cocoa, oil palm, coffee, plantain, cassava and cocoyam. Fertility falls fast after the forest is cleared, so farmers use bush fallow (rest the land for some years)."],
        ]),
        D("**Leaching** is the washing of nutrients down through the soil by rain, out of reach of plant roots. It is strongest in hot, wet regions.", title="Leaching"),
        KEY("2. Volcanic soils", "Around Mount Cameroon and in the western highlands (for example around Bamenda and Bafoussam).", cards=[
            ["Appearance", "Dark brown or black, loose and crumbly."],
            ["Characteristics", "Formed from lava and volcanic ash. Rich in minerals, well drained and very fertile. Steep slopes mean soil can be eroded."],
            ["Farming", "Tea, banana, oil palm and rubber plantations near Mount Cameroon, and arabica coffee, maize, beans, potatoes and vegetables in the western highlands. Rich soils and cool climate support high population densities."],
        ]),
        KEY("3. Alluvial soils", "River plains and estuaries: the Benue and Logone plains, around Lake Chad, and the Wouri and Sanaga valleys.", cards=[
            ["Appearance", "Grey or brown, fine and silty, often deep and moist."],
            ["Characteristics", "Made of silt and mud deposited by rivers when they flood. Renewed every year by floods, so they are fertile. They can be waterlogged in the wet season."],
            ["Farming", "Rice, vegetables, maize and dry-season sorghum on the flood plains of the north, and market gardening and rice in valleys. Fishing is also important."],
        ]),
        KEY("4. Tropical ferruginous soils", "The Adamawa plateau and the North Region (the savanna lands).", cards=[
            ["Appearance", "Red-brown or reddish, often sandy at the top."],
            ["Characteristics", "Iron-rich soils formed under savanna with a long dry season. Less leached than ferralitic soils, so moderately fertile, but with little humus because grass is burnt or dries up. Hard iron crusts can form where the soil is bare."],
            ["Farming", "Cotton, groundnuts, maize, millet and sorghum in the north, and cattle grazing on the Adamawa plateau. Yields depend on good rainfall."],
        ]),
        T("In the Far North, some soils are sandy and others are heavy clay that cracks when dry. Mangrove coasts have wet, salty swamp soils. Check your textbook for the names used for these local soils."),
        CODE("""
Soil          Colour        Where                    Fertility
-----------   -----------   ----------------------   ---------
Ferralitic    red, yellow   south and east           low
Volcanic      dark          Mt Cameroon, west        high
Alluvial      grey-brown    river plains, estuaries  high
Ferruginous   red-brown     Adamawa and north        medium
""", "text", title="Comparison of the four main soils (check your textbook)"),
        H("Soil and farming"),
        T("Farmers choose crops to suit their soils. Where soils are fertile, many people can live and farms are small and busy. Where soils are poor or dry, farmers need more land, rest the land (fallow) or add manure and fertiliser."),
        KEY("Ways of keeping soil fertile", "Good soil management helps farmers on every soil.", cards=[
            ["Bush fallow", "Rest the land for several years so that natural vegetation restores humus."],
            ["Manure and compost", "Add animal dung and plant waste to give nutrients and humus."],
            ["Crop rotation and mixed cropping", "Change the crops each year. Plant beans or groundnuts, which add nitrogen, with other crops."],
            ["Terracing and contour ridges", "Reduce erosion on steep slopes, for example in the Mandara mountains and western highlands."],
            ["Mulching and tree planting", "Cover the soil with leaves and plant trees to reduce evaporation and protect it from heavy rain."],
        ]),
        EX("Model answer: describe the main soils of Cameroon", intro="Describe the main soil types of Cameroon and say where they are found.", steps=[
            S("Ferralitic", text="Red or yellow soils found in the south and east under the rainforest. They are deep but acid and poor in nutrients because heavy rain washes the nutrients out."),
            S("Volcanic", text="Dark and fertile soils from lava and ash, found around Mount Cameroon and in the western highlands."),
            S("Alluvial", text="Fine silty soils deposited by rivers, found on the Benue and Logone plains and in estuaries. They are fertile and renewed by floods."),
            S("Tropical ferruginous", text="Red-brown soils of the Adamawa plateau and the North, formed under savanna. They are moderately fertile but low in humus and may form hard crusts."),
        ]),
        EX("Model answer: soil and farming", intro="Explain why farmers on ferralitic soils often practise bush fallow.", steps=[
            S("Point: soil is poor in nutrients", text="Heavy rain washes nutrients out of ferralitic soils, so they are acid and not very fertile."),
            S("Point: nutrients are in the forest", text="Most nutrients are held in the plants and in a thin humus layer. When the forest is cleared and burnt, the nutrients are used up in a few years and crop yields fall."),
            S("Solution: fallow", text="Farmers move to a new plot and leave the old one to grow bush again. The bush returns humus and nutrients to the soil."),
            S("Link", text="Bush fallow works when land is plentiful. When population grows and fallow is shortened, farmers need manure or fertiliser."),
        ]),
        TIP("This topic appears in **Paper 2, Section D (Geography of Cameroon)** as 'describe the main soil types and their characteristics' and in **Paper 1** as multiple-choice questions linking a soil to its region or crop. "
            "The more general topic of soil is also in the Biogeography part of the syllabus.",
            title="Exam link"),
        MISTAKE("Thinking that forest means fertile soil", "Rainforest grows quickly, but the nutrients are in the trees, not in the soil. The ferralitic soil under it is poor, and fertility falls fast when the forest is cleared."),
        MISTAKE("Mixing up volcanic and alluvial soils", "Volcanic soils come from lava and ash and are found in the highlands and near Mount Cameroon. Alluvial soils are deposited by rivers on flood plains and in estuaries."),
        QUIZ("Which soil type is red or yellow, acid and poor in nutrients because of heavy leaching?",
             ["Volcanic", "Alluvial", "Ferralitic", "Tropical ferruginous"], 2,
             "Ferralitic soils of the hot wet south have lost their nutrients by leaching. Iron and aluminium make them red or yellow.",
             hint="It covers the south and east, under rainforest.",
             feedback=["Volcanic soils are dark and fertile.", "Alluvial soils are renewed by river floods and are fertile.", "", "Tropical ferruginous soils are red-brown, but they are found under savanna and are less leached."]),
        QUIZ("Which soil is formed from lava and ash and is found around Mount Cameroon?",
             ["Volcanic soil", "Ferralitic soil", "Alluvial soil", "Sandy Sahelian soil"], 0,
             "Volcanic soil comes from lava and ash and is rich in minerals, which is why plantations thrive around Mount Cameroon.",
             hint="The mountain is a volcano.",
             feedback=["", "Ferralitic soils are red or yellow and are mostly in the south and east.", "Alluvial soils are deposited by rivers.", "Sandy Sahelian soils are in the far north."]),
        PQ("Name the four main soil types of Cameroon.",
           "Ferralitic soils, volcanic soils, alluvial soils and tropical ferruginous soils."),
        PQ("Describe the characteristics of volcanic soils and name two crops grown on them.",
           "Volcanic soils are dark, loose and rich in minerals because they form from lava and ash. They are well drained and very fertile. Crops include tea, banana, oil palm, rubber, arabica coffee and maize."),
        PQ("Explain why alluvial soils are fertile.",
           "Rivers deposit fresh silt and mud on their flood plains each year when they flood. This silt contains minerals and humus and renews the soil. So alluvial soils stay fertile and can support crops such as rice and vegetables."),
        PQ("Outline two ways in which farmers on poor soils can improve fertility.",
           "They can add manure or compost to supply nutrients and humus. They can use bush fallow or crop rotation, including beans or groundnuts, so that the soil recovers."),
        SUM("Cameroon has four main soils: ferralitic (south and east), volcanic (Mount Cameroon and the western highlands), alluvial (river plains and estuaries) and tropical ferruginous (Adamawa and north).",
            "Ferralitic soils are red or yellow, deep and acid, with low fertility because of leaching. Their nutrients are in the forest, so fertility falls after clearing.",
            "Volcanic and alluvial soils are fertile. Volcanic soils come from lava and ash. Alluvial soils are renewed by river floods.",
            "Tropical ferruginous soils are red-brown and moderately fertile, with little humus, and support cotton, groundnuts and grain crops.",
            "Fertility can be kept by fallow, manure, crop rotation, terracing and mulching."),
    ],
))
