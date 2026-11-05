"""Form 5 Geography: The Geography of Cameroon, Human characteristics (5 lessons, one practice set each)."""

from .dsl import *  # noqa: F403

COURSE = ("geography", "form-5")

MODULE = "The Geography of Cameroon"
TOPIC = "Human characteristics"

LESSONS = []

CHECK = ("Details such as exact boundaries, names and figures differ between sources and change over time, so "
         "check them in your textbook and atlas.")

# ------------------------------------------------------------------ 1. Growth and structure
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Population growth and structure of Cameroon",
    slug="cmrhum-population-growth-and-structure",
    minutes=22,
    summary="Cameroon has a young and growing population: many births, falling deaths and a pyramid with a wide base. This lesson explains how to describe growth and structure, draw a pyramid, and give causes and results.",
    objectives=[
        "Describe the growth pattern of the population of Cameroon",
        "Describe the structure of the population using an age-sex pyramid",
        "Draw an age-sex pyramid from a table of exercise data",
        "Explain the causes and results of the growth pattern",
    ],
    key_concepts=["Birth rate", "Death rate", "Natural increase", "Age-sex pyramid", "Young population", "Dependency ratio"],
    blocks=[
        H("Introduction"),
        T("Walk past a primary school in Douala, Bamenda or Maroua at break time. The yard is full. Now look at "
          "the market: many more young people than elderly people are buying and selling. This is a simple picture "
          "of the population of Cameroon: **young** and **growing**."),
        T("Geographers describe a population in two ways. **Growth** asks: how fast is the number of people changing? "
          "**Structure** asks: how many people are in each age group, and how many are male or female?"),
        D("**Population growth** is the change in the number of people living in a place over time. A population "
          "grows when more people are added (births and in-migration) than are lost (deaths and out-migration).",
          title="Population growth"),
        D("The **birth rate** is the number of live births in a year for every 1000 people. The **death rate** is the "
          "number of deaths in a year for every 1000 people. **Natural increase** is the birth rate minus the death rate.",
          title="Birth rate, death rate and natural increase", formula=r"\text{natural increase} = \text{birth rate} - \text{death rate}"),
        H("The growth pattern"),
        T("For many decades the population of Cameroon has grown quickly. The reason is simple. The birth rate has stayed "
          "high, while the death rate has fallen. The gap between them is large, so natural increase is large."),
        T("This pattern is common in tropical Africa. This lesson describes the pattern in words rather than giving exact "
          "totals, because totals change with every census and estimate. Use the latest figures in your textbook if the "
          "question asks for them."),
        IMG("f5g-cmrhum-growth-schematic.svg",
            alt="Schematic graph: the birth rate line stays high while the death rate line falls; the shaded gap between them is natural increase",
            caption="Figure 1. A high birth rate and a falling death rate create a wide gap: rapid natural increase (schematic)."),
        H("Causes of the growth pattern"),
        KEY("Why is the birth rate high?", "Several reasons work together. Examiners like answers that give three or more.", cards=[
            ["Social and cultural", "Large families are valued; marriage and first births often happen at young ages."],
            ["Economic", "In farming families, children help on the farm, so a large family can mean more labour."],
            ["Services", "Family planning and girls' schooling do not reach everyone, especially in rural areas."],
        ]),
        KEY("Why has the death rate fallen?", "Fewer people now die young than in the past.", cards=[
            ["Health care", "More clinics and hospitals, immunisation, and treatment for common diseases."],
            ["Water and food", "Safer drinking water and better food supply reduce illness."],
            ["Education", "Better knowledge of hygiene and child care."],
        ]),
        T("Migration also affects total numbers. Some people enter Cameroon and some leave, but for the whole country "
          "natural increase is the main reason for growth. Migration matters more for a single region or town."),
        H("Population structure"),
        D("An **age-sex pyramid** is a bar graph that shows the number or percentage of males and females in each age "
          "group. Males are on the left, females on the right, and the youngest age group is at the bottom.",
          title="Age-sex pyramid"),
        T("The shape of the pyramid tells a story. A pyramid with a **wide base** has many young people. "
          "**Steep sides** that narrow quickly mean that fewer people reach older ages. A **narrow top** means that "
          "there are few elderly people."),
        T("Cameroon has this kind of pyramid. It is a young population. Figure 2 is an imaginary pyramid with the same general "
          "shape, drawn from exercise data (not real census figures)."),
        IMG("f5g-cmrhum-pyramid.svg",
            alt="Age-sex pyramid with a wide base: 0 to 4 years is the largest bar at 8.7 percent for males and 8.5 for females, narrowing to under 1 percent at 60 plus",
            caption="Figure 2. An age-sex pyramid of an imaginary country (exercise data). Each bar is a percentage of the whole population."),
        EX("Model answer: describe the pyramid", intro="Describe the structure of the population shown in Figure 2.", steps=[
            S("Shape", text="The pyramid has a very wide base and narrows steadily towards the top. It has steep sides and a narrow top."),
            S("Evidence", text="The 0 to 4 group is the largest bar (8.7 percent of the population for males and 8.5 for females). By 60 to 64 each bar is below 1 percent."),
            S("Meaning", text="This is a young population. Together the three youngest groups make up 45.3 percent of the people, so almost half are under 15. Very few are aged 65 and over."),
            S("Males and females", text="The sexes are nearly equal at young ages. In the oldest groups there are slightly more females than males."),
        ]),
        H("Drawing an age-sex pyramid"),
        T("You may be asked to draw a pyramid from a table. Use the steps below. Table 1 shows exercise data with five age "
          "groups. The numbers are percentages of the whole population."),
        CODE(r"""Age group    Males (%)    Females (%)
0-14            22.9          22.4
15-29           14.2          14.1
30-44            7.8           8.1
45-59            3.7           4.0
60 and over      1.3           1.5
Total           49.9          50.1""", "text", title="Table 1. Exercise data"),
        EX("Model answer: draw the pyramid", intro="Draw an age-sex pyramid for the data in Table 1.", steps=[
            S("Choose one scale", text="Use 1 cm for every 5 percent. The largest value is 22.9 percent, which is 4.6 cm. Both sides must use the same scale."),
            S("Draw the axes", text="Draw a vertical line in the middle for the age groups. Males go to the left and females to the right. Mark a scale along the bottom."),
            S("Draw the bars", text="Draw one horizontal bar for each age group. Start at the bottom with 0 to 14. Keep every bar the same height. For 0 to 14 the male bar is 4.6 cm and the female bar is 4.5 cm. For 60 and over the bars are 0.3 cm each."),
            S("Label", text="Label the age groups, write Males and Females, give the unit (percent of total population) and add a title."),
        ]),
        TIP("In the exam, always say what the shape shows. A drawing with no comment earns only part of the marks. "
            "Write one sentence about the base, one about the top and one about the whole shape."),
        H("Results of the growth pattern"),
        T("Rapid growth and a young population have **positive** and **negative** results. Give both if the question says "
          "'discuss' or 'assess'."),
        KEY("Results", "Think of three groups: families, services and the economy.", cards=[
            ["Pressure on services", "More schools, teachers, clinics and housing are needed each year."],
            ["Pressure on jobs and land", "Many young people look for work. Farms are divided into smaller plots and some people migrate to towns."],
            ["Opportunities", "A large young workforce and a growing market for goods, if jobs and training are available."],
        ]),
        D("The **dependency ratio** compares the people who are usually dependent (children under 15 and adults 65 and over) with the "
          "people of working age (15 to 64). It is the number of dependants for every 100 workers.", title="Dependency ratio",
          formula=r"\text{dependency ratio} = \frac{\text{under 15} + \text{65 and over}}{\text{15 to 64}} \times 100"),
        T("For Figure 2: under 15 is 45.3 percent, 65 and over is 1.5 percent and 15 to 64 is 53.2 percent. "
          "So the ratio is (45.3 + 1.5) divided by 53.2, times 100, which is about 88. "
          "There are about 88 dependants for every 100 people of working age. Most of them are children."),
        MISTAKE("Mixing up growth rate and population size", "A country can have a small population and a fast growth rate. "
                "Write 'growing quickly' only when natural increase is high, not just because the total is large."),
        MISTAKE("Saying a young population is 'bad'", "A young population brings pressures and opportunities. Balanced answers "
                "name both and give an example, for example schools needed now and a bigger workforce later."),
        QUIZ("A pyramid has a very wide base and a narrow top. What does it show?",
             ["An old population with few children", "A young population with many births", "A population with equal numbers in every age group", "A population that is falling quickly"],
             1, "A wide base means many children and a narrow top means few elderly people: a young population.",
             hint="What does the base of a pyramid show?",
             feedback=["An old population has a narrow base and a wider top.", "", "Equal numbers would give a pyramid with straight vertical sides, like a rectangle.", "A falling population has a narrowing base, not a wide one."]),
        QUIZ("Which pair of changes best explains rapid natural increase in Cameroon?",
             ["Falling birth rate and rising death rate", "High birth rate and falling death rate", "High death rate and high birth rate", "Falling birth rate and falling death rate"],
             1, "Natural increase is births minus deaths. A high birth rate with a falling death rate makes the gap wide.",
             hint="Natural increase is the gap between births and deaths.",
             feedback=["That would reduce growth.", "", "With both high, the gap is smaller. The death rate has fallen.", "If births fell as fast as deaths the gap would not widen."], title="Quick check 2"),
        H("Practice questions"),
        PQ("Describe the growth pattern of the population of Cameroon.",
           "The population has grown quickly for many years. The birth rate has stayed high while the death rate has fallen, "
           "so natural increase is large. As a result, the number of people increases every year. This growth is mainly "
           "from natural increase, not from migration. Give the latest figures from your textbook if asked."),
        PQ("Explain two causes of the high rate of population growth in Cameroon.",
           "First, the birth rate is high. Large families are valued and, in farming areas, children help with work. Family planning "
           "services do not reach everyone. Second, the death rate has fallen because of better health care, immunisation, safer "
           "water and better food. When the birth rate stays high and the death rate falls, natural increase is large."),
        PQ("Using Figure 2, calculate the percentage of the population aged 0 to 14 years. Show your working.",
           "Males 0 to 14: 8.7 + 7.6 + 6.6 = 22.9 percent. Females 0 to 14: 8.5 + 7.4 + 6.5 = 22.4 percent. "
           "Total: 22.9 + 22.4 = 45.3 percent. This is almost half the population, which shows a young population."),
        PQ("Outline three results of a young and rapidly growing population.",
           "First, pressure on services: more schools, teachers and clinics are needed. Second, pressure on jobs and land: "
           "many young people look for work, farms become smaller and some move to towns. Third, opportunity: there is a large "
           "workforce and a growing market, if jobs and training are provided."),
        SUM("Cameroon has a young, growing population: a high birth rate and a falling death rate give a large natural increase.",
            "Natural increase is the birth rate minus the death rate (per 1000 people).",
            "An age-sex pyramid with a wide base and a narrow top shows many young people and few elderly people.",
            "To draw a pyramid, use one scale, males on the left, females on the right, equal bar heights, labels and a title.",
            "Causes: social, economic and service reasons for high births; health, water and food for lower deaths.",
            "Results: pressure on services, jobs and land, but also a large workforce and market."),
    ],
))

