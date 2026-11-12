"""A Level Geography (0750), Lower Sixth: Population & Migration Geography, Settlement & Urban Geography, and the Examination module.

10 topic lessons and 3 examination lessons (slug prefix gpl3-), one practice set each (see the practice file of the same name),
plus Paper 1 mock exam A, Paper 2 practice paper A and Paper 3 practice paper A in the practice file.
Content follows KKEVO's master curriculum blueprint (module lines GEO-0750-L6M5 and L6M6) and the Board's 2023 Advanced Level
subject report for paper structure and the errors candidates made; it is not a Board syllabus booklet. All data sets for
calculations are invented for practice and labelled as such. Every statistic (densities, rates, dependency ratios, doubling
times, Todaro expected income, nearest neighbour index, urbanization rates, rank-size values, primacy indices, central place
counts, gradients, vertical exaggeration, sinuosity, interquartile range) was checked by script.
"""

from .dsl import *  # noqa: F403

COURSE = ("geography", "lower-sixth")

M_POP = "Population & Migration Geography"
M_SET = "Settlement & Urban Geography"
M_EXAM = "Examination"

LESSONS = []

# ------------------------------------------------------------------ 1. Population distribution and density
LESSONS.append(lesson(
    module=M_POP,
    topic="Population distribution and density",
    title="Population distribution and density: indices, patterns and explanations",
    slug="gpl3-population-distribution-density",
    minutes=23,
    summary="How geographers measure population density with crude, physiological and agricultural indices, map it, and explain uneven distribution through physical and human factors, with Cameroon as the case study.",
    objectives=[
        "Distinguish population distribution from population density and define the ecumene",
        "Calculate and interpret crude, physiological and agricultural density",
        "Explain uneven distribution using physical, economic, historical and political factors",
        "Evaluate the usefulness and limits of density figures and density maps",
    ],
    key_concepts=["Population distribution", "Crude density", "Physiological density", "Agricultural density",
                  "Ecumene", "Choropleth map", "Carrying capacity"],
    blocks=[
        H("Introduction"),
        T("Travel from Bafoussam to Bertoua and you see two very different Cameroons. Around Bafoussam and in the Bamenda "
          "Grassfields, compounds, farms and market towns crowd the hills. In much of the East region you can drive a long way "
          "through forest and see only small roadside villages. People are spread very unevenly over the earth's surface. "
          "At O Level you calculated a simple density. At A Level you must use several density indices, judge what each one "
          "shows, and explain the pattern with balanced reasoning."),
        H("Distribution and density"),
        D("**Population distribution** is the way people are spread over an area: where they live and where they do not. It is "
          "described as a pattern (even, uneven, clustered, linear). **Population density** is the number of people per unit "
          "of area, a single number for each area.", title="Two different ideas"),
        D("The **ecumene** is the inhabited, permanently settled part of the earth. The **anecumene** (non-ecumene) is the "
          "uninhabited or very thinly used part: ice sheets, high mountains, the driest deserts.", title="Ecumene"),
        T("About half of the world's people live on a small fraction of its land area, mainly in East Asia, South Asia, Europe "
          "and parts of West Africa and the Nile valley. Large areas are almost empty. Any description of distribution should "
          "therefore name the dense areas, the sparse areas and the pattern between them, with examples."),
        H("Three density indices"),
        F(r"\text{crude density} = \frac{\text{total population}}{\text{total land area (km}^2)}", title="Crude (arithmetic) density"),
        F(r"\text{physiological density} = \frac{\text{total population}}{\text{area of arable (cultivated) land (km}^2)}", title="Physiological density"),
        F(r"\text{agricultural density} = \frac{\text{farming population}}{\text{area of arable land (km}^2)}", title="Agricultural density"),
        KEY("What each index tells you", "Choose the index that fits the question.", cards=[
            ["Crude density", "Easy to calculate, but it divides people over all land, including forest, swamp and mountain that may not be usable."],
            ["Physiological density", "Shows the pressure of the whole population on the land that can feed it. A high value warns of pressure on farmland."],
            ["Agricultural density", "Shows how many farmers work each unit of farmland. A high value suggests small farms, rural crowding and possible push factors for migration."],
        ]),
        EX("Worked example 1: comparing two regions", intro="Two regions (data invented for practice). Region X: area 12 000 km², population 1 800 000, arable land 3 000 km², farmers 900 000. Region Y: area 40 000 km², population 1 200 000, arable land 12 000 km², farmers 720 000. Calculate the three densities for each and comment.", steps=[
            S("Crude density", math=r"X: \frac{1\,800\,000}{12\,000} = 150 \qquad Y: \frac{1\,200\,000}{40\,000} = 30 \text{ persons per km}^2"),
            S("Physiological density", math=r"X: \frac{1\,800\,000}{3\,000} = 600 \qquad Y: \frac{1\,200\,000}{12\,000} = 100 \text{ persons per km}^2 \text{ of arable land}"),
            S("Agricultural density", math=r"X: \frac{900\,000}{3\,000} = 300 \qquad Y: \frac{720\,000}{12\,000} = 60 \text{ farmers per km}^2 \text{ of arable land}"),
            S("Comment", text="X is five times as crowded as Y on the crude index, but six times on the physiological index: its people depend on a small area of farmland. Each X farmer has on average only 1/300 km² (about 0.33 ha) of land, so farms are small and young people may be pushed to migrate."),
        ], check=r"\frac{600}{150} = \frac{12\,000}{3\,000} = 4"),
        H("Mapping density"),
        T("A **dot map** shows distribution: each dot stands for a fixed number of people, placed where they live. A **choropleth map** "
          "shades each administrative area by its density class, darker for higher values. A choropleth is easy to read, but it "
          "suggests that density is even within each area and changes suddenly at boundaries, which is rarely true."),
        EX("Worked example 2: choosing choropleth classes", intro="Six divisions have densities (invented) of 18, 45, 96, 140, 260 and 410 persons per km². Use the classes 0-49, 50-99, 100-199 and 200 and over, and say how many divisions fall in each.", steps=[
            S("Sort the values", text="18, 45 | 96 | 140 | 260, 410."),
            S("Count", text="0-49: two divisions; 50-99: one; 100-199: one; 200 and over: two."),
            S("Shade", text="Use four shades of one colour, lightest for 0-49 and darkest for 200 and over. Classes must not overlap and must cover every value."),
        ]),
        H("Explaining the pattern"),
        KEY("Factors that influence distribution", "Explain each factor in two directions: how it attracts and how it repels people.", cards=[
            ["Physical", "Relief and altitude, climate (rainfall reliability, temperature), water supply, soil fertility (for example volcanic soils), vegetation, and disease such as river blindness or sleeping sickness in some valleys."],
            ["Economic", "Fertile farmland, minerals, ports, industry, plantations and services draw people. Places with few jobs lose people."],
            ["Historical and social", "Old kingdoms and dense farming traditions, past slave raiding that drove people to defensive hills, and colonial ports and railways."],
            ["Political", "Planned settlement schemes, capital cities, borders, protected areas and resettlement policies."],
        ]),
        T("In Cameroon, dense areas include the Western Highlands (West and North West regions), with fertile volcanic soils, a cool "
          "healthy climate and long farming traditions; the Far North plains and the Mandara Mountains; and the two large cities, "
          "Douala (port and industry) and Yaoundé (capital and services). Sparse areas include much of the East region and the "
          "southern forest, where dense forest, poor access and leached soils limit settlement, and parts of the Adamawa Plateau. "
          "Check your textbook or the latest census report for exact regional densities."),
        H("Evaluation: what density figures cannot show"),
        T("A density is an average. It hides clusters inside an area and says nothing about wealth, technology or resources. A "
          "high density is not the same as over-population: a rich, industrial region can support many people per km² well, while "
          "a poor dry region can be over-populated at a low density. The idea of **carrying capacity** (the largest population an "
          "area can support with a given technology without damaging its resources) helps here, but carrying capacity changes "
          "as technology changes. Data quality is also a limit: censuses are infrequent and boundaries change."),
        MISTAKE("Using 'distribution' and 'density' as if they mean the same", "Distribution is the pattern of where people are; density is a number per km². Describe a pattern with places and directions, and give densities with units."),
        MISTAKE("Explaining only one side of a factor", "Examiners expect two-sided explanations: high rainfall attracts farmers but extreme rainfall with dense forest and leached soil repels them. Give both effects and a named example."),
        QUIZ("Region P has a crude density of 40 persons per km² and a physiological density of 800 persons per km² of arable land. What does this suggest?", [
            "Only a small share of the land is arable, so there is heavy pressure on farmland",
            "Most of the land is arable and lightly used",
            "Most of the people are farmers",
            "The region is over-populated in all respects"], 0,
            "800 ÷ 40 = 20, so only one twentieth (5%) of the land is arable; the farmland carries a heavy load.",
            hint="Divide the physiological density by the crude density.",
            feedback=["", "If most land were arable, the two densities would be close.", "Agricultural density, not physiological density, measures farmers per arable km².", "Density alone cannot prove over-population; resources and technology matter."]),
        QUIZ("Which map is best for showing exactly where people live inside a large division?", ["Choropleth map", "Dot map", "Flow-line map", "Isoline map of rainfall"], 1,
             "Dots are placed where people live, so they show clusters inside an area.",
             hint="Which map does not shade the whole area evenly?",
             feedback=["A choropleth shades the whole area with one value and hides clusters.", "", "Flow lines show movement between places.", "A rainfall isoline map shows climate, not people."]),
        TIP("Population distribution appears in Paper 1 (definitions, density calculations, factors) and in Paper 2 essays such as 'account for the uneven distribution of population in a named country'. In Paper 3, density data can be mapped (choropleth) or used with Cameroon examples. Always give units and named places.", title="Exam link"),
        PQ("A division has 2 500 000 people on 20 000 km², of which 5 000 km² is arable, and 1 000 000 farmers. Calculate its crude, physiological and agricultural densities and explain what the physiological density adds to the crude density.",
           "Crude density = 2 500 000 ÷ 20 000 = 125 persons per km². Physiological density = 2 500 000 ÷ 5 000 = 500 persons per km² of arable land. Agricultural density = 1 000 000 ÷ 5 000 = 200 farmers per km² of arable land. The physiological density is four times the crude density, because only a quarter of the land is arable; it shows the real pressure of the population on the land that produces food."),
        PQ("Explain why the Western Highlands of Cameroon are more densely populated than the East region.",
           "Model plan. Introduction: define density; state that the Western Highlands have far higher densities. Point 1: fertile volcanic soils allow intensive food and cash-crop farming (coffee, maize, beans). Point 2: altitude gives a cooler, healthier climate with fewer disease vectors. Point 3: long-established farming societies and chiefdoms with dense villages and markets. Point 4: the East has dense forest, leached ferralitic soils, poor road access and historically fewer job opportunities, so people are few. Evaluation: densities are averages and the Highlands have sparse areas (steep slopes, high summits), while East region towns such as Bertoua are locally dense. Conclusion: physical advantages and history together explain the contrast."),
        PQ("'Population density is a poor measure of population pressure.' Discuss.",
           "Model plan. For the statement: crude density divides people by all land, including unusable land; it ignores technology, wealth and resources, so a dense rich region may not be under pressure while a sparse dry one may be; averages hide clusters. Against: physiological and agricultural densities relate people to farmland and do reveal pressure; density maps are a useful first view; changes in density over time show growth pressure. Conclusion: density is a starting point, best used with physiological density, carrying capacity and data on resources and living standards."),
        SUM("Distribution is the pattern of where people live; density is people per km².",
            "Crude density uses all land; physiological density uses arable land; agricultural density uses farmers per arable km².",
            "Dot maps show distribution; choropleth maps show density by area but hide variation inside areas.",
            "Physical, economic, historical and political factors explain uneven distribution; explain each in both directions.",
            "Density is an average and is not the same as over-population; relate it to resources, technology and carrying capacity."),
    ],
))