# ------------------------------------------------------------------ 2. Distribution
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Spatial distribution of population in Cameroon",
    slug="cmrhum-population-distribution",
    minutes=22,
    summary="People are not spread evenly across Cameroon. This lesson describes the dense and sparse areas on a sketch map and explains them with physical and human factors.",
    objectives=[
        "Describe the spatial pattern of population distribution in Cameroon",
        "Locate the main dense and sparse areas on a sketch map",
        "Explain the pattern using physical and human factors",
        "Calculate population density from population and area",
    ],
    key_concepts=["Population distribution", "Population density", "Dense and sparse areas", "Physical factors", "Human factors"],
    blocks=[
        H("Introduction"),
        T("Travel by road from Bafoussam to Bertoua. In the Grassfields, villages and farms follow each other closely. "
          "Further east, you can drive for a long time through forest before reaching the next settlement. "
          "The land is the same country, but the number of people per kilometre is very different."),
        D("**Population distribution** is the way people are spread across an area. It shows where people live and where "
          "few people live.", title="Population distribution"),
        D("**Population density** is the average number of people living in each square kilometre. It is found by dividing the "
          "number of people by the area.", title="Population density",
          formula=r"\text{density} = \frac{\text{number of people}}{\text{area in km}^2}"),
        T("A **dense** area has many people in each square kilometre. A **sparse** area has few. "
          "Average density for a whole country hides these differences, so geographers also look at maps."),
        H("The pattern on the map"),
        T("Figure 1 is a simplified sketch map. The general pattern is easy to remember: people are clustered in the "
          "west and south-west, in the cities, and in parts of the far north. The east and parts of the Adamawa have few people."),
        IMG("f5g-cmrhum-distribution-map.svg",
            alt="Sketch map of Cameroon with dense areas shaded in the western highlands, around Douala, around Yaounde, in the Far North near Maroua and near Garoua, and sparse areas in the east forest and parts of the Adamawa",
            caption="Figure 1. Dense and sparse areas of population in Cameroon (simplified sketch map, not to scale)."),
        KEY("Dense areas", "Places where many people live in each square kilometre.", cards=[
            ["Western highlands", "The Bamenda and Bafoussam areas of the North-West and West regions."],
            ["Coast and cities", "The Douala area on the coast, and the Yaoundé area in the Centre."],
            ["Parts of the Far North and north", "For example around Maroua and the Mandara foothills, and some areas near Garoua."],
        ]),
        KEY("Sparse areas", "Places where few people live in each square kilometre.", cards=[
            ["East and south-east", "A large forest zone with few towns and roads."],
            ["Parts of the Adamawa", "A high savanna plateau, used mainly for cattle."],
        ]),
        TIP("Describe a map in the order: general pattern, then the dense areas, then the sparse areas, with one or two named places "
            "for each. " + CHECK),
        H("Explaining the pattern: physical factors"),
        T("**Physical factors** come from nature: relief, climate, soils, water and natural vegetation. "
          "People tend to settle where farming is productive and where life is healthy."),
        T("In the western highlands, volcanic soils are fertile, rainfall is reliable and the cooler air is healthier "
          "than the hot lowlands. These conditions support intensive farming and a large number of people."),
        T("In the east and south-east, the dense equatorial forest makes farming, road building and settlement difficult. "
          "Many tropical forest soils lose their nutrients quickly when cleared. "
          "On the high Adamawa plateau, thin soils and savanna grass suit cattle rearing, which needs a lot of land for each person. "
          "Check your textbook for the role of diseases such as those spread by the tsetse fly."),
        H("Explaining the pattern: human factors"),
        T("**Human factors** come from people and society: jobs, transport, trade, services and history."),
        T("Douala has a large seaport, industries, banks and markets, so it attracts jobs and people. "
          "Yaoundé is the capital: it has government offices, universities and many services. "
          "Roads and railways link these places to rural areas, which supports further growth."),
        T("Some places are crowded because of history and land use. For example, long farming traditions in the highlands and "
          "the Far North have supported many people on small farms. Some densely settled hill areas may also have been "
          "chosen for safety in the past. Check your textbook for the history of the Mandara area."),
        T("Sparse areas often lack roads, towns and services. This makes people less willing to settle there. "
          "Job opportunities are fewer, so many young people leave."),
        EX("Model answer: explain the pattern", intro="Explain why the western highlands of Cameroon are densely populated.", steps=[
            S("Point 1: fertile soil", text="Volcanic soils are fertile, so farmers get good harvests of food crops and cash crops such as coffee. A farm can feed a large family."),
            S("Point 2: climate", text="Reliable rainfall and a cooler climate suit many crops and are healthier than hot, humid lowlands."),
            S("Point 3: people and services", text="Towns such as Bamenda and Bafoussam have markets, schools and roads. These attract and keep people."),
            S("Conclusion", text="Physical advantages and human developments together explain the high density."),
        ]),
        H("Calculating population density"),
        EX("Worked example: density", intro="District X has 120 000 people and an area of 400 square kilometres. District Y has 18 000 people and an area of 900 square kilometres. These are fictitious districts. Calculate the density of each.", steps=[
            S("Use the formula", math=r"\text{density} = \frac{\text{people}}{\text{area}}"),
            S("District X", math=r"\frac{120\,000}{400} = 300 \text{ people per km}^2"),
            S("District Y", math=r"\frac{18\,000}{900} = 20 \text{ people per km}^2"),
            S("Compare", text="District X is much denser than District Y (300 compared with 20). It is 15 times as dense."),
        ]),
        MISTAKE("Giving only physical or only human factors", "Most explanations in Paper 2 need both. Write at least one of each, and say how they work together."),
        MISTAKE("Saying 'no one lives' in sparse areas", "Sparse means few people, not none. Use 'low density' or 'few people'."),
        QUIZ("Which area of Cameroon is generally sparsely populated?",
             ["The Douala area", "The western highlands", "The east and south-east forest", "The Yaoundé area"],
             2, "The east and south-east forest has few roads, towns and services, so population density is low.",
             hint="Think of a large area of dense forest.",
             feedback=["Douala is a port city with many people.", "The highlands are densely populated.", "", "Yaoundé is a large city."]),
        QUIZ("A district has 60 000 people and an area of 300 square kilometres. What is its density?",
             ["20 people per km2", "200 people per km2", "300 people per km2", "18 000 people per km2"],
             1, "60 000 divided by 300 = 200 people per square kilometre.",
             hint="Divide the number of people by the area.",
             feedback=["20 is 6000 divided by 300; you left out a zero.", "", "300 is the area, not the density.", "You multiplied instead of dividing."], title="Quick check 2"),
        H("Practice questions"),
        PQ("Describe the distribution of population in Cameroon.",
           "Population is unevenly distributed. Dense areas include the western highlands (around Bamenda and Bafoussam), "
           "the Douala coastal area and Yaoundé area, and parts of the Far North and north. Sparse areas include the east and "
           "south-east forest and parts of the Adamawa plateau. Cities and the west are generally more crowded than the east."),
        PQ("Explain two physical factors that influence population distribution in Cameroon.",
           "First, soils: the fertile volcanic soils of the western highlands support intensive farming and many people, while many "
           "forest soils in the east lose nutrients quickly. Second, relief and vegetation: dense equatorial forest in the east "
           "makes roads and farming difficult, and the high Adamawa plateau is used for cattle, which supports few people per square kilometre."),
        PQ("Explain two human factors that attract people to the Douala area.",
           "First, economic activity: the port, industries, banks and markets provide jobs. Second, transport and services: "
           "roads, rail and the port link Douala with other regions, and the city has schools and hospitals. "
           "Jobs and services attract migrants, so density is high."),
        PQ("A village has 4500 people on 15 square kilometres. Calculate the density. (Fictitious data)",
           "Density = 4500 divided by 15 = 300 people per square kilometre."),
        SUM("Distribution is the pattern of where people live. Density is people per square kilometre.",
            "Dense areas: western highlands, Douala and Yaoundé areas, parts of the Far North and north.",
            "Sparse areas: the east and south-east forest and parts of the Adamawa.",
            "Physical factors: soils, climate, relief, vegetation and water. Human factors: jobs, ports, transport, services and history.",
            "Density = number of people divided by area in square kilometres.",
            "Good explanations use both physical and human factors with named places."),
    ],
))

# ------------------------------------------------------------------ 3. Migration
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Migration patterns in Cameroon",
    slug="cmrhum-migration-patterns",
    minutes=22,
    summary="People move within and across the borders of Cameroon for work, land, services and safety. This lesson describes the main flows and explains them with push and pull factors.",
    objectives=[
        "Define migration, internal migration and cross-border migration",
        "Describe the general migration patterns in Cameroon",
        "Explain migration using push and pull factors",
        "Outline the effects of migration on source and destination areas",
    ],
    key_concepts=["Migration", "Push factor", "Pull factor", "Rural-urban migration", "Internal migration", "Cross-border migration"],
    blocks=[
        H("Introduction"),
        T("A young man leaves a village in the Far North for a job in a town in the south. A family from the western "
          "highlands moves to the coast to work on a plantation. A trader crosses a border to sell goods in a market in "
          "a neighbouring country. These are all examples of **migration**."),
        D("**Migration** is the movement of people from one place to live in another, usually for a long time. "
          "**Internal migration** happens inside a country. **Cross-border** (international) migration crosses a country border.",
          title="Migration"),
        D("A **push factor** is a reason that makes people want to leave a place. A **pull factor** is a reason that "
          "attracts people to a place.", title="Push and pull factors"),
        T("**Emigrants** leave a place. **Immigrants** arrive in it. **Net migration** is the number of arrivals minus the number of departures."),
        H("General migration patterns"),
        T("Figure 1 shows the main flows in simplified form. The arrows show general directions only. " + CHECK),
        IMG("f5g-cmrhum-migration-map.svg",
            alt="Sketch map of Cameroon with arrows: north to south from the Far North towards the Centre, from the western highlands to the coast and to the Centre, from villages towards Yaounde and Douala, and two-way arrows across the borders with Nigeria and Chad",
            caption="Figure 1. Main migration flows in Cameroon (simplified sketch map, not to scale)."),
        KEY("Main patterns", "Four patterns appear again and again in textbooks.", cards=[
            ["Rural to urban", "From villages to towns, especially Douala and Yaoundé."],
            ["Towards plantations and farm belts", "To the coast and the South-West for plantation work, and to cocoa and coffee-growing areas."],
            ["North to south", "From the drier north towards the wetter south."],
            ["Cross-border", "To and from neighbouring countries such as Nigeria and Chad."],
        ]),
        TIP("Most of the movement is internal. People moving across borders are fewer than people moving between regions. "
            "Say this if you are asked to compare."),
        H("Explaining the patterns: push and pull factors"),
        IMG("f5g-cmrhum-push-pull.svg",
            alt="Two boxes joined by an arrow: push factors at the village origin and pull factors at the town destination",
            caption="Figure 2. Push factors at the origin and pull factors at the destination."),
        T("**Rural to urban.** Push: shortage of land, low farm incomes, few schools and clinics, and few jobs for young people. "
          "Pull: jobs, wages, schools, hospitals, electricity and the hope of a better life. Young people often move first."),
        T("**Towards plantations and farm belts.** Pull: plantation work and land for cash crops such as cocoa and coffee, "
          "and the markets for these crops. Many people from crowded highland areas moved to areas with more land or work, such as parts of the "
          "coast and the cocoa areas of the Centre, South and South-West. Check your textbook for named examples."),
        T("**North to south.** Push: in the drier north, rainfall is lower and drought and shortage of farmland can reduce "
          "harvests. Pull: wetter southern areas have more farming and more jobs in towns and cash-crop areas."),
        T("**Cross-border.** People move to trade, to find work, to join family and sometimes to escape insecurity. "
          "Cameroon has both emigrants and immigrants. Markets near borders, such as those with Nigeria and Chad, make movement easy."),
        EX("Model answer: explain a pattern", intro="Explain why many young people migrate from rural areas to Douala and Yaoundé.", steps=[
            S("Push: farming", text="Farmland is limited and farm incomes are low, so young people see few chances to earn money in the village."),
            S("Push: services", text="Some villages have few secondary schools and clinics, so families move to find them."),
            S("Pull: jobs", text="Douala and Yaoundé have industries, offices, shops, a port and informal work, so there are more job chances."),
            S("Pull: services and links", text="Cities have universities, hospitals and relatives who can offer a place to stay."),
            S("Link", text="Push and pull factors together explain the flow. Remember that perceived opportunity is not always real: many migrants find only low-paid informal work."),
        ]),
        H("Effects of migration"),
        T("Migration changes both the place that people leave and the place they go to."),
        KEY("Effects", "Think about people, jobs and services.", cards=[
            ["Source area", "Loss of young workers, fewer people to farm, but money sent home (remittances) can help families."],
            ["Destination area", "More labour and a bigger market, but pressure on housing, water, schools and jobs."],
        ]),
        EX("Worked example: net migration", intro="In an imaginary town, 12 000 people arrive in a year and 8 000 leave. What is the net migration?", steps=[
            S("Use the formula", math=r"\text{net migration} = \text{arrivals} - \text{departures}"),
            S("Calculate", math=r"12\,000 - 8\,000 = +4\,000"),
            S("Meaning", text="A positive answer means more people arrived than left, so migration added 4 000 people to the town."),
        ]),
        MISTAKE("Confusing push and pull", "Push factors belong to the place people leave. Pull factors belong to the place they go to. "
                "A shortage of jobs in a village is a push factor. A factory with jobs in a town is a pull factor."),
        MISTAKE("Giving only one reason", "Migration decisions usually have several reasons. Give at least one push and one pull factor, "
                "and say how they connect."),
        QUIZ("Which of the following is a pull factor for a young person moving to Douala?",
             ["Shortage of farmland in the village", "Jobs in the port and industries", "Low farm prices", "Drought in the north"],
             1, "Jobs in the port and industries attract people to Douala. The others are push factors from the place they leave.",
             hint="A pull factor belongs to the destination.",
             feedback=["That is a push factor in the village.", "", "Low farm prices push people away from farming areas.", "Drought is a push factor in the origin area."]),
        QUIZ("Moving from a village in the Far North to a town in the south is an example of",
             ["Cross-border migration", "Internal migration", "Immigration", "Natural increase"],
             1, "Both places are in Cameroon, so this is internal migration.",
             hint="Both the start and the end are inside the same country.",
             feedback=["No border is crossed.", "", "Immigration is arriving from another country.", "Natural increase is births minus deaths, not movement."], title="Quick check 2"),
        H("Practice questions"),
        PQ("Define the terms push factor and pull factor, with one example of each.",
           "A push factor is a reason for leaving a place, such as a shortage of farmland in a village. A pull factor is a reason "
           "for choosing a place, such as jobs in a town."),
        PQ("Describe the general pattern of migration in Cameroon shown in Figure 1.",
           "Many people move from rural areas to towns, especially Douala and Yaoundé. People also move from the western highlands "
           "to the coast and to cocoa areas in the south, and from the north towards the south. Some people cross the borders with "
           "Nigeria and Chad in both directions."),
        PQ("Explain three reasons why people move from the north to the south of Cameroon.",
           "First, the north is drier and farming can be difficult in dry years. Second, pressure on land is high in some areas, "
           "so farms are small. Third, the south has more jobs in towns, cash-crop areas and plantations. These are push factors "
           "in the north and pull factors in the south."),
        PQ("Outline two effects of rural-urban migration on the countryside.",
           "First, many young workers leave, so fewer people are available to farm and the population becomes older. "
           "Second, migrants may send money home, which can help families pay for food and school fees."),
        SUM("Migration is long-term movement of people. It can be internal or cross-border.",
            "Main patterns in Cameroon: rural to urban, towards plantations and cocoa and coffee areas, north to south, and cross-border.",
            "Push factors are reasons for leaving. Pull factors are reasons for going to a place.",
            "Push: shortage of land, low incomes, few services, drought. Pull: jobs, wages, services, land for cash crops.",
            "Effects on the source area: loss of young workers and remittances. Effects on the destination: labour, a bigger market and pressure on services."),
    ],
))