# ------------------------------------------------------------------ 2. Fertility, mortality and the demographic transition
LESSONS.append(lesson(
    module=M_POP,
    topic="Fertility, mortality and the demographic transition",
    title="Fertility, mortality and the demographic transition model: measures, causes and significance",
    slug="gpl3-fertility-mortality-dtm",
    minutes=25,
    summary="How fertility and mortality are measured (crude rates, total fertility, infant mortality, natural increase, doubling time), why they change, and how the demographic transition model describes, explains and predicts population change, with its significance and limits.",
    objectives=[
        "Calculate crude birth and death rates, natural increase, general fertility, infant mortality and doubling time",
        "Explain the economic, social and cultural factors that raise or lower fertility and mortality",
        "Describe the five stages of the demographic transition model and the causes of change between them",
        "Discuss the significance and the limitations of the model for countries such as Cameroon",
    ],
    key_concepts=["Crude birth rate", "Crude death rate", "Natural increase", "Total fertility rate", "Infant mortality rate",
                  "Replacement level", "Doubling time", "Demographic transition model"],
    blocks=[
        H("Introduction"),
        T("A population changes in only three ways: people are born, people die, and people move. This lesson deals with the first "
          "two, which together give **natural change**. Migration follows later in the module. Fertility and mortality explain why "
          "Cameroon's population has grown fast for decades while the populations of Japan and Italy have begun to shrink."),
        H("Measuring fertility and mortality"),
        F(r"\text{CBR} = \frac{\text{live births in a year}}{\text{mid-year population}} \times 1\,000 \qquad \text{CDR} = \frac{\text{deaths in a year}}{\text{mid-year population}} \times 1\,000", title="Crude birth and death rates (per 1 000)"),
        F(r"\text{rate of natural increase (\%)} = \frac{\text{CBR} - \text{CDR}}{10}", title="Natural increase"),
        D("**General fertility rate (GFR)**: live births per 1 000 women aged 15 to 49 in a year. **Total fertility rate (TFR)**: the "
          "average number of children a woman would have in her lifetime at current age-specific rates. **Replacement level** "
          "fertility is a TFR of about 2.1, enough for each generation to replace itself (slightly above 2 because some children "
          "die young and slightly more boys than girls are born).", title="Fertility measures"),
        D("**Infant mortality rate (IMR)**: deaths of babies under one year old per 1 000 live births. **Life expectancy**: the average "
          "number of years a newborn can expect to live at current death rates. The IMR is a sensitive indicator of health care, "
          "nutrition and the education of mothers.", title="Mortality measures"),
        F(r"\text{doubling time (years)} \approx \frac{70}{\text{growth rate in \%}}", title="Rule of 70"),
        EX("Worked example 1: rates for a country", intro="A country (data invented for practice) has a mid-year population of 25 000 000, 900 000 live births and 225 000 deaths in a year. Calculate the CBR, CDR, rate of natural increase and doubling time.", steps=[
            S("CBR", math=r"\frac{900\,000}{25\,000\,000} \times 1\,000 = 36 \text{ per } 1\,000"),
            S("CDR", math=r"\frac{225\,000}{25\,000\,000} \times 1\,000 = 9 \text{ per } 1\,000"),
            S("Natural increase", math=r"\frac{36 - 9}{10} = 2.7\%"),
            S("Doubling time", math=r"\frac{70}{2.7} \approx 26 \text{ years}", text="With no migration, the population would double in about 26 years."),
        ], check=r"25\,000\,000 \times (1.027)^{26} \approx 50\,000\,000"),
        EX("Worked example 2: GFR and IMR", intro="In the same country 5 500 000 women are aged 15 to 49, and 46 800 of the 900 000 babies born died before their first birthday. Calculate the GFR and the IMR.", steps=[
            S("GFR", math=r"\frac{900\,000}{5\,500\,000} \times 1\,000 \approx 163.6 \text{ per } 1\,000 \text{ women}"),
            S("IMR", math=r"\frac{46\,800}{900\,000} \times 1\,000 = 52 \text{ per } 1\,000 \text{ live births}"),
            S("Why GFR is better than CBR", text="The CBR divides by everyone, including men, children and old people. The GFR divides only by the women who can give birth, so it is not distorted by the age-sex structure."),
        ]),
        H("Why fertility and mortality change"),
        KEY("Factors affecting fertility", "Each can raise or lower the birth rate.", cards=[
            ["Economic", "Where children work on farms and support parents in old age, large families make sense. In cities, school fees and housing make children costly."],
            ["Infant mortality", "Where many babies die, parents may have more children to be sure some survive. Falling IMR is usually followed by falling fertility."],
            ["Education and status of women", "Girls who stay longer at school marry later, have paid work and choose smaller families."],
            ["Family planning and policy", "Access to contraception and government programmes (anti-natalist or pro-natalist) change fertility."],
            ["Social and cultural norms", "Value placed on large families, age at marriage, and religious teaching influence family size; treat these respectfully and with evidence."],
        ]),
        KEY("Factors affecting mortality", "Death rates fell first in most countries.", cards=[
            ["Health and medicine", "Vaccination, antibiotics, oral rehydration, malaria control and clinics."],
            ["Water, sanitation, food", "Clean water, latrines and better nutrition reduce diarrhoea and infection."],
            ["Shocks", "Epidemics (for example HIV/AIDS in parts of southern Africa), famine and conflict raise death rates."],
            ["Age structure", "An old population has a higher CDR even with good health care, because more people are at ages where death is likely."],
        ]),
        H("The demographic transition model"),
        T("The **demographic transition model (DTM)** describes how birth and death rates, and so total population, change as a "
          "country develops. It was built from the experience of Western Europe and North America (Warren Thompson and Frank "
          "Notestein are usually credited; check your textbook). A fifth stage was added later for countries where births fall below deaths."),
        IMG("algpl3-dtm.svg", alt="Demographic transition model: birth rate line and death rate line across five stages, with total population rising slowly in stage 1, rapidly in stages 2 and 3, levelling in stage 4 and falling slightly in stage 5",
            caption="Figure 1. The demographic transition model (schematic). The gap between the birth rate and death rate is the natural increase."),
        KEY("The five stages", "Learn the rates, the growth and the causes.", cards=[
            ["1 High stationary", "High, fluctuating birth and death rates (about 35 to 40 per 1 000). Little growth. Famine and disease."],
            ["2 Early expanding", "Death rate falls fast (clean water, vaccination, food supply); birth rate stays high. Rapid growth."],
            ["3 Late expanding", "Birth rate falls (urbanization, education of women, family planning, lower IMR); death rate falls more slowly. Growth slows."],
            ["4 Low stationary", "Both rates low (about 10 to 15 per 1 000). Little growth; the population ages."],
            ["5 Declining", "Birth rate below death rate. Natural decrease, as in Japan and several European countries."],
        ]),
        H("Significance of the model"),
        T("Examiners ask for the **significance** of the DTM, not only its stages. The model is significant because it gives a "
          "framework for comparing countries at one moment; it links population change to economic and social development; it "
          "helps governments predict future change and plan (for schools and jobs in stages 2 and 3, for pensions and health care "
          "of the elderly in stages 4 and 5); and it shows which policy is needed, such as family planning in stage 3 or "
          "pro-natalist measures in stage 5."),
        H("Evaluation of the model"),
        T("Strengths: simple, easy to apply, and it fits the history of many developed countries well. Limitations: it is based on "
          "Western European experience; in many developing countries death rates fell much faster than in Europe because medicine "
          "was imported, so growth in stage 2 was faster and larger; birth rates can fall without industrialization when education "
          "and family planning spread; it ignores migration, which can change a population more than natural change; it gives no "
          "time scale; and it cannot predict shocks such as epidemics or wars. Cameroon is usually placed in late stage 2 or stage 3, "
          "with falling but still high fertility (check recent data in your textbook)."),
        MISTAKE("Describing the stages when the question asks for significance", "In the Board's 2023 report many candidates described the characteristics of the DTM, or wrote about Rostow's model, when asked for its significance. Answer the command: explain how the model is useful for comparison, prediction and planning, with examples."),
        MISTAKE("Mixing up percentages and rates per 1 000", "Birth and death rates are per 1 000. Natural increase is usually given as a percentage: divide the difference by 10. 27 per 1 000 is 2.7%, not 27%."),
        QUIZ("A country has a CBR of 31 per 1 000 and a CDR of 8 per 1 000. What is its rate of natural increase?", ["23%", "2.3%", "3.9%", "0.23%"], 1,
             "(31 − 8) ÷ 10 = 2.3%.", hint="Subtract, then change per 1 000 into per 100.",
             feedback=["23 per 1 000 is not 23%; divide by 10.", "", "That is 31 ÷ 8, a ratio, not a rate.", "That divides by 100 instead of 10."]),
        QUIZ("In which stage of the DTM is the gap between birth and death rates usually widest?", ["Stage 1", "Stage 2", "Stage 4", "Stage 5"], 1,
             "In stage 2 the death rate falls fast while the birth rate stays high, so natural increase is greatest (late stage 2 to early stage 3).",
             hint="Which stage has a falling death rate and a high birth rate?",
             feedback=["Both rates are high and close in stage 1.", "", "Both rates are low and close in stage 4.", "In stage 5 the birth rate is below the death rate."]),
        TIP("Rates and the DTM appear in Paper 1 (calculations, matching stages to data) and in Paper 2 questions on population change and its significance. Draw and label the DTM when it helps, and always use a named country in each stage.", title="Exam link"),
        PQ("A town of 80 000 people records 2 960 births and 720 deaths in one year. Calculate (a) the CBR, (b) the CDR, (c) the natural increase in %, and (d) the approximate doubling time.",
           "(a) 2 960 ÷ 80 000 × 1 000 = 37 per 1 000. (b) 720 ÷ 80 000 × 1 000 = 9 per 1 000. (c) (37 − 9) ÷ 10 = 2.8%. (d) 70 ÷ 2.8 = 25 years (assuming no migration)."),
        PQ("Discuss three ways in which the demographic transition model is significant to a developing country.",
           "Model plan. Introduction: define the DTM briefly. Point 1, prediction: by placing the country in a stage (Cameroon: late stage 2 or stage 3), planners can expect continued growth and a youthful structure. Point 2, planning: it shows future needs, such as schools, health care and jobs for young people now, and pensions later. Point 3, policy: it suggests that lowering infant mortality and educating girls helps move the country into stage 3, so it supports family planning and education policies. Evaluation: the model is based on Europe, ignores migration and gives no time scale, so it is a guide rather than a forecast. Conclusion."),
        PQ("Explain why death rates fell faster in many developing countries in the twentieth century than they did in nineteenth-century Europe.",
           "Developing countries could import medical knowledge and technology already invented elsewhere: vaccines, antibiotics, insecticides against malaria mosquitoes, oral rehydration therapy. International programmes spread them quickly. In Europe these improvements had to be invented and spread slowly over a century. So death rates in developing countries fell in decades while birth rates stayed high, giving very rapid growth."),
        SUM("CBR and CDR are per 1 000; natural increase (%) = (CBR − CDR) ÷ 10; doubling time ≈ 70 ÷ growth rate.",
            "GFR and TFR measure fertility better than CBR; IMR is a sensitive indicator of health and development; replacement level is a TFR of about 2.1.",
            "Fertility depends on the economic value of children, infant mortality, education of women, family planning and norms; mortality on health, water, food and shocks.",
            "The DTM has five stages: high stationary, early expanding, late expanding, low stationary and declining.",
            "Its significance lies in comparison, prediction and planning; its limits include its European base, no migration and no time scale."),
    ],
))

# ------------------------------------------------------------------ 3. Population structure and pyramids
LESSONS.append(lesson(
    module=M_POP,
    topic="Population structure and pyramids",
    title="Population structure: pyramids, dependency, sex ratios and the ageing population",
    slug="gpl3-population-structure-pyramids",
    minutes=24,
    summary="How to read and explain age-sex pyramids, calculate youth, old-age and total dependency ratios and sex ratios, and examine the problems of youthful and ageing populations with measures matched to each problem.",
    objectives=[
        "Describe and explain the shapes of expansive, stationary and constrictive pyramids, including bulges and notches",
        "Calculate total, youth and old-age dependency ratios and the sex ratio, and interpret them",
        "Explain how migration, fertility and mortality shape a population structure",
        "Examine the problems of youthful and ageing populations and propose measures tied to each problem",
    ],
    key_concepts=["Age-sex pyramid", "Expansive pyramid", "Constrictive pyramid", "Dependency ratio", "Sex ratio",
                  "Ageing population", "Youthful population", "Median age"],
    blocks=[
        H("Introduction"),
        T("Two countries can have the same total population and still face opposite problems. One must build schools and create "
          "jobs for millions of young people; the other must pay pensions and care for millions of elderly people with fewer "
          "workers. **Population structure** (the composition of a population by age and sex) explains the difference. Its main "
          "tool is the **age-sex pyramid**."),
        H("Reading an age-sex pyramid"),
        D("An **age-sex pyramid** is a pair of horizontal bar graphs placed back to back: males on the left, females on the right, "
          "with age groups (usually five-year groups) from the youngest at the bottom to the oldest at the top. Bars show the "
          "number or, better for comparison, the percentage of the total population in each group.", title="Age-sex pyramid"),
        IMG("algpl3-pyramids.svg", alt="Two age-sex pyramids. Pyramid A has a very wide base and narrows steadily to a thin top. Pyramid B has a narrow base, is widest in the 40 to 49 age groups, and has a large group of women aged 75 and over",
            caption="Figure 1. Two pyramids drawn from invented data. A: expansive (youthful). B: constrictive (ageing)."),
        KEY("Three basic shapes", "Link each shape to the DTM.", cards=[
            ["Expansive (progressive)", "Wide base, concave sides, narrow top. High birth rate, high but falling death rate, low life expectancy. DTM stage 2 or 3; typical of many sub-Saharan African countries."],
            ["Stationary", "Bars of similar width up to old age, then narrowing. Low birth and death rates. DTM stage 4."],
            ["Constrictive (regressive)", "Base narrower than the middle; many elderly, often more women than men at the top because women live longer. DTM stage 5."],
        ]),
        T("Look also for irregularities. A **bulge** may be a baby boom or an inflow of migrants; a **notch** may be war deaths, an "
          "epidemic, a famine or a period of low births (for example a strict birth control policy). In towns that attract labour, "
          "such as mining or plantation areas, there is often a male bulge at ages 20 to 40. Areas that lose young adults to "
          "migration show a 'waist' in the working ages and relatively many children and old people."),
        H("Dependency and sex ratios"),
        F(r"\text{total dependency ratio} = \frac{\text{(aged 0-14)} + \text{(aged 65 and over)}}{\text{aged 15-64}} \times 100", title="Total dependency ratio"),
        F(r"\text{youth DR} = \frac{\text{aged 0-14}}{\text{aged 15-64}} \times 100 \qquad \text{old-age DR} = \frac{\text{aged 65+}}{\text{aged 15-64}} \times 100", title="Youth and old-age dependency ratios"),
        F(r"\text{sex ratio} = \frac{\text{number of males}}{\text{number of females}} \times 100", title="Sex ratio (males per 100 females)"),
        EX("Worked example 1: comparing dependency", intro="Country P (invented): 42% aged 0-14, 55% aged 15-64, 3% aged 65 and over. Country Q (invented): 15%, 64% and 21%. Calculate the total, youth and old-age dependency ratios.", steps=[
            S("Country P", math=r"\text{total} = \frac{42 + 3}{55} \times 100 \approx 81.8; \quad \text{youth} = \frac{42}{55} \times 100 \approx 76.4; \quad \text{old} = \frac{3}{55} \times 100 \approx 5.5"),
            S("Country Q", math=r"\text{total} = \frac{15 + 21}{64} \times 100 \approx 56.3; \quad \text{youth} = \frac{15}{64} \times 100 \approx 23.4; \quad \text{old} = \frac{21}{64} \times 100 \approx 32.8"),
            S("Interpret", text="P has about 82 dependants for every 100 people of working age, almost all of them children: a youthful population. Q has fewer dependants overall, but one third of its dependency is elderly: an ageing population. The burdens are different in kind, not only in size."),
        ], check=r"76.4 + 5.5 = 81.9 \approx 81.8 \text{ (rounding)}"),
        EX("Worked example 2: a sex ratio", intro="A plantation district has 46 200 males and 38 500 females (invented). Calculate the sex ratio and suggest a reason.", steps=[
            S("Calculate", math=r"\frac{46\,200}{38\,500} \times 100 = 120 \text{ males per } 100 \text{ females}"),
            S("Explain", text="The ratio is well above 100. Plantation and agro-industrial work has long attracted young men from other regions as labour migrants, as in the plantations of the South West region of Cameroon."),
        ]),
        T("A dependency ratio is a rough measure. Not everyone aged 15 to 64 works (students, the unemployed, people in unpaid "
          "work), while many people under 15 and over 65 do work, especially on farms in developing countries. Use it with "
          "care and say so in an essay."),
        H("Youthful and ageing populations"),
        D("An **ageing population** is one in which the proportion of people aged 65 and over (and the median age) is rising, "
          "because fertility is falling and life expectancy is rising. It is not just 'a population with old people'.", title="Ageing population"),
        KEY("Ageing: each problem with its measure", "Tie every solution to a named problem.", cards=[
            ["Rising pension costs", "Raise the retirement age; encourage private and workplace pension savings."],
            ["Shrinking workforce and tax base", "Admit young immigrant workers; bring more women and older people into work; invest in automation (as Japan has done)."],
            ["Rising health and care costs", "Promote healthy ageing and preventive care; support family and community care."],
            ["Too few births for the future", "Pro-natalist measures: child allowances, paid parental leave, cheap child care (as in France)."],
        ]),
        KEY("Youthful: each problem with its measure", "Typical of Cameroon and many African countries.", cards=[
            ["Pressure on schools and health care", "Invest in primary and secondary schools, vaccination and mother-and-child clinics."],
            ["Too few jobs for young adults", "Vocational training, support for small businesses and agriculture, labour-intensive public works."],
            ["Continued rapid growth (momentum)", "Education of girls and access to family planning lower fertility over time."],
        ]),
        MISTAKE("Bald definitions and lists of problems only", "The Board's 2023 report noted weak definitions of 'ageing population' and answers that listed problems when solutions were asked for, or solutions without the problem. Define precisely, then write 'problem: ... measure: ... how it helps: ...'."),
        MISTAKE("Reading numbers when the pyramid shows percentages", "Check the axis. A percentage pyramid lets you compare countries of different sizes, but you cannot read the number of people from it."),
        QUIZ("A country has 30% aged 0-14, 60% aged 15-64 and 10% aged 65 and over. What is its total dependency ratio?", ["40.0", "66.7", "50.0", "150.0"], 1,
             "(30 + 10) ÷ 60 × 100 = 66.7.", hint="Add the two dependent groups, divide by the working-age group.",
             feedback=["That is 30 + 10, not divided by 60.", "", "That is 30 ÷ 60 × 100, the youth ratio only.", "That is 60 ÷ 40 × 100, the inverse."]),
        QUIZ("A pyramid for a town shows a large bulge of males aged 20 to 39. What is the most likely cause?", ["A baby boom twenty years ago", "Male labour in-migration to work in the town", "High female life expectancy", "A high infant mortality rate"], 1,
             "A bulge confined to young adult males usually means labour migrants.", hint="Which process adds young men only?",
             feedback=["A baby boom adds both sexes, not mainly males.", "", "That would widen the female side at old ages.", "That would narrow the base, not widen young adult male bars."]),
        TIP("Population structure appears in Paper 1 (reading pyramids, dependency calculations) and Paper 2 (problems and solutions for youthful or ageing populations). In Paper 3, you may be asked to draw a pyramid from data: title it, label both axes and the sexes, and use a consistent scale.", title="Exam link"),
        PQ("Using Figure 1, compare the structures of pyramids A and B.",
           "A has a very wide base (about 8% of the population in each sex at 0-4) that narrows steadily, so most of the population is young and few people reach old age: high birth rate, high death rate at older ages, low life expectancy. B has a narrow base (about 2% each sex at 0-4), is widest in the middle-aged groups (40 to 49), and has many elderly people, with more women than men aged 75 and over: low birth rate, long life expectancy, female longevity. A suggests DTM stage 2 or 3; B suggests stage 4 to 5."),
        PQ("A region has 1 200 000 people aged 0-14, 1 500 000 aged 15-64 and 90 000 aged 65 and over. Calculate the total, youth and old-age dependency ratios.",
           "Total = (1 200 000 + 90 000) ÷ 1 500 000 × 100 = 86. Youth = 1 200 000 ÷ 1 500 000 × 100 = 80. Old-age = 90 000 ÷ 1 500 000 × 100 = 6. The population is youthful; nearly all the dependency is of children."),
        PQ("Examine four measures a government could take to solve the problems of an ageing population.",
           "Model plan. Define ageing population precisely. Measure 1: raise the retirement age, which cuts pension costs and keeps experienced workers. Measure 2: managed immigration of young workers, which fills labour shortages and widens the tax base. Measure 3: pro-natalist incentives (allowances, parental leave, child care), which raise births in the long term. Measure 4: pension reform and private saving schemes, which spread the cost. Evaluation: immigration may be politically sensitive; pro-natalist policies work slowly and often weakly; raising the retirement age is unpopular. Conclusion: a combination is needed, tied to each problem."),
        SUM("Age-sex pyramids show population structure; expansive, stationary and constrictive shapes match DTM stages.",
            "Bulges and notches record baby booms, migration, wars, epidemics and policies.",
            "Total dependency ratio = (0-14 + 65+) ÷ (15-64) × 100; split it into youth and old-age ratios.",
            "Sex ratio = males ÷ females × 100; labour migration often creates male-dominated destinations.",
            "Youthful and ageing populations bring different problems; always match each measure to a stated problem."),
    ],
))