# ------------------------------------------------------------------ 4. Settlement and urbanisation
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Settlement and urbanisation in Cameroon",
    slug="cmrhum-settlement-and-urbanisation",
    minutes=22,
    summary="Settlements in Cameroon range from small farming villages to the large cities of Douala and Yaoundé. This lesson describes settlement patterns and the unequal rate of urbanisation, and explains the reasons.",
    objectives=[
        "Describe the main types and patterns of settlement in Cameroon",
        "Locate the main urban centres on a sketch map",
        "Describe the disparities in the rate of urbanisation between areas",
        "Explain the reasons for the differences in urbanisation",
    ],
    key_concepts=["Settlement", "Nucleated, linear and dispersed", "Urbanisation", "Rate of urbanisation", "Urban centre", "Primate city"],
    blocks=[
        H("Introduction"),
        T("From the plane above Cameroon you could see many different settlements: farming hamlets in the forest, villages "
          "along a road in the Adamawa, large compounds in the Far North and busy cities on the coast. Each is a **settlement**."),
        D("A **settlement** is a place where people live and build homes. A **rural settlement** is small and mainly depends on farming, fishing or herding. "
          "An **urban settlement** is larger and depends mainly on trade, industry, administration and services.",
          title="Settlement"),
        H("Settlement patterns"),
        T("The pattern is the way the houses are arranged on the ground. There are three main patterns."),
        IMG("f5g-cmrhum-settlement-patterns.svg",
            alt="Three panels: nucleated houses clustered round a centre, linear houses in two lines along a road, and dispersed houses scattered with gaps between them",
            caption="Figure 1. Nucleated, linear and dispersed settlement patterns (imaginary examples)."),
        KEY("Three patterns", "Describe each by the arrangement of houses.", cards=[
            ["Nucleated", "Houses are grouped closely together, often around a market, chief's compound or water point."],
            ["Linear", "Houses are in a line along a road, river or railway."],
            ["Dispersed", "Houses are spread out with space between them, often with each home near its own farm."],
        ]),
        T("Each pattern has reasons. Nucleated villages often grew for safety, water or trade. Linear settlements follow roads that "
          "give access to markets. Dispersed settlement is found where farms are large or land is spread out. "
          "Real villages often mix patterns, and several types can be found in a single region. " + CHECK),
        H("Urbanisation"),
        D("**Urbanisation** is the increase in the share of a country's people who live in towns and cities. "
          "The **rate of urbanisation** is how quickly this share is increasing.", title="Urbanisation"),
        T("Urbanisation has two main causes. First, **rural-urban migration**: people move to towns. Second, **natural increase** "
          "in towns, because births are higher than deaths. A town can also grow when its boundaries are widened."),
        T("Cameroon is urbanising quickly. Urban centres are growing faster than the national population."),
        H("Main urban centres"),
        IMG("f5g-cmrhum-towns-map.svg",
            alt="Sketch map of Cameroon marking Douala and Yaounde as the two largest cities and regional towns including Bamenda, Bafoussam, Maroua, Garoua, Ngaoundere, Bertoua, Ebolowa, Buea and the port of Kribi",
            caption="Figure 2. Main urban centres of Cameroon (simplified sketch map, not to scale)."),
        T("**Douala** is the main seaport and the leading commercial and industrial city. "
          "**Yaoundé** is the capital and the centre of government. These are the two largest cities. "
          "Each region has a regional headquarters: Bafoussam, Bamenda, Buea, Ebolowa, Bertoua, Ngaoundéré, Garoua and Maroua. "
          "**Kribi** is a second seaport."),
        TIP("Learn the ten regional capitals as pairs. West and North-West: Bafoussam and Bamenda. South and South-West: Ebolowa and Buea. "
            "North of the country: Ngaoundéré, Garoua, Maroua. Centre and East: Yaoundé and Bertoua. Littoral: Douala."),
        H("Differences in the rate of urbanisation"),
        T("Urbanisation is not the same everywhere. In general, the south and west are more urbanised and are urbanising faster. "
          "The Littoral and the Centre have the largest cities. Some northern and eastern areas are more rural, "
          "though towns such as Garoua, Maroua and Ngaoundéré are growing. Check your textbook for the latest regional figures."),
        KEY("Reasons for the differences", "Use cause and result in your answers.", cards=[
            ["Where jobs are", "Industry, the port, banks and government jobs are concentrated in Douala and Yaoundé, so migrants go there."],
            ["Transport links", "Good roads, rail and the port encourage trade and the growth of towns along them."],
            ["Farming and history", "In some northern and eastern areas, most people still farm or herd, and fewer large industries exist."],
            ["Services", "Cities have more schools, hospitals and electricity, and young people move there."],
        ]),
        EX("Model answer: explain the differences", intro="Explain why urbanisation is more advanced in the Littoral than in the Far North.", steps=[
            S("Point 1: economy", text="The Littoral has the port of Douala, industries, banks and many other jobs. These attract migrants, so the city grows."),
            S("Point 2: transport", text="Roads, rail and sea links make trade easy and encourage the growth of towns."),
            S("Point 3: the north", text="Many people in the Far North depend on farming and herding, and there are fewer large industries, so fewer jobs pull people into towns."),
            S("Conclusion", text="Jobs, transport and the structure of the economy explain the difference. Towns like Maroua are growing, but more slowly than Douala."),
        ]),
        MISTAKE("Writing only a list of towns", "Naming towns is not enough. Say where each is, what it does (port, capital, market) and why it grew."),
        MISTAKE("Confusing urbanisation with urban population", "Urbanisation is the rise in the share of people living in towns. "
                "A country can have a large urban population and a slow rate of urbanisation."),
        H("Calculating the urban share"),
        EX("Worked example: urban percentage", intro="In an imaginary region of 150 000 people, 45 000 live in towns. What percentage live in towns?", steps=[
            S("Formula", math=r"\text{urban share} = \frac{\text{urban population}}{\text{total population}} \times 100"),
            S("Substitute", math=r"\frac{45\,000}{150\,000} \times 100 = 30"),
            S("Answer", text="Thirty percent of this region lives in towns."),
        ]),
        QUIZ("Houses are arranged in lines along a main road. What type of settlement pattern is this?",
             ["Nucleated", "Linear", "Dispersed", "Isolated"],
             1, "Houses in a line along a road or river form a linear pattern.",
             hint="Think about the shape of the line.",
             feedback=["Nucleated houses are grouped round a centre.", "", "Dispersed houses are spread out with gaps.", "Isolated is not one of the three patterns."]),
        QUIZ("Which is the main seaport and commercial city of Cameroon?",
             ["Yaoundé", "Bamenda", "Douala", "Maroua"],
             2, "Douala is the main seaport and leading commercial city. Yaoundé is the capital.",
             hint="Think of the port on the Wouri estuary.",
             feedback=["Yaoundé is the capital, not the main port.", "Bamenda is the regional capital of the North-West.", "", "Maroua is the capital of the Far North."], title="Quick check 2"),
        H("Practice questions"),
        PQ("Describe the three main settlement patterns.",
           "Nucleated settlements have houses clustered closely together. Linear settlements have houses in a line along a road or river. "
           "Dispersed settlements have houses spread over the land with gaps between them."),
        PQ("Name and locate three urban centres in Cameroon and state one function of each.",
           "Douala is on the coast and is the main seaport and commercial city. Yaoundé is in the Centre region and is the capital. "
           "Maroua is in the Far North and is a regional headquarters and market centre. Other examples: Bamenda in the North-West, Kribi on the coast."),
        PQ("Explain why urbanisation is faster in some regions than in others.",
           "Urbanisation is faster where jobs and services are concentrated. Douala and Yaoundé have a port, industries, government work, "
           "universities and hospitals, so migrants go there. Transport links help trade. In some northern and eastern areas, farming and "
           "herding are the main activities and fewer large industries exist, so towns grow more slowly."),
        PQ("A region has 80 000 people and 24 000 live in towns. Calculate the urban percentage. (Exercise data)",
           "24 000 divided by 80 000, times 100, is 30 percent."),
        SUM("Settlement patterns are nucleated, linear and dispersed.",
            "Urbanisation is the rise in the share of people living in towns. Causes: rural-urban migration and natural increase.",
            "Douala (port) and Yaoundé (capital) are the two largest cities. Each region has a regional capital.",
            "Urbanisation is faster in the Littoral and Centre than in much of the north and east.",
            "Reasons: where jobs are, transport links, services, and the main economic activity of the area."),
    ],
))