# ------------------------------------------------------------------ 4. Population theories and policies
LESSONS.append(lesson(
    module=M_POP,
    topic="Population theories and policies",
    title="Population and resources: Malthus, Boserup and Simon, and population policies",
    slug="gpl3-population-theories-policies",
    minutes=25,
    summary="The pessimistic and optimistic theories of population and resources (Malthus and the neo-Malthusians, Boserup, Simon), how to evaluate them with evidence, and how anti-natalist, pro-natalist and distribution policies work, with their successes and problems.",
    objectives=[
        "Explain Malthus's theory, its preventive and positive checks, and the neo-Malthusian revival",
        "Explain Boserup's theory of agricultural intensification and Simon's view of people as the ultimate resource",
        "Evaluate the theories with evidence from the past two centuries and from Africa",
        "Describe and assess anti-natalist, pro-natalist and population distribution policies",
    ],
    key_concepts=["Malthusian theory", "Positive checks", "Preventive checks", "Neo-Malthusian", "Boserup's theory",
                  "Agricultural intensification", "Cornucopian view", "Anti-natalist policy", "Pro-natalist policy"],
    blocks=[
        H("Introduction"),
        T("Will a growing population run out of food and resources, or will it find new ways to produce more? This question has "
          "divided thinkers for more than two hundred years. At O Level you met Malthus. At A Level you must set him against "
          "Boserup and Simon, judge each with evidence, and connect the theories to the policies governments actually use."),
        H("Malthus and the pessimists"),
        D("Thomas Malthus, in his *Essay on the Principle of Population* (1798), argued that population, if unchecked, grows "
          "**geometrically** (1, 2, 4, 8, 16...), doubling about every 25 years, while food supply grows only **arithmetically** "
          "(1, 2, 3, 4, 5...). Population must therefore outrun food unless it is checked.", title="Malthus's theory"),
        KEY("Malthus's checks", "Two kinds of check keep population within food supply.", cards=[
            ["Preventive checks", "Lower the birth rate: delayed marriage and 'moral restraint' (abstinence)."],
            ["Positive checks", "Raise the death rate: famine, disease, war. They act when preventive checks fail."],
        ]),
        EX("Worked example 1: Malthus's two series", intro="Using Malthus's assumptions, start with population = 1 and food = 1 and let each period be 25 years. Compare population and food after 100 years and after 200 years.", steps=[
            S("Number of periods", text="100 years = 4 periods; 200 years = 8 periods."),
            S("Population (geometric)", math=r"2^4 = 16; \qquad 2^8 = 256"),
            S("Food (arithmetic)", math=r"1 + 4 = 5; \qquad 1 + 8 = 9"),
            S("Ratio", text="After 100 years population is to food as 16 to 5; after 200 years as 256 to 9. Malthus used this kind of comparison to show that growth must be checked."),
        ], check=r"\frac{256}{9} \approx 28"),
        IMG("algpl3-malthus-boserup.svg", alt="Two graphs. A, Malthus: a straight food supply line and a curving population line that crosses it at a crisis point, then falls. B, Boserup: a steadily rising population line and a stepped food supply line that jumps upward with new farming methods",
            caption="Figure 1. Schematic comparison: Malthus (A) and Boserup (B)."),
        T("**Neo-Malthusians** revived these fears in the twentieth century. Paul Ehrlich's *The Population Bomb* (1968) and the "
          "Club of Rome's report *The Limits to Growth* (1972) warned that rising population and consumption would exhaust "
          "resources and damage the environment. Today similar arguments link population growth to deforestation, soil "
          "degradation, water stress and climate change."),
        H("Boserup and the optimists"),
        D("Ester Boserup, in *The Conditions of Agricultural Growth* (1965), argued the reverse of Malthus: population growth "
          "comes first and **causes** farmers to change. As land becomes scarce, they shorten fallow periods and invest more labour "
          "and new techniques in each hectare (terracing, manuring, irrigation, multiple cropping). Food supply rises in steps.", title="Boserup's theory"),
        T("Boserup described a sequence of intensification: forest fallow, bush fallow, short fallow, annual cropping and finally "
          "multi-cropping. Farming geographers measure the intensity with the **R-value** (cultivation frequency), the share of "
          "time a plot is cultivated (an idea associated with Ruthenberg; check your textbook)."),
        F(r"R = \frac{\text{years cultivated}}{\text{years cultivated} + \text{years fallow}} \times 100", title="R-value (cultivation frequency)"),
        EX("Worked example 2: intensification", intro="In a thinly populated forest area a plot is cultivated for 2 years and rested for 10. In a densely populated highland area a plot is cultivated for 3 years and rested for 1. Calculate the R-values and relate them to Boserup.", steps=[
            S("Forest area", math=r"R = \frac{2}{2 + 10} \times 100 \approx 16.7"),
            S("Highland area", math=r"R = \frac{3}{3 + 1} \times 100 = 75"),
            S("Interpret", text="The denser population uses land far more intensively. Boserup would say population pressure pushed farmers to shorter fallows, with more manure, ridging and mixed cropping to keep yields up."),
        ]),
        T("Julian Simon, in *The Ultimate Resource* (1981), went further: people, with their skills and inventions, are the "
          "ultimate resource. Scarcity raises prices, which encourages substitutes, recycling and new technology, so resources "
          "become more available over time. This is often called the **cornucopian** view."),
        H("Evaluating the theories"),
        KEY("Evidence for and against", "Use evidence, not opinion.", cards=[
            ["Against Malthus", "World population has grown about eightfold since 1800, yet food production per person has risen, thanks to new land, fertilizers, high-yield seeds and trade. He underestimated technology and did not foresee falling birth rates."],
            ["For Malthus", "Famines, soil exhaustion and conflict over land still occur locally, especially where technology and capital are scarce; neo-Malthusians point to environmental limits."],
            ["For Boserup", "Densely populated areas often farm most intensively; some studies (for example of Machakos in Kenya) found more people with less erosion. Check your textbook."],
            ["Against Boserup", "Intensification needs time, capital, secure land rights and markets; under fast growth soils may degrade before farmers can adapt. She focused on farming, not on all resources."],
        ]),
        H("Population policies"),
        T("An **anti-natalist** policy tries to lower the birth rate; a **pro-natalist** policy tries to raise it. Governments may "
          "also try to change the **distribution** of population, for example with resettlement or new towns. Cameroon has a "
          "national population policy whose aims include balancing population growth with development; check your textbook "
          "for its date and details."),
        KEY("Examples to know", "Name the country, the measures and the results.", cards=[
            ["China (anti-natalist)", "One-child policy from about 1979-80 to 2015: rewards and penalties. Birth rates fell sharply, but it brought a sex-ratio imbalance and rapid ageing. It moved to a two-child policy (2016) and then three (2021)."],
            ["India (anti-natalist)", "Family planning programmes since the 1950s, including a coercive phase in the 1970s that was widely criticised; fertility has fallen gradually, faster where female literacy is high."],
            ["France (pro-natalist)", "Long-standing family allowances, tax relief for larger families, paid parental leave and cheap child care; fertility has stayed relatively high for Europe."],
            ["Singapore (both)", "'Stop at two' in the 1970s, then from the late 1980s incentives to have more children when fertility fell too low."],
        ]),
        MISTAKE("Describing a theory without evaluating it", "An A Level essay on Malthus or Boserup must weigh evidence on both sides and reach a judgement. A description alone earns only part of the credit."),
        MISTAKE("Getting the direction of cause wrong", "Malthus: food limits population. Boserup: population growth drives food production. Do not write that Boserup thought population would outstrip food."),
        QUIZ("Which statement best summarises Boserup's view?", ["Population growth will always outrun food supply", "Population pressure stimulates farmers to intensify and raise food output", "Population is controlled mainly by famine and disease", "Resources are fixed, so growth must stop"], 1,
             "Boserup saw population growth as the cause of agricultural change.", hint="What comes first in Boserup's chain of cause and effect?",
             feedback=["That is Malthus's conclusion.", "", "Those are Malthus's positive checks.", "That is a neo-Malthusian limits view."]),
        QUIZ("A plot is cultivated for 4 years and left fallow for 4 years. What is its R-value?", ["100", "50", "25", "4"], 1,
             "4 ÷ (4 + 4) × 100 = 50.", hint="Divide years cultivated by the whole cycle length.",
             feedback=["That would mean no fallow at all.", "", "That is 4 ÷ 16 × 100, counting the cycle twice.", "That is just the number of years cultivated."]),
        TIP("Theories and policies appear in Paper 1 (who said what, checks, policy types) and in Paper 2 essays ('Assess the relevance of Malthus's theory today', 'Discuss the success of population policies'). Name the theorist and date, give evidence, and conclude.", title="Exam link"),
        PQ("Distinguish between Malthus's preventive checks and positive checks, giving one example of each.",
           "Preventive checks reduce the birth rate before population outgrows food, for example delayed marriage or moral restraint. Positive checks raise the death rate once population has outgrown food, for example famine, disease or war."),
        PQ("'Malthus was wrong.' Discuss with reference to evidence.",
           "Model plan. Introduction: summarise Malthus (geometric v arithmetic growth, checks). For the statement: global food output has grown faster than population since 1800 (new land, fertilizers, Green Revolution, trade); birth rates fell voluntarily as countries developed (DTM), which Malthus did not foresee; Boserup and Simon show that population can stimulate innovation. Against the statement: local famines and land conflicts, soil degradation and water shortages in fast-growing poor regions; neo-Malthusian concerns about climate and biodiversity; growth in food output relies on fossil energy and may not be sustainable. Conclusion: wrong as a universal law but still a useful warning where technology and capital are scarce."),
        PQ("Assess the success of China's one-child policy.",
           "Successes: fertility and the birth rate fell sharply; hundreds of millions fewer births than would otherwise have occurred (estimates vary; check your textbook); more resources per child for education and health; contribution to rapid economic growth. Problems: a high sex ratio at birth, rapid ageing and a shrinking workforce, the '4-2-1' family structure, strong criticism of coercive enforcement; fertility was already falling before 1979, so not all the fall was due to the policy. The policy was relaxed in 2016 and 2021. Conclusion: effective in lowering births, but with serious social and demographic costs."),
        SUM("Malthus (1798): population grows geometrically, food arithmetically; preventive and positive checks restore balance.",
            "Neo-Malthusians (Ehrlich, Club of Rome) stress environmental and resource limits.",
            "Boserup (1965): population pressure drives agricultural intensification; R-value measures cultivation frequency.",
            "Simon (1981): people are the ultimate resource; scarcity drives innovation (cornucopian view).",
            "Anti-natalist (China, India) and pro-natalist (France, Singapore) policies have mixed results; always evaluate."),
    ],
))

# ------------------------------------------------------------------ 5. Migration
LESSONS.append(lesson(
    module=M_POP,
    topic="Migration",
    title="Migration: types, selectivity and the models of Ravenstein, Lee and Todaro",
    slug="gpl3-migration-models",
    minutes=25,
    summary="Types and measures of internal and international migration, why migration is selective by age and sex, the models of Ravenstein, Lee and Todaro with their strengths and limits, and the consequences of migration for origins and destinations, with Cameroon's rural exodus as the case study.",
    objectives=[
        "Classify migration and calculate net migration and its contribution to population change",
        "Explain how and why migration is selective by age and sex",
        "Apply and evaluate Ravenstein's laws, Lee's push-pull model and Todaro's expected-income model",
        "Assess the consequences of migration for areas of origin and destination and the measures to manage rural exodus",
    ],
    key_concepts=["Migration", "Net migration", "Step migration", "Migration selectivity", "Ravenstein's laws",
                  "Intervening obstacles", "Expected income", "Remittances", "Rural exodus"],
    blocks=[
        H("Introduction"),
        T("Every week young people from villages of the North West, the West and the Far North arrive in Douala and Yaoundé "
          "looking for work, schooling or trade. Others leave Cameroon for Nigeria, Gabon, Europe or North America. Migration "
          "is the third component of population change, and in many towns it matters more than births and deaths. A Level "
          "asks you to explain it with models and to judge those models."),
        H("Definitions and types"),
        D("**Migration** is a permanent or semi-permanent change of usual residence, normally across an administrative boundary "
          "(many statistical services use a stay of a year or more). Daily commuting and short seasonal movements are "
          "**circulation**, not migration.", title="Migration"),
        KEY("Ways to classify migration", "An essay should use precise types.", cards=[
            ["By distance and boundary", "Internal (within a country) or international (across a border)."],
            ["By direction", "Rural-urban, urban-urban, rural-rural, urban-rural (counter-urbanization)."],
            ["By decision", "Voluntary (economic, family, education) or forced (refugees fleeing conflict or persecution; people displaced by disasters or projects)."],
            ["By pattern", "Step migration (village, small town, city), chain migration (following relatives), return migration, seasonal labour migration."],
        ]),
        F(r"\text{population change} = (\text{births} - \text{deaths}) + (\text{in-migrants} - \text{out-migrants})", title="Components of change"),
        EX("Worked example 1: the role of migration in a town", intro="A town (invented data) has 200 000 people at the start of a year. During the year there are 7 000 births, 1 800 deaths, 12 000 in-migrants and 5 000 out-migrants. Calculate natural increase, net migration, total change and the share of growth due to migration.", steps=[
            S("Natural increase", math=r"7\,000 - 1\,800 = 5\,200"),
            S("Net migration", math=r"12\,000 - 5\,000 = +7\,000"),
            S("Total change", math=r"5\,200 + 7\,000 = 12\,200 \;\Rightarrow\; \frac{12\,200}{200\,000} \times 100 = 6.1\%"),
            S("Share due to migration", math=r"\frac{7\,000}{12\,200} \times 100 \approx 57\%", text="Net in-migration contributes more than natural increase: typical of a fast-growing African city."),
        ]),
        H("Migration is selective"),
        KEY("How and why migration is sex-selective", "Migrants are not a random sample of the population. They are mostly young adults (about 15 to 35), who have the "
            "most to gain and the fewest ties. Migration is also selective by education, marital status and occupation, and above all by sex. Learn the two patterns of sex selectivity and the reasons for each.", cards=[
            ["Pattern 1: male-dominated", "Long-distance and international labour migration has often been dominated by men: to plantations, mines, building sites and distant cities. Why: jobs demanding heavy labour, men expected to earn cash for the family, fewer social restrictions on men travelling alone, and the cost and risk of long journeys."],
            ["Pattern 2: female-dominated", "Short-distance moves are often dominated by women: marriage migration (in many societies the wife moves to the husband's home), domestic work, petty trade and services in nearby towns. In Latin America and parts of Asia, rural-urban streams are often female-dominated because of jobs in domestic service and factories."],
            ["Change over time", "Female migration is rising in Africa as girls' education, urban service jobs and independent trading grow."],
        ]),
        H("Ravenstein's laws"),
        T("E. G. Ravenstein (1885 and 1889) studied British census data and proposed 'laws of migration'. The main ones: most "
          "migrants move only short distances; long-distance migrants go mainly to great centres of commerce and industry; "
          "migration proceeds **step by step**; each main current produces a **counter-current**; town dwellers migrate less than "
          "rural people; women are more migratory over short distances and men over long distances; most migrants are adults; "
          "and economic motives dominate. "
          "Strengths: many laws still hold (distance decay, step migration, economic motives, age selectivity). Limits: they come "
          "from nineteenth-century Britain; cheap transport and phones reduce distance decay; forced migration and international "
          "flows are poorly covered; and they describe patterns rather than explain individual decisions."),
        H("Lee's push-pull model"),
        IMG("algpl3-lee-model.svg", alt="Lee's model: an origin circle and a destination circle, each containing plus, minus and zero signs, separated by three bars labelled intervening obstacles, with an arrow labelled migration from origin to destination",
            caption="Figure 1. Lee's model of migration (1966): factors at origin and destination, intervening obstacles and personal factors."),
        T("Everett Lee (1966) argued that every place has positive factors (+) that hold or attract people, negative factors (−) "
          "that repel them, and neutral factors (0). Between origin and destination lie **intervening obstacles**: distance, cost, "
          "borders and laws, lack of information. **Personal factors** (age, education, family, personality) decide how each "
          "person judges these. Migration happens when the perceived advantages outweigh the obstacles. "
          "Lee's model is flexible and includes perception, but it is descriptive, hard to test with numbers, and it treats "
          "migrants as free choosers, so it fits forced migration poorly."),
        H("Todaro's expected-income model"),
        D("Michael Todaro (1969) argued that rural people move to town in response to the **expected** urban income, not the "
          "actual wage. The expected income is the urban wage multiplied by the probability of getting a modern-sector job. "
          "People keep migrating while expected urban income exceeds rural income, even when urban unemployment is high.", title="Todaro's model",
          formula=r"\text{expected urban income} = \text{urban wage} \times \text{probability of employment}"),
        EX("Worked example 2: will Paul migrate?", intro="Paul earns FCFA 35 000 a month from farming (invented figures). A formal job in the city pays FCFA 100 000 a month, but only 45% of city job-seekers get such a job. Use Todaro's model. Then repeat for a rural income of FCFA 50 000.", steps=[
            S("Expected urban income", math=r"100\,000 \times 0.45 = 45\,000 \text{ FCFA}"),
            S("Compare (rural FCFA 35 000)", text="45 000 is more than 35 000, so the model predicts Paul migrates, even though he has a 55% chance of not finding a formal job."),
            S("Compare (rural FCFA 50 000)", text="45 000 is less than 50 000, so the model predicts he stays: raising rural incomes reduces migration."),
        ]),
        T("Todaro's model explains why cities with high unemployment keep attracting migrants, and why creating urban jobs can "
          "attract even more migrants. Its policy message is to raise rural incomes and services. Limits: it is purely economic; "
          "it ignores the informal sector, family strategies (sending one member to town to spread risk) and non-economic motives "
          "such as schooling and bright lights."),
        H("Consequences and management"),
        KEY("Effects of rural-urban migration", "Give both positive and negative effects.", cards=[
            ["Areas of origin", "Remittances fund school fees, houses and farm inputs; less pressure on land. But loss of young workers, ageing villages, farm labour shortages and a 'brain drain'."],
            ["Areas of destination", "Labour for industry and services; growth of markets. But pressure on housing, water, transport and jobs; informal settlements and a large informal sector."],
        ]),
        T("Measures to slow the rural exodus in Cameroon have included support for farming (inputs, credit, cooperatives), rural "
          "roads, electrification and water supply, rural schools and health centres, and decentralisation to strengthen regional "
          "towns. In an exam, give concrete examples and separate measures actually taken from measures you propose; check "
          "names and dates of programmes in your textbook."),
        MISTAKE("Explaining 'why' but not 'how' migration is sex-selective", "The Board's 2023 report noted that candidates explained the reasons but did not show how: state the two patterns (male-dominated long-distance, female-dominated short-distance) before giving reasons."),
        MISTAKE("Confusing sex selectivity with other selectivity", "When a question asks about sex, do not drift into age, marital status or occupation selectivity; each must be treated separately."),
        QUIZ("A city wage is FCFA 120 000 a month and the chance of a formal job is 0.3. Rural income is FCFA 40 000. What does Todaro's model predict?", [
            "No migration, because 70% of migrants will be unemployed",
            "Migration, because the expected urban income of FCFA 36 000 exceeds rural income",
            "Migration, because the expected urban income of FCFA 36 000 is less than rural income",
            "No migration, because the expected urban income of FCFA 36 000 is less than rural income"], 3,
            "120 000 × 0.3 = 36 000, which is below 40 000, so the model predicts no migration.",
            hint="Multiply the wage by the probability, then compare with rural income.",
            feedback=["The decision depends on comparing expected income with rural income, not on the unemployment rate alone.", "36 000 does not exceed 40 000.", "If expected urban income is lower, the model predicts staying, not migrating.", ""]),
        QUIZ("Which idea comes from Lee rather than Ravenstein?", ["Most migrants move short distances", "Each current produces a counter-current", "Intervening obstacles between origin and destination", "Migration proceeds step by step"], 2,
             "Intervening obstacles are central to Lee's 1966 model.", hint="Which idea concerns what lies between two places?",
             feedback=["That is one of Ravenstein's laws.", "That is one of Ravenstein's laws.", "", "That is one of Ravenstein's laws."]),
        TIP("Migration appears in Paper 1 (types, laws, model terms), Paper 2 (selectivity, causes and consequences, evaluation of models) and Paper 3 Cameroon questions (rural exodus and its management). Use Cameroonian flows as examples.", title="Exam link"),
        PQ("A city of 1 500 000 gains 60 000 in-migrants and loses 15 000 out-migrants in a year. Births are 54 000 and deaths 13 500. Calculate (a) net migration, (b) natural increase, (c) total growth rate in %.",
           "(a) 60 000 − 15 000 = 45 000. (b) 54 000 − 13 500 = 40 500. (c) (45 000 + 40 500) ÷ 1 500 000 × 100 = 85 500 ÷ 1 500 000 × 100 = 5.7%."),
        PQ("Briefly explain how and why migration is sex-selective.",
           "How: two patterns. Long-distance and international labour migration is often male-dominated, while short-distance migration is often female-dominated (Ravenstein noted this). Why: men have traditionally sought cash wages in heavy jobs far away (plantations, mines, construction) and face fewer restrictions on travelling alone; women move at marriage to the husband's home and to nearby towns for domestic work, trade and services. In some regions (Latin America) rural-urban migration is female-dominated because of demand for domestic and factory workers."),
        PQ("Evaluate Todaro's model as an explanation of rural-urban migration in Cameroon.",
           "Model plan. Explain the model: expected income = wage × probability of employment; migration continues while expected urban income exceeds rural income. Strengths: explains continued migration to Douala and Yaoundé despite high unemployment; supports rural development policies; can be tested with data. Limits: ignores the informal sector, where most migrants actually work; ignores family strategies and remittances; ignores non-economic motives (education, services, escape from insecurity); assumes good information. Conclusion: a useful economic core, but must be combined with Lee's broader push-pull factors."),
        SUM("Migration is a permanent or semi-permanent change of residence; classify it by distance, direction, decision and pattern.",
            "Population change = natural increase + net migration; in growing African cities migration often adds more than births.",
            "Migrants are mainly young adults; sex selectivity shows male-dominated long-distance and female-dominated short-distance patterns.",
            "Ravenstein described laws; Lee added origin and destination factors, intervening obstacles and personal factors; Todaro used expected income.",
            "Migration brings remittances and labour but also rural ageing and urban pressure; management combines rural development with urban planning."),
    ],
))

# ------------------------------------------------------------------ 6. Rural settlement
LESSONS.append(lesson(
    module=M_SET,
    topic="Rural settlement",
    title="Rural settlement: site, pattern, nearest neighbour analysis and the rural-urban fringe",
    slug="gpl3-rural-settlement",
    minutes=25,
    summary="The factors that decided the sites of early rural settlements, why rural settlement is nucleated, dispersed or linear, how to measure pattern with the nearest neighbour index, and the land-use conflicts of the rural-urban fringe, with Cameroonian examples.",
    objectives=[
        "Distinguish site and situation and explain the physical and human factors behind the sites of early rural settlements",
        "Explain nucleated, dispersed and linear patterns and the forces that change them",
        "Calculate and interpret the nearest neighbour index",
        "Describe the rural-urban fringe and evaluate ways of managing its conflicts",
    ],
    key_concepts=["Site", "Situation", "Wet-point site", "Dry-point site", "Nucleated settlement", "Dispersed settlement",
                  "Linear settlement", "Nearest neighbour index", "Rural-urban fringe"],
    blocks=[
        H("Introduction"),
        T("Before modern roads, piped water and police, a family choosing where to build had to think about water, safety, "
          "food and flooding. Their choices still show on topographic maps: villages on spring lines, on hilltops, on river "
          "terraces and along roads. This lesson explains those choices, the patterns they create, and how to measure a pattern "
          "objectively."),
        H("Site and situation"),
        D("The **site** is the actual land a settlement is built on: its relief, soil, drainage and water supply. The **situation** "
          "is its position relative to the surrounding area: routes, rivers, resources and other settlements. Site explains why a "
          "settlement began; situation usually explains why it grew.", title="Site and situation"),
        KEY("Factors influencing the site of early rural settlements", "Explain how each factor attracted settlers.", cards=[
            ["Water supply", "A **wet-point site** is near a reliable spring, well or river in a dry area (a spring line at the foot of a scarp). A **dry-point site** is raised, flood-free ground in a marshy or flood-prone area (a river terrace, a levee, a low hill)."],
            ["Defence", "Hilltops, steep slopes, river meanders and islands protected people from raids. In the Mandara Mountains of northern Cameroon, hill sites gave refuge in the past."],
            ["Relief and soils", "Gentle, well-drained slopes for building; fertile soils for farming (volcanic soils of the Western Highlands; alluvium of river valleys)."],
            ["Resources", "Building materials (stone, timber, clay, thatch grass), firewood, grazing, fishing grounds (Lake Chad and coastal fishing villages)."],
            ["Communication", "Bridging points, fords, confluences, gaps through hills and later road junctions attracted traders."],
        ]),
        H("Settlement patterns"),
        IMG("algpl3-settlement-patterns.svg", alt="Three schematic panels: nucleated houses clustered around a crossroads and well; dispersed houses spread evenly and far apart; linear houses strung along both sides of a road",
            caption="Figure 1. Nucleated, dispersed and linear rural settlement patterns (schematic)."),
        KEY("Causes of each pattern", "Link each pattern to a cause and an example.", cards=[
            ["Nucleated", "Houses clustered together: scarce water points, need for defence, communal farming or herding, social and religious ties, a market or chief's palace at the centre."],
            ["Dispersed", "Houses scattered over the land: water available everywhere, each family living on its own farm, security, abundant land. The scattered compounds of the Western Highlands (Bamileke and Grassfields areas) are a classic example."],
            ["Linear (ribbon)", "Houses strung along a road, river, valley floor or coast, to use access or a narrow strip of good land. In the southern forest zone many villages lie along roads; check your textbook for the history of village regrouping there."],
        ]),
        H("Measuring pattern: the nearest neighbour index"),
        T("Describing a pattern by eye is subjective. The **nearest neighbour index** (Rn), adapted from ecology for settlement "
          "studies, gives a number. For each settlement, measure the straight-line distance to its nearest neighbour, then find "
          "the mean of these distances."),
        F(r"R_n = 2\bar{d}\sqrt{\frac{n}{A}}", title="Nearest neighbour index"),
        T(r"Here $\bar{d}$ is the mean nearest neighbour distance (km), $n$ the number of settlements and $A$ the area (km²). "
          r"$R_n = 0$ means all settlements are clustered at one point; $R_n = 1$ means a random pattern; $R_n = 2.15$ is a perfectly "
          r"regular (uniform, hexagonal) pattern."),
        EX("Worked example 1: a dispersed pattern?", intro="On a map extract of 100 km², 20 rural settlements have a mean nearest neighbour distance of 1.6 km (invented data). Calculate Rn and interpret it.", steps=[
            S("Density term", math=r"\sqrt{\frac{20}{100}} = \sqrt{0.2} \approx 0.447"),
            S("Rn", math=r"R_n = 2 \times 1.6 \times 0.447 \approx 1.43"),
            S("Interpret", text="1.43 lies between random (1) and regular (2.15): the settlements tend towards an even spacing, as expected where each family lives on its own land and water is widely available."),
        ], check=r"2 \times 1.6 \times \sqrt{0.2} = 1.431"),
        EX("Worked example 2: a clustered pattern?", intro="Another extract of 150 km² has 30 settlements with a mean nearest neighbour distance of 0.9 km. Calculate Rn and interpret it.", steps=[
            S("Density term", math=r"\sqrt{\frac{30}{150}} = \sqrt{0.2} \approx 0.447"),
            S("Rn", math=r"R_n = 2 \times 0.9 \times 0.447 \approx 0.80"),
            S("Interpret", text="0.80 lies between clustered (0) and random (1), closer to random: settlements show some clustering, perhaps along a river valley or around water points."),
        ]),
        T("Limits of Rn: the result depends on the size and boundary of the study area; it treats a hamlet and a village alike; "
          "it uses straight-line distance, not travel distance; and it describes a pattern without explaining it. Always add a "
          "reason drawn from the map or the field."),
        H("The rural-urban fringe"),
        D("The **rural-urban fringe** is the transition zone at the edge of a built-up area where urban and rural land uses "
          "mix and compete. It is changing fast, especially around growing cities.", title="Rural-urban fringe"),
        T("Typical land uses include new housing estates and informal building, factories and warehouses that need cheap land, "
          "market gardens and poultry farms supplying the city, quarries, waste dumps, sewage works, airports and leisure uses. "
          "Around Douala and Yaoundé, the fringe pushes into farmland and forest; land prices rise, customary land is sold, and "
          "farmers may lose land. In developed countries, governments use planning controls such as **green belts** (around London "
          "since the mid-twentieth century) to limit urban sprawl, while villages within commuting distance become dormitory "
          "(commuter) villages."),
        MISTAKE("Mixing up site and situation", "Site is the ground under the settlement; situation is its position in the wider area. 'Near a spring on a gentle slope' is site; 'at the junction of two roads 10 km from a market town' is situation."),
        MISTAKE("Reporting Rn without interpreting it", "A number alone earns little credit. Say where it lies on the 0, 1, 2.15 scale and suggest a geographical reason for the pattern."),
        QUIZ("A village is built on a low gravel terrace that stays dry when the surrounding floodplain floods. What kind of site is this?", ["Wet-point site", "Dry-point site", "Gap site", "Defensive meander site"], 1,
             "A dry-point site is raised, flood-free land in a wet or flood-prone area.", hint="Is the settlement looking for water or escaping it?",
             feedback=["A wet-point site is chosen for access to water in a dry area.", "", "A gap site lies in a pass through hills.", "A meander site uses a loop of a river for defence."]),
        QUIZ("A study area gives Rn = 2.05. How should the pattern be described?", ["Highly clustered", "Random", "Close to perfectly regular", "Impossible: Rn cannot exceed 2"], 2,
             "2.05 is near the maximum of 2.15, so the settlements are almost evenly spaced.", hint="Recall the values 0, 1 and 2.15.",
             feedback=["Clustered patterns are near 0.", "Random patterns are near 1.", "", "The maximum is 2.15, not 2."]),
        TIP("Rural settlement appears in Paper 1 (site types, patterns, Rn values), Paper 2 (factors influencing the site of early settlements; patterns) and Paper 3 map work (describe and explain the distribution of settlements using map evidence). The Board's 2023 report found the site question well answered; keep naming examples.", title="Exam link"),
        PQ("Calculate Rn for 12 settlements in an area of 48 km² with a mean nearest neighbour distance of 1.2 km, and interpret the result.",
           "Rn = 2 × 1.2 × √(12 ÷ 48) = 2.4 × √0.25 = 2.4 × 0.5 = 1.2. The pattern is close to random, with a slight tendency towards regular spacing."),
        PQ("Discuss three factors that influenced the site of early rural settlements.",
           "Model plan. Define site. Factor 1, water supply: wet-point sites at springs and rivers in dry areas (spring-line villages; villages by permanent rivers in the Sudano-Sahelian north); dry-point sites on terraces and levees above floodplains. Factor 2, defence: hilltops, steep slopes and meanders offered safety; Mandara Mountains hill villages. Factor 3, relief and soils: gentle, well-drained slopes and fertile soils (volcanic soils around Mount Cameroon and in the Western Highlands). Evaluation: several factors usually combined; today piped water and roads reduce the importance of the original site factors. Conclusion."),
        PQ("Describe the main land uses of the rural-urban fringe and explain why conflicts arise there.",
           "Land uses: new housing (planned and informal), industry and warehouses, retail and leisure, market gardening and poultry farming, quarries, waste dumps and sewage works, airports and roads. Conflicts arise because land is cheaper than in the city but in demand from many users at once; farmers and customary owners lose land to developers; residents oppose dumps and quarries; sprawl removes farmland and forest; planning controls are often weak, so building happens before services arrive."),
        SUM("Site is the land a settlement is built on; situation is its position relative to its surroundings.",
            "Early sites were chosen for water (wet-point or dry-point), defence, relief, soils, resources and routes.",
            "Patterns are nucleated, dispersed or linear, each with physical, social and historical causes.",
            "Rn = 2 × mean distance × √(n ÷ A): 0 clustered, 1 random, 2.15 regular; always interpret and explain.",
            "The rural-urban fringe is a zone of mixed, competing land uses, managed by planning controls such as green belts."),
    ],
))