# ------------------------------------------------------------------ 5. Challenges and links
LESSONS.append(lesson(
    module=MODULE,
    topic=TOPIC,
    title="Rural and urban challenges and town-countryside links",
    slug="cmrhum-rural-and-urban-challenges-and-town-countryside-links",
    minutes=24,
    summary="Both villages and cities face problems, and efforts are made to solve them. Towns and the countryside also depend on each other through food, labour, services, markets and money.",
    objectives=[
        "Outline the main challenges of rural and urban settings in Cameroon",
        "Outline efforts made to resolve rural and urban problems",
        "Describe the relationships between town and countryside",
        "Explain how flows of goods, people and money link them",
    ],
    key_concepts=["Rural challenges", "Urban challenges", "Informal settlement", "Rural electrification", "Town-countryside link", "Remittances"],
    blocks=[
        H("Introduction"),
        T("A farmer near Bamenda grows maize and vegetables. Her son studies in Yaoundé. A trader in Douala buys her "
          "plantains at the market and sells her soap, cooking oil and school books. Each depends on the other. "
          "But both also face problems: poor roads in her village and crowded housing in the city."),
        H("Challenges of rural areas"),
        T("A **challenge** or problem is something that makes life or work difficult. In many rural areas of Cameroon, "
          "the challenges are linked."),
        KEY("Rural challenges", "Think of services, income and transport.", cards=[
            ["Poor roads and transport", "Feeder roads can be muddy in the rainy season. Farmers struggle to bring crops to market and crops can spoil."],
            ["Limited services", "Fewer schools, clinics, electricity and clean water than in towns."],
            ["Low income", "Farm incomes are small and uncertain, and farms may be small."],
            ["Loss of young people", "Many young people leave for towns, so fewer workers remain."],
        ]),
        H("Efforts to solve rural problems"),
        T("Several kinds of effort are made, by government, local councils, communities and non-governmental organisations (NGOs). "
          "Check your textbook for the names of specific programmes."),
        KEY("Efforts", "For each problem, think of one solution.", cards=[
            ["Roads", "Building and repairing feeder roads to link farms to markets."],
            ["Services", "Building schools and health centres, bringing in water supply and electricity (rural electrification)."],
            ["Farming support", "Farmers' groups and cooperatives, access to credit, training and better seeds."],
            ["Local development", "Local councils and community self-help projects that use local labour."],
        ]),
        H("Challenges of urban areas"),
        KEY("Urban challenges", "Fast growth makes it hard for services to keep up.", cards=[
            ["Housing", "Not enough housing. Some people live in crowded informal settlements, sometimes on land that floods."],
            ["Unemployment and informal work", "More people than formal jobs. Many earn a living in small trades and services."],
            ["Traffic and transport", "Congested roads and too few public transport services."],
            ["Water, waste and drainage", "Water supply and waste collection do not reach everyone. Poor drainage leads to flooding in heavy rain."],
        ]),
        D("An **informal settlement** is a part of a town where people have built homes without proper planning or services, "
          "such as piped water, sewers or paved roads.", title="Informal settlement"),
        H("Efforts to solve urban problems"),
        KEY("Efforts", "Planning, building and investing.", cards=[
            ["Planning and housing", "Town planning, building new housing and improving informal areas with roads, drainage and water."],
            ["Transport", "Road building and repair, and better public transport."],
            ["Environment", "Drainage channels, rubbish collection and waste management."],
            ["Jobs", "Support for small businesses and training for young people."],
            ["Decentralisation", "Local councils get more responsibility for planning and services. Another idea is to develop other towns, so that fewer people move only to Douala and Yaoundé."],
        ]),
        EX("Model answer: challenge and efforts", intro="Outline two problems of a fast-growing city in Cameroon and one effort to solve each.", steps=[
            S("Problem 1: housing", text="Many migrants arrive and housing is short, so some people live in crowded informal settlements without good water or drainage."),
            S("Effort 1", text="Town planners can improve these areas with roads, drainage and water points, and build more housing."),
            S("Problem 2: flooding and waste", text="Rubbish and poor drains block channels, so streets flood in heavy rain."),
            S("Effort 2", text="Councils can build and clean drains, collect waste and stop building in flood-prone places."),
        ]),
        H("Town-countryside relationships"),
        T("Towns and the countryside are **interdependent**: each needs what the other provides. "
          "Goods, people, money and services move between them in both directions."),
        IMG("f5g-cmrhum-flows.svg",
            alt="Diagram with the countryside on the left and the town on the right: blue arrows carry food and cash crops, workers and migrants, and timber and firewood to the town; orange arrows carry goods and farm inputs, schools clinics and banks, and wages and remittances to the countryside",
            caption="Figure 1. Flows between countryside and town."),
        KEY("From countryside to town", "What farms and villages provide.", cards=[
            ["Food supply", "Maize, plantains, cassava, vegetables and livestock sold in town markets."],
            ["Raw materials", "Cash crops such as cocoa and coffee, timber, firewood and charcoal."],
            ["Labour", "Workers and students move to the town."],
        ]),
        KEY("From town to countryside", "What towns provide.", cards=[
            ["Goods and inputs", "Manufactured goods, tools, fertiliser and building materials sold in shops."],
            ["Services", "Hospitals, secondary schools and universities, banks and government offices."],
            ["Markets and money", "Markets where farmers can sell. Wages and remittances (money sent home by relatives working in town)."],
        ]),
        T("Roads and rail make these links possible. Weekly markets in small towns are often the meeting place for villagers and traders."),
        EX("Model answer: describe the links", intro="Describe the relationships between a town and the surrounding countryside.", steps=[
            S("Food and markets", text="Farmers bring food to town markets. This feeds the town and gives farmers income."),
            S("Labour and people", text="Young people move to town to work or study, and some people commute or return to the village at weekends."),
            S("Goods and services", text="Town shops sell manufactured goods, and villagers use hospitals, schools and banks in town."),
            S("Money", text="Workers in town send money home. This pays for food, school fees and farm inputs."),
        ]),
        MISTAKE("Describing only one direction", "A link is a flow in both directions. Name at least one flow from the countryside to the town "
                "and one from the town to the countryside."),
        MISTAKE("Listing problems without solutions", "Questions that ask for 'efforts' need solutions with a clear link to each problem."),
        QUIZ("Which of these is a flow of money from town to countryside?",
             ["Food sold at the market", "Remittances sent home by workers in town", "Timber sent to a sawmill", "Students moving to a university"],
             1, "Remittances are money sent home from town workers to relatives in the countryside.",
             hint="Which choice is money moving to the village?",
             feedback=["Food moves from the countryside to the town.", "", "Timber moves from the countryside to a town.", "Students are people, not money, and move to the town."]),
        QUIZ("Which is the best effort to help farmers get their crops to market?",
             ["Build a stadium in the capital", "Repair feeder roads", "Close village markets", "Raise the price of fertiliser"],
             1, "Feeder roads link farms to markets, so crops reach buyers faster.",
             hint="Which action links the farm to the market?",
             feedback=["A stadium does not help transport.", "", "Closing markets would make it harder to sell crops.", "Higher fertiliser prices make farming harder."], title="Quick check 2"),
        H("Practice questions"),
        PQ("Outline three challenges of rural areas in Cameroon.",
           "First, roads are poor, so crops are hard to take to market. Second, services are limited: there are fewer schools, "
           "clinics and sources of electricity and clean water. Third, farm incomes are low, and young people leave for towns."),
        PQ("State three problems found in large towns in Cameroon, and one effort to solve each.",
           "Housing shortage: build new housing and improve informal areas. Flooding and waste: build drains and collect rubbish. "
           "Traffic congestion: repair roads and improve public transport. Other answers include unemployment and water supply."),
        PQ("Describe the relationship between a town and the countryside around it.",
           "The countryside supplies food, raw materials and labour to the town. The town provides goods, services such as hospitals "
           "and banks, markets and jobs. Money flows back to villages as wages and remittances. Roads and markets link the two."),
        PQ("A worker in Douala earns 60 000 FCFA a month and sends one-fifth to the family in the village. How much does he send? (Exercise data)",
           "One-fifth of 60 000 is 60 000 divided by 5 = 12 000 FCFA per month."),
        SUM("Rural challenges: poor roads, few services, low incomes and loss of young people.",
            "Rural efforts: feeder roads, schools and clinics, electricity and water, farmers' groups and credit.",
            "Urban challenges: housing, unemployment, traffic, water, waste and flooding.",
            "Urban efforts: planning and housing, transport, drainage and waste, support for small businesses, decentralisation.",
            "Towns and countryside depend on each other: food, raw materials and labour go to town; goods, services, markets and money go to the countryside.",
            "Always give links in both directions."),
    ],
))