# ------------------------------------------------------------------ 7. Urbanization
LESSONS.append(lesson(
    module=M_SET,
    topic="Urbanization",
    title="Urbanization, suburbanization and counter-urbanization: processes, causes and urban problems",
    slug="gpl3-urbanization-processes",
    minutes=25,
    summary="How to measure urbanization, why it is fast in developing countries, how suburbanization, counter-urbanization and re-urbanization differ in developed countries, and how cities manage problems such as traffic congestion and waste disposal.",
    objectives=[
        "Define and calculate the level and rate of urbanization and distinguish urbanization from urban growth",
        "Explain the causes of rapid urbanization in developing countries using the urbanization curve",
        "Distinguish urbanization, suburbanization, counter-urbanization and re-urbanization and explain the causes of suburbanization",
        "Propose and evaluate measures for urban problems, especially traffic congestion and waste disposal",
    ],
    key_concepts=["Urbanization", "Urban growth", "Level of urbanization", "Suburbanization", "Counter-urbanization",
                  "Re-urbanization", "Informal settlement", "Traffic congestion", "Waste disposal"],
    blocks=[
        H("Introduction"),
        T("Around 1960 most Cameroonians lived in villages. Today a majority live in towns, and Douala and Yaoundé have each "
          "grown to well over two million people (check current estimates in your textbook). The world as a whole passed the point of "
          "half its people living in towns in the early twenty-first century. Understanding how towns grow, and how people "
          "later move outwards from them, is central to human geography."),
        H("Measuring urbanization"),
        D("**Urbanization** is the increase in the **proportion** of a country's population living in urban areas. **Urban growth** "
          "is the increase in the **number** of people living in towns (or in the built-up area). A country can have urban growth "
          "without urbanization if the rural population grows just as fast.", title="Urbanization and urban growth"),
        F(r"\text{level of urbanization} = \frac{\text{urban population}}{\text{total population}} \times 100", title="Level of urbanization (%)"),
        EX("Worked example 1: level and rate", intro="A country (invented data) had 9.0 million urban people out of 17.5 million in 2005 and 18.0 million out of 29.0 million in 2025. Calculate the level of urbanization in each year and the average annual urban growth rate.", steps=[
            S("Level in 2005", math=r"\frac{9.0}{17.5} \times 100 \approx 51.4\%"),
            S("Level in 2025", math=r"\frac{18.0}{29.0} \times 100 \approx 62.1\%"),
            S("Urban growth rate", math=r"\left(\frac{18.0}{9.0}\right)^{1/20} - 1 = 2^{0.05} - 1 \approx 0.035 = 3.5\% \text{ a year}", text="The urban population doubled in 20 years, a compound rate of about 3.5% a year."),
        ], check=r"9.0 \times 1.035^{20} \approx 17.9"),
        H("The urbanization curve and its causes"),
        IMG("algpl3-urban-curve.svg", alt="An S-shaped curve of percentage urban against time, divided into an initial stage of slow growth, an acceleration stage of rapid growth and a terminal stage where the curve levels off, with Niger, Cameroon and the UK as examples",
            caption="Figure 1. The urbanization curve (usually credited to Ray Northam). Examples are approximate; check current figures."),
        T("Countries pass through an **initial** stage (mostly rural), an **acceleration** stage (rapid shift to towns as industry "
          "and services grow) and a **terminal** stage (above about 70 to 80% urban, the curve levels off). In developing "
          "countries the acceleration stage is fast because two causes act together: **rural-urban migration** (push factors such as "
          "land shortage and low farm incomes; pull factors such as jobs, schools, hospitals and services) and high **natural "
          "increase** in towns, because migrants are young adults of child-bearing age. Reclassification of growing villages as "
          "towns also adds to the urban total."),
        T("Where cities grow faster than jobs, housing and services, the result is sometimes called **over-urbanization**: large "
          "informal settlements, an expanding informal sector, and pressure on water, sanitation and transport."),
        H("The cycle of urban change in developed countries"),
        KEY("Four processes", "Do not confuse them.", cards=[
            ["Urbanization", "The share of people living in towns rises (Britain in the nineteenth century)."],
            ["Suburbanization", "People, and later shops, offices and factories, move from the inner city to the edge of the built-up area. The city spreads outwards; the urban share need not change."],
            ["Counter-urbanization", "People move out of large cities altogether, to small towns and villages beyond the commuter belt; the urban share may fall."],
            ["Re-urbanization", "People move back into inner-city areas, often after regeneration schemes; gentrification of old housing."],
        ]),
        T("This sequence is often presented as a model of urban development (associated with van den Berg and colleagues; check "
          "your textbook). It fits many cities in Western Europe and North America since 1945, but not every city follows every stage."),
        EX("Worked example 2: why suburbanization increased in developed countries", intro="Plan an answer to: 'Examine two reasons for the increasing rate of suburbanization in developed countries.'", steps=[
            S("Define first", text="Suburbanization is the outward spread of residence and activity from the inner city to the suburbs at the edge of the built-up area. It is not the same as urbanization."),
            S("Reason 1: transport", text="Mass car ownership, motorways and commuter railways let people live far from work and still reach it daily, so families moved to suburban estates."),
            S("Reason 2: housing and environment", text="Rising incomes and cheap mortgages let families buy larger houses with gardens on cheaper land at the edge, escaping inner-city congestion, pollution, noise and old, crowded housing."),
            S("Add depth", text="Jobs and shops followed people: out-of-town retail parks and business parks with cheap land and good road access. Government planning (new estates and new towns) also helped. Conclude that pull factors in the suburbs and push factors in the inner city worked together."),
        ]),
        H("Urban problems and their management"),
        KEY("Traffic congestion", "Problem, causes, measures.", cards=[
            ["Causes", "Rapid growth in vehicles, narrow and poorly maintained roads, few traffic lights, roadside trading, on-street parking, weak public transport."],
            ["Measures", "Road widening, flyovers and ring roads; traffic lights and traffic police; mass transit (buses, bus rapid transit, urban rail); parking control; moving markets off the roadside; staggered working hours."],
        ]),
        KEY("Waste disposal", "Problem, causes, measures.", cards=[
            ["Causes", "Rapid population growth, low collection coverage in informal areas, few sanitary landfills, dumping in drains and streams (which worsens flooding)."],
            ["Measures", "Regular collection (in several Cameroonian cities a private company, HYSACAM, collects waste under contract), sanitary landfills, sorting and recycling, composting organic waste, community clean-up days, fines for illegal dumping and public education."],
        ]),
        MISTAKE("Writing about urbanization when asked about suburbanization", "The Board's 2023 report found that most candidates did not know the concept of suburbanization and wrote about urbanization or rural-urban migration instead. Define suburbanization as outward movement within the urban area, and give its own causes."),
        MISTAKE("Measures not linked to a named problem", "List each problem, then the measure that solves it and how. 'Build roads' alone is weak; 'build a ring road so through-traffic avoids the city centre' is strong."),
        QUIZ("A country's urban population rises from 6 to 8 million while its total population rises from 12 to 16 million. What has happened?", [
            "Urbanization but no urban growth", "Urban growth but no urbanization", "Both urban growth and urbanization", "Counter-urbanization"], 1,
            "The urban share stays at 50% (6/12 and 8/16), but the number of urban people grows by 2 million.",
            hint="Compare the percentage urban in the two years.",
            feedback=["The urban number rose, so there was urban growth; the share did not rise.", "", "The share did not change, so there was no urbanization.", "Counter-urbanization would mean people leaving cities; the urban population rose."]),
        QUIZ("Which statement describes suburbanization?", ["The proportion of a country's people in towns rises", "Families move from the inner city to new estates at the edge of the same city", "People leave the city for remote villages beyond commuting range", "Old inner-city housing is renovated and wealthier people move in"], 1,
             "Suburbanization is outward movement within the urban area.", hint="Where do the people end up: inside or outside the urban area?",
             feedback=["That is urbanization.", "", "That is counter-urbanization.", "That is gentrification, part of re-urbanization."]),
        TIP("Urbanization appears in Paper 1 (definitions, curve, processes), Paper 2 (causes and effects; suburbanization; solutions to urban problems) and Paper 3 (urban land use fieldwork; Cameroon urban problems such as floods). Keep the four processes sharply distinct.", title="Exam link"),
        PQ("A country had 4.2 million urban people out of 14.0 million in 2000 and 8.4 million out of 21.0 million in 2020. Calculate the level of urbanization in each year and comment.",
           "2000: 4.2 ÷ 14.0 × 100 = 30%. 2020: 8.4 ÷ 21.0 × 100 = 40%. Urbanization has taken place (the urban share rose by 10 percentage points), and urban growth was fast: the urban population doubled in 20 years (about 3.5% a year), while the total grew only by half."),
        PQ("Distinguish between suburbanization and counter-urbanization.",
           "Suburbanization: people (and later jobs and shops) move from the inner city to the suburbs at the edge of the same urban area; the built-up area grows outwards; people still commute into the city. Counter-urbanization: people move out of the large city altogether, to small towns and rural areas beyond the commuter belt; this can reduce the urban share. The first enlarges the city; the second moves population down the urban hierarchy."),
        PQ("Discuss two measures to solve traffic congestion and two to solve waste disposal problems in a large city such as Douala.",
           "Traffic: (1) mass transit, such as dedicated bus lanes or a bus rapid transit line, moves many people in fewer vehicles; (2) road improvements and traffic management, such as widening main roads, building flyovers at busy junctions, installing traffic lights and removing roadside trading from carriageways. Waste: (1) regular, wider collection coverage, including informal neighbourhoods, with transfer points and a sanitary landfill instead of open dumps; (2) reduce and recycle: sorting at source, composting organic market waste, recycling plastics, with education and fines for dumping in drains. Evaluation: cost, maintenance and enforcement are the main limits."),
        SUM("Urbanization is a rise in the urban share; urban growth is a rise in urban numbers.",
            "The urbanization curve has initial, acceleration and terminal stages; developing countries urbanize fast through migration and natural increase.",
            "Developed cities show suburbanization, counter-urbanization and re-urbanization; define each precisely.",
            "Suburbanization is driven by transport, incomes, cheap edge land, planning and inner-city push factors.",
            "Traffic congestion and waste disposal need measures matched to their causes, with attention to cost and enforcement."),
    ],
))

# ------------------------------------------------------------------ 8. Urban land-use models
LESSONS.append(lesson(
    module=M_SET,
    topic="Urban land-use models",
    title="Urban land-use models: bid-rent, Burgess, Hoyt, Harris and Ullman, and Mann",
    slug="gpl3-urban-land-use-models",
    minutes=25,
    summary="Why land uses sort themselves inside a city (bid-rent theory), the classic concentric, sector, multiple-nuclei and Mann models, how to evaluate them, and how far they fit cities in developing countries such as Douala and Yaoundé.",
    objectives=[
        "Explain bid-rent theory and use bid-rent curves to find where each land use dominates",
        "Describe the Burgess, Hoyt, Harris and Ullman, and Mann models and the ideas behind each",
        "Evaluate the models: assumptions, strengths and limitations",
        "Apply the models to a city in a developing country and explain the differences",
    ],
    key_concepts=["Bid-rent theory", "Peak land value intersection", "Concentric zone model", "Sector model",
                  "Multiple nuclei model", "Mann model", "Invasion and succession", "Informal settlement"],
    blocks=[
        H("Introduction"),
        T("Walk from the banks and offices of a city centre to its outer edge and the land uses change: shops and offices, then "
          "warehouses and old housing, then newer estates, then farmland. Is there an order behind this? Geographers since the 1920s "
          "have built **models**, simplified pictures of reality, to explain urban land use. A Level essays ask you to describe "
          "them, compare them and judge how well they fit real cities."),
        H("Bid-rent theory"),
        D("**Bid-rent theory** (developed by William Alonso in the 1960s) says that land users compete for the most accessible "
          "land, at the centre, and that each user is willing to pay less rent the further it is from the centre. The user that "
          "bids highest at a given distance occupies that land. The most accessible and expensive point is the **peak land value "
          "intersection (PLVI)** in the central business district (CBD).", title="Bid-rent theory"),
        EX("Worked example 1: bid-rent curves", intro="Rents (invented units per m² per year) at distance d km from the PLVI are: retail 1 000 − 200d, industry 600 − 80d, housing 400 − 40d. Find where each land use dominates.", steps=[
            S("Retail meets industry", math=r"1\,000 - 200d = 600 - 80d \;\Rightarrow\; 400 = 120d \;\Rightarrow\; d \approx 3.3 \text{ km}"),
            S("Industry meets housing", math=r"600 - 80d = 400 - 40d \;\Rightarrow\; 200 = 40d \;\Rightarrow\; d = 5 \text{ km}"),
            S("Housing reaches zero", math=r"400 - 40d = 0 \;\Rightarrow\; d = 10 \text{ km}"),
            S("Result", text="Retail dominates from 0 to about 3.3 km, industry from 3.3 to 5 km, housing from 5 to 10 km. Rings of land use appear: bid-rent theory explains concentric zones."),
        ], check=r"1\,000 - 200(3.33) \approx 600 - 80(3.33) \approx 333"),
        H("The concentric zone model (Burgess)"),
        IMG("algpl3-urban-models.svg", alt="Two urban models. A: five concentric rings around a central business district. B: the same CBD with wedge-shaped sectors radiating outward, including a light industry sector, low-class housing on both sides of it, middle-class sectors and a high-class sector opposite the industry",
            caption="Figure 1. Burgess's concentric zones (A) and Hoyt's sectors (B). 1 CBD; 2 transition zone or light industry; 3 low-class housing; 4 middle-class housing; 5 high-class housing (commuter zone in Burgess)."),
        T("E. W. Burgess (1925) based his model on Chicago. The city grows outward from the CBD in rings: the CBD; a **zone in "
          "transition** of old housing, small factories and recent immigrants; working-class housing; better middle-class "
          "housing; and an outer commuter zone. As the city grows, each group moves outward into the next zone, a process he "
          "called **invasion and succession**. Wealth and housing quality rise with distance from the centre."),
        H("The sector model (Hoyt)"),
        T("Homer Hoyt (1939) studied rents in many American cities and found that land uses form **sectors** (wedges) along "
          "transport routes rather than rings. Industry follows railways, rivers or main roads outward; low-class housing grows "
          "beside it; high-class housing grows along the most attractive routes, on higher ground or away from industry, and "
          "keeps extending outward in that direction."),
        H("The multiple nuclei model (Harris and Ullman)"),
        IMG("algpl3-multiple-nuclei.svg", alt="A square city divided into irregular cells numbered 1 to 9: a central CBD, light industry next to it, low, middle and high class housing areas, heavy industry, an outlying business district, a residential suburb and an industrial suburb",
            caption="Figure 2. Harris and Ullman's multiple nuclei model (1945), schematic."),
        T("C. D. Harris and E. L. Ullman (1945) argued that large cities grow around **several nuclei**, not one: the old CBD, a "
          "port or industrial district, a university, an outlying business district or suburban shopping centre. Similar "
          "activities cluster (shops), some repel each other (heavy industry and high-class housing), and some cannot afford "
          "central sites."),
        H("The Mann model of a British city"),
        T("Peter Mann (1965) combined Burgess's zones with Hoyt's sectors for British cities. He identified sectors for "
          "middle-class, lower-middle-class, working-class and lower working-class housing with industry. Because the prevailing "
          "winds in Britain are westerly, the middle-class sector lay to the west (upwind of factory smoke) and industry and "
          "working-class housing to the east (downwind). Within each sector the zones (city centre, transition zone, small "
          "terraced houses, post-1918 housing, commuter villages) still appear."),
        H("Evaluating the models"),
        KEY("Strengths and limitations", "Use these in any 'assess' or 'to what extent' question.", cards=[
            ["Strengths", "Simple and easy to test; bid-rent gives an economic explanation; together the models show distance (zones), direction (sectors) and multiple centres (nuclei); still useful for describing many Western cities."],
            ["Shared limitations", "Based on early twentieth-century North American or British cities; assume flat land and a free land market; ignore government planning, public housing, physical barriers and cultural factors; do not show change over time well (except Burgess's invasion and succession)."],
            ["Developing cities", "Often the wealthy live near the centre and the poor at the edge in informal settlements (the reverse of Burgess); colonial planning created separate administrative and residential quarters; models such as Griffin and Ford's Latin American city (1980) adapt the ideas (check your textbook)."],
        ]),
        EX("Worked example 2: applying the models to Douala", intro="Plan a paragraph: 'To what extent does Douala fit the classic urban models?'", steps=[
            S("Evidence of a CBD", text="Bonanjo (administration, banks, head offices) and Akwa (commerce) form a central business core near the river and port, as all models expect."),
            S("Evidence of sectors", text="Port activity and much industry extend along the Wouri estuary, the railway and main roads (for example the Bassa industrial zone), which recalls Hoyt's sectors along transport routes."),
            S("Evidence of multiple nuclei", text="Large markets and secondary commercial centres in several districts act as extra nuclei, as Harris and Ullman predicted."),
            S("Differences", text="Many low-income informal neighbourhoods lie on flood-prone lowlands and at the urban edge, not in an inner zone; land is shaped by customary ownership and planning decisions, not only by bid-rent. Conclusion: the models help describe parts of Douala but none fits it fully (check local details with your teacher)."),
        ]),
        MISTAKE("Describing a model without evaluating it", "A diagram and description earn part of the marks. Add the assumptions, a real city that fits, a real city that does not, and a judgement."),
        MISTAKE("Muddling the authors", "Burgess: concentric zones (1925). Hoyt: sectors (1939). Harris and Ullman: multiple nuclei (1945). Mann: British city combining zones and sectors (1965)."),
        QUIZ("Which idea explains why industry and low-class housing extend outward together along a railway in Hoyt's model?", ["Peak land value intersection", "Growth in sectors along transport routes", "Invasion and succession in rings", "Several independent nuclei"], 1,
             "Hoyt argued that land uses grow outward in wedges along routes.", hint="Which model uses wedges?",
             feedback=["The PLVI is the most expensive point in the CBD.", "", "Rings are Burgess's idea.", "Nuclei are Harris and Ullman's idea."]),
        QUIZ("Using the bid-rent curves retail 900 − 150d and housing 300 − 30d, at what distance does housing outbid retail?", ["2 km", "5 km", "6 km", "10 km"], 1,
             "900 − 150d = 300 − 30d gives 600 = 120d, so d = 5 km.", hint="Set the two rents equal and solve for d.",
             feedback=["At 2 km retail bids 600 and housing 240; retail still wins.", "", "At 6 km retail bids 0, but housing already outbid it at 5 km.", "That is where housing rent falls to zero."]),
        TIP("Urban models appear in Paper 1 (match the model to the author and diagram) and Paper 2 essays ('Assess the relevance of urban land-use models to cities in developing countries'). Paper 3 fieldwork on urban land use or functional segregation uses the same ideas. Draw neat, labelled diagrams and name a real city.", title="Exam link"),
        PQ("Explain how bid-rent theory produces a concentric pattern of land use.",
           "Accessibility is greatest at the centre, so all users would like central sites. Shops and offices gain most from accessibility (many customers) and can pay the highest rents, so their bid-rent curve is steep and they win the central land. Industry and then housing have flatter curves, paying less in the centre but more than retail further out. Where curves cross, the land use changes. Because rent depends on distance from one centre, the result is rings: CBD, then industry and older housing, then outer housing."),
        PQ("Compare the concentric zone and sector models.",
           "Similarities: both start from a single CBD; both are based on American cities; both show social groups separated by income. Differences: Burgess uses distance (rings), Hoyt uses direction (wedges along routes); Burgess explains change by invasion and succession outward, Hoyt by the outward extension of each sector; Burgess places the wealthy at the edge, Hoyt places them in a sector that may reach close to the centre along an attractive route."),
        PQ("Assess the relevance of the classic urban land-use models to cities in developing countries.",
           "Model plan. Introduction: name the models. Relevance: most cities have a CBD with the highest land values (bid-rent); industry often follows rivers, ports and railways (Hoyt); large cities have several commercial nuclei (Harris and Ullman). Limits: wealthy groups often live near the centre or in planned colonial-era quarters, while the poor live in informal settlements at the edge or on hazardous land (the reverse of Burgess); customary land tenure, government projects and relief (steep slopes, swamps) shape land use; rapid growth outpaces planning. Conclusion: useful as a starting point, but adapted models are needed."),
        SUM("Bid-rent theory: land users compete for accessible central land; where bid-rent curves cross, land use changes.",
            "Burgess (1925): concentric zones and invasion and succession; Hoyt (1939): sectors along transport routes.",
            "Harris and Ullman (1945): several nuclei; Mann (1965): zones within sectors for British cities, middle class upwind to the west.",
            "All models simplify: flat land, free market, Western cities, little planning; evaluate them.",
            "Developing cities, including Douala, often reverse Burgess, with informal settlements at the edge and on hazardous land."),
    ],
))

# ------------------------------------------------------------------ 9. Rank-size rule and primate cities
LESSONS.append(lesson(
    module=M_SET,
    topic="Rank-size rule and primate cities",
    title="The urban hierarchy: the rank-size rule, primate cities and binary patterns",
    slug="gpl3-rank-size-primate-cities",
    minutes=23,
    summary="How to test a country's urban hierarchy against the rank-size rule, measure primacy with two-city and four-city indices, explain why primate and binary patterns develop, and judge their consequences and the policies used to correct them, with Cameroon's Douala-Yaoundé pattern as the case study.",
    objectives=[
        "State the rank-size rule and calculate expected city populations and deviations",
        "Plot and interpret a rank-size graph on logarithmic scales",
        "Define a primate city and calculate two-city and four-city primacy indices",
        "Explain the causes and consequences of primacy and evaluate decentralization policies",
    ],
    key_concepts=["Urban hierarchy", "Rank-size rule", "Primate city", "Primacy index", "Binary (duo-primate) pattern",
                  "Logarithmic scale", "Decentralization", "Growth pole"],
    blocks=[
        H("Introduction"),
        T("Every country has an **urban hierarchy**: one or a few large cities, more medium towns and many small towns. But the "
          "shape of the hierarchy differs. In some countries one giant city dominates everything; in others there is a smooth "
          "ladder of sizes. Cameroon is unusual: two cities of similar size, Douala and Yaoundé, sit at the top. This lesson gives "
          "you the tools to describe and explain such patterns."),
        H("The rank-size rule"),
        D("The **rank-size rule** states that the population of the city ranked n in a country equals the population of the largest "
          "city divided by n. The second city is half the size of the first, the third a third, and so on. It was popularised by "
          "G. K. Zipf (1949), building on earlier work by F. Auerbach (1913).", title="Rank-size rule",
          formula=r"P_n = \frac{P_1}{n}"),
        EX("Worked example 1: expected populations", intro="The largest city of a country has 2 400 000 people. Use the rank-size rule to find the expected populations of the 2nd, 3rd, 4th and 6th cities. The 3rd city actually has 560 000 people: calculate its deviation from the expected value.", steps=[
            S("Expected sizes", math=r"P_2 = \frac{2\,400\,000}{2} = 1\,200\,000; \; P_3 = 800\,000; \; P_4 = 600\,000; \; P_6 = 400\,000"),
            S("Deviation of the 3rd city", math=r"560\,000 - 800\,000 = -240\,000"),
            S("As a percentage", math=r"\frac{-240\,000}{800\,000} \times 100 = -30\%", text="The 3rd city is 30% smaller than the rule predicts."),
        ], check=r"3 \times 800\,000 = 2\,400\,000"),
        T(r"Plotted on **logarithmic scales** (log of rank against log of population), cities that obey the rule lie on a straight "
          r"line with a slope of $-1$. Log scales are used because the data span a huge range, from millions to thousands, and "
          r"because a straight line is easier to judge than a curve."),
        IMG("algpl3-rank-size.svg", alt="Rank-size graph on logarithmic axes: Country R's ten cities lie on a straight line from 2 million at rank 1 to 200 000 at rank 10; Country S's largest city is also 2 million but its second city is only about 420 000, and the rest fall well below the line",
            caption="Figure 1. Rank-size graphs for two invented countries. R follows the rule; S has a primate distribution."),
        H("Primate cities"),
        D("A **primate city** is a city that is much larger than the next city in the country (often more than twice as large) "
          "and dominates its economic, political and cultural life. Mark Jefferson described this as 'the law of the primate city' "
          "(1939). Examples often cited are Bangkok in Thailand, Lima in Peru and Paris in France.", title="Primate city"),
        F(r"\text{two-city index} = \frac{P_1}{P_2} \qquad \text{four-city index} = \frac{P_1}{P_2 + P_3 + P_4}", title="Primacy indices"),
        T("Under the rank-size rule the two-city index is 2 and the four-city index is 1 ÷ (1/2 + 1/3 + 1/4) ≈ 0.92. Values well above "
          "these indicate primacy."),
        EX("Worked example 2: is Country S primate?", intro="Country S (Figure 1, invented data) has cities of 2 000 000, 420 000, 300 000 and 240 000. Calculate both indices and interpret.", steps=[
            S("Two-city index", math=r"\frac{2\,000\,000}{420\,000} \approx 4.8"),
            S("Four-city index", math=r"\frac{2\,000\,000}{420\,000 + 300\,000 + 240\,000} = \frac{2\,000\,000}{960\,000} \approx 2.1"),
            S("Interpret", text="Both values are far above the rank-size expectations (2 and about 0.92). The largest city is nearly five times the second and more than twice the next three combined: a strongly primate pattern."),
        ]),
        H("Binary patterns: the case of Cameroon"),
        T("Some countries have two leading cities of similar size, a **binary** (or duo-primate) pattern, giving a two-city index "
          "close to 1. Cameroon is an example: Douala, the main port and industrial and commercial centre, and Yaoundé, the "
          "political capital and administrative centre, are of broadly similar size, far above the next towns (such as Garoua, "
          "Bamenda, Bafoussam, Maroua and Ngaoundéré). Australia (Sydney and Melbourne) is another often-quoted example. Check "
          "the latest population estimates in your textbook before quoting figures."),
        H("Causes and consequences of primacy"),
        KEY("Why primate cities develop", "Most causes reinforce each other (cumulative causation).", cards=[
            ["Colonial history", "Colonial powers concentrated ports, railways, administration and investment in one city linking the colony to the coloniser."],
            ["Capital plus port", "Where the capital is also the main port and industrial centre, government, trade and industry all reinforce one city."],
            ["Small or centralised economy", "A small country or a highly centralised state cannot support several large centres."],
            ["Cumulative advantage", "Infrastructure, universities, markets and skilled labour attract more firms and migrants, so the gap widens."],
        ]),
        T("Consequences: economies of scale and a strong link to the world economy, but also regional inequality, congested and "
          "over-urbanized capitals, neglected secondary towns and rural areas, and high rural-urban migration. Policies to reduce "
          "primacy include **decentralization** of government services, **growth poles** (investment in selected secondary "
          "towns), better regional infrastructure and new capital cities (Brasília in 1960, Abuja as Nigeria's capital from 1991)."),
        H("Evaluating the rank-size rule"),
        T("The rule is an empirical regularity, not a theory: it describes but does not explain. It fits large, long-urbanized "
          "countries with integrated economies (the USA is the usual example) better than small or recently independent ones. "
          "Results depend on how a city is defined (city proper or metropolitan area) and on the quality of census data. Still, "
          "deviations from the rule are useful: they raise questions about history, politics and regional development."),
        MISTAKE("Calling every capital a primate city", "A primate city must be disproportionately larger than the second city. Yaoundé is the capital of Cameroon, but it is not a primate city because Douala is of similar size."),
        MISTAKE("Plotting on ordinary scales and expecting a straight line", "The rank-size relationship is a straight line only on log-log axes. On ordinary scales it is a steep curve."),
        QUIZ("The largest city of a country has 1 800 000 people. According to the rank-size rule, what is the expected population of the 5th city?", ["360 000", "900 000", "9 000 000", "300 000"], 0,
             "1 800 000 ÷ 5 = 360 000.", hint="Divide the largest population by the rank.",
             feedback=["", "That is the 2nd city.", "That multiplies by 5 instead of dividing.", "That is the 6th city."]),
        QUIZ("A country's three largest cities have 3.0 million, 2.7 million and 0.6 million people. How is its urban hierarchy best described?", ["Strongly primate", "Binary (duo-primate)", "Following the rank-size rule exactly", "Without any hierarchy"], 1,
             "The two-city index is 3.0 ÷ 2.7 ≈ 1.1, and both cities are far larger than the third.", hint="Calculate P1 ÷ P2.",
             feedback=["A primate city is far larger than the second; here the first two are similar.", "", "The rule predicts a 2nd city of 1.5 million and a 3rd of 1.0 million.", "There is a clear hierarchy, with two cities at the top."]),
        TIP("The rank-size rule and primacy appear in Paper 1 (calculations, definitions), Paper 2 (causes and effects of primate cities; urban hierarchy) and Paper 3 (graphs on log scales, statistics, Cameroon's urban system). Show your working and interpret every number.", title="Exam link"),
        PQ("A country's cities ranked 1 to 4 have 3 600 000, 1 000 000, 900 000 and 500 000 people. Calculate (a) the expected populations of cities 2 to 4 under the rank-size rule, (b) the two-city and four-city indices.",
           "(a) 3 600 000 ÷ 2 = 1 800 000; ÷ 3 = 1 200 000; ÷ 4 = 900 000. (b) Two-city index = 3 600 000 ÷ 1 000 000 = 3.6. Four-city index = 3 600 000 ÷ (1 000 000 + 900 000 + 500 000) = 3 600 000 ÷ 2 400 000 = 1.5. Both exceed the rank-size values (2 and 0.92), so the largest city is primate."),
        PQ("Explain why primate cities are common in former colonies.",
           "Colonial administrations concentrated the port, railway terminus, administration, banks and processing industries in one city that linked the colony to the coloniser's economy. After independence this city kept its advantages (infrastructure, skilled labour, markets, government), so it attracted more investment and migrants (cumulative causation), while other towns remained small. Where the capital and main port were the same city, primacy was strongest."),
        PQ("To what extent does Cameroon's urban hierarchy differ from a primate pattern?",
           "Model plan. Define primate city and the rank-size rule. Evidence: Douala and Yaoundé are of broadly similar size, so the two-city index is close to 1, giving a binary pattern rather than primacy. Reasons: functions are split, Douala as port, industrial and commercial centre, Yaoundé as political and administrative capital, and each attracts its own migrants. Similarity to primacy: the two cities together dominate the system and are far larger than regional towns such as Garoua, Bamenda and Bafoussam, so the hierarchy below them is weak. Conclusion: not primate in the strict sense, but a dual concentration with similar consequences for regional inequality."),
        SUM("Rank-size rule: Pn = P1 ÷ n; on log-log axes the cities fall on a straight line of slope −1.",
            "Compare actual and expected sizes and express deviations as percentages.",
            "A primate city is far larger than the second city; two-city index = P1 ÷ P2, four-city index = P1 ÷ (P2 + P3 + P4).",
            "Cameroon has a binary pattern: Douala (port and economy) and Yaoundé (capital) of similar size.",
            "Primacy grows from colonial history, centralisation and cumulative advantage; decentralization, growth poles and new capitals try to reduce it."),
    ],
))

# ------------------------------------------------------------------ 10. Central place theory
LESSONS.append(lesson(
    module=M_SET,
    topic="Central place theory",
    title="Christaller's central place theory: threshold, range, hexagons and the K principles",
    slug="gpl3-central-place-theory",
    minutes=25,
    summary="Christaller's explanation of the size, number and spacing of service centres: threshold and range, low- and high-order goods, hexagonal market areas, the marketing, traffic and administrative principles (K = 3, 4, 7), calculations, evaluation, and periodic markets in Cameroon.",
    objectives=[
        "Define central place, threshold, range, order of goods and sphere of influence",
        "State Christaller's assumptions and explain why market areas are hexagonal",
        "Explain the K = 3, K = 4 and K = 7 principles and calculate the numbers of centres in a hierarchy",
        "Evaluate the theory and apply threshold and range to periodic markets",
    ],
    key_concepts=["Central place", "Threshold", "Range", "Low-order and high-order goods", "Sphere of influence",
                  "Isotropic surface", "Hexagonal market area", "K value", "Periodic market"],
    blocks=[
        H("Introduction"),
        T("Why can you buy bread, soap and phone credit in almost every village, but must travel to a regional town for a "
          "specialist doctor, and to Douala or Yaoundé for a university hospital or an embassy? Walter Christaller, a German "
          "geographer, tried to answer this in 1933 with **central place theory**, using southern Germany as his study area. "
          "His theory explains why settlements form a hierarchy and why centres of the same order are spaced regularly."),
        H("Key terms"),
        D("A **central place** is a settlement that provides goods and services to the people of its surrounding area (its "
          "**complementary region**, hinterland or **sphere of influence**).", title="Central place"),
        D("The **threshold** is the minimum number of customers (or minimum purchasing power) needed to keep a good or service in "
          "business. The **range** is the maximum distance people are willing to travel to obtain it. A service survives only "
          "if enough customers live within its range to reach its threshold.", title="Threshold and range"),
        KEY("Order of goods", "Threshold and range rise together.", cards=[
            ["Low-order goods", "Bought often, cheap, small threshold and short range: bread, kerosene, soap, phone credit. Found in every village and town."],
            ["High-order goods", "Bought rarely, expensive or specialised, large threshold and long range: jewellery, cars, specialist hospitals, universities. Found only in large centres."],
            ["Hierarchy", "A high-order centre provides all lower-order goods as well. There are few high-order centres, far apart, and many low-order centres, close together."],
        ]),
        H("Assumptions and the hexagon"),
        T("Christaller assumed an **isotropic surface**: a flat, uniform plain; population and purchasing power evenly spread; "
          "transport equally easy in all directions with cost proportional to distance; consumers who always buy from the "
          "nearest centre; and suppliers who earn no excess profits. Under these conditions each centre's market area would be a "
          "circle with radius equal to the range. But circles either leave unserved gaps or overlap. **Hexagons** are the "
          "shape closest to a circle that fills a plane with no gaps and no overlaps, so market areas become hexagons."),
        IMG("algpl3-central-place.svg", alt="A pattern of small light green hexagons, each around a small black dot, with larger blue hexagons around bigger blue dots. Each large hexagon has small centres at its six corners",
            caption="Figure 1. Christaller's K = 3 (marketing) arrangement: each higher-order centre lies at the centre of a large hexagon, with lower-order centres at its corners."),
        H("The three principles"),
        KEY("K values", "K is the number of lower-order market areas served by one higher-order centre (counting its own).", cards=[
            ["K = 3: marketing principle", "Lower-order centres sit at the corners of the higher-order hexagon. Each corner centre is shared by three higher-order centres, so a higher-order centre serves its own area plus 6 × 1/3 = 2 others: 3 in all. This gives the most efficient supply of goods (the greatest number of central places)."],
            ["K = 4: traffic principle", "Lower-order centres sit at the midpoints of the hexagon's sides, on straight routes between higher-order centres. Each is shared by two: 1 + 6 × 1/2 = 4. This gives the most efficient transport network."],
            ["K = 7: administrative principle", "The six lower-order centres lie wholly inside the higher-order area so that each falls under one authority: 1 + 6 = 7. This suits administration and control, though some people travel further."],
        ]),
        EX("Worked example 1: counting centres in a K = 3 hierarchy", intro="In a K = 3 system with one top-order centre, how many market areas and how many centres of each order are there for the first four levels?", steps=[
            S("Market areas at each level", math=r"3^0 = 1, \; 3^1 = 3, \; 3^2 = 9, \; 3^3 = 27", text="Each level has three times as many market areas as the level above."),
            S("New centres at each level", math=r"1, \; 3 - 1 = 2, \; 9 - 3 = 6, \; 27 - 9 = 18", text="Every higher-order centre also serves lower-order goods, so subtract the centres already counted."),
            S("Result", text="1 top-order centre, 2 of the second order, 6 of the third and 18 of the fourth: 27 centres in total. In K = 4 the same method gives 1, 3, 12, 48; in K = 7 it gives 1, 6, 42, 294."),
        ], check=r"1 + 2 + 6 + 18 = 27 = 3^3"),
        EX("Worked example 2: is a service viable?", intro="A pharmacy needs a threshold of 6 000 customers. The rural population density around a small town is 50 persons per km² (invented data), and people will travel up to 8 km for medicines. Is the pharmacy viable? What is the smallest range that would just reach the threshold?", steps=[
            S("Area within the range", math=r"\pi \times 8^2 \approx 201 \text{ km}^2"),
            S("Customers within the range", math=r"201 \times 50 \approx 10\,050 > 6\,000", text="The threshold is reached, so the pharmacy is viable."),
            S("Minimum range", math=r"\pi r^2 \times 50 = 6\,000 \;\Rightarrow\; r = \sqrt{\frac{120}{\pi}} \approx 6.2 \text{ km}"),
        ], check=r"\pi \times 6.18^2 \times 50 \approx 6\,000"),
        H("Periodic markets: threshold and range in Cameroon"),
        T("In many rural parts of Cameroon, markets are held on a fixed day of the week in each village, in a rotating cycle. "
          "Central place ideas explain why. In a poor, thinly populated area, the threshold for a full-time shop may be larger "
          "than the number of customers within walking range. By moving from market to market on different days, a trader adds "
          "up the customers of several places and reaches the threshold, while each buyer travels only a short distance. As "
          "incomes, density and roads improve, periodic markets often become daily markets and permanent shops."),
        H("Evaluating the theory"),
        KEY("Strengths and weaknesses", "Weigh both sides.", cards=[
            ["Strengths", "Explains why settlements form a hierarchy and why the number of centres falls as their order rises; introduced threshold and range, which are used in retail planning; has guided planned settlement, as in the Dutch IJsselmeer polders; fits some flat farming regions fairly well."],
            ["Weaknesses", "Assumptions are unrealistic: relief, rivers and resources are uneven; population is clustered; transport follows routes, not all directions; people combine trips and do not always use the nearest centre; governments and history shape towns; cars, supermarkets and online shopping have changed ranges. Lösch later modified the theory with a more flexible pattern."],
        ]),
        MISTAKE("Confusing threshold with range", "Threshold is a number of people (or amount of spending); range is a distance. A service needs enough people within its range."),
        MISTAKE("Getting K = 3 wrong", "In K = 3 the lower-order centres are at the corners of the higher-order hexagon (shared by three), not at the midpoints of the sides (that is K = 4)."),
        QUIZ("Which principle places lower-order centres on the straight routes between higher-order centres?", ["K = 3 marketing", "K = 4 traffic", "K = 7 administrative", "Rank-size rule"], 1,
             "The traffic principle (K = 4) puts as many centres as possible on straight routes, at the midpoints of the hexagon's sides.", hint="Which principle is about transport?",
             feedback=["K = 3 puts lower-order centres at the corners, sharing customers among three centres.", "", "K = 7 keeps lower-order centres wholly inside one administrative area.", "The rank-size rule concerns city populations, not spacing."]),
        QUIZ("A service has a threshold of 3 000 people. The population density is 40 per km² and the range is 5 km. About how many customers live within the range?", ["About 200", "About 3 140", "About 630", "About 7 850"], 1,
             "π × 5² × 40 ≈ 78.5 × 40 ≈ 3 140, just above the threshold.", hint="Area of a circle with radius equal to the range, times density.",
             feedback=["That is 5 × 40, using the radius instead of the area.", "", "That is π × 5 × 40, forgetting to square the range.", "That is 78.5 × 100; the density is 40, not 100."]),
        TIP("Central place theory appears in Paper 1 (definitions, K values, hexagons) and Paper 2 essays ('Examine the relevance of Christaller's theory'). Fieldwork on shopping or service catchments in Paper 3 uses threshold and range. Draw the hexagons neatly and state the assumptions.", title="Exam link"),
        PQ("Explain why Christaller's market areas are hexagonal rather than circular.",
           "On an isotropic plain each centre would serve a circle with radius equal to the range of its goods. Circles drawn round evenly spaced centres either leave gaps (unserved people) or overlap (people with two equally near centres). Because consumers use the nearest centre and every area must be served, the overlaps are divided and the circles become hexagons, the regular shape closest to a circle that covers a plane completely without gaps or overlaps."),
        PQ("In a K = 4 system with one top-order centre, how many centres are there of the second and third orders? Show your working.",
           "Market areas: 1, 4, 16. Second-order centres: 4 − 1 = 3. Third-order centres: 16 − 4 = 12. So there are 3 second-order and 12 third-order centres (16 centres in total for three levels)."),
        PQ("Assess the relevance of central place theory to the pattern of settlements and markets in Cameroon.",
           "Model plan. Introduction: summarise the theory (threshold, range, hierarchy, hexagons). Relevance: a clear hierarchy from villages to divisional towns, regional capitals and the two metropolises; high-order services (universities, specialist hospitals, embassies) only in large centres; periodic markets show threshold and range at work. Limits: relief (Western Highlands, Mount Cameroon, Adamawa), forest and rivers distort spacing; population is clustered, not even; roads and the railway concentrate towns along routes; administrative decisions created towns; Douala and Yaoundé form a binary pattern. Conclusion: the theory explains the hierarchy and periodic markets well, but not the precise spacing of centres."),
        SUM("A central place serves its sphere of influence; threshold is the minimum demand, range the maximum travel distance.",
            "Low-order goods have small thresholds and short ranges; high-order goods have large thresholds and long ranges.",
            "On an isotropic plain market areas are hexagonal, because hexagons fill space without gaps or overlaps.",
            "K = 3 (marketing), K = 4 (traffic), K = 7 (administrative); numbers of market areas grow as powers of K.",
            "The theory explains hierarchy and periodic markets but rests on unrealistic assumptions; evaluate it with real examples."),
    ],
))

# ------------------------------------------------------------------ Examination 1. Paper 1
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 1",
    title="Paper 1: answering 50 multiple-choice questions in physical and human geography",
    slug="gpl3-paper1-multiple-choice",
    minutes=23,
    summary="What the Board's 2023 report says about Paper 1, a routine for every multiple-choice question, how to handle calculation, graph and model questions, the traps in wrong options, and a revision map of the six Lower Sixth modules.",
    objectives=[
        "Describe the structure of Paper 1 as reported by the Board in 2023",
        "Apply a four-step routine: read, predict, eliminate, check",
        "Answer calculation, data, diagram and model questions quickly and accurately",
        "Plan revision with a map of the six Lower Sixth modules",
    ],
    key_concepts=["Stem", "Distractor", "Elimination", "Section A (physical)", "Section B (human)", "Data response", "Revision map"],
    blocks=[
        H("Introduction"),
        T("Paper 1 of A Level Geography (0750) is a multiple-choice paper of 50 questions, marked by machine. The Board's 2023 "
          "report describes it as divided into two sections of 25 questions each: Section A on physical geography and Section B "
          "on human geography. Each question has one correct option; there is no credit for a nearly right idea. In the KKEVO "
          "mock paper that goes with this lesson we allow 90 minutes (a KKEVO practice setting): just under two minutes a question."),
        H("What the paper covered in 2023"),
        T("The report lists how the 50 questions were shared between syllabus areas in 2023. Section A: meteorology, climatology "
          "and hydrology 8; geomorphology 7; biogeography 7; environmental issues 3. Section B: population 7; economic activity 8; "
          "settlement 7; development issues 3. The report rated the 2023 paper as more demanding than that of 2022. Economic activity "
          "and development issues are mainly Upper Sixth topics, but everything you learn in Lower Sixth can appear. The exact "
          "share may change from year to year, so revise every module."),
        H("A routine for every question"),
        KEY("Four steps", "Use them on every question until they become automatic.", cards=[
            ["1. Read the stem", "Find the command (which, NOT, calculate, best explains). Note units, places and any data."],
            ["2. Predict", "Answer in your head before you look at the options. This protects you from attractive distractors."],
            ["3. Eliminate", "Cross out options you can prove wrong. Ask: which misconception is this option built on?"],
            ["4. Check", "Re-read the stem with your chosen option. For calculations, check units and size."],
        ]),
        T("If a question takes more than about two minutes, choose your best option, mark the question and move on. Return to it at "
          "the end. Never leave a question blank; follow your teacher's guidance for the live paper."),
        H("Kinds of question"),
        KEY("Types you will meet", "Each has its own method.", cards=[
            ["Definitions and terms", "Infiltration capacity, albedo, catena, threshold, primate city. Learn precise definitions: options often differ by one word."],
            ["Models and theorists", "Match the idea to the author: Burgess, Hoyt, Christaller, Malthus, Boserup, Lee, Todaro, Gersmehl, Hjulström, Köppen."],
            ["Calculations", "Density, birth and death rates, dependency ratio, Rn, rank-size, gradient, sinuosity, hydraulic radius, albedo. Write the formula first."],
            ["Data and diagrams", "Hydrographs, climographs, pyramids, DTM, Hjulström curve, soil profiles, urban model diagrams. Read axes and labels before the options."],
            ["Cause and effect", "Which factor best explains a pattern? Choose the most direct cause, not a true but unrelated fact."],
        ]),
        EX("Worked example 1: a calculation", intro="A country has a CBR of 38 per 1 000 and a CDR of 11 per 1 000. Its approximate doubling time is: A 2.7 years, B 26 years, C 7 years, D 70 years.", steps=[
            S("Predict", text="Natural increase = (38 − 11) ÷ 10 = 2.7%. Doubling time ≈ 70 ÷ 2.7."),
            S("Calculate", math=r"\frac{70}{2.7} \approx 26 \text{ years}"),
            S("Eliminate", text="A is the growth rate itself. C is 70 ÷ 10 (the death rate rounded). D is the constant of the rule. The answer is B."),
        ], check=r"1.027^{26} \approx 2.0"),
        EX("Worked example 2: a model question", intro="'In a large city, heavy industry lies near the port, a university forms a second centre, and an outlying business district has grown around a ring-road junction.' Which model does this fit best? A Burgess, B Hoyt, C Harris and Ullman, D Christaller.", steps=[
            S("Predict", text="Several separate centres: multiple nuclei."),
            S("Eliminate", text="Burgess has one centre and rings; Hoyt has one centre and sectors; Christaller explains the spacing of towns, not land use inside a city."),
            S("Answer", text="C, Harris and Ullman."),
        ]),
        H("Traps in wrong options"),
        KEY("Common distractors", "Each is built on a real mistake.", cards=[
            ["Reversed", "Geometric for arithmetic, push for pull, wet-point for dry-point, inner for outer bend."],
            ["Neighbouring idea", "Urban growth for urbanization; suburbanization for counter-urbanization; range for threshold; drought for desertification."],
            ["Unfinished calculation", "The natural increase instead of the doubling time; the area instead of the density."],
            ["True but irrelevant", "A correct statement that does not answer this stem."],
            ["Absolute words", "Always, never, only: rarely true in geography."],
        ]),
        H("Revision map of the six Lower Sixth modules"),
        CODE("Module                                   Be ready for\n"
             "Hydrology & Fluvial Geomorphology        basin stores and flows, hydrographs, regimes,\n"
             "                                         Hjulstrom, landforms, sinuosity, rejuvenation\n"
             "Meteorology & Climatology                layers, heat budget, albedo, lapse rates,\n"
             "                                         tricellular model, ITCZ, air masses, Koppen,\n"
             "                                         urban heat island, climate change\n"
             "Biogeography & Pedology                  Jenny's factors, horizons, ferralitization,\n"
             "                                         podzolization, catenas, selva and savanna,\n"
             "                                         Gersmehl, seres\n"
             "Tectonic, Slope, Coastal & Arid          plates, weathering, factor of safety, waves,\n"
             "                                         longshore drift, reefs, sea level, deserts\n"
             "Population & Migration                   densities, vital rates, DTM, pyramids,\n"
             "                                         Malthus/Boserup/Simon, Ravenstein/Lee/Todaro\n"
             "Settlement & Urban                       site, Rn, urbanization, urban models,\n"
             "                                         rank-size, primacy, central places", "text", title="Table 1. Lower Sixth revision map"),
        MISTAKE("Choosing a true statement that answers a different question", "Many distractors are true facts. Ask whether the option answers this stem: 'Which factor best explains...?' needs the most direct cause."),
        MISTAKE("Rushing data questions", "Read the title, axes, units and key of every graph or table before you read the options. Many errors come from reading the wrong line or axis."),
        QUIZ("A question asks: 'Which of the following is NOT a positive check in Malthus's theory?' What should you look for?", ["The first option that is a positive check", "The option that is a preventive check or not a check at all", "The longest option", "Any option containing the word 'famine'"], 1,
             "A NOT question asks for the one option that does not belong, here a preventive check such as delayed marriage.", hint="What is a NOT question asking for?",
             feedback=["The positive checks are the three wrong answers.", "", "Length tells you nothing.", "Famine is a positive check, so it is not the answer."]),
        QUIZ("Twelve villages lie in an area of 75 km² with a mean nearest neighbour distance of 1.25 km. Rn is about:", ["0.5", "1.0", "2.0", "1.5"], 1,
             "Rn = 2 × 1.25 × √(12 ÷ 75) = 2.5 × 0.4 = 1.0: a random pattern.", hint="Find √(n ÷ A) first.",
             feedback=["That is half the correct value; check the factor of 2.", "", "That doubles the correct value.", "Check √(12 ÷ 75) = √0.16 = 0.4."]),
        TIP("Work through the whole paper once, answering everything you are sure of. Use the time left for marked questions, and keep the last 5 to 10 minutes to check that every question has an answer.", title="Exam link"),
        PQ("A river's channel between two points is 9.0 km long; the straight-line distance is 6.0 km. Its sinuosity is: A 0.67, B 1.5, C 3.0, D 15.0.",
           "Sinuosity = channel length ÷ straight-line distance = 9.0 ÷ 6.0 = 1.5, so B. A is the inverse. C is the difference. D is the sum."),
        PQ("The largest city in a country has 3 000 000 people. Under the rank-size rule the 6th city should have: A 18 000 000, B 2 994 000, C 500 000, D 600 000.",
           "3 000 000 ÷ 6 = 500 000, so C. A multiplies by 6, B subtracts 6 000, D divides by 5 (the 5th city)."),
        PQ("List four kinds of distractor used in multiple-choice questions and say how to avoid each.",
           "Reversed ideas (check the direction in the stem); neighbouring ideas such as range and threshold (learn exact definitions); unfinished calculations (finish every step and check units); true but irrelevant statements (ask whether the option answers this stem). Absolute words such as always and never are also suspicious."),
        SUM("Paper 1 has 50 multiple-choice questions; in 2023 the report described 25 physical (Section A) and 25 human (Section B).",
            "Use the routine: read the stem, predict, eliminate, check; never leave a blank.",
            "Learn definitions, model authors and formulas; read every graph's axes and units first.",
            "Distractors are reversed, neighbouring, unfinished, irrelevant or absolute.",
            "Revise all six Lower Sixth modules; the KKEVO mock allows 90 minutes as a practice setting."),
    ],
))

# ------------------------------------------------------------------ Examination 2. Paper 2
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 2",
    title="Paper 2: structured essays in physical, human and contemporary geography",
    slug="gpl3-paper2-structured-essays",
    minutes=25,
    summary="The structure of Paper 2 as described in the Board's 2023 report, how to read command words, define precisely, answer exactly the aspect asked, explain factors on both sides, tie solutions to problems, use Cameroon examples and plan model answers.",
    objectives=[
        "Describe the sections of Paper 2 as reported by the Board in 2023",
        "Interpret command words and answer exactly the aspect the question asks",
        "Build paragraphs that define, explain, illustrate and evaluate, with Cameroonian and world examples",
        "Avoid the errors the 2023 report identified, and plan answers in the time available",
    ],
    key_concepts=["Command word", "Precise definition", "Digression", "Two-sided explanation", "Problem-solution link",
                  "Case study", "Essay plan", "Evaluation"],
    blocks=[
        H("Introduction"),
        T("Paper 2 tests your understanding of the concepts and theories of physical and human geography in written answers. The "
          "Board's 2023 report describes a paper of seven questions in three sections: Section A, physical geography (meteorology, "
          "climatology and hydrology; geomorphology; biogeography); Section B, human geography (population; economic activity; "
          "settlement); and Section C, contemporary environmental and development issues, with an 'either' and an 'or' question. "
          "Questions are structured into parts such as (a), (b) and (c). Check with your teacher how many questions you must "
          "answer and from which sections, since the report does not state it. In KKEVO's practice paper we allow 150 minutes (a "
          "KKEVO practice setting)."),
        T("The report also describes a 'new examination structure' in which Cameroon geography is no longer a separate branch: it "
          "is to be integrated into each branch (for example the relief of Cameroon in geomorphology, its soils and vegetation in "
          "biogeography). Expect Paper 2 questions to reward Cameroonian examples in every topic."),
        H("Read the command word"),
        KEY("Common command words", "Your answer must do what the word says.", cards=[
            ["Describe", "Say what something is like or what a pattern shows, with figures and places. No reasons needed."],
            ["Explain / account for", "Give reasons, causes or processes: why or how something happens."],
            ["Examine / discuss", "Explain several points and look at them from more than one side, with evidence."],
            ["Assess / evaluate / to what extent", "Weigh strengths and limits and reach a supported judgement."],
            ["Illustrate", "Use a labelled diagram, graph or map, or a specific example, as the question requires."],
        ]),
        H("What the 2023 report warned about"),
        KEY("Errors and the fix for each", "Paraphrased from the examiners' comments.", cards=[
            ["Bald definitions", "One-line definitions are not accepted at A Level. Define fully, with the key process or measure, then apply it."],
            ["Digression", "Candidates wrote about all factors of rainfall when asked about latitude, or about all selectivity when asked about sex. Answer only the aspect named."],
            ["Not illustrating", "Where the question says illustrate, draw the graph or map; many did not."],
            ["One-sided explanations", "Explain how a factor can both encourage and hinder (for example transport connectivity)."],
            ["Solutions without problems", "Name each problem and tie a measure to it (ageing, urban traffic, waste)."],
            ["Confusing similar concepts", "Urbanization and suburbanization; drought and desertification; agglomeration and linkages; models of Rostow and the DTM."],
            ["Characteristics instead of significance", "When asked for the significance of a model, explain its usefulness, not its stages."],
            ["General effects", "When asked about effects on local communities, name the community and the effect on it."],
        ]),
        H("Building a strong answer"),
        T("Open with a short introduction that defines the key terms precisely and states the direction of your answer. Then write "
          "one paragraph per point: make the **point**, **explain** it (process, cause or mechanism), give an **example** (a named "
          "place, preferably Cameroonian, or a figure), and **link** it back to the question. Add evaluation where the command needs "
          "it: limits, exceptions, how important the factor is compared with others. End with a conclusion that answers the "
          "question directly. Diagrams must be large, neat, titled and labelled, and you must refer to them in the text."),
        EX("Worked example 1: a physical geography part", intro="Plan: 'Explain how the form and intensity of precipitation influence the rate of interception.'", steps=[
            S("Define", text="Interception is the capture of precipitation by vegetation (leaves, stems) before it reaches the ground; the interception store fills to a maximum capacity and the rest drips or flows down as throughfall and stemflow."),
            S("Intensity", text="Light, gentle rain is largely held on leaves and later evaporates, so a high percentage is intercepted. In intense convective storms, common in southern Cameroon, the store fills in minutes and most water passes through, so the percentage intercepted falls even though the amount held may be similar."),
            S("Duration and form", text="Long, steady rain fills the store and then interception stops rising. Form matters too: fine drizzle and mist are captured efficiently by leaves; large raindrops splash through; snow can build up on branches in cold climates."),
            S("Stay on the question", text="Do not drift into infiltration, soil or relief: they do not answer 'form and intensity of precipitation'. This was a digression noted by examiners."),
        ]),
        EX("Worked example 2: a human geography part", intro="Plan: 'Discuss three significances of the demographic transition model.'", steps=[
            S("Introduction", text="Define the DTM as a model of changing birth and death rates and total population as a country develops, in five stages."),
            S("Significance 1: comparison", text="It places countries in stages so they can be compared (Cameroon late stage 2 or stage 3; Japan stage 5)."),
            S("Significance 2: prediction and planning", text="It helps forecast growth and age structure, so governments plan schools and jobs in stages 2 and 3, pensions and care in stages 4 and 5."),
            S("Significance 3: policy", text="It suggests what lowers fertility (lower infant mortality, education of girls, family planning), guiding population policy."),
            S("Evaluate and conclude", text="It is based on European experience, ignores migration and has no time scale, so it guides rather than predicts exactly. Do not list the stages as the answer and do not confuse it with Rostow."),
        ]),
        H("Managing the paper"),
        T("Read all the questions you may choose from before starting. Choose questions where you can answer every part, not only "
          "part (a). Divide your time in proportion to the parts and keep a few minutes to re-read. Write in clear, simple English "
          "and legible handwriting; the report asks candidates to take care with both."),
        MISTAKE("Answering the topic, not the question", "A question on suburbanization in developed countries is not a question on rural-urban migration in Cameroon. Underline the key words and test every paragraph against them."),
        MISTAKE("Measures without examples", "Write 'the government' or 'the people' only with a named action and place. Distinguish measures actually taken from measures you propose."),
        QUIZ("A question asks: 'Examine two reasons for the increasing rate of suburbanization in developed countries.' Which opening is best?", [
            "Urbanization is the increase in the proportion of people living in towns.",
            "Suburbanization is the outward movement of people and activities from the inner city to the edges of the built-up area; two reasons are growing car ownership and the desire for larger, cheaper homes.",
            "Rural-urban migration in Cameroon is caused by push and pull factors.",
            "Suburbs are areas near cities."], 1,
            "It defines the right concept fully and states the two reasons that the essay will examine.",
            hint="Which opening defines the exact concept asked and sets out the answer?",
            feedback=["That defines the wrong concept, a digression the report noted.", "", "That is about a different process and a different region.", "That is a bald definition with no process."]),
        QUIZ("Which paragraph structure best suits an 'explain' question?", ["Point, explanation, example, link", "Example only", "List of points with no explanation", "Conclusion first, then points without reasons"], 0,
             "Each point must be explained and supported with an example, then linked to the question.", hint="What makes a point an explanation?",
             feedback=["", "An example without a point or reason earns little.", "A list does not explain.", "A judgement needs reasons and evidence."]),
        TIP("Revise each topic as three things: precise definitions, explained points with examples (including Cameroon), and evaluation. That is what Paper 2 marks reward.", title="Exam link"),
        PQ("Rewrite this bald definition as an A Level definition: 'An ageing population is when there are many old people.'",
           "An ageing population is one in which the proportion of people aged 65 and over, and the median age, are rising over time, because fertility is falling and life expectancy is increasing; it raises the old-age dependency ratio."),
        PQ("Plan an answer to: 'Examine three factors that influence the site of early rural settlements.'",
           "Introduction: define site (the land a settlement occupies) and contrast with situation. Factor 1: water supply, wet-point sites near springs and rivers in dry areas; dry-point sites on terraces and levees above floodplains; example. Factor 2: defence, hilltops and meanders; Mandara Mountains example. Factor 3: relief and soils, gentle well-drained slopes and fertile volcanic or alluvial soils; Western Highlands example. Evaluation: factors combine; modern technology reduces their importance. Conclusion."),
        PQ("Distinguish between drought and desertification in two sentences.",
           "A drought is a temporary period of well-below-average rainfall that causes water shortage, after which conditions can recover. Desertification is the long-term degradation of land in dry areas into desert-like conditions, caused by climatic variation and human activities such as overgrazing, over-cultivation and deforestation."),
        SUM("In 2023 the report described Paper 2 as seven structured questions in Section A (physical), Section B (human) and Section C (contemporary issues, either/or); check the choice rules with your teacher.",
            "Obey the command word: describe, explain, examine, assess, illustrate.",
            "Define fully, answer only the aspect asked, explain both sides, and tie every solution to a problem.",
            "Use point, explanation, example, link; add evaluation and a clear conclusion.",
            "Integrate Cameroon examples in every branch, as the new examination structure expects."),
    ],
))

# ------------------------------------------------------------------ Examination 3. Paper 3
LESSONS.append(lesson(
    module=M_EXAM,
    topic="Paper 3",
    title="Paper 3: map work, statistics, fieldwork and the geography of Cameroon",
    slug="gpl3-paper3-mapwork-fieldwork",
    minutes=25,
    summary="Paper 3 as described in the Board's 2023 report: map-work description and calculations (gradient, vertical exaggeration, sinuosity), the interquartile range and graphs, writing up fieldwork, and answering Cameroon questions with concrete examples.",
    objectives=[
        "Describe the sections of Paper 3 as reported by the Board in 2023",
        "Calculate and interpret gradient, vertical exaggeration, sinuosity and the interquartile range",
        "Describe relief and drainage from map evidence only and relate features to each other",
        "Write a fieldwork report with a clear objective, hypothesis, method, presentation and conclusion",
    ],
    key_concepts=["Map evidence", "Gradient", "Vertical exaggeration", "Sinuosity", "Interquartile range", "Hypothesis",
                  "Objective", "Sketch map"],
    blocks=[
        H("Introduction"),
        T("Paper 3 applies geographical knowledge to maps, data and the real world. The Board's 2023 report describes seven "
          "questions in three sections: Section A, map work (one compulsory question on physical and human aspects of a "
          "topographic map); Section B, fieldwork and techniques (two questions: one on fieldwork, one on statistical or graphical "
          "techniques); and Section C, the geography of Cameroon (four questions). Check with your teacher how many questions you "
          "answer in Sections B and C. In 2023, map work averaged about half marks, and the statistics question was the least "
          "popular. KKEVO's practice paper allows 150 minutes (a KKEVO practice setting)."),
        H("Map work: use map evidence"),
        T("The report's main advice is to answer **from the map**. When describing relief, cover four elements: **height** (spot "
          "heights and contour values), **slope** (gentle or steep, from contour spacing), **landforms** (hill, spur, valley, "
          "plateau, scarp) and **orientation** (which way the land slopes or a ridge runs). Divide the map into sections using "
          "eastings, northings or relief regions, as the report recommends, and compare them. Then relate features: settlements "
          "on flood-free ground, roads following valleys, swamps on flat valley floors, plantations on gentle slopes."),
        IMG("algpl3-map-extract.svg", alt="Map extract with 1 km grid squares, eastings 52 to 58 and northings 30 to 34. Summit A, 620 m, at 530330 is ringed by contours 600 to 400 m. Point B, 380 m, lies on a north-south river at 560330. A road crosses the south past a village",
            caption="Figure 1. Schematic map extract (invented). Contours every 50 m from 400 m to 600 m; scale 1:50 000; grid squares 1 km."),
        F(r"\text{gradient} = \frac{\text{vertical interval (difference in height)}}{\text{horizontal equivalent (distance)}}", title="Gradient (same units top and bottom)"),
        EX("Worked example 1: gradient from A to B", intro="Using Figure 1, find the average gradient from A (620 m) to B (380 m).", steps=[
            S("Horizontal distance", text="A is at easting 53, B at easting 56 on the same northing: 3 grid squares = 3 km = 3 000 m."),
            S("Vertical interval", math=r"620 - 380 = 240 \text{ m}"),
            S("Gradient", math=r"\frac{240}{3\,000} = \frac{1}{12.5} \;\text{ i.e. } 1 \text{ in } 12.5 \;(8\%)"),
            S("Interpret", text="A moderate slope, falling eastward from the summit to the river: a road up to A would need bends, and the river valley floor near B is the easiest route north-south."),
        ], check=r"\frac{3\,000}{240} = 12.5"),
        F(r"\text{VE} = \frac{\text{vertical scale}}{\text{horizontal scale}} = \frac{\text{horizontal scale denominator}}{\text{vertical scale denominator}}", title="Vertical exaggeration"),
        EX("Worked example 2: vertical exaggeration and sinuosity", intro="(a) A cross-section from a 1:50 000 map uses a vertical scale of 1 cm to 50 m. Find the vertical exaggeration. (b) Between two points a river channel measures 7.2 km and the straight line between them 4.8 km. Find the sinuosity.", steps=[
            S("Vertical scale as a ratio", math=r"1 \text{ cm} : 50 \text{ m} = 1 \text{ cm} : 5\,000 \text{ cm} = 1:5\,000"),
            S("VE", math=r"\frac{50\,000}{5\,000} = 10", text="Heights are drawn ten times steeper than reality; state this under the section."),
            S("Sinuosity", math=r"\frac{7.2}{4.8} = 1.5", text="1 means straight; values of about 1.5 or more are usually called meandering (check your textbook's classes). The report noted that many candidates calculated sinuosity correctly but could not say what the value meant: always interpret it."),
        ], check=r"4.8 \times 1.5 = 7.2"),
        H("Statistical and graphical techniques"),
        T("The 2023 statistics question asked for an interquartile range, a choropleth and a climograph (rainfall bars and a "
          "temperature line). The report recommends that statistics be taught in Lower Sixth before fieldwork. Every graph needs a "
          "title, labelled axes with units, a sensible scale and a key."),
        EX("Worked example 3: interquartile range", intro="The number of shops in 11 settlements (invented) is: 12, 15, 18, 20, 22, 25, 27, 30, 34, 38, 45. Find the median and the interquartile range.", steps=[
            S("Order and n", text="The data are already in order; n = 11."),
            S("Median", math=r"\frac{n + 1}{2} = 6\text{th value} = 25"),
            S("Quartiles", math=r"Q_1 = \frac{n+1}{4} = 3\text{rd value} = 18; \quad Q_3 = \frac{3(n+1)}{4} = 9\text{th value} = 34"),
            S("IQR", math=r"34 - 18 = 16", text="The middle half of the settlements have between 18 and 34 shops. Unlike the range (45 − 12 = 33), the IQR is not distorted by the extreme values. Some textbooks use slightly different quartile rules; follow your teacher's."),
        ]),
        H("Writing up fieldwork"),
        KEY("A fieldwork report the examiners reward", "Based on the report's comments on the 2023 fieldwork question.", cards=[
            ["Location", "A sketch map with title, frame, north arrow, scale and key."],
            ["Objective and hypothesis", "Objective: what you set out to do ('to investigate how channel velocity changes downstream'). Hypothesis: a testable statement ('velocity increases downstream'). Many candidates confused the two."],
            ["Tools and methods", "Name each tool and its use (float and stopwatch for velocity; ranging poles; questionnaire), and the sampling method, step by step."],
            ["Presentation and analysis", "Real, titled tables and graphs with labelled axes; statistics where relevant."],
            ["Findings and conclusion", "Accept or reject the hypothesis using your results; explain the results; state problems met; and say why the study matters to the local community."],
        ]),
        H("The geography of Cameroon"),
        T("Answer with concrete Cameroonian examples: named regions, towns, rivers, crops, industries and projects. The report "
          "notes that many candidates gave general answers without examples, or described Cameroon's major climates in general "
          "when asked to contrast two named regions such as the South Cameroon Plateau and the Adamawa Plateau. When asked about measures, separate measures actually taken from measures you would "
          "propose, and match each to a problem. Use sketch maps to show distributions."),
        MISTAKE("Using outside knowledge when the question says 'map evidence only'", "If the question asks for map evidence, every point must be something you can see on the map: contours, spot heights, symbols, names, grid references."),
        MISTAKE("Calculating without interpreting", "A gradient, sinuosity value or IQR needs one sentence of meaning: steep or gentle, meandering or straight, spread wide or narrow."),
        QUIZ("A cross-section from a 1:25 000 map is drawn with a vertical scale of 1 cm to 25 m. What is the vertical exaggeration?", ["1", "10", "25", "100"], 1,
             "1 cm to 25 m = 1:2 500. VE = 25 000 ÷ 2 500 = 10.", hint="Convert 25 m into centimetres first.",
             feedback=["That would need equal scales.", "", "That confuses the 25 m with the exaggeration.", "That forgets that 25 m is 2 500 cm."]),
        QUIZ("Which is a hypothesis rather than an objective?", ["To investigate land use along a transect from the CBD", "To measure stream velocity at five sites", "Land values decrease with distance from the CBD", "To find out how traders choose market sites"], 2,
             "A hypothesis is a statement that can be tested and accepted or rejected.", hint="Which option is a statement rather than an aim beginning 'to'?",
             feedback=["That is an objective (an aim).", "That is a method or objective.", "", "That is an objective (an aim)."]),
        TIP("Map work is compulsory and carries great weight: practise on real topographic sheets of Cameroon every week. Learn the formulas for gradient, vertical exaggeration, sinuosity, density, Rn and the IQR, and always interpret your answer.", title="Exam link"),
        PQ("On a 1:50 000 map, two points 4.5 km apart have heights of 520 m and 340 m. Calculate the average gradient.",
           "Vertical interval = 520 − 340 = 180 m. Horizontal equivalent = 4 500 m. Gradient = 180 ÷ 4 500 = 1 ÷ 25, i.e. 1 in 25 (4%), a gentle slope."),
        PQ("Rainfall totals (mm) at nine stations are: 1 450, 1 520, 1 600, 1 680, 1 750, 1 820, 1 900, 2 100, 2 600. Find the median and interquartile range.",
           "n = 9. Median = 5th value = 1 750 mm. Q1 = (9 + 1) ÷ 4 = 2.5th value = (1 520 + 1 600) ÷ 2 = 1 560 mm. Q3 = 7.5th value = (1 900 + 2 100) ÷ 2 = 2 000 mm. IQR = 2 000 − 1 560 = 440 mm."),
        PQ("State a suitable objective and a hypothesis for a fieldwork study of a river near your school.",
           "Objective: to investigate how the width, depth and velocity of the river change downstream between the source area and the school. Hypothesis: the velocity of the river increases downstream. (The hypothesis must be a testable statement; the objective is the aim of the study.)"),
        SUM("In 2023 Paper 3 had compulsory map work (Section A), fieldwork and techniques (Section B) and Cameroon geography (Section C).",
            "Describe relief by height, slope, landforms and orientation; use map evidence and relate features.",
            "Gradient = vertical interval ÷ horizontal distance; VE = horizontal scale denominator ÷ vertical scale denominator; sinuosity = channel ÷ straight length.",
            "IQR = Q3 − Q1; every graph needs a title, labelled axes, units and a key.",
            "Fieldwork: location map, objective versus hypothesis, tools, method, presentation, findings against the hypothesis, problems and community value."),
    ],
))
